#!/usr/bin/env python3
"""Fail-closed route/history tests for exact source lines 11354--11960."""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
INTERVALS = (
    (11354, 11413), (11414, 11505), (11506, 11519), (11520, 11598),
    (11599, 11627), (11628, 11644), (11645, 11695), (11696, 11710),
    (11711, 11740), (11741, 11767), (11768, 11823), (11824, 11881),
    (11882, 11913), (11914, 11960),
)
RESTORATION_INPUTS = [
    f"restoration/scope-SRC-{start:05d}-{end:05d}"
    for start, end in INTERVALS
]


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


class Part7ReaderRouteTests(unittest.TestCase):
    def test_exact_wrappers_and_open_additions_have_one_source_order_route(self) -> None:
        direct = inputs(HANDBOOK / "parts/p07.tex")
        expected = (
            RESTORATION_INPUTS[:8]
            + ["parts/p07/calculi-and-derivability-supplement"]
            + RESTORATION_INPUTS[8:]
            + [
                "parts/p07/cut-elimination-and-interpolation-supplement",
                "restoration/scope-SRC-11961-12029",
                "restoration/scope-SRC-12030-12100",
                "restoration/scope-SRC-12101-12132",
                "restoration/scope-SRC-12133-12217",
                "restoration/scope-SRC-12218-12248",
                "parts/p07/normalization-and-curry-howard-supplement",
            ]
            + [
                "parts/p07/lambda-calculi-and-type-theories",
                "parts/p07/arithmetic-proof-theory-supplement",
                "parts/p07/functional-interpretations",
                "parts/p07/structural-extensions",
                "parts/p07/proof-complexity",
            ]
        )
        self.assertEqual(direct, expected)
        text = (HANDBOOK / "parts/p07.tex").read_text(encoding="utf-8")
        self.assertEqual(
            text.count(
                r"\part{Proof Theory, Lambda Calculi, and Higher-Order Logic}"
                r"\label{part:p07}"
            ),
            1,
        )
        self.assertIn("generated/audit-p07 is intentionally OPEN and unrouted", text)
        self.assertNotIn("parts/p07/calculi-and-derivability", direct)
        self.assertNotIn("parts/p07/cut-elimination-and-interpolation", direct)

    def test_historical_bodies_and_annexes_are_exact_and_unreachable(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        pins = {
            "parts/p07/calculi-and-derivability.tex":
                "a9a44a5b20aed82c412894750808c363c588d5b18b3695e3f7f4cf0af23c2ffd",
            "parts/p07/cut-elimination-and-interpolation.tex":
                "02d5b4791bb9392f0e86095559a7539d4ad75c05abad5729f0f3e36a078fc8f1",
            "annex/p07/calculi-and-cut-elimination.tex":
                "ec9cbe318f783a3dbf343bf065dd56a8a39ab51b87b0f11b1fae11f777923fd7",
            "annex/p07/interpolation.tex":
                "257a3c6df73e5f7011c119fc1ffbbb4d4312ce03dd119bb06eb7bdf6272fd97f",
        }
        for relative, digest in pins.items():
            with self.subTest(relative=relative):
                path = HANDBOOK / relative
                self.assertEqual(sha256(path.read_bytes()), digest)
                self.assertNotIn(path.resolve(), route)

    def test_calculus_additions_are_exactly_bounded_and_consumer_corrected(self) -> None:
        original_path = HANDBOOK / "parts/p07/calculi-and-derivability.tex"
        lines = original_path.read_text(encoding="utf-8").splitlines(keepends=True)
        supplement = HANDBOOK / "parts/p07/calculi-and-derivability-supplement.tex"

        soundness = "".join(lines[78:90])
        self.assertEqual(len(soundness.encode()), 670)
        self.assertEqual(
            sha256(soundness.encode()),
            "9e97a4fdcbb657bda3d053e50ea59112c61b484138fd0a3353b13b67fa67f5c4",
        )
        self.assertEqual(marked(supplement, "SLICE", 79, 90), soundness)

        addition = "".join(lines[131:318])
        self.assertEqual(len(addition.encode()), 9875)
        self.assertEqual(
            sha256(addition.encode()),
            "0ef20a44bfe6fd42a93ee66b68d2f3156934d7fef492d580ded6dd9a234a6d16",
        )
        expected = addition.replace(
            r"Theorem~\ref{thm:p07-cut-elimination}",
            r"Chapter~\ref{ch:cut-elimination}",
        ).replace(
            "sec:p07-normalization-and-curry-howard",
            "ch:normalization-curry-howard",
        )
        derivative = marked(supplement, "DERIVATIVE", 132, 318)
        self.assertEqual(derivative, expected)
        self.assertEqual(len(derivative.encode()), 9856)
        self.assertEqual(
            sha256(derivative.encode()),
            "abcb91e5dd4a728219de4dd56666f73e04f5f977c6d0cde1ef5b86dc750c8c8d",
        )

        annex_lines = (
            HANDBOOK / "annex/p07/calculi-and-cut-elimination.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        annex = "".join(annex_lines[4:35])
        self.assertEqual(len(annex.encode()), 1934)
        self.assertEqual(
            sha256(annex.encode()),
            "629cd2f170b3bf5b1ca8c66a9f84410ecbab562109afba2af5badd70b80b8e29",
        )
        self.assertEqual(
            marked(
                HANDBOOK / "annex/p07/calculi-and-cut-elimination-supplement.tex",
                "SLICE",
                5,
                35,
            ),
            annex,
        )

    def test_cut_and_interpolation_additions_are_exactly_bounded(self) -> None:
        original_path = HANDBOOK / "parts/p07/cut-elimination-and-interpolation.tex"
        lines = original_path.read_text(encoding="utf-8").splitlines(keepends=True)
        supplement = HANDBOOK / "parts/p07/cut-elimination-and-interpolation-supplement.tex"
        for start, end, size, digest in (
            (133, 220, 4440, "a378509ce819fe86a6e2877df6e6b7861576d162de146bc35698e1c6798c8cb8"),
            (253, 272, 1217, "260c4814ee46b4ee8e3376e8b07294c9745acec8110f05680d5b5cf7435614ce"),
        ):
            block = "".join(lines[start - 1:end])
            self.assertEqual(len(block.encode()), size)
            self.assertEqual(sha256(block.encode()), digest)
            self.assertEqual(marked(supplement, "SLICE", start, end), block)

        annex_path = HANDBOOK / "annex/p07/interpolation.tex"
        annex_lines = annex_path.read_text(encoding="utf-8").splitlines(keepends=True)
        annex = "".join(annex_lines[2:23])
        self.assertEqual(len(annex.encode()), 1283)
        self.assertEqual(
            sha256(annex.encode()),
            "cd543038bd86fc4372d1341d185b3eaf0ab22e730307ce313e427387ebc211ee",
        )
        self.assertEqual(
            marked(
                HANDBOOK / "annex/p07/interpolation-supplement.tex",
                "SLICE",
                3,
                23,
            ),
            annex,
        )

    def test_annex_routes_only_the_bounded_additions(self) -> None:
        self.assertEqual(
            inputs(HANDBOOK / "annex/p07.tex"),
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
            "sec:p07-calculi-and-derivability",
            "def:p07-contexts",
            "def:p07-classical-intuitionistic-sequents",
            "def:p07-lkd-derivation",
            "def:p07-sequent-levels",
            "def:p07-rule-standing",
            "def:p07-principal-formula",
            "sec:p07-cut-elimination-and-interpolation",
            "def:p07-mix-measure",
            "thm:p07-cut-mix-equivalence",
            "def:p07-cut-elimination-method",
            "thm:p07-cut-elimination",
            "def:p07-cut-proof-boundary",
            "def:p07-analytic-derivation",
            "thm:p07-cut-free-subformula",
            "thm:p07-propositional-analytic-existence",
            "thm:p07-empty-sequent",
            "def:p07-cut-free-search",
            "thm:p07-craig-interpolation",
            "thm:p07-beth-definability",
            "annex:p7.cut.1",
            "annex:p7.cut.2",
            "annex:p7.cut.3",
            "annex:p7.cut.4",
            "annex:p7.cut.5",
        }
        for label in retired:
            with self.subTest(label=label):
                self.assertNotIn(label, live_labels)
        for label in (
            "part:proof-theory",
            "ch:lk-lj",
            "ch:cut-elimination",
            "lem:cut-mix-equipollence",
            "lem:cutfree-subformula",
            "thm:craig-interpolation",
            "thm:beth",
            "thm:p07-lkd-soundness",
            "thm:p07-lk-presentation-equivalence",
            "thm:p07-maehara-partition",
            "annex:p7.calculi.1",
            "annex:p7.calculi.2",
            "annex:p7.interp.1",
        ):
            with self.subTest(live_label=label):
                self.assertEqual(live_labels.count(label), 1)

    def test_downstream_consumers_use_genuine_exact_or_distinct_addition_labels(self) -> None:
        consumer = (HANDBOOK / "parts/p07/proof-complexity.tex").read_text(
            encoding="utf-8"
        )
        for retired in (
            "thm:p07-cut-mix-equivalence",
            "thm:p07-cut-elimination",
            "thm:p07-cut-free-subformula",
            "thm:p07-propositional-analytic-existence",
            "thm:p07-empty-sequent",
            "thm:p07-craig-interpolation",
            "thm:p07-beth-definability",
            "annex:p7.cut.1",
            "annex:p7.cut.2",
            "annex:p7.cut.3",
            "annex:p7.cut.4",
            "annex:p7.cut.5",
        ):
            self.assertNotIn(retired, consumer)
        for genuine in (
            "lem:cut-mix-equipollence",
            "ch:cut-elimination",
            "lem:cutfree-subformula",
            "sec:cut-elimination-02",
            "thm:craig-interpolation",
            "thm:beth",
        ):
            self.assertIn(genuine, consumer)


if __name__ == "__main__":
    unittest.main()
