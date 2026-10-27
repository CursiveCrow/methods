from pathlib import Path
from types import SimpleNamespace
import importlib.util
import sys
import unittest

tools=Path.cwd()/"tools"
if not (tools/"check.py").is_file(): tools=Path(__file__).resolve().parent
sys.path.insert(0,str(tools))
candidate=Path(__file__).resolve().parent
if "--candidate-dir" in sys.argv:
    i=sys.argv.index("--candidate-dir");candidate=Path(sys.argv[i+1]);del sys.argv[i:i+2]
def load(name):
    spec=importlib.util.spec_from_file_location(name,candidate/(name+".py"))
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod
registry=load("symbol_registry")
rendering=load("symbols2tex")

class UnnumberedRendering(unittest.TestCase):
    def test_deterministic_separate_group(self):
        keys=[rendering.group_key({"_scope":SimpleNamespace(part=p)}) for p in (19,None,1,"global",3)]
        self.assertEqual(sorted(keys,key=rendering.group_sort_key),["global","unnumbered",1,3,19])
        self.assertEqual(rendering.group_title("unnumbered"),"Unnumbered reader regions")
        self.assertIn("unnumbered",rendering.table_label("unnumbered"))
        self.assertNotEqual(rendering.table_label("unnumbered"),rendering.table_label("global"))

    def test_actual_mixed_render_keeps_each_row_and_group(self):
        rows=[]
        for line,p in enumerate((2,None,"global",1),2):
            rows.append({"glyph":rf"\(x_{line}\)","macro":"x","role":"letter","scope":"global" if p=="global" else "sec:test"+str(line),"precedence":"n/a","first_use":"P1.1","notes":"Recorded note.","_line":line,"_scope":SimpleNamespace(part=p)})
        text=rendering.render(rows)
        labels=[rendering.table_label(k) for k in ("global","unnumbered",1,2)]
        positions=[text.index(r"\label{"+label+"}") for label in labels]
        self.assertEqual(positions,sorted(positions))
        for row in rows: self.assertEqual(text.count(r"\label{entry:symbol-registry-"+str(row["_line"]).zfill(5)+"}"),1)
        self.assertNotIn("PNone",text)

    def test_unnumbered_reference_is_named_and_numbered_reference_unchanged(self):
        class Index:
            def unique(self,label): return SimpleNamespace(part=None if label=="sec:front" else 1)
        resolver=SimpleNamespace(index=Index())
        row={"scope":"sec:front","first_use":"sec:front","_resolver":resolver}
        self.assertEqual(registry.scope_tex(row),r"\hyperref[sec:front]{\nameref*{sec:front}}")
        self.assertEqual(registry.first_use_tex(row),registry.scope_tex(row))
        row.update(scope="sec:body",first_use="sec:body")
        self.assertEqual(registry.scope_tex(row),r"\hyperref[sec:body]{\ref*{sec:body}}")
        row["scope"]="sec:front through sec:body"
        self.assertEqual(registry.scope_tex(row),r"\hyperref[sec:front]{\nameref*{sec:front}}--\hyperref[sec:body]{\ref*{sec:body}}")

if __name__=="__main__":unittest.main()
