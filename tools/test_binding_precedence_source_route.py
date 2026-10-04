#!/usr/bin/env python3
"""Fail-closed route and byte tests for exact source lines 15207--15239."""

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


class BindingPrecedenceSourceRouteTests(unittest.TestCase):
    def test_exact_artifact_and_wrapper_match_the_frozen_authority(self) -> None:
        lines = AUTHORITY.read_bytes().splitlines(keepends=True)
        raw = b"".join(lines[15206:15239])
        self.assertEqual(len(raw), 1261)
        self.assertEqual(
            hashlib.sha256(raw).hexdigest(),
            "f273d7e92feb1f94ba23d1840977a0578775c583e195f180432ad75eea64cfd7",
        )
        normalized = raw.replace(b"\r\n", b"\n")
        self.assertEqual(len(normalized), 1228)
        self.assertEqual(
            hashlib.sha256(normalized).hexdigest(),
            "5f167b81d41e56030d833194ebba03b03d8aa8efe13a8d27c0020845698e8881",
        )
        self.assertTrue(normalized.endswith(b"\n\n"))
        self.assertNotIn(b"\\chapter{Rule Sheets}", normalized)
        artifact = HANDBOOK / "restoration/inherited-15207-15239.tex"
        self.assertEqual(artifact.read_bytes(), normalized)
        wrapper = HANDBOOK / "restoration/scope-SRC-15207-15239.tex"
        self.assertEqual(
            wrapper.read_text(encoding="utf-8"),
            "\\begin{inheritedrestorationscope}{SRC-15207-15239}\n"
            "\\input{restoration/inherited-15207-15239}\n"
            "\\end{inheritedrestorationscope}\n",
        )
        self.assertEqual(
            hashlib.sha256(wrapper.read_bytes()).hexdigest(),
            "505c73e2f9e56b7658d270566805f490f688aa4ab357f38156aeb11bbf87b79b",
        )

    def test_appendix_b_wrapper_precedes_editorial_aggregator(self) -> None:
        direct = inputs(HANDBOOK / "parts/p12.tex")
        predecessor = "restoration/scope-SRC-15093-15206"
        wrapper = "restoration/scope-SRC-15207-15239"
        aggregator = "parts/p12/automation-and-mechanization"
        start = direct.index(predecessor)
        self.assertEqual(direct[start : start + 3], [predecessor, wrapper, aggregator])
        self.assertEqual(direct.count(wrapper), 1)

    def test_exact_labels_are_unique_and_no_second_appendix_token_occurs(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = re.findall(r"\\label\s*\{([^{}]+)\}", live)
        for label in ("ch:binding-precedence", "app:precedence"):
            with self.subTest(label=label):
                self.assertEqual(labels.count(label), 1)
        artifact = (
            HANDBOOK / "restoration/inherited-15207-15239.tex"
        ).read_text(encoding="utf-8")
        self.assertNotIn(r"\appendix", artifact)
        self.assertEqual(artifact.count(r"\chapter{Binding and Precedence}"), 1)


if __name__ == "__main__":
    unittest.main()
