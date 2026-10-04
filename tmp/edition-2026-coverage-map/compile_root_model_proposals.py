"""Publish finite source allocations for the fourteen reserved model-theory goals."""
from pathlib import Path
import csv
import copy
import hashlib
import json
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "spec/coverage/edition-2026"
sys.path.insert(0, str(ROOT / "tools"))
import check as grammar

def rows(name):
    return [json.loads(line) for line in (DEST/name).read_text(encoding="utf-8-sig").splitlines() if line.strip()]

requirements = {r["original_requirement_id"]: r for r in rows("requirements-crosswalk.jsonl")}
units = {r["unit_id"]: r for r in rows("requirements-units.jsonl")}
profiles = json.loads((DEST/"root-model-goal-profiles.json").read_text(encoding="utf-8"))["profiles"]
identities = json.loads((DEST/"model-theory-additional-identities.json").read_text(encoding="utf-8"))
extra = {r["key"]: r for r in identities["sources"]}
with (DEST/"root-model-source-allocations.tsv").open(encoding="utf-8", newline="") as stream:
    allocations = list(csv.DictReader(stream, delimiter="\t"))
assert len(profiles) == 14 and len(allocations) == 42
assert {p["id"] for p in profiles} == {f"N-a-{n:03}" for n in range(1,15)}

bibtext = (ROOT/"handbook/bib/handbook.bib").read_text(encoding="utf-8-sig")
bib = {}
for match in re.finditer(r"@[A-Za-z]+\s*\{", bibtext):
    args, end = grammar.scan_braced_args(bibtext, match.end()-1, 1)
    if args and "," in args[0]:
        key = args[0].split(",",1)[0].strip()
        bib[key] = {"key":key, "path":"handbook/bib/handbook.bib", "line":bibtext.count("\n",0,match.start())+1,
                    "literal_record":bibtext[match.start():end]}

def identity(key):
    if key in extra:
        return extra[key]
    if key in bib:
        return bib[key]
    raise ValueError("Unidentified exact citation key: " + key)

anchors = {}
paths = {ROOT/"handbook/parts/p03"/name for name in [
    "classification-theory.tex", "preservation-abstract-logic.tex",
    "types-ultraproducts-supplement.tex", "qe-categoricity-games-supplement.tex",
    "ultrafilter-choice-and-source-boundary.tex"]}
paths.add(ROOT/"handbook/restoration/inherited-07295-07468.tex")
for path in sorted(paths):
    literal = path.read_text(encoding="utf-8-sig")
    text = grammar.strip_verbatims(grammar.strip_comments(literal))
    rel = path.relative_to(ROOT).as_posix()
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    for match in grammar.HB_ENV_RE.finditer(text):
        env = match.group(1)
        arity = 3 if env in grammar.HB_STATUS_ENVS or env == "annexitem" else 2
        args, end = grammar.scan_braced_args(text, match.end(), arity)
        if len(args) != arity:
            continue
        close = text.find("\\end{"+env+"}",end)
        anchors.setdefault(args[0],[]).append({"path":rel,"line":text.count("\n",0,match.start())+1,
            "label":args[0],"sha256":digest,"kind":env,"title":args[-1],
            "declared_status":args[1] if env in grammar.HB_STATUS_ENVS else None,
            "declaration_text":text[end:close] if close >= 0 else None})

