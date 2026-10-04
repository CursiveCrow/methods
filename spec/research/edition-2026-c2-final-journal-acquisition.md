# Edition 2026 C2: bounded final-journal acquisition follow-up

Date: 7 September 2026. Acquisition investigator:
`/root/p4b_corrected_admission/terminal_selection_check`, reassigned by the
root agent to this independent source-location task. Scope: free public
author, institutional, publisher and archive leads for the exact final
journal body. No manuscript comparison or source-admission verdict was
assigned.

## Outcome

**The exact final journal body was not acquired. SF-C2-02 remains open.**
The target is Christel Baier, Boudewijn Haverkort, Holger Hermanns and
Joost-Pieter Katoen, *Model-Checking Algorithms for Continuous-Time Markov
Chains*, *IEEE Transactions on Software Engineering* 29(6), 524-541,
June 2003, DOI [10.1109/TSE.2003.1205180](https://doi.org/10.1109/TSE.2003.1205180).
The [Twente journal record](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains/)
was reopened and supplies that identity; its Access to Document section
lists the DOI and does not offer a journal PDF. The open-access file shown
under related research output belongs to the separate April 2002 report.

A new freely downloadable author-institutional PDF was found through the
[RWTH publication catalogue](https://www-i2.moves.rwth-aachen.de/i2/publications/).
Its actual printed masthead and pagination identify the same unresolved
July/no. 7/pages 1-18 manifestation class already described in the source
review. It does not satisfy the June/no. 6/pages 524-541 requirement.
No final-journal PDF or final-journal hash is reported, and no PDF was added
to the project's retained source-reference tree.

## Prior records consulted before acquisition

Read completely:

- `spec/verification/edition-2026-c2-source-review-r2.md`;
- `spec/research/edition-2026-c2-review-repairs.md`;
- `spec/verification/edition-2026-c2-source-review.md`.

Also inspected the source-acquisition section of
`spec/research/edition-2026-c2-csl-correction.md` and the CTMC/CSL source
section of `spec/research/p09-source-presentations-lot4.md`, lines 2223-2275.
The earlier reports distinguish the held 37-page CTIT 02-10 report, the
July/no. 7 typeset candidate, and the required final journal. Their recorded
failed IEEE/RG/CiteSeer routes were not treated as body evidence. The large
`acquisition-src-*` corpus was not read or searched for content.

## New leads and precise outcomes

| Lead | Actual outcome in this pass |
| --- | --- |
| [RWTH historical publication catalogue](https://www-i2.moves.rwth-aachen.de/i2/publications/) | Ordinary HTTPS request returned HTTP 200 and 548,903 bytes of HTML. The row with the exact title, four authors and journal metadata links `https://www-i2.informatik.rwth-aachen.de/i2/pdfs/111.pdf`. |
| [RWTH linked article PDF](https://www-i2.informatik.rwth-aachen.de/i2/pdfs/111.pdf) | HTTP 200 after redirect to `https://www-i2.moves.rwth-aachen.de/i2/pdfs/111.pdf`; content type `application/pdf`; 952,093 bytes and 18 pages. Its printed first and last pages show volume 29, no. 7, July 2003, pages 1 and 18. All 18 extracted page markers run consecutively from 1 to 18. Rejected as the exact final journal. |
| [Historical Dresden author file](https://www.inf.tu-dresden.de/content/institutes/thi/algi/publikationen/texte/13_00.pdf) | A newly found indexed document mirror exposed this historical author URL. Ordinary HTTPS returned HTTP 404. The mirror's visible masthead is itself July/no. 7/pages 1-18; no final identity was inferred from the URL. |
| [Historical Twente FMT author file](https://fmt.cs.utwente.nl/publications/files/399_116221.pdf) | Newly located through references in indexed institutional project reports. Ordinary HTTPS returned HTTP 404. |
| [Historical publisher abstract](https://csdl.computer.org/comp/trans/ts/2003/06/e0524abs.htm) | The author's Saarland course bibliography identifies this historical route. HTTP 200 after redirect to `https://www.computer.org/csdl/journal/ts/2003/06/e0524/13rRUxcsYNE`; 8,211 bytes of HTML application shell, with no readable article body returned. |
| [Historical publisher PDF route](https://www.computer.org/csdl/trans/ts/2003/06/e0524.pdf) | HTTP 200 after redirect to the same current catalogue URL; the response is the same-size HTML application shell, not PDF bytes. This was a distinct publisher archive lead, not another attempt at the previously failed IEEE Xplore PDF URL. |
| [Internet Archive CDX lookup for the newly located FMT file](https://web.archive.org/cdx/search/cdx?url=fmt.cs.utwente.nl/publications/files/399_116221.pdf&output=json&filter=statuscode:200&filter=mimetype:application/pdf&collapse=digest&fl=timestamp,original,digest,length) | Ordinary HTTPS read timed out after the configured 20-second timeout. No archive capture or article bytes were obtained. |
| [OpenAlex DOI location record](https://api.openalex.org/works/https://doi.org/10.1109/TSE.2003.1205180) | Discovery index only: the response lists the DOI and Twente journal record, both with `pdf_url: null`, and no best OA location. This index result is not proof that no free copy exists. |

Additional title/DOI searches across Dresden, RWTH and Saarland sources
returned bibliographic records, citing papers, the already-known candidate,
or the failed historical URLs above. No new final-body lead succeeded.

## Candidate identity, custody and reading extent

The RWTH PDF has SHA256
`02c76f42027a8c5b3b01ef2ce7322e545c8c2c36875838b2481027d2113ef457`.
The same hash was checked on a subsequent download for visual inspection.
Its temporary local location is:

`C:/Users/Crow/AppData/Local/Temp/c2-final-acquisition-799a45722f8e4989be6fe097767e0c78/rwth-111-candidate.pdf`.

The PDF metadata title is `116221-2 1..18`; the creation/modification metadata
is dated 22 April 2003. These metadata values are supplementary observations,
not the basis for the version decision. The decision rests on the printed
masthead and page numbers.

Actual reading in this pass:

- Extracted and inspected the first-page title and full author line.
- Extracted and inspected the running mastheads/page numbers on all 18 pages.
- Rendered and visually inspected complete PDF pages 1 and 18, confirming
  the title, four authors, July 2003/no. 7 mastheads, endpoint page numbers,
  first-page publication details and last-page reference/author-biography
  layout.
- Did not read the intervening mathematical body, compare the candidate
  with the final journal, or compare source passages against the manuscript.

The temporary candidate supplies a reproducible source-location and version
rejection result. It supplies neither final-journal identity nor full source
review. The known report was not reopened or re-rendered in this pass.

## Handoff boundary

Only this new acquisition note was added to the repository. The manuscript,
bibliography, provenance records, held report and existing review files were
not changed. No account, purchase, message or access-control bypass was used.
All HTTP requests used normal TLS verification. The Research skill guided
primary-source tracing; the PDF skill guided the visual identity check.

SF-C2-02 still requires a readable exact-final-journal body with verified
identity and local hash, followed by the independent review's required
passage comparison. This bounded acquisition follow-up ends with that
obligation unresolved.
