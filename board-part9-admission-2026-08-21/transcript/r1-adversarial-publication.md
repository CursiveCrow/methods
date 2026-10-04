REJECT

# Part IX R1 adversarial-publication review

## Verdict and review boundary

The current Part IX reader route is not source/content admissible. Its labels and citations are mechanically coherent, and several individual statements have appropriately narrow finite/data-complexity qualifications. However, the chapter remains a short survey where the register requires reconstructible calculi, algorithms, correctness arguments, comparison tables, figures, and retrieval surfaces. Four failures are independently blocking: the printed `\mathcal{ALC}` tableau accepts an unsatisfiable input under its own stated rules; the Hoare calculus and its alleged soundness proof do not have a complete registered rule surface; the CTL labelling method is not a total algorithm for the language it names; and the separation-logic frame rule is stated without the command/heap condition needed for soundness. The rest of the findings document additional mandatory content and publication-apparatus omissions.

This was a blind, read-only source audit. I read `board-part9-admission-2026-08-21/charter.md`, the complete live route rooted at `handbook/parts/p09.tex` and `handbook/annex/p09.tex`, the referenced existing results, the calculus registry, `handbook/generated/audit-p09.tex`, the named-theorem and symbol retrieval surfaces, the bibliography, and the P9-targeted register rows. I did not read another seat's transcript or conclusion, edit manuscript/spec/tool/generated source, run tests, run a TeX/PDF build, or inspect rendered pages. Static source findings below therefore do not establish or deny final pagination, float placement, overfull boxes, index collation, or clickable-PDF behaviour.

## Findings

### AP9-F1 [blocker] [open] The displayed `\mathcal{ALC}` tableau is not a decision procedure for the grammar it defines

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:118-136,146-164`; obligation `spec/registers/new-content.csv:116` (N-c-009).
- **Claim:** The concept grammar admits `\top`, `\bot`, and arbitrary `\neg C` at lines 121-124. The method decomposes only conjunction, disjunction, existential, and universal restrictions, and closes only on `A` together with `\neg A` at lines 151-155. It never converts the input and internalized GCIs to negation normal form, gives no rules for negated compound concepts, and gives no `\bot` clash rule. Nevertheless lines 158-162 call it a terminating decision procedure.
- **Concrete failure:** Give the method the legal input concept `\bot` and an empty TBox. The root label is `{\bot}`. No printed decomposition or clash rule applies, so the branch is exhaustively open and is not blocked. The method therefore reports an open branch for an unsatisfiable concept. The same problem occurs with `\neg\top`; internalizing a GCI as `\neg C\sqcup D` also introduces precisely the negation forms for which no normalization rule is printed.
- **Harm:** A reader following the exact algorithm obtains a false satisfiability answer. Termination alone does not supply the correctness ceiling required by N-c-009.
- **Exact correction:** Before expansion, convert the input and every internalized GCI to a fixed NNF whose negation occurs only on concept names; state the complement operation used by closure. Add the `\bot` clash and all constructor rules, state that blocking occurs only on saturated labels, and give a status-bearing theorem that a complete branch is open exactly when the input is satisfiable, with the termination and model/unravelling directions proved or explicitly sketched in a reciprocal annex item.
- **Status:** open; source/content blocker independent of build/visual gates.

### AP9-F2 [blocker] [open] The Hoare theorem names a calculus that is neither displayed nor registered

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:289-322`; `handbook/CONVENTIONS.md:60-72,162-180`; `spec/registers/apparatus.csv:23,97,193` (A-022, A-096, A-192); `spec/registers/new-content.csv:126` (N-c-019); `spec/registers/depth-gaps.csv:135` (D-P11-008).
- **Claim:** Lines 300-305 display assignment and while, while consequence, sequencing, and conditional are only named. Theorem `thm:p09-hoare-soundness` at lines 309-313 nevertheless claims soundness of the “displayed assignment, consequence, sequencing, conditional, and while rules.” A current-registry search finds no `sheet:hoare*` identity or Hoare calculus file. The two body inference displays also violate the binding rule at `handbook/CONVENTIONS.md:173-180` that new editorial rule displays live only in `registry/calculi/`.
- **Status contradiction:** The theorem token is `cited=Apt1981`, which `handbook/CONVENTIONS.md:64-66` defines as “statement only; source carries the proof,” but lines 315-322 print a local paragraph headed `Proof.` The paragraph is at most a sketch: the command transition semantics, the substitution lemma, and three of the five rule shapes are absent. It is neither the cited-only standing printed by the status token nor a reciprocal annex proof/sketch.
- **Additional unmet ceiling:** N-c-019 expressly requires a worked verification example; none occurs anywhere in the 442-line body. Total correctness is defined at lines 289-298 but has no variant rule or worked total-correctness surface.
- **Harm:** A reader cannot determine derivability in the claimed calculus, check the theorem against the actual side conditions, or reconstruct the promised example. The generated audit repeats the misleading cited-only standing at `handbook/generated/audit-p09.tex:27`.
- **Exact correction:** Add the registered A-022 Hoare sheet with the exact command language, assertion substitution, assignment, consequence, sequence, conditional, while, and any total-correctness variant rules and side conditions. Link the body to that sheet and replace the body rule displays with the registered route. Supply the A-096 comparison/wp table and one fully worked derivation. Put a complete soundness proof in a reciprocal annex item and use `proved=annex:<id>`, or put a declared incomplete sketch there and use `sketched=annex:<id>`; do not retain both `cited=` and an inline editorial proof.
- **Status:** open; source/content blocker.

