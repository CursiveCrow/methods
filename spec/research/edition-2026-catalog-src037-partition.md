# CAT-01: SRC-037 structural partition and proposed presentation packets

Date: 9 September 2026. This is a bounded production proposal, not a catalog admission or a manuscript-completion count. The historical catalog, assignment index, validators, canonical ledger, manuscript and admission records are unchanged.

## Completed extent and explicit continuation

The complete SRC-037 source group has been extracted with every original CSV field and raw record ID preserved. Its 3,015 hierarchy records are partitioned by their actual producer roles and retain their complete parent joins. All 34 Crossref identity strings and all 1,422 legacy obligation-candidate strings were compared, in order, with their complete producer construction and match exactly.

The retained institutional contents evidence identifies 28 numbered chapter presentations across two volumes. These are proposed presentation packets with concrete component obligations below. They are not 28 completed chapters, and they are not yet a final count of intellectual units: a chapter can contain several distinct calculi, proofs, methods and versions.

The source group's complete structural partition is finished. The fine semantic partition of every mixed artifact's contents is not finished. In particular, the extractor's child text-shape counters are navigation hints, not admitted metadata classifications. No whole artifact family is called metadata merely because some members are headers, parser fields or access responses. The next block must join each artifact to its acquisition and derivation version, apply full artifact-specific producer grammars and map actual chapter-body components. All raw membership is retained for that continuation.

## Authority and pinned input

The edition contract requires every historical record to retain a traceable disposition and prohibits counting metadata as writing. CAT-01 permits deterministic metadata-family batches only with justified predicates and preserved membership. The existing record-profile and first-partition conventions distinguish record structure, source evidence, intellectual treatment and admission.

The existing profile and assignment fingerprint are reused:

- Catalog: spec/full-compendium-coverage-manifest.csv
- Pinned SHA256: 69d0f7ccb89e9be070366102f958a4034f632088b269a92ee244bfa5b41d55e8
- Pinned records: 9,162,150.
- Observed byte size: 6,947,214,502, matching the existing profile.
- The full catalog hash was not repeated. The stream read the prefix through SRC-037 and stopped at the SRC-038 source descriptor. Global uniqueness evidence is inherited from the already completed profile; the new receipt checks sequential IDs and parent/path consistency within this source group.

Observed SRC-037:

| Record kind | Count |
| --- | ---: |
| source | 1 |
| hierarchy | 3,015 |
| topic | 2,460,146 |
| Total source-group records | 2,463,162 |

The complete group occupies byte interval [524080654,2346007392) of the pinned CSV, excluding the CSV header: 1,821,926,738 bytes. Its scoped raw-byte SHA256 is 58b60de8cdf92ce5929910af026d73ed93efde21d464a384c8f172316af69912. This is a source-group hash, not a recomputation of the full catalog hash.

All topic IDs SRC-037-T001 through SRC-037-T2460146 and hierarchy IDs SRC-037-H001 through SRC-037-H3015 occurred in consecutive producer order. There were zero observed parent/path or sequential-ID conflicts. The complete source descriptor, including its ordered locator arrays and source metadata, is preserved in the receipt and original-row archive.

## Reproducible artifacts

All artifacts below are under tmp/edition-2026-catalog-src037/:

| Artifact | Role and fingerprint |
| --- | --- |
| extract_src037.py | Source-specific streaming extractor. It reads the existing CSV, copies the exact header and SRC-037 rows, records every hierarchy's original fields and emits contiguous raw-ID/parent membership ranges. It refuses to overwrite existing outputs. |
| src037-original.csv.gz | Exact original CSV header plus the entire SRC-037 row block, gzip encoded. 68,423,349 bytes; SHA256 1bdfa12ad5d432770f5b5f5d6ad40aa2cf02b6fdf50d9982e76202a0ce8498bf. |
| parents.json | Every original source/hierarchy record and all parent-level counts and first/last topic IDs. 4,591,003 bytes; SHA256 50c45c66ea8e5e950da76548c34c09ec38c981efec852a6828ef837244f551e0. |
| membership-ranges.jsonl | Ordered contiguous ranges, with original first/last IDs, parent, record type, count and original byte endpoints. 1,829,027 bytes; SHA256 8622c155e7df582dcec8ad135f740a0a84cf382373b603a883bfa6bca7ae11e7. |
| receipt.json | Input pin, actual source descriptor, observed counts, source-group byte interval/digest, all parent-family counts, producer fingerprints and output hashes. |
| crossref-items.json | All 34 original Crossref item objects, retaining every field and author/contributor array. 1,322,432 bytes; SHA256 15c618e9f4f4e923284cbfcac4b8624f33946e699c40c7bad4ea93411d455d20. |
| extract_identity_obligation_families.py | Complete, bounded construction of the 34 identity strings and 1,422 obligation strings from the actual producer constants and full Crossref item sequence. |
| identity-obligation-receipt.json | All original rows of those two families plus exact ordered string-comparison results. SHA256 e66fb89b13ca546b8aaaad0b7d557c86fcad704e59ac85a6551581150f59e675. |

