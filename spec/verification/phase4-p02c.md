# Phase 4 verification: Parts 2.3 and 2.4

> **PASS VERDICT INVALIDATED (2026-08-12).** This note verified the revoked
> compressed-migration policy, not the binding full-transcription standard.
> Retain it only as audit evidence; see `FULL-TRANSCRIPTION-READINESS.md`.

Date: 2026-08-10
Visit: P2c, Higher-Order Logic and Variants
Verified source: `v1.1-verified`, Part IX; the live `source/` tree is unchanged.

## Delivered scope

- Body: relational second-order syntax; full and Henkin semantics; full
  comprehension; second-order arithmetic; full-semantic categoricity,
  noncompactness, and non-enumerability boundaries; the exact incidence
  reduction and matched relational calculus; simple type theory; strict
  many-sorted logic; free logic; infinitary logic; generalized-quantifier and
  analytical-hierarchy pointers; and the full-versus-Henkin comparison.
- Registry: `sheet:sol` displays four relation-quantifier rules plus the
  comprehension and choice schemas.  Every rule has five arguments and exact
  side conditions; no body chapter displays a rule.
- Annex: nine items in exact one-to-one correspondence with seven `proved`
  and two `sketched` body results.  Both sketches enumerate their omissions.
- Result inventory: thirteen statused results -- seven `proved`, two
  `sketched`, and four `cited`.
- Apparatus: A-038, A-039, and A-091; the central Part-14 calculus catalog now
  renders every current sheet, including `sheet:sol`.
- Integration: the P2a, P2b, and P2c body and annex drivers are assembled and
  end with the generated Part-2 audit register.

## Source and evidence accounting

Every status-bearing Part-IX result was compared against the repaired source.
No evidence class was upgraded.  Full comprehension, PA2 categoricity,
full-semantic noncompactness, the two L\"owenheim--Skolem failures, and the
incidence translation retain complete annex proofs.  Effective
non-enumerability and typed substitution remain sketches with explicit
omission ledgers.  Full real categoricity and typed Henkin completeness remain
citation-only.

The established `detex` alphabetic-word method gives:

| Migrated unit | Source to annex words | Ratio |
|---|---:|---:|
| Full comprehension | 47 to 26 | 55.3% |
| PA2 categoricity | 192 to 101 | 52.6% |
| Full noncompactness | 93 to 51 | 54.8% |
| No effective completeness | 89 to 46 | 51.7% |
| Incidence correspondence | 144 to 79 | 54.9% |
| Typed substitution and beta soundness | 129 to 75 | 58.1% |
| L\"owenheim--Skolem derivation | 90 to 46 | 51.1% |

Every migrated proof or sketch lies in the required 40--60% band.

## Repaired-source fidelity

- R-031: the full-semantics categoricity argument retains the injectivity
  induction and the exact second-order induction standing.
- R-032: the second-order arithmetic language, induction axiom, and all four
  recursion axioms for addition and multiplication precede their use.
- R-033: full real categoricity is a labeled `cited` theorem with the exact
  least-upper-bound sentence, the local definition of `\leq`, and the
  common-rational-cuts proof-method citation.  The downward
  L\"owenheim--Skolem counterexample points explicitly to that label.

The simple-type entry also preserves typed constant interpretations, the
typed universal-binder abbreviation, curried application, and the exact
functional-extensionality formula while distinguishing an extensionality
axiom from identity-of-functions semantics.

## Depth rows and ceilings

- D-P9-001 is filled at E by the displayed second-order calculus, exact
  comprehension and choice schemas, translation-defined derivability, and
  matched-model adequacy.
- D-P3-007 is filled at E by strict many-sorted syntax, semantics, guard
  translation, sort axioms, and exact consequence reduction.
- D-P3-008 receives its required P2.4 free-logic statement/comparison and
  Part-8 pointer; its final P8 home remains open.
- D-P3-009 and N-a-059 remain honestly open and are named by an explicit
  `\hbstub`; the supplied infinitary statement does not falsely close the
  requested full entry.
- N-a-060 remains a pointer-only generalized-quantifier obligation for P3.
- D-P9-002 receives the required analytical-hierarchy pointer to P4.

The Lindstr\"om theorem is deliberately relocated to P3 as required by the
work order.  The P2.4 pointer nevertheless states its exact regularity,
extension, invariance, compactness, and downward-LS hypotheses and preserves
its cited provenance.  Source exercises are retired as exercises; no theorem
or proof status is inferred from them.  Registers remain unchanged until
global reconciliation.

## Adversarial correction log

The independent fidelity and standards passes corrected:

- free-variable-only guards, which admitted junk assignments and also hid a
  choice requirement for unused sorted variables, were replaced by the
  definition-before-use all-variable assignment guard;
- the guard covers both object and relation variables, blocks the
  `forall y P(y)` / `P(x)` counterexample, and supports the eigenvariable rules
  by discharge followed by weakening;
- the canonical incidence model now tags every sort, symbol value, and
  assignment, so it is genuinely strict even when the untagged carriers
  overlap set-theoretically;
- the reverse many-sorted construction uses one global junk point for
  ill-typed function inputs and is choice-free;
- the advertised two-sided SOL sheet acquired an exact derivability meaning,
  including empty succedents, and all six displayed additions were proved
  admissible for that projection;
- extensional collapse now retains object constants/functions, transports the
  counterassignment, and handles relation-parameter representatives without
  assuming relation equality;
- upward L\"owenheim--Skolem transfer was restricted to a specified infinite
  sort, and the matched SOL instance to an infinite object sort;
- typed equality was separated from global alpha-equivalence as
  `\mathsf{Eq}_{\alpha}` and used with the declared curried grammar;
- the exact real-completeness sentence, R-033 label dependency, typed semantic
  data, binder abbreviation, Lindstr\"om hypotheses, extensionality formula,
  and relation-term scope were restored after the source crosscheck; and
- long theorem headings, schema displays, comparison tables, the SOL sheet,
  and annex titles were reflowed until the owned slice had no overfull boxes.

## Mechanical and visual evidence

- Independent isolated P2c TeX Live build: pass, 32 pages.
- Integrated handbook build: pass, 332 pages, with biber and makeindex.
- All handbook citations and references resolve in the integrated build.
- `python tools/check.py --tree handbook --strict`: pass; 202 symbol rows,
  323 bibliography entries, 88 proved / 9 sketched / 35 cited globally, and
  zero malformed statuses.
- `python tools/check.py --tree source`: pass; `git diff -- source` is empty.
- `python tools/symbols2tex.py`: pass; 202 rows and 199 distinct glyphs.
- `git diff --check`: pass.
- Visual inspection covered every P2c body and annex page, A-038/A-039/A-091,
  the exact least-upper-bound and assignment-guard displays, typed
  extensionality, and both rendered SOL-sheet pages.  No owned clipping,
  collision, unreadable condition, or overfull box remains.

Compilation verifies typesetting, not mathematics.  The separate
source-fidelity, counterexample, status, proof-compression, standards, and
visual reviews are recorded independently above.
