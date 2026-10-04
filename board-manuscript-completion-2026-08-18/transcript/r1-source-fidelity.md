### F1 [must-fix] [open] Skolem-arithmetic theorem points to the wrong Skolem work
- author: source-fidelity r1
- location: handbook/parts/p05/decidable-arithmetics.tex:42-65; handbook/bib/handbook.bib:951-959
- criterion: C1, "claims and definitions match their cited authorities or explicitly stay at a cited/sketch boundary"
- claim: Both the definition-level history and the decidability theorem cite `Skolem1934`, but that key denotes Skolem's 1934 paper on non-characterizability of the natural-number sequence, not the 1930 arithmetic paper to which the decidability of multiplication-only arithmetic is normally attributed. The current citation therefore does not pin the stated theorem to its claimed source.
- evidence: The local bibliography identifies `Skolem1934` as *Uber die Nicht-charakterisierbarkeit ...* (1934). The authoritative EuDML record gives the same title, date, journal, and pages: https://eudml.org/doc/212717. Cambridge's bibliography for *Metamathematics of First-Order Arithmetic* separately lists Skolem's *Uber einige Satzfunktionen in der Arithmetik* as the 1930 work: https://www.cambridge.org/core/books/metamathematics-of-firstorder-arithmetic/bibliography/A3B2F626505D5BA820BEEFD59D6C1446.
- correction: Add a bibliographically verified record for the 1930 Skolem paper (and, if the complete proof used is later, the exact later proof source), change lines 49 and 61 to that authority, and retain `Skolem1934` only where the 1934 non-characterizability result is actually invoked.

### F2 [must-fix] [open] Presentation-dependent consistency is cited to an unrelated Feferman title
- author: source-fidelity r1
- location: handbook/parts/p05/independence-catalog.tex:78-99; handbook/bib/handbook.bib:3923-3932
- criterion: C1, "claims and definitions match their cited authorities or explicitly stay at a cited/sketch boundary"
- claim: The text attributes the dependence of internal consistency sentences on numbering, axiom predicates, base theories, and derivability conditions to `Feferman1964`, but that key is *Systems of Predicative Analysis*. Feferman's directly relevant primary work on general arithmetization is a different 1960 paper, so the cited key does not support the prose as written.
- evidence: The bibliography's `Feferman1964` record is DOI 10.2307/2269764, *Systems of Predicative Analysis*. The Polish Academy of Sciences journal record identifies Feferman's distinct primary article *Arithmetization of metamathematics in a general setting*, Fundamenta Mathematicae 49 (1960), 35-92, DOI 10.4064/fm-49-1-35-92: https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/49/1/94633/arithmetization-of-metamathematics-in-a-general-setting.
- correction: Replace `Feferman1964` at lines 89 and 99 with a new, verified record for the 1960 arithmetization paper, or narrow the prose to the exact claim actually established in *Systems of Predicative Analysis* and cite a separate authority for presentation dependence.

### F3 [must-fix] [open] Equational completeness is assigned to Birkhoff's 1944 subdirect-union paper
- author: source-fidelity r1
- location: handbook/parts/p10/algebraic-and-categorical-logic.tex:37-59; handbook/bib/handbook.bib:2508-2528
- criterion: C1, "claims and definitions match their cited authorities or explicitly stay at a cited/sketch boundary"
- claim: The equational-completeness theorem uses status `cited=Birkhoff1944`, but the cited 1944 paper is *Subdirect Unions in Universal Algebra*. The primary completeness/HSP source is Birkhoff's 1935 *On the Structure of Abstract Algebras*, already present as `Birkhoff1935`.
- evidence: The local records identify the two works exactly. A Max Planck Institute-hosted account states that Birkhoff's 1935 paper gave the first soundness-and-completeness proof for equational logic and states the same `Sigma models e iff Sigma proves e` theorem: https://pure.mpg.de/rest/items/item_1834965_3/component/file_1857488/content. The primary 1935 DOI is https://doi.org/10.1017/S0305004100013463; the 1944 DOI is https://doi.org/10.1090/S0002-9904-1944-08235-9.
- correction: Change the theorem status to `cited=Birkhoff1935` (retaining Burris-Sankappanavar as the modern proof pointer), and reserve `Birkhoff1944` for the subdirect-representation result.

