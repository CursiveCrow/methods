# N-c-018: full sequential text inventory

The active source-presentation file has been read **in full, lines 1–10,097, sequentially**. There is no unread interval. This replaces the earlier sampled census for this file; it does not replace a mathematical correctness audit.

- File: `handbook/parts/p09/presentations/n-c-018.tex`
- SHA256 at every read and again after the last line: `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49`
- Size: 294,217 bytes; 10,097 lines.
- Reading evidence: 28 consecutive numbered, non-truncated intervals listed below.
- Current heading inventory: 125 subsection/subsubsection/paragraph intervals, all covered by the sequential reading.
- Companion structured record: [p09-n-c-018-full-text-inventory.json](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/p09-n-c-018-full-text-inventory.json).

Only these two audit outputs were edited. The book, registers, bibliography and sources were read-only. No tests, builds, renders, acquisitions, or additional agents were used.

## Disposition

The original N-c-018 requirement's core subjects—syntax, Knaster–Tarski semantics, parity-game connection, and the alternation hierarchy—are substantively present, with extensive supplied proofs. The file is far beyond a heading or statement-only treatment.

The **inventory task is complete**. Whole N-c-018 source completeness remains unverified because the original Kozen threshold and imported tree-like convention have distinct unresolved source obligations, source-version qualifications remain, and reading the full text does not establish correctness of every long argument. The JSON therefore keeps `completion_verified: false` for the manuscript obligation while recording `inventory_complete: true` and `all_manuscript_lines_read: true`.

A cited theorem is not automatically an omitted proof. In particular, the current full-calculus completeness statement expressly uses Walukiewicz as a cited deductive dependency. The text does not pretend that the later semantic ANF construction proves derivable normalization.

## Requirement and active interfaces

The original row in `spec/registers/new-content.csv` is:

> N-c-018, P9, 9.5 model-checking: modal mu-calculus: syntax, Knaster-Tarski semantics, relation to parity games, alternation hierarchy statement. Sources: Kozen 1983; Emerson-Jutla 1991; Bradfield-Stirling 2007. Note: subsumes CTL/LTL expressiveness discussion; cross-listed with D-P10-009.

The historical treatment code S is recorded but was not used as a current ceiling.

The current host at `handbook/parts/p09/logic-in-computer-science.tex:1047–1101` defines the simple, Emerson–Lei and Niwiński class-generation rules and states the precise strictness claim: a closed simple Sigma_n witness has no Niwiński Pi_n equivalent, including over all finite transition systems. The later proof at N18 lines 9348–10097 matches that stated claim. The host retains a cited tagline while explicitly directing the reader to the supplied body proof; the tagline is not evidence that the local proof is absent.

The actual language/model/card interface at `handbook/parts/p08/temporal-epistemic-supplement.tex:188–302` was read. It fixes nonempty Kozen models, positivity, primitive and derived syntax, the equational calculus, and weak completeness. The complete ten-line `handbook/registry/calculi/hilbert-mu.tex` was also read: the Boolean equational base, modal join/mixed/zero principles, pre-fixed-point axiom and Park rule match the local interface as text.

The active `handbook/annex/p09.tex` imports general P9 proofs, finite trees, and ALC; it imports no N18-only annex. N18 itself has no annex reference. Its substantive supplied proofs are in this source-presentation file.

## 1. Kozen presentation, lines 6–2503

### What is actually supplied

Lines 9–199 give the two languages, environments, modal dead-end behavior, least/greatest fixed points, complement duality, nested polarity, capture-safe substitution, transfinite approximants and stabilization. The fixed-point proof is written out. Stabilization uses an ordinal that cannot inject into the powerset; this is a set-theoretic background dependency, not an independently audited Hartogs proof here.

Lines 201–375 construct closed subformulas from raw occurrences with binder links, prove the seven-rule closure/leastness characterization, define activity, supply the activity transitivity/prefix argument, and define aconjunctivity. The source's substitution notation is explicitly translated into the book's replacement-before-variable order; the operation is sequential, innermost first.

Lines 377–748 contain two substantial separation arguments. The first specifies an omega+1 closure-ordinal model and proves its approximants, with dependent choice explicitly used for the general infinite-path converse. It derives the PDL star identities and the PDL filtration separation. The second gives the even-number model and a full finite/cofinite proof using a word lemma, a guarded finite automaton, and induction over PDL programs with iteration, tests and converse.

