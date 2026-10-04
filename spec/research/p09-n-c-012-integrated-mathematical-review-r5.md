# N-c-012 Round 5 integrated mathematical review

## Scope and result

I reviewed the live source `handbook/parts/p09/presentations/n-c-012.tex` from line 1 through line 3060 and the integrating temporal-logic material in `handbook/parts/p09/logic-in-computer-science.tex`, especially lines 602--711, 713--797, and 799--904. I used no rendered or derived manuscript form and no earlier N-c-012 review. The review was adversarial with respect to definitions, quantifier order, type and standing, counterexamples, proof steps, and theorem strength.

No mathematical or proof-coherence blocker remains. The presentation consistently distinguishes a source theorem from a source assertion, proof outline, source defect, handbook repair, and handbook-supplied argument. The chapter-level statements reuse the same inclusive operators and preserve the restrictions established in the presentation.

## Presentation-by-presentation findings

### Kamp

The order classes, the single-free-variable first-order standing, and the strict witness/open-interval argument order are explicitly fixed before use (`n-c-012.tex:16--98`). The temporal-to-first-order translation is capture-avoiding and has the right strict inequalities and open intervals (`n-c-012.tex:100--131`); the converse is confined to complete strict linear orders and the rational-cut counterexample prevents an illicit extension to all chains (`n-c-012.tex:133--165`).

The sparse-square separation does not rely on Kamp's false unrestricted second uniformity. The atomic parity counterexample is explicit, the missing same-parity hypothesis is stated as a handbook repair, and the conjunction, immediate-neighbour, strict-past, and strict-future induction cases close under that repaired invariant (`n-c-012.tex:233--341`). In particular, the unbounded past/future cases are eventually constant, so they do not require the defective square calculation. The theorem-number and source-proof boundary is then preserved (`n-c-012.tex:343--361`).

### Pnueli

