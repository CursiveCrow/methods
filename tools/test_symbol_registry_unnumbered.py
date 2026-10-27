"""Focused regression tests for unnumbered scopes and typed local evidence.

Default: load tools/symbol_registry.py when this test is integrated beside it.
Pass --candidate PATH to check a staged module before shared files are changed.
"""
from pathlib import Path
import importlib.util
import json
import sys
import tempfile
import unittest

repo_tools = Path.cwd() / "tools"
if not (repo_tools / "check.py").is_file():
    repo_tools = Path(__file__).resolve().parent
sys.path.insert(0, str(repo_tools))
candidate = Path(__file__).with_name("symbol_registry.py")
if "--candidate" in sys.argv:
    i = sys.argv.index("--candidate")
    candidate = Path(sys.argv[i+1])
    del sys.argv[i:i+2]
spec = importlib.util.spec_from_file_location("tested_symbol_registry", candidate)
registry = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = registry
spec.loader.exec_module(registry)

class UnnumberedRegions(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        (self.base/"parts/p01").mkdir(parents=True)
        (self.base/"bib").mkdir()
        (self.base/"main.tex").write_text("\\input{frontmatter}\n\\input{parts/p01/chapter}\n", encoding="utf-8")
        (self.base/"frontmatter.tex").write_text(r"""\chapter*{How to use the book}
\section*{Notation}\label{sec:front-notation}
\(a:=b\) is a displayed form.
\section*{Next}\label{sec:front-next}
Other text.
""", encoding="utf-8")
        (self.base/"parts/p01/chapter.tex").write_text(r"""\chapter{Notation}\label{sec:p01-notation}
\begin{hbconvention}{def:p01-mention}{Displayed signs}
Displayed register entries mention their signs and assert no relation.
\end{hbconvention}
\begin{hbdefinition}{def:p01-example}{A notation definition}
A second explicit typed declaration.
\end{hbdefinition}
""", encoding="utf-8")
        (self.base/"bib/handbook.bib").write_text("@misc{ExistingSource, title={Existing source}}\n",encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def resolver(self, source=None):
        scopes = {}
        if source is not None:
            scopes["sec:front-notation"] = {
                "presentation": "Explicit register-mention convention in unnumbered matter.",
                "regions": [{"anchor":"sec:front-notation"}],
                "overrides": [{"glyph":r"\(a:=b\)","local_role":"displayed register entry",
                    "first_use":"sec:front-notation","broader_scope":"global",
                    "broader_role":"definition","reason":"The local convention explicitly declares the mention reading.",
                    "source":source}]}
        return registry.Resolver(self.base, bindings={"schema_version":1,"scopes":scopes})

    def test_front_label_resolves_and_contains_its_first_use(self):
        res = self.resolver()
        front = res.resolve("sec:front-notation")
        self.assertIsNone(front.part)
        self.assertTrue(front.regions)
        self.assertTrue(res.contains(front,"sec:front-notation"))
        self.assertFalse(res.contains(front,"sec:front-next"))

    def test_front_overlap_uses_real_regions_and_excludes_numeric_parts(self):
        res = self.resolver()
        front = res.resolve("sec:front-notation")
        for scope in (res.resolve("P1.1"),res.resolve("sec:p01-notation"),res.resolve("sec:front-next")):
            self.assertFalse(res.overlaps(front,scope))
            self.assertFalse(res.overlaps(scope,front))
        self.assertTrue(res.overlaps(front,front))
        self.assertTrue(res.overlaps(front,res.resolve("global")))
        self.assertTrue(res.overlaps(res.resolve("global"),front))

    def test_body_numeric_overlap_is_preserved(self):
        res = self.resolver()
        self.assertTrue(res.overlaps(res.resolve("sec:p01-notation"),res.resolve("P1.1")))

    def test_typed_local_convention_and_definition_are_valid_evidence(self):
        for source in ("def:p01-mention","def:p01-example","ExistingSource"):
            with self.subTest(source=source):
                res = self.resolver(source)
                local = {"glyph":r"\(a:=b\)","role":"displayed register entry","first_use":"sec:front-notation","_scope":res.resolve("sec:front-notation")}
                broad = {"scope":"global","role":"definition","_scope":res.resolve("global")}
                self.assertTrue(res.authorized_override(local,broad))

    def test_unknown_ambiguous_and_untyped_evidence_fail_closed(self):
        for source in ("arbitrary prose","def:missing","sec:p01-notation"):
            with self.subTest(source=source), self.assertRaises(registry.RegistryError):
                self.resolver(source).resolve("sec:front-notation")
        path = self.base/"parts/p01/chapter.tex"
        path.write_text(path.read_text(encoding="utf-8")+"\n\\begin{hbconvention}{def:p01-mention}{Duplicate}\\end{hbconvention}\n", encoding="utf-8")
        with self.assertRaises(registry.RegistryError):
            self.resolver("def:p01-mention").resolve("sec:front-notation")

    def test_front_override_does_not_cover_a_numeric_part(self):
        res = self.resolver("def:p01-mention")
        local_scope = res.resolve("sec:front-notation")
        local_scope.overrides[0]["broader_scope"] = "P1.1"
        local = {"glyph":r"\(a:=b\)","role":"displayed register entry","first_use":"sec:front-notation","_scope":local_scope}
        broad = {"scope":"P1.1","role":"definition","_scope":res.resolve("P1.1")}
        self.assertFalse(res.authorized_override(local,broad))

    def test_unknown_scope_and_empty_binding_still_fail(self):
        with self.assertRaises(registry.RegistryError): self.resolver().resolve("unknown prose scope")
        res = registry.Resolver(self.base,bindings={"schema_version":1,"scopes":{"empty":{"presentation":"Empty","regions":[]}}})
        with self.assertRaises(registry.RegistryError): res.resolve("empty")

if __name__ == "__main__": unittest.main()
