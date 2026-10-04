#!/usr/bin/env python3
"""Rendered regression for provenance-scoped source-method destinations."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:  # pragma: no cover - expressed by the class skip below
    PdfReader = None  # type: ignore[assignment]


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
PDFLATEX = shutil.which("pdflatex")

PREFIX_INPUTS = (
    "restoration/scope-SRC-06049-06069",
    "restoration/scope-SRC-06070-06137",
    "restoration/scope-SRC-06138-06242",
    "restoration/scope-SRC-06243-06331",
    "restoration/scope-SRC-06332-06421",
    "restoration/scope-SRC-06422-06431",
    "restoration/scope-SRC-06432-06493",
    "restoration/scope-SRC-06494-06509",
    "parts/p03/maps-elementarity-supplement",
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
    "parts/p03/types-ultraproducts-supplement",
    "restoration/scope-SRC-07150-07294",
    "restoration/scope-SRC-07295-07468",
)

LEGACY_METHOD = r"""
\makeatletter
\renewenvironment{method}[1][]{%
  \ifhb@inheritedrestoration\else
    \PackageError{handbook}{source method environment outside an inherited
      restoration scope}%
      {Editorial methods use hbmethod.  The source environment is reserved
       for unchanged, provenance-scoped inherited artifacts.}%
  \fi
  \if\relax\detokenize{#1}\relax\hbsourcemethod\else\hbsourcemethod[#1]\fi
}{\endhbsourcemethod}
\makeatother
"""


def fixture_document(*, legacy: bool) -> str:
    inputs = "\n".join(rf"\input{{{value}}}" for value in PREFIX_INPUTS)
    mutation = LEGACY_METHOD if legacy else ""
    return rf"""\documentclass[11pt]{{book}}
\usepackage{{handbook}}
\usepackage[backend=biber,style=alphabetic]{{biblatex}}
\addbibresource{{bib/handbook.bib}}
\hypersetup{{pdftitle={{Source method anchor fixture}}}}
{mutation}
\begin{{document}}
\setcounter{{part}}{{2}}
\setcounter{{chapter}}{{16}}
\setcounter{{page}}{{199}}
{inputs}
\end{{document}}
"""


@unittest.skipUnless(
    PDFLATEX and PdfReader is not None,
    "pdflatex and pypdf are required for source-method anchor tests",
)
class SourceMethodAnchorTests(unittest.TestCase):
    def compile(self, *, legacy: bool) -> tuple[PdfReader, str, str]:
        temporary = tempfile.TemporaryDirectory(prefix="source-method-anchor-")
        self.addCleanup(temporary.cleanup)
        build = Path(temporary.name)
        (build / "fixture.tex").write_text(
            fixture_document(legacy=legacy), encoding="utf-8", newline="\n"
        )
        env = os.environ.copy()
        env["TEXINPUTS"] = str(HANDBOOK) + os.pathsep
        env["BIBINPUTS"] = str(HANDBOOK) + os.pathsep
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
            timeout=180,
        )
        output = completed.stdout + completed.stderr
        if "Windows API error 5: Access is denied" in output:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        self.assertEqual(completed.returncode, 0, output)
        reader = PdfReader(str(build / "fixture.pdf"))
        aux = (build / "fixture.aux").read_text(
            encoding="utf-8", errors="replace"
        )
        label = re.search(
            r"\\newlabel\{method:back-and-forth\}"
            r"\{\{.*?\}\{.*?\}\{.*?\}\{([^{}]+)\}\{\}\}",
            aux,
        )
        self.assertIsNotNone(label, aux)
        anchor = label.group(1)
        self.assertIn(anchor, reader.named_destinations)
        return reader, anchor, output

    def pages_for_method(self, reader: PdfReader, anchor: str) -> tuple[int, int]:
        visible = [
            index
            for index, page in enumerate(reader.pages)
            if re.search(
                r"Method\s+19\.13\s*\(Back-and-forth\)",
                page.extract_text() or "",
            )
        ]
        self.assertEqual(visible, [visible[0]] if visible else [])
        destination = reader.get_destination_page_number(
            reader.named_destinations[anchor]
        )
        return destination, visible[0]

    def test_exact_source_method_destination_shares_its_visible_page(self) -> None:
        reader, anchor, _ = self.compile(legacy=False)
        destination, visible = self.pages_for_method(reader, anchor)
        self.assertEqual(destination, visible)

    def test_legacy_anchor_is_wrong_page_without_layout_or_text_change(self) -> None:
        production, production_anchor, _ = self.compile(legacy=False)
        legacy, legacy_anchor, _ = self.compile(legacy=True)
        production_destination, production_visible = self.pages_for_method(
            production, production_anchor
        )
        legacy_destination, legacy_visible = self.pages_for_method(
            legacy, legacy_anchor
        )
        self.assertEqual(production_destination, production_visible)
        self.assertEqual(legacy_destination + 1, legacy_visible)
        self.assertEqual(len(production.pages), len(legacy.pages))
        self.assertEqual(
            [page.extract_text() for page in production.pages],
            [page.extract_text() for page in legacy.pages],
        )


if __name__ == "__main__":
    unittest.main()
