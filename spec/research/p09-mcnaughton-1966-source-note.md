# McNaughton 1966, *Testing and Generating Infinite Sequences by a Finite Automaton*: source note

**Disposition:** PUBLISHER VERSION OF RECORD IDENTIFIED AS OPEN ARCHIVE, BUT
COMPLETE ARTICLE BODY NOT ACQUIRED; CONTEMPORARY FIRST-PERSON PROJECT MAC
SUMMARY ACQUIRED AND READ FROM THE ACTUAL SOURCE PDF; ALL BODY-DEPENDENT MATHEMATICAL DETAIL
REMAINS OPEN.

This is a route-bounded result for Part IX topic N-c-013.b. It does not
reconstruct the missing article from later textbooks, surveys, encyclopedia
entries, or memory.

## Registered work and publisher provenance

The registered work is Robert McNaughton, “Testing and generating infinite
sequences by a finite automaton,” *Information and Control* 9(5), October
1966, pp. 521--530, DOI
[10.1016/S0019-9958(66)80013-X](https://doi.org/10.1016/S0019-9958(66)80013-X).
Crossref records Elsevier BV as publisher, volume 9, issue 5, and pp. 521--530
([Crossref work record](https://api.crossref.org/works/10.1016%2FS0019-9958(66)80013-X),
JSON paths `/message/{DOI,title,publisher,volume,issue,page,published}`).

An archived copy of the publisher landing page fixes the platform identity
more finely. Its embedded publisher JSON records PII
`S001999586680013X`, EID `1-s2.0-S001999586680013X`, issue PII
`S0019995866X80110`, first and last pages 521 and 530, `pageCount: 10`,
Academic Press as the imprint, receipt on 14 September 1965, publication on
1 October 1966, and platform availability on 10 December 2006. It reports no
scholarly abstract. These dates have different standings and must not be
collapsed into a single publication date
([publisher capture, 2023-02-27 19:10:37 UTC](https://web.archive.org/web/20230227191037id_/https://www.sciencedirect.com/science/article/pii/S001999586680013X),
embedded JSON `data-iso-key="_0"`, keys
`article.{pii,eid,issuePii,pages,pageCount,publication-content.imprintPublisher,dates,hasScholarlyAbstract}`).

The same publisher data say `isPdfFullText: true` but `hasBody: false` and
leave `body` empty. The publisher's exposed page is therefore metadata plus a
PDF route, not an HTML article body. The PDF object is named
`1-s2.0-S001999586680013X-main.pdf`; the recorded PDF request has MD5 query
parameter `2b64a91c7b77d0a6f584533d94e98df7`. That parameter identifies a
publisher delivery request; it is not a locally verified checksum of the
unacquired article file (same publisher capture, embedded JSON
`article.{isPdfFullText,hasBody,body,pdfDownload}`).

## Access and rights boundary

The publisher data label the article `openarchive`, set
`access.openAccess: true`, and record anonymous guest entitlement with
`entitlementReason: "openarchive"`. The anonymous Elsevier Article API also
returns `openaccessArticle: true`, `openaccessType: Full`, and
`openArchiveArticle: true`
([Elsevier Article API](https://api.elsevier.com/content/article/pii/S001999586680013X),
XML `/full-text-retrieval-response/coredata`; publisher capture,
`article.{access,articleEntitlement,entitlementReason}`).

Crossref attaches an Elsevier user license to the version of record beginning
15 May 2014 (`/message/license`, entry with `content-version: "vor"`). The
current official [Elsevier user-license page](https://www.elsevier.com/about/policies-and-standards/open-access-licenses/elsevier-user)
says such articles remain copyright-protected. It permits specified
noncommercial access and copying but excludes redistribution, display, and
adaptation absent further permission (section “Elsevier user license,” first
paragraph). Thus “open archive” establishes a publisher-designated access
route; it does not place the article in the public domain or authorize this
note to reproduce an unacquired body.

The Project MAC report described below has its own, separate notice:
“Distribution of this document is unlimited.” Its preceding sentence limits
the express reproduction permission to United States Government purposes.
Those terms concern the Project MAC report, not McNaughton's journal article
(*Project MAC Progress Report*, PDF p. 2). No rights term from one object is
transferred to the other.

All web retrievals in this note were made on 2026-08-22 in
America/Los_Angeles unless a capture date is stated separately.

## Acquired evidence objects and integrity

The source files are under `tmp/pdfs/p09-mcnaughton-1966/`. Derived text or
page images are viewer aids only; the scanned PDF and publisher records remain
authoritative for what they visibly or structurally contain.

| Object | Identity and locator | Bytes / pages | SHA-256 |
|---|---|---:|---|
| Archived ScienceDirect landing HTML | 2023-02-27 capture of PII `S001999586680013X`; `sciencedirect-20230227-archived-decompressed.html` | 97,501 bytes | `13B152729D3C9C90CB293031673025E56C06239F54044D91B802CF007EA02A7D` |
| Crossref work JSON | DOI work endpoint; `crossref-work-2026-08-22.json` | 3,275 bytes | `460045999BFD30D63A64E54A9FD27C29C043C65199FAE5EB55989EEE0E1FCE1C` |
| Elsevier API core metadata XML | PII endpoint, anonymous default view; `elsevier-api-coredata-2026-08-22.xml` | 1,947 bytes | `DAAED6E8E91F4E85D6159185BBFCA34F578778B951CDEC6E55B889709AA13A0E` |
| OpenAlex work JSON | OpenAlex work `W2094912129`; `openalex-work-2026-08-22.json` | 12,343 bytes | `6641FD659B33FF6119D3BDC18CD75D90B3B43663043037B7FD8C06D6BC119320` |
| Semantic Scholar work JSON | paper `f628d62d2e7b8aaed47a3f8e28d7fd7ca3fe1047`; `semantic-scholar-work-2026-08-22.json` | 741 bytes | `C2E56284A5B198CA5B1584C70307CD479564D90E2F86D754ED14C028FDE9C72D` |
| Elsevier user-license HTML | official current policy; `elsevier-user-license-2026-08-22.html` | 195,384 bytes | `A1A48C8F93A304064BC3921ED3A8DDCE5A005313B333BD09833B4F1DAF7D4868` |
| Project MAC report scan | [MIT Project MAC, *Progress Report*, July 1965 to July 1966](https://bitsavers.org/pdf/mit/lcs/progress_reports/DTIC_AD0648346_Project_MAC_Progress_Report_03_196507-196607.pdf), DTIC AD-648346; `DTIC_AD0648346_Project_MAC_Progress_Report_03_196507-196607.pdf` | 17,580,936 bytes; 306 PDF pages | `68AB1D453C2F0F57B47B066DCC5706B9EA2851277DC76B61D6EF9032C86DD0BE` |

The Project MAC report's printed p. 58 is PDF p. 81. That page was read from
the actual source PDF. A derived viewer image aided legibility but supplies no
independent evidence. The accompanying extracted text misread every omega
glyph and several ordinary words, so the extraction was not used to decide
the printed wording.

## Route-bounded acquisition result

No complete article body was lawfully retrievable in this environment after
the following routes were checked.

| Route | Exact result |
|---|---|
| Publisher landing page | The live [ScienceDirect PII page](https://www.sciencedirect.com/science/article/pii/S001999586680013X) presented a human-verification challenge. It was not bypassed. The 2023 Internet Archive capture yielded the publisher metadata described above but expressly has no HTML body. |
| Publisher PDF endpoints | The canonical `/pdf`, `/pdfft?isDTMRedir=true&download=true`, and `/sdfe/pdf/download/eid/1-s2.0-S001999586680013X/first-page-pdf` routes returned HTTP 403 HTML challenge pages, not `%PDF-` files. |
| Wayback PDF captures | The [CDX query for the publisher PDF route](https://web.archive.org/cdx/search/cdx?url=www.sciencedirect.com%2Fscience%2Farticle%2Fpii%2FS001999586680013X%2Fpdf%2A&output=json&fl=timestamp%2Coriginal%2Cmimetype%2Cstatuscode%2Cdigest%2Clength&filter=statuscode%3A200&collapse=digest) returned two captures, both typed `text/html`, from 23 and 25 April 2024. The saved 23 April object contains Cloudflare challenge code and is not an article PDF (`wayback-pdf-cdx-search-2026-08-22.json`; `sciencedirect-pdf-wayback-cloudflare-2024-04-23.html`). Queries for the older `/pdfft`, Elsevier reader, ScienceDirect asset-CDN, and Elsevier image-CDN patterns returned no successful PDF capture. |
| Elsevier Article API | Anonymous default XML returned only `coredata`. `view=FULL`, `view=ENTITLED`, and `view=META_ABS` returned HTTP 401 `AUTHENTICATION_ERROR`; requesting `application/pdf` returned HTTP 406 with `Accept header value 'application/pdf' is restricted`. Crossref's two version-of-record text-mining links point back to this API (`/message/link`). |
| OpenAlex content | The [OpenAlex work record](https://api.openalex.org/works/https://doi.org/10.1016/S0019-9958(66)80013-X) says `locations_count: 1`; its sole and best location is the same ScienceDirect PDF. It says `open_access.any_repository_has_fulltext: false`. Although `content_urls` advertises a PDF and structured-text object, the PDF request returned HTTP 401 and the exact JSON body `{"error":"API key required","message":"Content downloads require an API key. Get one free at https://openalex.org/users"}`. The 121-byte response has been retained as `.json`, not mislabeled as a PDF (`openalex-content-download-401-2026-08-22.json`, SHA-256 `A51A6FB41EFA67BC3EAA6F96A1F8BBE74716087A26174490CB54BB1D4279C0A8`). |
| Other bibliographic registries | The Semantic Scholar work record also supplies only the ScienceDirect `/pdf` URL (`openAccessPdf.url`) and labels it open access. [DBLP](https://dblp.org/rec/journals/iandc/McNaughton66) and [zbMATH](https://zbmath.org/?q=an%3A0212.33902) identify the work but exposed no independent body in exact-title and DOI searches. Registry agreement therefore corroborates identity, not article content. |
| Author and institutional routes | An [exact-title query of MIT DSpace](https://dspace.mit.edu/server/api/discover/search/objects?query=dc.title%3A%22Testing%20and%20generating%20infinite%20sequences%20by%20a%20finite%20automaton%22&size=100) returned zero title matches (`mit-dspace-exact-title-search-2026-08-22.json`, HAL page `totalElements: 0`). [Rensselaer's public computer-science technical-report index](https://www.cs.rpi.edu/research/tr.html) has no exact-title or identifier match, and the former author-home candidates return 404. The Project MAC report was the only complete primary institutional document found; it summarizes the article but is not it. |
| Legitimate scan/catalog routes | [Internet Archive's exact-title catalog query](https://archive.org/advancedsearch.php?q=%22Testing+and+generating+infinite+sequences+by+a+finite+automaton%22&fl%5B%5D=identifier%2Ctitle&rows=50&page=1&output=json) returned `numFound: 0` (`internet-archive-exact-title-search-2026-08-22.json`). Exact DOI/title searches of [Internet Archive Scholar](https://scholar.archive.org/search?q=%22Testing%20and%20generating%20infinite%20sequences%20by%20a%20finite%20automaton%22), library-catalog results, and publicly indexed scans found metadata, citations, or later discussions only. No bound-volume or article scan was acquired. |

This is an access failure, not evidence that the publisher PDF does not exist.
The publisher, OpenAlex, and Semantic Scholar all point to the same PDF. A
user-completed publisher challenge, a user-supplied OpenAlex API credential,
or a lawfully supplied library/author scan could therefore change the body
status without changing the registered-work identity.

## Contemporary first-person evidence: Project MAC printed p. 58

The acquired report places two separately lettered entries under “Research
in the Theory of Automata - Robert McNaughton.” Section A says verbatim:

> This paper, originally an informal memorandum, has been published in
> Information and Control (vol. 9, no. 5, Oct. 1966, pp. 521-530). Given that an
> ω-event is a set of infinite sequences, the paper defines "regular ω-event" in
> terms of state graphs. It then proves an analogue to the so-called Kleene-
> Myhill theorem, to the effect that an ω-event is finite-state if and only if it
> is regular.

(*Project MAC Progress Report*, “Research in the Theory of Automata,”
section A, printed p. 58, PDF p. 81.)

This closes only the following facts, at the level of McNaughton's own
contemporary summary:

- the object called an “omega-event” is a set of infinite sequences;
- the article uses “regular omega-event” and defines it through state graphs;
- its reported result is an analogue of the Kleene--Myhill theorem,
  with the effect “finite-state if and only if regular”; and
- the journal paper originated as an informal memorandum.

These are source-verified report facts. The report does not reproduce the
article's definitions, theorem numbering, quantifiers, hypotheses,
constructions, examples, or proof.

## Game and determinacy separation

The immediately following Project MAC entry is separately headed
“B. FINITE-STATE INFINITE GAMES.” It begins:

> This writing was distributed as Computation Structures Memo No. 14 in
> September, 1965.

It later says:

> The paper sets out to prove that, in any deterministic finite-state
> infinite game, one of the players has a winning strategy, and such a strategy
> is a finite-state strategy. Thus, if what the paper claims to prove is true,
> it will follow that for any such game there is a finite automaton

and then records the source-critical qualification:

> Recently, a fallacy in my proof was discovered by Mr. Lawrence Landweber,
> a student of Professor J. R. Buchi of Purdue University. The error is deep,
> and I have not yet been able to patch it up. The concepts of this paper are
> intimately related to those of A.

(*Project MAC Progress Report*, section B, printed p. 58, PDF p. 81.)

The report thus treats the game writing as a distinct memo, says only that
its concepts are intimately related to article A, and expressly withholds
confidence in its claimed proof. The warranted handbook separation is:

1. article A supplies the reported omega-event equivalence;
2. memo B concerns infinite games and a finite-state winning-strategy claim;
3. the report itself says B's proof contains a deep, then-unpatched fallacy.

It would be source-confounding to attribute B's determinacy or strategy claim
to the 1966 journal article, or to use the article citation as if it repaired
the memo's acknowledged error. This conclusion is based on the report's
document separation. Because the article body remains unread, no stronger
claim is made about incidental game remarks, if any, inside the article.

## Body-dependent mathematical extraction status

| Requested handbook datum | Source-verified result | What remains open |
|---|---|---|
| Paper's objects and original terms | Contemporary report: an omega-event is a set of infinite sequences; “regular omega-event,” “state graphs,” and “finite-state” are source terms (Project MAC p. 58). The title supplies “testing” and “generating.” | The article's own notation, alphabet assumptions, definition of an infinite sequence, and exact meanings of “testing” and “generating.” |
| Automaton and state graph | The report says regularity is defined in terms of state graphs (Project MAC p. 58). | States, edges, labels, start data, determinism or nondeterminism, runs, outputs, and every acceptance clause. No tuple can be responsibly reconstructed. |
| Acceptance definition | None exposed by an acquired article body. | Which recurrent-state data are used, how they are quantified, and how testing differs from generating. |
| Exact theorem statements | The report gives only the effect “an omega-event is finite-state if and only if it is regular” (Project MAC p. 58). | Article theorem number, exact wording, hypotheses, notation, and whether subsidiary lemmas or corollaries occur. |
| Finite-state-to-regular construction | Existence of one direction follows only as a logical component of the reported equivalence. This is an inference from “if and only if,” not a recovered construction. | Construction inputs, outputs, invariants, induction measure, proof order, and any size bound. |
| Regular-to-finite-state construction | Same limited inference from the reported equivalence. | The actual construction, its state data, correctness argument, proof architecture, and any effectiveness or complexity statement. |
| Examples | No example was recovered from an article body or from Project MAC section A. | Every article example, diagram, worked sequence, and its role in the proof. |
| Qualifications and limitations | The platform provenance, access status, and distinct game-memo fallacy are closed as above. | Qualifications stated inside the article, including scope, effectivity, finiteness assumptions, or comparison with cited predecessors. |
| Printed defects | No printed article page was acquired, so no printed defect can be certified. | The archived publisher metadata renders the title footnote as “closely related to a tall: given by the author.” This may be a publisher transcription/OCR defect; without the page image it must not be silently corrected to, or cited as proof of, any printed reading (publisher capture, embedded JSON `article.title` footnote). |
| What the article does not prove | The evidence supports separating the distinct, fallacious 1965 game memo from article A. | No other negative mathematical claim is safe. Absence from metadata or the short Project MAC summary is not absence from the article. |

Crossref exposes four references—to Büchi (1962), Muller (1963), Kleene
(1956), and Myhill (1957)—at
`/message/reference[0..3]`. That registered list may orient a later body
audit, but it does not supply the article's definitions or license a proof
reconstruction from those cited works.

## Reader-facing disposition for N-c-013.b

The present metadata-only warning must remain. The source record now supports
one narrow historical statement: McNaughton's own Project MAC report describes
the paper as defining regular omega-events through state graphs and proving
that omega-events are finite-state exactly when regular. It does **not** yet
support a handbook presentation of the acceptance mechanism, either
construction direction, proof architecture, examples, internal
qualifications, or printed defects.

No later name for an automaton or acceptance condition should be retrojected
as McNaughton's terminology on this evidence. No theorem should be printed as
an “exact statement” from the paper until the ten-page body has been acquired,
hashed, page-mapped, and read from the actual source file. Once a lawful body
is supplied, the next source visit must read printed pp. 521--530 in full
and compare its first page against the publisher metadata footnote before
replacing any of the open cells above.

## Download follow-up, 2026-09-06

The exact publisher PDF route was opened in the normal in-app browser:
https://www.sciencedirect.com/science/article/pii/S001999586680013X/pdf .
It displayed an explicit human-verification checkbox. No article PDF
was acquired. The page was queued in the user's browser panel and a
nonblocking request asked the user to complete that verification if
available. Other manuscript writing continued. This is a verified
access-step outcome, not acquisition or a reason to halt the whole book.
