# Imprecise probability: mathematical draft and exact-source gap

Authoring checkpoint: 1 October 2026. Unit:
`ED26-METHOD-imprecise-probability`, the complete row in
`spec/coverage/edition-2026/additional-method-units.jsonl`.

**Status:** the general mathematical component draft is written, with twelve
complete reciprocal proofs. The exact selected Walley 2014 article body is
still unacquired. This package does not discharge the complete selected
source presentation, and the acquired dependencies are not substitutes for
that body. Source matching, root integration and independent admission remain
open. Do not assign full-source completion credit from these twelve pairs.

## Required Walley source and verified acquisition boundaries

Peter Walley, *Imprecise Probabilities*, Wiley StatsRef: Statistics Reference
Online, DOI `10.1002/9781118445112.stat01581`, first published
29 September 2014. The [publisher landing page](https://onlinelibrary.wiley.com/doi/10.1002/9781118445112.stat01581)
explicitly identifies republication of an article originally published online
in the 2006 *Encyclopedia of Statistical Sciences*. That origin is a separate
version identity; no equivalence of an unread 2006 and 2014 body was inferred.

The readable landing page exposes identity, references and the origin note.
It does not expose the full selected article body. The author tried the
publisher full-HTML, PDF, ePDF, PDF-direct and full-XML routes. Standard
verified urllib HTTPS returned HTTP 403 for full HTML, PDF and full XML;
the web tool could not retrieve ePDF/PDF-direct or its read-full-text link.
Crossref's exact DOI record confirms 2014-09-29 and lists the same PDF and
full-XML version-of-record endpoints. No publisher permission or purchase
was requested. Bounded filename searches found no exact Walley or relevant
Encyclopedia body in the manuscript captures or the local Calibre library.

The source acquisition helper used disjoint new routes and returned these
observed outcomes, without editing this note or replaying those publisher
body routes:

- [OpenAlex exact DOI lookup](https://api.openalex.org/works/https://doi.org/10.1002/9781118445112.stat01581):
  HTTP 200, 8,451 bytes, work `W4251521769`, publication date 2014-09-29.
  Its record supplies only the publisher DOI location and reports closed
  access, no OA URL, no repository full text, no best OA location and no
  PDF URL. These are index observations, not a proof that no free body exists.
- Semantic Scholar exact DOI lookup: HTTP 404.
- Internet Archive exact `9781118445112.stat01581` search: HTTP 200,
  308 bytes, zero catalog results. Exact title plus Walley search:
  HTTP 200, 2,422 bytes, one result, the distinct 1991 book
  `statisticalreaso0000wall` with xii + 706 pages.
- The linked [SIPTA documentation](https://sipta.org/info/documentation/)
  and [archive](https://sipta.org/info/archive/) expose books, tutorials and
  seven legacy topic documents, with no identified 2014 article link.
  The historically linked `ippserv.rug.ac.be` resource was not retrievable.
- Exact DOI/title searches scoped to UGent, IDSIA, Granada, PhilArchive and
  CORE returned related works or citations, with no qualified StatsRef body.

Older Walley 1999 Update Volume 3, Walley 2000's unified-theory article and
Walley 1991's monograph remain distinct sources. None was used to assert
that the missing 2014 source had been read. A further acquisition attempt
should begin with a concrete new public deposit or exact cataloged body.

## Acquired bounded proof dependencies

1. Enrique Miranda, *A survey of the theory of coherent lower previsions*,
   undated 44-page author manuscript distributed by SIPTA School 2008/LIRMM.
   Local file:
   `source/references/p15-imprecise-probability/miranda-survey-lirmm.pdf`.
   [Public source](https://www.lirmm.fr/SiptaSchool08/biblio/surveyMiranda.pdf).
   256,628 bytes, SHA-256
   `B8C24C2E43DFEFEC943E5A072B8D61A1DBCF8E4794ADAA53C68864C8144C879E`.
   PDF production is 6 December 2007; this is not asserted to be the final
   2008 version of record. The exact selected passages were read: §§2.1-2.4,
   printed pp4-16, on prices, coherence, representation and natural
   extension; §§3.1-3.3, pp17-24, on conditional prices, positive lower
   probability, zero boundaries and the infinite-partition limitation;
   §§4.1-4.4, pp25-30, on the distinct independence notions; §5.2,
   pp31-32, on Williams' different conditional criterion. Source pp1-3,
   the almost-desirability passages and the beginnings of the adjoining
   comparison sections were also read for context. Unread later material
   is not claimed inspected.
2. Jasper De Bock and Gert de Cooman, *Conditioning, Updating and Lower
   Probability Zero*, the author preprint submitted to Elsevier on
   18 August 2015, as stated on its first page. Local file:
   `source/references/p15-imprecise-probability/de-bock-de-cooman-2015-conditioning.pdf`.
   [Author-hosted source](https://users.ugent.be/~jdbock/documents/JDB-2015-IJAR-2-paper.pdf).
   42 pages, 411,032 bytes, SHA-256
   `AFBE53104D435DBE926F6EE82C29372C7F597F13DB8E1E265BE6D1ACF29C55CC`.
   Source pp1-5 were read. The selected dependency is the introductory
   three-case conditioning description and finite Example 1 on p2.
   The preprint itself explicitly restricts its developments to finite
   spaces. The general algebra proofs in this draft are not attributed
   to that finite source. The distinct 36-page journal version,
   DOI `10.1016/j.ijar.2015.08.006`, is identified separately by its
   publisher/repository record and was not substituted for this capture.

The research and PDF skills supported acquisition and reading. The first
local directory creation attempt failed; granting the already authorized
manuscript path and creating the exact owned directories resolved it.
The bundled pdftotext path was absent, so pypdf was used for source text.
No certificate verification was disabled. No manuscript PDF was rendered.

## Written components and proof scope

Body: `handbook/parts/p15/imprecise-probability.tex`.
Annex: `handbook/annex/p15/imprecise-probability.tex`.
The draft has twelve reciprocal pairs and twelve full proofs:

- Integer versus real stakes, including arbitrary finite non-linear domains.
- Natural extension, least coherent domination, exact extension criterion,
  and the all-gambles infinite result when the input incurs sure loss.
- The full vector-domain coherence characterization, including uniform
  domain identifications and the cash/monotonicity/continuity deductions.
- Compatible-model existence and exact attained lower representation on
  arbitrary domains, using the existing proved Hahn-Banach, charge
  integration, compactness and finite-coordinate separation premises.
- Conjugate upper previsions, event conjugacy and transitive extension.
- The extra upper-continuity criterion for all compatible models to be
  countably additive, plus the ultrafilter and vacuous-lower counterexamples.
- Two three-state coherent envelopes with identical bounds on every event
  and different gamble prices and decision comparisons.
- A finite normalized-possibility bridge via nested subset masses, using
  the P14 definitions and allocated-envelope result rather than duplicating
  the finite comparison table.
- One-event natural/regular conditioning with every zero-probability branch,
  supported precise models and the full joint portfolio argument.
- The generalized-Bayes unique root at positive lower probability and its
  complete half-line root set at zero lower but positive upper probability.
- Two explicit buying/selling portfolios which force the generalized-Bayes
  identity, establishing the extremal coherent conditional bounds.
- A binary strong-product example whose natural and regular conditionals
  differ at the zero-lower-probability observation.

The general domain is the uniform closure of simple gambles on an arbitrary
event algebra. The power-set case is all bounded gambles; the sigma-algebra
case is all bounded measurable gambles. Basic representation uses finite
additivity. Countable additivity is never inferred from coherence alone.
The exact conditional results concern one nonempty observation event.
They do not silently assert an envelope or extension theorem for arbitrary
infinite partitions; the actual distinction from Walley's conglomerability
requirements is stated in the body.

The C01-C05 mathematical questions all have substantive draft treatments,
but matching their complete identified Walley source extent remains open.
The missing body could contain additional definitions, examples,
qualifications or applications, which must be supplied after reading it.
The source article's unknown remaining extent is not a scope waiver.

P14 references were checked against the returned actual files and confirmed
by their author: `def:p14-evidence-uncertainty-data`,
`thm:p14-evidence-finite-measures` and
`thm:p14-evidence-measure-separation`. Their finite comparison and allocation
proofs remain in P14. P17 analytic premises and utility/decision distinctions
retain their actual labels and hypotheses.

## Integration and local checks

Unique intakes:
`handbook/bib/intake-p15-imprecise-probability.bib` (two exact dependency
identities; no unread Walley body citation) and
`handbook/registry/symbols-intake-p15-imprecise-probability.csv` (22 rows).

Suggested exact scope bindings for root:

```json
{
  "P15 imprecise-probability lower-prevision treatment": {
    "presentation": "General bounded-gamble coherence and one-event conditioning draft with separately identified proof dependencies",
    "regions": [
      {"anchor": "sec:p15-imprecise-probability"},
      {"file": "annex/p15/imprecise-probability.tex"}
    ]
  },
  "P15 imprecise-probability event-information example": {
    "presentation": "The full and reduced permutation hulls C and D",
    "regions": [
      {"anchor": "thm:p15-ip-event-separation"},
      {"anchor": "annex:p15.ip.event-separation"}
    ]
  },
  "P15 imprecise-probability finite possibility bridge": {
    "presentation": "Ordered possibility scores and their nested focal masses",
    "regions": [
      {"anchor": "thm:p15-ip-possibility-bridge"},
      {"anchor": "annex:p15.ip.possibility-bridge"}
    ]
  },
  "P15 imprecise-probability Bayes-root proof": {
    "presentation": "Root functional F in the generalized-Bayes proof",
    "regions": [{"anchor": "annex:p15.ip.generalized-bayes"}]
  },
  "P15 imprecise-probability independence example": {
    "presentation": "The declared binary coordinates X and Y",
    "regions": [
      {"anchor": "thm:p15-ip-independence-boundary"},
      {"anchor": "annex:p15.ip.independence-boundary"}
    ]
  }
}
```

The writer read the actual resulting body and annex. The bounded structural
check found twelve exact reciprocal body/annex pairs, no mismatches, and all
22 first-use labels in the owned text. New mathematical examples were
calculated explicitly in their proofs. This does not establish independent
mathematical acceptance. No review wave, manuscript build/render or software
test suite was run. Shared drivers, canonical registries and generated files
were not changed by this writer.

Snapshot hashes:

| Artifact | Lines/bytes | SHA-256 |
| --- | --- | --- |
| Body | 389 lines / 19,359 bytes | `500A7A307EE391CC375BDBFA2772E4902793DA8BCCA3069AF9E013B672946C41` |
| Annex | 433 lines / 22,129 bytes | `07FC686A690A5C41F3FD38787CC3DC5F402A7BB94401A449E1577D4579423F4A` |
| Symbols | 22 rows / 5,465 bytes | `6CBA42F7320C1EC8FBF32FD086FA32704473EE71D3C373BCFCBB59A4C795B159` |
| Bibliography | 2 entries / 1,046 bytes | `5BCFFCED81616225E66187B1D8AB05A4E52419F771CEC06A3D8103BDCA24EB56` |

Next substantive dependency: acquire and read the complete exact Walley2014
StatsRef body, match all its content against this draft, and author anything
the complete source adds. That source gap remains after this block's
mathematical authoring progress.
