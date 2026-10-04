# Huber 1964: general prototype and information game

## Assignment and source

P15 / approved parent U6. The owned body and annex are
handbook/parts/p15/huber-information-game.tex and
handbook/annex/p15/huber-information-game.tex. The disjoint notation
intake is handbook/registry/symbols-intake-p15-huber-information-game.csv.
There are 12 reciprocal statement/proof pairs. Shared integration
and the parent's build/review-2026-09-08-2130 snapshot are outside scope.
No review, scanner, test, build or manuscript rendering was performed.

Peter J. Huber, “Robust Estimation of a Location Parameter,”
Annals of Mathematical Statistics 35(1), March 1964, 73–101.
DOI 10.1214/aoms/1177703732. Canonical key: Huber1964RobustLocation.
Held original: source/references/huber-robust-location-1964/huber-1964.pdf.
It has 29 journal pages without a cover and 2,835,541 bytes.
SHA256: 0BD9E67B4910EBD47CB0349F673CA6C25307A4035DBCF0E98EEAC567DD150AD4.

Verified original URL:
https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-35/issue-1/Robust-Estimation-of-a-Location-Parameter/10.1214/aoms/1177703732.pdf

The preceding block read the entire original. This block reread
physical pages 8–10 (printed 80–82), containing Section 5, and
physical pages 14–19 (printed 86–91), containing Section 8 and
surrounding qualifications. Source images are held under
tmp/pdfs/p15-huber-location-source/source-NN.png.
Physical page number plus 72 is printed page number.
The PDF skill supported source-page reading; the research skill
required this durable source and scope record. No new bibliography
record or primary capture is required.

## Source map and reciprocal proof map

Each body label below begins thm:p15-; each annex label begins annex:p15.

| Original scope | Body suffix | Annex suffix |
| --- | --- | --- |
| Section 8 measure domain and contamination closure | vague-subprobability-compactness | vague.subprobability.compactness |
| Section 8 Lemma 6, ratio scaling, Nature's mixtures | information-payoff-bridge | information.payoff.bridge |
| Section 8 Theorem 3, all finite-information regularity conclusions | finite-information-characterization | finite.information.characterization |
| Section 8 Theorem 4 existence, plus explicit minimax-value derivation | information-game-value | information.game.value |
| Correction to the general uniqueness conclusion | information-equality-components | information.equality.components |
| Section 8 Theorem 2 support-sensitive variation | information-first-variation | information.first.variation |
| Section 8 Theorem 2 efficient score and global extension | information-saddlepoint-criterion | information.saddlepoint.criterion |
| Section 8 Theorem 5 singular limits and statistical bridge | information-closure-extension | information.closure.extension |
| Section 5 Theorem 1 general prototype and normalization | huber-general-density | huber.general.density |
| Section 5 saddlepoint and exact centered statistical class | huber-general-minimax | huber.general.minimax |
| Logistic and asymmetric Gumbel calculations | huber-nonnormal-examples | huber.nonnormal.examples |
| Support-extension, ordinary-derivative and atomic failures | information-game-failures | information.game.failures |

The density-characterization proof supplies an editorial functional
derivation of all six source conclusions: density, boundedness,
continuity, absolute continuity, bounded variation and the Fisher
integral. It proves C1 test-function density, L2 completeness, the
bounded-functional representation and the cumulative signed-measure
argument. It is not attributed as a transcription of the source's
six-stage proof. No representation theorem is an unproved dependency.
The source's ratio-scaling and perspective-convexity route is retained
separately from the affine-game minimax proof. The latter uses a
finite cover and explicit Euclidean separation, without assuming
an infinite-dimensional minimax theorem.

## Exact corrections and premises

The domain is nonnegative Borel subprobabilities on the real line
with vague topology. Proper contamination is not vaguely closed:
its closure admits escaping contaminant mass. The zero measure and
zero-denominator payoffs are specified. For nonzero measures these
conventions preserve the source's positive-denominator supremum.

