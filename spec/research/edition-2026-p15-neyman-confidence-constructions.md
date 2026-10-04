# P15 / U4: Neyman 1937 examples and comparison criteria

Integration update: the Student Example III and equation (130) mathematical
dependencies identified below are now supplied in student-inference.tex,
with thirteen full proof pairs and their source map in
edition-2026-p15-student-inference.md. The earlier block inventory below
preserves its historical checkpoint. The distinct introductory,
simultaneous-region and referred-original source obligations remain open.

Author block began 2026-09-09 01:08:40 UTC, with deadline 01:53:40 UTC. Twelve complete statement/proof pairs are saved. One whole-batch author reading of the saved LaTeX is complete. No independent review, scanner, test, build or manuscript render was run. The remaining unknown-variance Student construction is identified precisely below; the whole original article is not claimed complete.

## Files and frozen hashes

- handbook/parts/p15/neyman-confidence-constructions.tex — 17341 bytes; SHA256 21BBA9FA7FC59B526A8D16461BE902CD1171049A1883750187D86B28DBA2CF80.
- handbook/annex/p15/neyman-confidence-constructions.tex — 23987 bytes; SHA256 8EB486A9005BD91D0BA7EA9EA5DC92C61EC7C029A7FA5075C143E389411F88E6.
- This note is the third owned file; its hash is supplied in the final handoff.

All three paths were unused before creation. Prior testing/confidence files, other authors' work and shared integration files were preserved.

## Source identity and full reading

The unchanged source is J. Neyman, Outline of a Theory of Statistical Estimation Based on the Classical Theory of Probability, Philosophical Transactions of the Royal Society of London, Series A, Mathematical and Physical Sciences 236, no. 767 (30 August 1937), 333–380, DOI 10.1098/rsta.1937.0005.

Original: source/references/neyman-1937-confidence/Neyman-1937.pdf.

Acquisition URL recorded by the previous block: https://wwwusers.ts.infn.it/~milotti/Didattica/StatisticaAvanzata/Neyman_1937.pdf.

SHA256: 9D5657795AC8314E5C9DD7D4CA512132381533B9D11328F47EFFDB5F87ADF4B0. Size 7085828 bytes. Forty-nine physical pages: a JSTOR cover plus the 48 original pages; physical page = printed page minus 331.

The entire substantive original has now been read across this block and the preceding core block. This block read all of the previously unread introductory pp. 333–346 and the entire remaining pp. 356–380, including all displayed examples, comparison definitions, Proposition X and the references. The preceding block read the complete pp. 347–355 core. Required formula/figure pages were also personally inspected as images, including pp. 356–360, 362–363, 368–371 and 376–378. Source-only reading derivatives are in tmp/pdfs/p15-neyman-inference/ny37-rest-25.png through ny37-rest-49.png. The extraction neyman-1937.txt is a reading aid; the source scans resolved several substantive OCR ambiguities and original errors.

No new bibliography entry is needed: use the existing Neyman1937Confidence key. The full source acquisition remains separate from completion of all its historical presentations.

## Twelve delivered proof pairs

Every suffix below has body label thm:p15-neyman-SUFFIX:

| Suffix | Annex label | Supplied construction |
| --- | --- | --- |
| uniform-coverage | annex:p15.neyman.uniform.coverage | All three Example I systems, correct sum density/calibration, exact inversions, empty first-system sections and general n maximum law. |
| uniform-lengths | annex:p15.neyman.uniform.lengths | All interval lengths/expectations, the original two observed pairs and 400-trial scale schedule, exact tail probability and dependence of paired counts. |
| conditional-similarity | annex:p15.neyman.conditional.similarity | Propositions VIII–IX through specified coordinates, normalized conditional densities, measurable combination and explicit continuous-CDF sections of arbitrary size. |
| triangle-conditional | annex:p15.neyman.triangle.conditional | The literal two-parameter density/domain, normalization, radial failure probability, marginal and nuisance-free conditional law. |
| triangle-coverage | annex:p15.neyman.triangle.coverage | All fixed-placement b intervals, exact nuisance-uniform coverage and unique pointwise length minimum within that family. |
| switched-intervals | annex:p15.neyman.switched.intervals | Complete corrected exercise at the switch line, every ratio/alpha case, exact closed endpoints and both source length-crossing inequalities. |
| accuracy-duality | annex:p15.neyman.accuracy.duality | Original false-coverage shortest-system criterion, one-sided identities and its distinct integrated-length consequence. |
| uniform-shortest | annex:p15.neyman.uniform.shortest | Full cube-volume comparison against every exact-size measurable competitor, including randomized acceptance; explicit false-coverage function. |
| triangle-shortest | annex:p15.neyman.triangle.shortest | Full conditional-fiber minimum for every true scale and nuisance, exact comparison class and explicit false-coverage function. |
| regular-obstruction | annex:p15.neyman.regular.obstruction | Correct regular two-sided obstruction with L1 differentiability at the actual null, nonzero score, atomless equal-mass selections and complete contradiction. |
| normal-one-sided | annex:p15.neyman.normal.one.sided | Complete known-variance normal one-sided optima and a rigorous no-shortest-system counterexample, explicitly separate from source Example III. |
| unbiased-derivatives | annex:p15.neyman.unbiased.derivatives | Source global unbiasedness, its necessary derivative conditions, local curvature criterion and a concrete failure of the converse. |

