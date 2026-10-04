# P15.25: predictable quadratic variation and adaptive counts

Date: 8 September 2026. Root authored the full Durrett Section 4.5
presentation and its required bounded-increment, predictable-drift and
conditional-count premises. The body and annex contain nineteen reciprocal
statement/proof pairs. The entire saved mathematical batch was read as
actual LaTeX before the final author corrections below.

Files:

- handbook/parts/p15/predictable-quadratic-variation.tex
- handbook/annex/p15/predictable-quadratic-variation.tex

## Exact primary and read extent

The primary is the held Durrett author Version 5 dated 11 January 2019,
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
It has 490 PDF pages and 2,195,717 bytes. SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
The existing bibliography key is DurrettPTEAuthor2019.
Physical page number is printed page number plus eight.

The complete Section 4.5, printed pp. 240–244, physical pp. 248–252,
was read: Theorems 4.5.1–4.5.3, Example 4.5.4, Theorem 4.5.5,
every case of Example 4.5.6, the complete tail-integral proof of
Theorem 4.5.7, and Example 4.5.8.

The required Section 4.3.1 premises were read on printed pp. 224–226,
physical pp. 232–234: Theorem 4.3.1, the full Doob decomposition,
conditional event counts and Theorem 4.3.4, and the first Pólya urn case.
Printed p. 227, physical p. 235, was read to finish that uniform-law
assertion. The general beta-law statement and density-martingale
introduction on the same page are retained as subsequent source leads.
Exercises 4.3.1–4.3.3 were also read for the random-boundary examples
and the adapted summable-error result.

The actual source equations on printed pp. 225 and 242 were additionally
read from the images at tmp/pdfs/p15-quadratic-source/page-233.png and
page-250.png. These are source-reading derivatives. No manuscript PDF
was produced or inspected.

## Nineteen supplied reciprocal pairs

Each suffix has body prefix thm:p15- and annex prefix annex:p15.
followed by that identical suffix.

| Suffix | Complete supplied content |
| --- | --- |
| doob-decomposition | Integrable adapted drift, existence and uniqueness of the predictable decomposition, and the submartingale/increasing-drift equivalence. |
| bounded-increment-dichotomy | Full stopped-below argument, arbitrary integrable initial value, countable bound union and reflected alternative. |
| conditional-borel-cantelli-source | The distinct source dichotomy proof of conditional Borel–Cantelli, including the finite-probability-sum event. |
| summable-adapted-errors | Nonnegative adapted descent with known-before-step error allowances; finite error sum implies finite convergence and finite accumulated descent, without an expected-total-error premise. |
| predictable-variation-identities | Conditional and realized square variation, both compensated martingales, mean-square identities and the discrete product identity. |
| variation-stopping-transform | Stopping and predictable transforms, the extended realized-variation expectation identity, and failure of an unrestricted terminal-square identity. |
| quadratic-maximal-bound | L2 maximal estimate and full finite expected-variation limit and norm identity. |
| finite-variation-convergence | Convergence on the finite predictable-variation event using stopping before a variance overshoot. |
| bounded-jump-variation-dichotomy | The bounded-jump converse, finite-limit equivalence and two-sided oscillation on the infinite-variation event. |
| variance-clock-normalization | Full reciprocal-square-integrable normalizer proof, predictable transform, right-endpoint integral estimate and pathwise Kronecker application. |
| variance-logarithmic-rate | Everywhere-defined logarithmic normalizer, exact integral and the source asymptotic scale. |
| conditional-borel-cantelli-ratio | Complete source ratio proof retaining both finite and infinite count-variance cases, plus the finite-compensator conclusion. |
| friedman-urn-limit | Full two-color calculation for a >= 0 and b > 0, all source iteration cases, and the additional a = 0 convergence proof. |
| square-root-variation-bound | Full three-times-square-root maximal bound, both tail terms and Tonelli calculations, including infinite expectations. |
| square-root-stopping | L1 optional sampling, the conditional S <= T conclusion, the stronger L2 criterion and fair-walk hitting-time boundaries. |
| variance-clock-examples | Infinite predictable variation with eventually constant paths, initially known random horizons with L1 but not L2 terminal values, and the finite-clock normalization boundary. |
| randomly-bounded-paths | Complete rare-reset martingale for Exercises 4.3.1–4.3.2, samplewise bounds, three recurring values, distributional limit and failure of probability convergence. |
| urn-boundary-calculations | The exact uniform Pólya source case and the random-propensity conditional event-count example. |
| decomposition-rate-boundaries | Adapted versus predictable drift, nonzero initial value, and a fourth-moment demonstration that the normalizer integral hypothesis matters. |

