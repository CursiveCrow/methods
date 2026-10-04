#!/usr/bin/env python3
"""Fail-closed route/history tests for exact source lines 10675--11353."""

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
        (10675, 10769), (10770, 10825), (10826, 10881), (10882, 10899),
        (10900, 10988), (10989, 11011), (11012, 11052), (11053, 11103),
        (11104, 11126), (11127, 11199), (11200, 11239), (11240, 11279),
        (11280, 11293), (11294, 11314), (11315, 11337), (11338, 11353),
    )
)


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
    match = re.search(
        rf"(?s)% BEGIN HISTORICAL SLICE {start}-{end}\n"
        rf"(.*?)% END HISTORICAL SLICE {start}-{end}",
        path.read_text(encoding="utf-8"),
    )
    if match is None:
        raise AssertionError(f"missing historical slice {start}-{end} in {path}")
    return match.group(1)


def declared_labels(text: str) -> list[str]:
    labels = re.findall(r"\\label\s*\{([^{}]+)\}", text)
    labels.extend(
        re.findall(
            r"\\begin\{(?:hb(?:convention|definition|theorem|warning|example|corollary|method|lemma)|proofboundary|annexitem)\}\{([^{}]+)\}",
            text,
        )
    )
    return labels


class Part6ConstructibilityForcingRouteTests(unittest.TestCase):
    def test_sixteen_wrappers_are_contiguous_before_open_additions(self) -> None:
        direct = inputs(HANDBOOK / "parts/p06.tex")
        first = direct.index("restoration/scope-SRC-10675-10769")
        expected = [f"restoration/scope-{item}" for item in RESTORATION_IDS]
        self.assertEqual(direct[first:first + len(expected)], expected)
        self.assertEqual(
            direct[first + len(expected):first + len(expected) + 3],
            [
                "parts/p06/forcing-vocabulary",
                "parts/p06/constructibility-forcing-supplement",
                "parts/p06/forcing-variants-supplement",
            ],
        )
        self.assertNotIn("parts/p06/constructibility-forcing", direct)
        self.assertNotIn("parts/p06/forcing-variants", direct)
        for item in expected:
            self.assertEqual(direct.count(item), 1)

    def test_historical_originals_are_exact_and_unreachable(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        pins = {
            "parts/p06/constructibility-forcing.tex": "aa07af766e41f5e34a76385ff3118110caf6ab5204ba4e1add8bf1179f315d03",
            "annex/p06/constructibility-forcing.tex": "53a353652500bf77b24ec0f4a1c99d9946a47cc65c8a5be5a03f53684e414ff6",
            "parts/p06/forcing-variants.tex": "5aea34290ea15571ef42051696c1d2c1e29bca4bbdc9c9a03762f7cce98932aa",
        }
        for relative, digest in pins.items():
            with self.subTest(relative=relative):
                path = HANDBOOK / relative
                self.assertEqual(sha256(path.read_bytes()), digest)
                self.assertNotIn(path.resolve(), route)

    def test_open_body_additions_are_exactly_bounded(self) -> None:
        original_path = HANDBOOK / "parts/p06/constructibility-forcing.tex"
        original = original_path.read_text(encoding="utf-8").splitlines(keepends=True)
        supplement = HANDBOOK / "parts/p06/constructibility-forcing-supplement.tex"
        for start, end, digest in (
            (87, 128, "f1d86025199d9832b919b708fb5a0e209922b5ab5dc87eec56c382e518a64e1b"),
            (296, 323, "9879364ff49786ce6996e932c1698f1eec16b649e6814f02bee0a430588bdc18"),
        ):
            block = "".join(original[start - 1:end])
            self.assertEqual(sha256(block.encode()), digest)
            self.assertEqual(marked_slice(supplement, start, end), block)
        ccc = "".join(original[323:372])
        corrected = ccc.replace(
            "Definition~\\ref{def:p06-names-extension}",
            "Section~\\ref{sec:constructibility-forcing-02}",
        )
        self.assertEqual(
            sha256(ccc.encode()),
            "b2d7873f764db6b193df43b53c01aae101bc9f4321f8c6e86340fb314efd8cd9",
        )
        self.assertEqual(marked_slice(supplement, 324, 372), corrected)

    def test_vocabulary_and_forcing_variant_additions_are_exact(self) -> None:
        vocabulary = HANDBOOK / "parts/p06/forcing-vocabulary.tex"
        self.assertEqual(
            sha256(vocabulary.read_bytes()),
            "8ce8ecd25496b7a46d824ba9f60f6afe694fb818c4f7b3dd5018ead50ba08895",
        )
        self.assertIn(vocabulary.resolve(), reachable(HANDBOOK / "main.tex"))

        original = (HANDBOOK / "parts/p06/forcing-variants.tex").read_text(
            encoding="utf-8"
        )
        expected = original.replace(
            "sec:p06-constructibility-forcing", "ch:constructibility-forcing"
        ).replace("thm:p06-ch-nonderivability", "thm:ch-nonderivability")
        derivative = HANDBOOK / "parts/p06/forcing-variants-supplement.tex"
        self.assertEqual(marked_slice(derivative, 1, 268), expected)

    def test_annex_keeps_only_distinct_ccc_and_name_counting_proofs(self) -> None:
        route = HANDBOOK / "annex/p06-route.tex"
        self.assertEqual(
            inputs(route),
            [
                "annex/p06/cardinals-choice-supplement",
                "annex/p06/constructibility-forcing-supplement",
                "annex/p06/infinitary-combinatorics",
            ],
        )
        original = (HANDBOOK / "annex/p06/constructibility-forcing.tex").read_text(
            encoding="utf-8"
        ).splitlines(keepends=True)
        block = "".join(original[89:178])
        self.assertEqual(
            sha256(block.encode()),
            "b73feecde04766c683b70104fa5fa2cf52c72000a6e5da2fe25f3d51f40830d3",
        )
        supplement = HANDBOOK / "annex/p06/constructibility-forcing-supplement.tex"
        self.assertEqual(marked_slice(supplement, 90, 178), block)

    def test_retired_overlap_labels_have_no_reachable_aliases(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        live_labels = declared_labels(live)
        retired = {
            "sec:p06-constructibility-forcing", "sec:p06-constructible-hierarchy",
            "def:p06-definable-subsets", "def:p06-constructible-hierarchy",
            "def:p06-constructible-relativization", "thm:p06-constructible-class",
            "thm:p06-l-model", "sec:p06-ctm-forcing", "def:p06-forcing-standing",
            "thm:p06-ctm-strength", "thm:p06-bounded-absoluteness",
            "def:p06-generic-filter-method", "thm:p06-generic-filter-existence",
            "def:p06-names-extension", "thm:p06-check-name-evaluation",
            "def:p06-semantic-forcing", "thm:p06-semantic-forcing-monotone",
            "thm:p06-forcing-theorem", "def:p06-forcing-proof-boundary",
            "def:p06-recursive-forcing-use", "thm:p06-cohen-new-real",
            "sec:p06-relative-consistency", "thm:p06-relativization-derivations",
            "thm:p06-ch-relative-consistency", "thm:p06-not-ch-relative-consistency",
            "thm:p06-arithmetized-ch-consistency", "thm:p06-ch-nonderivability",
            "def:p06-consistency-boundary", "annex:p6.force.1", "annex:p6.force.2",
            "annex:p6.force.3", "annex:p6.force.4", "annex:p6.force.5",
            "annex:p6.force.6", "annex:p6.force.7", "annex:p6.force.12",
            "annex:p6.force.13", "annex:p6.force.14", "annex:p6.force.15",
        }
        for label in retired:
            with self.subTest(label=label):
                self.assertNotIn(label, live_labels)
        for label in (
            "ch:constructibility-forcing", "sec:constructibility-forcing-01",
            "sec:constructibility-forcing-02", "sec:constructibility-forcing-03",
            "lem:relativization-derivations", "thm:ch-relative-consistency",
            "thm:ch-nonderivability", "ex:constructibility-forcing-01",
            "ex:constructibility-forcing-02", "thm:p06-condensation",
            "fig:p06-constructible-hierarchy", "fig:p06-forcing-extension",
            "thm:p06-ccc-preservation", "thm:p06-nice-name-counting",
            "thm:p06-many-cohen-continuum", "annex:p6.force.9",
            "annex:p6.force.10", "annex:p6.force.11",
        ):
            with self.subTest(live_label=label):
                self.assertEqual(live_labels.count(label), 1)

    def test_external_consumers_use_genuine_exact_destinations(self) -> None:
        large = (HANDBOOK / "parts/p06/large-cardinals-absoluteness.tex").read_text(
            encoding="utf-8"
        )
        variants = (HANDBOOK / "parts/p06/forcing-variants-supplement.tex").read_text(
            encoding="utf-8"
        )
        for retired in (
            "thm:p06-bounded-absoluteness", "def:p06-forcing-standing",
            "sec:p06-constructible-hierarchy", "thm:p06-ctm-strength",
        ):
            self.assertNotIn(retired, large)
        self.assertGreaterEqual(large.count("sec:constructibility-forcing-02"), 3)
        self.assertIn("sec:constructibility-forcing-01", large)
        self.assertNotIn("sec:p06-constructibility-forcing", variants)
        self.assertNotIn("thm:p06-ch-nonderivability", variants)
        self.assertEqual(variants.count("ch:constructibility-forcing"), 2)
        self.assertEqual(variants.count("thm:ch-nonderivability"), 1)


if __name__ == "__main__":
    unittest.main()
