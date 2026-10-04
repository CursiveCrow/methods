from __future__ import annotations

import copy
import csv
import hashlib
import importlib.util
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("build_acquisition_gap_resolution.py")
SPEC = importlib.util.spec_from_file_location(
    "build_acquisition_gap_resolution", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
target = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(target)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_digest(value: object) -> str:
    return digest(
        json.dumps(
            value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
    )


class AcquisitionGapResolutionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(
            prefix="acquisition-gap-resolution-"
        )
        self.root = Path(self.temporary.name)
        self.gap_id = "ACQ-GAP-001"
        self.control_id = "ACQ-CONTROL-001"
        self.source_path = "spec/research/baseline.md"
        self.source_line = 7
        self.source_bytes = (
            "heading\n\ncontext\n\nmore\n\n"
            "- `ACQ-GAP-001` (`open`): Missing exact source.\n"
            "- `ACQ-CONTROL-001` (`active`): Keep authorities separate.\n"
        ).encode("utf-8")
        self._write(self.source_path, self.source_bytes)
        self.source_sha256 = digest(self.source_bytes)
        self.gap_description = "Missing exact source."
        self.manifest_rows = [
            {
                "acquisition_id": self.gap_id,
                "record_type": "gap",
                "status": "open",
                "source_file": self.source_path,
                "source_line": str(self.source_line),
                "source_sha256": self.source_sha256,
                "description": self.gap_description,
            },
            {
                "acquisition_id": self.control_id,
                "record_type": "provenance_control",
                "status": "active",
                "source_file": self.source_path,
                "source_line": "8",
                "source_sha256": self.source_sha256,
                "description": "Keep authorities separate.",
            },
        ]
        manifest_output = io.StringIO(newline="")
        writer = csv.DictWriter(
            manifest_output,
            fieldnames=target.MANIFEST_FIELDS,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(self.manifest_rows)
        self.manifest_bytes = manifest_output.getvalue().encode("utf-8")
        self.manifest_path = self._write(target.MANIFEST_PATH, self.manifest_bytes)
        self.manifest_sha256 = digest(self.manifest_bytes)
        self.gap_record_sha256 = canonical_digest(self.manifest_rows[0])
        self.reviewed_path = self.root / target.REVIEWED_PATH

        self.destination_path = "handbook/parts/p01/acquisition-resolution.tex"
        self.destination_bytes = (
            b"\\begin{hbdefinition}\n"
            b"\\label{def:p01-acquisition-resolution}\n"
            b"Exact acquired content.\n"
            b"\\end{hbdefinition}\n"
        )
        self._write(self.destination_path, self.destination_bytes)
        self.content_links = [
            {
                "path": self.destination_path,
                "sha256": digest(self.destination_bytes),
                "start_line": 1,
                "end_line": 4,
                "content_sha256": digest(self.destination_bytes),
                "labels": ["def:p01-acquisition-resolution"],
            }
        ]
        self.content_links_digest = canonical_digest(self.content_links)
        self.exact_scope = {
            "acquisition_id": self.gap_id,
            "gap_record_sha256": self.gap_record_sha256,
            "content_links_digest": self.content_links_digest,
        }
        manifest_row_bytes = self.manifest_bytes.splitlines(keepends=True)[1]
        source_row_bytes = self.source_bytes.splitlines(keepends=True)[6]
        self.authority_files = sorted(
            [
                {"path": target.MANIFEST_PATH, "sha256": self.manifest_sha256},
                {"path": self.source_path, "sha256": self.source_sha256},
                {
                    "path": self.destination_path,
                    "sha256": digest(self.destination_bytes),
                },
            ],
            key=lambda item: item["path"],
        )
        self.authority_locators = sorted(
            [
                {
                    "path": target.MANIFEST_PATH,
                    "start_line": 2,
                    "end_line": 2,
                    "content_sha256": digest(manifest_row_bytes),
                },
                {
                    "path": self.source_path,
                    "start_line": self.source_line,
                    "end_line": self.source_line,
                    "content_sha256": digest(source_row_bytes),
                },
                {
                    "path": self.destination_path,
                    "start_line": 1,
                    "end_line": 4,
                    "content_sha256": digest(self.destination_bytes),
                },
            ],
            key=lambda item: (item["path"], item["start_line"], item["end_line"]),
        )
        self.evidence: list[dict[str, object]] = []
        for index, category in enumerate(target.VERIFICATION_FIELDS):
            evidence_path = f"spec/evidence/{self.gap_id.lower()}-{category}.txt"
            evidence_bytes = (
                f"Independent {category} evidence for {self.gap_id}; fixture {index}.\n"
            ).encode("utf-8")
            self._write(evidence_path, evidence_bytes)
            item: dict[str, object] = {
                "category": category,
                "recorded_result": "pass",
                "artifact_path": evidence_path,
                "sha256": digest(evidence_bytes),
                "producer_identity": f"Reviewer {index}",
                "exact_scope": copy.deepcopy(self.exact_scope),
            }
            if category in target.AI_VERIFICATION_FIELDS:
                item.update(
                    {
                        "model": "self-test-model",
                        "model_version": f"self-test-version-{index}",
                        "instructions": "Check the exact gap and linked content against every pinned authority locator.",
                        "consulted_authority_files": copy.deepcopy(
                            self.authority_files
                        ),
                        "consulted_authority_locators": copy.deepcopy(
                            self.authority_locators
                        ),
                        "findings": [f"The {category} fixture passes."],
                        "evidence_digest": digest(evidence_bytes),
                    }
                )
            self.evidence.append(item)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _write(self, relative: str, data: bytes) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def _document(self, records: list[dict[str, object]]) -> dict[str, object]:
        return {
            "schema_version": target.SCHEMA_VERSION,
            "acquisition_gap_manifest_path": target.MANIFEST_PATH,
            "acquisition_gap_manifest_sha256": self.manifest_sha256,
            "nonterminal_reports": [],
            "nonterminal_evidence": [],
            "records": records,
        }

    def _record(self) -> dict[str, object]:
        return {
            "acquisition_id": self.gap_id,
            "record_type": "gap",
            "manifest_status": "open",
            "source_file": self.source_path,
            "source_line": self.source_line,
            "source_sha256": self.source_sha256,
            "gap_description": self.gap_description,
            "gap_record_sha256": self.gap_record_sha256,
            "resolution_status": "resolved",
            "content_links": copy.deepcopy(self.content_links),
            "destination_labels": ["def:p01-acquisition-resolution"],
            "resolution_description": "The exact acquired source and content now discharge this gap.",
            "verification": {key: "pass" for key in target.VERIFICATION_FIELDS},
            "verification_evidence": copy.deepcopy(self.evidence),
        }

    def _apply_document(self, document: dict[str, object]) -> list[dict[str, str]]:
        self.reviewed_path.parent.mkdir(parents=True, exist_ok=True)
        self.reviewed_path.write_text(
            json.dumps(document, indent=2) + "\n", encoding="utf-8"
        )
        rows = target.load_manifest(
            self.manifest_path,
            self.root,
            expected_gap_ids=(self.gap_id,),
            expected_manifest_sha256=self.manifest_sha256,
        )
        return target.apply_reviewed_records(
            rows, self.reviewed_path, self.manifest_path, self.root
        )

    def _apply_records(self, *records: dict[str, object]) -> list[dict[str, str]]:
        return self._apply_document(self._document(list(records)))

    def test_empty_reviewed_input_projects_every_true_gap_as_open(self) -> None:
        first = self._apply_records()
        second = self._apply_records()
        self.assertEqual(first, second)
        self.assertEqual([row["acquisition_id"] for row in first], [self.gap_id])
        self.assertEqual(first[0]["resolution_status"], "OPEN")
        self.assertEqual(first[0]["content_links"], "[]")
        self.assertEqual(first[0]["destination_labels"], "[]")
        self.assertEqual(first[0]["visual_verification"], "pending")

    def test_valid_terminal_resolution_is_resolved_and_deterministic(self) -> None:
        first = self._apply_records(self._record())
        second = self._apply_records(self._record())
        self.assertEqual(first, second)
        self.assertEqual(first[0]["resolution_status"], "RESOLVED")
        self.assertEqual(first[0]["gap_record_sha256"], self.gap_record_sha256)
        self.assertEqual(
            json.loads(first[0]["destination_labels"]),
            ["def:p01-acquisition-resolution"],
        )
        self.assertEqual(first[0]["source_fidelity_ai_verification"], "pass")
        self.assertEqual(first[0]["visual_verification"], "pass")

    def test_unknown_duplicate_control_and_stale_identities_fail_closed(self) -> None:
        duplicate = self._record()
        with self.assertRaisesRegex(ValueError, "duplicate acquisition ID"):
            self._apply_records(duplicate, copy.deepcopy(duplicate))

        unknown = self._record()
        unknown["acquisition_id"] = "ACQ-GAP-999"
        with self.assertRaisesRegex(ValueError, "unknown acquisition gap"):
            self._apply_records(unknown)

        control = self._record()
        control["acquisition_id"] = self.control_id
        with self.assertRaisesRegex(ValueError, "not a resolvable gap"):
            self._apply_records(control)

        for field, value in (
            ("record_type", "provenance_control"),
            ("manifest_status", "active"),
            ("source_file", "spec/research/other.md"),
            ("source_line", self.source_line + 1),
            ("source_sha256", "0" * 64),
            ("gap_description", "Different gap."),
            ("gap_record_sha256", "0" * 64),
        ):
            with self.subTest(field=field):
                stale = self._record()
                stale[field] = value
                with self.assertRaisesRegex(ValueError, "stale or mismatched"):
                    self._apply_records(stale)

        wrong_type = self._record()
        wrong_type["source_line"] = True
        with self.assertRaisesRegex(ValueError, "expected integer"):
            self._apply_records(wrong_type)

    def test_exact_document_record_and_json_shapes_are_required(self) -> None:
        document = self._document([])
        document["extra"] = True
        with self.assertRaisesRegex(ValueError, "unexpected"):
            self._apply_document(document)

        record = self._record()
        del record["resolution_description"]
        with self.assertRaisesRegex(ValueError, "missing"):
            self._apply_records(record)

        record = self._record()
        record["extra"] = True
        with self.assertRaisesRegex(ValueError, "unexpected"):
            self._apply_records(record)

        raw = json.dumps(self._document([]))
        marker = f'"schema_version": {target.SCHEMA_VERSION},'
        raw = raw.replace(marker, f"{marker} {marker}")
        self.reviewed_path.write_text(raw, encoding="utf-8")
        rows = target.load_manifest(
            self.manifest_path,
            self.root,
            expected_gap_ids=(self.gap_id,),
            expected_manifest_sha256=self.manifest_sha256,
        )
        with self.assertRaisesRegex(ValueError, "duplicate JSON field"):
            target.apply_reviewed_records(
                rows, self.reviewed_path, self.manifest_path, self.root
            )

    def test_manifest_hash_identity_and_kind_status_are_fail_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "manifest SHA-256 drift"):
            target.load_manifest(
                self.manifest_path,
                self.root,
                expected_gap_ids=(self.gap_id,),
                expected_manifest_sha256="0" * 64,
            )

        duplicate_rows = self.manifest_rows + [copy.deepcopy(self.manifest_rows[0])]
        output = io.StringIO(newline="")
        writer = csv.DictWriter(
            output, fieldnames=target.MANIFEST_FIELDS, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(duplicate_rows)
        duplicate_bytes = output.getvalue().encode("utf-8")
        self.manifest_path.write_bytes(duplicate_bytes)
        with self.assertRaisesRegex(ValueError, "duplicate acquisition ID"):
            target.load_manifest(
                self.manifest_path,
                self.root,
                expected_gap_ids=(self.gap_id, self.gap_id),
                expected_manifest_sha256=digest(duplicate_bytes),
            )

        bad_rows = copy.deepcopy(self.manifest_rows)
        bad_rows[0]["status"] = "active"
        output = io.StringIO(newline="")
        writer = csv.DictWriter(
            output, fieldnames=target.MANIFEST_FIELDS, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(bad_rows)
        bad_bytes = output.getvalue().encode("utf-8")
        self.manifest_path.write_bytes(bad_bytes)
        with self.assertRaisesRegex(ValueError, "kind/status mismatch"):
            target.load_manifest(
                self.manifest_path,
                self.root,
                expected_gap_ids=(self.gap_id,),
                expected_manifest_sha256=digest(bad_bytes),
            )

    def test_source_and_destination_bytes_ranges_and_labels_are_exact(self) -> None:
        self._write(self.source_path, self.source_bytes + b"drift\n")
        with self.assertRaisesRegex(ValueError, "live gap source drift"):
            self._apply_records(self._record())
        self._write(self.source_path, self.source_bytes)

        record = self._record()
        record["content_links"] = []
        with self.assertRaisesRegex(ValueError, "at least one exact content link"):
            self._apply_records(record)

        record = self._record()
        record["content_links"][0]["path"] = "../outside.tex"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "inside the repository"):
            self._apply_records(record)

        record = self._record()
        record["content_links"][0]["sha256"] = "0" * 64  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "destination file SHA-256 drift"):
            self._apply_records(record)

        record = self._record()
        record["content_links"][0]["content_sha256"] = "0" * 64  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "linked content drift"):
            self._apply_records(record)

        record = self._record()
        record["content_links"][0]["labels"] = []  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "exactly equal labels"):
            self._apply_records(record)

        record = self._record()
        record["destination_labels"] = []
        with self.assertRaisesRegex(ValueError, "exactly equal linked destination labels"):
            self._apply_records(record)

        self._write(
            "handbook/parts/p02/duplicate.tex",
            b"\\label{def:p01-acquisition-resolution}\n",
        )
        with self.assertRaisesRegex(ValueError, "occurs 2 times"):
            self._apply_records(self._record())

    def test_path_symlinks_are_rejected_when_the_platform_allows_them(self) -> None:
        target_path = self.root / self.destination_path
        link_path = self.root / "handbook/parts/p01/symlink.tex"
        try:
            os.symlink(target_path, link_path)
        except OSError as error:
            self.skipTest(f"symlink creation unavailable: {error}")
        record = self._record()
        record["content_links"][0]["path"] = (  # type: ignore[index]
            "handbook/parts/p01/symlink.tex"
        )
        with self.assertRaisesRegex(ValueError, "symbolic-link or junction"):
            self._apply_records(record)

    def test_terminal_status_and_all_six_verification_gates_are_required(self) -> None:
        record = self._record()
        record["resolution_status"] = "RESOLVED"
        with self.assertRaisesRegex(ValueError, "terminal record must be 'resolved'"):
            self._apply_records(record)

        record = self._record()
        record["verification"]["visual"] = "pending"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "resolution requires pass"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"] = record["verification_evidence"][:-1]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "exactly six"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][1]["category"] = "source_fidelity_ai"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "duplicate evidence category"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][3]["category"] = "unknown"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "unknown category"):
            self._apply_records(record)

        record = self._record()
        evidence = record["verification_evidence"]  # type: ignore[assignment]
        evidence[3], evidence[4] = evidence[4], evidence[3]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "canonical order"):
            self._apply_records(record)

    def test_evidence_paths_hashes_producers_scope_and_reuse_fail_closed(self) -> None:
        record = self._record()
        record["verification_evidence"][0]["artifact_path"] = "../outside.txt"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "inside the repository"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["sha256"] = "0" * 64  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "evidence SHA-256 drift"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][1]["artifact_path"] = record["verification_evidence"][0]["artifact_path"]  # type: ignore[index]
        record["verification_evidence"][1]["sha256"] = record["verification_evidence"][0]["sha256"]  # type: ignore[index]
        record["verification_evidence"][1]["evidence_digest"] = record["verification_evidence"][0]["sha256"]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "separate evidence files"):
            self._apply_records(record)

        record = self._record()
        first_path = record["verification_evidence"][0]["artifact_path"]  # type: ignore[index]
        copied_bytes = (self.root / first_path).read_bytes()
        copied_path = "spec/evidence/copied-identical.txt"
        self._write(copied_path, copied_bytes)
        record["verification_evidence"][1]["artifact_path"] = copied_path  # type: ignore[index]
        record["verification_evidence"][1]["sha256"] = digest(copied_bytes)  # type: ignore[index]
        record["verification_evidence"][1]["evidence_digest"] = digest(copied_bytes)  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "reuse identical artifact bytes"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][1]["producer_identity"] = " reviewer 0 "  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "whitespace|distinct recorded producer"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["exact_scope"]["gap_record_sha256"] = "0" * 64  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "stale or mismatched exact resolution scope"):
            self._apply_records(record)

        for path in (
            target.MANIFEST_PATH,
            self.source_path,
            self.destination_path,
            target.REVIEWED_PATH,
        ):
            with self.subTest(self_evidence=path):
                record = self._record()
                record["verification_evidence"][0]["artifact_path"] = path  # type: ignore[index]
                if (self.root / path).is_file():
                    record["verification_evidence"][0]["sha256"] = digest(  # type: ignore[index]
                        (self.root / path).read_bytes()
                    )
                with self.assertRaisesRegex(ValueError, "cannot be its own evidence"):
                    self._apply_records(record)

        copied_destination = "spec/evidence/copied-destination-bytes.txt"
        self._write(copied_destination, self.destination_bytes)
        record = self._record()
        record["verification_evidence"][0]["artifact_path"] = copied_destination  # type: ignore[index]
        record["verification_evidence"][0]["sha256"] = digest(self.destination_bytes)  # type: ignore[index]
        record["verification_evidence"][0]["evidence_digest"] = digest(self.destination_bytes)  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "self-evidence bytes"):
            self._apply_records(record)

    def test_ai_evidence_metadata_authorities_locators_and_digest_are_exact(self) -> None:
        record = self._record()
        del record["verification_evidence"][0]["model"]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "missing"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["consulted_authority_files"][0]["sha256"] = "0" * 64  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "authority file digest drift"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["consulted_authority_files"] = record["verification_evidence"][0]["consulted_authority_files"][1:]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "missing exact required authority"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["consulted_authority_locators"] = record["verification_evidence"][0]["consulted_authority_locators"][1:]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "missing exact required authority locator"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["consulted_authority_locators"][0]["content_sha256"] = "0" * 64  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "authority locator drift"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["findings"] = []  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "at least one value"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["evidence_digest"] = "0" * 64  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "must equal the live review evidence"):
            self._apply_records(record)

    def test_not_clean_sweep_report_is_pinned_without_closing_a_gap(self) -> None:
        report_path = "spec/research/acquisition-completion-sweep-test.md"
        report_bytes = (
            b"# Independent acquisition-completion sweep test\n\n"
            b"Sweep result: NOT CLEAN; ACQ-GAP-001 remains OPEN.\n"
            b"Rights-holder contacts: 0. External messages sent: 0.\n"
            b"Subscription-only bodies retrieved: 0. "
            b"Inaccessible bodies credited as acquired: 0.\n"
        )
        self._write(report_path, report_bytes)
        report = {
            "path": report_path,
            "sha256": digest(report_bytes),
            "report_result": "not_clean",
            "gap_status_effect": "none",
            "applies_to_gap_ids": [self.gap_id],
            "rights_holder_contacts": 0,
            "external_messages_sent": 0,
            "subscription_only_bodies_retrieved": 0,
            "inaccessible_bodies_credited_as_acquired": 0,
        }
        document = self._document([])
        document["nonterminal_reports"] = [report]
        projected = self._apply_document(document)
        self.assertEqual(projected[0]["resolution_status"], "OPEN")
        self.assertEqual(
            json.loads(projected[0]["nonterminal_report_refs"]),
            [
                {
                    "path": report_path,
                    "sha256": digest(report_bytes),
                    "report_result": "not_clean",
                }
            ],
        )
        markdown = target.markdown_bytes(projected).decode("utf-8")
        self.assertIn(report_path, markdown)
        self.assertIn("rights-holder contacts", markdown)
        self.assertIn("inaccessible bodies", markdown)
        self.assertIn("cannot change OPEN to RESOLVED", markdown)

        document["records"] = [self._record()]
        with self.assertRaisesRegex(ValueError, "nonterminal NOT CLEAN report"):
            self._apply_document(document)

        for field, value, message in (
            ("sha256", "0" * 64, "report SHA-256 drift"),
            ("gap_status_effect", "resolve", "must be 'none'"),
            ("rights_holder_contacts", 1, "must be exactly 0"),
            (
                "inaccessible_bodies_credited_as_acquired",
                1,
                "must be exactly 0",
            ),
        ):
            with self.subTest(field=field):
                bad_report = copy.deepcopy(report)
                bad_report[field] = value
                bad_document = self._document([])
                bad_document["nonterminal_reports"] = [bad_report]
                with self.assertRaisesRegex(ValueError, message):
                    self._apply_document(bad_document)

    def test_planned_presentation_evidence_is_pinned_without_closing_the_gap(self) -> None:
        evidence_path = "spec/research/acquisition-gap-hlics-volume-6-2026-08-13.md"
        evidence_bytes = (target.ROOT / evidence_path).read_bytes()
        self._write(evidence_path, evidence_bytes)
        evidence = copy.deepcopy(
            target.PLANNED_PRESENTATION_EVIDENCE_PROFILES[evidence_path]
        )
        self.assertEqual(evidence["sha256"], digest(evidence_bytes))
        document = self._document([])
        document["nonterminal_evidence"] = [evidence]

        projected = self._apply_document(document)

        self.assertEqual(projected[0]["resolution_status"], "OPEN")
        self.assertEqual(
            json.loads(projected[0]["nonterminal_evidence_refs"]),
            [evidence],
        )
        markdown = target.markdown_bytes(projected).decode("utf-8")
        self.assertIn("Volume 6 Logical methods in computer science", markdown)
        self.assertIn("S. Abramsky; D. M. Gabbay; T. S. E. Maibaum", markdown)
        self.assertIn("chapter_presentation_only", markdown)
        self.assertIn("not_established", markdown)
        self.assertIn("not_acquired", markdown)

    def test_planned_presentation_claims_must_match_the_governed_profile(self) -> None:
        evidence_path = "spec/research/acquisition-gap-profile-test.md"
        evidence_bytes = (
            b"ACQ-GAP-001 remains OPEN; completion claim: none.\n"
            b"Volume 6 Logical methods in computer science. Categorical Logic.\n"
            b"S. Abramsky; D. M. Gabbay; T. S. E. Maibaum.\n"
            b"1995 planned Volume VI chapter presentation; "
            b"2001 published Volume 5 chapter presentation.\n"
            b"No published Volume 6 identity. No Volume 6 body. "
            b"No reproduction basis.\n"
        )
        self._write(evidence_path, evidence_bytes)
        evidence = {
            "evidence_type": "planned_presentation",
            "path": evidence_path,
            "sha256": digest(evidence_bytes),
            "gap_status_effect": "none",
            "applies_to_gap_ids": [self.gap_id],
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
        sentinel = object()
        saved = getattr(target, "PLANNED_PRESENTATION_EVIDENCE_PROFILES", sentinel)
        target.PLANNED_PRESENTATION_EVIDENCE_PROFILES = {
            evidence_path: copy.deepcopy(evidence)
        }
        try:
            document = self._document([])
            document["nonterminal_evidence"] = [copy.deepcopy(evidence)]
            self._apply_document(document)

            terminal_document = self._document([self._record()])
            terminal_document["nonterminal_evidence"] = [copy.deepcopy(evidence)]
            with self.assertRaisesRegex(ValueError, "nonterminal evidence keeps it OPEN"):
                self._apply_document(terminal_document)

            document["nonterminal_evidence"][0]["planned_volume_title"] = "Categorical Logic"  # type: ignore[index]
            with self.assertRaisesRegex(ValueError, "governed evidence profile"):
                self._apply_document(document)

            for field, value, message in (
                ("gap_status_effect", "resolve", "must be 'none'"),
                (
                    "published_volume_identity_status",
                    "established",
                    "must be 'not_established'",
                ),
                ("volume_body_status", "acquired", "must be 'not_acquired'"),
                ("rights_status", "established", "must be 'not_established'"),
            ):
                with self.subTest(field=field):
                    bad = copy.deepcopy(evidence)
                    bad[field] = value
                    bad_document = self._document([])
                    bad_document["nonterminal_evidence"] = [bad]
                    with self.assertRaisesRegex(ValueError, message):
                        self._apply_document(bad_document)

            collapsed = copy.deepcopy(evidence)
            collapsed["presentation_relation"]["superseding_presentation"] = collapsed["presentation_relation"]["planned_presentation"]  # type: ignore[index]
            collapsed_document = self._document([])
            collapsed_document["nonterminal_evidence"] = [collapsed]
            with self.assertRaisesRegex(ValueError, "must remain distinct"):
                self._apply_document(collapsed_document)
        finally:
            if saved is sentinel:
                delattr(target, "PLANNED_PRESENTATION_EVIDENCE_PROFILES")
            else:
                target.PLANNED_PRESENTATION_EVIDENCE_PROFILES = saved

    def test_generated_markdown_has_five_part_name_justification_and_boundaries(self) -> None:
        markdown = target.markdown_bytes(self._apply_records()).decode("utf-8")
        for heading in (
            "**Necessity:**",
            "**Definition:**",
            "**Standing:**",
            "**Nonredundancy:**",
            "**Use:**",
        ):
            self.assertIn(heading, markdown)
        self.assertIn("Provenance controls", markdown)
        self.assertIn("nonterminal", markdown)
        self.assertIn("OPEN", markdown)

    def test_schema_v2_declares_the_exact_planned_presentation_evidence_contract(self) -> None:
        schema = json.loads(
            (target.ROOT / target.SCHEMA_PATH).read_text(encoding="utf-8")
        )
        self.assertEqual(target.SCHEMA_VERSION, 2)
        self.assertEqual(schema["properties"]["schema_version"]["const"], 2)
        self.assertIn("nonterminal_evidence", schema["required"])
        evidence = schema["$defs"]["plannedPresentationEvidence"]
        self.assertEqual(
            set(evidence["required"]), target.NONTERMINAL_EVIDENCE_FIELDS
        )
        self.assertEqual(
            set(schema["$defs"]["presentationRelation"]["required"]),
            target.PRESENTATION_RELATION_FIELDS,
        )

    def test_main_write_and_check_are_end_to_end_and_fail_on_stale_output(self) -> None:
        self._apply_records()
        saved = {
            "ROOT": target.ROOT,
            "DEFAULT_MANIFEST": target.DEFAULT_MANIFEST,
            "DEFAULT_REVIEWED": target.DEFAULT_REVIEWED,
            "DEFAULT_CSV": target.DEFAULT_CSV,
            "DEFAULT_MD": target.DEFAULT_MD,
            "GAP_IDS": target.GAP_IDS,
            "MANIFEST_SHA256": target.MANIFEST_SHA256,
        }
        target.ROOT = self.root
        target.DEFAULT_MANIFEST = self.manifest_path
        target.DEFAULT_REVIEWED = self.reviewed_path
        target.DEFAULT_CSV = self.root / target.CSV_PATH
        target.DEFAULT_MD = self.root / target.MD_PATH
        target.GAP_IDS = (self.gap_id,)
        target.MANIFEST_SHA256 = self.manifest_sha256
        stdout = io.StringIO()
        stderr = io.StringIO()
        try:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                self.assertEqual(target.main(["--write"]), 0)
                self.assertEqual(target.main(["--check"]), 0)
            self.assertTrue(target.DEFAULT_CSV.is_file())
            self.assertTrue(target.DEFAULT_MD.is_file())
            target.DEFAULT_CSV.write_bytes(target.DEFAULT_CSV.read_bytes() + b"stale")
            with redirect_stdout(stdout), redirect_stderr(stderr):
                self.assertEqual(target.main(["--check"]), 1)
            self.assertIn("stale generated file", stderr.getvalue())
        finally:
            for name, value in saved.items():
                setattr(target, name, value)

    def test_committed_schema_and_reviewed_input_match_runtime_contract(self) -> None:
        schema = json.loads(
            (target.ROOT / target.SCHEMA_PATH).read_text(encoding="utf-8")
        )
        document = json.loads(target.DEFAULT_REVIEWED.read_text(encoding="utf-8"))
        self.assertEqual(
            set(schema["required"]),
            {
                "schema_version",
                "acquisition_gap_manifest_path",
                "acquisition_gap_manifest_sha256",
                "nonterminal_reports",
                "nonterminal_evidence",
                "records",
            },
        )
        self.assertEqual(schema["properties"]["schema_version"]["const"], target.SCHEMA_VERSION)
        self.assertEqual(
            set(schema["$defs"]["record"]["required"]), target.RECORD_FIELDS
        )
        self.assertEqual(
            set(schema["$defs"]["record"]["properties"]), target.RECORD_FIELDS
        )
        self.assertEqual(
            set(schema["$defs"]["nonterminalReport"]["required"]),
            target.NONTERMINAL_REPORT_FIELDS,
        )
        self.assertEqual(
            set(schema["$defs"]["contentLink"]["required"]),
            target.CONTENT_LINK_FIELDS,
        )
        self.assertEqual(
            set(schema["$defs"]["aiEvidence"]["required"]),
            target.AI_EVIDENCE_FIELDS,
        )
        self.assertEqual(
            set(schema["$defs"]["mechanicalEvidence"]["required"]),
            target.MECHANICAL_EVIDENCE_FIELDS,
        )
        self.assertEqual(document["schema_version"], target.SCHEMA_VERSION)
        self.assertEqual(document["records"], [])
        self.assertEqual(len(document["nonterminal_reports"]), 3)
        self.assertEqual(len(document["nonterminal_evidence"]), 1)
        sweep_report = document["nonterminal_reports"][0]
        self.assertEqual(
            sweep_report["path"],
            "spec/research/acquisition-completion-sweep-01-2026-08-13.md",
        )
        self.assertEqual(
            sweep_report["sha256"],
            "a76b5b107ca816ba802b5191efa0cab00c81f02c73c61a154d95fa7d39b1fef9",
        )
        self.assertEqual(sweep_report["applies_to_gap_ids"], list(target.GAP_IDS))
        boolean_report = document["nonterminal_reports"][1]
        self.assertEqual(
            boolean_report["path"],
            "spec/research/acquisition-gap-boolean-algebras-volumes-2026-08-14.md",
        )
        self.assertEqual(
            boolean_report["sha256"],
            "74783baec57c8c377e4fa02e8f9b22b97a6d9638b64492aafa3f902b238a5d94",
        )
        self.assertEqual(boolean_report["report_result"], "not_clean")
        self.assertEqual(boolean_report["gap_status_effect"], "none")
        self.assertEqual(boolean_report["applies_to_gap_ids"], ["ACQ-GAP-002"])
        history_report = document["nonterminal_reports"][2]
        self.assertEqual(
            history_report["path"],
            "spec/research/acquisition-gap-history-of-logic-volumes-1-10-2026-08-14.md",
        )
        self.assertEqual(
            history_report["sha256"],
            "7a962c9a6a52c40781f20f2ad5283e81a0f7b1516600367f2ab7f815c7078d19",
        )
        self.assertEqual(history_report["report_result"], "not_clean")
        self.assertEqual(history_report["gap_status_effect"], "none")
        self.assertEqual(history_report["applies_to_gap_ids"], ["ACQ-GAP-003"])
        for boundary in (
            "rights_holder_contacts",
            "external_messages_sent",
            "subscription_only_bodies_retrieved",
            "inaccessible_bodies_credited_as_acquired",
        ):
            self.assertEqual(sweep_report[boundary], 0)
            self.assertEqual(boolean_report[boundary], 0)
            self.assertEqual(history_report[boundary], 0)
        evidence = document["nonterminal_evidence"][0]
        self.assertEqual(evidence["evidence_type"], "planned_presentation")
        self.assertEqual(evidence["applies_to_gap_ids"], ["ACQ-GAP-001"])
        self.assertEqual(evidence["gap_status_effect"], "none")

    def test_committed_boolean_algebras_report_is_nonterminal_and_blocks_gap_002_resolution(
        self,
    ) -> None:
        rows = target.load_manifest(
            target.DEFAULT_MANIFEST,
            target.ROOT,
            expected_gap_ids=target.GAP_IDS,
            expected_manifest_sha256=target.MANIFEST_SHA256,
        )
        projected = target.apply_reviewed_records(
            rows,
            target.DEFAULT_REVIEWED,
            target.DEFAULT_MANIFEST,
            target.ROOT,
        )
        self.assertEqual(len(projected), 6)
        self.assertTrue(all(row["resolution_status"] == "OPEN" for row in projected))
        by_id = {row["acquisition_id"]: row for row in projected}
        gap_002_reports = json.loads(by_id["ACQ-GAP-002"]["nonterminal_report_refs"])
        self.assertEqual(
            gap_002_reports,
            [
                {
                    "path": "spec/research/acquisition-completion-sweep-01-2026-08-13.md",
                    "sha256": "a76b5b107ca816ba802b5191efa0cab00c81f02c73c61a154d95fa7d39b1fef9",
                    "report_result": "not_clean",
                },
                {
                    "path": "spec/research/acquisition-gap-boolean-algebras-volumes-2026-08-14.md",
                    "sha256": "74783baec57c8c377e4fa02e8f9b22b97a6d9638b64492aafa3f902b238a5d94",
                    "report_result": "not_clean",
                },
            ],
        )
        boolean_path = gap_002_reports[1]["path"]
        for acquisition_id, row in by_id.items():
            if acquisition_id != "ACQ-GAP-002":
                self.assertNotIn(boolean_path, row["nonterminal_report_refs"])

        document = json.loads(target.DEFAULT_REVIEWED.read_text(encoding="utf-8"))
        document["nonterminal_reports"] = [document["nonterminal_reports"][1]]
        document["nonterminal_evidence"] = []
        terminal_attempt = {field: None for field in target.RECORD_FIELDS}
        terminal_attempt["acquisition_id"] = "ACQ-GAP-002"
        document["records"] = [terminal_attempt]
        reviewed_path = self.root / "boolean-terminal-attempt.json"
        reviewed_path.write_text(
            json.dumps(document, indent=2) + "\n", encoding="utf-8"
        )
        with self.assertRaisesRegex(
            ValueError,
            "nonterminal NOT CLEAN report keeps it OPEN",
        ):
            target.apply_reviewed_records(
                rows,
                reviewed_path,
                target.DEFAULT_MANIFEST,
                target.ROOT,
            )

    def test_committed_history_of_logic_report_is_nonterminal_and_blocks_gap_003_resolution(
        self,
    ) -> None:
        rows = target.load_manifest(
            target.DEFAULT_MANIFEST,
            target.ROOT,
            expected_gap_ids=target.GAP_IDS,
            expected_manifest_sha256=target.MANIFEST_SHA256,
        )
        projected = target.apply_reviewed_records(
            rows,
            target.DEFAULT_REVIEWED,
            target.DEFAULT_MANIFEST,
            target.ROOT,
        )
        self.assertEqual(len(projected), 6)
        self.assertTrue(all(row["resolution_status"] == "OPEN" for row in projected))
        by_id = {row["acquisition_id"]: row for row in projected}
        gap_003_reports = json.loads(by_id["ACQ-GAP-003"]["nonterminal_report_refs"])
        self.assertEqual(
            gap_003_reports,
            [
                {
                    "path": "spec/research/acquisition-completion-sweep-01-2026-08-13.md",
                    "sha256": "a76b5b107ca816ba802b5191efa0cab00c81f02c73c61a154d95fa7d39b1fef9",
                    "report_result": "not_clean",
                },
                {
                    "path": "spec/research/acquisition-gap-history-of-logic-volumes-1-10-2026-08-14.md",
                    "sha256": "7a962c9a6a52c40781f20f2ad5283e81a0f7b1516600367f2ab7f815c7078d19",
                    "report_result": "not_clean",
                },
            ],
        )
        history_path = gap_003_reports[1]["path"]
        for acquisition_id, row in by_id.items():
            if acquisition_id != "ACQ-GAP-003":
                self.assertNotIn(history_path, row["nonterminal_report_refs"])

        document = json.loads(target.DEFAULT_REVIEWED.read_text(encoding="utf-8"))
        document["nonterminal_reports"] = [document["nonterminal_reports"][2]]
        document["nonterminal_evidence"] = []
        terminal_attempt = {field: None for field in target.RECORD_FIELDS}
        terminal_attempt["acquisition_id"] = "ACQ-GAP-003"
        document["records"] = [terminal_attempt]
        reviewed_path = self.root / "history-terminal-attempt.json"
        reviewed_path.write_text(
            json.dumps(document, indent=2) + "\n", encoding="utf-8"
        )
        with self.assertRaisesRegex(
            ValueError,
            "nonterminal NOT CLEAN report keeps it OPEN",
        ):
            target.apply_reviewed_records(
                rows,
                reviewed_path,
                target.DEFAULT_MANIFEST,
                target.ROOT,
            )


if __name__ == "__main__":
    unittest.main()
