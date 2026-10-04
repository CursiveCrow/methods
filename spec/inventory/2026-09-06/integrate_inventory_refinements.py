"""Integrate current read-only findings without changing book or original ledgers."""
from __future__ import annotations
import collections
import csv
from datetime import datetime, timezone
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("C:/Dev/the-methods-of-reason")
OUT = ROOT / "spec/inventory/2026-09-06"


def load(name):
    return json.loads((OUT / name).read_text(encoding="utf-8-sig"))


def save(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


initial_path = OUT / "initial-requirement-ledger.json"
base = load("initial-requirement-ledger.json" if initial_path.exists() else "complete-requirement-ledger.json")
if not initial_path.exists():
    save("initial-requirement-ledger.json", base)
rows = base["requirements"]
lookup = {r["id"]: r for r in rows}
evidence_checks, hash_cache, issues = [], {}, []


def record_evidence(owner, evidence):
    path_text = evidence.get("path")
    expected = evidence.get("sha256")
    if not path_text or not expected:
        return
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    key = str(path)
    if key not in hash_cache:
        if not path.is_file():
            hash_cache[key] = (None, None)
        else:
            raw = path.read_bytes()
            hash_cache[key] = (hashlib.sha256(raw).hexdigest(),
                               len(raw.decode("utf-8-sig", errors="replace").splitlines()) if path.suffix.lower() in {".tex", ".sty", ".md", ".csv", ".json", ".py"} else None)
    actual, lines = hash_cache[key]
    start = evidence.get("start_line", evidence.get("start"))
    end = evidence.get("end_line", evidence.get("end"))
    matches = actual == str(expected).lower()
    range_valid = (1 <= start <= end <= lines) if isinstance(start, int) and isinstance(end, int) and lines is not None else None
    result = {"owner": owner, "path": path_text, "expected_sha256": str(expected).lower(), "current_sha256": actual,
              "hash_matches": matches, "read_start": start, "read_end": end, "range_valid": range_valid}
    evidence_checks.append(result)
    if not matches or range_valid is False:
        issues.append(result)


refinement_counts = {}
for name, family in (("apparatus-completion-inventory.json", "apparatus"),
                     ("defect-mapping-completion.json", "defects"),
                     ("remaining-defect-components.json", "defects_remaining"),
                     ("remaining-content-mappings.json", "content")):
    if not (OUT / name).exists():
        continue
    data = load(name)
    updated = 0
    for detail in data["rows"]:
        row = lookup[detail["id"]]
        original = row["original_register_row"]
        if family == "apparatus":
            for field in ("item", "spec"):
                if detail.get(field) != original.get(field):
                    issues.append({"owner": row["id"], "kind": "original_field_mismatch", "field": field})
            outcome = detail["content_disposition"]
            components = detail["required_components"]
            remaining = detail["concrete_remaining"]
            investigated = detail["inventory_fields_investigated"]
            evidence = detail["reading_coverage"]
        elif family == "defects_remaining":
            for field, value in detail["original"].items():
                if value != original.get(field):
                    issues.append({"owner": row["id"], "kind": "original_field_mismatch", "field": field})
            outcome = detail["state"]
            components = detail["components"]
            remaining = detail["remaining_book_obligation"]
            investigated = data["inventory_complete"] and row["id"] not in data["remaining_ids"]
            evidence = detail["read_evidence"]
        elif family == "defects":
            for field, detail_field in (("finding", "original_finding"), ("required_fix", "original_required_fix"), ("acceptance", "original_acceptance")):
                if detail.get(detail_field) != original.get(field):
                    issues.append({"owner": row["id"], "kind": "original_field_mismatch", "field": field})
            outcome = detail["inventory_outcome"]
            components = detail["component_findings"]
            remaining = detail["remaining_book_obligation"]
            investigated = detail["mapping_complete"]
            evidence = detail["read_evidence"]
        else:
            if detail.get("item") != original.get("item"):
                issues.append({"owner": row["id"], "kind": "original_item_mismatch"})
            outcome = detail["inventory_outcome"]
            components = detail["components"]
            remaining = detail["concrete_remaining"]
            investigated = detail["mapping_complete"]
            evidence = detail["read_evidence"]
        row["refined_inventory"] = {"source": name, "outcome": outcome, "components": components,
                                     "remaining_book_work": remaining, "fields_investigated": investigated,
                                     "reading_evidence": evidence, "complete_assessment": detail}
        row["current_remaining"] = remaining
        for item in evidence:
            record_evidence(row["id"], item)
        updated += 1
    refinement_counts[name] = updated

full_read_files = []
def validate_intervals(owner, path, expected_hash, count, intervals):
    cursor, valid = 1, True
    for interval in intervals:
        if isinstance(interval, list):
            start, end = interval
            interval_hash = expected_hash
        else:
            start, end = interval["start"], interval["end"]
            interval_hash = interval.get("sha256", expected_hash)
        if start != cursor or end < start or str(interval_hash).lower() != str(expected_hash).lower():
            valid = False
        cursor = end + 1
    valid = valid and cursor == count + 1
    if not valid:
        issues.append({"owner": owner, "path": path, "kind": "full_read_interval_coverage_mismatch"})
    record_evidence(owner, {"path": path, "sha256": expected_hash, "start_line": 1, "end_line": count})
    return valid

for path in sorted(OUT.glob("p09-*-full-text-inventory.json")):
    data = load(path.name)
    if not data.get("inventory_complete"):
        continue
    for item in data.get("files", []):
        manuscript = item["path"]
        count = item.get("line_count", item.get("lines"))
        expected_hash = item["sha256"]
        identity = item.get("id")
        if not identity:
            stem = Path(manuscript).stem
            candidate = "N" + stem[1:] if stem.startswith("n-") else None
            identity = candidate if candidate in lookup else None
        owner = identity or manuscript
        valid = validate_intervals(owner, manuscript, expected_hash, count, item.get("read_intervals", []))
        detail = {"source": path.name, "manuscript": manuscript, "line_count": count, "sha256": expected_hash,
                  "all_manuscript_lines_read": item.get("all_lines_read", item.get("next_unread_line") is None),
                  "next_unread_line": item.get("next_unread_line"), "sequential_interval_coverage_matches": valid,
                  "remaining_completion_obligations": item.get("concrete_remaining", item.get("boundaries", [])),
                  "completion_verified": item.get("completion_verified", False)}
        detail["content_state"] = item.get("content_state")
        detail["proof_state"] = item.get("proof_state")
        prefix = "N" + str(int(identity.rsplit("-",1)[1])) if identity and identity.startswith("N-c-") else None
        for obligation in data.get("remaining_completion_obligations", []):
            if isinstance(obligation, dict) and prefix and prefix in obligation.get("id", ""):
                detail["remaining_completion_obligations"].append(obligation)
        full_read_files.append(detail)
        if identity:
            lookup[identity]["full_text_inventory"] = detail
            matches = [m for m in data.get("requirement_reconciliation", data.get("requirement_mapping", [])) if m.get("id") == identity]
            if matches:
                lookup[identity]["current_topic_components"] = {"source": path.name, "records": matches}
            original_detail = item.get("original_requirement", {})
            original_detail = original_detail.get("row", original_detail.get("original_row", original_detail))
            if original_detail and original_detail.get("item") != lookup[identity]["original_register_row"].get("item"):
                issues.append({"owner": identity, "kind": "multi_full_read_original_item_mismatch"})
    requirement = data.get("original_requirement", {})
    if isinstance(requirement, dict):
        original_detail = requirement.get("row", requirement.get("original_row", requirement))
        identity = original_detail.get("id")
    else:
        identity = None
    if identity not in lookup:
        continue
    row = lookup[identity]
    for field in ("item", "sources", "notes"):
        value = original_detail.get(field)
        if field == "sources" and isinstance(value, list):
            value = "; ".join(value)
        if field in original_detail and value != row["original_register_row"].get(field):
            issues.append({"owner": identity, "kind": "full_read_original_field_mismatch", "field": field})
    intervals_ok = validate_intervals(identity, data["manuscript"], data.get("final_sha256", data["sha256"]),
                                      data["line_count"], data.get("read_intervals", []))
    row["full_text_inventory"] = {"source": path.name, "manuscript": data.get("manuscript"),
                                  "line_count": data.get("line_count"), "sha256": data.get("final_sha256", data.get("sha256")),
                                  "all_manuscript_lines_read": data.get("all_manuscript_lines_read"),
                                  "next_unread_line": data.get("next_unread_line"),
                                  "sequential_interval_coverage_matches": intervals_ok,
                                  "remaining_completion_obligations": data.get("remaining_completion_obligations", []),
                                  "completion_verified": data.get("completion_verified")}
    full_read_files.append(row["full_text_inventory"])

unique_full_read = {r["manuscript"]: r for r in full_read_files}
save("full-text-reading-coverage.json", {"files": full_read_files, "unique_files": len(unique_full_read),
                                       "unique_lines": sum(r["line_count"] for r in unique_full_read.values()),
                                       "scope": "Only complete sequential read records are counted. This is reading coverage, not proof acceptance; dependency and partial-range reads are separate."})

def remaining_texts(value):
    if isinstance(value, str):
        return [value] if value else []
    result = []
    for item in value or []:
        if isinstance(item, str):
            result.append(item)
        elif isinstance(item, dict):
            text = item.get("obligation", item.get("remaining", item.get("finding", "")))
            if text:
                result.append(text)
    return result

new_findings = load("additional-current-content-findings.json")["findings"]
for row in rows:
    initial = {key: row.get(key) for key in ("content_state", "proof_state", "defect_current_state", "remaining", "evidence", "inventory_file", "narrow_content_or_repair_verified", "inventory_assessment")}
    row["initial_assessment"] = initial
    current = {"content_state": initial["content_state"] or initial["defect_current_state"],
               "proof_or_validation_state": initial["proof_state"] or "See recorded repair and review components.",
               "remaining_book_work": remaining_texts(initial["remaining"]), "evidence": initial["evidence"],
               "evidence_sources": [initial["inventory_file"]], "known_findings": [],
               "assessment_scope": "Current text/content/proof standing, source evidence and outstanding book work; not whole-book mathematical or publication acceptance."}
    refined = row.get("refined_inventory")
    if refined:
        current["content_state"] = refined["outcome"]
        current["components"] = refined["components"]
        current["remaining_book_work"] = remaining_texts(refined["remaining_book_work"])
        current["evidence"] = refined["reading_evidence"]
        current["evidence_sources"].append(refined["source"])
        full = refined["complete_assessment"]
        if row["register"] == "apparatus":
            current["proof_or_validation_state"] = "All source-surface components inspected; full current admission remains pending."
            current["validation"] = full["validation"]
        else:
            component_proofs = sorted({c["proof_state"] for c in refined["components"] if c.get("proof_state")})
            current["proof_or_validation_state"] = full.get("proof_state") or full.get("proof_classification") or "; ".join(component_proofs) or "Recorded repair components inspected; independent whole-proof/output acceptance is separate."
            current["validation"] = full.get("known_independent_review_status", full.get("production_evidence", []))
    full_read = row.get("full_text_inventory")
    if full_read:
        current["evidence_sources"].append(full_read["source"])
        current["complete_text_reading"] = {k: full_read[k] for k in ("manuscript", "line_count", "sha256", "all_manuscript_lines_read", "sequential_interval_coverage_matches")}
        if full_read.get("content_state"):
            current["content_state"] = full_read["content_state"]
        if full_read.get("proof_state"):
            current["proof_or_validation_state"] = full_read["proof_state"]
        remaining = remaining_texts(full_read["remaining_completion_obligations"])
        if remaining:
            current["remaining_book_work"] = remaining
    topic = row.get("current_topic_components")
    if topic:
        current["topic_components"] = topic["records"]
        if len(topic["records"]) == 1:
            record = topic["records"][0]
            current["content_state"] = record.get("content_state", current["content_state"])
            current["proof_or_validation_state"] = record.get("proof_state", current["proof_or_validation_state"])
            if record.get("concrete_remaining"):
                current["remaining_book_work"] = remaining_texts(record["concrete_remaining"])
    for finding in new_findings:
        if row["id"] in finding["affected_requirement_ids"]:
            current["known_findings"].append(finding)
            current["remaining_book_work"].insert(0, finding["remaining_book_work"])
            if finding["kind"] == "confirmed_mathematical_defect":
                current["content_state"] = "substantive_present_with_confirmed_mathematical_defect"
    current["remaining_book_work"] = list(dict.fromkeys(current["remaining_book_work"]))
    current["evidence_sources"] = list(dict.fromkeys(s for s in current["evidence_sources"] if s))
    row["current_assessment"] = current
    row["current_remaining"] = " ".join(current["remaining_book_work"])
    # Historical classifications are retained only under their explicitly named block.
    for key in initial:
        row.pop(key, None)

# Reconcile the original requirements directly with the current registers.
live_originals = []
for register in ("new-content", "depth-gaps", "defects", "apparatus"):
    with (ROOT / "spec/registers" / (register + ".csv")).open(encoding="utf-8-sig", newline="") as handle:
        live_originals.extend({"register": register, **item} for item in csv.DictReader(handle))
original_map = {(item["register"], item["id"]): item for item in live_originals}
if len(original_map) != 615 or len(rows) != 615 or len(lookup) != 615:
    issues.append({"kind": "original_requirement_count_mismatch"})
for row in rows:
    if original_map.get((row["register"], row["id"])) != row["original_register_row"]:
        issues.append({"owner": row["id"], "kind": "live_original_register_mismatch"})

# A fresh path enumeration detects added and removed protected files as well as edits.
before = load("manuscript-snapshot-before.json")
suffixes = {".tex", ".sty", ".bib", ".csv", ".md", ".pdf", ".png", ".jpg", ".jpeg", ".svg", ".eps", ".ps"}
protected = {p for p in (ROOT / "handbook").rglob("*") if p.is_file() and p.suffix.lower() in suffixes}
protected |= {p for p in (ROOT / "spec/registers").rglob("*") if p.is_file() and p.suffix.lower() in {".csv", ".md"}}
protected |= {ROOT / p for p in ("source/formal-logic-reference.tex", "source/formal-logic-reference.pdf",
                               "spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md", "spec/INHERITED-CORPUS-MANIFEST.md")
              if (ROOT / p).is_file()}
after_rows = []
for path in sorted(protected, key=lambda p: p.relative_to(ROOT).as_posix()):
    with path.open("rb") as handle:
        digest = hashlib.file_digest(handle, "sha256").hexdigest()
    after_rows.append({"path": path.relative_to(ROOT).as_posix(), "bytes": path.stat().st_size, "sha256": digest})
after_hash = hashlib.sha256("".join(f'{r["path"]}\t{r["sha256"]}\n' for r in after_rows).encode()).hexdigest()
save("manuscript-snapshot-after.json", {"captured_utc": datetime.now(timezone.utc).isoformat(), "aggregate_sha256": after_hash, "files": after_rows})
bmap, amap = ({r["path"]: r for r in items} for items in (before["files"], after_rows))
comparison = {"before_sha256": before["aggregate_sha256"], "after_sha256": after_hash,
              "before_files": len(bmap), "after_files": len(amap),
              "added": sorted(set(amap) - set(bmap)), "removed": sorted(set(bmap) - set(amap)),
              "changed": [p for p in sorted(set(bmap) & set(amap)) if bmap[p]["sha256"] != amap[p]["sha256"]]}
comparison["unchanged"] = not any(comparison[k] for k in ("added", "removed", "changed"))
save("snapshot-comparison.json", comparison)
if not comparison["unchanged"]:
    issues.append({"kind": "protected_snapshot_changed", "comparison": comparison})

sources = load("bibliography-source-reconciliation.json")
source_rows = {r["key"]: r for r in sources["rows"]}
key_rows = {r["key"]: r for r in load("bibliography-current-keys.json")}
if len(source_rows) != 630 or set(source_rows) != set(key_rows) or sources["remaining_keys"] or sources["remaining_targeted_identity_checks"]:
    issues.append({"kind": "source_inventory_coverage_mismatch"})
for key, item in source_rows.items():
    if not item["inventory_complete"] or item["target"]["fields"] != key_rows[key]["fields"]:
        issues.append({"owner": key, "kind": "source_inventory_fields_or_completion_mismatch"})
with (ROOT / sources["current_bibliography"]["path"]).open("rb") as handle:
    if hashlib.file_digest(handle, "sha256").hexdigest() != sources["current_bibliography"]["sha256"]:
        issues.append({"kind": "current_bibliography_changed"})
if len(unique_full_read) != 36 or sum(r["line_count"] for r in unique_full_read.values()) != 33808:
    issues.append({"kind": "full_p9_reading_count_mismatch"})
if sum("refined_inventory" in r for r in rows) != 293:
    issues.append({"kind": "refinement_count_mismatch"})
for identity, finding_id in (("N-c-010", "INV-ELPP-001"), ("N-x-015", "INV-CSL-001")):
    if finding_id not in {f["id"] for f in lookup[identity]["current_assessment"]["known_findings"]}:
        issues.append({"owner": identity, "kind": "confirmed_finding_missing_from_current_view"})

finalize = "--finalize" in sys.argv
audit = load("inventory-completion-audit.json")
audit_ready = audit.get("ready_for_completion", audit["decision"].get("public_completion_claim_ready", False))
final_ready = not issues and audit_ready and not audit.get("remaining_conditions", [])
if finalize and not final_ready:
    raise SystemExit("Finalization conditions remain unresolved; current completion must not be claimed.")

summary = {"created_utc": datetime.now(timezone.utc).isoformat(), "original_rows": len(rows), "unique_ids": len(lookup),
           "refinement_counts": refinement_counts, "refined_rows": sum("refined_inventory" in r for r in rows),
           "refinement_outcomes": dict(collections.Counter(r["refined_inventory"]["outcome"] for r in rows if "refined_inventory" in r)),
           "full_text_inventories": full_read_files, "evidence_records_checked": len(evidence_checks),
           "unique_evidence_files_hashed": len(hash_cache), "evidence_problems": issues,
           "protected_snapshot": comparison, "source_keys_reconciled": len(source_rows),
           "whole_inventory_complete": bool(finalize and final_ready),
           "reason_not_complete": None if finalize and final_ready else "Evidence coverage is complete. Final public report and independent closure reconciliation are pending.",
           "completion_scope": "Current-state inventory of all fourteen parts, original requirements, inherited content, apparatus, full active P9 text, source holdings and review/publication standing. The manuscript itself remains unfinished."}
save("refinement-evidence-reconciliation.json", {"summary": summary, "evidence": evidence_checks})
ledger = {"schema_version": 2, "scope": "All 615 original rows; current_assessment is authoritative for the inventory. initial_assessment preserves the superseded first census, not unresolved current work.", "summary": summary, "requirements": rows}
save("refined-requirement-ledger.json", ledger)
save("complete-requirement-ledger.json", ledger)
with (OUT / "refined-requirement-ledger.csv").open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["register", "id", "part", "item", "current_content_state", "current_proof_or_validation_state", "current_remaining", "known_finding_ids", "evidence_sources", "full_text_inventory"])
    writer.writeheader()
    for row in rows:
        refined = row.get("refined_inventory", {})
        current = row["current_assessment"]
        writer.writerow({"register": row["register"], "id": row["id"], "part": row["part"], "item": row["item"],
                         "current_content_state": current["content_state"], "current_proof_or_validation_state": current["proof_or_validation_state"],
                         "current_remaining": row["current_remaining"], "known_finding_ids": "; ".join(f["id"] for f in current["known_findings"]),
                         "evidence_sources": "; ".join(current["evidence_sources"]),
                         "full_text_inventory": row.get("full_text_inventory", {}).get("source", "")})
