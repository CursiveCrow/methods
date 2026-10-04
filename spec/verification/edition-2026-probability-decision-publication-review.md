# Probability and decision foundations: independent publication-text review

Reviewer: `/root/probability_decision_publication_review`, fresh nonauthor context. Review ran on 7 September 2026 from 21:00 to 21:12 Pacific time, within the assigned 45-minute block. Repository: `C:/Dev/the-methods-of-reason`; observed HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The reviewed manuscript files are untracked working-tree content, so the file hashes below identify this review's text. No other current reviewer report was read.

## Scoped verdicts

| Treatment | Verdict | Judgment |
| --- | --- | --- |
| Measurable probability and random variables | PASS | The complete body and ten proofs supply the stated measure, observation, limit and distribution claims with usable domains and explicit existence/integration boundaries. |
| Finite lotteries and expected utility | PASS | The complete body and six proofs define the lottery preference independently of finite ordinal representation, supply the representation and uniqueness arguments, and give a usable finite-menu method and explicit counterpreferences. |
| Monetary risk and risk aversion | PASS | The complete body and seven proofs retain the finite-support monetary domain, distinguish global and local risk comparisons, and prove the continuous wealth-invariance characterization without adding a differentiability premise to it. |
| Bibliography, notation and candidate navigation | PASS | All 34 new rows and their table/index entries were read. One local-role omission was corrected by the integrator and its actual projections reread at the final hashes below. The active routes preserve dependency order. |

No actionable publication-text defect was found in the six treatment files. These judgments concern the stated units and their current text. They provide no admission of the broader P15-U1 or P17-D2 obligations, complete source lectures, or the edition.

## Complete manuscript reading and identity

Every line of each file in this table was read, including all examples, warnings, boundaries and complete proofs. Truncated command output was reread over the omitted spans before recording complete coverage.

| File relative to `handbook/` | Read extent | SHA-256 |
| --- | --- | --- |
| `parts/p15/measurable-probability.tex` | 1-484 | `C249F33E0E0FC88084B05A7D44098DB87B3E4814083B34709D6DBE2B562340D9` |
| `annex/p15/measurable-probability.tex` | 1-481 | `FBB9E6C733A1F286F7E56FC31B7E76D4412D781E03711ED02D8D4B3AAEF8C8FC` |
| `parts/p17/finite-expected-utility.tex` | 1-390 | `6F83B6CB0300B241C8751E48747B577FB5869A02418C1C8C621E808515DD6EB5` |
| `annex/p17/finite-expected-utility.tex` | 1-340 | `C04B72A6DDC4B34147359A776597B99A16E4DE6D61A7C4789F5C413CF2FF11D3` |
| `parts/p17/risk-aversion.tex` | 1-355 | `F2B0A4CF575723E4CB6F8212077A59E64E276DAA43A5B25B57374D8E6657CD4A` |
| `annex/p17/risk-aversion.tex` | 1-417 | `1FAEAA08391C801C52CC0814189AE4B7FB4FB26DE788C0F7789D62D46917DC7A` |

The four actual dependency files were also read completely, including their proofs, rather than relying on their historical review status:

| File relative to `handbook/` | Read extent | SHA-256 |
| --- | --- | --- |
| `parts/p15/finite-probability.tex` | 1-467 | `934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1` |
| `annex/p15/finite-probability.tex` | 1-284 | `7CE651CE52FE8BFA66E5BEC221BDF48EE6318538E6A99B8E987E18C90D6B67F3` |
| `parts/p17/finite-preferences.tex` | 1-330 | `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C` |
| `annex/p17/finite-preferences.tex` | 1-324 | `B141A371731E7A0A3BEFF1C88C839F98720BE4F894A2D475CAF098A61159202C` |

The edition contract, handbook conventions, both author intakes (174 and 54 lines), and all four P15/P17 body/annex wrappers were read completely. The P15 route places the measurable chapter after finite probability. The P17 route places finite expected utility and then monetary risk after finite preferences. The annex routes follow the same dependency order.

