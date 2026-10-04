#!/usr/bin/env python3
"""Focused tests for the terminal readiness manifest and release gate."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import jsonschema

from tools import check_external_coverage_assignments as coverage_checker
from tools import check_terminal_readiness as terminal


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def csv_raw(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


class TerminalReadinessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="terminal-readiness-")
        self.root = Path(self.temporary.name)
        (self.root / "spec/verification").mkdir(parents=True)
        (self.root / "spec/provenance").mkdir(parents=True)
        (self.root / "handbook").mkdir()
        self.pdf_raw = b"test final PDF bytes"
        self.write("handbook/main.pdf", self.pdf_raw)
        self.paths = terminal.ReadinessPaths(
            inherited_source_map=Path("spec/source-map.csv"),
            restoration_record_root=Path("spec/provenance"),
            source_units=Path("spec/source.csv"),
            handbook_units=Path("spec/handbook.csv"),
            register_obligations=Path("spec/register.csv"),
            acquisition_gaps=Path("spec/acquisition.csv"),
            packet_admissions=Path("spec/packets.csv"),
            coverage_index=Path("spec/coverage-index.json"),
            publication_manifest=Path("spec/compendium-volume-manifest.json"),
            readiness_manifest=Path("spec/verification/terminal-readiness-manifest.json"),
            user_final_acceptance=Path("spec/provenance/user-final-acceptance.json"),
        )
        self.expected = {
            "inherited_interval_restoration": 3,
            "source_unit_admission": 2,
            "handbook_unit_admission": 2,
            "register_obligation_closure": 2,
            "acquisition_gap_resolution": 2,
        }
        self.write_publication(release=False)
        self.write_ledgers(passing=False)
        self.write(
            "spec/source-map.csv",
            b"stable_id,source_start,source_end,source_sha256\n"
            + b"SRC-A,1,2," + b"0" * 64 + b"\n"
            + b"SRC-B,3,4," + b"1" * 64 + b"\n"
            + b"SRC-C,5,6," + b"2" * 64 + b"\n",
        )
        source_map_raw = (self.root / "spec/source-map.csv").read_bytes()
        self.interval_open = terminal.IntervalRestorationResult(
            3, 0, 3, 0, "0" * 64, digest(source_map_raw), len(source_map_raw)
        )
        self.interval_complete = terminal.IntervalRestorationResult(
            3, 3, 0, 3, "1" * 64, digest(source_map_raw), len(source_map_raw)
        )
        self.source_order_open = terminal.SourceOrderResult(3, "2" * 64, 4)
        self.source_order_complete = terminal.SourceOrderResult(0, "3" * 64, 5)
        self.coverage_open = coverage_checker.CoverageAssignmentResult(5, 0, 5, 0, 0)
        self.coverage_complete = coverage_checker.CoverageAssignmentResult(5, 5, 0, 1, 1)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, raw: bytes) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return path

    def review_columns(self, value: str) -> dict[str, str]:
        return {f"{name}_verification": value for name in terminal.REVIEW_GATES}

    def write_ledgers(self, *, passing: bool) -> None:
        review = "pass" if passing else "pending"
        source_rows = [
            {
                "unit_ordinal": str(index),
                "provenance_disposition": "full transcription" if passing else "open/missing",
                "audit_result": "full-and-accurate" if passing else "pending/unclassified",
                **self.review_columns(review),
            }
            for index in (1, 2)
        ]
        self.write(
            "spec/source.csv",
            csv_raw(list(source_rows[0]), source_rows),
        )
        handbook_rows = [
            {
                "unit_id": f"HBU-{index}",
                "mapping_status": "mapped/reviewed" if passing else "open/unmapped",
                "semantic_review_status": "pass" if passing else "pending",
                **self.review_columns(review),
            }
            for index in (1, 2)
        ]
        self.write("spec/handbook.csv", csv_raw(list(handbook_rows[0]), handbook_rows))
        register_rows = [
            {
                "obligation_id": f"OBL-{index}",
                "completion_status": "COMPLETE" if passing else "OPEN",
                **self.review_columns(review),
            }
            for index in (1, 2)
        ]
        self.write("spec/register.csv", csv_raw(list(register_rows[0]), register_rows))
        gap_rows = [
            {
                "acquisition_id": f"ACQ-{index}",
                "resolution_status": "RESOLVED" if passing else "OPEN",
                **self.review_columns(review),
            }
            for index in (1, 2)
        ]
        self.write("spec/acquisition.csv", csv_raw(list(gap_rows[0]), gap_rows))
        packet_fields = [
            "packet_id",
            "admission_status",
            *[f"{name}_verification" for name in terminal.REVIEW_GATES],
        ]
        self.write("spec/packets.csv", csv_raw(packet_fields, []))
        self.write("spec/coverage-index.json", b"{}\n")

    def publication(self, *, release: bool, final_evidence: object = None) -> dict[str, object]:
        return {
            "schema_version": 2,
            "manifest_kind": "single-publication-handbook",
            "title": terminal.BOOK_TITLE,
            "public_artifact": {
                "artifact_id": "the-methods-of-reason",
                "title": terminal.BOOK_TITLE,
                "path": terminal.PUBLIC_PDF_PATH,
                "artifact_kind": "pdf",
                "publication_status": "release" if release else "construction-draft",
                "release_ready": release,
                "observed": {
                    "bytes": len(self.pdf_raw),
                    "pages": 1,
                    "sha256": digest(self.pdf_raw),
                },
            },
            "internal_authority_evidence": {
                "inherited_corpus_manifest": "spec/inherited-corpus-manifest.json",
                "published_with_book": False,
            },
            "final_release_evidence": final_evidence,
        }

    def write_publication(self, *, release: bool, final_evidence: object = None) -> None:
        value = self.publication(release=release, final_evidence=final_evidence)
        self.write(
            "spec/compendium-volume-manifest.json",
            (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
        )

    def build(self, coverage: coverage_checker.CoverageAssignmentResult) -> tuple[dict[str, object], bytes]:
        interval = (
            self.interval_complete
            if coverage is self.coverage_complete
            else self.interval_open
        )
        source_order = (
            self.source_order_complete
            if coverage is self.coverage_complete
            else self.source_order_open
        )
        return terminal.build_readiness_manifest(
            self.root,
            self.paths,
            expected_counts=self.expected,
            interval_result=interval,
            source_order_result=source_order,
            coverage_result=coverage,
            validate_publication=False,
        )

    def write_readiness(self, raw: bytes) -> Path:
        return self.write("spec/verification/terminal-readiness-manifest.json", raw)

    def acceptance(self, readiness_raw: bytes) -> dict[str, object]:
        return {
            "schema_version": 1,
            "record_kind": "user_final_acceptance",
            "acceptance_status": "accepted",
            "publication_title": terminal.BOOK_TITLE,
            "public_pdf": {
                "path": terminal.PUBLIC_PDF_PATH,
                "sha256": digest(self.pdf_raw),
                "bytes": len(self.pdf_raw),
                "pages": 1,
            },
            "readiness_manifest": {
                "path": self.paths.readiness_manifest.as_posix(),
                "sha256": digest(readiness_raw),
            },
            "accepted_by": "repository user",
            "accepted_at": "2026-08-13T12:00:00-07:00",
            "acceptance_statement": "I accept this exact final public PDF for release.",
        }

    def test_open_manifest_reports_exact_residuals_and_acceptance_absent(self) -> None:
        value, raw = self.build(self.coverage_open)
        self.assertEqual(value["readiness_status"], "OPEN")
        self.assertEqual(
            value["gates"]["external_coverage_assignment"]["residual"], 5  # type: ignore[index]
        )
        self.assertEqual(
            value["user_final_acceptance"]["status"], "absent"  # type: ignore[index]
        )
        self.assertEqual(raw, terminal.manifest_bytes(value))

    def test_metadata_reconciliation_does_not_credit_presentation_content(self) -> None:
        coverage = coverage_checker.CoverageAssignmentResult(
            5, 1, 1, 1, 1, metadata_disposition_count=3, metadata_batch_count=1
        )
        value, _ = self.build(coverage)
        gate = value["gates"]["external_coverage_assignment"]
        self.assertEqual((gate["required"], gate["pass"], gate["residual"]), (5, 4, 1))
        self.assertEqual((gate["content_assignment_count"], gate["metadata_disposition_count"], gate["metadata_batch_count"]), (1, 3, 1))
        baseline, _ = self.build(self.coverage_open)
        self.assertEqual(value["gates"]["presentation_packet_content_admission"], baseline["gates"]["presentation_packet_content_admission"])
        schema = json.loads((terminal.ROOT / "spec/terminal-readiness-manifest.schema.json").read_text())
        jsonschema.Draft202012Validator(schema).validate(value)

    def test_corrected_pair_counts_only_with_all_six_gate_columns(self) -> None:
        row = {
            "unit_ordinal": "1",
            "provenance_disposition": "full reconstruction",
            "audit_result": "corrected-and-verified",
            **self.review_columns("pass"),
        }
        # Live provenance/snapshot reproduction is covered by the source-unit
        # fixture tests. Here test the final CSV gate's independent predicate.
        def count(value: dict[str, str]) -> int:
            self.write("spec/source.csv", csv_raw(list(value), [value]))
            gate = terminal.read_csv_gate(
                self.root, self.paths.source_units, "source_unit_admission", "unit_ordinal",
                terminal.source_unit_checker.is_terminal_source_unit, 1,
            )
            return gate["pass"]

        self.assertEqual(count(row), 1)
        for name in terminal.REVIEW_GATES:
            for value in ("pending", "fail"):
                with self.subTest(gate=name, result=value):
                    self.assertEqual(count({**row, f"{name}_verification": value}), 0)
            missing = dict(row); del missing[f"{name}_verification"]
            with self.subTest(missing=name), self.assertRaisesRegex(ValueError, "required unique"):
                count(missing)
        for disposition, result in (
            ("open/missing", "corrected-and-verified"),
            ("full transcription", "corrected-and-verified"),
            ("full reconstruction", "full-and-accurate"),
            ("full reconstruction", "layout-only relocation"),
        ):
            with self.subTest(disposition=disposition, result=result):
                self.assertEqual(count({**row, "provenance_disposition": disposition, "audit_result": result}), 0)

    def test_acceptance_is_pending_only_after_all_other_residuals_are_zero(self) -> None:
        self.write_ledgers(passing=True)
        value, raw = self.build(self.coverage_complete)
        self.assertEqual(value["readiness_status"], "AWAITING_USER_FINAL_ACCEPTANCE")
        self.assertEqual(value["non_user_residual_count"], 0)
        self.assertEqual(value["user_final_acceptance"]["status"], "pending")  # type: ignore[index]
        self.write_readiness(raw)
        with self.assertRaisesRegex(ValueError, "user final acceptance record is missing"):
            terminal.validate_terminal_release(self.root, self.paths, value, raw)

    def test_generator_reproduced_contract_supersession_is_terminal_but_not_completion(self) -> None:
        self.write_ledgers(passing=True)
        register_rows = [
            {
                "obligation_id": "OBL-COMPLETE",
                "completion_status": "COMPLETE",
                **self.review_columns("pass"),
            },
            {
                "obligation_id": "OBL-SUPERSEDED",
                "completion_status": "SUPERSEDED_BY_CONTRACT",
                **self.review_columns("pass"),
            },
        ]
        self.write(
            "spec/register.csv",
            csv_raw(list(register_rows[0]), register_rows),
        )
        value, _raw = self.build(self.coverage_complete)
        gate = value["gates"]["register_obligation_closure"]  # type: ignore[index]
        self.assertEqual(gate["pass"], 2)
        self.assertEqual(gate["residual"], 0)
        self.assertEqual(gate["status"], "PASS")
        self.assertEqual(value["readiness_status"], "AWAITING_USER_FINAL_ACCEPTANCE")

    def test_premature_acceptance_is_rejected(self) -> None:
        self.write(
            "spec/provenance/user-final-acceptance.json",
            b'{"acceptance_status":"accepted"}\n',
        )
        with self.assertRaisesRegex(ValueError, "must be absent while non-user residuals remain"):
            self.build(self.coverage_open)

    def test_valid_acceptance_and_release_pins_both_records_and_pdf(self) -> None:
        self.write_ledgers(passing=True)
        value, raw = self.build(self.coverage_complete)
        readiness_path = self.write_readiness(raw)
        acceptance_value = self.acceptance(raw)
        acceptance_raw = (json.dumps(acceptance_value, indent=2) + "\n").encode("utf-8")
        acceptance_path = self.write(
            "spec/provenance/user-final-acceptance.json", acceptance_raw
        )
        final = {
            "readiness_manifest_path": self.paths.readiness_manifest.as_posix(),
            "readiness_manifest_sha256": digest(readiness_path.read_bytes()),
            "user_final_acceptance_path": self.paths.user_final_acceptance.as_posix(),
            "user_final_acceptance_sha256": digest(acceptance_path.read_bytes()),
            "public_pdf_sha256": digest(self.pdf_raw),
        }
        self.write_publication(release=True, final_evidence=final)
        rebuilt_value, rebuilt_raw = self.build(self.coverage_complete)
        self.assertEqual(rebuilt_value, value)
        self.assertEqual(rebuilt_raw, raw)
        terminal.validate_terminal_release(self.root, self.paths, value, raw)

    def test_stale_acceptance_readiness_and_pdf_pins_fail_closed(self) -> None:
        self.write_ledgers(passing=True)
        value, raw = self.build(self.coverage_complete)
        self.write_readiness(raw)
        acceptance = self.acceptance(raw)
        acceptance["readiness_manifest"]["sha256"] = "0" * 64  # type: ignore[index]
        self.write(
            "spec/provenance/user-final-acceptance.json",
            (json.dumps(acceptance) + "\n").encode("utf-8"),
        )
        with self.assertRaisesRegex(ValueError, "readiness manifest digest drift"):
            terminal.validate_terminal_release(self.root, self.paths, value, raw)

    def test_non_integer_acceptance_schema_version_is_rejected(self) -> None:
        self.write_ledgers(passing=True)
        value, raw = self.build(self.coverage_complete)
        self.write_readiness(raw)
        for invalid_version in (True, 1.0):
            acceptance = self.acceptance(raw)
            acceptance["schema_version"] = invalid_version
            acceptance_raw = (json.dumps(acceptance) + "\n").encode("utf-8")
            self.write("spec/provenance/user-final-acceptance.json", acceptance_raw)
            with self.assertRaisesRegex(ValueError, "schema_version"):
                terminal.validate_terminal_release(self.root, self.paths, value, raw)

    def test_manifest_and_acceptance_schemas_are_exact(self) -> None:
        value, _raw = self.build(self.coverage_open)
        schema_root = Path(__file__).resolve().parents[1] / "spec"
        readiness_schema = json.loads(
            (schema_root / "terminal-readiness-manifest.schema.json").read_text(encoding="utf-8")
        )
        readiness_validator = jsonschema.Draft202012Validator(readiness_schema)
        readiness_validator.validate(value)
        # JSON Schema defines 1.0 as an integer-valued number. The release
        # path above additionally rejects Python float aliases; the schema
        # itself rejects booleans and nonintegral numbers.
        for invalid_version in (True, 1.5):
            invalid_readiness = json.loads(json.dumps(value))
            invalid_readiness["schema_version"] = invalid_version
            with self.assertRaises(jsonschema.ValidationError):
                readiness_validator.validate(invalid_readiness)
        acceptance_schema = json.loads(
            (schema_root / "provenance/user-final-acceptance.schema.json").read_text(encoding="utf-8")
        )
        acceptance = self.acceptance(b"readiness\n")
        acceptance_validator = jsonschema.Draft202012Validator(acceptance_schema)
        acceptance_validator.validate(acceptance)
        for invalid_version in (True, 1.5):
            invalid_acceptance = json.loads(json.dumps(acceptance))
            invalid_acceptance["schema_version"] = invalid_version
            with self.assertRaises(jsonschema.ValidationError):
                acceptance_validator.validate(invalid_acceptance)
        acceptance["human_content_review"] = "pass"
        with self.assertRaises(jsonschema.ValidationError):
            acceptance_validator.validate(acceptance)

    def test_interval_accounting_requires_exact_once_coverage(self) -> None:
        intervals = [("SRC-09099-09111", 9099, 9111)]
        self.assertEqual(
            terminal.exact_interval_accounted_count(
                intervals, [("SRC-09099-09111", 9099, 9111)]
            ),
            1,
        )
        self.assertEqual(
            terminal.exact_interval_accounted_count(
                intervals,
                [
                    ("SRC-09099-09111", 9099, 9111),
                    ("SRC-09099-09111", 9099, 9111),
                ],
            ),
            0,
        )
        self.assertEqual(
            terminal.exact_interval_accounted_count(
                intervals,
                [
                    ("SRC-09099-09111", 9099, 9104),
                    ("SRC-09099-09111", 9105, 9111),
                ],
            ),
            1,
        )

    def test_upstream_restoration_preflight_uses_its_read_only_cli(self) -> None:
        commands: list[list[str]] = []

        def successful_run(command: list[str], **_kwargs: object) -> object:
            commands.append(command)
            return terminal.subprocess.CompletedProcess(command, 0, "", "")

        with mock.patch.object(terminal.subprocess, "run", side_effect=successful_run):
            terminal.run_upstream_checks(self.root)

        self.assertEqual(
            commands[0],
            [terminal.sys.executable, "tools/check_inherited_restoration.py"],
        )
        self.assertTrue(
            all(command[-1] == "--check" for command in commands[1:]),
            commands,
        )
        self.assertIn(
            [
                terminal.sys.executable,
                "tools/build_register_obligation_closure.py",
                "--check",
            ],
            commands,
        )

    def test_stale_hand_edited_register_projection_stops_before_readiness_aggregation(self) -> None:
        with (
            mock.patch.object(
                terminal,
                "run_upstream_checks",
                side_effect=ValueError(
                    "upstream register closure check failed: register obligation closure CSV is stale"
                ),
            ),
            mock.patch.object(terminal, "build_readiness_manifest") as build,
        ):
            result = terminal.main(
                ["--repository-root", str(self.root), "--check"]
            )
        self.assertEqual(result, 1)
        build.assert_not_called()


if __name__ == "__main__":
    unittest.main()
