# Edition 2026 C1 independent topic review

## Scope, identity, instructions, and verdict

Reviewer: the independent topic-specialist agent /root/edition_c1_topic_review. The actual execution model identifier, reasoning setting, and service configuration are unavailable to this reviewer; no configuration is inferred from the tool catalog.

Assigned artifact: handbook/parts/p09/presentations/n-c-010.tex, lines 1–615, with particular attention to the corrected query marking, completion procedure, and canonical-model argument at lines 127–593. I read the complete assigned passage, including lines 595–615. No assigned line remains unread. Line 616 is the next line outside this assignment; line 615 ends within the subsequent boundary discussion, so that later discussion receives no completeness verdict.

Whole-file SHA-256, checked before and after the mathematical examination:

645f9a718b66d740948436ca5309ad25b59d39ce63acc6c41a108549cbb8ffa1

My instructions were to review the frozen passage independently, seek semantic counterexamples, check all eleven rules, the quotient and witness construction, the countermodel, complexity, and the reasoning-task reductions, and write only this report. The parent allowed at most 45 minutes and requested a checkpoint within 15 minutes. I sent a checkpoint after the complete passage read and a second message after resolving the normalization-size issue. No subagent was used. No other C1 review output or author verdict was consulted. The manuscript and all other files were left unchanged. No software test, build, rendering, or formal proof checker was used.

Scoped verdict: **FAIL for the full assigned text as written**, because the unrestricted linear normalization-size claim has the explicit counterexample in C1-TOP-01. **PASS for the corrected marked decision criterion and its normalized-input soundness/completeness proof**, on this textual mathematical review. I found no counterexample to (Q), (D), (R), (F), or (T). The normalization issue does not refute the polynomial tractability conclusion: the stated rules still admit a polynomial written-size bound, but that weaker bound must be stated and justified rather than silently substituted for the printed linear claim.

This verdict concerns C1 textual mathematics. It does not admit the artifact formally, accept the remainder of N-c-010, establish whole-book correctness, or establish build, visual, rights, or publication acceptance.

## Material actually consulted

- The complete frozen LaTeX passage, lines 1–615. Reads were contiguous ranges 1–220, 221–430, and 431–615, with the opening range subsequently read again with line numbers.
- Baader–Brandt–Lutz, LTCS-05-01, printed pages 3–14, in the local layout extraction. This covers Table 1 and semantics, task reductions, normal form and Figure 1, Table 2, admissibility, soundness, completeness, and Theorem 8. I additionally extracted printed pages 5–6 directly from the pinned PDF to verify the precise normalization rules and input-size convention underlying C1-TOP-01.
- Baader–Brandt–Lutz, IJCAI 2005, printed pages 364–367, in the local layout extraction, with printed page 367 additionally extracted directly from the pinned PDF. This covers the source language, normal form, completion format, concrete examples, and the stated complexity result. Source assertions were checked as assertions of the source, not treated as correctness certificates.
- General earlier workflow guidance in the local memory registry was used only to maintain the distinction between textual review and other admission gates. It supplies no mathematical evidence or C1 verdict.

Primary source files and verified SHA-256 values:

- tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-2005.pdf: 4c9caa8c224506123b7ee06cfcc8f5759d3537f4c241bb7e6bddcb89e0727a5a
- tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-ltcs-05-01.pdf: 374d73eb848e556da759d89231385353996f44e6a6131f53d2794bb68d5aa3ba

The PDF skill was consulted for source-text inspection. This assignment expressly excludes rendering, and no layout-fidelity conclusion is made from the text extraction.

## Findings

### C1-TOP-01 — The full language does not support the claimed linear written output from NF1–NF7

Status: confirmed mathematical defect in the stated size bound. Severity: medium. File: handbook/parts/p09/presentations/n-c-010.tex. Principal lines: 121–124 and 566. Relevant hypotheses and rules: 28–38, 85–87, 101–119, and 211–217. The heading at line 84 also announces the stronger bound.

The concrete language requires positive predicate arities but supplies no uniform arity bound. Its basic descriptions include entire concrete atoms. The two-phase schedule does not abbreviate a large concrete atom merely because it is large.

For a fixed concrete domain, take

\[
\Delta^{\mathcal D}=\{0\},\qquad
P^{\mathcal D}=\{t_k:k\geq 1\},\qquad
t_k^{\mathcal D}=\{(0,\ldots,0)\}.
\]

