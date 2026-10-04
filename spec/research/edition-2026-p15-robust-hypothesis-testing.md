# P15-U6: robust probability-ratio testing

Author block began 9 September 2026 at 02:34:11 UTC; deadline 03:19:11 UTC.
Owned manuscript pair: handbook/parts/p15/robust-hypothesis-testing.tex and
handbook/annex/p15/robust-hypothesis-testing.tex. This note and the disjoint
bibliography/symbol intakes accompany it. Root owns shared integration.

## Verified primary and actual reading

Peter J. Huber, "A Robust Version of the Probability Ratio Test",
The Annals of Mathematical Statistics 36(6), December 1965, pp.1753--1758,
DOI 10.1214/aoms/1177699803.

Acquired free from the journal Project Euclid endpoint:
https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-36/issue-6/A-Robust-Version-of-the-Probability-Ratio-Test/10.1214/aoms/1177699803.pdf

Local capture:
source/references/huber-robust-probability-ratio-1965/huber-1965.pdf.
Size 578627 bytes; six pages, directly corresponding to printed 1753--1758.
SHA256: B3E9489F3CD1F7AB9E7F65AC205128DD31A14B1DF44DB620650A1CBD71D17970.
The matching official journal issue was also located at
https://www.jstor.org/stable/i312826 (article2239116).
The actual first page verifies title and author; all six journal pages,
ending in the complete bibliography, were read in full.
The archival PDF creation date 2006 describes digitization, not publication.
The source body is image-only; a footer text extraction was not treated
as the body. All six source images are in tmp/pdfs/p15-huber-robust-source/.
The exact original PDF is preserved.

Research/PDF skills guided the acquisition and original-page reading.
A requested background source-location agent could not start because
the agent thread limit was reached. No background review or other
agent ran. Conventions and the current edition contract were read.

## Full source route

Read the whole original, Sections 1--8:

- p.1753: motivation, arbitrary probability-measure contamination classes,
  and the sampling/testing setup.
- p.1754: three risk criteria, the least-favorable-pair implication,
  Theorem1, and original density/normalization equations(2)--(3).
- p.1755: Lemma1 normalization proof, the retained-mass ratio b,
  clipped ratio equation(4), complete Lemma2 and the coupling lead.
- p.1756: fixed-sample likelihood test equation(5), its constant
  threshold randomization and ordered-sum proof; the equal-radius
  sign-statistic limit; first sequential error argument.
- p.1757: the partial expected-sample-size asymptotic, unequal-radius
  drift qualification, MLR extension, and the distinct variation
  construction equation(6).
- p.1758: variation normalization equation(7), Lemma3 and its proof,
  the variation/MLR bridge, historical open questions and references.

The body retains both actual neighborhood types. In the variation
section the source norm has range0--2 and its mass transfers are
epsilon/2. The manuscript makes explicit that this is twice the
sup-event convention; it does not conflate it with contamination.

## Statement/proof map

Chapter label: sec:p15-robust-hypothesis-testing.
Annex section: sec:annex-p15-robust-hypothesis-testing.

| Body result | Reciprocal complete proof |
| --- | --- |
| thm:p15-robust-overlap | annex:p15.robust.overlap |
| thm:p15-huber-contamination-pair | annex:p15.huber.contamination.pair |
| thm:p15-huber-tv-pair | annex:p15.huber.tv.pair |
| thm:p15-huber-stochastic-order | annex:p15.huber.stochastic.order |
| thm:p15-robust-product-order | annex:p15.robust.product.order |
| thm:p15-huber-minimax-tests | annex:p15.huber.minimax.tests |
| thm:p15-robust-sensitivity | annex:p15.robust.sensitivity |
| thm:p15-robust-testing-calculation | annex:p15.robust.testing.calculation |
| thm:p15-robust-sampling-boundary | annex:p15.robust.sampling.boundary |
| thm:p15-robust-mlr-extension | annex:p15.robust.mlr.extension |
| thm:p15-robust-sequential-errors | annex:p15.robust.sequential.errors |
| thm:p15-robust-sequential-asymptotic | annex:p15.robust.sequential.asymptotic |

The active Neyman--Pearson experiment, threshold theorem and full
Neyman--Pearson proof were read in
handbook/parts/p15/hypothesis-tests-and-confidence.tex and its matching
annex. The used labels are def:p15-statistical-experiment,
thm:p15-likelihood-threshold and thm:p15-neyman-pearson.
The new pair is dominated by the finite measure P0+P1; the whole
contamination class need not be dominated by that measure.

## Mathematical construction and endpoint handling

