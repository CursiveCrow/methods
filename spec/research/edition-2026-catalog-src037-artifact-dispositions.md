# CAT-01: SRC-037 artifact dispositions and chapter construction queue

Date: 9 September 2026. Proposed construction dispositions for the complete 2,932 artifact-parent set. This note does not admit a catalog batch or credit manuscript completion.

## Completed extent

Every retained artifact parent has an accounted disposition, its original parent record, raw topic endpoints, actual file path, byte count and hash, and acquisition or derivative evidence where that evidence exists. All 2,932 files are present. Their combined size is 350,602,085 bytes.

The complete ordered producer output was reconstructed in memory for every parent. All 2,457,307 displayed artifact-topic strings agree in order and count with the preserved source-group records; all recorded artifact hashes and manifest hash joins agree with the actual files. This establishes the complete representation family and its membership. It does not establish that every physical line is technical prose, that a bibliography supplies its cited papers, or that a chapter's mathematics has been written or accepted.

The final proposal is `tmp/edition-2026-catalog-src037/artifact-dispositions-v3.jsonl`:

| Proposed artifact disposition | Parents | Associated raw topic records |
| --- | ---: | ---: |
| Technical source text or its retained document representation | 43 | 240,556 |
| Bibliographic, structural or operational metadata | 1,212 | 2,052,640 |
| Failed acquisition or failed derivative evidence | 279 | 19,308 |
| Visual artifact or recorded visual observation | 1,371 | 29,654 |
| Still unresolved mixed material | 27 | 115,149 |
| Total assigned artifact set | 2,932 | 2,457,307 |

These are artifact dispositions. The topic column counts the complete children attached to those artifacts; it is not a semantic assertion that every child of a technical PDF is mathematical content. PDF children contain metadata, page geometry, annotations and image descriptors. The separately identified text derivative holds the extracted prose. Likewise, a technical chapter includes contents, references and indexes. All such material stays associated with its version and raw IDs.

The other SRC-037 families retain the earlier [structural partition](edition-2026-catalog-src037-partition.md). Adding this proposal's artifact children to those earlier non-artifact families accounts for SRC-037's 2,460,146 topic records. Neither number counts intellectual units.

## Authority, inputs and preservation

The [edition contract](../EDITION-2026-CONTRACT.md), especially its historical-record reconciliation, source-version and source-acquisition clauses, governs this proposal. [CAT-01](../EDITION-2026-WORK-PACKAGES.md) requires actual intellectual treatments, complete membership predicates and explicit unresolved candidates. The [first descriptor partition](edition-2026-catalog-first-partition.md) supplies the distinction between an acquisition descriptor and its referenced content. Its [complete-set receipt note](edition-2026-catalog-first-partition-full-set.md) supplies the already completed historical uniqueness evidence.

The pinned historical catalog remains `spec/full-compendium-coverage-manifest.csv`, SHA256 `69d0f7ccb89e9be070366102f958a4034f632088b269a92ee244bfa5b41d55e8`. This block did not reopen or hash that 6,947,214,502-byte catalog. It consumed the earlier exact `src037-original.csv.gz`, the preserved `parents.json`, and actual files under `tmp/acquisition/src037/`.

The compressed archive still preserves the original CSV header and every original SRC-037 row and field. Its SHA256 is `1bdfa12ad5d432770f5b5f5d6ad40aa2cf02b6fdf50d9982e76202a0ce8498bf`. The earlier receipt pins the uncompressed source block to byte interval [524080654,2346007392), with scoped SHA256 `58b60de8cdf92ce5929910af026d73ed93efde21d464a384c8f172316af69912`. The original source descriptor, retrieval dates, locator order, empty child fields and mapping states remain literal.

Only this note and new supporting artifacts were written. Historical acquisition files, the historical catalog, assignment index, validators, canonical ledger, manuscript, review snapshots and admission records were not edited. Python bytecode writes were disabled before importing the retained, main-guarded producer. No acquisition, historical validator, manuscript scanner, test, build or renderer was run.

## Complete producer and lineage construction

The catalog role still comes from `tools/build_coverage_manifest.py`: it serializes headings and bullets and does not determine intellectual content. The immediate producer, `tmp/acquisition/src037/build_acquisition_note.py`, has SHA256 `e1ef31b8e93c1379810b915e4d78d7abee94175aa3eab4c81a65757ac7a38302`. Its entire artifact grammar was read and used directly.

