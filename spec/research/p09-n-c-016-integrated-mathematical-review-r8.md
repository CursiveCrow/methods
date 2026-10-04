VERDICT: ACCEPT

## Scope and disposition

This is a fresh mathematical/definedness review of the frozen current 2,059-line `N-c-016` presentation, read directly as LaTeX source. No line-specific mathematical must-fix remains in the reviewed source. Acceptance is bounded to the definitions, constructions, claims, and source-strength boundaries actually present in the text and to their consistency with the authorized host and prerequisite definitions listed below.

## Bounded positive evidence

### 1. Clarke--Emerson: domains, indexed modalities, model checking, and factorization

- `n-c-016.tex` lines 41--60 fixes the positive process arity \(k\geq1\), types each \(A_i\subseteq S\times S\), defines \(A=\bigcup_iA_i\), states totality with both state quantifiers, and consequently gives infinite paths with an explicit adjacency condition. The computation tree, per-process skeleton, and finite global flowgraph are kept as three objects with different standings.
- Lines 62--124 give a state-formula grammar before using it, quantify \(EX_j\) over \(A_j\)-successors, quantify both until clauses over paths from the evaluation state, permit the \(i=0\) witness, and correctly identify the until as strong. The derived \(EX/AX\) forms retain \(k\geq1\), and the text correctly records that \(AX_i\) can be vacuous even though the union \(A\) is total.
- Lines 126--183 restrict the labelling procedure to finite \(M\), seed both until recurrences at the right-operand states, retain the required \(f_1\) guard in both directions, and distinguish the reconstructed existential recurrence from the source's displayed universal recurrence. Stabilization and the source's quadratic accounting are asserted only in the finite setting.
- Lines 199--234 keep the infinitary SCC result inside the finite setting and give the Hamiltonian reduction on the explicit base domain \(n\geq1\). The construction includes all original graph edges, the two fresh states, the terminal self-loop needed for an infinite semantic path, and both logical directions of the encoding. Its conclusion is only the source's stated \(\mathsf{NP}\)-hardness, not membership, completeness, or a later CTL* classification.
- Lines 236--318 distinguish the published tableau outline from a full correctness proof and type the `Blocks`/`Tiles` alternation without pretending that the omitted general process-indexed tile clauses were printed. Lines 320--416 likewise keep the worked mutual-exclusion construction separate from a general synthesis theorem; the indexed next modalities and the anti-vacuity conjunct in requirement group 6 have the correct logical direction.
- The repaired general factorization at lines 441--488 is total. For every duplicate propositional label class of size \(d\geq2\), the fresh discriminator has the stated domain \(\{0,\ldots,d\}\), has exactly one value proposition at every global node, is initialized at every designated initial node, and is assigned the target-node value on every global arc. The value \(0\) handles all nodes outside the duplicate class. For each process with \(m\geq1\) regions, a local guard omits only that process's source-region atom, retains the \(k-1\) other region components and every source auxiliary equality, and has the explicit nullary value `true`. The update map is complete, with absent component assignments interpreted as identity. Arcs are merged only when source region, target region, and the complete update agree; identity and nonidentity updates therefore cannot be collapsed. Guards remain state formulas and updates remain transition actions.
- Lines 490--502 accurately separate four evidentiary levels: printed labelling algorithm, two proposition-level proofs, abridged tableau outline, and worked factorization without a separate general correctness theorem.

### 2. Queille--Sifakis: retained-variable scope, finite and maximal executions, nullary families, and transformer algebra

