# P15.34 — Bernstein approximation, Hausdorff moments and exchangeability

## Frozen source and completed writing

This treatment supplies the complete mathematical presentation in
Feller, Probability Theory and Its Applications, Volume II, second
edition (1971), Chapter VII, Sections 1–4, printed pp. 219–230.
The held copy is an undated Mei Ya/Taipei reprint of that edition.
No unsupported printing year is assigned.

Held original:
source/references/feller-probability-volume2-second-edition/feller-volume2-second-edition.pdf

SHA-256:
CB87C933D4175234F5F5958A74F3A466ECF13C29BE4E0DFEDF9C9B739F717486

The file has 683 physical pages and 44,136,265 bytes. Its hash was
verified during this authoring continuation. The canonical bibliography
key is Feller1971ProbabilityII; no new entry is required.

Owned files:

- handbook/parts/p15/feller-bernstein-hausdorff.tex
- handbook/annex/p15/feller-bernstein-hausdorff.tex
- spec/research/edition-2026-p15-feller-bernstein-hausdorff.md

The saved body contains 19,842 bytes, SHA-256
40490EC393E7FC46B472F204CA454243280D530F75BADBFD94031EBA6516EB93.
The saved annex contains 35,334 bytes, SHA-256
E443D0F0EBF46D42FBC5FA7A0933CE2DC37FB1266E6916ECEBD1AA4E72FE329E.
These identify the final authoring batch before later manuscript editing.
Sixteen reciprocal formal statement/proof pairs are supplied.

## Primary reading

The complete printed pp. 219–230 were read, including continued proofs,
formulas, examples and footnotes. In this extent physical page numbers
equal printed page numbers plus 15. This is a local mapping: physical
p. 233 is printed p. 217, so the offset is not asserted globally.

Original page images for printed pp. 220, 223, 224, 226 and 230 were
personally read to resolve the kernel variance, finite-difference
exponents, positive-series/grid argument, ramp construction and
exchangeability examples. They are retained under
tmp/pdfs/p15-feller-moments-source/. Those images are primary-source
reading aids. They are not manuscript renders.

Section VII.5 and the start of VII.6 through printed p. 232 were read
as leads for the next source treatment. Their complete transform and
moment proofs are not claimed in this chapter.

Existing actual manuscript interfaces were read for Stieltjes measure
construction, compact moment determinacy, the analytic/Carleman
criteria, beta/gamma integration, the central limit theorem and the
standard-Borel directing-law result. The present Feller construction
does not replace his moment route with the earlier reverse-martingale
proof of de Finetti's theorem.

## Reciprocal inventory

Every suffix below has body label thm:p15-SUFFIX and annex label
annex:p15.SUFFIX.

| Suffix | Supplied result |
| --- | --- |
| feller-concentration | Chebyshev concentration approximation, pointwise and compact uniform forms, and the unbounded-parameter hypothesis. |
| feller-kernel-examples | Binomial, Poisson and gamma kernels, affine approximation and the finite-variance independent common-law plug-in. |
| feller-differences | Finite differences, normalized differences, the full reciprocity identity, inversion and shifted/polynomial specializations. |
| feller-bernstein | Both Bernstein representations, uniform approximation and quantitative modulus/Lipschitz estimates. |
| feller-positive-series | Coefficient extraction and positive-series closure, compact convergence and endpoint mass behavior. |
| feller-absolute-monotone | Equivalence of positive power series, all nonnegative derivatives and the source's exact normalized-grid criterion. |
| feller-hausdorff-weights | Complete monotonicity of moment sequences, normalized discrete Hausdorff weights and polynomial expectation limits. |
| feller-ramp-measure | Continuous positive functional, the explicit ramp CDF, right continuity, measure construction and continuity-point squeeze. |
| feller-hausdorff | Moment existence, uniqueness and inversion on [0,1], both endpoint atoms and finite-mass normalization. |
| feller-moment-calculations | Uniform, endpoint-mixture and point-mass reconstructions, affine support changes and the insufficient finite-prefix counterexample. |
| feller-lognormal-moments | Full lognormal family with identical moments and the power-series sufficient determinacy criterion. |
| feller-binary-mixture | Binary exchangeability from the finite-difference recurrence and Hausdorff moments, including every word and count probability and the converse. |
| feller-polya-moments | The source's beta identification from all-success Pólya moments and the complete word/count mixture. |
| feller-finite-alphabet | Finite-alphabet mixing on the simplex, empirical recovery and uniqueness, with the explicit existing directing-law bridge. |
| feller-finite-exchangeability | The occupancy counterexample and the residual-vector obstruction for every nondegenerate real input law and n at least 3. |
| feller-approximation-boundaries | Concrete failures without bounded tests, uniform continuity, order-zero positivity or valid normalization. |

