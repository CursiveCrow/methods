"""Split proposal previews into: au (established), genuine (an open verdict, gap or blocker),
omission (open only because an assessor omitted or keyed an owed item differently).
Usage: python -B work/waves/tooling/classify_disputes.py PROPOSALS.jsonl..."""
import json, sys

OMIT = ("not assessed in confirm", "but not in first", "assessed in neither")
out = {"au": [], "genuine": [], "omission": []}
for f in sys.argv[1:]:
    for line in open(f, encoding="utf-8"):
        p = json.loads(line)
        ms = p["set"]["missing_pieces"]
        if p["set"]["status"] == "authored_unreviewed":
            out["au"].append(p["section_id"])
        elif ms and all(m["kind"] == "assessment_dispute" and any(o in m["duty"] for o in OMIT) for m in ms):
            out["omission"].append(p["section_id"])
        else:
            out["genuine"].append(p["section_id"])
print(json.dumps({k: (len(v), v) for k, v in out.items()}))
