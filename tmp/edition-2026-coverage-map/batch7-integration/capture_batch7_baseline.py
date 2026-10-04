"""Capture batch7 before routing; import reusable helpers, never their mains."""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from datetime import datetime, timezone
from pathlib import Path
sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
BASE = ROOT / "handbook"
sys.path.insert(0, str(ROOT / "tools"))
spec = importlib.util.spec_from_file_location(
    "batch6_capture_helper_only", OUT.parent/"batch6-integration/prepare_batch6.py")
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
helper.OUT = OUT
helper.grounded.OUT = OUT
helper.grounded.PREFIX = "batch7-proposal-"
helper.ARTIFACT_PREFIX = ""
NAME = "pre-batch7-numeric-meanings"

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    baseline_path = OUT / (NAME + ".json")
    if baseline_path.exists():
        old = json.loads(baseline_path.read_text(encoding="utf-8"))
        print(json.dumps({"standing":"Existing immutable baseline retained",
            "utc":old["utc"],"symbols":old["canonical_row_count"],
            "bibliography":old["canonical_bib_count"],
            "baseline_sha256":sha(baseline_path)}))
        return
    watched = [BASE/"registry/symbols.csv",BASE/"registry/symbol-scopes.json",
               BASE/"bib/handbook.bib",BASE/"main.tex"]
    watched += sorted((BASE/"parts").glob("p[0-9][0-9].tex"))
    watched += sorted((BASE/"annex").glob("p[0-9][0-9].tex"))
    before = {p.relative_to(ROOT).as_posix():sha(p) for p in watched}
    frozen = helper.capture_numeric_meanings(NAME,
        "Immutable actual pre-batch7 baseline BEFORE any B7 writer route; "
        "includes current B6 and root six clausal rows/three proofs. "
        "No old producer run, no route credit, no review or acceptance.")
    after = {p.relative_to(ROOT).as_posix():sha(p) for p in watched}
    receipt = {
        "utc":datetime.now(timezone.utc).isoformat(),
        "baseline":baseline_path.name,"baseline_sha256":sha(baseline_path),
        "symbols":frozen["canonical_row_count"],
        "bibliography":frozen["canonical_bib_count"],
        "actual_chapters":len(frozen["chapters"]),
        "numeric_rows":len(frozen["numeric_rows"]),
        "symbols_sha256":frozen["canonical_symbols_sha256"],
        "scopes_sha256":frozen["canonical_scopes_sha256"],
        "bib_sha256":frozen["canonical_bib_sha256"],
        "watched_before":before,"watched_after":after,
        "changed_during_capture":[p for p in before if before[p]!=after[p]],
        "manifest_sha256":sha(ROOT/"spec/research/edition-2026-authoring-batch-intake-7.json"),
        "scope":{"parts":19,"planned_chapters":289,"main_sections":2475,
                 "original_requirements":615},
        "standing":"Read-only route/index capture, not check/review; baseline immutable.",
    }
    (OUT/"baseline-capture-receipt.json").write_text(
        json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:receipt[k] for k in (
        "utc","baseline_sha256","symbols","bibliography","actual_chapters",
        "numeric_rows","symbols_sha256","scopes_sha256","bib_sha256",
        "changed_during_capture")}))

if __name__ == "__main__":
    main()
