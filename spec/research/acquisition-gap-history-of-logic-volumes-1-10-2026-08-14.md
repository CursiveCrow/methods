# ACQ-GAP-003 evidence — *Handbook of the History of Logic*, Volumes 1–10 — 2026-08-14

- **Book:** *The Methods of Reason*
- **Governed gap:** `ACQ-GAP-003` only
- **Disposition:** **OPEN**
- **Standing:** independent, nonterminal acquisition evidence. This note does not admit a source presentation or packet, fulfill an external-coverage row, establish a right to reproduce chapter bodies, close `ACQ-GAP-003`, or alter any shared ledger.
- **Fresh DBLP response window:** 2026-08-14 09:30:17Z–09:31:24Z
- **Rights-holder contacts:** 0
- **External messages sent:** 0
- **Chapter bodies retrieved:** 0
- **Packets admitted:** 0

## Disposition

Current DBLP metadata establishes a complete, page-ordered chapter-level inventory for Volumes 1–10 of the *Handbook of the History of Logic*. The inventory below contains 145 separately identified DBLP rows: 10 volume editorship records, 8 front-matter records, and 127 chapter records. It preserves 145 unique DBLP keys, 145 canonical DBLP record URLs, 136 unique DOI strings and resolver URLs, and every page range supplied by DBLP. All ten current HTML volume pages and all ten current XML exports contain exactly the same per-volume record sets.

This evidence is not terminal. DBLP states on its volume pages that its metadata is released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/), but that statement applies to DBLP metadata; it does not license Elsevier chapter bodies or other protected expression. No body was acquired, no reproduction basis was established, no presentation packet was independently admitted, and no content item was integrated. The exact governed status therefore remains **`OPEN`**.

The narrow result is:

- Volume 1–10 identities and current DBLP editorship records: **established**;
- complete current DBLP page-order record sets: **established**;
- titles, authors/editors, years, page ranges, DOI strings, DOI URLs, DBLP keys, and DBLP record URLs: **recorded below**;
- retained `web-open-dblp-01.txt` through `web-open-dblp-10.txt` captures: **verified as source-order prefixes, not complete volume captures**;
- Volume 11: **excluded and preserved as the distinct `SRC-062` presentation**;
- lawful reproduction basis for protected chapter-body expression: **not established**;
- independently admitted presentation packets: **none**;
- terminal acquisition-gap resolution: **not justified**;
- exact governed status: **`OPEN`**.

## Evidence boundary and method

The existing rendered DBLP captures under `tmp/acquisition/src063/` were reused only as prior evidence. Their exact bytes, line counts, hashes, and exposed DBLP-key sequences were checked. Fresh HTML volume pages and XML table-of-contents exports were then requested from DBLP’s own Trier mirror, which the canonical DBLP pages expose as their mirror. Canonical DBLP volume pages were also reopened during this investigation to confirm the live presentation and the CC0 statement. The fresh HTML pages supply the displayed DBLP order; the fresh XML exports independently supply complete structured metadata. DBLP record URLs and DOI resolver URLs below use their canonical hosts.

For the request hashes below, the exact hashed UTF-8 bytes are, with one final line feed and no blank line:

```text
GET <exact URL>
Accept: <text/html or application/xml>
User-Agent: The-Methods-of-Reason-acquisition-audit/1.0
```

This explicit representation is necessary because a transport library may add connection-level headers that are not stable. Response hashes are SHA-256 over the exact response-body bytes received. All 20 responses returned HTTP 200 with UTF-8 content types. The response `Date` headers supply the research window above.

Evidence roles remain separate:

| Evidence surface | Establishes here | Does not establish |
|---|---|---|
| Current DBLP HTML volume pages | volume-page heading, page order, displayed metadata, persistent record routes, CC0 metadata notice | XML ordering, publisher-body rights, packet admission |
| Current DBLP XML exports | complete structured field set and per-volume record set | HTML source order or a right to reproduce protected bodies |
| Retained `web-open-dblp-*.txt` captures | earlier rendered page prefixes and historical evidence hashes | complete page contents; 33 current tail records are absent from those captures |
| Canonical DBLP record and DOI URLs | stable metadata and resolver locators | body acquisition, open access, permission, or equivalence among presentations |
| `spec/research/acquisition-src-062.md` | separately governed Volume 11 acquisition evidence | permission to merge Volume 11 into `SRC-063` or this note |

## Counts and invariants

| Measure | Exact result |
|---|---:|
| Volumes in scope | 10 |
| Fresh requests / successful responses | 20 / 20 |
| Fresh HTML response bytes | 1,495,434 |
| Fresh XML response bytes | 80,974 |
| Fresh response bytes, combined | 1,576,408 |
| Ordered DBLP rows | 145 |
| Volume editorship rows | 10 |
| Front-matter rows | 8 |
| Chapter rows | 127 |
| Unique DBLP keys / record URLs | 145 / 145 |
| Rows with DOI / unique DOI strings case-insensitively | 136 / 136 |
| Rows with page ranges | 127 |
| Per-volume HTML/XML record-set equality | 10 / 10 |
| Per-volume HTML/XML order equality | 0 / 10 |
| Retained rendered captures | 10 files; 269,438 bytes; 3,783 LF lines |
| DBLP keys exposed by retained captures | 112 |
| Current tail keys absent from retained captures | 33 |
| Volume 11 rows included here | 0 |

The XML result order differs from the page order in every volume, although the sets agree exactly. Because the gap asks for chapter-level contents and source order, the ledger below follows the HTML page order. XML is used to supply the exact structured field values at each page-ordered key; it is not used to reorder the chapters.

## Volume identity and responsibility

| Vol. | DBLP title | DBLP editorship field | XML year | HTML heading year | Rows | Breakdown |
|---:|---|---|---:|---:|---:|---|
| 1 | Greek, Indian and Arabic Logic | Dov M. Gabbay; John Woods 0001 | 2004 | 2001 | 10 | 1 editorship; 1 front matter; 8 chapters |
| 2 | Mediaeval and Renaissance Logic | Dov M. Gabbay; John Woods 0001 | 2008 | 2008 | 15 | 1 editorship; 1 front matter; 13 chapters |
| 3 | The Rise of Modern Logic: From Leibniz to Frege | Dov M. Gabbay; John Woods 0001 | 2004 | 2004 | 13 | 1 editorship; 1 front matter; 11 chapters |
| 4 | British Logic in the Nineteenth Century | Dov M. Gabbay; John Woods 0001 | 2008 | 2008 | 17 | 1 editorship; 1 front matter; 15 chapters |
| 5 | Logic from Russell to Church | Dov M. Gabbay; John Woods 0001 | 2009 | 2009 | 18 | 1 editorship; 1 front matter; 16 chapters |
| 6 | Sets and Extensions in the Twentieth Century | Dov M. Gabbay; Akihiro Kanamori; John Woods 0001 | 2012 | 2012 | 12 | 1 editorship; 0 front matter; 11 chapters |
| 7 | Logic and the Modalities in the Twentieth Century | Dov M. Gabbay; John Woods 0001 | 2006 | 2006 | 11 | 1 editorship; 1 front matter; 9 chapters |
| 8 | The Many Valued and Nonmonotonic Turn in Logic | Dov M. Gabbay; John Woods 0001 | 2007 | 2007 | 12 | 1 editorship; 1 front matter; 10 chapters |
| 9 | Computational Logic | Jörg H. Siekmann | 2014 | 2014 | 18 | 1 editorship; 1 front matter; 16 chapters |
| 10 | Inductive Logic | Dov M. Gabbay; Stephan Hartmann 0001; John Woods 0001 | 2011 | 2011 | 19 | 1 editorship; 0 front matter; 18 chapters |

DBLP classifies the volume rows as `Editorship`; accordingly, the responsibility names in this table are recorded as editors. DBLP’s XML disambiguation suffixes (for example, `John Woods 0001`) are retained exactly. The HTML display commonly omits those suffixes while retaining them in person metadata; neither form silently replaces the other.

## Complete DBLP page-order metadata ledger

Each row is independently identified. Titles, authors, editor fields, years, pages, and DOI strings use the current XML values. Order follows the current HTML page. A dash means DBLP supplied no value for that field in the XML export. DOI resolver and DBLP record URLs are constructed only from the exact DOI and DBLP key that DBLP supplied; they are locators, not body-access claims.

### Volume 1 — Greek, Indian and Arabic Logic

- Canonical page: `https://dblp.org/db/series/hhl/hhl1.html`
- Fresh raw page: `https://dblp.uni-trier.de/db/series/hhl/hhl1.html`
- Fresh XML export: `https://dblp.uni-trier.de/search/publ/api?format=xml&h=1000&q=toc%3Adb%2Fseries%2Fhhl%2Fhhl1.bht%3A`