For each artifact, the first child is its exact path/standing/byte-count/SHA256 identity. Subsequent children are emitted according to the actual payload: UTF-8 or reversible Latin-1 physical lines and original terminators; complete JSON pointer/object/array/scalar traversal; complete HTML/XML element, attribute, direct/tail text and table traversal; PDF descriptors; raster metadata; gzip descriptors; or binary edge bytes. The complete original sequence and a reconstruction through these exact emitters have the same newline-framed UTF-8 SHA256 and count for all parents. There was no selection by a sampled title or by the earlier substring counters.

This replay is bounded source-data processing. The original producer's `build_note`, `main` and `validate` functions were not invoked, and no generated historical file was overwritten. `artifact-identities-v1.jsonl` preserves every original identity row with all CSV fields; the original archive preserves every other row. The disposition file preserves every original parent row and its contiguous topic range, and the prior membership file preserves original byte positions.

The actual acquisition procedures and receipt producers were read: `acquire_doi_presentations.ps1`, `acquire_primary_presentations.ps1`, `acquire_linked_presentations.ps1`, `acquire_linked_presentations_retry_02.ps1`, and `build_request_manifest.py`. The exact request sequence has 448 records:

| Request source | Records |
| --- | ---: |
| Initial source-producer sequence | 7 |
| DOI/API/ScienceDirect derived request manifest | 374 |
| Primary request manifest | 41 |
| Linked request manifest | 13 |
| Linked retry manifest | 13 |

Each join keeps the ledger filename, its local sequence, full requested URL, requested Accept value, returned status information, curl outcome, body/header/stderr filenames and explicit retry predecessor. A request's `sequence` is not globally unique, so no join uses it without its ledger. Final HTTP status uses the last HTTP status line, falling back to curl's write-out only when no such lines exist. The complete stored request is retained even if no body file was produced. Request count and failed-artifact count are different quantities.

The derivative producers were read completely: `derive_document_renderers.py`, `render_and_extract_pdfs.py`, `build_visual_overviews.py`, and `build_pre_note_evidence.py`. Their full manifests provide input/output filenames, byte counts, hashes, operation outcomes, PDF identity, physical-page mappings and derivative roles. A failed PostScript conversion remains failed even if it leaves a one-page PDF.

The resulting lineage accounting is:

- 2,905 parents have explicit acquisition, derivative or source/page manifest edges.
- Two additional layout parents have exact byte equality to a manifested derivative; their original generation event is not recorded.
- Two additional image inventories have complete line equality to manifested inventories after explicit BOM/newline decoding; their bytes and generation events remain distinct.
- The remaining 23 have their original identity and operational or unresolved role recorded, but no exact generation event. They include retained procedures, producer manifests, the local failure log, a contact-path list and compiled bytecode. Known producer source is identified here; an execution event is not invented.

The complete lists and all joins are in `artifact-lineages-v1.json` and each final disposition's `lineage_records`, `manifest_hash_evidence`, `semantic_evidence` and `lineage_accounting` fields.

## Defensible completed families

### DOI and publisher metadata

All 34 Crossref item ordinals were followed through all eight actual negotiation formats, for 272 body presentations. The second construction parses every complete body, retaining full fields or nodes in `artifact-semantic-families-v1.json`:

- 34 CSL JSON objects have their actual book-chapter type, keys and exact DOI join recorded.
- 34 BibTeX records are parsed through the entire balanced-brace field grammar, retaining every field and DOI.
- 34 RIS records retain every tagged line, entry boundaries and DOI.
- 34 Turtle documents are parsed through their entire returned subject/predicate/object grammar, including typed/language literals, lists of objects and predicates; all triples and predicates are preserved.
- The 102 RDF/XML, Unixref and Unixsd documents retain complete XML trees and actual namespaces/tags.
- All 34 HTML documents have the `Redirecting` title, empty visible body and exact hidden redirect fields. Their full DOM, scripts, attributes and text remain captured. These are linking-hub navigation responses; the requested chapter body was not acquired by returning them.

