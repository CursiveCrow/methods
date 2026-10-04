# Independent publication-text review: P19 evidence methods and Kamp III.2 Lemma 3

Date: 7 September 2026 Pacific time; review on 8 September UTC.
Reviewer: `/root/p19_kamp3_publication_review`.
Repository: `C:\Dev\the-methods-of-reason`.
Owned output: this report only.

## Verdict and scope

**P19 selected publication-text component: FAIL pending PT-P19-01.** The chapter's empirical, normative and causal qualifications are sound at the level reviewed. Its selected Study 1 record nevertheless uses two model-derived predictor scores without defining their operational construction or scale, while expressly calling the record complete. This is a measure-definition omission, not a demand for an unassigned statistical theory chapter.

**Kamp III.2 Lemma 3 body and annex: PASS at the bounded publication-text scope.** The two promised proof items, their cases, the variable and predicate conditions, the finite construction, and the worked example are supplied coherently. No required repair was found in these two target files.

**Canonical integration: UNRESOLVED pending the lead's final snapshot.** At the lead's explicit direction, this blind R1 content report is returned before the final shared snapshot. The final routes, bibliography and projected notation require the next scoped review. An interim missing route or unmerged intake is not recorded as a manuscript defect while the lead owns that integration.

This is a fresh independent reading of the assigned actual LaTeX. No other current reviewer report or conclusion was consulted. The two named author/intake notes were used as locator and scope leads only. No manuscript or shared file was edited, no subagent was used, and no tests, generators, manuscript builds, renders or admission operations were run. This report does not establish primary-source fidelity, complete P19/E1, complete Kamp III.2, production quality, formal admission or final acceptance.

## Exact target reading and identities

All three files were read completely, including all displays, paragraph qualifications, examples and proof cases. The initial line counts and hashes match the assigned freeze.

| Target under `handbook/` | Actual reading | SHA256 |
| --- | --- | --- |
| `parts/p19/evidence-methods.tex` | 1–610, complete | `6ECBF1112C0F3E2465D457CC1677B70CBE556A7047F46A37111B699EA7B2F68B` |
| `parts/p09/presentations/kamp-iii2-lemma3.tex` | 1–234, complete | `811AAA41E515F647CB6BC252A4AFEF59279B8338A0FBB43BE72DA3E572A29BA3` |
| `annex/p09/kamp-iii2-lemma3.tex` | 1–410, complete; both annex items | `1193D892D2BA1A16EBDCBC10CA3FDF2AF161CFBE7084BE8C78AA6A9A84FCAE7A` |

Truncated combined shell output was not treated as complete reading: the affected P19 spans were reread with explicit line numbers. All three target line counts and hashes were rechecked at report submission and still match the assigned freeze.

## Required repair

### PT-P19-01 — Define the measures actually used in the selected complete evidence record

**Finding: FAIL.** Location: `handbook/parts/p19/evidence-methods.tex:349` and `:361–368`, with the resulting table at `:389–417`.

The chapter's method explicitly requires the investigator to define each score and the transformations that determine its meaning (131–139). The two proportion scores in 312–327 meet that requirement. The selected Study 1 coefficients, however, are expressly stated not to use those scores: 363–368 names a fitted response model and two person-level components, but gives neither that model's response probabilities nor the construction and scale of the two fitted predictor scores. The reader is then given unstandardized coefficients for those scores. The warning at 413–417 correctly prevents comparing unlike scales, but it does not tell the reader what either scale is or what a unit change denotes. A page-range citation identifies where to investigate this omission; it does not itself define the actual measures in the claimed complete record.

This matters to the chapter's own measurement lesson. The reader can reconstruct the raw scores and the complementary-pair outcome, yet cannot reconstruct what the model-derived reflection and calculation predictors represent or determine how they differ operationally from the preceding raw scores. The explicitly stated distinction between the two kinds of score must be accompanied by the missing definitions.

**Required repair:** add a concise source-checked specification of the Study 1 response model, identify the person scores used in the regressions and their scale/normalization, and state any score-estimation details the primary source leaves unavailable. Tie the displayed coefficients to those declared measures. This need not derive the fitting algorithm, its standard errors or the broader theory of latent measurement. Preserve the existing cautions about construct interpretation, observational adjustment and separate normative premises. Changing only the paragraph heading would not supply the required complete evidence record.

**Recheck condition:** an independent reader can identify the actual regression predictors and their units from the record, distinguish them from `\widehat a,\widehat c`, and see which unresolved estimation details are explicitly unavailable rather than silently supplied.

## Component results

