#!/usr/bin/env python3
"""Focused regression tests for the governed Part II reader route."""

from __future__ import annotations

import csv
import re
import hashlib
import shutil
import tempfile
import unittest
from pathlib import Path

from tools import check as handbook_check


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
WRAPPERS = [
    "restoration/scope-SRC-01649-01660",
    "restoration/scope-SRC-01661-01816",
    "restoration/scope-SRC-01817-01898",
    "restoration/scope-SRC-01899-01945",
    "restoration/scope-SRC-01946-02186",
    "restoration/scope-SRC-02187-02192",
    "restoration/scope-SRC-02193-02340",
    "restoration/scope-SRC-02341-02450",
    "restoration/scope-SRC-02451-02544",
    "restoration/scope-SRC-02545-02664",
    "restoration/scope-SRC-02665-02809",
    "restoration/scope-SRC-02810-02914",
    "restoration/scope-SRC-02915-02932",
    "restoration/scope-SRC-02933-03021",
    "restoration/scope-SRC-03022-03037",
    "restoration/scope-SRC-03038-03104",
    "restoration/scope-SRC-03105-03165",
    "restoration/scope-SRC-03166-03239",
    "restoration/scope-SRC-03240-03428",
    "restoration/scope-SRC-03429-03518",
    "restoration/scope-SRC-03519-03680",
    "restoration/scope-SRC-03681-03728",
    "restoration/scope-SRC-03729-03907",
    "restoration/scope-SRC-03908-03926",
    "restoration/scope-SRC-03927-04061",
    "restoration/scope-SRC-04062-04108",
    "restoration/scope-SRC-04109-04213",
    "restoration/scope-SRC-04214-04234",
    "restoration/scope-SRC-04235-04305",
    "restoration/scope-SRC-04306-04575",
    "restoration/scope-SRC-04576-04712",
    "restoration/scope-SRC-04713-04920",
    "restoration/scope-SRC-04921-04967",
    "restoration/scope-SRC-04968-05042",
    "restoration/scope-SRC-05043-05131",
    "restoration/scope-SRC-05132-05567",
    "restoration/scope-SRC-05568-05923",
    "restoration/scope-SRC-05924-05959",
    "restoration/scope-SRC-05960-06048",
    "restoration/scope-SRC-12249-12261",
    "restoration/scope-SRC-12262-12289",
    "restoration/scope-SRC-12290-12355",
    "restoration/scope-SRC-12356-12414",
    "restoration/scope-SRC-12415-12536",
    "restoration/scope-SRC-12537-12673",
    "restoration/scope-SRC-12674-12720",
    "restoration/scope-SRC-12721-12783",
    "restoration/scope-SRC-12784-12923",
    "restoration/scope-SRC-12924-12950",
    "restoration/scope-SRC-12951-12969",
]
METATHEORY_WRAPPERS = WRAPPERS[8:14]
FIRST_ORDER_SYNTAX_WRAPPERS = WRAPPERS[14:19]
FIRST_ORDER_SEMANTICS_WRAPPERS = WRAPPERS[19:22]
FIRST_ORDER_THEORIES_WRAPPERS = WRAPPERS[22:24]
FIRST_ORDER_DEDUCTION_WRAPPERS = WRAPPERS[24:29]
FIRST_ORDER_COMPLETENESS_WRAPPERS = WRAPPERS[29:33]
FIRST_ORDER_CARDINALITY_WRAPPERS = WRAPPERS[33:39]
HIGHER_ORDER_WRAPPERS = WRAPPERS[39:50]
TYPED_LABEL_RE = re.compile(
    r"\\begin\s*\{(?:hbdefinition|hbtheorem|hblemma|hbcorollary|hbmethod|"
    r"hbwarning|hbconvention|hbexample|hbsystementry|annexitem)\}\s*\{([^{}]+)\}"
)
REF_RE = re.compile(
    r"\\(?:ref|pageref|autoref|nameref|cref|Cref)\s*\{([^{}]+)\}"
    r"|\\hyperref\s*\[([^\]]+)\]"
)


