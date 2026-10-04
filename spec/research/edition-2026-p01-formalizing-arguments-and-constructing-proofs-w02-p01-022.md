# w02-p01-022: sections 7.1, 7.2, 7.3 (formalizing arguments; ambiguity, restricted quantification, uniqueness and scope; typed definitions and theorem statements)

Provenance note for packet `work/waves/w02/packets/w02-p01-022.json`, label tag
`p01-w02-p01-022`. Session date 2026-10-04.

## Gap addressed

Assessment disputes for 7.2: (a) ambiguity: only the instruction in
`handbook/restoration/inherited-01024-01084.tex` lines 35-36 and the
quantifier-order example (48-60); nothing on detection, resolution or
recording; (b) restricted quantification named only; no patterns, no
conditional/conjunction warning; (c) uniqueness named only; no formalization of
"exactly one", "the unique", definite descriptions.

New section `sec:p01-w02-p01-022-translation` (body
`handbook/parts/p01/formalizing-arguments-and-constructing-proofs-w02-p01-022.tex`,
annex `handbook/annex/p01/formalizing-arguments-and-constructing-proofs-w02-p01-022.tex`):

- setting: background set Pi, Pi-equivalence, solution sets
  (def:...-setting);
- ambiguity: def:...-reading (dictionary, reading, ambiguity relative to L and
  Pi, separating structure, harmless/harmful), def:...-kinds (lexical,
  structural, scope, pronoun, plurality with their formal effect),
  thm:...-readings (Pi-equivalent readings interchangeable; all premise
  readings = disjunction; all conclusion readings = conjunction),
  def:...-ambiguity-method (detect/separate/resolve/record/unresolved),
  examples lexical (equivocation with countermodel), scope
  (thm:...-negation-scope), pronoun (thm:...-indefinite lemma), plurality
  (distributive/collective/numerical);
- restricted quantification: thm:...-relativization (semantics, duality,
  empty restrictor), def:...-patterns (table incl. "only", nested
  restrictor, existential import), thm:...-mismatch (exact cost of
  forall-with-and and exists-with-implies; existential import),
  def:...-mismatch-warning;
- uniqueness: def:...-uniqueness (at most one, exactly one, comparison
  variable), thm:...-uniqueness (counting characterization, equivalent
  forms, independence of comparison variable), thm:...-freshness (failure
  when the comparison variable is free), thm:...-exactly-one (exactly one P
  is Q vs the P is Q), example reviewers (source exercise ex:fol-deduction-06
  sentences translated);
- descriptions: def:...-description (Russellian contextual elimination,
  wide/narrow = primary/secondary), thm:...-description-scope,
  def:...-description-warning (description is not a name; links to free-logic
  description policies);
- worked example def:...-worked + thm:...-worked (validity; invalidity
  without the uniqueness clause);
- limitations and relationships.

All results proved in the annex (10 annexitems).

## Components (sections 7.1 and 7.3 source blocks)

The eleven packet components are source blocks preserved by the restoration
captures. Checked this session with `diff`: 
`handbook/restoration/inherited-01024-01084.tex` is byte-identical to source
lines 1024-1084 (restoration line = source line - 1023), and
`handbook/restoration/inherited-01411-01504.tex` is byte-identical to source
lines 1411-1504 (restoration line = source line - 1410). Both are on the P1
route through `restoration/scope-SRC-01024-01084` and
`restoration/scope-SRC-01411-01504` in `handbook/parts/p01.tex`. No correction
applied; none needed. Those hosts are read-only and were not edited.

## Inputs opened this session

Held source FLRV1, Version 1.0, `source/formal-logic-reference.tex` (title
page 173-193 read: "Formal Logic / Language, Semantics, Deduction, and
Metatheory", Version 1.0, 9 August 2026). Lines read: 1024-1084 (via diff and
restoration text), 1411-1504 (same), 1600-1660 (error taxonomy table rows,
exercises), 1705-1717 (association convention, defined connectives),
1925-1945 (exclusive disjunction example), 2910-2935, 3038-3104 (signature
and term definitions, via grep of lines), 3125-3140 (quantifier display
convention), 3240-3260 (capture-avoiding substitution heading/definition,
via grep), 3519-3728 (satisfaction, coincidence, substitution lemma, truth
and consequence; translation with quantifiers; byte-identical to
restoration files 03519-03680 and 03681-03728 by diff), 3798-3818 (infinite
structures example), 4260-4300 (exercises incl. ex:fol-deduction-06).

