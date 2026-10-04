#!/usr/bin/env python3
"""Fail-closed route/history tests for exact source lines 14095--14270."""

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
        (14095, 14146), (14147, 14169), (14170, 14202),
        (14203, 14230), (14231, 14270),
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


def marked(path: Path, start: int, end: int) -> str:
    match = re.search(
        rf"(?s)% BEGIN HISTORICAL SLICE {start}-{end}\n"
        rf"(.*?)% END HISTORICAL SLICE {start}-{end}",
        path.read_text(encoding="utf-8"),
    )
    if match is None:
        raise AssertionError(f"missing historical slice {start}-{end}")
    return match.group(1)


def declared_labels(text: str) -> list[str]:
    labels = re.findall(r"\\label\s*\{([^{}]+)\}", text)
    labels.extend(
        re.findall(
            r"\\begin\{(?:hb(?:method|example|definition|theorem|warning)|"
            r"proofboundary|systementry|annexitem)\}\{([^{}]+)\}",
            text,
        )
    )
    return labels


class FormalPracticeSourceRouteTests(unittest.TestCase):
    def test_five_wrappers_and_open_supplement_lead_public_part12(self) -> None:
        direct = inputs(HANDBOOK / "parts/p12.tex")
        expected = [f"restoration/scope-{item}" for item in RESTORATION_IDS]
        self.assertEqual(
            direct[:6],
            expected + ["parts/p12/formal-practice-supplement"],
        )
        self.assertEqual(direct.count("parts/p12/automation-and-mechanization"), 1)
        self.assertGreater(
            direct.index("parts/p12/automation-and-mechanization"),
            direct.index("parts/p12/formal-practice-supplement"),
        )
        source = (HANDBOOK / "parts/p12.tex").read_text(encoding="utf-8")
        self.assertEqual(
            source.count(
                r"\part{Automation, Mechanization, and Formal Practice}"
                r"\label{part:p12}"
            ),
            1,
        )
        self.assertNotIn("generated/audit-p12", direct)
        self.assertNotIn(
            "parts/p12/formal-workflow",
            inputs(HANDBOOK / "parts/p12/automation-and-mechanization.tex"),
        )

    def test_historical_formal_workflow_is_exact_and_unreachable(self) -> None:
        path = HANDBOOK / "parts/p12/formal-workflow.tex"
        self.assertEqual(
            hashlib.sha256(path.read_bytes()).hexdigest(),
            "b5d74d38ca0fa5756e3f36a6cd10200a5b4d082c01eb0dce9052e628a8d1af36",
        )
        self.assertNotIn(path.resolve(), reachable(HANDBOOK / "main.tex"))

    def test_open_supplement_contains_only_three_complete_historical_slices(self) -> None:
        original = (
            HANDBOOK / "parts/p12/formal-workflow.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        supplement = HANDBOOK / "parts/p12/formal-practice-supplement.tex"
        self.assertEqual(
            hashlib.sha256(supplement.read_bytes()).hexdigest(),
            "308c6c9f28d9730c4a86ea6928f3384e5b72728899ed0808454a5f0cfa2a5a19",
        )
        pins = {
            (50, 59): (584, "8b1d29f1033492e2eabc787cb09a67f5cbffcf74199d8f575bde8f5b80fd2863"),
            (73, 192): (7042, "f10ad245ec39925aa8b492235ea25cfe0429e383f361a6ac62fddfa19b6be82c"),
            (219, 348): (7386, "9cccf7cd95559707d2f5c4cb1622aea77150c08d02bd5a6f618b022715dace62"),
        }
        for (start, end), (byte_count, digest) in pins.items():
            raw = "".join(original[start - 1:end])
            with self.subTest(start=start, end=end):
                self.assertEqual(len(raw.encode()), byte_count)
                self.assertEqual(hashlib.sha256(raw.encode()).hexdigest(), digest)
                self.assertEqual(marked(supplement, start, end), raw)
        prose = supplement.read_text(encoding="utf-8")
        for heading in (
            "Necessity:", "Definition:", "Standing:", "Nonredundancy:", "Use:"
        ):
            self.assertIn(heading, prose)
        self.assertEqual(prose.count(r"\noindent\textit{Reader note.}"), 1)

    def test_retired_overlap_labels_have_no_reachable_aliases(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = declared_labels(live)
        retired = {
            "sec:p12-formal-workflow", "def:p12-derivation-search",
            "def:p12-countervaluation-search", "def:p12-small-structure-search",
            "def:p12-metatheorem-plan", "tab:p12-failure-classification",
        }
        for label in retired:
            with self.subTest(retired=label):
                self.assertNotIn(label, labels)
        exact = {
            "ch:formal-practice", "sec:formal-practice-01",
            "sec:formal-practice-02", "sec:formal-practice-03",
            "sec:formal-practice-04", "sec:formal-practice-05",
            "ex:formal-practice-01", "ex:formal-practice-02",
        }
        for label in exact:
            with self.subTest(exact=label):
                self.assertEqual(labels.count(label), 1)
        consumer = (
            HANDBOOK / "parts/p12/sat-and-certificates.tex"
        ).read_text(encoding="utf-8")
        self.assertIn(r"Chapter~\ref{ch:formal-practice}", consumer)
        self.assertNotIn("sec:p12-formal-workflow", consumer)


if __name__ == "__main__":
    unittest.main()
