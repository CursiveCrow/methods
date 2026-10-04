# N-c-012 integrated source-fidelity review — Round 5

## Scope and evidence

I read `handbook/parts/p09/presentations/n-c-012.tex` from line 1 through line
3060 and the integrating LaTeX in
`handbook/parts/p09/logic-in-computer-science.tex`, especially lines 602--812
and the input boundary at line 904.  I compared that source directly with the
current Kamp, Pnueli, GPSS, Sistla--Clarke, and Alpern--Schneider source notes.
Those records settled every attribution checked, so no historical-source file
was needed.  No manuscript render, build, checker, hash, or prior integrated
review was used.

## Source-fidelity findings

1. **Kamp.**  The presentation preserves the four order classes and their
   endpoint policy (`n-c-012.tex:16--40`), the equality-free displayed
   first-order vocabulary and uniform current-point assignment
   (`n-c-012.tex:42--72`), and the strict witness/open-interval semantics with
   Kamp's operand order (`n-c-012.tex:74--98`).  It keeps the easy translation
   valid over every binary structure distinct from the converse over
   \(\mathsf{Com}\), and does not turn expressive completeness into deductive
   completeness (`n-c-012.tex:100--165`).  Literal Chapter IV Theorem 3 is the
   integer-order isolation result (`n-c-012.tex:167--231`); the false printed
   parity-free induction clause is exhibited (`n-c-012.tex:272--278`), the
   same-parity correction is expressly handbook-owned (`n-c-012.tex:280--341`),
   and the source attempt and repaired proof are not conflated
   (`n-c-012.tex:343--361`).

2. **Pnueli.**  Strict \(\leadsto\), inclusive \(F,G\), literal P2, and the
   resulting source tensions remain separate (`n-c-012.tex:461--541`,
   `668--676`, and `819--845`).  The ER theorem's finite-branching,
   assertion-expressiveness, arbitrary-start, and seriality boundaries are all
   exposed rather than silently supplied (`n-c-012.tex:618--666`).  Most
   importantly, \(K_b\) is defined exactly as the pure propositional future
   theorem system with G1--G3 and RT/RG/MP, not as a language, model class, or
   system-dependent extension (`n-c-012.tex:847--898`).  I1, I2, E, N, DI, and
   DN are kept in the later system-dependent layer (`n-c-012.tex:930--1018`).
   Theorem 3's ER comparison is correctly left unresolved because translated
   A1 needs E, which bare \(K_b\) does not contain, and the paper prints neither
   an extension convention nor the individual derivations
   (`n-c-012.tex:1020--1029`).

3. **GPSS.**  The strict-future convention, the reversed printed inequality
   for \(F\), the handbook-supplied no-successor and past-dual completions, and
   the exact strict/inclusive discrete bridge are individually disclosed
   (`n-c-012.tex:1216--1317`).  The four theorem domains—point 0 on
   \(\omega\), future formulas on discrete complete orders, past/future
   separation on that same domain, and the arbitrary-order claim with
   undefined gap symbols—are not merged (`n-c-012.tex:1477--1543`).  The
   normal-form argument remains an outline with its external referrals and
   omissions (`n-c-012.tex:1545--1649`), while \(DX/DUX\), their weak
   theoremhood completeness standing, the omitted canonical-model steps, and
   the conflicting \(U^0\) displays retain their exact ownership and limits
   (`n-c-012.tex:1651--1838`).

4. **Sistla--Clarke.**  The source languages use inclusive \(U,S,F\), and the
   existential path problem is not renamed universal model checking
   (`n-c-012.tex:1867--1974`).  The repaired NP certificate is indexed by
   prefix occurrence, not graph node: the three-state repeated-node witness is
   explicit (`n-c-012.tex:2145--2162`), prefix truth sets
   \(\mathcal L_i\) and recurrent summaries \(\mathcal L_C(x)\) are distinct,
   and both eventuality clauses include the current occurrence
   (`n-c-012.tex:2163--2202`).  Its size remains polynomial because there are
   \(r+1+|C|\) sets, each contained in \(\operatorname{SF}(f)\), together with
   the preceding bound \(\operatorname{length}(p')\le |f||N|\)
   (`n-c-012.tex:2132--2143`, `2203--2215`).  The loopless-singleton
   counterexample and handbook-owned directed-cycle condition are stated
   separately (`n-c-012.tex:2217--2234`).  Strong connectivity then joins a
   finite enumeration of the nodes of \(C\) into a closed walk; repeating it
   visits every node infinitely often, while the added cycle supplies exactly
   the singleton case.  This validates the suffix claim used by the recurrent
   summaries without importing an automata argument.  Finally, the journal's
   corrected regular-operator proof controls, but the reconstruction expressly
   restricts productions to nonempty emissions and leaves the epsilon extension
   unestablished (`n-c-012.tex:2468--2519`, `2571--2637`).

5. **Alpern--Schneider.**  Properties remain arbitrary subsets of the full
   \(S^\omega\) space, not formula classes or paths relativized to one
   transition system (`n-c-012.tex:2674--2769`).  The nonempty-state repair,
   uniform/absolute quantifier distinctions, repaired leads-to hypotheses, and
   predictive example are all labelled at their proper standing
   (`n-c-012.tex:2709--2714`, `2771--2868`).  The topology equivalences and
   Theorems 1--2 preserve source proof ownership (`n-c-012.tex:2880--2976`),
   while the printed intersection/union defect in Corollary 2.1 is retained,
   refuted, and repaired only on the handbook side
   (`n-c-012.tex:2978--3011`).

6. **Integration boundary.**  The chapter-level bridge uses Kamp's strict
   operand order and retains \(\mathsf X,\mathsf Y\) for equivalence with the
   inclusive language (`logic-in-computer-science.tex:628--694`).  The PSPACE
   theorem keeps the precise inclusive \(L(U,X)\) basis and the neighbouring
   fragment distinctions (`logic-in-computer-science.tex:696--711`), and the
   later model-checking theorem explicitly obtains universal-path checking by
   complementing Sistla--Clarke's existential problem
   (`logic-in-computer-science.tex:799--811`).  The final five-way paragraph
   accurately separates Kamp's order expressiveness, Pnueli's transition-system
   proof rules and internal strict/inclusive tension, GPSS's strict language,
   Sistla--Clarke's inclusive operator-sensitive decision problems, and
   Alpern--Schneider's semantic property classes; it also forbids retroactive
   transfer of definitions, proofs, or terminology (`n-c-012.tex:3047--3060`).

No source-attribution, theorem-strength, hypothesis/domain, repair-ownership,
proof-ownership, or integration-boundary blocker remains in the reviewed
LaTeX.

VERDICT: ACCEPT
