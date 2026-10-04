# N-c-012 Round 4 blind mathematical and proof-coherence review

## Review protocol

I read the actual current LaTeX file `handbook/parts/p09/presentations/n-c-012.tex` directly and completely from line 1 through line 3024 (EOF). I independently reconstructed all five presentations in their displayed order: Kamp, Pnueli, GPSS, Sistla--Clarke, and Alpern--Schneider.

I also read the actual current controlling passages of `handbook/parts/p09/logic-in-computer-science.tex`: the temporal-logic and past-operator interface and strict/inclusive bridge (lines 602--685), the public first-order and complexity theorems (lines 687--711), the safety/liveness and infinite-word-automata interfaces (lines 713--762), the automata-theoretic model-checking method and theorem (lines 764--812), the presentation input seam (lines 900--908), the LTL row of the consolidated complexity boundary (lines 2200--2246), and the publication-boundary statement (lines 2330--2335).

This was a blind source-only review. I did not read any earlier integrated review report and did not consult another reviewer. I used no manuscript PDF, PNG, page image, render, screenshot, test, checker, repository script, TeX command, build, or hash. The evidence below is actual-LaTeX line evidence only.

## Result

No mathematical, typing, quantifier, model-domain, proof-ownership, terminology, or parent-interface defect remains that warrants a Round 4 finding.

## 1. Kamp reconstruction

The presentation correctly fixes nonempty strict linear orders and distinguishes the four order classes, including the material fact that order completeness neither entails density nor removes endpoints (`n-c-012.tex`, lines 16--40). The first-order side is correctly typed as a uniform operation on predicate interpretations with one current-point variable (`n-c-012.tex`, lines 42--72). The temporal clauses preserve all three source-sensitive features: strict witness, open interval, and Kamp's witness-first operand order (`n-c-012.tex`, lines 74--98). The capture-avoiding translation preserves those features explicitly, and its easy direction is correctly stated over arbitrary binary structures while the converse is restricted to complete strict linear orders (`n-c-012.tex`, lines 100--155). This matches the parent statement that the forward direction is unrestricted but the converse uses Kamp's complete strict linear orders (`logic-in-computer-science.tex`, lines 628--637).

The Chapter IV theorem numbers and domains remain separated. Literal Theorem IV.3 is stated as integer-order non-expressibility of the isolation tenses from the exact operation basis, not as the rational-cut theorem or as a direct GPSS reduction (`n-c-012.tex`, lines 167--231, 343--354, 1469--1475). The sparse-square repair is mathematically coherent. The presentation first exhibits the false unrestricted offset clause with an atomic counterexample, then adds the necessary same-parity premise and labels it as a handbook repair (`n-c-012.tex`, lines 233--289). The induction handles Boolean closure, immediate neighbours, and the two unbounded operators without reusing the defective clause (`n-c-012.tex`, lines 291--332). In particular, strict past is eventually constant to the right once its operand is nonempty, while strict future is either everywhere true when the operand is unbounded above or eventually false when it is bounded above. The alternating central-square gaps then contradict the first repaired uniformity exactly as required (`n-c-012.tex`, lines 334--341). Proof ownership is explicit: Kamp's printed induction is not represented as sound, and the parity-corrected proof belongs to the handbook (`n-c-012.tex`, lines 356--361).

## 2. Pnueli reconstruction, including P1 and the repaired \(K_b\) paragraph

The system model, executions, and sequential/concurrent transition relations are correctly typed before any proof rule is used (`n-c-012.tex`, lines 372--431). Reachability is reflexive--transitive, so the displayed P1 has the right base and preservation premises and concludes exactly over the reachable set \(X\) (`n-c-012.tex`, lines 433--489). Its later sequential use is also correct: the initial attachment and one obligation for every typed location/data pair are premises to P1, not consequences illicitly attributed to it (`n-c-012.tex`, lines 678--711).

The strict/inclusive tension is not hidden. The printed relation \(p\leadsto q\) quantifies \(j>i\) (`n-c-012.tex`, lines 461--478). The rank rule is first minimally typed at rank zero, then independently refuted both by the missing zero-boundary condition and by its current-state \(\psi(s)\) disjunct under strict futurity (`n-c-012.tex`, lines 480--541). ER's A2 and the later inclusive \(F\) are likewise retained at their incompatible printed standings rather than normalized into one semantics (`n-c-012.tex`, lines 668--676). The two completeness-sketch gaps concerning arbitrary starts/reachability and dead-end vacuity are supported by correctly typed countermodels (`n-c-012.tex`, lines 618--666).