The first variation includes the information on newly occupied
support. If the efficient score has infinite second moment under a
finite-information competitor, the right derivative is minus infinity;
the proof does not hide a tail assumption. Equality in information
convexity means proportionality on each connected component of the
union of positive supports. Component weights may differ. A positive
everywhere minimizer is unique; compactness and convexity alone do
not imply uniqueness. The disjoint sine-squared example has value
4 pi squared at every mixture and demonstrates the independent
obligation on a score's extension to competing supports.

For singular laws a locally absolutely continuous score and a specified
bounded Borel weak-derivative representative define the extended
payoff. The source's C0 or nonnegative upper-semicontinuous
vanishing-at-infinity premises justify passage to singular limits.
The step-score example shows why the ordinary derivative zero almost
everywhere cannot replace its distributional point-mass derivative.

The prototype is a C2 density on the real line, positive on an
interval with convex negative log density there. Finite and infinite
tangent endpoints are included. Its clipped-score derivative can be
unbounded. The direct contamination proof therefore uses its
integrability and the proved boundedness of finite-information
densities; it does not invoke the separate abstract bounded-derivative
extension theorem without that premise.

The asymmetric statistical class fixes E_F psi_k = 0. Arbitrary
contamination does not preserve location zero automatically. The
all-equivariant risk is the active sup_F limit_C liminf_n truncated
risk. The proof gives a pointwise upper limsup bound first and never
interchanges the sample limit and supremum over laws. The epsilon-zero
endpoint retains the nominal information and normality hypotheses.
Root bracketing and bisection follow from proved monotonicity,
continuity and endpoint limits; no quadrature-error claim is made.

## Exact active dependencies

The body/annex use thm:p15-helly-selection and
thm:p15-stieltjes-construction, whose exact interfaces were read.
Missing subprobability mass is first placed at an escaping point;
the new proof converts the source interval convergence to vague
convergence. The statistical proof uses
thm:p15-convex-location-normality, thm:p15-clt-lindeberg-feller,
thm:p15-location-integrated-score-bound and the risk order in
def:p15-huber-symmetric-location-model. The disjoint-support example
from thm:p15-fisher-minimizer-nonuniqueness is explicitly recalculated
with the competing scores. Every additional functional, compactness,
semicontinuity and variational dependency is proved in the new annex.

## Completed subsequent source presentations

The Section 4 examples, full Table I, Section 7 bias comparison,
Section 9 CDF construction and Table II, Section 10 scale construction
and Table III, all three Section 11 proposals and Table IV, and
Section 12 subset/pair-median treatment are supplied in P15.52,
sec:p15-huber-remaining-methods. That chapter contains 15 reciprocal
theorem/proof pairs and preserves the source's actual conjectures.

P15.53, sec:p15-huber-joint-endpoints, supplies ten further pairs:
the exact identification condition, full directional and joint
clipping-atom law, its non-Gaussian consequences, the sharp bound,
the unrestricted continuous-mixture bridge and the all-sign
scale-equivariant minimax lower bound. These are completed proofs,
not pending promises attached to the earlier normal special case.

The delegated production extension routes both chapters in the body
and annex drivers. The combined canonical-format notation intake is
handbook/registry/symbols-intake-p15-huber-remaining-and-endpoints.csv;
root owns its append to the canonical registry. Later separate
influence-function and breakdown originals retain their own source
obligations.

## Author read-through and fingerprints

Completed one full author read-through of the saved body, all 12
annex proofs, this note and the notation intake. The cross moment in
the first-variation statement is now defined only on its proved
integrability domain, and the computation specifies both endpoints
of a possible flat sample-score zero interval. Convexity of the
saddlepoint model class and i.i.d. sampling for the estimator are
stated directly. Those corrections
were read directly afterward. The return supplies final hashes.
This is authoring evidence, not independent review or manuscript admission.
