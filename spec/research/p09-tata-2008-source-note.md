# TATA 2008 source custody and reconstruction note

## Status

The complete 18 November 2008 release of *Tree Automata Techniques and
Applications* is acquired from the official HAL deposit, visually inspected at
the pages controlling the Part IX finite-tree presentation, and integrated into
`handbook/parts/p09/presentations/n-c-015.tex`.

Three fresh Round 4 seats unanimously accepted the frozen nine-object snapshot
for `N-c-015.b` manuscript content. The [decision ledger and chair
reconciliation](boards/p09-tata-2008/) and [independent review
record](p09-tata-2008-independent-review-record.md) preserve the exact hashes
and four-round history. That narrow source-specific admission does not admit
`N-c-015.a`; the later [integrated direct-LaTeX review
record](p09-n-c-015-integrated-independent-review-record.md) admits the
source-bounded `N-c-015` reader content while leaving the Thatcher--Wright body
open. Neither admission covers Part IX, a build, a rendered handbook, human or
user review, the book, or publication. No manuscript build, test, test harness,
checker, or repository script was run as part of this source audit or review.

## Identity and custody

- Authors: Hubert Comon, Max Dauchet, Rémi Gilleron, Florent Jacquemard,
  Denis Lugiez, Christof Löding, Sophie Tison, and Marc Tommasi.
- Title: *Tree Automata Techniques and Applications*.
- Internal release date: `TATA — November 18, 2008 —`, printed in the footer.
- HAL record: <https://inria.hal.science/hal-03367725>.
- Official deposited PDF:
  <https://inria.hal.science/hal-03367725/file/tata.pdf>.
- HAL cover: cites the work as 262 pages, 2008, HAL id `hal-03367725`, and
  records submission on 6 October 2021.
- Local file: `tmp/pdfs/p09-tata-2008/tata-2008.pdf`.
- Local length: 2,292,046 bytes; 263 physical PDF pages, consisting of the
  added HAL cover and the 262-page monograph object.
- SHA-256:
  `3EB9C3F9A1A9A3BD45EC1E50BD50A1C10010789B542A2818F030A7246F9B5B22`.

The HAL cover establishes an authorized public deposit, not a blanket licence
to republish the PDF pages or protected expression. No Creative Commons licence
was observed in the inspected object. The local PDF and page renders are
research evidence, not handbook assets.

## Physical-to-printed page map and visual inspection

Physical PDF page 1 is the added HAL cover and physical page 2 is the internal
title page. For the relevant numbered body, physical PDF page `n + 1` is printed
page `n`. The following physical pages were rendered and visually inspected at
original detail:

- 1--2: HAL custody cover and internal title;
- 12--14: printed introduction pp. 11--13;
- 20--28: printed chapter-opening and §1.1 pp. 19--27;
- 31: printed p. 30, Theorem 1.3.1 and its first constructions;
- 41: printed p. 40, Theorem 1.7.4 and its proof;
- 44: printed p. 43, Exercise 1.4;
- 88--97: printed pp. 87--96, the complete §3.3 passage controlling the WSkS
  reconstruction and its finite/infinite boundary.

The corresponding render sets are
`tmp/pdfs/p09-tata-2008/core-rendered/` and
`tmp/pdfs/p09-tata-2008/relevant-rendered/`. Text extraction was used only as a
reading aid; the PDF pages control.

## Exact source findings

### Finite bottom-up automata

Printed pp. 20--22 define a nondeterministic finite tree automaton as
`A = (Q,F,Q_f,Delta)`, give the ranked transition form and its ground shorthand,
define bottom-up runs as maps from positions to states, and require a final
state at the root. The reader's finite-run example is explicitly a handbook
example, not a source quotation.

- Theorem 1.1.9, printed pp. 25--27, gives effective subset determinization.
- Theorem 1.3.1, printed p. 30, gives effective closure under union,
  complementation, and intersection.
- Theorem 1.7.4, printed p. 40, gives linear-time emptiness. Its proof reduces
  nonemptiness to the existence of an accessible final state and explains the
  linear least-fixed-point/Horn formulation.
- Exercise 1.4, printed p. 43, fixes the ranked alphabet with one nullary
  symbol `a` and one binary symbol `f`, then asks the reader to prove that
  `{f(t,t) | t in T(F)}` is not recognizable. The handbook now supplies the
  short deterministic-state separation proof, including the required reason
  every term reaches a state, rather than presenting the exercise as if TATA
  had printed a proof or dropping the source's alphabet hypothesis.

### WSkS and finite encodings

Printed pp. 87--90 define WSkS over `{1,...,k}*`, with first-order variables
ranging over words and set variables ranging over finite sets of words.
Proposition 3.3.1 translates first-order variables into singleton set variables
and reduces to the exact atomic forms `X subseteq Y`, `Sing(X)`, `X = Yi`, and
`X = epsilon`.

Definition 3.3.2 and Example 3.3.3, printed pp. 90--91, encode a tuple of finite
sets as a finite tree over `{0,1,bottom}^n`. The manuscript now works through
the source's example
`S_1 = {epsilon,11}, S_2 = empty, S_3 = {11,22}` and identifies the source
labels at the root, the two first-level positions, the two occupied second-level
positions, and all remaining nullary bottom-padding positions.

