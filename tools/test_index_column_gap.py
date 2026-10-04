#!/usr/bin/env python3
"""Rendered public-seam tests for separation between index columns."""

from __future__ import annotations

import html
import os
import shutil
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK_TEX = ROOT / "handbook"
HANDBOOK_STYLE = HANDBOOK_TEX / "handbook.sty"
PDFLATEX = shutil.which("pdflatex")
PDFTOTEXT = shutil.which("pdftotext")
MINIMUM_INDEX_COLUMN_GAP_PT = 4.0


@dataclass(frozen=True)
class WordBox:
    page: int
    column: int
    text: str
    x_min: float
    y_min: float
    x_max: float
    y_max: float


def fixture_document(*, case: str, column_gap_override: str | None = None) -> str:
    mutation = ""
    if column_gap_override is not None:
        mutation = (
            r"\BeforeBeginEnvironment{theindex}{\setlength{\columnsep}{"
            + column_gap_override
            + "}}"
            "\n"
        )
    if case == "aligned":
        left = (
            r"\item Primitive, derived, and admissible rules, \hyperpage{392}"
            "\n"
            + r"\item Primitive recursive relation, \hyperpage{233}"
        )
        right = (
            r"\item Proof theory, \hyperpage{17}"
            "\n"
            + r"\item Proof-net and GoI boundary, \hyperpage{422}"
        )
    elif case == "staggered":
        left = (
            r"\item Negative solution to the classical Entscheidungsproblem, "
            r"\hyperpage{247}"
            "\n"
            + r"\item negative translation, \hyperpage{463}"
        )
        # The actual index columns are not locked to a shared baseline grid.
        # This offset reproduces the p794 pair whose word boxes intersect even
        # though their y origins differ, which the former oracle missed.
        right = (
            r"\item \raisebox{-2.37pt}{normal derivation, \hyperpage{406}}"
            "\n"
            + r"\item normal form, \hyperpage{405}"
        )
    else:
        raise ValueError(f"unknown index collision fixture {case!r}")
    return (
        r"\documentclass[11pt]{book}"
        "\n"
        r"\usepackage{handbook}"
        "\n"
        + mutation
        + r"\begin{document}"
        "\n"
        + r"\begin{theindex}"
        "\n"
        + left
        + "\n"
        + r"\newpage"
        "\n"
        + right
        + "\n"
        + r"\end{theindex}"
        "\n"
        + r"\end{document}"
        "\n"
    )


def _tag(node: ET.Element) -> str:
    return node.tag.rsplit("}", 1)[-1]


def parse_word_boxes(path: Path) -> tuple[int, list[WordBox]]:
    root = ET.parse(path).getroot()
    boxes: list[WordBox] = []
    pages = [node for node in root.iter() if _tag(node) == "page"]
    for page_number, page in enumerate(pages):
        # Both columns lie inside the book class's centered text block, so the
        # right column begins left of the physical-page midpoint.  Forty-five
        # percent of the page width lies inside the actual intercolumn gap for
        # every governed mutation (10pt, 25pt, and the production candidate).
        column_divider = float(page.attrib["width"]) * 0.45
        for line in (node for node in page.iter() if _tag(node) == "line"):
            line_column = 0 if float(line.attrib["xMin"]) < column_divider else 1
            words = [node for node in line if _tag(node) == "word"]
            split_at: int | None = None
            if line_column == 0:
                for word_number in range(1, len(words)):
                    previous = words[word_number - 1]
                    current = words[word_number]
                    if (
                        float(current.attrib["xMin"]) < float(previous.attrib["xMax"])
                        and float(current.attrib["xMin"]) > column_divider
                    ):
                        # Poppler may merge physically overlapping left- and
                        # right-column runs into one XML line.  The backwards
                        # x step is the fail-closed boundary between them.
                        split_at = word_number
                        break
            for word_number, word in enumerate(words):
                column = (
                    1
                    if line_column == 1
                    or (split_at is not None and word_number >= split_at)
                    else 0
                )
                boxes.append(
                    WordBox(
                        page=page_number,
                        column=column,
                        text=html.unescape("".join(word.itertext())),
                        x_min=float(word.attrib["xMin"]),
                        y_min=float(word.attrib["yMin"]),
                        x_max=float(word.attrib["xMax"]),
                        y_max=float(word.attrib["yMax"]),
                    )
                )
    return len(pages), boxes


def tightest_cross_column_pair(
    boxes: list[WordBox],
) -> tuple[float, WordBox, WordBox]:
    candidates: list[tuple[float, WordBox, WordBox]] = []
    for left in boxes:
        if left.column != 0 or left.y_min < 120.0:
            continue
        for right in boxes:
            if right.page != left.page or right.column != 1 or right.y_min < 120.0:
                continue
            if left.y_min < right.y_max and right.y_min < left.y_max:
                candidates.append((right.x_min - left.x_max, left, right))
    if not candidates:
        raise AssertionError("rendered index has no opposing vertically intersecting words")
    return min(candidates, key=lambda candidate: candidate[0])


