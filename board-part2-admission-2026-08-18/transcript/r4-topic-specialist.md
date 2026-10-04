# Round 4 topic-specialist hard-cap verification

### F16 — accept-fixed
- reply: accept-fixed
- current location: `handbook/registry/calculi/hilbert-fol.tex:10-19`; `handbook/parts/p02/first-order-calculi-supplement.tex:47-98,173-188`; `handbook/annex/p02/first-order-calculi-supplement.tex:22-54`.
- calculus identity: The sheet identity at line 10 now defines Hilbert derivability by finite dependency-annotated sequences and lists MP, Gen, and the displayed existential-elimination rule as the possible inference steps. The displayed rule at line 18 is Kleene's premise-sensitive form: from `theta -> psi` infer `exists x theta -> psi`, with `x` absent from `psi` and from every premise on which the premise line depends.
- dependency definition: The body's exact clause at lines 64-68 now takes an earlier pair `(theta -> psi,D_j)` to `(exists x theta -> psi,D_j)`, preserves the dependency set, and requires both `x notin FV(psi)` and `x notin FV(delta)` for every `delta in D_j`. This is the same rule and the same side condition as the sheet. Premise, axiom, MP, Gen, and existential elimination now exhaust the declared derivation surface.
- deduction theorem, assumption absent: Annex lines 40-43 handle `varphi notin D`. The premise line's traced subderivation already uses only premises in `Gamma`; existential elimination remains licensed with the same `D`, and A1 prefixes the discharged formula. This yields `Gamma |- varphi -> (exists x theta -> psi)` without importing an unused assumption.
- deduction theorem, assumption present: Annex lines 43-49 use the rule condition to obtain `x notin FV(varphi)` as well as `x notin FV(psi)` and the surviving dependencies. The induction result is `varphi -> (theta -> psi)`. Propositional permutation gives `theta -> (varphi -> psi)`; existential elimination is licensed because `x` is free in neither the consequent `varphi -> psi` nor the surviving dependency set; inverse permutation gives `varphi -> (exists x theta -> psi)`. The side conditions and implication association are correct.
- source/completeness standing: The body and table continue to attribute Mendelson's universal base and Kleene's existential-introduction schema 11/existential-elimination rule 12 by component. The comparison row now describes the same rule surface as the sheet and body, and the deduction theorem has an induction case for every primitive inference. The existential-duality elimination bridge therefore applies to one exact dependency-annotated calculus rather than three mismatched presentations.
- conclusion: No blocking correctness objection remains for F16.

## F1 notice-replacement decision

- answer: yes, at source/content level the F1 notices may now be replaced by ordinary attribution.
- basis: The routed duality body theorem and annex proof close the only missing propositional topic; the inherited NNF and functional-basis proofs remain inline while their retired historical annex fragment is off route; F3, F6, F10, F15, and now F16 are accepted at source/content level. No accepted editorial unit in this board's reviewed scope needs to remain labelled OPEN merely to represent an external administrative gate.
- boundary: This round does not perform the notice edit. The later source pass may replace the stale annex-root debt paragraph and each accepted supplement's OPEN notice with accurate attribution/nonreplacement/proof-status prose. `F2` provenance and admission records remain open. Compilation, fresh reference/index resolution, PDF rendering, visual inspection, human review, and user acceptance also remain open and are not evidence supplied by this verdict.

## Hard-cap disposition

- F16: accept-fixed.
- F1 source/content release condition: satisfied; ordinary-attribution replacement is permitted, but not performed here.
- blocking objections: none.
- new findings: none.

This round read the latest ledger, all Round 3 transcripts, and the current F16 sheet/body/annex bytes. It made no manuscript, control, test, provenance, generated-file, or notice edit and ran no build.
