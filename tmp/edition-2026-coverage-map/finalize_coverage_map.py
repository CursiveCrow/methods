"""Complete-set construction accounting and readable coverage-map handoff."""
from pathlib import Path
from collections import Counter,defaultdict
from datetime import datetime,timezone
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[2]
DEST=ROOT/"spec/coverage/edition-2026"
def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8-sig"))
def rows(path):
    return [json.loads(s) for s in (ROOT/path).read_text(encoding="utf-8-sig").splitlines() if s.strip()]
def pin(path):
    p=ROOT/path
    return {"path":str(path),"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def verify(item):
    p=pin(item["path"])
    if p["sha256"].lower()!=item["sha256"].lower():
        raise SystemExit("Changed input before construction completion: "+item["path"])
    return p

master=load("spec/edition-2026-coverage-map.json")
sources=master["active_source_manifests"]
assert len(sources)==3
for item in sources:verify(item)
a,b,c=[load(item["path"]) for item in sources]
assert a["counts"]["requirements_mapping"]=={"resolved":615}
assert a["counts"]["inherited_mapping"]=={"resolved":1055}
assert b["counts"]["topic_total"]==b["counts"]["topic_resolved"]==742017
assert b["counts"]["topic_unresolved"]==0
assert b["counts"]["resolved_source_records"]==36
assert b["counts"]["resolved_hierarchy_records"]==1622
assert b["counts"]["unresolved_scope_units"]==0
assert c["raw_record_count"]==8418475
assert c["raw_mapping_states"].get("resolved")==8418475
assert c["raw_mapping_states"].get("unresolved",0)==0
checked=[]
for f in a["files"]: checked.append(verify(f))
for f in b["active_files"]: checked.append(verify(f))
for name,entry in c["files"].items():
    if any(name in names for names in c["active_files"].values() if isinstance(names,list)):
        checked.append(verify({"path":str(Path(sources[2]["path"]).parent/name),"sha256":entry["sha256"]}))
units=[]
for f in master["unit_shards"]:
    checked.append(verify(f))
    units.extend(rows(f["path"]))
assert len({u["unit_id"] for u in units})==len(units)
open_units=[u["unit_id"] for u in units if u.get("scope_state")!="resolved" or u.get("unresolved_questions")]
if open_units: raise SystemExit(json.dumps({"unresolved_unit_scopes":open_units}))
for u in units:
    if not u.get("required_components") or not u.get("source_presentations") or not u.get("destination"):
        raise SystemExit("Incomplete unit allocation: "+u["unit_id"])
requirements=rows("spec/coverage/edition-2026/requirements-crosswalk.jsonl")
inherited=rows("spec/coverage/edition-2026/inherited-crosswalk.jsonl")
assert len(requirements)==615 and all(r["mapping_state"]=="resolved" for r in requirements)
assert len(inherited)==1055 and all(r["mapping_state"]=="resolved" for r in inherited)
relation=load("spec/coverage/edition-2026/relation-reconciliation-receipt.json")
assert relation["known_interface_allocation_complete"] and not relation["unresolved_relations"]
assert relation["active_unit_count"]==len(units)
for item in relation["input_unit_shards"]+relation["outputs"]: verify(item)
relation_inputs={item["path"]:item["sha256"].lower() for item in relation["input_unit_shards"]}
assert all(relation_inputs.get(f["path"])==f["sha256"].lower() for f in master["unit_shards"])
gap=load("spec/coverage/edition-2026/gap-integration-receipt.json")
for item in gap["inputs"]+gap["outputs"]+[gap["selection"]]: verify(item)
assert gap["all_selected_new_units_returned"] and gap["all_existing_gap_links_resolve"]
decisions=load("spec/coverage/edition-2026/gap-unit-selections.json")
assert decisions["selection_complete"]
assert gap["new_units"]==len(decisions["selected_units"])
findings=rows("spec/coverage/edition-2026/reasoning-gap-register.jsonl")
overlap_path="spec/coverage/edition-2026/thinking-gaps/selected-source-overlaps.jsonl"
overlaps=rows(overlap_path)
assert len(overlaps)==11
all_ids={u["unit_id"] for u in units}
known_relation_ids=all_ids|{f["finding_id"] for f in findings}
known_relation_ids.update(component["component_id"] for u in units for component in u["required_components"])
def unit_refs(value):
    if isinstance(value,str):
        yield from (s.rstrip(".:") for s in re.findall(r"ED26-[A-Za-z0-9_.:-]+",value))
    elif isinstance(value,dict):
        for v in value.values(): yield from unit_refs(v)
    elif isinstance(value,list):
        for v in value: yield from unit_refs(v)
bad_refs=[]
for r in overlaps:
    for uid in unit_refs(r):
        if uid not in known_relation_ids: bad_refs.append(uid)
if bad_refs:raise SystemExit(json.dumps({"unbound_overlap_identifiers":sorted(set(bad_refs))}))

queue=[]
for u in units:
    uid=u["unit_id"]
    queue.append({"unit_id":uid,"title":u["title"],"content_state":u.get("content_state"),"source_state":u.get("source_state"),
        "required_components":u["required_components"],"source_presentations":u["source_presentations"],"destination":u["destination"],
        "prerequisite_allocation_prefix":uid+"/PRE-","remaining_work":u.get("remaining_work",[]),
        "next_action":"Preserve and integrate the existing treatment, complete its explicitly outstanding source/proof/apparatus work, then include it in the consolidated manuscript checks." if u.get("content_state")=="authored" else "Qualify the selected source bodies and complete every missing or partial component at its mapped destination; coordinate shared destinations before editing.",
        "success_condition":"Every mapped component, source/version qualification, required derivation or argument, example and lookup obligation is supplied at the exact stated scope.",
        "failure_condition":"A source pointer, related topic, different version, incomplete proof or duplicated coverage credit is used to discharge an unsupplied component.",
        "review_sequence":"Complete the requested writing/correction/integration batch before consolidated independent reviews.",
        "counting_rule":"This is a requirement/source facet queue. Shared-source and destination crosswalks prevent summing these records as independent works or a manuscript completion percentage."})
queue_path=DEST/"completion-work-queue.jsonl"
queue_path.write_text("".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in queue),encoding="utf-8")
now=datetime.now(timezone.utc).isoformat()
accounting=master["complete_set_accounting"]
accounting.update(cross_shard_overlap_reconciliation_complete=True,prerequisite_reconciliation_complete=True,semantic_scope_complete=True,
    new_gap_findings=gap["findings"],new_gap_units=gap["new_units"],new_gap_components=gap["new_components"],
    prerequisite_reconciliation_scope="Every declared known interface/source import is bound or explicitly allocated as local setup/source-closure work. This is not acceptance of the actual proof dependency graph.",
    historical_raw_record_reconciliation_complete=True)
