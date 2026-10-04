REJECT

# Part VIII R3 adversarial-publication admission review

## Scope and evidentiary boundary

I reviewed the current reader graph rooted at
`handbook/parts/p08.tex` and `handbook/annex/p08.tex`: all forty exact-source
wrappers on the body route, every routed Part VIII supplement, the three annex
inputs, every calculus sheet reached through the Part VIII system cards, the
generated Part VIII theorem/definition audit, the global named-theorem index,
the generated symbol registry/index data, citations, cross-references, source
and navigation prose, and the P8 rows in the new-content and apparatus
registers. I did not read another seat's transcript or conclusion. I made no
manuscript, specification, tool, test, or generated-file edit. I ran no test
suite and no TeX/PDF build. Consequently, compilation, hyperlink behavior in a
rendered PDF, page breaks, float placement, table overflow, glyph coverage, and
visual legibility remain separate unrun gates.

The named R2 repair seams are source-correct. Admission nevertheless remains
blocked by four concrete publication/source defects below. F1 and F3 are
independent of any render; F2 and F4 are shortfalls against explicit live P8
register language.

## Source/content blockers

### F1 — blocking — the symbol registry and all 632 registration destinations are not on the live book route

**Locations.** Part VIII explicitly sends readers to
`sec:p01-symbol-registry` and `tab:p01-precedence` at
`handbook/parts/p08/source-map.tex:88-92`. Those labels are defined only in
`handbook/parts/p01/symbol-registry.tex:2-4` and
`handbook/parts/p01/symbol-registry.tex:83-97`; that file also inputs the
generated registry rows. But the complete live Part I driver,
`handbook/parts/p01.tex:1-35`, contains only restoration inputs and never inputs
`parts/p01/symbol-registry`. Part XIV nevertheless prints the compact generated
symbol index at `handbook/parts/p14/master-tables.tex:219-231` and asserts that
it links back to the Chapter 1 registry at
`handbook/parts/p14/master-tables.tex:233-236`.

**Concrete failure path.** A reader following either Part VIII navigation link
lands on an undefined label. More broadly, the generated compact index contains
632 links to `entry:symbol-registry-*` destinations, while none of those
destinations is reachable from the live book graph. Static expansion of the
live route found exactly two unresolved Part VIII targets—the chapter and
precedence-table labels above—and found no live destination for any of the 632
generated symbol-index registration links. This is not a merely visual concern:
the target-defining source is absent from the input graph.

**Exact correction.** Route
`\input{parts/p01/symbol-registry}` exactly once at the intended Part I
location, so that the registry chapter, precedence table, generated registry
rows, and their 632 destinations are live. Then refresh generated surfaces if
the routing change requires it and run the separate reference/build/visual
gates.

**Status:** still-open source blocker.

### F2 — high — N-b-031 promises a lattice survey but supplies only a four-logic chain

**Locations.** The controlling P8 row
`spec/registers/new-content.csv:103` requires “the lattice of
superintuitionistic logics survey” in addition to KC and Gödel--Dummett LC.
The live chapter defines an intermediate logic at
`handbook/parts/p08/intuitionistic-supplement.tex:482-494`, gives the KC and LC
profiles and their strict inclusions at
`handbook/parts/p08/intuitionistic-supplement.tex:496-537`, and prints only the
two-row comparison and four-node chain at
`handbook/parts/p08/intuitionistic-supplement.tex:540-579`.

**Concrete failure path.** A reader sent to this material by the registered
deliverable learns the local chain
`IPC < KC < LC < CPC`, but is never told what the lattice order is, how meets
or joins are formed, or that the displayed chain is only a small suborder of
the superintuitionistic lattice. The filename/figure label containing
“lattice” cannot substitute for the promised survey. The current KC/LC claims
and countermodels are sound; the omission is the larger declared ceiling.

**Exact correction.** Add a source-cited compact survey that states the order
on intermediate logics, the lattice standing and its meet/join constructions
at the claimed level, and the fact that the current four-node diagram is only a
local subdiagram. Alternatively, an authorized register/admission decision
must narrow the declared deliverable; the present source does not silently
satisfy it.

**Status:** still-open source/content obligation.

### F3 — high — the Lewis triviality item is marked `cited` but carries a new complete proof

**Locations.** The status grammar says that `cited=<bibkey>` means “statement
only; source carries the proof” at `handbook/CONVENTIONS.md:60-66`, and places
new editorial proof-audit material in the annex at
`handbook/CONVENTIONS.md:68-72`. In contrast,
`handbook/parts/p08/conditionals-deontic-free.tex:437-453` marks
`thm:p08-lewis-triviality` as `cited=Lewis1976` and then gives the complete
four-atom mass argument at lines 445-450.

