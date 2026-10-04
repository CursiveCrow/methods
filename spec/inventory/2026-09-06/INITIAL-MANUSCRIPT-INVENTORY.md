# The Methods of Reason: current manuscript inventory

**Completion assessment in progress, September 7, 2026.** The initial file census and 615-row enumeration are complete. The complete assessment of manuscript obligations is still being investigated under [the inventory completion plan](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/INVENTORY-COMPLETION-PLAN.md). Later evidence in this directory supersedes preliminary classifications where explicitly identified. The report must not be read as an exhaustive completed content audit.

Snapshot begun September 6, 2026, Pacific time. Authoritative folder: `C:/Dev/the-methods-of-reason`. The source snapshot was captured at `2026-09-07T06:32:40.260857+00:00`; the comparison at the end of this inventory records the unchanged final bytes.

## Current completion assessment

**The manuscript is a substantial, unevenly developed draft. It is not complete or ready for publication.** All fourteen parts have active content. Parts IX and X contain extensive recent technical writing. Other parts still contain short surveys, cited results, sketches, and explicit promises to developments that have not been supplied. Several registered historical source presentations remain unpresented. References and lookup material also need reconciliation with the current text.

Manuscript writing is stopped. Authored audit files are confined to `spec/inventory/2026-09-06/`. The comparison of 951 protected source, bibliography, registry, governing, archival, and publication files found no additions, removals, or changed bytes. See [snapshot comparison](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/snapshot-comparison.json).

**There is no defensible single completion percentage.** The 615 original requirements overlap, vary greatly in size, and do not exhaust the inherited-source and separate-source-presentation obligations. A present theorem, a local proof, a whole source presentation, a current review, and final publication acceptance are different units. The counts below identify what actually exists and what remains unresolved without treating any of those units as interchangeable.

## What exists in the current manuscript

The census follows the actual `main.tex` input graph, including the known `showcalculus` macro. It does not execute TeX or treat every file under `handbook/` as part of the reader's book.

| Measure | Current inventory |
| --- | ---: |
| Active parts | 14 |
| LaTeX files under `handbook/` | 937 |
| Unique LaTeX files reached from the current driver | 840 |
| LaTeX files outside that route | 97 |
| Lines in the reachable files, including drivers and generated lookups | 92,889 |
| Reachable TeX bytes | 4,871,791 |
| Explicit editorial theorem/lemma/corollary declarations | 396 |
| Their declared status: proved / sketched / cited | 136 / 4 / 256 |
| Additional inherited theorem/lemma/corollary environments | 185 |
| Definition environments, inherited and editorial | 582 |
| Annex items | 152 |
| Explicit proof environments | 264 |
| Inherited proof-plan environments | 15 |
| System entry cards | 43 |
| Card adequacy/decidability fields: proved / sketched / cited | 8 / 4 / 74 |
| Calculus-sheet declarations / rule rows | 84 / 566 |
| Symbol-registry rows | 854 |
| Bibliography entries / distinct keys cited through inspected mechanisms | 630 / 615 |
| Literal missing input files / unresolved proof-status targets | 0 / 0 |
| Unresolved literal reference targets | 7 |

These are source counts and declared statuses. They are not newly verified mathematical results. Annex items and proof environments overlap and must not be added together. Part IX also contains substantial inline proof prose that these environments do not count: 30 of its paragraph headings explicitly concern proofs, constructions, soundness, or completeness. Its three `proof` environments therefore do not measure its actual proof-writing volume.

Other active source structures include 35 figure environments and 35 TikZ pictures; 38 table floats and 102 longtable environments; 152 caption commands; 106 exercise and five solution environments; three listing environments; and 953 explicit index commands. These counts include containers and generated structures. They do not establish distinct mathematical coverage, diagram correctness, exercise/solution correspondence, or final index completeness.

The 92,889 lines divide physically into 59,928 under `parts/`, 17,482 under `restoration/`, 10,951 under `annex/`, 3,310 in generated lookups, 999 in calculus-registry files, and 219 in the remaining driver/frontmatter/bibliography inputs. A line count is a volume indicator, not a prose word count.

