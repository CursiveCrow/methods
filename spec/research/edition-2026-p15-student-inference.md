# Student inference: author return for U4

## Completed assignment and saved scope

Authored the exact unknown-variance normal construction required for Neyman1937 Example III, printed pp. 376–377, and the Student short-unbiased assertion at equation (130), p. 378. The body and annex supply 13 complete result/proof pairs. They include the original one-sided similar-region comparison and the composite type-B local second-derivative comparison. A separately proved exponential-chord inequality establishes the stronger global UMPU conclusion; this conclusion is not inferred merely from zero first derivative or local curvature.

Owned new files:

- handbook/parts/p15/student-inference.tex
- handbook/annex/p15/student-inference.tex
- spec/research/edition-2026-p15-student-inference.md

The mathematical scope is every integer n >= 2, every real mean, every positive unknown variance, and every confidence coefficient 0 < alpha < 1. The comparison classes allow all Borel randomized tests, not just invariant, symmetric, or sample-mean/variance tests. One-sided optimality is among similar tests. The two-sided test dominates every stationary similar test, is globally unbiased, and hence is UMPU among all unbiased level tests.

One whole-batch author read-through of the actual body and annex was completed; its local definition corrections and the explicit single-sphere counterexample were saved. No independent review, scanner, test, build, or manuscript rendering was run. Source page images were used to read the primaries. This author return does not grant independent acceptance.

## Frozen source identities and read extents

### Neyman1937, unchanged original

J. Neyman, Outline of a Theory of Statistical Estimation Based on the Classical Theory of Probability, Philosophical Transactions of the Royal Society A 236, no. 767 (1937), 333–380. DOI 10.1098/rsta.1937.0005.

- Original: source/references/neyman-1937-confidence/Neyman-1937.pdf
- SHA256: 9D5657795AC8314E5C9DD7D4CA512132381533B9D11328F47EFFDB5F87ADF4B0
- Size: 7085828 bytes; 49 physical pages, including cover.
- Physical page = printed page minus 331.
- Direct acquisition URL: https://wwwusers.ts.infn.it/~milotti/Didattica/StatisticaAvanzata/Neyman_1937.pdf
- Existing key: Neyman1937Confidence.

This block reread the exact original images of pp. 376–378, including equations (121)–(130). The entire 49-page capture had already been read across the two preceding author blocks, as recorded in edition-2026-p15-neyman-confidence-constructions.md. The exact source target was frozen before authoring: unknown mean and variance, source standard-error divisor n(n-1), separate one-sided and central table tails, global unbiasedness definition, and the nuisance-uniform local first/second derivative criterion.

### Neyman–Pearson1933, unchanged original

J. Neyman and E. S. Pearson, On the Problem of the Most Efficient Tests of Statistical Hypotheses, Philosophical Transactions A 231, no. 702 (1933), 289–337. DOI 10.1098/rsta.1933.0009.

- Original: source/references/neyman-pearson-1933-tests/Neyman-Pearson-1933.pdf
- SHA256: 520D0B524AE336E0CB5C4DDD728FAEBFB86E4FFD987CB5B72C6B4DF16940F2F0
- Size: 6690382 bytes; 50 physical pages.
- Physical page = printed page minus 287.
- Direct acquisition URL: http://www.stats.org.uk/statistical-inference/NeymanPearson1933.pdf
- Existing key: NeymanPearson1933Tests.

Personally read the complete similar-region passage pp. 313–318, including its explicit restriction to similar tests, derivative/moment hypotheses, moment-determinacy qualification, Example 7 normal spheres, and conditional likelihood optimization. Then read the entire Example 8 on pp. 319–321 through its conclusion immediately before Example 9. The source is image-only; original-page images, not blank text extraction, supplied the reading.

Reading derivatives: tmp/pdfs/p15-student-inference/np33-similar-26.png through -31.png; np33-student-32.png through -34.png; np33-score-detail-29.png. The last image confirms the printed score denominator error in equation (94).

### Neyman1935, newly acquired complete original

