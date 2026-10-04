# CAT-01: SRC-037 residual file roles and provenance gaps

Date: 9 September 2026. This follows [the artifact disposition proposal](edition-2026-catalog-src037-artifact-dispositions.md). It concerns the 27 previously unresolved artifact parents and the 23 separately identified missing generation events. All outcomes are construction proposals, with historical records and source bytes preserved.

## Result and boundaries

All 27 residual files now have an identified content role. No file remains untyped merely because its generation event is unknown. Their roles are:

| Residual role | Parents |
| --- | ---: |
| Bibliographic records, publication lists and descriptions/abstracts | 19 |
| Failed intended-target acquisitions: corporate landing page and wrong-work PDF/text | 3 |
| Truncated technical PostScript fragments | 2 |
| Identified garbled text-extraction derivative | 1 |
| Mixed table/diagram extraction derivative | 1 |
| Operational CPython bytecode | 1 |
| Total | 27 |

The 23 assigned generation events remain explicit historical provenance gaps where the retained evidence cannot supply the original invocation or write record. Their content roles are established independently. Nothing in this note infers an execution event from a filename, a filesystem timestamp or a matching title.

The revised complete parent proposal is `tmp/edition-2026-catalog-src037/artifact-dispositions-v4.jsonl`: 1,232 bibliographic/structural/operational parents; 284 failed-acquisition parents; 45 source-content representations or derivatives; and 1,371 visual parents. These still total 2,932. The source-content category includes a known garbled derivative and lossy diagram/table output; the category is not a claim of reliable formula transcription or completed manuscript writing.

The principal source result is a corrected acquisition boundary: the two Maryland files contain only an initial fragment of the declared 115-page report. Prefix removal cannot recover the absent pages. The Encoding PDF, in contrast, is intact as a visually readable 84-page source; a separately identified OCR reading aid has now been produced from those exact pages.

## Inputs and reading method

Inputs are the retained v3 disposition records, complete acquisition files under `tmp/acquisition/src037/`, existing source images, and existing source/derivative manifests. The 7 GB historical catalog was neither opened nor hashed. Earlier receipts and originals remain untouched.

The research skill supplied the primary-source and complete-producer approach. The PDF skill supplied source-page reading and explicit limits for text extraction. Source-only rendering and data processing were authorized for this block. No manuscript file, historical catalog/index/validator/ledger/admission record, review snapshot or shared generator was edited. No independent review, test system or manuscript build/render was run.

For all 20 residual web captures, `residual-reading-01/` preserves complete DOM nodes, text/tail values, attributes, anchor records and visible-text derivatives. The complete visible text comprises 617,052 characters, including citation exports and abstracts. Script/style payloads are preserved in the node records and omitted only from the separate visible-text reading aid. Source instructions, web controls, comments and navigation strings were treated as data.

The page-family construction retains every text node in a typed container or as explicit interstitial material. It does not classify a sampled title and extrapolate to an entire page. `residual-web-family-membership-v1.json` holds all 20 complete families, including 2,609 selected DOM containers. Those containers overlap in some pages and include navigation; they are not a count of papers or intellectual units. `residual-web-interstitial-v1.json` retains every text node outside those selected containers.

The largest repeated source grammars were resolved completely: all 16 Calvanese definition lists consist of exactly 529 ordered title/citation pairs, with no exceptional child sequence; all 238 Pfenning preformatted blocks and all 49 de Rijke preformatted blocks have complete balanced BibTeX roots. Every field, description, title, author, venue and linked locator remains available in its original source or supplemental record. Parsing a bibliography does not read or acquire its cited papers, and no such claim is made here.

## Every remaining web capture

All IDs in the following table have prefix `SRC-037-`. Full paths and original hashes are in the v4 parent records and `residual-reading-01/web-reading-index.json`.

