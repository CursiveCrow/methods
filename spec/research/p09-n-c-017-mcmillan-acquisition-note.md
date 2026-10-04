# N-c-017.c: McMillan book acquisition recheck

Date: 2026-09-06. Scope: a bounded author/publisher/institutional search for
the revised 1993 book, not another reconstruction from the 1992 thesis.

## Outcome

No complete, legitimately accessible 1993 book body was obtained through the
routes checked below. This is a route-bounded finding, not a claim that no
authorized copy exists. The acquisition gap in the
[earlier acquisition note](p09-mcmillan-1993-acquisition-note.md) and the
[source presentation record](p09-source-presentations-lot2-3.md) remains open.

## Live primary-source checks

- **Publisher identity.** Springer's record identifies Kenneth L. McMillan,
  *Symbolic Model Checking*, first edition, Kluwer copyright 1993, XVII + 194
  pages. The hardcover ISBN is 978-0-7923-9380-1, dated 31 July 1993. The
  electronic ISBN is 978-1-4615-3190-6 and DOI is
  10.1007/978-1-4615-3190-6. The record dates electronic publication to
  6 December 2012 while retaining first-edition status and 1993 copyright;
  that later delivery date alone does not establish an author revision.
  [Publisher book record](https://link.springer.com/book/10.1007/978-1-4615-3190-6).
- **Publisher access.** The book page identifies subscription content and
  offers institutional login. The inspected SMV chapter page does likewise;
  it exposes an abstract and preview link, not its complete pp. 61–85 body.
  The ordinary public preview request returned a retrieval cache miss in
  this session. That retrieval failure is not itself evidence of a paywall;
  the subscription/login status is stated separately on the chapter page.
  [The SMV System, DOI suffix `_4`](https://link.springer.com/chapter/10.1007/978-1-4615-3190-6_4);
  [advertised preview route](https://page-one.springer.com/pdf/preview/10.1007/978-1-4615-3190-6_4).
- **Author routes.** The thesis page distinguishes the original report
  CMU-CS-92-131 from a revised Kluwer hardback, ISBN 0-7923-9380-5, catalog
  number TK7888.4.M43 1993. Its download resolves to `pubs/thesis.pdf`.
  More decisively, the author's publication list has separate entries:
  item 17 is the 1993 Kluwer book with a bibliography link only; item 16 is
  the 1992 Carnegie Mellon thesis with the PDF link. No separate book PDF
  is offered by those inspected entries.
  [Author thesis page](https://mcmil.net/thesis.html);
  [author publications, 1993/1992 entries](https://mcmil.net/pubs/);
  [author-linked thesis PDF](https://mcmil.net/pubs/thesis.pdf).
- **Institutional route.** CMU's doctoral-degree list places McMillan and
  *Symbolic Model Checking: An approach to the State Explosion Problem*
  under academic year 1991–1992, with Edmund Clarke as adviser. The linked
  individual record did not load in this session. The visible institutional
  entry supports thesis identity, not acquisition of the revised book.
  [CMU doctoral degrees, page 9](https://www.csd.cs.cmu.edu/academics/doctoral/degrees-conferred?page=9).

Four targeted searches covered the exact book title/year on institutional
domains, the exact electronic ISBN, CMU, and the author's domain. Returned
CMU publication lists, degree records, and papers citing the book did not
provide its body. A citation inside another publication was not treated as
an acquired chapter. No purchases, logins, author contacts, access-control
bypasses, or unverified mirror downloads were attempted.

## Actual-file identity boundary

The existing local `tmp/pdfs/p09-mcmillan-1993/thesis.pdf` was rechecked:
1,712,433 bytes, SHA-256
`A458477801CBC806D9290F6F5FAF367A6860956FA52258EDDDF83A9DD4CDDFBF`.
It is unchanged from the file whose title page was inspected in the earlier
acquisition note: May 1992, CMU-CS-92-131, PhD submission, 1992 copyright.
Those title-page readings are inherited from that recorded inspection, not
newly inferred from the filename. The live web PDF reports 214 pages but
its extracted first-page text is garbled. A local text-only extraction
attempt failed on a MiKTeX data-directory permission error; no environment
repair or page rendering was undertaken for this bounded search.

## Remaining acquisition requirement

Obtain an authorized complete copy of the 1993 revised body, or the complete
relevant publisher chapters, and inspect its own identifiers and printed
pages. The chapter abstracts, contents, and the unchanged 1992 thesis cannot
establish the book's exact SMV grammar/semantics, partitioned transitions,
algorithms, examples, theorem numbering, or proofs. Keep the book's
presentation open; writing from already acquired sources can continue.
