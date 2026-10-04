# Independent topic review: probability and decision theory

Date: 8 September 2026 UTC / 7 September 2026 Pacific. Reviewer: `/root/probability_decision_topic_review`, a fresh nonauthor review context. Repository: `C:/Dev/the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The six working-tree bodies below, rather than HEAD alone, identify this review's content.

**VERDICT: PASS for the mathematical scope supplied by all three treatments.** All 23 supplied result/proof pairs were read and checked. No actionable mathematical error, missing direction, undefined boundary operation, or unresolved proof component was found in those pairs or their accompanying examples. This conclusion concerns the frozen treatments; it does not close their broader P15-U1 or P17-D2 units.

## Independence and actual reading

No current source-review or publication-review conclusion was consulted. The author intakes supplied scope and locators, not proof of their own correctness. Every line of all six target files was read, including definitions, qualifications, examples and concluding boundaries. The supplied SHA-256 values were verified against the files. Paths in the following tables are relative to the repository.

| Target | Complete read | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p15/measurable-probability.tex` | 1-484 | `C249F33E0E0FC88084B05A7D44098DB87B3E4814083B34709D6DBE2B562340D9` |
| `handbook/annex/p15/measurable-probability.tex` | 1-481 | `FBB9E6C733A1F286F7E56FC31B7E76D4412D781E03711ED02D8D4B3AAEF8C8FC` |
| `handbook/parts/p17/finite-expected-utility.tex` | 1-390 | `6F83B6CB0300B241C8751E48747B577FB5869A02418C1C8C621E808515DD6EB5` |
| `handbook/annex/p17/finite-expected-utility.tex` | 1-340 | `C04B72A6DDC4B34147359A776597B99A16E4DE6D61A7C4789F5C413CF2FF11D3` |
| `handbook/parts/p17/risk-aversion.tex` | 1-355 | `F2B0A4CF575723E4CB6F8212077A59E64E276DAA43A5B25B57374D8E6657CD4A` |
| `handbook/annex/p17/risk-aversion.tex` | 1-417 | `1FAEAA08391C801C52CC0814189AE4B7FB4FB26DE788C0F7789D62D46917DC7A` |

The actual finite prerequisites were inspected at the following extents. Unlisted portions are not claimed read in this review.

| Prerequisite | Partial read | SHA-256 of entire file |
| --- | --- | --- |
| `handbook/parts/p15/finite-probability.tex` | 1-169, 345-385 | `934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1` |
| `handbook/annex/p15/finite-probability.tex` | 1-119, 202-249 | `7CE651CE52FE8BFA66E5BEC221BDF48EE6318538E6A99B8E987E18C90D6B67F3` |
| `handbook/parts/p17/finite-preferences.tex` | 1-240 | `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C` |
| `handbook/annex/p17/finite-preferences.tex` | 1-145, 212-253 | `B141A371731E7A0A3BEFF1C88C839F98720BE4F894A2D475CAF098A61159202C` |

Additional complete reads: `spec/EDITION-2026-CONTRACT.md` 1-168 (`C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3`); `spec/research/edition-2026-p15-u1-measurable-probability.md` 1-174 (`5C28174B6A444DD458A6701D6EB775F50EE940F1B715ECEC97DCFBE826FD5AD6`); `spec/research/edition-2026-p17-d2-finite-expected-utility.md` 1-54 (`FCA706984A46F4EF5AEE5AE60E1782E84D9759A174D57C0CFCC57AC20140E144`). No primary-source PDF was needed to discharge a missing mathematical argument; no source-fidelity verdict is asserted here.

## P15: measurable probability — PASS

The table uses the result suffix after `thm:p15-`; the corresponding annex identifier uses `annex:p15.`. Body and annex line ranges belong to the measurable-probability files above.

