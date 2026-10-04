"""Project explicitly authored N-b-001..018 allocations onto preserved IDs."""
from pathlib import Path
import copy
import hashlib
import json
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CAT = HERE.parent
sys.path.insert(0, str(ROOT / "tools"))
import check as grammar

def readrows(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8-sig").splitlines() if x.strip()]

requirements = {r["original_requirement_id"]: r for r in readrows(CAT / "requirements-crosswalk.jsonl")}
units = {r["unit_id"]: r for r in readrows(CAT / "requirements-units.jsonl")}
profiles = json.loads((HERE / "profiles.json").read_text(encoding="utf-8"))["profiles"]
assert len(profiles) == 18
assert {p["id"] for p in profiles} == {f"N-b-{n:03}" for n in range(1, 19)}
extra = {r["key"]: r for r in json.loads((CAT / "nonclassical-additional-identities.json").read_text(encoding="utf-8-sig"))["sources"]}
bibtext = (ROOT / "handbook/bib/handbook.bib").read_text(encoding="utf-8-sig")
bib = {}
for match in re.finditer(r"@[A-Za-z]+\s*\{", bibtext):
    args, end = grammar.scan_braced_args(bibtext, match.end() - 1, 1)
    if args and "," in args[0]:
        key = args[0].split(",", 1)[0].strip()
        bib[key] = {"key": key, "path": "handbook/bib/handbook.bib", "line": bibtext.count("\n", 0, match.start()) + 1, "literal_record": bibtext[match.start():end]}

def identity(key):
    if key in extra:
        return extra[key]
    if key in bib:
        return bib[key]
    raise ValueError("Missing exact source identity: " + key)

anchors = {}
for filename in ["modal-logics-supplement.tex", "conditionals-deontic-free.tex", "temporal-epistemic-supplement.tex"]:
    path = ROOT / "handbook/parts/p08" / filename
    literal = path.read_text(encoding="utf-8-sig")
    text = grammar.strip_verbatims(grammar.strip_comments(literal))
    for match in grammar.HB_ENV_RE.finditer(text):
        env = match.group(1)
        arity = 3 if env in grammar.HB_STATUS_ENVS or env == "annexitem" else 2
        args, end = grammar.scan_braced_args(text, match.end(), arity)
        if len(args) != arity:
            continue
        close = text.find("\\end{" + env + "}", end)
        anchors.setdefault(args[0], []).append({"path": path.relative_to(ROOT).as_posix(), "line": text.count("\n", 0, match.start()) + 1, "label": args[0], "kind": env, "title": args[-1], "declared_status": args[1] if env in grammar.HB_STATUS_ENVS else None, "declaration_text": text[end:close] if close >= 0 else None, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})

evidence = ["spec/coverage/edition-2026/nonclassical-001-018/profiles.json", "spec/coverage/edition-2026/nonclassical-001-018/source-note-010-018.md", "spec/coverage/edition-2026/nonclassical-additional-identities.json", "spec/coverage/edition-2026/root-depth-profiles.tsv", "spec/research/edition-2026-map-nonclassical-001-018.md"]
proposals = []
for profile in profiles:
    rid = profile["id"]
    original = requirements[rid]
    assert len(profile["sources"]) == len(original["unit_ids"])
    current = []
    for label in profile["anchors"]:
        found = anchors.get(label, [])
        if len(found) != 1:
            raise ValueError(f"{rid}: anchor {label} has {len(found)} bindings")
        current.append(found[0])
    parents = sorted({c["component_id"] for uid in original["unit_ids"] for c in units[uid]["required_components"]})
    components = []
    for n, (description, ordinals) in enumerate(profile["components"], 1):
        assert ordinals and all(1 <= ordinal <= len(profile["sources"]) for ordinal in ordinals)
        components.append({"component_id": f"{rid}-MAP-{n:02}", "parent_component_ids": parents, "description": description, "source_ordinals": ordinals, "success_condition": "Complete the exact stated subgoal and its allocated source argument: " + description, "failure_condition": profile["failure"], "required_source_extent": [{"source_key": profile["sources"][i - 1][0], "extent": profile["sources"][i - 1][1]} for i in ordinals]})
    additional = [{"key": key, "extent": extent, "role": role, "bibliographic_identity": identity(key), "allocation_standing": "Explicit bounded dependency or existing presentation; exact body qualification and source fidelity are still required."} for key, extent, role in profile.get("additional", [])]
    related = [{"id": x, "unit_ids": requirements[x]["unit_ids"], "role": "reader_interface", "relation": "Explicit shared subject or prerequisite interface; not automatic identity of complete source presentations or an unproved proof premise."} for x in profile["related"]]
    patches = []
    for ordinal, (key, extent) in enumerate(profile["sources"], 1):
        uid = original["unit_ids"][ordinal - 1]
        assert uid == f"ED26-REQ-{rid}-{ordinal:02}"
        old = units[uid]
        selected = [c for c in components if ordinal in c["source_ordinals"]]
        assert selected
        patch = copy.deepcopy(old)
        body = f"handbook/parts/p08/presentations/{rid.lower()}-{ordinal:02}.tex"
        annex = f"handbook/annex/p08/{rid.lower()}-{ordinal:02}.tex"
        label = f"sec:p08-{rid.lower()}-{ordinal:02}"
        patch["source_presentations"] = [{"source_id": key, "original_source_literal": old["source_presentations"][0].get("original_source_literal", old["source_presentations"][0]["source_id"]), "original_source_ordinal": ordinal, "bibliographic_identity": identity(key), "version": "Exact named original publication or edition in the preserved canonical/additional identity record; no unqualified later-version substitution", "precise_extent": extent, "allocated_subcomponent_ids": [c["component_id"] for c in selected], "identification_evidence": evidence, "body_acquisition_standing": "Bibliographic and current-text evidence identifies the allocation; it does not qualify the complete source body or prove source fidelity."}]
        patch["required_components"] = []
        for old_component in old["required_components"]:
            c = copy.deepcopy(old_component)
            c["required_source_extent"] = {"original_scope": original["original_register_row"], "source_key": key, "precise_extent": extent, "standing": "resolved finite source allocation"}
            c["allocated_subcomponent_ids"] = [x["component_id"] for x in selected]
            c["success_condition"] = "Complete this source's named presentation and every allocated subcomponent, preserving source-native proof/argument boundaries: " + extent
            c["failure_condition"] = profile["failure"]
            patch["required_components"].append(c)
        patch["required_subcomponents"] = selected
        patch["prerequisites"] = [{"named_premise": s, "role": "internal_setup", "supply_rule": "Define and supply the exact needed lemma within this treatment or bind an already completed proof before use; root reconciles identifiers separately."} for s in profile["setup"]]
        patch["prerequisites"] += [{"named_premise": a["extent"], "source_key": a["key"], "role": a["role"], "bibliographic_identity": a["bibliographic_identity"], "required_source_extent": a["extent"]} for a in additional]
        patch["reader_interfaces"] = related
        patch["destination"] = {"body": {"existing_common_goal_anchors": current, "proposed_source_presentation": body, "proposed_label": label}, "annex": {"proposed_source_proof_destination": annex, "label_prefix": f"annex:p8.{rid.lower()}.{ordinal}"}, "lookup": {"body_path": body, "entry_label": label, "keys": [rid, key, original["original_wording"]]}}
        patch["destination_rule"] = "Reuse a current exact complete source treatment if established; route the disjoint proposed files only for missing material. A topic match or an unrouted annex file is not completed proof credit."
        if rid == "N-b-014" and key == "Kamp1968":
            patch["destination"]["body"]["existing_separate_source_destination"] = {"path": "handbook/parts/p09/presentations/n-c-012.tex", "label": "sec:p09-presentation-n-c-012", "relation": "Exact same identified thesis; share the complete proved source results and retain the philosophical-tense interface. This map does not independently accept the proof."}
        patch["source_state"] = "identified_missing"
        patch["source_state_explanation"] = "This mapping does not establish a fully qualified readable source body for the complete required extent. Existing held artifacts may satisfy subsequent qualification; their existence is not denied."
        patch["scope_state"] = "resolved"
        patch["unresolved_questions"] = []
        patch["mapping_stage"] = "separate_original_source_and_exact_named_goal_allocation"
        patch["current_declaration_bindings"] = current
        patch["remaining_work"] = list(original["current_assessment"].get("remaining_book_work", [])) + ["Qualify and read the exact source extent, version, corrections and required dependencies.", "Complete every unsupplied source-specific subcomponent and proof/argument, correcting active errors directly.", "Integrate body, proof annex, rule-sheet and lookup targets; retain historical correction provenance outside reader derivations.", "Submit the complete manuscript change set to the later consolidated independent review and publication checks."]
        patch["evidence"] = list(patch.get("evidence", [])) + evidence
        patches.append(patch)
    proposals.append({"original_requirement_id": rid, "original_wording": original["original_wording"], "original_register_row": original["original_register_row"], "unit_ids": original["unit_ids"], "parent_component_ids_preserved": parents, "required_subcomponents": components, "unit_patches": patches, "present_destinations": current, "original_inventory_destinations_preserved": original["present_destinations"], "additional_bounded_dependencies": additional, "reader_interfaces": related, "mapping_state": "resolved", "scope_state": "resolved", "unresolved_questions": [], "current_assessment": original["current_assessment"], "preserve_current_assessment": True, "remaining_work": original["current_assessment"].get("remaining_book_work", []) + ["Complete every separately allocated source treatment and exact subcomponent; map completion grants no proof/source/publication acceptance."]})

output = HERE / "proposals.jsonl"
if output.exists():
    raise SystemExit("Refusing to overwrite published proposals")
output.write_text("".join(json.dumps(p, ensure_ascii=False, separators=(",", ":")) + "\n" for p in proposals), encoding="utf-8")
receipt = {"requirements": len(proposals), "source_unit_patches": sum(len(p["unit_patches"]) for p in proposals), "required_subcomponents": sum(len(p["required_subcomponents"]) for p in proposals), "original_source_ordinals_and_ids_preserved": True, "original_wording_and_assessments_preserved": True, "all_selected_current_anchors_unique": True, "sha256": hashlib.sha256(output.read_bytes()).hexdigest(), "inputs": {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in [HERE / "profiles.json", HERE / "source-note-010-018.md", CAT / "nonclassical-additional-identities.json"]}, "standing": "Finite construction-map proposals; acquisition, writing, independent admission and publication remain separate."}
(HERE / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False))
