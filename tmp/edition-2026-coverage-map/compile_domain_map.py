"""Assemble the coverage-map projection from declared decisions and saved source evidence.

This is a one-purpose data transformation. It neither invokes manuscript
checks nor writes manuscript, generated reference apparatus, or admission files.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "spec/coverage/edition-2026"
sys.path.insert(0, str(ROOT / "tools"))
import check as grammar

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]

def write_jsonl(name, rows):
    path = DEST / name
    if path.exists():
        raise SystemExit(f"Preserve previous projection: {path}")
    path.write_text("".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n" for r in rows), encoding="utf-8")
    return {"path": path.relative_to(ROOT).as_posix(), "rows": len(rows), "sha256": digest(path)}

decisions = json.loads((DEST / "domain-allocation-decisions.json").read_text(encoding="utf-8"))
surfaces = read_jsonl(DEST / "new-domain-destination-evidence.jsonl")
body = {r["path"]: r for r in surfaces if re.search(r"handbook/parts/p1[5-9]/", r["path"])}
by_path = {r["path"]: r for r in surfaces}
notes = sorted((ROOT / "spec/research").glob("edition-2026-*.md"))
note_by_name = {p.stem: p for p in notes}

def find_notes(path):
    part = Path(path).parent.name
    stem = Path(path).stem
    result = [p for name, p in note_by_name.items()
              if name == f"edition-2026-{part}-{stem}"
              or (name.startswith(f"edition-2026-{part}-") and name.endswith("-" + stem))]
    if not result and stem == "risk-aversion":
        result = [note_by_name["edition-2026-p17-d2-finite-expected-utility"]]
    return result

# Preserve literal bibliographic records; a shared citation key is not itself
# permission to merge distinct source versions named in the author notes.
bib_records = {}
for bib_path in [ROOT / "handbook/bib/handbook.bib", ROOT / "handbook/bib/intake-p17-19-p19-11-integration.bib"]:
    if not bib_path.exists():
        continue
    raw = bib_path.read_text(encoding="utf-8-sig")
    for m in re.finditer(r"@([A-Za-z]+)\s*\{", raw):
        args, end = grammar.scan_braced_args(raw, m.end() - 1, 1)
        if args and "," in args[0]:
            key = args[0].split(",", 1)[0].strip()
            bib_records.setdefault(key, []).append({"path": bib_path.relative_to(ROOT).as_posix(),
                "line": raw.count("\n", 0, m.start()) + 1,
                "literal_record": raw[m.start():end]})

path_unit = {p: "ED26-" + Path(p).parent.name.upper() + "-CH-" + Path(p).stem for p in body}
domains_by_path = {p: [] for p in body}
missing_paths = []
for d in decisions["domains"]:
    paths = [f"handbook/parts/{d['id'].split('-')[0].lower()}/{stem}.tex" for stem in d["stems"]] + d.get("other_destinations", [])
    for p in paths:
        if p in domains_by_path:
            domains_by_path[p].append(d["id"])
        else:
            missing_paths.append({"domain": d["id"], "path": p})
if missing_paths:
    raise SystemExit(json.dumps({"unresolved_destination_paths": missing_paths}))

units = []
for path, r in sorted(body.items()):
    uid = path_unit[path]
    part = Path(path).parent.name
    annex_path = path.replace("/parts/", "/annex/")
    raw = (ROOT / path).read_text(encoding="utf-8-sig")
    author_notes = []
    for note in find_notes(path):
        text = note.read_text(encoding="utf-8-sig")
        author_notes.append({"path": note.relative_to(ROOT).as_posix(), "sha256": digest(note),
            "standing": "Author's exact scope/provenance record; not fresh independent acceptance",
            "text": text})
    locators = {}
    for m in re.finditer(r"\\[A-Za-z]*cite[A-Za-z]*\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^{}]*)\}", raw):
        for key in m.group(1).split(","):
            locators.setdefault(key.strip(), []).append({"line": raw.count("\n", 0, m.start()) + 1, "literal_citation": m.group(0)})
    source_presentations = [{"citation_key": k, "bibliographic_records": bib_records.get(k, []),
        "required_extent": {"inline_locators": locators.get(k, []), "author_scope_records": [n["path"] for n in author_notes]},
        "extent_rule": "Only the specifically selected presentation/components recorded by these source notes and locators; a reference does not add an entire monograph."}
        for k in r["citation_keys"]]
    components = []
    for i, e in enumerate(r["entries"], 1):
        components.append({"component_id": f"{uid}-C{i:03}", "description": e["title"],
            "entry_kind": e["environment"], "body_label": e["label"], "body_lines": [e["line"], e["end_line"]],
            "declared_treatment": e["declared_status"], "exact_current_text": e["text"],
            "required_source_extent": {"source_presentations": r["citation_keys"], "scope_records": [n["path"] for n in author_notes]},
            "success_condition": "Supply this exact entry's definitions, hypotheses, construction or argument, worked boundary and the full treatment promised by its declared status; preserve the identified source variants.",
            "failure_condition": "Missing promised direction/case, unsupported source attribution, unstated assumption, incorrect argument, or a different regime substituted for this component.",
            "declared_proof_destinations": e.get("declared_proof_destinations", [])})
    # Include every unrecognized draft proof wrapper as text with an explicit
    # integration repair, never as a valid existing environment.
    draft_proofs = []
    if (ROOT / annex_path).exists():
        ann = (ROOT / annex_path).read_text(encoding="utf-8-sig")
        for m in re.finditer(r"\\begin\{hbproof\}", ann):
            args, start = grammar.scan_braced_args(ann, m.end(), 2)
            end = ann.find(r"\end{hbproof}", start)
            if len(args) != 2 or end < 0:
                raise SystemExit(f"Unparsed draft proof wrapper in {annex_path}")
            draft_proofs.append({"label": args[0], "body_backref": args[1],
                "line": ann.count("\n", 0, m.start()) + 1, "text": ann[start:end],
                "standing": "Derivation text present; wrapper undefined; integration repair required"})
    questions = []
    if not author_notes:
        questions.append("Identify the exact source-version and selected-extent record for this current treatment.")
    if any(not x["bibliographic_records"] for x in source_presentations):
        questions.append("Resolve the missing exact bibliographic record for the listed citation key; preserve distinct versions.")
    if not domains_by_path[path]:
        questions.append("Bind this authored treatment to an initial reasoning assignment or explicit mandatory family.")
    repair = []
    if draft_proofs:
        repair.append("Convert the undefined hbproof wrappers to the maintained annexitem/proof interface; preserve every supplied derivation and reciprocal target. See spec/research/edition-2026-map-destination-repairs.md.")
    if Path(path).stem in {"epistemic-nash-conditions", "explanatory-preferences"}:
        repair.append("Merge the combined P17.19/P19.11 bibliography and symbol intakes into the canonical files exactly once.")
    units.append({"unit_id": uid,
        "kind": "empirical_treatment" if part == "p19" else "theorem_proof_group",
        "title": r["headings"][0]["title"] if r["headings"] else Path(path).stem,
        "reasoning_question": "The exact inference problem, assumptions and boundaries specified by the named components below.",
        "initial_assignment_ids": domains_by_path[path], "original_requirement_ids": [], "inherited_source_ordinals": [],
        "source_presentations": source_presentations, "required_components": components,
        "prerequisites": sorted(set(m.group(1) for m in re.finditer(r"\\(?:c|C)?ref\{([^{}]*)\}", raw))),
        "prerequisite_representation": "Literal existing cross-reference groups, to be reconciled with catalog unit IDs; internal and forward comparisons are retained distinctly from a proven dependency order.",
        "destination": {"body": {"path": path, "sha256": r["sha256"], "on_reader_route": r["in_static_reader_graph"]},
            "annex": {"path": annex_path, "exists": annex_path in by_path, "sha256": by_path.get(annex_path, {}).get("sha256")},
            "lookup": {"maintained_entry_labels": [e["label"] for e in r["entries"]], "final_subject_task_cases_pending": True}},
        "content_state": "partly_authored" if repair else "authored",
        "content_state_extent": "Existing named body text and present derivations only; does not close the surrounding assignment, all cited sources, or independent acceptance.",
        "source_state": "mixed",
        "scope_state": "unresolved" if questions else "resolved",
        "scope_resolution_extent": "The finite selected treatment and its exact retained source notes; wider family decisions live in the domain and benchmark crosswalks.",
        "evidence": [{"path": path, "sha256": r["sha256"]}], "author_scope_records": author_notes,
        "unrecognized_draft_proof_texts": draft_proofs,
        "remaining_work": repair + ["Complete the promised component treatments and source-specific residual obligations recorded in the retained author scope notes, then perform the consolidated content and publication reviews."],
        "unresolved_questions": questions})

plan = (ROOT / "spec/EDITION-2026-WORK-PACKAGES.md").read_text(encoding="utf-8-sig")
literal = {}
part = None
family_rows = []
for number, line in enumerate(plan.splitlines(), 1):
    h = re.match(r"### (P1[5-9]) ", line)
    if h:
        part = h.group(1)
    if re.match(r"\| [UCDAE][1-6] \|", line):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        literal[f"{part}-{cells[0]}"] = {"required_treatment": cells[1], "success_case": cells[2], "failure_condition": cells[3], "plan_line": number}
    if 390 <= number <= 425 and line.startswith("| ") and not line.startswith(("| ---", "| Topic family", "| Family /")):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        family_rows.append({"family_id": f"CF-{len(family_rows)+1:02}", "literal_cells": cells, "plan_line": number,
            "mapping_state": "unresolved", "required_decision": "Bind the exact finite source presentations and components to existing units or a specifically described new destination; retain all original obligations."})
domain_rows = []
for d in decisions["domains"]:
    paths = [f"handbook/parts/{d['id'].split('-')[0].lower()}/{s}.tex" for s in d["stems"]] + d.get("other_destinations", [])
    domain_rows.append({"assignment_id": d["id"], **literal[d["id"]],
        "unit_ids": [path_unit[p] for p in paths], "present_destinations": paths,
        "prerequisites": d["prerequisites"], "original_requirement_ids": d.get("original_requirement_ids", []),
        "remaining_mapping_decisions": d["remaining"], "mapping_state": "unresolved",
        "mapping_state_reason": "Current finite treatments are mapped; the listed wider scope decisions must still be closed against the benchmark and original-requirement units.",
        "evidence": ["spec/EDITION-2026-WORK-PACKAGES.md", "spec/coverage/edition-2026/domain-allocation-decisions.json", "spec/coverage/edition-2026/new-domain-destination-evidence.jsonl"]})
if len(domain_rows) != 26 or len(literal) != 26 or len(family_rows) != 12:
    raise SystemExit(f"Unexpected preserved plan denominators: {len(domain_rows)}, {len(literal)}, {len(family_rows)}")
outputs = [write_jsonl("current-reasoning-units.jsonl", units),
           write_jsonl("new-domain-crosswalk.jsonl", domain_rows),
           write_jsonl("mandatory-family-crosswalk.jsonl", family_rows)]
receipt = {"purpose": "Finite coverage-map data projection; no manuscript tests, review or admission",
    "outputs": outputs, "unit_count": len(units), "component_count": sum(len(u["required_components"]) for u in units),
    "scope_states": {s: sum(u["scope_state"] == s for u in units) for s in ["resolved", "unresolved"]},
    "unassigned_current_files": [p for p, ids in domains_by_path.items() if not ids],
    "undefined_wrapper_derivations": sum(len(u["unrecognized_draft_proof_texts"]) for u in units),
    "scope_questions": [{"unit_id": u["unit_id"], "questions": u["unresolved_questions"]} for u in units if u["unresolved_questions"]],
    "domain_rows": len(domain_rows), "mandatory_family_rows": len(family_rows),
    "map_complete": False}
(DEST / "new-domain-map-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False))
