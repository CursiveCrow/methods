# Round 2 — adversarial-publication

### F1 — still-open-reader
- repaired portion: `handbook/parts/p05/models-and-interpretability-supplement.tex:18-26`; `handbook/annex/p05/depth-completion-supplement.tex:12-15`
- response: The routed OPEN/unadmitted/gate notices are gone. Both the body completion and reciprocal annex now use ordinary reader-facing authorship, source, complete-proof, and nonreplacement prose. A noncomment scan finds no remaining `OPEN:`/unadmitted/D-/N-/R-/workflow/finalizer token.
- residual defect: The newly authored apparatus captions print internal register IDs directly to readers: `handbook/parts/p05/models-and-interpretability-supplement.tex:30-32` (`A-053`), `handbook/parts/p05/provability-logic-gl.tex:143-146` (`A-057`), `handbook/parts/p05/decidable-arithmetics.tex:83-85` (`A-055`), `handbook/parts/p05/independence-catalog.tex:278-281` (`A-054`), and `handbook/parts/p05/reverse-mathematics.tex:104-107, :192-198` (`A-056`, `A-128`). These are construction/control identities, not mathematical titles or reader retrieval terms.
- exact correction: Remove the parenthetical `apparatus A-...` strings from all captions while retaining the labels and control-side obligation mappings. Do not alter the mathematical captions or infer any later gate.

### F2 — still-open-external
- response: Per the board charter and round scope, provenance/admission, build, visual, human, administrative, and user gates remain separate. No source repair below is promoted into those controls.

### F3 — accept-fixed
- current evidence: `handbook/parts/p05/provability-logic-gl.tex:4-8`; `handbook/parts/p05/decidable-arithmetics.tex:4-8`; `handbook/parts/p05/independence-catalog.tex:4-8`; `handbook/parts/p05/reverse-mathematics.tex:4-8`
- response: All four editorial chapters now open with visible reader notes identifying separately authored standing, their controlling source domains, their relationship to the exact inherited sequence, and nonreplacement. Claim-local citations and proof statuses remain visible.

### F4 — accept-fixed
- current evidence: `handbook/parts/p05/models-and-interpretability-supplement.tex:137-160`; `handbook/annex/p05/depth-completion-supplement.tex:18-157`
- response: The body is now `proved=annex:p5.sigma.1`. The annex supplies the chosen \(\Sigma^0_1\) normal-form conversion, primitive-recursive term evaluation, simultaneous positive/negative bounded-formula induction in \(\mathsf Q\), bounded quantifier cases, proof-code constructors, substitution invariant, internal PA verification, formalized implication, and external witness-to-Q-proof clause. The round-one omissions are explicitly filled, and the one body/annex pair is reciprocal.

### F5 — accept-fixed
- current evidence: `handbook/parts/p05/independence-catalog.tex:17-92`
- response: The Paris--Harrington definition and cited independence statement now lead to a labeled indicator-method entry explaining the nonstandard-cut/unprovability route. The chapter separately defines full-induction \(\mathsf{ACA}\) versus \(\mathsf{ACA}_0\), states the full-ACA upper calibration, and explains why bare \(\mathsf{ACA}_0\) cannot prove the arithmetical principle. N-a-027's three requested components are now present at their stated survey/citation ceilings.

### F6 — accept-fixed for coverage
- current evidence: `handbook/parts/p05/independence-catalog.tex:94-198`
- response: The chapter now fixes the Goodstein base schedule, local Cantor-normal-form/\(\varepsilon_0\) dependency, termination and PA-unprovability statements, the exact Kirby--Paris tree/regrowth rule, hydra termination/unprovability theorem, and the ordinal ranking. The former undefined “declared rule” and missing ordinal dependency are repaired. The presentation/status of the two new proof-like paragraphs is a distinct repair-exposed record, F15.

### F7 — accept-fixed
- current evidence: `handbook/parts/p05/provability-logic-gl.tex:114-139`; `handbook/registry/symbols.csv:60`; `handbook/generated/symbol-index.tex:354`
- response: The route now defines the Rosser proof-order predicate and strict/non-strict witness comparisons, distinguishes them from ordinary provability and Kripke accessibility, connects the comparison to the inherited Rosser theorem, and gives an explicit Guaspari--Solovay \(R\) bibliographic pointer while declining to manufacture a local calculus. The Rosser predicate is registered and generated.

### F8 — accept-fixed
- current evidence: `handbook/parts/p05/provability-logic-gl.tex:10-112, :141-184`; `handbook/registry/calculi/hilbert-gl.tex:1-4`
- response: The GL definition now states theorem-only necessitation and links `sheet:hilbert-gl`. A local Kripke definition fixes the box clause, accessibility direction, and converse well-foundedness. The PA-specific arithmetical realization and Solovay hypotheses are exact, the proof architecture is a labeled `proofboundary`, and the A-057 dictionary pairs K, D1--D3, L"ob, fixed points, and Solovay completeness without identifying relational and arithmetical semantics.

### F9 — accept-fixed for apparatus content
- current evidence: `handbook/parts/p05/models-and-interpretability-supplement.tex:28-58`; `handbook/parts/p05/decidable-arithmetics.tex:81-115`; `handbook/parts/p05/provability-logic-gl.tex:141-184`
- response: Captioned/labeled tables now provide the complete Q/PA axiom/schema comparison, Presburger/Skolem/full-arithmetic decision and complexity comparison, and provability-logic dictionary. The contents match A-053/A-055/A-057. Their reader-visible control IDs remain solely under F1.

