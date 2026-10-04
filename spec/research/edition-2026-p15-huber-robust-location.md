# P15-U6: Huber's original known-scale location construction

9 September 2026. Author block began 04:01:56 UTC; deadline 04:46:56 UTC.
Owned body/annex: handbook/parts/p15/huber-robust-location.tex and
handbook/annex/p15/huber-robust-location.tex, this note, disjoint bibliography
and notation intakes, and source/references/huber-robust-location-1964/.
Root owns shared drivers, canonical bibliography and notation.

## Verified primary and full reading

Peter J. Huber, Robust Estimation of a Location Parameter,
The Annals of Mathematical Statistics 35(1), March 1964, pp.73--101,
DOI 10.1214/aoms/1177703732.
Exact free journal URL and capture record are in the source README.
PDF: source/references/huber-robust-location-1964/huber-1964.pdf.
29 journal pages, no cover, 2835541 bytes.
SHA256: 0BD9E67B4910EBD47CB0349F673CA6C25307A4035DBCF0E98EEAC567DD150AD4.

All 29 pages were read in full from the actual original images, including
Tables I--IV and the concluding comparisons and references on p.101.
Physical page n corresponds to printed page n+72.
The source-reading images are in tmp/pdfs/p15-huber-location-source/.
The PDF's 2006 creation metadata describes digitization, not publication.
The research and PDF skills guided reading. A source-index agent could
not start because the agent thread limit was reached.

## Authored scope, without a whole-paper completion claim

The saved component fully develops the known-scale contaminated-normal
location construction. It includes the general convex-criterion
foundations of Section 2, the conditional smooth-score argument of
Section 3, the clipped-score construction and its finite computation,
the normal-contamination saddlepoint of Sections 5--6, the exact
asymmetric-bias analysis needed to qualify that result, and the original
all-translation-equivariant limiting-risk conclusion.

The primary paper is broader than this component. Its general prototype,
information game, alternative neighborhood, scale and joint proposals,
and higher-order methods now have their own authored destinations in
P15.51–P15.53, recorded below. This preserves their distinct models
and proof obligations rather than treating the normal special case
as the entire paper.

## Twelve reciprocal pairs

Chapter: sec:p15-huber-robust-location.
Annex: sec:annex-p15-huber-robust-location.

| Body | Full proof |
| --- | --- |
| thm:p15-convex-location-minimizers | annex:p15.convex.location.minimizers |
| thm:p15-convex-location-consistency | annex:p15.convex.location.consistency |
| thm:p15-convex-location-normality | annex:p15.convex.location.normality |
| thm:p15-nonconvex-location-qualification | annex:p15.nonconvex.location.qualification |
| thm:p15-huber-location-computation | annex:p15.huber.location.computation |
| thm:p15-huber-normal-variance | annex:p15.huber.normal.variance |
| thm:p15-huber-least-favorable-normal | annex:p15.huber.least.favorable.normal |
| thm:p15-location-integrated-score-bound | annex:p15.location.integrated.score.bound |
| thm:p15-huber-location-minimax | annex:p15.huber.location.minimax |
| thm:p15-huber-asymmetric-bias | annex:p15.huber.asymmetric.bias |
| thm:p15-huber-location-failure-cases | annex:p15.huber.location.failure.cases |
| thm:p15-fisher-minimizer-nonuniqueness | annex:p15.fisher.minimizer.nonuniqueness |

## Hypotheses and substantive proof decisions

The actual i.i.d. strong-law interface and the Lindeberg--Feller,
i.i.d. CLT and perturbation interfaces were read before use:
thm:p15-etemadi-strong-law, thm:p15-clt-lindeberg-feller,
thm:p15-clt-iid and thm:p15-clt-perturbation.
The convex-score proof retains the source's triangular-array route;
the Lindeberg tail domination, zero-variance case, one-sided derivative
limit, minimizing intervals and threshold atoms are all explicit.
The smooth nonconvex result retains consistency as a premise and
derives E psi=0 from the exact score equation, rather than assuming it.

The original Lemma 4's strict event inclusions need care for arbitrary
minimizer selection, flat intervals and score jumps. The active proof
uses a valid shifted-threshold sandwich instead of copying the
unqualified strict inclusion. Midpoint selection is proved measurable
and translation equivariant; set equivariance is not asserted to make
every possible selector equivariant.

For symmetric contamination with atoms at the two clipping points,
the population derivative is the mass in the open central interval
plus half the mass at its two endpoints. This handles the actual
normality premise instead of assigning an arbitrary value to psi'
and integrating it against atoms. An asymmetric two-atom example
calculates the different slopes and the two-half-normal limit.

