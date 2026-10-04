"""Immutable post-actual-five capture; pure helper only, never an old main."""
from __future__ import annotations
import hashlib,importlib.util,json,sys
from datetime import datetime,timezone
from pathlib import Path
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
BASE=ROOT/"handbook"
spec=importlib.util.spec_from_file_location("post_five_capture_support",OUT/"capture_batch7_baseline.py")
support=importlib.util.module_from_spec(spec);spec.loader.exec_module(support)
helper=support.helper
helper.OUT=OUT;helper.ARTIFACT_PREFIX=""
NAME="post-actual-five-numeric-baseline"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    target=OUT/(NAME+".json")
    if target.exists():
        existing=json.loads(target.read_text(encoding="utf-8"))
        print(json.dumps({"standing":"Immutable existing post-five capture retained",
            "utc":existing["utc"],"symbols":existing["canonical_row_count"],
            "bibliography":existing["canonical_bib_count"],"baseline_sha256":sha(target)}))
        return
    watched=[BASE/"main.tex",BASE/"registry/symbols.csv",
             BASE/"registry/symbol-scopes.json",BASE/"bib/handbook.bib"]
    watched+=sorted((BASE/"parts").glob("p[0-9][0-9].tex"))
    watched+=sorted((BASE/"annex").glob("p[0-9][0-9].tex"))
    before={p.relative_to(ROOT).as_posix():sha(p) for p in watched}
    payload=helper.capture_numeric_meanings(NAME,
        "Immutable actual baseline AFTER root applied all14 corrected R2 five-stage patches, BEFORE Savage/P13/P19 chapter routing. Applied R2, old11 historical packet, previous baselines/raws and B6 pending2 are not replayed. No proof/source acceptance or check/review.")
    after={p.relative_to(ROOT).as_posix():sha(p) for p in watched}
    receipt={"utc":datetime.now(timezone.utc).isoformat(),"baseline":target.name,
        "baseline_sha256":sha(target),"symbols":payload["canonical_row_count"],
        "bibliography":payload["canonical_bib_count"],
        "actual_chapter_headings":len(payload["chapters"]),
        "numeric_rows":len(payload["numeric_rows"]),
        "symbols_sha256":payload["canonical_symbols_sha256"],
        "scopes_sha256":payload["canonical_scopes_sha256"],
        "bib_sha256":payload["canonical_bib_sha256"],
        "watched_before":before,"watched_after":after,
        "changed_during_capture":[p for p in before if before[p]!=after[p]],
        "scope":{"parts":19,"planned_chapters":289,"main_sections":2475,"original_requirements":615},
        "standing":"Read-only capture only, no old main or checker/review/build/render; target immutable."}
    (OUT/"post-actual-five-capture-receipt.json").write_text(
        json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:receipt[k] for k in ("utc","baseline_sha256","symbols",
        "bibliography","actual_chapter_headings","numeric_rows","symbols_sha256",
        "scopes_sha256","bib_sha256","changed_during_capture")}))
if __name__=="__main__":main()
