# Hertwig-Kozyreva 2021 bounded rationality: source and authoring record

Date: 1 October 2026. Assigned unit `ED26-BM-RAT2021-8-5`, components
C01-C05. The full catalog row and actual P17/P19 prerequisite interfaces
were read before writing. Body and annex ownership is disjoint; shared
drivers, style, canonical records and generated outputs belong to root.

## Selected source and finite dependency set fixed before authoring

- Hertwig and Kozyreva, 2021, *Bounded Rationality: A Vision of Rational
  Choice in the Real World*, chapter 8.5 in *The Handbook of Rationality*,
  printed 505-515. Exact held source
  `source/references/knauff-spohn-2021/s039900-mpg-copy.pdf`,
  14 physical pages, 401,780 bytes, SHA-256
  `4311A58AD7062F1A763382FD3ABFC0F9455FBA6A8EE166E6BCE420D2B298B70C`.
  The complete chapter, notes and references were read, including all eleven
  substantive printed pages. Physical page 12 is blank apart from the
  download notice; pages 13-14 identify the book, 2021 publication, ISBNs,
  publisher and copyright. Chapter DOI is
  `10.7551/mitpress/11252.003.0053`, distinct from the whole-book DOI.
- Simsek's original 2013 NeurIPS *Linear Decision Rule as Aspiration for
  Simple Decision Heuristics*: bounded dependency for the precise
  noncompensation definition, its linear-decision comparison and the
  source's computational environment claims. Its actual experiment inputs
  and evaluation details must be read before reporting new statistics.
  The citation does not silently add a whole-book obligation.
- Campbell, Hoane and Hsu's 2002 *Deep Blue* technical article: bounded
  dependency for actual search-throughput measurements and architecture.
  Silver et al. 2018, the chapter's cited AlphaZero paper, supplies only its
  inspected introductory description of alpha-beta search and adaptations;
  its intro does not supply the chapter's 300-million-per-second number.
  The technical measurement and conditions will govern the active numerical
  statement, with any correction provenance kept in this note.
- Existing handbook proofs: finite preference/utility, sequential decision
  and empirical evidence-record interfaces named by the parent. The new
  worked choice/environment comparison will use explicitly stipulated
  values and receive full mathematical derivations if a theorem is claimed.

Qualitative historical and research-program claims are attributed to the
selected chapter. Its firefighter, ant, Linda, car-search, prospect-theory
and decision-aid examples will retain their source status and limitations.
No participant counts, effects or generalization statistics will be invented
where the selected review supplies none. The original bibliography remains
the chapter's provenance trail rather than an automatic mandate to acquire
every cited book in full.

The research/PDF workflow supports source reading. Manuscript builds,
renders, review waves and prose-test suites are deferred as directed by
the user. Authoring and independent acceptance are distinct.

## Acquired dependency identities and exact reading

The selected chapter's ant illustration, Figure 8.5.1 on printed page 508,
was also inspected from an actual source-page render. It is an illustrative
drawing rather than an observed ant-tracking dataset. Its mechanism and
qualification are preserved in prose; no measured path lengths were invented.
Pypdf's font-decoding warnings did not obscure the prose or named sections.

