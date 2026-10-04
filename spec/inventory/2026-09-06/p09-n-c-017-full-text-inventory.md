# N-c-017: complete sequential text inventory

The full active N-c-017 presentation has been read: **all 3,715 lines**, in 13 consecutive numbered, non-truncated intervals. It contains substantial mathematical presentations for Bryant, Burch et al., Biere–Cimatti–Clarke–Zhu, and Clarke et al. The separately registered **revised McMillan 1993 book presentation remains explicitly absent**.

This completes the assigned reading inventory. It does not certify every proof independently or establish full source-presentation completion. No manuscript, source, register or bibliography was changed.

## Scope and reading evidence

- Manuscript: [handbook/parts/p09/presentations/n-c-017.tex](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex).
- SHA256 at the initial reading, every subsequent interval and final read: `C37A5684B92B078EF44E9B751876891C51D12D8CF0027F573A76F0FDCABFA464`.
- Size: 159,140 bytes; 3,715 lines.
- Fully read intervals: 1–250, 251–500, 501–800, 801–1100, 1101–1400, 1401–1700, 1701–2000, 2001–2300, 2301–2600, 2601–2900, 2901–3200, 3201–3500, 3501–3715.
- Coverage: no gaps or overlaps; no truncated reading output; next unread line: **none**.
- Finalized: 2026-09-07 09:17:23 UTC.
- Active route: [handbook/main.tex:33](C:/Dev/the-methods-of-reason/handbook/main.tex:33) → [handbook/parts/p09.tex:3](C:/Dev/the-methods-of-reason/handbook/parts/p09.tex:3) → [handbook/parts/p09/logic-in-computer-science.tex:1535](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:1535) → N-c-017.
- The accompanying JSON preserves all interval hashes, 57 headings, 39 mathematical result/algorithm entries, seven bounded dependency readings, original requirement fields, and the remaining obligations.

The text was read sequentially before headings and references were extracted for reconciliation. Primary PDFs were not re-read during this bounded manuscript inventory. Source identities and edition distinctions below are the explicit current manuscript/bibliography scope, not a new audit of the held bytes. No acquisitions, tests, builds or manuscript renders were performed.

## Original requirement and current scope

[Original N-c-017 row](C:/Dev/the-methods-of-reason/spec/registers/new-content.csv:124) requires “symbolic model checking: BDDs and Bryant canonicity, fixpoint computation, bounded model checking via SAT, CEGAR pointer,” names Bryant 1986, Burch et al. 1992, McMillan 1993, Biere–Cimatti–Clarke–Zhu 1999 and Clarke et al. 2003, and historically notes “BDD canonicity at T level; industrial context one paragraph; cross-listed with D-P11-009.”

Those historical treatment ceilings are not applied as current limits. The source-specific presentation requirement and the actual manuscript promises remain visible. [D-P11-009](C:/Dev/the-methods-of-reason/spec/registers/depth-gaps.csv:136) has historical source part XI but **target P12**; it is not an extra P9 row. Its active P12 ROBDD definition and cited canonicity statement were read at [handbook/parts/p12/sat-and-certificates.tex:122](C:/Dev/the-methods-of-reason/handbook/parts/p12/sat-and-certificates.tex:122) through line 154.

## Source presentations and actual content

