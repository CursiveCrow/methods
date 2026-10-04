#!/usr/bin/env python3
"""Fail-closed route and history tests for the exact inherited Part V run."""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
PART5 = HANDBOOK / "parts" / "p05.tex"
MAIN = HANDBOOK / "main.tex"

FIRST_WRAPPERS = (
    "09080-09098",
    "09099-09111",
    "09112-09149",
    "09150-09174",
    "09175-09187",
    "09188-09261",
    "09262-09327",
    "09328-09438",
)
SECOND_WRAPPERS = (
    "09439-09497",
    "09498-09538",
    "09539-09619",
    "09620-09728",
    "09729-09749",
    "09750-09816",
    "09817-09876",
    "09877-09924",
    "09925-09992",
    "09993-10027",
    "10028-10059",
)
BODY_SUPPLEMENT = "parts/p05/models-and-interpretability-supplement"
ANNEX_ROUTE = "annex/p05-route"
ANNEX_SUPPLEMENT = "annex/p05/depth-completion-supplement"

HISTORICAL = {
    "parts/p05/diagonalization.tex": (
        16436,
        "63dc7704391e0cfd6c9bfa07465b0dfa905112f612f57a0b35932f2810c9dfb4",
    ),
    "parts/p05/models-and-interpretability.tex": (
        12042,
        "dce02758d3950e0eeb3a1b5e621baec58eb7552294ed5ec5a843d9f0ab907a9e",
    ),
    "parts/p05/provability-truth.tex": (
        8768,
        "1ce4fca01f2e371d78c6b41a8e6dcf909c700ad959a0c0de0d2f932ccc697ac6",
    ),
    "annex/p05.tex": (
        9251,
        "aba296def30934f250036c7f2ea10c1b6cf36090ea698788a06df22423c8c4ae",
    ),
    "annex/p05/depth-completion.tex": (
        1935,
        "4325b14b8ed8f7487eef9d51e887b862619bfbcc7059fd7dd546619c2d2524c8",
    ),
}