### F4 [must-fix] [open] The biographical half of the chronology has no source apparatus
- author: source-fidelity r1
- location: handbook/parts/p13/chronology-and-biography.tex:4-8,94-286
- criterion: C1, "claims and definitions match their cited authorities"; invariant I6, "No reader-facing ... uncited external claim may remain"
- claim: The chapter promises an apparatus keyed to primary works, but after the cited chronology ends, all biographical capsules are uncited. This leaves historical claims about Aristotle, Chrysippus, Leibniz, Dedekind, De Morgan, Hilbert, Tarski, and the modern figures without a fetchable authority and makes the primary-source preference uncheckable.
- evidence: Citations occur in the chronology at lines 27-87; no `cite` command occurs anywhere in the capsule sequence at lines 94-286. Several capsule-only subjects (for example Leibniz at 104-107, Dedekind at 133-135, and De Morgan at 114-116) have no source supplied by the chronology rows at all.
- correction: Add at least one primary source where available, otherwise an authoritative historical source, to every capsule or to tightly delimited capsule groups; identify secondary reconstructions explicitly for ancient and fragmentary evidence.

### F5 [must-fix] [open] Master tables assert sourced abbreviations but omit the promised destinations
- author: source-fidelity r1
- location: handbook/parts/p14/master-tables.tex:5-9,23-44,63-76,96-106
- criterion: C1, "claims and definitions match their cited authorities"; C4, "notation, terminology, labels, cross-references, proof statuses, and variants are coherent with the live handbook"
- claim: The apparatus says every row abbreviates a theorem or definition "at the cited destination," yet most decision, strength, and expressive-power rows contain neither a citation nor a destination. Readers cannot verify qualifications such as NL-completeness of 2-CNF, the exact two-variable/guarded-fragment bounds, the large-cardinal ordering, or the LTL/CTL/CTL* comparisons against the source-bearing statement supposedly being abbreviated.
- evidence: Among lines 23-44 only the `ALC` row contains a cross-reference; the remaining rows have no `cite`, `ref`, or label. The strength rows at 63-76 and expressive rows at 96-106 likewise have no source/destination links despite the governing promise at lines 5-9.
- correction: Add an explicit theorem/definition cross-reference or primary/authoritative citation to every substantive row, and remove or weaken any row for which no exact source-bearing destination exists.

### F6 [must-fix] [open] New calculus sheets do not expose their controlling sources
- author: source-fidelity r1
- location: handbook/parts/p14/rule-sheets.tex:4-8,90-100; handbook/registry/calculi/gs5-avron.tex:1-8; handbook/registry/calculi/display-k-wansing.tex:1-14; handbook/registry/calculi/deep-s5-stouppa.tex:1-11; handbook/registry/calculi/labelled-k-negri.tex:1-7
- criterion: C1, "claims and definitions match their cited authorities"; invariant I6, "No reader-facing ... uncited external claim may remain"
- claim: Part XIV says each sheet's surrounding record supplies its controlling citation, but the rendered sheets contain no source field or citation. Source names appearing only in `%` comments are not reader-facing, and body citations elsewhere do not tell a reader at the sheet which exact presentation controls each displayed rule list and side condition.
- evidence: `calculussheet` renders only the title and its third-argument identity text; the four named source-derived sheets above contain no `cite` command. Part XIV renders them via `showcalculus` and gives only three general background sources at line 100, none of which is Avron 1996, Negri 2005, Wansing 1994, or Stouppa 2007.
- correction: Add a reader-facing controlling-source sentence with the exact citation to each registry file (and do the same for every other new sheet derived from a named presentation), so the source travels with the rendered rule surface rather than only with a remote body discussion or source comment.

### F7 [must-fix] [open] All 64 inherited bibliography mappings remain semantically unreviewed
- author: source-fidelity r1
- location: spec/provenance/inherited-bibliography-field-ledger.csv:1-65; spec/provenance/SRC-16803-17196.json:37-67
- criterion: C1, "claims and definitions match their cited authorities"; invariant I5, "Source fidelity, mathematical correctness, static validation, compilation, visual review, AI review, and user acceptance remain separate claims"
- claim: Every ledger row passes the token/year/locator static comparison but every `semantic_field_review` value is still `pending`; the controlling provenance record likewise leaves attribution and independent-source review pending and its destination open/missing. Static field retention therefore has not established that each BibLaTeX reconstruction preserves authorship roles, title/version semantics, publication relationships, or reader-visible meaning.
- evidence: The ledger has exactly 64 data rows; all 64 have `static_field_status=pass` and `semantic_field_review=pending`. `SRC-16803-17196.json` records `status: open/missing`, `attribution: pending`, and `independent_source: pending`. The restoration checker passed source/static identity but expressly reported that independent source review remains pending.
- correction: Perform and record row-by-row semantic review against the retained manual entries and authoritative metadata, resolve any author/editor, edition, container, date, or locator discrepancy, then change each row and the provenance gate individually; do not bulk-promote the static pass.

