# w02-p01-013: section 5.7 (transfinite recursion on an ordinal, full proof)

Provenance note for packet `work/waves/w02/packets/w02-p01-013.json`, label tag
`p01-w02-p01-013`. Session date 2026-10-04.

## Gap addressed

5.7: existence and uniqueness of set-length transfinite recursion were
citation-only (`thm:transfinite-recursion`, handbook/restoration/inherited-00603-00647.tex
29-44, "Status: cited theorem", proof deferred to Jech2003). The P6 class
version (annex p6.ordinals.3 and inherited-10353-10451 74-97) is a sketch.

Written: `thm:p01-w02-p01-013-recursion` (proved=annex) restating the source
theorem with identical hypotheses, notation and closing qualification; full
annex proof via two lemmas (`thm:p01-w02-p01-013-agreement`,
`thm:p01-w02-p01-013-assembly`), two corollaries (coherence across lengths;
zero/successor/limit form), a worked example with a proved values lemma, a
proved counterexample lemma (ill-founded index: uniqueness failure and
existence failure), a method entry with side conditions, a warning with
limitations, relationships and sources.

## Source block FLRV1-U00040 (source lines 631-642)

Mapped content: ordinal delta; functional rule G defined on every function
whose domain is an ordinal smaller than delta; unique F with domain delta;
recursion equation; label `thm:transfinite-recursion` (kept on the capture,
cross-referenced); qualification "metalinguistic recursion principle ... not a
new inference rule of any object-language calculus" (carried in the theorem);
attributed standing "Status: cited theorem" / "See Jech2003" (reported in the
Sources subsection; superseded by the full proof).

Authorized corrections identified: none to the mathematics. The statement is
correct as a ZF schema. Two editorial explications (not corrections): (1)
"functional rule" is read as a formula theta(g,y,p) with set parameters
(convention `def:p01-w02-p01-013-reading`, item 4), so the theorem is a
schema; (2) standing changes from cited to proved. The capture's status line
is read-only; patch request `work/waves/w02/patches/w02-p01-013.json`.

## Inputs opened this session

- `source/formal-logic-reference.tex` (held, FLRV1 v1.0): lines 365, 450-470
  (strict well-order definition), 533 (section heading "Finite, countable, and
  uncountable sets"), 603-650 (ordinal definition, theorem 631-642), 10063,
  10089, 10120-10185 (Separation and Replacement schemas).
- Handbook: restoration/inherited-00603-00647.tex, inherited-10353-10451.tex
  60-100, inherited-04306-04575.tex (lem:transfinite-lindenbaum uses);
  parts/p06/axioms-hierarchy.tex 229-290 and its annex 40-100;
  parts/p01/finite-strings-numerical-coding-and-the-w02-p01-011.tex and annex
  (ordinal facts lemma reused, not duplicated);
  parts/p01/sets-relations-functions-and-quotients-w02-p01-005.tex;
  parts/p01/mathematical-preliminaries.tex 80-140.
- Halbeisen2017 held file (2011 manuscript) opened; text extraction is
  unreadable (Type 3 fonts) and the version differs from the key; not cited.
- Jech2003 is NOT held; no locator written. The handbook now proves the
  theorem, so no Jech locator is needed for the proof.

## Existing treatment found

- Listed: inherited-00603-00647.tex (capture), inherited-04306-04575.tex
  (users of the theorem).
- Not listed: parts/p01/mathematical-preliminaries.tex 109-115
  `thm:p01-transfinite-recursion` (cited=Jech2003); off route (not input by
  parts/p01.tex); not reused, label not duplicated.
- Not listed: P6 `thm:p06-transfinite-recursion` (sketched) and
  `thm:p06-transfinite-induction` (proved); linked from the warning and
  relationships.

## Dependencies

- `thm:p01-w02-p01-011-ordinals` (packet w02-p01-011) items 1, 3, 5, 6 are used
  by the proofs and must be on route with this section.

## Continuation

Block 2 (2026-10-04): G1 hard-guard hits name files of packets w02-p02-042,
-044 and -045 (spec/research/edition-2026-p02-unit-accounting-*); not created
or edited by this packet and left untouched. Fixes this block: stray "By"
fragment removed from the ill-founded proof (annex 380-381); body qualification
restored the source's "exact" and reworded (body 96-98). unit-compile ok;
check.py shows only the intake bib-key. Open: lead inserts driver lines
(parts/p01.tex after parts/p01/equivalence-closure-and-quotients;
annex/p01-route.tex after annex/p01/equivalence-closure-and-quotients) and
applies the capture status patch.