Full item inventories: [LaTeX files and active routing](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/latex-files.csv), [input edges](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/input-edges.csv), [mathematical environments](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/mathematical-environments.csv), [proof links](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/proof-links.csv), [all environments](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/all-environments.csv), [headings](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/headings.csv), [calculus rules](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/calculus-rules.csv), and [bibliography](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/bibliography.csv).

## Every original requirement is accounted for

The inventory reconciles exactly to the four original registers: **615 rows, with no missing or duplicate register/ID pairs**. Original wording, historical status, treatment, priority, and other original fields remain in the consolidated JSON. All fifteen original domain-x rows are retained. Their old exclusions and the old E/T/S/P treatment ceilings are not used to declare the present full-compendium scope complete.

| Register | Rows inventoried |
| --- | ---: |
| New content | 185 |
| Depth gaps | 141 |
| Historical defects | 88 |
| Apparatus | 201 |
| Total | 615 |

For the **527 content, depth, and apparatus rows**, the current matching-material assessment is:

| Current coverage classification | Rows | Meaning |
| --- | ---: | --- |
| Substantive matching material present | 384 | An actual passage, proof, sheet, table, figure, or other relevant artifact exists; full fulfillment can still be unverified or incomplete. |
| Mixed | 100 | Some required components are substantial while others are short, absent, cited, or unverified. |
| Summary only | 27 | The matching treatment is a short description or pointer. |
| Not located | 5 | The specifically requested surface or treatment was not found in the inspected active scope. |
| Mapping unverified | 11 | A historical or candidate artifact has not been reliably mapped to the active requirement. |

The same rows have 37 local-proof, 136 cited-only, 11 source-sketch, 114 mixed, 31 not-applicable, and 198 unverified proof/validation classifications. These are row-level assessments; overlapping requirements can refer to the same proof. They are not counts of distinct proofs.

Twelve very narrow content or repair obligations have positive bounded verification flags: `N-a-013`, `N-a-070`, `D-P1-001`, `D-P10-027`, `D-P2-003`, `D-P2-006`, `D-P3-005`, `D-P8-004`, `R-016`, `R-031`, `R-035`, and `R-041`. This is neither “only twelve things written” nor a twelve-of-615 completion score. It records the limited scope actually verified in this inventory; every other row states its concrete omission or outstanding verification question.

The complete ledger is available as [readable Markdown](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/complete-requirement-ledger.md), [CSV](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/complete-requirement-ledger.csv), and [JSON with original fields and full assessments](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/complete-requirement-ledger.json). The [reconciliation record](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/requirement-reconciliation.json) records the exact coverage comparison.

## Part-by-part inventory

Body lines below include the active inherited restoration text and exclude generated lookup files. Annex lines include annex drivers. Shared calculus and lookup inputs are tracked separately; these columns are source-volume measures, not page or completion estimates. Full counts are in [per-part-census.csv](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/per-part-census.csv).

