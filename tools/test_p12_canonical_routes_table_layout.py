#!/usr/bin/env python3
"""Rendered public-seam test for the first row of Table 68.2."""

from __future__ import annotations

import html
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK_TEX = ROOT / "handbook"
SOURCE = HANDBOOK_TEX / "parts" / "p12" / "further-reading.tex"
PDFLATEX = shutil.which("pdflatex")
PDFTOTEXT = shutil.which("pdftotext")
MINIMUM_COLUMN_GAP_PT = 2.0


@dataclass(frozen=True)
class WordBox:
    text: str
    x_min: float
    y_min: float
    x_max: float
    y_max: float


WORD_RE = re.compile(
    r'<word xMin="(?P<x_min>[0-9.]+)" yMin="(?P<y_min>[0-9.]+)" '
    r'xMax="(?P<x_max>[0-9.]+)" yMax="(?P<y_max>[0-9.]+)">'
    r"(?P<text>.*?)</word>"
)


def governed_row(*, legacy_unbreakable_mutation: bool) -> str:
    source = SOURCE.read_text(encoding="utf-8")
    match = re.search(
        r"(?ms)^Equisatisfiability/(?:\\allowbreak )?Tseitin &\n.*?\\\\ \\addlinespace$",
        source,
    )
    if match is None:
        raise AssertionError("Table 68.2 governed row is absent")
    row = match.group(0)
    if legacy_unbreakable_mutation:
        row = row.replace(r"/\allowbreak ", "/")
    return row


def fixture_document(*, legacy_unbreakable_mutation: bool) -> str:
    return (
        r"\documentclass[11pt]{book}"
        "\n"
        r"\usepackage{handbook}"
        "\n"
        r"\begin{document}"
        "\n"
        r"\begin{longtable}{@{}p{.25\textwidth}p{.31\textwidth}p{.34\textwidth}@{}}"
        "\n"
        r"P12 use & Canonical destination & Boundary \\ \midrule"
        "\n"
        + governed_row(legacy_unbreakable_mutation=legacy_unbreakable_mutation)
        + "\n"
        + r"\bottomrule"
        "\n"
        r"\end{longtable}"
        "\n"
        r"\end{document}"
        "\n"
    )


def parse_word_boxes(path: Path) -> list[WordBox]:
    boxes: list[WordBox] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = WORD_RE.search(line)
        if match is None:
            continue
        boxes.append(
            WordBox(
                text=html.unescape(match.group("text")),
                x_min=float(match.group("x_min")),
                y_min=float(match.group("y_min")),
                x_max=float(match.group("x_max")),
                y_max=float(match.group("y_max")),
            )
        )
    return boxes


def first_row_gap(boxes: list[WordBox]) -> float:
    first_column = [box for box in boxes if "Equisatisfiability" in box.text]
    second_column = [box for box in boxes if box.text == "OPEN:"]
    if len(first_column) != 1 or len(second_column) != 1:
        return float("-inf")
    left = first_column[0]
    right = second_column[0]
    if abs((left.y_min + left.y_max) - (right.y_min + right.y_max)) > 3.0:
        return float("-inf")
    return right.x_min - left.x_max


@unittest.skipUnless(
    PDFLATEX and PDFTOTEXT,
    "pdflatex and pdftotext are required for rendered table tests",
)
class CanonicalRoutesTableLayoutTests(unittest.TestCase):
    def compile_row(self, *, legacy_unbreakable_mutation: bool) -> list[WordBox]:
        temporary = tempfile.TemporaryDirectory(prefix="canonical-routes-row-")
        self.addCleanup(temporary.cleanup)
        build = Path(temporary.name)
        (build / "fixture.tex").write_text(
            fixture_document(
                legacy_unbreakable_mutation=legacy_unbreakable_mutation
            ),
            encoding="utf-8",
            newline="\n",
        )
        env = os.environ.copy()
        env["TEXINPUTS"] = str(HANDBOOK_TEX) + os.pathsep
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
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        bbox = build / "fixture-bbox.html"
        extracted = subprocess.run(
            [str(PDFTOTEXT), "-bbox", "fixture.pdf", bbox.name],
            cwd=build,
            text=True,
            capture_output=True,
            timeout=60,
        )
        self.assertEqual(
            extracted.returncode, 0, extracted.stdout + extracted.stderr
        )
        return parse_word_boxes(bbox)

    def test_first_row_leaves_a_visible_intercolumn_gap(self) -> None:
        boxes = self.compile_row(legacy_unbreakable_mutation=False)
        self.assertGreaterEqual(
            first_row_gap(boxes),
            MINIMUM_COLUMN_GAP_PT,
            "Equisatisfiability/Tseitin must not collide with the OPEN cell",
        )

    def test_oracle_rejects_the_unbreakable_legacy_row(self) -> None:
        boxes = self.compile_row(legacy_unbreakable_mutation=True)
        self.assertLess(
            first_row_gap(boxes),
            MINIMUM_COLUMN_GAP_PT,
            "the previously rendered cross-column collision must fail closed",
        )


if __name__ == "__main__":
    unittest.main()
