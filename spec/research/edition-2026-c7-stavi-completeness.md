# C7 / N-c-012: completed arbitrary-order Stavi construction

## Author return

The new body and annex supply nine reciprocal theorem/proof pairs completing the remaining canonical partition-negation construction and the full monadic first-order induction. The exact target is equivalence of monadic first-order logic with one free variable and the defined full past/future language TL(U-strict, S-strict, U-gap, S-gap), uniformly over every nonempty strict linear order and every unary interpretation. No restriction to complete, dense or discrete orders enters this result.

Owned files:

- handbook/parts/p09/presentations/stavi-completeness.tex
- handbook/annex/p09/stavi-completeness.tex
- spec/research/edition-2026-c7-stavi-completeness.md

The author read back the entire actual saved body and annex as one mathematical batch. Source reading, derivation and author corrections were performed; no independent review, scanner, test, build, manuscript render or acceptance run was performed. Integration and consolidated review belong to root.

## Exact unchanged primary and read extent

Alexander Rabinovich, A Proof of Stavi's Theorem, Logical Methods in Computer Science 14(1:20), 2018, pp. 1–18, DOI 10.23638/LMCS-14(1:20)2018. The held revised arXiv version is 1711.03876v2, revised 5 March 2018; publication is dated 6 March 2018.

Original URL: https://arxiv.org/pdf/1711.03876v2

Held original: source/references/rabinovich-stavi-2018/1711.03876v2.pdf

Original SHA256: A8A1D4A6D0F8D76E3F358C87CFE7336A7B9F3DC19900BDBCD708114F4B9F8AC6

Original size: 458841 bytes. Existing bibliography key: Rabinovich2018Stavi. No new bibliography item is required.

Reading derivative: tmp/pdfs/p09-rabinovich-stavi-2018/1711.03876v2.txt. The complete primary was read for the preceding foundation; this block reread the required complete pp. 8–17 passage, including Proposition 3.7 and the canonical expansion; Propositions 4.2–4.3 and Theorem 4.4; Lemma 5.2; Propositions 5.3–5.4; Lemmas 5.5–5.6; Corollary 5.7; Observation 5.8; and every case through the end of Section 5.3. Page 17 was additionally read from the source image tmp/pdfs/p09-rabinovich-stavi-2018/completion-page-17.png to resolve the printed final-label index. Printed and physical page numbers agree.

The earlier nine-pair foundation in stavi-gap-temporal-logic.tex is the explicit interface for proper gaps, gamma formulas, all four first-order truth tables, the two-cell operator, finite/ray prefix recurrence, positive refinement and existential assembly, the one-variable temporal return, the named common-gap formula UG, and the corrected open/closed gap-partition translators OG/CG. This block reread the actual foundation body and needed proof interfaces. No unacquired GHR or GPSS manuscript is used as a proof premise.

## Completed proof pairs and source mapping

1. thm:p09-stavi-completion-primitives / annex:p9.stavi.completion.primitives: simple emptiness, occurrence, universal-label and cardinality conditions; exhaustive actual-infimum or proper-gap classification on arbitrary orders. Supplies the preliminary conditions of Section 5.
2. thm:p09-stavi-point-chain-complement / annex:p9.stavi.point.chain.complement: full Proposition 5.4. The finite recursion retains every label in actual-boundary reductions, both orientations, coincident internal witnesses, ordered proper gaps and all empty conjunctions.
3. thm:p09-stavi-bounded-sampling / annex:p9.stavi.bounded.sampling: full Lemma 5.6 with the strengthened cell invariant D_i AND F_i, backward stability and every sample-truncation case for all four flag configurations.
4. thm:p09-stavi-uniform-handlers / annex:p9.stavi.uniform.handlers: explicit Corollary 5.7 prefix/suffix complements from the plain-chain construction, followed by separately proved uniform first/last identities with their indispensable unflagged hypotheses.
5. thm:p09-stavi-partition-cut / annex:p9.stavi.partition.cut: the exact fixed-point cut equivalence and explicit interior De Morgan expressions, supplying Observation 5.8 with its descriptor retained at the same witness.
6. thm:p09-stavi-equal-gap-branch / annex:p9.stavi.equal.gap.branch: the corrected common-gap detector and every between-cell or within-unflagged-cell cut. Both endpoint formulas refer to the same named missing gap; no label is evaluated there.
7. thm:p09-stavi-open-partition-complement / annex:p9.stavi.open.partition.complement: full Proposition 5.3. First remove forced endpoint cells, then handle uniform intervals, endpoint limits, actual lower/upper boundary points, strictly ordered gaps, and equal gaps. All recursive partition calls strictly decrease word length.
8. thm:p09-stavi-simple-negation / annex:p9.stavi.simple.negation: full Lemma 5.2 and Proposition 4.2, with the explicit four endpoint-remainder choices for closed intervals, empty reduced words, equality/reversed endpoints, ray and whole-order atoms, and complete Boolean assembly.
9. thm:p09-stavi-completeness / annex:p9.stavi.completeness: Proposition 4.3 and Theorem 4.4, including every first-order constructor, free-variable weak types and existential cases through the proved refinement interface, explicit unary basic-form temporal returns, finite label inlining, and the reverse constructor induction.

