# Huber joint endpoints and the sign-information bridge

## Source and assignment

Peter J. Huber, Robust Estimation of a Location Parameter,
Annals of Mathematical Statistics 35(1), March 1964, 73–101.
DOI 10.1214/aoms/1177703732. Canonical key Huber1964RobustLocation.
Held PDF: source/references/huber-robust-location-1964/huber-1964.pdf.
29 journal pages without a cover; 2,835,541 bytes.
SHA256: 0BD9E67B4910EBD47CB0349F673CA6C25307A4035DBCF0E98EEAC567DD150AD4.
Original free URL:
https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-35/issue-1/Robust-Estimation-of-a-Location-Parameter/10.1214/aoms/1177703732.pdf

The complete original was read previously. This block rereads printed
94–95 and 97–100, covering the scale-equivariant claim and the exact
joint equations, iteration and variance discussion. Source images
are source-22.png, source-23.png and source-25.png through source-28.png
under tmp/pdfs/p15-huber-location-source/.
The research and PDF skills support the source note and direct
primary reading. A parallel source-reading request failed at the
agent thread limit; all reading and writing proceeded locally.

Owned files: handbook/parts/p15/huber-joint-endpoints.tex,
handbook/annex/p15/huber-joint-endpoints.tex,
handbook/registry/symbols-intake-p15-huber-joint-endpoints.csv,
and this note. Shared files were untouched during authoring. The later delegated
production extension is recorded below; review snapshots remain untouched.

## Ten reciprocal proof pairs

Body suffixes have prefix thm:p15-; annex suffixes have prefix annex:p15.

| Obligation | Body suffix | Annex suffix |
| --- | --- | --- |
| Exact identification and eventual unique estimation | huber-joint-identified | huber.joint.identified |
| Complete directional derivative at clipping atoms | huber-joint-directional | huber.joint.directional |
| Strong monotonicity and four inverse pieces | huber-joint-cone-inverse | huber.joint.cone.inverse |
| Root rate, local empirical expansion and joint limit | huber-joint-atomic-limit | huber.joint.atomic.limit |
| Gaussian case, non-Gaussian density, risk and variance estimate | huber-joint-law-and-variance | huber.joint.law.variance |
| Calculated four-point law | huber-joint-worked-atomic-law | huber.joint.worked.atomic.law |
| Original-model non-Gaussian location counterexample | huber-joint-normal-contamination-counterexample | huber.joint.normal.contamination.counterexample |
| Sharp Table IV upper bound including atoms | huber-joint-atomic-bound | huber.joint.atomic.bound |
| Zero-atom normal-mixture bridge | huber-zero-atom-mixture-bridge | huber.zero.atom.mixture.bridge |
| Full scale-equivariant comparison allowing signs | huber-scale-sign-minimax | huber.scale.sign.minimax |

## Mathematical completion and correction scope

The equations are the original clipped-score joint equations.
Their convex perspective criterion is centered before taking
population expectation, so no first observation moment is assumed.
The exact centered-scale identification condition is
F{0} < 1-beta/k-squared. Restricted interior curvature proves
population uniqueness, eventual unique sample roots, measurability,
almost-sure consistency and the root-n rate. The stronger
finite-sample maximum-multiplicity condition is not used as a
necessary population condition.

Each clipping atom has mass p and contributes its actual positive-part
directional term. The full limit is the inverse of the resulting
strongly monotone map applied to a Gaussian vector. Uniform local
empirical expansions, the needed bivariate Gaussian limit, inverse
existence and the four piecewise formulas are all proved.
No no-atom or ordinary-differentiability premise remains in this
joint limit. A zero second Gaussian variance is explicitly allowed
in the no-clipping-atom case.

When p is positive the joint law is non-Gaussian, and the proposed
strict-interior variance estimate has a nonconstant three-value
limit. The location marginal can also fail to be Gaussian: the
proof compares its Gaussian tail rate with its smaller second
moment. The original-model example is
0.998 Phi + 0.001 delta(-q) + 0.001 delta(q), with k=1,
beta=B(1) and the displayed exact equation for q.
Calculated q is about 1.00244151, A about 0.68250186, and C about
0.19856041. These are formula evaluations, not simulation evidence.

The separate four-point example uses equally weighted values
-1, -1/2, 1/2, 1 at k=1 and beta=5/8. Its full inverse law is
given by arithmetic branches. Its variance is 1.832700020...
from an exact trigonometric integral. The variance-estimate
limits are 5/2, 10/9 and 5/8.

The source's sharp Table IV bound remains true for the variance
of the possibly non-Gaussian limiting location law. Strict-tail
contaminants attain it. The law-specific statement retains exact
identification; the whole symmetric-contaminant class is identified
when epsilon < 1-beta/k-squared. A finite maximal cutoff separately
requires epsilon < beta/k-squared. The source's universal normal
interpretation is corrected directly by the actual limiting law.

At the identification equality, the text supplies both a continuum
of scales and a no-positive-scale example. The original adaptive
minimax conjecture and iteration-cycle question retain their
historical standing; neither is claimed solved by this limit theorem.

## Signs and the original estimator class

All finite positive measurable scale-equivariant estimators on
nonzero observation vectors are compared; they may use all signs.
The original strict-tail model assigns that domain probability one.
Positive equivariance at the all-zero vector is impossible.
The explicit least-favorable original density has a normal core
and power tails of exponent q-squared.
Its independent fair signs are independent of its log-squared
observations. Conditional on each fixed sign pattern, the actual
original estimator is a deterministic translation-equivariant
function of those transformed observations.

The existing finite-n, finite-truncation information lower bound
applies to every such conditional function; averaging the actual
sign probabilities gives the same lower bound for the original
estimator. No decision is averaged, no artificial randomization is
introduced, and no Jensen inequality for truncated loss is used.
The proof preserves liminf in n, then increasing truncation, then
the law supremum. Scale equivariance removes the scale parameter
pathwise. The source magnitude estimator attains the value on
the whole strict-tail class, including contaminants whose signs
and magnitudes are dependent away from the least-favorable law.

## Mixture bridge and integration

Every symmetric non-atomic law has zero mass both at zero and at
its clipping points. The new identification and Gaussian-case
theorems therefore justify the normal/scale-three-normal comparison
for all mixture fractions from zero to one. The sufficient
worst-contaminant atom bound is not needed for this family.

The delegated production extension routes this chapter as P15.53
after huber-remaining-methods at P15.52 in both drivers.
Predecessor reader pointers now reach
thm:p15-huber-joint-atomic-limit, thm:p15-huber-joint-law-and-variance
and thm:p15-huber-joint-atomic-bound; the sign bridge is
thm:p15-huber-scale-sign-minimax and the mixture bridge is
thm:p15-huber-zero-atom-mixture-bridge.
All three assigned open implications have complete proofs here.

The canonical-format combined intake is
handbook/registry/symbols-intake-p15-huber-remaining-and-endpoints.csv,
with 23 rows under P15.52/P15.53 and meta precedence. Local
section/annex scopes are retained in its notes. Root owns the
append to symbols.csv; this extension did not edit that canonical file,
the bibliography, shared progress or any review snapshot.

## Authoring evidence

Completed one author read-through of the saved body, all ten annex
proofs and both intakes. Direct corrections define local proof
variables before use, distinguish fixed and varying cutoffs, and
make the measurable exceptional extension explicit. Those changed
passages were read afterward. Final hashes are returned at handoff.
No independent review, scanner, test, build or manuscript rendering
was run. Authoring completion does not constitute publication admission.