Every predicate is universal at its arity. All finite conjunctions are satisfiable, every supported atom is implied, and convexity holds. Parsing and constraint decisions are polynomial. Thus this is one fixed p-admissible domain within the displayed hypotheses, not a varying sequence of unverified concrete-domain oracles.

For distinct feature names \(f_1,\ldots,f_k\) and concept names \(A_1,\ldots,A_k\), put

\[
X_k=t_k(f_1,\ldots,f_k),\qquad
\mathcal C_k=\{X_k\sqsubseteq A_1\sqcap\cdots\sqcap A_k\}.
\]

With ordinary binary conjunction syntax, the input has \(\Theta(k)\) symbol occurrences when names are unit-cost symbols. NF1–NF4 do nothing. NF5 does not apply because \(X_k\) is basic. Exhaustive NF7 produces exactly the \(k\) distinct GCIs

\[
X_k\sqsubseteq A_i\qquad(1\leq i\leq k).
\]

Each output GCI contains the \(k\)-argument atom in full, so the written output has \(\Theta(k^2)\) symbol occurrences. The family remains superlinear if names are encoded as strings rather than counted as unit-cost symbols. The schedule at lines 121–122 therefore does not suffice for the unrestricted linear-output assertion at lines 123–124.

The relevant source convention is explicit: LTCS-05-01 printed page 5 defines the size of a CBox by the number of symbols needed to write it down. Figure 1 on printed page 6 supplies the same rules and has no concrete-atom abbreviation rule, uniform arity premise, or shared-expression output representation. The source's own linearity assertion does not resolve this counterexample. The frozen handbook likewise declares no sharing representation or bounded-arity premise.

Required correction: revise the normalization statement and the complexity paragraph consistently. One option is to establish the polynomial written-size bound actually available for the displayed schedule and retain the resulting polynomial decision theorem. Another option is to retain linear normalization by adding an explicit conservative abbreviation step: replace each occurring concrete atom \(X\) by a fresh name \(A_X\), and retain the already normalized defining GCIs \(A_X\sqsubseteq X\) and \(X\sqsubseteq A_X\). Each full atom then need be written only in its definition before the remaining constructor normalization. That step requires its own size and model-expansion explanation and clear identification as an additional handbook construction. A bounded-arity assumption or an explicitly shared output representation would also change the claim, but neither is presently stated.

The correction must not merely replace the word “linear” in one location: line 566 invokes the same premise. For the unmodified schedule, the reason a polynomial bound remains available is that phase 1 leaves left sides with at most one existential constructor or one binary conjunction over basic descriptions; later splitting can copy these basic descriptions, but only polynomially many times. The quadratic family above already shows why linear written size cannot be recovered from the existing schedule alone.

### C1-TOP-02 — The normalization schema omits the range of B and the meaning of its size notation

Status: definition-before-use omission. Severity: low. File: handbook/parts/p09/presentations/n-c-010.tex. Lines: 101–123, particularly 116–119 and 123.

The explanation introduces hatted descriptions and fresh \(A,u\), but it does not declare the range of \(B\) in NF6–NF7. The intended schema must include basic antecedents such as \(\top\), nominals, and concrete atoms; treating \(B\) as a concept-name metavariable would leave, for example, \(\top\sqsubseteq P\sqcap Q\) without an applicable displayed normalization rule. Treating \(B\) as a basic-description or suitable general-concept metavariable makes the intended use possible. This is not an independently established semantic counterexample once that intended range is supplied.

The passage also calls a CBox a finite set and later uses \(|\mathcal C|\) for an application bound without defining a symbol-size convention. The source supplies that convention on printed page 5. If the expression were read as set cardinality, the single-axiom CBox \(\{A\sqsubseteq(P\sqcap Q)\sqcap R\}\) needs two NF7 applications although it has one member. Thus the intended measure must be made explicit.

Required correction: declare the normalization metavariable ranges before the rules, and define the size measure as written input length before the application bound. These clarifications do not resolve C1-TOP-01: that counterexample already uses the intended symbol-size measure and allows \(B\) to range over basic descriptions.

## Mathematical checks of the corrected procedure

### Query reductions and normalization semantics

