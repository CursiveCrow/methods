# Packet w02b-p01-013 (P1 chapter 8; sections 8.3, 8.4, 8.6, 8.7), block 1

Provenance note for the equivalence-glyph audit (S-003-C04 / A-168-C02). Not reader text.

## Scope of this block

The assessment named one remaining gap: section 8.4, components S-003-C04 and A-168-C02.
Live uses of the triple bar had no covering registry row at
handbook/parts/p05/decidable-arithmetics.tex:17 (Presburger congruence predicate),
handbook/parts/p15/conditional-expectation.tex:355 (h identically 1/2) and
handbook/parts/p15/characteristic-functions-and-inversion.tex:399 (phi identically 1),
and nothing on the route audited every live use of the triple bar, the double arrow and the
definitional sign against the registry. The superseded sole-elementary-equivalence rule is not
implemented (policy section 7 of spec/decisions/edition-2026-coverage-policy-resolution.md).

Existing treatments found and extended rather than duplicated:
handbook/parts/p01/symbol-registry.tex (editorial defaults, lines 15-25),
handbook/parts/p01/notation-binding-and-comparison-of-formal-w02-p01-025.tex
(sec:p01-w02-p01-025-signs, def:p01-w02-p01-025-equivalence-roles, thm:p01-w02-p01-025-equiv-bridges),
handbook/parts/p14/symbols-terminology-and-glossary.tex (glossary rows for the glyphs). The last
one was not in the packet's existing list.

## Audit method

1. Reader route: tools/symbol_registry.py ReaderIndex over handbook/main.tex (1689 live files),
   with each regex hit placed at the reader position of the last preceding command, so that a
   registry scope (numeric, label, label range or named binding) can be tested for containment.
2. Occurrences: every `\equiv` (with any attached subscript or superscript), `\Leftrightarrow`
   and `\defeq` after comment and verbatim stripping: 1925 occurrences (989 definitional-sign
   macro, 622 bare triple bar, 64 double arrow, 250 subscripted or superscripted triple bars).
3. Coverage: an occurrence is covered when a row of handbook/registry/symbols.csv or an intake
   CSV with the same glyph form lies in scope; for bare forms only rows whose glyph has the bare
   sign count. Occurrences covered only by the global rows (30 editorial formula equivalence,
   32 definitional sign, 42 elementary equivalence, 6555 source definitional sign) were read and
   accepted only when the operands match that row's type (structures for row 42, formulas for
   row 30, a colon prefix for row 32).
4. Literal `\mathrel{:\equiv}` is the definitional sign (row 32). The `\defeq` macro prints
   `:\equiv` (row 32) and inside the restoration provenance scopes `:=` (row 6555, handbook.sty
   around line 1539); both roles are global, so every macro use maps to one of them by its
   printing region.
5. Family instances: subscripted forms whose index is a declared metavariable of a registered
   family in scope were mapped to that family row (rows 3717 Morley approximants, 807 Lawvere
   equational congruence, 2258 rewriting congruence, 1928 small-clause equivalence with its
   bare-chain note).

Result after adding the 77 intake rows: every occurrence is mapped to a row, except the three
first-order equivalence chains in handbook/restoration/inherited-15638-16742.tex (exercise
feedback, lines 334-335 and 994). That file carries only `ch:` and `app:` labels, which a
registry scope cannot name (tools/symbol_registry.py LABEL_RE), so a named scope binding in
handbook/registry/symbol-scopes.json is needed (blocked_policy; lead change). The same blocker
affects the earlier intake rows 9 and 12 of
handbook/registry/symbols-intake-p01-notation-binding-and-comparison-of-formal-w02-p01-025.csv
(scopes `app:exercise-feedback`, `app:notation` do not resolve).

Validation: the intake resolves with no errors through symbol_registry.read_rows, and
collision_check over symbols.csv plus the intake reports no collision involving the intake.

## Role assignments by region (intake rows)

