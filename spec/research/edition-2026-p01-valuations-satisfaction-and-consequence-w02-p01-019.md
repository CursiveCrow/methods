# w02-p01-019: section 6.7 (soundness, completeness, consistency, distinct implications)

Provenance note for packet `work/waves/w02/packets/w02-p01-019.json`, label tag
`p01-w02-p01-019`. Session date 2026-10-04.

## Gap addressed

Assessment gap for 6.7 against `handbook/restoration/inherited-00907-00984.tex`
lines 53-77 (`sec:levels-03`): the interval has the Soundness and Completeness
definitions and the Direction-check warning, but no general definition of
consistency for a specified calculus and no proved comparison of the three
notions. Consistency existed only calculus- or theory-specifically
(inherited-02545-02664.tex 4-7 ND_CPL; inherited-04306-04575.tex 12-17 ND_FOL;
inherited-09498-09538.tex 4-12 theories); deductive vs semantic completeness at
inherited-07150-07294.tex 60-80 and inherited-09498-09538.tex 14-19.

The host interval is read-only and was not edited. New section
`sec:p01-w02-p01-019-consistency` (body) and
`sec:annex-p01-w02-p01-019-consistency` (annex) supply the general definition,
the comparison theorems with full annex proofs, separating examples, a worked
example, limits, relationships and sources, linking to the existing treatments
instead of restating them.

## Inputs opened this session (held source FLRV1, Version 1.0)

`source/formal-logic-reference.tex` (packet held path), read at lines 900-1000
(sec:levels-03, units U00072-U00074 at 959-967, 969-977, 979-983; diffed
against restoration lines 53-77: identical), 1661-1700 (propositional alphabet,
readable-example convention P,Q,R,S), 2451-2465 (CPL soundness theorem),
2545-2552 (definition Consistency, ND_CPL), 2665-2720 (strong completeness,
compactness), 4317-4323 (First-order consistency), 7150 (chapter heading),
7209-7229 (Deductive completeness... definition), 9498-9510 (Consistency for
theories), 12973-13110 (intuitionistic Kripke structures, forcing, consequence,
soundness and strong completeness of IPL with proof sketch, counterexample
structure). Restoration files read: inherited-00907-00984, 00985-01023,
01817-01898 (coincidence lemma), 02193-02340 head (ND derivation definition,
relabeling), 02451-02544 head, 02545-02664 head, 02665-02809 head,
04306-04575 head, 07150-07294 lines 50-90, 09498-09538; registry sheet
nd-cpl.tex (rules incl. nonvacuous RAA). Sibling packet w02-p01-016 body and
return read for satisfiability / unsat-reduction labels used here.

## Decisions

- Three forms of consistency (absolute/trivial, negation, falsum) defined for an
  arbitrary calculus; unqualified "consistent" = negation consistency, matching
  the theory definition in sec:first-incompleteness-02.
- "For an explosive calculus with negation, completeness iff every consistent
  set satisfiable" (assessment example) is stated exactly: the forward
  direction holds for every calculus and semantics; the converse needs reductio
  (which implies explosion). Explosion alone does not suffice, proved by the
  test calculus C_ex. This keeps the assessment's claim and adds the hypothesis
  under which it is true.
- Soundness: shown equivalent (classical negation clause + reflexivity) to
  consistency of every satisfiable set; consistency of the calculus is the
  instance at the empty set; C_P separates them.
- Test calculi C_0, C_ex, C_P are editorial counterexamples with decidable rule
  sets (side conditions decided by finite truth tables via
  thm:p01-w02-p01-016-finite-check); proofs use thm:prop-compactness.
- Intuitionistic limitation proved directly from the forcing clauses; the
  application to IPL rests on the source theorem "Soundness and strong
  completeness of IPL", which the source gives with a proof sketch; the body
  says so.
- Notation: \mathsf{ND}_{\mathsf{CPL}}, \mathsf{Fm}_{\mathsf{CPL}}, \mathsf{IPL}
  written out because the short macros are restricted to inherited scopes.
  Worked-example third variable is S (not R) to avoid clashing with the
  rule-set metavariable R.

## Placement

Body after `parts/p01/valuations-satisfaction-and-consequence-w02-p01-016` if
that input is present (it is proposed after restoration/scope-SRC-00985-01023),
otherwise directly after restoration/scope-SRC-00985-01023. Annex likewise after
the w02-p01-016 annex input, otherwise after
annex/p01/boolean-prime-ideal-and-ultrafilters. The section depends on labels
from w02-p01-016 (def:p01-w02-p01-016-datum, -satisfaction, -satisfiable,
thm:p01-w02-p01-016-unsat-reduction, -sentences, -variants, -finite-check,
sec:p01-w02-p01-016-models); it cannot be routed without that packet.

## Continuation

Block 2 (4 October 2026). Hard guard G1 named six files of packets
w02-p02-044, w02-p02-045 and w02-p02-054 (their research notes and returns).
They were written by those packets' agents in the shared tree at 04:01-04:08,
interleaved with this packet's writes; this packet did not write them and,
under the rule against modifying other agents' files, did not touch or delete
them. Reported in the return as a guard attribution for the lead.

Re-verified this block: sibling labels from w02-p01-016 present and clause
numbering of thm:p01-w02-p01-016-unsat-reduction unchanged (clauses 1, 3, 4
as used); unit-compile ok (5 overfull boxes, cosmetic); find_fused_spaces no
hits; check.py shows only bib-key for the intake key
FrozenFormalLogicConsistencyComparison. Body and annex text unchanged in
this block. Lead actions: insert the two driver input lines after the
w02-p01-016 inputs; merge intake bib and symbol rows; re-attribute the G1
files.
