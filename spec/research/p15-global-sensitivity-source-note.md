# Global sensitivity: source reconstruction and authoring record

Date: 9 September 2026.
Unit: ED26-SCI-SaltelliAnnoni2010-001.
Standing: the four selected components are authored and ready for lead
integration. This is an authoring record, not independent acceptance.

## Delivered files

- handbook/parts/p15/global-sensitivity-and-robustness.tex
- handbook/annex/p15/global-sensitivity-and-robustness.tex
- handbook/bib/intake-p15-global-sensitivity.bib
- handbook/registry/symbols-intake-p15-global-sensitivity.csv

The lead owns drivers and canonical records. No shared drivers, style,
canonical bibliography or canonical symbol registry were edited.

## Exact source and reading

Andrea Saltelli and Paola Annoni, *How to avoid a perfunctory sensitivity
analysis*, Environmental Modelling & Software 25 (2010), 1508–1517,
DOI 10.1016/j.envsoft.2010.04.012.

- Free author-hosted personal copy:
  https://www.andreasaltelli.eu/file/repository/PublishedPageNumbers.pdf
- Local:
  source/references/p15-global-sensitivity/saltelli-annoni-2010.pdf
- Bytes: 1670724.
- SHA-256:
  FBA86067787DB902321E536DF82AA0631440B6402F716B2181768CE6296E0DDC.
- Eleven physical pages: an author-copy wrapper followed by the ten
  numbered article pages, including references.
- The visible first article page identifies both authors, journal,
  pages and DOI. The PDF information dictionary has blank title/author
  fields and does not replace that internal identification.
- Received 21 October 2009, revised 14 April 2010, accepted 15 April 2010,
  available online 15 May 2010.
- This is not the similarly titled three-author Procedia Social and
  Behavioral Sciences 2 (2010), 7592–7594 conference paper.

The entire article, Sections 1–7 and references, was read in the complete
layout extraction tmp/p15-global-sensitivity/source-layout.txt.
Physical pages 4–6 were visually inspected for the geometry, factorial
effects, regression relation, index formulas, and exact G/D expressions.
Physical pages 8–9 were visually inspected for the reported CDF comparisons
and their evaluation counts. The PDF renderer reported fallback-font
warnings for Symbol/ArialUnicode; the displayed formulas and labels used
in this reconstruction remained legible and were compared with the text.
No manuscript rendering was performed.

The research and PDF skills were read and used for primary-source
retrieval and source-equation/figure inspection. They did not cause an
extra manuscript review, build or rendered-output cycle.

## Retrieved Content

### Source: article Section 1, printed p. 1508

The two questions are stated as:

> How uncertain is this inference?

> Where is this uncertainty coming from?

These are the source's separate uncertainty-analysis and sensitivity-analysis
questions. The editorial reconstruction is recorded below.

## Supplementary Notes

### Component coverage

**ED26-GAP-SCI-005-C01.** The body defines the model, feasible domain,
joint law, baseline and target inference. It distinguishes output
uncertainty, local derivatives, finite coordinate changes and robustness
across a family of assumptions. Joint distributions, physical ranges
and probability-coordinate designs are not conflated.

**ED26-GAP-SCI-005-C02.** The OAT limitation is proved by a continuous
bilinear family agreeing on every baseline coordinate line. The centered
hypercube/inscribed-ball calculation is supplied with its actual
hypotheses and interpretation. The two-level corner decomposition,
regression projection and elementary-effects procedure provide the three
less expensive alternatives selected by the paper. The factorial proof
includes every subset interaction rather than only the displayed
three-factor example. The elementary-effects discussion preserves
changing backgrounds, radial alternatives, nominal costs and the
curvature/interaction ambiguity.

**ED26-GAP-SCI-005-C03.** The functional ANOVA decomposition is derived
from commuting coordinate conditional expectations under a product law.
The annex proves zero-coordinate averages, orthogonality, uniqueness and
variance additivity. It then derives first-order and total indices,
their bounds, sum relations, additive equivalences and the total-zero
criterion. The centered product example has variance 1/9,
first-order indices zero and total indices one.
Explicit paired-evaluation identities and consistent estimators are
derived, with correct independence, L2 and positive-variance conditions.
No finite-sample unbiasedness or confidence interval is fabricated.

**ED26-GAP-SCI-005-C04.** The declared-law G example is analyzed exactly,
and a four-point D contrast isolates its interaction. A linear example
reverses the factor ranking under a changed input range and changes a
threshold claim, with exact exceedance probability 1/12.
The variance-family condition for a ranking to hold throughout its
declared rectangle is proved. Dependent inputs and causal intervention
have separate explicit counterexamples; independent observed inputs do
not by themselves identify a structural intervention effect.

The body has 546 lines and the annex 394 lines at this checkpoint.
There are 12 reciprocal theorem/proof pairs and 25 symbol-intake rows.
The bibliography intake contains one exact primary article entry.
These counts concern construction, not mathematical or publication
acceptance by an independent reviewer.