Worked cases: the rational cut at sqrt(2), with initial label below the cut, middle true label and final label above the cut, distinguishes an unflagged middle cell from a forced singleton. It also proves why the common-gap detector needs the final label. A dense real interval with a forced first singleton exhibits the missing-successor obstruction that must precede any uniform-cell extension.

## Direct corrections incorporated into the new mathematics

- The source's Proposition 5.4 actual-infimum branch on p. 12 drops the final label from a shortened list. The new branch is O_(m-1)(P_2,...,P_m;c,b), and its dual retains P_1,...,P_(m-1). The proof explicitly inserts an attained first point or a coinitial later occurrence.
- The uniform-first reduction on p. 14 needs its first cell unflagged; its dual needs the last cell unflagged. The new algorithm resolves forced endpoints first, using an actual immediate successor/predecessor, emptiness, the endpoint label and a strictly shorter remaining word. This preserves arbitrary original flag sets.
- The printed p. 17 detector uses delta_2 where the final label delta_(n+1) is required. The new T_W uses D_N. Its equivalence is proved under the retained gap descriptors and the two-cell condition, which is exactly its needed domain.
- The equal-gap assembly explicitly ranges over all between-cell cuts and all within-cell cuts whose shared cell is unflagged. It shifts every suffix flag, keeps the common-gap guard Q_W, and uses the corrected foundation OG/CG rather than the insufficient terminal substitution printed in Lemma 5.5.
- Source shorthand for same-length subinterval negation is replaced by the independent L_W/R_W construction from point-chain negation. The partition induction therefore never appeals to itself at the same rank.
- The final guarded complement N_W includes a < b as part of every returned expression. Empty subtuples mean interval emptiness E, with complement Occ_true. Closed intervals have separate a = b, a > b, forced-singleton and endpoint-label cases.

These are corrections in the actual statements, formulas and proofs. The source's historical formulas are recorded here solely to explain provenance.

## Symbols and integration

New local notation: E; Occ_B; All_B; W = (label tuple, singleton flags); Pi_W and shifted Pi_(i:j); Inf_B and Sup_B; A_m for plain point chains and O_m for their complements; L_W/R_W for independently constructed prefix/suffix complements; A_i and its explicit complement for a fixed point cut; M_W for the interior conjunction; N_W for guarded partition complement; I_W/J_W for actual boundaries; G_W/V_W/B_W for two-gap descriptors; T_W/Q_W for the final-label common-gap test; lambda_i/rho_j for exact left/right gap-side partitions; Z_W for their complete cut complement. All are locally defined; the two uses of A have distinct displayed scopes.

Root should route the new body after stavi-gap-temporal-logic.tex and route the matching annex. The preceding foundation's proof boundary def:p09-stavi-completeness-continuation currently says that partition negation and the final induction remain unproved. Replace that reader paragraph directly with a reference to thm:p09-stavi-open-partition-complement, thm:p09-stavi-simple-negation and thm:p09-stavi-completeness. Its historical continuation wording is superseded by this completed authored chain.

The full theorem target has no remaining mathematical construction identified by this author's batch. Shared routing, notation/registry updates and consolidated independent review remain outside this assignment. This statement is an author handoff, not independent acceptance.

## Frozen authored pair

Body SHA256: FD8E0B7792E478FF9710C8525DBDB798A4D668BF3547ADA909301F45A3EB7973

Annex SHA256: 2AF74E44D9EB78EDC21B609B910B4B758F04680C1DADC793A73B98B022320F02
