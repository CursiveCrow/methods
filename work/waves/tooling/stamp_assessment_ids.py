"""Add assessment_id (= file stem, the id the workflow named the file by) to assessment files
that omit it. Leaves every other field untouched. Usage: python -B ... FILE..."""
import json, os, sys

for f in sys.argv[1:]:
    d = json.load(open(f, encoding="utf-8"))
    if "assessment_id" in d:
        continue
    d = {"assessment_id": os.path.basename(f)[:-5], **d}
    json.dump(d, open(f, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print("stamped", f)
