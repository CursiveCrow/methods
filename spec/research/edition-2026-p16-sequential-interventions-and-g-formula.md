# P16 authoring: sequential interventions and the longitudinal g-formula

Date: 8 September 2026. Author block began 15:59:23 UTC, with a maximum
45-minute extent. This is an authoring/source handoff, not an independent
review or an admission record. All manuscript changes precede consolidated
reviews under the user's current instruction.

## Owned outputs and integration

- `handbook/parts/p16/sequential-interventions-and-g-formula.tex`
- `handbook/annex/p16/sequential-interventions-and-g-formula.tex`
- this note
- `handbook/bib/intake-p16-longitudinal-whatif.bib`
- new source directory
  `source/references/hernan-robins-what-if-longitudinal-2026/`

The three assigned manuscript/note paths and the bibliography intake were
absent before authoring. No older manuscript, shared driver, registry,
canonical bibliography or review report was edited. Root owns integration.
The section can follow the existing counterfactual and identification
treatments; its direct mathematical prerequisites are the finite probability,
structural-model and counterfactual treatments, not ID or IDC.

## Primary acquisition and actual version

Author's page, opened on 8 September 2026:
https://miguelhernan.org/whatifbook

The page offers the full book freely and links its current download through
`https://miguelhernan.org/s/hernanrobins_WhatIf_19aug26.pdf`, redirecting to:
https://static1.squarespace.com/static/675db8b0dd37046447128f5f/t/6a86cf7ecfcb6b4ca8eea5cb/1787219838424/hernanrobins_WhatIf_19aug26.pdf

Local file:
`source/references/hernan-robins-what-if-longitudinal-2026/hernan-robins-what-if-19aug2026.pdf`

- Full downloaded extent: **365 PDF pages; 11,315,465 bytes**.
- SHA-256: **A1067AF923E9156BB95FBE4B0D18699BD0723E9C902BDC74465CF7782820B1B5**.
- Actual title page, PDF page 2: *Causal Inference: What If*, Miguel A.
  Hernán and James M. Robins, **August 19, 2026**.
- Copyright page, PDF page 3: copyright 2020, 2026 by the authors; suggested
  publication citation remains Hernán and Robins (2020), Chapman & Hall/CRC,
  Boca Raton. Copyright permission is not inferred from free downloading.
- PDF creation metadata: `D:20260819102943Z`; modification metadata:
  `D:20260820055021-04'00'`. These corroborate the version; the title page
  supplies its actual displayed date.
- New citation key: `HernanRobins2020WhatIf2026`. Its note preserves the
  19 August 2026 author version separately from the suggested 2020 citation.

The search also found a 2 January 2025 revision and older downloads. They
were not substituted for the author's live version. An initially requested
2025-named source-directory permission was unused; the actual capture is
only in the 2026 directory. The default filesystem/TLS capture failed; one
exactly scoped escalated download succeeded. No paid access was used.

## Selected source extent actually read

The title/copyright/contents were read before selecting the chapters. In
this version the printed page equals the PDF page number minus nine over
the selected body extent. Full text was read for every page in **printed
255–291 (PDF 264–300)**, including all intervening technical/fine points:

- Chapter 19, *Time-varying treatments*, pp. 255–266: all six sections;
  deterministic/random strategies; Technical Point 19.1 on recursively
  removing past-action arguments; sequential consistency and policy-specific
  positivity; outcome-only, joint one-world and full cross-world forms of
  exchangeability; static/dynamic distinctions.
- Chapter 20, *Treatment-confounder feedback*, pp. 267–276: all five
  sections, hypothetical Table 20.1, null feedback, collider conditioning,
  causal-path adjustment and past-treatment qualifications. Page 276 is blank.
- Section 21.1, *The g-formula for time-varying treatments*, pp. 277–281:
  conditional-history standardization, Table 21.1, joint trajectory versus
  outcome-only interpretation, and Technical Point 21.1's deterministic
  and random-policy formulas.
- Section 21.2, *IP weighting for time-varying treatments*, pp. 282–285:
  nonstabilized and stabilized weights; Technical Point 21.2's dynamic
  indicator and stochastic density-ratio identities; fitting caveats.
- Pages 286–291: the complete Section 21.3 and its technical points, followed
  by the beginning of Section 21.4, including Technical Point 21.6 and
  **Fine Point 21.2, Representations of the g-formula**, p. 291. The latter
  explicitly relates joint-density, ICE and weighting representations.

For contextual comparison, all of printed **300–304 (PDF 309–313)** was
also read: Section 21.6, *The big g-formula*, and Technical Points 21.11–21.13.
Their separate front-door/SWIG and structural-nested-model extensions are
not claimed as newly supplied by this component. The whole 365-page book
was acquired, but it was not read in full.

Source-only Poppler images were generated for PDF pages 264–294. The actual
images of PDF pages 266, 270, 271, 278, 287, 290 and 293 were read to resolve
strategy definitions, joint exchangeability notation, source counts, and
the g-formula/IPW displays. All selected pages were read in extracted text;
no manuscript PDF was generated or inspected. Source images reside in the
old task's `tmp/pdfs/p16-longitudinal-source/` scratch directory.

