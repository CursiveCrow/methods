# w02-p02-003 research note (P2, sections 10.1, 10.2)

Label tag: `p02-w02-p02-003`.

## Files

- Body: `handbook/parts/p02/propositional-languages-valuations-and-truth-functions-w02-p02-003.tex`
  (`\section`, label `sec:p02-w02-p02-003-exercise-link`).
- Annex: `handbook/annex/p02/propositional-languages-valuations-and-truth-functions-w02-p02-003.tex`
  (label `sec:annex-p02-w02-p02-003-exercise-link`, annex item `annex:p02-w02-p02-003-replace`).
- Symbol intake: `handbook/registry/symbols-intake-p02-propositional-languages-valuations-and-truth-functions-w02-p02-003.csv`
  (one row: the relation metavariable `E`).
- No bibliography intake: the only key cited, `Kleene1952`, is already in `handbook/bib/handbook.bib`.

## Duty closed in this session: D-P2-010-GOAL-03

Gap as assessed: nothing on the active route connected `thm:p02-replacement` /
`thm:p02-uniform-substitution` (active host `handbook/parts/p02/propositional-substitution.tex`,
annex `handbook/annex/p02/propositional-substitution.tex`, items `annex:p2.prop.replacement`,
`annex:p2.prop.substitution`) to the retained exercise `ex:prop-metatheory-09`
(`handbook/restoration/inherited-02933-03021.tex:60-64`; frozen source
`source/formal-logic-reference.tex:2992-2996`) or to its feedback entry
(`handbook/restoration/inherited-15638-16742.tex:161-167`; frozen source lines 15798-15804).

What the body supplies:

- `def:p02-w02-p02-003-exercise-link` (hbconvention): states that the two parts of the
  exercise are the first two assertions of `thm:p02-replacement`, proved in
  `annex:p2.prop.replacement`; maps each step of the feedback solution sketch onto the
  annex proof; records that the sketch lists negation and the binary connectives but
  not the nullary connective `\bottom` (the alphabet calls it the nullary connective,
  `inherited-01661-01816.tex:4-19`), which the annex proof covers; links the
  uniform-substitution theorem and its annex as the companion result and says the
  exercise does not ask for its equivalence clause.
- `thm:p02-w02-p02-003-congruence-replacement` (proved=`annex:p02-w02-p02-003-replace`):
  for any equivalence relation E on Fm_CPL, constructor congruence iff selected-occurrence
  replacement in the sense of `def:p02-selected-replacement`. Shows that a complete
  solution of the exercise yields the replacement clause, and conversely.
- `def:p02-w02-p02-003-worked-replacement`: worked replacement at position 11 of
  `(\neg(P\to Q)\lor R)`, with each exercise clause used; one uniform-substitution instance.
- `def:p02-w02-p02-003-congruence-limits`: agreement at one valuation is not equivalence
  (quantifier order in the feedback sketch); equisatisfiability is an equivalence relation
  but not a congruence, so by (b)=>(a) replacement fails, instance at
  `def:p02-substitution-replacement-limits`.
- Relationships paragraph with the Kleene comparison.

Inactive promoted statements: `handbook/parts/p02/propositional-syntax-semantics.tex:198-212`
declares the same labels `thm:p02-uniform-substitution` and `thm:p02-replacement` with
`cited=Kleene1952`. That file is input by no driver. The new text refers only to the labels;
in the active build they resolve to the proved statements in `propositional-substitution.tex`.
Nothing in the new text counts the inactive declarations.

## Provenance

- Kleene1952 held file: `source/references/acq-r1-ACQ-2026-10-0230/kleene-1952-introduction-to-metamathematics-1974-reprint.pdf`
  (1974 reprint, opened this session through pdftotext). Verified locators: Section 26
  "Equivalence, replacement"; Theorem 6 (Replacement theorem), its depth induction and
  "Lemmas for replacement" *26--*30 on printed p. 116; remarks that the theorem includes
  the lemmas as the depth-1 cases and that sets of occurrences are replaced by iterated
  single replacements on printed p. 117. Kleene's theorem is deductive (hypothesis A ~ B,
  conclusion C_A ~ C_B deducible), for one specified occurrence; the body says so.
- The proposition and its proof are written here; no source claims the general
  equivalence-relation form in these words.

## Existing treatments found that the packet did not list

- `handbook/parts/p02/propositional-substitution.tex` as host of `def:p02-uniform-substitution`,
  `thm:p02-uniform-substitution`, `def:p02-selected-replacement`, `thm:p02-replacement`,
  `def:p02-substitution-replacement-example`, `def:p02-substitution-replacement-limits`
  (the packet lists the file only under `thm:prop-unique-readability`).
- `handbook/annex/p02/propositional-substitution.tex` (`annex:p2.prop.substitution`,
  `annex:p2.prop.replacement`).
- `handbook/parts/p01/notation-binding-and-comparison-of-formal-w02-p01-025.tex:71-90`,
  `def:p01-w02-p01-025-exercise-link`: an off-route convention with the same purpose. If
  that file is ever input, the lead should keep only one of the two conventions; the
  present one is more specific (nullary case, quantifier order, the congruence/replacement
  equivalence).

## Blocked components

- ED26-SRC-001-001-* (Barwise, "An introduction to first-order logic", Handbook of
  Mathematical Logic, first edition 1977, printed pp. 5-46): no held file
  (`held_paths` empty; no Barwise key in `spec/coverage/edition-2026/held-sources.json`).
- ED26-SRC-007-001-* (Hodges, "Elementary Predicate Logic", Handbook of Philosophical Logic,
  second edition, Vol. 1, Kluwer 2001, printed pp. 1-129): no held file (same checks).

## Continuation

- 2026-10-04: GOAL-03 text, proposition, annex proof, example, warning and Kleene
  comparison written. `tools/waves.py unit-compile` ok (0 overfull);
  `find_fused_spaces.py` clean; `tools/check.py --tree handbook` shows no finding in
  these files.
- Remaining for the lead: insert the two `\input` lines (body after
  `restoration/scope-SRC-01899-01945` per the packet proposal, or directly after
  `parts/p02/propositional-substitution`, which the section continues; annex after
  `annex/p02/propositional-substitution`). Merge the symbol intake row.
- Optional, outside owned files (restoration capture): a back-link from the feedback
  paragraph for `ex:prop-metatheory-09` to `def:p02-w02-p02-003-exercise-link`. Not needed
  for the link to exist in the forward direction.
- Next session, if assigned: SRC-001-001 and SRC-007-001 stay blocked until the sources
  are acquired.