The repaired \(K_b\) paragraph is now correct. Pure \(K_b\) is defined only by the propositional \(F,G\) language, G1--G3, RT, RG, and MP; no system transition relation occurs in that theorem system (`n-c-012.tex`, lines 819--928). The transition-sensitive principles I1, I2, E, N, DI, and DN are introduced later and each explicitly mentions \(R\) or an action relation (`n-c-012.tex`, lines 930--1018). ER's A1 has a transition premise, and its translation to \(p\to Fq\) therefore needs the system rule E; it cannot be a theorem of bare \(K_b\). Lines 1020--1029 state exactly that, report the source's Theorem 3 comparison, identify the overload, and decline both to add E silently and to claim the missing derivations. The mention of possible I1/I2/N additions also avoids implying that A1 is the only system-sensitive point. This is a correctly typed unresolved source assertion, not a repaired embedding theorem.

The finite-state specialization keeps its quantifiers straight. Proper executions begin at \(s_0\), arbitrary-start continuations are introduced only where the decision argument needs them, and the action-occurrence condition is explicit (`n-c-012.tex`, lines 1034--1066). The SCC criterion requires a cyclic component with an internal edge from every action class; its two directions are correctly supplied (`n-c-012.tex`, lines 1079--1098). Theorem 5's adequacy assertion is not conflated with Appendix B, which supplies only semantic decision routes and does not print a modern LTL-to-Buechi construction or complexity class (`n-c-012.tex`, lines 1116--1121, 1154--1201). These distinctions agree with the parent automata/model-checking interface, which separately constructs an automaton for \(\neg A\), checks an accepting cyclic SCC, and derives universal-path checking by complementing an existential counterexample question (`logic-in-computer-science.tex`, lines 764--812).

## 3. GPSS reconstruction and every strict/inclusive convention

The presentation exposes rather than erases the source's contradictory formal \(F\)-inequality. It adopts the coherent strict-future reading supported by the surrounding source clauses and identities and labels the inequality reversal and endpoint totalization as handbook repairs (`n-c-012.tex`, lines 1216--1251). The local symbols \(\mathsf U_s\) and \(\mathsf S_s\) have exact clauses and distinct ownership: \(\mathsf U_s\) transcribes the source; \(\mathsf S_s\) is the explicitly supplied order dual (`n-c-012.tex`, lines 1253--1280).

The discrete bridge is exact in both directions:

- strict future/since is next/previous applied to inclusive until/since; and
- inclusive until/since is the current-witness case disjoined with the current left operand and the strict operator.

Those equations appear at `n-c-012.tex`, lines 1296--1317, and match the recursively extended parent bridge at `logic-in-computer-science.tex`, lines 639--685. Neither location claims that inclusive until or since alone defines next or previous. Operand order is preserved throughout.

The response, precedence, and correctness formulas continue to use strict \(F,G,U_s\) (`n-c-012.tex`, lines 1319--1459); the later Sistla--Clarke operators are not imported retroactively. The four expressive-result domains are kept distinct: point zero of every omega-model, future formulas at every point of discrete complete models, separation over discrete complete models, and arbitrary linear orders only with undefined additional source symbols (`n-c-012.tex`, lines 1477--1543). The normal-form/Main-Lemma passage is accurately bounded as an outline with omitted event-expression translations, referrals, and numbering tension (`n-c-012.tex`, lines 1545--1649). The \(DX/DUX\) statements are weak theoremhood completeness claims over omega-validity, with the canonical construction's unprinted steps and omitted adjacency clause identified (`n-c-012.tex`, lines 1651--1776). Finally, the incompatible \(\mathsf U^0\) equation and recursion are demonstrated by a concrete valuation and are not adopted as one coherent operator (`n-c-012.tex`, lines 1778--1831).

## 4. Sistla--Clarke reconstruction, periodic argument, and repaired ETL domain

The base semantics is unambiguously inclusive: next advances once, until permits a witness at the current point, and since permits a witness at the current point (`n-c-012.tex`, lines 1867--1934). Satisfiability and truth in an \(R\)-structure are kept distinct, with the latter existentially quantifying a path; universal checking is its complemented counterexample problem (`n-c-012.tex`, lines 1936--1974). This is the exact distinction used by the parent model-checking theorem (`logic-in-computer-science.tex`, lines 799--811).