Commands from C:/Dev/the-methods-of-reason, using the available bundled Python:

    python -X utf8 tmp/edition-2026-catalog-src037/extract_src037.py
    python -X utf8 tmp/edition-2026-catalog-src037/extract_identity_obligation_families.py

Existing outputs are retained; a deliberate rerun needs a separately named output location. The extraction is data processing for this source group, not a new validator or acceptance system. No production catalog tool, renderer, test suite or review was executed.

## Complete producer chain read

The actual catalog producer is tools/build_coverage_manifest.py. Its schema is:

    stable_id, record_type, source_id, source_title, source_metadata,
    retrieved_granularity, hierarchy_path, parent_stable_id, displayed_title,
    source_https_urls, source_non_https_urls, source_scheme_less_identifiers,
    retrieval_date, mapping_status

Its streaming parser assigns one source row; sequential H identities to level 4–6 headings; and sequential T identities to every nonempty remaining bullet. It does not classify subject matter. The exact metadata parser, ordered locator handling, source-row construction, hierarchy stack and topic construction were read. Its CLI uses that streaming parser. No historical manifest or baseline generator was run.

Source-only metadata and locator cells are populated on the source descriptor and blank on child rows. A blank child cell means resolve through source_id; it is not the source descriptor's literal empty JSON list. The extraction retains that distinction and all ordered locators.

The immediate upstream producer is tmp/acquisition/src037/build_acquisition_note.py. Its complete artifact emitters and orchestration were read, including:

- Ledger.heading/topic: the administrative heading/bullet grammar and OPEN suffix.
- Physical-line decoding and transcription, including strict UTF-8 result, reversible Latin-1 fallback, original line terminators and JSON-literal escaping.
- JSON object/key-order, array/length and scalar/address records.
- HTML source lines, element/XPath/attributes, direct/tail text, table cells and JSON-LD records.
- XML source lines, element/XPath/attributes and text records.
- PDF identity, metadata, outline, form fields, page geometry, annotations and embedded-image descriptors.
- Raster dimensions, mode/format, metadata and EXIF descriptors; no raster-pixel rows are emitted by this producer.
- Gzip headers/trailers/decompression descriptors and binary edge-byte descriptors.
- Full request-manifest joins, failed-request generation, the fixed conflict list, the complete legacy unit/component product and all recorded gate statements.
- The page-observation ledger and the sorted scratch-directory/artifact hierarchy.

Also read: build_request_manifest.py, build_pre_note_evidence.py, render_and_extract_pdfs.py and derive_document_renderers.py under that acquisition directory, plus the relevant primary-acquisition script. These establish distinct DOI content-negotiation formats, HTTP body/header/stderr receipts, PostScript/gzip derivatives, PDF text/image derivatives, table extraction and thumbnail-observation records.

The page-observation producer uses two fixed observation strings: one for the two failed blank renderer outputs and one saying that visible marks occurred in a thumbnail. These records do not establish that a chapter's mathematics was read or accepted.

## Exact hierarchy families and raw topic membership

