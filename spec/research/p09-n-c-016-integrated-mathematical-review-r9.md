VERDICT: ACCEPT

# N-c-016 Round 9 mathematical/definedness review

## Decision

No line-specific mathematical or definedness must-fix remains in the frozen current presentation. The acceptance is limited to the actual 2,070-line LaTeX source and the authorized host, prerequisite, source-note, acquisition-note, and bibliography text listed below. It is not a publication, source-fidelity, visual, compilation, or historical-source verdict.

## Bounded positive evidence

### 1. Clarke--Emerson: domains, formula types, graph constructions, and factorization

- Lines 41--60 type the source structure, process-indexed transition relations, their total union, infinite paths, and the computation-tree unfolding before any of those objects are used semantically. Lines 62--124 then give the indexed CTL grammar and typed state-satisfaction clauses, including strong current-inclusive until and the distinction between potentially vacuous AX_i and total unindexed EX. The state/path and per-process/global distinctions are therefore explicit rather than inferred.
- Lines 127--183 type the two finite-state approximation sequences, state which recurrence is printed and which is reconstructed, give the correct least-growth directions, justify stabilization on finite S, and identify the omitted f_1 guard in the source display without copying that defect. Lines 199--234 retain the finite-structure scope of the infinitely-often SCC result and give the Hamiltonian reduction on the explicit base domain n >= 1, with fresh states, totalizing sink loop, exact labels, both logical directions, and only the source-supported NP-hardness conclusion.
- Lines 236--318 keep the satisfiability procedure at its published outline strength. Blocks is defined by its closure conditions; Tiles is reported only at the level actually printed by the source, with its incomplete general process-indexed definition expressly disclosed. The worked tableau is not promoted into a general correctness proof.
- Lines 320--394 quantify the mutual-exclusion requirements, distinguish process indices i and j, preserve the enabledness guard that prevents vacuous AX_i satisfaction, and correctly observe that requirement group 9 is redundant under the already declared total union relation while retaining it as source material.
- Lines 396--416 define a model fragment as a finite construction artifact rather than a complete model, distinguish its role in eventuality-safe cycle closure, and explain why TURN is a state-label component required by later factorization rather than a temporal operator.
- The factorization at lines 441--497 is now mathematically local and total. For every duplicated propositional label of multiplicity d >= 2, lines 443--458 give a total discriminator with domain {0,...,d}, exactly one equality at every node, explicit initialization at every initial node, and a target-determined assignment on every global arc. Lines 460--470 condition the rule on every global i-arc preserving every other process's region and explain both why requirement group 8 supplies that premise in the worked two-process construction and why a violating arc cannot be represented as a local P_i transition.
- Within that valid locality scope, lines 471--480 type gamma_e as a source-state formula guard and sigma_e as a complete auxiliary-variable update map. The guard removes only P_i's own source-region atom, retains every other region and auxiliary equality, and declares an empty conjunction true. The update map treats every absent assignment as identity. Lines 481--495 quantify the source and target regions and restrict each disjunction to a nonempty realized update class; they merge only identical complete update maps, leaving identity and nonidentity updates as distinct parallel transitions. This closes the former risks of cross-process region updates, partial-update ambiguity, and guard/update conflation.
- Lines 499--511 keep four evidentiary strengths separate: the finite labeller and its bound, proved propositions, the abridged tableau outline, and the worked synthesis/factorization construction without a separately stated general correctness theorem.

### 2. Queille--Sifakis: declaration order, finite families, executions, and transformer algebra

