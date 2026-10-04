# The Methods of Reason: current manuscript inventory

Inventory date: 7 September 2026. Authoritative manuscript folder: `C:/Dev/the-methods-of-reason`.

**The current-state inventory is complete.** Every original requirement, all fourteen parts, inherited content, apparatus, current source holdings, bibliography entries and recorded review/publication standing have an explicit inventory disposition. The independent audit closed both final reconciliation conditions and found no additional unassigned manuscript-reading task.

**The manuscript remains a substantial, unevenly developed, unfinished draft.** All fourteen parts contain active writing; Parts IX and X contain extensive technical developments. The inventory also identifies missing developments, incomplete proofs, exact-source gaps, apparatus omissions and two confirmed mathematical defects. A complete inventory does not mean the book is complete or its proofs have all been accepted.

Manuscript authoring remains stopped. The inventory was conducted through the actual LaTeX, its active input route and existing evidence. Audit changes are confined to this directory. The final [snapshot comparison](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/snapshot-comparison.json) confirms that all 951 protected manuscript, bibliography, register, governing, archival and publication files are unchanged, with no additions or removals.

## The current records

The [current requirement ledger](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/complete-requirement-ledger.md) is the authoritative assessment of all 615 original rows. Its [JSON](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/complete-requirement-ledger.json) preserves every original register field and identifies each effective assessment under `current_assessment`; its [CSV](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/complete-requirement-ledger.csv) exposes the same current view. `initial_assessment` is explicitly historical. The first report is retained as [INITIAL-MANUSCRIPT-INVENTORY.md](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/INITIAL-MANUSCRIPT-INVENTORY.md), not current authority.

The former queues of eleven apparatus mappings, 28 defect mappings, four other content mappings, sampled Part IX text and incomplete source identities have been investigated. Their resolved assessments and remaining book obligations appear in the current records. Missing book work is not an unassigned inventory task.

There is **no defensible single percentage for manuscript completion**. The original requirements overlap and vary greatly in size; they also do not exhaust inherited content and separate source-presentation obligations. A present statement, a supplied proof, a complete source presentation, current independent review and publication acceptance are different accomplishments.

## What exists

The source census follows literal `input`/`include` edges and the known calculus macro from the current driver. It does not execute arbitrary TeX.

| Measure | Current inventory |
| --- | ---: |
| Active parts | 14 |
| LaTeX files under `handbook/` | 937 |
| Unique LaTeX files reached by the current driver | 840 |
| LaTeX files outside that route | 97 |
| Active source lines, including drivers and generated material | 92,889 |
| Structured theorem/lemma/corollary declarations | 396 |
| Their declared status: proved / sketched / cited | 136 / 4 / 256 |
| Additional inherited theorem/lemma/corollary environments | 185 |
| Definition environments | 582 |
| Explicit proof environments / proof-plan environments | 264 / 15 |
| Annex items | 152 |
| Calculus sheets / rule rows | 84 / 566 |
| Symbol-registry rows | 854 |
| Bibliography entries / keys cited through inspected mechanisms | 630 / 615 |
| Missing literal input files / unresolved proof-status targets | 0 / 0 |
| Unresolved literal reference targets | 7 |

These are source counts and recorded declarations, not new mathematical acceptances. Inline proofs are not all enclosed in proof environments. In particular, Part IX contains much more proof prose than its three explicit proof environments suggest. The [source census](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/inventory-summary.json), [active file inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/latex-files.csv), [input edges](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/input-edges.csv), [environment inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/mathematical-environments.csv) and [per-part census](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/per-part-census.csv) preserve the detailed counts.

## Every original requirement

All **615 original rows** occur exactly once, with original fields preserved: **185 new-content, 141 depth-gap, 88 historical-defect and 201 apparatus requirements**. All fifteen domain-x rows remain represented. Historical exclusions and E/T/S/P treatment ceilings are not used to declare the later full-compendium scope finished.

All 201 apparatus requirements now have component assessments: **120 have complete source surfaces, 66 are partial, six are absent, four exist only in inactive material, and five conflict with later policy**. A complete source surface does not imply that its independent review or output gate has passed. All 201 formal apparatus closure records remain OPEN. See the [apparatus assessment](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/apparatus-completion-inventory.md).