The 34 successful Elsevier API `-01` bodies parse as `full-text-retrieval-response` XML with a sole `coredata` child. Every element, attribute and text value was retained. The XML root's name does not turn the bibliographic payload into a full chapter. The other negotiated API/request outcomes keep their own failure dispositions. Actual HTTP success and the requested MIME type are never used alone to claim technical content.

Crossref fields include abstracts and references; those fields remain attached to their original item and raw topic membership. The original five-name Unification author array is retained without rewriting its roles. The separate chapter-title evidence below supplies the role distinction.

The two Open Library edition objects, Library of Congress search response, and Maryland item/bundle responses were read and retained as complete metadata. The Library of Congress object has zero matching search results plus unrelated featured-item navigation; this does not establish the book's absence from the Library of Congress catalog. The Open Library objects report different edition keys, page totals and manifestation data. No title-based work or edition merge was performed.

### Document, visual and operational families

The 19 retained PDFs resolve to 15 technical chapter presentations, an 11-page title/contents presentation, a 23-page mismatched work, and two failed one-page blank outputs. The 15 technical PDFs represent eleven chapter leads and retain multiple versions/locators. Their gzip/PostScript inputs and text derivatives remain distinct artifacts.

The visual family comprises 1,261 page images, 89 contact sheets and 19 overview images, plus the acquired publisher placeholder JPEG and the complete visual-observation ledger. The exact page/contact/overview maps and image hashes remain preserved. The observation producer uses fixed strings about visible marks or blank failed outputs; these do not establish mathematical reading. The acquired JPEG is identified only as the asset at `https://mit-press-new-us.imgix.net/missing-cover.jpg`; no book-cover identity is inferred.

The complete source of the retained operational procedures, including the two historical validation scripts, was read as data. They were not executed. The local `acquire_doi_presentations-run-01-failure.txt` records the failure of PowerShell's `Set-Content -Encoding utf8NoBOM` at line 98; it is not evidence that every earlier HTTP request failed. The later `doi-request-manifest-derived.json` reconstructs the already retained requests.

`visual-contact-sheet-paths.txt` contains the complete ordered 89-path list. Each old absolute path is preserved literally and joined to the corresponding current relative contact path. The manuscript migration did not justify erasing old locator spellings.

The two loose layout files are byte-identical to their corresponding manifested CMU and GBV layout derivatives. The two loose image inventories retain UTF-8 BOMs while the manifested inventories do not. All 291 CMU inventory lines and all 13 GBV inventory lines agree after explicitly decoding that BOM and line separators. The final receipt records both hashes, the byte inequality and the complete line equality; it makes no claim that their original production events coincide.

## Actual chapter versions and bounded writing queue

The earlier institutional contents evidence identifies the 2001 Robinson/Voronkov handbook, its two volumes, 28 numbered chapters and six Crossref paratext records. Elsevier ISBN 9780444508133 and MIT Press ISBN 9780262182232 remain distinct manifestation identifiers. The legacy 0444829490 locator remains unresolved.

`chapter-component-queue-v2.json` preserves all 28 original Crossref objects, their raw seed and parent IDs, all associated artifact parents and 59 proposed bounded component groups for the eleven body-backed chapter leads. These groups are proposed work packages, not a claim that the chapters contain exactly 59 intellectual units. Every group names its actual section/pages, concrete definitions/constructions/proofs owed, and success/failure conditions. Additional units may be required when full body reading freezes each scope.

