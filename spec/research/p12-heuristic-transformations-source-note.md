# Heuristic transformations and working backwards: authoring record

Date: 9 September 2026. Assigned unit: ED26-P12-PRACT-001, all five selected
components. The exact unit row and authoring-resumption contract were read,
alongside the current P12 conventions and the actual P19 analogy/transfer
chapter. The latter remains an empirical counterpart, not a substitute for
Pólya's selected method presentation.

## Acquired source and edition identity

The freely downloadable [source PDF](https://dmitry.ai/uploads/default/original/1X/b28682972c04ef65cac434a6cb3715ec9945ae1a.pdf)
is held at
`source/references/polya-2004-how-to-solve-it/polya-2004-dmitry.pdf`.
It is 1,964,699 bytes with SHA-256
`7CF9042FDB71FAACAD333B8C8CBAA26ADA0C30A8F008D3C3B759C892791A6888`.

The actual title page gives G. Polya, *How to Solve It: A New Aspect of
Mathematical Method*, with John H. Conway's foreword. Its copyright page
explicitly identifies the expanded Princeton Science Library edition, 2004,
ISBN 978-0-691-11966-3, and retains the 1957 second-edition copyright and
the earlier printing history. This is the selected 2004 text manifestation;
an unverified 1945 or 1957 copy has not been substituted for it.

The file is a reflowed 148-physical-page PDF. Its container identifies pdftk
2.02/itext and a 2016 conversion timestamp. It is not the original printed
pagination and is not asserted byte-identical to a publisher PDF. The complete
named source sections and entries were read in this actual artifact, including
their mathematical examples and relevant footnotes. The book's original
entry/page identities are preserved by name; source citations in the new
chapter use section and entry titles, not invented physical-to-print offsets.
The [publisher contents](https://assets.press.princeton.edu/chapters/c669.pdf)
were already the edition-map source for the selected entry identities.

A university Moodle URL at lms.umb.sk was indexed with the same 2004 edition
copyright text. Direct web opening timed out; local curl failed in its
Schannel credential initialization; a normal certificate-valid Python request
then returned HTTP 403. No body is credited from that route and no access
restriction or certificate check was bypassed. The successful source above
required no account, payment or authentication.

The DOI 10.1515/9781400828678 is deliberately not assigned to the 2004
bibliography intake. The [Crossref resolution record](https://chooser.crossref.org/?doi=10.1515%2F9781400828678)
labels it with a 1945 publication date, while a [publisher chapter citation](https://www.degruyterbrill.com/document/doi/10.1515/9781400828678-003/html)
describes its parent book as 2014, with a 2019 copyright display. Those
coexisting manifestation dates do not override the held copy's explicit
2004 edition and ISBN. The intake uses that exact edition/ISBN and the
publisher contents URL without manufacturing a DOI-equivalence assertion.

## Complete selected reading extent

`source/references/polya-2004-how-to-solve-it/source-receipt.json` pins the
source and layout hashes, exact extraction-line ranges, physical-page ranges
and text hashes for the following complete selections. A final physical page
can also contain the next heading; selection stops at that heading.

| Selected source text | Physical pages in the held reflowed PDF |
| --- | --- |
| Part I, sections 6–14 | 23–29 |
| Decomposing and recombining | 59–64 |
| Generalization | 74–75 |
| Heuristic reasoning | 76–77 |
| Problems to find, problems to prove | 96–98 |
| Specialization | 114–118 |
| What is the unknown? | 126 |
| Working backwards | 131–135 |

Additional bounded source reading covered the associated Part III footnotes
2, 6 and 9; Auxiliary Problem sections 6–8 on equivalent/unilateral reductions;
Pappus's analysis/synthesis discussion and the author's convertibility proviso;
Analogy sections 8–10; and the immediate cube-sum induction discussion.
The selected source's r+R inequality and radius formulas were read from the
actual physical page 114 image because some formulas are image objects absent
from text extraction. The one-quart pail diagrams were checked on physical
page 133. These are source-reading operations, not manuscript output checks.

## Authored coverage

Body:
`handbook/parts/p12/heuristic-transformations-and-backward-reasoning.tex`.
Annex:
`handbook/annex/p12/heuristic-transformations-and-backward-reasoning.tex`.
Bibliography intake:
`handbook/bib/intake-p12-heuristic-transformations.bib`.
Symbol intake:
`handbook/registry/symbols-intake-p12-heuristic-transformations.csv`.

| Component | Written treatment |
| --- | --- |
| C01: specify the task | Unknown/domain/data/condition records; one versus all solutions; proof assumptions and targets; side versus altitude specifications; source word, chess and evidential-task distinctions. |
| C02: decompose/recombine | Necessary/sufficient/equivalent condition relations; intersections and compatible local solutions; auxiliary reconstruction maps; circle center/radius; equivalent triangle descriptions; complete two-locus triangle calculation; word-puzzle interpretation and verification. |
| C03: work backwards | Fixed-context sufficient implication chains and the converse-direction counterexample; exact square-root candidate filtering; predecessor relation/path proof; every legal action in the source's nine/four-quart pail construction. |
| C04: generalize/specialize/analogize | Restriction and refutation versus universal proof; finite-sample polynomial separator; cube-sum induction; centrally symmetric volume bisection; parameterized frustum; genuine triangle counterexample and the source limiting family; relative-motion transfer with both time domains. |
| C05: check/limit | Forward verification, all-solutions coverage, permitted-operation checking, domain guards, box symmetry/scaling/limit checks, source cable application, failed division/squaring examples, and explicit limits on discovery/empirical claims. |

The body uses fourteen proved results with fourteen matching ordinary proofs
inside reciprocal annex items. The proofs supply the actual formal claims;
the source's heuristic recommendations remain methods with scope and reasons,
not invented general theorems about successful discovery.

## Source examples and direct qualifications

The full box/face-diagonal derivation, common center, four equal roof cables
and the exact 14.5-yard result are retained. The three-side versus three-altitude
distinction and the equal-sided quadrilateral proof make their actual geometric
conditions explicit. The new numerical altitude construction is an editorial
realization of the source's symbolic distinction.

The triangle with a given side, altitude and opposite angle is solved by the
intersection of the height line and the proper angle arc. The source's
half-plane footnote is preserved in substance. The derived quadratic also
states the zero/one/two-solution cases and permits an altitude foot outside
the base segment. Finding separate points on the two loci is not a solution.

The generalization examples retain the sum of cubes, octahedral bisection via
central symmetry, and the square-pyramid frustum. The central point lying on
the given line is handled directly: there are many suitable planes in that
case. The frustum calculation keeps the a-b division guard and handles the
equal-base prism separately. Its numerical volume is 350 cubic inches.

For specialization, the false proposed inequality r+R<=H is treated as a
conjecture to refute, not as an active theorem requiring a reader's correction.
Both source limiting directions are calculated using equal side lengths fixed
at one. A positive-area coordinate triangle gives an exact, finite counterexample.
For the ship problem, subtraction of a common time-dependent translation proves
the relative-motion reduction. Zero relative velocity and future time t>=0 are
separate cases; a past closest approach does not solve a future-only problem.

The pail sequence obeys the exact capacities and allowed fill/empty/pour-until-full
or-empty operations. Its backward predecessors are validated by their actual
forward moves. The fence-detour passage is retained as the source's qualified
illustration; no species ranking, experimental effect size or universal human
performance claim is inferred from it. The existing P19 analogy chapter remains
the explicit empirical cross-reference.

## Authoring checks and remaining work

The actual completed body and annex received an author read-through. A direct
structural extraction found fourteen body proved results, fourteen annex items,
fourteen ordinary annex proofs, zero ordinary body proofs and all reciprocal
targets matching. The square-root rejection, cable/frustum arithmetic, pail
states, geometric counterexample and relative-motion boundary were recomputed
as local mathematical checks. This is not an independent acceptance review.

All five assigned components are authored, with no selected source entry or
promised formal proof deliberately left unwritten. Root still owns driver
routing and the canonical bibliography/symbol merges. The source manifestation
and source-reading record remain explicit for the later consolidated source
review. No manuscript build, manuscript render, independent review or new
software test suite was run. Final integrated review and publication acceptance
remain separate from this authoring completion.
