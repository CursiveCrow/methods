"""Assemble the saved read-only audit and compare its original manuscript snapshot."""
from __future__ import annotations

import collections
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path("C:/Dev/the-methods-of-reason")
OUT = ROOT / "spec/inventory/2026-09-06"


def read_json(name):
    return json.loads((OUT / name).read_text(encoding="utf-8-sig"))


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_csv(name):
    with (OUT / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def table(name, rows, fields):
    with (OUT / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v
                             for k, v in row.items() if k in fields})


def reg_name(value):
    return Path(value.replace("\\", "/")).stem


original = read_json("original-registers.json")
original_by_key = {(r["register"], r["id"]): r for r in original}
sources = ["parts-01-07-requirements.json", "parts-08-11-requirements.json",
           "parts-12-14-apparatus-requirements.json", "defects-requirements.json"]
rows, seen, problems = [], collections.Counter(), []
for name in sources:
    data = read_json(name)
    selected = data["requirements"] if isinstance(data, dict) else data
    for r in selected:
        register = reg_name(r["register"])
        key = (register, r["id"])
        seen[key] += 1
        o = original_by_key.get(key)
        if o is None:
            problems.append({"kind": "unknown_requirement", "key": key, "inventory": name})
            continue
        if r.get("item") is not None and r["item"] != o.get("item"):
            problems.append({"kind": "item_text_mismatch", "key": key, "inventory": name})
        if register == "defects":
            for field in ("finding", "required_fix", "acceptance"):
                if r.get(field) != o.get(field):
                    problems.append({"kind": "defect_text_mismatch", "key": key, "field": field})
            for field, historical in (("status", "historical_status"), ("disposition", "historical_disposition")):
                if r.get(historical) != o.get(field):
                    problems.append({"kind": "defect_history_mismatch", "key": key, "field": field})
        part = r.get("part") or o.get("target_part") or o.get("target_home") or "cross_book"
        rows.append({
            "register": register, "id": r["id"], "part": part,
            "item": o.get("item") or o.get("finding"),
            "domain": o.get("domain", ""), "original_status": o.get("status", ""),
            "original_treatment": o.get("treatment", ""), "original_priority": o.get("priority", ""),
            "content_state": r.get("content_state", ""), "proof_state": r.get("proof_state", ""),
            "defect_current_state": r.get("current_state", ""),
            "evidence": r.get("evidence", r.get("current_evidence", [])),
            "remaining": r.get("concrete_remaining", r.get("remaining_verification", "")),
            "narrow_content_or_repair_verified": bool(r.get("completion_verified")),
            "full_compendium_completion_verified": None,
            "inventory_file": name,
            "original_register_row": o,
            "inventory_assessment": r,
        })
missing = sorted(set(original_by_key) - set(seen))
duplicates = sorted([key for key, count in seen.items() if count != 1])
problems.extend({"kind": "missing_requirement", "key": key} for key in missing)
problems.extend({"kind": "duplicate_requirement", "key": key, "count": seen[key]} for key in duplicates)
dump("requirement-reconciliation.json", {
    "original_count": len(original), "inventoried_count": len(rows), "unique_count": len(seen),
    "problems": problems, "original_domain_x_rows": sum(r.get("domain") == "x" for r in original),
    "inventoried_domain_x_rows": sum(r["domain"] == "x" for r in rows),
    "method": "Exact register/id pairing, original item/defect text comparison, and separate retained historical data."
})
if problems:
    raise SystemExit(json.dumps(problems, indent=2))
