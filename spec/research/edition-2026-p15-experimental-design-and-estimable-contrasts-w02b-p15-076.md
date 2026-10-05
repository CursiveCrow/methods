# w02b-p15-076 — P15 chapter 174 (sections 174.5–174.8): treatment versions, interference, adherence, missing outcomes and sample size

Packet: work/waves/w02b/packets/w02b-p15-076.json. Label tag: p15-w02b-p15-076.

## Files

- Body: handbook/parts/p15/experimental-design-and-estimable-contrasts-w02b-p15-076.tex
- Annex: handbook/annex/p15/experimental-design-and-estimable-contrasts-w02b-p15-076.tex
- Bib intake: handbook/bib/intake-p15-experimental-design-and-estimable-contrasts-w02b-p15-076.bib
  (HigginsSavovicEtAl2024Cochrane08, HigginsEldridgeLi2024Cochrane23)
- Symbol intake: handbook/registry/symbols-intake-p15-experimental-design-and-estimable-contrasts-w02b-p15-076.csv
- Patch request (readonly host factorial-inference-and-estimability.tex, two forward links):
  work/waves/w02b/patches/w02b-p15-076.json

## Provenance

Held sources opened in this session (text extracted with pdftotext / HTML tag stripping):

- source/references/hernan-robins-what-if-longitudinal-2026/hernan-robins-what-if-19aug2026.pdf
  (bib HernanRobins2020WhatIf2026, already in handbook.bib). Printed page = PDF page − 9.
  Locators seen and used: Fine Point 1.1, p. 5 (interference; Y^a ill-defined; need to name others'
  allocation); §3.4, pp. 34–36 (well-defined interventions; one treatment name, different versions in
  two trials; effect depends on unspecified components such as surgeon experience); Technical Point 16.2,
  p. 212 (data-only bounds; continuous outcome needs min and max); §16.4, pp. 217–218 (compliance types,
  monotonicity, IV estimand equals complier effect); Technical Point 16.7, p. 224 (proof of the complier
  identity for a population); §22.1 with Fine Point 22.1, p. 306 (intention-to-treat effect vs per-protocol
  effect). §12.6, pp. 172–173 was read (censoring weights) but is not cited.
- source/references/acq-r1-ACQ-2026-10-0328/cochrane-handbook-ch08.html (Higgins, Savović, Page, Elbers,
  Sterne, Chapter 8, last updated October 2019, Handbook v6.5, 2024). Sections read and cited: 8.2.2
  (ITT vs per-protocol effect), 8.4.4 (appropriate analyses; as-treated and naive per-protocol
  inappropriate), 8.5.1 (complete-case bias depends on relation of missingness to true value within arm),
  8.5.2 (no threshold for small missing fraction).
- source/references/acq-r1-ACQ-2026-10-0323/cochrane-handbook-ch23.html (Higgins, Eldridge, Li,
  Chapter 23, last updated October 2019, v6.5, 2024). Sections read and cited: 23.1.1 (cluster
  allocation, contamination, unit-of-analysis error), 23.1.3 (analysis at cluster level), 23.1.4 and
  23.1.4.1 (design effect 1 + (M − 1) ICC, effective sample size; formula text appears in 23.1.4.1).
- NIST/SEMATECH 2012 PDF not opened; no NIST locator written in the new files.

Handbook derivations (not attributed to a source): the weighting-statistic lemma for an arbitrary
observation model; version-mixture estimand, version dependence, swap nonidentification, recorded-version
identification; design-averaged contrast under interference, two-unit example, cluster-confined
interference with cluster assignment; finite-unit complier identity and its two counterexamples, the
as-treated functional; finite-unit sharp bounds, exact complete-case bias identity (covariance form and
q(μ_cc − μ_mis) form), covariate-stratified premise and its ten-unit instance; planning families
(replication, complete blocks, cluster means), known-variance size and power, t_{ν,p} > z_p by strict
concavity, z-plug coverage loss, mean and probability criteria for the Student half-width, exact Student
power integral and product lower bound. All worked numbers are stipulated planning values or hypothetical
tables; numeric quantiles and integrals were computed with scipy 1.17.1 (stats.t, stats.chi2,
integrate.quad) in this session.

Existing treatments found and linked rather than duplicated (A9):
- sec:p15-factorial-* (readonly unit ED26-SCI-NIST2012-001, owner w02b-p15-075): contrast derivations
  and aliasing (174.5, 174.6) — routed by \cref in the chapter opening; precision formulas reused.
- handbook/parts/p15/experimental-design-and-estimable-contrasts-w02b-p15-077.tex (not listed in the
  packet's "existing"): thm:p15-w02b-p15-077-interference, -noncompliance, -missingness give the
  structural nonidentification forms; this chapter links them and adds what the weighting statistic
  estimates, the version premise, the complier identity, sharp bounds and the exact complete-case bias.
- handbook/parts/p15/experimental-design-and-estimable-contrasts-w02b-p15-075.tex (not listed):
  sampling/transport section linked in the limitations section.
- P16 sequential-interventions-and-g-formula.tex (editable host): not modified; its sequential
  positivity/failure theorems are linked.

## Continuation

- 174.7 and 174.8 material written in body and annex; unit-compile reports ok (5 overfull boxes under 5pt;
  tree check shows only bib-key findings for the two
  intake keys.
- Open items for the lead: apply the patch request after the driver inputs exist; merge the bib and
  symbol intakes. Driver insertion per return JSON.
