#!/usr/bin/env python3
"""Build/check the all-residual terminal-readiness manifest and release pins."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Callable

try:
    import check_compendium_volume_manifest as publication_checker
    import check_external_coverage_assignments as coverage_checker
    import check_inherited_restoration as restoration_checker
    import build_source_unit_audit_crosswalk as source_unit_checker
except ImportError:  # pragma: no cover
    from tools import check_compendium_volume_manifest as publication_checker  # type: ignore
    from tools import check_external_coverage_assignments as coverage_checker  # type: ignore
    from tools import check_inherited_restoration as restoration_checker  # type: ignore
    from tools import build_source_unit_audit_crosswalk as source_unit_checker  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
BOOK_TITLE = "The Methods of Reason"
PUBLIC_PDF_PATH = "handbook/main.pdf"
SCHEMA_VERSION = 1
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ISO_DATETIME_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$"
)
PENDING_INHERITED_REFS_RE = re.compile(
    r"^\[metric\] pending inherited references: (\d+)$", re.MULTILINE
)
REVIEW_GATES = (
    "source_fidelity_ai",
    "topic_specialist_ai",
    "adversarial_publication_ai",
    "static",
    "build",
    "visual",
)
DEFAULT_EXPECTED_COUNTS = {
    "inherited_interval_restoration": 282,
    "source_unit_admission": 1055,
    "register_obligation_closure": 615,
    "acquisition_gap_resolution": 6,
}


@dataclass(frozen=True)
class ReadinessPaths:
    inherited_source_map: Path = Path("spec/inherited-source-map.csv")
    restoration_record_root: Path = Path("spec/provenance")
    source_units: Path = Path("spec/source-unit-audit-crosswalk.csv")
    handbook_units: Path = Path("spec/handbook-unit-reverse-ledger.csv")
    register_obligations: Path = Path("spec/register-obligation-closure.csv")
    acquisition_gaps: Path = Path("spec/acquisition-gap-resolution.csv")
    packet_admissions: Path = Path("spec/presentation-packet-admission.csv")
    coverage_index: Path = Path("spec/external-coverage-assignment-index.json")
    publication_manifest: Path = Path("spec/compendium-volume-manifest.json")
    readiness_manifest: Path = Path("spec/verification/terminal-readiness-manifest.json")
    user_final_acceptance: Path = Path("spec/provenance/user-final-acceptance.json")


class DuplicateJsonFieldError(ValueError):
    pass


@dataclass(frozen=True)
class IntervalRestorationResult:
    interval_count: int
    accounted_count: int
    residual_count: int
    restoration_record_count: int
    restoration_record_set_sha256: str
    source_map_sha256: str
    source_map_bytes: int


@dataclass(frozen=True)
class SourceOrderResult:
    pending_reference_count: int
    handbook_tree_sha256: str
    handbook_tex_file_count: int


def duplicate_rejecting_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonFieldError(f"duplicate JSON field {key!r}")
        result[key] = value
    return result


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load_json(path: Path, location: str) -> dict[str, object]:
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=duplicate_rejecting_object,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateJsonFieldError) as exc:
        raise ValueError(f"{location}: invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{location}: expected object")
    return value


def require_exact_fields(value: object, fields: set[str], location: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{location}: expected object")
    missing = sorted(fields - set(value))
    extra = sorted(set(value) - fields)
    if missing or extra:
        raise ValueError(
            f"{location}: exact field set required (missing {missing}; unexpected {extra})"
        )
    return value


def nonempty(value: object, location: str) -> str:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError(f"{location}: expected nonempty trimmed string")
    return value


def sha(value: object, location: str) -> str:
    if not isinstance(value, str) or SHA256_RE.fullmatch(value) is None:
        raise ValueError(f"{location}: expected lowercase SHA-256")
    return value


def exact_int(value: object, location: str, *, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{location}: expected integer >= {minimum}")
    return value


def relative_path_value(path: Path) -> str:
    value = path.as_posix()
    pure = PurePosixPath(value)
    if (
        pure.is_absolute()
        or any(part in ("", ".", "..") for part in pure.parts)
        or "\\" in value
    ):
        raise ValueError(f"noncanonical repository path: {value}")
    return value


def resolve_path(root: Path, path: Path, location: str, *, required: bool = True) -> Path:
    value = relative_path_value(path)
    resolved_root = root.resolve()
    resolved = (resolved_root / Path(*PurePosixPath(value).parts)).resolve()
    try:
        relative = resolved.relative_to(resolved_root).as_posix()
    except ValueError as exc:
        raise ValueError(f"{location}: path escapes repository") from exc
    if relative != value:
        raise ValueError(f"{location}: path traversal or symlink indirection")
    if required and not resolved.is_file():
        raise ValueError(f"{location}: missing file {value}")
    return resolved


def read_csv_gate(
    root: Path,
    relative: Path,
    gate_name: str,
    id_field: str,
    terminal_predicate: Callable[[dict[str, str]], bool],
    expected_count: int | None,
) -> dict[str, object]:
    path = resolve_path(root, relative, gate_name)
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise ValueError(f"{gate_name}: cannot read ledger: {exc}") from exc
    if b"\r" in raw:
        raise ValueError(f"{gate_name}: LF-only generated CSV required")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{gate_name}: invalid UTF-8: {exc}") from exc
    reader = csv.DictReader(io.StringIO(text, newline=""))
    header = tuple(reader.fieldnames or ())
    required_fields = {
        id_field,
        *[f"{review}_verification" for review in REVIEW_GATES],
    }
    if len(header) != len(set(header)) or not required_fields.issubset(header):
        raise ValueError(f"{gate_name}: required unique generated columns are missing")
    seen: set[str] = set()
    review_counts = {name: 0 for name in REVIEW_GATES}
    total = 0
    passed = 0
    for row_number, row in enumerate(reader, start=2):
        identifier = nonempty(row.get(id_field), f"{gate_name}:{row_number}.{id_field}")
        if identifier in seen:
            raise ValueError(f"{gate_name}:{row_number}: duplicate ID {identifier}")
        seen.add(identifier)
        total += 1
        all_reviews = True
        for review in REVIEW_GATES:
            value = row.get(f"{review}_verification")
            if value == "pass":
                review_counts[review] += 1
            else:
                all_reviews = False
        if terminal_predicate(row) and all_reviews:
            passed += 1
    if expected_count is not None and total != expected_count:
        raise ValueError(
            f"{gate_name}: expected {expected_count} rows, found {total}"
        )
    review_output = {
        name: {
            "required": total,
            "pass": review_counts[name],
            "residual": total - review_counts[name],
            "status": "PASS" if review_counts[name] == total else "OPEN",
        }
        for name in REVIEW_GATES
    }
    residual = total - passed
    return {
        "artifact_path": relative_path_value(relative),
        "artifact_sha256": sha256_bytes(raw),
        "required": total,
        "pass": passed,
        "residual": residual,
        "status": "PASS" if residual == 0 else "OPEN",
        "review_gates": review_output,
    }


def exact_interval_accounted_count(
    intervals: list[tuple[str, int, int]],
    record_links: list[tuple[str, int, int]],
) -> int:
    """Count map intervals covered once, rejecting overlap as non-accounting."""

    ranges_by_id: dict[str, list[tuple[int, int]]] = {
        interval_id: [] for interval_id, _start, _end in intervals
    }
    for interval_id, start, end in record_links:
        ranges = ranges_by_id.get(interval_id)
        if ranges is None:
            raise ValueError(f"restoration record references unknown interval {interval_id}")
        ranges.append((start, end))
    accounted = 0
    for interval_id, interval_start, interval_end in intervals:
        intersections = sorted(
            (max(start, interval_start), min(end, interval_end))
            for start, end in ranges_by_id[interval_id]
            if start <= interval_end and end >= interval_start
        )
        cursor = interval_start
        exact = bool(intersections)
        for start, end in intersections:
            if start != cursor or end < start:
                exact = False
                break
            cursor = end + 1
        if exact and cursor == interval_end + 1:
            accounted += 1
    return accounted


def inspect_interval_restoration(
    root: Path,
    paths: ReadinessPaths,
    *,
    validate_records: bool,
) -> IntervalRestorationResult:
    source_map_path = resolve_path(
        root, paths.inherited_source_map, "inherited source map"
    )
    source_map_lines = coverage_checker.HashedUtf8Lines(
        source_map_path, "inherited source map"
    )
    reader = csv.DictReader(source_map_lines)
    required = {"stable_id", "source_start", "source_end", "source_sha256"}
    header = tuple(reader.fieldnames or ())
    if len(header) != len(set(header)) or not required.issubset(header):
        raise ValueError("inherited source map: required unique columns are missing")
    intervals: list[tuple[str, int, int]] = []
    seen: set[str] = set()
    previous_end = 0
    for row_number, row in enumerate(reader, start=2):
        stable_id = nonempty(
            row.get("stable_id"), f"inherited source map:{row_number}.stable_id"
        )
        if stable_id in seen:
            raise ValueError(f"inherited source map:{row_number}: duplicate ID {stable_id}")
        seen.add(stable_id)
        try:
            start = int(row.get("source_start", ""))
            end = int(row.get("source_end", ""))
        except ValueError as exc:
            raise ValueError(f"inherited source map:{row_number}: invalid bounds") from exc
        if start < 1 or end < start or start <= previous_end:
            raise ValueError(
                f"inherited source map:{row_number}: intervals must be disjoint and ordered"
            )
        sha(row.get("source_sha256"), f"inherited source map:{row_number}.source_sha256")
        previous_end = end
        intervals.append((stable_id, start, end))
    record_root = (root / paths.restoration_record_root).resolve()
    try:
        record_root.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError("restoration record root escapes repository") from exc
    if not record_root.is_dir():
        raise ValueError("restoration record root is missing")
    record_paths = sorted(
        path
        for path in record_root.glob("*.json")
        if restoration_checker.PROVENANCE_ID_RE.fullmatch(path.stem)
    )
    record_links: list[tuple[str, int, int]] = []
    record_pins: list[dict[str, str]] = []
    seen_provenance: set[str] = set()
    for path in record_paths:
        try:
            raw = path.read_bytes()
        except OSError as exc:
            raise ValueError(f"restoration record {path}: cannot read: {exc}") from exc
        record = load_json(path, f"restoration record {path.name}")
        if validate_records:
            try:
                restoration_checker.validate_record(record, path, root)
            except restoration_checker.CheckFailure as exc:
                raise ValueError(f"restoration record {path.name}: {exc}") from exc
        provenance_id = nonempty(
            record.get("provenance_id"), f"restoration record {path.name}.provenance_id"
        )
        if provenance_id in seen_provenance or path.name != f"{provenance_id}.json":
            raise ValueError(f"restoration record {path.name}: duplicate or mismatched provenance ID")
        seen_provenance.add(provenance_id)
        locator = record.get("source_locator")
        if not isinstance(locator, dict):
            raise ValueError(f"restoration record {path.name}: source locator is missing")
        start = exact_int(
            locator.get("start_line"), f"restoration record {path.name}.start_line", minimum=1
        )
        end = exact_int(
            locator.get("end_line"), f"restoration record {path.name}.end_line", minimum=start
        )
        audit = record.get("audit_evidence")
        if not isinstance(audit, dict) or not isinstance(audit.get("interval_ids"), list):
            raise ValueError(f"restoration record {path.name}: interval IDs are missing")
        interval_ids = audit["interval_ids"]
        if not interval_ids or len(interval_ids) != len(set(interval_ids)):
            raise ValueError(f"restoration record {path.name}: interval IDs must be nonempty and unique")
        for index, interval_id_value in enumerate(interval_ids):
            interval_id = nonempty(
                interval_id_value,
                f"restoration record {path.name}.interval_ids[{index}]",
            )
            record_links.append((interval_id, start, end))
        relative = path.resolve().relative_to(root.resolve()).as_posix()
        record_pins.append({"path": relative, "sha256": sha256_bytes(raw)})
    accounted = exact_interval_accounted_count(intervals, record_links)
    pin_raw = json.dumps(
        record_pins, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return IntervalRestorationResult(
        interval_count=len(intervals),
        accounted_count=accounted,
        residual_count=len(intervals) - accounted,
        restoration_record_count=len(record_paths),
        restoration_record_set_sha256=sha256_bytes(pin_raw),
        source_map_sha256=source_map_lines.digest,
        source_map_bytes=source_map_lines.byte_count,
    )


def validate_corrected_source_rows(root: Path, rows: list[dict[str, str]]) -> None:
    """Live v4 unit identities force validation regardless of CSV claims."""
    corrected_owners: dict[str, set[str]] = {}
    for path in sorted((root / "spec/provenance").glob("*.json")):
        if restoration_checker.PROVENANCE_ID_RE.fullmatch(path.stem) is None:
            continue
        record = restoration_checker.load_json(path)
        if record.get("schema_version") != 4:
            continue
        restoration_checker.validate_record(record, path, root)
        for ordinal in record["source_unit_evidence"]["unit_ordinals"]:
            corrected_owners.setdefault(str(ordinal), set()).add(record["provenance_id"])
    for ordinal in corrected_owners:
        if sum(row.get("unit_ordinal") == ordinal for row in rows) != 1:
            raise ValueError(f"source_unit_admission: live corrected unit {ordinal} must occur exactly once")
    corrected_rows = [row for row in rows if
                      row.get("unit_ordinal") in corrected_owners
                      or row.get("provenance_disposition") == source_unit_checker.CORRECTED_DISPOSITION
                      or row.get("audit_result") == source_unit_checker.CORRECTED_AUDIT_RESULT]
    if not corrected_rows:
        return
    validated = {row["unit_ordinal"]: row for row in source_unit_checker.validated_reviewed_rows(root)}
    compared_fields = set(source_unit_checker.OUTPUT_FIELDS) - {"audit_interval_ids", "audit_class_evidence"}
    for row in corrected_rows:
        actual = validated.get(row.get("unit_ordinal", ""), {})
        owners = corrected_owners.get(row.get("unit_ordinal", ""))
        if owners and source_unit_checker.is_terminal_source_unit(actual) and (
            actual.get("provenance_disposition") != source_unit_checker.CORRECTED_DISPOSITION
            or actual.get("restoration_provenance_id") not in owners
        ):
            raise ValueError("source_unit_admission: terminal corrected unit must use its live version-4 provenance")
        if any(row.get(field) != actual.get(field) for field in compared_fields):
            raise ValueError("source_unit_admission: corrected row differs from validated admission")


def inspect_terminal_source_order(root: Path) -> SourceOrderResult:
    command = [
        sys.executable,
        "tools/check.py",
        "--tree",
        "handbook",
        "--strict",
        "--require-no-pending-inherited-refs",
    ]
    completed = subprocess.run(
        command,
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    combined = completed.stdout + completed.stderr
    matches = PENDING_INHERITED_REFS_RE.findall(combined)
    if len(matches) != 1:
        raise ValueError("inherited source-order terminal check emitted no unique pending count")
    pending = int(matches[0])
    hard_categories = re.findall(r"^  - ([a-z0-9-]+):", combined, re.MULTILINE)
    if pending == 0:
        if completed.returncode != 0 or hard_categories:
            raise ValueError(
                "inherited source-order terminal check failed without pending references"
            )
    elif (
        completed.returncode != 1
        or len(hard_categories) != pending
        or any(category != "pending-inherited-ref" for category in hard_categories)
    ):
        detail = combined.strip().splitlines()[-1] if combined.strip() else "no output"
        raise ValueError(
            "inherited source-order terminal check has non-pending failures: " + detail
        )
    handbook_root = resolve_path(
        root, Path("handbook/main.tex"), "handbook source-order root"
    ).parent
    pins: list[dict[str, str]] = []
    for path in sorted(handbook_root.rglob("*.tex")):
        resolved = path.resolve()
        try:
            relative = resolved.relative_to(root).as_posix()
        except ValueError as exc:
            raise ValueError(f"handbook source-order file leaves repository: {path}") from exc
        if Path(path.absolute()) != resolved:
            raise ValueError(f"handbook source-order file uses symlink indirection: {path}")
        pins.append({"path": relative, "sha256": sha256_bytes(path.read_bytes())})
    pin_raw = json.dumps(
        pins, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return SourceOrderResult(pending, sha256_bytes(pin_raw), len(pins))


def publication_identity(
    root: Path,
    paths: ReadinessPaths,
    *,
    validate_publication: bool,
) -> tuple[dict[str, object], dict[str, object]]:
    manifest_path = resolve_path(root, paths.publication_manifest, "publication manifest")
    document = load_json(manifest_path, "publication manifest")
    if validate_publication:
        failures = publication_checker.validate_manifest_structure(document)
        if not failures:
            failures.extend(publication_checker.validate_live_files(document, root))
            failures.extend(publication_checker.validate_book_sources(root))
        if failures:
            raise ValueError(f"publication controls: {failures[0]}")
    if document.get("title") != BOOK_TITLE:
        raise ValueError(f"publication manifest: title must be exactly {BOOK_TITLE!r}")
    public = document.get("public_artifact")
    if not isinstance(public, dict) or public.get("path") != PUBLIC_PDF_PATH:
        raise ValueError(f"publication manifest: public path must be {PUBLIC_PDF_PATH!r}")
    if public.get("title") != BOOK_TITLE:
        raise ValueError("publication manifest: public artifact title drift")
    observed = require_exact_fields(
        public.get("observed"), {"bytes", "pages", "sha256"}, "publication observed"
    )
    pdf_path = resolve_path(root, Path(PUBLIC_PDF_PATH), "public PDF")
    try:
        pdf_raw = pdf_path.read_bytes()
    except OSError as exc:
        raise ValueError(f"public PDF: cannot read file: {exc}") from exc
    pdf_hash = sha(observed["sha256"], "publication observed.sha256")
    pdf_bytes = exact_int(observed["bytes"], "publication observed.bytes", minimum=1)
    pdf_pages = exact_int(observed["pages"], "publication observed.pages", minimum=1)
    if len(pdf_raw) != pdf_bytes or sha256_bytes(pdf_raw) != pdf_hash:
        raise ValueError("publication observed: public PDF bytes or digest drift")
    identity = {
        "title": BOOK_TITLE,
        "path": PUBLIC_PDF_PATH,
        "sha256": pdf_hash,
        "bytes": pdf_bytes,
        "pages": pdf_pages,
    }
    identity_raw = json.dumps(
        identity, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    gate = {
        "manifest_path": relative_path_value(paths.publication_manifest),
        "publication_identity_sha256": sha256_bytes(identity_raw),
        "required": 1,
        "pass": 1,
        "residual": 0,
        "status": "PASS",
    }
    return identity, gate


def manifest_bytes(value: dict[str, object]) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def build_readiness_manifest(
    root: Path,
    paths: ReadinessPaths = ReadinessPaths(),
    *,
    expected_counts: dict[str, int] = DEFAULT_EXPECTED_COUNTS,
    interval_result: IntervalRestorationResult | None = None,
    source_order_result: SourceOrderResult | None = None,
    coverage_result: coverage_checker.CoverageAssignmentResult | None = None,
    validate_publication: bool = True,
    validate_restoration_records: bool = True,
) -> tuple[dict[str, object], bytes]:
    root = root.resolve()
    gates: dict[str, dict[str, object]] = {}
    if interval_result is None:
        interval_result = inspect_interval_restoration(
            root, paths, validate_records=validate_restoration_records
        )
    expected_intervals = expected_counts.get("inherited_interval_restoration")
    if expected_intervals is not None and interval_result.interval_count != expected_intervals:
        raise ValueError(
            "inherited_interval_restoration: expected "
            f"{expected_intervals} rows, found {interval_result.interval_count}"
        )
    gates["inherited_interval_restoration"] = {
        "artifact_path": relative_path_value(paths.inherited_source_map),
        "artifact_sha256": interval_result.source_map_sha256,
        "artifact_bytes": interval_result.source_map_bytes,
        "required": interval_result.interval_count,
        "pass": interval_result.accounted_count,
        "residual": interval_result.residual_count,
        "status": "PASS" if interval_result.residual_count == 0 else "OPEN",
        "restoration_record_count": interval_result.restoration_record_count,
        "restoration_record_set_sha256": interval_result.restoration_record_set_sha256,
    }
    if source_order_result is None:
        source_order_result = inspect_terminal_source_order(root)
    pending_refs = source_order_result.pending_reference_count
    gates["inherited_source_order"] = {
        "terminal_command": (
            "python tools/check.py --tree handbook --strict "
            "--require-no-pending-inherited-refs"
        ),
        "handbook_tree_sha256": source_order_result.handbook_tree_sha256,
        "handbook_tex_file_count": source_order_result.handbook_tex_file_count,
        "required": pending_refs,
        "pass": 0,
        "residual": pending_refs,
        "status": "PASS" if pending_refs == 0 else "OPEN",
    }
    source_rows = source_unit_checker.read_rows(resolve_path(root, paths.source_units, "source units"))
    validate_corrected_source_rows(root, source_rows)
    gates["source_unit_admission"] = read_csv_gate(
        root,
        paths.source_units,
        "source_unit_admission",
        "unit_ordinal",
        source_unit_checker.is_terminal_source_unit,
        expected_counts.get("source_unit_admission"),
    )
    gates["handbook_unit_admission"] = read_csv_gate(
        root,
        paths.handbook_units,
        "handbook_unit_admission",
        "unit_id",
        lambda row: row.get("mapping_status") == "mapped/reviewed"
        and row.get("semantic_review_status") in {"pass", "not-applicable"},
        expected_counts.get("handbook_unit_admission"),
    )
    gates["register_obligation_closure"] = read_csv_gate(
        root,
        paths.register_obligations,
        "register_obligation_closure",
        "obligation_id",
        lambda row: row.get("completion_status")
        in {"COMPLETE", "SUPERSEDED_BY_CONTRACT"},
        expected_counts.get("register_obligation_closure"),
    )
    gates["acquisition_gap_resolution"] = read_csv_gate(
        root,
        paths.acquisition_gaps,
        "acquisition_gap_resolution",
        "acquisition_id",
        lambda row: row.get("resolution_status") == "RESOLVED",
        expected_counts.get("acquisition_gap_resolution"),
    )
    gates["presentation_packet_content_admission"] = read_csv_gate(
        root,
        paths.packet_admissions,
        "presentation_packet_content_admission",
        "packet_id",
        lambda row: row.get("admission_status") == "ADMITTED",
        expected_counts.get("presentation_packet_content_admission"),
    )
    if coverage_result is None:
        coverage_result = coverage_checker.validate_index(
            root, resolve_path(root, paths.coverage_index, "coverage assignment index")
        )
    coverage_index_path = resolve_path(root, paths.coverage_index, "coverage assignment index")
    coverage_raw = coverage_index_path.read_bytes()
    gates["external_coverage_assignment"] = {
        "artifact_path": relative_path_value(paths.coverage_index),
        "artifact_sha256": sha256_bytes(coverage_raw),
        "required": coverage_result.coverage_record_count,
        "pass": coverage_result.assignment_count + coverage_result.metadata_disposition_count,
        "residual": coverage_result.unassigned_count,
        "status": "PASS" if coverage_result.unassigned_count == 0 else "OPEN",
        "admitted_packet_count": coverage_result.admitted_packet_count,
        "sidecar_count": coverage_result.sidecar_count,
        "content_assignment_count": coverage_result.assignment_count,
        "metadata_disposition_count": coverage_result.metadata_disposition_count,
        "metadata_batch_count": coverage_result.metadata_batch_count,
    }
    publication, publication_gate = publication_identity(
        root, paths, validate_publication=validate_publication
    )
    gates["publication_artifact"] = publication_gate
    residual = sum(int(gate["residual"]) for gate in gates.values())
    acceptance_path = resolve_path(
        root,
        paths.user_final_acceptance,
        "user final acceptance",
        required=False,
    )
    if residual and acceptance_path.exists():
        raise ValueError(
            "user final acceptance must be absent while non-user residuals remain"
        )
    acceptance_status = "absent" if residual else "pending"
    readiness_status = "OPEN" if residual else "AWAITING_USER_FINAL_ACCEPTANCE"
    value: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "manifest_kind": "terminal-readiness",
        "publication": publication,
        "required_review_gates": list(REVIEW_GATES),
        "gates": gates,
        "non_user_residual_count": residual,
        "user_final_acceptance": {
            "status": acceptance_status,
            "record_path": relative_path_value(paths.user_final_acceptance),
        },
        "readiness_status": readiness_status,
    }
    return value, manifest_bytes(value)


def validate_acceptance(
    root: Path,
    paths: ReadinessPaths,
    readiness: dict[str, object],
    readiness_raw: bytes,
) -> tuple[Path, bytes]:
    readiness_path = resolve_path(root, paths.readiness_manifest, "readiness manifest")
    if readiness_path.read_bytes() != readiness_raw:
        raise ValueError("readiness manifest bytes are stale")
    acceptance_path = resolve_path(root, paths.user_final_acceptance, "user final acceptance")
    acceptance_raw = acceptance_path.read_bytes()
    document = require_exact_fields(
        load_json(acceptance_path, "user final acceptance"),
        {
            "schema_version",
            "record_kind",
            "acceptance_status",
            "publication_title",
            "public_pdf",
            "readiness_manifest",
            "accepted_by",
            "accepted_at",
            "acceptance_statement",
        },
        "user final acceptance",
    )
    if type(document["schema_version"]) is not int or document["schema_version"] != 1:
        raise ValueError("user final acceptance.schema_version: must be 1")
    if document["record_kind"] != "user_final_acceptance":
        raise ValueError("user final acceptance.record_kind: exact value required")
    if document["acceptance_status"] != "accepted":
        raise ValueError("user final acceptance.acceptance_status: must be accepted")
    if document["publication_title"] != BOOK_TITLE:
        raise ValueError("user final acceptance.publication_title: title drift")
    nonempty(document["accepted_by"], "user final acceptance.accepted_by")
    accepted_at = nonempty(document["accepted_at"], "user final acceptance.accepted_at")
    if ISO_DATETIME_RE.fullmatch(accepted_at) is None:
        raise ValueError("user final acceptance.accepted_at: timezone-qualified ISO time required")
    nonempty(document["acceptance_statement"], "user final acceptance.acceptance_statement")
    publication = require_exact_fields(
        readiness.get("publication"),
        {"title", "path", "sha256", "bytes", "pages"},
        "readiness publication",
    )
    public_pdf = require_exact_fields(
        document["public_pdf"], {"path", "sha256", "bytes", "pages"}, "acceptance public_pdf"
    )
    if public_pdf != {key: publication[key] for key in ("path", "sha256", "bytes", "pages")}:
        raise ValueError("user final acceptance: public PDF identity drift")
    readiness_pin = require_exact_fields(
        document["readiness_manifest"], {"path", "sha256"}, "acceptance readiness_manifest"
    )
    if readiness_pin["path"] != relative_path_value(paths.readiness_manifest):
        raise ValueError("user final acceptance: readiness manifest path drift")
    if sha(readiness_pin["sha256"], "acceptance readiness_manifest.sha256") != sha256_bytes(readiness_raw):
        raise ValueError("user final acceptance: readiness manifest digest drift")
    return acceptance_path, acceptance_raw


def validate_terminal_release(
    root: Path,
    paths: ReadinessPaths,
    readiness: dict[str, object],
    readiness_raw: bytes,
) -> None:
    if readiness.get("non_user_residual_count") != 0:
        raise ValueError("terminal release: non-user residuals remain")
    acceptance_candidate = resolve_path(
        root, paths.user_final_acceptance, "user final acceptance", required=False
    )
    if not acceptance_candidate.is_file():
        raise ValueError("user final acceptance record is missing")
    acceptance_path, acceptance_raw = validate_acceptance(root, paths, readiness, readiness_raw)
    publication_path = resolve_path(root, paths.publication_manifest, "publication manifest")
    publication = load_json(publication_path, "publication manifest")
    public = publication.get("public_artifact")
    if not isinstance(public, dict) or public.get("publication_status") != "release" or public.get("release_ready") is not True:
        raise ValueError("terminal release: publication manifest is not release-ready")
    final = require_exact_fields(
        publication.get("final_release_evidence"),
        {
            "readiness_manifest_path",
            "readiness_manifest_sha256",
            "user_final_acceptance_path",
            "user_final_acceptance_sha256",
            "public_pdf_sha256",
        },
        "publication final_release_evidence",
    )
    expected = {
        "readiness_manifest_path": relative_path_value(paths.readiness_manifest),
        "readiness_manifest_sha256": sha256_bytes(readiness_raw),
        "user_final_acceptance_path": relative_path_value(paths.user_final_acceptance),
        "user_final_acceptance_sha256": sha256_bytes(acceptance_raw),
        "public_pdf_sha256": readiness["publication"]["sha256"],  # type: ignore[index]
    }
    if final != expected:
        raise ValueError("publication final_release_evidence: terminal pins differ")
    if acceptance_path.resolve() != resolve_path(root, paths.user_final_acceptance, "user final acceptance"):
        raise ValueError("terminal release: acceptance path drift")


def run_upstream_checks(root: Path) -> None:
    commands = (
        ("inherited interval restoration", ("tools/check_inherited_restoration.py",)),
        ("source-unit admission", ("tools/build_source_unit_audit_crosswalk.py", "--check")),
        ("handbook-unit admission", ("tools/build_handbook_unit_reverse_ledger.py", "--check")),
        ("register closure", ("tools/build_register_obligation_closure.py", "--check")),
        ("acquisition-gap resolution", ("tools/build_acquisition_gap_resolution.py", "--check")),
        ("packet admission", ("tools/build_presentation_packet_admission.py", "--check")),
    )
    for label, arguments in commands:
        completed = subprocess.run(
            [sys.executable, *arguments],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if completed.returncode:
            detail = completed.stderr.strip() or completed.stdout.strip() or "unknown failure"
            raise ValueError(f"upstream {label} check failed: {detail}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--require-ready", action="store_true")
    args = parser.parse_args(argv)
    if args.require_ready and not args.check:
        parser.error("--require-ready requires --check")
    root = args.repository_root.resolve()
    paths = ReadinessPaths()
    try:
        run_upstream_checks(root)
        readiness, raw = build_readiness_manifest(root, paths)
        output = resolve_path(root, paths.readiness_manifest, "readiness manifest", required=False)
        if args.check:
            if not output.is_file() or output.read_bytes() != raw:
                raise ValueError("terminal readiness manifest is stale")
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(raw)
        if args.require_ready:
            validate_terminal_release(root, paths, readiness, raw)
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        print(f"terminal readiness: FAIL ({exc})", file=sys.stderr)
        return 1
    action = "verified" if args.check else "wrote"
    print(f"terminal readiness: {action}; status={readiness['readiness_status']}")
    for gate_name, gate in readiness["gates"].items():  # type: ignore[union-attr]
        print(
            f"  {gate_name}: pass={gate['pass']} required={gate['required']} "
            f"residual={gate['residual']} status={gate['status']}"
        )
    print(
        f"  user_final_acceptance: {readiness['user_final_acceptance']['status']}"  # type: ignore[index]
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
