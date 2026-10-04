# Bracket abstraction: source identity, proofs, and integration

Date: 9 September 2026. Authoring work only; independent admission remains pending.

## Assigned original content

The actual host is `handbook/parts/p07/lambda-calculi-and-type-theories.tex`,
Definition `def:p07-sk-combinators` and Theorem `thm:p07-bracket-abstraction`.
Its fixed algorithm has three cases: identity, an absent-variable shortcut for
an entire subtree, and recursive application. The unchanged primitive calculus
is `handbook/registry/calculi/sk-combinatory.tex`, `sheet:sk-combinatory`.

The exact original source allocation read from
`spec/coverage/edition-2026/completion-work-queue.jsonl` is
`ED26-REQ-N-a-015-04`, with components `N-a-015-S04-PRESENTATION`,
`N-a-015-S04-PROOF`, and `N-a-015-S04-BRIDGE`. Its selected 1958 presentation
includes combinators, reduction, bracket abstraction, substitution, and both
translations. That source obligation is retained separately. The overlapping
`ED26-REQ-D-P9-003-01` is the original untyped-lambda/confluence goal and does not
turn this supplement into a proof of lambda-definability equals partial
recursiveness.

## Exact supporting primary source read

Peter Selinger, *Lecture Notes on the Lambda Calculus*, arXiv 0804.3434,
version 2, dated 26 December 2013, 120 physical pages.

- Primary URL: https://arxiv.org/pdf/0804.3434v2
- Held source: `source/references/p07-monotonicity/selinger-2013-v2-lambda-notes.pdf`
- SHA-256: `9C4AD820D6A48E7D926996F04100830B86F4131BCA0CAB4BF1D6349A2182481F`
- Existing bibliography key: `Selinger2013LambdaNotesV2`.
- Read directly with the installed PDF text extractor: printed/physical pages
  39–46, including all of Sections 5.1–5.4, the definition of lambda algebra,
  the translations, and Lemmas 5.10–5.11; pages 49–50 for Section 5.6.
  The earlier local source reading already covered ordinary beta confluence;
  the active handbook has `thm:p07-church-rosser` with its own proof.
- This assignment selects the abstraction/representation and translation
  material just identified, plus the extensionality clauses. It does not select
  all nine-axiom characterizations of lambda algebras on pages 47–49.

The source's Section 5.2 uses an atom-by-atom abstractor, with separate variable,
coefficient, and application clauses. Its constant clause treats coefficients
as atoms in the polynomial language. The supplement preserves that source
construction as A and extends the coefficient case explicitly in the algebra
section. Its purely syntactic S–K specialization has only S and K as primitive
constant atoms. I is always expanded to S K K when the syntactic algorithm or
tree-size count is evaluated.

The source's Exercise 20 asks for combinatory confluence; the supplement supplies
the full parallel-development proof. Lemma 5.10 asks for the beta-correct lambda
round trip; the supplement supplies all of its abstraction cases. The source's
Section 5.4 explains failure of general lambda soundness in an arbitrary
combinatory algebra. The supplement gives a fully expanded host-algorithm
normal-form counterexample. Section 5.6 provides the extensionality condition;
the supplement proves the exact syntactic beta-eta/extensional correspondence
from that explicitly stated rule. These are independently worded derivations,
not verbatim reproduction of the source's prose.

## Curry–Feys 1958: acquisition boundary remains open

The exact selected 1958 body has not been acquired or read in this block.
The checked free search results supplied metadata, references, and later
presentations. The inspected Internet Archive item
https://archive.org/details/combinatorylogic0001curr identifies publication
year 1958, Volume 1, Amsterdam/North-Holland, 446 scanned pages, and explicitly
reports `Access-restricted-item true`. Its download section reports
`No suitable files to display here.` No access control was bypassed.
The Google Books record https://books.google.com/books/about/Combinatory_Logic.html?id=qrstAAAAMAAJ
is a snippet/contents record, not acquisition evidence for the selected body.

This is a bounded account of those checked surfaces, not a claim that no free
copy exists anywhere. The original source-specific manuscript unit remains
unfinished until a readable exact body is held, its actual internal locators
are recorded, and its separate presentation is supplied. The later Selinger
construction and the full host proof do not close that historical allocation.