## Substantive corrections applied directly

### Example I sum-strip calibration, pp. 357–358

Source equation (47) prints coverage 1-(Delta/theta)^2 for the band theta-Delta <= X1+X2 <= theta+Delta. The triangular sum density instead gives exactly 1-(1-Delta/theta)^2. Hence, writing q=sqrt(1-alpha), the correct half-width is (1-q)theta and the interval is

    [(x1+x2)/(2-q), (x1+x2)/q].

The corresponding length is 2(1-q)(x1+x2)/[q(2-q)]. The original printed interval happens to give the requested coverage at alpha=3/4, so the source's numerical examples conceal the general error. Equation (49) also has an invalid negative-denominator witness; the new nonempty-section proof uses the actual inverted inequalities. These corrections are in the active formulas and their full coverage proof.

### Endpoint and length comparisons, pp. 356–362

The source's strict sample inequalities and later closed interval formulas are not pointwise identical. The active acceptance sets include the relevant boundary points and therefore invert exactly to the declared closed intervals; the changes have probability zero under every fixed continuous law.

Equation (69)'s lower bound is weak, not strict: equality occurs at x1=x2. The active general ratio is (2-q)/4 <= D3/D2 < (2-q)/2, reducing to 3/8 <= D3/D2 < 3/4 in the printed numerical case.

### Switched-fiber exercise, pp. 369–370

As printed, the inverse can be half-open; for alpha<1/2 it can even be empty for an interval of observed ratios. The active construction makes the switch fiber x1=t/2 its full conditional support, and closes the other conditional endpoints. For each fixed candidate and every true law these are null modifications. The exact inverse is

    lower = max{x1+x2, x1+min(x2/alpha,x1)}
    upper = max{2x1, x1+x2/(1-alpha)}.

This gives a nonempty closed interval for every positive observation and every 0<alpha<1, including singleton cases. The original two length-crossing comparisons are proved with all cases retained.

### Conditional similarity, pp. 364–367

Algebraic independence is not by itself a proof of an a.e. globally invertible coordinate transformation with a valid Jacobian. The active theorem requires the actual specified coordinate representation and normalized joint-density factorization. It proves the nuisance-free conditional law and the integration step completely. When a residual real coordinate has a density, a continuous conditional cumulative transform explicitly supplies infinitely many measurable sections of probability alpha. Atomic residual laws do not automatically permit this nonrandomized choice. Example II uses the identity coordinates (X1,X2), so no unavailable transformation result is needed there.

### Regular obstruction and unbiasedness, pp. 372–378

The active obstruction states the analytic conditions actually used: L1 differentiability at the null parameter with nonzero derivative there. It does not infer a nonzero derivative at that parameter merely because the family changes elsewhere, and it does not turn an a.e. likelihood ordering into a pointwise assertion at an arbitrary region boundary. The proof uses two-sided probability derivatives and explicit equal-mass sets.

Neyman's global false-coverage maximum condition (124) and his local derivative/curvature conditions (126), (128), (129) are kept distinct. The latter alone do not imply a global maximum, as the supplied binary example proves. The unknown-variance optimum asserted in (130) has not been replaced by this necessary-condition result.

## Complete remaining-original inventory