The manuscript now also makes explicit the bridge to the main finite-tree MSO
theorem: the finite position set and its symbol-label subsets code one ground
term; the label and child atoms become membership in the appropriate label
set and the corresponding successor equation; element quantifiers are
restricted to that position set and monadic quantifiers to its subsets; in the
converse direction the state-position sets of Lemma 3.3.6 partition exactly
the same finite domain. The ambient prefix tree is therefore the coding
structure, not an infinite input to the automaton.

Lemma 3.3.4 begins on printed p. 91 and continues through p. 93. It constructs
an automaton for each restricted formula. Figure 3.9's complete one-state
transition list for `X subseteq Y` has been transcribed into the manuscript.
For disjunction, the induction adds unconstrained coordinates for variables
missing from either disjunct and then takes union. It uses complement for
negation and projection for existential set quantification.

Lemma 3.3.6, printed pp. 94--95, gives the converse. It existentially quantifies
one position set per state, requires a partition and a final root label, and
uses the displayed local transition clause to describe a successful run. The
manuscript includes that clause.

Theorem 3.3.7 is printed on p. 95, but TATA immediately calls it a slogan that
is "not very precise" and says the precise statements are the two lemmas. The
manuscript now preserves that qualification.

Theorem 3.3.8, also on printed p. 95, derives WSkS decidability. For a formula
with no free variables, the source says the alphabet is empty or, under its
explicit convention, contains the sole constant `top`; validity is equivalent to
the presence of a transition `top -> q_f` for some final state. The former
manuscript phrase "sole all-zero track encoding" was not the source's closed
sentence reduction and has been corrected.

Printed pp. 95--96 distinguish the finite-set WSkS construction from the
logic obtained when set variables range over arbitrary, possibly infinite,
subsets of the successor tree, which TATA calls full SkS. TATA says that logic
requires automata assigning states from the root downward on infinite inputs
and a different complementation argument, and sends the reader to Thomas
rather than presenting infinite-tree automata itself.

## Manuscript reconciliation

The integrated reader object is
`handbook/parts/p09/presentations/n-c-015.tex`, 9,443 bytes, SHA-256
`69AC3973E247EF090D9C78E92991BCEEDB30C0145CC276DC2C45F85DE984B4AD`.
The previously suspected source-numbering defect is resolved: 3.3.4 and 3.3.6
are both subsection numbers and actual lemma numbers, while 3.3.7 and 3.3.8
are both subsection numbers and actual theorem numbers on the same printed
page. No numbering repair was required.

The two reconciliations deferred while the Rabin Round 1 snapshot was frozen
are now complete:

1. `handbook/bib/handbook.bib` preserves the stable key `ComonEtAl2007` but now
   gives 2008 as the year and 18 November 2008 as the release date of the
   inspected object.
2. `spec/research/p09-source-presentations-lot2-3.md` now gives the source's
   title-page author order, empty-alphabet/single-constant `top` reduction,
   exact restricted syntax, explicit restriction of monadic quantifiers to the
   finite encoded tree, worked encoding, inclusion automaton, local
   accepting-run clause, exact alphabet hypothesis for Exercise 1.4, and
   TATA's qualification of Theorem 3.3.7.

The registered 2007 date may continue to identify the evolving TATA work in the
source register, but it must not be presented as the date of the fixed PDF that
controls this reconstruction.

After Rabin Round 5 closed, the compact record was reconciled to the reader's
post-freeze refinements. It now gives the literal source-to-handbook symbol
map and tuple order; defines determinism as uniqueness of the target for a
symbol/child-state tuple; records the same-language, reachable-subset content
of Theorem 1.1.9; states the final-state criterion in the emptiness marking
construction; spells out the label and child-atom translations in the
finite-tree MSO bridge; replaces the former padding shorthand by the exact
nullary bottom-padding description; supplies the reachability premise in the
Exercise 1.4 proof; and distinguishes finite-set WSkS from full SkS over
arbitrary, possibly infinite, subsets and its root-down infinite-input
automata. The Thatcher--Wright paragraph now reports “finite algebras” only
as abstract language and leaves every body-dependent definition open. The
reader now closes with an explicit reconstruction boundary: it describes an
operative constructive outline at the strength actually reproduced, not every
proof or transition table printed for the cited theorems, and identifies its
small run and Exercise 1.4 proof as handbook-owned.

A later source preflight found that the compact record's displayed TATA tuple
had accidentally omitted the ranked-alphabet component even though this note
and the reader had it correctly. Because the shared compact file was then
frozen for Rabin Round 6, the omission was recorded and left untouched until
that round closed. It is now corrected to the literal source tuple
`A=(Q,F,Q_f,Delta)`. No TATA review was open during either the discovery or the
repair. The records were reconciled before Round 4 froze. Three independent
Round 4 seats then accepted the unchanged snapshot, and `N-c-015.b` manuscript
content is admitted at the narrow scope recorded above.

## Thatcher--Wright boundary

TATA cites Thatcher--Wright 1968 for Theorem 3.3.8, but this later monograph is
not a substitute for the registered article's missing technical body. The
same-title IBM Research Paper RC-1713 (1966) remains an acquisition lead only.
Until either the report or the article body is acquired, the paper's exact
finite-algebra definition, recognizability relation, algebraic signature,
input domain and coding, closure and generalized Kleene results, precise
second-order language and variable ranges, source-controlled examples, and
proof boundary remain open. No technical name or modern ranked-tree structure
is assigned to the missing construction before that evidence is inspected.
