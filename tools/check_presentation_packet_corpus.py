#!/usr/bin/env python3
"""Check presentation packets as one corpus without certifying content truth.

The individual packet validator checks shape and referenced-byte integrity. This
checker adds corpus-wide administrative constraints and verifies the independently
generated content-admission projection against its governed reviewed records. The
structural checks cannot establish that a packet is faithful or complete, and the
admission check establishes only that the separate evidence protocol admitted the
exact maintained packet content; neither result is whole-book readiness.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import sys
import tempfile
from pathlib import Path
from typing import Any

import check_presentation_packet as packet_checker
from check_presentation_packet import _open_fixture, _verified_fixture

try:
    import build_presentation_packet_admission as admission_builder
except ImportError:  # pragma: no cover
    from tools import build_presentation_packet_admission as admission_builder  # type: ignore


REPO_ROOT = Path(__file__).resolve().parents[1]
PACKET_ROOT = REPO_ROOT / "spec" / "presentations"
COVERAGE_MANIFEST = REPO_ROOT / "spec" / "full-compendium-coverage-manifest.csv"
REGISTER_MANIFEST = REPO_ROOT / "spec" / "register-obligation-manifest.csv"

# Acquisition source rows can legitimately carry hundreds of exact locators.
csv.field_size_limit(2_147_483_647)


def discover_packets(packet_root: Path = PACKET_ROOT) -> list[Path]:
    """Return every JSON packet below the dedicated packet directory."""

    if not packet_root.is_dir():
        return []
    return sorted(path for path in packet_root.rglob("*.json") if path.is_file())


def _load_json(path: Path) -> tuple[Any | None, str | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except OSError as exc:
        return None, f"could not read: {exc}"
    except json.JSONDecodeError as exc:
        return None, f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"


def _manifest_ids(path: Path, field: str) -> tuple[frozenset[str], str | None]:
    """Use the packet checker's path- and fingerprint-scoped immutable cache."""

    errors: list[str] = []
    identifiers = packet_checker._manifest_ids(path, field, errors)
    return identifiers, errors[0] if errors else None


def _validate_packet_with_manifests(
    packet: dict[str, Any],
    *,
    base_dir: Path,
    packet_path: Path,
    coverage_manifest: Path,
    register_manifest: Path,
) -> list[str]:
    """Route packet membership checks through this corpus run's exact manifests."""

    previous_coverage = packet_checker.COVERAGE_MANIFEST
    previous_register = packet_checker.REGISTER_MANIFEST
    packet_checker.COVERAGE_MANIFEST = coverage_manifest
    packet_checker.REGISTER_MANIFEST = register_manifest
    try:
        return packet_checker.validate_packet(
            packet,
            base_dir=base_dir,
            packet_path=packet_path,
        )
    finally:
        packet_checker.COVERAGE_MANIFEST = previous_coverage
        packet_checker.REGISTER_MANIFEST = previous_register


def _is_within(path: Path, directory: Path) -> bool:
    try:
        path.relative_to(directory)
        return True
    except ValueError:
        return False


def _assignment_ids(packet: dict[str, Any], field: str) -> set[str]:
    links = packet.get("obligation_links")
    if not isinstance(links, dict):
        return set()
    assignments = links.get(field)
    if not isinstance(assignments, list):
        return set()
    return {
        assignment["obligation_id"]
        for assignment in assignments
        if isinstance(assignment, dict)
        and isinstance(assignment.get("obligation_id"), str)
        and assignment["obligation_id"].strip()
    }


def _fulfilled_assignment_ids(packet: dict[str, Any], field: str) -> set[str]:
    links = packet.get("obligation_links")
    if not isinstance(links, dict):
        return set()
    assignments = links.get(field)
    if not isinstance(assignments, list):
        return set()
    return {
        assignment["obligation_id"]
        for assignment in assignments
        if isinstance(assignment, dict)
        and assignment.get("assignment_status") == "fulfilled"
        and isinstance(assignment.get("obligation_id"), str)
        and assignment["obligation_id"].strip()
    }