| Parent | Complete returned source role and important qualification |
| --- | --- |
| H064 | Aalto bibliographic record for the **1998** Koblenz working paper, *Fachbericht Informatik* 20-98. The page's citation styles describe that report, rather than the Maryland 1999 report or final 2001 chapter. |
| H072 | Bockmayr's selected bibliography: eight subject groups, all 89 list items, links and qualifications. Its Bockmayr/Weispfenning C12 citation is a source lead, not the chapter's body. |
| H109 | Calvanese bibliography: sixteen topic sections and 529 complete `dt`/`dd` title/citation pairs. All author-name fields, venue fields and links survive. The C23 chapter link remains associated with the already held source; unrelated citations are not automatically new required units. |
| H129 | Clarke bibliography: eight category tables, all 368 rows, citation/format/download cells and bibliographic text outside malformed table boundaries. The page distinguishes thesis, journal/conference publications, invited work, reports, books and contributions. These are publication records, not the linked technical bodies. |
| H148 | Comon chronological bibliography, including 53 list items and all draft/full/abstract link distinctions. Its C14 entry explicitly describes the download as a **draft handbook chapter**, consistent with the held source's 1999 draft presentation. |
| H176 | de Rijke book/chapter list, including all 49 complete BibTeX blocks and surrounding citations, years, author/editor roles and navigation. It contains bibliographic versions and source leads, not the full linked books. |
| H211, H214 | Two retained Nonnengart publication-page captures. Each contains 41 publication records with title, metadata, abstract and links. The abstracts are descriptive intellectual claims attached to their respective papers; they are preserved, not promoted to full proofs. The exact C06 and C21 links remain chapter leads. |
| H1053 | Edinburgh C13 bibliographic record: Alan Bundy, 2001, pp.845–911, plus an accepted-author-manuscript link. Its raw editor spelling **A. Boronkov** is preserved as a metadata discrepancy; the actual volume identifies Andrei Voronkov. |
| H1292 | Geuvers publication list: 115 list items, source-version/correction notices and related bibliographic material. The C18 chapter record is explicit. Notes that particular linked PDFs correct proceedings mistakes are retained with those sources; they do not establish their corrected technical contents here. |
| H1313 | ICCL C08 record: Baader/Snyder, volume I, pp.447–533, exact PostScript link, and the author's **final-version** description. That source claim is preserved separately from file/pagination comparisons and does not merge the Snyder version. |
| H1318 | Liverpool research-output list and full institutional navigation. Every displayed citation, DOI/export occurrence and publication-type label is retained. It includes two differently titled C25 records sharing the same DOI, alongside many other publications. Neither duplicated records nor source-link titles count as full bodies. |
| H1339 | Manchester C26 bibliographic record. Its two named research authors and editor-labelled Robinson/Voronkov presentation differ from the actual chapter's three-author title page. Both representations remain literal. |
| H1366 | The old Elsevier handbook locator returns the corporate homepage, with product descriptions, marketing stories and navigation. This is **failed intended-target acquisition**, despite the successful transport and readable HTML. The corporate material creates no new handbook-source obligation. |
| H1382 | Pfenning generated BibTeX bibliography: all 238 complete preformatted roots, with the `bib2bib`/`bibtex2html` 1.99 statements and every field/comment. Its publication metadata and annotations retain their own source identities. |
| H1387 | Pfenning bibliography sorted by publication type: 103 list containers, with navigation, unpublished/in-preparation/to-appear qualifications and source links. The visible 1999 update statement and separate source comment are retained; neither determines the current validity of all cited publication states. |
| H1497 | Snyder publication list: all 34 list entries and other page text. Its C08 entry incorrectly says *Handbook of Automated Deduction*, Springer, Berlin. That string remains historical metadata. The held chapter and institutional contents establish the corrected handbook/title/imprint, without rewriting the capture. |
| H1519 | TalTech C25 bibliographic record: volume II, pp.1791–1849, bibliography pp.1843–1846 and volume ISBN 0444508120. Volume and whole-set ISBN fields remain distinguishable. |
| H1566 | Maryland item page: CS-TR-4052 / UMIACS-TR-99-48, dated 1999-09-11, named contributors, full abstract and a 628.38 KB PostScript download. The linked payload's truncation is established separately below. |

These source roles close the former uncertainty about what kinds of files were captured. They do not close source-selection, source-version, full-proof or manuscript obligations. In particular, descriptive abstracts remain attributed descriptions, and external linked works remain unacquired until their bodies are actually obtained and read.

## Maryland: exact failure, reversible transformation and missing content

The two originals are `umd-nonmonotonic-api-content-retry-02.body` (H1534) and `umd-nonmonotonic-download-retry-02.body` (H1551). Both are **643,460 bytes**, SHA256 **`e6db20eb7d2374970cdbefd5cb11d677be422561038340e54ede634bcb5c0060`**. Separate locators and parent identities survive their byte equality.

