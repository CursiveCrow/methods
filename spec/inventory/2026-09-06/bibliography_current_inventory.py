"""Enumerate every current bibliography key and its available local evidence."""
from __future__ import annotations

import collections
import csv
import hashlib
import json
from pathlib import Path
import re

ROOT = Path("C:/Dev/the-methods-of-reason")
OUT = ROOT / "spec/inventory/2026-09-06"


def csv_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def table(name, rows):
    fields = list(dict.fromkeys(k for row in rows for k in row))
    with (OUT / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in row.items()})


def braced(text, start):
    if text[start] != "{":
        raise ValueError("Expected opening brace")
    depth, i = 1, start + 1
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if not depth:
                return text[start + 1:i], i + 1
        i += 1
    raise ValueError("Unterminated brace group")


def parse_fields(body):
    result, issues, index = {}, [], 0
    while index < len(body):
        skip = re.match(r"(?:\s|,|%[^\n]*(?:\n|$))*", body[index:])
        index += skip.end()
        if index >= len(body):
            break
        match = re.match(r"([A-Za-z][A-Za-z0-9_-]*)\s*=\s*", body[index:])
        if not match:
            issues.append(body[index:index + 120])
            break
        name = match.group(1).lower()
        index += match.end()
        if body[index] == "{":
            value, index = braced(body, index)
        elif body[index] == '"':
            start = index + 1
            index += 1
            while index < len(body) and (body[index] != '"' or body[index - 1] == "\\"):
                index += 1
            value = body[start:index]
            index += 1
        else:
            end = body.find(",", index)
            end = len(body) if end < 0 else end
            value, index = body[index:end].strip(), end
        result[name] = value
    return result, issues


bib_path = ROOT / "handbook/bib/handbook.bib"
bib_raw = bib_path.read_bytes()
bib = bib_raw.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
entries, parse_issues = [], []
for match in re.finditer(r"(?m)^\s*@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", bib):
    brace = bib.index("{", match.start())
    content, end = braced(bib, brace)
    fields, issues = parse_fields(content[content.index(",") + 1:])
    entry_start = bib.index("@", match.start(), match.end())
    entry_end = end + (1 if end < len(bib) and bib[end] == "\n" else 0)
    literal = bib[entry_start:entry_end]
    entries.append({"key": match.group(2), "type": match.group(1).lower(),
                    "line_start": bib.count("\n", 0, entry_start)+1,
                    "line_end": bib.count("\n", 0, end)+1,
                    "literal_normalized_sha256": hashlib.sha256(literal.encode()).hexdigest(),
                    "fields": fields})
    if issues:
        parse_issues.append({"key": match.group(2), "issues": issues})
keys = {r["key"] for r in entries}
occurrences = collections.defaultdict(list)
for row in csv_rows(OUT / "citation-occurrences.csv"):
    occurrences[row["key"]].append(row)
inherited = {r["key"]: r for r in csv_rows(ROOT / "spec/provenance/inherited-bibliography-field-ledger.csv")}
physical = csv_rows(OUT / "source-and-pdf-files.csv")
physical_paths = {r["path"] for r in physical}

# Exact key/DOI mentions locate evidence. They do not certify what the note says.
key_pattern = re.compile(r"(?<![A-Za-z0-9_-])(" + "|".join(re.escape(k) for k in sorted(keys, key=len, reverse=True)) + r")(?![A-Za-z0-9_-])")
doi_to_keys = collections.defaultdict(list)
for r in entries:
    if r["fields"].get("doi"):
        doi_to_keys[r["fields"]["doi"].lower()].append(r["key"])
doi_pattern = re.compile("|".join(re.escape(d) for d in sorted(doi_to_keys, key=len, reverse=True)), re.I)
note_mentions, note_inventory = collections.defaultdict(list), []
note_files = sorted((ROOT / "spec/research").glob("*.md"))
note_files += sorted((ROOT / "spec/provenance").glob("*.md"))
for path in note_files:
    size = path.stat().st_size
    if path.name == "full-compendium-coverage-baseline.md":
        note_inventory.append({"path": path.relative_to(ROOT).as_posix(), "bytes": size, "scope": "metadata_only_legacy_catalog"})
        continue
    with path.open("rb") as handle:
        raw = handle.read() if size <= 10_000_000 else handle.read(131_072)
    text = raw.decode("utf-8-sig", errors="replace")
    if len(raw) < size:
        text = text.rsplit("\n", 1)[0] + "\n"
    lines = text.splitlines()
    rel = path.relative_to(ROOT).as_posix()
    refs = sorted({p for p in physical_paths if p in text})
    note_inventory.append({"path": rel, "bytes": size, "scope": "full_text_parsed_not_semantically_read" if len(raw) == size else "first_128KiB_only",
                           "parsed_lines": len(lines), "parsed_bytes_sha256": hashlib.sha256(raw).hexdigest(), "physical_source_paths_mentioned": refs})
    mention_keys = collections.defaultdict(list)
    for number, line in enumerate(lines, 1):
        found = {m.group(1) for m in key_pattern.finditer(line)}
        for match in doi_pattern.finditer(line):
            found.update(doi_to_keys[match.group(0).lower()])
        for key in found:
            if len(mention_keys[key]) < 8:
                mention_keys[key].append({"line": number, "excerpt": line[:700]})
    for key, positions in mention_keys.items():
        note_mentions[key].append({"path": rel, "mention_evidence": positions,
                                   "physical_source_paths_mentioned_elsewhere_in_same_note": refs,
                                   "standing": "Evidence-location candidate; source identity, reading and acceptance require inspecting the actual passage."})

