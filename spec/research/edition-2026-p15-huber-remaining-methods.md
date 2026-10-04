# Huber 1964: remaining methods and historical comparisons

## Source and extent

Peter J. Huber, Robust Estimation of a Location Parameter,
Annals of Mathematical Statistics 35(1), March 1964, 73–101.
DOI 10.1214/aoms/1177703732. Canonical key Huber1964RobustLocation.
Held original: source/references/huber-robust-location-1964/huber-1964.pdf.
29 journal pages, no cover; 2,835,541 bytes.
SHA256: 0BD9E67B4910EBD47CB0349F673CA6C25307A4035DBCF0E98EEAC567DD150AD4.
Original free journal URL:
https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-35/issue-1/Robust-Estimation-of-a-Location-Parameter/10.1214/aoms/1177703732.pdf

The full original was read in the preceding source assignment.
This block reread source images 05–08 (printed 77–80), 11–14
(printed 83–86), and 19–29 (printed 91–101), completely.
These contain the exact selected examples, Section 7 comparison,
all of Sections 9–12 and every cell/caption of Tables I–IV.
Images are held in tmp/pdfs/p15-huber-location-source/source-NN.png.
Physical image number plus 72 is printed page number.
No additional original has been acquired by association with its
citation in this paper.

## Files and ownership

Owned body: handbook/parts/p15/huber-remaining-methods.tex.
Owned annex: handbook/annex/p15/huber-remaining-methods.tex.
Notation intake: handbook/registry/symbols-intake-p15-huber-remaining-methods.csv.
During the authoring block, shared drivers and canonical records were
not edited. The later delegated production extension routes this
component as P15.52 and its endpoint successor as P15.53. The requested
build/review-2026-09-08-2130 snapshot remains untouched.
The research and PDF skills governed the source-reading and this
durable intake. A parallel table-reading attempt failed because
the agent thread limit was reached; all source reading was performed
locally. No independent review, scanner, test, build or manuscript
render was performed.

## Fifteen complete statement/proof pairs

Every body suffix below is prefixed thm:p15- and every annex suffix
is prefixed annex:p15.

| Source component | Body suffix | Annex suffix |
| --- | --- | --- |
| Section 4 mean and median | huber-mean-median | huber.mean.median |
| Section 4 capped quadratic, global deletion and formal derivative | huber-trimming-calculation | huber.trimming.calculation |
| Section 3 Lemma 5, reread with the examples | huber-smooth-stationary-limit | huber.smooth.stationary.limit |
| Section 7 median bias and indistinguishability | huber-exact-median-bias | huber.exact.median.bias |
| Section 9 actual vague domain and dense finite-information class | huber-cdf-domain | huber.cdf.domain |
| Section 9 cosine/normal/exponential construction | huber-cdf-construction | huber.cdf.construction |
| Section 9 cumulative variational proof and atomic joins | huber-cdf-saddlepoint | huber.cdf.saddlepoint |
| Section 10 log-scale prototype and both clipping regimes | huber-scale-model | huber.scale.model |
| Section 10 scale computation and zero-data cases | huber-scale-computation | huber.scale.computation |
| Section 10 normal gauging | huber-scale-gauging | huber.scale.gauging |
| Section 11 finite existence/uniqueness and iteration | huber-joint-finite | huber.joint.finite |
| Section 11 location variance under explicit regularity | huber-joint-regular-limit | huber.joint.regular.limit |
| Section 11 sharp bound behind Table IV | huber-joint-variance-bound | huber.joint.variance.bound |
| Section 12 projection and a sufficient smooth-root theorem | huber-mr-projection | huber.mr.projection |
| Section 12 distinct-pair median and variance comparisons | huber-pair-median | huber.pair.median |

## Historical numbers

Table I, printed 84–85: all 31 k rows from 0 through 3.0,
the two normal score moments, tuning fraction and all ten
contamination columns are retained in three readable panels.
Its k-zero row is the median limit, not an all-zero score equation.
The tuning fraction one in that row is an endpoint limit.
Every variance is for square-root-n times the estimate, at normal
scale one.

Table II, printed 92: all six epsilon/a/b/c rows are retained.
The construction also has an exact independently specified example
z = pi/6, with a about 0.77756015, c about 1.34677369,
epsilon about 0.0023297693, b about 2.18553979,
information about 0.96245777 and variance about 1.03900663.

Table III, printed 95: all five normal-gauging rows are retained,
including q-prime, S-infinity, unadjusted q and its tuning fraction.
At unadjusted q = 2 the derived values are epsilon about 0.02580420,
q-prime about 1.89734505 and S-infinity about 0.94867253.

Table IV, printed 99: all eleven k rows and six contamination columns
are retained, including the three greater-than-four entries.
The source says it obtained these numbers by linear interpolation
in Table I; they are historical rounded values, not newly certified
interval computations.

The unnumbered final-page tables are both retained: all ten
contamination values for the pair-median supremum, and all five
values comparing that estimator with Proposal 2 at k = 1.5 under
the scale-three normal contamination model.
Their exact integral/root formulas are supplied.
Exploratory iteration counts and the sample-size-5-and-10 variance
discussion retain the actual source populations/sample sizes;
the paper supplies no replication counts or uncertainty estimates
there, and none are invented.

