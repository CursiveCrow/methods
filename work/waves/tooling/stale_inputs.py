"""For each AU proposal, report cited assessments whose inputs.tex hashes are stale.
Usage: python -B ... PROPOSALS.jsonl"""
import json, sys
from pathlib import Path
sys.path.insert(0, "tools")
import ledger_patch as lp

root = Path(".").resolve()
for line in open(sys.argv[1], encoding="utf-8"):
    p = json.loads(line)
    if p["set"]["status"] != "authored_unreviewed":
        continue
    for a in lp._load_assessments(root, p["assessment_ids"]):
        try:
            lp._validate_assessment_inputs_current(root, a)
        except lp.Refusal as e:
            print(p["section_id"], e)
