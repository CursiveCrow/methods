#!/usr/bin/env python3
"""Verify historical inventory evidence or build the current-tree inventory.

The historical artifacts are immutable anchored records and have no write
mode.  Current inventory candidates require explicit, non-existing paths.
Every inventory row remains open/unmapped; inventory is not content review.
"""

from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path

from check_handbook_construction_snapshot import (
    CONSTRUCTION_INVENTORY_CSV,
    CONSTRUCTION_INVENTORY_MD,
    MANIFEST as CONSTRUCTION_SNAPSHOT,
    MANIFEST_SHA256 as CONSTRUCTION_SNAPSHOT_SHA256,
    verify_current,
)
from handbook_tree_manifest import (
    SHA256_RE,
    anchored_rows,
    digest,
    parse as parse_manifest,
    require_live_equality,
    resolve_candidate_path,
    validate_new_candidate_path,
    write_new_candidate,
)


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
HISTORICAL_SNAPSHOT = ROOT / "spec/handbook-audit-snapshot.csv"
HISTORICAL_CSV = ROOT / "spec/handbook-source-inventory.csv"
HISTORICAL_MD = ROOT / "spec/handbook-source-inventory.md"
HISTORICAL_SNAPSHOT_SHA256 = (
    "63b405b2b9d1384ee32ae963e053d5c971b90dfe34d186fde0d1b2a0b3cec2ba"
)
HISTORICAL_CSV_SHA256 = (
    "d9a03b844bf9123061371f59e99a1b223cd136cbcfbda2d30a49479832f5ac39"
)
HISTORICAL_MD_SHA256 = (
    "eef4c4cff8024233c22bbd605fd17c53c41655022e03a0c35a80422899b2eb90"
)
FIELDS = (
    "record_id",
    "record_type",
    "path",
    "line_number",
    "bytes",
    "sha256",
    "provenance_status",
    "source_authority_ids",
)
FORBIDDEN_CANDIDATE_PATHS = frozenset(
    {
        HISTORICAL_SNAPSHOT,
        HISTORICAL_CSV,
        HISTORICAL_MD,
        CONSTRUCTION_SNAPSHOT,
        CONSTRUCTION_INVENTORY_CSV,
        CONSTRUCTION_INVENTORY_MD,
    }
)


