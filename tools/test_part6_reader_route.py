#!/usr/bin/env python3
"""Fail-closed route and history tests for the exact Part VI opening."""

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


class Part6ReaderRouteTests(unittest.TestCase):
    def test_exact_wrappers_and_open_continuations_have_one_ordered_route(self) -> None:
        driver = HANDBOOK / "parts/p06.tex"
        expected = [
            "restoration/scope-SRC-10060-10088",
            "restoration/scope-SRC-10089-10271",
            "parts/p06/zfc-axiom-table-supplement",
            "restoration/scope-SRC-10272-10352",
            "parts/p06/axioms-hierarchy-continuation",
            "parts/p06/cardinals-choice",
            "parts/p06/constructibility-forcing",
            "parts/p06/forcing-variants",
            "parts/p06/infinitary-combinatorics",
            "parts/p06/cardinal-arithmetic",
            "parts/p06/large-cardinals-absoluteness",
            "parts/p06/descriptive-set-theory",
            "parts/p06/determinacy",
        ]
        self.assertEqual(inputs(driver), expected)
        text = driver.read_text(encoding="utf-8")
        self.assertNotRegex(text, r"\\part(?!\*)\s*\{")
        self.assertNotRegex(text, r"\\label\s*\{part:(?:p06|set-theory)\}")
        self.assertIn("generated/audit-p06 is intentionally OPEN and unrouted", text)

    def test_historical_axiom_body_and_annex_are_exact_and_unreachable(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        pins = {
            "parts/p06/axioms-hierarchy.tex": "a6c38c9617f69a66076f56050b19d8ee04ec16ebe38cb92fe202a2dd53982fb2",
            "annex/p06/axioms-hierarchy.tex": "9d78bdea96c760449b5986dfe69aadafb48ceea3483b82e59b82c592715d8f1b",
        }
        for relative, digest in pins.items():
            with self.subTest(relative=relative):
                path = HANDBOOK / relative
                self.assertEqual(sha256(path.read_bytes()), digest)
                self.assertNotIn(path.resolve(), route)

    def test_a058_derivative_and_continuations_have_exact_boundaries(self) -> None:
        body = HANDBOOK / "parts/p06/axioms-hierarchy.tex"
        body_lines = body.read_text(encoding="utf-8").splitlines(keepends=True)
        original_table = "".join(body_lines[51:156])
        self.assertEqual(len(original_table.encode()), 4295)
        self.assertEqual(
            sha256(original_table.encode()),
            "fba5efe1f0a082019f53db8829905e460f417659eb2b51bd50e1d5a88481824f",
        )
        table = (HANDBOOK / "parts/p06/zfc-axiom-table-supplement.tex").read_text(encoding="utf-8")
        match = re.search(r"(?s)% BEGIN HISTORICAL SLICE 52-156\n(.*?)% END HISTORICAL SLICE 52-156", table)
        self.assertIsNotNone(match)
        expected = original_table.replace(
            "The Part~1 presentation of its identity theorem is a separate\n"
            "inherited source unit; it does not replace or discharge the distinct later\n"
            "Part~6 statement and proof identified as OPEN below.  For the Choice row, the\n",
            "The Part~1 presentation of its identity theorem is a separate\n"
            "inherited source unit; the exact Part~VI statement and proof are in\n"
            "Section~\\ref{sec:zf-zfc-02}.  For the Choice row, the\n",
        ).replace(
            "Asserts an inductive set; leastness of \\(\\omega\\) is Theorem~\\ref{thm:p06-omega-least}. \\\\\n",
            "Asserts an inductive set; the exact source definition of \\(\\omega\\) is in\n"
            "Section~\\ref{sec:zf-zfc-01}. \\\\\n",
        )
        self.assertEqual(match.group(1), expected)

        continuation = (HANDBOOK / "parts/p06/axioms-hierarchy-continuation.tex").read_text(encoding="utf-8")
        match = re.search(r"(?s)% BEGIN HISTORICAL SLICE 228-594\n(.*?)% END HISTORICAL SLICE 228-594", continuation)
        self.assertIsNotNone(match)
        original_continuation = "".join(body_lines[227:594])
        self.assertEqual(len(original_continuation.encode()), 14310)
        self.assertEqual(sha256(original_continuation.encode()), "f9ca81559954dd05a3a636230cd38553d639a107e986ee8769656784fca50c60")
        self.assertEqual(match.group(1), original_continuation)

        annex = HANDBOOK / "annex/p06/axioms-hierarchy.tex"
        annex_lines = annex.read_text(encoding="utf-8").splitlines(keepends=True)
        original_annex = "".join(annex_lines[38:113])
        self.assertEqual(len(original_annex.encode()), 4410)
        self.assertEqual(sha256(original_annex.encode()), "58f16aea977cfad500fc186905018d5926314e7d3989a8ba8f1f3b40f24e82d8")
        routed_annex = (HANDBOOK / "annex/p06/axioms-hierarchy-continuation.tex").read_text(encoding="utf-8")
        match = re.search(r"(?s)% BEGIN HISTORICAL SLICE 39-113\n(.*?)% END HISTORICAL SLICE 39-113", routed_annex)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), original_annex)

    def test_main_routes_the_new_annex_driver_only(self) -> None:
        main = (HANDBOOK / "main.tex").read_text(encoding="utf-8")
        self.assertEqual(main.count(r"\input{annex/p06-route}"), 1)
        route = HANDBOOK / "annex/p06-route.tex"
        self.assertEqual(
            inputs(route),
            [
                "annex/p06/axioms-hierarchy-continuation",
                "annex/p06/cardinals-choice",
                "annex/p06/constructibility-forcing",
                "annex/p06/infinitary-combinatorics",
            ],
        )
        self.assertEqual(route.read_text(encoding="utf-8").count(r"\label{annex:p06}"), 1)


if __name__ == "__main__":
    unittest.main()
