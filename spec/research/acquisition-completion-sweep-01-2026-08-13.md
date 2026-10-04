# Independent acquisition-completion sweep 01 — 2026-08-13

**Book:** *The Methods of Reason*  
**Sweep result:** **NOT CLEAN — NEW AUTHORITATIVE PRESENTATIONS FOUND; ALL SIX GOVERNED GAPS REMAIN OPEN.**  
**Standing:** discovery and adjudication input only. This report does not admit a source, fulfill a coverage row, close a gap, resolve rights, or alter any acquisition ledger.

## Scope and constraints

This is the first independent acquisition-completion sweep required by the completion plan. It was performed read-only against:

- the 68-source acquisition baseline in [`full-compendium-coverage-baseline.md`](full-compendium-coverage-baseline.md);
- the six governed gaps and two active provenance controls in [`../acquisition-gap-manifest.md`](../acquisition-gap-manifest.md);
- the source-local acquisition records under this directory; and
- successful responses from official publishers, standards bodies, maintained-system documentation, institutional catalogues, and bibliographic registries.

The sweep did not contact a rights holder, send any external message, retrieve subscription-only body text, or credit an inaccessible response as acquired. A search-result mention or a title inside another source's bibliography was not treated as an independently acquired presentation. Publisher or institutional metadata establishes only what that presentation actually exposes; it does not establish reproduction permission for protected expression.

Retrieval was performed on 2026-08-13 in the repository's `America/Los_Angeles` working context. All conclusions below are limited to the exact successful sources and queries recorded here.

## Digest

| Item | Result |
|---|---|
| Governed gaps inspected | 6 of 6 |
| Governed gaps closed by this sweep | 0 |
| Governed gaps still open | 6 |
| Provenance controls inspected | 2 of 2; both still active |
| Maintained-source version changes beyond the existing local records | none found |
| New or newly established independent presentation candidates | found on official Springer, Cambridge, College Publications, W3C, Library of Congress, and Open Library surfaces |
| Previously identified but still untranscribed chapter records | 135 DBLP `incollection` records for *Handbook of the History of Logic*, Volumes 1–10 |
| Rights-holder contacts | 0 |
| Inaccessible bodies credited | 0 |
| Can this sweep count as a no-new-presentation sweep? | no |

The acquisition state is therefore not ready to close. The discoveries in this report require governed adjudication, independent acquisition/admission where applicable, coverage regeneration, and another independent sweep. Because this sweep found new presentations, it is not one of the two consecutive no-new-presentation sweeps required for closure.

## Governed gaps

### ACQ-GAP-001 — *Handbook of Logic in Computer Science*, alleged Volume 6

**Verdict: OPEN. No Volume 6 publication identity was established.**

Successful exact queries:

1. `https://api.crossref.org/works?query.title=Handbook%20of%20Logic%20in%20Computer%20Science%20Volume%206&rows=20`
2. `https://openlibrary.org/search.json?title=Handbook%20of%20Logic%20in%20Computer%20Science%20Volume%206&limit=20`

The Crossref query returned five matching Oxford book records, with these DOIs:

- `10.1093/oso/9780198537809.001.0001`
- `10.1093/oso/9780198537618.001.0001`
- `10.1093/oso/9780198537625.001.0001`
- `10.1093/oso/9780198537359.001.0001`
- `10.1093/oso/9780198537816.001.0001`

The Open Library query returned `numFound: 0`. Neither successful response supplied a Volume 6 ISBN, DOI, title, publication date, or contents.

The unresolved disagreement remains exact: Oxford's descriptive prose says the handbook “comprises six volumes,” while the established book records and contents in the local source-ID baseline cover Volumes 1–5 only. The existing SRC-030 record also preserves a Cambridge institutional description of a chapter as intended for a “forthcoming Volume VI”; that wording is not a publication record. This sweep does not infer that Volume 6 was published, cancelled, renamed, or absorbed elsewhere.

A Google Books API query for the exact title plus “Volume 6” returned HTTP 429 and yielded no usable body. It is recorded as an access failure, not evidence for or against a volume.

### ACQ-GAP-002 — *Handbook of Boolean Algebras* volumes

**Verdict: OPEN. New bibliographic presentations establish a three-volume set and distinct Volume 1 and Volume 3 records; publisher contents for those volumes remain unacquired.**

Successful exact sources:

