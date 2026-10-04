# N-c-014 integrated mathematical review — Round 7

**Review date:** 2026-08-24  
**Seat:** fresh blind mathematical correctness, completeness, typing, edge-case, dependency, and terminology review  
**Reviewed object:** `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1884, integrated at `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--944

VERDICT: ACCEPT

## Scope and evidence actually examined

I read the actual LaTeX presentation from line 1 through its line-1884 end and the complete host interval from lines 836--944. I also read, as the only auxiliary source evidence:

- `spec/research/p09-buchi-1960-source-note.md`;
- `spec/research/p09-elgot-1961-source-note.md`;
- `spec/research/p09-trakhtenbrot-1961-source-note.md`;
- `spec/research/p09-rabin-1969-source-note.md`;
- `spec/research/p09-thomas-1996-report-source-note.md`;
- the N-c-014 compact source-presentation bullets in `spec/research/p09-source-presentations-lot2-3.md`, lines 681--745; and
- the relevant entries in `handbook/bib/handbook.bib`: `Buchi1959WeakReport`, `Buchi1960`, `Buchi1962`, `BruyereEtAl1994`, `Elgot1959Report`, `Elgot1961`, `Elgot1962Errata`, `Trakhtenbrot1961`, `Trakhtenbrot1962Expanded`, `Rabin1969`, `Meyer1975Complexity`, `McNaughton1966`, `Thomas1996Report`, and `ComonEtAl2007`.

The source notes were used as bounded evidence for the historical bodies and for the source-versus-handbook ownership statements. I did not treat a source note as manuscript-render evidence or as a substitute for checking the actual LaTeX.

## Prohibitions observed

I did not open, inspect, render, build, or cite any manuscript PDF, PNG, image, page render, or other manuscript rendering. I did not run a TeX or PDF build, test, harness, checker, repository script, or hash operation. I did not inspect any prior N-c-014 review, independent-review record, admission record, board ledger, board transcript, or review history linked from an allowed note or compact bullet. I did not alter the presentation, host, source notes, compact record, bibliography, manuscript, or any prior report. This file is a mathematical review only and is not an admission record.

## Mathematical audit

### 1. Host integration and theorem strength

The host's finite-word theorem at lines 836--854 has the correct domain and exact modern strength: a language (L\subseteq\Sigma^*) over a finite alphabet is regular exactly when it is MSO-definable on the finite position structure with the letter predicates and order. The successor-only reformulation is sound because endpoints and the finite-chain order are MSO-definable from successor; it does not identify weak and full monadic quantification on an infinite structure. Lines 846--853 explicitly distinguish this modern package from the different source encodings and do not claim verbatim occurrence in each historical body.

The host's S2S theorem at lines 877--882 uses the full infinite binary successor tree (T=\{0,1\}^*) and the typed successors (S_i(u)=ui). It states decidability only, matching the presentation's withdrawal of Rabin's obsolete elementary-recursive complexity qualification. The neighboring finite-ranked-tree definitions and theorem at lines 884--934 explicitly keep finite bottom-up runs, finite-domain weak/full coincidence, and Rabin's infinite-tree construction distinct. The input ordering at lines 940--943 places N-c-014 at the intended host seam without changing any theorem hypothesis.

### 2. B\"uchi presentation

Lines 18--71 correctly separate the interpreted weak language, finite-set predicate assignments, finite propositional automaton data, the uniquely induced run, the output predicate, and the behavior set. The special-output identity

\[
U(y)=U(H(y,\bot^n))
\]

is the required pointwise invariance under an all-false input step, not the stronger and false requirement (U(\bot^m)=\top).

The handbook-owned repair at lines 121--142 is mathematically sufficient in both directions. A finite, nonempty, downward-closed witness (j) has a last true point (h\geq0). The guarded recurrence makes (r) equal the actual run through (h); the input clause makes the real input all false from (h) onward; and (U(r(h))), together with the special-output identity, propagates output truth along the omitted tail. Conversely, an accepted special input permits (h) to be chosen after both input extinction and eventual output truth, after which the actual run can be retained through (h) and the finite witness set false. The clauses also cover (h=0): no predecessor recurrence is needed, the input is false from time zero, and the boundary test is (U(E)). Thus the repair does not hide an empty-prefix or off-by-one gap.