Both retained HTTP exchanges finish with 200 and `Content-Length: 643460`; the repository metadata also reports that byte extent. The download response redirects to the same repository bitstream endpoint as the API capture. Thus the evidence does not support blaming an incomplete local transfer: the retained successful responses delivered the stated resource length. The historical event that introduced the damaged/truncated resource is unknown.

The original bytes begin `>%!PS-Adobe-2.0`. The complete physical-line diagnosis finds 8,810 lines: the first 8,805 begin with one `>` and the last five are blank. Removing precisely that first character from each prefixed line produces a **634,655-byte** PostScript fragment, SHA256 **`99748a16e7e307d17b74dc42a82cd2608e81e1de5d20210cb5d9047bf566fa39`**. The two separately named derivatives are under `residual-reading-01/`, ending `.quote-prefix-removed.ps`. The transformation preserves every other byte and does not assert that missing content has been supplied.

The bare initial `>` is incompatible with the intended PostScript header and explains the immediate syntax failure in the old Ghostscript logs. Both old conversions report `/syntaxerror`, followed by an unrecoverable exit code 1. Their blank one-page PDFs are failed outputs and remain preserved as such.

Removing the quotation prefix exposes a second defect. The header declares `%%Pages: 115`, but the complete retained file has only `%%Page` markers 1 through 7. Pages 1–6 end with their `eop` commands. Page 7 ends mid-paragraph after the words about the difference between Herbrand models, without a page-end command, normal trailer or EOF marker. The text header identifies TeX output dated 23 August 1999 and an Elsevier 1999 draft presentation.

No further conversion was attempted after this full diagnosis: it could only render the surviving fragment, not reconstruct the remaining report. The correct status is **truncated technical source fragment and failed complete-target acquisition**. The exact missing content is the rest of page 7 and the subsequently declared pages, together with the document ending. A complete original report must be acquired through another intact capture or the original authors/repository. Its identity must remain distinct from the 1998 Koblenz working paper and the final 2001 C19 chapter.

`residual-reading-01/maryland-postscript-diagnosis.json` preserves both original hashes, every unprefixed-line ordinal, the deterministic transformation, complete DSC marker list and literal header/tail evidence. The old logs remain under their original acquisition paths.

## Encoding: source remains intact; readable derivative supplied

The source is H181, `derijke-encoding-pdf-retry-02.body`, SHA256 **`a782f28d080ee585f31975545e4509c1afbfb2754921d667f93a0410c0923432`**. The previously garbled text is H183 and remains unchanged.

The full font inventory contains 1,246 page/font occurrences. Every one is Type 3, and none has a `ToUnicode` map. The first page uses generic `/a0` through `/a255` encoding names. This explains why the old extraction presents encoded glyph values rather than the readable words seen on the original pages. It does not imply that the PDF is missing its visual content.

A new reading aid under `encoding-ocr-01/` was produced from **all 84 pages of this exact PDF**, rendered at 150 dpi and read with the installed Tesseract.js 7.0.0 English model. It includes every page image, per-page text, per-page image/text hashes and engine confidence diagnostic. The complete text is:

`tmp/edition-2026-catalog-src037/encoding-ocr-01/complete-84-page-reading-aid.txt`

SHA256: **`f32dd84aaa13771207bb94d04de0f44d72e23ae2ba5069334c5a316d7229d741`**.

The associated original reading receipt has SHA256 `42df0d711a5a563ad58d112ea2b52a750bb7450963016283dc31649b8fbc119c`. `encoding-reading-aid-intake-v1.json` pins the source, engine, font diagnosis, model hash and combined text. The downloaded English traineddata is 5,199,098 bytes, SHA256 `5dc5d8d640a212c9d6184921ba103b186f50e0fed9ee716c53e6b312b400d747`.

The opening prose is substantially readable, including the printed p.1405 introduction and its exact restriction to monotone two-valued nonclassical logics. The last page reaches the printed p.1486 index. OCR still misreads some glyphs, formulas, names and index entries. Engine confidence values range from 49 to 95; those are internal diagnostics, not measured transcription accuracy. A full mathematical reading must consult the original images. This derivative is an aid, not a new source edition, an exact transcription or a substitute for the separate 83-page DFKI version.

## Table ledger: all 22 candidates resolved against actual source pages