proposals = []
for p in profiles:
    rid = p["id"]
    original = requirements[rid]
    assigned = [a for a in allocations if a["id"] == rid]
    assert len(assigned) == len(original["unit_ids"])
    for ordinal, a in enumerate(assigned,1):
        assert int(a["ordinal"]) == ordinal
        identity(a["key"])
    present = []
    for label in p["anchors"]:
        matches = anchors.get(label,[])
        if len(matches) != 1:
            raise ValueError(f"{rid}: {label} has {len(matches)} bindings")
        present.append(matches[0])
    parent_ids = sorted({c["component_id"] for uid in original["unit_ids"] for c in units[uid]["required_components"]})
    components = []
    for n, c in enumerate(p["components"],1):
        assert c["sources"] and all(1 <= i <= len(assigned) for i in c["sources"])
        components.append({"component_id":f"{rid}-MAP-{n:02}","parent_component_ids":parent_ids,
            "description":c["text"],"source_ordinals":c["sources"],
            "success_condition":"Complete the exact stated subgoal: " + c["text"],
            "failure_condition":p["failure"],
            "required_source_extent":[{"source_key":assigned[i-1]["key"],"extent":assigned[i-1]["required_extent"],
                "scope_conditions":assigned[i-1]["conditions"]} for i in c["sources"]]})
    additional = [{**a,"bibliographic_identity":identity(a["key"]),"allocation_standing":"Explicit bounded dependency/evidence obligation; the named extent remains to be completed or checked."} for a in p["additional"]]
    related = [{**r,"unit_ids":requirements[r["id"]]["unit_ids"]} for r in p["related"]]
    patches = []
    for ordinal, a in enumerate(assigned,1):
        uid = original["unit_ids"][ordinal-1]
        assert uid == f"ED26-REQ-{rid}-{ordinal:02}"
        old = units[uid]
        selected = [c for c in components if ordinal in c["source_ordinals"]]
        assert selected
        body = f"handbook/parts/p03/presentations/{rid.lower()}-{ordinal:02}.tex"
        annex = f"handbook/annex/p03/{rid.lower()}-{ordinal:02}.tex"
        label = f"sec:p03-{rid.lower()}-{ordinal:02}"
        primary = {"source_id":a["key"],"original_source_literal":old["source_presentations"][0]["source_id"],
            "bibliographic_identity":identity(a["key"]),"version":"Exact publication/edition identified by the preserved record and additional identity decisions",
            "precise_extent":a["required_extent"],"source_role":a["source_role"],"conditions":a["conditions"],
            "allocated_subcomponent_ids":[c["component_id"] for c in selected],
            "identity_evidence_paths":["spec/coverage/edition-2026/model-theory-additional-identities.json","spec/coverage/edition-2026/root-model-source-allocations.tsv"],
            "body_acquisition_standing":"The exact original source body, all required dependencies and any corrigenda remain to be qualified before source-specific writing is accepted; bibliographic identity alone is not body credit."}
        patch = copy.deepcopy(old)
        patch["source_presentations"] = [primary]
        patch["required_components"] = []
        for old_component in old["required_components"]:
            component = copy.deepcopy(old_component)
            component["required_source_extent"] = {"original_scope":original["original_register_row"],"precise_extent":a["required_extent"],
                "source_key":a["key"],"source_role":a["source_role"],"conditions":a["conditions"],"standing":"resolved finite source allocation"}
            component["allocated_subcomponent_ids"] = [c["component_id"] for c in selected]
            component["success_condition"] = "Complete this source's actual named presentation and the allocated subcomponents, preserving its own proof scope: " + a["required_extent"]
            component["failure_condition"] = p["failure"] + " " + a["conditions"]
            patch["required_components"].append(component)
        patch["required_subcomponents"] = selected
        patch["prerequisites"] = [{"named_premise":s,"role":"internal_setup","supply_rule":"Define and supply the exact needed lemma in this treatment or explicitly bind a previously completed proof before use; no unspecified external result is assumed."} for s in p["setup"]]
        patch["prerequisites"] += [{"named_premise":d["extent"],"source_key":d["key"],"role":d["role"],"bibliographic_identity":d["bibliographic_identity"],"required_source_extent":d["extent"]} for d in additional]
        patch["reader_interfaces"] = related
        patch["destination"] = {"body":{"existing_common_goal_anchors":present,"proposed_source_presentation":body,"proposed_label":label},
            "annex":{"proposed_source_proof_destination":annex,"label_prefix":f"annex:p3.{rid.lower()}.{ordinal}"},
            "lookup":{"body_path":body,"entry_label":label,"keys":[rid,a["key"],original["original_wording"]]}}
        patch["destination_rule"] = "Reuse an existing exact source treatment where present and route these disjoint destinations only for missing material; a topic-level match does not establish source identity."
        patch["source_state"] = "identified_missing"
        patch["source_state_explanation"] = "A qualified complete body for this exact allocated original version and proof extent is not established by this root proposal. Held artifacts may satisfy later acquisition checks; their existence is not denied."
        if a["key"] == "Hodges1993":
            patch["source_state"] = "mixed"
            patch["source_state_explanation"] = "SRC-048 holds the exact contents and 2011 author corrections; complete named original book bodies remain acquisition/writing obligations."
            patch["related_source_unit_ids"] = [f"ED26-SRC-048-{n:04}" for n in ([7,17] if rid in ["N-a-001","N-a-002"] else [11,17] if rid=="N-a-008" else [6,17] if rid=="N-a-011" else [6,10,17])]
            patch["related_source_relation"] = "The same identified 1993 book and applicable corrected named extents; generic chapter headings alone do not establish exact theorem location or completed proof."
        patch["scope_state"] = "resolved"
        patch["unresolved_questions"] = []
        patch["mapping_stage"] = "root_exact_goal_and_separate_source_allocation"
        patch["remaining_work"] = list(original["current_assessment"].get("remaining_book_work",[])) + [
            "Qualify and read the exact source/version extent and all explicitly required corrections and proof dependencies.",
            "Complete every allocated unsupplied subcomponent and the source-native presentation, preserving already correct current results.",
            "Integrate the body, complete proof annex and lookup targets; retain acquisition/source identity evidence outside the reader's derivation.",
            "Submit the full completed manuscript to the later consolidated independent content and publication checks."]
        patch["evidence"] += ["spec/coverage/edition-2026/root-model-goal-profiles.json","spec/coverage/edition-2026/root-model-source-allocations.tsv","spec/coverage/edition-2026/model-theory-additional-identities.json"]
        patch["current_declaration_bindings"] = present
        patches.append(patch)
    proposals.append({"original_requirement_id":rid,"original_wording":original["original_wording"],"original_register_row":original["original_register_row"],
        "unit_ids":original["unit_ids"],"parent_component_ids_preserved":parent_ids,"required_subcomponents":components,"unit_patches":patches,
        "present_destinations":present,"original_inventory_destinations_preserved":original["present_destinations"],
        "additional_bounded_dependencies":additional,"reader_interfaces":related,
        "mapping_state":"resolved","scope_state":"resolved","unresolved_questions":[],
        "current_assessment":original["current_assessment"],"preserve_current_assessment":True,
        "remaining_work":original["current_assessment"].get("remaining_book_work",[]) + ["Complete each separate source allocation and its exact mapped subcomponents; no proof/source/publication acceptance follows from this map."]})

out = DEST/"root-new-content-proposals.jsonl"
if out.exists():
    raise SystemExit("Refusing to overwrite the published proposal batch")
out.write_text("".join(json.dumps(p,ensure_ascii=False,separators=(",",":"))+"\n" for p in proposals),encoding="utf-8")
receipt = {"requirements":len(proposals),"source_unit_patches":sum(len(p["unit_patches"]) for p in proposals),
    "mathematical_subcomponents":sum(len(p["required_subcomponents"]) for p in proposals),
    "exact_original_source_ordinals_preserved":True,"original_wording_and_assessment_preserved":True,
    "all_selected_current_anchors_unique":True,"sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
    "standing":"Finite scope proposals for shard A; manuscript authoring and independent acceptance remain separate."}
(DEST/"root-new-content-proposals-receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt,ensure_ascii=False))
