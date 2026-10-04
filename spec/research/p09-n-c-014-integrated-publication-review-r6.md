# N-c-014 integrated publication-text review — Round 6

## Review identity and scope

This is a fresh blind publication-text review of the current integrated
`N-c-014` LaTeX presentation.  The review addresses definition-before-use,
notation, exact standing, graduate-reference completeness, logical sequencing,
source and handbook ownership, citations, host consistency, and the local
technical-name rule.  It is not a source-facsimile review, a mathematical-source
reinspection, a typesetting review, or a page-layout review.

The verdict below is my independent judgment of the actual LaTeX text against
the permitted source notes and bibliography data.  Review or admission status
statements appearing incidentally in those notes were not used as evidence for
the verdict.

## Files and ranges read

I read the following permitted evidence:

1. `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1869, from the first
   source comment through the final Thomas report-precursor boundary, with no
   line omitted.
2. `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--944, including
   the finite-word theorem, the `S2S` theorem, the neighboring finite-ranked-tree
   definitions and theorem, and the four presentation inputs.
3. `spec/research/p09-buchi-1960-source-note.md`, lines 1--367.
4. `spec/research/p09-elgot-1961-source-note.md`, lines 1--423.
5. `spec/research/p09-trakhtenbrot-1961-source-note.md`, lines 1--583.
6. `spec/research/p09-rabin-1969-source-note.md`, lines 1--665.
7. `spec/research/p09-thomas-1996-report-source-note.md`, lines 1--353.
8. The compact `N-c-014` record only in
   `spec/research/p09-source-presentations-lot2-3.md`, lines 681--745.
9. The relevant entries in `handbook/bib/handbook.bib`: `McNaughton1966`,
   `Thomas1996Report`, `Thomas1997`, `ComonEtAl2007`, `Elgot1961`,
   `Elgot1959Report`, `Elgot1962Errata`, `Meyer1975Complexity`, `Rabin1969`,
   `Trakhtenbrot1961`, `Trakhtenbrot1962Expanded`, `Buchi1959WeakReport`,
   `Buchi1960`, and `BruyereEtAl1994`.

I did not open any earlier `N-c-014` review report, independent-review record,
admission record, board file, chair transcript, ledger, or history file.

## Prohibited actions not taken

- I did not open, inspect, render, build, or cite a manuscript PDF, PNG, page
  image, rendered page, or other manuscript-render artifact.
- I did not inspect any historical publication page or historical-source PDF;
  no ambiguity required going beyond the permitted notes.
- I did not run a TeX command, PDF command, build, test, test harness,
  automated checker, repository script, or hash computation.
- I did not treat visual inspection recorded by a source note as manuscript
  layout evidence.
- I did not call `list_agents`.
- I created no admission record and changed no manuscript, host, bibliography,
  source note, compact record, ledger, or prior report.

## Publication-text findings

### 1. Definition-before-use and exact standing

No must-fix was found.

The presentation consistently gives an object a type before relying on it and
keeps formulae, assignments, encodings, runs, automata, behaviors, languages,
relations, and metalinguistic abbreviations distinct.

- The B\"uchi presentation first fixes the finite-set meaning of a special
  predicate and the standing of `W.2.A.` (lines 18--29), then types the source's
  propositional data, recursion, output, special-output identity, and behavior
  (lines 31--71).  The local normal form precedes the synthesis and analysis
  claims (lines 73--108).  The handbook correction to the printed analysis
  formula is not merely asserted: the counterexample, replacement clauses,
  finite-witness argument, converse, and ownership statement are all supplied
  before downstream use (lines 109--142).
- The finite-word marker encoding precedes string behavior and Theorems 6--8
  (lines 144--171).  The arithmetic encoding precedes the false source claim,
  and both `\in_2` and `V_2` receive eliminable definitions before the corrected
  boundary is stated (lines 194--232).
- The Elgot presentation types the source acceptor before its run and behavior
  (lines 241--259), and types the finite-set assignment, characteristic column,
  admissible word, and language `T_r(A)` separately (lines 261--298).  The
  display `c_F(z)=a` is expressly classified as a metalinguistic abbreviation
  and expanded into the underlying language (lines 276--284).
