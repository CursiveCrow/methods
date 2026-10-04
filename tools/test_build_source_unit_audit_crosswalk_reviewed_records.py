#!/usr/bin/env python3
"""Adversarial tests for reviewer-supplied source-unit data."""

from __future__ import annotations

import copy
import hashlib
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

import jsonschema

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import build_source_unit_audit_crosswalk as target
import audit_tables
from tools import check_terminal_readiness as terminal
from tools.test_check_inherited_restoration import make_corrected_reader_fixture


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class ReviewedSourceUnitRecordTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)

        self.authority_bytes = target.DEFAULT_SOURCE.read_bytes()
        self.authority_hash = digest(self.authority_bytes)
        self.assertEqual(self.authority_hash, target.AUTHORITY_SHA256)
        self._write_bytes(target.AUTHORITY_PATH, self.authority_bytes)
        self.authority_lines = self.authority_bytes.splitlines(keepends=True)
        self._write_bytes(
            "spec/inherited-corpus-manifest.json",
            (target.ROOT / "spec/inherited-corpus-manifest.json").read_bytes(),
        )

        self.destination_path = "handbook/parts/p01/synthetic.tex"
        self.destination_bytes = (
            b"\\section{One}\\label{def:p01-unit-one}\n"
            b"\\begin{hbdefinition}{def:p01-unit-two}{Two}\n"
            b"Body.\n\\end{hbdefinition}\n"
        )
        self._write_bytes(self.destination_path, self.destination_bytes)

        self.evidence_paths: dict[str, str] = {}
        for kind in target.VERIFICATION_FIELDS:
            path = f"spec/evidence/{kind}.txt"
            self._write_bytes(path, f"recorded {kind} evidence\n".encode())
            self.evidence_paths[kind] = path

        self.review_path = self.root / "spec/provenance/reviewed.json"
        self.rows = [self._base_row(1), self._base_row(2)]
        inventory = (
            "ordinal,kind,title,label,start_line,end_line,sha256\n"
            + "\n".join(
                ",".join(
                    (
                        row["unit_ordinal"],
                        row["unit_kind"],
                        row["unit_title"],
                        row["unit_source_label"],
                        row["source_start"],
                        row["source_end"],
                        row["source_sha256"],
                    )
                )
                for row in self.rows
            )
            + "\n"
        ).encode()
        self._write_bytes("spec/source-unit-inventory.csv", inventory)
        audit_rows = [
            (10, 22),
            (20, 22),
        ]
        audit_map = (
            "stable_id,source_start,source_end,source_sha256,class_normalized\n"
            + "\n".join(
                f"AUDIT-{start:05d}-{end:05d},{start},{end},"
                f"{digest(b''.join(self.authority_lines[start - 1:end]))},"
                "full-and-accurate"
                for start, end in audit_rows
            )
            + "\n"
        ).encode()
        self._write_bytes("spec/inherited-source-map.csv", audit_map)

        self.restoration_provenance_id = "SRC-00010-00022"
        self.restoration_record_path = self._write_restoration_record(
            self.restoration_provenance_id, 10, 22, [1, 2]
        )
        self._write_bytes(
            "handbook/main.tex",
            (
                "\\input{restoration/scope-"
                f"{self.restoration_provenance_id}"
                "}\n"
            ).encode(),
        )

    def _write_bytes(self, relative_path: str, content: bytes) -> Path:
        path = self.root / Path(*relative_path.split("/"))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def _base_row(self, ordinal: int) -> dict[str, str]:
        start = 10 * ordinal
        end = start + 2
        row = {field: "" for field in target.OUTPUT_FIELDS}
        row.update(
            {
                "unit_ordinal": str(ordinal),
                "unit_kind": "definition",
                "unit_title": f"Synthetic unit {ordinal}",
                "unit_source_label": f"src:unit-{ordinal}",
                "source_start": str(start),
                "source_end": str(end),
                "source_sha256": digest(
                    b"".join(self.authority_lines[start - 1 : end])
                ),
                "authority_path": target.AUTHORITY_PATH,
                "authority_sha256": self.authority_hash,
                "authority_edition_status": "pending",
                "presentation_identity_status": "open/missing",
                "audit_interval_ids": "[]",
                "audit_class_evidence": "[]",
                "provenance_disposition": "open/missing",
                "audit_result": "pending",
                "handbook_destination_status": "open/missing",
                "stable_labels": "[]",
            }
        )
        for field in target.COMPLETENESS_FIELDS:
            row[f"{field}_completeness"] = "pending"
        for field in target.VERIFICATION_FIELDS:
            row[target.VERIFICATION_OUTPUT_FIELDS[field]] = "pending"
        return row

    def _write_restoration_record(
        self, provenance_id: str, start: int, end: int, ordinals: list[int]
    ) -> str:
        artifact = b"".join(self.authority_lines[start - 1 : end])
        artifact_path = f"handbook/restoration/inherited-{start:05d}-{end:05d}.tex"
        self._write_bytes(artifact_path, artifact)
        exact_units = [
            row
            for row in self.rows
            if int(row["source_start"]) == start and int(row["source_end"]) == end
        ]
        identity_kind = "source interval"
        identity_title = f"Synthetic restoration {start}--{end}"
        if len(exact_units) == 1:
            identity_kind = exact_units[0]["unit_kind"]
            identity_title = exact_units[0]["unit_title"]
        record = {
            "schema_version": 1,
            "provenance_id": provenance_id,
            "authority": {
                "path": target.AUTHORITY_PATH,
                "edition": target.AUTHORITY_EDITION,
                "corpus_manifest": "spec/inherited-corpus-manifest.json",
                "bytes": len(self.authority_bytes),
                "physical_lines": len(self.authority_lines),
                "sha256": self.authority_hash,
            },
            "source_locator": {
                "start_line": start,
                "end_line": end,
                "line_count": end - start + 1,
                "interval_sha256": digest(artifact),
            },
            "source_unit_evidence": {
                "inventory": "spec/source-unit-inventory.csv",
                "unit_ordinals": ordinals,
            },
            "artifact_line_standing": "reader-facing content",
            "presentation_identity": {
                "kind": identity_kind,
                "source_title": identity_title,
                "description": "Exact test interval used by the admission checks.",
            },
            "restoration_artifact": {
                "path": artifact_path,
                "bytes": len(artifact),
                "physical_lines": len(artifact.splitlines(keepends=True)),
                "sha256": digest(artifact),
                "content_token_sha256": digest(
                    target.inherited_restoration.canonical_content_token_bytes(
                        artifact.splitlines(keepends=True), "test restoration"
                    )
                ),
                "content_token_comparison": (
                    target.inherited_restoration.CONTENT_TOKEN_COMPARISON
                ),
            },
            "handbook_destination": {
                "status": "open/missing",
                "file": "",
                "stable_label": "",
                "reason": "Destination review remains open.",
            },
            "disposition": "full transcription",
            "audit_evidence": {
                "source_map": "spec/inherited-source-map.csv",
                "interval_ids": [f"AUDIT-{start:05d}-{end:05d}"],
                "classifications": ["full-and-accurate"],
            },
            "completeness": {
                field: "pending"
                for field in target.inherited_restoration.COMPLETENESS_FIELDS
            },
            "verification": {
                "source": "pass",
                "independent_source": "pending",
                "static": "pass",
                "build": "pending",
                "visual": "pending",
                "human_review": "pending",
            },
            "verification_evidence": [
                {
                    "kind": kind,
                    "checker": "tools/check_inherited_restoration.py",
                    "command": "test command",
                    "scope": f"Test {kind} scope.",
                }
                for kind in ("source", "static")
            ],
            "owed_artifacts": ["Complete the remaining review."],
        }
        record_path = f"spec/provenance/{provenance_id}.json"
        self._write_bytes(
            record_path, (json.dumps(record, indent=2) + "\n").encode()
        )
        self._write_bytes(
            f"handbook/restoration/scope-{provenance_id}.tex",
            (
                f"\\begin{{inheritedrestorationscope}}{{{provenance_id}}}\n"
                f"\\input{{{artifact_path.removeprefix('handbook/').removesuffix('.tex')}}}\n"
                "\\end{inheritedrestorationscope}\n"
            ).encode(),
        )
        return record_path

    def _record(self, ordinal: int = 1, label: str | None = None) -> dict[str, object]:
        base = self.rows[ordinal - 1]
        label = label or f"def:p01-unit-{'one' if ordinal == 1 else 'two'}"
        evidence: list[dict[str, object]] = []
        for kind in target.VERIFICATION_FIELDS:
            relative_path = self.evidence_paths[kind]
            evidence_path = self.root / Path(*relative_path.split("/"))
            evidence.append(
                {
                    "category": kind,
                    "recorded_result": "pass",
                    "artifact_path": relative_path,
                    "sha256": digest(evidence_path.read_bytes()),
                    "producer_identity": f"producer for {kind}",
                    "recorded_scope": f"unit {ordinal} {kind} check",
                    **(
                        {
                            "model": f"fixture-model-{kind}",
                            "model_version": "1",
                            "instructions": f"Review unit {ordinal} for {kind}.",
                            "consulted_authorities": [
                                {
                                    "path": target.AUTHORITY_PATH,
                                    "locator": (
                                        f"lines {base['source_start']}--"
                                        f"{base['source_end']}"
                                    ),
                                    "sha256": self.authority_hash,
                                }
                            ],
                            "findings": ["No fixture defect found."],
                            "other_review_outputs_consulted": False,
                        }
                        if kind in target.AI_REVIEW_FIELDS
                        else {}
                    ),
                }
            )
        return {
            "unit_ordinal": ordinal,
            "unit_kind": base["unit_kind"],
            "unit_title": base["unit_title"],
            "unit_source_label": base["unit_source_label"],
            "source_start": int(base["source_start"]),
            "source_end": int(base["source_end"]),
            "source_sha256": base["source_sha256"],
            "restoration_record_path": self.restoration_record_path,
            "restoration_record_sha256": digest(
                (self.root / self.restoration_record_path).read_bytes()
            ),
            "restoration_provenance_id": self.restoration_provenance_id,
            "authority_path": target.AUTHORITY_PATH,
            "authority_sha256": self.authority_hash,
            "authority_edition_status": "identified",
            "authority_edition_value": target.AUTHORITY_EDITION,
            "presentation_identity_status": "identified",
            "presentation_identity_value": f"presentation-{ordinal}",
            "presentation_identity_description": (
                f"{base['unit_kind']} at authority lines "
                f"{base['source_start']}--{base['source_end']}"
            ),
            "provenance_disposition": "full transcription",
            "handbook_destination_status": "identified",
            "handbook_destination": self.destination_path,
            "handbook_destination_sha256": digest(self.destination_bytes),
            "stable_labels": [label],
            "audit_result": "full-and-accurate",
            "layout_changes": [],
            "defect_exclusions": list(target.DEFECT_EXCLUSIONS),
            "variant_links": [],
            "completeness": {field: "pass" for field in target.COMPLETENESS_FIELDS},
            "verification": {field: "pass" for field in target.VERIFICATION_FIELDS},
            "verification_evidence": evidence,
        }

    def _open_record(
        self, ordinal: int = 1, *, stable_labels: list[str] | None = None
    ) -> dict[str, object]:
        record = self._record(ordinal)
        record["provenance_disposition"] = target.OPEN_DISPOSITION
        record["stable_labels"] = [] if stable_labels is None else stable_labels
        record["audit_result"] = target.PENDING_AUDIT_RESULT
        record["layout_changes"] = []
        record["defect_exclusions"] = []
        record["completeness"] = {
            field: "pending" for field in target.COMPLETENESS_FIELDS
        }
        record["verification"] = {
            "source_fidelity_ai": "pending",
            "topic_specialist_ai": "pending",
            "adversarial_publication_ai": "pending",
            "static": "pass",
            "build": "pending",
            "visual": "pending",
        }
        independent_path = self.evidence_paths["source_fidelity_ai"]
        independent_file = self.root / Path(*independent_path.split("/"))
        restoration_file = self.root / self.restoration_record_path
        record["verification_evidence"] = [
            {
                "category": "source_fidelity_ai",
                "recorded_result": "pending",
                "artifact_path": independent_path,
                "sha256": digest(independent_file.read_bytes()),
                "producer_identity": "independent source auditor",
                "recorded_scope": f"unit {ordinal} exact source comparison",
            },
            {
                "category": "static",
                "recorded_result": "pass",
                "artifact_path": self.restoration_record_path,
                "sha256": digest(restoration_file.read_bytes()),
                "producer_identity": "restoration record checker",
                "recorded_scope": f"unit {ordinal} static restoration validation",
            },
        ]
        return record

    def _variant_link(self, ordinal: int) -> dict[str, object]:
        base = self.rows[ordinal - 1]
        return {
            "unit_ordinal": ordinal,
            "unit_source_label": base["unit_source_label"],
            "source_start": int(base["source_start"]),
            "source_end": int(base["source_end"]),
            "source_sha256": base["source_sha256"],
            "relationship": "separately presented source variant",
        }

    def _linked_records(self) -> tuple[dict[str, object], dict[str, object]]:
        first = self._record(1)
        second = self._record(2)
        first["variant_links"] = [self._variant_link(2)]
        second["variant_links"] = [self._variant_link(1)]
        return first, second

    def _document(self, records: list[dict[str, object]]) -> dict[str, object]:
        return {
            "schema_version": target.REVIEW_SCHEMA_VERSION,
            "authority_path": target.AUTHORITY_PATH,
            "authority_sha256": self.authority_hash,
            "records": records,
        }

    def _apply_document(self, document: dict[str, object]) -> list[dict[str, str]]:
        self.review_path.parent.mkdir(parents=True, exist_ok=True)
        self.review_path.write_text(
            json.dumps(document, indent=2) + "\n", encoding="utf-8"
        )
        return target.apply_reviewed_records(
            self.rows, self.review_path, self.authority_hash, self.root
        )

    def _apply_records(self, *records: dict[str, object]) -> list[dict[str, str]]:
        return self._apply_document(self._document(list(records)))

    def _point_record_at(
        self, record: dict[str, object], path: str, content: bytes, label: str
    ) -> None:
        self._write_bytes(path, content)
        record["handbook_destination"] = path
        record["handbook_destination_sha256"] = digest(content)
        record["stable_labels"] = [label]

    def test_valid_record_overrides_only_reviewed_unit(self) -> None:
        original_rows = copy.deepcopy(self.rows)
        result = self._apply_records(self._record())

        self.assertEqual(result[0]["provenance_disposition"], "full transcription")
        self.assertEqual(result[0]["handbook_destination"], self.destination_path)
        self.assertEqual(json.loads(result[0]["stable_labels"]), ["def:p01-unit-one"])
        for field in target.COMPLETENESS_FIELDS:
            self.assertEqual(result[0][f"{field}_completeness"], "pass")
        for field in target.VERIFICATION_FIELDS:
            self.assertEqual(
                result[0][target.VERIFICATION_OUTPUT_FIELDS[field]], "pass"
            )
        self.assertEqual(result[1], original_rows[1])
        self.assertEqual(self.rows, original_rows, "input rows must not be mutated")

    def _corrected_records(self, labels: tuple[str, str] = (
        "def:p01-unit-one", "def:p01-unit-two",
    )) -> list[dict[str, object]]:
        """A real v4 fixture with separately recorded six-gate unit evidence."""
        corrected = make_corrected_reader_fixture(
            self.root, self.root / self.restoration_record_path,
            [(0, 0, (f"\\begin{{definition}}[One]\\label{{{labels[0]}}}\n"
                     "Corrected fixture one.\n\\end{definition}\n"
                     f"\\begin{{definition}}[Two]\\label{{{labels[1]}}}\n"
                     "Corrected fixture two.\n\\end{definition}\n").encode())],
        )
        self._write_bytes("handbook/main.tex", b"\\input{parts/p01}\n")
        self._write_bytes("handbook/parts/p01.tex", (
            f"\\input{{restoration/scope-{self.restoration_provenance_id}}}\n"
        ).encode())
        records = [self._record(ordinal) for ordinal in (1, 2)]
        for record in records:
            record.update({
                "provenance_disposition": target.CORRECTED_DISPOSITION,
                "audit_result": target.CORRECTED_AUDIT_RESULT,
                "defect_exclusions": list(target.CORRECTED_DEFECT_EXCLUSIONS),
                "presentation_identity_value": (
                    f"{self.restoration_provenance_id}:fixture.correction:unit-{record['unit_ordinal']}"
                ),
                "handbook_destination": corrected["restoration_artifact"]["path"],
                "handbook_destination_sha256": corrected["restoration_artifact"]["sha256"],
                "stable_labels": [labels[record["unit_ordinal"] - 1]],
            })
            for evidence in record["verification_evidence"]:
                evidence["correction_snapshot"] = {
                    field: record[field] for field in target.CORRECTION_SNAPSHOT_FIELDS
                }
        self.review_path = self.root / "spec/provenance/reviewed-source-unit-records.json"
        return records

    def test_corrected_six_gate_records_pass_schema_admission_and_active_audit(self) -> None:
        records = self._corrected_records()
        schema = json.loads((target.ROOT / "spec/provenance/reviewed-source-unit-records.schema.json").read_text())
        jsonschema.Draft202012Validator(schema).validate(self._document(records))
        rows = self._apply_records(*records)
        self.assertTrue(all(target.is_terminal_source_unit(row) for row in rows))
        terminal.validate_corrected_source_rows(self.root, rows)
        target.require_corrected_reader_admissions(self.root, {self.restoration_provenance_id})
        with mock.patch.object(sys, "argv", ["audit_tables.py", "--root", str(self.root)]), redirect_stdout(io.StringIO()):
            self.assertEqual(audit_tables.main(), 0)
        self.assertTrue((self.root / "handbook/generated/audit-p01.tex").is_file())

    def test_legacy_six_gate_record_is_schema_valid(self) -> None:
        schema = json.loads((target.ROOT / "spec/provenance/reviewed-source-unit-records.schema.json").read_text())
        jsonschema.Draft202012Validator(schema).validate(self._document([self._record()]))

    def test_corrected_restoration_lemma_and_method_labels_pass_schema_and_python(self) -> None:
        records = self._corrected_records(("lem:relativization-derivations", "method:back-and-forth"))
        schema = json.loads((target.ROOT / "spec/provenance/reviewed-source-unit-records.schema.json").read_text())
        validator = jsonschema.Draft202012Validator(schema)
        validator.validate(self._document(records))
        rows = self._apply_records(*records)
        terminal.validate_corrected_source_rows(self.root, rows)
        target.require_corrected_reader_admissions(self.root, {self.restoration_provenance_id})
        for record in records:
            editorial = copy.deepcopy(record)
            editorial["handbook_destination"] = self.destination_path
            with self.subTest(editorial_label=record["stable_labels"][0]):
                with self.assertRaises(jsonschema.ValidationError):
                    validator.validate(self._document([editorial]))
                with self.assertRaisesRegex(ValueError, "substantive part-owned label"):
                    target.validate_unit_label(record["stable_labels"][0], "part", "p01", "fixture")

    def test_terminal_selection_uses_live_corrected_units_and_preserves_open_candidates(self) -> None:
        records = self._corrected_records()
        admitted_rows = self._apply_records(*records)
        terminal.validate_corrected_source_rows(self.root, admitted_rows)
        false_markers = copy.deepcopy(admitted_rows)
        false_markers[0]["provenance_disposition"] = target.PASSING_DISPOSITION
        false_markers[0]["audit_result"] = "full-and-accurate"
        with self.assertRaisesRegex(ValueError, "differs from validated admission"):
            terminal.validate_corrected_source_rows(self.root, false_markers)
        # This narrow consumer guard also rejects substitution by another join.
        with mock.patch.object(terminal.source_unit_checker, "validated_reviewed_rows", return_value=false_markers):
            with self.assertRaisesRegex(ValueError, "must use its live version-4 provenance"):
                terminal.validate_corrected_source_rows(self.root, false_markers)
        candidates = copy.deepcopy(records)
        for candidate in candidates:
            candidate.update({
                "provenance_disposition": target.OPEN_DISPOSITION,
                "audit_result": target.PENDING_AUDIT_RESULT,
                "defect_exclusions": [],
                "completeness": {field: "pending" for field in target.COMPLETENESS_FIELDS},
                "verification": {field: "pending" for field in target.VERIFICATION_FIELDS},
                "verification_evidence": [],
            })
        pending_rows = self._apply_records(*candidates)
        terminal.validate_corrected_source_rows(self.root, pending_rows)
        self.assertFalse(any(target.is_terminal_source_unit(row) for row in pending_rows))
        for replacement_links in (False, True):
            forged = copy.deepcopy(admitted_rows)
            for row in forged:
                row["provenance_disposition"] = target.PASSING_DISPOSITION
                row["audit_result"] = "full-and-accurate"
                if replacement_links:
                    row["restoration_provenance_id"] = "SRC-99990-99999"
                    row["restoration_record_path"] = "spec/provenance/SRC-99990-99999.json"
                    row["handbook_destination"] = self.destination_path
            with self.subTest(replacement_links=replacement_links), self.assertRaisesRegex(ValueError, "differs from validated admission"):
                terminal.validate_corrected_source_rows(self.root, forged)
        # An unreviewed corrected unit must remain representable as open.
        unreviewed_rows = self._apply_records()
        terminal.validate_corrected_source_rows(self.root, unreviewed_rows)
        forged_ordinal = copy.deepcopy(unreviewed_rows)
        forged_ordinal[0]["unit_ordinal"] = "99999"
        with self.assertRaisesRegex(ValueError, "live corrected unit 1 must occur exactly once"):
            terminal.validate_corrected_source_rows(self.root, forged_ordinal)
        with self.assertRaisesRegex(ValueError, "live corrected unit 1 must occur exactly once"):
            terminal.validate_corrected_source_rows(self.root, [*unreviewed_rows, unreviewed_rows[0]])

    def test_corrected_admission_requires_every_gate_and_evidence(self) -> None:
        records = self._corrected_records()
        for kind in target.VERIFICATION_FIELDS:
            for failure in ("missing", "fail", "pending", "missing evidence"):
                with self.subTest(kind=kind, failure=failure):
                    bad = copy.deepcopy(records[0])
                    if failure == "missing":
                        del bad["verification"][kind]
                    elif failure == "missing evidence":
                        bad["verification_evidence"] = [e for e in bad["verification_evidence"] if e["category"] != kind]
                    else:
                        bad["verification"][kind] = failure
                        for item in bad["verification_evidence"]:
                            if item["category"] == kind:
                                item["recorded_result"] = failure
                                if kind in target.AI_REVIEW_FIELDS:
                                    for field in target.AI_EVIDENCE_FIELDS - target.EVIDENCE_FIELDS:
                                        del item[field]
                    with self.assertRaises(ValueError):
                        self._apply_records(bad)
        for kind in target.AI_REVIEW_FIELDS:
            with self.subTest(missing_model_version=kind):
                bad = copy.deepcopy(records[0])
                del next(e for e in bad["verification_evidence"] if e["category"] == kind)["model_version"]
                with self.assertRaises(ValueError):
                    self._apply_records(bad)
        for field in target.COMPLETENESS_FIELDS:
            for failure in ("missing", "fail", "pending"):
                with self.subTest(completeness=field, failure=failure):
                    bad = copy.deepcopy(records[0])
                    if failure == "missing":
                        del bad["completeness"][field]
                    else:
                        bad["completeness"][field] = failure
                    with self.assertRaises(ValueError):
                        self._apply_records(bad)

    def test_corrected_admission_rejects_false_identity_disposition_and_stale_links(self) -> None:
        records = self._corrected_records()
        mutations = {
            "stale record": ("restoration_record_sha256", "0" * 64),
            "wrong record": ("restoration_provenance_id", "SRC-00020-00022"),
            "wrong unit": ("source_start", 11),
            "wrong identity": ("presentation_identity_value", "unchanged-source"),
            "wrong destination": ("handbook_destination", self.destination_path),
            "stale destination": ("handbook_destination_sha256", "0" * 64),
            "false transcription": ("provenance_disposition", target.PASSING_DISPOSITION),
            "malformed disposition": ("provenance_disposition", [target.CORRECTED_DISPOSITION]),
            "false exact result": ("audit_result", "full-and-accurate"),
            "malformed result": ("audit_result", [target.CORRECTED_AUDIT_RESULT]),
            "false alteration exclusion": ("defect_exclusions", list(target.DEFECT_EXCLUSIONS)),
        }
        for name, (field, value) in mutations.items():
            with self.subTest(name=name):
                bad = copy.deepcopy(records[0]); bad[field] = value
                with self.assertRaises(ValueError):
                    self._apply_records(bad)
        for kind in target.VERIFICATION_FIELDS:
            with self.subTest(stale_evidence=kind):
                bad = copy.deepcopy(records[0])
                next(e for e in bad["verification_evidence"] if e["category"] == kind)["correction_snapshot"]["handbook_destination_sha256"] = "0" * 64
                with self.assertRaisesRegex(ValueError, "correction snapshot"):
                    self._apply_records(bad)
        artifact = self.root / records[0]["handbook_destination"]
        artifact.write_bytes(artifact.read_bytes() + b"later edit\n")
        with self.assertRaisesRegex(ValueError, "inherited restoration validation failed"):
            self._apply_records(*records)

    def test_corrected_result_cannot_attach_to_legacy_provenance(self) -> None:
        record = self._record()
        record["provenance_disposition"] = target.CORRECTED_DISPOSITION
        record["audit_result"] = target.CORRECTED_AUDIT_RESULT
        with self.assertRaisesRegex(ValueError, "validated version-4"):
            self._apply_records(record)

    def test_corrected_candidate_cannot_enter_active_audit_or_terminal_csv(self) -> None:
        records = self._corrected_records()
        rows = self._apply_records(*records)
        candidate = copy.deepcopy(records[0])
        candidate.update({
            "provenance_disposition": target.OPEN_DISPOSITION,
            "audit_result": target.PENDING_AUDIT_RESULT,
            "defect_exclusions": [],
            "completeness": {field: "pending" for field in target.COMPLETENESS_FIELDS},
            "verification": {field: "pending" for field in target.VERIFICATION_FIELDS},
            "verification_evidence": [],
        })
        candidate_rows = self._apply_records(candidate)
        self.assertFalse(target.is_terminal_source_unit(candidate_rows[0]))
        with self.assertRaisesRegex(ValueError, "differs from validated admission"):
            terminal.validate_corrected_source_rows(self.root, rows)
        with mock.patch.object(sys, "argv", ["audit_tables.py", "--root", str(self.root)]), redirect_stderr(io.StringIO()):
            self.assertEqual(audit_tables.main(), 1)
        self.assertFalse((self.root / "handbook/generated/audit-p01.tex").exists())
        self._apply_records(records[0])
        with self.assertRaisesRegex(ValueError, "unit 2 still needs terminal admission"):
            target.require_corrected_reader_admissions(self.root, {self.restoration_provenance_id})
        self._apply_records(*records)
        with self.assertRaisesRegex(ValueError, "emitted correction labels"):
            target.require_corrected_reader_admissions(self.root, {self.restoration_provenance_id},
                                                      {self.restoration_provenance_id: {"def:unadmitted"}})
        with self.assertRaisesRegex(ValueError, "collected reader bytes"):
            target.require_corrected_reader_admissions(
                self.root, {self.restoration_provenance_id}, artifact_hashes={self.restoration_provenance_id: "0" * 64})
        self._write_bytes("handbook/main.tex", (
            "\\input{parts/p01}\n"
            f"\\input{{{records[0]['handbook_destination'].removeprefix('handbook/')}}}\n"
        ).encode())
        with self.assertRaisesRegex(ValueError, "reachable exactly once"):
            self._apply_records(*records)

    def test_typed_environment_label_is_active(self) -> None:
        result = self._apply_records(self._record(2))
        self.assertEqual(json.loads(result[1]["stable_labels"]), ["def:p01-unit-two"])

    def test_open_record_exposes_checked_fields_without_closing_unit(self) -> None:
        result = self._apply_records(self._open_record())
        row = result[0]
        self.assertEqual(row["provenance_disposition"], target.OPEN_DISPOSITION)
        self.assertEqual(row["handbook_destination_status"], "identified")
        self.assertEqual(row["restoration_provenance_id"], self.restoration_provenance_id)
        self.assertEqual(row["audit_result"], target.PENDING_AUDIT_RESULT)
        self.assertEqual(row["source_fidelity_ai_verification"], "pending")
        self.assertEqual(row["static_verification"], "pass")
        self.assertEqual(row["build_verification"], "pending")
        self.assertEqual(row["visual_verification"], "pending")
        self.assertEqual(row["adversarial_publication_ai_verification"], "pending")
        self.assertEqual(json.loads(row["stable_labels"]), [])
        self.assertTrue(
            all(row[f"{field}_completeness"] == "pending" for field in target.COMPLETENESS_FIELDS)
        )

    def test_empty_record_set_leaves_all_defaults_unchanged(self) -> None:
        self.assertEqual(self._apply_records(), self.rows)

    def test_empty_input_keeps_all_1055_live_units_open(self) -> None:
        empty_review = self.root / "empty-live-review.json"
        empty_review.write_text(
            json.dumps(
                {
                    "schema_version": target.REVIEW_SCHEMA_VERSION,
                    "authority_path": target.AUTHORITY_PATH,
                    "authority_sha256": target.AUTHORITY_SHA256,
                    "records": [],
                }
            )
            + "\n",
            encoding="utf-8",
        )
        projected, projected_hash = target.build_rows(
            target.DEFAULT_INVENTORY,
            target.DEFAULT_AUDIT_MAP,
            target.DEFAULT_SOURCE,
            empty_review,
            target.ROOT,
        )
        baseline, baseline_hash = target.build_rows(
            target.DEFAULT_INVENTORY,
            target.DEFAULT_AUDIT_MAP,
            target.DEFAULT_SOURCE,
            None,
            target.ROOT,
        )
        self.assertEqual(projected_hash, baseline_hash)
        self.assertEqual(projected, baseline)
        self.assertEqual(len(projected), 1055)
        self.assertTrue(
            all(
                row["provenance_disposition"] == "open/missing"
                and row["handbook_destination_status"] == "open/missing"
                for row in projected
            )
        )

    def test_build_rows_rejects_authority_drift_before_inventory_processing(self) -> None:
        source = self._write_bytes("source/drifted.tex", b"drifted authority\n")
        inventory = self._write_bytes("spec/empty-inventory.csv", b"ordinal\n")
        audit_map = self._write_bytes("spec/empty-audit-map.csv", b"stable_id\n")
        with self.assertRaisesRegex(ValueError, "exact frozen authority"):
            target.build_rows(inventory, audit_map, source, self.review_path, self.root)

    def test_duplicate_and_unknown_ordinals_are_rejected(self) -> None:
        record = self._record()
        with self.assertRaisesRegex(ValueError, "duplicate unit ordinal"):
            self._apply_records(record, copy.deepcopy(record))

        unknown = self._record()
        unknown["unit_ordinal"] = 999
        with self.assertRaisesRegex(ValueError, "unknown unit ordinal"):
            self._apply_records(unknown)

    def test_stale_unit_and_authority_identity_are_rejected(self) -> None:
        cases = (
            ("unit_kind", "theorem"),
            ("unit_title", "Stale title"),
            ("unit_source_label", "src:stale"),
            ("source_start", 11),
            ("source_end", 13),
            ("source_sha256", "0" * 64),
            ("authority_path", "source/other.tex"),
            ("authority_sha256", "0" * 64),
        )
        for field, value in cases:
            with self.subTest(field=field):
                record = self._record()
                record[field] = value
                with self.assertRaisesRegex(ValueError, "stale or mismatched"):
                    self._apply_records(record)

        document = self._document([self._record()])
        document["authority_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "authority SHA-256 drift"):
            self._apply_document(document)

        self._write_bytes(target.AUTHORITY_PATH, b"changed authority\n")
        with self.assertRaisesRegex(ValueError, "live authority hash mismatch"):
            self._apply_records(self._record())

    def test_restoration_record_fields_file_digest_and_id_are_required(self) -> None:
        record = self._record()
        del record["restoration_record_path"]
        with self.assertRaisesRegex(ValueError, "restoration_record_path"):
            self._apply_records(record)

        record = self._record()
        record["restoration_record_path"] = (
            "spec/provenance/SRC-99999-99999.json"
        )
        record["restoration_provenance_id"] = "SRC-99999-99999"
        with self.assertRaisesRegex(ValueError, "file does not exist"):
            self._apply_records(record)

        record = self._record()
        record["restoration_record_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "restoration record SHA-256 drift"):
            self._apply_records(record)

        record = self._record()
        record["restoration_provenance_id"] = "SRC-00020-00022"
        with self.assertRaisesRegex(ValueError, "does not match the record path"):
            self._apply_records(record)

        record_data = json.loads(
            (self.root / self.restoration_record_path).read_text(encoding="utf-8")
        )
        record_data["disposition"] = "full reconstruction"
        self._write_bytes(
            self.restoration_record_path,
            (json.dumps(record_data, indent=2) + "\n").encode(),
        )
        record = self._record()
        with self.assertRaisesRegex(ValueError, "disposition must be"):
            self._apply_records(record)

    def test_restoration_record_must_contain_the_reviewed_unit_and_range(self) -> None:
        other_id = "SRC-00020-00022"
        other_path = self._write_restoration_record(other_id, 20, 22, [2])
        record = self._record(1)
        record["restoration_record_path"] = other_path
        record["restoration_record_sha256"] = digest(
            (self.root / other_path).read_bytes()
        )
        record["restoration_provenance_id"] = other_id
        with self.assertRaisesRegex(ValueError, "does not contain reviewed unit ordinal 1"):
            self._apply_records(record)

    def test_governed_wrapper_must_be_recursively_reachable_exactly_once(self) -> None:
        main = self.root / "handbook/main.tex"
        main.write_text("No wrapper input.\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "reachable 0 times"):
            self._apply_records(self._record())

        self._write_bytes(
            "handbook/chapter.tex",
            (
                "\\input{restoration/scope-"
                f"{self.restoration_provenance_id}"
                "}\n"
            ).encode(),
        )
        main.write_text(
            "\\input{chapter}\n\\input{chapter}\n", encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "reachable 2 times"):
            self._apply_records(self._record())

    def test_frontmatter_is_an_accepted_substantive_destination(self) -> None:
        label = "sec:synthetic-frontmatter-unit"
        frontmatter = (
            f"\\section*{{Synthetic front matter}}\\label{{{label}}}\n"
            "\\input{restoration/scope-"
            f"{self.restoration_provenance_id}"
            "}\n"
        ).encode()
        self._write_bytes("handbook/frontmatter.tex", frontmatter)
        self._write_bytes("handbook/main.tex", b"\\input{frontmatter}\n")
        record = self._record(label=label)
        record["handbook_destination"] = "handbook/frontmatter.tex"
        record["handbook_destination_sha256"] = digest(frontmatter)
        result = self._apply_records(record)
        self.assertEqual(
            result[0]["handbook_destination"], "handbook/frontmatter.tex"
        )

    def test_integer_identity_fields_reject_boolean_and_float_aliases(self) -> None:
        document = self._document([self._record()])
        document["schema_version"] = True
        with self.assertRaisesRegex(ValueError, "schema_version"):
            self._apply_document(document)

        for field, value in (("source_start", 10.0), ("source_end", True)):
            with self.subTest(field=field, value=value):
                record = self._record()
                record[field] = value
                with self.assertRaisesRegex(ValueError, "expected integer"):
                    self._apply_records(record)

    def test_authority_edition_must_match_the_frozen_source(self) -> None:
        record = self._record()
        record["authority_edition_value"] = "Version 2.0"
        with self.assertRaisesRegex(ValueError, "exact frozen edition"):
            self._apply_records(record)

    def test_exact_document_record_and_json_shapes_are_required(self) -> None:
        document = self._document([self._record()])
        document["unexpected"] = True
        with self.assertRaisesRegex(ValueError, "unexpected"):
            self._apply_document(document)

        record = self._record()
        del record["audit_result"]
        with self.assertRaisesRegex(ValueError, "missing"):
            self._apply_records(record)

        raw = json.dumps(self._document([self._record()]))
        needle = f'"schema_version": {target.REVIEW_SCHEMA_VERSION},'
        raw = raw.replace(needle, f"{needle} {needle}", 1)
        self.review_path.write_text(raw, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "duplicate JSON field"):
            target.apply_reviewed_records(
                self.rows, self.review_path, self.authority_hash, self.root
            )

    def test_destination_existence_scope_hash_and_active_label_are_required(self) -> None:
        record = self._record()
        record["handbook_destination"] = "handbook/restoration/missing.tex"
        with self.assertRaisesRegex(ValueError, "file does not exist"):
            self._apply_records(record)

        record = self._record()
        record["handbook_destination"] = target.AUTHORITY_PATH
        with self.assertRaisesRegex(ValueError, "must start with"):
            self._apply_records(record)

        record = self._record()
        record["handbook_destination"] = "../outside.tex"
        with self.assertRaisesRegex(ValueError, "inside the repository"):
            self._apply_records(record)

        record = self._record()
        record["handbook_destination"] = "C:/outside.tex"
        with self.assertRaisesRegex(ValueError, "drive-qualified"):
            self._apply_records(record)

        record = self._record()
        record["handbook_destination_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "destination SHA-256 drift"):
            self._apply_records(record)

        record = self._record(label="def:p01-absent")
        with self.assertRaisesRegex(ValueError, "occurs 0 times"):
            self._apply_records(record)

        commented = self.destination_bytes + b"% \\label{def:p01-commented}\n"
        self._write_bytes(self.destination_path, commented)
        record = self._record(label="def:p01-commented")
        record["handbook_destination_sha256"] = digest(commented)
        with self.assertRaisesRegex(ValueError, "occurs 0 times"):
            self._apply_records(record)

        escaped = b"\\\\label{def:p01-escaped}\n"
        self._write_bytes(self.destination_path, escaped)
        record = self._record(label="def:p01-escaped")
        record["handbook_destination_sha256"] = digest(escaped)
        with self.assertRaisesRegex(ValueError, "occurs 0 times"):
            self._apply_records(record)

    def test_generated_registry_lookup_and_driver_destinations_are_rejected(self) -> None:
        cases = (
            "handbook/generated/unit.tex",
            "handbook/registry/unit.tex",
            "handbook/parts/p01/symbol-registry.tex",
            "handbook/parts/p14/master-tables.tex",
            "handbook/parts/p14/rule-sheets.tex",
            "handbook/main.tex",
            "handbook/parts/p01.tex",
            "handbook/annex/p01.tex",
            "handbook/parts/p01/not-tex.md",
        )
        content = b"\\label{def:p01-unit-one}\n"
        for path in cases:
            with self.subTest(path=path):
                destination_content = content
                if path == "handbook/main.tex":
                    destination_content = (self.root / path).read_bytes()
                else:
                    self._write_bytes(path, destination_content)
                record = self._record()
                record["handbook_destination"] = path
                record["handbook_destination_sha256"] = digest(
                    destination_content
                )
                with self.assertRaisesRegex(
                    ValueError,
                    "forbidden|must be a nested .tex content file|permitted only",
                ):
                    self._apply_records(record)

    def test_labels_follow_taxonomy_and_part_ownership(self) -> None:
        for label in (
            "unit:p01-one",
            "def:p01/unit",
            "def:p01:unit",
            "sheet:p01-unit",
            "rule:p01-unit",
            "def:p02-unit-one",
            "part:p01",
        ):
            with self.subTest(label=label):
                record = self._record(label=label)
                with self.assertRaisesRegex(
                    ValueError, "malformed|structural or lookup|part-owned"
                ):
                    self._apply_records(record)

        restoration = b"\\label{sec:preface}\n"
        record = self._record(label="sec:preface")
        self._point_record_at(
            record, "handbook/restoration/preface.tex", restoration, "sec:preface"
        )
        self.assertEqual(
            self._apply_records(record)[0]["handbook_destination"],
            "handbook/restoration/preface.tex",
        )

        annex = b"\\begin{annexitem}{annex:p01-proof-one}{thm:p01-one}{Proof}\n"
        record = self._record(label="annex:p01-proof-one")
        self._point_record_at(
            record,
            "handbook/annex/p01/proof.tex",
            annex,
            "annex:p01-proof-one",
        )
        self.assertEqual(
            json.loads(self._apply_records(record)[0]["stable_labels"]),
            ["annex:p01-proof-one"],
        )

        legacy_annex = b"\\label{annex:p1.1}\n"
        record = self._record(label="annex:p1.1")
        self._point_record_at(
            record,
            "handbook/annex/p01/legacy.tex",
            legacy_annex,
            "annex:p1.1",
        )
        with self.assertRaisesRegex(ValueError, "must begin p01-"):
            self._apply_records(record)

    def test_labels_must_be_unique_and_unshared(self) -> None:
        record = self._record()
        record["stable_labels"] = ["def:p01-unit-one", "def:p01-unit-one"]
        with self.assertRaisesRegex(ValueError, "duplicate label"):
            self._apply_records(record)

        with self.assertRaisesRegex(ValueError, "already closes unit"):
            self._apply_records(self._record(1), self._record(2, "def:p01-unit-one"))

    def test_legacy_supplied_objects_accept_only_open_or_full_transcription(self) -> None:
        self.assertEqual(
            self._apply_records(self._open_record())[0]["provenance_disposition"],
            target.OPEN_DISPOSITION,
        )
        for disposition in (
            "full-and-accurate",
            ["full transcription"],
        ):
            with self.subTest(disposition=disposition):
                record = self._record()
                record["provenance_disposition"] = disposition
                with self.assertRaisesRegex(ValueError, "expected one of"):
                    self._apply_records(record)

    def test_all_completeness_and_verification_fields_are_exact(self) -> None:
        record = self._record()
        del record["completeness"]["proofs"]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "completeness.*missing"):
            self._apply_records(record)

        record = self._record()
        record["completeness"]["syntax"] = "pass"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "completeness.*unexpected"):
            self._apply_records(record)

        record = self._record()
        del record["verification"]["adversarial_publication_ai"]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "verification.*missing"):
            self._apply_records(record)

    def test_audit_result_and_layout_changes_are_exact(self) -> None:
        record = self._record()
        record["audit_result"] = "verified"
        with self.assertRaisesRegex(ValueError, "audit_result"):
            self._apply_records(record)

        record = self._record()
        record["layout_changes"] = ["typography"]
        with self.assertRaisesRegex(ValueError, "requires an empty list"):
            self._apply_records(record)

        record = self._record()
        record["audit_result"] = "layout-only relocation"
        with self.assertRaisesRegex(ValueError, "requires at least one"):
            self._apply_records(record)

        record = self._record()
        record["audit_result"] = "layout-only relocation"
        record["layout_changes"] = ["typography", "typography"]
        with self.assertRaisesRegex(ValueError, "duplicate value"):
            self._apply_records(record)

        record = self._record()
        record["audit_result"] = "layout-only relocation"
        record["layout_changes"] = ["content rewrite"]
        with self.assertRaisesRegex(ValueError, "expected only"):
            self._apply_records(record)

        record = self._record()
        record["audit_result"] = "layout-only relocation"
        record["layout_changes"] = ["typography"]
        self.assertEqual(
            self._apply_records(record)[0]["provenance_disposition"],
            "full transcription",
        )

    def test_every_contract_defect_must_be_excluded_in_exact_order(self) -> None:
        record = self._record()
        record["defect_exclusions"] = list(reversed(target.DEFECT_EXCLUSIONS))
        with self.assertRaisesRegex(ValueError, "exact ordered list"):
            self._apply_records(record)

        record = self._record()
        record["defect_exclusions"] = list(target.DEFECT_EXCLUSIONS[:-1])
        with self.assertRaisesRegex(ValueError, "exact ordered list"):
            self._apply_records(record)

    def test_passing_audit_rejects_pending_or_failing_dimensions(self) -> None:
        record = self._record()
        record["completeness"]["examples"] = "pending"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "requires all completeness"):
            self._apply_records(record)

        open_record = self._open_record()
        self.assertEqual(
            self._apply_records(open_record)[0]["provenance_disposition"],
            target.OPEN_DISPOSITION,
        )

        for audit_result, layout_changes in (
            ("full-and-accurate", []),
            ("layout-only relocation", ["wrapper"]),
        ):
            with self.subTest(audit_result=audit_result):
                open_record = self._open_record()
                open_record["audit_result"] = audit_result
                open_record["layout_changes"] = layout_changes
                open_record["defect_exclusions"] = list(target.DEFECT_EXCLUSIONS)
                with self.assertRaisesRegex(
                    ValueError, "passing audit result requires all completeness"
                ):
                    self._apply_records(open_record)

        record = self._record()
        record["verification"]["visual"] = "fail"  # type: ignore[index]
        for item in record["verification_evidence"]:  # type: ignore[assignment]
            if item["category"] == "visual":
                item["recorded_result"] = "fail"
        with self.assertRaisesRegex(ValueError, "requires all completeness"):
            self._apply_records(record)

    def test_pending_audit_result_is_restricted_to_open_records(self) -> None:
        record = self._record()
        record["audit_result"] = target.PENDING_AUDIT_RESULT
        record["layout_changes"] = []
        record["defect_exclusions"] = []
        with self.assertRaisesRegex(ValueError, "permitted only for an open/missing"):
            self._apply_records(record)

    def test_evidence_categories_files_results_and_hashes_are_exact(self) -> None:
        record = self._record()
        record["verification_evidence"][1]["category"] = (  # type: ignore[index]
            "source_fidelity_ai"
        )
        with self.assertRaisesRegex(ValueError, "duplicate evidence category"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["recorded_result"] = "fail"  # type: ignore[index]
        for field in target.AI_EVIDENCE_FIELDS - target.EVIDENCE_FIELDS:
            del record["verification_evidence"][0][field]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "does not match"):
            self._apply_records(record)

        record = self._record()
        del record["verification_evidence"][0]["model"]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "missing.*model"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0][  # type: ignore[index]
            "other_review_outputs_consulted"
        ] = True
        with self.assertRaisesRegex(ValueError, "must record false"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["consulted_authorities"][0][  # type: ignore[index]
            "sha256"
        ] = "0" * 64
        with self.assertRaisesRegex(ValueError, "authority SHA-256 drift"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][1]["artifact_path"] = (  # type: ignore[index]
            record["verification_evidence"][0]["artifact_path"]  # type: ignore[index]
        )
        record["verification_evidence"][1]["sha256"] = (  # type: ignore[index]
            record["verification_evidence"][0]["sha256"]  # type: ignore[index]
        )
        with self.assertRaisesRegex(ValueError, "separate evidence files"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["artifact_path"] = (  # type: ignore[index]
            "spec/evidence/missing.txt"
        )
        with self.assertRaisesRegex(ValueError, "file does not exist"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["sha256"] = "0" * 64  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "evidence SHA-256 drift"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["independently_produced"] = True  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "unexpected"):
            self._apply_records(record)

    def test_producer_identity_strings_must_be_distinct_after_normalization(self) -> None:
        for first, second in (
            ("Reviewer K", "reviewer k"),
            ("Producer \N{KELVIN SIGN}", "producer k"),
            ("Producer  K", "producer k"),
        ):
            with self.subTest(first=first, second=second):
                record = self._record()
                record["verification_evidence"][0][  # type: ignore[index]
                    "producer_identity"
                ] = first
                record["verification_evidence"][1][  # type: ignore[index]
                    "producer_identity"
                ] = second
                with self.assertRaisesRegex(ValueError, "distinct recorded producer"):
                    self._apply_records(record)

    def test_authority_destination_and_input_cannot_be_their_own_evidence(self) -> None:
        cases = (
            target.AUTHORITY_PATH,
            self.destination_path,
            "spec/provenance/reviewed.json",
        )
        for artifact_path in cases:
            with self.subTest(artifact_path=artifact_path):
                record = self._record()
                record["verification_evidence"][0][  # type: ignore[index]
                    "artifact_path"
                ] = artifact_path
                record["verification_evidence"][0]["sha256"] = "0" * 64  # type: ignore[index]
                with self.assertRaisesRegex(ValueError, "own evidence artifact"):
                    self._apply_records(record)

    def test_reciprocal_separately_recorded_variant_links_are_accepted(self) -> None:
        first, second = self._linked_records()
        result = self._apply_records(first, second)
        self.assertEqual(
            [row["provenance_disposition"] for row in result],
            ["full transcription", "full transcription"],
        )

    def test_variant_links_reject_self_duplicate_unknown_and_stale_targets(self) -> None:
        record = self._record()
        record["variant_links"] = [self._variant_link(1)]
        with self.assertRaisesRegex(ValueError, "cannot link itself"):
            self._apply_records(record)

        record = self._record()
        link = self._variant_link(2)
        record["variant_links"] = [link, copy.deepcopy(link)]
        with self.assertRaisesRegex(ValueError, "duplicate variant unit ordinal"):
            self._apply_records(record)

        record = self._record()
        link = self._variant_link(2)
        link["unit_ordinal"] = 999
        record["variant_links"] = [link]
        with self.assertRaisesRegex(ValueError, "unknown variant unit ordinal"):
            self._apply_records(record)

        record = self._record()
        link = self._variant_link(2)
        link["source_sha256"] = "0" * 64
        record["variant_links"] = [link]
        with self.assertRaisesRegex(ValueError, "stale or mismatched variant"):
            self._apply_records(record)

    def test_variant_links_require_recorded_reciprocity_and_distinct_presentations(self) -> None:
        first = self._record(1)
        first["variant_links"] = [self._variant_link(2)]
        with self.assertRaisesRegex(ValueError, "not separately recorded"):
            self._apply_records(first)

        first, second = self._linked_records()
        second["variant_links"] = []
        with self.assertRaisesRegex(ValueError, "reciprocal link"):
            self._apply_records(first, second)

        first, second = self._linked_records()
        second["presentation_identity_value"] = first["presentation_identity_value"]
        with self.assertRaisesRegex(ValueError, "different presentation identity"):
            self._apply_records(first, second)

    def test_committed_schema_and_input_use_current_interface(self) -> None:
        schema = json.loads(
            (target.ROOT / "spec/provenance/reviewed-source-unit-records.schema.json")
            .read_text(encoding="utf-8")
        )
        document = json.loads(target.DEFAULT_REVIEWED_RECORDS.read_text(encoding="utf-8"))
        self.assertEqual(
            schema["properties"]["schema_version"]["const"],
            target.REVIEW_SCHEMA_VERSION,
        )
        self.assertEqual(document["schema_version"], target.REVIEW_SCHEMA_VERSION)
        shard_paths = sorted(
            (
                target.ROOT
                / "spec/provenance/reviewed-source-unit-shards"
            ).glob("*.json")
        )
        self.assertTrue(shard_paths, "at least one governed review shard is required")
        document_pins = {
            field: value for field, value in document.items() if field != "records"
        }
        shard_records: list[dict[str, object]] = []
        for shard_path in shard_paths:
            shard = json.loads(shard_path.read_text(encoding="utf-8"))
            self.assertEqual(set(shard), set(document))
            self.assertEqual(
                {
                    field: value
                    for field, value in shard.items()
                    if field != "records"
                },
                document_pins,
            )
            shard_records.extend(shard["records"])

        shard_ordinals = [record["unit_ordinal"] for record in shard_records]
        self.assertEqual(len(shard_ordinals), len(set(shard_ordinals)))
        expected_records = sorted(
            shard_records, key=lambda record: record["unit_ordinal"]
        )
        self.assertEqual(document["records"], expected_records)
        self.assertEqual(len(document["records"]), len(shard_records))
        self.assertTrue(
            all(
                record["provenance_disposition"] == target.OPEN_DISPOSITION
                for record in document["records"]
            )
        )
        self.assertTrue(
            all(
                record["audit_result"] == target.PENDING_AUDIT_RESULT
                for record in document["records"]
            )
        )
        self.assertEqual(
            set(schema["$defs"]["record"]["required"]),
            target.REVIEW_RECORD_FIELDS,
        )
        self.assertEqual(
            set(schema["$defs"]["record"]["properties"]),
            target.REVIEW_RECORD_FIELDS,
        )
        self.assertEqual(
            set(schema["$defs"]["evidence"]["required"]),
            target.EVIDENCE_FIELDS,
        )
        self.assertEqual(
            set(schema["$defs"]["evidence"]["properties"]),
            target.AI_EVIDENCE_FIELDS | {"correction_snapshot"},
        )
        self.assertEqual(
            set(schema["$defs"]["variantLink"]["required"]),
            target.VARIANT_LINK_FIELDS,
        )
        self.assertEqual(
            set(schema["$defs"]["variantLink"]["properties"]),
            target.VARIANT_LINK_FIELDS,
        )

    def test_committed_records_cover_restored_unit_evidence_without_phantom_row(
        self,
    ) -> None:
        document = json.loads(target.DEFAULT_REVIEWED_RECORDS.read_text(encoding="utf-8"))
        records = document["records"]
        restoration_paths = sorted(
            (target.ROOT / "spec/provenance").glob("SRC-*.json")
        )
        self.assertTrue(
            restoration_paths, "at least one governed restoration record is required"
        )
        expected_links: set[tuple[int, str, str, str]] = set()
        unitless_fragments: list[str] = []
        for restoration_path in restoration_paths:
            restoration = json.loads(restoration_path.read_text(encoding="utf-8"))
            provenance_id = restoration["provenance_id"]
            self.assertEqual(restoration_path.name, f"{provenance_id}.json")
            ordinal_list = restoration["source_unit_evidence"]["unit_ordinals"]
            self.assertEqual(ordinal_list, sorted(set(ordinal_list)))
            ordinals = set(ordinal_list)
            linked = {
                record["unit_ordinal"]
                for record in records
                if record["restoration_provenance_id"] == provenance_id
            }
            self.assertEqual(linked, ordinals)
            if ordinals:
                record_path = restoration_path.relative_to(target.ROOT).as_posix()
                record_sha256 = digest(restoration_path.read_bytes())
                for ordinal in ordinals:
                    link = (ordinal, provenance_id, record_path, record_sha256)
                    self.assertNotIn(link, expected_links)
                    expected_links.add(link)
            else:
                unitless_fragments.append(provenance_id)

        self.assertEqual(
            unitless_fragments,
            [
                "SRC-00171-00197",
                "SRC-11012-11052",
                "SRC-11240-11279",
                "SRC-11520-11598",
                "SRC-13255-13284",
                "SRC-13410-13439",
                "SRC-13862-13896",
                "SRC-13897-13918",
                "SRC-14035-14051",
            ],
        )
        self.assertFalse(
            any(
                record["restoration_provenance_id"] in unitless_fragments
                for record in records
            ),
            "a unitless restoration must not create a phantom source-unit row",
        )
        actual_links = {
            (
                record["unit_ordinal"],
                record["restoration_provenance_id"],
                record["restoration_record_path"],
                record["restoration_record_sha256"],
            )
            for record in records
        }
        self.assertEqual(actual_links, expected_links)
        self.assertEqual(len(actual_links), len(records))
        self.assertEqual(
            len({record["unit_ordinal"] for record in records}), len(records)
        )
        self.assertTrue(
            all(record["provenance_disposition"] == target.OPEN_DISPOSITION for record in records)
        )


if __name__ == "__main__":
    unittest.main()