## Completed mathematical content in this supplement

1. Full finite grammars, primitive combinators, FV and both substitutions.
2. All three host B cases and all four atom-by-atom A cases; termination,
   exact variable elimination, substitution/application, fresh renaming, and
   multi-argument implementation with explicit simultaneous-substitution conditions.
3. Both translations, alpha invariance, beta-correct lambda expansion, the
   exact root/applicative-context weak simulation, and explicit numerical
   representation through the transported beta equality.
4. Weak S–K confluence by parallel development, with all root cases and the
   normal-form consequence; the host counterexample to conversion beneath binders.
5. Explicit extensional equality, substitution stability, abstraction congruence,
   both conversion equivalences, and the combinatory round trip.
6. The four-case eta-optimized algorithm H, its exact application and beta-eta
   guarantee, the free-variable eta counterexample to beta-only equality, and
   failure when the freshness side condition is omitted.
7. Coefficient polynomials, all-assignment interpretation, both directions of
   S/K combinatory completeness, and extensional-algebra soundness.
8. Tree-size recurrences: 4s(P)+1 for one abstraction, 5^b(M)s(M) for compilation,
   10s(P) for expansion, single-abstraction tightness on all-x trees, and the
   precise marking/output construction cost. These are proved elementary bounds;
   neither a polynomial full-compilation bound nor a matching exponential lower
   bound was imported from an unselected source.

## Proof-driven distinctions retained in the final statements

The host B's whole-subtree K shortcut commutes literally with substitution under
the specified freshness conditions. The atom-by-atom A does not: substituting
u v for y in A_x(y) gives K(u v), while recomputing A_x(u v) gives
S(K u)(K v), for four distinct variables. The general A commutation result is
therefore extensional, with literal atomic renaming retained. The two outputs
are also different weak normal forms, by the proved confluence theorem.

Accordingly the root beta simulation always reaches substitution into the
compiled body. For B this is literal recompilation of the substituted lambda
body; for A the latter identification is extensional. Both lambda expansions
remain beta-correct. This keeps the atom/coefficients distinction visible rather
than treating an expanded I as an extra primitive constant.

The eta optimization returns f from abstraction of f x; this is beta-eta correct
but is not beta-equal to the unapplied lambda term lambda x.f x. Weak S–K equality,
transported lambda beta equality, beta-eta equality, and syntactic extensional
equality are all explicitly named. None is silently exchanged for another.

## Owned outputs and root integration

- `handbook/parts/p07/combinatory-abstraction.tex`
- `handbook/annex/p07/combinatory-abstraction.tex`
- `handbook/registry/calculi/p07-combinatory-abstraction.tex`
- `handbook/registry/symbols-intake-p07-combinatory-abstraction.csv`
- `handbook/bib/intake-p07-combinatory-abstraction.bib`
- This note.

The bibliography intake records reuse of the existing exact source key and adds
no duplicate identity. Symbol rows use actual TeX glyphs and supported literal
body-section, sheet/rule, or annex anchors. The size function s(P) is scoped
away from the algebra element s. Source-presentation annex scope extensions may
be added by the integrator; no whole-book alias or collision override is proposed.

The root owns routing, the old theorem/status, the old primitive sheet, and
canonical registry integration. Route the new body, annex, and auxiliary sheet.
The new annex includes `annex:p07.combinatory.bracket-abstraction`, with the
original `thm:p07-bracket-abstraction` as its back-reference. Set that original
theorem's status to `proved=annex:p07.combinatory.bracket-abstraction` when routing
the completed proof. The original theorem's citation/status was not edited here;
until root makes that change this intentional integration pair is not reciprocal.
The unchanged old statement's no-free-x/application-to-x assertion follows by
specializing `thm:p07-combinatory-substitution` to Q=x and D=B. Its translation
claim should link to `thm:p07-combinatory-translation`, retaining that theorem's
precise operational relation. The original Curry–Feys citation continues to
identify the outstanding historical source allocation and must not stand in
for the new proof's actual source identity.

No original shared theorem/status, driver, canonical registry, or original SK
rule sheet was edited. No new tests, independent reviews, builds, or manuscript
renders were run. A direct author read-through and the displayed mathematical
case calculations are authoring evidence, not independent acceptance.