| Ord. | Standing | Authors / editors | Exact title | Pages | Year | DOI and resolver URL | DBLP key and record URL |
|---:|---|---|---|---|---:|---|---|
| 1 | volume editorship | Dov M. Gabbay; John Woods 0001 | Greek, Indian and Arabic Logic | — | 2004 | — | `series/hhl/1`<br>`https://dblp.org/rec/series/hhl/1` |
| 2 | front matter | Dov M. Gabbay; John Woods 0001 | Preface. | — | 2001 | `10.1016/S1874-5857(04)80001-3`<br>`https://doi.org/10.1016/S1874-5857(04)80001-3` | `series/hhl/GabbayW01`<br>`https://dblp.org/rec/series/hhl/GabbayW01` |
| 3 | chapter | Julius Moravcsik | Logic before Aristotle: Development or birth? | 1-25 | 2001 | `10.1016/S1874-5857(04)80003-7`<br>`https://doi.org/10.1016/S1874-5857(04)80003-7` | `series/hhl/Moravcsik01`<br>`https://dblp.org/rec/series/hhl/Moravcsik01` |
| 4 | chapter | John Hayden Woods; Andrew Irvine | Aristotle's early logic. | 27-99 | 2001 | `10.1016/S1874-5857(04)80004-9`<br>`https://doi.org/10.1016/S1874-5857(04)80004-9` | `series/hhl/WoodsI01`<br>`https://dblp.org/rec/series/hhl/WoodsI01` |
| 5 | chapter | George Boger | Aristotle's underlying logic. | 101-246 | 2001 | `10.1016/S1874-5857(04)80005-0`<br>`https://doi.org/10.1016/S1874-5857(04)80005-0` | `series/hhl/Boger01`<br>`https://dblp.org/rec/series/hhl/Boger01` |
| 6 | chapter | Fred Johnson | Aristotle's modal syllogisms. | 247-307 | 2001 | `10.1016/S1874-5857(04)80006-2`<br>`https://doi.org/10.1016/S1874-5857(04)80006-2` | `series/hhl/Johnson01`<br>`https://dblp.org/rec/series/hhl/Johnson01` |
| 7 | chapter | Jonardon Ganeri | Indian logic. | 309-395 | 2001 | `10.1016/S1874-5857(04)80007-4`<br>`https://doi.org/10.1016/S1874-5857(04)80007-4` | `series/hhl/Ganeri01`<br>`https://dblp.org/rec/series/hhl/Ganeri01` |
| 8 | chapter | Robert R. O'Toole; Raymond E. Jennings | The megarians and the stoics. | 397-522 | 2001 | `10.1016/S1874-5857(04)80008-6`<br>`https://doi.org/10.1016/S1874-5857(04)80008-6` | `series/hhl/OTooleJ01`<br>`https://dblp.org/rec/series/hhl/OTooleJ01` |
| 9 | chapter | Tony Street | Arabic logic. | 523-596 | 2001 | `10.1016/S1874-5857(04)80009-8`<br>`https://doi.org/10.1016/S1874-5857(04)80009-8` | `series/hhl/Street01`<br>`https://dblp.org/rec/series/hhl/Street01` |
| 10 | chapter | Charles Burnett | The translation of arabic works on logic into latin in the middle ages and the renaissance. | 597-606 | 2001 | `10.1016/S1874-5857(04)80010-4`<br>`https://doi.org/10.1016/S1874-5857(04)80010-4` | `series/hhl/Burnett01`<br>`https://dblp.org/rec/series/hhl/Burnett01` |

### Volume 2 — Mediaeval and Renaissance Logic

- Canonical page: `https://dblp.org/db/series/hhl/hhl2.html`
- Fresh raw page: `https://dblp.uni-trier.de/db/series/hhl/hhl2.html`
- Fresh XML export: `https://dblp.uni-trier.de/search/publ/api?format=xml&h=1000&q=toc%3Adb%2Fseries%2Fhhl%2Fhhl2.bht%3A`

| Ord. | Standing | Authors / editors | Exact title | Pages | Year | DOI and resolver URL | DBLP key and record URL |
|---:|---|---|---|---|---:|---|---|
| 1 | volume editorship | Dov M. Gabbay; John Woods 0001 | Mediaeval and Renaissance Logic | — | 2008 | — | `series/hhl/2`<br>`https://dblp.org/rec/series/hhl/2` |
| 2 | front matter | Dov M. Gabbay; John Woods 0001 | Preface. | — | 2008 | `10.1016/S1874-5857(08)80020-9`<br>`https://doi.org/10.1016/S1874-5857(08)80020-9` | `series/hhl/GabbayW08a`<br>`https://dblp.org/rec/series/hhl/GabbayW08a` |
| 3 | chapter | John Marenbon | The Latin Tradition of Logic to 1100. | 1-63 | 2008 | `10.1016/S1874-5857(08)80022-2`<br>`https://doi.org/10.1016/S1874-5857(08)80022-2` | `series/hhl/Marenbon08`<br>`https://dblp.org/rec/series/hhl/Marenbon08` |
| 4 | chapter | John Marenbon | Logic at the Turn of the Twelfth Century. | 65-81 | 2008 | `10.1016/S1874-5857(08)80023-4`<br>`https://doi.org/10.1016/S1874-5857(08)80023-4` | `series/hhl/Marenbon08a`<br>`https://dblp.org/rec/series/hhl/Marenbon08a` |
| 5 | chapter | Ian Wilks | Peter Abelard and his Contemporaries. | 83-156 | 2008 | `10.1016/S1874-5857(08)80024-6`<br>`https://doi.org/10.1016/S1874-5857(08)80024-6` | `series/hhl/Wilks08`<br>`https://dblp.org/rec/series/hhl/Wilks08` |
| 6 | chapter | Terence Parsons | The development of supposition theory in the later 12th through 14th centuries. | 157-280 | 2008 | `10.1016/S1874-5857(08)80025-8`<br>`https://doi.org/10.1016/S1874-5857(08)80025-8` | `series/hhl/Parsons08`<br>`https://dblp.org/rec/series/hhl/Parsons08` |
| 7 | chapter | Henrik Lagerlund | The Assimilation of Aristotelian and Arabic Logic up to the Later Thirteenth Century. | 281-346 | 2008 | `10.1016/S1874-5857(08)80026-X`<br>`https://doi.org/10.1016/S1874-5857(08)80026-X` | `series/hhl/Lagerlund08`<br>`https://dblp.org/rec/series/hhl/Lagerlund08` |
| 8 | chapter | Ria van der Lecq | Logic and theories of meaning in the late 13th and early 14th century including the modistae. | 347-388 | 2008 | `10.1016/S1874-5857(08)80027-1`<br>`https://doi.org/10.1016/S1874-5857(08)80027-1` | `series/hhl/Lecq08`<br>`https://dblp.org/rec/series/hhl/Lecq08` |
| 9 | chapter | Gyula Klima | The nominalist semantics of Ockham and Buridan: A "rational reconstruction". | 389-431 | 2008 | `10.1016/S1874-5857(08)80028-3`<br>`https://doi.org/10.1016/S1874-5857(08)80028-3` | `series/hhl/Klima08`<br>`https://dblp.org/rec/series/hhl/Klima08` |
| 10 | chapter | Catarina Dutilh Novaes | Logic in the 14th century after Ockham. | 433-504 | 2008 | `10.1016/S1874-5857(08)80029-5`<br>`https://doi.org/10.1016/S1874-5857(08)80029-5` | `series/hhl/Novaes08`<br>`https://dblp.org/rec/series/hhl/Novaes08` |
| 11 | chapter | Simo Knuuttila | Medieval Modal Theories and Modal Logic. | 505-578 | 2008 | `10.1016/S1874-5857(08)80030-1`<br>`https://doi.org/10.1016/S1874-5857(08)80030-1` | `series/hhl/Knuuttila08`<br>`https://dblp.org/rec/series/hhl/Knuuttila08` |
| 12 | chapter | Mikko Yrjönsuuri | Treatments of the paradoxes of self-reference. | 579-608 | 2008 | `10.1016/S1874-5857(08)80031-3`<br>`https://doi.org/10.1016/S1874-5857(08)80031-3` | `series/hhl/Yrjonsuuri08`<br>`https://dblp.org/rec/series/hhl/Yrjonsuuri08` |
| 13 | chapter | Earline Jennifer Ashworth | Developments in the Fifteenth and Sixteenth Centuries. | 609-643 | 2008 | `10.1016/S1874-5857(08)80032-5`<br>`https://doi.org/10.1016/S1874-5857(08)80032-5` | `series/hhl/Ashworth08`<br>`https://dblp.org/rec/series/hhl/Ashworth08` |
| 14 | chapter | Petr Dvorak | Relational Logic of Juan Caramuel. | 645-665 | 2008 | `10.1016/S1874-5857(08)80033-7`<br>`https://doi.org/10.1016/S1874-5857(08)80033-7` | `series/hhl/Dvorak08`<br>`https://dblp.org/rec/series/hhl/Dvorak08` |
| 15 | chapter | Russell Wahl | Port Royal: The Stirrings of Modernity. | 667-699 | 2008 | `10.1016/S1874-5857(08)80034-9`<br>`https://doi.org/10.1016/S1874-5857(08)80034-9` | `series/hhl/Wahl08`<br>`https://dblp.org/rec/series/hhl/Wahl08` |

### Volume 3 — The Rise of Modern Logic: From Leibniz to Frege

- Canonical page: `https://dblp.org/db/series/hhl/hhl3.html`
- Fresh raw page: `https://dblp.uni-trier.de/db/series/hhl/hhl3.html`
- Fresh XML export: `https://dblp.uni-trier.de/search/publ/api?format=xml&h=1000&q=toc%3Adb%2Fseries%2Fhhl%2Fhhl3.bht%3A`

