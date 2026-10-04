#!/usr/bin/env python3
"""Stream-check external-coverage assignment sidecars against admitted packets."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sqlite3
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterator

try:
    import build_presentation_packet_admission as packet_admission
except ImportError:  # pragma: no cover
    from tools import build_presentation_packet_admission as packet_admission  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "spec/external-coverage-assignment-index.json"
SCHEMA_VERSION = 1
METADATA_SCHEMA_VERSION = 2
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COVERAGE_ID_RE = re.compile(r"^SRC-(\d{3})(?:-([HT])(\d{3,}))?$")
INDEX_FIELDS = {
    "schema_version",
    "coverage_manifest_path",
    "coverage_manifest_sha256",
    "coverage_manifest_bytes",
    "coverage_manifest_record_count",
    "packet_admission_path",
    "packet_admission_sha256",
    "packet_admission_bytes",
    "sidecars",
}
SIDECAR_INDEX_FIELDS = {
    "sidecar_path",
    "sidecar_sha256",
    "assignment_count",
    "first_coverage_id",
    "last_coverage_id",
}
SIDECAR_FIELDS = (
    "coverage_id",
    "packet_id",
    "source_locator",
    "present_content_item_ids",
)
METADATA_FIELDS = {
    "disposition_id", "disposition_kind", "descriptor_profile", "membership_receipt_path",
    "membership_receipt_sha256", "rationale_path", "rationale_sha256",
    "verification_evidence",
}
CATALOG_FIELDS = (
    "stable_id", "record_type", "source_id", "source_title", "source_metadata",
    "retrieved_granularity", "hierarchy_path", "parent_stable_id", "displayed_title",
    "source_https_urls", "source_non_https_urls", "source_scheme_less_identifiers",
    "retrieval_date", "mapping_status",
)
# The first reviewed producer profile is deliberately bounded. Other scratch
# inventories have different grammars and need their own reviewed compatibility.
DESCRIPTOR_SOURCE = "SRC-068"
DESCRIPTOR_PARENT = "SRC-068-H278"
DESCRIPTOR_PRECEDING = "SRC-068-T11119"
DESCRIPTOR_HEADING = "SRC-068 deterministic scratch inventory"
DESCRIPTOR_IDS = tuple(f"SRC-068-T{i}" for i in range(11120, 11529))
DESCRIPTOR_PATTERN = (
    r"\[TOPIC-(?P<topic>[0-9]{6})\] \[SCRATCH-(?P<scratch>[0-9]{4})\] "
    r"(?P<path>tmp/acquisition/src068/[^\r\n|]+) \| bytes=(?P<bytes>0|[1-9][0-9]*) "
    r"\| physical_lines=(?P<lines>0|[1-9][0-9]*) \| sha256=(?P<sha>[0-9a-f]{64}) — \*\*OPEN\*\*"
)
DESCRIPTOR_RE = re.compile(DESCRIPTOR_PATTERN)
DESCRIPTOR_LOCATOR = "acquisition_file_descriptor:SRC-068-H278:SRC-068-T11120..SRC-068-T11528"
RECEIPT_FIELDS = {
    "standing", "catalog_path", "catalog_sha256", "catalog_bytes", "rows",
    "type_counts", "source_count", "all_stable_ids_unique", "uniqueness_method",
    "predicate", "selected_count", "source_and_parent", "preceding_excluded_record", "selected",
}


class DuplicateJsonFieldError(ValueError):
    pass


@dataclass(frozen=True)
class CoverageAssignmentResult:
    coverage_record_count: int
    assignment_count: int
    unassigned_count: int
    admitted_packet_count: int
    sidecar_count: int
    metadata_disposition_count: int = 0
    metadata_batch_count: int = 0


@dataclass(frozen=True)
class AdmittedPacket:
    packet_id: str
    packet_path: str
    packet_sha256: str
    presentation_identity_projection_sha256: str
    present_content_item_ids: frozenset[str]


@dataclass(frozen=True)
class Assignment:
    coverage_id: str
    packet_id: str
    source_locator: str
    present_content_item_ids: tuple[str, ...]
    location: str


@dataclass
class MetadataBatch:
    disposition_id: str
    records: dict[str, dict[str, str]]
    selected_ids: frozenset[str]
    type_counts: dict[str, int]


def metadata_review_scope(disposition: dict[str, object], index: dict[str, object]) -> str:
    """Exact review scope: excludes evidence itself, binds every decision input."""
    identity = {key: disposition[key] for key in sorted(METADATA_FIELDS - {"verification_evidence"})}
    identity["catalog"] = {
        key: index[key] for key in (
            "coverage_manifest_path", "coverage_manifest_sha256",
            "coverage_manifest_bytes", "coverage_manifest_record_count",
        )
    }
    return f"{disposition['disposition_id']} disposition_sha256={packet_admission.canonical_digest(identity)}"


def row_payload_digest(row: dict[str, str]) -> str:
    """The receipt producer hashes compact UTF-8 JSON in CSV field order."""
    return sha256_bytes(json.dumps(
        {field: row[field] for field in CATALOG_FIELDS},
        ensure_ascii=False, separators=(",", ":"),
    ).encode("utf-8"))


def receipt_record(value: object, location: str) -> dict[str, str]:
    record = require_exact_fields(value, set(CATALOG_FIELDS), location)
    if any(not isinstance(value, str) for value in record.values()):
        raise ValueError(f"{location}: original catalog fields must be strings")
    if record["mapping_status"] != "open/unmapped":
        raise ValueError(f"{location}: historical mapping status drift")
    validate_coverage_id(nonempty(record["stable_id"], location), location)
    return dict(record)  # type: ignore[arg-type]


def read_descriptor_receipt(value: object, index: dict[str, object], location: str) -> MetadataBatch:
    receipt = require_exact_fields(value, RECEIPT_FIELDS, location)
    for receipt_key, index_key in (
        ("catalog_path", "coverage_manifest_path"),
        ("catalog_sha256", "coverage_manifest_sha256"),
        ("catalog_bytes", "coverage_manifest_bytes"),
        ("rows", "coverage_manifest_record_count"),
    ):
        if type(receipt[receipt_key]) is not type(index[index_key]) or receipt[receipt_key] != index[index_key]:
            raise ValueError(f"{location}: receipt catalog identity drift ({receipt_key})")
    nonempty(receipt["standing"], f"{location}.standing")
    nonempty(receipt["uniqueness_method"], f"{location}.uniqueness_method")
    if receipt["all_stable_ids_unique"] is not True:
        raise ValueError(f"{location}: receipt must record global uniqueness")
    counts = require_exact_fields(receipt["type_counts"], {"source", "hierarchy", "topic"}, location)
    type_counts = {key: exact_integer(value, location) for key, value in counts.items()}
    if sum(type_counts.values()) != index["coverage_manifest_record_count"] or exact_integer(receipt["source_count"], location) != type_counts["source"]:
        raise ValueError(f"{location}: receipt type/source count drift")
    if receipt["predicate"] != DESCRIPTOR_PATTERN:
        raise ValueError(f"{location}: unsupported descriptor grammar; receipt predicates cannot widen membership")
    if exact_integer(receipt["selected_count"], location) != len(DESCRIPTOR_IDS):
        raise ValueError(f"{location}: exact descriptor membership count required")
    joins = require_exact_fields(receipt["source_and_parent"], {DESCRIPTOR_SOURCE, DESCRIPTOR_PARENT}, location)
    source = receipt_record(joins[DESCRIPTOR_SOURCE], f"{location}.source")
    parent = receipt_record(joins[DESCRIPTOR_PARENT], f"{location}.parent")
    title = nonempty(source["source_title"], f"{location}.source_title")
    if (source["stable_id"], source["source_id"], source["record_type"], source["parent_stable_id"], source["displayed_title"]) != (DESCRIPTOR_SOURCE, DESCRIPTOR_SOURCE, "source", "", title) or json.loads(source["hierarchy_path"]) != [title]:
        raise ValueError(f"{location}: invalid source join")
    if (parent["stable_id"], parent["source_id"], parent["record_type"], parent["parent_stable_id"], parent["source_title"], parent["displayed_title"], parent["retrieval_date"]) != (DESCRIPTOR_PARENT, DESCRIPTOR_SOURCE, "hierarchy", DESCRIPTOR_SOURCE, title, DESCRIPTOR_HEADING, source["retrieval_date"]) or json.loads(parent["hierarchy_path"]) != [title, DESCRIPTOR_HEADING]:
        raise ValueError(f"{location}: invalid parent join")
    preceding = receipt_record(receipt["preceding_excluded_record"], f"{location}.preceding")
    if (preceding["stable_id"], preceding["record_type"], preceding["source_id"], preceding["parent_stable_id"], preceding["source_title"]) != (DESCRIPTOR_PRECEDING, "topic", DESCRIPTOR_SOURCE, "SRC-068-H277", title):
        raise ValueError(f"{location}: preceding excluded record drift")
    records = {DESCRIPTOR_SOURCE: source, DESCRIPTOR_PARENT: parent, DESCRIPTOR_PRECEDING: preceding}
    selected = receipt["selected"]
    if not isinstance(selected, list) or len(selected) != len(DESCRIPTOR_IDS):
        raise ValueError(f"{location}: exact descriptor membership required")
    inherited_fields = ("source_metadata", "retrieved_granularity", "source_https_urls", "source_non_https_urls", "source_scheme_less_identifiers")
    for ordinal, (raw, expected_id) in enumerate(zip(selected, DESCRIPTOR_IDS), start=1):
        entry = require_exact_fields(raw, {"original_record", "payload_sha256", "descriptor_fields"}, location)
        row = receipt_record(entry["original_record"], f"{location}.selected[{ordinal - 1}]")
        match = DESCRIPTOR_RE.fullmatch(row["displayed_title"])
        if (row["stable_id"], row["record_type"], row["source_id"], row["parent_stable_id"], row["source_title"], row["retrieval_date"]) != (expected_id, "topic", DESCRIPTOR_SOURCE, DESCRIPTOR_PARENT, title, source["retrieval_date"]) or match is None:
            raise ValueError(f"{location}: invalid descriptor membership or grammar at {expected_id}")
        fields = match.groupdict()
        descriptor_path = PurePosixPath(fields["path"])
        if (str(descriptor_path) != fields["path"] or "\\" in fields["path"] or ".." in descriptor_path.parts or fields["path"] != fields["path"].strip()):
            raise ValueError(f"{location}: invalid descriptor path data")
        if int(fields["topic"]) != 11119 + ordinal or int(fields["scratch"]) != ordinal:
            raise ValueError(f"{location}: descriptor topic/scratch ordinal drift")
        if entry["descriptor_fields"] != fields:
            raise ValueError(f"{location}: extracted descriptor fields drift")
        if any(row[key] for key in inherited_fields) or json.loads(row["hierarchy_path"]) != [title, DESCRIPTOR_HEADING, row["displayed_title"]]:
            raise ValueError(f"{location}: descriptor hierarchy or source inheritance drift")
        if sha(entry["payload_sha256"], location) != row_payload_digest(row):
            raise ValueError(f"{location}: original payload digest drift")
        records[expected_id] = row
    return MetadataBatch("", records, frozenset(DESCRIPTOR_IDS), type_counts)


def validate_metadata_evidence(
    value: object, root: Path, forbidden: set[Path], known_hashes: dict[Path, str],
    coverage_path: Path, required_authorities: dict[str, str], scope: str, location: str,
) -> None:
    """The existing AI evidence convention, with three administrative gates.

    The catalog digest is checked by the caller's single manifest stream. Never
    read it as an evidence blob or hash it again for each authority record.
    """
    if not isinstance(value, list) or len(value) != 3:
        raise ValueError(f"{location}: exactly three AI evidence records required")
    categories: set[str] = set()
    artifacts: set[Path] = set()
    hashes: set[str] = set()
    producers: set[str] = set()

    def digest_file(path: Path) -> str:
        if path not in known_hashes:
            digest = hashlib.sha256()
            with path.open("rb") as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(block)
            known_hashes[path] = digest.hexdigest()
        return known_hashes[path]

    forbidden_hashes = {digest_file(path) for path in forbidden}
    for ordinal, raw in enumerate(value):
        where = f"{location}[{ordinal}]"
        item = require_exact_fields(raw, packet_admission.AI_EVIDENCE_FIELDS, where)
        category = nonempty(item["category"], where)
        if category not in packet_admission.AI_VERIFICATION_FIELDS or category in categories:
            raise ValueError(f"{where}: distinct required AI categories required")
        categories.add(category)
        if item["recorded_result"] != "pass":
            raise ValueError(f"{where}: metadata evidence must pass")
        _, artifact = repo_file(root, item["artifact_path"], where)
        if packet_admission.shares_filesystem_identity(artifact, forbidden | artifacts, where):
            raise ValueError(f"{where}: separate non-self evidence filesystem identity required")
        artifact_hash = sha(item["sha256"], where)
        if digest_file(artifact) != artifact_hash:
            raise ValueError(f"{where}: evidence SHA-256 drift")
        if artifact_hash in hashes or artifact_hash in forbidden_hashes:
            raise ValueError(f"{where}: distinct non-self evidence bytes required")
        artifacts.add(artifact)
        hashes.add(artifact_hash)
        producer = packet_admission.producer_key(nonempty(item["producer_identity"], where))
        if producer in producers:
            raise ValueError(f"{where}: distinct producers required")
        producers.add(producer)
        if item["recorded_scope"] != scope:
            raise ValueError(f"{where}: exact disposition review scope required")
        for field in ("model", "model_version", "instructions"):
            nonempty(item[field], f"{where}.{field}")
        if sha(item["evidence_digest"], where) != artifact_hash:
            raise ValueError(f"{where}: evidence digest must equal artifact hash")
        authorities = item["consulted_authority_files"]
        if not isinstance(authorities, list) or not authorities:
            raise ValueError(f"{where}: consulted authority files required")
        actual: dict[str, str] = {}
        for raw_authority in authorities:
            authority = require_exact_fields(raw_authority, {"path", "sha256"}, where)
            path_value, path = repo_file(root, authority["path"], where)
            authority_hash = sha(authority["sha256"], where)
            if path != coverage_path and packet_admission.shares_filesystem_identity(path, {coverage_path}, where):
                raise ValueError(f"{where}: catalog authority requires its canonical path")
            if path_value in actual or digest_file(path) != authority_hash:
                raise ValueError(f"{where}: duplicate authority or authority digest drift")
            actual[path_value] = authority_hash
        if list(actual) != sorted(actual) or any(actual.get(key) != digest for key, digest in required_authorities.items()):
            raise ValueError(f"{where}: sorted exact receipt/rationale/catalog authorities required")
        locators = packet_admission.sorted_strings(item["consulted_authority_locators"], where, nonempty_array=True)
        if DESCRIPTOR_LOCATOR not in locators:
            raise ValueError(f"{where}: descriptor membership authority locator required")
        packet_admission.sorted_strings(item["findings"], where, nonempty_array=True)


def read_metadata_batches(root: Path, index_path: Path, document: dict[str, object], coverage_path: Path) -> list[MetadataBatch]:
    values = document.get("metadata_dispositions", [])
    if not isinstance(values, list):
        raise ValueError("metadata_dispositions: expected array")
    batches: list[MetadataBatch] = []
    disposition_ids: set[str] = set()
    selected_ids: set[str] = set()
    known_hashes = {coverage_path: str(document["coverage_manifest_sha256"])}
    for ordinal, raw in enumerate(values):
        location = f"metadata_dispositions[{ordinal}]"
        item = require_exact_fields(raw, METADATA_FIELDS, location)
        identity = nonempty(item["disposition_id"], location)
        if re.fullmatch(r"META-[A-Za-z0-9][A-Za-z0-9._-]*", identity) is None or identity in disposition_ids:
            raise ValueError(f"{location}: invalid or duplicate disposition ID")
        disposition_ids.add(identity)
        if item["disposition_kind"] != "acquisition_file_descriptor":
            raise ValueError(f"{location}: unsupported disposition kind")
        if item["descriptor_profile"] != "src068-h278-v1":
            raise ValueError(f"{location}: unsupported descriptor profile")
        receipt_value, receipt_path = repo_file(root, item["membership_receipt_path"], location, prefix="spec/provenance/external-coverage-assignments/")
        rationale_value, rationale_path = repo_file(root, item["rationale_path"], location, prefix="spec/research/")
        for path, field in ((receipt_path, "membership_receipt_sha256"), (rationale_path, "rationale_sha256")):
            if packet_admission.shares_filesystem_identity(path, {coverage_path, index_path.resolve()}, location):
                raise ValueError(f"{location}: receipt/rationale cannot alias catalog or index")
            expected_hash = sha(item[field], location)
            if sha256_bytes(path.read_bytes()) != expected_hash:
                raise ValueError(f"{location}: receipt/rationale digest drift")
            known_hashes[path] = expected_hash
        if packet_admission.shares_filesystem_identity(receipt_path, {rationale_path}, location):
            raise ValueError(f"{location}: separate receipt and rationale required")
        batch = read_descriptor_receipt(load_json(receipt_path, location), document, location)
        batch.disposition_id = identity
        if selected_ids & batch.selected_ids:
            raise ValueError(f"{location}: overlapping metadata batches")
        selected_ids.update(batch.selected_ids)
        validate_metadata_evidence(
            item["verification_evidence"], root,
            {coverage_path, index_path.resolve(), receipt_path, rationale_path}, known_hashes,
            coverage_path,
            {str(document["coverage_manifest_path"]): str(document["coverage_manifest_sha256"]), receipt_value: str(item["membership_receipt_sha256"]), rationale_value: str(item["rationale_sha256"])},
            metadata_review_scope(item, document), location,
        )
        batches.append(batch)
    return batches


class HashedUtf8Lines:
    """Binary-line stream exposing exact digest/byte totals without materializing a file."""

    def __init__(self, path: Path, location: str) -> None:
        self.path = path
        self.location = location
        self.sha256 = hashlib.sha256()
        self.byte_count = 0

    def __iter__(self) -> Iterator[str]:
        try:
            with self.path.open("rb") as stream:
                for line_number, raw in enumerate(stream, start=1):
                    self.sha256.update(raw)
                    self.byte_count += len(raw)
                    if b"\r" in raw:
                        raise ValueError(
                            f"{self.location}:{line_number}: LF-only CSV is required"
                        )
                    try:
                        yield raw.decode("utf-8")
                    except UnicodeDecodeError as exc:
                        raise ValueError(
                            f"{self.location}:{line_number}: invalid UTF-8: {exc}"
                        ) from exc
        except OSError as exc:
            raise ValueError(f"{self.location}: cannot read file: {exc}") from exc

    @property
    def digest(self) -> str:
        return self.sha256.hexdigest()


def duplicate_rejecting_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonFieldError(f"duplicate JSON field {key!r}")
        result[key] = value
    return result


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load_json(path: Path, location: str) -> object:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=duplicate_rejecting_object,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateJsonFieldError) as exc:
        raise ValueError(f"{location}: invalid JSON: {exc}") from exc


def require_exact_fields(value: object, expected: set[str], location: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{location}: expected object")
    missing = sorted(expected - set(value))
    extra = sorted(set(value) - expected)
    if missing or extra:
        raise ValueError(
            f"{location}: exact field set required (missing {missing}; unexpected {extra})"
        )
    return value


def nonempty(value: object, location: str) -> str:
    if (
        not isinstance(value, str)
        or not value.strip()
        or value != value.strip()
        or "\r" in value
        or "\n" in value
    ):
        raise ValueError(f"{location}: expected one nonempty trimmed line")
    return value


def sha(value: object, location: str) -> str:
    if not isinstance(value, str) or SHA256_RE.fullmatch(value) is None:
        raise ValueError(f"{location}: expected lowercase SHA-256")
    return value


def exact_integer(value: object, location: str, *, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{location}: expected integer >= {minimum}")
    return value


def repo_file(
    root: Path,
    value: object,
    location: str,
    *,
    prefix: str | None = None,
) -> tuple[str, Path]:
    raw = nonempty(value, location)
    if "\\" in raw:
        raise ValueError(f"{location}: use POSIX path syntax")
    pure = PurePosixPath(raw)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        raise ValueError(f"{location}: path must remain inside repository")
    if prefix is not None and not raw.startswith(prefix):
        raise ValueError(f"{location}: path must start with {prefix!r}")
    resolved_root = root.resolve()
    resolved = (resolved_root / Path(*pure.parts)).resolve()
    try:
        relative = resolved.relative_to(resolved_root).as_posix()
    except ValueError as exc:
        raise ValueError(f"{location}: path must remain inside repository") from exc
    if relative != raw:
        raise ValueError(f"{location}: noncanonical path, traversal, or symlink indirection")
    if not resolved.is_file():
        raise ValueError(f"{location}: file does not exist")
    return raw, resolved


def parse_compact_string_array(
    value: object,
    location: str,
    *,
    nonempty_array: bool,
) -> tuple[str, ...]:
    raw = nonempty(value, location)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{location}: invalid JSON array: {exc}") from exc
    if not isinstance(parsed, list):
        raise ValueError(f"{location}: expected JSON array")
    strings = tuple(nonempty(item, f"{location}[{index}]") for index, item in enumerate(parsed))
    if list(strings) != sorted(set(strings)):
        raise ValueError(f"{location}: values must be unique and sorted")
    if nonempty_array and not strings:
        raise ValueError(f"{location}: expected nonempty array")
    canonical = json.dumps(list(strings), ensure_ascii=False, separators=(",", ":"))
    if raw != canonical:
        raise ValueError(f"{location}: compact canonical JSON is required")
    return strings


def validate_coverage_id(value: str, location: str) -> str:
    match = COVERAGE_ID_RE.fullmatch(value)
    if match is None:
        raise ValueError(f"{location}: noncanonical coverage ID")
    kind = match.group(2)
    raw_counter = match.group(3)
    if kind is None:
        return value
    assert raw_counter is not None
    counter = int(raw_counter)
    if counter < 1 or raw_counter != f"{counter:03d}":
        raise ValueError(f"{location}: noncanonical coverage ID")
    return value


class DiskBackedUniqueIds:
    """Exact global uniqueness with fixed RAM and a disposable SQLite index."""

    def __init__(self) -> None:
        self._temporary: tempfile.TemporaryDirectory[str] | None = None
        self._connection: sqlite3.Connection | None = None

    def __enter__(self) -> "DiskBackedUniqueIds":
        try:
            self._temporary = tempfile.TemporaryDirectory(
                prefix="external-coverage-unique-"
            )
            database = Path(self._temporary.name) / "stable-ids.sqlite3"
            self._connection = sqlite3.connect(database)
            # This index is disposable and rebuilt from the hash-pinned source
            # on every run. Bound SQLite's RAM while avoiding durability work
            # that cannot add correctness to a temporary database.
            self._connection.execute("PRAGMA cache_size=-16384")
            self._connection.execute("PRAGMA journal_mode=OFF")
            self._connection.execute("PRAGMA synchronous=OFF")
            self._connection.execute("PRAGMA temp_store=FILE")
            self._connection.execute("PRAGMA locking_mode=EXCLUSIVE")
            self._connection.execute(
                "CREATE TABLE seen (stable_id TEXT PRIMARY KEY) WITHOUT ROWID"
            )
            self._connection.execute("BEGIN IMMEDIATE")
        except (OSError, sqlite3.Error) as exc:
            self.close()
            raise ValueError(f"coverage uniqueness index: cannot initialize: {exc}") from exc
        return self

    def add(self, stable_id: str, location: str) -> None:
        assert self._connection is not None
        try:
            self._connection.execute(
                "INSERT INTO seen(stable_id) VALUES (?)", (stable_id,)
            )
        except sqlite3.IntegrityError as exc:
            raise ValueError(
                f"{location}: duplicate coverage ID {stable_id}"
            ) from exc
        except sqlite3.Error as exc:
            raise ValueError(f"coverage uniqueness index: cannot write: {exc}") from exc

    def close(self) -> None:
        if self._connection is not None:
            self._connection.close()
            self._connection = None
        if self._temporary is not None:
            self._temporary.cleanup()
            self._temporary = None

    def __exit__(self, _exc_type: object, _exc: object, _traceback: object) -> None:
        self.close()


def read_admitted_packets(
    root: Path,
    admission_path: Path,
    expected_digest: str,
    expected_bytes: int,
) -> tuple[dict[str, AdmittedPacket], dict[str, tuple[str, str, tuple[str, ...]]]]:
    try:
        raw = admission_path.read_bytes()
    except OSError as exc:
        raise ValueError(f"packet admission: cannot read file: {exc}") from exc
    if len(raw) != expected_bytes:
        raise ValueError("packet admission: byte-count drift")
    if sha256_bytes(raw) != expected_digest:
        raise ValueError("packet admission: digest drift")
    if b"\r" in raw:
        raise ValueError("packet admission: LF-only CSV is required")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"packet admission: invalid UTF-8: {exc}") from exc
    reader = csv.DictReader(io.StringIO(text, newline=""))
    if tuple(reader.fieldnames or ()) != packet_admission.OUTPUT_FIELDS:
        raise ValueError("packet admission: exact generated header is required")
    admitted: dict[str, AdmittedPacket] = {}
    seen_packet_ids: set[str] = set()
    packet_declared: dict[str, tuple[str, str, tuple[str, ...]]] = {}
    for row_number, row in enumerate(reader, start=2):
        location = f"packet admission:{row_number}"
        packet_id = nonempty(row.get("packet_id"), f"{location}.packet_id")
        if packet_id in seen_packet_ids:
            raise ValueError(f"{location}: duplicate packet ID {packet_id}")
        seen_packet_ids.add(packet_id)
        status = row.get("admission_status")
        if status == "OPEN":
            continue
        if status != "ADMITTED":
            raise ValueError(f"{location}.admission_status: expected OPEN or ADMITTED")
        for category in packet_admission.VERIFICATION_FIELDS:
            if row.get(f"{category}_verification") != "pass":
                raise ValueError(f"{location}: ADMITTED packet lacks passing {category}")
        packet_path_value, packet_path = repo_file(
            root, row.get("packet_path"), f"{location}.packet_path", prefix="spec/presentations/"
        )
        packet_hash = sha(row.get("packet_sha256"), f"{location}.packet_sha256")
        try:
            packet_raw = packet_path.read_bytes()
        except OSError as exc:
            raise ValueError(f"{location}.packet_path: cannot read packet: {exc}") from exc
        if sha256_bytes(packet_raw) != packet_hash:
            raise ValueError(f"{location}.packet_sha256: packet digest drift")
        packet = load_json(packet_path, f"presentation packet {packet_path_value}")
        if not isinstance(packet, dict):
            raise ValueError(f"presentation packet {packet_path_value}: expected object")
        if packet.get("packet_id") != packet_id:
            raise ValueError(f"{location}.packet_id: differs from packet")
        if packet.get("overall_status") != "verified":
            raise ValueError(f"{location}: ADMITTED packet is not verified")
        identity = packet.get("presentation_identity")
        if not isinstance(identity, dict) or identity.get("identity_status") != "identified":
            raise ValueError(f"{location}: packet presentation is not identified")
        identity_digest = sha(
            row.get("presentation_identity_projection_sha256"),
            f"{location}.presentation_identity_projection_sha256",
        )
        if packet_admission.canonical_digest(identity) != identity_digest:
            raise ValueError(f"{location}: presentation identity projection drift")
        content_ids = parse_compact_string_array(
            row.get("present_content_item_ids"),
            f"{location}.present_content_item_ids",
            nonempty_array=True,
        )
        if list(content_ids) != packet_admission.present_item_ids(packet):
            raise ValueError(f"{location}: admitted content item projection drift")
        admitted[packet_id] = AdmittedPacket(
            packet_id=packet_id,
            packet_path=packet_path_value,
            packet_sha256=packet_hash,
            presentation_identity_projection_sha256=identity_digest,
            present_content_item_ids=frozenset(content_ids),
        )
        obligation_links = packet.get("obligation_links")
        if not isinstance(obligation_links, dict):
            raise ValueError(f"{location}: packet obligation links are invalid")
        assignments = obligation_links.get("coverage_assignments")
        if not isinstance(assignments, list):
            raise ValueError(f"{location}: packet coverage assignments are invalid")
        for assignment_index, assignment_value in enumerate(assignments):
            assignment_location = (
                f"presentation packet {packet_path_value}.obligation_links."
                f"coverage_assignments[{assignment_index}]"
            )
            if not isinstance(assignment_value, dict):
                raise ValueError(f"{assignment_location}: expected object")
            if assignment_value.get("assignment_status") != "fulfilled":
                raise ValueError(f"{assignment_location}: admitted packet assignment is not fulfilled")
            coverage_id = nonempty(
                assignment_value.get("obligation_id"), f"{assignment_location}.obligation_id"
            )
            locator = nonempty(
                assignment_value.get("source_locator"), f"{assignment_location}.source_locator"
            )
            raw_ids = assignment_value.get("present_content_item_ids")
            if not isinstance(raw_ids, list):
                raise ValueError(f"{assignment_location}.present_content_item_ids: expected array")
            item_ids = tuple(
                nonempty(item, f"{assignment_location}.present_content_item_ids[{index}]")
                for index, item in enumerate(raw_ids)
            )
            if list(item_ids) != sorted(set(item_ids)) or not item_ids:
                raise ValueError(
                    f"{assignment_location}.present_content_item_ids: nonempty sorted unique array required"
                )
            if not set(item_ids).issubset(admitted[packet_id].present_content_item_ids):
                raise ValueError(f"{assignment_location}: references unknown admitted content item")
            if coverage_id in packet_declared:
                raise ValueError(
                    f"{assignment_location}: duplicate packet-declared coverage ID {coverage_id}"
                )
            packet_declared[coverage_id] = (packet_id, locator, item_ids)
    return admitted, packet_declared


def iter_assignments(
    root: Path,
    sidecars: list[dict[str, object]],
    admitted: dict[str, AdmittedPacket],
) -> Iterator[Assignment]:
    previous_path = ""
    previous_assignment_id: str | None = None
    seen_paths: set[Path] = set()
    for sidecar_index, untyped in enumerate(sidecars):
        location = f"assignment index.sidecars[{sidecar_index}]"
        record = require_exact_fields(untyped, SIDECAR_INDEX_FIELDS, location)
        path_value, path = repo_file(
            root,
            record["sidecar_path"],
            f"{location}.sidecar_path",
            prefix="spec/provenance/external-coverage-assignments/",
        )
        if path_value <= previous_path:
            raise ValueError("assignment index.sidecars: paths must be unique and sorted")
        previous_path = path_value
        if path in seen_paths:
            raise ValueError(f"{location}.sidecar_path: duplicate sidecar")
        seen_paths.add(path)
        expected_digest = sha(record["sidecar_sha256"], f"{location}.sidecar_sha256")
        expected_count = exact_integer(
            record["assignment_count"], f"{location}.assignment_count", minimum=1
        )
        expected_first = nonempty(record["first_coverage_id"], f"{location}.first_coverage_id")
        expected_last = nonempty(record["last_coverage_id"], f"{location}.last_coverage_id")
        lines = HashedUtf8Lines(path, f"coverage sidecar {path_value}")
        reader = csv.DictReader(lines)
        if tuple(reader.fieldnames or ()) != SIDECAR_FIELDS:
            raise ValueError(f"coverage sidecar {path_value}: exact header is required")
        count = 0
        first_id = ""
        last_id = ""
        for row_number, row in enumerate(reader, start=2):
            row_location = f"coverage sidecar {path_value}:{row_number}"
            coverage_id = nonempty(row.get("coverage_id"), f"{row_location}.coverage_id")
            validate_coverage_id(coverage_id, f"{row_location}.coverage_id")
            if coverage_id == previous_assignment_id:
                raise ValueError(f"{row_location}.coverage_id: duplicate assignment {coverage_id}")
            previous_assignment_id = coverage_id
            packet_id = nonempty(row.get("packet_id"), f"{row_location}.packet_id")
            packet = admitted.get(packet_id)
            if packet is None:
                raise ValueError(
                    f"{row_location}.packet_id: packet {packet_id!r} is not independently admitted"
                )
            locator = nonempty(row.get("source_locator"), f"{row_location}.source_locator")
            content_ids = parse_compact_string_array(
                row.get("present_content_item_ids"),
                f"{row_location}.present_content_item_ids",
                nonempty_array=True,
            )
            for item_id in content_ids:
                if item_id not in packet.present_content_item_ids:
                    raise ValueError(
                        f"{row_location}.present_content_item_ids: unknown admitted content item {item_id}"
                    )
            count += 1
            if count == 1:
                first_id = coverage_id
            last_id = coverage_id
            yield Assignment(coverage_id, packet_id, locator, content_ids, row_location)
        if count != expected_count:
            raise ValueError(f"{location}.assignment_count: assignment count drift")
        if first_id != expected_first:
            raise ValueError(f"{location}.first_coverage_id: first coverage ID drift")
        if last_id != expected_last:
            raise ValueError(f"{location}.last_coverage_id: last coverage ID drift")
        if lines.digest != expected_digest:
            raise ValueError(f"{location}.sidecar_sha256: sidecar digest drift")


def validate_index(
    root: Path,
    index_path: Path,
    require_complete: bool = False,
) -> CoverageAssignmentResult:
    root = root.resolve()
    untyped = load_json(index_path, "external coverage assignment index")
    version = untyped.get("schema_version") if isinstance(untyped, dict) else None
    if type(version) is not int or version not in (SCHEMA_VERSION, METADATA_SCHEMA_VERSION):
        raise ValueError("external coverage assignment index.schema_version: must be 1 or 2")
    document = require_exact_fields(
        untyped, INDEX_FIELDS | ({"metadata_dispositions"} if version == METADATA_SCHEMA_VERSION else set()),
        "external coverage assignment index",
    )
    coverage_path_value, coverage_path = repo_file(
        root,
        document["coverage_manifest_path"],
        "external coverage assignment index.coverage_manifest_path",
    )
    expected_coverage_digest = sha(
        document["coverage_manifest_sha256"],
        "external coverage assignment index.coverage_manifest_sha256",
    )
    expected_coverage_bytes = exact_integer(
        document["coverage_manifest_bytes"],
        "external coverage assignment index.coverage_manifest_bytes",
    )
    expected_coverage_count = exact_integer(
        document["coverage_manifest_record_count"],
        "external coverage assignment index.coverage_manifest_record_count",
        minimum=1,
    )
    _admission_path_value, admission_path = repo_file(
        root,
        document["packet_admission_path"],
        "external coverage assignment index.packet_admission_path",
    )
    expected_admission_digest = sha(
        document["packet_admission_sha256"],
        "external coverage assignment index.packet_admission_sha256",
    )
    expected_admission_bytes = exact_integer(
        document["packet_admission_bytes"],
        "external coverage assignment index.packet_admission_bytes",
    )
    sidecars = document["sidecars"]
    if not isinstance(sidecars, list):
        raise ValueError("external coverage assignment index.sidecars: expected array")
    admitted, packet_declared = read_admitted_packets(
        root,
        admission_path,
        expected_admission_digest,
        expected_admission_bytes,
    )
    metadata_batches = read_metadata_batches(root, index_path, document, coverage_path)
    metadata_ids = set().union(*(batch.selected_ids for batch in metadata_batches))
    if metadata_ids.intersection(packet_declared):
        raise ValueError("metadata disposition overlaps packet-declared content assignment")
    pending_metadata = {
        stable_id: row for batch in metadata_batches for stable_id, row in batch.records.items()
    }
    assignments = iter(iter_assignments(root, sidecars, admitted))
    try:
        current: Assignment | None = next(assignments)
    except StopIteration:
        current = None
    assignment_count = 0
    metadata_count = 0
    unassigned_count = 0
    manifest_lines = HashedUtf8Lines(coverage_path, f"coverage manifest {coverage_path_value}")
    reader = csv.DictReader(manifest_lines)
    header = tuple(reader.fieldnames or ())
    if "stable_id" not in header or len(header) != len(set(header)):
        raise ValueError(f"coverage manifest {coverage_path_value}: unique stable_id header required")
    if metadata_batches and header != CATALOG_FIELDS:
        raise ValueError("metadata dispositions require the exact historical catalog header")
    coverage_count = 0
    type_counts = {"source": 0, "hierarchy": 0, "topic": 0}
    with DiskBackedUniqueIds() as seen_coverage_ids:
        for row_number, row in enumerate(reader, start=2):
            stable_location = (
                f"coverage manifest {coverage_path_value}:{row_number}.stable_id"
            )
            stable_id = validate_coverage_id(
                nonempty(row.get("stable_id"), stable_location), stable_location
            )
            seen_coverage_ids.add(stable_id, stable_location)
            coverage_count += 1
            if metadata_batches:
                kind = row.get("record_type")
                if kind not in type_counts or None in row or any(value is None for value in row.values()):
                    raise ValueError(f"{stable_location}: malformed historical catalog row")
                type_counts[kind] += 1
                if row.get("parent_stable_id") == DESCRIPTOR_PARENT and stable_id not in metadata_ids:
                    raise ValueError(f"{stable_location}: unexpected child outside exact descriptor membership")
                if stable_id in pending_metadata:
                    if row != pending_metadata.pop(stable_id):
                        raise ValueError(f"{stable_location}: metadata payload/source/parent drift")
                if stable_id in metadata_ids:
                    if current is not None and current.coverage_id == stable_id:
                        raise ValueError(f"{stable_location}: metadata disposition overlaps content assignment")
                    metadata_count += 1
                    continue
            if current is None or current.coverage_id != stable_id:
                unassigned_count += 1
                continue
            expected = packet_declared.get(stable_id)
            actual = (current.packet_id, current.source_locator, current.present_content_item_ids)
            if expected is not None:
                if actual != expected:
                    raise ValueError(
                        f"{current.location}: packet-declared assignment differs from sidecar source of truth"
                    )
                del packet_declared[stable_id]
            assignment_count += 1
            try:
                current = next(assignments)
            except StopIteration:
                current = None
    if current is not None:
        raise ValueError(
            f"{current.location}.coverage_id: unknown or out of manifest order ({current.coverage_id})"
        )
    if coverage_count != expected_coverage_count:
        raise ValueError("external coverage assignment index: coverage record-count drift")
    if manifest_lines.byte_count != expected_coverage_bytes:
        raise ValueError("external coverage assignment index: coverage manifest byte-count drift")
    if manifest_lines.digest != expected_coverage_digest:
        raise ValueError("external coverage assignment index: coverage manifest digest drift")
    if pending_metadata:
        raise ValueError(f"metadata disposition has unknown or missing catalog IDs: {sorted(pending_metadata)[0]}")
    if any(batch.type_counts != type_counts for batch in metadata_batches):
        raise ValueError("metadata receipt catalog type/source-count drift")
    if packet_declared:
        absent = sorted(packet_declared)
        raise ValueError(
            f"packet-declared assignment is absent from sidecar source of truth: {absent[0]}"
        )
    if require_complete and unassigned_count:
        raise ValueError(f"external coverage remains unassigned: {unassigned_count} records")
    return CoverageAssignmentResult(
        coverage_record_count=coverage_count,
        assignment_count=assignment_count,
        unassigned_count=unassigned_count,
        admitted_packet_count=len(admitted),
        sidecar_count=len(sidecars),
        metadata_disposition_count=metadata_count,
        metadata_batch_count=len(metadata_batches),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args(argv)
    try:
        result = validate_index(args.repository_root, args.index, args.require_complete)
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        print(f"external-coverage assignments: FAIL ({exc})", file=sys.stderr)
        return 1
    print(
        "external-coverage assignments: PASS "
        f"coverage={result.coverage_record_count} assignments={result.assignment_count} "
        f"unassigned={result.unassigned_count} admitted-packets={result.admitted_packet_count} "
        f"sidecars={result.sidecar_count} metadata-dispositions={result.metadata_disposition_count} "
        f"metadata-batches={result.metadata_batch_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
