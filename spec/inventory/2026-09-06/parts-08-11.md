# Current inventory: Parts VIII–XI

Inventory date: 6 September 2026 Pacific time. Scope: the actual active LaTeX routes and the assigned requirements in `spec/registers/new-content.csv` and `spec/registers/depth-gaps.csv`. This census writes only this Markdown file and its companion JSON. No manuscript, source, bibliography, registry, or generated lookup was changed; no tests, builds, manuscript renders, or source acquisitions were performed.

The exhaustive row ledger is [parts-08-11-requirements.json](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/parts-08-11-requirements.json). It contains every assigned register row, with its original item text, current evidence, separate content/proof states, concrete remaining work or verification question, and an explicit completion flag.

| Part | New-content rows | Depth-gap rows | Total |
| --- | ---: | ---: | ---: |
| VIII | 30 | 35 | 65 |
| IX | 28 | 4 | 32 |
| X | 26 | 8 | 34 |
| XI | 9 | 0 | 9 |
| Total | 93 | 47 | 140 |

Seven new-content rows belong to the original domain x. They remain individual entries in the ledger and are listed separately below. Their old exclusion notes, and all old E/T/S/P ceilings, are historical register data rather than present completion authority.

## What the statuses mean

`substantive_present` means a substantive matching presentation was located and read; it does not certify every source variant or every proof. `summary_only` records a short descriptive or cited treatment. `mixed` means that different components or source presentations have different standing. `not_located` is confined to the active routes inspected, not an assertion of absence from every repository file.

`local_proof`, `source_sketch`, `cited_only`, `mixed`, `not_applicable`, and `unverified` describe the actual proof situation. A correctly attributed source sketch is not automatically a defective proof, and a cited theorem need not be reproduced merely because it is cited. An unpresented registered source body or an explicit promise to an absent construction is a separate presentation issue.

Only the narrowly stated three-fact requirement `D-P10-027` is marked `completion_verified: true`: its current statement and complete proof were read, including the constant-free language and finite multiple-conclusion K3–LP duality. The other flags remain false because a definite component is missing or the full requirement/source correspondence has not been verified. False is not shorthand for “nothing written.” No completion percentage is inferred.

This is a requirement census, not a new end-to-end correctness audit of every proof. Matching definitions, statements, source boundaries, and selected actual proof passages were read. The long P9 files, including the 10,097-line N-c-018 presentation, were not reread in full. Existing bounded reviews are identified as such and do not certify whole-topic completion.

## Active route established

The root `handbook/main.tex` inputs `parts/p08` through `parts/p11` at lines 32–35 and their annex drivers at lines 50–53. Part VIII's source-anchor input is at line 31. Recursive reading of the eight part/annex drivers resolves 186 static `input` files, including restoration wrappers, restored text, supplied additions, and generated lookups. Generated lookup claims were not used to establish mathematical completion.

- Part VIII's driver explicitly imports 40 `scope-SRC-...` wrappers leading to 40 `inherited-...` LaTeX slices, interleaved with the current intuitionistic, modal, temporal/epistemic, conditional/deontic/free, many-valued, relevance/linear, and nonmonotonic supplements. Older combined files such as `parts/p08/substructural.tex` are not substituted for that active route.
- Part IX imports its current host, 27 `n-c-...` source-presentation files, the separate `n-x-015` presentation, and the general-TBox ALC insertion. Its annex imports `proofs`, `finite-trees`, and `alc-general-tboxes`.
- Part X imports the current algebraic, duality, modal, categorical, Lawvere, doctrine, contextual, adjoint, and presheaf additions. The actual active annex route contains **80 `annexitem` bodies**. This is a route count, not a mathematical or publication-completion count.
- Part XI imports the 244-line `philosophy-of-logic.tex`. Its annex explicitly contains no annex-only proof.

The registered calculus sheets are evidence where a matching body invokes them; the static input count above does not pretend that `showcalculus` is an ordinary `input` edge.

## Part VIII: Nonclassical logics

### Actual content

The active source slices and supplements supply IPL semantics and translations; twelve modal-system cards; standard translation, elementary correspondence, Sahlqvist and bisimulation statements; filtration; neighborhood systems; two-index actuality/fixedly semantics; quantified-modal domain distinctions; CTL/CTL*/mu cards; strict tense and branching-time policies; multi-agent, common and distributed knowledge; public announcements and hybrid logic; free-logic variants and descriptions; SDL paradoxes and dyadic preference semantics; selection/sphere conditionals; K3/LP/FDE, finite and infinite Lukasiewicz, Post, Bochvar, t-norm and supervaluation treatments; relevance, full CLL, phase semantics and Lambek; and preferential/default/circumscription/autoepistemic and AGM material.