Lines 144--171 state the terminal-marker finite-word encoding completely, including (n\geq1), nonempty words, the separately encoded empty word, and the exact state time (r(|w|)) at which arbitrary-output string acceptance is read. Lines 173--192 preserve both the all-false-tail guard and the finite loop-deletion bound in the sentence decision. Lines 194--232 correctly separate the sound weak-monadic/regular finite-word correspondence from the false unary-powers equivalence, state why the displayed bit-occurrence formula fails, and assign the corrected (\in_2/V_2) signature to later work. No false arithmetic equivalence is retained as a handbook theorem.

### 3. Elgot presentation

Lines 241--259 type the acceptor correctly: (I) is the nonempty input alphabet, (S) is the finite nonempty state set, (f:I\times S\to S), and the empty word is accepted exactly when (d\in D). Lines 261--341 give the canonical finite-set column encoding, including the all-empty assignment, the last-nonzero-column convention, the admissible universe, both directions of Theorem 5.3, terminal-zero truncation after projection, state-track projection in the reverse construction, and the separate empty-word branch.

The finite-behavior and synthesis development at lines 357--456 is typed and total. The (A/B)-automaton applies (f) before (g) at each input position and includes the empty paired word. The four conditions in Theorem 7.1 distinguish prefix closure, output functionality, and input totality. The explicit descending construction at lines 391--431 is finite, starts from accepting run states, tests the empty prefix through (d\in D), tests every first input letter, and retains exactly the states from which every next input has a surviving output continuation. Consequently its stable language is strongly extendable and maximal. When it is empty, the subsequent universal uniqueness claim is correctly identified as vacuous; when it is nonempty, opposite output orders test the extremal functional selections.

The erratum-controlled arbitrary-set reduction at lines 458--557 does not suppress the finite union. It fixes the column-stream type, the bounded-window arity, each relation field, each prefix set, and the componentwise tagged construction. For (n\geq2), overlap of adjacent windows forces a constant tag. For (n=1), the handbook first replaces the unary constraint by

\[
\widehat R_j=R_j\times R_j,
\qquad
\widehat E_j=(E_j\cap R_j)\times R_j.
\]

This is exact: every letter is thereby forced into (R_j), while precisely the first letter retains the (E_j) condition. The binary overlap argument can then be applied without assuming a missing unary overlap. Lines 559--584 preserve the undecidability boundary and the article/report/erratum authority order.

### 4. Trakhtenbrot presentation

Lines 586--647 define the interpreted system, its primitive grammar, the standing of its normalized name, the syntactic controlled/lower/upper classes, and their separate semantic dependence consequences before those notions are used. Lines 649--702 keep anticipation, broad finite memory, bounded-anticipation finite operators, zero-anticipation automaton-realizable operators, and weight distinct; the whole-future suffix arguments in the broad memory equations are not silently replaced by finite windows.

The tuple-portion and graph calculations at lines 704--798 are correctly typed and convention-sensitive. For a zero-anticipation operator, an input prefix fixes the output prefix, and every paired graph portion is either the graph of the residual operator (T_u) or empty. The two-state counterexample is valid: its recurrence gives (q(t)=X(1)\mathbin{\mathsf{xor}}X(t)), its output is the identity branch when (X(1)=1) and zero otherwise, and a one-state presentation would have to use the same suffix function at times one and two. Its original, zero, identity, and inconsistent portions refute the printed weight-to-degree bound even under the nonempty-portion convention.

Lines 800--852 repair the converse construction's empty-set endpoint without weakening the theorem. For a nonempty homogeneous set, the finite portion transition and a choice stream generate exactly the closure; closedness makes the image the original set. For the empty set, a contradictory initial state clause gives the same recurrent syntactic shape without pretending that a total map can have empty image. The distinction between unconditional residual transitions and conditionally decidable nonemptiness is retained.