- Lines 525--544 define the IPN, its retained program-variable vector bold X, guarded commands, firing semantics, and omitted-inscription convention before use. Lines 556--562 separately declare scalar X as the sender's data value before the first occurrence of the message pair (X,Y). Lines 572--590 then define the message copies, field projection, process identifiers, and every action label subsequently used. The IPN vector and the example scalar are neither conflated nor retroactively declared.
- Lines 592--597 correctly keep permanent non-loss outside the printed transition model: the true-guarded loss branches can be selected forever and no fairness clause is silently supplied.
- Lines 599--655 define the state-formula language, maximal finite or infinite execution domain, actual-position set D_s, and all four temporal clauses. The clauses quantify only over positions where a Q-valued state exists, so the fictitious post-terminal omega is never incorrectly asked to satisfy a state formula. The manuscript explicitly labels the start/adjacency clauses as a reader-facing completion of a source omission.
- Lines 665--701 define enable and after as unlike atomic state predicates, quantify finite action families for every k in N, and state the nullary disjunction and conjunction values. Hence empty action lists, actionless processes, and the vacuous conjunction of zero liveness obligations all have determinate truth values. Lines 721--785 preserve the logical directions: liveness and response formulas concern possible or inevitable future enabledness, not actual execution or fairness.
- Lines 787--849 type pre, its Boolean dual, Id, transformer composition, pointwise union and intersection, and both finite-iterate operators as maps on P(Q) before the four equations use them. The manuscript does not mistake the source superscript x for an unexplained fixed-point binder or assert a descending chain for an arbitrary transformer. The source's image-finiteness hypothesis is retained for all four equations; the sink behavior of dual-pre and the existential-pre factor in INEV are explained; and the proofs remain explicitly delegated to the cited 1979 report.
- Lines 851--914 keep the analyzer outline, one worked computation, iteration-cap failure, supported variable representations, and absence of a general asymptotic or total-answer theorem separate. A capped approximation is not reported as a proof.

### 3. Emerson--Halpern: structure classes, state/path ownership, and proof repairs

- Lines 927--1004 define the nonempty state and path sets, finite/infinite suffix convention, branching and linear truth types, suffix closure, model validity, and strong equivalence in declaration order. The shared Lamport glyphs are not used as if they already possessed the later CTL* state/path typing.
- Lines 1006--1059 explicitly type finite, nonempty finite, and infinite strings; bound every fusion and limit component; restrict decompositions to well-formed nonempty paths; and state that suffix, fusion, and limit closure are path-set properties. Lines 1029--1046 define R-generability by exact equality with all infinite paths of a total relation on S. The equivalence correctly includes state completeness: total R generates a path from every state, so the three closure conditions alone would be insufficient on an ambient S containing unused states. The subsequent prose identifies the distinct use of fusion, limit, and state-completeness hypotheses.
- Lines 1061--1153 give mutually typed CTL* state and path grammars before any fragment comparison. Only A/E return a path assertion to a state assertion; temporal path clauses retain the current-position, finite-last-state, and all-sequences-versus-X distinctions. The fragment names also distinguish state-level Boolean closure from path-level Boolean closure.
- Lines 1155--1207 distinguish the metalinguistic associated-language constructor B(L), whole-model strong equivalence, and pointwise state-formula equivalence. Proposition 4's fusion-closed, state-complete class is defined before use, and the two hypotheses' nonredundancy is witnessed separately.
- Lines 1209--1270 fix the R-generable structure class for the expressiveness diagram, state every strict/equality edge and the incomparability convention, and restrict the Appendix's segment notation to positive arity with an explicit n = 1 base case.
- Lines 1272--1375 preserve the logical and evidentiary repairs to Theorems 5--9. The literal B(L(...)) targets of Theorems 5--6 are first recorded as self-defeating, then distinguished from the proof-supported B(F,...) targets. Lines 1300--1308 now say exactly that the EXq, E[q U r], and A[q U r] cases are printed while atomic, conjunction, and negation cases are left to the reader, and they identify Theorem 8(a), not Theorem 9, as the required Boolean-path elimination. Theorem 6's repeated induction, Theorem 7's Boolean cases, and Theorems 8--9's cited status remain explicit.
- Lines 1390--1483 keep the PL translation's unprinted induction, the literal MPL U/X defects, the closure lemmas, and the unproved Theorem 10 boundary separate. Lines 1485--1511 type the terminal-server atoms and its CTL* state formula, establish the actual use of existential alternatives, and limit the conclusion to an application argument rather than a general model-checking, complexity, or synthesis theorem.

### 4. Clarke--Grumberg--Peled acquisition limit

