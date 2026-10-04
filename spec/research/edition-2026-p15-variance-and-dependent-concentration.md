# P15: variance and dependent-sampling concentration

Author block: 9 September 2026, 01:57:33--02:42:33 UTC.
Owned files: handbook/parts/p15/variance-and-dependent-concentration.tex,
handbook/annex/p15/variance-and-dependent-concentration.tex, this note,
and handbook/registry/symbols-intake-p15-variance-and-dependent-concentration.csv.
Root owns shared drivers, bibliography and canonical symbols.

## Primary identity and actual reading

Wassily Hoeffding, "Probability Inequalities for Sums of Bounded Random
Variables", Journal of the American Statistical Association, March 1963,
printed pp.13--30.

Held primary: source/references/hoeffding-bounded-sums-1963/hoeffding-1963.pdf.
The image-only file has 19 physical pages, including one preceding cover.
Printed page equals physical page plus eleven.
File size 1,451,039 bytes.
SHA256: 3021BCC097EF23A99A84D0EEF8DCCE2FD835C71DF79A105727D3E03F8F0B8930.
Identity verified from the actual first journal page, running journal/date
headers, final body and complete bibliography.
Use canonical key Hoeffding1963BoundedSums, added by root.

Read every journal page, physical 2--19 / printed 13--30, from actual images.
The held source images cover physical 2--15 in
tmp/pdfs/p15-hoeffding-source/source-NN.png.
New source-reading images for physical 16--19 are in
tmp/pdfs/p15-hoeffding-variance-source/source-NN.png.
These are primary-reading intermediates, not manuscript renders.
No source PDF was changed or acquired in this block.

The research and PDF skills guided primary reading and capture of this
source note. A bounded research delegation was attempted but the agent
thread limit prevented it; no additional agent ran.
The author read the actual manuscript conventions and current 2026
contract, and the complete saved root bounded-concentration chapter
before using its interfaces.

## Frozen substantive scope

This component supplies:

- Theorem 3, printed p.16, including (2.8), (2.9), extremizing two-point
  law (2.10), and endpoint statements; (2.11)--(2.14) on pp.16--17,
  including the Bennett, Bernstein and Prohorov comparisons.
- The variance-specific comparison in Section 3, p.20:
  (3.10)--(3.15), the exact rho series and log ratio, and the relation
  to the common-range theorem through variance at most -ab.
- The independent partial-sum maximal variance extension in (2.17),
  pp.17--18, with a full first-crossing proof of its terminal-moment bound.
- Lemmas 2 and 3 and the proof of Theorem 3, pp.23--24, including
  (4.18)--(4.22), explicit optimizing parameter, and the distinct
  tangent-line route to Bennett's simpler bound.
- All of Section 5, pp.24--28: convex averages (5.1)--(5.2);
  one-sample U statistics (5.3)--(5.7); two-sample U statistics
  (5.8)--(5.11); repeated-index statistics (5.12)--(5.17), including
  the Cramer--von Mises identity; finite-range dependence (5.18)--(5.21)
  and its continuation at the top of p.28.
- All of Section 6, pp.28--29: the finite-population model and parameters,
  Theorem 4, and the full symmetrized convex comparison (6.1)--(6.10).
  The explicit partition coefficients in the annex fill the source's
  unspecified arithmetic-mean coefficients without changing its route.

This is a complete author treatment of those selected source components.
Reading the other journal pages is not a claim that every distinct
presentation mentioned there has been authored by this component.

## Reciprocal statement/proof map

Each body identifier has the reciprocal annex target shown here:

| Body result | Full annex proof |
| --- | --- |
| thm:p15-upper-moment-extremal | annex:p15.upper-moment-extremal |
| thm:p15-variance-moment-concavity | annex:p15.variance-moment-concavity |
| thm:p15-variance-tail-chain | annex:p15.variance-tail-chain |
| thm:p15-variance-maximal | annex:p15.variance-maximal |
| thm:p15-variance-bound-comparison | annex:p15.variance-bound-comparison |
| thm:p15-variance-optimality-boundary | annex:p15.variance-optimality-boundary |
| thm:p15-concentration-convex-mixture | annex:p15.concentration-convex-mixture |
| thm:p15-one-sample-u-concentration | annex:p15.one-sample-u-concentration |
| thm:p15-two-sample-u-concentration | annex:p15.two-sample-u-concentration |
| thm:p15-repeated-index-concentration | annex:p15.repeated-index-concentration |
| thm:p15-cramer-von-mises-kernel | annex:p15.cramer-von-mises-kernel |
| thm:p15-finite-range-concentration | annex:p15.finite-range-concentration |
| thm:p15-without-replacement-convex | annex:p15.without-replacement-convex |
| thm:p15-dependent-concentration-examples | annex:p15.dependent-concentration-examples |

Chapter label: sec:p15-variance-dependent-concentration.
Annex section label: sec:annex-p15-variance-dependent-concentration.

The chapter defines the centered upper-variance setting, ordered U
statistics with their common measurable input spaces, finite-range
dependence as independence of separated vectors, and the two precise
finite-population sampling laws before using them.
Zero variance, zero/nonpositive upper bounds, upper endpoints, empty
residue avoidance, and population size one are handled explicitly.
The distribution is bounded only from above in the variance theorem;
the geometric-power example has finite variance and no negative
exponential moment, showing why the lower-tail route needs another premise.

The exact twenty-variable two-point example calculates its binomial tail
and all four variance bounds. Further calculations cover the unadjusted
Kendall pair statistic, normalized strict Wilcoxon--Mann--Whitney count,
Cramer--von Mises statistic, moving products, a four-value population,
and a three-variable pairwise-independent countermodel.
All numerical examples are stipulated probability models, not empirical
data or estimation claims.

