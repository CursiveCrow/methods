# w02-p01-016: sections 6.1, 6.3, 6.4 (semantic data, models, undischarged assumptions)

Provenance note for packet `work/waves/w02/packets/w02-p01-016.json`, label tag
`p01-w02-p01-016`. Session date 2026-10-04.

## Gaps addressed

Assessment disputes against the reader interval
`handbook/restoration/inherited-00907-00984.tex` lines 1-78 (`sec:levels-03`):

- 6.1: no standalone account of semantic data / complete tuple; variable
  assignments only mentioned (no domain/codomain, no variants); satisfaction
  used but not defined in the interval.
- 6.3: models absent; satisfiability absent.
- 6.4: undischarged assumptions only used inside Derivability; no account of
  assumptions, discharge, or undischarged status.

The host interval is read-only and was not edited. The new section
`sec:p01-w02-p01-016-semantic-data` supplies the missing definitions and
results and links back to `sec:levels-01`, `sec:levels-03`, `sec:levels-04`.

## Inputs opened this session (held source FLRV1, Version 1.0)

`source/formal-logic-reference.tex` (packet held path), read at lines:
- 798-852 chapter "Levels, Objects, and Consequence", section "Formal logic and a
  logical system" (definitions Formal language, Calculus, Semantics, Logical system);
- 907-984 section "Syntax, semantics, and proof theory" (components U00065-U00074);
- 985-1060 sections "Truth, satisfaction, validity, and models" and "Arguments and
  formalization" (Satisfaction, Truth in a structure, Model, Countermodel);
- 1661-1700 propositional alphabet and formula; 1817-1898 "Valuations and recursive
  truth clauses" (Truth values and valuation, lemma Coincidence for propositional
  formulas `lem:prop-coincidence`, Semantic notions, truth-table example);
- 2187-2340 "Classical natural deduction" (Natural-deduction derivation: leaves,
  discharge labels, open assumptions, merging relabeling; rule list; Propositional
  derivability; examples; lemma `lem:nd-substitution`);
- 2344-2380 "Sequent" definition with support lifting;
- 2665-2700 "Strong completeness of classical propositional natural deduction"
  (`thm:prop-completeness`, proof via consistency of Gamma u {neg phi});
- 3429-3680 chapter "Structures, Satisfaction, and Translation" (structure, extension,
  Variable assignment and update, Term value, Satisfaction clauses, Formula
  coincidence `lem:fol-coincidence`, substitution, assignment independence corollary
  (unlabelled), Truth, validity, and semantic consequence);
- 3729-3770 chapter "Theories and Axiomatization" (`def:fol-theory-satisfiability`);
- 3927-3995 "Natural-deduction rules for quantifiers and equality" and "First-order
  derivability";
- 12973-13045 "Intuitionistic Logic": lifted IPL derivability through finite
  contexts, negation defined as A -> bottom, intuitionistic Kripke structure and the
  forcing clauses (atomic clause w in V(p));
- 13201-13290 "Modal, Temporal, and Epistemic Logic": Kripke frame and structure,
  structure/frame validity, local and global consequence ("can differ"), Hilbert
  calculi K, T, S4, S5 with premise-sensitive derivations and theorem-only Nec;
- 13825-13845 Routley-Meyer atomic clause (checked only to locate where atomic
  satisfaction w in V(p) is stated).

Restoration captures 01817-01898, 02193-02340, 03429-03518, 03519-03680, 03729-03907,
03927-04061, 00907-00984, 00985-01023 were diffed against the source: identical.

## Decisions

- Modal atomic clause: the modal Kripke definition does not display it. The text
  states the reading M,w |= p iff w in V(p) explicitly as a reading, citing the
  intuitionistic forcing clause for a valuation of the same type. Not attributed to
  the modal definition.
- "Model" is kept to the registered first-order sense (sets of sentences); the
  propositional and modal data are not called models (sec:levels-04 restriction).
- Assumption leaves are described as carrying labels from N, following the source's
  "Discharge labels are metalinguistic markers drawn from N" and merging relabeling.
- Discharge theorem case 2 (no open occurrence of phi) uses land I / land E_2 because
  the source forbids a label that discharges nothing.
- Bib key FrozenFormalLogicSemanticData (own intake), same pattern as the sibling
  keys FrozenFormalLogicLanguageChange / FrozenFormalLogicFoundationsClosure.
- Source macros \Meta, \Prop, \Var, \ND, \Mod etc. are guarded outside restoration
  scopes; editorial forms (\mathcal M, \mathsf{Prop}, \mathsf{Var}, \dom,
  \operatorname{Mod}) are used.

## Existing treatment found (not in packet's existing list)

- `handbook/parts/p01/formal-work-conventions.tex` tables `tab:p01-level-vocabulary`
  and `tab:p01-consequence-vocabulary` (schematic satisfaction, model, derivability
  with "undischarged assumptions"); not on the p01 driver route; not cited.
- `handbook/parts/p02/propositional-syntax-semantics.tex` line 169 (propositional
  satisfiable) and `handbook/parts/p02/first-order-syntax-semantics.tex` line 443
  (`def:p02-fol-theory`); not on the p02 driver route; not cited.
- On-route inherited definitions (`sec:prop-syntax-semantics-02`,
  `sec:prop-deduction-01`, `sec:fol-semantics-01/02`, `def:fol-theory-satisfiability`,
  `sec:fol-deduction-01`, `sec:modal-temporal-epistemic-01`) are linked, not restated
  beyond the clauses the new definitions need.

## Continuation

State at return (2026-10-04): body
`handbook/parts/p01/valuations-satisfaction-and-consequence-w02-p01-016.tex`
(lines 1-603) and annex
`handbook/annex/p01/valuations-satisfaction-and-consequence-w02-p01-016.tex`
(lines 1-414) written; eleven annexitems, one per body result. unit-compile ok
(7 small overfull boxes, largest about 10.8pt in the annex/bibliography);
find_fused_spaces no hits; check.py filtered shows only bib-key for the own intake
key. Driver insertions (p01.tex after restoration/scope-SRC-00985-01023;
annex/p01-route.tex after annex/p01/boolean-prime-ideal-and-ultrafilters) are for the
lead. No component is reported partial or blocked; one open item (modal
atomic clause reading) is listed in the return file.