| Part | Body / annex lines | What is present | Concrete remaining scope or verification |
| --- | ---: | --- | --- |
| I — Foundations | 1,716 / 0 | Sets, relations, functions, cardinality, languages, structural induction/recursion, and proof conventions; ten inherited proof environments. | No new-content/depth rows target this part. That does not close inherited-source obligations. Its standalone historical annex is not active; complete source coverage remains unverified. |
| II — Classical logic | 7,651 / 360 | CPL, FOL, calculi, normal forms, completeness, higher-order material, and substantial Hilbert, equality, many-sorted and matched SOL additions. | Full Post classification and the requested Tseitin construction were not located on the active route; equivalence congruence remains an exercise. General Herbrand/tableau and parts of HOL/source completeness remain cited or incomplete. |
| III — Model theory | 3,370 / 596 | Classical model theory, types, ultraproducts, classification, finite models, preservation, and a substantive Craig–Robinson–Beth proof package. | Fraïssé and categoricity developments retain outlines/citations; Morley/Baldwin–Lachlan hard lemmas are deferred. Many preservation, forking, saturation, and source-specific proof obligations remain. |
| IV — Computability and complexity | 3,582 / 251 | Computation, reducibility, degrees, finite-injury work, hierarchies, algorithmic information, MRDP survey, and complexity classifications. | MRDP encoding and composition machinery are omitted; many equivalence and hierarchy results remain cited. TTE, computable analysis, and Weihrauch development were not located in the active part. |
| V — Arithmetic, incompleteness, and provability | 2,244 / 237 | Arithmetic/coding, incompleteness, interpretability, provability logic, decidable arithmetic, independence examples, and reverse mathematics. | Solovay arithmetization is not supplied; Guaspari–Solovay R is a pointer; Goodstein/hydra descent and independence developments remain incomplete or cited. The larger historical annex is inactive. |
| VI — Set theory | 4,895 / 420 | ZFC, ordinals, cardinals, forcing, Choice, combinatorics, large-cardinal/absoluteness material, descriptive set theory, determinacy, and an actual PCF introduction. | Advanced PCF machinery/proofs, proper forcing and iterations/PFA/MM, fine structure and core models remain incomplete. Numerous large-cardinal, cardinal-arithmetic, regularity, and determinacy results remain cited. |
| VII — Proof theory and type theory | 3,947 / 1,234 | LK/LJ variants, translations, Cut/normalization material, Craig/Beth proofs, lambda/type theory, interpretations, generalized calculi, and proof complexity. | Full arithmetic Gentzen analysis, several normalization/interpretation results, HoTT/HIT/cubical developments, proof-net correctness/sequentialization, and GoI execution remain unfinished or pointers. |
| VIII — Nonclassical logics | 6,252 / 265 | Intuitionistic, modal, temporal/epistemic, conditional/deontic/free, many-valued, relevance/linear, and nonmonotonic material, with 41 system cards. | The supplied canonical proof covers four systems rather than all seven requested. Relevance/gamma proofs remain cited. Promises to Part X for arbitrary-premise MV completeness and exact algebra classes are not fulfilled there. |
| IX — Logic in computer science | 32,823 / 894 | Extensive separate presentations for finite models, description logic, automata, model checking, mu-calculus, program logic, databases, CSP, and complexity. Much proof writing is inline. | Several exact historical source presentations remain unpresented. N-c-018 retains the original-threshold and tree/backedge-convention questions; other long source proofs remain abbreviated. Technical volume alone does not close whole-topic requirements. |
| X — Algebraic and categorical logic | 4,927 / 6,646 | Eighty annex proof items covering universal algebra, Stone/Priestley/Heyting/Esakia, modal algebra, categories/STLC, Lawvere theories, doctrines/quantifiers, adjoints, and presheaf foundations/topos objects. | HSP remains cited. Locales, topological S4, MV/BL/MTL and related algebraic presentations, cylindric/relation algebras, full topos internal logic/Kripke–Joyal clauses, and Tierney/CH remain short or incomplete. |
| XI — Philosophy of logic | 247 / 7 | A 244-line chapter on truth, paradoxes, philosophical positions, and related distinctions; five definitions. | TB/CT/KF/FS are not fixed formal theories with exact axioms and strength claims. Several arguments and plural/inductive/confirmation treatments remain brief or unlocated. No local annex proof is supplied. |
| XII — Automation and formal practice | 4,760 / 41 | SAT/CDCL, SMT, unification, superposition, rewriting, proof assistants, extraction/trust discussion, worked methods, restored exercises and feedback. | The explicitly requested Nelson–Oppen and MM termination/MGU proofs are still cited or incomplete. Congruence closure/simplex, realizability extraction, and some algorithmic details need development. Status and route tables are stale. |
| XIII — Chronology and biography | 335 / 0 | Selected chronology, biographical capsules, and a method-transition table. | A-201's requested notation lineages, periods, exemplar glyphs, and descendants are not supplied by the current table. A dedicated landmark-paper register and full historical verification remain unresolved. |
| XIV — Apparatus | 436 / 0 | Active rule catalog, master tables, selected glossary, named-theorem/symbol views, and unified subject/person index policy. | Coverage and freshness remain unverified; glossary coverage is selective. Requested lists of tables, figures, and listings were not located. Rule/table/figure requirements have specific scope and mapping gaps. |

