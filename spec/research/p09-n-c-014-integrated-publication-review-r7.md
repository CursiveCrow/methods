# N-c-014 integrated publication-text review — Round 7

## Review identity and scope

This is a fresh blind publication-text review of the integrated `N-c-014`
reader presentation.  The review concerns the actual LaTeX source and its
publication-facing mathematical exposition, not page layout.

The following evidence was read completely within the assigned scope:

- `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1884;
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--944;
- `spec/research/p09-buchi-1960-source-note.md`;
- `spec/research/p09-elgot-1961-source-note.md`;
- `spec/research/p09-trakhtenbrot-1961-source-note.md`;
- `spec/research/p09-rabin-1969-source-note.md`;
- `spec/research/p09-thomas-1996-report-source-note.md`;
- the `N-c-014` compact record in
  `spec/research/p09-source-presentations-lot2-3.md`, lines 681--745; and
- the relevant entries in `handbook/bib/handbook.bib`: `McNaughton1966`,
  `Thomas1996Report`, `Thomas1997`, `ComonEtAl2007`, `Elgot1961`,
  `Elgot1959Report`, `Elgot1962Errata`, `Meyer1975Complexity`, `Rabin1969`,
  `Trakhtenbrot1961`, `Trakhtenbrot1962Expanded`, `Buchi1959WeakReport`,
  `Buchi1960`, and `BruyereEtAl1994`.

The review tested definition-before-use, notation and type/standing discipline,
graduate-reference completeness, logical sequencing, ownership of source
claims and handbook emendations, citation and bibliography consistency, the
host seam, and the repository's technical-name rule.

## Prohibitions observed

No manuscript PDF, historical-source PDF, PNG, page image, render, or other
visual artifact was opened, inspected, rendered, or cited as manuscript
evidence.  No TeX or PDF build, test, harness, checker, repository script, hash,
or automated validation was run.  No separate prior `N-c-014` integrated
review, admission record, board ledger, chair transcript, or review-history
artifact was opened.  Status prose incidentally embedded in the mandated
source notes and compact bullets was not used as verdict evidence.  This
report makes no layout finding and no admission decision.

## Verdict

VERDICT: ACCEPT

The actual publication text is acceptable at the source-bounded strengths it
expressly claims.  I found no unresolved defect in definition-before-use,
notation, standing, logical sequence, graduate-reference completeness,
ownership, citations, bibliography, host consistency, or the technical-name
rule.

## Findings and evidence

### 1. Source and version ownership is explicit throughout

The presentation does not collapse distinct publications into a compound
folklore theorem.  It identifies the 1959 B\"uchi report as the reconstructed
precursor and leaves literal 1960 journal reconciliation open
(`n-c-014.tex` 8--16); makes Elgot's 1961 article controlling, the 1959 report
a precursor, and the 1962 errata controlling for corrected formulae
(234--239, 574--584); separates Trakhtenbrot's 1961 announcement from the 1962
expanded article, including their different official English titles
(586--596); limits the modern finite-word reconstruction to Thomas's May 1996
report (1008--1080); and identifies Rabin's 1969 article as controlling for the
original infinite-tree definitions and proof architecture (1082--1086).

The later Thomas game-theoretic route is introduced only after the Rabin
reconstruction and is expressly denied retrospective ownership of Rabin's
proof (1689--1693, 1879--1884).  The relevant bibliography entries preserve
the same identities, dates, page ranges, report numbers, DOI or repository
routes, and precursor/final-publication boundary.

### 2. Operative objects are defined before use and keep distinct standings

The B\"uchi section fixes the finite-set semantics of `W.2.A.`, then separately
defines the finite propositional automaton data, its time-indexed run, its
output, and its behavior (18--71).  Formula, finite-set assignment, run, output
predicate, and accepted behavior are not interchanged.  The terminal-marker
encoding is given pointwise before string behavior and the finite-word
equivalence are stated (144--171).

The Elgot section types the alphabet, state set, transition map, initial state,
accepting set, run, and language before using them (241--259).  It defines the
characteristic-column notation as an eliminable metalinguistic abbreviation,
then defines admissible words and `T_r(A)` (261--298).  The later acceptor and
transducer are kept separate (327--341, 357--370).  `A`-extendability and
strong `A`-extendability are defined before the finite descending construction
and its maximal language are used (386--448).  The arbitrary-set correction
defines the characteristic streams, bounded-window languages, relation fields,
prefix sets, tags, and the unary-window promotion before invoking the corrected
synthesis reduction (458--557).

The Trakhtenbrot section defines the formal system, its variable ranges and
primitive grammar, the controlled syntactic classes, and their separate
semantic dependence consequences before the normal-form theorem (598--647).
Anticipation, finite memory, weight, finite operator, and the normalized
`A`-operator terminology are distinguished before later realization results
(649--702).  Portions, tuple portions, homogeneity, bases, graphs, tails, and
residual stream maps are all typed before their theorem uses (704--756).
Relation-as-graph, solution, general solution, and fixed-lookahead solution
classes are defined in the order required by the synthesis statements
(854--912).  The finite-word maps, automaton-enumerability,
automaton-decidability, and special beginnings are likewise defined before the
corresponding theorems (914--989).

The Rabin section defines both tree orders, successors, predecessor, successor
structures, paths, valued subtrees, tables, automata, runs, the infinitely-often
operator, and ordinary acceptance before invoking closure or logical
translations (1088--1197).  It then types formula tracks before both
definability directions (1199--1293).  The finite tree, terminal-node frontier,
and frontieredness property appear before the worked principal-formula witness
(1245--1272).  Dual pair acceptance is defined before complementation
(1349--1397); marked trees and the exact no-infinite-descent condition on the
well-founded obligation mapping are introduced before their lemma uses
(1424--1465); the finite-tree automaton is fully typed before the lift and
compactness roles (1468--1522); and the distinct finite table-run is defined
before the emptiness base uses it (1587--1647).

The Thomas route similarly defines Muller runs, strict chain acceptance,
order-vector-with-hit memory, the language-preserving completion, game
positions, local strategy instructions, and regular generated trees before
their proof roles (1689--1856).

### 3. New technical names satisfy the repository rule

No hypothetical primitive is named in place of an owed construction.  Each
source-specific or handbook-specific name used materially has a local exact
definition, an identified standing, a stated distinction, and a later use.
Representative cases include:

- `W.2.A.` as an interpreted finite-set monadic language, not a calculus or an
  infinite-word system (18--29);
- Elgot's source-specific `open`, `A`-extendable, and strongly
  `A`-extendable language properties (371--390);
- Trakhtenbrot's typographic `\mathcal I`, normalized `A`-operator, tuple
  portion, basis, residual operator `T_u`, solution, and general solution
  (598--647, 678--693, 704--756, 866--912);
- Rabin's frontieredness as a property of a finite predecessor-closed set,
  explicitly nonredundant with predecessor closure and used by the finite-tree
  lift and emptiness base (1245--1260, 1468--1522);
- the dual sequence `\Omega`, its zero-length representative
  `\Omega^{\dagger}`, and the well-founded obligation mapping, each separated
  from ordinary path acceptance and tied to the complementation induction
  (1349--1465); and
- Thomas's order-vector with hit, completed chain automaton
  `\mathcal A^\bot`, game, memoryless strategy, and regular input tree
  (1728--1856).

The text repeatedly states whether an object is a formula, assignment,
predicate, language, relation, stream map, state datum, run, tree, automaton,
property, or metalinguistic abbreviation.  Those statements are used rather
than decorative: they prevent precisely the source conflations that the later
arguments would otherwise invite.

### 4. Logical sequencing supports graduate-reference use

The presentation proceeds from each original source's syntax and semantics to
its automaton or operator, translations, decision/synthesis argument,
limitations, and source-owned or handbook-owned corrections.  It then supplies
Thomas's modern finite-word proof as a separate locator, reconstructs Rabin's
original infinite-tree route, and only afterward presents Thomas's later
game-theoretic complement and regular-basis route.  This order makes
dependencies visible without presenting later machinery as an original-source
proof.

The treatment includes the theorem-strength boundaries a graduate reference
needs: both directions of the B\"uchi and Elgot correspondences; Elgot's
finite-set projection and design/undecidability boundary; Trakhtenbrot's
normal-form, topology, finite-realization, general-solution, conditionality,
and literal finite-word bridge; both directions of Rabin's logical
translation; the deterministic path product; the ordinary/dual acceptance
distinction; the marked-tree, well-foundedness, two-half-step, finite-tree, and
emptiness architecture; the Chapter II application boundary; and Thomas's
later completion, game, complement, emptiness, regular-tree, and `S2S` route.
The stated proof boundary at 1680--1687 is therefore a transparent compression,
not a substitute for the proof architecture.

### 5. Edge cases and handbook repairs are publication-ready

The exposition treats rather than suppresses the cases that determine whether
the stated constructions are actually total or equivalent.  These include the
B\"uchi finite-witness cutoff and empty-word marker (121--171); Elgot's empty
word, empty synthesis language, and unary-window case (256--257, 327--341,
539--552); Trakhtenbrot's empty closed homogeneous set and empty finite-word
language (821--837, 957--978); Rabin's empty pair sequence, empty `H`, empty
`U_0`, no-run branch, and distinction between frontier runs and finite table
runs (1399--1422, 1574--1647); and Thomas's empty chain plus completion of a
partial transition relation before game use (1728--1789, 1821--1829,
1847--1856).

Each departure from printed source text is explicitly owned.  The B\"uchi
analysis repair, Elgot unary-window completion, Trakhtenbrot counterexamples
and empty cases, Rabin zero-length and empty-witness completions, and Thomas
empty-chain and deadlock completions are all labelled handbook-owned at their
operative locations.  Published or later scholarly corrections are instead
attributed to their actual owners.  I found no silent emendation or source
strength inflation.

### 6. Host theorem and neighboring finite-tree material are consistent

The host's B\"uchi--Elgot--Trakhtenbrot theorem states the modern finite-word
equivalence and immediately says that this is a modern formulation rather than
verbatim common source wording (host 836--854).  Its source list and citations
match the integrated presentation's authority boundaries.  The host's `S2S`
theorem uses the same binary-tree carrier and successor functions as the later
Rabin/Thomas presentation (877--882 versus presentation 1858--1874).

The host defines finite ranked trees and bottom-up finite-tree automata before
inputting `n-c-014` (884--934, 940--943).  The presentation then explicitly
distinguishes Rabin's frontiered finite-tree automaton and infinite-tree run
from that host object (presentation 1468--1522).  The input order therefore
supports, rather than defeats, definition-before-use and nonconflation.

### 7. Citations and bibliography are internally consistent

Every material source block carries a nearby source locator.  The manuscript
uses report page locators only for the B\"uchi and Thomas precursor bodies,
uses the Elgot journal and errata for controlling publication claims, keeps the
two Trakhtenbrot bodies separately cited, uses Rabin for the original proof,
and uses Meyer only for the later complexity correction.  `McNaughton1966` is
identified as an external dependency of Rabin's product construction, not as a
reconstructed body.  The bibliography keys cited by the host and presentation
resolve to entries whose identities and version standings agree with the five
source notes and compact record.

## Must-fixes

None.

## Bounded acceptance and remaining open source work

This verdict accepts the actual integrated publication text at its expressly
bounded evidentiary strength.  It does not close the unreconciled 1960 B\"uchi
journal version, the unreconciled 1997 Thomas chapter, any broader source
register, layout, build, Part IX, the handbook, or publication.  Those open
source-version obligations are already stated in the presentation and do not
constitute a publication-text defect in the bounded claims reviewed here.

REGISTER STATUS: OPEN