| Chapter lead and retained PDF versions | Concrete construction groups now queued |
| --- | --- |
| C04, The Inverse Method: pdf-018, 94 pages; H2984/H2986 | Classical signed-sequent inverse calculi and lifting; intuitionistic/modal variants; naming and resolution; path calculi, subsumption and contraction-free decision methods; source limits. |
| C06, Computing Small Clause Normal Forms: pdf-008, 33 pages; H219/H221 | Full standard CNF chain; formula renaming; optimized/strong Skolemization; equality, atom and BDD simplification; exact implementation comparisons. |
| C08, Unification Theory: pdf-011, 89 pages, H1299/H1301; pdf-014, 88 pages, H1502/H1504 | Terms and DAG unification; E-unification types and boundaries; general syntactic methods and narrowing; commutative/monoidal semantic methods; algorithm combination; remaining distinct topics. |
| C10, Equality Reasoning in Sequent-Based Calculi: pdf-017, 96 pages; H2963/H2965 | Equality-free translations and free-variable calculi; simultaneous rigid E-unification; incomplete procedures; tableau paramodulation; equality elimination; intuitionistic/modal regimes; rule appendix. |
| C14, Inductionless Induction: pdf-005, 51 pages; H154/H156 | Formal inductive background; saturation and normal axiomatizations; separate Musser/Huet-Hullot/Jouannaud-Kounalis/Bachmair routes; ground reducibility, test sets and limits. This retained source is a 1999 draft with local Chapter 1 numbering. |
| C17, Logical Frameworks: pdf-004, 87 pages; H134/H136 and byte-equal extra layout H132 | Binding/abstract syntax, judgments and adequacy; framework proof search; both metatheoretic translations and deduction theorem; typed lambda-calculus premises; extensions. This retained source is a 1999 draft with local Chapter 1 numbering. |
| C18, Proof-Assistants Using Dependent Type Systems: pdf-010, 90 pages; H1280/H1282 | Proofs as terms, conversion/equality and subject reduction; higher-order and pure type systems; products/sums/inductive types; proof development and source comparisons. |
| C21, Encoding Two-Valued Nonclassical Logics in Classical Logic: pdf-006, 84 pages, H181/H183; pdf-007, 83 pages, H197/H199 | Consequence-encoding criterion; relational, functional and semifunctional translations; background saturation and rule extraction; indirect, SnS and weak-set encodings. H183's text extraction remains garbled and unresolved. |
| C23, Reasoning in Expressive Description Logics: pdf-001, pdf-002 and pdf-012, each 54 pages; H083/H085, H097/H099, H1327/H1329 | ALCQI knowledge bases and PDL/internalization bridge; unrestricted-model reasoning; finite-model reasoning through inequalities; complex roles, arity and fixpoint boundaries. |
| C24, Model Checking: pdf-003, 156 pages; H115/H117 | Languages/automata and expressiveness; simulation/bisimulation; completeness/decision procedures; global/local/mu-calculus checking; reactive/symbolic systems; partial orders/bounded checking; abstraction/modularity; timed/probabilistic/security extensions. |
| C26, Term Indexing: pdf-019, 112 pages; H3002/H3004 | Retrieval relations, modes and perfect filtering; path/discrimination/adaptive/automata-driven indexes; code/substitution/context trees; unification factoring and multiterm retrieval; AC/variable normalization; source comparisons. |

All abbreviated IDs in this table have prefix `SRC-037-`. PDF source paths, SHA256 values, text paths and complete raw topic endpoints are in the queue. The table records body availability and construction leads, not completed full-source acquisition acceptance or completed proofs.

The 17 other chapter packets remain explicitly present: C01, C02, C03, C05, C07, C09, C11, C12, C13, C15, C16, C19, C20, C22, C25, C27 and C28. Their exact titles, DOI objects, original raw IDs and earlier bounded obligations remain in the queue and prior partition. Sixteen require a verified exact technical body. C19 additionally has the damaged 1999 Maryland candidate described below. Metadata and bibliography links do not close any of those chapters.

### Version and contributor qualifications

Both retained Unification title pages name **Franz Baader and Wayne Snyder as authors** and **Paliath Narendran, Manfred Schmidt-Schauss and Klaus Schulz as second readers**. Raw Crossref item T006 places all five in its author array; that source value is preserved as a conflicting metadata presentation. The actual chapter contributor roles take their evidence from the title pages.

The Snyder introduction is printed p.441 and the ICCL introduction p.447. The respective section 2.1 contents entries are p.444 and p.451. Therefore the introductory six-page difference must not be promoted to a universal pagination offset. Each version's entire actual contents display, section starts and text remain available for a future full comparison. No 88/89-page equivalence was asserted.

The de Rijke 84-page Encoding PDF and DFKI 83-page PostScript-derived PDF remain different versions. The 84-page source's first page was read from the already retained page image because its text extraction is garbled. It identifies Chapter 21, the title, authors Hans Jürgen Ohlbach, Andreas Nonnengart, Maarten de Rijke and Dov M. Gabbay, and second reader Nikolaj Bjørner. The existing 83-page text supplied readable contents/introductory component leads. No new page was rendered, and the unreadable derivative was not counted as reader-usable text.

