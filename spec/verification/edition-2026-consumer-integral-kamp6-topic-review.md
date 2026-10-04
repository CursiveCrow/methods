# Mathematical review: PA consumers, Kamp Lemma 6, integration and expectation

Date: 8 September 2026 UTC / 7 September Pacific. Reviewer: `/root/consumer_integral_kamp6_topic_review`, a fresh nonauthor. Review began at 05:48 UTC; final reading and report verification concluded at 06:00 UTC, within the assigned 45-minute limit. Only this report was written.

## Verdict

| Assigned scope | Mathematical verdict | Reading coverage |
| --- | --- | --- |
| A. Exact ten-file PA selected-predicate consumer correction | PASS | Every actual before/after change, necessary surrounding mathematics, the complete current Sigma-one theorem and 357-line annex, and the selected-construction dependencies described below. |
| B. Kamp III.2, Lemma 6 | PASS | Complete 171-line body and 271-line annex, including both examples and every stated boundary case. |
| C. Integration and expectation | PASS | Complete 433-line body and 552-line annex; all eleven full theorem/proof pairs and all examples. |

No actionable mathematical finding remains in these assigned scopes. PASS concerns the supplied mathematical statements and arguments. This report makes no source-fidelity, publication, build, rendering or admission decision. No manuscript edit, software test, manuscript build, rendering or subagent review was performed. No current source or publication review conclusions were consulted.

## Frozen targets and actual before comparison

The controlling consumer note is `spec/research/edition-2026-pa-selected-consumer-correction.md`, 46 lines, SHA-256 `617822FBC3262D7D09F50E91841127166C7D304C9C6875C89A21D959FDECB2C2`. I read it and compared each actual current file with its actual predecessor under `tmp/edition-2026-bounded-kamp4-probability-decision/consumer-before/`, using the stated slash-to-double-hyphen filename mapping. Every predecessor and current hash matches that note. The table records the exact checked pairs.

