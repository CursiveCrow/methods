# P15.37 — The complete weak-convergence exercise list

## Completed authoring

The treatment supplies the eight remaining exercises in Durrett
Section 3.2, together with their required geometric, metric and
moment premises. Ten new statement/proof pairs are saved and routed.
The nine already supplied exercises retain their existing proofs
and have explicit links in the new chapter. Together these routes
cover all seventeen actual exercises.

Files:

- handbook/parts/p15/weak-convergence-exercises.tex
- handbook/annex/p15/weak-convergence-exercises.tex
- spec/research/edition-2026-p15-weak-convergence-exercises.md

Body: 14,189 bytes, SHA-256
7CA98A8857FABCE57516012D045EE5F25ED701760295A908F9D6E770F5F88264.

Annex: 19,955 bytes, SHA-256
3104371B365AD4EF5A1F912F62FF4ACAA006DF7C37A3063C5B354812EE83EB99.

Chapter label: sec:p15-weak-convergence-exercises.
Annex label: sec:annex-p15-weak-convergence-exercises.

The original author saved both drafts before the account usage
limit stopped its turn. Root resumed locally, read both complete
actual LaTeX files, read the whole primary exercise list and
the existing statement interfaces, supplied a direct total-variation
calculation, and completed notation, indexing, routing and this
source record. No independent review was performed.

## Primary source

Rick Durrett, Probability: Theory and Examples, author Version 5,
dated 2019-01-11. The exact target is Exercises 3.2.1–3.2.17,
printed pp. 123–125, physical pp. 131–133 of the held PDF.
The complete exercise list, every subpart and the actual transition
to Section 3.3 were read during root's continuation.

Held original:
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf

SHA-256 verified in the current continuation:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.

Canonical bibliography key: DurrettPTEAuthor2019.
No new bibliography entry or primary acquisition is required.

The source's Gaussian maximum exercise refers to its Theorem
1.2.6 tail estimate; its complete existing counterpart is
thm:p15-stirling-tail-premises. The bounded-distance comparison
refers to Exercise 2.3.6; the needed metric and convergence
premise is explicitly proved in the present annex.

## All seventeen exercise locations

| Exercise | Actual requested content | Supplied location |
| --- | --- | --- |
| 3.2.1 | Weak convergence of densities with failure of pointwise density convergence everywhere on [0,1]. | thm:p15-wce-dyadic-densities; annex:p15.wce-dyadic-densities. |
| 3.2.2 | All three independent-maximum limits, including their supports and normalizations. | thm:p15-wce-extreme-maxima; annex:p15.wce-extreme-maxima. |
| 3.2.3 | Gaussian tail ratio, quantile-centered maximum law and square-root-log first-order scale. | thm:p15-wce-normal-maxima; annex:p15.wce-normal-maxima. |
| 3.2.4 | Weak Fatou for a nonnegative continuous function. | thm:p15-criteria-weak-integration; annex:p15.criteria-weak-integration. |
| 3.2.5 | Unbounded integration under a dominating continuous moment function and a vanishing tail ratio. | thm:p15-criteria-weak-integration; annex:p15.criteria-weak-integration. |
| 3.2.6 | Levy metric and its equivalence to weak convergence. | thm:p15-weak-metric-premises; annex:p15.weak-metric-premises. |
| 3.2.7 | Ky Fan metric and the corresponding bound on Levy distance. | thm:p15-weak-metric-premises; annex:p15.weak-metric-premises. |
| 3.2.8 | Both exact comparisons between Ky Fan and bounded expectation distance. | thm:p15-wce-bounded-distance; annex:p15.wce-bounded-distance. |
| 3.2.9 | Uniform CDF convergence when the limiting CDF is continuous. | thm:p15-continuous-cdf-uniform; annex:p15.continuous-cdf-uniform, in strong-law-applications.tex. |
| 3.2.10 | Finite atomic approximation of an arbitrary probability CDF. | thm:p15-criteria-weak-integration; annex:p15.criteria-weak-integration. |
| 3.2.11 | Equivalence between weak convergence and every integer point mass converging to the given integer law. | thm:p15-wce-integer-laws; annex:p15.wce-integer-laws. |
| 3.2.12 | Probability convergence implies weak convergence; weak convergence to a constant implies probability convergence. | thm:p15-weak-metric-premises; annex:p15.weak-metric-premises. |
| 3.2.13 | Converging-together sum and its residual consequence. | The constant-limit bridge in weak-metric-premises followed by thm:p15-clt-perturbation and annex:p15.clt-perturbation. Use Y_n-c, or Z_n-X_n, as the residual. |
| 3.2.14 | Product with a variable converging to a constant, including the source's unrestricted sign extension. | The same constant-limit bridge and clt-perturbation with A_n=Y_n and B_n=0. |
| 3.2.15 | First coordinate of the uniform surface law on the radius sqrt(n) sphere. | thm:p15-wce-spherical-area and thm:p15-wce-sphere-coordinate, with their reciprocal annex items. |
| 3.2.16 | Two distinct positive moments tending to one force probability convergence to one for nonnegative variables. | thm:p15-wce-moment-concentration; annex:p15.wce-moment-concentration. |
| 3.2.17 | A uniform positive tail bound under second- and fourth-moment conditions for every y<1 and finite K. | thm:p15-wce-fourth-moment; annex:p15.wce-fourth-moment. |

