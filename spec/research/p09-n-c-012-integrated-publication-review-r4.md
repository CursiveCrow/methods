# N-c-012 Round 4 blind publication review

## Review basis and constraints

I read handbook/parts/p09/presentations/n-c-012.tex directly from line 1 through line 3024 (EOF). I also directly read the current controlling passages of handbook/parts/p09/logic-in-computer-science.tex: the chapter standing at lines 1--47; the complete temporal-logic, past-semantics, strict/inclusive bridge, public-theorem, safety/liveness, automata, model-checking, and presentation-input passage at lines 602--909; and the public complexity/publication boundary and closing navigation/register passage at lines 2200--2394.

This was a blind actual-LaTeX review. I did not read an earlier integrated review report or a manuscript PDF; I did not open a PNG, page image, render, or screenshot; and I did not invoke a TeX command, build, repository script, test, checker, hash, or board review.

## Blocking finding

### N-C-012-R4-01 -- The finite-prefix certificate conflates graph nodes with path occurrences

The \(R\)-structure definition permits paths to revisit a graph node: a path is simply an infinite node sequence satisfying \(R\) (n-c-012.tex lines 1936--1949). The NP certificate likewise guesses an unrestricted finite path prefix \(p'\) (n-c-012.tex lines 2127--2139). Nevertheless, the checking account creates one set \(\operatorname{label}(x)\) for each **node** \(x\) occurring in \(p'\) or in \(C\) (n-c-012.tex lines 2140--2143), while its \(F\)-clause asks for a witness at or after “that occurrence” of \(x\) in \(p'\) (n-c-012.tex lines 2153--2160). If \(x\) occurs twice, there is no bound occurrence to which “that occurrence” refers, and a single node-indexed label cannot record the generally different future truth at the two positions. The labels are load-bearing: the presentation says that the machine accepts exactly when the input formula is in the start label (n-c-012.tex lines 2174--2179).

This is a mathematical defect, not only a wording preference. Let

\[
 N=\{x,u,c\},\qquad
 R=\{(x,u),(x,c),(u,x),(c,c)\},
\]

start at \(x\), let atom \(a\) hold only at \(u\), and let atom \(b\) hold only at \(x\). The relation is total. The path

\[
 x,u,x,c,c,\ldots
\]

satisfies the \(L(F)\)-formula

\[
 Fa\ \land\ F\bigl(b\land\neg Fa\bigr).
\]

At the first occurrence of \(x\), \(Fa\) is true because \(u\) follows. At the second occurrence of \(x\), \(b\land\neg Fa\) is true because the remaining suffix contains no \(a\)-state. A single \(\operatorname{label}(x)\) cannot contain \(Fa\) for the first occurrence and its single-negation mate \(\neg Fa\) for the second; the manuscript's own negation rule makes those alternatives exclusive (n-c-012.tex lines 2146--2149). Taking \(p'=(x,u,x)\) and \(C=\{c\}\) also satisfies the separately added directed-cycle requirement, so the problem is independent of the source-level singleton-SCC repair at lines 2181--2198.

