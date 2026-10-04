# Affected source-fidelity review: PA consumers, Kamp 6 and integration

Reviewer: `/root/consumer_integral_kamp6_source_review`, a fresh nonauthor.
Date: 8 September 2026 UTC / 7 September Pacific.
Repository: `C:/Dev/the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`.
Review began 05:47 UTC. The root's final frozen amendments, routes and notation have been rechecked; the review is complete within its 45-minute bound. A 15-minute checkpoint was sent; completion preceded the 30-minute checkpoint.

## Final verdicts

| Scope | Verdict | Finding |
| --- | --- | --- |
| A: PA selected-predicate consumer correction, including the final eleventh continuation edit | PASS | The actual selected formulas and constructors support the changed consumers at the preserved scope. |
| B: complete Kamp III.2 Lemma 6 pair | PASS | Statement, both source switches, proof, endpoint cases and examples agree with the held thesis. |
| C: complete integration and expectation pair | PASS | C-S1 was corrected in the final frozen body and the complete comparison theorem/proof was reread. |

These verdicts concern source fidelity and the affected mathematical content read below. They grant no build, manuscript-page, rights, register, board or other admission gate. All findings and the first complete draft were produced without reading current parallel reviewers' conclusions. After that draft was sent, an agent-status inventory unexpectedly displayed the completed topic review's final summary; no other review report was opened, and the already documented finding and verdicts were unchanged. This timing was disclosed to the root. Only this review file is owned by this reviewer; no manuscript, source, test or driver was edited. No test, manuscript build or manuscript render was run.

## Finding C-S1: state the full nonnegative source stage — resolved

In the initially reviewed body `DA89703F5694C0E909294EC4CB6BF414FF4C1F390B74F4D71682201B622DD57A`, `handbook/parts/p15/integration-expectation.tex:174`–175 bound `f` as real, bounded and zero outside a finite-measure set `E`. The next assertion at 183 only added `f >= 0`, so the existing restrictions remained in scope. Lines 190–193 nevertheless identified the construction with Durrett's entire nonnegative stage. This finding and the initial C FAIL were written and sent before the later incidental status-summary exposure.

The held source, printed pp. 21–22 / physical pp. 29–30, Step 3 and Lemma 1.4.4, applies to arbitrary nonnegative measurable functions on the stipulated sigma-finite space, including unbounded functions and an infinite integral. The general nonnegative function has to be declared separately from the preceding bounded finite-support function. For example, `f = 1` on the real line with Borel length is already excluded by the first assertion's support premise.

The root corrected the second assertion at final lines 183–185 to state separately that `f: Omega -> [0,infinity]` is any nonnegative measurable function. I reread the complete comparison theorem, lines 172–195, against its complete unchanged annex, lines 205–252, and the source stage. This resolves the restriction and permits the stated infinite values. Final body: 434 lines, SHA-256 `A29C887386C298112FC4E9820C6A37B3E934112EF32D704A9CC5EE77F5D909D5`. An in-memory reconstruction restoring only the original two scope lines has exactly the initial body hash above, proving that this declaration is the sole body change. No file was rewritten for that comparison.

## A: source and construction checks

The initial ten-file correction note was read completely and hashed to `617822FBC3262D7D09F50E91841127166C7D304C9C6875C89A21D959FDECB2C2`. Its final eleven-file version was then read completely and hashed to `252AD0F0AEABCE023A6ADAA70CFD27FB27BCA670ABB8CC5A8EBAF734C9F886AC`. The separate Sigma-one author note was also read completely. The original source file remains `0509750C13B88A4E18914BD52BDE171C725CBA14221CBFC2227D7693A2B421CC`; this is an identity check, not a fresh reading of that whole source file.

All ten initial actual before files were compared directly with their current counterparts using complete before/current diffs, including the replaced text. The final eleventh file received the same direct comparison. Every before and after hash agrees with the corresponding controlling note; all eleven final target hashes were rechecked. The backups are under `tmp/edition-2026-bounded-kamp4-probability-decision/consumer-before/`, with each relative path's slashes replaced by `--`.