## Promised proof audit

Each row identifies the actual body result and its reciprocal annex item by their common suffix; prefixes are `thm:p15-`/`annex:p15.` or `thm:p17-`/`annex:p17.`. All 23 pairs were followed in both directions and their entire proof text read. The line columns give body result start and complete annex-item extent.

| Unit and result suffix | Body line | Annex lines | Publication-text check |
| --- | --- | --- | --- |
| P15 `generated-events` | 49 | 12-35 | Empty events, relative complements, arbitrary nonempty intersections and smallest generated collection. |
| P15 `measure-laws` | 102 | 37-90 | Empty/finite additivity, disjointization, both continuity directions, finite subtraction, null unions and probability-one intersections. |
| P15 `countable-atomic` | 129 | 92-145 | Supremum-based grouping includes empty blocks and infinite sums; atomic construction and converse uniqueness are supplied. |
| P15 `borel-generators` | 216 | 147-184 | Rational rectangles cover open sets through a countable basis; rational and real ray generators are connected. |
| P15 `measurability-criterion` | 249 | 186-221 | Both directions of the generator test; inverse-image collection, minimality and generator identity for sigma(X). |
| P15 `measurable-operations` | 291 | 223-274 | Composition, both vector directions, continuous operations and both simple-function descriptions. |
| P15 `measurable-limits` | 323 | 276-339 | Extended infimum/supremum and both tail limits; finite real convergence event; increasing dyadic approximations including infinity. |
| P15 `pushforward-laws` | 376 | 341-372 | Probability measure on values, transformed laws, atomic outcome sum and countable value-space masses. |
| P15 `measure-uniqueness` | 410 | 374-429 | Both stages of the pi-lambda argument; agreement collection uses probability normalization and finite subtraction. |
| P15 `cdf-laws` | 427 | 431-481 | Endpoint/right/left limits, intervals, atom jumps, countability and equality of laws via the proved uniqueness result. |
| P17 expected utility `lottery-reduction` | 52 | 4-38 | Normalization, flattening, joint branch/prize construction and zero-probability branch convention. |
| P17 expected utility `mixture-comparison` | 149 | 40-104 | Indifference and strict comparisons; positive, zero and unit weights; all strict segment endpoint cases. |
| P17 expected utility `lottery-calibration` | 164 | 106-152 | Closed calibration set and supremum argument; existence, uniqueness and endpoint indifferences. |
| P17 expected utility `finite-vnm` | 200 | 154-241 | Best/worst bounds, all-indifferent and singleton cases, finite replacement, representation, normalization and converse continuity. |
| P17 expected utility `vnm-affine-uniqueness` | 229 | 243-286 | All-lottery indifferences determine consequence scale; nonconstant, constant and singleton cases. |
| P17 expected utility `vnm-counterpreferences` | 353 | 288-340 | Both relations checked for completeness/transitivity and the stated retained/failed axioms; explicit witnesses. |
| P17 risk `finite-stochastic-dominance` | 62 | 4-62 | Finite telescoping, explicit continuous strictly increasing converse witness, singleton support and both threshold conventions. |
| P17 risk `finite-jensen` | 117 | 64-115 | Zero weights, strictness from a minimum positive-weight prize, both secant inequalities and open-interval derivative criterion. |
| P17 risk `risk-aversion-concavity` | 139 | 117-143 | Both concavity directions, strict consequence and risk-neutral affine characterization on the whole interval. |
| P17 risk `certainty-equivalent` | 165 | 145-174 | Expected value in the attained interval, intermediate value argument, uniqueness, premium sign and affine invariance. |
| P17 risk `comparative-risk` | 199 | 176-223 | Sure-prize acceptance, certainty equivalents, concave relative transformation and premium ordering, including ties. |
| P17 risk `arrow-pratt-comparison` | 247 | 225-273 | Positive derivatives justify inverse/quotients; global coefficient criterion and explicitly local indifference derivatives. |
| P17 risk `cara-characterization` | 296 | 275-417 | Global affine uniqueness, continuous additive/multiplicative equations, negative wealth, grid compatibility, differential route, converse and translated premiums. |

