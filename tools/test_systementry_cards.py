#!/usr/bin/env python3
"""Public-seam regression tests for ``systementry`` card machinery."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "tools" / "check.py"
AUDIT_TABLES = ROOT / "tools" / "audit_tables.py"
HANDBOOK_TEX = ROOT / "handbook"
PDFLATEX = shutil.which("pdflatex")


REQUIRED_FIELDS = (
    "entrylanguage",
    "entrysemantics",
    "entrycalculus",
    "entryadequacy",
    "entrydecidability",
    "entrycharacteristic",
    "entrysources",
)


def card(
    label: str,
    *,
    title: str = "Fixture system",
    overrides: dict[str, str] | None = None,
    duplicate: str | None = None,
) -> str:
    """Return one complete card, optionally blanking or duplicating a field."""
    values = {
        "entrylanguage": r"\entrylanguage{Fixture formulas.}",
        "entrysemantics": r"\entrysemantics{Fixture structures.}",
        "entrycalculus": r"\entrycalculus{sheet:fixture}",
        "entryadequacy": (
            r"\entryadequacy{cited=FixtureSource}{Sound and complete.}"
        ),
        "entrydecidability": (
            r"\entrydecidability{cited=FixtureSource}{Decidable.}"
        ),
        "entrycharacteristic": (
            r"\entrycharacteristic{A characteristic fixture theorem.}"
        ),
        "entrysources": r"\entrysources{FixtureSource}",
    }
    values.update(overrides or {})
    rows: list[str] = []
    for name in REQUIRED_FIELDS:
        rows.append("  " + values[name])
        if duplicate == name:
            rows.append("  " + values[name])
    return (
        rf"\begin{{systementry}}{{{label}}}{{{title}}}" + "\n"
        + "\n".join(rows)
        + "\n"
        + r"\end{systementry}"
        + "\n"
    )


def tex_document(*cards: str) -> str:
    return (
        r"\documentclass{book}" + "\n"
        + r"\usepackage{handbook}" + "\n"
        + r"\begin{document}" + "\n"
        + r"\setcounter{part}{8}" + "\n"
        + "\n".join(cards)
        + r"\end{document}" + "\n"
    )


@unittest.skipUnless(PDFLATEX, "pdflatex is required for card integration tests")
class SystemEntryTeXTests(unittest.TestCase):
    def compile(self, source: str) -> tuple[subprocess.CompletedProcess[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        build = Path(temporary.name)
        tex = build / "fixture.tex"
        tex.write_text(source, encoding="utf-8", newline="\n")
        env = os.environ.copy()
        # A trailing path separator retains the TeX installation's defaults.
        env["TEXINPUTS"] = str(HANDBOOK_TEX) + os.pathsep
        result = subprocess.run(
            [
                str(PDFLATEX),
                "-interaction=nonstopmode",
                "-halt-on-error",
                tex.name,
            ],
            cwd=build,
            env=env,
            text=True,
            capture_output=True,
            timeout=120,
        )
        combined = result.stdout + result.stderr
        if "Windows API error 5: Access is denied" in combined:
            self.skipTest("pdflatex cannot access the sandboxed MiKTeX cache")
        return result, build

    def test_incomplete_second_card_fails_after_complete_first_card(self) -> None:
        incomplete = (
            r"\begin{systementry}{entry:fixture-second}{Incomplete second card}"
            "\n"
            r"  \entrylanguage{Only this field is present.}"
            "\n"
            r"\end{systementry}"
            "\n"
        )
        result, _ = self.compile(
            tex_document(card("entry:fixture-first"), incomplete)
        )
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn("systementry entry:fixture-second is missing", output)

    def test_blank_required_field_is_rejected(self) -> None:
        result, _ = self.compile(
            tex_document(
                card(
                    "entry:fixture-blank",
                    overrides={"entrylanguage": r"\entrylanguage{   }"},
                )
            )
        )
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        compact = "".join(output.split())
        self.assertIn(r"hasanemptyrequiredfield\entrylanguage", compact)

    def test_duplicate_required_field_is_rejected(self) -> None:
        result, _ = self.compile(
            tex_document(
                card("entry:fixture-duplicate", duplicate="entrylanguage")
            )
        )
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        compact = "".join(output.split())
        self.assertIn(r"duplicatesrequiredfield\entrylanguage", compact)

    def test_complete_card_emits_typed_complete_metadata(self) -> None:
        complete = card("entry:fixture-metadata").replace(
            r"\entrylanguage{Fixture formulas.}",
            r"\entryaliases{Fixture alias.}"
            "\n  "
            r"\entrylanguage{Fixture formulas.}",
        ).replace(
            r"\entrysources{FixtureSource}",
            r"\entrytranslations{Fixture translation.}"
            "\n  "
            r"\entryalgebra{Fixture algebra.}"
            "\n  "
            r"\entrysources{FixtureSource}",
        )
        result, build = self.compile(tex_document(complete))
        output = result.stdout + result.stderr
        self.assertEqual(result.returncode, 0, output)
        lines = (build / "fixture.hbentry").read_text(
            encoding="utf-8", errors="replace"
        ).splitlines()
        self.assertEqual(len(lines), 11, lines)
        self.assertEqual(
            lines[0],
            "CARD|entry:fixture-metadata|p08|Fixture system",
        )
        self.assertIn(
            "FIELD|entry:fixture-metadata|language|Fixture formulas.", lines
        )
        self.assertIn(
            "FIELD|entry:fixture-metadata|calculus|sheet:fixture", lines
        )
        self.assertIn(
            "STATUS|entry:fixture-metadata|adequacy|cited|FixtureSource|"
            "Sound and complete.",
            lines,
        )
        self.assertIn(
            "STATUS|entry:fixture-metadata|decidability|cited|FixtureSource|"
            "Decidable.",
            lines,
        )
        for field in (
            "aliases",
            "language",
            "semantics",
            "calculus",
            "characteristic",
            "translations",
            "algebra",
            "sources",
        ):
            self.assertTrue(
                any(line.startswith(
                    f"FIELD|entry:fixture-metadata|{field}|"
                ) for line in lines),
                (field, lines),
            )


class SystemEntryToolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "handbook" / "parts" / "p08").mkdir(parents=True)
        (self.root / "handbook" / "registry" / "calculi").mkdir(parents=True)
        (self.root / "handbook" / "registry").mkdir(parents=True, exist_ok=True)
        (self.root / "handbook" / "bib").mkdir(parents=True)
        (self.root / "handbook" / "registry" / "calculi" / "fixture.tex").write_text(
            r"\calculussheet{sheet:fixture}{Fixture}{Fixture identity.}" + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (self.root / "handbook" / "registry" / "symbols.csv").write_text(
            "glyph,macro,role,scope,precedence,first_use,notes\n",
            encoding="utf-8",
            newline="\n",
        )
        (self.root / "handbook" / "bib" / "handbook.bib").write_text(
            "@book{FixtureSource,\n  title={Fixture source},\n  year={2026}\n}\n",
            encoding="utf-8",
            newline="\n",
        )

    def write_part(self, body: str) -> None:
        (self.root / "handbook" / "parts" / "p08" / "cards.tex").write_text(
            body, encoding="utf-8", newline="\n"
        )

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

    def test_static_check_rejects_blank_required_fields(self) -> None:
        blank_forms = {
            "entrylanguage": r"\entrylanguage{   }",
            "entrysemantics": r"\entrysemantics{}",
            "entrycalculus": r"\entrycalculus{   }",
            "entryadequacy": (
                r"\entryadequacy{cited=FixtureSource}{   }"
            ),
            "entrydecidability": (
                r"\entrydecidability{cited=FixtureSource}{}"
            ),
            "entrycharacteristic": r"\entrycharacteristic{   }",
            "entrysources": r"\entrysources{}",
        }
        for field, replacement in blank_forms.items():
            with self.subTest(field=field):
                self.write_part(card(
                    f"entry:blank-{field}", overrides={field: replacement}
                ))
                result = self.run_check()
                output = result.stdout + result.stderr
                self.assertNotEqual(result.returncode, 0, output)
                self.assertIn(f"empty required field \\{field}", output)

    def test_static_check_rejects_duplicate_required_fields(self) -> None:
        for field in REQUIRED_FIELDS:
            with self.subTest(field=field):
                self.write_part(card(
                    f"entry:duplicate-{field}", duplicate=field
                ))
                result = self.run_check()
                output = result.stdout + result.stderr
                self.assertNotEqual(result.returncode, 0, output)
                self.assertIn(f"duplicates required field \\{field}", output)

    def test_audit_generator_withholds_unadmitted_card_metadata(self) -> None:
        self.write_part(
            r"\begin{hbtheorem}{thm:fixture-result}{cited=FixtureSource}"
            r"{Fixture theorem}Body.\end{hbtheorem}"
            "\n"
            + card("entry:fixture-reference")
        )
        result = subprocess.run(
            [sys.executable, str(AUDIT_TABLES), "--root", str(self.root)],
            text=True,
            capture_output=True,
            timeout=60,
        )
        output = result.stdout + result.stderr
        self.assertEqual(result.returncode, 0, output)
        generated = (
            self.root / "handbook" / "generated" / "audit-p08.tex"
        ).read_text(encoding="utf-8")
        self.assertIn("Fixture theorem", generated)
        self.assertNotIn("System entry card metadata", generated)
        self.assertNotIn("Fixture system", generated)

        first_bytes = generated.encode("utf-8")
        second_write = subprocess.run(
            [sys.executable, str(AUDIT_TABLES), "--root", str(self.root)],
            text=True,
            capture_output=True,
            timeout=60,
        )
        self.assertEqual(
            second_write.returncode, 0,
            second_write.stdout + second_write.stderr,
        )
        generated_path = (
            self.root / "handbook" / "generated" / "audit-p08.tex"
        )
        self.assertEqual(generated_path.read_bytes(), first_bytes)

        fresh = subprocess.run(
            [
                sys.executable,
                str(AUDIT_TABLES),
                "--root",
                str(self.root),
                "--check",
            ],
            text=True,
            capture_output=True,
            timeout=60,
        )
        self.assertEqual(fresh.returncode, 0, fresh.stdout + fresh.stderr)

        stale_text = generated + "% deliberate stale fixture\n"
        generated_path.write_text(
            stale_text, encoding="utf-8", newline="\n"
        )
        stale = subprocess.run(
            [
                sys.executable,
                str(AUDIT_TABLES),
                "--root",
                str(self.root),
                "--check",
            ],
            text=True,
            capture_output=True,
            timeout=60,
        )
        self.assertNotEqual(stale.returncode, 0, stale.stdout + stale.stderr)
        self.assertIn("audit-p08.tex", stale.stderr)
        self.assertEqual(generated_path.read_text(encoding="utf-8"), stale_text)


if __name__ == "__main__":
    unittest.main()
