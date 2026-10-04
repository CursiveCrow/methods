#!/usr/bin/env python3
"""Focused regression checks for the admitted Part-I reader route."""

from __future__ import annotations

import csv
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
INPUT_RE = re.compile(r"\\input\s*\{([^}]+)\}")

PART_I_INTERVALS = (
    "SRC-00363-00372",
    "SRC-00373-00405",
    "SRC-00406-00443",
    "SRC-00444-00506",
    "SRC-00507-00532",
    "SRC-00533-00602",
    "SRC-00603-00647",
    "SRC-00648-00744",
    "SRC-00745-00772",
    "SRC-00773-00789",
    "SRC-00790-00797",
    "SRC-00798-00852",
    "SRC-00853-00906",
    "SRC-00907-00984",
    "SRC-00985-01023",
    "SRC-01024-01084",
    "SRC-01085-01100",
    "SRC-01101-01147",
    "SRC-01148-01163",
    "SRC-01164-01223",
    "SRC-01224-01263",
    "SRC-01264-01308",
    "SRC-01309-01319",
    "SRC-01320-01342",
    "SRC-01343-01397",
    "SRC-01398-01410",
    "SRC-01411-01504",
    "SRC-01505-01553",
    "SRC-01554-01579",
    "SRC-01580-01591",
    "SRC-01592-01631",
    "SRC-01632-01648",
)
EXPECTED_PART_I_INPUTS = tuple(
    f"restoration/scope-{interval}" for interval in PART_I_INTERVALS
)
HISTORICAL_PART_I_FILES = (
    "parts/p01/symbol-registry.tex",
    "parts/p01/mathematical-preliminaries.tex",
    "parts/p01/formal-work-conventions.tex",
    "generated/audit-p01.tex",
    "annex/p01.tex",
)
RETIRED_LIVE_LABELS = (
    "thm:p01-ultrafilter-lemma",
    "thm:p01-cardinal-assignment",
    "thm:p01-finite-coding",
    "def:p01-axiom-choice",
    "thm:p01-well-ordering",
    "thm:p01-ordered-pair-identity",
    "annex:p1.1",
    "tab:p01-classical-symbols",
    "tab:p01-precedence",
    "tab:p01-sixteen",
    "sec:p01-symbol-registry",
    "sec:p01-generated-symbols",
)
PART_I_CHAPTERS = (
    "Sets, Relations, Functions, and Cardinality",
    "Levels, Objects, and Consequence",
    "Finite Strings, Induction, and Recursion",
    "Writing Formal Definitions and Proofs",
)
EXACT_INHERITED_RULE_DISPLAY = (
    r"  \Rule[\(\forall I\)]{\Gamma\derives\varphi}"
    r"{\Gamma\derives\forall x\,\varphi}"
    "\n"
    r"  \side{provided \(x\) is not free in any member of \(\Gamma\)}."
)
OPEN_SYMBOL_OBLIGATIONS = (
    "OBL::apparatus::A-024",
    "OBL::apparatus::A-025",
    "OBL::apparatus::A-157",
    "OBL::apparatus::A-161",
    "OBL::apparatus::A-162",
    "OBL::apparatus::A-163",
    "OBL::apparatus::A-164",
    "OBL::apparatus::A-165",
    "OBL::apparatus::A-166",
    "OBL::apparatus::A-189",
    "OBL::apparatus::A-193",
    "OBL::apparatus::A-201",
)
RECONCILED_READER_FILES = (
    "parts/p02/propositional-metatheory.tex",
    "parts/p02/propositional-syntax-semantics.tex",
    "parts/p03/types-ultraproducts.tex",
    "parts/p06/axioms-hierarchy.tex",
    "parts/p06/cardinals-choice.tex",
    "parts/p07/proof-complexity.tex",
    "parts/p08/intuitionistic-supplement.tex",
    "parts/p12/formal-workflow.tex",
    "parts/p12/further-reading.tex",
)


def uncommented_tex(path: Path) -> str:
    lines: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        lines.append(re.split(r"(?<!\\)%", line, maxsplit=1)[0])
    return "\n".join(lines)


def input_targets(path: Path) -> tuple[str, ...]:
    return tuple(INPUT_RE.findall(uncommented_tex(path)))


def resolve_input(target: str) -> Path:
    relative = Path(target)
    if relative.suffix != ".tex":
        relative = relative.with_suffix(".tex")
    return HANDBOOK / relative


def reachable_tex(start: str) -> set[Path]:
    pending = [HANDBOOK / start]
    reached: set[Path] = set()
    while pending:
        path = pending.pop()
        relative = path.relative_to(HANDBOOK)
        if relative in reached:
            continue
        reached.add(relative)
        pending.extend(resolve_input(target) for target in input_targets(path))
    return reached


def reachable_text(start: str) -> str:
    return "\n".join(
        uncommented_tex(HANDBOOK / relative)
        for relative in sorted(reachable_tex(start))
    )


