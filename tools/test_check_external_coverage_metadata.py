"""CAT-01 fixtures are synthetic decisions, never real review/admission records."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import unittest
from pathlib import Path
from unittest import mock

import jsonschema

from tools import check_external_coverage_assignments as checker
from tools import build_presentation_packet_admission as admission
from tools import test_check_external_coverage_assignments as assignment_fixtures
from tools.test_check_external_coverage_assignments import csv_raw, digest


class MetadataDispositionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = assignment_fixtures.ExternalCoverageAssignmentTests()
        self.fixture.setUp()
        self.root = self.fixture.root
        self.title = "Synthetic acquisition source; no actual admission"

        def row(stable: str, kind: str, parent: str, title: str, hierarchy: list[str]) -> dict[str, str]:
            value = {field: "" for field in checker.CATALOG_FIELDS}
            value.update(stable_id=stable, record_type=kind, source_id="SRC-068",
                         source_title=self.title, parent_stable_id=parent, displayed_title=title,
                         hierarchy_path=json.dumps(hierarchy, ensure_ascii=False, separators=(",", ":")),
                         retrieval_date="2026-08-12", mapping_status="open/unmapped")
            return value

        self.source = row("SRC-068", "source", "", self.title, [self.title])
        self.parent = row("SRC-068-H278", "hierarchy", "SRC-068", checker.DESCRIPTOR_HEADING, [self.title, checker.DESCRIPTOR_HEADING])
        self.preceding = row("SRC-068-T11119", "topic", "SRC-068-H277", "An unresolved actual presentation", [self.title, "Other", "An unresolved actual presentation"])
        self.rows = []
        for stable in ("SRC-001", "SRC-002"):
            value = row(stable, "source", "", stable, [stable])
            value.update(source_id=stable, source_title=stable)
            self.rows.append(value)
        self.rows.extend([self.source, row("SRC-068-H277", "hierarchy", "SRC-068", "Other", [self.title, "Other"]), self.preceding, self.parent])
        selected = []
        for ordinal in range(1, 410):
            topic = 11119 + ordinal
            fields = {"topic": f"{topic:06d}", "scratch": f"{ordinal:04d}",
                      "path": f"tmp/acquisition/src068/file-{ordinal:04d}.bin", "bytes": "12", "lines": "1", "sha": "a" * 64}
            title = (f"[TOPIC-{fields['topic']}] [SCRATCH-{fields['scratch']}] {fields['path']}"
                     f" | bytes=12 | physical_lines=1 | sha256={'a' * 64} — **OPEN**")
            original = row(f"SRC-068-T{topic}", "topic", "SRC-068-H278", title, [self.title, checker.DESCRIPTOR_HEADING, title])
            self.rows.append(copy.deepcopy(original))
            payload = json.dumps(original, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
            selected.append({"original_record": original, "payload_sha256": hashlib.sha256(payload).hexdigest(), "descriptor_fields": fields})
        self.receipt = {
            "standing": "Synthetic mechanical fixture; not an admission",
            "catalog_path": "spec/coverage.csv", "catalog_sha256": "", "catalog_bytes": 0, "rows": 0,
            "type_counts": {}, "source_count": 3, "all_stable_ids_unique": True,
            "uniqueness_method": "Synthetic rows with distinct stable IDs",
            "predicate": checker.DESCRIPTOR_PATTERN, "selected_count": 409,
            "source_and_parent": {"SRC-068": copy.deepcopy(self.source), "SRC-068-H278": copy.deepcopy(self.parent)},
            "preceding_excluded_record": copy.deepcopy(self.preceding), "selected": selected,
        }
        self.receipt_path = "spec/provenance/external-coverage-assignments/descriptor-receipt.json"
        self.rationale_path = "spec/research/synthetic-descriptor-rationale.md"
        self.fixture.write(self.rationale_path, b"Synthetic producer rationale for tests only.\n")
        self.save()

    def tearDown(self) -> None:
        self.fixture.tearDown()

    def save(self) -> None:
        raw = csv_raw(checker.CATALOG_FIELDS, self.rows)
        self.fixture.coverage_path.write_bytes(raw)
        self.receipt.update(catalog_sha256=digest(raw), catalog_bytes=len(raw), rows=len(self.rows))
        self.receipt["type_counts"] = {kind: sum(row["record_type"] == kind for row in self.rows) for kind in ("source", "hierarchy", "topic")}
        self.receipt["source_count"] = self.receipt["type_counts"]["source"]
        receipt_raw = (json.dumps(self.receipt, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        self.fixture.write(self.receipt_path, receipt_raw)
        self.fixture.write_sidecar(self.fixture.sidecar_rows)
        self.index = self.fixture.index(include_sidecar=True)
        self.index.update(schema_version=2, coverage_manifest_record_count=len(self.rows))
        self.batch = {
            "disposition_id": "META-synthetic-src068", "disposition_kind": "acquisition_file_descriptor",
            "descriptor_profile": "src068-h278-v1", "membership_receipt_path": self.receipt_path,
            "membership_receipt_sha256": digest(receipt_raw), "rationale_path": self.rationale_path,
            "rationale_sha256": digest((self.root / self.rationale_path).read_bytes()), "verification_evidence": [],
        }
        authorities = sorted([
            {"path": "spec/coverage.csv", "sha256": digest(raw)},
            {"path": self.receipt_path, "sha256": self.batch["membership_receipt_sha256"]},
            {"path": self.rationale_path, "sha256": self.batch["rationale_sha256"]},
        ], key=lambda item: item["path"])
        for ordinal, category in enumerate(admission.AI_VERIFICATION_FIELDS):
            artifact = f"spec/verification/synthetic-{ordinal}.md"
            artifact_raw = f"Synthetic {category} fixture; not a real review.\n".encode()
            self.fixture.write(artifact, artifact_raw)
            self.batch["verification_evidence"].append({
                "category": category, "recorded_result": "pass", "artifact_path": artifact,
                "sha256": digest(artifact_raw), "producer_identity": f"synthetic reviewer {ordinal}",
                "recorded_scope": checker.metadata_review_scope(self.batch, self.index),
                "model": "synthetic fixture model", "model_version": "synthetic fixture version",
                "instructions": "Synthetic bounded metadata review fixture",
                "consulted_authority_files": copy.deepcopy(authorities),
                "consulted_authority_locators": [checker.DESCRIPTOR_LOCATOR],
                "findings": [f"Synthetic independent {category} finding"], "evidence_digest": digest(artifact_raw),
            })
        self.index["metadata_dispositions"] = [self.batch]
        self.write_index()

    def write_index(self) -> None:
        self.fixture.index_path.write_text(json.dumps(self.index) + "\n", encoding="utf-8")

    def check(self, complete: bool = False) -> checker.CoverageAssignmentResult:
        return checker.validate_index(self.root, self.fixture.index_path, complete)

    def test_valid_batch_is_metadata_and_catalog_is_streamed_once(self) -> None:
        original = checker.HashedUtf8Lines.__iter__
        calls = []

        def counted(lines):
            if lines.path == self.fixture.coverage_path:
                calls.append(lines.path)
            return original(lines)

        original_read = Path.read_bytes

        def bounded_read(path):
            self.assertNotEqual(path, self.fixture.coverage_path, "catalog must not be loaded as an authority blob")
            return original_read(path)

        with mock.patch.object(checker.HashedUtf8Lines, "__iter__", counted), mock.patch.object(Path, "read_bytes", bounded_read):
            result = self.check()
        self.assertEqual(calls, [self.fixture.coverage_path])
        self.assertEqual((result.coverage_record_count, result.assignment_count, result.metadata_disposition_count, result.metadata_batch_count, result.unassigned_count), (415, 2, 409, 1, 4))
        self.assertEqual((result.admitted_packet_count, result.sidecar_count), (1, 1))
        with self.assertRaisesRegex(ValueError, "remains unassigned: 4"):
            self.check(complete=True)

    def test_complete_requires_disjoint_content_plus_metadata(self) -> None:
        for row in self.rows[2:6]:
            self.fixture.sidecar_rows.append({**self.fixture.sidecar_rows[-1], "coverage_id": row["stable_id"]})
        self.save()
        result = self.check(complete=True)
        self.assertEqual((result.assignment_count, result.metadata_disposition_count, result.unassigned_count), (6, 409, 0))

    def test_versions_and_schema_are_strict(self) -> None:
        schema = json.loads((checker.ROOT / "spec/external-coverage-assignment-index.schema.json").read_text())
        validator = jsonschema.Draft202012Validator(schema)
        validator.validate(self.index)
        for change in ({"schema_version": 1}, {"schema_version": True}, {"schema_version": 3}, {"unexpected": 1}):
            with self.subTest(change=change):
                invalid = {**self.index, **change}
                with self.assertRaises(jsonschema.ValidationError):
                    validator.validate(invalid)
                self.fixture.index_path.write_text(json.dumps(invalid), encoding="utf-8")
                with self.assertRaises(ValueError):
                    self.check()
        invalid = {key: value for key, value in self.index.items() if key != "metadata_dispositions"}
        self.fixture.index_path.write_text(json.dumps(invalid), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "exact field set"):
            self.check()

    def test_missing_failing_stale_or_reused_review_evidence(self) -> None:
        mutations = [
            lambda batch: batch["verification_evidence"].pop(),
            lambda batch: batch["verification_evidence"][0].update(recorded_result="fail"),
            lambda batch: batch["verification_evidence"][0].update(recorded_scope="old disposition scope"),
            lambda batch: batch["verification_evidence"][0].update(sha256="0" * 64),
            lambda batch: batch["verification_evidence"][0].update(evidence_digest="0" * 64),
            lambda batch: batch["verification_evidence"][0].update(model_version=""),
            lambda batch: batch["verification_evidence"][0].update(instructions=""),
            lambda batch: batch["verification_evidence"][0].update(findings=[]),
            lambda batch: batch["verification_evidence"][1].update(producer_identity="SYNTHETIC REVIEWER 0"),
            lambda batch: batch["verification_evidence"][1].update(category="source_fidelity_ai"),
            lambda batch: batch["verification_evidence"][0].update(consulted_authority_files=[]),
            lambda batch: batch["verification_evidence"][0]["consulted_authority_files"].pop(0),
            lambda batch: batch["verification_evidence"][0]["consulted_authority_files"][0].update(sha256="0" * 64),
            lambda batch: batch["verification_evidence"][0].update(consulted_authority_locators=["wrong locator"]),
            lambda batch: batch["verification_evidence"][0].update(artifact_path=batch["rationale_path"]),
            lambda batch: batch.update(disposition_id="META-changed-decision"),
            lambda batch: batch.update(membership_receipt_path="../outside.json"),
        ]
        baseline = copy.deepcopy(self.batch)
        for ordinal, mutate in enumerate(mutations):
            self.index["metadata_dispositions"] = [copy.deepcopy(baseline)]
            mutate(self.index["metadata_dispositions"][0])
            self.write_index()
            with self.subTest(mutation=ordinal), self.assertRaises(ValueError):
                self.check()

    def test_receipt_rationale_artifact_and_catalog_drift(self) -> None:
        for path in (self.receipt_path, self.rationale_path, "spec/verification/synthetic-0.md"):
            file = self.root / path
            original = file.read_bytes()
            file.write_bytes(original + b"stale\n")
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, "digest drift|SHA-256 drift"):
                self.check()
            file.write_bytes(original)
        self.fixture.coverage_path.write_bytes(self.fixture.coverage_path.read_bytes() + b"\n")
        with self.assertRaisesRegex(ValueError, "byte-count drift"):
            self.check()

    def test_broad_predicate_bad_profile_and_nonmetadata_rows_are_rejected(self) -> None:
        baseline = copy.deepcopy(self.receipt)
        mutations = [
            lambda receipt: receipt.update(predicate=".*"),
            lambda receipt: receipt.update(selected_count=410),
            lambda receipt: receipt["selected"][0].update(original_record=copy.deepcopy(self.parent)),
            lambda receipt: receipt["selected"][0].update(original_record=copy.deepcopy(self.preceding)),
            lambda receipt: receipt["selected"][1].update(original_record=copy.deepcopy(receipt["selected"][0]["original_record"])),
            lambda receipt: receipt["selected"][0].update(payload_sha256="0" * 64),
            lambda receipt: receipt["selected"][0]["descriptor_fields"].update(bytes="13"),
        ]
        for ordinal, mutate in enumerate(mutations):
            self.receipt = copy.deepcopy(baseline)
            mutate(self.receipt)
            self.save()
            with self.subTest(mutation=ordinal), self.assertRaises(ValueError):
                self.check()
        self.receipt = baseline
        self.save()
        for field, value in (("descriptor_profile", "src064"), ("disposition_kind", "arbitrary_exclusion")):
            self.batch[field] = value
            self.write_index()
            with self.assertRaisesRegex(ValueError, "unsupported"):
                self.check()

    def test_payload_source_parent_and_missing_members_fail(self) -> None:
        baseline = copy.deepcopy(self.rows)
        for position, field, value in ((6, "displayed_title", "A substantive theorem"), (6, "source_id", "SRC-067"), (6, "parent_stable_id", "SRC-068-H277"), (2, "source_metadata", "changed metadata"), (5, "displayed_title", "changed heading")):
            self.rows = copy.deepcopy(baseline)
            self.rows[position][field] = value
            self.save()
            with self.subTest(field=field, position=position), self.assertRaisesRegex(ValueError, "payload/source/parent drift"):
                self.check()
        self.rows = copy.deepcopy(baseline[:-1])
        self.save()
        with self.assertRaisesRegex(ValueError, "unknown or missing catalog IDs"):
            self.check()
        self.rows = copy.deepcopy(baseline)
        self.rows.append({**self.rows[-1], "stable_id": "SRC-068-T11529"})
        self.save()
        with self.assertRaisesRegex(ValueError, "unexpected child"):
            self.check()

    def test_duplicate_batches_overlap_and_content_overlap(self) -> None:
        duplicate = copy.deepcopy(self.batch)
        self.index["metadata_dispositions"].append(duplicate)
        self.write_index()
        with self.assertRaisesRegex(ValueError, "duplicate disposition ID"):
            self.check()
        duplicate["disposition_id"] = "META-overlapping-batch"
        self.write_index()
        with self.assertRaisesRegex(ValueError, "overlapping metadata batches"):
            self.check()
        self.index["metadata_dispositions"].pop()
        self.fixture.sidecar_rows.append({**self.fixture.sidecar_rows[-1], "coverage_id": "SRC-068-T11120"})
        self.save()
        with self.assertRaisesRegex(ValueError, "overlaps content assignment"):
            self.check()
        self.fixture.packet["obligation_links"]["coverage_assignments"][0]["obligation_id"] = "SRC-068-T11120"
        self.fixture.write_packet()
        self.fixture.write_admission(admitted=True)
        self.save()
        with self.assertRaisesRegex(ValueError, "overlaps packet-declared content"):
            self.check()

    def test_version_two_retains_every_content_review_gate(self) -> None:
        for category in admission.VERIFICATION_FIELDS:
            row = self.fixture.admission_row(admitted=True)
            row[f"{category}_verification"] = "pending"
            self.fixture.admission_path.write_bytes(csv_raw(admission.OUTPUT_FIELDS, [row]))
            self.save()
            with self.subTest(category=category), self.assertRaisesRegex(ValueError, f"lacks passing {category}"):
                self.check()

    def test_hardlinked_self_evidence_is_rejected(self) -> None:
        alias = self.root / "spec/verification/hardlinked-rationale.md"
        try:
            os.link(self.root / self.rationale_path, alias)
        except OSError as exc:
            self.skipTest(f"hardlinks unavailable: {exc}")
        self.batch["verification_evidence"][0]["artifact_path"] = alias.relative_to(self.root).as_posix()
        self.write_index()
        with self.assertRaisesRegex(ValueError, "filesystem identity"):
            self.check()

    def test_catalog_authority_alias_is_rejected_without_blob_read(self) -> None:
        alias = self.root / "spec/catalog-alias.csv"
        try:
            os.link(self.fixture.coverage_path, alias)
        except OSError as exc:
            self.skipTest(f"hardlinks unavailable: {exc}")
        authorities = self.batch["verification_evidence"][0]["consulted_authority_files"]
        authorities.append({"path": "spec/catalog-alias.csv", "sha256": self.index["coverage_manifest_sha256"]})
        authorities.sort(key=lambda item: item["path"])
        self.write_index()
        with self.assertRaisesRegex(ValueError, "catalog authority requires its canonical path"):
            self.check()

    def test_review_artifacts_cannot_reuse_bytes_under_new_names(self) -> None:
        first, second = self.batch["verification_evidence"][:2]
        duplicate = self.root / second["artifact_path"]
        duplicate.write_bytes((self.root / first["artifact_path"]).read_bytes())
        second.update(sha256=first["sha256"], evidence_digest=first["sha256"])
        self.write_index()
        with self.assertRaisesRegex(ValueError, "distinct non-self evidence bytes"):
            self.check()


if __name__ == "__main__":
    unittest.main()
