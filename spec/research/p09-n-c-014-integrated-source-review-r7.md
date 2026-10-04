# N-c-014 integrated source review — blind Round 7

## Verdict

VERDICT: ACCEPT

The actual LaTeX presentation is acceptable at its expressly bounded source strength.  It distinguishes each controlling source from its precursors, later corrections, and handbook-owned repairs; its mathematical and historical claims are supported by the permitted source notes; its locators point to the bodies actually used; and its unresolved Büchi-1960 and Thomas-1997 reconciliations remain open rather than being converted into false final-publication fidelity claims.

This verdict concerns the source-grounded content of `N-c-014` and its stated host integration only.  It is not a claim that either unreconciled final publication has been inspected, that a rendered handbook has been reviewed, or that the register may close.

## Evidence examined

I read the following permitted evidence directly and completely where the scope required complete reading:

- `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1884, from first line through EOF;
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--944;
- `spec/research/p09-buchi-1960-source-note.md`;
- `spec/research/p09-elgot-1961-source-note.md`;
- `spec/research/p09-trakhtenbrot-1961-source-note.md`;
- `spec/research/p09-rabin-1969-source-note.md`;
- `spec/research/p09-thomas-1996-report-source-note.md`;
- the compact `N-c-014` source-presentation block in `spec/research/p09-source-presentations-lot2-3.md`, lines 681--745; and
- the relevant entries in `handbook/bib/handbook.bib`: `Buchi1959WeakReport`, `Buchi1960`, `BruyereEtAl1994`, `Elgot1959Report`, `Elgot1961`, `Elgot1962Errata`, `Trakhtenbrot1961`, `Trakhtenbrot1962Expanded`, `Rabin1969`, `Meyer1975Complexity`, `McNaughton1966`, `Thomas1996Report`, and the adjacent host citation `ComonEtAl2007`.

The five source notes and the compact bullets were used as auxiliary source-control evidence, not as substitutes for reading the actual presentation.  Status or review-history prose embedded in those permitted notes was not used to decide this verdict.

## Prohibitions observed

- I did not open, inspect, render, build, or cite a handbook or manuscript PDF.
- I did not open or inspect any PDF page image, PNG, render directory, or other visual derivative.
- I did not run TeX, a PDF tool, a build, a test, a harness, a checker, a repository script, or a hash operation.
- I did not open a prior `N-c-014` review, admission record, board ledger, chair transcript, or other history artifact.
- I did not use a historical source page as manuscript-render evidence, and no note-unresolved mathematical ambiguity required opening a historical source body.
- I made no change to the presentation, host, source notes, compact record, bibliography, manuscript, or any prior report.

## Findings

### 1. Host statement and integration

The host theorem at `logic-in-computer-science.tex:836--854` states the modern finite-word MSO/regular-language equivalence and immediately limits the attribution: it says that the displayed sentence is a modern formulation, names the materially different Büchi, Elgot, and Trakhtenbrot source packages, and denies that the modern sentence occurs verbatim in every source.  The order-versus-successor equivalence is stated only for finite successor chains.  The cited-source metadata and prose include the acquired Büchi report precursor, the registered Büchi article identity, both Trakhtenbrot bodies, Elgot's article, and Thomas's report.

The host's `S2S` theorem at lines 877--882 is consistent with the later presentation: the binary successor structure is stated directly, while `n-c-014.tex:1115--1137` explains why Rabin's two displayed orders can be eliminated for finite branching.  Lines 884--934 separately define finite ranked-tree automata and explicitly deny their identification with Rabin's infinite-tree automata.  Lines 940--943 input `n-c-014` in the expected source-presentation sequence.  No host line overstates an open source reconciliation.

### 2. Büchi precursor strength, defects, and ownership

`n-c-014.tex:8--16` correctly identifies UMR1083 as the complete acquired September 1959 report precursor and states that wording, numbering, examples, proof detail, and page-for-page reconciliation with the registered 1960 article remain open.  All subsequent page locators for reconstructed mathematical content use `Buchi1959WeakReport`, not journal pages.

Lines 18--71 accurately separate the interpreted weak finite-set language, the propositional formula tuple `(E,H)`, its induced transit predicate, the output formula, and the behavior set.  The special-output identity is the pointwise source identity recorded in the source note, not the previously erroneous constant-state variant.  Lines 73--142 preserve the synthesis/analysis distinction, exhibit the defect in printed formula (2), give the finite-witness counterexample, and label the repaired local construction as a handbook-owned emendation.  The correction is not silently attributed to Büchi.

Lines 144--171 give the exact terminal-marker word encoding, including the empty word and the state at which output is read.  Lines 173--232 retain the false-tail guard and inclusive finite bound in the decision proof, distinguish the displayed last-true-point convention from the source's conflicting prose, reject the false unary-powers equivalence, identify the later `\in_2`/`V_2` correction as later scholarship, and preserve the one sound direction needed for the decidability consequence.  The locators agree with the permitted note: report pp. 2--8, 14--20, 18--25, 30--36, and 41--42, with Bruyère et al. pp. 202--203 for the later correction history.

The summary at lines 1000--1002 again limits the result to 1959-precursor strength.  The Büchi-1960 fidelity obligation is therefore honestly open and precisely bounded.

### 3. Elgot article, precursor, errata, and design results

`n-c-014.tex:234--239` assigns controlling publication authority to the complete 1961 article, precursor status to UMR1342, and correction authority to the published 1962 errata.  Lines 241--355 give the correctly typed source automaton, canonical admissible finite-set encoding, both effective directions of Theorem 5.3, the empty-word case, and the arithmetic consequences.  Formula, assignment, column word, run, automaton, and language retain distinct standings.

Lines 357--456 distinguish the later synchronous `A/B` transducer from the acceptor and reconstruct the finite-behavior, maximal-extension, synthesis, uniqueness, and infinite causal-behavior results at their proper source roles.  The explicit finite descending construction at lines 391--431 terminates over finite data and states both maximality directions; it introduces no speculative machine type.

Lines 458--557 state the exact restricted syntax used in section 8.6, apply the erratum's finite-union and disjoint-tag correction, and separately own the unary-window completion not printed by the erratum.  Lines 559--584 preserve the negative design boundary and the exact article/report/errata authority order.  The article locators (pp. 21--51), report comparison locators (pp. 4, 6, and 41), and errata locators (pp. 558--559) agree with the permitted note and bibliography.  No correction is silently selected from the precursor.

### 4. Trakhtenbrot's two Russian source bodies

`n-c-014.tex:586--618` keeps the 1961 announcement and 1962 expanded article distinct, including their different official English title renderings, locators, and theorem roles.  The editorial `\mathcal I` normalization is declared and given the standing of an interpreted formal language, not an automaton.  The grammar and arbitrary-predicate interpretation are defined before use and distinguished from Büchi's weak system.

Lines 620--702 define the syntactic controlled/lower/upper classes, their separate semantic dependence consequences, anticipation, whole-future finite memory, finite operators, weight, and the announcement-versus-expansion naming boundary for the automaton-realizable zero-anticipation class.  The source's conditional and nonrecursive boundaries remain visible.

Lines 704--843 define portions coordinatewise, state the convention difference between the two source bodies, type the handbook's residual stream operators, and give the handbook-owned counterexample to the printed weight/degree claim.  The standing and use of the residual maps are explicit: they are neither memory states nor a new automaton species, and they are used to identify the correct graph portions.  The nonempty covering restriction and empty-set recurrence case are also expressly handbook-owned.

Lines 845--912 preserve the conditional-algorithm qualification, the unequal strengths of finite realization and finite memory, the graph-contained-in-relation meaning of solution, both clauses of a general solution, and the fixed-lookahead scope of the extended theorem.  Lines 914--989 type the induced finite-word maps, expose and repair the empty-language edge case in the printed enumeration converse, and present the source's literal weak-predicate/special-beginning bridge without falsely quoting the modern finite-word theorem as the four-page announcement's wording.  Lines 991--1006 close with the explicit source-package and translation boundary.  The announcement and expansion locators match the permitted note.

### 5. Rabin's original tree-automata proof

`n-c-014.tex:1082--1188` accurately fixes Rabin's source notation, successor structures, ordinary tree automaton, arbitrary-root valued trees, global-run/universal-path acceptance, and Muller-family acceptance datum.  The later pair sequence is explicitly excluded from ordinary acceptance.  Rabin's historical elementary-recursive claim is reported but not retained; the later Meyer lower bound is attributed separately and leaves decidability and effectiveness intact.

Lines 1190--1293 give the exact closure dependencies, both logical translations, the deferred principal-formula route, a clearly owned worked instance, and the direct sentence-to-nonemptiness argument.  The finite rooted tree, terminal-node frontier, and `frontiered` property are defined at first use with standing, nonredundancy, and subsequent use.  In particular, predecessor closure is expressly insufficient.

Lines 1295--1466 correctly separate the deterministic Muller word-product dependency, ordinary acceptance, dual acceptance, the possibly vacuous no-run branch, and the two-half-step complementation architecture.  The empty-pair-list normalization is exact and expressly handbook-owned.  Rabin's well-founded obligation mapping is defined by the literal no-infinite-dependency-chain condition before its ordinal and automata uses; it is distinguished from path acceptance and simultaneous-run merging.

Lines 1468--1657 keep three finite-run notions distinct, give the source finite-tree automaton with its external frontier value, and reconstruct Rabin's actual one-letter/dual-language/weak-finite-tree emptiness proof.  The two printed nonempty-witness omissions and the zero-length omission are identified, repaired, and owned by the handbook.  The external finite-tree decision theorem is kept at the base of Rabin's proof and is not used to turn `S2S` into weak logic or to import Thomas's later regular-tree basis route.

Lines 1659--1687 account for the source's application chapter and state the reconstruction boundary without claiming to reproduce every transition table or induction in the article.  The Rabin locators and bibliography identity agree with the permitted source note.

### 6. Thomas's later report route and open final-chapter reconciliation

`n-c-014.tex:1008--1080` attributes the finite-word proof only to the May 1996 report, gives the exact Section 3.1 structures, formula tracks, empty-word guard, converse atomic automata, `WS1S` distinction, and Presburger route, and refuses to substitute that proof for the three historical finite-word presentations.

Lines 1689--1877 likewise mark Sections 6.1--6.3 as a later game-theoretic route rather than Rabin's original proof.  The Muller automaton, path stream, strict chain, order-vector-with-hit memory, game, local instruction, regular generated tree, and MSO translations are each given their relevant standing.  The empty-chain endpoint and the partial-transition deadlock repair are explicitly handbook-owned.  The completion `\mathcal A^\bot` is introduced only after its necessity is stated, is fully typed, is distinguished from a game and run, is proved language-preserving, and is then used exactly where the game hypotheses require it.

Lines 1879--1884 finally state that the registered 1997 chapter was not used as a source body and that every Thomas locator belongs to the 1996 report precursor.  This matches `Thomas1996Report` in the bibliography and leaves final-chapter reconciliation open without weakening the report-level reconstruction.

### 7. Technical-name rule

No speculative technical name is introduced in place of an owed artifact.  Source terms are defined before substantive use, and the presentation's own notation is introduced only where a distinction is needed.  Representative high-risk cases satisfy all five requirements locally:

- `\mathcal I` (`n-c-014.tex:598--618`) is necessary to render the source's Cyrillic system name, is defined by grammar and interpretation, is identified as a formal language, is distinguished from automata and Büchi's weak system, and is used throughout the Trakhtenbrot reconstruction.
- Residual stream operators `T_u` (lines 730--756) are typed and defined, distinguished from broad memory states, and required for the corrected graph-portion statement.
- Rabin's `frontiered` property (lines 1245--1260) is defined exactly, identified as a property of a finite predecessor-closed set, distinguished from predecessor closure, and used in the worked lift and later finite-tree arguments.
- Rabin's well-founded obligation mapping (lines 1436--1442) is defined by exclusion of an infinite dependency chain, identified as a condition on obligations, distinguished from path acceptance, and used in Lemmas 3.3, 3.4, and 3.11.
- `\Omega^\dagger` (lines 1399--1422), the finite table-run rooted at a state (lines 1587--1602), and `\mathcal A^\bot` (lines 1755--1784) each have an explicit necessity, definition, standing, nonredundancy explanation, and later proof use at their introduction.

The editorial relation subscripts, renamed Thomas letter predicates, and source-version terminology normalizations are also declared rather than silently projected onto a source.

### 8. Bibliography and locator integrity

The relevant bibliography entries identify the bodies at exactly the strength claimed in the presentation: Büchi's 1959 report is separate from the 1960 journal article; Elgot's 1961 article, 1959 report, and 1962 errata are separate entries; the two Trakhtenbrot publications retain their distinct official English titles and Russian-source notes; Rabin and Meyer are separate original/later-correction authorities; and Thomas's May 1996 report has its own entry and precursor note rather than being cited as the 1997 chapter.  Elgot's page range is 21--51, Rabin's is 1--35, and the cited report and errata locators agree with the source notes.

No presentation locator is assigned to an unread final publication.  No bibliography entry is used to erase the report/article, announcement/expansion, original/later-route, or source/handbook-correction boundary.

## Must-fix findings

None.

## Bounded open obligations

The following are genuine source obligations, but they are already stated accurately in the LaTeX and therefore are not defects in this bounded presentation:

1. Acquire a lawful complete body of Büchi's registered 1960 journal article or the 1990 reprint and reconcile it page by page with UMR1083 before assigning journal-text fidelity or journal locators.
2. Acquire the registered Thomas 1997 chapter body and reconcile every relied-on definition, result, example, proof move, section locator, and modification with the May 1996 report before assigning final-chapter strength.

Those obligations prevent register closure; they do not require the accepted precursor-level text to pretend that unavailable evidence has already been read.

REGISTER STATUS: OPEN