1. Library of Congress MARCXML: `https://lccn.loc.gov/88025140/marcxml`
2. Open Library Volume 1 lookup: `https://openlibrary.org/api/books?bibkeys=ISBN%3A044470261X&jscmd=data&format=json`
3. Open Library Volume 2 lookup: `https://openlibrary.org/api/books?bibkeys=ISBN%3A0444871527&jscmd=data&format=json`
4. Open Library Volume 3 lookup: `https://openlibrary.org/api/books?bibkeys=ISBN%3A0444871535&jscmd=data&format=json`
5. Open Library set lookup: `https://openlibrary.org/api/books?bibkeys=ISBN%3A0444872914&jscmd=data&format=json`
6. Existing official Elsevier Volume 2 page: `https://shop.elsevier.com/books/handbook-of-boolean-algebras/luisa/978-0-444-87152-7`

Successful-response SHA-256 values from this sweep:

| Response | SHA-256 |
|---|---|
| Library of Congress MARCXML | `619554cb679dd0d7d736c03bf3d7d060c3801a1d203115483e4474da28cca331` |
| Open Library ISBN `044470261X` | `6ca7527f39ee2b33c515864e58b9aa991ae9e41572024d5d88c497a61e39734f` |
| Open Library ISBN `0444871527` | `e84c68d062fb031d682ede4fe58cc0689fda5997b42fa694ba4df6d9271289e0` |
| Open Library ISBN `0444871535` | `8e0c58b8e5eb0914a4b9fecf6c8e6f61f652280ad9a896198a649414c9ea3b0f` |
| Open Library ISBN `0444872914` | `55e672476fdc3e2b8b6ffc226184cac23386b0b920452026d709d12095da91e1` |

Exact established metadata:

| Presentation | Record | Date | Extent / note |
|---|---|---:|---|
| Volume 1 | ISBN `044470261X`; Open Library `/books/OL21433659M` | 1988 | 311 pages; North-Holland |
| Volume 2 | ISBN `0444871527`; Open Library `/books/OL21437329M` | 1989 | 716 pages; North-Holland; already represented by SRC-043 through the Elsevier Volume 2 page |
| Volume 3 | ISBN `0444871535`; Open Library `/books/OL15046687M` | 1989 | 1,367 pages; North-Holland |
| Three-volume set | ISBN `0444872914`; Open Library `/books/OL2047887M` | 1989 | North-Holland; Elsevier Science Pub. Co. named as U.S./Canada distributor |

The Library of Congress record independently exposes `0444872914 (Set)`, `0444871535 (v. 3)`, the title *Handbook of Boolean algebras*, publication year 1989, and extent `3 v.`. These records establish identities that the current SRC-043-only source-ID baseline does not independently acquire.

No successful official Elsevier product/contents presentation for Volume 1 or Volume 3 was established in this sweep. The new library records therefore trigger acquisition and presentation-identity adjudication but do not close the gap or authorize inferred contents.

### ACQ-GAP-003 — *Handbook of the History of Logic* chapter granularity

**Verdict: OPEN. Exact chapter-level registry records are available and remain untranscribed for Volumes 1–10.**

Exact registry route pattern:

`https://dblp.uni-trier.de/db/series/hhl/hhl{VOLUME}.xml`

Successful live retrieval established the following `incollection` record counts:

| Volume | DBLP volume title | Year | ISBN | Chapter records |
|---:|---|---:|---|---:|
| 1 | *Greek, Indian and Arabic Logic* | 2004 | `978-0-444-50466-1` | 9 |
| 2 | *Mediaeval and Renaissance Logic* | 2008 | `978-0-444-51625-1` | 14 |
| 3 | *Rise of Modern Logic: From Leibniz to Frege* | 2004 | `978-0-444-51611-4` | 12 |
| 4 | *British Logic in the Nineteenth Century* | 2008 | `978-0-444-51610-7` | 16 |
| 5 | *Logic from Russell to Church* | 2009 | `978-0-444-51620-6` | 17 |
| 6 | *Sets and Extensions in the Twentieth Century* | 2012 | `978-0-444-51621-3` | 11 |
| 7 | *Logic and the Modalities in the Twentieth Century* | 2006 | `978-0-444-51622-0` | 10 |
| 8 | *Many Valued and Nonmonotonic Turn in Logic* | 2007 | `978-0-444-51623-7` | 11 |
| 9 | *Computational Logic* | 2014 | `978-0-444-51624-4` | 17 |
| 10 | *Inductive Logic* | 2011 | `978-0-444-52936-7` | 18 |
| 11 | *Logic: A History of its Central Concepts* | 2012 | `978-0-444-52937-4` | 12 |

