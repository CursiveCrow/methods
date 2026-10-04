# N-c-014 integrated source-fidelity review — Round 6

## Review question and disposition

I reviewed the current actual LaTeX source for the integrated `N-c-014`
presentation against the permitted source records, with particular attention to
source claims, attribution, locators, ownership of corrections and
exactifications, publication-version boundaries, register language, and the
local `AGENTS.md` rule for technical names.

The presentation is source-faithful at the explicitly stated strengths.  I
found no source-fidelity must-fix in the presentation or in its host
integration.  In particular, the text does not collapse the four original
source presentations into the modern compound theorem, does not project
Thomas's later proof backward onto Rabin, and does not promote either an
unreconciled precursor to final-publication strength.

## Files and passages read

I read the following permitted evidence:

- `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1869, from line 1
  through EOF;
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--944;
- `spec/research/p09-buchi-1960-source-note.md`, through EOF;
- `spec/research/p09-elgot-1961-source-note.md`, through EOF;
- `spec/research/p09-trakhtenbrot-1961-source-note.md`, through EOF;
- `spec/research/p09-rabin-1969-source-note.md`, through EOF;
- `spec/research/p09-thomas-1996-report-source-note.md`, through EOF;
- the compact `N-c-014` record in
  `spec/research/p09-source-presentations-lot2-3.md`, lines 681--745; and
- the relevant entries in `handbook/bib/handbook.bib`:
  `Buchi1959WeakReport`, `Buchi1960`, `BruyereEtAl1994`, `Elgot1959Report`,
  `Elgot1961`, `Elgot1962Errata`, `Trakhtenbrot1961`,
  `Trakhtenbrot1962Expanded`, `Rabin1969`, `Meyer1975Complexity`,
  `McNaughton1966`, `Thomas1996Report`, `Thomas1997`, `Buchi1962`, and
  `ComonEtAl2007`.

The adjacent host material at lines 856--934 was read to check the integration
boundary: it keeps the infinite-word, infinite-tree, and finite-ranked-tree
objects separate from `N-c-014`.  This review does not re-adjudicate the
separate `N-c-013` or `N-c-015` source presentations.

## Prohibited actions not taken

- I did not open, inspect, render, build, or cite any manuscript PDF, source
  PDF, PNG, page image, contact sheet, or other render.
- I did not run TeX, a PDF build, tests, a test harness, an automated checker,
  a repository script, or a hash computation.
- I did not open or rely on any separate earlier `N-c-014` review, admission,
  board, ledger, or history file.
- I did not create an admission record.
- I did not edit the manuscript, host, compact record, source notes,
  bibliography, ledger, or any prior report.

## Detailed findings

### 1. Host theorem and integration boundary

Host lines 836--854 state the modern finite-word MSO/regular-language
equivalence and immediately delimit its historical standing.  Lines 846--853
say expressly that the displayed sentence is a modern formulation, summarize
the materially different Büchi, Elgot, and Trakhtenbrot source packages, and
deny that the sentence occurs verbatim in each source.  That is the necessary
qualification for the compound theorem title.  The cited source set matches
the bounded source basis, including `Thomas1996Report` rather than an
uninspected final chapter.

Host lines 877--882 state Rabin's binary-tree decision theorem without
importing the later Thomas proof.  Host lines 884--934 separately define finite
ranked trees and bottom-up tree automata and explicitly deny their identity
with Rabin's infinite-tree automata.  The `N-c-014` input at host line 942 is
therefore integrated between, but not conflated with, its neighboring
presentations.

### 2. Büchi presentation

Presentation lines 8--16 correctly separate the registered 1960 journal
identity from the complete September 1959 UMR1083 precursor and say exactly
what remains unreconciled.  The report, not the unread journal body, controls
the page and theorem locators used in the reconstruction.

Lines 18--71 preserve the source's interpreted weak second-order language,
finite-set meaning of “special predicate,” propositional-formula automaton,
typed transit recursion, pointwise special-output identity, and eventual-truth
behavior.  Formula data, input predicates, runs, outputs, and behavior sets are
kept at distinct standings.

Lines 73--142 accurately distinguish synthesis from analysis.  They expose the
printed Theorem 2 witness defect, give the supported one-bit counterexample,
state a sufficient finite-witness correction, prove both directions of that
correction, and label it a handbook-owned emendation.  The source is not
silently strengthened.

Lines 144--171 reproduce the report's terminal-marker finite-word encoding and
the endpoint at which string behavior is read.  Lines 173--232 retain the
false-tail guard and inclusive finite search in the decision argument,
identify the report's free-individual length inconsistency, and separate the
sound finite-word correspondence from the false unary-powers equivalence.
The later `\in_2`/`V_2` correction is attributed to later scholarship rather
than to Büchi's report.  Lines 987--989 restate, without overclaim, that literal
1960 journal reconciliation remains separate.

### 3. Elgot presentation

Lines 234--239 and 574--584 give the correct authority order: the complete 1961
journal article controls, the complete UMR1342 report is a distinct precursor,
and the published 1962 errata owns the corrections.  The comparison facts about
the two report occurrences of the projection symbol, the reversed pair, and
the false single-relation claim agree with the source record and are not used
to blur the versions.

Lines 241--355 correctly type the source acceptor, finite-set language,
canonical admissible encoding, and both directions of Theorem 5.3.  In
particular, existential set projection includes the required right truncation,
and the reverse construction supplies start, terminal, and local-transition
formulae rather than being inferred from the compound theorem name.

Lines 357--456 separately define the `A/B` transducer, finite behavior,
extendability conditions, the effective finite descending construction of the
largest strongly extendable sublanguage, and the exact synthesis and uniqueness
consequences.  The infinite-behavior result is correctly identified as causal
synchronous behavior, not Büchi acceptance.

Lines 458--557 preserve the literal restrictions on the arbitrary-set
specification and use the erratum's finite union rather than the false printed
single-relation sentence.  The general-arity tagging is typed, and the
`n=1` promotion is explicitly identified as a handbook completion rather than
erratum wording.  Lines 559--572 then give the separate undecidability boundary
at the source's exact strength.  I found no locator, attribution, or ownership
mismatch in this section.

### 4. Trakhtenbrot presentation

Lines 586--647 keep the 1961 announcement and 1962 expansion distinct,
preserve the two official English title renderings, define the typographic
normalization `\mathcal I`, and state the primitive grammar, interpretation,
controlled formula classes, and semantic dependence consequences at their
recorded strengths.

Lines 649--702 distinguish anticipation, finite memory, finite operator,
weight, and the zero-anticipation automaton-realizable class.  They explicitly
record the announcement's Cyrillic class letter and the expansion's Latin
`A`, so the normalized terminology is not projected backward without notice.

Lines 704--843 define portions coordinatewise, state which portion convention
the handbook adopts, define the residual maps before naming their standing,
and explain why they are not broad memory states.  The counterexample to the
printed weight/degree bound is fully typed and expressly handbook-owned.  The
nonempty covering restriction and the empty-set recurrence are likewise owned
by the handbook, while the source's valid closedness and definability claims
remain intact.

Lines 845--912 preserve the unequal strengths of the continuous finite-
realization result and the noncontinuous finite-memory result; distinguish a
solution from a graph defined exactly by a formula; define the two-clause
general-solution standing; retain the conditional-algorithm qualification; and
state the fixed-lookahead extension one bound at a time.  Lines 914--985 then
type the finite-word maps, distinguish enumeration from decision, expose and
repair the empty-language edge case, and state the exact special-beginning
bridge.  Lines 991--993 make no complete-translation claim.  No
Russian-language-specialist certification is asserted.

### 5. Thomas finite-word precursor presentation

Lines 995--1067 use only the May 1996 report at explicit precursor strength.
They type the finite-word automaton and word structure, preserve the empty-word
guard in the automaton-to-formula direction, define the singleton-set atomic
predicates used in the converse, and distinguish finite word structures from
`WS1S` over the natural numbers.  The final paragraph says exactly that this
closes the 1996-report locator only; it neither replaces the original source
presentations nor claims reconciliation with the registered 1997 chapter.

### 6. Rabin presentation

Lines 1069--1184 preserve Rabin's notation and source standings: the two order
symbols are editorially disambiguated rather than replaced, the successor
structures retain their orders, ordinary automata use a family
`F \subseteq \mathcal P(S)`, and acceptance has the essential
`\exists r\,\forall\pi` order.  The later Meyer result is used only to reject
Rabin's historical elementary-recursive complexity qualification; decidability
and effectiveness are left intact.

Lines 1186--1279 type the formula-track encoding and both logical directions.
The worked principal-formula example is labelled handbook-worked rather than
source-printed.  The finite tree, terminal-node frontier, and `frontiered`
property are defined before their substantive use, their standings and
nonredundancy are stated, and their later lift role is identified.  The closed-
sentence proof is correctly reduced directly to source emptiness, with no
regular-tree basis step attributed to Rabin.

Lines 1281--1452 reproduce the deterministic word-product dependency and keep
ordinary and dual acceptance separate.  The dual pair sequence, its two path
types, the quantifier reversal, the possible vacuity, and the zero-length
normalization are exact and typed.  The normalization is expressly a
handbook-owned representation of the omitted base case, not a new ordinary
acceptance condition.  The marked-tree, simultaneous-run, well-foundedness,
two-half-step, and induction architecture is retained, and the exact
transfinite locus is stated without replacing the finite-state proof by a
slogan.

Lines 1454--1642 distinguish Rabin's external-frontier finite-tree automaton
from the finite restrictions of current one-letter table runs used in the
emptiness base.  The actual one-letter, complement, dual-language, and weak-
finite-tree-theory reduction is reconstructed.  The empty `H` and empty `U_0`
branches and the zero-pair normalization are individually proved and labelled
as handbook repairs.  Lines 1644--1672 map the application chapter and state
the proof boundary without claiming to reproduce the complete fourteen-page
complementation development.  I found no Rabin/Thomas route conflation.

### 7. Thomas infinite-tree precursor presentation

Lines 1674--1738 expressly identify the game-theoretic construction as a later
Thomas route.  They type the Muller tree automaton, global run, path condition,
strict chain, empty-chain endpoint, and order-vector-with-hit memory, while
distinguishing all of those objects from Rabin's earlier path-set presentation.

Lines 1740--1814 identify the source's missing game premise, define the
rejecting-state completion, prove language preservation, and label the
completion handbook-owned.  The game positions, moves, strategies, instruction
labels, complement construction, determinacy proof role, and empty-chain base
are all given after their operative objects are defined.

Lines 1816--1862 define a regular input tree as a generated-tree property,
derive the later emptiness/basis route, and state the MSO correspondence at
1996-report strength.  Lines 1864--1869 then deny every backward attribution to
Rabin and explicitly leave the registered 1997 chapter outside the source
basis.  The bibliography also keeps `Thomas1996Report` and `Thomas1997` as
separate entries.

### 8. Technical names, ownership, bibliography, and register bounds

Every locally introduced technical name needed by `N-c-014` is accompanied at
its operative introduction by an exact definition or explicit source
normalization, a clear standing, a distinction from nearby objects, and a later
use.  The most vulnerable names and distinctions are handled expressly:
special output and string behavior; admissible encodings; strong
extendability; Trakhtenbrot's two operator-class letters, portions, residual
operators, and general solutions; Rabin's frontier, `frontiered` property,
ordinary versus dual acceptance, well-founded obligation mapping, and finite
table-run; and Thomas's order-vector-with-hit, rejecting completion, game, and
regular generated tree.  I found no violation of the supplied local
technical-name rule.

The bibliography identities and page ranges agree with the permitted source
records.  In particular, Büchi's report and journal, Elgot's article/report/
errata, the two Trakhtenbrot publications, Rabin and Meyer, and Thomas's report
and final chapter remain separate entries.  Citations in the presentation use
report locators only for report-controlled claims and do not present either
open reconciliation as complete.

The remaining Büchi 1960 journal comparison and Thomas 1997 chapter comparison
are genuine register obligations, but they are honestly bounded throughout the
LaTeX.  They do not create a source-fidelity must-fix in this precursor-bounded
presentation and they prevent the source register from closing.

## Must-fixes

None.  I found no source-fidelity change required in
`handbook/parts/p09/presentations/n-c-014.tex` lines 1--1869 or in its host
integration at `handbook/parts/p09/logic-in-computer-science.tex` lines
836--944.

VERDICT: ACCEPT

REGISTER STATUS: OPEN
