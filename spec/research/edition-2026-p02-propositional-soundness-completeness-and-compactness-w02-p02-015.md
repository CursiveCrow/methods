# w02-p02-015: P2 section 14.7, interpolation boundary cases (D-P2-006)

## Provenance

- Gap addressed: D-P2-006-GOAL-03 (empty shared vocabulary; inconsistent and valid
  endpoints under the actual constant convention), and through it the composite
  D-P2-006-C01. Before this packet the whole treatment was the last sentence of
  annex:p2.3.9 (handbook/annex/p02/propositional-metatheory-supplement.tex:54-56).
- Constant convention read in this session from
  handbook/restoration/inherited-01661-01816.tex: alphabet (lines 4-19, bottom a
  nullary connective), formation clauses (21-34), topv := neg bottom (48-58),
  finite conjunction/disjunction with n = 0 values topv / bottom (60-79).
  Valuation clause v-hat(bottom) = F, coincidence lemma (lem:prop-coincidence)
  and semantic notions read from handbook/restoration/inherited-01817-01898.tex
  lines 1-66.
- Construction treated: Method def:p02-interpolant-truth-table and Lemma
  thm:p02-interpolant-truth-table-correctness at
  handbook/parts/p02/propositional-metatheory-supplement.tex:131-166 (read-only
  host, not edited). Definition def:p02-w02-p02-015-output makes the method's
  "complete conjunction ... in lexicographic order" exact; it introduces no new
  construction.
- Part 7 relation: def:p07-maehara-method in
  handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex:96-109
  (on the p07 route, parts/p07.tex line 106) mentions interpolants at initial
  and bot-L leaves; nothing more is claimed.
- All results and proofs are derived editorially from the inherited definitions;
  none is attributed to Craig 1957. Craig1957 is cited only by key (no locator)
  as the origin of the theorem; no Craig locator was verified.
- Editorial macro note: \Fm, \CPL, \set, \True, \False and \Var are
  restoration-only macros; the files use \mathsf{Fm}_{\mathsf{CPL}}, \{...\},
  \mathbf{T}, \mathbf{F}, \operatorname{Var}.

## Existing treatment found

- Listed: annex:p2.3.9 and sec:p02-prop-interpolation (supplement, on route).
- Also present: handbook/parts/p02/propositional-metatheory.tex:165-195 and
  handbook/annex/p02/propositional-metatheory.tex:137 carry the same labels
  (that file is not input by parts/p02.tex lines 22-23); not cited.
- No other handbook treatment of the empty-shared-vocabulary case was found
  (searched handbook/parts, annex, restoration for "empty shared", "no common
  variable", "no shared variable").

## Continuation

- GOAL-03 text is in body sec:p02-w02-p02-015-interpolation-boundary and annex
  sec:annex-p02-w02-p02-015-interpolation-boundary. unit-compile ok, overfull 0,
  find_fused_spaces no hits, check.py --tree no finding on these files.
- Open for the lead: insert the two \input lines per the packet insertion
  proposal (drivers read-only here); merge the symbol intake.
