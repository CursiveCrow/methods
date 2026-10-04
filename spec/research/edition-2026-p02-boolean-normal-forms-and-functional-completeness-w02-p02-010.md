# w02-p02-010 research note (P2 sections 11.4, 11.5, 11.6)

Provenance and decisions for packet w02-p02-010. Reader text carries none of this.

## Sources opened in this session

- Kleene, Introduction to Metamathematics, held file
  `source/references/acq-r1-ACQ-2026-10-0230/kleene-1952-introduction-to-metamathematics-1974-reprint.pdf`
  (seventh reprint 1974; bib key Kleene1952 already in handbook.bib). Text extracted with
  pdftotext; running heads read in this session: section 27 "Equivalences, duality",
  Theorem 8 (statement p. 121, proof continues p. 122), Corollary "Principle of duality"
  (p. 122), Example 5 and the remark that duality holds only as a subsidiary deduction rule,
  with the attribution to Schroeder 1877 (p. 123), Corollary second part "dual converse"
  (p. 124). Kleene's results concern provable equivalence in his formal system; the
  handbook text cites them only as the syntactic origin of the semantic statements proved here.
- Inherited chapter captures: `handbook/restoration/inherited-01661-01816.tex` (alphabet,
  grammar, top as abbreviation), `inherited-01817-01898.tex` (valuations, coincidence,
  semantic notions), `inherited-01946-02186.tex` (literals, clauses, form_CPL, NNF/CNF/DNF
  definitions, clause-satisfaction lemma, unlabeled NNF theorem at 97-100, normal-form
  theorem thm:prop-normal-forms, forward reference at 210-212).
- Existing treatments: `handbook/parts/p02/propositional-metatheory-supplement.tex` 74-128
  (def:p02-nnf-dual, thm:p02-propositional-duality, tab:p02-duality; read-only host),
  `handbook/annex/p02/propositional-metatheory-supplement.tex` 7-37 (annex:p2.1.8; editable),
  `handbook/parts/p02/tseitin-transformation.tex` and its annex (editable; already cover
  D-P2-007 GOAL-01/02), `handbook/parts/p02/propositional-substitution.tex`
  (thm:p02-uniform-substitution, reused for the complementing substitution).
  `handbook/parts/p02/propositional-syntax-semantics.tex` and its annex carry a second,
  off-route copy of the duality definition/theorem/annex item with the same labels; it is not
  input by handbook/parts/p02.tex. Not listed as a problem by the packet; recorded here.

## Mathematical correction found

The body statement of thm:p02-propositional-duality says dualization "exchanges CNF with DNF".
Under the inherited definitions (clauses are sets; form_CPL lists distinct literals in strictly
increasing code order) the CNF-to-DNF direction holds exactly, but the DNF-to-CNF direction
holds only up to logical equivalence: (P and P) is DNF, its dual (P or P) is not CNF. The
annex item now proves the exact statement and gives the counterexample; a patch request asks
for the body wording to be corrected and for "1 - v(p)" to be replaced by the F/T definition
of the complemented valuation (the truth values of the inherited chapter are F, T).

## Continuation

- DONE (written, not assessed): annex:p2.1.8 rewritten with every case (literals, units,
  conjunction, disjunction), involution induction, equivalence both ways, valid<->unsatisfiable
  both ways, exact CNF/DNF clause with counterexample.
- DONE (written): owned body section sec:p02-w02-p02-010-duality-arbitrary and owned annex.
- Patch requests: work/waves/w02/patches/w02-p02-010.json (CNF forward reference to the
  Tseitin proofs in inherited-01946-02186.tex; body wording of thm:p02-propositional-duality;
  pointer from the duality section to the new section).
- Remaining: D-P2-007-GOAL-03 needs the restoration patch applied by the lead (blocked_policy).
</content>
</invoke>
