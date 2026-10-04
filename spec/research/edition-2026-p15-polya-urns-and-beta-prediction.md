# P15.29: Pólya urns and beta prediction

8 September 2026. Nine complete statement/proof pairs supply the full
positive-parameter urn presentation and its explicitly proved updating,
dependence and prediction consequences.

## Exact source and reading

Durrett author Version 5, 11 January 2019:
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
Reuse DurrettPTEAuthor2019.

The complete Section 4.3.2 on printed pp. 226–227, physical pp. 234–235,
was read, including the transition calculation, the permuted word
numerator, both special cases, general beta density and opposite-color
continuation. Printed p. 227 was also read from its actual image at
tmp/pdfs/p15-polya-source/source-235.png.

The existing beta integral definition, beta-gamma normalization,
gamma recursion and moments were read in the active convolution chapter.
The supplied strong-law and countable-product interfaces are reused.
No general de Finetti theorem, moment-determinacy theorem or central
limit theorem is presumed in this urn-specific construction.

## Nine reciprocal pairs

Body prefix thm:p15- and proof prefix annex:p15. have these same suffixes:

- polya-construction: full independent-uniform recursion, predictable
  draw probabilities, martingale increment, all finite Lp limits and
  the deterministic bound comparing fraction with draw frequency.
- polya-word-law: every ordered-word probability, beta-binomial counts,
  the exact source permuted-product argument and full exchangeability.
- polya-mixture-representation: normalized beta integral for every
  finite word and parameter event, equality on the full sequence
  sigma-field and a measurable-section strong-law proof.
- polya-beta-limit: the entire general source beta law, joint
  frequency/sequence transfer and all finite conditional Bernoulli laws.
- polya-posterior-prediction: full beta update at every finite history,
  mean/variance, every future count probability and its extra variance.
- polya-moments: every mixed integer moment, distinct-draw covariance
  and correlation, count variation and exact mean-square prediction error.
- polya-source-special-cases: both original mass calculations and their
  separate Riemann/CDF routes, including the corrected density scaling.
- polya-parameter-boundaries: scale invariance, both reinforcement
  parameter limits, zero reinforcement and both zero-color cases.
- polya-worked-prediction: complete ordered/count likelihoods, two-draw
  prediction and model odds for the concrete green-green-red observation.

## Direct correction and scope

The source displays the g = 2, r = c = 1 single-cell probability as
converging to 2x. Its exact value is 2(s + 1)/((n + 1)(n + 2)),
which tends to zero. The active statement supplies
n times that probability tending to 2x when s/n tends to x,
and proves both limits. The direct count CDF also tends to x squared.

All positive finite real weights g,r,c are retained. Literal integer
balls and the real-weight extension have the same explicit transition
formula. The mixture construction is a joint probability representation;
it is not presented as a causal replacement of reinforcement.
The conditional strong-law event is measurable before product
integration; parameter-specific null sets are not silently intersected.

Zero reinforcement is treated without evaluating g/c or r/c. The two
zero-initial-color cases name which point-mass limit occurs.
The variance and posterior formulas retain the common random parameter;
a plug-in independent binomial law is explicitly distinguished by its
calculated probabilities and variance.

The Bayesian worked case follows from the proved urn path law and an
explicit two-model mixture. Its posterior model probability is distinct
from within-model success prediction. These consequences, sensitivity
limits and the exact beta-mixture proof are supplied additions, not
claims that the source prints those derivations.

## Saved pair and integration

Body: handbook/parts/p15/polya-urns-and-beta-prediction.tex
11,144 bytes, SHA-256:
0B1477F795435D02470C8F89B13345CC2A7BB6B87042A4A0304D5F2BAE8694EC.

Annex: handbook/annex/p15/polya-urns-and-beta-prediction.tex
15,711 bytes, SHA-256:
593FCC37AA997118DE167B59392A76D51B5CCBF9A6673F7B6F9F9011FB370191.

Both are integrated after density martingales, provisional scope P15.29.
The preceding density and quadratic-variation boundaries now refer to
this completed beta limit. The general de Finetti representation remains
a distinct subsequent source presentation.

The entire saved body and annex were read as one authoring batch.
Final corrections define the distribution notation before use and spell
out the two zero-color outcomes. Research and PDF skills guided exact
primary reading. No independent review, scanner, test, manuscript build,
manuscript render or admission check ran.