Lines 750–950 state the exact equational calculus and prove its soundness, six derived fixed-point laws, a consistency consequence, and a two-state counterexample to misreading Park induction as a local implication rule.

Lines 952–1424 define the raw-key tableau, eight counter assignments, deterministic collision handling, nu-flag guard, clash/overflow outcomes, finite counter lifetimes, nonmodal saturation, and a finite safety-game decision for nonrejection. Infinite modal continuation is not confused with termination. Counter identity, sharing and priority order remain part of the finite state.

Lines 1426–1965 supply the nonrejection-to-model direction: collision-continuation bounds, ordinal-closed labels, all six saturation conditions, a parameterized truth lemma with every binder case, a finite directed-model quotient, and an explicit backedge representation.

Lines 1967–2370 give a separate, complete-as-text context-counted consistency-to-nonrejection proof using closed formula annotations and repeated-context exclusion. Its estimates and exact algorithm variant are explicit.

### Original threshold: the precise remaining boundary

The initial source cap is `N=2^m` at lines 1028–1032. The general supplied consistency proof instead uses

`M = 2^m (m^2+1)^(m^2)`

at lines 1967–1984. It preserves the rule/counter machinery but changes overflow. Lines 2230–2247 count context signatures, including the distribution of fixed higher annotations among their changing holders. Lines 2278–2292 obtain the smaller raw-label count only when all higher annotations equal 1, including the highest-priority counter. Lines 2367–2370 expressly distinguish the resulting A_M proof from the earlier N presentation.

Consequently, the original N-cap consistency-to-nonrejection conclusion is **not established by the supplied general A_M argument**. This is an original-source/threshold obligation, not a claim that the A_M construction is absent or that no finite-model theorem has been proved.

### Tree/backedge convention: the precise boundary

Lines 1933–1956 explicitly unfold a finite directed model until a projected state repeats and then insert a backedge to its earlier ancestor occurrence, allowing a self-loop. The tree-edge depth is at most the number of directed states minus one.

Lines 1958–1965 explicitly permit nested or crossing backedges and impose no further condition on their targets. Therefore this proof establishes an ordinary rooted tree with ancestor-or-self backedges. It does not establish a stronger no-nesting/no-crossing convention. Whether Kozen's imported use of “tree-like” requires a stronger convention remains a source-definition verification task; the inventory does not assume the stronger requirement without that check.

### Full equational completeness: citation is deliberate

The theorem at lines 2384–2394 is `thm:p09-kozen-full-completeness`, tagged `cited=Walukiewicz2000`. It covers full finitary L_mu, not only aconjunctive or initially guarded formulas.

Lines 2396–2418 align the author-version theorem and K1–K6 calculus with the actual sheet. Lines 2420–2439 identify the deductive bridge:

- Fact 17: provable normalization to the positive, guarded, well-named cover presentation.
- Theorem 26: semantic disjunctive normalization together with the crucial derivable inequality from the input to the normal form.
- Theorem 18: derivability of the negation of each unsatisfiable disjunctive formula.
- Theorem 25: the resulting weak completeness.

This is a cited proof with its exact interfaces explained. The full Walukiewicz proof is not locally reproduced, and the later semantic ANF theorem is explicitly not offered as a substitute. Lines 2441–2502 supply the equation/inequality/finite-premise consequences and a complete noncompactness example, preventing promotion to arbitrary-premise strong local completeness.

## 2. Emerson–Jutla presentation, lines 2504–4696

The text supplies substantially more than a theorem summary:

- The nondeterministic and alternating OR/DAND/AAND tuples, source GREEN/RED Streett condition and complementary Pairs convention, finite threads/infinite ithreads, and node-plus-state history freedom.
- Finite-play terminal convention and absorbing completion, including the empty input alphabet and an empty original Streett pair list.
- A proved Streett response monitor and full-state Muller permutation record interface.
- Nondeterminization using augmented controls, a deterministic good-trace monitor, subset obligations and explicit directional choice maps. Both language directions and the stated double-exponential bounds are written.
- A formula automaton for the source's single-proposition-labelled full binary trees. Used alphabet P0, optional ambient symbols, both sinks, empty true/false transitions, unrequired directions and all three transition layers are explicit. Both Boolean/layered game directions and the history-free strategy extension are supplied.
- A corrected reverse-translation scope: general ordered-tree automata use separate 0/1 modalities. The two trees with the sole P at the left versus right root child give a concrete separator against unindexed EX/AX.
- Paired-color, total bipartite parity games with round predecessors; target-aware nested formulas, both players' characterizations, reach/avoid duality, pure determinacy, and a separate full-vertex target variant.
- Equality of remaining *labelled, move-named* game trees, its quotient arena, strategy transfer, and uniform positional choices.
- The complete Section 5 fixed-point arguments: constrained reachability, safety with exit, complementary countable operators, ordinal-decreasing I phases, full-prefix closed-set predicates, least-unviolated-index II phases, and the separate historical-maximum strategy for natural colors.