- `source/references/p17-rationality-8-5/simsek-2013-linear-decision.pdf`:
  exact nine-page NeurIPS 2013 paper, 225,301 bytes,
  SHA-256 `884697574405ACDD73089AEE63A7EB35CA82DF9F5D074C8ED7E167951B3B543B`.
  [Proceedings PDF](https://proceedings.neurips.cc/paper/2013/file/e48e13207341b6bffb7fb1622282247b-Paper.pdf).
  All nine pages were read, including references. The body's selected
  dependencies are section 2.3's exact binary noncompensation condition,
  and section 4's design and noncompensation results, with section 5's
  explicit limitation on transfer to actual heuristics. Its approximate
  dominance method is not introduced or claimed reconstructed here.
- `source/references/p17-rationality-8-5/campbell-hoane-hsu-2002-deep-blue.pdf`:
  Artificial Intelligence 134 (2002), 57-83, DOI
  `10.1016/S0004-3702(01)00129-1`, 27 pages, 171,823 bytes,
  SHA-256 `DB5AA5F355CDC2BC05DE29B43A1208089FD68ACEA1CA0E13BC590C1724DDCE7C`.
  [Held mirror](https://www.cs.oswego.edu/~mgrzenda/CSC466/Paper%20Sources/Deep%20Blue.pdf).
  Read printed pp57-60: identity, distinction between the 1996 and 1997
  systems, relevant architecture and the complete throughput paragraph.
  The actual report describes the 1997 match average for searches longer
  than one minute as 126 million positions per second and the maximum
  sustained speed as 330 million. Tactical positions were about 100
  million and quiet positions typically near 200 million. The PDF's
  2001 copyright is distinguished from its printed 2002 publication.

Silver et al. 2018's inspected introductory passage describes alpha-beta
search and domain-specific adaptations, with a citation to the Deep Blue
technical paper. It does not itself give a 300-million throughput figure.
It was used to locate and check that attribution chain; the manuscript
uses the acquired primary engineering report for the numerical statement.
The whole-paper DOI is `10.1126/science.aar6404`; the inspected public PDF
was https://ailab-ua.github.io/courses/resources/science_alphazero_december_2018.pdf.
No full Silver treatment is claimed by this unit.

## Completed source correspondence and components

Body: `handbook/parts/p17/rationality-8-5.tex`.
Annex: `handbook/annex/p17/rationality-8-5.tex`.
The chapter has three new reciprocal statement/proof pairs. The annex
contains only those genuine analytical derivations, rather than invented
mathematical proof statuses for historical, conceptual or empirical claims.

| Selected source extent | Supplied treatment |
| --- | --- |
| Summary, section 1.1, pp505-506 | Bounds as a principle versus positive and prescriptive theory; early organizational limits and the 1955/1956 development; substantive, procedural and ecological distinctions; scissors and labyrinth; original terminology and classical target. |
| Section 1.2, pp506-507 | Exhaustive states and outcomes, values and probabilities; small-world assumptions and unforeseen consequences; firefighter recognition/mental checking; epistemic and aleatory uncertainty; chess growth, qualified throughput and selective search; unclear social rules, many actors and conflicting goals. |
| Section 1.3, pp507-508 | All four principles: process realism and the Friedman objection; approximate methods with sophisticated capacities; satisficing, adjustable aspirations and disappearing options; ant/environment interaction and the limits of its illustration. |
| Section 2.1, pp508-509 | Costly search and the car example; expected marginal returns/costs; Good's prior 1952 contribution; Simon's information, opportunity-cost and computation burden objection. The exact finite optimization proofs remain separate prerequisites. |
| Section 2.2, pp509-510 | Probability/statistical/coherence benchmarks; representativeness, availability and anchoring/adjustment; actual error examples; three attribute-substitution conditions; Linda and the inclusion-law/response interpretation distinction; fictional systems 1/2 and fatigue; original risk-domain prospect theory; all three objection lines. |
| Section 2.3, pp510-512 | Adaptive toolbox and correspondence criteria; competing strategies and environments; three discoveries; environment-generating theories and risk-reward/foraging example; accuracy-effort versus less-is-more; fitting versus prediction and bias-variance mechanism; cue structure and lexicographic rules; engineering decision aids, boosting and nudging. |
| Section 3, p512 | All stated 2021 research directions: environmental taxonomy, interaction-generated complexity, cognitive tools beyond simple heuristics, and integration of heuristics/search/learning. Their present status is not inferred. |
| Notes 1-6, p513 | Initial residual conception; multiple classical-rationality names and coherence standards; uncertainty/probability duality; Simon's uncertainty/imperfect-competition objection; Good's earlier cost account; different Vernon Smith ecological-rationality concept. |
| Acknowledgments and bibliography, pp512-515 | Read for attribution and the chapter's complete provenance trail; the selected dependencies are identified separately above. No individual reference silently adds a whole-book obligation. |

Component dispositions for authoring:

- **C01:** written. The complete held chapter was read and represented as
  its identified source-specific account of resource limits, environment
  structure and feasible choice.
- **C02:** written. Definitions, principle/positive-theory/prescription
  distinctions, all four Simon principles and all three research programs
  are explicit; no single ideal optimization model substitutes for them.
- **C03:** written. Actual firefighter, chess, ant, partner search, car,
  Linda, prospect theory, representation/adaptation, cue and policy-aid
  examples remain with their actual types and limitations. The new
  prediction, cue-budget and aspiration examples are labelled stipulated.
- **C04:** written. The exact existing weak-preference, finite-vNM,
  sequential-model/backward-recursion and empirical-record interfaces are
  connected with their hypotheses intact. Their mathematical conclusions
  are not mistaken for input discovery, cognitive mechanism or deployment
  evidence. The source's objections and program distinctions remain.
- **C05:** written for the selected extent. The chapter is argumentative
  and comparative, without an original mathematical theorem-proof sequence.
  Every new formal claim in this treatment has its full proof. Numerical
  evidence uses the acquired primary dependencies under the declared
  measurement and evaluation conditions. Review-level qualitative claims
  retain their source-reported standing, without invented samples or
  confidence statements. Independent admission remains pending.

## Direct precision corrections and evidence limits

The chapter's search-tree number is treated as the conditional product
30 to the power 80, approximately 1.48 times 10 to the power 118. It is
not an exact count of legal positions or a proof of a general complexity
class result. The active throughput account replaces the unqualified
300-million shorthand with the engineers' measured average/peak conditions;
this does not claim that the original peak interpretation was impossible.

The informal correlation description of a noncompensatory cue is replaced
by the precise decision-rule weight condition in Simsek section 2.3.
High correlation alone is not a weight-dominance theorem. The binary
proof retains all nonnegative coefficients and handles zero-weight cues,
negative original cue directions, strict inequality and tie cases explicitly.

Training-fit monotonicity is qualified by nested classes, a shared objective
and attained/global minimization. Parameter count alone is insufficient.
The squared-error identity states finite moments and independent future
test noise and then proves every mixed term vanishes. Its numerical risks
are stipulated analytical examples, not estimates of human behavior.

The computational dataset record preserves 51 selected datasets, the
12-601 object and 3-21 attribute ranges, preprocessing and missing-data
handling, elastic-net training selection, pair-based evaluation and five
seed replications. Its 0.85/0.96 medians measure agreement with the full
linear comparison, not predictive accuracy or the prevalence of a human
strategy. Preprocessing uses dataset objects; this is not described as
isolated prospective preprocessing. Shared objects and seeds do not create
independent populations, and the reported medians have no supplied
population sampling confidence interval. No rerun or data reproduction
is claimed. All independent empirical/publication gates remain distinct.

## Local checks, intake ownership and root handoff

The writer read the complete resulting body and annex. A bounded label/status
check found three exact reciprocal pairs, all ten symbol first-use labels
in the actual files, no duplicate local labels and no body proof environment.
The worked arithmetic is explicit in the full proofs and satisficing
calculations. No review wave, manuscript build/render or prose-test suite
was run. This is authoring evidence rather than independent acceptance.

Unique intakes:
`handbook/bib/intake-p17-rationality-8-5.bib` (three identities) and
`handbook/registry/symbols-intake-p17-rationality-8-5.csv` (ten rows).
Root still owns routing, canonical merges and generated apparatus.

Suggested exact scope bindings:

```json
{
  "P17 bounded-rationality squared-error comparison": {
    "presentation": "The explicitly stipulated fixed-input training/test risk comparison",
    "regions": [
      {"anchor": "thm:p17-br-bias-variance"},
      {"anchor": "annex:p17.br.bias-variance"}
    ]
  },
  "P17 bounded-rationality squared-error proof": {
    "presentation": "Mean mu of the trained prediction in the variance proof",
    "regions": [{"anchor": "annex:p17.br.bias-variance"}]
  },
  "P17 bounded-rationality noncompensation comparison": {
    "presentation": "Oriented nonnegative weights and binary difference values",
    "regions": [
      {"anchor": "thm:p17-br-noncompensation"},
      {"anchor": "annex:p17.br.noncompensation"}
    ]
  },
  "P17 bounded-rationality noncompensation proof": {
    "presentation": "First discriminating positive-weight index r",
    "regions": [{"anchor": "annex:p17.br.noncompensation"}]
  },
  "P17 bounded-rationality feasible-choice example": {
    "presentation": "Alternative vectors a and b and the stipulated evaluation environments N and C",
    "regions": [
      {"anchor": "def:p17-br-cue-instance"},
      {"anchor": "thm:p17-br-environment-contrast"},
      {"anchor": "annex:p17.br.environment-contrast"}
    ]
  }
}
```

Final authoring snapshot:

| Artifact | Lines/bytes | SHA-256 |
| --- | --- | --- |
| Body | 476 lines / 28,215 bytes | `4F6A1A65EF16C44BB7761F36457ACE7150D80E323B6B2663F6DA3EF2D34AA1F1` |
| Annex | 71 lines / 3,634 bytes | `1B11817E42811029221C8AB4F0E2556F262DA8AFA3981E23318FA11D12D67D7A` |
| Symbols | 10 rows / 2,571 bytes | `2598E38BE3AC2EE0BACED8EF0BE98996EBE884F8E96440B0A78962F45318B8A0` |
| Bibliography | 3 entries / 1,778 bytes | `98529CA6DD375D6FED89B1C01377541E2BCBDEFCAE64C5B71F438B451D8B78EC` |

No missing source or authoring component is identified in this selected
unit at the handoff. Root integration and the later consolidated independent
content, static, build and publication checks remain unfinished.
