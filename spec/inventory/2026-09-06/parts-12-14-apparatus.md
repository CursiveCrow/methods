# Current inventory: Parts XII–XIV and apparatus

Snapshot date: 2026-09-06, inspected on 2026-09-07 UTC. This is a read-only inventory of the saved LaTeX and its supporting artifacts. Only this report and its companion JSON were written. No manuscript, source, bibliography, registry, review, or publication file was changed; no tests, builds, renders, new acquisitions, or multi-GB coverage scans were performed.

The exhaustive row ledger is [parts-12-14-apparatus-requirements.json](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/parts-12-14-apparatus-requirements.json). It contains **223 distinct requirement records**:

| Register | Assigned rows | Coverage |
| --- | ---: | --- |
| new-content.csv | 10 | N-c-031 through N-c-040, all target P12 |
| depth-gaps.csv | 12 | D-P11-001–005 and D-P11-009–015: 11 target P12, one target P14 |
| apparatus.csv | 201 | Every row A-001 through A-201 |

There are **no new-content rows targeting P13 or P14**, no depth rows targeting P13, and **no original domain-x new-content rows targeting P12–P14**. This absence of register rows does not establish that those parts are complete. The original domain and historical treatment/status fields are retained where supplied; old E/T/S/P treatments and historical `open`/`done` values are not treated as final acceptance or as current writing ceilings.

## What the states mean

Each JSON row includes its register, ID, target part or `cross_book`, exact item, actual file/line/label evidence, content state, proof state, concrete remaining work, completion flag, and historical status where present. Apparatus rows remain `cross_book` because that register has no structured target-part field, even when their actual artifacts are located in a particular part.

**Located does not mean complete.** `substantive_present` records an actual relevant artifact or passage. When an apparatus table, figure, sheet, index, generator, or check implementation was located but its complete specification was not validated, its proof/validation standing remains `unverified` and `completion_verified` is false. Candidate artifacts in historical files outside the current literal input graph are identified as `mapping_unverified`; they are not counted as active content. `not_located` is used only for the two list surfaces whose commands/surfaces were not found in the inspected active architecture. It does not mean every possible alternative construction was mathematically disproved.

The ledger has 166 `substantive_present`, 42 `mixed`, 11 `mapping_unverified`, two `summary_only`, and two `not_located` records. **These counts are not a completion percentage.** No row is promoted to fully verified completion in this bounded mapping pass: it did not exhaustively validate every source, proof, artifact criterion, and reader-facing behavior. Many substantial artifacts are present, and their presence is recorded rather than described as missing.

Evidence collection followed literal `input` and `showcalculus` links from the live driver and inspected the relevant active passages. It is a source-reading aid, not a TeX expansion/build or a replacement for root's authoritative route/citation/index diagnostics. Captions and labels establish candidate artifact presence; they do not by themselves establish fulfillment of every requirement field.

## Part XII: substantial active content with specific proof and presentation gaps

The live [Part XII driver](C:/Dev/the-methods-of-reason/handbook/parts/p12.tex:1) routes the restored formal-practice, automated-reasoning, mechanized-proof, writing/typesetting, research-workflow, notation, rule-sheet, assessment, and exercise-feedback source sequences. Its local [aggregator](C:/Dev/the-methods-of-reason/handbook/parts/p12/automation-and-mechanization.tex:4) additionally routes SAT/certificates, SMT/exchange formats, first-order automation, rewriting, interactive proof, and further reading. The routed formal-practice supplement contains worked and methodological material, explicitly distinguished from inherited source and release acceptance.

The active annex driver routes `annex/p12/sat-and-certificates.tex`. The DPLL theorem names its local annex proof. The CDCL and Newman discussions contain inline arguments; many other named results remain explicitly cited. This inventory records those standings without treating every citation as an authoring defect.