Volumes 1–10 total 135 chapter records. Volume 11 totals 12 and is already separately represented by SRC-062. The DBLP routes were already named by SRC-063, so this is not a newly named series identity; it is direct confirmation that the owed chapter-level presentation exists and can be transcribed without inventing titles. It remains open until those exact records are acquired, reviewed, independently admitted, and linked without collapsing the separate Volume 11 presentation.

The primary `dblp.org` route began returning rate-limit/network failures during repeated access. The successful `dblp.uni-trier.de` institutional mirror responses are the only bodies credited here.

### ACQ-GAP-004 — maintained online sources

**Verdict: OPEN. No version identity newer than the existing local records was found on the checked official current-version pages.**

| Source | Exact live query | Live identity found | Already present locally |
|---|---|---|---|
| SRC-042 SMT-LIB | `https://smt-lib.org/language.shtml` | Version 2.7; latest linked release `smt-lib-reference-v2.7-r2026-03-27.pdf` | yes |
| SRC-052 Lean | `https://lean-lang.org/doc/reference/latest/` | Lean `4.34.0-rc1` | yes |
| SRC-052 Lean stable | `https://lean-lang.org/doc/reference/stable/` | Lean `4.33.0` | yes |
| SRC-053 Rocq | `https://rocq-prover.org/doc/V9.2.0/refman/` | Rocq Prover `9.2` / route `V9.2.0` | yes |
| SRC-054 Isabelle | `https://isabelle.in.tum.de/documentation.html` | `Isabelle2025-2` | yes |
| SRC-055 Agda stable | `https://agda.readthedocs.io/en/stable/` | Agda `2.8.0` | yes |
| SRC-055 Agda latest | `https://agda.readthedocs.io/en/latest/` | Agda `2.9.0` | yes |

This is a no-version-delta result only. It does not turn a maintained URL into a frozen source, replace any dated local snapshot, or close the rule that future snapshots must be separately attributed.

### ACQ-GAP-005 — unresolved metadata conflicts

**Verdict: OPEN. No conflict was adjudicated or normalized.**

| Source | Preserved disagreement confirmed in the local acquisition evidence |
|---|---|
| SRC-004, *Handbook of Computability Theory* | Elsevier's visible edition date is 1 October 1999 and its product data also exposes `publicationYear: 1999` and `onSaleDate: 1999-10-01`, while the same page exposes `datePublished` / `publicationDate: 2011-06-29`; Crossref exposes 1999. |
| SRC-030, HLICS Volume 5 | Oxford catalogue title *Volume 5. Algebraic and Logical Structures* versus printed title-page wording *Volume 5 Logic and Algebraic Methods*; Oxford/Crossref date 25 January 2001 versus LMS, DBLP, WorldCat, CiNii, and Oxford departmental 2000 records; Clarendon Press and Oxford University Press presentations remain distinct. |
| SRC-036, *Handbook of Knowledge Representation* | Elsevier's visible edition/on-sale date is 18 December 2007; the page also exposes `publicationYear: 2007` and `publicationDate` / `datePublished: 2008-01-08`; Open Library exposes 27 December 2007; Crossref chapter records expose 2008. |
| SRC-061, *Handbook of Quantum Logic and Quantum Structures: Quantum Structures* | Elsevier/ScienceDirect/PagePlace date, title-expansion, personal-name, index-locator, chapter-page, glyph, and diacritic variants recorded in SRC-061 remain unreconciled. |

The sweep found no official correction record that licenses choosing one field as the replacement for another. All variants must remain separately attributed until governed adjudication.

### ACQ-GAP-006 — broader acquisition completeness

**Verdict: OPEN. Multiple official publisher and standards-body presentations are not independent source-ID records in the current 68-source baseline.**

An occurrence inside another source's bibliography or raw Crossref reference array does not satisfy the one-presentation acquisition requirement. The baseline's 68 source headings contain none of the independent source headings listed below.

#### Springer Nature

1. *Handbook of Tableau Methods* — official book page and contents: `https://link.springer.com/book/10.1007/978-94-017-1754-0`; DOI `10.1007/978-94-017-1754-0`; 1999; the publisher labels 11 chapters and separately exposes front and back matter.
2. *Handbook of Defeasible Reasoning and Uncertainty Management Systems*, Volume 1, *Quantified Representation of Uncertainty and Imprecision* — `https://link.springer.com/book/10.1007/978-94-017-1735-9`.
3. The same series, Volume 3, *Belief Change* — `https://link.springer.com/book/10.1007/978-94-011-5054-5`.
4. The same series, Volume 4, *Abductive Reasoning and Learning* — `https://link.springer.com/book/10.1007/978-94-017-1733-5`.
5. The same series, Volume 5, *Algorithms for Uncertainty and Defeasible Reasoning* — `https://link.springer.com/book/10.1007/978-94-017-1737-3`.
6. The same series, Volume 6, *Dynamics and Management of Reasoning Processes* — `https://link.springer.com/book/10.1007/978-94-017-1743-4`.
7. The same series, Volume 7, *Agent-Based Defeasible Control in Dynamic Environments* — `https://link.springer.com/book/10.1007/978-94-017-1741-0`.

