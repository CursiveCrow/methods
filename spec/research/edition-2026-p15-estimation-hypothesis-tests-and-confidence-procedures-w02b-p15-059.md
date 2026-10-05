# w02b-p15-059: P15 169.9-169.11, large-sample regimes of Student inference

Packet: `work/waves/w02b/packets/w02b-p15-059.json`, block 1. Label tag
`p15-w02b-p15-059`. Heading `\chapter`, toc tag `%% toc: P15 169 169.9,169.10,169.11`.

## Gap addressed

Assessment of 169.9 (US-0): the route `student-inference.tex` /
`neyman-confidence-constructions.tex` covers the exact finite-sample procedures
and boundary cases but has no asymptotic regime: no large-sample approximation
of the Student or Neyman tests and intervals, no limit of the Student law or its
quantiles toward the normal, and no asymptotic coverage statement, rate or
failure.

## What was written (new files only)

Body `handbook/parts/p15/estimation-hypothesis-tests-and-confidence-procedures-w02b-p15-059.tex`
(chapter `sec:p15-w02b-p15-059`, "Large-Sample Regimes of Student Inference"):

- def:p15-w02b-p15-059-setting (34-77): normal / finite-variance / uniform
  sampling schemes, z_p, C_k, kappa_nu(c), pointwise vs uniform asymptotic coverage.
- def:p15-w02b-p15-059-method (79-104): procedure with side conditions.
- thm:p15-w02b-p15-059-chisq-moments (106-117).
- thm:p15-w02b-p15-059-student-limit (122-130): f_nu -> phi_0, L1/uniform CDF, quantiles.
- thm:p15-w02b-p15-059-mixture-order (132-150): F_nu = E Phi(t sqrt(W/nu));
  strict ordering; strict undercoverage of normal cutoffs at every n.
- thm:p15-w02b-p15-059-second-order (152-173): nu(F_nu - Phi) -> -psi uniformly
  on compacts; coverage-deficit rate c phi_0(c)(1+c^2)/(2 nu); quantile rate
  z(1+z^2)/(4 nu).
- thm:p15-w02b-p15-059-nonnormal (183-216): finite-variance iid: S_n -> sigma a.s.,
  self-normalized CLT, coverage -> alpha (Student and normal cutoffs, two- and
  one-sided), level, consistency, local power in a location-shift array.
- thm:p15-w02b-p15-059-nonuniform (224-237): Bernoulli construction, coverage
  infimum zero at every n for every multiplier.