The complexity fragment is correct. The public theorem concerns inclusive \(L(U,X)\), obtains hardness from \(L(U)\), and obtains its upper bound from \(L(U,S,X)\) (`logic-in-computer-science.tex`, lines 696--710). The source presentation separately preserves the NP-complete \(L(F)\) and positive \(\widetilde L(F,X)\) cases and the richer PSPACE bases (`n-c-012.tex`, lines 1880--1934, 2108--2209, 2211--2422). It also repairs the singleton-SCC certificate by requiring an actual directed cycle, which is necessary for an infinite witness (`n-c-012.tex`, lines 2181--2198).

The periodic argument does not conflate three different data:

1. complete propositional valuation periodicity;
2. equality of the formula-relative truth sets; and
3. discharge of pending until obligations.

Lemma 4.6 and Theorem 4.7 state all three separately, keep a positive period, and use \(Ff\) when a past formula may hold away from the initial point (`n-c-012.tex`, lines 2284--2384). The polynomial-space checker then enforces the local next/until/since equations, the initial since boundary, loop closure, and within-loop until discharge (`n-c-012.tex`, lines 2386--2422).

The repaired ETL domain is coherent end to end:

- The presentation requires emitted terminal words to be nonempty because the printed local consistency machinery has no epsilon case. It labels this as a handbook domain repair, not a source restriction (`n-c-012.tex`, lines 2432--2442).
- Every production emitting several terminals is replaced by a finite chain of single-terminal productions with fresh nonterminals (`n-c-012.tex`, lines 2443--2447). Because every original emission is nonempty, this gives a bijective expansion/contraction of finite and infinite derivations without epsilon-only infinite chains, preserves the emitted terminal sequence, and has linear encoded-size overhead.
- The constructor has a precise formula-class standing and a typed finite/infinite satisfaction clause. A finite generated word of length \(r\) checks exactly offsets \(0\leq\ell<r\); an infinite word checks every \(\ell\geq0\) (`n-c-012.tex`, lines 2448--2483). The parity error in the source example is isolated and unused (`n-c-012.tex`, lines 2485--2494).
- The continuation tree \(\Gamma\) is finitely branching. Lemma 5.1 therefore gives the correct negative characterization: absence of every finite terminal witness plus finiteness of \(\Gamma\), the latter excluding an infinite branch by Koenig's lemma (`n-c-012.tex`, lines 2496--2517).
- Lemma 5.2 and Theorem 5.3 extend the periodic argument by requiring each negated grammar constructor to have its finite continuation tree exhausted within the period, while retaining both truth-transfer conclusions (`n-c-012.tex`, lines 2518--2545).
- The positive local consistency equivalence has exactly the two exhaustive cases after normalization: a satisfied one-terminal continuation production leading to the next nonterminal formula, or a satisfied one-terminal terminal production (`n-c-012.tex`, lines 2560--2574). Boolean negative consistency excludes any such finite success backwards through these equations. For each negated constructor at loop entry, the layer set \(\varphi\) follows all enabled continuation productions and is required to become empty during the period; this excludes an infinite generated witness (`n-c-012.tex`, lines 2575--2596). Thus the finite and infinite negative cases match Lemma 5.1 rather than relying on one another circularly.
- Theorem 5.4 explicitly makes the grammars part of the input, distinguishes constructor arity from total encoded length, and bounds the enlarged closure by that total length (`n-c-012.tex`, lines 2546--2559). PSPACE hardness already comes from the grammar-free temporal sublanguage, while normalization has only linear overhead, so the repaired nonempty-emission domain preserves the stated class.
- The final table carries the qualification forward: ETL is in the PSPACE row only with the nonempty-emission convention and repaired journal-version boundary (`n-c-012.tex`, lines 2603--2634). No epsilon-admitting ETL result is asserted.

Accordingly, the repaired Theorem 5.4 claim, its positive and negative consistency rules, the periodic model argument, and the table entry all quantify over the same domain.

## 5. Alpern--Schneider reconstruction over the full \(S^\omega\)

The universe is explicitly the full execution space over a nonempty state set, not the path space of a chosen transition relation (`n-c-012.tex`, lines 2636--2678). Safety and liveness quantify respectively over every word and every finite word with continuations in the full \(S^\omega\) (`n-c-012.tex`, lines 2680--2708). Lines 2730--2733 expressly warn that transition-system relativization would change both the continuation domain and topology.

