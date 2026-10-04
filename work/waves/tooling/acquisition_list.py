"""Compile W1 scouting + verification into the user-facing acquisition list.

Reads work/waves/w01/acq/shard-*.verified.jsonl (falls back to shard-*.jsonl) and
work/waves/w01/census/shard-*.jsonl; writes
  spec/coverage/edition-2026/acquisition-requests.jsonl  (machine record, ACQ ids)
  work/waves/w01/ACQUISITION-LIST.md                      (for the user's approval)
  work/waves/w01/ACQUISITION-LIST.csv
Categories: A = identity confirmed, exact version, full body (ready to approve);
B = confirmed but version differs or full body unknown (approve only if acceptable);
C = no free copy found (needs a user-supplied file); D = unresolved/rejected candidates."""
import csv, glob, json, os, re
from collections import defaultdict

census = {}
for f in sorted(glob.glob("work/waves/w01/census/shard-*.jsonl")):
    for line in open(f, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            census[r["key"]] = r

cands = defaultdict(list)
for f in sorted(glob.glob("work/waves/w01/acq/shard-*.jsonl")):
    if f.endswith(".verified.jsonl"):
        continue
    vf = f.replace(".jsonl", ".verified.jsonl")
    src = vf if os.path.exists(vf) else f
    for line in open(src, encoding="utf-8"):
        if line.strip():
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            cands[r.get("key")].append(r)


def category(rows):
    best = None
    for r in rows:
        if r.get("state") == "no_free_copy":
            continue
        v = r.get("verification") or {}
        c = r.get("candidate") or {}
        ident = v.get("identity")
        vm = (v.get("version_match") or c.get("version_match") or "unknown")
        fb = (v.get("full_body") or c.get("full_body") or "unknown")
        if ident == "confirmed" and vm == "exact" and fb == "yes":
            rank = ("A", r)
        elif ident == "confirmed":
            rank = ("B", r)
        else:
            rank = ("D", r)
        if best is None or rank[0] < best[0]:
            best = rank
    return best if best else ("C", rows[0] if rows else None)


out, n = [], 0
for key in sorted(set(census) | set(cands)):
    cen = census.get(key, {})
    if cen.get("verdict") == "held_full":
        continue
    cat, row = category(cands.get(key, []))
    n += 1
    req = (row or {}).get("required") or cen.get("required") or {}
    cand = (row or {}).get("candidate") or {}
    ver = (row or {}).get("verification") or {}
    out.append({
        "acq_id": f"ACQ-2026-10-{n:04d}", "category": cat, "key": key,
        "census_verdict": cen.get("verdict"), "units": cen.get("units") or (row or {}).get("units") or [],
        "work": req.get("work"), "version": req.get("version"), "extent": req.get("extent"),
        "url": cand.get("url"), "host": cand.get("host"), "host_kind": cand.get("host_kind"),
        "version_match": ver.get("version_match") or cand.get("version_match"),
        "full_body": ver.get("full_body") or cand.get("full_body"), "size": cand.get("size"),
        "verification_notes": ver.get("notes"),
        "state": {"A": "candidate_verified", "B": "candidate_verified", "C": "needs_user_supplied_file",
                  "D": "unresolved"}[cat],
    })

os.makedirs("work/waves/w01", exist_ok=True)
with open("spec/coverage/edition-2026/acquisition-requests.jsonl", "w", encoding="utf-8", newline="\n") as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
with open("work/waves/w01/ACQUISITION-LIST.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["acq_id", "category", "work", "version", "extent", "url", "host_kind",
                                      "version_match", "full_body", "size", "census_verdict", "key", "units"])
    w.writeheader()
    for r in out:
        w.writerow({k: (";".join(r[k]) if isinstance(r.get(k), list) else r.get(k)) for k in w.fieldnames})

counts = defaultdict(int)
for r in out:
    counts[r["category"]] += 1
units_blocked = defaultdict(set)
for r in out:
    for u in r["units"]:
        units_blocked[r["category"]].add(u)
with open("work/waves/w01/ACQUISITION-LIST.md", "w", encoding="utf-8", newline="\n") as f:
    f.write("# Acquisition list r1 (W1 source census, 2026-10-03)\n\n")
    f.write("Downloads happen only for entries you approve. No shadow libraries were searched.\n\n")
    f.write("| Category | Meaning | Sources | Queue units affected |\n|---|---|---:|---:|\n")
    meaning = {"A": "identity confirmed, exact version, full body: ready to approve",
               "B": "identity confirmed; version differs or full body unknown: approve only if acceptable",
               "C": "no free copy found: needs a file you supply in source/references/",
               "D": "candidate unresolved or rejected on verification"}
    for c in "ABCD":
        f.write(f"| {c} | {meaning[c]} | {counts[c]} | {len(units_blocked[c])} |\n")
    for c in "ABCD":
        f.write(f"\n## Category {c}\n\n| ACQ | Work | Required version | URL | Host | Version match | Full body |\n|---|---|---|---|---|---|---|\n")
        for r in out:
            if r["category"] == c:
                cell = lambda s: str(s or "").replace("|", "/").replace("\n", " ")[:160]
                f.write(f"| {r['acq_id']} | {cell(r['work'])} | {cell(r['version'])} | {cell(r['url'])} | {cell(r['host_kind'])} | {cell(r['version_match'])} | {cell(r['full_body'])} |\n")
print(dict(counts), {c: len(units_blocked[c]) for c in "ABCD"})