order = {name: i for i, name in enumerate(("new-content", "depth-gaps", "defects", "apparatus"))}
rows.sort(key=lambda r: (order[r["register"]], r["id"]))
dump("complete-requirement-ledger.json", {
    "captured_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Every original row; historical treatment ceilings are not completion authority.",
    "verification_meaning": "The narrow flag preserves a bounded inspected content/repair result. False can mean a definite gap or an explicit verification unknown. Full-compendium completion is not established by this inventory.",
    "requirements": rows
})
fields = ["register", "id", "part", "item", "domain", "original_status", "original_treatment",
          "original_priority", "content_state", "proof_state", "defect_current_state", "evidence",
          "remaining", "narrow_content_or_repair_verified", "full_compendium_completion_verified", "inventory_file"]
table("complete-requirement-ledger.csv", rows, fields)

totals = {
    "rows": len(rows), "by_register": dict(collections.Counter(r["register"] for r in rows)),
    "content_states_excluding_defects": dict(collections.Counter(r["content_state"] for r in rows if r["register"] != "defects")),
    "proof_states_excluding_defects": dict(collections.Counter(r["proof_state"] for r in rows if r["register"] != "defects")),
    "defect_states": dict(collections.Counter(r["defect_current_state"] for r in rows if r["register"] == "defects")),
    "bounded_verified_ids": [r["id"] for r in rows if r["narrow_content_or_repair_verified"]],
    "domain_x_ids": [r["id"] for r in rows if r["domain"] == "x"],
    "completion_percentage": None,
    "completion_percentage_reason": "Rows overlap, differ greatly in scope and effort, and do not exhaust the inherited source/registered source-presentation obligations. Present, cited, and locally proved are not one acceptance measure."
}
dump("requirement-inventory-summary.json", totals)

# Keep each row readable without discarding its exact original fields or evidence.
def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def evidence_text(value):
    rendered = []
    for entry in value:
        if isinstance(entry, dict):
            path = entry.get("path", "")
            line = entry.get("line")
            label = path + (":" + str(line) if line else "")
            if path and (ROOT / path).is_file():
                rendered.append(f'[{cell(label)}](<{(ROOT / path).as_posix()}{":" + str(line) if line else ""}>)')
            else:
                rendered.append(cell(label or json.dumps(entry, ensure_ascii=False)))
        else:
            rendered.append(cell(entry))
    return "; ".join(rendered)


md = ["# Complete manuscript requirement inventory", "",
      "Snapshot: 6 September 2026 Pacific time. All 615 original requirements are represented exactly once, including all 15 original domain-x rows. Original text and history are retained in the companion JSON and CSV. The book was not edited.", "",
      "`Bounded yes` means only that the specifically identified content or repair was verified in the inventory. It does not mean full source, mathematical, apparatus, or publication acceptance. All other rows state their actual remaining work or verification question; they are not automatically unwritten.", ""]
for register in order:
    group = [r for r in rows if r["register"] == register]
    md += [f"## {register} ({len(group)} rows)", "",
           "| ID / home | Original requirement | Current content / proof or defect state | Current evidence | Remaining work or verification | Bounded verification |",
           "| --- | --- | --- | --- | --- | --- |"]
    for r in group:
        state = r["defect_current_state"] or (r["content_state"] + " / " + r["proof_state"])
        md.append("| " + " | ".join([cell(r["id"] + " / " + r["part"]), cell(r["item"]), cell(state),
                                       evidence_text(r["evidence"]), cell(r["remaining"]),
                                       "Bounded yes" if r["narrow_content_or_repair_verified"] else "Not established"]) + " |")
    md.append("")
(OUT / "complete-requirement-ledger.md").write_text("\n".join(md), encoding="utf-8")

