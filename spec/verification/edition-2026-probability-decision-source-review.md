# Independent source-fidelity review: probability and decision treatments

Date: 8 September 2026 UTC / 7 September 2026 Pacific. Reviewer: `/root/probability_decision_source_review`, a fresh nonauthor context. Review began at 04:02 UTC and completed within the first 15-minute block. Root: `C:/Dev/the-methods-of-reason`; branch `phase4-codex`; HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The live tree contains extensive pre-existing changes.

## Verdict

| Treatment | Verdict | Basis |
| --- | --- | --- |
| P15 measurable probability and random variables | PASS | All ten stated results, their complete proofs, examples, source qualifications and scope boundaries checked against the specified Durrett author version. |
| P17 finite lotteries and expected utility | PASS | All six stated results and complete proofs retain the finite objective-lottery domain and vNM assumptions, including degenerate cases. |
| P17 monetary risk and risk aversion | PASS | All seven stated results and complete proofs preserve finite support, the common monetary interval, and the continuous wealth-invariance theorem with both source proof routes. |
| Final routes, versioned bibliography, relevant notation and candidate projections | PASS | Final bytes and the meanings of all 34 added records checked; the final row 1083 correction is included. |

No FAIL or UNRESOLVED source-fidelity finding remains within this assigned snapshot. This verdict is bounded to the three supplied treatments and their source/apparatus seams. It supplies no manuscript build, rendered-page, publication, rights, register-admission or whole-part completion decision.

## Actual reading and source identity

Read all six manuscript files below in full, including every definition, displayed formula, example, warning, proof boundary and all 23 reciprocal theorem/annex pairs. Read both complete author intakes, `spec/research/edition-2026-p15-u1-measurable-probability.md` and `spec/research/edition-2026-p17-d2-finite-expected-utility.md`, and the governing `spec/EDITION-2026-CONTRACT.md`. Author verification statements were checked against source and manuscript evidence; they were not independent acceptance evidence.

| Held primary source | Exact identity and complete relevant reading | SHA-256 |
| --- | --- | --- |
| `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf` | Rick Durrett, *Probability: Theory and Examples*, Version 5, 11 January 2019; 490 physical pages. Full text and full page-image inspection of printed 1-18 (physical 9-26) and Appendix A.1 printed 455-460 (physical 463-468), plus the title. This includes the extension/existence passages, all exercises in the assigned extent, and the opening of Section 1.4. | `AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886` |
| `source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf` | Ariel Rubinstein, *Lecture Notes in Microeconomic Theory: The Economic Agent*, second edition (2012), author revision 11 January 2015; 172 physical pages. Full text and full page-image inspection of printed 94-104 (physical 108-118) and 108-119 (physical 122-133). Full preliminary text physical 1-14, with visual verification of version/title/imprint physical 2-4. | `F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8` |

Thus all 47 assigned substantive source pages were inspected as complete pages, including figures and proof endings. Other book chapters are not claimed read. Durrett physical 2-3 and 5-6 were additionally read as preliminary/contents context; Sections 1.4-1.6 are located there as integration, properties of the integral and expected value, and their later proof bodies are not claimed reviewed here.

Canonical prerequisites were inspected in the actual LaTeX, with deliberately partial reads: finite P15 body 24-160 and 345-400; finite P15 annex 12-120 and 202-250; finite P17 body 21-145 and 194-241; finite P17 annex 212-254. These establish the used finite mass, law, conditional ratio, expectation, preference and finite-menu interfaces. All four P15/P17 wrappers were read completely. Bibliography inspection covered the two relevant complete entries; registry inspection covered physical rows 1062-1095; candidate inspection covered every corresponding table and index entry. Unrelated registry/bibliography content is not claimed semantically reviewed.

The PDF skill guided source extraction and complete-page inspection; the research skill guided primary-source tracing and this report. No subagent was used. No current topic/publication report was opened. A root message supplied one specific apparatus correction and final hashes; its corrected wording was independently checked against the manuscript. No manuscript file, source PDF, test, build, admission or manuscript render was changed or run. Only this report and temporary held-source reading images were written.

## Frozen manuscript bytes

Initial and final SHA-256 checks agree; final check at 04:13 UTC.

