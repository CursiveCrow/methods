# P15 chapter 172, sections 172.7-172.10: sensitivity conclusions under changed dependence and formulation

Packet: w02b-p15-069 (wave w02b, r2 continuation). Label tag: p15-w02b-p15-069.
Date: 4 October 2026. This is an authoring record, not an acceptance.

## Files

- handbook/parts/p15/robustness-and-sensitivity-of-inference-w02b-p15-069.tex
  (chapter sec:p15-w02b-p15-069-assumption-sensitivity, 351 lines)
- handbook/annex/p15/robustness-and-sensitivity-of-inference-w02b-p15-069.tex
  (section sec:annex-p15-w02b-p15-069-assumption-sensitivity, 247 lines)
- handbook/bib/intake-p15-robustness-and-sensitivity-of-inference-w02b-p15-069.bib (no new keys)
- handbook/registry/symbols-intake-p15-robustness-and-sensitivity-of-inference-w02b-p15-069.csv
- work/waves/w02b/patches/w02b-p15-069.json (two insert_after link requests
  for the read-only host handbook/parts/p15/global-sensitivity-and-robustness.tex)

## Gap addressed

r1 assessment of this packet: ED26-GAP-SCI-005-C04 partial. The existing
host (global-sensitivity-and-robustness.tex) reports ranking and threshold
changes only across input ranges of one independent linear model
(thm:p15-global-ranking); the dependent-input theorem
(thm:p15-global-dependent-boundary) gives index values without a ranking or
factor-fixing comparison against the independent law; def:p15-global-lookup
only instructs recomputation.

New material (all mathematics derived here; no result is attributed to the
source article):

- def:p15-w02b-p15-069-assumption-family: conclusions as functions of an
  assumption member; status sets and breaking values.
- def:p15-w02b-p15-069-fixing-error: substitution error phi_i(c).
- def/thm:p15-w02b-p15-069-coupling: binary coupling P_rho with fixed fair
  marginals; three-input law Q_rho with X_3 = epsilon X_1.
- thm:p15-w02b-p15-069-linear-two: two-factor linear model under P_rho;
  ranking preserved for |rho|<1 (with proof that this cannot reverse);
  sum of first-order indices differs from 1 for an additive model;
  S_i <= S_Ti fails; threshold P(Y>2) <= 1/10 holds iff rho <= -3/5.
- thm:p15-w02b-p15-069-duplicate: Y = 2X_1 + X_2 under Q_rho; first-order
  ranking of X_2, X_3 reverses at |rho| > 1/2; total ranking of X_1, X_2
  reverses at |rho| > sqrt(3)/2; S_T3 = 0 throughout.
- thm:p15-w02b-p15-069-fixing: lower bound V S_Ti for any law; under
  independence of X_i from X_{-i}, average substitution error 2 V S_Ti and a
  constant achieving at most that; under Q_rho the bound fails for
  rho^2 > 1/2 and S_T1 = 0 at |rho| = 1 while phi_1 >= 4/5 V.
- thm:p15-w02b-p15-069-formulation: f_gamma = x_1 + gamma x_1^2 + 2x_2 with
  identical baseline value and gradient; ranking reverses iff
  gamma^2 > 45/4; sure bound f <= 3 holds iff gamma <= 0.
- def:p15-w02b-p15-069-report (method), def:p15-w02b-p15-069-worked-report
  (two report tables), def:p15-w02b-p15-069-limits (warning).

All exact values were checked by exact rational enumeration (Python
fractions) for the binary laws and by closed-form moments for the uniform
case before writing.

## Source and locators

Held file: source/references/p15-global-sensitivity/saltelli-annoni-2010.pdf,
sha256 fba86067787db902321e536df82aa0631440b6402f716b2181768ce6296e0ddc
(matches held-sources.json), opened in this session by text extraction.
Locators used, each seen in this session:

- p. 1509, Section 2: global approach as showing a desired inference holds
  while input assumptions vary over plausible ranges; Leamer's organized
  global sensitivity analysis as quoted there. Paraphrased, not quoted.
- p. 1512, Section 5.4: Equations (1) and (2) for S_i and S_Ti; S_Ti
  recommended for fixing non-influential factors; recipes cited for
  independent inputs; non-independent case referred to Saltelli and
  Tarantola (2002) and Da Veiga et al. (2009). Those two works are not held
  and nothing from them is presented.

Seven-word n-gram overlap check against the extracted source text: none.

## Ownership note

The packet lists ED26-SCI-SaltelliAnnoni2010-001 under readonly_units with
owner w02b-p15-068. The r1 results show w02b-p15-068 closed with no open
components for that unit and is not in the r2 carry-over list, while this
packet's own r1 assessment left C04 partial and the r2 task text directs
this packet to close it. The new material is therefore written in this
packet's owned files only; no file of w02b-p15-068 or the existing host was
edited. The lead should decide whether this conflict needs a ruling.

## Continuation

- C04 gap: written (body and annex as above); unit-compile ok (4 overfull:
  two annex headings from long annex ids, two from the bibliography entry
  of SaltelliAnnoni2010Sensitivity, not from these files).
- check.py --tree handbook: no finding mentions these files.
- find_fused_spaces: no hits.
- Open for the lead: apply work/waves/w02b/patches/w02b-p15-069.json;
  insert the body and annex inputs after global-sensitivity-and-robustness
  in handbook/parts/p15.tex (line 70) and handbook/annex/p15.tex (line 69).
- Nothing further pending in this packet's owned files.