| Result | Body; annex | Mathematical checks and disposition |
| --- | --- | --- |
| `generated-events` | 49-56; 12-35 | PASS. Complements, differences and countable intersections follow by set identities. Arbitrary nonempty intersections of sigma-algebras preserve every axiom; the generating family is nonempty, including when the generator collection is empty. |
| `measure-laws` | 102-124; 37-90 | PASS. Empty finite additivity, disjointification and monotonicity justify subadditivity. Increasing continuity permits infinite mass; decreasing continuity uses finite subtraction only after `mu(A_1)<infinity`. Null unions and probability-one intersections follow with no completion assumption. |
| `countable-atomic` | 129-147; 92-145 | PASS. Finite-subset suprema prove regrouping in both directions; finite sums approximating finite suprema, an infinite block, empty blocks, empty total index set and zero terms are covered. The construction and converse singleton decomposition prove countable additivity and unique probability masses without signed-series rearrangement. |
| `borel-generators` | 216-222; 147-184 | PASS. Rational rectangles form a countable base in each fixed finite dimension; the union for the empty open set is empty. Rational closed rays generate both sorts of real ray and open intervals, with the endpoint inclusions correct. |
| `measurability-criterion` | 249-261; 186-221 | PASS. The collection of target sets with measurable inverse images is a sigma-algebra. The actual inverse-image collection is itself a sigma-algebra and is minimal; applying the proved criterion supplies the reverse inclusion for inverse images of generators. |
| `measurable-operations` | 291-300; 223-274 | PASS. Composition, coordinates in both directions and continuous functions use the proved generators. Indicators, overlapping indicator sums, constants and the empty sum are covered. Finite measurable fibers supply the converse simple-function representation. |
| `measurable-limits` | 323-346; 276-339 | PASS. Strict-sublevel identities handle both extended endpoints and avoid attainment assumptions for infima. Tail infima/suprema give both extended limits. The convergence event uses only finite real differences. Dyadic approximants are measurable, finite and increasing in all three threshold cases, including zero, grid boundaries, truncation boundaries and `Z=infinity`; convergence is proved separately for finite and infinite values. |
| `pushforward-laws` | 376-390; 341-372 | PASS. Inverse images preserve disjointness, normalization and unions. Transformation composition and atomic sums follow directly. The countable target representation allows an arbitrary source space and covers empty fibers and events. |
| `measure-uniqueness` | 410-415; 374-429 | PASS. Both auxiliary-system stages of the pi-lambda argument are supplied; the empty pi-system is included. The agreement class for two probabilities uses valid finite subtraction and continuity from below. This is uniqueness, with no inferred measure existence. |
| `cdf-laws` | 427-445; 431-481 | PASS. Everywhere finite real values justify both endpoint limits. Right continuity and the left-limit formula use the correct nested events; interval probabilities and atom jumps use finite differences. Positive-mass sets have at most countably many points, exactly accounting for discontinuities. Closed rays are a proved generating pi-system, so CDF equality determines the full Borel law. |

The measure space need not be complete: “null” always refers to a measurable set, and no arbitrary subset of a null event is declared measurable. The nonempty outcome-space convention is consistent throughout. The extended-limit statement does not assert that an infinite limit is real valued or permit infinity minus infinity.

Examples checked directly: `sum_{n=1}^m 2^{-n}=1-2^{-m}`, waiting tail `2^{1-m}`, even mass `1/3`, odd mass `2/3`, and CDF jump `2^{-m}`, including the left limit zero at 1. The tails are nonempty with empty intersection. Counting measure supplies the stated failure without the finiteness premise; equal singleton masses cannot normalize on the positive integers. The finite/cofinite charge has the stated finite additivity and impossible countably additive extension. The parity sigma-algebra has exactly four events; `{1}` is absent. The values `1/n` have the specified atoms and an unattained zero limit point. These claims occur at body 58-68, 157-201, 267-278, 348-352, 392-398 and 447-456.

## P17: finite expected utility — PASS