### AP9-F3 [blocker] [open] The frame rule is unsupported without a local heap-action semantics

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:332-349`; obligation `spec/registers/new-content.csv:127` (N-c-020).
- **Claim:** The chapter defines heap disjointness and separating conjunction, then prints the frame rule with only the store-variable condition that `C` not modify a free variable of `R`. It defines neither a heap command language nor an operational/local-action condition saying execution on one subheap leaves a disjoint framed subheap untouched. N-c-020 requires frame-rule soundness at statement/sketch level, but no theorem/status/proof is present.
- **Concrete failure:** Under the chapter's unrestricted metavariable `C`, take a command that clears the entire heap while modifying no program variable free in `R`. The premise `{\top}\,C\,{\top}` is valid. Let `R` assert ownership of a particular disjoint cell. A starting heap can satisfy `\top*R`, but after whole-heap clearing it cannot satisfy `\top*R`. Thus the displayed conclusion fails even though the sole printed side condition holds.
- **Harm:** The handbook presents an invalid inference rule under its stated assumptions and then cites it as the basis of symbolic execution and bi-abduction.
- **Exact correction:** Fix a command/heap transition semantics and state the exact property used by the frame proof: execution or safety on the owned subheap must preserve every disjoint heap fragment and leave it unchanged, in addition to the free-variable/modification condition. Then state and status a frame-rule soundness theorem under those hypotheses, with proof or cited source. If a registered separation-logic sheet is chosen, route the rule only through that sheet.
- **Status:** open; source/content blocker.

### AP9-F4 [blocker] [open] The CTL “labelling algorithm” is partial and has no correctness proof

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:229-255`; obligation `spec/registers/new-content.csv:123` (N-c-016).
- **Claim:** Definition `def:p09-ctl` gives examples only for `EG` and `E[U]`; it supplies no complete CTL grammar or inductive semantics. Lines 242-255 then give two fixed-point equations and call them “the standard finite-state labelling algorithm.” There is no clause for atoms, Boolean connectives, `EX`, universal next/until, or a declared dual-normal-form preprocessing step. There is also no correctness theorem/proof, although N-c-016 requires an E-level labelling algorithm with correctness proof.
- **Concrete failure:** Give the alleged algorithm the basic CTL input `EX p` (or `AX p`). Neither the definition nor the two equations gives a recursive labelling clause for that input. The procedure therefore has no specified next state, output, or acceptance condition for a formula in the language it names.
- **Harm:** The advertised complexity at lines 251-255 is attached to no total algorithm over an exact input language. The reader cannot reconstruct model checking from the printed surface.
- **Exact correction:** Reuse or cross-reference the complete CTL state-formula syntax and semantics already live at `handbook/parts/p08/temporal-epistemic-supplement.tex:58-128`, fix a normal-form convention, and print labelling clauses for every remaining constructor (or explicit dual reductions plus their base clauses). State the worklist/fixed-point initialization and termination measure, prove by structural induction that each computed label is the semantic truth set, and derive the complexity under the declared explicit finite representation.
- **Status:** open; source/content blocker.