## Corrections incorporated into the actual mathematics

The source's displayed Doob sum uses the final-time term under its summation.
The manuscript sums the properly indexed conditional increment at each j.
Nonnegative conditional versions are selected separately at each time;
countability supplies a common almost-sure event for process claims.

Predictable variation A and realized variation [X] remain different
processes. E([X]_T) = E A_T has extended nonnegative meaning. It does not
imply E X_T squared = E A_T at an arbitrary unbounded finite stopping time.
For the first fair-walk hit of minus one, finite expected hitting time
would contradict bounded sampling and dominated convergence. This
counterargument occurs before the later square-root criterion and hence
does not depend circularly on it.

The finite-clock stop is T_c = inf{n: A_(n+1) > c}. Since A_(n+1) is
known at time n, this is a stopping time and the stopped clock excludes
the overshoot. Its bound supports L2 convergence. The result on
{A_infinity < infinity} requires no global integrability of the unstopped
terminal variable.

The logarithmic source expression is replaced by a function defined on
all nonnegative inputs: sqrt(e) up to e and the source square-root
logarithmic expression above e. Its reciprocal-square integral is
1 + 1/epsilon. The asymptotic assertion uses the original source scale
once the clock exceeds e.

The count proof treats P_n and V_n separately. Infinite conditional
probability sum can coexist with finite, or zero, count-martingale
variance. Both regimes are necessary for the ratio conclusion.

The source's Friedman urn total has an n versus n + 1 indexing mismatch;
the active formula is g + r + (a + b)n after n draws. The printed
iteration does not force convergence when a = 0 because its slope
equals one. The manuscript supplies that entire boundary case using
the squared centered fraction, a summable allowance and harmonic
divergence. The result retains every a >= 0, b > 0 case. Literal
integer-ball counts and their real-weight extension are stated.

The additive-error proof stops before exceeding the fixed allowance,
so it never assumes integrability of the eventual total. The
square-root maximal proof handles zero and infinite clock limits
through nonnegative integrals. Conditional sampling uses events
A intersect {S <= n} at the bounded stopped sigma-fields and
dominated convergence by the integrable stopped maximum.

The random-horizon example specifies a fair walk starting at zero and
an independent horizon already known in the initial sigma-field.
The random-propensity example uses mutually independent uniform inputs
independent of the initial propensity, and normalizes only for n >= 2.
All per-step drift/variance definitions begin at n = 1, and all
cumulative processes have their explicit time-zero values.

## Authored identities and integration

Body at author return: 18,804 bytes, SHA-256
86E9F4F5146D1C712F215098DF77523E0286BDFCF2C35EF83D0409AA1AF18126.

Annex at author return: 33,672 bytes, SHA-256
449E220B0D97BAD05ADC0654FE82142178EA62D1A0A8EFC920D115D5B7B11898.

Drafting scope P15.25. The body and annex are routed after the
Stirling presentation and before the characteristic-function prefix.
The earlier martingale and maximal-inequality boundaries now refer
to these completed results. The local notation is recorded in the
canonical symbol registry.

The general Pólya beta distribution, density-martingale Lebesgue
decomposition, Kakutani product-measure presentation, further
exchangeability/stopping presentations and the source's separate
Kesten–Stigum referral retain their subsequent obligations. The
limited Pólya uniform case here does not complete the general beta
source presentation.

The research skill directed primary reading and this source record;
the PDF skill supported reading exact primary equations.
No independent review, scoped scanner, test, build, manuscript render,
formal admission or generated navigation update ran in this authoring
and integration batch. Consolidated reviews follow all remaining changes.

