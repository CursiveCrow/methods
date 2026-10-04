"""Integrate explicitly selected gap findings without importing rejected candidates."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import argparse
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
DEST=ROOT/"spec/coverage/edition-2026"
parser=argparse.ArgumentParser()
parser.add_argument("inputs",nargs="+")
args=parser.parse_args()
def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8-sig"))
def rows(path):
    return [json.loads(s) for s in (ROOT/path).read_text(encoding="utf-8-sig").splitlines() if s.strip()]
def pin(path):
    p=ROOT/path
    return {"path":str(path),"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
decision=load("spec/coverage/edition-2026/gap-unit-selections.json")
selected={r["unit_id"]:r for r in decision["selected_units"]}
findings=[]
units=[]
seen=set()
for input_path in args.inputs:
    for row in rows(input_path):
        finding_id=row.get("finding_id",row.get("gap_id"))
        if not finding_id or finding_id in seen:
            raise SystemExit("Missing or duplicate gap identity: "+str(finding_id))
        seen.add(finding_id)
        proposed=row.get("proposed_unit_ids",[])
        if len(proposed)>1:
            raise SystemExit("Split multiple proposed units before integration: "+finding_id)
        uid=row.get("unit_id") or row.get("proposed_unit_id") or (proposed[0] if proposed else None)
        include=uid in selected
        if include and row.get("inclusion_decision","").startswith("not_selected"):
            raise SystemExit("Selection conflicts with explicit source disposition: "+uid)
        retained={**row,"finding_id":finding_id,"source_shard":input_path,"root_selected_new_unit":include,
            "selected_unit_id":uid if include else None,"root_selection":selected.get(uid)}
        if include and selected[uid].get("classification_override"):
            retained["original_classification"]=row["classification"]
            retained["classification"]=selected[uid]["classification_override"]
        findings.append(retained)
        if not include:
            continue
        if row.get("scope_state")!="resolved" or row.get("unresolved_questions"):
            raise SystemExit("New unit still has unresolved scope: "+uid)
        components=row.get("required_components",[])
        if not components or any(not all(c.get(k) for k in ["component_id","description","success_condition","failure_condition","required_source_extent"]) for c in components):
            raise SystemExit("Incomplete component allocation: "+uid)
        if not row.get("source_presentations") or not row.get("destination") or not row.get("reasoning_question"):
            raise SystemExit("Incomplete source/destination/question: "+uid)
        unit={k:v for k,v in row.items() if k in ["title","reasoning_question","original_requirement_ids","inherited_source_ordinals","source_presentations","required_components","prerequisites","destination","content_state","source_state","scope_state","evidence","remaining_work","unresolved_questions","inputs","conclusions","assumptions","worked_case","failure_case","priority"]}
        unit.update(unit_id=uid,kind=selected[uid]["kind"],gap_finding_id=finding_id,
            inclusion_authority="spec/coverage/edition-2026/gap-unit-selections.json",
            related_existing_unit_ids=row.get("related_existing_unit_ids",row.get("existing_mapped_unit_ids",row.get("existing_unit_ids",[]))),
            original_requirement_ids=row.get("original_requirement_ids",[]),
            inherited_source_ordinals=row.get("inherited_source_ordinals",[]),
            content_state=row.get("content_state","missing"),
            source_state=row.get("source_state","identified_missing"),
            independent_acceptance=False,
            source_scope_standing="The exact selected source method and components remain a writing obligation. A subject overlap is not identity of the source presentation or completed proof.")
        if row.get("positive_case") is not None:
            unit["worked_case"]=row["positive_case"]
        if row.get("negative_case") is not None:
            unit["failure_case"]=row["negative_case"]
        if row.get("assumptions_and_conclusions") is not None:
            unit["assumptions_and_conclusions"]=row["assumptions_and_conclusions"]
        units.append(unit)
if set(selected)!={u["unit_id"] for u in units}:
    raise SystemExit(json.dumps({"unreturned_selected_units":sorted(set(selected)-{u['unit_id'] for u in units})}))
master=load("spec/edition-2026-coverage-map.json")
existing={u["unit_id"] for f in master["unit_shards"] if not f["path"].endswith("added-reasoning-units.jsonl") for u in rows(f["path"])}
all_ids=existing|set(selected)
bad=[]
for row in findings:
    for key in ["related_existing_unit_ids","existing_mapped_unit_ids","existing_unit_ids"]:
        for uid in row.get(key,[]):
            if uid not in all_ids:
                bad.append({"finding_id":row["finding_id"],"unit_id":uid})
if bad:
    raise SystemExit(json.dumps({"unbound_existing_gap_links":bad}))
outputs=[]
for name,data in [("reasoning-gap-register.jsonl",findings),("added-reasoning-units.jsonl",units)]:
    p=DEST/name
    p.write_text("".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in data),encoding="utf-8")
    outputs.append({**pin(p.relative_to(ROOT)),"rows":len(data)})
receipt={"snapshot_utc":datetime.now(timezone.utc).isoformat(),"inputs":[pin(p) for p in args.inputs],
    "selection":pin("spec/coverage/edition-2026/gap-unit-selections.json"),"outputs":outputs,
    "findings":len(findings),"new_units":len(units),"new_components":sum(len(u["required_components"]) for u in units),
    "finding_classifications":dict(Counter(f["classification"] for f in findings)),
    "all_selected_new_units_returned":True,"all_existing_gap_links_resolve":True,
    "scope_standing":"Root-selected construction additions to the logic/reasoning reference; no manuscript content or publication acceptance inferred."}
(DEST/"gap-integration-receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in receipt.items() if k not in ['inputs','selection','outputs']},ensure_ascii=False))
