# P15.45: Bounded concentration and finite-class learning

## Completed authoring

Thirteen complete statement/proof groups supply the common-range and
unequal-range concentration construction, the martingale extension,
all original first-theorem bound comparisons and Gaussian benchmarks,
and finite/countable-class learning and validation applications.
Parent scope: U5, with U1 probability and U4 confidence interfaces.

- handbook/parts/p15/bounded-concentration-learning.tex
- handbook/annex/p15/bounded-concentration-learning.tex

Chapter: sec:p15-bounded-concentration-learning.
Annex: sec:annex-p15-bounded-concentration-learning.

The integrated authoring snapshot:
body 17,298 bytes, SHA-256
D51C447C417F809FA1F5EC9872698A2662C56B838A07202A7E65651958613C42;
annex 23,756 bytes, SHA-256
40D6737C6AF2056BAA9F6FA86632C85CE6C8D9B63BF070428275BB151E7D4E41.
The body explicitly defines bar(X) at its benchmark use.

## Exact source and actual reading

Wassily Hoeffding, Probability Inequalities for Sums of Bounded Random
Variables, Journal of the American Statistical Association 58(301),
13-30, March 1963. DOI 10.1080/01621459.1963.10500830.
Canonical key: Hoeffding1963BoundedSums.

Held original:
source/references/hoeffding-bounded-sums-1963/hoeffding-1963.pdf.
Size: 1,451,039 bytes. SHA-256:
3021BCC097EF23A99A84D0EEF8DCCE2FD835C71DF79A105727D3E03F8F0B8930.
The nineteen physical pages contain one archive cover followed by the
eighteen original printed pages 13-30; printed page = physical page + 11.

University acquisition URL:
https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf

Publisher identity:
https://www.tandfonline.com/doi/abs/10.1080/01621459.1963.10500830

The repository also advertises a 1962 mimeographed report, but that was
not substituted for this journal original. The held scan is image-only;
its blank extracted text was not treated as equation evidence.
Root read all actual source pages 13-24 as images, including every
displayed formula and footnote in that extent. Source-reading images
are tmp/pdfs/p15-hoeffding-source/source-02.png through source-13.png.
The principal assigned passages are Theorems 1-2 and corollary on
pp. 15-16, the maximum/martingale claims on pp. 17-18, comparisons
(3.1)-(3.9) on pp. 18-19, and their complete proofs on pp. 20-23.
The adjacent Theorem3 material was read to coordinate its distinct
variance-sensitive author assignment, not counted as written here.

## Exact reciprocal proof map

Each suffix has thm:p15- and annex:p15. labels:

| Suffix | Complete content |
| --- | --- |
| conc-exponential | Convex chord, centered moment bound, sharp one-eighth coefficient, and exponential Markov inequality. |
| conc-common-range | All three bounds of source Theorem1, exact minimum coefficient g(p), endpoint/degenerate cases, and affine range change. |
| conc-common-comparison | Full source power series, both high-mean ratio bounds, reflected low-mean identity and inequality, and precise small-deviation ratio limit. |
| conc-unequal-ranges | Full Theorem2, squared ranges, signed weights, the exact two-sample corollary, and a separately justified paired-loss bound. |
| conc-martingale | Conditional moment bounds, Doob maximum argument, and the source's common-conditional-mean extension. |
| conc-benchmarks | Moment and one-sided variance bounds, Gaussian exponential moment and Mills squeeze, exact Lyapunov route for (2.15), sharp nonnegative Markov example and exponential-minus-one refinement. |
| conc-finite-learning | Simultaneous bounded-risk estimation, exact/approximate empirical minimization and simultaneous clipped confidence intervals. |
| conc-weighted-learning | Countable fixed-weight bound, penalized risk comparison and measurable approximate selection with attainment conditions. |
| conc-validation | Independence from the entire training object, conditional frozen-candidate bound and selection among K validation candidates. |
| conc-noisy-example | Four exact predictor risks, empirical tie, ordered sample probability and sufficient sample-size calculation. |
| conc-selection-example | Exact probability of finding a zero-training-error column among many equally inaccurate predictors. |
| conc-dependence-boundaries | Full fifteen-variable pairwise-independence counterexample and the finite-mean/growing-range obstruction. |
| conc-time-uniform | Countable allocation over all times, zero-width cases, simultaneous mean band and finite data-dependent stopping. |

## Important mathematical and interpretation decisions

The common-range theorem retains all three source inequalities, not only
the simple quadratic exponent. The full first-theorem comparison also
keeps the p<1/2 and p>=1/2 regimes distinct. Its reflected argument
t'=1-2p-t can be negative, so the divergence numerator is explicitly
defined on -p<t<1-p before using the reflection identity.

The centered moment proof retains the square of each interval width.
This corrects the missing width square in the source's intermediate
printed (4.17), consistently with its (4.16), stated Theorem2 and
following minimizer. Zero-width variables are handled separately rather
than divided by. Bounds above one are not treated as impossible values
of probability; they are capped at one where useful.

Mutual independence, conditional martingale centering and pairwise
independence are distinct. The actual fifteen-variable finite-field
counterexample disproves the unsupported pairwise replacement. The
source's common-range martingale extension uses deterministic conditional
means and therefore obtains the same product bound by iteration.

The exact source normal-limit hypotheses are mapped to the existing
thm:p15-clt-lyapunov with exponent parameter one. The extra variance
divergence condition in the source benchmark is retained; no assertion
that normalized Lyapunov convergence itself requires it is made.
The source's moment comparison uses the existing exact Cantelli theorem.

The learning statements are explicit editorial applications. No target
with zero risk is assumed, and losses for different candidates on the
same record need not be independent. The finite class and countable
weights are fixed before observing the sample. An arbitrary countable
infimum is not claimed effectively computable or always attained.

Validation is proved by integrating over an independent training object;
no pointwise conditional probability on an exceptional null event is
needed. The all-time result allocates delta/[n(n+1)] across observation
times. It is not inferred by repeatedly reusing a one-time confidence
statement. Predictive probabilities, posterior probabilities and sampling
coverage remain different operations throughout.

## Integration and continuation

Body, annex, canonical source key and P15.45 symbol roles are integrated.
Root read the complete saved body and annex as one authoring batch,
then read the added source-comparison and benchmark groups and completed
their local definitions. This was writing and integration, not an
independent review. No scanner, test, manuscript build, manuscript
render or admission check ran.

The complementary author returned fourteen complete pairs for Theorem 3,
the second family of comparison ratios, dependent mixtures/U statistics
and sampling without replacement in variance-and-dependent-concentration.tex.
That body and annex are now integrated, with an exact combined source map
in edition-2026-p15-variance-and-dependent-concentration.md. The complete
1963 source standing is recorded across both notes; this note alone does
not claim its whole article.
Modern uniform complexity, VC/Rademacher methods, general loss classes,
robust inference and further U5/U6 source presentations remain in the
approved manuscript objective.
