# Current important source holdings and exact-source gaps

Snapshot: 2026-09-07, approximately 06:54 UTC. This is a bounded local inventory for the manuscript completion audit. The machine-readable companion is [source-holdings.json](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/source-holdings.json), containing 16 source or source-family records and all 26 files whose names end in `.pdf` but whose recorded headers are not PDF headers.

## What the inventory establishes

The current metadata inventory records **468 physical files with PDF headers**. That is a file count, not a count of unique works, complete books, exact required editions, sources read, or source-fidelity approvals. It includes copies, extracts, and other PDF artifacts. This pass used `source-and-pdf-files.csv`, filtered rows of `workspace-files.csv`, the inventory summary, narrowly selected acquisition/research notes, and small prefix reads of the 26 suspect files. It did not read every PDF or certify a source collection.

Each source record distinguishes physical file presence, exact bibliographic identity, recorded reading scope, manuscript use, and source-fidelity review. Reading an acquisition note establishes what that note reports; it does not constitute a new full reading of the source. Historical acquisition statuses are retained as evidence and reconciled with later records where possible.

## Principal exact-source findings

| Required or used source | Current holding and inspected scope | Manuscript consequence and remaining work |
| --- | --- | --- |
| Thatcher–Wright 1968, *Generalized Finite Automata Theory with an Application to a Decision Problem of Second-Order Logic*, DOI 10.1007/BF01691346, pp. 57–81 | Latest bounded acquisition report records no exact article PDF. A real 89-page Thatcher 1965 dissertation PDF is held; it is a different work. RC-1713 remains a bibliographic lead. | The live exact-source boundary is **N-c-015**, not N-c-016: `handbook/parts/p09/presentations/n-c-015.tex:489–500`. Modern finite-tree/MSO/WSkS proofs do not establish fidelity to the missing article. Exact article acquisition and reading remain unresolved. |
| McMillan, *Symbolic Model Checking*, revised Kluwer book, 1993 | `tmp/pdfs/p09-mcmillan-1993/thesis.pdf` is a genuine 214-page **May 1992 CMU thesis**, not the revised 1993 book. | `n-c-017.tex:1627–1639` explicitly retains this distinction. Book-specific SMV syntax, algorithms, examples, and proofs still need the revised book's body for exact-source verification. |
| *The Description Logic Handbook*, first edition, 2003 | The exact full first-edition body is not established by the selected holdings and source records. Front matter and later-edition information do not supply it. | The live boundary is `n-c-009.tex:806–812`, with the development distinction at 840–842. Exact 2003 rule, blocking, and proof fidelity remains unverified. |
| Baader–Horrocks–Lutz–Sattler, *An Introduction to Description Logic*, 2017 | Full required chapters are not recorded as acquired/read. Held alternatives include Baader's 2017/2018 Chapter 5 slides, a 2007 author draft of the separately published 2008 handbook chapter, and Donini–Massacci 2000. Their relevant portions have separate source notes. | `n-c-009.tex:814–842` distinguishes the missing exact book surfaces from the independent modern ALC proofs. The source gap does **not** mean the current ALC upper/lower-bound development is absent. |
| Clarke–Grumberg–Peled, *Model Checking*, 1999 | The live source boundary records no complete exact book body; this bounded local pass did not identify a newly acquired exact copy. | `n-c-016.tex:1610–1620` remains the evidence for this source requirement. No renewed external search was performed. |
| Baier–Katoen, *Principles of Model Checking*, 2008 | A genuine 994-page published-book PDF is held at `tmp/pdfs/baier-katoen-2008.pdf`. The source note records relevant Chapter 6 CTL/CTL* surfaces read and page-matched. | Supports the separate N-c-016.e development. It does not fill the Clarke–Grumberg–Peled 1999 exact-edition requirement. A full 994-page reading is not claimed. |
| Mac Lane–Moerdijk, *Sheaves in Geometry and Logic*, 1992 | A genuine 638-page scan is held at `tmp/pdfs/p10-topos/mac-lane-moerdijk-sheaves-in-geometry-and-logic-institutional.pdf`; title/copyright pages identify 1992. Relevant I §§4, 6, 8–9; III §8; IV §§8–9; and VI §§5–7 passages have recorded body-level inspections. | The presheaf development uses this correctly identified source. Recorded reviews cover the stated passages and the corresponding local proofs; they do not assert a whole-book reading. No acquisition gap remains for those inspected passages. |
| Adámek–Rosický–Vitale, *Algebraic Theories*, published 2011 | A real 252-page **1 February 2010 author draft** is held at `tmp/pdfs/p10-lawvere/adamek-rosicky-vitale-gab-cup2-author.pdf`. Its pagination differs from the published 2011 book. Relevant §§1, 11, and 13 have been inspected. | Current Lawvere development identifies `AdamekRosickyVitale2010Draft` separately. Exact published-2011 body and locator verification remain unestablished. |
| Pitts categorical-logic manuscript | The held 95-page author manuscript is dated **18 May 1995**, report UCAM-CL-TR-367. Relevant context-category, lambda, and hyperdoctrine passages were inspected. | Current developments use `Pitts1995Draft`. The eventual handbook chapter is a different manifestation; its exact body is not silently credited as read. |
| Riehl, *Category Theory in Context* | The held author PDF is the **299-page second edition online text**, not the 2016 first edition. The toolkit's cited portions have recorded source verification. | Current key `Riehl2026ContextOnline` distinguishes the online version. No unverified printed publication date is assigned to this edition. |