The clipped normal density is normalized by
(1-epsilon)^(-1)=2Phi(k)-1+2phi(k)/k.
The map is strictly decreasing, giving the unique positive k for
each 0<epsilon<1. Nonnegative excess tails, information, score
optimality and uniqueness within the stated absolutely continuous
contamination-density class are proved.
The literal k=0 criterion is constant; the median is the limit
after normalizing rho_k by k.

The all-equivariant lower bound quoted through Le Cam on pp.81--82
is supplied directly by an editorial integrated-score proof.
A cosine-squared prior of width C/(2sqrt(n)), together with a clipped
estimator and justified integration by parts, gives
E min(nT_n^2,C^2)>=1/(I+4pi^2/C^2).
This proves the exact needed inequality for every n and C.
It does not assert acquisition of either Le Cam original.
The resulting minimax proof keeps sup_F, limit_C and liminf_n in the
source's stated order. A finite-sample convex-hull variance example
shows why those operations cannot be interchanged.

Section 7's bias approximations are replaced, for the covered clipped
normal method, by the exact population-root equation. The linear
expression is explicitly a fixed-k small-contamination approximation.
The normal-component location is not claimed identified without the
symmetry or decomposition premise.

## Direct general-information correction already supplied

The blanket uniqueness assertion in Section 8, Theorems 2 and 4,
requires correction for disconnected supports. The active chapter
contains a complete counterexample: the density 2 sin^2(pi x) on (0,1)
and its translate to (2,3) generate a convex vaguely compact class
whose every member has Fisher information 4pi^2.
Thus every member minimizes information.
The known-scale normal-contamination density's uniqueness remains
valid and has its own positive-density equality proof.
The general-information presentation now proves the exact componentwise
equality and support-sensitive variation in P15.51; its positive-density
uniqueness conclusion preserves this correction.

## Current destinations of the completed continuations

The former continuation list is now supplied across the four Huber
chapters. This is the current authoring/integration map; the original
author block and its scope above remain historical evidence.

| Source scope | Current destination |
| --- | --- |
| Section 4 median, capped quadratic and the stated conjecture | P15.52, thm:p15-huber-mean-median and thm:p15-huber-trimming-calculation |
| Section 5 general log-concave construction | P15.51, thm:p15-huber-general-density and thm:p15-huber-general-minimax |
| Full historical Table I and its units | P15.52, sec:p15-huber-table-one, all 31 rows and every column |
| Section 7 median bias and sample-size interpretation | P15.52, thm:p15-huber-exact-median-bias and the accompanying source comparison |
| Section 8 information game and uniqueness correction | P15.51, sec:p15-huber-information-game |
| Section 9 CDF neighborhood and Table II | P15.52, thm:p15-huber-cdf-domain through thm:p15-huber-cdf-saddlepoint |
| Section 10 scale, both regimes and Table III | P15.52, sec:p15-huber-log-scale; full sign-information lower bound in P15.53 |
| Section 11 all three proposals, finite theorem, iteration and Table IV | P15.52, sec:p15-huber-joint-proposals |
| Full joint law at clipping atoms and correct variance-bound interpretation | P15.53, thm:p15-huber-joint-atomic-limit and thm:p15-huber-joint-atomic-bound |
| Section 12 subset projection, distinct-pair median and final comparisons | P15.52, sec:p15-huber-mr |
| Every-sign scale comparison and unrestricted continuous-mixture bridge | P15.53, thm:p15-huber-scale-sign-minimax and thm:p15-huber-zero-atom-mixture-bridge |

The paper's explicitly conjectural trimmed/adaptive claims and its
iteration-cycle question retain their stated 1964 standing. Their
historical description is not a claim of a present-day resolution.
Separate Hoeffding1948, Hodges–Lehmann1963, influence-function and
breakdown originals are not acquired by association.

The delegated production extension routes P15.52 and P15.53 in both
drivers and updates these reader pointers. Canonical bibliography
and symbols remain root-owned; the new combined notation intake
is handbook/registry/symbols-intake-p15-huber-remaining-and-endpoints.csv.
No review, scanner, test, build or manuscript rendering was run.

## Author handoff

The saved body, annex and source/intake files received the complete
author read-through. Final corrections made the independent-sampling
premise and density-function regularity explicit and corrected the
local interval used in the finite-sample computation proof.
No independent review, scanner,
test, build or manuscript render is run in this block.