- Elgot's `A/B` transducer is defined before finite behavior (lines 357--370).
  Extendability and strong extendability are defined before the finite
  fixed-point construction (lines 386--431).  The arbitrary-set language
  `T_d^\infty(C)`, window length, relation field, relation sequence, and prefix
  sets are all typed before the erratum repair and tagged projection use them
  (lines 458--557).
- The Trakhtenbrot presentation defines the standing and primitive grammar of
  `\mathcal I` before its syntactic classes (lines 598--647).  Operator,
  anticipation, finite memory, weight, finite operator, and the version-specific
  names for the zero-anticipation automaton class are separated before any
  theorem uses them (lines 649--703).
- Portions, tuple portions, homogeneity, basis, graph, tail, and residual
  operator are defined and typed before the printed degree claim is tested
  (lines 704--793).  The text explicitly distinguishes a residual stream
  operator from a state in the source's broader whole-future memory
  presentation (lines 753--756).
- The recurrent formula identifies the free predicate, bound state predicates,
  bound choice predicate, and quantifier-free matrix at the point of use
  (lines 800--837).  `Conditional \mathcal I`-algorithm, solution, general
  solution, the finite-word maps `T_t`, automaton-enumerability,
  automaton-decidability, and special beginning are each defined before their
  respective results depend on them (lines 845--976).
- The modern finite-word presentation types the automaton, finite-word
  structure, run, track predicates, singleton predicate, successor predicate,
  and `WS1S` domain independently (lines 995--1060).
- The Rabin presentation defines the two order symbols and predecessor before
  the successor structures (lines 1075--1124), then defines subtree, path,
  valued tree, transition table, automaton, infinite-occurrence set, run,
  ordinary acceptance, and accepted-language standing before the closure and
  translation theorems (lines 1126--1184).
- Principal formulae receive their exact syntactic family and construction role
  together (lines 1209--1230).  The finite tree, terminal-node frontier,
  frontieredness, finite valuation, and their nonredundancy are all stated
  before the worked witness uses them (lines 1232--1258).
- The path-language product is fully typed before its product transition and
  Muller family are used (lines 1281--1333).  The dual pair sequence, both path
  types, and the `forall run / exists path` dual language are defined before the
  complement argument (lines 1335--1383).  The empty pair sequence and its
  exact one-pair representative are then discharged before the source's
  positive-length induction (lines 1385--1451).
- Rabin's well-founded obligation mapping receives its exact no-infinite-descent
  definition, its standing, its ordinal characterization, and its later proof
  use at the same local introduction (lines 1422--1428).  The later finite
  table-run is likewise typed and distinguished from both infinite runs and
  external-frontier finite-tree-automaton runs before the emptiness base uses it
  (lines 1572--1587).
- In the Thomas tree presentation, the Muller automaton, direction-stream path,
  chain condition, empty-chain endpoint, order-vector-with-hit memory,
  rejecting completion, game positions, memoryless strategy, and regular tree
  generator are all defined before use (lines 1674--1841).

### 2. Local technical-name rule

No must-fix was found.

The presentation does not name a hypothetical answer.  Its technical names are
either source terms needed to report a source distinction or handbook-owned
abbreviations for constructions already given exact, eliminable definitions.
At their substantive first uses, the text supplies the required standing and
the distinction that makes each term nonredundant, and later exposition uses
the distinction.  Particularly strong examples are Elgot's admissibility and
strong extendability, Trakhtenbrot's residual operators versus broad memory
states, Rabin's frontieredness versus predecessor closure, the ordinary versus
dual acceptance data, the empty-sequence representative `\Omega^\dagger`, the
finite table-run, Thomas's order-vector-with-hit, and the completed chain tree
automaton `\mathcal A^\bot`.

The text also avoids creating names where a direct description suffices.  For
example, the B\"uchi and Elgot repair passages state local clauses and tagged
relations directly, and Rabin's marked-obligation summary describes the proof
objects without postulating a new automaton species.

### 3. Stable and disambiguated notation