## Preserved proof routes

The concentration argument splits the expectation at a fixed distance
from the mean, then applies Chebyshev to the outside term. Compact
uniform approximation uses a common modulus and uniform variance
control. Uniform variance on an unbounded parameter set does not by
itself yield uniform approximation for every bounded continuous test.

The reciprocity identity is proved by finite binomial expansion,
including order zero and the relevant shifted indices. Its polynomial
specialization yields the second Bernstein representation and the
Hausdorff expectation identity. The binomial representation gives the
approximation estimate directly.

The positive-series lemma uses coefficient subsequences and uniform
tail bounds at a larger argument. Uniqueness then identifies all
coefficient limits. Endpoint normalization is handled separately;
the sequence x to the n demonstrates why compact convergence inside
[0,1) can lose total mass at x=1.

The absolute-monotonicity result retains the source's original
condition Delta_(1/n)^k u(0) >= 0 for k<n. For fixed 0<a<1, set
m_N=floor(aN)<N and use the Bernstein polynomial of the grid values
u(j/N), j=0,...,m_N. Its coefficient of x^r is
binomial(m_N,r) N^(-r) Delta_(1/N)^r u(0), hence nonnegative.
Its coefficient sum is u(m_N/N), uniformly bounded, and concentration
gives uniform convergence to u(ax). Positive-series closure supplies
the local series. Rescaling on a common smaller interval identifies
the coefficients, and a increasing to 1 completes the argument.
This proof neither adds a missing highest-order grid assumption nor
divides by a potentially zero value of u.

For Hausdorff existence, normalized positive weights define discrete
laws. Polynomial approximation makes their expectations Cauchy on
all continuous functions. The resulting positive functional L is
applied to continuous descending ramps. The infimum of those ramp
values defines F. Right continuity follows from the fixed-ramp
Lipschitz bound before invoking the already proved Stieltjes measure
construction. The lower and upper ramp bounds yield convergence at
continuity points of F.

All positive integer moments, including the first, follow from the
layer-cake identity
integral x^r dmu = 1-r integral_0^1 t^(r-1) F(t) dt.
Dominated convergence handles the countable set of CDF jumps.
Polynomial approximation and ramps give uniqueness. The construction
retains the source's ramp argument rather than replacing it with a
functional-representation or subsequence-selection theorem.

The binary exchangeability recurrence gives complete monotonicity
of all-success probabilities. Hausdorff's theorem then yields the
mixing law and every ordered word probability. The converse uses
uniform thresholds conditional on the directing parameter. The Pólya
application identifies the same mixing law through beta moments.
The finite-alphabet generalization identifies the precise
standard-Borel directing-law bridge already proved in the manuscript;
it does not claim that the source supplied an unprinted multivariate
moment proof.

## Corrections incorporated in the actual manuscript

The gamma kernel with shape n and rate n/theta has variance
theta squared divided by n. The source's printed theta/n variance
is not used. Shape n can be any positive real number. At theta=0
the kernel is explicitly the point mass at zero.

In the moment identity the factor is x^k (1-x)^r. The source's
equation (3.3) prints an incorrect exponent r-k. All subsequent
weights and differences use the corrected exponent.

The normalized-grid theorem is proved under k<n exactly as stated.
The source's bounded-endpoint step does not justify the order n
difference, and a later rescaling of the grid condition is not
automatic. The grid construction described above supplies that
missing argument under the original hypothesis. The zero function
is included without division.

The ramp expression is U_epsilon(t)=L(u_(t,epsilon)); the source's
undefined expectation subscript does not introduce an extra measure.
The CDF can have mass at zero. The proof establishes F(t)=0 for t<0
and F(t)=1 for t>=1, with F(0) allowed to be positive. Both endpoint
atoms are recovered:
mu({1})=lim c_n and mu({0})=lim (-1)^n Delta^n c_0.

The inverse weighted-CDF formula is asserted only at continuity
points. For a point mass at an interior t_0, the approximating
binomial CDF at t_0 tends to one half while the target CDF there
equals one. This is a worked warning about the exact inversion
hypothesis, not an exception to moment determinacy.

