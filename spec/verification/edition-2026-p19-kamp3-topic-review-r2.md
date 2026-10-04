# P19 and Kamp Lemma 3: focused R2 topic recheck

Date: 7 September 2026 Pacific time; recheck began 8 September at 02:32:22 UTC.
Reviewer: `/root/p19_kamp3_topic_review`.
Repository: `C:\Dev\the-methods-of-reason`.
Scope: the two R1 topic findings, the new Study 1 response-model definition and its statistical interpretation, and preservation of the Kamp mathematical verdict through the single formatting change. Maximum assigned duration: 12 minutes.

## Verdict

**PASS for the focused R2 topic scope.** Both R1 P19 findings are resolved. The new Study 1 model description supplies valid conditional response probabilities, correct log-odds units, and the source-described modal-score interpretation while stating the unavailable estimation details. No new topic defect was found.

The P19 topic verdict is now **PASS for this bounded evidence-method treatment**, combining the unchanged valid R1 evidence with the verified changes below. The prior complete Kamp body/annex mathematical verdict remains **PASS**. These are topic-text judgments; they do not establish full P19-E1 coverage, complete Kamp III.2, numerical reproduction of participant scores, production acceptance, formal admission, or user acceptance.

## Current snapshots and exact change checks

| Artifact | Current extent and SHA-256 | Recheck |
| --- | --- | --- |
| `handbook/parts/p19/evidence-methods.tex` | 704 lines; `F9884A1A9267F1A8940C3C574874C6702B257B359BEC21AD137F642104B9CD12` | Read the revised affected text and surrounding context at 301-704; reread the complete new definition at 368-442 separately after the initial combined output truncated part of it. Independently reversed the new definition and changed surrounding groups in memory. The resulting 610-line UTF-8/LF content has exactly the original R1 SHA-256 `6ECBF1112C0F3E2465D457CC1677B70CBE556A7047F46A37111B699EA7B2F68B`. Thus the remaining content is identical to the complete text read in R1. |
| `handbook/parts/p09/presentations/kamp-iii2-lemma3.tex` | 234 lines; `811AAA41E515F647CB6BC252A4AFEF59279B8338A0FBB43BE72DA3E572A29BA3` | Exact same complete body as R1. |
| `handbook/annex/p09/kamp-iii2-lemma3.tex` | 410 lines; `91E5182F2545CDA968E8B13FAB320988CEA3B24FC1E6572271A4EC4B66E53C0E` | Read the changed line 268 and context 263-274. Replacing exactly one `\textbf{The staged grammar is exactly the stated least closure.}\enspace` with the former `\paragraph{The staged grammar is exactly the stated least closure.}` in memory yields exactly the R1 SHA-256 `1193D892D2BA1A16EBDCBC10CA3FDF2AF161CFBE7084BE8C78AA6A9A84FCAE7A`. No mathematical text changed. |

Both identity reversals were read-only diagnostics. No old manuscript copy or diagnostic script was written to disk. The P19 inverse was independently reconstructed from the actual R1 text, rather than accepting the repair author's asserted inverse result.

The actual At dependency and both complete Lemma 1/2 body-annex dependencies retain their R1 hashes: respectively `0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31`, `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6`, `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1`, `49C59D4BDF9169590457F73F3841B35E9620F6C4A54083044DAD625598823677`, and `75BAE1D38B195849018E8F573741A7F04B8F0984C6804FECFF770D00602FA4F2`. These direct checks preserve the dependency evidence used by the complete R1 mathematical review.

## Disposition of the two R1 findings

### T1: primary question and contrast — PASS, resolved

At P19 604-610 the primary question now explicitly concerns adding checking when the numerical aid is already supplied. Lines 629-636 define the corresponding descriptive contrast as `Delta_aid = Ybar_11 - Ybar_01`, requiring its two means. Lines 637-643 retain the equally weighted average across aid conditions as a separate secondary contrast. The two estimands are no longer interchanged.

The sign interpretation and counterexample at 644-650 are correct. With `(Ybar_00, Ybar_10, Ybar_01, Ybar_11) = (4, 0, 0, 2)`, the primary contrast is `+2`, while the secondary contrast is `(-4 + 2)/2 = -1`. All four hypothetical means fall inside the declared 0-4 range. The text explicitly states why an average reduction can coexist with worsening when checking is added to aid. It labels the values as hypothetical, and the assignment, compliance, missingness, interference, process, and transfer limitations remain at 651-673.

No additional contrast, interaction test, power calculation, or participant data is required to resolve T1. The body does not claim these descriptive means alone establish a causal process.

### T2: Study 2 adjustment set — PASS, resolved

At P19 556-566, the `-0.01`, `p = 0.81` reflection coefficient is now explicitly conditional on Calculation, numeracy, age, income, education, and gender. The passage distinguishes the absent intelligence composite from its use in later composite-outcome models. This matches the source's selected framing-inconsistency model on printed p. 10 and its separation from the subsequent stepwise composite analyses.

