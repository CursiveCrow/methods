# Complete *The Methods of Reason* as a comprehensive reference of reasoning and logic

## 1. Deliverable and governing decisions

Produce one integrated, publication-ready handbook for graduate readers, researchers and practitioners. It should support both **looking up a subject** and **finding a method for a reasoning task**, with precise statements, explicit assumptions, useful comparisons and access to complete treatments.

The CRC model contributes expert evaluation, organized reference tables, consistent terminology and deliberate edition maintenance. Those functions will be implemented for definitions, calculi, theorems, algorithms, reasoning methods and empirical findings. [CRC Handbook publisher description](https://www.routledge.com/CRC-Handbook-of-Chemistry-and-Physics/McEwen/p/book/9781041194620)

The following decisions are fixed by this planning discussion:

- Cover all major forms of reasoning, including deductive, inductive, statistical, Bayesian, abductive, causal, strategic, informal and empirical approaches.
- Use **7 September 2026** as the first edition’s coverage cutoff.
- Preserve all existing substantive content and all **615 original requirement IDs**. Preserve the frozen inherited source as archival evidence while correcting errors directly in the active manuscript.
- Allow the current fourteen-part organization to expand and change.
- Provide consistent reference entries linked to complete attributed treatments. Reference entries supplement the full treatments.
- Obtain required material through **free resources and available free access**. No paid acquisitions.
- Keep materially different systems, source versions and notation conventions distinguishable.
- Impose no page-count or proof-compression target.
- Publish only the final integrated handbook. Internal construction outputs remain working artifacts.

The completed [manuscript inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/MANUSCRIPT-INVENTORY.md) and [current requirement ledger](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/complete-requirement-ledger.json) are the starting evidence. Existing writing is retained wherever it passes review; authors work on missing, incomplete or incorrect components.

**Meaning of completion:** every obligation in the first-edition catalog and every retained existing requirement has an accepted disposition, all required content and sources are present, and the final book passes its content and publication gates. New publications after the cutoff belong to a later edition. An overlooked required topic or error discovered before release must be resolved in this edition.

## 2. Coverage and reference architecture

### A. Establish a finite, traceable coverage catalog

Before broad authoring, the lead editor will convert the inventory into a catalog of actual intellectual units: identified definitions, systems, theorem-and-proof groups, algorithms, reasoning methods, comparative treatments and empirical topics.

Each unit must identify its source presentation, required components, prerequisites, handbook destination and acceptance conditions.

The old catalog’s **9,162,150 records** require a traceable reconciliation. They include source metadata, hierarchy and retrieval records as well as substantive content leads. Preserve the old files and map their records to:

- A substantive obligation in the edition catalog.
- An alias or repeated capture of an already identified obligation.
- Non-content metadata, with its purpose recorded.
- An unresolved candidate requiring investigation.

Different editions or materially different presentations cannot be merged merely because their titles match. No existing substantive obligation may disappear during reconciliation.

Check breadth against identified editions and actual contents of the established mathematical-logic, philosophical-logic, computer-science logic, automated-reasoning and knowledge-representation handbooks. Add explicit reasoning coverage checks against *The Handbook of Rationality* and *The Oxford Handbook of Thinking and Reasoning*. These supply complementary normative and empirical perspectives. [MIT Press](https://mitpress.mit.edu/9780262045070/the-handbook-of-rationality/), [Oxford Academic](https://academic.oup.com/edited-volume/34559)

**Catalog passes when:** every existing requirement and substantive coverage record has a destination or a documented, reviewed disposition; every domain below has identified source presentations and bounded content units; no unresolved scope candidate remains.

**Catalog fails when:** metadata is counted as authored content, repeated records inflate the work count, a domain is represented only by a heading, or a source/version distinction is silently removed.

### B. Expand to nineteen parts

Keep existing stable part identifiers and labels. Change printed order without renumbering those identifiers.

**Printed order:** existing P1–P10; new P15–P19; existing P11–P14.

The five new parts contain these **26 initial chapter assignments**. The catalog will enumerate their specific methods and source presentations.

| Stable part | New part | Required chapters |
|---|---|---|
| **P15** | **Uncertainty and Statistical Inference** | U1 probability, conditioning, independence and expectation; U2 induction and confirmation; U3 Bayesian updating, prediction and model comparison; U4 likelihood, estimation, confidence procedures and testing; U5 statistical generalization and learning; U6 robustness, imprecise probability, sensitivity and evidence synthesis. |
| **P16** | **Explanation, Abduction and Causation** | C1 logical abduction and diagnosis; C2 explanatory comparison, analogy and scientific inference; C3 causal graphs, structural models and intervention; C4 identification and estimation, including separately presented potential-outcome approaches; C5 causal counterfactuals and connections to conditional logics. |
| **P17** | **Decision and Strategic Reasoning** | D1 preferences, utility and representation; D2 risk, uncertainty and ambiguity; D3 information value and sequential decisions; D4 strategic interaction and equilibrium; D5 collective choice and aggregation. |
| **P18** | **Argumentation and Informal Reasoning** | A1 abstract argumentation; A2 structured and defeasible argumentation; A3 argument reconstruction, schemes, critical questions and fallacies; A4 dialogue, burden of proof, disagreement and evidential assessment. |
| **P19** | **Empirical Science of Reasoning** | E1 experimental methods and evidential standards; E2 deductive and conditional reasoning; E3 probabilistic judgment, calibration and heuristics; E4 explanation and analogy; E5 problem solving and visual/spatial reasoning; E6 metacognition, expertise, development and group reasoning. |

Move the primary treatment of **N-x-008** to P15 and **N-x-009** to P18 while preserving their IDs and existing navigation. Keep **N-x-015** identifiable as probability logic and quantitative verification in P9, linked to P15’s foundations.

Applied examples may come from science, law, engineering or everyday reasoning. The book covers their inference principles; it does not expand into a complete textbook of every applied discipline.

### C. Define the standard reference entry

Every applicable entry supplies:

1. **Purpose:** the question the method or system addresses.
2. **Inputs and conclusions:** what objects it takes and what it establishes.
3. **Definitions and assumptions:** including notation, types and scope.
4. **Rules or procedure:** with all necessary side conditions.
5. **Results and justification:** complete required proofs or exact source boundaries.
6. **Worked example.**
7. **Failure case or limitation:** showing why an assumption matters.
8. **Relationships:** prerequisites, alternatives and separately identified variants.
9. **Sources and destinations:** exact locators and links to full treatments.

Use existing manuscript environments and source records where possible. Do not create a second content-management system.

Empirical entries additionally require the task studied, population, design, measures, reported uncertainty, competing explanations and replication/generalization limits. A descriptive finding cannot become a normative recommendation without a separate argument.

A cited or sketched boundary is acceptable only when it accurately reflects the identified presentation and does not evade an existing obligation to supply a full proof.

## 3. Agent distribution and operating rules

### A. Four-slot working model

Use **one lead editor/integrator and at most three concurrent subagents**.

| Role | Responsibility |
|---|---|
| **Lead editor / root** | Own the catalog, dependency ordering, shared files, integration, review assignments and acceptance records. Resolve conflicts and keep the work moving. |
| **Author slot 1** | One mathematical correction or proof-development assignment. |
| **Author slot 2** | One independent subject-development assignment in disjoint files. |
| **Author slot 3** | One source-acquisition, additional writing or apparatus assignment, according to the immediate dependency queue. |

Whenever sources and prerequisites permit, keep at least two subagent slots on manuscript writing.

After an authoring wave, freeze the integrated units and use three fresh review contexts:

- **Source-fidelity reviewer:** exact source identity, complete assigned content, notation, qualifications and attribution.
- **Topic-specialist reviewer:** definitions, hypotheses, derivations, counterexamples and method validity.
- **Adversarial-publication reviewer:** omissions, misleading comparisons, dependencies, navigation and publication defects.

Reviewers file independently before seeing one another’s conclusions. Authors do not provide their own independent acceptance. A failure or unresolved uncertainty keeps the affected unit open.

### B. Required assignment contract

Every dispatch must contain:

- One concrete output and its requirement/catalog IDs.
- Exact owned files and permitted shared-file contributions.
- Identified source files, versions and passage ranges.
- Prerequisites that must already hold.
- Required statements, proofs, examples and boundary cases.
- Specific pass and failure conditions.
- The required return artifacts and continuation point.

Authors must be told that other agents share the workspace and that they must preserve others’ edits.

The lead owns the master driver, shared style, canonical bibliography, symbol registry and generated navigation. Authors use the existing intake mechanism and disjoint content files. Two writers never own the same host file simultaneously.

### C. Bound the work and prevent unattended agents

- Work in **45-minute blocks**, with a concrete checkpoint at least every 15 minutes.
- At the end of a block, return completed work, an exact continuation point, or a documented blocker.
- A time boundary never justifies shortening a proof or claiming completion.
- After two blocks without new manuscript content, a verified source acquisition or a resolved finding, the lead must split, redirect or block that assignment.
- After two unsuccessful repair cycles on the same finding, stop repeating the review loop. Identify the missing source, mathematical dependency or policy decision and assign that specific problem.
- Finish or interrupt agents after their assigned return; do not leave them running without an owned task.

Progress reports count actual catalog units by **drafted, text accepted, formally admitted and blocked** standing. Report source blockers separately. File counts, review reports and generated tables do not count as completed manuscript content.

## 4. Actionable execution program

### Stage 1 — Record policy and repair the necessary shared interfaces

These are bounded enabling changes, followed immediately by content work.

| Task | Owner | Success condition | Failure condition |
|---|---|---|---|
| **P1. Record the edition contract** | Lead, independently reviewed | The dated catalog, broader scope, reference-entry layer, nineteen-part order, free acquisition rule and direct-correction policy are explicit and consistent. | Earlier compression, normalization or fixed-fourteen-part rules still control conflicting behavior. |
| **P2. Separate stable part identity from printed order** | Integration specialist; lead merges | New P15 emits `p15` metadata when printed as Part XI; old P11 retains `p11` when printed later. Body, annex, symbols, review records and prose references agree. | Status/card records infer ownership from the printed counter, or an annex names the wrong part. |
| **P3. Bind validators to the edition catalog** | Integration specialist | Packet validation and coverage assignment use the same configured catalog, identity and count. Old catalog records remain traceable. | A validator still silently uses the historical catalog or two competing coverage authorities exist. |
| **P4. Resolve obsolete requirement components** | Lead plus three review roles | Each policy conflict has an explicit component-level disposition, preserving remaining content and output obligations. Closure machinery represents those dispositions truthfully. | Blanket waivers, marking obsolete demands “fulfilled,” or restoring an error to satisfy an old preservation check. |

For P2, update only actual consumers that assume fourteen parts or derive stable IDs from position: status/card metadata, part-order validation, symbol/review validation and annex numbering.

For P4, extend the current narrow supersession mechanism only for specifically reviewed policy decisions. Preserve original register rows.

### Stage 2 — Correct confirmed errors and missing foundational interfaces

Run the first three assignments concurrently; their main files are disjoint.

| Task | Required result | Specific acceptance condition |
|---|---|---|
| **C1. EL++ correction — INV-ELPP-001 / N-c-010** | Correct the completion procedure, decision criterion and dependent correctness argument. | The recorded seven-GCI nominal counterexample produces the correct outcome. Any query normalization used in the repair has a complete justification. The shared-nominal quotient argument is valid for the stated scope. A suggested repair without proof fails. |
| **C2. CSL endpoint correction — INV-CSL-001 / N-x-015** | Correct the timed-until interval claim and every dependent algorithm or explanation. | The absorbing-state example retains probability zero for the open-zero interval and one for the closed-zero interval. Any remaining endpoint equivalence has explicit hypotheses and justification. |
| **C3. CTL illustration — INV-CTL-001 / A-146** | Supply the missing root valuation and reconcile the diagram with the semantics. | The complete displayed model entails the displayed AFp verdict. An unlabelled assumption fails. |
| **C4. Definition-before-use repairs** | Complete R-032’s expanded-signature PA2 definition, S-013’s analytic-derivation definition, and D-P2-010’s substitution/replacement statements. | Each exact object and operation is defined on the active route before substantive use, with valid statement/proof links. Inactive text does not satisfy the task. |
| **C5. Recover missing active results and proofs** | Complete R-030’s four DLO extension cases, S-011’s active ACF result/attribution, and D-P2-007’s Tseitin statement and forward route. | The active reader can reach the exact result and every required case. A generic chapter pointer or table citation fails. |
| **C6. Arithmetic verification — R-002** | Supply the required arithmetic computation-verification development. | The omitted h1–h4 and step/digit verification components are actually derived. Naming coding primitives or retaining the current omission statement fails. |
| **C7. Long Part IX proof boundaries** | Resolve the outstanding N-c-012 and N-c-018 constructions at their promised scope. | Required construction steps are supplied; source sketches remain accurately distinguished. A larger bound does not establish the separately claimed original bound. Any proved source error receives a corrected treatment and explicit provenance. |

For all corrections, change the active definitions, formulas, statements and proofs. Keep historical evidence separately; do not make readers repair a still-active false statement.

### Stage 3 — Acquire the exact sources required for completion

Run acquisition alongside writing whose sources are already adequate.

Use publisher open access, author and institutional repositories, scholarly archives, freely available library access and other available free copies. Verify the actual document, not its filename.

The first acquisition queue is:

1. **N-x-014:** computable analysis, represented spaces and Weihrauch complexity.
2. **N-c-009/010:** exact 2003 and 2017 description-logic sources and required chapters.
3. **N-c-015:** downloadable complete Thatcher–Wright 1968 article.
4. **N-c-013:** McNaughton 1966 and Safra 1988.
5. **N-c-013/014:** Thomas’s published 1997 chapter, separately from the 1996 report.
6. **N-c-016:** Clarke–Grumberg–Peled 1999.
7. **N-c-017:** revised McMillan 1993 book, separately from the 1992 thesis.
8. **N-x-015:** Halpern 2003 Chapter 7.
9. **New reasoning parts:** primary treatments identified by the dated domain catalog.
10. **Bibliographic discrepancies:** resolve exact edition and pagination conflicts, including the Baader–Snyder chapter.

**An acquisition passes only when** identity, version, full required extent, readable body, locator and local file hash are verified.

**It fails when** the evidence is only metadata, a preview, a wrong version or an incomplete article. An unavailable required source blocks its dependent unit and final release; unrelated work continues. Availability does not authorize substituting another presentation.

### Stage 4 — Complete the existing subject areas

Assign these streams in dependency order. Each stream includes **every current-ledger component mapped to its parts**, not just the examples below.

| Specialist stream | Required work | Stream-specific failure conditions |
|---|---|---|
| **Foundations and classical logic — P1/P2** | Complete active definitions, calculi, substitution, Post/Tseitin and higher-order adequacy obligations; reconcile inherited foundations. | Missing side conditions, inactive required results, or undefined objects used in reductions. |
| **Model theory — P3** | Complete required categoricity, compactness, type, classification and preservation developments. | A requested proof remains an outline, or finite/infinite-model hypotheses are conflated. |
| **Computability and arithmetic — P4/P5** | Complete coding, reductions, MRDP and incompleteness dependencies, Goodstein/hydra and Solovay obligations, and computable-analysis links. | An encoding or reduction is asserted without the required construction or direction of implication. |
| **Set theory — P6** | Complete the catalogued forcing, PCF, proper-forcing, PFA/MM and inner-model treatments. | Relative consistency, model existence or independence is overstated, or a required source presentation remains cited in place of its supplied proof. |
| **Proof theory and type theory — P7** | Complete normalization, interpretation, Gentzen, higher-order, HoTT/cubical and proof-net obligations. | Circular normalization arguments, missing translation cases or undeclared equality/type assumptions. |
| **Nonclassical logic — P8** | Complete each identified modal, temporal, relevance, many-valued, substructural, conditional, deontic and nonmonotonic presentation. | Rules, semantics or evidence from different systems are combined without justified bridges. |
| **Logic in computer science — P9** | Finish finite-model, automata, temporal, description-logic, verification and programming-logic obligations; complete SHOIQ/OWL coverage. | Missing exact sources, unfinished constructions, incorrect algorithm claims or stale comparison tables. |
| **Algebraic and categorical logic — P10** | Complete required HSP, duality, algebraization, locale, topos and internal-logic developments. | Claimed equivalences lack hypotheses or directions, or source-specific theories are collapsed. |
| **Philosophy of logic — P11** | Expand truth, paradox, vagueness, consequence and philosophical argument treatments to their catalogued depth. | A named position has only a capsule description, or a philosophical argument is represented as a mathematical theorem without warrant. |
| **Automation and formal practice — P12** | Complete Nelson–Oppen, unification, rewriting, superposition, extraction and proof-assistant trust boundaries; cover AI-assisted reasoning within the dated catalog. | A successful tool run substitutes for a correctness argument, or generated answers are confused with checked proofs. |
| **History — P13** | Complete chronology, biographies, notation lineage and attribution. | Dates or priority claims lack sources, or modern notation is attributed retrospectively without qualification. |

A stream passes when all assigned catalog units satisfy the common acceptance gates below. Previously accepted evidence is reused only when its source, content and dependencies still match.

### Stage 5 — Write the new reasoning parts

Use one specialist stream per new part, scheduled through the three available authoring slots.

- **P15 first:** stabilize probability and statistical foundations before dependent causal, decision and empirical treatments.
- **P16:** begin logical abduction and explanatory methods in parallel; causal identification follows the required probability foundations.
- **P17:** develop preferences and representation first, followed by uncertainty, sequential decisions and strategic/collective reasoning.
- **P18:** complete abstract argumentation first, then structured arguments and practical analysis.
- **P19:** establish empirical evidence standards first; subsequent chapters use those standards and the relevant normative foundations.

Each of the 26 chapters is a separate parent assignment, divided at genuine source, definition or lemma boundaries.

Specific acceptance scenarios include:

| Area | Required scenario |
|---|---|
| Bayesian inference | A worked prior-odds/likelihood-ratio calculation distinguishes evidence strength from posterior probability and checks sensitivity to assumptions. |
| Statistical inference | Confidence, credibility and significance claims are distinguished by their actual definitions; examples demonstrate the consequence of confusing them. |
| Abduction | Competing explanations are generated and assessed using the stated consistency, minimality or preference criterion. |
| Causation | Observational conditioning and intervention are distinguished; a confounding or collider example demonstrates a failed inference. |
| Decision theory | A worked choice follows from explicit preferences, information and risk assumptions; removing a representation assumption changes the warranted conclusion. |
| Argumentation | Extension semantics are calculated on concrete attack graphs, including a cycle; informal examples identify implicit premises and relevant defeaters. |
| Empirical reasoning | A finding is traced to its design and evidence, with uncertainty and generalization limits; competing results are represented rather than suppressed. |

A chapter fails if it contains topic names without the required methods, omits its worked cases, or treats empirical, normative and deductive claims as interchangeable.

### Stage 6 — Complete the reference apparatus

The apparatus specialist closes all **201 original apparatus requirements**, plus the lookup obligations introduced by the new parts.

Required outputs include:

- Subject/system lookup and task/property lookup.
- Complete chapter contents, bookmarks and appropriate lists of tables, figures and listings.
- Theorem, method, symbol and name indexes.
- Required calculus sheets and comparison tables derived from accepted content.
- Glossary coverage for catalogued core terms and ambiguous terminology.
- Correct exercise/feedback navigation.
- Complete bibliography and exact source locators.
- Reconciled printed part numbers, captions and cross-references.

**Pass conditions:** every catalogued method is reachable through both subject and task navigation; each comparison states the hypotheses under which it holds; every relevant symbol role is recorded; all required links resolve; the index meets the existing minimum of 2,500 meaningful entries without padding.

A count alone cannot pass an apparatus task. Its entries must be correct and useful.

## 5. Verification, admission and release

### A. Accept content through explicit gates

| Gate | Pass | Fail |
|---|---|---|
| **Authority** | Exact source presentation and required body are available, or the unit is an explicitly justified manuscript correction. | Wrong edition, inaccessible proof, unsupported attribution or unresolved source identity. |
| **Content completeness** | Every assigned definition, rule, hypothesis, proof component, example and qualification is supplied. | Omitted cases, compressed required proofs or pointers replacing owed content. |
| **Mathematical or empirical validity** | The argument or evidence supports exactly the stated conclusion. | Counterexample, invalid inference, circular dependence or overstated empirical result. |
| **Reference usability** | Entry, full treatment, prerequisites, alternatives and source locations agree and are reachable. | Misleading summaries, broken dependencies, inconsistent notation or missing lookup routes. |
| **Production** | Relevant static checks, build and visual checks pass for the recorded scope. | Stale output, unresolved diagnostics, missing glyphs, clipped content or uninspected required pages. |
| **Formal admission** | Independent records bind the exact content, sources and all required gates. | A positive inventory flag, self-review or valid schema is used as a substitute for acceptance. |

Reviewers read the **actual manuscript LaTeX** for content and mathematical assessment. Source documents supply the authority comparison. Rendered manuscript pages are inspected for publication quality after the content has been assessed.

Use independent recomputation and explicit countermodels for mathematical examples. Use existing static/build tools for mechanical checks. Add focused regression checks only for genuine changes to shared style, validators or generators; do not build software test suites that merely repeat manuscript prose.

### B. Sequence admission and generated navigation without circular dependencies

1. Freeze a unit’s maintained content and real dependencies.
2. Complete the three independent reviews, scoped static checks, an internal unit/dependency build and inspection of that output.
3. Record the exact scope and hashes, then admit the unit through the existing admission mechanism.
4. Generate lookup surfaces from admitted content projections. Keep these downstream artifacts outside the source unit’s content identity.
5. Build and validate the integrated book, including all generated reference material.

If integration changes mathematical content or a relevant dependency, reopen the affected reviews. If it changes only pagination or presentation, repeat the affected output checks and final book validation without re-proving unchanged mathematics.

### C. Final release checklist

The book is ready for final user acceptance only when:

- All 615 original requirements have valid terminal dispositions.
- Every first-edition catalog unit is admitted.
- All inherited substantive units are preserved or directly corrected with recorded provenance.
- No required source, proof, correction or coverage gap remains open.
- All applicable independent review gates pass.
- Bibliography, indexes, notation, tables and cross-references are complete.
- The integrated manuscript passes the existing strict checks.
- A clean build succeeds using the configured LaTeX toolchain.
- **Every page of the final PDF** has recorded visual inspection.
- The terminal-readiness record has zero non-user residuals and pins the exact final artifact.

The user then supplies final editorial acceptance against the exact PDF and readiness hashes.

The lead reports remaining work through concrete catalog units and blockers throughout execution. Completion is determined by these conditions, with no unconditional date promised while required free-source access or mathematical dependencies remain unresolved.