The tenth new proof group, thm:p15-wce-boundaries with
annex:p15.wce-boundaries, supplies explicit counterexamples
for the independence, lattice, normalization, nonnegativity,
distinct-moment and common-fourth-moment hypotheses.
It is additional explanatory material, not an eighteenth exercise.

## Geometric premise supplied in full

Uniform surface probability is first defined geometrically,
before a Gaussian representation is introduced. Cone volumes
define a Borel probability on the unit sphere. Radial-shell
volume derivatives give the surface-area measure at each
positive radius and its exact total area.

The annex proves translation and scalar-dilation identities
from half-open rectangles and sigma-finite measure uniqueness.
It proves orthogonal invariance by first showing that any
translation-invariant Borel measure finite on bounded sets
is a constant multiple of product Lebesgue measure, then
normalizing that constant on the invariant unit ball.

Radial slabs identify the polar product measure on generating
rectangles. Monotone approximation gives the complete
nonnegative polar integration formula and then the integrable
signed version. Gaussian normalization and the gamma recurrence
give the exact ball-volume and area constants.

Only after this construction does the radial Gaussian density
identify the normalized direction with the prescribed surface
law, and prove its independence from the radius. The common
infinite Gaussian product and the integrable strong law supply
the coordinate limit. The zero-radius event and the
one-dimensional two-point sphere are handled explicitly.
The same representation yields the finite-n second and fourth
coordinate moments.

This is a construction for Euclidean spheres. It does not
assert a general surface-integration or manifold
change-of-variables theorem.

## Calculations and precise boundary conditions

- The dyadic density example has CDF error exactly 2^(-n-1),
  density L1 distance one and total-variation distance one half.
  The distance is proved directly using the positive and negative
  density differences and the event E_n. Endpoint density values
  are assigned so the requested pointwise failure includes both
  endpoints.
- All three extreme-value limits have full CDFs, support cases,
  normalization and finite maximum quantiles. The formulas are
  used only when their finite thresholds are within support.
- The Gaussian centering b_n is a positive finite solution only
  for n>=3. The source's n=1 tail equation has no finite solution,
  and n=2 gives zero. The full asymptotic argument uses precisely
  the eventual positive sequence and includes the second-order
  log-log correction.
- The bounded metric is defined modulo almost-sure equality;
  its triangle inequality and convergence equivalence are proved.
  Both source inequalities use the attained Ky Fan infimum.
  The lower bound is attained and the upper bound approached by
  explicit finite-valued variables, including a=0 and a=1.
- Integer mass convergence uses a specified limiting law whose
  masses sum to one. The full finite-set tail argument gives
  L1 and total-variation convergence. Escape of mass to integer
  infinity does not satisfy that normalization.
- The convexity-gap proof for arbitrary 0<alpha<beta does not
  require independence or a finite first moment. Moment
  finiteness is invoked only at the sufficiently large indices
  where convergence to the finite limiting moments guarantees it.
- The fourth-moment inequality gives (1-y^2)^2/K for
  0<=y<1. Negative y gives probability one. K<1 is an
  impossible input under the unit second moment, and y=1 is
  excluded by an explicit strict-tail counterexample.

## Notation intake

- M_n, F, phi, Phi, bar(Phi), alpha, beta, H_alpha,
  H_beta^-, G, u, b_n, theta: maximum laws, normal tails,
  local shape parameters, quantile level and Gaussian
  normalization/shift variables.
- E_n, f_n, ell, F_n, total-variation distance: dyadic
  half-cells, densities, cell length and corresponding CDFs.
- alpha(X,Y), beta(X,Y), a, D, h(t): Ky Fan metric,
  bounded metric, attained distance, absolute difference
  and bounded increasing transform.
- lambda_d, B_d, S^(d-1), v_d, O, C(A), sigma_d,
  area_r, pi: product volume, ball/sphere, orthogonal map,
  cones, sphere probability, radial-shell area and projection.
- X^(n), Y_j, D_n, Z^(n), R, U: surface vector,
  independent Gaussian sequence, empirical squared norm,
  coupled vector, radius and direction.
- Y_n, alpha, beta, p, D(z), c_epsilon, K, y:
  moment-concentration variables, exponent ratio, convexity
  gap, deviation constant and fourth-moment tail parameters.

Repeated letters are local to their declared sections.
In particular D is an absolute difference in the metric
proof and D(z) is a deterministic convexity-gap function
in the moment proof.

## Remaining manuscript work

The exact seventeen-exercise list is supplied. The broader
extreme-value domain-of-attraction classification mentioned
after source Exercise 3.2.2 remains a separate original
Gnedenko/Resnick presentation. The three explicit model
limits are not promoted into that classification.

The research and PDF skills supported exact source reading.
No independent review, test, scanner, manuscript build,
manuscript render or admission procedure ran. The governing
sequence remains all manuscript changes before consolidated
reviews.
