"""Prepare scoped current-fulfillment edits for actually integrated writing.

The immutable source-facet baseline is not changed; no independent acceptance
is inferred from an author's supplied proof or a structural reader route.
"""
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
FOLDER = ROOT / 'spec/coverage/edition-2026/current-fulfillment'
updates = {
    '5.6': ('authored_unreviewed', 'p01/equivalence-closure-and-quotients', 'sec:p01-equivalence-closure-and-quotients', [], 'The complete construction, leastness, quotient classes, choice-free factorization and connected finite counterexample are supplied with four full author proofs.'),
    '14.5': ('authored_unreviewed', 'p01/boolean-prime-ideal-and-ultrafilters', 'thm:p01-bpi-propositional-compactness', [], 'The inherited countable case and the newly routed arbitrary-set BPI equivalence provide the recorded compactness extent; the complete body and compactness bridge were read.'),
    '14.6': ('authored_unreviewed', 'p01/boolean-prime-ideal-and-ultrafilters', 'thm:p01-bpi-equivalence', [], 'The Boolean prime ideal, Boolean ultrafilter extension, set ultrafilter and arbitrary propositional compactness directions are supplied by full author proofs. Choice separation remains accurately cited.'),
    '14.8': ('partial', 'p01/boolean-prime-ideal-and-ultrafilters', 'sec:p01-bpi-compactness-bridge', ['The new Boolean quotient/extension and compactness proofs do not replace the still-outlined calculus-specific Lindenbaum/free-Boolean-algebra completeness construction and its complete derivability correspondence.'], 'Boolean quotient, finite evaluation and extension dependencies are now supplied; the narrower algebraic-completeness residual is retained.'),
    '77.1': ('authored_unreviewed', 'p06/proper-forcing-and-master-conditions', 'sec:p06-proper-forcing-master', [], 'The hereditary-size ambient set, actual countable hulls/clubs, predensity/master tests, antichain equivalence and properness constructions are supplied at the recorded ZFC scope.'),
    '77.2': ('partial', 'p06/proper-forcing-and-master-conditions', 'sec:p06-pfm-semiproper', ['The definitions and proper-to-semigeneric club implication are supplied; a full separately developed semiproper preservation/comparison treatment and the distinct original source extents remain owed.'], 'The recorded missing single-poset core is now reader-routed, with complete supplied proofs; broader semiproper coverage is not inferred.'),
    '133.2': ('partial', 'p09/negative-premises-and-stratification', 'sec:p09-negative-premises', ['The full publisher chapter and remainder of the separate 133-page author presentation remain owed, including the wider proof-answer hierarchy and referred dependencies. The supplied seven-proof negative-premise/ordinal/semantic core is not absent.'], 'Actual arbitrary-premise positive closure, stable/well-supported/well-founded meanings, ordinal stratification, source countermodels and process applications are supplied.'),
    '137.2': ('partial', 'p09/timed-automata-regions-and-zones', 'sec:p09-timed-automata-regions-and-zones', ['The full source allocations, progressing/infinite timed acceptance and practical DBM extrapolation variants are not supplied by the finite reachability/region-union construction.'], 'The clock model, region and diagonal-sensitive construction, strict DBM operations and finite exact search are now supplied with nine full author proofs.'),
    '164.2': ('partial', 'p15/hume-and-the-problem-of-induction', 'sec:p15-hume-and-the-problem-of-induction', ['Pre-Hume history and the distinct full Lange2011 allocated chapter remain unsupplied; the 1777 Enquiry treatment does not replace them or the Treatise.'], 'The complete new Hume reader treatment is routed and its 1777 scholarly copytext identity is explicit; all its selected philosophical distinctions and examples were read.'),
    '164.3': ('partial', 'p15/whewell-mill-scientific-induction', 'sec:p15-whewell-mill', ['Forster2011 pp.93--115 and all three allocated components remain unacquired/unread; the separately sourced primary-book comparison is not a replacement.'], 'The actual Whewell1858/Mill1882 primary comparison, all five canons and two finite separating constructions are supplied and routed.'),
    '164.9': ('partial', 'p15/goodman-projectibility', 'sec:p15-goodman-projectibility', ['Complete original/revised entrenchment and projectibility constructions and the complete Schwartz2011 chapter remain owed. The newly held fourth-edition source reading continues separately.'], 'The original chapter-III grue/bleen, representation and confirmation argument has a routed distinct treatment with three supplied proofs; the unidentified teaching-scan edition is not promoted.'),
    '165.3': ('partial', 'p15/probability-quantifiers', 'sec:p15-probability-quantifiers', ['Keisler1985 pp.509--556, C001--C005, remain unacquired/unread. General measure/conditional-expectation/full-language completeness and the remaining distinct Keisler--Lotfallah elimination work are not supplied by the new finite treatment.'], 'A distinct finite-model probability-binder treatment supplies actual syntax, both measures, size-indexed translation and critical-threshold countermodels with three full proofs.'),
    '166.9': ('authored_unreviewed', 'p15/rissanen-structural-and-numerical-inference', 'sec:p15-rissanen-structural-and-numerical-inference', [], 'The complete original1978 source-specific structural/numerical argument is reconstructed with seven supplied proofs, declared approximation/precision/code boundaries, corrected constants and separate comparisons. This does not close the whole broader MDL method facet.'),
    '169.3': ('partial', 'p15/fisher-estimation-and-regularity', 'sec:p15-fisher-estimation', ['The full grouping/Fourier, Pearson joint/covariance and curve regimes, general location/scaling, discrete/Poisson/dilution and justified asymptotic source arguments remain owed. Five exact core proofs do not establish general MLE sufficiency or full-paper completion.'], 'The exact original1922 scan is held, and the routed core preserves estimation properties, coordinates, score/information conditions, sufficiency failure and Cauchy examples.'),
    '176.2': ('partial', 'p16/peirce-abduction-and-inquiry', 'sec:p16-peirce-abduction-and-inquiry', ['Psillos2011 pp.117--151 C001--C003 and intervening Peirce original presentations remain unsupplied. The two distinct complete electronic-primary texts do not substitute for the allocated historical chapter or its unprinted proofs.'], 'The substantive Peirce1878 and1908 primary comparison is reader-routed, with rule/case/result, concrete countercases, inquiry stages and precise omitted-proof boundaries.'),
    '186.7': ('authored_unreviewed', 'p16/nonmonotonic-causal-theories', 'sec:p16-nct-semantics', [], 'At the selected complete Turner2008 chapter extent, causal semantics, SE-characterization and definite completion have supplied full proofs; broader first-order/UCL referrals retain their cited standing.'),
    '186.8': ('authored_unreviewed', 'p16/nonmonotonic-causal-theories', 'sec:p16-nct-action-cases', [], 'All six selected-source action cases, domains, implied preconditions, nondeterminism and tendencies are supplied with exact author-proved outcomes and counts, without invented probabilities.'),
    '186.9': ('partial', 'p16/nonmonotonic-causal-theories', 'sec:p16-nct-cplus', ['The complete C+ grammar/general translation and its separately allocated original-source developments remain owed; the two displayed descriptions and their path proof are not the whole language.'], 'The complete displayed Turner2008 C+ fragment and state/transition/path correspondence are supplied; broader action-language work remains distinct.'),
}
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if '--followon-only' in __import__('sys').argv:
    updates = {
        '14.8': ('authored_unreviewed', 'p02/free-boolean-algebra-and-completeness', 'sec:p02-free-boolean-completeness', [], 'The actual syntactic Boolean quotient/free property, rule-by-rule Boolean-valued ND soundness, exact generated-filter/derivability correspondence, proper avoiding filter and BPI-relative completeness are now supplied by seven full author proofs; earlier cited statements retain their standing.'),
        '133.2': ('partial', 'p09/sos-congruence-and-conservative-extension', 'sec:p09-sos-formats', ['The general panth-to-ntree/congruence transformation, recursive/binding/many-sorted variants, wider proof-answer hierarchy and distinct publisher/full-author source units remain owed. The full first-order conservativity and declared local-input/GSOS results are supplied.'], 'The new eight-proof continuation supplies conservative extension, semantic projection/lifting, a complete declared local congruence class and source failures, alongside the previously routed negative-premise core.'),
        '164.9': ('partial', 'p15/goodman-entrenchment-and-projectibility', 'sec:p15-goodman-entrenchment-and-projectibility', ['Original first/second-edition rules, the separate original1970 paper and the complete Schwartz2011 chapter remain unsupplied. The revised fourth-edition IV.1--IV.6 construction is now present, not an outstanding outline.'], 'The exact fourth-edition chapter-IV definitions, complete selected cases, override/parity distinction and comparative arguments are supplied, with three full formal consequences and philosophical/normative boundaries.'),
        '165.3': ('partial', 'p15/probability-quantifier-elimination', 'sec:p15-probability-elimination', ['All original Keisler1985 chapter components C001--C005 remain unacquired/unread. Full-language completeness/general measure/conditional expectation and journal-version identity are not supplied by the distinct finite-model author manuscript.'], 'The distinct Keisler--Lotfallah finite-model core and seven-proof noncritical/common-class/parametric/size-dependent continuation are now supplied; source corrections and exact hypotheses are retained.'),
        '169.3': ('partial', 'p15/fisher-grouping-and-moments', 'sec:p15-fisher-grouping', ['Fixed-grid information periodic remainder, grouped-MLE existence/limit and goodness-of-fit calibration remain owed; full TypeIII/joint, location/scaling, Pearson regime, near-normal moment, Poisson/dilution and general sufficiency/asymptotic source arguments are still partial. The new Fourier/phase-average/moment/cell-likelihood constructions are supplied.'], 'The six-proof grouping continuation supplies fixed/averaged recording distinctions, complete Fourier coefficients/tails, moment conditions, normalized likelihood, the actual300-error table, information loss and qualified expansions.'),
        '171.5': ('partial', 'p15/vc-dimension-and-uniform-learning', 'sec:p15-vcl-capacity', ['The original1971 source-specific entropy/necessary-and-sufficient construction, whole2011 source-version treatment and general non-core/outer-probability framework remain owed. The complete Sauer and measurable-core uniform-deviation sufficient route is now supplied.'], 'General infinite-class traces, zero/infinite VC dimension, actual measurable-core witness/split construction and uniform bounds are supplied with complete proofs.'),
        '171.6': ('partial', 'p15/vc-dimension-and-uniform-learning', 'sec:p15-vcl-learning', ['Whole original/source-version obligations and broader real-loss/minimax/general admissibility regimes remain unclosed; mathematical measurable ERM is not asserted to be an effective terminating search.'], 'The actual measurable empirical minimizer, agnostic excess risk, independent same-law validation and finite sufficient sample sizes are supplied, distinct from realizability.'),
        '171.7': ('partial', 'p15/vc-dimension-and-uniform-learning', 'sec:p15-vcl-examples', ['Original1971 necessary-and-sufficient/source-specific estimates, broader real-loss/noise theory and minimax lower bounds remain distinct residuals.'], 'The supplied conditional estimates and worked memorizer/noisy-label/infinite-capacity cases preserve realizable versus agnostic and fixed-law versus distribution-free distinctions.'),
        '186.9': ('partial', 'p16/cplus-action-language', 'sec:p16-cplus-action-language', ['Publisher-final/version comparison, later C+ extensions/CCalc and broader nonpropositional developments remain owed. The captured April2003 complete three-law grammar, all17 abbreviation conventions and six proved correspondences are now supplied.'], 'The full captured original C+ grammar, values/events, finite histories, rigid compression and source examples are supplied separately from the earlier Turner fragment.'),
        '220.8': ('partial', 'p19/self-explanation-and-learning', 'sec:p19-self-explanation-and-learning', ['Exact Oxford2012 chapters14/12 and their full source/version allocations remain unheld; broader empirical coverage is not inferred from three qualified primary studies.'], 'The complete bounded primary physics/biology/diffusion studies supply actual coding, designs, samples, outcomes, nulls, mechanism limits, three evidence tables and two worked processes.'),
        '227.7': ('partial', 'p19/aging-goals-and-reasoning', 'sec:p19-aging-goals-and-reasoning', ['Exact Oxford33 and Hess--Emery source extents, full emotional-goal/wisdom comparisons and Taylor supplements remain owed; no all-population trajectory or individual diagnosis is claimed.'], 'Four complete qualified primary records supply contextual engagement/choice, longitudinal expertise and targeted randomized training, retaining sample and uncertainty distinctions.'),
        '227.8': ('partial', 'p19/aging-goals-and-reasoning', 'sec:p19-aging-training', ['Full original source/version extents and broader support/compensation mechanisms remain owed. ACTIVE has no younger group and does not establish elimination of an age gap; the expertise interaction was not detected.'], 'The exact trial, task-structure and expertise records establish bounded supports/trained-outcome contrasts, not universal transfer or equality inferred from nonsignificance.'),
    }