**Concrete failure path.** The generated theorem/definition audit necessarily
publishes the item as source-carried/cited even though the reader is given a
locally authored proof in the body. That is exactly the source-versus-editorial
standing contradiction prohibited by the charter. The bounded mathematical
claim itself is honest—it excludes a fixed event in one finite Boolean algebra
and explicitly lists its essential hypotheses at lines 450-452—so this finding
does not inflate it into a false theorem or claim that it is the full Lewis
triviality result.

**Exact correction.** Preserve the bounded theorem, move the local mass
argument to a reciprocal Part VIII annex item, and give the body theorem the
corresponding `proved=annex:<id>` standing while retaining `Lewis1976` as a
source/motivation citation. If the intended standing is genuinely `cited`,
remove the local proof and state the exact source-carried result instead.

**Status:** still-open proof-status/source-role blocker.

### F4 — medium — A-091 asks for quantifier rules for all three free-logical variants, but only the negative rules are printed

**Locations.** A-091 requires a comparison of positive, negative, and neutral
free logics “with existence predicate, quantifier rules, and
definite-description treatment” at `spec/registers/apparatus.csv:92`. The live
source gives exact negative semantics at
`handbook/parts/p08/conditionals-deontic-free.tex:7-27` and prints guarded
universal-instantiation/existential-generalization rules only for that negative
presentation at lines 29-32. The table at lines 51-78 gives semantic ranges and
description policies for all three variants, but its own qualification at
lines 80-84 says the displayed guarded rules belong to the negative
presentation and that positive and neutral calculi must match separate
clauses.

**Concrete failure path.** A reader can reconstruct the negative quantifier
policy but cannot recover the promised positive or neutral quantifier-rule
surface from the table. In particular, the positive row combines outer-domain
term values with inner-domain quantifier ranges without stating the exact
substitution/existence side condition, while the neutral row gives value
aggregation but no rule/consequence formulation. The source accurately admits
this boundary; the apparatus register still overstates what the table
contains.

**Exact correction.** Add source-specific quantifier-rule cells (including
exact existence/definedness side conditions and the neutral consequence
standing) for each variant, or narrow A-091 through the authorized register
process to a semantic comparison. Do not invent one family-wide calculus.

**Status:** still-open apparatus obligation.

## Focused repair verification

The following named seams are **accept-source-fixed**; none licenses a rendered
publication claim.

- **Lewis VC calculus and completeness.** The live sheet is CK plus ID, CA,
  CSO, CV, conditional MP, and CS, and explicitly states that CA replaces the
  non-equivalent MOD presentation at
  `handbook/registry/calculi/hilbert-counterfactual-vc.tex:1-11`. The theorem
  and system card consistently claim centered, limit-free sphere semantics at
  `handbook/parts/p08/conditionals-deontic-free.tex:322-364`.
- **Weak centering, centering, and the limit assumption.** The nested-sphere
  closure, union-domain truth clause, weak-centering clause, centering clause,
  and independent least-permitting-sphere condition are stated separately and
  consistently at
  `handbook/parts/p08/conditionals-deontic-free.tex:234-278`.
- **Dyadic conditional/deontic semantics.** The total-preorder orientation,
  smoothness over definable candidate sets, best-world operator, and explicit
  impossible-antecedent policy are all present at
  `handbook/parts/p08/conditionals-deontic-free.tex:139-180`.
- **Büchi example.** The automaton tuple, run indexing convention,
  `Inf`-acceptance condition, total two-state transition graph, and the exact
  `GF p` equivalence agree at
  `handbook/parts/p08/temporal-epistemic-supplement.tex:353-401`.
- **Epistemic/group repair.** The routed convention excludes the empty group
  at `handbook/parts/p08/group-operator-convention.tex:1-8`; distributed and
  common knowledge use the stated intersection/closure distinctions at
  `handbook/parts/p08/temporal-epistemic-supplement.tex:517-578`; and the
  epistemic figure caption accurately describes a synopsis whose complete
  fixed-point/induction surface remains on the linked sheet at
  `handbook/parts/p08/temporal-epistemic-supplement.tex:679-683`.
- **KC/LC hierarchy.** The WEM and prelinearity profiles, strict inclusion
  derivation/countermodels, table, and figure consistently establish only
  `IPC < KC < LC < CPC` at
  `handbook/parts/p08/intuitionistic-supplement.tex:496-579`. F2 concerns the
  additional promised lattice survey, not an error in this chain.
- **AGM.** The revision and contraction postulates, tautology exception,
  supplementary conjunctive postulates, Levi identity, Harper identity, and
  faithful-preorder boundary agree at
  `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:246-357`.
- **da Costa C1.** The consistency operator, exact fifteen-postulate sheet, and
  LP/C1 comparison agree at
  `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:72-133` and
  `handbook/registry/calculi/hilbert-da-costa-c1.tex:1-18`.
