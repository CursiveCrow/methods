#!/usr/bin/env python3
"""Fail-closed route and byte tests for exact source lines 15240--15488."""

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


class RuleSheetsSourceRouteTests(unittest.TestCase):
    def test_exact_artifact_and_wrapper_match_the_frozen_authority(self) -> None:
        lines = AUTHORITY.read_bytes().splitlines(keepends=True)
        raw = b"".join(lines[15239:15488])
        self.assertEqual(len(raw), 8067)
        self.assertEqual(
            hashlib.sha256(raw).hexdigest(),
            "46f85e115319017fbbb5ba133f876db402c0668063eb741c55ac9c6669ecad05",
        )
        normalized = raw.replace(b"\r\n", b"\n")
        self.assertEqual(len(normalized), 7818)
        self.assertEqual(
            hashlib.sha256(normalized).hexdigest(),
            "f63b9f82b7b28ab0fdef72181ac3aa368a40cc5fa1c6a87c42566bf20b86f3a8",
        )
        self.assertTrue(normalized.endswith(b"\n\n"))
        self.assertNotIn(
            b"\\chapter{Qualifying-Examination Problems and Selected Solutions}",
            normalized,
        )
        artifact = HANDBOOK / "restoration/inherited-15240-15488.tex"
        self.assertEqual(artifact.read_bytes(), normalized)
        wrapper = HANDBOOK / "restoration/scope-SRC-15240-15488.tex"
        self.assertEqual(
            wrapper.read_text(encoding="utf-8"),
            "\\begin{inheritedrestorationscope}{SRC-15240-15488}\n"
            "\\input{restoration/inherited-15240-15488}\n"
            "\\end{inheritedrestorationscope}\n",
        )
        self.assertEqual(
            hashlib.sha256(wrapper.read_bytes()).hexdigest(),
            "fb3f82b4e39a823ada2ac134c3c9cf59418f9eafee5a5c3635401b98c15efbad",
        )

    def test_appendix_c_wrapper_follows_appendix_b_before_editorial_aggregator(self) -> None:
        direct = inputs(HANDBOOK / "parts/p12.tex")
        appendix_b = "restoration/scope-SRC-15207-15239"
        appendix_c = "restoration/scope-SRC-15240-15488"
        aggregator = "parts/p12/automation-and-mechanization"
        start = direct.index(appendix_b)
        self.assertEqual(
            direct[start : start + 3], [appendix_b, appendix_c, aggregator]
        )
        self.assertEqual(direct.count(appendix_c), 1)

    def test_exact_labels_are_unique_and_registry_sheet_stays_distinct(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = re.findall(r"\\label\s*\{([^{}]+)\}", live)
        for label in (
            "ch:rule-sheets",
            "app:rules",
            "sec:rule-sheets-01",
            "sec:rule-sheets-02",
            "sec:rule-sheets-03",
            "sec:p14-rule-sheets",
        ):
            with self.subTest(label=label):
                self.assertEqual(labels.count(label), 1)

        source = (
            HANDBOOK / "restoration/inherited-15240-15488.tex"
        ).read_text(encoding="utf-8")
        registry = (HANDBOOK / "parts/p14/rule-sheets.tex").read_text(
            encoding="utf-8"
        )
        self.assertNotIn(r"\appendix", source)
        self.assertEqual(source.count(r"\chapter{Rule Sheets}"), 1)
        self.assertNotIn(r"\label{sec:p14-rule-sheets}", source)
        for source_label in (
            "ch:rule-sheets",
            "app:rules",
            "sec:rule-sheets-01",
            "sec:rule-sheets-02",
            "sec:rule-sheets-03",
        ):
            self.assertNotIn(rf"\label{{{source_label}}}", registry)


if __name__ == "__main__":
    unittest.main()
