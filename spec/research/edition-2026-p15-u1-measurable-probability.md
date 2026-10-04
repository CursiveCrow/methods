# P15-U1: measurable probability and random variables

Date: 7 September 2026 (America/Los_Angeles). Author:
`/root/probability_measure_author`. Continuation of P15-U1 for N-x-008.
Status: complete assigned measure/random-variable foundation authored and
read back, with ten complete proof items. Independent reviews, integration,
production checks and admission are separate remaining work.

## Written artifacts and dependencies

| Artifact | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p15/measurable-probability.tex` | 484 lines; new chapter, four sections | `C249F33E0E0FC88084B05A7D44098DB87B3E4814083B34709D6DBE2B562340D9` |
| `handbook/annex/p15/measurable-probability.tex` | 481 lines; ten full proof items | `FBB9E6C733A1F286F7E56FC31B7E76D4412D781E03711ED02D8D4B3AAEF8C8FC` |
| `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf` | Exact full author PDF, 490 pages | `AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886` |

The governing `spec/EDITION-2026-CONTRACT.md` was read completely, as were
the handbook conventions, finite probability body/annex, its source note,
and current P15 wrappers. The finite body and annex were unchanged and
their hashes were verified before and after writing:
`934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1`
and `7CE651CE52FE8BFA66E5BEC221BDF48EE6318538E6A99B8E987E18C90D6B67F3`.
These match `spec/verification/edition-2026-p15-scoped-production.md`.

The new chapter assumes elementary set theory, finite sums, real order
completeness and elementary Euclidean topology. It defines nonnegative
countable sums and proves the grouping result needed for its atomic model.
It does not assume any probability measure on an uncountable space exists.

## Exact source acquisition and reading

Source: Rick Durrett, *Probability: Theory and Examples*, **Version 5,
January 11, 2019**, as printed on the author PDF's title page.
Primary URL: [Duke Mathematics author PDF](https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf).
This capture is the author version, not the Cambridge printed manifestation;
no publisher, printed-edition pagination or ISBN has been substituted.

Before acquisition, bounded filename checks under `source/references` and
`tmp`, plus author/key checks in the canonical bibliography, found no
Durrett/PTE5 holding or entry. The exact target file was also checked for
existence before downloading. The download returned HTTP 200,
`application/pdf`, content length **2,195,717 bytes**, and
`Last-Modified: Thu, 28 Mar 2019 19:01:27 GMT`. The saved length matches.
The unencrypted PDF has 490 pages. Its PDF metadata records creation and
modification on 28 March 2019; this is distinct from the title's version
date. The title retains its copyright 2019, all rights reserved notice.
The source bytes were preserved; no source prose or figure was reproduced
in the new exposition.

Actual complete text extents read from the saved PDF with `pypdf`:

| Printed pages | Physical PDF pages | Actual reading |
| --- | --- | --- |
| 1-9 | 9-17 | Complete Section 1.1, including its extension-theorem boundary, examples and exercises. |
| 10-14 | 18-22 | Complete Section 1.2, including distribution functions, existence construction, densities, examples and exercises. |
| 15-18 | 23-26 | Complete Section 1.3 through Exercises 1.3.7-1.3.9 on p. 18; also the adjacent opening of Section 1.4 on that page. |
| 455-460 | 463-468 | Complete Appendix A.1, including the pi-lambda proof and the measure extension existence proof. Only its uniqueness component is used as a theorem dependency here. |

Physical page equals printed page plus eight in these body extents.
The title and complete printed pages 1, 2, 3, 10, 11, 12, 15, 16, 17 and
457 were also visually inspected by rendering the saved PDF in memory
with `pypdfium2`. This checked the actual mathematical glyphs and the
version notice. No page image files or manuscript PDFs were generated.
The rest of the 490-page book is not claimed read. The later integration
sections are identified as subsequent work, not completed source coverage.

The PDF skill guided primary text extraction and visual reading. The
research skill guided primary-source tracing and this single research
note; the assignment's explicit prohibition on subagents controlled its
delegation instruction. Scoped file/network permission was requested;
creating the exact new source directory required a scoped escalation.
The subsequent acquisition succeeded without paid access.

## Result-to-source map and independent development

All body IDs below have prefix `thm:p15-`; all annex IDs have prefix
`annex:p15.`. The suffixes match one-to-one.

| Result suffix | Exact source foundation | Supplied proof extent |
| --- | --- | --- |
| `generated-events` | Section 1.1, pp. 1 and 3 | Annex 12-35: closure, arbitrary intersections, generated sigma-algebra and uniqueness. |
| `measure-laws` | Theorem 1.1.1, p. 2 | Annex 37-90: finite/empty additivity, monotonicity, finite subtraction, countable subadditivity, both continuity directions, null unions and probability-one intersections. |
| `countable-atomic` | Example 1.1.2, p. 2; nonnegative regrouping used in Appendix A.1, pp. 455-456 | Annex 92-145: full supremum-based regrouping proof, including infinite values, atomic measure construction and unique countable probability representation. |
| `borel-generators` | Borel definition p. 3; Exercises 1.1.2-1.1.3 p. 9; Examples 1.3.2-1.3.3 p. 15 | Annex 147-184: rational rectangles, countable open-set unions and rational/real closed-ray generators. |
| `measurability-criterion` | Theorem 1.3.1 and equation (1.3.1), p. 15; Exercise 1.3.1 p. 17 | Annex 186-221: generator criterion, sigma(X), minimality and inverse images of generators. |
| `measurable-operations` | Theorems 1.3.4-1.3.6, pp. 15-16; Exercises 1.3.4 and 1.3.7, pp. 17-18 | Annex 223-274: composition, both directions for vectors, continuous maps, finite operations and both simple-function descriptions. |
| `measurable-limits` | Theorem 1.3.7 pp. 16-17; Exercise 1.3.7 pp. 17-18 | Annex 276-339: extended infimum/supremum and both tail limits; measurable real convergence event; explicit increasing nonnegative dyadic approximation, including the infinity case. |
| `pushforward-laws` | Section 1.2 opening and proof, p. 10; Theorem 1.3.4 p. 15 | Annex 341-372: probability law, measurable composition, atomic outcome formula and countable value-space representation. |
| `measure-uniqueness` | Theorem A.1.4 pp. 456-457; probability specialization of Theorem A.1.5 pp. 457-458 | Annex 374-429: full two-stage pi-lambda argument and equality of probability measures on the generated sigma-algebra. |
| `cdf-laws` | Theorem 1.2.1 p. 11; equality in distribution pp. 11-12; Exercise 1.2.3 p. 14 | Annex 431-481: endpoint limits, right/left limits, intervals, point masses, countably many jumps and equality of laws via the proved uniqueness theorem. |

This is an independently worded reconstruction, with explicit supporting
proofs where the source leaves an exercise or an immediate deduction.
The author's nonnegative sums are defined by finite-subset suprema, so
the atomic construction does not appeal to an unproved rearrangement rule.
The source's printed measure codomain on p. 1 is R, despite its later
infinite-measure examples; this chapter explicitly uses `[0,infinity]`.
The extended codomain is also declared before taking suprema/infima of
variables. The source's p. 16 displayed convergence event subtracts its
upper and lower limits; the chapter instead supplies a countable formula
using finite real differences. This avoids an infinity-minus-infinity
expression and states exactly which finite convergence event is proved.

The waiting model is constructed directly with masses `2^-n`. Its tail
probability is `2^(1-m)`, parity probabilities are `1/3` and `2/3`, and
the cumulative function jumps by `2^-m` at integer m. Counting measure
on the same set proves the failure of continuity from above without the
finite-measure condition. Additional boundaries distinguish finite from
countable closure, exclude uniform mass on the positive integers, show
why the finite/cofinite charge cannot extend, and exhibit a coarse
parity observation and an unattained limit point of values.

## Root-owned bibliography and notation intake

Proposed bibliography entry (the only new key used in these files):

```bibtex
@misc{DurrettPTEAuthor2019,
  author       = {Durrett, Rick},
  title        = {Probability: Theory and Examples},
  year         = {2019},
  howpublished = {Author version hosted by Duke University Mathematics},
  note         = {Version 5, dated 11 January 2019. Author PDF;
                  distinct from the Cambridge printed manifestation},
  url          = {https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf},
  urldate      = {2026-09-07}
}
```

All notation roles are local to `sec:p15-measurable-probability`; the root
owns canonical symbol intake. Reuse the actual spellings in the LaTeX:

| First definition/result | Roles to record |
| --- | --- |
| `def:p15-sigma-algebra` | Omega/omega, `2^Omega`, relative complement; calligraphic F/H/C for event collections and generators; `sigma(C)`. |
| `def:p15-measure`, `thm:p15-countable-atomic` | `[0,infinity]`, nonnegative countable sum by supremum, mu, P, atomic weights p and measure mu_p. |
| `def:p15-borel-sets` | Borel collection `mathcal B(mathbb R^d)`; d positive integer and Q rational endpoints. |
| `def:p15-measurable-map` | X, target S/calligraphic S, inverse image `X^{-1}(B)`, event shorthand, `f(X)` composition and `sigma(X)`. |
| `def:p15-simple-functions`, `def:p15-extended-random-variables` | Indicator `mathbf1_A`, finite simple-function coefficients, extended real line, infimum/supremum, liminf/limsup, extended variable Z and dyadic simple approximants s_n. |
| `def:p15-pushforward-law` | Law `mathbb P_X`, point mass `p_X`, measurable transformation f. |
| `def:p15-pi-lambda`, proof of uniqueness | Pi/lambda collections C/L, least lambda-system L_0, auxiliary collection G_A, probability measures nu_1/nu_2. |
| `def:p15-cumulative-distribution` | Real cumulative function F_X and left limit F_X(a-), distinct from event collection calligraphic F and the point mass p_X. |

The finite chapter's probability/indicator/mass notation is retained with
the wider domain declared. No source-only alias macro, canonical row,
driver or style definition was written by this author.

## Integration seam, completed scope and next prerequisites

The body input is `parts/p15/measurable-probability`, after the existing
finite chapter. Its chapter label is `sec:p15-measurable-probability`.
The annex input is `annex/p15/measurable-probability`, after the finite
proof section. Ten `proved=` targets have corresponding full `annexitem`
proofs and backreferences. Root owns both wrappers, bibliography, symbols
and canonical records.

Author read-back covered both complete saved files and the subsequent
short terminology/display edits. It checked all stated proof directions,
finite versus infinite quantities, the simple approximation's three
monotonicity cases, and the exact numerical examples by reasoning. This is
author verification; no manuscript test, build, rendering or independent
acceptance was performed. Existing unrelated files were preserved.

The assignment's measure/random-variable scope is supplied. P15-U1 and
N-x-008 remain broader obligations. Next, construct Lebesgue measure and
the distribution-function existence theorem through the full extension
argument (Durrett Theorems 1.1.4, 1.1.9/A.1.1, A.1.3, and 1.2.2), then
give the full integration foundation and convergence theorems. A coherent
alternative ordering can develop integration first on a given measure
space, since this chapter already supplies such spaces and measurable
approximations; continuous example construction still needs extension.
General conditional expectation, density representation, infinite products,
independence on general spaces and probabilistic limit theorems remain
subsequent units. None is silently used to prove these ten results.
