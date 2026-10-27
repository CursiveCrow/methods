"""Fail-closed probes for the explicit eight-label compatibility policy."""
from __future__ import annotations

import copy
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

CHECK_PATH = Path(os.environ.get('METHODS_CHECK_MODULE', str(Path(__file__).with_name('check.py'))))
sys.path.insert(0, str(CHECK_PATH.parent))
spec = importlib.util.spec_from_file_location('legacy_test_checker', CHECK_PATH)
assert spec and spec.loader
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)
from handbook_legacy_labels import load_legacy_label_policy, validate_legacy_labels


def fixture(kind='hblemma-argument'):
    relative = 'parts/p04/fixture.tex' if kind == 'hblemma-argument' else 'annex/p05/fixture.tex'
    prefix = 'sec' if kind == 'section-label' else 'thm'
    old = 'annex:sec:p05-old' if kind == 'section-label' else 'lem:p05-old'
    canonical = prefix + ':p05-canonical'
    row = {'old': old, 'canonical': canonical, 'file': 'handbook/' + relative, 'kind': kind}
    if kind == 'hblemma-argument':
        head = rf'\begin{{hblemma}}{{{canonical}}}{{cited=Fixture}}{{A {{grouped}} title}}'
        tail = r'Claim.\end{hblemma}'
    elif kind == 'annexlemma-label':
        head = rf'\begin{{annexlemma}}[A {{[grouped]}} title]\label{{{canonical}}}'
        tail = r'Claim.\end{annexlemma}'
    else:
        head = rf'\section{{A {{grouped}} title}}\label{{{canonical}}}'
        tail = 'Text.'
    alias = rf'\hblegacylabel{{{old}}}{{{canonical}}}'
    return {'schema_version': 1, 'aliases': [row]}, {relative: head + '\n' + alias + '\n' + tail}


def scan(policy, files):
    bodies = {p: check.strip_verbatims(check.strip_comments(t)) for p, t in files.items()}
    data = check._HBData()
    for relative, text in bodies.items():
        check._hb_scan_file(relative, text, data)
    errors, aliases = validate_legacy_labels(policy, bodies, data.labels, check.scan_braced_args)
    return errors, aliases, data


