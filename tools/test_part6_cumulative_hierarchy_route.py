#!/usr/bin/env python3
"""Fail-closed route/history tests for exact source lines 10353--10674."""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def inputs(path: Path) -> list[str]:
    return [
        match.group(1).strip().removesuffix(".tex")
        for match in re.finditer(r"\\input\s*\{([^{}]+)\}", path.read_text(encoding="utf-8"))
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


def marked_slice(path: Path, start: int, end: int) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        rf"(?s)% BEGIN HISTORICAL SLICE {start}-{end}\n"
        rf"(.*?)% END HISTORICAL SLICE {start}-{end}",
        text,
    )
    if match is None:
        raise AssertionError(f"missing historical slice {start}-{end} in {path}")
    return match.group(1)


def declared_labels(text: str) -> list[str]:
    labels = re.findall(r"\\label\s*\{([^{}]+)\}", text)
    labels.extend(
        re.findall(
            r"\\begin\{(?:hb(?:convention|definition|theorem|warning|example|corollary|method)|annexitem)\}\{([^{}]+)\}",
            text,
        )
    )
    return labels


class Part6CumulativeHierarchyRouteTests(unittest.TestCase):
    def test_exact_wrappers_are_contiguous_before_distinct_open_additions(self) -> None:
        driver = HANDBOOK / "parts/p06.tex"
        expected_prefix = [
            "restoration/scope-SRC-10060-10088",
            "restoration/scope-SRC-10089-10271",
            "parts/p06/zfc-axiom-table-supplement",
            "restoration/scope-SRC-10272-10352",
            "restoration/scope-SRC-10353-10451",
            "restoration/scope-SRC-10452-10520",
            "restoration/scope-SRC-10521-10558",
            "restoration/scope-SRC-10559-10674",
            "parts/p06/ordinal-rank-supplement",
            "parts/p06/cardinals-choice-supplement",
        ]
        direct = inputs(driver)
        self.assertEqual(direct[: len(expected_prefix)], expected_prefix)
        self.assertEqual(direct.count("parts/p06/cardinal-arithmetic-supplement"), 1)
        self.assertNotIn("parts/p06/axioms-hierarchy-continuation", direct)
        self.assertNotIn("parts/p06/cardinals-choice", direct)
        self.assertNotIn("parts/p06/cardinal-arithmetic", direct)
        for restoration_id in (
            "SRC-10353-10451",
            "SRC-10452-10520",
            "SRC-10521-10558",
            "SRC-10559-10674",
        ):
            self.assertEqual(
                direct.count(f"restoration/scope-{restoration_id}"), 1
            )

    def test_historical_originals_are_exact_and_unreachable(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        pins = {
            "parts/p06/axioms-hierarchy.tex": "a6c38c9617f69a66076f56050b19d8ee04ec16ebe38cb92fe202a2dd53982fb2",
            "annex/p06/axioms-hierarchy.tex": "9d78bdea96c760449b5986dfe69aadafb48ceea3483b82e59b82c592715d8f1b",
            "parts/p06/cardinals-choice.tex": "c8fd192939632620a7665044e32fdf781928d31f70f478e94705259011613c7b",
            "parts/p06/cardinal-arithmetic.tex": "9b0f95b04f9054cf877f874dbb6714bf811539375025e70db0e80749985e3c49",
            "annex/p06/cardinals-choice.tex": "0a41cef98a376cd6dbe377771c4a173f7153fb229dbc14fcb2307a231d00e584",
        }
        for relative, digest in pins.items():
            with self.subTest(relative=relative):
                path = HANDBOOK / relative
                self.assertEqual(sha256(path.read_bytes()), digest)
                self.assertNotIn(path.resolve(), route)

    def test_open_additions_are_exactly_bounded_historical_derivatives(self) -> None:
        axioms = (HANDBOOK / "parts/p06/axioms-hierarchy.tex").read_text(
            encoding="utf-8"
        ).splitlines(keepends=True)
        ordinal = HANDBOOK / "parts/p06/ordinal-rank-supplement.tex"
        for start, end, digest in (
            (288, 460, "865a59b69247ed329c09a56dffd161a620a81ff225ce1b01ecabcd289ede2eeb"),
            (505, 514, "b557cdf0ac75bfaea80099d22df0d62988d4f4ba540d6ea5711e9fb63a83293c"),
            (530, 564, "8ba8cb6652dc76ba56f16012f65cec826bdb92da0216946abbd75c1895e0d2fa"),
        ):
            block = "".join(axioms[start - 1 : end])
            self.assertEqual(sha256(block.encode()), digest)
            self.assertEqual(marked_slice(ordinal, start, end), block)

        choice_original = (HANDBOOK / "parts/p06/cardinals-choice.tex").read_text(
            encoding="utf-8"
        ).splitlines(keepends=True)
        choice = HANDBOOK / "parts/p06/cardinals-choice-supplement.tex"
        for start, end, digest in (
            (1, 99, "ed5096ce831a2de07d4e8cd5c712eb3f6baceaec085f5910966c000c9a3559c5"),
            (142, 143, "c056ddab8bc84f9e65f673978d07dcd9be93205dbc432d788d1779a8b8f767db"),
        ):
            block = "".join(choice_original[start - 1 : end])
            self.assertEqual(sha256(block.encode()), digest)
            self.assertEqual(marked_slice(choice, start, end), block)
        original_choice_depth = "".join(choice_original[165:470])
        corrected_choice_depth = original_choice_depth.replace(
            "Definition~\\ref{def:p06-equipotence-comparison}",
            "Section~\\ref{sec:cumulative-hierarchy-04}",
        )
        self.assertEqual(marked_slice(choice, 166, 470), corrected_choice_depth)

        arithmetic_original = (
            HANDBOOK / "parts/p06/cardinal-arithmetic.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        arithmetic = HANDBOOK / "parts/p06/cardinal-arithmetic-supplement.tex"
        for start, end, digest in (
            (1, 57, "4f580643a45db61e678729be03941a051245bd296e79705508e91e86b83a2fae"),
            (92, 182, "ecfeafb22ea562bb29f3d48f7262b9a7f0e55158ead89da9aba2abeb419cc918"),
            (186, 221, "7a54a6f3575f06d2fbb92afc2d0c563eab80d66f4119d9fdc69f54624b16ccbe"),
        ):
            block = "".join(arithmetic_original[start - 1 : end])
            self.assertEqual(sha256(block.encode()), digest)
            self.assertEqual(marked_slice(arithmetic, start, end), block)
        arithmetic_text = arithmetic.read_text(encoding="utf-8")
        self.assertIn(r"\begin{hbdefinition}{def:p06-beth-hierarchy}{Beth hierarchy}", arithmetic_text)
        self.assertNotIn("def:p06-aleph-beth-continuum", arithmetic_text)

    def test_annex_keeps_only_distinct_choice_proofs(self) -> None:
        route = HANDBOOK / "annex/p06-route.tex"
        self.assertEqual(
            inputs(route),
            [
                "annex/p06/cardinals-choice-supplement",
                "annex/p06/constructibility-forcing",
                "annex/p06/infinitary-combinatorics",
            ],
        )
        original = (HANDBOOK / "annex/p06/cardinals-choice.tex").read_text(
            encoding="utf-8"
        ).splitlines(keepends=True)
        block = "".join(original[16:79])
        self.assertEqual(
            sha256(block.encode()),
            "8d95f4d771a553171d2b4d49ace9e9f9e66566f7386de0df0db818e3ffb821f8",
        )
        supplement = HANDBOOK / "annex/p06/cardinals-choice-supplement.tex"
        self.assertEqual(marked_slice(supplement, 17, 79), block)

    def test_retired_overlap_labels_have_no_reachable_aliases(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        live_labels = declared_labels(live)
        retired = {
            "sec:p06-ordinals",
            "def:p06-ordinal-standing",
            "thm:p06-ordinal-trichotomy",
            "thm:p06-transfinite-induction",
            "thm:p06-transfinite-recursion",
            "annex:p6.ordinals.1",
            "annex:p6.ordinals.2",
            "annex:p6.ordinals.3",
            "sec:p06-cumulative-hierarchy",
            "def:p06-cumulative-hierarchy",
            "thm:p06-hierarchy",
            "def:p06-rank",
            "def:p06-first-hierarchy-levels",
            "def:p06-well-founded-extensional-relation",
            "thm:p06-mostowski-collapse",
            "annex:p6.hierarchy.1",
            "annex:p6.hierarchy.2",
            "def:p06-equipotence-comparison",
            "def:p06-hartogs-number",
            "thm:p06-hartogs",
            "def:p06-cardinal-notation-choice",
            "def:p06-order-vocabulary",
            "annex:p6.card.1",
            "def:p06-aleph-beth-continuum",
        }
        for label in retired:
            with self.subTest(label=label):
                self.assertNotIn(label, live_labels)
        for label in (
            "ch:cumulative-hierarchy",
            "sec:cumulative-hierarchy-01",
            "sec:cumulative-hierarchy-02",
            "sec:cumulative-hierarchy-03",
            "sec:cumulative-hierarchy-04",
            "ex:cumulative-hierarchy-01",
            "ex:cumulative-hierarchy-02",
            "ex:cumulative-hierarchy-03",
            "thm:p06-rank-recursion",
            "fig:p06-cumulative-hierarchy",
            "thm:p06-zorn",
        ):
            with self.subTest(live_label=label):
                self.assertEqual(live_labels.count(label), 1)


if __name__ == "__main__":
    unittest.main()
