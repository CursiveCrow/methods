# Missing evidence and selective reporting

Authoring checkpoint: 1 October 2026. Assignment:
`ED26-METHOD-missing-evidence`, components C01--C05, from the exact
`additional-method-units.jsonl` row. The reader destinations correspond
to proposed contents 175.7--175.11. The new body introduces five sections
within evidence synthesis; it does not create a second meta-analysis chapter.
The author owns only this body/annex, unique intakes, this source note,
and disjoint source/scratch captures. Shared routes and canonical files
are reserved to the lead.

## Exact selected chapter and history

The [chapter-13 citation](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-13)
identifies Matthew J Page, Julian PT Higgins and Jonathan AC Sterne,
*Assessing risk of bias due to missing evidence in a meta-analysis*,
Cochrane Handbook version 6.5, last updated August 2024. The
[current handbook index](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current)
still identifies version 6.5, 2024. The official
[versions and changes record](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/versions-and-changes-handbook)
states that the 2024 chapter-13 update introduces ROB-ME. Its later
6.5.1 entries list chapter-4/chapter-14 corrections in 2025 and a
chapter-3 change in 2026; no chapter-13 change is listed there.
The captured current body therefore matches the selected explicit
chapter citation and listed revision history. A later whole-handbook
correction number has not silently replaced this chapter presentation.

Public source captures in
`source/references/missing-evidence-cochrane-2024/`:

- `chapter13-current-retrieved-2026-10-01.html`: 186787 bytes;
  SHA-256 `32DECF2E86754D2DB28DF5DDDCC5169161A5A523FD5C6AC438A3BDD2FE2640F8`.
- `handbook-current-index-retrieved-2026-10-01.html`: 82062 bytes;
  SHA-256 `691F9EEDF4866E3D66830ACBA584D6C07F799D62F06B1468F15E12A0CB9D08A4`.
- `versions-and-changes-retrieved-2026-10-01.html`: 94144 bytes;
  SHA-256 `7A5BA2534DF3B32B0B77E05A00E3B09C7899B2732F9D34482ECDAAE6AC134F9E`.

Sections 13.1--13.4 were read in full, including nested subsections,
tables, figure descriptions, the summary and MECIR Box 13.4.a. The
selected text includes 9909 whitespace-delimited words and 26 headings
when extracted from the captured content between `section-13-1` and
`section-13-5`. Source chapter PDFs are restricted to registered
Cochrane contributors; the complete public HTML supplies the assigned
body without paid access or an account. Web retrieval and local lxml
extraction were used. BeautifulSoup was not installed; no dependency
installation was needed.

The source's empirical counts and hypothetical plots are not generalized
into universal propositions. The new empirical example was checked
against its primary study, while the mathematical examples are expressly
stipulated. The selected chapter does not supply a mathematical proof
that a completed search contains every eligible study.

## Exact operating tool dependency

