# Thatcher-Wright 1968: new public-link checks, 2026-09-08

Bounded acquisition pass: 2026-09-08, 08:11-08:18 UTC. The assigned
maximum was 15 minutes; the pass ended earlier after the new concrete
links returned bibliographic records without an article file.

## Result

No PDF of the exact 1968 article was acquired or saved. No capture
folder was created. The full text and complete printed page sequence
57-81 remain unavailable from the routes checked here.

The target is J. W. Thatcher and J. B. Wright, *Generalized finite
automata theory with an application to a decision problem of second-order
logic*, Mathematical Systems Theory 2(1) (1968), 57-81,
DOI [10.1007/BF01691346](https://doi.org/10.1007/BF01691346).

## Retrieved Content

### MaRDI paper record: full-work field

Source: [MaRDI Q5592253](https://portal.mardi4nfdi.de/wiki/Generalized_finite_automata_theory_with_an_application_to_a_decision_problem_of_second-order_logic),
retrieved 2026-09-08 at approximately 08:17 UTC. The following extracts
are separate complete HTML lines: first the field label, then its linked
value. Intervening page markup is not transcribed.

```html
<span class="pub-meta-label"><a href="/wiki/Property:P205" title="Property:P205">Full work available at URL</a></span>
```

```html
<a rel="nofollow" class="external text" href="https://doi.org/10.1007/BF01691346">https://doi.org/10.1007/BF01691346</a></span>
```

### Dresden reading list: exact target's DOI anchor

Source: [Formale Baumsprachen, Sommersemester 2017](https://www.orchid.inf.tu-dresden.de/teaching/2017ss/wta/),
Literatur, entry TW68, retrieved 2026-09-08 at approximately 08:17 UTC.
This is the complete anchor inside the target's bibliographic entry.

```html
<a href="http://dx.doi.org/10.1007/BF01691346">10.1007/BF01691346</a>
```

## Supplementary Notes

The latest September 6 acquisition status and its complete reading-list,
archive, and institutional follow-ups were read before source searching.
The older university, archive, citation-access, and initial acquisition
notes were searched for already attempted hosts and consulted at the
relevant passages. The Springer subscription/cart route, SciSpace signup,
Scholars Portal restriction, completed eighteen-file repository search,
and known nonmatching historical works were not reopened as new leads.

The local filename inventory used `rg --files --hidden --no-ignore`,
excluding only `.git`, and matched Thatcher, Wright, BF01691346,
RC-1713 variants, generalized/finite-automata names, journal ISSN and
page-range variants. Target-related results were the existing acquisition
notes and two locations for the already known Thatcher dissertation:
`citations/Thatcher - Decision Problems and Definability for Generalized Arithmetic (1964, dissertation, 1965 microfilm record).pdf`
and `tmp/pdfs/p09-thatcher-1965/6511049.pdf`. No target-named 1968
capture was found. This filename check does not identify every generic
PDF in the repository by content.

The new concrete lead outcomes were:

- **MaRDI Q5592253:** ordinary public HTTP retrieval succeeded with status
  200, HTML, 86,470 bytes. The full-work field contains only the target
  DOI. The outgoing links also expose zbMATH accession 0196.01901 and a
  MaRDI FDO metadata route; no PDF URL was exposed. The indexed second
  MaRDI record Q5538923, associated with zbMATH DE number 3252205, also
  lists only the DOI as its full-work URL. The second record's page was
  not successfully opened; that observation is limited to indexed text.
- **Dresden 2017 reading list:** ordinary public HTTP retrieval succeeded
  with status 200, HTML, 56,511 bytes. The full course page and attachment
  list were inspected. TW68 has the DOI anchor quoted above; the page's
  PDFs are course exercises or different literature, with no separate
  target-article attachment.
- **[SIGMOD's archived DBLP volume 2 index](https://www.sigmod.org/publications/dblp/db/journals/mst/mst2.html):**
  the complete 39-line web-reader result was inspected. The volume 2,
  number 1 target entry gives 57-81 and links its authors and BibTeX
  record. It has no article-file link. The site's old volume index is
  bibliographic evidence, not a journal scan.

One previously unresolved technical route was retried explicitly as an
old lead: the [Fatcat exact-DOI lookup](https://api.fatcat.wiki/v0/release/lookup?doi=10.1007%2FBF01691346).
Its ordinary request again reached the configured 20-second timeout and
returned no release record or file URL. This is not a new holding.

Initial Windows-sandbox requests to MaRDI and Dresden failed TLS setup;
curl reported `SEC_E_NO_CREDENTIALS`. The approved ordinary requests
outside that sandbox subsequently returned the successful public HTML
responses recorded above. No remote login or access restriction was
bypassed. The web reader separately failed to open the MaRDI pages;
the first record was verified through its actual HTTP response instead.

No paid access, account creation, external correspondence, manuscript
edits, tests, builds, or manuscript rendering occurred. The research and
PDF skills were read personally. No PDF candidate reached identity or
page-extent verification, so there is no target-file hash and no source
acquisition claim. These checks supply no new verified download lead;
they do not establish that a public copy cannot exist elsewhere.
