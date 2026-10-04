# Phase 4 verification: Part 5 depth completion

> **PASS VERDICT INVALIDATED (2026-08-12).** This note verified the revoked
> compressed-migration policy, not the binding full-transcription standard.
> Retain it only as audit evidence; see `FULL-TRANSCRIPTION-READINESS.md`.

Date: 2026-08-11
Visit: P5d, Arithmetic and Incompleteness depth completion
Verified source: `v1.1-verified`, Part VI, especially lines 9192--9229,
9249--9260, and 9373--9437.

## Delivered scope

- New body chapter: standard and nonstandard arithmetic models, finite-distance
  blocks, the countable nonstandard-PA order type, overspill, Tennenbaum's
  theorem, external and formalized Sigma-one completeness, and relative
  interpretation with essential-undecidability transfer.
- New annex fragment: the migrated compactness proof and the honest
  Sigma-one-completeness sketch.
- New result inventory: six statused results -- one `proved`, one `sketched`,
  and four `cited` -- with exactly two new annex items.
- Full P5 result inventory after the visit: seventeen statused results -- seven
  `proved`, four `sketched`, and six `cited`; the eleven proved/sketched results
  have an exact eleven-to-eleven body--annex graph.
- Four Phase-5 stub chapters remain, as required.  No fifth remainder stub was
  introduced.

## Source and evidence accounting

The source definition of standard and nonstandard models, its complete
compactness proof, the nonstandard-PA example, and the restricted
truth-to-provability warning were migrated.  The compactness theorem remains
`proved`; its proof retains finite satisfiability, compactness, the
numeral-preserving isomorphism contradiction, and downward
Loewenheim--Skolem with the new constant designated.

Under the established one-pass `detex` alphabetic-word method, excluding the
result statement and proof delimiters, the compactness proof has 112 source
words and 66 annex words, or 58.9 percent.  It is inside the Tier-2 target and
was not tuned further after reaching compliance.

The source only states the restricted Sigma-one fact implicitly and does not
supply a complete proof block from which an honest compression denominator
could be taken.  The new named result therefore remains `sketched`; its annex
note explicitly owes the bounded-form induction, normal-form conversion,
numeral-substitution invariant, primitive-recursive witness-to-proof-code
construction, and verification inside PA.  No ratio was manufactured for it.

The v1.1 arithmetization-of-syntax sketch is deliberately retired as a
separate printed result, not relabeled or claimed proved elsewhere.  Its
primitive-recursive existence conclusion remains explicit in the fixed proof-
predicate definition; Part 4 supplies shared coding and bounded-certificate
ingredients, while the P5 source disposition expressly says that those
entries do not reprove the omitted syntax-specific induction.  The three
source exercises are also explicitly retired because the handbook has no
exercise layer; their elementary-equivalence, proof-predicate typing, and
coded-sequence cautions survive in adjacent entries.

## Depth and new-content rows

- D-P6-002 is filled at S by the cited, exactly scoped Tennenbaum statement.
- D-P6-003 is filled at E by the exact PA-model definitions, countable order-
  type theorem, overspill theorem, and worked application.
- D-P6-005 and N-a-029 are filled at S by the one-dimensional parameter-free
  interpretation entry, examples, essential-undecidability transfer, and
  interpretability-logic pointer.
- D-P6-006 remains open at its E ceiling.  The requested named statement and
  annex sketch exist, but the binding CSV requires a complete proof.  The
  existing independence-catalog stub names that exact full-proof remainder.
- N-a-032 remains open because its E package requires a T-level proof of
  Tennenbaum's theorem.  The delivered S-level cited statement is not reported
  as fulfilling that ceiling, and the same existing stub names the remainder.
- D-P6-001, D-P6-004, D-P6-007, and D-P6-008 remain explicitly named in the
  four Phase-5 chapter stubs.  Their corresponding Phase-4 apparatus rows
  A-053 through A-057 and A-128 remain open rather than being falsely marked
  complete.

## Adversarial correction log

The independent fidelity and standards passes corrected:

- the phrase `standard initial segment`, restricting it to PA models while
  retaining `standard numerals` for arbitrary arithmetic theories;
- the finite-distance-block entry, replacing vague subtraction prose with an
  exact external-natural-number equivalence relation;
- the overspill scope, including parameters, no countability hypothesis, the
  stronger initial-segment form, and its parameter-definability consequence;
- quotient interpretations, adding interpreted equality, total functional
  graphs modulo that equality, and the required congruence obligations without
  silently choosing representatives;
- the Sigma-one sketch's construction and omission list;
- the compactness proof's load-bearing isomorphism contradiction;
- the source-disposition paragraph, which no longer claims that Part 4 proves
  syntax arithmetization and now accounts for all three source exercises;
- the D-P6-006 and N-a-032 remainder wording, keeping exactly four stubs; and
- the chapter running head and symbol intake for order type and interpretation
  data.

## Mechanical evidence

- Integrated TeX Live 2025 `latexmk` build with biber and makeindex: pass,
  474 pages; no undefined citation, reference, or control-sequence warning.
- `python tools/check.py --tree handbook --strict`: pass; 304 symbol rows,
  289 distinct glyphs, 363 bibliography entries, 124 proved / 21 sketched /
  93 cited statuses globally, zero malformed statuses, and 31 tracked stubs,
  exactly four in P5.
- `python tools/check.py --tree source`: pass; the source file is byte-identical
  to `v1.1-verified` by Git object hash.
- `python tools/symbols2tex.py`: pass; 304 rows in ten scope groups.
- `python tools/audit_tables.py`: pass; 50 generated P5 audit rows and 514 rows
  across all fourteen generated part tables.
- Text-tree `git diff --check`, excluding the tracked binary `main.pdf`,
  passes; `git diff --exit-code -- source` is empty.

## Visual evidence

The final 474-page PDF was rendered and inspected across physical pages
291--310 and 427--432.  This covers the entire new P5 body chapter, all four
retained stub chapters, the regenerated P5 audit register, the P5 annex, and
the adjacent chapter transitions.

The initial running-head collision on the new chapter's even pages was fixed
with a shorter chapter mark and rerendered.  The final pages have no clipped
text, overlap, broken glyph, unreadable table, malformed stub box, or broken
page transition.  Four small heading overfull warnings remain in the TeX log;
their rendered headings wrap legibly and do not cross the text block.

The mathematical/spec review is a PASS.  The standards review found no
remaining content violation; its temporary finalizer-only blockers (stale
audit table, unmerged symbol intake, and unreconstructed full PDF) were all
resolved by the integrated generation, build, strict/source checks, and visual
pass recorded above.  Compilation and rendering establish integration and
presentation, not independent human mathematical review.
