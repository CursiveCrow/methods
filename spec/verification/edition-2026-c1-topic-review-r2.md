# Edition 2026 C1 independent topic review, round 2

## Scope, identity, instructions, and verdict

Reviewer: the independent topic-specialist agent /root/edition_c1_topic_review. The actual execution model identifier, reasoning setting, and service configuration are unavailable to this reviewer.

Frozen artifact: handbook/parts/p09/presentations/n-c-010.tex.

Verified whole-file SHA-256:

415a3769adaf9091582626a497eb82263e9ecdde037c4c447dd9c7ebd7369638

The assigned repair ranges were lines 8–354 and 781–818, with supporting interface and proof passages as needed. I read all of current lines 8–818, including the entire intervening marking, completion, soundness, and countermodel argument. No assigned range remains unread. Lines 1–7 and 819 onward were not reread in this round and receive no new verdict. In particular, the subsequent concrete-domain example and intractability-source bodies are outside this round's acceptance.

My instructions were to test the concrete-atom prepass, conservative expansion and reduct, protection of the defining GCIs, normalization notation and exact rewrite count, fully written symbolic size with unbounded predicate arity, encoded complexity, raw-query ordering, and compatibility with the current saturation proof. I was to resolve my own prior findings independently and write only this new report. I sent a checkpoint after reading the complete supporting passage. No subagent, other reviewer's report, or author verdict was consulted. No manuscript edit, software test, build, render, or formal proof checker was used.

The first-round report is preserved. Its SHA-256 is:

9ad3af771698e4b57c293473493992a9b23b8ac0898ba073831f075a6184414e

**Scoped verdict: PASS.** Both C1-TOP-01 and C1-TOP-02 are closed by independently checked mathematics in this frozen revision. The amended normalization has the stated linear bound in its explicitly defined symbolic measure and a polynomial bound in actual encoded input length. The current marking and saturation proof remains applicable to its output. I found no new required mathematical correction within lines 8–818.

This is a textual mathematical verdict for the reviewed C1 passage. It is not formal admission, acceptance of the rest of N-c-010, or evidence of build, rendering, rights, or publication acceptance.

## Material actually consulted

- Current manuscript lines 8–200, 201–354, 355–570, 571–780, and 781–818, all read directly with line numbers.
- The independently established first-round finding and source-size convention retained in this reviewer's conversation context. The first-round report's file hash was checked for preservation.
- No additional primary-source PDF passage was opened in this round. The closure arguments below are direct proofs against the current manuscript and the earlier growth family. The source's own assertion of linearity supplies no premise of the repaired size proof.

## Closure of the previous findings

### C1-TOP-01 — CLOSED

Previous issue: unrestricted NF7 could copy a concrete atom of length proportional to \(k\) into \(k\) GCIs, producing quadratic written output from a linear-size input.

Current repair: lines 127–181, 214–237, 239–336, and 781–790.

Use the same fixed p-admissible concrete domain as in the first review: carrier \(\{0\}\), with a universal predicate \(t_k\) at every positive arity. Put

\[
X_k=t_k(f_1,\ldots,f_k),\qquad
\mathcal C_k=\{X_k\sqsubseteq A_1\sqcap\cdots\sqcap A_k\}.
\]

The current prepass produces one fresh name \(A_{X_k}\), the two full defining GCIs

\[
A_{X_k}\sqsubseteq X_k,\qquad X_k\sqsubseteq A_{X_k},
\]

and the mutable GCI with antecedent \(A_{X_k}\). NF7 then produces \(k\) GCIs \(A_{X_k}\sqsubseteq A_i\). The full \(k\)-argument atom occurs twice, while all \(k\) copied antecedents have constant symbolic length. The fully written output therefore has \(\Theta(k)\) symbolic length. This closes the actual growth counterexample without imposing an arity bound.

The repair also addresses the general case: it bounds the sum of the written lengths of distinct atoms, protects their two definitions from rewriting, and proves that every left side which NF7 can copy has bounded symbolic length. These facts are checked in detail below.

### C1-TOP-02 — CLOSED

Previous issue: the range of \(B\) in NF6–NF7 and the intended meaning of \(|\mathcal C|\) were not declared.

Current repair: lines 88–110 and 188–195.

The basic vocabulary is now exactly the specified smallest set; bottom, conjunctions, and existential restrictions are explicitly excluded. The schema variables \(B,C,D,E\) range over arbitrary concept descriptions. Hatted descriptions are nonbasic in the current CBox, with bottom explicitly included in that condition. New concept and role names are fresh relative to the prepass and earlier steps.

The notation \(|\mathcal C|\) now counts symbols in the fully written CBox, with feature arguments and punctuation counted. Names are atomic symbols in this particular measure, and later vocabulary cardinalities are distinguished explicitly. Thus a one-axiom CBox with two right-hand conjunctions is not assigned input size one, and \(\top\sqsubseteq P\sqcap Q\) is an eligible NF7 instance. Both earlier definition omissions are resolved.