The values `r = -0.12`, `b = -0.01`, `p = 0.81`, and Table 7 outcome count 926 remain unchanged. The scale warning still prevents numerical pooling with Study 1's model-derived score slope. No remaining T2 repair is required.

## New Study 1 model definition: component checks

| Component | Verdict | Mathematical/statistical check |
| --- | --- | --- |
| Three-category response coding, 369-377 | PASS | The first step records avoiding the designated error. Correct and other non-designated responses proceed to success/failure at the calculation step; an intuitive error leaves that step unentered under the model. It is not counted as a second observed failure. |
| Logistic function and conditional step probabilities, 379-390 | PASS | For real inputs, `L(s) = 1/(1+exp(-s))` lies strictly between zero and one. Item intercept plus person effect gives the declared step-success log odds. The second probability is explicitly conditional on reaching calculation. |
| Three response probabilities, 391-398 | PASS | The products follow the conditional-probability chain rule. They are nonnegative, and `(1-piR) + piR*piC + piR*(1-piC) = 1`. Multiplying by the conditional calculation probability does not assume independence of the two latent person effects. |
| Item/person structure and model comparison, 399-407 | PASS | Five intercepts at each of two steps give ten item-by-step effects. Larger displayed intercepts increase success probability, matching the source's log-odds direction despite its use of the term difficulty. Model 2 has separate person effects with estimated variation and correlation; Model 1 has a common person effect. Reported scales 1.2/2.1 and latent correlation 0.40 match the source. The latter is not confused with the separate empirical correlation 0.67 between extracted scores. |
| Extracted participant scores, 409-416 | PASS at the source's stated level | The predictors are identified as source-described conditional modes of fitted person-effect distributions, using distinct notation from the simple proportion scores. They are neither raw correctness totals nor probabilities. The text does not select an unreported joint/marginal extraction method. |
| Units and standardization, 418-428 | PASS | Algebra gives `L(s)/(1-L(s)) = exp(s)`. Adding one to a person effect multiplies the corresponding conditional success odds by `exp(1)` with the item fixed; it does not multiply the probability by that factor. Table 3 gives score mean/SD pairs `-0.01/0.86` and `0.04/1.27`. These are distinct from estimated latent scales 1.2/2.1. Numeracy is the explicitly standardized predictor, with table mean/SD `0/1`. |
| Estimation and reproduction boundary, 430-441 | PASS | The description identifies the published response structure and meaning of the reported scores while explicitly leaving unavailable fitting calls, score-extraction calls, numerical settings, score vectors, density/identification specification, and joint/marginal mode details unresolved. No density, optimizer, integration procedure, or participant-level estimator was invented. |
| Connection to the regression table, 463-493 | PASS | The existing reflection and Calculation rows are now tied to the newly named modal scores. Their coefficient and SE values are unchanged. The numeracy slope remains a fitted mean-count difference per one numeracy SD. The different predictor scales do not support comparing absolute slopes as common-scale effects. |

The new display describes per-item conditional probabilities. It does not purport to supply a complete joint sampling model and numerical fitting implementation from which the reported individual scores can be regenerated. The explicit unavailable-details paragraph is therefore material to the PASS judgment. Removing that qualification or claiming numerical reproducibility would require a separate source and statistical assessment.

## Primary evidence used in this recheck

The held source is `source/references/sinayev-peters-2015/sinayev-peters-2015-fpsyg-6-532.pdf`. Its current SHA-256 was revalidated as `6D23EE182D1298C91ADB48C1861BB2D68778BD012188925C558D1D7A1E0A0B27`, identical to the PDF inspected visually in R1.

For this focused recheck I reread successful text extraction directly from complete source pages 3, 5, 6, 7, and 10, plus page 4's Numeracy and CRT section through its page ending. This verifies the branching interpretation, Table 1 coding, item/person model structure, log-odds interpretation, Table 3 means/SDs, conditional-mode description, and Study 2 adjustment paragraph. The R1 complete visual reads of pages 4-11, 13, and 16 remain the underlying table-reading evidence. No source or manuscript pages were newly rendered in R2.

The repair note `spec/research/edition-2026-p19-e1-review-repairs.md` was read for its reported changes and source locators. Its additional indexed-model lookup is not treated here as an acquired fourth source or as authority for an unreported fitting algorithm. No other current reviewer report was read.

## Return boundary

The two original topic findings are closed by the current P19 hash, and the new model interpretation introduces no further required topic repair. The complete R1 Kamp mathematical assessment carries forward through exact body identity and the verified single-heading inverse for the annex. Root may continue the remaining independent and production steps required by the contract.

Only this R2 report was authored. No manuscript edit, test, build, render, subagent, commit, or admission operation was performed.
