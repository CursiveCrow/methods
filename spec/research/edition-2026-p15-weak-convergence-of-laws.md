# P15.23 author return: weak convergence of laws

Date: 8 September 2026. This note records the completed authoring
scope for root integration. All writing and corrections precede
consolidated reviews.

Owned and saved files:

- handbook/parts/p15/weak-convergence-of-laws.tex
- handbook/annex/p15/weak-convergence-of-laws.tex
- This note.

Root retains all shared routes, notation, bibliography, source
records and prior boundary updates. No shared file was edited.

## Exact source and complete read extent

Durrett, author Version 5 dated 11 January 2019:
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
Existing bibliography key: DurrettPTEAuthor2019.

Read the entire Section 3.2, printed pp. 116–125, physical PDF
pp. 124–133. This included every numbered example and theorem,
the unnumbered Scheffe theorem and its proof, all continued
proofs, both tightness directions, the metric referral before
Theorem 3.2.15, and all seventeen exercise statements through
the Section 3.3 heading. Complete source page images were read
for pp. 116–122, including the median density factors, the inverse
exceptional set and both continued selection arguments.

Read source Theorem 1.2.2 and its full inverse-realization proof
on printed p. 11, physical p. 19; the complete required
discontinuity-set exercise 1.3.6 on printed p. 17, physical p. 25,
with its upper/lower-envelope premise; and Section 3.1's full
printed pp. 113–115, physical pp. 121–123, to identify exactly
which normal-limit and elementary-product premises the examples use.
Printed p. 112 was navigational context.

The held source has the required scope. Its separately cited
Stirling formula source, Feller Volume I (1968), p. 52, was not
used as an assumed premise and is not claimed read in this block.

Actual manuscript prerequisites personally read include the
CDF laws and proof; the empirical-CDF definitions, quantile-grid
statement and complete Glivenko–Cantelli proof; the full Gaussian
normalization proof; and the relevant affine-density statements.
The already authored measure/integration/product results supply
Lebesgue measure, pushforwards, Tonelli, bounded and dominated
convergence, Fatou and finite independent variance addition.

## Completed section components and proof routes

There are sixteen reciprocal full statement/proof pairs. All
body labels have prefix thm:p15-; each proof target has prefix
annex:p15. followed by the identical suffix.

| Suffix | Complete scope |
| --- | --- |
| weak-quantile-foundations | Countable jumps and dense continuity points, uniqueness, both inverse conventions, finite endpoints, Borel realization and exact CDF. |
| weak-quantile-coupling | Theorem 3.2.8: the source plateau intervals, their countable exceptional set, and both limiting inverse inequalities. |
| weak-bounded-continuous | Theorem 3.2.9: coupling/expectation proof and the separate continuous-ramp converse. |
| weak-continuous-mapping | Theorem 3.2.10: exact limiting-law discontinuity hypothesis, both the source envelope proof of Borel measurability and an F-sigma proof, composition and bounded expectation conclusions. |
| weak-portmanteau | Theorem 3.2.11: all four conditions and every implication in the source proof. |
| helly-selection | Theorem 3.2.12: scalar compact selection, nested rational subsequences, diagonal, right-continuous envelope and all continuity-point inequalities; finite remaining measure construction. |
| weak-tightness-selection | Theorem 3.2.13: both source directions including a defective selected limit in the failure case; equivalence with uniform tails and the subsequence formulation. |
| weak-coercive-tightness | Theorem 3.2.14: measurable coercive function, exact nonnegative integral bound, extended-value and zero-C qualifications. |
| weak-metric-premises | Full required Exercises 3.2.6–3.2.7: Levy metric properties and equivalence with CDF convergence; Ky Fan metric on almost-sure classes, attained infimum and distance comparison. Also supplies Exercise 3.2.12's probability/constant-limit bridge. |
| weak-subsequence-criterion | Theorem 3.2.15: original metric argument with its premises proved, and an independent direct CDF argument; tightness plus unique-limit method. |
| scheffe-density-limit | The full positive-part proof, equal finite mass and limiting normalization, exact factor-two event supremum; common dominating measure may have infinite mass. |
| weak-elementary-asymptotics | The scalar and triangular product limits needed by the examples; an independently proved central-binomial asymptotic from cosine integrals and Gaussian normalization. |
| weak-rademacher-example | Example 3.2.1: complete independent local-mass proof, uniform control on bounded scaled intervals, Riemann sums, tail removal and odd indices. |
| weak-first-examples | Examples 3.2.2–3.2.5: empirical CDFs, shifted atoms, rare-event geometric scaling and the birthday calculation, including endpoint cases and exact numerical comparison. |
| weak-central-order-statistic | Example 3.2.6 and Lemma 3.2.7: measurable median, null ties, exact index-counting integral, density normalization, affine scaling and the source Scheffe route. |
| weak-convergence-boundaries | Weak versus total variation/probability/expectation convergence, required map continuity and density normalization, and the source two-direction mass-escape mixture. |

## Corrections and source qualifications applied directly

1. Source Theorem 3.2.10's conclusion prints g(X) although its
   named limiting variable is X_infinity. The manuscript uses
   g(X_infinity) consistently.
