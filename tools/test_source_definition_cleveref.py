#!/usr/bin/env python3
"""Rendered public-seam tests for inherited definition references."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK_TEX = ROOT / "handbook"
THEORY_SOURCE = HANDBOOK_TEX / "restoration" / "inherited-03729-03907.tex"
CARDINALITY_SOURCE = HANDBOOK_TEX / "restoration" / "inherited-05043-05131.tex"
PDFLATEX = shutil.which("pdflatex")
PDFTOTEXT = shutil.which("pdftotext")


def exact_source_fixture_body() -> str:
    theory = THEORY_SOURCE.read_text(encoding="utf-8")
    definitions = re.findall(
        r"\\begin\{definition\}.*?\\end\{definition\}", theory, re.DOTALL
    )
    if len(definitions) < 2:
        raise AssertionError("the restored theories artifact must retain two definitions")
    first_definition = definitions[0]
    if r"\label{def:fol-theory-satisfiability}" not in first_definition:
        raise AssertionError("the real source definition label is absent")

    second_definition = definitions[1].replace(
        r"\begin{definition}[Axiomatization]",
        r"\begin{definition}[Axiomatization]"
        "\n"
        r"\label{def:fixture-axiomatization}",
        1,
    )
    if r"\label{def:fixture-axiomatization}" not in second_definition:
        raise AssertionError("the second definition fixture label was not inserted")

    real_reference_line = next(
        (
            line.strip()
            for line in CARDINALITY_SOURCE.read_text(encoding="utf-8").splitlines()
            if r"\cref{def:fol-theory-satisfiability}" in line
        ),
        "",
    )
    if real_reference_line != (
        r"defined in \cref{def:fol-theory-satisfiability}."
    ):
        raise AssertionError("restored source line 5124 is not exact")

    return (
        r"\begin{inheritedrestorationscope}{SRC-03729-03907}"
        "\n"
        + first_definition
        + "\n"
        + second_definition
        + "\n"
        + r"\begin{theorem}[Fixture theorem]"
        + "\n"
        + r"\label{thm:fixture-source}A source theorem."
        + "\n"
        + r"\end{theorem}"
        + "\n"
        + r"\begin{lemma}[Fixture lemma]"
        + "\n"
        + r"\label{lem:fixture-source}A source lemma."
        + "\n"
        + r"\end{lemma}"
        + "\n"
        + r"\begin{corollary}[Fixture corollary]"
        + "\n"
        + r"\label{cor:fixture-source}A source corollary."
        + "\n"
        + r"\end{corollary}"
        + "\n"
        + "REAL-LINE: "
        + real_reference_line
        + "\n"
        + r"DEF-LOWER: \cref{def:fol-theory-satisfiability,def:fixture-axiomatization}."
        + "\n"
        + r"DEF-UPPER: \Cref{def:fol-theory-satisfiability,def:fixture-axiomatization}."
        + "\n"
        + r"RESULTS: \cref{thm:fixture-source,lem:fixture-source,cor:fixture-source}."
        + "\n"
        + r"\end{inheritedrestorationscope}"
        + "\n"
        + r"\begin{hbdefinition}{def:fixture-editorial}{Editorial fixture}"
        + "\n"
        + "An editorial item after the source environment."
        + "\n"
        + r"\end{hbdefinition}"
        + "\n"
    )


def fixture_document(body: str) -> str:
    return (
        r"\documentclass[11pt]{book}"
        "\n"
        + r"\usepackage{handbook}"
        + "\n"
        + r"\begin{document}"
        + "\n"
        + r"\chapter{Cleveref fixture}"
        + "\n"
        + body
        + r"\end{document}"
        + "\n"
    )


@unittest.skipUnless(
    PDFLATEX and PDFTOTEXT,
    "pdflatex and pdftotext are required for inherited-definition tests",
)
class SourceDefinitionCleverefTests(unittest.TestCase):
    def compile(
        self, body: str, *, runs: int
    ) -> tuple[subprocess.CompletedProcess[str], Path]:
        temporary = tempfile.TemporaryDirectory(prefix="source-definition-cref-")
        self.addCleanup(temporary.cleanup)
        build = Path(temporary.name)
        (build / "fixture.tex").write_text(
            fixture_document(body), encoding="utf-8", newline="\n"
        )
        env = os.environ.copy()
        env["TEXINPUTS"] = str(HANDBOOK_TEX) + os.pathsep
        completed: subprocess.CompletedProcess[str] | None = None
        for _ in range(runs):
            completed = subprocess.run(
                [
                    str(PDFLATEX),
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "fixture.tex",
                ],
                cwd=build,
                env=env,
                text=True,
                capture_output=True,
                timeout=120,
            )
            if completed.returncode != 0:
                break
        assert completed is not None
        return completed, build

    def test_real_definition_crefs_are_named_numbered_and_scope_local(self) -> None:
        result, build = self.compile(exact_source_fixture_body(), runs=3)
        output = result.stdout + result.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(result.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)
        self.assertNotIn("reference format for label type", output)
        self.assertNotIn("There were undefined references", output)
        self.assertNotIn("Rerun to get cross-references right", output)

        extracted = subprocess.run(
            [str(PDFTOTEXT), "-layout", "fixture.pdf", "-"],
            cwd=build,
            text=True,
            capture_output=True,
            timeout=60,
        )
        self.assertEqual(
            extracted.returncode, 0, extracted.stdout + extracted.stderr
        )
        rendered = " ".join(extracted.stdout.split())
        self.assertNotIn("??", rendered)
        self.assertIn("REAL-LINE: defined in definition 1.1.", rendered)
        self.assertIn("DEF-LOWER: definitions 1.1 and 1.2.", rendered)
        self.assertIn("DEF-UPPER: Definitions 1.1 and 1.2.", rendered)
        self.assertIn(
            "RESULTS: theorem 1.3, lemma 1.4, and corollary 1.5.", rendered
        )

        aux = (build / "fixture.aux").read_text(
            encoding="utf-8", errors="replace"
        )
        self.assertRegex(
            aux,
            r"def:fol-theory-satisfiability@cref\}\{\{\[definition\]",
        )
        self.assertRegex(aux, r"thm:fixture-source@cref\}\{\{\[hbsourcetheorem\]")
        self.assertRegex(aux, r"lem:fixture-source@cref\}\{\{\[hbsourcelemma\]")
        self.assertRegex(aux, r"cor:fixture-source@cref\}\{\{\[hbsourcecorollary\]")
        self.assertRegex(aux, r"def:fixture-editorial@cref\}\{\{\[hbitem\]")
        self.assertNotRegex(
            aux, r"def:fixture-editorial@cref\}\{\{\[definition\]"
        )

    def test_source_definition_still_fails_outside_restoration_scope(self) -> None:
        result, _ = self.compile(
            r"\begin{definition}[Outside]Not source-scoped.\end{definition}",
            runs=1,
        )
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn("source definition environment outside", output)


if __name__ == "__main__":
    unittest.main()