Lines 854--912 distinguish graph definition from graph containment, continuity from mere finite memory, one solution from a general parametrization of all and only solutions of a named class, and one fixed anticipation bound from an unbounded simultaneous statement. Lines 914--989 type the positive-length word maps before using them. The printed converse from automaton-decidability to automaton-enumerability is correctly strengthened by (L\neq\varnothing): together with positive-prefix closure and strict extendibility, that supplies a word at every positive length, whereas the empty language is decidable but cannot be the range of a total length-preserving operator. The special-beginning condition is also distinguished from an arbitrary finite prefix.

### 5. Thomas finite-word presentation

Lines 1008--1080 give the finite automaton, word-position structure, (n+1)-state run, and both effective logical translations with their correct types. The automaton-to-formula direction explicitly handles the last transition and the empty-word guard. The singleton-set translation defines singleton and successor on the finite position domain before the atomic automata are invoked. WS1S is kept as a theory over (\mathbb N) with finite set variables rather than identified with any one finite word structure. The May 1996 report is explicitly used only at precursor strength and is not substituted for the distinct B\"uchi, Elgot, or Trakhtenbrot source presentations.

### 6. Rabin presentation

Lines 1082--1197 define both source orders, the (n)-successor structures, arbitrary-root valued subtrees, paths, transition tables, ordinary automata, runs, the infinitely-recurring-state operator, and ordinary (\exists r\,\forall\pi) acceptance. The later pair sequence is not put into the ordinary automaton tuple. The later non-elementary lower bound is used only to withdraw Rabin's complexity qualification, not his decidability or effectiveness result.

Lines 1199--1293 type the track-tree bijection and both logical directions. The principal-formula family is displayed before use. The finite witness object is finite, rooted, predecessor closed, and frontiered; frontieredness is defined as a property of that set and is distinguished from mere predecessor closure. The worked two-track example can be witnessed by extending the named node and child until both are labelled internal nodes. The converse run tracks and the exact closed-sentence-to-nonemptiness dependency are also present.

The path-language product at lines 1295--1347 has the correct time alignment. At a node carrying product state ((u,s)), both children carry first coordinate (K(u,s)); along a branch this is the unique deterministic word-automaton history on the tree-table state sequence. Projection of the infinitely recurring product pairs onto the first coordinate gives the required Muller set because the second state component is finite.

Lines 1349--1466 correctly define type-(\Omega), type-(\Omega)-empty, and dual (\forall r\,\exists\pi) acceptance. The zero-length pair-list case is not assumed away. For (\Omega^\dagger=((S,S))), no infinite path map can have an infinitely recurring state set that both meets and avoids (S); hence its path type is impossible, and its dual language equals the empty-list dual language, namely the no-run case. This gives an exact positive-length induction input rather than a new acceptance condition. The marked-obligation, simultaneous-run, well-foundedness, ordinal-stratum, two-half-step, and pair-length-induction roles remain separate.

Lines 1468--1522 distinguish three finite objects that would otherwise be easy to conflate: a source finite-tree-automaton run uses the external frontier value (f\notin S); a valid frontiered tree can nevertheless have one frontier child and one internal child, for which the printed no-mixed-pair transition type permits no run; and the later emptiness base uses ordinary states even at frontier nodes. The lift, principal-formula application, compactness lemma, and complementation corollary are assigned distinct roles.

The actual emptiness recursion at lines 1533--1657 is complete at the stated outline strength. Alphabet erasure is sound node by node; complementation and the dual conversion reduce nonemptiness to one specified dual question; current table state sets are allowed to change under reductions; and the restricted table constrains states strictly below, not necessarily at, the root. The (L_k=\varnothing) reduction includes (H=\varnothing) as the direct shorter question. The (k=1) base permits (U_0=\varnothing), in which case the finite witness says that there is no finite table-run from the root state; K\"onig compactness makes such a finite obstruction equivalent to the absence of an infinite run. The external weak finite-tree decision theorem is identified as a dependency and is not confused with S2S or with a regular-tree basis theorem.

Lines 1659--1687 accurately delimit the application chapter and say what detailed source machinery remains in the cited article. This is a legitimate proof boundary, not a completeness claim for a fourteen-page line-by-line reconstruction.

### 7. Thomas infinite-tree presentation