H1379 is the complete `pdf-table-extraction-manifest.json`, a derivative produced by `build_pre_note_evidence.py` using `pdfplumber.extract_tables()`. Every one of its 1,261 page records, including empty results, errors if present, tables, rows and null/empty cells, has a preserved source/page disposition in `residual-table-page-dispositions-v1.json`.

All 22 nonempty extraction candidates occur on six pages. The existing source images were read for every one:

| Source and page | Actual source object | Extraction outcome |
| --- | --- | --- |
| pdf-003 physical 6, printed 1640 | Figure 1, Futurebus+ error-scenario diagram | One table-shaped extraction from an event/communication diagram. |
| pdf-003 physical 96, printed 1730 | Figure 23, shift-register circuit for data-bus interfacing | Five candidates extracted from circuit geometry. |
| pdf-019 physical 14, printed 1866 | Figure 1, term DAG | Three candidates extracted from node arrays. |
| pdf-019 physical 16, printed 1868 | Figures 2 and 3, flatterm and Prolog representations | Eleven candidates extracted from pointer/data-structure drawings. |
| pdf-019 physical 58, printed 1910 | Figure 30, flatterm structure | One candidate extracted from a pointer-array drawing. |
| pdf-019 physical 76, printed 1928 | Figure 43(b), an SFA construction cost table, alongside predicates and the SFA | One actual cost-table subfigure, still with lossy extracted cells. |

Twenty-one candidates are diagram/data-structure extractions rather than independent source tables. The final one is a genuine table subfigure whose predicate and automaton context must be preserved. The ledger therefore supplies **lossy source-content derivative evidence**, not 22 new intellectual units or 22 verified mathematical tables. Every actual table cell was read in the complete ledger; source image reading fixes its context. The empty entries for other PDFs do not establish that their source pages contain no tables or mathematics.

The comparison records in `residual-source-figure-comparisons-v1.json` preserve exact source-image hashes and source/physical/printed locators. They introduce no graphics-paper obligation.

## Wrong-work PDF and text

H1348 and H1350 remain the original PDF and extracted text for **Bump Map Shadows for OpenGL Rendering**, **Jan Kautz, Wolfgang Heidrich and Katja Daubert**, **MPI-I-2000-4-001**, February 2000. They have an established source identity and a clear failed-target role: the acquisition did not supply the intended handbook chapter.

The proposal retains their raw IDs, bytes, hash and lineage as evidence of that failure. It creates no new requirement to write about computer graphics and does not discard the captures. Obtaining the actually intended handbook source remains a separate source obligation.

## Bytecode: operational role established without execution

H062 is `__pycache__/build_acquisition_note.cpython-312.pyc`, SHA256 `9a0a26990161e7529f4d050dd154c5d48c64dc8c22b32336e22b73e363139964`. Its magic bytes match the available CPython 3.12 runtime; header flags are zero. The marshalled code object was inspected as data. Its module filename and complete module/function-name sets identify an acquisition-note producer, including the text/JSON/HTML/XML/PDF/image/gzip emitters and note-building functions.

The code object was not executed. A compilation of the held source for comparison was also not executed. The marshalled representations differ, so no exact compiled-source identity is claimed from that comparison. The correct content role is **operational compiled artifact**; the original compile/import invocation and environment remain unestablished. `residual-reading-01/bytecode-data-inspection.json` preserves the exact observations and both comparison hashes. Header time bytes were not promoted to a trustworthy execution date.

## All 23 assigned generation-event gaps

`residual-generation-events-v1.json` enumerates every assigned parent separately, with path, hash, established content role, known producer/relation, precise missing evidence and provenance disposition. The set is:

- H062, compiled acquisition module.
- H067, retained PowerShell failure diagnostic; its message identifies the failed source line, but not the command that captured this text file.
- H068–H071, the four retained acquisition procedures.
- H075–H078, note/evidence/request/overview producer procedures.
- H193, document-renderer derivation procedure.
- H194, document-renderer manifest; its source construction is known from that procedure.
- H1049, DOI request manifest derived from already retained acquisition artifacts.
- H1316 and H1317, linked retry and linked request manifests.
- H1375, H1376 and H1378, overview/contact/PDF extraction manifests.
- H1390 and H1391, primary request manifest and PDF extraction/render procedure.
- H1569 and H1570, retained historical validator procedures, read as data and not run.
- H1571, the complete contact-path list.