## Reader-facing assumptions, examples and boundaries

P15 declares nonnegative sums and extended arithmetic before its infinite arguments (body 70-100), and states the finite-measure premise where subtraction is used (102-124). Counting-measure tails demonstrate its necessity (183-201). The waiting model is constructed directly; its masses do not imply an unconstructed independent trial process (157-181). The geometric total, tail `2^(1-m)`, parity masses `1/3, 2/3`, and CDF jump `2^-m` recompute as stated. The parity sigma-algebra and reciprocal-value example distinguish information, attained values, accumulation points and positive mass.

The finite chapter's mass-function law becomes a measure on value sets through the new definition and its countable representation (body 357-390); the point-mass notation keeps its numerical role. A CDF determines an existing real law, while its converse existence theorem, Lebesgue construction, integration, density and general conditional expectation remain expressly pending (458-484). The text does not substitute uniqueness for existence or a point mass for a density. Extended limits use no infinity-minus-infinity expression (302-352).

P17 distinguishes preference independence from stochastic independence (expected-utility body 114-129), and its conditional branch construction does not assert independence of branch and final prize (52-79; annex 28-36). The infinite lottery simplex receives its own axioms and full representation proof. The later monetary interval receives a supplied global utility (risk body 16-42); the finite-prize theorem is not used to infer that utility's existence.

The finite-menu method supplies normalization, preference calibration, explicit sums, all maximizers, ties, empty-menu behavior and sensitivity checks (expected-utility body 253-273). Restricting the established representation to that finite menu justifies its finite-choice reference. The middle-prize example correctly distinguishes transforming consequence values from transforming completed lottery scores; its threshold is `2/5`. The four common-consequence lotteries and their quarter-factor score identity are exact. Both counterpreferences have complete mathematical exclusions (337-373).

Risk dominance retains `x <= t` versus `x >= t` and proves their equivalence using successive support points, avoiding an incorrect complement at atoms. Certainty equivalents and premiums are monetary quantities, preserved by positive affine utility changes (risk body 152-179). Comparative risk orders certainty equivalents in the correct direction and includes utilities that are not themselves risk averse (181-210). The log/square-root example gives mean 5, equivalents 3 and 4, and premiums 2 and 1. Positive derivative assumptions precede every Arrow-Pratt quotient. A coefficient comparison at one wealth level is explicitly insufficient for the global relation.

The CARA statement retains continuous, strictly increasing utility on all real wealth (risk body 296-319). The annex derives differentiability, supplies a common parameter across grids and separates the extra assumptions of its differential route. The exponential premium `log(cosh(rho*d))/rho`, its zero/positive cases and the value `log(5/4)/log(2)` follow directly. The final-wealth example gives the same sure 1500 and binary lottery on 1000/2000 in both descriptions. Mathematical stipulations, observed behavior, normative judgments, interpersonal utility, and empirical generalization remain distinct throughout.

## Primary source reading and attribution

The PDF skill guided bounded primary-document extraction and visual glyph checks. Source files were preserved. No manuscript PDF was built or rendered.

Durrett: `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`, SHA-256 `AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886`, 490 pages. Direct text reading covered physical page 1 and physical 9-11, 18-20, 23-25, 464-466 (printed 1-3, 10-12, 15-17, 456-458). The title confirms Version 5, 11 January 2019. The actual distribution, measurable-map and pi-lambda text supports the manuscript's scoped terminology; the source's CDF existence proof uses Lebesgue measure on `(0,1)` as stated. No complete reading of the book or its entire extension/integration treatment is claimed.

Rubinstein: `source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf`, SHA-256 `F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8`, 172 pages. Direct complete text reading covered physical pages 1-5, 108-118 and 122-133 (printed 94-104 and 108-119). Existing source images were visually inspected for printed pages 97, 98, 100, 114, 117 and 118. The title/revision and source notation `[z]`, `L(Z)`, mixture operation, Axioms I/C, consequence-versus-lottery utility and both wealth-invariance routes were checked. The supplied chapters do not claim completion of the source's separate betting model, Dutch-book discussion, every preference example, St. Petersburg argument or Rabin calibration.

