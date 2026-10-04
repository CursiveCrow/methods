# P15 / U4: hypothesis tests and confidence sets

Author block: 2026-09-09 00:12:14 UTC, with a 00:57:14 UTC deadline. The assigned construction is complete. Twelve statement/proof pairs are saved, and their actual LaTeX received one whole-batch author read-through. The earlier checkpoint's provisional count of thirteen was corrected to twelve after the related components were paired together. No independent review, scanner, test, manuscript build or manuscript render was run. No usage-limit failure occurred.

The preceding P17 work was left to root after root confirmed that its newer files, source note and integration were already complete. This U4 block changed only the assigned new P15 files and the two disjoint source-capture directories.

## Delivered files

- handbook/parts/p15/hypothesis-tests-and-confidence.tex — 17219 bytes; SHA256 13F992C0A0853E04F35591CAF86D720E0CDBAAB059D4EC89C11B64633E9EC5FC.
- handbook/annex/p15/hypothesis-tests-and-confidence.tex — 23574 bytes; SHA256 7F287F0B2689415EF81B2104E87A0C9480D84D436969D403678C88E6883EDCCB.
- This source and integration note is the third assigned file. Its hash is supplied in the final return.

The three target paths were unused before creation. Shared drivers, bibliography, symbols and other authors' chapters were preserved.

## Primary acquisition and exact read extent

### Neyman and Pearson, 1933

J. Neyman and E. S. Pearson, On the Problem of the Most Efficient Tests of Statistical Hypotheses, Philosophical Transactions of the Royal Society of London, Series A, volume 231, no. 702, pp. 289–337. Published 16 February 1933; received 31 August 1932 and read 10 November 1932, as shown on the original first page. DOI 10.1098/rsta.1933.0009.

- Original capture: source/references/neyman-pearson-1933-tests/Neyman-Pearson-1933.pdf.
- Exact acquisition URL: http://www.stats.org.uk/statistical-inference/NeymanPearson1933.pdf.
- The HTTPS www and bare-host endpoints both failed certificate-name validation. The public HTTP endpoint returned the complete original scan; no credentials or private data were transmitted and certificate verification was not disabled.
- SHA256: 520D0B524AE336E0CB5C4DDD728FAEBFB86E4FFD987CB5B72C6B4DF16940F2F0.
- Size: 6690382 bytes. Fifty physical pages: one JSTOR cover plus original printed pp. 289–337. Physical page = printed page minus 287.
- Identity, contents and publication information were read on printed p. 289. The complete relevant definitions and discussion on pp. 293–298, the entire boundary-variation construction pp. 298–300, and the set-difference power comparison through equation (28) on p. 301 were personally read as source images. The continuation pp. 301–302 concerning likelihood envelopes and the start of the normal example was also read to identify the exact boundary.
- The PDF is image-only; its blank text extraction was not treated as source evidence. Readable source-page images are tmp/pdfs/p15-neyman-inference/np33-06.png through np33-15.png, with np33-02.png for identity.

The claimed source reconstruction is the simple-hypothesis optimization core, its density ordering, the two-error distinction and the local variation argument under explicit regularity assumptions. The dominated randomized formulation is an expressly supplied generalization with its own full proof; it is not presented as the literal 1933 syntax. Neither the complete 49-page article nor every illustrative/likelihood-envelope construction is claimed finished.

### Neyman, 1937

J. Neyman, Outline of a Theory of Statistical Estimation Based on the Classical Theory of Probability, Philosophical Transactions of the Royal Society of London, Series A, Mathematical and Physical Sciences, volume 236, no. 767, pp. 333–380. Published 30 August 1937; received 20 November 1936 and read 17 June 1937. DOI 10.1098/rsta.1937.0005.