| Ord. | Standing | Authors / editors | Exact title | Pages | Year | DOI and resolver URL | DBLP key and record URL |
|---:|---|---|---|---|---:|---|---|
| 1 | volume editorship | Dov M. Gabbay; John Woods 0001 | The Rise of Modern Logic: From Leibniz to Frege | — | 2004 | — | `series/hhl/3`<br>`https://dblp.org/rec/series/hhl/3` |
| 2 | front matter | Dov M. Gabbay; John Woods 0001 | Preface. | — | 2004 | `10.1016/S1874-5857(04)80012-8`<br>`https://doi.org/10.1016/S1874-5857(04)80012-8` | `series/hhl/GabbayW04`<br>`https://dblp.org/rec/series/hhl/GabbayW04` |
| 3 | chapter | Wolfgang Lenzen | Leibniz's logic. | 1-83 | 2004 | `10.1016/S1874-5857(04)80014-1`<br>`https://doi.org/10.1016/S1874-5857(04)80014-1` | `series/hhl/Lenzen04`<br>`https://dblp.org/rec/series/hhl/Lenzen04` |
| 4 | chapter | Mary Tiles | Kant: From general to transcendental logic. | 85-130 | 2004 | `10.1016/S1874-5857(04)80015-3`<br>`https://doi.org/10.1016/S1874-5857(04)80015-3` | `series/hhl/Tiles04`<br>`https://dblp.org/rec/series/hhl/Tiles04` |
| 5 | chapter | John W. Burbidge | Hegel's logic. | 131-175 | 2004 | `10.1016/S1874-5857(04)80016-5`<br>`https://doi.org/10.1016/S1874-5857(04)80016-5` | `series/hhl/Burbidge04`<br>`https://dblp.org/rec/series/hhl/Burbidge04` |
| 6 | chapter | Paul Rusnock; Rolf George | Bolzano as logician. | 177-205 | 2004 | `10.1016/S1874-5857(04)80017-7`<br>`https://doi.org/10.1016/S1874-5857(04)80017-7` | `series/hhl/RusnockG04`<br>`https://dblp.org/rec/series/hhl/RusnockG04` |
| 7 | chapter | Richard Tieszen | Husserl's logic. | 207-321 | 2004 | `10.1016/S1874-5857(04)80018-9`<br>`https://doi.org/10.1016/S1874-5857(04)80018-9` | `series/hhl/Tieszen04`<br>`https://dblp.org/rec/series/hhl/Tieszen04` |
| 8 | chapter | Theodore Hailperin | Algebraical logic 1685-1900. | 323-388 | 2004 | `10.1016/S1874-5857(04)80019-0`<br>`https://doi.org/10.1016/S1874-5857(04)80019-0` | `series/hhl/Hailperin04`<br>`https://dblp.org/rec/series/hhl/Hailperin04` |
| 9 | chapter | Victor Sánchez Valencia | The algebra of logic. | 389-544 | 2004 | `10.1016/S1874-5857(04)80020-7`<br>`https://doi.org/10.1016/S1874-5857(04)80020-7` | `series/hhl/Valencia04`<br>`https://dblp.org/rec/series/hhl/Valencia04` |
| 10 | chapter | Ivor Grattan-Guinness | The mathematical turns in logic. | 545-556 | 2004 | `10.1016/S1874-5857(04)80021-9`<br>`https://doi.org/10.1016/S1874-5857(04)80021-9` | `series/hhl/Grattan-Guinness04`<br>`https://dblp.org/rec/series/hhl/Grattan-Guinness04` |
| 11 | chapter | Volker Peckhaus | Schröder's logic. | 557-609 | 2004 | `10.1016/S1874-5857(04)80022-0`<br>`https://doi.org/10.1016/S1874-5857(04)80022-0` | `series/hhl/Peckhaus04`<br>`https://dblp.org/rec/series/hhl/Peckhaus04` |
| 12 | chapter | Risto Hilpinen | Peirce's logic. | 611-658 | 2004 | `10.1016/S1874-5857(04)80023-2`<br>`https://doi.org/10.1016/S1874-5857(04)80023-2` | `series/hhl/Hilpinen04`<br>`https://dblp.org/rec/series/hhl/Hilpinen04` |
| 13 | chapter | Peter M. Sullivan | Frege's logic. | 659-750 | 2004 | `10.1016/S1874-5857(04)80024-4`<br>`https://doi.org/10.1016/S1874-5857(04)80024-4` | `series/hhl/Sullivan04`<br>`https://dblp.org/rec/series/hhl/Sullivan04` |

### Volume 4 — British Logic in the Nineteenth Century

- Canonical page: `https://dblp.org/db/series/hhl/hhl4.html`
- Fresh raw page: `https://dblp.uni-trier.de/db/series/hhl/hhl4.html`
- Fresh XML export: `https://dblp.uni-trier.de/search/publ/api?format=xml&h=1000&q=toc%3Adb%2Fseries%2Fhhl%2Fhhl4.bht%3A`

| Ord. | Standing | Authors / editors | Exact title | Pages | Year | DOI and resolver URL | DBLP key and record URL |
|---:|---|---|---|---|---:|---|---|
| 1 | volume editorship | Dov M. Gabbay; John Woods 0001 | British Logic in the Nineteenth Century | — | 2008 | — | `series/hhl/4`<br>`https://dblp.org/rec/series/hhl/4` |
| 2 | front matter | Dov M. Gabbay; John Woods 0001 | Preface. | — | 2008 | `10.1016/S1874-5857(08)80002-7`<br>`https://doi.org/10.1016/S1874-5857(08)80002-7` | `series/hhl/GabbayW08`<br>`https://dblp.org/rec/series/hhl/GabbayW08` |
| 3 | chapter | Gordon R. McOuat; Charissa S. Varma | Bentham's logic. | 1-32 | 2008 | `10.1016/S1874-5857(08)80004-0`<br>`https://doi.org/10.1016/S1874-5857(08)80004-0` | `series/hhl/McOuatV08`<br>`https://dblp.org/rec/series/hhl/McOuatV08` |
| 4 | chapter | Tim Milnes | Coleridge's logic. | 33-74 | 2008 | `10.1016/S1874-5857(08)80005-2`<br>`https://doi.org/10.1016/S1874-5857(08)80005-2` | `series/hhl/Milnes08`<br>`https://dblp.org/rec/series/hhl/Milnes08` |
| 5 | chapter | James W. van Evra | Richard Whately and logical theory. | 75-91 | 2008 | `10.1016/S1874-5857(08)80006-4`<br>`https://doi.org/10.1016/S1874-5857(08)80006-4` | `series/hhl/Evra08`<br>`https://dblp.org/rec/series/hhl/Evra08` |
| 6 | chapter | Ralph Jessop | The logic of sir William Hamilton: Tunnelling through sand to place the keystone in the aristotelic arch. | 93-162 | 2008 | `10.1016/S1874-5857(08)80007-6`<br>`https://doi.org/10.1016/S1874-5857(08)80007-6` | `series/hhl/Jessop08`<br>`https://dblp.org/rec/series/hhl/Jessop08` |
| 7 | chapter | Laura J. Snyder | "The whole box of tools": William Whewell and the logic of induction. | 163-228 | 2008 | `10.1016/S1874-5857(08)80008-8`<br>`https://doi.org/10.1016/S1874-5857(08)80008-8` | `series/hhl/Snyder08`<br>`https://dblp.org/rec/series/hhl/Snyder08` |
| 8 | chapter | Fred Wilson | The logic of John Stuart Mill. | 229-281 | 2008 | `10.1016/S1874-5857(08)80009-X`<br>`https://doi.org/10.1016/S1874-5857(08)80009-X` | `series/hhl/Wilson08`<br>`https://dblp.org/rec/series/hhl/Wilson08` |
| 9 | chapter | Michael E. Hobart; Joan L. Richards | De Morgan's logic. | 283-329 | 2008 | `10.1016/S1874-5857(08)80010-6`<br>`https://doi.org/10.1016/S1874-5857(08)80010-6` | `series/hhl/HobartR08`<br>`https://dblp.org/rec/series/hhl/HobartR08` |
| 10 | chapter | Dale Jacquette | Boole's logic. | 331-379 | 2008 | `10.1016/S1874-5857(08)80011-8`<br>`https://doi.org/10.1016/S1874-5857(08)80011-8` | `series/hhl/Jacquette08`<br>`https://dblp.org/rec/series/hhl/Jacquette08` |
| 11 | chapter | Maria Panteki | French 'logique' and British 'logic': On the origins of augustus de Morgan's early logical inquiries, 1805-1835. | 381-456 | 2008 | `10.1016/S1874-5857(08)80012-X`<br>`https://doi.org/10.1016/S1874-5857(08)80012-X` | `series/hhl/Panteki08`<br>`https://dblp.org/rec/series/hhl/Panteki08` |
| 12 | chapter | Amirouche Moktefi | Lewis Carroll's logic. | 457-505 | 2008 | `10.1016/S1874-5857(08)80013-1`<br>`https://doi.org/10.1016/S1874-5857(08)80013-1` | `series/hhl/Moktefi08`<br>`https://dblp.org/rec/series/hhl/Moktefi08` |
| 13 | chapter | James W. van Evra | John Venn and logical theory. | 507-513 | 2008 | `10.1016/S1874-5857(08)80014-3`<br>`https://doi.org/10.1016/S1874-5857(08)80014-3` | `series/hhl/Evra08a`<br>`https://dblp.org/rec/series/hhl/Evra08a` |
| 14 | chapter | Bert Mosselmans; Ard Van Moer | William Stanley Jevons and the substitution of similars. | 515-531 | 2008 | `10.1016/S1874-5857(08)80015-5`<br>`https://doi.org/10.1016/S1874-5857(08)80015-5` | `series/hhl/MosselmansM08`<br>`https://dblp.org/rec/series/hhl/MosselmansM08` |
| 15 | chapter | Shahid Rahman; Juan Redmond | Hugh Maccoll and the birth of logical pluralism. | 533-604 | 2008 | `10.1016/S1874-5857(08)80016-7`<br>`https://doi.org/10.1016/S1874-5857(08)80016-7` | `series/hhl/RahmanR08`<br>`https://dblp.org/rec/series/hhl/RahmanR08` |
| 16 | chapter | David Sullivan | The Idealists. | 605-661 | 2008 | `10.1016/S1874-5857(08)80017-9`<br>`https://doi.org/10.1016/S1874-5857(08)80017-9` | `series/hhl/Sullivan08`<br>`https://dblp.org/rec/series/hhl/Sullivan08` |
| 17 | chapter | William J. Mander | Bradley's logic. | 663-717 | 2008 | `10.1016/S1874-5857(08)80018-0`<br>`https://doi.org/10.1016/S1874-5857(08)80018-0` | `series/hhl/Mander08`<br>`https://dblp.org/rec/series/hhl/Mander08` |

### Volume 5 — Logic from Russell to Church

- Canonical page: `https://dblp.org/db/series/hhl/hhl5.html`
- Fresh raw page: `https://dblp.uni-trier.de/db/series/hhl/hhl5.html`
- Fresh XML export: `https://dblp.uni-trier.de/search/publ/api?format=xml&h=1000&q=toc%3Adb%2Fseries%2Fhhl%2Fhhl5.bht%3A`

