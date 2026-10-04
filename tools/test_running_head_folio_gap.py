#!/usr/bin/env python3
"""Rendered public-seam tests for book-class running-head separation."""

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
MINIMUM_FOLIO_MARK_GAP_PT = 4.0


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


def fixture_document(
    *,
    legacy_even_head_mutation: bool = False,
    legacy_odd_head_mutation: bool = False,
) -> str:
    if legacy_even_head_mutation and legacy_odd_head_mutation:
        raise ValueError("running-head mutations are mutually exclusive")
    mutation = ""
    if legacy_even_head_mutation:
        mutation = (
            r"\makeatletter"
            "\n"
            r"\def\@evenhead{\thepage\hfil\slshape\leftmark}"
            "\n"
            r"\makeatother"
            "\n"
        )
    elif legacy_odd_head_mutation:
        mutation = (
            r"\makeatletter"
            "\n"
            r"\def\@oddhead{{\slshape\rightmark}\hfil\thepage}"
            "\n"
            r"\makeatother"
            "\n"
        )
    return (
        r"\documentclass[11pt]{book}"
        "\n"
        r"\usepackage{handbook}"
        "\n"
        r"\pagestyle{headings}"
        "\n"
        + mutation
        + r"\begin{document}"
        "\n"
        + r"\mainmatter"
        "\n"
        + r"\setcounter{page}{107}"
        "\n"
        + r"\setcounter{chapter}{12}"
        "\n"
        + r"\chapter{Cardinality, Normal Forms, and Resolution}"
        "\n"
        + r"\section{Standard and nonstandard models of arithmetic}"
        "\n"
        + r"Chapter opening.\newpage"
        "\n"
        + r"Long even running-head page.\newpage"
        "\n"
        + r"Odd running-head control page.\newpage"
        "\n"
        + r"\chaptermark{Short Header Control}"
        "\n"
        + r"\sectionmark{Short Odd Header Control}"
        "\n"
        + r"Short even running-head control page.\newpage"
        "\n"
        + r"Short odd running-head control page."
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


def header_word(boxes: list[WordBox], *, page_number: str, text: str) -> WordBox:
    page_numbers = [
        box for box in boxes if box.text == page_number and box.y_min < 120.0
    ]
    if len(page_numbers) != 1:
        raise AssertionError(
            f"expected one header folio {page_number}, found {page_numbers}"
        )
    page = page_numbers[0].page
    matches = [
        box
        for box in boxes
        if box.page == page and box.text == text and box.y_min < 120.0
    ]
    if len(matches) != 1:
        raise AssertionError(
            f"expected one header word {text!r} on folio {page_number}, "
            f"found {matches}"
        )
    return matches[0]


def folio_mark_gap(boxes: list[WordBox], page_number: str) -> float:
    try:
        folio = header_word(boxes, page_number=page_number, text=page_number)
        mark = header_word(boxes, page_number=page_number, text="CHAPTER")
    except AssertionError:
        # Poppler fuses touching glyph runs such as ``108CHAPTER`` into one
        # word.  Treating a missing separate token as negative infinity makes
        # the rendered oracle fail closed on exactly that collision.
        return float("-inf")
    return mark.x_min - folio.x_max


def mark_folio_gap(boxes: list[WordBox], page_number: str) -> float:
    try:
        mark = header_word(boxes, page_number=page_number, text="ARITHMETIC")
        folio = header_word(boxes, page_number=page_number, text=page_number)
    except AssertionError:
        # A touching odd-page run such as ``ARITHMETIC109`` is one Poppler
        # token and must fail closed.
        return float("-inf")
    return folio.x_min - mark.x_max


@unittest.skipUnless(
    PDFLATEX and PDFTOTEXT,
    "pdflatex and pdftotext are required for rendered running-head tests",
)
class RunningHeadFolioGapTests(unittest.TestCase):
    def compile_fixture(
        self,
        *,
        legacy_even_head_mutation: bool = False,
        legacy_odd_head_mutation: bool = False,
    ) -> list[WordBox]:
        temporary = tempfile.TemporaryDirectory(prefix="running-head-gap-")
        self.addCleanup(temporary.cleanup)
        build = Path(temporary.name)
        (build / "fixture.tex").write_text(
            fixture_document(
                legacy_even_head_mutation=legacy_even_head_mutation,
                legacy_odd_head_mutation=legacy_odd_head_mutation,
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
        if not legacy_even_head_mutation and not legacy_odd_head_mutation:
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

    def test_long_even_running_head_leaves_a_readable_gap_after_the_folio(self) -> None:
        boxes = self.compile_fixture()
        self.assertGreaterEqual(
            folio_mark_gap(boxes, "108"),
            MINIMUM_FOLIO_MARK_GAP_PT,
            "the even-page folio must not run directly into a long chapter mark",
        )

    def test_oracle_rejects_the_legacy_even_running_head(self) -> None:
        boxes = self.compile_fixture(legacy_even_head_mutation=True)
        self.assertLess(
            folio_mark_gap(boxes, "108"),
            MINIMUM_FOLIO_MARK_GAP_PT,
            "the known concatenating book-class header must fail closed",
        )

    def test_long_odd_running_head_leaves_a_readable_gap_before_the_folio(self) -> None:
        boxes = self.compile_fixture()
        self.assertGreaterEqual(
            mark_folio_gap(boxes, "109"),
            MINIMUM_FOLIO_MARK_GAP_PT,
            "the long odd-page section mark must not run into its folio",
        )

    def test_oracle_rejects_the_legacy_odd_running_head(self) -> None:
        boxes = self.compile_fixture(legacy_odd_head_mutation=True)
        self.assertLess(
            mark_folio_gap(boxes, "109"),
            MINIMUM_FOLIO_MARK_GAP_PT,
            "the known concatenating odd header must fail closed",
        )

    def test_short_even_and_odd_headers_keep_book_class_positions(self) -> None:
        production = self.compile_fixture()
        legacy = self.compile_fixture(legacy_even_head_mutation=True)
        targets = (("110", "SHORT"), ("111", "SHORT"))
        for page_number, word in targets:
            with self.subTest(page_number=page_number, word=word):
                actual = header_word(production, page_number=page_number, text=word)
                control = header_word(legacy, page_number=page_number, text=word)
                self.assertEqual(
                    (actual.x_min, actual.y_min, actual.x_max, actual.y_max),
                    (control.x_min, control.y_min, control.x_max, control.y_max),
                )


if __name__ == "__main__":
    unittest.main()
