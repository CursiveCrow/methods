#!/usr/bin/env python3
"""Focused regressions for the exact Part IV reader opening."""

from __future__ import annotations

import hashlib
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from tools import check as handbook_check


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
MACHINE_WRAPPERS = [
    "restoration/scope-SRC-07494-07505",
    "restoration/scope-SRC-07506-07677",
    "restoration/scope-SRC-07678-07752",
    "restoration/scope-SRC-07753-07843",
    "restoration/scope-SRC-07844-07850",
]
UNIVERSAL_WRAPPERS = [
    "restoration/scope-SRC-07851-08048",
    "restoration/scope-SRC-08049-08080",
    "restoration/scope-SRC-08081-08143",
    "restoration/scope-SRC-08144-08186",
    "restoration/scope-SRC-08187-08238",
    "restoration/scope-SRC-08239-08247",
]
DECISION_WRAPPERS = [
    "restoration/scope-SRC-08248-08305",
    "restoration/scope-SRC-08306-08438",
    "restoration/scope-SRC-08439-08709",
    "restoration/scope-SRC-08710-08876",
    "restoration/scope-SRC-08877-08897",
    "restoration/scope-SRC-08898-09079",
]
WRAPPERS = MACHINE_WRAPPERS + UNIVERSAL_WRAPPERS + DECISION_WRAPPERS
HISTORICAL = {
    "parts/p04/machines-effective-procedures":
        "745c470a05c7fde4f66670f6c81ae69bf6674e1c40f269a6de5fa169795d959b",
    "annex/p04/machines-effective-procedures":
        "1fa574674deb89dcc7fa9b4976c928298f39921a6aa6117a4ad79edbd91988bd",
    "parts/p04/universal-reductions":
        "46ebae43bd661d65951dd4a5c55960d36d586146ab6c758b21672ed0b6c84c0c",
    "annex/p04/universal-reductions":
        "c9b4dbe85da7ac62efc36def8cdce445ac5a20a8c10d1cbd492e78f0f4621880",
    "parts/p04/decision-problems-and-arithmetical-hierarchy":
        "7e7a5082c59955a9b539173fdaf105197aaef9eedbeb9f4bcceeea250df7eb4e",
    "annex/p04/decision-problems-and-arithmetical-hierarchy":
        "e897b6d4357d7d421a886fc5274d90a6c6801d8ef3b8a67e93dc40bf9b5e968f",
    "parts/p04/degrees-and-priority":
        "cc4d58a3fcac3cf80232c40612ba0b408ec962a7cd112444b210b92fcc8cca82",
    "annex/p04/degrees-and-priority":
        "4f314dcfacd1b097a88b63f1207382b4f3bb69e18b32b4a7dd949267304b16e5",
}
RETIRED_LABELS = {
    "sec:p04-machines-effective-procedures",
    "sec:p04-machines",
    "def:p04-turing-machine",
    "def:p04-configuration-computation",
    "def:p04-numerical-coding",
    "def:p04-numerical-output",
    "def:p04-partial-computable",
    "def:p04-coding-procedures",
    "def:p04-unary-successor",
    "def:p04-formalism-complexity",
    "sec:p04-primitive-recursion",
    "def:p04-primitive-recursive-function",
    "def:p04-primitive-recursive-relation",
    "thm:p04-pr-functions-computable",
    "def:p04-addition-multiplication-pr",
    "sec:p04-decidable-ce",
    "def:p04-decidable-ce-set",
    "def:p04-decidable-ce-relation",
    "def:p04-machine-decision-recognition",
    "thm:p04-machine-decidability",
    "thm:p04-ce-equivalences",
    "thm:p04-ce-complement",
    *(f"annex:p04-machines.{number}" for number in range(1, 5)),
}
OPEN_SUPPLEMENT_LABELS = {
    "sec:p04-partial-recursion",
    "def:p04-kleene-equality",
    "def:p04-partial-recursive",
    "thm:p04-kleene-normal-form",
    "thm:p04-tm-partial-recursive",
    "def:p04-shepherdson-sturgis-urm",
    "tab:p04-machine-equivalences",
    "def:p04-church-turing",
}
RETIRED_UNIVERSAL_LABELS = {
    "sec:p04-universal-reductions",
    "sec:p04-effective-numbering",
    "sec:p04-many-one",
    "sec:p04-self-application",
    "sec:p04-recursion-theorem",
    "sec:p04-rice",
    "def:p04-program-numbering",
    "thm:p04-renaming-invariance",
    "thm:p04-enumeration",
    "thm:p04-universal-computation",
    "thm:p04-parameter",
    "def:p04-many-one-reduction",
    "thm:p04-reduction-preservation",
    "def:p04-reduction-direction",
    "def:p04-self-application-domain",
    "thm:p04-halting-undecidable",
    "thm:p04-k-complement",
    "def:p04-binary-application-domain",
    "thm:p04-binary-application-equivalence",
    "thm:p04-recursion-theorem",
    "def:p04-self-reference-without-inspection",
    "def:p04-extensional-index-property",
    "thm:p04-rice",
    "def:p04-rice-scope",
    *(f"annex:p04-universal.{number}" for number in (*range(1, 9), 10)),
}
RETIRED_DECISION_LABELS = {
    "sec:p04-decision-hierarchy",
    "sec:p04-logical-decision-problems",
    "sec:p04-arithmetic-hierarchy-syntax",
    "sec:p04-bounded-coding",
    "sec:p04-computation-histories",
    "fig:p04-arithmetical-hierarchy",
    "thm:p04-fol-validity-undecidable",
    "thm:p04-fol-validity-ce",
    "def:p04-restricted-signatures",
    "thm:p04-trakhtenbrot",
    "def:p04-language-arithmetic",
    "def:p04-bounded-quantifiers",
    "def:p04-syntactic-hierarchy",
    "def:p04-definability-classes",
    "def:p04-convergence-notation",
    "thm:p04-pairing-graph",
    "thm:p04-goedel-beta",
    "thm:p04-pairing-contraction",
    "thm:p04-bounded-exchange",
    "def:p04-prefix-form",
    "thm:p04-prefix-normal-form",
    "def:p04-history-code",
    "thm:p04-bounded-verification",
    "thm:p04-ce-sigma-one",
    "def:p04-many-one-completeness",
    "thm:p04-domain-totality-completeness",
    "thm:p04-arithmetical-strictness",
    "def:p04-syntax-versus-class",
    "sec:p04-degrees-priority",
    "sec:p04-oracles-jump",
    "def:p04-oracle-reducibility",
    "def:p04-turing-jump",
    "thm:p04-relativized-adequacy",
    "thm:p04-jump",
    "thm:p04-post",
    "thm:p04-jump-convention-bridge",
    *(f"annex:p04-hierarchy.{number}" for number in range(1, 9)),
    *(f"annex:p4.degrees.{number}" for number in range(1, 4)),
}


