#!/usr/bin/env python3
"""Rendered TOC tests for annex number/title and title/page separation."""

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
    legacy_annex_width_mutation: bool = False,
    leaked_page_width_mutation: bool = False,
) -> str:
    if legacy_annex_width_mutation and leaked_page_width_mutation:
        raise ValueError("TOC width mutations are mutually exclusive")
    mutation = ""
    if legacy_annex_width_mutation:
        mutation = (
            r"\makeatletter"
            "\n"
            r"\providecommand\hbannextocsetup{}"
            "\n"
            r"\providecommand\hbannextocrestore{}"
            "\n"
            r"\renewcommand\hbannextocsetup{}"
            "\n"
            r"\renewcommand\hbannextocrestore{}"
            "\n"
            r"\makeatother"
            "\n"
        )
    elif leaked_page_width_mutation:
        mutation = (
            r"\makeatletter"
            "\n"
            r"\renewcommand\hbannextocrestore{%"
            "\n"
            r"  \patchcmd{\l@chapter}%"
            "\n"
            r"    {\setlength\@tempdima{2.5em}}%"
            "\n"
            r"    {\setlength\@tempdima{1.5em}}%"
            "\n"
            r"    {}%"
            "\n"
            r"    {\PackageError{fixture}{left width restore failed}{}}}"
            "\n"
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
        + r"\setcounter{chapter}{11}"
        "\n"
        + r"\chapter{BodyControl}"
        "\n"
        + r"\hbannexsetup"
        "\n"
        + r"\part*{Appendix P: Proof Annex}"
        "\n"
        + r"\addcontentsline{toc}{part}{Appendix P: Proof Annex}"
        "\n"
        + r"\hbannexchapter{3}{Model Theory}"
        "\n"
        + r"\setcounter{page}{720}"
        "\n"
        + r"\hbannexchapter{10}{Algebraic and Categorical Logic}"
        "\n"
        + r"\hbannexchapter{12}{Automation and Mechanization}"
        "\n"
        + r"\hbannexfinish"
        "\n"
        + r"\renewcommand\thechapter{\arabic{chapter}}"
        "\n"
        + r"\setcounter{chapter}{12}"
        "\n"
        + r"\chapter{AfterControl Ordinary Entry I BoundarySensitiveControl}"
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


def number_title_gap(boxes: list[WordBox], number: str) -> float:
    title_boxes = [box for box in boxes if box.text == "Proof" and box.page == 0]
    number_boxes = [box for box in boxes if box.text == number and box.page == 0]
    candidates: list[float] = []
    for number_box in number_boxes:
        for title_box in title_boxes:
            if abs((number_box.y_min + number_box.y_max) - (title_box.y_min + title_box.y_max)) < 2.0:
                candidates.append(title_box.x_min - number_box.x_max)
    return max(candidates, default=float("-inf"))


def first_toc_word(boxes: list[WordBox], text: str) -> WordBox:
    matches = [box for box in boxes if box.text == text and box.page == 0]
    if not matches:
        raise AssertionError(f"table-of-contents word is absent: {text}")
    return min(matches, key=lambda box: (box.y_min, box.x_min))


def toc_page_box_for_title(boxes: list[WordBox], title_word: str) -> WordBox:
    title_box = first_toc_word(boxes, title_word)
    matches = [
        box
        for box in boxes
        if box.page == title_box.page
        and box.text.isdigit()
        and box.x_min > title_box.x_max
        and abs((box.y_min + box.y_max) - (title_box.y_min + title_box.y_max))
        < 2.0
    ]
    if not matches:
        raise AssertionError(f"TOC page number is absent beside {title_word}")
    return max(matches, key=lambda box: box.x_max)


def title_page_gap(boxes: list[WordBox], *final_title_words: str) -> float:
    title_boxes = [
        box
        for box in boxes
        if box.text in final_title_words and box.page == 0
    ]
    candidates: list[float] = []
    for title_box in title_boxes:
        page_boxes = [
            box
            for box in boxes
            if box.page == title_box.page
            and box.text.isdigit()
            and box.x_min >= title_box.x_max
            and abs((box.y_min + box.y_max) - (title_box.y_min + title_box.y_max))
            < 2.0
        ]
        if page_boxes:
            page_box = min(page_boxes, key=lambda box: box.x_min)
            candidates.append(page_box.x_min - title_box.x_max)
    # A fused extraction token such as ``Mechanization725`` makes the exact
    # final title word disappear and therefore fails closed here.
    return max(candidates, default=float("-inf"))


@unittest.skipUnless(
    PDFLATEX and PDFTOTEXT,
    "pdflatex and pdftotext are required for rendered TOC tests",
)
class AnnexTocChapterNumberWidthTests(unittest.TestCase):
    def compile_toc(
        self,
        *,
        legacy_annex_width_mutation: bool = False,
        leaked_page_width_mutation: bool = False,
    ) -> list[WordBox]:
        temporary = tempfile.TemporaryDirectory(prefix="annex-toc-chapter-width-")
        self.addCleanup(temporary.cleanup)
        build = Path(temporary.name)
        (build / "fixture.tex").write_text(
            fixture_document(
                legacy_annex_width_mutation=legacy_annex_width_mutation,
                leaked_page_width_mutation=leaked_page_width_mutation,
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
        if not legacy_annex_width_mutation and not leaked_page_width_mutation:
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

    def test_annex_chapter_numbers_leave_a_readable_gap_before_titles(self) -> None:
        boxes = self.compile_toc()
        for number in ("P3", "P12"):
            with self.subTest(number=number):
                self.assertGreaterEqual(
                    number_title_gap(boxes, number),
                    MINIMUM_NUMBER_TITLE_GAP_PT,
                    f"{number} must leave a readable gap before Proof",
                )

    def test_long_annex_titles_leave_a_readable_gap_before_page_numbers(self) -> None:
        boxes = self.compile_toc()
        targets = {
            "Logic": ("Logic",),
            # A clean wrap may hyphenate this as ``Mechaniza-`` / ``tion``;
            # the final fragment must still remain separate from the folio.
            "Mechanization": ("Mechanization", "tion"),
        }
        for title, final_title_words in targets.items():
            with self.subTest(title=title):
                self.assertGreaterEqual(
                    title_page_gap(boxes, *final_title_words),
                    MINIMUM_NUMBER_TITLE_GAP_PT,
                    f"{title} must leave a readable gap before its page number",
                )

    def test_oracle_rejects_the_legacy_annex_number_width_only(self) -> None:
        production = self.compile_toc()
        legacy = self.compile_toc(legacy_annex_width_mutation=True)
        gaps = [number_title_gap(legacy, number) for number in ("P3", "P12")]
        self.assertTrue(
            any(gap < MINIMUM_NUMBER_TITLE_GAP_PT for gap in gaps),
            f"the legacy annex width must be detected, but gaps were {gaps}",
        )
        # The ordinary-body fallback now reserves 2.3em locally, so even this
        # full annex-switch mutation keeps the right title/folio boundary
        # readable.  This mutation remains load-bearing for the independent
        # P3/P12 number/title boundary; the restore-only mutation below locks
        # the distinct annex-to-body right-boundary transition.
        for title in ("BodyControl", "AfterControl"):
            with self.subTest(control_title=title):
                actual = first_toc_word(production, title)
                control = first_toc_word(legacy, title)
                self.assertEqual(
                    (actual.x_min, actual.x_max),
                    (control.x_min, control.x_max),
                    "the annex-only width must not reposition an ordinary "
                    "chapter horizontally before or after the annex",
                )

    def test_finish_restores_the_ordinary_right_page_number_boundary(self) -> None:
        production = self.compile_toc()
        leaked = self.compile_toc(leaked_page_width_mutation=True)

        body_folio = toc_page_box_for_title(production, "BodyControl")
        after_folio = toc_page_box_for_title(production, "AfterControl")
        self.assertAlmostEqual(body_folio.x_max, after_folio.x_max, places=3)
        self.assertGreaterEqual(
            title_page_gap(production, "BoundarySensitiveControl"),
            MINIMUM_NUMBER_TITLE_GAP_PT,
        )

        leaked_body_folio = toc_page_box_for_title(leaked, "BodyControl")
        leaked_after_folio = toc_page_box_for_title(leaked, "AfterControl")
        self.assertGreater(
            abs(leaked_after_folio.x_max - leaked_body_folio.x_max),
            1.0,
            "a restore-only mutation that leaks the annex page-number width "
            "must move the post-annex folio boundary",
        )


if __name__ == "__main__":
    unittest.main()
