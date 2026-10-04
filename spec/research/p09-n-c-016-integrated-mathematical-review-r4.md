VERDICT: REJECT

# Round 4 mathematical/definedness review: N-c-016

The repaired 1,967-line presentation closes the earlier structural gaps in its process arity, Hamiltonian constructions, finite-execution domain, transformer algebra, path domain, formula recursion, and CTL/LTL witness family. Three local definition/type defects nevertheless remain. They are confined to the Clarke--Emerson factorization paragraph and the Queille--Sifakis finite-action-family abbreviations; no theorem-strength or host-level rewrite is required.

## Line-specific must-fixes

1. **handbook/parts/p09/presentations/n-c-016.tex:441-450 — the same \(m\) counts two unrelated finite families.** Lines 442-444 use \(v_1,\ldots,v_m\) for the distinct global nodes carrying one duplicated label. Lines 446-450 immediately reuse \(R_1,\ldots,R_m\) for the regions of process \(P_i\) and quantify \(u,v\in\{1,\ldots,m\}\). Nothing establishes that the number of duplicate occurrences of a label equals the number of regions of a process. Consequently the later occurrence index \(r\), region indices \(u,v\), and their domains are not unambiguous. **Minimal repair:** use a fresh duplicate-count symbol, for example \(d\geq2\), in \(v_1,\ldots,v_d\) and \(1\leq r\leq d\); separately state that \(P_i\) has \(m\geq1\) regions \(R_1,\ldots,R_m\), with \(u,v\in\{1,\ldots,m\}\).

2. **handbook/parts/p09/presentations/n-c-016.tex:442-470 — \(Q\) is introduced as a propositional node label and then used as the target of a program assignment.** The phrase “where a label \(Q\) occurs” gives \(Q\) the standing of a global-state label, but \(Q:=r\) treats the same symbol as an assignable auxiliary variable. A set/conjunction of propositional labels is not an integer-valued program variable, and no fresh variable or value domain is introduced. This also fails the supplied technical-name rule at definition and standing: the needed discriminator is motivated and used, but its mathematical sort is not defined. **Minimal repair:** for each duplicated label \(Q\), introduce a fresh auxiliary variable, say \(z_Q\), with value domain \(\{1,\ldots,d\}\); add the state-label component \(z_Q=r\) to \(v_r\), assign \(z_Q:=r\) on every incoming arc to \(v_r\), and replace the copied assignment at line 470 by \(z_Q:=r\). Keep \(Q\) solely as the original propositional label. If a duplicated node is initial and has no incoming arc, state its initial \(z_Q\)-value explicitly.

3. **handbook/parts/p09/presentations/n-c-016.tex:647-668, 694-704 — the finite action-family arity and the set-valued process abbreviation are not defined exactly.** The display introduces \(a_1,\ldots,a_k\) without rebinding \(k\), writes \(\bigvee_i\) and \(\bigwedge_i\) without an index range, and then applies the tuple notation \(\operatorname{enable}(a_1,\ldots,a_k)\) to the set \(A(\mathcal P)\). The nullary truth values at lines 660-668 determine the empty results but do not define the family index or the tuple/set overload. **Minimal repair:** write “for every \(k\in\mathbb N\) and finite family \((a_i)_{i=1}^k\)” and replace the unbounded operators by \(\bigvee_{i=1}^k\) and \(\bigwedge_{i=1}^k\). Define the process abbreviation directly by

   \[
   \operatorname{enable}\mathcal P
   :=\bigvee_{a\in A(\mathcal P)}\operatorname{enable}a,
   \]

   with the already stated empty-disjunction convention. Define \(\operatorname{after}\) analogously on a finite family or explicitly say that any enumeration of a finite action set may be used; commutativity makes the result enumeration-independent.

These three findings are exhaustive for this review. No other line-specific must-fix remains.

## Bounded positive evidence

- **Clarke--Emerson domains and graph constructions:** lines 41-65 now fix \(k\geq1\) before the process-indexed structure, union, and grammar. Lines 208-234 fix \(n\geq1\), retain the original directed edges, add exactly the fresh-source, vertex-to-sink, and sink-loop edges, type every label, and prove both directions of the Hamiltonian-path correspondence at NP-hardness strength only. Lines 449-468 now use distinct source/target region indices \(u,v\) and retain the \(k=1\) empty-conjunction value; findings 1-2 concern only the neighboring duplicate-label discriminator.

- **Fixed-point directions:** the guarded Clarke--Emerson \(A[U]\) and reconstructed \(E[U]\) iterations at lines 137-183 grow from the right operand and stabilize in the correct direction. The Baier--Katoen least/greatest characterizations at lines 1632-1680, the increasing/decreasing chains at lines 1712-1725, and the worklist invariant at lines 1725-1738 agree with the host's \(\mu/\nu\) clauses at logic-in-computer-science.tex:974-1005.

- **Finite and infinite execution domains:** Queille--Sifakis executions now have start, adjacency, maximality, and the actual-position domain \(D_s\) at lines 592-608. The four temporal clauses quantify only over \(D_s\), so no satisfaction judgment is formed at the fictitious post-terminal state. Emerson--Halpern path semantics explicitly range over nonempty finite or infinite sequences at lines 1030-1069. Baier--Katoen maximal paths are infinite under the no-terminal-state hypothesis at lines 1554-1565.

- **Pointwise transformer algebra and image-finiteness:** lines 754-816 type \(\operatorname{pre}\), its Boolean dual, \(\operatorname{Id}\), pointwise transformer union/intersection, finite iterates, \(h^*\), and \(h^x\). The text correctly declines to treat \(h^x\) as an unexplained greatest-fixed-point binder or to assert a descending chain for arbitrary \(h\). Image-finiteness remains an explicit hypothesis of both Queille--Sifakis propositions, and their proofs remain delegated to Sifakis 1979.

