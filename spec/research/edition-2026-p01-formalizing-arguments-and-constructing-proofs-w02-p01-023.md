# w02-p01-023: sections 7.4-7.7 (invariants; changes of governing logic)

Provenance note for packet `work/waves/w02/packets/w02-p01-023.json`, label tag
`p01-w02-p01-023`. Session date 2026-10-04.

## Gaps addressed

1. 7.5 (title scope): invariants as a proof method. Before this note the only
   occurrence on the reader route was the proof-plan item at
   `handbook/restoration/inherited-01411-01504.tex:90`.
2. 7.7 (title scope): a diagnostic and repair for a change of governing logic
   inside an argument. The Error taxonomy longtable
   (`handbook/restoration/inherited-01592-01631.tex:4-39`) has no
   governing-logic row; its Rule error row (lines 25-27) asks only whether a
   rule belongs to the active calculus.

Both restoration hosts are read-only and were not edited. The new section is
one body file placed after `restoration/scope-SRC-01592-01631` (packet
insertion proposal) and links back to `sec:writing-foundations-04`,
`sec:writing-foundations-07` and `ch:writing-foundations`.

## Inputs opened this session

- `source/formal-logic-reference.tex` (FLRV1, Version 1.0): lines 1480-1553
  (proof plan method, section "Proof methods" and its six subsections),
  1592-1631 (Error taxonomy longtable), 12973 (chapter "Intuitionistic
  Logic"), 12989-13127 (language, LJ finite-support derivability, Kripke
  structure, forcing, persistence, semantic consequence, soundness and
  completeness statement, the two-world counterexample at 13100).
- Handbook route files read: `restoration/inherited-01411-01504.tex`,
  `inherited-01505-01553.tex`, `inherited-01592-01631.tex`,
  `inherited-01817-01898.tex` (classical valuations,
  `sec:prop-syntax-semantics-02`), `inherited-02545-02664.tex`
  (`lem:prop-lindenbaum`), `inherited-12989-13045.tex` through
  `inherited-13180-13200.tex` (IPL chapter, `thm:glivenko`,
  `thm:disjunction-property`), `parts/p08/intuitionistic-kripke-completeness.tex`
  lines 1-100 and 220-245 (`thm:p08-ipl-completeness-persistence`,
  `thm:p08-ipl-completeness-soundness`, `thm:p08-ipl-strong-completeness-full`;
  all on the p08 driver route, line 16 of `parts/p08.tex`),
  `parts/p02/propositional-metatheory-supplement.tex` lines 264-330
  (`def:p02-tractable-classes`, `thm:p02-horn-sat`, cited to
  DowlingGallier1984, which is not held), `registry/calculi/hoare-while.tex`
  (`rule:p09-hoare-while-partial`, `rule:p09-hoare-while-total`),
  `parts/p09/logic-in-computer-science.tex` labels near line 1674
  (`sec:p09-program-logics`, `def:p09-hoare-triple`).
- Held external sources (listed in `spec/coverage/edition-2026/held-sources.json`):
  - `source/references/acq-r1-ACQ-2026-10-0197/hoare-1969-axiomatic-basis-for-computer-programming.pdf`
    (bib key Hoare1969). PDF page 3 is printed p. 578: section 3.4 "Rule of
    iteration" and rule D3. PDF page 4 is printed p. 579: section 4 opens with
    the remark that the rules give no basis for proving termination.
  - `source/references/acq-r1-ACQ-2026-10-0136/floyd-1967-assigning-meanings.pdf`
    (bib key Floyd1967). Printed p. 19, Introduction: propositions attached to
    connections in the flow of control, a condition imposed on each command,
    induction on the number of commands executed, and termination by a
    decreasing entity.

## Existing treatment search (A9)

- Listed: the two restoration files and labels `sec:writing-foundations-04`,
  `sec:writing-foundations-07`. Linked, not duplicated.
- Not listed but found and linked as relationships:
  - `rule:p09-hoare-while-partial` / `rule:p09-hoare-while-total`
    (`registry/calculi/hoare-while.tex`) and `def:p09-hoare-triple`: loop
    invariants in Hoare logic.
  - `parts/p09/presentations/n-c-012.tex:805` (global-invariant method in a
    concurrency presentation); not cited in reader text.
  - `parts/p01/formal-work-conventions.tex:190` mentions a maintained
    invariant in a proof plan (off the P1 driver route; not cited).
  - `thm:p02-horn-sat` (cited, forward chaining); the new worked example
    proves the correctness half by invariants and does not prove the time
    bound.
  - `lem:prop-lindenbaum`: an invariant (consistency) at finite stages with a
    separate limit argument; linked from the limit theorem.
  - IPL: `sec:intuitionistic-logic-01` already contains the two-world
    counterexample to excluded middle and double-negation elimination
    (source line 13100). The new theorem reuses that structure, adds Peirce,
    the contraposition instance, the De Morgan direction and the reductio
    rule instance, and derives non-derivability through the soundness theorem.

## Decisions

- All proofs of the new results are editorial completions; none is
  attributed to Floyd, Hoare or the frozen manuscript. Floyd and Hoare are
  cited only for the historical formulation of the method (exact pages above).
- Formula metavariables are the global `\varphi,\psi`; IPL notation follows
  the editorial p08 file (`\mathsf{IPL}`, `\derives_{\mathsf{IPL}}`,
  `\entails_{\mathsf{IPL}}`, `\forces`, `\nforces`, `\bottom`), because the
  source macros `\IPL`, `\LJ`, `\CPL` raise errors outside restoration scopes.
- Classical consequence is written `\entails_{\mathsf{CPL}}` (instance of the
  registered per-system pattern); negation is read as `\varphi\to\bottom` in
  both logics, which has the same classical truth value as primitive negation.
- Non-derivability claims go through `thm:p08-ipl-completeness-soundness`;
  derivability claims go through `thm:p08-ipl-strong-completeness-full`
  (proved in classical ZFC; the stated metalogic here is classical).
- The Error taxonomy longtable is a source capture and is not patched; the new
  section supplies its own governing-logic row (table
  `tab:p01-w02-p01-023-logic-error`) in the same three-column form.

## Continuation

State at return (2026-10-04):

- 7.5 invariants: written in
  `handbook/parts/p01/formalizing-arguments-and-constructing-proofs-w02-p01-023.tex`
  lines 23-339 (sec:p01-w02-p01-023-invariants), proofs in
  `handbook/annex/p01/formalizing-arguments-and-constructing-proofs-w02-p01-023.tex`
  lines 8-210 (seven annex items).
- 7.7 governing logic: written in the same body file lines 340-602
  (sec:p01-w02-p01-023-governing-logic), proofs in annex lines 212-409.
- Restoration hosts compared byte-for-byte with the source this session:
  source 1505-1552 equals inherited-01505-01553.tex lines 1-48; source
  1592-1630 equals inherited-01592-01631.tex lines 1-39. No correction applied.
- Checks: unit-compile ok (4 overfull boxes: three annex headings whose long
  label ids do not break, one bibliography note); find_fused_spaces no hits;
  check.py --tree filtered to these files shows only bib-key for the own
  intake key FrozenFormalLogicProofMethods.
- Tool limitation found: tools/waves.py `_existing_labels` does not parse
  `\hbrule` labels, so a `\cref` to rule:p09-hoare-while-partial is reported
  as an unknown reference by unit-compile although the label exists in
  `handbook/registry/calculi/hoare-while.tex`. The body therefore points to
  `sec:p09-program-logics` and `def:p09-hoare-triple` instead.
- The lead inserts the two `\input` lines (drivers are read-only here).