### F10 — accept-fixed for apparatus content
- current evidence: `handbook/parts/p05/independence-catalog.tex:276-326`; `handbook/parts/p05/reverse-mathematics.tex:102-199`
- response: The independence table now has a caption/label and exact G"odel, Rosser, consistency, Paris--Harrington, Goodstein, and hydra rows. The reverse-mathematics table has a caption/label, exact defining principles, a source column, and representative equivalences for the four nonbase systems while honestly treating RCA\(_0\) as the base. The new A-128 figure supplies the five-system strict ladder with representative theorems and explicit non-cover/non-exhaustiveness qualifications. Caption control IDs remain under F1.

### F11 — still-open-generated
- repaired portion: `handbook/parts/p05/reverse-mathematics.tex:220-240`
- response: Part V now ends with a grouped historical/primary and modern Further Reading route covering incompleteness, models, decidable reducts, independence, provability logic, and reverse mathematics. A-186 is fixed at reader-source level.
- residual defect: `handbook/parts/p05.tex:42-43` still leaves `generated/audit-p05` unrouted because the generator reads retained historical labels rather than the final live graph. The exact inherited final audit table is useful but does not satisfy A-113's fresh generated per-part audit identity.
- exact correction: Implement and review a reachability-backed Part V audit generator, regenerate from the final live route, and route the resulting table once. Keep source/content acceptance distinct from the build that will test it.

### F12 — accept-fixed
- current evidence: `handbook/registry/symbols.csv:58, :60-62, :175`; `handbook/generated/symbols-tables.tex:154, :360, :362-364`; `handbook/generated/symbol-index.tex:253, :282, :284, :350, :354`; `handbook/parts/p05/provability-logic-gl.tex:45-59`; `handbook/parts/p05/independence-catalog.tex:247-266`
- response: The live registry and both generated surfaces now use exact inherited \(\mathsf{Prov}_T\), separately register Rosser provability and the presentation-indexed consistency sentence, and explain that the subscripted \(\mathcal N_{\mathrm{ar}}\) is an earlier editorial alias while exact Part V uses \(\mathcal N\). The GL realization uses the exact PA instantiation, and the consistency definition explicitly relates its exposed presentation parameter to inherited \(\mathsf{Con}(T)\). No roman/operatorname predicate alias remains.

### F13 — accept-fixed
- current evidence: `handbook/parts/p05.tex:11-19, :27-30`; `tools/build_named_theorem_index.py:27-28`; `handbook/generated/named-theorem-index.tex:12, :355`
- response: Provenance-safe hooks now anchor the exact Arithmetization of syntax theorem and Undecidability of theoremhood corollary at their environment boundaries. The generated theorem index contains one row for each with reader-facing source proof/status and no source-byte edit.

### F14 — accept-fixed
- current evidence: `handbook/parts/p05/provability-logic-gl.tex:103-112`; `handbook/parts/p05/independence-catalog.tex:208-243`
- response: Solovay's proof ceiling is now a labeled `proofboundary`, and the Tennenbaum architecture is a labeled `hbmethod` containing the inseparability data, overspill/product construction, division test, and separator contradiction. Both are referenceable and state their controlling sources/standing.

### F15 [must-fix] [new] Two cited independence theorems are followed by unclassified proof presentations
- location: `handbook/parts/p05/independence-catalog.tex:135-155, :181-198`
- claim: `thm:p05-goodstein-termination` is declared `cited=Goodstein1944`, but the immediately following block is headed `Proof.`, gives the ordinal-decrease argument, and closes with a QED square without a labeled environment or status. The cited hydra theorem is likewise followed by an unlabelled ordinal-assignment and unprovability derivation. These additions may be valuable proof architecture, but the first visually claims a complete local proof while the theorem status says citation-only, and neither block has a durable identity or explicit omissions.
- harm and failure path: Readers and audit generators cannot tell whether the handbook claims local proofs, proof sketches, or explanatory surveys; the square materially inflates the Goodstein block. Neither passage can be referenced from the new table/figure or reviewed independently.
- exact correction: If complete proofs are intended, move them into reciprocal annex items and change body statuses to `proved` only after verification. Otherwise convert each block to a labeled `proofboundary` or `hbmethod`, remove the QED presentation, and state exactly which key descent/unprovability lemmas remain with the citations.

## Round-2 disposition and publication boundary

- accept-fixed: F3, F4, F5, F6 (coverage), F7, F8, F9 (content), F10 (content), F12, F13, and F14.
- still-open-reader: F1, solely for six caption-level internal apparatus IDs.
- still-open-external: F2.
- still-open-generated: F11, solely for the unrouted stale audit generator; Further Reading is fixed.
- new still-open: F15.
- route/static evidence: the two roots still reach 46 files through 44 noncomment inputs with no missing or duplicate target. The current route has 100 explicit/typed labels with no duplicate. All 43 references resolve when the specialized `sheet:hilbert-gl` calculus label is included; all 78 citation keys exist. The sole `proved=annex:p5.sigma.1` result has exactly one reciprocal annex item. The generated named-theorem index has current rows for both source hooks and no raw sort delimiter.
- no additional register omission: N-a-025--034, D-P6-001--008, A-012/A-053--057/A-128/A-159/A-163/A-186 are now substantively present at source except for the F1 caption text; A-113 remains F11.
- non-build/non-visual boundary: I inspected live source, registry, and generated text only. I did not run a generator, restoration checker, test, TeX/reference/index build, or PDF build; inspect layout, floats, links, bookmarks, glyphs, or sorting; edit manuscript/control/test/generated files; read another Part V seat transcript; perform human review; or close administrative/user gates.
