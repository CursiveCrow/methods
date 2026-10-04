"""Focused regressions for the real symbol reader, resolver and renderers."""
from __future__ import annotations

import contextlib
import csv
import io
import json
from pathlib import Path
import tempfile
import unittest

from tools import check, symbol_registry as registry, symbols2tex


class SymbolRegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base=Path(self.temp.name)/'handbook'
        for directory in ['parts/p08','annex/p08','registry','bib']:
            (self.base/directory).mkdir(parents=True,exist_ok=True)
        (self.base/'main.tex').write_text('\\input{parts/p08/source}\n\\input{annex/p08/source}\n',encoding='utf-8')
        (self.base/'parts/p08/source.tex').write_text(r'''
\chapter{First}\label{sec:p08-source}
\section{A}\label{sec:p08-a}
\begin{hbdefinition}{def:p08-a}{Source A} Text.\end{hbdefinition}
\begin{hbtheorem}{thm:p08-a}{proved=annex:p8.a}{A} Text.\end{hbtheorem}
\section{B}\label{sec:p08-b}
\begin{hbdefinition}{def:p08-b}{Source B} Text.\end{hbdefinition}
\chapter{Second}\label{sec:p08-second}
\begin{hbdefinition}{def:p08-second}{Second} Text.\end{hbdefinition}
''',encoding='utf-8')
        (self.base/'annex/p08/source.tex').write_text(r'''
\section{Proofs}
\begin{annexitem}{annex:p8.a}{thm:p08-a}{A}
\begin{proof} Proof.\end{proof}
\end{annexitem}
''',encoding='utf-8')
        (self.base/'bib/handbook.bib').write_text('@book{Source1980,title={Source},year={1980}}\n',encoding='utf-8')
        self.path=self.base/'registry/symbols.csv'

    def row(self,scope='P8.1',first='def:p08-a',role='first role',glyph=r'\(q\)',precedence='meta'):
        return [glyph,'q',role,scope,precedence,first,'']

    def read(self,*rows,bindings=None):
        with self.path.open('w',encoding='utf-8',newline='') as stream:
            writer=csv.writer(stream);writer.writerow(registry.HEADER);writer.writerows(rows)
        if bindings is not None:
            (self.base/'registry/symbol-scopes.json').write_text(json.dumps(bindings),encoding='utf-8')
        return symbols2tex.read_rows(self.path)

    def test_actual_label_first_use_passes_and_both_outputs_link_it(self):
        rows,errors=self.read(self.row())
        self.assertEqual(errors,[])
        link=r'\hyperref[def:p08-a]{\ref*{def:p08-a}}'
        self.assertIn(link,symbols2tex.render(rows))
        self.assertIn(link,symbols2tex.render_index(rows))

    def test_unknown_and_duplicate_reader_labels_fail(self):
        _,errors=self.read(self.row(first='def:p08-absent'))
        self.assertTrue(any('resolves 0 times' in e for e in errors))
        with (self.base/'parts/p08/source.tex').open('a',encoding='utf-8') as stream:
            stream.write(r'\begin{hbdefinition}{def:p08-a}{Duplicate} Text.\end{hbdefinition}')
        _,errors=self.read(self.row())
        self.assertTrue(any('resolves 2 times' in e for e in errors))

    def test_unrouted_label_is_not_accepted(self):
        (self.base/'parts/p08/unrouted.tex').write_text(r'\label{def:p08-draft}',encoding='utf-8')
        _,errors=self.read(self.row(first='def:p08-draft'))
        self.assertTrue(any('resolves 0 times' in e for e in errors))

    def test_numeric_scope_checks_actual_chapter_and_annex_owner(self):
        _,errors=self.read(self.row(first='def:p08-second'))
        self.assertTrue(any('outside scope' in e for e in errors))
        _,errors=self.read(self.row(first='annex:p8.a'))
        self.assertEqual(errors,[])

    def test_invalid_scope_never_becomes_global_or_adjacent_part(self):
        for scope in ['','garbage','P20','P15.101','P8.2-P8.1','P8 words']:
            with self.subTest(scope=scope):
                _,errors=self.read(self.row(scope=scope))
                self.assertTrue(errors)
                self.assertIsNone(registry.parse_scope(scope))

    def test_disjoint_sections_pass_but_same_region_conflicts(self):
        rows,errors=self.read(self.row('sec:p08-a'),self.row('sec:p08-b','def:p08-b','second role'))
        self.assertEqual(errors,[])
        self.assertEqual(registry.collision_check(rows),[])
        rows,errors=self.read(self.row('sec:p08-a'),self.row('def:p08-a',role='second role'))
        self.assertEqual(errors,[])
        self.assertIn('glyph-role collision',registry.collision_check(rows)[0])

    def test_range_includes_both_complete_sections_and_rejects_reversal(self):
        _,errors=self.read(self.row('sec:p08-a through sec:p08-b','def:p08-b'))
        self.assertEqual(errors,[])
        _,errors=self.read(self.row('sec:p08-b through sec:p08-a'))
        self.assertTrue(any('unordered' in e for e in errors))

    def test_named_aliases_use_actual_regions_not_different_strings(self):
        bindings={'schema_version':1,'scopes':{
            'P8 source A':{'presentation':'Source1980','regions':[{'anchor':'sec:p08-a'}]},
            'P8 other spelling':{'presentation':'Source1980','regions':[{'anchor':'sec:p08-a'}]}}}
        rows,errors=self.read(self.row('P8 source A'),self.row('P8 other spelling',role='other'),bindings=bindings)
        self.assertEqual(errors,[])
        self.assertTrue(registry.collision_check(rows))

    def test_binding_cannot_launder_invalid_or_mismatched_part_numbers(self):
        for scope in ['P20','P15.101','P17 wrong part']:
            with self.subTest(scope=scope):
                bindings={'schema_version':1,'scopes':{scope:{'presentation':'Source1980','regions':[{'anchor':'sec:p08-a'}]}}}
                _,errors=self.read(self.row(scope),bindings=bindings)
                self.assertTrue(errors)

    def test_annex_scope_does_not_silently_accept_body_first_use(self):
        _,errors=self.read(self.row('annex:p8.a','thm:p08-a'))
        self.assertTrue(any('outside scope' in e for e in errors))

    def test_source_override_is_exact_and_does_not_exempt_other_conflicts(self):
        bindings={'schema_version':1,'scopes':{'P8 source A':{
            'presentation':'Source1980','regions':[{'anchor':'sec:p08-a'}],
            'overrides':[{'glyph':r'\(q\)','local_role':'source role','first_use':'def:p08-a',
                'broader_scope':'global','broader_role':'default role','reason':'Explicit local source declaration.', 'source':'Source1980'}]}}}
        rows,errors=self.read(self.row('global','P8.1','default role'),self.row('P8 source A',role='source role'),bindings=bindings)
        self.assertEqual(errors,[]);self.assertEqual(registry.collision_check(rows),[])
        rows,errors=self.read(self.row('global','P8.1','different default'),self.row('P8 source A',role='source role'),bindings=bindings)
        self.assertEqual(errors,[]);self.assertTrue(registry.collision_check(rows))
        rows,errors=self.read(self.row('P8 source A',role='source role'),self.row('P8 source A',role='different local'),bindings=bindings)
        self.assertEqual(errors,[]);self.assertTrue(registry.collision_check(rows))

    def test_override_cannot_hide_duplicate_role_or_unidentified_source(self):
        bindings={'schema_version':1,'scopes':{'P8 source A':{'presentation':'Source1980','regions':[{'anchor':'sec:p08-a'}]}}}
        rows,errors=self.read(self.row('P8 source A'),self.row('P8 source A'),bindings=bindings)
        self.assertEqual(errors,[])
        self.assertIn('duplicate glyph-role',registry.collision_check(rows)[0])
        bindings['scopes']['P8 source A']['overrides']=[{'glyph':r'\(q\)','local_role':'source role','first_use':'def:p08-a','broader_scope':'global','broader_role':'default role','reason':'Declared','source':'MissingSource'}]
        _,errors=self.read(self.row('P8 source A'),bindings=bindings)
        self.assertTrue(any('unidentified override source' in e for e in errors))

    def test_descriptor_is_retained_not_converted_to_rank(self):
        for descriptor in ['meta','n/a','3.5','infix','object','relation']:
            with self.subTest(descriptor=descriptor):
                rows,errors=self.read(self.row(precedence=descriptor))
                self.assertEqual(errors,[]);self.assertEqual(rows[0]['precedence'],descriptor)
        _,errors=self.read(self.row(precedence='anything-goes'))
        self.assertTrue(any('malformed precedence' in e for e in errors))

    def test_both_consumers_report_the_same_real_collision(self):
        rows,errors=self.read(self.row('sec:p08-a'),self.row('def:p08-a',role='second role'))
        self.assertEqual(errors,[])
        data=check._HBData()
        with contextlib.redirect_stdout(io.StringIO()):check._hb_check_symbols(self.path,data)
        self.assertEqual(data.findings['glyph-collision'],registry.collision_check(rows))


if __name__=='__main__':unittest.main()