| New-content row | Current substantive evidence | Specific remainder or verification limit |
| --- | --- | --- |
| N-c-031 | PTS specification, eight lambda-cube vertices, universes/inductives/W-types, and CIC/pCIC boundaries in `interactive-proof.tex:128–230` | Validate the full cross-part calculus and version-specific foundation claims; the text correctly distinguishes CIC from Lean's exact kernel. |
| N-c-032 | CDCL/UIP/watch/restart/DRAT vocabulary, conflict graph, transitions and invariant discussion in `sat-and-certificates.tex:202–378` | Watched-literal maintenance and VSIDS details remain brief; no complete end-to-end certificate-correctness validation was established. |
| N-c-033 | P2 Horn/2-SAT cross-references and a defined random-k-SAT distribution/phase-transition pointer at `sat-and-certificates.tex:108–118` | Current P2 algorithm/theorem and source validation remain separate; no chapter is missing merely because the canonical treatment is cross-part. |
| N-c-034 | EUF definition, purification/convexity/stable infiniteness, theory table and DPLL(T) transitions | **The requested Nelson–Oppen proof is absent from the local account:** `smt-and-exchange-formats.tex:100–111` is a cited theorem. Congruence closure and simplex are described, without a full algorithmic construction/proof in the inspected text. |
| N-c-035 | Actual MM sheet, transformation invariant, claimed termination measure, cited MGU theorem in `first-order-automation.tex:186–222` | **A full rule-by-rule termination and MGU-factorization proof remains owed by the row's explicit proof request.** AC/equational variants are only brief boundary prose. |
| N-c-036 | Ordered-superposition sheet, ordering/eligibility/redundancy and fair-saturation vocabulary | The requested model-construction completeness sketch is compressed to a sentence at `first-order-automation.tex:239–247`; concrete ordering details also need validation. |
| N-c-037 | Rewriting definitions, local Newman argument, critical-pair and conditional completion statements, example and rule sheet | Critical-pair/completion results are cited; LPO/KBO descriptions lack full formal definitions. A worked word-problem application and complete proof scope remain to be established. |
| N-c-038 | Checking layers, LCF, reflection, versioned assistant/trust table | Substantial architecture account exists; current source accuracy and result-specific trusted-base claims were not fully validated here. |
| N-c-039 | Coq-style extraction/erasure and a conditional simulation requirement at `interactive-proof.tex:380–399` | The specifically requested **realizability-based extraction explanation** is not developed in that erasure account. |
| N-c-040 | Four-stage hammer/reconstruction pipeline at `interactive-proof.tex:401–420` | The requested pointer is present; source and exact trust-path validation remain unverified, not additional implementation work inferred from the row. |

The eleven P12 depth rows are all separately represented in JSON. D-P11-001/002/003/005/012/014 overlap the corresponding new-content items; they are not dropped or merged away. D-P11-004 has refinement definitions and a taxonomy; D-P11-009 has ROBDD/counting/MaxSAT material and QBF links; D-P11-011 lists the requested assistant families including Metamath; D-P11-013 has an explicit HoTT/univalence pointer; D-P11-015 has all five named landmark formalizations with scope/trust boundaries. Their complete source/proof/content requirements have not all been revalidated.

### Definite stale Part XII navigation

[further-reading.tex:29](C:/Dev/the-methods-of-reason/handbook/parts/p12/further-reading.tex:29) says its status table lists every P12 status-bearing result exactly once. The table at lines 40–59 lists eight results, while the current chapter files also contain the CDCL invariant, DPLL(T) correctness, unification MGU, superposition completeness, and three rewriting theorems. Those seven are not represented in that table. The same file's canonical-routes table still describes the MM obligation as deferred. These are stale navigation assertions, separate from the newer substantive content.

[parts/p12.tex:47](C:/Dev/the-methods-of-reason/handbook/parts/p12.tex:47) explicitly leaves `generated/audit-p12.tex` unrouted because the generator scans historical files rather than the reachable reader graph. [audit_tables.py:6](C:/Dev/the-methods-of-reason/tools/audit_tables.py:6) confirms the broad `parts/**/*.tex` scan. Existing generated files are therefore present but not proof of current audit freshness.

## Part XIII: selected chronology and capsules are present; one explicit apparatus mismatch

[parts/p13.tex](C:/Dev/the-methods-of-reason/handbook/parts/p13.tex:1) routes the actual chronology-and-biography chapter. It contains a selected chronology from ancient logic through the 2013–2021 formalization/Lean entry, named biographical capsules with source groupings and person-index tags, and a notation/method-transition table. This is substantive current writing. The current pass did not independently validate every date, biographical claim, cited primary, or person-index correspondence.

Apparatus A-109 and A-111 have definite artifacts at `chronology-and-biography.tex:10` and `:91`. A-110's dedicated landmark-papers register with full citations/significance fields was not located; the chronology supplies related paper references but is not automatically that artifact.

**A-201 has a definite content mismatch.** The table at [chronology-and-biography.tex:313](C:/Dev/the-methods-of-reason/handbook/parts/p13/chronology-and-biography.tex:313) compares broad changes in inference, computation, semantics and mechanization. The row instead asks for Peano–Russell dots, Polish notation, Gentzen sequents and the Hilbert school, with periods, exemplar glyphs and modern descendants. Those rows and fields are not supplied by the active table. The JSON records `summary_only` and the exact missing content rather than calling the whole part empty.

## Part XIV: active retrieval apparatus, not verified global completion

The driver routes [rule-sheets.tex](C:/Dev/the-methods-of-reason/handbook/parts/p14/rule-sheets.tex:1) and [master-tables.tex](C:/Dev/the-methods-of-reason/handbook/parts/p14/master-tables.tex:1). The rule catalog inputs actual registry sheets across classical, algebraic/categorical, modal, temporal, program, many-valued, relevance, linear and Lambek families. The master file contains a substantial complexity table, a strength-surface cross-reference, an expressive-power table, modal correspondence table, selected glossary, generated named-theorem and symbol-index inputs, unified-index policy, and a further-reading map.