| Component | Result | Located evidence and assessment |
| --- | --- | --- |
| P19 corpus and editorial/source standing | PASS | 11–26 states the two empirical articles, ASA statement, selection reason, cutoff and limits; the record, procedure and proposed experiment are explicitly handbook syntheses. No fabricated participant data or completed follow-up is asserted. |
| P19 basic terminology and descriptive notation | PASS | 31–110 defines question, task, construct, measure, benchmark, population, frame, sample, estimand and estimate before their substantive use. 172–206 defines observed proportions, differences and uncertainty vocabulary. The group labels do not imply assignment. |
| P19 model-derived Study 1 predictors | FAIL | PT-P19-01: 361–368 distinguishes the actual predictors from the defined proportion scores without defining the actual predictors. |
| P19 population, design and estimate denominators | PASS | 239–265 keeps 3,428, the two item-specific groups and their total 706 distinct. 350–359 distinguishes initial participants, four attention exclusions and 1,225 complete cases. 389–391 explicitly leaves the correlation-cell sample size unavailable. |
| P19 arithmetic and conditional-score domains | PASS | 172–190 requires positive denominators. 254–265 uses rounded percentages and an approximate 15-point difference. 313–326 gives the product identity only with a positive conditional denominator; 335–347 identifies the aggregate-item calculation `14/(14+8)` and does not substitute it for a participant mean. 489–503 preserves the undefined `0/0` case and the source's separate imputation convention. |
| P19 estimate/uncertainty interpretation | PASS | 192–225 distinguishes standard errors, intervals and p-values from effect size, hypothesis probabilities and all-purpose uncertainty. 393–417 gives source standard errors and the numeracy coefficient's count units. Nondetection is not turned into proof of absence. The score-definition omission remains separately open. |
| P19 conflicting/limiting evidence and comparison | PASS | 276–299 preserves weaker intertemporal cases and interpretation limits; 329–347 supplies a concrete other-error limitation; 430–436 calls robustness a same-data sensitivity analysis; 452–520 distinguishes instrument/component mixtures, score construction, data dates, missing conditional scores and familiarity arguments. No numerical pooling of differently scaled slopes is proposed. |
| P19 normative and causal boundaries | PASS | 65–93 and 293–299 require benchmark assumptions; 267–274 and 438–447 limit observational claims. 564–579 gives assumptions and limitations for assignment comparisons and explicitly distinguishes compliance and putative reflection mechanisms. No unproved universal guarantee is smuggled into empirical exposition. |
| P19 hypothetical design | PASS at the declared illustrative scope | 525–580 identifies an unperformed design, four assignment conditions, participant outcome/unit, a descriptive equal-weight contrast and the requirement that all four means exist. It requires a stopping rule, effect/variance/missingness assumptions and uncertainty analysis without inventing a power result. Its general methodological guidance is not represented as a new proved causal-identification theorem or a completed executable protocol. |
| P19 proof/annex obligation | PASS | There is no new theorem status or promised annex proof. The shown arithmetic is elementary and conditional; statistical derivations and wider methods are expressly deferred at 220–225 and 603–610. An annex is not required merely because the chapter uses numbers. |
| Kamp proper substitution: type, scope and capture | PASS | Body 14–59 types the equality-free language, unary target and exactly one free replacement parameter. Source-selected spelling and direct fresh-copy construction are distinguished. Original atoms are visited once; shared and self-occurring predicates, absent targets, intended outer binding and a different parameter name are covered. |
| Kamp temporal substitution | PASS | Body 61–89 defines all primitive constructors, preserves strict witness/open-interval operand order, expands derived operations, and separates a finite ordered sequence from simultaneous or recursive substitution. |
| Kamp substitution theorem and proof coverage | PASS | Body 91–110 and annex 6–261 agree. The proof covers free-variable dependence, both quantifiers, bound renaming, ordinary free-variable replacement, existence/agreement of fresh copies, all first-order atoms/Booleans/quantifiers, exact free-variable preservation, temporal atoms/Booleans/S/U, full D truth verification, D compatibility and the expressibility chain. |
| Kamp changed interpretations and hypotheses | PASS | Annex 83–141 evaluates the replacement in the original structure and proves its truth set independent of the ambient assignment. Annex 223–241 applies expressibility in the modified structure, which retains the original linear order. There is no fixed-point interpretation or hidden extra free parameter. |
| Kamp finite E closure and all seeds | PASS | Body 112–159 and annex 267–315 cover the five source seed classes, retained stages, finite least closure, exact free variable and input predicate letters. Source unstarred At, including its P0 tautology/contradiction, is distinguished from the earlier starred/order-constant presentation. |
| Kamp procedure and every closure case | PASS | Body 161–207 and annex 317–373 cover negation, conjunction, disjunction, retention, empty Boolean abbreviations, proper substitution and finite output. The input includes a construction history; no arbitrary-formula membership decision procedure is claimed. |
| Kamp example and boundary behavior | PASS | Body 209–223 and annex 375–402 place the inserted past limit at the selected future endpoint, retain its internal C occurrence, and check no future witness and empty intervals. The prior limit definitions justify endpoint/adjacency behavior. |
| Kamp text/annex reciprocity | PASS | Body 91 points to `annex:p9.kamp.proper.substitution`, whose annex backref at 6 is exactly `thm:p09-kamp-proper-substitution`; body 192 and annex 263 likewise pair `thm:p09-kamp-iii2-lemma3` with `annex:p9.kamp.iii2.lemma3`. Both items contain full proofs. |
| Kamp source/handbook distinction and continuing obligation | PASS | Body 35–42 separates formula enumeration from class E and source spelling from fresh implementation. Body 225–234 and annex 404–408 locate the subsequent Com convention and leave Lemma 4/full III.2 separate. The result applies to Lin and does not assert all one-variable formulas belong to E. |
| New canonical routes, bibliography and notation | UNRESOLVED | Awaiting final lead snapshot; see integration section. |