### F8 [must-fix] [open] The page-furniture reconstruction is not presentation-identical to its source interval
- author: source-fidelity r1
- location: source/formal-logic-reference.tex:49-55; handbook/handbook.sty:148-193; spec/provenance/PRE-00049-00055.json:23-40,87-90
- criterion: C1, "claims and definitions match their cited authorities"; invariant I2, "Exact inherited artifacts remain byte-faithful; editorial additions remain separately identified and do not replace, alias, or upgrade inherited claims"
- claim: The source interval specifies `fancy` page furniture with left `leftmark`, fixed right text "Formal Logic," a centered footer folio, and a 0.4pt head rule. The integrated style instead installs book `headings`, alternating chapter/section marks, header folios, and no reconstructed fixed right text or stated head rule. The provenance record calls this a full reconstruction that must preserve every source use, but also correctly leaves the destination open/missing; it cannot pass exact-presentation review as implemented.
- evidence: The two implementations differ in each named visible component. Byte identity of `handbook/restoration/inherited-00049-00055.tex` only establishes retained authority evidence; the checker does not establish reader-visible equivalence, exactly as its verification boundary reports.
- correction: Either scope an actually equivalent source page style to the inherited presentation, or explicitly reclassify and document this as a non-identical editorial page-style adaptation authorized by the governing one-book design; do not describe the present surface as a preserving reconstruction.

### F9 [must-fix] [open] The printed bibliography does not identify inherited records separately from editorial additions
- author: source-fidelity r1
- location: handbook/main.tex:53-55; handbook/bib/handbook.bib:9-598,599-640; spec/provenance/SRC-16803-17196.json:22-40
- criterion: C4, "notation, terminology, labels, cross-references, proof statuses, and variants are coherent with the live handbook"; invariant I2, "editorial additions remain separately identified"
- claim: The source interval has reader-facing standing and contains 64 inherited records, but `main.tex` prints one unfiltered BibLaTeX bibliography. The source file distinguishes inherited and added blocks only with nonprinting `%` comments, so the rendered reader cannot tell which entries reconstruct the inherited bibliography and which are editorial additions.
- evidence: The 64 mapped records occupy bibliography lines 9-598; line 599 begins an added-source block. `printbibliography` at main line 54 applies no keyword/category filter or annotation, and the provenance reason expressly replaces the manual bibliography with this unified database.
- correction: Keep one book and one backmatter bibliography, but make provenance reader-visible: tag inherited versus editorial entries and print labeled subbibliographies under the single Bibliography chapter, or add an equally explicit per-entry provenance marker. Preserve the 64-row mapping and avoid duplicate printing.

Coverage note:

- Lot 1 — finding-linked: F1-F2. All four files were read and all 16 used citation keys resolve in `handbook.bib`; external source-content checks were completed for the two filed mismatches, not for every remaining theorem citation.
- Lot 2 — finding-linked: F3. The three body files and three short annex files were inspected; all 103 used citation keys resolve. Citation-by-citation external semantic verification beyond the Birkhoff mismatch was not completed in this capped opening round.
- Lot 3 — finding-linked: F4-F5. All three files were inspected and all 84 used citation keys resolve. Individual verification of every chronology date and every uncited table result was not performed because the absence of source pins itself blocks that check.
- Lot 4 — finding-linked: F6. All changed/new paths were enumerated, all 325 used citation keys resolve, all thirteen new/changed registry sheets were read, and their relevant body routes were sampled. Line-by-line external source comparison of every changed Part II/III/VI/VII/VIII/XII file was not checked within the 12-finding opening cap.
- Lot 5 — finding-linked: F7-F9. The 64-row field ledger and all fifteen designated tail/preamble/control provenance records were inspected. All fifteen exact restoration checks passed frozen-authority digest, interval digest, artifact digest, and content-token equality; the ledger has 64 static passes and no missing-substantive-token flags. Semantic field review, rendered bibliography separation, page-furniture equivalence, build, and visual identity are not checked clean and remain finding-linked or explicitly pending as above.