- Lines 1513--1534 make no content-strength claim from the unacquired 1999 first-edition body. Preview and contents metadata are used only for locators; restricted lending, a different handbook chapter, a different survey, the second edition, and Baier--Katoen are not substituted for the missing source. The host complexity theorem retains independent citations. This is consistent with the controlling acquisition note's explicit prohibition on attributing an exact grammar, algorithm, proof, example, or complexity statement to the 1999 book.

### 5. Baier--Katoen: host bridge, fixed points, witnesses, and complexity

- Lines 1547--1571 define the six-component action-labelled source tuple, finiteness, successor sets, terminality, and the no-terminal-state condition. Lines 1573--1586 then define the action-forgetting binary relation R_0 and valuation V_0 with their metalinguistic standings, and identify the host proposition alphabet with AP.
- Lines 1588--1610 declare every source CTL constructor before defining the recursive translation tr, including both quantified-next and both quantified-until forms. Lines 1612--1617 state its necessity, source/host distinction, and exact finite-nonempty host domain. Lines 1618--1634 prove the predecessor correspondence, guard the host instantiation by S nonempty, treat S empty separately with empty satisfaction sets and vacuous system truth, and distinguish K action-labelled transition triples from the at-most-K binary edges of R_0. The empty-state bridge therefore neither violates the prerequisite's S != empty requirement nor drops the source's permitted vacuous system case.
- Lines 1636--1696 distinguish maximal fragments from initial paths and give the detailed CTL state/path grammar and semantics. Lines 1698--1716 state the bridge induction only after those source clauses are available, and the host bound uses |R_0| and |tr(Phi)| rather than silently identifying them with source K and |Phi|.
- Lines 1718--1732 preserve the potentially exponential ENF materialization warning. Lines 1734--1782 state least and greatest set characterizations with the inclusion order, give the correct fixed-point directions, preserve the no-terminal semantic convention, and identify recursive choice versus the finite-cycle specialization. Lines 1784--1851 distinguish the naive Algorithm 14 loops, monotone simultaneous chains, Algorithms 15--16 worklists, their typed count invariant, and the handbook's explicit global induction from what the book labels as a theorem proof.
- Lines 1853--1902 define every state label, Boolean comparison abbreviation, edge, initial state, satisfaction set, and both fixed-point example results. The abbreviations add no hidden state-variable sort.
- Lines 1904--1918 retain every representation-sensitive condition for Theorem 6.30: finite no-terminal source system, N states, K action-labelled transitions, predecessor linked lists, direct treatment of modalities, and no separate source-stated space theorem.
- Lines 1920--1979 make the Hamiltonian example total and defined at its base: n >= 1, a fresh sink b, AP = V, I = V, a singleton recursion base, recursion only for 2 <= k <= n, and a nonempty permutation family. Both directions of the satisfaction equivalence are stated. The manuscript also correctly identifies the missing uniform-construction premise in the source's P = NP aside rather than promoting mere polynomial-size existence into a uniform algorithm.
- Lines 1981--2016 separate the n = 0 witness systems from the n > 0 inductive family, avoiding the source's undefined negative index, and retain the reader-left bounded-formula induction. Lines 2018--2053 restore CTL* state/path ownership, use a well-typed state formula for strictness, and label the atom-substitution step as an omitted reconstruction. Lines 2055--2070 inventory the remaining printed defects and close with the exact source-versus-handbook proof boundary.

### 6. Host and prerequisite consistency

- The prerequisite at handbook/parts/p08/temporal-epistemic-supplement.tex lines 46--55 requires a nonempty carrier, total binary relation, typed valuation, and infinite paths. Lines 58--104 give the host CTL state grammar and strong-until semantics; lines 129--164 give the mutually typed CTL* state/path grammar and semantics. The N-c-016 bridge respects each of these domains and ownership rules.
- The host at handbook/parts/p09/logic-in-computer-science.tex lines 948--972 types both predecessor maps on P(S). Lines 974--1007 type the mu/nu bound variable as a state set, give the correct least/greatest directions and iteration bases, and return a global satisfaction set. Lines 1009--1017 state the finite-total correctness and adjacency-list/worklist bound. The source presentation's R_0, V_0, tr, and nonempty-domain guard therefore instantiate the actual host method rather than a nearby but differently typed algorithm.
- Host lines 1019--1035 keep CTL/LTL expressiveness and four CTL/CTL* complexity problems distinct, and lines 1517--1521 place this presentation at the expected host location. Nothing in N-c-016 attributes those host classifications to the unacquired 1999 body.

