from pathlib import Path
import importlib.util,json,sys,tempfile,unittest
tools=Path(__file__).parent
repo_tools=Path.cwd()/'tools'
if not (repo_tools/'check.py').exists():repo_tools=tools
sys.path.insert(0,str(repo_tools));sys.path.insert(0,str(tools))
import check
import symbol_registry as sr

class LineIndex(unittest.TestCase):
    def test_exact_count_equivalence_at_all_stops(self):
        for text in ('','plain','\n','α\r\nb\nc\n','x'*300+'\n'+'z'*20):
            for pos in range(-len(text)-3,len(text)+4):
                self.assertEqual(text.count('\n',0,pos)+1,check._line(text,pos))
    def test_cache_is_bounded(self):
        for n in range(10):check._line(str(n)+'\n',1)
        self.assertLessEqual(check._line_breaks.cache_info().currsize,2)

class BarShapes(unittest.TestCase):
    def test_entire_nested_operands(self):
        for value in (r'\abs{\mathcal M}',r' \left|\mathcal M\right| ',r'\lvert\mathcal M\rvert',r'|\mathcal M|'):
            self.assertTrue(sr._sole_bar_operand(value),value)
    def test_compound_expressions_are_not_bars_around_bars(self):
        for value in (r'\{\psi(K;b):b\in K^{\abs{y}}\}',r'1+\abs{x}',r'\abs{x}+1',r'\left|x\right|+\left|y\right|'):
            self.assertFalse(sr._sole_bar_operand(value),value)
    def test_original_structure_failures_remain(self):
        sr._notation_lint_selftest()

class ScopedRoles(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.base=Path(self.temp.name)
        (self.base/'parts/p09').mkdir(parents=True);(self.base/'bib').mkdir()
        (self.base/'main.tex').write_text(r'\input{parts/p09/test}',encoding='utf-8')
        (self.base/'bib/handbook.bib').write_text('@misc{Fixture,title={Fixture}}',encoding='utf-8')
        (self.base/'parts/p09/test.tex').write_text(r'''
\chapter{Test}\label{sec:p09-test}
\section{Local}\label{sec:p09-local}
\begin{hbdefinition}{def:p09-kb}{A finite knowledge base}
\(\mathcal M\) is a finite set of formulas; its size is \(\abs{\mathcal M}\).
\end{hbdefinition}
\(\abs{\{x:x\in A^{\abs{y}}\}}\) is a cardinality.
\section{Structures}\label{sec:p09-outside}
\(\abs{\mathcal M}\) has no domain convention here.
''',encoding='utf-8')
    def tearDown(self):self.temp.cleanup()
    def rows(self,authorized):
        spec={'presentation':'Finite knowledge base','regions':[{'anchor':'sec:p09-local'}]}
        if authorized:
            spec['overrides']=[{'glyph':r'\(\mathcal M\)','local_role':'finite set of formulas','first_use':'def:p09-kb','broader_scope':'global','broader_role':'structures','source':'def:p09-kb','reason':'The local definition declares the finite set explicitly.'}]
        res=sr.Resolver(self.base,bindings={'schema_version':1,'scopes':{'sec:p09-local':spec}})
        rows=[]
        for n,(glyph,macro,role,scope,first) in enumerate(((r'\(|X|\)',r'\abs','cardinality','global','sec:p09-test'),(r'\(\mathcal M\)',r'\mathcal M','structures','global','sec:p09-test'),(r'\(\mathcal M\)',r'\mathcal M','finite set of formulas','sec:p09-local','def:p09-kb')),1):
            rows.append({'glyph':glyph,'macro':macro,'role':role,'scope':scope,'first_use':first,'_line':n,'_resolver':res,'_scope':res.resolve(scope)})
        return rows
    def test_authorized_local_role_does_not_hide_outside_structure(self):
        out=sr.notation_lint(self.rows(True))
        self.assertEqual(1,len(out),out)
        self.assertIn('notation-role',out[0][0]);self.assertNotIn('(2 uses)',out[0][1])
    def test_merely_adding_a_row_does_not_shadow(self):
        out=sr.notation_lint(self.rows(False))
        self.assertEqual(1,len(out),out);self.assertIn('(2 uses)',out[0][1])
    def test_inner_untyped_structure_in_set_is_still_reported(self):
        p=self.base/'parts/p09/test.tex';s=p.read_text();p.write_text(s.replace(r'A^{\abs{y}}',r'A^{\abs{\mathcal N}}'),encoding='utf-8')
        rows=self.rows(True);rows[1]['macro']=r'\mathcal M,\mathcal N'
        out=sr.notation_lint(rows);self.assertEqual(2,len(out),out)

if __name__=='__main__':unittest.main(verbosity=2)
