# P15.30: event products and elementary density constructions

8 September 2026. Eight complete statement/proof pairs supply every
source Exercise 4.3.4–4.3.10 and the elementary convergence premise
needed to retain the source's distinct density proof.

## Exact source

Durrett author Version 5 dated 11 January 2019:
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
Reuse DurrettPTEAuthor2019.

Printed pp. 233–234, physical pp. 241–242, were read in full,
including all thirteen Section 4.3 exercises and their exact hypotheses.
The frozen new target is Exercises 4.3.4–4.3.10. Exercises 4.3.1–3
and 4.3.11–13 have their previously authored martingale/branching homes;
Kesten–Stigum's separate referred source is not supplied by this batch.

The actual density calculus annex was read for sums, change of measure,
chains and reciprocal versions. The new elementary density proof does
not depend on that annex's general Radon–Nikodym existence theorem.

## Supplied pairs

Body prefix thm:p15- and proof prefix annex:p15. use identical suffixes:

1. event-product-criterion: source Exercise 4.3.4, preserving both
   Borel–Cantelli arguments and the positive finite-prefix factor.
2. survival-product: Exercise 4.3.5, exact successive conditional
   hazards, decreasing-event limit and zero-survival handling.
3. partition-ratio-supermartingale: Exercise 4.3.6, explicit finite
   conditional averages, each refinement identity/inequality and a
   strict lost-mass example.
4. elementary-partition-convergence: a full bounded upcrossing proof
   using only finite-cell integral identities; no general conditional
   expectation existence is assumed.
5. countably-generated-radon-nikodym: the complete Exercise 4.3.7
   finite-partition mixture proof, sigma-finite reduction, assembly
   and uniqueness.
6. bernoulli-product-complete: both parts of Exercise 4.3.8, with
   exact affinity bounds and an explicit endpoint-support extension.
7. bernoulli-sparse-singularity: Exercise 4.3.9's event proof and
   an explicit square-summable-difference singular example.
8. bernoulli-l1-comparison: Exercise 4.3.10's affinity bound,
   both licensed directions, and a failed-local-support example.

## Mathematical scope and completed premises

The product criterion assumes every p_m < 1, so a single zero product
factor cannot defeat a finite-sum conclusion. Its proof uses the
source's Borel–Cantelli route independently of the earlier logarithmic
argument.

The survival statement never conditions on a null survival event.
If one occurs, the conclusion follows by inclusion. Otherwise all
hazards are in [0,1), and the exact product gives both directions.
No independence of the original events is imposed.

The elementary conditional average is defined as a finite sum of cell
constants with its all-event identity proved directly. The upcrossing
argument uses only these finite identities and finite trading sums.
The countably generated density construction starts with bounded ratios
relative to (mu + nu)/(mu(Omega) + 1), obtains their limits from that
elementary lemma, and extends finite-cell measure identities by the
pi-lambda theorem. Its density is their limiting quotient. This avoids
the circular general conditional-expectation existence premise explicitly
flagged by the source exercise.

The sigma-finite construction uses a disjoint common finite-measure
cover, normalizes the positive reference blocks, rescales their
densities and sums them. Null reference blocks have zero target mass.
The uniqueness proof removes the common nonfinite null set before
subtracting two densities, so no infinity-minus-infinity is evaluated.

The full endpoint Bernoulli criterion states local support separately
from the infinite affinity product. Interior bounds yield constants
1/(4(1-epsilon)) and 1/(4 epsilon) for the squared-difference comparison.
The explicit alpha_m = 1/(m+1)^2, beta_m = 1/(m+1) example has summable
squared differences and singular laws, proved by success-event counts.
Summable absolute differences suffice with local support; mutual
absolute continuity requires both local directions.

## Saved artifacts and integration

Body: handbook/parts/p15/density-and-product-exercises.tex
8,976 bytes; SHA-256:
D2938E941CF73AD7C922AEB1FABEF2F24E7F7E498A5981851738087E02CF21A6.

Annex: handbook/annex/p15/density-and-product-exercises.tex
14,424 bytes; SHA-256:
2E9A123FC4732039F5305CD67A2C569A335B896591D472A47E482002E292A5B6.

The pair is integrated after the Pólya treatment, with provisional
scope P15.30. Earlier density and Radon–Nikodym reader boundaries now
refer to these source exercises and the separate elementary proof.

Root read both complete actual LaTeX files in the authoring batch.
The last correction makes the uniqueness proof's null-set exclusion
explicit. Research and PDF skills guided primary reading; no independent
review, scanner, test, manuscript build, manuscript render or admission
check ran.

