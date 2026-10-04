#!/usr/bin/env python3
"""Contract tests for AI review gates in register and packet controls."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools import build_register_obligation_closure as register
from tools import check_presentation_packet as packet


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = (
    "source_fidelity_ai",
    "topic_specialist_ai",
    "adversarial_publication_ai",
    "static",
    "build",
    "visual",
)
AI_KEYS = EXPECTED[:3]


class RegisterPacketAiReviewMigrationTests(unittest.TestCase):
    def point_packet_checker_at_fixture_manifests(self, base: Path) -> None:
        coverage = base / "coverage.csv"
        coverage.write_text("stable_id\nSRC-001\n", encoding="utf-8")
        register_manifest = base / "register.csv"
        register_manifest.write_text("obligation_id\n", encoding="utf-8")
        packet.COVERAGE_MANIFEST = coverage
        packet.REGISTER_MANIFEST = register_manifest

    def test_generators_use_exact_six_gates(self) -> None:
        self.assertEqual(register.VERIFICATION_FIELDS, EXPECTED)
        self.assertEqual(packet.VERIFICATION_KEYS, EXPECTED)

    def test_active_schemas_remove_generic_human_gates(self) -> None:
        for path in (
            ROOT / "spec/provenance/reviewed-register-obligation-records.schema.json",
            ROOT / "spec/presentation-packet.schema.json",
        ):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn('"human"', text)
            self.assertNotIn("human_content_review", text)
            for key in EXPECTED:
                self.assertIn(f'"{key}"', text)

    def test_empty_register_input_migrates_without_promotion(self) -> None:
        document = json.loads(
            (
                ROOT / "spec/provenance/reviewed-register-obligation-records.json"
            ).read_text(encoding="utf-8")
        )
        schema = json.loads(
            (
                ROOT
                / "spec/provenance/reviewed-register-obligation-records.schema.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(document["schema_version"], register.SCHEMA_VERSION)
        self.assertEqual(
            schema["properties"]["schema_version"]["const"], register.SCHEMA_VERSION
        )
        self.assertEqual(document["records"], [])

    def test_open_packet_uses_pending_six_gate_shape(self) -> None:
        value = packet._open_fixture()
        self.assertEqual(value["schema_version"], packet.SCHEMA_VERSION)
        self.assertEqual(tuple(value["verification"]), EXPECTED)
        self.assertEqual(set(value["verification"].values()), {"pending"})
        self.assertEqual(value["verification_evidence"], [])

    def test_verified_packet_ai_evidence_carries_required_review_metadata(self) -> None:
        with tempfile.TemporaryDirectory(prefix="packet-ai-review-") as temporary:
            base = Path(temporary)
            self.point_packet_checker_at_fixture_manifests(base)
            value = packet._verified_fixture(base)
            errors = packet.validate_packet(value, base_dir=base)
            self.assertEqual(errors, [])
            by_kind = {item["kind"]: item for item in value["verification_evidence"]}
            for kind in AI_KEYS:
                self.assertEqual(
                    set(packet.AI_EVIDENCE_FIELDS), set(by_kind[kind])
                )
                self.assertTrue(by_kind[kind]["model"])
                self.assertTrue(by_kind[kind]["model_version"])
                self.assertTrue(by_kind[kind]["instructions"])
                self.assertTrue(by_kind[kind]["consulted_authority_files"])
                self.assertTrue(by_kind[kind]["consulted_authority_locators"])
                self.assertTrue(by_kind[kind]["findings"])
                self.assertEqual(
                    by_kind[kind]["evidence_digest"], by_kind[kind]["sha256"]
                )

    def test_verified_packet_ai_evidence_missing_model_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="packet-ai-review-") as temporary:
            base = Path(temporary)
            self.point_packet_checker_at_fixture_manifests(base)
            value = packet._verified_fixture(base)
            evidence = next(
                item
                for item in value["verification_evidence"]
                if item["kind"] == "source_fidelity_ai"
            )
            del evidence["model"]
            errors = packet.validate_packet(value, base_dir=base)
            self.assertTrue(any("model" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