| Original extent | Actual material | Disposition after this block |
| --- | --- | --- |
| I(a), pp. 333–343 | Sampling versus random experiments; measure-based probability; relative probabilities, including null-event discussion; two Bertrand chord constructions; random variables versus fixed constants; integral/elementary probability laws. | Entire text read. Exact historical reconstruction remains separate; existing P15 foundations are not automatically counted as this presentation. The original normalized-measure and null-conditioning qualifications require care. |
| I(b), pp. 343–346 | Bayes density formula and prior discussion; unbiased/best-unbiased point estimates; maximum likelihood; normal variance estimates with divisors n and n-1 and bias formula. | Read; separate source reconstruction remains. Vanishing bias alone must not be used as a proof of consistency. |
| I(c), pp. 346–347 | Transition from a unique estimate and its reported uncertainty to two interval endpoints. | Read; confidence meaning is supplied by prior core, but the complete historical point-estimator discussion is not claimed reconstructed here. |
| II(a)–(b), pp. 347–355 | Confidence coefficient, repeated-sampling interpretation, acceptance regions, Propositions I–VII and interval reconstruction. | Supplied by the prior hypothesis-tests-and-confidence pair with explicit measurability; preserved unchanged in this block. |
| II(c), pp. 356–362 | Uniform Example I, three systems, maximum distribution for general n, all numerical observations, 400-trial schedule and length comparisons. | Supplied in this block, with the direct calibration and endpoint corrections above. No empirical table exercise is claimed performed. |
| II(d), pp. 362–364 | Example II triangular density, cubic nuisance restriction and failure of radial acceptance bands. | Supplied completely. The nuisance range retained is -1 < theta1^3 theta2 <= 2. |
| II(e), pp. 364–367 | Propositions VIII–IX and conditional construction based on a sufficient system. | Used density/conditional construction supplied with explicit coordinate and measurability premises. The distinct general sufficiency theory referred to Neyman–Pearson 1936(b) remains an external source presentation. |
| II(f), pp. 367–370 | Example IIa fixed placements, exact interval lengths, best b, switched-placement exercise and crossing comparisons. | Supplied completely with the explicit null-boundary completion of the flawed exercise. |
| III(a), pp. 370–374 | Shortest systems defined by false coverage; acceptance comparison; claimed optima for Examples I/IIa; regular obstruction Proposition X. | Definitions and both optimum claims fully proved. A corrected regular obstruction with explicit sufficient analytic premises is proved; no unsupported original boundary argument remains in the active result. |
| III(b), pp. 374–376 | Best one-sided lower and upper estimates, their false-target directions and acceptance criteria. | Definitions and event/optimization bridge supplied. A separately identified known-variance normal example is complete. |
| III(c), pp. 376–377 | Original Example III: normal sample, unknown mean xi and unknown sigma, one-sided xbar +/- t s, with s^2=RSS/[n(n-1)], Fisher table P=2(1-alpha). | **Next substantive continuation.** Full Student pivot law, nuisance-uniform coverage and the actual optimality comparison class still require proof/source work. |
| III(d), pp. 377–378 | Global unbiasedness and local first/second derivative criteria; assertion that central Student intervals xbar +/- t s are short unbiased, Fisher table P=1-alpha. | Definitions, necessary conditions and distinction supplied. **The specific Student short-unbiased optimum remains dependent**, together with its required source machinery. |
| IV, pp. 378–380 | Summary, simultaneous-parameter extension remark and relationship to prior 1934/1935 presentations. | Read. Core summary reflected in supplied constructions; a distinct simultaneous confidence-region presentation and the earlier variants remain separate obligations. |
| V, p. 380 | Full reference list. | Read and used to identify the exact pending leads below. |

## Precise next continuation

Complete the source's normal unknown-variance Example III and the Student assertion at equation (130). For n>=2 the source's s is the estimated standard error, with s^2=sum(X_i-xbar)^2/[n(n-1)], not the sample variance. Required mathematical dependencies include the joint normal mean/residual decomposition, the Student pivot distribution and its quantiles, conditional similarity at the null across all sigma, and the comparison/completeness or equivalent argument establishing the exact one-sided and locally short-unbiased optimum. A named Student distribution or a coverage calculation alone does not complete the optimum.

The source cites Neyman–Pearson (1933) and (1936,a), Statistical Research Memoirs 1, pp. 1–37, for the one-sided theory; for the short-unbiased construction it additionally cites Neyman (1935,b), Bulletin de la Société Mathématique de France 63, pp. 248–266. The 1933 article is held from the prior block. The complete bodies and exact identities of the 1936(a) and 1935(b) references have not been acquired in this block. Do not infer the original optimum from the separate known-variance normal example.

## Integration and symbol intake

Body chapter label: sec:p15-neyman-confidence-constructions. Annex section label: sec:annex-p15-neyman-confidence-constructions. Route after the preceding hypothesis-tests-and-confidence unit. Reused active labels: thm:p15-confidence-test-inversion; thm:p15-neyman-interval-construction; thm:p15-neyman-pearson; def:p15-normal-law; thm:p15-normal-normalization. The normal affine transformation is the existing thm:p15-normal-sums.

New local roles include source confidence coefficient alpha; uniform minimum l, maximum L and maximum L_n, sum S, mean Xbar, beta=1-sqrt(alpha), q=sqrt(1-alpha), q_n; A_j^U and I_j^U; realized lengths D_2/D_3; conditional coordinates T,V, marginal m and density h; exact source theta1/theta2 and dimensionless rho=theta1^3 theta2; candidate t, true s and nuisance eta; placement b; A_b^T/I_b^T and I_*^T; switched acceptance A_sw^T and endpoints ell_sw/h_sw; coverage function Q_I; Lebesgue length operator len; L1 derivative g and score w in the obstruction; standard normal cumulative Phi and quantile z_alpha; common dominating measure nu for derivative integrals. Local q in the source's crossing-ray comparison is an observed ratio, explicitly bound there, rather than the earlier uniform cutoff.

The exact source remains unchanged. No bibliography or shared symbol file was edited; this note supplies the intake for root. Author completion of these twelve pairs does not grant independent acceptance.
