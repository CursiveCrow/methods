#!/usr/bin/env python3
"""Adversarial tests for independent presentation-packet admission."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

import jsonschema

from tools import build_presentation_packet_admission as admission
from tools import check_presentation_packet as packet_checker


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


class PresentationPacketAdmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="packet-admission-")
        self.root = Path(self.temporary.name)
        (self.root / "spec/presentations").mkdir(parents=True)
        (self.root / "spec/provenance").mkdir(parents=True)
        (self.root / "handbook").mkdir()
        self.coverage = self.write("spec/coverage.csv", b"stable_id\nSRC-001\n")
        self.register = self.write("spec/register.csv", b"obligation_id\n")
        self.packet = packet_checker._verified_fixture(self.root / "spec/presentations")
        destination = b"\\label{packet:self-test}\nComplete packet destination.\n"
        self.destination = self.write("handbook/self-test.tex", destination)
        self.packet_path = self.root / "spec/presentations/verified.json"
        self.write_packet(self.packet)
        self.evidence = self.make_evidence()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, raw: bytes) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return path

    def write_packet(self, value: dict[str, object]) -> None:
        self.packet_path.write_text(
            json.dumps(value, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def make_evidence(self) -> list[dict[str, object]]:
        result: list[dict[str, object]] = []
        authority = self.root / "spec/presentations/authority-source.txt"
        for index, category in enumerate(admission.VERIFICATION_FIELDS):
            path = f"spec/evidence/{category}.txt"
            raw = f"admission evidence {category}\n".encode("utf-8")
            self.write(path, raw)
            item: dict[str, object] = {
                "category": category,
                "recorded_result": "pass",
                "artifact_path": path,
                "sha256": digest(raw),
                "producer_identity": f"admission producer {index}",
                "recorded_scope": f"verified.self-test admission {category}",
            }
            if category in admission.AI_VERIFICATION_FIELDS:
                item.update(
                    {
                        "model": "self-test-model",
                        "model_version": f"version-{index}",
                        "instructions": "Review the packet against the exact authority.",
                        "consulted_authority_files": [
                            {
                                "path": authority.relative_to(self.root).as_posix(),
                                "sha256": digest(authority.read_bytes()),
                            }
                        ],
                        "consulted_authority_locators": ["Self-test locator"],
                        "findings": [f"The {category} review passes."],
                        "evidence_digest": digest(raw),
                    }
                )
            result.append(item)
        return result

    def record(self) -> dict[str, object]:
        packet_bytes = self.packet_path.read_bytes()
        return {
            "packet_id": "verified.self-test",
            "packet_path": "spec/presentations/verified.json",
            "packet_sha256": digest(packet_bytes),
            "admission_status": "admitted",
            "authority_projection_sha256": admission.canonical_digest(
                self.packet["authority"]
            ),
            "presentation_identity_projection_sha256": admission.canonical_digest(
                self.packet["presentation_identity"]
            ),
            "content_projection_sha256": admission.canonical_digest(
                self.packet["content"]
            ),
            "present_content_item_ids": ["self-test.definitions.present"],
            "destination_file": "handbook/self-test.tex",
            "destination_sha256": digest(self.destination.read_bytes()),
            "destination_labels": ["packet:self-test"],
            "verification": {
                category: "pass" for category in admission.VERIFICATION_FIELDS
            },
            "verification_evidence": copy.deepcopy(self.evidence),
        }

    def document(self, records: list[dict[str, object]]) -> dict[str, object]:
        return {
            "schema_version": admission.SCHEMA_VERSION,
            "packet_root": "spec/presentations",
            "records": records,
        }

    def write_review(self, records: list[dict[str, object]]) -> Path:
        path = self.root / "spec/provenance/reviewed-presentation-packet-admissions.json"
        path.write_text(
            json.dumps(self.document(records), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return path

    def build(self, records: list[dict[str, object]]) -> list[dict[str, str]]:
        return admission.build_rows(
            self.root,
            self.root / "spec/presentations",
            self.write_review(records),
            self.coverage,
            self.register,
        )

    def test_empty_review_input_never_admits_verified_packet(self) -> None:
        rows = self.build([])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["admission_status"], "OPEN")
        self.assertEqual(rows[0]["present_content_item_ids"], "[]")

    def test_terminal_record_admits_exact_packet_and_content_items(self) -> None:
        packet_evidence = {
            item["kind"]: self.packet_path.parent / item["artifact_path"]
            for item in self.packet["verification_evidence"]
        }
        admission_evidence = {
            item["category"]: self.root / item["artifact_path"]
            for item in self.evidence
        }
        self.assertTrue(
            set(packet_evidence.values()).isdisjoint(admission_evidence.values())
        )
        self.assertTrue(
            {
                digest(path.read_bytes()) for path in packet_evidence.values()
            }.isdisjoint(
                {digest(path.read_bytes()) for path in admission_evidence.values()}
            )
        )
        self.assertTrue(
            all(
                not os.path.samefile(packet_evidence[category], admission_evidence[category])
                for category in admission.VERIFICATION_FIELDS
            )
        )
        rows = self.build([self.record()])
        self.assertEqual(rows[0]["admission_status"], "ADMITTED")
        self.assertEqual(
            json.loads(rows[0]["present_content_item_ids"]),
            ["self-test.definitions.present"],
        )
        self.assertEqual(rows[0]["visual_verification"], "pass")

    def test_packet_declared_verification_evidence_cannot_attest_admission(self) -> None:
        packet_evidence = {
            item["kind"]: item for item in self.packet["verification_evidence"]
        }
        exact_reuse = self.record()
        for item in exact_reuse["verification_evidence"]:  # type: ignore[union-attr]
            declared = packet_evidence[item["category"]]
            declared_path = self.packet_path.parent / declared["artifact_path"]
            item["artifact_path"] = declared_path.relative_to(self.root).as_posix()
            item["sha256"] = declared["sha256"]
            if item["category"] in admission.AI_VERIFICATION_FIELDS:
                item["evidence_digest"] = declared["sha256"]
        with self.assertRaisesRegex(ValueError, "packet-declared verification evidence"):
            self.build([exact_reuse])

        declared = packet_evidence[admission.VERIFICATION_FIELDS[0]]
        declared_path = self.packet_path.parent / declared["artifact_path"]
        copied_path = self.write(
            "spec/evidence/copied-packet-evidence.txt", declared_path.read_bytes()
        )
        copied_reuse = self.record()
        copied_item = copied_reuse["verification_evidence"][0]  # type: ignore[index]
        copied_item["artifact_path"] = copied_path.relative_to(self.root).as_posix()
        copied_item["sha256"] = declared["sha256"]
        copied_item["evidence_digest"] = declared["sha256"]
        with self.assertRaisesRegex(ValueError, "packet-declared verification evidence"):
            self.build([copied_reuse])

        hardlink_path = self.root / "spec/evidence/hardlinked-packet-evidence.txt"
        try:
            os.link(declared_path, hardlink_path)
        except OSError as exc:
            self.skipTest(f"hardlinks unavailable: {exc}")
        hardlink_reuse = self.record()
        hardlink_item = hardlink_reuse["verification_evidence"][0]  # type: ignore[index]
        hardlink_item["artifact_path"] = hardlink_path.relative_to(self.root).as_posix()
        hardlink_item["sha256"] = declared["sha256"]
        hardlink_item["evidence_digest"] = declared["sha256"]
        with self.assertRaisesRegex(ValueError, "packet-declared verification evidence"):
            self.build([hardlink_reuse])

    def test_packet_declared_evidence_rejects_symlink_indirection(self) -> None:
        item = self.packet["verification_evidence"][0]
        target = self.packet_path.parent / item["artifact_path"]
        link = self.packet_path.parent / "linked-packet-evidence.txt"
        try:
            link.symlink_to(target.name)
        except OSError as exc:
            self.skipTest(f"symlinks unavailable: {exc}")
        item["artifact_path"] = link.name
        self.write_packet(self.packet)
        with self.assertRaisesRegex(ValueError, "symlink|junction|indirection"):
            self.build([self.record()])

    def test_duplicate_unknown_and_stale_packet_records_fail_closed(self) -> None:
        record = self.record()
        with self.assertRaisesRegex(ValueError, "duplicate packet ID"):
            self.build([record, copy.deepcopy(record)])
        unknown = self.record()
        unknown["packet_id"] = "unknown.packet"
        with self.assertRaisesRegex(ValueError, "unknown packet ID"):
            self.build([unknown])
        stale = self.record()
        stale["packet_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "packet SHA-256 drift"):
            self.build([stale])

    def test_projection_and_destination_drift_fail_closed(self) -> None:
        record = self.record()
        record["content_projection_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "content projection"):
            self.build([record])
        record = self.record()
        record["destination_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "destination SHA-256 drift"):
            self.build([record])

    def test_ai_evidence_metadata_is_required(self) -> None:
        record = self.record()
        del record["verification_evidence"][0]["model"]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "model"):
            self.build([record])

    def test_packet_discovery_rejects_symlink_indirection(self) -> None:
        outside = self.root / "spec/elsewhere.json"
        other = copy.deepcopy(self.packet)
        other["packet_id"] = "verified.symlink-target"
        outside.write_text(json.dumps(other) + "\n", encoding="utf-8")
        link = self.root / "spec/presentations/symlink.json"
        try:
            link.symlink_to(outside)
        except OSError as exc:
            self.skipTest(f"symlinks unavailable: {exc}")
        with self.assertRaisesRegex(ValueError, "symlink|packet root"):
            admission.discover_packets(self.root, self.root / "spec/presentations")

    def test_evidence_scope_self_bytes_and_authority_binding_are_exact(self) -> None:
        record = self.record()
        record["verification_evidence"][0]["recorded_scope"] = (  # type: ignore[index]
            "verified.self-test-extra admission"
        )
        with self.assertRaisesRegex(ValueError, "exact packet scope"):
            self.build([record])

        record = self.record()
        item = record["verification_evidence"][0]  # type: ignore[index]
        artifact = self.root / item["artifact_path"]
        artifact.write_bytes(self.destination.read_bytes())
        item["sha256"] = digest(self.destination.read_bytes())
        item["evidence_digest"] = item["sha256"]
        with self.assertRaisesRegex(ValueError, "self evidence bytes"):
            self.build([record])

        self.evidence = self.make_evidence()
        record = self.record()
        item = record["verification_evidence"][0]  # type: ignore[index]
        unrelated = self.write("spec/unrelated-authority.txt", b"unrelated\n")
        item["consulted_authority_files"] = [
            {
                "path": unrelated.relative_to(self.root).as_posix(),
                "sha256": digest(unrelated.read_bytes()),
            }
        ]
        item["consulted_authority_locators"] = ["Unrelated locator"]
        with self.assertRaisesRegex(ValueError, "packet authority"):
            self.build([record])

    def test_schema_matches_terminal_record_and_outputs_are_deterministic(self) -> None:
        document = self.document([self.record()])
        schema_path = (
            Path(__file__).resolve().parents[1]
            / "spec/provenance/reviewed-presentation-packet-admissions.schema.json"
        )
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator(schema).validate(document)
        rows = self.build([self.record()])
        self.assertEqual(admission.csv_bytes(rows), admission.csv_bytes(copy.deepcopy(rows)))
        self.assertEqual(
            admission.markdown_bytes(rows),
            admission.markdown_bytes(copy.deepcopy(rows)),
        )
        malformed = copy.deepcopy(document)
        del malformed["records"][0]["verification_evidence"][0]["model"]  # type: ignore[index]
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(schema).validate(malformed)


if __name__ == "__main__":
    unittest.main()
