# Thatcher–Wright 1968: archive and aggregator download follow-up

Date: 2026-09-06 Pacific time (checks conducted 2026-09-07, approximately 01:01–01:07 UTC).

## Target and outcome

The target is James W. Thatcher and Jesse B. Wright, “Generalized Finite Automata Theory with an Application to a Decision Problem of Second-Order Logic,” *Mathematical Systems Theory* 2(1) (1968), 57–81, DOI [10.1007/BF01691346](https://doi.org/10.1007/BF01691346). Acquisition requires the complete article, including all 25 printed pages. A metadata record, abstract, review, different paper, and the earlier IBM report do not establish acquisition of this article.

**No complete target PDF was obtained in this bounded follow-up.** No file was placed under `tmp/pdfs/p09-thatcher-wright-1968`. No PDF candidate reached the stage where its article title and complete page sequence could be verified. The results below concern the routes checked; they do not prove that no public copy exists anywhere.

The latest download status, earlier archive search, citation-access note, and university search note were read before the fresh checks. Previously inspected Internet Archive duplicate manifests, HathiTrust identifiers, Scholars Portal restrictions, Bitsavers directories, and university citation PDFs were not treated as newly available sources. The parent independently completed the ordinary browser check of Springer and the Google Scholar versions list during this follow-up.

## Fresh OpenAIRE aggregation check

The [OpenAIRE exact DOI API query](https://api.openaire.eu/search/publications?doi=10.1007%2FBF01691346&format=json) returned one aggregate record. Its journal fields identify volume 2, start page 57, end page 81, and ISSN 0025-5661. The record reports:

```text
bestaccessright: CLOSED / Closed Access
isgreen: false
collectedfrom: zbMATH Open; Crossref; Microsoft Academic Graph; DBLP
```

The aggregate's actual web resources reduce to the DOI and the [DBLP article record](https://dblp.org/rec/journals/mst/ThatcherW68.html). Its constituent records additionally supply the two zbMATH records [3311762](https://zbmath.org/3311762) and [3252205](https://zbmath.org/3252205). These constituent instances are marked closed access. The DBLP instance is marked unspecified access; it links to bibliographic metadata and the DOI, not an article PDF.

The strings “Unknown Repository” occur among the merged hosting labels for old Microsoft Academic Graph data. They do **not** supply a repository URL: the corresponding instance's web resource is the same DOI. Therefore this wording is not evidence of an undiscovered repository attachment. The record's “Springer TDM” license label likewise does not establish open access.

Attempts to open the two zbMATH pages through the web reader failed with a non-retryable URL safety error. No full-text URL was obtained from them. This is a retrieval limitation, not proof that their pages contain nothing beyond the aggregator data.

## Other aggregator and published-link checks

| Route | Actual result |
| --- | --- |
| [OpenAlex exact DOI work](https://api.openalex.org/works/https://doi.org/10.1007/BF01691346) | Work `W2035020702`; `is_oa: false`; `oa_status: closed`; `any_repository_has_fulltext: false`; only DOI location; `pdf_url: null`; `best_oa_location: null`. This refreshed a previously checked route. |
| [Semantic Scholar exact DOI record](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/BF01691346?fields=title,year,url,openAccessPdf,externalIds) | Paper `2727b71c9b7c73a9b6b64f0c025aca7a2a93de94`; 1968; `openAccessPdf.url` empty and status `CLOSED`. This refreshed a previously checked route. |
| [CORE exact-title search](https://core.ac.uk/search?q=%22Generalized%20finite%20automata%20theory%22) | Ordinary request returned HTTP 403. External indexed CORE search results were later works citing Thatcher–Wright, not the target article. |
| [Internet Archive Fatcat DOI lookup](https://api.fatcat.wiki/v0/release/lookup?doi=10.1007%2FBF01691346) | Ordinary request timed out after 20 seconds. The web reader also could not open the endpoint. No release record, file identifier, or archived PDF URL was obtained. This route remains unverified because of retrieval failure. |
| [Crossref exact DOI metadata](https://api.crossref.org/works/10.1007/BF01691346) | Supplies publisher full-text link metadata, including `http://link.springer.com/content/pdf/10.1007/BF01691346.pdf`, marked version of record / text mining. The metadata itself is not article access. |
| [Published Springer PDF endpoint, HTTPS](https://link.springer.com/content/pdf/10.1007/BF01691346.pdf) | Ordinary request returned HTTP 200 but `text/html; charset=utf-8`, 3,038 bytes, HTML title `Client Challenge`. These bytes were not saved as a PDF. The parent's independent normal browser check redirected to the subscription preview. |

Crossref also lists `http://link.springer.com/article/10.1007/BF01691346/fulltext.html` and the extensionless `http://link.springer.com/content/pdf/10.1007/BF01691346`. They are publisher endpoints associated with the same DOI. They were not represented as alternative public repository copies, and no access restriction was circumvented.

## Bounded archive and repository discovery

Fresh indexed searches combined the exact DOI, exact title (including the British spelling “Generalised”), authors/year/PDF, `RC1713`, `RC-1713`, and journal/year with archive, repository, scan, or digitized terms. Targeted CORE, Internet Archive, and HAL domain queries produced no new target full-text lead. The matches that did appear were citation passages in later theses, articles, proceedings, and course notes. A Bitsavers match was an IBM journal bibliography/news item discussing other 1968 papers; it did not supply the target article.

No fresh institutional attachment or complete journal-volume PDF was identified. The earlier archive note's Internet Archive duplicate-manifest entry `theory-of-computing-systems_1968_2_1-4` remains a catalog lead with no publicly returned item file list in the prior check. It is not a verified download. The previously identified Scholars Portal preserved volume remains an institutional access route, not a public PDF acquired here.

## Handoff

There is no verified public download link to hand off from this follow-up. The actionable technical residue is narrow: the Fatcat DOI lookup and the two zbMATH records were not successfully retrieved, and thus have not been exhausted as metadata-to-attachment checks. No evidence currently shows that any of those routes holds a complete file. This note records the unsuccessful acquisition honestly; it does not substitute a different paper or a source summary for the requested PDF.