Evidence includes `modal-logics-supplement.tex:318` (the separate four-system canonical theorem), `:365–440` (translation/correspondence/Sahlqvist), `:491–580` (bisimulation and filtration), `:636–691` (neighborhood data), and `:809–977` (actuality and quantified-modal distinctions). The temporal supplement's common-knowledge card at `:546` links the actual fixed-point/induction sheet and explicitly distinguishes weak completeness from arbitrary-premise noncompactness.

The annex route distinguishes the inherited IPL, modal, LTL, multi-agent S5, and IMLL sketches from independently supplied proofs. `annex/p08/source-sketch-map.tex` is a navigation account of those sketches, not an additional proof. The actual four-system modal proof in `annex/p08/modal-completeness-supplement.tex` and the matrix specialization/duality proofs in `annex/p08/many-valued-supplement.tex` were read during this census.

### Definite presentation gaps and bounded remaining work

- `N-b-001` asks for K, T, D, B, K4, S4 and S5. The supplied canonical proof is explicitly for only K, KT, S4 and S5. The other cards and cited theorems are not that same local construction.
- `N-b-005`: Thomason/Fine incompleteness is a cited existence paragraph at `modal-logics-supplement.tex:784–790`, followed by a general-frame definition. The actual counterexample logics and distinct source constructions are not given there.
- `N-b-027` / `D-P10-032`: the exact relevance sheets/frame data are present, but the specifically requested variable-sharing proof and gamma admissibility are cited statements at `relevance-linear-supplement.tex:137–170`.
- `N-b-028` and `N-b-029` contain concrete promises to P10 that are not fulfilled by that target's current text. `many-valued-supplement.tex:375–378` points to an arbitrary-premise MV completeness theorem; `:430–432` points to the corresponding exact algebra classes. P10 currently provides only the short Chang/Mundici/BL/MTL paragraph and the general residuated-lattice definition. These are presentation gaps, distinct from the legitimate finite-premise standard-completeness citations.
- `D-P3-008` asks for an inclusive/empty-domain convention. The selected free-logic definition in `conditionals-deontic-free.tex:8–9` explicitly requires both inner and outer domains nonempty. The later P10 empty-sort doctrine does not silently alter this P8 convention.
- The coherence-space/proof-net passage at `relevance-linear-supplement.tex:693–705` contains source pointers and explicitly no technical correctness, sequentialization, or execution construction. Its historical ceiling is not used to certify the row complete.

### Verification unknowns

Many substantial P8 statements are explicitly cited, including source-sensitive filtration, van Benthem, neighborhood completeness, PAL, hybrid tableaux, IQC, KC/LC, relevance/gamma, CLL and phase adequacy, and KLM/AGM representation. Their precise source proof granularity and full source-presentation coverage were not re-established here. Absence of a local proof is therefore recorded rather than uniformly called an error.

The BHK/realizability and Markov passages explicitly route to P7. Those cross-part theorem bodies are outside this assignment; their status is left for the P7 inventory. The existence statement at `intuitionistic-supplement.tex:407` is specifically about a closed normal pure-NJ derivation and depends on the separately stated normalization boundary.

## Part IX: Logic in computer science

### Actual content

The active host and its separate source files contain finite-model theory, zero-one laws, locality/descriptive complexity, classical decidable fragments, description logics, temporal and automata methods, model checking, the modal mu-calculus, program logics, logic programming/ASP/Datalog/CSP, complexity and interpolation. These are not just host entry cards: many individual source presentations now contain hundreds or thousands of lines of constructions and examples.

The current files for N-c-009 through N-c-018 include substantial mathematical additions. In particular the original ALC concept calculus is separate from the supplied blocking/general-TBox procedures and the type-elimination/EXPTIME proof pair; N-c-015 has the modern finite-tree/WSkS constructions with canonical codes and pruning; N-c-016 distinguishes four technical source presentations from the 1999 book boundary; and N-c-018 has extensive Kozen, Emerson–Jutla, and Bradfield–Stirling developments.

The current N-c-013 text at `:1403–1415` states and proves the corrected positive-length accepting-state return criterion. This census does not revive that corrected issue as an unfinished obligation.

### Distinct source presentations still explicitly unpresented

The following are current manuscript boundaries, not fresh claims about whether a source file could now be available. The root source inventory must separately reconcile present holdings with these passages.

