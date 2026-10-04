"""Preserve the previously saved R2 draft bytes before resumed preparation."""
import hashlib,json
from pathlib import Path
OUT=Path(__file__).resolve().parent
DEST=OUT/"five-r2-draft-20261003T172603Z"
DEST.mkdir(exist_ok=True)
NAMES=["five-r2-stage.json","five-r2-transformed-rows.json",
       "five-r2-scope-bindings.json","five-r2-transformations.json",
       "five-r2-family-members.json","five-r2-decisions-required.json",
       "five-r2-root-decisions.json","prepare_five_stage_r2.py",
       "batch7-proposal-numeric-migrations.json"]
records=[]
for name in NAMES:
    data=(OUT/name).read_bytes();target=DEST/name
    if target.exists() and target.read_bytes()!=data:
        raise RuntimeError("Old R2 draft already archived with different bytes")
    if not target.exists():target.write_bytes(data)
    records.append({"name":name,"sha256":hashlib.sha256(data).hexdigest()})
receipt=DEST/"historical-standing.json"
if not receipt.exists():
    receipt.write_text(json.dumps({"standing":"Historical saved/unapplied draft from the read-only status interruption. No patch existed or was applied; one dQ binding dependency remained. Preserve bytes; successor preparation is separate.",
                                 "artifacts":records},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"directory":DEST.name,"files":len(records)}))