| Current consumer file | Current SHA-256 | Actual reading beyond its full diff |
| --- | --- | --- |
| `handbook/restoration/inherited-09328-09438.tex` | `3C8947571A8DB7953ACCA52551EA4B5A303B6AF6D2FF3B4F3F1ECC8CADC023B4` | Complete 1–552. |
| `handbook/restoration/inherited-09750-09816.tex` | `C349CB272C3771C144798A25029E404EB11B6EC9DBBCA9E252B3A4ECD0EFEF7A` | Complete 1–94. |
| `handbook/restoration/inherited-09877-09924.tex` | `BE42EE8E10B64F754DE176B3F6D716F256CEF8CCFB423F45A27F90370ED5ABA4` | Complete 1–47. |
| `handbook/parts/p05/provability-logic-gl.tex` | `3A9C9FB7A4A1DB02E4380645BDC2DACA78E5E05F7A0465B27EBBF790EE3C5525` | Complete 1–209. |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | `CEAF88551ADCB5D9DAE1318CF13B3B7FDA150024FE14B317875CEE2D681A4D2C` | Complete 1–254. |
| `handbook/parts/p05/pa-checker-arithmetization.tex` | `BFB54076530ADAB0DCAA1ED95E183EBB22341403EAE08187CFDD66F1DC766441` | Complete 1–526. |
| `handbook/annex/p05/internal-proof-predicate.tex` | `0BA00EA54615857EC2EBF334D9C947CBFEF8D67239BE0F78ED2A84126B7AEB28` | Complete 1–534, with the final changed boundary read through its full diff. |
| `handbook/parts/p05/models-and-interpretability-supplement.tex` | `49F73D85C2ECF81812D194B9A079955AD8AE186934302581E21EA240BE415A41` | Complete 1–266, including the original-sentence theorem. |
| `handbook/annex/p05/depth-completion-supplement.tex` | `7BEA46720C677FF6384C3D512D064CD195FEA9B9646B24BF7F200FFC61A3B55A` | Complete 1–357, including both clauses and the changed displays (4) and (9). |
| `handbook/parts/p05/independence-catalog.tex` | `24716C807E6D5F1C8B795225B8E0F0ADAE6209FAEFD2F3B110A8DA01DAAA3BE2` | 243–342: preceding proof end, full consistency presentation and catalog. |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | `9EAFE46E69EE0F91D472B205D2F60E9C8D6053D1775E9BD888DC0625F5C3E4C6` | Complete initial 1–537 and final changed continuation 528–539; sole final edit verified against the exact predecessor. |

Preservation was independently established by the diffs and by exact raw-text substring equality against the backups: certified coding before its proof-predicate definition; the direct numerical construction from `Use exactly` to its final continuation paragraph; checker/selected-Gamma construction before its final paragraph; the old internal-arithmetic/graph/evidence proofs before their changed concluding sentence; and the complete certified numerical MP lemma/proof before its boundary. All five comparisons were equal. The changed whole-file hashes were never used to infer unchanged definitions or proofs.

The certified numerical relation and its chosen numeralwise representative remain the objects of the certified definition and its D1 lemma. The derivability chapter now declares a formula parameter, and its standard PA selection is literally `exists p Gamma_d19(p,x,1)`. The actual D1 and D2 theorem and the new D3 theorem use that same graph. Generic `T` still has its chosen formula and all three derivability hypotheses. The unchanged Loeb statement/proof was read completely to check this consumption.

The consistency sentence uses `0=S0` and the same selected formula. The presentation-dependent consistency definition equates the subscripted sentence with `Con(T)` only when the chosen provability formula is the existential closure of that particular proof formula. GL's realization and the PA dictionary agree with this selection. The modal fixed-point, frame and Solovay assertions retain their separate cited status and the Solovay proof boundary; this review supplies no full GL-completeness closure.

