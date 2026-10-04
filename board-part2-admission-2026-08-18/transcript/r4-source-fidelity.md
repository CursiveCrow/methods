# Round 4 — hard-cap source-fidelity verification

- scope: F16 only, plus the requested F1 source-debt threshold for replacing printed workflow notices
- record basis: latest live sheet/body/annex bytes and all three round-3 transcripts
- verification boundary: source/proof standing only; no edit, build, visual inspection, human review, or user acceptance

### F16 — accept-fixed

- evidence changing my r3 position: The Mendelson/Kleene component attribution remains exact and internally consistent. The sheet source note assigns Mendelson schemas A1-A5 and Gen and assigns Kleene existential-introduction schema 11 and existential-elimination rule 12 at `handbook/registry/calculi/hilbert-fol.tex:1-9`. The displayed surface now has `\exists1` as the zero-premise schema and `\exists E` as the one-premise rule at lines 17-18. This matches Kleene's primary postulate list: schema 11 is `A(t) -> exists x A(x)`, while rule 12 infers `exists x A(x) -> C` from `A(x) -> C` when `x` is not free in `C`; see pp. 82-83 of this [fetchable scan of Kleene, *Introduction to Metamathematics*](https://www.scribd.com/document/919627203/Bubliotheca-Mathematica-Stephen-Cole-Kleene-Introduction-to-Metamathematics-Wolters-Noordhoff-Publishing-1971).
- sheet/body agreement: The sheet identity now says dependency-annotated lines may arise by MP, Gen, or the displayed existential-elimination rule (`hilbert-fol.tex:10`). The governing derivation definition now includes exactly that fifth clause at `handbook/parts/p02/first-order-calculi-supplement.tex:47-76`: from `(\theta\to\psi,D_j)` it forms `(\exists x\,\theta\to\psi,D_j)` precisely when `x` is free in neither `\psi` nor any dependency in `D_j`. The opening reader note, explanatory paragraph, and comparison table consistently assign Mendelson the universal base and Kleene schema 11/rule 12 at lines 2-12, 92-98, and 173-188. The table's rule families and dependency side conditions therefore describe the same calculus as the sheet and body definition.
- deduction-theorem proof standing: The annex induction now contains the missing `\exists E` case at `handbook/annex/p02/first-order-calculi-supplement.tex:40-52`. When the discharged assumption is absent from the premise line's dependencies, it traces the `\Gamma`-subderivation, applies `\exists E`, and uses A1. When the assumption is present, the rule condition supplies the required freshness; propositional permutation changes `\varphi\to(\theta\to\psi)` to `\theta\to(\varphi\to\psi)`, `\exists E` yields `\exists x\theta\to(\varphi\to\psi)`, and inverse permutation gives the induction target. Together with the existing premise/axiom/MP and Gen cases at lines 23-38, this justifies the proof's claim at lines 51-52 that every annotated line is covered.
- conclusion: The exact source roles, displayed calculus, body derivability relation, comparison-table adequacy claim, and locally proved dependency-sensitive deduction theorem now concern one rule surface. My r3 blocking condition is resolved; no blocking objection remains under the source-fidelity mandate.

### F1 source-debt threshold — yes, closed enough to replace the printed OPEN notices

- basis: Round 3 established a unique routed duality body theorem and reciprocal local annex proof, exact inline inherited NNF and functional-basis proofs, and exclusion of both retired propositional syntax/semantics migration files. F3 and F15 are source-fixed, and the final remaining focused source/proof defect F16 is now fixed above. The accepted editorial additions have visible source/nonreplacement or local-proof standing at their live surfaces.
- source-level disposition: The substantive source/content debt represented by F1 is now closed sufficiently for the manuscript owner to replace `handbook/annex/p02.tex:4-12,27-34` and the six routed body/annex OPEN notices with ordinary present-tense attribution and proof-status prose. The replacement should say that the retired propositional fragment is excluded, the exact inherited NNF and functional-basis proofs remain inline, and the separately attributed duality theorem/proof is the live addition; each first-order notice should retain its inherited-versus-editorial boundary without saying that external gates have passed.
- current-byte qualification: The existing reader bytes still print `OPEN`, `owes`, or `unadmitted`, so F1 is not mechanically absent from the current manuscript until that authorized notice replacement is actually applied. This round supplies the requested source-fidelity basis for the replacement; it does not perform it.

### External boundaries preserved

- F2 remains independently open. The source/content conclusion above does not create reviewed-unit or reviewed-obligation records, regenerate the construction snapshot, or close any register obligation.
- Full build, fresh cross-reference/index/bibliography resolution, PDF rendering, visual inspection, human review, and user acceptance remain external and pending. Replacing reader-facing workflow notices with ordinary attribution must not state or imply otherwise.

## Hard-cap answer

- F16: `accept-fixed`.
- F1 substantive/source debt: closed enough to replace the printed OPEN notices with ordinary attribution, subject to the explicit F2 and late-gate boundaries above.
- blocking objection: none.
- new findings: none.
- edits/build: none.