All 88 historical defect rows have component dispositions: **38 exact recorded repairs present, 15 partial repairs, eight absent or confirmed remaining components, 20 policy conflicts, and seven output-dependent or mixed cases**. These classify the recorded repair specifications; they are not a count of every error in the book. Evidence is divided between the [30-row mapping assessment](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/defect-mapping-completion.md) and [58-row component assessment](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/remaining-defect-components.md).

The [four previously unresolved content mappings](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/remaining-content-mappings.md) are settled as follows:

- **N-x-014:** related randomness and left-c.e. material is present; the requested TTE, represented-space and Weihrauch development is absent from the active body.
- **D-P10-019:** the requested Markov-principle statement and status are supplied through the active P8-to-P7 route, including cited realizability and nonderivability. The requirement does not call for an HA proof of Markov's principle.
- **D-P2-007:** the Tseitin discussion, root clause and conjunction example are active in P12; the requested P2 forward reference is absent, and the former general theorem is inactive.
- **D-P2-010:** an active congruence exercise and solution sketch exist; the promoted uniform-substitution and replacement theorems are inactive. Other substitution results do not automatically satisfy this requirement.

## State of all fourteen parts

Body counts exclude generated material; annex counts are separate. Shared calculus and lookup files are recorded in the census rather than treated as new chapter prose. These figures indicate volume, not a completion denominator. The current ledger contains the individual requirement evidence behind the remaining-work descriptions.

| Part | Body / annex lines | Current content and principal remaining work |
| --- | ---: | --- |
| I | 1,716 / 0 | Foundations are present. Source, notation, navigation and admission obligations remain in the apparatus assessment. |
| II | 7,651 / 360 | Substantial propositional, first-order and higher-order material. Active Post treatment, the P2 Tseitin pointer, promoted substitution results and the complete expanded-signature PA2 definition remain missing or inactive; several adequacy developments remain incomplete. |
| III | 3,370 / 596 | Substantial model-theoretic content. Several classification arguments remain outlines or citations; the requested active four-case DLO argument is absent. |
| IV | 3,582 / 251 | Computability and coding material is present. The full arithmetic computation-verification transcription is omitted; MRDP machinery and TTE/Weihrauch development remain incomplete or absent. |
| V | 2,244 / 237 | Incompleteness and related material is present. Solovay, Goodstein/hydra developments and the identified G-SR source pointer need further work. |
| VI | 4,895 / 420 | Extensive set-theoretic statements and some proofs. Advanced PCF, proper forcing, PFA/MM, fine structure and core-model developments remain uneven or cited. |
| VII | 3,947 / 1,234 | Proof-theoretic developments and local proofs are present. Full arithmetic Gentzen arguments, normalization/interpretation developments, HoTT/HIT/cubical and proof-net/GoI material remain incomplete; the analytic-derivation definition is inactive and equality-inclusive translation remains a sketch. |
| VIII | 6,252 / 265 | Many logic presentations and system entries. Modal/relevance and many-valued developments retain proof or cross-part obligations; the CTL illustration needs an explicit root valuation. |
| IX | 32,823 / 894 | The largest technical development. All active files were read in full. Two mathematical defects, missing SHOIQ/expressive-description-logic coverage, exact-source/version gaps and unexpanded original constructions remain. |
| X | 4,927 / 6,646 | Substantial algebraic/categorical work, including 80 explicit proof environments. HSP remains cited; locales, topological S4, MV/BL/MTL, residuated/cylindric/relation algebra, AAL and full internal-HOL/Kripke-Joyal/Tierney developments remain incomplete in scope. |
| XI | 247 / 7 | The chapter itself is 244 lines. Truth families and philosophical arguments are brief and do not yet supply the requested formal systems and full comparative development. |
| XII | 4,760 / 41 | Methods and algorithms are present. Nelson-Oppen and Martelli-Montanari proof/extraction requirements remain incomplete; overview tables need reconciliation. |
| XIII | 335 / 0 | Historical material exists. Notation lineage, the landmark register and historical source verification remain incomplete. |
| XIV | 436 / 0 | Lookup and apparatus material exists, with shared generated content elsewhere. Glossary, index, lists, comparisons and checker coverage remain below requirements. |

The initial part assessments remain useful evidence through the current ledger. Their superseded unknowns must be read with the later component and full-text assessments.

## Full Part IX reading and confirmed findings