- Lines 516--545 define an IPN as a Petri net plus guards and updates on the retained-variable vector \(\mathbf X\). Lines 525--527 explicitly exclude deleted internal variables of nonspecified types from that vector. Lines 560--564 separately type the example's scalar data value \(X\), the IPN vector \(\mathbf X\), the message records, and their bit projection; the two uses of \(X\) are no longer conflated.
- Lines 589--645 give the complete formula grammar before the temporal clauses, distinguish state operators from any later CTL path grammar, and define both finite and infinite executions. Maximal finite executions end at sinks. The actual-position domain \(D_s\) is explicitly finite or \(\mathbb N\), so no satisfaction predicate is ever applied to the fictitious post-terminal state \(\omega\). All four temporal clauses quantify over maximal executions from \(q\) and allow the current position.
- Lines 647--653 label the source's missing start/adjacency and Boolean interpretation clauses as omissions and distinguish the reader-facing completion from printed source text.
- Lines 655--691 type `Init`, `enable`, and `after` as state predicates and give eliminable finite-family definitions. The arity is allowed to be zero, with \(\bigvee\varnothing=\mathsf{false}\) and \(\bigwedge\varnothing=\mathsf{true}\). Consequently empty action families, empty process action sets, deadlock disjunctions, and universal liveness conjunctions all have stated truth values rather than undefined notation.
- Lines 711--775 preserve the quantifier direction of liveness, deadlock freedom, possible response, and inevitable response. They distinguish eventual enabledness from event occurrence and do not import fairness or the prose non-loss assumption into the transition semantics.
- Lines 777--839 type every transformer as a map \(\mathcal P(Q)\to\mathcal P(Q)\), define Boolean dual, identity, pointwise union/intersection, composition iterates, and both finite-iterate aggregates before use. The literal superscript \(x\) is defined as pointwise intersection and is not silently promoted to an unexplained fixed-point binder. The text makes no descending-chain claim for an arbitrary transformer. The four identities have the correct transformer directions, the existential factor excludes non-\(f\) sinks from `INEV`, and the printed image-finiteness hypothesis is attached to all four stated identities. The proof delegation to Sifakis 1979 is explicit.
- Lines 841--904 keep the analyzer's architecture, single worked computation, bounded supported variable classes, user iteration cap, possible no-answer result, and absence of an asymptotic theorem distinct. No capped approximation is presented as a proof.

### 3. Emerson--Halpern: structure classes, exact \(R\)-generation, CTL* ownership, and proof repairs

- Lines 917--994 type \(S\ne\varnothing\), \(X\ne\varnothing\), finite and infinite nonempty paths, the suffix operation, branching state truth, linear path truth, whole-model validity, and strong equivalence before their use. The two Lamport readings do not exchange state and path domains.
- Lines 996--1018 type the string domains \(S^*,S^+,S^\omega\), the shared fusion state, finite/infinite suffix pieces, and positive limit blocks. Compatibility and nonempty-path conditions are stated, so the concatenations and the infinite limit are defined.
- Lines 1019--1040 restrict \(R\)-generability to \(X\subseteq S^\omega\) and give the exact equality with all infinite paths generated by a total \(R\subseteq S\times S\). The equivalence is also restricted to infinite-path sets and has the necessary fourth right-hand conjunct, state completeness. This is mathematically required because a total relation produces a path from every state. The text separately explains the uses of fusion, limit, and state completeness and records rather than reproduces the source's `states from X` type defect.
- Lines 1051--1143 mutually generate state formulas and path formulas, state that only \(A/E\) return a path assertion to state standing, and evaluate the two formula sorts on states and sequences respectively. Current-inclusive \(F\) and strong \(U\), the false-at-a-finite-last-state next clause, and infinitely-many-position semantics are explicit. Path-formula evaluation is allowed on every nonempty finite or infinite sequence over \(S\); only \(A/E\) restrict to members of \(X\). The named CTL and associated linear fragments preserve those ownership rules.
- Lines 1145--1197 distinguish whole-model strong equivalence from pointwise state equivalence and state the fusion/state-completeness hypotheses of Proposition 4 in the direction in which each is used. The metalinguistic \(B(L)\) construction is not treated as an object-language connective.
- Lines 1199--1364 keep all expressiveness comparisons inside the declared structure class. Theorem 3's path-deletion contradiction has the correct implication direction. Theorem 4's segment recursion has an explicit positive-arity base case. For Theorems 5--6, the literal self-defeating printed targets, proof-supported targets, diagram dependency, and bad theorem cross-reference are each separated; no correction is attributed as literal source text. Theorem 7's bounded-formula invariants, reader-left Boolean cases, and reliance on cited Theorem 8 are stated at their actual strengths.
- Lines 1366--1500 keep fairness as a formula rather than a structural premise; distinguish the PL and MPL translations; exhibit the literal MPL \(U/X\) conflicts with concrete countervaluations; and refuse to infer Theorem 10 from those defective displays. The terminal-server formula is well typed and its existential alternatives have a real later use. The concluding application discussion is not promoted to a dominance, algorithmic, or complexity theorem.

### 4. Clarke--Grumberg--Peled acquisition limit

- Lines 1502--1523 use the 1999 item only for bibliographic identity, audited access state, and contents-page locators. They explicitly deny body-level support for grammar, algorithms, proofs, examples, or complexity. The 2001 chapter, 1996 survey, 2018 second edition, and Baier--Katoen book are not substituted for the missing first-edition body. The host's four decision-complexity classifications therefore remain supported by their independent citations, not by an unacquired book body.

### 5. Baier--Katoen: host bridge, empty state set, fixed points, worklists, witnesses, and complexity

