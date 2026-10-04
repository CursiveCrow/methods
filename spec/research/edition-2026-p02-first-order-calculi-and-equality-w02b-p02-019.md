# Edition 2026, P2 17.7: matched LK adequacy and two-way ND/LK maps (w02b-p02-019)

Packet: work/waves/w02b/packets/w02b-p02-019.json.  Label tag
`p02-w02b-p02-019`.  Sections 17.1, 17.2, 17.3, 17.7; this block closes the
17.7 gaps named by the assessment:

- A-037-C02 / ED26-REQ-A-037-01: the LK row of `tab:p02-fol-proof-systems`
  (handbook/parts/p02/first-order-calculi-supplement.tex 219-228, read-only)
  cites only the sketch `thm:fol-lk-completeness`.
- MP-0 (17.7): two-way ND/LK maps at the equality-free and identity
  hypotheses, with the equality-free alpha case written out (the existing
  equality-free proof, annex:p7.calculi.3 lines 173-175, states alpha
  admissibility in one sentence).

## Existing treatments found (A9)

- handbook/parts/p07/calculi-and-derivability-supplement.tex:
  `def:p07-sequent-nd-translation`, `thm:p07-lk-nd-equivalence`
  (annex:p7.calculi.3), `thm:p07-canonical-lk-completeness`
  (annex:p7.calculi.4).  Linked, not restated.
- handbook/parts/p07/equality-lk-metatheory.tex: `def:p07-eqlk-domain`,
  `thm:p07-eqlk-alpha`, `-replacement`, `-congruence`, `-soundness`, `-nd`,
  `-completeness`, `-cut-failure`; annex handbook/annex/p07/equality-lk-metatheory.tex.
  Linked, not restated.  (Not in the packet's existing list.)
- handbook/restoration/inherited-04109-04213.tex `thm:fol-lk-soundness`;
  inherited-04713-04920.tex `thm:fol-lk-completeness` (sketch, assumes AC),
  `thm:fol-completeness`, `cor:fol-completeness-countable`.
- handbook/parts/p02/first-order-syntax-semantics.tex: `def:p02-fol-occurring-variables`,
  `def:p02-fol-term-substitution`, `def:p02-fol-capture-avoiding-substitution`,
  `def:p02-fol-alpha-equivalence`, `thm:p02-fol-free-variables-substitution`.
- handbook/restoration/inherited-03927-04061.tex `lem:reduct-invariance`.

## Defects found in existing proofs (not edited; read-only)

- annex:p7.calculi.3 (equality-free LK to ND) does not treat the Mix rule of
  sheet:lk, although its last paragraph says all rules are exhausted; the
  alpha case of the ND-to-LK direction is one sentence; the forall-R case
  applies forall-I to the eigenvariable without the renaming to the original
  bound variable.  The new annex proof of `thm:p02-w02b-p02-019-maps` derives
  the equality-free maps from annex:p7.eqlk.nd instead (which treats Mix,
  freshening and alpha), plus the new alpha-kernel lemma.

## Sources opened in this session

- Gentzen, Untersuchungen ueber das logische Schliessen II, Math. Z. 39
  (1935) 405-431; held file
  source/references/acq-r1-ACQ-2026-10-0153/gentzen-1935-untersuchungen-II.pdf
  (GDZ scan, image only).  Read printed pp. 417 (Abschnitt V title, par. 1.1),
  418 (par. 1.1 continued, 1.2, plan of par. 2-6), 429 (par. 6, 6.1-6.3).
  Bib key `Gentzen1935b` (already in handbook.bib, pages 405--431).
  Used only for the relationship sentence: Gentzen's equivalence notion
  translates a sequent into a formula and his classical proof routes
  NK -> LK -> LHK -> NK through a Hilbert-type calculus.

## Symbols

D_Delta, supp, =_alpha, Var, FV are existing notation.  Proof-local rows
(S^circ, K, theta, L_0) are in the intake CSV.

## Checks at return

unit-compile ok (overfull 2, both in the handbook.bib Gentzen1935b entry);
check.py --tree shows no finding in this packet's files; fused-space check
clean.

## Continuation

Status: body, annex, patch request and return written in this block; checks
run as recorded in the return file.  Open: the lead applies
work/waves/w02b/patches/w02b-p02-019.json (LK row of
tab:p02-fol-proof-systems) and the driver inputs.
