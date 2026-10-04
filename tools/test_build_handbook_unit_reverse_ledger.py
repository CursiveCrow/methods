#!/usr/bin/env python3
"""Adversarial tests for the exhaustive handbook-unit reverse ledger."""

from __future__ import annotations

import copy
import csv
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

import build_handbook_unit_reverse_ledger as ledger  # noqa: E402


def csv_raw(rows: list[dict[str, str]], fields: tuple[str, ...]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


class HandbookUnitReverseLedgerTests(unittest.TestCase):
    def make_fixture(
        self,
        root: Path,
        raw: bytes = b"% administrative\n\\newcommand{\\x}{x}\n\n",
        filename: str = "fixture.sty",
    ) -> tuple[Path, Path, Path, Path]:
        handbook = root / "handbook"
        handbook.mkdir(parents=True)
        source = handbook / filename
        source.write_bytes(raw)
        source_path = f"handbook/{filename}"
        snapshot_rows = [
            {
                "path": source_path,
                "bytes": str(len(raw)),
                "sha256": hashlib.sha256(raw).hexdigest(),
            }
        ]
        spec = root / "spec"
        provenance = spec / "provenance"
        provenance.mkdir(parents=True)
        snapshot = spec / "snapshot.csv"
        snapshot.write_bytes(csv_raw(snapshot_rows, ledger.SNAPSHOT_FIELDS))

        physical_rows = [
            {
                "record_id": "HB-F0001",
                "record_type": "file",
                "path": source_path,
                "line_number": "",
                "bytes": str(len(raw)),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "provenance_status": "open/unmapped",
                "source_authority_ids": "[]",
            }
        ]
        for line_number, line in enumerate(raw.splitlines(keepends=True), start=1):
            physical_rows.append(
                {
                    "record_id": f"HB-F0001-L{line_number:06d}",
                    "record_type": "physical_line",
                    "path": source_path,
                    "line_number": str(line_number),
                    "bytes": str(len(line)),
                    "sha256": hashlib.sha256(line).hexdigest(),
                    "provenance_status": "open/unmapped",
                    "source_authority_ids": "[]",
                }
            )
        physical = spec / "physical.csv"
        physical.write_bytes(csv_raw(physical_rows, ledger.PHYSICAL_FIELDS))
        register = spec / "register.csv"
        register.write_text("obligation_id\n", encoding="utf-8")
        return snapshot, physical, provenance / "reviewed.json", register

    def build(
        self, root: Path, snapshot: Path, physical: Path
    ) -> tuple[list[dict[str, str]], str, str]:
        snapshot_sha = hashlib.sha256(snapshot.read_bytes()).hexdigest()
        rows, observed_sha = ledger.build_inventory(
            snapshot, physical, root, snapshot_sha
        )
        self.assertEqual(observed_sha, snapshot_sha)
        inventory_sha = hashlib.sha256(
            ledger.csv_bytes(rows, ledger.INVENTORY_FIELDS)
        ).hexdigest()
        return rows, snapshot_sha, inventory_sha

    def evidence(self, root: Path) -> list[dict[str, object]]:
        result: list[dict[str, object]] = []
        authority = root / "handbook/fixture.sty"
        authority_hash = hashlib.sha256(authority.read_bytes()).hexdigest()
        for index, category in enumerate(ledger.VERIFICATION_FIELDS, start=1):
            path = root / "evidence" / f"{index}.txt"
            path.parent.mkdir(exist_ok=True)
            path.write_text(f"{category} evidence\n", encoding="utf-8")
            item: dict[str, object] = {
                    "category": category,
                    "recorded_result": "pass",
                    "artifact_path": f"evidence/{index}.txt",
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "producer_identity": f"reviewer {index}",
                    "recorded_scope": f"Recorded {category} check for fixture unit.",
                }
            if category in ledger.AI_REVIEW_FIELDS:
                item.update(
                    {
                        "model": f"fixture-model-{index}",
                        "model_version": "1",
                        "instructions": f"Review the fixture for {category}.",
                        "consulted_authorities": [
                            {
                                "path": "handbook/fixture.sty",
                                "locator": "complete file",
                                "sha256": authority_hash,
                            }
                        ],
                        "findings": ["No fixture defect found."],
                        "other_review_outputs_consulted": False,
                    }
                )
            result.append(item)
        return result

    def reviewed_record(self, row: dict[str, str], root: Path) -> dict[str, object]:
        record = ledger.record_identity(row)
        record.update(
            {
                "mapping_status": "mapped/reviewed",
                "semantic_review_status": "not-applicable",
                "source_authority_ids": [],
                "presentation_packet_ids": [],
                "register_obligation_ids": [],
                "verification": {category: "pass" for category in ledger.VERIFICATION_FIELDS},
                "verification_evidence": self.evidence(root),
            }
        )
        return record

    def write_review(
        self,
        path: Path,
        snapshot_sha: str,
        inventory_sha: str,
        records: list[dict[str, object]],
    ) -> None:
        path.write_text(
            json.dumps(
                {
                    "schema_version": ledger.SCHEMA_VERSION,
                    "construction_snapshot_sha256": snapshot_sha,
                    "handbook_unit_inventory_sha256": inventory_sha,
                    "records": records,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    def apply(
        self,
        rows: list[dict[str, str]],
        review: Path,
        snapshot_sha: str,
        inventory_sha: str,
        root: Path,
        register: Path,
    ) -> list[dict[str, str]]:
        return ledger.apply_reviewed_records(
            rows,
            review,
            snapshot_sha,
            inventory_sha,
            root,
            register,
            root / "spec/presentations",
        )

    def test_partition_is_exhaustive_and_output_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp:
            root = Path(raw_temp)
            snapshot, physical, _, _ = self.make_fixture(root)
            first, _, _ = self.build(root, snapshot, physical)
            second, _, _ = self.build(root, snapshot, physical)
        self.assertEqual(ledger.csv_bytes(first, ledger.INVENTORY_FIELDS), ledger.csv_bytes(second, ledger.INVENTORY_FIELDS))
        self.assertEqual([row["unit_kind"] for row in first], ["comment", "control", "blank"])

    def test_inherited_warning_body_has_named_owner(self) -> None:
        raw = (
            b"\\begin{warning}\n"
            b"Keep the source warning body.\n"
            b"\\end{warning}\n"
        )
        with tempfile.TemporaryDirectory() as raw_temp:
            root = Path(raw_temp)
            snapshot, physical, _, _ = self.make_fixture(root, raw, "fixture.tex")
            rows, _, _ = self.build(root, snapshot, physical)
        self.assertEqual([row["unit_kind"] for row in rows], ["warning", "control"])
        warning = rows[0]
        self.assertEqual(warning["start_line"], "1")
        self.assertEqual(warning["end_line"], "2")
        self.assertEqual(warning["parser_basis"], "recognized TeX environment warning")

    def test_partition_rejects_dropped_and_overlapped_lines(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp:
            root = Path(raw_temp)
            snapshot, physical, _, _ = self.make_fixture(root)
            rows, _, _ = self.build(root, snapshot, physical)
            files, _ = ledger.load_physical_files(snapshot, physical, root)
            dropped = [rows[0], rows[2]]
            with self.assertRaisesRegex(ValueError, "gap"):
                ledger.validate_partition(dropped, files)
            overlapped = copy.deepcopy(rows)
            overlapped[1]["start_line"] = "1"
            overlapped[1]["unit_id"] = ledger.unit_id_for(overlapped[1])
            with self.assertRaisesRegex(ValueError, "overlap"):
                ledger.validate_partition(overlapped, files)

    def test_stale_physical_line_digest_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp:
            root = Path(raw_temp)
            snapshot, physical, _, _ = self.make_fixture(root)
            with physical.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
            rows[1]["sha256"] = "0" * 64
            physical.write_bytes(csv_raw(rows, ledger.PHYSICAL_FIELDS))
            with self.assertRaisesRegex(ValueError, "physical inventory line row differs"):
                self.build(root, snapshot, physical)

    def test_unknown_and_duplicate_reviewed_unit_ids_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp:
            root = Path(raw_temp)
            snapshot, physical, review, register = self.make_fixture(root)
            rows, snapshot_sha, inventory_sha = self.build(root, snapshot, physical)
            record = self.reviewed_record(rows[0], root)
            unknown = copy.deepcopy(record)
            unknown["unit_id"] = "HBU-" + "0" * 24
            self.write_review(review, snapshot_sha, inventory_sha, [unknown])
            with self.assertRaisesRegex(ValueError, "unknown handbook unit ID"):
                self.apply(rows, review, snapshot_sha, inventory_sha, root, register)
            self.write_review(review, snapshot_sha, inventory_sha, [record, record])
            with self.assertRaisesRegex(ValueError, "duplicate handbook unit ID"):
                self.apply(rows, review, snapshot_sha, inventory_sha, root, register)

    def test_extra_and_missing_review_fields_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp:
            root = Path(raw_temp)
            snapshot, physical, review, register = self.make_fixture(root)
            rows, snapshot_sha, inventory_sha = self.build(root, snapshot, physical)
            extra = self.reviewed_record(rows[0], root)
            extra["invented"] = "value"
            self.write_review(review, snapshot_sha, inventory_sha, [extra])
            with self.assertRaisesRegex(ValueError, "unexpected"):
                self.apply(rows, review, snapshot_sha, inventory_sha, root, register)
            missing = self.reviewed_record(rows[0], root)
            del missing["parser_basis"]
            self.write_review(review, snapshot_sha, inventory_sha, [missing])
            with self.assertRaisesRegex(ValueError, "missing"):
                self.apply(rows, review, snapshot_sha, inventory_sha, root, register)

    def test_wrong_evidence_and_path_traversal_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp:
            root = Path(raw_temp)
            snapshot, physical, review, register = self.make_fixture(root)
            rows, snapshot_sha, inventory_sha = self.build(root, snapshot, physical)
            wrong = self.reviewed_record(rows[0], root)
            wrong["verification_evidence"][0]["recorded_result"] = "fail"  # type: ignore[index]
            self.write_review(review, snapshot_sha, inventory_sha, [wrong])
            with self.assertRaisesRegex(ValueError, "terminal pass"):
                self.apply(rows, review, snapshot_sha, inventory_sha, root, register)
            traversal = self.reviewed_record(rows[0], root)
            traversal["verification_evidence"][0]["artifact_path"] = "../escape.txt"  # type: ignore[index]
            self.write_review(review, snapshot_sha, inventory_sha, [traversal])
            with self.assertRaisesRegex(ValueError, "path traversal"):
                self.apply(rows, review, snapshot_sha, inventory_sha, root, register)

    def test_ai_review_metadata_and_isolation_are_required(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp:
            root = Path(raw_temp)
            snapshot, physical, review, register = self.make_fixture(root)
            rows, snapshot_sha, inventory_sha = self.build(root, snapshot, physical)
            missing = self.reviewed_record(rows[0], root)
            del missing["verification_evidence"][0]["model"]  # type: ignore[index]
            self.write_review(review, snapshot_sha, inventory_sha, [missing])
            with self.assertRaisesRegex(ValueError, "missing.*model"):
                self.apply(rows, review, snapshot_sha, inventory_sha, root, register)
            exposed = self.reviewed_record(rows[0], root)
            exposed["verification_evidence"][0][  # type: ignore[index]
                "other_review_outputs_consulted"
            ] = True
            self.write_review(review, snapshot_sha, inventory_sha, [exposed])
            with self.assertRaisesRegex(ValueError, "expected false"):
                self.apply(rows, review, snapshot_sha, inventory_sha, root, register)

    def test_write_then_check_and_terminal_nonreader_record(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp:
            root = Path(raw_temp)
            snapshot, physical, review, register = self.make_fixture(root)
            snapshot_sha = hashlib.sha256(snapshot.read_bytes()).hexdigest()
            paths = {
                "inventory_csv": root / "spec/unit.csv",
                "inventory_md": root / "spec/unit.md",
                "reverse_csv": root / "spec/reverse.csv",
                "reverse_md": root / "spec/reverse.md",
            }
            common = [
                "--repository-root", str(root),
                "--snapshot", str(snapshot),
                "--physical-inventory", str(physical),
                "--inventory-csv", str(paths["inventory_csv"]),
                "--inventory-markdown", str(paths["inventory_md"]),
                "--reverse-csv", str(paths["reverse_csv"]),
                "--reverse-markdown", str(paths["reverse_md"]),
                "--reviewed-records", str(review),
                "--register-manifest", str(register),
                "--presentation-root", str(root / "spec/presentations"),
                "--expected-snapshot-sha256", snapshot_sha,
            ]
            self.assertEqual(ledger.main(["--write", *common]), 0)
            rows, observed_snapshot_sha, inventory_sha = self.build(root, snapshot, physical)
            record = self.reviewed_record(rows[0], root)
            self.write_review(review, observed_snapshot_sha, inventory_sha, [record])
            self.assertEqual(ledger.main(["--write", *common]), 0)
            self.assertEqual(ledger.main(["--check", *common]), 0)
            with paths["reverse_csv"].open(encoding="utf-8", newline="") as handle:
                reverse = list(csv.DictReader(handle))
            self.assertEqual(reverse[0]["mapping_status"], "mapped/reviewed")
            self.assertEqual(reverse[0]["semantic_review_status"], "not-applicable")


if __name__ == "__main__":
    unittest.main()