- Original capture: source/references/neyman-1937-confidence/Neyman-1937.pdf.
- Exact acquisition URL: https://wwwusers.ts.infn.it/~milotti/Didattica/StatisticaAvanzata/Neyman_1937.pdf.
- SHA256: 9D5657795AC8314E5C9DD7D4CA512132381533B9D11328F47EFFDB5F87ADF4B0.
- Size: 7085828 bytes. Forty-nine physical pages: one JSTOR cover plus original pp. 333–380. Physical page = printed page minus 331.
- Identity and contents were read; the assigned extent is the complete confidence problem and sampling interpretation on pp. 347–350 and the full acceptance-region construction on pp. 350–355, including Figure 1, Propositions I–VII, both corollaries, all four region conditions and every finite/infinite or singleton endpoint case.
- Readable extraction: tmp/pdfs/p15-neyman-inference/neyman-1937.txt. Source images ny37-16.png through ny37-24.png were prepared; key formula and endpoint pages were personally inspected as images, including printed pp. 350, 354 and 355.

The source's confidence coefficient is alpha; the active statistical chapter explicitly calls this q or 1-alpha, while alpha denotes testing size. The probability identity retains every nuisance parameter through the general target map tau. Endpoint measurability is made an explicit hypothesis instead of assuming that an arbitrary single-valued function is measurable.

## Complete proof-pair map

| Body label | Annex label | Closed content |
| --- | --- | --- |
| thm:p15-test-randomization | annex:p15.test.randomization | Measurable product-space rejection and exact expectation, including values zero and one. |
| thm:p15-likelihood-threshold | annex:p15.likelihood.threshold | Finite threshold existence, tail continuity, threshold atoms, c=0 and size endpoints. |
| thm:p15-neyman-pearson | annex:p15.neyman.pearson | Global dominated comparison, all equality/converse conditions, common zero sets, singular mass and alpha=0/1. |
| thm:p15-neyman-pearson-variation | annex:p15.neyman.pearson.variation | Full local endpoint variation, dominated derivative, bump-function necessity and reversed orientation. |
| thm:p15-binomial-most-powerful | annex:p15.binomial.most.powerful | Likelihood ordering, composite-null coupling, one-sided UMP including alternative p=1, exact randomized arithmetic and no two-sided UMP. |
| thm:p15-discrete-p-values | annex:p15.discrete.p.values | Inclusive-tail validity, strict conservatism, randomized uniformity, lower tails and the binomial equivalence. |
| thm:p15-confidence-test-inversion | annex:p15.confidence.test.inversion | Joint measurability, nuisance-uniform inversion, converse tests and measurable integration of auxiliary randomization. |
| thm:p15-neyman-interval-construction | annex:p15.neyman.interval.construction | All membership directions, closed order-convex sections, singleton/infinite endpoints, rational-cut measurability and the converse. |
| thm:p15-binomial-tail-roots | annex:p15.binomial.tail.roots | Both telescoping derivatives, unique roots, nonempty intervals and exact endpoint formulas. |
| thm:p15-binomial-confidence-coverage | annex:p15.binomial.confidence.coverage | Strict-tail inversion with closed endpoints, all p=0/1 and k=0/n cases, exact finite coverage and worked intervals. |
| thm:p15-binomial-beta-quantiles | annex:p15.binomial.beta.quantiles | Beta/binomial identities from derivative and normalization, unique quantiles and exclusion of zero shapes. |
| thm:p15-confidence-credibility-boundary | annex:p15.confidence.credibility.boundary | Coverage frequencies, distinct joint prior model, explicit posterior content and zero frequentist coverage of central credible sets. |

## Exact worked calculations and corrections

The finite binomial test uses n=4, p0=1/2, alpha=1/10. It rejects count 4 and rejects count 3 with probability 3/20. Size is 1/10. Power at p1=3/4 is 243/640 and type-II error is 397/640. Without boundary randomization, rejecting only count 4 gives size 1/16 and power 81/256. The discrete randomized p-value at count 3 is 1/16+U/4 and reproduces the same 3/20 decision probability.

At n=2 and confidence coefficient 9/10, count 1 gives [1-sqrt(19/20), sqrt(19/20)]. All count intervals contain p=1/2, so actual coverage there is 1. At n=4 and count zero, the interval is [0, 1-20^(-1/4)].

With an explicitly separate uniform prior, the latter interval has posterior probability 1-20^(-5/4), not 9/10. The central beta posterior intervals have probability 9/10 conditional on every count, but sampling coverage zero at p=0 and also at every positive p below the minimum of their finitely many positive lower endpoints.

