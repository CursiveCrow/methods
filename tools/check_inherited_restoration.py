#!/usr/bin/env python3
"""Fail-closed checks for exact captures and explicit corrected-reader candidates.

This checker establishes only the source and static results described by each
record.  It does not establish semantic correctness, build success, rendered
fidelity, reviewer independence, or human approval.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[1]
PROVENANCE_ID_RE = re.compile(r"^(?:PRE|SRC|CTL|SEP)-(\d{5})-(\d{5})$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
LABEL_RE = re.compile(
    r"^(?:part|ch|sec|entry|def|thm|lem|cor|method|rem|prob|app|ex|tab|fig|sheet|rule|annex):[^\s{}]+$"
)
CONTENT_TOKEN_COMPARISON = (
    "Replace each terminal CRLF, LF, or CR with one LF byte, preserve "
    "physical-line order, and compare every other byte exactly."
)
FROZEN_AUTHORITY = {
    "path": "source/formal-logic-reference.tex",
    "bytes": 762835,
    "lines": 17206,
    "sha256": "0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc",
}
# Version 4 is mechanical candidate validation, not corrected-source admission.
CORRECTION_POLICY_PATH = "spec/EDITION-2026-CONTRACT.md"
CORRECTION_POLICY_LOCATOR = "Reader-facing content and corrections"
CORRECTION_POLICY_TEXT = (
    "Correct known mathematical errors directly in active definitions, formulas, "
    "statements and proofs, including active restoration files. Preserve the frozen "
    "source artifact byte for byte and retain historical readings as evidence."
)
CORRECTED_CONTENT_COMPARISON = (
    "Normalize terminal CRLF, LF, or CR to LF; replay the recorded correction edits "
    "against the frozen interval; compare every unchanged line and every replacement exactly."
)
READER_CORRECTION_FIELDS = {
    "kind", "correction_id", "policy_authority", "rationale", "predecessor_record",
    "affected_ids", "source_content_token_sha256", "edits",
}
CORRECTION_VERIFICATION_SCOPES = {
    "source": "Checks the frozen authority/interval, current reader bytes and declared correction map; not source-text acceptance.",
    "static": "Checks the closed corrected-reader candidate, identities and unchanged spans; independent review, build, visual and admission remain pending.",
}
ROOT_FIELDS = {
    "schema_version",
    "provenance_id",
    "authority",
    "source_locator",
    "source_unit_evidence",
    "artifact_line_standing",
    "presentation_identity",
    "restoration_artifact",
    "handbook_destination",
    "disposition",
    "audit_evidence",
    "completeness",
    "verification",
    "verification_evidence",
    "owed_artifacts",
}
# Necessity: the exact source contains part commands whose unchanged placement
# either nests beneath an already fixed public part or carries a source printed
# ordinal different from its fixed final public ordinal; ordinary inclusion
# cannot express both cases without ambiguity.
# Definition: reader_layout is the following closed administrative object; for
# exactly each listed provenance ID, it binds that exact source command, optional label,
# wrapper, public driver, heading behavior, counter effect, TOC level, bookmark
# level, and attribution.  The three Part II entries and the Part IV and Part VII
# entries become subordinate chapters; the Model Theory entry executes directly
# once as final public Part III; the Formal Arithmetic entry advances the
# counter once while retaining the fixed public Part V title and exact source
# label; the exact Set Theory entry executes directly once as final public Part
# VI; the Nonclassical entry advances once while retaining the fixed plural
# public Part VIII title and exact source label; and the label-less Formal
# Practice entry becomes a subordinate chapter under fixed public Part XII.
# Standing: it is layout/build metadata, not a motive, relation, statement
# family, source-fidelity verdict, completeness result, or review result.
# Nonredundancy: the locator proves source-byte identity and the destination
# records placement, but neither states whether one of these exact part commands
# is subordinate or direct, nor its allowed counter effect or final container.
# Use: this checker, the TeX scope where interception is required, and the
# public-part scanner consume these exact fields and fail closed for every
# listed ID; no unlisted ID is admitted and no status can be promoted.
READER_LAYOUT_FIELDS = {
    "source_part_line",
    "source_part_command",
    "source_label_line",
    "source_label",
    "wrapper_path",
    "public_part_file",
    "public_part_title",
    "public_part_label",
    "reader_heading_level",
    "reader_heading_title",
    "reader_attribution",
    "part_counter_effect",
    "toc_level",
    "bookmark_level",
}
READER_LAYOUTS = {
    "SRC-01649-01660": {
        "source_part_line": 1649,
        "source_part_command": r"\part{Classical Propositional Logic}",
        "source_label_line": 1650,
        "source_label": "part:classical-propositional",
        "wrapper_path": "handbook/restoration/scope-SRC-01649-01660.tex",
        "public_part_file": "handbook/parts/p02.tex",
        "public_part_title": "Classical Logic",
        "public_part_label": "part:p02",
        "reader_heading_level": "chapter*",
        "reader_heading_title": "Classical Propositional Logic",
        "reader_attribution": (
            "Inherited source: Formal Logic, Version 1.0, source line 1649."
        ),
        "part_counter_effect": "none",
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
    "SRC-03022-03037": {
        "source_part_line": 3022,
        "source_part_command": r"\part{Classical First-Order Logic}",
        "source_label_line": 3023,
        "source_label": "part:classical-first-order",
        "wrapper_path": "handbook/restoration/scope-SRC-03022-03037.tex",
        "public_part_file": "handbook/parts/p02.tex",
        "public_part_title": "Classical Logic",
        "public_part_label": "part:p02",
        "reader_heading_level": "chapter*",
        "reader_heading_title": "Classical First-Order Logic",
        "reader_attribution": (
            "Inherited source: Formal Logic, Version 1.0, source line 3022."
        ),
        "part_counter_effect": "none",
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
    "SRC-06049-06069": {
        "source_part_line": 6049,
        "source_part_command": r"\part{Model Theory}",
        "source_label_line": 6050,
        "source_label": "part:model-theory",
        "wrapper_path": "handbook/restoration/scope-SRC-06049-06069.tex",
        "public_part_file": "handbook/parts/p03.tex",
        "public_part_title": "Model Theory",
        "public_part_label": "part:model-theory",
        "reader_heading_level": "part",
        "reader_heading_title": "Model Theory",
        "reader_attribution": (
            "Inherited source: Formal Logic, Version 1.0, printed Part IV at "
            "source line 6049; executed unchanged as final public Part III."
        ),
        "part_counter_effect": "increment once to final Part III",
        "toc_level": "part",
        "bookmark_level": -1,
    },
    "SRC-07494-07505": {
        "source_part_line": 7494,
        "source_part_command": r"\part{Computability}",
        "source_label_line": 7495,
        "source_label": "part:computability",
        "wrapper_path": "handbook/restoration/scope-SRC-07494-07505.tex",
        "public_part_file": "handbook/parts/p04.tex",
        "public_part_title": "Computability and Complexity",
        "public_part_label": "part:p04",
        "reader_heading_level": "chapter*",
        "reader_heading_title": "Computability",
        "reader_attribution": (
            "Inherited source: Formal Logic, Version 1.0, source line 7494."
        ),
        "part_counter_effect": "none",
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
    "SRC-09080-09098": {
        "source_part_line": 9080,
        "source_part_command": r"\part{Formal Arithmetic and Incompleteness}",
        "source_label_line": 9081,
        "source_label": "part:incompleteness",
        "wrapper_path": "handbook/restoration/scope-SRC-09080-09098.tex",
        "public_part_file": "handbook/parts/p05.tex",
        "public_part_title": "Arithmetic and Incompleteness",
        "public_part_label": "part:incompleteness",
        "reader_heading_level": "part",
        "reader_heading_title": "Arithmetic and Incompleteness",
        "reader_attribution": (
            "Inherited source: Formal Logic, Version 1.0, printed Part VI at "
            "source line 9080; executed with its exact label as final public Part V."
        ),
        "part_counter_effect": "increment once to final Part V",
        "toc_level": "part",
        "bookmark_level": -1,
    },
    "SRC-10060-10088": {
        "source_part_line": 10060,
        "source_part_command": r"\part{Axiomatic Set Theory}",
        "source_label_line": 10061,
        "source_label": "part:set-theory",
        "wrapper_path": "handbook/restoration/scope-SRC-10060-10088.tex",
        "public_part_file": "handbook/parts/p06.tex",
        "public_part_title": "Axiomatic Set Theory",
        "public_part_label": "part:set-theory",
        "reader_heading_level": "part",
        "reader_heading_title": "Axiomatic Set Theory",
        "reader_attribution": (
            "Inherited source: Formal Logic, Version 1.0, printed Part VII at "
            "source line 10060; executed unchanged as final public Part VI."
        ),
        "part_counter_effect": "increment once to final Part VI",
        "toc_level": "part",
        "bookmark_level": -1,
    },
    "SRC-11354-11413": {
        "source_part_line": 11354,
        "source_part_command": r"\part{Proof Theory}",
        "source_label_line": 11355,
        "source_label": "part:proof-theory",
        "wrapper_path": "handbook/restoration/scope-SRC-11354-11413.tex",
        "public_part_file": "handbook/parts/p07.tex",
        "public_part_title": "Proof Theory, Lambda Calculi, and Higher-Order Logic",
        "public_part_label": "part:p07",
        "reader_heading_level": "chapter*",
        "reader_heading_title": "Proof Theory",
        "reader_attribution": (
            "Inherited source: Formal Logic, Version 1.0, source line 11354."
        ),
        "part_counter_effect": "none",
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
    "SRC-12249-12261": {
        "source_part_line": 12249,
        "source_part_command": r"\part{Second-Order and Higher-Order Logic}",
        "source_label_line": 12250,
        "source_label": "part:higher-order",
        "wrapper_path": "handbook/restoration/scope-SRC-12249-12261.tex",
        "public_part_file": "handbook/parts/p02.tex",
        "public_part_title": "Classical Logic",
        "public_part_label": "part:p02",
        "reader_heading_level": "chapter*",
        "reader_heading_title": "Second-Order and Higher-Order Logic",
        "reader_attribution": (
            "Inherited source: Formal Logic, Version 1.0, printed Part IX at "
            "source line 12249; retained at the audited public Part II "
            "higher-order destination."
        ),
        "part_counter_effect": "none",
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
    "SRC-12970-12988": {
        "source_part_line": 12970,
        "source_part_command": r"\part{Nonclassical Logic}",
        "source_label_line": 12971,
        "source_label": "part:nonclassical",
        "wrapper_path": "handbook/restoration/scope-SRC-12970-12988.tex",
        "public_part_file": "handbook/parts/p08.tex",
        "public_part_title": "Nonclassical Logics",
        "public_part_label": "part:nonclassical",
        "reader_heading_level": "part",
        "reader_heading_title": "Nonclassical Logics",
        "reader_attribution": (
            "Inherited source: Formal Logic, Version 1.0, printed Part X at "
            "source line 12970; executed with its exact label as final public Part VIII."
        ),
        "part_counter_effect": "increment once to final Part VIII",
        "toc_level": "part",
        "bookmark_level": -1,
    },
    "SRC-14095-14146": {
        "source_part_line": 14095,
        "source_part_command": r"\part{Formal Practice, Automation, and Verification}",
        "source_label_line": 0,
        "source_label": "",
        "wrapper_path": "handbook/restoration/scope-SRC-14095-14146.tex",
        "public_part_file": "handbook/parts/p12.tex",
        "public_part_title": "Automation, Mechanization, and Formal Practice",
        "public_part_label": "part:p12",
        "reader_heading_level": "chapter*",
        "reader_heading_title": "Formal Practice, Automation, and Verification",
        "reader_attribution": (
            "Inherited source: Formal Logic, Version 1.0, source line 14095."
        ),
        "part_counter_effect": "none",
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
}
COMPLETENESS_FIELDS = {
    "notation",
    "definitions",
    "hypotheses",
    "rules",
    "side_conditions",
    "statement_strength",
    "proof_status",
    "proof_steps",
    "examples",
    "qualifications",
    "attribution",
}
VERIFICATION_FIELDS = {
    "source",
    "independent_source",
    "static",
    "build",
    "visual",
    "human_review",
}
# Necessity: the exact source appendix transition at line 15093 must establish
# source Appendix A without globally converting the later public Parts XIII and
# XIV into appendices; the part-only reader_layout object cannot state that
# local counter boundary without misnaming the source command.
# Definition: reader_appendix_layout is the closed administrative object below;
# it binds the exact appendix/chapter or section-continuation commands, all
# source labels, wrapper, public Part XII driver, local appendix ordinal,
# heading, counter restoration, TOC level, and bookmark level for the listed
# records.
# Standing: it is layout/build metadata, not a mathematical relation, statement
# family, source-fidelity verdict, admission result, or review result.
# Nonredundancy: the source locator and artifact hash prove the bytes, and the
# destination records the file, but neither contains the local Appendix A--F
# numbering effects or the mandatory restoration of the prior public counter.
# Use: this checker validates every field and token, handbook.sty consumes each
# provenance-specific layout, and Part XII publication and TeX tests reject
# missing, duplicated, reordered, leaking, or globally renumbering variants.
READER_APPENDIX_LAYOUT_FIELDS = {
    "source_appendix_line",
    "source_appendix_command",
    "source_chapter_line",
    "source_chapter_command",
    "source_label_lines",
    "source_labels",
    "wrapper_path",
    "public_part_file",
    "public_part_title",
    "public_part_label",
    "appendix_ordinal",
    "reader_heading_level",
    "reader_heading_title",
    "chapter_counter_effect",
    "toc_level",
    "bookmark_level",
}
READER_APPENDIX_LAYOUTS = {
    "SRC-15093-15206": {
        "source_appendix_line": 15093,
        "source_appendix_command": r"\appendix",
        "source_chapter_line": 15095,
        "source_chapter_command": r"\chapter{Registered Notation}",
        "source_label_lines": [15096, 15097, 15194, 15201],
        "source_labels": [
            "ch:registered-notation",
            "app:notation",
            "sec:registered-notation-01",
            "sec:registered-notation-02",
        ],
        "wrapper_path": "handbook/restoration/scope-SRC-15093-15206.tex",
        "public_part_file": "handbook/parts/p12.tex",
        "public_part_title": "Automation, Mechanization, and Formal Practice",
        "public_part_label": "part:p12",
        "appendix_ordinal": "A",
        "reader_heading_level": "appendix chapter",
        "reader_heading_title": "Registered Notation",
        "chapter_counter_effect": (
            "local Appendix A; restore prior public chapter counter"
        ),
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
    "SRC-15207-15239": {
        "source_appendix_line": 0,
        "source_appendix_command": "",
        "source_chapter_line": 15207,
        "source_chapter_command": r"\chapter{Binding and Precedence}",
        "source_label_lines": [15208, 15209],
        "source_labels": ["ch:binding-precedence", "app:precedence"],
        "wrapper_path": "handbook/restoration/scope-SRC-15207-15239.tex",
        "public_part_file": "handbook/parts/p12.tex",
        "public_part_title": "Automation, Mechanization, and Formal Practice",
        "public_part_label": "part:p12",
        "appendix_ordinal": "B",
        "reader_heading_level": "appendix chapter",
        "reader_heading_title": "Binding and Precedence",
        "chapter_counter_effect": (
            "local Appendix B; restore prior public chapter counter"
        ),
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
    "SRC-15240-15488": {
        "source_appendix_line": 0,
        "source_appendix_command": "",
        "source_chapter_line": 15240,
        "source_chapter_command": r"\chapter{Rule Sheets}",
        "source_label_lines": [15241, 15242, 15245, 15368, 15471],
        "source_labels": [
            "ch:rule-sheets",
            "app:rules",
            "sec:rule-sheets-01",
            "sec:rule-sheets-02",
            "sec:rule-sheets-03",
        ],
        "wrapper_path": "handbook/restoration/scope-SRC-15240-15488.tex",
        "public_part_file": "handbook/parts/p12.tex",
        "public_part_title": "Automation, Mechanization, and Formal Practice",
        "public_part_label": "part:p12",
        "appendix_ordinal": "C",
        "reader_heading_level": "appendix chapter",
        "reader_heading_title": "Rule Sheets",
        "chapter_counter_effect": (
            "local Appendix C; restore prior public chapter counter"
        ),
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
    "SRC-15489-15619": {
        "source_appendix_line": 0,
        "source_appendix_command": "",
        "source_chapter_line": 15489,
        "source_chapter_command": (
            r"\chapter{Qualifying-Examination Problems and Selected Solutions}"
        ),
        "source_label_lines": [
            15490,
            15491,
            15494,
            15495,
            15534,
            15535,
            15556,
            15557,
            15578,
            15579,
            15596,
            15597,
        ],
        "source_labels": [
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
        ],
        "wrapper_path": "handbook/restoration/scope-SRC-15489-15619.tex",
        "public_part_file": "handbook/parts/p12.tex",
        "public_part_title": "Automation, Mechanization, and Formal Practice",
        "public_part_label": "part:p12",
        "appendix_ordinal": "D",
        "reader_heading_level": "appendix chapter",
        "reader_heading_title": (
            "Qualifying-Examination Problems and Selected Solutions"
        ),
        "chapter_counter_effect": (
            "local Appendix D; restore prior public chapter counter"
        ),
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
    "SRC-15620-15637": {
        "source_appendix_line": 0,
        "source_appendix_command": "",
        "source_chapter_line": 0,
        "source_chapter_command": "",
        "source_label_lines": [15621],
        "source_labels": ["sec:qualifying-problems-06"],
        "wrapper_path": "handbook/restoration/scope-SRC-15620-15637.tex",
        "public_part_file": "handbook/parts/p12.tex",
        "public_part_title": "Automation, Mechanization, and Formal Practice",
        "public_part_label": "part:p12",
        "appendix_ordinal": "D",
        "reader_heading_level": "appendix section continuation",
        "reader_heading_title": "Additional problems",
        "chapter_counter_effect": (
            "local Appendix D.6; restore prior public chapter and section counters"
        ),
        "toc_level": "section",
        "bookmark_level": 1,
    },
    "SRC-15638-16742": {
        "source_appendix_line": 0,
        "source_appendix_command": "",
        "source_chapter_line": 15638,
        "source_chapter_command": r"\chapter{Exercise Feedback}",
        "source_label_lines": [15639, 15640],
        "source_labels": ["ch:exercise-feedback", "app:exercise-feedback"],
        "wrapper_path": "handbook/restoration/scope-SRC-15638-16742.tex",
        "public_part_file": "handbook/parts/p12.tex",
        "public_part_title": "Automation, Mechanization, and Formal Practice",
        "public_part_label": "part:p12",
        "appendix_ordinal": "E",
        "reader_heading_level": "appendix chapter",
        "reader_heading_title": "Exercise Feedback",
        "chapter_counter_effect": (
            "local Appendix E; restore prior public chapter counter"
        ),
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
    "SRC-16743-16801": {
        "source_appendix_line": 0,
        "source_appendix_command": "",
        "source_chapter_line": 16743,
        "source_chapter_command": r"\chapter{Editorial and Formal-Logical Release Checklist}",
        "source_label_lines": [16744, 16745, 16748, 16762, 16778, 16790],
        "source_labels": [
            "ch:release-checklist",
            "app:release-checklist",
            "sec:release-checklist-01",
            "sec:release-checklist-02",
            "sec:release-checklist-03",
            "sec:release-checklist-04",
        ],
        "wrapper_path": "handbook/restoration/scope-SRC-16743-16801.tex",
        "public_part_file": "handbook/parts/p12.tex",
        "public_part_title": "Automation, Mechanization, and Formal Practice",
        "public_part_label": "part:p12",
        "appendix_ordinal": "F",
        "reader_heading_level": "appendix chapter",
        "reader_heading_title": "Editorial and Formal-Logical Release Checklist",
        "chapter_counter_effect": (
            "local Appendix F; restore prior public chapter counter"
        ),
        "toc_level": "chapter",
        "bookmark_level": 0,
    },
}
CONTRACT_CLASSIFICATIONS = {
    "full-and-accurate",
    "layout-only relocation",
    "altered",
    "abridged",
    "omitted",
    "hybridized",
    "unsupported addition",
}


class CheckFailure(ValueError):
    """One fail-closed validation result."""


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def exact_object(value: Any, fields: set[str], where: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise CheckFailure(f"{where}: expected object")
    actual = set(value)
    if actual != fields:
        missing = sorted(fields - actual)
        extra = sorted(actual - fields)
        raise CheckFailure(f"{where}: field mismatch; missing={missing}, extra={extra}")
    return value


def nonempty_string(value: Any, where: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CheckFailure(f"{where}: expected nonempty string")
    return value


def exact_integer(value: Any, where: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise CheckFailure(f"{where}: expected integer >= {minimum}")
    return value


def exact_sha256(value: Any, where: str) -> str:
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise CheckFailure(f"{where}: expected lowercase SHA-256")
    return value


def one_of(value: Any, allowed: set[str], where: str) -> str:
    if not isinstance(value, str) or value not in allowed:
        raise CheckFailure(f"{where}: expected one of {sorted(allowed)}, got {value!r}")
    return value


def duplicate_rejecting_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CheckFailure(f"duplicate JSON field {key!r}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=duplicate_rejecting_object,
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CheckFailure(f"{path}: cannot read JSON: {exc}") from exc


def contained_file(
    repo_root: Path,
    raw_path: Any,
    where: str,
    required_parent: Path | None = None,
) -> tuple[str, Path]:
    relative = nonempty_string(raw_path, where)
    candidate = Path(relative)
    if candidate.is_absolute():
        raise CheckFailure(f"{where}: path must be repository-relative")
    resolved = (repo_root / candidate).resolve()
    try:
        resolved.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise CheckFailure(f"{where}: path escapes repository root") from exc
    if required_parent is not None:
        parent = (repo_root / required_parent).resolve()
        try:
            resolved.relative_to(parent)
        except ValueError as exc:
            raise CheckFailure(f"{where}: path must be under {required_parent.as_posix()}") from exc
    if not resolved.is_file():
        raise CheckFailure(f"{where}: file does not exist: {relative}")
    return candidate.as_posix(), resolved


def physical_lines(raw: bytes, where: str) -> list[bytes]:
    lines = raw.splitlines(keepends=True)
    if b"".join(lines) != raw:
        raise CheckFailure(f"{where}: byte-preserving physical-line split failed")
    return lines


def line_body_and_ending(line: bytes) -> tuple[bytes, bytes]:
    if line.endswith(b"\r\n"):
        return line[:-2], b"\r\n"
    if line.endswith(b"\n"):
        return line[:-1], b"\n"
    if line.endswith(b"\r"):
        return line[:-1], b"\r"
    return line, b""


def canonical_content_token_bytes(lines: list[bytes], where: str) -> bytes:
    bodies: list[bytes] = []
    for index, line in enumerate(lines, start=1):
        body, ending = line_body_and_ending(line)
        if not ending:
            raise CheckFailure(f"{where}: physical line {index} lacks a terminal line ending")
        bodies.append(body)
    return b"\n".join(bodies) + b"\n"


def validate_authority(
    record: dict[str, Any], repo_root: Path
) -> tuple[bytes, list[bytes]]:
    authority = exact_object(
        record["authority"],
        {"path", "edition", "corpus_manifest", "bytes", "physical_lines", "sha256"},
        "authority",
    )
    nonempty_string(authority["edition"], "authority.edition")
    manifest_display, manifest_path = contained_file(
        repo_root, authority["corpus_manifest"], "authority.corpus_manifest"
    )
    manifest = exact_object(load_json(manifest_path), {"schema_version", "tex", "pdf"}, manifest_display)
    if manifest["schema_version"] != 1 or type(manifest["schema_version"]) is not int:
        raise CheckFailure(f"{manifest_display}.schema_version: expected integer 1")
    tex = exact_object(
        manifest["tex"], {"path", "bytes", "lines", "sha256"}, f"{manifest_display}.tex"
    )
    if tex != FROZEN_AUTHORITY:
        raise CheckFailure(
            f"{manifest_display}.tex disagrees with the exact frozen authority"
        )

    authority_path, source_path = contained_file(repo_root, authority["path"], "authority.path")
    if authority_path != tex["path"]:
        raise CheckFailure("authority.path does not match the inherited-corpus manifest")
    expected_bytes = exact_integer(authority["bytes"], "authority.bytes", 1)
    expected_lines = exact_integer(authority["physical_lines"], "authority.physical_lines", 1)
    expected_hash = exact_sha256(authority["sha256"], "authority.sha256")
    if (expected_bytes, expected_lines, expected_hash) != (
        tex["bytes"],
        tex["lines"],
        tex["sha256"],
    ):
        raise CheckFailure("authority integrity fields do not match the inherited-corpus manifest")

    raw = source_path.read_bytes()
    lines = physical_lines(raw, authority_path)
    if len(raw) != expected_bytes:
        raise CheckFailure(f"authority byte count mismatch: {len(raw)} != {expected_bytes}")
    if len(lines) != expected_lines:
        raise CheckFailure(f"authority line count mismatch: {len(lines)} != {expected_lines}")
    actual_hash = sha256(raw)
    if actual_hash != expected_hash:
        raise CheckFailure(f"authority digest mismatch: {actual_hash} != {expected_hash}")
    return raw, lines


def validate_source_locator(
    record: dict[str, Any], provenance_id: str, source_lines: list[bytes]
) -> tuple[int, int, list[bytes]]:
    locator = exact_object(
        record["source_locator"],
        {"start_line", "end_line", "line_count", "interval_sha256"},
        "source_locator",
    )
    start = exact_integer(locator["start_line"], "source_locator.start_line", 1)
    end = exact_integer(locator["end_line"], "source_locator.end_line", 1)
    count = exact_integer(locator["line_count"], "source_locator.line_count", 1)
    if end < start or count != end - start + 1 or end > len(source_lines):
        raise CheckFailure("source_locator has inconsistent or out-of-range line bounds")
    match = PROVENANCE_ID_RE.fullmatch(provenance_id)
    if not match or (int(match.group(1)), int(match.group(2))) != (start, end):
        raise CheckFailure("provenance_id does not encode the exact source locator")
    interval = source_lines[start - 1 : end]
    actual_hash = sha256(b"".join(interval))
    expected_hash = exact_sha256(locator["interval_sha256"], "source_locator.interval_sha256")
    if actual_hash != expected_hash:
        raise CheckFailure(f"source interval digest mismatch: {actual_hash} != {expected_hash}")
    return start, end, interval


def validate_audit_evidence(
    record: dict[str, Any],
    repo_root: Path,
    start: int,
    end: int,
    source_lines: list[bytes],
) -> None:
    evidence = exact_object(
        record["audit_evidence"],
        {"source_map", "interval_ids", "classifications"},
        "audit_evidence",
    )
    map_display, map_path = contained_file(
        repo_root, evidence["source_map"], "audit_evidence.source_map"
    )
    interval_ids = evidence["interval_ids"]
    if not isinstance(interval_ids, list) or not interval_ids:
        raise CheckFailure("audit_evidence.interval_ids: expected nonempty array")
    for index, value in enumerate(interval_ids):
        nonempty_string(value, f"audit_evidence.interval_ids[{index}]")
    if len(interval_ids) != len(set(interval_ids)):
        raise CheckFailure("audit_evidence.interval_ids: duplicate identifier")

    classifications = evidence["classifications"]
    if not isinstance(classifications, list):
        raise CheckFailure("audit_evidence.classifications: expected array")
    for index, value in enumerate(classifications):
        one_of(value, CONTRACT_CLASSIFICATIONS, f"audit_evidence.classifications[{index}]")
    if len(classifications) != len(set(classifications)):
        raise CheckFailure("audit_evidence.classifications: duplicate classification")

    try:
        with map_path.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, UnicodeError, csv.Error) as exc:
        raise CheckFailure(f"{map_display}: cannot read source map: {exc}") from exc
    required_columns = {
        "stable_id",
        "source_start",
        "source_end",
        "source_sha256",
        "class_normalized",
    }
    if not rows or not required_columns.issubset(rows[0]):
        raise CheckFailure(f"{map_display}: missing required source-map columns")
    by_id: dict[str, dict[str, str]] = {}
    for row in rows:
        stable_id = row.get("stable_id", "")
        if stable_id in by_id:
            raise CheckFailure(f"{map_display}: duplicate stable_id {stable_id!r}")
        by_id[stable_id] = row
    selected: list[dict[str, str]] = []
    for interval_id in interval_ids:
        if interval_id not in by_id:
            raise CheckFailure(f"audit interval does not resolve: {interval_id}")
        selected.append(by_id[interval_id])

    coverage = [0] * (end - start + 1)
    found_classes: set[str] = set()
    for row in selected:
        try:
            row_start = int(row["source_start"])
            row_end = int(row["source_end"])
        except (KeyError, ValueError) as exc:
            raise CheckFailure(f"{map_display}: invalid interval bounds") from exc
        if row_end < row_start or row_end < start or row_start > end:
            raise CheckFailure("audit interval does not cover the provenance source locator")
        recorded_hash = exact_sha256(
            row.get("source_sha256"),
            f"audit interval {row.get('stable_id', '<missing>')}.source_sha256",
        )
        actual_hash = sha256(b"".join(source_lines[row_start - 1 : row_end]))
        if recorded_hash != actual_hash:
            raise CheckFailure(
                "audit interval digest mismatch at "
                f"{row.get('stable_id', '<missing>')}: {recorded_hash} != {actual_hash}"
            )
        for number in range(max(row_start, start), min(row_end, end) + 1):
            coverage[number - start] += 1
        found_classes.update(
            item.strip()
            for item in row.get("class_normalized", "").split(";")
            if item.strip()
        )
    if any(value != 1 for value in coverage):
        raise CheckFailure("audit intervals do not cover the provenance source locator exactly once")
    if set(classifications) != found_classes:
        raise CheckFailure(
            "audit classifications do not exactly match the selected source-map intervals"
        )


def validate_source_unit_evidence(
    record: dict[str, Any],
    repo_root: Path,
    start: int,
    end: int,
    source_lines: list[bytes],
) -> None:
    evidence = exact_object(
        record["source_unit_evidence"],
        {"inventory", "unit_ordinals"},
        "source_unit_evidence",
    )
    inventory_display, inventory_path = contained_file(
        repo_root, evidence["inventory"], "source_unit_evidence.inventory"
    )
    raw_ordinals = evidence["unit_ordinals"]
    if not isinstance(raw_ordinals, list):
        raise CheckFailure("source_unit_evidence.unit_ordinals: expected array")
    ordinals = [
        exact_integer(value, f"source_unit_evidence.unit_ordinals[{index}]", 1)
        for index, value in enumerate(raw_ordinals)
    ]
    if ordinals != sorted(set(ordinals)):
        raise CheckFailure(
            "source_unit_evidence.unit_ordinals must be unique and increasing"
        )

    try:
        with inventory_path.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, UnicodeError, csv.Error) as exc:
        raise CheckFailure(f"{inventory_display}: cannot read source-unit inventory: {exc}") from exc
    required_columns = {
        "ordinal",
        "kind",
        "title",
        "label",
        "start_line",
        "end_line",
        "sha256",
    }
    if not rows or not required_columns.issubset(rows[0]):
        raise CheckFailure(f"{inventory_display}: missing required source-unit columns")

    parsed: list[tuple[int, int, int, dict[str, str]]] = []
    seen: set[int] = set()
    for row in rows:
        try:
            ordinal = int(row["ordinal"])
            row_start = int(row["start_line"])
            row_end = int(row["end_line"])
        except (KeyError, ValueError) as exc:
            raise CheckFailure(f"{inventory_display}: invalid source-unit locator") from exc
        if ordinal in seen:
            raise CheckFailure(f"{inventory_display}: duplicate source-unit ordinal {ordinal}")
        seen.add(ordinal)
        parsed.append((ordinal, row_start, row_end, row))

    overlapping = [item for item in parsed if item[1] <= end and item[2] >= start]
    expected_ordinals = sorted(item[0] for item in overlapping)
    if ordinals != expected_ordinals:
        raise CheckFailure(
            "source-unit locator mismatch: unit_ordinals do not exactly list every "
            "inventory unit overlapping the source locator"
        )
    for ordinal, row_start, row_end, row in overlapping:
        if row_start < start or row_end > end:
            raise CheckFailure(
                "source-unit locator mismatch: the source locator truncates inventory "
                f"unit {ordinal} at {row_start}--{row_end}"
            )
        actual_hash = sha256(b"".join(source_lines[row_start - 1 : row_end]))
        if exact_sha256(row["sha256"], f"source-unit inventory row {ordinal}.sha256") != actual_hash:
            raise CheckFailure(f"source-unit inventory digest mismatch at ordinal {ordinal}")

    identity = record["presentation_identity"]
    exact_matches = [
        item for item in overlapping if item[1] == start and item[2] == end
    ]
    if len(exact_matches) == 1:
        row = exact_matches[0][3]
        if identity["kind"] != row["kind"] or identity["source_title"] != row["title"]:
            raise CheckFailure(
                "presentation_identity does not match the exact source-unit inventory row"
            )


def validate_restoration_artifact(
    record: dict[str, Any], repo_root: Path, start: int, end: int, source_interval: list[bytes]
) -> None:
    artifact = exact_object(
        record["restoration_artifact"],
        {
            "path",
            "bytes",
            "physical_lines",
            "sha256",
            "content_token_sha256",
            "content_token_comparison",
        },
        "restoration_artifact",
    )
    display, path = contained_file(
        repo_root,
        artifact["path"],
        "restoration_artifact.path",
        Path("handbook/restoration"),
    )
    expected_name = f"inherited-{start:05d}-{end:05d}.tex"
    if path.name != expected_name:
        raise CheckFailure(
            f"restoration_artifact.path: expected locator-bound filename {expected_name}"
        )
    raw = path.read_bytes()
    lines = physical_lines(raw, display)
    expected_bytes = exact_integer(artifact["bytes"], "restoration_artifact.bytes", 1)
    expected_lines = exact_integer(
        artifact["physical_lines"], "restoration_artifact.physical_lines", 1
    )
    expected_hash = exact_sha256(artifact["sha256"], "restoration_artifact.sha256")
    if len(raw) != expected_bytes:
        raise CheckFailure(f"restoration artifact byte count mismatch: {len(raw)} != {expected_bytes}")
    if len(lines) != expected_lines or expected_lines != end - start + 1:
        raise CheckFailure("restoration artifact line count does not match its source locator")
    actual_hash = sha256(raw)
    if actual_hash != expected_hash:
        raise CheckFailure(f"restoration artifact digest mismatch: {actual_hash} != {expected_hash}")
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CheckFailure(f"{display}: restoration artifact is not UTF-8") from exc
    if raw.startswith(b"\xef\xbb\xbf"):
        raise CheckFailure(f"{display}: restoration artifact has an added UTF-8 BOM")
    if artifact["content_token_comparison"] != CONTENT_TOKEN_COMPARISON:
        raise CheckFailure("restoration_artifact.content_token_comparison is not the exact rule")

    source_content = canonical_content_token_bytes(source_interval, "source interval")
    artifact_content = canonical_content_token_bytes(lines, display)
    expected_content_hash = exact_sha256(
        artifact["content_token_sha256"], "restoration_artifact.content_token_sha256"
    )
    if sha256(source_content) != expected_content_hash:
        raise CheckFailure("source content-token digest does not match the provenance record")
    if sha256(artifact_content) != expected_content_hash:
        raise CheckFailure("restoration artifact content-token digest does not match the source")
    source_bodies = [line_body_and_ending(line)[0] for line in source_interval]
    artifact_bodies = [line_body_and_ending(line)[0] for line in lines]
    if artifact_bodies != source_bodies:
        raise CheckFailure("restoration artifact content tokens differ from the source interval")


def correction_slice_bytes(lines: list[bytes], where: str) -> bytes:
    """V4 half-open slices use SHA256(empty bytes) for an empty range."""
    return canonical_content_token_bytes(lines, where) if lines else b""


def _correction_file(value: Any, root: Path, where: str, *, locator: bool = False) -> tuple[Path, dict[str, Any]]:
    fields = {"path", "sha256"} | ({"locator"} if locator else set())
    item = exact_object(value, fields, where)
    _, path = contained_file(root, item["path"], f"{where}.path", Path("spec"))
    if sha256(path.read_bytes()) != exact_sha256(item["sha256"], f"{where}.sha256"):
        raise CheckFailure(f"{where}: evidence digest mismatch")
    if locator:
        nonempty_string(item["locator"], f"{where}.locator")
    return path, item


def _validate_correction_predecessor(record: dict[str, Any], record_path: Path, root: Path) -> None:
    """Check historical record custody, not the old artifact at its now changed path."""
    link = record["reader_correction"]["predecessor_record"]
    seen = {record_path.resolve()}
    while True:
        path, _ = _correction_file(link, root, "reader_correction.predecessor_record")
        if path in seen:
            raise CheckFailure("reader_correction.predecessor_record: cyclic/self predecessor")
        seen.add(path)
        previous = load_json(path)
        if not isinstance(previous, dict) or type(previous.get("schema_version")) is not int:
            raise CheckFailure("reader_correction.predecessor_record: invalid record")
        version = previous["schema_version"]
        if version not in {1, 4}:
            raise CheckFailure("reader_correction.predecessor_record: only plain source records are supported")
        exact_object(previous, ROOT_FIELDS | ({"reader_correction"} if version == 4 else set()),
                     "reader_correction.predecessor_record")
        for field in ("provenance_id", "authority", "source_locator", "source_unit_evidence"):
            if previous[field] != record[field]:
                raise CheckFailure(f"reader_correction.predecessor_record: wrong {field}")
        previous_artifact = exact_object(previous["restoration_artifact"],
            {"path", "bytes", "physical_lines", "sha256", "content_token_sha256", "content_token_comparison"},
            "reader_correction.predecessor_record.restoration_artifact")
        if previous_artifact["path"] != record["restoration_artifact"]["path"]:
            raise CheckFailure("reader_correction.predecessor_record: wrong artifact path")
        exact_sha256(previous["restoration_artifact"]["sha256"], "predecessor artifact.sha256")
        if version == 1:
            if previous["restoration_artifact"]["content_token_sha256"] != record["reader_correction"]["source_content_token_sha256"]:
                raise CheckFailure("reader_correction.predecessor_record: wrong frozen content digest")
            return
        if previous["disposition"] != "full reconstruction":
            raise CheckFailure("reader_correction.predecessor_record: false corrected disposition")
        prior_correction = exact_object(previous["reader_correction"], READER_CORRECTION_FIELDS,
                                        "predecessor reader_correction")
        link = prior_correction["predecessor_record"]


def reader_source_line_map(record: dict[str, Any]) -> dict[int, int | None]:
    """Map 1-based reader lines after validate_record; this helper grants no admission.

    Corrected hunk lines have no original locator, even if a token within them
    happens to be unchanged. Callers must validate the record before using this
    projection, as both the namespace checker and audit-table reader do.
    """
    start = record["source_locator"]["start_line"]
    count = record["restoration_artifact"]["physical_lines"]
    if record["schema_version"] != 4:
        return {line: start + line - 1 for line in range(1, count + 1)}
    mapping: dict[int, int | None] = {}
    source_cursor = reader_cursor = 0
    for edit in record["reader_correction"]["edits"]:
        ss, se = edit["source_range"]
        rs, re_ = edit["reader_range"]
        for offset in range(rs - reader_cursor):
            mapping[reader_cursor + offset + 1] = start + source_cursor + offset
        for line in range(rs + 1, re_ + 1):
            mapping[line] = None
        source_cursor, reader_cursor = se, re_
    for offset in range(count - reader_cursor):
        mapping[reader_cursor + offset + 1] = start + source_cursor + offset
    return mapping


def validate_reader_correction(
    record: dict[str, Any], record_path: Path, repo_root: Path,
    start: int, end: int, source_interval: list[bytes],
) -> None:
    correction = exact_object(record["reader_correction"], READER_CORRECTION_FIELDS,
                              "reader_correction")
    if correction["kind"] != "candidate corrected reader interval":
        raise CheckFailure("reader_correction.kind: candidate corrected reader interval required")
    if record["disposition"] != "full reconstruction":
        raise CheckFailure("reader_correction: disposition must be full reconstruction, not transcription/layout")
    if record["artifact_line_standing"] != "reader-facing content":
        raise CheckFailure("reader_correction: reader-facing content required")
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9._:-]*", nonempty_string(correction["correction_id"], "reader_correction.correction_id")):
        raise CheckFailure("reader_correction.correction_id: invalid stable ID")

    policy_path, policy = _correction_file(correction["policy_authority"], repo_root,
                                           "reader_correction.policy_authority", locator=True)
    if policy["path"] != CORRECTION_POLICY_PATH or policy["locator"] != CORRECTION_POLICY_LOCATOR:
        raise CheckFailure("reader_correction.policy_authority: wrong correction policy/locator")
    policy_text = policy_path.read_text(encoding="utf-8")
    if ("## " + CORRECTION_POLICY_LOCATOR) not in policy_text or CORRECTION_POLICY_TEXT not in " ".join(policy_text.split()):
        raise CheckFailure("reader_correction.policy_authority: direct-correction authorization absent")
    rationale_path, _ = _correction_file(correction["rationale"], repo_root,
                                        "reader_correction.rationale", locator=True)
    if rationale_path in {record_path.resolve(), policy_path}:
        raise CheckFailure("reader_correction.rationale: separate rationale artifact required")

    ids = correction["affected_ids"]
    if (not isinstance(ids, list) or not ids
            or any(not isinstance(item, str) or not item for item in ids)
            or ids != sorted(set(ids)) or record["provenance_id"] not in ids):
        raise CheckFailure("reader_correction.affected_ids: sorted unique IDs including this source ID required")
    known_ids = {record["provenance_id"]}
    known_ids.update(f"source-unit:{n}" for n in record["source_unit_evidence"]["unit_ordinals"])
    for name in ("new-content", "depth-gaps", "defects", "apparatus"):
        register = repo_root / "spec" / "registers" / f"{name}.csv"
        if register.is_file():
            with register.open(encoding="utf-8-sig", newline="") as handle:
                known_ids.update(row["id"] for row in csv.DictReader(handle) if row.get("id"))
    if set(ids) - known_ids:
        raise CheckFailure("reader_correction.affected_ids: unknown affected ID")
    _validate_correction_predecessor(record, record_path, repo_root)

    artifact = exact_object(record["restoration_artifact"],
                            {"path", "bytes", "physical_lines", "sha256",
                             "content_token_sha256", "content_token_comparison"},
                            "restoration_artifact")
    display, path = contained_file(repo_root, artifact["path"], "restoration_artifact.path",
                                   Path("handbook/restoration"))
    if path.name != f"inherited-{start:05d}-{end:05d}.tex":
        raise CheckFailure("reader_correction: artifact filename must encode its original source locator")
    if record["handbook_destination"]["file"] != artifact["path"]:
        raise CheckFailure("reader_correction: destination must name the corrected reader artifact")
    raw = path.read_bytes()
    lines = physical_lines(raw, display)
    if len(raw) != exact_integer(artifact["bytes"], "restoration_artifact.bytes"):
        raise CheckFailure("reader_correction: artifact byte count mismatch")
    if len(lines) != exact_integer(artifact["physical_lines"], "restoration_artifact.physical_lines"):
        raise CheckFailure("reader_correction: artifact line count mismatch")
    if sha256(raw) != exact_sha256(artifact["sha256"], "restoration_artifact.sha256"):
        raise CheckFailure("reader_correction: artifact digest mismatch")
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CheckFailure("reader_correction: artifact is not UTF-8") from exc
    if raw.startswith(b"\xef\xbb\xbf"):
        raise CheckFailure("reader_correction: added UTF-8 BOM")
    if artifact["content_token_comparison"] != CORRECTED_CONTENT_COMPARISON:
        raise CheckFailure("reader_correction: exact corrected-content comparison rule required")
    source_content = correction_slice_bytes(source_interval, "frozen correction interval")
    reader_content = correction_slice_bytes(lines, "corrected reader artifact")
    if sha256(source_content) != exact_sha256(correction["source_content_token_sha256"], "reader_correction.source_content_token_sha256"):
        raise CheckFailure("reader_correction: frozen content digest mismatch")
    if sha256(reader_content) != exact_sha256(artifact["content_token_sha256"], "restoration_artifact.content_token_sha256"):
        raise CheckFailure("reader_correction: current content digest mismatch")

    edits = correction["edits"]
    if not isinstance(edits, list) or not edits:
        raise CheckFailure("reader_correction.edits: nonempty edit map required")
    source_cursor = reader_cursor = 0
    for index, value in enumerate(edits):
        where = f"reader_correction.edits[{index}]"
        edit = exact_object(value, {"source_range", "reader_range", "source_sha256",
                                    "reader_sha256", "reason"}, where)
        bounds = []
        for field, size in (("source_range", len(source_interval)), ("reader_range", len(lines))):
            span = edit[field]
            if not isinstance(span, list) or len(span) != 2:
                raise CheckFailure(f"{where}.{field}: two half-open line offsets required")
            low, high = [exact_integer(n, f"{where}.{field}") for n in span]
            if low > high or high > size:
                raise CheckFailure(f"{where}.{field}: out-of-range/reversed range")
            bounds.append((low, high))
        (ss, se), (rs, re_) = bounds
        if ss < source_cursor or rs < reader_cursor:
            raise CheckFailure(f"{where}: overlapping or unordered edits")
        old_gap = correction_slice_bytes(source_interval[source_cursor:ss], where)
        new_gap = correction_slice_bytes(lines[reader_cursor:rs], where)
        if old_gap != new_gap:
            raise CheckFailure(f"{where}: unexplained change in unchanged span")
        old = correction_slice_bytes(source_interval[ss:se], where)
        new = correction_slice_bytes(lines[rs:re_], where)
        if old == new:
            raise CheckFailure(f"{where}: empty/no-op correction")
        for field, content in (("source_sha256", old), ("reader_sha256", new)):
            if sha256(content) != exact_sha256(edit[field], f"{where}.{field}"):
                raise CheckFailure(f"{where}.{field}: slice digest mismatch")
        nonempty_string(edit["reason"], f"{where}.reason")
        source_cursor, reader_cursor = se, re_
    if correction_slice_bytes(source_interval[source_cursor:], "source tail") != correction_slice_bytes(lines[reader_cursor:], "reader tail"):
        raise CheckFailure("reader_correction: unexplained change in unchanged tail")


def validate_destination(record: dict[str, Any], repo_root: Path) -> None:
    destination = exact_object(
        record["handbook_destination"],
        {"status", "file", "stable_label", "reason"},
        "handbook_destination",
    )
    one_of(destination["status"], {"open/missing"}, "handbook_destination.status")
    nonempty_string(destination["reason"], "handbook_destination.reason")
    raw_file = destination["file"]
    raw_label = destination["stable_label"]
    if not isinstance(raw_file, str) or not isinstance(raw_label, str):
        raise CheckFailure("handbook_destination file and stable_label must be strings")
    if not raw_file:
        if raw_label:
            raise CheckFailure(
                "handbook_destination.stable_label cannot be set without a file"
            )
        return
    display, path = contained_file(
        repo_root, raw_file, "handbook_destination.file", Path("handbook")
    )
    if not raw_label:
        return
    label = nonempty_string(raw_label, "handbook_destination.stable_label")
    if not LABEL_RE.fullmatch(label):
        raise CheckFailure("handbook_destination.stable_label has an invalid label form")
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise CheckFailure(f"{display}: cannot read destination: {exc}") from exc
    if f"{{{label}}}" not in text:
        raise CheckFailure(f"handbook destination does not contain stable label {label!r}")


def validate_statuses(record: dict[str, Any]) -> None:
    completeness = exact_object(record["completeness"], COMPLETENESS_FIELDS, "completeness")
    for field, value in completeness.items():
        one_of(value, {"pending", "pass", "fail", "not applicable"}, f"completeness.{field}")
    if any(value != "pending" for value in completeness.values()):
        raise CheckFailure("all completeness dimensions must remain pending in this restoration stage")

    verification = exact_object(record["verification"], VERIFICATION_FIELDS, "verification")
    for field, value in verification.items():
        one_of(value, {"pending", "pass", "fail"}, f"verification.{field}")
    if verification["source"] != "pass" or verification["static"] != "pass":
        raise CheckFailure("source and static verification must record pass after this checker succeeds")
    for field in VERIFICATION_FIELDS - {"source", "static"}:
        if verification[field] != "pending":
            raise CheckFailure(f"verification.{field} must remain pending")

    evidence = record["verification_evidence"]
    if not isinstance(evidence, list) or len(evidence) != 2:
        raise CheckFailure("verification_evidence must contain exactly source and static evidence")
    kinds: set[str] = set()
    for index, item in enumerate(evidence):
        item = exact_object(
            item, {"kind", "checker", "command", "scope"}, f"verification_evidence[{index}]"
        )
        kind = one_of(item["kind"], {"source", "static"}, f"verification_evidence[{index}].kind")
        if kind in kinds:
            raise CheckFailure(f"verification_evidence: duplicate {kind!r} evidence")
        kinds.add(kind)
        if item["checker"] != "tools/check_inherited_restoration.py":
            raise CheckFailure(f"verification_evidence[{index}].checker is not this checker")
        nonempty_string(item["command"], f"verification_evidence[{index}].command")
        nonempty_string(item["scope"], f"verification_evidence[{index}].scope")
        if record["schema_version"] == 4 and item["scope"] != CORRECTION_VERIFICATION_SCOPES[kind]:
            raise CheckFailure("version 4 verification scope must state candidate validation, not exact transcription/admission")
    if kinds != {"source", "static"}:
        raise CheckFailure("verification_evidence must cover source and static exactly")


def validate_reader_layout(record: dict[str, Any], repo_root: Path) -> None:
    provenance_id = record["provenance_id"]
    expected_layout = READER_LAYOUTS[provenance_id]
    layout = exact_object(record["reader_layout"], READER_LAYOUT_FIELDS, "reader_layout")
    if layout != expected_layout:
        raise CheckFailure("reader_layout does not match the exact governed reader layout")

    artifact_path = repo_root / record["restoration_artifact"]["path"]
    artifact_text = artifact_path.read_text(encoding="utf-8")
    if artifact_text.count(layout["source_part_command"]) != 1:
        raise CheckFailure("reader_layout source part command must occur exactly once in its artifact")
    if layout["source_label"]:
        if artifact_text.count(rf"\label{{{layout['source_label']}}}") != 1:
            raise CheckFailure(
                "reader_layout source part label must occur exactly once in its artifact"
            )
    elif layout["source_label_line"] != 0 or re.search(
        r"\\label\s*\{part:[^{}]+\}", artifact_text
    ):
        raise CheckFailure(
            "reader_layout label-less source part must use line 0 and contain no part label"
        )
    if provenance_id in {
        "SRC-06049-06069",
        "SRC-09080-09098",
        "SRC-10060-10088",
        "SRC-12970-12988",
    }:
        if len(re.findall(r"\\part\s*\*?\s*\{", artifact_text)) != 1:
            raise CheckFailure(
                "reader_layout direct public artifact must contain exactly one part command"
            )
        part_labels = re.findall(r"\\label\s*\{(part:[^{}]+)\}", artifact_text)
        if part_labels != [layout["source_label"]]:
            raise CheckFailure(
                "reader_layout direct public artifact must contain exactly one part label"
            )

    wrapper_display, wrapper_path = contained_file(
        repo_root,
        layout["wrapper_path"],
        "reader_layout.wrapper_path",
        Path("handbook/restoration"),
    )
    artifact_input = Path(record["restoration_artifact"]["path"]).with_suffix("").as_posix()
    if not artifact_input.startswith("handbook/"):
        raise CheckFailure("reader-layout restoration artifact must be under handbook")
    artifact_input = artifact_input.removeprefix("handbook/")
    expected_wrapper = (
        rf"\begin{{inheritedrestorationscope}}{{{provenance_id}}}" + "\n"
        + rf"\input{{{artifact_input}}}" + "\n"
        + r"\end{inheritedrestorationscope}" + "\n"
    )
    if wrapper_path.read_text(encoding="utf-8") != expected_wrapper:
        raise CheckFailure(f"{wrapper_display}: reader-layout wrapper is not the exact three-line form")

    public_display, public_path = contained_file(
        repo_root,
        layout["public_part_file"],
        "reader_layout.public_part_file",
        Path("handbook/parts"),
    )
    public_text = public_path.read_text(encoding="utf-8")
    wrapper_input_path = Path(layout["wrapper_path"]).with_suffix("").as_posix()
    if not wrapper_input_path.startswith("handbook/"):
        raise CheckFailure("reader-layout wrapper must be under handbook")
    wrapper_input = rf"\input{{{wrapper_input_path.removeprefix('handbook/')}}}"
    if public_text.count(wrapper_input) != 1:
        raise CheckFailure(f"{public_display}: governed reader-layout wrapper must be input once")
    if provenance_id in {
        "SRC-06049-06069",
        "SRC-09080-09098",
        "SRC-10060-10088",
        "SRC-12970-12988",
    }:
        direct_inputs = [
            match.group(1).strip().removesuffix(".tex")
            for match in re.finditer(r"\\input\s*\{([^{}]+)\}", public_text)
        ]
        if not direct_inputs or direct_inputs[0] != wrapper_input_path.removeprefix("handbook/"):
            raise CheckFailure(
                f"{public_display}: governed direct-public wrapper must be the first direct input"
            )
        if re.search(r"\\part(?!\*)\s*\{", public_text):
            raise CheckFailure(
                f"{public_display}: direct public part must come only from the exact artifact"
            )
        forbidden_driver_labels = {
            "SRC-06049-06069": r"part:(?:p03|model-theory)",
            "SRC-09080-09098": r"part:(?:p05|incompleteness)",
            "SRC-10060-10088": r"part:(?:p06|set-theory)",
            "SRC-12970-12988": r"part:(?:p08|nonclassical)",
        }[provenance_id]
        if re.search(
            rf"\\label\s*\{{(?:{forbidden_driver_labels})\}}", public_text
        ):
            raise CheckFailure(
                f"{public_display}: direct public part cannot acquire a driver label alias"
            )
    else:
        public_command = (
            rf"\part{{{layout['public_part_title']}}}"
            rf"\label{{{layout['public_part_label']}}}"
        )
        public_surface = {
            "part:p02": "Part II",
            "part:p04": "Part IV",
            "part:p07": "Part VII",
            "part:p12": "Part XII",
        }[layout["public_part_label"]]
        if public_text.count(public_command) != 1:
            raise CheckFailure(
                f"{public_display}: exact public {public_surface} binding must occur once"
            )
        if public_text.index(public_command) > public_text.index(wrapper_input):
            raise CheckFailure(
                f"{public_display}: governed wrapper must follow the public {public_surface} binding"
            )
        part_commands = re.findall(r"\\part(?!\*)\s*\{([^{}]+)\}", public_text)
        if part_commands != [layout["public_part_title"]]:
            raise CheckFailure(
                f"{public_display}: exact public {public_surface} part command is the sole driver part"
            )
        if layout["source_label"] != layout["public_part_label"] and re.search(
            rf"\\label\s*\{{{re.escape(layout['source_label'])}\}}", public_text
        ):
            raise CheckFailure(
                f"{public_display}: driver cannot acquire a source part label alias"
            )


def validate_reader_appendix_layout(
    record: dict[str, Any], repo_root: Path
) -> None:
    provenance_id = record["provenance_id"]
    expected_layout = READER_APPENDIX_LAYOUTS[provenance_id]
    layout = exact_object(
        record["reader_appendix_layout"],
        READER_APPENDIX_LAYOUT_FIELDS,
        "reader_appendix_layout",
    )
    if layout != expected_layout:
        raise CheckFailure(
            "reader_appendix_layout does not match the exact governed reader appendix layout"
        )

    artifact_path = repo_root / record["restoration_artifact"]["path"]
    artifact_text = artifact_path.read_text(encoding="utf-8")
    if layout["source_appendix_command"]:
        if artifact_text.count(layout["source_appendix_command"]) != 1:
            raise CheckFailure(
                "reader_appendix_layout source appendix command must occur exactly once in its artifact"
            )
    elif layout["source_appendix_line"] != 0 or re.search(
        r"\\appendix(?![A-Za-z@])", artifact_text
    ):
        raise CheckFailure(
            "reader_appendix_layout continuation must use line 0 and contain no appendix command"
        )
    if layout["source_chapter_command"]:
        if artifact_text.count(layout["source_chapter_command"]) != 1:
            raise CheckFailure(
                "reader_appendix_layout source chapter command must occur exactly once in its artifact"
            )
    elif layout["source_chapter_line"] != 0 or re.search(
        r"\\chapter(?![A-Za-z@])", artifact_text
    ):
        raise CheckFailure(
            "reader_appendix_layout section continuation must use chapter line 0 and contain no chapter command"
        )
    actual_labels = re.findall(r"\\label\s*\{([^{}]+)\}", artifact_text)
    if actual_labels != layout["source_labels"]:
        raise CheckFailure(
            "reader_appendix_layout source labels must occur exactly once and in order"
        )

    wrapper_display, wrapper_path = contained_file(
        repo_root,
        layout["wrapper_path"],
        "reader_appendix_layout.wrapper_path",
        Path("handbook/restoration"),
    )
    artifact_input = Path(record["restoration_artifact"]["path"]).with_suffix("").as_posix()
    if not artifact_input.startswith("handbook/"):
        raise CheckFailure("reader-appendix restoration artifact must be under handbook")
    artifact_input = artifact_input.removeprefix("handbook/")
    expected_wrapper = (
        rf"\begin{{inheritedrestorationscope}}{{{provenance_id}}}" + "\n"
        + rf"\input{{{artifact_input}}}" + "\n"
        + r"\end{inheritedrestorationscope}" + "\n"
    )
    if wrapper_path.read_text(encoding="utf-8") != expected_wrapper:
        raise CheckFailure(
            f"{wrapper_display}: reader-appendix wrapper is not the exact three-line form"
        )

    public_display, public_path = contained_file(
        repo_root,
        layout["public_part_file"],
        "reader_appendix_layout.public_part_file",
        Path("handbook/parts"),
    )
    public_text = public_path.read_text(encoding="utf-8")
    public_command = (
        rf"\part{{{layout['public_part_title']}}}"
        rf"\label{{{layout['public_part_label']}}}"
    )
    if public_text.count(public_command) != 1:
        raise CheckFailure(
            f"{public_display}: exact public Part XII binding must occur once"
        )
    wrapper_input_path = Path(layout["wrapper_path"]).with_suffix("").as_posix()
    if not wrapper_input_path.startswith("handbook/"):
        raise CheckFailure("reader-appendix wrapper must be under handbook")
    wrapper_input = rf"\input{{{wrapper_input_path.removeprefix('handbook/')}}}"
    aggregator_input = r"\input{parts/p12/automation-and-mechanization}"
    if public_text.count(wrapper_input) != 1:
        raise CheckFailure(
            f"{public_display}: governed reader-appendix wrapper must be input once"
        )
    if public_text.count(aggregator_input) != 1:
        raise CheckFailure(
            f"{public_display}: editorial aggregator must be input once"
        )
    if public_text.index(public_command) > public_text.index(wrapper_input):
        raise CheckFailure(
            f"{public_display}: governed appendix wrapper must follow the public Part XII binding"
        )
    if public_text.index(wrapper_input) > public_text.index(aggregator_input):
        raise CheckFailure(
            f"{public_display}: governed appendix wrapper must precede the editorial aggregator"
        )


def validate_record(record: Any, record_path: Path, repo_root: Path) -> str:
    if not isinstance(record, dict):
        raise CheckFailure(f"{record_path}: expected object")
    schema_version = record.get("schema_version")
    provenance_value = record.get("provenance_id")
    if type(schema_version) is not int or schema_version not in {1, 2, 3, 4}:
        raise CheckFailure("schema_version: expected integer 1, 2, 3, or 4")
    if schema_version == 4 and (not isinstance(provenance_value, str)
            or not provenance_value.startswith("SRC-")
            or provenance_value in READER_LAYOUTS
            or provenance_value in READER_APPENDIX_LAYOUTS):
        raise CheckFailure("schema_version 4 supports plain reader SRC intervals, not governed layouts/controls")
    if schema_version == 2 and provenance_value not in READER_LAYOUTS:
        raise CheckFailure(
            "schema_version 2 is reserved for the ten governed reader layouts"
        )
    if schema_version == 3 and provenance_value not in READER_APPENDIX_LAYOUTS:
        raise CheckFailure(
            "schema_version 3 is reserved for the governed reader appendix layouts"
        )
    extra_layout_fields = (
        {"reader_layout"}
        if schema_version == 2
        else {"reader_appendix_layout"}
        if schema_version == 3
        else {"reader_correction"}
        if schema_version == 4
        else set()
    )
    expected_fields = ROOT_FIELDS | extra_layout_fields
    data = exact_object(record, expected_fields, str(record_path))
    provenance_id = nonempty_string(data["provenance_id"], "provenance_id")
    if record_path.name != f"{provenance_id}.json":
        raise CheckFailure("record filename does not match provenance_id")
    if not PROVENANCE_ID_RE.fullmatch(provenance_id):
        raise CheckFailure("provenance_id must use an inherited source-map identifier form")
    one_of(
        data["artifact_line_standing"],
        {"reader-facing content", "nonprinting control syntax", "comment", "blank material"},
        "artifact_line_standing",
    )
    identity = exact_object(
        data["presentation_identity"],
        {"kind", "source_title", "description"},
        "presentation_identity",
    )
    for field, value in identity.items():
        nonempty_string(value, f"presentation_identity.{field}")
    one_of(
        data["disposition"],
        {"full transcription", "full reconstruction", "open/missing"},
        "disposition",
    )

    _raw, source_lines = validate_authority(data, repo_root)
    start, end, source_interval = validate_source_locator(data, provenance_id, source_lines)
    validate_source_unit_evidence(data, repo_root, start, end, source_lines)
    validate_audit_evidence(data, repo_root, start, end, source_lines)
    if schema_version == 4:
        validate_reader_correction(data, record_path, repo_root, start, end, source_interval)
    else:
        validate_restoration_artifact(data, repo_root, start, end, source_interval)
    validate_destination(data, repo_root)
    validate_statuses(data)
    if schema_version == 2:
        validate_reader_layout(data, repo_root)
    if schema_version == 3:
        validate_reader_appendix_layout(data, repo_root)
    owed = data["owed_artifacts"]
    if not isinstance(owed, list) or not owed:
        raise CheckFailure("owed_artifacts: expected nonempty array")
    for index, value in enumerate(owed):
        nonempty_string(value, f"owed_artifacts[{index}]")
    return provenance_id


def resolve_record(repo_root: Path, raw: Path) -> Path:
    path = raw if raw.is_absolute() else repo_root / raw
    resolved = path.resolve()
    provenance_root = (repo_root / "spec" / "provenance").resolve()
    try:
        resolved.relative_to(provenance_root)
    except ValueError as exc:
        raise CheckFailure(f"record must be under {provenance_root}: {resolved}") from exc
    if not resolved.is_file():
        raise CheckFailure(f"record does not exist: {resolved}")
    return resolved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=DEFAULT_REPO_ROOT)
    parser.add_argument("--record", type=Path, action="append")
    args = parser.parse_args(argv)
    repo_root = args.repo_root.resolve()
    raw_records = args.record
    if raw_records is None:
        raw_records = sorted(
            path
            for path in (repo_root / "spec" / "provenance").glob("*.json")
            if PROVENANCE_ID_RE.fullmatch(path.stem)
        )
    if not raw_records:
        print("RESTORATION CHECK FAILED: no provenance records found", file=sys.stderr)
        return 1

    failures: list[str] = []
    passed: list[str] = []
    for raw_record in raw_records:
        try:
            path = resolve_record(repo_root, raw_record)
            provenance_id = validate_record(load_json(path), path, repo_root)
        except CheckFailure as exc:
            failures.append(f"{raw_record}: {exc}")
        else:
            passed.append(provenance_id)
            print(f"RESTORATION CHECK OK: {provenance_id}")
    if failures:
        print("RESTORATION CHECK FAILED", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1
    print(f"verified restoration records: {len(passed)}")
    print(
        "verification boundary: source/static PASS only; independent source, "
        "build, visual, and human review remain pending"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