J. Neyman, Sur la vérification des hypothèses statistiques composées, Bulletin de la Société Mathématique de France 63 (1935), 246–266. DOI 10.24033/bsmf.1236.

- Original: source/references/neyman-1935-composite/Neyman-1935-composite.pdf
- SHA256: 10CB8FD913AF66D717EBF3C6E8F78DB3FAD87F395E1B67479F1DF15993770D7F
- Size: 1562858 bytes; 22 physical pages, including Numdam cover.
- Physical page = printed page minus 244.
- Exact publisher/archive identity: https://numdam.org/articles/10.24033/bsmf.1236/
- Direct original PDF: https://numdam.org/item/10.24033/bsmf.1236.pdf
- Reading text: tmp/pdfs/p15-student-inference/neyman1935.txt
- Original-page images: tmp/pdfs/p15-student-inference/n35-07.png through n35-12.png.

The complete original body pp. 246–266 was read in extraction. The exact type-B conditions, affine-score hypotheses, nondegeneracy, polynomial-completeness hypothesis and outside-two-roots statement were also checked in the original images of pp. 252–256. Required proof extent: Sections 4–7, pp. 251–265; especially (8)–(10) for the local criterion, (15)–(17) for score derivatives, (29)–(31) for the conditional construction, the conditional size/score reductions through (57), and the second-derivative and constrained-selection argument through (71). Section 7 explicitly permits deriving the needed conditional equations separately rather than using its sufficient polynomial-completeness hypothesis. The present normal application does exactly that by a proved gamma-family Laplace-completeness argument.

The 1937 bibliography gives 248 as the first page. The unchanged original first page and Numdam identity establish 246. The original capture is retained unchanged; text and images are reading derivatives.

## Thirteen complete result/proof pairs

Each body suffix below follows thm:p15-student-.

| Body suffix | Exact annex label | Complete construction |
| --- | --- | --- |
| orthogonal | annex:p15.student.orthogonal | Explicit Householder map; orthogonal normal density; independence; squared-normal gamma law; residual chi-square law; positivity for n >= 2. |
| beta-direction | annex:p15.student.beta.direction | Gamma sum/ratio independence by iterated one-dimensional substitutions; beta coordinate law; fair sign; normalized sphere projection and radius/direction bridge. |
| law | annex:p15.student.law | Exact Student density integral and normalization; continuity, symmetry, quantiles; nuisance-free pivot and spherical-coordinate relation. |
| coverage | annex:p15.student.coverage | Both one-sided and central endpoints, exact coverage for all nuisance values, strict-test/closed-interval inversion at every sample, zero residuals and signed quantiles. |
| laplace-completeness | annex:p15.student.laplace.completeness | Signed weighted Laplace uniqueness from Bernstein approximation, continuous ramps and finite signed-measure uniqueness; gamma-family completeness. |
| null-fibers | annex:p15.student.null.fibers | Explicit joint null kernel; exact alternative likelihood tilt; its normalizer and radial density; all signs of mean shift and null radius cases. |
| score-fibers | annex:p15.student.score.fibers | Gaussian derivative domination; exact first/second scores; similarity iff conditional mass; stationary similarity iff conditional zero score; unbiasedness implies both; single-sphere counterexample to pointwise claims. |
| one-sided-optimal | annex:p15.student.one.sided.optimal | Both conditional likelihood inequalities and all-radius integration; UMP in the original similar class; precise lower/upper false-candidate confidence directions. |
| exponential-chord | annex:p15.student.exponential.chord | Every sign/cut case of the affine chord; fixed mass/score cancellation; separate strict global unbiasedness by cosh; quadratic maximum under mass constraint. |
| two-sided-optimal | annex:p15.student.two.sided.optimal | Integration for every nuisance variance and every nonzero mean shift; global UMPU; original type-B local second-derivative optimum and acceptance sign. |
| unbiased-confidence | annex:p15.student.unbiased.confidence | Exact coverage forced by unbiasedness, optimal false coverage, local confidence criterion, randomized inclusion realization and sampling quantifiers. |
| source-score-bridge | annex:p15.student.source.score.bridge | Literal 1935 parameter map, all affine derivatives, differentiation and Jacobian premises, exact conditional constraints/objective, and 1933 scale/statistic bridge. |
| worked-cases | annex:p15.student.worked.cases | Exact n=2 Cauchy and n=3 Student formulas, specified observations and intervals, absence of Cauchy mean, n=1 boundary, nonnormal dependence and changed coverage under a normal cutoff. |

