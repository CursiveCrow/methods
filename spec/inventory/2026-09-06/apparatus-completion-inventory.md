# Apparatus completion inventory

Snapshot: 2026-09-07T09:46:55Z. **All 201 original apparatus rows have been investigated. No assigned row remains unaccounted for.** The [JSON inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/apparatus-completion-inventory.json) preserves each original ID, item and specification and records its required components, present/missing/conflicting evidence, current paths, concrete remainder, existing validation state, and reading intervals with SHA-256.

The result is **120 complete surfaces, 66 partial surfaces, 6 absent surfaces, 4 inactive-only surfaces, and 5 policy conflicts**. A complete surface means the specified apparatus components were found in the inspected source. It does not mean its mathematics, source fidelity, current compilation, visual output, or publication admission has passed. These counts do not measure whole-manuscript completion.

## Coverage by category

| Category | Rows | Complete surface | Partial surface | Absent | Inactive only | Policy conflict |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rule-sheet | 23 | 9 | 13 | 0 | 0 | 1 |
| table | 91 | 58 | 30 | 1 | 2 | 0 |
| figure | 40 | 36 | 1 | 1 | 2 | 0 |
| index | 6 | 1 | 5 | 0 | 0 | 0 |
| symbol-registry | 13 | 8 | 3 | 1 | 0 | 1 |
| environment | 7 | 3 | 3 | 0 | 0 | 1 |
| bibliography | 3 | 3 | 0 | 0 | 0 | 0 |
| navigation | 7 | 2 | 3 | 2 | 0 | 0 |
| check | 11 | 0 | 8 | 1 | 0 | 2 |
| **Total** | **201** | **120** | **66** | **6** | **4** | **5** |

The row-level reading coverage records 141 distinct files and 266 distinct line intervals. Source/implementation reading and CSV metadata aggregation are identified separately. All 23 original rule-sheet specifications were compared with their complete current sheet files. Tables and figures were read as definitions and constructions with the necessary surrounding text; caption or label presence alone was not counted as fulfillment.

## Resolution of the initial 11 mapping questions

| Row | Current disposition |
| --- | --- |
| A-027 | All requested equivalence laws occur in the inactive P2 historical table. The active NNF proof uses only some rewrites and does not supply that table. |
| A-029 | The five maximal-clone tests and Post criterion are in the inactive historical P2 file. |
| A-032 | The active controlled-English guide covers only-if and unless, but lacks neither-nor. |
| A-114 | The worked syntax tree exists only in the inactive historical P2 file. |
| A-115 | Resolved positively to the active P7 composition derivation: a complete ND tree with three explicit discharges, beside its STLC instance. |
| A-116 | Resolved positively to the active P2 nested cut-free sequent derivation in inherited-02341-02450.tex:101–109. |
| A-119 | The inactive Post diagram shows only the upper cover and explicitly omits the lower lattice. |
| A-150 | The active Stone body gives a finite example in prose but has no requested finite algebra/space picture. |
| A-156 | Eight active synonym see entries exist; no see-also layer was located. |
| A-172 | The first-order bracket notation is defined at inherited-03429-03518.tex:55–68; the superscript form occurs at inherited-06070-06137.tex:45–60. Their requested registered bridge is absent. |
| A-199 | A latexmk instruction and historical build records exist; the specified warnings-as-errors implementation and current pass are not established. |

## Main apparatus still to supply or reconcile

Several substantial rule sheets omit a specifically requested on-sheet theorem, caveat, definition or reference. The JSON identifies each one, including the Hilbert deduction-theorem statements, common-knowledge completeness caveat, and matrix-tableau saturation definition. Uniform substitution for K is credited through the actual axiom-schema closure and derivation rules; it does not require an additional primitive rule merely to satisfy the inventory.

The larger missing subject surfaces are concrete:

- A-018 lacks the concretely fixed ordering/eligibility/redundancy package requested for superposition. A-019 supplies IMLL, its four-rule bang extension and CLL, while explicitly declining to call the middle sheet full ILL.
- A-052 deliberately leaves the exact FO capture theorem unstated. A-073 leaves CIC comparison cells empty, and A-074 expressly omits the lower Q-range ordinal-analysis endpoint.
- A-051 omits several displayed logic families and has no card-harvesting provenance. A-069 is an authored strength map with necessary distinctions among comparison relations; its original harvesting requirement is unfulfilled. A-077 has a real active axiom/frame/algebra companion at master-tables.tex:143–166, resolving the earlier apparent absence of algebraic conditions; row-level Sahlqvist coverage and harvesting remain to be supplied.
- A-063 has not incorporated the new Part X DC/BPIT uses. A-092 lacks an ASP row in its nonmonotonic comparison.
- A-095 explicitly lacks the SHOIQ/SROIQ endpoints and identifies the exact-source and encoding issues still to resolve.
- A-098 has no current Boolean-law/ring comparison; A-099 has no Stone dictionary or ideal/open correspondence; A-100 has no aggregate logic/algebra table. These absences coexist with the substantial new Part X proofs.
- A-101's paradox table omits Russell, sorites and Skolem. A-102 and A-104 have relevant prose or family capsules, without the requested comparison tables. A-112 often names broad expressiveness boundaries rather than explicit separating witnesses.
- A-201's current table concerns broad changes of method, rather than the specified Peano–Russell, Polish, Gentzen and Hilbert notation lineages with periods and glyphs.

