# Woods 2012: exact source acquisition and dependent authoring

Date: 9 September 2026. Assigned source unit: `ED26-SRC-063-1110`; dependent comparison: `ED26-P18-refutation-diagnosis-0001`, component `LR006-C4`.

## Exact target and reserved destinations

The target is **John Woods, “A History of the Fallacies in Western Logic,”** in *Logic: A History of its Central Concepts*, **Handbook of the History of Logic, volume 11**, edited by Dov M. Gabbay, Francis Jeffry Pelletier and John Woods, Elsevier/North-Holland, **2012**, chapter 10, **pp. 513–610**, DOI **10.1016/B978-0-444-52937-4.50010-1**. That is an inclusive extent of 98 printed pages, including its source apparatus. An abstract, contents list, related Woods book or different fallacy paper does not supply this target.

The source allocation was read from `spec/coverage/edition-2026/sources-037-068/src063-content-units.jsonl`, together with the complete `LR006-C4` allocation and the prior Aristotle source note. The following exact proposed destinations were verified absent and reported to the root before any source-dependent writing:

- `handbook/parts/p18/presentations/src063-1110.tex`
- `handbook/annex/p18/src063-1110.tex`

If the complete source is qualified, this writer owns those destinations and unique `p18-woods-2012` bibliography/symbol intakes. The root owns routing and canonical merges. No manuscript stub or substitute chapter has been created during acquisition.

## Required intellectual extent

All sixteen mapped components remain required:

- **C001–C003:** the full historical argument, actual objects and inference tasks, source-specific formal definitions/rules/results/proofs, chronology, distinct interpretations, examples, limitations and comparisons. Formal, philosophical and empirical claims must retain their different evidential roles.
- **C004:** the complete Aristotle section and an explicit comparison with the separately sourced modern inference-defect interface. A contents page is not proof of its actual thirteen-category discussion.
- **C005:** Section 1, Introductory Remarks.
- **C006:** Section 2, Aristotle (384–322 BC).
- **C007:** Section 3, The Hellenistic and Mediaeval Periods.
- **C008:** Section 4, Francis Bacon (1561–1626).
- **C009:** Section 5, Antoine Arnauld (1612–1694) and Pierre Nicole (1625–1695).
- **C010:** Section 6, Isaac Watts: An Interlude.
- **C011:** Section 7, John Locke.
- **C012:** Section 8, Richard Whately (1787–1863).
- **C013:** Section 9, John Stuart Mill (1806–1873).
- **C014:** Section 10, Augustus De Morgan (1806–1871).
- **C015:** Section 11, The Great Depression: 1848–1970.
- **C016:** Section 12, Now.

These headings fix acquisition and future reading scope. They are not an authored reconstruction and supply no proof or comparison credit by themselves.

## Bounded acquisition evidence

The following routes were checked in this block. Failure of a retrieval route is not a claim that no freely obtainable copy exists anywhere.