| Row | Source presentation not supplied by the displayed later account | Actual evidence |
| --- | --- | --- |
| N-c-001 | Ebbinghaus–Flum 1995 edition | `n-c-001.tex:60–68` |
| N-c-002 | Glebskii–Kogan–Liogon'kii–Talanov 1969 | final independent-priority paragraph of `n-c-002.tex` |
| N-c-004 | Immerman 1999 Chapter 4 ordered fixed-point treatment | `n-c-004.tex:136–142` |
| N-c-005 | Lewis 1979 book | `n-c-005.tex:86–93` |
| N-c-006 | Mortimer 1975 article | `n-c-006.tex:81–88` |
| N-c-007 | 1998 journal text distinct from the used 1996 AVBN preprint | `n-c-007.tex:8–12` |
| N-c-008 | Exact Löwenheim 1915 and Behmann 1922 presentations | `n-c-008.tex:61–75` |
| N-c-009/010 | Baader et al. 2017 book algorithms/proofs | `n-c-009.tex:820–822`; `n-c-010.tex:1520–1527` |
| N-c-013 | McNaughton 1966; Safra 1988 proceedings; Thomas 1997 chapter | `n-c-013.tex:921–963`, `:1430–1441` |
| N-c-015 | Thatcher–Wright 1968; RC-1713 remains a lead | `n-c-015.tex:489–500` |
| N-c-016 | Clarke–Grumberg–Peled 1999 first edition | `n-c-016.tex:1610–1631` |
| N-c-017 | McMillan's revised 1993 book, distinct from the 1992 thesis | `n-c-017.tex:1627–1639` |
| N-x-015 | Halpern 2003 uncertainty chapter | `n-x-015.tex:13–25` |

The JSON retains separate rows even where one source boundary affects several topics.

### Proof standing and verification unknowns

- Libkin's finite Craig/Beth locations are exercises with hints, explicitly identified at `n-c-001.tex:53–58`. Calling them source sketches does not make them full source proofs; neither does it establish that a cited statement is mathematically wrong.
- Pnueli/GPSS and the W3C complexity discussion explicitly distinguish source sketches, outlines, and classification tables from supplied proofs. Their actual source status must remain visible.
- N-c-024 explicitly keeps combined EXPTIME-hardness and undecidable-containment constructions cited at `:321–327`. N-c-025 distinguishes Bulatov's and Zhuk's independent algorithms and expressly stops short of reproducing their long structural proofs at `:447–473`.
- N-c-018's complete context-counted argument uses `M=2^m(m^2+1)^{m^2}`, at `:1967–2370`, and explicitly distinguishes it from the original `N=2^m` cap. It does not establish the original threshold. Its tree representation at `:1958–1964` explicitly permits nested/crossing ancestor backedges; a stronger imported tree-like convention would need separate verification. The Walukiewicz full-calculus theorem at `:2377–2438` is explicitly cited with the required deductive-normalization interface; that citation is not itself classified as a missing-proof defect.
- The current N-c-018 progress note records bounded independent reviews and still distinguishes these source-threshold/tree-convention questions. Its status is corroborated by the actual passages above, rather than used as a completion substitute.

No whole-topic completion is certified merely because a modern proof supplies the core theorem while an original registered presentation remains unpresented.

## Part X: Algebraic and categorical logic

### Actual content and bounded reviews

The live route now contains substantial supplied proofs for equational logic/free algebras, subdirect representation, Stone duality and countable atomless Boolean algebras, prime-filter separation/Priestley duality, Heyting completeness, Esakia and intermediate-algebra correspondence, the distinct Rasiowa–Sikorski dense-set lemma, BAO/canonical-extension/descriptive duality, unary/polyadic modal completeness, elementary category theory, contextual STLC/internal-language equivalence, Lawvere theories and free models, quantifier/equality doctrines, powersets, contextual first-order soundness, Pitts's adjoint presentations and Eq0, and presheaf foundations/exponentials/classifiers/power objects.

The actual annex driver imports 80 items. In the latest block, the three adjoint proof pairs and five presheaf proof pairs are active, and both extra rule sheets are displayed. The actual presheaf body includes the stage-dependent exponential formula `Nat(yc×X,Y)` and the power-object/subpresheaf identification; those constructions are not falsely reported as absent merely because general internal logic remains unfinished.

The following current bounded reviews were inspected as review evidence:

- `p10-adjoint-calculus-review-2026-09-06.md`: a scoped mathematical/source pass over all four actual adjoint files and the primary Pitts figures.
- `p10-presheaf-foundations-review-2026-09-06.md`: the pointwise/cancellation/subobject review, with its sole universe-closure point resolved by `def:p10-categorical-size`.
- `p10-presheaf-topos-review-2026-09-06.md`: the exponential/classifier/power-object review; its final read-back closes the typed-k and source-entry incorporation points.

These reviews certify their stated bounded scopes. They do not establish complete source coverage for every P10 register row or completion of the whole part.

### Definite short or incomplete presentations

