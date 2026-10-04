#!/usr/bin/env python3
"""Fail-closed route/history tests for exact source lines 11961--12248."""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
RESTORATION_IDS = (
    "SRC-11961-12029",
    "SRC-12030-12100",
    "SRC-12101-12132",
    "SRC-12133-12217",
    "SRC-12218-12248",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def inputs(path: Path) -> list[str]:
    return [
        match.group(1).strip().removesuffix(".tex")
        for match in re.finditer(
            r"\\input\s*\{([^{}]+)\}", path.read_text(encoding="utf-8")
        )
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


def marked(path: Path, kind: str, start: int, end: int) -> str:
    match = re.search(
        rf"(?s)% BEGIN HISTORICAL {kind} {start}-{end}\n"
        rf"(.*?)% END HISTORICAL {kind} {start}-{end}",
        path.read_text(encoding="utf-8"),
    )
    if match is None:
        raise AssertionError(f"missing {kind.lower()} {start}-{end} in {path}")
    return match.group(1)


def declared_labels(text: str) -> list[str]:
    labels = re.findall(r"\\label\s*\{([^{}]+)\}", text)
    labels.extend(
        re.findall(
            r"\\begin\{(?:hb(?:convention|definition|theorem|warning|example|"
            r"corollary|method|lemma)|proofboundary|annexitem)\}\{([^{}]+)\}",
            text,
        )
    )
    return labels


class Part7NormalizationRouteTests(unittest.TestCase):
    def test_five_exact_wrappers_precede_only_bounded_additions(self) -> None:
        direct = inputs(HANDBOOK / "parts/p07.tex")
        first = direct.index("restoration/scope-SRC-11961-12029")
        expected = [f"restoration/scope-{item}" for item in RESTORATION_IDS]
        self.assertEqual(direct[first:first + 5], expected)
        self.assertEqual(
            direct[first + 5:first + 9],
            [
                "parts/p07/normalization-and-curry-howard-supplement",
                "parts/p07/lambda-calculi-and-type-theories",
                "parts/p07/arithmetic-proof-theory-supplement",
                "parts/p07/functional-interpretations",
            ],
        )
        self.assertNotIn("parts/p07/normalization-and-curry-howard", direct)
        self.assertNotIn("parts/p07/arithmetic-proof-theory", direct)
        for item in expected:
            self.assertEqual(direct.count(item), 1)

    def test_historical_bodies_and_annexes_are_exact_and_unreachable(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        pins = {
            "parts/p07/normalization-and-curry-howard.tex":
                "6aca2a57c14b65dce494f358ffd9116b19a765536e5a7f70bc2ce640fd120be0",
            "annex/p07/normalization.tex":
                "1f2d4449f7afb5d79e3551464cb050d9c396df1b9e561730221b3511e7a4f951",
            "parts/p07/arithmetic-proof-theory.tex":
                "f25320abf78d1ee9465126b4a81ee261af2cabfc1e05ad9325119e1b593992f7",
            "annex/p07/arithmetic-proof-theory.tex":
                "db6ec58dda1c4b887595fda70fe5f9c51b27147a338bf185a63061bc9cae6149",
        }
        for relative, digest in pins.items():
            with self.subTest(relative=relative):
                path = HANDBOOK / relative
                self.assertEqual(sha256(path.read_bytes()), digest)
                self.assertNotIn(path.resolve(), route)

    def test_categorical_addition_is_exactly_bounded(self) -> None:
        original = (
            HANDBOOK / "parts/p07/normalization-and-curry-howard.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        block = "".join(original[149:358])
        self.assertEqual(len(block.encode()), 9404)
        self.assertEqual(
            sha256(block.encode()),
            "766e093552892212d3b773613fdc778c281253b749420d3c66a60390d0d4be49",
        )
        supplement = HANDBOOK / "parts/p07/normalization-and-curry-howard-supplement.tex"
        self.assertEqual(marked(supplement, "SLICE", 150, 358), block)

    def test_arithmetic_additions_exclude_the_duplicate_source_theorem_and_boundary(self) -> None:
        original = (
            HANDBOOK / "parts/p07/arithmetic-proof-theory.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        supplement = HANDBOOK / "parts/p07/arithmetic-proof-theory-supplement.tex"
        for start, end, size, digest in (
            (7, 46, 2092, "375bd6ffd54303767d4aaa411df0618907256ccac91475a74841159dd86a5a42"),
            (65, 95, 1532, "906a944c038a33f8da5e1c78a0af4cb5df5f5286cc2d282c3269007e7169cfc3"),
            (110, 110, 273, "a78a6c0db712103e7a4cf92bbde81e4ef0d89403fe12a469f877648a2095dda2"),
        ):
            block = "".join(original[start - 1:end])
            self.assertEqual(len(block.encode()), size)
            self.assertEqual(sha256(block.encode()), digest)
            self.assertEqual(marked(supplement, "SLICE", start, end), block)

        addition = "".join(original[111:309])
        self.assertEqual(len(addition.encode()), 10586)
        self.assertEqual(
            sha256(addition.encode()),
            "3cc005114948552403b6d19cff86326f58556b0e41c26f55c6d8f20bb25ab810",
        )
        expected = addition.replace(
            r"Theorem~\ref{thm:p07-gentzen-consistency}",
            r"Section~\ref{sec:normalization-curry-howard-04}",
        )
        derivative = marked(supplement, "DERIVATIVE", 112, 309)
        self.assertEqual(derivative, expected)
        self.assertEqual(len(derivative.encode()), 10592)
        self.assertEqual(
            sha256(derivative.encode()),
            "d9a52d0f144bb0de117703c5140b676b8df6b43c802f5d5cf2fab7512c2b8df5",
        )

    def test_annex_removes_source_duplicate_normalization_and_arithmetic_fragments(self) -> None:
        direct = inputs(HANDBOOK / "annex/p07.tex")
        self.assertEqual(
            direct,
            [
                "annex/p07/calculi-and-cut-elimination-supplement",
                "annex/p07/interpolation-supplement",
                "annex/p07/lambda-calculi",
                "annex/p07/functional-interpretations",
            ],
        )

    def test_retired_overlap_labels_have_no_reachable_aliases(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        live_labels = declared_labels(live)
        retired = {
            "sec:p07-normalization-and-curry-howard",
            "def:p07-abstract-reduction",
            "def:p07-weak-not-strong",
            "def:p07-nj-normality",
            "def:p07-normalization-method",
            "thm:p07-normalization",
            "def:p07-normalization-proof-boundary",
            "def:p07-stlc",
            "thm:p07-stlc-subject-reduction",
            "thm:p07-stlc-strong-normalization",
            "def:p07-normalization-distinctions",
            "def:p07-k-term-weakening",
            "thm:p07-gentzen-consistency",
            "def:p07-gentzen-proof-boundary",
            "annex:p7.norm.1",
            "annex:p7.norm.2",
            "annex:p7.norm.3",
        }
        for label in retired:
            with self.subTest(label=label):
                self.assertNotIn(label, live_labels)
        for label in (
            "ch:normalization-curry-howard",
            "sec:normalization-curry-howard-01",
            "sec:normalization-curry-howard-02",
            "sec:normalization-curry-howard-03",
            "sec:normalization-curry-howard-04",
            "ex:normalization-curry-howard-01",
            "ex:normalization-curry-howard-02",
            "ex:normalization-curry-howard-03",
            "def:p07-curry-howard",
            "tab:p07-curry-howard",
            "fig:p07-curry-howard-triangle",
            "fig:p07-stlc-nd-derivation",
            "sec:p07-arithmetic-proof-theory",
            "def:p07-gentzen-reduction-method",
            "tab:p07-gentzen-components",
            "def:p07-pra",
            "thm:p07-feferman-schuette",
        ):
            with self.subTest(live_label=label):
                self.assertEqual(live_labels.count(label), 1)

    def test_downstream_consumers_use_exact_sections_or_distinct_additions(self) -> None:
        paths = (
            "parts/p07/calculi-and-derivability-supplement.tex",
            "parts/p07/lambda-calculi-and-type-theories.tex",
            "parts/p07/proof-complexity.tex",
            "parts/p08/intuitionistic-supplement.tex",
            "parts/p12/further-reading.tex",
            "parts/p12/interactive-proof.tex",
        )
        text = "\n".join((HANDBOOK / path).read_text(encoding="utf-8") for path in paths)
        for retired in (
            "sec:p07-normalization-and-curry-howard",
            "def:p07-stlc",
            "thm:p07-normalization",
            "def:p07-normalization-proof-boundary",
            "thm:p07-stlc-subject-reduction",
            "thm:p07-stlc-strong-normalization",
            "annex:p7.norm.1",
            "annex:p7.norm.2",
            "annex:p7.norm.3",
            "thm:p07-gentzen-consistency",
        ):
            self.assertNotIn(retired, text)
        for genuine in (
            "ch:normalization-curry-howard",
            "sec:normalization-curry-howard-01",
            "sec:normalization-curry-howard-02",
            "sec:normalization-curry-howard-04",
            "def:p07-curry-howard",
        ):
            self.assertIn(genuine, text)


if __name__ == "__main__":
    unittest.main()
