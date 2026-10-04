# edition-2026 P2 ch. 12 (12.1-12.4): natural deduction trees and the intuitionistic boundary — packet w02b-p02-008

Label tag: `p02-w02b-p02-008`. Heading level `\section`. toc tag `%% toc: P2 12 12.1,12.2,12.3,12.4`.

## Files

- Body: `handbook/parts/p02/natural-deduction-and-classical-sequent-calculi-w02b-p02-008.tex`
- Annex: `handbook/annex/p02/natural-deduction-and-classical-sequent-calculi-w02b-p02-008.tex`
- Symbol intake: `handbook/registry/symbols-intake-p02-natural-deduction-and-classical-sequent-calculi-w02b-p02-008.csv`
- No bib intake: the only citation key used (`Gentzen1934a`) is already in `handbook/bib/handbook.bib`.

## Gaps addressed in this block

1. A-115-C01/C02/C03 (all four sections): the inactive figure `fig:p02-nd-tree`
   (`handbook/parts/p02/propositional-calculi.tex:71-91`, ND_CPL conjunction
   commutativity with two `[P∧Q]^1` leaves discharged by `→I,1`) had no tree
   counterpart on the active route. The new body file displays the same
   derivation as a Prawitz-style TikZ tree (`fig:p02-w02b-p02-008-commutativity-tree`)
   with discharge labels, and an explicit line-to-node map
   (`def:p02-w02b-p02-008-commutativity-map`) onto the linear example at
   `handbook/restoration/inherited-02193-02340.tex:88-101`. A second tree,
   the classical excluded-middle derivation (`fig:p02-w02b-p02-008-excluded-middle-tree`),
   is mapped onto `inherited-02193-02340.tex:103-121` (`def:p02-w02b-p02-008-excluded-middle-map`).
   Rule names in the trees are plain text (hyperref to `rule:nd-cpl-*`
   rows produced unknown-ref failures in the unit compile, since the
   registry sheet is not in the unit closure).
2. 12.3 MP-0: complete Kripke argument for the calculus the Excluded-middle
   example names (ND_CPL without RAA, primitive ¬, ¬I, ¬E, ⊥E kept). Chosen
   route: direct Kripke soundness, not a translation into LJ.
   - `def:p02-w02b-p02-008-nd-minus-raa` (the calculus; descriptive subscript notation).
   - `def:p02-w02b-p02-008-forcing` (P8 Kripke structures of
     `sec:intuitionistic-logic-01` plus a primitive-negation clause).
   - `thm:p02-w02b-p02-008-persistence` (annex `annex:p02-w02b-p02-008-pers`; includes ¬ case).
   - `thm:p02-w02b-p02-008-defined-negation` (annex `annex:p02-w02b-p02-008-dneg`;
     the ¬ clause agrees with ¬φ := φ→⊥ under the translation φ*).
   - `thm:p02-w02b-p02-008-open-accounting` (annex `annex:p02-w02b-p02-008-oa`;
     discharge bookkeeping for every rule, including ∨E with labels i,j).
   - `thm:p02-w02b-p02-008-kripke-soundness` (annex `annex:p02-w02b-p02-008-ks`;
     every rule: ∧I, ∧E1/2, ∨I1/2, ∨E, →I, →E, ¬I, ¬E, ⊥E, with discharge and persistence).
   - `thm:p02-w02b-p02-008-nonderivability` (annex `annex:p02-w02b-p02-008-lem`;
     countermodel, P∨¬P and ¬¬P→P not derivable, strictness of inclusion with
     a full check that the excluded-middle tree is an ND_CPL derivation).
   - Example `def:p02-w02b-p02-008-countermodel`, warnings
     `def:p02-w02b-p02-008-raa-step` (failure case: the RAA step has no
     forcing analogue; one-world structures cannot refute) and
     `def:p02-w02b-p02-008-scope-of-result` (soundness only; vacuous-discharge independence).

## Existing treatments checked (A9)

- `handbook/restoration/inherited-02193-02340.tex` (ND_CPL rules, examples, substitution lemma): extended by tree displays and the boundary proof; not duplicated.
- `handbook/restoration/inherited-02451-02544.tex:7-46` (`thm:prop-nd-soundness`, classical): used as the comparison for the RAA failure case.
- `handbook/restoration/inherited-12989-13045.tex` (P8 Kripke structures, persistence for defined-negation language) and `inherited-13100-13127.tex:1-12` (two-world counterexample): reused by reference; the new persistence lemma adds the primitive ¬ case.
- `handbook/parts/p14/classical-and-constructive-calculi.tex:416-425, 583-585`: already warns that ND without RAA is not literally defined-negation NJ and not minimal; consistent with the new text.
- `handbook/parts/p07/normalization-and-curry-howard-supplement.tex` (`fig:p07-stlc-nd-derivation`, NJ, defined negation): a different calculus; not used as the ND_CPL tree.
- `handbook/registry/calculi/nd-cpl.tex`: rule names follow its rows.
- Found, not listed in packet `existing`: `handbook/registry/calculi/p07-nj-vacuous.tex` (NJ with vacuous discharge) and the `\operatorname{oa}(D)` notation of `def:p02-fbc-language` (`handbook/parts/p02/free-boolean-algebra-and-completeness.tex:28`), reused here.

## Sources read in this session

- `source/references/acq-r1-ACQ-2026-10-0153/gentzen-1934-untersuchungen-I.pdf` (Gentzen1934a, Math. Z. 39, pp. 176-210; image scan). Read printed pp. 185-186 (item 2.21: NJ schemata UE..NB and the falsum schema; bracketed assumptions "in beliebiger Anzahl (evtl. keine)") and p. 190 (item 5.3: NK = NJ plus basic formulas A∨¬A; alternative schema ¬¬A/A). Locators used: `[2.21, pp.~185--186]`, `[2.21, p.~185]`, `[5.3, p.~190]`.
- Frozen reference source lines are represented on the route by the hash-checked restoration captures listed above; not modified.

## Blocked

- ED26-SRC-008-001-{SETUP,DEVELOPMENT,CASES,APPARATUS}: "Systems of Deduction", Handbook of Philosophical Logic, second edition, Volume 2, Kluwer 2001, printed pp. 1-52. Not in `spec/coverage/edition-2026/held-sources.json` (packet `held_paths` empty; no file under `source/references`). No presentation written (A3/A13).

## Placement

- Body: `\input{parts/p02/natural-deduction-and-classical-sequent-calculi-w02b-p02-008}` into `handbook/parts/p02.tex` after line 21 (`\input{restoration/scope-SRC-02665-02809}`).
- Annex: `\input{annex/p02/natural-deduction-and-classical-sequent-calculi-w02b-p02-008}` into `handbook/annex/p02.tex` after line 18 (`\input{annex/p02/propositional-rejection-and-refutation}`).

## Continuation

Status at end of block 1 (2026-10-04):
- A-115-C01/C02/C03 and 12.3 MP-0: text and annex proofs written in the owned files; unit compile ok, 0 overfull; no check.py findings on these files; fused-space check clean.
- FLRV1-U00169..U00177 and A-116-C01..C03: existing route text, not modified in this block.
- Open: SRC-008-001 (blocked_source, acquisition needed). Driver insertion is the lead's action.
- Possible follow-up: if the registry sheet becomes part of unit closures, the tree rule names could hyperlink to `rule:nd-cpl-*` rows as the P7 figure does.