- thm:p15-w02b-p15-059-uniform-regimes (242-265): exact max interval (n-sample
  extension of Neyman's I_3^U), rate 1/n vs plug-in normal interval rate n^{-1/2};
  P(min J_n < L_n) -> (1+alpha)/2.
- def:p15-w02b-p15-059-example (270-314), def:p15-w02b-p15-059-limits (316-337),
  relationships and sources paragraphs (339-356).

Annex `handbook/annex/p15/estimation-hypothesis-tests-and-confidence-procedures-w02b-p15-059.tex`
(sec:annex-p15-w02b-p15-059), one annexitem per body result, lines 22-416.

Routing patch request: `work/waves/w02b/patches/w02b-p15-059.json` (one
insert_after in read-only host `handbook/parts/p15/student-inference.tex`
after thm:p15-student-worked-cases).

## Sources opened this session and locators used

- `citations/Durrett - Probability - Theory and Examples (2019-01-11, Version 5).pdf`
  (DurrettPTEAuthor2019, Version 5): printed p. 144 holds Theorem 3.4.1
  (i.i.d. CLT); printed p. 147 (PDF page 155) holds Exercise 3.4.5
  (self-normalized sums). Only these two locators are cited.
- No Neyman 1933/1935/1937 locator was written in the new files; the
  connections to Neyman's systems go through handbook cross-references
  (def:p15-neyman-uniform-systems, thm:p15-neyman-normal-one-sided).

All other mathematics (chi-square moments, Student density limit, scale-mixture
ordering, second-order expansion, Bernoulli non-uniformity, uniform endpoint
regimes) is proved in full in the annex from handbook results
(thm:p15-clt-iid, thm:p15-clt-perturbation, thm:p15-weak-continuous-mapping,
thm:p15-extended-mean-strong-law, thm:p15-scheffe-density-limit,
thm:p15-normal-normalization, def:p15-gamma-density, thm:p15-student-law,
thm:p15-student-orthogonal) and is not attributed to any source.

Numerical values in the example were computed with scipy in this session
(t quantiles for nu=9,29; 2F_nu(c)-1 for nu=9,29); nu=1,2 values use the
closed forms of thm:p15-student-worked-cases.

## Existing treatments found

- `handbook/parts/p15/measurement-uncertainty.tex` 490-511: mentions the exact
  Student procedure and the Welch-Satterthwaite Student approximation; no
  asymptotic regime. Not listed in the packet's existing list; not modified.
- `handbook/parts/p15/evidence-synthesis.tex` 175, 295: large-sample remarks for
  weighted procedures; not a Student-law limit. Not listed; not modified.
- Huber unit (ED26-P15-CH-huber-robust-location) C001-C015 are the existing
  environments of `handbook/parts/p15/huber-robust-location.tex` (17-339);
  not modified in this block.

## Open items

- Neyman's Example II (triangular law) has no sample-size index in the source
  presentation as routed; no asymptotic statement was written for it.
- The second-order term is proved only under normal sampling; no rate for
  non-normal laws (e.g. Edgeworth-type one-sided corrections) is written; no
  held source for such a rate was opened.
- Laws without finite variance (e.g. the self-normalized Cauchy case): nothing
  written; would need a held source and proof.
- Three small overfull boxes remain in the unit build (two annex item titles,
  one 2.5pt line in the method); no content effect.

## 169.10 practical magnitude (continuation pass)

Gap: X-169.10-practical-magnitude (no on-route treatment of significance or
confidence or posterior statements against practical magnitude). Searched
handbook/parts/p15 for practical, negligible, effect size, magnitude,
significance: no existing treatment; related results linked, not duplicated:
thm:p15-confidence-credibility-boundary, thm:p15-bayes-coverage,
def:p15-valid-p-value, thm:p15-bayes-normal-calculation.

Written (body section sec:p15-w02b-p15-059-magnitude, lines 275-547; annex
lines 418-696): def:...-magnitude (departure d, margin delta fixed before data,
band B_delta, significance, Student p-value pi_m, verdict events N_n/O_n,
posterior Pi_n); lemma ...-pvalue (equivalences, exact uniform null law);
thm ...-verdicts (O_n implies significance; N_n = two one-sided Student tests
at (1+alpha)/2; normal-sampling bounds P(N_n) <= (1-alpha)/2 for |d|>=delta
and P(O_n) <= 1-alpha for |d|<=delta); thm ...-scale (rejection probability a
continuous function of (mu-m)/sigma, equal to 1-alpha at 0 and tending to 1;
not monotone in |mu-m|); thm ...-magnitude-limits (finite-variance sampling:
significance -> 1 for every d != 0, p-value -> 0 a.s.; verdicts -> indicator of
|d| vs delta, boundary |d|=delta gives (1-alpha)/2 each; 0<|d|<delta gives
significant and interval inside the negligible half-band with probability ->
1); thm ...-posterior (conjugate normal, known sigma: posterior of positive
departure -> 1 for every d>0, uniform limit law at d=0, posterior interval
matches the confidence interval to o(n^{-1/2})); method, worked example and
warning. Chapter title and introduction updated to include the section.

Numbers in def:...-magnitude-example computed with scipy in this session
(t quantiles, noncentral t power, numerical integration of P(N_n) and of the
joint event over the independent normal mean and chi-square variance,
posterior normal tails).

No source-specific presentation was written and no new locator was written.

## Continuation

Block 1 wrote the 169.9 asymptotic-regime gap and, in the continuation pass,
the 169.10 practical-magnitude gap, both in the owned files. Remaining open
items: as listed above and in the return file (verdict bounds only under
normal sampling; posterior only for the conjugate known-variance model; small
overfull boxes). Placement unchanged: body after `parts/p15/huber-robust-location`
(handbook/parts/p15.tex line 62), annex after `annex/p15/huber-robust-location`
(handbook/annex/p15.tex line 61); routing patch request
work/waves/w02b/patches/w02b-p15-059.json.
