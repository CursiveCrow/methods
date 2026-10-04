# P15-U3: Bayes-factor computation

9 September 2026. Block began 01:08:44 UTC; deadline 01:53:44 UTC.
Owned new body/annex: handbook/parts/p15/bayes-factor-computation.tex and
handbook/annex/p15/bayes-factor-computation.tex; this note; disjoint symbols
intake. Root owns all shared routes and canonical bibliography/symbols.

The first action corrected the prior component's model definition to require
finite jointly measurable likelihood versions, matching the saved root
posterior-kernel theorem. Corrected model-comparison body SHA:
01F3E46555141A6F92FE382CAA70B4E4EEC75D316E904482F08737F35DDD7FF2.
Its amended source note SHA:
8A360C9460460A0B257CECC137782021372FF2788257E38F0C831C8671A6854F.
That correction did not change its annex or any shared route.

## Exact source scope

Read Kass and Raftery (1995), Bayes Factors, JASA 90(430), Section 4 in full,
printed pp.777-781 (PDF pages 6-10), in the held text and actual source images.
Local original:
source/references/kass-raftery-bayes-factors-1995/kass-raftery-1995.pdf
SHA: 3DA446B1AEA8E64801DBE17C0B727A71E7ACBBC304D4879532066C7139E50D86.
The 24-page file includes one cover and journal pp.773-795.
Use existing canonical key KassRaftery1995BayesFactors.

Read all of 4.1.1 posterior-mode Laplace; 4.1.2 MLE, information and
one-step variants; 4.1.3 Schwarz; 4.2 prior Monte Carlo, importance and
quadrature; 4.3 posterior simulation, harmonic/generalized harmonic and
further methods; 4.4 comparison through the end on p.781. Source images
resolved the equations omitted by the two-column text extraction.
No claim to have completed the entire article or its cited primary papers.

## Complete authored proof map

Each result below has a reciprocal annex item with the stated identifier:
- thm:p15-laplace-relative-error / annex:p15.laplace-relative-error.
- thm:p15-laplace-mode-variants / annex:p15.laplace-mode-variants.
- thm:p15-laplace-curvature-replacement / annex:p15.laplace-curvature-replacement.
- thm:p15-bic-leading-order / annex:p15.bic-leading-order.
- thm:p15-laplace-normal-example / annex:p15.laplace-normal-example.
- thm:p15-direct-evidence-mc / annex:p15.direct-evidence-mc.
- thm:p15-importance-evidence / annex:p15.importance-evidence.
- thm:p15-harmonic-evidence / annex:p15.harmonic-evidence.
- thm:p15-evidence-mc-clt / annex:p15.evidence-mc-clt.
- thm:p15-mc-evidence-boundaries / annex:p15.mc-evidence-boundaries.

The Laplace result is an explicit handbook theorem, not an assertion that
the paper spells out all conditions. Fixed dimension, a fixed interior ball,
uniform positive Hessian eigenvalues, bounded C4 exponent and C2 amplitude
derivatives, positive bounded mode amplitude, local quadratic domination
and an exponentially small weighted outer tail are all stated.
The proof rescales at n^-1/2, expands on the symmetric n^(1/12) ball,
cancels the odd term, bounds the integrated remainder by O(n^-1), and
bounds both remaining tails. Gaussian integration is proved by successive
Schur-complement square completion and one-dimensional Gaussian integration.

Posterior- and likelihood-mode versions are distinct substitutions into
that theorem. The expected/observed information substitution is conditional
on an explicit symmetric-matrix norm bound; no universal Fisher-information
convergence rate is asserted. BIC is fixed-dimensional and retains its
bounded prior/determinant constant before discarding it. A relative-log
claim requires divergence of the exact log factor; bounded factors do not
satisfy that additional premise automatically.

The exact normal example has posterior-mode Laplace exact. For the MLE
version, bounded sample summaries verify every uniform hypothesis. At zero,
with sampling variance 1/n and prior variance 4, exact factor is
1/sqrt(1+4n), MLE factor 1/(2sqrt(n)), and BIC factor 1/sqrt(n);
the BIC relative ratio tends to two. Proper-prior Bernoulli likelihood
examples expose boundary, secondary-mode and zero-Hessian failures.

Monte Carlo identities assume proper prior Pi, finite nonnegative likelihood
L, and 0<I=integral L dPi<infinity. Direct prior simulation is unbiased.
Ordinary importance requires target-measure domination T<<Q; the source's
self-normalized form requires the stronger prior domination Pi<<Q.
Positive finite-sample denominators are not assumed automatically.
Generalized harmonic averages are unbiased for reciprocal evidence under
G<<T, and their inverses are consistent but generally biased.

Convergence uses the actual existing integrable strong law
thm:p15-etemadi-strong-law (i.i.d. is stronger than its pairwise premise).
Finite-variance normal limits use the read interfaces thm:p15-clt-iid and
thm:p15-clt-perturbation, with the exact second moments given for each
estimator. No general MCMC convergence theorem is asserted.

## Source corrections and evidence boundaries

The p.778 equation (6), as printed, lacks the factor two on prior-log
ordinates when forming twice the log ratio of equation (5). The active
manuscript derives and states both coefficients correctly.
The p.780 equation (12) is the average g/(L*pi), whose expectation is 1/I,
although its description calls it an unbiased estimate of I. The manuscript
states the reciprocal target explicitly and proves that inversion is generally
biased, with a two-point example. This is not a quotation of a corrected
historical formula.

Classic harmonic consistency requires L>0 prior-almost-everywhere.
When the positive-likelihood prior mass is s<1, its inverse limit is I/s.
A two-point rare-support example also separates ordinary importance from
self-normalization. A normal proposal with thin tails gives infinite
importance variance despite full support; a proper normal-prior example
gives infinite harmonic variance when prior variance is at least sampling
variance. A stationary identity chain has correct posterior marginals but
fails all the needed averaging conclusions. Thus stationary or approximately
posterior-distributed output is not promoted to independent sampling.

Separate computational-source developments still owed: one-step Newton
implementation and its general error analysis; adaptive Gaussian quadrature;
prior/posterior mixture iterative estimators; bridge-sampling optimization;
Laplace--Metropolis mode/curvature estimation; Savage--Dickey and latent-data
ratios; Metropolis/Gibbs ergodicity and weighted-likelihood-bootstrap error.
Reading their source summaries is not completing those methods. The current
chapter does not claim their results.

## Author handoff

The complete body and annex were read by the author after writing; symmetry,
zero-parameter positivity, mode-choice and reciprocal-target conditions
were made explicit. The source note and notation intake were also read.
This is authored mathematics and source checking, not independent admission.
No reviews, scanners, tests, builds or manuscript renders were run.
The research/PDF skills guided the primary reading; all source pages are
held locally, and no additional purchase or acquisition was needed.

