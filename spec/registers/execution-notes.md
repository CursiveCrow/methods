# Phase-2 execution notes (from adversarial verification of the fix designs)

Recorded 2026-08-10 after the fix-design verification pass. These bind the
Phase-2 executor; they are constraints the register rows alone don't express.

## Ordering and interdependencies

- **R-010 before R-007.** R-007's Lemma B (renaming recursion) makes a
  non-structural call on `phi[z/x]` and leans on R-010's `lem:substitution-fv`.
- **The G2 repairs (R-002..R-006) apply together.** R-006's Lemma C cites
  R-002's Lemma A; R-002's history coding cites R-003's registered `\le` and
  R-005's designated-slot normalization. Do not land them piecemeal.
- **R-014 has two synchronized restatements** (propositional 2488 and
  first-order 4165); keep the wording aligned with each calculus's soundness
  scope, and do not silently upgrade the FOL half's `proof sketch` status.

## Sweeps the designs require but cannot check themselves

- **R-013 vacuous-discharge sweep:** the repaired discharge convention makes
  vacuous ∨E/→I/¬I/RAA discharges illegal. Every derivation in the manuscript
  (examples, exercises, solutions) must be swept for vacuous discharges and
  repaired. No mechanical check exists yet — consider adding a derivation
  linter to tools/check.py during Phase 2.
- **S-026 (`>`-marked quantifiers):** solutions at 13749–13759 use `\exists
  x>b` / `\forall x>b`, registered nowhere; register `>` or rewrite (same
  family as R-003's `\le`).

## Status-label hygiene flagged by verifiers

- R-004's jump theorem and convention-bridge remark are **proof sketch**, not
  complete proof (they rest on the sketch-status adequacy lemma).
- R-012 deliberately leaves cut elimination a **proof sketch** (mix/multicut
  bookkeeping is designed, the full case table stays cited); its two
  corollaries get rest-on-sketch labels until a full proof exists.
- R-002's design shorthand `2v_j` must be expanded to numeral form in
  execution; its status phrase must be emitted as exactly `proof sketch`
  (one-mechanism rule S-008).

## Verified-clean notes (no action)

- R-003's Q1/Q2 lemmas were checked instance-by-instance against Q's axioms
  (left-witness convention needs only the right-recursion axioms); both Rosser
  branches verified as the standard argument.
- R-011, R-015, R-016 verified sound against the exact string-valued
  definitions and part-IV maps; no edits were needed for R-015/R-016.
- All four fragments compile standalone under amsmath/amssymb.

## Phase-2 completion (recorded 2026-08-10)

All 36 FIX-SOURCE rows landed across eight group commits (G1 29c2d0f +
corrections 4201fbf; G2 b1a77b6 + corrections 563da95; G3a fe1f17d; G3b
58ef447; G5 89cfaa8; G6 b3eb76d; G7 13c1cea; G4 a8e2f5f + corrections
2465859). The defects register now carries `fixed (<hash>)` on each,
attributed to the group's final commit.

### G4 vacuous-discharge sweep results (commits a8e2f5f, 2465859)

The repaired discharge convention (R-013) makes vacuous vE/->I/negI/RAA
discharges illegal; the mandated global sweep covered every derivation in
the manuscript (examples, exercises, solutions, rule sheets).

Repairs made by the sweep (three sites):

- **FOL completeness (`thm:fol-completeness`):** the same non-vacuity case
  split (bottomE/RAA on whether neg-phi occurs open) applied before closing
  by RAA, matching the rewritten propositional completeness proof.
- **Mixed-search example (formal-practice chapter):** vacuous ->I
  discharges replaced by the conjunction detour.
- **Solution `ex:normalization-curry-howard-01`:** vacuous discharge of B
  replaced by the conjunction detour; the weakening relocated to the
  typing-context reading, where it belongs.

Sweep sites checked and found compliant (no repair needed): ND_CPL examples
(commutativity, excluded middle), ND soundness cases, closure clause 4, LK
completeness translation sketch, FOL ND examples and worked example
(exists-E), FOL deductive-closure passage (already non-vacuous),
transfinite Lindenbaum/Henkin proofs, Part VII relativization and CH proofs
(already non-vacuous), normalization detour display, rule sheets
(consequence-form schemas remain admissible), solutions
ex:prop-metatheory-06/-07, ex:fol-deduction-04, and the
intuitionistic/modal/linear chapters (no tree-ND discharges).

G4 verification correction (2465859): the Cut/Mix rule names in the
equipollence lemma statement set upright, removing the small-caps-italic
font substitution introduced with `lem:cut-mix-equipollence`. G4 build
evidence: latexmk exit 0, 251 pp, no undefined refs; tools/check.py hard
checks pass.

### Residual out-of-scope observations from the Phase-2 commit messages

No Phase-2 commit message contains a literal "did NOT fix" marker; the
deliberate non-fixes and residuals the messages do record are collected
here:

- **G1 (29c2d0f):** relative consistency of not-CH remains a *cited
  theorem* (Boolean-valued import, Jech Ch. 14) — not proved in-document;
  the ctm presentation remains a pedagogical device with its omitted
  verifications listed in the new remark.
- **G2 (b1a77b6):** `thm:bounded-verification` stays *proof sketch* (plan
  (h1)-(h4)); `lem:relativized-adequacy`, `thm:jump`, and
  `rem:jump-convention` stay *proof sketch* per the status policy;
  `lem:bounded-collection` makes N-equivalence claims only — no
  formal-theory-provability claim, its caveat deliberately phrased without
  naming Q or PA (both undefined at that point of the book); the
  N-equivalence of registered `\le` with `x<St` is recorded as *not*
  claimed in Q.
- **G3a (fe1f17d):** both LK completeness theorems remain Status *proof
  sketch* (FOL half deliberately not upgraded, per these notes); cut is
  acknowledged as primitive with no cut-free claim.
- **G3b (58ef447), R-024:** the unproved eliminability sentence was
  dropped rather than proved; the citation of `lem:reduct-invariance` is a
  forward reference flagged as independent of the chapter.
- **G4 (a8e2f5f):** cut elimination deliberately remains a *proof sketch*
  (mix/multicut bookkeeping displayed, the full case table stays cited);
  the subformula corollary and the underivability-of-empty-sequent
  corollary carry rest-on-sketch labels until a full proof exists.
- **G6 (b3eb76d):** the principal/cofinite ultrafilter definitions remain
  as prose (not promoted to labeled environments).

Register consequences deferred by disposition (unchanged): all
RESOLVE-BY-MIGRATION, CARRY, and OBSOLETE rows stay open for their phases;
S-026 and the R-013-adjacent derivation-linter suggestion for
tools/check.py remain recorded above and were not executed in Phase 2.