The countable quantifiers are explicitly unions/intersections of predicates; these schemata are not advertised as finite syntax or as positional strategies for arbitrary infinitary objectives.

The generic conversion's finite-representation interface deserves a future source/correctness check: the opening tuple prose explicitly says OR is finite, while later counts use m as the number of DAND choices. The formula-generated tuple is explicitly finite. This inventory records the interface question without asserting a counterexample or an absent construction.

## 3. Bradfield–Stirling and supporting developments, lines 4697–10097

### Source-version boundary

Lines 4700–4703 explicitly assign the locators to the accessible preprint dated 15 November 2005 while the bibliography identifies the 2007 chapter. This is a distinct source state. Literal identity with the published chapter has not been established by reading the present manuscript.

### Supplied semantic and game machinery

Lines 4705–5415 provide labelled systems, primitive box/nu syntax, coherent-environment bisimulation invariance, image-finite HML converse, unravelling, complete evaluation-game data, four binder cases in the truth/strategy induction, examples, and a transfinite positional-determinacy proof. The latter explicitly works in ZFC, handles infinite branching by re-closing removed regions under attraction at limit stages, and constructs one winning strategy on each entire region.

Lines 5417–6013 give contextual environments for raw occurrences, linked-game truth, pre-model annotations/trails, both directions of same-structure pre-model equivalence, ordinal certificate construction and examples, and bounded-branching model pruning. The text distinguishes a single coherent winning strategy from arbitrary mixtures of individually winning choices.

### Supplied automata and normal forms

Lines 6015–6674 define modal parity games/runs, prove their equivalence, give Boolean closure, and build guarded one-step automata from arbitrary closed formulas. Finite local games account for unguarded internal-only loops. The proof distinguishes actual recurring control priority from a running minimum used only to summarize a completed episode, and it gives both strategy directions and effective finite bounds.

Lines 6676–7241 supply the reverse translation through an explicit finite-control product, the complete binary and finite-coordinate Bekić identity, scalar control elimination, and two nested-block calculations. The result uses only the original vocabulary on the original model, with no polynomial-size or alternation-preservation promise.

Lines 7243–8266 supply cover identities/games, the bad-trace monitor, Muller-to-parity conversion, both directions of cover simulation, the exact ANF grammar, guarded substitution/Bekić preservation, and cover-to-ANF scalarization. The composed normal-form theorem is explicitly **semantic** same-model equivalence. It does not prove the deductive normalization needed by the equational axiomatization.

Lines 8268–8907 supply both cut-equisatisfiability directions, an occurrence game, the finite reconstructed endpoint model, linear decision in the specified ANF representation, full finite-model/decidability consequences, and counterexamples to dropping the grammar hypotheses. Its finite-model size is measured in ANF size; it is not asserted to be linear in an arbitrary shorter pre-normal-form formula.

### Supplied alternation proof

Lines 8909–9346 define the three conventions through the host interface, prove inclusions/duality, give exact simple/Emerson–Lei indices and a capture-stable Niwiński lower bound, and calculate all three source examples. Syntactic index calculations are expressly separated from semantic hierarchy strictness.

Lines 9348–10097 supply the semantic strictness proof:

1. At level one, nu-only tree languages are closed; a reachability mu witness has a nonclosed language.
2. A simultaneous class-generation induction builds open recursion graphs in fixed priority intervals. Capture-safe substitution and all four binder cases are explicit.
3. Local summaries remove internal moves without enlarging the interval; for n≥2, both terminal parities are totalized inside the interval.
4. The game formula W_n is a simple Sigma_n witness.
5. Padded transition trees give a prefix-gaining acceptance-to-game-tree map; stabilized prefixes provide a fixed tree.
6. A complement automaton at the same index yields the diagonal contradiction.
7. Duality and the full finite-model property transfer the exclusion to all three conventions, open competitors, and equivalence over finite systems.

No single finite model separating every competitor or index bound on the difference formula is asserted.