| Source and actual range | Mathematical text now supplied | Current standing |
|---|---|---|
| [Bryant, 6–591](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:6) | Fixed-order reduced graphs; canonicity and minimality; reduction; Apply, restriction, quantification, equality and Compose; assignment finding/listing/counting; exact order-sensitive graph counts; symmetry and multiplication lower bound; ALU account. | Substantial supplied arguments and exact examples. The declared source is the annotated electronic author version. |
| [Burch et al., 592–1626](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:592) | Relational fixed-point language, denotations and recursive BDD evaluators; Boolean-domain encoding; symbolic CTL; transitive closure and restricted iterative squaring; nested fixed points; fair paths; symbolic LTL tableau; strong/weak equivalence; Büchi containment; pipeline assertions and experiment. | Substantial supplied constructions and semantic proofs. Relational and modal fixed-point calculi are distinguished. |
| [McMillan, 1627–1640](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:1627) | Source boundary only. The revised 1993 book's SMV syntax, partitioned-transition algorithms, examples and proofs are expressly outside the supplied technical source basis. | Definite missing registered source presentation. The May 1992 thesis CMU-CS-92-131 is a separate record and cannot establish the 1993 book presentation. |
| [Biere et al., 1641–2593](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:1641) | All no-loop and selected-loop SAT clauses; bounded soundness and correspondence; successive horizons; shift-register calculation; several stopping bounds; arbitrary-LTL Büchi-product bound; F/G witness construction; separately supplied branching ECTL certificates; experimental qualifications. | Source locators refer to the complete January 1999 CMU report, not an asserted LNCS facsimile. The ECTL certificate construction is expressly handbook-owned. |
| [Clarke et al., 2594–3715](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:2594) | Simulation and ACTL* preservation; exact/early/combined abstraction; guarded programs; atom and product quotients; path/lasso validation; product-refinement hardness; slice-based PolyRefine; exact and combined-policy termination; industrial account. | Full JACM article distinguished from preliminary CAV 2000. Completeness is explicitly restricted to fragments admitting finite-path or lasso refutations. |

### Bryant: supplied proof and algorithm boundaries

[Lines 59–109](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:59) supply existence, uniqueness including shared subgraphs, and minimum size under one fixed variable order. Reduction is an actual bottom-up algorithm with an invariant and worked IDs, not just a canonicity citation. Its comparison-sorting cost is distinguished from stronger implementation assumptions. Apply and Compose likewise charge construction, memoization and reduction separately.

The residual argument gives the exact interleaved/separated counts and handles constant/zero-variable cases. Parity and symmetric-function bounds are distinguished. The multiplication proof at [482–559](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:482) quantifies over every order and then chooses a hard output bit; it does not claim every bit is hard. Satisfying-assignment counts include skipped levels and distinguish arithmetic-operation counts from bit complexity. The ALU table reports source observations rather than ordering optimality or a general running-time guarantee.

### Burch: fixed points, fairness and automata

The relation language at [608–752](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:608) defines the two variable sorts, positive-arity relation terms, freshness conditions and finite-domain evaluation. A Boolean-vector surjection can represent one state several times; the encoding proof addresses that case.

The full iterative-squaring formulas at [881–1040](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:881) apply to `F(X)=B ∪ Post_K(X)` on a finite domain with fixed seed and kernel. The text proves both fixed-point identities and gives counterexamples to unrestricted use on infinite domains or arbitrary monotone bodies such as universal predecessor. Logarithmically many squaring rounds do not imply polynomial or improved BDD running time.

Fair-path proofs include an empty fairness family, fixed predicate interpretation and positive continuation. The LTL tableau at [1206–1347](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:1206) supplies local predicates, transitions, fairness, a truth lemma and converse. Its transition relation may have dead ends; arbitrary totalization would change the construction. Weak equivalence is divergence insensitive. Containment requires a complete deterministic specification automaton, with explicit examples explaining the restriction. The pipeline passage proves future-bit uniqueness before replacing its path assertions by the displayed state assertions.

### Bounded model checking: exact clauses and later constructions

The complete translations at [1725–1866](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:1725) include no-loop release endpoints, wrapped until/release witnesses, the lasso's forever-right release case, and the `k=ell=i=0` case. No-loop semantics is a finite-witness underapproximation, so infinite-path dualities are not silently applied to it. The SAT proof distinguishes soundness at every horizon from completeness at some horizon.

Stopping arguments distinguish recurrence diameter, ordinary shortest-path diameter, safety reachability, existential persistence, and formula-product bounds. The arbitrary-LTL bound at [2212–2261](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:2212) includes all acceptance-tracking states in an ordinary Büchi automaton and proves positive-cycle padding. The F/G bound at [2311–2428](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:2311) has a supplied temporal-record/recurring-witness construction; it excludes X.

[Lines 2430–2555](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:2430) supply a branching ECTL certificate semantics, soundness for each horizon, completeness for sufficiently large horizons, and SAT compilation. The text explicitly says this is separate from the report's unprinted bounded ECTL semantics and makes no polynomial-size promise for naive certificate expansion. This is a supplied alternative, not evidence that an unprinted source construction has been reproduced.