Source details requiring correction or clarification include the unqualified positive-arity NAND/NOR completeness note and inactive Post destination (A-024), omitted P2.3 type scope in the letter-family summary (A-026), a literal double-backslash before a closing set brace in the ACA0 table row (A-056), the CTL root's unstated p-value while AF p is asserted false (A-146), and the registry's positive-only description of Diag against the body's atomic-and-negated-atomic definition (A-162). These are source observations; no repairs were made.

## Generated apparatus and navigation

**Exactly six generated audit tables are active**, although all 14 files exist:

| Part | Actual input |
| --- | --- |
| V | handbook/parts/p05.tex:51 |
| VI | handbook/parts/p06.tex:152 |
| VII | handbook/parts/p07.tex:128 |
| VIII | handbook/parts/p08.tex:68 |
| IX | handbook/parts/p09/logic-in-computer-science.tex:2459 |
| X | handbook/parts/p10/algebraic-and-categorical-logic.tex:287 |

P1–P4 and P11–P14 have generated files but no active audit-table input. The earlier intermediate four-route count missed the two chapter-host inputs and is withdrawn. The maintained generator follows the reader graph for theorem/definition rows; its main function deliberately withholds system-card projection pending a packet-admission input. No current freshness run was executed or inferred from timestamps.

The symbol registry has **854 rows**, and every registry-line anchor is present in both generated symbol outputs. Registration-page links exist. First-use fields remain bare part/chapter locators, and principal-use fields are notes rather than an occurrence/page index. Anchor coverage is not full field-value or rendered-page validation.

The subject-index target has a source-side size shortfall. Its 953 explicit commands yield at most 1,175 heading/prefix entries; all 1,103 automatically indexable environments yield at most another 1,103. Even that deliberately generous bound is **2,278**, below the required minimum 2,500. It overcounts duplicate and untitled entries, and is not a rendered index count. Only 78 of the 953 explicit commands contain an explicit @ sort key. The saved main.ind/main.idx are from August 14.

The generated named-theorem index contains the Lindenbaum and both truth lemmas, but its collector skips some unlabelled source results outside specially hooked families. The active P2 NNF and functionally-complete-basis theorems provide concrete omissions. Source proof-detail cells also differ from separately anchored annex-proof destinations.

There are **36 glossary entries** and **40 biographical capsules matching the 40 explicit person-index entries located**. Many glossary entries lack their defining-entry links, and substantial terminology is absent. Individual biographical dates were not fact-checked in this inventory.

Exercise feedback has **112 unique exercise backlinks and five problem backlinks**, distributed across 111 manual solution/sketch headers because some answers share a heading. It has only the two chapter labels, with no per-solution anchors for forward links. That establishes the missing direction without miscounting shared answers as missing exercises.

The current installed book class sets tocdepth=2 and puts subsections at level 2. Together with numbered sheet-group sections and the sheet labels/counters, this resolves A-183's source-level navigation requirements. A fresh render is still needed. Lists of tables, figures and listings have no active invocation. Part-specific further-reading sections are missing in P1, P10, P11 and P13; the historical P1 reading file is inactive.

## Validation and policy boundaries

The maintained checker implements substantial editorial label/status, reference, reciprocal-annex, registry-collision and bibliography-key checks. It does not supply the requested body-glyph coverage, complete index-heading/sort hygiene, unused-bibliography/DOI consistency, or unreferenced-label/prose-pointer scans. Its chapter-citation check is file-based rather than a reconstruction of every reader chapter. The JSON identifies these precise implementation limits instead of calling every gate merely unverified.

All **201 formal apparatus closure rows are OPEN**; their manifest bindings are open and all six verification fields are pending. Each inventory row carries its exact closure-record hash and source line. The closure CSV SHA-256 is:

`92e43694db98276a1a84d70f4c5636f1394a277a19591a19a96eb49e6792d1c0`.

The reviewed-register store has zero records and zero formal contract supersessions. Its SHA-256 is:

`fc7de3b183ffd25ed16cf7b1b89ace014f69d7c1442f2f0a542ae8c3378da703`.

The terminal manifest still names the August 18, 836-page PDF with SHA-256 `ee4c5324c1aac7fc3b0e13fba816b35ec6f39be059e807b01695fe1a9900851f`. It does not certify the September source snapshot. Historical done/open strings are retained in every row and are not promoted to current validation.

The five policy conflicts are A-001, A-168, A-177, A-190 and A-192: repetition/vacuous discharge versus R-013; universal equivalence-symbol wording versus declared source-local roles; and universal registry/status bans versus authorized source presentations. Recording these conflicts does not silently amend the register or authorize a manuscript change.

Only the two assigned apparatus inventory files were authored. No manuscript/source/registry/bibliography edits, tests, maintained validator runs, builds, renders, manuscript generator runs, acquisitions, commits or new agents were performed. The installed-class lookup and metadata aggregations were read-only. This completes the assigned apparatus inventory, with content and validation remainders explicit for every row.