def parse_inventory(raw: bytes) -> list[dict[str, str]]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("handbook source inventory is not UTF-8") from exc
    with io.StringIO(text, newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError("handbook source inventory has an unexpected schema")
        rows = list(reader)
    if not rows:
        raise ValueError("handbook source inventory is empty")
    return rows


def verify_inventory_structure(
    inventory_rows: list[dict[str, str]], snapshot_rows: list[dict[str, str]]
) -> tuple[int, int]:
    """Check the lossless record grammar and file rows against a snapshot."""

    cursor = 0
    line_total = 0
    seen_ids: set[str] = set()
    for file_index, snapshot in enumerate(snapshot_rows, start=1):
        if cursor >= len(inventory_rows):
            raise ValueError(f"inventory lacks file record {file_index}")
        file_row = inventory_rows[cursor]
        expected_file_id = f"HB-F{file_index:04d}"
        if file_row != {
            "record_id": expected_file_id,
            "record_type": "file",
            "path": snapshot["path"],
            "line_number": "",
            "bytes": snapshot["bytes"],
            "sha256": snapshot["sha256"],
            "provenance_status": "open/unmapped",
            "source_authority_ids": "[]",
        }:
            raise ValueError(f"inventory file record differs: {expected_file_id}")
        seen_ids.add(expected_file_id)
        cursor += 1
        expected_line = 1
        while cursor < len(inventory_rows):
            row = inventory_rows[cursor]
            if row["record_type"] == "file":
                break
            expected_line_id = f"{expected_file_id}-L{expected_line:06d}"
            if row["record_id"] != expected_line_id:
                raise ValueError(
                    f"inventory line sequence differs: expected {expected_line_id}"
                )
            if row["record_type"] != "physical_line":
                raise ValueError(f"unexpected inventory record type: {row['record_type']}")
            if row["path"] != snapshot["path"]:
                raise ValueError(f"inventory line path differs: {expected_line_id}")
            if row["line_number"] != str(expected_line):
                raise ValueError(f"inventory line number differs: {expected_line_id}")
            if (
                not row["bytes"].isascii()
                or not row["bytes"].isdecimal()
                or str(int(row["bytes"])) != row["bytes"]
            ):
                raise ValueError(f"invalid inventory byte count: {expected_line_id}")
            if not SHA256_RE.fullmatch(row["sha256"]):
                raise ValueError(f"invalid inventory digest: {expected_line_id}")
            if row["provenance_status"] != "open/unmapped":
                raise ValueError(f"inventory row is not open/unmapped: {expected_line_id}")
            if row["source_authority_ids"] != "[]":
                raise ValueError(f"inventory row has source authority IDs: {expected_line_id}")
            if row["record_id"] in seen_ids:
                raise ValueError(f"duplicate inventory record ID: {row['record_id']}")
            seen_ids.add(row["record_id"])
            cursor += 1
            expected_line += 1
            line_total += 1
    if cursor != len(inventory_rows):
        raise ValueError("inventory has records beyond the snapshot file sequence")
    return len(snapshot_rows), line_total


def verify_historical() -> tuple[int, int]:
    """Verify immutable historical records without consulting current files."""

    snapshot_rows = anchored_rows(
        HISTORICAL_SNAPSHOT, HISTORICAL_SNAPSHOT_SHA256
    )
    if not HISTORICAL_CSV.is_file() or not HISTORICAL_MD.is_file():
        raise ValueError("historical handbook inventory artifact missing")
    csv_raw = HISTORICAL_CSV.read_bytes()
    md_raw = HISTORICAL_MD.read_bytes()
    if digest(csv_raw) != HISTORICAL_CSV_SHA256:
        raise ValueError("historical handbook inventory CSV drifted")
    if digest(md_raw) != HISTORICAL_MD_SHA256:
        raise ValueError("historical handbook inventory Markdown drifted")
    return verify_inventory_structure(parse_inventory(csv_raw), snapshot_rows)


def build(snapshot_rows: list[dict[str, str]], root: Path = ROOT) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for file_index, snapshot in enumerate(snapshot_rows, start=1):
        path = root / snapshot["path"]
        raw = path.read_bytes()
        if str(len(raw)) != snapshot["bytes"] or digest(raw) != snapshot["sha256"]:
            raise ValueError(f"snapshot source drifted: {snapshot['path']}")
        rows.append(
            {
                "record_id": f"HB-F{file_index:04d}",
                "record_type": "file",
                "path": snapshot["path"],
                "line_number": "",
                "bytes": str(len(raw)),
                "sha256": digest(raw),
                "provenance_status": "open/unmapped",
                "source_authority_ids": "[]",
            }
        )
        try:
            raw.decode("utf-8")
            physical_lines = raw.splitlines(keepends=True)
        except UnicodeDecodeError:
            physical_lines = []
        for line_number, line in enumerate(physical_lines, start=1):
            rows.append(
                {
                    "record_id": f"HB-F{file_index:04d}-L{line_number:06d}",
                    "record_type": "physical_line",
                    "path": snapshot["path"],
                    "line_number": str(line_number),
                    "bytes": str(len(line)),
                    "sha256": digest(line),
                    "provenance_status": "open/unmapped",
                    "source_authority_ids": "[]",
                }
            )
    verify_inventory_structure(rows, snapshot_rows)
    return rows


def csv_bytes(rows: list[dict[str, str]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def md_bytes(rows: list[dict[str, str]]) -> bytes:
    files = sum(row["record_type"] == "file" for row in rows)
    lines = sum(row["record_type"] == "physical_line" for row in rows)
    return (
        "\n".join(
            [
                "# Current handbook construction source inventory",
                "",
                "This generated view inventories every file and every physical line of",
                "every UTF-8 text file in the pinned current handbook construction",
                "snapshot. Binary inputs remain covered by their whole-file byte counts",
                "and digests rather than being treated as text lines.",
                "",
                "It is not a semantic-unit inventory and makes no provenance, fidelity,",
                "correctness, completeness, visual-quality, or release claim. Every row",
                "remains `open/unmapped` with no source-authority IDs.",
                "",
                f"- Snapshot source files: {files:,}.",
                f"- Physical source lines: {lines:,}.",
                f"- Total inventory records: {len(rows):,}.",
                "- Reverse provenance status on every row: `open/unmapped`.",
                "- Semantic handbook-unit inventory and keyed provenance join: `OPEN`.",
                "",
                "The CSV is lossless at the file/physical-line level through exact byte",
                "counts and SHA-256 digests. Later semantic-unit records must cover these",
                "rows without using file/line presence as a content-fidelity verdict.",
                "",
            ]
        )
    ).encode("utf-8")


def verify_construction() -> tuple[int, int]:
    snapshot_rows = verify_current(
        CONSTRUCTION_SNAPSHOT,
        CONSTRUCTION_SNAPSHOT_SHA256,
        HANDBOOK,
        ROOT,
    )
    rows = build(snapshot_rows)
    if (
        not CONSTRUCTION_INVENTORY_CSV.is_file()
        or CONSTRUCTION_INVENTORY_CSV.read_bytes() != csv_bytes(rows)
    ):
        raise ValueError("current construction inventory CSV is missing or stale")
    if (
        not CONSTRUCTION_INVENTORY_MD.is_file()
        or CONSTRUCTION_INVENTORY_MD.read_bytes() != md_bytes(rows)
    ):
        raise ValueError("current construction inventory Markdown is missing or stale")
    return verify_inventory_structure(rows, snapshot_rows)


def candidate_snapshot_rows(snapshot_path: Path) -> list[dict[str, str]]:
    if not snapshot_path.is_file():
        raise ValueError(f"construction snapshot candidate missing: {snapshot_path}")
    rows = parse_manifest(snapshot_path.read_bytes())
    return require_live_equality(rows, HANDBOOK, ROOT)


def write_construction_candidates(
    snapshot_value: str, csv_value: str, md_value: str
) -> tuple[Path, Path, int, int]:
    snapshot_path = resolve_candidate_path(snapshot_value, ROOT)
    snapshot_rows = candidate_snapshot_rows(snapshot_path)
    rows = build(snapshot_rows)
    csv_path = resolve_candidate_path(csv_value, ROOT)
    md_path = resolve_candidate_path(md_value, ROOT)
    if csv_path.suffix.lower() != ".csv" or md_path.suffix.lower() != ".md":
        raise ValueError("inventory candidate suffixes must be .csv and .md")
    if csv_path == md_path:
        raise ValueError("inventory candidate paths must be distinct")
    allowed = ROOT / "spec"
    validate_new_candidate_path(
        csv_path, allowed_root=allowed, forbidden_paths=FORBIDDEN_CANDIDATE_PATHS
    )
    validate_new_candidate_path(
        md_path, allowed_root=allowed, forbidden_paths=FORBIDDEN_CANDIDATE_PATHS
    )
    write_new_candidate(
        csv_path,
        csv_bytes(rows),
        allowed_root=allowed,
        forbidden_paths=FORBIDDEN_CANDIDATE_PATHS,
    )
    write_new_candidate(
        md_path,
        md_bytes(rows),
        allowed_root=allowed,
        forbidden_paths=FORBIDDEN_CANDIDATE_PATHS,
    )
    file_count, line_count = verify_inventory_structure(rows, snapshot_rows)
    return csv_path, md_path, file_count, line_count


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--check", action="store_true", help="verify immutable historical records"
    )
    mode.add_argument(
        "--check-construction",
        action="store_true",
        help="verify current snapshot-derived inventory artifacts",
    )
    mode.add_argument(
        "--write-construction-candidates",
        nargs=3,
        metavar=("SNAPSHOT", "CSV", "MARKDOWN"),
        help=(
            "read an explicit live-equal snapshot candidate and write inventory "
            "to two explicit, non-existing candidate paths under spec"
        ),
    )
    args = parser.parse_args(argv)
    try:
        if args.check:
            files, lines = verify_historical()
            label = "historical handbook reverse baseline"
        elif args.check_construction:
            files, lines = verify_construction()
            label = "current handbook construction inventory"
        else:
            csv_path, md_path, files, lines = write_construction_candidates(
                *args.write_construction_candidates
            )
            print(
                "wrote construction inventory candidates: "
                f"{csv_path.relative_to(ROOT)}, {md_path.relative_to(ROOT)}"
            )
            print(
                f"candidate inventory: {files} files, {lines} physical lines, "
                "all open/unmapped"
            )
            print("The candidates are not pinned evidence and make no content claim.")
            return 0
    except (OSError, ValueError) as exc:
        print(f"handbook source inventory: FAIL ({exc})")
        return 1
    print(f"verified {label}: {files} files, {lines} physical lines")
    print("This is byte inventory evidence only, not content correctness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