The series' Volume 2, *Reasoning with Actual and Potential Contradictions*, is already SRC-064. The official Springer records establish that SRC-064 is one volume in a seven-volume series, leaving Volumes 1 and 3–7 without independent source IDs.

#### Cambridge University Press

1. *The Description Logic Handbook: Theory, Implementation and Applications*, second edition — official book presentation `https://www.cambridge.org/core/books/description-logic-handbook/F050683766E57EE9BB07BC01BB7A7069`; DOI `10.1017/CBO9780511711787`; print publication year 2007; official contents presentation `https://www.cambridge.org/core/books/abs/description-logic-handbook/contents/8DDEF4FA6060409728271211A1E8E9F3`.

This work appears in existing bibliographies, but it is not an independent acquired source in the 68-source heading ledger.

#### College Publications

1. *Handbook of Deontic Logic and Normative Systems*, Volume 1 — `https://collegepublications.co.uk/handbooks/?00001=`; 31 October 2013; ISBN `978-1-84890-132-2`.
2. *Handbook of Deontic Logic and Normative Systems*, Volume 2 — `https://collegepublications.co.uk/handbooks/?00005=`; July 2021; ISBN `978-1-84890-363-0`.
3. *Handbook of Formal Argumentation*, Volume 1 — `https://collegepublications.co.uk/handbooks/?00003=`; 28 February 2018; ISBN `978-1-84890-275-6`.
4. *Handbook of Formal Argumentation*, Volume 2 — `https://collegepublications.co.uk/handbooks/?00006=`; August 2021; ISBN `978-1-84890-336-4`.

The same official catalogue's *Handbook of Epistemic Logic* presentation `?00002=` is already SRC-065 and was not duplicated.

#### W3C standards

The following separate W3C Recommendation presentations are authoritative logical-language records and are not independent source IDs in the current baseline:

1. *OWL 2 Web Ontology Language Document Overview (Second Edition)* — `https://www.w3.org/TR/owl-overview/`.
2. *OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition)* — `https://www.w3.org/TR/owl2-syntax/`.
3. *OWL 2 Web Ontology Language Direct Semantics (Second Edition)* — `https://www.w3.org/TR/owl2-direct-semantics/`.
4. *OWL 2 Web Ontology Language Profiles (Second Edition)* — `https://www.w3.org/TR/owl2-profiles/`.

Each page identifies itself as a W3C Recommendation dated 11 December 2012 and names separate current/versioned locators. These must be adjudicated as separate presentations; the sweep does not collapse the document set into one packet or infer that the four checked documents exhaust the OWL 2 Recommendation family.

## Provenance-control check

### ACQ-CONTROL-001

**Still active.** SRC-051 continues to distinguish IOS Press/SAGE publisher or distributor identity metadata from DBLP and other institutional contents records. SRC-057 continues to distinguish the Springer publisher identity from DBLP and institutional contents records. Nothing retrieved in this sweep justifies merging those provenances.

### ACQ-CONTROL-002

**Still active.** SRC-065 continues to distinguish the University of Groningen work record from the Cornell-hosted introductory chapter and its chapter-title overview. The official College Publications catalogue check did not supply a basis to collapse them.

## Exact query log

### Local inventory and gap queries

```text
rg -n "^### SRC-" spec/research/full-compendium-coverage-baseline.md
rg -n "^### SRC-.*(Deontic|Formal Argumentation|Tableau|Description Logic|Defeasible)" spec/research/full-compendium-coverage-baseline.md
rg -n "Handbook of Tableau Methods|The Description Logic Handbook|Handbook of Defeasible Reasoning and Uncertainty Management Systems|OWL 2 Web Ontology Language" spec data handbook
rg -n "2.7|2026-03-27|4.34.0-rc1|4.33.0|V9.2.0|Isabelle2025-2|Agda 2.8.0|Agda 2.9.0" spec/research/acquisition-src-042.md spec/research/acquisition-src-052.md spec/research/acquisition-src-053.md spec/research/acquisition-src-054.md spec/research/acquisition-src-055.md
```

