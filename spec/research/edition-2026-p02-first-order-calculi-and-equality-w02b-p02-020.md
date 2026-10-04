# Edition 2026, P2 17.8: proof of the quantified subformula property (w02b-p02-020)

Packet: work/waves/w02b/packets/w02b-p02-020.json.  Label tag
`p02-w02b-p02-020`.  Section 17.8, duty MP-0: the first-order
subformula-instance theorem `thm:p02-fol-subformula-property`
(handbook/parts/p02/first-order-depth.tex) was citation-only
(`cited=RathjenSieg2024`) with no written proof on the handbook route.

## Existing treatments found (A9)

- handbook/parts/p02/first-order-depth.tex: `sec:p02-fol-subformula-property`,
  `def:p02-fol-subformula-instance` (the relation; reused, not redefined),
  `thm:p02-fol-subformula-property` (statement; read-only host).
- handbook/parts/p02/first-order-syntax-semantics.tex 251-255: pointer to the
  host section (listed in the packet).
- Not listed in the packet but relevant: handbook/parts/p07/cut-elimination-and-interpolation.tex
  `thm:p07-cut-free-subformula` (annex:p7.cut.3; propositional
  LK_d/LJ only); handbook/parts/p07/intuitionistic-cut-elimination.tex
  `def:p07-lj-instance-subformula`, `thm:p07-lj-analyticity`
  (annex:p7.lj.analyticity; sheet:lj, modulo alpha-equivalence).  Neither is a
  theorem about sheet:lk (registry note handbook/registry/calculi/lk.tex 7-9).
  The new section links them and does not restate them.
- Substitution: `def:p02-fol-capture-avoiding-substitution`,
  `def:p02-fol-formula`, `def:p02-fol-term`,
  `thm:p02-fol-unique-readability` (first-order-syntax-semantics.tex).

## Sources opened in this session

- Buss, "An Introduction to Proof Theory", Chapter I of Buss (ed.),
  Handbook of Proof Theory (Elsevier 1998), printed pp. 1-78.  Held file
  source/references/acq-r1-ACQ-2026-10-0067/buss-1998-handbook-proof-theory-ch1.pdf
  (author-hosted; manifest identifies printed pp. 1-78).  Locators read:
  sec. 1.2.3 (p. 12) principal/auxiliary/side formulas and immediate
  descendants; Prop. 1.2.4 (p. 13) subformula property for cut-free PK;
  sec. 2.3.1 (pp. 31-32) free/bound variable classes, the note that a
  subformula of a formula is in general a semiformula, and the remark that
  without these conventions cut elimination would need reformulation
  (Feferman example, p. 32); Def. 2.3.2 (p. 32) quantifier rules with
  arbitrary term t and eigenvariable b.  New intake key `Buss1998Intro`
  because handbook.bib's `Buss1998` is the edited collection, not the
  authored chapter.
- Gentzen 1934/35 (held scans) has no text layer; not used, no locator.
- RathjenSieg2024 is not in held-sources.json; not cited by the new files.

## Design

The handbook's own proof (the D-P3-014 presentation is the handbook's).
Body: conventions for instance sets SI(chi), literal subformulas and the
successor map on occurrences; Lemma (closure/chains/transitivity); Lemma
(literal subformulas are instances; equality for quantifier-free formulas);
Theorem (traced form; its "in particular" clause is the host statement);
Corollary (quantifier-free endsequent gives literal subformulas); worked
example with renaming of a bound variable; failure with Cut; failure on
sheet:lk-eq (=L); limitations; relationships; sources.  Annex: full proofs,
including every rule case of the inductive step.

The host theorem keeps `cited=RathjenSieg2024` until the lead applies the
patch request in work/waves/w02b/patches/w02b-p02-020.json (status change to
a proof item plus a one-paragraph annex item deriving it from the traced
theorem).  The annex check forbids writing that annex item before the host
status points at it.

## Continuation

- Done: research, design, all files written (see return JSON).
- Open: lead to apply patch request (host status + annex item); driver
  inputs per insertion proposal.