def check_corpus(
    packet_paths: list[Path],
    repo_root: Path = REPO_ROOT,
    coverage_manifest: Path = COVERAGE_MANIFEST,
    register_manifest: Path = REGISTER_MANIFEST,
) -> tuple[list[str], dict[str, Any]]:
    """Return corpus-control errors and non-semantic accounting statistics."""

    errors: list[str] = []
    coverage_ids, coverage_error = _manifest_ids(coverage_manifest, "stable_id")
    register_ids, register_error = _manifest_ids(register_manifest, "obligation_id")
    if coverage_error:
        errors.append(coverage_error)
    if register_error:
        errors.append(register_error)

    loaded: list[tuple[Path, dict[str, Any], bool]] = []
    packet_id_owners: dict[str, Path] = {}
    label_owners: dict[str, tuple[str, Path]] = {}
    declared_coverage: set[str] = set()
    structurally_valid_coverage: set[str] = set()
    verified_fulfilled_coverage: set[str] = set()
    declared_register: set[str] = set()
    verified_fulfilled_register: set[str] = set()
    open_packets = 0
    verified_packets = 0

    for path in packet_paths:
        packet, load_error = _load_json(path)
        if load_error is not None:
            errors.append(f"{path}: {load_error}")
            continue
        if not isinstance(packet, dict):
            errors.append(f"{path}: packet root must be an object")
            continue

        packet_errors = _validate_packet_with_manifests(
            packet,
            base_dir=path.resolve().parent,
            packet_path=path.resolve(),
            coverage_manifest=coverage_manifest,
            register_manifest=register_manifest,
        )
        for error in packet_errors:
            errors.append(f"{path}: {error}")
        individually_valid = not packet_errors
        loaded.append((path, packet, individually_valid))

        packet_id = packet.get("packet_id")
        if isinstance(packet_id, str) and packet_id.strip():
            if packet_id in packet_id_owners:
                errors.append(
                    f"{path}: duplicate packet_id {packet_id}; first used by "
                    f"{packet_id_owners[packet_id]}"
                )
            else:
                packet_id_owners[packet_id] = path

        status = packet.get("overall_status")
        open_packets += int(status == "open")
        verified_packets += int(status == "verified")
        packet_coverage = _assignment_ids(packet, "coverage_assignments")
        packet_register = _assignment_ids(packet, "register_assignments")
        declared_coverage.update(packet_coverage)
        declared_register.update(packet_register)
        if individually_valid:
            structurally_valid_coverage.update(packet_coverage)
            if status == "verified":
                verified_fulfilled_coverage.update(
                    _fulfilled_assignment_ids(packet, "coverage_assignments")
                )
                verified_fulfilled_register.update(
                    _fulfilled_assignment_ids(packet, "register_assignments")
                )

        destination = packet.get("destination")
        if isinstance(destination, dict):
            labels = destination.get("stable_labels")
            if isinstance(labels, list):
                for label in labels:
                    if not isinstance(label, str) or not label.strip():
                        continue
                    owner = label_owners.get(label)
                    if owner is not None and owner[1] != path:
                        errors.append(
                            f"{path}: destination label {label!r} also closes packet "
                            f"{owner[0]} in {owner[1]}"
                        )
                    else:
                        label_owners[label] = (
                            packet_id if isinstance(packet_id, str) else "<invalid-id>",
                            path,
                        )

            if status == "verified":
                raw_file = destination.get("file")
                if isinstance(raw_file, str) and raw_file.strip():
                    candidate = Path(raw_file)
                    resolved = (
                        candidate.resolve()
                        if candidate.is_absolute()
                        else (repo_root / candidate).resolve()
                    )
                    handbook_root = (repo_root / "handbook").resolve()
                    if not _is_within(resolved, handbook_root):
                        errors.append(
                            f"{path}: verified destination must be contained under "
                            f"{handbook_root}, got {resolved}"
                        )
                    elif not resolved.is_file():
                        errors.append(f"{path}: verified destination does not exist: {resolved}")
                    else:
                        try:
                            destination_text = resolved.read_text(encoding="utf-8")
                        except (OSError, UnicodeError) as exc:
                            errors.append(f"{path}: could not read destination {resolved}: {exc}")
                        else:
                            if isinstance(labels, list):
                                for label in labels:
                                    if isinstance(label, str) and label.strip():
                                        literal = f"\\label{{{label}}}"
                                        if literal not in destination_text:
                                            errors.append(
                                                f"{path}: stable label {label!r} does not "
                                                f"literally resolve as {literal!r} in {resolved}"
                                            )

    known_packet_ids = set(packet_id_owners)
    for path, packet, _ in loaded:
        own_id = packet.get("packet_id")
        variants = packet.get("variants")
        if not isinstance(variants, list):
            continue
        for index, variant in enumerate(variants):
            if not isinstance(variant, dict):
                continue
            related = variant.get("related_packet_id")
            if not isinstance(related, str) or not related.strip():
                continue
            if related == own_id:
                errors.append(
                    f"{path}: variants[{index}].related_packet_id cannot refer to its own packet"
                )
            elif related not in known_packet_ids:
                errors.append(
                    f"{path}: variants[{index}].related_packet_id does not resolve: {related}"
                )

    stats = {
        "packet_files": len(packet_paths),
        "loaded_packets": len(loaded),
        "open_packets": open_packets,
        "verified_packets": verified_packets,
        "coverage_total": len(coverage_ids),
        "coverage_declared": sum(
            obligation_id in coverage_ids for obligation_id in declared_coverage
        ),
        "coverage_structurally_valid": sum(
            obligation_id in coverage_ids
            for obligation_id in structurally_valid_coverage
        ),
        "coverage_verified_fulfilled": sum(
            obligation_id in coverage_ids
            for obligation_id in verified_fulfilled_coverage
        ),
        "coverage_missing_verified_fulfilled": sum(
            obligation_id not in verified_fulfilled_coverage
            for obligation_id in coverage_ids
        ),
        "register_total": len(register_ids),
        "register_declared": sum(
            obligation_id in register_ids for obligation_id in declared_register
        ),
        "register_verified_fulfilled": sum(
            obligation_id in register_ids
            for obligation_id in verified_fulfilled_register
        ),
    }
    return errors, stats


