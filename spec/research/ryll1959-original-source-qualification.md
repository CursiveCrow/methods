# Ryll-Nardzewski 1959: new journal-volume source qualification

Date: 2 October 2026 UTC. This is one bounded, source-only acquisition/qualification block. The complete original article was **not acquired or read**. No original-body hash, page-completeness check, symbol-readability claim, original-proof reconstruction, or source-completion credit is claimed.

## Target and inherited boundary

The requested canonical locator is `RyllNardzewski1959`: C. Ryll-Nardzewski, *On the Categoricity in Power* \(\leq\aleph_0\), *Bulletin de l'Académie Polonaise des Sciences, Série des sciences mathématiques, astronomiques et physiques* **7** (1959), printed **545-548**. The article title is retained as the inherited bibliographic locator, not presented as newly checked against an original title page. Exact original title typography, formulation, hypotheses, proof and presentation remain unverified until an actual 545-548 source body is acquired and read.

The complete existing `spec/research/p03-ryll-nardzewski-source-note.md` and `source/references/original-source-new-routes/baldwin-lachlan-ryll-haken-2026-10-02/source-acquisition-note.md` were read before the new work. Their closed RCIN volume, Fuhrken/JSL review, Wroclaw legacy, South Carolina course, bibliography and other already closed routes were not retried as supposed original-body routes. The new work used ordinary institutional journal/volume catalogues and the public Internet Archive search UI. No later proof, differently dated paper, review or teaching note was substituted.

## New routes, exact observations and disposition

### 1. HathiTrust journal-volume catalogue