| Ord. | Standing | Authors / editors | Exact title | Pages | Year | DOI and resolver URL | DBLP key and record URL |
|---:|---|---|---|---|---:|---|---|
| 1 | volume editorship | Dov M. Gabbay; John Woods 0001 | Logic from Russell to Church | — | 2009 | — | `series/hhl/5`<br>`https://dblp.org/rec/series/hhl/5` |
| 2 | front matter | Dov M. Gabbay; John Woods 0001 | Preface. | — | 2009 | `10.1016/S1874-5857(09)70003-2`<br>`https://doi.org/10.1016/S1874-5857(09)70003-2` | `series/hhl/GabbayW09`<br>`https://dblp.org/rec/series/hhl/GabbayW09` |
| 3 | chapter | Andrew David Irvine | Bertrand Russell's Logic. | 1-28 | 2009 | `10.1016/S1874-5857(09)70005-6`<br>`https://doi.org/10.1016/S1874-5857(09)70005-6` | `series/hhl/Irvine09`<br>`https://dblp.org/rec/series/hhl/Irvine09` |
| 4 | chapter | Dale Jacquette | Logic for Meinongian Object Theory Semantics. | 29-76 | 2009 | `10.1016/S1874-5857(09)70006-8`<br>`https://doi.org/10.1016/S1874-5857(09)70006-8` | `series/hhl/Jacquette09`<br>`https://dblp.org/rec/series/hhl/Jacquette09` |
| 5 | chapter | Joan Rand Moschovakis | The Logic of Brouwer and Heyting. | 77-125 | 2009 | `10.1016/S1874-5857(09)70007-X`<br>`https://doi.org/10.1016/S1874-5857(09)70007-X` | `series/hhl/Moschovakis09`<br>`https://dblp.org/rec/series/hhl/Moschovakis09` |
| 6 | chapter | Jens Erik Fenstad; Hao Wang 0001 | Thoralf Albert Skolem. | 127-194 | 2009 | `10.1016/S1874-5857(09)70008-1`<br>`https://doi.org/10.1016/S1874-5857(09)70008-1` | `series/hhl/FenstadW09`<br>`https://dblp.org/rec/series/hhl/FenstadW09` |
| 7 | chapter | Claus-Peter Wirth; Jörg H. Siekmann; Christoph Benzmüller; Serge Autexier | Jacques Herbrand: Life, Logic, and Automated Deduction. | 195-254 | 2009 | `10.1016/S1874-5857(09)70009-3`<br>`https://doi.org/10.1016/S1874-5857(09)70009-3` | `series/hhl/WirthSBA09`<br>`https://dblp.org/rec/series/hhl/WirthSBA09` |
| 8 | chapter | Michael Potter | The Logic of The Tractatus. | 255-304 | 2009 | `10.1016/S1874-5857(09)70010-X`<br>`https://doi.org/10.1016/S1874-5857(09)70010-X` | `series/hhl/Potter09`<br>`https://dblp.org/rec/series/hhl/Potter09` |
| 9 | chapter | Peter M. Simons | Leśniewski's Logic. | 305-320 | 2009 | `10.1016/S1874-5857(09)70011-1`<br>`https://doi.org/10.1016/S1874-5857(09)70011-1` | `series/hhl/Simons09`<br>`https://dblp.org/rec/series/hhl/Simons09` |
| 10 | chapter | Wilfried Sieg | Hilbert's Proof Theory. | 321-384 | 2009 | `10.1016/S1874-5857(09)70012-3`<br>`https://doi.org/10.1016/S1874-5857(09)70012-3` | `series/hhl/Sieg09`<br>`https://dblp.org/rec/series/hhl/Sieg09` |
| 11 | chapter | Barry Hartley Slater | Hilbert's Epsilon Calculus and its Successors. | 385-448 | 2009 | `10.1016/S1874-5857(09)70013-5`<br>`https://doi.org/10.1016/S1874-5857(09)70013-5` | `series/hhl/Slater09`<br>`https://dblp.org/rec/series/hhl/Slater09` |
| 12 | chapter | Mark van Atten; Juliette Kennedy | Gödel's Logic. | 449-509 | 2009 | `10.1016/S1874-5857(09)70014-7`<br>`https://doi.org/10.1016/S1874-5857(09)70014-7` | `series/hhl/AttenK09`<br>`https://dblp.org/rec/series/hhl/AttenK09` |
| 13 | chapter | Keith Simmons | Tarski's Logic. | 511-616 | 2009 | `10.1016/S1874-5857(09)70015-9`<br>`https://doi.org/10.1016/S1874-5857(09)70015-9` | `series/hhl/Simmons09`<br>`https://dblp.org/rec/series/hhl/Simmons09` |
| 14 | chapter | Alasdair Urquhart | Emil Post. | 617-666 | 2009 | `10.1016/S1874-5857(09)70016-0`<br>`https://doi.org/10.1016/S1874-5857(09)70016-0` | `series/hhl/Urquhart09`<br>`https://dblp.org/rec/series/hhl/Urquhart09` |
| 15 | chapter | Jan von Plato | Gentzen's Logic. | 667-721 | 2009 | `10.1016/S1874-5857(09)70017-2`<br>`https://doi.org/10.1016/S1874-5857(09)70017-2` | `series/hhl/Plato09`<br>`https://dblp.org/rec/series/hhl/Plato09` |
| 16 | chapter | Felice Cardone; J. Roger Hindley | Lambda-Calculus and Combinators in the 20th Century. | 723-817 | 2009 | `10.1016/S1874-5857(09)70018-4`<br>`https://doi.org/10.1016/S1874-5857(09)70018-4` | `series/hhl/CardoneH09`<br>`https://dblp.org/rec/series/hhl/CardoneH09` |
| 17 | chapter | Jonathan P. Seldin | The Logic of Church and Curry. | 819-873 | 2009 | `10.1016/S1874-5857(09)70019-6`<br>`https://doi.org/10.1016/S1874-5857(09)70019-6` | `series/hhl/Seldin09`<br>`https://dblp.org/rec/series/hhl/Seldin09` |
| 18 | chapter | Andrea Cantini | Paradoxes, Self-Reference and Truth in the 20th Century. | 875-1013 | 2009 | `10.1016/S1874-5857(09)70020-2`<br>`https://doi.org/10.1016/S1874-5857(09)70020-2` | `series/hhl/Cantini09`<br>`https://dblp.org/rec/series/hhl/Cantini09` |

### Volume 6 — Sets and Extensions in the Twentieth Century

- Canonical page: `https://dblp.org/db/series/hhl/hhl6.html`
- Fresh raw page: `https://dblp.uni-trier.de/db/series/hhl/hhl6.html`
- Fresh XML export: `https://dblp.uni-trier.de/search/publ/api?format=xml&h=1000&q=toc%3Adb%2Fseries%2Fhhl%2Fhhl6.bht%3A`

| Ord. | Standing | Authors / editors | Exact title | Pages | Year | DOI and resolver URL | DBLP key and record URL |
|---:|---|---|---|---|---:|---|---|
| 1 | volume editorship | Dov M. Gabbay; Akihiro Kanamori; John Woods 0001 | Sets and Extensions in the Twentieth Century | — | 2012 | — | `series/hhl/6`<br>`https://dblp.org/rec/series/hhl/6` |
| 2 | chapter | Akihiro Kanamori | Set Theory from Cantor to Cohen. | 1-71 | 2012 | `10.1016/B978-0-444-51621-3.50001-3`<br>`https://doi.org/10.1016/B978-0-444-51621-3.50001-3` | `series/hhl/Kanamori12`<br>`https://dblp.org/rec/series/hhl/Kanamori12` |
| 3 | chapter | Juris Steprans | History of the Continuum in the 20th Century. | 73-144 | 2012 | `10.1016/B978-0-444-51621-3.50002-5`<br>`https://doi.org/10.1016/B978-0-444-51621-3.50002-5` | `series/hhl/Steprans12`<br>`https://dblp.org/rec/series/hhl/Steprans12` |
| 4 | chapter | Jean A. Larson | Infinite Combinatorics. | 145-357 | 2012 | `10.1016/B978-0-444-51621-3.50003-7`<br>`https://doi.org/10.1016/B978-0-444-51621-3.50003-7` | `series/hhl/Larson12`<br>`https://dblp.org/rec/series/hhl/Larson12` |
| 5 | chapter | Akihiro Kanamori | Large Cardinals with Forcing. | 359-413 | 2012 | `10.1016/B978-0-444-51621-3.50004-9`<br>`https://doi.org/10.1016/B978-0-444-51621-3.50004-9` | `series/hhl/Kanamori12a`<br>`https://dblp.org/rec/series/hhl/Kanamori12a` |
| 6 | chapter | William J. Mitchell 0002 | Inner Models for Large Cardinals. | 415-456 | 2012 | `10.1016/B978-0-444-51621-3.50005-0`<br>`https://doi.org/10.1016/B978-0-444-51621-3.50005-0` | `series/hhl/Mitchell12`<br>`https://dblp.org/rec/series/hhl/Mitchell12` |
| 7 | chapter | Paul B. Larson | A Brief History of Determinacy. | 457-507 | 2012 | `10.1016/B978-0-444-51621-3.50006-2`<br>`https://doi.org/10.1016/B978-0-444-51621-3.50006-2` | `series/hhl/Larson12a`<br>`https://dblp.org/rec/series/hhl/Larson12a` |
| 8 | chapter | Menachem Kojman | Singular Cardinals: From Hausdorff's Gaps to Shelah's PCF Theory. | 509-558 | 2012 | `10.1016/B978-0-444-51621-3.50007-4`<br>`https://doi.org/10.1016/B978-0-444-51621-3.50007-4` | `series/hhl/Kojman12`<br>`https://dblp.org/rec/series/hhl/Kojman12` |
| 9 | chapter | M. Randall Holmes; Thomas E. Forster; Thierry Libert | Alternative Set Theories. | 559-632 | 2012 | `10.1016/B978-0-444-51621-3.50008-6`<br>`https://doi.org/10.1016/B978-0-444-51621-3.50008-6` | `series/hhl/HolmesFL12`<br>`https://dblp.org/rec/series/hhl/HolmesFL12` |
| 10 | chapter | John L. Bell | Types, Sets, and Categories. | 633-687 | 2012 | `10.1016/B978-0-444-51621-3.50009-8`<br>`https://doi.org/10.1016/B978-0-444-51621-3.50009-8` | `series/hhl/Bell12`<br>`https://dblp.org/rec/series/hhl/Bell12` |
| 11 | chapter | Jean-Pierre Marquis; Gonzalo E. Reyes | The History of Categorical Logic: 1963-1977. | 689-800 | 2012 | `10.1016/B978-0-444-51621-3.50010-4`<br>`https://doi.org/10.1016/B978-0-444-51621-3.50010-4` | `series/hhl/MarquisR12`<br>`https://dblp.org/rec/series/hhl/MarquisR12` |
| 12 | chapter | Fairouz Kamareddine; Twan Laan; Robert L. Constable | Russell's Orders in Kripke's Theory of Truth and Computational Type Theory. | 801-845 | 2012 | `10.1016/B978-0-444-51621-3.50011-6`<br>`https://doi.org/10.1016/B978-0-444-51621-3.50011-6` | `series/hhl/KamareddineLC12`<br>`https://dblp.org/rec/series/hhl/KamareddineLC12` |

