"""Build the W1 source-census input: one record per distinct required source presentation
across all queue units, keyed by source_id (or a normalized identity when absent), with the
units that need it and every recorded identity/extent/local-path field. Shards for agents.

Usage: python -B work/waves/tooling/census_input.py OUTDIR SHARD_SIZE"""
import json, os, re, sys
from collections import OrderedDict

QUEUE = "spec/coverage/edition-2026/completion-work-queue.jsonl"
KEEP = ("source_id", "benchmark_id", "title", "authors", "version", "container", "doi", "container_doi",
        "citation_key", "extent", "precise_extent", "required_extent", "printed_pages", "contents_start_page",
        "end_page", "locator", "body_state", "body_acquisition_standing", "local_path", "local_artifact",
        "local_artifacts", "artifacts", "sha256", "source_sha256", "source_url", "publisher_url", "version_boundary")


def key_of(sp):
    if sp.get("source_id"):
        return sp["source_id"]
    ident = " ".join(str(sp.get(k, "")) for k in ("authors", "title", "version", "benchmark_id"))
    return "NOID:" + re.sub(r"\W+", "-", ident.lower()).strip("-")[:120]


def main(outdir, size):
    recs = OrderedDict()
    for line in open(QUEUE, encoding="utf-8-sig"):
        u = json.loads(line)
        for sp in u.get("source_presentations", []):
            k = key_of(sp)
            r = recs.setdefault(k, {"key": k, "presentations": [], "units": [], "unit_states": {}})
            slim = {f: sp[f] for f in KEEP if f in sp}
            if slim not in r["presentations"]:
                r["presentations"].append(slim)
            if u["unit_id"] not in r["units"]:
                r["units"].append(u["unit_id"])
                r["unit_states"][u["unit_id"]] = [u.get("content_state"), u.get("source_state")]
    os.makedirs(outdir, exist_ok=True)
    allrecs = list(recs.values())
    with open(os.path.join(outdir, "census-input.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for r in allrecs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    shards = [allrecs[i:i + size] for i in range(0, len(allrecs), size)]
    for i, sh in enumerate(shards, 1):
        with open(os.path.join(outdir, f"shard-{i:03d}.jsonl"), "w", encoding="utf-8", newline="\n") as f:
            for r in sh:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(len(allrecs), "distinct presentations;", len(shards), "shards of", size)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