### AP9-F5 [blocker] [open] The omega/tree-automata route lacks exact machines, runs, and the promised model-checking construction

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:177-227`; `spec/registers/new-content.csv:119-122` (N-c-012 through N-c-015); `spec/registers/depth-gaps.csv:94` (D-P10-010).
- **Claim:** Definition `def:p09-omega-automata` states only acceptance slogans. It never fixes an automaton tuple, alphabet, initial state, transition relation, run compatibility, or whether each parity/Rabin machine is nondeterministic or deterministic. It says the models may be words “or trees” at lines 203-206, then concedes at lines 226-227 that a tree model and branching convention “must be specified” without specifying either. The body does not link to the complete nondeterministic Buechi word-automaton definition and worked figure already live at `handbook/parts/p08/temporal-epistemic-supplement.tex:353-401`.
- **Missing required construction:** D-P10-010 requires automata-theoretic LTL model checking. Lines 211-216 cite an LTL-to-Buechi translation and complementation, but there is no product of the transition system with the automaton for the negated property, no accepting-cycle/emptiness condition, no returned verdict or counterexample, and no complexity statement for that construction.
- **Harm:** A reader cannot reconstruct what constitutes a run or decide whether a given machine accepts a word/tree, much less reconstruct the promised model-checking algorithm. The named acceptance conditions float free of exact machine classes.
- **Exact correction:** Link to and reuse the existing Part VIII Buechi definition rather than create an unannounced second identity. Add exact parity and Rabin word/tree automaton data and run clauses, state the selected tree branching/acceptance convention, and give the LTL model-checking product plus accepting-run emptiness test, output/counterexample condition, and complexity. Keep finite-word BET, S1S, and S2S statements separate from infinite-word/tree acceptance.
- **Status:** open; source/content blocker.

### AP9-F6 [blocker] [open] Deliverable-level theorems evade the mandatory proof-status and generated-index apparatus

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:75-100,102-113,166-172,190-225,251-284,324-330,371-410`; `handbook/CONVENTIONS.md:60-72`; `handbook/generated/audit-p09.tex:15-30`; `handbook/generated/named-theorem-index.tex:12,163,357`.
- **Claim:** The chapter has only three local status-bearing theorem identities: the zero--one law, the `\mathcal{ALC}`/modal correspondence, and Hoare soundness. Numerous register-deliverable results appear as ordinary prose with a citation but no exact `proved`/`sketched`/`cited` standing: Gaifman/Hanf locality and the two inexpressibility consequences; decidability/complexity of monadic FOL, `\mathrm{FO}^2`, and the guarded fragment; `\mathcal{ALC}` complexity; Kamp; LTL-to-Buechi; BET/S1S/S2S; CTL algorithm correctness; PDL completeness; Cook relative completeness; SLD completeness; stable-model existence complexity; Chandra--Merlin; Datalog complexity; and the CSP dichotomy.
- **Specific mismatch:** The local Fagin “Proof idea” at lines 87-94 supplies an editorial sketch next to a cross-part theorem whose public standing is cited, but no annex target or local status records that additional sketch. Hoare's cited/inline-proof mismatch is AP9-F2.
- **Harm:** The 16-row generated audit omits most of the chapter's substantive theorem claims, and the named-theorem index exposes only the three local theorem environments. A reader cannot tell which arguments the handbook claims to supply and which remain entirely source-carried. This violates the charter's exact-proof-status invariant even if every bibliography key resolves.
- **Exact correction:** Give each deliverable-level result a single public identity: either a status-bearing local theorem, or an explicit `Theorem~\ref{...}` link to an already status-bearing public result. Put every new editorial proof/sketch in a reciprocal P9 annex item with enumerated omissions for sketches; leave `cited=<key>` only where the handbook prints the statement and the source carries the proof. Regenerate both the P9 audit and named-theorem index after the identities are fixed.
- **Status:** open; source/content and retrieval blocker.