The active Neyman–Pearson theorem uses a.e. strict-region conditions and allows arbitrary measurable decisions on a positive-mass tie region. It does not preserve an overly strict region-uniqueness reading. The source's smooth boundary derivation is retained only with actual stationary variation assumptions; global optimality is proved separately by the sign integral.

The binomial confidence set accepts equality at each root. Therefore its exact inverted rejection condition uses tail probability strictly less than alpha/2. A weak less-than-or-equal rejection condition would instead remove the corresponding parameter endpoints. Finite-sample validity is distinguished explicitly from equality to the nominal coverage.

The binomial tail inversion is a proved application of the source acceptance construction and the already present binomial/beta probability calculus. This handoff does not claim acquisition or full reconstruction of the distinct Clopper–Pearson 1934 historical presentation.

## Bibliography intake for root

The two keys used in the body are new proposed entries:

    @article{NeymanPearson1933Tests,
      author = {Neyman, J. and Pearson, E. S.},
      title = {On the Problem of the Most Efficient Tests of Statistical Hypotheses},
      journaltitle = {Philosophical Transactions of the Royal Society of London. Series A},
      volume = {231},
      number = {702},
      pages = {289--337},
      date = {1933-02-16},
      doi = {10.1098/rsta.1933.0009},
      url = {http://www.stats.org.uk/statistical-inference/NeymanPearson1933.pdf}
    }

    @article{Neyman1937Confidence,
      author = {Neyman, J.},
      title = {Outline of a Theory of Statistical Estimation Based on the Classical Theory of Probability},
      journaltitle = {Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences},
      volume = {236},
      number = {767},
      pages = {333--380},
      date = {1937-08-30},
      doi = {10.1098/rsta.1937.0005},
      url = {https://wwwusers.ts.infn.it/~milotti/Didattica/StatisticaAvanzata/Neyman_1937.pdf}
    }

## Symbol and route intake

Route the body in P15 under U4 and the matching annex after the probability foundations. Body chapter label: sec:p15-hypothesis-tests-confidence. Annex section label: sec:annex-p15-hypothesis-tests-confidence.

Chapter-local roles: sample space mathsf X / sigma-field mathscr X; data X; parameter Theta, null Theta_0 and alternative Theta_1; sampling laws P_theta and expectations E_theta; test phi, competitor psi, optimal phi-star; power beta_phi(theta); significance alpha; uniform auxiliary U and its probability measure lambda_01; common dominating measure mu and densities f_0/f_1; extended ratio L; threshold c and tie probability gamma; binomial count K, sample size n, parameter p, baseline p_0, b_n,p(k); p-value pi and randomized pi_r; target map tau into Lambda, possible target t, acceptance A_t, confidence set C(x,u), section S(x), endpoints ell/u, and exact confidence coefficient q; binomial half-tail d=alpha/2, upper and lower tails T_n,p/F_n,p, limits ell_n/u_n; beta quantile Q_a,b and normalized incomplete beta integral I_p(a,b).

The smooth-variation lemma separately declares its local dimension d, boundary functions ell/q, perturbation eta and scalar s, source multiplier k and integrand h=f_0-k f_1. The confidence-frequency proof's q is the actual coverage probability. These roles are local and should not be silently combined with the historical sources' alternative alpha conventions.

Active external dependency labels used directly: def:p15-beta-integral and thm:p15-beta-gamma-convolution in convolution-gamma-normal.tex. The independent-uniform product construction, finite integration, dominated convergence and elementary moment bounds use the existing P15 probability foundations. The conditional prior comparison is derived directly from its joint density, so it does not depend on unfinished or changing Bayesian-updating labels.

## Remaining historical source material

None in the concrete U4 target assigned for this block. The complete NP 1933 article remains broader: the likelihood-envelope discussion at the end of III(a), the normal and rectangular examples in III(b), and the composite/similar-region optimality constructions in IV–V are separate source obligations. Neyman 1937 Sections I beyond the used setup, II(c) onward examples/sufficient-statistic constructions, and III shortest, one-sided and unbiased interval optimization likewise remain separate. No full-article admission is claimed.

Root owns shared integration, bibliographic merging, symbol registration, proof-pair records and the eventual consolidated reviews.
