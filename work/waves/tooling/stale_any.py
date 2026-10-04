"""List assessment files (under the given wave dirs) whose inputs.tex hashes are stale.
Usage: python -B ... WAVE..."""
import glob, json, sys
from pathlib import Path
sys.path.insert(0, "tools")
import ledger_patch as lp

root = Path(".").resolve()
for wave in sys.argv[1:]:
    n = bad = 0
    for f in sorted(glob.glob(f"spec/coverage/edition-2026/assessments/{wave}/*.json")):
        n += 1
        try:
            lp._validate_assessment_inputs_current(root, json.load(open(f, encoding="utf-8")))
        except lp.Refusal as e:
            bad += 1
            print(" ", e)
    print(wave, n, "files,", bad, "stale")
