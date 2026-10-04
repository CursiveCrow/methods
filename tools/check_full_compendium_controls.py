#!/usr/bin/env python3
"""Run and aggregate non-editorial integrity and coverage controls."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(arguments: list[str]) -> int:
    print(f"== {' '.join(arguments)} ==")
    try:
        completed = subprocess.run(arguments, cwd=ROOT, check=False)
    except OSError as exc:
        print(f"control could not start: {exc}")
        return 1
    return completed.returncode


def command_list(python: str) -> list[list[str]]:
    """Return controls with live-tree equality checked before and after all work."""

    return [
        [python, "tools/check_handbook_construction_snapshot.py"],
        [python, "tools/check_inherited_corpus.py"],
        [python, "tools/check_handbook_audit_snapshot.py"],
        [python, "tools/build_handbook_source_inventory.py", "--check"],
        [
            python,
            "tools/build_handbook_source_inventory.py",
            "--check-construction",
        ],
        [python, "tools/check_compendium_volume_manifest.py"],
        [
            python,
            "tools/source_unit_inventory.py",
            "--source",
            "source/formal-logic-reference.tex",
            "--csv",
            "spec/source-unit-inventory.csv",
            "--summary",
            "spec/source-unit-inventory.md",
            "--check",
        ],
        [python, "tools/build_inherited_source_map.py", "--check"],
        [python, "tools/build_source_unit_audit_crosswalk.py", "--check"],
        [python, "tools/build_handbook_unit_reverse_ledger.py", "--check"],
        [python, "tools/build_coverage_manifest.py", "--check"],
        [python, "tools/build_acquisition_gap_manifest.py", "--check"],
        [python, "tools/build_register_obligation_manifest.py", "--check"],
        [python, "tools/build_register_obligation_closure.py", "--check"],
        [python, "tools/check_presentation_packet.py", "--self-test"],
        [python, "tools/check_presentation_packet_corpus.py", "--self-test"],
        [python, "tools/check_presentation_packet_corpus.py"],
        [
            python,
            "tools/check_transcription_audit_coverage.py",
            "--source",
            "source/formal-logic-reference.tex",
            "--audit",
            "spec/research/full-transcription-audit-p01-p04.md",
            "--audit",
            "spec/research/full-transcription-audit-p05-p08.md",
            "--audit",
            "spec/research/full-transcription-audit-p09-p14.md",
        ],
        [python, "tools/check_handbook_construction_snapshot.py"],
    ]


def run_all(commands: list[list[str]]) -> list[tuple[list[str], int]]:
    """Run every independent control and return all nonzero results."""

    failures: list[tuple[list[str], int]] = []
    for command in commands:
        returncode = run(command)
        if returncode != 0:
            failures.append((command, returncode))
    return failures


def main() -> int:
    failures = run_all(command_list(sys.executable))
    if failures:
        print(f"full-compendium controls: FAIL ({len(failures)} control runs)")
        for command, returncode in failures:
            print(f"- exit {returncode}: {' '.join(command[1:])}")
        print("COMPENDIUM CONTENT/RESTORATION/READINESS: OPEN")
        print(
            "The failures are reported independently; no passing control "
            "compensates for another control's failure."
        )
        return 1
    print("CONTROL CONSISTENCY CHECK OK")
    print("COMPENDIUM CONTENT/RESTORATION/READINESS: OPEN")
    print(
        "These controls establish only the stated structural and byte-integrity "
        "properties; they do not certify semantic truth or completeness."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
