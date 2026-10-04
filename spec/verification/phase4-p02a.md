# Phase 4 verification: Part 2.1

> **PASS VERDICT INVALIDATED (2026-08-12).** This note verified the revoked
> compressed-migration policy, not the binding full-transcription standard.
> Retain it only as audit evidence; see `FULL-TRANSCRIPTION-READINESS.md`.

Date: 2026-08-10
Visit: P2a, Propositional Logic
Verified source: `v1.1-verified`, Part II, lines 1649--3021; the live
`source/` tree is unchanged.

## Delivered scope

- Body: propositional syntax and unique readability; two-valued semantics;
  substitution, equivalence laws, controlled-prose translation, clauses and
  normal forms; duality and Post's criterion; natural deduction, finite-
  multiset sequents, a Hilbert calculus, analytic tableaux, and the five-way
  proof-system comparison; soundness, completeness, compactness,
  interpolation, resolution, Davis--Putnam elimination, decidability, and
  SAT/TAUT complexity.
- Registry: corrected `nd-cpl`; added `tableaux-cpl` and `resolution-cpl`;
  reused the existing `hilbert-cpl` and `lk` sheets.  No body chapter
  redisplays a calculus rule.
- Annex: 22 items -- 21 complete proofs and one honest sketch.  Seventeen
  complete items migrate complete v1.1 proofs; four complete items prove new
  depth-fill results (duality, Hilbert deduction, truth-table interpolant
  correctness, and dual-Horn tractability).  The sole source sketch, LK
  completeness, remains `sketched` and enumerates its omitted translation
  trees.
- Result inventory: 37 statused results -- 21 `proved`, one `sketched`, and
  15 `cited`.  Every `proved`/`sketched` target resolves to exactly one annex
  item and every annex item has exactly one body back-reference.
- Lookup apparatus: six body tables and seven body figures, plus five
  rendered calculus sheets used by the visit.
- Generated Part-2 audit: 71 labeled entries in the present unassembled Part
  2 tree.

The top-level `parts/p02.tex` and `annex/p02.tex` drivers are deliberately not
assembled by this visit.  The campaign order requires P2a, P2b, and P2c to
finish first; the Part-2 finalizer will then replace the Phase-3 driver stubs
with all three visits at once.

## Source-result and proof accounting

All 18 v1.1 result mappings were compared statement by statement.  The table
records alphabetic proof-word counts after `detex`; result headers are
excluded.  Every complete Tier-2 migration is within the required 40--60%
band.  The sketch is shown separately and is also within that band.

| v1.1 result | Source evidence | Target annex item | Source to target words | Ratio |
|---|---|---|---:|---:|
| Parenthesis counting | complete | P2.1.1 | 153 to 66 | 43.1% |
| Unique readability | complete | P2.1.2 | 179 to 75 | 41.9% |
| Propositional coincidence | complete | P2.1.3 | 39 to 19 | 48.7% |
| Clause satisfaction | complete | P2.1.4 | 157 to 83 | 52.9% |
| Negation normal form | complete | P2.1.5 | 70 to 40 | 57.1% |
| Conjunctive/disjunctive normal forms | complete | P2.1.6 | 559 to 265 | 47.4% |
| Functional basis | complete | P2.1.7 | 46 to 24 | 52.2% |
| Substitution for open assumptions | complete | P2.CALC.1 | 155 to 92 | 59.4% |
| Natural-deduction soundness | complete | P2.3.1 | 191 to 101 | 52.9% |
| LK soundness | complete | P2.3.2 | 360 to 198 | 55.0% |
| Maximal-consistent-set closure | complete | P2.3.3 | 223 to 119 | 53.4% |
| Countable Lindenbaum lemma | complete | P2.3.4 | 74 to 41 | 55.4% |
| Propositional truth lemma | complete | P2.3.5 | 60 to 32 | 53.3% |
| Natural-deduction completeness | complete | P2.3.6 | 112 to 49 | 43.8% |
| Fixed-language compactness | complete | P2.3.7 | 49 to 27 | 55.1% |
| LK completeness | sketch | P2.3.8 | 381 to 180 | 47.2% |
| Resolution soundness | complete | P2.3.10 | 72 to 37 | 51.4% |
| Resolution completeness | complete | P2.3.11 | 370 to 190 | 51.4% |

The aggregate for the 17 complete source proofs is 1,458/2,869 = 50.8%.
Compression did not delete the source repairs or load-bearing cases:

- R-011: the clause lemma retains both downward inductions; the CNF proof
  retains non-initial variable indices, increasing literal-code order, the
  exact clause interpretation, validity, and both variable-free values.
- R-013: no repetition rule or vacuous-discharge license was reintroduced.
  Open-assumption substitution uses globally fresh, pairwise-disjoint label
  sets; maximal-consistency and completeness retain the genuine-use
  conjunction/deduction detours.
- R-014: LK completeness keeps the exact finite-multiset scope, empty
  antecedent and succedent cases, multiple succedents, primitive Cut, and a
  `sketchnote` disclaiming cut elimination and listing the omitted
  rule-by-rule translation trees.
- R-023: Davis--Putnam is attributed only to variable elimination;
  resolution is attributed to Robinson.  The arbitrary-set resolution step
  uses compactness and explicitly selects one preimage clause per member of
  the finite unsatisfiable image, without assuming the clause-interpretation
  map is injective.

Exact retained hypotheses include `m>0` in the clause-conjunction result,
nullary arity in functional completeness, a fixed countable propositional
language in Lindenbaum and compactness, arbitrary finite-multiset contexts
for LK, finite roots for tableaux, and arbitrary clause sets only after the
compactness extension.

## Remaining source disposition

