"""Materialize the finite method selections and join mandatory family decisions."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "spec/coverage/edition-2026"

def read_jsonl(path):
    return [json.loads(s) for s in path.read_text(encoding="utf-8-sig").splitlines() if s.strip()]

def write_jsonl(name, rows):
    path = DEST / name
    if path.exists():
        raise SystemExit("Preserve prior map projection: " + name)
    path.write_text("".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in rows),encoding="utf-8")
    return {"path":path.relative_to(ROOT).as_posix(),"rows":len(rows),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()}

selections = json.loads((DEST / "method-source-selections.json").read_text(encoding="utf-8"))["methods"]
inquiry = json.loads((DEST / "inquiry-source-version-decision.json").read_text(encoding="utf-8"))
units = []
for r in selections:
    uid = "ED26-METHOD-" + r["id"]
    sources = r["sources"]
    questions = [r["scope_question"]] if r.get("scope_question") else []
    if r["id"] == "inquiry-design":
        sources = [{"title":"Cochrane Handbook chapter " + str(c["chapter"]) + ": " + c["title"],
            "version":c["version"] + "; last updated " + c["last_updated"],"url":c["url"],
            "extent":"Complete selected chapter method development, including its examples, limitations and claim-level dependencies",
            "version_decision":"spec/coverage/edition-2026/inquiry-source-version-decision.json"} for c in inquiry["chapters"]]
        questions = []
    part = r["part"].lower()
    units.append({"unit_id":uid,"kind":"empirical_treatment" if r["id"] in {"generated-quantitative-reasoning","model-confidence"} else "philosophical_argument" if r["id"] == "inference-best-explanation" else "algorithm_method",
        "title":r["title"],"reasoning_question":r["question"],"initial_assignment_ids":r["domains"],"mandatory_family_ids":r["families"],
        "original_requirement_ids":[],"inherited_source_ordinals":[],"source_presentations":sources,
        "required_components":[{"component_id":f"{uid}-C{i:02}","description":c,
            "required_source_extent":[s["extent"] for s in sources],"success_condition":r["success"],"failure_condition":r["failure"]} for i,c in enumerate(r["components"],1)],
        "prerequisites":r["prerequisites"],
        "destination":{"body":{"path":f"handbook/parts/{part}/{r['id']}.tex","standing":"Precise proposed destination; no empty manuscript file created"},
            "annex":{"path":f"handbook/annex/{part}/{r['id']}.tex","standing":"For the full formal derivations promised by this selected method; philosophical/empirical justification remains in the treatment"},
            "lookup":{"subject":r["title"],"task":r["question"],"positive_case":r["success"],"negative_case":r["failure"]}},
        "content_state":"missing","source_state":"identified_missing","scope_state":"unresolved" if questions else "resolved",
        "evidence":[s["url"] for s in sources]+["spec/coverage/edition-2026/method-source-selections.json"],
        "remaining_work":["Verify/capture and read each exact selected source version and extent using free access.","Supply every named component and its required proofs or source/evidence argument.","Resolve exact prerequisite interfaces and source-specific overlaps, then integrate the full treatment and lookup cases.","Complete the consolidated content and publication reviews after the whole change set."],
        "unresolved_questions":questions,"body_read_or_accepted_from_metadata":False})

families = json.loads((DEST / "mandatory-family-selections.json").read_text(encoding="utf-8"))["families"]
literal = {r["family_id"]:r for r in read_jsonl(DEST / "mandatory-family-crosswalk.jsonl")}
known_units = {r["unit_id"] for r in units}
for name in ["requirements-units.jsonl","current-reasoning-units.jsonl","benchmark-content-units.jsonl"]:
    known_units.update(r["unit_id"] for r in read_jsonl(DEST / name))
b = json.loads((DEST / "sources-001-036/active-shard-manifest.json").read_text(encoding="utf-8"))
for f in b["active_files"]:
    if f["role"] == "content_units":
        known_units.update(r["unit_id"] for r in read_jsonl(ROOT / f["path"]))
cpath = DEST / "sources-037-068/shard-manifest-v4.json"
c = json.loads(cpath.read_text(encoding="utf-8"))
for name in c["active_files"]["content_unit_files"]:
    known_units.update(r["unit_id"] for r in read_jsonl(cpath.parent / name))
for family in families:
    missing = sorted(set(family["selected_unit_ids"]) - known_units)
    if missing:
        raise SystemExit(json.dumps({"family":family["family_id"],"unbound_units":missing}))
    family.update({"literal_plan_obligation":literal[family["family_id"]]["literal_cells"],"plan_line":literal[family["family_id"]]["plan_line"],
        "mapping_state":"resolved","writing_acceptance_inferred":False,
        "scope_resolution_extent":"Exact included unit set and positive/negative scope conditions; unresolved questions within an underlying source unit and global reconciliation remain independently open."})

bench = read_jsonl(DEST / "benchmark-crosswalk.jsonl")
domains = read_jsonl(DEST / "new-domain-crosswalk.jsonl")
family_domains = {"CF-01":["P19-E1","P19-E2"],"CF-02":["P19-E2","P19-E3","P19-E4","P19-E5"],
    "CF-03":["P19-E2","P19-E5","P19-E6"],"CF-04":["P17-D2","P17-D3","P19-E3","P19-E6"],
    "CF-05":[],"CF-06":["P18-A4","P19-E2"],"CF-07":["P15-U1","P15-U2","P15-U5","P15-U6"],
    "CF-08":["P15-U6"],"CF-09":["P15-U4","P15-U6","P16-C3","P16-C4","P19-E1"],
    "CF-10":["P16-C1"],"CF-11":[],"CF-12":["P19-E5","P19-E6","P18-A4"]}
for domain in domains:
    did = domain["assignment_id"]
    additions = set()
    for item in bench:
        if did in item["assigned_domains_or_families"]:
            additions.update(item["unit_ids"])
    for item in units:
        if did in item["initial_assignment_ids"]:
            additions.add(item["unit_id"])
    contributing = []
    for family in families:
        if did in family_domains[family["family_id"]]:
            additions.update(family["selected_unit_ids"])
            contributing.append(family["family_id"])
    domain["selected_additional_unit_ids"] = sorted(additions - set(domain["unit_ids"]))
    domain["contributing_family_ids"] = contributing
    domain["initial_mapping_questions_preserved"] = domain.pop("remaining_mapping_decisions")
    domain["mapping_state"] = "resolved"
    domain["mapping_state_reason"] = "The finite current treatments, selected source presentations and named additional methods now allocate the required breadth. Exact actual prerequisite edges and cross-source overlaps remain global reconciliation work; no manuscript acceptance is inferred."
    domain["all_selected_unit_ids"] = sorted(set(domain["unit_ids"]) | additions)
    domain["remaining_work"] = ["Execute every incomplete selected unit and retained original source/proof requirement.","Resolve the exact prerequisite graph and component-level overlap relations without double credit.","Complete the final source/topic/publication reviews and both lookup routes."]
    domain["global_reconciliation_pending"] = True

products = [write_jsonl("additional-method-units.jsonl",units),write_jsonl("mandatory-family-crosswalk-v2.jsonl",families),write_jsonl("new-domain-crosswalk-v2.jsonl",domains)]
receipt = {"purpose":"Coverage-map data assembly; no manuscript review/build or admission", "outputs":products,
    "method_units":len(units),"method_components":sum(len(r["required_components"]) for r in units),
    "family_rows":len(families),"domain_rows":len(domains),"all_selected_family_ids_bound":True,
    "method_scope_questions":[q for r in units for q in r["unresolved_questions"]],
    "historical_source_manifest_used":cpath.relative_to(ROOT).as_posix(),"global_map_complete":False}
(DEST / "method-family-map-receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt,ensure_ascii=False))