(OUT / "complete-requirement-ledger.csv").write_bytes((OUT / "refined-requirement-ledger.csv").read_bytes())
md = ["# Current manuscript requirement inventory", "", "All 615 original rows are retained exactly once. This is the effective current view. The initial classifications are archived in initial-requirement-ledger.json and each current JSON row's initial_assessment block. Source/proof/readiness states are not interchangeable, and current book work below is not claimed completed.", ""]
def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ").replace("\r", " ")
for register in ("new-content", "depth-gaps", "defects", "apparatus"):
    group = [r for r in rows if r["register"] == register]
    md += [f"## {register} ({len(group)} rows)", "", "| ID / part | Original requirement | Current content and proof/validation standing | Current remaining book work | Current evidence |", "| --- | --- | --- | --- | --- |"]
    for row in group:
        current = row["current_assessment"]
        sources = "; ".join(f"[{name}](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/{name})" for name in current["evidence_sources"])
        md.append("| " + " | ".join([cell(row["id"]+" / "+row["part"]), cell(row["item"]), cell(current["content_state"]+"; "+current["proof_or_validation_state"]), cell(row["current_remaining"]), sources]) + " |")
    md.append("")
(OUT / "complete-requirement-ledger.md").write_text("\n".join(md)+"\n", encoding="utf-8")
print(json.dumps({k: v for k, v in summary.items() if k != "full_text_inventories"}, ensure_ascii=False, indent=2))
if issues:
    raise SystemExit("Refinement evidence needs reconciliation; do not claim verified integration.")
