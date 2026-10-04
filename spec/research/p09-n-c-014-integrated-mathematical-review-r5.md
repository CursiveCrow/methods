# Fresh blind Round 5 integrated mathematical review — N-c-014

VERDICT: ACCEPT

## Review scope and decision rule

This is a direct mathematical and definedness review of the current reader-facing LaTeX for `N-c-014`, bounded to the source strengths that the manuscript itself claims.  I reviewed the presentation for definition-before-use, exact standings and types, empty and vacuous cases, partial transitions and completions, theorem hypotheses and conclusions, proof dependencies, and compliance with the local technical-name rule.

The acceptance threshold was strict: any unresolved mathematical error, ill-typed construction, undefined recursion, missing hypothesis, false empty-case claim, or proof dependency that does not establish the stated conclusion would require `VERDICT: REJECT`.  Source-version obligations that the manuscript expressly leaves open do not by themselves defeat this bounded mathematical verdict.

## Evidence read

I read the following actual text directly:

- `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1859, from the first line through EOF;
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--941;
- `spec/research/p09-buchi-1960-source-note.md`, lines 1--367;
- `spec/research/p09-elgot-1961-source-note.md`, lines 1--423;
- `spec/research/p09-trakhtenbrot-1961-source-note.md`, lines 1--583;
- `spec/research/p09-rabin-1969-source-note.md`, lines 1--665;
- `spec/research/p09-thomas-1996-report-source-note.md`, lines 1--353;
- the compact `N-c-014` source entries in `spec/research/p09-source-presentations-lot2-3.md`, lines 681--745, and its relevant open-source bullets at lines 974--975; and
- the relevant entries in `handbook/bib/handbook.bib`: `McNaughton1966`, `Thomas1996Report`, `Elgot1961`, `Elgot1959Report`, `Elgot1962Errata`, `Meyer1975Complexity`, `Rabin1969`, `Trakhtenbrot1961`, `Trakhtenbrot1962Expanded`, `Buchi1959WeakReport`, `Buchi1960`, and `BruyereEtAl1994`.

The five permitted source notes were used as the bounded source and version evidence.  Administrative or prior-review assertions embedded in those permitted notes were not used as substitutes for reviewing the current LaTeX.

## Prohibited actions not taken

- I did not open, inspect, render, build, or cite a manuscript PDF, a manuscript page image, a PNG, or any other manuscript render.
- I did not open or inspect any historical-source PDF or page image; the permitted source notes, not source renders, supplied the source-bounded evidence for this review.
- I did not run TeX, a PDF build, tests, a test harness, an automated checker, a repository script, a hash command, or any other automated validation.
- I did not open any earlier `N-c-014` integrated review, admission record, board file, ledger, chair transcript, or review-history file.
- I did not call `list_agents` or delegate any part of the review.
- I did not edit the manuscript, host, bibliography, source notes, compact source record, ledger, or any prior report.

## Detailed mathematical findings

### 1. Host theorem and integration boundary

The host theorem at `logic-in-computer-science.tex` lines 836--851 has the correct modern finite-word strength: for a finite alphabet, MSO definability over the finite position structure is equivalent to regularity.  It expressly says that the displayed sentence is a modern formulation and does not claim verbatim occurrence in each historical source.  The finite-word presentation is included at line 939 after the host has distinguished finite ranked-tree bottom-up automata from Rabin's infinite-tree runs at lines 881--930.  The `S2S` theorem at lines 874--879 has the correct full binary successor-tree domain and conclusion.

The presentation preserves the relevant source boundary.  Büchi's current evidence is the 1959 report precursor rather than a reconciled 1960 journal body (`n-c-014.tex` lines 8--16 and 977--983), and Thomas's locators belong to the May 1996 report rather than the unreconciled 1997 chapter (lines 985--1057 and 1854--1859).  Those limitations are stated as limitations; neither is silently promoted to stronger version evidence.

### 2. Büchi finite-set logic, automaton recursion, and finite-word edges

Lines 18--71 distinguish all operative standings: individuals range over `\mathbb N`; predicate variables range over eventually-false Boolean predicates, equivalently finite subsets; `E` and `H` are finite propositional data; the transit predicate is the unique total recursion

\[
 r(0)=E,\qquad r(t+1)=H[r(t),i(t)];
\]

`U` induces the time predicate `u`; and `\beta(E,H,U)` is a set of special input assignments.  The special-output identity is pointwise invariance under an all-false transition, which is exactly what is required to make the output eventually constant on an eventually-false input.

The handbook-owned repair of the printed analysis formula at lines 95--142 is mathematically sufficient in both directions.  A finite, nonempty, downward-closed cutoff predicate `j` has a last true point `h`; the recurrence is enforced through `h`; the input is forced false from `h` onward; and `U(r(h))`, together with special-output invariance, propagates truth along the omitted actual tail.  Conversely, an accepted special input supplies such an `h`, and the finite run witness may be set false after that point because no later recurrence clause is imposed.  The clauses also cover `h=0`.

The terminal-marker word encoding at lines 144--171 handles both nonempty and empty words explicitly.  A word of length `|w|` is tested at `r(|w|)`, while the empty word is tested at `r(0)`; the extra all-true marker is part of the finite predicate encoding rather than a silently assumed endpoint.  The sentence decision at lines 173--192 first checks the all-false-tail constraint `B(\bot,\bot)` and then performs the bounded path search, so a finite witness cannot evade the required infinite false tail.  The later arithmetic discussion correctly separates the sound finite-word/weak-monadic result from the false unary-powers equivalence and from the later corrected `\in_2/V_2` signature.

No undefined transition, no-run case, or empty-word defect remains in this part.

### 3. Elgot finite words, maximal extendability, and the corrected infinite synthesis reduction

The source acceptor at lines 241--259 has a finite nonempty state set, a total typed transition map `f:I\times S\to S`, an initial state, and an accepting subset.  Its run has exactly one more state than input letters, and the empty word is accepted exactly when the initial state lies in the accepting subset.

The finite-set column encoding at lines 261--346 is canonical: the all-empty assignment maps to `\Lambda`, every nonempty assignment is cut at its last nonzero column, and the admissible universe is `U_r^*U_r^0\cup\{\Lambda\}`.  Coordinate projection is followed by removal of newly exposed terminal zero columns, so existential finite-set quantification respects the canonical encoding.  The reverse construction separately handles `\Lambda` and correctly types the start set, terminal set, and local adjacency relation.

The descending construction at lines 377--439 is a valid finite greatest-survival computation for the largest strongly `A`-extendable sublanguage.  Each retained triple carries an accepting post-state; the fixed-point condition supplies a continuation for every next input letter; the two initial tests cover the empty prefix and all first input letters; and induction proves maximality.  If the initial state is not accepting or some first-letter continuation set is empty, the construction correctly returns the empty language.  Corollary 8.2's uniqueness condition is expressly vacuous when that language is empty.

The erratum-controlled arbitrary-set reduction at lines 449--548 has the necessary literal hypotheses: the matrix is quantifier-free, has only the displayed variables free, contains neither equality nor order, and depends on a bounded successor window.  The manuscript does not assume that the resulting language is governed by a single relation.  It keeps the finite union, defines each relation's field, and types the prefix sets.  For arity at least two, overlapping tagged windows force one constant tag.  For unary windows, the promotion

\[
 \widehat R_j=R_j\times R_j,\qquad
 \widehat E_j=(E_j\cap R_j)\times R_j
\]

preserves exactly the original first-letter condition and unary pointwise constraint before applying the tagged binary construction.  Empty relation languages remain empty under this promotion.  Thus the projection is exactly the required finite union, and the later synthesis dependency is sound.

### 4. Trakhtenbrot's types, residuals, empty set, and positive-length word boundary

Lines 577--638 define the interpreted formal system before using its syntactic subclasses.  Individuals, arbitrary monadic predicates, successor iterates, atomic formulae, eliminable conveniences, controlled quantifier ranges, and the separate semantic prefix/tail dependencies are not conflated.

Lines 640--684 correctly distinguish bounded anticipation, broad finite memory whose update may inspect the whole future suffix, finite operators, and the zero-anticipation automaton-realizable subclass.  The initial state and the typed output/update maps make the state recursion unique for each input stream.  The later `A` in “`A`-operator” is expressly distinguished from an input-alphabet variable.

The one-coordinate and tuple portions at lines 695--747 are coordinatewise residual sets.  The graph residual `T_u` has a typed stream domain and output domain; zero anticipation makes its removed output prefix independent of the chosen continuation; and inconsistent paired prefixes yield the empty portion.  These residual stream maps are explicitly distinguished from states in the source's broader whole-future finite-memory presentations.  The two-state counterexample at lines 749--785 is correct: induction gives `q(t)=X(1)\mathbin{\mathsf{xor}}X(t)`, the output is the stated operator, no one-state suffix presentation can realize both the time-one and the `01` time-two requirements, and the listed graph portions are four distinct sets.  It therefore refutes the printed numerical homogeneity bound without affecting graph closedness.

The closed-homogeneous converse at lines 790--833 treats the empty case rather than applying a total covering map with necessarily nonempty image.  For a nonempty set, every nonempty portion permits at least one next bit, the finite portion transition gives a total choice-stream map, and its image is exactly the closure.  For the empty set, contradictory initial clauses define the empty set in the same recurrent syntactic shape.  This closes the no-image edge without changing the theorem.

The finite-word action at lines 919--966 is extension-independent and prefix-compatible by zero anticipation.  Its languages are explicitly positive-length languages.  The manuscript identifies the missing empty-language seed in the printed converse: the empty language is decidable and satisfies the printed conditions vacuously but cannot be a lengthwise range of a total operator.  Adding nonemptiness, together with prefix closure in the stated positive-length word universe and proper extendibility, supplies words at every positive length.  The weak eventually-zero system and “special beginning” condition then fix the tail rather than treating an arbitrary finite prefix as a complete input.

### 5. Thomas's finite-word construction and the empty word

Lines 985--1050 type the finite automaton, word position structure, letter predicates, successor relation, and successful run.  A word of length `n` has a run of length `n+1`, including `n=0`.  In the automaton-to-formula direction, state tracks cover the pre-final states and the final transition is tested separately; the text expressly records the report's empty-word behavior and the required existence guard when the automaton rejects the empty word.

The reverse direction defines singleton and singleton-successor predicates over arbitrary subsets of the finite position domain before listing the atomic automata.  Complement, union, bit-track projection, and the separate input-free `WS1S` decision use have the correct logical roles.  The finite position structure is not confused with the infinite weak-successor structure.

### 6. Rabin ordinary runs, products, dual vacuity, finite trees, and emptiness

Lines 1065--1165 define finite words, both orders, successor maps, predecessor, the structures `\mathfrak N_n`, rooted subtrees, paths, valued trees, partial move tables, runs, and ordinary acceptance before use.  A path is rooted, predecessor closed, and chooses exactly one child at every level, hence is infinite.  Ordinary acceptance has the essential `\exists r\,\forall\pi` order and uses a family `F\subseteq\mathcal P(S)`; the later pair sequence is not substituted for that datum.  A partial move table may have no run.

The formula tracks and both definability directions at lines 1176--1269 are correctly typed.  The finite witness object used for principal formulae is defined before the worked example: it is finite, rooted, predecessor closed, and separately required to be frontiered.  The terminal-node frontier, frontieredness property, and finite valuation domain are all distinguished.  The converse formula has the correct existential state-track/universal path-set prefix.  A closed sentence is reduced directly to automaton nonemptiness, matching the stated source proof boundary.

The path-language product at lines 1271--1323 is sound.  The deterministic Muller word automaton has a total transition function, so its first-coordinate history is coherent up to every branch point.  At depth `n`, the product state carries the word-automaton state before reading the current tree-run state; both children receive the update after that state.  Projection of the infinitely recurring product pairs to the first coordinate gives exactly the infinitely recurring word-automaton states because both component sets are finite.

The dual language at lines 1325--1373 has the correct `\forall r\,\exists\pi` prefix and is true vacuously when no rooted run exists.  The zero-length sequence case at lines 1375--1398 is exact.  No path map is of type `((S,S))`, so the one-pair sequence `\Omega^\dagger` represents exactly the same no-run language as the empty sequence and legitimately enters the source's positive-length induction.  Its definition, standing, reason for introduction, difference from ordinary acceptance, and subsequent use satisfy the local technical-name rule.

The marked-obligation and well-foundedness development at lines 1400--1442 supplies the exact no-infinite-deferral condition, its standing as a relation among obligations, its ordinal characterization, and the two later proof uses.  It is not used as a vague replacement for the finite-state simultaneous-run construction.

The source finite-tree automaton at lines 1444--1497 keeps the distinguished frontier value outside the ordinary state set and permits no mixed state/frontier transition pair.  The run type, root condition, frontier values, and transition condition are explicit.  The text correctly observes that a frontiered tree can have one frontier child and one nonfrontier child at a node even though the printed automaton then has no run there.  That is a permitted no-run input, not a reason to enlarge the source transition codomain.

The emptiness reconstruction at lines 1508--1632 preserves every edge case needed for the recursion:

- erasing the input labels by unioning transitions preserves nonemptiness;
- complement followed by the dual conversion returns the original one-letter language;
- an empty pair sequence is normalized before positive-length recursion;
- restricted tables constrain states strictly below the root while retaining the formal root-state type;
- the arbitrary half-step includes `H=\varnothing`, which is the direct shorter question;
- the base permits `m=0` and `U_0=\varnothing`;
- a finite table-run uses ordinary states at frontier nodes and imposes no transition there; and
- when `U_0` is empty, the finite witness must admit no such run, exactly matching the no-infinite-run case by König compactness.

The weak two-successor finite-tree decision theorem is kept as an external dependency at the base.  It is not used to turn the full infinite-tree logic into weak logic or to substitute a later regular-tree basis theorem for Rabin's argument.

### 7. Thomas's later game route, partial-transition completion, empty chain, and regular basis

Lines 1664--1701 type the later Muller tree automaton, full-tree input, global run, direction-stream paths, and `\exists r\,\forall\pi` success condition.  The direction stream is explicitly distinguished from Rabin's earlier path-as-node-set convention.

The chain presentation at lines 1703--1728 covers the endpoint `m=0`: the existential pair condition is false, so every path rejects.  For positive length, the strict chain and its path condition are exact.  The order-vector-with-hit is defined as finite automaton memory, distinguished from an input tree and a run, and used for the precise recovery of the Muller recurring-state set.

The rejecting completion at lines 1730--1759 is language preserving.  For every missing state/letter transition it adds the pair `(\bot,\bot)` and makes `\bot` absorbing.  The old chain sets remain subsets of the enlarged state set and contain no `\bot`.  Therefore every new run that uses an added transition has a path eventually constant at `\bot` and fails every chain pair, while every old run remains available.  The empty chain remains empty.  Completion supplies nonempty outgoing moves at every later game position without strengthening the recognized language.

After the explicit renaming at lines 1761--1764, the game at lines 1765--1804 has typed Automaton and Pathfinder positions, a live move from every position, an initial position, an infinite play, and the exact chain payoff.  A current-position-only Pathfinder strategy is representable by a tree of finitely many local direction functions.  The complement automaton is independent of the particular input tree.  The determinacy theorem is applied only after completion has established its nonempty finite-outdegree hypothesis.

The regular-tree definition at lines 1806--1831 supplies a finite nonempty generator state set, total direction transition, output map, and total word extension `\delta^*`, including the empty direction word.  The emptiness/basis argument treats the empty chain separately and applies the same deadlock completion before solving the finite game.  A memoryless winning strategy then supplies a finite deterministic generator for an accepted tree.  The final MSO translation at lines 1833--1852 uses the completed complementation and emptiness results in the correct dependency order.

### 8. Technical-name rule and cross-presentation nonconflation

Every locally introduced technical expression needed by the mathematical construction is either a source term with an exact definition or a handbook-owned abbreviation whose necessity, standing, nonredundancy, and later use are supplied at introduction.  In particular, the residual stream maps, `\Omega^\dagger`, frontieredness, finite table-runs, the completed chain automaton, and the order-vector-with-hit are not hypothetical names standing in for unconstructed objects.

The presentation also preserves the noninterchangeable standings across sources: Büchi's formula-defined bit recursion is not Elgot's acceptor or transducer; Elgot's causal infinite behavior is not Büchi acceptance; Trakhtenbrot's whole-future finite memory is not a prefix-determined automaton state; Rabin's ordinary Muller-family acceptance is not his dual pair sequence; Rabin's source finite-tree runs are not the host's ranked bottom-up runs; and Thomas's later regular-basis game route is not projected backward into Rabin's Section 3.12 proof.

## Must-fix findings

None.  I found no line-specific mathematical, typing, definedness, empty-case, partial-transition, completion, vacuity, theorem-strength, dependency, or technical-name defect in the reviewed snapshot.

## Bounded open status

This verdict accepts only the mathematical correctness and completeness of the current integrated LaTeX at its expressly bounded source strengths.  It does not close the unreconciled 1960 Büchi journal version, the unreconciled 1997 Thomas chapter, final typesetting or visual inspection, Part IX, the handbook, or publication.  No admission record is added by this report.

REGISTER STATUS: OPEN
