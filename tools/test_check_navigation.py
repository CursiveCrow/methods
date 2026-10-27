#!/usr/bin/env python3
"""Regression probes for calculus-file and entry-proof navigation."""
from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import unittest

CHECK_PATH = Path(os.environ.get('METHODS_CHECK_MODULE', str(Path(__file__).with_name('check.py'))))
spec = importlib.util.spec_from_file_location('navigation_checker', CHECK_PATH)
assert spec and spec.loader
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

def scan(files: dict[str, str]):
    data = check._HBData()
    for relative, text in files.items():
        check._hb_scan_file(relative, check.strip_verbatims(check.strip_comments(text)), data)
    check._hb_cross_checks(data, {})
    return data.findings

def theorem(label='thm:p08-owner', form='proved'):
    return rf'\begin{{hbtheorem}}{{{label}}}{{{form}=annex:p08-proof}}{{Result}}Claim.\end{{hbtheorem}}'

def annex(owner='thm:p08-owner'):
    return rf'\begin{{annexitem}}{{annex:p08-proof}}{{{owner}}}{{Proof}}Argument.\end{{annexitem}}'

def entry(text=r'Theorem~\ref{thm:p08-owner}.', form='proved'):
    return rf'''\begin{{systementry}}{{entry:p08-card}}{{Card}}
\entrylanguage{{Formula language.}}
\entrysemantics{{Declared structures.}}
\entrycalculus{{sheet:p08-first}}
\entryadequacy{{{form}=annex:p08-proof}}{{{text}}}
\entrydecidability{{cited=Fixture}}{{Decision criterion.}}
\entrycharacteristic{{A characteristic property.}}
\entrysources{{Fixture}}
\end{{systementry}}'''

def proof_files(body=None, proof=None):
    return {
        'parts/p08/fixture.tex': (theorem()+entry()) if body is None else body,
        'annex/p08/fixture.tex': annex() if proof is None else proof,
        'registry/calculi/bundle.tex': r'\calculussheet{sheet:p08-first}{First}{Identity.}',
    }

class EntryProofNavigationTests(unittest.TestCase):
    def test_card_navigates_to_exact_owner_without_second_ownership(self):
        self.assertNotIn('annex-bidir',scan(proof_files()))

    def test_card_requires_field_local_owner_reference(self):
        body=theorem()+entry('Proved here.')+r'\ref{thm:p08-owner}'
        findings=scan(proof_files(body))
        self.assertTrue(any('must reference its owning result' in s for s in findings['annex-bidir']))

    def test_card_reference_to_another_result_is_not_sufficient(self):
        body=theorem()+r'\label{thm:p08-other}'+entry(r'\ref{thm:p08-other}')
        self.assertIn('annex-bidir',scan(proof_files(body)))

    def test_card_cannot_upgrade_sketched_owner_to_proved(self):
        findings=scan(proof_files(theorem(form='sketched')+entry()))
        self.assertTrue(any('owner status is sketched' in s for s in findings['annex-bidir']))

    def test_two_theorem_owners_still_fail(self):
        findings=scan(proof_files(theorem()+theorem('thm:p08-second')+entry()))
        self.assertTrue(any('targeted by 2 results' in s for s in findings['annex-bidir']))

    def test_missing_annex_still_fails(self):
        findings=scan(proof_files(proof=''))
        self.assertTrue(any('no annexitem' in s for s in findings['annex-bidir']))

    def test_entry_owned_annex_remains_valid(self):
        findings=scan(proof_files(entry('An entry-owned proof.'),annex('entry:p08-card')))
        self.assertNotIn('annex-bidir',findings)

    def test_unowned_annex_with_body_label_only_still_fails(self):
        findings=scan(proof_files(r'\label{thm:p08-owner}'+entry()))
        self.assertIn('annex-bidir',findings)

class CalculusFileNavigationTests(unittest.TestCase):
    def test_bundle_basename_need_not_be_a_sheet_label(self):
        findings=scan({
            'parts/p07/fixture.tex': r'\showcalculus{bundle}\ref{sheet:p07-a}\ref{sheet:p07-b}',
            'registry/calculi/bundle.tex': r'\calculussheet{sheet:p07-a}{A}{Identity.}\calculussheet{sheet:p07-b}{B}{Identity.}',
        })
        self.assertNotIn('dangling-ref',findings)

    def test_missing_file_is_not_excused_by_matching_label_elsewhere(self):
        findings=scan({
            'parts/p07/fixture.tex': r'\showcalculus{missing}',
            'registry/calculi/another.tex': r'\calculussheet{sheet:missing}{A}{Identity.}',
        })
        self.assertTrue(any('input registry/calculi/missing.tex is missing' in s for s in findings['dangling-ref']))

    def test_file_without_sheet_is_rejected(self):
        findings=scan({'parts/p07/fixture.tex':r'\showcalculus{empty}','registry/calculi/empty.tex':'Prose only.'})
        self.assertTrue(any('declares no calculus sheet' in s for s in findings['dangling-ref']))

    def test_nested_sheet_bundle_is_supported(self):
        findings=scan({
            'parts/p07/fixture.tex':r'\showcalculus{bundle}',
            'registry/calculi/bundle.tex':r'\input{registry/calculi/child}',
            'registry/calculi/child.tex':r'\calculussheet{sheet:p07-child}{A}{Identity.}',
        })
        self.assertNotIn('dangling-ref',findings)

    def test_actual_missing_label_still_fails(self):
        findings=scan({
            'parts/p07/fixture.tex':r'\showcalculus{bundle}\ref{sheet:p07-absent}',
            'registry/calculi/bundle.tex':r'\calculussheet{sheet:p07-present}{A}{Identity.}',
        })
        self.assertTrue(any('sheet:p07-absent' in s for s in findings['dangling-ref']))

if __name__=='__main__':
    unittest.main(verbosity=2)
