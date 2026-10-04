#!/usr/bin/env python3
"""Focused regressions for the exact Part III reader opening."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
import unittest
from pathlib import Path

from tools import check as handbook_check


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
WRAPPERS = [
    "restoration/scope-SRC-06049-06069",
    "restoration/scope-SRC-06070-06137",
    "restoration/scope-SRC-06138-06242",
    "restoration/scope-SRC-06243-06331",
    "restoration/scope-SRC-06332-06421",
    "restoration/scope-SRC-06422-06431",
    "restoration/scope-SRC-06432-06493",
    "restoration/scope-SRC-06494-06509",
    "restoration/scope-SRC-06510-06629",
    "restoration/scope-SRC-06630-06639",
    "restoration/scope-SRC-06640-06693",
    "restoration/scope-SRC-06694-06782",
    "restoration/scope-SRC-06783-06791",
    "restoration/scope-SRC-06792-06845",
    "restoration/scope-SRC-06846-06854",
    "restoration/scope-SRC-06855-06941",
    "restoration/scope-SRC-06942-07134",
    "restoration/scope-SRC-07135-07149",
    "restoration/scope-SRC-07150-07294",
    "restoration/scope-SRC-07295-07468",
    "restoration/scope-SRC-07469-07493",
]
HISTORICAL = {
    "parts/p03/maps-elementarity":
        "2c3b31b2905b6ba4c11ecdea119edce02960e8fa3e85525cbe2d6b93a069c7ac",
    "annex/p03/maps-elementarity":
        "81a912fb519d811c1a517b764e4e716b6687e16c2e1986218e6b6b7f6ebd67b4",
    "parts/p03/types-ultraproducts":
        "fd8eb5788fd460ef6555df01692597c9649badabbb17f366d43ef1575e263ecf",
    "annex/p03/types-ultraproducts":
        "7363e0df7e9afdccdb557de9c1eed7702c854083aba6b21b5c90f5c17523d385",
    "parts/p03/qe-categoricity-games":
        "59b274b3d0f0f40f9d9f7c138d173044150082d222a30829587702caee2cd551",
    "annex/p03/qe-categoricity-games":
        "89a7bac0248d521eba8c8c321ed79c1dc587b40f1d50bd1b628342f7a8a5392d",
}

QE_BODY_BLOCK_HASHES = (
    "2649b7fcc28a90fee1e7bb908ce7c30865ab8418f433b0898e06641f82134520",
    "9728d1eda11996bf1ed4cf584fad0b7aff50e380617868c153fa3830058dd24f",
    "8be03b0fb51bd99c017662332258de5faa95c9374748f10af78ef8463a79fcfe",
)
QE_ANNEX_BLOCK_HASH = (
    "a61933ee5bc7bd1ccde24bc1e6f3a96d8efc1fecf7e6165454f5f9404bc2644d"
)
RETIRED_QE_LABELS = {
    "sec:p03-qe-categoricity-games",
    "sec:p03-quantifier-elimination",
    "def:p03-quantifier-elimination",
    "def:p03-one-quantifier-reduction",
    "thm:p03-dlo-qe",
    "def:p03-dlo-one-quantifier",
    "def:p03-theory-completeness",
    "thm:p03-model-completeness-reduction",
    "thm:p03-dlo-complete-model-complete",
    "thm:p03-acfp-qe",
    "sec:p03-categoricity-back-and-forth",
    "def:p03-categoricity",
    "def:p03-categoricity-cardinal",
    "def:p03-finite-partial-isomorphism",
    "def:p03-back-and-forth",
    "thm:p03-back-and-forth-test",
    "thm:p03-countable-saturated-automorphism",
    "thm:p03-dlo-countable-categorical",
    "thm:p03-acfp-uncountable-categorical",
    "thm:p03-ryll-nardzewski",
    "thm:p03-morley-categoricity",
    "def:p03-completeness-versus-categoricity",
    *(f"annex:p3.qe.{number}" for number in range(1, 5)),
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


class Part3ReaderRouteTests(unittest.TestCase):
    def test_source_part_executes_directly_once_before_later_part3_chapters(self) -> None:
        self.assertEqual(
            inputs("parts/p03"),
            WRAPPERS[:8]
            + [
                "parts/p03/maps-elementarity-supplement",
            ]
            + WRAPPERS[8:18]
            + [
                "parts/p03/types-ultraproducts-supplement",
            ]
            + WRAPPERS[18:]
            + [
                "parts/p03/qe-categoricity-games-supplement",
                "parts/p03/classification-theory",
                "parts/p03/finite-model-theory",
                "parts/p03/preservation-abstract-logic",
            ],
        )
        driver = uncommented("parts/p03")
        self.assertNotRegex(driver, r"\\part\s*(?:\[[^]]*\])?\s*\{")
        self.assertNotIn("part:p03", driver)

        artifact = (
            HANDBOOK / "restoration/inherited-06049-06069.tex"
        ).read_text(encoding="utf-8")
        self.assertEqual(artifact.count(r"\part{Model Theory}"), 1)
        self.assertEqual(artifact.count(r"\label{part:model-theory}"), 1)

    def test_historical_overlap_is_byte_retained_and_unreachable(self) -> None:
        live = reachable("parts/p03") | reachable("annex/p03")
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

    def test_exact_parameter_expansion_replaces_only_the_reachable_old_label(self) -> None:
        live = (
            reachable("parts/p03")
            | reachable("annex/p03")
            | {"parts/p06/cardinals-choice"}
        )
        text = "\n".join(
            (HANDBOOK / f"{relative}.tex").read_text(encoding="utf-8")
            for relative in sorted(live)
        )
        self.assertNotIn("def:p03-parameter-expansion", text)
        self.assertIn(r"\cref{def:parameter-expansion}", text)
        self.assertNotIn("part:p03", text)
        for retired in (
            "def:p03-principal-type",
            "thm:p03-nonprincipal-ultrafilter",
            "thm:p03-los",
            "thm:p03-saturation-homogeneity",
        ):
            self.assertNotIn(f"{{{retired}}}", text)
        for exact in (
            r"\ref{def:principal-type}",
            r"\ref{lem:nonprincipal-ultrafilter}",
            r"\ref{thm:los}",
            r"\cref{thm:saturation-homogeneity}",
        ):
            self.assertIn(exact, text)

    def test_stale_generated_audit_is_explicitly_open_and_unrouted(self) -> None:
        driver = (HANDBOOK / "parts/p03.tex").read_text(encoding="utf-8")
        self.assertNotIn("generated/audit-p03", inputs("parts/p03"))
        self.assertIn("OPEN: generated/audit-p03", driver)
        self.assertIn("unreachable historical P3 files", driver)
        self.assertIn("reachability- and admission-backed generator", driver)
        self.assertTrue((HANDBOOK / "generated/audit-p03.tex").is_file())

    def test_a162_is_open_and_consumer_corrected_without_aliases(self) -> None:
        supplement = (
            HANDBOOK / "parts/p03/maps-elementarity-supplement.tex"
        ).read_text(encoding="utf-8")
        prose = " ".join(supplement.replace("%", "").split())
        self.assertIn("OPEN", prose)
        self.assertIn("does not admit or close A-162", prose)
        self.assertIn(r"\ref{def:type-space}", supplement)
        self.assertIn(r"\ref{sec:types-ultraproducts-04}", supplement)
        self.assertIn(r"\ref{sec:types-ultraproducts-05}", supplement)
        self.assertNotIn("def:p03-type-space", supplement)
        self.assertNotIn("def:p03-filter", supplement)
        self.assertNotIn("def:p03-ultraproduct", supplement)

    def test_distinct_types_additions_remain_explicitly_open_and_attributed(self) -> None:
        body = (
            HANDBOOK / "parts/p03/types-ultraproducts-supplement.tex"
        ).read_text(encoding="utf-8")
        annex = (
            HANDBOOK / "annex/p03/types-ultraproducts-supplement.tex"
        ).read_text(encoding="utf-8")
        annex_prose = " ".join(annex.replace("%", "").split())
        self.assertIn("D-P4-003", body)
        self.assertIn("D-P4-004", body)
        self.assertIn("remain OPEN", body)
        self.assertIn("cited=Shelah1971Ultrapowers", body)
        self.assertIn("proved=annex:p3.types.8", body)
        self.assertIn("annex:p3.types.8", annex)
        self.assertIn("does not admit or close D-P4-004", annex_prose)
        self.assertNotIn(r"\chapter{Types, Saturation, and Ultraproducts}", body)

    def test_qe_additions_are_exactly_bounded_open_derivatives(self) -> None:
        body_path = HANDBOOK / "parts/p03/qe-categoricity-games-supplement.tex"
        body = body_path.read_text(encoding="utf-8")
        self.assertIn("OPEN", body)
        self.assertIn("unadmitted", body)
        self.assertNotIn(r"\chapter{Quantifier Elimination", body)
        marked_blocks = re.findall(
            r"(?ms)^%% BEGIN AUDITED QE BODY SLICE (\d+)-(\d+)\n(.*?)"
            r"^%% END AUDITED QE BODY SLICE (\d+)-(\d+)\n",
            body,
        )
        self.assertEqual(len(marked_blocks), 3)
        self.assertEqual(
            [
                (int(start), int(end), int(closing_start), int(closing_end))
                for start, end, _, closing_start, closing_end in marked_blocks
            ],
            [(104, 212, 104, 212), (326, 329, 326, 329), (331, 451, 331, 451)],
        )
        blocks = [block for _, _, block, _, _ in marked_blocks]
        self.assertEqual(
            tuple(hashlib.sha256(block.encode("utf-8")).hexdigest() for block in blocks),
            QE_BODY_BLOCK_HASHES,
        )
        self.assertNotIn("thm:p03-acfp-uncountable-categorical", body)
        self.assertNotIn("thm:p03-ryll-nardzewski", body)
        self.assertNotIn("the unique countable model is prime", body)

        annex_path = HANDBOOK / "annex/p03/qe-categoricity-games-supplement.tex"
        annex = annex_path.read_text(encoding="utf-8")
        annex_prose = " ".join(annex.replace("%", "").split())
        self.assertIn("OPEN", annex_prose)
        self.assertIn("R-030", annex_prose)
        match = re.search(
            r"(?ms)^%% BEGIN CONSUMER-CORRECTED QE ANNEX SLICE 45-53\n(.*?)"
            r"^%% END CONSUMER-CORRECTED QE ANNEX SLICE 45-53\n",
            annex,
        )
        self.assertIsNotNone(match)
        self.assertEqual(
            hashlib.sha256(match.group(1).encode("utf-8")).hexdigest(),
            QE_ANNEX_BLOCK_HASH,
        )
        self.assertIn(r"{thm:dlo-countable-categorical}", match.group(1))
        self.assertIn(r"\ref{thm:back-and-forth-test}", match.group(1))
        self.assertNotIn("thm:p03-dlo-countable-categorical", match.group(1))
        self.assertNotIn("thm:p03-back-and-forth-test", match.group(1))

    def test_qe_replacement_has_no_retired_alias_consumers(self) -> None:
        live = reachable("parts/p03") | reachable("annex/p03")
        text = "\n".join(uncommented(relative) for relative in sorted(live))
        for retired in sorted(RETIRED_QE_LABELS):
            self.assertNotIn(retired, text)
        self.assertIn("annex:p3.qe.5", text)
        self.assertIn("ex:back-and-forth-equivalence", text)
        classification = (
            HANDBOOK / "parts/p03/classification-theory.tex"
        ).read_text(encoding="utf-8")
        self.assertIn(r"Section~\ref{sec:qe-categoricity-02}", classification)

    def test_open_qe_annex_points_to_a_genuine_source_result_without_promotion(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools/check.py"),
                "--tree",
                "handbook",
                "--strict",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=120,
        )
        output = completed.stdout + completed.stderr
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("proved=annex:p3.qe.5", output)
        self.assertIn("pending inherited references: 1", output)

    def test_only_nonoverlapping_annex_supplements_are_routed(self) -> None:
        self.assertEqual(
            inputs("annex/p03"),
            [
                "annex/p03/types-ultraproducts-supplement",
                "annex/p03/qe-categoricity-games-supplement",
            ],
        )


if __name__ == "__main__":
    unittest.main()
