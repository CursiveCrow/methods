# Packet w02-p02-016 (P2, chapter 14, sections 14.1-14.4): research note

Label tag: `p02-w02-p02-016`.  Heading level `\section`.  Toc tag
`%% toc: P2 14 14.1,14.2,14.3,14.4`.

## Gap addressed in this pass

Assessment gap for 14.4: D-P2-011-GOAL-03 (and therefore D-P2-011-C01).
Required: at the arbitrary-language treatment, distinguish the effective
finite-input decision procedures from the larger language scope; state that
`thm:p02-decidability` and SAT/TAUT (`def:p02-sat-taut`) act on finite encoded
inputs over the countable p_n coding, that a finite input involves only finitely
many atoms, and that the BPI-relative completeness/compactness theorem for an
arbitrary (possibly uncountable) P supplies no decision procedure, enumeration or
encoding of Form(P).

## What was written

New body file `handbook/parts/p02/propositional-soundness-completeness-and-compactness-w02-p02-016.tex`
(section `sec:p02-w02-p02-016-finite-input-scope`), to be input directly after
`parts/p02/free-boolean-algebra-and-completeness` (the arbitrary-language
treatment), and its annex
`handbook/annex/p02/propositional-soundness-completeness-and-compactness-w02-p02-016.tex`.

- `def:p02-w02-p02-016-semantics` (convention): valuations P -> {0,1},
  `\entails_P`, satisfiable/valid over P, `\equiv_P`, `\operatorname{Var}` on
  Form(P).  Reduces to the source notions for P = Prop.
- `def:p02-w02-p02-016-inputs` (convention): the inputs of
  `thm:p02-decidability` are finite bit strings; under `def:p02-sat-taut` they
  encode exactly the formulas over Prop = {p_n}; infinite premise sets are never
  inputs.
- `thm:p02-w02-p02-016-finite-atoms` (lemma, proved=annex:p02-w02-p02-016-atoms):
  Var of a formula and of a finite set is finite (ZF, no choice); Var(P) = P.
- `def:p02-w02-p02-016-renaming`: injection r : A -> Prop of a finite atom set,
  translation r-star : Form(P) -> Fm_CPL (atoms outside A to bottom); "initial"
  when a bijection onto p_0..p_{k-1}.
- `thm:p02-w02-p02-016-transfer` (proved=annex:p02-w02-p02-016-transfer):
  finite consequence, satisfiability, validity, equivalence over P are
  preserved and reflected by r-star for every injection; answers independent of
  r; no choice, BPI, completeness or compactness used.
- `thm:p02-w02-p02-016-decision` (corollary, proved=annex:p02-w02-p02-016-decision):
  reduction to membership of one encoded string in TAUT or SAT, settled by the
  2^k assignments on p_0..p_{k-1} (via `lem:prop-coincidence`).  Prose links the
  procedure itself to `thm:p02-decidability` (cited EFT) and to the written
  proof `thm:p02-w02-p02-018-decision`.
- `thm:p02-w02-p02-016-no-coding` (proved=annex:p02-w02-p02-016-no-coding):
  for uncountable P (no injection into N, the frozen source's definition of
  countable at source/formal-logic-reference.tex line 541-542), no injection
  Form(P) -> {0,1}^* and no surjection N -> Form(P).  Proof self-contained
  (explicit length-lex injection of {0,1}^* into N; least preimage).
- `def:p02-w02-p02-016-bpi-boundary` (proofboundary): what
  `thm:p02-fbc-completeness`, `thm:p02-arbitrary-prop-completeness`,
  `thm:p02-arbitrary-prop-compactness-bpi` do not supply, in three exact
  places (uncountable P: no coding; P = Prop with infinite Gamma: undecidable
  in general by `thm:p02-w02-p02-018-limits`(1); countable P: an injection
  exists by definition, not by the theorem, and no computable presentation is
  given).  Plus: the finite-input decision does not use BPI or completeness.
- `tab:p02-w02-p02-016-regimes`: three regimes (finite input / countable
  infinite / arbitrary infinite) with set-theoretic standing and effective
  content.
- `def:p02-w02-p02-016-example`: finite input over P = {a_r : r real}, renamed
  to p_0, p_1, encoded string shown, four rows checked; non-initial injection
  gives the same answer.
- `def:p02-w02-p02-016-failure` (warning): uncountable premise set Delta with a
  consequence a_1 and a non-consequence a_{-1} (countervaluation given); not an
  input.

## Existing treatments found

Listed in the packet and linked: `propositional-metatheory-supplement.tex`
(def:p02-arbitrary-prop-language, thm:p02-arbitrary-prop-compactness-bpi,
thm:p02-arbitrary-prop-completeness, thm:p02-decidability, def:p02-sat-taut);
`free-boolean-algebra-and-completeness.tex` (def:p02-fbc-language,
thm:p02-fbc-completeness and annex sentence on no general algorithm);
p01 `thm:p01-bpi-propositional-compactness` and remark.

Not listed in the packet's `existing` list, found by search:
- `handbook/parts/p02/propositional-resolution-and-satisfiability-procedures-w02-p02-018.tex`
  lines 216-246: `def:p02-w02-p02-018-scope` (warning: limits of the
  decidability theorem, including Form(P)) and `thm:p02-w02-p02-018-limits`
  ((1) infinite Gamma_A undecidable for all but countably many A; (2) no
  injection of uncountable P into {0,1}^*), with annex proof; and
  `thm:p02-w02-p02-018-decision` (written proof of the content of
  thm:p02-decidability for its own token encoding).  This file is a sibling
  wave file not yet on the static input route.  The new section links to it
  rather than reproving (1); for the Form(P) non-encodability it gives its own
  three-line proof so that its own results do not depend on 018 being routed.
  If 018 is not integrated, the five references to 018 labels in the body
  (decision prose: 018-decision, 018-input; proofboundary item 2 and regimes table: 018-limits; relationships: 018-scope) must be redirected.
- `handbook/parts/p02/propositional-metatheory.tex` line 283-290 holds an
  older copy of thm:p02-decidability (inactive historical file).

## Symbol intake

`\equiv_P`, `\mathsf r`, `\mathsf r^{\star}`, `w^{\mathsf r}`, `v_{\mathsf r}`,
scoped to the new section.  Reused registered `\operatorname{Var}` (global
occurring-variable set) and `\models_P` (row 5426).  Deliberately avoided
`\iota` (registered in P2 as a base type, description binder and at-least-n
sentence) and a sharp superscript (registered P2 incidence translation).

## Sources

No new bibliography keys.  Citations: EbbinghausFlumThomas1994 (via
thm:p02-decidability, no locator added) and HowardRubin1998 (via the
arbitrary-language statements, no locator added).  All results in the new
section are editorial with complete annex proofs.  Open item: no page locator
was verified this session for either citation; none is written.

## Continuation

- GOAL-03 distinction written (body 1-355, annex 1-226).  unit-compile ok,
  overfull 0; find_fused_spaces clean; check.py --tree shows no finding for
  the new files.
- Remaining for the lead: insert `\input{parts/p02/propositional-soundness-completeness-and-compactness-w02-p02-016}`
  after `parts/p02/free-boolean-algebra-and-completeness` in
  handbook/parts/p02.tex, and the annex input after
  `annex/p02/free-boolean-algebra-and-completeness` in handbook/annex/p02.tex;
  merge the symbol intake.  Route w02-p02-018 so that its labels resolve.
- The FLRV1 units of 14.1-14.4 are the exact restoration captures; not edited.