| Path under `handbook/` | Full read extent | SHA-256 |
| --- | --- | --- |
| `parts/p15/measurable-probability.tex` | 1-484 | `C249F33E0E0FC88084B05A7D44098DB87B3E4814083B34709D6DBE2B562340D9` |
| `annex/p15/measurable-probability.tex` | 1-481 | `FBB9E6C733A1F286F7E56FC31B7E76D4412D781E03711ED02D8D4B3AAEF8C8FC` |
| `parts/p17/finite-expected-utility.tex` | 1-390 | `6F83B6CB0300B241C8751E48747B577FB5869A02418C1C8C621E808515DD6EB5` |
| `annex/p17/finite-expected-utility.tex` | 1-340 | `C04B72A6DDC4B34147359A776597B99A16E4DE6D61A7C4789F5C413CF2FF11D3` |
| `parts/p17/risk-aversion.tex` | 1-355 | `F2B0A4CF575723E4CB6F8212077A59E64E276DAA43A5B25B57374D8E6657CD4A` |
| `annex/p17/risk-aversion.tex` | 1-417 | `1FAEAA08391C801C52CC0814189AE4B7FB4FB26DE788C0F7789D62D46917DC7A` |

## Result-to-source comparison

All page locators in this section are printed pages of the exact held sources. Result suffixes below correspond to body IDs beginning `thm:p15-` or `thm:p17-` and reciprocal annex IDs beginning `annex:p15.` or `annex:p17.`. Each listed proof was read completely, rather than inferred from the presence of an annex marker.

| Result suffix | Source foundation and checked reconstruction | Verdict |
| --- | --- | --- |
| P15 `generated-events` | Durrett Section 1.1, pp. 1, 3: complements, countable closure, arbitrary intersections of event collections and least generated sigma-algebra. | PASS |
| P15 `measure-laws` | Theorem 1.1.1, p. 2: disjointization and continuity; finite subtraction is explicit. Monotonicity also recovers the source's subadditivity bound for any subset of a covered union. | PASS |
| P15 `countable-atomic` | Example 1.1.2, p. 2 and Appendix A.1, pp. 455-456: supplied finite-subset-supremum regrouping proves the rearrangement premise used by the source and gives the full atomic converse. | PASS |
| P15 `borel-generators` | p. 3, Exercises 1.1.2-1.1.3 p. 9, Examples 1.3.2-1.3.3 p. 15: rational rectangles and closed-ray choices are justified by the supplied two-inclusion proofs. | PASS |
| P15 `measurability-criterion` | Theorem 1.3.1, equation (1.3.1), p. 15 and Exercise 1.3.1 p. 17: inverse-image closure, minimality and inverse images of generators supplied. | PASS |
| P15 `measurable-operations` | Theorems 1.3.4-1.3.6 pp. 15-16; Exercises 1.3.4, 1.3.7 pp. 17-18: composition, both vector directions, continuity, finite operations and simple-function equivalence supplied. | PASS |
| P15 `measurable-limits` | Theorem 1.3.7 pp. 16-17 and Exercise 1.3.7 pp. 17-18: explicitly extended codomain, measurable tails/limits, specified-real-target convergence event and increasing dyadic approximants, including infinity. | PASS |
| P15 `pushforward-laws` | Section 1.2 opening p. 10 and Theorem 1.3.4 p. 15: direct inverse-image proof, composition and countable value-space mass representation preserve the measurable-space hypotheses. | PASS |
| P15 `measure-uniqueness` | Theorems A.1.4 and A.1.5, pp. 456-458: full two-stage pi-lambda argument; probability specialization uses finite total masses. The proof supplies no extension existence. | PASS |
| P15 `cdf-laws` | Theorem 1.2.1 pp. 10-11; equality in distribution pp. 11-12; Exercise 1.2.3 p. 14: endpoints, right/left limits, intervals, jumps and countability supplied. CDF uniqueness is proved from the earlier pi-lambda result. | PASS |
| P17 `lottery-reduction` | Rubinstein pp. 94, 96-97: coordinate mixture identity and nested finite sums; an explicit joint law supplies the conditional formulation and null-branch case. | PASS |
| P17 `mixture-comparison` | Axiom I, property I* and strict binary lemma, pp. 97-98: both comparison directions follow from independence; zero/unit weights and arbitrary endpoint lotteries are proved. | PASS |
| P17 `lottery-calibration` | Axiom C and C*, pp. 98-100: relative-neighborhood continuity yields a closed nonempty calibration set; supremum and endpoint arguments fully supply the source's interpolation step. | PASS |
| P17 `finite-vnm` | vNM theorem, pp. 99-100: finite extrema, all-indifferent case, replacement by calibrated binaries and converse supplied. The proof does not rely on the preceding source mention of Debreu's theorem. | PASS |
| P17 `vnm-affine-uniqueness` | p. 100: positive affine consequence scale, both directions, ties and constant-utility case; completed lottery-score transformations are distinguished. | PASS |
| P17 `vnm-counterpreferences` | Largest probability pp. 95, 99 and lexicographic preference pp. 96, 99: complete explicit witnesses and proofs of retained axioms supplied. | PASS |
| P17 `finite-stochastic-dominance` | pp. 108-110: finite supports, exact source telescoping identity, both atom conventions and a constructed continuous strictly increasing converse witness. | PASS |
| P17 `finite-jensen` | pp. 110-111: full finite induction and secant arguments; strict case and derivative converse are explicitly proved supporting developments. Included endpoints are not assigned unwarranted continuity. | PASS |
| P17 `risk-aversion-concavity` | pp. 110-111: weak sure-mean comparison in both directions; strict Jensen and the full affine risk-neutral characterization are proved additions. | PASS |
| P17 `certainty-equivalent` | p. 111: finite-support extrema and interval continuity prove existence; strict increase gives uniqueness, inversion and premium sign. | PASS |
| P17 `comparative-risk` | pp. 111-114: lottery acceptance implication, certainty-equivalent order and concavity of the relative transformation have all directions supplied, with ties retained. | PASS |
| P17 `arrow-pratt-comparison` | pp. 114-115: coefficient order and exact binary-curve derivatives; additional C2 and positive-derivative hypotheses make every inverse, logarithm and quotient legitimate. | PASS |
| P17 `cara-characterization` | pp. 115-118: continuous monotone risk aversion and wealth invariance on the whole real line; continuous functional equation, source grid recurrence and separate differential route all supplied. | PASS |

