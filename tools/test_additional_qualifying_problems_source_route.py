#!/usr/bin/env python3
"""Fail-closed route and byte tests for exact source lines 15620--15637."""

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


class AdditionalQualifyingProblemsSourceRouteTests(unittest.TestCase):
    def test_exact_artifact_and_wrapper_match_the_frozen_authority(self) -> None:
        lines = AUTHORITY.read_bytes().splitlines(keepends=True)
        raw = b"".join(lines[15619:15637])
        self.assertEqual(len(raw), 937)
        self.assertEqual(
            hashlib.sha256(raw).hexdigest(),
            "d81a26dabe610eef304a6b8eb35af5f2dbd9e4a95d5a3c08060f006aea4ed9ea",
        )
        normalized = raw.replace(b"\r\n", b"\n")
        self.assertEqual(len(normalized), 919)
        self.assertEqual(
            hashlib.sha256(normalized).hexdigest(),
            "9d788c4df60544647f1de42a65ac789e7ab3ed1a3b81fd2dc02974bf89e983e7",
        )
        self.assertTrue(normalized.endswith(b"\n\n"))
        self.assertNotIn(b"\\chapter{Exercise Feedback}", normalized)
        artifact = HANDBOOK / "restoration/inherited-15620-15637.tex"
        self.assertEqual(artifact.read_bytes(), normalized)
        wrapper = HANDBOOK / "restoration/scope-SRC-15620-15637.tex"
        self.assertEqual(
            wrapper.read_text(encoding="utf-8"),
            "\\begin{inheritedrestorationscope}{SRC-15620-15637}\n"
            "\\input{restoration/inherited-15620-15637}\n"
            "\\end{inheritedrestorationscope}\n",
        )
        self.assertEqual(
            hashlib.sha256(wrapper.read_bytes()).hexdigest(),
            "4f9c4fd53ba9d65e2316757f9691165d0dd6bb655ef6df4a6c1f3ee0bc592a0b",
        )

    def test_appendix_d6_continuation_precedes_editorial_aggregator(self) -> None:
        direct = inputs(HANDBOOK / "parts/p12.tex")
        appendix_d = "restoration/scope-SRC-15489-15619"
        continuation = "restoration/scope-SRC-15620-15637"
        aggregator = "parts/p12/automation-and-mechanization"
        start = direct.index(appendix_d)
        self.assertEqual(
            direct[start : start + 3], [appendix_d, continuation, aggregator]
        )
        self.assertEqual(direct.count(continuation), 1)
        self.assertNotIn("generated/audit-p12", direct)

    def test_exact_section_and_all_five_prompts_are_preserved_without_invented_prompt_units(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = re.findall(r"\\label\s*\{([^{}]+)\}", live)
        self.assertEqual(labels.count("sec:qualifying-problems-06"), 1)

        artifact = (
            HANDBOOK / "restoration/inherited-15620-15637.tex"
        ).read_text(encoding="utf-8")
        self.assertEqual(artifact.count(r"\section{Additional problems}"), 1)
        self.assertEqual(len(re.findall(r"(?m)^\s*\\item\b", artifact)), 5)
        self.assertIn("Formalize one theorem in a proof assistant", artifact)
        self.assertNotIn(r"\chapter", artifact)


if __name__ == "__main__":
    unittest.main()
