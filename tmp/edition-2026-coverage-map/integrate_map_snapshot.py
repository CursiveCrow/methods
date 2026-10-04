"""Integrate explicitly selected active coverage shards without unioning revisions."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
from collections import Counter
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "spec/coverage/edition-2026"
parser = argparse.ArgumentParser()
parser.add_argument("--first-source-manifest",required=True)
parser.add_argument("--last-source-manifest",required=True)
args = parser.parse_args()

def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8-sig"))
def read_rows(path):
    return [json.loads(s) for s in (ROOT/path).read_text(encoding="utf-8-sig").splitlines() if s.strip()]
def pin(path):
    p = ROOT/path
    return {"path":path,"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def verify(path,expected):
    actual = pin(path)
    if actual["sha256"].lower() != expected.lower():
        raise SystemExit("Active files changed or wrong manifest selected: " + path)
    return actual

a_path = "tmp/edition-2026-map-requirements/active-shard-manifest.json"
a,b,c = load(a_path),load(args.first_source_manifest),load(args.last_source_manifest)
unit_files = []
for f in a["files"]:
    if f["path"].endswith("requirements-units.jsonl"):
        unit_files.append(verify(f["path"],f["sha256"]))
first_source_unit_names = set(b.get("counts",{}).get("content_unit_files",[]))
for f in b["active_files"]:
    if f["role"] == "content_units" or Path(f["path"]).name in first_source_unit_names:
        unit_files.append(verify(f["path"],f["sha256"]))
for name in c["active_files"]["content_unit_files"]:
    path = (Path(args.last_source_manifest).parent / name).as_posix()
    unit_files.append(verify(path,c["files"][name]["sha256"]))
root_unit_names=["current-reasoning-units.jsonl","benchmark-content-units.jsonl","additional-method-units.jsonl"]
if (DEST/"added-reasoning-units.jsonl").is_file():
    root_unit_names.append("added-reasoning-units.jsonl")
for name in root_unit_names:
    unit_files.append(pin("spec/coverage/edition-2026/" + name))
units = []
for f in unit_files:
    entries = read_rows(f["path"])
    f["unit_records"] = len(entries)
    f["component_records"] = sum(len(e.get("required_components",[])) for e in entries)
    units.extend(entries)
ids = Counter(u["unit_id"] for u in units)
duplicate_ids = [k for k,v in ids.items() if v > 1]
if duplicate_ids:
    raise SystemExit(json.dumps({"duplicate_unit_ids":duplicate_ids}))
unit_lookup = {u["unit_id"]:u for u in units}
prerequisite_overlays = []
for f in b["active_files"]:
    if "prerequisite-role-overlay" not in Path(f["path"]).name:
        continue
    checked = verify(f["path"],f["sha256"])
    overlay_rows = read_rows(f["path"])
    for row in overlay_rows:
        uid = row["unit_id"]
        if uid not in unit_lookup:
            raise SystemExit("Prerequisite overlay targets absent unit: " + uid)
        target = unit_lookup[uid]
        for field in ["prerequisites","internal_setup","ambient_hypothesis_policy","external_premise_policy"]:
            if field in row:
                target[field] = row[field]
        if row.get("remaining_work_addition"):
            target.setdefault("remaining_work",[]).append(row["remaining_work_addition"])
        target.setdefault("applied_prerequisite_overlays",[]).append({"path":f["path"],"unit_id":uid,"evidence":row.get("evidence")})
    checked["target_units"] = len(overlay_rows)
    prerequisite_overlays.append(checked)
rq_path = "spec/coverage/edition-2026/requirements-crosswalk.jsonl"
ih_path = "spec/coverage/edition-2026/inherited-crosswalk.jsonl"
for path in [rq_path,ih_path]:
    expected = next(f["sha256"] for f in a["files"] if f["path"] == path)
    verify(path,expected)
requirements,inherited = read_rows(rq_path),read_rows(ih_path)
bench_path = "spec/coverage/edition-2026/benchmark-crosswalk-v2.jsonl"
domain_path = "spec/coverage/edition-2026/new-domain-crosswalk-v3.jsonl"
family_path = "spec/coverage/edition-2026/mandatory-family-crosswalk-v2.jsonl"
bench,domains,families = read_rows(bench_path),read_rows(domain_path),read_rows(family_path)
unbound = []
for category,entries,field in [("requirements",requirements,"unit_ids"),("inherited",inherited,"unit_ids"),("benchmarks",bench,"unit_ids"),("domains",domains,"all_selected_unit_ids"),("families",families,"selected_unit_ids")]:
    for entry in entries:
        for uid in entry.get(field,[]):
            if uid not in ids:
                unbound.append({"category":category,"unit_id":uid})
if unbound:
    raise SystemExit(json.dumps({"unbound_unit_references":unbound}))
if len(requirements)!=615 or len(inherited)!=1055 or len(bench)!=106 or len(domains)!=26 or len(families)!=12:
    raise SystemExit("Required identity denominator changed")

def counts(entries,key):
    return dict(Counter(r.get(key,"unspecified") for r in entries))
now = datetime.now(timezone.utc).isoformat()
scope_questions = [{"unit_id":u["unit_id"],"title":u["title"],"scope_state":u.get("scope_state"),"questions":u.get("unresolved_questions",[]),"destination":u.get("destination")}
    for u in units if u.get("scope_state") != "resolved" or u.get("unresolved_questions")]
question_path = DEST / "integrated-unresolved-scope.json"
question_data = {"snapshot_utc":now,"unit_questions":scope_questions,
    "requirement_rows":[{"id":r["original_requirement_id"],"questions":r.get("unresolved_questions",[])} for r in requirements if r["mapping_state"] != "resolved"],
    "inherited_rows":[{"ordinal":r["inherited_ordinal"],"questions":r.get("unresolved_questions",[])} for r in inherited if r["mapping_state"] != "resolved"],
    "historical_source_manifests":[pin(args.first_source_manifest),pin(args.last_source_manifest)],
    "global_remaining":["Finish unresolved historical source/record roles and exact source scopes.","Finish original requirement scope allocations.","Complete cross-shard source/extent and shared-destination reconciliation.","Bind source-specific prerequisites as internal setup, ambient hypotheses, reading interfaces or explicit external results; do not treat every cross-reference as a proof premise.","Complete final map-level accounting and retain independent catalog admission as a separate later gate."]}
question_path.write_text(json.dumps(question_data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

master = load("spec/edition-2026-coverage-map.json")
master["snapshot_utc"] = now
master["stage"] = "integrated_scope_reconciliation"
master["unit_shards"] = unit_files
master["applied_unit_field_overlays"] = prerequisite_overlays
master["active_source_manifests"] = [pin(a_path),pin(args.first_source_manifest),pin(args.last_source_manifest)]
master["original_requirement_crosswalks"] = [{**pin(rq_path),"rows":len(requirements),"mapping_states":counts(requirements,"mapping_state")}]
master["inherited_unit_crosswalks"] = [{**pin(ih_path),"rows":len(inherited),"mapping_states":counts(inherited,"mapping_state"),"user_retired_opening_ordinals":[1,2,3,4,5,6]}]
master["historical_disposition_shards"] = [
    {"manifest":args.first_source_manifest,"source_range":[1,36],"accounted_original_records":743675,"reported_accounting":b["counts"],"precedence":b.get("precedence",b.get("precedence_semantics")),"overlay_order":b.get("overlay_order")},
    {"manifest":args.last_source_manifest,"source_range":[37,68],"accounted_original_records":c["raw_record_count"],"raw_mapping_states":c["raw_mapping_states"],"precedence":"Only active_files in the selected manifest; superseded revisions are not additional rows."}]
master["benchmark_crosswalks"] = [{**pin(bench_path),"rows":len(bench),"mapping_states":counts(bench,"mapping_state"),"role_manifest":pin("spec/coverage/edition-2026/benchmark-role-manifest.json")}]
master["domain_crosswalks"] = [{**pin(domain_path),"rows":len(domains),"mapping_states":counts(domains,"mapping_state")},{**pin(family_path),"rows":len(families),"mapping_states":counts(families,"mapping_state")}]
master["reader_interface_crosswalk"] = load("spec/coverage/edition-2026/reader-interface-receipt.json")
if (DEST/"gap-integration-receipt.json").is_file():
    master["reasoning_gap_register"] = load("spec/coverage/edition-2026/gap-integration-receipt.json")
master["construction_policy_decisions"] = [pin(p) for p in [
    "spec/decisions/edition-2026-coverage-policy-resolution.md",
    "spec/decisions/edition-2026-source-template-dispositions.md",
    "spec/decisions/handbook-of-thinking-scope-2026-09-09.md"]]
master["complete_set_accounting"] = {"identity_accounting":{"original_requirements":615,"inherited_ordinals":1055,"historical_sources":68,"historical_records":743675+c["raw_record_count"],"new_domain_assignments":26,"mandatory_families":12,"reasoning_benchmark_rows":106},
    "historical_partition_equation":"743675 + 8418475 = 9162150, disjoint source ranges 001-036 and 037-068",
    "current_unit_records":len(units),"current_component_records":sum(len(u.get("required_components",[])) for u in units),
    "unique_unit_ids":len(ids),"all_selected_unit_references_bound":True,
    "unit_scope_states":counts(units,"scope_state"),"unit_content_states":counts(units,"content_state"),
    "unit_count_standing":"Catalog records before semantic overlap/requirement-facet reconciliation; not independent complete works or an authoring percentage.",
    "benchmark_contents_all_accounted":True,"cross_shard_overlap_reconciliation_complete":False,"prerequisite_reconciliation_complete":False,"semantic_scope_complete":False,"manuscript_completion_fraction":None}
master["unresolved_scope_register"] = pin(question_path.relative_to(ROOT).as_posix())
master["map_complete"] = False
master["catalog_admission_complete"] = False
master["note"] = "Integrated construction snapshot from explicitly selected manifests. Missing writing remains distinct from missing scope. Active workers may publish later versions; refresh deliberately. No whole-book completion or independent acceptance is inferred."
(ROOT / "spec/edition-2026-coverage-map.json").write_text(json.dumps(master,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"snapshot":now,"units":len(units),"components":master["complete_set_accounting"]["current_component_records"],"requirements":counts(requirements,"mapping_state"),"inherited":counts(inherited,"mapping_state"),"unit_scope_states":counts(units,"scope_state"),"remaining_unit_question_records":len(scope_questions),"all_selected_unit_references_bound":True},ensure_ascii=False))