## Result and proof-standing ledger

The table records what is supplied in text. “Supplied” does not mean that an independent mathematical audit of every dependency has been completed.

| Lines | Identity or source result | Content | Current proof standing |
| --- | --- | --- | --- |
| 59–199 | Powerset fixed points, polarity/substitution and stabilization | Least/greatest characterization, duality, nested positivity and ordinal approximants | supplied proofs; transfinite-recursion/Hartogs background not independently audited |
| 377–429 | Kozen Figure 1 closure ordinal | Explicit omega+1 closure and DC-qualified well-founded-path characterization | supplied calculation and argument |
| 434–459 | PDL star/fixed-point identities | Reachability mu and invariance nu interpretations | supplied finite-path arguments |
| 249–287 | Kozen Proposition 3.2.3 | Seven-rule closure characterization of closed images | supplied proof |
| 311–345 | Kozen Lemma 3.3.3 and active-prefix fact | Transitivity of activity and retained enclosing prefix | supplied argument; later counter dependency |
| 461–476 | Kozen Proposition 4.1 | mu X.[a]X not expressible in PDL | supplied proof using cited/developed PDL filtration dependency |
| 478–748 | Kozen Proposition 4.2 | Single-model finite/cofinite PDL property including tests/converse/star, versus even-set mu property | supplied detailed word/automaton/formula-induction proof |
| 820–936 | Kozen Proposition 5.7 | Six derived fixed-point laws and consistency consequence | supplied equational derivations |
| 1200–1292 | Kozen Lemmas 6.2.6–6.2.7 | Individual counter event bound and nonmodal saturation | supplied proof with explicit lifetime/collision distinction |
| 1294–1424 | Finite configuration nonrejection algorithm | Safety greatest fixed point, decidability and examples | supplied both-direction proof and bound |
| 1426–1965 | Nonrejection-to-model construction | Six saturation conditions, parameterized truth lemma, finite configuration model and ancestor-backedge representation | supplied proof, with forward reference to bisimulation invariance |
| 1967–2370 | Context-counted aconjunctive completeness | Consistency iff A_M nonrejection iff finite model | supplied proof for changed cap M, not original cap N |
| 2384–2394 | thm:p09-kozen-full-completeness | Full finitary Kozen equational weak completeness | cited=Walukiewicz2000; source interfaces explained |
| 2441–2502 | Equational/finite-premise consequences and noncompactness | Weak versus local finite-premise versus arbitrary-premise distinction | supplied derivations from cited weak completeness; supplied counterexample |
| 2659–2817 | Streett-response record lemma | Streett word condition recognized by deterministic parity/Rabin monitor with h! factor and h+1 Rabin pairs | supplied proof including h=0 |
| 2819–3222 | Emerson–Jutla Theorem 2.2 conversion | Alternating Streett/Muller binary-tree acceptance to nondeterministic Pairs automata with explicit bounds | supplied construction/proof using finite-memory and deterministic trace-monitor dependencies |
| 3298–3705 | Emerson–Jutla Theorem 3.1 | Finite Streett formula automaton and accepting history-free strategies | supplied construction/proof with later parity-automaton/determinacy dependencies |
| 3707–3823 | Ordered-tree automata reverse translation/complement | Directional mu language required; EX/AX swap-invariance separator | supplied reduction and concrete counterexample |
| 3825–4156 | Emerson–Jutla Theorems 4.1–4.2 and Corollary 4.3 | Nested winning-region formulas with targets and parity determinacy | supplied proof via evaluation-game dependency; source/all-vertex targets separated |
| 4158–4264 | Emerson–Jutla Theorem 4.4 | Same choices on identical remaining labelled games | supplied quotient/lift proof using positional determinacy |
| 4289–4383 | Constrained reachability and safety-with-exit lemmas | mu/nu fixed-point characterizations | supplied rank and opposing-strategy proofs |
| 4266–4609 | Emerson–Jutla Theorem 5.2 | Countable-union-of-closed winning sets and determinacy via nested fixed points | supplied proof |
| 4611–4695 | Emerson–Jutla Theorem 5.1 | Bounded versus unbounded natural-color objectives | supplied proof with historical-maximum phases |
| 4756–4810 | Bisimulation invariance | All fixed-point formulas with coherent free-variable environments | supplied proof |
| 4812–4848 | Image-finite HML converse | HML/fixed-point equivalence iff bisimilarity under image-finiteness | supplied finite-conjunction proof |
| 4850–4889 | Tree-model unravelling | Satisfaction preserved by path unravelling, including open environments | supplied bisimulation proof |
| 4891–5077 | Evaluation-game truth theorem | Truth iff existential win; falsity iff universal win | supplied four-binder-case proof without positionality assumption |
| 5127–5415 | sec:p09-parity-positional-proof | ZFC positional determinacy of arbitrary set-sized total finite-priority arenas; model-checking positional conclusion | supplied transfinite proof |
| 5417–5525 | sec:p09-mu-contextual-truth | Linked raw-occurrence evaluation game agrees with contextual binder environment | supplied depth/first-exit proof |
| 5527–5718 | Bradfield–Stirling Theorems 3.1–3.2 | Same-structure well-founded pre-model equivalence | supplied contextual game proof |
| 5720–5974 | Ordinal trail certificate theorem | All paths even iff ordinal signature comparisons | supplied both-direction proof, DC and terminal cases explicit |
| 5976–6013 | Bounded-branching tree-model property | At most the number of diamond occurrences retained per state | supplied positional strategy pruning/unravelling proof |
| 6015–6265 | Modal parity automata, runs and Boolean closure | Game/run equivalence, complement, union, intersection and examples | supplied proofs |
| 6267–6674 | Formula-to-modal-parity-automaton direction | Every closed formula, including unguarded formulas, has a finite equivalent depth-one modal parity automaton | supplied construction, two-direction strategy proof and effective finite bound |
| 6859–6967 | Bekić identity and finite block elimination | mu and nu simultaneous systems scalarized with external parameters | supplied proof |
| 6676–7111 | Modal-parity-automaton-to-formula direction | Closed scalar formula in original vocabulary equivalent on arbitrary models | supplied product-control, Bekić and truth-induction proof |
| 7243–7380 | Cover modalities and cover-form acceptance | Dead-end identities and exact game semantics | supplied definitions and arguments |
| 7382–7546 | Trace monitor and Muller-parity record | Deterministic least-parity monitor for all good obligation traces | supplied bad-trace/record proofs plus Safra determinization dependency |
| 7565–7860 | Cover-form simulation | Every modal parity automaton has a finite cover-form equivalent on the same pointed model | supplied two-direction proof |
| 7862–7980 | ANF grammar and substitution preservation | Cover normal-form grammar and finite same-sign block closure | supplied grammar induction |
| 7982–8228 | Cover automata to guarded ANF | Closed guarded well-named ANF formula preserving acceptance in original vocabulary/model | supplied construction and parameterized scalarization proof |
| 8230–8266 | Janin–Walukiewicz Theorem 4.4 semantic normal form | Effective same-model equivalence from arbitrary closed formula to guarded ANF | supplied composed proof; explicitly not derivable-equivalence proof |
| 8268–8715 | Janin–Walukiewicz Theorem 4.6 cut reduction | Guarded ANF satisfiable iff its cut is satisfiable; finite reconstructed model | supplied occurrence-game and finite-model proofs |
| 8717–8821 | ANF linear decision and full finite-model property | O(n) ANF decision under stated representation; effective full-calculus satisfiability/FMP | supplied proof with explicit representation/normalization boundary |
| 8929–9137 | Alternation inclusions, duality and S/EL membership | Exact structural/fragment indices for simple and Emerson–Lei conventions | supplied class-generation arguments, host definitions outstanding |
| 9139–9192 | Niwiński dependency lower bound | Class membership bounds dependency-chain sign costs | supplied necessary-condition induction, not full decision algorithm |
| 9194–9346 | Three source alternation examples | Exact (s,p,d) triples and A1/A2 semantic distinction | supplied membership/nonmembership proofs and explicit model |
| 9406–9482 | First-level semantic strictness | W1 in simple Sigma1 has nonclosed tree language; no Niwiński Pi1 equivalent | supplied topology/approximant proof |
| 9484–9812 | Niwiński class to fixed-index binary automata | Sigma_n and Pi_n generation preserves required priority intervals; constants totalized for n>=2 | supplied generation/strategy/local-summary proof |
| 9814–9940 | Separating game formulas and acceptance encoding | W_n in simple Sigma_n and game-tree encoding of any matching-index automaton | supplied semantics/index argument |
| 9348–10097 | Semantic alternation hierarchy strictness | For every n>=1, a closed simple Sigma_n witness has no Niwiński Pi_n equivalent, also over finite systems | supplied first-level/topological and higher-level fixed-index/diagonal proofs |

