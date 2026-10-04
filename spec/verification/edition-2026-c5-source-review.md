# C5 independent source-fidelity review

Date: 7 September 2026. Reviewer: independent source-review context.
The report was filed blind, before reading another C5 review or receiving
another reviewer's findings. The author notes were locator leads only.

## Verdicts and scope

| Unit | Verdict | Scope of the verdict |
| --- | --- | --- |
| S-011: ACF attribution | PASS | The active result at restoration lines 177-218 accurately applies and attributes Steinitz's field classification, algebraic-closure results and cardinal calculation, with the characteristic, uncountability, existence and Choice qualifications retained. |
| D-P2-007: Tseitin construction | PASS | The complete 188-line body and 167-line annex preserve the bounded Harrison attribution and clearly supply an authored occurrence construction and proofs. The source is not credited with the new occurrence conventions or encoding analysis. |

No source-fidelity correction is required in this frozen scope. These are
source-review verdicts. They do not grant mathematical-specialist acceptance,
publication-text acceptance, manuscript build or visual acceptance, provenance
migration, canonical admission or whole-book release.

The governing amendment and C5 integration note were read completely. The
assignment permits cited field-classification dependencies for S-011. It does
not require a local reconstruction of every proof in Steinitz's paper.

## Frozen text and actual reading

Repository root: `C:/Dev/the-methods-of-reason`.

| Artifact | Actual read interval | Verified SHA256 |
| --- | --- | --- |
| `handbook/parts/p02/tseitin-transformation.tex` | 1-188, complete | `9E09805F966C64DF13CFDC0471C40AE0E0DCC9B2DC187B68E915E5E5A334E0D5` |
| `handbook/annex/p02/tseitin-transformation.tex` | 1-167, complete; the initially truncated tail was separately reread at 111-167 | `975195E565E2AE77F128EDA22568BF728555380F03E360006D4A5D67C4D19561` |
| `handbook/restoration/inherited-07295-07468.tex` | 1-250, complete, with the adjudicated ACF scope at 177-218 and categoricity definition at 4-8 | `A133AD43A7AF91BEC6DC90B1AC5335F0524C1447869CB382B05175138A9C0505` |
| `handbook/restoration/inherited-01661-01816.tex` | 1-57: alphabet, primitive grammar, association and defined connectives | `FB12D36A183AC0FDF5C8B2F8A1BBC09238526FDB03F75364A6DC18239913EC3E` |
| `handbook/restoration/inherited-01817-01898.tex` | 1-40: valuations, recursive truth clauses and coincidence | `499FEC700936D0625769D7C09AA2BC5FD1F6D976B9EAB1A9CBC8EDFE8CAFB9C4` |
| `handbook/restoration/inherited-01946-02186.tex` | 1-96: clauses, formula interpretation, CNF and satisfaction lemma | `185C35156F2E1983B1BEF028888C3FF2A0DFFF333366CFF1A3D2769225E37468` |
| `handbook/parts/p02/propositional-substitution.tex` | 66-104: occurrence positions and subformula notation, with following context | `5B39B8DC52B60442850707C6D4DF2C7E853929FC52541F85D839986BFD8DC146` |
| `handbook/restoration/inherited-14351-14400.tex` | 1-50, complete: existing Part 12 equisatisfiability/root and conjunction example | `A7A70819ADFAD23F3B5F16285E253E63D9F6FA0914AE58F1D80E8F0F2BFCF355` |
| `handbook/restoration/inherited-07150-07294.tex` | 131-145: preceding ACF theory and ring-language identification | `CCB19227218A479328D04079082C149BBD9ACF4B587C45D13FFF49A07548EFF8` |
| `handbook/bib/handbook.bib` | Steinitz1910 record at 4000-4011 and Harrison2003PropositionalSlides record at 5354-5361 | `84FF6BDD200A86DB3D82B84B0405376C98F395C7E504DA6CC38F52EFF340B7CC` |