- Presburger congruence predicate: def:p05-presburger through def:p05-presburger-example.
- Identically equal: thm:p15-conditional-examples, thm:p15-characteristic-second-moment,
  sec:p15-characteristic-function-criteria-and-moments and its annex section,
  sec:annex-p15-bayes-factor-computation.
- Metalinguistic number congruence: sec:p09-presentation-n-c-012 (n congruent n' mod 2).
- Double arrow between assertions: global (first use def:p01-w02-p01-022-setting); regions
  read: P4 complexity, Turing degrees, frontiers; P6 finite character, Suslin, absoluteness;
  P2 second-order chapters and annex.
- CPL semantic equivalence outside the named CPL scope: ten P2 body and annex sections.
- First-order equivalence and alpha-equivalence extensions: P1 annexes, P2 Craig-Beth annex,
  P7 cut-elimination and equality chapters.
- Displayed register entries: sec:p01-symbol-registry, sec:p01-w02-p01-024-notation,
  sec:p01-w02-p01-025-overview, sec:p14-symbols-terminology-and-glossary; Principia column in
  sec:p01-notation-variants.
- Object-language connectives: Church type theory (P2 040 body and annex), Lambek-Scott
  internal language (P10 n-d-023 body and annex; the calculus sheet lies inside the body
  section region), Reichenbach (P15), erotetic languages (P18 body and proofs).
- Equivalence of a declared semantics, also introducing defined operators: P9 logic in computer
  science, presentations n-c-012 to n-c-021, Stavi body and annex, finite-tree annex.
- Named relations: filter agreement (P3 Feferman-Vaught), rank agreement (P3 abstract annex),
  Morley approximants annex, equality pattern (P2 035 annex), Weihrauch (P4 body and annex),
  judgmental equality (P7 HIT, circle, identity systems and their annexes), provable
  equivalence (P10), rewriting congruence instances (P12 fair completion, rewriting annex),
  small-clause bare chains (P12 annex), Emerson-Halpern, CEGAR, tree-depth and filtration
  relations (P9 presentations), predicate definition (P15 PR learning), sentence equivalence
  (P15 systematic power), classical equivalence (P16 deductive-nomological).

## Reader text written

- handbook/parts/p01/notation-binding-and-comparison-of-formal-w02b-p01-013.tex: chapter
  sec:p01-w02b-p01-013-equivalence-audit with def:...-congruence-predicate,
  def:...-identically-equal, def:...-statement-iff, def:...-mention, def:...-role-reading,
  thm:...-congruence-definable, thm:...-identically-equal, def:...-example, def:...-failure,
  tab:...-roles.
- handbook/annex/p01/notation-binding-and-comparison-of-formal-w02b-p01-013.tex: the two
  annex proofs.
- work/waves/w02b/patches/w02b-p01-013.json: glosses at the three named sites (anchors
  verified unique).

Sources: no source-specific presentation is written. The congruence lemma is proved from the
division algorithm and the satisfaction clauses; Presburger1929 is cited only as the source of
the elimination theorem already cited by def:p05-presburger. No page locator is given.

## Continuation

- Lead: insert the body after `parts/p01/notation-binding-and-comparison-of-formal-w02-p01-025`
  in handbook/parts/p01.tex (it extends that chapter's convention) and the annex after
  `annex/p01/notation-binding-and-comparison-of-formal-w02-p01-025` in
  handbook/annex/p01-route.tex; apply the three patch requests.
- Lead: add a named scope binding for `restoration/inherited-15638-16742.tex` (and the
  `app:notation` region) to symbol-scopes.json, then a row
  `\(\varphi\equiv\psi\)`, source first-order logical equivalence of formulas, scoped to it.
- Open: each of the 989 `\defeq` uses is mapped by its printing region; the individual uses
  were not read one by one for definitional usage. Subscripted groups were classified from
  their first occurrences and the declarations of their sections; bare groups were read in
  full.