All IDs have prefix `SRC-037-`. Known generator source is evidence of how a file can be constructed, not a recovered historical invocation. For each of these 23 files, the remaining evidence need is the original invocation or authored-write receipt, its actual environment and a binding to this output event. The retained acquisition folder has no such complete event record for these items. The proposal preserves that gap instead of inventing an event.

The four earlier loose-layout/inventory joins retain their previous qualification too: exact bytes or complete decoded-line equality establishes a payload relationship, not the old generation event. They were outside the assigned 23-event set and were not silently promoted to fully recovered provenance.

## Source-supported queue changes

`chapter-component-queue-v3.json` preserves the 28 chapter packets and all prior raw identities. Only the following changes were made:

1. C19 now explicitly records the **1998 Koblenz**, **1999 Maryland** and **2001 handbook** identities separately. Its next step requires an intact source; prefix removal is no longer a proposed route to the absent 115-page body.
2. C21's actual 84-page source receives the new OCR reading-aid link and its limitations. Its source identity, 83-page counterpart and full proof obligations remain distinct.
3. C24/C26 receive the six actual source-figure obligations listed above, attached to the relevant existing construction groups.
4. A bounded C24-G00 group records the introductory Futurebus+ model/property/counterexample source example on pp.1637–1641. Its success condition requires the actual states, transitions, property and counterexample trace with the source repair explanation; the diagram alone does not supply it.

The queue now has 60 proposed component groups. It does not assert a final intellectual-unit count, full reading of every technical chapter, new manuscript writing or admission. No author bibliography's unrelated papers were automatically added to the required chapter queue.

## Outputs, reproduction and exact continuation

All supporting paths below are under `tmp/edition-2026-catalog-src037/`.

| Artifact | SHA256 |
| --- | --- |
| artifact-dispositions-v4.jsonl | 31f2a61d37a5bc3499f990d862f7a3d7b126c60298767569fc9877873a394530 |
| residual-disposition-receipt-v1.json | f8b356b151b42e7c3a644c63781d62d496437093948d2103805d4336c2fafba7 |
| residual-web-family-membership-v1.json | 93a8d1d299366713c6450b004b81c5cb94b121132b0ea666284bb6f9247b0548 |
| residual-web-interstitial-v1.json | 2722c014e533692ff062a7c755e1b52e8b49154e042c308a7187aa8d3c7d56d0 |
| residual-bibliography-grammar-v1.json | d155abe8250d491a6ab0c1c179b2163262a0c1308584069bf816e4d68b44b33a |
| residual-table-page-dispositions-v1.json | 4ef31ca22141b86094fcddf1e46141cb3d86a2a5402a14e0e4efbf9de215b243 |
| residual-generation-events-v1.json | c24e7320d4e1ede75c87df954a14c069a68cc36459c00322f8e0983206bbfd15 |
| encoding-reading-aid-intake-v1.json | c9dd9c22d76f5ef1fff3ba10926ee2dc9be02f9641e3f1e77fe27290715c7617 |
| residual-source-figure-comparisons-v1.json | 9f4201a297decbcf02b7ac64fe18e3824001147dbaae5db0d8ac608c46f5ea84 |
| chapter-component-queue-v3.json | df3c56c9eca8745a29d0b1fe5378f212ac545662a2499e07264086378ab362e1 |
| residual-finish-receipt-v1.json | 557d015551190000b80dbb28f0765638fc37780196999c33a0d78ed438acb60f |
| residual-source-comparison-receipt-v1.json | 31cd4a5966f9cae83ff00b69feff56e19c0cfd67f370ebfea041f358d50cb428 |

The supplemental source-processing scripts are `read_residual_sources.py`, `partition_residual_records.py`, `finish_residual_intake.py`, `record_source_comparisons.py` and `ocr_encoding_source.cjs`. They write only uniquely named supplemental artifacts and refuse to overwrite prior outputs. Original acquisition files and prior receipts stay authoritative for their literal data.

The remaining obligations are concrete: recover the missing generation-event records if available, or retain the specified historical gaps; acquire an intact Maryland report and exact required final chapters; read technical chapter versions in full before resolving their component correspondences; check OCR mathematical symbols against the original pages; and complete the later consolidated reconciliation/admission process. The 27 former file-role ambiguities are resolved as proposals. Those separate evidence and writing obligations remain open.