class LegacyLabelTests(unittest.TestCase):
    def rejects(self, policy, files, phrase):
        errors, aliases, _ = scan(policy, files)
        self.assertTrue(any(phrase in error for error in errors), errors)
        self.assertEqual([], aliases)

    def test_three_narrow_kinds_accept(self):
        for kind in ('hblemma-argument', 'annexlemma-label', 'section-label'):
            with self.subTest(kind=kind):
                errors, aliases, _ = scan(*fixture(kind))
                self.assertEqual([], errors)
                self.assertEqual(1, len(aliases))

    def test_comments_and_whitespace_preserve_adjacency(self):
        policy, files = fixture()
        files = {p: t.replace('\n', '\n% harmless comment\n  ') for p, t in files.items()}
        self.assertEqual([], scan(policy, files)[0])

    def test_missing_command(self):
        policy, files = fixture()
        files = {p: t.replace(r'\hblegacylabel', '%\\hblegacylabel') for p, t in files.items()}
        self.rejects(policy, files, 'expected one declaration, found 0')

    def test_unmanifested_command(self):
        policy, files = fixture()
        policy['aliases'] = []
        self.rejects(policy, files, 'unmanifested alias')

    def test_duplicate_command_same_file(self):
        policy, files = fixture()
        row = policy['aliases'][0]
        files[next(iter(files))] += rf"\hblegacylabel{{{row['old']}}}{{{row['canonical']}}}"
        self.rejects(policy, files, 'expected one declaration, found 2')

    def test_duplicate_command_other_file(self):
        policy, files = fixture()
        files['parts/p04/other.tex'] = next(iter(files.values()))
        self.rejects(policy, files, 'expected one declaration, found 2')

    def test_wrong_target(self):
        policy, files = fixture()
        files = {p: t.replace(r'\hblegacylabel{lem:p05-old}{thm:p05-canonical}',
                             r'\hblegacylabel{lem:p05-old}{thm:p05-wrong}') for p, t in files.items()}
        self.rejects(policy, files, 'disagrees with policy')

    def test_wrong_file(self):
        policy, files = fixture()
        files = {'parts/p04/other.tex': next(iter(files.values()))}
        self.rejects(policy, files, 'disagrees with policy')

    def test_intervening_text(self):
        policy, files = fixture()
        files = {p: t.replace(r'\hblegacylabel', r'Intervening.\hblegacylabel') for p, t in files.items()}
        self.rejects(policy, files, 'immediately follow')

    def test_intervening_counter_change(self):
        policy, files = fixture()
        files = {p: t.replace(r'\hblegacylabel', r'\refstepcounter{section}\hblegacylabel') for p, t in files.items()}
        self.rejects(policy, files, 'immediately follow')

    def test_alias_before_canonical(self):
        policy, files = fixture()
        files = {p: '\n'.join([t.splitlines()[1], t.splitlines()[0], t.splitlines()[2]]) for p, t in files.items()}
        self.rejects(policy, files, 'immediately follow')

    def test_wrong_environment_kind(self):
        policy, files = fixture()
        files = {p: t.replace('hblemma', 'hbtheorem') for p, t in files.items()}
        self.rejects(policy, files, 'immediately follow')

    def test_annex_plain_label_must_follow_its_own_lemma_header(self):
        policy, files = fixture('annexlemma-label')
        files = {p: t.replace(r'\label', r'\end{annexlemma}\label', 1) for p, t in files.items()}
        self.rejects(policy, files, 'immediately follow')

    def test_section_label_must_follow_section_header(self):
        policy, files = fixture('section-label')
        files = {p: t.replace(r'\section', r'\subsection') for p, t in files.items()}
        self.rejects(policy, files, 'immediately follow')

    def test_canonical_global_duplicate(self):
        policy, files = fixture()
        files['parts/p04/other.tex'] = r'\label{thm:p05-canonical}'
        self.rejects(policy, files, 'globally unique')

    def test_old_plain_label_collision(self):
        policy, files = fixture()
        files['annex/p05/other.tex'] = r'\label{lem:p05-old}'
        self.rejects(policy, files, 'ordinary/environment label')

    def test_old_environment_label_cannot_be_laundered(self):
        policy, files = fixture()
        files['parts/p05/other.tex'] = r'\begin{hblemma}{lem:p05-old}{cited=Fixture}{Old}Text.\end{hblemma}'
        self.rejects(policy, files, 'ordinary/environment label')

    def test_duplicate_policy_old(self):
        policy, files = fixture()
        policy['aliases'].append(copy.deepcopy(policy['aliases'][0]))
        self.rejects(policy, files, 'policy repeats old')

    def test_alias_chain_rejected(self):
        policy, files = fixture()
        second = copy.deepcopy(policy['aliases'][0])
        second.update(old='thm:p05-canonical', canonical='thm:p05-new')
        policy['aliases'].append(second)
        self.rejects(policy, files, 'chain/cycle')

    def test_restoration_path_not_allowed(self):
        policy, files = fixture()
        policy['aliases'][0]['file'] = 'handbook/restoration/inherited-00001-00002.tex'
        self.rejects(policy, files, 'invalid editorial file')

    def test_path_traversal_not_allowed(self):
        policy, files = fixture()
        policy['aliases'][0]['file'] = 'handbook/parts/p04/../p05/fixture.tex'
        self.rejects(policy, files, 'invalid editorial file')

    def test_malformed_command_rejected(self):
        policy, files = fixture()
        files = {p: t.replace(r'{thm:p05-canonical}', r'{\dynamiclabel}', 2) for p, t in files.items()}
        self.rejects(policy, files, 'malformed hblegacylabel')

    def test_invalid_schema_does_not_crash(self):
        _, files = fixture()
        for policy in (None, [], {}, {'schema_version': True, 'aliases': []},
                       {'schema_version': 1, 'aliases': [None]},
                       {'schema_version': 1, 'aliases': [{'old': []}]}):
            with self.subTest(policy=policy):
                errors, aliases, _ = scan(policy, files)
                self.assertTrue(errors)
                self.assertEqual([], aliases)

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'policy.json'
            path.write_text('{"schema_version":1,"schema_version":1,"aliases":[]}', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'duplicate JSON key'):
                load_legacy_label_policy(path)

    def test_missing_policy_is_always_hard(self):
        self.assertIn('legacy-label', check.HB_ALWAYS_HARD)
        data = check._HBData()
        with tempfile.TemporaryDirectory() as directory:
            check._hb_check_legacy_labels(Path(directory), {}, data)
        self.assertIn('legacy-label', data.findings)

    def test_registered_old_references_resolve_without_new_status_owner(self):
        policy, files = fixture()
        relative = next(iter(files))
        files[relative] += r'\ref{lem:p05-old}\cref{lem:p05-old}\pageref{lem:p05-old}\hyperref[lem:p05-old]{Old}'
        _, _, data = scan(policy, files)
        bodies = {p: check.strip_comments(t) for p, t in files.items()}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'spec' / 'handbook-legacy-labels.json'
            path.parent.mkdir()
            path.write_text(json.dumps(policy), encoding='utf-8')
            check._hb_check_legacy_labels(Path(directory), bodies, data)
        check._hb_cross_checks(data, {})
        self.assertNotIn('legacy-label', data.findings)
        self.assertNotIn('dangling-ref', data.findings)
        self.assertEqual({'lem:p05-old': 'thm:p05-canonical'}, data.legacy_label_aliases)
        self.assertEqual(['thm:p05-canonical'], [s['owner'] for s in data.statuses])


if __name__ == '__main__':
    unittest.main(verbosity=2)
