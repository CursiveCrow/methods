#!/usr/bin/env python3
"""Adversarial public-CLI and source-occurrence tests for the SRC-025 adapter."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import replace_baseline_source_from_split_acquisition as subject


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).with_name(
    "replace_baseline_source_from_split_acquisition.py"
)
FROZEN_NOTE = ROOT / "spec/research/acquisition-src-025.md"


class Src025AdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.baseline = self.root / "baseline.md"
        self.note = FROZEN_NOTE
        self.write_old_baseline()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_old_baseline(self, extra_after_retrieval: str = "") -> None:
        self.baseline.write_text(
            "### SRC-025 — Handbook of Modal Logic\n\n"
            "- Exact work title: *Handbook of Modal Logic*\n"
            "- Editors: Patrick Blackburn; Johan van Benthem; Frank Wolter\n"
            "- Publisher metadata: 1st Edition; Volume 3; November 3, 2006\n"
            "- Official publisher source: https://shop.elsevier.com/books/handbook-of-modal-logic/blackburn/978-0-444-51690-9\n"
            "- Exact HTTPS locator 1: https://shop.elsevier.com/books/handbook-of-modal-logic/blackburn/978-0-444-51690-9\n"
            "- Retrieved granularity: old source ledger\n\n"
            f"{extra_after_retrieval}"
            "#### Publisher and printed hierarchy\n\n"
            "- `HANDBOOK OF MODAL LOGIC` — **OPEN**.\n\n"
            "### SRC-026 — Following source\n\n"
            "- Exact work title: *Following source*\n"
            "- Retrieved granularity: unchanged\n\n"
            "#### Following hierarchy\n\n"
            "- Following source topic — **OPEN**\n\n"
            "---\n",
            encoding="utf-8",
            newline="\n",
        )

    def cli(
        self,
        *,
        mode: str = "--write",
        note: Path | None = None,
        source_id: str = subject.FROZEN_SOURCE_ID,
        sha256: str = subject.FROZEN_NOTE_SHA256,
        expected_topics: int = subject.FROZEN_COUNTS["topics"],
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--baseline",
                str(self.baseline),
                "--note",
                str(note or self.note),
                "--source-id",
                source_id,
                "--expected-note-sha256",
                sha256,
                "--expected-https",
                str(subject.FROZEN_COUNTS["https"]),
                "--expected-non-https",
                str(subject.FROZEN_COUNTS["non_https"]),
                "--expected-scheme-less",
                str(subject.FROZEN_COUNTS["scheme_less"]),
                "--expected-hierarchy",
                str(subject.FROZEN_COUNTS["hierarchy"]),
                "--expected-h4",
                str(subject.FROZEN_COUNTS["h4"]),
                "--expected-h5",
                str(subject.FROZEN_COUNTS["h5"]),
                "--expected-h6",
                str(subject.FROZEN_COUNTS["h6"]),
                "--expected-topics",
                str(expected_topics),
                mode,
            ],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )

    @staticmethod
    def payload_args(note: Path) -> argparse.Namespace:
        return argparse.Namespace(
            note=note,
            expected_https=subject.FROZEN_COUNTS["https"],
            expected_non_https=subject.FROZEN_COUNTS["non_https"],
            expected_scheme_less=subject.FROZEN_COUNTS["scheme_less"],
            expected_hierarchy=subject.FROZEN_COUNTS["hierarchy"],
            expected_h4=subject.FROZEN_COUNTS["h4"],
            expected_h5=subject.FROZEN_COUNTS["h5"],
            expected_h6=subject.FROZEN_COUNTS["h6"],
            expected_topics=subject.FROZEN_COUNTS["topics"],
            scheme_less_heading=None,
            scheme_less_end_heading=None,
        )

    def mutated_note(self, lines: list[str]) -> Path:
        path = self.root / "mutated-note.md"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        return path

    def test_all_exact_source_occurrences_are_conserved_in_split_order_and_fixed_point(self) -> None:
        write = self.cli()
        self.assertEqual(write.returncode, 0, write.stderr)
        block, _ = subject.source_block_and_digest(
            self.baseline, subject.FROZEN_SOURCE_ID
        )
        retrieval = next(
            index
            for index, line in enumerate(block)
            if line.startswith("- Retrieved granularity:")
        )
        actual_records = [
            line
            for line in block[retrieval + 1 :]
            if subject.BASELINE_HIERARCHY_RE.fullmatch(line) is not None
            or line.startswith("- ")
        ]

        note = self.note.read_text(encoding="utf-8").splitlines()
        first_start = note.index(subject.FIRST_LEDGER_HEADING)
        https_start = note.index(subject.HTTPS_HEADING)
        non_https_start = note.index(subject.NON_HTTPS_HEADING)
        non_https_end = note.index(subject.NON_HTTPS_END_HEADING)
        second_start = note.index(subject.SECOND_LEDGER_HEADING)
        ledger_end = note.index(subject.LEDGER_END_HEADING)
        source_rows = [
            *note[first_start + 1 : https_start],
            *note[non_https_start + 1 : non_https_end],
            *note[second_start + 1 : ledger_end],
        ]
        expected_records = [
            f"#{line}" if subject.HIERARCHY_RE.fullmatch(line) else line
            for line in source_rows
            if subject.HIERARCHY_RE.fullmatch(line) is not None
            or line.startswith("- ")
        ]
        self.assertEqual(actual_records, expected_records)
        self.assertEqual(
            sum(line.startswith("#### ") for line in actual_records), 39
        )
        self.assertEqual(sum(line.startswith("- ") for line in actual_records), 1257)
        self.assertNotIn(subject.FIRST_LEDGER_PREAMBLE[0], block)
        self.assertNotIn(subject.FIRST_LEDGER_INTERLUDE[0], block)
        self.assertNotIn(subject.SECOND_LEDGER_INTERLUDE[0], block)

        check = self.cli(mode="--check")
        self.assertEqual(check.returncode, 0, check.stderr)

    def test_production_contract_rejects_source_count_and_digest_substitution(self) -> None:
        cases = [
            {"source_id": "SRC-999"},
            {"expected_topics": 1256},
            {"sha256": "0" * 64},
        ]
        for arguments in cases:
            with self.subTest(arguments=arguments):
                result = self.cli(**arguments)
                self.assertNotEqual(result.returncode, 0)

    def test_changed_note_is_rejected_by_frozen_digest(self) -> None:
        lines = self.note.read_text(encoding="utf-8").splitlines()
        lines[239] = lines[239].replace("HANDBOOK", "CHANGED")
        changed = self.mutated_note(lines)

        result = self.cli(note=changed)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("SHA-256 mismatch", result.stderr)

    def test_internal_interludes_and_count_bridge_are_exact_not_silently_filtered(self) -> None:
        originals = self.note.read_text(encoding="utf-8").splitlines()
        mutations = [
            (315, originals[315].replace("All 82", "All 83")),
            (859, originals[859].replace("4 part", "5 part")),
            (1666, originals[1666].replace("first acquisition", "second acquisition")),
        ]
        for index, replacement in mutations:
            lines = originals.copy()
            lines[index] = replacement
            note = self.mutated_note(lines)
            with self.subTest(line=index + 1), self.assertRaises(ValueError):
                subject.exact_note_payload(lines, self.payload_args(note))

    def test_topic_punctuation_and_non_https_scheme_are_typed(self) -> None:
        originals = self.note.read_text(encoding="utf-8").splitlines()

        topic_lines = originals.copy()
        topic_lines[239] = topic_lines[239].removesuffix(".")
        topic_note = self.mutated_note(topic_lines)
        with self.assertRaisesRegex(ValueError, "topic lacks exact"):
            subject.exact_note_payload(topic_lines, self.payload_args(topic_note))

        locator_lines = originals.copy()
        locator_lines[842] = locator_lines[842].replace("`http://", "`https://", 1)
        locator_note = self.mutated_note(locator_lines)
        with self.assertRaisesRegex(ValueError, "non-HTTPS URI scheme"):
            subject.exact_note_payload(locator_lines, self.payload_args(locator_note))

    def test_untyped_stale_block_rows_and_duplicate_target_blocks_fail_closed(self) -> None:
        self.write_old_baseline("Untyped stale presentation\n")
        untyped = self.cli()
        self.assertNotEqual(untyped.returncode, 0)
        self.assertIn("replaceable ledger line", untyped.stderr)

        typed_extras = [
            "- Extra source presentation absent from the frozen note — **OPEN**.\n",
            "#### Extra hierarchy absent from the frozen note\n",
        ]
        for extra in typed_extras:
            self.write_old_baseline(extra)
            result = self.cli()
            with self.subTest(extra=extra):
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("would discard typed occurrences", result.stderr)

        self.write_old_baseline()
        baseline_text = self.baseline.read_text(encoding="utf-8").replace(
            "- Exact HTTPS locator 1: https://shop.elsevier.com/books/handbook-of-modal-logic/blackburn/978-0-444-51690-9",
            "- Exact HTTPS locator 1: https://not-in-frozen.example/",
        )
        self.baseline.write_text(baseline_text, encoding="utf-8", newline="\n")
        locator = self.cli()
        self.assertNotEqual(locator.returncode, 0)
        self.assertIn("would discard typed occurrences", locator.stderr)

        self.write_old_baseline()
        wrong_identity = self.baseline.read_text(encoding="utf-8").replace(
            subject.FROZEN_SOURCE_HEADING,
            "### SRC-025 — Completely Different Work",
            1,
        )
        self.baseline.write_text(wrong_identity, encoding="utf-8", newline="\n")
        identity = self.cli()
        self.assertNotEqual(identity.returncode, 0)
        self.assertIn("frozen source heading changed", identity.stderr)

        self.write_old_baseline()
        text = self.baseline.read_text(encoding="utf-8")
        duplicate = (
            "### SRC-025 — Duplicate target\n\n"
            "- Exact work title: *Duplicate target*\n"
            "- Retrieved granularity: duplicate\n\n"
            "#### Duplicate hierarchy\n\n"
            "- Duplicate source topic — **OPEN**\n\n"
        )
        self.baseline.write_text(
            text.replace("### SRC-026", duplicate + "### SRC-026"),
            encoding="utf-8",
            newline="\n",
        )
        duplicated = self.cli()
        self.assertNotEqual(duplicated.returncode, 0)
        self.assertIn("found at least 2", duplicated.stderr)


if __name__ == "__main__":
    unittest.main()
