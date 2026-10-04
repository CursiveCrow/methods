# Holm 1979: multiple-testing authoring and source record

Unit: ED26-METHOD-multiple-testing. Authoring completed 1 October 2026.
This is an author return and source record, not independent acceptance.
The parent owns reader routing, canonical intake merging and final gates.

## Exact selected source and actual reading

Sture Holm, A Simple Sequentially Rejective Multiple Test Procedure,
Scandinavian Journal of Statistics 6(2), 1979, pp.65-70.
The first article page says received December 1977, revised September 1978.
The journal issue/publication date remains 1979.

- Free source URL: https://www.ime.usp.br/~abe/lista/pdf4R8xPVzCnX.pdf
- Stable article locator: https://www.jstor.org/stable/4615733
- Held PDF: source/references/p15-multiple-testing/holm-1979-sequentially-rejective.pdf
- Size: 1,059,670 bytes; seven physical pages.
- SHA-256: 4317A0D1555DAD949DC1760605D925BA20037402827741FDF99CD8EA37E80C46
- Extent: physical page 1 is the archive cover; physical pages 2-7 are
  the complete original article, printed pp.65-70.
- Capture: ordinary verified TLS download from the recorded free URL;
  the response was application/pdf with a PDF header. No paid access.
- Source acquisition and extraction records:
  source/references/p15-multiple-testing/acquisition.json,
  acquire-and-extract.py and holm-1979-extracted.txt in that directory.

The author read the complete extracted article, including its introduction,
both theorems, both procedure schemes, all applications, acknowledgement
and references. All six complete article pages were rendered and inspected
to check formulas and the source's actual nonstrict comparisons; the OCR
alone obscured some inequality glyphs. The inspection files are in
tmp/pdfs/p15-multiple-testing/source-page-2.png through source-page-7.png.
The cover identifies the source and the archived 2013 access manifestation;
that access date is not a publication or revision date.

The primary-source locations are:

- pp.65-66: family critical regions, protection for free combinations,
  actual and restricted truth configurations, secondary intersections,
  coherence/consonance and further logical consistency constraints.
- p.66: upper-tail critical functions and the obtained levels.
- p.67, Scheme 1 and Theorem 1: ordinary sorted step-down and its
  union-bound error protection.
- pp.67-68: dominance over fixed Bonferroni and the ten-normal-test
  power example.
- p.68: opposite directional hypotheses and complementary inclusive
  tails; the all-detail-nonrejection confidence-set limitation; the
  independence-based larger thresholds; start of control comparisons.
- pp.68-69: normal treatment/control and refined Dunnett comparison,
  unequal sample sizes, directional comparisons, Wilcoxon marginal
  inputs, contingency tables, time series and multivariate problems.
- pp.69-70, Scheme 2 and Theorem 2: positive-weight ratio ordering,
  remaining-weight allocation and full weighted error-protection proof.
- p.70: weight priorities, exact or approximate individual calibration,
  the design observation about independence, and the complete references.

The selected extent is the whole six-page article and has been supplied.
Holm's cited Dunnett 1955, Gabriel 1969, Holm 1977, Marcus et al.1976 and
other referenced works are not silently counted as newly read full bodies.
The source's refined Dunnett numerical entries are identified as reported
values for its comparison example. This unit does not prove those separate
source treatments or count them as independently verified reproductions.

## Prerequisite interfaces and local exposition

Read actual current definitions in
handbook/parts/p15/hypothesis-tests-and-confidence.tex:

- def:p15-statistical-experiment supplies the measurable sample law and
  the distinction among size, power, rejection and nonrejection.
- def:p15-valid-p-value supplies marginal superuniformity for every
  parameter in the composite null.
- thm:p15-discrete-p-values supplies the preceding finite inclusive-tail
  treatment; this chapter also proves the general real-statistic case.
- def:p15-confidence-procedure and thm:p15-confidence-test-inversion
  supply the interpretation of candidate-set coverage.

The whole current student-inference.tex was read. Its
thm:p15-student-orthogonal and thm:p15-student-law are the normal
coordinate and Student-law interfaces used in the new common-control
derivation. The comparison proof carries unequal positive group sizes,
including singleton groups, the positive pooled residual degrees of
freedom, the common positive variance and the zero-scale convention explicitly.
It does not assume the resulting comparisons are independent.

## All five selected component conditions

| Component | Current authored evidence |
| --- | --- |
| C01: family, valid levels and family-error event | def:p15-mt-family and def:p15-mt-obtained-levels; inclusive composite-tail proof at annex:p15.mt.inclusive-levels |
| C02: exact step-down rule | def:p15-mt-holm-rule; termination, measurable sorting, equality and tie proof at annex:p15.mt.ordering; adjusted-level equivalence and worked stopping example |
| C03: every configuration of true hypotheses | thm:p15-mt-holm-strong and annex:p15.mt.holm-strong; actual full parameter, empty true set, first true rank, union bound and equivalent source subset statement |
| C04: comparisons | thm:p15-mt-domination and its full proof; pointwise rejection-set inclusion, false-subset power probabilities, expected rejections, nonstrictness and identical no-rejection event |
| C05: multiple-comparison failure and remedy | thm:p15-mt-failures and annex:p15.mt.failures; twenty-test selection failure, complete-null-only gate, dependent independent-tail failure, data-selected weighting failure, and appropriate proved procedures |

These component conditions are complete as authored arguments. The unit is
not independently admitted.

