#!/usr/bin/env python3
"""Focused contract tests for the six independent review/validation gates."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools import build_handbook_unit_reverse_ledger as handbook
from tools import build_source_unit_audit_crosswalk as source


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = (
    "source_fidelity_ai",
    "topic_specialist_ai",
    "adversarial_publication_ai",
    "static",
    "build",
    "visual",
)


class AiReviewSchemaMigrationTests(unittest.TestCase):
    def test_generators_use_exact_six_gates(self) -> None:
        self.assertEqual(source.VERIFICATION_FIELDS, EXPECTED)
        self.assertEqual(handbook.VERIFICATION_FIELDS, EXPECTED)

    def test_existing_source_records_migrate_ai_gates_as_pending(self) -> None:
        document = json.loads(
            (ROOT / "spec/provenance/reviewed-source-unit-records.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(document["schema_version"], source.REVIEW_SCHEMA_VERSION)
        self.assertGreater(len(document["records"]), 0)
        for record in document["records"]:
            self.assertEqual(set(record["verification"]), set(EXPECTED))
            for field in EXPECTED[:3]:
                self.assertEqual(record["verification"][field], "pending")

    def test_empty_handbook_records_migrate_without_promotion(self) -> None:
        document = json.loads(
            (ROOT / "spec/provenance/reviewed-handbook-unit-records.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(document["schema_version"], handbook.SCHEMA_VERSION)
        self.assertEqual(document["records"], [])

    def test_active_schemas_do_not_expose_generic_human_gate(self) -> None:
        for name in (
            "reviewed-source-unit-records.schema.json",
            "reviewed-handbook-unit-records.schema.json",
        ):
            text = (ROOT / "spec/provenance" / name).read_text(encoding="utf-8")
            self.assertNotIn('"human"', text)
            self.assertNotIn("human_content_review", text)
            for field in EXPECTED:
                self.assertIn(f'"{field}"', text)


if __name__ == "__main__":
    unittest.main()