Every Part-II definition, method, warning, and non-exercise distinction is
represented in the three body chapters or the registry sheets.  Source
exercises are deliberately retired as exercises: their substantive content
is either promoted to a lookup entry (substitution, replacement, normal-form
and equality-style congruence facts), represented by the proof-system and
decision tables, or routed to later parts.  Consequently apparatus A-188,
which asks for exercise-to-solution links, remains open rather than being
falsely marked done.

The arbitrary-language extension is not silently implied by the fixed
countable development.  D-P2-011 is an explicit stub, and arbitrary-language
choice calibration is deferred at its registered ceiling.

## Depth rows

Filled at their register ceilings:

- D-P1-005: Ultrafilter Lemma / Boolean Prime Ideal Theorem versus arbitrary
  propositional compactness, with the exact fixed-language distinction;
- D-P2-001: Hilbert CPL, deduction theorem, and the ND/LK/Hilbert comparison;
- D-P2-002: Post's five maximal clones, exact criterion, negative tests,
  NAND/NOR, and an honest upper-cover figure rather than a false full lattice;
- D-P2-003: duality definition, table, theorem, and annex proof;
- D-P2-004: decidability theorem;
- D-P2-005: SAT NP-completeness and TAUT coNP-completeness statements with
  concrete encoding standing and a Part-4 forward pointer;
- D-P2-006: interpolation theorem plus a separately proved truth-table
  construction;
- D-P2-007: precise Tseitin existential-projection/equisatisfiability
  statement and Part-12 forward pointer;
- D-P2-008: Horn-SAT and 2-SAT full entries, with dual-Horn and XOR rows in
  the tractability table; and
- D-P2-010: uniform substitution and replacement congruence.

D-P2-011 is present as an explicit `\hbstub` with its row id, as required for
the `could` row.  P2a completes the propositional half of D-P3-002; the row
remains open until P2b supplies first-order tableaux and their completeness.
No depth row is flipped in the CSV before global reconciliation.

## Apparatus

New Phase-4 deliverables are A-027--A-032, A-114--A-117, and A-119--A-121.
A-024 and A-161 are reused from the verified P1 visit rather than duplicated.
The visit supplies the Part-2.1 contributions to A-182, A-186, and A-189;
those cross-part rows remain open pending final integration.  A-188 remains
open for the deliberate exercise retirement stated above.

## Adversarial correction log

The visit was treated as wrong until rechecked.  Corrections after the first
draft included:

- rejected the stale A-001 wording that would have reintroduced repetition
  and vacuous discharge contrary to repaired v1.1 and the live ND sheet;
- replaced an out-of-alphabet `q_0` in the Hilbert translation by the
  declared variable `p_0`, preserving its uniformly false role;
- repaired BNF metavariable reuse, connective associativity, clause-set
  satisfaction, literal complementation, tautological clauses, and deletion
  invariance;
- replaced globally reserved substitution/translation letters with scoped,
  registered notation and merged 22 collision-checked symbol rows;
- corrected Post's clone table, NAND/NOR constant recovery, positive-arity
  versus nullary-inclusive completeness, and the upper-cover/full-lattice
  distinction;
- gave Tseitin the exact unique-extension/existential-projection statement,
  without claiming same-vocabulary logical equivalence;
- rebuilt the natural-deduction example as a genuine tree, linked every
  calculus mention to a real sheet, retained branch formulas in tableaux, and
  put every pivot/complement condition directly on the resolution rule;
- corrected Davis--Putnam by deleting tautologies, requiring an occurring
  pivot, defining the reduced set, and claiming strictly fewer rather than
  exactly one fewer occurring variables;
- added an evidence-bearing correctness theorem for the derived truth-table
  interpolant construction instead of laundering it through Craig's citation;
- made the SAT/TAUT encoding, malformed-string policy, complexity classes,
  completeness definition, 2-SAT SCC criterion, and input-size measures
  exact;
- verified the direct Arora--Barak locator for TAUTOLOGY coNP-completeness;
- rerouted the resolution DAG to remove an ambiguous crossing and made the
  coined maximal-consistent-set method satisfy the naming rule through actual
  annex use;
- restored the noninjective preimage-selection step in the arbitrary-set
  resolution proof; and
- after a source audit found 12 per-proof compression overruns, shortened each
  one into the 40--60% band and then rechecked all repaired steps.

## Mechanical and visual evidence

- `python tools/check.py --tree handbook --strict`: pass.
- `python tools/check.py --tree source`: pass.
- `python tools/audit_tables.py`: 14 outputs, 133 rows; P2 currently has 71
  rows.
- `python tools/symbols2tex.py`: 127 rows, 125 distinct glyphs, 9 scope
  groups.
- `git diff --check`: pass; `source/` has no diff.
- Isolated P2a body/calculi/annex build: pass, 54 pages, bibliography and index
  generated.  Its only unresolved references are the four intentional P1
  references omitted from the scratch driver; every P2a-local reference and
  citation resolves.
- Full-tree metrics at this visit: 304 bibliography entries, 38 stubs, global
  statuses `proved=37`, `sketched=4`, `cited=22`.
- Visual inspection covered the syntax tree, equivalence/normal-form material,
  Tseitin statement, Post table and upper-cover figure, natural-deduction and
  LK trees, ND/LK correspondence, closed tableau, landscape proof-system
  comparison, interpolation, resolution DAG, tractable-class table, all five
  calculus sheets, and the compressed annex pages.  No clipping, ambiguous
  edge crossing, unreadable table, or P2a content overflow remains.

Compilation verifies typesetting, not mathematical correctness.  The two
independent source/status/proof audits above are separate evidence.  The
registers remain unchanged until the globally integrated Phase-4 tree exists.
