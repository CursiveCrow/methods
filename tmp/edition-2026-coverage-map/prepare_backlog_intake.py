"""Read-only proposal for released reader contributions; lead applies patches.

This constructs explicit presentation regions and reports actual collisions.
It does not authorize proof/source acceptance or alter historical coverage.
"""
import csv
import io
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
import symbol_registry as sr

B = ROOT / 'handbook'
groups = [
    ('p01-equivalence-closure', 'parts/p01/equivalence-closure-and-quotients.tex', 'annex/p01/equivalence-closure-and-quotients.tex', 'FrozenFormalLogicFoundationsClosure'),
    ('p01-bpi-ultrafilters', 'parts/p01/boolean-prime-ideal-and-ultrafilters.tex', 'annex/p01/boolean-prime-ideal-and-ultrafilters.tex', 'Koppelberg1989'),
    ('p06-proper-forcing-master', 'parts/p06/proper-forcing-and-master-conditions.tex', 'annex/p06/proper-forcing-and-master-conditions.tex', 'Dow1988ElementarySubmodels'),
    ('p09-timed-regions-zones', 'parts/p09/timed-automata-regions-and-zones.tex', 'annex/p09/timed-automata-regions-and-zones.tex', 'AlurDill1994TimedOriginal'),
    ('p07-ch88-object-product', 'parts/p07/presentations/coquand-huet-1988-object-product.tex', 'annex/p07/presentations/coquand-huet-1988-object-product.tex', 'CoquandHuet1988'),
    ('p12-equational-basic-completeness', 'parts/p12/presentations/n-c-035-05-basic-completeness.tex', 'annex/p12/n-c-035-05-basic-completeness.tex', 'BaaderSnyder2001'),
    ('p12-har-autarkic', 'parts/p12/presentations/har2001-c18-autarkic.tex', 'annex/p12/presentations/har2001-c18-autarkic.tex', 'BarendregtGeuvers2001'),
    ('p12-har-kprime', 'parts/p12/presentations/har2001-c18-kprime.tex', 'annex/p12/presentations/har2001-c18-kprime.tex', 'BarendregtGeuvers2001'),
    ('p12-har-polynomial-normalizer', 'parts/p12/presentations/har2001-c18-polynomial-normalizer.tex', 'annex/p12/presentations/har2001-c18-polynomial-normalizer.tex', 'BarendregtGeuvers2001'),
    ('p15-fisher-estimation', 'parts/p15/fisher-estimation-and-regularity.tex', 'annex/p15/fisher-estimation-and-regularity.tex', 'Fisher1922Foundations'),
    ('p15-rissanen-mdl', 'parts/p15/rissanen-structural-and-numerical-inference.tex', 'annex/p15/rissanen-structural-and-numerical-inference.tex', 'Rissanen1978Modeling'),
    ('p15-probability-quantifiers', 'parts/p15/probability-quantifiers.tex', 'annex/p15/probability-quantifiers.tex', 'KeislerLotfallah2009AuthorProbability'),
    ('p16-nonmonotonic-causal-theories', 'parts/p16/nonmonotonic-causal-theories.tex', 'annex/p16/nonmonotonic-causal-theories.tex', 'Turner2008NonmonotonicCausalLogic'),
    ('p09-negative-premises', 'parts/p09/negative-premises-and-stratification.tex', 'annex/p09/negative-premises-and-stratification.tex', 'AcetoFokkinkVerhoefSOSAuthorNP'),
    ('p16-peirce-abduction', 'parts/p16/peirce-abduction-and-inquiry.tex', None, 'Peirce1878DIHPrimary'),
    ('p15-whewell-mill', 'parts/p15/whewell-mill-scientific-induction.tex', 'annex/p15/whewell-mill-scientific-induction.tex', 'Mill1882SystemLogicPG'),
    ('p15-goodman-projectibility', 'parts/p15/goodman-projectibility.tex', 'annex/p15/goodman-projectibility.tex', 'GoodmanNewRiddleTeachingScan'),
    ('p15-fisher-grouping', 'parts/p15/fisher-grouping-and-moments.tex', 'annex/p15/fisher-grouping-and-moments.tex', 'Fisher1922Foundations'),
    ('p12-har-primitive-recursive-compiler', 'parts/p12/presentations/har2001-c18-primitive-recursive-compiler.tex', 'annex/p12/presentations/har2001-c18-primitive-recursive-compiler.tex', 'OostdijkGeuvers2000ProofByComputationPreprint'),
    ('p15-goodman-entrenchment', 'parts/p15/goodman-entrenchment-and-projectibility.tex', 'annex/p15/goodman-entrenchment-and-projectibility.tex', 'Goodman1983FourthProjection'),
    ('p19-self-explanation', 'parts/p19/self-explanation-and-learning.tex', None, 'ChiEtAl1989SelfExplanations'),
    ('p19-aging-reasoning', 'parts/p19/aging-goals-and-reasoning.tex', None, 'RebokEtAl2014ACTIVE'),
    ('p15-probability-elimination', 'parts/p15/probability-quantifier-elimination.tex', 'annex/p15/probability-quantifier-elimination.tex', 'KeislerLotfallah2009AuthorProbability'),
    ('p16-cplus-action-language', 'parts/p16/cplus-action-language.tex', 'annex/p16/cplus-action-language.tex', 'GiunchigliaEtAl2003CplusAuthor'),
    ('p15-vc-learning', 'parts/p15/vc-dimension-and-uniform-learning.tex', 'annex/p15/vc-dimension-and-uniform-learning.tex', 'LuxburgScholkopf2008Author'),
    ('p09-sos-formats', 'parts/p09/sos-congruence-and-conservative-extension.tex', 'annex/p09/sos-congruence-and-conservative-extension.tex', 'AcetoFokkinkVerhoefSOSAuthorNP'),
    ('p02-free-boolean-completeness', 'parts/p02/free-boolean-algebra-and-completeness.tex', 'annex/p02/free-boolean-algebra-and-completeness.tex', 'HowardRubin1998'),
]
if '--har-only' in sys.argv:
    groups = [g for g in groups if g[0].startswith('p12-har-')]