Every remaining subsection/paragraph is listed in the heading catalogue below and described by its containing read-group in JSON.

## Cross-file dependencies and additional card promises

All twelve explicit ref targets in N18 resolve to the current file or the inspected host/Safra interfaces. Nine are local, now fully read; the three external targets are `def:p09-mu-calculus`, `thm:p09-mu-alternation`, and `sec:p09-safra-determinization`.

The Safra dependency was read at `n-c-013.tex:965–1223`: it has the explicit construction, rejecting empty-root sink, n Rabin pairs, correctness arguments and 2^O(n log n) count used by N18. It is attributed to the expanded Safra manuscript, not to the unread 1988 proceedings text. Its deep lineage invariants were not independently re-proved in this inventory.

The PDL filtration dependency was read at `n-c-021.tex:82–209`: it defines test-containing programs, finite closure, quotient atomic edges containing original edge images, and the truth-preservation argument required by the ordinary PDL separation. This is a checked textual dependency interface, not a new proof audit of every mutual-induction clause.

The P8 system card also asserts sharp full-language EXPTIME satisfiability, polynomial parity-game equivalence/quasipolynomial model checking, and one-program CTL*/LTL embeddings and strict extension. These are cited card claims. N18's large effective constructions do not supply every sharp complexity bound, and its complete text contains no explicit CTL* embedding/strictness construction. The inspected N16 paragraph at 2115–2150 instead supplies LTL-to-CTL* lifting and CTL*/CTL/LTL separation. The precise source attribution and required presentation scope of the additional card claims remain to be matched; a citation by itself is not classified as a missing-proof defect.

