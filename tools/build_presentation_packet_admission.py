#!/usr/bin/env python3
"""Build the independent presentation-packet content-admission projection."""

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

try:
    import check_presentation_packet as packet_checker
except ImportError:  # pragma: no cover
    from tools import check_presentation_packet as packet_checker  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACKET_ROOT = ROOT / "spec/presentations"
DEFAULT_REVIEWED = ROOT / "spec/provenance/reviewed-presentation-packet-admissions.json"
DEFAULT_COVERAGE = ROOT / "spec/full-compendium-coverage-manifest.csv"
DEFAULT_REGISTER = ROOT / "spec/register-obligation-manifest.csv"
DEFAULT_CSV = ROOT / "spec/presentation-packet-admission.csv"
DEFAULT_MD = ROOT / "spec/presentation-packet-admission.md"
PACKET_ROOT_VALUE = "spec/presentations"
SCHEMA_VERSION = 1
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
AI_VERIFICATION_FIELDS = (
    "source_fidelity_ai",
    "topic_specialist_ai",
    "adversarial_publication_ai",
)
VERIFICATION_FIELDS = (*AI_VERIFICATION_FIELDS, "static", "build", "visual")
RECORD_FIELDS = {
    "packet_id",
    "packet_path",
    "packet_sha256",
    "admission_status",
    "authority_projection_sha256",
    "presentation_identity_projection_sha256",
    "content_projection_sha256",
    "present_content_item_ids",
    "destination_file",
    "destination_sha256",
    "destination_labels",
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
OUTPUT_FIELDS = (
    "packet_id",
    "packet_path",
    "packet_sha256",
    "admission_status",
    "authority_projection_sha256",
    "presentation_identity_projection_sha256",
    "content_projection_sha256",
    "present_content_item_ids",
    "destination_file",
    "destination_sha256",
    "destination_labels",
    "source_fidelity_ai_verification",
    "topic_specialist_ai_verification",
    "adversarial_publication_ai_verification",
    "static_verification",
    "build_verification",
    "visual_verification",
    "verification_evidence",
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


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical_digest(value: object) -> str:
    raw = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return sha256_bytes(raw)


def require_exact_fields(value: object, expected: set[str], location: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{location}: expected object")
    missing = sorted(expected - set(value))
    extra = sorted(set(value) - expected)
    if missing or extra:
        raise ValueError(f"{location}: exact field set required (missing {missing}; unexpected {extra})")
    return value


def nonempty(value: object, location: str) -> str:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError(f"{location}: expected nonempty trimmed string")
    return value


def sha(value: object, location: str) -> str:
    if not isinstance(value, str) or SHA256_RE.fullmatch(value) is None:
        raise ValueError(f"{location}: expected lowercase SHA-256")
    return value


def repo_file(root: Path, value: object, location: str, prefix: str | None = None) -> tuple[str, Path]:
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
        raise ValueError(f"{location}: path escapes repository") from exc
    if relative != raw:
        raise ValueError(f"{location}: noncanonical path or indirection")
    if not resolved.is_file():
        raise ValueError(f"{location}: file does not exist")
    return raw, resolved


def sorted_strings(value: object, location: str, *, nonempty_array: bool = False) -> list[str]:
    if not isinstance(value, list):
        raise ValueError(f"{location}: expected array")
    result = [nonempty(item, f"{location}[{index}]") for index, item in enumerate(value)]
    if result != sorted(set(result)):
        raise ValueError(f"{location}: values must be unique and sorted")
    if nonempty_array and not result:
        raise ValueError(f"{location}: expected nonempty array")
    return result


def load_json(path: Path, location: str) -> object:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=duplicate_rejecting_object,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateJsonFieldError) as exc:
        raise ValueError(f"{location}: invalid JSON: {exc}") from exc


def discover_packets(root: Path, packet_root: Path) -> dict[str, tuple[str, Path, dict[str, Any]]]:
    if not packet_root.is_dir():
        return {}
    packet_root_absolute = Path(os.path.abspath(packet_root))
    packet_root_resolved = packet_root.resolve()
    if packet_root_absolute != packet_root_resolved:
        raise ValueError("presentation packet root uses symlink or junction indirection")
    result: dict[str, tuple[str, Path, dict[str, Any]]] = {}
    for path in sorted(packet_root.rglob("*.json")):
        path_absolute = Path(os.path.abspath(path))
        path_resolved = path.resolve()
        if path_absolute != path_resolved:
            raise ValueError(f"presentation packet {path}: symlink or junction indirection")
        try:
            path_resolved.relative_to(packet_root_resolved)
        except ValueError as exc:
            raise ValueError(f"presentation packet {path}: path leaves packet root") from exc
        value = load_json(path, f"presentation packet {path}")
        if not isinstance(value, dict):
            raise ValueError(f"presentation packet {path}: root must be object")
        packet_id = nonempty(value.get("packet_id"), f"presentation packet {path}.packet_id")
        if packet_id in result:
            raise ValueError(f"presentation packet corpus: duplicate packet ID {packet_id}")
        try:
            relative = path_resolved.relative_to(root.resolve()).as_posix()
        except ValueError as exc:
            raise ValueError(f"presentation packet escapes repository: {path}") from exc
        result[packet_id] = (relative, path.resolve(), value)
    return result


def present_item_ids(packet: dict[str, Any]) -> list[str]:
    content = packet.get("content")
    result: list[str] = []
    if isinstance(content, dict):
        for items in content.values():
            if not isinstance(items, list):
                continue
            for item in items:
                if isinstance(item, dict) and item.get("status") == "present":
                    item_id = item.get("item_id")
                    if isinstance(item_id, str):
                        result.append(item_id)
    if len(result) != len(set(result)):
        raise ValueError("presentation packet: duplicate present content item ID")
    return sorted(result)


def producer_key(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def packet_verification_evidence_paths(
    root: Path,
    packet_path: Path,
    packet: dict[str, Any],
    location: str,
) -> set[Path]:
    value = packet.get("verification_evidence")
    if not isinstance(value, list):
        raise ValueError(f"{location}: packet verification evidence is invalid")
    resolved_root = root.resolve()
    result: set[Path] = set()
    for index, untyped in enumerate(value):
        item_location = f"{location}.packet_verification_evidence[{index}]"
        if not isinstance(untyped, dict):
            raise ValueError(f"{item_location}: expected object")
        raw = nonempty(untyped.get("artifact_path"), f"{item_location}.artifact_path")
        if "\\" in raw:
            raise ValueError(f"{item_location}.artifact_path: use POSIX path syntax")
        pure = PurePosixPath(raw)
        if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
            raise ValueError(
                f"{item_location}.artifact_path: path must remain under the packet directory"
            )
        candidate = packet_path.parent / Path(*pure.parts)
        absolute = Path(os.path.abspath(candidate))
        resolved = candidate.resolve()
        if absolute != resolved:
            raise ValueError(
                f"{item_location}.artifact_path: symlink or junction indirection is forbidden"
            )
        try:
            resolved.relative_to(resolved_root)
        except ValueError as exc:
            raise ValueError(
                f"{item_location}.artifact_path: packet evidence leaves repository"
            ) from exc
        if not resolved.is_file():
            raise ValueError(f"{item_location}.artifact_path: file does not exist")
        declared_hash = sha(untyped.get("sha256"), f"{item_location}.sha256")
        if sha256_bytes(resolved.read_bytes()) != declared_hash:
            raise ValueError(f"{item_location}.sha256: packet evidence digest drift")
        result.add(resolved)
    if len(result) != len(value):
        raise ValueError(f"{location}: packet verification evidence paths must be distinct")
    return result


def shares_filesystem_identity(path: Path, candidates: set[Path], location: str) -> bool:
    try:
        return any(os.path.samefile(path, candidate) for candidate in candidates)
    except OSError as exc:
        raise ValueError(f"{location}: cannot compare evidence file identity: {exc}") from exc


def validate_evidence(
    value: object,
    verification: dict[str, object],
    root: Path,
    forbidden: set[Path],
    packet_evidence: set[Path],
    required_authority_files: dict[str, str],
    required_authority_locators: set[str],
    packet_id: str,
    location: str,
) -> list[dict[str, object]]:
    if not isinstance(value, list) or len(value) != len(VERIFICATION_FIELDS):
        raise ValueError(f"{location}: exactly six records are required")
    categories: set[str] = set()
    artifacts: set[Path] = set()
    hashes: set[str] = set()
    producers: set[str] = set()
    normalized: list[dict[str, object]] = []
    forbidden_hashes = {
        sha256_bytes(path.read_bytes()) for path in forbidden if path.is_file()
    }
    packet_evidence_hashes = {
        sha256_bytes(path.read_bytes()) for path in packet_evidence
    }
    for index, untyped in enumerate(value):
        item_location = f"{location}[{index}]"
        if not isinstance(untyped, dict):
            raise ValueError(f"{item_location}: expected object")
        category = nonempty(untyped.get("category"), f"{item_location}.category")
        fields = AI_EVIDENCE_FIELDS if category in AI_VERIFICATION_FIELDS else MECHANICAL_EVIDENCE_FIELDS
        item = require_exact_fields(untyped, fields, item_location)
        if category not in VERIFICATION_FIELDS:
            raise ValueError(f"{item_location}.category: unknown category")
        if category in categories:
            raise ValueError(f"{item_location}.category: duplicate category")
        categories.add(category)
        if verification.get(category) != "pass" or item["recorded_result"] != "pass":
            raise ValueError(f"{item_location}: evidence and verification must pass")
        artifact_value, artifact = repo_file(root, item["artifact_path"], f"{item_location}.artifact_path")
        if artifact in artifacts or artifact in forbidden:
            raise ValueError(f"{item_location}.artifact_path: separate non-self evidence file required")
        if artifact in packet_evidence:
            raise ValueError(
                f"{item_location}.artifact_path: packet-declared verification evidence is forbidden"
            )
        if shares_filesystem_identity(artifact, forbidden, item_location):
            raise ValueError(
                f"{item_location}.artifact_path: self evidence filesystem identity is forbidden"
            )
        if shares_filesystem_identity(artifact, packet_evidence, item_location):
            raise ValueError(
                f"{item_location}.artifact_path: packet-declared verification evidence filesystem identity is forbidden"
            )
        artifacts.add(artifact)
        artifact_hash = sha(item["sha256"], f"{item_location}.sha256")
        if sha256_bytes(artifact.read_bytes()) != artifact_hash:
            raise ValueError(f"{item_location}.sha256: evidence SHA-256 drift")
        if artifact_hash in forbidden_hashes:
            raise ValueError(f"{item_location}.sha256: self evidence bytes are forbidden")
        if artifact_hash in packet_evidence_hashes:
            raise ValueError(
                f"{item_location}.sha256: packet-declared verification evidence bytes are forbidden"
            )
        if artifact_hash in hashes:
            raise ValueError(f"{item_location}.sha256: evidence bytes must be distinct")
        hashes.add(artifact_hash)
        producer = nonempty(item["producer_identity"], f"{item_location}.producer_identity")
        key = producer_key(producer)
        if key in producers:
            raise ValueError(f"{item_location}.producer_identity: distinct producers required")
        producers.add(key)
        scope = nonempty(item["recorded_scope"], f"{item_location}.recorded_scope")
        if packet_id not in scope.split():
            raise ValueError(f"{item_location}.recorded_scope: exact packet scope required")
        output: dict[str, object] = {
            "category": category,
            "recorded_result": "pass",
            "artifact_path": artifact_value,
            "sha256": artifact_hash,
            "producer_identity": producer,
            "recorded_scope": scope,
        }
        if category in AI_VERIFICATION_FIELDS:
            output["model"] = nonempty(item["model"], f"{item_location}.model")
            output["model_version"] = nonempty(item["model_version"], f"{item_location}.model_version")
            output["instructions"] = nonempty(item["instructions"], f"{item_location}.instructions")
            raw_files = item["consulted_authority_files"]
            if not isinstance(raw_files, list) or not raw_files:
                raise ValueError(f"{item_location}.consulted_authority_files: expected nonempty array")
            authority_files: list[dict[str, str]] = []
            for file_index, raw_file in enumerate(raw_files):
                file_location = f"{item_location}.consulted_authority_files[{file_index}]"
                file_record = require_exact_fields(raw_file, {"path", "sha256"}, file_location)
                path_value, path = repo_file(root, file_record["path"], f"{file_location}.path")
                path_hash = sha(file_record["sha256"], f"{file_location}.sha256")
                if sha256_bytes(path.read_bytes()) != path_hash:
                    raise ValueError(f"{file_location}.sha256: authority digest drift")
                authority_files.append({"path": path_value, "sha256": path_hash})
            if authority_files != sorted(authority_files, key=lambda item: item["path"]) or len({item["path"] for item in authority_files}) != len(authority_files):
                raise ValueError(f"{item_location}.consulted_authority_files: paths must be unique and sorted")
            actual_authorities = {
                item["path"]: item["sha256"] for item in authority_files
            }
            for required_path, required_hash in required_authority_files.items():
                if actual_authorities.get(required_path) != required_hash:
                    raise ValueError(
                        f"{item_location}.consulted_authority_files: packet authority is required"
                    )
            output["consulted_authority_files"] = authority_files
            authority_locators = sorted_strings(item["consulted_authority_locators"], f"{item_location}.consulted_authority_locators", nonempty_array=True)
            if not required_authority_locators.issubset(authority_locators):
                raise ValueError(
                    f"{item_location}.consulted_authority_locators: packet authority locator is required"
                )
            output["consulted_authority_locators"] = authority_locators
            output["findings"] = sorted_strings(item["findings"], f"{item_location}.findings", nonempty_array=True)
            evidence_digest = sha(item["evidence_digest"], f"{item_location}.evidence_digest")
            if evidence_digest != artifact_hash:
                raise ValueError(f"{item_location}.evidence_digest: must equal evidence artifact digest")
            output["evidence_digest"] = evidence_digest
        normalized.append(output)
    if categories != set(VERIFICATION_FIELDS):
        raise ValueError(f"{location}: every verification category is required")
    return normalized


def build_rows(
    root: Path,
    packet_root: Path,
    reviewed_path: Path,
    coverage_manifest: Path,
    register_manifest: Path,
) -> list[dict[str, str]]:
    root = root.resolve()
    packets = discover_packets(root, packet_root)
    document = require_exact_fields(
        load_json(reviewed_path, "reviewed packet-admission records"),
        {"schema_version", "packet_root", "records"},
        "reviewed packet-admission records",
    )
    if type(document["schema_version"]) is not int or document["schema_version"] != SCHEMA_VERSION:
        raise ValueError(f"reviewed packet-admission records.schema_version: must be {SCHEMA_VERSION}")
    if document["packet_root"] != PACKET_ROOT_VALUE:
        raise ValueError(f"reviewed packet-admission records.packet_root: must be {PACKET_ROOT_VALUE!r}")
    records = document["records"]
    if not isinstance(records, list):
        raise ValueError("reviewed packet-admission records.records: expected array")
    output: list[dict[str, str]] = []
    output_by_id: dict[str, dict[str, str]] = {}
    for packet_id in sorted(packets):
        packet_path, path, _packet = packets[packet_id]
        row = {
            "packet_id": packet_id,
            "packet_path": packet_path,
            "packet_sha256": sha256_bytes(path.read_bytes()),
            "admission_status": "OPEN",
            "authority_projection_sha256": "",
            "presentation_identity_projection_sha256": "",
            "content_projection_sha256": "",
            "present_content_item_ids": "[]",
            "destination_file": "",
            "destination_sha256": "",
            "destination_labels": "[]",
            **{f"{category}_verification": "pending" for category in VERIFICATION_FIELDS},
            "verification_evidence": "[]",
        }
        output.append(row)
        output_by_id[packet_id] = row
    seen: set[str] = set()
    previous_coverage = packet_checker.COVERAGE_MANIFEST
    previous_register = packet_checker.REGISTER_MANIFEST
    packet_checker.COVERAGE_MANIFEST = coverage_manifest
    packet_checker.REGISTER_MANIFEST = register_manifest
    try:
        for index, untyped in enumerate(records):
            location = f"reviewed packet-admission records.records[{index}]"
            record = require_exact_fields(untyped, RECORD_FIELDS, location)
            packet_id = nonempty(record["packet_id"], f"{location}.packet_id")
            if packet_id in seen:
                raise ValueError(f"{location}: duplicate packet ID {packet_id}")
            seen.add(packet_id)
            packet_entry = packets.get(packet_id)
            if packet_entry is None:
                raise ValueError(f"{location}: unknown packet ID {packet_id}")
            packet_path_value, packet_path, packet = packet_entry
            if record["packet_path"] != packet_path_value:
                raise ValueError(f"{location}.packet_path: packet path drift")
            packet_hash = sha(record["packet_sha256"], f"{location}.packet_sha256")
            if sha256_bytes(packet_path.read_bytes()) != packet_hash:
                raise ValueError(f"{location}.packet_sha256: packet SHA-256 drift")
            if record["admission_status"] != "admitted":
                raise ValueError(f"{location}.admission_status: terminal value 'admitted' required")
            errors = packet_checker.validate_packet(packet, base_dir=packet_path.parent, packet_path=packet_path)
            if errors:
                raise ValueError(f"{location}: packet validation failed: {errors[0]}")
            if packet.get("overall_status") != "verified":
                raise ValueError(f"{location}: packet is not verified")
            packet_evidence = packet_verification_evidence_paths(
                root, packet_path, packet, location
            )
            projections = {
                "authority_projection_sha256": canonical_digest(packet.get("authority")),
                "presentation_identity_projection_sha256": canonical_digest(packet.get("presentation_identity")),
                "content_projection_sha256": canonical_digest(packet.get("content")),
            }
            for field, expected in projections.items():
                if sha(record[field], f"{location}.{field}") != expected:
                    label = field.removesuffix("_sha256").replace("_", " ")
                    raise ValueError(f"{location}.{field}: {label} drift")
            item_ids = sorted_strings(record["present_content_item_ids"], f"{location}.present_content_item_ids", nonempty_array=True)
            if item_ids != present_item_ids(packet):
                raise ValueError(f"{location}.present_content_item_ids: must equal packet present items")
            destination = packet.get("destination")
            if not isinstance(destination, dict):
                raise ValueError(f"{location}: packet destination is invalid")
            destination_value, destination_path = repo_file(root, record["destination_file"], f"{location}.destination_file", prefix="handbook/")
            if destination_value != destination.get("file"):
                raise ValueError(f"{location}.destination_file: differs from packet")
            destination_hash = sha(record["destination_sha256"], f"{location}.destination_sha256")
            if sha256_bytes(destination_path.read_bytes()) != destination_hash:
                raise ValueError(f"{location}.destination_sha256: destination SHA-256 drift")
            labels = sorted_strings(record["destination_labels"], f"{location}.destination_labels", nonempty_array=True)
            if labels != sorted(destination.get("stable_labels", [])):
                raise ValueError(f"{location}.destination_labels: differs from packet")
            text = destination_path.read_text(encoding="utf-8")
            for label in labels:
                if text.count(f"\\label{{{label}}}") != 1:
                    raise ValueError(f"{location}.destination_labels: label {label!r} does not resolve exactly once")
            authority = packet.get("authority")
            if not isinstance(authority, dict):
                raise ValueError(f"{location}: packet authority is invalid")
            authority_local = nonempty(
                authority.get("local_path"), f"{location}.packet_authority.local_path"
            )
            authority_candidate = packet_path.parent / authority_local
            authority_absolute = Path(os.path.abspath(authority_candidate))
            authority_path = authority_candidate.resolve()
            if authority_absolute != authority_path:
                raise ValueError(f"{location}: packet authority uses symlink or junction indirection")
            try:
                authority_value = authority_path.relative_to(root).as_posix()
            except ValueError as exc:
                raise ValueError(f"{location}: packet authority leaves repository") from exc
            if not authority_path.is_file():
                raise ValueError(f"{location}: packet authority file is missing")
            authority_hash = sha(
                authority.get("source_sha256"),
                f"{location}.packet_authority.source_sha256",
            )
            if sha256_bytes(authority_path.read_bytes()) != authority_hash:
                raise ValueError(f"{location}: packet authority digest drift")
            authority_locator = nonempty(
                authority.get("exact_locator"),
                f"{location}.packet_authority.exact_locator",
            )
            verification = require_exact_fields(record["verification"], set(VERIFICATION_FIELDS), f"{location}.verification")
            if any(verification[field] != "pass" for field in VERIFICATION_FIELDS):
                raise ValueError(f"{location}.verification: every category must pass")
            evidence = validate_evidence(
                record["verification_evidence"],
                verification,
                root,
                {reviewed_path.resolve(), packet_path, destination_path, authority_path},
                packet_evidence,
                {authority_value: authority_hash},
                {authority_locator},
                packet_id,
                f"{location}.verification_evidence",
            )
            row = output_by_id[packet_id]
            row.update(
                {
                    "packet_sha256": packet_hash,
                    "admission_status": "ADMITTED",
                    **projections,
                    "present_content_item_ids": json.dumps(item_ids, separators=(",", ":")),
                    "destination_file": destination_value,
                    "destination_sha256": destination_hash,
                    "destination_labels": json.dumps(labels, separators=(",", ":")),
                    **{f"{category}_verification": "pass" for category in VERIFICATION_FIELDS},
                    "verification_evidence": json.dumps(evidence, ensure_ascii=False, separators=(",", ":")),
                }
            )
    finally:
        packet_checker.COVERAGE_MANIFEST = previous_coverage
        packet_checker.REGISTER_MANIFEST = previous_register
    return output


def csv_bytes(rows: list[dict[str, str]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=OUTPUT_FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def markdown_bytes(rows: list[dict[str, str]]) -> bytes:
    admitted = sum(row["admission_status"] == "ADMITTED" for row in rows)
    lines = [
        "# Presentation-packet content admission",
        "",
        "Generated by `tools/build_presentation_packet_admission.py`; do not edit by hand.",
        "",
        f"- Packet files: {len(rows):,}.",
        f"- Independently admitted: {admitted:,}.",
        f"- OPEN: {len(rows) - admitted:,}.",
        "",
        "## Why this separate administrative record exists",
        "",
        "- **Necessity:** packet structural validity cannot state that separately scoped",
        "  reviews admitted its maintained content into the compendium.",
        "- **Definition:** a packet is admitted exactly when one terminal reviewed record",
        "  pins its bytes, authority, presentation identity, complete content projection,",
        "  present content-item IDs, destination bytes and labels, and all six evidence gates.",
        "- **Standing:** this is a metalinguistic administrative projection, not logical content.",
        "- **Nonredundancy:** a packet records a presentation; this projection records the",
        "  independent decision that the exact packet and maintained destination passed admission.",
        "- **Use:** streamed external assignments and terminal readiness may rely only on",
        "  packets recorded here as `ADMITTED`.",
        "",
    ]
    return "\n".join(lines).encode("utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--packet-root", type=Path, default=DEFAULT_PACKET_ROOT)
    parser.add_argument("--reviewed-records", type=Path, default=DEFAULT_REVIEWED)
    parser.add_argument("--coverage-manifest", type=Path, default=DEFAULT_COVERAGE)
    parser.add_argument("--register-manifest", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MD)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        rows = build_rows(
            args.repository_root,
            args.packet_root,
            args.reviewed_records,
            args.coverage_manifest,
            args.register_manifest,
        )
        outputs = ((args.csv, csv_bytes(rows)), (args.markdown, markdown_bytes(rows)))
        for path, raw in outputs:
            if args.check:
                if not path.is_file() or path.read_bytes() != raw:
                    raise ValueError(f"stale generated artifact: {path}")
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(raw)
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        print(f"presentation-packet admission: FAIL ({exc})", file=sys.stderr)
        return 1
    admitted = sum(row["admission_status"] == "ADMITTED" for row in rows)
    print(
        f"presentation-packet admission: {'verified' if args.check else 'wrote'} "
        f"{len(rows)} rows; admitted={admitted} open={len(rows) - admitted}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
