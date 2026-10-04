#!/usr/bin/env python3
"""Exercise symbol collisions through the handbook checker's real CSV path."""

from __future__ import annotations

import contextlib
import csv
import io
import tempfile
import unittest
from pathlib import Path

from tools import check, symbols2tex


class HandbookSymbolScopeTests(unittest.TestCase):
    def check_pair(
        self, first_scope: str, second_scope: str, *, same_role: bool = False
    ) -> dict[str, list[str]]:
        """Run the actual checker on two registrations of one glyph."""
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "symbols.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.writer(handle)
                writer.writerow(symbols2tex.HEADER)
                for scope, role in (
                    (first_scope, "first role"),
                    (second_scope, "first role" if same_role else "second role"),
                ):
                    lower = scope.split("-", 1)[0]
                    first_use = (
                        "P1.1" if lower in ("", "global", "unparseable")
                        else lower if "." in lower else lower + ".0"
                    )
                    writer.writerow([r"\xi", r"\xi", role, scope,
                                     "meta", first_use, ""])
            data = check._HBData()
            with contextlib.redirect_stdout(io.StringIO()):
                check._hb_check_symbols(path, data)
            return data.findings

    def test_global_conflicting_role_is_rejected_in_every_approved_part(self):
        for part in range(1, 20):
            scope = f"P{part}.1"
            with self.subTest(scope=scope):
                findings = self.check_pair("global", scope)
                self.assertEqual(set(findings), {"glyph-collision"})
                self.assertEqual(len(findings["glyph-collision"]), 1)
                self.assertIn(repr(scope), findings["glyph-collision"][0])

    def test_global_identical_role_is_rejected_in_new_parts(self):
        for scope in ("P15.1", "P19.99"):
            with self.subTest(scope=scope):
                findings = self.check_pair(scope, "global", same_role=True)
                self.assertEqual(set(findings), {"symbols-csv"})
                self.assertEqual(len(findings["symbols-csv"]), 1)
                self.assertIn("duplicate glyph-role", findings["symbols-csv"][0])

    def test_global_covers_whole_parts_and_last_chapter(self):
        for scope in ("P15", "P19", "P19.99"):
            with self.subTest(scope=scope):
                self.assertIn("glyph-collision", self.check_pair("global", scope))

    def test_unknown_scope_is_rejected_instead_of_becoming_global(self):
        for fallback in ("", "unparseable"):
            with self.subTest(scope=fallback):
                self.assertIn("symbols-csv", self.check_pair(fallback, "P19.1"))

    def test_disjoint_chapters_and_stable_part_ranges_still_pass(self):
        for left, right in (
            ("P8.2-P8.4", "P8.5"),
            ("P15.1", "P15.2"),
            ("P11-P14", "P15-P19"),
        ):
            for same_role in (False, True):
                with self.subTest(left=left, right=right, same_role=same_role):
                    self.assertEqual(self.check_pair(left, right, same_role=same_role), {})

    def test_overlapping_chapter_and_stable_part_ranges_still_reject(self):
        for left, right in (("P8.2-P8.4", "P8.4"), ("P14-P16", "P15.1")):
            with self.subTest(left=left, right=right):
                self.assertIn("glyph-collision", self.check_pair(left, right))

    def test_checker_and_generator_agree_on_approved_overlap_cases(self):
        scopes = ("global", "P1", "P8.2-P8.4", "P8.5", "P11-P14",
                  "P14-P16", "P15", "P15.1", "P19.99")
        for index, left in enumerate(scopes):
            for right in scopes[index + 1:]:
                with self.subTest(left=left, right=right):
                    expected = symbols2tex.overlap(
                        symbols2tex.parse_scope(left), symbols2tex.parse_scope(right)
                    )
                    actual = "glyph-collision" in self.check_pair(left, right)
                    self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