The active Part IX file set exactly matches **36 completely read files totaling 33,808 lines**. The [reading coverage record](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/full-text-reading-coverage.json) gives hashes and sequential intervals. The detailed assessments cover [N-c-018](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/p09-n-c-018-full-text-inventory.md), [N-c-017](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/p09-n-c-017-full-text-inventory.md), [N-c-012](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/p09-n-c-012-full-text-inventory.md), [N-c-014/016](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/p09-n-c-014-016-full-text-inventory.md), [N-c-009/010/013](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/p09-n-c-009-010-013-full-text-inventory.md), [the other twenty presentations](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/p09-remaining-presentations-full-text-inventory.md), and [host, annex and drivers](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/p09-host-annex-full-text-inventory.md).

Two newly confirmed mathematical defects are recorded with explicit counterexamples in [current content findings](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/additional-current-content-findings.md):

- **INV-ELPP-001 / N-c-010:** the printed EL++ completion criterion misses an inconsistency caused by two reachable concepts sharing a nominal. A seven-GCI counterexample makes A empty in every model, while the printed closure neither derives bottom for A nor returns the required subsumption. The related quotient-agreement claim also fails. This requires correction in the manuscript; a possible query normalization has not been implemented or verified.
- **INV-CSL-001 / N-x-015:** the claim that closing any time interval preserves a CSL path probability is false at time zero. In a one-state absorbing model with p true, `(not top) U^(0,1] p` has probability zero and `(not top) U^[0,1] p` has probability one. The defect is in the current manuscript claim; the inventory does not attribute it to the cited paper.

**INV-CTL-001 / A-146** is a separate underspecified illustration: the claimed false AFp outcome requires p to be false at the unlabelled root. It is not counted as another confirmed false mathematical theorem.

The reading also credits completed corrections and real proofs. The corrected Rabin no-run boundary, Thomas empty-chain/sink treatment, ordinary-F witness, R-generability, MPL translation and typed factorization are present. N-c-018 supplies a larger bound but does not establish the separately required original `2^m` bound; Walukiewicz's full weak-completeness result remains a cited deductive bridge. N-c-012 retains construction roadmaps and condensed proofs. Its explicitly refuted, unused historical Pnueli formula is not classified as an adopted book error merely because the history displays it.

The generated P9 audit table has stale source mappings for several current developments, including finite Craig/Beth, Hanf, CTL*, CSL and PDL. The full-reading records identify the actual current sources and scopes.

## Inherited content, exercises and apparatus

All **1,055 inherited structural units** map to active text. Of **282 physical fragments**, 263 are active and unchanged, six are active and changed, and thirteen are inactive preamble/control/bibliography/index artifacts. All six changed active fragments were read in full and compared with the frozen source; they concern empty-base/Def and L1 reasoning, conjunction/index handling, Craig/Beth proof links, nonempty groups and the empty tensor. Their old provenance hashes are stale. These corrections must not be overwritten merely to restore old hashes.

All seventeen non-body map rows are separately accounted for. All 64 inherited bibliography keys remain: 62 have unchanged field sets and two have added fields beyond the prior reviewed sets. See [inherited content assessment](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/inherited-content-current-assessment.md), [exact differences](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/inherited-current-differences.md), and [preamble/control inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/inherited-preamble-layout-inventory.md).

The [feedback inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/exercise-feedback-current-inventory.json) records **111 headings**, comprising 89 declared solutions and 22 sketches, with **117 distinct active backlinks**: 112 exercises and five problems. Shared headings explain why heading and target counts differ. Individual solution anchors for forward links remain missing.

Important apparatus results include:

- Six generated audit tables are active, for P5-P10; eight others are inactive.
- All 854 symbol anchors occur in the two generated symbol views.
- The glossary has 36 entries. Forty biographies and forty explicit person-index entries exist.
- A generous source-based upper bound for the index is **2,278 headings/prefixes**, below the specified 2,500: at most 1,175 from explicit commands plus 1,103 eligible auto-indexed environments.
- Lists of tables, figures and listings are absent. Several required comparison tables are absent or partial, including Boolean-ring, Stone dictionary, aggregate logic/algebra, truth/philosophy and expressive description-logic comparisons.
- Existing checks do not cover every required body-glyph, index-sort, uncited bibliography/DOI, unreferenced-label and prose-pointer condition. Existing old notation/rule policies also conflict with later source-preservation and direct-correction policy.

## Bibliography and actual source holdings

