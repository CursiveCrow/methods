#!/usr/bin/env python3
"""Adversarial CLI tests for exact inherited forward-reference admission."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools" / "check.py"
PROVENANCE_ID = "SRC-00853-00906"
ARTIFACT_REL = "restoration/inherited-00853-00906.tex"
TARGET = "ch:prop-syntax-semantics"


class PendingInheritedReferenceCliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for relative in (
            "source/formal-logic-reference.tex",
            "spec/inherited-corpus-manifest.json",
            "spec/inherited-source-map.csv",
            "spec/source-unit-inventory.csv",
        ):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, target)
        for directory in (
            "handbook/restoration",
            "handbook/registry",
            "handbook/bib",
            "spec/provenance",
        ):
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        (self.root / "handbook/registry/symbols.csv").write_text(
            "glyph,macro,role,scope,precedence,first_use,notes\n",
            encoding="utf-8",
            newline="\n",
        )
        (self.root / "handbook/bib/handbook.bib").write_text(
            "@book{Tarski1983, author={Tarski}, title={Logic}, year={1983}}\n",
            encoding="utf-8",
            newline="\n",
        )
        self._make_exact_record()
        (self.root / f"handbook/restoration/scope-{PROVENANCE_ID}.tex").write_text(
            rf"\begin{{inheritedrestorationscope}}{{{PROVENANCE_ID}}}" + "\n"
            + rf"\input{{{ARTIFACT_REL.removesuffix('.tex')}}}" + "\n"
            + r"\end{inheritedrestorationscope}" + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (self.root / "handbook/main.tex").write_text(
            rf"\input{{restoration/scope-{PROVENANCE_ID}}}" + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def _make_exact_record(self) -> None:
        source_lines = (self.root / "source/formal-logic-reference.tex").read_bytes().splitlines(
            keepends=True
        )
        source_interval = source_lines[852:906]
        artifact = b"".join(line.rstrip(b"\r\n") + b"\n" for line in source_interval)
        artifact_path = self.root / "handbook" / ARTIFACT_REL
        artifact_path.write_bytes(artifact)

        template = json.loads(
            (ROOT / "spec/provenance/SRC-00790-00797.json").read_text(encoding="utf-8")
        )
        template["provenance_id"] = PROVENANCE_ID
        template["source_locator"] = {
            "start_line": 853,
            "end_line": 906,
            "line_count": 54,
            "interval_sha256": hashlib.sha256(b"".join(source_interval)).hexdigest(),
        }
        template["source_unit_evidence"]["unit_ordinals"] = list(range(60, 65))
        template["presentation_identity"] = {
            "kind": "source interval",
            "source_title": "Object language and metalanguage",
            "description": "Exact inclusive source interval 853--906.",
        }
        template["restoration_artifact"].update(
            {
                "path": f"handbook/{ARTIFACT_REL}",
                "bytes": len(artifact),
                "physical_lines": 54,
                "sha256": hashlib.sha256(artifact).hexdigest(),
                "content_token_sha256": hashlib.sha256(artifact).hexdigest(),
            }
        )
        template["handbook_destination"]["file"] = f"handbook/{ARTIFACT_REL}"
        template["audit_evidence"] = {
            "source_map": "spec/inherited-source-map.csv",
            "interval_ids": [PROVENANCE_ID],
            "classifications": ["altered", "abridged"],
        }
        for item in template["verification_evidence"]:
            item["command"] = (
                "python tools/check_inherited_restoration.py --record "
                f"spec/provenance/{PROVENANCE_ID}.json"
            )
        (self.root / f"spec/provenance/{PROVENANCE_ID}.json").write_text(
            json.dumps(template, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def run_check(self, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(CHECK),
                "--tree",
                "handbook",
                "--strict",
                "--root",
                str(self.root),
                *extra,
            ],
            text=True,
            capture_output=True,
            timeout=60,
        )

    def inventory_rows(self) -> tuple[list[str], list[dict[str, str]]]:
        path = self.root / "spec/source-unit-inventory.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            return list(reader.fieldnames or []), list(reader)

    def write_inventory(self, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
        path = self.root / "spec/source-unit-inventory.csv"
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    def test_exact_later_inventory_target_is_pending_by_default(self) -> None:
        result = self.run_check()
        output = result.stdout + result.stderr
        self.assertEqual(result.returncode, 0, output)
        self.assertIn("pending inherited references: 1", output)
        self.assertIn(TARGET, output)

    def test_terminal_option_rejects_even_an_authorized_pending_reference(self) -> None:
        result = self.run_check("--require-no-pending-inherited-refs")
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn("pending inherited reference", output)
        self.assertIn(TARGET, output)

    def test_unknown_target_in_exact_artifact_remains_dangling(self) -> None:
        fieldnames, rows = self.inventory_rows()
        for row in rows:
            if row["label"] == TARGET:
                row["label"] = ""
        self.write_inventory(fieldnames, rows)
        result = self.run_check()
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn(f"dangling-ref: {TARGET}", output)
        self.assertIn("pending inherited references: 0", output)

    def test_backward_missing_target_in_exact_artifact_remains_dangling(self) -> None:
        fieldnames, rows = self.inventory_rows()
        for row in rows:
            if row["label"] == TARGET:
                row["start_line"] = "700"
                row["end_line"] = "700"
        self.write_inventory(fieldnames, rows)
        result = self.run_check()
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn(f"dangling-ref: {TARGET}", output)
        self.assertIn("pending inherited references: 0", output)

    def test_editorial_reference_to_later_inventory_target_remains_dangling(self) -> None:
        editorial = self.root / "handbook/parts/p01/editorial.tex"
        editorial.parent.mkdir(parents=True)
        editorial.write_text(rf"Editorial \cref{{{TARGET}}}." + "\n", encoding="utf-8")
        result = self.run_check()
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn(f"dangling-ref: {TARGET} (parts/p01/editorial.tex", output)

    def test_unprovenanced_restoration_reference_remains_dangling(self) -> None:
        artifact = self.root / "handbook/restoration/inherited-09998-09999.tex"
        artifact.write_text(rf"Unprovenanced \cref{{{TARGET}}}." + "\n", encoding="utf-8")
        with (self.root / "handbook/main.tex").open("a", encoding="utf-8") as handle:
            handle.write(r"\input{restoration/inherited-09998-09999}" + "\n")
        result = self.run_check()
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn(f"dangling-ref: {TARGET} (restoration/inherited-09998-09999.tex", output)

    def test_live_route_has_no_pending_reference_after_exact_target_restoration(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHECK), "--tree", "handbook", "--strict"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=60,
        )
        output = result.stdout + result.stderr
        self.assertEqual(result.returncode, 0, output)
        self.assertIn("pending inherited references: 0", output)
        pending = [
            line for line in output.splitlines()
            if line.startswith("[pending] inherited reference:")
        ]
        self.assertEqual(pending, [])
        self.assertNotIn("[pending] inherited reference: ch:fol-theories", output)
        self.assertNotIn("[pending] inherited reference: ch:fol-deduction", output)
        self.assertNotIn("[pending] inherited reference: lem:reduct-invariance", output)
        self.assertNotIn("[pending] inherited reference: thm:fol-soundness", output)
        self.assertNotIn("[pending] inherited reference: thm:fol-completeness", output)


if __name__ == "__main__":
    unittest.main()