The next table uses result suffixes after `thm:p17-`, with annex identifiers `annex:p17.`. Its ranges belong to the finite-expected-utility files.

| Result | Body; annex | Mathematical checks and disposition |
| --- | --- | --- |
| `lottery-reduction` | 52-71; 4-38 | PASS. Coordinates and all flattened weights normalize. The joint mass `alpha_k p_k(z)` proves reduction; conditional division is performed only for positive branch probability. Zero branches can carry arbitrary specified laws without affecting the marginal. Probability-law identity does not infer a preference axiom or branch/prize independence. |
| `mixture-comparison` | 149-162; 40-104 | PASS. Independence in both comparison directions preserves weak, strict and indifferent relations. Weight zero and weight one are treated before forming a normalized residual. Strict segment order includes all endpoint cases and has a valid interior decomposition with `lambda=t/s`. |
| `lottery-calibration` | 164-176; 106-152 | PASS. The calibration set is nonempty and relatively closed using exactly the stated neighborhood axiom C. Real completeness supplies its supremum; closedness and the strict-neighborhood contradiction prove indifference. Strict segment order proves uniqueness and all endpoint/interior characterizations. |
| `finite-vnm` | 200-220; 154-241 | PASS. Finite best/worst selection and successive replacement bound every lottery. Calibration yields the utility and reduction yields representation in both directions, including ties. All-indifferent and singleton domains are included. The converse proves completeness, transitivity, independence and actual two-argument neighborhood continuity; `C=0` is handled without division. |
| `vnm-affine-uniqueness` | 229-242; 243-286 | PASS. Equality on all lottery comparisons yields the same calibration indifferences and one positive affine scale. Nonconstant utilities fix both constants; constant utilities allow any positive slope with a matching intercept. The converse follows from normalization and includes singleton prizes. |
| `vnm-counterpreferences` | 353-373; 288-340 | PASS. The largest-coordinate score is Lipschitz continuous and violates indifferent replacement. Lexicographic completeness/transitivity and both directions of independence are proved; the displayed perturbation stays in the simplex and has distance `sqrt(2) epsilon`, contradicting the actual continuity axiom. |

The finite-menu use at body 253-273 is valid by restricting the represented lottery preference to the finite menu and applying the actual finite maximal-choice theorem; it asserts no maximum on an arbitrary infinite menu. Empty menus and ties are addressed. The finite ordinal theorem is not used to represent the infinite simplex.

Worked comparisons at body 275-332 and 360-372 were recomputed: scores `1/2` versus `2/5` or `3/5`; `sqrt(2/5)>1/2`; the threshold `alpha=2/5`; and invariance under `5u-2`. For the common-consequence example the coefficient vector of each side of `U(L_1)-U(L_2)=(U(L_3)-U(L_4))/4`, ordered by prizes `0,3000,4000`, is exactly `(-1/20,1/4,-1/5)`. Thus the stated paired strict choices contradict expected utility without assuming linear utility in money.

## P17: monetary risk — PASS

The following ranges belong to the risk-aversion files.

