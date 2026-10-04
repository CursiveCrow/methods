# P15-U3/U6: Bayesian model comparison

Author block began 9 September 2026 at 00:11:49 UTC; bounded deadline
00:56:49 UTC. Owned: handbook/parts/p15/bayesian-model-comparison.tex,
matching annex, this note, and the disjoint symbols intake. Root owns
bayesian-updating-prediction.tex, shared routes and canonical records.
No earlier manuscript component was edited.

## Exact source identity and read scope

Robert E. Kass and Adrian E. Raftery, Bayes Factors, Journal of the American
Statistical Association 90(430), June 1995, 773-795.

Held primary:
source/references/kass-raftery-bayes-factors-1995/kass-raftery-1995.pdf

Verified SHA-256:
3DA446B1AEA8E64801DBE17C0B727A71E7ACBBC304D4879532066C7139E50D86

The PDF has the original 23 journal pages and one archive cover. The held
kass-raftery-1995.txt is a two-column extraction; its interrupted equations
were checked against actual source page images rather than guessed.
The archive cover identifies the journal, authors, volume/issue/date/pages.
Its 2007 archive transmission date is not a new article version.

Read the complete assigned sections:
- Section 3, including 3.1 and 3.2: printed 776-777, PDF pages 5-6.
  Definition, integration versus maximization, parameter priors, retained
  constants, numerator conventions, both descriptive evidence scales and
  predictive-log-score interpretation.
- Section 5, including 5.1, 5.2 and 5.3: printed 781-783, PDF pages 10-12.
  Prior elicitation, marginal versus null-conditional nuisance conventions,
  sensitivity, normal-class bounds, asymptotic nuisance qualifications,
  generalized-linear-model prior recipes and improper-prior proposals.
- Section 6 introduction and 6.1: printed 783-784, PDF pages 12-13.
  Finite posterior model weights, common-quantity averaging, mean, variance,
  expected utility and qualifications on selecting one model.
- Section 8.2: printed 789-790, PDF pages 18-19.
  Significance/posterior distinctions, likelihood-principle discussion,
  nonnested comparisons, multiple-model concerns, approximation-based
  thresholds, and the distinct role of goodness-of-fit checks.

All eight listed formula-bearing pages were read as source images.
Adjacent material visible on those pages was read as context only.
This is not a claim to have completed the whole 773-795 paper, its five
applications, or all primary works cited there. No new source was purchased
or acquired; the already held exact original was used.

Root supplies canonical key KassRaftery1995BayesFactors. No duplicate
bibliography intake was created.

## Manuscript scope and explicit domains

The chapter supplies the requested exact model-comparison core:
a finite family of models, proper within-model priors, a common standard
Borel observation space with sigma-finite reference measure, jointly
measurable likelihood densities normalized for every parameter, and declared
model prior masses (including zero masses). Marginal likelihoods may be
infinite only on reference-null sets; all pointwise weight and factor
formulas use the declared positive finite comparison domain.

Root's single-model posterior theorem is used through its actual agreed
interface:
- chapter sec:p15-bayesian-updating-prediction;
- definition def:p15-bayes-experiment;
- theorem thm:p15-bayes-posterior-kernel.

The tagged finite model/parameter union meets that interface. Model-weight
identities are also verified directly against the joint measure. Defaults on
predictive-null exceptional sets are explicit, and a zero model prior is
not silently divided by or revived. A parameter point null and an atom of
prior model mass remain different from a singleton inside a continuous
alternative prior.

Other actual interfaces read before writing:
- thm:p15-tonelli and thm:p15-fubini, product-measures.tex;
- thm:p15-radon-nikodym and thm:p15-density-calculus, radon-nikodym.tex;
- def:p15-probability-kernel and thm:p15-kernel-expectation,
  regular-conditional-laws.tex;
- def:p15-normal-law, thm:p15-normal-normalization and
  thm:p15-normal-sums, convolution-gamma-normal.tex;
- thm:p15-conditional-variance and the surrounding conditional-mean
  interfaces, conditional-expectation.tex.