| File | Before SHA-256 | Reviewed SHA-256 |
| --- | --- | --- |
| `handbook/restoration/inherited-09328-09438.tex` | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` | `3C8947571A8DB7953ACCA52551EA4B5A303B6AF6D2FF3B4F3F1ECC8CADC023B4` |
| `handbook/restoration/inherited-09750-09816.tex` | `EFA16565DC4206D722BA62585AA452A86394B5827C84B6201C6340815062D2DE` | `C349CB272C3771C144798A25029E404EB11B6EC9DBBCA9E252B3A4ECD0EFEF7A` |
| `handbook/restoration/inherited-09877-09924.tex` | `2AA31395C09B01D9D0058A7AEDAE38FCB148A03C9DBAFD2EE52DC70125B74AA0` | `BE42EE8E10B64F754DE176B3F6D716F256CEF8CCFB423F45A27F90370ED5ABA4` |
| `handbook/parts/p05/provability-logic-gl.tex` | `9AD6D30124B666C8845B421FA40BED296CC59621D0F733C7053581C870EF183E` | `3A9C9FB7A4A1DB02E4380645BDC2DACA78E5E05F7A0465B27EBBF790EE3C5525` |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` | `CEAF88551ADCB5D9DAE1318CF13B3B7FDA150024FE14B317875CEE2D681A4D2C` |
| `handbook/parts/p05/pa-checker-arithmetization.tex` | `993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA` | `BFB54076530ADAB0DCAA1ED95E183EBB22341403EAE08187CFDD66F1DC766441` |
| `handbook/annex/p05/internal-proof-predicate.tex` | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` | `0BA00EA54615857EC2EBF334D9C947CBFEF8D67239BE0F78ED2A84126B7AEB28` |
| `handbook/parts/p05/models-and-interpretability-supplement.tex` | `6FF8A78906F572422862078DD5E75E07F6924BAAA16E73E37ADCD8F21D20E6C1` | `49F73D85C2ECF81812D194B9A079955AD8AE186934302581E21EA240BE415A41` |
| `handbook/annex/p05/depth-completion-supplement.tex` | `C04CCF07077B183DC4BC8AB622CC49653CA6B927C40A81AE074D57A407808FF0` | `7BEA46720C677FF6384C3D512D064CD195FEA9B9646B24BF7F200FFC61A3B55A` |
| `handbook/parts/p05/independence-catalog.tex` | `5C0F15A7244728C5DC703F625BEB03D039E504284BE1A8B2D51D75CA5F75F599` | `24716C807E6D5F1C8B795225B8E0F0ADAE6209FAEFD2F3B110A8DA01DAAA3BE2` |

| Complete new target | Lines | Reviewed SHA-256 |
| --- | --- | --- |
| `handbook/parts/p09/presentations/kamp-iii2-lemma6.tex` | 171 | `EBB6DEAE8B3C2538DDB8CF5AB9CF24C7C52AA0EB6202585A7E7B33B188AE99DB` |
| `handbook/annex/p09/kamp-iii2-lemma6.tex` | 271 | `9EA42EBBDFFE6A6A9071C581E2F10721CF2D2504B96EC1CE51FE15658469D171` |
| `handbook/parts/p15/integration-expectation.tex` | 433 | `DA89703F5694C0E909294EC4CB6BF414FF4C1F390B74F4D71682201B622DD57A` |
| `handbook/annex/p15/integration-expectation.tex` | 552 | `F5F1AE8A99F95BE08E1C4A448EF1DF865D9B49E6D238A6DECED46BEF82EBC7FE` |

## A. PA consumer correction

The changed definition at `inherited-09328-09438.tex:472` correctly retains the certified numerical presentation and its chosen numeralwise representative. The actual before comparison shows that its numerical definitions and numeralwise D1 proof were preserved. The local selection in `inherited-09750-09816.tex:7` changes the standard PA application to the literal `exists p Gamma_d19(p,x,1)` while retaining the formula parameter, proof-existence meaning and D1-D3 hypotheses for a generic theory. The full current 94-line fragment was read.

The current selected definition and theorem in `pa-checker-arithmetization.tex:396-494` supply the promised formula, its standard proof meaning, internal D2 and metatheoretic D1. I read the actual internal MP proof in `handbook/annex/p05/pa-checker-arithmetization.tex:317-537`: the offset/open-list and parent-count invariants, actual final rule, direct axiom checks and graph-output elimination justify the universal implication. Its finite numeral computation establishes D1 for this same graph. The certified numerical `mp` remains explicitly distinct from `mp_19` in the changed continuation.

The complete current second-incompleteness statement/proof and its unchanged 60-line Loeb dependency were read. `Con(T)` uses the chosen formula, so the standard PA consistency sentence uses exactly the selected graph. Loeb's D1-D3 argument and the contradiction argument remain valid for the formula parameter. The revised subscripted consistency discussion identifies the two consistency expressions only when that particular proof formula has the chosen existential closure; it asserts no internal equivalence with an arbitrary certified representative.

The complete 209-line GL chapter was read. Its realization and all affected PA dictionary entries consistently use `Prv^19_PA`. D1, D2, D3 and Loeb give the asserted arithmetical soundness. Finite-frame completeness, the modal fixed point and Solovay completeness retain their cited status and stated scope. The consumer change does not supply or claim a completed local Solovay arithmetization.

The complete current Sigma-one theorem at `models-and-interpretability-supplement.tex:139-167` and the complete 357-line `depth-completion-supplement.tex` were read against the actual correction. Both promises survive: external true original closed Sigma-one sentences are provable in Q, and the internal schema is proved for the literal selected PA graph. The class is the original closure class, including dependent witnesses under bounded universals; no prenex restriction was substituted.

In equation (4), each `Gamma_d_theta` output is a proof value and each `Gamma_s_theta` output is the original numeral-instance code. The separately fixed substitution descriptions have the stated input order and unique outputs. The bounded-builder theorem has exactly those hypotheses and supplies the selected-checker conclusion; its graph formulation licenses the displayed existential witnesses. The negative branch uses the negation of the original substituted code.

The evidence alias is exact. The current annex fixes `E_varphi = Ev_varphi = E_(N+ varphi)` with the same auxiliary choices, associations and retained comparison binders. Its bounded priority, conjunction, disjunction, existential and universal clauses match the actual library. In particular, evidence guards remain weak `<= e`; the marked existential retains its own original guard. Equation (6) requires only logical elimination/introduction and the fixed normal-form equivalence in Q. Equation (7) uses the actual PA beta-extension/finite-collection induction, with parameters retained, strict empty range and weak one-entry zero range.

The external Q proof uses the two actual comparison expansions. Its added strict enumeration follows from `y+Sz=S m`, successor injectivity, and the zero-or-successor split of `z`; the zero range is contradictory. This supplies precisely `j<m`, while the separately proved weak enumeration supplies `j<=m`. No unproved equivalence of those two abbreviations inside Q is used. Bounded truth and refutation constructions cover both quantified signs and both zero cases. Standard finite evidence, Q's bounded-instance theorem and equation (6) then give the external clause for the original sentence.

For equation (9), I read the complete accepted positive-introspection body and 984-line annex, including the signed construction and the literal graph/D3 specialization. The signed Boolean identities (S1)-(S3), original-connective constructors, arbitrary-matrix bounded collection and safe-tree packing give the original root required by the consumer. The original closed sentence has an empty parameter tuple, so its substitution graph has the constant original code. Eliminating that graph output, the evidence witness and the proof witness yields precisely the selected provability sentence. The D3 specialization uses the literal code of that provability sentence as its output root; the input sentence need not itself be Sigma-one. No D3 instance is assumed in producing the evidence proof.

### PA dependency reading and hashes

The full accepted D3 body/annex were read. The graph/evidence library in `internal-proof-predicate.tex:1-406`, the graph and evidence declarations in `inherited-09262-09327.tex:67-253`, the complete weak Q enumeration, and the actual hierarchy definition in `inherited-08306-08438.tex:28-94` were read. The bounded-builder dependency was read selectively at body `318-486` and annex `372-473`, including its exact theorem, description, substitution, Boolean and finite-description interfaces; its previously accepted remaining raw-template/exhaustion proofs were not independently rereviewed in full here. Likewise, the checker dependency outside its selected declaration and full MP proof was inspected through the actual interfaces used, not rereviewed as a new checker construction.

| Dependency | Reviewed SHA-256 |
| --- | --- |
| `handbook/parts/p05/pa-positive-introspection.tex` | `7310A4F7967AD376E54F799324ADDC214535520ACA5AD8174F2D73AA8F9B821B` |
| `handbook/annex/p05/pa-positive-introspection.tex` | `46CCC2144A1599DD6C5118EFCC8CA3BFB7899B8234CEF37E28547D7F47DEB9D0` |
| `handbook/parts/p05/pa-bounded-proof-builders.tex` | `8345A3C2C7702A5DD039BA6068CEBD7C0B69D2ABE387FB6FDFB29A5E46AFE480` |
| `handbook/annex/p05/pa-bounded-proof-builders.tex` | `0C3D2614397C7CF68D4B32E0179E4A023EB460A8815EAE67E58836326DFA260A` |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/restoration/inherited-09262-09327.tex` | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/restoration/inherited-09112-09149.tex` | `23A060D7646D1BBB54480F35833F2D40A78180E67A36232CF8406D7E71B3FBAE` |

## B. Kamp III.2, Lemma 6

The statement and the whole proof use one fixed occurrence word and one interpretation. The original past witness is unrestricted relative to `a`; only its strict past relation to `c` is required. The exact pattern has `n>=1`, `n+1` points and `n` intervals.

Both switch arguments are valid on an arbitrary strict linear order. In the first branch, the greatest index with `w_i<=v_i` exists below `n` because index zero qualifies and the final index does not; it supplies an eligible index for the actual weaker condition `w_k<=v_k<w_(k+1)`. The proof then correctly handles every eligible index, including the least one returned by the method. In the second branch, the analogous greatest comparison index supplies `v_k<=w_k<v_(k+1)`. Both range conversions are exactly `0,...,n-1`, corresponding to `1,...,n`.

For the first new gap, every point below `w_(k+1)` lies in the old w gap, and every point at or above it lies in the old v gap because `v_k<w_(k+1)`. This proves the stated union cover, including discarded endpoints that become interior points. For the second new gap, `v_k<=w_k` gives inclusion in the old v gap. All unchanged gaps keep the predicate at their own index; every point keeps its original point label, including `A_n(c)`.

The proof covers both extreme switches, `n=1`, equal starts, empty gaps, adjacent points, repeated letters, absent witnesses and domains without four ordered points. No supremum in the underlying order is used. The finite overlap example and the failed-final-label example were recalculated and satisfy every stated assertion. Thus the actual proof has Lin scope.

I read the complete Lemma 1 body and annex lines `1-133`, including the full ordered-endpoint realization equivalence and guarded-closure equivalence actually used here. Its body/annex hashes are respectively `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` and `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1`. Its later temporal-construction proof was outside the dependency needed for Lemma 6. The author note was read; a new source-page review was not needed for this mathematical verdict.

## C. Integration and expectation

| Complete annex proof | Mathematical check |
| --- | --- |
| `12-47`, simple integral laws | Common refinement proves representation independence, finite additivity, scaling, order and overlapping sums. Empty cells and zero coefficients on infinite-measure cells are explicitly valid under the declared convention. |
| `49-84`, monotone convergence | The lower-simple/theta argument proves the reverse bound directly from continuity below of a measure. Zero cells, infinite simple integrals and infinite limits are handled without finite-measure or sigma-finite assumptions. |
| `86-144`, nonnegative calculus | Increasing simple approximations give additivity and scaling, then series by increasing partial sums. The zero-integral and finite-a.e. criteria, measurable null replacements, Fatou tail infima and weighted-measure additivity all follow with the stated domains. |
| `146-203`, signed laws | Part integrals determine definedness; the finite representative removes undefined pointwise infinite sums. Difference representations and linearity rearrange only finite values. Disjoint-set sums are absolutely convergent by the absolute integral bound. |
| `205-252`, source-construction bridge | Finite-support signed dyadic upper/lower approximations have gap `2^-n mu(E)`. The sigma-finite exhaustion is explicitly assumed for its truncation clause. Both zero bound and zero-measure support are covered. |
| `254-309`, dominated and bounded convergence | The Fatou argument subtracts only finite integrals and proves L1 convergence. In-measure convergence first supplies the limit's bound and support; the estimate `delta mu(E)+2M mu(|f_n-f|>delta)` then proves the claimed result, including `M=0`. |
| `311-355`, Holder | Norm zero implies zero a.e.; real-valued factors avoid pointwise undefined products. Nonzero infinite norms are settled before division. The essential bound is attained a.e., Young's minimum is correctly computed, and both endpoint exponent pairs are covered. |
| `357-403`, Jensen | Convex secant comparisons prove continuity and a finite supporting slope. The supporting affine function is integrable under the probability normalization; the final inequality uses exactly the assumed integrability of f and its convex transform. |
| `405-459`, integration over a law | Indicators, simple functions and increasing approximation establish the nonnegative formula on both spaces. Absolute integrability and signed subtraction then transfer. Infinite nonnegative means under every scalar sign are handled without subtracting infinities; atomic evaluation includes infinite values at zero-mass points. |
| `461-496`, probability bounds and variance | The nonempty-set infimum is finite because the function is finite valued. The empty event is separate. Markov includes extended nonnegative variables. Cauchy-Schwarz first proves the finite mean, so variance expansion, affine scaling and centered Chebyshev use integrable terms. |
| `498-552`, stronger-moment convergence | Fatou bounds the limit's moment before use. The tail ratio and compact boundedness first prove integrability. Non-atomic truncation levels give bounded convergence, and the two tail errors are uniformly at most `K epsilon_M`. The final p-th-moment example satisfies every assumption. |

All examples were checked directly: the concentration integrals stay one and force a divergent harmonic lower bound for any dominator; their negatives refute an unrestricted signed Fatou inequality. Expanding supports on the constructed real-line measure show failure of bounded convergence without finite support measure; negative tail indicators show failure of the displayed monotone conclusion without its nonnegativity condition. Uniform-cell sums give mean `1/2`, second moment `1/3` and variance `1/12`. The paired atomic example has both part expectations infinite, so its signed mean is undefined.

The actual measurable-probability prerequisites were checked at the measure laws, countable atomic model, measurable limits/simple approximation, pushforward law and positive-mass countability statements and their used proof portions. The simple-approximation proof uses only measurability, so its use for the arbitrary measure in this chapter is valid. The actual measure-extension dependency was checked at its Stieltjes construction and compact-cover argument, followed by the complete Lebesgue/uniform-space proof. These constructions do not use the integral under review. I read the integration author note for its source and dependency map; the mathematical verdict uses the supplied arguments rather than a citation as a replacement for a missing case.

| Accepted prerequisite | Reviewed SHA-256 |
| --- | --- |
| `handbook/parts/p15/measurable-probability.tex` | `C249F33E0E0FC88084B05A7D44098DB87B3E4814083B34709D6DBE2B562340D9` |
| `handbook/annex/p15/measurable-probability.tex` | `FBB9E6C733A1F286F7E56FC31B7E76D4412D781E03711ED02D8D4B3AAEF8C8FC` |
| `handbook/parts/p15/measure-extension.tex` | `E1333244607DB51AE1EE5EC8FBF6AECA9AE8A2D85989677ED29ED9866119558E` |
| `handbook/annex/p15/measure-extension.tex` | `D5179047198A9EDDE628274345D19DE75E30FC33CE065DAEC9F23F02DE83838F` |

The two prerequisite pairs were selectively reread for the dependencies just listed, not independently reviewed in full as new units. No assigned target proof remains unread. Further source exercises, general Lp completeness, density representation, conditional expectation, product measures and Fubini remain outside the supplied unit's claims.

## Bounded addendum: two root corrections

8 September 2026, 06:08-06:11 UTC. Both corrections PASS mathematically. This addendum updates the two affected snapshot entries above; the original report remains a record of its earlier snapshot. No other reviewers' reports were read and no accepted proof was generally reopened.

| Corrected file | Current lines | Current SHA-256 |
| --- | --- | --- |
| `handbook/parts/p15/integration-expectation.tex` | 434 | `A29C887386C298112FC4E9820C6A37B3E934112EF32D704A9CC5EE77F5D909D5` |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | 539 | `9EAFE46E69EE0F91D472B205D2F60E9C8D6053D1775E9BD888DC0625F5C3E4C6` |

The integration theorem at body lines `172-195` now explicitly resets `f` to an arbitrary measurable map `Omega -> [0,infinity]` before the sigma-finite assertion. I read the whole theorem and its existing annex proof at `205-252`. For this new scope, `min(f,n) 1_(E_n)` is measurable, bounded and supported on a finite-measure set; the sequence increases to f at finite and infinite values. Monotone convergence proves the limit, and its integrals increase to the stated lower supremum. The proof uses no boundedness or finite support of f in this second assertion. Its annex remains unchanged at `F5F1AE8A99F95BE08E1C4A448EF1DF865D9B49E6D238A6DECED46BEF82EBC7FE`. The domain reset therefore makes the general nonnegative stage explicit and is fully supported.

For the PA annex, I verified the actual predecessor `tmp/edition-2026-bounded-kamp4-probability-decision/consumer-before/handbook--annex--p05--pa-checker-arithmetization.tex` at SHA-256 `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5`. The complete before/after diff changes only its final explanatory paragraph, now lines `531-538`; an additional byte comparison confirms that the preceding 29,678 bytes and the final annex delimiter with trailing bytes are identical. I read the replacement with the preceding D1/D2 conclusion and its two referenced body theorems. The original-Sigma-one theorem supplies exactly `widehat d_sigma^+`, the evidence-to-proof invariant and the original sentence root; the direct D3 theorem concerns the same literal selected graph. Their body remains at `7310A4F7967AD376E54F799324ADDC214535520ACA5AD8174F2D73AA8F9B821B`. The new continuation correctly points to these completed constructions while preserving the distinction from the D1/D2 proof and from an arbitrary numeralwise representative. It introduces no circular premise or new mathematical claim beyond those established dependencies.

No actionable mathematical finding remains for either patch. Only this report was amended.