| Result | Body; annex | Mathematical checks and disposition |
| --- | --- | --- |
| `finite-stochastic-dominance` | 62-79; 4-62 | PASS. The telescoping identity holds for every finite union of supports, including its one-point case. Tails use `>=` and CDFs use `<=`; their exact adjacent-support relation is `G(x_{i+1})=1-F(x_i)`. Every failed tail produces a negative `D_j`; the specified positive increment `H` makes the expectation difference at most `-1`, and the linear extension is continuous and strictly increasing on the entire interval. The nondecreasing-utility variant follows in both directions. |
| `finite-jensen` | 117-137; 64-115 | PASS. Removing zero weights makes the induction denominator positive. For the strict case, choosing a minimum positive-weight prize leaves a residual mean strictly above it whenever another distinct prize occurs, including repeated minima. Both secant inequalities and both directions of the open-interval second-derivative criterion are justified. |
| `risk-aversion-concavity` | 139-147; 117-143 | PASS. Jensen gives the sure-mean comparison; all binary lotteries give the converse. Exact mean indifference forces one affine function by anchors and mixtures also outside the anchor interval, with the singleton case covered. Strict monotonicity forces positive slope only on a nondegenerate interval, as stated. |
| `certainty-equivalent` | 165-179; 145-174 | PASS. The finite support has attained extrema and its closed convex hull stays inside the monetary interval. The intermediate value theorem supplies an attained utility value and strict increase gives uniqueness; singletons, open intervals and included endpoints are covered. Premium signs and affine-scale invariance follow from this exact range argument and Jensen. |
| `comparative-risk` | 199-210; 176-223 | PASS. The acceptance implication is equivalent to CE ordering by choosing `c=CE_1(p)`, including ties. Jensen proves concave transformation implies CE ordering; arbitrary two-point lotteries prove the reverse on every point and mixture of `u_2(I)`. Neither utility must itself be concave. |
| `arrow-pratt-comparison` | 247-269; 225-273 | PASS. Open interval, C2 regularity and everywhere positive derivative justify the inverse and its derivatives. The factor multiplying `r_2-r_1` is positive. The local curve remains inside the inverse's range and differentiation gives exactly `psi'(t)=-theta/(1-theta)` and `psi''(t)=r_u(t) theta/(1-theta)^2`. Global comparison requires the inequality throughout the interval. |
| `cara-characterization` | 296-312; 275-417 | PASS. The anchor proof first extends affine uniqueness to every real prize using only finite-support lotteries, including prizes outside `[0,1]`. Wealth invariance then gives one positive continuous translation factor. Its multiplicative identity and the additive logarithm yield `A(w)=exp(k w)` for negative and positive rational and real shifts. The zero-parameter and nonzero-parameter cases are solved separately; concavity excludes `k>0`. The grid recurrence extends to negative indices and the already derived common parameter enforces compatibility across all grids. The differential route states its extra assumptions and derives constant coefficient. Both converse families and translation of CE/premium are proved. |

Examples checked at body 81-94, 212-229, 271-273, 321-335 and 337-346: the one-unit shifted lottery satisfies the two dominance criteria, whereas the mean-one spread and sure one have crossing CDFs at the specified endpoints. For prizes 1 and 9 the mean is 5, logarithmic CE is 3, square-root CE is 4, and premiums are 2 and 1; the relative transformation is `2 log t`, with coefficients `1/x` and `1/(2x)`. Exponential averaging gives `-exp(-rho w) cosh(rho d)` and premium `log(cosh(rho d))/rho`, zero exactly at `d=0`; `rho=log 2,d=1` gives `log(5/4)/log 2`. The final-wealth examples both produce certain 1500 and the same equal-probability lottery on 1000 and 2000.

## Scope and disposition

No mathematical correction is requested for the frozen files. The arguments use elementary set theory and real analysis as stated or inherent in the explicit differentiability results: real completeness, rational density/countability, finite arithmetic, the intermediate and mean value theorems, and the inverse derivative formula. No omitted specialized probability or preference theorem is substituted by a source citation.

The measurable-probability boundary (body 458-484) correctly leaves measure existence/extension, Lebesgue measure, general integration and its convergence theorems, densities and conditional expectation for subsequent work. The monetary domain (body 16-44) supplies its global utility as a premise; it does not infer consistency on an infinite interval from the finite-prize theorem. The P17 boundaries explicitly retain subjective probabilities, ambiguity, sequential information, infinite-support and stopping questions, and the separate Rabin argument. The examples assert calculations from stipulated preferences, with no population-frequency, welfare-scale or normative conclusion inferred.

This reviewer wrote only this report. No manuscript PDF, build, render, test, source edit, canonical-record edit or admission was performed. The verdict supplies the independent mathematical review component for this exact six-file snapshot.
