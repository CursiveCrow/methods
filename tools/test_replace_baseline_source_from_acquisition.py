#!/usr/bin/env python3
"""Focused synthetic tests for the list-based acquisition replacer."""

from __future__ import annotations

import argparse
import tempfile
import unittest
from pathlib import Path

import replace_baseline_source_from_acquisition as subject


LEDGER_START = "## Patch-ready hierarchy-and-topic ledger"
LEDGER_END = "## Exact integration counts and deltas"
HTTPS_START = "## Patch-ready exact HTTPS locator ledger"
NON_HTTPS_START = "## Exact non-HTTPS locator ledger"
SCHEMELESS_START = "## Exact scheme-less identifier ledger"
TOPIC = "- Synthetic presentation — **OPEN**"


class ExactLedgerTests(unittest.TestCase):
    def test_exact_two_line_preamble_is_removed_without_blank_normalization(self) -> None:
        lines = [
            LEDGER_START,
            "",
            "Every bullet is one separate OPEN record. No row stands for, corrects,",
            "compresses, merges, or replaces another row.",
            "",
            "#### Synthetic hierarchy",
            "",
            TOPIC,
            "",
            LEDGER_END,
            "",
            "- Exact HTTPS locators: 1.",
        ]

        ledger, headings, topics = subject.exact_ledger(
            lines, LEDGER_START, LEDGER_END, Path("synthetic-note.md")
        )

        self.assertEqual(
            ledger,
            ["", "", "#### Synthetic hierarchy", "", TOPIC, ""],
        )
        self.assertEqual((headings, topics), (1, 1))

    def test_exact_one_line_preamble_is_removed(self) -> None:
        lines = [
            LEDGER_START,
            "",
            "Every bullet is one independently OPEN record.",
            "",
            "#### Synthetic hierarchy",
            TOPIC,
            LEDGER_END,
            "- Acquisition gate: OPEN.",
        ]

        ledger, headings, topics = subject.exact_ledger(
            lines, LEDGER_START, LEDGER_END, Path("synthetic-note.md")
        )

        self.assertEqual(ledger, ["", "", "#### Synthetic hierarchy", TOPIC])
        self.assertEqual((headings, topics), (1, 1))

    def test_rewrapped_duplicated_and_misplaced_preambles_fail_closed(self) -> None:
        bad_sections = {
            "rewrapped": [
                "Every bullet is one separate OPEN record. No row stands for, corrects, "
                "compresses, merges, or replaces another row.",
                "#### Synthetic hierarchy",
                TOPIC,
            ],
            "duplicated": [
                "Every bullet is one independently OPEN record.",
                "",
                "Every bullet is one independently OPEN record.",
                "#### Synthetic hierarchy",
                TOPIC,
            ],
            "misplaced": [
                "#### Synthetic hierarchy",
                "Every bullet is one independently OPEN record.",
                TOPIC,
            ],
        }
        for label, section in bad_sections.items():
            with self.subTest(label=label), self.assertRaises(ValueError):
                subject.exact_ledger(
                    [LEDGER_START, *section, LEDGER_END],
                    LEDGER_START,
                    LEDGER_END,
                    Path("synthetic-note.md"),
                )

    def test_known_post_ledger_administrative_rows_are_typed(self) -> None:
        administrative_rows = [
            "- Cambridge Contents rows: 1.",
            "- Crossref ISBN-query items retained in returned order: 1.",
            "- Mechanically extracted PDF tables retained: 1.",
            "- Mechanically extracted PDF table rows retained: 2.",
            "- Mechanically extracted PDF table cells retained: 3.",
            "- Patch-ledger top-level file manifestations: 1.",
            "- Prior SRC-032 baseline: 1.",
            "- Replacement delta: +1.",
        ]
        subject.exact_ledger(
            [
                LEDGER_START,
                "#### Synthetic hierarchy",
                TOPIC,
                LEDGER_END,
                "",
                *administrative_rows,
            ],
            LEDGER_START,
            LEDGER_END,
            Path("synthetic-note.md"),
        )

    def test_unknown_or_source_content_after_ledger_fails_closed(self) -> None:
        bad_tails = [
            "- Arbitrary administrative claim: 1.",
            "- Exact source presentation: theorem body copied after the boundary.",
            "- Source presentation: theorem body copied after the boundary.",
            "- Exact HTTPS locators: theorem body copied after the boundary.",
            "- Acquisition gate: CLOSED.",
            "#### Late source hierarchy",
            "- Late source presentation — **OPEN**",
            "Untyped prose after the ledger.",
        ]
        for tail in bad_tails:
            with self.subTest(tail=tail), self.assertRaises(ValueError):
                subject.exact_ledger(
                    [
                        LEDGER_START,
                        "#### Synthetic hierarchy",
                        TOPIC,
                        LEDGER_END,
                        tail,
                    ],
                    LEDGER_START,
                    LEDGER_END,
                    Path("synthetic-note.md"),
                )


