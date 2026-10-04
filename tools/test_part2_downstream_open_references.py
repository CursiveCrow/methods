#!/usr/bin/env python3
"""Regressions for P12 consumers of retired Part-II draft labels."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
P12_FILES = (
    HANDBOOK / "parts/p12/sat-and-certificates.tex",
    HANDBOOK / "parts/p12/further-reading.tex",
)
RETIRED_LABELS = (
    "def:p02-equisatisfiability",
    "thm:p02-tseitin",
)


def uncommented_tex(path: Path) -> str:
    return "\n".join(
        re.split(r"(?<!\\)%", line, maxsplit=1)[0]
        for line in path.read_text(encoding="utf-8").splitlines()
    )


class PartIIDownstreamOpenReferenceTests(unittest.TestCase):
    def test_retired_draft_labels_are_not_live_p12_targets(self) -> None:
        for path in P12_FILES:
            text = uncommented_tex(path)
            for label in RETIRED_LABELS:
                with self.subTest(path=path.name, label=label):
                    self.assertNotIn(label, text)

    def test_each_consumer_keeps_the_missing_exact_destination_open(self) -> None:
        expected = {
            "sat-and-certificates.tex": (
                r"\textbf{OPEN:}",
                "exact source-mapped Part~2 destinations",
                "do not replace or discharge them",
            ),
            "further-reading.tex": (
                r"\textbf{OPEN:}",
                "exact source-mapped Part~2 destinations",
                "does not supply those destinations",
            ),
        }
        for path in P12_FILES:
            text = re.sub(r"\s+", " ", uncommented_tex(path))
            for needle in expected[path.name]:
                with self.subTest(path=path.name, needle=needle):
                    self.assertIn(re.sub(r"\s+", " ", needle), text)


if __name__ == "__main__":
    unittest.main()
