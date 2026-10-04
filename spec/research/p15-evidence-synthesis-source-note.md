# Evidence synthesis: completed authoring return

Date: 1 October 2026. Unit: `ED26-METHOD-evidence-synthesis`, the exact row
in `spec/coverage/edition-2026/additional-method-units.jsonl`. All five
selected authoring components are supplied. This is not an independent
admission record, and it does not close the adjacent Chapter 13
`ED26-METHOD-missing-evidence` unit.

## Source identity, acquisition and reading

The primary source is Deeks, Higgins, Altman, McKenzie and Veroniki,
*Analysing data and undertaking meta-analyses*, Cochrane Handbook Chapter 10,
version 6.5, last updated November 2024. The exact institutional page was
retrieved on 1 October 2026 and still prints that chapter-specific citation.

- URL: <https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-10>.
- Held body: `source/references/p15-evidence-synthesis/cochrane-ch10-v6.5-2024-11.html`.
- Bytes: 254549; SHA256
  `C0F902161CFBB80C08DA8A91D798EB80F16A70823B76E1BDA71040340856122E`.
- Reading: all Sections 10.1--10.14, including their subheadings, MECIR
  boxes, missing-data table and methodological qualifications. Formula images
  were inspected directly; Figure 10.2.a and all three panels of Figure
  10.10.a were captured and visually read. References in 10.16 are retained
  in the source capture, not represented as individually acquired source bodies.

The institutional version history was also captured and read:
<https://www.cochrane.org/authors/handbooks-and-manuals/handbook/versions-and-changes-handbook>.
It places the Chapter 10 random-effects revisions under version 6.5 (2024).
The later 6.5.1 entries list changes to Chapters 4 and 14 in 2025 and Chapter
3 in 2026. The chapter's own citation retains the specified November 2024
identity. The general Handbook citation's August 2024 date is not substituted
for this chapter-specific date. The source capture contains the current site
wrapper, whose retrieval date is separate from the chapter's identified date.
No claim of byte identity to a separately held November 2024 web archive is made.

Held history: `source/references/p15-evidence-synthesis/versions-and-changes.html`,
94144 bytes; SHA256
`7A5BA2534DF3B32B0B77E05A00E3B09C7899B2732F9D34482ECDAAE6AC134F9E`.

The linked formula dependency is the exact May 2022 eleven-page document by
Deeks and Higgins, *Statistical algorithms in Review Manager*:
<https://documentation.cochrane.org/revman-kb/files/210600101/210600103/1/1654774257333/Statistical_methods_in_revman.pdf>.
Held at `source/references/p15-evidence-synthesis/deeks-higgins-statistical-algorithms-may-2022.pdf`,
211112 bytes; SHA256
`DC6A98E3BA02109DAA5512946539B72AF57FC1FE3CE5A9A2ED2F3C89CC25E712`.
The exact used portions are p.2 (binary Peto/null hypergeometric quantities),
pp.4--5 (Mantel--Haenszel OR/RR table weights), and pp.6--7 (generic weighting
and Peto aggregation). Pages 4--5 were visually checked for the displayed
table formulas; the used equations and their context were read. This older
dependency is explicitly identified in the manuscript and bibliography. It
does not replace the November 2024 REML/HKSJ/prediction/I-squared presentation.
No entire 2022 software-method presentation is marked complete by this unit.

Source image hashes:

| Held filename | SHA256 |
| --- | --- |
| equation-weighted.png | D4FE530432803145FE22C6E234DDC87B02FF564F32BDC60BF8F0AB425AAE57E3 |
| equation-inverse-variance.png | D7F10DC03F8332A5EFB6FB3D51EC5A2D5A621239389812C4EF28B5F25EBFFEF3 |
| equation-smd-logodds.png | 35BC9EE92ED4347F87B07B6212BF02B26613EB612C83779A40043E4E4FA0E173 |
| equation-prediction.png | 93A84736A1AFC7B101D997A1A8E3F8A983536AA27C8C543E73B8B52AA6C51F8F |
| equation-inconsistency.png | FD2D1EB47B260A406C9755D921418CD82D1C925C118BCA721232A032199B76A6 |
| figure-10-2-a.png | 22312FD6A43E0B4E96E3F3763FA70227657B8D8F6B1D941F607E68EF76B40BD1 |
| figure-10-10-a-panel-a.png | 8689CDB7D742ADC3DE7EB3713CAEA0730F27AA251B72F07B81E3FA2D85E5DE79 |
| figure-10-10-a-panel-b.png | 31F36B0FC191278CCB00BECB4F007E2E3D95E0ED3528B9ED75E040861BA92321 |
| figure-10-10-a-panel-c.png | EFAB66DF936CE55A7509DA84B10811A984BEAEC91548AE10F092D3F13AAA4620 |

The five equation images and four figure images are retained for source reading,
not reproduced as handbook illustrations. The mathematical examples in the
chapter are explicitly hypothetical. The local `read-html.py` is only a
reading utility for the frozen HTML; it introduces no software test suite.

## Component completion

| Component | Written treatment and decisive boundary |
| --- | --- |
| C01: estimand/design/scale compatibility | Review/evidence record, common-effect/finite-weight/random-effect targets, adjustment and marginal/conditional distinction, outcome/time/population alignment, exact scale identities, complement and absolute-risk conversions, non-collapsibility construction, change/final-score and logistic-conversion premises |
| C02: weighted estimates and uncertainty | Complete covariance/GLS optimality and known-normal coverage proofs; data-dependent-weight bias identity and explicit counterexample; exact conditional score/information and Peto one-step derivation; specified large-arm MH table-ratio consistency and delta uncertainty proof |
| C03: common effects, heterogeneous effects, prediction | Exact normal random-effects mean/future-effect calculation; DL moment expectation, Q-profile set, REML restricted likelihood and global-maximizer existence; Q/tau I-squared distinction; exact fixed-shape Student theorem; approximate HKSJ/Wald/prediction calculations; proper-prior posterior/predictive variance proof |
| C04: heterogeneity/dependence/missingness/sensitivity | Covariance and shared-comparator proofs, duplicate reports, study subgroup decomposition and observational/ecological limits, outcome-specific/sparse-event boundaries, all Chapter 10 missing-data classes, conditional MAR/MCAR distinction, finite missing-outcome bounds, fixed-weight deletion/bias sensitivity |
| C05: pooling and failures | Full three-study common/DL/HKSJ/prediction/deletion calculation, incompatible measurement/scale cases, duplicate precision failure, subgroup significance-label failure, multiple-comparison probability, ecological non-identification, missing-data sign interval |

The source extent is reflected by the outcome-specific treatment of binary,
continuous, mixed continuous/binary, ordinal, recurrent-event/rate and
time-to-event data; by clinical/methodological/statistical heterogeneity; by
effect modification, subgroup comparison, meta-regression, underlying risk,
dose and ecological/confounding limits; and by missingness, Bayesian synthesis
and sensitivity. Clinical-performance claims from cited external simulations
are not promoted into general mathematical guarantees. Network meta-analysis
and the separate Chapter 13 missing-evidence/ROB-ME treatment are not claimed.

## Formal assumptions and constructed calculations

All 17 proved statements have complete reciprocal annex items. The result
suffixes, following `thm:p15-synthesis-` and `annex:p15.synthesis.`, are:
`scale`, `linear`, `estimated-weights`, `score`, `table-delta`, `change`,
`random-known`, `q`, `reml`, `inconsistency`, `fixed-shape-t`, `bayes`,
`dependence`, `subgroups`, `missing-bounds`, `sensitivity`, and `example`.