The first 14 lines of `handbook/parts/p03/qe-categoricity-games-supplement.tex`
were also read for its attribution and fixed-characteristic context. The two
C5 author notes and `spec/research/edition-2026-c5-integration.md` were read
completely; none was treated as independent source-body evidence.

All three adjudicated whole-file hashes were checked again at 16:49 UTC and
still matched the freeze. The retained DLO interval at lines 108-176 was
recomputed as UTF-8 with LF line endings and has SHA256
`9AC556285A7ABB3F42E7652606A28BE92EE3C50102F5F045FB9805A20617A213`,
matching the protected interval in the integration note. Reading that context
does not reopen or replace its separate mathematical review.

## D-P2-007: Harrison source and manuscript comparison

The source is John Harrison, *Formal Verification Methods 1: Propositional
Logic*, Marktoberdorf lecture dated 30 July 2003. The complete local PDF is
`source/references/harrison-2003-propositional/slides1.pdf`, 71,285 bytes,
19 physical pages, SHA256
`2CC74465CEBB0B33738EF4C7BE080DF9E5CFAA3C202DBBAC4FB95D7A1B76E011`.
An independent live retrieval from the
[author-hosted PDF](https://www.cl.cam.ac.uk/~jrh13/slides/marktoberdorf-30jul03/slides1.pdf)
returned HTTP 200 and the same byte count and hash.

Actual source reading: complete physical pages 1, 12, 13 and 14, carrying
printed slide numbers 0, 11, 12 and 13. The local title page and physical page
13 were additionally rendered and visually inspected. Their headings, date,
formulas and printed slide numbers were legible. This was source-PDF
inspection; no manuscript was rendered.

The title page explicitly gives 30 July 2003. PDF metadata reports a file
creation date of 1 July 2007. The bibliography correctly identifies the
lecture date; the inspected artifact is the subsequently generated author
PDF, not evidence that these exact PDF bytes existed in 2003.

Printed slide 12 shows three biconditional definitions for a compound input,
their conjunction/disjunction CNF blocks and a final asserted representative
`p_3`. It explicitly distinguishes satisfiability preservation from logical
equivalence. Slide 13 supplies the clause-set interpretation. Thus body
lines 7-9 have the correct source and printed locator. The displayed source
root appears both before and after its CNF conversion.

The manuscript's construction is independently specified at body lines 28-92.
It labels every nonvariable occurrence, including bottom and negation, reuses
original variable leaves and treats repeated nonvariable occurrences
separately. Harrison's example selects larger subformulas and leaves the
negated atom inside a gate input. The text never calls the manuscript's
position policy Harrison's exact procedure. Its new example also differs
from Harrison's example. The Part 12 cross-reference correctly points to the
same conjunction-clause shape and an explicit root rule in the existing
manuscript.

The important source qualifications survive in the authored generalization:

- All primitive constructors of the active grammar have an explicit row,
  including bottom, negation and implication; each nontrivial row enforces
  both directions of its defining truth function.
- The root clause is retained even for an atomic input. The bottom example
  makes its necessity explicit.
- Body lines 94-123 quantify the original assignment on the finite input
  set `V` and the unique defining extension on `V` union the fresh variables.
  They do not promise uniqueness of arbitrary global valuations or reuse a
  total assignment while changing its already assigned auxiliaries.
- Equisatisfiability, the projection onto original satisfying assignments
  and enlarged-vocabulary entailment have distinct stated roles. The
  countervaluation at lines 182-187 preserves the source's nonequivalence
  qualification.
- The token-size and conditional emission claims at lines 125-147 are
  separated from the binary-encoding bound. They measure the expanded
  primitive occurrence tree and do not assert linear bit time.

Both local theorem statuses point to their actual annex proofs. The first
annex covers gate equivalences, extension existence, forced values,
uniqueness and the root/CNF conclusion at lines 1-108. The second supplies
the counting and encoding argument at lines 110-167. Those are authored
proofs, not a transcription of a complete proof in the slides. In particular,
the precise `3M+1`, `7M+1` and binary-index bounds are supported by the local
argument rather than falsely attributed to slide 12.

No original Tseitin 1968 paper, Prestwich chapter, full Harrison 2009 book or
Harrison source-code file was independently read in this assignment. Their
mention in author leads or adjacent historical material supplies no additional
review evidence. The bounded attribution in the new body requires none of
those sources to stand in for its actually consulted Harrison passage.

## S-011: Steinitz source and manuscript comparison

The historical source is Ernst Steinitz, *Algebraische Theorie der Körper*,
*Journal für die reine und angewandte Mathematik* 137 (1910), 167-309,
DOI `10.1515/crll.1910.137.167`. The
[publisher record](https://www.degruyterbrill.com/document/doi/10.1515/crll.1910.137.167/html)
and DOI content-negotiated metadata confirm author, title, print year and
article extent. The publisher's modern metadata uses volume 1910 / issue
137 and an online date in 2009. The historical page-167 footer instead reads
volume 137; the existing bibliography preserves the printed volume and 1910
date correctly.

The primary body actually read was the GDZ journal digitization's complete
HTML OCR responses for the seven pages below. Page 167 was read for identity;
the other six pages supply the required statements and immediate context.
These are preserved local source-page captures, not a claim to have acquired
or read all 143 pages of the article.

| Printed page / GDZ scan | Exact primary endpoint | Source passage and comparison |
| --- | --- | --- |
| 167 / 171 | [page 167](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000171?_format=xml) | Title, author and printed journal volume identify the historical article. |
| 287 / 291 | [page 287](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000291?_format=xml) | Section 21(9) states algebraic-closure existence and essential uniqueness; its following explanation explicitly extends a given base-field isomorphism. This supports lines 199-202 and the cited dependency at 215-218. |
| 288 / 292 | [page 288](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000292?_format=xml) | Section 22 begins with algebraic dependence and finite character. It confirms the next section boundary and the meaning behind the modern basis terminology. |
| 289 / 293 | [page 289](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000293?_format=xml) | The paragraph preceding Section 22(5) constructs purely transcendental extensions on arbitrary sets of indeterminates. It explicitly extends a prescribed bijection of independent systems to an isomorphism fixing the base. Item 5 states equivalence of extensions with equal-sized independent systems. This supports lines 199-207. |
| 299 / 303 | [page 299](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000303?_format=xml) | Section 23(3) gives equality of cardinality for equivalent independent systems; the following paragraph defines transcendence degree and assigns degree zero to algebraic extensions. This supports the invariant used at lines 188-196. |
| 300 / 304 | [page 300](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000304?_format=xml) | The absolute degree is relative to the prime field. Characteristic ranges over zero and primes; degree ranges over zero, finite degrees and arbitrary transfinite cardinals. The paragraph constructs a rational-function type and an algebraically closed algebraic extension in every class. This supports both invariants and model existence. |
| 301 / 305 | [page 301](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000305?_format=xml) | Section 23(6) identifies the unique algebraically closed type in each class. Section 24 invokes well-ordering, gives the cardinal calculation for algebraic extensions and explicitly equates an uncountable field's cardinality with its absolute transcendence degree. This supports lines 177-183 and 192-218. |

The active theorem's existence and uniqueness formulation matches its local
categoricity definition at lines 4-8. The hypothesis fixes `p=0` or a prime,
quantifies every uncountable cardinal and expressly assumes ambient Choice.
Steinitz's classification is by characteristic and transcendence degree, not
cardinality alone; the manuscript uses the cardinal calculation to obtain
the latter implication precisely in the uncountable case.

The countable exception is accurately explained. The text contrasts degree
zero and degree one closures and accounts for their countability by the
polynomial/root argument; different degrees cannot become isomorphic. The
same argument handles finite and countably infinite bases. This is an
authored explanation of the model-theoretic consequence of the cited field
results. It is not presented as Steinitz's literal use of the modern phrase
`ACF_p is kappa-categorical`.

The result is explicitly `cited=Steinitz1910`. Lines 215-218 identify the
classification, existence and closure theorems as cited dependencies whose
full proofs are not reproduced. That is a truthful boundary for this
attribution assignment. It does not require or pretend to supply an annex
proof of all of Sections 21-24.

## Local Steinitz capture identity and access limits

All seven endpoints returned HTTP 200 and `text/html; charset=UTF-8` despite
their `_format=xml` query. Each stored `.html` file preserves the received
UTF-8 body with exactly one final LF added by the file-creation tool. Removing
that final byte reproduces the independently computed response SHA256 below.
This distinction was verified for every file; the local hashes are not
misreported as hashes of the unmodified HTTP payload.

Capture directory: `source/references/steinitz-1910/`. File pattern:
`c5-20260907-page-PRINTED-scan-SCAN.html`.

| PRINTED / SCAN | Local SHA256 | Response SHA256, before the added final LF |
| --- | --- | --- |
| 167 / 00000171 | `304ECB85D9F27AE6C4651DA484B1C04B6E6859059A88F6099ED2D1C114509E87` | `8F2A39690EFD97E3EF2E5E656C70D7AE25663BCC7A0C4D5D48E52A42013D2594` |
| 287 / 00000291 | `854278D777A6B89A97C33E2C5235338D2B7AE41598C495515B8A492ADAD563AD` | `216C94CDF4F9329D8B1B646718915EE27CAA75F81F5934A267587C193CE4AA3E` |
| 288 / 00000292 | `50ADD19AE59BD460FF2863EB8F3B809B544BAB8911FC9C3C76913F4ACCB99512` | `76C0D97EA555F3C9304727A13B3497B8BEF230CA5A7B4FB384A100362A4D1D40` |
| 289 / 00000293 | `B975A7CB4AA26691F38620D533DD494E188BE7A6C8EDDB7E98A0D011324C06CD` | `CB4692BD15CC8FDCED5F2449F446D60BE0D33C3096B4A593678EFB719E953A0B` |
| 299 / 00000303 | `E1E9F60D6A1D4FACDE8EB7A0C096F5AF192B57C6310BC8C6219EDF0CCA301D34` | `16CE2896A4F23E7D7F6EF6A0527DB53542027CAD50713ABBC8DB452989AA83F8` |
| 300 / 00000304 | `CC277BA261BAED4D9FE1EBC1B7EE0C8FAF7CFC31D573AB22D4BF9B9E7039F8DF` | `5EF2F56914297928FDE194B43C3413C33555B13D91A62748F3713744E9E2FB46` |
| 301 / 00000305 | `9D61D4221E373F27523AF061CF9B8B87316A819999E1752E362837537083C724` | `413C3081951AE73BCFE31A334DA4D2E84AB4F470A879F0C60725A24760C2383A` |

The OCR has visible corruption in German words, mathematical type labels and
some printed page numerals: scan 291's numeral is damaged, and scan 293 reads
280. The printed-page mapping uses the scan sequence, neighboring readable
page numerals and the section/result context. No pristine scan-image
transcription is claimed. The required prose assertions, their quantifiers
and their relation to the manuscript are readable in the captured passages;
the assessment does not depend on accepting a garbled type symbol as exact.
For example, the uncountable-cardinality assertion is explicit prose in
Section 24 as well as part of its preceding calculation.

No Steinitz page image or complete PDF was successfully acquired or inspected.
The old resolver did not provide a readable body through the web tool, and
the direct GDZ volume-page route returned 404; these are recorded access
limits. The seven functioning primary OCR endpoints and their saved bodies
supply the extent needed for this bounded source review. A future full-paper
or historical proof-reconstruction task must obtain and inspect its own
additional required extent.

Only this report and the seven new Steinitz captures were added to the
repository by this reviewer. Temporary Harrison source-page renders were
placed outside the repository. No manuscript, code, shared registry,
bibliography or provenance record was edited; no tests, manuscript builds or
manuscript renders were run. The research and PDF skills guided primary
source capture and source-PDF inspection. No further agent was delegated.
