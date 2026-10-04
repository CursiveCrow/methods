#!/usr/bin/env python3
"""Rendered public-seam tests for chapter-title/folio separation in the TOC."""

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


def fixture_document(*, legacy_body_page_width_mutation: bool = False) -> str:
    mutation = ""
    if legacy_body_page_width_mutation:
        mutation = (
            r"\makeatletter"
            "\n"
            r"\patchcmd{\l@chapter}%"
            "\n"
            r"  {\begingroup\ifdefstring{\@pnumwidth}{1.55em}%"
            "\n"
            r"     {\def\@pnumwidth{2.3em}}{}}%"
            "\n"
            r"  {\begingroup\ifdefstring{\@pnumwidth}{1.55em}%"
            "\n"
            r"     {\def\@pnumwidth{1.55em}}{}}%"
            "\n"
            r"  {}%"
            "\n"
            r"  {\PackageError{fixture}{legacy body TOC mutation failed}{}}%"
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
        +
        r"\begin{document}"
        "\n"
        r"\frontmatter"
        "\n"
        r"\tableofcontents"
        "\n"
        r"\mainmatter"
        "\n"
        r"\setcounter{chapter}{24}"
        "\n"
        r"\setcounter{page}{245}"
        "\n"
        r"\chapter{Logical Decision Problems and the Arithmetical Hierarchy}"
        "\n"
        r"\section{The classical decision problem}"
        "\n"
        r"\chapter{BodyControl}"
        "\n"
        r"\end{document}"
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


def title_folio_gap(boxes: list[WordBox]) -> float:
    titles = [
        box
        for box in boxes
        if box.page == 0 and box.text in {"Hierarchy", "chy"}
    ]
    candidates: list[float] = []
    for title in titles:
        folios = [
            box
            for box in boxes
            if box.page == title.page
            and box.text == "245"
            and box.x_min >= title.x_max
            and abs((box.y_min + box.y_max) - (title.y_min + title.y_max)) < 2.0
        ]
        for folio in folios:
            candidates.append(folio.x_min - title.x_max)
    # A fused extraction token such as Hierarchy245 makes the title word
    # disappear and deliberately fails closed.
    return max(candidates, default=float("-inf"))


def first_toc_word(boxes: list[WordBox], text: str) -> WordBox:
    matches = [box for box in boxes if box.page == 0 and box.text == text]
    if not matches:
        raise AssertionError(f"TOC word is absent: {text}")
    return min(matches, key=lambda box: (box.y_min, box.x_min))


def folio_beside(boxes: list[WordBox], title: str) -> WordBox:
    title_box = first_toc_word(boxes, title)
    matches = [
        box
        for box in boxes
        if box.page == title_box.page
        and box.text.isdigit()
        and box.x_min > title_box.x_max
        and abs((box.y_min + box.y_max) - (title_box.y_min + title_box.y_max)) < 2.0
    ]
    if not matches:
        raise AssertionError(f"TOC folio is absent beside {title}")
    return max(matches, key=lambda box: box.x_max)


@unittest.skipUnless(
    PDFLATEX and PDFTOTEXT,
    "pdflatex and pdftotext are required for rendered TOC tests",
)
class TocChapterPageNumberWidthTests(unittest.TestCase):
    def compile_toc(
        self, *, legacy_body_page_width_mutation: bool = False
    ) -> tuple[list[WordBox], str, str]:
        temporary = tempfile.TemporaryDirectory(prefix="toc-chapter-page-width-")
        self.addCleanup(temporary.cleanup)
        build = Path(temporary.name)
        (build / "fixture.tex").write_text(
            fixture_document(
                legacy_body_page_width_mutation=legacy_body_page_width_mutation
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

        bbox = build / "fixture-bbox.html"
        extracted = subprocess.run(
            [str(PDFTOTEXT), "-bbox", "fixture.pdf", bbox.name],
            cwd=build,
            text=True,
            capture_output=True,
            timeout=60,
        )
        self.assertEqual(extracted.returncode, 0, extracted.stdout + extracted.stderr)
        plain = subprocess.run(
            [str(PDFTOTEXT), "-layout", "fixture.pdf", "-"],
            cwd=build,
            text=True,
            capture_output=True,
            timeout=60,
        )
        self.assertEqual(plain.returncode, 0, plain.stdout + plain.stderr)
        return parse_word_boxes(bbox), plain.stdout, output

    def test_long_body_chapter_title_leaves_a_readable_gap_before_its_folio(self) -> None:
        boxes, plain, output = self.compile_toc()
        self.assertGreaterEqual(
            title_folio_gap(boxes),
            MINIMUM_TITLE_FOLIO_GAP_PT,
            "the Chapter 25 title must leave a readable gap before folio 245; "
            f"relevant boxes={[box for box in boxes if box.text in {'Hierarchy', 'Hierarchy245', '245'}]}; "
            f"plain={plain!r}",
        )
        self.assertNotIn("Hierarchy245", plain.replace(" ", ""))
        self.assertNotIn(r"Overfull \hbox", output)

    def test_oracle_rejects_the_legacy_body_chapter_page_reserve_only(self) -> None:
        production, _, _ = self.compile_toc()
        legacy, legacy_plain, _ = self.compile_toc(
            legacy_body_page_width_mutation=True
        )
        self.assertLess(
            title_folio_gap(legacy),
            MINIMUM_TITLE_FOLIO_GAP_PT,
            "restoring the legacy reserve must reproduce the unsafe seam",
        )
        self.assertIn("Hierarchy245", legacy_plain.replace(" ", ""))

        for word in ("BodyControl", "classical"):
            with self.subTest(control_word=word):
                actual = first_toc_word(production, word)
                control = first_toc_word(legacy, word)
                self.assertEqual((actual.x_min, actual.x_max), (control.x_min, control.x_max))
        self.assertAlmostEqual(
            folio_beside(production, "BodyControl").x_max,
            folio_beside(legacy, "BodyControl").x_max,
            places=3,
            msg="the right-aligned folio position must remain unchanged",
        )


if __name__ == "__main__":
    unittest.main()
