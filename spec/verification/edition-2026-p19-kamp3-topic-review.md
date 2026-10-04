# P19 evidence methods and Kamp III.2 Lemma 3: independent topic review

Date: 7 September 2026 Pacific time; review performed on 8 September UTC.
Reviewer: `/root/p19_kamp3_topic_review`.
Repository: `C:\Dev\the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`.
Assignment: fresh topic review of the three frozen target files; maximum 35 minutes, with a checkpoint supplied at approximately 01:57 UTC and the report completed at approximately 02:03 UTC.

## Verdict

**P19: FAIL pending the two located reporting repairs below.** The reported numbers and their principal statistical, causal, and normative interpretations pass. The proposed design does not yet align its opening question unambiguously with its primary contrast. The Study 2 paragraph also omits the adjustment set defining its reported conditional coefficient.

**Kamp III.2 Lemma 3 body and annex: PASS for the assigned topic scope.** The complete substitution proof, finite closure argument, dependency use, and mixed example are valid under the stated conventions. No repair is required in these two frozen files from this review.

These verdicts concern the inspected text and dependencies. They do not establish full P19-E1 coverage, complete Kamp III.2, production acceptance, formal admission, or user acceptance. The root owns routes, bibliography, and notation integration. The review does not adopt any other reviewer's findings or any author's claimed verification as evidence.

## Actual complete target reads and identities

All three target files were read in full as actual LaTeX. Their SHA-256 values matched the assignment before reading and at the final identity check.

| Target | Actual complete read | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p19/evidence-methods.tex` | 1-610 | `6ECBF1112C0F3E2465D457CC1677B70CBE556A7047F46A37111B699EA7B2F68B` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma3.tex` | 1-234 | `811AAA41E515F647CB6BC252A4AFEF59279B8338A0FBB43BE72DA3E572A29BA3` |
| `handbook/annex/p09/kamp-iii2-lemma3.tex` | 1-410, both entire annex items | `1193D892D2BA1A16EBDCBC10CA3FDF2AF161CFBE7084BE8C78AA6A9A84FCAE7A` |

The governing contract was read completely at `spec/EDITION-2026-CONTRACT.md:1-168`, SHA-256 `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3`.

Actual dependency reads:

