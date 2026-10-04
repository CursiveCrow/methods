# Measurement uncertainty: author source and completion record

Date: 9 September 2026.
Unit: ED26-SCI-JCGM2008-001.
Owner: scientific-reasoning author, under the resumed authoring batch contract.

The assigned body, proof annex and distinct bibliography/symbol intakes are
written. Twelve mathematical results have complete corresponding annex proofs.
The four mapped components are represented in the actual treatment. This is an
author completion record, not independent source, topic or publication admission.
No build, manuscript render or review wave was run.

## Files for lead integration

- handbook/parts/p15/measurement-uncertainty.tex
- handbook/annex/p15/measurement-uncertainty.tex
- handbook/bib/intake-p15-measurement-uncertainty.bib
- handbook/registry/symbols-intake-p15-measurement-uncertainty.csv

The lead owns the part/annex drivers, canonical bibliography and canonical
symbol registry. None of those shared files was changed. The bibliography
intake contains two complete entries. The symbol intake contains 18 typed rows.
The body and annex remain available for the lead's routing decision.

| File | SHA-256 |
| --- | --- |
| Body | 1BFA231AD647D9C101FA170CADB425DEA4B96C4371496312CA5CC29B605CC7EA |
| Annex | AA182339D31113D1D1F5ABDD01A62A6B947A8FE61EB0C8E14CCD7F59890E692F |
| Bibliography intake | 8038E24C1DA7A1F972101EA0D89F7C4706FBF8101B4B0F6C6CE6F9BE7A979A6C |
| Symbol intake | E5DDC1A8280FD589D50C60F8C332AB32D1B82FBC7719C55FBFAED09F7D16053A |

## Exact sources acquired

All paths below are relative to
source/references/jcgm-measurement-uncertainty/.

| Artifact | Identity and extent | SHA-256 |
| --- | --- | --- |
| jcgm-100-2008-e.pdf | Official JCGM 100:2008(E), GUM 1995 with minor corrections; 134 physical pages | 41BBF068FBC0D7986C98691B2D1AF6680CB3044F6A1A89B3560933ED9EF9626C |
| jcgm-100-amd1-2026.pdf | JCGM 100:2008/Amd.1:2026, first edition; five physical pages, one substantive amendment page | CE50A6BA8B5A338D81082494E81988F137C89D951C8DCB647A1FC856B7B5F809 |
| jcgm-100-2008-e.txt | Layout text extracted from the held 2008 PDF | 5E1D04CB072201ACDB09425A4EFE5FA5B7513D0DC62B7D40FDF17CBE682A0E02 |
| jcgm-100-amd1-2026.txt | Layout text extracted from the held amendment | C329AAB867018DE51E9941936A5B64415E2EC5C061C7FEE3176BB9E89BA8FD53 |
| amendment-crossref-2026-09-09.json | Publisher-deposited DOI record fetched from Crossref | 3B29720C2FC4D63519435D2EF140A1B5D2024DB43C2626D08DC5436299DECDE2 |

Primary acquisition addresses:

