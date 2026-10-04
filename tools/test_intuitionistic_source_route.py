#!/usr/bin/env python3
"""Fail-closed route/history tests for exact source lines 12970--13200."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
RESTORATION_IDS = tuple(
    f"SRC-{start:05d}-{end:05d}"
    for start, end in (
        (12970, 12988), (12989, 13045), (13046, 13057),
        (13058, 13099), (13100, 13127), (13128, 13140),
        (13141, 13157), (13158, 13179), (13180, 13200),
    )
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


class IntuitionisticSourceRouteTests(unittest.TestCase):
    def test_nine_wrappers_open_public_part8_and_replace_historical_body(self) -> None:
        driver = HANDBOOK / "parts/p08.tex"
        direct = inputs(driver)
        expected = [f"restoration/scope-{item}" for item in RESTORATION_IDS]
        self.assertEqual(direct[:10], expected + ["parts/p08/intuitionistic-supplement"])
        self.assertEqual(direct[10], "restoration/scope-SRC-13201-13213")
        self.assertNotIn("parts/p08/intuitionistic-and-intermediate", direct)
        self.assertNotIn("generated/audit-p08", direct)
        source = driver.read_text(encoding="utf-8")
        self.assertNotIn(r"\part{Nonclassical Logics}", source)
        self.assertNotIn("part:p08", source)
        for item in expected:
            self.assertEqual(direct.count(item), 1)

    def test_historical_body_and_annex_are_exact_and_unreachable(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        pins = {
            "parts/p08/intuitionistic-and-intermediate.tex":
                "aac30a07b44a9564662848fa39b8880ee4dad77673761a4402b2e1aa0fb30dd3",
            "annex/p08/intuitionistic-and-intermediate.tex":
                "e758da33c6f167e8eab621b2e151fd003269a1c9e54e41ca7c624e06bc9aed8a",
        }
        for relative, digest in pins.items():
            with self.subTest(relative=relative):
                path = HANDBOOK / relative
                self.assertEqual(sha256(path.read_bytes()), digest)
                self.assertNotIn(path.resolve(), route)
        self.assertNotIn(
            "annex/p08/intuitionistic-and-intermediate",
            inputs(HANDBOOK / "annex/p08.tex"),
        )

    def test_six_addition_slices_are_exact_or_consumer_corrected_only(self) -> None:
        original = (
            HANDBOOK / "parts/p08/intuitionistic-and-intermediate.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        supplement = HANDBOOK / "parts/p08/intuitionistic-supplement.tex"
        pins = {
            (90, 128): (2221, "28bff605b5501b68502f64adc2b8914b9865f86adf621a8861bd71f1ee81443f"),
            (149, 165): (762, "535f8bc0fa3dea82dcaedd8ba8a039aafad9425b7433e65ec086143548c7857b"),
            (175, 191): (709, "49d57d4ae8f5e0531c938fe1a6c9c38c5a3761648773edb4a8f3c98063d878ba"),
            (208, 275): (3130, "ebce843136aa37408497d30b6d8af53920225bb77119d9007cf318832bd220ef"),
            (313, 379): (2760, "bcd367687a311ed630c56f18baa7e0751d1b52479b7379c8aac337d84cc09109"),
            (396, 681): (13420, "44ecc858c0bba9759102f5fcae0e0513bd8a158ddf684ed835ad60c32d067cc5"),
        }
        for (start, end), (byte_count, digest) in pins.items():
            raw = "".join(original[start - 1:end])
            self.assertEqual(len(raw.encode()), byte_count)
            self.assertEqual(sha256(raw.encode()), digest)

        system = "".join(original[89:128])
        expected_system = system.replace(
            r"Definition~\ref{def:p08-ipl-finite-support}",
            r"Section~\ref{sec:intuitionistic-logic-01}",
        ).replace(
            "Persistent valuations on preordered Kripke frames, with\n"
            "    partial orders as the antisymmetric special presentation,\n"
            "    with forcing and consequence as in\n"
            "    Definitions~\\ref{def:p08-ipl-kripke-structure}--\\ref{def:p08-ipl-consequence}.",
            "Persistent valuations on the partially ordered Kripke frames fixed in\n"
            "    Section~\\ref{sec:intuitionistic-logic-01}, with forcing and consequence\n"
            "    as defined there.",
        ).replace(
            r"\entryadequacy{sketched=annex:p8.ipl.2}",
            r"\entryadequacy{cited=TroelstraSchwichtenberg2000}",
        ).replace("thm:p08-glivenko", "thm:glivenko").replace(
            "thm:p08-godel-gentzen", "thm:negative-translation"
        )
        self.assertEqual(marked(supplement, "DERIVATIVE", 90, 128), expected_system)

        for start, end in ((149, 165), (175, 191), (208, 275)):
            self.assertEqual(
                marked(supplement, "SLICE", start, end),
                "".join(original[start - 1:end]),
            )

        table = "".join(original[312:379])
        expected_table = table.replace("thm:p08-glivenko", "thm:glivenko").replace(
            "thm:p08-godel-gentzen", "thm:negative-translation"
        )
        self.assertEqual(marked(supplement, "DERIVATIVE", 313, 379), expected_table)

        continuation = "".join(original[395:681])
        expected_continuation = continuation.replace(
            "def:p08-ipl-forcing", "sec:intuitionistic-logic-01"
        )
        self.assertEqual(
            marked(supplement, "DERIVATIVE", 396, 681), expected_continuation
        )
        prose = supplement.read_text(encoding="utf-8")
        for heading in ("Necessity:", "Definition:", "Standing:", "Nonredundancy:", "Use:"):
            self.assertIn(heading, prose)
        self.assertEqual(prose.count(r"\noindent\textit{Reader note.}"), 1)

    def test_retired_overlap_labels_have_no_reachable_aliases(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        live_labels = declared_labels(live)
        retired = {
            "part:p08", "sec:p08-intuitionistic-and-intermediate",
            "def:p08-nonclassical-formula-roles", "def:p08-ipl-finite-support",
            "def:p08-ipl-kripke-structure", "def:p08-ipl-forcing",
            "thm:p08-ipl-persistence", "def:p08-ipl-consequence",
            "def:p08-ipl-constructive-benchmark", "def:p08-ipl-world-disjunction",
            "thm:p08-glivenko", "def:p08-godel-gentzen-translation",
            "thm:p08-godel-gentzen", "annex:p8.ipl.1", "annex:p8.ipl.2",
        }
        for label in retired:
            with self.subTest(retired=label):
                self.assertNotIn(label, live_labels)

        exact = {
            "part:nonclassical", "ch:intuitionistic-logic",
            "sec:intuitionistic-logic-01", "ex:intuitionistic-logic-01",
            "ex:intuitionistic-logic-02", "sec:intuitionistic-classical",
            "thm:glivenko", "thm:negative-translation",
            "thm:disjunction-property",
        }
        additions = {
            "entry:p08-ipl", "fig:p08-ipl-excluded-middle", "fig:p08-ipl-peirce",
            "def:p08-negative-translation-maps", "thm:p08-kolmogorov-embedding",
            "thm:p08-kuroda-embedding", "tab:p08-negative-translations",
            "def:p08-heyting-algebra", "thm:p08-heyting-completeness",
            "def:p08-ipl-topological-semantics", "thm:p08-topological-completeness",
            "def:p08-bhk-reading", "def:p08-intuitionistic-mathematics-boundary",
            "thm:p08-normal-existence-extraction", "def:p08-iqc-expanding-domain",
            "thm:p08-iqc-completeness", "def:p08-iqc-constant-domain-principle",
            "thm:p08-iqc-constant-domain-boundary", "def:p08-intermediate-logic",
            "thm:p08-kc-profile", "thm:p08-lc-profile",
            "tab:p08-intermediate-logics",
        }
        for label in exact | additions:
            with self.subTest(live=label):
                self.assertEqual(live_labels.count(label), 1)

    def test_exact_target_eliminates_all_live_pending_inherited_references(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "-B",
                "tools/check.py",
                "--tree",
                "handbook",
                "--strict",
                "--require-no-pending-inherited-refs",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        output = completed.stdout + completed.stderr
        self.assertEqual(completed.returncode, 0, output)
        self.assertIn("[metric] pending inherited references: 0", output)


if __name__ == "__main__":
    unittest.main()