BODY_SLICES = (
    (44, 116, 3666, "c6b18840a9d29de3b30e23a5f9c8e9df8fb16e7b967f9fc7ecbd076603b64a4f"),
    (118, 157, 1977, "913810e388368aa07d2a524987b11e7b7665a4cdf8a9c0bf15026f57c6c688d5"),
    (159, 237, 4219, "ebc76ea8d11e2e83dc4f642f3afe2788fb8de245b409965cf1fadd656c8e103a"),
)
ANNEX_SLICE = (
    16,
    34,
    1198,
    "5f6f06776c44f12d33e47339ef9172633ca1bf66d382a850eea4ddd37868a7c5",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def direct_inputs(text: str) -> list[str]:
    return [
        match.group(1).strip().removesuffix(".tex")
        for match in re.finditer(r"\\input\s*\{([^{}]+)\}", text)
    ]


def reachable(start: Path) -> set[Path]:
    seen: set[Path] = set()

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in seen:
            return
        seen.add(path)
        text = path.read_text(encoding="utf-8")
        for item in direct_inputs(text):
            child = HANDBOOK / f"{item}.tex"
            if child.exists():
                visit(child)

    visit(start)
    return seen


def declared_labels(text: str) -> set[str]:
    labels = set(re.findall(r"\\label\{([^{}]+)\}", text))
    labels.update(
        re.findall(
            r"\\begin\{hb(?:definition|theorem|lemma|corollary|warning|example|method|convention)\}"
            r"\{([^{}]+)\}",
            text,
        )
    )
    labels.update(re.findall(r"\\begin\{annexitem\}\{([^{}]+)\}", text))
    return labels


class Part5ReaderRouteTests(unittest.TestCase):
    def test_exact_part5_wrappers_and_open_addition_have_one_source_order_route(self) -> None:
        text = PART5.read_text(encoding="utf-8")
        expected = [
            *(f"restoration/scope-SRC-{item}" for item in FIRST_WRAPPERS),
            BODY_SUPPLEMENT,
            *(f"restoration/scope-SRC-{item}" for item in SECOND_WRAPPERS),
            "parts/p05/provability-logic-gl",
            "parts/p05/decidable-arithmetics",
            "parts/p05/independence-catalog",
            "parts/p05/reverse-mathematics",
        ]
        self.assertEqual(direct_inputs(text), expected)
        self.assertNotRegex(text, r"\\part(?!\*)\s*\{")
        self.assertNotRegex(text, r"\\label\s*\{part:(?:p05|incompleteness)\}")
        self.assertIn("generated/audit-p05 is intentionally OPEN and unrouted", text)

    def test_historical_part5_sources_are_exact_and_unreachable(self) -> None:
        route = reachable(MAIN)
        for relative, (size, digest) in HISTORICAL.items():
            with self.subTest(relative=relative):
                path = HANDBOOK / relative
                data = path.read_bytes()
                self.assertEqual(len(data), size)
                self.assertEqual(sha256(data), digest)
                self.assertNotIn(path.resolve(), route)

    def test_open_model_and_annex_derivatives_are_exactly_bounded(self) -> None:
        historical_body = (HANDBOOK / "parts/p05/models-and-interpretability.tex").read_bytes().splitlines(keepends=True)
        body_path = HANDBOOK / f"{BODY_SUPPLEMENT}.tex"
        body_data = body_path.read_bytes()
        self.assertEqual(len(body_data), 11448)
        self.assertEqual(
            sha256(body_data),
            "457a4d42b2834c73a88d77cfef7b7e94cc8e9574b2f85fae854b0bfc2cc9b1b0",
        )
        body = body_data.decode("utf-8")
        for start, end, size, digest in BODY_SLICES:
            with self.subTest(body_slice=(start, end)):
                original = b"".join(historical_body[start - 1 : end])
                self.assertEqual(len(original), size)
                self.assertEqual(sha256(original), digest)
                marker = rf"(?s)% BEGIN HISTORICAL SLICE {start}-{end}\n(.*?)% END HISTORICAL SLICE {start}-{end}"
                match = re.search(marker, body)
                self.assertIsNotNone(match)
                expected = original.decode("utf-8")
                if (start, end) == (118, 157):
                    expected = expected.replace(
                        r"Definition~\ref{def:p05-proof-predicate}",
                        r"Definition~\ref{def:fixed-proof-predicate}",
                    )
                self.assertEqual(match.group(1), expected)

        historical_annex = (HANDBOOK / "annex/p05/depth-completion.tex").read_bytes().splitlines(keepends=True)
        start, end, size, digest = ANNEX_SLICE
        original = b"".join(historical_annex[start - 1 : end])
        self.assertEqual(len(original), size)
        self.assertEqual(sha256(original), digest)
        annex_path = HANDBOOK / f"{ANNEX_SUPPLEMENT}.tex"
        annex_data = annex_path.read_bytes()
        self.assertEqual(len(annex_data), 2284)
        self.assertEqual(
            sha256(annex_data),
            "65dc26a7b13192750efca27c54b3516fc488228162da22ae74e45dc0c75ce907",
        )
        annex = annex_data.decode("utf-8")
        match = re.search(
            rf"(?s)% BEGIN HISTORICAL SLICE {start}-{end}\n(.*?)% END HISTORICAL SLICE {start}-{end}",
            annex,
        )
        self.assertIsNotNone(match)
        expected = original.decode("utf-8").replace(
            r"Section~\ref{sec:p05-diagonalization-prereq}",
            r"Section~\ref{sec:arithmetic-coding-01}",
        )
        self.assertEqual(match.group(1), expected)

    def test_annex_routes_only_the_distinct_open_depth_detail(self) -> None:
        main = MAIN.read_text(encoding="utf-8")
        self.assertEqual(main.count(r"\input{annex/p05-route}"), 1)
        self.assertNotIn(r"\input{annex/p05}", main.replace(r"\input{annex/p05-route}", ""))
        route = (HANDBOOK / f"{ANNEX_ROUTE}.tex").read_text(encoding="utf-8")
        self.assertEqual(direct_inputs(route), [ANNEX_SUPPLEMENT])
        self.assertEqual(route.count(r"\label{annex:p05}"), 1)

    def test_retired_part5_overlap_labels_are_absent_without_aliases(self) -> None:
        historical_text = "\n".join(
            (HANDBOOK / relative).read_text(encoding="utf-8")
            for relative in HISTORICAL
        )
        allowed = {
            "annex:p05",
            "annex:p5.sigma.1",
            "thm:p05-sigma-one-completeness",
            "def:p05-finite-distance-block",
            "thm:p05-countable-pa-order-type",
            "thm:p05-overspill",
            "def:p05-overspill-below",
            "thm:p05-tennenbaum",
            "def:p05-sigma-one-witness",
            "def:p05-completeness-soundness",
            "def:p05-relative-interpretation",
            "def:p05-essential-undecidability",
            "thm:p05-interpretation-transfer",
            "def:p05-interpretation-examples",
        }
        retired = declared_labels(historical_text) - allowed
        reachable_text = "\n".join(
            path.read_text(encoding="utf-8") for path in reachable(MAIN)
        )
        for label in sorted(retired):
            with self.subTest(label=label):
                self.assertNotRegex(
                    reachable_text,
                    rf"\\(?:label|ref|cref|Cref|autoref|pageref)\s*\{{{re.escape(label)}\}}",
                )

    def test_external_consumers_use_exact_or_distinct_live_destinations(self) -> None:
        arithmetic = (HANDBOOK / "parts/p07/arithmetic-proof-theory.tex").read_text(encoding="utf-8")
        catalog = (HANDBOOK / "parts/p05/independence-catalog.tex").read_text(encoding="utf-8")
        self.assertNotIn("def:p05-peano-arithmetic", arithmetic)
        self.assertNotIn("def:p05-robinson-q", arithmetic)
        self.assertGreaterEqual(arithmetic.count("sec:arithmetic-coding-01"), 2)
        self.assertNotIn("sec:p05-models-and-interpretability", catalog)
        self.assertIn("def:p05-relative-interpretation", catalog)


if __name__ == "__main__":
    unittest.main()
