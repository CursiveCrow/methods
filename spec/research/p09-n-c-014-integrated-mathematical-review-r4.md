# N-c-014 integrated mathematical and definedness review — blind Round 4

VERDICT: REJECT

## Review scope

This is a mathematical-correctness, completeness, and definedness review of the unchanged reader-facing LaTeX at its expressly bounded source strengths.  It is not an admission record, a source-fidelity certification for an unavailable final publication, a typesetting review, or a claim about any rendered handbook.

I read the following permitted objects:

- `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1852, from the first line through EOF;
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--941;
- `spec/research/p09-buchi-1960-source-note.md`, lines 1--367;
- `spec/research/p09-elgot-1961-source-note.md`, lines 1--423;
- `spec/research/p09-trakhtenbrot-1961-source-note.md`, lines 1--583;
- `spec/research/p09-rabin-1969-source-note.md`, lines 1--665;
- `spec/research/p09-thomas-1996-report-source-note.md`, lines 1--353;
- the compact `N-c-014` source bullets in `spec/research/p09-source-presentations-lot2-3.md`, lines 681--745, and the relevant open-source bullets at lines 967--980; and
- the relevant entries in `handbook/bib/handbook.bib`: `McNaughton1966`, `Thomas1996Report`, `Elgot1961`, `Elgot1959Report`, `Elgot1962Errata`, `Meyer1975Complexity`, `Rabin1969`, `Trakhtenbrot1961`, `Trakhtenbrot1962Expanded`, `Buchi1959WeakReport`, `Buchi1960`, and `BruyereEtAl1994`.

I applied the supplied local `AGENTS.md` rule to every technical name introduced or normalized in the presentation: necessity, exact definition or stated axiomatic standing, object standing, nonredundancy, and actual later use were all part of the review.

## Prohibited actions not taken

I did not open, inspect, render, build, or cite a manuscript PDF, a historical-source PDF, a PNG, a page image, or any other render.  No concrete source ambiguity required consultation of a historical source page.  I did not run TeX, a PDF build, a manuscript build, a test, a test harness, an automated checker, a repository script, or a hash command.  I did not call `list_agents`.  I did not open any earlier N-c-014 review, admission, board, ledger, transcript, independent-review record, or review-history file.

## Must-fix findings

### 1. The completed Thomas game is not closed under its declared position space

At `n-c-014.tex` lines 1732--1740 the handbook correctly enlarges the state set to

\[
Q^\bot=Q\cup\{\bot\}
\]

and adds transitions whose two successors are the new state \(\bot\).  Lines 1745--1751 then correctly use paths that become constantly \(\bot\) to prove language preservation and claim that completion makes every later game position live.

The notation reset at lines 1755--1757, however, says only that the completed automaton and transition relation are again written \(\mathcal A\) and \(\Delta\).  It does not rebind \(Q\) to \(Q^\bot\).  The game then declares its Automaton positions to be \(T\times Q\) at lines 1758--1760.  If an added transition is chosen, the move rule at lines 1761--1766 sends play to \((ud,\bot)\), but \(\bot\notin Q\) by line 1732.  The successor is therefore not an Automaton position in the declared game.  In particular, the claimed infinite-play property and the application of the deadlock-free game theorem are not formally established for the game as typed.

This is not merely a cosmetic symbol collision: it occurs precisely on every formerly missing transition, the cases for which completion was introduced.  Repair the state-space declaration by explicitly rebinding the completed state set, for example by saying that henceforth \(Q\) denotes \(Q^\bot\), or keep the notation unshadowed and declare Automaton positions to be \(T\times Q^\bot\) and use \(\Delta^\bot\) in the moves.  All subsequent run, instruction, strategy, and game domains must use that same completed state space.

### 2. B\"uchi's string behavior remains undefined on the empty word

Lines 144--155 define the terminal-marker encoding only for a nonempty word \(Y_0\cdots Y_h\), and lines 156--157 separately state that the empty word has its marker at time \(0\).  Lines 158--159 then define string acceptance only for \(Y_0\cdots Y_h\), by the condition \(U[r(h+1)]\).  No value of \(h\) is assigned to the empty word and no separate empty-word acceptance clause is supplied.

Consequently the named string behavior is only partially defined even though Theorems 6--8 immediately characterize sets of finite words at lines 160--167 and the host theorem ranges over \(\Sigma^*\) at `logic-in-computer-science.tex` lines 836--850.  Merely specifying the empty word's encoded input does not specify where the arbitrary output is read.  Under the displayed recursion, the terminal read for the empty word is at the marker position \(0\), so the missing clause should state explicitly that the empty word belongs to the string behavior exactly when \(U[r(0)]\) holds for its encoded input.  An equivalent uniform indexing convention would also suffice if it is defined rather than inferred.

### 3. Elgot's constructive least-output selection uses no defined order on \(B\)

The alphabets \(A,B\) are introduced only as finite nonempty sets at lines 346--355.  After the fixed-point construction, line 427 says that “lexicographically selecting the least compatible output word” produces the required automaton.  Lexicographic leastness is undefined until a linear order on \(B\) has been fixed.  The next sentence, at lines 429--431, refers to a selection from “an order on \(B\) and its reverse,” but that later reference neither supplies the order before its first use nor states which order controls the preceding constructive theorem.

This is a small repair but a real definition-before-use gap in an asserted effective construction.  Before line 427, fix an arbitrary effective linear order on the finite output alphabet \(B\), use it for the least compatible selection, and then identify its reverse for Corollary 8.2.  No new machine or selection species is needed.

## Detailed mathematical audit beyond the must-fixes

### B\"uchi precursor presentation

The language, finite-set predicate domain, Boolean formula tuple \((E,H)\), induced recursion, output formula, special-output identity, and eventual-truth behavior are given distinct and coherent standings at lines 18--71.  The handbook-owned repair of printed Theorem 2 is mathematically sound: the finite, nonempty, downward-closed witness \(j\) has a last true point \(h\); the transition witness agrees with the actual run through \(h\); the input is forced false from \(h\) onward; and the boundary output plus special-output invariance propagates truth along the omitted tail.  The converse choice of \(h\) after both extinction and eventual truth also covers \(h=0\).  The guarded sentence decision proof correctly separates the necessary \(B(\bot,\bot)\) tail test from the finite loop-deletion search.  The false unary-powers equivalence is not retained: the counterexamples are valid, the one-character nonrepair is correctly noted, and the later \(\in_2/V_2\) correction is kept separate from the surviving one-way decidability consequence.  The only must-fix in this portion is the missing empty-word string-acceptance clause above.

### Elgot presentation

The acceptor and transducer tuples are not conflated, and their runs include the empty-word cases.  The admissible finite-set encoding handles the all-empty assignment by \(\Lambda\), while projection correctly includes right truncation of newly exposed terminal zero columns.  Both directions of Theorem 5.3 have the required construction roles.  The descending \(M_h\) calculation is finite, typed, and handles \(D=\varnothing\), failure of the empty prefix, and failure of an input continuation by returning \(\gamma_A=\varnothing\).  Its stable triples give the maximal strongly extendable sublanguage.

The erratum-controlled arbitrary-set reduction is also complete at the stated strength.  The field, relation windows, and prefix sets are typed.  For arity at least two, overlap forces one constant tag.  For unary windows, replacing \(R_j\) by \(R_j\times R_j\) and the prefix set by \((E_j\cap R_j)\times R_j\) preserves exactly the first-letter condition and all unary constraints before tagging.  The negative Post-system boundary is not overgeneralized.  Apart from the unfixed output order in finding 3, I found no mathematical defect in this portion.

### Trakhtenbrot presentation

The formal language, arbitrary-set semantics, controlled syntactic classes, and their separate semantic dependence properties are introduced before use.  Anticipation, broad finite memory, finite operator, weight, and the zero-anticipation automaton-realizable class are not collapsed.  The two-state counterexample to the printed graph-degree bound checks: its recurrence gives \(q(t)=X(1)\mathbin{\mathsf{xor}}X(t)\), the one-state contradiction is valid, and the listed graph portions are distinct.  The typed residual maps \(T_u\) correctly replace the invalid identification of broad memory states with prefix residuals.

The all-prefix portion convention, closure construction, nonempty-image limitation, and contradictory empty-set recurrence collectively cover the empty set.  Solution versus exact graph, one solution versus a general parametrization, zero anticipation versus fixed positive anticipation, and conditional versus unconditional synthesis remain distinct.  The finite-word maps are extension-independent and prefix-compatible; the explicit nonemptiness repair excludes the vacuous empty-language counterexample and supplies words at every positive length.  The special-beginning condition is not confused with an arbitrary prefix.  The technical names in this portion have definitions, standings, nonredundancy explanations, and later uses adequate under the supplied local rule.

### Rabin presentation

The successor structures, the two orders, arbitrary-root valued trees, paths, ordinary runs, and the family-valued Muller acceptance datum are typed before the logical translations.  The track encoding is a bijection at the stated full-root scope.  The finite witness is predecessor-closed and frontiered before use; frontieredness is correctly distinguished from predecessor closure.  The product in Theorem 3.1 has the correct state space \(U\times S\), update, initial set, and projected infinitely-recurring family.

Ordinary \(\exists r\,\forall\pi\) acceptance and dual \(\forall r\,\exists\pi\) acceptance remain distinct.  The empty pair sequence is handled correctly: \(\Omega^\dagger=((S,S))\) has no path maps of its type because an infinite path into finite nonempty \(S\) has a nonempty infinitely recurring set, so it is exactly equivalent to the empty sequence in the dual condition.  The well-founded obligation map is defined by absence of an infinite descent and is used at the two stated proof loci.

The two finite-run notions are also kept separate.  The external-frontier finite-tree run uses \(f\notin S\), while the emptiness base uses ordinary states at frontier nodes and imposes no outgoing condition there.  The restricted table keeps the root state unrestricted.  The repaired exhaustive recursion admits \(H=\varnothing\), and the base admits \(U_0=\varnothing\); in that base the universal hitting condition becomes exactly the absence of a finite run, with K\"onig compactness supplying the equivalence to no infinite run.  These clauses correctly preserve the vacuous dual-acceptance case.  I found no remaining mathematical or definedness defect in the Rabin portion.

### Thomas precursor presentation and host context

The finite-word tuple, \(n+1\)-state run, finite position structure, singleton and successor predicates, and weak-theory distinction are typed.  The formula guard explicitly accounts for an automaton rejecting the empty word.  For infinite trees, the manuscript distinguishes node-set paths from direction streams, gives the global-run/all-directions acceptance prefix, and defines the empty strict chain so that every path rejects.

The sink completion itself is language preserving: the new state is outside every \(F_i\), so any run using an added transition has a constantly-sink path satisfying no chain pair.  That proof covers the empty chain as well.  The defect arises only when the later game reverts to the old symbol \(Q\) without rebinding it, as detailed in finding 1.  Once that state-space repair is made, the Automaton/Pathfinder moves, local instruction labels, memoryless-strategy use, regular generator, and formula/automaton induction have coherent mathematical roles.  The host's finite-word and S2S theorems are compatible with these bounded presentations and do not erase the explicitly open 1960 B\"uchi and 1997 Thomas publication reconciliations.

## Conclusion

The manuscript contains substantial and generally careful repairs of the source-inherited edge cases, including the finite B\"uchi run witness, Elgot's unary-window promotion, Trakhtenbrot's empty set and empty language, Rabin's zero-length pair sequence and two vacuous no-run branches, and Thomas's rejecting sink and empty chain.  Nevertheless, the unchanged snapshot cannot be accepted while the string behavior is partial on the empty word, the Elgot selection order is undefined at first use, and the completed Thomas game can leave its declared position space.  Each defect has a local repair, but this Round 4 review is of the unchanged source and therefore rejects it.

REGISTER STATUS: OPEN