if '--new-only' in sys.argv:
    groups = [g for g in groups if g[0] in {'p15-fisher-estimation', 'p15-rissanen-mdl', 'p15-probability-quantifiers', 'p16-nonmonotonic-causal-theories', 'p09-negative-premises'}]
if '--history-only' in sys.argv:
    groups = [g for g in groups if g[0] in {'p16-peirce-abduction', 'p15-whewell-mill', 'p15-goodman-projectibility'}]
if '--grouping-only' in sys.argv:
    groups = [g for g in groups if g[0] == 'p15-fisher-grouping']
if '--compiler-only' in sys.argv:
    groups = [g for g in groups if g[0] == 'p12-har-primitive-recursive-compiler']
if '--last-only' in sys.argv:
    groups = [g for g in groups if g[0] in {'p15-goodman-entrenchment', 'p19-self-explanation', 'p19-aging-reasoning'}]
if '--final-only' in sys.argv:
    groups = [g for g in groups if g[0] in {'p15-probability-elimination', 'p16-cplus-action-language', 'p15-vc-learning', 'p09-sos-formats', 'p02-free-boolean-completeness'}]
bindings = json.loads((B / 'registry/symbol-scopes.json').read_text(encoding='utf-8-sig'))
additions = {}
new = []
counts = {}
for stem, body, annex, source in groups:
    intake_text = (B / f'registry/symbols-intake-{stem}.csv').read_text(encoding='utf-8-sig')
    if stem == 'p15-fisher-grouping':
        intake_text = intake_text.replace('"\\(C_{k,s}\\)",C_{k,s},', '"\\(C_{k,s}\\)","C_{k,s}",')
    rows = list(csv.DictReader(io.StringIO(intake_text)))
    counts[stem] = len(rows)
    for row in rows:
        raw = row['scope']
        if raw not in additions:
            regions = [{'file': body}] + ([{'file': annex}] if annex else [])
            if raw == 'p01-bpi-algebra':
                regions = [{'anchor': a} for a in ['sec:p01-bpi-algebraic-vocabulary', 'sec:p01-bpi-extension-equivalence', 'annex:p01-bpi-duality', 'annex:p01-bpi-quotient', 'annex:p01-bpi-finite-local', 'annex:p01-bpi-equivalence', 'annex:p01-bpi-ac-implication', 'annex:p01-bpi-set-boundaries']]
            elif raw == 'p01-bpi-source-dictionary':
                regions = [{'anchor': 'def:p01-bpi-boolean-algebra'}, {'anchor': 'def:p01-bpi-quotient'}]
            elif raw == 'p01-bpi-propositional':
                regions = [{'anchor': 'sec:p01-bpi-compactness-bridge'}, {'anchor': 'annex:p01-bpi-propositional-compactness'}]
            elif raw == 'p01-bpi-principles':
                regions = [{'file': body}, {'file': annex}]
            elif raw == 'p01-bpi-choice-strength':
                regions = [{'anchor': 'sec:p01-bpi-choice-strength'}, {'anchor': 'annex:p01-bpi-ac-implication'}, {'anchor': 'annex:p01-bpi-set-boundaries'}]
            elif raw == 'annex:p12.eb.progress-countercase':
                regions = [{'anchor': 'thm:p12-eb-progress-countercase'}, {'anchor': raw}]
            elif stem == 'p15-fisher-estimation':
                selectors = {
                    'P15 Fisher property distinctions': ('def:p15-fe-properties', []),
                    'P15 Fisher binomial argument': ('def:p15-fe-binomial', ['annex:p15.fe.binomial']),
                    'P15 Fisher coordinate argument': ('thm:p15-fe-coordinates', ['annex:p15.fe.coordinates']),
                    'P15 Fisher finite regularity': ('def:p15-fe-finite-regularity', ['annex:p15.fe.score']),
                    'P15 Fisher finite countermodels': ('thm:p15-fe-failures', ['annex:p15.fe.failures']),
                    'P15 Fisher Cauchy location': ('thm:p15-fe-cauchy', ['annex:p15.fe.cauchy']),
                }
                target, proof_anchors = selectors[raw]
                regions = [{'heading_of': target, 'level': 'section'}] + [{'anchor': a} for a in proof_anchors]
            elif stem == 'p16-peirce-abduction':
                regions = [{'anchor': 'def:p16-peirce-empirical-formula'}]
            elif stem == 'p15-goodman-entrenchment':
                if raw == 'p15-goodman-override':
                    regions = [{'anchor': 'sec:p15-goodman-override'}]
                elif raw == 'p15-goodman-comparative and p15-goodman-negative-overhypotheses':
                    regions = [{'anchor': 'sec:p15-goodman-comparative'}, {'anchor': 'sec:p15-goodman-negative-overhypotheses'}]
            elif stem == 'p15-fisher-grouping':
                selectors = {
                    'P15 Fisher midpoint experiment': ('def:p15-fg-grid', 'annex:p15.fg.phase'),
                    'P15 Fisher phase-average correction': ('thm:p15-fg-phase', 'annex:p15.fg.phase'),
                    'P15 Fisher normal Fourier correction': ('thm:p15-fg-fourier', 'annex:p15.fg.fourier'),
                    'P15 Fisher moment precision': ('thm:p15-fg-moments', 'annex:p15.fg.moments'),
                    'P15 Fisher cell likelihood': ('def:p15-fg-cells', 'annex:p15.fg.deviance'),
                    'P15 Fisher Pearson approximation': ('thm:p15-fg-deviance', 'annex:p15.fg.deviance'),
                    'P15 Fisher normal class experiment': ('def:p15-fg-normal', 'annex:p15.fg.information'),
                    'P15 Fisher recorded normal information': ('thm:p15-fg-information', 'annex:p15.fg.information'),
                    'P15 Fisher averaged information expansion': ('thm:p15-fg-expansion', 'annex:p15.fg.expansion'),
                    'P15 Fisher expansion proof': ('thm:p15-fg-expansion', 'annex:p15.fg.expansion'),
                }
                target, proof = selectors[raw]
                regions = [{'heading_of': target, 'level': 'subsection'}, {'anchor': proof}]
            elif raw == 'P15 Whewell Mill source schemata':
                regions = [{'anchor': 'sec:p15-wm-methods'}, {'anchor': 'thm:p15-wm-causal-ambiguity'}, {'anchor': 'annex:p15.wm.causal-ambiguity'}]
            elif raw == 'P15 Whewell Mill causal illustration':
                regions = [{'anchor': 'thm:p15-wm-causal-ambiguity'}, {'anchor': 'annex:p15.wm.causal-ambiguity'}]
            elif raw == 'P15 Whewell Mill finite continuation':
                regions = [{'anchor': 'thm:p15-wm-finite-continuation'}, {'anchor': 'annex:p15.wm.finite-continuation'}]
            additions[raw] = {'presentation': source + '; released editorial construction with its declared local types', 'regions': regions}
        if not row['macro']:
            row['macro'] = row['glyph'].removeprefix('\\(').removesuffix('\\)')
        if stem in {'p15-probability-quantifiers', 'p15-probability-elimination'} and not row['glyph'].startswith('\\('):
            row['glyph'] = '\\(' + row['glyph'] + '\\)'
        if stem == 'p15-goodman-projectibility' and not row['glyph'].startswith('\\('):
            row['glyph'] = '\\(' + row['macro'] + '\\)'
        if stem == 'p15-goodman-entrenchment' and not row['glyph'].startswith('\\('):
            row['glyph'] = '\\(' + row['macro'] + '\\)'
        if row['precedence'] in {'atomic', 'set', 'hypothesis', 'numeric'}:
            row['precedence'] = 'object'
        if row['precedence'] in {'application', 'postfix', 'binder', 'function'}:
            row['precedence'] = 'meta'
        new.append(row)