Contamination overlap is proved equivalent to
integral max((1-epsilon0)p0,(1-epsilon1)p1)<=1.
For equal fraction e it occurs at e>=d/(1+d), where
d=sup-event total variation between the nominal laws.
Variation balls with the source's norm radius epsilon intersect exactly
at epsilon>=d. A common law proves the exact no-discrimination
maximin power alpha; constant decisions solve the corresponding
weighted and maximum-loss problems.

The source normalization functions are proved continuous by their
positive-part integral formulas, strictly increasing after their
flat region, and unbounded. This gives unique clipping parameters
for positive fractions and explicit zero-fraction choices.
Disjointness proves that the clipping thresholds are correctly
ordered. Excess masses are nonnegative, have exactly the required
contamination masses, and occupy the required extreme-score regions.
The variation pair uses equal positive and negative mass transfers,
so normalization and the full variation norm are both proved.

Every score is assigned on common nominal null sets, since arbitrary
contaminations can place mass there. The robust test therefore is not
defined only up to nominal almost-everywhere equality.
The source's stochastic-order proof is preserved separately for
contamination and variation neighborhoods.
The real-score quantile coupling is fully constructed and proved;
no disintegration or standard-Borel premise is silently imposed on
the arbitrary original observation space.

All fixed-sample statements refer to a common law R and independent
product R tensor n. Positive uncertainty in at least one contamination
class prevents simultaneous zero and infinite factors in the product.
When both fractions vanish, the ordinary joint-density test handles
mixed singular coordinates on the common zero-density set.
Level 0, level 1, finite threshold atoms and the constant boundary
randomization are explicit.
The proof gives all three original fixed-sample risk criteria, including
an equalizer construction for unequal positive error losses.

The finite example retains the full continuum of contamination
probabilities over its three observation values, not a finite list
of candidate laws. Its one- and two-observation score distributions,
randomization probabilities and error rates are fully calculated.
A separate normal example gives explicit clipping densities and
normalization through Phi. Both show why a nominal advertised level
does not transfer unchanged.
The difference between per-observation contamination, whole-sample
contamination and dependent repeated observations is proved explicitly.

The MLR extension states its common dominating measure and pointwise
cross-product condition. The proof derives stochastic ordering and
constructs a Borel monotone ratio extension across varying supports.
It then reproduces the source's endpoint-to-composite argument for
both neighborhood types.

## Sequential and broader scope boundaries

The sequential error theorem covers every separated constructed pair,
including zero-radius cases and infinite log-score endpoints. The
source path-order argument is proved in full. Finite expected
termination is supplied by an additional explicit affinity argument:
eta=integral sqrt(q0 q1)<1, and ordered half-power moments give
P0(N>n)<=exp(-A/2)eta^n and P1(N>n)<=exp(B/2)eta^n.
This avoids assuming a drift moment or bounded increments merely
to obtain termination.

The expected-size asymptotic is fully proved under its additional
bounded positive score premise. It includes negative/positive drift,
the stopped exponential error bounds, finite expected stopping time,
absolute-integrability justification for the stopped-sum identity,
uniform overshoot bounds, and uniform expected-size ratios.
Both boundaries diverge with no relative growth restriction.
This supplies a rigorous version of the source's partial asymptotic
argument for bounded clipping.

The formerly remaining unbounded-score expected-size endpoint is now
supplied in the body/annex pair robust-sequential-endpoints.tex, at
thm:p15-robust-endpoint-closure and annex:p15.robust.endpoint.closure.
It retains the original arbitrary neighborhoods, zero/infinite clipping
endpoints and vanishing-actual-error premise. The complete proof derives
the needed log-integrability, truncation, restart and overshoot bounds.
The separate size classifications assume both boundaries diverge and
distinguish finite entropy, infinite entropy with finite scores, and
positive singular-score mass. The earlier bounded-score theorem remains
intact. See edition-2026-p15-robust-sequential-endpoints.md for the exact
source correction record and all nine new proof pairs.

Huber's Section 8 questions are recorded as questions raised by the 1965
paper, not as claims that they remain open in current literature:
finite-boundary expected-size least favorability, contamination by
one shared unknown law under both hypotheses, and more than two
decisions. Those are different problems from the product-neighborhood
fixed-sample result.
Further U6 authoring remains for robust estimation/influence functions,
breakdown, robust confidence procedures, and data-dependent selection
of a contamination fraction or neighborhood radius.

## Author read-through and handoff

The complete body, annex, source capture and intakes received the author
read-through after the writing batch. Final corrections clarified the
normal-example contamination symbol, table point masses, log-score
infinity wording, and the zero-radius ordered-family bridge.
Final hashes are returned with this note. This is source reading and mathematical
authoring, not independent admission. No reviews, scanners, tests,
builds or manuscript renders were run. Root integrates the stable
labels, bibliography intake and notation rows.
