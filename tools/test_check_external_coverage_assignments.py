#!/usr/bin/env python3
"""Adversarial tests for streamed external-coverage assignments."""

from __future__ import annotations

import copy
import csv
import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path

import jsonschema

from tools import build_presentation_packet_admission as admission
from tools import check_external_coverage_assignments as checker
from tools import check_presentation_packet as packet_checker


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def csv_raw(fieldnames: tuple[str, ...], rows: list[dict[str, str]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


class ExternalCoverageAssignmentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="coverage-sidecar-")
        self.root = Path(self.temporary.name)
        (self.root / "spec/presentations").mkdir(parents=True)
        (self.root / "spec/provenance/external-coverage-assignments").mkdir(parents=True)
        self.coverage_path = self.write(
            "spec/coverage.csv",
            b"stable_id,mapping_status\nSRC-001,open/unmapped\nSRC-002,open/unmapped\n",
        )
        self.packet_path = self.root / "spec/presentations/verified.json"
        self.packet = packet_checker._verified_fixture(self.packet_path.parent)
        self.write_packet()
        self.admission_path = self.root / "spec/presentation-packet-admission.csv"
        self.write_admission(admitted=True)
        self.sidecar_path = (
            self.root
            / "spec/provenance/external-coverage-assignments/assignments-000001.csv"
        )
        self.sidecar_rows = [
            {
                "coverage_id": "SRC-001",
                "packet_id": "verified.self-test",
                "source_locator": "Self-test source acquisition record SRC-001",
                "present_content_item_ids": '["self-test.definitions.present"]',
            },
            {
                "coverage_id": "SRC-002",
                "packet_id": "verified.self-test",
                "source_locator": "Second exact source locator",
                "present_content_item_ids": '["self-test.definitions.present"]',
            },
        ]
        self.write_sidecar(self.sidecar_rows)
        self.index_path = self.root / "spec/external-coverage-assignment-index.json"
        self.write_index(include_sidecar=True)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, raw: bytes) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return path

    def write_packet(self) -> None:
        self.packet_path.write_text(
            json.dumps(self.packet, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def admission_row(self, admitted: bool) -> dict[str, str]:
        row = {field: "" for field in admission.OUTPUT_FIELDS}
        row.update(
            {
                "packet_id": "verified.self-test",
                "packet_path": "spec/presentations/verified.json",
                "packet_sha256": digest(self.packet_path.read_bytes()),
                "admission_status": "ADMITTED" if admitted else "OPEN",
                "authority_projection_sha256": (
                    admission.canonical_digest(self.packet["authority"])
                    if admitted
                    else ""
                ),
                "presentation_identity_projection_sha256": (
                    admission.canonical_digest(self.packet["presentation_identity"])
                    if admitted
                    else ""
                ),
                "content_projection_sha256": (
                    admission.canonical_digest(self.packet["content"])
                    if admitted
                    else ""
                ),
                "present_content_item_ids": (
                    '["self-test.definitions.present"]' if admitted else "[]"
                ),
                "destination_labels": '["packet:self-test"]' if admitted else "[]",
                "verification_evidence": "[]",
            }
        )
        for category in admission.VERIFICATION_FIELDS:
            row[f"{category}_verification"] = "pass" if admitted else "pending"
        return row

    def write_admission(self, admitted: bool) -> None:
        self.admission_path.write_bytes(
            csv_raw(admission.OUTPUT_FIELDS, [self.admission_row(admitted)])
        )

    def write_sidecar(self, rows: list[dict[str, str]]) -> None:
        self.sidecar_path.write_bytes(csv_raw(checker.SIDECAR_FIELDS, rows))

    def index(self, include_sidecar: bool) -> dict[str, object]:
        sidecars: list[dict[str, object]] = []
        if include_sidecar:
            sidecars.append(
                {
                    "sidecar_path": self.sidecar_path.relative_to(self.root).as_posix(),
                    "sidecar_sha256": digest(self.sidecar_path.read_bytes()),
                    "assignment_count": len(self.sidecar_rows),
                    "first_coverage_id": self.sidecar_rows[0]["coverage_id"],
                    "last_coverage_id": self.sidecar_rows[-1]["coverage_id"],
                }
            )
        return {
            "schema_version": checker.SCHEMA_VERSION,
            "coverage_manifest_path": "spec/coverage.csv",
            "coverage_manifest_sha256": digest(self.coverage_path.read_bytes()),
            "coverage_manifest_bytes": self.coverage_path.stat().st_size,
            "coverage_manifest_record_count": 2,
            "packet_admission_path": "spec/presentation-packet-admission.csv",
            "packet_admission_sha256": digest(self.admission_path.read_bytes()),
            "packet_admission_bytes": self.admission_path.stat().st_size,
            "sidecars": sidecars,
        }

    def write_index(self, include_sidecar: bool) -> None:
        self.index_path.write_text(
            json.dumps(self.index(include_sidecar), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def check(self, *, require_complete: bool = False) -> checker.CoverageAssignmentResult:
        return checker.validate_index(self.root, self.index_path, require_complete)

    def test_complete_streamed_assignment_is_accepted(self) -> None:
        result = self.check(require_complete=True)
        self.assertEqual(result.coverage_record_count, 2)
        self.assertEqual(result.assignment_count, 2)
        self.assertEqual(result.unassigned_count, 0)
        self.assertEqual(result.admitted_packet_count, 1)

    def test_manifest_native_hierarchy_topic_interleaving_is_accepted(self) -> None:
        manifest_ids = (
            "SRC-001",
            "SRC-001-H001",
            "SRC-001-T001",
            "SRC-001-H002",
        )
        manifest_raw = (
            "stable_id,mapping_status\n"
            + "".join(f"{stable_id},open/unmapped\n" for stable_id in manifest_ids)
        ).encode("utf-8")
        self.coverage_path.write_bytes(manifest_raw)
        self.sidecar_rows = [
            {
                "coverage_id": stable_id,
                "packet_id": "verified.self-test",
                "source_locator": f"Exact locator for {stable_id}",
                "present_content_item_ids": '["self-test.definitions.present"]',
            }
            for stable_id in manifest_ids
        ]
        # The fixture packet repeats only SRC-001; the sidecar may contain a
        # strict superset while remaining the sole assignment source of truth.
        self.sidecar_rows[0]["source_locator"] = (
            "Self-test source acquisition record SRC-001"
        )
        self.write_sidecar(self.sidecar_rows)
        value = self.index(include_sidecar=True)
        value["coverage_manifest_sha256"] = digest(manifest_raw)
        value["coverage_manifest_bytes"] = len(manifest_raw)
        value["coverage_manifest_record_count"] = len(manifest_ids)
        self.index_path.write_text(json.dumps(value) + "\n", encoding="utf-8")

        result = self.check(require_complete=True)
        self.assertEqual(result.coverage_record_count, len(manifest_ids))
        self.assertEqual(result.assignment_count, len(manifest_ids))
        self.assertEqual(result.unassigned_count, 0)

    def test_empty_sidecar_index_is_explicitly_incomplete(self) -> None:
        self.admission_path.write_bytes(csv_raw(admission.OUTPUT_FIELDS, []))
        self.write_index(include_sidecar=False)
        result = self.check()
        self.assertEqual(result.assignment_count, 0)
        self.assertEqual(result.unassigned_count, 2)
        with self.assertRaisesRegex(ValueError, "coverage remains unassigned"):
            self.check(require_complete=True)

    def test_duplicate_unknown_and_out_of_order_ids_fail_closed(self) -> None:
        for rows, message in (
            ([self.sidecar_rows[0], self.sidecar_rows[0]], "duplicate"),
            ([self.sidecar_rows[0], {**self.sidecar_rows[1], "coverage_id": "SRC-999"}], "unknown or out of manifest order"),
            ([self.sidecar_rows[1], self.sidecar_rows[0]], "unknown or out of manifest order"),
        ):
            with self.subTest(message=message):
                self.sidecar_rows = rows
                self.write_sidecar(rows)
                self.write_index(include_sidecar=True)
                with self.assertRaisesRegex(ValueError, message):
                    self.check()

    def test_nonadjacent_duplicate_manifest_and_assignment_fail_closed(self) -> None:
        repeated_manifest = (
            b"stable_id,mapping_status\n"
            b"SRC-001,open/unmapped\n"
            b"SRC-002,open/unmapped\n"
            b"SRC-001,open/unmapped\n"
        )
        self.coverage_path.write_bytes(repeated_manifest)
        self.sidecar_rows = [
            self.sidecar_rows[0],
            self.sidecar_rows[1],
            copy.deepcopy(self.sidecar_rows[0]),
        ]
        self.write_sidecar(self.sidecar_rows)
        value = self.index(include_sidecar=True)
        value["coverage_manifest_sha256"] = digest(repeated_manifest)
        value["coverage_manifest_bytes"] = len(repeated_manifest)
        value["coverage_manifest_record_count"] = 3
        self.index_path.write_text(json.dumps(value) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "duplicate coverage ID"):
            self.check(require_complete=True)

    def test_unknown_packet_content_and_unadmitted_packet_fail_closed(self) -> None:
        bad = copy.deepcopy(self.sidecar_rows)
        bad[0]["packet_id"] = "unknown.packet"
        self.sidecar_rows = bad
        self.write_sidecar(bad)
        self.write_index(include_sidecar=True)
        with self.assertRaisesRegex(ValueError, "not independently admitted"):
            self.check()

        self.setUp_fresh_rows()
        bad = copy.deepcopy(self.sidecar_rows)
        bad[0]["present_content_item_ids"] = '["unknown.content"]'
        self.sidecar_rows = bad
        self.write_sidecar(bad)
        self.write_index(include_sidecar=True)
        with self.assertRaisesRegex(ValueError, "unknown admitted content item"):
            self.check()

        self.setUp_fresh_rows()
        self.write_admission(admitted=False)
        self.write_index(include_sidecar=True)
        with self.assertRaisesRegex(ValueError, "not independently admitted"):
            self.check()

    def setUp_fresh_rows(self) -> None:
        self.sidecar_rows = [
            {
                "coverage_id": "SRC-001",
                "packet_id": "verified.self-test",
                "source_locator": "Self-test source acquisition record SRC-001",
                "present_content_item_ids": '["self-test.definitions.present"]',
            },
            {
                "coverage_id": "SRC-002",
                "packet_id": "verified.self-test",
                "source_locator": "Second exact source locator",
                "present_content_item_ids": '["self-test.definitions.present"]',
            },
        ]
        self.write_admission(admitted=True)

    def test_packet_declared_assignment_must_occur_identically_in_sidecar(self) -> None:
        bad = copy.deepcopy(self.sidecar_rows)
        bad[0]["source_locator"] = "Different locator"
        self.sidecar_rows = bad
        self.write_sidecar(bad)
        self.write_index(include_sidecar=True)
        with self.assertRaisesRegex(ValueError, "packet-declared assignment differs"):
            self.check()

        self.setUp_fresh_rows()
        self.sidecar_rows = [self.sidecar_rows[1]]
        self.write_sidecar(self.sidecar_rows)
        self.write_index(include_sidecar=True)
        with self.assertRaisesRegex(ValueError, "packet-declared assignment is absent"):
            self.check()

    def test_stale_digests_metadata_and_traversal_fail_closed(self) -> None:
        for field in (
            "coverage_manifest_sha256",
            "packet_admission_sha256",
        ):
            value = self.index(include_sidecar=True)
            value[field] = "0" * 64
            self.index_path.write_text(json.dumps(value) + "\n", encoding="utf-8")
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "digest drift"):
                self.check()
        value = self.index(include_sidecar=True)
        value["sidecars"][0]["assignment_count"] = 999  # type: ignore[index]
        self.index_path.write_text(json.dumps(value) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "assignment count drift"):
            self.check()
        value = self.index(include_sidecar=True)
        value["sidecars"][0]["sidecar_path"] = "../outside.csv"  # type: ignore[index]
        self.index_path.write_text(json.dumps(value) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "inside repository"):
            self.check()

    def test_index_schema_accepts_exact_document(self) -> None:
        schema_path = (
            Path(__file__).resolve().parents[1]
            / "spec/external-coverage-assignment-index.schema.json"
        )
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        document = self.index(include_sidecar=True)
        jsonschema.Draft202012Validator(schema).validate(document)
        document["unexpected"] = True
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(schema).validate(document)


if __name__ == "__main__":
    unittest.main()