## Actual prerequisite checks

The P15 reference at P19 75 points to finite probability identities whose clauses at `finite-probability.tex:57–75` include exactly the subset inequality and complement law used. Their probability-space assumptions are supplied at 24–49. P19 explicitly requires the same outcome space, information and intended complementary or nested events. The null-conditioning warning at P15 160–169 states the undefined ratio and nonuniqueness from the multiplication equation; it supports the positive-denominator comparison without claiming that a missing empirical count proves a population conditional probability is zero.

P19's P17 reference points to the actual ordinal-representation definition at `finite-preferences.tex:95–119`. Its equivalence preserves the supplied comparison relation and ties. P17's opening 12–16 and the existence statement at 121–141 retain the completeness/transitivity assumptions and the distinction from empirical preference validation. P19 does not promote that representation to cardinal money utility or a universal choice criterion.

Kamp's active host at `n-c-012.tex:16–131` declares nonempty strict linear orders, the equality-free first-order language, temporal grammar, strict S/U operand order and capture-avoiding D clauses before Lemma 3's intended insertion point. The III.1 components at `kamp-iii1-normal-form.tex:66–128` confirm the exact unstarred At class. Lemma 1's whole body (1–202) supplies named-variable expressibility, basic-class guards, exact stages, words and the `L_n/R_0` constructions. Lemma 2's whole body (1–212) supplies witness-point limits, zero-stage singleton seeds and `Lambda` recurrences. Their actual hypotheses match the uses in Lemma 3. This prerequisite-interface check is not a fresh complete reproof of either earlier annex.

The shared style was read at 448–510 and 1801–1840. Its nine editorial entry kinds now set typed `crefalias` values before the common counter step (496–504), with matching singular/plural reference names (1809–1826). The new files use these editorial interfaces. This review does not confuse a source-only command spelling with an editorial concept, nor infer rendered reference correctness from source inspection alone.

## Instruction, dependency and lead identities

The extents below describe actual reading, not a claim to have independently reviewed every line in every dependency.

| File | Actual reading used here | SHA256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | Complete 1–168 | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `handbook/CONVENTIONS.md` | Complete 1–251 | `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242` |
| `spec/EDITION-2026-WORK-PACKAGES.md` | Located NOW-07/NOW-10, common scope and P19 E1 rows with adjacent context; not complete | `F49DE88FC33093390FD0CC377E7647019F74FD0529F7DCC07B503E559545160E` |
| `handbook/parts/p01/formal-work-conventions.tex` | Complete 1–292 | `0543B9EE6059B3DFE37A0F445648E971B4C0A01726632ED7728C69423C54C878` |
| `handbook/parts/p15/finite-probability.tex` | 1–176 | `934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1` |
| `handbook/parts/p17/finite-preferences.tex` | 1–147 | `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C` |
| `handbook/parts/p09/presentations/n-c-012.tex` | 1–180 before final route integration | `D234631589FA3B60FF1CD150713AA66CD0DBE61C8BA4F00D73462A5B3089966C` |
| `handbook/parts/p09/presentations/kamp-iii1-normal-form.tex` | 1–145 | `0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma1.tex` | Complete 1–202 | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma2.tex` | Complete 1–212 | `49C59D4BDF9169590457F73F3841B35E9620F6C4A54083044DAD625598823677` |
| `handbook/handbook.sty` | 448–510 and 1801–1840, with targeted interface search | `2411A09B48D5C0A4ADBF583B350D5606CBD1A60C504681F67D52EEC444406C44` |
| `spec/research/edition-2026-p19-e1-evidence-methods.md` | Locator/scope, source-to-body and intake passages; not independent source evidence | `328CA72661CE4FE08666D92A1CD3A7EA2D1BAFC4A7E16774AA95931BEB38D280` |
| `spec/research/edition-2026-c7-kamp-iii2-lemma3.md` | Author/intake lead, including source-convention and complete-proof map passages; not independent source evidence | `9D793E042CB154B6A2AA60292B2D7C0DC4C8DDF5A362057035CF591E58C18D6F` |

## Canonical integration and submission checkpoint

The final canonical snapshot was requested from the lead after all three target files had been read. A checkpoint reported the complete target/dependency reading, saved findings and pending shared integration. The lead then expressly directed this review block to finalize its blind R1 content report, retaining integration as pending, so that a bounded content repair can precede R2 against the final integrated snapshot.

The report is now submitted blind. No other review's findings or verdict details were read before submission. The three target identities were revalidated unchanged. The shared routes, bibliography and projected notation have not received a final-snapshot verdict in this report. PT-P19-01 remains required; Kamp Lemma 3's bounded publication-text component passes. The next review must inspect the actual repair and final canonical notation/routes rather than treating this content-only return as their acceptance.