Uniform and absolute liveness have exact, noninterchangeable quantifier orders and the expected implication chain (`n-c-012.tex`, lines 2735--2775). The repaired leads-to separation includes the precise necessary hypotheses and checks all degenerate cases (`n-c-012.tex`, lines 2777--2809). The predictive example correctly witnesses ordinary but non-uniform liveness (`n-c-012.tex`, lines 2811--2832).

The safety/closed and liveness/dense equivalences are proved in both directions on the full prefix topology (`n-c-012.tex`, lines 2844--2863). Theorem 1's closure factor is dense by the minimality-of-closure argument and is not misreported as a uniqueness or effective expressibility theorem (`n-c-012.tex`, lines 2865--2907). Theorem 2 correctly requires \(|S|>1\), uses two disjoint dense eventually-constant-tail properties, and distinguishes its factorization from the defective printed Corollary 2.1 (`n-c-012.tex`, lines 2915--2975). The counterexample family is intersection-closed and demonstrates that the printed hypothesis is genuinely insufficient, while the replacement by union closure is exactly what the displayed construction needs.

## Technical-name rule

The five-part rule is satisfied throughout the reviewed scope.

- Translation and basis names such as \(D\), \(\mathcal S'\), \(\tau\), and \(\sigma\) have exact eliminable definitions, metalinguistic standing, a stated distinction from object-language connectives, and immediate theorem use (`n-c-012.tex`, lines 100--145, 203--231; `logic-in-computer-science.tex`, lines 651--685).
- Pnueli-specific names such as \(\leadsto\), full/partial attachment, \(K_b\), proper execution, and \(\models_{\rm prop}\) are defined at the point of introduction, typed as statement families, assertion organizations, theorem systems, path classes, or semantic relations, and immediately used for a distinction that existing LTL terminology would blur (`n-c-012.tex`, lines 461--478, 713--768, 887--928, 1034--1066).
- GPSS's \(\mathsf U_s\), handbook-supplied \(\mathsf S_s\), \(\operatorname{Pr}\), special/decomposition formulas, and \(DX/DUX\) each have exact standing and are used only within their declared source reconstruction (`n-c-012.tex`, lines 1253--1294, 1422--1459, 1553--1649, 1651--1692).
- Sistla--Clarke's closure, ambient-relative subsequence measures, truth sets, fulfillment obligations, ETL constructors, \(\Gamma\), layer set \(\varphi\), and \(\ell_{\mathrm{in}}\) are all eliminable or source-defined mathematical artifacts whose nonredundancy and later use are stated locally (`n-c-012.tex`, lines 1889--1904, 2020--2089, 2284--2362, 2432--2596).
- Alpern--Schneider's uniform/absolute classes are exact semantic property classes, while \(P_{A,B}\), \(L_P\), \(E_a,E_b\), \(Q\), and \(\mathcal F\) are explicitly eliminable proof-local names (`n-c-012.tex`, lines 2735--2775, 2811--2832, 2865--2898, 2915--2975).

No hypothetical primitive, relation, motive, statement family, or metalinguistic abbreviation is named before its necessity, definition or axiom standing, nonredundancy, and actual use are supplied.

## Parent interfaces and final integration

The presentation supports, and does not overstate, every controlling parent interface:

- inclusive previous/since semantics and the exact two-way discrete bridge (`logic-in-computer-science.tex`, lines 605--685);
- first-order expressive completeness on pointed natural-number words and PSPACE-completeness for the exact inclusive \(L(U,X)\) fragment (`logic-in-computer-science.tex`, lines 687--711);
- safety and liveness as semantic classes of full word properties (`logic-in-computer-science.tex`, lines 713--721);
- the separation of Pnueli's Appendix B route from the later LTL-to-Buechi theorem and automata-theoretic model checking (`logic-in-computer-science.tex`, lines 723--812);
- the input order placing N-c-012 after the public temporal interfaces and before the later dedicated source presentations (`logic-in-computer-science.tex`, lines 900--908); and
- the consolidated combined-input/fixed-formula complexity distinction (`logic-in-computer-science.tex`, lines 2200--2246).

The final boundary paragraph accurately assigns one mathematical job to each of the five sources and forbids retroactive transfer of definitions, proofs, or terminology (`n-c-012.tex`, lines 3011--3024). No cross-presentation theorem is made stronger by integration.

VERDICT: ACCEPT
