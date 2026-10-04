#!/usr/bin/env python3
"""Fail-closed route/history tests for exact source lines 12249--12969."""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
RESTORATION_IDS = tuple(
    f"SRC-{start:05d}-{end:05d}"
    for start, end in (
        (12249, 12261), (12262, 12289), (12290, 12355), (12356, 12414),
        (12415, 12536), (12537, 12673), (12674, 12720), (12721, 12783),
        (12784, 12923), (12924, 12950), (12951, 12969),
    )
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


class HigherOrderSourceRouteTests(unittest.TestCase):
    def test_eleven_exact_wrappers_replace_the_historical_part2_body(self) -> None:
        direct = inputs(HANDBOOK / "parts/p02.tex")
        anchor = direct.index("parts/p02/first-order-logic")
        expected = [f"restoration/scope-{item}" for item in RESTORATION_IDS]
        self.assertEqual(direct[anchor + 1:anchor + 12], expected)
        self.assertEqual(
            direct[anchor + 12:anchor + 14],
            [
                "parts/p02/second-and-higher-order-logic-supplement",
                "parts/p02/variants",
            ],
        )
        self.assertNotIn("parts/p02/second-and-higher-order-logic", direct)
        self.assertNotIn("generated/audit-p02", direct)
        for item in expected:
            self.assertEqual(direct.count(item), 1)

    def test_historical_body_and_annex_are_exact_and_unreachable(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        pins = {
            "parts/p02/second-and-higher-order-logic.tex":
                "72551e0b9ef0b8051f15a5efbde7107b147607f314a1f411641157134cc60ca0",
            "annex/p02/higher-order.tex":
                "456ee135aa668118cd9184deabdb02ba02947a4ef9451045823138cb96303dc9",
        }
        for relative, digest in pins.items():
            with self.subTest(relative=relative):
                path = HANDBOOK / relative
                self.assertEqual(sha256(path.read_bytes()), digest)
                self.assertNotIn(path.resolve(), route)

    def test_translation_calculus_and_comparison_additions_are_bounded(self) -> None:
        original = (
            HANDBOOK / "parts/p02/second-and-higher-order-logic.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        supplement = HANDBOOK / "parts/p02/second-and-higher-order-logic-supplement.tex"

        calculus = "".join(original[337:436])
        self.assertEqual(len(calculus.encode()), 5014)
        self.assertEqual(
            sha256(calculus.encode()),
            "901af98fc0aa9e53f090f07ecb587db48e46aa5ba69d5575fed36e05c8833945",
        )
        self.assertEqual(marked(supplement, "SLICE", 338, 436), calculus)

        comparison = "".join(original[457:496])
        self.assertEqual(len(comparison.encode()), 2550)
        self.assertEqual(
            sha256(comparison.encode()),
            "0484fcdb6d8f15780ef70dc3ede88fb7c16661368f0d6d7d1f27fd17ca102f9f",
        )
        expected = comparison.replace(
            r"Theorem~\ref{thm:p02-sol-full-noncompact}",
            r"Section~\ref{sec:second-order-logic-04}",
        )
        derivative = marked(supplement, "DERIVATIVE", 458, 496)
        self.assertEqual(derivative, expected)
        self.assertEqual(len(derivative.encode()), 2548)
        self.assertEqual(
            sha256(derivative.encode()),
            "d04f03ed212bcb7b50fdc7dc1db3e78935ee33781fe4b1cbd891df5991b6d365",
        )

    def test_annex_retains_only_many_sorted_and_matched_calculus_additions(self) -> None:
        original = (HANDBOOK / "annex/p02/higher-order.tex").read_text(
            encoding="utf-8"
        ).splitlines(keepends=True)
        supplement = HANDBOOK / "annex/p02/higher-order-supplement.tex"

        many_sorted = "".join(original[61:100])
        self.assertEqual(len(many_sorted.encode()), 2283)
        self.assertEqual(
            sha256(many_sorted.encode()),
            "b7eafdb404bba2638d005eabc6bc8078e9d1e03a29dc266c6d2ea3314157b711",
        )
        self.assertEqual(marked(supplement, "SLICE", 62, 100), many_sorted)

        adequacy = "".join(original[130:182])
        self.assertEqual(len(adequacy.encode()), 2657)
        self.assertEqual(
            sha256(adequacy.encode()),
            "1b49dd28a398a8ffad7491e34a26de32edda6f4c2667a5a0a60e3525cd56a803",
        )
        expected = adequacy.replace(
            r"Theorem~\ref{thm:p02-sol-incidence-satisfaction}",
            r"the exact satisfaction equivalence in Section~\ref{sec:second-order-logic-05}",
        )
        derivative = marked(supplement, "DERIVATIVE", 131, 182)
        self.assertEqual(derivative, expected)
        self.assertEqual(len(derivative.encode()), 2686)
        self.assertEqual(
            sha256(derivative.encode()),
            "1317d115b67bd66346c071c55e2b205ffb2c313297221a2a3216e6f921d7d6e7",
        )

        self.assertIn("annex/p02/higher-order-supplement", inputs(HANDBOOK / "annex/p02.tex"))
        self.assertNotIn("annex/p02/higher-order", inputs(HANDBOOK / "annex/p02.tex"))

    def test_retired_overlap_labels_have_no_reachable_aliases(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        live_labels = declared_labels(live)
        retired = {
            "sec:p02-second-and-higher-order-logic", "sec:p02-sol-syntax",
            "def:p02-sol-language", "sec:p02-sol-full-semantics",
            "def:p02-sol-full-semantics", "thm:p02-sol-full-comprehension",
            "def:p02-pa2", "thm:p02-pa2-categoricity",
            "thm:p02-sol-full-noncompact", "thm:p02-sol-full-no-effective-completeness",
            "thm:p02-sol-real-categoricity", "thm:p02-sol-full-ls-failures",
            "sec:p02-sol-henkin-semantics", "def:p02-sol-henkin-structure",
            "def:p02-sol-matched-henkin", "def:p02-sol-henkin-consequence",
            "def:p02-sol-incidence-translation", "thm:p02-sol-incidence-satisfaction",
            "def:p02-sol-reachability", "def:p02-sol-semantic-parameter",
            "sec:p02-simple-type-theory", "def:p02-simple-types",
            "def:p02-type-structures", "thm:p02-typed-henkin-completeness",
            "thm:p02-typed-substitution-beta", "def:p02-typed-completeness-boundary",
            "def:p02-simple-types-polymorphism", "def:p02-simple-types-relation",
            "def:p02-type-theory-scope", "annex:p2.hol.1", "annex:p2.hol.2",
            "annex:p2.hol.3", "annex:p2.hol.4", "annex:p2.hol.6",
            "annex:p2.hol.7", "annex:p2.hol.9",
        }
        for label in retired:
            with self.subTest(label=label):
                self.assertNotIn(label, live_labels)
        for label in (
            "part:higher-order", "ch:second-order-logic",
            "sec:second-order-logic-01", "sec:second-order-logic-02",
            "sec:second-order-logic-03", "sec:second-order-logic-04",
            "thm:second-order-reals-categorical", "thm:lindstrom",
            "sec:second-order-logic-05", "ex:second-order-logic-01",
            "ex:second-order-logic-02", "ex:second-order-logic-03",
            "ch:simple-type-theory", "sec:simple-type-theory-01",
            "sec:simple-type-theory-02", "sec:simple-type-theory-03",
            "ex:simple-type-theory-01", "ex:simple-type-theory-02",
            "ex:simple-type-theory-03", "def:p02-ms-variable-guard",
            "def:p02-sol-derived-calculus", "thm:p02-sol-derived-adequacy",
            "def:p02-sol-native-boundary", "sec:p02-sol-comparison",
            "tab:p02-full-vs-henkin-sol", "annex:p2.hol.5", "annex:p2.hol.8",
        ):
            with self.subTest(live_label=label):
                self.assertEqual(live_labels.count(label), 1)

    def test_symbol_note_and_addition_consumers_use_genuine_source_sections(self) -> None:
        registry = (HANDBOOK / "registry/symbols.csv").read_text(encoding="utf-8")
        generated = (HANDBOOK / "generated/symbols-tables.tex").read_text(encoding="utf-8")
        supplement = (HANDBOOK / "parts/p02/second-and-higher-order-logic-supplement.tex").read_text(
            encoding="utf-8"
        )
        annex = (HANDBOOK / "annex/p02/higher-order-supplement.tex").read_text(
            encoding="utf-8"
        )
        for text in (registry, generated, supplement, annex):
            self.assertNotIn("def:p02-pa2", text)
            self.assertNotIn("thm:p02-sol-full-noncompact", text)
            self.assertNotIn("thm:p02-sol-incidence-satisfaction", text)
        self.assertIn("sec:second-order-logic-03", registry)
        self.assertIn("sec:second-order-logic-03", generated)
        self.assertIn("sec:second-order-logic-04", supplement)
        self.assertIn("sec:second-order-logic-05", annex)


if __name__ == "__main__":
    unittest.main()
