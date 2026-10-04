#!/usr/bin/env python3
"""Fail-closed route/addition tests for exact source lines 14591--14728."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
MECHANIZED_IDS = (
    "SRC-14591-14628",
    "SRC-14629-14660",
    "SRC-14661-14690",
    "SRC-14691-14728",
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


class MechanizedProofSourceRouteTests(unittest.TestCase):
    def test_exact_wrappers_precede_the_editorial_automation_aggregator(self) -> None:
        direct = inputs(HANDBOOK / "parts/p12.tex")
        aggregator = "parts/p12/automation-and-mechanization"
        expected = [f"restoration/scope-{item}" for item in MECHANIZED_IDS]
        start = direct.index("restoration/scope-SEP-14590-14590") + 1
        self.assertEqual(direct[start : start + 5], expected + [aggregator])
        for item in expected:
            self.assertEqual(direct.count(item), 1)

    def test_exact_labels_are_unique_and_editorial_chapter_stays_distinct(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = re.findall(r"\\label\s*\{([^{}]+)\}", live)
        exact = {
            "ch:mechanization",
            *(f"sec:mechanization-{number:02d}" for number in range(1, 5)),
            "ex:mechanization-01",
            "ex:mechanization-02",
        }
        for label in exact:
            with self.subTest(label=label):
                self.assertEqual(labels.count(label), 1)
        self.assertEqual(labels.count("sec:p12-interactive-proof"), 1)

    def test_editorial_interactive_proof_declares_separate_standing(self) -> None:
        text = (HANDBOOK / "parts/p12/interactive-proof.tex").read_text(
            encoding="utf-8"
        )
        self.assertIn("separately authored editorial survey", text)
        self.assertRegex(
            text,
            r"exact\s+inherited Mechanized Proof Checking chapter",
        )
        self.assertIn(r"\chapter{Interactive and Mechanized Proof}", text)


if __name__ == "__main__":
    unittest.main()
