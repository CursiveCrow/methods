"""Ledger proposals from failed upgrade audits (tmor-upgrade-audit.js results). A section whose
fresh adversarial auditor found an owed component not covered returns to partial: its recorded
duties are kept and one writable duty is added per failed component, in the auditor's words.
Sections whose audit held produce no proposal.
Usage: python -B work/waves/tooling/audit_downgrades.py SINCE OUT.jsonl AUDIT_RESULTS.json..."""
import json
import sys
from pathlib import Path

sys.path.insert(0, "tools")
import ledger_patch as lp  # noqa: E402

since, out, inputs = sys.argv[1], sys.argv[2], sys.argv[3:]
ledger = lp.load_ledger(Path(".").resolve())
proposals = []
for path in inputs:
    for res in json.load(open(path, encoding="utf-8"))["results"]:
        if not res or res.get("all_covered"):
            continue
        sid = res["section_id"]
        row = ledger.by_section[sid]
        kept = [m for m in row.obj.get("missing_pieces") or []]
        added = [{"duty": f"{f['key']} ({f['verdict']}): {f['gap']}", "component_ids": [f["key"]],
                  "kind": "writable", "blocker_ref": None, "since": since} for f in res["failures"]]
        proposals.append({"section_id": sid, "original_row_sha256": row.row_sha256,
                          "set": {"status": "partial", "missing_pieces": kept + added},
                          "append_reader_evidence": [], "assessment_ids": [res["assessment_id"]],
                          "reason": f"{since}: fresh adversarial audit of the wave's upgrade found owed components not covered"})
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    for p in proposals:
        fh.write(json.dumps(p, ensure_ascii=False) + "\n")
print(len(proposals), "downgrade proposals:", [p["section_id"] for p in proposals])