| Producer family | Hierarchy nodes | Direct topics | Actual role |
| --- | ---: | ---: | --- |
| Crossref sequence container, H001 | 1 | 0 | Administrative returned-order container. |
| Crossref items, H002–H035 | 34 | 34, T001–T034 | Bibliographic identity records. Complete strings match all 34 returned item objects. |
| Failed requests, H036 | 1 | 96, T035–T130 | Historical request/access outcome descriptors; not requested chapter bodies. |
| Conflicts, H037 | 1 | 18, T131–T148 | Preserved source/version/access-conflict assertions. They remain evidence to resolve. |
| Legacy obligations, H038 | 1 | 1,422, T149–T1570 | Exactly 47 unit descriptors times 30 component descriptors, plus 12 additional gap candidates. These are retained claims requiring disposition, not 1,422 proven intellectual units. |
| Historical gates, H039 | 1 | 8, T1571–T1578 | Historical OPEN gate statements, not current instructions or acceptance. |
| Visual container, H040 | 1 | 0 | Administrative container. |
| Page-observation parents, H041–H059 | 19 | 1,261, T1579–T2839 | Recorded observations of page thumbnails, separately tied to source PDF/render/overview/page coordinates. |
| Scratch container, H060 | 1 | 0 | Administrative container. |
| Scratch directories | 23 | 0 | Exact retained acquisition-directory hierarchy. All IDs and original paths are in parents.json. |
| Artifact presentations | 2,932 | 2,457,307, T2840–T2460146 | Mixed acquired/derived/operational evidence. Complete per-artifact raw membership is in parents.json and membership-ranges.jsonl. No whole-family metadata or source-equivalence disposition is proposed. |

The hierarchy counts sum to 3,015, and the topic counts sum to 2,460,146. Every original parent record and its complete fields is retained; the table abbreviates only the display of that full membership.

The mixed-artifact diagnostic counters include 2,107,695 physical-line-shaped records, 119,273 JSON-field-shaped records, 150,265 XML-shaped records and 63,641 HTML-shaped records. These counters come from navigational shape predicates in the extractor and are not a completed full-string grammar classification. In particular, physical lines can encode PostScript, a PDF text derivative, an HTML response, a bibliography, or an acquisition script. A line count cannot identify its intellectual role. The full raw archive is the authority for refining these candidates.

For the two completely matched bounded families, the exact membership predicate includes the pinned catalog identity, source_id SRC-037, record_type topic, actual parent IDs, sequential stable IDs, and equality of the full displayed string with the actual producer construction. All original rows are retained in identity-obligation-receipt.json. No title sample or substring alone supplies those classifications.

## Source editions, manifestations and retained chapter presentations

The retained GBV institutional title/contents PDF is gbv-toc-retry-01.body, an 11-page PDF. Its preserved layout derivative was read in full. It identifies Alan Robinson and Andrei Voronkov as editors, shows a Volume II title page with both Elsevier and MIT Press imprints, and contains the complete contents for Volume 1 and Volume 2:

- Volume 1: chapters 1–14, Parts I–IV, and a Concept Index beginning at 963.
- Volume 2: chapters 15–28, Parts V–VIII, and a Concept index beginning at 2115.

The 2001 edited-work identity is supported by the retained Crossref and institutional bibliographic records. Preserve separate manifestation nodes for the Elsevier ISBN 9780444508133 and MIT ISBN 9780262182232. The legacy ISBN/locator 0444829490 is a separate unresolved identifier lead. Different recorded page totals and publisher displays must not be merged by title alone.

The 34 Crossref items comprise 28 chapter identity leads and six paratext/index leads: Preface (T011), List of contributors (T016), Copyright (T018), List of second readers (T024), Front matter (T027), and Concept index (T031). Crossref's generic book-chapter type does not make these six into mathematical chapter treatments. The volume-one index has its own contents locator and must not be erased merely because this returned Crossref sequence has only the volume-two Concept index DOI.

The source note preserves 19 PDF presentations covering 1,261 recorded pages. The full rendering manifest retains every path, hash and derivation relationship. They include:

