"""Assemble the W2-b restoration-correction rationale (one '## <id>' section per edited capture)
from the capture agents' rationale files, after repairing unescaped backslashes in their
decision files. Usage: python -B work/waves/w02b/assemble_restoration.py IDS.json"""
import glob
import json
import re
import sys

for path in glob.glob("work/waves/w02b/lead/applied-*.json"):
    text = open(path, encoding="utf-8").read()
    try:
        json.loads(text)
    except json.JSONDecodeError:
        data = json.loads(re.sub(r'\\(?![\\"/bfnrtu])', r"\\\\", text))
        json.dump(data, open(path, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
        print("repaired", path)

pids = json.load(open(sys.argv[1], encoding="utf-8"))
parts = [
    "# W2-b lead corrections to restoration captures\n",
    "Corrections applied by the lead to active restoration captures during the W2-b wave-end "
    "integration (2026-10-05), under the correction policy of spec/EDITION-2026-CONTRACT.md "
    "(\"Reader-facing content and corrections\") and handbook/CONVENTIONS.md (2026-09-06). Each section "
    "is keyed by the provenance id whose version-4 corrected-reader record cites it. The requests come "
    "from W2-a and W2-b author patch requests (work/waves/w02/patches, work/waves/w02b/patches); "
    "per-request decisions are in work/waves/w02b/lead/applied-<id>.json.\n",
]
for pid in pids:
    body = open(f"work/waves/w02b/lead/rationale-{pid}.md", encoding="utf-8").read().strip()
    if not body.startswith(f"## {pid}"):
        body = f"## {pid}\n\n{body}"
    parts.append(body + "\n")
out = "spec/research/edition-2026-w02b-restoration-corrections.md"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(parts))
print(len(pids), "sections ->", out)