The chapter provides its own needed square completion, kernel integral
extension, density comparisons and mixture calculations rather than leaving
them as source sketches.

## Exact reciprocal proof map

Each body result points to exactly one complete annexitem with the same
body back-reference:

1. thm:p15-model-posterior-odds /
   annex:p15.model-posterior-odds.
   Tonelli normalization, predictive-full domain, tagged model posterior,
   prior-zero models, odds, reciprocal factors and predictive log-density
   difference. Source Sections 3.1-3.2 and 6.1, equations (1), (2), (16).

2. thm:p15-model-density-invariance /
   annex:p15.model-density-invariance.
   Jointly measurable density-version changes; intrinsic domination by the
   equal-weight model predictive mixture Q_*; full common-reference-measure
   invariance almost everywhere; explicit pointwise compatible versions;
   transported parameter and observation coordinates. A singleton-modified
   uniform density proves why arbitrary pointwise versions cannot be ignored.
   This is a handbook measure-level foundation for the source's density ratios.

3. thm:p15-nuisance-integration /
   annex:p15.nuisance-integration.
   Declared proper conditional nuisance-prior kernel Lambda_k, nonnegative
   integral extension from rectangles by a pi-lambda argument, joint
   measurability, and a fully calculated profile-likelihood counterexample.
   Source Sections 3.1 and 5.1.

4. thm:p15-normal-point-null-factor /
   annex:p15.normal-point-null-factor.
   General normal alternative center and proper positive variance; exact
   marginal likelihood and factor including constants; full-sample residual
   factor and reduction to a sample mean at known common variance.
   Source's point-null and normal-prior sensitivity setting, Sections 5.1-5.2.

5. thm:p15-normal-factor-sensitivity /
   annex:p15.normal-factor-sensitivity.
   Diffuse and collapsing-prior limits, exact centered-normal maximum,
   proper scale-mixture bound, arbitrary-prior likelihood bound, and the
   distinction between fixed standardized and fixed nonzero-departure
   increasing-sample paths. The numerical table is completely calculated.
   Source Section 5.2 normal-class bound and Sections 5.1/8.2 distinctions.

6. thm:p15-model-average-moments /
   annex:p15.model-average-moments.
   Kernel normalization and signed integration under explicit integrability;
   both forms of total posterior variance; positive-weight second moments;
   two examples showing that a selected model variance can lie on either
   side of the mixture variance. Source Section 6.1, equations (17)-(19).

7. thm:p15-model-label-refinement /
   annex:p15.model-label-refinement.
   Prior-odds sensitivity, invariance under a mass-preserving split of
   duplicate labels and common-quantity kernels, and changed posterior
   support under a fresh uniform prior on duplicated labels. This is a
   handbook clarification of model-space prior choice in Section 6.1.

8. thm:p15-improper-model-priors /
   annex:p15.improper-model-priors.
   Arbitrary constant cancellation within a proper parameter posterior but
   not across model integrals; infinite integrated predictive mass; limited
   common-nuisance-constant cancellation; flat-normal and proper uniform
   approximation examples; explicit proper-prior null-fiber version example.
   Source Sections 5.1 and 5.3.

9. thm:p15-finite-model-evaluation /
   annex:p15.finite-model-evaluation.
   Full finite sums, positive common-factor cancellation, failure for
   model-dependent factors, exact exponential rescaling with zero terms
   omitted, binomial count example and different-normal-variance constants.
   Source Section 3.1's instruction to retain likelihood constants.

10. thm:p15-normal-significance-comparison /
    annex:p15.normal-significance-comparison.
    Exact uniform null-tail calibration in the continuous normal model,
    fixed z=2 versus changing proper priors, and the fixed-z posterior-null
    limit. Source Section 8.2; no significance/posterior conflation.

## Worked values and author corrections

The normal table holds z=2 and equal model masses fixed. Its exact factors
for r=1,3,9,99,999 are sqrt(2)e^-1, 2e^-1.5,
sqrt(10)e^-1.8, 10e^-1.98 and sqrt(1000)e^-1.998.
The resulting null probabilities range from approximately .3086 to .8109
although the two-sided null-tail probability stays approximately .0455.