Before publication, the account owes an occurrence-indexed finite-prefix check: truth data for positions of \(p'\) must be kept distinct from the state summaries for \(C\), and the inclusive-\(F\) rule must quantify over a specified prefix position and its later positions. Until that artifact is supplied, the stated certificate is ill-defined on repeated nodes and incomplete on the displayed example. Under the workspace five-part rule, the current \(\operatorname{label}(x)\) also fails exact definition and standing: \(x\) is introduced as a graph node, but the subsequent clause silently needs an occurrence.

## Required focused audits

### Technical-name rule

I applied the necessity/definition/standing/nonredundancy/use test at the introductions and load-bearing later uses. The node/occurrence collapse above is the only blocking failure I found. In particular, source-reported undefined material is not silently adopted: GPSS's \(U',S'\) remain only source-reported symbols with no derived handbook use (n-c-012.tex lines 1531--1543), and the source's unformalized event-expression step is explicitly identified as an owed grammar/semantics and an omitted proof core (n-c-012.tex lines 1625--1636).

### \(K_b\), P1, and proof ownership

- P1 is stated as reachable-state induction with its initial-state premise, universally closed preservation premise, and conclusion over \(X\) (n-c-012.tex lines 433--450 and 480--489). It is not confused with P2 or with a temporal connective.
- \(K_b\) is defined exactly as the pure propositional future theorem system with derived \(F\), G1--G3, RT, RG, and MP; its standing and distinction from \(DX,DUX\) are explicit (n-c-012.tex lines 819--898). The linear-execution/S4 model-class mismatch is demonstrated rather than hidden (n-c-012.tex lines 900--928).
- The later sentence that Theorem 3 says \(K_b\) is at least as strong as ER is immediately treated as an under-specified source assertion. The text identifies the missing system-dependent rule E and expressly denies an embedding theorem for bare \(K_b\) (n-c-012.tex lines 1020--1029). The finite-system result separately says “\(K_b\) ... extended by” the system-dependent material (n-c-012.tex lines 1116--1121). No unqualified embedding claim survives.
- Handbook repairs, counterexamples, and source proof sketches are repeatedly owned at their actual standing: Kamp's parity repair at lines 272--341 and 356--361; Pnueli's P2 counterexamples and completeness gaps at lines 517--541 and 618--676; GPSS's outline/referral boundaries at lines 1545--1649 and 1694--1776; Sistla--Clarke's handbook graph correction at lines 2181--2198; and Alpern--Schneider's repaired corollary at lines 2942--2975.

### Strict/inclusive conventions, model domains, and public theorem strength

- Kamp's witness-strict, open-interval, source-operand convention is explicit (n-c-012.tex lines 74--98). Pnueli's strict \(\leadsto\), inclusive \(F,G\), and unresolved internal tensions are separated (n-c-012.tex lines 461--478, 668--676, and 819--845). GPSS's strict convention, repaired misprinted inequality, and supplied past dual are owned at lines 1216--1280; the exact discrete bridge is at lines 1296--1317. Sistla--Clarke's \(U,S,F\) are explicitly inclusive at lines 1867--1927.
- The four GPSS result domains--point zero, future formulas, discrete complete orders, and arbitrary orders with undefined additional symbols--remain separate (n-c-012.tex lines 1477--1543). The conflicting \(\mathsf U^0\) displays are not normalized into a fictitious coherent operator (n-c-012.tex lines 1778--1838).
- The chapter's public past semantics and exact recursive strict/inclusive translations are stated at logic-in-computer-science.tex lines 605--685. Its public first-order theorem fixes pointed \(\mathbb N\)-words and both directions (logic-in-computer-science.tex lines 687--694); its PSPACE theorem fixes the inclusive \(L(U,X)\) basis and separately scopes adjacent fragments (logic-in-computer-science.tex lines 696--711). The automata-theoretic model-checking method and theorem distinguish existential counterexamples from universal satisfaction, combined input from fixed-formula structure complexity, and nonempty accepting cycles (logic-in-computer-science.tex lines 764--812).

### ETL and the epsilon boundary

- The presentation explicitly makes nonempty emission a handbook restriction because the printed consistency rule has no empty-word case, excludes the epsilon-admitting extension, and gives a linear one-terminal normalization (n-c-012.tex lines 2432--2447).
- \(\mathsf{ETL}\) is exactly defined as a formula class, not a grammar, automaton, or proof system; its grammar-indexed formation distinction and later theorem/table uses are stated at the introduction (n-c-012.tex lines 2448--2464). Finite and infinite generated witnesses are typed separately (n-c-012.tex lines 2465--2483).
- The theorem scope again fixes the reconstructed nonempty-emission domain and separates constructor arity from complete encoded input length (n-c-012.tex lines 2546--2559). The final source table carries the same convention rather than leaking an epsilon case into \(\mathsf{ETL}\)'s PSPACE row (n-c-012.tex lines 2603--2634). I found no ETL scope or ownership blocker.

### Safety/liveness, transitions, and input seam

- The chapter definition classifies word properties semantically, not formulas by typography (logic-in-computer-science.tex lines 713--721). The presentation supplies the nonempty state-space boundary, exact bad-prefix and continuation quantifiers, topology, decomposition, expressibility qualifications, and corrected closure hypothesis (n-c-012.tex lines 2638--2708, 2844--2907, and 2942--2995).
- The final five-presentation boundary correctly keeps Kamp expressiveness, Pnueli proof rules, GPSS strict time, Sistla--Clarke's inclusive decision problems, and Alpern--Schneider semantic properties from inheriting one another's definitions or proofs (n-c-012.tex lines 3011--3024).
- The chapter inputs N-c-012 only after the public LTL/past, automata, and model-checking surface (logic-in-computer-science.tex lines 602--904), followed by the adjacent source presentations at lines 905--907. Cross-references used by N-c-012 therefore meet the current input seam.

### Publication-debris search

The requested acquisition/hash/audit/test/board/review/render/build/campaign-status search found no workflow or campaign-status prose in n-c-012.tex. The literal hits there are ordinary mathematical or expository uses: formulas “built” by a reduction (line 139), “proof status” (line 343), a semantic procedure that “tests continuations” (line 1050), and an assumption not “built into” definitions (line 2727). In the controlling chapter, the solver-status sentence at lines 2330--2335 is substantive publication-boundary guidance, while \(\backslash\mathrm{input}\{generated/audit-p09\}\) at line 2394 is a TeX input directive rather than N-c-012 prose. Neither is campaign debris in the reviewed presentation.

VERDICT: REJECT -- N-C-012-R4-01