bindings['scopes'].update(additions)
index = sr.ReaderIndex(B)
resolver = sr.Resolver(B, bindings=bindings, index=index)
old, errors = sr.read_rows(B / 'registry/symbols.csv', resolver=resolver)
rebindings = {}
binding_repairs = {}
if '--new-only' in sys.argv:
    bad_lines = {int(re.match(r'line (\d+):', e)[1]) for e in errors if re.match(r'line (\d+): first_use', e)}
    stale_scopes = {r['scope'] for r in old if r['_line'] in bad_lines}
    for raw in sorted(stale_scopes):
        related = [r for r in old if r['scope'] == raw]
        paths = {index.unique(r['first_use']).path for r in related}
        assert len(paths) == 1, ('nonlocal legacy scope', raw, paths)
        body = next(iter(paths))
        annex = body.replace('parts/', 'annex/', 1)
        assert len(index.files.get(annex, [])) == 1, ('existing proof route', annex)
        name = 'P15 routed chapter ' + Path(body).stem
        rebindings[raw] = name
        binding_repairs[name] = {
            'presentation': 'Existing declared source chapter and matching proof annex; stable region binding replaces a numeric chapter index invalidated by reader insertion',
            'regions': [{'file': body}, {'file': annex}],
        }
    bindings['scopes'].update(binding_repairs)
    additions.update(binding_repairs)
    additions['P15 Fisher binomial argument']['overrides'] = [{
        'glyph': '\\(\\mathcal L\\)', 'local_role': 'likelihood function',
        'first_use': 'def:p15-fe-binomial', 'broader_scope': 'global',
        'broader_role': 'signature', 'source': 'Fisher1922Foundations',
        'reason': 'The source-informed finite binomial experiment explicitly types this displayed mathcal L as its likelihood function, not an object-language signature.',
    }]
    additions['p15-rmdl-source']['overrides'] = [{
        'glyph': '\\(s\\)', 'local_role': 'integer model structure',
        'first_use': 'sec:p15-rmdl-structure', 'broader_scope': 'global',
        'broader_role': 'variable assignment', 'source': 'Rissanen1978Modeling',
        'reason': 'The original structural/numerical split explicitly types s as the integer model structure, not a logical variable assignment.',
    }]
    resolver = sr.Resolver(B, bindings=bindings, index=index)
    for r in old:
        r['scope'] = rebindings.get(r['scope'], r['scope'])
        r['_resolver'] = resolver
        r['_scope'] = resolver.resolve(r['scope'])
        r['_interval'] = sr.parse_scope(r['scope'])
    errors = [e for e in errors if not re.match(r'line (\d+): first_use', e)]
    for r in old:
        if not resolver.contains(r['_scope'], r['first_use']):
            errors.append('rebound first_use outside scope: ' + r['first_use'])
parsed_new = []
for n, row in enumerate(new, 1):
    r = dict(row, _line=n, _resolver=resolver, _interval=sr.parse_scope(row['scope']))
    try:
        r['_scope'] = resolver.resolve(row['scope'])
        if not resolver.contains(r['_scope'], row['first_use']):
            errors.append('new first_use outside scope: ' + repr(row))
    except sr.RegistryError as exc:
        errors.append(str(exc))
    parsed_new.append(r)
collisions = sr.collision_check(old + parsed_new)
print(json.dumps({'groups': groups, 'scopes': additions, 'rows': new, 'counts': counts, 'rebindings': rebindings, 'errors': errors, 'collisions': collisions}, ensure_ascii=False))