No must-fix was found.

Notation is locally stable and deliberately disambiguated where the historical
sources collide.

- B\"uchi's propositional tuples `E,H,U`, time predicates `i,r,u`, and behavior
  `\beta(E,H,U)` retain distinct types.
- Elgot's input alphabets, internal states, accepting subsets, transducer output
  maps, finite-set columns, and language encodings are never conflated.  The
  source-specific use of "open" is defined as prefix closure.
- The letter `A` as an alphabet and the hyphenated `A`-operator name are
  expressly distinguished (lines 685--693), as are the announcement's Cyrillic
  label and the expansion's Latin normalization.
- The Trakhtenbrot tuple-portion definition makes concatenation and shifting
  coordinatewise, excluding an interleaving reading (lines 704--728).
- Rabin's source root `\Lambda` is retained, while Thomas's editorial
  `\epsilon` is confined to the later report route.  Rabin's initial-segment
  and lexicographic orders have explicit subscripts.  Ordinary acceptance uses
  `F \subseteq \mathcal P(S)`, while `\Omega=((L_i,U_i))` is reserved for the
  dual construction.
- The text distinguishes the finite-tree frontier value `f\notin S` from an
  ordinary state (lines 1468--1496), and distinguishes those finite runs from
  the host's bottom-up ranked-tree runs.
- Thomas's direction stream is expressly not Rabin's node-set path
  (lines 1692--1702), and the successor functions `S_i` are expressly unrelated
  to Rabin's earlier initial-state set `S_0` (lines 1843--1850).
- Reuse of conventional letters such as `Q`, `S`, `F`, `r`, and `\bot` occurs
  only after a new source subsection supplies their new types; no live scope
  leaves their standing ambiguous.

### 4. Logical sequencing and graduate-reference completeness

No must-fix was found.

The presentation has a coherent dependency order:

1. the three original finite-word predicate/automata packages are reconstructed
   separately;
2. Thomas's 1996 report supplies the modern finite-word proof architecture;
3. Rabin's own successor structures, translations, complementation, and
   emptiness proof are reconstructed at 1969 strength; and
4. Thomas's later game/complement/basis route is then presented as a separate
   post-1969 proof.

The exposition does not replace theorem statements by slogans.  It supplies
the operative maps, quantifier prefixes, finite constructions, edge cases, and
proof dependencies needed to follow each route.  In particular:

- B\"uchi's finite-witness repair, false-tail guard, inclusive decision bound,
  and false unary-powers equivalence are all exposed rather than smoothed over.
- Elgot's two directions, canonical truncation issue, maximal extendable
  sublanguage, finite-union erratum, general-arity tagging, and unary-window
  completion are present.
- Trakhtenbrot's syntactic/semantic distinction, whole-future memory, false
  graph-degree bound, empty-set recurrence case, conditional algorithm,
  solution/general-solution distinction, fixed-lookahead scope, and nonempty
  finite-word correction are all present.
- Rabin's ordinary/dual quantifier reversal, product construction, marked and
  well-founded obligations, two half-steps, positive-length induction,
  zero-length normalization, finite-tree dependencies, restricted tables, and
  both empty-witness repairs are all present.  The precise transfinite locus is
  stated without substituting it for the finite-state proof.
- Thomas's empty chain and partial-transition cases are completed before the
  game theorems, and the completion is proved language preserving before it is
  reused for complement, emptiness, formula translation, and `S2S`.

The explicit proof boundary at lines 1665--1672 is publication-appropriate: it
lists the reconstructed architecture and says exactly which article-level
transition tables and inductions remain in the cited complete source.  That is
a bounded reference boundary, not an unexplained omission.

### 5. Source strength and handbook ownership

No must-fix was found.

The text is unusually careful about authority:

- B\"uchi's 1959 report precursor is not passed off as the unreconciled 1960
  journal article (lines 8--16 and 987--989).
- Elgot's 1961 article controls, the 1959 report is a precursor, and the 1962
  errata owns the corrections (lines 234--239 and 574--584).