Detailed current text and row evidence: [Parts I–VII](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/parts-01-07.md), [Parts VIII–XI](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/parts-08-11.md), and [Parts XII–XIV plus every apparatus category](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/parts-12-14-apparatus.md).

## Confirmed reference and apparatus issues

Five active reference targets are defined only in files outside the current reader route:

| Active use | Unavailable target definition |
| --- | --- |
| [Heyting completeness, line 60](C:/Dev/the-methods-of-reason/handbook/parts/p10/heyting-completeness.tex:60) | `def:p08-ipl-finite-support`, in inactive `parts/p08/intuitionistic-and-intermediate.tex:24`. |
| [Heyting completeness, line 182](C:/Dev/the-methods-of-reason/handbook/parts/p10/heyting-completeness.tex:182) | `def:p08-ipl-kripke-structure` and `def:p08-ipl-consequence`, in that inactive file at lines 38 and 80. |
| [Modal algebra, line 26](C:/Dev/the-methods-of-reason/handbook/parts/p10/modal-algebra-completeness.tex:26) and line 163 | `def:p08-modal-derivability`, in inactive `parts/p08/modal-logics.tex:48`. |
| [AC-to-Zorn proof, line 18](C:/Dev/the-methods-of-reason/handbook/annex/p06/cardinals-choice-supplement.tex:18) | `thm:p01-well-ordering`, in inactive `parts/p01/mathematical-preliminaries.tex:136`. |

Two additional targets, `thm:p09-cq-evaluation` and `thm:p09-tqbf-proof`, have no current definition anywhere in the inspected handbook TeX. They remain in the active [Part IX audit](C:/Dev/the-methods-of-reason/handbook/generated/audit-p09.tex:83) and [named-theorem index](C:/Dev/the-methods-of-reason/handbook/generated/named-theorem-index.tex:94). The actual TQBF theorem is `thm:p04-tqbf-pspace` and its annex proof is present; the stale name does not mean the TQBF proof is absent.

Part XII's [status table](C:/Dev/the-methods-of-reason/handbook/parts/p12/further-reading.tex:29) says it is exhaustive but lists eight results and omits seven newer named results. Its canonical-route table still calls the MM material deferred despite the actual added sheet and method. Its driver expressly leaves `audit-p12` inactive because the generator scans historical files. These are current navigation mismatches, independent of whether the mathematics they point to is correct.

The [97 unrouted files](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/unrouted-latex-files.csv) include historical combined chapters/annexes, unused audit tables, former errata files, and some inherited title/bibliography slices. They are not all missing content and must not be indiscriminately imported. Active corrections and restored passages may replace them.

## Historical defects and current policy

Every one of the 88 historical defect rows has a separate current disposition:

| Current disposition | Rows |
| --- | ---: |
| Actual remediation evidence present | 43 |
| Confirmed remaining presentation issue in a mapped passage | 2 |
| Historical claim still unverified | 14 |
| Old coordinate/current mapping unverified | 14 |
| Old required fix conflicts with later policy | 15 |

The two narrow remaining findings are R-030's absent four-case DLO extension analysis in the mapped proof and S-011's uncited/unlabelled ACF categoricity example. They are not new mathematical counterexamples. R-039 now has common-knowledge axioms, theorem-only induction, and qualified weak-completeness/noncompactness claims. Canonical LK, defined-negation LK, and LK with equality are explicitly separated in the current text.

Current policy requires direct correction of active mathematical errors. Historical global notation bans, blanket conversion of source results into editorial status syntax, registry-only source displays, and exercise-retirement dispositions conflict with later source-scoped and correction policies. Those rows require an accurate present disposition; their old wording is not authority to damage current content. The full evidence is in the [defects inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/defects.md).

## Source holdings and source-presentation completion