### AP9-F7 [must-fix] [open] Lot 1 omits mandatory finite-model and prefix-class material

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:14-113`; `spec/registers/new-content.csv:108-115` (N-c-001 through N-c-008); `spec/registers/apparatus.csv:37,45,53` (A-036, A-044, A-052).
- **Claim:** The chapter covers finite compactness failure, Trakhtenbrot, a zero--one statement, locality prose, Fagin, Immerman--Vardi, and one sentence about fragments. It omits N-c-001's finite Craig/Beth failures and finite EF-game method; it names but does not display N-c-002's extension axioms or give a navigable random-graph route; and it does not supply N-c-005's required table of BSR, Ackermann, Goedel--Kalmar--Schuette, reduction classes, and decidable/undecidable boundaries. The monadic paragraph says merely “a declared equality convention” rather than declaring whether equality is present for the stated decision result.
- **Existing but inaccessible apparatus:** A complete decidable-fragments table already exists at `handbook/parts/p02/first-order-depth.tex:188-233` under `tab:p02-decidable-fragments`, and descriptive-complexity apparatus exists at `handbook/parts/p04/complexity.tex:477-500` under `tab:p04-descriptive-complexity`; P9 links to neither. No A-044 finite-model comparison table is present on the P9 route.
- **Harm:** Several must/should register topics cannot be retrieved at all, while the one-sentence prefix paragraph can be mistaken for fulfillment of a table/classification ceiling it does not meet.
- **Exact correction:** Add a finite-model section that states and statuses the finite Craig/Beth boundaries, gives the exact finite EF-game/invariance method or a precise live cross-reference, prints the extension-axiom/random-structure bridge, and adds the A-044 finite/unrestricted comparison. Add an explicit route to `tab:p02-decidable-fragments` and the descriptive-complexity table, supplementing them with any P9-only prefix classes and reduction boundaries required by N-c-005 rather than duplicating existing rows.
- **Status:** open.

### AP9-F8 [must-fix] [open] The description-logic family/OWL deliverable is replaced by six survey lines

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:166-172`; `spec/registers/new-content.csv:117-118` (N-c-010, N-c-011); `spec/registers/apparatus.csv:96` (A-095); bibliography source at `handbook/bib/handbook.bib:2187-2196`.
- **Claim:** N-c-010 requires the lightweight/expressive constructor families, EL-family classification, DL-Lite query role, and a SHOIQ/OWL profile map; A-095 requires a labelled ALC-through-SROIQ complexity/OWL table. The live body gives only six prose lines and no table, exact constructor profiles, reasoning problem per bound, or OWL correspondence.
- **Source-role discrepancy:** N-c-011 names the Schild correspondence and source, but `thm:p09-alc-modal` at lines 138-144 is `cited=SchmidtSchaussSmolka1991`; no Schild bibliography entry exists. Schmidt-Schauß--Smolka is a real, resolved bibliography entry, but the current source apparatus does not explain the substitution for the register's controlling correspondence source.
- **Harm:** Family names are introduced without the exact constructors/decision problems that make their complexity bounds meaningful, directly violating the charter's no-family-wide-transfer rule.
- **Exact correction:** Supply A-095 with one row per selected logic/profile, listing its exact constructors, ontology/ABox/query task, input convention, complexity, OWL correspondence, and controlling source. Add the Schild primary entry/citation for N-c-011 or explicitly justify and source the replacement; do not infer an SROIQ/OWL bound from the ALC theorem.
- **Status:** open.

