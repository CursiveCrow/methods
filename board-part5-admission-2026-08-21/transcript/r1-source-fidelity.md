# Part V admission board — blind round 1 source-fidelity findings

- seat: source-fidelity/evidence
- round: r1 blind opening
- scope: the complete current reader graph rooted at `handbook/parts/p05.tex` and `handbook/annex/p05-route.tex`; all 19 exact wrappers/artifacts; every routed body/annex addition; Part V bibliography, symbol, new-content, depth, and apparatus records needed for source claims
- independence: I did not read another Part V seat transcript or speculate about another seat's conclusions
- boundary: read-only review; no manuscript, source, provenance, control, registry, generated, or test edit; no build or test

### F1 [blocker] [open] The live body and annex print OPEN/unadmitted workflow debt

- author: source-fidelity r1
- location: body route `handbook/parts/p05.tex:15`; rendered body notice `handbook/parts/p05/models-and-interpretability-supplement.tex:19-22`; annex route `handbook/annex/p05-route.tex:14`; rendered annex notice `handbook/annex/p05/depth-completion-supplement.tex:15-17`
- claim: The two routed editorial units visibly call themselves `OPEN and unadmitted` and enumerate source, content, AI, build, visual, register, and acceptance gates. This violates the charter's explicit no-reader-debt invariant. The `OPEN` text in comments at `handbook/parts/p05.tex:1,13,31-32` and `handbook/annex/p05-route.tex:4-10` is non-rendered and is not the reader-facing part of this finding.
- evidence: The body supplement is reached between exact intervals `SRC-09328-09438` and `SRC-09439-09497`; the annex supplement is the sole child of the live Part V annex route. These are not dormant control notes.
- exact correction: First resolve F3-F10. Then replace the rendered notices by ordinary source attribution: separately authored/consumer-corrected standing, exact nonreplacement boundary, and honest body/annex proof status only. Remove all internal gate and admission language from rendered prose while retaining unresolved administrative/build/visual/user gates in control records.
- status: open.

### F2 [blocker] [open-external] Exact destinations and Part V obligation admissions remain administratively open

- author: source-fidelity r1
- location: all 19 records `spec/provenance/SRC-09080-09098.json` through `spec/provenance/SRC-10028-10059.json`; `spec/provenance/reviewed-handbook-unit-records.json:5`; `spec/provenance/reviewed-register-obligation-records.json:6`; relevant open rows in `spec/register-obligation-closure.csv`
- claim: Exact source bytes are clean, but no admission control binds the final Part V graph or this board's conclusions. All 19 `handbook_destination` fields remain `open/missing`; all 19 independent-source fields remain pending; all 209 completeness fields (11 per exact record) remain pending; and both reviewed-record arrays are empty.
- evidence: Direct current parsing produced `open_destinations=19`, `independent_source_pending=19`, and `completeness_pending_fields=209`. The exact comparison in the coverage note establishes only source identity, not these later gates.
- exact correction: After source/content repairs freeze, regenerate the construction snapshot and live unit inventory; add hash-bound reviewed-unit and reviewed-obligation records for the final body, annex, bibliography, registry, tables, and figures; update each exact provenance record individually. Preserve build, visual, human-compatibility, and final-user gates as separate later boundaries.
- status: open administrative boundary; it must not be treated as closed by a source/content vote.

### F3 [must-fix] [open] The historical-derivative header understates its edits and its new interpretability cross-reference points to no supporting content