Russell1905 (held: `source/references/acq-r1-ACQ-2026-10-0425/russell-1905-on-denoting-mind-14-56.pdf`,
PDF pp. 39-53 = printed pp. 479-493, extracted with pdftotext this session).
Locators used and seen: p. 481 (analysis of "C (a man)" as a conjunction not
always false; "all men are mortal" as hypothetical; footnote on the
suggestion of "only one" / "more than one", which is neglected), pp. 481-482
(the father of Charles II: uniqueness, elimination), p. 482 (if the
uniqueness condition fails every proposition of that form is false), p. 489
(primary and secondary occurrences defined), p. 490 ("C has the property"
analysis, King of France not bald under primary vs secondary). Russell1905 is
already in `handbook/bib/handbook.bib`; no intake entry needed.

## Existing treatment search (A9)

Listed: restoration 01024-01084 and 01411-01504 (extended, not edited).
Found and linked, not listed in the packet:
- `sec:fol-semantics-03` (`handbook/restoration/inherited-03681-03728.tex`):
  restricted quantification abbreviation and quantifier-order example; the
  new section cites it and adds semantics, patterns and mismatch results
  instead of re-defining the abbreviation.
- `sec:prop-syntax-semantics-03` (`inherited-01899-01945.tex`): "only if",
  "unless", exclusive disjunction "exactly one of P and Q"; linked.
- `sec:writing-foundations-07` (`inherited-01592-01631.tex`): error taxonomy
  row "Scope error" recommends explicit restricted quantification; linked
  from the mismatch warning.
- `sec:zf-zfc-01` (`inherited-10089-10271.tex` line 93): exists! abbreviation
  with fresh z; linked.
- `sec:p02-free-logic` (`handbook/parts/p02/variants.tex` 255-330):
  Russellian contextual principles and Lambert's law for a primitive iota;
  `sec:p08-conditionals-deontic-free` lines 36-54: Russellian elimination vs
  primitive descriptions. Linked from the description warning; not repeated.
- `sec:p02-many-sorted`: relativization of quantifiers to sort predicates;
  linked.
- Off route (not linked): `handbook/parts/p01/formal-work-conventions.tex`
  def:p01-formalizing-argument (lists ambiguity among things to resolve,
  no treatment); `handbook/parts/p06/axioms-hierarchy.tex` exists!
  abbreviation.

## Decisions

- Comparison-variable condition: "does not occur in phi" (stronger than "not
  free") so that phi[y/x] needs no renaming and the coincidence argument is
  direct. Freshness failure shown by thm:...-freshness.
- `\mathsf{the}_x(phi, chi)` is a metalinguistic abbreviation, not the
  registered iota term former; wide/narrow terminology with Russell's
  primary/secondary cited.
- Background set named Pi (scoped to this section; other Pi roles have
  disjoint scopes).
- Tense and modality from the inherited step 3 are not treated here (stated
  limitation in reader text); they were not among the assessment gaps.

## Checks

unit-compile ok (1 overfull box, 1.5pt, auto-generated annex heading); find_fused_spaces no hits; check.py --tree filtered: only bib-key for own intake key FrozenFormalLogicFormalizing. Example nouns use 'referee' (source exercise uses 'reviewer'; reader text says so).

## Continuation

All three 7.2 gaps (ambiguity, restricted quantification, uniqueness) are
written in the new section with annex proofs. Remaining for the lead:
insert `\input{parts/p01/formalizing-arguments-and-constructing-proofs-w02-p01-022}`
in `handbook/parts/p01.tex` after `restoration/scope-SRC-01592-01631` and the
annex input in `handbook/annex/p01-route.tex` after
`annex/p01/equivalence-closure-and-quotients`; merge the bib and symbol
intakes.