class PartIReaderRouteTests(unittest.TestCase):
    def test_part_i_has_only_the_exact_restoration_route(self) -> None:
        driver = HANDBOOK / "parts/p01.tex"
        self.assertEqual(input_targets(driver), EXPECTED_PART_I_INPUTS)
        self.assertEqual(
            uncommented_tex(driver).count(r"\label{sec:inherited-set-prerequisites}"),
            1,
        )

        expected_reachable = {Path("parts/p01.tex")}
        expected_reachable.update(
            Path(f"restoration/scope-{interval}.tex") for interval in PART_I_INTERVALS
        )
        expected_reachable.update(
            Path(f"restoration/inherited-{interval.removeprefix('SRC-')}.tex")
            for interval in PART_I_INTERVALS
        )
        self.assertEqual(reachable_tex("parts/p01.tex"), expected_reachable)

        main_reachable = reachable_tex("main.tex")
        for relative in HISTORICAL_PART_I_FILES:
            with self.subTest(relative=relative):
                self.assertTrue((HANDBOOK / relative).is_file())
                self.assertNotIn(Path(relative), main_reachable)

    def test_retired_part_i_labels_are_absent_from_the_live_reader_route(self) -> None:
        live_text = reachable_text("main.tex")
        for label in RETIRED_LIVE_LABELS:
            with self.subTest(label=label):
                self.assertNotIn(label, live_text)

    def test_live_references_use_exact_inherited_part_i_targets(self) -> None:
        expected = {
            "parts/p02/propositional-metatheory.tex": (
                r"Definition~\ref{def:ultrafilter-lemma}",
            ),
            "parts/p03/types-ultraproducts.tex": (
                r"Definition~\ref{def:ultrafilter-lemma}",
            ),
            "parts/p06/cardinals-choice.tex": (
                r"Definition~\ref{def:ultrafilter-lemma}",
                r"Corollary~\ref{cor:cardinal-assignment}",
                r"Section~\ref{sec:set-prerequisites-06}",
                r"Theorem~\ref{thm:infinite-cardinal-finite-coding}",
            ),
            "parts/p06/axioms-hierarchy.tex": (
                r"Section~\ref{sec:set-prerequisites-02}",
            ),
        }
        for relative, needles in expected.items():
            text = uncommented_tex(HANDBOOK / relative)
            for needle in needles:
                with self.subTest(relative=relative, needle=needle):
                    self.assertIn(needle, text)

    def test_four_inherited_chapters_and_rule_display_occur_once(self) -> None:
        part_i_text = reachable_text("parts/p01.tex")
        chapters = re.findall(r"\\chapter(?!\*)\s*\{([^{}]+)\}", part_i_text)
        self.assertCountEqual(chapters, PART_I_CHAPTERS)
        self.assertEqual(len(chapters), len(PART_I_CHAPTERS))
        self.assertEqual(part_i_text.count(EXACT_INHERITED_RULE_DISPLAY), 1)

    def test_no_part_i_annex_anchor_is_live(self) -> None:
        self.assertIsNone(re.search(r"annex:p1(?:\.\d+|\b)", reachable_text("main.tex")))

    def test_reconciled_reader_prose_does_not_authorize_source_retirement(self) -> None:
        for relative in RECONCILED_READER_FILES:
            text = uncommented_tex(HANDBOOK / relative).lower()
            for authorization in (
                "retired",
                "deliberately not printed",
                "already appear",
                "does not duplicate",
            ):
                with self.subTest(relative=relative, authorization=authorization):
                    self.assertNotIn(authorization, text)

    def test_distinct_part_vi_ordered_pair_units_remain_open(self) -> None:
        text = uncommented_tex(HANDBOOK / "parts/p06/axioms-hierarchy.tex")
        self.assertIn(r"\texttt{SRC-10272-10352}", text)
        self.assertIn("is a separate source unit and does not", text)
        self.assertIn("replace or discharge the Part~6 statement or proof", text)

    def test_symbol_registry_stays_out_while_admission_is_open(self) -> None:
        self.assertNotIn(
            Path("parts/p01/symbol-registry.tex"), reachable_tex("main.tex")
        )

        with (ROOT / "spec/register-obligation-closure.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            obligations = {
                row["obligation_id"]: row for row in csv.DictReader(handle)
            }
        for obligation_id in OPEN_SYMBOL_OBLIGATIONS:
            with self.subTest(obligation_id=obligation_id):
                self.assertIn(obligation_id, obligations)
                self.assertEqual(
                    obligations[obligation_id]["completion_status"], "OPEN"
                )

        with (ROOT / "spec/presentation-packet-admission.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            packets = list(csv.DictReader(handle))
        self.assertFalse(
            any(row["admission_status"] == "ADMITTED" for row in packets)
        )


if __name__ == "__main__":
    unittest.main()