- **KLM.** Strict preference, smoothness over formula-definable sets, the seven
  System P rules, rational monotony as a separate extension, and the
  representation boundaries are coherent at
  `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:149-218`.
- **Affine logic.** The sheet is exactly commutative IMLL plus unrestricted
  antecedent weakening, retains multiset exchange, omits contraction, and
  makes no unproved adequacy or cut-elimination claim at
  `handbook/registry/calculi/affine-ill.tex:1-5`. The comparison text, table,
  structural-policy figure, and consequence table preserve that standing at
  `handbook/parts/p08/relevance-linear-supplement.tex:528-677`.
- **Modal proof reciprocity.** The annex contains a complete canonical strong
  completeness argument for K, KT, S4, and S5, including the existence lemma,
  truth lemma, frame-property steps, and local-consequence conclusion at
  `handbook/annex/p08/modal-completeness-supplement.tex:4-65`.
- **Many-valued proof reciprocity.** The finite-matrix specializations and the
  K3/LP/FDE decision and duality arguments have literal reciprocal annex
  destinations at `handbook/annex/p08/many-valued-supplement.tex:18-133`.

## Static route, apparatus, and source-role checks

- The live body driver routes the exact inherited spans and supplements once at
  `handbook/parts/p08.tex:1-74`; the annex routes its source-sketch map and two
  proof supplements once at `handbook/annex/p08.tex:1-10`. The older combined
  historical Part VIII files are not reachable and therefore do not create a
  second reader identity.
- The exact-source hash printed in the current source map is
  `0509750C13B88A4E18914BD52BDE171C725CBA14221CBFC2227D7693A2B421CC`,
  matching the current restored source file. Exact source order and separately
  authored editorial-role prose remain distinct.
- No reachable noncomment text exposes `OPEN`, `stub`, `owed`, a workflow/finalizer
  instruction, or an internal register-row identifier. Semantic uses such as an
  open branch or an open mathematical problem are not construction debt.
- The generated Part VIII audit at `handbook/generated/audit-p08.tex` has one
  caption/label and 166 unique linked entries, all with live Part VIII targets.
  Its 35 exact-source theorem/definition-class units are covered by 32
  source-entry anchors plus the three retained named theorem labels.
- The current generated named-theorem index has 474 unique rows and 474 live
  targets. Its only literal `@` belongs to the displayed title `K(@)` rather
  than leaking a makeindex sort key. The index is routed at
  `handbook/parts/p14/master-tables.tex:212`.
- The symbol CSV, generated registry table, and compact index agree on 632
  unique registrations and destinations. F1 is specifically the missing live
  input of those otherwise coherent generated destinations.
- The 48 Part VIII calculus-sheet labels resolve through 45 live sheet files;
  the shared t-norm sheet accounts for the multiple labels. Each sheet is
  routed from the Part XIV rule-sheet catalog.
- All 128 citation keys reached from the live Part VIII body, annex, and sheets
  resolve in the handbook bibliography. The annotated further-reading route
  covers all four lots and explicitly refuses authority transfer at
  `handbook/parts/p08/further-reading.tex:7-44`.

## Four-lot disposition

1. **Intuitionistic/intermediate lot:** checked. Negative translations,
   algebraic/topological semantics, realizability/existence boundaries, IQC,
   KC, LC, the strict chain, table, and figure are source-clean. **Not clean:**
   F2, the missing promised superintuitionistic-lattice survey.
2. **Modal lot:** checked clean at the source/content level. Syntax, frame
   clauses, correspondence, filtration/bisimulation, quantified modal/domain
   variation, non-normal boundaries, calculus identities, and reciprocal
   canonical proof routes were inspected. Rendered references and layout are
   not checked.
3. **Temporal/epistemic/conditional/deontic/free lot:** checked. Büchi,
   group/common-knowledge, conditional, dyadic, deontic, and VC repairs are
   source-clean. **Not clean:** F3's proof status and F4's incomplete A-091
   quantifier-rule apparatus.
4. **Many-valued/substructural/paraconsistent/nonmonotonic/apparatus lot:**
   checked clean on the substantive system-specific surfaces, including AGM,
   da Costa C1, KLM, affine logic, tables, figures, rule sheets, citations,
   generated Part VIII audit, named-theorem index, and further reading.
   **Not clean:** F1 makes the global symbol retrieval apparatus inaccessible.

## Verdict

Part VIII is not source/content-admissible in this frozen snapshot. The
corrected mathematical seams should remain accepted, but the live route and
declared publication contract still require F1-F4. No static statement in this
review is a substitute for the outstanding full-build, reference-log, PDF
visual, human, provenance, or user gates.