- author: source-fidelity r1
- location: derivative claim `handbook/parts/p05/models-and-interpretability-supplement.tex:2-18`, especially `:8-10`; current third-slice ending `:220-223`; retained historical evidence `handbook/parts/p05/models-and-interpretability.tex:235-237`; alleged target `handbook/parts/p05/independence-catalog.tex:1-113`
- claim: The supplement says it contains the three exact historical slices with “only” the fixed-proof-predicate consumer changed. The first slice is indeed the historical lines 44-116. The second slice also changes the proof-predicate destination, as declared. But the third slice additionally changes “outside this visit ... the Phase-5 independence chapter” to “outside this chapter ... Chapter~\ref{sec:p05-independence-catalog}.” That extra delta is not declared. Worse, the cited independence chapter contains no interpretability-logic calculus, theorem, or pointer; it covers combinatorial independence, Tennenbaum, and presentation-dependent consistency.
- evidence: The old and new terminal sentences are directly comparable at the cited locations. The live target's complete 113 lines contain no interpretability-logic content. This is both inaccurate lineage metadata and a false reader navigation claim.
- exact correction: Enumerate every permitted derivative delta rather than saying “only.” Either add the promised interpretability-logic pointer/content at the target or remove that chapter reference and cite only the actual source (`Visser1997`). Re-pin the derivative hash/provenance after the exact intended delta set is fixed. The annex derivative's one source-section delta is otherwise correctly described.
- status: open.

### F4 [must-fix] [open] Editorial additions and the symbol registry replace exact Part V notation by unbridged variants and stale scopes

- author: source-fidelity r1
- location: exact arithmetic structure `handbook/restoration/inherited-08306-08438.tex:4-16` and Part V inheritance `handbook/restoration/inherited-09080-09098.tex:15-18`; exact proof/provability definition `handbook/restoration/inherited-09328-09438.tex:65-85`; exact later uses `handbook/restoration/inherited-09539-09619.tex:7-67`, `inherited-09750-09816.tex:7-65`; editorial variants `handbook/parts/p05/models-and-interpretability-supplement.tex:103-140`, `handbook/parts/p05/provability-logic-gl.tex:18-27`, `handbook/parts/p05/independence-catalog.tex:78-99`; registry `handbook/registry/symbols.csv:57-59,172,419-421`
- claim: Exact source fixes `\mathcal N`, `\mathsf{Proof}_T`, `\mathsf{Prov}_T`, and `\mathsf{Con}(T)`. The routed additions silently switch to `\mathcal N_{\mathrm{ar}}`, `\mathrm{Prov}_{\PA}`, `\operatorname{Prov}_T`, `\operatorname{Proof}_T`, and a second `\operatorname{Con}_{\operatorname{Proof}_T}(T)` notation without an identity/variant bridge. The registry then publishes `\mathcal N_{\mathrm{ar}}` and `\mathrm{Prov}_T` rather than the exact-source glyphs, has no row for exact `\mathsf{Proof}_T`, and assigns the PA provability predicate to P8.2 although the current Solovay theorem is in Part V.
- evidence: This is not mere font styling: the exact source expressly says Part V retains the previously fixed syntax and semantics. The new consistency-presentation notation has a legitimate intensional role, but it never states how its standard exact-source instance relates to `\mathsf{Con}(T)`. The reverse-mathematics rows compound the drift: registry lines 419-421 call the substantial Part V chapter an “explicit forward stub,” say the exact theories are fixed in P7.5, omit `\mathsf{WKL}_0` and `\Pi^1_1\text{-}\mathsf{CA}_0`, and thereby contradict `handbook/parts/p05/reverse-mathematics.tex:9-38`.
- exact correction: Preserve inherited artifacts. Make the editorial material use/register exact `\mathcal N`, `\mathsf{Proof}_T`, and `\mathsf{Prov}_T`; if a deliberately presentation-indexed consistency notation is retained, define its exact relationship to `\mathsf{Con}(T)` at the introduction. Correct all scopes/introduction points and add the missing `\mathsf{WKL}_0` and `\Pi^1_1\text{-}\mathsf{CA}_0` rows, then regenerate both public symbol surfaces.
- status: open.

### F5 [blocker] [open] Provable Sigma-one completeness is registered as stated and proved, but remains an annex sketch that names its missing proof