## Mathematical extent and source distinctions

Twelve body results have full annex proofs, with suffixes:
`sequential-policy-semantics`, `sequential-exchangeability-bridge`,
`sequential-structural-bridge`, `sequential-support`,
`sequential-joint-g-formula`, `sequential-outcome-g-formula`, `sequential-ice`,
`sequential-ipw`, `sequential-source-feedback`, `sequential-feedback-effects`,
`sequential-failures`, and `sequential-weight-boundaries`.
Body prefixes are `thm:p16-`; matching annex prefixes are `annex:p16.`.

The manuscript defines a common finite potential-trajectory table with
no anticipation and sequential consistency. A stochastic policy is evaluated
with independent finite selector entries, one for every time/history,
independent of the entire original outcome space. This supplies policy
counterfactuals before any policy distribution or conditioning is used.

Two source routes remain distinct and fully proved. The backward
outcome-only proof requires exchangeability for the one deterministic
policy's response and does not identify its covariate trajectory. The
full trajectory proof uses joint fixed-world future-covariate/response
exchangeability. A cellwise event bridge proves that these joint static
conditions are equivalent to the joint deterministic dynamic family,
without requiring independence of the collection of all counterfactual
worlds. Independent stochastic selectors then give an exact path formula.

The structural bridge imposes actual private treatment randomization
conditional on the measured history; it proves full exchangeability by
conditional finite factorization. Shared background causes of covariates
and response are allowed. None of these causal assumptions is asserted to
follow from an observed distribution alone.

The support condition is imposed on the positive branches selected by the
policy. Its observed-law equivalent, positive prefix propagation, agreement
with the true policy history distribution under the joint theorem, and
independence of null conditional versions are proved. Zero branches are
terminated before an undefined conditional is requested. IPW proves the
mass identity on positive observed paths by cancelling individually positive
denominators; absolute continuity proves zero on the complement. Setting
policy kernels equal to observational kernels is also proved to reproduce
the observational population law, with a counterexample to unitwise equality.
The support equivalence is proved in both directions by stopping the joint
path proof at a proposed first support failure. A separate equal-observed-law
example shows that outcome-only exchangeability does not identify the
intervened covariate law; its apparent reachable-history distinction is
therefore an explicit theorem boundary rather than an implicit substitution.

The source's hypothetical 32,000-count example is retained, with its exact
g-formula and weighting calculations. A new finite latent-threshold model
realizes all of its counts and means under the pointwise sharp null; its
complete sixteen-cell response table is supplied. A second, non-null
feedback model calculates every observed mass, four static values, two
dynamic values and two stochastic-policy values through all three routes.

Three explicit assumption failures cover unsupported actions, positive-law
nonidentification without exchangeability, and a static-exchangeability
example with separate future marginal independences but a failed dynamic
target. A further example calculates the wrong dynamic stabilized ratio.
The only sampling result is proved finite unbiasedness of a sample average
using true weights. A fixed incorrect denominator already supplies a
counterexample to unqualified replacement by fitted probabilities.

The binary strategy count is written correctly as 2^(K+1) for times 0,...,K;
the source uses 2^K in several surrounding passages while elsewhere explicitly
calling the treatment vector K+1 dimensional. This elementary count is
proved directly rather than copying the mismatch. The source's approximate
54.7 and -13.3 in the feedback example are evaluated exactly as 164/3 and
-40/3. No expository passage was copied wholesale.

## Prerequisites, notation and exact next requirements

Read authoring interfaces: `handbook/CONVENTIONS.md`,
`spec/EDITION-2026-CONTRACT.md`, the complete body/annex of
`finite-counterfactuals.tex`, and the finite structural-model definitions,
existence/uniqueness and equation-replacement interfaces in
`handbook/parts/p16/finite-causal-models.tex`. The current contract's
all-changes-before-reviews sequence governs this handoff.

Local typed notation for root's registry integration: K; L_k, A_k, Y and
their finite sets; O; barred prefixes and H_k/h_k; potential tables and
the complete tuple T-calligraphic; g, g', pi_k; selector R_(k,h); O^pi and
policy value psi; future tuple T_k(a); SE--Y and SE--J; observed baseline b,
assignment e_k, transition/terminal r_k; reached masses m_k; RP; functional
q_pi; terminal response function phi; backward B_k,V_k; and weight W^pi.
These roles are local to this section, especially V_k (a backward value,
not a structural vertex coordinate) and q_pi (a trajectory mass, not the
background mass q). Root owns canonical notation and bibliography merging.

The component's finite policy semantics, identification, ICE and true-weight
IPW proofs have no remaining authoring gap. Estimation with fitted models,
asymptotic inference, multiply robust methods, g-estimation, censoring,
continuous kernels, optimal-policy learning, and policies depending on the
current natural treatment are separate treatments; no result for those
extensions is silently asserted here. Independent review, integration and
all later admission requirements remain with the completed manuscript batch.

The author read back the complete actual LaTeX body and all twelve full
annex proofs, then applied and read the definition, support-equivalence,
worked-table and display corrections. The source note and bibliography
intake were also read in full. No independent reviews, scanners, tests,
manuscript builds, manuscript renders or acceptance checks were run.