### AP9-F9 [blocker] [open] Logic-programming/database claims lack the registered calculus and exact complexity surfaces

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:351-410`; `spec/registers/new-content.csv:128-132` (N-c-022 through N-c-025); `spec/registers/depth-gaps.csv:133-134` (D-P11-006, D-P11-007); `spec/registers/apparatus.csv:24,98,149` (A-023, A-097, A-148).
- **Claim:** The definite-program/least-model definition is useful, but the SLD calculus is only four prose lines. There is no `sheet:sld*` registry identity, rule shape, computed-answer substitution, standardization-apart condition, failure/selection-tree definition, or A-148 worked SLD tree. Thus the claimed soundness/completeness at lines 371-374 is not reconstructible at the E ceiling of N-c-022.
- **Stable-model syntax gap:** Lines 379-391 define the reduct for a “normal program” but never print the normal-rule grammar that determines the positive body, default-negated body, allowed head, or atom universe before the deletion clauses operate.
- **Complexity gap:** Lines 398-404 state Chandra--Merlin and say only that Datalog combined complexity is “strictly larger.” N-c-024 requires containment decidability and exact data/combined complexity; A-097 requires SLD, negation-as-failure, completion, well-founded, stable-model, and Datalog comparison. Neither exact comparison nor any labelled table exists.
- **Harm:** The reader cannot reproduce an SLD derivation or know the exact decision problem behind the database bounds. The omission also leaves the stable-model definition's input syntax implicit at the point where the charter requires exact syntax/problem.
- **Exact correction:** Add the A-023 registered SLD sheet with unification, renamed-apart clauses, selection/fairness, computed answers, and the negation-as-failure boundary; add the A-148 worked tree. Print the exact finite ground normal-rule grammar before the reduct. Add A-097 with separate rows/problems for completion/SLDNF/well-founded/stable/Datalog semantics and exact data/combined bounds, and status the SLD, Chandra--Merlin, and stable-existence results.
- **Status:** open; source/content blocker for the must-level SLD ceiling.

### AP9-F10 [must-fix] [open] The required P9 complexity treatment is explicitly deferred without navigable proof routes

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:412-442`; obligation `spec/registers/new-content.csv:133,135` (N-c-026, N-c-028).
- **Claim:** The only local complexity surface is an uncaptioned, unlabeled `tabularx` at lines 415-429. N-c-026 requires a Cook--Levin recap, a QBF PSPACE-completeness proof, a Ladner-style modal table, and a first-order undecidability recap. Lines 431-435 instead say the QBF/Cook--Levin/FOL results are established in Parts IV and V without any theorem/section reference, and reduce the modal comparison to prose. The required new QBF proof is therefore neither present nor navigable.
- **Harm:** A prose assurance that another part contains a result is not a retrieval path. The table cannot be cited, cannot enter the list of tables, and does not carry the full registered problem/input/status distinctions.
- **Exact correction:** Either provide the required QBF proof in a reciprocal P9 annex item or cite the exact existing theorem/proof destination and amend the register contract explicitly; add exact `\ref`/`\hyperref` routes for Cook--Levin and FOL. Convert the current complexity summary into a captioned, labelled table that includes the modal rows and the missing P9 problems with their finite/data/combined qualifications. Keep the McMillan pointer explicitly at pointer ceiling with a live Craig-interpolation destination.
- **Status:** open.

### AP9-F11 [must-fix] [open] P9 has no live registered table or figure apparatus

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:1-442`; `handbook/generated/audit-p09.tex:3-31`; `spec/registers/apparatus.csv:45,96-98,114,146-149` (A-044, A-095 through A-097, A-113, A-145 through A-148).
- **Evidence:** The body contains zero `table`, `longtable`, `figure`, `\caption`, `tab:*`, or `fig:*` surfaces. Its only `tabularx` is the unlabeled complexity block at lines 415-429. The sole captioned P9 table is the generated audit file, which is not routed (AP9-F12). Required P9-facing A-044, A-095, A-096, A-097, and A-148 artifacts are absent.
- **Existing cross-part assets not used:** The temporal comparison and A-145/A-146/A-147 figures are live at `handbook/parts/p08/temporal-epistemic-supplement.tex:293-401`; the P9 chapter does not reference them. A-036 and A-052 likewise exist in Parts II/IV but are not linked from P9.
- **Harm:** Readers get no reconstructive diagrams for LTL/CTL/Buechi or SLD and no citable comparison apparatus for the main P9 families, even though the prose repeatedly relies on distinctions that those registered artifacts were meant to stabilize.
- **Exact correction:** Route existing cross-part assets by exact labels rather than duplicating them, then add the genuinely missing finite-model, DL-family, Hoare/wp, logic-programming, and SLD-tree artifacts with one caption/label each. Give every prose table a labelled floating/longtable identity appropriate for lists and cross-reference it at first use.
- **Status:** open.

### AP9-F12 [must-fix] [open] The generated Part IX audit exists but is unreachable from the Part IX route

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09.tex:1-3`; `handbook/generated/audit-p09.tex:1-31`; A-113 at `spec/registers/apparatus.csv:114`.
- **Claim:** `handbook/generated/audit-p09.tex` contains a valid 16-link theorem/definition register with label `tab:p09-theorem-definition-register`, but the P9 driver inputs only `parts/p09/logic-in-computer-science`. Neither the body nor annex inputs the generated file. The table therefore has source labels and links but no reader destination.
- **Harm:** A-113 is not fulfilled on the live route, and a reader has no Part IX theorem/definition retrieval table even though the file's existence can be mistaken for publication.
- **Exact correction:** Add one Part IX register section with a public section label and exactly one `\input{generated/audit-p09}` on the live body route. Regenerate it after AP9-F6 so its rows cover the actual deliverable-level result identities; then separately confirm its rendered continuation heads and links in the final build/visual gate.
- **Status:** open.