summary = read_json("inventory-summary.json")
latex = read_csv("latex-files.csv")
units = read_csv("mathematical-environments.csv")
headings = read_csv("headings.csv")
per_part = []
for n in range(1, 15):
    part = "P" + str(n)
    selected = [r for r in latex if r["active"] == "True" and part in json.loads(r["parts"])]
    envs = summary["per_part_environment_counts"].get(part, {})
    declared = [r for r in units if r["active"] == "True" and part in json.loads(r["parts"]) and r["declared_status"]]
    prose = [r for r in headings if part in json.loads(r["parts"]) and r["level"] in {"paragraph", "subparagraph"}
             and re.search(r"\b(proof|sketch|derivation|completeness|soundness|construction)\b", r["title"], re.I)]
    per_part.append({
        "part": part, "reachable_files_with_part_ownership": len(selected),
        "source_lines_with_part_ownership": sum(int(r["lines"]) for r in selected),
        "body_lines_including_restoration": sum(int(r["lines"]) for r in selected if "body" in json.loads(r["areas"]) and r["role"] != "generated"),
        "annex_lines": sum(int(r["lines"]) for r in selected if "annex" in json.loads(r["areas"])),
        "generated_lines": sum(int(r["lines"]) for r in selected if r["role"] == "generated"),
        "annex_items": envs.get("annexitem", 0), "proof_environments": envs.get("proof", 0),
        "proofplan_environments": envs.get("proofplan", 0), "proof_or_result_paragraph_headings": len(prose),
        "structured_result_declarations": len(declared),
        "declared_proved": envs.get("status_proved", 0), "declared_sketched": envs.get("status_sketched", 0),
        "declared_cited": envs.get("status_cited", 0),
        "raw_result_environments": sum(envs.get(k, 0) for k in ("theorem", "lemma", "corollary", "proposition")),
        "new_content_rows": sum(r["part"] == part and r["register"] == "new-content" for r in rows),
        "depth_rows": sum(r["part"] == part and r["register"] == "depth-gaps" for r in rows)
    })
table("per-part-census.csv", per_part, list(per_part[0]))
dump("per-part-census.json", per_part)
table("unrouted-latex-files.csv", [r for r in latex if r["active"] != "True"], list(latex[0]))

print(json.dumps({"requirements": totals, "per_part": per_part}, ensure_ascii=False, indent=2))

# A second independent path enumeration also detects additions and removals.
before = read_json("manuscript-snapshot-before.json")
suffixes = {".tex", ".sty", ".bib", ".csv", ".md", ".pdf", ".png", ".jpg", ".jpeg", ".svg", ".eps", ".ps"}
paths = {p for p in (ROOT / "handbook").rglob("*") if p.is_file() and p.suffix.lower() in suffixes}
paths |= {p for p in (ROOT / "spec/registers").rglob("*") if p.is_file() and p.suffix.lower() in {".csv", ".md"}}
paths |= {ROOT / p for p in ("source/formal-logic-reference.tex", "source/formal-logic-reference.pdf",
                             "spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md", "spec/INHERITED-CORPUS-MANIFEST.md")
          if (ROOT / p).is_file()}
after_rows = []
for path in sorted(paths, key=lambda p: p.relative_to(ROOT).as_posix()):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    after_rows.append({"path": path.relative_to(ROOT).as_posix(), "bytes": path.stat().st_size, "sha256": digest.hexdigest()})
after_hash = hashlib.sha256("".join(f'{r["path"]}\t{r["sha256"]}\n' for r in after_rows).encode()).hexdigest()
dump("manuscript-snapshot-after.json", {"captured_utc": datetime.now(timezone.utc).isoformat(), "aggregate_sha256": after_hash, "files": after_rows})
bmap = {r["path"]: r for r in before["files"]}
amap = {r["path"]: r for r in after_rows}
comparison = {"before_sha256": before["aggregate_sha256"], "after_sha256": after_hash,
              "before_files": len(bmap), "after_files": len(amap),
              "added": sorted(set(amap) - set(bmap)), "removed": sorted(set(bmap) - set(amap)),
              "changed": [p for p in sorted(set(bmap) & set(amap)) if bmap[p]["sha256"] != amap[p]["sha256"]]}
comparison["unchanged"] = not any(comparison[k] for k in ("added", "removed", "changed"))
dump("snapshot-comparison.json", comparison)
print(json.dumps(comparison, indent=2))
