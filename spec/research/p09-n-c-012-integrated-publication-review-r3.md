# N-c-012 Round 3 blind adversarial publication review

## Scope and method

This is a manuscript-content review of the actual LaTeX sources, not of a derived artifact. I read `handbook/parts/p09/presentations/n-c-012.tex` completely and continuously from line 1 through its EOF at line 3010. I also read the current host-chapter LaTeX in `handbook/parts/p09/logic-in-computer-science.tex` for the reused LTL and past definitions, the strict/inclusive bridge, the public theorem statements, the safety/liveness definition, the infinite-word automata and LTL model-checking interface, and the `\input` seam (especially lines 601--811 and 899--906).

I did not read an integrated N-c-012 review report and did not contact another reviewer. I did not inspect or create a manuscript PDF, page image, PNG, render, screenshot, test, checker, repository script, TeX command, build, or hash. Accordingly, this report makes no layout or final-publication claim.

## Blocking finding

### R3-01 — `K_b` changes standing between its definition and the reported ER comparison

The manuscript gives `K_b` an exact, deliberately narrow standing and then uses the same name at a materially different apparent strength:

- The pure future syntax and semantics are given at presentation lines 819--845. Lines 847--878 display G1--G3, RT, RG, MP, and Q1--Q4. Presentation lines 887--894 then say explicitly that `K_b` denotes **exactly** the pure propositional future calculus with derived `F`, G1--G3, RT, RG, and MP; it is a theorem system, not a formula or model class.
- Presentation lines 930--990 explicitly keep I1, I2, E, and N separate as system-dependent forms. In particular, E at lines 963--966 is the rule that turns the same transition premise used by ER's A1 at lines 562--565 into the translated conclusion `p\Rightarrow Fq`.
- Despite that separation, lines 1020--1025 say without an extension qualifier that Theorem 3 makes every ER axiom a theorem of `K_b`. On the manuscript's own preceding definitions, the translated A1 step is supplied by E, which has just been placed outside pure `K_b`; G1--G3, RT, RG, and MP alone do not internalize an arbitrary transition relation.
- The later finite-state statement shows that the distinction is available and meaningful: lines 1112--1115 expressly say “the `K_b` calculus extended by the system-dependent axioms, P, and MRG.” Theorem 3 receives no corresponding scope statement.

This is not merely an omitted derivation. It leaves the reader unable to tell whether the source theorem concerns pure `K_b`, `K_b` under transition premises, or `K_b` extended by some or all of I1/I2/E/N. It also defeats the five-part technical-name rule at the point of use: the initial definition and standing are exact, but the later use appears to require a distinction not supplied at that location.

Required repair: state the exact theorem system in the Theorem 3 paragraph. If the source itself is under-specified or inconsistent about the extension, say so explicitly and keep the claim at source-reported standing. If an extension is intended, enumerate precisely which already displayed system-dependent forms are assumed. No new system name is needed unless its necessity, exact definition, standing, nonredundancy, and later use are all supplied together.

## Adversarial checks that passed

### Definition before use and technical-name discipline

- P1 passes. A state assertion and reachable set `X` are defined at lines 433--450; P1 is then displayed as reachable-state induction at lines 480--489 and used through explicit initial and preservation obligations at lines 678--711. Its standing is a proof principle, not a tense connective.
- The parameterized ER apparatus passes. `\widehat p`, `\widehat p_u`, and `\exists_U\widehat p` are typed at lines 543--558, their sole need is R4, and lines 589--616 distinguish the uniform-parameter proof condition from a new temporal constructor.
- `\Sigma\models_{\rm prop}` and `L_{\rm prop}(\Sigma)` pass. Their semantic standings and reasons for separate notation are given at lines 1030--1062 and 1150--1165 before their theorem and inclusion uses.
- `\mathsf{ETL}` passes. Right-linear grammars are defined first at lines 2428--2436; ETL is then defined as the least formula class with the grammar-indexed formation rule at lines 2437--2446. Lines 2454--2472 give the constructor semantics and distinguish it from ordinary until; lines 2485--2584 use the distinction in the closure, tree, periodic-model, and decision arguments; and lines 2590--2620 use it in the complete classification table.
- Other potentially hazardous names are supplied with eliminable definitions and standings before use, including tense-defining formulas (lines 42--72), expressibility from `\mathcal S'` (lines 203--231), `\leadsto` (lines 461--478), full and partial attachments (lines 713--768), `\operatorname{Pr}` (lines 1410--1455), decomposition formulas (lines 1597--1632), acceptable subsequences and ambient-size notation (lines 2016--2047), source truth sets and fulfillment (lines 2280--2303), ultimate periodicity (lines 2346--2358), and uniform and absolute liveness (lines 2721--2761).
- Source-reported undefined items are not promoted into handbook definitions. In particular, GPSS's `S'`/`U'` symbols are confined to source-reported standing at lines 1532--1539, and its unformalized “event expressions” are identified as an owed part of the omitted proof at lines 1621--1632 rather than used as established machinery.