## Independent proof checks

### 1. The prepass preserves models and partial-feature meaning

Lines 151–167 give both required directions.

For any model of the original input, define each fresh \(A_X\) to have exactly the extension of \(X\), using the original interpretation of its features. If a feature required by \(X\) is undefined, \(X\) and \(A_X\) are both false there. Structural induction through conjunction and existential restriction proves equality of every original description's extension with its replaced description. Roles are unchanged, so original RIs continue to hold.

Conversely, the two defining GCIs force \(A_X=X\) extensionally in every model of the expanded input. The same induction shows that its reduct satisfies every original GCI. The prepass therefore preserves every original model by expansion and admits only reducts satisfying the original input.

The definitions are protected at lines 144–147 and 214–216. Only the replaced mutable part undergoes the source transformations. Both full copies of each atom remain in the final CBox. Because both \(A_X\) and \(X\) occur in those definitions, both belong to the exact final basic vocabulary. This is the interface needed by the later completion rules.

### 2. The prepass's written-size bound is valid

Concrete atoms have feature arguments rather than concept-valued children. Their occurrences are therefore disjoint subexpressions in the concept syntax trees. Choosing one occurrence of each distinct atom proves

\[
\sum_{\text{distinct occurring }X}\ell(X)\leq N.
\]

For each distinct atom, the defining pair costs \(2\ell(X)+O(1)\). There are at most \(O(N)\) distinct atoms, so the total defining text is \(O(N)\). Replacing every original occurrence by a short fresh name also leaves \(O(N)\) mutable text.

The fresh name's displayed subscript is expressly an explanatory association, not a literal copy of the atom in the encoded identifier. Consequently the proof does not hide repeated large atoms inside the fresh-name notation.

### 3. The normalization replacements remain conservative

The arguments at lines 219–237 are valid for the declared arbitrary-description metavariables.

- NF1 interprets the fresh role as the old chain prefix; the two replacement inclusions imply the original chain inclusion in the reduct.
- NF2 and NF3 assign the new concept name to the extracted description. Conversely, inclusion of that extracted description in the new name, together with monotonicity of conjunction or existential restriction, implies the old GCI.
- NF5 uses the old left description as the new name's extension; transitivity of inclusion proves the reduct direction.
- NF6 uses the old filler as the new name's extension. Inclusion of the new name in the old filler implies the needed inclusion between existential restrictions.
- NF4 deletes an inclusion whose antecedent is empty. NF7 is precisely distribution of a left-side inclusion over an intersection on the right.

Freshness ensures these expansions preserve all other existing axioms, including the protected definitions. Finite composition gives the stated expansion and reduct properties for the full normalization.

### 4. The exact application bound is justified

I reconstructed the charge argument at lines 242–297.

In phase one, an NF2 or NF3 step cuts one edge to a nonbasic child in an original mutable left-side tree. The child subtree moves to a new GCI; it is not copied. The replacement edge points to a fresh basic name and cannot be cut again. Internal edges of an extracted subtree retain their original identities. Thus there are at most \(e\) combined NF2–NF3 steps.

There are at most \(g+e\) left-side GCI roots over this phase, so there are at most \(g+e\) NF4 deletions. Every NF1 step reduces the remaining excess role-chain length by one and emits a normalized length-two chain, giving exactly \(h\) steps. The phase-one bound is therefore

\[
g+2e+h.
\]

After phase one, left sides are basic, a conjunction of two basic descriptions, or an existential restriction with a basic filler. Bottom left sides have been deleted. The mutable part contains no concrete atoms, and its names, nominals, and top have bounded symbolic length.

In phase two, NF7 consumes one original right-side conjunction occurrence without copying either child, so there are at most \(a\) NF7 steps. NF6 processes an original right-side existential occurrence at most once: afterward its filler is basic. Hence there are at most \(v\) NF6 steps.

For NF5, let \(q\) count mutable GCIs having both sides nonbasic. Initially \(q\leq g+e\). NF5 reduces \(q\) by one. NF6 leaves \(q\) unchanged when its left side is nonbasic and otherwise leaves it zero; its additional GCI has a fresh basic left side. NF7 increases \(q\) by at most one. Therefore NF5 can occur at most \(g+e+a\) times, independently of the order of the eligible rules within phase two.

Adding these bounds gives exactly

\[
2g+3e+h+v+2a=O(N).
\]

All five initial counts are bounded linearly in the mutable prepass input length, which is itself \(O(N)\). The argument proves termination and the stated count; it does not merely infer termination from an expected output shape.

### 5. Fully written final size and normal form

The per-step length accounting at lines 299–307 is correct. NF1–NF3 and NF5–NF6 move the existing expression pieces and add a bounded number of symbols. NF4 removes text. NF7 copies only its left side, which has bounded symbolic length after phase one.