The report's shift-register horizon is not asserted minimal. The mutual-exclusion experiment at [2582–2592](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:2582) records only bounded checks without a known completeness bound, so it is not presented as unbounded verification.

### CEGAR: exact objects, progress and limits

The abstraction construction supplies both relation and initial-set images. Early abstraction may add initial states or edges because different conjuncts obtain independent witnesses. The product quotient at [2891–3048](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:2891) handles constant atoms, separate unobserved-variable coordinates, empty formula families and the zero-variable program case explicitly.

Path validation is the full concrete image recurrence with a first-empty-index output contract. Refinement distinguishes dead, bad and irrelevant states. The text supplies a polynomial reduction for minimum-size product refinement and then a greatest slice-based refinement for the stronger task of separating a set from its entire complement. It distinguishes a minimum local number of blocks from a greatest global equivalence, and explicit-table polynomial cost from succinct BDD cost.

The lasso validator at [3520–3592](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:3520) uses `m+1` full loop copies, where `m` is the smallest loop-block size, and proves both directions by equal-state occurrences at the same loop coordinate. Exact refinement decreases `|S|-b(h)`. The combined policy at [3647–3702](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:3647) performs an exact recheck before requesting a partition split and decreases the displayed lexicographic measure.

The theorem's fragment restriction at [3594–3645](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:3594) is material: the refutation must be witnessed by a finite path or lasso whose every concretization is a refutation. The text explicitly says a branching counterexample requires an additional validator and progress argument.

## Resolved interfaces and proof dependencies

All three explicit cross-references in N-c-017 were resolved against current active text.

| N17 reference | Current target read | Standing relevant to N17 |
|---|---|---|
| [def:p09-ltl](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:1209) | [handbook/parts/p09/logic-in-computer-science.tex:615](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:615), the active Part VIII LTL card, and the full inherited LTL semantics at [handbook/restoration/inherited-13340-13409.tex:1](C:/Dev/the-methods-of-reason/handbook/restoration/inherited-13340-13409.tex:1). | Discrete infinite words and inclusive strong until. Hilbert completeness is not a premise of the tableau's semantic proof. |
| [thm:p09-ltl-buchi](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:2222) | [handbook/parts/p09/logic-in-computer-science.tex:777](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:777). | Effective exponential-size ordinary Büchi translation is explicitly cited. |
| [sec:p09-presentation-n-c-013](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:2223) | [handbook/parts/p09/presentations/n-c-013.tex:1](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-013.tex:1) through line 285. | Actual acceptor, start-set conversion, local/eventuality product and alphabet projection supplied. Lines 218–222 expressly retain the source's lack of a line-by-line two-inclusion induction. |

The ordinary Büchi type was read at [handbook/parts/p08/temporal-epistemic-supplement.tex:355](C:/Dev/the-methods-of-reason/handbook/parts/p08/temporal-epistemic-supplement.tex:355). N17's product records the automaton state before consuming the current label; the host product at [handbook/parts/p09/logic-in-computer-science.tex:796](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:796) records it after that consumption. These are explicitly typed shifted representations, so their different initial sets are not by themselves a mismatch.

The adjacent CTL interface and the full paired [annex:p9.ctl.1](C:/Dev/the-methods-of-reason/handbook/annex/p09/proofs.tex:86) were read. N17's local Burch constructions supply their own specialized formulas and arguments. Graph-colouring/clique-partition hardness remains an ordinary cited/known complexity dependency of the displayed reduction; this inventory does not require its proof to be reproduced.

## Remaining obligations and verification limits

1. **Definite missing presentation:** the separately registered revised McMillan 1993 book, at [1627–1639](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-017.tex:1627). The 1992 thesis has its own title/date/report identity at [handbook/bib/handbook.bib:2556](C:/Dev/the-methods-of-reason/handbook/bib/handbook.bib:2556). No current acquisition claim or source interchangeability is inferred.
2. **Explicit construction limit:** full branching-counterexample treatment is absent from the supplied CEGAR path/lasso method. Its exact additional source obligation must be established by source comparison before authoring a broader claim. The restricted theorem is not recorded as erroneous merely because it is restricted.
3. **Source coverage not certified:** annotated Bryant versus journal version, CMU report versus published Biere article, and JACM versus preliminary CAV are explicitly different source states. No fresh complete source-body comparison was performed here.
4. **Proof acceptance not performed:** substantial local proofs and legitimate cited dependencies are now inventoried. Sequential reading is evidence of what the manuscript says and supplies, not independent acceptance of every mathematical step. In particular, N13's written automaton interface keeps its source proof boundary visible.

