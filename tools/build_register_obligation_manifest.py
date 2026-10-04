#!/usr/bin/env python3
"""Build the lossless open-obligation manifest from the four source registers.

The source registers have different schemas.  Each original record is therefore
stored as a JSON object whose keys retain source-column order and whose string
values are copied without normalization.  ``record_sha256`` hashes the exact
UTF-8 bytes of the source CSV record, including its stored line ending.

This program assigns no completion status, interprets no marker, and merges no
records. Every row receives the neutral disposition ``open``. The source
register's exact preserved record, rather than this projection, records any old
scope, pointer, sketch, ceiling, retirement, exclusion, or completion wording
and determines what kind of fulfillment is owed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV = REPO_ROOT / "spec" / "register-obligation-manifest.csv"
DEFAULT_MARKDOWN = REPO_ROOT / "spec" / "register-obligation-manifest.md"

# Counts and headers are frozen intake assertions.  A register change therefore
# requires an explicit generator review instead of silently changing the floor.
REGISTER_SPECS = (
    (
        "spec/registers/depth-gaps.csv",
        141,
        (
            "id",
            "source_part",
            "item",
            "target_home",
            "treatment",
            "priority",
            "effort",
            "depends",
            "notes",
        ),
    ),
    (
        "spec/registers/new-content.csv",
        185,
        (
            "id",
            "domain",
            "target_part",
            "chapter",
            "item",
            "treatment",
            "priority",
            "effort",
            "sources",
            "notes",
        ),
    ),
    (
        "spec/registers/apparatus.csv",
        201,
        (
            "id",
            "category",
            "item",
            "spec",
            "priority",
            "effort",
            "phase",
            "status",
        ),
    ),
    (
        "spec/registers/defects.csv",
        88,
        (
            "id",
            "class",
            "priority",
            "v1_lines",
            "part_ch",
            "finding",
            "required_fix",
            "acceptance",
            "effort",
            "disposition",
            "phase",
            "status",
        ),
    ),
)
FROZEN_REGISTER_SHA256 = {
    "spec/registers/depth-gaps.csv": "ae52ee64c552bed923f267ddfa1402c4dc871c008ff102faaa659e484d9c1532",
    "spec/registers/new-content.csv": "3b105c1f9d3356c26f649157469802b0e3873881c6415e6b9030ad6d8c5d94e9",
    "spec/registers/apparatus.csv": "70700bdf332a18a2e460c5b2a7b16e4f9183379efe97b65ea488e8349a9ae407",
    "spec/registers/defects.csv": "7bdfb09005dd4035672f6267fa6cd74ec8a505aa3abb7a734ee1b0592fc939b0",
}

OUTPUT_FIELDS = (
    "obligation_id",
    "source_register",
    "source_line",
    "record_sha256",
    "binding_disposition",
    "original_record_json",
)

@dataclass(frozen=True)
class SourceRecord:
    source_register: str
    source_line: int
    row_id: str
    values: dict[str, str]
    original_record_json: str
    record_sha256: str
    binding_disposition: str

    @property
    def obligation_id(self) -> str:
        register_name = Path(self.source_register).stem
        return f"OBL::{register_name}::{self.row_id}"


def fail(message: str) -> None:
    raise ValueError(message)


def disposition_for(values: dict[str, str]) -> str:
    """Return the sole neutral binding disposition without interpreting fields."""

    del values
    return "open"


def read_register(
    relative_path: str, expected_count: int, expected_header: tuple[str, ...]
) -> list[SourceRecord]:
    path = REPO_ROOT / relative_path
    raw = path.read_bytes()
    actual_source_hash = hashlib.sha256(raw).hexdigest()
    expected_source_hash = FROZEN_REGISTER_SHA256[relative_path]
    if actual_source_hash != expected_source_hash:
        fail(
            f"{relative_path}: frozen register drifted "
            f"({actual_source_hash}, expected {expected_source_hash})"
        )
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        fail(f"{relative_path}: source register is not UTF-8: {error}")

    raw_lines = raw.splitlines(keepends=True)
    reader = csv.reader(io.StringIO(text, newline=""), strict=True)
    try:
        header = next(reader)
    except StopIteration:
        fail(f"{relative_path}: empty source register")

    if tuple(header) != expected_header:
        fail(
            f"{relative_path}: header {tuple(header)!r}, expected {expected_header!r}"
        )
    if len(set(header)) != len(header):
        fail(f"{relative_path}: duplicate source column")

    previous_end = reader.line_num
    records: list[SourceRecord] = []
    ids: set[str] = set()

    for cells in reader:
        source_line = previous_end + 1
        source_end = reader.line_num
        if not cells:
            fail(f"{relative_path}:{source_line}: blank CSV record")
        if len(cells) != len(header):
            fail(
                f"{relative_path}:{source_line}: {len(cells)} cells, "
                f"expected {len(header)}"
            )

        values = dict(zip(header, cells, strict=True))
        row_id = values["id"]
        if not row_id:
            fail(f"{relative_path}:{source_line}: empty row ID")
        if row_id in ids:
            fail(f"{relative_path}:{source_line}: duplicate row ID {row_id!r}")
        ids.add(row_id)

        # csv.reader.line_num is the last physical line consumed.  Slicing the
        # original bytes preserves quoted multiline records and stored EOLs.
        row_bytes = b"".join(raw_lines[source_line - 1 : source_end])
        if not row_bytes:
            fail(f"{relative_path}:{source_line}: unable to recover source bytes")

        record_json = json.dumps(
            values,
            ensure_ascii=False,
            separators=(",", ":"),
        )
        # Round-trip every key and value before admitting the record.
        decoded = json.loads(record_json)
        if list(decoded.keys()) != header or decoded != values:
            fail(f"{relative_path}:{source_line}: JSON round trip lost source data")

        records.append(
            SourceRecord(
                source_register=relative_path,
                source_line=source_line,
                row_id=row_id,
                values=values,
                original_record_json=record_json,
                record_sha256=hashlib.sha256(row_bytes).hexdigest(),
                binding_disposition=disposition_for(values),
            )
        )
        previous_end = source_end

    if len(records) != expected_count:
        fail(
            f"{relative_path}: {len(records)} records, expected immutable count "
            f"{expected_count}"
        )
    if previous_end != len(raw_lines):
        fail(
            f"{relative_path}: unparsed physical lines after line {previous_end} "
            f"of {len(raw_lines)}"
        )
    return records


def collect_records() -> list[SourceRecord]:
    records: list[SourceRecord] = []
    global_ids: dict[str, str] = {}
    obligation_ids: set[str] = set()

    for relative_path, expected_count, expected_header in REGISTER_SPECS:
        register_records = read_register(
            relative_path, expected_count, expected_header
        )
        for record in register_records:
            if record.row_id in global_ids:
                fail(
                    f"row ID {record.row_id!r} occurs in both "
                    f"{global_ids[record.row_id]} and {record.source_register}"
                )
            global_ids[record.row_id] = record.source_register
            if record.obligation_id in obligation_ids:
                fail(f"duplicate obligation ID {record.obligation_id!r}")
            obligation_ids.add(record.obligation_id)
        records.extend(register_records)

    expected_total = sum(spec[1] for spec in REGISTER_SPECS)
    if len(records) != expected_total:
        fail(f"combined manifest has {len(records)} rows, expected {expected_total}")
    return records


def csv_bytes(records: Iterable[SourceRecord]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=OUTPUT_FIELDS,
        lineterminator="\n",
        extrasaction="raise",
    )
    writer.writeheader()
    for record in records:
        writer.writerow(
            {
                "obligation_id": record.obligation_id,
                "source_register": record.source_register,
                "source_line": record.source_line,
                "record_sha256": record.record_sha256,
                "binding_disposition": record.binding_disposition,
                "original_record_json": record.original_record_json,
            }
        )
    return output.getvalue().encode("utf-8")


def status_rows(records: list[SourceRecord]) -> list[tuple[str, str, int]]:
    result: list[tuple[str, str, int]] = []
    for relative_path, _, expected_header in REGISTER_SPECS:
        relevant = [row for row in records if row.source_register == relative_path]
        if "status" not in expected_header:
            result.append((relative_path, "(source column absent)", len(relevant)))
            continue
        counts: Counter[str] = Counter()
        first_seen: list[str] = []
        for row in relevant:
            status = row.values["status"]
            if status not in counts:
                first_seen.append(status)
            counts[status] += 1
        result.extend((relative_path, value, counts[value]) for value in first_seen)
    return result


def markdown_bytes(records: list[SourceRecord]) -> bytes:
    per_register = Counter(row.source_register for row in records)
    dispositions = Counter(row.binding_disposition for row in records)
    total = len(records)

    lines = [
        "# Register obligation manifest",
        "",
        "This file is generated by `tools/build_register_obligation_manifest.py`.",
        "The companion CSV is a lossless administrative projection of every row",
        "in the four frozen registers. It does not rank, merge, close, reinterpret,",
        "or rewrite any obligation.",
        "",
        f"- Total source rows: {total}",
        f"- Unique source row IDs: {len({row.row_id for row in records})}",
        f"- Unique obligation IDs: {len({row.obligation_id for row in records})}",
        "- Completion inferred from old status fields: none",
        "- Generator self-checks: **PASS**",
        "",
        "## Per-register counts",
        "",
        "| Source register | Rows |",
        "|---|---:|",
    ]
    for relative_path, expected_count, _ in REGISTER_SPECS:
        lines.append(f"| `{relative_path}` | {per_register[relative_path]} |")
        if per_register[relative_path] != expected_count:
            fail(f"{relative_path}: Markdown count disagrees with frozen count")

    lines.extend(
        [
            "",
            "## Original status values",
            "",
            "These are copied status values and counts, not current dispositions.",
            "Registers without a `status` column are reported without inventing one.",
            "",
            "| Source register | Original status value | Rows |",
            "|---|---|---:|",
        ]
    )
    for relative_path, status, count in status_rows(records):
        escaped_status = status.replace("|", r"\|")
        lines.append(f"| `{relative_path}` | `{escaped_status}` | {count} |")

    lines.extend(
        [
            "",
            "## Binding dispositions",
            "",
            "Every source row receives the neutral disposition `open`. Legacy",
            "exclusion, pointer, sketch, ceiling, retirement, stub, and old completion",
            "strings remain untouched inside `original_record_json`; the generator does",
            "not interpret or classify them. This projection does not infer whether an",
            "obligation requires a source presentation, apparatus artifact, correction,",
            "or another kind of fulfillment. The mechanical marker test grants no",
            "permission to omit content and makes no completion claim.",
            "",
            "| Binding disposition | Rows |",
            "|---|---:|",
            f"| `open` | {dispositions['open']} |",
            "",
            "## Lossless record schema",
            "",
            "The CSV adds only the five administrative fields authorized by the",
            "full-compendium contract: `obligation_id`, `source_register`,",
            "`source_line`, `record_sha256`, and `binding_disposition`.",
            "`original_record_json` is the data-preservation container: it retains",
            "every original column name, column order, and string value. The digest",
            "is SHA-256 over the exact stored bytes of the original CSV record,",
            "including its line ending. `source_register` is the repository-relative",
            "source path and `source_line` is the first physical line of the record.",
            "",
            "## Verification",
            "",
            "Run:",
            "",
            "```text",
            "python tools/build_register_obligation_manifest.py --check",
            "```",
            "",
            "The check re-reads all four source registers, enforces their frozen",
            "headers and row counts, rejects duplicate or empty IDs, round-trips every",
            "original JSON record, recomputes every exact row digest and disposition,",
            "and byte-compares both generated artifacts.",
            "",
        ]
    )
    return "\n".join(lines).encode("utf-8")


def compare_generated(path: Path, expected: bytes) -> list[str]:
    if not path.is_file():
        return [f"missing generated artifact: {path.relative_to(REPO_ROOT).as_posix()}"]
    actual = path.read_bytes()
    if actual != expected:
        return [
            f"generated artifact is stale: {path.relative_to(REPO_ROOT).as_posix()}"
        ]
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify generated artifacts without writing them",
    )
    args = parser.parse_args()

    try:
        records = collect_records()
        csv_output = csv_bytes(records)
        markdown_output = markdown_bytes(records)
    except (OSError, UnicodeError, ValueError, csv.Error) as error:
        print("register obligation manifest: FAIL")
        print(f"  {error}")
        return 1

    if args.check:
        failures = []
        failures.extend(compare_generated(DEFAULT_CSV, csv_output))
        failures.extend(compare_generated(DEFAULT_MARKDOWN, markdown_output))
        if failures:
            print("register obligation manifest: FAIL")
            for failure in failures:
                print(f"  {failure}")
            return 1
        print("register obligation manifest: PASS")
        print(f"  rows: {len(records)}")
        print(f"  unique source IDs: {len({row.row_id for row in records})}")
        print("  completion inferred: none")
        return 0

    DEFAULT_CSV.write_bytes(csv_output)
    DEFAULT_MARKDOWN.write_bytes(markdown_output)
    print("register obligation manifest: WROTE")
    print(f"  {DEFAULT_CSV.relative_to(REPO_ROOT).as_posix()}")
    print(f"  {DEFAULT_MARKDOWN.relative_to(REPO_ROOT).as_posix()}")
    print(f"  rows: {len(records)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
