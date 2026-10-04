#!/usr/bin/env python3
"""Fail-closed route/history tests for exact source lines 13201--13583."""

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
        (13201, 13213), (13214, 13254), (13255, 13284), (13285, 13316),
        (13317, 13339), (13340, 13409), (13410, 13439), (13440, 13471),
        (13472, 13478), (13479, 13518), (13519, 13551), (13552, 13564),
        (13565, 13583),
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


class ModalTemporalSourceRouteTests(unittest.TestCase):
    def test_thirteen_wrappers_replace_two_historical_bodies(self) -> None:
        direct = inputs(HANDBOOK / "parts/p08.tex")
        anchor = direct.index("parts/p08/intuitionistic-supplement")
        expected = [f"restoration/scope-{item}" for item in RESTORATION_IDS]
        self.assertEqual(direct[anchor + 1:anchor + 14], expected)
        self.assertEqual(
            direct[anchor + 14:anchor + 17],
            [
                "parts/p08/modal-logics-supplement",
                "parts/p08/temporal-epistemic-supplement",
                "parts/p08/conditionals-deontic-free",
            ],
        )
        self.assertNotIn("parts/p08/modal-logics", direct)
        self.assertNotIn("parts/p08/temporal-dynamic-epistemic", direct)

    def test_four_historical_files_are_exact_and_unreachable(self) -> None:
        pins = {
            "parts/p08/modal-logics.tex":
                "b2f93697504b9b494fd015783683e0de970cc77fbfa3767590da6cb8594acf46",
            "annex/p08/modal-logics.tex":
                "115fa5aaf61cf3e4c89e86d6cfe25a188f9740c36d2d17d3651899063397ce8d",
            "parts/p08/temporal-dynamic-epistemic.tex":
                "14403d7c48bc1569d2505ad031abb4ff2f923d0b284fd62375c154a714fd32e4",
            "annex/p08/temporal-dynamic-epistemic.tex":
                "933b2a29ecc9a0b851abd20d9b4245158cc6f6ef9ed578ce5be01da2c3c5ed79",
        }
        route = reachable(HANDBOOK / "main.tex")
        for relative, expected in pins.items():
            path = HANDBOOK / relative
            with self.subTest(relative=relative):
                self.assertEqual(sha256(path.read_bytes()), expected)
                self.assertNotIn(path.resolve(), route)

        annex_inputs = inputs(HANDBOOK / "annex/p08.tex")
        self.assertNotIn("annex/p08/modal-logics", annex_inputs)
        self.assertNotIn("annex/p08/temporal-dynamic-epistemic", annex_inputs)

    def test_seven_addition_slices_are_exact_or_consumer_corrected_only(self) -> None:
        modal_path = HANDBOOK / "parts/p08/modal-logics.tex"
        temporal_path = HANDBOOK / "parts/p08/temporal-dynamic-epistemic.tex"
        modal_lines = modal_path.read_text(encoding="utf-8").splitlines(keepends=True)
        temporal_lines = temporal_path.read_text(encoding="utf-8").splitlines(
            keepends=True
        )
        modal_supplement = HANDBOOK / "parts/p08/modal-logics-supplement.tex"
        temporal_supplement = HANDBOOK / "parts/p08/temporal-epistemic-supplement.tex"
        self.assertEqual(
            sha256(modal_supplement.read_bytes()),
            "fdb235bce5fb70e6ebc573a434160d62e1779b3f4f29842c4c2e7197463d8283",
        )
        self.assertEqual(
            sha256(temporal_supplement.read_bytes()),
            "f516c37c186ac42388207c25e180f301e2da8237f1cb4d33b3ed6508d6e505a0",
        )

        pins = {
            (modal_path, 60, 343):
                (15257, "d33c092c70147b435f51371f9f26cedc9d73d960b32661910b0f51c9ce441430"),
            (modal_path, 358, 607):
                (11385, "271dfe3475b9a2d78bdb14b514c1ff9abeccbddfb98105f4fdd95feed5884913"),
            (modal_path, 610, 1050):
                (21815, "3a0d58a925dbb0f342819c09243c430661778d7832a3c81fb6a35742bd331f9a"),
            (temporal_path, 49, 68):
                (1215, "ad78fb48d5a3053e3834d3424e5a943255a7eff710736f458c6c28efff9c9022"),
            (temporal_path, 89, 508):
                (19852, "53530acd927a51f0d5bcb4e92164e33db3cda22489d0d779824d6a38d8b05e53"),
            (temporal_path, 526, 564):
                (2344, "96ab7a29db6d621b638862d703d75feb4a49dfaa41fcba675a59eee34c56c081"),
            (temporal_path, 610, 774):
                (9464, "19324c1f67233a187b032eb217f2f89dcca8c83fa2c83fd1c6a7acfab92b3bea"),
        }
        for (path, start, end), (byte_count, digest) in pins.items():
            lines = modal_lines if path == modal_path else temporal_lines
            raw = "".join(lines[start - 1:end])
            with self.subTest(path=path.name, start=start, end=end):
                self.assertEqual(len(raw.encode()), byte_count)
                self.assertEqual(sha256(raw.encode()), digest)

        modal_catalog = "".join(modal_lines[59:343])
        old_modal_theorem = r"Theorem~\ref{thm:p08-modal-four-system-adequacy}"
        self.assertEqual(modal_catalog.count(old_modal_theorem), 4)
        expected_modal_catalog = modal_catalog.replace(
            old_modal_theorem,
            r"Section~\ref{sec:modal-temporal-epistemic-01}",
        )
        self.assertEqual(
            marked(modal_supplement, "DERIVATIVE", 60, 343),
            expected_modal_catalog,
        )
        self.assertEqual(
            marked(modal_supplement, "SLICE", 358, 607),
            "".join(modal_lines[357:607]),
        )

        modal_continuation = "".join(modal_lines[609:1050])
        modal_continuation = modal_continuation.replace(
            r"Definition~\ref{def:p08-modal-kripke-structure}",
            r"Section~\ref{sec:modal-temporal-epistemic-01}",
        )
        old_modal_note = (
            "\\paragraph{Source and navigation note.}\n"
            "The normal-modal definitions, premise discipline for K, T, S4, and S5, bundled adequacy\n"
            "statement, and three countermodel calculations migrate v1.1 Part X,\n"
            "lines 13204--13339.  The rule schemas themselves occur only on the exact\n"
            "registry sheets.  The canonical sketch is in Annex~\\ref{annex:p8.modal.1}; the\n"
            "new correspondence, filtration, bisimulation, neighborhood, and quantified\n"
            "material is cited at its stated evidence ceiling.\n"
        )
        new_modal_note = (
            "\\paragraph{Source and navigation note.}\n"
            "The exact inherited chapter above supplies the normal-modal definitions,\n"
            "premise discipline for K, T, S4, and S5, bundled adequacy statement,\n"
            "three countermodels, and inline canonical proof sketch in\n"
            "Section~\\ref{sec:modal-temporal-epistemic-01}.  The registered sheets are\n"
            "separate navigation aids.  The correspondence, filtration, bisimulation,\n"
            "neighborhood, and quantified material below is cited at its stated evidence\n"
            "ceiling.\n"
        )
        self.assertEqual(modal_continuation.count(old_modal_note), 1)
        modal_continuation = modal_continuation.replace(old_modal_note, new_modal_note)
        self.assertEqual(
            marked(modal_supplement, "DERIVATIVE", 610, 1050),
            modal_continuation,
        )

        ltl_card = "".join(temporal_lines[48:68])
        ltl_card = ltl_card.replace(
            r"Definition~\ref{def:p08-ltl-word}",
            r"Section~\ref{sec:modal-temporal-epistemic-02}",
        )
        old_ltl_status = (
            "The inherited source argument remains the separately\n"
            "    labelled sketch in Theorem~\\ref{thm:p08-ltl-adequacy};"
        )
        new_ltl_status = (
            "The exact inherited source gives the theorem and inline proof sketch in\n"
            "    Section~\\ref{sec:modal-temporal-epistemic-02};"
        )
        self.assertEqual(ltl_card.count(old_ltl_status), 1)
        ltl_card = ltl_card.replace(old_ltl_status, new_ltl_status)
        self.assertEqual(
            marked(temporal_supplement, "DERIVATIVE", 49, 68), ltl_card
        )

        temporal_body = "".join(temporal_lines[88:508])
        self.assertEqual(
            temporal_body.count(r"Definition~\ref{def:p08-ltl-word}"), 1
        )
        temporal_body = temporal_body.replace(
            r"Definition~\ref{def:p08-ltl-word}",
            r"Section~\ref{sec:modal-temporal-epistemic-02}",
        )
        self.assertEqual(
            marked(temporal_supplement, "DERIVATIVE", 89, 508), temporal_body
        )

        epistemic_cards = "".join(temporal_lines[525:564])
        old_s5_status = (
            "The inherited canonical argument remains the\n"
            "    separate sketch in Theorem~\\ref{thm:p08-s5n-adequacy}."
        )
        new_s5_status = (
            "The exact inherited source gives the theorem and inline proof sketch in\n"
            "    Section~\\ref{sec:modal-temporal-epistemic-03}."
        )
        self.assertEqual(epistemic_cards.count(old_s5_status), 1)
        epistemic_cards = epistemic_cards.replace(old_s5_status, new_s5_status)
        self.assertEqual(
            marked(temporal_supplement, "DERIVATIVE", 526, 564), epistemic_cards
        )

        epistemic_continuation = "".join(temporal_lines[609:774])
        epistemic_continuation = epistemic_continuation.replace(
            r"Definition~\ref{def:p08-group-knowledge}",
            r"Section~\ref{sec:modal-temporal-epistemic-03}",
        )
        old_temporal_note = (
            "\\paragraph{Source and status boundary.}\n"
            "The LTL definitions, exact sheet, adequacy sketch, and eventuality example\n"
            "migrate v1.1 lines 13340--13478.  The multi-agent \\(\\mathsf{S5}_{I}\\)\n"
            "definitions, exact sheet, adequacy sketch, common-knowledge semantics, and\n"
            "truth-without-knowledge example migrate lines 13479--13583.  CTL, CTL*, modal\n"
            "\\(\\mu\\), tense logic, \\(\\mathsf{KD45}_{I}\\), the common-knowledge calculus,\n"
            "distributed knowledge, public announcements, and all five apparatus artifacts\n"
            "are new cited or explicitly calculated content; none inherits a source-proof\n"
            "length denominator.  OPEN: the three source exercise prompts at lines\n"
            "13565--13582 and any supplied feedback remain owed in full at exact\n"
            "source-mapped destinations.  The modal countermodel in\n"
            "Figure~\\ref{fig:p08-modal-countermodels}, the LTL timeline in\n"
            "Figure~\\ref{fig:p08-ltl-path}, and the explicit\n"
            "everyone-without-common-knowledge model in\n"
            "Example~\\ref{def:p08-everyone-not-common} are separate later material and do\n"
            "not replace or discharge those source prompts.\n"
        )
        new_temporal_note = (
            "\\paragraph{Source and status boundary.}\n"
            "The exact inherited chapter above supplies the LTL and multi-agent\n"
            "\\(\\mathsf{S5}_{I}\\) definitions, calculi, adequacy statements and inline\n"
            "proof sketches, examples, common-knowledge semantics, and all three source\n"
            "exercises at lines 13340--13582.  CTL, CTL*, modal \\(\\mu\\), tense logic,\n"
            "\\(\\mathsf{KD45}_{I}\\), the common-knowledge calculus, distributed\n"
            "knowledge, public announcements, and all five apparatus artifacts below are\n"
            "separate cited or explicitly calculated additions; none inherits a\n"
            "source-proof length denominator.  The modal countermodel in\n"
            "Figure~\\ref{fig:p08-modal-countermodels}, the LTL timeline in\n"
            "Figure~\\ref{fig:p08-ltl-path}, and the explicit\n"
            "everyone-without-common-knowledge model in\n"
            "Example~\\ref{def:p08-everyone-not-common} neither replace nor alter the\n"
            "exact source examples or exercises.\n"
        )
        self.assertEqual(epistemic_continuation.count(old_temporal_note), 1)
        epistemic_continuation = epistemic_continuation.replace(
            old_temporal_note, new_temporal_note
        )
        self.assertEqual(
            marked(temporal_supplement, "DERIVATIVE", 610, 774),
            epistemic_continuation,
        )

        for supplement in (modal_supplement, temporal_supplement):
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
            "sec:p08-modal-logics", "def:p08-modal-kripke-structure",
            "def:p08-modal-validity", "def:p08-modal-local-global",
            "def:p08-modal-derivability", "thm:p08-modal-four-system-adequacy",
            "annex:p8.modal.1", "sec:p08-temporal-dynamic-epistemic",
            "def:p08-ltl-word", "def:p08-ltl-eventuality", "thm:p08-ltl-adequacy",
            "def:p08-epistemic-structure", "thm:p08-s5n-adequacy",
            "def:p08-truth-without-knowledge", "def:p08-group-knowledge",
            "annex:p8.temporal.1", "annex:p8.temporal.2",
        }
        for label in retired:
            with self.subTest(retired=label):
                self.assertNotIn(label, labels)

        exact = {
            "ch:modal-temporal-epistemic",
            "sec:modal-temporal-epistemic-01",
            "sec:modal-temporal-epistemic-02",
            "sec:modal-temporal-epistemic-03",
            "ex:modal-temporal-epistemic-01",
            "ex:modal-temporal-epistemic-02",
            "ex:modal-temporal-epistemic-03",
        }
        for label in exact:
            with self.subTest(exact=label):
                self.assertEqual(labels.count(label), 1)

    def test_exact_target_preserves_zero_pending_inherited_references(self) -> None:
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