The public catalogue home redirected normally to [HathiTrust's home search](https://www.hathitrust.org/). The search UI was used with field **ISBN, ISSN, OCLC, etc.**, query `0001-4117`; the ordinary [All Items result](https://catalog.hathitrust.org/Search/Home?type%5B%5D=isn&lookfor%5B%5D=0001-4117&page=1&pagesize=100&ft=) displayed six records. Its two Full View matches were unrelated titles. The three Bulletin records below were inspected directly in the ordinary public browser catalogue.

| Public catalogue record | Explicit 1959 item/source observations | Access classification |
| --- | --- | --- |
| [000505551](https://catalog.hathitrust.org/Record/000505551) | `mdp.39015030610540`, University of Michigan; `pst.000059908005`, Pennsylvania State University; each labelled v.7 1959 | Both Limited (search only) |
| [007838598](https://catalog.hathitrust.org/Record/007838598) | `uc1.b3552113`, University of California; `coo.31924000958698`, Cornell University; each labelled v.7 1959 | Both Limited (search only) |
| [010851361](https://catalog.hathitrust.org/Record/010851361) | `chi.23180332`, University of Chicago; labelled c.1 v.7 1959 | Limited (search only) |

Record 007838598 also displays `uc1.b4473961`, University of California, labelled v.7 without a year in that item label; it is retained with that qualification, not promoted to independently original-body-verified 1959 evidence. Exact observed item links and labels are in `source/references/ryll1959-qualification/hathitrust-browser-observations.json`.

These are concrete digitized-volume locators, but not article-body acquisitions. The catalogue's access classifications were sufficient to stop: none of the limited-access viewer/item links was opened or downloaded. No login, accessibility-service claim, CAPTCHA, or access-restriction workaround was attempted.

The text web retrieval tool could not access the catalogue root. Browser catalogue navigation nevertheless supplied the observations above. **Separate, single ordinary HTML-capture requests** to each of the three public record URLs returned **HTTP 403 Forbidden**; no HathiTrust server HTML files were retained, and no retry or client-fingerprint/TLS workaround followed those 403 results. The saved JSON is explicitly a transcription of targeted browser observations, not represented as downloaded HathiTrust HTML.

### 2. Mathdoc PCMath conservation catalogue

The actual [periodical record 1335](https://cfp.mathdoc.fr/periodique/1335/) identifies ISSN `0001-4117`, the mathematics/astronomy/physics series, and print publication from 1958 to 1978. It lists physical conservation holdings including Grenoble, Marseille, Orsay, Polytechnique, IHP, Jussieu, Strasbourg and Toulouse that span 1959. The record contains binding, condition, shelf and linear-metre information, not an original-article/issue download link. Its primary standing is print-holding metadata, not a digitized four-page source. HTTP 200 HTML was retained as `mathdoc-pcmath-1335.html`.

### 3. National Diet Library's exact mathematics-series record

The NDL public search UI was used with `0001-4117`; the actual mathematics-series result led to [bibliographic record 000000118498](https://ndlsearch.ndl.go.jp/en/books/R100000002-I000000118498), call number **Z53-A241**. This is not the chemistry/geology series that broad searches also return.

The record reports paper format, onsite Kansai holdings, and the holding range **6(6):1958 - 26(12):1978**, with a stated lack of **9(1-5)**. It does not provide a public digital-view/download route to the target 1959 article. Its individually displayed catalogue item entries are a general unlisted-material entry and volumes 8 (1960) and 10 (1962); the holding range, rather than these individually displayed items, spans 1959. No ordering, paid copying, login or contact action was taken. A web-tool request for this record was unavailable, while ordinary browser navigation and a separate HTTP 200 request supplied the catalogue observation and retained HTML `ndl-000000118498.html`.

### 4. Internet Archive's ordinary journal-collection navigation

This was a genuinely changed mechanism from the previous failed advanced-search API: the ordinary public search UI at [archive.org](https://archive.org/) successfully submitted `title:("Bulletin" AND "polonaise")`. Its displayed 120 metadata matches included the actual [journal collection `pub_bulletin-pan-physiques-et-astronomiques`](https://archive.org/details/pub_bulletin-pan-physiques-et-astronomiques). The complete displayed collection inventory has **17 items**: twelve issues of volume **9 (1961)** and five **contents-only** items for **1965, 1967, 1968, 1969 and 1970**. No item in this inspected inventory is volume 7 (1959).

The collection header describes the later physics/astronomy successor series and establishment in 1979, whereas the actual item titles identify earlier mathematics/astronomy/physics series issues. That metadata mismatch is not silently resolved in favour of an assumed 1959 holding; this result relies on the actual enumerated item dates and titles only.

The collection exposes a [public RSS inventory link](https://archive.org/services/collection-rss.php?collection=pub_bulletin-pan-physiques-et-astronomiques). It was downloaded normally with HTTP 200, retained as `internet-archive-bulletin-collection.rss.xml`, and read completely. XML parsing independently counted **17 `/rss/channel/item` elements**, with **zero 1959 titles**, agreeing with the full public UI inventory. The RSS is a dynamically generated recent-additions feed, not inherently a universal collection dump; completeness here is supported by its 17 entries agreeing with the public collection's 17-result count and the observed entire list.

One precise narrowing in the ordinary public archive UI, [query `title:("Bulletin" AND "polonaise") AND year:1959`](https://archive.org/search?query=title%3A%28%22Bulletin%22+AND+%22polonaise%22%29+AND+year%3A1959&tab=all), displayed **0 Results** and no metadata search results. This establishes only the outcome of that exact catalogue query on this date, not universal absence from Internet Archive, other collections or unindexed material. The formerly failing advanced-search API was not retried. No non-target issue body was downloaded or used for mathematics.

### 5. Bounded external discovery and rejected neighbours

Discovery queries used exact author/page/title strings and the mathematics-series title/ISSN to seek an observed original-scan link. Representative exact queries were `"Ryll-Nardzewski" "545" "548" pdf`, `"On the categoricity in power" original scan`, `"0001-4117" digital`, `"Bulletin" "Polonaise" "1959" site:babel.hathitrust.org`, `"Bulletin" "Polonaise" "Volume 7" "1959" "mathématiques"`, and `"Ryll-Nardzewski" "1959" "545" "scan"`. Other domain-scoped journal discovery used HathiTrust, NDL, Polona, Gallica, Google Books and IMPAN. These searches supplied catalogue/bibliography records, later theorem expositions, or other years/series, but no verified original-body link. They are discovery results only.

The observed [Google Books volume](https://books.google.com/books?vid=UCAL%3AB4473964) is **volume 10 (1962)**. Its description was inspected; it is not volume 7 (1959) and was not downloaded or substituted. A search-located [CINiBA print serial record](https://integro.ciniba.edu.pl/integro/192001771679/dokumenty-ciagle/bulletin-de-lacademie-polonaise-des-sciences) produced a web-tool cache-miss failure; it was not credited as a body or repeatedly requested. Niche unrelated papers, modern theorem proofs and the known 1966 review were not adopted.

## Retained artifacts and hashes

All four artifacts are in `source/references/ryll1959-qualification/`. They are catalogue/collection evidence, **not original article bodies**. SHA-256 authenticates the retained object only; it does not confer original-proof standing.

| Artifact | Bytes | SHA-256 | Method/standing |
| --- | ---: | --- | --- |
| `mathdoc-pcmath-1335.html` | 22318 | `DBBC0CBB565E96C924048DFF536367AEBEC34D5377B049EEBB617506D976AEB8` | HTTP 200 public primary print-holding catalogue HTML |
| `ndl-000000118498.html` | 225583 | `9F14C1D394B00CA84FDDBBC75195F534B38B4993E76ACA46E10C188073CC6C05` | HTTP 200 exact mathematics-series catalogue HTML |
| `internet-archive-bulletin-collection.rss.xml` | 25880 | `C8CBD5EA0AD2BF99BE67942FA1AB9747AD9B068B8A3B1BA3AAC5643CDFDD282D` | HTTP 200 observed collection RSS; complete feed read; 17 items checked against UI inventory |
| `hathitrust-browser-observations.json` | 3269 | `E67AB272B138E435B016FB537FFCC91960F1ACDE995BDA6008A690C6EEBD0B63` | Targeted browser-observation transcription; not downloaded catalogue HTML |

## Qualification result and precise remaining dependency

**Original-body acquisition: no. Original printed pages read: none. Body SHA-256: none. Exact original title/symbols/proof/version and 545-548 completeness: not checked.** New journal-volume evidence gives five explicit institutional digitized 1959 volume locators, all limited-access, plus one year-unlabelled v.7 locator and public print holdings. The actual public Internet Archive collection inspected here covers different years.

The remaining dependency is a freely/publicly reachable original scan of all printed **545-548**, or an authorized source copy supplied within the existing scope. On acquisition it must be checked for actual author/title/year/series/volume identity, complete four-page extent, readable mathematical notation and any institutional reproduction/version qualifications, then hashed and read in full before original formulation/proof credit. An institutional reproduction must not be called a publisher facsimile without supporting evidence.

This block exhausted the concrete new public catalogue paths described above without a body. It does not show universal unavailability or impossibility. No source requirement is marked complete. No manuscript, queue, canonical record, intake, driver, renderer, build, prose test or protected bridge was edited or run. No child agent, payment, account/login, contact, CAPTCHA, access-control bypass, robots-restriction bypass or TLS disabling was used. Exact assigned-path/network permissions were requested; the shell directory/download operations used narrowly scoped approved escalation after a default-sandbox write denial. Local authored evidence and this note used `apply_patch`.
