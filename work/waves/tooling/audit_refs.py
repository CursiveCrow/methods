"""List blocked_source items whose blocker record's work (surname or SRC id) is not named in the
duty text. Usage: python -B ... PROPOSALS.jsonl"""
import json, sys
sys.path.insert(0, "tools")
import wave_proposals as w

acq = {}
for line in open("spec/coverage/edition-2026/acquisition-requests.jsonl", encoding="utf-8"):
    if line.strip():
        d = json.loads(line)
        acq[d["acq_id"]] = d
bad = 0
for line in open(sys.argv[1], encoding="utf-8"):
    p = json.loads(line)
    for m in p["set"]["missing_pieces"]:
        if m["kind"] != "blocked_source":
            continue
        key = acq.get(m["blocker_ref"], {}).get("key", "")
        tok = w.cite_tokens(key)
        if not (tok and tok[0] in w._fold(m["duty"])) and not key.startswith("NOID"):
            bad += 1
            print(p["section_id"], m["blocker_ref"], key, "|", m["duty"][:200].replace("\n", " "))
print("unmatched", bad)