### Volume 7 — Logic and the Modalities in the Twentieth Century

- Canonical page: `https://dblp.org/db/series/hhl/hhl7.html`
- Fresh raw page: `https://dblp.uni-trier.de/db/series/hhl/hhl7.html`
- Fresh XML export: `https://dblp.uni-trier.de/search/publ/api?format=xml&h=1000&q=toc%3Adb%2Fseries%2Fhhl%2Fhhl7.bht%3A`

| Ord. | Standing | Authors / editors | Exact title | Pages | Year | DOI and resolver URL | DBLP key and record URL |
|---:|---|---|---|---|---:|---|---|
| 1 | volume editorship | Dov M. Gabbay; John Woods 0001 | Logic and the Modalities in the Twentieth Century | — | 2006 | — | `series/hhl/7`<br>`https://dblp.org/rec/series/hhl/7` |
| 2 | front matter | Dov M. Gabbay; John Woods 0001 | Preface. | — | 2006 | `10.1016/S1874-5857(06)80025-7`<br>`https://doi.org/10.1016/S1874-5857(06)80025-7` | `series/hhl/GabbayW06`<br>`https://dblp.org/rec/series/hhl/GabbayW06` |
| 3 | chapter | Robert Goldblatt | Mathematical modal logic: A view of its evolution. | 1-98 | 2006 | `10.1016/S1874-5857(06)80027-0`<br>`https://doi.org/10.1016/S1874-5857(06)80027-0` | `series/hhl/Goldblatt06`<br>`https://dblp.org/rec/series/hhl/Goldblatt06` |
| 4 | chapter | Paul Gochet; E. Pascal Gribomont | Epistemic logic. | 99-195 | 2006 | `10.1016/S1874-5857(06)80028-2`<br>`https://doi.org/10.1016/S1874-5857(06)80028-2` | `series/hhl/GochetG06`<br>`https://dblp.org/rec/series/hhl/GochetG06` |
| 5 | chapter | Paul McNamara | Deontic logic. | 197-288 | 2006 | `10.1016/S1874-5857(06)80029-4`<br>`https://doi.org/10.1016/S1874-5857(06)80029-4` | `series/hhl/McNamara06`<br>`https://dblp.org/rec/series/hhl/McNamara06` |
| 6 | chapter | Greg Restall | Relevant and substructural logics. | 289-398 | 2006 | `10.1016/S1874-5857(06)80030-0`<br>`https://doi.org/10.1016/S1874-5857(06)80030-0` | `series/hhl/Restall06`<br>`https://dblp.org/rec/series/hhl/Restall06` |
| 7 | chapter | Peter Øhrstrøm; Per F. V. Hasle | A.N. Prior's logic. | 399-446 | 2006 | `10.1016/S1874-5857(06)80031-2`<br>`https://doi.org/10.1016/S1874-5857(06)80031-2` | `series/hhl/OhrstromH06`<br>`https://dblp.org/rec/series/hhl/OhrstromH06` |
| 8 | chapter | Peter Øhrstrøm; Per F. V. Hasle | Modern temporal logic: The philosophical background. | 447-498 | 2006 | `10.1016/S1874-5857(06)80032-4`<br>`https://doi.org/10.1016/S1874-5857(06)80032-4` | `series/hhl/OhrstromH06a`<br>`https://dblp.org/rec/series/hhl/OhrstromH06a` |
| 9 | chapter | Jan van Eijck; Martin Stokhof | The gamut of dynamic logics. | 499-600 | 2006 | `10.1016/S1874-5857(06)80033-6`<br>`https://doi.org/10.1016/S1874-5857(06)80033-6` | `series/hhl/EijckS06`<br>`https://dblp.org/rec/series/hhl/EijckS06` |
| 10 | chapter | Keith Devlin | Situation theory and situation semantics. | 601-664 | 2006 | `10.1016/S1874-5857(06)80034-8`<br>`https://doi.org/10.1016/S1874-5857(06)80034-8` | `series/hhl/Devlin06`<br>`https://dblp.org/rec/series/hhl/Devlin06` |
| 11 | chapter | Erik C. W. Krabbe | Dialogue logic. | 665-704 | 2006 | `10.1016/S1874-5857(06)80035-X`<br>`https://doi.org/10.1016/S1874-5857(06)80035-X` | `series/hhl/Krabbe06`<br>`https://dblp.org/rec/series/hhl/Krabbe06` |

### Volume 8 — The Many Valued and Nonmonotonic Turn in Logic

- Canonical page: `https://dblp.org/db/series/hhl/hhl8.html`
- Fresh raw page: `https://dblp.uni-trier.de/db/series/hhl/hhl8.html`
- Fresh XML export: `https://dblp.uni-trier.de/search/publ/api?format=xml&h=1000&q=toc%3Adb%2Fseries%2Fhhl%2Fhhl8.bht%3A`

| Ord. | Standing | Authors / editors | Exact title | Pages | Year | DOI and resolver URL | DBLP key and record URL |
|---:|---|---|---|---|---:|---|---|
| 1 | volume editorship | Dov M. Gabbay; John Woods 0001 | The Many Valued and Nonmonotonic Turn in Logic | — | 2007 | — | `series/hhl/8`<br>`https://dblp.org/rec/series/hhl/8` |
| 2 | front matter | Dov M. Gabbay; John Woods 0001 | Preface. | — | 2007 | `10.1016/S1874-5857(07)80002-1`<br>`https://doi.org/10.1016/S1874-5857(07)80002-1` | `series/hhl/GabbayW07`<br>`https://dblp.org/rec/series/hhl/GabbayW07` |
| 3 | chapter | Grzegorz Malinowski | Many-valued logic and its philosophy. | 13-94 | 2007 | `10.1016/S1874-5857(07)80004-5`<br>`https://doi.org/10.1016/S1874-5857(07)80004-5` | `series/hhl/Malinowski07`<br>`https://dblp.org/rec/series/hhl/Malinowski07` |
| 4 | chapter | Bryson Brown | Preservationism: a short history. | 95-127 | 2007 | `10.1016/S1874-5857(07)80005-7`<br>`https://doi.org/10.1016/S1874-5857(07)80005-7` | `series/hhl/Brown07`<br>`https://dblp.org/rec/series/hhl/Brown07` |
| 5 | chapter | Graham Priest | Paraconsistency and dialetheism. | 129-204 | 2007 | `10.1016/S1874-5857(07)80006-9`<br>`https://doi.org/10.1016/S1874-5857(07)80006-9` | `series/hhl/Priest07`<br>`https://dblp.org/rec/series/hhl/Priest07` |
| 6 | chapter | Maria Luisa Dalla Chiara; Roberto Giuntini; Miklós Rédei | The history of quantum logic. | 205-283 | 2007 | `10.1016/S1874-5857(07)80007-0`<br>`https://doi.org/10.1016/S1874-5857(07)80007-0` | `series/hhl/ChiaraGR07`<br>`https://dblp.org/rec/series/hhl/ChiaraGR07` |
| 7 | chapter | Dominic Hyde | Logics of vagueness. | 285-324 | 2007 | `10.1016/S1874-5857(07)80008-2`<br>`https://doi.org/10.1016/S1874-5857(07)80008-2` | `series/hhl/Hyde07`<br>`https://dblp.org/rec/series/hhl/Hyde07` |
| 8 | chapter | Didier Dubois; Francesc Esteva; Lluís Godo; Henri Prade | Fuzzy-set based logics - an history-oriented presentation of their main developments. | 325-449 | 2007 | `10.1016/S1874-5857(07)80009-4`<br>`https://doi.org/10.1016/S1874-5857(07)80009-4` | `series/hhl/DuboisEGP07`<br>`https://dblp.org/rec/series/hhl/DuboisEGP07` |
| 9 | chapter | Karl Schlechta | Nonmonotonic logics: a preferential approach. | 451-516 | 2007 | `10.1016/S1874-5857(07)80010-0`<br>`https://doi.org/10.1016/S1874-5857(07)80010-0` | `series/hhl/Schlechta07`<br>`https://dblp.org/rec/series/hhl/Schlechta07` |
| 10 | chapter | Grigoris Antoniou; Kewen Wang 0001 | Default logic. | 517-555 | 2007 | `10.1016/S1874-5857(07)80011-2`<br>`https://doi.org/10.1016/S1874-5857(07)80011-2` | `series/hhl/AntoniouW07`<br>`https://dblp.org/rec/series/hhl/AntoniouW07` |
| 11 | chapter | Alexander Bochman | Nonmonotonic reasoning. | 557-632 | 2007 | `10.1016/S1874-5857(07)80012-4`<br>`https://doi.org/10.1016/S1874-5857(07)80012-4` | `series/hhl/Bochman07`<br>`https://dblp.org/rec/series/hhl/Bochman07` |
| 12 | chapter | Carl J. Posy | Free logics. | 633-680 | 2007 | `10.1016/S1874-5857(07)80013-6`<br>`https://doi.org/10.1016/S1874-5857(07)80013-6` | `series/hhl/Posy07`<br>`https://dblp.org/rec/series/hhl/Posy07` |

