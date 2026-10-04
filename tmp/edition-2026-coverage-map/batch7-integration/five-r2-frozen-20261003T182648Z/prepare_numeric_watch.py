"""Prepare current numeric-meaning proposals only; never apply any patch."""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from datetime import datetime, timezone
from pathlib import Path
sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
BASE = ROOT/"handbook"
spec = importlib.util.spec_from_file_location("batch7_capture_support",
                                            OUT/"capture_batch7_baseline.py")
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)
grounded = support.helper.grounded
registry = support.helper.registry

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    baseline = OUT/"pre-batch7-numeric-meanings.json"
    frozen = json.loads(baseline.read_text(encoding="utf-8"))
    watched = [BASE/"main.tex",BASE/"registry/symbols.csv",
               BASE/"registry/symbol-scopes.json",BASE/"bib/handbook.bib"]
    watched += sorted((BASE/"parts").glob("p[0-9][0-9].tex"))
    watched += sorted((BASE/"annex").glob("p[0-9][0-9].tex"))
    before = {p.relative_to(ROOT).as_posix():sha(p) for p in watched}
    index = registry.ReaderIndex(BASE)
    # Reuse the pure identity-mapping helper, not any old batch main.
    result = grounded.propose_numeric_migrations(frozen,index)
    for row in result["proposed_migration_rows"]:
        row["proposed"]["scope"] = row["proposed"]["scope"].replace("pre-batch5","pre-batch7")
        row["proposed"]["notes"] = row["proposed"]["notes"].replace("pre-batch5","pre-batch7")
        if row["binding"]:
            row["binding"]["presentation"] = row["binding"]["presentation"].replace("batch5","batch7")
    after = {p.relative_to(ROOT).as_posix():sha(p) for p in watched}
    result.update({
        "utc":datetime.now(timezone.utc).isoformat(),
        "baseline_file":baseline.name,"baseline_sha256":sha(baseline),
        "actual_chapter_headings":sum(h.kind=="chapter" and h.chapter is not None
                                     and h.part is not None for h in index.heading_records),
        "watched_before":before,"watched_after":after,
        "changed_during_capture":[p for p in before if before[p]!=after[p]],
        "standing":"Current actual anchor-to-frozen-identity mapping PROPOSALS ONLY. No old producer, collision/strict check, proof/source review, build or render. Future off-route chapters have no guessed placement. Nothing applied; B6 pending2 untouched.",
    })
    grounded.save("numeric-migrations",result)
    print(json.dumps({k:result[k] for k in (
        "utc","baseline_sha256","actual_chapter_headings",
        "unchanged_numeric_rows_examined","changed_during_capture")} |
        {"proposed_migration_rows":len(result["proposed_migration_rows"]),
         "unresolved_identity_records":len(result["unresolved"])}))

if __name__=="__main__":
    main()
