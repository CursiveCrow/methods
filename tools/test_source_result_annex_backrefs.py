#!/usr/bin/env python3
"""Focused structural tests for annex links to exact inherited results."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools/check.py"
PROVENANCE_ID = "SRC-07295-07468"
WRAPPER = f"restoration/scope-{PROVENANCE_ID}"
ARTIFACT = "restoration/inherited-07295-07468"


class SourceResultAnnexBackrefTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for relative in (
            "source/formal-logic-reference.tex",
            "spec/inherited-corpus-manifest.json",
            "spec/inherited-source-map.csv",
            "spec/source-unit-inventory.csv",
            f"spec/provenance/{PROVENANCE_ID}.json",
            f"handbook/{WRAPPER}.tex",
            f"handbook/{ARTIFACT}.tex",
            "handbook/bib/handbook.bib",
        ):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, target)
        symbols = self.root / "handbook/registry/symbols.csv"
        symbols.parent.mkdir(parents=True, exist_ok=True)
        symbols.write_text(
            "glyph,macro,role,scope,precedence,first_use,notes\n",
            encoding="utf-8",
            newline="\n",
        )
        annex = self.root / "handbook/annex/p03/open-qe.tex"
        annex.parent.mkdir(parents=True, exist_ok=True)
        annex.write_text(
            r"\begin{annexitem}{annex:p3.qe.fixture}{thm:dlo-countable-categorical}{Exact source result}"
            + "\n"
            + r"Structural support only."
            + "\n"
            + r"\end{annexitem}"
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.main = self.root / "handbook/main.tex"
        self.main.write_text(
            r"\label{def:homogeneity}" + "\n"
            + r"\label{def:theory-completeness}" + "\n"
            + r"\label{thm:saturation-homogeneity}" + "\n"
            + rf"\input{{{WRAPPER}}}" + "\n"
            + r"\input{annex/p03/open-qe}" + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def run_check(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(CHECK),
                "--tree",
                "handbook",
                "--strict",
                "--root",
                str(self.root),
            ],
            text=True,
            capture_output=True,
            timeout=120,
        )

    def assert_fails_with(self, *needles: str) -> None:
        completed = self.run_check()
        output = completed.stdout + completed.stderr
        self.assertNotEqual(completed.returncode, 0, output)
        for needle in needles:
            self.assertIn(needle, output)

    def test_reachable_validated_source_theorem_is_a_structural_backref_target(self) -> None:
        completed = self.run_check()
        self.assertEqual(
            completed.returncode,
            0,
            completed.stdout + completed.stderr,
        )

    def test_unreachable_wrapper_cannot_authorize_source_result_recognition(self) -> None:
        self.main.write_text(
            self.main.read_text(encoding="utf-8").replace(
                rf"\input{{{WRAPPER}}}" + "\n", ""
            ),
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "validated scope wrapper is not reachable exactly once",
            "does not resolve to a body result",
        )

    def test_direct_unvalidated_artifact_path_cannot_authorize_recognition(self) -> None:
        self.main.write_text(
            self.main.read_text(encoding="utf-8").replace(WRAPPER, ARTIFACT),
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "included outside its validated scope wrapper",
            "does not resolve to a body result",
        )

    def test_duplicate_source_result_label_still_fails_closed(self) -> None:
        with self.main.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(r"\label{thm:dlo-countable-categorical}" + "\n")
        self.assert_fails_with("duplicate-label")

    def test_nonresult_environment_label_is_not_structurally_recognized(self) -> None:
        annex = self.root / "handbook/annex/p03/open-qe.tex"
        annex.write_text(
            annex.read_text(encoding="utf-8").replace(
                "thm:dlo-countable-categorical", "def:theory-completeness"
            ),
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "backref 'def:theory-completeness' must be",
            "does not resolve to a body result",
        )


if __name__ == "__main__":
    unittest.main()