## Proof routes and direct source corrections

Hoeffding's Lemma 2 cites a Bennett proof rather than proving its
quadratic moment majorant. The new annex gives an explicitly editorial
Hermite-quadratic proof: interpolate exp(hx) and its derivative at
-v/b, interpolate its value at b, prove the sign on the entire
half-line x<=b using a full Rolle remainder argument, and match the
first two moments of the two-point law. This proves the promised
moment bound but does not claim to reproduce an unread Bennett proof.

The original p.23 line appears to print "Bennett [1]". The actual
bibliography identifies [1] as Bahadur--Rao1960 and [2] as George
Bennett, "Probability inequalities for the sum of independent random
variables", JASA57 (1962), pp.33--45. No 1956 identity is supported.
The earlier transient coordination message suggesting 1956 was corrected
immediately after reading the actual bibliography and is not manuscript
or source-intake evidence.

Hoeffding's Lemma 3 concavity derivation is preserved in full, with the
zero-variance endpoint supplied. The source's two routes to (2.9) are
preserved: comparison with the exact bound and the separate tangent
moment envelope followed by its own optimization.
Bernstein and Prohorov comparisons receive complete elementary proofs.
The source's optimality assertion is confined to its exponential-moment
method and to the specified functional reduction; a one-variable
Cantelli calculation supplies a strictly smaller exact tail optimum.

For the B1/B2 comparison, rho(x)>x/6 produces an upper bound on the
ratio, because the ratio is exp(-n phi). The source paragraph following
(3.15) describes this as a lower bound; the active displayed inequalities
have the correct directions.
The source's approximation exp{-nt^3/(6b sigma^2)} is recorded with
the actual proved regime: fixed positive b,sigma^2 and t decreasing
to zero. Small lambda=bt/sigma^2 alone need not make w=t/b small.
Indeed, holding 0<w<1 fixed and letting lambda decrease to zero gives
phi/(w^2 lambda/6) tending to 6 rho(w)/w, which is not generally one.
The body therefore states the exact ratio and a justified asymptotic
regime rather than silently asserting the broader approximation.

For nonidentically distributed U inputs, the annex centers each
permutation block by its own expectation before averaging.
Common-distribution assumptions are stated separately for the
mean-specific and variance-specific transfers.
For finite-range dependence, joint independence within residues is
proved by induction from prefix/tail vector independence.
The unequal-size step uses q L(h/q)<=k L(h/k), proved from convexity
of the actual log moment envelope and L(0)=0; it is not an unexplained
replacement of n_i by floor(n/r).

For without-replacement sampling, the proof constructs the source's
symmetrized repeated-index kernel with explicit partition weights,
proves the averaging identity and its linear mean, and then applies
finite Jensen. Its covariance calculation retains the exact
finite-population correction, while the transferred exponential bound
continues to use the population variance. It does not assert the
same convex comparison for arbitrary signed weighted samples.

## Dependencies and remaining source routes

Read and used the actual root interfaces:

- thm:p15-conc-exponential, including its chord and centered moment bounds;
- thm:p15-conc-common-range, including the binary-divergence bound,
  the exact g(p) refinement, and endpoints;
- thm:p15-conc-unequal-ranges, restricted here to its unweighted
  common-interval sum specialization.

Their chapter is sec:p15-bounded-concentration-learning.
Root separately supplies its first-theorem comparison (3.5)--(3.9) as
thm:p15-conc-common-comparison / annex:p15.conc-common-comparison, and the
bounded/maximal martingale presentation.

The actual new root statement thm:p15-conc-benchmarks and its complete
annex:p15.conc-benchmarks proof were read before this handoff. They supply
the explicit source routes for:

- Section 1 moment comparisons (1.5)--(1.6);
- normal-tail discussion (2.15)--(2.16), p.17, including the exact
  displayed triangular-array assumptions via the existing Lyapunov
  theorem, Gaussian moment calculation, and full Mills-ratio squeeze;
- the p.15 footnote's sharp nonnegative-mean-only construction and
  exponential-minus-one improvement at the optimizing parameter.

Those source routes are therefore supplied in the combined manuscript;
they are not unresolved items in this component's source handoff.
The remaining independent partial-sum maximal variance consequence
(2.17) is now supplied here by thm:p15-variance-maximal and its complete
first-crossing proof. This keeps joint independence explicit, and does
not assert a variance-sensitive martingale result from unconditional
variances alone.

The p.15 footnote also proposes using general finite linear combinations
of exponentials satisfying a pointwise majorant condition. Its particular
subtracted-exponential construction is fully supplied by root.
The general majorant principle itself, including integrability and the
inequality direction for negative coefficients, is now stated and proved
in thm:p15-variance-optimality-boundary and its annex.
No additional general optimization theory beyond the source's stated
majorant proposal is claimed.
The distinction between exponential-method optimality and actual tail
optimality from Section 1 and its footnote is explicitly proved here.

Bennett1962's distinct original proof presentation, and the original
Bernstein/Prohorov sources, have not been acquired or read in this block.
Their named consequences as presented by Hoeffding are fully proved
here through the stated editorial/source routes.

## Author handoff

The complete body, annex, source note and notation intake were read by
the author after the writing batch. Direct final corrections made the
positive-threshold and strict-width premises explicit, defined the empty
falling factorial, specified common measurable input spaces, and stated
endpoint limits as increasing thresholds with decreasing events.
The added maximal pair and all subsequent correction paragraphs were
read in full as part of this author read-through.
There are fourteen reciprocal statement/proof pairs.
Shared integration and consolidated independent
review remain root responsibilities. No manuscript scanner, test, build,
independent review or manuscript render was run.