## Direct mathematical and source corrections

1. **Three different scale conventions.** The 1937 s is e = sqrt(V/[n(n-1)]). This chapter's S is sqrt(V/(n-1)). The 1933 s is sqrt(V/n), and its z equals modern T/sqrt(n-1). The active formulas and proofs implement all three bridges.
2. **Printed score error.** Neyman–Pearson1933 equation (94), p. 316, prints 4 sigma^3 in the denominator of the squared-distance term. Differentiating its density (92) gives phi = -n/sigma + Q_m/sigma^3. That corrected formula agrees with (95). The annex derives it directly.
3. **Individual sphere sections.** The source phrase following (91), p. 316, is too strong if interpreted as a pointwise assertion for every radius and every measurable critical set. Null changes on a single sphere preserve similarity but change that sphere's angular mass. The active theorem states the correct Lebesgue-almost-everywhere equivalence and proves the counterexample, with a single null set adequate for every nuisance and alternative radius law.
4. **Two tails form a union.** The 1935 displayed outside-root inequalities (29), p. 256, must define the union of the lower and upper tails; treating the printed linking word as a logical conjunction would give an empty set when k1 < k2. Its acceptance-mass equations (30)–(31) determine the intended interval complement. The active formula is |Z| > c and its proof covers both tails.
5. **The source comparison class is explicit.** The one-sided theorem ranges over similar tests, exactly as the restriction on NP1933 p. 313 requires. It is not asserted to be UMP among every test satisfying only a level inequality. The two-sided UMPU statement is separately proved for every globally unbiased level test.
6. **Local and global criteria.** The original local criterion maximizes null second derivative of rejection power, or minimizes the corresponding acceptance derivative, with null size and first derivative constrained. The central interval satisfies this and is independently proved globally unbiased/optimal. Realized interval length is not the optimization objective of that criterion.
7. **Completeness premise.** No unproved unrestricted L1 orthogonal-polynomial completeness assertion is used. The source's exact needed conditional consequences are obtained from a signed Laplace uniqueness proof with integrability under every positive rate. Higher nuisance derivatives used in the source route are justified by Gaussian envelopes.
8. **Endpoints and domains.** n >= 2 and sigma > 0 are explicit. Tests use unscaled inequalities on V = 0, so closed inversions remain exact even when the signed one-sided quantile is negative. Sphere density is defined piecewise, including outside its support. No posterior probability is assigned from the coverage calculation.

No existing shared formula was edited. Prior notes that called Student Example III or (130) pending are superseded for this thirteen-pair mathematical component by this return; root owns their integration/status changes.

## Active prerequisite and notation intake

Read the actual body and annex premises used from:

- def:p15-normal-law; thm:p15-normal-normalization.
- def:p15-gamma-density; thm:p15-gamma-normalization; thm:p15-beta-gamma-convolution.
- def:p15-wce-spherical-measure; thm:p15-wce-spherical-area; thm:p15-wce-sphere-coordinate. In particular the full orthogonal-volume and Gaussian radius/direction proofs were read.
- thm:p15-feller-bernstein, with its actual uniform approximation proof.

The existing probability-law Laplace uniqueness premise in reflection-and-ballot-counts.tex was read as context; it was insufficient by itself for the signed weighted function needed here, so the full missing signed argument is supplied.

Chapter label: sec:p15-student-inference. Annex section: sec:annex-p15-student-inference. Integration should follow the normal/gamma/sphere/Bernstein foundations and the U4 hypothesis-testing/Neyman confidence units. No shared route was edited.

