#!/usr/bin/env python3
"""Fail-closed route and byte tests for exact source lines 15638--16742."""

from __future__ import annotations

import hashlib
import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
AUTHORITY = ROOT / "source/formal-logic-reference.tex"


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


class ExerciseFeedbackSourceRouteTests(unittest.TestCase):
    def test_exact_artifact_and_wrapper_match_the_frozen_authority(self) -> None:
        lines = AUTHORITY.read_bytes().splitlines(keepends=True)
        raw = b"".join(lines[15637:16742])
        self.assertEqual(len(raw), 64418)
        self.assertEqual(
            hashlib.sha256(raw).hexdigest(),
            "b6122d675c419640ac3f2297fb9c3920725e45907d531d5a76c08b6f0e0b49e9",
        )
        normalized = raw.replace(b"\r\n", b"\n")
        self.assertEqual(len(normalized), 63313)
        self.assertEqual(
            hashlib.sha256(normalized).hexdigest(),
            "993a3153c9ca856f761b5650c312e85e2be78fa23b8afc8edcd4e87a7b2983bf",
        )
        self.assertTrue(normalized.endswith(b"\n\n"))
        self.assertNotIn(b"\\chapter{Editorial and Formal-Logical Release Checklist}", normalized)
        artifact = HANDBOOK / "restoration/inherited-15638-16742.tex"
        self.assertEqual(artifact.read_bytes(), normalized)
        wrapper = HANDBOOK / "restoration/scope-SRC-15638-16742.tex"
        self.assertEqual(
            wrapper.read_text(encoding="utf-8"),
            "\\begin{inheritedrestorationscope}{SRC-15638-16742}\n"
            "\\input{restoration/inherited-15638-16742}\n"
            "\\end{inheritedrestorationscope}\n",
        )
        self.assertEqual(
            hashlib.sha256(wrapper.read_bytes()).hexdigest(),
            "29d01f396b496337daa15f72b48979d48ba7eb1591fc0e002fc8282b60881490",
        )

    def test_appendix_e_follows_d6_before_editorial_aggregator(self) -> None:
        direct = inputs(HANDBOOK / "parts/p12.tex")
        d6 = "restoration/scope-SRC-15620-15637"
        appendix_e = "restoration/scope-SRC-15638-16742"
        aggregator = "parts/p12/automation-and-mechanization"
        start = direct.index(d6)
        self.assertEqual(direct[start : start + 3], [d6, appendix_e, aggregator])
        self.assertEqual(direct.count(appendix_e), 1)

    def test_all_feedback_headings_solutions_and_targets_are_exact(self) -> None:
        artifact = (
            HANDBOOK / "restoration/inherited-15638-16742.tex"
        ).read_text(encoding="utf-8")
        self.assertEqual(
            re.findall(r"\\label\{([^{}]+)\}", artifact),
            ["ch:exercise-feedback", "app:exercise-feedback"],
        )
        self.assertEqual(len(re.findall(r"\\section\{", artifact)), 12)
        paragraph_targets = re.findall(
            r"\\paragraph\{\\hyperref\[([^\]]+)\]", artifact
        )
        self.assertEqual(len(paragraph_targets), 111)
        self.assertEqual(len(set(paragraph_targets)), 111)
        self.assertEqual(artifact.count(r"\textit{Solution.}"), 89)
        self.assertEqual(artifact.count(r"\textit{Solution sketch.}"), 22)
        all_targets = re.findall(r"\\hyperref\[([^\]]+)\]", artifact)
        self.assertEqual(len(all_targets), 117)
        self.assertEqual(len(set(all_targets)), 117)
        self.assertEqual(
            re.findall(r"\\[Cc]ref\{([^{}]+)\}", artifact),
            ["lem:q-bounded-cases", "lem:q-dichotomy"],
        )
        self.assertNotIn(r"\cite", artifact)

        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = Counter(re.findall(r"\\label\s*\{([^{}]+)\}", live))
        for target in [*all_targets, "lem:q-bounded-cases", "lem:q-dichotomy"]:
            with self.subTest(target=target):
                self.assertEqual(labels[target], 1)


if __name__ == "__main__":
    unittest.main()
