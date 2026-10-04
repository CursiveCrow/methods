"""Summarize the exact active relation shapes before root reconciliation."""
from pathlib import Path
from collections import Counter, defaultdict
import json

ROOT=Path(__file__).resolve().parents[2]
def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8-sig"))
def rows(path):
    return [json.loads(s) for s in (ROOT/path).read_text(encoding="utf-8-sig").splitlines() if s.strip()]
master=load("spec/edition-2026-coverage-map.json")
units={u["unit_id"]:u for f in master["unit_shards"] for u in rows(f["path"])}
for f in master.get("applied_unit_field_overlays",[]):
    for overlay in rows(f["path"]):
        units[overlay["unit_id"]].update({k:v for k,v in overlay.items() if k in ["prerequisites","internal_setup","ambient_hypothesis_policy","external_premise_policy"]})
counts=Counter()
examples=defaultdict(list)
for unit in units.values():
    for p in unit.get("prerequisites",[]):
        if isinstance(p,str):
            key="string:"+p[:100]
        elif isinstance(p,dict):
            key="object:"+str(p.get("role",p.get("kind","no_role")))+":"+",".join(sorted(p))
        else:
            key=type(p).__name__
        counts[key]+=1
        if len(examples[key])<3:
            examples[key].append({"unit_id":unit["unit_id"],"prerequisite":p})
out={"active_units":len(units),"units_without_prerequisite_items":sum(not u.get("prerequisites") for u in units.values()),
    "relation_shapes":[{"shape":k,"count":v,"examples":examples[k]} for k,v in counts.most_common()]}
path=ROOT/"tmp/edition-2026-coverage-map/relation-shapes.json"
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"active_units":len(units),"shapes":len(counts),"top_shapes":counts.most_common(28),"evidence_path":str(path)},ensure_ascii=False))