## Concrete source-fidelity findings

P15's extended measure codomain is supported by the actual source situation: Durrett p. 1 prints a real codomain, while pp. 2-6 and Appendix A.1 use potentially infinite measures. The handbook declares `[0,infinity]` before use (body 70-100), proves the finite-subset definition and regrouping (annex 92-145), and keeps the finite condition in continuity from above (body 116-118; annex 71-80). The counting-measure counterexample directly validates that condition. No inaccurate quotation or unproved rearrangement is substituted.

Durrett p. 16 displays a difference of upper and lower limits; p. 17 then extends the variable codomain and permits measurable subdomains. The handbook declares its own total-function and extended-value conventions first (body 224-247, 302-321). Its displayed event is exactly convergence of real `X_n` to a specified real `X`, using finite differences (body 328-345; annex 309-337). This is valid at every outcome, and the increasing approximation handles `Z=infinity` by `s_n=n`. The displayed event is not falsely presented as the source's verbatim existential-limit formula.

The P15 countable waiting model has total mass one, tail `2^(1-m)`, even/odd probabilities `1/3` and `2/3`, and jump `2^-m`; its reciprocal observation puts zero mass at the unattained limit point zero. The text constructs the model by its masses and explicitly avoids assuming an underlying infinite sequence of independent trials. Its CDF and law terminology preserves the distinction between a measure, singleton mass and density.

P15 body 458-484 accurately leaves the converse CDF existence assertion, Lebesgue/extension construction and integration owed. The locator Theorem 1.2.2 p. 11 is exact; its source proof does use Lebesgue measure on `(0,1)`. Theorem 1.1.4, Theorem 1.1.9 and Appendix A.1 are the relevant existence dependencies. The later integration citation is a continuation locator, not a claimed completed proof. No continuous probability law or density existence is smuggled into the ten results.

Rubinstein p. 94 takes lottery probabilities as objective input; pp. 102-103 introduce a separate subjective betting domain with elicited probabilities. The handbook keeps probabilities supplied (expected-utility body 14-20, 25-50) and explicitly leaves subjective probabilities and the separate betting model outside this theorem (375-390). Source p. 97 assumes independent random factors for the two randomization stages; that does not imply independence of branch and final prize. The handbook's conditional joint-law calculation (annex 28-36) preserves the mixture law and correctly distinguishes these two notions (body 73-79, 114-129).

The full finite vNM proof retains completeness, transitivity, source Axiom I and source neighborhood Axiom C. It supplies the source's omitted interpolation/endpoint work and the constant case without changing the represented domain. The four common-consequence lotteries are exactly the source's p. 101 amounts and probabilities: `(3000,1/4)`, `(4000,1/5)`, sure `3000`, and `(4000,4/5)`, with the remaining masses at zero. The displayed difference factor `1/4` is correct. The source's response percentages are not imported as population evidence. The additional calibrated-choice and counterpreference calculations are exact stipulated models.