- author: source-fidelity r1
- location: contract `spec/registers/depth-gaps.csv:57` (`D-P6-006`); body `handbook/parts/p05/models-and-interpretability-supplement.tex:101-140`; annex `handbook/annex/p05/depth-completion-supplement.tex:20-38`
- claim: D-P6-006 requires “Provable \(\Sigma_1\)-completeness stated and proved.” The body instead declares `sketched=annex:p5.sigma.1`, and the annex explicitly omits the full bounded-formula evaluation induction, normal-form conversion, exact primitive-recursive proof-code constructor, numeral-substitution invariant, and verification inside PA. Those are the load-bearing steps in the internalized clause, not cosmetic detail.
- evidence: The theorem's two statements and their direction/scope are correct, and the annex is honest about its limitations. Honesty does not satisfy the separate proof-depth contract.
- exact correction: Supply the omitted structural induction and exact proof-code construction/verification in the reciprocal annex, using the exact `\mathsf{Prov}_{\PA}` notation and the already proved Q bounded-case lemmas; change the body status to `proved=annex:p5.sigma.1`. Alternatively, an explicit user-level contract change must downgrade D-P6-006 from “proved” to “sketched”; the current file cannot silently do so.
- status: open.

### F6 [must-fix] [open] The GL entry uses undefined relational semantics and omits its registered apparatus links

- author: source-fidelity r1
- location: contract `spec/registers/new-content.csv:26` (`N-a-025`), `spec/registers/apparatus.csv:13,58` (`A-012`, `A-057`); live entry `handbook/parts/p05/provability-logic-gl.tex:4-74`; existing global sheet `handbook/registry/calculi/hilbert-gl.tex:1-4`
- claim: N-a-025 requires GL axioms, Kripke semantics, finite-frame completeness/FMP, fixed-point theorem, and Solovay completeness at survey depth. The chapter defines the calculus and arithmetical realization, but invokes “Kripke frames,” “accessibility direction,” and “the box clause” at lines 36-45 without defining the valuation/satisfaction clause or pointing to an already available definition. It never links the registered GL rule sheet, and the required GL modal/arithmetic dictionary table A-057 is absent.
- evidence: The theorem statements have plausible primary/standard sources (`Segerberg1971`, `Sambin1976`, `Solovay1976`, `Boolos1993`), and Solovay's primary paper really does study all arithmetical realizations in PA ([DOI 10.1007/BF02757006](https://doi.org/10.1007/BF02757006)). The defect is the missing reader dependency and apparatus, not an objection to the cited theorem. The current sheet itself contains only the Hilbert axioms/rules; Part V never references it.
- exact correction: Define the Kripke model/box clause and chosen accessibility orientation before the frame theorem, or give a real forward/back reference to the canonical modal definition. Link `sheet:hilbert-gl`. Add A-057 pairing K/necessitation/Lob/fixed-point/modal validity with D1-D3/Lob/arithmetical realizations/Solovay, without identifying frame accessibility with formal derivability.
- status: open.

### F7 [blocker] [open] The Paris--Harrington register demands a false/ambiguous ACA claim and the body supplies only the theorem statement