- `N-d-001`: the subdirect representation is developed, but HSP remains the cited theorem at host lines 32–37. The two results are not interchangeable.
- `N-d-005` / `N-d-007`: the CPL ultrafilter countermodel argument is local at host lines 86–106; the free-Boolean assertion and the compactness/type-space dividends are much shorter. The latter are only lines 110–112 here, not a separately constructed theory/type Stone space.
- `N-d-010`: locales are a short pointer at lines 123–125.
- `N-d-012`: topological S4 and the real line are a cited paragraph at lines 131–134.
- `N-d-013`: MV identities and the standard example are present, but Chang completeness/Mundici correspondence are short cited sentences at lines 162–165. The arbitrary-premise completeness promised from P8 is not supplied.
- `N-d-014`: one residuated-lattice definition at lines 171–188 does not supply the required FL-algebra classes, subvariety survey, algebraization, and cut-elimination correspondence.
- `N-d-015`: BL/MTL remain a short description at lines 165–169 rather than exact algebra classes and scoped completeness theorems.
- `N-d-016/017`: cylindric and relation algebras occupy lines 190–200; their axioms, exact translation, representability/undecidability statements and variable-free set-theory treatment are not developed there.
- `N-d-018`: Blok–Pigozzi is the brief verbal criterion at lines 202–206.
- `N-d-023`: the presheaf topos and power-object construction are proved, but the full higher-order internal language, its semantics/soundness, and the general Kripke–Joyal forcing clauses are not supplied by the short host comparison at lines 271–278.
- `N-d-024`: the Tierney/CH connection remains the pointer at lines 279–283; no specific site, internal statement, construction and transfer have been supplied there.

These are current text descriptions. Whether a particular cited source proof must be reconstructed in full is a separate requirement/source decision; the inventory does not impose that rule indiscriminately.

## Part XI: Philosophy of logic

### Actual content

The active chapter has Convention T and an object/metalanguage discussion, a short strong-Kleene fixed-point definition, a brief revision-theory comparison, a TB/CT/KF/FS family table, a five-paradox mechanism table, sorites and vagueness comparisons, model-theoretic consequence and harmony/invariance/pluralism, and plural quantification/ontological-commitment discussion. All 244 current lines were read. The annex is explicitly a navigation boundary without an additional proof.

### Definite gaps

- `N-b-020`: the truth jump is not specified by its exact clauses and information order, nor are the transfinite limit and stabilization arguments supplied. Least/maximal fixed-point and groundedness claims remain short descriptions.
- `N-b-021`: revision sequences and their limit policy, stability/nearly-stability definitions, and distinct Herzberger/Gupta–Belnap presentations are not supplied by lines 55–60.
- `N-b-022`: lines 62–93 explicitly do not fix formal TB/CT/KF/FS variants. The complete axiom/rule packages, coding/induction choices and exact conservativity/strength statements remain outstanding.
- `N-b-023`: the table and surrounding prose give mechanisms rather than a complete formal diagnosis for every named paradox. The Curry display uses bottom; the arbitrary-conclusion derivation characteristic of Curry's paradox is not supplied there.
- `N-b-024`, `N-b-034`, and `N-b-035` have brief philosophical comparisons. Full separate source arguments, formal precisification/consequence distinctions, and plural-language/translation details remain unverified or unpresented.

No current bounded whole-chapter source/mathematical review is claimed by this census. Cited philosophical argument and local formal theorem proof are kept as different kinds of evidence.

## Original domain-x rows, kept separate

| Row | Part | Actual current treatment |
| --- | --- | --- |
| N-x-006 | VIII | Quantum/orthomodular logic: source pointer only at `relevance-linear-supplement.tex:693–705`. |
| N-x-007 | VIII | Adaptive logic: source pointer only in that same active passage. |
| N-x-009 | VIII | Abstract argumentation: source pointer only in that same active passage. |
| N-x-008 | XI | No inductive-logic/confirmation-theory presentation located in the complete active chapter. |
| N-x-010 | X | The Blok–Pigozzi pointer is present; broader AAL/Leibniz-hierarchy material is not developed there. |
| N-x-013 | X | Substantial CCC/doctrine/presheaf work is now present; fibrations, categorical sketches and infinity-topoi are not located as technical presentations. |
| N-x-015 | IX | A separate quantitative source presentation is active, with Halpern 2003's contents-only boundary explicitly retained. |

None is counted complete from its historical exclusion. The JSON preserves `domain: x` so these cannot disappear inside the ordinary additions.

## Handoff boundary

The companion JSON accounts for all 140 assigned IDs exactly once. Its evidence is current LaTeX, with reviews and source notes used only for their stated bounded scope. Current source-file availability, bibliography accuracy, global requirements outside these parts, and publication administration belong to the root inventory. No stale audit table or old treatment ceiling has been used to close an obligation.