| Route | Observed result | Qualification |
| --- | --- | --- |
| [Publisher article record](https://www.sciencedirect.com/science/article/pii/B9780444529374500101) | Web retrieval returned HTTP 403. | No body acquired. |
| [Publisher handbook chapter route](https://www.sciencedirect.com/science/chapter/handbook/pii/B9780444529374500101) | Search-indexed record confirms volume 11, 2012, pp. 513–610 and DOI; direct retrieval failed. Indexed content consists of introductory/section snippets and citation material. | Metadata and snippets, not a complete 98-page text. |
| [Publisher ordinary PDF route](https://www.sciencedirect.com/science/article/pii/B9780444529374500101/pdfft?isDTMRedir=true&download=true) | Web request returned a retrieval/cache failure. | No PDF body or source hash. |
| [Author CV endpoint](https://www.johnwoods.ca/John_Woods_CV.pdf) | Indexed CV entry 128 gives the exact chapter, editors, year and pp. 513–610; direct PDF request returned a 502 retrieval error. | Identity corroboration from an indexed author document only. |
| [Current former author homepage](https://www.johnwoods.ca/) | Returned unrelated casino-game content. | The page is not current academic source-body evidence. No assumption is made about why the site's content changed. |
| [Legacy author Index.htm](https://www.johnwoods.ca/Index.htm) | Search results retained an academic description; direct attempts were unavailable through the web tool. | No recovered publication links or body. |
| [UBC author profile](https://philosophy.ubc.ca/profile/johnwoods/) | The institutional profile identifies Woods and selected publications; it points to the former personal site but does not supply this chapter body in the retrieved material. | Institutional identity, not chapter acquisition. |
| [CAS institutional PDF](https://web.flu.cas.cz/scan/323557072.pdf) | The actual PDF contains **two pages**, the volume title and contents. Woods starts at 513 and the next chapter at 611. | A misleadingly promising PDF filename; it is not the full volume or chapter. |
| [ResearchGate record](https://www.researchgate.net/publication/288318962_A_History_of_the_Fallacies_in_Western_Logic) | Explicitly states that full text is unavailable and offers a request form. Its displayed 514–610 range differs from the publisher record. | No request or external message sent. Publisher/author identity controls the 513–610 target. |
| Exact-title and DOI searches across institutional, author and PhilArchive routes | Returned the record above, bibliography entries, excerpts citing Woods, and different papers/books. | No complete matching primary body was identified in those results; none was substituted. |
| Public archive and DOI-based open-access metadata endpoints | The web tool rejected or could not retrieve the attempted archive/OpenAlex/SemanticScholar endpoints. | No open-access status was inferred from these tool failures. |
| Bounded local manuscript/source and library filename searches | No matching full chapter/volume was found by the checked title/author/ISBN patterns. Existing old author-CV retry bodies were empty. Unrelated inaccessible temporary dependency directories were not treated as missing book evidence. | Filename search is limited evidence, not a full library-content inspection. |

The exact publisher start page is independently consistent with the 2012 author-CV entry and the actual two-page contents scan. The chapter's superscript footnote marker in some catalog titles is not part of a different work identity. Current shop or index posting dates are not substituted for 2012.

## Final native retrieval check

The root completed the final bounded requests through its working authorized network route, using ordinary TLS validation. These are the reported concrete outcomes:

- **OpenAlex: HTTP 200.** The DOI record identifies the exact chapter and returns `is_oa=false`, `oa_status=closed`, `oa_url=null`, `any_repository_has_fulltext=false` and `best_oa_location=null`. Its sole DOI location has no `pdf_url`. [DOI-based OpenAlex record](https://api.openalex.org/works/https://doi.org/10.1016/B978-0-444-52937-4.50010-1).
- **Semantic Scholar: HTTP 200.** The exact 2012 chapter is paper `89b622367dfe206abd95cb081505aa6b7da5b117`; `openAccessPdf.url` is empty and status is `CLOSED`. [DOI-based Semantic Scholar record](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/B978-0-444-52937-4.50010-1?fields=title,year,openAccessPdf,url).
- **Legacy author index: HTTP 200 after redirect.** `https://www.johnwoods.ca/Index.htm` redirects to `https://www.johnwoods.ca/` and returns **25,428 bytes** of *Casino Games Explained* content. It is not the requested chapter or an academic publication index.
- **Ordinary publisher PDF route: HTTP 403.** The exact `article/pii/B9780444529374500101/pdfft?isDTMRedir=true&download=true` request did not return a qualified PDF.

Open-access-index flags describe those services' records; they do not prove that no free copy exists anywhere. Together with the checked author, publisher, institutional and local routes above, they establish the bounded result of this block: **no complete matching free body was acquired**. No payment, external contact request, login workaround or access-control bypass was attempted.

## Authoring and comparison state

This acquisition block is concluded with the source-dependent step blocked: **no complete Woods source body has been qualified, hashed or read**. Consequently:

- No Woods source-specific manuscript or annex text has been written.
- No source-dependent claim about Woods's actual Aristotle analysis has been added to the existing refutation-diagnosis chapter.
- The already authored Aristotle translation treatment remains intact and independently identified.
- No part of Woods's 98-page chapter is credited from an abstract, quoted paragraph, modern taxonomy or adjacent publication.

Once a complete free body is obtained, verify its title, author, original volume/year, beginning at printed 513, ending at 610, all twelve sections, all necessary source apparatus, readability and hash. Then read the complete extent, reconstruct the mapped presentation, and compare the actual Aristotle section with the already written chapter. Record actual shared arguments and materially different interpretations; reuse a shared reconstruction only where source identity and content support doing so. Until then this is a specific source-acquisition blocker, not an unresolved scope or source-identity question.

The whole 98-page source, all sixteen mapped components and the actual Woods/Aristotle comparison remain open. No authoring completion state or canonical coverage record was changed. The two reserved manuscript destinations remain absent; this record is the only new artifact from the source-dependent acquisition block.

## Public-source continuation, 1 October 2026

This bounded continuation read the complete preceding note and the connected
refutation-diagnosis source note. It tried archived author publication links,
alternate cataloged scans and the public author repository profile. It did not
replay the unchanged publisher PDF or closed-index routes from the earlier block.

| New route | Actual observed result | Source-body consequence |
| --- | --- | --- |
| [Wayback CDX author PDF index](https://web.archive.org/cdx/search/cdx?url=johnwoods.ca%2F%2A&output=json&filter=statuscode%3A200&filter=mimetype%3Aapplication%2Fpdf&collapse=urlkey) | Ordinary HTTPS request timed out after 35 seconds; the web tool also could not retrieve it. | No archive listing or body obtained. |
| [Archived author index availability](https://archive.org/wayback/available?url=www.johnwoods.ca%2FIndex.htm&timestamp=20190101) and [homepage availability](https://archive.org/wayback/available?url=www.johnwoods.ca%2F&timestamp=20200101) | Both ordinary availability requests returned HTTP 429. | No capture URL or archived publication links recovered. No restriction was bypassed. |
| [Internet Archive volume-title search](https://archive.org/advancedsearch.php?q=title%3A%22Logic+a+history+of+its+central+concepts%22&output=json&rows=25) | HTTP 200, 287 bytes, `numFound=0`. | No matching volume scan from this query. |
| [Internet Archive print/e-book ISBN search](https://archive.org/advancedsearch.php?q=isbn%3A9780444529374+OR+isbn%3A9780080931708&output=json&rows=25) | HTTP 200, 252 bytes, `numFound=0`. | No matching scan from these identifiers. |
| [Public Woods author profile](https://independent.academia.edu/JohnWoods54) | The retrieved public publication list includes related fallacy papers and a different handbook chapter, *Varieties of Bayesianism*. It does not list the selected 2012 chapter. | Related works were not substituted or downloaded as target evidence. |
| [DBLP exact record](https://dblp.org/rec/series/hhl/Woods12.xml) | Native request returned HTTP 200 with 3,265 bytes of a bot-verification HTML page, not the requested record. | No unpaywalled source link was recovered. No challenge was completed. |

Exact-title searches constrained to UBC's open repository returned no matching
chapter result. This is limited search-index evidence. Citation pages, bookshop
listings and the previously identified two-page contents PDF were not treated as
the 98-page source. No qualified target body was acquired, hashed or read during
this continuation.

**Outcome:** the Woods source presentation and the actual Woods/Aristotle
comparison remain open. No manuscript, annex, intake or canonical coverage state
was changed. Further acquisition should start from a concrete newly available
author/repository deposit or cataloged public body rather than repeat the failed
routes recorded here.
