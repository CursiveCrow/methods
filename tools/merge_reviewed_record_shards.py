#!/usr/bin/env python3
"""Merge reviewed-record documents deterministically and validate the result."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

REGISTER_CONTRACT_SUPERSESSION_FIELD = "contract_supersessions"
REGISTER_CONTRACT_SUPERSESSION_IDS = frozenset(
    {
        "OBL::defects::S-002",
        "OBL::defects::S-003",
        "OBL::apparatus::A-167",
        "OBL::apparatus::A-168",
    }
)


class DuplicateJsonFieldError(ValueError):
    """Raised when a JSON object repeats a field name."""


def duplicate_rejecting_object(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonFieldError(f"duplicate JSON field {key!r}")
        result[key] = value
    return result


@dataclass(frozen=True)
class Kind:
    top_fields: frozenset[str]
    identity_field: str
    identity_type: type
    validator: Callable[[dict[str, object], Path, Path], None]


def _repo_path(root: Path, module_root: Path, default: Path) -> Path:
    return root / default.resolve().relative_to(module_root.resolve())


def _validate_source(document: dict[str, object], candidate: Path, root: Path) -> None:
    import build_source_unit_audit_crosswalk as source

    source.build_rows(
        _repo_path(root, source.ROOT, source.DEFAULT_INVENTORY),
        _repo_path(root, source.ROOT, source.DEFAULT_AUDIT_MAP),
        _repo_path(root, source.ROOT, source.DEFAULT_SOURCE),
        candidate,
        root,
    )


def _validate_handbook(document: dict[str, object], candidate: Path, root: Path) -> None:
    import build_handbook_unit_reverse_ledger as handbook

    snapshot = _repo_path(root, handbook.ROOT, handbook.DEFAULT_SNAPSHOT)
    physical = _repo_path(root, handbook.ROOT, handbook.DEFAULT_PHYSICAL_INVENTORY)
    rows, snapshot_sha = handbook.build_inventory(
        snapshot,
        physical,
        root,
        str(document["construction_snapshot_sha256"]),
    )
    inventory_raw = handbook.csv_bytes(rows, handbook.INVENTORY_FIELDS)
    handbook.apply_reviewed_records(
        rows,
        candidate,
        snapshot_sha,
        handbook.sha256_bytes(inventory_raw),
        root,
        _repo_path(root, handbook.ROOT, handbook.DEFAULT_REGISTER_MANIFEST),
        _repo_path(root, handbook.ROOT, handbook.DEFAULT_PRESENTATION_ROOT),
    )


def _validate_register(document: dict[str, object], candidate: Path, root: Path) -> None:
    import build_register_obligation_closure as register

    register.build_outputs(
        _repo_path(root, register.ROOT, register.DEFAULT_MANIFEST),
        candidate,
        root,
        unit_inventory_path=_repo_path(
            root, register.ROOT, register.DEFAULT_UNIT_INVENTORY
        ),
        unit_reverse_path=_repo_path(root, register.ROOT, register.DEFAULT_UNIT_REVERSE),
        packet_root=_repo_path(root, register.ROOT, register.DEFAULT_PACKET_ROOT),
    )


KINDS = {
    "source-unit": Kind(
        frozenset(
            {"schema_version", "authority_path", "authority_sha256", "records"}
        ),
        "unit_ordinal",
        int,
        _validate_source,
    ),
    "handbook-unit": Kind(
        frozenset(
            {
                "schema_version",
                "construction_snapshot_sha256",
                "handbook_unit_inventory_sha256",
                "records",
            }
        ),
        "unit_id",
        str,
        _validate_handbook,
    ),
    "register-obligation": Kind(
        frozenset(
            {
                "schema_version",
                "register_manifest_path",
                "register_manifest_sha256",
                REGISTER_CONTRACT_SUPERSESSION_FIELD,
                "records",
            }
        ),
        "obligation_id",
        str,
        _validate_register,
    ),
}


def load_document(path: Path) -> dict[str, object]:
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=duplicate_rejecting_object,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateJsonFieldError) as exc:
        raise ValueError(f"{path}: invalid reviewed-record JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path}: document root must be an object")
    return value


def _validate_register_contract_pin(
    document: dict[str, object], path: Path
) -> list[object]:
    collection = document[REGISTER_CONTRACT_SUPERSESSION_FIELD]
    if not isinstance(collection, list) or len(collection) > 1:
        raise ValueError(
            f"{path}: contract_supersessions must be an empty or single-item array"
        )
    return collection


def merge_documents(paths: list[Path], kind_name: str) -> dict[str, object]:
    if not paths:
        raise ValueError("at least one input document is required")
    kind = KINDS[kind_name]
    first = load_document(paths[0])
    if set(first) != set(kind.top_fields):
        raise ValueError(
            f"{paths[0]}: top-level fields differ; expected {sorted(kind.top_fields)}"
        )
    base_contract_pin: list[object] | None = None
    if kind_name == "register-obligation":
        base_contract_pin = _validate_register_contract_pin(first, paths[0])
    pins = {field: first[field] for field in first if field != "records"}
    records: list[dict[str, object]] = []
    seen: set[object] = set()
    for path_index, path in enumerate(paths):
        document = first if path_index == 0 else load_document(path)
        if set(document) != set(kind.top_fields):
            raise ValueError(
                f"{path}: top-level fields differ; expected {sorted(kind.top_fields)}"
            )
        if kind_name == "register-obligation":
            candidate_contract_pin = _validate_register_contract_pin(document, path)
            if candidate_contract_pin != base_contract_pin:
                raise ValueError(
                    f"{path}: contract_supersessions: shards must not modify "
                    "the validated base collection"
                )
        candidate_pins = {
            field: document[field] for field in document if field != "records"
        }
        if candidate_pins != pins:
            raise ValueError(f"{path}: document pins differ from the first input")
        untyped_records = document["records"]
        if not isinstance(untyped_records, list):
            raise ValueError(f"{path}: records must be an array")
        for index, untyped in enumerate(untyped_records):
            if not isinstance(untyped, dict):
                raise ValueError(f"{path}: records[{index}] must be an object")
            identity = untyped.get(kind.identity_field)
            if kind.identity_type is int:
                valid_identity = type(identity) is int
            else:
                valid_identity = (
                    isinstance(identity, str)
                    and bool(identity)
                    and identity == identity.strip()
                )
            if not valid_identity:
                raise ValueError(
                    f"{path}: records[{index}].{kind.identity_field} has the wrong type"
                )
            if (
                kind_name == "register-obligation"
                and identity in REGISTER_CONTRACT_SUPERSESSION_IDS
            ):
                raise ValueError(
                    f"{path}: records[{index}] uses reserved obligation {identity!r}; "
                    "the atomic disposition belongs only in contract_supersessions"
                )
            if identity in seen:
                raise ValueError(
                    f"{path}: duplicate {kind.identity_field} {identity!r} across inputs"
                )
            seen.add(identity)
            records.append(untyped)
    records.sort(key=lambda record: record[kind.identity_field])
    return dict(pins, records=records)


def document_bytes(document: dict[str, object]) -> bytes:
    return (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def validate_domain(
    document: dict[str, object], kind_name: str, repository_root: Path
) -> None:
    repository_root = repository_root.resolve()
    if not repository_root.is_dir():
        raise ValueError(f"repository root does not exist: {repository_root}")
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", suffix=".json", prefix="reviewed-record-merge-", delete=False
        ) as handle:
            handle.write(document_bytes(document))
            temporary_path = Path(handle.name)
        KINDS[kind_name].validator(document, temporary_path, repository_root)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=sorted(KINDS), required=True)
    parser.add_argument("--input", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    try:
        input_resolved = {path.resolve() for path in args.input}
        if not args.check and args.output.resolve() in input_resolved:
            raise ValueError("write output must not overwrite an input shard")
        document = merge_documents(args.input, args.kind)
        validate_domain(document, args.kind, args.repository_root)
        expected = document_bytes(document)
        if args.check:
            if not args.output.is_file() or args.output.read_bytes() != expected:
                raise ValueError(f"stale merged output: {args.output}")
            action = "verified"
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(expected)
            action = "wrote"
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"reviewed-record merge: FAIL ({exc})", file=sys.stderr)
        return 1

    print(
        f"reviewed-record merge: {action} {len(document['records'])} "
        f"{args.kind} records from {len(args.input)} inputs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
