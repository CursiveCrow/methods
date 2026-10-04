#!/usr/bin/env python3
"""Fail-closed route and byte tests for exact source lines 15489--15619."""

from __future__ import annotations

import hashlib
import re
import unittest
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


class QualifyingProblemsSourceRouteTests(unittest.TestCase):
    def test_exact_artifact_and_wrapper_match_the_frozen_authority(self) -> None:
        lines = AUTHORITY.read_bytes().splitlines(keepends=True)
        raw = b"".join(lines[15488:15619])
        self.assertEqual(len(raw), 6295)
        self.assertEqual(
            hashlib.sha256(raw).hexdigest(),
            "26dd4437a60fb0fe1d822b3c80e49e77fe877980ef3b343498168bf0a7ed6d09",
        )
        normalized = raw.replace(b"\r\n", b"\n")
        self.assertEqual(len(normalized), 6164)
        self.assertEqual(
            hashlib.sha256(normalized).hexdigest(),
            "175a9850e56757bcdd168d683f1e52a35b9207832204e3bb105f4a57405beb78",
        )
        self.assertTrue(normalized.endswith(b"\n\n"))
        self.assertNotIn(b"\\section{Additional problems}", normalized)
        artifact = HANDBOOK / "restoration/inherited-15489-15619.tex"
        self.assertEqual(artifact.read_bytes(), normalized)
        wrapper = HANDBOOK / "restoration/scope-SRC-15489-15619.tex"
        self.assertEqual(
            wrapper.read_text(encoding="utf-8"),
            "\\begin{inheritedrestorationscope}{SRC-15489-15619}\n"
            "\\input{restoration/inherited-15489-15619}\n"
            "\\end{inheritedrestorationscope}\n",
        )
        self.assertEqual(
            hashlib.sha256(wrapper.read_bytes()).hexdigest(),
            "be591efc3d984b76d55f9dd99491fd1c4a165481cdd877a85f3706b4412f8a91",
        )

    def test_appendix_d_follows_appendix_c_before_editorial_aggregator(self) -> None:
        direct = inputs(HANDBOOK / "parts/p12.tex")
        appendix_c = "restoration/scope-SRC-15240-15488"
        appendix_d = "restoration/scope-SRC-15489-15619"
        aggregator = "parts/p12/automation-and-mechanization"
        start = direct.index(appendix_c)
        self.assertEqual(
            direct[start : start + 3], [appendix_c, appendix_d, aggregator]
        )
        self.assertEqual(direct.count(appendix_d), 1)

    def test_exact_problem_labels_and_five_complete_solutions_are_unique(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = re.findall(r"\\label\s*\{([^{}]+)\}", live)
        expected = ["ch:qualifying-problems", "app:qualifying"]
        for number, suffix in enumerate(
            (
                "substitution",
                "compactness",
                "incompleteness",
                "modal-frame",
                "cut-subformula",
            ),
            start=1,
        ):
            expected.extend((f"sec:qualifying-problems-0{number}", f"prob:{suffix}"))
        for label in expected:
            with self.subTest(label=label):
                self.assertEqual(labels.count(label), 1)

        artifact = (
            HANDBOOK / "restoration/inherited-15489-15619.tex"
        ).read_text(encoding="utf-8")
        self.assertNotIn(r"\appendix", artifact)
        self.assertEqual(
            artifact.count(
                r"\chapter{Qualifying-Examination Problems and Selected Solutions}"
            ),
            1,
        )
        self.assertEqual(artifact.count(r"\begin{solution}"), 5)
        self.assertEqual(artifact.count(r"\end{solution}"), 5)


if __name__ == "__main__":
    unittest.main()