The author-hosted Calvanese PDF and Manchester mirror have identical complete PDF bytes, SHA256 `25671b0ae3bafea718e5c5a7f3ce61fb89feb36d428420b7ba83517e035be93b`. They retain separate acquisition locators, request records and raw IDs. The PostScript-derived PDF has its own hash and is not merged with them.

The wrongly acquired `mpg-equality-pdf-retry-01.body` is **Bump Map Shadows for OpenGL Rendering**, by **Jan Kautz, Wolfgang Heidrich and Katja Daubert**, report **MPI-I-2000-4-001**, February 2000. Its title page and text were read. It supplies neither an equality chapter nor a proof of the source obligation. The original PDF and its derivative remain unresolved out-of-scope source candidates; they were not deleted or relabelled as a handbook chapter.

The Maryland candidate's original header begins `>%!PS-Adobe-2.0`, declares 115 pages and TeX output dated 23 August 1999. Both acquired paths retain that leading-character corruption. The repository item identifies a 1999-09-11 technical report, CS-TR-4052 / UMIACS-TR-99-48, with the Nonmonotonic Reasoning title and Dix/Furbach/Niemelä contributor data. That is a separate report-version lead, not established byte identity to the 2001 chapter. Its two recorded conversions failed and produced blank one-page files. Repair into a new reading derivative and complete source reading remain owed.

### Exact source-text association and manuscript bridges

`artifact-chapter-associations-v2.jsonl` accounts for all 2,932 parents. DOI/API/ScienceDirect memberships use the actual original Crossref ordinal from the complete request producer; image/text/descriptor associations use explicit PDF lineage. Six paratext ordinals remain separate from numbered chapters. A residual 270 parents have no specific chapter or paratext association; these include whole-work/operational artifacts and unresolved pages. That is an explicit association boundary, not a disposition omission.

`source-text-block-membership-v2.jsonl` preserves 4,214 maximal nonblank text blocks from all 15 chapter PDF text derivatives. Each record gives the actual PDF/version, layout parent, physical-line interval, raw topic endpoints, physical-page interval and content hash. These are unclassified source-text blocks: contents, technical paragraphs, formulas, bibliography and index text all survive. The construction does not call every block technical or claim every block was read. The original complete text is retained at its hashed layout path.

The exact line-to-topic bridge follows the complete emitter: identity, decoding result and decoding descriptor precede physical line 1; line n is topic ordinal `first_topic + 2 + n`. Line terminators and form-feed page boundaries retain their original representation. The preserved archive is authoritative for the literal CSV row and its full field values.

Existing manuscript bridges are limited to the actual LaTeX read during the preceding source block:

- P12 `def:p12-martelli-montanari` and `thm:p12-unification-mgu` are leads for finite syntactic unification only; the cited theorem is not a full C08 source treatment.
- P12 `def:p12-lcf-architecture` and `thm:p12-lcf-boundary` are a related trust architecture, without an LF adequacy equivalence to C17.
- P12 `def:p12-pts-lambda-cube` supplies a definition-level comparison for C18, without the complete source metatheory.
- P9 `def:p09-ctl`, `def:p09-ctl-labelling` and `thm:p09-ctl-labelling`, with `annex:p9.ctl.1`, supply the finite total-Kripke CTL labelling component. They do not cover all of C24.

No new P7/P8 content equivalence or manuscript-completion claim is made. The 59 groups each require a full version-specific reading and an exact active-premise bridge before writing can be counted as supplying their source.

## Exact remaining unresolved parents

The complete final list, with paths and reasons, is `artifact-unresolved-v3.json`. All IDs below have prefix `SRC-037-`.

| Remaining family | Exact parent IDs | Required next construction |
| --- | --- | --- |
| Compiled producer bytecode | H062 | Identify its generation/compiler-source relation without executing it or equating a filename with a source version. |
| Publication, bibliography, book or institutional web pages | H064, H072, H109, H129, H148, H176, H211, H214, H1053, H1292, H1313, H1318, H1339, H1366, H1382, H1387, H1497, H1519, H1566, H2998 | Partition the complete returned page contents into navigation, bibliographic entries, abstracts, technical passages and unresolved items. Keep every distinct linked work/version. Full page-family semantic disposition is still owed. |
| Garbled Encoding extraction | H183 | Recover a faithful new reading derivative or read the actual source pages; retain original bytes and the separate 83-page presentation. |
| Wrong-work PDF and extracted text | H1348, H1350 | Record exact out-of-scope work identity and obtain the actually required equality chapter through its own valid source route. |
| Mixed table extraction ledger | H1379 | Distribute every source/page/table/cell through its complete existing map; preserve chapter cells, contents cells, wrong-work cells and failed-renderer cases separately. |
| Two malformed Maryland PostScript bodies | H1534, H1551 | Preserve the original corruption; construct a named derivative with a justified transformation, then read the entire 115-page declared report and compare to C19. |