The sole P14 depth row, **D-P11-010**, is recorded as mixed: a live decision-problem table exists at `master-tables.tex:12`, but it is manually authored and this pass did not establish coverage of every presented logic or entry-card harvesting. Explicit T/IPL rows are not in the inspected table. Whole-table accuracy and all decision-polarity qualifications remain to be checked.

The glossary at `master-tables.tex:168` is a selected alphabetical list; it does not cover all current registered terms and many entries lack defining-entry links. The named-theorem and symbol-index artifacts exist and are actively input at lines 258 and 275. Their freshness and exhaustive correspondence to today's statements/registry were not validated. The person and subject indexes intentionally share the backmatter index rather than appearing as separate printed books.

## All apparatus categories

The JSON enumerates every A-001–A-201 independently, with its exact spec and evidence. The following summarizes the category-level findings and limits.

| Category | Rows | Current presence and remaining limits |
| --- | ---: | --- |
| Rule sheets | 23 | Relevant registry sheets are present and routed. Headers/source boundaries were inspected; full side-condition/theorem correspondence for all sheets was not revalidated. A-001 and A-019 have explicit scope conflicts/partial coverage noted below. |
| Tables | 91 | Most rows have located active tables with caption/label evidence. Several original P2 candidates occur only in unrouted historical files and require active mapping. P10/P11 requested comparison tables were not all located despite substantive prose. A-110, A-113 and A-201 have specific gaps. |
| Figures | 40 | Most requested diagram families have active caption/label evidence. The original syntax/ND/LK/Post figures include candidates in historical files outside the inventoried route; active equivalents need mapping. A-150's finite Stone-duality picture was not located in the routed caption inventory. Full diagram correctness/rendering was not tested. |
| Indexes | 6 | Main `printindex`, generated symbol/named-theorem files, and the person-index policy exist. Exhaustive entry coverage, sort-key behavior, see/see-also coverage and source-preserved indexing remain unverified. |
| Symbol registry | 13 | `handbook/registry/symbols.csv`, generators and printed views exist. Full glyph/role/precedence/first-use validation was not performed. Several historical global-normalization requirements need reconciliation with current source-scoped notation policy. |
| Environments | 7 | Style definitions for mandatory editorial status, warnings, conventions, proof boundaries, rules and guarded source solutions exist. Full current usage and error behavior were not checked; the audit generator has a documented route/freshness issue. |
| Bibliography | 3 | Biblatex and inherited/editorial database separation are active; the five requested primary keys exist. Full source identity, field normalization, intake completeness and point-of-use citation coverage remain unverified. |
| Navigation | 7 | Numbered rule-sheet sections, reading maps, glossary, index and exercise/feedback routes exist. **A-184/A-185 list-of-tables/figures/listings surfaces were not located** in the current source search. Full bidirectional navigation was not tested. |
| Checks | 11 | Maintained static-check implementations and historical verification records exist. No current check was run. Their existence and historical `done` statuses do not establish today's gate results; audit freshness is explicitly open. |

### Historical apparatus wording that conflicts with current source policy

- **A-001** requires repetition and vacuous discharge, while [nd-cpl.tex:5](C:/Dev/the-methods-of-reason/handbook/registry/calculi/nd-cpl.tex:5) explicitly excludes both under R-013. Reconcile the row with the controlling corrected calculus; do not insert forbidden rules simply to satisfy old wording.
- **A-019** asks for IMLL/ILL/CLL. The IMLL and one-sided CLL sheets exist, but [ill-exponential-extension.tex:2](C:/Dev/the-methods-of-reason/handbook/registry/calculi/ill-exponential-extension.tex:2) explicitly says it is only the four-rule bang extension, not full ILL. A full ILL surface or a revised requirement disposition remains necessary.
- **A-177/A-192** demand a blanket registry-only rule policy. Current [frontmatter.tex:98](C:/Dev/the-methods-of-reason/handbook/frontmatter.tex:98) and the P14 catalog expressly retain inherited source displays. The maintained checker documents provenance-backed source exceptions. Literal old-row compliance should not be inferred, and source displays should not be rewritten merely to meet the superseded blanket wording.
- **A-167–A-171** express global collision/normalization decisions. The current frontmatter instead preserves each attributed presentation's notation scope. These rows need a current scoped disposition, not automatic acceptance from historical `done (6348bdc)` fields.

## Supporting records and limits of this inventory

The [historical terminal-readiness manifest](C:/Dev/the-methods-of-reason/spec/verification/terminal-readiness-manifest.json:1) records an 836-page PDF and a particular source snapshot. It is a real artifact, not missing evidence, but it is not a completion certificate for the present text. The active formal-practice supplement contains explicit methods and release-gate tables distinguishing source review, mathematical review, kernel/certificate checks, build, visual and human review. These methods are present; this inventory did not execute those gates or verify per-result records globally.

Root separately handles the complete source inventory, defects register, and quantitative route/citation/index diagnostics. This report contributes the exhaustive assigned-row mapping and concrete current writing/apparatus gaps. It should be combined with those other inventories before making a whole-manuscript completion claim. No defensible global completion percentage follows from these row counts.