The manuscript gives the pure system \(K_b\) at exactly its displayed strength: derived \(F:=\neg G\neg\), G1--G3, and only RT, RG, and MP (`n-c-012.tex:819--898`). It does not merge that pure theorem system with the later system-dependent principles I1, I2, E, and N (`n-c-012.tex:930--990`). This separation is load-bearing. ER's A1 has an \(R\)-dependent one-step premise, and its translation \(p\Rightarrow Fq\) is internalized by E, whose premise is precisely \(p(s)\land R(s,s')\Rightarrow q(s')\). Bare \(K_b\) has no rule capable of importing that transition-system premise. The manuscript therefore correctly refuses to treat Pnueli's skeletal Theorem 3 comparison as an embedding into pure \(K_b\) (`n-c-012.tex:1020--1029`).

The strict \(j>i\) definition, the zero-rank and current-state P2 counterexamples, A2's inclusive tension, and the arbitrary-start and nonserial gaps in the ER completeness sketch are all kept separate (`n-c-012.tex:461--541`, `618--676`). Thus no false soundness or completeness result is silently rehabilitated. For the finite-state decision argument, the action-fair SCC criterion is correct: select one internal edge per action, connect the selected edges inside the finite strongly connected component, and repeat the resulting closed walk; conversely, a fair infinite path eventually remains in one SCC of the finite condensation and supplies every action internally (`n-c-012.tex:1034--1098`). The general finite-system proof-adequacy claim remains explicitly unconstructed (`n-c-012.tex:1116--1121`).

### GPSS

The isolated reversed inequality in the printed \(F\)-clause is not propagated. The presentation fixes the coherent strict-future reading, totalizes next only where needed, and gives exact semantics and standing for the local \(\mathsf U_s\) warning and the handbook-supplied past dual (`n-c-012.tex:1216--1294`). Its two-way bridge to inclusive discrete until/since retains next and previous; it never claims that inclusive \(U,S\) alone define adjacency (`n-c-012.tex:1296--1317`).

The four expressiveness domains---at zero on \(\omega\)-models, future formulas on discrete complete orders, separation on discrete complete orders, and the source-reported gap-operator claim on arbitrary orders---are not collapsed (`n-c-012.tex:1477--1543`). The omitted negation core and other referrals remain an outline rather than a completed proof (`n-c-012.tex:1545--1649`). Likewise, the \(D^0UX\) semantic/fixed-point conflict is exposed rather than normalized (`n-c-012.tex:1778--1838`).

### Sistla--Clarke

The source's \(U,S,F\) clauses are inclusive, including the current position (`n-c-012.tex:1867--1927`). That convention is respected in the repaired NP certificate. The three-state path \(x,u,x,c,c,\ldots\) shows why one node-indexed label is unsound: \(Fa\) differs between the two occurrences of \(x\) (`n-c-012.tex:2145--2162`). The separate occurrence sets \(\mathcal L_i\) and recurrent-node summaries \(\mathcal L_C(x)\) have different future domains, and their two eventuality clauses include the present witness (`n-c-012.tex:2163--2205`).

The repaired witness construction is sound. After the guessed prefix and entry edge, enumerate the finite set \(C\). If \(|C|>1\), strong connectivity supplies internal finite paths from each enumerated node to the next and from the last back to the first; repeating their concatenation visits every node of \(C\) infinitely often. If \(|C|=1\), the added directed-cycle condition supplies the required self-loop. Structural induction then proves the summaries: atoms use the node valuation; negation and conjunction are local; at a prefix occurrence, the future is exactly the remaining prefix occurrences plus the recurrent suffix; at a recurrent occurrence, every node of \(C\) occurs again, so the future existential is exactly the displayed \(\exists y\in C\) clause. The certificate has \(r+1+|C|\) truth sets, each a subset of \(\operatorname{SF}(f)\), with \(r+1\) polynomially bounded by the guessed-prefix bound, so occurrence indexing preserves polynomial size (`n-c-012.tex:2132--2143`, `2163--2215`).

The cycle condition is necessary, not decorative: the explicit three-node graph with the acyclic singleton guess \(C=\{c\}\) makes the literal strong-connectivity check accept false \(GP\); requiring a directed cycle excludes exactly that dead suffix (`n-c-012.tex:2217--2234`). The subsequent PSPACE truth-set recurrences also preserve inclusive until/since and explicitly discharge loop eventualities (`n-c-012.tex:2320--2458`).

For ETL, restricting every emitted terminal word to be nonempty is an openly identified handbook domain restriction forced by the printed consistency rule's lack of an epsilon case. Replacing a length-\(r\) emission by \(r\) one-terminal productions with fresh nonterminals preserves finite and infinite emitted terminal sequences and grows the encoded grammar only linearly (`n-c-012.tex:2468--2500`). The normalized positive recurrence and the finite continuation-layer check then match that restricted semantics (`n-c-012.tex:2501--2519`, `2538--2585`, `2596--2633`). The final complexity table retains this nonempty-emission qualification (`n-c-012.tex:2639--2670`).

### Alpern--Schneider and the integrated boundary

Safety and liveness quantify over the full \(S^\omega\), with \(S\ne\varnothing\) made explicit so that every basic cylinder has a continuation (`n-c-012.tex:2672--2769`). The prefix-topology equivalences are proved in both directions (`n-c-012.tex:2880--2899`). For arbitrary \(P\), \(\overline P\) is closed and
\[
L_P=P\cup(S^\omega\setminus\overline P)
\]
is dense: a nonempty open subset of \(\overline P\setminus P\) would yield a strictly smaller closed superset of \(P\), contradicting closure minimality. Hence \(P=\overline P\cap L_P\) with the exact expressibility caveat preserved (`n-c-012.tex:2901--2943`). The two-live-factor theorem has the material \(|S|>1\) hypothesis, and the printed Corollary 2.1 is correctly rejected by an intersection-closed denotation-family counterexample; union closure is the needed repair (`n-c-012.tex:2951--3011`).

Finally, the five-way boundary does not transfer syntax, semantics, proof rules, or theorem strength between Kamp, Pnueli, GPSS, Sistla--Clarke, and Alpern--Schneider (`n-c-012.tex:3047--3060`). The integrating chapter agrees: it fixes inclusive LTL/past semantics (`logic-in-computer-science.tex:605--626`), gives the exact strict/inclusive discrete translations (`logic-in-computer-science.tex:628--685`), states PSPACE completeness only for the specified operator bases (`logic-in-computer-science.tex:696--711`), and treats safety/liveness as semantic word-property classes (`logic-in-computer-science.tex:713--721`).

VERDICT: ACCEPT