- author: source-fidelity r1
- location: contract `spec/registers/new-content.csv:28` (`N-a-027`); body `handbook/parts/p05/independence-catalog.tex:9-29`; reverse-mathematics base `handbook/parts/p05/reverse-mathematics.tex:9-38`
- claim: N-a-027 requires a survey-level indicator/model-theoretic unprovability argument and “provability in ACA context.” The live entry gives the principle and unprovability statement but no registered proof route and no ACA claim. More importantly, if “ACA context” means the handbook's `\mathsf{ACA}_0`, the requested claim is false: `\mathsf{ACA}_0` has PA as its first-order part and is conservative for arithmetical sentences, so it does not prove the arithmetical Paris--Harrington principle unprovable in PA. A suitable stronger context is, for example, a second-order base plus the relevant infinite Ramsey theorem, not bare `\mathsf{ACA}_0`.
- evidence: The body correctly states the relative-largeness condition `|H|\ge\min H` and cites the original source. An authoritative reverse-mathematics survey explicitly notes that ACA0 does not prove PH and distinguishes the stronger Ramsey context ([Hirschfeldt, *Slicing the Truth*, discussion of PH](https://math.uchicago.edu/~drh/Papers/Papers/rm.pdf)).
- exact correction: Repair N-a-027 before implementing it: name the exact stronger second-order theory/principle intended, or delete the ACA clause. Add the promised survey-level model/indicator or reflection argument with `ParisHarrington1977` and `KanamoriMcAloon1987` attached to their actual roles. Do not assert bare ACA0-provability.
- status: open source-critical contract defect.

### F8 [must-fix] [open] The Goodstein/hydra and Tennenbaum additions fall below their registered treatment and leave a named hydra undefined

- author: source-fidelity r1
- location: contracts `spec/registers/new-content.csv:29,33` (`N-a-028`, `N-a-032`); Goodstein/hydra body `handbook/parts/p05/independence-catalog.tex:31-58`; Tennenbaum theorem `handbook/parts/p05/models-and-interpretability-supplement.tex:86-97`; proof architecture `handbook/parts/p05/independence-catalog.tex:60-74`
- claim: N-a-028 asks for Goodstein termination via epsilon-zero at theorem-level treatment and the Kirby--Paris hydra with its exact rule. The live Goodstein route is three architecture sentences; the hydra paragraph says regrowth occurs “according to the declared rule,” but no rule is declared and the same paragraph admits that the result depends on the exact rule set. Thus the technical name lacks an eliminable definition at its use site. N-a-032 asks for the model package at extended depth with Tennenbaum's proof at theorem-level treatment; the live theorem is citation-only and the later paragraph explicitly says the full coding and overspill proof still must be verified.
- evidence: `Goodstein1944`, `KirbyParis1982`, `Tennenbaum1959`, and `Kaye1991` are attached to the right broad results; the problem is the promised depth and exact variant. An undefined “hydra” cannot carry a rule-dependent theorem.
- exact correction: Define the precise Kirby--Paris hydra position and move/regrowth operation, then show the corresponding ordinal descent and mark the proof boundary honestly. Expand the Goodstein ordinal assignment beyond the three-line assertion to the registered treatment. For Tennenbaum, add a status-bearing method/proof route with the inseparable c.e. sets, nonstandard coding, standard trace, overspill, and computability contradiction; otherwise explicitly downgrade the register contract.
- status: open.

### F9 [must-fix] [open] Registered primary/method sources are absent from the concrete records they are supposed to support

- author: source-fidelity r1
- location: source contracts `spec/registers/new-content.csv:27-35` and bibliography intake `spec/registers/apparatus.csv:183`; live claims `handbook/parts/p05/decidable-arithmetics.tex:42-67`, `handbook/parts/p05/independence-catalog.tex:9-58`, `handbook/parts/p05/reverse-mathematics.tex:4-74`, `handbook/parts/p05/models-and-interpretability-supplement.tex:43-97`; bibliography-wide absence of `FefermanVaught1959` and `GuaspariSolovay1979`
- claim: Several registered source roles were never attached to a reader record. N-a-026's Guaspari--Solovay Rosser-provability pointer is absent entirely, as is its bibliography record. The Skolem-arithmetic paragraph invokes a “Feferman--Vaught-style decomposition” but neither cites nor records Feferman--Vaught 1959. The Paris--Harrington entry does not cite the registered Kanamori--McAloon analysis; reverse mathematics omits Friedman's founding source; the nonstandard-model package omits the registered Skolem 1934 role. Those latter records exist in the bibliography but are not tied to the claims.
- evidence: The missing method source is exactly Solomon Feferman and Robert Vaught, “The First Order Properties of Products of Algebraic Systems,” *Fundamenta Mathematicae* 47 (1959), 57--103 ([publisher record and DOI](https://doi.org/10.4064/fm-47-1-57-103)). The missing Rosser source is David Guaspari and Robert Solovay, “Rosser Sentences,” *Annals of Mathematical Logic* 16(1) (1979), 81--99 ([DOI 10.1016/0003-4843(79)90017-2](https://doi.org/10.1016/0003-4843(79)90017-2)).
- exact correction: Add exact bibliography records for those two works and place their citations only at the method/pointer claims they support. Attach `KanamoriMcAloon1987`, `Friedman1975`, and `Skolem1934` to their registered historical/method roles, while retaining modern sources for contemporary formulations. Do not satisfy A-182 with unattached bibliography entries.
- status: open.

### F10 [blocker] [open] Mandatory Part V tables/figure/audit artifacts are absent or materially incomplete

- author: source-fidelity r1
- location: contracts `spec/registers/apparatus.csv:54-58,114,129` (`A-053`--`A-057`, `A-113`, `A-128`); current exact Q/PA definitions `handbook/restoration/inherited-09099-09111.tex:1-13`, `inherited-09175-09187.tex:2-12`; current independence table `handbook/parts/p05/independence-catalog.tex:101-113`; decidable-arithmetic chapter `handbook/parts/p05/decidable-arithmetics.tex:1-73`; reverse-mathematics table `handbook/parts/p05/reverse-mathematics.tex:40-55`; provability-logic chapter `handbook/parts/p05/provability-logic-gl.tex:1-74`; unrouted audit declaration `handbook/parts/p05.tex:31-32`
- claim: A-053 requires a Q/PA axiom table; the axioms exist as exact definitions but no comparison table exists. A-054 requires Godel/Rosser sentences, consistency sentences, Paris--Harrington, and Goodstein with their exact base theories; the live table omits the Godel and Rosser rows and gives no canonical identity/caption. A-055's Presburger/Skolem comparison table is absent. A-056's Big Five calibration table is substantively present and checked clean. A-057's GL modal/arithmetic dictionary is absent. A-128's Big Five figure is absent. A-113's generated Part V audit is expressly unrouted and declared untrustworthy.
- evidence: This is an absence/coverage finding against exact register rows, not a request for decorative extras. The prose chapters cannot silently substitute for required tables/figures, and a generated audit scanning unreachable historical labels cannot establish the live graph.
- exact correction: Add A-053, complete and label A-054, add A-055 and A-057, and add the A-128 figure with evidence-safe inclusion arrows and representative theorems. Repair the reachability-aware generator before routing A-113. Keep compilation and visual legibility as later gates after the source/content of each apparatus item is correct.
- status: open.

## Checked-clean and not-checked coverage

### Whole-route and exact-source fidelity

- **Checked clean:** `handbook/parts/p05.tex:4-29` routes exactly 19 wrappers once each, in contiguous authority order `SRC-09080-09098` through `SRC-10028-10059`. The model/interpretability supplement intervenes only at the chapter boundary between source line 9438 and source line 9439. `handbook/annex/p05-route.tex:13-14` creates one Part V annex destination and routes only the distinct Sigma-one supplement; the overlapping historical body and annex files are unreachable.
- **Checked clean:** every wrapper contains one matching `inheritedrestorationscope` and one matching inherited artifact. I compared all 980 artifact lines directly with `source/formal-logic-reference.tex:9080-10059`: 19/19 records, 980/980 lines, zero mismatch. No exact inherited unit is duplicated or altered on the reader route.
- **Checked clean statically:** the rooted body/annex graph contains 75 active statement/navigation/annex identities with no duplicate; all 15 distinct parsed references resolve; all 26 distinct inline citation keys exist; and the sole editorial `sketched` target has exactly one reciprocal annex item with no orphan. These checks do not establish the disputed proof depth in F5.

### Lot 1 — Q/PA, representation, coding, first incompleteness foundations

- **Checked clean:** exact Robinson arithmetic and PA axioms; the two fully proved Q bounded-comparison lemmas; standard/nonstandard model definitions and compactness proof; numeralwise relation/function representation with the cited proof boundary; exact Godel numbering, c.e.-axiom/proof-certificate distinction, proof/provability predicate types, and coding exercises. The exact source keeps standard truth, formal derivability, and metatheory separate.
- **Checked clean:** diagonal lemma construction and its cited primitive-recursive dependency; consistency, Sigma-one soundness, omega-consistency; Godel-sentence hypotheses; Rosser's bounded proof comparison; and the theoremhood-undecidability construction. The exact source marks its proof sketches honestly and names the missing cited dependencies.
- **Findings affecting the integrated lot:** F1, F2, F4, F10.

### Lot 2 — models, overspill, Tennenbaum, Sigma-one completeness, interpretation

- **Checked clean:** finite-distance blocks are explicitly external; the countable PA order type separates the standard `omega`, within-block `Z`, and dense block quotient; overspill requires an internal formula and no countability; Tennenbaum is scoped to countable nonstandard PA and simultaneous computability of transported addition/multiplication. The relative-interpretation definition includes domain, equality/quotient, function graphs, quantifier relativization, axiom translation, and an effective transfer boundary; essential undecidability is distinguished from plain undecidability.
- **Checked clean:** the retained body slices do not duplicate the exact standard/nonstandard definitions or compactness proof. The annex compactness proof is correctly excluded because its exact proof is now inline.
- **Findings:** F1-F5, F8-F10.

### Lot 3 — exact lines 9439--10059

- **Checked clean:** all 11 exact intervals and their authority order; diagonalization, Godel/Rosser hypotheses and proof-status ceilings, derivability conditions D1-D3, fixed consistency sentence, complete Lob proof, complete second-incompleteness proof, complete Tarski proof/corollary, final hypothesis audit table, and exercises. No editorial addition alters or duplicates these exact theorem identities.
- **Findings affecting reuse/source notation:** F2 and F4.

### Lot 4 — GL, decidable reducts, independence, reverse mathematics, apparatus

- **Checked clean:** GL's Hilbert axioms/rules, modalized fixed-point hypothesis, and PA-specific Solovay theorem are attached to appropriate classical sources; the Solovay paragraph explicitly remains a proof architecture, not a full proof. Presburger's positive decision statement, congruence expansion, and Fischer--Rabin lower-bound boundary are source-calibrated. Skolem arithmetic uses the positive-domain convention and states the corrected Rackoff space bound `2^{2^{2^{cn}}}` without the former nonelementary/Oppen error. The Big Five definitions, strict ladder, sample equivalence scopes, coded-countable-object warning, and nonexhaustion warning are mathematically coherent at survey level.
- **Findings:** F1, F2, F4, F6-F10.

### Not checked / explicitly external

- No build, tests, generator run, PDF inspection, counter/bookmark/TOC check, index rendering, table/figure legibility check, visual inspection, administrative admission, human review, or final user acceptance was performed. Those gates cannot be inferred from this source-fidelity opening.

## Prioritized repair checklist

1. Correct the source-critical contract in N-a-027: remove/replace bare ACA0-provability before writing Paris--Harrington prose (F7).
2. Complete the Sigma-one annex proof or obtain an explicit contract downgrade (F5).
3. Remove rendered OPEN/unadmitted/gate prose only after substantive repairs freeze (F1).
4. Normalize exact Part V arithmetic/proof notation and repair/regenerate the registry and symbol surfaces, including all five reverse-mathematics systems (F4).
5. Repair the derivative delta declaration and the false interpretability-logic chapter link, then re-pin the derivative (F3).
6. Supply the missing registered depth: exact hydra rules/ordinal descent, expanded Goodstein route, and status-bearing Tennenbaum method (F8).
7. Complete the GL semantic dependency and its rule-sheet/dictionary navigation (F6).
8. Add and attach the Guaspari--Solovay and Feferman--Vaught sources; attach the already present historical sources to their concrete records (F9).
9. Build the missing/partial A-053--A-057, A-128, and reachability-correct A-113 apparatus content, deferring rendering judgments to the visual gate (F10).
10. After all source/content bytes freeze, close the 19 exact destinations and the reviewed unit/obligation records individually; do not merge those controls with build/visual/user acceptance (F2).