def uncommented_inputs(relative: str) -> list[str]:
    text = (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
    text = re.sub(r"(?m)(?<!\\)%.*$", "", text)
    return re.findall(r"\\input\s*\{([^{}]+)\}", text)


def reachable(start: str) -> list[str]:
    reached: list[str] = []

    def visit(relative: str, active: tuple[str, ...]) -> None:
        if relative in active:
            raise AssertionError(f"cyclic test route at {relative}")
        reached.append(relative)
        for child in uncommented_inputs(relative):
            visit(child.removesuffix(".tex"), active + (relative,))

    visit(start, ())
    return reached


class Part2ReaderRouteTests(unittest.TestCase):
    def test_public_part_and_exact_source_order_with_audited_additions(self) -> None:
        driver = (HANDBOOK / "parts/p02.tex").read_text(encoding="utf-8")
        self.assertEqual(driver.count(r"\part{Classical Logic}\label{part:p02}"), 1)
        self.assertEqual(
            uncommented_inputs("parts/p02"),
            WRAPPERS[:8]
            + ["parts/p02/propositional-hilbert-tableaux"]
            + WRAPPERS[8:14]
            + ["parts/p02/propositional-metatheory-supplement"]
            + FIRST_ORDER_SYNTAX_WRAPPERS
            + FIRST_ORDER_SEMANTICS_WRAPPERS
            + FIRST_ORDER_THEORIES_WRAPPERS
            + FIRST_ORDER_DEDUCTION_WRAPPERS
            + FIRST_ORDER_COMPLETENESS_WRAPPERS
            + FIRST_ORDER_CARDINALITY_WRAPPERS
            + [
               "parts/p02/first-order-calculi-supplement",
               "parts/p02/first-order-completeness-remainder",
               "parts/p02/first-order-logic",
            ]
            + HIGHER_ORDER_WRAPPERS
            + [
               "parts/p02/second-and-higher-order-logic-supplement",
               "parts/p02/variants",
            ],
        )

    def test_competing_body_and_proof_fragment_are_retained_but_unreachable(self) -> None:
        historical = [
            "parts/p02/propositional-syntax-semantics",
            "annex/p02/propositional-syntax-semantics",
            "parts/p02/propositional-calculi",
            "annex/p02/propositional-calculi",
            "parts/p02/propositional-logic",
            "parts/p02/propositional-metatheory",
            "annex/p02/propositional-metatheory",
            "parts/p02/first-order-syntax-semantics",
            "annex/p02/first-order-syntax-semantics",
            "parts/p02/first-order-calculi",
            "annex/p02/first-order-calculi",
            "parts/p02/first-order-completeness",
            "annex/p02/first-order-completeness",
            "parts/p02/first-order-normal-forms",
            "annex/p02/first-order-normal-forms",
            "parts/p02/first-order-resolution",
            "annex/p02/first-order-resolution",
            "parts/p02/second-and-higher-order-logic",
            "annex/p02/higher-order",
        ]
        for relative in historical:
            self.assertTrue((HANDBOOK / f"{relative}.tex").is_file())
        live = set(reachable("parts/p02")) | set(reachable("annex/p02"))
        self.assertEqual(set(historical) & live, set())
        self.assertIn("parts/p02/propositional-hilbert-tableaux", live)
        self.assertIn("annex/p02/propositional-hilbert", live)
        self.assertIn("parts/p02/propositional-metatheory-supplement", live)
        self.assertIn("annex/p02/propositional-metatheory-supplement", live)
        self.assertIn("parts/p02/first-order-calculi-supplement", live)
        self.assertIn("annex/p02/first-order-calculi-supplement", live)
        self.assertIn("parts/p02/first-order-completeness-remainder", live)
        self.assertIn("annex/p02/first-order-completeness-remainder", live)
        self.assertIn("parts/p02/first-order-normal-forms-supplement", live)
        self.assertIn("parts/p02/first-order-resolution-supplement", live)
        self.assertIn("parts/p02/second-and-higher-order-logic-supplement", live)
        self.assertIn("annex/p02/higher-order-supplement", live)
        for removed in (
            "parts/p02/first-order-syntax-semantics-remainder",
            "annex/p02/first-order-syntax-semantics-remainder",
        ):
            self.assertNotIn(removed, live)
            self.assertFalse((HANDBOOK / f"{removed}.tex").exists())

    def test_retained_supplement_is_distinct_suffix_with_exact_ref_repair(self) -> None:
        historical = (
            HANDBOOK / "parts/p02/propositional-calculi.tex"
        ).read_text(encoding="utf-8")
        boundary = historical.index(
            r"\subsection{Hilbert calculus and the deduction theorem}"
        )
        expected = historical[boundary:]
        for title in (
            "Hilbert calculus and the deduction theorem",
            "Analytic tableaux",
            "Proof-system comparison",
        ):
            expected = expected.replace(
                rf"\subsection{{{title}}}", rf"\section{{{title}}}", 1
            )
        expected = expected.replace(
            r"Sound and refutationally complete, Theorems~\ref{thm:p02-resolution-soundness} and~\ref{thm:p02-resolution-completeness}",
            r"Sound by the inline theorem in \cref{sec:prop-metatheory-04}; finite refutational completeness is \cref{thm:prop-resolution-complete}, with the arbitrary-set extension stated in \cref{rem:resolution-finiteness}",
            1,
        )

        preamble = (
            "%% Additional propositional calculi retained after exact source restoration.\n"
            "\\noindent\\textit{Reader note.} The following Hilbert, tableau, and\n"
            "comparison material is a separately attributed addition to the inherited\n"
            "chapter above; it neither alters nor replaces the exact source rule displays.\n\n"
            "The retained Hilbert presentation and deduction theorem are attributed to\n"
            "\\cite{Mendelson1997}.\n\n"
        )
        supplement = (
            HANDBOOK / "parts/p02/propositional-hilbert-tableaux.tex"
        ).read_text(encoding="utf-8")
        self.assertTrue(supplement.startswith(preamble))
        self.assertEqual(supplement[len(preamble):], expected)

    def test_historical_reader_exclusion_is_exact_and_fails_closed(self) -> None:
        paths = set(handbook_check.HB_RETAINED_UNREACHABLE_READER_FILES)
        with tempfile.TemporaryDirectory(prefix="p2-reader-history-") as temporary:
            base = Path(temporary)
            bodies = {
                "main.tex": "",
                "parts/p02/propositional-hilbert-tableaux.tex": "",
                "parts/p02/propositional-metatheory-supplement.tex": "",
                "annex/p02/propositional-metatheory-supplement.tex": "",
                "restoration/scope-SRC-03022-03037.tex": "",
                "restoration/scope-SRC-12249-12261.tex": "",
            }
            for relative in paths:
                destination = base / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(HANDBOOK / relative, destination)
                bodies[relative] = destination.read_text(encoding="utf-8")

            data = handbook_check._HBData()
            self.assertEqual(
                handbook_check._hb_retained_unreachable_reader_files(
                    base, bodies, data
                ),
                paths,
            )
            self.assertEqual(data.findings, {})

            changed = "parts/p02/propositional-calculi.tex"
            with (base / changed).open("ab") as handle:
                handle.write(b"% mutation\n")
            changed_data = handbook_check._HBData()
            excluded = handbook_check._hb_retained_unreachable_reader_files(
                base, bodies, changed_data
            )
            self.assertNotIn(changed, excluded)
            self.assertTrue(changed_data.findings.get("duplicate-label"))

            shutil.copy2(HANDBOOK / changed, base / changed)
            reached = "annex/p02/propositional-calculi.tex"
            bodies["main.tex"] = rf"\input{{{reached}}}"
            route_data = handbook_check._HBData()
            excluded = handbook_check._hb_retained_unreachable_reader_files(
                base, bodies, route_data
            )
            self.assertNotIn(reached, excluded)
            self.assertTrue(route_data.findings.get("duplicate-label"))

    def test_retained_annex_is_exactly_the_distinct_hilbert_item(self) -> None:
        historical = (
            HANDBOOK / "annex/p02/propositional-calculi.tex"
        ).read_text(encoding="utf-8")
        boundary = historical.index(r"\begin{annexitem}{annex:p2.calc.2}")
        expected = (
            "%% Retained Hilbert-calculus proof after exact source restoration.\n"
            + historical[boundary:]
        )
        retained = (
            HANDBOOK / "annex/p02/propositional-hilbert.tex"
        ).read_text(encoding="utf-8")
        self.assertEqual(retained, expected)

    def test_first_order_deduction_supplements_are_exact_supported_ranges(self) -> None:
        historical_body_path = HANDBOOK / "parts/p02/first-order-calculi.tex"
        historical_annex_path = HANDBOOK / "annex/p02/first-order-calculi.tex"
        self.assertEqual(
            hashlib.sha256(historical_body_path.read_bytes()).hexdigest(),
            "ac38cba6e24cc9adcc6d95b1ddc8f4e45ea803fa486b7d642accdba2b5f52c1f",
        )
        self.assertEqual(
            hashlib.sha256(historical_annex_path.read_bytes()).hexdigest(),
            "8268564a38345e1299de69d5ac8226cb5d13b8e663f26b342099bcf29d830356",
        )

        body_lines = historical_body_path.read_text(encoding="utf-8").splitlines(
            keepends=True
        )
        body_range = "".join(body_lines[81:274])
        self.assertEqual(len(body_range.encode("utf-8")), 9545)
        self.assertEqual(
            hashlib.sha256(body_range.encode("utf-8")).hexdigest(),
            "b957125728c54061b4329a085f7af3981e56f4385e4dcb620bc0f1e253b705f6",
        )
        body_range = body_range.replace(
            r"Theorem~\ref{thm:p02-fol-nd-soundness}",
            r"Theorem~\ref{thm:fol-soundness}",
            1,
        ).replace(
            r"Theorem~\ref{thm:p02-fol-lk-soundness}",
            r"Theorem~\ref{thm:fol-lk-soundness}",
            1,
        ).replace(
            r"Theorem~\ref{thm:p02-equality-congruence}",
            r"Lemma~\ref{lem:equality-congruence}",
            1,
        ).replace(
            "Theorems~\\ref{thm:p02-fol-completeness} and\n"
            r"\ref{thm:p02-fol-completeness-countable}",
            "Theorem~\\ref{thm:fol-completeness} and\n"
            r"Corollary~\ref{cor:fol-completeness-countable}",
            1,
        ).replace(
            r"Theorem~\ref{thm:p02-fol-lk-completeness}",
            r"Theorem~\ref{thm:fol-lk-completeness}",
            1,
        )
        body_preamble = (
            "%% Distinct first-order calculi additions retained after exact source restoration.\n"
            "\\noindent\\textbf{OPEN.} The following equality, Hilbert, tableau, and\n"
            "comparison material is separately attributed editorial apparatus.  It does\n"
            "not alter, normalize, or replace the exact inherited natural-deduction or\n"
            "sequent-rule displays above.  The equality laws have the supplied annex\n"
            "derivation; the Hilbert material is attributed to\n"
            "\\cite{Mendelson1997,Enderton2001}, and tableau adequacy to\n"
            "\\cite{Smullyan1968}.  The separately identified registry sheets provide\n"
            "navigation and variant context, not source substitutes; their added policies\n"
            "and notation do not change the exact inherited calculi.  This placement does\n"
            "not close D-P3-001, D-P3-002, D-P3-011, A-037, or any review or admission\n"
            "gate.\n\n"
        )
        self.assertEqual(
            (HANDBOOK / "parts/p02/first-order-calculi-supplement.tex").read_text(
                encoding="utf-8"
            ),
            body_preamble + body_range,
        )

        annex_lines = historical_annex_path.read_text(encoding="utf-8").splitlines(
            keepends=True
        )
        annex_range = "".join(annex_lines[59:92])
        self.assertEqual(len(annex_range.encode("utf-8")), 1743)
        self.assertEqual(
            hashlib.sha256(annex_range.encode("utf-8")).hexdigest(),
            "9346e16d657f0470ea889696e64e0168ff8d9963a57d18a287bfc8bb56333832",
        )
        annex_preamble = (
            "%% Distinct first-order calculi proofs retained after exact source restoration.\n"
            "\\noindent\\textbf{OPEN.} These two separately attributed editorial proofs\n"
            "support only the retained equality and Hilbert additions.  The inherited\n"
            "reduct and soundness proofs remain exact in the body and are not repeated;\n"
            "historical items .1--.3 remain on disk only.  Registry sheets provide\n"
            "navigation and variant context, not source replacement.  No review,\n"
            "admission, or register gate is closed here.\n\n"
        )
        self.assertEqual(
            (HANDBOOK / "annex/p02/first-order-calculi-supplement.tex").read_text(
                encoding="utf-8"
            ),
            annex_preamble + annex_range,
        )

    def test_first_order_completeness_remainders_keep_only_exact_open_ranges(self) -> None:
        historical_body_path = HANDBOOK / "parts/p02/first-order-completeness.tex"
        historical_annex_path = HANDBOOK / "annex/p02/first-order-completeness.tex"
        self.assertEqual(
            hashlib.sha256(historical_body_path.read_bytes()).hexdigest(),
            "fa0f9c6075cb85bb79dd280f254355ac297d415eddfc21d8c70e3e14de94ab95",
        )
        self.assertEqual(
            hashlib.sha256(historical_annex_path.read_bytes()).hexdigest(),
            "f7b25a11112feebfd04a88a670ffbc6267e61d9adcec4d07498668ec692eaef0",
        )

        body_lines = historical_body_path.read_text(encoding="utf-8").splitlines(
            keepends=True
        )
        body_range = "".join(body_lines[313:371])
        self.assertEqual(len(body_range.encode("utf-8")), 2819)
        self.assertEqual(
            hashlib.sha256(body_range.encode("utf-8")).hexdigest(),
            "fec359188e90a3d1ad1b822bba15c1fd680c655501fd75106983a392e1d5eb2f",
        )
        body_preamble = (
            "%% parts/p02/first-order-completeness-remainder.tex --- retained OPEN additions\n"
            "\\noindent\\textbf{OPEN.} The exact inherited chapter through source line 6048 now\n"
            "replaces the earlier elementary-substructure and L\\\"owenheim--Skolem overlap.\n"
            "The following separately attributed historical lines 314--371 retain only\n"
            "the D-P3-013 elementary-diagram and internal--external calibrations.  They\n"
            "remain unadmitted and close no content, AI, build, visual, register, or\n"
            "publication gate.\n\n"
        )
        self.assertEqual(
            (HANDBOOK / "parts/p02/first-order-completeness-remainder.tex").read_text(
                encoding="utf-8"
            ),
            body_preamble + body_range,
        )

        annex_lines = historical_annex_path.read_text(encoding="utf-8").splitlines(
            keepends=True
        )
        annex_range = "".join(annex_lines[302:338])
        self.assertEqual(len(annex_range.encode("utf-8")), 1959)
        self.assertEqual(
            hashlib.sha256(annex_range.encode("utf-8")).hexdigest(),
            "e2581b6dd722e65becfb4d3a50eec8f96e790362ff1c9b4bc035e809f8856758",
        )
        annex_preamble = (
            "%% annex/p02/first-order-completeness-remainder.tex --- retained OPEN proofs\n"
            "\\noindent\\textbf{OPEN.} The exact inherited proofs through source line 6048\n"
            "replace historical annex items 2.2.17--2.2.19.  The following exact historical\n"
            "lines 303--338 support only the separately attributed D-P3-013 additions.\n"
            "They remain unadmitted and do not replace inherited proofs or close any\n"
            "content, AI, build, visual, register, or publication gate.\n\n"
        )
        self.assertEqual(
            (HANDBOOK / "annex/p02/first-order-completeness-remainder.tex").read_text(
                encoding="utf-8"
            ),
            annex_preamble + annex_range,
        )

    def test_exact_source_part_and_chapter_labels_appear_once_on_live_part2_route(self) -> None:
        surface = "\n".join(
            (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            for relative in reachable("parts/p02")
        )
        self.assertEqual(surface.count(r"\part{Classical Propositional Logic}"), 1)
        self.assertEqual(surface.count(r"\label{part:classical-propositional}"), 1)
        self.assertEqual(surface.count(r"\chapter{Propositional Syntax and Semantics}"), 1)
        self.assertEqual(surface.count(r"\label{ch:prop-syntax-semantics}"), 1)
        self.assertEqual(surface.count(r"\chapter{Natural Deduction and Sequents}"), 1)
        self.assertEqual(surface.count(r"\label{ch:prop-deduction}"), 1)
        self.assertEqual(
            surface.count(
                r"\chapter{Soundness, Completeness, Compactness, and Resolution}"
            ),
            1,
        )
        self.assertEqual(surface.count(r"\label{ch:prop-metatheory}"), 1)
        self.assertEqual(surface.count(r"\part{Classical First-Order Logic}"), 1)
        self.assertEqual(surface.count(r"\label{part:classical-first-order}"), 1)
        self.assertEqual(surface.count(r"\chapter{First-Order Syntax}"), 1)
        self.assertEqual(surface.count(r"\label{ch:fol-syntax-semantics}"), 1)
        self.assertEqual(
            surface.count(r"\chapter{Structures, Satisfaction, and Translation}"),
            1,
        )
        self.assertEqual(surface.count(r"\label{ch:fol-semantics}"), 1)
        self.assertEqual(surface.count(r"\chapter{Theories and Axiomatization}"), 1)
        self.assertEqual(surface.count(r"\label{ch:fol-theories}"), 1)
        self.assertEqual(surface.count(r"\chapter{First-Order Deduction}"), 1)
        self.assertEqual(surface.count(r"\label{ch:fol-deduction}"), 1)
        self.assertEqual(
            surface.count(r"\chapter{Henkin Completeness and Compactness}"), 1
        )
        self.assertEqual(surface.count(r"\label{ch:fol-metatheory}"), 1)

    def test_exact_first_order_syntax_surface_is_complete(self) -> None:
        surface = "".join(
            (HANDBOOK / f"{artifact}.tex").read_text(encoding="utf-8")
            for wrapper in FIRST_ORDER_SYNTAX_WRAPPERS
            for artifact in uncommented_inputs(wrapper)
        )
        expected_environments = {
            "definition": 9,
            "example": 2,
            "theorem": 1,
            "lemma": 3,
            "proof": 4,
            "enumerate": 3,
            "aligned": 2,
            "cases": 1,
        }
        for environment, count in expected_environments.items():
            self.assertEqual(surface.count(rf"\begin{{{environment}}}"), count)
        self.assertEqual(surface.count(r"\cite{"), 3)
        self.assertEqual(surface.count(r"\index{"), 0)
        self.assertEqual(
            re.findall(r"\\cref\{([^{}]+)\}", surface),
            [
                "thm:prop-unique-readability",
                "lem:substitution-complexity",
                "lem:substitution-complexity",
                "lem:substitution-fv",
                "lem:substitution-fv",
                "lem:substitution-complexity",
            ],
        )

    def test_exact_first_order_semantics_surface_is_complete(self) -> None:
        surface = "".join(
            (HANDBOOK / f"{artifact}.tex").read_text(encoding="utf-8")
            for wrapper in FIRST_ORDER_SEMANTICS_WRAPPERS
            for artifact in uncommented_inputs(wrapper)
        )
        expected_environments = {
            "definition": 6,
            "lemma": 3,
            "theorem": 1,
            "corollary": 2,
            "proof": 6,
            "example": 2,
            "enumerate": 1,
            "aligned": 1,
            "cases": 1,
        }
        for environment, count in expected_environments.items():
            self.assertEqual(surface.count(rf"\begin{{{environment}}}"), count)
        self.assertEqual(surface.count(r"\chapter{"), 1)
        self.assertEqual(surface.count(r"\section{"), 3)
        self.assertEqual(surface.count(r"\Meta"), 84)
        self.assertEqual(surface.count(r"\abs{\Meta}"), 10)
        self.assertEqual(surface.count(r"\sem{"), 18)
        self.assertEqual(surface.count(r"\equiv"), 3)
        self.assertIn(r"\varphi\equiv\psi", surface)
        self.assertEqual(surface.count(r"\cite{"), 0)
        self.assertEqual(surface.count(r"\index{"), 0)
        self.assertEqual(
            re.findall(r"\\cref\{([^{}]+)\}", surface),
            [
                "lem:term-substitution",
                "lem:substitution-complexity",
                "lem:substitution-complexity",
                "thm:fol-substitution",
                "lem:fol-coincidence",
            ],
        )

    def test_exact_source_notation_does_not_promote_open_register_obligations(self) -> None:
        with (ROOT / "spec/register-obligation-closure.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            closure = list(csv.DictReader(handle))
        by_id = {row["obligation_id"]: row for row in closure}
        for obligation in (
            "OBL::defects::S-002",
            "OBL::defects::S-003",
            "OBL::apparatus::A-172",
            "OBL::depth-gaps::D-P3-010",
            "OBL::depth-gaps::D-P3-013",
            "OBL::defects::R-024",
        ):
            self.assertEqual(by_id[obligation]["completion_status"], "OPEN")

    def test_exact_first_order_theories_surface_is_complete(self) -> None:
        surface = "".join(
            (HANDBOOK / f"{artifact}.tex").read_text(encoding="utf-8")
            for wrapper in FIRST_ORDER_THEORIES_WRAPPERS
            for artifact in uncommented_inputs(wrapper)
        )
        expected_environments = {
            "definition": 2,
            "example": 4,
            "aligned": 2,
            "theorem": 1,
            "enumerate": 2,
            "proof": 1,
            "warning": 1,
        }
        for environment, count in expected_environments.items():
            self.assertEqual(surface.count(rf"\begin{{{environment}}}"), count)
        self.assertEqual(surface.count(r"\chapter{"), 1)
        self.assertEqual(surface.count(r"\section{"), 1)
        self.assertEqual(surface.count(r"\label{"), 4)
        self.assertEqual(surface.count(r"\Th"), 3)
        self.assertEqual(surface.count(r"\Cn"), 1)
        self.assertEqual(surface.count(r"\FOL"), 2)
        self.assertEqual(surface.count(r"\cite{"), 0)
        self.assertEqual(surface.count(r"\index{"), 0)
        self.assertEqual(surface.count(r"\begin{longtable}"), 0)
        self.assertEqual(
            re.findall(r"\\cref\{([^{}]+)\}", surface),
            [
                "thm:definitional-conservativity",
                "lem:reduct-invariance",
                "ch:fol-deduction",
                "lem:fol-coincidence",
                "thm:fol-soundness",
                "thm:fol-completeness",
            ],
        )

    def test_exact_first_order_deduction_surface_is_complete(self) -> None:
        surface = "".join(
            (HANDBOOK / f"{artifact}.tex").read_text(encoding="utf-8")
            for wrapper in FIRST_ORDER_DEDUCTION_WRAPPERS
            for artifact in uncommented_inputs(wrapper)
        )
        expected_environments = {
            "definition": 1,
            "lemma": 1,
            "proof": 3,
            "example": 3,
            "array": 6,
            "theorem": 2,
            "warning": 1,
            "enumerate": 1,
            "exercise": 9,
        }
        for environment, count in expected_environments.items():
            self.assertEqual(surface.count(rf"\begin{{{environment}}}"), count)
        self.assertEqual(surface.count(r"\chapter{"), 1)
        self.assertEqual(surface.count(r"\section{"), 5)
        self.assertEqual(surface.count(r"\Rule"), 12)
        self.assertEqual(surface.count(r"\side{"), 3)
        self.assertEqual(surface.count(r"\label{"), 18)
        self.assertEqual(surface.count(r"\FOL"), 11)
        self.assertEqual(surface.count(r"\cite{"), 0)
        self.assertEqual(surface.count(r"\index{"), 0)
        self.assertEqual(surface.count(r"\begin{longtable}"), 0)
        self.assertEqual(
            re.findall(r"\\cref\{([^{}]+)\}", surface),
            [
                "ch:fol-syntax-semantics",
                "sec:fol-syntax-semantics-04",
                "thm:prop-nd-soundness",
                "thm:prop-lk-soundness",
                "thm:fol-substitution",
                "lem:fol-coincidence",
                "thm:fol-soundness",
            ],
        )

    def test_exact_first_order_completeness_surface_is_complete(self) -> None:
        surface = "".join(
            (HANDBOOK / f"{artifact}.tex").read_text(encoding="utf-8")
            for wrapper in FIRST_ORDER_COMPLETENESS_WRAPPERS
            for artifact in uncommented_inputs(wrapper)
        )
        expected_environments = {
            "definition": 3,
            "lemma": 10,
            "proof": 15,
            "theorem": 3,
            "corollary": 2,
            "enumerate": 3,
        }
        for environment, count in expected_environments.items():
            self.assertEqual(surface.count(rf"\begin{{{environment}}}"), count)
        self.assertEqual(surface.count(r"\chapter{"), 1)
        self.assertEqual(surface.count(r"\section{"), 4)
        self.assertEqual(surface.count(r"\label{"), 19)
        self.assertEqual(surface.count(r"\item"), 9)
        self.assertEqual(surface.count(r"\Rule[Cut]"), 1)
        self.assertEqual(surface.count(r"\begin{proof}[Proof sketch]"), 1)
        self.assertEqual(surface.count(r"\cite{"), 2)
        self.assertEqual(surface.count(r"\index{"), 0)
        self.assertIn(r"\abs{\Meta_\Delta}", surface)
        self.assertIn(r"\sem{t}^{\Meta_\Delta}_{s_0}", surface)
        self.assertEqual(
            re.findall(r"\\cite\{([^{}]+)\}", surface),
            ["Godel1930", "Henkin1949"],
        )
        self.assertEqual(
            set(re.findall(r"\\label\{([^{}]+)\}", surface)),
            {
                "ch:fol-metatheory",
                "sec:fol-metatheory-01",
                "lem:quantifier-duality",
                "lem:fresh-constant",
                "lem:witness-extension",
                "lem:new-constant-elimination",
                "lem:transfinite-lindenbaum",
                "lem:henkin-lindenbaum",
                "sec:fol-metatheory-02",
                "lem:equality-congruence",
                "lem:term-model-evaluation",
                "lem:quantifier-membership",
                "lem:fol-truth",
                "sec:fol-metatheory-03",
                "thm:fol-completeness",
                "cor:fol-completeness-countable",
                "thm:fol-lk-completeness",
                "sec:fol-metatheory-04",
                "thm:fol-compactness",
            },
        )

    def test_exact_cardinality_normal_forms_and_resolution_surface_is_complete(self) -> None:
        surface = "".join(
            (HANDBOOK / f"{artifact}.tex").read_text(encoding="utf-8")
            for wrapper in FIRST_ORDER_CARDINALITY_WRAPPERS
            for artifact in uncommented_inputs(wrapper)
        )
        expected_environments = {
            "definition": 12,
            "lemma": 5,
            "theorem": 10,
            "proof": 13,
            "example": 2,
            "exercise": 10,
            "enumerate": 6,
            "aligned": 3,
            "cases": 1,
            "gathered": 1,
            "longtable": 1,
        }
        for environment, count in expected_environments.items():
            self.assertEqual(surface.count(rf"\begin{{{environment}}}"), count)
        self.assertEqual(surface.count(r"\chapter{"), 1)
        self.assertEqual(surface.count(r"\section{"), 6)
        self.assertEqual(len(re.findall(r"(?m)^\s*\\item\b", surface)), 21)
        self.assertEqual(surface.count(r"\begin{proof}[Proof sketch]"), 2)
        self.assertEqual(surface.count(r"\Rule"), 2)
        self.assertEqual(surface.count(r"\label{"), 29)
        self.assertEqual(surface.count(r"\index{"), 0)
        self.assertEqual(surface.count(r"\cite{"), 2)
        for token, count in {
            r"\abs": 37,
            r"\equiv": 23,
            r"\defeq": 12,
            r"\preccurlyeq": 6,
            r"\doteq": 8,
            r"\sem": 3,
        }.items():
            self.assertEqual(surface.count(token), count, token)
        self.assertEqual(
            re.findall(r"\\cite\{([^{}]+)\}", surface),
            [
                "Robinson1965,BachmairGanzinger2001",
                "Robinson1965,BachmairGanzinger2001",
            ],
        )
        self.assertEqual(
            re.findall(r"\\(?:c|C)ref\{([^{}]+)\}", surface),
            [
                "cor:syntax-counting",
                "thm:infinite-cardinal-finite-coding",
                "def:fol-theory-satisfiability",
                "lem:substitution-complexity",
                "lem:substitution-fv",
                "lem:substitution-complexity",
                "cor:alpha-invariance",
                "lem:fol-coincidence",
                "lem:fol-coincidence",
                "lem:fol-coincidence",
                "lem:fol-nnf,lem:rectified-variant,lem:prenex-extraction",
                "lem:fol-nnf",
                "lem:rectified-variant",
                "lem:prenex-extraction",
                "lem:fol-coincidence",
                "lem:reduct-invariance",
                "thm:fol-substitution",
                "thm:fol-substitution",
                "lem:reduct-invariance",
                "lem:clause-substitution",
                "lem:clause-substitution",
                "thm:herbrand-clauses,thm:resolution-lifting",
                "thm:herbrand-clauses",
                "thm:resolution-lifting",
            ],
        )
        self.assertEqual(
            set(re.findall(r"\\label\{([^{}]+)\}", surface)),
            {
                "ch:fol-cardinality-normalforms",
                "sec:fol-cardinality-normalforms-01",
                "thm:tarski-vaught-fol",
                "sec:fol-cardinality-normalforms-02",
                "thm:downward-ls",
                "thm:upward-ls",
                "sec:fol-cardinality-normalforms-03",
                "lem:fol-nnf",
                "lem:rectified-variant",
                "lem:prenex-extraction",
                "thm:prenex-normal-form",
                "thm:skolem-equisatisfiable",
                "sec:fol-cardinality-normalforms-04",
                "lem:clause-substitution",
                "thm:herbrand-clauses",
                "thm:resolution-lifting",
                "thm:fol-resolution",
                "sec:fol-cardinality-normalforms-05",
                "sec:fol-cardinality-normalforms-06",
                *(f"ex:fol-cardinality-normalforms-{number:02d}" for number in range(1, 11)),
            },
        )

    def test_first_order_historical_files_are_byte_pinned(self) -> None:
        expected = {
            "parts/p02/first-order-syntax-semantics.tex":
                "5a737c791bf8e24a98f8bdc97c75b7257ac33cd9596d535e3fa5dffd96bd83d4",
            "annex/p02/first-order-syntax-semantics.tex":
                "8f0cf70d498925661e03430b12a611836f80f9a31550cc34022a11fbfcd8492e",
        }
        for relative, digest in expected.items():
            self.assertEqual(
                hashlib.sha256((HANDBOOK / relative).read_bytes()).hexdigest(),
                digest,
            )

    def test_first_order_theory_overlap_copies_are_removed_without_historical_loss(self) -> None:
        historical_body = (
            HANDBOOK / "parts/p02/first-order-syntax-semantics.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        expected_body = "".join(historical_body[439:548])
        self.assertEqual(len(expected_body.encode("utf-8")), 4837)
        self.assertEqual(
            hashlib.sha256(expected_body.encode("utf-8")).hexdigest(),
            "3cfd276ed4762246270d9c44dae0c783f39657bc8febe475a435d2cd92f37a2e",
        )

        historical_annex = (
            HANDBOOK / "annex/p02/first-order-syntax-semantics.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        expected_annex = "".join(historical_annex[117:148])
        self.assertEqual(len(expected_annex.encode("utf-8")), 1610)
        self.assertEqual(
            hashlib.sha256(expected_annex.encode("utf-8")).hexdigest(),
            "247e7ca2ff5663b945092038b3338604a4275f43aa75ddf357d0a4ee0faaea57",
        )
        for removed in (
            "parts/p02/first-order-syntax-semantics-remainder.tex",
            "annex/p02/first-order-syntax-semantics-remainder.tex",
        ):
            self.assertFalse((HANDBOOK / removed).exists())

        self.assertNotIn(
            "first-order-syntax-semantics-remainder",
            (HANDBOOK / "parts/p02/first-order-logic.tex").read_text(
                encoding="utf-8"
            ),
        )
        self.assertNotIn(
            "first-order-syntax-semantics-remainder",
            (HANDBOOK / "annex/p02.tex").read_text(encoding="utf-8"),
        )

    def test_first_order_overlap_labels_and_annex_items_are_not_live(self) -> None:
        historical_body = (
            HANDBOOK / "parts/p02/first-order-syntax-semantics.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        retired = set(re.findall(r"\\label\s*\{([^{}]+)\}", "".join(historical_body[:439])))
        retired.update(TYPED_LABEL_RE.findall("".join(historical_body[:439])))
        live_surface = "\n".join(
            (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            for relative in reachable("main")
        )
        live_labels = set(re.findall(r"\\label\s*\{([^{}]+)\}", live_surface))
        live_labels.update(TYPED_LABEL_RE.findall(live_surface))
        live_refs = {
            target.strip()
            for match in REF_RE.finditer(live_surface)
            for target in (match.group(1) or match.group(2)).split(",")
        }
        self.assertEqual(retired & live_labels, set())
        self.assertEqual(retired & live_refs, set())
        for number in range(1, 12):
            self.assertNotIn(f"annex:p2.2.syn.{number}", live_labels)
        self.assertFalse(
            (HANDBOOK / "parts/p02/first-order-syntax-semantics-remainder.tex").exists()
        )
        self.assertFalse(
            (HANDBOOK / "annex/p02/first-order-syntax-semantics-remainder.tex").exists()
        )

    def test_first_order_semantics_consumers_use_only_genuine_source_destinations(self) -> None:
        expected_by_file = {
            "annex/p02/first-order-calculi.tex": (
                r"Corollary~\ref{cor:alpha-invariance}",
                r"Theorem~\ref{thm:fol-substitution}",
            ),
            "parts/p12/formal-workflow.tex": (
                r"Theorem~\ref{thm:fol-substitution}",
            ),
            "parts/p02/variants.tex": (
                r"satisfaction definition in Section~\ref{sec:fol-semantics-02}",
            ),
        }
        for relative, required in expected_by_file.items():
            body = (HANDBOOK / relative).read_text(encoding="utf-8")
            for phrase in required:
                self.assertIn(phrase, body, relative)

        variants = (HANDBOOK / "parts/p02/variants.tex").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "Term evaluation and the atomic and Boolean clauses are those of\n"
            "the recursive satisfaction definition in "
            r"Section~\ref{sec:fol-semantics-02}",
            variants,
        )
        self.assertNotIn("those of\nThe recursive satisfaction definition", variants)

        live = "\n".join(
            (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            for relative in reachable("main")
        )
        live_labels = set(re.findall(r"\\label\s*\{([^{}]+)\}", live))
        live_labels.update(TYPED_LABEL_RE.findall(live))
        live_refs = {
            target.strip()
            for match in REF_RE.finditer(live)
            for target in (match.group(1) or match.group(2)).split(",")
        }
        for retired in (
            "thm:p02-fol-alpha-invariance",
            "thm:p02-fol-substitution",
            "def:p02-fol-satisfaction",
        ):
            self.assertNotIn(retired, live_labels)
            self.assertNotIn(retired, live_refs)

    def test_first_order_deduction_consumers_use_only_genuine_source_destinations(self) -> None:
        expected_by_file = {
            "parts/p02/first-order-depth.tex": ("thm:fol-soundness",),
            "parts/p07/calculi-and-derivability.tex": ("thm:fol-lk-soundness",),
            "parts/p02/first-order-calculi-supplement.tex": (
                "thm:fol-soundness",
                "thm:fol-lk-soundness",
            ),
        }
        for relative, labels in expected_by_file.items():
            body = (HANDBOOK / relative).read_text(encoding="utf-8")
            for label in labels:
                self.assertIn(label, body, relative)

        live = "\n".join(
            (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            for relative in reachable("main")
        )
        live_labels = set(re.findall(r"\\label\s*\{([^{}]+)\}", live))
        live_labels.update(TYPED_LABEL_RE.findall(live))
        live_refs = {
            target.strip()
            for match in REF_RE.finditer(live)
            for target in (match.group(1) or match.group(2)).split(",")
        }
        for retired in (
            "thm:p02-fol-nd-soundness",
            "thm:p02-fol-lk-soundness",
        ):
            self.assertNotIn(retired, live_labels)
            self.assertNotIn(retired, live_refs)

    def test_first_order_completeness_consumers_use_only_genuine_source_destinations(self) -> None:
        expected_by_file = {
            "parts/p02/first-order-calculi-supplement.tex": (
                "lem:equality-congruence",
                "thm:fol-completeness",
                "cor:fol-completeness-countable",
                "thm:fol-lk-completeness",
            ),
            "parts/p02/first-order-depth.tex": (
                "sec:fol-metatheory-02",
                "thm:fol-completeness",
                "cor:fol-completeness-countable",
                "thm:fol-compactness",
            ),
            "parts/p06/cardinals-choice.tex": (
                "cor:fol-completeness-countable",
                "thm:fol-completeness",
            ),
            "parts/p07/calculi-and-derivability.tex": (
                "thm:fol-lk-completeness",
            ),
        }
        for relative, labels in expected_by_file.items():
            body = (HANDBOOK / relative).read_text(encoding="utf-8")
            for label in labels:
                self.assertIn(label, body, relative)

        depth = (HANDBOOK / "parts/p02/first-order-depth.tex").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            r"The term structure in Section~\ref{sec:fol-metatheory-02}",
            depth,
        )
        self.assertIn(
            "AC in this handbook's derivation; complete inherited proof,\n"
            r"Theorem~\ref{thm:fol-compactness}",
            depth,
        )

        live = "\n".join(
            (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            for relative in reachable("main")
        )
        for retired in (
            "thm:p02-equality-congruence",
            "thm:p02-fol-completeness",
            "thm:p02-fol-completeness-countable",
            "thm:p02-fol-lk-completeness",
            "thm:p02-fol-compactness",
            "def:p02-henkin-term-structure",
        ):
            self.assertNotIn(retired, live)

    def test_cardinality_normal_forms_and_resolution_supplements_are_exact_open_slices(self) -> None:
        historical_hashes = {
            "parts/p02/first-order-completeness.tex":
                "fa0f9c6075cb85bb79dd280f254355ac297d415eddfc21d8c70e3e14de94ab95",
            "annex/p02/first-order-completeness.tex":
                "f7b25a11112feebfd04a88a670ffbc6267e61d9adcec4d07498668ec692eaef0",
            "parts/p02/first-order-normal-forms.tex":
                "4e4594b277c315f658a0f2e586dc3139aed3d0abedfe29132de168ab5c54a8ba",
            "annex/p02/first-order-normal-forms.tex":
                "d300a9a54a76d21abb5c5300198ab1404a2d26e5148059f51ef85154b9e8e237",
            "parts/p02/first-order-resolution.tex":
                "f0d6c96e4215241247595e03432166017b9605b900fe14e2b78f0f3ab8c466c0",
            "annex/p02/first-order-resolution.tex":
                "2fabb80918d495f4f419b479d319bd90875ab77996d4a53fe82293e7f091f19c",
        }
        for relative, digest in historical_hashes.items():
            self.assertEqual(
                hashlib.sha256((HANDBOOK / relative).read_bytes()).hexdigest(),
                digest,
            )

        historical_completeness = (
            HANDBOOK / "parts/p02/first-order-completeness.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        historical_completeness_annex = (
            HANDBOOK / "annex/p02/first-order-completeness.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        body_slice = "".join(historical_completeness[313:371])
        annex_slice = "".join(historical_completeness_annex[302:338])
        self.assertEqual(len(body_slice.encode("utf-8")), 2819)
        self.assertEqual(
            hashlib.sha256(body_slice.encode("utf-8")).hexdigest(),
            "fec359188e90a3d1ad1b822bba15c1fd680c655501fd75106983a392e1d5eb2f",
        )
        self.assertEqual(len(annex_slice.encode("utf-8")), 1959)
        self.assertEqual(
            hashlib.sha256(annex_slice.encode("utf-8")).hexdigest(),
            "e2581b6dd722e65becfb4d3a50eec8f96e790362ff1c9b4bc035e809f8856758",
        )

        normal_lines = (
            HANDBOOK / "parts/p02/first-order-normal-forms.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        quantifier_slice = "".join(normal_lines[83:133])
        pipeline_slice = "".join(normal_lines[260:357])
        self.assertEqual(
            hashlib.sha256(quantifier_slice.encode("utf-8")).hexdigest(),
            "16fcd0bc7b51fc4d96955d59c8e649699fac2782361ab751ef6ce9397e1e24c7",
        )
        self.assertEqual(
            hashlib.sha256(pipeline_slice.encode("utf-8")).hexdigest(),
            "2fe27881844f717d8367b52264e7945d1fc405c27e1c32c07b0bd15dd930135e",
        )

        resolution_lines = (
            HANDBOOK / "parts/p02/first-order-resolution.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        figure_slice = "".join(resolution_lines[170:195])
        self.assertEqual(
            hashlib.sha256(figure_slice.encode("utf-8")).hexdigest(),
            "04be72e1be209993f175350a2c45d292eb37104583ac1cbb8018b3391f269971",
        )

        body_preamble = (
            "%% parts/p02/first-order-completeness-remainder.tex --- retained OPEN additions\n"
            "\\noindent\\textbf{OPEN.} The exact inherited chapter through source line 6048 now\n"
            "replaces the earlier elementary-substructure and L\\\"owenheim--Skolem overlap.\n"
            "The following separately attributed historical lines 314--371 retain only\n"
            "the D-P3-013 elementary-diagram and internal--external calibrations.  They\n"
            "remain unadmitted and close no content, AI, build, visual, register, or\n"
            "publication gate.\n\n"
        )
        annex_preamble = (
            "%% annex/p02/first-order-completeness-remainder.tex --- retained OPEN proofs\n"
            "\\noindent\\textbf{OPEN.} The exact inherited proofs through source line 6048\n"
            "replace historical annex items 2.2.17--2.2.19.  The following exact historical\n"
            "lines 303--338 support only the separately attributed D-P3-013 additions.\n"
            "They remain unadmitted and do not replace inherited proofs or close any\n"
            "content, AI, build, visual, register, or publication gate.\n\n"
        )
        self.assertEqual(
            (HANDBOOK / "parts/p02/first-order-completeness-remainder.tex").read_text(encoding="utf-8"),
            body_preamble + body_slice,
        )
        self.assertEqual(
            (HANDBOOK / "annex/p02/first-order-completeness-remainder.tex").read_text(encoding="utf-8"),
            annex_preamble + annex_slice,
        )

        normal_preamble = (
            "%% parts/p02/first-order-normal-forms-supplement.tex --- retained OPEN additions\n"
            "\\section*{Editorial normal-form additions}\n"
            "\\addcontentsline{toc}{section}{Editorial normal-form additions}\n"
            "\\noindent\\textbf{OPEN.} The exact inherited chapter supplies the governing\n"
            "normal-form definitions, results, and proofs.  The following exact historical\n"
            "slices retain only A-033 and D-P3-012/A-034/A-118 editorial additions.\n"
            "They remain separately attributed and unadmitted, do not replace or alter the\n"
            "inherited source, and close no content, AI, build, visual, register, or\n"
            "publication gate.\n\n"
        )
        self.assertEqual(
            (HANDBOOK / "parts/p02/first-order-normal-forms-supplement.tex").read_text(encoding="utf-8"),
            normal_preamble + quantifier_slice + "\n" + pipeline_slice,
        )
        resolution_preamble = (
            "%% parts/p02/first-order-resolution-supplement.tex --- retained OPEN figure\n"
            "\\section*{Editorial resolution figure}\n"
            "\\addcontentsline{toc}{section}{Editorial resolution figure}\n"
            "\\noindent\\textbf{OPEN.} The exact inherited chapter supplies the governing\n"
            "resolution definitions, rules, results, and proofs.  The following exact\n"
            "historical slice retains only the A-121 editorial derivation figure.  It is\n"
            "unadmitted, does not replace or alter the inherited source, and closes no\n"
            "content, AI, build, visual, register, or publication gate.\n\n"
        )
        self.assertEqual(
            (HANDBOOK / "parts/p02/first-order-resolution-supplement.tex").read_text(encoding="utf-8"),
            resolution_preamble + figure_slice,
        )
        self.assertNotIn("Skolemization boundary", normal_preamble + quantifier_slice + pipeline_slice)

    def test_cardinality_normal_forms_and_resolution_consumers_use_only_genuine_source_destinations(self) -> None:
        expected_by_file = {
            "parts/p02/first-order-depth.tex": (
                "thm:herbrand-clauses",
                "thm:downward-ls",
                "thm:upward-ls",
                "complete inherited proof",
            ),
            "parts/p06/cardinals-choice.tex": ("thm:downward-ls",),
            "parts/p12/first-order-automation.tex": (
                "sec:fol-cardinality-normalforms-04",
                "thm:fol-resolution",
            ),
            "parts/p12/further-reading.tex": (
                "sec:fol-cardinality-normalforms-04",
                "thm:fol-resolution",
            ),
        }
        for relative, required in expected_by_file.items():
            body = (HANDBOOK / relative).read_text(encoding="utf-8")
            for phrase in required:
                self.assertIn(phrase, body, relative)

        automation = (
            HANDBOOK / "parts/p12/first-order-automation.tex"
        ).read_text(encoding="utf-8")
        self.assertNotIn("canonical registered surface", automation)
        self.assertIn("does not invent labels for the unlabeled source units", automation)

        registry = (
            HANDBOOK / "registry/calculi/resolution-fol.tex"
        ).read_text(encoding="utf-8")
        registry_prose = registry.replace("\n% ", " ")
        self.assertIn("Separately identified editorial lookup", registry_prose)
        self.assertIn("does not replace", registry_prose)
        self.assertIn("A-018", registry_prose)
        self.assertIn("OPEN", registry_prose)
        self.assertNotIn("EXTRACTED from", registry)

        live = "\n".join(
            (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            for relative in reachable("main")
        )
        live_labels = set(re.findall(r"\\label\s*\{([^{}]+)\}", live))
        live_labels.update(TYPED_LABEL_RE.findall(live))
        live_refs = {
            target.strip()
            for match in REF_RE.finditer(live)
            for target in (match.group(1) or match.group(2)).split(",")
        }
        for retired in (
            "thm:p02-tarski-vaught",
            "thm:p02-downward-ls",
            "thm:p02-upward-ls",
            "thm:p02-fol-nnf",
            "thm:p02-fol-rectification",
            "thm:p02-fol-prenex-extraction",
            "thm:p02-fol-prenex",
            "thm:p02-skolem-equisatisfiable",
            "thm:p02-fol-clause-substitution",
            "thm:p02-herbrand-clauses",
            "thm:p02-resolution-lifting",
            "thm:p02-fol-resolution-completeness",
            "thm:p02-fol-resolution-soundness",
            "thm:p02-fol-unification",
            "def:p02-fol-simultaneous-substitution",
            "def:p02-fol-instance-preorder",
            "def:p02-fol-mgu",
            "def:p02-fol-unification-procedure",
            "def:p02-fol-renaming-apart",
            "def:p02-fol-resolution-derivation",
            "def:p02-fol-clause",
            "def:p02-fol-ground-instance",
        ):
            self.assertNotIn(retired, live_labels)
            self.assertNotIn(retired, live_refs)

    def test_first_order_completeness_overlap_labels_and_annex_items_are_not_live(self) -> None:
        historical_body = (
            HANDBOOK / "parts/p02/first-order-completeness.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        historical_annex = (
            HANDBOOK / "annex/p02/first-order-completeness.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        retired = set(
            re.findall(r"\\label\s*\{([^{}]+)\}", "".join(historical_body[:247]))
        )
        retired.update(TYPED_LABEL_RE.findall("".join(historical_body[:247])))
        retired_annex = set(TYPED_LABEL_RE.findall("".join(historical_annex[:256])))
        self.assertEqual(len(retired), 24)
        self.assertEqual(len(retired_annex), 16)

        live_surface = "\n".join(
            (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            for relative in reachable("main")
        )
        live_labels = set(re.findall(r"\\label\s*\{([^{}]+)\}", live_surface))
        live_labels.update(TYPED_LABEL_RE.findall(live_surface))
        live_refs = {
            target.strip()
            for match in REF_RE.finditer(live_surface)
            for target in (match.group(1) or match.group(2)).split(",")
        }
        self.assertEqual(retired & live_labels, set())
        self.assertEqual(retired & live_refs, set())
        self.assertEqual(retired_annex & live_labels, set())

    def test_exact_deduction_source_has_its_complete_rule_surface(self) -> None:
        surface = "".join(
            (HANDBOOK / f"{artifact}.tex").read_text(encoding="utf-8")
            for wrapper in WRAPPERS[5:8]
            for artifact in uncommented_inputs(wrapper)
        )
        self.assertEqual(surface.count(r"\Rule"), 27)
        self.assertEqual(surface.count(r"\side"), 1)
        self.assertEqual(surface.count(r"\begin{array}"), 11)
        self.assertEqual(surface.count(r"\begin{definition}"), 3)
        self.assertEqual(surface.count(r"\begin{example}"), 3)
        self.assertEqual(surface.count(r"\begin{lemma}"), 1)
        self.assertEqual(surface.count(r"\begin{proof}"), 1)
        self.assertEqual(
            re.findall(r"\\cref\{([^{}]+)\}", surface),
            ["ch:intuitionistic-logic"],
        )

    def test_retired_calculus_labels_and_duplicate_proof_are_not_live(self) -> None:
        historical = (
            HANDBOOK / "parts/p02/propositional-calculi.tex"
        ).read_text(encoding="utf-8")
        boundary = historical.index(
            r"\subsection{Hilbert calculus and the deduction theorem}"
        )
        retired = set(re.findall(r"\\label\s*\{([^{}]+)\}", historical[:boundary]))
        retired.update(TYPED_LABEL_RE.findall(historical[:boundary]))
        self.assertEqual(len(retired), 9)

        live_surface = "\n".join(
            (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            for relative in reachable("main")
        )
        live_labels = set(re.findall(r"\\label\s*\{([^{}]+)\}", live_surface))
        live_labels.update(TYPED_LABEL_RE.findall(live_surface))
        live_refs = {
            target.strip()
            for match in REF_RE.finditer(live_surface)
            for target in (match.group(1) or match.group(2)).split(",")
        }
        self.assertEqual(retired & live_labels, set())
        self.assertEqual(retired & live_refs, set())
        self.assertNotIn("annex:p2.calc.1", live_labels)
        self.assertIn("annex:p2.calc.2", live_labels)

    def test_registry_framing_does_not_replace_inherited_rule_displays(self) -> None:
        framing = (HANDBOOK / "parts/p14/rule-sheets.tex").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("from its sole source", framing)
        self.assertNotIn("do not copy rule displays into body chapters", framing)
        self.assertIn("do not replace inherited source rule displays", framing)

        metatheory = (
            HANDBOOK / "parts/p02/propositional-metatheory-supplement.tex"
        ).read_text(encoding="utf-8")
        self.assertNotIn("The active rule sets are the registry sheets", metatheory)
        self.assertIn(r"\cref{sec:prop-metatheory-03}", metatheory)
        self.assertIn(r"\cref{sec:prop-metatheory-04}", metatheory)
        self.assertIn("do not replace exact\ninherited statements", metatheory)

    def test_retired_editorial_labels_are_absent_from_the_live_reader_route(self) -> None:
        historical = (
            HANDBOOK / "parts/p02/propositional-syntax-semantics.tex"
        ).read_text(encoding="utf-8")
        retired = set(re.findall(r"\\label\s*\{([^{}]+)\}", historical))
        retired.update(TYPED_LABEL_RE.findall(historical))
        self.assertEqual(len(retired), 42)

        live_labels: set[str] = set()
        live_refs: set[str] = set()
        for relative in reachable("main"):
            source = (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            live_labels.update(re.findall(r"\\label\s*\{([^{}]+)\}", source))
            live_labels.update(TYPED_LABEL_RE.findall(source))
            for match in REF_RE.finditer(source):
                for target in (match.group(1) or match.group(2)).split(","):
                    live_refs.add(target.strip())
        self.assertEqual(retired & live_labels, set())
        self.assertEqual(retired & live_refs, set())

    def test_unlabelled_source_results_do_not_acquire_editorial_aliases(self) -> None:
        metatheory = (
            HANDBOOK / "parts/p02/propositional-metatheory-supplement.tex"
        ).read_text(encoding="utf-8")
        for retired in (
            "def:p02-propositional-clause",
            "thm:p02-resolution-soundness",
            "def:p02-resolution-refutation",
        ):
            self.assertNotIn(retired, metatheory)

    def test_metatheory_supplement_uses_only_genuine_exact_source_destinations(self) -> None:
        metatheory = (
            HANDBOOK / "parts/p02/propositional-metatheory-supplement.tex"
        ).read_text(encoding="utf-8")
        self.assertIn(r"Theorem~\ref{thm:prop-compactness}", metatheory)
        self.assertIn(r"Lemma~\ref{lem:prop-lindenbaum}", metatheory)
        self.assertNotIn("thm:p02-compactness", metatheory)
        self.assertNotIn("thm:p02-lindenbaum", metatheory)

    def test_exact_metatheory_source_surface_is_complete(self) -> None:
        surface = "".join(
            (HANDBOOK / f"{artifact}.tex").read_text(encoding="utf-8")
            for wrapper in METATHEORY_WRAPPERS
            for artifact in uncommented_inputs(wrapper)
        )
        expected_environments = {
            "theorem": 7,
            "lemma": 3,
            "definition": 3,
            "proof": 10,
            "remark": 1,
            "warning": 1,
            "exercise": 12,
            "enumerate": 4,
        }
        for environment, count in expected_environments.items():
            self.assertEqual(surface.count(rf"\begin{{{environment}}}"), count)
        self.assertEqual(surface.count(r"\begin{proof}[Proof sketch]"), 1)
        self.assertEqual(len(re.findall(r"(?m)^\s*\\item\b", surface)), 19)
        self.assertEqual(surface.count(r"\Rule[Cut]"), 1)
        self.assertEqual(surface.count(r"\index{"), 0)
        self.assertEqual(surface.count(r"\cite{"), 3)
        self.assertEqual(
            re.findall(r"\\cref\{([^{}]+)\}", surface),
            [
                "sec:prop-deduction-02",
                "lem:nd-substitution",
                "lem:prop-mcs",
                "lem:prop-lindenbaum",
                "thm:prop-nd-soundness,thm:prop-completeness",
                "thm:prop-lk-soundness",
                "sec:prop-syntax-semantics-04",
                "thm:prop-resolution-complete",
                "sec:prop-syntax-semantics-04",
                "thm:prop-compactness",
                "thm:prop-resolution-complete",
            ],
        )

    def test_metatheory_historical_files_are_byte_pinned(self) -> None:
        expected = {
            "parts/p02/propositional-metatheory.tex":
                "db4e2b81d8c319e42df4c82768f95d91818488360194ed892e9e8f2640170e62",
            "annex/p02/propositional-metatheory.tex":
                "a958662006df1cf3956731ca63e1c5d9f327eb85596415ec1f7e64efdae1c71e",
        }
        for relative, digest in expected.items():
            self.assertEqual(
                hashlib.sha256((HANDBOOK / relative).read_bytes()).hexdigest(),
                digest,
            )

    def test_metatheory_supplements_are_only_the_audited_historical_ranges(self) -> None:
        historical_body = (
            HANDBOOK / "parts/p02/propositional-metatheory.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        selected_body = "\n\n".join(
            "".join(historical_body[start - 1:end]).rstrip("\n")
            for start, end in (
                (131, 150),
                (164, 199),
                (253, 281),
                (283, 408),
                (421, 427),
            )
        ) + "\n"
        selected_body = selected_body.replace(
            "thm:p02-compactness", "thm:prop-compactness"
        ).replace("thm:p02-lindenbaum", "lem:prop-lindenbaum")
        body_preamble = (
            "%% parts/p02/propositional-metatheory-supplement.tex --- retained editorial additions\n"
            "\\section*{Editorial supplement to the restored chapter}\n"
            "\\addcontentsline{toc}{section}{Editorial supplement to the restored chapter}\n"
            "\\noindent\\textit{Reader note.} The following separately attributed editorial\n"
            "additions are retained after the exact source chapter so that the inherited\n"
            "order and bytes remain intact.  The Boolean Prime Ideal calibration belongs\n"
            "with \\cref{sec:prop-metatheory-03}, and the resolution-refutation DAG belongs\n"
            "with \\cref{sec:prop-metatheory-04}.  These additions do not replace exact\n"
            "inherited statements, supply aliases for unlabeled source results, or change\n"
            "any source or review status.\n\n"
        )
        self.assertEqual(
            (
                HANDBOOK / "parts/p02/propositional-metatheory-supplement.tex"
            ).read_text(encoding="utf-8"),
            body_preamble + selected_body,
        )

        historical_annex = (
            HANDBOOK / "annex/p02/propositional-metatheory.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        selected_annex = "\n\n".join(
            "".join(historical_annex[start - 1:end]).rstrip("\n")
            for start, end in ((137, 156), (193, 201))
        ) + "\n"
        annex_preamble = (
            "%% annex/p02/propositional-metatheory-supplement.tex --- retained editorial proofs\n"
            "\\noindent\\textit{Reader note.} These two proofs support only the separately\n"
            "attributed interpolation and dual-Horn additions retained after the exact\n"
            "source chapter.  The exact inherited proofs remain inline in their governed\n"
            "source scopes; this supplement neither duplicates nor replaces them.\n\n"
        )
        self.assertEqual(
            (
                HANDBOOK / "annex/p02/propositional-metatheory-supplement.tex"
            ).read_text(encoding="utf-8"),
            annex_preamble + selected_annex,
        )

    def test_metatheory_split_does_not_restore_retired_named_methods(self) -> None:
        supplement = (
            HANDBOOK / "parts/p02/propositional-metatheory-supplement.tex"
        ).read_text(encoding="utf-8")
        self.assertNotIn("Maximal-countervaluation method", supplement)
        self.assertNotIn("Davis--Putnam elimination", supplement)
        self.assertNotIn("def:p02-maximal-countervaluation", supplement)
        self.assertNotIn("def:p02-davis-putnam", supplement)

        annex = (
            HANDBOOK / "annex/p02/propositional-metatheory-supplement.tex"
        ).read_text(encoding="utf-8")
        self.assertEqual(annex.count(r"\begin{annexitem}"), 2)
        self.assertIn("annex:p2.3.9", annex)
        self.assertIn("annex:p2.3.12", annex)

    def test_exact_metatheory_consumers_use_genuine_source_destinations(self) -> None:
        expected_by_file = {
            "annex/p02/first-order-calculi.tex": (
                "thm:prop-nd-soundness",
                "thm:prop-lk-soundness",
            ),
            "parts/p06/cardinals-choice.tex": ("thm:prop-compactness",),
            "parts/p07/calculi-and-derivability.tex": (
                "thm:prop-lk-completeness",
                "thm:prop-lk-soundness",
            ),
            "parts/p02/propositional-hilbert-tableaux.tex": (
                "sec:prop-metatheory-04",
                "thm:prop-resolution-complete",
                "rem:resolution-finiteness",
            ),
        }
        for relative, labels in expected_by_file.items():
            body = (HANDBOOK / relative).read_text(encoding="utf-8")
            for label in labels:
                self.assertIn(label, body, relative)

        live = "\n".join(
            (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            for relative in reachable("main")
        )
        for retired in (
            "thm:p02-nd-soundness",
            "thm:p02-lk-soundness",
            "thm:p02-nd-completeness",
            "thm:p02-lk-completeness",
            "thm:p02-compactness",
            "thm:p02-resolution-soundness",
            "thm:p02-resolution-completeness",
        ):
            self.assertNotIn(retired, live)

    def test_resolution_registry_is_separate_editorial_lookup(self) -> None:
        sheet = (
            HANDBOOK / "registry/calculi/resolution-cpl.tex"
        ).read_text(encoding="utf-8")
        self.assertIn("Separately identified editorial lookup", sheet)
        self.assertIn("does not replace", sheet)
        self.assertNotIn("EXTRACTED", sheet)
        self.assertNotIn("source substitute", sheet)
        self.assertNotIn("source admission", sheet)


if __name__ == "__main__":
    unittest.main()