def uncommented(relative: str) -> str:
    text = (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
    return re.sub(r"(?m)(?<!\\)%.*$", "", text)


def inputs(relative: str) -> list[str]:
    return re.findall(r"\\input\s*\{([^{}]+)\}", uncommented(relative))


def reachable(start: str) -> set[str]:
    reached: set[str] = set()

    def visit(relative: str) -> None:
        if relative in reached:
            return
        reached.add(relative)
        for child in inputs(relative):
            visit(child.removesuffix(".tex"))

    visit(start)
    return reached


def declared_labels(text: str) -> list[str]:
    return re.findall(
        r"\\label\{([^{}]+)\}|"
        r"\\begin\{(?:hbconvention|hbdefinition|hbtheorem|proofboundary)\}"
        r"\{([^{}]+)\}",
        text,
    )


def declaration_count(text: str, label: str) -> int:
    return sum(label in pair for pair in declared_labels(text))


class Part4ReaderRouteTests(unittest.TestCase):
    def test_exact_source_chapter_replaces_the_overlapping_machine_draft(self) -> None:
        self.assertEqual(
            inputs("parts/p04"),
            WRAPPERS
            + [
                "parts/p04/machines-effective-procedures-supplement",
                "parts/p04/universal-reductions-supplement",
                "parts/p04/decision-hierarchy-apparatus-supplement",
                "parts/p04/degrees-and-priority-continuation",
                "parts/p04/frontiers-of-computability",
                "parts/p04/complexity",
            ],
        )
        driver = uncommented("parts/p04")
        self.assertEqual(
            driver.count(r"\part{Computability and Complexity}\label{part:p04}"),
            1,
        )
        artifact = (
            HANDBOOK / "restoration/inherited-07494-07505.tex"
        ).read_text(encoding="utf-8")
        self.assertEqual(artifact.count(r"\part{Computability}"), 1)
        self.assertEqual(artifact.count(r"\label{part:computability}"), 1)

    def test_historical_overlap_is_byte_retained_and_unreachable(self) -> None:
        live = reachable("parts/p04") | reachable("annex/p04")
        for relative, expected_hash in HISTORICAL.items():
            path = HANDBOOK / f"{relative}.tex"
            self.assertTrue(path.is_file())
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected_hash)
            self.assertNotIn(relative, live)
            self.assertEqual(
                handbook_check.HB_RETAINED_UNREACHABLE_READER_FILES.get(
                    f"{relative}.tex"
                ),
                expected_hash,
            )
        body_lines = (
            HANDBOOK / "parts/p04/machines-effective-procedures.tex"
        ).read_text(encoding="utf-8").splitlines(keepends=True)
        exact_slice = "".join(body_lines[220:400]).encode("utf-8")
        self.assertEqual(len(exact_slice), 9443)
        self.assertEqual(
            hashlib.sha256(exact_slice).hexdigest(),
            "a7d57e02c98038974ed07efa6c74812ec2dab7dd42e02f8d4f0cb4113854437c",
        )

    def test_part4_scope_alone_activates_fail_closed_history_hashing(self) -> None:
        with tempfile.TemporaryDirectory(prefix="p04-history-activation-") as raw:
            base = Path(raw)
            for relative in handbook_check.HB_RETAINED_UNREACHABLE_READER_FILES:
                target = base / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(HANDBOOK / relative, target)
            wrapper_relative = "restoration/scope-SRC-07494-07505.tex"
            wrapper = base / wrapper_relative
            wrapper.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(HANDBOOK / wrapper_relative, wrapper)
            (base / "main.tex").write_text(
                r"\input{parts/p04}" + "\n", encoding="utf-8", newline="\n"
            )
            (base / "parts/p04.tex").write_text(
                rf"\input{{{wrapper_relative.removesuffix('.tex')}}}" + "\n",
                encoding="utf-8",
                newline="\n",
            )
            historical = base / "parts/p04/machines-effective-procedures.tex"
            historical.write_bytes(historical.read_bytes() + b"% mutation\n")
            bodies = {
                path.relative_to(base).as_posix(): path.read_text(
                    encoding="utf-8", errors="replace"
                )
                for path in base.rglob("*.tex")
            }
            data = handbook_check._HBData()
            verified = handbook_check._hb_retained_unreachable_reader_files(
                base, bodies, data
            )
        self.assertNotIn("parts/p04/machines-effective-procedures.tex", verified)
        self.assertTrue(
            any(
                "parts/p04/machines-effective-procedures.tex" in finding
                and "bytes changed" in finding
                for finding in data.findings.get("duplicate-label", [])
            )
        )

    def test_open_machine_supplement_is_exactly_bounded_and_consumer_corrected(self) -> None:
        supplement = (
            HANDBOOK / "parts/p04/machines-effective-procedures-supplement.tex"
        ).read_text(encoding="utf-8")
        prose = " ".join(supplement.replace("%", "").split())
        self.assertIn("OPEN", prose)
        self.assertIn("unadmitted", prose)
        match = re.search(
            r"(?ms)^%% BEGIN CONSUMER-CORRECTED P4 MACHINES BODY SLICE 221-400\n"
            r"(.*?)"
            r"^%% END CONSUMER-CORRECTED P4 MACHINES BODY SLICE 221-400\n",
            supplement,
        )
        self.assertIsNotNone(match)
        block = match.group(1)
        block_bytes = block.encode("utf-8")
        self.assertEqual(len(block_bytes), 9615)
        self.assertEqual(block.count("\n"), 183)
        self.assertEqual(
            hashlib.sha256(block_bytes).hexdigest(),
            "2b716093668ecd2ed5a860367d2949956fc9107ec9dcb135d48642791bc7e939",
        )
        for label in OPEN_SUPPLEMENT_LABELS:
            self.assertEqual(declaration_count(block, label), 1)
        self.assertIn(r"Section~\ref{sec:turing-machines-01}", block)
        self.assertIn(r"Section~\ref{sec:turing-machines-02}", block)
        self.assertNotIn("def:p04-turing-machine", block)
        self.assertNotIn("def:p04-primitive-recursive-function", block)
        self.assertNotIn("def:p04-formalism-complexity", block)

    def test_reachable_part4_has_no_retired_overlap_aliases(self) -> None:
        live = reachable("parts/p04") | reachable("annex/p04")
        text = "\n".join(uncommented(relative) for relative in sorted(live))
        for retired in sorted(RETIRED_LABELS):
            self.assertNotIn(retired, text)
        for label in sorted(OPEN_SUPPLEMENT_LABELS):
            self.assertEqual(declaration_count(text, label), 1)
        self.assertNotIn("part:p04-computability", text)

    def test_only_genuine_source_consumer_replacements_are_live(self) -> None:
        consumers = {
            "annex/p04/universal-reductions-supplement": r"thm:enumeration",
            "parts/p04/frontiers-of-computability": r"def:partial-computable",
            "parts/p05/diagonalization": r"sec:turing-machines-01",
            "parts/p04/degrees-and-priority-continuation": r"thm:universal-computation",
            "annex/p04/degrees-and-priority-continuation": r"def:turing-jump",
        }
        for relative, expected in consumers.items():
            text = (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            self.assertIn(expected, text)
        combined = "\n".join(
            (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            for relative in consumers
        )
        self.assertNotIn("def:p04-partial-computable", combined)
        self.assertNotIn("def:p04-numerical-coding", combined)

    def test_exact_universal_chapter_retires_old_core_without_aliases(self) -> None:
        live = reachable("parts/p04") | reachable("annex/p04")
        text = "\n".join(uncommented(relative) for relative in sorted(live))
        for retired in sorted(RETIRED_UNIVERSAL_LABELS):
            self.assertNotRegex(
                text,
                rf"{re.escape(retired)}(?![-A-Za-z0-9])",
            )

        supplement = uncommented("parts/p04/universal-reductions-supplement")
        self.assertIn("OPEN", supplement)
        self.assertIn("unadmitted", supplement)
        self.assertEqual(
            supplement.count("thm:p04-numbering-partial-recursive"), 1
        )
        self.assertIn("sec:universal-reductions-01", supplement)
        self.assertIn("def:p04-partial-recursive", supplement)
        self.assertNotIn("def:p04-program-numbering", supplement)
        self.assertNotIn("thm:p04-enumeration", supplement)

        annex = uncommented("annex/p04/universal-reductions-supplement")
        self.assertEqual(annex.count("annex:p04-universal.9"), 1)
        self.assertIn("thm:p04-numbering-partial-recursive", annex)
        self.assertIn("thm:enumeration", annex)
        self.assertNotIn("thm:p04-enumeration", annex)

    def test_exact_decision_chapter_retires_overlap_and_bounds_open_continuations(self) -> None:
        live = reachable("parts/p04") | reachable("annex/p04")
        text = "\n".join(uncommented(relative) for relative in sorted(live))
        for retired in sorted(RETIRED_DECISION_LABELS):
            self.assertNotRegex(
                text,
                rf"{re.escape(retired)}(?![-A-Za-z0-9])",
            )

        derivatives = {
            "parts/p04/decision-hierarchy-apparatus-supplement":
                "b16e51e7ec1f03f8711962cb9a74a280c4f53944c7d8393935e7e406fef2a337",
            "parts/p04/degrees-and-priority-continuation":
                "ac6fea5501c5a2c000371e1661aeef1f16bb155f404f1d659e646363003e980d",
            "annex/p04/degrees-and-priority-continuation":
                "e1a555d7fb2c4de4669d96d338811b58f02d1e2f27626a8b62c180766d7a6449",
        }
        for relative, expected_hash in derivatives.items():
            path = HANDBOOK / f"{relative}.tex"
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected_hash)
            prose = " ".join(uncommented(relative).split())
            self.assertIn("OPEN", prose)
            self.assertIn("unadmitted", prose)

        apparatus = uncommented(
            "parts/p04/decision-hierarchy-apparatus-supplement"
        )
        self.assertEqual(apparatus.count("tab:p04-arithmetical-hierarchy"), 1)
        self.assertIn("thm:prefix-normal-form", apparatus)
        self.assertIn("sec:decision-hierarchy-02", apparatus)
        self.assertIn("sec:decision-hierarchy-03", apparatus)
        self.assertNotIn("thm:p04-prefix-normal-form", apparatus)

        continuation = uncommented("parts/p04/degrees-and-priority-continuation")
        for label in (
            "sec:p04-turing-degrees",
            "sec:p04-finite-injury",
            "sec:p04-ce-structure",
            "fig:p04-turing-degrees",
        ):
            self.assertIn(label, continuation)
        self.assertIn("thm:jump", continuation)
        self.assertIn("rem:jump-convention", continuation)
        self.assertNotIn("thm:p04-jump", continuation)

        annex = uncommented("annex/p04/degrees-and-priority-continuation")
        self.assertIn("annex:p4.degrees.4", annex)
        self.assertNotIn("annex:p4.degrees.5", annex)
        self.assertIn("def:turing-jump", annex)
        self.assertNotIn("def:p04-turing-jump", annex)

    def test_machine_annex_and_generated_audit_are_explicitly_unrouted(self) -> None:
        self.assertEqual(
            inputs("annex/p04"),
            [
                "annex/p04/universal-reductions-supplement",
                "annex/p04/degrees-and-priority-continuation",
            ],
        )
        driver = (HANDBOOK / "parts/p04.tex").read_text(encoding="utf-8")
        self.assertNotIn("generated/audit-p04", inputs("parts/p04"))
        self.assertIn("OPEN: generated/audit-p04", driver)
        self.assertIn("unreachable historical P4 files", driver)
        self.assertIn("reachability- and admission-backed generator", driver)
        self.assertTrue((HANDBOOK / "generated/audit-p04.tex").is_file())


if __name__ == "__main__":
    unittest.main()