class ReplacementTests(unittest.TestCase):
    @staticmethod
    def args(baseline: Path, note: Path) -> argparse.Namespace:
        return argparse.Namespace(
            baseline=baseline,
            note=note,
            source_id="SRC-999",
            https_heading=HTTPS_START,
            https_end_heading=None,
            non_https_heading=NON_HTTPS_START,
            non_https_end_heading=SCHEMELESS_START,
            ledger_heading=LEDGER_START,
            ledger_end_heading=LEDGER_END,
            scheme_less_identifier=[],
            locator_rows_have_provenance=False,
            scheme_less_heading=SCHEMELESS_START,
            scheme_less_end_heading=None,
            expected_https=1,
            expected_non_https=1,
            expected_scheme_less=2,
            expected_hierarchy=1,
            expected_h4=1,
            expected_h5=0,
            expected_h6=0,
            expected_topics=1,
        )

    @staticmethod
    def note_lines() -> list[str]:
        return [
            HTTPS_START,
            "",
            "1. `https://example.test/source`",
            "",
            NON_HTTPS_START,
            "",
            "1. `urn:typed-non-https`",
            "",
            SCHEMELESS_START,
            "",
            "1. `urn:explicitly-scheme-less`",
            "2. `ark:/explicitly-scheme-less`",
            "",
            LEDGER_START,
            "",
            "Every bullet is one independently OPEN record.",
            "",
            "#### Synthetic hierarchy",
            "",
            TOPIC,
            "",
            LEDGER_END,
            "",
            "- Exact HTTPS locators: 1.",
            "- Exact non-HTTPS locators: 1.",
            "- Exact scheme-less identifiers: 2.",
            "- Acquisition gate: OPEN.",
        ]

    def test_typed_scheme_less_colon_values_and_block_fixed_point(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            baseline = root / "baseline.md"
            note = root / "note.md"
            old_block = [
                "### SRC-999 — Synthetic source",
                "",
                "- Exact source title: *Synthetic source*",
                "- Retrieved granularity: old synthetic block",
                "",
                "#### Old hierarchy",
                "",
                "- Old topic — **OPEN**",
                "",
            ]
            baseline.write_text(
                "\n".join([*old_block, "---", ""]), encoding="utf-8", newline="\n"
            )
            note.write_text(
                "\n".join([*self.note_lines(), ""]), encoding="utf-8", newline="\n"
            )
            args = self.args(baseline, note)

            replacement = subject.build_source_block(args)

            self.assertIn(
                "- Exact scheme-less identifier 1: urn:explicitly-scheme-less",
                replacement,
            )
            self.assertIn(
                "- Exact scheme-less identifier 2: ark:/explicitly-scheme-less",
                replacement,
            )
            retrieval = next(
                index
                for index, line in enumerate(replacement)
                if line.startswith("- Retrieved granularity:")
            )
            self.assertEqual(
                replacement[retrieval + 1 : retrieval + 5],
                ["", "", "", "#### Synthetic hierarchy"],
            )

            baseline.write_text(
                "\n".join([*replacement, "---", ""]),
                encoding="utf-8",
                newline="\n",
            )
            self.assertEqual(subject.build_source_block(args), replacement)


if __name__ == "__main__":
    unittest.main()