### Volume 9 — Computational Logic

- Canonical page: `https://dblp.org/db/series/hhl/hhl9.html`
- Fresh raw page: `https://dblp.uni-trier.de/db/series/hhl/hhl9.html`
- Fresh XML export: `https://dblp.uni-trier.de/search/publ/api?format=xml&h=1000&q=toc%3Adb%2Fseries%2Fhhl%2Fhhl9.bht%3A`

| Ord. | Standing | Authors / editors | Exact title | Pages | Year | DOI and resolver URL | DBLP key and record URL |
|---:|---|---|---|---|---:|---|---|
| 1 | volume editorship | Jörg H. Siekmann | Computational Logic | — | 2014 | — | `series/hhl/9`<br>`https://dblp.org/rec/series/hhl/9` |
| 2 | front matter | Jörg H. Siekmann; Dov M. Gabbay | Editorial Note. | — | 2014 | `10.1016/B978-0-444-51624-4.50019-8`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50019-8` | `series/hhl/SiekmannG14`<br>`https://dblp.org/rec/series/hhl/SiekmannG14` |
| 3 | chapter | Jörg H. Siekmann | Computational Logic. | 15-30 | 2014 | `10.1016/B978-0-444-51624-4.50001-0`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50001-0` | `series/hhl/Siekmann14`<br>`https://dblp.org/rec/series/hhl/Siekmann14` |
| 4 | chapter | Martin Davis | Logic and the development of the computer. | 31-38 | 2014 | `10.1016/B978-0-444-51624-4.50002-2`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50002-2` | `series/hhl/Davis14`<br>`https://dblp.org/rec/series/hhl/Davis14` |
| 5 | chapter | Dov M. Gabbay | What is a logical system? An evolutionary view: 1964-2014. | 41-132 | 2014 | `10.1016/B978-0-444-51624-4.50003-4`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50003-4` | `series/hhl/Gabbay14`<br>`https://dblp.org/rec/series/hhl/Gabbay14` |
| 6 | chapter | John Harrison 0001; Josef Urban; Freek Wiedijk | History of Interactive Theorem Proving. | 135-214 | 2014 | `10.1016/B978-0-444-51624-4.50004-6`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50004-6` | `series/hhl/HarrisonUW14`<br>`https://dblp.org/rec/series/hhl/HarrisonUW14` |
| 7 | chapter | Christoph Benzmüller; Dale Miller 0001 | Automation of Higher-Order Logic. | 215-254 | 2014 | `10.1016/B978-0-444-51624-4.50005-8`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50005-8` | `series/hhl/BenzmullerM14`<br>`https://dblp.org/rec/series/hhl/BenzmullerM14` |
| 8 | chapter | Claude Kirchner; Hélène Kirchner | Equational Logic and Rewriting. | 255-282 | 2014 | `10.1016/B978-0-444-51624-4.50006-X`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50006-X` | `series/hhl/KirchnerK14`<br>`https://dblp.org/rec/series/hhl/KirchnerK14` |
| 9 | chapter | Didier Dubois; Henri Prade | Possibilistic Logic - An Overview. | 283-342 | 2014 | `10.1016/B978-0-444-51624-4.50007-1`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50007-1` | `series/hhl/DuboisP14`<br>`https://dblp.org/rec/series/hhl/DuboisP14` |
| 10 | chapter | Fairouz Kamareddine; Joe B. Wells; Christoph Zengler; Henk Barendregt | Computerising Mathematical Text. | 343-396 | 2014 | `10.1016/B978-0-444-51624-4.50008-3`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50008-3` | `series/hhl/KamareddineWZB14`<br>`https://dblp.org/rec/series/hhl/KamareddineWZB14` |
| 11 | chapter | Jos C. M. Baeten; Davide Sangiorgi | Concurrency Theory: A Historical Perspective on Coinduction and Process Calculi. | 399-442 | 2014 | `10.1016/B978-0-444-51624-4.50009-5`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50009-5` | `series/hhl/BaetenS14`<br>`https://dblp.org/rec/series/hhl/BaetenS14` |
| 12 | chapter | Klaus Ambos-Spies; Peter A. Fejer | Degrees of Unsolvability. | 443-494 | 2014 | `10.1016/B978-0-444-51624-4.50010-1`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50010-1` | `series/hhl/Ambos-SpiesF14`<br>`https://dblp.org/rec/series/hhl/Ambos-SpiesF14` |
| 13 | chapter | Lance Fortnow; Steven Homer | Computational Complexity. | 495-521 | 2014 | `10.1016/B978-0-444-51624-4.50011-3`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50011-3` | `series/hhl/FortnowH14`<br>`https://dblp.org/rec/series/hhl/FortnowH14` |
| 14 | chapter | Robert A. Kowalski | Logic Programming. | 523-569 | 2014 | `10.1016/B978-0-444-51624-4.50012-5`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50012-5` | `series/hhl/Kowalski14`<br>`https://dblp.org/rec/series/hhl/Kowalski14` |
| 15 | chapter | Jack Minker; Dietmar Seipel; Carlo Zaniolo | Logic and Databases: A History of Deductive Databases. | 571-627 | 2014 | `10.1016/B978-0-444-51624-4.50013-7`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50013-7` | `series/hhl/MinkerSZ14`<br>`https://dblp.org/rec/series/hhl/MinkerSZ14` |
| 16 | chapter | John-Jules Ch. Meyer | Logics for Intelligent Agents and Multi-Agent Systems. | 629-658 | 2014 | `10.1016/B978-0-444-51624-4.50014-9`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50014-9` | `series/hhl/Meyer14`<br>`https://dblp.org/rec/series/hhl/Meyer14` |
| 17 | chapter | Matthias Knorr 0001; Pascal Hitzler | Description Logics. | 659-678 | 2014 | `10.1016/B978-0-444-51624-4.50015-0`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50015-0` | `series/hhl/KnorrH14`<br>`https://dblp.org/rec/series/hhl/KnorrH14` |
| 18 | chapter | Pascal Hitzler; Jens Lehmann 0001; Axel Polleres | Logics for the Semantic Web. | 679-710 | 2014 | `10.1016/B978-0-444-51624-4.50016-2`<br>`https://doi.org/10.1016/B978-0-444-51624-4.50016-2` | `series/hhl/HitzlerLP14`<br>`https://dblp.org/rec/series/hhl/HitzlerLP14` |

### Volume 10 — Inductive Logic

- Canonical page: `https://dblp.org/db/series/hhl/hhl10.html`
- Fresh raw page: `https://dblp.uni-trier.de/db/series/hhl/hhl10.html`
- Fresh XML export: `https://dblp.uni-trier.de/search/publ/api?format=xml&h=1000&q=toc%3Adb%2Fseries%2Fhhl%2Fhhl10.bht%3A`