| Dependency | Read extent | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p09/presentations/n-c-012.tex` | 1-161, covering the complete relevant host language, order classes, temporal semantics, D recursion, and current dependency inputs | `D234631589FA3B60FF1CD150713AA66CD0DBE61C8BA4F00D73462A5B3089966C` |
| `handbook/parts/p09/presentations/kamp-iii1-normal-form.tex` | 1-140, including the entire relevant unstarred At definition and its separate starred presentation | `0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma1.tex` | Complete, 1-202 | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| `handbook/annex/p09/kamp-iii2-lemma1.tex` | Complete, 1-212 | `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma2.tex` | Complete, 1-212 | `49C59D4BDF9169590457F73F3841B35E9620F6C4A54083044DAD625598823677` |
| `handbook/annex/p09/kamp-iii2-lemma2.tex` | Complete, 1-312 | `75BAE1D38B195849018E8F573741A7F04B8F0984C6804FECFF770D00602FA4F2` |
| `handbook/parts/p15/finite-probability.tex` | 1-83 and 127-178, including the complete finite probability laws and null-conditioning warning | `934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1` |
| `handbook/parts/p17/finite-preferences.tex` | 1-123, including the complete ordinal-representation definition | `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C` |

An initial overbroad host read returned truncated unrelated later material. It is not counted as a complete host read; the explicit bounded reread above establishes the relevant extent. The two research notes supplied file and page locators. Their author conclusions are not review authority. No other current reviewer report was read.

## Primary document checks actually performed

The PDF skill was read completely and used for source-page rendering and direct inspection. Existing source PDFs were preserved. The following listed pages were each read visually in full, including table headings, notes, and the surrounding text. PDF text extraction was supplementary. No complete reading of any entire empirical article is claimed in this topic review.

| Primary document | Capture and verified SHA-256 | Actual visual read |
| --- | --- | --- |
| Frederick 2005 | `source/references/frederick-2005-cognitive-reflection/frederick-2005-jep-19-4-25-42.pdf`; `D9CAB71F1EFD52878BD6A3740CDEACB00AE776C262C6722AF7CD1E4277711A86` | Physical 5-8 and 13; printed 28-31 and 36. Recruitment, extreme-score comparison, hypothetical task status, statistical-test convention, all of Table 2 and footnote 12. |
| Sinayev and Peters 2015 | `source/references/sinayev-peters-2015/sinayev-peters-2015-fpsyg-6-532.pdf`; `6D23EE182D1298C91ADB48C1861BB2D68778BD012188925C558D1D7A1E0A0B27` | Physical/printed 4-11, 13, and 16. Study 1 design and scoring, model descriptions and fit comparison, Tables 1-7, model-derived score explanation, Study 2 zero convention and imputation notes, adjustment paragraph, sample/date/construct discussion, and the complete robust-regression appendix. |
| Wasserstein and Lazar / ASA 2016 | `source/references/wasserstein-lazar-2016/wasserstein-lazar-2016-asa-p-values.pdf`; `B201C02C0F09B8CFEA287599E41E6A6A3194CCC62605D7E91534619BB2BB9A49` | Physical 4-5; printed 131-132. The actual embedded statement, its p-value definition, all six principles, other approaches, and conclusion. |
| Kamp 1968 | `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`; `C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA` | Physical 49, 68-69, 76, and 82; printed 40, 59-60, 67, and 73. Proper substitution, named-variable expressibility, complete R4, E closure, complete Lemma 3, and the following Com convention. |

The MiKTeX text extractor failed because it attempted to access its configuration area; an assumed bundled extractor path and an unavailable PyMuPDF import also failed. These failures are not counted as reading. Pypdf extraction succeeded, and actual rendered pages controlled the numerical and formula checks. No additional software was installed.

## Located findings and required repairs

### T1. The proposed design needs one explicit primary question/contrast pairing

**Priority P2; component FAIL.** Location: `handbook/parts/p19/evidence-methods.tex:525-529`, compared with `548-558`.

The opening question asks whether checking reduces inconsistencies "beyond a numerical aid." The natural additional-benefit interpretation is the checking effect when aid is supplied, with contrast `Ybar_11 - Ybar_01`. The displayed primary contrast instead gives equal weight to the checking effect without aid and the checking effect with aid. Those are different quantities whenever the factors interact. Reporting both constituent differences at line 558 is useful, but the text does not say which one answers the opening question or clarify that the opening question is meant to ask about the equal-weight average.

Concrete admissible counterexample: take condition means `(Ybar_00, Ybar_10, Ybar_01, Ybar_11) = (4, 0, 0, 2)`, all within the declared outcome range 0-4. Checking changes the mean by `-4` without aid and by `+2` with aid. The manuscript's contrast is `(-4 + 2) / 2 = -1`. It therefore indicates an average reduction while checking worsens the outcome when added to the aid. This is a counterexample to treating the average as an answer to the additional-benefit question; the displayed arithmetic itself is correct.

Required repair: state explicitly that the primary question concerns the checking effect averaged equally over aid and control, and retain the aid-present effect as a separate question; or retain the present additional-benefit question and designate `Ybar_11 - Ybar_01` as its primary contrast, with the equal-weight contrast identified separately. Explain that a negative value means fewer scored inconsistencies for the specified comparison. No empirical data or power calculation is needed for this repair.

### T2. Specify the adjustment variables for the selected Study 2 coefficient

**Priority P3; component FAIL for completeness of this evidence record.** Location: `handbook/parts/p19/evidence-methods.tex:480-487`.

The paragraph reports an "adjusted reflection coefficient" of `-0.01`, `p = 0.81`, but never names that model's adjustment set. The prior Study 1 table explicitly identifies its adjustment variables, while this paragraph is a different study and instrument. A conditional coefficient is not fully specified by naming the outcome and one predictor. This omission also falls short of the manuscript's own evidence-record instruction at lines 137-139.

Direct source evidence: Sinayev and Peters, printed p. 10, "Replications," gives this coefficient after controlling for demographic variables and including Calculation and numeracy. Its final model reports `F(7, 918)`, consistent with seven non-intercept predictors and `N = 926`. The source's demographic variable list is age, income, education, and gender; intelligence belongs to the subsequent composite models, not to this selected framing-inconsistency model.

Required repair: identify the reported coefficient as conditional on Calculation, numeracy, age, income, education, and gender. Retain the existing distinction between Table 7's outcome count and the named model. Do not imply adjustment for the later intelligence composite or transfer Study 1's latent-score units to Study 2.

No numerical correction is required for `-0.01`, `p = 0.81`, or the reported outcome count 926.

## P19 component assessment

| Component | Verdict | Evidence and reasoning |
| --- | --- | --- |
| Question, construct, operational measure, benchmark, population, frame, estimand | PASS | Body 28-167 distinguishes these roles and correctly separates random recruitment from random assignment. The P15 complement/monotonicity and P17 ordinal-representation interfaces support exactly the uses made here. |
| Response proportions and rounded percentages | PASS | Body 172-190 and 250-265. `0.37 - 0.22 = 0.15`; `409 + 297 = 706`. These are approximately 15 percentage points from rounded table proportions. The text does not infer integer successes, a 15 percent relative increase, or an all-3428 denominator. |
| Sampling variability, standard errors, confidence intervals, p-values | PASS | Body 192-225 correctly ties variability and uncertainty to a model/design, separates estimator and response dispersion, and rejects posterior-hypothesis and effect-magnitude readings of p-values. The statement's six principles support the selected interpretation. No new CI or unreported SE is claimed. |
| Frederick evidence and causal/normative limits | PASS | Body 230-299 and direct printed pp. 28-31. Extreme CRT groups are observed groups; the result is one hypothetical-payment association. The reported chi-square convention, sample sizes, and limiting Table 2 results are retained. The text does not adopt the source's wider population or normative interpretations merely because the authors suggest them. |
| Response decomposition and conditional denominator | PASS | Body 312-347. For positive `n_C+n_O`, cancellation gives `a-hat c-hat = n_C/m`. Rounded item percentages give `14/(14+8) = 0.636363...`, about 0.64. An item aggregate conditional proportion is correctly distinguished from an average of participant scores. |
| Recruitment, attention exclusions, and complete cases | PASS | Body 349-380 and source pp. 4-7. Initial 1413, four exclusions, and complete-case 1225 are distinct. Their difference is 188; the manuscript correctly avoids attributing all 188 to attention exclusions. Address-based recruitment is not used to assert unqualified representativeness of complete cases. |
| Threshold selection and mathematical benchmark | PASS | Body 370-387 records the threshold and its selection history. `65+45=110` meets the ten-point rule; `65+40=105` misses that code but still violates exact complementarity. The threshold does not amend probability theory. |
| Correlations, fitted coefficients, scales, significance markers | PASS | Body 389-417, source Tables 3 and 5. The `-0.20` marginal correlation is not treated as the adjusted slope. Table coefficients and SEs agree. Numeracy is standardized; `-0.13` is a change in the fitted mean inconsistency count per predictor SD. Reflection and Calculation are model-derived scores with different scales. No cross-scale comparison or causal effect follows from coefficient size. |
| Latent model, BIC comparison, and robustness | PASS | Body 419-447, source pp. 5-7 and 16. The 198 BIC difference and reported chi-square 217/2 df are retained as source model comparisons. Neither fit nor the observed response categories identifies a unique mental sequence. Robust coefficients agree with Table A1 and are described as sensitivity analysis of the same records. The manuscript does not claim that the reported fitted SEs account for all measurement/model uncertainty. |
| Study comparability and the selected Study 2 result | FAIL in one reporting field | Body 452-487 correctly distinguishes instruments, timing, composites, sample context, and predictor units. The correlation and coefficient values agree with source pp. 10-11. T2 requires the adjustment set to define the conditional result. |
| Zero conditional-score convention | PASS | Body 489-503 and source p. 9 including notes 2-3. About 24 percent have no eligible conditional responses. An assigned zero does not evaluate 0/0 and does not observe a conditional probability. The source's imputation sensitivity is attributed and does not establish the convention's universal validity. |
| Construct validity, reliability, familiarity, and evidence selection | PASS | Body 505-520 and 603-610 do not identify internal consistency with validity or source speculation with an exposure experiment. The purposive three-document corpus is not used as a systematic synthesis, consensus estimate, or a vote count. |
| Hypothetical factorial design and causal interpretation | FAIL on target alignment; causal limits PASS | Body 525-580 supplies the four conditions, person-level assignment, outcome range, missingness concerns, and assignment/compliance distinction. The equal-weight formula is algebraically correct and does not require equal realized cell sizes. T1 is the mismatch/ambiguity between the question and which contrast is primary. Stable intervention versions, interference, missingness, and process/generalization limitations are explicit. |
| Warranted conclusion and bounded scope | PASS | Body 582-610 limits conclusions to the observed relations, selected samples, and analysis. It neither ranks people's rationality nor derives a cognitive-ability intervention effect. |

The use of significance markings is not itself presented as a statistically significant difference between two coefficients, and the text does not equate a non-significant reflection coefficient with an exactly zero association. Those common errors were actively checked and are absent.

## Kamp component assessment and independent reasoning

| Component | Verdict | Located verification |
| --- | --- | --- |
| Proper substitution and enumeration | PASS | Body 14-59; annex 64-81. The replacement has exactly one free parameter; bound names avoid all variable names of the outer formula. The infinite variable stock makes eligible variants exist. The fixed enumeration chooses spelling, while a finite fresh-copy procedure produces an alphabetic variant. Source printed p. 40 agrees with the operation used. |
| Bound renaming and ordinary variable substitution | PASS | Annex 19-62. Variable dependence is proved for atoms, Booleans, and both quantifiers. The substitution identity is stated for arbitrary matrices, not just one-free-variable formulas. Fresh quantified names differ from both source and target variable names, so assignment updates commute in the quantifier step. |
| First-order interpretation substitution | PASS | Annex 83-141. The set A is evaluated in the original structure and is independent of the ambient assignment because the replacement's only free variable is its argument. Target atoms, other unary atoms, order atoms, all displayed Boolean cases, and both quantifiers are covered. An outer quantifier intentionally binds the inserted argument; it does not capture the replacement's fresh internal variables. |
| Exact free-variable preservation | PASS | Annex 134-141. Each target atom with argument y is replaced by a formula with exactly y free, preserving all Boolean unions and quantifier deletions. Semantic redundancy does not remove syntactic free variables. |
| Temporal substitution | PASS | Body 61-89; annex 143-174. Single-pass atom substitution, negation, conjunction, and both strict S/U witness/interval cases are explicit. Truth of the replacement is evaluated in the original structure. Empty intervals impose no extra witness. |
| D truth induction and compatibility | PASS | Host 100-131; annex 176-221. All primitive temporal cases are covered with fresh D variables. The truth equivalence uses arbitrary binary relations; linearity is imposed only for the expressibility application. The proof claims semantic equivalence rather than literal equality of independently selected bound names. |
| Expressibility theorem and Lin closure | PASS | Body 91-110; annex 223-241. Changing only one unary interpretation preserves membership in Lin. Thus the outer formula's universal expressibility assumption applies in the modified structure, closing the semantic chain. |
| Least finite E closure | PASS | Body 112-159; annex 268-282. Stage retention allows binary operands from different finite stages to meet at their maximum stage. Both closure and leastness are proved, and finite construction histories follow. No arbitrary external replacement, quantifier, semantic-equivalence, or infinitary closure is added. |
| Five generator classes and truth/false seeds | PASS | Annex 284-315 and 335-341; actual Lemma 1/2 recurrences. At is the unstarred class and includes the designated P0 tautology and contradictory literal conjunction. The temporal expressions contain the corresponding letter syntactically even when semantically constant. Basic and limiting recurrences cover all their declared stages and both orientations. |
| Every closure operation and exact letters | PASS | Annex 317-373. Boolean operations preserve or unite the two child letter sets. When a target occurs, the result's set is the old set minus the target, union the replacement's set; when absent, the replacement contributes no letters. The temporal recursion has exactly the corresponding behavior. |
| Finite construction | PASS | Body 161-189; annex 243-259 and 367-373. Each seed expression is finite; each substitution traverses the finite original tree and copies a finite replacement. A finite sequence remains finite. This proves construction from a history, not arbitrary-formula membership decidability. |
| Mixed basic-future/limiting-past example | PASS | Body 209-223; annex 375-402. The expanded first-order limit is at the selected future endpoint u. Internal C(r) survives the single substitution. Missing future witnesses and empty intervening B intervals agree with the temporal form. |
| Lin before later Com convention | PASS | Body 225-234; annex 404-408; source printed pp. 59 and 73. The proof uses no supremum, infimum, density, or endpointlessness assumption. The later change of default scope is placed after Lemma 3. |

Three direct edge checks reinforce the induction rather than replacing it:

1. With `phi = P_i(w) and exists y P_i(y)` and `psi(v) = P_i(v) and Q(v)`, substitution returns `(P_i(w) and Q(w)) and exists y (P_i(y) and Q(y))`, with fresh internal bound names if needed. Both original occurrences are replaced, the inserted P_i occurrences remain, and exactly w stays free. Repeating the substitution would be a separate operation.
2. For a replacement containing free v and a separately bound occurrence spelled v, the source's whole-variable renaming changes that binder and its occurrences together. Because the target argument occurs in the outer formula, no eligible replacement binder originally has that argument name. Separating the bound v first therefore produces an alphabetic variant of the same inserted binding pattern; it does not create a different free-variable meaning.
3. The mixed example is false at every point of a finite strict order: at a last point no future endpoint exists, and every later endpoint in a finite order has an immediate predecessor, making the inserted past limit false. On the real order with A and C everywhere, an appropriate future endpoint satisfies the limit (and B can be chosen everywhere). These outcomes agree with both the first-order display and the temporal expression. The example does not claim that every empty B interval makes the entire formula true.

No counterexample to either frozen Kamp theorem was found. The complete supplied proof, rather than these finite edge checks alone, establishes the PASS judgment.

## Handoff and boundaries

Repair T1 and T2 in P19, freeze the revised file, and rerun the affected topic and other independent scopes required by the contract. The unchanged Kamp hashes can retain this topic evidence. There is no request from this review to change the Kamp manuscript.

Only this assigned report was authored. Temporary source-page images were created for read-only inspection and removed afterward. No manuscript edit, new test, manuscript static check, build, manuscript render, commit, or formal-admission operation was performed. No subagent was spawned.

Historical memory supplied only the procedural distinction between bounded text evidence and final admission. All substantive judgments above derive from the current LaTeX, actual primary pages, direct arithmetic, and explicit mathematical reasoning in this review.
