#!/usr/bin/env python3
"""Project immutable register obligations through strictly reviewed completions.

The register manifest remains the sole lossless record of the four inherited
registers.  This generator never infers terminal standing from their historical
status fields or from handbook text.  A row changes from OPEN to COMPLETE only
when a reviewer record passes every identity, support, label, and evidence check
below.  The one exact atomic notation-contract conflict is separately projected
as SUPERSEDED_BY_CONTRACT, never COMPLETE, and only after its stronger controls
pass.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
import unicodedata
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "spec/register-obligation-manifest.csv"
DEFAULT_REVIEWED = ROOT / "spec/provenance/reviewed-register-obligation-records.json"
DEFAULT_UNIT_INVENTORY = ROOT / "spec/handbook-unit-inventory.csv"
DEFAULT_UNIT_REVERSE = ROOT / "spec/handbook-unit-reverse-ledger.csv"
DEFAULT_PACKET_ROOT = ROOT / "spec/presentations"
DEFAULT_CSV = ROOT / "spec/register-obligation-closure.csv"
DEFAULT_MD = ROOT / "spec/register-obligation-closure.md"

MANIFEST_PATH = "spec/register-obligation-manifest.csv"
MANIFEST_SHA256 = "f3e18f08183192977055aa2edd30a5632d426e6f636457fab02e1f6d56e25f1f"
MANIFEST_COUNT = 615
SCHEMA_VERSION = 3

MANIFEST_FIELDS = (
    "obligation_id",
    "source_register",
    "source_line",
    "record_sha256",
    "binding_disposition",
    "original_record_json",
)
RECORD_FIELDS = {
    "obligation_id",
    "source_register",
    "source_line",
    "record_sha256",
    "completion_status",
    "handbook_unit_ids",
    "presentation_packet_ids",
    "destination_labels",
    "fulfillment_description",
    "verification",
    "verification_evidence",
}
MECHANICAL_EVIDENCE_FIELDS = {
    "category",
    "recorded_result",
    "artifact_path",
    "sha256",
    "producer_identity",
    "recorded_scope",
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
CONTRACT_SUPERSESSION_ID = "notation-contract-2026-08-11"
CONTRACT_SUPERSESSION_OBLIGATION_IDS = (
    "OBL::defects::S-002",
    "OBL::defects::S-003",
    "OBL::apparatus::A-167",
    "OBL::apparatus::A-168",
)
CONTRACT_SUPERSESSION_EXCLUDED_ID = "OBL::apparatus::A-172"
CONTRACT_SUPERSESSION_STATEMENT = (
    "Only the four listed demands to rewrite inherited notation are displaced by "
    "the 2026-08-11 fidelity contract; source tokens, renderings, scoped roles, "
    "original register rows, and every unlisted obligation remain unchanged."
)
CONTRACT_SUPERSESSION_EVIDENCE_SCOPE = (
    "Atomic notation-contract-2026-08-11: "
    "OBL::defects::S-002, OBL::defects::S-003, "
    "OBL::apparatus::A-167, OBL::apparatus::A-168"
)
SUPERSEDED_FIELDS_BY_OBLIGATION = {
    "OBL::defects::S-002": ("required_fix", "acceptance"),
    "OBL::defects::S-003": ("required_fix", "acceptance"),
    "OBL::apparatus::A-167": ("spec", "status"),
    "OBL::apparatus::A-168": ("spec", "status"),
}
CONTRACT_CLAUSE_SPECS = (
    (
        "spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md",
        3,
        7,
        ("supersedes every earlier plan",),
    ),
    (
        "spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md",
        30,
        55,
        ("retained byte for", "does not choose a winner"),
    ),
    (
        "spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md",
        68,
        69,
        ("rewriting a source presentation into house notation",),
    ),
    (
        "spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md",
        119,
        134,
        ("without content or syntax change", "**`altered`**"),
    ),
    (
        "spec/FULL-COMPENDIUM-ARCHITECTURE.md",
        49,
        60,
        ("manual editing of", "source content tokens cannot serve"),
    ),
    (
        "spec/FULL-COMPENDIUM-ARCHITECTURE.md",
        210,
        225,
        ("without rewriting it into", "house notation"),
    ),
    (
        "handbook/CONVENTIONS.md",
        3,
        8,
        ("supersedes conflicting",),
    ),
    (
        "handbook/CONVENTIONS.md",
        198,
        208,
        ("keeps its own published syntax", "rather than renamed"),
    ),
)
CURRENT_SOURCE_LOCATOR_SPECS = (
    ("OBL::defects::S-002", 3439, 3447, (r"\abs{\Meta}",)),
    ("OBL::defects::S-002", 3472, 3472, (r"\abs{\Meta}",)),
    ("OBL::defects::S-003", 3668, 3675, (r"\equiv",)),
)
HISTORICAL_SOURCE_SHA256 = (
    "81bf3c0ab12863d7d89e1b44648ccc1d63832dc68ab8e32b84aa9a0700cd6de1"
)
REVISION_LOCATOR_PAIR_SPECS = (
    (
        "OBL::defects::S-002",
        4317,
        4317,
        "72cdf3383cb543f3e7273b1fe3ba3569bffa7aae316bf57a48983623b623f2f2",
        5053,
        5053,
    ),
    (
        "OBL::defects::S-002",
        4386,
        4386,
        "eff749f747dbe7f735653eac65df946e8b390ee23bc4cbb9b47d4f1b93a81026",
        5122,
        5122,
    ),
    (
        "OBL::defects::S-003",
        4371,
        4371,
        "6295142ce77d696fb81609888eef67e6eb3531e5cb0f5178c049b00cdb6b36ba",
        5107,
        5107,
    ),
)
PROVENANCE_INTERVAL_SPECS = (
    ("SRC-03429-03518", 3429, 3518),
    ("SRC-03519-03680", 3519, 3680),
    ("SRC-05043-05131", 5043, 5131),
)
AFFECTED_SOURCE_RANGES = (
    ("SRC-03429-03518", 3439, 3447),
    ("SRC-03429-03518", 3472, 3472),
    ("SRC-03519-03680", 3668, 3675),
    ("SRC-05043-05131", 5053, 5053),
    ("SRC-05043-05131", 5107, 5107),
    ("SRC-05043-05131", 5122, 5122),
)
SURVIVING_SCOPED_ROLES = (
    {
        "glyph": r"\abs",
        "scope": "editorial handbook outside inheritedrestorationscope",
        "standing": "editorial notation",
        "role": "cardinality",
    },
    {
        "glyph": r"\dom",
        "scope": "editorial handbook outside inheritedrestorationscope",
        "standing": "editorial notation",
        "role": "domain operator",
    },
    {
        "glyph": r"\equiv",
        "scope": "editorial handbook outside inheritedrestorationscope",
        "standing": "editorial notation",
        "role": "elementary equivalence",
    },
    {
        "glyph": r"\Leftrightarrow",
        "scope": "editorial handbook outside inheritedrestorationscope",
        "standing": "editorial notation",
        "role": "formula equivalence",
    },
    {
        "glyph": r"\defeq",
        "scope": "editorial handbook outside inheritedrestorationscope",
        "standing": "editorial notation",
        "role": r"definitional abbreviation rendered :\equiv",
    },
    {
        "glyph": r"\abs",
        "scope": "inheritedrestorationscope",
        "standing": "source-supplied notation",
        "role": "the source-supplied vertical-bar role at each exact presentation",
    },
    {
        "glyph": r"\equiv",
        "scope": "inheritedrestorationscope",
        "standing": "source-supplied notation",
        "role": "the source-supplied equivalence role at each exact presentation",
    },
    {
        "glyph": r"\defeq",
        "scope": "inheritedrestorationscope",
        "standing": "source-supplied notation",
        "role": "the source-supplied definitional sign rendered :=",
    },
)
PRESERVATION_CONTROL_SPECS = (
    (
        "handbook/handbook.sty",
        tuple(
            sorted(
                (
                    r"\renewcommand\defeq{\mathrel{:=}}%",
                    r"\renewcommand\abs[1]{\lvert##1\rvert}%",
                    r"\renewcommand\Meta{\mathcal M}%",
                )
            )
        ),
    ),
    (
        "tools/test_restoration_scope.py",
        tuple(sorted((r"\ifx\abs\expectedabs", r"\ifx\equiv\expectedequiv", r"\abs{\Meta}"))),
    ),
    (
        "tools/test_part2_reader_route.py",
        tuple(
            sorted(
                (
                    r'surface.count(r"\abs{\Meta}")',
                    r'surface.count(r"\equiv")',
                    r'self.assertIn(r"\varphi\equiv\psi", surface)',
                )
            )
        ),
    ),
)
CONTRACT_SUPERSESSION_FIELDS = {
    "supersession_id",
    "obligations",
    "binding_contract_clauses",
    "revision_locator_pairs",
    "current_source_locators",
    "affected_handbook_units",
    "affected_provenance_records",
    "surviving_scoped_roles",
    "preservation_controls",
    "rendered_artifact",
    "supersession_statement",
    "verification",
    "verification_evidence",
}
SUPERSESSION_OBLIGATION_FIELDS = {
    "obligation_id",
    "source_register",
    "source_line",
    "record_sha256",
    "original_record_json_sha256",
    "superseded_fields",
}
SUPERSEDED_FIELD_FIELDS = {
    "field_name",
    "original_value",
    "original_value_sha256",
}
CLAUSE_FIELDS = {"path", "sha256", "start_line", "end_line", "excerpt_sha256"}
CURRENT_LOCATOR_FIELDS = {
    "obligation_id",
    "revision",
    "source_path",
    "source_sha256",
    "start_line",
    "end_line",
    "excerpt_sha256",
    "required_tokens",
}
REVISION_PAIR_FIELDS = {
    "obligation_id",
    "historical_revision",
    "historical_source_sha256",
    "historical_start_line",
    "historical_end_line",
    "historical_excerpt_sha256",
    "current_revision",
    "current_source_path",
    "current_source_sha256",
    "current_start_line",
    "current_end_line",
    "current_excerpt_sha256",
}
PROVENANCE_IDENTITY_FIELDS = {
    "provenance_id",
    "path",
    "sha256",
    "source_start",
    "source_end",
    "interval_sha256",
    "restoration_artifact_path",
    "restoration_artifact_sha256",
}
UNIT_IDENTITY_FIELDS = {
    "unit_id",
    "record_type",
    "path",
    "start_line",
    "end_line",
    "bytes",
    "sha256",
    "unit_kind",
    "identity_sha256",
}
SCOPED_ROLE_FIELDS = {"glyph", "scope", "standing", "role"}
PRESERVATION_CONTROL_FIELDS = {"path", "sha256", "required_tokens"}
RENDERED_ARTIFACT_FIELDS = {"path", "sha256", "bytes"}
OUTPUT_FIELDS = (
    "obligation_id",
    "source_register",
    "source_line",
    "record_sha256",
    "manifest_binding_disposition",
    "completion_status",
    "contract_supersession_id",
    "contract_supersession_record_sha256",
    "handbook_unit_ids",
    "presentation_packet_ids",
    "destination_labels",
    "fulfillment_description",
    "source_fidelity_ai_verification",
    "topic_specialist_ai_verification",
    "adversarial_publication_ai_verification",
    "static_verification",
    "build_verification",
    "visual_verification",
    "verification_evidence",
)

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
UNIT_ID_RE = re.compile(r"^HBU-[0-9a-f]+$")
LABEL_RE = re.compile(
    r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9][A-Za-z0-9._:-]*$"
)
LABEL_OWNER_ENVIRONMENTS = (
    "hbtheorem",
    "hblemma",
    "hbcorollary",
    "hbdefinition",
    "hbconvention",
    "hbmethod",
    "hbexample",
    "hbwarning",
    "proofboundary",
    "systementry",
    "annexitem",
)

csv.field_size_limit(2_147_483_647)


class DuplicateJsonFieldError(ValueError):
    """A duplicate name made a reviewer-supplied JSON object ambiguous."""


def duplicate_rejecting_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonFieldError(f"duplicate JSON field {key!r}")
        result[key] = value
    return result


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


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
        raise ValueError(f"{location}: exact field set required ({'; '.join(details)})")
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


def repo_file(
    root: Path,
    raw_path: object,
    location: str,
    *,
    required_prefix: str | None = None,
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
    if required_prefix is not None and not value.startswith(required_prefix):
        raise ValueError(f"{location}: path must start with {required_prefix!r}")
    resolved_root = root.resolve()
    resolved = (resolved_root / Path(*pure.parts)).resolve()
    try:
        relative = resolved.relative_to(resolved_root).as_posix()
    except ValueError as exc:
        raise ValueError(f"{location}: path escapes the repository") from exc
    if relative != value:
        raise ValueError(f"{location}: symbolic-link or junction indirection is forbidden")
    if not resolved.is_file():
        raise ValueError(f"{location}: file does not exist: {value}")
    return value, resolved


def _source_records(path: Path) -> dict[int, tuple[str, str, str]]:
    """Return start-line -> (row digest, canonical JSON, row id)."""

    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    raw_lines = raw.splitlines(keepends=True)
    reader = csv.reader(io.StringIO(text, newline=""), strict=True)
    try:
        header = next(reader)
    except StopIteration as exc:
        raise ValueError(f"{path}: empty register") from exc
    if not header or "id" not in header or len(set(header)) != len(header):
        raise ValueError(f"{path}: invalid or duplicate source-register header")
    previous_end = reader.line_num
    result: dict[int, tuple[str, str, str]] = {}
    for cells in reader:
        start = previous_end + 1
        end = reader.line_num
        if len(cells) != len(header):
            raise ValueError(f"{path}:{start}: malformed CSV record")
        values = dict(zip(header, cells, strict=True))
        row_bytes = b"".join(raw_lines[start - 1 : end])
        canonical = json.dumps(values, ensure_ascii=False, separators=(",", ":"))
        result[start] = (sha256_bytes(row_bytes), canonical, values["id"])
        previous_end = end
    if previous_end != len(raw_lines):
        raise ValueError(f"{path}: unparsed source-register lines")
    return result


def load_manifest(
    path: Path,
    root: Path,
    *,
    expected_count: int = MANIFEST_COUNT,
    expected_sha256: str | None = MANIFEST_SHA256,
) -> list[dict[str, str]]:
    raw = path.read_bytes()
    if expected_sha256 is not None and sha256_bytes(raw) != expected_sha256:
        raise ValueError("register manifest SHA-256 drift")
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8"), newline=""), strict=True)
    if tuple(reader.fieldnames or ()) != MANIFEST_FIELDS:
        raise ValueError(
            f"register manifest: exact header {list(MANIFEST_FIELDS)!r} required"
        )
    rows = list(reader)
    if len(rows) != expected_count:
        raise ValueError(
            f"register manifest: expected {expected_count} rows, found {len(rows)}"
        )
    by_id: set[str] = set()
    by_source_line: set[tuple[str, int]] = set()
    parsed_registers: dict[str, dict[int, tuple[str, str, str]]] = {}
    for index, row in enumerate(rows, start=2):
        location = f"register manifest row {index}"
        if None in row or any(value is None for value in row.values()):
            raise ValueError(f"{location}: malformed CSV row")
        obligation_id = require_nonempty_string(row["obligation_id"], f"{location}.obligation_id")
        if obligation_id in by_id:
            raise ValueError(f"{location}: duplicate obligation ID {obligation_id}")
        by_id.add(obligation_id)
        source_register, source_path = repo_file(
            root,
            row["source_register"],
            f"{location}.source_register",
            required_prefix="spec/registers/",
        )
        try:
            source_line = int(row["source_line"])
        except ValueError as exc:
            raise ValueError(f"{location}.source_line: expected integer") from exc
        if source_line < 2 or str(source_line) != row["source_line"]:
            raise ValueError(f"{location}.source_line: expected canonical integer >= 2")
        source_key = (source_register, source_line)
        if source_key in by_source_line:
            raise ValueError(f"{location}: duplicate source register and line")
        by_source_line.add(source_key)
        digest = require_sha256(row["record_sha256"], f"{location}.record_sha256")
        if row["binding_disposition"] != "open":
            raise ValueError(f"{location}.binding_disposition: immutable value must be 'open'")
        if source_register not in parsed_registers:
            parsed_registers[source_register] = _source_records(source_path)
        parsed = parsed_registers[source_register]
        source_record = parsed.get(source_line)
        if source_record is None:
            raise ValueError(f"{location}: source line does not begin a live CSV record")
        live_digest, live_json, live_row_id = source_record
        if digest != live_digest:
            raise ValueError(f"{location}: source-record SHA-256 drift")
        if row["original_record_json"] != live_json:
            raise ValueError(f"{location}: original record JSON drift")
        expected_id = f"OBL::{Path(source_register).stem}::{live_row_id}"
        if obligation_id != expected_id:
            raise ValueError(f"{location}: obligation ID does not match live source row")
    return rows


def _read_csv(path: Path, location: str) -> tuple[tuple[str, ...], list[dict[str, str]]]:
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, strict=True)
            header = tuple(reader.fieldnames or ())
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        raise ValueError(f"{location}: could not read CSV: {exc}") from exc
    if not header or len(set(header)) != len(header):
        raise ValueError(f"{location}: missing or duplicate header")
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError(f"{location}: malformed CSV row")
    return header, rows


def _json_string_array(raw: str, location: str) -> list[str]:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{location}: expected JSON string array") from exc
    if (
        not isinstance(value, list)
        or any(not isinstance(item, str) or not item.strip() or item != item.strip() for item in value)
        or len(value) != len(set(value))
        or value != sorted(value)
    ):
        raise ValueError(f"{location}: expected sorted unique nonempty JSON string array")
    return value


def load_admitted_units(
    inventory_path: Path,
    reverse_path: Path,
) -> dict[str, dict[str, Any]]:
    if not inventory_path.is_file() or not reverse_path.is_file():
        raise ValueError(
            "handbook-unit inventory and reverse ledger are required for handbook-unit links"
        )
    inventory_header, inventory_rows = _read_csv(inventory_path, "handbook-unit inventory")
    reverse_header, reverse_rows = _read_csv(reverse_path, "handbook-unit reverse ledger")
    required = {
        "unit_id",
        "mapping_status",
        "semantic_review_status",
        "stable_labels",
        "register_obligation_ids",
    }
    if "unit_id" not in inventory_header:
        raise ValueError("handbook-unit inventory: unit_id column is required")
    if not required.issubset(reverse_header):
        raise ValueError(
            "handbook-unit reverse ledger: required columns missing: "
            + ", ".join(sorted(required - set(reverse_header)))
        )
    inventory_by_id: dict[str, dict[str, str]] = {}
    for index, row in enumerate(inventory_rows, start=2):
        unit_id = require_nonempty_string(row["unit_id"], f"handbook-unit inventory row {index}.unit_id")
        if UNIT_ID_RE.fullmatch(unit_id) is None:
            raise ValueError(f"handbook-unit inventory row {index}: malformed unit ID")
        if unit_id in inventory_by_id:
            raise ValueError(f"handbook-unit inventory row {index}: duplicate unit ID")
        inventory_by_id[unit_id] = row
    reverse_by_id: dict[str, dict[str, Any]] = {}
    shared_identity = set(inventory_header) & set(reverse_header)
    shared_identity.discard("mapping_status")
    shared_identity.discard("semantic_review_status")
    shared_identity.discard("source_authority_ids")
    shared_identity.discard("presentation_packet_ids")
    shared_identity.discard("register_obligation_ids")
    for index, row in enumerate(reverse_rows, start=2):
        unit_id = require_nonempty_string(row["unit_id"], f"handbook-unit reverse row {index}.unit_id")
        if unit_id in reverse_by_id:
            raise ValueError(f"handbook-unit reverse row {index}: duplicate unit ID")
        base = inventory_by_id.get(unit_id)
        if base is None:
            raise ValueError(f"handbook-unit reverse row {index}: unknown unit ID {unit_id}")
        for field in shared_identity:
            if row[field] != base[field]:
                raise ValueError(f"handbook-unit reverse row {index}.{field}: inventory drift")
        labels = _json_string_array(row["stable_labels"], f"handbook-unit reverse row {index}.stable_labels")
        register_ids = _json_string_array(
            row["register_obligation_ids"],
            f"handbook-unit reverse row {index}.register_obligation_ids",
        )
        reverse_by_id[unit_id] = {"row": row, "labels": labels, "register_ids": register_ids}
    if set(reverse_by_id) != set(inventory_by_id):
        missing = len(set(inventory_by_id) - set(reverse_by_id))
        raise ValueError(f"handbook-unit reverse ledger: {missing} inventory units are absent")
    return reverse_by_id


def _load_json(path: Path, location: str) -> Any:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=duplicate_rejecting_object,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateJsonFieldError) as exc:
        raise ValueError(f"{location}: invalid JSON: {exc}") from exc


def load_packets(packet_root: Path) -> dict[str, tuple[Path, dict[str, Any]]]:
    if not packet_root.is_dir():
        return {}
    packets: dict[str, tuple[Path, dict[str, Any]]] = {}
    for path in sorted(item for item in packet_root.rglob("*.json") if item.is_file()):
        packet = _load_json(path, f"presentation packet {path}")
        if not isinstance(packet, dict):
            raise ValueError(f"presentation packet {path}: root must be an object")
        packet_id = require_nonempty_string(packet.get("packet_id"), f"presentation packet {path}.packet_id")
        if packet_id in packets:
            raise ValueError(f"presentation packet corpus: duplicate packet ID {packet_id}")
        packets[packet_id] = (path, packet)
    return packets


def _packet_file_inside_repository(
    raw_path: object,
    packet_path: Path,
    root: Path,
    location: str,
) -> Path:
    value = require_nonempty_string(raw_path, location)
    if "\\" in value:
        raise ValueError(f"{location}: use POSIX path syntax")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        raise ValueError(f"{location}: path traversal and absolute paths are forbidden")
    candidate = (packet_path.parent / Path(*pure.parts)).resolve()
    resolved_root = root.resolve()
    try:
        candidate.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"{location}: packet artifact escapes the repository") from exc
    if not candidate.is_file():
        raise ValueError(f"{location}: packet artifact does not exist")
    return candidate


def _validate_packet_artifact_paths(
    packet: dict[str, Any], packet_path: Path, root: Path, packet_id: str
) -> None:
    candidates: list[tuple[object, str]] = []
    authority = packet.get("authority")
    if isinstance(authority, dict) and "local_path" in authority:
        candidates.append(
            (authority["local_path"], f"presentation packet {packet_id}.authority.local_path")
        )
    content = packet.get("content")
    if isinstance(content, dict):
        for category, items in content.items():
            if not isinstance(items, list):
                continue
            for index, item in enumerate(items):
                if isinstance(item, dict) and "artifact_path" in item:
                    candidates.append(
                        (
                            item["artifact_path"],
                            f"presentation packet {packet_id}.content.{category}[{index}].artifact_path",
                        )
                    )
    evidence = packet.get("verification_evidence")
    if isinstance(evidence, list):
        for index, item in enumerate(evidence):
            if isinstance(item, dict) and "artifact_path" in item:
                candidates.append(
                    (
                        item["artifact_path"],
                        f"presentation packet {packet_id}.verification_evidence[{index}].artifact_path",
                    )
                )
    for raw_path, location in candidates:
        _packet_file_inside_repository(raw_path, packet_path, root, location)


def _validate_verified_packet(
    packet_id: str,
    obligation_id: str,
    packet_path: Path,
    packet: dict[str, Any],
    manifest_path: Path,
    root: Path,
    owners: dict[str, list[Path]],
    packets: dict[str, tuple[Path, dict[str, Any]]],
) -> list[str]:
    if packet.get("overall_status") != "verified":
        raise ValueError(f"presentation packet {packet_id}: packet is not verified")
    try:
        import check_presentation_packet as packet_checker
    except ImportError:  # pragma: no cover - module-style invocation fallback
        from tools import check_presentation_packet as packet_checker  # type: ignore
    previous_register = packet_checker.REGISTER_MANIFEST
    previous_coverage = packet_checker.COVERAGE_MANIFEST
    packet_checker.REGISTER_MANIFEST = manifest_path
    packet_checker.COVERAGE_MANIFEST = root / "spec/full-compendium-coverage-manifest.csv"
    try:
        errors = packet_checker.validate_packet(
            packet,
            base_dir=packet_path.parent,
            packet_path=packet_path,
        )
    finally:
        packet_checker.REGISTER_MANIFEST = previous_register
        packet_checker.COVERAGE_MANIFEST = previous_coverage
    if errors:
        raise ValueError(
            f"presentation packet {packet_id}: structural verification failed: {errors[0]}"
        )
    _validate_packet_artifact_paths(packet, packet_path, root, packet_id)
    variants = packet.get("variants")
    if isinstance(variants, list):
        for index, variant in enumerate(variants):
            related = variant.get("related_packet_id") if isinstance(variant, dict) else None
            if related == packet_id:
                raise ValueError(
                    f"presentation packet {packet_id}.variants[{index}]: cannot refer to itself"
                )
            if isinstance(related, str) and related not in packets:
                raise ValueError(
                    f"presentation packet {packet_id}.variants[{index}]: related packet does not resolve"
                )
    links = packet.get("obligation_links")
    assignments = links.get("register_assignments") if isinstance(links, dict) else None
    matches = [
        item
        for item in assignments or []
        if isinstance(item, dict) and item.get("obligation_id") == obligation_id
    ]
    if len(matches) != 1 or matches[0].get("assignment_status") != "fulfilled":
        raise ValueError(
            f"presentation packet {packet_id}: exact register obligation is not fulfilled"
        )
    destination = packet.get("destination")
    labels = destination.get("stable_labels") if isinstance(destination, dict) else None
    if not isinstance(labels, list) or not labels:
        raise ValueError(f"presentation packet {packet_id}: destination labels are absent")
    assert isinstance(destination, dict)
    _, destination_path = repo_file(
        root,
        destination.get("file"),
        f"presentation packet {packet_id}.destination.file",
        required_prefix="handbook/",
    )
    validated_labels: list[str] = []
    for label in labels:
        validated = require_nonempty_string(
            label, f"presentation packet {packet_id}.destination label"
        )
        occurrences = owners.get(validated, [])
        if occurrences != [destination_path]:
            raise ValueError(
                f"presentation packet {packet_id}: destination label {validated!r} "
                "does not resolve exactly once in its declared destination"
            )
        validated_labels.append(validated)
    return validated_labels


def tex_without_comments(text: str) -> str:
    output: list[str] = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for index, char in enumerate(line):
            if char != "%":
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


def label_owners(root: Path) -> dict[str, list[Path]]:
    owners: dict[str, list[Path]] = {}
    environment_pattern = "|".join(re.escape(item) for item in LABEL_OWNER_ENVIRONMENTS)
    patterns = (
        re.compile(r"\\label\s*\{\s*([^{}]+?)\s*\}"),
        re.compile(r"\\begin\s*\{\s*(?:" + environment_pattern + r")\s*\}\s*\{\s*([^{}]+?)\s*\}"),
        re.compile(r"\\(?:calculussheet|hbrule)\s*\{\s*([^{}]+?)\s*\}"),
    )
    handbook = root / "handbook"
    if not handbook.is_dir():
        raise ValueError("handbook directory is absent")
    for path in sorted(handbook.rglob("*.tex")):
        active = tex_without_comments(path.read_text(encoding="utf-8"))
        for pattern in patterns:
            for match in pattern.finditer(active):
                label = match.group(1).strip()
                owners.setdefault(label, []).append(path.resolve())
    return owners


def _substantive_destination(path: Path, root: Path) -> bool:
    relative = path.relative_to(root.resolve()).as_posix()
    if relative.startswith(("handbook/generated/", "handbook/registry/")):
        return False
    if re.fullmatch(r"handbook/(?:parts|annex)/p[0-9]{2}\.tex", relative):
        return False
    return bool(
        relative.startswith("handbook/frontmatter/")
        or relative.startswith("handbook/restoration/")
        or re.fullmatch(r"handbook/(?:parts|annex)/p[0-9]{2}/.+\.tex", relative)
    )


def _sorted_string_list(
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


def _exact_integer(value: object, location: str, *, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{location}: expected integer >= {minimum}")
    return value


def _canonical_digest(value: object) -> str:
    return sha256_bytes(
        json.dumps(
            value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
    )


def _line_excerpt(path: Path, start: int, end: int, location: str) -> bytes:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise ValueError(f"{location}: cannot read file: {exc}") from exc
    lines = raw.splitlines(keepends=True)
    if start < 1 or end < start or end > len(lines):
        raise ValueError(f"{location}: line locator is outside the pinned file")
    return b"".join(lines[start - 1 : end])


def _same_file_as_any(path: Path, candidates: set[Path], location: str) -> bool:
    try:
        return any(os.path.samefile(path, candidate) for candidate in candidates)
    except OSError as exc:
        raise ValueError(f"{location}: cannot compare filesystem identity: {exc}") from exc


def _validate_contract_supersession(
    untyped: object,
    rows_by_id: dict[str, dict[str, str]],
    root: Path,
    manifest_path: Path,
    reviewed_path: Path,
    unit_inventory_path: Path,
) -> tuple[str, list[dict[str, object]], list[str]]:
    location = "reviewed-record document.contract_supersessions[0]"
    record = require_exact_fields(untyped, CONTRACT_SUPERSESSION_FIELDS, location)
    if record["supersession_id"] != CONTRACT_SUPERSESSION_ID:
        raise ValueError(f"{location}.supersession_id: exact notation-contract record required")
    if record["supersession_statement"] != CONTRACT_SUPERSESSION_STATEMENT:
        raise ValueError(
            f"{location}.supersession_statement: generic waivers are forbidden"
        )

    obligations = record["obligations"]
    if not isinstance(obligations, list) or len(obligations) != len(
        CONTRACT_SUPERSESSION_OBLIGATION_IDS
    ):
        raise ValueError(f"{location}.obligations: exact atomic four-row group required")
    observed_ids: list[str] = []
    source_register_paths: set[Path] = set()
    for index, (untyped_obligation, expected_id) in enumerate(
        zip(obligations, CONTRACT_SUPERSESSION_OBLIGATION_IDS, strict=True)
    ):
        obligation_location = f"{location}.obligations[{index}]"
        obligation = require_exact_fields(
            untyped_obligation, SUPERSESSION_OBLIGATION_FIELDS, obligation_location
        )
        obligation_id = require_nonempty_string(
            obligation["obligation_id"], f"{obligation_location}.obligation_id"
        )
        observed_ids.append(obligation_id)
        if obligation_id == CONTRACT_SUPERSESSION_EXCLUDED_ID:
            raise ValueError(f"{location}.obligations: A-172 is outside this control")
        if obligation_id != expected_id:
            raise ValueError(
                f"{location}.obligations: partial, arbitrary, duplicate, or reordered group"
            )
        base = rows_by_id.get(obligation_id)
        if base is None:
            raise ValueError(f"{obligation_location}: unknown obligation ID")
        expected_identity: dict[str, object] = {
            "source_register": base["source_register"],
            "source_line": int(base["source_line"]),
            "record_sha256": base["record_sha256"],
            "original_record_json_sha256": sha256_bytes(
                base["original_record_json"].encode("utf-8")
            ),
        }
        for field, expected in expected_identity.items():
            if obligation[field] != expected:
                raise ValueError(
                    f"{obligation_location}.{field}: stale immutable row identity"
                )
        original = json.loads(base["original_record_json"])
        superseded = obligation["superseded_fields"]
        expected_fields = SUPERSEDED_FIELDS_BY_OBLIGATION[obligation_id]
        if not isinstance(superseded, list) or len(superseded) != len(expected_fields):
            raise ValueError(
                f"{obligation_location}.superseded_fields: exact field set required"
            )
        for field_index, (untyped_field, expected_field) in enumerate(
            zip(superseded, expected_fields, strict=True)
        ):
            field_location = (
                f"{obligation_location}.superseded_fields[{field_index}]"
            )
            field = require_exact_fields(
                untyped_field, SUPERSEDED_FIELD_FIELDS, field_location
            )
            if field["field_name"] != expected_field:
                raise ValueError(f"{field_location}.field_name: wrong superseded field")
            original_value = original.get(expected_field)
            if not isinstance(original_value, str):
                raise ValueError(f"{field_location}: original field is not a string")
            if field["original_value"] != original_value:
                raise ValueError(f"{field_location}.original_value: historical value drift")
            if field["original_value_sha256"] != sha256_bytes(
                original_value.encode("utf-8")
            ):
                raise ValueError(
                    f"{field_location}.original_value_sha256: historical hash drift"
                )
        _, source_register = repo_file(
            root,
            base["source_register"],
            f"{obligation_location}.source_register",
            required_prefix="spec/registers/",
        )
        source_register_paths.add(source_register)
    if len(set(observed_ids)) != len(observed_ids):
        raise ValueError(f"{location}.obligations: duplicate obligation ID")

    clauses = record["binding_contract_clauses"]
    if not isinstance(clauses, list) or len(clauses) != len(CONTRACT_CLAUSE_SPECS):
        raise ValueError(
            f"{location}.binding_contract_clauses: exact binding clause set required"
        )
    clause_paths: set[Path] = set()
    required_locator_strings: list[str] = []
    for index, (untyped_clause, spec) in enumerate(
        zip(clauses, CONTRACT_CLAUSE_SPECS, strict=True)
    ):
        clause_location = f"{location}.binding_contract_clauses[{index}]"
        clause = require_exact_fields(untyped_clause, CLAUSE_FIELDS, clause_location)
        expected_path, expected_start, expected_end, required_tokens = spec
        if (
            clause["path"] != expected_path
            or clause["start_line"] != expected_start
            or clause["end_line"] != expected_end
        ):
            raise ValueError(f"{clause_location}: wrong binding contract clause")
        _value, path = repo_file(root, clause["path"], f"{clause_location}.path")
        clause_paths.add(path)
        raw_hash = sha256_file(path)
        if clause["sha256"] != raw_hash:
            raise ValueError(f"{clause_location}.sha256: binding contract drift")
        excerpt = _line_excerpt(path, expected_start, expected_end, clause_location)
        if clause["excerpt_sha256"] != sha256_bytes(excerpt):
            raise ValueError(f"{clause_location}.excerpt_sha256: contract clause drift")
        text = excerpt.decode("utf-8")
        if any(token not in text for token in required_tokens):
            raise ValueError(f"{clause_location}: binding contract token drift")
        required_locator_strings.append(
            f"{expected_path}:{expected_start}-{expected_end}"
        )

    source_value, source_path = repo_file(
        root,
        "source/formal-logic-reference.tex",
        f"{location}.current_source_locators.source_path",
    )
    source_hash = sha256_file(source_path)
    current_locators = record["current_source_locators"]
    if not isinstance(current_locators, list) or len(current_locators) != len(
        CURRENT_SOURCE_LOCATOR_SPECS
    ):
        raise ValueError(
            f"{location}.current_source_locators: exact current locator set required"
        )
    for index, (untyped_locator, spec) in enumerate(
        zip(current_locators, CURRENT_SOURCE_LOCATOR_SPECS, strict=True)
    ):
        locator_location = f"{location}.current_source_locators[{index}]"
        locator = require_exact_fields(
            untyped_locator, CURRENT_LOCATOR_FIELDS, locator_location
        )
        obligation_id, start, end, tokens = spec
        expected = {
            "obligation_id": obligation_id,
            "revision": "v1.1-verified",
            "source_path": source_value,
            "source_sha256": source_hash,
            "start_line": start,
            "end_line": end,
            "required_tokens": list(tokens),
        }
        for field, expected_value in expected.items():
            if locator[field] != expected_value:
                raise ValueError(
                    f"{locator_location}.{field}: mixed or stale source coordinate"
                )
        excerpt = _line_excerpt(source_path, start, end, locator_location)
        if locator["excerpt_sha256"] != sha256_bytes(excerpt):
            raise ValueError(f"{locator_location}.excerpt_sha256: source token drift")
        text = excerpt.decode("utf-8")
        if any(token not in text for token in tokens):
            raise ValueError(f"{locator_location}: required source token changed")
        required_locator_strings.append(
            f"source/formal-logic-reference.tex:{start}-{end}@v1.1-verified"
        )

    pairs = record["revision_locator_pairs"]
    if not isinstance(pairs, list) or len(pairs) != len(REVISION_LOCATOR_PAIR_SPECS):
        raise ValueError(f"{location}.revision_locator_pairs: exact pair set required")
    for index, (untyped_pair, spec) in enumerate(
        zip(pairs, REVISION_LOCATOR_PAIR_SPECS, strict=True)
    ):
        pair_location = f"{location}.revision_locator_pairs[{index}]"
        pair = require_exact_fields(untyped_pair, REVISION_PAIR_FIELDS, pair_location)
        obligation_id, old_start, old_end, old_excerpt, new_start, new_end = spec
        expected = {
            "obligation_id": obligation_id,
            "historical_revision": "v1.0-audit",
            "historical_source_sha256": HISTORICAL_SOURCE_SHA256,
            "historical_start_line": old_start,
            "historical_end_line": old_end,
            "historical_excerpt_sha256": old_excerpt,
            "current_revision": "v1.1-verified",
            "current_source_path": source_value,
            "current_source_sha256": source_hash,
            "current_start_line": new_start,
            "current_end_line": new_end,
        }
        for field, expected_value in expected.items():
            if pair[field] != expected_value:
                raise ValueError(
                    f"{pair_location}.{field}: mixed coordinate revisions are forbidden"
                )
        current_excerpt = _line_excerpt(
            source_path, new_start, new_end, pair_location
        )
        if pair["current_excerpt_sha256"] != sha256_bytes(current_excerpt):
            raise ValueError(f"{pair_location}.current_excerpt_sha256: locator drift")
        required_locator_strings.append(
            f"v1.0-audit:{old_start}-{old_end}->v1.1-verified:{new_start}-{new_end}"
        )

    provenance = record["affected_provenance_records"]
    if not isinstance(provenance, list) or len(provenance) != len(
        PROVENANCE_INTERVAL_SPECS
    ):
        raise ValueError(
            f"{location}.affected_provenance_records: exact provenance set required"
        )
    provenance_paths: set[Path] = set()
    restoration_paths: set[Path] = set()
    provenance_runtime: dict[str, tuple[int, int, str, Path]] = {}
    for index, (untyped_identity, spec) in enumerate(
        zip(provenance, PROVENANCE_INTERVAL_SPECS, strict=True)
    ):
        identity_location = f"{location}.affected_provenance_records[{index}]"
        identity = require_exact_fields(
            untyped_identity, PROVENANCE_IDENTITY_FIELDS, identity_location
        )
        provenance_id, start, end = spec
        expected_path = f"spec/provenance/{provenance_id}.json"
        if (
            identity["provenance_id"] != provenance_id
            or identity["path"] != expected_path
            or identity["source_start"] != start
            or identity["source_end"] != end
        ):
            raise ValueError(f"{identity_location}: wrong affected provenance identity")
        _value, path = repo_file(root, identity["path"], f"{identity_location}.path")
        provenance_paths.add(path)
        if identity["sha256"] != sha256_file(path):
            raise ValueError(f"{identity_location}.sha256: provenance record drift")
        document = _load_json(path, f"affected provenance {provenance_id}")
        if not isinstance(document, dict) or document.get("provenance_id") != provenance_id:
            raise ValueError(f"{identity_location}: provenance ID drift")
        source_locator = document.get("source_locator")
        artifact = document.get("restoration_artifact")
        if not isinstance(source_locator, dict) or not isinstance(artifact, dict):
            raise ValueError(f"{identity_location}: provenance identity fields missing")
        source_excerpt = _line_excerpt(source_path, start, end, identity_location)
        interval_hash = sha256_bytes(source_excerpt)
        if (
            source_locator.get("start_line") != start
            or source_locator.get("end_line") != end
            or source_locator.get("line_count") != end - start + 1
            or source_locator.get("interval_sha256") != interval_hash
            or identity["interval_sha256"] != interval_hash
        ):
            raise ValueError(f"{identity_location}: provenance source locator drift")
        expected_artifact = f"handbook/restoration/inherited-{start:05d}-{end:05d}.tex"
        if (
            artifact.get("path") != expected_artifact
            or identity["restoration_artifact_path"] != expected_artifact
        ):
            raise ValueError(f"{identity_location}: restoration artifact path drift")
        _artifact_value, artifact_path = repo_file(
            root, expected_artifact, f"{identity_location}.restoration_artifact_path"
        )
        restoration_paths.add(artifact_path)
        artifact_hash = sha256_file(artifact_path)
        if (
            artifact.get("sha256") != artifact_hash
            or identity["restoration_artifact_sha256"] != artifact_hash
            or artifact_path.read_bytes() != source_excerpt
        ):
            raise ValueError(
                f"{identity_location}: source-token or restoration rendering drift"
            )
        provenance_runtime[provenance_id] = (
            start,
            end,
            expected_artifact,
            artifact_path,
        )

    inventory_header, inventory_rows = _read_csv(
        unit_inventory_path, "handbook-unit inventory"
    )
    unit_identity_names = (
        "unit_id",
        "record_type",
        "path",
        "start_line",
        "end_line",
        "bytes",
        "sha256",
        "unit_kind",
    )
    if not set(unit_identity_names).issubset(inventory_header):
        raise ValueError(f"{location}.affected_handbook_units: inventory fields missing")
    inventory_by_id: dict[str, dict[str, str]] = {}
    for index, row in enumerate(inventory_rows, start=2):
        unit_id = require_nonempty_string(
            row["unit_id"], f"handbook-unit inventory row {index}.unit_id"
        )
        if unit_id in inventory_by_id:
            raise ValueError("handbook-unit inventory: duplicate unit ID")
        inventory_by_id[unit_id] = row
    expected_units: dict[str, dict[str, object]] = {}
    for provenance_id, affected_start, affected_end in AFFECTED_SOURCE_RANGES:
        interval_start, _interval_end, artifact_value, artifact_path = provenance_runtime[
            provenance_id
        ]
        local_start = affected_start - interval_start + 1
        local_end = affected_end - interval_start + 1
        matches = []
        for row in inventory_rows:
            if row["path"] != artifact_value:
                continue
            try:
                row_start = int(row["start_line"])
                row_end = int(row["end_line"])
            except ValueError as exc:
                raise ValueError("handbook-unit inventory: invalid unit bounds") from exc
            if row_start <= local_end and row_end >= local_start:
                matches.append(row)
        if not matches:
            raise ValueError(
                f"{location}.affected_handbook_units: source locator lacks a unit identity"
            )
        for row in matches:
            identity_strings = {name: row[name] for name in unit_identity_names}
            start = int(row["start_line"])
            end = int(row["end_line"])
            unit_excerpt = _line_excerpt(
                artifact_path, start, end, "affected handbook unit"
            )
            if (
                int(row["bytes"]) != len(unit_excerpt)
                or row["sha256"] != sha256_bytes(unit_excerpt)
            ):
                raise ValueError(
                    f"{location}.affected_handbook_units: inventory unit bytes drift"
                )
            expected_units[row["unit_id"]] = {
                **{
                    name: (
                        int(row[name])
                        if name in {"start_line", "end_line", "bytes"}
                        else row[name]
                    )
                    for name in unit_identity_names
                },
                "identity_sha256": _canonical_digest(identity_strings),
            }
    units = record["affected_handbook_units"]
    if not isinstance(units, list) or not units:
        raise ValueError(f"{location}.affected_handbook_units: exact nonempty set required")
    observed_units: list[dict[str, object]] = []
    for index, untyped_unit in enumerate(units):
        unit_location = f"{location}.affected_handbook_units[{index}]"
        unit = require_exact_fields(untyped_unit, UNIT_IDENTITY_FIELDS, unit_location)
        observed_units.append(unit)
    expected_unit_list = [expected_units[key] for key in sorted(expected_units)]
    if observed_units != expected_unit_list:
        raise ValueError(f"{location}.affected_handbook_units: stale or incomplete unit set")

    roles = record["surviving_scoped_roles"]
    if not isinstance(roles, list):
        raise ValueError(f"{location}.surviving_scoped_roles: expected array")
    for index, role in enumerate(roles):
        require_exact_fields(role, SCOPED_ROLE_FIELDS, f"{location}.surviving_scoped_roles[{index}]")
    if roles != list(SURVIVING_SCOPED_ROLES):
        raise ValueError(f"{location}.surviving_scoped_roles: exact scoped roles required")

    controls = record["preservation_controls"]
    if not isinstance(controls, list) or len(controls) != len(PRESERVATION_CONTROL_SPECS):
        raise ValueError(f"{location}.preservation_controls: exact control set required")
    preservation_paths: set[Path] = set()
    for index, (untyped_control, spec) in enumerate(
        zip(controls, PRESERVATION_CONTROL_SPECS, strict=True)
    ):
        control_location = f"{location}.preservation_controls[{index}]"
        control = require_exact_fields(
            untyped_control, PRESERVATION_CONTROL_FIELDS, control_location
        )
        expected_path, expected_tokens = spec
        if control["path"] != expected_path or control["required_tokens"] != list(
            expected_tokens
        ):
            raise ValueError(f"{control_location}: preservation control drift")
        _value, path = repo_file(root, control["path"], f"{control_location}.path")
        preservation_paths.add(path)
        if control["sha256"] != sha256_file(path):
            raise ValueError(f"{control_location}.sha256: preservation control drift")
        text = path.read_text(encoding="utf-8")
        if any(token not in text for token in expected_tokens):
            raise ValueError(f"{control_location}: source-token/rendering check changed")

    rendered = require_exact_fields(
        record["rendered_artifact"], RENDERED_ARTIFACT_FIELDS, f"{location}.rendered_artifact"
    )
    if rendered["path"] != "handbook/main.pdf":
        raise ValueError(f"{location}.rendered_artifact.path: exact public PDF required")
    _rendered_value, rendered_path = repo_file(
        root, rendered["path"], f"{location}.rendered_artifact.path"
    )
    rendered_bytes = rendered_path.read_bytes()
    if (
        rendered["sha256"] != sha256_bytes(rendered_bytes)
        or rendered["bytes"] != len(rendered_bytes)
    ):
        raise ValueError(f"{location}.rendered_artifact: rendering changed")

    verification = require_exact_fields(
        record["verification"], set(VERIFICATION_FIELDS), f"{location}.verification"
    )
    if any(verification[category] != "pass" for category in VERIFICATION_FIELDS):
        raise ValueError(f"{location}.verification: all six categories must pass")
    evidence = record["verification_evidence"]
    if not isinstance(evidence, list) or len(evidence) != len(VERIFICATION_FIELDS):
        raise ValueError(f"{location}.verification_evidence: exactly six records required")

    required_authority_paths = (
        clause_paths
        | {source_path, manifest_path.resolve(), unit_inventory_path.resolve()}
        | provenance_paths
        | preservation_paths
        | source_register_paths
    )
    required_authorities = sorted(
        (
            {
                "path": path.relative_to(root.resolve()).as_posix(),
                "sha256": sha256_file(path),
            }
            for path in required_authority_paths
        ),
        key=lambda item: item["path"],
    )
    required_locator_strings.extend(
        f"{rows_by_id[obligation_id]['source_register']}:"
        f"{rows_by_id[obligation_id]['source_line']}"
        for obligation_id in CONTRACT_SUPERSESSION_OBLIGATION_IDS
    )
    required_locators = sorted(required_locator_strings)
    forbidden_paths = (
        required_authority_paths
        | restoration_paths
        | {reviewed_path.resolve(), rendered_path}
    )
    forbidden_hashes = {sha256_file(path) for path in forbidden_paths}
    evidence_paths: set[Path] = set()
    evidence_hashes: set[str] = set()
    producer_keys: set[str] = set()
    normalized_evidence: list[dict[str, object]] = []
    for index, (untyped_evidence, expected_category) in enumerate(
        zip(evidence, VERIFICATION_FIELDS, strict=True)
    ):
        evidence_location = f"{location}.verification_evidence[{index}]"
        raw_category = (
            untyped_evidence.get("category")
            if isinstance(untyped_evidence, dict)
            else None
        )
        fields = (
            AI_EVIDENCE_FIELDS
            if raw_category in AI_VERIFICATION_FIELDS
            else MECHANICAL_EVIDENCE_FIELDS
        )
        item = require_exact_fields(untyped_evidence, fields, evidence_location)
        if item["category"] != expected_category or item["recorded_result"] != "pass":
            raise ValueError(f"{evidence_location}: exact passing category order required")
        artifact_value, artifact_path = repo_file(
            root, item["artifact_path"], f"{evidence_location}.artifact_path"
        )
        if artifact_path in evidence_paths or _same_file_as_any(
            artifact_path, evidence_paths, evidence_location
        ):
            raise ValueError(f"{evidence_location}: reused evidence file")
        if artifact_path in forbidden_paths or _same_file_as_any(
            artifact_path, forbidden_paths, evidence_location
        ):
            raise ValueError(f"{evidence_location}: self evidence is forbidden")
        evidence_paths.add(artifact_path)
        evidence_hash = require_sha256(item["sha256"], f"{evidence_location}.sha256")
        if sha256_file(artifact_path) != evidence_hash:
            raise ValueError(f"{evidence_location}.sha256: evidence digest drift")
        if evidence_hash in evidence_hashes or evidence_hash in forbidden_hashes:
            raise ValueError(f"{evidence_location}.sha256: reused or copied evidence")
        evidence_hashes.add(evidence_hash)
        producer = require_nonempty_string(
            item["producer_identity"], f"{evidence_location}.producer_identity"
        )
        producer_key = _producer_key(producer)
        if producer_key in producer_keys:
            raise ValueError(f"{evidence_location}.producer_identity: distinct producer required")
        producer_keys.add(producer_key)
        scope = require_nonempty_string(
            item["recorded_scope"], f"{evidence_location}.recorded_scope"
        )
        if scope != CONTRACT_SUPERSESSION_EVIDENCE_SCOPE:
            raise ValueError(f"{evidence_location}.recorded_scope: exact atomic scope required")
        normalized_item: dict[str, object] = {
            "category": expected_category,
            "recorded_result": "pass",
            "artifact_path": artifact_value,
            "sha256": evidence_hash,
            "producer_identity": producer,
            "recorded_scope": scope,
        }
        if expected_category in AI_VERIFICATION_FIELDS:
            for string_field in ("model", "model_version", "instructions"):
                normalized_item[string_field] = require_nonempty_string(
                    item[string_field], f"{evidence_location}.{string_field}"
                )
            authorities = item["consulted_authority_files"]
            if not isinstance(authorities, list):
                raise ValueError(f"{evidence_location}.consulted_authority_files: expected array")
            normalized_authorities: list[dict[str, str]] = []
            for authority_index, untyped_authority in enumerate(authorities):
                authority_location = f"{evidence_location}.consulted_authority_files[{authority_index}]"
                authority = require_exact_fields(
                    untyped_authority, {"path", "sha256"}, authority_location
                )
                authority_value, authority_path = repo_file(
                    root, authority["path"], f"{authority_location}.path"
                )
                authority_hash = require_sha256(
                    authority["sha256"], f"{authority_location}.sha256"
                )
                if sha256_file(authority_path) != authority_hash:
                    raise ValueError(f"{authority_location}.sha256: authority drift")
                normalized_authorities.append(
                    {"path": authority_value, "sha256": authority_hash}
                )
            if normalized_authorities != required_authorities:
                raise ValueError(
                    f"{evidence_location}.consulted_authority_files: exact governed authorities required"
                )
            locators = _sorted_string_list(
                item["consulted_authority_locators"],
                f"{evidence_location}.consulted_authority_locators",
                require_nonempty=True,
            )
            if locators != required_locators:
                raise ValueError(
                    f"{evidence_location}.consulted_authority_locators: exact revision-qualified locators required"
                )
            findings = _sorted_string_list(
                item["findings"], f"{evidence_location}.findings", require_nonempty=True
            )
            evidence_digest = require_sha256(
                item["evidence_digest"], f"{evidence_location}.evidence_digest"
            )
            if evidence_digest != evidence_hash:
                raise ValueError(f"{evidence_location}.evidence_digest: evidence hash required")
            normalized_item.update(
                {
                    "consulted_authority_files": normalized_authorities,
                    "consulted_authority_locators": locators,
                    "findings": findings,
                    "evidence_digest": evidence_digest,
                }
            )
        normalized_evidence.append(normalized_item)
    return _canonical_digest(record), normalized_evidence, sorted(expected_units)


def apply_reviewed_records(
    rows: list[dict[str, str]],
    reviewed_path: Path,
    manifest_path: Path,
    root: Path,
    unit_inventory_path: Path = DEFAULT_UNIT_INVENTORY,
    unit_reverse_path: Path = DEFAULT_UNIT_REVERSE,
    packet_root: Path = DEFAULT_PACKET_ROOT,
) -> list[dict[str, str]]:
    document = _load_json(reviewed_path, "reviewed register-obligation records")
    document = require_exact_fields(
        document,
        {
            "schema_version",
            "register_manifest_path",
            "register_manifest_sha256",
            "records",
            "contract_supersessions",
        },
        "reviewed-record document",
    )
    if type(document["schema_version"]) is not int or document["schema_version"] != SCHEMA_VERSION:
        raise ValueError(f"reviewed-record document.schema_version: must be {SCHEMA_VERSION}")
    if document["register_manifest_path"] != MANIFEST_PATH:
        raise ValueError(f"reviewed-record document.register_manifest_path: must be {MANIFEST_PATH!r}")
    manifest_hash = require_sha256(
        document["register_manifest_sha256"],
        "reviewed-record document.register_manifest_sha256",
    )
    if manifest_hash != sha256_file(manifest_path):
        raise ValueError("reviewed-record document: register manifest SHA-256 drift")
    records = document["records"]
    if not isinstance(records, list):
        raise ValueError("reviewed-record document.records: expected array")
    contract_supersessions = document["contract_supersessions"]
    if not isinstance(contract_supersessions, list):
        raise ValueError(
            "reviewed-record document.contract_supersessions: expected array"
        )
    output: list[dict[str, str]] = []
    for row in rows:
        output.append(
            {
                "obligation_id": row["obligation_id"],
                "source_register": row["source_register"],
                "source_line": row["source_line"],
                "record_sha256": row["record_sha256"],
                "manifest_binding_disposition": row["binding_disposition"],
                "completion_status": "OPEN",
                "contract_supersession_id": "",
                "contract_supersession_record_sha256": "",
                "handbook_unit_ids": "[]",
                "presentation_packet_ids": "[]",
                "destination_labels": "[]",
                "fulfillment_description": "",
                "source_fidelity_ai_verification": "pending",
                "topic_specialist_ai_verification": "pending",
                "adversarial_publication_ai_verification": "pending",
                "static_verification": "pending",
                "build_verification": "pending",
                "visual_verification": "pending",
                "verification_evidence": "[]",
            }
        )
    by_id = {row["obligation_id"]: row for row in rows}
    output_by_id = {row["obligation_id"]: row for row in output}

    for index, untyped_record in enumerate(records):
        if not isinstance(untyped_record, dict):
            continue
        ordinary_id = untyped_record.get("obligation_id")
        if ordinary_id not in CONTRACT_SUPERSESSION_OBLIGATION_IDS:
            continue
        if contract_supersessions:
            raise ValueError(
                "reviewed-record document: ordinary completion and contract "
                f"supersession overlap at records[{index}]"
            )
        raise ValueError(
            "reviewed-record document: ordinary completion is forbidden for "
            f"the atomic notation-contract row {ordinary_id}"
        )

    if len(contract_supersessions) > 1:
        raise ValueError(
            "reviewed-record document.contract_supersessions: duplicate atomic record"
        )
    if contract_supersessions:
        supersession_digest, supersession_evidence, affected_unit_ids = (
            _validate_contract_supersession(
                contract_supersessions[0],
                by_id,
                root,
                manifest_path,
                reviewed_path,
                unit_inventory_path,
            )
        )
        evidence_json = json.dumps(
            supersession_evidence, ensure_ascii=False, separators=(",", ":")
        )
        unit_ids_json = json.dumps(affected_unit_ids, separators=(",", ":"))
        for obligation_id in CONTRACT_SUPERSESSION_OBLIGATION_IDS:
            projected = output_by_id[obligation_id]
            projected.update(
                {
                    "completion_status": "SUPERSEDED_BY_CONTRACT",
                    "contract_supersession_id": CONTRACT_SUPERSESSION_ID,
                    "contract_supersession_record_sha256": supersession_digest,
                    "handbook_unit_ids": unit_ids_json,
                    "fulfillment_description": CONTRACT_SUPERSESSION_STATEMENT,
                    "source_fidelity_ai_verification": "pass",
                    "topic_specialist_ai_verification": "pass",
                    "adversarial_publication_ai_verification": "pass",
                    "static_verification": "pass",
                    "build_verification": "pass",
                    "visual_verification": "pass",
                    "verification_evidence": evidence_json,
                }
            )

    if not records:
        return output

    units = load_admitted_units(unit_inventory_path, unit_reverse_path)
    packets = load_packets(packet_root)
    owners = label_owners(root)
    seen_ids: set[str] = set()

    for index, untyped in enumerate(records):
        location = f"reviewed-record document.records[{index}]"
        record = require_exact_fields(untyped, RECORD_FIELDS, location)
        obligation_id = require_nonempty_string(record["obligation_id"], f"{location}.obligation_id")
        if obligation_id in seen_ids:
            raise ValueError(f"{location}: duplicate obligation ID {obligation_id}")
        seen_ids.add(obligation_id)
        base = by_id.get(obligation_id)
        if base is None:
            raise ValueError(f"{location}: unknown obligation ID {obligation_id}")
        if isinstance(record["source_line"], bool) or not isinstance(record["source_line"], int):
            raise ValueError(f"{location}.source_line: expected integer")
        exact_identity: dict[str, object] = {
            "source_register": base["source_register"],
            "source_line": int(base["source_line"]),
            "record_sha256": base["record_sha256"],
        }
        for field, expected in exact_identity.items():
            if record[field] != expected:
                raise ValueError(f"{location}.{field}: stale or mismatched register identity")
        if record["completion_status"] != "complete":
            raise ValueError(f"{location}.completion_status: terminal record must be 'complete'")

        unit_ids = _sorted_string_list(record["handbook_unit_ids"], f"{location}.handbook_unit_ids", pattern=UNIT_ID_RE)
        packet_ids = _sorted_string_list(record["presentation_packet_ids"], f"{location}.presentation_packet_ids")
        if not unit_ids and not packet_ids:
            raise ValueError(f"{location}: completion requires a handbook unit or presentation packet")
        labels = _sorted_string_list(
            record["destination_labels"],
            f"{location}.destination_labels",
            pattern=LABEL_RE,
            require_nonempty=True,
        )
        description = require_nonempty_string(record["fulfillment_description"], f"{location}.fulfillment_description")

        expected_labels: set[str] = set()
        for unit_id in unit_ids:
            unit = units.get(unit_id)
            if unit is None:
                raise ValueError(f"{location}.handbook_unit_ids: unknown unit ID {unit_id}")
            unit_row = unit["row"]
            if unit_row["mapping_status"] != "mapped/reviewed":
                raise ValueError(f"{location}.handbook_unit_ids: unit {unit_id} is unadmitted")
            if unit_row["semantic_review_status"] not in {"pass", "not-applicable"}:
                raise ValueError(f"{location}.handbook_unit_ids: unit {unit_id} lacks semantic review")
            if obligation_id not in unit["register_ids"]:
                raise ValueError(f"{location}.handbook_unit_ids: unit {unit_id} does not link this obligation")
            if not unit["labels"]:
                raise ValueError(f"{location}.handbook_unit_ids: unit {unit_id} has no stable label")
            expected_labels.update(unit["labels"])

        linked_packet_paths: set[Path] = set()
        for packet_id in packet_ids:
            packet_entry = packets.get(packet_id)
            if packet_entry is None:
                raise ValueError(f"{location}.presentation_packet_ids: unknown packet ID {packet_id}")
            packet_path, packet = packet_entry
            linked_packet_paths.add(packet_path.resolve())
            expected_labels.update(
                _validate_verified_packet(
                    packet_id,
                    obligation_id,
                    packet_path,
                    packet,
                    manifest_path,
                    root,
                    owners,
                    packets,
                )
            )
        if labels != sorted(expected_labels):
            raise ValueError(
                f"{location}.destination_labels: must exactly equal linked support labels {sorted(expected_labels)!r}"
            )

        destination_paths: set[Path] = set()
        for label in labels:
            occurrences = owners.get(label, [])
            if len(occurrences) != 1:
                raise ValueError(f"{location}.destination_labels: label {label!r} occurs {len(occurrences)} times")
            owner = occurrences[0]
            if not _substantive_destination(owner, root):
                raise ValueError(f"{location}.destination_labels: label {label!r} is not in maintained content")
            destination_paths.add(owner)

        verification = require_exact_fields(record["verification"], set(VERIFICATION_FIELDS), f"{location}.verification")
        for category in VERIFICATION_FIELDS:
            if verification[category] != "pass":
                raise ValueError(f"{location}.verification.{category}: completion requires pass")
        evidence = record["verification_evidence"]
        if not isinstance(evidence, list) or len(evidence) != len(VERIFICATION_FIELDS):
            raise ValueError(f"{location}.verification_evidence: exactly six records are required")
        categories: set[str] = set()
        artifact_paths: set[Path] = set()
        artifact_hashes: set[str] = set()
        producer_keys: set[str] = set()
        source_path = (
            root / Path(*PurePosixPath(base["source_register"]).parts)
        ).resolve()
        forbidden_paths = {
            manifest_path.resolve(),
            reviewed_path.resolve(),
            source_path,
            unit_inventory_path.resolve(),
            unit_reverse_path.resolve(),
        } | linked_packet_paths | destination_paths
        normalized_evidence: list[dict[str, object]] = []
        for evidence_index, untyped_evidence in enumerate(evidence):
            evidence_location = f"{location}.verification_evidence[{evidence_index}]"
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
            category = require_nonempty_string(item["category"], f"{evidence_location}.category")
            if category not in VERIFICATION_FIELDS:
                raise ValueError(f"{evidence_location}.category: unknown category")
            if category in categories:
                raise ValueError(f"{evidence_location}.category: duplicate evidence category")
            categories.add(category)
            if item["recorded_result"] != "pass":
                raise ValueError(f"{evidence_location}.recorded_result: completion requires pass")
            artifact_value, artifact_path = repo_file(root, item["artifact_path"], f"{evidence_location}.artifact_path")
            if artifact_path in artifact_paths:
                raise ValueError(f"{evidence_location}.artifact_path: separate evidence files are required")
            artifact_paths.add(artifact_path)
            if artifact_path in forbidden_paths:
                raise ValueError(f"{evidence_location}.artifact_path: input, support, destination, or source cannot be its own evidence artifact")
            evidence_hash = require_sha256(item["sha256"], f"{evidence_location}.sha256")
            if sha256_file(artifact_path) != evidence_hash:
                raise ValueError(f"{evidence_location}.sha256: evidence SHA-256 drift")
            if evidence_hash in artifact_hashes:
                raise ValueError(
                    f"{evidence_location}.sha256: independently recorded evidence "
                    "must not reuse identical artifact bytes"
                )
            artifact_hashes.add(evidence_hash)
            producer = require_nonempty_string(item["producer_identity"], f"{evidence_location}.producer_identity")
            producer_key = _producer_key(producer)
            if producer_key in producer_keys:
                raise ValueError(f"{evidence_location}.producer_identity: every category requires a distinct recorded producer")
            producer_keys.add(producer_key)
            scope = require_nonempty_string(item["recorded_scope"], f"{evidence_location}.recorded_scope")
            if obligation_id not in scope:
                raise ValueError(f"{evidence_location}.recorded_scope: exact obligation ID is required")
            normalized_item: dict[str, object] = {
                "category": category,
                "recorded_result": "pass",
                "artifact_path": artifact_value,
                "sha256": evidence_hash,
                "producer_identity": producer,
                "recorded_scope": scope,
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
                authority_files = item["consulted_authority_files"]
                if not isinstance(authority_files, list) or not authority_files:
                    raise ValueError(
                        f"{evidence_location}.consulted_authority_files: "
                        "expected nonempty array"
                    )
                normalized_authority_files: list[dict[str, str]] = []
                seen_authority_paths: set[Path] = set()
                for authority_index, untyped_authority in enumerate(authority_files):
                    authority_location = (
                        f"{evidence_location}.consulted_authority_files"
                        f"[{authority_index}]"
                    )
                    authority = require_exact_fields(
                        untyped_authority, {"path", "sha256"}, authority_location
                    )
                    authority_value, authority_path = repo_file(
                        root, authority["path"], f"{authority_location}.path"
                    )
                    if authority_path in seen_authority_paths:
                        raise ValueError(
                            f"{evidence_location}.consulted_authority_files: "
                            "duplicate path"
                        )
                    seen_authority_paths.add(authority_path)
                    authority_hash = require_sha256(
                        authority["sha256"], f"{authority_location}.sha256"
                    )
                    if sha256_file(authority_path) != authority_hash:
                        raise ValueError(f"{authority_location}.sha256: digest drift")
                    normalized_authority_files.append(
                        {"path": authority_value, "sha256": authority_hash}
                    )
                if normalized_authority_files != sorted(
                    normalized_authority_files, key=lambda value: value["path"]
                ):
                    raise ValueError(
                        f"{evidence_location}.consulted_authority_files: "
                        "values must be sorted by path"
                    )
                authority_locators = _sorted_string_list(
                    item["consulted_authority_locators"],
                    f"{evidence_location}.consulted_authority_locators",
                    require_nonempty=True,
                )
                findings = _sorted_string_list(
                    item["findings"],
                    f"{evidence_location}.findings",
                    require_nonempty=True,
                )
                evidence_digest = require_sha256(
                    item["evidence_digest"], f"{evidence_location}.evidence_digest"
                )
                if evidence_digest != evidence_hash:
                    raise ValueError(
                        f"{evidence_location}.evidence_digest: must equal the "
                        "review evidence artifact digest"
                    )
                normalized_item.update(
                    {
                        "model": model,
                        "model_version": model_version,
                        "instructions": instructions,
                        "consulted_authority_files": normalized_authority_files,
                        "consulted_authority_locators": authority_locators,
                        "findings": findings,
                        "evidence_digest": evidence_digest,
                    }
                )
            normalized_evidence.append(normalized_item)
        if categories != set(VERIFICATION_FIELDS):
            raise ValueError(f"{location}.verification_evidence: every verification category is required")

        projected = output_by_id[obligation_id]
        projected.update(
            {
                "completion_status": "COMPLETE",
                "handbook_unit_ids": json.dumps(unit_ids, separators=(",", ":")),
                "presentation_packet_ids": json.dumps(packet_ids, separators=(",", ":")),
                "destination_labels": json.dumps(labels, separators=(",", ":")),
                "fulfillment_description": description,
                "source_fidelity_ai_verification": "pass",
                "topic_specialist_ai_verification": "pass",
                "adversarial_publication_ai_verification": "pass",
                "static_verification": "pass",
                "build_verification": "pass",
                "visual_verification": "pass",
                "verification_evidence": json.dumps(normalized_evidence, ensure_ascii=False, separators=(",", ":")),
            }
        )
    return output


def csv_bytes(rows: list[dict[str, str]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=OUTPUT_FIELDS, lineterminator="\n", extrasaction="raise")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def _md_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def markdown_bytes(rows: list[dict[str, str]]) -> bytes:
    complete = sum(row["completion_status"] == "COMPLETE" for row in rows)
    superseded = sum(
        row["completion_status"] == "SUPERSEDED_BY_CONTRACT" for row in rows
    )
    open_count = len(rows) - complete - superseded
    lines = [
        "# Register-obligation closure",
        "",
        "Generated by `tools/build_register_obligation_closure.py`; do not edit by hand.",
        "The immutable register manifest remains unchanged. Historical register status",
        "fields do not close an obligation.",
        "",
        "- Manifest rows: {}".format(len(rows)),
        "- COMPLETE after reviewed admission: {}".format(complete),
        "- SUPERSEDED_BY_CONTRACT after atomic contract review: {}".format(superseded),
        "- OPEN: {}".format(open_count),
        "",
        "## Why this separate administrative record exists",
        "",
        "- **Necessity:** the immutable manifest preserves owed register rows but cannot",
        "  record later reviewed fulfillment without overwriting source evidence.",
        "- **Definition:** a row is COMPLETE exactly when its reviewer record pins the",
        "  manifest identity, links admitted handbook units and/or verified presentation",
        "  packets, resolves the exact destination labels, describes fulfillment, and",
        "  supplies passing source-fidelity AI, topic-specialist AI, adversarial-publication AI,",
        "  static, build, and visual evidence.",
        "- **Standing:** this is a metalinguistic administrative projection, not a motive,",
        "  relation among motives, statement family, or handbook doctrine.",
        "- **Nonredundancy:** the manifest preserves register bytes; the handbook-unit",
        "  reverse ledger reviews constructed units; presentation packets govern content",
        "  presentations. This file alone joins one register obligation to admitted support.",
        "- **Use:** readiness checks can count exact residual OPEN obligations without",
        "  inferring closure from prose, historical statuses, or unreviewed additions.",
        "",
        "## Why contract supersession is a separate disposition",
        "",
        "- **Necessity:** ordinary completion cannot express that an immutable demand",
        "  to normalize inherited notation conflicts with the later fidelity contract.",
        "- **Definition:** SUPERSEDED_BY_CONTRACT is projected only for the atomic set",
        "  S-002, S-003, A-167, and A-168 after the exact contract record, source",
        "  coordinates, affected units and provenance, scoped roles, and six evidence",
        "  categories validate. It is never COMPLETE.",
        "- **Standing:** this is a metalinguistic administrative disposition, not a",
        "  motive, a relation among motives, a statement family, or handbook doctrine.",
        "- **Nonredundancy:** COMPLETE records fulfilled work; this disposition preserves",
        "  the original rows and records why only their notation-rewrite fields no longer",
        "  govern. A-172 and every other obligation remain outside this control.",
        "- **Use:** terminal readiness may count the four rows only when this generator",
        "  reproduces the projection; a hand-edited CSV cannot establish supersession.",
        "",
        "## Rows",
        "",
        "| Obligation | Source | Line | Record SHA-256 | Status | Contract record | Handbook units | Packets | Labels |",
        "|---|---|---:|---|---|---|---|---|---|",
    ]
    for row in rows:
        values = (
            row["obligation_id"],
            row["source_register"],
            row["source_line"],
            row["record_sha256"],
            row["completion_status"],
            row["contract_supersession_id"],
            row["handbook_unit_ids"],
            row["presentation_packet_ids"],
            row["destination_labels"],
        )
        lines.append("| " + " | ".join(_md_cell(value) for value in values) + " |")
    return ("\n".join(lines) + "\n").encode("utf-8")


def build_outputs(
    manifest_path: Path,
    reviewed_path: Path,
    root: Path,
    *,
    expected_count: int = MANIFEST_COUNT,
    expected_manifest_sha256: str | None = MANIFEST_SHA256,
    unit_inventory_path: Path = DEFAULT_UNIT_INVENTORY,
    unit_reverse_path: Path = DEFAULT_UNIT_REVERSE,
    packet_root: Path = DEFAULT_PACKET_ROOT,
) -> tuple[list[dict[str, str]], bytes, bytes]:
    rows = load_manifest(
        manifest_path,
        root,
        expected_count=expected_count,
        expected_sha256=expected_manifest_sha256,
    )
    projected = apply_reviewed_records(
        rows,
        reviewed_path,
        manifest_path,
        root,
        unit_inventory_path,
        unit_reverse_path,
        packet_root,
    )
    return projected, csv_bytes(projected), markdown_bytes(projected)


def _compare(path: Path, expected: bytes) -> str | None:
    if not path.is_file():
        return f"missing generated file: {path}"
    actual = path.read_bytes()
    if actual != expected:
        return f"stale generated file: {path}"
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="write deterministic outputs")
    mode.add_argument("--check", action="store_true", help="check committed outputs byte-for-byte")
    args = parser.parse_args(argv)
    try:
        rows, csv_output, markdown_output = build_outputs(
            DEFAULT_MANIFEST,
            DEFAULT_REVIEWED,
            ROOT,
        )
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        print("register obligation closure: FAIL", file=sys.stderr)
        print(f"  {exc}", file=sys.stderr)
        return 1
    if args.check:
        failures = [
            item
            for item in (
                _compare(DEFAULT_CSV, csv_output),
                _compare(DEFAULT_MD, markdown_output),
            )
            if item is not None
        ]
        if failures:
            print("register obligation closure: FAIL", file=sys.stderr)
            for failure in failures:
                print(f"  {failure}", file=sys.stderr)
            return 1
        complete = sum(row["completion_status"] == "COMPLETE" for row in rows)
        superseded = sum(
            row["completion_status"] == "SUPERSEDED_BY_CONTRACT" for row in rows
        )
        print("register obligation closure: OK")
        print(
            f"  rows={len(rows)} complete={complete} superseded={superseded} "
            f"open={len(rows) - complete - superseded}"
        )
        return 0
    DEFAULT_CSV.write_bytes(csv_output)
    DEFAULT_MD.write_bytes(markdown_output)
    complete = sum(row["completion_status"] == "COMPLETE" for row in rows)
    superseded = sum(
        row["completion_status"] == "SUPERSEDED_BY_CONTRACT" for row in rows
    )
    print("register obligation closure: WROTE")
    print(
        f"  rows={len(rows)} complete={complete} superseded={superseded} "
        f"open={len(rows) - complete - superseded}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
