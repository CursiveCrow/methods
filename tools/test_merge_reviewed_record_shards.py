#!/usr/bin/env python3
"""CLI tests for deterministic reviewed-record document merging."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools import merge_reviewed_record_shards as merge_tool


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "merge_reviewed_record_shards.py"


class ReviewedRecordShardMergeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="reviewed-record-merge-")
        self.base = Path(self.temporary.name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_json(self, name: str, value: object) -> Path:
        path = self.base / name
        path.write_text(
            json.dumps(value, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return path

    def run_tool(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(TOOL), *arguments],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def source_document(self) -> dict[str, object]:
        return json.loads(
            (ROOT / "spec/provenance/reviewed-source-unit-records.json").read_text(
                encoding="utf-8"
            )
        )

    def committed_document(self, name: str) -> dict[str, object]:
        return json.loads(
            (ROOT / f"spec/provenance/{name}").read_text(encoding="utf-8")
        )

    def test_source_unit_shards_merge_in_canonical_ordinal_order(self) -> None:
        document = self.source_document()
        records = list(document["records"])
        self.assertGreaterEqual(len(records), 2)
        left = dict(document, records=records[::2])
        right = dict(document, records=records[1::2])
        left_path = self.write_json("left.json", left)
        right_path = self.write_json("right.json", right)
        output = self.base / "merged.json"

        result = self.run_tool(
            "--kind",
            "source-unit",
            "--input",
            str(right_path),
            "--input",
            str(left_path),
            "--output",
            str(output),
            "--write",
            "--repository-root",
            str(ROOT),
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        merged = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(
            [record["unit_ordinal"] for record in merged["records"]],
            sorted(record["unit_ordinal"] for record in records),
        )
        self.assertEqual(set(merged), set(document))

        check = self.run_tool(
            "--kind",
            "source-unit",
            "--input",
            str(left_path),
            "--input",
            str(right_path),
            "--output",
            str(output),
            "--check",
            "--repository-root",
            str(ROOT),
        )
        self.assertEqual(check.returncode, 0, check.stderr)

    def test_duplicate_record_identity_is_rejected_across_shards(self) -> None:
        document = self.source_document()
        record = list(document["records"])[0]
        first = self.write_json("first.json", dict(document, records=[record]))
        second = self.write_json("second.json", dict(document, records=[record]))

        result = self.run_tool(
            "--kind",
            "source-unit",
            "--input",
            str(first),
            "--input",
            str(second),
            "--output",
            str(self.base / "merged.json"),
            "--write",
            "--repository-root",
            str(ROOT),
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate unit_ordinal", result.stderr)

    def test_divergent_document_pin_is_rejected(self) -> None:
        document = self.source_document()
        changed = copy.deepcopy(document)
        changed["authority_sha256"] = "0" * 64
        first = self.write_json("first.json", dict(document, records=[]))
        second = self.write_json("second.json", dict(changed, records=[]))

        result = self.run_tool(
            "--kind",
            "source-unit",
            "--input",
            str(first),
            "--input",
            str(second),
            "--output",
            str(self.base / "merged.json"),
            "--write",
            "--repository-root",
            str(ROOT),
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("document pins differ", result.stderr)

    def test_unknown_source_unit_is_rejected_by_domain_validation(self) -> None:
        document = self.source_document()
        record = copy.deepcopy(list(document["records"])[0])
        record["unit_ordinal"] = 99_999
        shard = self.write_json("unknown.json", dict(document, records=[record]))

        result = self.run_tool(
            "--kind",
            "source-unit",
            "--input",
            str(shard),
            "--output",
            str(self.base / "merged.json"),
            "--write",
            "--repository-root",
            str(ROOT),
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown unit ordinal", result.stderr)

    def test_check_detects_stale_output_bytes(self) -> None:
        document = self.source_document()
        shard = self.write_json("source.json", document)
        output = self.base / "merged.json"
        output.write_text("{}\n", encoding="utf-8")

        result = self.run_tool(
            "--kind",
            "source-unit",
            "--input",
            str(shard),
            "--output",
            str(output),
            "--check",
            "--repository-root",
            str(ROOT),
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("stale merged output", result.stderr)

    def test_handbook_and_register_shards_validate_end_to_end(self) -> None:
        cases = (
            ("handbook-unit", "reviewed-handbook-unit-records.json"),
            ("register-obligation", "reviewed-register-obligation-records.json"),
        )
        for kind, filename in cases:
            with self.subTest(kind=kind):
                document = self.committed_document(filename)
                self.assertEqual(document["records"], [])
                shard = self.write_json(f"{kind}.json", document)
                output = self.base / f"{kind}-merged.json"
                result = self.run_tool(
                    "--kind",
                    kind,
                    "--input",
                    str(shard),
                    "--output",
                    str(output),
                    "--write",
                    "--repository-root",
                    str(ROOT),
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                expected = (
                    json.dumps(document, ensure_ascii=False, indent=2) + "\n"
                ).encode("utf-8")
                self.assertEqual(output.read_bytes(), expected)

    def test_register_contract_supersession_collection_is_a_single_immutable_pin(self) -> None:
        document = self.committed_document(
            "reviewed-register-obligation-records.json"
        )
        pinned = [{"supersession_id": "validated-base-record"}]
        first_value = dict(document, records=[], contract_supersessions=pinned)
        second_value = copy.deepcopy(first_value)
        first = self.write_json("register-first.json", first_value)
        second = self.write_json("register-second.json", second_value)
        merged = merge_tool.merge_documents(
            [first, second], "register-obligation"
        )
        self.assertEqual(merged["contract_supersessions"], pinned)

        changed = copy.deepcopy(second_value)
        changed["contract_supersessions"] = []
        changed_path = self.write_json("register-changed.json", changed)
        with self.assertRaisesRegex(ValueError, "contract_supersessions.*must not modify"):
            merge_tool.merge_documents(
                [first, changed_path], "register-obligation"
            )

        too_many = dict(
            document,
            records=[],
            contract_supersessions=[
                {"supersession_id": "first"},
                {"supersession_id": "second"},
            ],
        )
        too_many_path = self.write_json("register-too-many.json", too_many)
        with self.assertRaisesRegex(ValueError, "empty or single-item"):
            merge_tool.merge_documents([too_many_path], "register-obligation")

    def test_register_shards_cannot_complete_reserved_supersession_rows(self) -> None:
        document = self.committed_document(
            "reviewed-register-obligation-records.json"
        )
        for obligation_id in (
            "OBL::defects::S-002",
            "OBL::defects::S-003",
            "OBL::apparatus::A-167",
            "OBL::apparatus::A-168",
        ):
            with self.subTest(obligation_id=obligation_id):
                shard = self.write_json(
                    "register-reserved.json",
                    dict(document, records=[{"obligation_id": obligation_id}]),
                )
                with self.assertRaisesRegex(ValueError, "reserved.*contract_supersessions"):
                    merge_tool.merge_documents([shard], "register-obligation")


if __name__ == "__main__":
    unittest.main()