Lines 127–138 correctly reduce the arbitrary query using one-sided fresh-name axioms. An original countermodel expands with \(A_0=C\) and \(B_0=D\); an expanded model satisfying \(A_0\) must satisfy \(C\), and satisfaction of \(D\) forces \(B_0\). Both implications have the correct direction.

The individual normalization replacements are conservative under their intended metavariable ranges. A fresh concept name can be interpreted by the replaced subdescription; for NF1 the fresh role can be interpreted as the indicated prefix composition. Conversely, the introduced inclusions imply the original inclusion after reduct. NF4 removes a tautology and NF7 uses the semantic equivalence between inclusion in an intersection and the two separate inclusions. The size defect above is not a failure of these model-expansion arguments.

Lines 142–169 correctly mark an arbitrary prospective \(A_0\)-instance by a fresh nominal. The reverse direction uses a counterexample element to interpret that nominal. The account of forced-empty \(A_0\) is correct: marked inconsistency entails the query and does not incorrectly assert that marking preserves every original model. The extra tautology ensures \(B_0\) is in the finite vocabulary.

### Every completion rule

| Rule | Result of direct check |
| --- | --- |
| CR1 | The existing subsumption invariant followed by the normalized GCI proves the added label. |
| CR2 | The two label invariants give membership in the GCI's intersection. |
| CR3 | The GCI supplies the existential witness required by the role-pair invariant. |
| CR4 | The existing role pair supplies a witness in the actual filler; its label invariant supplies the left-existential antecedent. |
| CR5 | A witness in a filler labelled bottom is impossible, so the source concept is empty. |
| CR6 | The path begins either at the assumed source instance or at an existing nominal. It therefore supplies an instance of the target. The shared nominal identifies that target instance with the source instance. The zero-edge case is covered by the definition. |
| CR7 | The values of the positive features form an assignment on exactly the required support, contradicting unsatisfiability. No extension to undefined features is needed. |
| CR8 | The support guard establishes both definedness and the correct concrete carrier for every feature of the conclusion. The concrete implication can then be applied soundly. |
| CR9 | A single feature value cannot inhabit two disjoint concrete carriers. |
| CR10 | The role-inclusion axiom preserves the existing witness edge. |
| CR11 | The particular first-edge target is an instance of the intermediate basic description, so its existential consequence supplies the second witness. Composition gives the required edge. |

The two invariants at lines 183–188 and their complete proof at lines 351–406 justify both success disjuncts of (D). The nominal-bottom disjunct correctly includes disconnected original nominals and the query nominal.

### Quotient, concrete witnesses, truth lemma, and countermodel

The retained set \(L\) at lines 410–423 includes every nominal and is closed under every final role pair. Backward CR5 propagation proves that no retained label contains bottom. For all retained descriptions, reachability from some nominal supplies both directions needed by CR6. Consequently the equality of labels used in the transitivity proof of \(\sim\) is justified.

The proof of (R), lines 450–462, legitimately fixes the final equivalence while inducting on the earlier first insertion of an edge. CR3 uses final label agreement; CR10 and CR11 use strictly earlier premise edges and final saturation. This avoids assuming that the equivalence was already available at insertion time. Only outgoing-edge transfer is needed: incoming targets may be represented by any member of their class.

At lines 465–486, satisfiability follows from absence of CR7. The finite set \(E_j\) contains exactly the omitted atoms whose features are all supported in domain \(j\). Convexity then supplies a simultaneous avoiding assignment, with the empty-\(E_j\) case separately covered by satisfiability. CR9 supplies the disjointness of feature supports across domains. There is no need to choose values for unsupported features.

The interpretation at lines 488–509 is well defined. The root nominal gives a nonempty abstract domain. The truth lemma at lines 511–531 is correct for top, bottom, names, nominals, and concrete atoms. In its unsupported-feature case, the feature is either undefined or assigned in another disjoint carrier; either makes that domain's atom false.

All four normalized GCI forms and both RI forms are verified at lines 534–557. In particular, the composition case replaces the source representative of the second witness edge by the target representative of the first edge using (R), so quotienting creates no unchecked composed edge. The root then satisfies \(A_0\) through the marking axiom and fails \(B_0\) by (T). The reduct at lines 559–563 is the required original countermodel.

### Adversarial cases traced by hand

These are symbolic semantic checks, not executable test results.