### 7. Supplied technical-name rule

The presentation does not introduce a new technical name as an unexplained hypothetical answer. The principal names satisfy necessity, eliminable definition or explicit source standing, category, nonredundancy, and actual use at their introduction sites:

- synchronization skeleton and global system flowgraph at lines 20--39, with the latter fully constructed at lines 441--497;
- model fragment and TURN at lines 396--416;
- interpreted Petri net at lines 525--544;
- enable and after at lines 665--673;
- suffix/fusion/limit closure, R-generability, and state completeness at lines 983--1050;
- the CTL* state/path categories at lines 1061--1083;
- the associated-language construction B(L) and the two equivalence relations at lines 1155--1207;
- MPL stage at lines 1413--1419;
- the R_0/V_0/tr host bridge at lines 1573--1617; and
- the Boolean comparison abbreviations at lines 1876--1888.

Where the source itself withholds a complete artifact, the manuscript does not falsely close it under a new name: Tiles is explicitly limited to the published example at lines 249--306, diagnostics has no invented format at lines 551--553, and the 1999 body contributes no content-level terminology at lines 1513--1534.

## Explicit non-claims

- ACCEPT does not assert that every cited external theorem has been reproved in the presentation. Reader-left, citation-only, reconstruction, outline, and handbook-supplied steps remain identified at their actual locations.
- ACCEPT does not convert the Clarke--Emerson tableau outline or synthesis example into a general printed correctness theorem, the CESAR architecture into a total decision procedure or complexity theorem, the Emerson--Halpern expressiveness article into a model-checking algorithm, or Baier--Katoen's CTL material into a CTL* model-checking result.
- ACCEPT makes no mathematical-content claim from Clarke--Grumberg--Peled 1999 beyond the acquisition boundary and bibliographic/locator metadata authorized by its note.
- ACCEPT is not evidence of TeX compilation, cross-reference resolution, typographic layout, rendered-page quality, source-image identity, independent publication verification, or executable reproduction.

## Substantive text read

- handbook/parts/p09/presentations/n-c-016.tex lines 1--2070, complete through EOF.
- handbook/parts/p09/logic-in-computer-science.tex lines 945--1036 and 1500--1525.
- handbook/parts/p08/temporal-epistemic-supplement.tex lines 42--190.
- spec/research/p09-clarke-emerson-1981-source-note.md lines 1--884, complete through EOF.
- spec/research/p09-queille-sifakis-1982-source-note.md lines 1--867, complete through EOF.
- spec/research/p09-emerson-halpern-1986-source-note.md lines 1--729, complete through EOF.
- spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md lines 1--470, complete through EOF.
- spec/research/p09-baier-katoen-2008-ch6-source-note.md lines 1--1120, complete through EOF.
- handbook/bib/handbook.bib lines 2393--2407, 2409--2422, 2424--2436, 2438--2447, 2449--2458, 4815--4824, 4826--4835, 4837--4846, and 4897--4906.
- The technical-name rule supplied as AGENTS.md instructions in the task prompt.

## Prohibitions observed

- I did not open any prior N-c-016 review or report, including my own prior work, any source-fidelity or publication report, any board/admission/history file, any parent conclusion, or any other agent output.
- I did not contact, inspect, or delegate to another agent. I did not use prior-run memory.
- I did not inspect a PDF, render, screenshot, page image, or historical publication file, and I did not browse the web.
- I did not run a TeX or handbook build, test, checker, validator, hash, executable source system, or repository/script file. Only direct plain-text reads, a non-content existence check for the designated output, and the authorized report edit were performed.
- I modified no manuscript, bibliography, note, or other repository file. The only written output is this Round 9 report.

REGISTER STATUS: OPEN
