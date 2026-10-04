# Thatcher-Wright: independent archive and report-download search

Date: 2026-09-06.

## Result

No downloadable public body of either the exact 1968 article or the
same-title 1966 IBM RC-1713 report was verified in this bounded pass.
No target PDF was saved. A catalog entry, preservation claim, citation,
or unrelated paper was not substituted for the requested body.

The user declined the paid route and requests a downloadable PDF. The
remaining lead recorded below is therefore an institutional digital
preservation route, not a purchase recommendation or a request that the
user supply a copy. No third party was contacted and no purchase or
authentication action was taken.

## Exact targets and excluded substitutes

The journal target is James W. Thatcher and Jesse B. Wright,
*Generalized Finite Automata Theory with an Application to a Decision
Problem of Second-Order Logic*, *Mathematical Systems Theory* 2(1),
March 1968, pp. 57-81, DOI
[10.1007/BF01691346](https://doi.org/10.1007/BF01691346).
The [IBM publication record](https://research.ibm.com/publications/generalized-finite-automata-theory-with-an-application-to-a-decision-problem-of-second-order-logic)
identifies this journal article, gives its abstract, and links to its
publication record; no target report or article download was exposed.

The separately acceptable precursor target is the same-title IBM
Research Paper RC-1713, 1966. Contemporary corroboration includes the
reference list on p. 491 of Brainerd's *The Minimalization of Tree
Automata*, whose [primary article scan is hosted by the Naval
Postgraduate School repository](https://calhoun.nps.edu/server/api/core/bitstreams/729033fd-f419-43b0-a021-58a6c05d11a0/content).
That is a citation to RC-1713, not its body.

Excluded from target acquisition:

- The already-held 89-page Thatcher dissertation at
  `tmp/pdfs/p09-thatcher-1965/6511049.pdf`, *Decision Problems and
  Definability for Generalized Arithmetic*, associated with the
  earlier RC-1316/1964-1965 work. It is a different source.
- Thatcher's 1969 STOC paper, *Transformations and Translations from the
  Point of View of Generalized Finite Automata Theory*. Its
  [IBM record](https://research.ibm.com/publications/transformations-and-translations-from-the-point-of-view-of-generalized-finite-automata-theory)
  has a download route, but it is a different paper and was not credited.
- Dirk Siefkes's two-page 1972 JSL review, DOI `10.2307/2272790`.
  Search results repeat the full target title but identify the
  [review rather than the 1968 body](https://www.cambridge.org/core/product/identifier/S0022481200079597/type/journal_article).
- Other downloadable primary articles, theses, and textbooks that merely
  cite Thatcher-Wright or reconstruct later tree-automata theory.

## Internet Archive: independent item discovery

This pass did not start and finish with the old guessed volume endpoint.
It queried the public advanced-search service by journal title, collection,
report identifier, author/year, and institutional creator/date.

The queries and returned counts were:

| Public metadata query | Result |
|---|---|
| `title:"Mathematical Systems Theory"` | 22 results; mostly later annual indexes plus unrelated books. |
| `collection:pub_theory-of-computing-systems` | 25 public search results, all later annual index records; no 1968 issue or volume. |
| `identifier:sim_theory-of-computing-systems_1968*` | 0 results. |
| `title:"Mathematical Systems Theory" AND year:1968` | 0 results. |
| `"RC1713"` and `"RC-1713"` | 0 results in each query. |
| `"Generalized finite automata"` | 2 unrelated later arXiv items. |
| `creator:"International Business Machines"` with dates in 1960-1969 | 32 records; no RC-1713 body among the returned records. |
| `Thatcher AND year:1966` | 10 unrelated records. |

The [journal collection metadata](https://archive.org/metadata/pub_theory-of-computing-systems)
was readable. It identifies the predecessor title and ISSN `0025-5661`,
collection `pub_theory-of-computing-systems`, SIM publication ID `13200`,
and pallets `IA408535` and `IA408550`. The collection record itself
has `hidden=true`, but its public administrative files were exposed.

The three exposed duplicate-scan files were inspected:

- [IA40853505_dupes.json](https://archive.org/download/pub_theory-of-computing-systems/IA40853505_dupes.json)
- [IA40855007_dupes.json](https://archive.org/download/pub_theory-of-computing-systems/IA40855007_dupes.json)
- [IA40855023_dupes.json](https://archive.org/download/pub_theory-of-computing-systems/IA40855023_dupes.json)

The first contains exactly the relevant discovered scan-volume record:

```text
identifier: theory-of-computing-systems_1968_2_1-4
title: Mathematical Systems Theory 1968: Vol 2 1-4
date: 1968
volume: 2
issue: 1-4
col_number: COL-1804
old_pallet: IA408535
old_identifier: empty
```

The other two manifests supply no alternate 1968 entry. The current
[metadata endpoint for the discovered volume](https://archive.org/metadata/theory-of-computing-systems_1968_2_1-4)
returned no item metadata or file list. Thus no public PDF, page-image
archive, or alternate duplicate download was obtained from this actual
volume discovery.

The collection's public MARC and `per_metadata.json` files are catalog
and vendor-coverage metadata, not article pages. They supplied no target
download. Internet Archive Scholar's DOI search returned a session
verification page rather than a usable result; no challenge bypass was
attempted.

## HathiTrust: journal and catalog-identifier checks

The public bibliographic API was queried for the old journal ISSN in
both forms, `00255661` and `0025-5661`, and for successor identifiers
`1433-0490` and `1432-4350`. Each returned empty `records` and `items`.
Example: [full bibliographic query for ISSN 0025-5661](https://catalog.hathitrust.org/api/volumes/full/issn/0025-5661.json).

The IA MARC record supplied these OCLC identifiers:

```text
225163872, 263653202, 632300339, 780534137,
850748079, 960784449, 36165160
```

Each corresponding HathiTrust `api/volumes/full/oclc/{id}.json`
query also returned no records or items. The title-search interface
returned HTTP 403. No HathiTrust volume identifier or readable scan was
therefore established. These empty API responses and interface failures
do not prove that no relevant HathiTrust holding exists.

Stanford SearchWorks title/ISSN requests returned browser-verification
HTML rather than catalog results. No Stanford digital item was inferred
from that response.

## IBM report collections and public institutional repositories

Exact-title and report-number searches used `RC-1713`, `RC 1713`, and
`RC1713`, with author names and report/year terms. They located
contemporary citations but no RC-1713 PDF or authoritative target
report-record download.

IBM's older public report service was positively identified through
an unrelated report by the same research group,
[RC4526, 1973](https://dominoweb.draco.res.ibm.com/49eae98dc5a21de0852574ff005001c8.html).
Its indexed institutional page advertises an actual research-report
PDF. That establishes a real report repository worth checking, but
not RC-1713 availability. Targeted searches of that service found no
RC-1713 item. The RC4526 page request timed out, and a bounded direct
candidate request to `https://dominoweb.draco.res.ibm.com/RC1713.pdf`
also timed out. The latter was a filename probe, not a discovered
download link, and must not be represented as an available PDF.

Bitsavers IBM directory access failed with HTTP 403. The institutional
Stuttgart mirror's HTTPS index request was refused. Consequently this
pass did not complete a file-index audit of those collections and
does not report a verified absence there.

The [Berkeley Logic Library inventory](https://logic-library.berkeley.edu/)
was inspected for both authors and the exact title. It lists several
different Thatcher works, including *Decision Problems for Multiple
Successor Arithmetics* (1965) and *Generalized Sequential Machine Maps*
(1969), but no matching Thatcher-Wright target was found. The inventory
describes physical research material in the Tarski Room; it did not
provide a matching scan download.

## Best remaining institutional digital-download lead

The strongest new preservation evidence is the
[ISSN Keepers record for Mathematical Systems Theory](https://portal.issn.org/resource/ISSN/0025-5661).
Its current displayed archival entry names **Scholars Portal**, coverage
1967-1996, and explicitly includes **volume 2, issues 1-4** as preserved.
The displayed preservation update was 2026-03-19.

This establishes a specific institutional digital preservation target,
not public access to its content. The record links to
`https://scholarsportal.info/`; that link returned HTTP 403 here, and
the journals interface did not yield an accessible article record or
PDF. Exact-title and DOI searches restricted to Scholars Portal found
no indexed target download URL.

The next precise digital access path is therefore to locate the
preserved **0025-5661 / volume 2 / issue 1 / pages 57-81** object in
Scholars Portal and establish whether its actual PDF has a publicly
available institutional route. No article-object identifier or PDF URL
has yet been verified. The other still-unresolved public-download
paths are IBM's older report service for **RC-1713** and the unavailable
IA scan object **theory-of-computing-systems_1968_2_1-4**.

Print holdings were also found in search-indexed library records, but
they are not the requested downloadable PDF and are not presented as
completion. A Mathdoc holdings page explicitly labelled itself a test
platform, so it is not used as decisive live access evidence.

## Scope and handoff

This is a bounded negative acquisition result with concrete remaining
digital leads. It does not claim that all lawful copies have been
exhausted or that the article is unavailable everywhere. It establishes
that the named downloadable body was not obtained through the checked
archive and report routes.

Only this note was authored. The target PDF directory was not created,
because no target body was found to save. No handbook edits, software
tests, builds, manuscript renders, purchases, or external messages were
performed.
