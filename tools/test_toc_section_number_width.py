#!/usr/bin/env python3
"""Rendered public-seam tests for both edges of section rows in the TOC."""

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
PDFLATEX = shutil.which("pdflatex")
PDFTOTEXT = shutil.which("pdftotext")
MINIMUM_NUMBER_TITLE_GAP_PT = 4.0
MINIMUM_TITLE_FOLIO_GAP_PT = 4.0


@dataclass(frozen=True)
class WordBox:
    page: int
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


def fixture_document(*, standard_section_width_mutation: bool = False) -> str:
    mutation = ""
    if standard_section_width_mutation:
        mutation = (
            r"\makeatletter"
            r"\renewcommand*\l@section{\@dottedtocline{1}{1.5em}{2.3em}}"
            r"\makeatother"
            "\n"
        )
    return (
        r"\documentclass[11pt]{book}"
        "\n"
        r"\usepackage{handbook}"
        "\n"
        + mutation
        + r"\begin{document}"
        "\n"
        + r"\frontmatter"
        "\n"
        + r"\tableofcontents"
        "\n"
        + r"\mainmatter"
        "\n"
        + r"\setcounter{part}{11}"
        "\n"
        + r"\part{AutomationPart}"
        "\n"
        + r"\setcounter{chapter}{11}"
        "\n"
        + r"\chapter{AutomationChapter}"
        "\n"
        + r"\setcounter{section}{9}"
        "\n"
        + r"\section{WideTen}"
        "\n"
        + r"\section{WideEleven}"
        "\n"
        + r"\setcounter{page}{613}"
        "\n"
        + r"\section{What the conflict-analysis apparatus does and does not supply}"
        "\n"
        + r"\subsection{NarrowSubsection}"
        "\n"
        + r"\end{document}"
        "\n"
    )


def parse_word_boxes(path: Path) -> list[WordBox]:
    source = path.read_text(encoding="utf-8", errors="replace")
    boxes: list[WordBox] = []
    page = -1
    for line in source.splitlines():
        if "<page " in line:
            page += 1
        match = WORD_RE.search(line)
        if match is None:
            continue
        boxes.append(
            WordBox(
                page=page,
                text=html.unescape(match.group("text")),
                x_min=float(match.group("x_min")),
                y_min=float(match.group("y_min")),
                x_max=float(match.group("x_max")),
                y_max=float(match.group("y_max")),
            )
        )
    return boxes


def number_title_gap(boxes: list[WordBox], number: str, title: str) -> float:
    # The fixture's table of contents is the first rendered page.  Restricting
    # the oracle to that page also makes a fused number/title token fail closed
    # instead of accidentally measuring the later body heading.
    title_boxes = [box for box in boxes if box.text == title and box.page == 0]
    if not title_boxes:
        return float("-inf")
    title_box = min(title_boxes, key=lambda box: (box.page, box.y_min, box.x_min))
    number_boxes = [
        box
        for box in boxes
        if box.text == number
        and box.page == title_box.page
        and abs((box.y_min + box.y_max) - (title_box.y_min + title_box.y_max)) < 2.0
    ]
    if not number_boxes:
        return float("-inf")
    number_box = min(number_boxes, key=lambda box: abs(box.x_max - title_box.x_min))
    return title_box.x_min - number_box.x_max


def first_toc_word(boxes: list[WordBox], text: str) -> WordBox:
    matches = [box for box in boxes if box.text == text and box.page == 0]
    if not matches:
        raise AssertionError(f"table-of-contents word is absent: {text}")
    return min(matches, key=lambda box: (box.y_min, box.x_min))


def title_folio_gap(boxes: list[WordBox], title_word: str, folio: str) -> float:
    title_boxes = [
        box for box in boxes if box.text == title_word and box.page == 0
    ]
    if not title_boxes:
        return float("-inf")
    gaps: list[float] = []
    for title_box in title_boxes:
        for folio_box in boxes:
            if (
                folio_box.text == folio
                and folio_box.page == title_box.page
                and abs(
                    (folio_box.y_min + folio_box.y_max)
                    - (title_box.y_min + title_box.y_max)
                )
                < 2.0
            ):
                gaps.append(folio_box.x_min - title_box.x_max)
    return min(gaps) if gaps else float("-inf")


@unittest.skipUnless(
    PDFLATEX and PDFTOTEXT,
    "pdflatex and pdftotext are required for rendered TOC tests",
)
class TocSectionNumberWidthTests(unittest.TestCase):
    def compile_toc(self, *, standard_section_width_mutation: bool = False) -> list[WordBox]:
        temporary = tempfile.TemporaryDirectory(prefix="toc-section-width-")
        self.addCleanup(temporary.cleanup)
        build = Path(temporary.name)
        (build / "fixture.tex").write_text(
            fixture_document(
                standard_section_width_mutation=standard_section_width_mutation
            ),
            encoding="utf-8",
            newline="\n",
        )
        env = os.environ.copy()
        env["TEXINPUTS"] = str(HANDBOOK_TEX) + os.pathsep
        completed: subprocess.CompletedProcess[str] | None = None
        for _ in range(3):
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
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Rerun to get cross-references right", output)
        self.assertNotIn("Label(s) may have changed", output)
        self.assertNotIn(r"Overfull \hbox", output)

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

    def test_multidigit_section_numbers_leave_a_readable_gap_before_titles(self) -> None:
        boxes = self.compile_toc()
        for number, title in (("12.10", "WideTen"), ("12.11", "WideEleven")):
            with self.subTest(number=number):
                self.assertGreaterEqual(
                    number_title_gap(boxes, number, title),
                    MINIMUM_NUMBER_TITLE_GAP_PT,
                    f"{number} must leave at least a readable interword gap before {title}",
                )

    def test_long_section_title_leaves_a_readable_gap_before_three_digit_folio(self) -> None:
        boxes = self.compile_toc()
        self.assertGreaterEqual(
            title_folio_gap(boxes, "ply", "613"),
            MINIMUM_TITLE_FOLIO_GAP_PT,
            "the final title word must remain separated from its three-digit folio",
        )

    def test_oracle_rejects_the_standard_insufficient_section_width(self) -> None:
        production_boxes = self.compile_toc()
        boxes = self.compile_toc(standard_section_width_mutation=True)
        gaps = [
            number_title_gap(boxes, "12.10", "WideTen"),
            number_title_gap(boxes, "12.11", "WideEleven"),
        ]
        self.assertTrue(
            any(gap < MINIMUM_NUMBER_TITLE_GAP_PT for gap in gaps),
            f"the mutation must be detected, but rendered gaps were {gaps}",
        )
        self.assertLess(
            title_folio_gap(boxes, "ply", "613"),
            MINIMUM_TITLE_FOLIO_GAP_PT,
            "the standard right reserve must reproduce the title/folio defect",
        )

        production_chapter = first_toc_word(production_boxes, "AutomationChapter")
        mutated_chapter = first_toc_word(boxes, "AutomationChapter")
        self.assertEqual(
            (production_chapter.x_min, production_chapter.y_min),
            (mutated_chapter.x_min, mutated_chapter.y_min),
            "the section-row repair must not reposition the chapter entry",
        )
        production_subsection = first_toc_word(production_boxes, "NarrowSubsection")
        mutated_subsection = first_toc_word(boxes, "NarrowSubsection")
        self.assertEqual(
            production_subsection.x_min,
            mutated_subsection.x_min,
            "the section-row repair must not change subsection indentation",
        )


if __name__ == "__main__":
    unittest.main()