### Strict/inclusive conventions and model domains

- The host chapter defines inclusive since and previous at `logic-in-computer-science.tex` lines 604--625 and then gives the exact two-way discrete bridge at lines 627--684. Its public first-order theorem is restricted to pointed `\mathbb N`-words at lines 686--693, and its PSPACE theorem names the inclusive operator basis at lines 695--710.
- Kamp's presentation fixes strict witnesses, open intervals, and source operand order at presentation lines 74--98 and preserves them in the first-order translation at lines 100--145.
- GPSS explicitly identifies its strict future convention and the source's conflicting printed F-clause at lines 1212--1247. The local `\mathsf U_s` and handbook-supplied past dual are defined and assigned different source ownership at lines 1249--1276. The strict/inclusive equivalences are restricted to omega-models at lines 1292--1313.
- GPSS's four theorem domains—zero of an omega-model, arbitrary-point future formulas on discrete complete orders, separation on discrete complete orders, and arbitrary linear orders with undefined extra symbols—remain separated at lines 1473--1539.
- The transition to Sistla--Clarke resets the convention explicitly: its inclusive X/U/S clauses are stated at lines 1863--1923, and line 1923 warns that they are not the preceding strict GPSS clauses.
- The Alpern--Schneider presentation changes domain again, from formula satisfaction to arbitrary properties `P\subseteq S^\omega`, at lines 2622--2657; lines 2716--2719 explicitly warn that relativizing the quantifiers to one transition system would change both the continuation space and topology.

### Proof ownership and theorem strength

- The presentation consistently distinguishes source proofs, source assertions, source gaps, and handbook repairs. Representative load-bearing examples are Kamp's parity repair at lines 272--341; Pnueli P2 counterexamples at lines 517--541; the two independent gaps in Pnueli's ER completeness sketch at lines 618--676; the GPSS linear/S4 countermodel at lines 900--928; the GPSS proof-outline boundary at lines 1541--1645 and 1689--1772; the Sistla--Clarke directed-cycle repair at lines 2177--2194; and the Alpern--Schneider Corollary 2.1 repair and counterexample at lines 2928--2961.
- Appendix A does not transfer Pnueli's local six-step lemma proof to externally owned T2/T3 (lines 1119--1148).
- Appendix B separates Pnueli's local acceptor assertion from imported closure and inclusion results and does not turn that route into a later formula-to-Buchi translation (lines 1150--1197).

### Safety/liveness and automata/model-checking interfaces

- The host semantic safety/liveness definition at `logic-in-computer-science.tex` lines 712--720 matches the quantified full-word definitions developed at presentation lines 2624--2694. The presentation additionally makes the nonempty state-domain hypothesis and the full-space rather than transition-relative domain explicit at lines 2659--2664 and 2716--2719.
- The host defines the relevant infinite-word automata at lines 722--745, states the LTL-to-Buchi interface at lines 747--756, and gives the product construction and universal-path theorem at lines 763--811.
- Pnueli's Appendix B is kept at its historical language-inclusion standing at presentation lines 1150--1197. Sistla--Clarke's problem is explicitly existential path truth at lines 1932--1970, and the presentation explains how universal correctness is obtained through the negated existential problem at lines 1953--1956. The classification table at lines 2590--2620 preserves that quantifier.
- The input seam is coherent: `logic-in-computer-science.tex` lines 899--906 places `n-c-012` after the public LTL, past, safety/liveness, automata, and model-checking definitions and before the next main model-checking section. Thus the presentation's backward references to those interfaces are defined before the input.

### Cross-presentation reader coherence and final integration

- Each convention reset is explicit at the point where it matters: Pnueli distinguishes strict `\leadsto` from inclusive F/G (presentation lines 461--478, 819--845, and 668--676); GPSS declares strict futurity and its local notation (lines 1212--1313); Sistla--Clarke declares inclusive semantics (lines 1863--1930); and Alpern--Schneider declares semantic property standing (lines 2622--2657).
- The final integration paragraph at lines 2997--3010 accurately keeps apart Kamp's order-theoretic expressiveness, Pnueli's transition-system proof rules and internal strict/inclusive tension, GPSS's strict language and discrete bridge, Sistla--Clarke's operator-sensitive decision problems, and Alpern--Schneider's semantic property classes. It does not transfer definitions or proof ownership among them.

### Reader-facing workflow debris

A case-insensitive prose search found no acquisition-log, hash, audit, board, review, build, or campaign-status debris. The potentially matching occurrences are substantive mathematical prose: “proof status” names the source/handbook proof boundary at line 343; “tests continuations” describes a semantic procedure at line 1046; “realizability is being tested” describes guessed truth sets at line 2387; and “renders its quantifiers” introduces a formalization of source prose at line 2798. None is a workflow artifact. Ordinary phrases such as accepted runs, proof trees, model checking, and formula rendering were not misclassified.

VERDICT: REJECT -- R3-01