Known sampling variances are required for exact inverse-variance, whitening,
Q-profile and known-heterogeneity guarantees. Estimated weights do not gain
those guarantees. The large-arm binary result has a fixed number of studies,
interior fixed event probabilities, independent arms and positive limiting
arm fractions; it excludes sparse-event and increasing-small-study regimes.
Its derived delta variance is explicitly a particular procedure, not silently
identified with every finite-sample formula in the software supplement.

The normal future-observation prediction result explicitly requires independent
normal future error, rather than only an error variance. The exact weighted
Student theorem has deterministic variance-shape weights. Actual HKSJ weights
estimated from the effects generally do not meet that premise. The Q-profile
confidence set is the exact known-variance inversion and is allowed to be empty;
clamping every empty inversion to a convenient boundary interval would be a
different procedure. REML existence is proved without claiming uniqueness.

The posterior uses a proper prior probability measure with stated moment
conditions, and its normalizer/moments are proved finite. The source's informal
discussion of a uniform non-informative distribution is not taken as a proper
uniform law on an unbounded space. Likewise participant MAR is stated
conditionally, distinct from MCAR; generic complete-case unbiasedness is not
inferred from the source's simplified introductory wording.

Constructed arithmetic was recomputed with exact rational numbers and normal
quantiles, not only rounded text. For `Y=(-2,-1,2), v=(1,1,4)`:
common mean `-10/9`, common variance `4/9`, `Q=29/9`, `C=4/3`,
DL variance `11/12`; random plug-in total weight `1692/1357`, mean `-131/141`,
Wald variance `1357/1692`; HKSJ residual factor `1268/1081` and variance
`18703/19881`. The Wald, HKSJ and two prediction interval endpoints were
computed, as were deletion of the third study, the subgroup contrast
`0.1/sqrt(0.41)`, and the multiple-comparison probability `1-0.95^20`.
The manuscript distinguishes exact-model confidence/prediction statements
from these estimated-heterogeneity example calculations.

## Artifacts and integration

- Body: `handbook/parts/p15/evidence-synthesis.tex`, 718 lines, 38800 bytes;
  SHA256 `B5578BA366DB36C25064B081114352BABD4F89513A3B93087195719ADE4D384F`.
- Annex: `handbook/annex/p15/evidence-synthesis.tex`, 501 lines, 26687 bytes;
  SHA256 `863D71E9875C04FBDC89C94F058549098B20BB09C2FA8F11E2594E7AA780CC26`.
- Bibliography intake: `handbook/bib/intake-p15-evidence-synthesis.bib`, two keys,
  `DeeksEtAl2024Cochrane10` and `DeeksHiggins2022RevMan`; SHA256
  `2F0839C46CAAC9F1BDDAAAB756DD52C53B86893C7F71B9F368E249A5CA27B1B4`.
- Symbol intake: `handbook/registry/symbols-intake-p15-evidence-synthesis.csv`,
  51 data records; SHA256
  `EF9A46E6A749621D0AA56EF17F1DDBC7A28ACD803D5254013A5D8022FBE94754`.

The completed body and annex received a full author read-through. All 17
statement/proof pairs and all 51 notation first-use labels were checked in
the actual files; comma-containing macros are correctly quoted in the CSV.
Relevant existing P19 evidence methods and P15 normal/Student/independence
and CLT interfaces were read. No unrelated manuscript files were changed.

Root integration remains: add the two driver inputs, merge the two bibliography
entries and the notation intake, bind its exact named scopes, and project this
return into the authoring coverage record. Distinct local meanings of `a_i`,
`A_i`, `R`, `r`, and `c` are declared in the actual relevant environments and
are retained in the separate scope records. No named scope should be widened
to the whole part merely to suppress a role conflict.

No selected authoring component remains unwritten. Independent source,
mathematical and publication reviews, shared integration checks, manuscript
compilation and final rendered-page inspection remain pending. No such gates
were run or claimed during this authoring block. No source Ch13 text, shared
driver, canonical bibliography, canonical notation, style or generated file
was edited, and no child agent was created for this assignment.