The prefix (1,1/2,1/10) passes all complete-monotonicity differences
available within that prefix, but cannot be a probability moment
prefix: its variance would be -3/20. The infinite-sequence theorem
is not promoted to an arbitrary finite-prefix existence theorem.

The lognormal density family f_a(x)=f(x)(1+a sin(2 pi log x)),
-1<=a<=1, is normalized and nonnegative, and all integer moments
are exp(k squared/2). The zero sine integral is proved by shifting
the centered Gaussian variable by the integer k and using oddness.
Distinct laws are identified on a specified interval.

The finite exchangeability examples include exact scope conditions.
For three cells and two balls under the uniform occupancy law,
the all-success sequence is (1,1/2,1/6,0,0,...), whose later
fourth difference has the wrong sign. No infinite binary extension
or independent identical mixture follows from finite symmetry.

For residuals Y_j=Z_j-bar(Z), j=1,...,n-1, the absence of an
independent identical mixture is proved for n>=3 and every
nondegenerate real input law, without any moment assumption.
Writing q_mu(t) for a component characteristic function and
c(t)=|phi_Z(t)| squared, the two identities are

- integral |q_mu(t)| squared dLambda = c(t), from Y_1-Y_2;
- integral q_mu(t)^(n-2) q_mu(2t) dLambda = c(t), from
  Y_1+...+Y_(n-2)+2Y_(n-1).

For n=3, Cauchy–Schwarz and halving force c(t)=1 near zero.
For n>=4, equality in the modulus bound forces the component
characteristic functions to have modulus one, first on a common
countable rational set and then everywhere by continuity. Both
arguments force a degenerate input. The elementary
characteristic-function degeneracy implication is proved explicitly.
The finite-variance negative-covariance formula is an additional
calculation, not a hidden premise. The n=2 and degenerate-input
exceptions are stated.

Concrete approximation counterexamples retain exact quantifiers:
vanishing variance with an unbounded fourth-power test; bounded
continuous narrow bumps with uniformly vanishing variance but no
uniform approximation over the whole unbounded parameter set;
missing order-zero positivity; and a positive series of infinite
total mass that cannot be normalized as a probability generating
function.

## Notation intake

- Parameter theta, kernel laws F_(n,theta), means, variances
  v_(n,theta), tests u, modulus omega_u and Lipschitz constant L.
- Binomial coefficients with zero conventions, Bernstein B_n u,
  forward difference Delta, normalized Delta_h and grid m_N.
- Positive coefficients a_r, approximating coefficients a_(n,r),
  series radius/arguments, total mass and compact tail bounds.
- Moment sequence c_k, complete-monotonicity indices k,r,
  weights w_(n,j), discrete expectations E_n, functional L,
  ramps u_(t,epsilon), U_epsilon, CDF F and measure mu.
- Interior point t_0, endpoint mixture weight a, affine interval
  [a,b], lognormal perturbation parameter a and even moments m_(2n).
- Binary word probabilities p_(k,n), all-success moments c_k,
  directing parameter Theta and mixing measure lambda.
- Pólya initial masses b,r, reinforcement c, beta parameters
  alpha,beta, rising factorials and simplex Delta_d.
- Independent input Z_j, sample mean bar(Z), residual Y_j,
  component law mu, mixing law Lambda, transforms q_mu, phi
  and c(t), with independent-copy variables in the degeneracy proof.

Every overloaded letter is locally declared. In particular L is a
Lipschitz constant in the approximation estimate and later a positive
functional; c is reinforcement in the urn and later c(t) is a real
characteristic-function modulus squared.

## Author completion and retained source obligations

The complete saved body and annex were read once as an authoring
batch. The final domain, normalization, reciprocal-series and
residual-scope corrections were then applied. The final file hashes
above were read back. A duplicate attempted application of that
already applied correction patch was rejected at its first hunk;
the saved final files and hashes were unchanged.

The Chapter VII Sections 1–4 mathematical scope is supplied.
Later Feller transform proofs, the later distinct proof associated
with the source's moment condition, the quantitative
Diaconis–Freedman presentation and the original general-space
counterexamples retain their separate source obligations.

The research and PDF skills guided exact primary reading and source
provenance. No independent review, manuscript scanner, test, build,
manuscript render or admission procedure ran. All remaining
manuscript changes precede the consolidated reviews.
