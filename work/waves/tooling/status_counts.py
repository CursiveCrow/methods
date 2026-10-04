"""Ledger status counts at a git ref (or the working tree when no ref).
Usage: python -B ... [REF...]"""
import collections, json, subprocess, sys, glob

def rows_at(ref):
    if ref is None:
        for f in sorted(glob.glob("spec/coverage/edition-2026/current-fulfillment/*.jsonl")):
            yield from (json.loads(l) for l in open(f, encoding="utf-8") if l.strip())
        return
    names = subprocess.run(["git", "ls-tree", "--name-only", ref, "spec/coverage/edition-2026/current-fulfillment/"],
                           capture_output=True, text=True, check=True).stdout.split()
    for n in names:
        if n.endswith(".jsonl"):
            text = subprocess.run(["git", "show", f"{ref}:{n}"], capture_output=True, text=True, encoding="utf-8", check=True).stdout
            yield from (json.loads(l) for l in text.splitlines() if l.strip())

for ref in (sys.argv[1:] or [None]):
    c = collections.Counter(r.get("status") for r in rows_at(ref))
    print(ref or "worktree", dict(sorted(c.items())), "total", sum(c.values()))