## Remaining completion obligations

1. **Original Kozen cap.** Preserve the separate standing of the original N=2^m threshold. The supplied M-cap proof does not establish it.
2. **Imported tree convention.** Determine the exact source meaning of “tree-like”; the local theorem proves only its explicitly allowed ancestor/self-backedge form and permits nested/crossing edges.
3. **Source states.** Keep the 2005 Bradfield–Stirling preprint and expanded Safra dependency distinct from their registered publication bodies; full source-by-source identity is not certified.
4. **Cited interfaces.** Keep Walukiewicz's deductive bridge separate from semantic ANF, and keep sharp complexity/CTL* card claims on exact source support. Whether the compendium requires a larger local source presentation is a separate scope/source determination.
5. **Independent correctness review.** The long counter, strategy, monitor, cover, cut and alternation chains are now completely inventoried as written. This reading does not independently verify every mathematical premise or deep source invariant; the finite generic transition-layer convention noted above is among the checks to retain.

These are distinct from already supplied arguments. No source grammar, finite-model theorem or alternation proof is declared absent merely because an older progress note called it a sketch.

## Complete heading catalogue

Intervals end at the next subsection/subsubsection/paragraph heading. Nested italic sublemmas are covered by their containing paragraph and the result/read-group ledgers. All these intervals were read in the sequential coverage below.