Phase two keeps a left side equal to a phase-one left side or a fresh name, allowing copies of those forms. It cannot introduce a new nonbasic child into a left-side syntax tree. Thus no phase-one rule becomes newly applicable.

At termination, a nonbasic left side cannot coexist with a nonbasic right side because NF5 would apply. For basic left sides, right-side conjunctions and existentials with nonbasic fillers would trigger NF7 and NF6. All remaining mutable GCIs therefore have one of the declared normal forms, and the protected definitions already have those forms.

The \(O(N)\) rewrite count, constant symbolic growth per step, and the \(O(N)\) full defining text prove the claimed linear size for the entire written output, including unbounded-arity atoms.

### 6. Effective encoded complexity

Lines 326–336 and 781–790 distinguish the established symbolic bound from the effective computation cost. This distinction is mathematically sound.

There are \(O(N)\) output symbol occurrences, and \(N\) is bounded by the length of a direct encoding of the input. Every original identifier or parameter has length at most that encoded input length. Only \(O(N)\) fresh names are needed, and they can be assigned polynomial-length encodings. Thus the complete encoded output is polynomial in encoded input length even if an original long identifier is repeated.

Direct syntactic comparison for atom identification and repeated scans for rule applicability take polynomial time on these polynomial-size encodings. No linear-time implementation claim is needed for this argument.

Every concrete conjunction assembled from one label contains only occurring basic concrete atoms. Their full descriptions are present in the retained defining GCIs, so each test input has polynomial encoded length. Under the stated p-admissibility assumption for those constraint problems, the finite completion state and its rule tests give polynomial overall decision time. This argument does not require a bound on predicate arity or unit-cost arithmetic on its encoded parameters.

### 7. Raw queries enter before atom replacement

The order at lines 338–354 is correct: adjoin \(A_0\sqsubseteq C\) and \(D\sqsubseteq B_0\) first, then apply the prepass to the entire expanded input, including query-only atoms, and then normalize.

The raw-query equivalence has both directions: original subsumption forces every \(A_0\)-instance into \(B_0\), while an original counterexample survives the extension \(A_0=C,\ B_0=D\). Conservativity of the subsequent steps preserves those two queried names' extensions. The symbol-size bound includes the raw CBox and both query descriptions.

I also checked the query \( \top\sqsubseteq X \) where \(X\) is a universal concrete predicate on a possibly undefined feature. Prepass definitions \(A_X\leftrightarrow X\) do not force \(A_X\) to have an instance or force the feature to be defined. The original countermodel with the feature undefined remains an expanded countermodel. This verifies the partial-feature case at the normalization/query interface.

### 8. The current saturation proof still applies

I reread current lines 355–780 rather than importing the first-round verdict without checking the interface.

The marking equivalence, finite labels and role pairs, support sets, guarded CR8, nominal reachability, and all eleven rule schemas remain mathematically valid. The finite-state count at lines 501–509 still bounds successful applications because every application adds at least one absent entry.

The soundness argument at lines 567–622 covers all eleven rules. In particular, CR6 obtains an existing target instance from its permitted path and identifies it with the source instance using the shared nominal; CR8 uses exactly the defined features in the correct concrete carrier.

The reachable quotient at lines 624–678 retains all nominals, excludes bottom by backward CR5 propagation, proves label agreement through CR6, and establishes outgoing-edge transfer using induction on insertion time with the final equivalence fixed. The concrete witnesses and truth lemma at lines 680–747 retain the supported-atom avoidance argument and the undefined-or-wrong-carrier case.

The new defining GCIs need no special semantic exception. At saturation, CR1 makes \(A_X\in S(C)\) equivalent to \(X\in S(C)\) for each retained label. The truth lemma therefore makes their extensions equal in the constructed interpretation. The general normalized-GCI proof at lines 749–773 consequently verifies the protected definitions along with the other axioms.

Composed role edges remain covered by the representative-transfer argument at lines 766–772. The root countermodel at lines 775–779 is therefore a countermodel for the normalized marked query; the proved reduct steps recover the original raw-query countermodel.

The reasoning-task reductions at lines 801–817 remain correct. ABox assertions become equivalent singleton GCIs, consistency uses nonempty abstract domains, instance checking uses nominal subsumption, and concept satisfiability uses failure of subsumption by bottom. Query-only concrete atoms are now explicitly included in the prepass for these reductions.

## Final disposition

PASS for the repaired normalization, its explicit size and rewrite-count bounds, effective polynomial complexity, raw-query reduction, and connection to the complete current marked-saturation proof in lines 8–818.

C1-TOP-01 and C1-TOP-02 are closed. No new actionable mathematical finding was established. The source-body boundary at line 819 and the separate formal, build, visual, rights, and publication gates remain outside this verdict.