rows, inherited_comparison = [], []
for entry in entries:
    key, fields = entry["key"], entry["fields"]
    history = inherited.get(key)
    field_match = fields == json.loads(history["bib_fields_json"]) if history else None
    if history:
        evidence_path = ROOT / history["semantic_review_evidence"]
        inherited_comparison.append({"key": key, "original_source_lines": [int(history["source_start_line"]), int(history["source_end_line"])],
                                     "current_bibliography_lines": [entry["line_start"], entry["line_end"]],
                                     "current_fields_equal_recorded_fields": field_match,
                                     "current_entry_hash_equals_recorded_hash": entry["literal_normalized_sha256"] == history["bib_sha256"],
                                     "historical_semantic_review": history["semantic_field_review"],
                                     "review_path": history["semantic_review_evidence"],
                                     "review_file_exists": evidence_path.is_file(),
                                     "review_hash_matches": hashlib.sha256(evidence_path.read_bytes()).hexdigest() == history["semantic_review_sha256"] if evidence_path.is_file() else False})
    # Names locate candidates only. Deliberately do not infer an exact edition.
    compact_key = re.sub(r"[^a-z0-9]", "", key.lower())
    named_files = [r["path"] for r in physical if len(compact_key) >= 8 and compact_key in re.sub(r"[^a-z0-9]", "", r["path"].lower())]
    row = {**entry, "title": fields.get("title", ""), "author_or_editor": fields.get("author", fields.get("editor", "")),
           "year_or_date": fields.get("year", fields.get("date", "")), "edition": fields.get("edition", ""),
           "doi": fields.get("doi", ""), "url": fields.get("url", ""),
           "active_citation_count": len(occurrences[key]), "active_citation_locations": occurrences[key],
           "inherited_bibliography_key": history is not None,
           "inherited_record_fields_match": field_match,
           "exact_key_or_doi_note_candidates": note_mentions[key], "filename_candidates": named_files,
           "holding_identity_assessment": "Pending passage-level identification; candidate locations are not accepted holdings." if note_mentions[key] or named_files else
                                          "No exact-key/DOI or filename holding evidence in inspected indexes; broader source-title and holding identification still required.",
           "inventory_complete": False}
    rows.append(row)
summary = {"bibliography_sha256": hashlib.sha256(bib_raw).hexdigest(), "entry_count": len(rows), "unique_keys": len(keys),
           "parse_issues": parse_issues, "duplicate_keys": [k for k,n in collections.Counter(r["key"] for r in rows).items() if n > 1],
           "cited_keys": sum(bool(r["active_citation_count"]) for r in rows),
           "keys_with_note_candidates": sum(bool(r["exact_key_or_doi_note_candidates"]) for r in rows),
           "keys_with_filename_candidates": sum(bool(r["filename_candidates"]) for r in rows),
           "keys_without_either_candidate": [r["key"] for r in rows if not r["exact_key_or_doi_note_candidates"] and not r["filename_candidates"]],
           "inherited_key_count": len(inherited_comparison),
           "inherited_field_comparisons": dict(collections.Counter(str(r["current_fields_equal_recorded_fields"]) for r in inherited_comparison)),
           "inherited_entry_hash_comparisons": dict(collections.Counter(str(r["current_entry_hash_equals_recorded_hash"]) for r in inherited_comparison)),
           "inherited_review_hash_comparisons": dict(collections.Counter(str(r["review_hash_matches"]) for r in inherited_comparison)),
           "notes_parsed": len(note_inventory), "notes_with_limited_scope": [r for r in note_inventory if r["scope"] != "full_text_parsed_not_semantically_read"],
           "completion_state": "Enumeration and candidate evidence discovery complete; exact holding/reading/review classifications still need passage-level investigation."}
dump("bibliography-current-keys.json", rows)
table("bibliography-current-keys.csv", [{k:v for k,v in r.items() if k not in {"fields", "active_citation_locations", "exact_key_or_doi_note_candidates"}} for r in rows])
dump("bibliography-current-summary.json", summary)
dump("bibliography-evidence-notes-index.json", note_inventory)
dump("inherited-bibliography-current-comparison.json", inherited_comparison)
print(json.dumps({k:v for k,v in summary.items() if k != "notes_with_limited_scope"}, ensure_ascii=False, indent=2))