supplementary = {
    '133.2': [('p09/negative-premises-and-stratification', 'sec:p09-negative-premises')],
    '164.9': [('p15/goodman-projectibility', 'sec:p15-goodman-projectibility')],
    '165.3': [('p15/probability-quantifiers', 'sec:p15-probability-quantifiers')],
    '169.3': [('p15/fisher-estimation-and-regularity', 'sec:p15-fisher-estimation')],
    '186.9': [('p16/nonmonotonic-causal-theories', 'sec:p16-nct-cplus')],
}
patches = []
changes = []
for shard in sorted(FOLDER.glob('*.jsonl')):
    for line in shard.read_text(encoding='utf-8-sig').splitlines():
        row = json.loads(line)
        sid = row['section_id']
        if sid not in updates:
            continue
        status, stem, anchor, missing, basis = updates[sid]
        evidence = []
        for directory in ['parts', 'annex']:
            path = ROOT / 'handbook' / directory / (stem + '.tex')
            if not path.is_file():
                continue
            data = path.read_bytes()
            evidence.append({
                'path': path.relative_to(ROOT).as_posix(),
                'anchor': anchor if directory == 'parts' else None,
                'line_start': 1, 'line_end': len(data.decode('utf-8-sig').splitlines()),
                'read_extent': 'Complete body read for this bounded drafting disposition; annex is author-supplied full proof evidence with reciprocal routing checked, not an independent proof-validity review.' if directory == 'parts' else 'Supplied author proof annex; extent/source hash recorded, reciprocal integration checked, no independent semantic review inferred.',
                'route_state': 'on_current_recursive_input_route',
                'sha256': hashlib.sha256(data).hexdigest(),
            })
        old_status = row['status']
        for other_stem, other_anchor in supplementary.get(sid, []):
            path = ROOT / 'handbook/parts' / (other_stem + '.tex')
            data = path.read_bytes()
            evidence.append({'path': path.relative_to(ROOT).as_posix(), 'anchor': other_anchor, 'line_start': 1, 'line_end': len(data.decode('utf-8-sig').splitlines()), 'read_extent': 'Previously read and integrated prerequisite body, retained alongside the continuation; no independent semantic admission.', 'route_state': 'on_current_recursive_input_route', 'sha256': hashlib.sha256(data).hexdigest()})
        row.update(status=status, fulfillment_basis=basis, reader_evidence=evidence,
                   missing_pieces=missing, observed_utc=now,
                   independent_admission=False, source_obligations_preserved=True)
        row['integration_qualification'] = 'Current drafting disposition only. Frozen source-facet/version allocations and promised proof duties are preserved; no whole-facet, whole-chapter, publication or independent acceptance.'
        updated = json.dumps(row, ensure_ascii=False, separators=(',', ':'))
        patches.append('*** Begin Patch\n*** Update File: ' + shard.as_posix() + '\n@@\n-' + line + '\n+' + updated + '\n*** End Patch')
        changes.append({'section_id': sid, 'before': old_status, 'after': status,
                        'reader_path': evidence[0]['path'], 'anchor': anchor})
assert len(changes) == len(updates), ('missing planned IDs', len(changes), len(updates))
print(json.dumps({'patches': patches, 'changes': changes, 'observed_utc': now}, ensure_ascii=False))