| Lines | Heading level | Actual heading |
| --- | --- | --- |
| 3–5 | subsection | Three modal-\(\mu\) source presentations |
| 6–23 | subsubsection | Kozen's modal calculus and aconjunctive fragment |
| 24–58 | paragraph | Environments and denotations. |
| 59–104 | paragraph | Least and greatest fixed points. |
| 105–157 | paragraph | Polarity, parameters, and substitution. |
| 158–200 | paragraph | Transfinite approximants and stabilization. |
| 201–376 | paragraph | Closed source formulas and active variables. |
| 377–433 | paragraph | A closure ordinal beyond \(\omega\). |
| 434–525 | paragraph | The PDL comparison. |
| 526–749 | paragraph | Finite/cofinite sets under regular programs. |
| 750–777 | paragraph | The source calculus. |
| 778–819 | paragraph | Soundness of the calculus. |
| 820–951 | paragraph | Derived fixed-point laws. |
| 952–1293 | paragraph | The restricted tableau and its theorem. |
| 1294–1425 | paragraph | Deciding nonrejection on the configuration graph. |
| 1426–1577 | paragraph | From nonrejection to a model. |
| 1578–1716 | paragraph | Saturation of the ordinal-closed labels. |
| 1717–1878 | paragraph | The general truth lemma. |
| 1879–1966 | paragraph | A finite directed model and an explicit backedge depth. |
| 1967–1985 | paragraph | A context-counted completeness construction. |
| 1986–2143 | paragraph | Closed annotations and local consistency. |
| 2144–2229 | paragraph | Context signatures across modal steps. |
| 2230–2293 | paragraph | Counting excludes overflow. |
| 2294–2376 | paragraph | Completeness and the resulting finite bounds. |
| 2377–2440 | paragraph | Completeness of the full calculus. |
| 2441–2475 | paragraph | Equations, consistency, and finite premises. |
| 2476–2503 | paragraph | Why the completeness statement is weak. |
| 2504–2513 | subsubsection | Emerson--Jutla's tree-automata and determinacy presentation |
| 2514–2577 | paragraph | Nondeterministic and alternating binary-tree games. |
| 2578–2658 | paragraph | Total presentations and their parameters. |
| 2659–2818 | paragraph | A record for Streett responses. |
| 2819–2920 | paragraph | Finite memory before collecting threads. |
| 2921–2991 | paragraph | The deterministic monitor for all augmented threads. |
| 2992–3054 | paragraph | The nondeterministic state and transition. |
| 3055–3151 | paragraph | Every ithread is represented. |
| 3152–3223 | paragraph | Counting the construction. |
| 3224–3297 | paragraph | Binary-tree semantics and formula closure. |
| 3298–3413 | paragraph | Local unfolding and the formula automaton. |
| 3414–3519 | paragraph | Terms and the three transition layers. |
| 3520–3596 | paragraph | Equivalence of the layered and Boolean games. |
| 3597–3706 | paragraph | Streett pairs and the strategy theorem. |
| 3707–3824 | paragraph | The reverse translation retains the tree directions. |
| 3825–3881 | paragraph | Parity fixed points and determinacy. |
| 3882–3958 | paragraph | Target parameters and the nested formulas. |
| 3959–4072 | paragraph | Proof of the two characterizations. |
| 4073–4129 | paragraph | Duality and pure parity determinacy. |
| 4130–4157 | paragraph | Targets at every vertex. |
| 4158–4265 | paragraph | Identical remaining game trees. |
| 4266–4288 | paragraph | The two on-line-game applications. |
| 4289–4384 | paragraph | Constrained reachability and safety with an exit. |
| 4385–4422 | paragraph | The complementary nested regions. |
| 4423–4467 | paragraph | Player I's decreasing sequence of phases. |
| 4468–4538 | paragraph | Closed winning sets as prefix predicates. |
| 4539–4610 | paragraph | Player II's sequence of exclusions. |
| 4611–4696 | paragraph | Bounded and unbounded natural colors. |
| 4697–4704 | subsubsection | Bradfield--Stirling's semantic and alternation synthesis |
| 4705–4755 | paragraph | Labelled systems and the modal language. |
| 4756–4811 | paragraph | Bisimulation preserves fixed-point truth. |
| 4812–4849 | paragraph | The image-finite converse. |
| 4850–4890 | paragraph | Unravelling gives a tree model. |
| 4891–4971 | paragraph | The complete model-checking game. |
| 4972–5078 | paragraph | Truth and winning strategies. |
| 5079–5126 | paragraph | Finite arenas and two basic examples. |
| 5127–5374 | paragraph | Positional determinacy, including infinite arenas. |
| 5375–5416 | paragraph | Returning to the least-recurring convention. |
| 5417–5526 | paragraph | Binding contexts for annotated subformulas. |
| 5527–5632 | paragraph | Locally consistent pre-model annotations. |
| 5633–5719 | paragraph | The pre-model truth theorem and its converse. |
| 5720–5791 | paragraph | Ordinal certificates for the trail condition. |
| 5792–5898 | paragraph | Constructing the ordinal signatures. |
| 5899–5975 | paragraph | Resets, limit ranks, and pre-model certification. |
| 5976–6014 | paragraph | A bounded-branching tree model. |
| 6015–6071 | paragraph | Modal alternating parity automata. |
| 6072–6163 | paragraph | Runs and simultaneous successor obligations. |
| 6164–6214 | paragraph | Boolean operations on modal automata. |
| 6215–6266 | paragraph | Two small acceptance calculations. |
| 6267–6314 | paragraph | From arbitrary formulas to guarded automata. |
| 6315–6379 | paragraph | Finite local games and their Boolean summaries. |
| 6380–6412 | paragraph | The transition construction. |
| 6413–6445 | paragraph | The block-minimum lemma. |
| 6446–6507 | paragraph | Correctness: from evaluation to acceptance. |
| 6508–6592 | paragraph | Correctness: from acceptance to evaluation. |
| 6593–6621 | paragraph | Unguarded loops and the two uses of priority. |
| 6622–6675 | paragraph | Finiteness and effective construction. |
| 6676–6688 | paragraph | From modal automata back to formulas. |
| 6689–6858 | paragraph | A formula with explicit finite control. |
| 6859–6968 | paragraph | Eliminating a simultaneous fixed point. |
| 6969–7112 | paragraph | Removing the control coordinate. |
| 7113–7161 | paragraph | A direct equation-system description. |
| 7162–7242 | paragraph | Two calculations with fixed-point blocks. |
| 7243–7304 | paragraph | Cover modalities. |
| 7305–7381 | paragraph | Cover-form automata and their games. |
| 7382–7476 | paragraph | A finite monitor for all obligation traces. |
| 7477–7564 | paragraph | From the Muller condition to least parity. |
| 7565–7681 | paragraph | Converting an arbitrary modal automaton to cover form. |
| 7682–7775 | paragraph | Why the cover simulation accepts every original model. |
| 7776–7861 | paragraph | Why a cover strategy satisfies the original obligations. |
| 7862–7981 | paragraph | The automaton normal-form grammar. |
| 7982–8105 | paragraph | From cover automata to guarded ANF. |
| 8106–8229 | paragraph | ANF component bodies and scalarization. |
| 8230–8267 | paragraph | The semantic normal-form theorem. |
| 8268–8307 | paragraph | Cutting a guarded normal form. |
| 8308–8369 | paragraph | The finite local satisfiability calculation. |
| 8370–8465 | paragraph | A finite game on normal-form occurrences. |
| 8466–8534 | paragraph | Why satisfiability survives the cut. |
| 8535–8633 | paragraph | Restoring greatest-fixed-point returns. |
| 8634–8716 | paragraph | Truth in the reconstructed finite model. |
| 8717–8795 | paragraph | Size bounds and the decision procedure. |
| 8796–8822 | paragraph | The finite-model and decidability consequences. |
| 8823–8908 | paragraph | Examples and the role of the hypotheses. |
| 8909–8971 | paragraph | The three alternation conventions. |
| 8972–9020 | paragraph | Duality and the first level. |
| 9021–9080 | paragraph | Exact simple-class indices. |
| 9081–9138 | paragraph | Closed fragments for Emerson--Lei. |
| 9139–9193 | paragraph | A capture-stable dependency lower bound. |
| 9194–9347 | paragraph | Three exact class calculations. |
| 9348–9405 | paragraph | Semantic strictness and binary-tree witnesses. |
| 9406–9483 | paragraph | The first level. |
| 9484–9609 | paragraph | Open recursion graphs at a fixed index. |
| 9610–9689 | paragraph | Binding at the bottom priority of an interval. |
| 9690–9813 | paragraph | Removing internal moves without adding an index. |
| 9814–9869 | paragraph | Game formulas at the separating levels. |
| 9870–9941 | paragraph | Encoding acceptance as a binary game tree. |
| 9942–10043 | paragraph | The prefix fixed point and diagonal contradiction. |
| 10044–10097 | paragraph | Other conventions and finite transition systems. |

## Sequential reading record

Every interval below returned fully numbered text without truncation and the same file hash. Their union is exactly 1–10,097 with neither gaps nor overlaps. The exact next unread line is null.

| Read interval | SHA256 | Evidence status |
| --- | --- | --- |
| 1–250 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 251–500 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 501–800 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 801–1150 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 1151–1500 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 1501–1850 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 1851–2200 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 2201–2550 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 2551–2900 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 2901–3300 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 3301–3650 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 3651–4050 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 4051–4450 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 4451–4800 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 4801–5200 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 5201–5550 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 5551–5950 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 5951–6350 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 6351–6750 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 6751–7150 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 7151–7550 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 7551–7950 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 7951–8350 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 8351–8750 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 8751–9150 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 9151–9550 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 9551–9950 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |
| 9951–10097 | `3BF52D9B5B7767231FBADD624ABB42D1BE1EB54754C527C8D22667539FAEDC49` | Fully read; output not truncated |

Hashes and intervals for the separately inspected host, rule-sheet and proof dependencies are in the JSON. The final source-file hash again matched after the entire reading and dependency inspection. The two output files are the audit deliverables; no manuscript mutation accompanies this inventory.
