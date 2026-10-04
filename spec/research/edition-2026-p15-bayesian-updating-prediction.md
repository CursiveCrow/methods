# P15.39: Bayesian updating and prediction

## Completed authoring

The chapter supplies thirteen reciprocal statement/proof groups for
parent U3, with explicit links to U1 probability foundations, U4
confidence interpretation and U6 sensitivity. Its scope is the
posterior construction and its use for prediction and decisions.
The separate model-comparison author owns Bayes factors across
candidate model spaces and their point-null and prior-scale examples.

Active files:

- handbook/parts/p15/bayesian-updating-prediction.tex
- handbook/annex/p15/bayesian-updating-prediction.tex

Body: 22,825 bytes; SHA-256
4A696C6B5CEFEA6D5AB2DB2EC542B6B46D82B09E86A7AF94DC18ACE6E8110846.
Annex: 27,061 bytes; SHA-256
237AA39E8B3DFCD94855336EF5A83F10919EB057909336E03FB07E69BB9F3586.
These hashes identify the authoring snapshot before later cross-link edits.

Chapter: sec:p15-bayesian-updating-prediction.
Annex: sec:annex-p15-bayesian-updating-prediction.

## Sources and actual reading

Robert E. Kass and Adrian E. Raftery, Bayes Factors, Journal of the
American Statistical Association 90(430), 773-795 (June 1995),
DOI 10.1080/01621459.1995.10476572.
Canonical key: KassRaftery1995BayesFactors.

Held source: source/references/kass-raftery-bayes-factors-1995/kass-raftery-1995.pdf.
SHA-256: 3DA446B1AEA8E64801DBE17C0B727A71E7ACBBC304D4879532066C7139E50D86.
Size: 858,344 bytes. It has 24 physical pages: one JSTOR cover,
then the original printed pages 773-795. The cover and PDF metadata
date from April 10, 2007; the publisher's online date in 2012 is
also distinct from the actual 1995 publication.

Free university copy:
https://sites.stat.washington.edu/courses/stat527/s14/readings/KassRaftery_jasa1995.pdf

Publisher identity:
https://www.tandfonline.com/doi/abs/10.1080/01621459.1995.10476572

Root read Sections 3.1-3.2, 5.1-5.3, 6.1 and 8.2 with their
surrounding page context. Formula pages 776, 777 and 784 were
also read as images because several displayed equations were
missing from the text extraction. A truncated combined reading
was continued in separate calls until the assigned passages were
available. This is not a claim that root read the entire article.

The core posterior and predictive identities are the mathematical
starting point. All proofs here are independently worded editorial
derivations from the book's established probability foundations.
The synthetic inspection, credible-set, coordinate and selection
examples are not source experiments or reported participant data.
Their mathematical models are fully stated in the manuscript.

## Proof map

Each suffix below has a thm:p15- statement and annex:p15. proof:

| Suffix | Supplied result |
| --- | --- |
| bayes-posterior-kernel | Joint measure, marginal normalization, posterior kernel and all nonnegative/integrable function identities, including the exceptional observation set. |
| bayes-event-odds | Conditional-prior likelihoods, posterior odds multiplier, increase criterion and zero-likelihood/prior-null branches. |
| bayes-flag-calculation | Exact base-rate calculation, conditional independence versus a copied report, and prior-probability sensitivity. |
| bayes-sequential-update | Conditional likelihood products, normalized successive updates, telescoping predictive evidence and the specified permutation scope. |
| bayes-predictive-kernel | Joint future kernel, parameter-averaged prediction, total variance and future covariance. |
| bayes-beta-calculation | Full beta posterior and count/word likelihoods, predictive count, moments and worked numerical values. |
| bayes-normal-calculation | Full normal square completion, normalized data marginal including the residual factor, posterior and joint predictive variances. |
| bayes-transformation | Posterior pushforward and coherent coordinate transport, plus two different uniform-prior calculations. |
| bayes-reweighting | Exact posterior reweighting, sharp bounded-weight probability limits and contamination amplification. |
| bayes-coverage | Prior-average coverage identity, exact 95-percent posterior intervals with zero coverage at a specified parameter, and the normal posterior interval. |
| bayes-decision-rule | Measurable finite-action choice, integrated-risk minimization, value of information, binary loss threshold and squared-error estimation. |
| bayes-log-score | Full finite logarithmic-loss propriety argument, support-zero cases and sequential score identity. |
| bayes-stopping | Parameter-independent record factors, explicit randomized stopping mechanism, first-success beta update and two distinct selection experiments. |

## Definition and authoring decisions

The general posterior construction assumes a sigma-finite observation
measure and a jointly measurable normalized sampling density. It
constructs the kernel directly and therefore does not assert a general
regular conditional probability theorem for arbitrary measurable
spaces. Its extension from rectangles to data-dependent measurable
events uses the explicit Dynkin-system argument. Arbitrary null-point
values of density versions are not used as uniquely compelled inference.

Future means and variances exist almost everywhere under the posterior
when the integrated second moment is finite. Exceptional conditional
moment values receive the stated zero convention. Parameter uncertainty
is retained in predictions of several future observations.

The posterior normalizing constants are retained. The count and word
experiments have the same posterior only after their common constant
factor and fixed sample-size condition are made explicit. Uniformity
in different parameter coordinates is treated as a change of prior,
not as a violation of the pushforward identity.

The coverage result states exactly a prior average. The selected-only
and predesignated-trial examples have different sampling experiments
and prior specifications. No general claim that optional stopping is
harmless for frequentist errors is made. The squared-error result is
pointwise with a finite posterior second moment; the finite-action
measurable minimization result does not silently invoke an unrestricted
infinite-action selection theorem.

Root read the complete saved body and annex once, supplied the final
sigma-field, measurability and Dynkin-system details, and integrated
the body, annex, canonical key and P15.39 symbol roles. No independent
review, scanner, test, manuscript build, manuscript render or formal
admission check ran. Those later gates remain pending under the user's
all-changes-before-reviews instruction.

## Remaining wider source and edition scope

This chapter does not complete the Kass-Raftery article's five
applications, asymptotic integration and BIC methods, Monte Carlo
estimators, model-search algorithms, reference-prior procedures or
the separately cited original sources. Those presentations retain
their own requirements. Model comparison is separately authored.
General posterior asymptotics, nonparametric Bayesian methods,
elicitation, misspecification, statistical learning and the rest of
U3-U6 remain within the full approved manuscript objective.