- Lines 1536--1560 retain the source's six-component, action-labelled transition-system tuple and define `Post` before using terminality. The source's finite-system condition and standing no-terminal-state condition are not collapsed into a newly attributed source term.
- Lines 1562--1606 define the action-forgetting relation \(R_0\subseteq S\times S\), the valuation \(V_0:AP\to\mathcal P(S)\), the host alphabet choice, and every recursive constructor of the source-to-host translation before invoking the host method. Their standing is explicitly metalinguistic, and the translation maps the source's state formulas only to host CTL state formulas.
- Lines 1607--1623 prove the immediate `Post`/predecessor correspondence and separate all three domain cases needed by the host: nonempty plus no terminal states gives totality; source finiteness gives a finite host structure; \(S=\varnothing\) instead forces \(I=\varnothing\), empty satisfaction sets, and vacuous system satisfaction, and the host method is not instantiated. The source transition count \(K\) counts action-labelled triples, while the host parameter counts binary edges; the explicit inequality \(|R_0|\leq K\) prevents a representation-sensitive parameter identification.
- Lines 1625--1636 distinguish finite fragments, infinite fragments, maximal fragments from an arbitrary state, and initial maximal paths. Under the standing no-terminal-state hypothesis, every member of `Paths(s)` is infinite, matching the host path convention.
- Lines 1638--1685 give the CTL state/path recursion, including `true` and atom base cases, before its semantic recursion. Next and until have the correct operand types, and strong until permits the current-state witness. The system truth clause is the universal subset test and explicitly handles \(I=\varnothing\).
- Lines 1687--1705 state the structural-induction bridge only for nonempty \(S\), then invoke the finite host method only for finite nonempty \(S\). The returned satisfaction set and the host theorem's \(R_0\)- and translated-formula-sensitive bound are stated exactly.
- Lines 1707--1721 define ENF before Algorithm 14 uses it and preserve the exponential-expansion warning. The later linear-in-formula theorem is conditioned on direct modality handling, not on materializing the potentially exponential ENF rewrite.
- Lines 1723--1771 give the source's least-set direction for existential until and greatest-set direction for existential always with inclusion as the order. The displayed closure conditions have the correct directions. The semantic proof boundary is accurate: the nontrivial source arguments are summarized, elementary clauses are not called fully expanded, and the handbook's recursive-choice/cycle clarification is labelled as such.
- Lines 1773--1840 state all seven Algorithm 14 branches and then the increasing and decreasing chains. Algorithms 15--16 are distinguished from the naive loops. The count invariant is quantified only over the retained set \(T\), and its right side uses \(T\cup E\), which is exactly the unprocessed successor domain. The final global induction is explicitly a handbook assembly from Algorithm 13 and Theorem 6.23, not a separately printed source proof.
- Lines 1842--1891 give a total eight-state graph, define the propositional equality/inequality abbreviations eliminably, and compute both worked satisfaction sets with the correct least/greatest direction.
- Lines 1893--1907 retain finiteness, no terminals, predecessor-list representation, direct modality handling, and the separate initial-list test in the source's \(O((N+K)|\Phi|)\) theorem. No space theorem is inferred from the section heading.
- Lines 1909--1968 fix the Hamiltonian construction's base domain at \(n\geq1\), type \(V\) both as the finite initial-state set and proposition set exactly as the source construction requires, add the sink state and all sink edges needed for no terminal states, and give a positive-arity formula recursion with a \(k=1\) base. The satisfaction-set induction and system-level negated equivalence have both logical directions. The text correctly isolates the exponential enumeration and identifies the missing uniform construction premise in the source's informal \(\mathsf P=\mathsf{NP}\) inference.
- Lines 1970--2005 give the actual total witness systems, state the path that separates each pair, and keep the bounded-formula induction and second LTL witness at their reader-left/omitted strengths. Lines 2007--2042 restore the CTL* state/path recursion, evaluate state formulas only through the path's first state, and use a well-typed state formula for strictness. Theorem 6.83 is kept as a semantic embedding, not an algorithm. Theorem 6.84's atom-substitution step is expressly a reconstruction of the source's one-sentence appeal.
- Lines 2044--2059 inventory the source defects and close with the exact source-versus-handbook proof boundary; none of the repaired defective formulas is silently presented as literal source text.

### 6. Host and prerequisite consistency