The original topic list has substantial active content for BDDs, fixed points, BMC, CEGAR and industrial context. Whole N-c-017 completion remains unverified because the exact registered McMillan source presentation is absent and complete source fidelity/proof acceptance was outside this task.

## Complete heading ledger

Each heading below was encountered during the sequential read. Content and proof standing are described above and in the JSON; heading existence alone was not treated as completion.

| Line | Actual heading |
|---:|---|
| 3 | Four mechanisms behind symbolic verification |
| 6 | Bryant's fixed-order reduced function graphs |
| 111 | Bottom-up reduction. |
| 179 | Residual functions and the effect of variable order. |
| 240 | Symmetry can keep the graph small. |
| 276 | Combining two graphs. |
| 334 | Restriction, quantification, and equality. |
| 374 | Composition by three residuals. |
| 419 | Finding, listing, and counting satisfying assignments. |
| 482 | An exponential lower bound for multiplication. |
| 561 | The ALU experiment. |
| 592 | Burch et al.'s symbolic fixed points |
| 608 | The relation denoted by a term. |
| 691 | The two recursive BDD evaluators. |
| 844 | Positive transitive closure by squaring. |
| 881 | The general iterative-squaring transformation. |
| 1041 | Applying the transformation inside a nested fixed point. |
| 1091 | Fair paths as nested fixed points. |
| 1206 | A symbolic tableau for linear temporal logic. |
| 1349 | Strong and weak observational equivalence. |
| 1446 | Language containment with a deterministic specification. |
| 1549 | The pipeline experiment. |
| 1627 | McMillan's 1993 book and the earlier thesis |
| 1641 | Biere--Cimatti--Clarke--Zhu bounded semantics |
| 1725 | The complete no-loop translation. |
| 1764 | The complete selected-loop translation. |
| 1833 | Why a finite loop traversal suffices. |
| 1934 | Searching successive horizons. |
| 1969 | The three-bit shift-register calculation. |
| 2038 | Recurrence diameter and finite stopping bounds. |
| 2082 | Reachability and invariant verification. |
| 2122 | Certifying the ordinary diameter. |
| 2175 | A bounded witness for existential persistence. |
| 2193 | Padding a lasso to one fixed horizon. |
| 2212 | A completeness bound for arbitrary LTL. |
| 2263 | Systems with uniformly bounded stems and periods. |
| 2311 | A linear witness bound for the \(F,G\) fragment. |
| 2430 | Branching certificates for existential CTL. |
| 2557 | The implementation and positive verification experiments. |
| 2582 | Interpreting a bounded experiment. |
| 2594 | Clarke et al.'s counterexample-guided refinement |
| 2604 | Concrete structures, ACTL*, and simulation. |
| 2652 | Existential abstraction and appropriateness. |
| 2701 | Exact abstraction versus symbolic approximations. |
| 2798 | Guarded programs and their transition relation. |
| 2854 | The initial abstraction. |
| 2891 | The product representation required by symbolic refinement. |
| 3050 | Combining exact and early transition abstraction. |
| 3139 | The refinement loop. |
| 3159 | Exact validation of a finite abstract path. |
| 3258 | What the refinement must separate. |
| 3316 | Why minimum-size product refinement is hard. |
| 3400 | A coarsest refinement for separation from the complement. |
| 3520 | Validation of an abstract lasso. |
| 3594 | Termination and completeness of exact refinement. |
| 3647 | A terminating policy for combined approximation. |
| 3704 | The industrial experiment. |

## Mathematical result and algorithm ledger

