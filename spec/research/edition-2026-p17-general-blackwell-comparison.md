# P17.9: general Blackwell comparison and the full martingale construction

Written and integrated 8 September 2026. The previous goal continuation
was progress: it connected twelve components with 119 supplied
statement/proof pairs. This component continues the actual manuscript
writing from the completed finite comparison and probability foundations.
Consolidated independent reviews remain deferred until all changes finish.

Body: handbook/parts/p17/general-blackwell-comparison.tex, 17509 bytes,
SHA-256 BE0BAC815033749E3AD54E23B2233284AFE64780AD71E4EDEF5CE111C5B1A90F.
Annex: handbook/annex/p17/general-blackwell-comparison.tex, 35846 bytes,
SHA-256 E3BD7D67ECEEF555CD79EB83EC0DF90E474285D51FF74E6347462D4D7C1E55CC.

## Exact primary and complete reading

David Blackwell, Equivalent Comparisons of Experiments, Annals of
Mathematical Statistics 24 (1953), pp. 265–272. The unchanged held paper is
source/references/blackwell-equivalent-experiments-1953/blackwell-1953-equivalent-comparisons.pdf,
SHA-256 F490B8395187EDC34AB46A3D45455F1F59CBBC9632964C63218A2F4C8BA8CD1D.
The publisher source is
https://projecteuclid.org/download/pdf_1/euclid.aoms/1177729032.
The existing key Blackwell1953EquivalentExperiments is reused.

Root personally read every full source page 265–269 in this block,
including the original experiment/loss definitions, standard measures,
Theorems 1–3, the finite Theorems 4–7 and the entire general Theorem 8
with auxiliary constructions A, B and C. The relevant final two pages
had also been read at the preceding continuation boundary. The PDF is
image-based; the unsuccessful text extraction returned only page breaks.
The existing source-page images were therefore read directly.
No manuscript PDF was built or inspected.

The exact finite theorem and the conditional-law, countable-extension
and forward/backward limit interfaces were read in the actual LaTeX.
The new body and annex were read completely after writing, then their
domain and integration-variable corrections were made as one authoring
batch. No independent review, scoped scanner, test or acceptance check ran.

## The complete retained source construction

The centroid chain uses conditional means in positive-mass dyadic cells
and the actual coarse/fine joint law. The vertex chain uses normalized
product barycentric weights and proves the nested-grid identity even
on cell faces. The source's finite comparison theorem supplies each
distant-level coupling.

The full diagonal extraction gives compatible kernels at every level.
The new text states their exact row shapes and composition order:
W_N = T_N W_(N+1) V_(N+1). This is the source's condition B(d) with
row-stochastic rather than measure-operator notation.

The probability of every finite two-sided string is written explicitly.
Deleting its middle pair is proved to give the previous law, so the
already supplied Kolmogorov extension applies. The forward filtration,
reverse tail filtration and both conditional-mean identities are proved.
Both martingale limits and a final upward conditional-limit argument give
E(R_star | L_star)=L_star. Continuous-test convergence identifies the
marginals. A regular conditional law and a measurable point-mass repair
produce a probability kernel with the mean identity at every input.
No weak-compactness theorem substitutes for this source proof route.

## Fourteen complete statement/proof pairs

Body prefix thm:p17-; annex prefix annex:p17.:

compact-convex-tools; continuous-law-identification; centroid-refinement;
vertex-refinement; compatible-transports; blackwell-joint-process;
general-convex-transport; transport-calculations; general-standard-measure;
compact-measure-selection; general-risk-compactness;
general-decision-comparison; general-garbling; continuous-experiment-example.

The source's standard-measure assertions are also reconstructed: posterior
barycenters, implementing experiments, equality of original/canonical risk
sets, closed bounded convex risk sets, all finite payoff comparisons,
the single full-support prior criterion, and equality of standard measures.
The kernel simulation explicitly reverses the posterior coupling before
recovering the target observations.

The affine-approximation lemma, nested-cell compact measure selection,
closedness proof for attainable losses, arbitrary full-support prior
extension and concrete calculations are proved additions supporting
the complete source statements. They are not attributed as the literal
proofs in Blackwell's separate 1951 paper, whose body remains unacquired.

## Direct corrections and measurable-space qualifications

The source's approximation assertion on p. 268 refers to every open set.
The active theorem instead gives a quantitative continuous-test estimate.
The explicit mixture one-half delta-zero plus one-half uniform(0,1)
has centroid mass one on (0,infinity) at every level but original mass
one-half there. Its first centroid and mass are calculated exactly.

The vertex construction uses the normalized fractions
(t_i - h a_i)/h and 1 - (t_i - h a_i)/h, h=2^(-N).
Unnormalized coordinate distances would have total product mass h^d;
the supplied two-dimensional example verifies normalization and both
coordinate means. The source's displayed distance-like factors are
not copied into an unnormalized active kernel.

Zero-mass cells have no conditional centroid. Finite support means
positive-mass support, and any coincident centroid values are combined
through a conditional distribution rather than an arbitrary parent.
The upper grid may leave the original bounded set; all approximants
remain in one explicitly chosen compact box. The final laws are proved
to be the original laws and the final kernel is on the original Borel set.

A conditional kernel has its barycenter identity initially only almost
everywhere. The active construction replaces its exceptional row at x
by delta_x, rather than by a fixed point mass, to prove the source's
every-input requirement.

Loss-set and finite-decision equivalences are proved for arbitrary
measurable observation spaces. A full observation-simulation kernel is
proved on standard Borel spaces, or whenever the needed observation
recovery kernel exists. The actual proof uses that condition explicitly;
it is not silently inferred from the older phrase Borel field.
The vector transport theorem itself covers every bounded Borel X,
without requiring X closed, and proves the full implication of
Theorem 8's convex-hull test premise.

## Integration and next work

Both new files are connected after the restricted-decision/binary-testing
component. The finite comparison and conditional-limit chapters now link
the completed general construction. P17.9 remains a drafting scope
whose final nesting is governed by the approved parent-chapter outline.
All local notation is included in the canonical symbol intake.

The remaining decision work includes sequential information, dynamic
choice and strategic regimes. The separately identified 1951 source
presentation retains its own source obligation. The completed bounded
transport theorem does not assert an unbounded or infinite-state extension.
