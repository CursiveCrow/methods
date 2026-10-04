#!/usr/bin/env python3
"""Build an exact OPEN reviewed-source-unit shard from restoration records."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools import build_source_unit_audit_crosswalk as crosswalk  # noqa: E402
from tools import check_inherited_restoration as restoration  # noqa: E402


INVENTORY = ROOT / "spec/source-unit-inventory.csv"
AUDIT_MAP = ROOT / "spec/inherited-source-map.csv"
SOURCE = ROOT / "source/formal-logic-reference.tex"
COMPLETENESS = (
    "notation",
    "definitions",
    "rules",
    "side_conditions",
    "hypotheses",
    "statements",
    "proofs",
    "examples",
    "qualifications",
    "attribution",
)
VERIFICATION = (
    "source_fidelity_ai",
    "topic_specialist_ai",
    "adversarial_publication_ai",
    "static",
    "build",
    "visual",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_inventory(path: Path) -> dict[int, dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result: dict[int, dict[str, str]] = {}
    for row in rows:
        ordinal = int(row["ordinal"])
        if ordinal in result:
            raise ValueError(f"duplicate source-unit inventory ordinal {ordinal}")
        result[ordinal] = row
    return result


def load_record(path: Path, root: Path) -> dict[str, Any]:
    record = restoration.load_json(path)
    restoration.validate_record(record, path.resolve(), root.resolve())
    if not isinstance(record, dict):
        raise ValueError(f"{path}: restoration record must be an object")
    return record


def presentation_description(unit: dict[str, str], provenance_id: str) -> str:
    title = unit["title"] or "untitled"
    start = int(unit["start_line"])
    end = int(unit["end_line"])
    return (
        f"{unit['kind']} {title!r} at authority lines {start}--{end}, within "
        f"the exact {provenance_id} restoration interval."
    )


# Necessity: the inventory has one primary-label identity column, while a source
# unit may declare more than one literal label and a one-line heading unit may
# place those labels on the immediately following lines; the identity column
# alone cannot prove the active destination labels complete.  Definition: this
# helper returns the exact literal-label sequence in the unit slice, extended
# only across the contiguous blank/label block following a heading, after
# requiring the inventory primary label first.  Standing: this is administrative
# source-to-review-record projection logic, not a mathematical alias, result
# classification, or admission.  Nonredundancy: `unit_source_label` records the
# singular inventory identity, while `stable_labels` records dedicated active
# restoration destinations; the old unit-only slice omitted adjacent heading
# aliases and could not represent double-labelled exercises.  Use:
# shard construction and validation require every supported literal source label,
# so omission, duplication, or an out-of-unit replacement fails closed.
def stable_labels_from_exact_slice(
    unit: dict[str, str], authority_lines: list[str]
) -> list[str]:
    start = int(unit["start_line"])
    end = int(unit["end_line"])
    if start < 1 or end < start or end > len(authority_lines):
        raise ValueError(
            f"source unit {unit['ordinal']}: invalid authority line slice {start}--{end}"
        )
    primary = unit["label"]
    if unit["kind"] in {"lstlisting", "verbatim"}:
        return (
            [primary]
            if primary and crosswalk.UNIT_LABEL_RE.fullmatch(primary)
            else []
        )
    slice_lines = list(authority_lines[start - 1 : end])
    heading_kinds = {
        "part",
        "chapter",
        "section",
        "section*",
        "subsection",
        "subsection*",
        "subsubsection",
        "subsubsection*",
    }
    if unit["kind"] in heading_kinds:
        cursor = end
        while cursor < len(authority_lines):
            candidate = crosswalk.tex_without_comments(authority_lines[cursor]).strip()
            if not candidate or re.fullmatch(r"\\label\s*\{[^{}\s]+\}", candidate):
                slice_lines.append(authority_lines[cursor])
                cursor += 1
                continue
            break
    exact_slice = crosswalk.tex_without_comments("\n".join(slice_lines))
    literal_labels = re.findall(r"\\label\s*\{\s*([^{}\s]+)\s*\}", exact_slice)
    if len(literal_labels) != len(set(literal_labels)):
        raise ValueError(
            f"source unit {unit['ordinal']}: duplicate literal label in exact slice"
        )

    for label in literal_labels:
        if crosswalk.UNIT_LABEL_RE.fullmatch(label) is None:
            raise ValueError(
                f"source unit {unit['ordinal']}: unsupported literal label {label!r}"
            )

    if literal_labels:
        if not primary or literal_labels[0] != primary:
            raise ValueError(
                f"source unit {unit['ordinal']}: inventory primary label is not "
                "the first literal label in the exact slice"
            )
        return literal_labels

    return (
        [primary]
        if primary and crosswalk.UNIT_LABEL_RE.fullmatch(primary)
        else []
    )


def reviewed_record(
    unit: dict[str, str],
    provenance: dict[str, Any],
    record_path: Path,
    root: Path,
    authority_lines: list[str],
) -> dict[str, object]:
    ordinal = int(unit["ordinal"])
    provenance_id = str(provenance["provenance_id"])
    artifact = provenance["restoration_artifact"]
    if not isinstance(artifact, dict):
        raise ValueError(f"{record_path}: restoration_artifact must be an object")
    destination = str(artifact["path"])
    stable_labels = stable_labels_from_exact_slice(unit, authority_lines)
    record_relative = record_path.resolve().relative_to(root.resolve()).as_posix()
    record_hash = sha256(record_path)
    return {
        "unit_ordinal": ordinal,
        "unit_kind": unit["kind"],
        "unit_title": unit["title"],
        "unit_source_label": unit["label"],
        "source_start": int(unit["start_line"]),
        "source_end": int(unit["end_line"]),
        "source_sha256": unit["sha256"],
        "restoration_record_path": record_relative,
        "restoration_record_sha256": record_hash,
        "restoration_provenance_id": provenance_id,
        "authority_path": crosswalk.AUTHORITY_PATH,
        "authority_sha256": crosswalk.AUTHORITY_SHA256,
        "authority_edition_status": "identified",
        "authority_edition_value": crosswalk.AUTHORITY_EDITION,
        "presentation_identity_status": "identified",
        "presentation_identity_value": f"{provenance_id}/unit-{ordinal:05d}",
        "presentation_identity_description": presentation_description(
            unit, provenance_id
        ),
        "provenance_disposition": crosswalk.OPEN_DISPOSITION,
        "handbook_destination_status": "identified",
        "handbook_destination": destination,
        "handbook_destination_sha256": str(artifact["sha256"]),
        "stable_labels": stable_labels,
        "audit_result": crosswalk.PENDING_AUDIT_RESULT,
        "layout_changes": [],
        "defect_exclusions": [],
        "variant_links": [],
        "completeness": {field: "pending" for field in COMPLETENESS},
        "verification": {
            field: "pass" if field == "static" else "pending"
            for field in VERIFICATION
        },
        "verification_evidence": [
            {
                "category": "static",
                "recorded_result": "pass",
                "artifact_path": record_relative,
                "sha256": record_hash,
                "producer_identity": "governed inherited-restoration validator",
                "recorded_scope": (
                    f"{provenance_id} frozen-authority identity, source-unit "
                    "membership, exact artifact digest, wrapper route, destination "
                    "locator, and pending-gate boundaries."
                ),
            }
        ],
    }


def build_document(
    record_paths: list[Path],
    root: Path = ROOT,
    inventory_path: Path | None = None,
) -> dict[str, object]:
    root = root.resolve()
    inventory_path = inventory_path or (root / "spec/source-unit-inventory.csv")
    inventory = load_inventory(inventory_path)
    authority_lines = (root / crosswalk.AUTHORITY_PATH).read_text(
        encoding="utf-8", errors="strict"
    ).splitlines()
    records: list[dict[str, object]] = []
    seen: set[int] = set()
    for raw_path in record_paths:
        path = raw_path.resolve()
        provenance = load_record(path, root)
        evidence = provenance.get("source_unit_evidence")
        if not isinstance(evidence, dict) or not isinstance(
            evidence.get("unit_ordinals"), list
        ):
            raise ValueError(f"{path}: missing source_unit_evidence.unit_ordinals")
        for untyped_ordinal in evidence["unit_ordinals"]:
            if type(untyped_ordinal) is not int:
                raise ValueError(f"{path}: source unit ordinal must be an integer")
            ordinal = untyped_ordinal
            if ordinal in seen:
                raise ValueError(f"duplicate unit ordinal {ordinal} across inputs")
            if ordinal not in inventory:
                raise ValueError(f"{path}: unknown source unit ordinal {ordinal}")
            seen.add(ordinal)
            records.append(
                reviewed_record(
                    inventory[ordinal], provenance, path, root, authority_lines
                )
            )
    records.sort(key=lambda record: int(record["unit_ordinal"]))
    return {
        "schema_version": crosswalk.REVIEW_SCHEMA_VERSION,
        "authority_path": crosswalk.AUTHORITY_PATH,
        "authority_sha256": crosswalk.AUTHORITY_SHA256,
        "records": records,
    }


def document_bytes(document: dict[str, object]) -> bytes:
    return (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def validate_document(document: dict[str, object], root: Path) -> None:
    temporary_path: Path | None = None
    try:
        inventory = load_inventory(root / "spec/source-unit-inventory.csv")
        authority_lines = (root / crosswalk.AUTHORITY_PATH).read_text(
            encoding="utf-8", errors="strict"
        ).splitlines()
        records = document.get("records")
        if not isinstance(records, list):
            raise ValueError("reviewed-source-unit shard records must be an array")
        for index, record in enumerate(records):
            if not isinstance(record, dict):
                raise ValueError(f"records[{index}]: expected object")
            ordinal = record.get("unit_ordinal")
            if type(ordinal) is not int or ordinal not in inventory:
                raise ValueError(f"records[{index}]: invalid source unit ordinal")
            expected_labels = stable_labels_from_exact_slice(
                inventory[ordinal], authority_lines
            )
            if record.get("stable_labels") != expected_labels:
                raise ValueError(
                    f"records[{index}].stable_labels: source-declared stable "
                    "labels differ from the exact unit slice"
                )
        with tempfile.NamedTemporaryFile(
            mode="wb", suffix=".json", prefix="open-source-shard-", delete=False
        ) as handle:
            handle.write(document_bytes(document))
            temporary_path = Path(handle.name)
        crosswalk.build_rows(
            root / "spec/source-unit-inventory.csv",
            root / "spec/inherited-source-map.csv",
            root / "source/formal-logic-reference.tex",
            temporary_path,
            root,
        )
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        document = build_document(args.record, args.repository_root)
        validate_document(document, args.repository_root.resolve())
        expected = document_bytes(document)
        if args.check:
            if not args.output.is_file() or args.output.read_bytes() != expected:
                raise ValueError(f"stale OPEN reviewed-source-unit shard: {args.output}")
            action = "verified"
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(expected)
            action = "wrote"
    except (OSError, UnicodeError, ValueError, restoration.CheckFailure) as error:
        print(f"OPEN source-unit shard: FAIL ({error})", file=sys.stderr)
        return 1
    print(f"OPEN source-unit shard: {action} {len(document['records'])} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