- Trakhtenbrot's 1961 announcement and 1962 expansion retain distinct titles,
  pagination, numbering, terminology, and strengths (lines 586--596 and
  685--693).
- Thomas's May 1996 report is consistently cited at report-precursor strength;
  the unreconciled 1997 chapter is expressly excluded (lines 995--1067 and
  1864--1869).
- Rabin's 1969 proof and Thomas's later game-theoretic route are never projected
  onto one another (lines 1520--1521, 1639--1642, 1674--1676, and 1864--1866).
- Every substantive repair is labelled handbook-owned at the point where its
  role matters, including B\"uchi's finite witness, Elgot's unary window,
  Trakhtenbrot's residual exactification and empty cases, Rabin's three edge
  completions, and Thomas's empty chain and rejecting completion.
- Rabin's printed elementary-recursive qualification is reported as historical
  and then withdrawn on the separately cited later lower-bound evidence; the
  decidability/effectiveness theorem is preserved.

No sentence silently upgrades a precursor, erratum, later survey, or
handbook-owned repair into an original-source claim.

### 6. Host consistency

No must-fix was found.

The host theorem at lines 836--854 states the modern finite-word equivalence and
immediately warns that it is not verbatim in each named source.  Its source map
matches the integrated presentation: B\"uchi's terminal-marker finite-set
encoding, Elgot's arithmetic/design package, and Trakhtenbrot's broader
predicate/operator/topology/synthesis package are all present at their actual
strengths.  The Thomas report supplies the modern effective finite-word route
without being substituted for the three originals.

The host `S2S` theorem at lines 877--882 matches both Rabin's decidability
conclusion and the later Thomas route.  The integrated presentation retains
Rabin's richer original structure and source notation while ending with the
same successor-only modern statement used by the host.

The neighboring finite-ranked-tree material at lines 884--934 does not collide
with the presentation.  The presentation explicitly distinguishes Rabin's
finite initial subtrees and external-frontier runs from bottom-up ranked-tree
automata (lines 1490--1496), and it separately warns that the weak finite-tree
base does not make the infinite input or full monadic theory weak
(lines 1639--1642).  The host input order at lines 940--943 is consistent with
the presentation's dependencies.

### 7. Citations and bibliography

No must-fix was found.

The citation keys used by the presentation and host have corresponding relevant
bibliography entries.  Their identities and page/version boundaries agree with
the permitted notes:

- `Buchi1959WeakReport` and `Buchi1960` keep precursor evidence and registered
  journal identity separate; `BruyereEtAl1994` owns the later arithmetic
  correction evidence.
- `Elgot1961`, `Elgot1959Report`, and `Elgot1962Errata` have distinct publication
  standings, and the journal page range is 21--51.
- `Trakhtenbrot1961` and `Trakhtenbrot1962Expanded` preserve the official
  Single-Place/One-Place English-title distinction and Russian-source notes.
- `Rabin1969`, `McNaughton1966`, and `Meyer1975Complexity` are cited for separate
  roles: original tree theory, the external deterministic word-automaton
  dependency, and the later complexity correction.
- `Thomas1996Report` identifies Bericht 9607 and records its precursor standing;
  the presentation does not use `Thomas1997` as evidence for unread final-body
  locators.
- The host's `ComonEtAl2007` entry identifies the online finite-tree monograph;
  that citation remains confined to the neighboring finite-ranked-tree theorem.

Source locators are attached near the claims they support.  Handbook-owned
counterexamples and completions are identified as such instead of receiving a
misleading original-source attribution.  No journal locator is assigned to a
claim verified only at report-precursor strength.

## Line-specific must-fixes

None.  I found no publication-text defect that requires a change to
`n-c-014.tex`, the reviewed host excerpt, or the relevant bibliography entries.

## Verdict

The actual LaTeX is definition-complete at the level claimed, notation is
stable across the five historically distinct presentations, every material
source/handbook boundary is explicit, the proof sequence is usable as a
graduate reference, the citations support the stated source strengths, and the
host accurately summarizes the integrated content.  No publication-text
must-fix remains within the reviewed scope.

VERDICT: ACCEPT

REGISTER STATUS: OPEN
