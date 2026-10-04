#!/usr/bin/env python3
"""Project acquisition gaps through strictly reviewed terminal resolutions.

Absence of a terminal reviewer record leaves a true gap explicitly OPEN.  A
reviewer record changes exactly one gap to RESOLVED only after the immutable
manifest identity, exact destination content, labels, and six independent
evidence categories all pass the checks in this module.  Provenance controls
are deliberately excluded from the resolution projection.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
import unicodedata
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = "spec/acquisition-gap-manifest.csv"
REVIEWED_PATH = "spec/provenance/reviewed-acquisition-gap-resolutions.json"
SCHEMA_PATH = "spec/provenance/reviewed-acquisition-gap-resolutions.schema.json"
CSV_PATH = "spec/acquisition-gap-resolution.csv"
MD_PATH = "spec/acquisition-gap-resolution.md"

DEFAULT_MANIFEST = ROOT / MANIFEST_PATH
DEFAULT_REVIEWED = ROOT / REVIEWED_PATH
DEFAULT_CSV = ROOT / CSV_PATH
DEFAULT_MD = ROOT / MD_PATH

SCHEMA_VERSION = 2
MANIFEST_SHA256 = "0b03e6f4e0fb2abc5468ef0fce2961177d270a469d3ac37302c760a80a1a85dc"
GAP_IDS = tuple(f"ACQ-GAP-{number:03d}" for number in range(1, 7))
MANIFEST_FIELDS = (
    "acquisition_id",
    "record_type",
    "status",
    "source_file",
    "source_line",
    "source_sha256",
    "description",
)
RECORD_FIELDS = {
    "acquisition_id",
    "record_type",
    "manifest_status",
    "source_file",
    "source_line",
    "source_sha256",
    "gap_description",
    "gap_record_sha256",
    "resolution_status",
    "content_links",
    "destination_labels",
    "resolution_description",
    "verification",
    "verification_evidence",
}
NONTERMINAL_REPORT_FIELDS = {
    "path",
    "sha256",
    "report_result",
    "gap_status_effect",
    "applies_to_gap_ids",
    "rights_holder_contacts",
    "external_messages_sent",
    "subscription_only_bodies_retrieved",
    "inaccessible_bodies_credited_as_acquired",
}
NONTERMINAL_EVIDENCE_FIELDS = {
    "evidence_type",
    "path",
    "sha256",
    "gap_status_effect",
    "applies_to_gap_ids",
    "planned_volume_title",
    "planned_editors",
    "presentation_relation",
    "published_volume_identity_status",
    "volume_body_status",
    "rights_status",
}
PRESENTATION_RELATION_FIELDS = {
    "planned_presentation",
    "superseding_presentation",
    "relation_scope",
}
PLANNED_PRESENTATION_EVIDENCE_PROFILES: dict[str, dict[str, object]] = {
    "spec/research/acquisition-gap-hlics-volume-6-2026-08-13.md": {
        "evidence_type": "planned_presentation",
        "path": "spec/research/acquisition-gap-hlics-volume-6-2026-08-13.md",
        "sha256": "0de0b7d7a534476d4facde9d6cffb8d04c91acc4d6af7b5183b95493bdbd8fc2",
        "gap_status_effect": "none",
        "applies_to_gap_ids": ["ACQ-GAP-001"],
        "planned_volume_title": "Volume 6 Logical methods in computer science",
        "planned_editors": [
            "S. Abramsky",
            "D. M. Gabbay",
            "T. S. E. Maibaum",
        ],
        "presentation_relation": {
            "planned_presentation": "1995 planned Volume VI chapter presentation",
            "superseding_presentation": "2001 published Volume 5 chapter presentation",
            "relation_scope": "chapter_presentation_only",
        },
        "published_volume_identity_status": "not_established",
        "volume_body_status": "not_acquired",
        "rights_status": "not_established",
    }
}
CONTENT_LINK_FIELDS = {
    "path",
    "sha256",
    "start_line",
    "end_line",
    "content_sha256",
    "labels",
}
AUTHORITY_FILE_FIELDS = {"path", "sha256"}
AUTHORITY_LOCATOR_FIELDS = {
    "path",
    "start_line",
    "end_line",
    "content_sha256",
}
EXACT_SCOPE_FIELDS = {
    "acquisition_id",
    "gap_record_sha256",
    "content_links_digest",
}
MECHANICAL_EVIDENCE_FIELDS = {
    "category",
    "recorded_result",
    "artifact_path",
    "sha256",
    "producer_identity",
    "exact_scope",
}
AI_EVIDENCE_FIELDS = MECHANICAL_EVIDENCE_FIELDS | {
    "model",
    "model_version",
    "instructions",
    "consulted_authority_files",
    "consulted_authority_locators",
    "findings",
    "evidence_digest",
}
AI_VERIFICATION_FIELDS = (
    "source_fidelity_ai",
    "topic_specialist_ai",
    "adversarial_publication_ai",
)
VERIFICATION_FIELDS = (
    *AI_VERIFICATION_FIELDS,
    "static",
    "build",
    "visual",
)
OUTPUT_FIELDS = (
    "acquisition_id",
    "record_type",
    "manifest_status",
    "source_file",
    "source_line",
    "source_sha256",
    "gap_description",
    "gap_record_sha256",
    "resolution_status",
    "nonterminal_report_refs",
    "nonterminal_evidence_refs",
    "content_links",
    "destination_labels",
    "resolution_description",
    "source_fidelity_ai_verification",
    "topic_specialist_ai_verification",
    "adversarial_publication_ai_verification",
    "static_verification",
    "build_verification",
    "visual_verification",
    "verification_evidence",
)

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ACQUISITION_ID_RE = re.compile(r"^ACQ-(?:GAP|CONTROL)-[0-9]{3}$")
LABEL_RE = re.compile(
    r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9][A-Za-z0-9._:-]*$"
)
TEX_LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")


class DuplicateJsonFieldError(ValueError):
    """A duplicate reviewer-supplied JSON name made an object ambiguous."""


def duplicate_rejecting_object(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonFieldError(f"duplicate JSON field {key!r}")
        result[key] = value
    return result


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


def canonical_digest(value: object) -> str:
    raw = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return sha256_bytes(raw)


def require_exact_fields(
    value: object, expected: set[str], location: str
) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{location}: expected object")
    actual = set(value)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing or extra:
        details: list[str] = []
        if missing:
            details.append(f"missing {missing}")
        if extra:
            details.append(f"unexpected {extra}")
        raise ValueError(
            f"{location}: exact field set required ({'; '.join(details)})"
        )
    return value


def require_nonempty_string(value: object, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{location}: expected nonempty string")
    if value != value.strip():
        raise ValueError(f"{location}: leading or trailing whitespace is forbidden")
    return value


def require_sha256(value: object, location: str) -> str:
    if not isinstance(value, str) or SHA256_RE.fullmatch(value) is None:
        raise ValueError(f"{location}: expected lowercase SHA-256")
    return value


def require_integer(value: object, location: str, *, minimum: int = 1) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{location}: expected integer")
    if value < minimum:
        raise ValueError(f"{location}: expected integer >= {minimum}")
    return value


def repo_file(
    root: Path,
    raw_path: object,
    location: str,
) -> tuple[str, Path]:
    value = require_nonempty_string(raw_path, location)
    if "\\" in value:
        raise ValueError(f"{location}: use repository-relative POSIX path syntax")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        raise ValueError(f"{location}: path must remain inside the repository")
    if pure.parts and re.fullmatch(r"[A-Za-z]:", pure.parts[0]) is not None:
        raise ValueError(f"{location}: drive-qualified paths are forbidden")
    if value != pure.as_posix():
        raise ValueError(f"{location}: path must use canonical POSIX syntax")
    resolved_root = root.resolve()
    resolved = (resolved_root / Path(*pure.parts)).resolve()
    try:
        relative = resolved.relative_to(resolved_root).as_posix()
    except ValueError as exc:
        raise ValueError(f"{location}: path escapes the repository") from exc
    if relative != value:
        raise ValueError(
            f"{location}: symbolic-link or junction indirection is forbidden"
        )
    if not resolved.is_file():
        raise ValueError(f"{location}: file does not exist: {value}")
    return value, resolved


def _load_json(path: Path, location: str) -> object:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=duplicate_rejecting_object,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateJsonFieldError) as exc:
        raise ValueError(f"{location}: invalid JSON: {exc}") from exc


def _sorted_strings(
    value: object,
    location: str,
    *,
    pattern: re.Pattern[str] | None = None,
    require_nonempty: bool = False,
) -> list[str]:
    if not isinstance(value, list):
        raise ValueError(f"{location}: expected array")
    result: list[str] = []
    for index, item in enumerate(value):
        string = require_nonempty_string(item, f"{location}[{index}]")
        if pattern is not None and pattern.fullmatch(string) is None:
            raise ValueError(f"{location}[{index}]: malformed value")
        result.append(string)
    if len(result) != len(set(result)):
        raise ValueError(f"{location}: duplicate values are forbidden")
    if result != sorted(result):
        raise ValueError(f"{location}: values must be sorted")
    if require_nonempty and not result:
        raise ValueError(f"{location}: at least one value is required")
    return result


def _producer_key(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return " ".join(normalized.split())


def _tex_without_comments(text: str) -> str:
    output: list[str] = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for index, character in enumerate(line):
            if character != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut = index
                break
        output.append(line[:cut])
        if cut != len(line) and line.endswith(("\n", "\r")):
            output.append("\n")
    return "".join(output)


def _label_owners(root: Path) -> dict[str, list[Path]]:
    owners: dict[str, list[Path]] = {}
    handbook = root / "handbook"
    if not handbook.is_dir():
        return owners
    for path in sorted(handbook.rglob("*.tex")):
        if path.is_symlink():
            raise ValueError(f"handbook label scan: symbolic link is forbidden: {path}")
        try:
            active = _tex_without_comments(path.read_text(encoding="utf-8"))
        except UnicodeError as exc:
            raise ValueError(f"handbook label scan: non-UTF-8 TeX file: {path}") from exc
        for label in TEX_LABEL_RE.findall(active):
            owners.setdefault(label, []).append(path.resolve())
    return owners


def _line_range_bytes(path: Path, start_line: int, end_line: int) -> bytes:
    selected: list[bytes] = []
    last_line = 0
    with path.open("rb") as handle:
        for line_number, line in enumerate(handle, start=1):
            last_line = line_number
            if start_line <= line_number <= end_line:
                selected.append(line)
            if line_number >= end_line:
                break
    if last_line < end_line:
        raise ValueError(
            f"line range {start_line}-{end_line} exceeds {path} ({last_line} lines)"
        )
    return b"".join(selected)


def _cached_file_hash(path: Path, cache: dict[Path, str]) -> str:
    resolved = path.resolve()
    if resolved not in cache:
        cache[resolved] = sha256_file(resolved)
    return cache[resolved]


def _cached_range(
    path: Path,
    start_line: int,
    end_line: int,
    cache: dict[tuple[Path, int, int], bytes],
) -> bytes:
    key = (path.resolve(), start_line, end_line)
    if key not in cache:
        cache[key] = _line_range_bytes(path, start_line, end_line)
    return cache[key]


def load_manifest(
    path: Path,
    root: Path,
    *,
    expected_gap_ids: tuple[str, ...] = GAP_IDS,
    expected_manifest_sha256: str | None = MANIFEST_SHA256,
) -> list[dict[str, str]]:
    raw = path.read_bytes()
    if expected_manifest_sha256 is not None and sha256_bytes(raw) != expected_manifest_sha256:
        raise ValueError("acquisition gap manifest SHA-256 drift")
    try:
        reader = csv.DictReader(
            io.StringIO(raw.decode("utf-8"), newline=""), strict=True
        )
        if tuple(reader.fieldnames or ()) != MANIFEST_FIELDS:
            raise ValueError(
                f"acquisition gap manifest: exact header {list(MANIFEST_FIELDS)!r} required"
            )
        parsed_rows = list(reader)
    except (UnicodeError, csv.Error) as exc:
        raise ValueError(f"acquisition gap manifest: malformed CSV: {exc}") from exc
    if any(
        None in row or any(value is None for value in row.values())
        for row in parsed_rows
    ):
        raise ValueError("acquisition gap manifest: malformed CSV row")

    physical_lines = raw.splitlines(keepends=True)
    if len(physical_lines) != len(parsed_rows) + 1:
        raise ValueError(
            "acquisition gap manifest: embedded record newlines are forbidden"
        )
    seen_ids: set[str] = set()
    seen_sources: set[tuple[str, int]] = set()
    rows: list[dict[str, str]] = []
    for index, parsed in enumerate(parsed_rows, start=2):
        location = f"acquisition gap manifest row {index}"
        row = {field: parsed[field] for field in MANIFEST_FIELDS}
        acquisition_id = require_nonempty_string(
            row["acquisition_id"], f"{location}.acquisition_id"
        )
        if ACQUISITION_ID_RE.fullmatch(acquisition_id) is None:
            raise ValueError(f"{location}.acquisition_id: malformed value")
        if acquisition_id in seen_ids:
            raise ValueError(f"{location}: duplicate acquisition ID {acquisition_id}")
        seen_ids.add(acquisition_id)
        is_gap = acquisition_id.startswith("ACQ-GAP-")
        expected_type = "gap" if is_gap else "provenance_control"
        expected_status = "open" if is_gap else "active"
        if row["record_type"] != expected_type or row["status"] != expected_status:
            raise ValueError(
                f"{location}: acquisition kind/status mismatch for {acquisition_id}"
            )
        source_value, _ = repo_file(
            root, row["source_file"], f"{location}.source_file"
        )
        try:
            source_line = int(row["source_line"])
        except ValueError as exc:
            raise ValueError(f"{location}.source_line: expected integer") from exc
        if source_line < 1 or str(source_line) != row["source_line"]:
            raise ValueError(
                f"{location}.source_line: expected canonical integer >= 1"
            )
        source_key = (source_value, source_line)
        if source_key in seen_sources:
            raise ValueError(f"{location}: duplicate source file and line")
        seen_sources.add(source_key)
        require_sha256(row["source_sha256"], f"{location}.source_sha256")
        require_nonempty_string(row["description"], f"{location}.description")
        row["_manifest_row_line"] = str(index)
        row["_manifest_line_sha256"] = sha256_bytes(physical_lines[index - 1])
        row["_gap_record_sha256"] = canonical_digest(
            {field: row[field] for field in MANIFEST_FIELDS}
        )
        rows.append(row)
    gaps = [row["acquisition_id"] for row in rows if row["record_type"] == "gap"]
    if tuple(gaps) != expected_gap_ids:
        raise ValueError(
            "acquisition gap manifest: gaps are missing, reordered, or duplicated"
        )
    return rows


def _open_projection(row: dict[str, str]) -> dict[str, str]:
    return {
        "acquisition_id": row["acquisition_id"],
        "record_type": row["record_type"],
        "manifest_status": row["status"],
        "source_file": row["source_file"],
        "source_line": row["source_line"],
        "source_sha256": row["source_sha256"],
        "gap_description": row["description"],
        "gap_record_sha256": row["_gap_record_sha256"],
        "resolution_status": "OPEN",
        "nonterminal_report_refs": "[]",
        "nonterminal_evidence_refs": "[]",
        "content_links": "[]",
        "destination_labels": "[]",
        "resolution_description": "",
        "source_fidelity_ai_verification": "pending",
        "topic_specialist_ai_verification": "pending",
        "adversarial_publication_ai_verification": "pending",
        "static_verification": "pending",
        "build_verification": "pending",
        "visual_verification": "pending",
        "verification_evidence": "[]",
    }


def _normalize_content_links(
    value: object,
    location: str,
    root: Path,
    forbidden_paths: set[Path],
    file_hash_cache: dict[Path, str],
    range_cache: dict[tuple[Path, int, int], bytes],
) -> tuple[list[dict[str, object]], set[Path], list[str]]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{location}: resolution requires at least one exact content link")
    normalized: list[dict[str, object]] = []
    destination_paths: set[Path] = set()
    all_labels: set[str] = set()
    link_keys: set[tuple[str, int, int]] = set()
    for index, untyped in enumerate(value):
        item_location = f"{location}[{index}]"
        item = require_exact_fields(untyped, CONTENT_LINK_FIELDS, item_location)
        path_value, path = repo_file(root, item["path"], f"{item_location}.path")
        if path in forbidden_paths:
            raise ValueError(
                f"{item_location}.path: source, input, schema, or output cannot be resolution content"
            )
        file_digest = require_sha256(item["sha256"], f"{item_location}.sha256")
        if _cached_file_hash(path, file_hash_cache) != file_digest:
            raise ValueError(f"{item_location}.sha256: destination file SHA-256 drift")
        start_line = require_integer(item["start_line"], f"{item_location}.start_line")
        end_line = require_integer(item["end_line"], f"{item_location}.end_line")
        if end_line < start_line:
            raise ValueError(f"{item_location}: end_line precedes start_line")
        link_key = (path_value, start_line, end_line)
        if link_key in link_keys:
            raise ValueError(f"{item_location}: duplicate content link")
        link_keys.add(link_key)
        content = _cached_range(path, start_line, end_line, range_cache)
        if not content:
            raise ValueError(f"{item_location}: linked content is empty")
        content_digest = require_sha256(
            item["content_sha256"], f"{item_location}.content_sha256"
        )
        if sha256_bytes(content) != content_digest:
            raise ValueError(f"{item_location}.content_sha256: linked content drift")
        labels = _sorted_strings(
            item["labels"], f"{item_location}.labels", pattern=LABEL_RE
        )
        try:
            text = content.decode("utf-8")
        except UnicodeError as exc:
            raise ValueError(f"{item_location}: linked content must be UTF-8") from exc
        live_labels = sorted(set(TEX_LABEL_RE.findall(_tex_without_comments(text))))
        if path.suffix.casefold() == ".tex":
            if not live_labels:
                raise ValueError(
                    f"{item_location}.labels: TeX destination requires an exact label"
                )
            if labels != live_labels:
                raise ValueError(
                    f"{item_location}.labels: must exactly equal labels in linked content {live_labels!r}"
                )
        elif labels:
            raise ValueError(
                f"{item_location}.labels: labels are only valid for TeX destinations"
            )
        all_labels.update(labels)
        destination_paths.add(path)
        normalized.append(
            {
                "path": path_value,
                "sha256": file_digest,
                "start_line": start_line,
                "end_line": end_line,
                "content_sha256": content_digest,
                "labels": labels,
            }
        )
    expected_order = sorted(
        normalized,
        key=lambda item: (item["path"], item["start_line"], item["end_line"]),
    )
    if normalized != expected_order:
        raise ValueError(f"{location}: values must be sorted by path and line range")
    return normalized, destination_paths, sorted(all_labels)


def _normalize_scope(
    value: object,
    location: str,
    expected: dict[str, str],
) -> dict[str, str]:
    scope = require_exact_fields(value, EXACT_SCOPE_FIELDS, location)
    normalized = {
        "acquisition_id": require_nonempty_string(
            scope["acquisition_id"], f"{location}.acquisition_id"
        ),
        "gap_record_sha256": require_sha256(
            scope["gap_record_sha256"], f"{location}.gap_record_sha256"
        ),
        "content_links_digest": require_sha256(
            scope["content_links_digest"], f"{location}.content_links_digest"
        ),
    }
    if normalized != expected:
        raise ValueError(f"{location}: stale or mismatched exact resolution scope")
    return normalized


def _normalize_nonterminal_reports(
    value: object,
    location: str,
    rows: list[dict[str, str]],
    reviewed_path: Path,
    manifest_path: Path,
    root: Path,
    file_hash_cache: dict[Path, str],
) -> tuple[list[dict[str, object]], set[str], set[Path]]:
    if not isinstance(value, list):
        raise ValueError(f"{location}: expected array")
    gap_ids = {
        row["acquisition_id"] for row in rows if row["record_type"] == "gap"
    }
    control_ids = {
        row["acquisition_id"]
        for row in rows
        if row["record_type"] == "provenance_control"
    }
    source_paths = {
        (root / Path(*PurePosixPath(row["source_file"]).parts)).resolve()
        for row in rows
    }
    forbidden = {
        manifest_path.resolve(),
        reviewed_path.resolve(),
        (root / SCHEMA_PATH).resolve(),
        (root / CSV_PATH).resolve(),
        (root / MD_PATH).resolve(),
    } | source_paths
    normalized: list[dict[str, object]] = []
    blocking_gap_ids: set[str] = set()
    report_paths: set[Path] = set()
    report_hashes: set[str] = set()
    for index, untyped in enumerate(value):
        item_location = f"{location}[{index}]"
        item = require_exact_fields(
            untyped, NONTERMINAL_REPORT_FIELDS, item_location
        )
        path_value, path = repo_file(root, item["path"], f"{item_location}.path")
        if path in forbidden:
            raise ValueError(
                f"{item_location}.path: input, source, schema, or output cannot be a nonterminal report"
            )
        if path in report_paths:
            raise ValueError(f"{item_location}.path: duplicate nonterminal report")
        report_paths.add(path)
        report_digest = require_sha256(item["sha256"], f"{item_location}.sha256")
        if _cached_file_hash(path, file_hash_cache) != report_digest:
            raise ValueError(f"{item_location}.sha256: report SHA-256 drift")
        if report_digest in report_hashes:
            raise ValueError(
                f"{item_location}.sha256: nonterminal reports must not reuse identical bytes"
            )
        report_hashes.add(report_digest)
        if item["report_result"] != "not_clean":
            raise ValueError(
                f"{item_location}.report_result: must be 'not_clean'"
            )
        if item["gap_status_effect"] != "none":
            raise ValueError(f"{item_location}.gap_status_effect: must be 'none'")
        applies_to = _sorted_strings(
            item["applies_to_gap_ids"],
            f"{item_location}.applies_to_gap_ids",
            pattern=re.compile(r"^ACQ-GAP-[0-9]{3}$"),
            require_nonempty=True,
        )
        for gap_id in applies_to:
            if gap_id in control_ids:
                raise ValueError(
                    f"{item_location}.applies_to_gap_ids: provenance controls are nonterminal"
                )
            if gap_id not in gap_ids:
                raise ValueError(
                    f"{item_location}.applies_to_gap_ids: unknown acquisition gap {gap_id}"
                )
        for boundary_field in (
            "rights_holder_contacts",
            "external_messages_sent",
            "subscription_only_bodies_retrieved",
            "inaccessible_bodies_credited_as_acquired",
        ):
            boundary_value = item[boundary_field]
            if type(boundary_value) is not int or boundary_value != 0:
                raise ValueError(
                    f"{item_location}.{boundary_field}: must be exactly 0"
                )
        try:
            report_text = path.read_text(encoding="utf-8")
        except UnicodeError as exc:
            raise ValueError(f"{item_location}.path: report must be UTF-8") from exc
        folded = unicodedata.normalize("NFKC", report_text).casefold()
        required_phrase_groups = {
            ("not clean", '"report_result": "not_clean"'): "NOT CLEAN finding",
            ("open",): "OPEN finding",
            ("external message",): "no-external-message boundary",
            ("subscription-only",): "no-subscription-body boundary",
        }
        for phrases, name in required_phrase_groups.items():
            if not any(phrase in folded for phrase in phrases):
                raise ValueError(f"{item_location}.path: report lacks {name}")
        if not (
            "rights-holder contacts" in folded
            or "contact a rights holder" in folded
        ):
            raise ValueError(
                f"{item_location}.path: report lacks no-rights-contact boundary"
            )
        if not (
            "inaccessible bodies credited" in folded
            or "credit an inaccessible response as acquired" in folded
        ):
            raise ValueError(
                f"{item_location}.path: report lacks no-unavailable-body-credit boundary"
            )
        for gap_id in applies_to:
            if gap_id.casefold() not in folded:
                raise ValueError(
                    f"{item_location}.path: report does not identify {gap_id}"
                )
        blocking_gap_ids.update(applies_to)
        normalized.append(
            {
                "path": path_value,
                "sha256": report_digest,
                "report_result": "not_clean",
                "gap_status_effect": "none",
                "applies_to_gap_ids": applies_to,
                "rights_holder_contacts": 0,
                "external_messages_sent": 0,
                "subscription_only_bodies_retrieved": 0,
                "inaccessible_bodies_credited_as_acquired": 0,
            }
        )
    if normalized != sorted(normalized, key=lambda item: item["path"]):
        raise ValueError(f"{location}: values must be sorted by path")
    return normalized, blocking_gap_ids, report_paths


# Necessity: a completion sweep cannot represent a positive planned identity
# without pretending that the missing publication was acquired. Definition:
# planned-presentation evidence is a hash-pinned research note carrying only an
# intended title/editor credit and a distinct chapter-presentation relation,
# with three exact negative terminal boundaries. Standing: this is an
# administrative evidence record, not a publication, body, rights grant, or
# handbook claim. Nonredundancy: unlike a NOT CLEAN sweep it records a bounded
# discovery; unlike a terminal resolution it supplies no destination content or
# passing release gates. Use: it preserves the discovery while keeping the
# applicable acquisition gap OPEN and rejecting a simultaneous terminal record.
def _normalize_nonterminal_evidence(
    value: object,
    location: str,
    rows: list[dict[str, str]],
    reviewed_path: Path,
    manifest_path: Path,
    root: Path,
    file_hash_cache: dict[Path, str],
    other_nonterminal_paths: set[Path],
) -> tuple[list[dict[str, object]], set[str], set[Path]]:
    if not isinstance(value, list):
        raise ValueError(f"{location}: expected array")
    gap_ids = {
        row["acquisition_id"] for row in rows if row["record_type"] == "gap"
    }
    source_paths = {
        (root / Path(*PurePosixPath(row["source_file"]).parts)).resolve()
        for row in rows
    }
    forbidden = {
        manifest_path.resolve(),
        reviewed_path.resolve(),
        (root / SCHEMA_PATH).resolve(),
        (root / CSV_PATH).resolve(),
        (root / MD_PATH).resolve(),
    } | source_paths | other_nonterminal_paths
    other_hashes = {
        _cached_file_hash(path, file_hash_cache) for path in other_nonterminal_paths
    }
    normalized: list[dict[str, object]] = []
    blocking_gap_ids: set[str] = set()
    evidence_paths: set[Path] = set()
    evidence_hashes: set[str] = set()
    for index, untyped in enumerate(value):
        item_location = f"{location}[{index}]"
        item = require_exact_fields(
            untyped, NONTERMINAL_EVIDENCE_FIELDS, item_location
        )
        if item["evidence_type"] != "planned_presentation":
            raise ValueError(
                f"{item_location}.evidence_type: must be 'planned_presentation'"
            )
        path_value, path = repo_file(root, item["path"], f"{item_location}.path")
        if path in forbidden:
            raise ValueError(
                f"{item_location}.path: input, source, schema, output, or other "
                "nonterminal evidence cannot be reused"
            )
        if path in evidence_paths:
            raise ValueError(f"{item_location}.path: duplicate nonterminal evidence")
        evidence_paths.add(path)
        evidence_digest = require_sha256(
            item["sha256"], f"{item_location}.sha256"
        )
        if _cached_file_hash(path, file_hash_cache) != evidence_digest:
            raise ValueError(f"{item_location}.sha256: evidence SHA-256 drift")
        if evidence_digest in evidence_hashes or evidence_digest in other_hashes:
            raise ValueError(
                f"{item_location}.sha256: nonterminal evidence must use distinct bytes"
            )
        evidence_hashes.add(evidence_digest)
        if item["gap_status_effect"] != "none":
            raise ValueError(f"{item_location}.gap_status_effect: must be 'none'")
        applies_to = _sorted_strings(
            item["applies_to_gap_ids"],
            f"{item_location}.applies_to_gap_ids",
            pattern=re.compile(r"^ACQ-GAP-[0-9]{3}$"),
            require_nonempty=True,
        )
        for gap_id in applies_to:
            if gap_id not in gap_ids:
                raise ValueError(
                    f"{item_location}.applies_to_gap_ids: unknown acquisition gap {gap_id}"
                )
        title = require_nonempty_string(
            item["planned_volume_title"], f"{item_location}.planned_volume_title"
        )
        raw_editors = item["planned_editors"]
        if not isinstance(raw_editors, list) or not raw_editors:
            raise ValueError(f"{item_location}.planned_editors: expected nonempty array")
        editors = [
            require_nonempty_string(editor, f"{item_location}.planned_editors[{i}]")
            for i, editor in enumerate(raw_editors)
        ]
        if len(editors) != len(set(editors)):
            raise ValueError(f"{item_location}.planned_editors: duplicate values")
        relation = require_exact_fields(
            item["presentation_relation"],
            PRESENTATION_RELATION_FIELDS,
            f"{item_location}.presentation_relation",
        )
        planned = require_nonempty_string(
            relation["planned_presentation"],
            f"{item_location}.presentation_relation.planned_presentation",
        )
        superseding = require_nonempty_string(
            relation["superseding_presentation"],
            f"{item_location}.presentation_relation.superseding_presentation",
        )
        if _producer_key(planned) == _producer_key(superseding):
            raise ValueError(
                f"{item_location}.presentation_relation: planned and superseding "
                "presentations must remain distinct"
            )
        if relation["relation_scope"] != "chapter_presentation_only":
            raise ValueError(
                f"{item_location}.presentation_relation.relation_scope: must be "
                "'chapter_presentation_only'"
            )
        for field, expected in (
            ("published_volume_identity_status", "not_established"),
            ("volume_body_status", "not_acquired"),
            ("rights_status", "not_established"),
        ):
            if item[field] != expected:
                raise ValueError(f"{item_location}.{field}: must be {expected!r}")
        try:
            evidence_text = path.read_text(encoding="utf-8")
        except UnicodeError as exc:
            raise ValueError(f"{item_location}.path: evidence must be UTF-8") from exc
        folded = unicodedata.normalize("NFKC", evidence_text).casefold()
        required_exact_text = [*applies_to, title, *editors, planned, superseding]
        for required in required_exact_text:
            if unicodedata.normalize("NFKC", required).casefold() not in folded:
                raise ValueError(
                    f"{item_location}.path: evidence does not state {required!r}"
                )
        for phrases, name in (
            (("open",), "OPEN disposition"),
            (("completion claim",), "no-completion boundary"),
            (
                ("no volume 6 publication", "no published volume 6"),
                "no-published-volume boundary",
            ),
            (("no body", "no volume 6 body"), "no-volume-body boundary"),
            (("no reproduction",), "no-rights boundary"),
        ):
            if not any(phrase in folded for phrase in phrases):
                raise ValueError(f"{item_location}.path: evidence lacks {name}")
        normalized_item: dict[str, object] = {
            "evidence_type": "planned_presentation",
            "path": path_value,
            "sha256": evidence_digest,
            "gap_status_effect": "none",
            "applies_to_gap_ids": applies_to,
            "planned_volume_title": title,
            "planned_editors": editors,
            "presentation_relation": {
                "planned_presentation": planned,
                "superseding_presentation": superseding,
                "relation_scope": "chapter_presentation_only",
            },
            "published_volume_identity_status": "not_established",
            "volume_body_status": "not_acquired",
            "rights_status": "not_established",
        }
        profile = PLANNED_PRESENTATION_EVIDENCE_PROFILES.get(path_value)
        if profile is None or normalized_item != profile:
            raise ValueError(
                f"{item_location}: record does not match its governed evidence profile"
            )
        blocking_gap_ids.update(applies_to)
        normalized.append(normalized_item)
    if normalized != sorted(normalized, key=lambda item: item["path"]):
        raise ValueError(f"{location}: values must be sorted by path")
    return normalized, blocking_gap_ids, evidence_paths


def _normalize_authority_files(
    value: object,
    location: str,
    root: Path,
    required: dict[str, str],
    file_hash_cache: dict[Path, str],
) -> tuple[list[dict[str, str]], dict[str, Path]]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{location}: expected nonempty array")
    normalized: list[dict[str, str]] = []
    paths: dict[str, Path] = {}
    for index, untyped in enumerate(value):
        item_location = f"{location}[{index}]"
        item = require_exact_fields(untyped, AUTHORITY_FILE_FIELDS, item_location)
        path_value, path = repo_file(root, item["path"], f"{item_location}.path")
        if path_value in paths:
            raise ValueError(f"{location}: duplicate authority path")
        file_digest = require_sha256(item["sha256"], f"{item_location}.sha256")
        if _cached_file_hash(path, file_hash_cache) != file_digest:
            raise ValueError(f"{item_location}.sha256: authority file digest drift")
        paths[path_value] = path
        normalized.append({"path": path_value, "sha256": file_digest})
    if normalized != sorted(normalized, key=lambda item: item["path"]):
        raise ValueError(f"{location}: values must be sorted by path")
    for required_path, required_digest in required.items():
        actual = next(
            (item["sha256"] for item in normalized if item["path"] == required_path),
            None,
        )
        if actual != required_digest:
            raise ValueError(
                f"{location}: missing exact required authority {required_path!r}"
            )
    return normalized, paths


def _normalize_authority_locators(
    value: object,
    location: str,
    authority_paths: dict[str, Path],
    required: set[tuple[str, int, int, str]],
    range_cache: dict[tuple[Path, int, int], bytes],
) -> list[dict[str, object]]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{location}: expected nonempty array")
    normalized: list[dict[str, object]] = []
    keys: set[tuple[str, int, int]] = set()
    full_keys: set[tuple[str, int, int, str]] = set()
    located_paths: set[str] = set()
    for index, untyped in enumerate(value):
        item_location = f"{location}[{index}]"
        item = require_exact_fields(
            untyped, AUTHORITY_LOCATOR_FIELDS, item_location
        )
        path_value = require_nonempty_string(item["path"], f"{item_location}.path")
        path = authority_paths.get(path_value)
        if path is None:
            raise ValueError(
                f"{item_location}.path: locator lacks a consulted authority file"
            )
        start_line = require_integer(item["start_line"], f"{item_location}.start_line")
        end_line = require_integer(item["end_line"], f"{item_location}.end_line")
        if end_line < start_line:
            raise ValueError(f"{item_location}: end_line precedes start_line")
        key = (path_value, start_line, end_line)
        if key in keys:
            raise ValueError(f"{location}: duplicate authority locator")
        keys.add(key)
        content_digest = require_sha256(
            item["content_sha256"], f"{item_location}.content_sha256"
        )
        content = _cached_range(path, start_line, end_line, range_cache)
        if sha256_bytes(content) != content_digest:
            raise ValueError(f"{item_location}.content_sha256: authority locator drift")
        full_key = (*key, content_digest)
        full_keys.add(full_key)
        located_paths.add(path_value)
        normalized.append(
            {
                "path": path_value,
                "start_line": start_line,
                "end_line": end_line,
                "content_sha256": content_digest,
            }
        )
    if normalized != sorted(
        normalized,
        key=lambda item: (item["path"], item["start_line"], item["end_line"]),
    ):
        raise ValueError(f"{location}: values must be sorted by path and line range")
    missing = required - full_keys
    if missing:
        raise ValueError(f"{location}: missing exact required authority locator")
    if located_paths != set(authority_paths):
        raise ValueError(f"{location}: every authority file requires an exact locator")
    return normalized


def apply_reviewed_records(
    rows: list[dict[str, str]],
    reviewed_path: Path,
    manifest_path: Path,
    root: Path,
) -> list[dict[str, str]]:
    document = _load_json(reviewed_path, "reviewed acquisition-gap resolutions")
    document = require_exact_fields(
        document,
        {
            "schema_version",
            "acquisition_gap_manifest_path",
            "acquisition_gap_manifest_sha256",
            "nonterminal_reports",
            "nonterminal_evidence",
            "records",
        },
        "reviewed-resolution document",
    )
    if type(document["schema_version"]) is not int or document["schema_version"] != SCHEMA_VERSION:
        raise ValueError(
            f"reviewed-resolution document.schema_version: must be {SCHEMA_VERSION}"
        )
    if document["acquisition_gap_manifest_path"] != MANIFEST_PATH:
        raise ValueError(
            f"reviewed-resolution document.acquisition_gap_manifest_path: must be {MANIFEST_PATH!r}"
        )
    pinned_manifest_hash = require_sha256(
        document["acquisition_gap_manifest_sha256"],
        "reviewed-resolution document.acquisition_gap_manifest_sha256",
    )
    if pinned_manifest_hash != sha256_file(manifest_path):
        raise ValueError(
            "reviewed-resolution document: acquisition gap manifest SHA-256 drift"
        )
    records = document["records"]
    if not isinstance(records, list):
        raise ValueError("reviewed-resolution document.records: expected array")

    gap_rows = [row for row in rows if row["record_type"] == "gap"]
    output = [_open_projection(row) for row in gap_rows]
    file_hash_cache: dict[Path, str] = {manifest_path.resolve(): pinned_manifest_hash}
    nonterminal_reports, blocked_gap_ids, nonterminal_report_paths = (
        _normalize_nonterminal_reports(
            document["nonterminal_reports"],
            "reviewed-resolution document.nonterminal_reports",
            rows,
            reviewed_path,
            manifest_path,
            root,
            file_hash_cache,
        )
    )
    nonterminal_evidence, evidence_blocked_gap_ids, nonterminal_evidence_paths = (
        _normalize_nonterminal_evidence(
            document["nonterminal_evidence"],
            "reviewed-resolution document.nonterminal_evidence",
            rows,
            reviewed_path,
            manifest_path,
            root,
            file_hash_cache,
            nonterminal_report_paths,
        )
    )
    for projected in output:
        refs = [
            {
                "path": report["path"],
                "sha256": report["sha256"],
                "report_result": report["report_result"],
            }
            for report in nonterminal_reports
            if projected["acquisition_id"] in report["applies_to_gap_ids"]
        ]
        projected["nonterminal_report_refs"] = json.dumps(
            refs, ensure_ascii=False, separators=(",", ":")
        )
        evidence_refs = [
            evidence
            for evidence in nonterminal_evidence
            if projected["acquisition_id"] in evidence["applies_to_gap_ids"]
        ]
        projected["nonterminal_evidence_refs"] = json.dumps(
            evidence_refs, ensure_ascii=False, separators=(",", ":")
        )
    if not records:
        return output

    gap_by_id = {row["acquisition_id"]: row for row in gap_rows}
    control_ids = {
        row["acquisition_id"]
        for row in rows
        if row["record_type"] == "provenance_control"
    }
    output_by_id = {row["acquisition_id"]: row for row in output}
    seen_ids: set[str] = set()
    range_cache: dict[tuple[Path, int, int], bytes] = {}

    for index, untyped in enumerate(records):
        location = f"reviewed-resolution document.records[{index}]"
        record = require_exact_fields(untyped, RECORD_FIELDS, location)
        acquisition_id = require_nonempty_string(
            record["acquisition_id"], f"{location}.acquisition_id"
        )
        if acquisition_id in seen_ids:
            raise ValueError(f"{location}: duplicate acquisition ID {acquisition_id}")
        seen_ids.add(acquisition_id)
        if acquisition_id in control_ids:
            raise ValueError(
                f"{location}: provenance control {acquisition_id} is not a resolvable gap"
            )
        base = gap_by_id.get(acquisition_id)
        if base is None:
            raise ValueError(f"{location}: unknown acquisition gap {acquisition_id}")
        if acquisition_id in blocked_gap_ids:
            raise ValueError(
                f"{location}: cannot resolve {acquisition_id} while a pinned "
                "nonterminal NOT CLEAN report keeps it OPEN"
            )
        if acquisition_id in evidence_blocked_gap_ids:
            raise ValueError(
                f"{location}: cannot resolve {acquisition_id} while pinned "
                "nonterminal evidence keeps it OPEN"
            )
        if isinstance(record["source_line"], bool) or not isinstance(
            record["source_line"], int
        ):
            raise ValueError(f"{location}.source_line: expected integer")
        exact_identity: dict[str, object] = {
            "record_type": base["record_type"],
            "manifest_status": base["status"],
            "source_file": base["source_file"],
            "source_line": int(base["source_line"]),
            "source_sha256": base["source_sha256"],
            "gap_description": base["description"],
            "gap_record_sha256": base["_gap_record_sha256"],
        }
        for field, expected in exact_identity.items():
            if record[field] != expected:
                raise ValueError(
                    f"{location}.{field}: stale or mismatched gap identity"
                )
        if record["resolution_status"] != "resolved":
            raise ValueError(
                f"{location}.resolution_status: terminal record must be 'resolved'"
            )

        source_value, source_path = repo_file(
            root, base["source_file"], f"{location}.source_file"
        )
        if _cached_file_hash(source_path, file_hash_cache) != base["source_sha256"]:
            raise ValueError(f"{location}.source_sha256: live gap source drift")
        source_line_bytes = _cached_range(
            source_path,
            int(base["source_line"]),
            int(base["source_line"]),
            range_cache,
        )
        try:
            source_line_text = source_line_bytes.decode("utf-8")
        except UnicodeError as exc:
            raise ValueError(f"{location}.source_file: source line must be UTF-8") from exc
        if acquisition_id not in source_line_text or base["description"] not in source_line_text:
            raise ValueError(
                f"{location}.source_line: live source does not state the exact gap"
            )

        forbidden_content_paths = {
            manifest_path.resolve(),
            reviewed_path.resolve(),
            source_path,
            (root / SCHEMA_PATH).resolve(),
            (root / CSV_PATH).resolve(),
            (root / MD_PATH).resolve(),
        } | nonterminal_report_paths | nonterminal_evidence_paths
        content_links, destination_paths, expected_labels = _normalize_content_links(
            record["content_links"],
            f"{location}.content_links",
            root,
            forbidden_content_paths,
            file_hash_cache,
            range_cache,
        )
        labels = _sorted_strings(
            record["destination_labels"],
            f"{location}.destination_labels",
            pattern=LABEL_RE,
        )
        if labels != expected_labels:
            raise ValueError(
                f"{location}.destination_labels: must exactly equal linked destination labels {expected_labels!r}"
            )
        if labels:
            owners = _label_owners(root)
            for label in labels:
                occurrences = owners.get(label, [])
                if len(occurrences) != 1:
                    raise ValueError(
                        f"{location}.destination_labels: label {label!r} occurs "
                        f"{len(occurrences)} times"
                    )
                if occurrences[0] not in destination_paths:
                    raise ValueError(
                        f"{location}.destination_labels: label {label!r} is not "
                        "owned by an exact linked destination"
                    )
        resolution_description = require_nonempty_string(
            record["resolution_description"],
            f"{location}.resolution_description",
        )
        content_links_digest = canonical_digest(content_links)
        expected_scope = {
            "acquisition_id": acquisition_id,
            "gap_record_sha256": base["_gap_record_sha256"],
            "content_links_digest": content_links_digest,
        }

        verification = require_exact_fields(
            record["verification"],
            set(VERIFICATION_FIELDS),
            f"{location}.verification",
        )
        for category in VERIFICATION_FIELDS:
            if verification[category] != "pass":
                raise ValueError(
                    f"{location}.verification.{category}: resolution requires pass"
                )
        raw_evidence = record["verification_evidence"]
        if not isinstance(raw_evidence, list) or len(raw_evidence) != len(
            VERIFICATION_FIELDS
        ):
            raise ValueError(
                f"{location}.verification_evidence: exactly six records are required"
            )

        manifest_row_line = int(base["_manifest_row_line"])
        manifest_row_digest = base["_manifest_line_sha256"]
        required_authority_files = {
            MANIFEST_PATH: pinned_manifest_hash,
            source_value: base["source_sha256"],
        }
        for content_link in content_links:
            required_authority_files[str(content_link["path"])] = str(
                content_link["sha256"]
            )
        required_locators: set[tuple[str, int, int, str]] = {
            (
                MANIFEST_PATH,
                manifest_row_line,
                manifest_row_line,
                manifest_row_digest,
            ),
            (
                source_value,
                int(base["source_line"]),
                int(base["source_line"]),
                sha256_bytes(source_line_bytes),
            ),
        }
        for content_link in content_links:
            required_locators.add(
                (
                    str(content_link["path"]),
                    int(content_link["start_line"]),
                    int(content_link["end_line"]),
                    str(content_link["content_sha256"]),
                )
            )

        categories: list[str] = []
        evidence_paths: set[Path] = set()
        evidence_hashes: set[str] = set()
        producer_keys: set[str] = set()
        authority_paths_across_ai: set[Path] = set()
        authority_hashes_across_ai: set[str] = set()
        normalized_evidence: list[dict[str, object]] = []
        forbidden_evidence_paths = {
            manifest_path.resolve(),
            reviewed_path.resolve(),
            source_path,
            (root / SCHEMA_PATH).resolve(),
            (root / CSV_PATH).resolve(),
            (root / MD_PATH).resolve(),
        } | destination_paths | nonterminal_report_paths | nonterminal_evidence_paths
        forbidden_evidence_hashes = {
            pinned_manifest_hash,
            base["source_sha256"],
            base["_manifest_line_sha256"],
            sha256_bytes(source_line_bytes),
            sha256_file(reviewed_path),
        }
        forbidden_evidence_hashes.update(
            str(content_link["sha256"]) for content_link in content_links
        )
        forbidden_evidence_hashes.update(
            str(content_link["content_sha256"]) for content_link in content_links
        )
        forbidden_evidence_hashes.update(
            str(report["sha256"]) for report in nonterminal_reports
        )
        forbidden_evidence_hashes.update(
            str(evidence["sha256"]) for evidence in nonterminal_evidence
        )
        for governed_path in (
            root / SCHEMA_PATH,
            root / CSV_PATH,
            root / MD_PATH,
        ):
            if governed_path.is_file() and not governed_path.is_symlink():
                forbidden_evidence_hashes.add(
                    _cached_file_hash(governed_path, file_hash_cache)
                )
        for evidence_index, untyped_evidence in enumerate(raw_evidence):
            evidence_location = (
                f"{location}.verification_evidence[{evidence_index}]"
            )
            if not isinstance(untyped_evidence, dict):
                raise ValueError(f"{evidence_location}: expected object")
            raw_category = untyped_evidence.get("category")
            evidence_fields = (
                AI_EVIDENCE_FIELDS
                if raw_category in AI_VERIFICATION_FIELDS
                else MECHANICAL_EVIDENCE_FIELDS
            )
            item = require_exact_fields(
                untyped_evidence, evidence_fields, evidence_location
            )
            category = require_nonempty_string(
                item["category"], f"{evidence_location}.category"
            )
            if category not in VERIFICATION_FIELDS:
                raise ValueError(f"{evidence_location}.category: unknown category")
            if category in categories:
                raise ValueError(
                    f"{evidence_location}.category: duplicate evidence category"
                )
            categories.append(category)
            if item["recorded_result"] != "pass":
                raise ValueError(
                    f"{evidence_location}.recorded_result: resolution requires pass"
                )
            artifact_value, artifact_path = repo_file(
                root, item["artifact_path"], f"{evidence_location}.artifact_path"
            )
            if artifact_path in evidence_paths:
                raise ValueError(
                    f"{evidence_location}.artifact_path: separate evidence files are required"
                )
            evidence_paths.add(artifact_path)
            if artifact_path in forbidden_evidence_paths:
                raise ValueError(
                    f"{evidence_location}.artifact_path: source, input, destination, schema, or output cannot be its own evidence"
                )
            evidence_digest = require_sha256(
                item["sha256"], f"{evidence_location}.sha256"
            )
            if _cached_file_hash(artifact_path, file_hash_cache) != evidence_digest:
                raise ValueError(
                    f"{evidence_location}.sha256: evidence SHA-256 drift"
                )
            if evidence_digest in forbidden_evidence_hashes:
                raise ValueError(
                    f"{evidence_location}.sha256: source, input, destination, "
                    "schema, output, or nonterminal-report self-evidence bytes "
                    "are forbidden"
                )
            if evidence_digest in evidence_hashes:
                raise ValueError(
                    f"{evidence_location}.sha256: independent evidence must not reuse identical artifact bytes"
                )
            evidence_hashes.add(evidence_digest)
            producer = require_nonempty_string(
                item["producer_identity"],
                f"{evidence_location}.producer_identity",
            )
            producer_key = _producer_key(producer)
            if producer_key in producer_keys:
                raise ValueError(
                    f"{evidence_location}.producer_identity: every category requires a distinct recorded producer"
                )
            producer_keys.add(producer_key)
            exact_scope = _normalize_scope(
                item["exact_scope"],
                f"{evidence_location}.exact_scope",
                expected_scope,
            )
            normalized_item: dict[str, object] = {
                "category": category,
                "recorded_result": "pass",
                "artifact_path": artifact_value,
                "sha256": evidence_digest,
                "producer_identity": producer,
                "exact_scope": exact_scope,
            }
            if category in AI_VERIFICATION_FIELDS:
                model = require_nonempty_string(
                    item["model"], f"{evidence_location}.model"
                )
                model_version = require_nonempty_string(
                    item["model_version"], f"{evidence_location}.model_version"
                )
                instructions = require_nonempty_string(
                    item["instructions"], f"{evidence_location}.instructions"
                )
                authority_files, authority_paths = _normalize_authority_files(
                    item["consulted_authority_files"],
                    f"{evidence_location}.consulted_authority_files",
                    root,
                    required_authority_files,
                    file_hash_cache,
                )
                authority_paths_across_ai.update(authority_paths.values())
                authority_hashes_across_ai.update(
                    str(authority["sha256"]) for authority in authority_files
                )
                authority_locators = _normalize_authority_locators(
                    item["consulted_authority_locators"],
                    f"{evidence_location}.consulted_authority_locators",
                    authority_paths,
                    required_locators,
                    range_cache,
                )
                findings = _sorted_strings(
                    item["findings"],
                    f"{evidence_location}.findings",
                    require_nonempty=True,
                )
                ai_digest = require_sha256(
                    item["evidence_digest"],
                    f"{evidence_location}.evidence_digest",
                )
                if ai_digest != evidence_digest:
                    raise ValueError(
                        f"{evidence_location}.evidence_digest: must equal the live review evidence artifact digest"
                    )
                normalized_item.update(
                    {
                        "model": model,
                        "model_version": model_version,
                        "instructions": instructions,
                        "consulted_authority_files": authority_files,
                        "consulted_authority_locators": authority_locators,
                        "findings": findings,
                        "evidence_digest": ai_digest,
                    }
                )
            normalized_evidence.append(normalized_item)
        if tuple(categories) != VERIFICATION_FIELDS:
            raise ValueError(
                f"{location}.verification_evidence: categories must be the exact six keys in canonical order"
            )
        if evidence_paths & authority_paths_across_ai:
            raise ValueError(
                f"{location}.verification_evidence: an evidence artifact cannot serve as consulted authority evidence"
            )
        if evidence_hashes & authority_hashes_across_ai:
            raise ValueError(
                f"{location}.verification_evidence: evidence artifact bytes cannot "
                "be reused as consulted authority evidence"
            )

        output_by_id[acquisition_id].update(
            {
                "resolution_status": "RESOLVED",
                "content_links": json.dumps(
                    content_links, ensure_ascii=False, separators=(",", ":")
                ),
                "destination_labels": json.dumps(
                    labels, ensure_ascii=False, separators=(",", ":")
                ),
                "resolution_description": resolution_description,
                "source_fidelity_ai_verification": "pass",
                "topic_specialist_ai_verification": "pass",
                "adversarial_publication_ai_verification": "pass",
                "static_verification": "pass",
                "build_verification": "pass",
                "visual_verification": "pass",
                "verification_evidence": json.dumps(
                    normalized_evidence,
                    ensure_ascii=False,
                    separators=(",", ":"),
                ),
            }
        )
    return output


def csv_bytes(rows: list[dict[str, str]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=OUTPUT_FIELDS,
        lineterminator="\n",
        extrasaction="raise",
    )
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def _md_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def markdown_bytes(rows: list[dict[str, str]]) -> bytes:
    resolved = sum(row["resolution_status"] == "RESOLVED" for row in rows)
    open_count = len(rows) - resolved
    report_refs: dict[tuple[str, str], dict[str, str]] = {}
    evidence_refs: dict[tuple[str, str], dict[str, object]] = {}
    for row in rows:
        for report in json.loads(row["nonterminal_report_refs"]):
            report_refs[(report["path"], report["sha256"])] = report
        for evidence in json.loads(row["nonterminal_evidence_refs"]):
            evidence_refs[(evidence["path"], evidence["sha256"])] = evidence
    lines = [
        "# Acquisition-gap resolution",
        "",
        "Generated by `tools/build_acquisition_gap_resolution.py`; do not edit by hand.",
        "The acquisition-gap manifest remains the source record. Provenance controls",
        "remain nonterminal and are excluded from these resolution rows.",
        "",
        f"- True acquisition gaps: {len(rows)}",
        f"- RESOLVED after reviewed admission: {resolved}",
        f"- OPEN: {open_count}",
        f"- Pinned nonterminal NOT CLEAN reports: {len(report_refs)}",
        f"- Pinned nonterminal planned-presentation evidence: {len(evidence_refs)}",
        "",
        "## Why this administrative name is justified",
        "",
        "- **Necessity:** the manifest preserves the six identified acquisition gaps but",
        "  cannot record later reviewed discharge without overwriting the source record.",
        "- **Definition:** acquisition-gap resolution is the metalinguistic projection in",
        "  which a gap is RESOLVED exactly when a terminal reviewer record pins its live",
        "  manifest identity, exact destination content and applicable labels, and six",
        "  independent passing evidence records; otherwise that gap is OPEN.",
        "- **Standing:** this name denotes an administrative projection, not a motive, a",
        "  relation among motives, a statement family, or handbook doctrine.",
        "- **Nonredundancy:** the acquisition-gap manifest states what remains missing and",
        "  its controls preserve provenance roles; this projection alone records whether",
        "  one true gap has satisfied the stricter terminal evidence conditions.",
        "- **Use:** readiness checks can count residual OPEN gaps without inferring",
        "  acquisition closure from prose, controls, destinations, or unreviewed evidence.",
        "",
        "## Nonterminal report boundary",
        "",
        "A pinned NOT CLEAN report can explain why an applicable gap remains OPEN; it",
        "cannot change OPEN to RESOLVED. Each admitted report record requires exactly",
        "zero rights-holder contacts, external messages sent, subscription-only bodies",
        "retrieved, and inaccessible bodies credited as acquired.",
        "",
    ]
    if report_refs:
        lines.extend(
            [
                "| Report | SHA-256 | Result |",
                "|---|---|---|",
            ]
        )
        for report in sorted(report_refs.values(), key=lambda item: item["path"]):
            lines.append(
                "| {} | {} | {} |".format(
                    _md_cell(report["path"]),
                    report["sha256"],
                    report["report_result"],
                )
            )
        lines.append("")
    lines.extend(
        [
            "## Planned-presentation evidence boundary",
            "",
            "- **Necessity:** a completion sweep cannot record a positive planned identity",
            "  without implying that the missing publication was acquired.",
            "- **Definition:** planned-presentation evidence is a hash-pinned research note",
            "  carrying only an intended title and editor credit, a distinct chapter-level",
            "  planned/superseding presentation relation, and exact negative terminal bounds.",
            "- **Standing:** this is an administrative evidence record, not a published",
            "  volume identity, acquired body, rights grant, or handbook doctrine.",
            "- **Nonredundancy:** unlike a NOT CLEAN sweep it records a bounded discovery;",
            "  unlike a terminal resolution it supplies no admitted destination content or",
            "  passing release gates.",
            "- **Use:** it preserves the discovery while keeping the applicable gap OPEN and",
            "  rejecting a simultaneous terminal resolution record.",
            "",
        ]
    )
    if evidence_refs:
        lines.extend(
            [
                "| Gap | Evidence | SHA-256 | Effect | Planned title | Planned editors | Planned presentation | Superseding presentation | Scope | Published Volume 6 identity | Volume 6 body | Rights basis |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|",
            ]
        )
        for evidence in sorted(evidence_refs.values(), key=lambda item: item["path"]):
            relation = evidence["presentation_relation"]
            assert isinstance(relation, dict)
            values = (
                ", ".join(str(item) for item in evidence["applies_to_gap_ids"]),
                str(evidence["path"]),
                str(evidence["sha256"]),
                str(evidence["gap_status_effect"]),
                str(evidence["planned_volume_title"]),
                "; ".join(str(item) for item in evidence["planned_editors"]),
                str(relation["planned_presentation"]),
                str(relation["superseding_presentation"]),
                str(relation["relation_scope"]),
                str(evidence["published_volume_identity_status"]),
                str(evidence["volume_body_status"]),
                str(evidence["rights_status"]),
            )
            lines.append("| " + " | ".join(_md_cell(value) for value in values) + " |")
        lines.append("")
    lines.extend(
        [
        "## Rows",
        "",
        "| Gap | Source | Line | Gap record SHA-256 | Status | Nonterminal reports | Nonterminal evidence | Content links | Labels |",
        "|---|---|---:|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        values = (
            row["acquisition_id"],
            row["source_file"],
            row["source_line"],
            row["gap_record_sha256"],
            row["resolution_status"],
            row["nonterminal_report_refs"],
            row["nonterminal_evidence_refs"],
            row["content_links"],
            row["destination_labels"],
        )
        lines.append("| " + " | ".join(_md_cell(value) for value in values) + " |")
    return ("\n".join(lines) + "\n").encode("utf-8")


def build_outputs(
    manifest_path: Path,
    reviewed_path: Path,
    root: Path,
    *,
    expected_gap_ids: tuple[str, ...] = GAP_IDS,
    expected_manifest_sha256: str | None = MANIFEST_SHA256,
) -> tuple[list[dict[str, str]], bytes, bytes]:
    rows = load_manifest(
        manifest_path,
        root,
        expected_gap_ids=expected_gap_ids,
        expected_manifest_sha256=expected_manifest_sha256,
    )
    projected = apply_reviewed_records(rows, reviewed_path, manifest_path, root)
    return projected, csv_bytes(projected), markdown_bytes(projected)


def _compare(path: Path, expected: bytes) -> str | None:
    if not path.is_file() or path.is_symlink():
        return f"missing or unsafe generated file: {path}"
    if path.read_bytes() != expected:
        return f"stale generated file: {path}"
    return None


def _write_output(path: Path, data: bytes) -> None:
    if path.exists() and path.is_symlink():
        raise ValueError(f"refusing to write generated output through symlink: {path}")
    path.write_bytes(data)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="write deterministic outputs")
    mode.add_argument(
        "--check", action="store_true", help="check committed outputs byte-for-byte"
    )
    args = parser.parse_args(argv)
    try:
        rows, csv_output, markdown_output = build_outputs(
            DEFAULT_MANIFEST,
            DEFAULT_REVIEWED,
            ROOT,
            expected_gap_ids=GAP_IDS,
            expected_manifest_sha256=MANIFEST_SHA256,
        )
        if args.check:
            failures = [
                failure
                for failure in (
                    _compare(DEFAULT_CSV, csv_output),
                    _compare(DEFAULT_MD, markdown_output),
                )
                if failure is not None
            ]
            if failures:
                raise ValueError("; ".join(failures))
            action = "OK"
        else:
            _write_output(DEFAULT_CSV, csv_output)
            _write_output(DEFAULT_MD, markdown_output)
            action = "WROTE"
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        print("acquisition gap resolution: FAIL", file=sys.stderr)
        print(f"  {exc}", file=sys.stderr)
        return 1
    resolved = sum(row["resolution_status"] == "RESOLVED" for row in rows)
    print(f"acquisition gap resolution: {action}")
    print(f"  rows={len(rows)} resolved={resolved} open={len(rows) - resolved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