accounting["unit_count_standing"]="Catalog requirement/source facets with explicit overlap and shared-destination relations; not independent complete works or a manuscript completion percentage."
master.update(snapshot_utc=now,stage="coverage_construction_complete",map_complete=True,catalog_admission_complete=False,
    relation_reconciliation=pin("spec/coverage/edition-2026/relation-reconciliation-receipt.json"),
    gap_source_overlaps=pin(overlap_path),completion_work_queue={**pin(queue_path.relative_to(ROOT)),"unit_rows":len(queue)},
    note="Coverage-map construction is complete for the selected edition scope and source corpus. Acquisition, writing, source-body proof closure, independent catalog admission and manuscript publication remain explicit work. No manuscript completion percentage is inferred.")
question_path=DEST/"integrated-unresolved-scope.json"
question_path.write_text(json.dumps({"snapshot_utc":now,"unit_questions":[],"requirement_rows":[],"inherited_rows":[],"global_remaining":[],
    "construction_scope_complete":True,"remaining_manuscript_work":"spec/coverage/edition-2026/completion-work-queue.jsonl",
    "standing":"Zero unresolved construction-scope questions does not mean zero source-acquisition or manuscript work."},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
master["unresolved_scope_register"]=pin(question_path.relative_to(ROOT))
receipt={"snapshot_utc":now,"status":"construction_complete","checked_file_pins":checked,
    "original_requirements":615,"inherited_units":1055,"historical_sources":68,"historical_records":9162150,
    "historical_partition":[743675,8418475],"new_domain_assignments":26,"mandatory_families":12,"benchmark_rows":106,
    "unit_records":len(units),"required_component_records":sum(len(u["required_components"]) for u in units),
    "gap_findings":gap["findings"],"added_units":gap["new_units"],"unresolved_scope_questions":0,
    "prerequisite_allocation":pin("spec/coverage/edition-2026/relation-reconciliation-receipt.json"),
    "source_overlap":pin(overlap_path),"work_queue":pin(queue_path.relative_to(ROOT)),
    "raw_original_corpus_evidence":"The historical whole-corpus SHA and complete source partitions are retained in the source receipts. This final pass verifies active mapped files; it does not repeat the 7 GB raw parse or count metadata as mathematical content.",
    "independent_catalog_admission":False,"manuscript_publication_acceptance":False}
receipt_path=DEST/"construction-completion-receipt.json"
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
master["construction_completion_receipt"]=pin(receipt_path.relative_to(ROOT))
(ROOT/"spec/edition-2026-coverage-map.json").write_text(json.dumps(master,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

lines=["# The Methods of Reason: scope and coverage map","",f"Construction completed: {now}.","",
"The edition is a CRC-style reference handbook of logic and reasoning. Its entries support subject lookup and reasoning-task lookup, with explicit assumptions, methods, results, required proofs or arguments, examples, counterexamples and source distinctions.","",
"## Complete construction accounting","","| Coverage set | Mapped | Unresolved scope |","| --- | ---: | ---: |",
"| Original requirements | 615 / 615 | 0 |","| Inherited structural units | 1,055 / 1,055 | 0 |","| Historical source groups | 68 / 68 | 0 |","| Historical records | 9,162,150 / 9,162,150 | 0 |",
"| Initial new-reasoning assignments | 26 / 26 | 0 |","| Mandatory cross-part families | 12 / 12 | 0 |","| Selected benchmark contents | 106 / 106 | 0 |","",
f"The integrated catalog contains {len(units):,} unit records and {sum(len(u['required_components']) for u in units):,} component records. These are source and requirement facets with explicit overlap relations, not independent books or a manuscript completion percentage. Historical metadata and repeated captures retain their own dispositions.","",
"## Additional source treatments selected by the gap analysis","",
f"The gap register accounts for {gap['findings']} findings and selects {gap['new_units']} additional finite source treatments. Existing and already planned coverage is retained. Original absence observations are preserved where later source reconciliation qualifies them.","",
"| Treatment | Required contribution |","| --- | --- |"]
for selection in decisions["selected_units"]:
    u=next(u for u in units if u["unit_id"]==selection["unit_id"])
    lines.append("| "+u["title"].replace("|","/")+" | "+u["reasoning_question"].replace("|","/")+" |")
lines += ["","General design/prototyping additions were not selected. Existing analogy, testimony, diagrammatic logic, constraint programming, planning, scientific reasoning and empirical benchmarks retain their actual authored or missing-text standing.","",
"## Using the map","",
"- `edition-2026-coverage-map.json` is the root manifest. It selects exact active shard revisions and hashes; superseded files are historical evidence.",
"- `coverage/edition-2026/requirements-crosswalk.jsonl` preserves every original requirement and its current assessment.",
"- `coverage/edition-2026/inherited-crosswalk.jsonl` preserves all inherited ordinals, including the explicit retirement of the six opening-framing units.",
"- `coverage/edition-2026/reasoning-gap-register.jsonl` preserves every new candidate and its selected, existing or nonselected disposition.",
"- `coverage/edition-2026/prerequisite-allocation-crosswalk.jsonl` binds declared interfaces and explicit local setup/source-closure obligations. A reference alone is not a proof dependency.",
"- `coverage/edition-2026/source-overlap-crosswalk.jsonl` and `shared-destination-crosswalk.jsonl` preserve distinct source extents and prevent duplicate completion credit.",
"- `coverage/edition-2026/completion-work-queue.jsonl` supplies each unit's source, components, destination, remaining work and success/failure conditions.","",
"## Remaining manuscript work","",
"Source acquisition, complete writing and proofs, correction of active errors, integration of drafts and annexes, bibliography and symbols, task/subject navigation, and the final consolidated reviews remain governed by the completion queue and edition contract. Known repairs include unrecognized draft proof environments, unrouted annex material and source-attribution corrections. They were mapped during this phase; the book was not rewritten or rendered.","",
"`map_complete: true` records construction of the scope/coverage map. `catalog_admission_complete: false` preserves the separate independent-admission gate. Neither is publication acceptance. The finite source cutoff remains 7 September 2026. No broad authoring or manuscript review was substituted for this mapping task.",""]
(ROOT/"spec/edition-2026-coverage-map.md").write_text("\n".join(lines),encoding="utf-8")
print(json.dumps({k:v for k,v in receipt.items() if k not in ['checked_file_pins','raw_original_corpus_evidence']},ensure_ascii=False))