The chapter additionally preserves the entire selected source scope:
secondary intersection policy; a proved closed Bonferroni equivalence;
opposite-tail consistency with an explicit common boundary law;
the bounded confidence-inversion limitation; the original normal model;
ordinary and positive-weight Scheme 2 with Theorem 2 for every actual
truth configuration; the independence extension under the full required
true-null premise; and every application area named on pp.68-70.

The new normal-control and conditional permutation derivations make the
marginal assumptions usable. Approximate marginal validity has an explicit
sum-of-calibration-errors bound. Independence is used only where supplied
by the normal power example or required by the separate larger-threshold
extension. Ordinary and weighted Holm require only their actual marginal
null inequalities; no global-null or independence substitute was made.

## Numerical derivation and correction provenance

The original ten-test example specifies independent N(mu,1) variables
with four means zero, four means six and two means three, at family level
0.05. The selected power quantity is rejection of both mean-three
hypotheses. The article prints Bonferroni 0.439 and step-down 0.565.

Using exact normal quantiles gives:

- Bonferroni critical value 2.5758293035489.
- Bonferroni joint power 0.44126703489243324.
- Holm joint power 0.5631999190708721.

The Bonferroni quantity is the squared exact normal upper-tail power.
The Holm quantity is a finite probability-bin recursion whose complete
derivation is in annex:p15.mt.normal-power. It integrates all four
true-null variables and all four high-mean alternatives; it does not
pretend they are deterministically absent or already rejected.
The executable author calculation is
source/references/p15-multiple-testing/numerical-applications.py,
SHA-256 3A89B95173078A0C58C3AB3A7A9358024D3D9371F77ED947063A1DF36AD98D40.
It uses Python's ordinary NormalDist CDF/quantiles and no simulation to
evaluate that finite recurrence.

A separately executed Monte Carlo calculation with NumPy, seed 1979,
3,000,000 independent draws in 50,000-draw chunks, sorted the ten normal
statistics and applied the complete prefix stopping comparisons.
It gave Holm 0.5635273333333334 (Monte Carlo standard error
0.0002863356293580173) and Bonferroni 0.4414186666666667
(standard error 0.0002866869531881357). Those estimates support the
finite-recursion evaluations; they are not a proof of the general theorem.

The reason for the source's different approximations is not established
by the article. Its Bonferroni value is consistent with a rounded normal
critical value near 2.58, but that is an inference, not a verified account
of its calculation. The current active text uses the derived model
quantities directly. The source's printed numbers and the discrepancy
remain here as provenance, without asking readers to repair the example.

The same author calculation evaluated the failure-case probabilities:
unadjusted twenty-null FWER 0.6415140775914581, corrected twenty-null
FWER 0.04883012474683324, dependent independent-tail FWER
0.05064113103820733, and observed-weight-selection FWER 0.09654975.
Each has its exact algebraic derivation in the annex.

## Author read-through and integration handoff

The author read the full current body, annex and intakes. The focused
format check found 16 body results and 16 reciprocal annex items, zero
unmatched local proof links, 16 ordinary annex proof environments, zero
body proof environments, and no sketch tags. The 45 symbol rows have
no blank required cells, all glyphs have actual TeX math delimiters,
and all first-use labels are declared in these assigned files.
The check is authoring evidence, not independent mathematical acceptance.

No remaining source or proof gap is identified in this assigned selected
unit. The protected source is held, and the current treatment uses
independently worded exposition and newly supplied full arguments.
Rights, independent reviews, source admission and final publication
remain the parent campaign's separate gates.

| Artifact | Size or count | SHA-256 |
| --- | ---: | --- |
| handbook/parts/p15/multiple-testing.tex | 503 lines; 24,144 bytes | 60C24D1E219C01CEA8A1EDF90FB9F57DB766B363A857BB141E49A135C43FCAD0 |
| handbook/annex/p15/multiple-testing.tex | 544 lines; 26,088 bytes | A5061C8590458238872C299B1D97F4035C41FA8767909114F1C731EBC25A7B0A |
| handbook/bib/intake-p15-multiple-testing.bib | 1 entry | 35B637E544F6DE56F639AABCE9D2105F3E9FE75129D0CF71390AB487F5EB1E7C |
| handbook/registry/symbols-intake-p15-multiple-testing.csv | 45 data rows | A54404881253B9C6EF42330019BB1B9FF78E77BA392DA507D3D87864B83B1F68 |

The bibliography intake adds only Holm1979Original.
No shared driver, canonical record, generated file or rule sheet was
changed. The lead should route the two chapter files and merge the two
dedicated intakes, retaining this author record. No manuscript build,
render, review wave or prose test suite was run. Source pages alone were
rendered to read the primary schemes and application table.

The named broad scope needs the body/annex union:

    "P15 multiple testing": {
      "presentation": "Holm 1979 original ordinary and fixed-weight procedures with full derived calibration and application arguments",
      "regions": [
        {"anchor": "sec:p15-multiple-testing"},
        {"file": "annex/p15/multiple-testing.tex"}
      ]
    }

The conditioning-information role of Z_i is deliberately narrow:

    "P15 conditional multiple-testing calibration": {
      "presentation": "Conditioning information in the marginal-calibration lemma",
      "regions": [
        {"anchor": "thm:p15-mt-conditional-calibration"},
        {"anchor": "annex:p15.mt.conditional-calibration"}
      ]
    }

The separate standardized normal contrast Z_i is registered directly
on annex:p15.mt.control-model. These regions are disjoint; neither role
is renamed into a false global convention. No role override is requested.