The [complete source reconciliation](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/bibliography-source-reconciliation.md) accounts for **all 630 unique bibliography keys**, their original fields, current uses, local manifestations, exact version/extent, reading/review evidence and remaining obligations. There is no remaining source-identity queue within the inventoried scope.

| Current source standing | Keys |
| --- | ---: |
| Selected source body identified | 58 |
| Work body held in a different version | 19 |
| Partial target evidence | 14 |
| Related source held; exact target not established | 3 |
| Records or references only; no target body identified | 456 |
| No local body or matching source record identified within scope | 80 |
| Total | 630 |

These are key-level source findings. They do not assert that unavailable bodies do not exist online. Eighty-one keys have explicit scoped reading/review records, including acquisition boundaries; that is not 81 whole works read or accepted. Fifteen keys have no counted use through inspected citation mechanisms and were individually searched in active text.

Header inspection of all 64,947 enumerated files found **474 physical PDFs, representing 406 distinct byte identities and 68 duplicate copies**. Of the identities, 382 provide opening text and 24 needed image/source identity evidence. Twenty-six files named `.pdf` are actually HTML or a short 404 response. Three PDF identities are failed or blank conversion intermediates. File type alone is not source-body evidence.

The format census also covers 42 PostScript files, twelve gzip containers, thirty ZIP-format files and nine embedded PDF members. All nine embedded PDFs duplicate already inventoried physical files. Twenty-eight Word files are fourteen duplicate pairs of short APA citation exports, not chapter or book bodies. See [format census](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/document-container-summary.json), [PDF identities](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/pdf-holdings-identities-summary.json), [image-only identities](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/image-only-source-identities.md), and [candidate resolutions](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/bibliography-pdf-identity-resolutions.md).

Exact-version distinctions matter. McMillan's 1992 thesis does not supply the separately required revised 1993 book; a Thomas 1996 report is not automatically the 1997 chapter. The nominally 1982 Sistla-Clarke file includes a copy of the 1985 article, with a separate 1982 paper also held. The saved Burris text is a later author update. Positive holdings were also recovered: all three Boolean Algebra volumes, the published Baader-Horrocks-Sattler chapter inside the saved handbook, and the exact SMT-LIB release of 7 July 2025. The source summary now selects these exact manifestations rather than a convenient earlier draft or excerpt.

## Review, publication and preservation

The saved `handbook/main.pdf` has **836 pages**, was produced on **18 August 2026**, and is recorded as a construction draft with `release_ready: false`. It does not establish a build of the current September text. The inventory records its metadata and existing release evidence without generating a new build or inspecting manuscript renders.

All **615 formal requirement closure records remain OPEN**. Current reviewed-handbook, register and packet stores contain no accepted records. The inventory locates 42 dated scoped review/writing artifacts; these are not 42 independent accepted reviews. Several old accepted presentation hashes differ from current files. Final user acceptance is absent. These findings and the stale terminal/source-crosswalk evidence are detailed in [publication and review standing](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/publication-and-review-state.md).

The workspace census contains **64,947 files totaling 24,252,726,473 bytes**, excluding Git internals, directory links and this inventory directory. Much of that volume is acquisition material and two legacy coverage catalogs, not manuscript prose. The catalogs were inventoried by path and size. Fifty-seven preexisting test files were counted; they were not run as manuscript evidence.

The protected snapshot has **951 files**, aggregate SHA-256 `36611b04892a08aaea2b152b86a0871abb525848c94bcf50728faf81bf70c079`. Git was already dirty at the start: branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`, 147 modified tracked paths and 2,111 untracked paths outside this audit. Existing changes belong to the user. No manuscript edits, source acquisitions, commits, builds or render runs were part of the inventory continuation.

## Completion evidence and limits

The [independent inventory audit](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/inventory-completion-audit.md) independently reconciled original fields, protected hashes, full Part IX coverage, component packets and all bibliography keys. The [integration record](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/refinement-evidence-reconciliation.json) records current evidence hashes and exposes any unresolved integration conditions.

This completes the defined inventory by giving current evidence and a disposition for its scope. It does not claim a fresh independent proof audit of all 92,889 active source lines, full reading of every cited source book, current publication acceptance, or a completed manuscript. The remaining authoring, correction, exact-source, review and production obligations are recorded as book work in the current ledger. Authoring remains stopped.
