# w02-p02-004 research note (P2, sections 10.3, 10.4)

## Provenance

- Open component: D-P2-010-GOAL-03 (link complete proofs and the retained
  exercise/feedback surface without counting inactive promoted statements).
- Sources read this session: handbook/parts/p02/propositional-substitution.tex
  (on route via parts/p02.tex), handbook/annex/p02/propositional-substitution.tex
  (on route via annex/p02.tex), handbook/restoration/inherited-02933-03021.tex
  lines 60-65 (ex:prop-metatheory-09, on route via scope-SRC-02933-03021 in
  parts/p02.tex), handbook/restoration/inherited-15638-16742.tex lines 85
  (section "Classical propositional logic") and 161-167 (feedback entry, on
  route via scope-SRC-15638-16742 in parts/p12.tex),
  handbook/restoration/inherited-01661-01816.tex lines 9-11 (bottom is the
  nullary connective), handbook/restoration/inherited-01817-01898.tex lines
  42-60 (definition of logical equivalence).
- Inactive file handbook/parts/p02/propositional-syntax-semantics.tex is not
  input by any driver; its duplicate declarations of
  thm:p02-uniform-substitution / thm:p02-replacement (cited=Kleene1952, lines
  198, 205) are not referenced or credited anywhere in the new text.

## Placement decision

The packet lists the two on-route files as editable hosts, so the linkage was
written directly into them (no driver change needed):
- body: handbook/parts/p02/propositional-substitution.tex lines 183-281
  (def:p02-w02-p02-004-exercise-correspondence, def:p02-w02-p02-004-exercise-worked);
- annex: one backlink sentence inside the proof of annex:p2.prop.replacement
  (after the congruence cases).
The owned new files (parts/annex ...-w02-p02-004.tex, intake bib, symbol
intake) were not created: no new result, citation or symbol was needed, and
an empty file would be a placeholder.

## Mathematical content of the correspondence

- Exercise part (i) = first assertion of thm:p02-replacement = first annex
  paragraph. Part (ii) = congruence assertions = annex cases for bottom, neg,
  and, or, to.
- Feedback sketch omits the nullary bottom case from its case list; the annex
  supplies it. Stated in the convention as a completeness criterion.
- The replacement clause's annex induction uses only reflexivity, the
  congruence clauses, and psi equiv chi (no symmetry or transitivity).
- The substitution theorem's annex proof uses neither exercise part; the
  exercise asks for no part of it.
- Worked example check: (Q -> not Q) and (not Q or not Q) are both false
  exactly when Q is true.

## Overlap to report

Off-route draft handbook/parts/p02/propositional-languages-valuations-and-truth-functions-w02-p02-003.tex
(packet w02-p02-003) contains a longer treatment of the same linkage
(def:p02-w02-p02-003-exercise-link and following). If that draft is later
routed, the two conventions overlap; one should be kept.

## Pass 2 (G10 repair): owned body/annex pair

- The unit build failed because the owned body/annex .tex pair did not exist.
  The pair now exists with new content (not a move and not a stub):
  body handbook/parts/p02/propositional-languages-valuations-and-truth-functions-w02-p02-004.tex
  (sec:p02-w02-p02-004-equivalent-substitutions, lines 1-223),
  annex handbook/annex/p02/propositional-languages-valuations-and-truth-functions-w02-p02-004.tex
  (sec:annex-p02-w02-p02-004-equivalent-substitutions, lines 1-96).
- New results: thm:p02-w02-p02-004-equivalent-substitutions (pointwise
  equivalent substitutions on Var(phi) give equivalent instances; proof by
  structural induction using only reflexivity and the congruence clauses of
  thm:p02-replacement) and corollary thm:p02-w02-p02-004-substitution-invariance
  (phi equiv phi' and pointwise-equivalent substitutions give equivalent
  instances; proof = thm:p02-uniform-substitution + the theorem + transitivity).
  Worked example, failure/limit example, procedure, quotient consequence and
  relationships paragraphs included.
- GOAL-03 linkage text stays in the on-route host (lines 183-281) so that it
  is not taken off the reader route; the new section cross-references it.
- Var notation: reuses the global registry operator \operatorname{Var}
  (symbols.csv row "occurring-variable set"), defined recursively for CPL
  formulas in def:p02-w02-p02-004-occurring-variables.
- Sources opened this session: source/references/acq-r1-ACQ-2026-10-0230/
  kleene-1952-introduction-to-metamathematics-1974-reprint.pdf (held, key
  Kleene1952 already in handbook.bib). PDF page = printed page + 10.
  Locators seen: section 25 Theorem 3 p. 109 (substitution for proposition
  letters, deducibility form, empty-Gamma case); section 26 Theorem 6 p. 116
  (replacement theorem, A ~ B |- C_A ~ C_B, induction on depth; page image
  checked), second version p. 117; section 28 pp. 127-128 (identically
  true/identically equal; adding letters to the list), Lemma 12a p. 128
  (schema check by assigning values to the parts A, B, C; page image checked).
- Symbol intake: [phi] (local class notation) and Kleene's A~B|-C_A~C_B
  notation (source notation, local scope).
- Placement suggestion: the packet proposes after_input
  restoration/scope-SRC-01899-01945 (line 8). The section reads more
  naturally directly after parts/p02/propositional-substitution (line 7),
  before "Translation from controlled prose"; either works textually.

## Continuation

- D-P2-010-GOAL-03: text in the on-route hosts (pass 1).
- G10: owned pair written; unit-compile ok (1 overfull box of 5.8pt in the
  annex item heading); check.py --tree shows no finding on these files.
- No further component work pending in this packet.