| Actual lines | Result / algorithm | Proof standing in the current text |
|---|---|---|
| 59–109 | Bryant Theorem 1 | supplied existence/uniqueness/minimality proof |
| 111–177 | Bryant reduction algorithm | supplied algorithm and proof |
| 179–238 | Variable-order size example | supplied residual-function counting proof |
| 240–274 | Symmetry/parity size calculations | supplied argument |
| 276–327 | Apply | supplied algorithm/cost argument |
| 334–417 | Restriction, abstraction, equality and Compose | supplied identities, semantics and cost proof |
| 419–480 | Bryant Lemma 3 / satisfying assignments | supplied proofs with arithmetic-cost qualification |
| 482–559 | Bryant Appendix Theorem 2 / Lemma 4 | supplied residual-separation proof |
| 608–752 | Burch relational evaluation/Boolean encoding | supplied clauses and induction arguments |
| 754–842 | Symbolic CTL clauses and explicit Boolean encoding example | Supplied formulas and complete trace; not execution evidence. |
| 844–879 | Positive transitive-closure squaring | supplied proof; E+ not E* distinguished |
| 881–1040 | Burch Section 5.2 transformation | supplied both-fixed-point proof, counterexample and scope limitations |
| 1041–1089 | Nested fixed-point example | supplied derivation and path proof |
| 1091–1204 | Fair temporal fixed points | supplied two-direction path proof and symbolic operation count |
| 1206–1347 | Symbolic LTL tableau | supplied construction, truth lemma and converse |
| 1349–1383 | Strong observational equivalence | supplied characterization |
| 1385–1444 | Weak observational equivalence | supplied proof and divergence example |
| 1446–1547 | Büchi containment with deterministic specification | supplied proofs and restriction counterexample |
| 1549–1625 | Pipeline temporal-to-state reduction | Supplied proof of the reduction under its explicit uniqueness hypothesis; benchmark measurements cited. |
| 1665–1707 | BMC Lemmas 7–8 and Theorem 9 | Source theorem interfaces with finite-prefix/lasso arguments expanded in subsequent translation and stopping sections. |
| 1725–1866 | BMC Definitions 11–13 | supplied exact clauses, induction rationale and boundary examples |
| 1868–1932 | BMC Theorem 16 / Corollary 17 | supplied two-direction proof and source size claim |
| 1934–1967 | Increasing-horizon search | explicit procedure with correctness qualifications |
| 2038–2173 | Recurrence/ordinary diameters and reachability | supplied proofs and counterexample |
| 2175–2261 | Lasso completeness/padding | supplied positive-cycle and padding proof with Büchi dependency |
| 2263–2299 | Uniform execution bounds | supplied derivation |
| 2311–2428 | F/G-fragment witness bound | supplied interval/loop construction and truth-preservation proof |
| 2430–2555 | Branching ECTL certificates | explicit supplied handbook construction, not source's unprinted semantics |
| 2604–2699 | Clarke Theorem 2.3, Lemma 3.2, Theorem 3.3 | Local simultaneous semantic induction and simulation construction. |
| 2701–2781 | Clarke Theorem 3.5 / early abstraction | Local inclusion proof; initial-state approximation included. |
| 2798–2852 | Guarded-program model construction | Supplied finite-coordinate existence argument. |
| 2854–3048 | Clarke Proposition 4.2 and Theorem 4.8 | Local kernel equivalence proof with zero-variable atoms, vacuous formula families and unobserved coordinates. |
| 3050–3138 | Combined exact/early abstraction construction | Local typed construction and proofs, with example. |
| 3159–3218 | Clarke Lemma 4.10 / SplitPath | Both directions supplied, backward finite witness construction. |
| 3316–3398 | Clarke Theorem 4.17 / minimum product refinement | Complete displayed polynomial reduction from clique partition; NP-hardness of graph colouring used as known dependency. |
| 3400–3518 | Clarke Lemmas 4.18–4.19, Corollaries 4.20/4.22, Remark 4.23 / PolyRefine | Supplied separation/greatestness proof, explicit example and complexity scope. |
| 3520–3592 | Clarke Theorem 4.13 / SplitLoop | Both directions supplied using equal-state occurrences at equal loop coordinates. |
| 3594–3645 | Clarke Theorem 4.24 / scoped exact refinement | Full supplied progress measure N-b(h) and correctness proof; not general branching-counterexample completeness. |
| 3647–3702 | Combined approximation exact-recheck policy | Explicit policy and full lexicographic progress/correctness proof. |
