# Edition 2026 C1: EL++ query marking and partial-feature completion

## Checkpoint, 7 September 2026

Owned manuscript: `handbook/parts/p09/presentations/n-c-010.tex`, initial SHA-256 `A5E7135DED58AA5E8778AC7A71E0B9BBBC3BA57E62FA7970E4FCC3BDB4493F93`.

The current EL++ language, normal forms, CR1–CR11, claimed criterion and countermodel at original lines 18–303 have been read. The seven-GCI counterexample in `spec/inventory/2026-09-06/additional-current-content-findings.md` has been checked against those rules. The following correction has been derived; the complete manuscript insertion is being prepared. No independent acceptance is claimed.

## Primary-source evidence

- Baader, Brandt and Lutz, *Pushing the EL Envelope*, IJCAI-05, pp. 364–369, [official conference PDF](https://www.ijcai.org/Proceedings/05/Papers/0372.pdf). Held PDF: `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-2005.pdf`, SHA-256 `4C9CAA8C224506123B7EE06CFCC8F5759D3537F4C241BB7E6BDDCB89E0727A5A`. Table 1, Table 2, Lemmas 1–3 and Theorem 4 distinguish syntax, finite completion, the original criterion, and the polynomial-time claim.
- The expressly accompanying [LTCS-05-01 report](https://lat.inf.tu-dresden.de/research/reports/2005/BaaderBrandtLutz-LTCS-05-01.pdf), held at `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-ltcs-05-01.pdf`, current verified SHA-256 `374D73EB848E556DA759D89231385353996F44E6A6131F53D2794BB68D5AA3BA`. Printed pp. 3–4 fix partial features and reasoning tasks; pp. 5–6 give normalization; pp. 7–8 give the reachability guard and criterion; pp. 9–11 give soundness; pp. 11–14 give the quotient model and complexity result. The held layout extraction was read at lines 144–253, 311–434 and 435–664 for these passages. The report's source statements are evidence for the original procedure, not an independent validation of its disputed claims.

The source defines features as partial functions (report printed p. 3; extraction 184–195) but reads concrete implication as first-order implication over total variable assignments (printed p. 8; extraction 372–390). That creates a second soundness issue relevant to the owned theorem.

## Nominal correction derived

For normalized input CBox C and atomic query A0 <= B0, choose a fresh individual a* and use K = C union {{a*} <= A0, B0 <= B0}. The last tautology only registers the queried name. Query the saturated label of N* = {a*}, not the old unmarked A0 label. The equivalence is:

`C entails A0 <= B0` iff `K entails N* <= B0`.

Forward: every K-model is a C-model and its named a* is in A0. Reverse: a C-countermodel with x in A0 minus B0 expands by a*=x. The extension is query-dependent and need not preserve existence of models when A0 is empty; that is exactly the vacuous-subsumption case. The prior one-way fresh-concept reduction and ordinary conservative normalization preserve the indicated query, as shown by choosing the fresh concepts to denote the original descriptions in a countermodel.

After completion, accept iff B0 is in S(N*) or bottom belongs to S(N) for some occurring nominal N (including N*). All canonical nodes are those reached by role edges from some nominal. Hence every retained target D is reachable from a nominal, so the original CR6 guard is available in both directions whenever two retained labels share a nominal. Their labels coincide, the identity-or-common-nominal relation is an equivalence, and a derivation-history induction transfers their outgoing role edges. Bottom at any retained node propagates by CR5 to a nominal. The marked root ensures the quotient domain is nonempty.

In the seven-GCI example, the marker inherits A, creates edges to C and D, and makes both successors nominal-reachable. CR6 transfers P and Q between their common-a labels; the clash produces bottom and CR5 propagates it to the marker. The original CBox can still have A empty and a model. This is consistent with the query equivalence rather than a contradiction to conservativity.

## Necessary adjacent correction: CR8 and partial features

Let F_j(C) be exactly the feature names occurring in positive domain-j atoms already in S(C). Add an atom X by CR8 only when all its features belong to F_j(C) and con_j(S(C)) implies X in domain j. CR7 tests finite-support constraints, with the empty conjunction satisfied by the empty assignment.

Without the added guard, a universally true concrete atom top_Q(f) occurring in `top_Q(f) <= B` can be inferred from an empty conjunction at an A-node. But a one-element model with A true, B false and f undefined satisfies that GCI, so A <= B is not entailed. The unguarded step is unsound even without nominals. The source's Q example explicitly contains the universal unary predicate, so this is within its language, not an imported datatype.

For the corrected countermodel, solve each domain-j conjunction on F_j(C), avoiding all finitely many absent basic atoms whose features lie in F_j(C). CR7 supplies satisfiability. If every solution satisfied at least one absent atom, convexity would imply one of them, contradicting saturation under guarded CR8. Features outside F_j(C) are undefined or take values in a disjoint other domain, so other absent domain-j atoms are false automatically. CR9 ensures that one feature never receives values from two different domains at the same quotient point. Only finitely many assignments are selected; no global choice of representatives is needed.

Root explicitly authorized this adjacent correction as necessary for the owned theorem. The complete rule-by-rule soundness, quotient truth lemma, GCI/RI verification and polynomial bound are the remaining incorporation work at this checkpoint. No manuscript render or software test has been used.

## Historical source criterion retained as provenance

The source's original criterion was

\[
 A\sqsubseteq_{\mathcal C}B
 \quad\Longleftrightarrow\quad
 S(A)\cap\{B,\bot\}\ne\varnothing
 \ \lor\
 \exists\{a\}\in\mathsf{BC}_{\mathcal C}\;
       \bot\in S(\{a\}).
\]

It was asserted for the unmarked input and simultaneous classification. On the seven-GCI example the unmarked fixed point has S(A)={A,top}, S(C)={C,top,{a},P}, S(D)={D,top,{a},Q} and only the role edges (A,C) and (A,D). No nominal has an outgoing edge; neither C nor D reaches the other. CR6 therefore does not combine their labels, although every A-instance would force their witnesses to coincide. The quotient argument's inference from shared nominal to equal saturated labels is invalid for this unmarked reachable set.

The active manuscript replaces that criterion directly by (D), querying the new nominal under the marked input. It retains the sound guarded CR6 rule. No false criterion followed by a reader repair remains in that passage. The old source criterion is recorded here only as correction provenance. The previously noted source CR11 index, role interpretation, feature evaluation and rule-number slips are resolved in the active typed definitions and proof; the historical source note retains their exact readings.

## First authored freeze and proof structure

The complete correction was saved before the fifteen-minute checkpoint. Saved manuscript SHA-256 after full read-back:

    645F9A718B66D740948436CA5309AD25B59D39CE63ACC6C41A108549CBB8FFA1

The current named destinations and ranges are:

| Actual manuscript range | Supplied content |
| --- | --- |
| 8–23 | Exact source/report identity and attribution of the two handbook amendments. |
| 127–138 | Both directions of fresh-concept query normalization; explicit use of the cited conservative NF reduction. |
| 140–169, sec:p09-elpp-query-marking | Fresh individual, marked CBox, query equivalence (Q), exact queried label, and vacuous subsumption when the original queried concept is empty. |
| 171–217 | Finite source state, global-nominal reachability, finite feature supports, empty constraints, and the positive-arity/convexity conventions. |
| 219–281, sec:p09-elpp-partial-features | Partial-feature counterexample, every completion rule, and corrected CR8 with all feature-support premises. |
| 283–310, sec:p09-elpp-query-correctness | Slot bound, polynomial rule tests, and decision criterion (D), including disconnected global nominal inconsistency. |
| 312–349 | Conjunction/role-composition run and the complete repaired seven-GCI nominal run. |
| 351–406 | Invariant proof for every rule and soundness of each acceptance disjunct. |
| 408–462 | Nonempty nominal-reachable domain, backward bottom propagation, equivalence relation, final label equality, and derivation-history proof of outgoing-edge agreement. |
| 464–531 | Finite-support convex witness lemma, partial feature interpretation and full basic-description truth equivalence, including undefined/wrong-domain features. |
| 533–563 | Verification of all four normalized GCI forms, both RI forms, and a countermodel to the marked query when neither disjunct holds. |
| 565–593 | Polynomial classification by marked runs; direct singleton-GCI encodings of the ABox and all four reasoning-task reductions. |

The actual modified LaTeX was read back sequentially in ranges 1–195, 195–397 and 397–615. The final small clarifications were then read at 185–218, 281–294, 509–519 and 575–596: nonempty reachability sequences, nonempty disjunction in convexity, a role-count symbol distinct from a role name, the exact truth-lemma domain, and the explicit union defining the ABox CBox.

The old normalization algorithms and the later concrete-domain examples, hardness comparisons, DL-Lite, DLP and OWL material were not rewritten as part of C1. Normalization remains a precisely cited source dependency; the fresh-concept and fresh-nominal query-preservation steps are supplied here rather than delegated to that citation.

## Mathematical edge cases checked from the written construction

- **Empty original CBox, distinct queried names:** the marker label contains the marker, top and A0; no B0 or bottom is forced. The one-class countermodel interprets A0 true and B0 false.
- **Reflexive query A0 <= A0:** CR1 puts the queried name in the marker label, so the first disjunct holds.
- **Forced empty A0:** marking and CR1/CR5 propagate bottom to the marker. The original CBox may remain satisfiable, as the seven-GCI example explicitly demonstrates.
- **Disconnected inconsistent nominal:** a GCI {a} <= bottom triggers the global second disjunct even without an edge from the query marker to {a}. The procedure does not rely on propagating that contradiction specifically to the query marker.
- **No original individuals or roles:** the fresh marker exists, its zero-edge path places it in L, and the quotient remains nonempty. The statement proved is preservation of the queried subsumption; arbitrary original models need not expand to marked models.
- **Nominal chains and merged outgoing edges:** equivalence is taken only on final nominal-reachable labels. The transfer induction uses final equivalence and final saturation, so it does not assume that merged labels were equal before a role edge was first added.
- **No concrete atoms/no concrete domains:** each feature support is empty; features remain undefined, and the concrete part of the proof is vacuous. Empty constraints use the empty assignment.
- **Unrequired feature:** an absent atom with an unrequired feature is false because the feature is undefined or takes a value in a disjoint other domain. Total concrete assignments are never silently imposed on all abstract features.
- **Feature required in two concrete domains:** CR9 derives bottom. No countermodel feature is assigned two conflicting concrete values.
- **Absent atom on already required features:** guarded CR8 non-applicability and convexity jointly supply one assignment avoiding all such absent atoms. This does not require an effective algorithm for extracting concrete values; the decision algorithm only uses the stipulated polynomial satisfiability/implication tests.
- **Role composition through a merged nominal class:** outgoing agreement transfers the second edge to the representative reached by the first edge, allowing CR11 with a literally matching middle node.
- **Empty ABox:** its CBox translation is the original CBox. Consistency remains non-entailment of top <= bottom, using the stipulated nonempty abstract domain.

These are readings and finite mathematical derivations from the saved procedure, not software tests.

## Remaining scope and continuation

At the first authored freeze, no unresolved step was identified in the amended query-marking/partial-feature soundness and countermodel argument during this author's read-back. Subsequent independent review found the normalization-interface failures recorded in the next section. The first hash and its line ranges remain historical evidence. This author does not issue independent acceptance of their own insertion.

The source's full p-admissibility proofs for its rational/string domains remain at their existing separate source standing. The C1 correction does not complete all other N-c-010 source-presentation obligations. No shared host, bibliography, style, register, inventory file or other agent-owned file was edited.

## Second authoring round: normalization repair checkpoint

All three first-round reports were read in full: edition-2026-c1-source-review.md, edition-2026-c1-topic-review.md and edition-2026-c1-publication-text-review.md under spec/verification. Their verdicts bind the first frozen hash only. The source seat passed that scope; the topic and publication seats required normalization repairs. The topic reviewer supplied the unbounded-arity family X_k <= A_1 intersect ... intersect A_k, whose unmodified NF7 output repeats the full k-argument atom k times. That invalidates the old linear written-size claim even under the intended source symbol-count convention.

The normalization section has now been replaced directly. The concrete language and NF1–NF7 transformations are retained. The source's exact smallest basic set and its symbol-count convention have been restored, and all generic, hatted and fresh metavariable ranges are explicit. Source basis: LTCS-05-01, Section 3.1, printed pages 5–6, Definition 1, Lemma 2 and Figure 1 (held layout extraction lines 259–308, read again in this round).

A third handbook correction is now announced in the opening paragraph: each distinct concrete atom X in the whole raw-query-expanded input receives a fresh distinct concept name A_X, together with the protected already-normal definitions A_X <= X and X <= A_X. The complete expansion/reduct proof treats partial-feature truth exactly and proceeds by structural induction. The sum of distinct atom lengths is bounded by the original occurrence length; every atom is fully written twice in the protected definitions.

The saved count uses g initial mutable GCIs, e left-tree concept-child edges, h excess role-chain length, and a/v right-tree conjunction/existential occurrences. NF2/3 are charged to original left-tree edges, NF4 to at most g+e created GCI roots, and NF1 to h. NF6 and NF7 are charged to original right-tree constructors. NF5 decreases the number of GCIs with both sides nonbasic, and only NF7 can increase that number, by at most one. The complete NF schedule therefore has the proved bound 2g+3e+h+v+2a = O(N).

After phase one, mutable antecedents have bounded symbolic length because all concrete atoms were abbreviated. Thus every remaining rewrite adds only bounded written text, including NF7's copied antecedent. The final output is fully written and has O(N) symbols; no shared output or arity bound is assumed. Names are atomic vocabulary symbols in this source-local measure, while actual identifier/predicate-parameter encoding lengths are separately counted for the effective polynomial-time conclusion.

Checkpoint manuscript SHA-256:

    890E098FFD0FBF6580FE1C6EAFEF5FD6E5C50E778E562E19B739DE0CDBA41DB5

Checkpoint ranges: normalization definitions/prepass/rules/count/query interface, lines 86–354; updated complexity interface begins at 781. The original marked completion proof remains intact. Final read-back and edge-case accounting follow; this checkpoint is not an independent acceptance.

## Second-round frozen author report

Current manuscript SHA-256:

    415A3769ADAF9091582626A497EB82263E9ECDDE037C4C447DD9C7EBD7369638

The manuscript now has 2,041 lines. This second round changes only the opening attribution, normalization/input-size/query interface, and final complexity paragraph. The full text from “Marking the queried element” through immediately before “Complexity and the other reasoning tasks” is unchanged from the first reviewed freeze. Everything beginning “Concrete examples and the convexity boundary” is also unchanged. These comparisons were made on actual source text, not inferred from matching headings.

| Current range | Review repair and evidence |
| --- | --- |
| 8–25 | Lists all three handbook corrections, including the concrete-atom abbreviation prepass. |
| 86–110, sec:p09-elpp-normalization | Exact smallest basic set; no bottom/conjunction/existential extras; source-local symbol count; full concrete-atom argument length; separate encoded-length convention. |
| 112–125 | Original four normalized GCI forms and two RI forms, with their exact basic ranges. |
| 127–181 | One fresh distinct name per distinct atom, two protected normal defining GCIs, structural expansion/reduct proof, and full written prepass size bound. |
| 183–237 | Generic B/C/D/E, hatted nonbasic and fresh-name ranges; every original NF1–NF7 form; source two-phase order; semantic proof for every transformation. |
| 239–315 | Explicit occurrence counts, proved rewrite bound (N1), bounded mutable antecedents, linear fully written output and exhaustiveness of the final normal forms. |
| 317–336 | The unbounded-arity counterexample family is normalized through one abbreviation pair; effective encodings and polynomial construction time are distinguished from symbolic linearity. |
| 338–354 | Both fresh-concept query directions and the requirement to prepass the whole raw-query-expanded input. |
| 356–780 | The previously reviewed marked completion and countermodel argument, unchanged as a source substring. |
| 781–818 | Final polynomial-time and four-task interface, explicitly based on encoded raw input and the proved linear symbolic normalization. |
| 819 onward | Later concrete-domain examples and other N-c-010 material unchanged. |

The new normalization passage was read sequentially as current LaTeX, first at 1–181 and 180–371. The final prepass clarification was read at 127–183, the encoded/query interface at 323–358, the link into the unchanged marked procedure at 356–403, and the final complexity paragraph at 781–800. The unchanged proof segment has the independent first-round reviews described above; those verdicts are not automatically reissued for the changed complete file.

### Review findings addressed

- **C1-TOP-01:** The output for X_k <= A_1 intersect ... intersect A_k now contains k short-name GCIs plus two full X_k definitions, giving O(k) written symbol length without bounding k. The proof covers the whole grammar, not just that family. Concrete definitions are protected and counted in full.
- **C1-TOP-02 and C1-PUB-01:** B is explicitly a general concept-description metavariable. The source-local CBox bars mean symbol count rather than set cardinality. The unsupported exact “at most |C|” assertion has been replaced by the proved count 2g+3e+h+v+2a, which is linear in that symbol count.
- **C1-PUB-02:** The basic set is exactly the listed finite set. A conjunction such as B intersect C cannot be admitted as an extra basic filler. It is normalized using a fresh filler name and the corresponding split GCIs.

### Additional mathematical edge checks

For top <= P intersect Q and for {a} <= P intersect Q, the explicitly general B range permits NF7. For A <= exists r.(B intersect C), NF6 names the filler and NF7 splits its definition; no compound enters the basic set. Bottom extracted from a left conjunction or existential is removed by NF4 on its newly created GCI, while the remaining shallow left side stays covered by the model-expansion argument. Repeated identical atoms receive one shared name but two fully written definitions; differently ordered feature tuples remain distinct atoms. Atoms present only in the query are included because the prepass follows the fresh-concept query expansion.

For the phase-two count, NF5 removes one GCI with both sides nonbasic, NF6 preserves or lowers that count, and NF7 raises it by at most one. New NF6/NF5 antecedents are fresh basic names; NF7 copies only phase-one shallow antecedents. No new deep antecedent invalidates the phase-one invariant. Empty mutable input gives g=e=h=a=v=0 and no NF steps. All protected definitions remain normal even with unbounded arity or undefined features.

The linear theorem concerns the explicitly declared source count of written symbol occurrences. It is not a claim that the direct pairwise atom-comparison implementation runs in linear time, or that arbitrary string identifiers and predicate parameters have unit bit cost. A direct encoding of the fully written input gives the separately stated polynomial construction and decision bound.

No unresolved normalization step was identified in this author's final read-back. The continuation point is a fresh independent review against the second-round frozen hash, covering the new prepass, NF count/size proof, exact vocabulary and query/complexity interfaces. No first-round review file was edited, and this note is not an acceptance record.
