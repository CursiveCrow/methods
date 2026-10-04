"""Export source surfaces for coverage mapping; run no manuscript checks."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import check as grammar
import build_named_theorem_index as route

DEST = ROOT / "spec/coverage/edition-2026"
DEST.mkdir(parents=True, exist_ok=True)
OUT = DEST / "new-domain-destination-evidence.jsonl"
RECEIPT = DEST / "new-domain-destination-evidence-receipt.json"
if OUT.exists() or RECEIPT.exists():
    raise SystemExit("Preserve the previous export; use a new revision or an explicit patch.")

def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()

def clean(raw: str) -> str:
    return grammar.strip_verbatims(grammar.strip_comments(raw))

def env_end(body: str, name: str, start: int) -> int | None:
    depth = 1
    pat = re.compile(r"\\(begin|end)\{" + re.escape(name) + r"\}")
    for found in pat.finditer(body, start):
        depth += 1 if found.group(1) == "begin" else -1
        if depth == 0:
            return found.start()
    return None

live = {p.resolve() for p in route.reachable_files()}
paths: set[Path] = set()
for part in range(15, 20):
    for home in ("parts", "annex"):
        paths.update((ROOT / "handbook" / home / f"p{part:02}").glob("*.tex"))
for stem in ("small-clause-standard", "small-clause-optimizations"):
    for home in ("parts", "annex"):
        p = ROOT / "handbook" / home / "p12" / f"{stem}.tex"
        if p.exists():
            paths.add(p)
paths.add(ROOT / "handbook/parts/p11/reasons-and-rationality.tex")

records = []
label_destinations: dict[str, list[dict]] = {}
problems = []
for path in sorted(paths):
    raw_bytes = path.read_bytes()
    raw = raw_bytes.decode("utf-8-sig")
    body = clean(raw)
    rel = path.relative_to(ROOT).as_posix()
    entries = []
    for match in grammar.HB_ENV_RE.finditer(body):
        env = match.group(1)
        arity = 3 if env in grammar.HB_STATUS_ENVS or env == "annexitem" else 2
        args, end = grammar.scan_braced_args(body, match.end(), arity)
        last = env_end(body, env, end)
        if len(args) != arity or last is None:
            problems.append({"path": rel, "line": body.count("\n", 0, match.start()) + 1,
                             "problem": "unparsed_named_environment", "environment": env})
            continue
        title = args[-1]
        label = args[0]
        status = args[1] if env in grammar.HB_STATUS_ENVS else None
        backref = args[1] if env == "annexitem" else None
        rec = {
            "environment": env, "label": label, "title": title,
            "line": body.count("\n", 0, match.start()) + 1,
            "end_line": body.count("\n", 0, last) + 1,
            "declared_status": status, "annex_backref": backref,
            "text": body[end:last].strip(),
            "evidence_limit": "Literal source surface; status text and proof presence do not establish completion."
        }
        entries.append(rec)
        label_destinations.setdefault(label, []).append({"path": rel, "line": rec["line"]})
    unknown = sorted(set(re.findall(r"\\begin\{(hb[A-Za-z]+)\}", body))
                     - set(grammar.HB_THEOREM_CLASS))
    if unknown:
        problems.append({"path": rel, "problem": "other_hb_environments", "names": unknown})
    headings = []
    for m in re.finditer(r"\\(chapter|section|subsection)\*?\s*", body):
        args, _ = grammar.scan_braced_args(body, m.end(), 1)
        if args:
            headings.append({"kind": m.group(1), "title": args[0],
                             "line": body.count("\n", 0, m.start()) + 1})
    citations = set()
    for m in re.finditer(r"\\[A-Za-z]*cite[A-Za-z]*\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^{}]*)\}", body):
        citations.update(k.strip() for k in m.group(1).split(",") if k.strip())
    for rec in entries:
        if rec["declared_status"] and rec["declared_status"].startswith("cited="):
            citations.update(k.strip() for k in rec["declared_status"][6:].split(",") if k.strip())
    records.append({
        "path": rel, "sha256": sha(raw_bytes), "bytes": len(raw_bytes),
        "line_count": len(raw.splitlines()), "in_static_reader_graph": path.resolve() in live,
        "headings": headings, "citation_keys": sorted(citations), "entries": entries,
        "scope": "Current new-domain/selected continuation source surfaces, including explicitly unrouted drafts."
    })

for record in records:
    for entry in record["entries"]:
        status = entry["declared_status"] or ""
        if status.startswith(("proved=", "sketched=")):
            target = status.split("=", 1)[1]
            entry["declared_proof_destinations"] = label_destinations.get(target, [])
            entry["proof_presence_is_not_completion"] = True

with OUT.open("w", encoding="utf-8", newline="\n") as handle:
    for record in records:
        handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")

counts = {
    "files": len(records),
    "body_files": sum("/parts/" in r["path"] for r in records),
    "annex_files": sum("/annex/" in r["path"] for r in records),
    "named_entry_surfaces": sum(len(r["entries"]) for r in records),
    "unrouted_files": [r["path"] for r in records if not r["in_static_reader_graph"]],
}
receipt = {
    "purpose": "Coverage-map destination evidence, not manuscript review or admission",
    "parser": "Existing tools/check.py parsing helpers; existing named-index literal-input graph",
    "parser_hashes": {p: sha((ROOT / p).read_bytes()) for p in
                     ("tools/check.py", "tools/build_named_theorem_index.py")},
    "scope": "P15-P19 body/annex files plus saved P11 reasons and P12 small-clause continuations",
    "counts": counts, "parse_questions": problems,
    "output_path": OUT.relative_to(ROOT).as_posix(), "output_sha256": sha(OUT.read_bytes()),
    "limitations": [
        "Static literal input graph, not execution of arbitrary TeX macros or conditionals.",
        "Existing source assertions and labels are preserved as data, not accepted as true or complete.",
        "A file or named entry is not automatically a unique source-specific intellectual unit.",
        "Required components, source extents and gaps must still be mapped against the edition obligations."
    ]
}
RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"receipt": RECEIPT.relative_to(ROOT).as_posix(), **counts,
                  "parse_questions": len(problems)}, ensure_ascii=False))