2. Source Example 3.2.2 refers to Glivenko–Cantelli as Theorem
   8.4.1. The exact same held author version gives the required
   empirical-CDF result in Theorem 2.4.9; the written complete
   proof at thm:p15-glivenko-cantelli is used directly.
3. A density remains a density throughout. The source's later
   shorthand P(Y_n = y) for a continuous density is replaced by
   explicit f_(Y_n)(y), with the support and endpoint conventions
   supplied.
4. The source vague-CDF notation is retained with its exact
   meaning. For a defective limit F, the finite remaining
   measure has CDF F minus its negative endpoint limit beta.
   A positive beta is recorded as escaped negative mass, not
   mistaken for the CDF of that remaining finite measure.
5. Unit probability mass is retained in the complement proof.
   Helly's remaining measure is a subprobability. Scheffe's
   common dominating measure can have infinite mass, but all
   density integrals, including the limit, equal one.
6. Quantiles use the source strict inverse on u in (0,1),
   excluding both endpoints. Both plateau endpoints are finite.
   The exact exceptional set is countable, hence Borel and null.
   The coupling preserves marginals, not the original joint law.
7. Tightness preserves the source left-closed, right-open
   complement convention and its limsup quantifier. Its
   equivalence with uniform tails is proved by treating the
   finitely many initial laws explicitly.
8. The coercive function is explicitly Borel. The proof uses
   finite positive thresholds instead of division by a possibly
   infinite infimum.
9. Ky Fan's distance is a metric on variables modulo almost-sure
   equality. The infimum-attainment proof supplies the exact
   comparison at alpha rather than assuming an admissible
   infimum. Both real-line Levy implications are proved, so
   Theorem 3.2.15 retains its original metric route.
10. For the birthday example, the product stops at its zero
    factor when the finite domain is exhausted; it is not
    extended into negative factors. Exact value at N = 365,
    m = 22 is 0.52430469233745; the source leading approximation
    is 0.51529604509686.
11. The normal examples do not assume an unwritten CLT or
    Stirling formula. The central coefficient is proved by
    an independent cosine-integral argument. The Rademacher
    local estimate is then proved by factorial ratios, with
    uniform error, complete Riemann sums and both parities.
    The median retains its own source density/Scheffe proof.

## Integration and notation intake

Drafting scope: P15.23. Body root:
sec:p15-weak-convergence-of-laws.
Annex root: sec:annex-p15-weak-convergence-of-laws.
Root reserves P15.22 for maximal inequalities and owns final
physical placement and shared imports.

At def:p15-weak-law-convergence: laws mu_n, proper CDFs F_n,
finite variables X_n, index infinity, weak arrow Rightarrow,
and equality in distribution.
At def:p15-weak-quantiles: Q_F, source F inverse, a_F(u),
b_F(u), u in (0,1), and uniform-space Lebesgue measure.
At thm:p15-weak-quantile-coupling: copied Y_n and exceptional E.
At thm:p15-weak-bounded-continuous: bounded continuous g and
source ramps g_(x,epsilon).
At thm:p15-weak-continuous-mapping: Borel g and D_g.
At def:p15-weak-boundary-sets: closure, interior, boundary and
continuity sets. At def:p15-helly-cdf-limits: source Rightarrow_v,
endpoint limits beta and gamma. At thm:p15-helly-selection:
rational G, diagonal n_k and remaining finite measure nu.
At def:p15-weak-tightness: M_epsilon and uniform radius R.
At thm:p15-weak-coercive-tightness: varphi, C and threshold L.
At def:p15-weak-metrics: Levy rho and Ky Fan alpha, locally
distinct from earlier chapter roles.
At def:p15-weak-total-variation: source event-supremum TV norm,
normal density phi and CDF Phi.
At thm:p15-weak-elementary-asymptotics: scalar/row coefficients,
row length k_n, finite limit ell and central coefficient C_n.
At the example results: fair-sign partial sums, geometric X_p,
birthday T_N, median V_(n+1), and scaled median Y_n. These
are separate local example models. No new macro or key is needed.

## Authoring and exact remaining work

One full author read-back was performed on the initial body and
annex batch. The added metric prerequisite and its source route
were then read in full as the final substantive addition.
No independent review, review wait, scanner, test, build,
manuscript render or acceptance procedure was run.

The entire numbered Section 3.2 theorem/example presentation is
written. The separate Section 3.1 source proof through Stirling's
formula remains owed, including its actual cited source extent;
the present independent Rademacher proof does not replace that
source route. The later alternate Theorem 3.2.15 argument at
the end of 3.3.17 belongs to that separately owed characteristic-
function presentation.

Other Section 3.2 exercise presentations remain to be reconciled
individually. Exercises 3.2.6, 3.2.7 and 3.2.12 are proved here.
The content of 3.2.9 already has a complete prior proof at
thm:p15-continuous-cdf-uniform; it is not duplicated here.
The other exercises, including extreme-value laws, integration
bounds, the additional metric comparison, discrete approximation,
integer-valued laws, converging-together and product lemmas,
sphere coordinates and moment criteria, are not claimed written
by this return.

The research skill governed this one source note and attribution.
The PDF skill was used to read primary equations and page
continuations; no manuscript PDF was produced or inspected.