### AP9-F13 [blocker] [open] The symbol registry has virtually no Part IX coverage

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/registry/symbols.csv:316`; `handbook/parts/p09/logic-in-computer-science.tex:118-130,177-185,242-265,327-341,354-390`; A-160/A-193 at `spec/registers/apparatus.csv:161,194`.
- **Evidence:** The 633-row CSV, 633 generated table destinations, and 633 symbol-index targets agree mechanically. Yet a scope/first-use query returns exactly one P9-scoped row: the least-fixed-point constructor at `handbook/registry/symbols.csv:316`. The chapter introduces many other load-bearing notations without a P9 registry standing: ALC constructors and `\sqsubseteq`; temporal `X,U,F,G`; CTL `EG,E[U]` and `\operatorname{Pre}_{\exists}`; fixed-point `\mu,\nu`; `\operatorname{wp}`/`\operatorname{wlp}`; heap `\perp,\uplus,*`; `T_P`; and the reduct `P^M`.
- **Concrete collision path:** In existing registry scopes, `\mu` is minimization in P4 and a modal binder in P8, while `\perp`/`*` already have non-heap roles. With no P9 rows, the public symbol index cannot tell a Part IX reader which role applies, and no registration-page link leads to these P9 definitions.
- **Harm:** The generated symbol surface is internally consistent but semantically incomplete for the audited part. A-160's “single source” architecture does not establish A-193 coverage.
- **Exact correction:** Add eliminable, scope-limited P9 rows for every new notation, with role, precedence/standing, first-use anchor, and collision note; extend existing temporal/fixed-point rows to P9 only where the exact syntax is genuinely reused. Regenerate both symbol tables and index and require the destination/target sets to agree after the additions.
- **Status:** open; publication/retrieval blocker.

### AP9-F14 [must-fix] [open] Further reading and cross-part reciprocity are missing

- **Author:** adversarial-publication, R1.
- **Location:** `handbook/parts/p09.tex:1-3`; `handbook/parts/p09/logic-in-computer-science.tex:174-284,431-435`; `handbook/annex/p09.tex:1-15`; `handbook/parts/p14/master-tables.tex:246-264`; A-186/A-189 at `spec/registers/apparatus.csv:187,190`.
- **Claim:** Part IX has no per-part further-reading section. The global P14 map has only three starting sources for IX at line 260, which does not replace A-186's per-part annotated route. P9 repeats or paraphrases LTL, CTL, CTL*, modal-mu, Buechi, and PDL material without linking to the exact Part VIII definitions, tables, figures, or sheets; its “Parts IV and V” complexity deferral likewise has no exact destination. The navigation-only annex provides broad section descriptions but no rule-sheet, generated-audit, or proof-item route.
- **Harm:** Readers cannot distinguish deliberate reuse from duplicate identities and cannot follow claims to the more complete existing surfaces. This is especially harmful where the P9 restatement is thinner than the P8 definition.
- **Exact correction:** Add an annotated Part IX further-reading section covering all four charter lots and their source roles. At each reused system, link to the existing exact definition/table/figure/sheet before giving the P9 algorithmic specialization. Replace every “Parts IV/V” or generic “tree automata” pointer with an exact live label or a clearly cited external pointer when no internal destination exists.
- **Status:** open.

## Coverage map by charter lot

### Lot 1 — finite-model theory, locality, descriptive complexity, and fragments

- **Not clean:** AP9-F6, AP9-F7, AP9-F10, AP9-F11, AP9-F13.
- **Checked clean:** The finite/unrestricted distinction is explicit at `logic-in-computer-science.tex:14-31`; the zero--one distribution is typed by finite labelled structures at lines 33-49; Fagin and Immerman--Vardi point to live public labels and preserve the finite/order hypotheses at lines 82-100. No claim that a fixed-size probability is already zero or one is made.
- **Not checked by build:** rendered cross-part hyperlinks and table placement.

### Lot 2 — description logics

- **Not clean:** AP9-F1 and AP9-F8; AP9-F11/F13 also apply.
- **Checked clean:** `def:p09-alc` fixes the ALC syntax, domains, roles, individuals, TBox/ABox distinction, and the modal theorem correctly excludes global TBoxes from the notational equivalence. The blocker concerns the algorithm and missing family apparatus, not those semantic clauses.

### Lot 3 — temporal logics, automata, model checking, and modal fixed points

- **Not clean:** AP9-F4, AP9-F5, AP9-F6, AP9-F11, AP9-F13, AP9-F14.
- **Checked clean:** LTL next/strong-until clauses are explicit for infinite words; safety and liveness are not equated with single surface operators; bounded model checking explicitly disclaims an unbounded proof without a completeness bound at lines 269-278; the mu-calculus positivity condition correctly marks the monotonicity requirement. The missing alternation-hierarchy statement from N-c-018 remains part of the coverage defect.

### Lot 4 — program logics, logic programming/databases/CSP, and complexity

- **Not clean:** AP9-F2, AP9-F3, AP9-F6, AP9-F9, AP9-F10, AP9-F11, AP9-F13.
- **Checked clean:** Partial and total correctness are distinguished at lines 289-298; the stable-model definition is explicitly restricted to finite already-ground propositional normal programs and does not transfer its NP bound to disjunctive programs; Datalog's data-complexity qualifier and the fixed-template CSP qualifier prevent the most obvious family-wide overclaims. The blockers concern missing syntax/calculi/proofs and incomplete combined-complexity apparatus.

## Cross-cutting static checks that passed

- `handbook/main.tex:33,51` routes the P9 body and annex exactly once.
- The P9 body/annex/generated-audit surface contains 21 distinct static references, all with source targets. The 23 local P9 body targets are distinct; no local duplicate label was found.
- The body cites 46 distinct bibliography keys; all 46 resolve among the 551 current bibliography entries.
- The 426-row named-theorem index contains all three current local P9 theorem environments, and their targets resolve. AP9-F6 concerns theorem identities missing from the status apparatus, not broken links for the three that exist.
- The unrouted P9 audit contains 16 links and each target exists. AP9-F12 concerns its route and AP9-F6 its incomplete semantic coverage.
- The 633 symbol registrations, generated destinations, and index targets agree with zero set difference. AP9-F13 concerns missing P9 registrations, not generator drift among existing rows.
- A noncomment reader-route scan found no uppercase OPEN/TODO/FIXME, `\hbstub`, internal A/N/D-P row ID, workflow/finalizer language, or pointer-only construction notice. The word “open” at line 157 is the legitimate semantic description of a tableau branch.

## Prioritized repair order

1. Repair the false/partial algorithms and rules first: AP9-F1, AP9-F2, AP9-F3, AP9-F4, and AP9-F5.
2. Establish one status-bearing identity and reciprocal proof route per deliverable result (AP9-F6), then regenerate and route the P9 audit (AP9-F12).
3. Complete the must-level finite-model, DL, SLD/database, and complexity register ceilings (AP9-F7 through AP9-F10).
4. Add/link the registered tables and figures (AP9-F11), register P9 notation and regenerate symbol retrieval (AP9-F13), then close further-reading and cross-part navigation (AP9-F14).
5. Only after source/content repair, run the separate reference/build/visual/human/user gates. Static inspection cannot approve their outcomes.

## Final R1 disposition

Part IX is mechanically navigable at the labels and citations it currently exposes, but it does not meet the charter's mathematical, reconstructibility, status, apparatus, symbol, or register-completion invariants. The current source/content verdict is **REJECT**.
