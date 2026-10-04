#!/usr/bin/env python3
"""Generate the typed OPEN acquisition-gap ledger from the frozen baseline."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "spec/research/full-compendium-coverage-baseline.md"
CSV_PATH = ROOT / "spec/acquisition-gap-manifest.csv"
MD_PATH = ROOT / "spec/acquisition-gap-manifest.md"
FROZEN_INPUT_SHA256 = "b44701e82b987d03476652fc8aba987705221973a149d4439ad130de0484838f"
ENTRY_RE = re.compile(
    r"^- `(?P<identifier>ACQ-(?:GAP|CONTROL)-\d{3})` "
    r"\(`(?P<status>open|active)`\): (?P<description>.+)$"
)


def collect() -> list[dict[str, str]]:
    raw = INPUT.read_bytes()
    actual_hash = hashlib.sha256(raw).hexdigest()
    if actual_hash != FROZEN_INPUT_SHA256:
        raise ValueError(
            f"{INPUT}: frozen acquisition baseline drifted "
            f"({actual_hash}, expected {FROZEN_INPUT_SHA256})"
        )
    lines = raw.decode("utf-8").splitlines()
    try:
        start = lines.index("## Supplementary acquisition notes") + 1
        end = lines.index("## Mechanical handoff rule")
    except ValueError as error:
        raise ValueError("acquisition note boundaries are missing") from error
    rows: list[dict[str, str]] = []
    for line_number, line in enumerate(lines[start:end], start=start + 1):
        if not line.startswith("- `ACQ-"):
            continue
        match = ENTRY_RE.fullmatch(line)
        if match is None:
            raise ValueError(f"{INPUT}:{line_number}: malformed acquisition record")
        identifier = match.group("identifier")
        status = match.group("status")
        kind = "gap" if "-GAP-" in identifier else "provenance_control"
        if (kind == "gap") != (status == "open"):
            raise ValueError(f"{identifier}: kind/status mismatch")
        rows.append(
            {
                "acquisition_id": identifier,
                "record_type": kind,
                "status": status,
                "source_file": "spec/research/full-compendium-coverage-baseline.md",
                "source_line": str(line_number),
                "source_sha256": FROZEN_INPUT_SHA256,
                "description": match.group("description"),
            }
        )
    expected = [f"ACQ-GAP-{number:03d}" for number in range(1, 6)] + [
        "ACQ-CONTROL-001",
        "ACQ-CONTROL-002",
        "ACQ-GAP-006",
    ]
    if [row["acquisition_id"] for row in rows] != expected:
        raise ValueError("acquisition records are missing, reordered, or duplicated")
    return rows


def csv_text(rows: list[dict[str, str]]) -> str:
    buffer = io.StringIO(newline="")
    fields = tuple(rows[0])
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def md_text(rows: list[dict[str, str]]) -> str:
    gaps = [row for row in rows if row["status"] == "open"]
    controls = [row for row in rows if row["status"] == "active"]
    lines = [
        "# Acquisition gaps and provenance controls",
        "",
        "Generated from the hash-locked supplementary acquisition notes. Every gap",
        "keeps source-acquisition closure OPEN. Active controls preserve provenance",
        "distinctions and do not close any gap.",
        "",
        f"- Open acquisition gaps: {len(gaps)}.",
        f"- Active provenance controls: {len(controls)}.",
        "- Source-acquisition closure: `OPEN`.",
        "",
        "| ID | Type | Status | Source line | Description |",
        "|---|---|---|---:|---|",
    ]
    for row in rows:
        description = row["description"].replace("|", r"\|")
        lines.append(
            f"| `{row['acquisition_id']}` | {row['record_type']} | "
            f"`{row['status']}` | {row['source_line']} | {description} |"
        )
    lines.append("")
    return "\n".join(lines)


def write_or_check(path: Path, content: str, check: bool) -> None:
    raw = content.encode("utf-8")
    if check:
        if not path.is_file() or path.read_bytes() != raw:
            raise ValueError(f"stale generated artifact: {path}")
    else:
        path.write_bytes(raw)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rows = collect()
    write_or_check(CSV_PATH, csv_text(rows), args.check)
    write_or_check(MD_PATH, md_text(rows), args.check)
    print(
        f"{'verified' if args.check else 'wrote'} acquisition ledger: "
        "6 open gaps, 2 active provenance controls; closure OPEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
