#!/usr/bin/env python3
"""Fail-closed route/addition tests for exact source lines 14271--14590."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
PRECEDING_IDS = (
    "SRC-14095-14146",
    "SRC-14147-14169",
    "SRC-14170-14202",
    "SRC-14203-14230",
    "SRC-14231-14270",
)
RESTORATION_IDS = (
    "SRC-14271-14350",
    "SRC-14351-14400",
    "SRC-14401-14434",
    "SRC-14435-14479",
    "SRC-14480-14495",
    "SRC-14496-14521",
    "SRC-14522-14560",
    "SEP-14561-14561",
    "SRC-14562-14589",
    "SEP-14590-14590",
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


def declared_labels(text: str) -> list[str]:
    labels = re.findall(r"\\label\s*\{([^{}]+)\}", text)
    labels.extend(
        re.findall(
            r"\\begin\{(?:hb(?:method|example|definition|theorem|warning)|"
            r"proofboundary|systementry|annexitem)\}\{([^{}]+)\}",
            text,
        )
    )
    return labels


class AutomatedReasoningSourceRouteTests(unittest.TestCase):
    def test_exact_run_and_blank_continuity_precede_editorial_additions(self) -> None:
        direct = inputs(HANDBOOK / "parts/p12.tex")
        expected = (
            [f"restoration/scope-{item}" for item in PRECEDING_IDS]
            + ["parts/p12/formal-practice-supplement"]
            + [f"restoration/scope-{item}" for item in RESTORATION_IDS]
            + ["parts/p12/automation-and-mechanization"]
        )
        self.assertEqual(direct[: len(expected)], expected)
        self.assertEqual(
            [item for item in direct if item.startswith("restoration/scope-")],
            [f"restoration/scope-{item}" for item in PRECEDING_IDS + RESTORATION_IDS],
        )
        self.assertNotIn("generated/audit-p12", direct)

    def test_exact_labels_are_unique_and_editorial_labels_remain_distinct(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = declared_labels(live)
        exact = {
            "ch:automated-reasoning",
            *(f"sec:automated-reasoning-{number:02d}" for number in range(1, 8)),
            *(f"ex:automated-reasoning-{number:02d}" for number in range(1, 4)),
        }
        for label in exact:
            with self.subTest(label=label):
                self.assertEqual(labels.count(label), 1)
        for label in (
            "sec:p12-sat-and-certificates",
            "def:p12-dpll-state",
            "def:p12-dpll",
            "thm:p12-dpll-correctness",
            "sec:p12-first-order-automation",
        ):
            with self.subTest(editorial=label):
                self.assertEqual(labels.count(label), 1)

    def test_editorial_dpll_is_explicitly_separate_from_exact_source(self) -> None:
        text = (HANDBOOK / "parts/p12/sat-and-certificates.tex").read_text(
            encoding="utf-8"
        )
        self.assertIn("separately authored editorial correction", text)
        self.assertIn("exact inherited Automated Reasoning chapter", text)
        self.assertIn(r"\begin{hbdefinition}{def:p12-dpll-state}", text)
        self.assertIn(r"\begin{hbtheorem}{thm:p12-dpll-correctness}", text)

    def test_separator_artifacts_are_exact_single_blank_lines(self) -> None:
        for line in (14561, 14590):
            provenance_id = f"SEP-{line:05d}-{line:05d}"
            artifact = HANDBOOK / f"restoration/inherited-{line:05d}-{line:05d}.tex"
            wrapper = HANDBOOK / f"restoration/scope-{provenance_id}.tex"
            with self.subTest(line=line):
                self.assertEqual(artifact.read_bytes(), b"\n")
                self.assertEqual(
                    wrapper.read_text(encoding="utf-8"),
                    f"\\begin{{inheritedrestorationscope}}{{{provenance_id}}}\n"
                    f"\\input{{restoration/inherited-{line:05d}-{line:05d}}}\n"
                    "\\end{inheritedrestorationscope}\n",
                )


if __name__ == "__main__":
    unittest.main()
