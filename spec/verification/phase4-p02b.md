# Phase 4 verification: Part 2.2

> **PASS VERDICT INVALIDATED (2026-08-12).** This note verified the revoked
> compressed-migration policy, not the binding full-transcription standard.
> Retain it only as audit evidence; see `FULL-TRANSCRIPTION-READINESS.md`.

Date: 2026-08-10
Visit: P2b, First-Order Logic
Verified source: `v1.1-verified`, Part III, lines 3022--6048; the live
`source/` tree is unchanged.

## Delivered scope

- Body: first-order signatures, syntax, capture-avoiding substitution,
  structures and satisfaction, definitional extensions; natural deduction,
  sequent, Hilbert, tableau, and resolution calculi; the Henkin construction,
  completeness, compactness, L\"owenheim--Skolem results, normal forms,
  Skolemization, unification, Herbrand methods, decidable fragments,
  interpolation, implicit definability, and the quantified subformula
  property.
- Registry: corrected the first-order natural-deduction sheet and added
  first-order tableaux and resolution. Every rule remains in
  `registry/calculi/`; no body chapter displays a rule.
- Annex: 47 items, in exact one-to-one correspondence with 44 `proved` and
  three `sketched` body results. The three sketches enumerate their omissions.
- Result inventory: 56 statused results -- 44 `proved`, three `sketched`, and
  nine `cited`.
- New lookup apparatus: quantifier-law, normal-form, decidable-fragment,
  metatheorem, and proof-system tables; a clausification pipeline and a
  resolution-refutation DAG.

The top-level `parts/p02.tex` and `annex/p02.tex` drivers remain deliberately
unassembled. Campaign order requires P2a, P2b, and P2c to finish before the
Part-2 finalizer replaces both Phase-3 stubs.

## Source-result and proof accounting

All 45 v1.1 result mappings were checked statement by statement: 40 complete
proofs remain `proved`, three sketches remain `sketched`, and two cited
results remain `cited`. No evidence class was upgraded.

The syntax/semantics and Henkin-completeness audit covered 32 proof-bearing
entries. Its 29 migrated complete proofs total 2,089/3,944 detex alphabetic
words = 53.0%; the migrated LK-completeness sketch is 200/422 = 47.4%. Two
additional complete annex proofs establish the new elementary-diagram upward
L\"owenheim--Skolem entry and its countable nonstandard-arithmetic corollary.
Every individual complete proof in that audit lies in the required 40--60%
band.

The remaining source mappings and ratios are:

| Body result | v1.1 lines | Evidence | Source to annex words | Ratio |
|---|---:|---|---:|---:|
| Invariance under reduct | 3995--4016 | complete | 81 to 43 | 53.1% |
| First-order ND soundness | 4112--4159 | complete | 239 to 138 | 57.7% |
| First-order LK soundness | 4161--4212 | complete | 309 to 161 | 52.1% |
| First-order NNF | 5156--5230 | complete | 226 to 98 | 43.4% |
| Rectified variant | 5232--5312 | complete | 399 to 184 | 46.1% |
| Prenex extraction | 5314--5391 | complete | 382 to 169 | 44.2% |
| Prenex normal form | 5393--5413 | complete | 74 to 42 | 56.8% |
| Skolem expansion--reduct theorem | 5447--5561 | complete | 617 to 288 | 46.7% |
| Simultaneous-substitution composition | 5689--5705 | complete | 44 to 23 | 52.3% |
| Clause substitution | 5707--5724 | complete | 60 to 35 | 58.3% |
| First-order unification | 5782--5803 | sketch | 152 to 65 | 42.8% |
| Resolution and Factoring soundness | 5824--5842 | complete | 98 to 43 | 43.9% |
| Resolution completeness | 5896--5916 | sketch | 129 to 70 | 54.3% |

The migrated citation-only entries are the Herbrand clause theorem
(v1.1 lines 5853--5861) and the lifting lemma (5863--5877). The three source
sketches are LK completeness, first-order unification, and resolution
completeness; every target retains an honest `\sketchnote`.

Four new results are proved in the annex: derived equality laws, the
Hilbert-FOL deduction theorem, upward L\"owenheim--Skolem via elementary
diagrams, and a countable nonstandard elementary model of arithmetic. Seven
new statements are citation-only: first-order tableau adequacy, quantifier
equivalences, clausal form, Herbrand's validity theorem, Craig interpolation,
Beth definability, and the quantified first-order subformula property.

## Repaired-source fidelity

The adversarial comparison found the following repaired dependencies intact:

- R-007/R-008: rectification, prenex extraction, Skolem expansion and reduct
  directions, fresh symbols, and the universal-prefix/clause convention;
- R-009: the transfinite Lindenbaum construction, with the countable
  choice-free recursion kept distinct;
- R-010: strong recursion for capture-avoiding substitution, including fresh
  renaming at unchanged subformula complexity;
- R-013: nonvacuous discharge remains binding in witness extension and
  maximal-consistency arguments;
- R-024: definitional extension preserves unique expansion, satisfaction,
  semantic consequence, and the stated derivability direction;