The complete file-header scan now finds **474 physical files with PDF headers**, representing **406 distinct byte identities**. It found six PDFs with nonstandard or missing extensions that the first 468-file extension-based census had missed. There are 68 duplicate physical copies. The count includes manuscript builds, previews, unrelated reference material, and blank/failed conversion artifacts; it is not a count of distinct primary works or fully read and authenticated works. Twenty-six files named `.pdf` are failed download responses: 25 HTML documents and one short 404 text response. The bibliography has 630 entries, no duplicate keys, and no literal stub markers; 615 distinct keys are cited by the inspected literal, theorem-status, and card mechanisms. Bibliographic presence alone does not establish exact edition, complete local text, reading, rights, or faithful manuscript treatment.

All 64,947 enumerated files received a file-header inspection. The two general ZIP archives contain nine PDF members, each byte-identical to a physical PDF already inventoried. The 28 Word-format files are fourteen duplicate pairs of APA citation exports, only 103–166 text characters each; they are not the book/chapter bodies suggested by parts of their filenames. The other source containers comprise 42 PostScript files and twelve gzip files (eleven expand to PostScript and one to DVI). See [document-container inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/document-container-summary.json) and [non-PDF source inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/nonpdf-source-summary.json).

The current Part IX text explicitly leaves separate historical presentations open, including Thatcher–Wright 1968 in N-c-015; Clarke–Grumberg–Peled's 1999 first edition in N-c-016; McMillan's revised 1993 book in N-c-017; and other exact editions, articles, and chapters listed in the [Part IX inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/parts-08-11.md). A later proof or a thesis/precursor does not establish completion of a separately registered original presentation. Some sources can be held while their required presentation remains unwritten.

| Selected source requirement | Current holding / gap |
| --- | --- |
| Thatcher–Wright 1968 article | Exact article PDF remains unacquired in the inspected records; the held Thatcher 1965 dissertation is a different work. |
| McMillan revised 1993 book | The held PDF is the 1992 thesis; exact revised-book body remains unresolved. |
| Description-logic books, 2003 and 2017 | Exact required book bodies/chapters are not established by the selected holdings. Slides, other editions, and independent modern ALC proofs have separate standing. |
| Clarke–Grumberg–Peled 1999 | Complete exact book remains unresolved; the held Baier–Katoen 2008 book supports a different presentation. |
| Mac Lane–Moerdijk 1992 | Correctly identified 638-page scan is held; relevant presheaf and logic passages have recorded reading and use. |
| Adámek–Rosický–Vitale | The held 252-page text is the 2010 author draft, distinguished in the current manuscript from the published 2011 book. |
| Handbook of Boolean Algebras, volumes 1–3 | All three full scans are held. The older acquisition manifest understates holdings; full technical reading/admission remains separate. |

The separate [source-holdings report](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/source-holdings.md) records sixteen inspected source or source-family holdings, known missing editions, use, and review boundaries. It is selective about exact-source verification. The [physical source/PDF list](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/source-and-pdf-files.csv) accounts for all inspected candidate files. This inventory did not acquire new papers or certify every cited work's full-text reading or reproduction rights.

The frozen inherited source is intact: its 17,206-line TeX and 251-page PDF match the inherited manifest and current hashes. Archival integrity is separate from the completeness and correctness of the active corrected manuscript.

## Publication and review state

The saved [main.pdf](C:/Dev/the-methods-of-reason/handbook/main.pdf) is **836 pages**, 4,442,893 bytes, last modified August 18, 2026, at 00:39:32 Pacific. Its SHA-256 is `ee4c5324c1aac7fc3b0e13fba816b35ec6f39be059e807b01695fe1a9900851f`. Metadata and page count were read; the manuscript was not rendered. This PDF does not represent the later September writing.

The existing publication manifest says `construction-draft`, `release_ready: false`, and has no final release evidence. The terminal-readiness manifest is dated August 18 and remains **OPEN**. Its 265/282 restored intervals and 17 residuals are a historical restoration measure. They cannot be converted into a current manuscript writing percentage.