| Case | Construction and observed consequence |
| --- | --- |
| Empty queried concept | \(A\sqsubseteq\bot\) sends bottom to \(S(N_\ast)\) after marking. The query is correctly true for any right side. The more elaborate shared-nominal empty-concept example in lines 329–349 is also valid. |
| Disconnected contradiction | \(\{a\}\sqsubseteq P,\ \{a\}\sqsubseteq Q,\ P\sqcap Q\sqsubseteq\bot\) gives bottom in the original nominal even with no path from the query nominal. The second disjunct of (D) catches it. |
| Empty unreachable concept must not contaminate a nominal | With \(C\sqsubseteq\{a\},\ C\sqsubseteq P,\ \{a\}\sqsubseteq Q,\ P\sqcap Q\sqsubseteq\bot\), and no role edges to \(C\), the \(C\)-label becomes bottom. CR6 cannot copy it back into \(\{a\}\) because the required path to \(C\) is absent. A model with \(C=P=\varnothing\) exists. |
| Two shared nominals and transitivity | Retained descriptions with nominal labels respectively \(\{a\}\), both \(\{a\},\{b\}\), and \(\{b\}\) obtain equal labels under CR6. All three are in one quotient class; the transitivity argument does not assume a unique nominal per label. |
| Undefined feature and universal atom | \(\top_{\mathbb Q}(f)\sqsubseteq B\) does not force \(A\sqsubseteq B\). With \(f\) undefined at an \(A\)-instance, the GCI holds and \(B\) may be empty. CR8's support guard preserves this countermodel. |
| Feature defined in the wrong domain | A positive domain-1 atom defining \(f\) does not permit a domain-2 universal atom on \(f\) to be propagated. The domain-2 support guard fails, and the canonical assignment makes the domain-2 atom false. |
| Domain clash after a nominal merge | Two successors of the query root sharing \(\{a\}\), one forcing \(f\) into domain 1 and the other forcing it into domain 2, acquire both atoms through CR6. CR9 then produces bottom and CR5 returns it to the root. |
| Composed edge through equivalent fillers | For \(A\sqsubseteq\exists r.U,\ A\sqsubseteq\exists s.V,\ U\sqsubseteq\{a\},\ V\sqsubseteq\{a\},\ V\sqsubseteq\exists t.W,\ W\sqsubseteq P,\ r\circ t\sqsubseteq u,\ \exists u.P\sqsubseteq B\), CR6 transfers the existential trigger from \(V\) to \(U\), CR3 gives the \(t\)-edge, CR11 gives the \(u\)-edge from the root, and CR4 yields \(B\). This matches the semantic composition through the one individual \(a\). |

### Polynomial saturation and reasoning-task reductions

The entry count at lines 285–288 is correct: there are \(b(b+1)\) possible label memberships because top is already basic, and \(m_Rb^2\) role pairs. CR6 may add several memberships, but every successful application adds at least one new membership, so the stated application bound remains valid. All rule schemas have polynomially many candidates. Graph reachability and feature-support checks are polynomial, and the stated concrete-domain hypothesis supplies polynomial constraint tests. Thus the normalized-input completion cost is polynomial. Polynomially many marked name-pair runs also give a polynomial classification procedure.

The reductions at lines 577–593 are semantically correct. Singleton concepts express each ABox assertion exactly, without a unique-name assumption. A combined CBox is inconsistent exactly when it entails \(\top\sqsubseteq\bot\), because the abstract domain is nonempty. Instance checking reduces to the stated nominal subsumption, and concept satisfiability is the failure of subsumption by bottom. The fresh-name query reduction handles those non-atomic queries. Complementing the polynomial subsumption result is legitimate for the consistency and satisfiability decisions.

The concrete-domain examples at lines 595–608 agree with the consulted principal-source passage, including the corrected string-domain superscript. I did not independently reprove the polynomial concrete-constraint algorithms or the source propositions concerning their convexity; those are cited input hypotheses/examples, and the corrected main argument states exactly where admissibility is used.

## Final disposition

The corrected query marking, guarded concrete propagation, reachable quotient, concrete witnesses, truth lemma, normalized-model verification, and reasoning-task reductions withstand this review. The assigned text still requires the explicit normalization-bound repair in C1-TOP-01 and the notation clarifications in C1-TOP-02. No mathematical acceptance of later N-c-010 material is implied.
