# w02b-p15-075 — P15 chapter 174 (sections 174.1–174.4): target populations, design-based inference, sampling and observational comparisons

Packet: work/waves/w02b/packets/w02b-p15-075.json. Label tag: p15-w02b-p15-075.

## Provenance

- Held source opened in this session:
  source/references/hernan-robins-what-if-longitudinal-2026/hernan-robins-what-if-19aug2026.pdf
  (365 PDF pages; held-sources.json entry; bib key HernanRobins2020WhatIf2026, already in handbook.bib).
  Read via pdftotext: PDF pp. 22–24, 36–37, 61–63, 146–153. Printed page = PDF page − 9 on these spreads.
- Locators used and seen in this session:
  - ch. 2 opening, p. 13 (a causal question names an action, an outcome and a specific population);
  - §2.1, pp. 14–15 (exchangeability; Technical Point 2.1 on mean exchangeability);
  - ch. 3 opening, p. 27 (observational study: investigator observes and records); §3.1, p. 28 (three
    identifiability conditions: consistency, conditional exchangeability, positivity);
  - §4.3, p. 52 (transportability, effect-modifier distributions, unverifiable assumption);
    Fine Point 4.2, p. 54 (effect modification, treatment definition, interference; reweighting by stratum
    proportions with no guarantee);
  - §10.1, pp. 138–139 (estimand/estimator; calibrated, conservative, valid intervals);
  - §10.2, pp. 140–142 (two targets: randomization-based inference for the randomized sample versus
    super-population inference; randomization then sampling equivalence remark p. 142);
  - §10.3, pp. 142–144 (super-population as fiction; generalization by assumed random sampling).
- Handbook derivations (not attributed to the source): exact variance of a weighted multi-cell
  complete-randomization contrast, conservative variance estimator and its excess S_w^2/N, the
  non-existence of an unbiased variance estimator (cross-term argument), Chebyshev interval with
  Popoviciu bound, randomization test validity and constant-effect inversion, blocked design variance,
  inverse-inclusion estimator and its variance estimator, SRS-then-CR as a labelled partition of the
  target population, estimand gap decomposition, inclusion and no-assumption bounds, stratified
  observational premise; all worked numbers (hypothetical six-unit table).
- NIST/SEMATECH 2012 PDF not opened in this session; no NIST locator is written in the new files
  (the readonly host carries the NIST presentation).

## Gaps addressed (from the independent assessment)

- 174.1(i): def:p15-w02b-p15-075-populations, thm:p15-w02b-p15-075-estimand-gap (composition and
  within-stratum terms, stratum transport, nested and disjoint recruitment ranges),
  def:p15-w02b-p15-075-estimand-procedure.
- 174.1(ii): thm:p15-w02b-p15-075-neyman (exact variance, conservative estimator, excess S_w^2/N, no unbiased
  variance estimator), thm:p15-w02b-p15-075-chebyshev, def/thm randomization test with inversion.
- 174.2(i): sampling design, inverse-inclusion estimator, sampling-then-assignment, what each randomization licenses.
- 174.2(ii): observational comparison, selection decomposition, logical bounds, stratified premise (P)/(Q) and its
  untestability; cross-references to P16 identification results.
- 174.3/174.4 (C01–C03) remain in the readonly host factorial-inference-and-estimability.tex; the new chapter links
  them and adds the design-based blocked analysis (thm:p15-w02b-p15-075-blocked).

Existing treatment found and linked (not rewritten): host factorial chapter; P16 finite-counterfactuals
(def:p16-binary-potential-outcomes, thm:p16-po-ate-identification, thm:p16-po-att-identification);
thm:p15-without-replacement-convex. Sibling packet w02b-p15-077 (toc 174.9, 174.10) is separate.

Patch request: work/waves/w02b/patches/w02b-p15-075.json (routing sentence after the host's sampling/transport remark).

## Continuation

- State: body (692 lines) and annex (457 lines) written; eleven body results, each with an annexitem.
  unit-compile ok; check.py shows no findings for these files; find_fused_spaces no hits.
- Worked numbers verified by exact enumeration (scratch scripts, fractions) in this session.
- Open items: normal-approximation interval coverage not proved (stated in text); NIST PDF not opened, so no NIST
  locator written. Driver insertion and host patch are lead actions.
