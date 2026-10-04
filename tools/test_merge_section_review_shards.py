#!/usr/bin/env python3
"""Focused tests for section-local review shard validation and merging."""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tools import merge_section_review_shards as merger


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SectionReviewShardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="section-review-")
        self.root = Path(self.temporary.name)
        source = self.root / "handbook/parts/p01/example.tex"
        source.parent.mkdir(parents=True)
        source.write_text("\\section{Example}\\label{sec:p01-example}\n", encoding="utf-8")
        self.source = source
        self.inventory = self.root / "spec/handbook-unit-inventory.csv"
        self.inventory.parent.mkdir(parents=True)
        with self.inventory.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["unit_id"])
            writer.writeheader()
            writer.writerow({"unit_id": "HBU-example"})

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def evidence(self, category: str, ai: bool = False) -> dict[str, object]:
        artifact = self.root / f"spec/evidence/{category}.md"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text(f"evidence for {category}\n", encoding="utf-8")
        value: dict[str, object] = {
            "category": category,
            "artifact_path": artifact.relative_to(self.root).as_posix(),
            "sha256": digest(artifact),
            "producer_identity": f"reviewer-{category}",
            "recorded_scope": "sec:p01-example",
        }
        if ai:
            value.update(
                {
                    "model": "model-family",
                    "model_version": "model-version",
                    "instructions": "Independently review the complete assigned section.",
                    "consulted_authorities": [
                        {
                            "path": self.source.relative_to(self.root).as_posix(),
                            "locator": "section sec:p01-example",
                            "sha256": digest(self.source),
                        }
                    ],
                    "findings": ["No defect found in the assigned scope."],
                    "other_review_outputs_consulted": False,
                }
            )
        return value

    def queued_section(self, section_id: str = "sec:p01-example") -> dict[str, object]:
        return {
            "schema_version": 1,
            "section": {
                "section_id": section_id,
                "part_id": "p01",
                "title": "Example",
                "state": "queued",
                "source_files": [
                    {
                        "path": self.source.relative_to(self.root).as_posix(),
                        "sha256": digest(self.source),
                    }
                ],
                "handbook_unit_ids": ["HBU-example"],
                "inherited_source_unit_ordinals": [],
                "presentation_packet_ids": [],
                "register_obligation_ids": [],
                "dependency_section_ids": [],
                "gates": {category: "pending" for category in merger.GATE_ORDER},
                "evidence": [],
            },
        }

    def write(self, name: str, document: dict[str, object]) -> Path:
        path = self.root / name
        path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
        return path

    def test_valid_queued_shard_is_preserved_deterministically(self) -> None:
        shard = self.write("queued.json", self.queued_section())
        merged = merger.merge_and_validate([shard], self.root, self.inventory)
        self.assertEqual(merged["schema_version"], 1)
        self.assertEqual(merged["sections"][0]["section_id"], "sec:p01-example")

    def test_duplicate_section_identity_is_rejected(self) -> None:
        first = self.write("first.json", self.queued_section())
        second = self.write("second.json", self.queued_section())
        with self.assertRaisesRegex(ValueError, "duplicate section_id"):
            merger.merge_and_validate([first, second], self.root, self.inventory)

    def test_source_digest_drift_is_rejected(self) -> None:
        document = self.queued_section()
        document["section"]["source_files"][0]["sha256"] = "0" * 64  # type: ignore[index]
        shard = self.write("drift.json", document)
        with self.assertRaisesRegex(ValueError, "source file digest drifted"):
            merger.merge_and_validate([shard], self.root, self.inventory)

    def test_state_cannot_skip_an_earlier_gate(self) -> None:
        document = self.queued_section()
        document["section"]["state"] = "external content integrated"  # type: ignore[index]
        document["section"]["gates"]["external_content"] = "pass"  # type: ignore[index]
        document["section"]["evidence"] = [self.evidence("external_content")]  # type: ignore[index]
        shard = self.write("skipped.json", document)
        with self.assertRaisesRegex(ValueError, "gate prefix"):
            merger.merge_and_validate([shard], self.root, self.inventory)

    def test_ai_gate_requires_isolated_model_evidence(self) -> None:
        document = self.queued_section()
        gates = document["section"]["gates"]  # type: ignore[index]
        evidence: list[dict[str, object]] = []
        for category in merger.GATE_ORDER[:6]:
            gates[category] = "pass"
            evidence.append(self.evidence(category, ai=category in merger.AI_GATES))
        document["section"]["state"] = "topics AI-approved"  # type: ignore[index]
        evidence[-1]["other_review_outputs_consulted"] = True
        document["section"]["evidence"] = evidence  # type: ignore[index]
        shard = self.write("non-independent.json", document)
        with self.assertRaisesRegex(ValueError, "other review outputs"):
            merger.merge_and_validate([shard], self.root, self.inventory)

    def test_locked_section_requires_locked_dependencies(self) -> None:
        dependency = self.queued_section("sec:p01-dependency")
        dependency["section"]["title"] = "Dependency"  # type: ignore[index]
        locked = self.queued_section()
        locked_section = locked["section"]  # type: ignore[index]
        locked_section["state"] = "internally locked"
        locked_section["dependency_section_ids"] = ["sec:p01-dependency"]
        locked_section["gates"] = {category: "pass" for category in merger.GATE_ORDER}
        locked_section["evidence"] = [
            self.evidence(category, ai=category in merger.AI_GATES)
            for category in merger.GATE_ORDER
        ]
        first = self.write("dependency.json", dependency)
        second = self.write("locked.json", locked)
        with self.assertRaisesRegex(ValueError, "dependency is not internally locked"):
            merger.merge_and_validate([first, second], self.root, self.inventory)

    def test_unknown_handbook_unit_is_rejected(self) -> None:
        document = self.queued_section()
        document["section"]["handbook_unit_ids"] = ["HBU-unknown"]  # type: ignore[index]
        shard = self.write("unknown.json", document)
        with self.assertRaisesRegex(ValueError, "unknown handbook unit"):
            merger.merge_and_validate([shard], self.root, self.inventory)


if __name__ == "__main__":
    unittest.main()
