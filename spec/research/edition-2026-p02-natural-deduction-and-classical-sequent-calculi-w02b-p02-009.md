# Research note: P2 sections 12.5 and 12.6 (packet w02b-p02-009)

## Scope of this packet

Section-level duties (12.5 MP-0; 12.6 MP-0, X-0, X-1) from the current-text
assessment.  Every unit component listed in the packet (FLRV1-U00175..177,
A-115-C01..C03, A-116-C01..C03, ED26-SRC-008-001-*) belongs to a unit that the
packet's `readonly_units` assigns to w02b-p02-008; those components are not
written here.

## Sources opened in this session

- `source/references/acq-r1-ACQ-2026-10-0429/buss-1998-introduction-proof-theory.pdf`
  (Buss, "An Introduction to Proof Theory", ch. I of Handbook of Proof Theory,
  Elsevier 1998; printed pp. 1--78).  Locators verified: PK definition
  Sec. 1.2.2 pp. 11--12 (page 11 viewed as image: Cut with shared contexts,
  identity A=>A with A atomic, exchange explicit, implication written as a
  horseshoe, rules for negation, conjunction, disjunction, implication);
  Prop. 1.2.4 (subformula property) p. 13; 1.2.6 soundness p. 13; 1.2.7
  inversion theorem pp. 13--14; Thm 1.2.8 and Lemma 1.2.9 pp. 14--15;
  1.2.11 semantic cut elimination pp. 15--16.  New intake key `Buss1998Intro`.
- Gentzen 1934/35 scans are held but text extraction gives no text; no
  locator was verified, so Gentzen is not cited with a locator.

## Handbook material read

- restoration/inherited-02193-02340.tex (ND_CPL rules, discharge, lem:nd-substitution)
- restoration/inherited-02341-02450.tex (LK_CPL, Sequent definition, ND soundness, LK soundness)
- restoration/inherited-02451-02544.tex? (the soundness proofs are in 02341-02450 lines 117-203 of the
  concatenated read; the packet names inherited-02451-02544.tex lines 7-93)
- restoration/inherited-02665-02809.tex (completeness, LK completeness sketch)
- parts/p07/classical-cut-elimination.tex (scope of thm:p07-classical-cut-elimination)
- annex/p07/calculi-and-cut-elimination.tex and -supplement.tex (annex:p7.calculi.2, .3)
- registry/calculi/lk-defneg.tex (sheet:lk-defneg)
- parts/p02/propositional-syntax-semantics.tex (Fm_CPL, c, Sub, valuations)

Existing treatment not listed in the packet: parts/p02/axiomatic-calculi-analytic-tableaux-and-refutation-w02b-p02-010.tex
uses annex:p7.calculi.3 for ND<->LK; parts/p07/calculi-and-derivability.tex
thm:p07-lk-nd-equivalence (cited=Gentzen1934a); annex:p7.cut.3 (thm:p07-cut-free-subformula).

## Design decisions

- Cut: semantic admissibility (rule-wise soundness + inversion + cut-free
  completeness by induction on weight), proved directly for LK_CPL; this is
  the route of Buss 1.2.8--1.2.11 adapted to multisets, contexted identity,
  the bottom-sequent and primitive negation.  The cut-free derivations use no
  weakening or contraction.
- Subformula property: defined via Sub of def:p02-complexity-subformula,
  proved for every Cut-free derivation (W and C allowed).
- ND->LK: exact multiset of open occurrences om(D); per-rule trees with
  explicit counts of C_L and W_L steps.
- LK->ND: representation by ND derivations of falsum whose open occurrences
  carry labels from three jointly injective label maps (left, right,
  auxiliary); helper operations ext, neg, pin; no grafting, so no capture.

## Patch requests

work/waves/w02b/patches/w02b-p02-009-*.json (pointers from the inherited
soundness proofs and the completeness sketch to the new rule-case lemmas and
translations).

## Continuation

- Done in files: body and annex written (see return JSON for line ranges).
- Open: none of the unit components (readonly, owned by w02b-p02-008).