- Logical Frameworks: cmu-handbook00-retry-01.body, 87 pages, an author-hosted draft; not established as identical to publisher chapter 17.
- Proof-assistants: geuvers-proof-assistants-retry-01.body, 90 pages, separately retained author presentation.
- Unification: snyder-unification-pdf-retry-02.body, 88 pages, and a distinct 89-page ICCL PostScript-derived PDF.
- Description logics: an acquired 54-page author PDF and a byte-equal 54-page Manchester mirror, plus a separately derived 54-page PostScript rendering. Byte equality of two captures does not remove their locator identities.
- Model checking: a 156-page author PostScript-derived PDF.
- Inverse method, equality in sequent calculi, and term indexing: separate Voronkov PostScript-derived PDFs of 94, 96 and 112 pages.
- Two encodings presentations: an 84-page PDF and an 83-page PostScript-derived PDF; no equivalence is inferred.
- Inductionless induction and small-clause normal forms: separate 51-page and 33-page PostScript-derived PDFs.
- Two one-page blank UMD renderer outputs: retained failure evidence, not the nonmonotonic chapter.
- The MPG 23-page PDF is recorded as Bump Map Shadows for OpenGL Rendering, a mismatched acquisition, not an equality-reasoning chapter.
- The 11-page GBV title/contents presentation is bibliographic/contents evidence, not a full two-volume body.

The historical acquisition producer explicitly records publisher access failures, metadata-only Elsevier API responses and distinct author drafts/mirrors. Those distinctions remain active candidates. No complete publisher body or chapter-version equivalence was established in this block.

One concrete role/version conflict was read directly in the retained Snyder layout: it names Franz Baader and Wayne Snyder as authors, and Paliath Narendran, Manfred Schmidt-Schauss and Klaus Schulz as Second readers. The Crossref item places all five in its author array. The retained presentation's introduction is numbered 441, whereas the complete volume contents puts that chapter's introduction at 447. These are actual role and pagination differences, not title-only evidence of equivalence. Preserve the raw Crossref array, the two-author contents display and the separate second-reader display; the final chapter-version comparison remains open.

## Proposed 28 chapter presentation packets

The proposed identifiers below are local proposal names, not canonical catalog assignments. Every packet retains its raw Crossref seed and the full original item object. Pages are the literal Crossref page field; the independently retained contents provide chapter order and section starts. Differences in authorship arrays, spelling or endpoints remain candidates for a body/version comparison.