The monetary chapter states finite support and a supplied utility on a common interval (body 16-44), making its sure means and inverse-utility ranges valid. This retains the source's p. 108 distinction from a finite prize set. The dominance proof correctly uses adjacent support thresholds rather than `G(t)=1-F(t)` at an atom. The certainty equivalents `3` and `4` for the equally weighted prizes `1,9`, premiums `2` and `1`, relative transform `2 log t`, and coefficients `1/x` and `1/(2x)` are exact.

The continuous CARA theorem keeps the source's continuity context, strict monetary monotonicity, risk aversion and wealth invariance. Its global affine-uniqueness bridge (risk annex 277-291), positive continuous translation factor and rational-to-real extension (293-340) justify one exponential parameter across all grids, including negative shifts. The source grid route remains at 342-372, and its differential route at 374-393 explicitly adds C2 and `u'>0`. Those extra assumptions do not replace the continuous theorem. The final exponential premium and `log(5/4)/log 2` example are correct. Source pp. 115-116's final-wealth example is numerically unchanged; St. Petersburg, Rabin calibration, empirical frequencies and broader risk theories remain explicitly outside the supplied results.

## Final integration binding

The two bibliography entries preserve the exact manifestations: `Rubinstein2015LectureNotes` at `handbook/bib/handbook.bib:6608` records second edition 2012 and the 11 January 2015 author revision; `DurrettPTEAuthor2019` at 6663 records the 11 January 2019 Version 5 author PDF and distinguishes the Cambridge manifestation. Titles, Rubinstein's subtitle/ISBN/imprint, and dates agree with the held source pages. All manuscript citation locators and internal proof/prerequisite references were checked at their actual targets.

All 34 new notation records, physical rows 1062-1095, retain the reviewed source meanings. Final row 1083 now records `a,b` as lottery endpoints, `a,b,c` as prize labels, real affine constants with positive multiplier, and the finite menu as distinct local roles. This correction agrees with expected-utility body 158-175, 230-241, 253-273 and 337-350. Every corresponding candidate table and index entry was read; its final hashes are bound below. The four wrappers insert each complete body and annex after its finite prerequisite in matching order.

| Final apparatus/dependency path | SHA-256 |
| --- | --- |
| `handbook/registry/symbols.csv` (1,094 records) | `D85A0E644274ADF054E8DFB449CA28BB8CF2A36A407AF371ADB44FEB7D78238B` |
| `handbook/bib/handbook.bib` | `BD462E1E3BC9B6E6C1AA40B30E4E7C23A6B4533FA196EDD43B881F8C7757FA59` |
| `handbook/parts/p15.tex` | `370F510D7000306EB7F401ADDC12D4C735C379DC343E2360C5D3651E3E9D9A3D` |
| `handbook/annex/p15.tex` | `07D712711CC537FD96F71E41BC6274173450898A1E9159057F6D57074A6CCB3C` |
| `handbook/parts/p17.tex` | `379B5F93BDE109583DA8A51E787361D639F99D1F905EA8C83CC7F2EE70D953FD` |
| `handbook/annex/p17.tex` | `C52D23E6FADEBB1BB07EBCD5CE215D6356841D3839EEDDECD2D321FF5F89B199` |
| `tmp/edition-2026-bounded-kamp4-probability-decision/probability-decision/symbols-tables.tex` | `BE05737F6B1E3AE8DD679A8E5EC6FDA16E79F044D1222734C7109ACF27D370EF` |
| `tmp/edition-2026-bounded-kamp4-probability-decision/probability-decision/symbol-index.tex` | `08E962392B24787BDFBBAA3F9BD89376563E862C230CE472059179CEF659711B` |
| `handbook/parts/p15/finite-probability.tex` | `934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1` |
| `handbook/annex/p15/finite-probability.tex` | `7CE651CE52FE8BFA66E5BEC221BDF48EE6318538E6A99B8E987E18C90D6B67F3` |
| `handbook/parts/p17/finite-preferences.tex` | `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C` |
| `handbook/annex/p17/finite-preferences.tex` | `B141A371731E7A0A3BEFF1C88C839F98720BE4F894A2D475CAF098A61159202C` |

The next authorized gates can use this source-fidelity verdict only for these bytes. P15-U1, N-x-008, P17-D2 and the complete parts retain their broader obligations, including the explicitly deferred source and proof treatments.