The [official ROB-ME page](https://www.riskofbias.info/welcome/rob-me-tool)
currently offers the 1 October 2023 version, separately from its
24 October 2020 preliminary archive. The two linked official operating
documents were downloaded through their public Drive identifiers:

- `rob-me-cribsheet-20231001.pdf`: 648027 bytes, 15 pages;
  SHA-256 `70B26F8F5CA349A2D75FEEB505100BF5510DFC2CE88D65FB2FB6B7002802E6C6`.
  All 15 pages were read. Page 13's suggested algorithm was rendered
  and inspected at `tmp/pdfs/p15-missing-evidence/rob-me-algorithm-page13.png`.
- `rob-me-template-20231001.docx`: 57328 bytes;
  SHA-256 `3BEC0C33314E9D6E940C6ADDEE952839FD35A2596FEB23B273D889074BB4143A`.
  Its complete main document XML was read, including its version,
  planning questions, results matrix, eight signalling questions,
  conditional applicability and final judgement fields.

The short-version document contains the detailed operating information
needed by the chapter: Step 1 p.2; Step 2/results matrix pp.3--4;
Step 3 review-wide questions p.5; Step 4 and questions 4.1--4.8 pp.6--10;
classification scenarios p.11; suggested judgement graph p.13;
and its accompanying table pp.14--15. The original forms and protected
figures were not pasted into the manuscript. The prose reconstructs
the method and its branches with attribution.

Two interpretation details were preserved:

1. Planning question 3.1's affirmative inception-cohort response is
   protective. It cannot be counted as an affirmative high-risk signal.
2. Question 4.8 permits no/probably no if no sensitivity analysis was
   attempted. The manuscript records that case without promoting an
   unperformed analysis into evidence of stability. Question 4.7 can
   be not applicable when too few results exist to assess a pattern,
   but the suggested graph does not display an exit for every such
   allowed answer. The manuscript preserves the answer and requires
   a reasoned judgement, rather than inventing a no/low-risk transition.

This latter point is a documented source-algorithm boundary, not a
missing source body or an unperformed author proof. ROB-ME proposes an
assessment judgement; its graph is not a theorem that answers uniquely
determine the actual bias or its magnitude. The manuscript does not
claim to implement a corrected or validated software version of the tool.

## Primary historical example

The exact dependency for the one empirical numerical example is Eyding
et al., BMJ 2010;341:c4737, DOI 10.1136/bmj.c4737, PMID 20940209,
[PMCID PMC2954275](https://pmc.ncbi.nlm.nih.gov/articles/PMC2954275/).
The full primary HTML was captured as `eyding-2010-pmc2954275.html`,
244387 bytes, SHA-256
`CAB06C045EA00A82FF6C59C597A423D687FB0FD7B2B73845FA953E77E3EF9163`.
Its abstract, eligibility, search/data-extraction methods, study selection,
publication details and publication-bias sections were read for the
bounded example. Reading the full primary paper and supplements for
an independent drug-data reanalysis is not claimed.

The paper's 13 eligible acute-treatment trials comprise 4098 patients;
3033/4098 patient data, 74 percent when rounded, were unpublished.
That denominator must not become a trial-count percentage. The article
distinguishes subgroup-only reports and articles without main outcomes
from full result availability. Its required manufacturer submission
included the full trial list, usable study documents and permission to
report previously unpublished data, with incomplete initial cooperation
described. The manuscript reports its published-versus-combined comparison
as that study's finding, not as a universal causal conclusion or current
treatment recommendation. No raw-data reproduction or complete portfolio
census was claimed.

## Required components and complete proofs

- **C01:** Study/report identity; participant outcome domain, instrument,
  metric and time; study-result aggregation/contrast/analysis and precision;
  missing studies, missing results, partial reporting and selection among
  available results; distinct within-study participant missingness. The
  stipulated two/six-week example demonstrates the dependence on eligibility.
- **C02:** Availability mechanisms and a finite conditional selection model;
  exact distribution tilt and covariance shift; inverse-recovery hypotheses;
  identical observed laws with different full means; zero-selection support
  failure. These are independently derived mathematical results.
- **C03:** Search/register/protocol/SAP/regulatory/sponsor strategies;
  original versus amended plans; linked study denominators; recovery attempts
  and unresolved explanations; complete inception frames and their restricted
  targets, precision and applicability. A weighted target decomposition
  proves why a closed cohort does not identify excluded effects.
- **C04:** Every selected ROB-ME step, matrix category, review-wide question,
  the eight result-specific questions, conditional responses and suggested
  grading branches; effect of missing weight and direction; explicit uncertain
  and not-applicable boundaries; known-missing-result range/tipping calculation;
  common/random-effects comparisons, restrictions, selection assumptions
  and regression extrapolation limits. No unattempted analysis or missing
  numerical result is recoded as reassuring evidence.
- **C05:** Standard-error/reversed-scale and effect-scale choices; small-study
  effects from non-reporting, within-study bias, heterogeneity, artefact or
  chance; contour interpretation; test power and scale requirements. A
  rounded ten-study asymmetric plot is proved possible under chance,
  genuine effect heterogeneity and selective availability.

The five reciprocal complete proof pairs are selection, cohort target,
missing-weight bounds, two-study reweighting, and funnel compatibility.
The ROB-ME qualitative risk judgement is not given a mathematical
proved tag implying that it certifies actual bias.

## Integration and author checks

Actual `evidence-synthesis.tex` was read for the existing source scope,
effect/uncertainty and target conventions. Its complete linear, fixed-weight
sensitivity and known-random-effect proofs were inspected where needed.
The new treatment reuses `def:p15-synthesis-missing`,
`def:p15-synthesis-random-model` and `thm:p15-synthesis-sensitivity`.
The earlier chapter-10 treatment remains with its own author; its definitions
and pooling proofs were not duplicated or changed.

The body and annex were read sequentially. Range endpoints, selection
probabilities, covariance/recovery identities, the sign tipping point,
two-study derivative, and positive probabilities for rounded funnel data
were checked as mathematical calculations. The original ROB-ME graph
was used to check each reconstructed ordinary grading path and preserve
its unsupported not-applicable edge. MECIR C73 is recorded as highly
desirable, not silently strengthened into a mandatory standard.

There are three new bibliography keys and twelve symbol rows. The named
symbol scope `P15 missing evidence` requires lead binding to the exact
new body and annex files. All shared files, drivers, canonical records,
generation and coverage baselines remain the lead's responsibility.
No new prose-mirroring tests, children, consolidated reviews, manuscript
builds or manuscript renders were used. Independent review, source-rights
and publication checks retain their separate standing after authoring.