| Ord. | Standing | Authors / editors | Exact title | Pages | Year | DOI and resolver URL | DBLP key and record URL |
|---:|---|---|---|---|---:|---|---|
| 1 | volume editorship | Dov M. Gabbay; Stephan Hartmann 0001; John Woods 0001 | Inductive Logic | — | 2011 | `10.1016/C2009-0-16928-3`<br>`https://doi.org/10.1016/C2009-0-16928-3` | `series/hhl/10`<br>`https://dblp.org/rec/series/hhl/10` |
| 2 | chapter | J. R. Milton | Induction before Hume. | 1-41 | 2011 | `10.1016/B978-0-444-52936-7.50001-X`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50001-X` | `series/hhl/Milton11`<br>`https://dblp.org/rec/series/hhl/Milton11` |
| 3 | chapter | Marc Lange | Hume and the Problem of Induction. | 43-91 | 2011 | `10.1016/B978-0-444-52936-7.50002-1`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50002-1` | `series/hhl/Lange11`<br>`https://dblp.org/rec/series/hhl/Lange11` |
| 4 | chapter | Malcolm R. Forster | The Debate between Whewell and Mill on the Nature of Scientific Induction. | 93-115 | 2011 | `10.1016/B978-0-444-52936-7.50003-3`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50003-3` | `series/hhl/Forster11`<br>`https://dblp.org/rec/series/hhl/Forster11` |
| 5 | chapter | Stathis Psillos | An Explorer upon Untrodden Ground: Peirce on Abduction. | 117-151 | 2011 | `10.1016/B978-0-444-52936-7.50004-5`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50004-5` | `series/hhl/Psillos11`<br>`https://dblp.org/rec/series/hhl/Psillos11` |
| 6 | chapter | Maria Carla Galavotti | The Modern Epistemic Interpretations of Probability: Logicism and Subjectivism. | 153-203 | 2011 | `10.1016/B978-0-444-52936-7.50005-7`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50005-7` | `series/hhl/Galavotti11`<br>`https://dblp.org/rec/series/hhl/Galavotti11` |
| 7 | chapter | Alan Musgrave | Popper and Hypothetico-deductivism. | 205-234 | 2011 | `10.1016/B978-0-444-52936-7.50006-9`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50006-9` | `series/hhl/Musgrave11`<br>`https://dblp.org/rec/series/hhl/Musgrave11` |
| 8 | chapter | Jan Sprenger | Hempel and the Paradoxes of Confirmation. | 235-263 | 2011 | `10.1016/B978-0-444-52936-7.50007-0`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50007-0` | `series/hhl/Sprenger11`<br>`https://dblp.org/rec/series/hhl/Sprenger11` |
| 9 | chapter | Sandy L. Zabell | Carnap and the Logic of Inductive Inference. | 265-309 | 2011 | `10.1016/B978-0-444-52936-7.50008-2`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50008-2` | `series/hhl/Zabell11`<br>`https://dblp.org/rec/series/hhl/Zabell11` |
| 10 | chapter | Ilkka Niiniluoto | The Development of the Hintikka Program. | 311-356 | 2011 | `10.1016/B978-0-444-52936-7.50009-4`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50009-4` | `series/hhl/Niiniluoto11`<br>`https://dblp.org/rec/series/hhl/Niiniluoto11` |
| 11 | chapter | Frederick Eberhardt; Clark Glymour | Hans Reichenbach's Probability Logic. | 357-389 | 2011 | `10.1016/B978-0-444-52936-7.50010-0`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50010-0` | `series/hhl/EberhardtG11`<br>`https://dblp.org/rec/series/hhl/EberhardtG11` |
| 12 | chapter | Robert Schwartz | Goodman and the Demise of Syntactic and Semantic Models. | 391-413 | 2011 | `10.1016/B978-0-444-52936-7.50011-2`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50011-2` | `series/hhl/Schwartz11`<br>`https://dblp.org/rec/series/hhl/Schwartz11` |
| 13 | chapter | James M. Joyce | The Development of Subjective Bayesianism. | 415-475 | 2011 | `10.1016/B978-0-444-52936-7.50012-4`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50012-4` | `series/hhl/Joyce11`<br>`https://dblp.org/rec/series/hhl/Joyce11` |
| 14 | chapter | Jonathan Weisberg | Varieties of Bayesianism. | 477-551 | 2011 | `10.1016/B978-0-444-52936-7.50013-6`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50013-6` | `series/hhl/Jonathan11`<br>`https://dblp.org/rec/series/hhl/Jonathan11` |
| 15 | chapter | Nick Chater; Mike Oaksford; Ulrike Hahn; Evan Heit | Inductive Logic and Empirical Psychology. | 553-624 | 2011 | `10.1016/B978-0-444-52936-7.50014-8`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50014-8` | `series/hhl/ChaterOHH11`<br>`https://dblp.org/rec/series/hhl/ChaterOHH11` |
| 16 | chapter | Jan-Willem Romeijn | Inductive Logic and Statistics. | 625-650 | 2011 | `10.1016/B978-0-444-52936-7.50015-X`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50015-X` | `series/hhl/Romeijn11`<br>`https://dblp.org/rec/series/hhl/Romeijn11` |
| 17 | chapter | Ulrike von Luxburg; Bernhard Schölkopf | Statistical Learning Theory: Models, Concepts, and Results. | 651-706 | 2011 | `10.1016/B978-0-444-52936-7.50016-1`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50016-1` | `series/hhl/LuxburgS11`<br>`https://dblp.org/rec/series/hhl/LuxburgS11` |
| 18 | chapter | Daniel N. Osherson; Scott Weinstein | Formal Learning Theory in Context. | 707-717 | 2011 | `10.1016/B978-0-444-52936-7.50017-3`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50017-3` | `series/hhl/OshersonW11`<br>`https://dblp.org/rec/series/hhl/OshersonW11` |
| 19 | chapter | Ronald Ortner; Hannes Leitgeb | Mechanizing Induction. | 719-772 | 2011 | `10.1016/B978-0-444-52936-7.50018-5`<br>`https://doi.org/10.1016/B978-0-444-52936-7.50018-5` | `series/hhl/OrtnerL11`<br>`https://dblp.org/rec/series/hhl/OrtnerL11` |

## Conflicts and non-collapsible presentation differences

1. **Volume 1 year conflict.** The current HTML page heading is “Greek, Indian and Arabic Logic 2001,” and its nine non-volume rows carry year `2001`. The volume editorship record carries year `2004`, and the same page’s volume citation says “Elsevier 2004.” The Volume 1 DOI strings also contain `(04)`. This note preserves all of those attributed strings and does not choose a house date for the chapter rows.
2. **Page order versus XML order.** For every volume, the HTML and XML record sets are identical but the XML search-result ordering differs. This note preserves the HTML page order and keeps the XML order as a separately observed presentation fact.
3. **Retained-capture truncation.** Every old `web-open-dblp-01.txt` through `web-open-dblp-10.txt` key sequence is an exact prefix of the current page sequence. Volumes 1 and 7 reach the current final key; the other eight captures stop early. Across the ten files, 33 current tail records are absent. No missing record is inferred from those older captures; each is established by the fresh HTML and XML responses.
4. **HTML/XML serialization differences.** The HTML volume-entry titles end in a display period while XML volume titles do not. HTML renders ordinal suffixes typographically, producing visible-text forms such as “12 th,” while XML carries `12th`. The Volume 10 HTML DOI link uses lowercase `c2009` while XML supplies uppercase `C2009`. These exact differences remain attributed; the ledger uses XML field strings and records the presentation conflict here.
5. **Name disambiguation.** XML names may include numeric disambiguation suffixes that HTML suppresses in visible text. The suffixes are DBLP identity metadata, not extra parts of the scholars’ names in prose. The exact XML strings remain in the ledger rather than being silently stripped.
6. **Metadata rights versus body rights.** The DBLP CC0 notice is evidence for the metadata reproduced here. It is not treated as an Elsevier body licence, and a DOI link is not treated as permission or open access.

## Retained rendered-capture audit

| Vol. | Retained artifact | Bytes | LF lines | SHA-256 | Keys exposed | Current rows | Missing current tail keys |
|---:|---|---:|---:|---|---:|---:|---|
| 1 | `tmp/acquisition/src063/web-open-dblp-01.txt` | 26,643 | 368 | `6a25294ff348828bade3a2302c35f2aed63815aa2ee67a2d1d59692bc48e24a6` | 10 | 10 | — |
| 2 | `tmp/acquisition/src063/web-open-dblp-02.txt` | 27,014 | 379 | `daeba1486b39c54798d75a34561405ee05fb30a7df0123997c82b72219b2c18c` | 11 | 15 | `series/hhl/Yrjonsuuri08`, `series/hhl/Ashworth08`, `series/hhl/Dvorak08`, `series/hhl/Wahl08` |
| 3 | `tmp/acquisition/src063/web-open-dblp-03.txt` | 26,957 | 379 | `e4cc326372cfc76a14308384eb2e6774db774524426149a33a64a99703aa37a2` | 11 | 13 | `series/hhl/Hilpinen04`, `series/hhl/Sullivan04` |
| 4 | `tmp/acquisition/src063/web-open-dblp-04.txt` | 26,855 | 386 | `7fe63caad48ab1d57686fe1db75cfc3a5c84b956a59bd7e72652fc95e44a7d1f` | 13 | 17 | `series/hhl/MosselmansM08`, `series/hhl/RahmanR08`, `series/hhl/Sullivan08`, `series/hhl/Mander08` |
| 5 | `tmp/acquisition/src063/web-open-dblp-05.txt` | 26,990 | 378 | `f10b34ae12d17c98057a01ba118999a8b088988573849b7cde6507585a56696f` | 11 | 18 | `series/hhl/AttenK09`, `series/hhl/Simmons09`, `series/hhl/Urquhart09`, `series/hhl/Plato09`, `series/hhl/CardoneH09`, `series/hhl/Seldin09`, `series/hhl/Cantini09` |
| 6 | `tmp/acquisition/src063/web-open-dblp-06.txt` | 27,067 | 378 | `edc539ed626a2c78e1125963065d2b244ef587de9572dc85d36ed42cba35f1c3` | 11 | 12 | `series/hhl/KamareddineLC12` |
| 7 | `tmp/acquisition/src063/web-open-dblp-07.txt` | 26,973 | 376 | `c155481c73f4523c513153f13291d3d0ed5e17f0a1717f0c56f3feed6177fd3a` | 11 | 11 | — |
| 8 | `tmp/acquisition/src063/web-open-dblp-08.txt` | 27,017 | 373 | `b51de84844761c6df3850e07045c120e9449aade99176f8d8ead2d3a0f8df957` | 10 | 12 | `series/hhl/Bochman07`, `series/hhl/Posy07` |
| 9 | `tmp/acquisition/src063/web-open-dblp-09.txt` | 27,002 | 378 | `c81ac746f84bae371d6710702eac0bac739bc610bff4c5d78ee12f49d7cf5cbe` | 11 | 18 | `series/hhl/Ambos-SpiesF14`, `series/hhl/FortnowH14`, `series/hhl/Kowalski14`, `series/hhl/MinkerSZ14`, `series/hhl/Meyer14`, `series/hhl/KnorrH14`, `series/hhl/HitzlerLP14` |
| 10 | `tmp/acquisition/src063/web-open-dblp-10.txt` | 26,920 | 388 | `d6c7babcd245a51505ceb50b1531755782bb1c573ad6e8dcd50a4ed8302ff880` | 13 | 19 | `series/hhl/Jonathan11`, `series/hhl/ChaterOHH11`, `series/hhl/Romeijn11`, `series/hhl/LuxburgS11`, `series/hhl/OshersonW11`, `series/hhl/OrtnerL11` |

All ten retained key sequences match the corresponding current HTML page from the first volume row through the retained final row. That is a prefix verification only. It does not upgrade the retained artifacts into complete captures.

## Fresh request and response evidence