The profile example uses a proper two-point nuisance prior: the integrated
alternative success probability is .5 versus a null .6, giving B_10=5/6.
The profile values .9 at both outcomes sum to 1.8 and give a different
ratio 3/2. It is not relabeled as a normalized probability model.

The finite binomial example retains its coefficient two, giving
m_0=.5, m_1=.32, B_10=16/25 and alternative posterior mass 16/41.
Canceling this common coefficient is justified. The normal variance
comparison at zero needs its model-dependent constants and gives factor
two, rather than the spurious one from exponential kernels alone.

Model averaging gives variance five for equally weighted N(-2,1), N(2,1).
The contrasting variance-100/point-mass example gives mixture variance
50, so the text does not assert that every selected model understates it.
Strict understatement from omitting the between-model term is qualified by
different positive-weight means.

The duplicated-label example preserves evidence and changes posterior
support only through group prior mass. The text does not call the changed
prior itself new data evidence. Arbitrary density versions and duplicate
marginal laws receive their almost-everywhere qualifications explicitly.
The nuisance prior kernel Lambda_k is kept distinct from model-averaging R_k.

The source's Section 5.2 text describes symmetric unimodal priors with the
word nondecreasing in distance from the center. That wording is not imported
as a definition: an integrable nonnegative density cannot be positive and
nondecreasing along an unbounded outward tail. The current component uses
the explicit normal density instead. A future full treatment of the broader
symmetric-unimodal bound must state the correct shape premise and read the
cited original proof.

## Continuation obligations and what is not claimed

The requested exact model-comparison derivations and examples are supplied.
The following distinct source developments remain separate writing:
Laplace and Schwarz/BIC approximation hypotheses and error terms (Section 4),
the general asymptotic nuisance-orthogonality comparison and generalized-
linear-model prior recipes (Section 5.2), bounds for broader prior classes,
imaginary/partial/intrinsic/fractional training-sample constructions (5.3),
Occam's window and large-model-space algorithms (6.2-6.5), the five original
applications and their data, and the approximation-derived t thresholds in
8.2. Reading their summaries does not constitute writing their full proofs.
The exact normal limits are not claimed to establish those general results.

Root separately owns single-model conjugacy, posterior prediction, sequential
update and stopping-mechanism conditions, credible sets and loss. The
prequential interpretation of Section 3.2 is linked to that chapter, while
the present chapter proves the model predictive log-density difference.

## Handoff and author read-back

New notation is supplied in
handbook/registry/symbols-intake-p15-bayesian-model-comparison.csv.
Merge it by its declared local scopes; Q_*, r_k, the scalar normal ratio r,
the conditional nuisance kernel Lambda_k and posterior kernels R_k have
different typed roles. The single source key is root-owned.

The complete actual body and all ten annex proofs were read after the
authoring batch. Domain, null-set, nuisance-kernel, finite-likelihood and
variance-comparison qualifications were corrected directly. The source note
and symbols intake were also read. No independent review, manuscript scanner,
test, build or manuscript render was performed. Source-only images were used
to read the held original. The research/PDF skills guided provenance and
source reading; a bounded retrieval delegation failed at the agent-thread
limit, and no extra agent ran.

## Final integration-interface correction, 9 September 2026

At root's request, def:p15-model-comparison-experiment now explicitly requires
finite jointly measurable nonnegative likelihood density versions, normalized
for every parameter. This matches def:p15-bayes-experiment and
thm:p15-bayes-posterior-kernel exactly. Marginal likelihoods can still be
infinite on reference-null data sets, and the existing positive-finite
comparison domain and default posterior weights remain necessary.
The direct definition edit is authoring integration, not an independent review.

Updated body SHA-256:
01F3E46555141A6F92FE382CAA70B4E4EEC75D316E904482F08737F35DDD7FF2

Unchanged annex SHA-256:
0E108D6C615D7D21C0D807AC45EAF2CAF75D94F3D2E98580287EA757E6156160

The held Kass--Raftery primary hash remains
3DA446B1AEA8E64801DBE17C0B727A71E7ACBBC304D4879532066C7139E50D86.