- [JCGM 100:2008(E)](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf)
- [Official JCGM publication index](https://www.bipm.org/en/committees/jc/jcgm/publications)
- [Amendment identity](https://www.bipm.org/en/doi/10.59161/JCGM100-Amd-2026)
- [Actual amendment PDF](https://www.bipm.org/documents/20126/2071204/JCGM_100_Amd1_2026.pdf/18b8a72a-6caf-69e8-8bbd-dd13056a4a84?download=true&t=1785763281319&version=1.6)
- [Publisher DOI metadata](https://api.crossref.org/works/10.59161/PPDI3267)

No paid acquisition or access circumvention was used.

## Amendment date and correction scope

The publisher-deposited Crossref record explicitly gives 2026-06-30 as
published-online, issued and published. The DOI record was created
2026-07-21 and updated/indexed in August. The PDF creation date is
30 June 2026 and its modification date is 21 July 2026. These are different
fields; the bibliography uses the publisher's publication date, not a
filesystem timestamp. The amendment is within the 7 September 2026 cutoff.

The actual substantive page was read completely. It:

1. Adds Note 1 to 4.1.4: significant nonlinearity requires attention to the
   output estimate, using Monte Carlo propagation or higher Taylor terms.
   Its displayed independent-normal mean correction is one half of the sum
   of diagonal second derivatives times input variances.
2. Revises H.1.7 to require checking both the length estimate and its
   combined standard uncertainty; the indicated mean correction for that
   example is zero, while two variance terms remain.
3. Adds JCGM 101:2008 to the bibliography.

The complete amendment body has been incorporated at its relevant scope.
JCGM 101 is an identified referral of that amendment, not a newly claimed
complete Monte Carlo treatment. This chapter does not claim current normative
conformity of any real measurement.

## Reading completed

The selected 2008 text was read from the actual held source:

- Sections 2–8, printed pp. 2–27.
- Annex D, printed pp. 49–53, including its conceptual figures.
- Annex E.3, printed pp. 55–57.
- H.1, printed pp. 79–85, including all contributing inputs and second-order
  terms.
- H.2, printed pp. 85–89, including Tables H.2–H.5 and both data-analysis
  approaches.
- The actual G.3–G.4 Student/effective-degrees-of-freedom material used as the
  source dependency of H.1.6.

The two core input-distribution illustrations and two Annex D illustrations
were inspected directly as source images:
source-figures-028.png, source-figures-029.png,
source-annex-d-064.png and source-annex-d-065.png.
These are source-reading evidence, not rendered manuscript pages.
The active text reconstructs their mathematical/conceptual content with
formulas, data, distribution comparisons and the observed/latent distinction;
it does not reproduce the source artwork.

The research and PDF skills were read. PDF work was read-only acquisition and
inspection of primary sources; no PDF was authored or edited. The source
figures were inspected because the PDF skill's reading workflow and the source
content required their visual information. The user's no-per-edit manuscript
render instruction remained in force.

## Component completion

| Mapped component | Actual body coverage | Mathematical support |
| --- | --- | --- |
| C01: measurand/model, error/correction/uncertainty | Target, realization, reference conditions, model, input information, sources of uncertainty, shared corrections and reporting | Explicit model and source-attributed recommendations; no invented theorem for a standard's normative provision |
| C02: covariance propagation and first-order boundary | Scalar and vector affine propagation, covariance estimates, perfect dependence, product sensitivities, common offsets/scales, Taylor remainder, Gaussian next-order terms, H.1 and H.2 | Twelve named body/annex pairs, with complete proofs for the displayed mathematical assertions |
| C03: Type A/Type B distinction | Repeated observations, pooled information, fitted/time-correlated boundaries, certificate conversions, uniform/triangular/trapezoidal/arcsine models, asymmetric fixed-mean entropy model and double-counting prevention | Sample covariance and bounded-distribution proofs; entropy optimum derived directly |
| C04: coverage and nonlinear failure | Normal/non-normal coverage, exact Student interface, moment-matching basis of Welch–Satterthwaite, uncertain Type B reliability, zero-gradient example, nonlinear averaging and reporting | Explicit probability calculations, finite-moment bounds and separately qualified approximation |

The actual theorem/proof pairs are:

1. measurement-sample-covariance / measurement.sample-covariance
2. measurement-bounded-distributions / measurement.bounded-distributions
3. measurement-asymmetric-model / measurement.asymmetric-model
4. measurement-affine-covariance / measurement.affine-covariance
5. measurement-common-correction / measurement.common-correction
6. measurement-taylor-bound / measurement.taylor-bound
7. measurement-gaussian-expansion / measurement.gaussian-expansion
8. measurement-coverage-models / measurement.coverage-models
9. measurement-effective-df / measurement.effective-df
10. measurement-gauge-products / measurement.gauge-products
11. measurement-impedance-jacobian / measurement.impedance-jacobian
12. measurement-transform-average / measurement.transform-average

The body prefixes are thm:p15- and annex prefixes are annex:p15.
No hbproof wrapper, sketched tag or placeholder bibliography record was used.

## Mathematical qualifications and direct corrections

These decisions are recorded here so the active reader text can state the
correct result directly.

- Covariance propagation is exact for affine functions. For nonlinear
  functions it is explicitly a surrogate calculation with a separately
  proved remainder bound. A nonlinear plug-in estimate is not silently
  identified with the expectation of the transformed input.
- E.3.1's moment-characterization note is not used as a general determinacy
  theorem. The body states the actual limit and points to the existing
  lognormal moment-indeterminacy family.
- A uniform law is a modelling assumption, not a logical consequence of
  support bounds. With an asymmetric support interval and fixed mean, the
  guide's rectangular variance approximation is not treated as the variance
  of a uniform distribution retaining that different mean. The correct
  exponential-tilt maximum-entropy alternative has a full proof.
- The sign in the fully positively correlated scalar expression is handled
  with an absolute value before taking a standard deviation.
- Gaussian higher-order propagation states independence explicitly and
  retains both squared-Hessian and gradient–third-derivative contributions.
  The exact polynomial theorem includes the cubic variance remainder;
  nonpolynomial functions do not receive a fabricated exact truncation.
- The common-offset/scale calculation includes the product-of-variances
  term for the exact independent model. The source's first-order expression
  is accurately identified as first order.
- The draft gap statement “nondegenerate X implies variable X squared” is
  not true for a symmetric two-point law. The body uses a uniform interval
  counterexample, with explicit fourth moment, and also records the
  two-point boundary.
- H.1's primary reported standard uncertainty is 34 nm after its two thermal
  product terms. The value 32 nm appears only as the explicitly linear
  comparison. A 99-percent expanded interval is not inherited from that
  incomplete linear budget. Reliability of the additional terms and the
  output-law approximation are necessary inputs to such a claim.
- The H.1 product theorem states mutual independence. Zero pairwise
  covariance alone does not determine those product variances. The source's
  uncorrelated-input presentation is not silently promoted to an exact
  arbitrary-dependence product theorem.
- H.1's H.3 model is an approximation to the physical rational equation.
  The active text supplies the exact algebraic difference and separately
  identifies the nominal-length sensitivity approximation.
- H.10 requires separating ensemble uncertainty and finite-sample averaging.
  For fixed paired data with covariance-of-mean estimator U_mean, the
  quadratic difference is (n−1)/2 times the Hessian contraction with U_mean.
  The factor 1/2 belongs to an ensemble covariance of the random input
  actually transformed. These two identities and their definitions are
  derived separately in the active text.
- Source electrical results were recomputed from Table H.2's five rows.
  The manuscript does not silently force unrounded recomputations to equal
  the source's printed rounded standard uncertainties.

No active theorem tells the reader to repair an earlier incorrect formula.

## Author calculations

The end-gauge calculation retains unrounded conversions until reporting:

- comparison variance: 93.3847190890 nm squared;
- linear total variance: 1002.2388857557 nm squared;
- first extra product contribution: 137.5 nm squared;
- second extra product contribution: 2.7777777778 nm squared;
- resulting standard uncertainty: 33.8011340569 nm.

For the impedance calculation, the covariance of the input mean was computed
from the five simultaneous rows with denominator n(n−1)=20, converting mA to A.
The body and annex retain the input covariance, Jacobian and output covariance.
The standard uncertainties are:

| Method | Resistance | Reactance | Magnitude |
| --- | ---: | ---: | ---: |
| Propagate covariance at the input means | 0.0710714074 | 0.2955816774 | 0.2363361301 |
| Transform paired rows and estimate covariance of their mean | 0.0712735432 | 0.2954890856 | 0.2362475017 |
| Drop input covariances in the first-order propagation | 0.1945444545 | 0.2009093059 | 0.2040764254 |

All three columns are in ohms. The first two methods have close but distinct
centers and covariance estimates. The final method describes a changed
dependence assumption, not a permissible simplification of the paired data.

The density moments, affine covariance, Taylor bound, polynomial Gaussian
moments, product moments, entropy tilt and finite-sample averaging identity
were checked by their written derivations. These are author calculations, not
independent review or numerical confirmation of a missing proof.

## Author read-through and remaining integration

The completed actual body and annex were read through. During that pass a
missing display delimiter and ambiguous expectation-square typography were
corrected, entropy and normal-CDF notation were defined before use, and
wrapping table columns were used for long labels.

One direct body/annex inventory found 12 body results, 12 matching annex items,
zero unmatched reciprocal pairs, and equal counts of opening/closing display
delimiters (35 body, 29 annex before the final prose-only additions).
The intake parsed as CSV. No software test suite was created.

External mathematical interfaces used in the written batch are the existing
Gaussian/gamma moments, Student pivot/coverage and moment-indeterminacy
entries; their literal target labels were located in actual LaTeX.
Elementary finite linear algebra, integration, differentiation and
Cauchy–Schwarz are used with explicit local meanings.

No source-acquisition blocker remains for this selected treatment. The
remaining work is lead routing/intake integration and the separately required
consolidated independent reviews and final output checks. The nonlinear
coverage limitation is an accurately stated inference boundary, not a promise
to fabricate unavailable reliability data.
