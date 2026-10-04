#!/usr/bin/env python3
"""Fail-closed route and byte tests for exact source lines 15093--15206."""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
AUTHORITY = ROOT / "source/formal-logic-reference.tex"
PROVENANCE_ID = "SRC-15093-15206"


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


class RegisteredNotationSourceRouteTests(unittest.TestCase):
    def test_exact_artifact_and_wrapper_match_the_frozen_authority(self) -> None:
        lines = AUTHORITY.read_bytes().splitlines(keepends=True)
        raw = b"".join(lines[15092:15206])
        self.assertEqual(len(raw), 6248)
        self.assertEqual(
            hashlib.sha256(raw).hexdigest(),
            "f87c00a631ef363b00c2aa0bf8943e003019e05aa53a30d5c40b4f87d9772d40",
        )
        normalized = raw.replace(b"\r\n", b"\n")
        self.assertEqual(len(normalized), 6134)
        self.assertEqual(
            hashlib.sha256(normalized).hexdigest(),
            "36c030ab3074edf77475ba206cf288a8dabb3954e48718c94bbaba3b046e172c",
        )
        self.assertTrue(normalized.endswith(b"\n\n"))
        self.assertNotIn(b"\\chapter{Binding and Precedence}", normalized)
        artifact = HANDBOOK / "restoration/inherited-15093-15206.tex"
        self.assertEqual(artifact.read_bytes(), normalized)
        wrapper = HANDBOOK / "restoration/scope-SRC-15093-15206.tex"
        self.assertEqual(
            wrapper.read_text(encoding="utf-8"),
            "\\begin{inheritedrestorationscope}{SRC-15093-15206}\n"
            "\\input{restoration/inherited-15093-15206}\n"
            "\\end{inheritedrestorationscope}\n",
        )
        self.assertEqual(
            hashlib.sha256(wrapper.read_bytes()).hexdigest(),
            "46e10f92115c68a714164367628e775ef8bff14959c005f935770620544e5fff",
        )

    def test_registered_notation_wrapper_precedes_editorial_aggregator(self) -> None:
        direct = inputs(HANDBOOK / "parts/p12.tex")
        predecessor = "restoration/scope-SEP-15092-15092"
        wrapper = "restoration/scope-SRC-15093-15206"
        aggregator = "parts/p12/automation-and-mechanization"
        start = direct.index(predecessor)
        self.assertEqual(direct[start : start + 3], [predecessor, wrapper, aggregator])
        self.assertEqual(direct.count(wrapper), 1)

    def test_exact_labels_and_appendix_token_are_unique_on_reachable_surface(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = re.findall(r"\\label\s*\{([^{}]+)\}", live)
        for label in (
            "ch:registered-notation",
            "app:notation",
            "sec:registered-notation-01",
            "sec:registered-notation-02",
        ):
            with self.subTest(label=label):
                self.assertEqual(labels.count(label), 1)
        artifact = (
            HANDBOOK / "restoration/inherited-15093-15206.tex"
        ).read_text(encoding="utf-8")
        self.assertEqual(artifact.count(r"\appendix"), 1)
        self.assertEqual(artifact.count(r"\chapter{Registered Notation}"), 1)


if __name__ == "__main__":
    unittest.main()
