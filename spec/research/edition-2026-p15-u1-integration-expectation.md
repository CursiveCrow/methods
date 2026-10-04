# P15-U1: integration and expectation foundations

Date: 8 September 2026 UTC / 7 September Pacific. Author:
`/root/probability_measure_author`. Fresh block began 05:15 UTC.
Status: eleven complete theorem/proof pairs authored and read back.
Independent reviews, integration, production and admission remain due.

## Written files and dependencies

| Artifact | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p15/integration-expectation.tex` | 433 lines; four sections | `DA89703F5694C0E909294EC4CB6BF414FF4C1F390B74F4D71682201B622DD57A` |
| `handbook/annex/p15/integration-expectation.tex` | 552 lines; eleven full proofs | `F5F1AE8A99F95BE08E1C4A448EF1DF865D9B49E6D238A6DECED46BEF82EBC7FE` |

The accepted `measure-extension.tex` body/annex were revalidated at hashes
`E1333244607DB51AE1EE5EC8FBF6AECA9AE8A2D85989677ED29ED9866119558E`
and `D5179047198A9EDDE628274345D19DE75E30FC33CE065DAEC9F23F02DE83838F`.
Their three text PASS roles were checked in the actual
`edition-2026-evidence-extension-{source,topic,publication}-review.md`
reports. The earlier measurable-probability pair also retains hashes
`C249F33E0E0FC88084B05A7D44098DB87B3E4814083B34709D6DBE2B562340D9`
and `FBB9E6C733A1F286F7E56FC31B7E76D4412D781E03711ED02D8D4B3AAEF8C8FC`.
These prerequisites provide nonnegative sums, measures, measurable limits,
simple approximation, constructed Borel length, the uniform space,
pushforward laws and countability of positive point masses.

## Primary reading and mathematical scope

Held source: Rick Durrett, *Probability: Theory and Examples*, author
Version 5 dated 11 January 2019, at
`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`.
Verified SHA256:
`AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886`.
Primary locator: [Duke author PDF](https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf).
The previously verified 490-page author manifestation was reused unchanged;
no new source or bibliography entry was acquired.

All twenty complete printed pages **18-37** were freshly read from the
saved PDF with `pypdf` (physical PDF pages **26-45**). Section 1.4 runs
from p. 18 through its exercises on p. 24; Section 1.5 runs from p. 24
through its exercises on p. 28; Section 1.6 runs from p. 28 through
Exercise 1.6.16 on p. 37. The beginnings/endings sharing those pages were
also read. Thus the exact entire assigned extent, including the exercise
remainder after p. 36, was inspected before coverage claims.

Complete printed pages **18, 19, 22, 23, 25, 26, 27, 29, 31, 32 and 33**
were additionally rendered from that saved PDF in memory with `pypdfium2`
and visually inspected. No manuscript PDF or page image files were created.
The PDF skill guided source reading; the research skill guided this single
primary-source map. The assignment's no-subagent instruction controlled
the research skill's delegation suggestion.

The new presentation defines nonnegative simple integrals even on pieces
of infinite measure, with `0 * infinity = 0`, and defines the nonnegative
integral as their supremum. Its direct monotone convergence proof works
for an arbitrary measure. This is an independently supplied proof route,
not a claim that Durrett uses the same ordering: his Section 1.4 starts
on a sigma-finite space and passes through bounded functions on finite
supports. The explicit `integral-source-bridge` theorem proves equality
with both of those source stages; the signed stages agree by the same
positive/negative parts. The bridge's bounded approximations include
zero bounds and zero-measure supports.

## Exact result map

Body suffixes below have prefix `thm:p15-`; proof suffixes have prefix
`annex:p15.`. All eleven targets and backreferences are supplied.

| Suffix | Exact source foundation | Complete annex extent |
| --- | --- | --- |
| `simple-integral-laws` | Section 1.4 Step 1, p. 18; Lemmas 1.4.1-1.4.2, p. 19 | 12-47: refinement, zero/infinite measures, finite operations, monotonicity and overlapping representations. |
| `monotone-integral` | Nonnegative construction pp. 21-22; Theorem 1.5.7 p. 27 | 49-84: agreement on simple functions and direct lower-simple/theta proof, including infinite limits. |
| `nonnegative-integral-laws` | Lemma 1.4.5 p. 22; Exercise 1.4.1 p. 24; Theorem 1.5.5 pp. 26-27; Exercises 1.5.4/1.5.6 p. 28 | 86-144: nonnegative additivity/scaling/series, zero-integral and finite-a.e. facts, measurable a.e. replacement, Fatou, and the measure defined by restricted integrals. |
| `signed-integral-laws` | Step 4 pp. 22-23; Lemma 1.4.6 and Theorem 1.4.7 p. 23; Exercise 1.6.16 p. 37 | 146-203: parts and their measurability, finite representatives, difference representations, signed linearity/order/absolute bound and absolutely convergent disjoint-set sums. |
| `integral-source-bridge` | Step 2 and Lemma 1.4.3 pp. 20-21; Step 3 and Lemma 1.4.4 pp. 21-22 | 205-252: upper/lower simple equality on finite supports, sigma-finite truncation and equality of the two integral constructions. |
| `dominated-bounded-convergence` | Theorem 1.5.3 p. 26; Theorem 1.5.8 p. 27; Theorem 1.6.7 p. 30 | 254-309: dominated convergence in L1 and of integrals; bounded convergence in measure, including proof of the limit's boundedness and support. |
| `holder-integral` | Theorem 1.5.2 p. 25 and Cauchy-Schwarz remark p. 26; Exercise 1.5.1 p. 28; Theorem 1.6.3 p. 29 | 311-355: zero/infinite norms, essential-supremum attainment a.e., Young's inequality, finite positive normalization and both exponent endpoints. |
| `jensen-integral` | Theorem 1.5.1 p. 25; Theorem 1.6.2 p. 29 | 357-403: convex secant inequalities, continuity, a finite supporting slope, measurable composition and integration of the supporting affine function. |
| `expectation-law-integral` | Expectation definition p. 28; Theorem 1.6.1 p. 29; Theorem 1.6.9 pp. 32-33 | 405-459: expectation properties, all scalar signs for nonnegative infinite means, law transformation by indicators/simple approximation, equivalent integrability, and countable atomic evaluation. |
| `expectation-bounds` | Theorem 1.6.4 pp. 29-30; formulas (1.6.2)-(1.6.4), p. 33 | 461-496: measurable nonnegative-function bound with an empty-event branch, Markov, square-integrability implying finite mean, variance formula/scaling and centered Chebyshev. |
| `moment-controlled-convergence` | Theorem 1.6.8 and complete proof, p. 31 | 498-552: limit moment bound, prior proof of integrability, truncation at non-atomic levels, uniform tail error and convergence of means. |

The source's Theorem 1.5.3 statement gives only integral convergence; this
chapter supplies the stronger L1 conclusion by the same finite-measure
estimate. Its limit bound and support are proved rather than assumed.
Hölder normalization is applied only to finite positive norms; all zero
and infinite cases are handled first. The generalized probability bound
requires Borel measurability of the nonnegative function, making the
expectation's domain explicit. The empty target event has its own branch.
Signed infinite means never undergo an infinity-minus-infinity subtraction.

Examples are fully computed on constructed measures: the uniform variable
has mean 1/2, second moment 1/3 and variance 1/12 by finite cell bounds;
the paired countable model with masses `2^{-(n+1)}` has two infinite part
expectations and no signed mean. Concentrating functions show strict
Fatou and failure of convergence of integrals; a disjoint-interval sum
proves no integrable dominator exists. Expanding supports show why the
bounded-convergence domain must have finite measure, and negative tail
indicators show that increasing signed functions need an additional lower
integrability condition. These examples use no unconstructed density.

## Root-owned notation and integration

Existing bibliography key: `DurrettPTEAuthor2019`. No new entry is needed.
All roles below belong locally to `sec:p15-integration-expectation`:

| First anchor | Notation roles |
| --- | --- |
| `def:p15-simple-integral`, `def:p15-nonnegative-integral` | integral with respect to mu, nonnegative simple s/t and coefficients a_j, indicators, integral over A, nonnegative extended multiplication including zero times infinity, a.e. relation. |
| `def:p15-integrable-functions` | f+, f-, absolute value, defined versus undefined signed integral, finite measurable representative. |
| `def:p15-lp-convergence` | norms `\|f\|_p`, essential supremum norm, L1 classes, L1 convergence and convergence in measure. |
| `def:p15-convex-integral` | convex real function varphi and mixture coefficient t; finite supporting slope a and base point c in its proof. |
| `def:p15-expectation-integral` | expectation `\mathbb E[X]`, restricted expectation `\mathbb E[X;A]`, moments, mean m and `\operatorname{Var}(X)`. |
| Theorem-local and proof-local | weighted measure nu_f; Holder conjugate exponents p/q; lower bound c_A; positive threshold r; simple lower/upper a_n/b_n and floor; monotone proof theta/E_n; moment-control g/h/K, truncation Y^(M) and tail coefficient epsilon_M. |

Root can insert `parts/p15/integration-expectation` and
`annex/p15/integration-expectation` after the accepted measure-extension
routes. Chapter label: `sec:p15-integration-expectation`. The author edited
only these two new manuscript files and this note. No driver, canonical
bibliography/symbol record, style, test, manuscript build/render, subagent
review or admission was changed or performed.

Author read-back covered the complete body and complete annex, followed
by all precision edits. The assigned integration/expectation foundation and
all eleven promised proofs are supplied. This does not complete every
source exercise or example: approximation by continuous functions,
Riemann-Lebesgue, general Lp results including Minkowski, additional
one-sided/sharp probability bounds, and exponential/normal/Poisson/general
geometric moment computations retain their own obligations. Density
representation, Radon-Nikodym, general conditional expectation, product
measures and Fubini remain the subsequent representation/product work.
The broader P15-U1 / N-x-008 obligation remains open.
