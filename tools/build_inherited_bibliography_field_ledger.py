#!/usr/bin/env python3
"""Build the one-to-one ledger for the 64 inherited bibliography records.

Necessity: the final book uses one BibLaTeX bibliography, so the exact manual
``thebibliography`` cannot also be printed without duplication.
Definition: the inherited bibliography field ledger is the ordered 64-row map
from each exact ``\\bibitem`` block to its converted BibLaTeX entry, including
both hashes, every parsed field, and lexical/identifier preservation results.
Standing: it is administrative source-fidelity evidence, not a bibliography,
mathematical statement, source admission, or independent review verdict.
Nonredundancy: the source artifact proves the old bytes and ``handbook.bib``
proves the new bytes, but neither alone proves one-to-one key order or retained
publication facts after the layout-only conversion.
Use: the final unified bibliography and provenance record SRC-16803-17196 cite
this ledger; ``--check`` rejects key, order, locator, year, or substantive-token
drift before the final book build.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "formal-logic-reference.tex"
BIB = ROOT / "handbook" / "bib" / "handbook.bib"
CSV_OUT = ROOT / "spec" / "provenance" / "inherited-bibliography-field-ledger.csv"
MD_OUT = ROOT / "spec" / "provenance" / "inherited-bibliography-field-ledger.md"
SEMANTIC_REVIEW = (
    ROOT
    / "board-manuscript-completion-2026-08-18"
    / "transcript"
    / "r3-source-fidelity.md"
)
AUTHORITY_SHA256 = "0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc"
SOURCE_START = 16803
SOURCE_END = 17196
EXPECTED_KEYS = 64

FIELDS = [
    "ordinal",
    "key",
    "source_start_line",
    "source_end_line",
    "source_sha256",
    "bib_type",
    "bib_start_line",
    "bib_end_line",
    "bib_sha256",
    "source_literal_json",
    "bib_fields_json",
    "source_years_json",
    "bib_years_json",
    "source_locators_json",
    "bib_locators_json",
    "missing_substantive_tokens_json",
    "static_field_status",
    "semantic_field_review",
    "semantic_review_evidence",
    "semantic_review_sha256",
]

STOPWORDS = {
    "a",
    "an",
    "and",
    "at",
    "by",
    "current",
    "doi",
    "edition",
    "edited",
    "editor",
    "editors",
    "first",
    "in",
    "of",
    "on",
    "online",
    "pages",
    "part",
    "record",
    "retrieved",
    "series",
    "the",
    "translated",
    "version",
    "volume",
    "august",
}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def normalized_lines(raw: bytes) -> list[str]:
    text = raw.decode("utf-8")
    return re.split(r"\r\n|\n|\r", text)


def parse_source_records(lines: list[str]) -> list[dict[str, object]]:
    starts: list[tuple[str, int]] = []
    for line_number in range(SOURCE_START, SOURCE_END + 1):
        match = re.fullmatch(r"\\bibitem\{([^}]+)\}", lines[line_number - 1])
        if match:
            starts.append((match.group(1), line_number))
    if len(starts) != EXPECTED_KEYS:
        raise ValueError(f"expected {EXPECTED_KEYS} source bibitems, found {len(starts)}")
    records: list[dict[str, object]] = []
    for index, (key, start) in enumerate(starts):
        end = starts[index + 1][1] - 1 if index + 1 < len(starts) else 17195
        literal = "\n".join(lines[start - 1 : end]) + "\n"
        records.append(
            {
                "key": key,
                "start": start,
                "end": end,
                "literal": literal,
                "sha256": sha(literal.encode("utf-8")),
            }
        )
    return records


def parse_bib_records(raw: bytes) -> list[dict[str, object]]:
    text = raw.decode("utf-8")
    section_end = text.index("% ===== (2) Five primary sources =====")
    section = text[:section_end]
    entry_re = re.compile(r"(?ms)^@([A-Za-z]+)\{([^,]+),\n(.*?)^\}\n")
    field_re = re.compile(r"(?m)^\s{2}([A-Za-z][A-Za-z0-9_]*)\s*=\s*\{(.*)\},\s*$")
    records: list[dict[str, object]] = []
    for match in entry_re.finditer(section):
        literal = match.group(0)
        start = section.count("\n", 0, match.start()) + 1
        end = start + literal.count("\n") - 1
        fields = {name: value for name, value in field_re.findall(match.group(3))}
        records.append(
            {
                "key": match.group(2),
                "kind": match.group(1).lower(),
                "start": start,
                "end": end,
                "literal": literal,
                "sha256": sha(literal.encode("utf-8")),
                "fields": fields,
            }
        )
    if len(records) != EXPECTED_KEYS:
        raise ValueError(f"expected {EXPECTED_KEYS} converted entries, found {len(records)}")
    return records


def strip_locators(text: str) -> str:
    text = re.sub(r"\\href\{[^}]*\}\{[^}]*\}", " ", text)
    return re.sub(r"\\url\{[^}]*\}", " ", text)


def plain_tokens(text: str) -> set[str]:
    text = strip_locators(text)
    text = re.sub(r"\\bibitem\{[^}]+\}", " ", text)
    text = re.sub(r"\\(?:emph|texttt|allowbreak)\b", " ", text)
    text = text.replace(r"\LaTeX", "latex")
    text = re.sub(r"\\ss\s*", "ss", text)
    text = text.replace(r"\L{}", "l").replace(r"\L", "l").replace(r"\&", " and ")
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\\[\"'`^~=.Hckbduvr]\s*\{?([A-Za-z])\}?", r"\1", text)
    text = re.sub(r"(?i)\b([0-9]+)(?:st|nd|rd|th)\b", r"\1", text)
    text = text.replace("\\_", "_")
    text = re.sub(r"[\\]", " ", text)
    tokens = set(re.findall(r"[a-z0-9]+", text.lower()))
    normalized: set[str] = set()
    for token in tokens:
        if token in STOPWORDS or (len(token) == 1 and token.isalpha()):
            continue
        if len(token) >= 8 and re.fullmatch(r"[0-9a-f]+", token):
            continue
        normalized.add(str(int(token)) if token.isdigit() else token)
    return normalized


def source_locators(text: str) -> list[str]:
    values = re.findall(r"\\url\{([^}]+)\}", text)
    values += [url for url, _label in re.findall(r"\\href\{([^}]+)\}\{([^}]*)\}", text)]
    return sorted(value.replace(r"\_", "_") for value in values)


def bib_locators(fields: dict[str, str]) -> list[str]:
    values: list[str] = []
    if "doi" in fields:
        values.append("https://doi.org/" + fields["doi"].replace(r"\_", "_"))
    if "url" in fields:
        values.append(fields["url"].replace(r"\_", "_"))
    return sorted(values)


def year_tokens(text: str) -> list[str]:
    text = re.sub(r"\\bibitem\{[^}]+\}", " ", strip_locators(text))
    return sorted(set(re.findall(r"(?<![0-9])(?:1[0-9]{3}|20[0-9]{2})(?![0-9])", text)))


def semantic_reviews(expected_keys: list[str]) -> tuple[dict[str, str], str]:
    raw = SEMANTIC_REVIEW.read_bytes()
    decisions = re.findall(r"(?m)^BIBSEM (\S+) (pass|fail)$", raw.decode("utf-8"))
    keys = [key for key, _status in decisions]
    if keys != expected_keys or len(set(keys)) != EXPECTED_KEYS:
        raise ValueError("semantic bibliography decisions do not match the inherited key order")
    return dict(decisions), sha(raw)


def build_rows() -> list[dict[str, object]]:
    source_raw = SOURCE.read_bytes()
    if sha(source_raw) != AUTHORITY_SHA256:
        raise ValueError("frozen source authority hash changed")
    source_records = parse_source_records(normalized_lines(source_raw))
    bib_records = parse_bib_records(BIB.read_bytes())
    if [record["key"] for record in source_records] != [record["key"] for record in bib_records]:
        raise ValueError("converted bibliography keys or source order changed")
    decisions, review_sha256 = semantic_reviews(
        [str(record["key"]) for record in source_records]
    )
    rows: list[dict[str, object]] = []
    for ordinal, (source, bib) in enumerate(zip(source_records, bib_records, strict=True), 1):
        source_text = str(source["literal"])
        fields = dict(bib["fields"])
        field_text = " ".join(
            value for name, value in fields.items() if name not in {"doi", "url"}
        )
        missing = sorted(plain_tokens(source_text) - plain_tokens(field_text))
        src_years = year_tokens(source_text)
        dst_years = year_tokens(field_text)
        src_locators = source_locators(source_text)
        dst_locators = bib_locators(fields)
        status = (
            "pass"
            if not missing and set(src_years).issubset(dst_years) and src_locators == dst_locators
            else "fail"
        )
        rows.append(
            {
                "ordinal": ordinal,
                "key": source["key"],
                "source_start_line": source["start"],
                "source_end_line": source["end"],
                "source_sha256": source["sha256"],
                "bib_type": bib["kind"],
                "bib_start_line": bib["start"],
                "bib_end_line": bib["end"],
                "bib_sha256": bib["sha256"],
                "source_literal_json": json_text(source_text),
                "bib_fields_json": json_text(fields),
                "source_years_json": json_text(src_years),
                "bib_years_json": json_text(dst_years),
                "source_locators_json": json_text(src_locators),
                "bib_locators_json": json_text(dst_locators),
                "missing_substantive_tokens_json": json_text(missing),
                "static_field_status": status,
                "semantic_field_review": decisions[str(source["key"])],
                "semantic_review_evidence": SEMANTIC_REVIEW.relative_to(ROOT).as_posix(),
                "semantic_review_sha256": review_sha256,
            }
        )
    return rows


def render(rows: list[dict[str, object]]) -> tuple[bytes, bytes]:
    csv_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(csv_buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    csv_bytes = csv_buffer.getvalue().encode("utf-8")
    failures = [row for row in rows if row["static_field_status"] != "pass"]
    semantic_failures = [row for row in rows if row["semantic_field_review"] != "pass"]
    md = (
        "# Inherited bibliography field ledger\n\n"
        f"- Source interval: `SRC-16803-17196`\n"
        f"- Ordered inherited records: {len(rows)}\n"
        f"- Static field-preservation passes: {len(rows) - len(failures)}\n"
        f"- Static field-preservation failures: {len(failures)}\n"
        f"- Independent semantic field-review passes: {len(rows) - len(semantic_failures)}\n"
        f"- Independent semantic field-review failures: {len(semantic_failures)}\n"
        f"- Review evidence: `{SEMANTIC_REVIEW.relative_to(ROOT).as_posix()}` "
        f"(SHA-256 `{sha(SEMANTIC_REVIEW.read_bytes())}`)\n\n"
        "The CSV pins each exact manual bibliography block to the corresponding "
        "BibLaTeX entry and checks key order, locators, years, and substantive "
        "lexical facts. It is source-fidelity evidence, not an admission verdict.\n"
    )
    return csv_bytes, md.encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rows = build_rows()
    csv_bytes, md_bytes = render(rows)
    failures = [row for row in rows if row["static_field_status"] != "pass"]
    semantic_failures = [row for row in rows if row["semantic_field_review"] != "pass"]
    if args.write:
        CSV_OUT.write_bytes(csv_bytes)
        MD_OUT.write_bytes(md_bytes)
    else:
        if not CSV_OUT.exists() or CSV_OUT.read_bytes() != csv_bytes:
            raise SystemExit("inherited bibliography CSV is stale")
        if not MD_OUT.exists() or MD_OUT.read_bytes() != md_bytes:
            raise SystemExit("inherited bibliography Markdown is stale")
    if failures or semantic_failures:
        for row in failures:
            print(
                f"FAIL {row['key']}: missing={row['missing_substantive_tokens_json']} "
                f"source_years={row['source_years_json']} bib_years={row['bib_years_json']} "
                f"source_locators={row['source_locators_json']} bib_locators={row['bib_locators_json']}"
            )
        for row in semantic_failures:
            print(f"FAIL {row['key']}: semantic review={row['semantic_field_review']}")
        return 1
    print(f"inherited bibliography field ledger: {len(rows)} static and semantic mappings PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