New local notation: n >= 2; nu=n-1; P_{mu,sigma}, E_{mu,sigma}; sample mean Xbar, residual sum V, sample SD S, standard error e; pivot T_m; chi-square law chi_k^2; Householder O and vectors b,d,v; omega_n as local alias of the existing sphere measure sigma_n; beta ratio and sphere density h_n; Student f_nu/F_nu/t_{nu,p}; confidence sets C_-, C_+, C_0; tests phi_m^+, phi_m^-, phi_m^0; alpha confidence and epsilon rejection; power beta_phi; Q_m,U_m,Z_m; alternative shift delta, tilt a(q), normalizer M(a); score sum H_m; angular functions A_phi,B_phi; cutoffs c_+,c; conditional selector r and affine chord ell_a; inclusion function a(x,m), locally distinct from the scalar tilt; source variance coordinate v and scores varphi_i,varphi_ij; source-only s_33,z_33.

## Bibliography intake

Add the following new entry to the shared bibliography during root integration:

    @article{Neyman1935CompositeHypotheses,
      author = {Neyman, Jerzy},
      title = {Sur la v{\'e}rification des hypoth{\`e}ses statistiques compos{\'e}es},
      journal = {Bulletin de la Soci{\'e}t{\'e} Math{\'e}matique de France},
      volume = {63},
      year = {1935},
      pages = {246--266},
      doi = {10.24033/bsmf.1236},
      url = {https://numdam.org/articles/10.24033/bsmf.1236/}
    }

The original prints J. Neyman; the named author is Jerzy Neyman. Existing Neyman1937Confidence and NeymanPearson1933Tests entries are reused. The new PDF's complete identity and unchanged hash are above.

## Exact remaining source boundary

There is no unsupplied mathematical prerequisite for this assigned Student construction, its original one-sided similar optimum, or its original composite type-B local optimum. The stronger global unbiased optimum has its own complete proof in this pair.

Whole-original source coverage remains broader:

- Neyman1937 I(a), pp. 333–343: its exact historical probability/relative-probability/null-conditioning and Bertrand constructions remain separately untranscribed.
- Neyman1937 I(b)–(c), pp. 343–347: its original Bayes, point estimation, maximum-likelihood and normal-variance bias discussion remains a distinct source presentation. The present residual law can now supply the exact normal variance distribution and bias premise; it does not itself transcribe those original sections.
- Neyman1937 II(e), pp. 364–367: the used conditional construction is supplied by the prior unit, but the separately referred general sufficiency source remains a distinct obligation.
- Neyman1937 III(c), pp. 376–377, and the specific Student assertion (130), p. 378: now supplied by this unit. The source summary IV, pp. 378–380, includes a separate simultaneous-parameter extension remark still requiring its own construction if admitted as a result.
- Neyman1935 Sections 4–7: complete original read and the full normal specialization supplied. Its general arbitrary-family type-B theorem, variant derivative relations and other historical discussion have not been counted as a completed separate presentation.
- Neyman–Pearson1933 Examples 7–8 are supplied at the exact normal/similar scope used here. The article's other examples and general routes are governed by the existing earlier inventory and are not made complete by this Student unit.
- Neyman–Pearson1936(a), Contributions to the Theory of Testing Statistical Hypotheses. I. Unbiassed Critical Regions of Type A and Type A1, Statistical Research Memoirs 1 (1936), 1–37: bibliographic identity found, but a complete freely readable body was not acquired in this block. Search leads included the reprint in Joint Statistical Papers, pp. 203–239; metadata/reprint references are not source-body acquisition. The distinct original type-A/A1 presentation remains pending.
- The distinct 1936 sufficiency source and Student1908 original presentation are not acquired or claimed reconstructed by this unit.

The next historical continuation of Neyman1937 itself is its remaining I(a)–(c) material and simultaneous confidence-region extension, coordinated with root's Bayesian work. A next optimality-source continuation should acquire the exact 1936(a) body before claiming its separate type-A/A1 proof.