Exact note paths and line locators, physical byte sizes, and per-record remaining actions are in the JSON. Particularly relevant records are `p09-thatcher-wright-download-search-status-2026-09-06.md:7`, `p09-n-c-017-mcmillan-acquisition-note.md:7`, `p09-alc-general-tbox-source-verification-2026-09-06.md:7`, `p10-presheaf-topos-source-note-2026-09-06.md:7`, `p10-presheaf-logic-source-verification-2026-09-06.md:7`, and `p10-lawvere-theories-source-note-2026-09-06.md:11`, all under `spec/research/`.

## Other recorded source obligations

The selected categorical source packets do not establish exact body holdings for Mac Lane 1998, Awodey 2010, Lambek 1980, Lambek–Scott 1986, or Johnstone 2002. Separately identified Pitts, Riehl, and Mac Lane–Moerdijk sources support the relevant current constructions. This is a statement about the exact registered source versions, not a conclusion that all associated mathematics is unwritten.

Priestley's original 1970 article body remains unacquired in the source packet. A Priestley 2019 presentation, Bezhanishvili's 2006 thesis, and Esakia's original 1974 article are held as separately identified sources. The modern prime-filter and clopen-upset presentation should retain those actual attributions.

Four historical acquisition-gap families require careful interpretation:

| Historical record | Current evidence and remaining uncertainty |
| --- | --- |
| ACQ-GAP-001, planned *Handbook of Logic in Computer Science* Volume 6 | The plan is documented; a published volume identity, date, ISBN, extent, and body have not been established. Pitts's relocation to another volume does not prove that every planned contribution was absorbed or cancelled. See `spec/research/acquisition-gap-hlics-volume-6-2026-08-13.md:12–18`. |
| ACQ-GAP-002, *Handbook of Boolean Algebras* 1989, Volumes 1–3 | **All three full scans are held**, at `tmp/acquisition/boolean-algebras-volumes/016-monk-author-volume-1.pdf`, `017-monk-author-volume-2.pdf`, and `018-monk-author-volume-3.pdf`. The newer note establishes identities and contents, with limited opening-page inspection. Whole-body technical reading, admission, and reproduction fields remain separate. The older manifest's narrower account is stale. See `spec/research/acquisition-gap-boolean-algebras-volumes-2026-08-14.md:13–35`. |
| ACQ-GAP-003, *Handbook of the History of Logic*, Volumes 1–10 | The newer record contains volume/front-matter/chapter metadata, including 127 chapter entries; it reports no chapter-body retrieval in that pass. The older “no contents” description is therefore stale. Exact technical-body reading and admission remain unverified; this pass does not assert that no unidentified copy could exist elsewhere locally. See `spec/research/acquisition-gap-history-of-logic-volumes-1-10-2026-08-14.md:13–30`. |
| ACQ-GAP-004, maintained online sources SRC042 and SRC052–055 | These need dated version/snapshot evidence tied to each use. The historical open row is not evidence that all files are absent. No online freshness check was performed. See `spec/acquisition-gap-manifest.csv:5`. |

## All 26 misleading PDF filenames

Small prefix reads classified every file listed in `inventory-summary.json` as a non-PDF header. **25 contain HTML; one contains a 19-byte plain-text 404 response.** No file in this group was identified as a damaged PDF.

| Response type identified from prefix | Files |
| --- | ---: |
| “Client Challenge” HTML | 6 |
| “Just a moment...” HTML | 5 |
| Deep Blue repository application HTML | 3 |
| Wayback Machine HTML | 2 |
| Springer “Page Unavailable” HTML | 2 |
| Springer book/chapter landing-page HTML | 5 |
| ScienceDirect HTML | 1 |
| Finnish-language HTML, title not visible in inspected prefix | 1 |
| Plain 404 response: `tmp/src025/kurucz-chapter15.pdf` | 1 |
| **Total** | **26** |

The JSON enumerates every exact path, byte size, classification, and observed title or prefix evidence. Prefix reads were bounded at 8,192 bytes per file. These response artifacts do not count as source PDF holdings; their existence does not prove that a valid copy of the same source is absent elsewhere. No files were renamed, deleted, or replaced.

## Audit limits

This inventory is complete for the supplied list of 26 non-PDF-header filenames and deliberately selective for exact-source obligations. It is not an exhaustive source-by-source body reading, rights certification, bibliography validation, or manuscript acceptance decision. The 468-file header count comes from the current parent inventory; the source identities and reading histories come from the evidence cited per record. No acquisition, external browsing, manuscript editing, tests, builds, rendering, or generator run was performed in this pass. The only authored outputs are this note and its JSON companion.