| Proposal | Vol./chapter; raw seed | Source presentation; DOI suffix after 10.1016/b978-044450813-3/ | Concrete components to freeze and supply |
| --- | --- | --- | --- |
| HAR2001-C01 | I/1; T005 | Early History of Automated Deduction; 50003-5; 3–15 | Presburger procedure, early theorem-proving systems and first-order logic history, with exact source attribution; proposed P12/P13 context. |
| HAR2001-C02 | I/2; T010 | Resolution Theorem Proving; 50004-7; 19–99 | Standard/general resolution, saturation framework, fairness/redundancy, orderings/selection and effective saturation; proposed P7/P12. |
| HAR2001-C03 | I/3; T030 | Tableaux and Related Methods; 50005-9; 101–178 | Tableau and clause-tableau calculi, framework variants, soundness/completeness and calculus comparisons; proposed P7/P12. |
| HAR2001-C04 | I/4; T013 | The Inverse Method; 50006-0; 179–272 | Classical inverse construction, nonclassical adaptations, naming, strategies, path calculi and contraction-free cases; proposed P7/P8/P12. |
| HAR2001-C05 | I/5; T020 | Normal Form Transformations; 50007-2; 273–333 | Equivalence-preserving forms, Skolem form, CNF and nonclassical forms with exact preservation hypotheses; proposed P7/P12. |
| HAR2001-C06 | I/6; T025 | Computing Small Clause Normal Forms; 50008-4; 335–367 | Standard CNF, renaming, Skolemization, simplification and implementation conditions; proposed P12. |
| HAR2001-C07 | I/7; T014 | Paramodulation-Based Theorem Proving; 50009-6; 371–443 | Paramodulation calculi, saturation, constraints, built-in equational theories and symbolic constraint solving; proposed P7/P12. |
| HAR2001-C08 | I/8; T006 | Unification Theory; 50010-2; 445–533 | Syntactic and equational unification, E-unification methods, algorithm combinations and decidable/undecidable boundaries; proposed P7/P12. |
| HAR2001-C09 | I/9; T028 | Rewriting; 50011-4; 535–610 | Termination, Church–Rosser properties, completion, relativized/conditional rewriting and equational proof procedures; proposed P7/P12. |
| HAR2001-C10 | I/10; T022 | Equality Reasoning in Sequent-Based Calculi; 50012-6; 611–706 | Equality translations, free-variable systems, simultaneous rigid E-unification, incomplete procedures, paramodulation and elimination; proposed P7/P12. |
| HAR2001-C11 | I/11; T008 | Automated Reasoning in Geometry; 50013-8; 707–749 | Algebraic, coordinate-free and AI methods with source-specific algorithms and correctness scopes; proposed P12. |
| HAR2001-C12 | I/12; T012 | Solving Numerical Constraints; 50014-x; 751–842 | Linear constraints over fields, linear Diophantine constraints, nonlinear continuous and Diophantine regimes; proposed P12 with arithmetic dependencies. |
| HAR2001-C13 | I/13; T019 | Automation of Proof by Mathematical Induction; 50015-1; 845–911 | Induction rules, datatypes, proof techniques, search control, rippling, productive failure, existential goals and systems; proposed P7/P12. |
| HAR2001-C14 | I/14; T023 | Inductionless Induction; 50016-3; 913–962 | Formal method, inductive completion, axiomatizations, ground reducibility and comparison with induction; proposed P7/P12. |
| HAR2001-C15 | II/15; T007 | Classical Type Theory; 50017-5; 965–1007 | Actual classical type theory, metatheory and proof search, with its semantics and axioms; proposed P7. |
| HAR2001-C16 | II/16; T002 | Higher-Order Unification and Matching; 50018-7; 1009–1062 | STLC, undecidability, Huet's algorithm, scope management, decidable subclasses and dependent-type unification; proposed P7/P12. |
| HAR2001-C17 | II/17; T029 | Logical Frameworks; 50019-9; 1063–1147 | Abstract syntax, judgments/deductions, metaprogramming, metatheory representation and both typed-calculus appendices; proposed P7/P12. |
| HAR2001-C18 | II/18; T032 | Proof-Assistants Using Dependent Type Systems; 50020-5; 1149–1238 | Proof checking, type-theoretic foundations, type systems, proof development and actual assistant architectures; proposed P7/P12. |
| HAR2001-C19 | II/19; T001 | Nonmonotonic Reasoning; 50021-7; 1241–1354 | General logics and their automation, disjunctive programs, semantics, implementations and benchmarks; proposed P8/P9/P12. |
| HAR2001-C20 | II/20; T033 | Automated Deduction for Many-Valued Logics; 50022-9; 1355–1402 | Signed logic/resolution, proof-system classification, example, rule optimization and infinitely-valued boundaries; proposed P8/P12. |
| HAR2001-C21 | II/21; T021 | Encoding Two-Valued Nonclassical Logics in Classical Logic; 50023-0; 1403–1486 | Consequence encodings, relational, functional and semi-functional translations with adequacy directions; proposed P8/P12. |
| HAR2001-C22 | II/22; T009 | Connections in Nonclassical Logics; 50024-2; 1487–1578 | Labelled connections, propositional/first-order IPL, modal systems through S4 and the S5 family; proposed P8/P12. |
| HAR2001-C23 | II/23; T017 | Reasoning in Expressive Description Logics; 50025-4; 1581–1634 | DL/PDL bridge, unrestricted versus finite model reasoning and richer constructors; proposed P8/P9. |
| HAR2001-C24 | II/24; T004 | Model Checking; 50026-6; 1635–1790 | Logical/second-order languages, transformations/equivalence, completeness/decision procedures, basic and symbolic algorithms, partial orders, BMC, abstraction and modularity; proposed P9/P12. |
| HAR2001-C25 | II/25; T003 | Resolution Decision Procedures; 50027-8; 1791–1849 | Ordering-refinement decision procedures, hyperresolution and description-logic procedures with termination/completeness domains; proposed P8/P12. |
| HAR2001-C26 | II/26; T034 | Term Indexing; 50028-x; 1853–1964 | Path/discrimination/adaptive/code/substitution/context indexes, factoring, multiterm queries, perfect filtering, AC indexing and implementation; proposed P12. |
| HAR2001-C27 | II/27; T026 | Combining Superposition, Sorts and Splitting; 50029-1; 1965–2013 | Complete simple prover, inference/reduction rules, sorts, splitting and global design conditions; proposed P12. |
| HAR2001-C28 | II/28; T015 | Model Elimination and Connection Tableau Procedures; 50030-8; 2015–2114 | Connected tableaux, refinements/pruning, proof shortening, completeness, architectures, constraints and experimental results; proposed P7/P12. |

