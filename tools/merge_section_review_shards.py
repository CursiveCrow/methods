#!/usr/bin/env python3
"""Validate and deterministically merge section-local review shards."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INVENTORY = ROOT / "spec/handbook-unit-inventory.csv"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
SECTION_ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9][A-Za-z0-9._:-]*$")
PART_ID_RE = re.compile(r"^p(?:0[1-9]|1[0-9])$")

GATE_ORDER = (
    "source_restoration",
    "external_content",
    "provenance_mapping",
    "topic_source_fidelity_ai",
    "topic_specialist_ai",
    "topic_adversarial_publication_ai",
    "section_source_fidelity_ai",
    "section_specialist_ai",
    "section_adversarial_publication_ai",
    "build",
    "visual",
    "internal_lock",
)
AI_GATES = frozenset(GATE_ORDER[3:9])
TOPIC_AI_GATES = frozenset(GATE_ORDER[3:6])
SECTION_AI_GATES = frozenset(GATE_ORDER[6:9])
STATE_MILESTONES = (
    (12, "internally locked"),
    (11, "visual-approved"),
    (10, "build-approved"),
    (9, "section AI-approved"),
    (6, "topics AI-approved"),
    (3, "provenance mapped"),
    (2, "external content integrated"),
    (1, "source restored"),
    (0, "queued"),
)


class DuplicateJsonFieldError(ValueError):
    pass


def duplicate_rejecting_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonFieldError(f"duplicate JSON field {key!r}")
        result[key] = value
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def is_canonical_path(value: object) -> bool:
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    pure = PurePosixPath(value)
    return (
        not pure.is_absolute()
        and pure.as_posix() == value
        and all(part not in {"", ".", ".."} for part in pure.parts)
    )


def resolve_inside(root: Path, value: str) -> Path:
    path = (root / value).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as error:
        raise ValueError(f"path leaves repository root: {value}") from error
    return path


def exact_fields(value: object, expected: set[str], where: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{where}: must be an object")
    if set(value) != expected:
        raise ValueError(
            f"{where}: fields differ from exact schema: {sorted(set(value) ^ expected)}"
        )
    return value


def nonempty_string(value: object, where: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{where}: must be a nonempty trimmed string")
    return value


def exact_sorted_unique_strings(value: object, where: str) -> list[str]:
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item or item != item.strip() for item in value
    ):
        raise ValueError(f"{where}: must be an array of nonempty trimmed strings")
    if value != sorted(set(value)):
        raise ValueError(f"{where}: must be unique and in codepoint order")
    return value


def load_unit_ids(path: Path) -> set[str]:
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None or "unit_id" not in reader.fieldnames:
                raise ValueError(f"{path}: missing unit_id column")
            result = {row["unit_id"] for row in reader}
    except OSError as error:
        raise ValueError(f"unable to read handbook-unit inventory: {error}") from error
    if "" in result:
        raise ValueError(f"{path}: blank unit_id")
    return result


def validate_hashed_file(
    item: object,
    where: str,
    root: Path,
    *,
    require_handbook_source: bool = False,
) -> tuple[str, Path]:
    record = exact_fields(item, {"path", "sha256"}, where)
    path_value = record["path"]
    digest = record["sha256"]
    if not is_canonical_path(path_value):
        raise ValueError(f"{where}.path: must be a canonical repository-relative path")
    assert isinstance(path_value, str)
    if require_handbook_source and not path_value.startswith("handbook/"):
        raise ValueError(f"{where}.path: section source must be under handbook/")
    if not isinstance(digest, str) or SHA256_RE.fullmatch(digest) is None:
        raise ValueError(f"{where}.sha256: must be a lowercase SHA-256 digest")
    path = resolve_inside(root, path_value)
    if not path.is_file():
        raise ValueError(f"{where}: missing file {path_value}")
    if sha256(path) != digest:
        subject = "source file" if require_handbook_source else "evidence file"
        raise ValueError(f"{where}: {subject} digest drifted for {path_value}")
    return path_value, path


def validate_ai_evidence(
    evidence: dict[str, Any], where: str, root: Path
) -> None:
    required = {
        "category",
        "artifact_path",
        "sha256",
        "producer_identity",
        "recorded_scope",
        "model",
        "model_version",
        "instructions",
        "consulted_authorities",
        "findings",
        "other_review_outputs_consulted",
    }
    if set(evidence) != required:
        raise ValueError(
            f"{where}: AI evidence fields differ: {sorted(set(evidence) ^ required)}"
        )
    for field in (
        "producer_identity",
        "recorded_scope",
        "model",
        "model_version",
        "instructions",
    ):
        nonempty_string(evidence[field], f"{where}.{field}")
    if evidence["other_review_outputs_consulted"] is not False:
        raise ValueError(f"{where}: AI reviewer consulted other review outputs")
    findings = exact_sorted_unique_strings(evidence["findings"], f"{where}.findings")
    if not findings:
        raise ValueError(f"{where}.findings: at least one finding or no-defect statement is required")
    authorities = evidence["consulted_authorities"]
    if not isinstance(authorities, list) or not authorities:
        raise ValueError(f"{where}.consulted_authorities: must be nonempty")
    seen: set[tuple[str, str]] = set()
    for index, item in enumerate(authorities):
        authority_where = f"{where}.consulted_authorities[{index}]"
        record = exact_fields(item, {"path", "locator", "sha256"}, authority_where)
        path_value = record["path"]
        locator = nonempty_string(record["locator"], f"{authority_where}.locator")
        if not is_canonical_path(path_value):
            raise ValueError(f"{authority_where}.path: invalid canonical path")
        assert isinstance(path_value, str)
        digest = record["sha256"]
        if not isinstance(digest, str) or SHA256_RE.fullmatch(digest) is None:
            raise ValueError(f"{authority_where}.sha256: invalid digest")
        authority_path = resolve_inside(root, path_value)
        if not authority_path.is_file() or sha256(authority_path) != digest:
            raise ValueError(f"{authority_where}: consulted authority digest drifted")
        identity = (path_value, locator)
        if identity in seen:
            raise ValueError(f"{where}: duplicate consulted authority locator")
        seen.add(identity)


def expected_state(gates: dict[str, str]) -> str:
    passed = {category for category, result in gates.items() if result == "pass"}
    for count, state in STATE_MILESTONES:
        if all(category in passed for category in GATE_ORDER[:count]):
            return state
    raise AssertionError("queued milestone is always satisfied")


def validate_gate_dependencies(gates: dict[str, str], where: str) -> None:
    if gates["external_content"] == "pass" and gates["source_restoration"] != "pass":
        raise ValueError(f"{where}: gate prefix skips source_restoration")
    if gates["provenance_mapping"] == "pass" and any(
        gates[category] != "pass" for category in GATE_ORDER[:2]
    ):
        raise ValueError(f"{where}: gate prefix skips an earlier construction gate")
    if any(gates[category] == "pass" for category in TOPIC_AI_GATES) and gates[
        "provenance_mapping"
    ] != "pass":
        raise ValueError(f"{where}: topic AI review precedes provenance mapping")
    if any(gates[category] == "pass" for category in SECTION_AI_GATES) and any(
        gates[category] != "pass" for category in TOPIC_AI_GATES
    ):
        raise ValueError(f"{where}: section AI review precedes unanimous topic review")
    if gates["build"] == "pass" and any(
        gates[category] != "pass" for category in GATE_ORDER[:9]
    ):
        raise ValueError(f"{where}: build approval precedes section AI approval")
    if gates["visual"] == "pass" and gates["build"] != "pass":
        raise ValueError(f"{where}: visual approval precedes build approval")
    if gates["internal_lock"] == "pass" and gates["visual"] != "pass":
        raise ValueError(f"{where}: internal lock precedes visual approval")


def validate_section(
    untyped: object, where: str, root: Path, known_units: set[str]
) -> dict[str, Any]:
    fields = {
        "section_id",
        "part_id",
        "title",
        "state",
        "source_files",
        "handbook_unit_ids",
        "inherited_source_unit_ordinals",
        "presentation_packet_ids",
        "register_obligation_ids",
        "dependency_section_ids",
        "gates",
        "evidence",
    }
    section = exact_fields(untyped, fields, where)
    section_id = section["section_id"]
    if not isinstance(section_id, str) or SECTION_ID_RE.fullmatch(section_id) is None:
        raise ValueError(f"{where}.section_id: invalid stable section identifier")
    part_id = section["part_id"]
    if not isinstance(part_id, str) or PART_ID_RE.fullmatch(part_id) is None:
        raise ValueError(f"{where}.part_id: must be an approved stable ID p01 through p19")
    nonempty_string(section["title"], f"{where}.title")

    source_files = section["source_files"]
    if not isinstance(source_files, list) or not source_files:
        raise ValueError(f"{where}.source_files: at least one source file is required")
    source_paths = [
        validate_hashed_file(
            item,
            f"{where}.source_files[{index}]",
            root,
            require_handbook_source=True,
        )[0]
        for index, item in enumerate(source_files)
    ]
    if source_paths != sorted(set(source_paths)):
        raise ValueError(f"{where}.source_files: paths must be unique and sorted")

    unit_ids = exact_sorted_unique_strings(
        section["handbook_unit_ids"], f"{where}.handbook_unit_ids"
    )
    if not unit_ids:
        raise ValueError(f"{where}.handbook_unit_ids: at least one unit is required")
    unknown = sorted(set(unit_ids) - known_units)
    if unknown:
        raise ValueError(f"{where}: unknown handbook unit {unknown[0]}")

    ordinals = section["inherited_source_unit_ordinals"]
    if not isinstance(ordinals, list) or any(type(value) is not int or value < 1 for value in ordinals):
        raise ValueError(f"{where}.inherited_source_unit_ordinals: invalid ordinal array")
    if ordinals != sorted(set(ordinals)):
        raise ValueError(f"{where}.inherited_source_unit_ordinals: must be unique and sorted")
    for field in (
        "presentation_packet_ids",
        "register_obligation_ids",
        "dependency_section_ids",
    ):
        exact_sorted_unique_strings(section[field], f"{where}.{field}")

    gates = exact_fields(section["gates"], set(GATE_ORDER), f"{where}.gates")
    if any(value not in {"pending", "pass"} for value in gates.values()):
        raise ValueError(f"{where}.gates: every result must be pending or pass")
    typed_gates = {category: str(gates[category]) for category in GATE_ORDER}
    validate_gate_dependencies(typed_gates, f"{where}.gates")
    state = section["state"]
    expected = expected_state(typed_gates)
    if state != expected:
        raise ValueError(f"{where}.state: {state!r}, expected {expected!r} from gates")

    evidence_list = section["evidence"]
    if not isinstance(evidence_list, list):
        raise ValueError(f"{where}.evidence: must be an array")
    evidence_by_category: dict[str, dict[str, Any]] = {}
    artifact_paths: set[Path] = set()
    for index, item in enumerate(evidence_list):
        evidence_where = f"{where}.evidence[{index}]"
        if not isinstance(item, dict):
            raise ValueError(f"{evidence_where}: must be an object")
        category = item.get("category")
        if category not in GATE_ORDER:
            raise ValueError(f"{evidence_where}.category: unknown gate")
        assert isinstance(category, str)
        if category in evidence_by_category:
            raise ValueError(f"{where}.evidence: duplicate category {category}")
        evidence_by_category[category] = item
        if category in AI_GATES:
            validate_ai_evidence(item, evidence_where, root)
        else:
            exact_fields(
                item,
                {
                    "category",
                    "artifact_path",
                    "sha256",
                    "producer_identity",
                    "recorded_scope",
                },
                evidence_where,
            )
            nonempty_string(item["producer_identity"], f"{evidence_where}.producer_identity")
            nonempty_string(item["recorded_scope"], f"{evidence_where}.recorded_scope")
        artifact_record = {
            "path": item.get("artifact_path"),
            "sha256": item.get("sha256"),
        }
        _, artifact_path = validate_hashed_file(artifact_record, evidence_where, root)
        resolved = artifact_path.resolve()
        if resolved in artifact_paths:
            raise ValueError(f"{where}.evidence: evidence artifacts must be distinct")
        artifact_paths.add(resolved)

    for category, result in typed_gates.items():
        present = category in evidence_by_category
        if (result == "pass") != present:
            raise ValueError(
                f"{where}: gate {category} requires exactly one evidence record iff pass"
            )
    for categories, label in (
        (TOPIC_AI_GATES, "topic"),
        (SECTION_AI_GATES, "section"),
    ):
        producers = [
            unicodedata.normalize(
                "NFKC", str(evidence_by_category[category]["producer_identity"])
            ).casefold()
            for category in categories
            if category in evidence_by_category
        ]
        if len(producers) != len(set(producers)):
            raise ValueError(f"{where}: {label} AI reviewers must have distinct identities")
    return section


def load_shard(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=duplicate_rejecting_object,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateJsonFieldError) as error:
        raise ValueError(f"{path}: invalid section shard: {error}") from error
    return exact_fields(value, {"schema_version", "section"}, str(path))


def merge_and_validate(
    shard_paths: list[Path], repository_root: Path, inventory_path: Path
) -> dict[str, object]:
    if not shard_paths:
        raise ValueError("at least one section shard is required")
    root = repository_root.resolve()
    if not root.is_dir():
        raise ValueError(f"repository root does not exist: {root}")
    known_units = load_unit_ids(inventory_path)
    sections: list[dict[str, Any]] = []
    seen: set[str] = set()
    for path in shard_paths:
        document = load_shard(path)
        if document["schema_version"] != 1:
            raise ValueError(f"{path}: schema_version must be exactly 1")
        section = validate_section(document["section"], str(path), root, known_units)
        section_id = section["section_id"]
        if section_id in seen:
            raise ValueError(f"duplicate section_id {section_id!r} across shards")
        seen.add(section_id)
        sections.append(section)
    sections.sort(key=lambda section: (section["part_id"], section["section_id"]))
    section_by_id = {section["section_id"]: section for section in sections}
    for section in sections:
        for dependency in section["dependency_section_ids"]:
            if dependency not in section_by_id:
                raise ValueError(
                    f"{section['section_id']}: unknown dependency section {dependency}"
                )
            if section["state"] == "internally locked" and section_by_id[dependency][
                "state"
            ] != "internally locked":
                raise ValueError(
                    f"{section['section_id']}: dependency is not internally locked: {dependency}"
                )
    return {"schema_version": 1, "sections": sections}


def output_bytes(document: dict[str, object]) -> bytes:
    return (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--handbook-unit-inventory", type=Path, default=DEFAULT_INVENTORY)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        document = merge_and_validate(
            args.input, args.repository_root, args.handbook_unit_inventory
        )
        expected = output_bytes(document)
        if args.check:
            if not args.output.is_file() or args.output.read_bytes() != expected:
                raise ValueError(f"stale merged section review ledger: {args.output}")
            action = "verified"
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(expected)
            action = "wrote"
    except (OSError, UnicodeError, ValueError) as error:
        print(f"section review shard merge: FAIL ({error})", file=sys.stderr)
        return 1
    print(f"section review shard merge: {action} {len(document['sections'])} sections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