The live source-unit crosswalk has 1,055 rows. All stored static fields now pass, but source/topic/adversarial/build/visual fields remain pending and all admission dispositions remain open/missing. Its hash differs from the older terminal manifest. The formal register-closure projection still records 615 OPEN rows with pending gates. Reviewed handbook, register, and presentation-packet terminal-record stores are empty. These dated administrative records neither admit today's text nor prove that today's substantial writing is absent.

There are real scoped proof and source/text reviews. The review inventory indexes 42 dated review/writing/status artifacts and records their limits. Sampled older N-c-010, N-c-013/014, and N-c-016 acceptance snapshots differ from current manuscript bytes, so those historical verdicts do not automatically certify the current files. Recent P3/P7, PCF, and P10 reviews have narrower scopes than entire-part or whole-book completion. Final user acceptance is not recorded.

See the full [publication and review inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/publication-and-review-state.md). No new mathematical correctness certification, current build pass, visual pass, or publication acceptance is claimed by this source census.

## Workspace and workflow footprint

The physical inventory covers **64,947 files totaling 24,252,726,473 bytes (24.25 GB decimal)**, excluding `.git`, this audit directory, and directory links. No directory links or file-read errors were encountered in that enumeration.

| Category | Files | Bytes |
| --- | ---: | ---: |
| Manuscript source under `handbook/` | 941 | 6,408,830 |
| Manuscript build/assets | 17 | 7,678,712 |
| Frozen archival source | 2 | 2,805,138 |
| Requirement registers | 5 | 153,096 |
| Specification and ledgers | 58 | 47,876,953 |
| Two legacy coverage catalogs | 2 | 13,350,988,518 |
| Verification and provenance | 583 | 437,606,062 |
| Research and review notes | 511 | 3,811,569,910 |
| Acquisition and temporary working artifacts | 61,218 | 6,404,885,886 |
| Tooling | 222 | 6,339,426 |
| Other project files | 1,388 | 176,413,942 |

The two coverage catalogs alone occupy 13.35 GB. They and the multi-GB research records were inventoried by metadata, not scanned as a book-completion denominator. Their millions of bookkeeping rows are not millions of unwritten manuscript obligations. The tooling directory contains 57 `test_*.py` files; none were run or added to the book's maintained tools during this inventory. No cleanup or deletion was performed.

The source-control snapshot is branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`, with 147 previously modified tracked files and 2,111 previously untracked files outside this audit. Those changes were preserved. The [complete workspace file list](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/workspace-files.csv) and [Git inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/git-state.csv) preserve the individual records.

## What remains before manuscript completion can be claimed

1. Finish the specific mathematical, philosophical, algorithmic, and source-presentation gaps recorded for each part, including concrete cross-part promises that currently have no supplied target development.
2. Resolve exact-source requirements where a separately registered original is missing or unpresented, preserving the distinction between that original and a later reconstruction or precursor.
3. Reconcile the current text with requirement and defect records, including superseded policy conflicts; complete the outstanding source and mathematical verification for actual current passages.
4. Repair the recorded reference and apparatus mismatches, verify retrieval coverage and freshness, and account for every requested table, figure, rule sheet, glossary, index, and exercise/feedback relationship.
5. Once the text is settled, produce and verify a publication artifact from that exact source, update admission evidence against current files, and obtain final user acceptance.

These are recorded remaining obligations, not authorization to resume them during the inventory. Authoring remains stopped.

## Limits and reproducibility

This is a complete file and original-register inventory with current source-based coverage findings. It is not a line-by-line reproof of the 92,889-line manuscript, a full read of every held source, or a new publication review. The long source presentations were mapped and relevant evidence inspected; their entire proof bodies were not all reread during this census. Literal TeX routing does not evaluate arbitrary macros or conditional expansion. Candidate absence statements are limited to their documented search scope.

The research workflow produced evidence-pinned part reports and preserved every original requirement in a reusable ledger. The two audit scripts write only into this inventory directory. [collect_inventory.py](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/collect_inventory.py) preserves the initial snapshot when refreshing the text census; [consolidate_inventory.py](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/consolidate_inventory.py) reconciles the four ledgers and performs a fresh path/hash comparison. Neither changes the manuscript or runs the book's test, build, or rendering workflow.