- R-025: exact first-order LK eigenvariable conditions and the equality scope;
- R-026: both compactness clauses retain their exact sentence/theory scope;
  and
- R-027: the countable-signature completeness corollary performs the explicit
  recursion without invoking choice.

The Henkin method retains witness saturation, quotient representative
independence, term evaluation, the truth lemma, and the final reduct. Exact
cardinal and choice hypotheses are retained in Tarski--Vaught and both
L\"owenheim--Skolem directions. The Herbrand validity form is correctly
existential; the dual universal-clause form remains in the resolution entry.

## Depth rows

Filled at their registered ceilings:

- D-P3-001: Hilbert FOL and its deduction theorem;
- D-P3-002: the first-order tableau sheet, adequacy statement, fairness, and
  countermodel extraction, completing the row after P2a's propositional half;
- D-P3-003: Herbrand universe, base, structure, and exact validity form;
- D-P3-004: Craig interpolation and Beth definability statements with their
  Part-7 proof route;
- D-P3-006: the decidable-fragments catalog with language/equality/function
  scope, problem orientation, complexity, and undecidable boundaries;
- D-P3-010: definitional extension and conservativity;
- D-P3-011: equality rules and consolidated metatheory;
- D-P3-012: quantifier equivalences and the clausal-form chain;
- D-P3-013: compactness applications, including the elementary-diagram
  construction and nonstandard arithmetic model; and
- D-P3-014: the qualified first-order subformula-instance property.

D-P3-005 (Robinson joint consistency) remains an explicit Part-3/E pointer,
and D-P3-007 (many-sorted logic) remains an explicit Part-2.4/E pointer. They
are not falsely marked complete by this visit. No register row is flipped
before global reconciliation.

## Apparatus

The visit delivers A-033--A-037, A-118, and A-121. The final verifier required
the following substantive repairs before accepting them:

- A-033 gained the two vacuous-quantifier laws with their nonempty-domain and
  free-variable side conditions;
- A-034 gained DNF, existence/scope, preservation, and size-growth columns;
- A-118 now shows NNF, rectification, prenex, Skolem, CNF, and clause-set
  stages separately;
- A-035 now states exact hypotheses, choice standing, and a defined regular-
  abstract-logic closure package rather than leaving Lindstr\"om's hypotheses
  implicit;
- A-036 fixes the guarded-fragment equality scope and records precise
  three-variable and arithmetic-multiplication undecidable boundaries; and
- A-037 now compares rule families, exact side conditions, scope, and adequacy
  evidence rather than merely listing registry homes.

The visit contributes to the cross-part rows A-182, A-186, and A-189. Source
exercises are deliberately retired as exercises; apparatus A-188 therefore
remains open.

## Adversarial correction log

Corrections after the first drafts included:

- supplied the complete paired NNF recursion at its definition site;
- repaired the tableau fairness condition to enumerate every closed term of
  the active countable language, and made the countermodel's reduct/expansion
  construction exact;
- preserved the universal prefix through matrix CNF and erased it only under
  the declared universal-closure clause convention;
- repaired an equality-transitivity freshness error and the strong
  substitution/conservativity proof boundaries;
- made witness extension respect nonvacuous discharge and supplied the missing
  expanded-signature cardinal bound in the elementary-diagram proof;
- distinguished literal support from substitution support, formula maps from
  term metavariables, tableau atomic data from Herbrand structures, and a
  local relation interpretation from the registered reflexive-transitive
  closure glyph;
- corrected the Herbrand finite expansion to use its declared matrix
  `\varphi` consistently;
- retained the propositional soundness cross-references inside the FOL
  calculus proofs, avoiding circular self-citations;
- calibrated every decidable-fragment row to its exact signature, equality,
  function-symbol, model, and decision-problem scope; and
- merged nine verified bibliography records and 33 collision-checked symbol
  rows, while rehoming eight existing symbols at their true first use.

## Mechanical and visual evidence

- Integrated P2a+P2b body/calculus/annex build: pass, 130 pages.
- All P2-local references and citations resolve. The five undefined references
  are intentional P1 targets omitted from the scratch driver.
- `python tools/check.py --tree handbook --strict`: pass on the frozen P2b
  slice before concurrent P2c drafting began.
- `python tools/check.py --tree source`: pass; `git diff -- source` is empty.
- `python tools/symbols2tex.py`: pass, 160 rows and 158 distinct glyphs.
- `git diff --check`: pass.
- Visual inspection covered the three new calculus sheets, all six Phase-4
  apparatus items, the normal-form and resolution figures, the Henkin method,
  the landscape depth tables, and representative annex pages. No clipping or
  unreadable P2b table remains. The requested 19.711-point completeness-intro
  overflow was removed.

After the P2b slice passed, concurrent P2c drafting introduced expected
temporary missing-annex and missing-bibliography findings. None points into a
P2b file, and no P2c file is part of this visit's commit.

Compilation verifies typesetting, not mathematics. The independent source,
status, proof-compression, standards, and counterexample-oriented reviews are
separate evidence. Registers remain unchanged until the globally integrated
Phase-4 tree exists.
