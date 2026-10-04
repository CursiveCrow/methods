# Safra 1988: bounded proceedings acquisition follow-up

Date: 2026-09-06, local time. Search began at 2026-09-07 01:24:57 UTC.

## Outcome

The exact nine-page **FOCS 1988 proceedings paper remains unacquired**.
No new target PDF was saved. This pass verified the actual IEEE Computer
Society article page in the live browser, including its explicit sign-in
requirement for the PDF. The author directory still exposes the held
twenty-page expansion rather than an identified proceedings facsimile.

Consequently no new body-level comparison of the 1988 paper with the
1995 expansion can be claimed. The two source identities remain distinct.
This is a bounded access result, not a claim of worldwide unavailability.

## Exact target and prior evidence read

Shmuel Safra, **On the Complexity of omega-Automata**, *29th Annual
Symposium on Foundations of Computer Science*, White Plains, New York,
24-26 October 1988, IEEE, **pp. 319-327**, DOI
[10.1109/SFCS.1988.21948](https://doi.org/10.1109/SFCS.1988.21948).

The live `Safra1988` bibliography entry and
`spec/research/p09-safra-1988-source-note.md` were read first, together
with the held Crossref and DBLP metadata. The target is IEEE FOCS, not
an ACM proceedings article. Safra and Vardi's **On omega-Automata and
Temporal Logic**, STOC 1989, DOI `10.1145/73007.73019`, is a different
paper and was not substituted for it.

## Fresh publisher checks

The actual IEEE Computer Society resolver in the held DBLP record,
[doi.ieeecomputersociety.org/10.1109/SFCS.1988.21948](https://doi.ieeecomputersociety.org/10.1109/SFCS.1988.21948),
redirected successfully to
[the CSDL article](https://www.computer.org/csdl/proceedings-article/focs/1988/021948/12OmNqBbI2f).
Its plain HTML is a JavaScript application shell. The page was therefore
opened in the live browser and allowed to load normally. The resulting
visible page identified:

- title **On the complexity of omega -automata**;
- **S. Safra**, Department of Applied Mathematics, Weizmann Institute;
- **year 1988, pages 319-327**;
- exact DOI **10.1109/SFCS.1988.21948**;
- a PDF control labelled **Sign in and then download the PDF for this
  article**.

No sign-in, membership, transaction, or account operation was performed.
The visible record and its PDF control establish the current access
result; a successful HTML response does not establish PDF acquisition.

The ordinary [Xplore record](https://ieeexplore.ieee.org/document/21948)
returned **HTTP 202, text/html**, without article links in its direct
response. These ordinary retrieval requests also failed to return PDF
bytes:

| Route | Result |
| --- | --- |
| `https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=21948` | HTTP 418 |
| Held Crossref VOR locator, `http://xplorestaging.ieee.org/ielx2/219/889/00021948.pdf?arnumber=21948` | HTTP 418 |
| Same article-path probe on current Xplore host, `https://ieeexplore.ieee.org/ielx2/219/889/00021948.pdf?arnumber=21948` | HTTP 418 |

The last item is explicitly a path probe derived from the Crossref
locator, not an independently discovered download link. No challenge or
access-control bypass was attempted. A fresh DBLP XML request returned
503; the previously held XML supplied the exact Computer Society
resolver that was then successfully followed and verified.

## Fresh author and public reading-link checks

Safra's [actual university directory](https://www.cs.tau.ac.il/~safra/PapersAndTalks/)
returned HTTP 200. Its file links were inspected. The link for the
relevant determinization manuscript remains `DBA.ps`; no separate
1988 proceedings PDF was identified. The held file's header was checked
again directly:

```text
%%Title: jcss.dvi
%%CreationDate: Tue Mar 21 15:47:45 1995
%%Pages: 20
```

That file is already preserved as
`tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps`. The directory's other
automata-related PDF, `dsa.pdf`, is the separately titled strong-fairness
determinization paper, not the target.

Additional concrete reading routes checked:

- [ltl2dstar documentation](https://www.ltl2dstar.de/docs/ltl2dstar.html):
  the actual Safra bibliography link goes to
  `http://dx.doi.org/10.1109/SFCS.1988.21948`; its nearby PDF link is
  Klein's diploma thesis, not Safra's article.
- [FLOLAC 2009 temporal-logic course](https://flolac.iis.sinica.edu.tw/flolac09/tl.html):
  actual public attachments are course slides on Buchi automata,
  complementation, and temporal logic. The Safra reference has no
  target-PDF attachment in the inspected links.
- [UCSD CSE 291, Spring 2006 readings](https://cseweb.ucsd.edu/classes/sp06/cse291-a/readings.html):
  the actual page lists the exact Safra citation, but its outgoing PDF
  list contains other readings rather than a linked Safra body.
- [Stanford's 1988-1989 AFLB calendar](https://theory.stanford.edu/~aflb/1988-89.html)
  surfaced a contemporary Safra talk on 17 November 1988 with the
  matching title and abstract. This is a talk announcement, not the
  proceedings pages.

Exact title/DOI searches and filename variants `safra88.pdf`,
`safra1988.pdf`, and `safra-1988.pdf` returned later citing documents or
metadata; no complete nine-page target candidate emerged.

## Version-comparison standing

The held 1995 manuscript is authenticated in the earlier source note
as an expanded version of the FOCS paper. Its header confirms twenty
pages. The independently verified proceedings record requires nine
pages, 319-327. These are verified identity/extent differences.

Exact differences in theorem numbering, event conventions, proofs,
figures, bounds, and applications cannot be inferred merely from those
extents or the common abstract. No such body-level comparison was
performed in this follow-up, because the 1988 body was not obtained.

Only this new note was authored. Existing source copies, other notes,
and manuscript files were preserved. No tests, builds, or renders were
run, and no external correspondence was sent.
