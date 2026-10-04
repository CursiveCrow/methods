#!/usr/bin/env python3
"""Regression checks for the live exact Part-VI ordered-pair source route."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "handbook/parts/p06.tex"
REQUIRED_OPEN_EVIDENCE = (
    "exact inherited Part VI plus bounded OPEN continuations",
    r"\input{restoration/scope-SRC-10272-10352}",
    r"\input{parts/p06/axioms-hierarchy-continuation}",
)
FALSE_DISPOSITION_PATTERNS = (
    r"must\s+be\s+restored\s+verbatim",
    r"\bretir(?:e|ed|es|ing|ement)\b",
    r"\bconsolidat(?:e|ed|es|ing|ion)\b",
    r"\b(?:need(?:s)?\s+not|does\s+not\s+need)\s+"
    r"(?:to\s+be\s+|to\s+)?(?:duplicate|duplicated|repeat|repeated|"
    r"reprint|reprinted|restore|restored|print|printed)\b",
    r"\bdeliberately\s+not\s+(?:duplicate|duplicated|repeat|repeated|"
    r"reprint|reprinted|restore|restored|print|printed)\b",
    r"\balready\s+(?:appears?|appeared|recorded|presented|printed|proved|"
    r"included|carried)\s+(?:in|by)\s+(?:the\s+)?part~?1\b",
    r"\b(?:satisfied|discharged|covered|subsumed)\s+by\s+"
    r"(?:the\s+)?part~?1\b",
)


def normalized(path: Path) -> str:
    return re.sub(r"\s+", " ", path.read_text(encoding="utf-8")).strip()


def disposition_errors(text: str) -> tuple[str, ...]:
    errors = [
        f"missing required evidence: {required}"
        for required in REQUIRED_OPEN_EVIDENCE
        if required not in text
    ]
    lowered = text.lower()
    errors.extend(
        f"forbidden authorization: {forbidden}"
        for forbidden in FALSE_DISPOSITION_PATTERNS
        if re.search(forbidden, lowered)
    )
    return tuple(errors)


class PartVIOrderedPairSourceDispositionTests(unittest.TestCase):
    def assert_exact_destination_is_live_and_admission_remains_open(self, text: str) -> None:
        self.assertEqual((), disposition_errors(text))

    def test_exact_ordered_pair_statement_and_proof_are_on_the_live_route(
        self,
    ) -> None:
        self.assert_exact_destination_is_live_and_admission_remains_open(normalized(TARGET))

    def test_retirement_consolidation_and_nonduplication_wording_is_rejected(
        self,
    ) -> None:
        valid = normalized(TARGET)
        baseline_errors = set(disposition_errors(valid))
        mutations = (
            " The later statement and proof are retired in favor of Part~1.",
            " The two source presentations are consolidated in Part~1.",
            " The Part~6 proof need not be duplicated because it already appears in Part~1.",
            " The later source obligation is satisfied by the Part~1 proof.",
        )
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                mutation_errors = set(disposition_errors(valid + mutation))
                self.assertTrue(mutation_errors - baseline_errors)


if __name__ == "__main__":
    unittest.main()