- `temporal-epistemic-supplement.tex` lines 46--55 requires \(S\ne\varnothing\), total \(R\), and infinite maps \(\mathbb N\to S\). Lines 58--104 give the host CTL state syntax and semantics, and lines 129--164 give the CTL* state/path separation. The presentation's bridge respects all three constraints.
- `logic-in-computer-science.tex` lines 948--972 types both predecessor operations. Lines 974--1007 restrict the labelling method to finite total structures, bind fixed-point variables over \(\mathcal P(S)\), use least fixed points for both until forms and greatest fixed points for both always forms, and specify the correct empty/full starting approximants. Lines 1009--1017 state correctness and the binary-edge-sensitive bound.
- The host complexity theorem at lines 1029--1035 distinguishes four decision problems and relies on bibliography entries independent of the inaccessible 1999 body. The `N-c-016` input occurs later at host line 1519, so all reused definitions and theorems precede the presentation.

### 7. Supplied technical-name rule

The current source satisfies the supplied necessity/definition/standing/nonredundancy/use test at the actual introduction points:

- `synchronization skeleton` and `global system flowgraph` are motivated, defined, distinguished from ordinary control flow and from each other, assigned program/global-graph standing, and used by the factorization at lines 20--39 and 441--488;
- `model fragment` is exactly defined as a rooted finite DAG, distinguished from a complete model, and used as the checked unit for cycle closure at lines 396--405;
- `TURN` is introduced only to distinguish duplicate global labels, typed as an auxiliary program variable, distinguished from a temporal connective, and used by the resulting guards at lines 407--438;
- `IPN` is required to add data guards and updates to ordinary net control flow, exactly defined and used to compute the predecessor transformer at lines 516--535;
- `enable` and `after` are defined as unlike state predicates, their nonredundancy is explained, and all later specification families use the distinction at lines 655--663;
- suffix, fusion, limit, \(R\)-generability, and state completeness are exact structure properties rather than connectives, are distinguished by what each construction permits, and are used separately in the later proofs at lines 996--1040;
- the MPL `stage` is typed as a finite prefix, distinguished from a state and a connective, and used by both closure lemmas at lines 1402--1408;
- \(R_0,V_0,\operatorname{tr}\) are necessary type bridges, exactly eliminable, explicitly metalinguistic, distinguished from source objects, and immediately used at lines 1562--1606;
- the Boolean comparison signs in the worked graph are eliminable propositional abbreviations, add no new sort or atom, and are used immediately to parse the source formula at lines 1865--1878.

No hypothetical technical answer is named in lieu of an owed definition or theorem.

## Explicit non-claims

- This verdict does not claim a full correctness theorem for the published Clarke--Emerson tableau or general synthesis/factorization, a convergence or complexity theorem for CESAR, or any fairness premise not encoded in the relevant transition semantics.
- It does not turn cited, reader-left, proof-outline, or reconstructed steps in Emerson--Halpern or Baier--Katoen into complete local source proofs.
- It does not attribute any grammar, algorithm, theorem, proof, example, or complexity classification to the unacquired Clarke--Grumberg--Peled first-edition body.
- It does not claim a Baier--Katoen asymptotic space theorem, a CTL* model-checking algorithm from Theorems 6.83--6.84, or a uniform polynomial CTL translation where only formula-family existence was discussed.
- It does not establish TeX compilation, rendered-page correctness, typography, publication layout, independent execution of any historical tool, or correctness outside this frozen 2,059-line source and the exact dependencies read below.

## Substantive text read

- `handbook/parts/p09/presentations/n-c-016.tex`, lines 1--2059, complete through EOF.
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 945--1036 and 1500--1525.
- `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 42--190.
- `spec/research/p09-clarke-emerson-1981-source-note.md`, lines 1--884, complete through EOF.
- `spec/research/p09-queille-sifakis-1982-source-note.md`, lines 1--867, complete through EOF.
- `spec/research/p09-emerson-halpern-1986-source-note.md`, lines 1--729, complete through EOF.
- `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`, lines 1--470, complete through EOF.
- `spec/research/p09-baier-katoen-2008-ch6-source-note.md`, lines 1--1120, complete through EOF.
- `handbook/bib/handbook.bib`, lines 2393--2407, 2409--2422, 2424--2436, 2438--2447, 2449--2458, 4815--4824, 4826--4835, 4837--4846, and 4897--4906.
- This Round 8 report itself was read back completely through EOF after creation.

## Prohibitions observed

- No prior N-c-016 review or report of any round, including my own earlier work, was opened; no source-fidelity or publication report, admission/board/history file, parent conclusion, or other agent output was inspected.
- No agent was contacted and no work was delegated.
- No PDF, render, screenshot, page image, manuscript image, or historical publication file was opened or inspected.
- No web source was browsed, and no memory or prior-run context was consulted.
- No TeX build, test, checker, validator, repository script, hash operation, or executable historical source tool was run.
- No manuscript file or other repository work was modified. The sole written file is this Round 8 report.

REGISTER STATUS: OPEN
