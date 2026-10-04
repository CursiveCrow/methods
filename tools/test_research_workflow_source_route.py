#!/usr/bin/env python3
"""Fail-closed route and byte tests for exact source lines 15030--15092."""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
AUTHORITY = ROOT / "source/formal-logic-reference.tex"
INTERVALS = (
    ("SRC-15030-15050", 15030, 15050, 878, "1fd2ee5d49ddbd9ecd40b3e02f9af40c029d5bc01369436214c3e7d8218490aa", 857, "7212b17e1545b112490911617cc13f6339378ee34e7d55147646a894360a2a8d"),
    ("SRC-15051-15068", 15051, 15068, 675, "eb9d8095baf6ef703f62798d23e95a4713cad0b4f3c75dd7e6abe9f69773d2c5", 657, "614589e090319c8f2283315c1560f7bbaa3d90d12b7f4913fb2fab8f7aa0e6a8"),
    ("SRC-15069-15077", 15069, 15077, 428, "16219b6456666851457ed0ba2489ae5efe4e846469d33788c6d9a3a8af0cf358", 419, "cfbe35f374ad3dafe05907a1d6651be7bcec411d7c13e3b72588d43143711ff6"),
    ("SRC-15078-15091", 15078, 15091, 696, "e1d506c85b79c841a54581564e763d2970ee4d2308a2118aa117bc606112446b", 682, "b1ef867413cc6402b759a8fe72703b84276e164f623586599754ba177ac793a5"),
    ("SEP-15092-15092", 15092, 15092, 2, "7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6", 1, "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"),
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


class ResearchWorkflowSourceRouteTests(unittest.TestCase):
    def test_exact_artifacts_and_wrappers_match_the_frozen_authority(self) -> None:
        authority_lines = AUTHORITY.read_bytes().splitlines(keepends=True)
        concatenated = bytearray()
        for provenance_id, start, end, raw_bytes, raw_hash, lf_bytes, lf_hash in INTERVALS:
            with self.subTest(provenance_id=provenance_id):
                raw = b"".join(authority_lines[start - 1 : end])
                self.assertEqual(len(raw), raw_bytes)
                self.assertEqual(sha256(raw), raw_hash)
                normalized = raw.replace(b"\r\n", b"\n")
                self.assertEqual(len(normalized), lf_bytes)
                self.assertEqual(sha256(normalized), lf_hash)
                artifact = HANDBOOK / f"restoration/inherited-{provenance_id[4:]}.tex"
                self.assertEqual(artifact.read_bytes(), normalized)
                wrapper = HANDBOOK / f"restoration/scope-{provenance_id}.tex"
                self.assertEqual(
                    wrapper.read_text(encoding="utf-8"),
                    f"\\begin{{inheritedrestorationscope}}{{{provenance_id}}}\n"
                    f"\\input{{restoration/inherited-{provenance_id[4:]}}}\n"
                    "\\end{inheritedrestorationscope}\n",
                )
                concatenated.extend(normalized)
        self.assertEqual(len(concatenated), 2616)
        self.assertEqual(
            sha256(bytes(concatenated)),
            "84965b2e614e92da88da16f69f254af7b5ae5493a7ebf5d7f218d92bd769cda8",
        )
        self.assertNotIn(b"\\appendix", concatenated)

    def test_five_exact_wrappers_precede_the_editorial_aggregator(self) -> None:
        direct = inputs(HANDBOOK / "parts/p12.tex")
        expected = [f"restoration/scope-{item[0]}" for item in INTERVALS]
        start = direct.index("restoration/scope-SRC-14991-15029") + 1
        self.assertEqual(
            direct[start : start + 6],
            expected + ["parts/p12/automation-and-mechanization"],
        )
        for item in expected:
            self.assertEqual(direct.count(item), 1)

    def test_exact_labels_are_unique_on_the_reachable_surface(self) -> None:
        route = reachable(HANDBOOK / "main.tex")
        live = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(route)
            if path.suffix == ".tex"
        )
        labels = re.findall(r"\\label\s*\{([^{}]+)\}", live)
        for label in (
            "ch:research-workflow",
            "sec:research-workflow-01",
            "sec:research-workflow-02",
            "sec:research-workflow-03",
            "sec:research-workflow-04",
        ):
            with self.subTest(label=label):
                self.assertEqual(labels.count(label), 1)

    def test_editorial_workflow_does_not_replace_exact_research_chapter(self) -> None:
        text = (HANDBOOK / "parts/p12/formal-practice-supplement.tex").read_text(
            encoding="utf-8"
        )
        self.assertRegex(
            text,
            r"separately attributed OPEN additions[\s\S]*do not replace[\s\S]*Research Workflow and Reproducibility",
        )


if __name__ == "__main__":
    unittest.main()
