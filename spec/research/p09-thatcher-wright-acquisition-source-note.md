# Thatcher-Wright: bounded primary-source acquisition record

Date: 2026-09-06.

## Outcome

The full 1968 journal article and the same-title 1966 IBM report RC-1713
were **not acquired** in this bounded search. No authorized publicly
readable full copy was located in the checked local holdings, publisher,
IBM, author-site, repository, or open-copy discovery routes. This is a
dated acquisition result, not a claim that no copy exists anywhere.

Consequently there is no new source-controlled technical reconstruction
of the article's definitions, theorems, or proof architecture. The active
N15 boundary remains accurate about this missing body. TATA's definitions
and proof cannot be assigned to the 1968 article on the strength of its
abstract or later citations.

This record supplements the earlier
`spec/research/p09-thatcher-wright-1968-acquisition-note.md`; it records
the current checks rather than treating the older access results as current.

## 1. Verified journal identity

J. W. Thatcher and J. B. Wright (James W. Thatcher and Jesse B. Wright),
**Generalized finite automata theory with an application to a decision
problem of second-order logic**, *Mathematical Systems Theory* **2**(1)
(March 1968), **57-81**, DOI
[10.1007/BF01691346](https://doi.org/10.1007/BF01691346).

The [current Springer article record](https://link.springer.com/article/10.1007/BF01691346)
confirms the title, author initials, volume, pagination, issue date, and
receipt on 1 August 1967. It identifies both authors with the IBM Watson
Research Center. The displayed historic journal name is *Mathematical
Systems Theory*; the platform's current journal umbrella is *Theory of
Computing Systems*. These should not be confused when recording the
1968 publication.

The [IBM publication record](https://research.ibm.com/publications/generalized-finite-automata-theory-with-an-application-to-a-decision-problem-of-second-order-logic)
independently gives 1 March 1968, both authors, the journal, the abstract,
and a link to the DOI. The live bibliography entry `ThatcherWright1968`
already matches the verified journal metadata. The occasional 57-82
citation in later literature is not the controlling pagination.

## 2. Local holdings checked first

Filename searches covered the repository and, with ignored files included,
`tmp/pdfs`, `tmp/sources`, and `tmp/acquisition`. Searches used the author
names, RC-1713/1713, the DOI suffix, and the N15 identifier. The previous
acquisition record and the active N15 ending were also read.

No target article or same-title report appeared in these holdings. The
relevant local full PDF is instead

`tmp/pdfs/p09-thatcher-1965/6511049.pdf`.

Its current file length is 2,216,329 bytes and its SHA-256 is
`90F15B358E7ADA0B7BC60FA7985C73363A60B92AC200B9EB9A4A9A27AD784B52`.
The PDF has 89 pages. Its first two physical pages were read directly:

- The microfilm cover identifies **Decision Problems and Definability for
  Generalized Arithmetic**, James Winthrop Thatcher, University of Michigan,
  Ph.D., 1965, negative microfilm 65-11,049.
- The dissertation title page has the same separate title, gives 1964,
  and lists Jesse B. Wright on the doctoral committee.

It is therefore not the jointly authored 1968 article or the same-title
RC-1713 report. The publisher's reference list for the 1968 article
separately cites Thatcher's dissertation as IBM Research Report **RC 1316**,
November 1964. The cover/title-page dates and the distinct report numbers
are retained rather than collapsed into one version. No content comparison
with an unacquired article or report is claimed.

## 3. Refreshed public routes and their actual results

| Route | Current result | What it supports |
| --- | --- | --- |
| Springer article/DOI page | Labels the displayed material a preview of subscription content; offers institutional access or article purchase; explicitly says no SharedIt link is currently available | Verified metadata, abstract, references; no full body |
| IBM Research, exact 1968 record | Abstract and DOI route only, with no paper download resource | Institutional bibliographic corroboration; no full body |
| OpenAlex DOI lookup | Work `W2035020702`; `is_oa=false`, `oa_status=closed`, `any_repository_has_fulltext=false`, `best_oa_location=null`; sole recorded location has no PDF URL | No open copy indexed there; not proof of global absence |
| Internet Archive exact volume metadata | Public endpoint for `theory-of-computing-systems_1968_2_1-4` returned no item metadata or files | The old archive lead yielded no publicly readable scan in this visit |
| Maintained JimThatcher.com author archive | The about page records IBM and automata work; the inspected page and targeted search supplied no article or report download | Author background only |
| Exact-title, DOI, report-number, IBM, HathiTrust, Internet Archive, and Deep Blue searches | Publisher/institutional metadata and citations; no complete target PDF | Additional discovery checks without target acquisition |

The OpenAlex endpoint read was
`https://api.openalex.org/works/https://doi.org/10.1007/BF01691346`.
The archive endpoint read was
`https://archive.org/metadata/theory-of-computing-systems_1968_2_1-4`.
The current response does not justify repeating the older note's stronger
claim about the archive item's hidden status; it simply supplied no files.

The [maintained author-site page](https://jimthatcher.com/about.htm) is
hosted by Knowbility as an archive of Thatcher's content. It is not a
research-paper repository in the material inspected here.

## 4. RC-1713 remains a distinct precursor lead

Contemporary references identify the same-title item as an IBM Research
Paper/Report **RC-1713 (1966)**, jointly authored by Thatcher and Wright.
A current independently accessible example is the reference list on
printed p. 491 of W. S. Brainerd's *The Minimalization of Tree Automata*,
preserved in the [Naval Postgraduate School institutional repository](https://calhoun.nps.edu/server/api/core/bitstreams/729033fd-f419-43b0-a021-58a6c05d11a0/content).
This is evidence for the report citation, not its technical body.

Neither RC-1713's title page nor its body was obtained. There is therefore
no verified page count, exact issue date, source-file hash, physical page
map, or theorem-by-theorem comparison with the 1968 publication. Those
fields remain unavailable rather than inferred from the journal article.

The distinct dissertation/RC-1316 item above is not a substitute for
RC-1713 merely because it is earlier work by Thatcher under Wright.

## 5. A readable later-paper lead, kept separate

IBM supplies a download route for Thatcher's **Transformations and
translations from the point of view of generalized finite automata theory**,
STOC 1969, 129-142, DOI `10.1145/800169.805427`:

[IBM institutional record](https://research.ibm.com/publications/transformations-and-translations-from-the-point-of-view-of-generalized-finite-automata-theory).

The corresponding publisher landing page marks that separate paper free
access. Its abstract says that Sections 2-3 present generalized automata
basics and their relation to context-free languages before developing tree
transformations. This is a **later, differently titled, single-author
paper**, not the requested journal article or report. Its full body was
not downloaded or reconstructed in this bounded task, and its advertised
content is not used as evidence for the 1968 paper's exact statements.

## 6. What can and cannot now be stated in N15

The publisher and IBM abstract support the limited historical description
that the paper works with finite algebras, proves recognizability closure
results, develops a generalized Kleene theory, and applies it to a
second-order decision problem. They do not expose the algebraic signature,
recognition map, exact regular operations, language and semantics of the
logical application, numbered theorem statements, examples, or proofs.

Accordingly, this visit supplies no basis for replacing the N15 source
boundary by a technical reconstruction attributed to Thatcher-Wright 1968.
The missing acquisition target remains the complete article at pp. 57-81,
or a complete authoritative RC-1713 scan kept explicitly at precursor
standing until compared with the article.

Once either body is available, the source packet needs the actual title
page, page map, and file identity; the finite algebra and recognition
definitions; closure and Kleene statements with their hypotheses; the
exact second-order structure and quantifier range; the theorem/proof
architecture; and a source-controlled example. No such technical details
were invented from the abstract in this task.

The bounded search stops here because the inspected independent routes
have converged on metadata or unavailable bodies. No publication was
purchased, no contact or access request was sent, and no source copy was
saved. The allowed `tmp/pdfs/p09-thatcher-wright-1968` directory was not
needed or created. Only this note was written; no handbook edits, tests,
manuscript builds, renders, or additional agents were performed.
