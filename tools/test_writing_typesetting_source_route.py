#!/usr/bin/env python3
"""Fail-closed route/addition tests for exact source lines 14729--15029."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
WRITING_IDS = (
    "SRC-14729-14778",
    "SRC-14779-14814",
    "SRC-14815-14850",
    "SRC-14851-14870",
    "SRC-14871-14931",
    "SRC-14932-14945",
    "SRC-14946-14975",
    "SRC-14976-14990",
    "SRC-14991-15029",
)


def inputs(path: Path) -> list[str]:
    text = re.sub(r"(?m)(?<!\\)%.*$", "", path.read_text(encoding="utf-8"))
    return [
        match.group(1).strip().removesuffix(".tex")
        for match in re.finditer(r"\\input\s*\{([^{}]+)\}", text)
    ]


def reachable(path: Path) -> set[Path]:
    seen: set[Path] = set()

    def visit(current: Path) -> None:
        current = current.resolve()
        if current in seen:
            return
        seen.add(current)
        for item in inputs(current):
            child = HANDBOOK / f"{item}.tex"
            if child.exists():
                visit(child)

    visit(path)
    return seen


class WritingTypesettingSourceRouteTests(unittest.TestCase):
    def test_nine_exact_wrappers_precede_the_editorial_aggregator(self) -> None:
        direct = inputs(HANDBOOK / "parts/p12.tex")
        aggregator = "parts/p12/automation-and-mechanization"
        expected = [f"restoration/scope-{item}" for item in WRITING_IDS]
        start = direct.index("restoration/scope-SRC-14691-14728") + 1
        self.assertEqual(direct[start : start + 10], expected + [aggregator])
        for item in expected:
            self.assertEqual(direct.count(item), 1)

    def test_exact_labels_are_unique_on_the_reachable_surface(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = re.findall(r"\\label\s*\{([^{}]+)\}", live)
        exact = {
            "ch:latex-style",
            "sec:latex-style-01",
            "sec:latex-style-02",
            "sec:latex-style-before-after",
            "sec:latex-style-03",
            "sec:latex-style-source-render",
            "sec:latex-style-04",
            "sec:latex-style-rule-correction",
            "sec:latex-style-05",
            "sec:latex-style-06",
            "ex:latex-style-01",
            "ex:latex-style-02",
        }
        for label in exact:
            with self.subTest(label=label):
                self.assertEqual(labels.count(label), 1)

    def test_editorial_audit_supplement_does_not_replace_exact_writing_chapter(self) -> None:
        text = (HANDBOOK / "parts/p12/formal-practice-supplement.tex").read_text(
            encoding="utf-8"
        )
        self.assertRegex(
            text,
            r"do not replace\s+the later exact Writing and\s+Typesetting Formal Logic chapter",
        )


if __name__ == "__main__":
    unittest.main()