There is no claim that the 20 web-page parents are metadata merely because their names contain `publications`, `record` or `bibliography`. Their complete physical/DOM representations were reconstructed, but their complete semantic content remains a separate task. No citation list was promoted to full technical content.

## Durable artifacts and fingerprints

All supporting paths in this section are under `tmp/edition-2026-catalog-src037/`.

| Final or supporting artifact | SHA256 |
| --- | --- |
| artifact-dispositions-v3.jsonl | 76515e9ec946c43fdc7470d99e6809ce85ab229188f03ad62c29fcd00a7e11d0 |
| artifact-disposition-receipt-v3.json | df1d5f21219a5027bbe1861e2ec70044ff2f7391ba9b0a24f584a5c3f1c49a78 |
| artifact-unresolved-v3.json | e1a0a67bf59d224882769171d3caae059b7bd74cdcc3f199be45db387a9e4aae |
| artifact-identities-v1.jsonl | 604fc461a82afc1abd99289746ab2f93257d5718004e2798b68a55d46b7fa36a |
| artifact-lineages-v1.json | f4cf34850c1042b3104757ab07487b0f50576ce72f1e6c3da2d61a716ce9fb3b |
| artifact-semantic-families-v1.json | f041e883ade395277a61cf8164f7e5b048b1dea621e28fd1d174110ea23d6905 |
| artifact-disposition-receipt-v1.json | ada9519c65377f72e9a0573105862b25addc432eb97141a60a534b56c82ad804 |
| artifact-disposition-receipt-v2.json | 347bbbf8a97e2b57ebd75c11674f49f1c5ed2b89f8f4aa08f76658acefb4f4e6 |
| chapter-component-queue-v2.json | 18278d22b75b27fe279a961341cd352c35f08ed61590cd6c3cab5047895d1dfe |
| chapter-component-receipt-v2.json | 28fa6a4e135d172a4c5485201384d95a21519d6a34e108d02646bbf933ea356d |
| artifact-chapter-associations-v2.jsonl | ab10ea5c2ab8b946d10fe2a145edb99f8d31b7278cbc7f1f05b5026385fc9a6d |
| source-text-block-membership-v2.jsonl | d61d7557bfa788d644cf83eabc3528d66ae61ec8d6e94a33af260f5bffdc2319 |

The new source-data construction scripts are `dispose_artifact_parents.py`, `refine_artifact_dispositions.py`, `close_inventory_lineages.py`, and `build_chapter_component_queue.py`. Their hashes are in the corresponding receipts. They refuse to overwrite output files. The chronological construction is: complete source-family reconstruction and lineages; complete negotiated-metadata parsing; explicit two-inventory BOM/line equality; chapter/paragraph associations and bounded component queue. Reruns require deliberately separate output filenames/directories; existing receipts stay preserved.

The first chapter-component receipt is superseded by version 2: an initial accumulator counted empty chapter-version buckets as body-backed leads. The corrected count is eleven, and the actual 28 chapter objects and 15 version records were unchanged. This numerical construction error grants no body availability to the other seventeen chapters. The final disposition is version 3, superseding the intermediate 109- and 29-parent unresolved proposals while preserving them as construction history.

The research skill guided the primary-producer reading and this durable findings note. The PDF skill guided the use of actual retained source content and explicit extraction limits. The existing source page image used for the garbled Encoding title is an identity reading only; no manuscript PDF or source renderer was produced.

The assigned parent set is fully accounted at the proposed-disposition level. Complete semantic resolution of the 27 remaining mixed parents, the exact generation events identified above, full chapter/source-version readings, component authoring and the later consolidated reconciliation/admission process remain open.