Lines 1689--1753 define the Muller tree automaton, one global run, direction-stream paths, (\exists r\,\forall\pi) acceptance, strict chain condition, and the finite order-vector-with-hit memory. The empty-chain endpoint is explicit: the existential pair condition is false, so every path rejects.

The partial-transition completion at lines 1755--1789 is language preserving. The new state lies outside every (F_i) (and therefore every (E_i)); a run using an added transition has a path eventually constant at that state and fails every chain pair, while every original run remains. The completion thus supplies nonempty outdegree at every game position without adding an accepting run, including when the chain is empty.

Lines 1790--1829 correctly type the Automaton and Pathfinder positions and moves. A node-labelled finite function records Pathfinder's current-position-only choices, and the complement construction is independent of the particular input tree. The completed game meets the nonempty-outdegree premise. The empty chain is the trivial Pathfinder-winning base; nonempty chains use the stated finite-visit recursion and finite-game effectivity.

Lines 1831--1877 define a regular input tree by a finite deterministic direction generator before using the regular-member theorem. After labels are guessed, a memoryless winning strategy on the finite game fixes a finite generator; therefore emptiness is decidable and every nonempty recognized language has a regular member. The final MSO translation uses the same language-preserving completion before negation and emptiness. Lines 1879--1884 explicitly keep this later game-and-basis route separate from Rabin's 1969 complementation and Section 3.12 emptiness proof and retain the report-versus-final-chapter boundary.

## Definition-before-use, standing, and technical-name rule

No technical-name must-fix remains. In particular, the handbook-owned or source-normalized names that carry the highest ambiguity risk are introduced with all five required elements at their first substantive use:

- residual stream operators are exactly the typed maps (T_u), are distinguished from broad memory states, and are used to correct the graph-portion argument (lines 735--793);
- a general solution is given its two exact quantificational clauses, is distinguished from one solution, and is used in the synthesis theorems (lines 878--910);
- `frontiered` is an exact property of a finite predecessor-closed node set, is distinguished from predecessor closure, and is required by the finite automaton, lift, and emptiness constructions (lines 1245--1260 and 1468--1522);
- (\Omega^\dagger) is an exactly defined one-pair sequence, not an acceptance mode, and is used only to enter the positive-length dual induction (lines 1399--1422 and 1574--1576);
- well-foundedness is the exact absence of an infinite obligation-descent sequence, is a property of the obligation dependency map rather than a run or path condition, and is used in the marked-tree half-step (lines 1436--1465);
- a finite table-run is explicitly an ordinary-state restriction of the current one-letter table, is distinguished from both other run notions, and is used in the (k=1) emptiness base (lines 1587--1646);
- the completed chain automaton (\mathcal A^\bot) is exactly defined, distinguished from its runs and game, and used to discharge the game's live-move premise (lines 1755--1789); and
- a regular tree is exactly a tree generated by the displayed finite deterministic direction automaton with output, is a property of an input tree rather than an acceptance mode, and is used in the regular-member consequence (lines 1831--1856).

Other operative notions—special output, string behavior, admissible encoding, strong extendability, finite operator, portion, homogeneity, solution, automaton-enumerability, dual acceptance, strict chain, and memoryless strategy—are likewise defined and typed before their theorem uses and are distinguished where nearby terminology could otherwise collapse them.

## Dependencies, completeness boundary, and open source strength

The presentation exposes rather than conceals its dependencies: McNaughton's deterministic Muller word result enters Rabin's path product; Doner/Thatcher--Wright finite-tree decidability enters Rabin's emptiness base; Meyer supplies only the later complexity correction; and Thomas supplies a later, separately attributed game-and-regular-basis route. The presentation reconstructs the operative objects, proof reductions, edge cases, and theorem dependencies needed for the host claims while explicitly declining to reproduce every transition table or every induction from the long historical proofs.

The unresolved B\"uchi 1960 journal-versus-1959-report reconciliation and Thomas 1997 chapter-versus-1996-report reconciliation are stated at first use and again at the presentation boundaries. They limit source-version fidelity but do not make a mathematical statement silently stronger than its evidence. They therefore do not create a mathematical must-fix in this snapshot, while they do prevent closing the overall register item.

## Line-specific must-fixes

None.

REGISTER STATUS: OPEN