- **Formula recursion and nullary cases:** the Emerson--Halpern segment forms now have the explicit positive-arity base \([p_1]=Gp_1\) and recursion for \(n\geq2\) at lines 1198-1207. The Baier--Katoen Hamiltonian formula has \(n\geq1\), the unary base for \(\Psi\), and a nonempty permutation disjunction at lines 1818-1865. The Queille--Sifakis empty disjunction/conjunction truth values are correct at lines 660-668; finding 3 asks only that their surrounding family binder and set application be made exact.

- **CTL and CTL* ownership:** the prerequisite at temporal-epistemic-supplement.tex:46-55, 58-104, and 129-164 separates states, infinite paths, CTL state formulas, and CTL* path formulas. The source-specific Clarke--Emerson indexed CTL grammar at lines 62-124, Emerson--Halpern mutual grammar at lines 1006-1098, and Baier--Katoen CTL/CTL* grammars at lines 1567-1614 and 1915-1950 preserve the appropriate state/path constructors and non-strict strong-until bases.

- **Witness systems and logical directions:** lines 1878-1903 now give separate \(TS_0,TS'_0\) bases, separate primed/unprimed fresh states for \(n>0\), the exact attachment vertex \(s'_{n-1}\), and all new edges. The LTL persistence direction, the \(\forall\Box\exists\Diamond a\) trace argument, and the CTL* substitution argument at lines 1905-1950 have the correct directions while retaining the reader-left or one-sentence proof boundaries.

- **Proof, citation, and reconstruction strength:** Clarke--Emerson's defective displayed universal recurrence and reconstructed existential recurrence are explicitly separated; its tableau remains an outline and its synthesis remains a worked construction rather than a general correctness theorem. Queille--Sifakis's execution completion is labelled handbook-supplied, its fixed-point proofs remain external, and its analyzer may return no answer. Emerson--Halpern's printed theorem-target and MPL-clause defects remain literal-source defects with proof-supported repairs clearly separated. Baier--Katoen's global induction and CTL* substitution step are explicitly reader reconstructions, while Theorems 6.18, 6.21, and 6.84 retain their actual omissions.

- **Representation-sensitive complexity:** lines 1549-1552 distinguish action-labelled transition triples \(K\) from the collapsed binary edge set \(R_0\). Lines 1802-1816 retain finite/no-terminal hypotheses, predecessor linked lists, direct modality handling, and the absence of a printed asymptotic space theorem. Lines 1866-1876 correctly identify the missing uniformity premise in the source's succinctness argument.

- **Empty-state bridge and host consistency:** lines 1517-1552 type \(R_0,V_0,\mathcal K_0\), instantiate the nonempty host structure only when \(S\ne\varnothing\), and treat \(S=\varnothing\) separately with \(I=\varnothing\), empty satisfaction sets, and vacuous system satisfaction. This matches temporal-epistemic-supplement.tex:46-55 and the finite total host method at logic-in-computer-science.tex:948-1015.

- **1999 acquisition boundary:** lines 1457-1478 attribute no grammar, semantic clause, algorithm, theorem, proof, example, or complexity result to the unacquired Clarke--Grumberg--Peled first-edition body. Contents metadata remains only a locator, and the 1996 survey, 2001 handbook chapter, 2008 textbook, and 2018 second edition are not substituted.

- **Technical names apart from finding 2:** synchronization skeleton/global system flowgraph, model fragment, interpreted Petri net, the action-event labels, \(D_s\), the closure properties and state completeness, strongly equivalent, MPL stage, \(R_0,V_0,\mathcal K_0\), and the Boolean comparison abbreviations each have a local definition, mathematical standing, distinction from neighboring notions, and actual later use. No hypothetical artifact is named.

## Text evidence read

Every item below was read directly as text:

- handbook/parts/p09/presentations/n-c-016.tex: lines 1-1967, complete through EOF.
- handbook/parts/p09/logic-in-computer-science.tex: lines 945-1040 and 1505-1530.
- handbook/parts/p08/temporal-epistemic-supplement.tex: lines 42-190.
- spec/research/p09-clarke-emerson-1981-source-note.md: lines 1-884, complete through EOF.
- spec/research/p09-queille-sifakis-1982-source-note.md: lines 1-867, complete through EOF.
- spec/research/p09-emerson-halpern-1986-source-note.md: lines 1-729, complete through EOF.
- spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md: lines 1-470, complete through EOF.
- spec/research/p09-baier-katoen-2008-ch6-source-note.md: lines 1-1120, complete through EOF.
- handbook/bib/handbook.bib: lines 2393-2458, 4815-4846, and 4897-4906.

No other manuscript, research, review, or source-content file supplied substantive evidence.

## Prohibitions and non-claims

- No prior N-c-016 review report, including any earlier mathematical review, was opened. No source-fidelity report, publication report, board, admission, handoff, history file, parent conclusion, or other agent output was opened.
- No agent was contacted, inspected, or delegated to.
- No manuscript or source PDF, render, screenshot, page image, or historical publication file was opened or inspected. Descriptions of earlier visual/source work were read only as text in the five controlling notes.
- No web source was opened or queried.
- No TeX build, test, checker, validator, hash, repository script, executable source tool, or source program was run. Shell use was limited to direct text reads and checking that the requested output path did not already exist.
- No manuscript, host, prerequisite, note, bibliography, or other repository file was modified. This report is the sole output.
- This verdict establishes mathematical/definedness, source-strength, host-consistency, and technical-name findings only. It is not a build, static-check, visual-publication, rights, fresh-acquisition, or independent historical-source verdict.

REGISTER STATUS: OPEN