def exact_cross_column_gap(
    boxes: list[WordBox], *, left_text: str, right_text: str
) -> float:
    candidates = [
        right.x_min - left.x_max
        for left in boxes
        for right in boxes
        if left.text == left_text
        and right.text == right_text
        and left.page == right.page
        and left.column == 0
        and right.column == 1
        and left.y_min < right.y_max
        and right.y_min < left.y_max
    ]
    if len(candidates) != 1:
        matching_boxes = [
            box for box in boxes if box.text in {left_text, right_text}
        ]
        raise AssertionError(
            f"expected one vertically intersecting {left_text!r}/{right_text!r} "
            f"pair, found {candidates}; rendered matches: {matching_boxes}"
        )
    return candidates[0]


def exact_word(boxes: list[WordBox], text: str) -> WordBox:
    matches = [box for box in boxes if box.text == text]
    if len(matches) != 1:
        raise AssertionError(f"expected one rendered word {text!r}, found {matches}")
    return matches[0]


@unittest.skipUnless(
    PDFLATEX and PDFTOTEXT,
    "pdflatex and pdftotext are required for rendered index tests",
)
class IndexColumnGapTests(unittest.TestCase):
    def test_style_establishes_the_book_class_intended_gap_before_the_index(self) -> None:
        source = HANDBOOK_STYLE.read_text(encoding="utf-8")
        hook = r"\BeforeBeginEnvironment{theindex}{\setlength{\columnsep}{35pt}}"
        self.assertEqual(source.count(hook), 1)

    def compile_index(
        self, *, case: str, column_gap_override: str | None = None
    ) -> tuple[int, list[WordBox], str]:
        temporary = tempfile.TemporaryDirectory(prefix="index-column-gap-")
        self.addCleanup(temporary.cleanup)
        build = Path(temporary.name)
        (build / "fixture.tex").write_text(
            fixture_document(case=case, column_gap_override=column_gap_override),
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
            [str(PDFTOTEXT), "-bbox-layout", "fixture.pdf", bbox.name],
            cwd=build,
            text=True,
            capture_output=True,
            timeout=60,
        )
        self.assertEqual(
            extracted.returncode, 0, extracted.stdout + extracted.stderr
        )
        plain = subprocess.run(
            [str(PDFTOTEXT), "-layout", "fixture.pdf", "-"],
            cwd=build,
            text=True,
            capture_output=True,
            timeout=60,
        )
        self.assertEqual(plain.returncode, 0, plain.stdout + plain.stderr)
        pages, boxes = parse_word_boxes(bbox)
        return pages, boxes, plain.stdout

    def test_aligned_index_entries_leave_a_readable_gap_without_fused_text(self) -> None:
        pages, boxes, text = self.compile_index(case="aligned")
        self.assertEqual(pages, 1)
        self.assertGreaterEqual(
            tightest_cross_column_pair(boxes)[0], MINIMUM_INDEX_COLUMN_GAP_PT
        )
        self.assertNotIn("rules,Proof", text.replace(" ", ""))
        self.assertNotIn("rulesProof", text.replace(" ", ""))

        primitive = exact_word(boxes, "Primitive,")
        proof = exact_word(boxes, "Proof")
        relation = exact_word(boxes, "relation,")
        proof_net = exact_word(boxes, "Proof-net")
        self.assertAlmostEqual(primitive.x_min, 100.892, places=2)
        self.assertAlmostEqual(relation.x_min, 194.530, places=2)
        self.assertGreater(proof.x_min - primitive.x_min, 150.0)
        self.assertAlmostEqual(proof_net.x_min, proof.x_min, places=2)
        self.assertEqual((relation.page, proof_net.page), (0, 0))

    def test_staggered_index_entries_leave_a_readable_gap(self) -> None:
        pages, boxes, text = self.compile_index(case="staggered")
        self.assertEqual(pages, 1)
        self.assertGreaterEqual(
            tightest_cross_column_pair(boxes)[0],
            MINIMUM_INDEX_COLUMN_GAP_PT,
            "vertically intersecting words must clear across index columns",
        )
        self.assertNotIn("Entscheinormal", text.replace(" ", ""))
        self.assertIn("Negative solution", text)
        self.assertIn("normal derivation", text)

    def test_oracle_rejects_the_legacy_ten_point_column_gap(self) -> None:
        pages, boxes, text = self.compile_index(
            case="aligned", column_gap_override="10pt"
        )
        self.assertEqual(pages, 1)
        self.assertLess(
            exact_cross_column_gap(boxes, left_text="rules,", right_text="Proof"),
            MINIMUM_INDEX_COLUMN_GAP_PT,
            "the legacy index column geometry must fail closed",
        )
        self.assertTrue(
            "rules,Proof" in text.replace(" ", "")
            or "rulesProof" in text.replace(" ", "")
            or exact_cross_column_gap(
                boxes, left_text="rules,", right_text="Proof"
            )
            < 0.0,
            "the mutation must reproduce fused extraction or physical overlap",
        )

    def test_oracle_rejects_the_failed_twenty_five_point_gap(self) -> None:
        pages, boxes, text = self.compile_index(
            case="staggered", column_gap_override="25pt"
        )
        self.assertEqual(pages, 1)
        self.assertLess(
            exact_cross_column_gap(
                boxes, left_text="Entschei-", right_text="normal"
            ),
            MINIMUM_INDEX_COLUMN_GAP_PT,
            "the failed p794 geometry must remain a red-capable mutation",
        )
        self.assertTrue(
            "Entscheinormal" in text.replace(" ", "")
            or tightest_cross_column_pair(boxes)[0] < 0.0
        )


if __name__ == "__main__":
    unittest.main()
