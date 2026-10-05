#!/usr/bin/env python3
"""Regression tests for the provenance-gated inherited TeX scope."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools" / "check.py"
HANDBOOK_TEX = ROOT / "handbook"
PDFLATEX = shutil.which("pdflatex")
PROVENANCE_ID = "SRC-00406-00443"
ARTIFACT = "restoration/inherited-00406-00443.tex"


class RestorationScopeStaticTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for relative in (
            "source/formal-logic-reference.tex",
            "spec/inherited-corpus-manifest.json",
            "spec/inherited-source-map.csv",
            "spec/source-unit-inventory.csv",
        ):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, target)
        (self.root / "handbook" / "restoration").mkdir(parents=True)
        (self.root / "handbook" / "registry").mkdir(parents=True)
        (self.root / "handbook" / "bib").mkdir(parents=True)
        (self.root / "spec" / "provenance").mkdir(parents=True)
        (self.root / "handbook" / "registry" / "symbols.csv").write_text(
            "glyph,macro,role,scope,precedence,first_use,notes\n",
            encoding="utf-8",
            newline="\n",
        )
        (self.root / "handbook" / "bib" / "handbook.bib").write_text(
            "", encoding="utf-8", newline="\n"
        )
        self._make_exact_proof_record()
        self.write_wrapper()
        (self.root / "handbook" / "main.tex").write_text(
            rf"\input{{restoration/scope-{PROVENANCE_ID}}}" + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def _make_exact_proof_record(self) -> None:
        source = (
            self.root / "source" / "formal-logic-reference.tex"
        ).read_bytes().splitlines(keepends=True)
        source_interval = source[405:443]
        artifact = b"".join(
            line.rstrip(b"\r\n") + b"\n" for line in source_interval
        )
        artifact_path = self.root / "handbook" / ARTIFACT
        artifact_path.write_bytes(artifact)

        template = json.loads(
            (ROOT / "spec" / "provenance" / "SRC-09099-09111.json").read_text(
                encoding="utf-8"
            )
        )
        template["provenance_id"] = PROVENANCE_ID
        template["source_locator"] = {
            "start_line": 406,
            "end_line": 443,
            "line_count": 38,
            "interval_sha256": hashlib.sha256(
                b"".join(source_interval)
            ).hexdigest(),
        }
        with (self.root / "spec" / "source-unit-inventory.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            units = list(csv.DictReader(handle))
        template["source_unit_evidence"]["unit_ordinals"] = [
            int(row["ordinal"])
            for row in units
            if int(row["start_line"]) <= 443 and int(row["end_line"]) >= 406
        ]
        template["presentation_identity"] = {
            "kind": "section with definitions, lemma, and proof",
            "source_title": "Ordered pairs and products",
            "description": "Exact inclusive source interval 406--443.",
        }
        template["restoration_artifact"].update(
            {
                "path": f"handbook/{ARTIFACT}",
                "bytes": len(artifact),
                "physical_lines": 38,
                "sha256": hashlib.sha256(artifact).hexdigest(),
                "content_token_sha256": hashlib.sha256(artifact).hexdigest(),
            }
        )
        template["handbook_destination"] = {
            "status": "open/missing",
            "file": "",
            "stable_label": "",
            "reason": "The exact fixture remains a bounded restoration artifact.",
        }
        with (self.root / "spec" / "inherited-source-map.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            source_map = {
                row["stable_id"]: row for row in csv.DictReader(handle)
            }
        row = source_map[PROVENANCE_ID]
        template["audit_evidence"] = {
            "source_map": "spec/inherited-source-map.csv",
            "interval_ids": [PROVENANCE_ID],
            "classifications": [
                value.strip()
                for value in row["class_normalized"].split(";")
                if value.strip()
            ],
        }
        record_path = self.root / "spec" / "provenance" / f"{PROVENANCE_ID}.json"
        record_path.write_text(
            json.dumps(template, indent=2) + "\n", encoding="utf-8", newline="\n"
        )

    @property
    def wrapper(self) -> Path:
        return (
            self.root / "handbook" / "restoration" / f"scope-{PROVENANCE_ID}.tex"
        )

    def write_wrapper(self, body: str | None = None) -> None:
        if body is None:
            body = (
                rf"\begin{{inheritedrestorationscope}}{{{PROVENANCE_ID}}}" + "\n"
                + rf"\input{{{ARTIFACT.removesuffix('.tex')}}}" + "\n"
                + r"\end{inheritedrestorationscope}" + "\n"
            )
        self.wrapper.write_text(body, encoding="utf-8", newline="\n")

    def run_check(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(CHECK),
                "--tree",
                "handbook",
                "--strict",
                "--root",
                str(self.root),
            ],
            text=True,
            capture_output=True,
            timeout=60,
        )

    def assert_fails_with(self, *needles: str) -> None:
        result = self.run_check()
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        for needle in needles:
            self.assertIn(needle, output)

    def test_exact_recorded_proof_inside_wrapper_passes(self) -> None:
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_spoofed_scope_under_parts_fails(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "spoof.tex"
        part.parent.mkdir(parents=True)
        part.write_text(self.wrapper.read_text(encoding="utf-8"), encoding="utf-8")
        self.assert_fails_with(
            "may occur only under handbook/restoration",
            "included outside its validated scope wrapper",
        )

    def test_missing_record_fails_closed(self) -> None:
        missing_id = "SRC-00407-00443"
        missing = self.wrapper.with_name(f"scope-{missing_id}.tex")
        self.wrapper.unlink()
        missing.write_text(
            rf"\begin{{inheritedrestorationscope}}{{{missing_id}}}" + "\n"
            + rf"\input{{{ARTIFACT.removesuffix('.tex')}}}" + "\n"
            + r"\end{inheritedrestorationscope}" + "\n",
            encoding="utf-8",
        )
        (self.root / "handbook" / "main.tex").write_text(
            rf"\input{{restoration/scope-{missing_id}}}" + "\n",
            encoding="utf-8",
        )
        self.assert_fails_with("record/artifact is missing or stale")

    def test_stale_artifact_fails_closed(self) -> None:
        artifact = self.root / "handbook" / ARTIFACT
        artifact.write_bytes(artifact.read_bytes().replace(b"Ordered pair", b"Altered pair", 1))
        self.assert_fails_with("record/artifact is missing or stale")

    def test_unbalanced_scope_fails(self) -> None:
        self.write_wrapper(
            rf"\begin{{inheritedrestorationscope}}{{{PROVENANCE_ID}}}" + "\n"
            + rf"\input{{{ARTIFACT.removesuffix('.tex')}}}" + "\n"
        )
        self.assert_fails_with("unbalanced restoration scope begin")

    def test_nested_scope_fails(self) -> None:
        self.write_wrapper(
            rf"\begin{{inheritedrestorationscope}}{{{PROVENANCE_ID}}}" + "\n"
            + rf"\begin{{inheritedrestorationscope}}{{{PROVENANCE_ID}}}" + "\n"
            + rf"\input{{{ARTIFACT.removesuffix('.tex')}}}" + "\n"
            + r"\end{inheritedrestorationscope}" + "\n"
            + r"\end{inheritedrestorationscope}" + "\n"
        )
        self.assert_fails_with("nested restoration scope")

    def test_scope_body_cannot_smuggle_editorial_proof(self) -> None:
        self.write_wrapper(
            rf"\begin{{inheritedrestorationscope}}{{{PROVENANCE_ID}}}" + "\n"
            + rf"\input{{{ARTIFACT.removesuffix('.tex')}}}" + "\n"
            + r"\begin{proof}Editorial addition.\end{proof}" + "\n"
            + r"\end{inheritedrestorationscope}" + "\n"
        )
        self.assert_fails_with("must be exactly one braced artifact input")

    def test_direct_recorded_artifact_input_fails(self) -> None:
        self.wrapper.unlink()
        (self.root / "handbook" / "main.tex").write_text(
            rf"\input{{{ARTIFACT.removesuffix('.tex')}}}" + "\n",
            encoding="utf-8",
        )
        self.assert_fails_with("included outside its validated scope wrapper")

    def test_unreachable_validated_wrapper_fails(self) -> None:
        (self.root / "handbook" / "main.tex").write_text(
            "% The valid wrapper exists but is not integrated.\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "validated scope wrapper is not reachable exactly once from main.tex"
        )

    def test_editorial_part_proof_and_rule_remain_hard_failures(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True)
        part.write_text(
            r"\begin{proof}Editorial proof.\end{proof}" + "\n"
            + r"\Rule{\Gamma\vdash A}{\Gamma\vdash A}" + "\n",
            encoding="utf-8",
        )
        self.assert_fails_with("body-proof", "rule-outside-registry")

    def test_unrecorded_nonproof_nonrule_fragment_fails_closed(self) -> None:
        artifact = self.root / "handbook" / "restoration" / "inherited-00035-00037.tex"
        shutil.copy2(ROOT / "handbook" / "restoration" / artifact.name, artifact)
        with (self.root / "handbook" / "main.tex").open("a", encoding="utf-8") as handle:
            handle.write(r"\input{restoration/inherited-00035-00037}" + "\n")
        self.assert_fails_with("unrecorded restoration artifact")

    def test_unrecorded_proof_fragment_cannot_use_direct_path(self) -> None:
        artifact = self.root / "handbook" / "restoration" / "inherited-09998-09999.tex"
        artifact.write_text(
            r"\begin{proof}Unrecorded.\end{proof}" + "\n\n",
            encoding="utf-8",
            newline="\n",
        )
        with (self.root / "handbook" / "main.tex").open("a", encoding="utf-8") as handle:
            handle.write(r"\input{restoration/inherited-09998-09999}" + "\n")
        self.assert_fails_with("unrecorded restoration artifact", "unscoped inherited proof")

    def test_source_definition_environment_outside_scope_fails(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"\begin{definition}Editorial.\end{definition}" + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source environment definition outside a validated restoration scope"
        )

    def test_source_warning_environment_outside_scope_fails(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"\begin { warning }Editorial.\end{warning}" + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source environment warning outside a validated restoration scope"
        )

    def test_source_listing_environment_outside_scope_fails(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            "\\begin{lstlisting}\neditorial code\n\\end{lstlisting}\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source environment lstlisting outside a validated restoration scope"
        )

    def test_source_convention_environment_outside_scope_fails(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"\begin{convention}[Editorial]Not source.\end{convention}" + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source environment convention outside a validated restoration scope"
        )

    def test_source_solution_environment_outside_scope_fails(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"\begin{solution}Editorial answer.\end{solution}" + "\n",
            encoding="utf-8",
        )
        with (self.root / "handbook" / "main.tex").open(
            "a", encoding="utf-8"
        ) as handle:
            handle.write(r"\input{parts/p01/editorial}" + "\n")
        self.assert_fails_with(
            "source environment solution outside a validated restoration scope"
        )

    def test_source_commands_outside_scope_fail(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Editorial $\Pow_0(A)=\set_0{x:x\in A}$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source command \\Pow outside a validated restoration scope",
            "source command \\set outside a validated restoration scope",
        )

    def test_automated_reasoning_commands_outside_scope_fail(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Editorial $\SAT,\UNSAT,\NP$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source command \\SAT outside a validated restoration scope",
            "source command \\UNSAT outside a validated restoration scope",
            "source command \\NP outside a validated restoration scope",
        )

    def test_first_chapter_source_syntax_outside_scope_fails(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"\begin{lemma}Editorial lemma.\end{lemma}" + "\n"
            + r"\begin{method}Editorial method.\end{method}" + "\n"
            + r"\begin{theorem}Editorial theorem.\end{theorem}" + "\n"
            + r"\begin{corollary}Editorial corollary.\end{corollary}" + "\n"
            + r"\begin{example}Editorial example.\end{example}" + "\n"
            + r"\begin{exercise}Editorial exercise.\end{exercise}" + "\n"
            + r"Editorial $\tuple{x,y},\rng(f),\Mod(T),\Fm,\length(w),w\restr n,\rank(x),\ZF,\ZFC,\Z$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source environment lemma outside a validated restoration scope",
            "source environment method outside a validated restoration scope",
            "source environment theorem outside a validated restoration scope",
            "source environment corollary outside a validated restoration scope",
            "source environment example outside a validated restoration scope",
            "source environment exercise outside a validated restoration scope",
            "source command \\tuple outside a validated restoration scope",
            "source command \\rng outside a validated restoration scope",
            "source command \\Mod outside a validated restoration scope",
            "source command \\Fm outside a validated restoration scope",
            "source command \\length outside a validated restoration scope",
            "source command \\restr outside a validated restoration scope",
            "source command \\rank outside a validated restoration scope",
            "source command \\ZF outside a validated restoration scope",
            "source command \\ZFC outside a validated restoration scope",
            "source command \\Z outside a validated restoration scope",
        )

    def test_propositional_source_commands_outside_scope_fail(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Editorial $\Prop,\CPL,\Sub(A),\True,\False$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source command \\Prop outside a validated restoration scope",
            "source command \\CPL outside a validated restoration scope",
            "source command \\Sub outside a validated restoration scope",
            "source command \\True outside a validated restoration scope",
            "source command \\False outside a validated restoration scope",
        )

    def test_deduction_source_commands_outside_scope_fail(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Editorial $\ND_{\CPL}$, $\LK_{\CPL}$, and $\LJ$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source command \\ND outside a validated restoration scope",
            "source command \\LK outside a validated restoration scope",
            "source command \\LJ outside a validated restoration scope",
        )

    def test_metatheory_source_syntax_outside_scope_fails(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"\begin{remark}Editorial remark.\end{remark}" + "\n"
            + r"Editorial $v\notentails\varphi$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source environment remark outside a validated restoration scope",
            "source command \\notentails outside a validated restoration scope",
        )

    def test_first_order_source_commands_outside_scope_fail(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Editorial $\Var,\Term(\Lang),\Sent(\Lang),\arity(f),\Meta$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source command \\Var outside a validated restoration scope",
            "source command \\Term outside a validated restoration scope",
            "source command \\Sent outside a validated restoration scope",
            "source command \\arity outside a validated restoration scope",
            "source command \\Meta outside a validated restoration scope",
        )

    def test_first_order_theory_source_commands_outside_scope_fail(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Editorial $\Th(\Meta),\Cn(T),\ND_{\FOL}$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source command \\Th outside a validated restoration scope",
            "source command \\Cn outside a validated restoration scope",
            "source command \\FOL outside a validated restoration scope",
        )

    def test_qe_source_syntax_outside_scope_fails(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"\begin{proofplan}Editorial sketch.\end{proofplan}" + "\n"
            + r"Editorial $\Q$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source environment proofplan outside a validated restoration scope",
            "source command \\Q outside a validated restoration scope",
        )

    def test_higher_order_source_real_command_outside_scope_fails(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Editorial $\R$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source command \\R outside a validated restoration scope"
        )

    def test_intuitionistic_source_ipl_command_outside_scope_fails(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Editorial $\IPL$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source command \\IPL outside a validated restoration scope"
        )

    def test_modal_source_system_commands_outside_scope_fail(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Editorial $\K,\Sfour,\Sfive$; registered verum $\topv$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source command \\K outside a validated restoration scope",
            "source command \\Sfour outside a validated restoration scope",
            "source command \\Sfive outside a validated restoration scope",
        )

    def test_escaped_source_command_names_are_not_false_positives(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Displayed command names: \\Pow and \\set." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_balanced_detokenize_argument_is_not_source_command_execution(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Displayed command name: \texttt{\detokenize{\Mod}}." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_detokenize_does_not_hide_later_source_command_execution(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"\texttt{\detokenize{\Mod}} followed by editorial $\Mod(T)$." + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            "source command \\Mod outside a validated restoration scope"
        )

    def test_rule_and_side_outside_scope_fail(self) -> None:
        part = self.root / "handbook" / "parts" / "p01" / "editorial.tex"
        part.parent.mkdir(parents=True, exist_ok=True)
        part.write_text(
            r"Editorial $\Rule[Name]{A}{B}\side{provided x}$ outside scope."
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self.assert_fails_with(
            r"\Rule rule display",
            r"source command \side outside a validated restoration scope",
        )


    def corrected_record(self, inserted: bytes = b"Candidate reader correction.\n") -> dict[str, object]:
        from tools.test_check_inherited_restoration import make_corrected_reader_fixture
        return make_corrected_reader_fixture(self.root,
            self.root / f"spec/provenance/{PROVENANCE_ID}.json", [(0, 0, inserted)])

    def test_corrected_candidate_keeps_source_syntax_without_admission(self) -> None:
        record = self.corrected_record()
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(record["verification"]["build"], "pending")
        self.assertEqual(record["verification"]["visual"], "pending")
        self.assertEqual(record["handbook_destination"]["status"], "open/missing")

    def test_duplicate_corrected_wrapper_is_rejected(self) -> None:
        self.corrected_record()
        main = self.root / "handbook/main.tex"
        main.write_text(main.read_text() * 2, encoding="utf-8")
        self.assert_fails_with("restoration-scope", "reachable")

    def test_new_correction_reference_does_not_get_source_future_exemption(self) -> None:
        self.corrected_record(b"New reference: \\ref{thm:prop-unique-readability}.\n")
        result = self.run_check()
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn("dangling-ref", output)
        self.assertIn("thm:prop-unique-readability", output)
        self.assertNotIn("[pending-inherited-ref]", output)

    def test_reference_policy_distinguishes_mapped_and_corrected_lines(self) -> None:
        from tools import check as checker, check_inherited_restoration as restoration
        record = self.corrected_record()
        restoration.validate_record(record, self.root / f"spec/provenance/{PROVENANCE_ID}.json", self.root)
        data = checker._HBData()
        data.authorized_restorations[ARTIFACT] = {
            "provenance_id": PROVENANCE_ID, "governed_end_line": 443,
            "authorization_kind": "corrected-reader",
            "source_line_map": restoration.reader_source_line_map(record),
        }
        # Exercise the reference-policy consumer with one changed and one
        # validated original line; scanner-generated locations have this shape.
        data.refs = [("thm:future-new", f"{ARTIFACT}:1", ARTIFACT),
                     ("thm:future-original", f"{ARTIFACT}:2", ARTIFACT)]
        checker._hb_cross_checks(data, {"thm:future-new": 1000, "thm:future-original": 1001})
        self.assertEqual([x["target"] for x in data.pending_inherited_refs], ["thm:future-original"])
        self.assertTrue(any("future-new" in value for value in data.findings["dangling-ref"]))

    def test_audit_metadata_does_not_invent_source_lines_for_new_text(self) -> None:
        from tools import audit_tables
        self.corrected_record(b"\\begin{definition}[Candidate correction]\nNew reader text.\n\\end{definition}\n")
        parts = self.root / "handbook/parts"
        parts.mkdir()
        (parts / "p01.tex").write_text(r"\input{restoration/scope-" + PROVENANCE_ID + "}\n", encoding="utf-8")
        rows = audit_tables.collect(self.root)["01"]
        self.assertEqual(rows[0][1], "Candidate correction")
        self.assertEqual(rows[1][1], "Ordered pair")
        self.assertIsNone(audit_tables.source_line(self.root / "handbook" / ARTIFACT, 1))
        artifact = self.root / "handbook" / ARTIFACT
        artifact.write_bytes(artifact.read_bytes() + b"Unrecorded.\n")
        with self.assertRaises(ValueError):
            audit_tables.collect(self.root)

    def test_candidate_audit_projection_cannot_promote_active_output(self) -> None:
        from tools import audit_tables
        self.corrected_record()
        parts = self.root / "handbook/parts"; parts.mkdir()
        (parts / "p01.tex").write_text(r"\input{restoration/scope-" + PROVENANCE_ID + "}\n", encoding="utf-8")
        result = subprocess.run([sys.executable, str(ROOT / "tools/audit_tables.py"), "--root", str(self.root)],
                                text=True, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("terminal admission input", result.stderr)
        self.assertFalse((self.root / "handbook/generated").exists())

@unittest.skipUnless(PDFLATEX, "pdflatex is required for TeX scope tests")
class RestorationScopeTeXTests(unittest.TestCase):
    def assert_references_defined_in_handbook(self, log: str) -> None:
        """A fixture compiles a few captures alone. A corrected capture (version-4 record) may
        link to a proof in a routed handbook file outside the fixture; such a reference is
        unresolved in the fixture but must be defined somewhere in the handbook."""
        flat = log.replace("\n", "")  # TeX wraps log lines at 79 columns without spaces
        labels = set(re.findall(r"LaTeX Warning: (?:Hyper reference|Reference) `([^']+)'", flat))
        if not labels:
            return
        defined: set[str] = set()
        for path in HANDBOOK_TEX.rglob("*.tex"):
            text = path.read_text(encoding="utf-8", errors="replace")
            defined.update(label for label in labels if "{" + label + "}" in text
                           and re.search(r"(?:\\label|\\begin\{\w+\*?\})\s*\{" + re.escape(label) + r"\}", text))
        self.assertEqual(sorted(labels - defined), [], "references defined nowhere in the handbook")

    def compile_with_outputs(
        self, body: str, runs: int = 1
    ) -> tuple[subprocess.CompletedProcess[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        build = Path(temporary.name)
        (build / "fixture.tex").write_text(
            r"\documentclass{book}" + "\n"
            + r"\usepackage{handbook}" + "\n"
            + r"\begin{document}" + "\n"
            + body + "\n"
            + r"\end{document}" + "\n",
            encoding="utf-8",
            newline="\n",
        )
        env = os.environ.copy()
        env["TEXINPUTS"] = str(HANDBOOK_TEX) + os.pathsep
        completed: subprocess.CompletedProcess[str] | None = None
        for _ in range(runs):
            completed = subprocess.run(
                [
                    str(PDFLATEX),
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "fixture.tex",
                ],
                cwd=build,
                env=env,
                text=True,
                capture_output=True,
                timeout=120,
            )
            if completed.returncode != 0:
                break
        assert completed is not None
        return completed, build

    def compile(self, body: str) -> subprocess.CompletedProcess[str]:
        completed, _build = self.compile_with_outputs(body)
        return completed

    def test_compile_time_proof_exemption_is_lexically_bounded(self) -> None:
        after_scope = self.compile(
            r"\begin{inheritedrestorationscope}{SRC-00406-00443}"
            r"\begin{proof}Inherited proof.\end{proof}"
            r"\end{inheritedrestorationscope}"
            r"\begin{proof}Editorial proof after the scope.\end{proof}"
        )
        output = after_scope.stdout + after_scope.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertNotEqual(after_scope.returncode, 0, output)
        self.assertIn("proof environment outside the annex", output)

    def test_source_notation_and_warning_compile_only_inside_scope(self) -> None:
        inside = self.compile(
            r"\newcommand\expectedsourceeq{\mathrel{:=}}"
            r"\newcommand\expectededitorialeq{\mathrel{:\equiv}}"
            r"\begin{inheritedrestorationscope}{SRC-00373-00405}"
            r"\ifx\defeq\expectedsourceeq\else"
            r"\PackageError{fixture}{source defeq meaning was not restored}{}\fi"
            r"\begin{definition}[Power set]"
            r"$\Pow(A)\defeq\set{x:x\in A}$."
            r"\end{definition}"
            r"\begin{warning}Inherited warning.\end{warning}"
            r"\end{inheritedrestorationscope}"
            r"\ifx\defeq\expectededitorialeq\else"
            r"\PackageError{fixture}{editorial defeq meaning leaked}{}\fi"
        )
        inside_output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in inside_output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, inside_output)

        outside = self.compile(r"Editorial $\Pow(A)=\set{x:x\in A}$.")
        output = outside.stdout + outside.stderr
        self.assertNotEqual(outside.returncode, 0, output)
        self.assertIn("source Pow command outside", output)

    def test_two_sequential_scopes_do_not_conflict(self) -> None:
        sequential = self.compile(
            r"\begin{inheritedrestorationscope}{SRC-00406-00443}"
            r"\begin{proof}First inherited proof.\end{proof}"
            r"\end{inheritedrestorationscope}"
            r"\begin{inheritedrestorationscope}{SRC-00533-00602}"
            r"\begin{proof}Second inherited proof.\end{proof}"
            r"\end{inheritedrestorationscope}"
        )
        output = sequential.stdout + sequential.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(sequential.returncode, 0, output)

    def test_first_chapter_source_syntax_compiles_only_inside_scope(self) -> None:
        inside = self.compile(
            r"\begin{inheritedrestorationscope}{SRC-00406-00443}"
            r"\chapter{Inherited fixture}"
            r"\begin{definition}[Ordered pair]"
            r"$\tuple{x,y}\defeq\set{x,\set{x,y}}$."
            r"\end{definition}"
            r"\begin{lemma}[Pair equality]\label{lem:fixture-pair}"
            r"$\tuple{x,y}=\tuple{x,y}$."
            r"\end{lemma}"
            r"\begin{proof}Immediate.\end{proof}"
            r"\begin{method}[Quotient method]Use representatives.\end{method}"
            r"\begin{theorem}[Finite range]\label{thm:fixture-range}"
            r"$\rng(f)\subseteq\Z$."
            r"\end{theorem}"
            r"\begin{corollary}The range is a set.\end{corollary}"
            r"\begin{example}[Model class]"
            r"$\Mod(T)=\set{\mathcal M:\mathcal M\entails T}$."
            r"\end{example}"
            r"\begin{exercise}Compare $\ZF$, $\ZFC$, and $\Z$.\end{exercise}"
            r"By \cref{lem:fixture-pair,thm:fixture-range}, the claims hold."
            r"\end{inheritedrestorationscope}"
        )
        inside_output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in inside_output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, inside_output)

        outside = self.compile(r"\begin{lemma}Editorial lemma.\end{lemma}")
        outside_output = outside.stdout + outside.stderr
        self.assertNotEqual(outside.returncode, 0, outside_output)
        self.assertIn("source lemma environment outside", outside_output)

    def test_example_and_mod_have_exact_source_semantics_only_inside_scope(self) -> None:
        inside = self.compile(
            r"\makeatletter"
            r"\begin{inheritedrestorationscope}{SRC-00798-00852}"
            r"\newcommand\expectedmod{\operatorname{Mod}}"
            r"\ifx\Mod\expectedmod\else"
            r"\PackageError{fixture}{source Mod meaning was not restored}{}\fi"
            r"\setcounter{hbitem}{6}"
            r"\begin{example}[Shared counter]\label{ex:fixture-shared}Body.\end{example}"
            r"\ifnum\value{hbitem}=7\else"
            r"\PackageError{fixture}{source example did not share hbitem}{}\fi"
            r"\end{inheritedrestorationscope}"
            r"\makeatother"
        )
        inside_output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in inside_output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, inside_output)

        outside_example = self.compile(r"\begin{example}Editorial.\end{example}")
        outside_example_output = outside_example.stdout + outside_example.stderr
        self.assertNotEqual(outside_example.returncode, 0, outside_example_output)
        self.assertIn("source example environment outside", outside_example_output)

        outside_mod = self.compile(r"Editorial $\Mod(T)$.")
        outside_mod_output = outside_mod.stdout + outside_mod.stderr
        self.assertNotEqual(outside_mod.returncode, 0, outside_mod_output)
        self.assertIn("source Mod command outside", outside_mod_output)

    def test_qe_command_and_proofplan_are_exact_and_scope_local(self) -> None:
        inside = self.compile(
            r"\begin{inheritedrestorationscope}{SRC-07150-07294}"
            r"\begin{proofplan}A scoped source sketch.\end{proofplan}"
            r"\end{inheritedrestorationscope}"
            r"\begin{inheritedrestorationscope}{SRC-07678-07752}"
            r"\begin{proofplan}The first Part IV source sketch.\end{proofplan}"
            r"\end{inheritedrestorationscope}"
            r"\begin{inheritedrestorationscope}{SRC-07753-07843}"
            r"\begin{proofplan}The second Part IV source sketch.\end{proofplan}"
            r"\end{inheritedrestorationscope}"
            r"\begin{inheritedrestorationscope}{SRC-07469-07493}"
            r"The source field is $\Q$."
            r"\end{inheritedrestorationscope}"
        )
        inside_output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in inside_output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, inside_output)

        for body, needle in (
            (r"Editorial $\Q$.", "source Q command outside"),
            (
                r"\begin{proofplan}Editorial sketch.\end{proofplan}",
                "source proofplan environment outside",
            ),
        ):
            with self.subTest(body=body):
                outside = self.compile(body)
                output = outside.stdout + outside.stderr
                self.assertNotEqual(outside.returncode, 0, output)
                self.assertIn(needle, output)

    def test_string_commands_and_list_presentation_are_scope_local(self) -> None:
        inside_and_after = self.compile(
            r"\makeatletter"
            r"\newcommand\expectedfm{\mathsf{Fm}}"
            r"\newcommand\expectedlength{\operatorname{len}}"
            r"\newcommand\expectedrestr{\mathbin{\upharpoonright}}"
            r"\begin{inheritedrestorationscope}{SRC-01101-01147}"
            r"\ifx\Fm\expectedfm\else"
            r"\PackageError{fixture}{source Fm meaning was not restored}{}\fi"
            r"\ifx\length\expectedlength\else"
            r"\PackageError{fixture}{source length meaning was not restored}{}\fi"
            r"\ifx\restr\expectedrestr\else"
            r"\PackageError{fixture}{source restr meaning was not restored}{}\fi"
            r"\begin{enumerate}"
            r"\ifdim\topsep=0pt\else"
            r"\PackageError{fixture}{source enumerate topsep was not nosep}{}\fi"
            r"\ifdim\itemsep=0pt\else"
            r"\PackageError{fixture}{source enumerate itemsep was not nosep}{}\fi"
            r"\ifdim\parsep=0pt\else"
            r"\PackageError{fixture}{source enumerate parsep was not nosep}{}\fi"
            r"\ifdim\partopsep=0pt\else"
            r"\PackageError{fixture}{source enumerate partopsep was not nosep}{}\fi"
            r"\ifdim\leftmargin<\leftmargini\else"
            r"\PackageError{fixture}{source enumerate leftmargin star was not restored}{}\fi"
            r"\item $\length(w\restr n)\in\Fm$."
            r"\end{enumerate}"
            r"\begin{itemize}"
            r"\ifdim\topsep=0pt\else"
            r"\PackageError{fixture}{source itemize topsep was not nosep}{}\fi"
            r"\ifdim\itemsep=0pt\else"
            r"\PackageError{fixture}{source itemize itemsep was not nosep}{}\fi"
            r"\ifdim\parsep=0pt\else"
            r"\PackageError{fixture}{source itemize parsep was not nosep}{}\fi"
            r"\ifdim\partopsep=0pt\else"
            r"\PackageError{fixture}{source itemize partopsep was not nosep}{}\fi"
            r"\item Source item."
            r"\end{itemize}"
            r"\end{inheritedrestorationscope}"
            r"\begin{enumerate}"
            r"\ifdim\topsep>0pt\else"
            r"\PackageError{fixture}{source enumerate nosep leaked}{}\fi"
            r"\ifdim\leftmargin=\leftmargini\else"
            r"\PackageError{fixture}{source enumerate leftmargin leaked}{}\fi"
            r"\item Editorial list."
            r"\end{enumerate}"
            r"\begin{itemize}"
            r"\ifdim\topsep>0pt\else"
            r"\PackageError{fixture}{source itemize nosep leaked}{}\fi"
            r"\item Editorial item."
            r"\end{itemize}"
            r"\makeatother"
        )
        output = inside_and_after.stdout + inside_and_after.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside_and_after.returncode, 0, output)

        for body, needle in (
            (r"Editorial $\Fm$.", "source Fm command outside"),
            (r"Editorial $\length(w)$.", "source length command outside"),
            (r"Editorial $w\restr n$.", "source restr command outside"),
        ):
            with self.subTest(body=body):
                outside = self.compile(body)
                outside_output = outside.stdout + outside.stderr
                self.assertNotEqual(outside.returncode, 0, outside_output)
                self.assertIn(needle, outside_output)

    def test_rule_and_side_have_exact_source_semantics_only_inside_scope(self) -> None:
        inside = self.compile(
            r"\makeatletter"
            r"\begin{inheritedrestorationscope}{SRC-01580-01591}"
            r"\setbox0=\hbox{$\Rule[\(\forall I\)]{A}{B}$}"
            r"\setbox1=\hbox{$\frac{A}{B}\;\textsc{\(\forall I\)}$}"
            r"\ifdim\wd0=\wd1\else"
            r"\PackageError{fixture}{named source Rule width differed}{}\fi"
            r"\ifdim\ht0=\ht1\else"
            r"\PackageError{fixture}{named source Rule height differed}{}\fi"
            r"\ifdim\dp0=\dp1\else"
            r"\PackageError{fixture}{named source Rule depth differed}{}\fi"
            r"\setbox0=\hbox{$\Rule{A}{B}$}"
            r"\setbox1=\hbox{$\frac{A}{B}\;\textsc{}$}"
            r"\ifdim\wd0=\wd1\else"
            r"\PackageError{fixture}{unnamed source Rule width differed}{}\fi"
            r"\ifdim\ht0=\ht1\else"
            r"\PackageError{fixture}{unnamed source Rule height differed}{}\fi"
            r"\ifdim\dp0=\dp1\else"
            r"\PackageError{fixture}{unnamed source Rule depth differed}{}\fi"
            r"\setbox0=\hbox{$A\side{provided \(x\)}$}"
            r"\setbox1=\hbox{$A\quad\text{provided \(x\)}$}"
            r"\ifdim\wd0=\wd1\else"
            r"\PackageError{fixture}{source side width differed}{}\fi"
            r"\ifdim\ht0=\ht1\else"
            r"\PackageError{fixture}{source side height differed}{}\fi"
            r"\ifdim\dp0=\dp1\else"
            r"\PackageError{fixture}{source side depth differed}{}\fi"
            r"\end{inheritedrestorationscope}"
            r"\makeatother"
        )
        inside_output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in inside_output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, inside_output)

        for body, needle in (
            (r"Editorial $\Rule[Name]{A}{B}$.", "source Rule command outside"),
            (r"Editorial $A\side{provided x}$.", "source side command outside"),
        ):
            with self.subTest(body=body):
                outside = self.compile(body)
                outside_output = outside.stdout + outside.stderr
                self.assertNotEqual(outside.returncode, 0, outside_output)
                self.assertIn(needle, outside_output)

    def test_writing_chapter_citations_and_longtable_compile_in_scopes(self) -> None:
        completed = self.compile(
            r"\input{restoration/scope-SRC-01411-01504}"
            r"\input{restoration/scope-SRC-01505-01553}"
            r"\input{restoration/scope-SRC-01554-01579}"
            r"\input{restoration/scope-SRC-01580-01591}"
            r"\input{restoration/scope-SRC-01592-01631}"
            r"\input{restoration/scope-SRC-01632-01648}"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_exact_propositional_source_chapter_compiles_in_five_scopes(self) -> None:
        completed = self.compile(
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\input{restoration/scope-SRC-01649-01660}"
            r"\input{restoration/scope-SRC-01661-01816}"
            r"\input{restoration/scope-SRC-01817-01898}"
            r"\input{restoration/scope-SRC-01899-01945}"
            r"\input{restoration/scope-SRC-01946-02186}"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_propositional_source_commands_and_global_accent_are_scope_local(self) -> None:
        inside = self.compile(
            r"\makeatletter"
            r"\providecommand\B[1]{\underbar{#1}}"
            r"\let\expectedaccent\B"
            r"\newcommand\expectedprop{\mathsf{Prop}}"
            r"\newcommand\expectedcpl{\mathsf{CPL}}"
            r"\newcommand\expectedsub{\operatorname{Sub}}"
            r"\newcommand\expectedtrue{\mathbf{T}}"
            r"\newcommand\expectedfalse{\mathbf{F}}"
            r"\newcommand\expectedb{\mathbb{B}}"
            r"\begin{inheritedrestorationscope}{SRC-01661-01816}"
            r"\ifx\Prop\expectedprop\else\PackageError{fixture}{Prop differed}{}\fi"
            r"\ifx\CPL\expectedcpl\else\PackageError{fixture}{CPL differed}{}\fi"
            r"\ifx\Sub\expectedsub\else\PackageError{fixture}{Sub differed}{}\fi"
            r"\ifx\True\expectedtrue\else\PackageError{fixture}{True differed}{}\fi"
            r"\ifx\False\expectedfalse\else\PackageError{fixture}{False differed}{}\fi"
            r"\ifx\B\expectedb\else\PackageError{fixture}{B differed}{}\fi"
            r"$\Prop\;\CPL\;\Sub(\B)\;\True\;\False$."
            r"\end{inheritedrestorationscope}"
            r"\ifx\B\expectedaccent\else\PackageError{fixture}{B accent leaked}{}\fi"
            r"\setbox0=\hbox{\B{a}}"
            r"\makeatother"
        )
        output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, output)

        for command in (r"\Prop", r"\CPL", r"\Sub(A)", r"\True", r"\False"):
            with self.subTest(command=command):
                outside = self.compile(rf"Editorial ${command}$.")
                outside_output = outside.stdout + outside.stderr
                self.assertNotEqual(outside.returncode, 0, outside_output)
                name = command.lstrip("\\").split("(", 1)[0]
                self.assertIn(f"source {name} command outside", outside_output)

    def test_deduction_source_commands_have_exact_scope_local_meanings(self) -> None:
        inside = self.compile(
            r"\makeatletter"
            r"\newcommand\expectednd{\mathsf{ND}}"
            r"\newcommand\expectedlk{\mathsf{LK}}"
            r"\begin{inheritedrestorationscope}{SRC-02193-02340}"
            r"\ifx\ND\expectednd\else\PackageError{fixture}{ND differed}{}\fi"
            r"\ifx\LK\expectedlk\else\PackageError{fixture}{LK differed}{}\fi"
            r"$\ND_{\CPL}\;\LK_{\CPL}$."
            r"\end{inheritedrestorationscope}"
            r"\makeatother"
        )
        output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, output)

        for command in (r"\ND", r"\LK"):
            with self.subTest(command=command):
                outside = self.compile(rf"Editorial ${command}$.")
                outside_output = outside.stdout + outside.stderr
                self.assertNotEqual(outside.returncode, 0, outside_output)
                name = command.lstrip("\\")
                self.assertIn(f"source {name} command outside", outside_output)

    def test_metatheory_source_syntax_is_scope_local_and_remark_is_unindexed(self) -> None:
        inside, build = self.compile_with_outputs(
            r"\makeatletter"
            r"\newcommand\expectednotentails{\not\models}"
            r"\begin{inheritedrestorationscope}{SRC-02810-02914}"
            r"\ifx\notentails\expectednotentails\else"
            r"\PackageError{fixture}{notentails differed}{}\fi"
            r"\begin{remark}[Scope fixture]\label{rem:fixture}"
            r"$v\notentails\varphi$.\end{remark}"
            r"\ifnum\value{hbitem}=1\else"
            r"\PackageError{fixture}{source remark counter differed}{}\fi"
            r"\end{inheritedrestorationscope}"
            r"\makeatother"
        )
        inside_output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in inside_output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, inside_output)
        self.assertEqual(
            (build / "fixture.idx").read_text(encoding="utf-8").count(
                r"\indexentry"
            ),
            0,
        )

        for body, needle in (
            (r"Editorial $v\notentails\varphi$.", "source notentails command outside"),
            (
                r"\begin{remark}Editorial remark.\end{remark}",
                "source remark environment outside",
            ),
        ):
            with self.subTest(body=body):
                outside = self.compile(body)
                outside_output = outside.stdout + outside.stderr
                self.assertNotEqual(outside.returncode, 0, outside_output)
                self.assertIn(needle, outside_output)

    def test_source_convention_is_scope_local_shared_and_unindexed(self) -> None:
        inside, build = self.compile_with_outputs(
            r"\input{restoration/scope-SRC-06049-06069}"
            r"\ifnum\value{hbitem}=1\else"
            r"\PackageError{fixture}{source convention counter differed}{}\fi"
        )
        inside_output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in inside_output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, inside_output)
        self.assertEqual(
            (build / "fixture.idx").read_text(encoding="utf-8").count(
                r"\indexentry"
            ),
            0,
        )

        outside = self.compile(
            r"\begin{convention}[Editorial]Not source.\end{convention}"
        )
        outside_output = outside.stdout + outside.stderr
        self.assertNotEqual(outside.returncode, 0, outside_output)
        self.assertIn("source convention environment outside", outside_output)

    def test_exact_maps_substructures_elementarity_compiles_with_source_surface(self) -> None:
        completed, build = self.compile_with_outputs(
            r"\input{restoration/scope-SRC-06049-06069}"
            r"\input{restoration/scope-SRC-06070-06137}"
            r"\input{restoration/scope-SRC-06138-06242}"
            r"\input{restoration/scope-SRC-06243-06331}"
            r"\input{restoration/scope-SRC-06332-06421}"
            r"\input{restoration/scope-SRC-06422-06431}"
            r"\input{restoration/scope-SRC-06432-06493}"
            r"\input{restoration/scope-SRC-06494-06509}"
            r"\ifnum\value{part}=1\else"
            r"\PackageError{fixture}{source part counter differed}{}\fi"
            r"\ifnum\value{hbitem}=25\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 12)
        for title in (
            "Homomorphism",
            "Embedding",
            "Tarski--Vaught test",
            "Diagram tests for embeddings",
            "Elementary chain theorem",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        labels = {
            "part:model-theory",
            "ch:maps-elementarity",
            "sec:maps-elementarity-01",
            "lem:term-preservation",
            "sec:maps-elementarity-02",
            "lem:iso-invariance",
            "lem:embedding-image",
            "sec:maps-elementarity-03",
            "thm:tarski-vaught",
            "sec:maps-elementarity-04",
            "sec:diagrams",
            "def:parameter-expansion",
            "def:diagrams",
            "thm:diagram-tests",
            "ex:maps-elementarity-01",
            "ex:diagram-test",
            "sec:maps-elementarity-05",
            "thm:elementary-chain",
            "ex:maps-elementarity-02",
            "ex:maps-elementarity-03",
        }
        self.assertEqual(len(labels), 20)
        for label in labels:
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

    def test_exact_types_saturation_ultraproducts_compiles_with_source_surface(self) -> None:
        completed, build = self.compile_with_outputs(
            r"\input{restoration/scope-SRC-06049-06069}"
            r"\input{restoration/scope-SRC-06070-06137}"
            r"\input{restoration/scope-SRC-06138-06242}"
            r"\input{restoration/scope-SRC-06243-06331}"
            r"\input{restoration/scope-SRC-06332-06421}"
            r"\input{restoration/scope-SRC-06422-06431}"
            r"\input{restoration/scope-SRC-06432-06493}"
            r"\input{restoration/scope-SRC-06494-06509}"
            r"\input{restoration/scope-SRC-06510-06629}"
            r"\input{restoration/scope-SRC-06630-06639}"
            r"\input{restoration/scope-SRC-06640-06693}"
            r"\input{restoration/scope-SRC-06694-06782}"
            r"\input{restoration/scope-SRC-06783-06791}"
            r"\input{restoration/scope-SRC-06792-06845}"
            r"\input{restoration/scope-SRC-06846-06854}"
            r"\input{restoration/scope-SRC-06855-06941}"
            r"\input{restoration/scope-SRC-06942-07134}"
            r"\input{restoration/scope-SRC-07135-07149}"
            r"\ifnum\value{part}=1\else"
            r"\PackageError{fixture}{source part counter differed}{}\fi"
            r"\ifnum\value{hbitem}=29\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 25)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        labels = {
            "ch:types-ultraproducts",
            "sec:types-ultraproducts-01",
            "def:type-space",
            "thm:type-space-compact",
            "ex:types-ultraproducts-01",
            "ex:type-space-basis",
            "thm:saturated-extension",
            "sec:types-ultraproducts-02",
            "sec:homogeneity",
            "def:homogeneity",
            "thm:saturation-homogeneity",
            "ex:types-ultraproducts-02",
            "ex:homogeneity-back-step",
            "sec:types-ultraproducts-03",
            "sec:omitting-types",
            "def:principal-type",
            "thm:omitting-types",
            "ex:types-ultraproducts-03",
            "ex:omit-constant-type",
            "sec:types-ultraproducts-04",
            "lem:nonprincipal-ultrafilter",
            "sec:types-ultraproducts-05",
            "lem:los-terms",
            "thm:los",
            "cor:diagonal-ultrapower",
            "ex:types-ultraproducts-04",
            "ex:types-ultraproducts-05",
        }
        self.assertEqual(len(labels), 27)
        for label in labels:
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

    def test_exact_deduction_chapter_compiles_with_shared_counter_and_index(self) -> None:
        completed, build = self.compile_with_outputs(
            r"\input{restoration/scope-SRC-02187-02192}"
            r"\input{restoration/scope-SRC-02193-02340}"
            r"\input{restoration/scope-SRC-02341-02450}"
            r"\ifnum\value{hbitem}=7\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 3)
        for title in (
            "Natural-deduction derivation",
            "Propositional derivability",
            "Sequent",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:prop-deduction",
            "sec:prop-deduction-01",
            "lem:nd-substitution",
            "sec:prop-deduction-02",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

    def test_exact_propositional_metatheory_compiles_with_source_surface(self) -> None:
        completed, build = self.compile_with_outputs(
            r"\input{restoration/scope-SRC-02451-02544}"
            r"\input{restoration/scope-SRC-02545-02664}"
            r"\input{restoration/scope-SRC-02665-02809}"
            r"\input{restoration/scope-SRC-02810-02914}"
            r"\input{restoration/scope-SRC-02915-02932}"
            r"\input{restoration/scope-SRC-02933-03021}"
            r"\ifnum\value{hbitem}=27\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 10)
        for title in (
            "Soundness of classical propositional natural deduction",
            "Consistency",
            "Resolvent",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:prop-metatheory",
            "thm:prop-nd-soundness",
            "thm:prop-lk-soundness",
            "lem:prop-lindenbaum",
            "thm:prop-completeness",
            "thm:prop-compactness",
            "thm:prop-lk-completeness",
            "thm:prop-resolution-complete",
            "rem:resolution-finiteness",
            "ex:prop-metatheory-12",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

    def test_first_order_source_commands_have_exact_scope_local_meanings(self) -> None:
        inside = self.compile(
            r"\makeatletter"
            r"\newcommand\expectedvar{\mathsf{Var}}"
            r"\newcommand\expectedterm{\mathsf{Term}}"
            r"\newcommand\expectedsent{\mathsf{Sent}}"
            r"\newcommand\expectedarity{\operatorname{ar}}"
            r"\newcommand\expectedlang{\mathcal{L}}"
            r"\newcommand\expectedn{\mathbb{N}}"
            r"\newcommand\expectedfm{\mathsf{Fm}}"
            r"\newcommand\expectedfv{\operatorname{FV}}"
            r"\newcommand\expectedbottom{\bot}"
            r"\newcommand\expectedset[1]{\lbrace#1\rbrace}"
            r"\newcommand\expectedtuple[1]{\langle#1\rangle}"
            r"\newcommand\expectedabs[1]{\lvert#1\rvert}"
            r"\newcommand\expectedsourceeq{\mathrel{:=}}"
            r"\begin{inheritedrestorationscope}{SRC-03038-03104}"
            r"\ifx\Var\expectedvar\else\PackageError{fixture}{Var differed}{}\fi"
            r"\ifx\Term\expectedterm\else\PackageError{fixture}{Term differed}{}\fi"
            r"\ifx\Sent\expectedsent\else\PackageError{fixture}{Sent differed}{}\fi"
            r"\ifx\arity\expectedarity\else\PackageError{fixture}{arity differed}{}\fi"
            r"\ifx\Lang\expectedlang\else\PackageError{fixture}{Lang differed}{}\fi"
            r"\ifx\N\expectedn\else\PackageError{fixture}{N differed}{}\fi"
            r"\ifx\Fm\expectedfm\else\PackageError{fixture}{Fm differed}{}\fi"
            r"\ifx\FV\expectedfv\else\PackageError{fixture}{FV differed}{}\fi"
            r"\ifx\bottom\expectedbottom\else\PackageError{fixture}{bottom differed}{}\fi"
            r"\ifx\set\expectedset\else\PackageError{fixture}{set differed}{}\fi"
            r"\ifx\tuple\expectedtuple\else\PackageError{fixture}{tuple differed}{}\fi"
            r"\ifx\abs\expectedabs\else\PackageError{fixture}{abs differed}{}\fi"
            r"\ifx\defeq\expectedsourceeq\else\PackageError{fixture}{defeq differed}{}\fi"
            r"$\Var\;\Term(\Lang)\;\Sent(\Lang)\;\arity(f)\;\N\;\Fm(\Lang)"
            r"\;\FV(\varphi)\;\bottom\;\set{x}\;\tuple{x}\;\abs{x}\;x\defeq y$."
            r"\end{inheritedrestorationscope}"
            r"\makeatother"
        )
        output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, output)

        for command in (r"\Var", r"\Term(\Lang)", r"\Sent(\Lang)", r"\arity(f)"):
            with self.subTest(command=command):
                outside = self.compile(rf"Editorial ${command}$.")
                outside_output = outside.stdout + outside.stderr
                self.assertNotEqual(outside.returncode, 0, outside_output)
                name = command.lstrip("\\").split("(", 1)[0]
                self.assertIn(f"source {name} command outside", outside_output)

    def test_first_order_semantics_meta_is_exact_and_scope_local(self) -> None:
        inside = self.compile(
            r"\makeatletter"
            r"\newcommand\expectedmeta{\mathcal M}"
            r"\let\expectedsem\sem"
            r"\let\expectedequiv\equiv"
            r"\begin{inheritedrestorationscope}{SRC-03429-03518}"
            r"\ifx\Meta\expectedmeta\else"
            r"\PackageError{fixture}{Meta differed}{}\fi"
            r"\ifx\sem\expectedsem\else"
            r"\PackageError{fixture}{sem was redefined}{}\fi"
            r"\ifx\equiv\expectedequiv\else"
            r"\PackageError{fixture}{equiv was redefined}{}\fi"
            r"$\abs{\Meta}\;\sem{t}^{\Meta}_s\;\varphi\equiv\psi$."
            r"\end{inheritedrestorationscope}"
            r"\makeatother"
        )
        output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, output)

        outside = self.compile(r"Editorial $\Meta$.")
        outside_output = outside.stdout + outside.stderr
        self.assertNotEqual(outside.returncode, 0, outside_output)
        self.assertIn("source Meta command outside", outside_output)

    def test_first_order_theory_commands_have_exact_scope_local_meanings(self) -> None:
        inside = self.compile(
            r"\makeatletter"
            r"\newcommand\expectedth{\operatorname{Th}}"
            r"\newcommand\expectedcn{\operatorname{Cn}}"
            r"\newcommand\expectedfol{\mathsf{FOL}}"
            r"\begin{inheritedrestorationscope}{SRC-03729-03907}"
            r"\ifx\Th\expectedth\else"
            r"\PackageError{fixture}{Th differed}{}\fi"
            r"\ifx\Cn\expectedcn\else"
            r"\PackageError{fixture}{Cn differed}{}\fi"
            r"\ifx\FOL\expectedfol\else"
            r"\PackageError{fixture}{FOL differed}{}\fi"
            r"$\Th_{\Lang}(\Meta)\;\Cn(T)\;\ND_{\FOL}$."
            r"\end{inheritedrestorationscope}"
            r"\makeatother"
        )
        output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, output)

        for command, name in (
            (r"\Th(\Meta)", "Th"),
            (r"\Cn(T)", "Cn"),
            (r"\FOL", "FOL"),
        ):
            with self.subTest(command=command):
                outside = self.compile(rf"Editorial ${command}$.")
                outside_output = outside.stdout + outside.stderr
                self.assertNotEqual(outside.returncode, 0, outside_output)
                self.assertIn(f"source {name} command outside", outside_output)

    def test_exact_first_order_syntax_compiles_with_source_surface(self) -> None:
        completed, build = self.compile_with_outputs(
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\input{restoration/scope-SRC-03022-03037}"
            r"\input{restoration/scope-SRC-03038-03104}"
            r"\input{restoration/scope-SRC-03105-03165}"
            r"\input{restoration/scope-SRC-03166-03239}"
            r"\input{restoration/scope-SRC-03240-03428}"
            r"\ifnum\value{hbitem}=15\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 10)
        for title in (
            "First-order signature",
            "Term",
            "Unique readability for first-order expressions",
            "Alpha-equivalence",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "part:classical-first-order",
            "ch:fol-syntax-semantics",
            "sec:fol-syntax-semantics-01",
            "thm:fol-unique-readability",
            "lem:substitution-complexity",
            "lem:substitution-fv",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

    def test_exact_first_order_semantics_compiles_with_source_surface(self) -> None:
        completed, build = self.compile_with_outputs(
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\input{restoration/scope-SRC-03022-03037}"
            r"\input{restoration/scope-SRC-03038-03104}"
            r"\input{restoration/scope-SRC-03105-03165}"
            r"\input{restoration/scope-SRC-03166-03239}"
            r"\input{restoration/scope-SRC-03240-03428}"
            r"\input{restoration/scope-SRC-03429-03518}"
            r"\input{restoration/scope-SRC-03519-03680}"
            r"\input{restoration/scope-SRC-03681-03728}"
            r"\ifnum\value{hbitem}=14\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 17)
        for title in (
            "First-order structure",
            "Satisfaction",
            "Substitution lemma",
            "Truth, validity, and semantic consequence",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:fol-semantics",
            "sec:fol-semantics-01",
            "lem:term-substitution",
            "sec:fol-semantics-02",
            "lem:fol-coincidence",
            "thm:fol-substitution",
            "cor:alpha-invariance",
            "sec:fol-semantics-03",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

    def test_exact_first_order_theories_compiles_with_source_surface(self) -> None:
        completed, build = self.compile_with_outputs(
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\input{restoration/scope-SRC-03022-03037}"
            r"\input{restoration/scope-SRC-03038-03104}"
            r"\input{restoration/scope-SRC-03105-03165}"
            r"\input{restoration/scope-SRC-03166-03239}"
            r"\input{restoration/scope-SRC-03240-03428}"
            r"\input{restoration/scope-SRC-03429-03518}"
            r"\input{restoration/scope-SRC-03519-03680}"
            r"\input{restoration/scope-SRC-03681-03728}"
            r"\input{restoration/scope-SRC-03729-03907}"
            r"\input{restoration/scope-SRC-03908-03926}"
            r"\ifnum\value{hbitem}=8\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 20)
        for title in (
            "Theory, model, satisfiability, and structure theory",
            "Axiomatization",
            "Conservativity of definitional extensions",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:fol-theories",
            "def:fol-theory-satisfiability",
            "thm:definitional-conservativity",
            "sec:fol-theories-01",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

    def test_exact_first_order_deduction_compiles_with_source_surface(self) -> None:
        completed, build = self.compile_with_outputs(
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\input{restoration/scope-SRC-03022-03037}"
            r"\input{restoration/scope-SRC-03038-03104}"
            r"\input{restoration/scope-SRC-03105-03165}"
            r"\input{restoration/scope-SRC-03166-03239}"
            r"\input{restoration/scope-SRC-03240-03428}"
            r"\input{restoration/scope-SRC-03429-03518}"
            r"\input{restoration/scope-SRC-03519-03680}"
            r"\input{restoration/scope-SRC-03681-03728}"
            r"\input{restoration/scope-SRC-03729-03907}"
            r"\input{restoration/scope-SRC-03908-03926}"
            r"\input{restoration/scope-SRC-03927-04061}"
            r"\input{restoration/scope-SRC-04062-04108}"
            r"\input{restoration/scope-SRC-04109-04213}"
            r"\input{restoration/scope-SRC-04214-04234}"
            r"\input{restoration/scope-SRC-04235-04305}"
            r"\ifnum\value{hbitem}=17\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 23)
        for title in (
            "First-order derivability",
            "Soundness of first-order natural deduction",
            "Soundness of the first-order sequent calculus",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:fol-deduction",
            "sec:fol-deduction-01",
            "lem:reduct-invariance",
            "sec:fol-deduction-02",
            "sec:fol-deduction-03",
            "thm:fol-soundness",
            "thm:fol-lk-soundness",
            "sec:fol-deduction-04",
            "sec:fol-deduction-05",
            "ex:fol-deduction-01",
            "ex:fol-deduction-02",
            "ex:fol-deduction-03",
            "ex:fol-deduction-04",
            "ex:fol-deduction-05",
            "ex:fol-deduction-06",
            "ex:fol-deduction-07",
            "ex:fol-deduction-08",
            "ex:fol-deduction-09",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

    def test_exact_first_order_completeness_compiles_with_source_surface(self) -> None:
        completed, build = self.compile_with_outputs(
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\input{restoration/scope-SRC-04306-04575}"
            r"\input{restoration/scope-SRC-04576-04712}"
            r"\input{restoration/scope-SRC-04713-04920}"
            r"\input{restoration/scope-SRC-04921-04967}"
            r"\ifnum\value{hbitem}=18\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 6)
        for title in (
            "First-order consistency",
            "Term structure",
            "Strong completeness of classical first-order logic",
            "First-order compactness",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
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
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

    def test_exact_cardinality_normal_forms_and_resolution_compiles_with_source_surface(self) -> None:
        completed, build = self.compile_with_outputs(
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\input{restoration/scope-SRC-04968-05042}"
            r"\input{restoration/scope-SRC-05043-05131}"
            r"\input{restoration/scope-SRC-05132-05567}"
            r"\input{restoration/scope-SRC-05568-05923}"
            r"\input{restoration/scope-SRC-05924-05959}"
            r"\input{restoration/scope-SRC-05960-06048}"
            r"\ifnum\value{hbitem}=39\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 22)
        for title in (
            "Substructure",
            "Tarski--Vaught test",
            "First-order literal and negation normal form",
            "First-order unification procedure",
            "Refutational completeness of first-order resolution",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        labels = {
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
        }
        self.assertEqual(len(labels), 29)
        for label in labels:
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

    def test_governed_source_part_is_subordinate_and_scope_does_not_leak(self) -> None:
        completed = self.compile(
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\ifnum\value{part}=1\else\PackageError{fixture}{public part count}{}\fi"
            r"\input{restoration/scope-SRC-01649-01660}"
            r"\ifnum\value{part}=1\else\PackageError{fixture}{source part stepped counter}{}\fi"
            r"\part{After the governed scope}"
            r"\ifnum\value{part}=2\else\PackageError{fixture}{part meaning leaked}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_governed_source_label_toc_bookmark_anchor_and_attribution(self) -> None:
        from pypdf import PdfReader

        completed, build = self.compile_with_outputs(
            r"\tableofcontents"
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\input{restoration/scope-SRC-01649-01660}",
            runs=3,
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        toc = (build / "fixture.toc").read_text(encoding="utf-8")
        self.assertEqual(aux.count(r"\newlabel{part:classical-propositional}"), 1)
        self.assertRegex(
            aux,
            r"\\newlabel\{part:classical-propositional\}"
            r"\{\{Classical Propositional Logic\}\{\d+\}"
            r"\{Classical Propositional Logic\}\{section\*\.\d+\}\{\}\}",
        )
        self.assertEqual(
            toc.count(r"\contentsline {chapter}{Classical Propositional Logic}"), 1
        )

        reader = PdfReader(build / "fixture.pdf")
        outline_titles: list[str] = []

        def collect(items: list[object]) -> None:
            for item in items:
                if isinstance(item, list):
                    collect(item)
                else:
                    title = getattr(item, "title", None)
                    if isinstance(title, str):
                        outline_titles.append(title)

        collect(reader.outline)
        self.assertEqual(outline_titles.count("Classical Propositional Logic"), 1)
        pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        normalized_pdf_text = re.sub(r"\s+", " ", pdf_text)
        # One body heading plus its one requested TOC entry.
        self.assertEqual(normalized_pdf_text.count("Classical Propositional Logic"), 2)
        self.assertEqual(
            normalized_pdf_text.count(
                "Inherited source: Formal Logic, Version 1.0, source line 1649."
            ),
            1,
        )

    def test_governed_source_part_errors_on_missing_second_wrong_and_starred_calls(self) -> None:
        cases = (
            ("missing", r""),
            ("second", r"\part{Classical Propositional Logic}\part{Classical Propositional Logic}"),
            ("wrong", r"\part{Wrong title}"),
            ("starred", r"\part*{Classical Propositional Logic}"),
        )
        for name, body in cases:
            with self.subTest(name=name):
                completed = self.compile(
                    r"\begin{inheritedrestorationscope}{SRC-01649-01660}"
                    + body
                    + r"\end{inheritedrestorationscope}"
                )
                output = completed.stdout + completed.stderr
                self.assertNotEqual(completed.returncode, 0, output)
                self.assertIn("governed source part", output)

    def test_first_order_governed_part_is_subordinate_and_scope_does_not_leak(self) -> None:
        completed = self.compile(
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\ifnum\value{part}=1\else\PackageError{fixture}{public part count}{}\fi"
            r"\input{restoration/scope-SRC-03022-03037}"
            r"\ifnum\value{part}=1\else\PackageError{fixture}{source part stepped counter}{}\fi"
            r"\part{After the governed scope}"
            r"\ifnum\value{part}=2\else\PackageError{fixture}{part meaning leaked}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_first_order_governed_label_toc_bookmark_anchor_and_attribution(self) -> None:
        from pypdf import PdfReader

        completed, build = self.compile_with_outputs(
            r"\tableofcontents"
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\input{restoration/scope-SRC-03022-03037}",
            runs=3,
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        toc = (build / "fixture.toc").read_text(encoding="utf-8")
        self.assertEqual(aux.count(r"\newlabel{part:classical-first-order}"), 1)
        self.assertRegex(
            aux,
            r"\\newlabel\{part:classical-first-order\}"
            r"\{\{Classical First-Order Logic\}\{\d+\}"
            r"\{Classical First-Order Logic\}\{section\*\.\d+\}\{\}\}",
        )
        self.assertEqual(
            toc.count(r"\contentsline {chapter}{Classical First-Order Logic}"), 1
        )

        reader = PdfReader(build / "fixture.pdf")
        outline_titles: list[str] = []

        def collect(items: list[object]) -> None:
            for item in items:
                if isinstance(item, list):
                    collect(item)
                else:
                    title = getattr(item, "title", None)
                    if isinstance(title, str):
                        outline_titles.append(title)

        collect(reader.outline)
        self.assertEqual(outline_titles.count("Classical First-Order Logic"), 1)
        pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        normalized_pdf_text = re.sub(r"\s+", " ", pdf_text)
        self.assertEqual(normalized_pdf_text.count("Classical First-Order Logic"), 2)
        self.assertEqual(
            normalized_pdf_text.count(
                "Inherited source: Formal Logic, Version 1.0, source line 3022."
            ),
            1,
        )

    def test_first_order_governed_part_errors_on_missing_second_wrong_and_starred_calls(self) -> None:
        cases = (
            ("missing", r""),
            ("second", r"\part{Classical First-Order Logic}\part{Classical First-Order Logic}"),
            ("wrong", r"\part{Wrong title}"),
            ("starred", r"\part*{Classical First-Order Logic}"),
        )
        for name, body in cases:
            with self.subTest(name=name):
                completed = self.compile(
                    r"\begin{inheritedrestorationscope}{SRC-03022-03037}"
                    + body
                    + r"\end{inheritedrestorationscope}"
                )
                output = completed.stdout + completed.stderr
                self.assertNotEqual(completed.returncode, 0, output)
                self.assertIn("governed source part", output)

    def test_exact_universal_computation_chapter_compiles_with_source_surface(self) -> None:
        from pypdf import PdfReader

        wrappers = (
            "07494-07505",
            "07506-07677",
            "07678-07752",
            "07753-07843",
            "07844-07850",
            "07851-08048",
            "08049-08080",
            "08081-08143",
            "08144-08186",
            "08187-08238",
            "08239-08247",
        )
        body = r"\part{Computability and Complexity}\label{part:p04-fixture}"
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}"
            for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=16\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 18)
        for title in (
            "Adequacy of the numbering: enumeration theorem",
            "Universal computation",
            "Parameter theorem",
            "Many-one reduction",
            "Undecidability of the self-application domain set",
            "Kleene recursion theorem",
            "Rice",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:universal-reductions",
            "sec:universal-reductions-01",
            "lem:renaming-invariance",
            "thm:enumeration",
            "thm:universal-computation",
            "thm:parameter",
            "sec:universal-reductions-02",
            "sec:universal-reductions-03",
            "thm:halting-undecidable",
            "sec:universal-reductions-04",
            "thm:recursion-theorem",
            "sec:universal-reductions-05",
            "thm:rice",
            "ex:universal-reductions-01",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

        reader = PdfReader(build / "fixture.pdf")
        pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        normalized_pdf_text = re.sub(r"\s+", " ", pdf_text)
        self.assertEqual(normalized_pdf_text.count("Proof sketch."), 4)

    def test_exact_decision_hierarchy_chapter_compiles_with_source_surface(self) -> None:
        from pypdf import PdfReader

        wrappers = (
            "07494-07505",
            "07506-07677",
            "07678-07752",
            "07753-07843",
            "07844-07850",
            "07851-08048",
            "08049-08080",
            "08081-08143",
            "08144-08186",
            "08187-08238",
            "08239-08247",
            "08248-08305",
            "08306-08438",
            "08439-08709",
            "08710-08876",
            "08877-08897",
            "08898-09079",
        )
        body = r"\part{Computability and Complexity}\label{part:p04-fixture}"
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}"
            for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=28\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 33)
        for title in (
            "Negative solution to the classical Entscheidungsproblem",
            "Language and standard structure of arithmetic",
            "Prefix normal form",
            "History coding",
            "Bounded verification of computations",
            "Turing jump",
            "Jump theorem",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:decision-hierarchy",
            "sec:decision-hierarchy-01",
            "thm:fol-validity-undecidable",
            "sec:decision-hierarchy-02",
            "def:language-arithmetic",
            "lem:pairing-graph",
            "lem:goedel-beta",
            "lem:pair-contraction",
            "lem:bounded-collection",
            "thm:prefix-normal-form",
            "def:history-coding",
            "thm:bounded-verification",
            "ex:decision-hierarchy-01",
            "ex:decision-hierarchy-02",
            "ex:decision-hierarchy-03",
            "sec:decision-hierarchy-03",
            "def:turing-jump",
            "lem:relativized-adequacy",
            "thm:jump",
            "rem:jump-convention",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

        reader = PdfReader(build / "fixture.pdf")
        pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        normalized_pdf_text = re.sub(r"\s+", " ", pdf_text)
        self.assertEqual(normalized_pdf_text.count("Proof sketch."), 8)

    def test_computability_governed_part_is_subordinate_and_scope_does_not_leak(self) -> None:
        completed = self.compile(
            r"\part{Computability and Complexity}\label{part:p04-fixture}"
            r"\ifnum\value{part}=1\else\PackageError{fixture}{public part count}{}\fi"
            r"\input{restoration/scope-SRC-07494-07505}"
            r"\ifnum\value{part}=1\else\PackageError{fixture}{source part stepped counter}{}\fi"
            r"\part{After the governed scope}"
            r"\ifnum\value{part}=2\else\PackageError{fixture}{part meaning leaked}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_computability_governed_label_toc_bookmark_anchor_and_attribution(self) -> None:
        from pypdf import PdfReader

        completed, build = self.compile_with_outputs(
            r"\tableofcontents"
            r"\part{Computability and Complexity}\label{part:p04-fixture}"
            r"\input{restoration/scope-SRC-07494-07505}",
            runs=3,
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        toc = (build / "fixture.toc").read_text(encoding="utf-8")
        self.assertEqual(aux.count(r"\newlabel{part:computability}"), 1)
        self.assertRegex(
            aux,
            r"\\newlabel\{part:computability\}"
            r"\{\{Computability\}\{\d+\}"
            r"\{Computability\}\{section\*\.\d+\}\{\}\}",
        )
        self.assertEqual(toc.count(r"\contentsline {chapter}{Computability}"), 1)

        reader = PdfReader(build / "fixture.pdf")
        outline_titles: list[str] = []

        def collect(items: list[object]) -> None:
            for item in items:
                if isinstance(item, list):
                    collect(item)
                else:
                    title = getattr(item, "title", None)
                    if isinstance(title, str):
                        outline_titles.append(title)

        collect(reader.outline)
        self.assertEqual(outline_titles.count("Computability"), 1)
        pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        normalized_pdf_text = re.sub(r"\s+", " ", pdf_text)
        # The public Part IV title contributes the same word once in the body
        # and once in the TOC; the governed source heading contributes the
        # other body/TOC pair.
        self.assertEqual(
            normalized_pdf_text.count("Computability and Complexity"), 2
        )
        self.assertEqual(normalized_pdf_text.count("Computability"), 4)
        self.assertEqual(
            normalized_pdf_text.count(
                "Inherited source: Formal Logic, Version 1.0, source line 7494."
            ),
            1,
        )

    def test_computability_governed_part_errors_on_missing_second_wrong_and_starred_calls(self) -> None:
        cases = (
            ("missing", r""),
            ("second", r"\part{Computability}\part{Computability}"),
            ("wrong", r"\part{Wrong title}"),
            ("starred", r"\part*{Computability}"),
        )
        for name, body in cases:
            with self.subTest(name=name):
                completed = self.compile(
                    r"\begin{inheritedrestorationscope}{SRC-07494-07505}"
                    + body
                    + r"\end{inheritedrestorationscope}"
                )
                output = completed.stdout + completed.stderr
                self.assertNotEqual(completed.returncode, 0, output)
                self.assertIn("governed source part", output)

    def test_part5_governed_source_part_advances_once_and_scope_does_not_leak(self) -> None:
        completed = self.compile(
            r"\setcounter{part}{4}"
            r"\input{restoration/scope-SRC-09080-09098}"
            r"\ifnum\value{part}=5\else\PackageError{fixture}{public part count}{}\fi"
            r"\part{After the governed scope}"
            r"\ifnum\value{part}=6\else\PackageError{fixture}{part meaning leaked}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_complete_exact_part5_run_compiles_with_source_surface(self) -> None:
        from pypdf import PdfReader

        wrappers = (
            "09080-09098",
            "09099-09111",
            "09112-09149",
            "09150-09174",
            "09175-09187",
            "09188-09261",
            "09262-09327",
            "09328-09438",
            "09439-09497",
            "09498-09538",
            "09539-09619",
            "09620-09728",
            "09729-09749",
            "09750-09816",
            "09817-09876",
            "09877-09924",
            "09925-09992",
            "09993-10027",
            "10028-10059",
        )
        body = r"\setcounter{part}{4}"
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}" for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=15\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)

        index = (build / "fixture.idx").read_text(encoding="utf-8")
        self.assertEqual(index.count(r"\indexentry"), 23)
        for title in (
            "Robinson arithmetic",
            "Peano arithmetic",
            "Compactness produces nonstandard models",
            "Representability theorem",
            "Proof and provability predicates",
            "Diagonal lemma",
            "first incompleteness theorem, original form",
            "Rosser",
            r'L\"ob',
            "second incompleteness theorem",
            "Tarski undefinability",
        ):
            self.assertIn(title, index)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        labels = (
            "part:incompleteness",
            "ch:arithmetic-coding",
            "sec:arithmetic-coding-01",
            "lem:q-bounded-cases",
            "lem:q-dichotomy",
            "sec:arithmetic-coding-02",
            "sec:nonstandard-arithmetic",
            "def:nonstandard-model",
            "thm:nonstandard-model",
            "ex:arithmetic-coding-01",
            "ex:nonstandard-true-arithmetic",
            "sec:arithmetic-coding-03",
            "thm:representability",
            "sec:arithmetic-coding-04",
            "def:fixed-proof-predicate",
            "ex:arithmetic-coding-02",
            "ex:arithmetic-coding-03",
            "ch:first-incompleteness",
            "sec:first-incompleteness-01",
            "thm:diagonal-lemma",
            "sec:first-incompleteness-02",
            "sec:first-incompleteness-03",
            "thm:godel-first",
            "sec:first-incompleteness-04",
            "thm:rosser",
            "ex:first-incompleteness-01",
            "ex:first-incompleteness-02",
            "ex:first-incompleteness-03",
            "ch:second-incompleteness",
            "sec:second-incompleteness-01",
            "def:formal-consistency-sentence",
            "sec:second-incompleteness-02",
            "thm:lob",
            "sec:second-incompleteness-03",
            "thm:godel-second",
            "sec:second-incompleteness-04",
            "thm:tarski-undefinability",
            "sec:second-incompleteness-05",
            "ex:second-incompleteness-01",
            "ex:second-incompleteness-02",
            "ex:second-incompleteness-03",
            "ex:second-incompleteness-04",
        )
        for label in labels:
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1)

        reader = PdfReader(build / "fixture.pdf")
        pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        normalized_pdf_text = re.sub(r"\s+", " ", pdf_text)
        self.assertEqual(normalized_pdf_text.count("Proof sketch."), 4)

    def test_exact_part6_through_cumulative_hierarchy_compiles_with_source_surface(self) -> None:
        wrappers = (
            "10060-10088",
            "10089-10271",
            "10272-10352",
            "10353-10451",
            "10452-10520",
            "10521-10558",
            "10559-10674",
        )
        body = (
            r"\crefalias{hbitem}{section}"
            r"\refstepcounter{hbitem}\label{sec:set-prerequisites-06}"
            r"\crefalias{hbitem}{chapter}"
            r"\refstepcounter{hbitem}\label{ch:strings}"
            r"\crefalias{hbitem}{definition}"
            r"\refstepcounter{hbitem}\label{def:transitive-set}"
            r"\refstepcounter{hbitem}\label{def:ordinal-cardinal}"
            r"\setcounter{hbitem}{0}"
            r"\setcounter{part}{5}"
        )
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}" for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=18\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "part:set-theory",
            "ch:zf-zfc",
            "ch:cumulative-hierarchy",
            "sec:cumulative-hierarchy-01",
            "sec:cumulative-hierarchy-02",
            "sec:cumulative-hierarchy-03",
            "sec:cumulative-hierarchy-04",
            "ex:cumulative-hierarchy-01",
            "ex:cumulative-hierarchy-02",
            "ex:cumulative-hierarchy-03",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)

        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)
        self.assert_references_defined_in_handbook(log)

    def test_exact_constructibility_forcing_chapter_compiles_with_source_surface(self) -> None:
        wrappers = (
            "10675-10769", "10770-10825", "10826-10881", "10882-10899",
            "10900-10988", "10989-11011", "11012-11052", "11053-11103",
            "11104-11126", "11127-11199", "11200-11239", "11240-11279",
            "11280-11293", "11294-11314", "11315-11337", "11338-11353",
        )
        body = (
            r"\crefalias{hbitem}{definition}"
            r"\refstepcounter{hbitem}\label{def:formal-consistency-sentence}"
            r"\crefalias{hbitem}{theorem}"
            r"\refstepcounter{hbitem}\label{thm:fol-soundness}"
            r"\refstepcounter{hbitem}\label{thm:fol-completeness}"
            r"\refstepcounter{hbitem}\label{thm:godel-second}"
            r"\setcounter{hbitem}{0}"
            r"\setcounter{chapter}{36}"
        )
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}" for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=19\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:constructibility-forcing",
            "sec:constructibility-forcing-01",
            "sec:constructibility-forcing-02",
            "sec:constructibility-forcing-03",
            "lem:relativization-derivations",
            "thm:ch-relative-consistency",
            "thm:ch-nonderivability",
            "ex:constructibility-forcing-01",
            "ex:constructibility-forcing-02",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)

        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)
        self.assert_references_defined_in_handbook(log)

    def test_part5_governed_label_toc_bookmark_and_public_title(self) -> None:
        from pypdf import PdfReader

        completed, build = self.compile_with_outputs(
            r"\tableofcontents"
            r"\setcounter{part}{4}"
            r"\input{restoration/scope-SRC-09080-09098}",
            runs=3,
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        toc = (build / "fixture.toc").read_text(encoding="utf-8")
        self.assertEqual(aux.count(r"\newlabel{part:incompleteness}"), 1)
        self.assertRegex(
            aux,
            r"\\newlabel\{part:incompleteness\}"
            r"\{\{V\}\{\d+\}"
            r"\{Arithmetic and Incompleteness\}\{part\.5\}\{\}\}",
        )
        self.assertEqual(toc.count("Arithmetic and Incompleteness"), 1)
        self.assertNotIn("Formal Arithmetic and Incompleteness", toc)

        reader = PdfReader(build / "fixture.pdf")
        outline_titles: list[str] = []

        def collect(items: list[object]) -> None:
            for item in items:
                if isinstance(item, list):
                    collect(item)
                else:
                    title = getattr(item, "title", None)
                    if isinstance(title, str):
                        outline_titles.append(title)

        collect(reader.outline)
        self.assertEqual(outline_titles.count("V Arithmetic and Incompleteness"), 1)
        self.assertFalse(
            any("Formal Arithmetic and Incompleteness" in title for title in outline_titles)
        )
        pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        normalized_pdf_text = re.sub(r"\s+", " ", pdf_text)
        self.assertEqual(normalized_pdf_text.count("Arithmetic and Incompleteness"), 2)
        self.assertNotIn("Formal Arithmetic and Incompleteness", normalized_pdf_text)

    def test_part5_governed_part_errors_on_missing_second_wrong_and_starred_calls(self) -> None:
        cases = (
            ("missing", r""),
            (
                "second",
                r"\part{Formal Arithmetic and Incompleteness}"
                r"\part{Formal Arithmetic and Incompleteness}",
            ),
            ("wrong", r"\part{Wrong title}"),
            ("starred", r"\part*{Formal Arithmetic and Incompleteness}"),
        )
        for name, body in cases:
            with self.subTest(name=name):
                completed = self.compile(
                    r"\begin{inheritedrestorationscope}{SRC-09080-09098}"
                    + body
                    + r"\end{inheritedrestorationscope}"
                )
                output = completed.stdout + completed.stderr
                self.assertNotEqual(completed.returncode, 0, output)
                self.assertIn("governed source part", output)

    def test_part8_governed_source_part_advances_once_and_scope_does_not_leak(self) -> None:
        completed = self.compile(
            r"\setcounter{part}{7}"
            r"\input{restoration/scope-SRC-12970-12988}"
            r"\ifnum\value{part}=8\else\PackageError{fixture}{public part count}{}\fi"
            r"\part{After the governed scope}"
            r"\ifnum\value{part}=9\else\PackageError{fixture}{part meaning leaked}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_exact_intuitionistic_chapter_compiles_with_source_surface(self) -> None:
        wrappers = (
            "12970-12988", "12989-13045", "13046-13057",
            "13058-13099", "13100-13127", "13128-13140",
            "13141-13157", "13158-13179", "13180-13200",
        )
        body = (
            r"\crefalias{hbitem}{chapter}"
            r"\refstepcounter{hbitem}\label{ch:lk-lj}"
            r"\refstepcounter{hbitem}\label{ch:cut-elimination}"
            r"\crefalias{hbitem}{section}"
            r"\refstepcounter{hbitem}\label{sec:fol-syntax-semantics-02}"
            r"\refstepcounter{hbitem}\label{sec:lk-lj-02}"
            r"\crefalias{hbitem}{theorem}"
            r"\refstepcounter{hbitem}\label{thm:fol-unique-readability}"
            r"\setcounter{hbitem}{0}"
            r"\setcounter{part}{7}"
        )
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}" for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=13\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "part:nonclassical", "ch:intuitionistic-logic",
            "sec:intuitionistic-logic-01", "ex:intuitionistic-logic-01",
            "ex:intuitionistic-logic-02", "sec:intuitionistic-classical",
            "thm:glivenko", "thm:negative-translation",
            "thm:disjunction-property",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)
        self.assert_references_defined_in_handbook(log)

        from pypdf import PdfReader

        text = "\n".join(
            page.extract_text() or "" for page in PdfReader(build / "fixture.pdf").pages
        )
        self.assertEqual(re.sub(r"\s+", " ", text).count("Proof sketch."), 1)

    def test_exact_modal_temporal_epistemic_chapter_compiles_with_source_surface(self) -> None:
        wrappers = (
            "13201-13213", "13214-13254", "13255-13284",
            "13285-13316", "13317-13339", "13340-13409",
            "13410-13439", "13440-13471", "13472-13478",
            "13479-13518", "13519-13551", "13552-13564",
            "13565-13583",
        )
        body = r"\setcounter{hbitem}{0}"
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}" for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=13\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:modal-temporal-epistemic",
            "sec:modal-temporal-epistemic-01",
            "sec:modal-temporal-epistemic-02",
            "sec:modal-temporal-epistemic-03",
            "ex:modal-temporal-epistemic-01",
            "ex:modal-temporal-epistemic-02",
            "ex:modal-temporal-epistemic-03",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)
        self.assert_references_defined_in_handbook(log)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("Modal, Temporal, and Epistemic Logic", text)
        self.assertIn("Eventuality is not recurrence", text)
        self.assertIn("Truth without knowledge", text)

    def test_exact_many_valued_relevance_linear_chapters_compile_with_source_surface(self) -> None:
        wrappers = (
            "13584-13613", "13614-13640", "13641-13699",
            "13700-13730", "13731-13774", "13775-13788",
            "13789-13806", "13807-13861", "13862-13896",
            "13897-13918", "13919-13938", "13939-13971",
            "13972-14000", "14001-14015", "14016-14034",
            "14035-14051", "14052-14068", "14069-14094",
        )
        body = r"\setcounter{hbitem}{0}"
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}" for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=10\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:many-valued-paraconsistent",
            "sec:many-valued-paraconsistent-01",
            "sec:many-valued-paraconsistent-02",
            "sec:many-valued-paraconsistent-03",
            "sec:many-valued-paraconsistent-04",
            "ex:many-valued-paraconsistent-01",
            "ex:many-valued-paraconsistent-02",
            "ch:relevance-linear", "sec:relevance-linear-01",
            "sec:relevance-linear-02", "sec:relevance-linear-03",
            "sec:relevance-linear-04", "ex:relevance-linear-01",
            "ex:relevance-linear-02", "ex:relevance-linear-03",
            "ex:relevance-linear-04",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)
        self.assert_references_defined_in_handbook(log)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("Many-Valued and Paraconsistent Logic", text)
        self.assertIn("Relevance, Substructural Systems, and Linear Logic", text)
        self.assertIn("Soundness, completeness, and cut elimination", text)

    def test_formal_practice_source_part_is_subordinate_and_scope_does_not_leak(self) -> None:
        completed = self.compile(
            r"\setcounter{part}{11}"
            r"\part{Automation, Mechanization, and Formal Practice}"
            r"\label{part:p12-fixture}"
            r"\ifnum\value{part}=12\else\PackageError{fixture}{public part count}{}\fi"
            r"\input{restoration/scope-SRC-14095-14146}"
            r"\ifnum\value{part}=12\else\PackageError{fixture}{source part stepped counter}{}\fi"
            r"\part{After the governed scope}"
            r"\ifnum\value{part}=13\else\PackageError{fixture}{part meaning leaked}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_formal_practice_source_part_errors_on_missing_second_wrong_and_starred_calls(self) -> None:
        cases = (
            ("missing", r""),
            (
                "second",
                r"\part{Formal Practice, Automation, and Verification}"
                r"\part{Formal Practice, Automation, and Verification}",
            ),
            ("wrong", r"\part{Wrong title}"),
            ("starred", r"\part*{Formal Practice, Automation, and Verification}"),
        )
        for name, body in cases:
            with self.subTest(name=name):
                completed = self.compile(
                    r"\begin{inheritedrestorationscope}{SRC-14095-14146}"
                    + body
                    + r"\end{inheritedrestorationscope}"
                )
                output = completed.stdout + completed.stderr
                if "Windows API error 5: Access is denied" in output:
                    self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
                self.assertNotEqual(completed.returncode, 0, output)
                self.assertIn("governed source part", output)

    def test_exact_formal_practice_chapter_compiles_with_source_surface(self) -> None:
        wrappers = (
            "14095-14146", "14147-14169", "14170-14202",
            "14203-14230", "14231-14270",
        )
        body = (
            r"\setcounter{part}{11}"
            r"\part{Automation, Mechanization, and Formal Practice}"
            r"\label{part:p12-fixture}"
            r"\setcounter{hbitem}{0}"
        )
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}" for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=9\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)
        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:formal-practice", "sec:formal-practice-01",
            "sec:formal-practice-02", "sec:formal-practice-03",
            "sec:formal-practice-04", "sec:formal-practice-05",
            "ex:formal-practice-01", "ex:formal-practice-02",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        self.assertNotIn(r"\newlabel{part:formal-practice}", aux)
        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)
        self.assert_references_defined_in_handbook(log)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("Formal Practice, Automation, and Verification", text)
        self.assertIn("Constructing Derivations, Models, and Countermodels", text)
        self.assertIn("Failure analysis", text)

    def test_exact_automated_reasoning_chapter_and_blank_lines_compile(self) -> None:
        provenance_ids = (
            "SRC-14271-14350",
            "SRC-14351-14400",
            "SRC-14401-14434",
            "SRC-14435-14479",
            "SRC-14480-14495",
            "SRC-14496-14521",
            "SRC-14522-14560",
            "SEP-14561-14561",
            "SRC-14562-14589",
            "SEP-14590-14590",
        )
        body = r"\setcounter{hbitem}{0}" + "".join(
            rf"\input{{restoration/scope-{provenance_id}}}"
            for provenance_id in provenance_ids
        )
        body += (
            r"\ifnum\value{hbitem}=13\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)
        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:automated-reasoning",
            *(f"sec:automated-reasoning-{number:02d}" for number in range(1, 8)),
            *(f"ex:automated-reasoning-{number:02d}" for number in range(1, 4)),
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("Automated Reasoning", text)
        self.assertIn("DPLL(S, valuation, V):", text)
        self.assertIn("Automated-result audit", text)

    def test_automated_reasoning_commands_are_exactly_scoped(self) -> None:
        inside = self.compile(
            r"\makeatletter"
            r"\newcommand\expectedsat{\mathsf{SAT}}"
            r"\newcommand\expectedunsat{\mathsf{UNSAT}}"
            r"\newcommand\expectednp{\mathsf{NP}}"
            r"\begin{inheritedrestorationscope}{SRC-14271-14350}"
            r"\ifx\SAT\expectedsat\else\PackageError{fixture}{SAT differed}{}\fi"
            r"\ifx\UNSAT\expectedunsat\else\PackageError{fixture}{UNSAT differed}{}\fi"
            r"\ifx\NP\expectednp\else\PackageError{fixture}{NP differed}{}\fi"
            r"$\SAT\;\UNSAT\;\NP$."
            r"\end{inheritedrestorationscope}"
            r"\makeatother"
        )
        output = inside.stdout + inside.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(inside.returncode, 0, output)

        for command, needle in (
            (r"\SAT", "source SAT command outside"),
            (r"\UNSAT", "source UNSAT command outside"),
            (r"\NP", "source NP command outside"),
        ):
            with self.subTest(command=command):
                outside = self.compile(rf"Editorial ${command}$.")
                outside_output = outside.stdout + outside.stderr
                self.assertNotEqual(outside.returncode, 0, outside_output)
                self.assertIn(needle, outside_output)

    def test_exact_mechanized_proof_checking_chapter_compiles(self) -> None:
        wrappers = (
            "14591-14628",
            "14629-14660",
            "14661-14690",
            "14691-14728",
        )
        body = r"\setcounter{hbitem}{0}" + "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}"
            for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=10\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)
        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:mechanization",
            *(f"sec:mechanization-{number:02d}" for number in range(1, 5)),
            "ex:mechanization-01",
            "ex:mechanization-02",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("Mechanized Proof Checking", text)
        self.assertIn("Kernel, elaboration, and automation", text)
        self.assertIn("Mechanized-result report", text)

    def test_exact_writing_and_typesetting_chapter_compiles(self) -> None:
        wrappers = (
            "14729-14778",
            "14779-14814",
            "14815-14850",
            "14851-14870",
            "14871-14931",
            "14932-14945",
            "14946-14975",
            "14976-14990",
            "14991-15029",
        )
        body = r"\setcounter{hbitem}{0}" + "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}"
            for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=4\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)
        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:latex-style",
            "sec:latex-style-01",
            "sec:latex-style-02",
            "sec:latex-style-before-after",
            "sec:latex-style-03",
            "sec:latex-style-source-render",
            "sec:latex-style-04",
            "sec:latex-style-rule-correction",
            "sec:latex-style-05",
            "sec:latex-style-06",
            "ex:latex-style-01",
            "ex:latex-style-02",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        self.assertNotIn(r"\newlabel{thm:sample-semantic-implication}", aux)
        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("Writing and Typesetting Formal Logic", text)
        self.assertIn("Semantic macros for logic", text)
        self.assertIn("Worked correction of an invalid rule appli", text)

    def test_exact_research_workflow_chapter_compiles(self) -> None:
        wrappers = (
            "SRC-15030-15050",
            "SRC-15051-15068",
            "SRC-15069-15077",
            "SRC-15078-15091",
            "SEP-15092-15092",
        )
        body = r"\setcounter{hbitem}{0}" + "".join(
            rf"\input{{restoration/scope-{wrapper}}}"
            for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=1\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)
        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:research-workflow",
            "sec:research-workflow-01",
            "sec:research-workflow-02",
            "sec:research-workflow-03",
            "sec:research-workflow-04",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("Research Workflow and Reproducibility", text)
        self.assertIn("Counterexample-first testing", text)
        self.assertIn("Nofiniteauditestablishes", re.sub(r"\s+", "", text))

    def test_registered_notation_is_local_appendix_a_and_counter_restores(self) -> None:
        body = (
            r"\tableofcontents"
            r"\setcounter{chapter}{66}"
            r"\input{restoration/scope-SRC-15093-15206}"
            r"\ifnum\value{chapter}=66\else"
            r"\PackageError{fixture}{public chapter counter leaked}{}\fi"
            r"\chapter{Post Appendix Control}\label{ch:post-appendix-control}"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)
        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        toc = (build / "fixture.toc").read_text(encoding="utf-8")
        for label in (
            "ch:registered-notation",
            "app:notation",
            "sec:registered-notation-01",
            "sec:registered-notation-02",
            "ch:post-appendix-control",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        self.assertRegex(
            aux,
            r"\\newlabel\{ch:registered-notation\}\{\{A\}\{\d+\}",
        )
        self.assertRegex(
            aux,
            r"\\newlabel\{ch:post-appendix-control\}\{\{67\}\{\d+\}",
        )
        self.assertIn(r"\numberline {A}Registered Notation", toc)
        self.assertIn(r"\numberline {67}Post Appendix Control", toc)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("Appendix A Registered Notation", text)
        self.assertIn("Chapter 67 Post Appendix Control", text)

    def test_registered_notation_layout_rejects_missing_and_repeated_appendix(self) -> None:
        cases = (
            (
                "missing",
                r"\begin{inheritedrestorationscope}{SRC-15093-15206}"
                r"\chapter{Registered Notation}"
                r"\end{inheritedrestorationscope}",
                "governed source appendix call is missing",
            ),
            (
                "repeated",
                r"\begin{inheritedrestorationscope}{SRC-15093-15206}"
                r"\appendix\appendix\chapter{Registered Notation}"
                r"\end{inheritedrestorationscope}",
                "governed source appendix call occurred more than once",
            ),
            (
                "appendix-b-transition",
                r"\begin{inheritedrestorationscope}{SRC-15207-15239}"
                r"\appendix\chapter{Binding and Precedence}"
                r"\end{inheritedrestorationscope}",
                "governed Appendix B repeats the source appendix",
            ),
            (
                "appendix-c-transition",
                r"\begin{inheritedrestorationscope}{SRC-15240-15488}"
                r"\appendix\chapter{Rule Sheets}"
                r"\end{inheritedrestorationscope}",
                "governed Appendix C repeats the source appendix",
            ),
            (
                "appendix-d-transition",
                r"\begin{inheritedrestorationscope}{SRC-15489-15619}"
                r"\appendix\chapter{Qualifying Problems}"
                r"\end{inheritedrestorationscope}",
                "governed Appendix D repeats the source appendix",
            ),
            (
                "appendix-d6-transition",
                r"\begin{inheritedrestorationscope}{SRC-15620-15637}"
                r"\appendix\section{Additional problems}"
                r"\end{inheritedrestorationscope}",
                "governed Appendix D.6 repeats the source appendix",
            ),
            (
                "appendix-e-transition",
                r"\begin{inheritedrestorationscope}{SRC-15638-16742}"
                r"\appendix\chapter{Exercise Feedback}"
                r"\end{inheritedrestorationscope}",
                "governed Appendix E repeats the source appendix",
            ),
        )
        for name, body, expected in cases:
            with self.subTest(name=name):
                completed = self.compile(body)
                output = completed.stdout + completed.stderr
                if "Windows API error 5: Access is denied" in output:
                    self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
                self.assertNotEqual(completed.returncode, 0, output)
                self.assertIn(expected, output)

    def test_binding_precedence_is_local_appendix_b_and_counter_restores(self) -> None:
        body = (
            r"\tableofcontents"
            r"\setcounter{chapter}{66}"
            r"\input{restoration/scope-SRC-15093-15206}"
            r"\ifnum\value{chapter}=66\else"
            r"\PackageError{fixture}{counter leaked after Appendix A}{}\fi"
            r"\input{restoration/scope-SRC-15207-15239}"
            r"\ifnum\value{chapter}=66\else"
            r"\PackageError{fixture}{counter leaked after Appendix B}{}\fi"
            r"\chapter{Post Appendix Control}\label{ch:post-appendix-b-control}"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)
        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        toc = (build / "fixture.toc").read_text(encoding="utf-8")
        for label in (
            "ch:registered-notation",
            "app:notation",
            "ch:binding-precedence",
            "app:precedence",
            "ch:post-appendix-b-control",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        self.assertRegex(
            aux,
            r"\\newlabel\{ch:binding-precedence\}\{\{B\}\{\d+\}",
        )
        self.assertRegex(
            aux,
            r"\\newlabel\{ch:post-appendix-b-control\}\{\{67\}\{\d+\}",
        )
        self.assertIn(r"\numberline {A}Registered Notation", toc)
        self.assertIn(r"\numberline {B}Binding and Precedence", toc)
        self.assertIn(r"\numberline {67}Post Appendix Control", toc)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("Appendix B Binding and Precedence", text)
        self.assertIn("Chapter 67 Post Appendix Control", text)

    def test_rule_sheets_is_local_appendix_c_and_counter_restores(self) -> None:
        body = (
            r"\tableofcontents"
            r"\setcounter{chapter}{66}"
            r"\input{restoration/scope-SRC-15093-15206}"
            r"\ifnum\value{chapter}=66\else"
            r"\PackageError{fixture}{counter leaked after Appendix A}{}\fi"
            r"\input{restoration/scope-SRC-15207-15239}"
            r"\ifnum\value{chapter}=66\else"
            r"\PackageError{fixture}{counter leaked after Appendix B}{}\fi"
            r"\input{restoration/scope-SRC-15240-15488}"
            r"\ifnum\value{chapter}=66\else"
            r"\PackageError{fixture}{counter leaked after Appendix C}{}\fi"
            r"\chapter{Post Appendix Control}\label{ch:post-appendix-c-control}"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)
        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        toc = (build / "fixture.toc").read_text(encoding="utf-8")
        for label in (
            "ch:registered-notation",
            "app:notation",
            "ch:binding-precedence",
            "app:precedence",
            "ch:rule-sheets",
            "app:rules",
            "sec:rule-sheets-01",
            "sec:rule-sheets-02",
            "sec:rule-sheets-03",
            "ch:post-appendix-c-control",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        self.assertRegex(
            aux,
            r"\\newlabel\{ch:rule-sheets\}\{\{C\}\{\d+\}",
        )
        self.assertRegex(
            aux,
            r"\\newlabel\{ch:post-appendix-c-control\}\{\{67\}\{\d+\}",
        )
        self.assertIn(r"\numberline {A}Registered Notation", toc)
        self.assertIn(r"\numberline {B}Binding and Precedence", toc)
        self.assertIn(r"\numberline {C}Rule Sheets", toc)
        self.assertIn(r"\numberline {67}Post Appendix Control", toc)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("Appendix C Rule Sheets", text)
        self.assertIn("Classical natural deduction", text)
        self.assertIn("Classical sequent calculus", text)
        self.assertIn("Modal calculus for K", text)
        self.assertIn("Chapter 67 Post Appendix Control", text)

    def test_qualifying_problems_is_local_appendix_d_with_five_solutions(self) -> None:
        body = (
            r"\tableofcontents"
            r"\setcounter{chapter}{66}"
            r"\input{restoration/scope-SRC-15093-15206}"
            r"\input{restoration/scope-SRC-15207-15239}"
            r"\input{restoration/scope-SRC-15240-15488}"
            r"\input{restoration/scope-SRC-15489-15619}"
            r"\ifnum\value{chapter}=66\else"
            r"\PackageError{fixture}{counter leaked after Appendix D}{}\fi"
            r"\chapter{Post Appendix Control}\label{ch:post-appendix-d-control}"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)
        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        toc = (build / "fixture.toc").read_text(encoding="utf-8")
        labels = (
            "ch:qualifying-problems",
            "app:qualifying",
            "sec:qualifying-problems-01",
            "prob:substitution",
            "sec:qualifying-problems-02",
            "prob:compactness",
            "sec:qualifying-problems-03",
            "prob:incompleteness",
            "sec:qualifying-problems-04",
            "prob:modal-frame",
            "sec:qualifying-problems-05",
            "prob:cut-subformula",
            "ch:post-appendix-d-control",
        )
        for label in labels:
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        self.assertRegex(
            aux,
            r"\\newlabel\{ch:qualifying-problems\}\{\{D\}\{\d+\}",
        )
        self.assertRegex(
            aux,
            r"\\newlabel\{ch:post-appendix-d-control\}\{\{67\}\{\d+\}",
        )
        self.assertIn(
            r"\numberline {D}Qualifying-Examination Problems and Selected Solutions",
            toc,
        )
        self.assertIn(r"\numberline {67}Post Appendix Control", toc)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn(
            "Appendix D Qualifying-Examination Problems and Selected Solutions",
            text,
        )
        self.assertEqual(len(re.findall(r"\bSolution\.", text)), 5)
        self.assertIn("Chapter 67 Post Appendix Control", text)

    def test_additional_problems_continues_as_local_d6_and_restores_counters(self) -> None:
        body = (
            r"\tableofcontents"
            r"\setcounter{chapter}{66}"
            r"\setcounter{section}{4}"
            r"\input{restoration/scope-SRC-15093-15206}"
            r"\input{restoration/scope-SRC-15207-15239}"
            r"\input{restoration/scope-SRC-15240-15488}"
            r"\input{restoration/scope-SRC-15489-15619}"
            r"\input{restoration/scope-SRC-15620-15637}"
            r"\ifnum\value{chapter}=66\else"
            r"\PackageError{fixture}{chapter leaked after Appendix D.6}{}\fi"
            r"\ifnum\value{section}=4\else"
            r"\PackageError{fixture}{section leaked after Appendix D.6}{}\fi"
            r"\chapter{Post Appendix Control}\label{ch:post-appendix-d6-control}"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        toc = (build / "fixture.toc").read_text(encoding="utf-8")
        self.assertEqual(
            aux.count(r"\newlabel{sec:qualifying-problems-06}"), 1
        )
        self.assertRegex(
            aux,
            r"\\newlabel\{sec:qualifying-problems-06\}\{\{D\.6\}\{\d+\}",
        )
        self.assertRegex(
            aux,
            r"\\newlabel\{ch:post-appendix-d6-control\}\{\{67\}\{\d+\}",
        )
        self.assertIn(r"\numberline {D.6}Additional problems", toc)
        self.assertIn(r"\numberline {67}Post Appendix Control", toc)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("D.6 Additional problems", text)
        self.assertIn("Formalize one theorem in a proof assistant", text)
        self.assertIn("Chapter 67 Post Appendix Control", text)

    def test_exercise_feedback_is_local_appendix_e_and_restores_counters(self) -> None:
        body = (
            r"\tableofcontents"
            r"\setcounter{chapter}{66}"
            r"\input{restoration/scope-SRC-15093-15206}"
            r"\input{restoration/scope-SRC-15207-15239}"
            r"\input{restoration/scope-SRC-15240-15488}"
            r"\input{restoration/scope-SRC-15489-15619}"
            r"\input{restoration/scope-SRC-15620-15637}"
            r"\input{restoration/scope-SRC-15638-16742}"
            r"\ifnum\value{chapter}=66\else"
            r"\PackageError{fixture}{chapter leaked after Appendix E}{}\fi"
            r"\chapter{Post Appendix Control}\label{ch:post-appendix-e-control}"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        toc = (build / "fixture.toc").read_text(encoding="utf-8")
        for label in (
            "ch:exercise-feedback",
            "app:exercise-feedback",
            "ch:post-appendix-e-control",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)
        self.assertRegex(
            aux,
            r"\\newlabel\{ch:exercise-feedback\}\{\{E\}\{\d+\}",
        )
        self.assertRegex(
            aux,
            r"\\newlabel\{ch:post-appendix-e-control\}\{\{67\}\{\d+\}",
        )
        self.assertIn(r"\numberline {E}Exercise Feedback", toc)
        self.assertIn(
            r"\numberline {E.1}Language levels, formal objects, and proof writing",
            toc,
        )
        self.assertIn(r"\numberline {E.12}Keys for the qualifying problems", toc)
        self.assertIn(r"\numberline {67}Post Appendix Control", toc)

        from pypdf import PdfReader

        text = re.sub(
            r"\s+",
            " ",
            "\n".join(
                page.extract_text() or ""
                for page in PdfReader(build / "fixture.pdf").pages
            ),
        )
        self.assertIn("Appendix E Exercise Feedback", text)
        # The fixture also includes Appendix D's five Solution paragraphs, and
        # pypdf can merge one italic period at a page boundary.  Exact E counts
        # are byte-locked in test_exercise_feedback_source_route; this rendered
        # seam only requires every E solution class to remain visibly present.
        self.assertGreaterEqual(len(re.findall(r"\bSolution\.", text)), 89)
        self.assertEqual(len(re.findall(r"\bSolution sketch\.", text)), 22)
        self.assertIn("Keys for the qualifying problems", text)
        self.assertIn("Chapter 67 Post Appendix Control", text)

    def test_part8_governed_label_toc_bookmark_and_public_title(self) -> None:
        from pypdf import PdfReader

        completed, build = self.compile_with_outputs(
            r"\tableofcontents"
            r"\setcounter{part}{7}"
            r"\input{restoration/scope-SRC-12970-12988}",
            runs=3,
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        toc = (build / "fixture.toc").read_text(encoding="utf-8")
        self.assertEqual(aux.count(r"\newlabel{part:nonclassical}"), 1)
        self.assertRegex(
            aux,
            r"\\newlabel\{part:nonclassical\}"
            r"\{\{VIII\}\{\d+\}"
            r"\{Nonclassical Logics\}\{part\.8\}\{\}\}",
        )
        self.assertEqual(toc.count("Nonclassical Logics"), 1)
        self.assertNotIn("Nonclassical Logic}", toc)

        reader = PdfReader(build / "fixture.pdf")
        outline_titles: list[str] = []

        def collect(items: list[object]) -> None:
            for item in items:
                if isinstance(item, list):
                    collect(item)
                else:
                    title = getattr(item, "title", None)
                    if isinstance(title, str):
                        outline_titles.append(title)

        collect(reader.outline)
        self.assertEqual(outline_titles.count("VIII Nonclassical Logics"), 1)
        self.assertFalse(
            any(title == "X Nonclassical Logic" for title in outline_titles)
        )
        pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        normalized_pdf_text = re.sub(r"\s+", " ", pdf_text)
        self.assertEqual(normalized_pdf_text.count("Nonclassical Logics"), 2)
        self.assertNotIn("Nonclassical Logic ", normalized_pdf_text)

    def test_part8_governed_part_errors_on_missing_second_wrong_and_starred_calls(self) -> None:
        cases = (
            ("missing", r""),
            (
                "second",
                r"\part{Nonclassical Logic}"
                r"\part{Nonclassical Logic}",
            ),
            ("wrong", r"\part{Wrong title}"),
            ("starred", r"\part*{Nonclassical Logic}"),
        )
        for name, body in cases:
            with self.subTest(name=name):
                completed = self.compile(
                    r"\begin{inheritedrestorationscope}{SRC-12970-12988}"
                    + body
                    + r"\end{inheritedrestorationscope}"
                )
                output = completed.stdout + completed.stderr
                self.assertNotEqual(completed.returncode, 0, output)
                self.assertIn("governed source part", output)

    def test_proof_theory_governed_part_is_subordinate_and_scope_does_not_leak(self) -> None:
        completed = self.compile(
            r"\setcounter{part}{6}"
            r"\part{Proof Theory, Lambda Calculi, and Higher-Order Logic}"
            r"\label{part:p07-fixture}"
            r"\ifnum\value{part}=7\else\PackageError{fixture}{public part count}{}\fi"
            r"\input{restoration/scope-SRC-11354-11413}"
            r"\ifnum\value{part}=7\else\PackageError{fixture}{source part stepped counter}{}\fi"
            r"\part{After the governed scope}"
            r"\ifnum\value{part}=8\else\PackageError{fixture}{part meaning leaked}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_proof_theory_governed_part_errors_on_missing_second_wrong_and_starred_calls(self) -> None:
        cases = (
            ("missing", r""),
            ("second", r"\part{Proof Theory}\part{Proof Theory}"),
            ("wrong", r"\part{Wrong title}"),
            ("starred", r"\part*{Proof Theory}"),
        )
        for name, body in cases:
            with self.subTest(name=name):
                completed = self.compile(
                    r"\begin{inheritedrestorationscope}{SRC-11354-11413}"
                    + body
                    + r"\end{inheritedrestorationscope}"
                )
                output = completed.stdout + completed.stderr
                self.assertNotEqual(completed.returncode, 0, output)
                self.assertIn("governed source part", output)

    def test_source_lj_command_is_exactly_scoped(self) -> None:
        completed = self.compile(r"Outside: \(\LJ\).")
        output = completed.stdout + completed.stderr
        self.assertNotEqual(completed.returncode, 0, output)
        self.assertIn("source LJ command outside", output)

        completed = self.compile(
            r"\begin{inheritedrestorationscope}{SRC-11520-11598}"
            r"Inside: \(\LJ\)."
            r"\end{inheritedrestorationscope}"
            r"\let\fixtureafter\LJ"
            r"\ifx\fixtureafter\relax"
            r"\PackageError{fixture}{source LJ guard leaked}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_source_ipl_command_is_exactly_scoped(self) -> None:
        completed = self.compile(r"Outside: \(\IPL\).")
        output = completed.stdout + completed.stderr
        self.assertNotEqual(completed.returncode, 0, output)
        self.assertIn("source IPL command outside", output)

        completed = self.compile(
            r"\begin{inheritedrestorationscope}{SRC-12989-13045}"
            r"Inside: \(\IPL\)."
            r"\end{inheritedrestorationscope}"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_modal_source_system_commands_are_exactly_scoped(self) -> None:
        for name in ("K", "Sfour", "Sfive"):
            with self.subTest(outside=name):
                completed = self.compile(rf"Outside: \(\{name}\).")
                output = completed.stdout + completed.stderr
                if "Windows API error 5: Access is denied" in output:
                    self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
                self.assertNotEqual(completed.returncode, 0, output)
                self.assertIn(f"source {name} command outside", output)

        completed = self.compile(
            r"\begin{inheritedrestorationscope}{SRC-13255-13284}"
            r"\newbox\sourcebox\newbox\expectedbox"
            r"\setbox\sourcebox=\hbox{$\K\Sfour\Sfive$}"
            r"\setbox\expectedbox=\hbox{$\mathsf{K}\mathsf{S4}\mathsf{S5}$}"
            r"\ifdim\wd\sourcebox=\wd\expectedbox\else"
            r"\PackageError{fixture}{modal source command width mismatch}{}\fi"
            r"\end{inheritedrestorationscope}"
            r"Registered outside verum remains available: \(\topv\)."
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_exact_part7_calculi_and_cut_elimination_compile_with_source_surface(self) -> None:
        wrappers = (
            "11354-11413", "11414-11505", "11506-11519", "11520-11598",
            "11599-11627", "11628-11644", "11645-11695", "11696-11710",
            "11711-11740", "11741-11767", "11768-11823", "11824-11881",
            "11882-11913", "11914-11960",
        )
        body = (
            r"\crefalias{hbitem}{chapter}"
            r"\refstepcounter{hbitem}\label{ch:intuitionistic-logic}"
            r"\crefalias{hbitem}{theorem}"
            r"\refstepcounter{hbitem}\label{thm:definitional-conservativity}"
            r"\setcounter{hbitem}{0}"
            r"\setcounter{part}{6}"
            r"\part{Proof Theory, Lambda Calculi, and Higher-Order Logic}"
            r"\label{part:p07-fixture}"
        )
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}" for wrapper in wrappers
        )
        body += (
            r"\typeout{PARTSEVENHBITEM=\arabic{hbitem}}"
            r"\ifnum\value{hbitem}=13\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "part:proof-theory", "ch:lk-lj", "sec:lk-lj-01",
            "sec:lk-lj-02", "sec:lk-lj-03", "sec:lk-lj-04",
            "sec:lk-lj-05", "ex:lk-lj-01", "ex:lk-lj-02",
            "ch:cut-elimination", "sec:cut-elimination-01",
            "lem:cut-mix-equipollence", "lem:cutfree-subformula",
            "sec:cut-elimination-02", "ex:cut-elimination-01",
            "ex:cut-elimination-02", "sec:cut-elimination-interpolation",
            "thm:craig-interpolation", "thm:beth",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)

        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)
        self.assert_references_defined_in_handbook(log)

        from pypdf import PdfReader

        text = "\n".join(
            page.extract_text() or "" for page in PdfReader(build / "fixture.pdf").pages
        )
        self.assertEqual(re.sub(r"\s+", " ", text).count("Proof sketch."), 4)

    def test_exact_normalization_and_ordinal_analysis_compile_with_source_surface(self) -> None:
        wrappers = (
            "11961-12029",
            "12030-12100",
            "12101-12132",
            "12133-12217",
            "12218-12248",
        )
        body = (
            r"\crefalias{hbitem}{chapter}"
            r"\refstepcounter{hbitem}\label{ch:prop-deduction}"
            r"\refstepcounter{hbitem}\label{ch:fol-deduction}"
            r"\setcounter{hbitem}{0}"
            r"\setcounter{chapter}{45}"
        )
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}" for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=10\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "ch:normalization-curry-howard",
            "sec:normalization-curry-howard-01",
            "sec:normalization-curry-howard-02",
            "sec:normalization-curry-howard-03",
            "sec:normalization-curry-howard-04",
            "ex:normalization-curry-howard-01",
            "ex:normalization-curry-howard-02",
            "ex:normalization-curry-howard-03",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)

        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)
        self.assert_references_defined_in_handbook(log)

        from pypdf import PdfReader

        text = "\n".join(
            page.extract_text() or "" for page in PdfReader(build / "fixture.pdf").pages
        )
        self.assertEqual(re.sub(r"\s+", " ", text).count("Proof sketch."), 3)

    def test_higher_order_source_part_is_subordinate_and_scope_does_not_leak(self) -> None:
        completed = self.compile(
            r"\setcounter{part}{1}"
            r"\part{Classical Logic}\label{part:p02-fixture}"
            r"\ifnum\value{part}=2\else\PackageError{fixture}{public part count}{}\fi"
            r"\input{restoration/scope-SRC-12249-12261}"
            r"\ifnum\value{part}=2\else\PackageError{fixture}{source part stepped counter}{}\fi"
            r"\part{After the governed scope}"
            r"\ifnum\value{part}=3\else\PackageError{fixture}{part meaning leaked}{}\fi"
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)

    def test_higher_order_source_real_command_is_exactly_scoped(self) -> None:
        completed = self.compile(r"Outside: \(\R\).")
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertNotEqual(completed.returncode, 0, output)
        self.assertIn("source R command outside", output)

        completed = self.compile(
            r"\begin{inheritedrestorationscope}{SRC-12415-12536}"
            r"Inside: \(\R\)."
            r"\end{inheritedrestorationscope}"
        )
        output = completed.stdout + completed.stderr
        self.assertEqual(completed.returncode, 0, output)

    def test_exact_second_and_higher_order_part_compiles_with_source_surface(self) -> None:
        wrappers = (
            "12249-12261", "12262-12289", "12290-12355", "12356-12414",
            "12415-12536", "12537-12673", "12674-12720", "12721-12783",
            "12784-12923", "12924-12950", "12951-12969",
        )
        body = (
            r"\crefalias{hbitem}{theorem}"
            r"\refstepcounter{hbitem}\label{thm:tarski-undefinability}"
            r"\setcounter{hbitem}{0}"
            r"\setcounter{part}{1}"
            r"\part{Classical Logic}\label{part:p02-fixture}"
        )
        body += "".join(
            rf"\input{{restoration/scope-SRC-{wrapper}}}" for wrapper in wrappers
        )
        body += (
            r"\ifnum\value{hbitem}=9\else"
            r"\PackageError{fixture}{source hbitem counter differed}{}\fi"
        )
        completed, build = self.compile_with_outputs(body, runs=3)
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        self.assertNotIn("Cleveref Warning", output)

        aux = (build / "fixture.aux").read_text(encoding="utf-8")
        for label in (
            "part:higher-order", "ch:second-order-logic",
            "sec:second-order-logic-01", "sec:second-order-logic-02",
            "sec:second-order-logic-03", "sec:second-order-logic-04",
            "thm:second-order-reals-categorical", "thm:lindstrom",
            "sec:second-order-logic-05", "ex:second-order-logic-01",
            "ex:second-order-logic-02", "ex:second-order-logic-03",
            "ch:simple-type-theory", "sec:simple-type-theory-01",
            "sec:simple-type-theory-02", "sec:simple-type-theory-03",
            "ex:simple-type-theory-01", "ex:simple-type-theory-02",
            "ex:simple-type-theory-03",
        ):
            self.assertEqual(aux.count(rf"\newlabel{{{label}}}"), 1, label)

        log = (build / "fixture.log").read_text(encoding="utf-8", errors="replace")
        self.assertNotIn("multiply defined", log)
        self.assert_references_defined_in_handbook(log)

        from pypdf import PdfReader

        text = "\n".join(
            page.extract_text() or "" for page in PdfReader(build / "fixture.pdf").pages
        )
        # The one source "Proof sketch." (capture 12415-12536) became a complete "Proof." under the
        # recorded W02B-lead-corrections version-4 record: the full proof is routed in Part 2.
        flat_text = re.sub(r"\s+", " ", text)
        self.assertEqual(flat_text.count("Proof sketch."), 0)
        self.assertRegex(flat_text, r"Proof\. ?The complete proof, including the effectiveness of the reduction")

if __name__ == "__main__":
    unittest.main()