For the Sigma-one theorem, display (4) names the actual bounded positive/negative descriptions, their Gamma outputs and the exact finite numeral-substitution descriptions. The evidence is the existing fixed normal-form evidence, with bounded-leaf priority, weak component guards, original comparisons/binders and the same auxiliary choices. Display (9) follows from the signed original-root invariant and checked packing, then removes the constant root output in the closed case. Its evidence and proof witnesses are both eliminated before discharging the sentence assumption.

The external Q argument retains the full original closed-Sigma-one scope. Its term evaluation and signed bounded-instance recursion are independent of the selected PA builders. The new strict-range enumeration uses the actual `u < v := exists z (u + Sz = v)` abbreviation; the weak enumeration uses the actual reversed-addend `<=` abbreviation and the existing Q lemma. Empty strict bounds, weak zero bounds and dependent witnesses are present. Fixed first-order normal-form equivalence, finite external evidence and the Q evidence-to-original implication finish the original sentence, without transferring an arbitrary representative internally.

### A dependency extent and identities

| Actual dependency | Read extent | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p05/pa-positive-introspection.tex` | Complete 1–562. | `7310A4F7967AD376E54F799324ADDC214535520ACA5AD8174F2D73AA8F9B821B` |
| `handbook/annex/p05/pa-positive-introspection.tex` | Complete 1–984. | `46CCC2144A1599DD6C5118EFCC8CA3BFB7899B8234CEF37E28547D7F47DEB9D0` |
| `handbook/restoration/inherited-09262-09327.tex` | Complete 1–253: actual Gamma formation, fixed-description theorem and evidence interface. | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | Complete predecessor 1–537: finite expansion, numerical meaning, internal library, direct joining invariants, final checker factors and D1/D2 conclusion. Final continuation is recorded above. | Predecessor `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/parts/p05/pa-bounded-proof-builders.tex` | 1–79 and 259–486: conventions, arbitrary-matrix constructor, exact signed bounded descriptions and theorem. | `8345A3C2C7702A5DD039BA6068CEBD7C0B69D2ABE387FB6FDFB29A5E46AFE480` |
| `handbook/annex/p05/pa-bounded-proof-builders.tex` | 271–676: complete case-elimination and bounded-builder proofs. | `0C3D2614397C7CF68D4B32E0179E4A023EB460A8815EAE67E58836326DFA260A` |

The full hierarchy definition in `inherited-08306-08438.tex` and the full Q enumeration in `inherited-09112-09149.tex` were also read. The D3 dependency was checked as an already accepted construction against its actual definitions and complete proof, including signed return to original syntax, arbitrary quantified matrices, every trace conjunct, unchanged quote code and the two final witness eliminations.

## B: Kamp III.2 Lemma 6

The author note was read completely. The complete new body (1–171) has hash `EBB6DEAE8B3C2538DDB8CF5AB9CF24C7C52AA0EB6202585A7E7B33B188AE99DB`; the complete annex (1–271) has hash `9EA42EBBDFFE6A6A9071C581E2F10721CF2D2504B96EC1CE51FE15658469D171`. Both were read in full.

The held thesis `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf` was verified as 128 pages and hashed to `C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`. Complete printed pp. 63–66, 73 and 79–81 (physical pp. 72–75, 82 and 88–90) were inspected as full page images. Printed p. 80 was additionally inspected at its original 300-dpi image resolution. Printed pp. 73, 79 and 80 were also freshly rendered from that held PDF in memory and fully inspected, confirming the stored source-page images. No OCR comparison was substituted for the weak/strict glyphs.

The actual accepted Lemma 1 body (complete 1–202; hash `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6`) and annex (complete 1–212; hash `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1`) were read, including the whole ordered-endpoint realization and guarded-closure interface used by Lemma 6.

The source explicitly assumes a linear structure in Lemma 6. Its local premise controls over the earlier Com convention. The four source points map to `a<b<c<d`; both premises start at `a`, and the past witness at `c` has no added lower comparison with `a`. The source's one-based switch range `1,...,n` becomes `0,...,n-1`. Both printed bounds are weak at the left and strict at the right. The first case selects the realization ending at `d` and uses `w_k <= v_k < w_(k+1)`; the second selects the one ending at `b` and uses `v_k <= w_k < v_(k+1)`.

The proof establishes existence within those ranges using only maxima of finite integer sets. It verifies every eligible switch, rather than relying on an extra inequality available only for its existence witness. Its first new gap is covered by the two old gaps, including the displaced old endpoint; its second new gap is contained in the old v gap. Every point label and the final label at `c` remain required. Both examples, equality of starts, first/last switches, `n=1`, empty gaps and repeated letters were checked. The conclusion keeps exactly n intervals and uses no order completeness. Printed p. 81 was read only to verify the declared Lemma 7 boundary, not to claim its proof.

## C: integration and expectation

The author note and the complete initial body (1–433) and annex (1–552) were read. The final body has 434 lines and hash `A29C887386C298112FC4E9820C6A37B3E934112EF32D704A9CC5EE77F5D909D5`, with its sole scope amendment verified as recorded under C-S1. The unchanged annex hash is `F5F1AE8A99F95BE08E1C4A448EF1DF865D9B49E6D238A6DECED46BEF82EBC7FE`.

The actual held Durrett author manifestation, `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`, was hashed to `AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886`. Every complete printed page 18–37 / physical page 26–45 was freshly read using pypdf, including all exercises and the shared section boundaries. Complete printed pp. 25 and 31 were also rendered from that PDF in memory and inspected visually. Those source renders created no manuscript output.

| Supplied proof | Complete annex reading | Source comparison and result |
| --- | --- | --- |
| Simple integrals | 12–47 | Step 1 / Lemmas 1.4.1–1.4.2: refinement, overlap and zero/infinite measures verified. |
| Monotone convergence | 49–84 | Theorem 1.5.7: direct lower-simple/theta proof works on any measure space, with infinite limits. |
| Nonnegative calculus and Fatou | 86–144 | Lemma 1.4.5, Theorem 1.5.5 and relevant exercises: sums, scaling, null sets and the measure nu_f verified. |
| Signed integral laws | 146–203 | Lemma 1.4.6 / Theorem 1.4.7 / Exercise 1.6.16: finite representatives, finite subtraction and absolute disjoint-set sums verified. |
| Source-stage comparison | 205–252 | Steps 2–3 / Lemmas 1.4.3–1.4.4: proof establishes the full equivalence; final body resolves C-S1. |
| Dominated and bounded convergence | 254–309 | Theorems 1.5.3, 1.5.8 and 1.6.7: limit bound/support proved; stronger L1 conclusion justified. |
| Holder | 311–355 | Theorem 1.5.2, Exercise 1.5.1 and Theorem 1.6.3: zero and infinite norms precede normalization; both endpoints proved. |
| Jensen | 357–403 | Theorems 1.5.1 / 1.6.2: finite supporting slope, measurability, probability normalization and both integrability premises retained. |
| Expectation and law | 405–459 | Theorems 1.6.1 / 1.6.9: indicators, simple approximation, integrability equivalence and all affine infinite-mean sign cases verified. |
| Probability bounds and variance | 461–496 | Theorem 1.6.4 / formulas 1.6.2–1.6.4: measurable function, empty event, finite mean before variance, scaling and centered Chebyshev verified. |
| Stronger-moment convergence | 498–552 | Complete Theorem 1.6.8 proof, p. 31: prior integrability, limit moment bound, non-atomic truncation, two tail errors and return of h(0) verified. |

Measurable a.e. replacement is explicitly required, so no completion of the measure is presumed. The examples were checked on the constructed measures: uniform mean and second moment, undefined paired signed mean, strict Fatou, absence of an integrable concentration dominator, infinite-domain bounded-convergence failure and increasing signed functions with infinite negative integrals.

The unchanged prerequisites were hashed: measurable-probability body `C249F33E0E0FC88084B05A7D44098DB87B3E4814083B34709D6DBE2B562340D9`, annex `FBB9E6C733A1F286F7E56FC31B7E76D4412D781E03711ED02D8D4B3AAEF8C8FC`; measure-extension body `E1333244607DB51AE1EE5EC8FBF6AECA9AE8A2D85989677ED29ED9866119558E`, annex `D5179047198A9EDDE628274345D19DE75E30FC33CE065DAEC9F23F02DE83838F`. Actual readings were measurable-probability body 72–146, 279–387, 427–453; annex 276–369, 431–480; measure-extension body 1–27 and 216–242; annex 283–362. They cover nonnegative sums/measure continuity, measurable operations and complete simple-approximation proof, the law interface/proof, countability of positive masses, constructed length/uniform space and the compact-interval covering proof.

## Final snapshot and remainder

The frozen final routes and notation were read and hashed, including the root's superseding notation snapshot. The complete annex/P9 route, body/P15 route and annex/P15 route were read; the P9 presentation route was read at 132–166, including all six lemma inputs and the surrounding scope statement. Each new pair follows its predecessor. The canonical CSV's physical rows 58, 59, 63, 64 and 956, and every new row 1124–1141, were read in full, along with their corresponding entries in both generated tables; all those entries were reread after the final notation amendment. The registry has 1140 data rows plus its header. The PA formula parameter/selection, evidence identity, Kamp point/range scope and integration extended-value conventions agree with the verified manuscript definitions. The substitution row includes the original-Sigma-one `s_varphi^+` description. The `E_n,theta` row distinguishes arbitrary-measure monotone comparison sets from the separate finite-measure exhaustion and retains the corrected unrestricted nonnegative stage. The changed note symbols are in math delimiters in both generated outputs.

| Final artifact | SHA-256 |
| --- | --- |
| `handbook/registry/symbols.csv` | `E13255CAC4CC6B1D7F611EE723DEB049D5845B834947FD05006795BE1CBFFC35` |
| `tmp/edition-2026-bounded-kamp4-probability-decision/consumer-integral-kamp6/symbols-tables.tex` | `513D057BBDC10420E2E7B6ACF14C2D6239E2FA3F4EE3DD0C7A0AB20BA6DAF80F` |
| `tmp/edition-2026-bounded-kamp4-probability-decision/consumer-integral-kamp6/symbol-index.tex` | `BBB31595E72AB4508136B07A9724C34CE39D3E35CA9C44195B335C15194029F4` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `A1E7A8C1D370F1142FF094A0F6C1E5A4AF53F1D73494EC6A9BE43354346AD592` |
| `handbook/annex/p09.tex` | `52B834018C29E944568A9179E8F3BDBDE4ADFEE5113834BC1D92AC954F4279BF` |
| `handbook/parts/p15.tex` | `2DEEB348EA12691DE61FCAD0E91432D1234F0E55AA8F0EAC21A337B0FBEC35A8` |
| `handbook/annex/p15.tex` | `03C4F16C9822A8FCC3F9DFC687BD2159C67F4614E4B558CE01D6D60F9C9902A6` |

The final checker-annex edit changes only its explanation after the completed D1/D2 proof. It now identifies the already supplied original-sentence builders and D3 theorem, with the same explicit exclusion of arbitrary-representative identification. Its actual proof through line 529 is unchanged against the hashed predecessor. A and B retain PASS, C-S1 is resolved and C now passes. No actionable source-fidelity finding or assigned unread remainder remains. The assigned source extents and all eleven new proof pairs have been read completely; unrelated portions of the older dependencies above are outside this affected review, not claimed as freshly read.

The PDF skill governed direct source-page inspection and the research skill governed tracing to the controlling sources. The assignment's no-subagent instruction controlled its delegation suggestion. Earlier memory informed only the distinction between bounded text review and admission; all artifact identities and current mathematical claims above were checked in this review.