| Vol. | HTML request SHA-256 | HTML response UTC / bytes / SHA-256 | XML request SHA-256 | XML response UTC / bytes / SHA-256 | Rows / hits |
|---:|---|---|---|---|---:|
| 1 | `97d98604bacefae63161fd152a6600ac21c3a2d3c971f5aeba8ef4c790a63d09` | 09:30:17Z / 113,947 / `bfcc979e84ca701472d31648126ebeddeeebf45fec70cf28c0402cc2dc4e8415` | `71f309c5be1fd2a3668785ccee3a18a57a44a46fd1d6825422cab740d829321a` | 09:30:39Z / 5,506 / `f7d51d2b64a210fbccd3e3725e8f9374759227890760c2f5c3a1ae7e4fa31ad3` | 10 / 10 |
| 2 | `7b8d3ee0a2f542a08c8b99ffb4d9b30c9d695d748a86c2b3019c6d5a6139c3c3` | 09:30:45Z / 154,031 / `e84cd64780c9eaea7375d816b8707d5a9afc46b573cc14e4a08cf36241d453c6` | `ff0f02150a2731a20021c85b85ce103e895d4789f8deb7b95ad336d31daeffa2` | 09:30:48Z / 8,202 / `d97e60f9ac69b69ce54ddf03debf4151282cc71f86e27035f1dd53acb5bbeb67` | 15 / 15 |
| 3 | `e8a0cc2ad6569368c4d9f348047cf3e41486587924e863731cfc754a949e3705` | 09:30:50Z / 135,286 / `a15ccda5f7a97592d2f5b70c0807705e20e8b747e94b1104796c7198808061d9` | `e7ebf4e13970387ae0545a8e7a6c056ed1496f6b905fec05cdaa713c705b4767` | 09:30:52Z / 7,117 / `6417271129ccf3fa53c69647465adaf92553130eb7ee1b312ffcf69529311cd3` | 13 / 13 |
| 4 | `a674e15ad3a4fd6a68f9c0e903912c0781a412430608f4ddd00c6105d8ac4a1f` | 09:30:54Z / 168,223 / `66ccac409bbdf87a1612a2cc5424a91f7cc583f8ed778becabe106919dd83751` | `8b88f888af6453dff9a50351f326b56c98531f920e86274218e8fe6f36f58de4` | 09:30:57Z / 9,408 / `9781580d7426c863e542e9d39bad5efccd57b2c236d7cdd18033d414de520919` | 17 / 17 |
| 5 | `d428d7f5b9462be67ae5a20a12b100e14a4dc42157aec13eb84e2bb5dcba2ea8` | 09:30:59Z / 174,046 / `3d0889f717a422b3f6795304080d9ca8483868cf70c1e822b2d0c92f4fa978df` | `2b1c4b3212ec945fc29635d6047b0dee128c9a32cb64d60826baf7e3453c3528` | 09:31:02Z / 9,696 / `105c4227a4fc0beaa0451bccf41a27399beeef9f603087c66fae81627376b88f` | 18 / 18 |
| 6 | `50cd8fc5f9d4bac939874ff8696e2525809443072a7ec760d038fb652c670896` | 09:31:04Z / 131,974 / `0e6e68f67c3602aa25a79ab576e11dc94b4f00238b3bdb2a196c572be4dd19ab` | `bb0849185bbccc10897ca53ce154c1c9c648c6ad8a72e85cdc68289fa3f5f189` | 09:31:06Z / 7,089 / `21fa8b3286e16f4c3f1904f1ad40a053f267496391e77e49ea21e319a2e81459` | 12 / 12 |
| 7 | `091a027feaac9c4cf796d601f235244374f351137d77b0a48843648cb8e1418e` | 09:31:08Z / 122,738 / `f9ad44d7073fdf4122063749728b43f7232b2c88110ffcc9ad1f96a07d81691b` | `750a45d56115fc3eb01c166715d7a2e5fea163eae1afeb730582e1b39dc65fad` | 09:31:10Z / 6,265 / `3878f08bc75f306d51bc54e9a835b5d004b7a2de4f5b2398ae1e5d3aabf325f2` | 11 / 11 |
| 8 | `e8145faf50b0580c8b1f122d1775cd629258bdd1d569f29aeae2b7ef553cb2e4` | 09:31:12Z / 130,969 / `fd9d3c7aa316860d6aba329cf689ecb7122cd54d28eb2c7ea542ccb2a25c833d` | `598e7d315a21abb7fdfa08f87ed2cd969a56089e1893d6ed5ad2ad64ea6b599e` | 09:31:14Z / 6,885 / `b2a261eca109fd117960f2df3a771144b717aada660a16bd7a0d5b70943d8ae6` | 12 / 12 |
| 9 | `0e49cb84ba2a45bddb91e8335072be9e6612b9efe27eb01742c2c1207c4a4b80` | 09:31:17Z / 178,328 / `e1531f40c207cf2f47a10ce60e9bf7b7962ee91132636770e105ff5700550d2a` | `cede1fb1b1a6303af4491c9ef96d6d833e3b3807df01c9504a200c6b3718eebf` | 09:31:19Z / 10,367 / `7ed970d8af4ab6d8218fcbe3bb9f69f38d533b319365cc562e0f9bbfa082b361` | 18 / 18 |
| 10 | `7382b07c8ba5e1282d5ea7697038b3340bfe8e14524b1f6da193be87e6e9baca` | 09:31:21Z / 185,892 / `c349bd578b540f2081b3ac4a930b59661cef01a53b18804b8714f031cdc8fb84` | `1c6db9f8a0f8e206c137c7c271ac228e9673558d52f34f4350a5b6d1f6d6ca90` | 09:31:24Z / 10,439 / `92fc801f50e778dad2c600a9212d2eb988971be62233eb9547e9a3cdc44e9b4a` | 19 / 19 |

The exact request URLs are printed at the start of each volume subsection. The request-hash representation is printed verbatim above. The ten HTML response hashes cover 1,495,434 bytes; the ten XML hashes cover 80,974 bytes. No response body is committed as an acquired book body: these are metadata responses only.

## Volume 11 remains `SRC-062`

Volume 11, *Logic: A History of its Central Concepts*, is deliberately absent from the 145-row ledger. Its governed evidence remains `spec/research/acquisition-src-062.md` (13,917,427 bytes; 74,246 LF lines; SHA-256 `ff3c4ca346074c8b8026d92be1d0301c32d3234c4eff2ec790b1533746e36d3e`). That record separately identifies Volume 11, its chapter hierarchy, conflicting presentations, access responses, and rights state. The current task does not import `series/hhl/11`, its preface, or any Volume 11 chapter key into `SRC-063`; it therefore does not collapse the existing provenance boundary.

## Rights, admission, and unresolved work

- DBLP metadata licence: CC0 as stated by DBLP; applicable only to the metadata surface used here.
- Publisher chapter-body rights: not established.
- Exact protected-text reproduction permission: not obtained or requested.
- Rights-holder contacts: 0; no rights-holder contacts were made.
- External messages sent: 0; no external message was sent.
- Subscription-only bodies retrieved: 0; no subscription-only body was retrieved.
- Inaccessible bodies credited as acquired: 0; no inaccessible bodies were credited as acquired.
- Public/open chapter-body acquisition: not performed in this task.
- Presentation-packet construction: not performed.
- Independent packet-content admission: not performed.
- External-coverage fulfillment: not claimed.
- AI source-fidelity review: pending.
- AI topic-specialist review: pending.
- AI adversarial/publication review: pending.
- Static, build, and rendered-page validation of integrated content: pending.
- `ACQ-GAP-003`: **OPEN**.

The metadata inventory can support later packet construction, but every presentation must still establish its work/edition/locator identity, lawful use basis, exact content-item links, coverage/register links, completeness dimensions, and independent admission. Any protected body expression must be handled under the book’s rights policy. None of those later gates is implied by this note.

## Patch-ready nonterminal recommendation

After this note is frozen and its SHA-256 is independently computed, append exactly one nonterminal report reference to `ACQ-GAP-003`:

```json
{
  "path": "spec/research/acquisition-gap-history-of-logic-volumes-1-10-2026-08-14.md",
  "sha256": "<frozen-note-sha256>",
  "report_result": "not_clean",
  "gap_status_effect": "none",
  "applies_to_gap_ids": [
    "ACQ-GAP-003"
  ],
  "rights_holder_contacts": 0,
  "external_messages_sent": 0,
  "subscription_only_bodies_retrieved": 0,
  "inaccessible_bodies_credited_as_acquired": 0
}
```

The recommendation is deliberately nonterminal: `report_result` is `not_clean`; the gap status remains `OPEN`; the status effect is none; no content links or destination labels are supplied; every review/build/visual field remains pending. The report may be added only through the governed acquisition-gap generator and schema workflow, not by editing generated CSV/Markdown outputs directly.

## Validation checklist

- [x] Scope contains Volumes 1–10 only.
- [x] Ten fresh HTML page responses and ten fresh XML responses returned HTTP 200.
- [x] HTML and XML record sets agree for every volume.
- [x] Page order is retained; XML order is not substituted.
- [x] 145 rows are present exactly once by DBLP key.
- [x] 127 chapter rows, 8 front-matter rows, and 10 editorship rows are distinguished.
- [x] Every supplied page range, DOI, DOI URL, DBLP key, and DBLP record URL is retained.
- [x] All ten old rendered captures are hash-pinned and treated as prefixes.
- [x] All 33 old-capture omissions are enumerated.
- [x] Volume 11 remains a separate `SRC-062` presentation.
- [x] Rights, body access, packet admission, ledger fulfillment, and gap closure remain unclaimed.
- [x] Contacts and external messages remain zero.

## Primary/current source locators

- DBLP canonical series index: `https://dblp.org/db/series/hhl/index`
- DBLP canonical volume pages: `https://dblp.org/db/series/hhl/hhl1.html` through `https://dblp.org/db/series/hhl/hhl10.html`
- DBLP official Trier mirror pages and XML exports: exact URLs in the volume subsections above
- DBLP CC0 notice: displayed in the footer of the current DBLP volume pages; legal instrument: `https://creativecommons.org/publicdomain/zero/1.0/`
- Separate Volume 11 authority evidence: `spec/research/acquisition-src-062.md`