Relevant canonical bibliography entries were read at `handbook/bib/handbook.bib:6608-6620` and `6663-6672`. They identify the Rubinstein 2015 author revision of the 2012 second edition and the Durrett January 2019 author version without replacing either with a different manifestation.

## Apparatus completion and remaining gates

All 34 new canonical rows at physical lines 1062-1095 of `handbook/registry/symbols.csv` were read. The registry has 1,094 data rows. Every corresponding table entry was read at candidate `symbols-tables.tex:1224-1237` and `1292-1311`, and every matching sorted index entry was read by its `entry:symbol-registry-01062` through `01095` target. These are candidate projections under `tmp/edition-2026-bounded-kamp4-probability-decision/probability-decision/`; the older parent-folder candidates are outside this apparatus judgment.

The initial row at `symbols.csv:1083` recorded `a,b` only as affine constants, omitting the lottery-endpoint roles at expected-utility body 158-169 and prize-label roles at 337-350. This was an apparatus finding, not a defect in the locally typed manuscript. The integrator corrected the row to record `a,b,c` with the three local roles and retained the finite-menu role. The corrected row, table entry at line 1299 and sorted index entry at line 45 were read directly after regeneration. That finding is resolved in the final snapshot; no open finding remains in the assigned scope.

The rows accurately distinguish the P15 measure and P17 monetary-mean uses of mu, a value-space law from a singleton mass, a CDF from either, consequence utility from a completed expected score, the two finite lottery domains, cumulative and weak upper tails, certainty equivalents and premiums, the local Arrow-Pratt coefficient and the continuous translation proof's factors. The notes preserve excluded denominators, endpoint conventions, the supplied global monetary utility and the CDF existence boundary. Candidate index links name the corresponding actual table entries. This is text-level navigation evidence; page layout and live PDF links still require production inspection.

| Final apparatus file, relative to repository root | SHA-256 |
| --- | --- |
| `handbook/registry/symbols.csv` | `D85A0E644274ADF054E8DFB449CA28BB8CF2A36A407AF371ADB44FEB7D78238B` |
| `tmp/edition-2026-bounded-kamp4-probability-decision/probability-decision/symbols-tables.tex` | `BE05737F6B1E3AE8DD679A8E5EC6FDA16E79F044D1222734C7109ACF27D370EF` |
| `tmp/edition-2026-bounded-kamp4-probability-decision/probability-decision/symbol-index.tex` | `08E962392B24787BDFBBAA3F9BD89376563E862C230CE472059179CEF659711B` |
| `handbook/bib/handbook.bib` | `BD462E1E3BC9B6E6C1AA40B30E4E7C23A6B4533FA196EDD43B881F8C7757FA59` |
| `handbook/parts/p15.tex` | `370F510D7000306EB7F401ADDC12D4C735C379DC343E2360C5D3651E3E9D9A3D` |
| `handbook/annex/p15.tex` | `07D712711CC537FD96F71E41BC6274173450898A1E9159057F6D57074A6CCB3C` |
| `handbook/parts/p17.tex` | `379B5F93BDE109583DA8A51E787361D639F99D1F905EA8C83CC7F2EE70D953FD` |
| `handbook/annex/p17.tex` | `C52D23E6FADEBB1BB07EBCD5CE215D6356841D3839EEDDECD2D321FF5F89B199` |

All six new manuscript hashes were rechecked after the complete treatment reading and remain the stated frozen values. The final registry and candidate hashes were independently rechecked after the local-role correction. The assigned text review has no unread remainder.

This review performed text reading, direct mathematical reasoning and bounded primary-source checks. It performed no manuscript build, static test suite, rendered manuscript inspection, rights admission, register closure or editorial acceptance. No manuscript or shared apparatus was edited. The owned report is the only output file.