def check_content_admission(
    *,
    repo_root: Path,
    packet_root: Path,
    reviewed_admissions: Path,
    coverage_manifest: Path,
    register_manifest: Path,
    admission_projection: Path,
) -> tuple[list[str], dict[str, Any]]:
    """Verify the generated projection against independent reviewed records."""

    errors: list[str] = []
    stats: dict[str, Any] = {
        "admission_rows": 0,
        "admitted_packets": 0,
        "open_admissions": 0,
        "admission_projection_sha256": "",
    }
    try:
        rows = admission_builder.build_rows(
            repo_root,
            packet_root,
            reviewed_admissions,
            coverage_manifest,
            register_manifest,
        )
        expected = admission_builder.csv_bytes(rows)
        actual = admission_projection.read_bytes()
        if actual != expected:
            raise ValueError(
                f"stale or malformed generated projection: {admission_projection}"
            )
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        errors.append(str(exc))
        return errors, stats

    admitted = sum(row["admission_status"] == "ADMITTED" for row in rows)
    stats.update(
        {
            "admission_rows": len(rows),
            "admitted_packets": admitted,
            "open_admissions": len(rows) - admitted,
            "admission_projection_sha256": hashlib.sha256(actual).hexdigest(),
        }
    )
    return errors, stats


def _print_report(
    errors: list[str],
    stats: dict[str, Any],
    admission_errors: list[str],
    admission_stats: dict[str, Any],
) -> None:
    if errors:
        print("PRESENTATION PACKET CORPUS STRUCTURAL CHECK FAILED", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
    else:
        print("PRESENTATION PACKET CORPUS STRUCTURAL CHECK OK")
    print(
        "packet files: {packet_files}; loaded: {loaded_packets}; open: "
        "{open_packets}; verified: {verified_packets}".format(**stats)
    )
    print(
        "coverage assignments: declared {coverage_declared}/{coverage_total}; "
        "in individually valid packets {coverage_structurally_valid}/{coverage_total}; "
        "fulfilled by verified packets {coverage_verified_fulfilled}/{coverage_total}; "
        "still required {coverage_missing_verified_fulfilled}".format(**stats)
    )
    print(
        "register assignments: declared {register_declared}/{register_total}; "
        "fulfilled by verified packets {register_verified_fulfilled}/{register_total}".format(
            **stats
        )
    )
    if admission_errors:
        print("CONTENT-ADMISSION PROJECTION CHECK FAILED", file=sys.stderr)
        for error in admission_errors:
            print(f"  - {error}", file=sys.stderr)
        print(
            "content-admission control: FAIL-CLOSED; no packet content is accepted "
            "by this corpus run"
        )
    else:
        print("CONTENT-ADMISSION PROJECTION CHECK OK")
        print(
            "content-admission control: independently governed projection verified; "
            "independently admitted {admitted_packets}/{admission_rows}; open "
            "{open_admissions}; SHA-256 {admission_projection_sha256}".format(
                **admission_stats
            )
        )
    print("COMPENDIUM CONTENT/RESTORATION/READINESS: OPEN")
    print(
        "Packet counts are structural; admission counts come only from the independent "
        "projection. Neither control establishes whole-book terminal readiness."
    )


def _write_packet(path: Path, packet: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")


def run_self_tests() -> bool:
    cases: list[tuple[str, bool]] = []
    with tempfile.TemporaryDirectory(prefix="presentation-packet-corpus-self-test-") as temp:
        root = Path(temp)
        packet_root = root / "spec" / "presentations"
        coverage_manifest = root / "coverage-manifest.csv"
        register_manifest = root / "register-manifest.csv"
        coverage_manifest.write_text(
            "stable_id,record_type\nSRC-001,source\nSRC-001-T001,topic\n",
            encoding="utf-8",
            newline="",
        )
        register_manifest.write_text(
            "obligation_id,status\nREG-001,open\n",
            encoding="utf-8",
            newline="",
        )

        def check_fixture_corpus(
            packet_paths: list[Path],
        ) -> tuple[list[str], dict[str, Any]]:
            return check_corpus(
                packet_paths,
                repo_root=root,
                coverage_manifest=coverage_manifest,
                register_manifest=register_manifest,
            )

        errors, _ = check_fixture_corpus([])
        cases.append(("empty corpus is structurally valid", not errors))

        one = _open_fixture()
        one_path = packet_root / "one.json"
        _write_packet(one_path, one)
        packet_checker._cached_manifest_ids.cache_clear()
        errors, _ = check_fixture_corpus([one_path])
        cases.append(("one open packet is structurally valid", not errors))
        cache_info = packet_checker._cached_manifest_ids.cache_info()
        cases.append(
            (
                "corpus and packet validation reuse one cached manifest-ID object",
                cache_info.misses == 2 and cache_info.hits >= 2,
            )
        )

        duplicate_id = copy.deepcopy(one)
        duplicate_id["destination"]["stable_labels"] = ["packet:duplicate-id"]
        duplicate_id_path = packet_root / "duplicate-id.json"
        _write_packet(duplicate_id_path, duplicate_id)
        errors, _ = check_fixture_corpus([one_path, duplicate_id_path])
        cases.append(("duplicate packet id is rejected", bool(errors)))

        duplicate_label = copy.deepcopy(one)
        duplicate_label["packet_id"] = "open.duplicate-label"
        duplicate_label_path = packet_root / "duplicate-label.json"
        _write_packet(duplicate_label_path, duplicate_label)
        errors, _ = check_fixture_corpus([one_path, duplicate_label_path])
        cases.append(("destination label closing two packets is rejected", bool(errors)))

        unresolved = copy.deepcopy(one)
        unresolved["packet_id"] = "open.unresolved-variant"
        unresolved["destination"]["stable_labels"] = ["packet:unresolved-variant"]
        unresolved["variants"] = [
            {
                "related_packet_id": "missing.packet",
                "source_locator": "Self-test relation locator",
                "source_stated_relation": "Self-test source-stated relation",
            }
        ]
        unresolved_path = packet_root / "unresolved.json"
        _write_packet(unresolved_path, unresolved)
        errors, _ = check_fixture_corpus([unresolved_path])
        cases.append(("unresolved variant is rejected", bool(errors)))

        self_variant = copy.deepcopy(one)
        self_variant["packet_id"] = "open.self-variant"
        self_variant["destination"]["stable_labels"] = ["packet:self-variant"]
        self_variant["variants"] = [
            {
                "related_packet_id": "open.self-variant",
                "source_locator": "Self-test relation locator",
                "source_stated_relation": "Self-test source-stated relation",
            }
        ]
        self_variant_path = packet_root / "self-variant.json"
        _write_packet(self_variant_path, self_variant)
        errors, _ = check_fixture_corpus([self_variant_path])
        cases.append(("self-referential variant is rejected", bool(errors)))

        verified_dir = packet_root / "verified-files"
        verified_dir.mkdir(parents=True, exist_ok=True)
        verified = _verified_fixture(verified_dir)
        verified["destination"] = {
            "file": "handbook/verified.tex",
            "stable_labels": ["packet:verified"],
        }
        handbook = root / "handbook"
        handbook.mkdir(parents=True, exist_ok=True)
        (handbook / "verified.tex").write_text(
            "\\section{Self-test}\\label{packet:verified}\n", encoding="utf-8"
        )
        verified_path = verified_dir / "verified.json"
        _write_packet(verified_path, verified)
        errors, _ = check_fixture_corpus([verified_path])
        cases.append(("verified destination and literal label resolve", not errors))

        missing_label = copy.deepcopy(verified)
        missing_label["packet_id"] = "verified.missing-label"
        missing_label["destination"]["stable_labels"] = ["packet:not-in-file"]
        missing_label_path = verified_dir / "missing-label.json"
        _write_packet(missing_label_path, missing_label)
        errors, _ = check_fixture_corpus([missing_label_path])
        cases.append(("verified destination missing literal label is rejected", bool(errors)))

        missing_file = copy.deepcopy(verified)
        missing_file["packet_id"] = "verified.missing-file"
        missing_file["destination"] = {
            "file": "handbook/does-not-exist.tex",
            "stable_labels": ["packet:missing-file"],
        }
        missing_file_path = verified_dir / "missing-file.json"
        _write_packet(missing_file_path, missing_file)
        errors, _ = check_fixture_corpus([missing_file_path])
        cases.append(("verified missing destination file is rejected", bool(errors)))

        outside = copy.deepcopy(verified)
        outside["packet_id"] = "verified.outside"
        outside["destination"] = {
            "file": "outside.tex",
            "stable_labels": ["packet:outside"],
        }
        outside_path = verified_dir / "outside.json"
        _write_packet(outside_path, outside)
        errors, _ = check_fixture_corpus([outside_path])
        cases.append(("verified destination outside handbook is rejected", bool(errors)))

    failed = False
    for name, passed in cases:
        if passed:
            print(f"SELF-TEST PASS: {name}")
        else:
            failed = True
            print(f"SELF-TEST FAIL: {name}", file=sys.stderr)
    if not failed:
        print("SELF-TEST PASS: corpus controls do not establish book readiness")
    return not failed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check the complete presentation-packet corpus for cross-packet "
            "structural integrity; semantic truth is not certified."
        )
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--require-ready",
        action="store_true",
        help=(
            "require release readiness; fails closed because this corpus checker is "
            "not the book-level terminal-readiness verdict"
        ),
    )
    mode.add_argument(
        "--self-test", action="store_true", help="run internal corpus-control tests"
    )
    parser.add_argument("--repository-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--packet-root", type=Path, default=Path("spec/presentations"))
    parser.add_argument(
        "--coverage-manifest",
        type=Path,
        default=Path("spec/full-compendium-coverage-manifest.csv"),
    )
    parser.add_argument(
        "--register-manifest",
        type=Path,
        default=Path("spec/register-obligation-manifest.csv"),
    )
    parser.add_argument(
        "--reviewed-admissions",
        type=Path,
        default=Path("spec/provenance/reviewed-presentation-packet-admissions.json"),
    )
    parser.add_argument(
        "--admission-projection",
        type=Path,
        default=Path("spec/presentation-packet-admission.csv"),
    )
    args = parser.parse_args(argv)

    if args.self_test:
        return 0 if run_self_tests() else 1

    repo_root = args.repository_root.resolve()

    def rooted(path: Path) -> Path:
        return path if path.is_absolute() else repo_root / path

    packet_root = rooted(args.packet_root)
    coverage_manifest = rooted(args.coverage_manifest)
    register_manifest = rooted(args.register_manifest)
    reviewed_admissions = rooted(args.reviewed_admissions)
    admission_projection = rooted(args.admission_projection)

    packet_paths = discover_packets(packet_root)
    errors, stats = check_corpus(
        packet_paths,
        repo_root=repo_root,
        coverage_manifest=coverage_manifest,
        register_manifest=register_manifest,
    )
    admission_errors, admission_stats = check_content_admission(
        repo_root=repo_root,
        packet_root=packet_root,
        reviewed_admissions=reviewed_admissions,
        coverage_manifest=coverage_manifest,
        register_manifest=register_manifest,
        admission_projection=admission_projection,
    )
    _print_report(errors, stats, admission_errors, admission_stats)
    if args.require_ready:
        print(
            "REQUIRE-READY FAILED CLOSED: packet-corpus controls do not establish "
            "book-level terminal readiness; use tools/check_terminal_readiness.py.",
            file=sys.stderr,
        )
        return 1
    return 1 if errors or admission_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
