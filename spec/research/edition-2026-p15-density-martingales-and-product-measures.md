# P15.28: density martingales and infinite product measures

8 September 2026. This authoring and integration batch supplies eleven
complete statement/proof pairs for Durrett's Section 4.3.3 and explicit
extensions of its product criterion.

## Primary and complete target

The held primary is Durrett's author Version 5, 11 January 2019:
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
It remains the 490-page, 2,195,717-byte author version.
Reuse bibliography key DurrettPTEAuthor2019.

The complete target read and supplied is printed pp. 227–230:
Theorem 4.3.5, Lemma 4.3.6, the entire mixture-reference proof and its
continuation, Example 4.3.7, the strict-positive independent-product
tail argument and the complete proof of Theorem 4.3.8.
These are physical pp. 235–238. The extraction also included the
neighboring Pólya statement and branching material through printed
p. 232; those neighboring portions are not counted as new content here.
Actual source images were read for printed pp. 228–229, at
tmp/pdfs/p15-density-source/source-236.png and source-237.png.

The required Appendix A.4.6–A.4.9 exercises, Radon–Nikodym statement
and uniqueness and Lebesgue-decomposition continuation were read on
printed pp. 469–470, physical pp. 477–478. Their needed density
calculus is already proved in the active Radon–Nikodym body and annex.
The new proof preserves the source's bounded mixture method; it does
not replace that route with the existing supremum-of-densities proof.

## Supplied reciprocal pairs

Each suffix below has body prefix thm:p15- and proof prefix annex:p15.

1. density-martingale: restriction integration, every conditional
   expectation identity, finite convergence under the reference
   probability and the limiting mass inequality.
2. density-mixture-reference: bounded densities under the common
   probability, extension from the generating algebra, positivity of
   each finite denominator, and all finite/infinite limit cases.
3. density-lebesgue-decomposition: both integral terms, their correct
   measure transfers, the singular set and full uniqueness.
4. density-uniform-integrability: absolute continuity, no lost mass,
   uniform integrability and L1 convergence in both directions;
   mutual continuity and singularity criteria.
5. partition-density-approximation: every finite-cell ratio and null
   case, the full dyadic mixed-atom calculation and the counterexample
   when the filtration does not generate the target sigma-field.
6. product-density-filtration: cylinder densities, all finite affinity
   identities and the exact L2 distance between square roots.
7. product-positive-tail: both logarithmic tail events, including the
   reciprocal martingale under the target probability, and the
   complete equivalence-versus-singularity conclusion.
8. product-affinity-criterion: both source product alternatives, the
   exact square-root estimate, direct Fatou passage to L1 convergence,
   both singular limit measures and the zero-density extension.
9. product-affinity-series: logarithmic product/series equivalence
   with finite initial factors and the square-root deviation identity.
10. product-gaussian-comparison: full completed-square affinity for
    arbitrary positive normal variances and means; exact equal-variance
    summability criterion for the full sequence laws.
11. product-bernoulli-boundaries: exact two-point affinities, explicit
    quadratic bounds, convergent/divergent perturbation examples and
    a zero-coordinate-density counterexample to the tail assertion.

## Author corrections and exact scope

The mixture probability is (mu + nu)/(c + 1), where c = mu(Omega).
This keeps the source proof valid for every finite nonnegative target,
including the zero measure, without dividing by c. The restricted
reference measure is defined before its densities. The limits and
null-set transfers name rho, mu and nu explicitly.

Local absolute continuity makes rho_n equivalent to nu_n and supplies
Z_n > 0 rho-almost surely. The common countable full-measure event then
licenses the finite-time quotient identity. At a zero limiting Z, the
other limiting density is c + 1 > 0, so the entire quotient sequence
tends to infinity. No 0/0 or mere-limsup-to-limit step is used.

The source's single displayed zero-one assertion does not alone
determine the lost target mass. The full preserved tail route adds the
reciprocal product under mu and its own tail zero-one assertion, so
mu(X = infinity) is zero or one. The dyadic mixture explicitly shows
why a positive finite reference-almost-sure limit is insufficient
without mass preservation.

The source assumes every coordinate density is positive. That
assumption is retained in the logarithmic tail theorem. Its separate
square-root proof also establishes the stated extension to nonnegative
coordinate densities. In that extension positive affinity gives
one-sided absolute continuity. Equivalence requires equivalent
coordinate laws. A deterministic first coordinate against a fair
reference gives a positive affinity product and a zero-likelihood
event of probability one half.

The Gaussian and Bernoulli applications and the equivalent summability
test are proved additions. They are not attributed as printed source
examples. The preceding general Pólya beta-limit proof and other
Section 4.3 exercises remain separately assigned source presentations.

## Saved identities and integration

Body:
handbook/parts/p15/density-martingales-and-product-measures.tex
12,370 bytes; SHA-256:
C689EB49746EA81636720EDCF7E4C8BC97DFDAF7104C5EFF4C74B58E078B6C31.

Annex:
handbook/annex/p15/density-martingales-and-product-measures.tex
18,929 bytes; SHA-256:
B546A66929679B72AD1512EAE34506B67F17BE045E4FB6C964F16934D6729777.

Both files are on the active P15 routes. Provisional drafting scope
P15.28 leaves P15.27 reserved for the characteristic-function remainder.
Earlier Radon–Nikodym and quadratic-variation boundaries link to the
completed density and product results. Canonical notation includes
measure-specific limits, reference ratios, affinity products, reciprocal
likelihoods and the separate scalar Bernoulli probability role.

Root read the entire saved body and annex as one authoring batch.
The final body correction defines mutual absolute continuity before
use and qualifies the opening description by coordinate equivalence.
No independent review, scanner, test, build, manuscript render or
admission check ran. The research skill directed source reading and
this note; the PDF skill supported the exact primary equations.

