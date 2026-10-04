# w02b-p02-010 research note (P2, sections 13.1, 13.2, 13.3)

Packet: work/waves/w02b/packets/w02b-p02-010.json. Label tag `p02-w02b-p02-010`.

## Gaps addressed (in the order given)

1. A-006-C02 (named deduction theorem on sheet:hilbert-cpl). The sheet
   (handbook/registry/calculi/hilbert-cpl.tex, editable host) now states the
   deduction theorem as a named paragraph with its exact statement
   (every set Gamma, all phi, psi of the {neg,to}-fragment,
   Gamma u {phi} |-_H psi iff Gamma |-_H phi -> psi), names
   thm:p02-hilbert-deduction and annex:p2.calc.2, and points to the new
   translation results. The identity line's phrase "standard classical
   definitions" was replaced by a pointer to def:p02-hilbert-translation.
2. D-P2-001-GOAL-03 / MP-0 (both-direction Hilbert<->ND/LK derivation maps
   with written proofs). New section sec:p02-w02b-p02-010-translations:
   - thm:p02-w02b-p02-010-hilbert-to-nd: line-by-line Hilbert -> ND_CPL
     map; explicit nonvacuous ND derivations of A1 (two cases), A2, A3.
   - thm:p02-w02b-p02-010-nd-to-hilbert: ND_CPL -> Hilbert map on
     tr_H-images, rule by rule via lemma rule-images and DT.
   - thm:p02-w02b-p02-010-hilbert-to-lk: direct Hilbert -> LK_CPL map,
     cut-free derivations of A1-A3, MP by two cuts.
   - thm:p02-w02b-p02-010-lk-to-hilbert: LK_CPL -> ND (annex:p7.calculi.3,
     restriction to propositional derivations verified case by case) then
     ND -> Hilbert.
   - thm:p02-w02b-p02-010-hilbert-equivalence: the Hilbert legs of
     thm:p02-calculi-derivability-equivalence, proved syntactically.
   - Supporting lemmas: hilbert-structural, hilbert-theorems (8 explicit
     derivations), rule-images (8 items), nd-structural (padding, discharge
     as closure, composition via lem:nd-substitution), nd-translation
     (alpha and tr_H(alpha) ND-interderivable).
   - Method, worked example, two warnings (vacuous discharge failure case
     for A1 with phi = psi; size/shape not preserved), relationships and
     sources.
   - Patch request work/waves/w02b/patches/w02b-p02-010.json: changes
     thm:p02-calculi-derivability-equivalence from cited=Kleene1952 to
     proved=annex:p02-w02b-p02-010-calculi-equivalence, replaces its bare
     Kleene pointer, and inserts the assembling annex item into
     handbook/annex/p02/propositional-hilbert.tex.

## Sources opened in this session (held)

- Kleene1952: source/references/acq-r1-ACQ-2026-10-0230/kleene-1952-introduction-to-metamathematics-1974-reprint.pdf
  (1974 seventh reprint; pagination x+550 matching 1952). Verified via OCR text layer:
  §21 Theorem 1 "The deduction theorem", printed p. 90; example with Axiom Schema 1b
  (A ⊃ B) ⊃ ((A ⊃ (B ⊃ C)) ⊃ (A ⊃ C)) at p. 92; §77 Theorem 46 (H -> G1) p. 445,
  Theorem 47 (G1 -> H, with ¬(F ⊃ F) for an empty succedent) p. 446.
- Gentzen1935b: source/references/acq-r1-ACQ-2026-10-0153/gentzen-1935-untersuchungen-II.pdf
  (image scan, Math. Z. 39 pp. 405-431). Rendered and read: p. 417 Abschnitt V title and
  §1 "Der Begriff der Äquivalenz"; p. 418 §1.1-1.2 (sequent-formula and derivation
  equivalence; plan: §6 equivalence of LHK, NK, LK); p. 429 §6 "Die Äquivalenz der
  Kalküle LHK, NK und LK" with 6.1 LHK->NK, 6.2 NK->LK, 6.3 LK->LHK.
- Mendelson1997 is not in held-sources.json; cited only as the existing attribution of
  the axiom schemas on the sheet, with no locator.

## Proof provenance

All proofs are written directly for sheet:hilbert-cpl, sheet:nd-cpl (nonvacuous
discharge, discharge of all open occurrences), and the inherited LK_CPL. They are not
transcriptions of Kleene or Gentzen. The ND<->LK legs reuse annex:p7.calculi.3, whose
propositional cases were checked to use only sheet:nd-cpl rules / propositional LK rules.

## Notes for integration

- Sheet labels are referenced as \texttt{sheet:\allowbreak ...} in body/annex because
  tools/waves.py unit-compile does not recognise labels defined by \calculussheet.
- hilbert-cpl.tex now \ref's labels in the new body file; they resolve once the body file
  is input by handbook/parts/p02.tex.
- After the patch, annex:p2.hfa.kernels (handbook/annex/p02/hilbert-fol-adequacy.tex) still
  describes its propositional kernel as "cited=Kleene1952"; it could instead cite
  thm:p02-w02b-p02-010-hilbert-equivalence(3) (crosslink request, not patched here).
- handbook/parts/p02/propositional-calculi.tex (not input by the driver) duplicates
  def:p02-hilbert-translation and thm:p02-calculi-derivability-equivalence; not edited.

## Continuation

State at return: all files written; unit-compile ok; check.py shows no finding for these
files; fused-space check clean. Remaining: lead must input body/annex files, apply the
patch file, and decide on placement (return JSON). Units ED26-SRC-008-001-* belong to
packet w02b-p02-008 and were not written here.
