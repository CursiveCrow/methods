#!/usr/bin/env python3
"""Validate presentation packet structure and evidence integrity.

The checker intentionally uses only the Python standard library.  The JSON
Schema remains the interchange contract; these checks enforce the same strict
shape plus status-dependent rules used by the compendium workflow.  A pass is
not a judgment that source locators, reconstructions, non-applicability claims,
or AI-review findings are true.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import sys
import tempfile
from functools import lru_cache
from pathlib import Path
from typing import Any


# Acquisition source rows can legitimately carry hundreds of exact locators.
csv.field_size_limit(2_147_483_647)


SCHEMA_VERSION = 2

CONTENT_KEYS = (
    "notation_roles",
    "conventions",
    "syntax",
    "definitions",
    "axioms",
    "calculi",
    "rules",
    "side_conditions",
    "semantic_clauses",
    "statements",
    "hypotheses",
    "results",
    "proofs",
    "proof_boundaries",
    "examples",
    "counterexamples",
    "exercises",
    "exercise_solutions",
    "exercise_feedback",
    "warnings",
    "qualifications",
    "tables",
    "source_attributions",
)

COMPLETENESS_KEYS = (
    "notation",
    "conventions",
    "syntax",
    "definitions",
    "axioms",
    "calculi",
    "rules",
    "side_conditions",
    "semantic_clauses",
    "hypotheses",
    "statements",
    "results",
    "proofs",
    "proof_boundaries",
    "examples",
    "counterexamples",
    "exercises",
    "exercise_solutions",
    "exercise_feedback",
    "warnings",
    "qualifications",
    "tables",
    "attribution",
)

VERIFICATION_KEYS = (
    "source_fidelity_ai",
    "topic_specialist_ai",
    "adversarial_publication_ai",
    "static",
    "build",
    "visual",
)
AI_VERIFICATION_KEYS = VERIFICATION_KEYS[:3]
MECHANICAL_EVIDENCE_FIELDS = {
    "kind",
    "artifact_path",
    "sha256",
    "verifier_identity",
    "verification_scope",
    "independently_produced",
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
DIMENSION_RESULTS = {"pending", "pass", "fail"}

TOP_KEYS = {
    "schema_version",
    "packet_id",
    "overall_status",
    "authority",
    "presentation_identity",
    "reconstruction_mode",
    "content",
    "technical_names",
    "variants",
    "obligation_links",
    "destination",
    "completeness",
    "verification",
    "verification_evidence",
    "owed_artifacts",
}

REPO_ROOT = Path(__file__).resolve().parent.parent
COVERAGE_MANIFEST = REPO_ROOT / "spec" / "full-compendium-coverage-manifest.csv"
REGISTER_MANIFEST = REPO_ROOT / "spec" / "register-obligation-manifest.csv"
SHA256_LENGTH = 64

FORBIDDEN_TRUE_FLAGS = {
    "house_selected",
    "house_selection",
    "selected",
    "selection",
    "synthesized",
    "hybrid",
    "hybridized",
}


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_sha256(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == SHA256_LENGTH
        and all(character in "0123456789abcdef" for character in value)
    )


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _resolve_artifact(raw_path: str, base_dir: Path) -> Path:
    path = Path(raw_path)
    return path if path.is_absolute() else base_dir / path


def _check_file_digest(
    raw_path: Any,
    expected_digest: Any,
    path: str,
    base_dir: Path,
    errors: list[str],
    path_field: str = "artifact_path",
) -> None:
    if not _nonempty_string(raw_path):
        errors.append(f"{path}.{path_field}: expected nonempty string")
        return
    if not _is_sha256(expected_digest):
        errors.append(f"{path}.sha256: expected lowercase SHA-256")
        return
    artifact = _resolve_artifact(raw_path, base_dir)
    if not artifact.is_file():
        errors.append(f"{path}.{path_field}: file not found: {artifact}")
        return
    try:
        actual_digest = _sha256_bytes(artifact.read_bytes())
    except OSError as exc:
        errors.append(f"{path}.{path_field}: could not read {artifact}: {exc}")
        return
    if actual_digest != expected_digest:
        errors.append(
            f"{path}.sha256: digest mismatch for {artifact}; "
            f"expected {expected_digest}, got {actual_digest}"
        )


def _check_exact_keys(
    value: Any,
    path: str,
    required: set[str],
    allowed: set[str],
    errors: list[str],
) -> bool:
    if not isinstance(value, dict):
        errors.append(f"{path}: expected object")
        return False
    missing = sorted(required - set(value))
    extra = sorted(set(value) - allowed)
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(missing)}")
    if extra:
        errors.append(f"{path}: unknown fields: {', '.join(extra)}")
    return not missing


def _require_nonempty_strings(
    value: dict[str, Any], path: str, keys: set[str], errors: list[str]
) -> None:
    for key in sorted(keys):
        if key in value and not _nonempty_string(value[key]):
            errors.append(f"{path}.{key}: expected nonempty string")


def _check_forbidden_flags(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key in FORBIDDEN_TRUE_FLAGS and child is True:
                errors.append(f"{child_path}: selection, synthesis, and hybrid flags must be false")
            _check_forbidden_flags(child, child_path, errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _check_forbidden_flags(child, f"{path}[{index}]", errors)


def _check_authority(
    value: Any, verified: bool, base_dir: Path, errors: list[str]
) -> None:
    required = {"work", "edition", "exact_locator"}
    allowed = required | {"url", "local_path", "source_sha256"}
    if not _check_exact_keys(value, "authority", required, allowed, errors):
        return
    assert isinstance(value, dict)
    _require_nonempty_strings(value, "authority", required, errors)
    sources = [value.get("url"), value.get("local_path")]
    if not any(_nonempty_string(source) for source in sources):
        errors.append("authority: at least one nonempty url or local_path is required")
    for key in ("url", "local_path"):
        if key in value and not _nonempty_string(value[key]):
            errors.append(f"authority.{key}: expected nonempty string")
    if "source_sha256" in value and not _is_sha256(value["source_sha256"]):
        errors.append("authority.source_sha256: expected lowercase SHA-256")
    if verified:
        if not _nonempty_string(value.get("local_path")):
            errors.append("authority.local_path: verified packet requires a local source snapshot")
        elif _is_sha256(value.get("source_sha256")):
            _check_file_digest(
                value["local_path"],
                value["source_sha256"],
                "authority",
                base_dir,
                errors,
                "local_path",
            )
        else:
            errors.append("authority.source_sha256: verified packet requires a source digest")


def _check_identity(value: Any, verified: bool, errors: list[str]) -> str | None:
    flags = {"house_selected", "synthesized", "hybrid"}
    required = {"identity_status"} | flags
    allowed = required | {"source_given_name", "exact_eliminable_description"}
    if not _check_exact_keys(
        value, "presentation_identity", required, allowed, errors
    ):
        return None
    assert isinstance(value, dict)
    identity_status = value.get("identity_status")
    if identity_status not in {"unresolved", "identified"}:
        errors.append("presentation_identity.identity_status: expected unresolved or identified")
    has_identity = any(
        _nonempty_string(value.get(key))
        for key in ("source_given_name", "exact_eliminable_description")
    )
    if identity_status == "identified" and not has_identity:
        errors.append(
            "presentation_identity: identified status requires source_given_name "
            "or exact_eliminable_description"
        )
    if identity_status == "unresolved" and has_identity:
        errors.append(
            "presentation_identity: unresolved status cannot assert a name or description"
        )
    if verified and identity_status != "identified":
        errors.append("presentation_identity.identity_status: verified packet requires identified")
    for key in ("source_given_name", "exact_eliminable_description"):
        if key in value and not _nonempty_string(value[key]):
            errors.append(f"presentation_identity.{key}: expected nonempty string")
    for flag in sorted(flags):
        if value.get(flag) is not False:
            errors.append(f"presentation_identity.{flag}: must be false")
    return identity_status if isinstance(identity_status, str) else None


def _check_content_item(
    value: Any, path: str, base_dir: Path, errors: list[str]
) -> bool:
    if not isinstance(value, dict):
        errors.append(f"{path}: expected object")
        return False
    status = value.get("status")
    if status == "present":
        required = {"item_id", "status", "source_locator", "content_digest"}
        allowed = required | {
            "text",
            "artifact_path",
            "content_digest",
            "attribution_note",
        }
        _check_exact_keys(value, path, required, allowed, errors)
        _require_nonempty_strings(value, path, required - {"status"}, errors)
        present_bodies = sum(
            _nonempty_string(value.get(key)) for key in ("text", "artifact_path")
        )
        if present_bodies != 1:
            errors.append(f"{path}: present item requires exactly one of text or artifact_path")
        for key in ("text", "artifact_path", "content_digest", "attribution_note"):
            if key in value and not _nonempty_string(value[key]):
                errors.append(f"{path}.{key}: expected nonempty string")
        digest = value.get("content_digest")
        if not _is_sha256(digest):
            errors.append(f"{path}.content_digest: expected lowercase SHA-256")
        elif _nonempty_string(value.get("text")):
            actual = _sha256_bytes(value["text"].encode("utf-8"))
            if actual != digest:
                errors.append(
                    f"{path}.content_digest: inline-text digest mismatch; "
                    f"expected {digest}, got {actual}"
                )
        elif _nonempty_string(value.get("artifact_path")):
            _check_file_digest(
                value["artifact_path"], digest, path, base_dir, errors
            )
        return True
    elif status == "not_applicable":
        required = {"item_id", "status", "source_locator", "source_justification"}
        _check_exact_keys(value, path, required, required, errors)
        _require_nonempty_strings(value, path, required - {"status"}, errors)
        return False
    else:
        errors.append(f"{path}.status: expected present or not_applicable")
        return False


def _check_content(
    value: Any, has_owed: bool, base_dir: Path, errors: list[str]
) -> tuple[int, dict[str, str], set[str]]:
    required = set(CONTENT_KEYS)
    if not _check_exact_keys(value, "content", required, required, errors):
        return 0, {}, set()
    assert isinstance(value, dict)
    substantive_present_count = 0
    item_categories: dict[str, str] = {}
    present_item_ids: set[str] = set()
    for key in CONTENT_KEYS:
        items = value.get(key)
        path = f"content.{key}"
        if not isinstance(items, list):
            errors.append(f"{path}: expected array")
            continue
        if not items and not has_owed:
            errors.append(
                f"{path}: empty arrays require a corresponding open packet with owed_artifacts"
            )
        for index, item in enumerate(items):
            is_present = _check_content_item(
                item, f"{path}[{index}]", base_dir, errors
            )
            if isinstance(item, dict) and _nonempty_string(item.get("item_id")):
                item_id = item["item_id"]
                if item_id in item_categories:
                    errors.append(
                        f"{path}[{index}].item_id: duplicate content item id "
                        f"{item_id}; first used in content.{item_categories[item_id]}"
                    )
                else:
                    item_categories[item_id] = key
                if is_present:
                    present_item_ids.add(item_id)
            if is_present and key != "source_attributions":
                substantive_present_count += 1
    return substantive_present_count, item_categories, present_item_ids


def _check_technical_names(value: Any, errors: list[str]) -> None:
    if not isinstance(value, list):
        errors.append("technical_names: expected array")
        return
    fields = {
        "name",
        "necessity",
        "definition_or_axiom",
        "standing",
        "nonredundancy",
        "use",
    }
    for index, item in enumerate(value):
        path = f"technical_names[{index}]"
        if _check_exact_keys(item, path, fields, fields, errors):
            assert isinstance(item, dict)
            _require_nonempty_strings(item, path, fields, errors)


def _check_variants(value: Any, errors: list[str]) -> None:
    if not isinstance(value, list):
        errors.append("variants: expected array")
        return
    fields = {"related_packet_id", "source_locator", "source_stated_relation"}
    for index, item in enumerate(value):
        path = f"variants[{index}]"
        if _check_exact_keys(item, path, fields, fields, errors):
            assert isinstance(item, dict)
            _require_nonempty_strings(item, path, fields, errors)


def _manifest_fingerprint(path: Path) -> tuple[int, int, int, int, int]:
    stat = path.stat()
    return (
        stat.st_dev,
        stat.st_ino,
        stat.st_size,
        stat.st_mtime_ns,
        stat.st_ctime_ns,
    )


@lru_cache(maxsize=16)
def _cached_manifest_ids(
    resolved_path: str,
    field: str,
    fingerprint: tuple[int, int, int, int, int],
) -> frozenset[str]:
    path = Path(resolved_path)
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if field not in (reader.fieldnames or []):
            raise ValueError(f"missing {field} column")
        identifiers = frozenset(
            row[field].strip()
            for row in reader
            if row.get(field) and row[field].strip()
        )
    if _manifest_fingerprint(path) != fingerprint:
        raise OSError("manifest changed while its identifiers were being read")
    return identifiers


def _manifest_ids(path: Path, field: str, errors: list[str]) -> frozenset[str]:
    try:
        resolved = path.resolve(strict=True)
        fingerprint = _manifest_fingerprint(resolved)
        return _cached_manifest_ids(str(resolved), field, fingerprint)
    except (OSError, ValueError, csv.Error) as exc:
        errors.append(f"manifest {path}: could not read: {exc}")
        return frozenset()


def _run_manifest_id_cache_self_test(base_dir: Path) -> None:
    first = base_dir / "manifest-cache-first.csv"
    second = base_dir / "manifest-cache-second.csv"
    first.write_text("stable_id,value\nSRC-001,one\n", encoding="utf-8", newline="")
    second.write_text("stable_id,value\nSRC-002,two\n", encoding="utf-8", newline="")
    _cached_manifest_ids.cache_clear()

    errors: list[str] = []
    if _manifest_ids(first, "stable_id", errors) != frozenset({"SRC-001"}) or errors:
        raise AssertionError(f"initial manifest cache read failed: {errors!r}")
    hits_before = _cached_manifest_ids.cache_info().hits
    alias = first.parent / "." / first.name
    if _manifest_ids(alias, "stable_id", errors) != frozenset({"SRC-001"}) or errors:
        raise AssertionError(f"resolved-path manifest cache read failed: {errors!r}")
    if _cached_manifest_ids.cache_info().hits != hits_before + 1:
        raise AssertionError("same resolved manifest snapshot did not use the cache")

    if _manifest_ids(second, "stable_id", errors) != frozenset({"SRC-002"}) or errors:
        raise AssertionError("distinct manifest paths shared cached identifiers")

    first.write_text(
        "stable_id,value\nSRC-003,changed-size\n",
        encoding="utf-8",
        newline="",
    )
    if _manifest_ids(first, "stable_id", errors) != frozenset({"SRC-003"}) or errors:
        raise AssertionError("changed manifest fingerprint reused stale identifiers")

    missing_field = _manifest_ids(first, "obligation_id", errors)
    if missing_field or not errors or "missing obligation_id column" not in errors[-1]:
        raise AssertionError("missing manifest-ID column did not fail closed")
    _cached_manifest_ids.cache_clear()


def _check_obligation_assignments(
    assignments: Any,
    path: str,
    known_ids: set[str] | frozenset[str],
    item_categories: dict[str, str],
    present_item_ids: set[str],
    owed_artifact_ids: set[str],
    verified: bool,
    errors: list[str],
    require_nonempty: bool,
) -> set[str]:
    if not isinstance(assignments, list):
        errors.append(f"{path}: expected array")
        return set()
    if require_nonempty and not assignments:
        errors.append(f"{path}: expected nonempty array")

    fields = {
        "obligation_id",
        "assignment_status",
        "source_locator",
        "present_content_item_ids",
        "owed_artifact_ids",
    }
    assigned_ids: set[str] = set()
    for index, assignment in enumerate(assignments):
        item_path = f"{path}[{index}]"
        if not _check_exact_keys(assignment, item_path, fields, fields, errors):
            continue
        assert isinstance(assignment, dict)
        _require_nonempty_strings(
            assignment, item_path, {"obligation_id", "source_locator"}, errors
        )
        obligation_id = assignment.get("obligation_id")
        if _nonempty_string(obligation_id):
            if obligation_id in assigned_ids:
                errors.append(f"{item_path}.obligation_id: duplicate assignment {obligation_id}")
            assigned_ids.add(obligation_id)
            if obligation_id not in known_ids:
                errors.append(f"{item_path}.obligation_id: unknown manifest id {obligation_id}")

        status = assignment.get("assignment_status")
        if status not in {"open", "fulfilled"}:
            errors.append(f"{item_path}.assignment_status: expected open or fulfilled")
        if verified and status != "fulfilled":
            errors.append(
                f"{item_path}.assignment_status: verified packet requires fulfilled"
            )

        content_ids = assignment.get("present_content_item_ids")
        owed_ids = assignment.get("owed_artifact_ids")
        if not isinstance(content_ids, list):
            errors.append(f"{item_path}.present_content_item_ids: expected array")
            content_ids = []
        if not isinstance(owed_ids, list):
            errors.append(f"{item_path}.owed_artifact_ids: expected array")
            owed_ids = []
        for field, identifiers in (
            ("present_content_item_ids", content_ids),
            ("owed_artifact_ids", owed_ids),
        ):
            if any(not _nonempty_string(identifier) for identifier in identifiers):
                errors.append(f"{item_path}.{field}: every identifier must be nonempty")
            if len(identifiers) != len(set(identifiers)):
                errors.append(f"{item_path}.{field}: duplicate identifiers are not allowed")

        for item_id in content_ids:
            if _nonempty_string(item_id) and item_id not in item_categories:
                errors.append(
                    f"{item_path}.present_content_item_ids: unknown content item id {item_id}"
                )
            elif _nonempty_string(item_id) and item_id not in present_item_ids:
                errors.append(
                    f"{item_path}.present_content_item_ids: item {item_id} is not present"
                )
        for artifact_id in owed_ids:
            if _nonempty_string(artifact_id) and artifact_id not in owed_artifact_ids:
                errors.append(
                    f"{item_path}.owed_artifact_ids: unknown owed artifact id {artifact_id}"
                )

        if status == "fulfilled":
            if not content_ids:
                errors.append(
                    f"{item_path}.present_content_item_ids: fulfilled assignment "
                    "requires at least one present content item"
                )
            if owed_ids:
                errors.append(
                    f"{item_path}.owed_artifact_ids: fulfilled assignment must have none"
                )
            if content_ids and not any(
                item_id in present_item_ids
                and item_categories.get(item_id) != "source_attributions"
                for item_id in content_ids
            ):
                errors.append(
                    f"{item_path}.present_content_item_ids: attribution-only references "
                    "cannot fulfill an obligation"
                )
        elif status == "open":
            if content_ids:
                errors.append(
                    f"{item_path}.present_content_item_ids: open assignment must have none"
                )
            if not owed_ids:
                errors.append(
                    f"{item_path}.owed_artifact_ids: open assignment requires at least "
                    "one owed artifact"
                )
    return assigned_ids


def _check_obligation_links(
    value: Any,
    item_categories: dict[str, str],
    present_item_ids: set[str],
    owed_artifact_ids: set[str],
    verified: bool,
    errors: list[str],
) -> None:
    fields = {"coverage_assignments", "register_assignments"}
    if not _check_exact_keys(value, "obligation_links", fields, fields, errors):
        return
    assert isinstance(value, dict)
    coverage_known = _manifest_ids(COVERAGE_MANIFEST, "stable_id", errors)
    register_known = _manifest_ids(REGISTER_MANIFEST, "obligation_id", errors)
    _check_obligation_assignments(
        value.get("coverage_assignments"),
        "obligation_links.coverage_assignments",
        coverage_known,
        item_categories,
        present_item_ids,
        owed_artifact_ids,
        verified,
        errors,
        require_nonempty=True,
    )
    _check_obligation_assignments(
        value.get("register_assignments"),
        "obligation_links.register_assignments",
        register_known,
        item_categories,
        present_item_ids,
        owed_artifact_ids,
        verified,
        errors,
        require_nonempty=False,
    )


def _check_destination(value: Any, errors: list[str]) -> None:
    fields = {"file", "stable_labels"}
    if not _check_exact_keys(value, "destination", fields, fields, errors):
        return
    assert isinstance(value, dict)
    if not _nonempty_string(value.get("file")):
        errors.append("destination.file: expected nonempty string")
    labels = value.get("stable_labels")
    if not isinstance(labels, list) or not labels:
        errors.append("destination.stable_labels: expected nonempty array")
    elif any(not _nonempty_string(label) for label in labels):
        errors.append("destination.stable_labels: every label must be a nonempty string")
    elif len(labels) != len(set(labels)):
        errors.append("destination.stable_labels: duplicate labels are not allowed")


def _check_dimensions(
    value: Any, path: str, keys: tuple[str, ...], errors: list[str]
) -> None:
    fields = set(keys)
    if not _check_exact_keys(value, path, fields, fields, errors):
        return
    assert isinstance(value, dict)
    for key in keys:
        if value.get(key) not in DIMENSION_RESULTS:
            errors.append(f"{path}.{key}: expected pending, pass, or fail")


def _check_verification_evidence(
    value: Any,
    verified: bool,
    base_dir: Path,
    packet_path: Path | None,
    errors: list[str],
) -> set[str]:
    if not isinstance(value, list):
        errors.append("verification_evidence: expected array")
        return set()
    kinds: set[str] = set()
    artifact_paths: set[Path] = set()
    for index, item in enumerate(value):
        path = f"verification_evidence[{index}]"
        raw_kind = item.get("kind") if isinstance(item, dict) else None
        fields = (
            AI_EVIDENCE_FIELDS
            if raw_kind in AI_VERIFICATION_KEYS
            else MECHANICAL_EVIDENCE_FIELDS
        )
        if not _check_exact_keys(item, path, fields, fields, errors):
            continue
        assert isinstance(item, dict)
        _require_nonempty_strings(
            item,
            path,
            {"artifact_path", "verifier_identity", "verification_scope"},
            errors,
        )
        kind = item.get("kind")
        if kind not in VERIFICATION_KEYS:
            errors.append(
                f"{path}.kind: expected one of {', '.join(VERIFICATION_KEYS)}"
            )
        else:
            if kind in kinds:
                errors.append(f"{path}.kind: duplicate evidence kind {kind}")
            kinds.add(kind)
        if item.get("independently_produced") is not True:
            errors.append(f"{path}.independently_produced: must be true")
        raw_artifact = item.get("artifact_path")
        if _nonempty_string(raw_artifact):
            resolved = _resolve_artifact(raw_artifact, base_dir).resolve()
            if resolved in artifact_paths:
                errors.append(
                    f"{path}.artifact_path: every verification dimension requires "
                    "a separately produced evidence file"
                )
            artifact_paths.add(resolved)
            if packet_path is not None and resolved == packet_path.resolve():
                errors.append(
                    f"{path}.artifact_path: packet cannot serve as its own evidence"
                )
        _check_file_digest(
            item.get("artifact_path"),
            item.get("sha256"),
            path,
            base_dir,
            errors,
        )
        if kind in AI_VERIFICATION_KEYS:
            _require_nonempty_strings(
                item,
                path,
                {"model", "model_version", "instructions"},
                errors,
            )
            authority_files = item.get("consulted_authority_files")
            if not isinstance(authority_files, list) or not authority_files:
                errors.append(
                    f"{path}.consulted_authority_files: expected nonempty array"
                )
            else:
                seen_authority_paths: set[Path] = set()
                previous_authority_path = ""
                for authority_index, authority in enumerate(authority_files):
                    authority_path = (
                        f"{path}.consulted_authority_files[{authority_index}]"
                    )
                    authority_fields = {"path", "sha256"}
                    if not _check_exact_keys(
                        authority,
                        authority_path,
                        authority_fields,
                        authority_fields,
                        errors,
                    ):
                        continue
                    assert isinstance(authority, dict)
                    _require_nonempty_strings(
                        authority, authority_path, {"path"}, errors
                    )
                    raw_path = authority.get("path")
                    if _nonempty_string(raw_path):
                        resolved = _resolve_artifact(raw_path, base_dir).resolve()
                        if resolved in seen_authority_paths:
                            errors.append(
                                f"{path}.consulted_authority_files: duplicate path"
                            )
                        seen_authority_paths.add(resolved)
                        if raw_path < previous_authority_path:
                            errors.append(
                                f"{path}.consulted_authority_files: values must be "
                                "sorted by path"
                            )
                        previous_authority_path = raw_path
                    _check_file_digest(
                        authority.get("path"),
                        authority.get("sha256"),
                        authority_path,
                        base_dir,
                        errors,
                    )
            for field in (
                "consulted_authority_locators",
                "findings",
            ):
                strings = item.get(field)
                field_path = f"{path}.{field}"
                if (
                    not isinstance(strings, list)
                    or not strings
                    or any(not _nonempty_string(entry) for entry in strings)
                ):
                    errors.append(f"{field_path}: expected nonempty string array")
                elif strings != sorted(set(strings)):
                    errors.append(f"{field_path}: values must be unique and sorted")
            evidence_digest = item.get("evidence_digest")
            if not _is_sha256(evidence_digest):
                errors.append(f"{path}.evidence_digest: expected lowercase SHA-256")
            elif evidence_digest != item.get("sha256"):
                errors.append(
                    f"{path}.evidence_digest: must equal the review evidence "
                    "artifact digest"
                )
    if verified:
        missing = sorted(set(VERIFICATION_KEYS) - kinds)
        if missing:
            errors.append(
                "verification_evidence: verified packet lacks evidence for "
                + ", ".join(missing)
            )
    return kinds


def _check_owed_artifacts(value: Any, errors: list[str]) -> tuple[list[Any], set[str]]:
    if not isinstance(value, list):
        errors.append("owed_artifacts: expected array")
        return [], set()
    fields = {
        "artifact_id",
        "artifact_kind",
        "description",
        "source_obligation",
        "completion_condition",
    }
    artifact_ids: set[str] = set()
    for index, item in enumerate(value):
        path = f"owed_artifacts[{index}]"
        if _check_exact_keys(item, path, fields, fields, errors):
            assert isinstance(item, dict)
            _require_nonempty_strings(item, path, fields - {"artifact_kind"}, errors)
            artifact_id = item.get("artifact_id")
            if _nonempty_string(artifact_id):
                if artifact_id in artifact_ids:
                    errors.append(f"{path}.artifact_id: duplicate owed artifact id {artifact_id}")
                artifact_ids.add(artifact_id)
            if item.get("artifact_kind") not in {
                "presentation_identity",
                "authority",
                "content",
                "destination",
                "variant_relation",
                "verification",
                "other",
            }:
                errors.append(f"{path}.artifact_kind: unknown owed-artifact kind")
    return value, artifact_ids


def validate_packet(
    packet: Any,
    base_dir: Path | None = None,
    packet_path: Path | None = None,
) -> list[str]:
    """Return structural and referenced-artifact integrity errors.

    This function cannot establish source fidelity, completeness, correctness,
    reviewer independence, or the truth of a not-applicable justification.
    """

    errors: list[str] = []
    if base_dir is None:
        base_dir = Path.cwd()
    if not _check_exact_keys(packet, "$", TOP_KEYS, TOP_KEYS, errors):
        return errors
    assert isinstance(packet, dict)

    if (
        type(packet.get("schema_version")) is not int
        or packet["schema_version"] != SCHEMA_VERSION
    ):
        errors.append(f"schema_version: must be integer {SCHEMA_VERSION}")
    if not _nonempty_string(packet.get("packet_id")):
        errors.append("packet_id: expected nonempty string")

    overall_status = packet.get("overall_status")
    if overall_status not in {"open", "verified"}:
        errors.append("overall_status: expected open or verified")

    reconstruction_mode = packet.get("reconstruction_mode")
    if reconstruction_mode not in {
        "full_transcription",
        "full_reconstruction",
        "open_missing",
    }:
        errors.append(
            "reconstruction_mode: expected full_transcription, "
            "full_reconstruction, or open_missing"
        )

    verified = overall_status == "verified"
    _check_authority(packet.get("authority"), verified, base_dir, errors)
    identity_status = _check_identity(
        packet.get("presentation_identity"), verified, errors
    )
    owed, owed_artifact_ids = _check_owed_artifacts(
        packet.get("owed_artifacts"), errors
    )
    substantive_present_count, item_categories, present_item_ids = _check_content(
        packet.get("content"), bool(owed), base_dir, errors
    )
    _check_technical_names(packet.get("technical_names"), errors)
    _check_variants(packet.get("variants"), errors)
    _check_obligation_links(
        packet.get("obligation_links"),
        item_categories,
        present_item_ids,
        owed_artifact_ids,
        verified,
        errors,
    )
    _check_destination(packet.get("destination"), errors)
    _check_dimensions(
        packet.get("completeness"), "completeness", COMPLETENESS_KEYS, errors
    )
    _check_dimensions(
        packet.get("verification"), "verification", VERIFICATION_KEYS, errors
    )
    _check_verification_evidence(
        packet.get("verification_evidence"),
        verified,
        base_dir,
        packet_path,
        errors,
    )
    _check_forbidden_flags(packet, "$", errors)

    if overall_status == "open" and not owed:
        errors.append("owed_artifacts: an open packet requires at least one owed artifact")
    if overall_status == "open" and identity_status == "unresolved":
        identity_is_owed = any(
            isinstance(item, dict)
            and item.get("artifact_kind") == "presentation_identity"
            for item in owed
        )
        if not identity_is_owed:
            errors.append(
                "owed_artifacts: unresolved presentation identity requires a "
                "presentation_identity owed artifact"
            )

    if overall_status == "verified":
        if owed:
            errors.append("owed_artifacts: a verified packet must have none")
        if reconstruction_mode == "open_missing":
            errors.append("reconstruction_mode: verified packet cannot be open_missing")
        if substantive_present_count < 1:
            errors.append(
                "content: verified packet requires at least one substantive present "
                "item outside source_attributions; attribution-only and "
                "all-not_applicable packets fail closed"
            )
        completeness = packet.get("completeness")
        if isinstance(completeness, dict):
            for key in COMPLETENESS_KEYS:
                if completeness.get(key) != "pass":
                    errors.append(f"completeness.{key}: verified packet requires pass")
        verification = packet.get("verification")
        if isinstance(verification, dict):
            for key in VERIFICATION_KEYS:
                if verification.get(key) != "pass":
                    errors.append(f"verification.{key}: verified packet requires pass")

    return errors


def _open_fixture() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "packet_id": "open.self-test",
        "overall_status": "open",
        "authority": {
            "work": "Self-test authority",
            "edition": "Self-test edition",
            "exact_locator": "Self-test locator",
            "local_path": "self-test-source",
        },
        "presentation_identity": {
            "identity_status": "unresolved",
            "house_selected": False,
            "synthesized": False,
            "hybrid": False,
        },
        "reconstruction_mode": "open_missing",
        "content": {key: [] for key in CONTENT_KEYS},
        "technical_names": [],
        "variants": [],
        "obligation_links": {
            "coverage_assignments": [
                {
                    "obligation_id": "SRC-001",
                    "assignment_status": "open",
                    "source_locator": "Self-test source acquisition record SRC-001",
                    "present_content_item_ids": [],
                    "owed_artifact_ids": ["owed.content"],
                }
            ],
            "register_assignments": [],
        },
        "destination": {
            "file": "handbook/self-test.tex",
            "stable_labels": ["packet:self-test"],
        },
        "completeness": {key: "pending" for key in COMPLETENESS_KEYS},
        "verification": {key: "pending" for key in VERIFICATION_KEYS},
        "verification_evidence": [],
        "owed_artifacts": [
            {
                "artifact_id": "owed.identity",
                "artifact_kind": "presentation_identity",
                "description": "Establish the source presentation identity.",
                "source_obligation": "Use a source-given name or exact description.",
                "completion_condition": "Record an identified source-bound identity.",
            },
            {
                "artifact_id": "owed.content",
                "artifact_kind": "content",
                "description": "Gather the identified presentation.",
                "source_obligation": "Account for the exact source locator.",
                "completion_condition": "Complete and verify every dimension.",
            }
        ],
    }


def _write_fixture_artifact(base_dir: Path, name: str, data: bytes) -> tuple[str, str]:
    path = base_dir / name
    path.write_bytes(data)
    return name, _sha256_bytes(data)


def _verified_fixture(base_dir: Path) -> dict[str, Any]:
    packet = _open_fixture()
    packet["packet_id"] = "verified.self-test"
    packet["overall_status"] = "verified"
    packet["reconstruction_mode"] = "full_reconstruction"
    source_path, source_digest = _write_fixture_artifact(
        base_dir, "authority-source.txt", b"self-test authority snapshot\n"
    )
    packet["authority"]["local_path"] = source_path
    packet["authority"]["source_sha256"] = source_digest
    packet["presentation_identity"] = {
        "identity_status": "identified",
        "source_given_name": "Self-test source-given presentation name",
        "house_selected": False,
        "synthesized": False,
        "hybrid": False,
    }
    packet["owed_artifacts"] = []
    packet["content"] = {
        key: [
            {
                "item_id": f"self-test.{key}.na",
                "status": "not_applicable",
                "source_locator": f"Self-test locator for {key}",
                "source_justification": f"Self-test source states {key} is not applicable.",
            }
        ]
        for key in CONTENT_KEYS
    }
    present_text = "Self-test present definition content."
    packet["content"]["definitions"] = [
        {
            "item_id": "self-test.definitions.present",
            "status": "present",
            "source_locator": "Self-test definition locator",
            "text": present_text,
            "content_digest": _sha256_bytes(present_text.encode("utf-8")),
        }
    ]
    packet["obligation_links"] = {
        "coverage_assignments": [
            {
                "obligation_id": "SRC-001",
                "assignment_status": "fulfilled",
                "source_locator": "Self-test source acquisition record SRC-001",
                "present_content_item_ids": ["self-test.definitions.present"],
                "owed_artifact_ids": [],
            }
        ],
        "register_assignments": [],
    }
    packet["completeness"] = {key: "pass" for key in COMPLETENESS_KEYS}
    packet["verification"] = {key: "pass" for key in VERIFICATION_KEYS}
    packet["verification_evidence"] = []
    for kind_index, kind in enumerate(VERIFICATION_KEYS):
        artifact_path, artifact_digest = _write_fixture_artifact(
            base_dir,
            f"evidence-{kind}.txt",
            f"independently produced self-test evidence for {kind}\n".encode("utf-8"),
        )
        evidence: dict[str, Any] = {
            "kind": kind,
            "artifact_path": artifact_path,
            "sha256": artifact_digest,
            "verifier_identity": f"self-test {kind} verifier",
            "verification_scope": f"self-test scope for {kind}",
            "independently_produced": True,
        }
        if kind in AI_VERIFICATION_KEYS:
            evidence.update(
                {
                    "model": "self-test-model",
                    "model_version": f"self-test-version-{kind_index}",
                    "instructions": "Compare the packet to the consulted authority.",
                    "consulted_authority_files": [
                        {"path": source_path, "sha256": source_digest}
                    ],
                    "consulted_authority_locators": [
                        packet["authority"]["exact_locator"]
                    ],
                    "findings": [f"The self-test {kind} review passes."],
                    "evidence_digest": artifact_digest,
                }
            )
        packet["verification_evidence"].append(evidence)
    return packet


def _run_self_tests_in(base_dir: Path) -> bool:
    cache_failed = False
    try:
        _run_manifest_id_cache_self_test(base_dir)
        print("SELF-TEST PASS: manifest-ID cache is path- and fingerprint-scoped")
    except AssertionError as exc:
        cache_failed = True
        print(f"SELF-TEST FAIL: manifest-ID cache: {exc}", file=sys.stderr)

    cases: list[tuple[str, dict[str, Any], bool]] = []
    cases.append(("valid open skeleton", _open_fixture(), True))
    cases.append(("structurally valid verified packet with evidence", _verified_fixture(base_dir), True))

    invalid_open = _open_fixture()
    invalid_open["owed_artifacts"] = []
    cases.append(("open without owed artifact", invalid_open, False))

    invalid_verified_owed = _verified_fixture(base_dir)
    invalid_verified_owed["owed_artifacts"] = _open_fixture()["owed_artifacts"]
    cases.append(("verified with owed artifact", invalid_verified_owed, False))

    invalid_verified_empty = _verified_fixture(base_dir)
    invalid_verified_empty["content"]["proofs"] = []
    cases.append(("verified with empty content category", invalid_verified_empty, False))

    invalid_all_not_applicable = _verified_fixture(base_dir)
    invalid_all_not_applicable["content"]["definitions"] = [
        {
            "item_id": "self-test.definitions.na",
            "status": "not_applicable",
            "source_locator": "Self-test definition locator",
            "source_justification": "Self-test source says definitions are inapplicable.",
        }
    ]
    cases.append(("verified packet with all categories not applicable", invalid_all_not_applicable, False))

    invalid_attribution_only = _verified_fixture(base_dir)
    invalid_attribution_only["content"]["definitions"] = [
        {
            "item_id": "self-test.definitions.na",
            "status": "not_applicable",
            "source_locator": "Self-test definition locator",
            "source_justification": "Self-test source says definitions are inapplicable.",
        }
    ]
    attribution_text = "Self-test attribution only."
    invalid_attribution_only["content"]["source_attributions"] = [
        {
            "item_id": "self-test.attribution.present",
            "status": "present",
            "source_locator": "Self-test attribution locator",
            "text": attribution_text,
            "content_digest": _sha256_bytes(attribution_text.encode("utf-8")),
        }
    ]
    invalid_attribution_only["obligation_links"]["coverage_assignments"][0][
        "present_content_item_ids"
    ] = ["self-test.attribution.present"]
    cases.append(
        ("verified packet with attribution as its only present content", invalid_attribution_only, False)
    )

    invalid_bare_links = _open_fixture()
    invalid_bare_links["obligation_links"] = {
        "coverage_manifest_ids": ["SRC-001"],
        "register_obligation_ids": [],
    }
    cases.append(("bare obligation id arrays without assignments", invalid_bare_links, False))

    invalid_open_assignment = _open_fixture()
    invalid_open_assignment["obligation_links"]["coverage_assignments"][0][
        "owed_artifact_ids"
    ] = ["owed.does-not-exist"]
    cases.append(("open assignment with unknown owed artifact", invalid_open_assignment, False))

    invalid_fulfilled_reference = _verified_fixture(base_dir)
    invalid_fulfilled_reference["obligation_links"]["coverage_assignments"][0][
        "present_content_item_ids"
    ] = ["self-test.does-not-exist"]
    cases.append(
        ("fulfilled assignment with unknown present item", invalid_fulfilled_reference, False)
    )

    invalid_verified_open_assignment = _verified_fixture(base_dir)
    invalid_verified_open_assignment["obligation_links"]["coverage_assignments"][0][
        "assignment_status"
    ] = "open"
    cases.append(
        ("verified packet with open obligation assignment", invalid_verified_open_assignment, False)
    )

    invalid_missing_solution_category = _verified_fixture(base_dir)
    del invalid_missing_solution_category["content"]["exercise_solutions"]
    cases.append(
        (
            "verified with omitted exercise-solutions category",
            invalid_missing_solution_category,
            False,
        )
    )

    invalid_missing_feedback_gate = _verified_fixture(base_dir)
    del invalid_missing_feedback_gate["completeness"]["exercise_feedback"]
    cases.append(
        (
            "verified with omitted exercise-feedback completeness gate",
            invalid_missing_feedback_gate,
            False,
        )
    )

    invalid_na = _verified_fixture(base_dir)
    del invalid_na["content"]["examples"][0]["source_justification"]
    cases.append(("not-applicable without source justification", invalid_na, False))

    invalid_dimension = _verified_fixture(base_dir)
    invalid_dimension["verification"]["visual"] = "pending"
    cases.append(("verified with pending dimension", invalid_dimension, False))

    invalid_missing_evidence = _verified_fixture(base_dir)
    invalid_missing_evidence["verification_evidence"] = [
        item
        for item in invalid_missing_evidence["verification_evidence"]
        if item["kind"] != "adversarial_publication_ai"
    ]
    cases.append(("verified without adversarial AI evidence", invalid_missing_evidence, False))

    invalid_duplicate_evidence = _verified_fixture(base_dir)
    invalid_duplicate_evidence["verification_evidence"][1]["artifact_path"] = (
        invalid_duplicate_evidence["verification_evidence"][0]["artifact_path"]
    )
    invalid_duplicate_evidence["verification_evidence"][1]["sha256"] = (
        invalid_duplicate_evidence["verification_evidence"][0]["sha256"]
    )
    cases.append(("verification dimensions reuse one evidence file", invalid_duplicate_evidence, False))

    invalid_hybrid = _open_fixture()
    invalid_hybrid["presentation_identity"]["hybrid"] = True
    cases.append(("hybrid flag true", invalid_hybrid, False))

    invalid_authority = _open_fixture()
    del invalid_authority["authority"]["local_path"]
    cases.append(("authority without source location", invalid_authority, False))

    invalid_present = _verified_fixture(base_dir)
    invalid_present["content"]["syntax"] = [
        {
            "item_id": "self-test.syntax",
            "status": "present",
            "source_locator": "Self-test syntax locator",
            "text": "Self-test text",
            "artifact_path": "self-test-path",
            "content_digest": _sha256_bytes(b"Self-test text"),
        }
    ]
    cases.append(("present item with two bodies", invalid_present, False))

    failed = cache_failed
    for name, packet, expected_valid in cases:
        errors = validate_packet(copy.deepcopy(packet), base_dir=base_dir)
        actual_valid = not errors
        if actual_valid == expected_valid:
            print(f"SELF-TEST PASS: {name}")
        else:
            failed = True
            expectation = "valid" if expected_valid else "invalid"
            print(f"SELF-TEST FAIL: {name} expected {expectation}", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)

    self_evidence_packet = _verified_fixture(base_dir)
    packet_as_evidence = base_dir / self_evidence_packet["verification_evidence"][0][
        "artifact_path"
    ]
    self_evidence_errors = validate_packet(
        self_evidence_packet,
        base_dir=base_dir,
        packet_path=packet_as_evidence,
    )
    if self_evidence_errors:
        print("SELF-TEST PASS: packet cannot serve as its own evidence")
    else:
        failed = True
        print(
            "SELF-TEST FAIL: packet serving as its own evidence was accepted",
            file=sys.stderr,
        )
    return not failed


def run_self_tests() -> bool:
    with tempfile.TemporaryDirectory(prefix="presentation-packet-self-test-") as temp:
        return _run_self_tests_in(Path(temp))


def _load_packet(path: Path) -> tuple[Any | None, str | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except OSError as exc:
        return None, f"could not read file: {exc}"
    except json.JSONDecodeError as exc:
        return None, f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate presentation packet structure, obligation assignments, and "
            "referenced-artifact digests; content truth is not certified."
        )
    )
    parser.add_argument("packets", nargs="*", type=Path, help="packet JSON file")
    parser.add_argument(
        "--self-test", action="store_true", help="run internal positive and negative tests"
    )
    args = parser.parse_args(argv)

    if not args.self_test and not args.packets:
        parser.error("provide at least one packet JSON file or --self-test")

    ok = True
    if args.self_test:
        ok = run_self_tests() and ok

    for path in args.packets:
        packet, load_error = _load_packet(path)
        if load_error is not None:
            ok = False
            print(f"FAIL {path}: {load_error}", file=sys.stderr)
            continue
        errors = validate_packet(
            packet,
            base_dir=path.resolve().parent,
            packet_path=path.resolve(),
        )
        if errors:
            ok = False
            print(f"FAIL {path}", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
        else:
            print(
                f"STRUCTURAL/EVIDENCE-INTEGRITY CHECK OK {path}: "
                "content truth not certified"
            )

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