These component lists come from the complete retained contents outline and identify bounded next reading/writing tasks. Before a packet becomes a final intellectual-unit assignment, read its exact required chapter version, enumerate every definition/theorem/proof/method/example and identify internal subunits. The table does not pretend that chapter headings supply those complete technical statements.

## Current manuscript component evidence, with no chapter-completion credit

Actual active LaTeX was read for the following bounded comparisons:

- P12 first-order-automation.tex defines def:p12-martelli-montanari and states thm:p12-unification-mgu for finite first-order syntactic problems, with occurs check and MGU factorization. It cites BaaderSnyder2001 as well as MartelliMontanari1982. This is a concrete candidate for C08's syntactic-unification component; it does not supply C08's E-unification, combinations or full chapter proof. The retained Snyder presentation's introduction explicitly distinguishes syntactic and equational unification and most-general unifiers. Full section/version comparison remains owed.
- The same P12 file defines def:p12-ordered-superposition and states thm:p12-superposition-completeness with simplification order, negative selection, eligible inferences, redundancy and fair saturation. It cites BachmairGanzinger2001 and NieuwenhuisRubio2001. This is an actual component lead for C02/C07/C27, with a cited rather than newly proved status. It cannot be credited to all three complete chapter presentations without their separate content comparisons.
- P9 logic-in-computer-science.tex contains def:p09-ctl, def:p09-ctl-labelling and proved thm:p09-ctl-labelling on finite total structures, with explicit predecessor maps, least/greatest fixed points and O((|S|+|R|)|A|) complexity. This supplies a precise current finite-CTL algorithm component to compare with C24's basic-model-checking section. It does not complete C24's second-order languages, transformations, symbolic methods, partial-order reductions, bounded model checking, abstraction or compositionality.
- P12 interactive-proof.tex explicitly defines the PTS/lambda-cube specification and an LCF theorem-type boundary. These are bounded current constructions, not evidence that C17's LF encodings/adequacy or C18's entire dependent-type proof-assistant presentation is written. LCF and LF must not be identified by name similarity.

No source-specific P7 or P8 chapter equivalence was established in this block. Their candidate destinations above retain their full component obligations. No title-only link is recorded as a completed mapping.

## Continuation required for CAT-01

1. Refine the 2,932 mixed artifact parents by their actual acquired byte type, complete emitter grammar and acquisition/derivation joins. Use the existing original-row archive and membership receipts, not a new full-catalog scan. Do not turn the diagnostic substring counters into metadata dispositions.
2. Produce complete family receipts for artifact identity/decoding records, access outcomes, JSON/XML/HTML representations and PDF/raster descriptors. Preserve original content-bearing text, encoding fragments and unresolved strings separately from metadata.
3. Join all 19 PDF presentations and the original PostScript/gzip bodies to chapter, draft, mirror, failure or mismatch identities. Retain duplicate locators and byte-equal captures; compare versions before semantic equivalence.
4. Resolve authorship-array discrepancies and extracted glyph errors against original title pages and chapter bodies. Crossref includes additional contributor names in some arrays; the raw arrays remain intact.
5. Freeze the 28 proposed chapter packets into actual intellectual subunits after full body reading, retaining the six Crossref paratext leads, volume-one index, both publisher manifestations and legacy identifier candidates.
6. Add only source-backed component correspondences to the existing catalog mechanism. Current stated/cited/proved manuscript statuses remain distinct, and no record count becomes a completion percentage.
7. Submit semantic dispositions and membership evidence through the existing reviewed reconciliation/admission mechanism. This note changes none of those records and does not declare CAT-01 complete.

The reference-repair task's durable handoff is separately saved at spec/research/edition-2026-active-reference-repairs.md. Research skill instructions governed primary producer/source reading and this single findings note. The initial long extractor write failed before a file was created; the saved extractor then required the Windows-compatible CSV field-size bound. No historical data was modified during either correction.