The exact-title search found several titles inside acquired sources' reference material. The source-heading query found no independent source IDs for the new candidates. That distinction is why the titles are reported as acquisition candidates rather than treated as already acquired.

### Official-domain web searches

```text
site:link.springer.com/book "Handbook of Tableau Methods"
site:cambridge.org/core/books "Description Logic Handbook"
site:link.springer.com "Handbook of Defeasible Reasoning and Uncertainty Management Systems"
site:collegepublications.co.uk handbook paraconsistency deontic logic
site:link.springer.com/book/10.1007 "Handbook of Defeasible Reasoning and Uncertainty Management Systems" "volume 1"
site:link.springer.com/book/10.1007 "Handbook of Defeasible Reasoning and Uncertainty Management Systems" "volume 2"
site:link.springer.com/book/10.1007 "Handbook of Defeasible Reasoning and Uncertainty Management Systems" "volume 3"
site:link.springer.com/book/10.1007 "Handbook of Defeasible Reasoning and Uncertainty Management Systems" "volume 4"
site:link.springer.com/book/10.1007 "Handbook of Defeasible Reasoning and Uncertainty Management Systems" "volume 6"
site:collegepublications.co.uk/handbooks "Handbook of Deontic Logic"
site:collegepublications.co.uk/handbooks "Handbook of Paraconsistency"
site:collegepublications.co.uk "Handbook of Formal Argumentation"
site:w3.org/TR logic recommendation OWL 2
```

Only the official pages opened from those searches are used as positive evidence in this report.

### Direct bibliographic and maintained-source queries

```text
https://api.crossref.org/works?query.title=Handbook%20of%20Logic%20in%20Computer%20Science%20Volume%206&rows=20
https://openlibrary.org/search.json?title=Handbook%20of%20Logic%20in%20Computer%20Science%20Volume%206&limit=20
https://lccn.loc.gov/88025140/marcxml
https://openlibrary.org/api/books?bibkeys=ISBN%3A044470261X&jscmd=data&format=json
https://openlibrary.org/api/books?bibkeys=ISBN%3A0444871527&jscmd=data&format=json
https://openlibrary.org/api/books?bibkeys=ISBN%3A0444871535&jscmd=data&format=json
https://openlibrary.org/api/books?bibkeys=ISBN%3A0444872914&jscmd=data&format=json
https://dblp.uni-trier.de/db/series/hhl/hhl1.xml
...
https://dblp.uni-trier.de/db/series/hhl/hhl11.xml
https://smt-lib.org/language.shtml
https://lean-lang.org/doc/reference/latest/
https://lean-lang.org/doc/reference/stable/
https://rocq-prover.org/doc/V9.2.0/refman/
https://isabelle.in.tum.de/documentation.html
https://agda.readthedocs.io/en/stable/
https://agda.readthedocs.io/en/latest/
```

The ellipsis in the displayed DBLP route list denotes the mechanically enumerated integer routes `hhl2.xml` through `hhl10.xml`; it is not a claim that any response text was elided from this report.

## Disagreements and adjudication queue

1. Oxford's “six volumes” description conflicts with the five established HLICS volume records; Volume 6 remains unidentified.
2. The official Elsevier Boolean-algebra presentation acquired locally is Volume 2, while the Library of Congress and Open Library establish a three-volume set and distinct Volume 1 and Volume 3 records.
3. SRC-063 names DBLP routes for all history volumes, but 135 chapter records for Volumes 1–10 remain outside the transcribed source-ID coverage.
4. SRC-064 is only Volume 2 of a seven-volume Springer series; official records for Volumes 1 and 3–7 require separate acquisition decisions.
5. Multiple official handbook and standards presentations are bibliographically mentioned but not independently acquired as source records. Bibliographic mention cannot self-admit a presentation.
6. The four pre-existing metadata-conflict groups remain unreconciled.
7. The maintained documentation pages show no version delta today, but their future-snapshot obligation remains live.

## Required consequence

This sweep is a failing acquisition-completion checkpoint in the precise sense required by the completion plan: it found new authoritative presentations and unresolved known gaps. The next production action is not to mark acquisition complete. It is to:

1. adjudicate each presentation above for exact work/edition/version identity and applicability;
2. acquire and independently admit the applicable presentation records and contents without merging variants;
3. resolve or preserve each metadata disagreement through the governed gap-resolution process;
4. regenerate the affected external manifest and assignment surfaces from admitted records; and
5. run a new independent acquisition sweep after those changes.

At least two consecutive later independent sweeps must find no new authoritative presentation and no unresolved known gap. This sweep cannot count toward that pair.