## Corrections and qualifications

The capped quadratic is a residual-cutoff global minimization, not
fixed-fraction trimming. Removing saturated observations retains a
particular global minimizer; it need not preserve an arbitrary
selection convention. Its minimizing set can be disconnected.
The four-point example explicitly shows why taking the midpoint
of that nonconvex minimizing set is invalid.
The derivative calculation is proved. The paper's conditional
trimmed-variance conjecture remains identified as unproved in
that original; no claim about its present-day resolution is made.
The three-uniform counterexample refutes removal of the assumed
consistency premise, not the conditional conjecture itself.

The exact normal-contamination median bias is
Phi-inverse(1/[2(1-epsilon)]). The source's flat-core construction
gives a valid smaller lower bound and a first-order approximation,
not the exact median upper bound. The sharper indistinguishability
construction and its complete proof correct that statement.
The source sample-size discussion is interpreted as a specified
bias-to-standard-error comparison, not a prohibition on collecting
more data or a proof that contamination can be estimated.

The symmetric CDF identity uses a left limit at atoms.
Equal missing masses at the two infinities specify the actual
subprobability vague completion. Compactness and the finite-information
approximation are proved. The latter first mixes with the normal
to create slack and then smooths, instead of assuming smoothing
preserves the bound. The cosine construction's exact parameter
range ends at its unique a=b crossing; the source's approximate
0.03 description is not substituted for that range condition.
The variational proof retains the missing-mass term and uses the
average derivative at joined pieces to prove the proper symmetric
law's actual slope, including boundary atoms and the a=b endpoint.

The scale transformation requires X nonzero to give real log X-squared.
The algebraic equation is separately extended to zero observations,
with its root existence, flat intervals and failure cases proved.
Both c below one-half and c at least one-half have their actual
lower tangent and cap. On the one-sided branch, centering forces
closed-tail support, while the source's constant normal-limit
variance uses strict-tail support. Atoms exactly at the scale
threshold retain the one-sided slope qualification.

The joint finite-sample theorem states 0 < beta < k-squared:
the positivity omitted from a bare beta < k-squared extension is
necessary. The exact multiplicity condition and the source's
monotone-R proof are retained. A separate finite active-block
enumeration is proved; it is not misattributed as the historical
iteration. The latter can have undefined updates, and its finite
state count proves only termination or eventual periodicity when
all updates are defined. The source explicitly leaves cycling
unsettled. Proposal 3's adaptive minimax claim retains its
conjectural standing.

The joint asymptotic proof now supplies consistency, tightness,
uniform empirical control and the score expansion on a stated
regular domain. It requires no atoms at the population clipping
boundary and epsilon < 1-beta/k-squared. The finite sharp-variance
bound additionally requires epsilon < beta/k-squared.
The interpolation table is preserved with this justified domain.

The Mr proof supplies the required projection and its remainder
bound instead of assuming independent overlapping subsets.
It states sufficient smooth-root conditions explicitly.
The nonsmooth pair median receives a separate subset-CDF proof;
its source version uses i<j and omits diagonal pairs.
The density-contamination bound is equality at epsilon zero,
strict for each positive proper density contaminant, and sharp
as a supremum. The Gaussian-mixture comparison is fully reduced
to explicit integrals and one monotone scalar root.

## Completed endpoint follow-up and production integration

The joint boundary-atom implication is supplied in P15.53,
thm:p15-huber-joint-atomic-limit. Its exact directional map yields
the generally non-Gaussian joint law; thm:p15-huber-joint-law-and-variance
also proves the random limit of the proposed variance estimate.
The sharp source bound is extended to the variance of that limiting
law by thm:p15-huber-joint-atomic-bound.

The all-positive-scale-equivariant comparison permitting signs is
proved in thm:p15-huber-scale-sign-minimax, with the exact independent
fair-sign conditioning and finite information bound. The continuous
normal-mixture comparison is justified without a worst-contaminant
atom restriction by thm:p15-huber-zero-atom-mixture-bridge.
These three former source-scope gaps are closed by complete proofs.

The original conjectural claims and iteration-cycle question retain
their historical standing. Separate Hoeffding1948 and
Hodges–Lehmann1963 originals remain separate presentations, not
acquired through citation in Huber's paper.

The body and annex drivers now route this 15-pair component as P15.52
and the ten-pair endpoint component as P15.53. One combined 23-row
canonical-format symbols intake uses those scopes and meta precedence:
handbook/registry/symbols-intake-p15-huber-remaining-and-endpoints.csv.
It supersedes the two component intakes for canonical append; those
author intakes remain as provenance. Root owns the canonical append.
The reader pointers were updated in the same delegated production
extension. No review, scanner, test, build or manuscript rendering
was run.

## Author read-through

Completed one full read-through of the saved body, all fifteen proofs
and both intakes after the writing batch. Direct corrections make
the scale sampling/transform domain, candidate-partition rejection
conditions and the measurable kernel version explicit; these changed
passages were read afterward. Final fingerprints are supplied in the
handoff. This is authoring evidence, not independent admission.