### Mathematical clarifications applied directly

The source's geometric ratio is the volume of a ball containing a
centered OAT design. The active text does not call this the volume
actually explored. The OAT line set has zero volume in dimension at
least two, but so does every finite global sample. Sampling-law and
integration properties therefore matter; geometric volume alone is
not a proof that one finite method must be more accurate.
The inscribed-ball containment is explicitly restricted to a centered
baseline. The independent interaction-identifiability proof does not
require this geometric argument.

The standardized-regression relation is stated exactly:
R2 = b-transpose Sigma b.
It becomes a sum of squared standardized coefficients when the predictor
correlation matrix is the identity. Population independence does not
guarantee exact empirical orthogonality. Low R2 describes unexplained
variation under the selected linear span; it is not an unconditional
measure of nonlinearity, especially with stochastic error or omitted
inputs. The proof includes the singular-coefficient boundary.

Different trajectory locations are not equated with statistical
independence. The active method states when independently randomized
trajectories give independent replicates and keeps descriptive effect
spread separate from an inferential accuracy guarantee.
Elementary-effect spread does not separate nonlinearity from interaction.

The first-order numerator measures the expected variance reduction from
learning an input; it is not the variance reduction obtained by setting
that input to an arbitrary chosen nominal value. Under dependence,
S_i <= S_Ti and the independent orthogonal variance allocation need not hold.
The exact X1=X2=U example gives S1=S2=1 and ST1=ST2=0.
Zero output variance leaves normalized indices undefined.

The source's toy experiment explicitly uses uniform [-1,1] inputs.
For W=|4X-2| on that law, EW=5/2 and Var(W)=37/12.
The active product formulas use these values; the familiar [0,1] moments
were not substituted. The D expression was checked against the visible
formula, including its X2 sixth-power term and cos(3 X1 squared) factor.
Its mixed rational-bump contrast is exactly 81/35.

### Source experiment standing

The body reports the source's toy parameters, OAT/EE budgets and
qualitative plotted behavior. The toy comparisons use 9/9 evaluations
at dimension 2, 21/24 at dimension 5, and 29/32 at dimension 7.
The displayed reference CDF was computed from 1000d quasi-Monte Carlo
evaluations; the active text calls it a numerical reference, not the
exact population CDF.

The source describes a zero toy baseline and nominal OAT step magnitudes
0.2 and 0.4. A complete EE/QMC point list and randomization/configuration
record is not supplied in the article. Exact reconstruction of each
published plotted ordinate is not claimed. The analytic toy calculations
in the annex instead use the explicitly declared [-1,1] law and exact
displayed response functions.

Section 6.2 remains application evidence, as the allocation requires.
The body records the Bateman-chain equations, initial conditions,
time, rate ranges, sample budgets and numerical-reference role.
It does not create an additional requirement to derive a complete
nuclear/chemical kinetics theory, validate that application domain,
or reproduce its unavailable random input-range choices.

The paper's reports of prior applications and recommended performance
are attributed to that source. The underlying studies were not newly
reproduced, and no unrestricted guarantee about the relative accuracy
of EE, regression or OAT is asserted.

### Source methods versus added derivations

The 2010 article specifies the first and total indices and points to
separate estimator papers. This handbook supplies the conditional
expectation/variance derivations and the paired-evaluation identities
as direct mathematical consequences, rather than claiming the article
itself prints these complete proofs or this exact estimator exposition.

The corner-basis decomposition is over its uniform finite design
measure, not automatically the uncertainty law P.
The product decomposition is over the explicitly independent probability
law. These two decompositions have different inputs and are not merged.

The causal counterexample uses two structural models with independent
observed inputs and identical observational output laws. Their different
post-intervention output expectations, 1 and 1/2, demonstrate
nonidentification directly. This is an analytic example, not a
new empirical result.

### Prerequisites and checks

The actual existing LaTeX was inspected for conditional expectation,
conditional L2 projection, total variance, product integration, gamma
normalization and the integrable iid strong law. The relevant interfaces
include:

- thm:p15-conditional-variance
- thm:p15-conditional-l2-projection
- thm:p15-conditional-factorization
- thm:p15-fubini
- thm:p15-tonelli
- thm:p15-gamma-normalization
- thm:p15-iid-series-strong-law
- sec:p16-finite-causal-models

The entire authored body and annex were read through. The OAT theorem
was clarified to say that its counterexample has nonzero values outside
the line set, rather than incorrectly implying nonzero values at every
off-line point in dimensions above two. Hybrid coordinates are explicitly
placed in their original positions.

Direct arithmetic checks gave:
r12 = 0.00032599188692738996,
D contrast = 2.3142857142857145 = 81/35,
EW = 2.5,
EW2 = 28/3,
Var(W) = 37/12.
A bounded structural check found all 12 body targets matched by their
annex back-references, with no unmatched pair. The symbol CSV parsed as
25 rows.

No software test suite, independent review, manuscript build or
manuscript render was run. Lead routing, canonical intake merging and
later consolidated reviews remain separate work.
