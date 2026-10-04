#!/usr/bin/env python3
"""Fail-closed route/history tests for exact source lines 13584--14094."""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
MANY_IDS = tuple(
    f"SRC-{start:05d}-{end:05d}"
    for start, end in (
        (13584, 13613), (13614, 13640), (13641, 13699),
        (13700, 13730), (13731, 13774), (13775, 13788),
    )
)
RELEVANCE_IDS = tuple(
    f"SRC-{start:05d}-{end:05d}"
    for start, end in (
        (13789, 13806), (13807, 13861), (13862, 13896),
        (13897, 13918), (13919, 13938), (13939, 13971),
        (13972, 14000), (14001, 14015), (14016, 14034),
        (14035, 14051), (14052, 14068), (14069, 14094),
    )
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
            r"corollary|method|lemma)|proofboundary|systementry|annexitem)\}"
            r"\{([^{}]+)\}",
            text,
        )
    )
    return labels


class ManyRelevanceSourceRouteTests(unittest.TestCase):
    def test_wrappers_replace_historical_bodies_at_two_chapter_seams(self) -> None:
        direct = inputs(HANDBOOK / "parts/p08.tex")
        conditionals = direct.index("parts/p08/conditionals-deontic-free")
        expected_many = [f"restoration/scope-{item}" for item in MANY_IDS]
        self.assertEqual(
            direct[conditionals + 1:conditionals + 8],
            expected_many + ["parts/p08/many-valued-supplement"],
        )
        relevance_anchor = conditionals + 8
        expected_relevance = [
            f"restoration/scope-{item}" for item in RELEVANCE_IDS
        ]
        self.assertEqual(
            direct[relevance_anchor:relevance_anchor + 13],
            expected_relevance + ["parts/p08/relevance-linear-supplement"],
        )
        self.assertEqual(
            direct[relevance_anchor + 13:relevance_anchor + 15],
            [
                "parts/p08/paraconsistent-and-nonmonotonic",
                "parts/p08/further-reading",
            ],
        )
        self.assertNotIn("parts/p08/many-valued-and-fuzzy", direct)
        self.assertNotIn("parts/p08/substructural", direct)

    def test_four_historical_files_are_exact_and_unreachable(self) -> None:
        pins = {
            "parts/p08/many-valued-and-fuzzy.tex":
                "717904583f7f888fc716f7fc29f88c411211a5c2fd333184c70235c0dd76f1da",
            "annex/p08/many-valued-and-fuzzy.tex":
                "c15c354b5ee52ae0fa55acceb61b2a314bca9509d871120aacb54e194eb11bfc",
            "parts/p08/substructural.tex":
                "2217b18d6e9c84748a94952a6b9d9977a1bbe3d7dbbf3a9851e7f87c02673a61",
            "annex/p08/substructural.tex":
                "3d86ce418247e23de00a07aa3bb6257b74e239dd397c374268ef75dd8b565126",
        }
        route = reachable(HANDBOOK / "main.tex")
        for relative, expected in pins.items():
            path = HANDBOOK / relative
            with self.subTest(relative=relative):
                self.assertEqual(
                    hashlib.sha256(path.read_bytes()).hexdigest(), expected
                )
                self.assertNotIn(path.resolve(), route)

        annex_inputs = inputs(HANDBOOK / "annex/p08.tex")
        self.assertIn("annex/p08/many-valued-supplement", annex_inputs)
        self.assertNotIn("annex/p08/many-valued-and-fuzzy", annex_inputs)
        self.assertNotIn("annex/p08/substructural", annex_inputs)

    def test_addition_slices_are_exact_or_consumer_corrected_only(self) -> None:
        many_path = HANDBOOK / "parts/p08/many-valued-and-fuzzy.tex"
        relevance_path = HANDBOOK / "parts/p08/substructural.tex"
        annex_path = HANDBOOK / "annex/p08/many-valued-and-fuzzy.tex"
        many_lines = many_path.read_text(encoding="utf-8").splitlines(keepends=True)
        relevance_lines = relevance_path.read_text(encoding="utf-8").splitlines(
            keepends=True
        )
        annex_lines = annex_path.read_text(encoding="utf-8").splitlines(
            keepends=True
        )
        many_supplement = HANDBOOK / "parts/p08/many-valued-supplement.tex"
        relevance_supplement = HANDBOOK / "parts/p08/relevance-linear-supplement.tex"
        annex_supplement = HANDBOOK / "annex/p08/many-valued-supplement.tex"
        self.assertEqual(
            hashlib.sha256(many_supplement.read_bytes()).hexdigest(),
            "11e11313d884af8b75b763fcba2164c02f146c24e29a039d954b9c6179801fad",
        )
        self.assertEqual(
            hashlib.sha256(relevance_supplement.read_bytes()).hexdigest(),
            "0621e68f391e83ea6c7cf9e27f48cff4d4d02f9985089381965414e696b0498f",
        )
        self.assertEqual(
            hashlib.sha256(annex_supplement.read_bytes()).hexdigest(),
            "419e488fd3b4f4665b49e54349c2654a6090088082e592caa0ac029886a26965",
        )

        pins = {
            (many_path, 90, 137): (2270, "45f0e643b9d87d004ea7c3680400ab0978c38248e4bdce802b346b076be92ce2"),
            (many_path, 180, 569): (18687, "e1d25bd0786e8243936d394759c7805ce3aaa1dd745fc5451600e4fc2e5ff7d8"),
            (relevance_path, 125, 145): (937, "4ff521ee57740d6d7c15049e6ab233d8f2dfcb1879475a8d3194d30af6622751"),
            (relevance_path, 161, 341): (8958, "50e8aba0429d877a30e590893cb2a35740ee1a0e3a686fa7e2a6843b0bf3406a"),
            (relevance_path, 398, 423): (1494, "fdd0767de5dd2e149907c020a9642eacb12e1de7d5e87579074848fc59dce16c"),
            (relevance_path, 453, 715): (12320, "70f7d925fc064171a6379893a423c704fa6777da3a2e5af324f9a4ed7e53623b"),
            (relevance_path, 716, 866): (7554, "a6dac8343c2f0f97a679569bcc09cd98987f48c841ad8be17ff7e0a5cdbe8fbe"),
            (relevance_path, 874, 894): (1142, "d89e4aa626ce674b41d461b5641748e25fb4dda76dd55e58f7a6c641cdfef574"),
            (annex_path, 39, 116): (3702, "d9c55104a86b2dcfd40924637ffdd1e999cd3e21f1776045c689e9104371cf69"),
        }
        for (path, start, end), (byte_count, digest) in pins.items():
            lines = (
                many_lines if path == many_path
                else relevance_lines if path == relevance_path
                else annex_lines
            )
            raw = "".join(lines[start - 1:end])
            with self.subTest(path=path.name, start=start, end=end):
                self.assertEqual(len(raw.encode()), byte_count)
                self.assertEqual(hashlib.sha256(raw.encode()).hexdigest(), digest)

        self.assertEqual(
            marked(many_supplement, "SLICE", 90, 137),
            "".join(many_lines[89:137]),
        )
        many_continuation = "".join(many_lines[179:569])
        self.assertEqual(
            many_continuation.count(r"Theorem~\ref{thm:p08-finite-matrix-tableau}"),
            1,
        )
        many_continuation = many_continuation.replace(
            r"Theorem~\ref{thm:p08-finite-matrix-tableau}",
            r"the finite-matrix theorem in Section~\ref{sec:many-valued-paraconsistent-02}",
        )
        old_many_note = (
            "The inherited matrix definitions, exact generic sheet, repaired theorem,\n"
            "K3/LP matrices, two countervaluations, and formal-data warning migrate v1.1\n"
            "lines 13584--13787.  The inherited proof is\n"
            "Annex~\\ref{annex:p8.matrix.1}.  The K3, LP, and FDE cards all point to the one\n"
            "real generic sheet; their finite specialization and decision arguments have\n"
            "distinct annex targets.  Finite Lukasiewicz matrices point to that sheet in\n"
            "prose, while the infinite real matrix expressly does not.\n"
        )
        new_many_note = (
            "The exact inherited chapter above supplies the matrix definitions, value-labelled\n"
            "tableau calculus, complete generic theorem and proof, exact K3/LP matrices,\n"
            "countervaluations, formal-data warning, and exercises at lines 13584--13787.\n"
            "The K3, LP, and FDE cards all point to the one real generic sheet; their\n"
            "separately retained finite specializations and decision arguments have distinct\n"
            "OPEN annex targets.  Finite Lukasiewicz matrices point to that sheet in prose,\n"
            "while the infinite real matrix expressly does not.\n"
        )
        self.assertEqual(many_continuation.count(old_many_note), 1)
        many_continuation = many_continuation.replace(old_many_note, new_many_note)
        self.assertEqual(
            marked(many_supplement, "DERIVATIVE", 180, 569), many_continuation
        )

        self.assertEqual(
            marked(relevance_supplement, "SLICE", 125, 145),
            "".join(relevance_lines[124:145]),
        )
        relevance_cards = "".join(relevance_lines[160:341])
        old_rm = r"Definition~\ref{def:p08-rm-base-structure}"
        self.assertEqual(relevance_cards.count(old_rm), 2)
        relevance_cards = relevance_cards.replace(
            old_rm, r"Section~\ref{sec:relevance-linear-02}"
        )
        self.assertEqual(
            marked(relevance_supplement, "DERIVATIVE", 161, 341),
            relevance_cards,
        )

        imll_card = "".join(relevance_lines[397:423])
        old_adequacy = (
            "  \\entryadequacy{sketched=annex:p8.imll.1}{The displayed source calculus is sound and\n"
            "    complete for the displayed algebras, and cut is admissible in its cut-free\n"
            "    fragment.  The inherited source gives only a proof sketch.}\n"
        )
        new_adequacy = (
            "  \\entryadequacy{cited=Girard1987}{The displayed source calculus is sound and\n"
            "    complete for the displayed algebras, and cut is admissible in its cut-free\n"
            "    fragment.  The exact theorem and inline proof sketch are in\n"
            "    Section~\\ref{sec:relevance-linear-03}.}\n"
        )
        self.assertEqual(imll_card.count(old_adequacy), 1)
        imll_card = imll_card.replace(old_adequacy, new_adequacy)
        self.assertEqual(
            marked(relevance_supplement, "DERIVATIVE", 398, 423), imll_card
        )
        for start, end in ((453, 715), (716, 866), (874, 894)):
            self.assertEqual(
                marked(relevance_supplement, "SLICE", start, end),
                "".join(relevance_lines[start - 1:end]),
            )

        annex = "".join(annex_lines[38:116])
        self.assertEqual(
            annex.count(r"Theorem~\ref{thm:p08-finite-matrix-tableau}"), 3
        )
        annex = annex.replace(
            "\nTheorem~\\ref{thm:p08-finite-matrix-tableau}",
            "\nThe finite-matrix theorem in Section~\\ref{sec:many-valued-paraconsistent-02}",
            1,
        ).replace(
            "card.  Theorem~\\ref{thm:p08-finite-matrix-tableau}",
            "card.  The finite-matrix theorem in Section~\\ref{sec:many-valued-paraconsistent-02}",
            1,
        ).replace(
            r"Theorem~\ref{thm:p08-finite-matrix-tableau}",
            r"the finite-matrix theorem in Section~\ref{sec:many-valued-paraconsistent-02}",
        )
        self.assertEqual(
            marked(annex_supplement, "DERIVATIVE", 39, 116), annex
        )

        for supplement in (many_supplement, relevance_supplement, annex_supplement):
            prose = supplement.read_text(encoding="utf-8")
            for heading in (
                "Necessity:", "Definition:", "Standing:", "Nonredundancy:", "Use:"
            ):
                self.assertIn(heading, prose)
        annex_prose = annex_supplement.read_text(encoding="utf-8")
        self.assertIn(
            r"Section~\ref{sec:many-valued-paraconsistent-02}", annex_prose
        )
        self.assertNotIn("Section 55.2", annex_prose)

    def test_retired_overlap_labels_have_no_reachable_aliases(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = declared_labels(live)
        retired = {
            "sec:p08-many-valued-and-fuzzy", "def:p08-logical-matrix",
            "def:p08-matrix-consequence", "def:p08-value-labelled-formula",
            "def:p08-saturated-matrix-branch", "thm:p08-finite-matrix-tableau",
            "def:p08-k3-lp-excluded-middle", "def:p08-lp-explosion",
            "def:p08-paraconsistent-consequence", "def:p08-matrix-values-formal",
            "annex:p8.matrix.1", "sec:p08-substructural",
            "def:p08-context-profile", "def:p08-rm-base-structure",
            "def:p08-rm-normal-point", "def:p08-rm-star-example",
            "def:p08-rm-irrelevant-weakening", "def:p08-relevance-proof-boundary",
            "def:p08-residuated-pomonoid", "def:p08-imll-counteralgebra",
            "def:p08-imll-bang-boundary", "def:p08-resource-metaphor",
            "annex:p8.imll.1",
        }
        for label in retired:
            with self.subTest(retired=label):
                self.assertNotIn(label, labels)

        exact = {
            "ch:many-valued-paraconsistent",
            "sec:many-valued-paraconsistent-01",
            "sec:many-valued-paraconsistent-02",
            "sec:many-valued-paraconsistent-03",
            "sec:many-valued-paraconsistent-04",
            "ex:many-valued-paraconsistent-01",
            "ex:many-valued-paraconsistent-02",
            "ch:relevance-linear", "sec:relevance-linear-01",
            "sec:relevance-linear-02", "sec:relevance-linear-03",
            "sec:relevance-linear-04", "ex:relevance-linear-01",
            "ex:relevance-linear-02", "ex:relevance-linear-03",
            "ex:relevance-linear-04",
        }
        for label in exact:
            with self.subTest(exact=label):
                self.assertEqual(labels.count(label), 1)


if __name__ == "__main__":
    unittest.main()
