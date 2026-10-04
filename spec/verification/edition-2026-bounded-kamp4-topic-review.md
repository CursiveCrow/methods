# P5 bounded proof builders and Kamp Lemma 4: independent topic review

Reviewer: `/root/bounded_kamp4_topic_review`. Date: 7 September 2026 Pacific / 8 September UTC.

**Verdict: PASS for P5 NOW-03b; PASS for Kamp III.2 Lemma 4.** The complete supplied statements, constructors and proofs are mathematically valid at their declared scope. No required mathematical repair or unresolved proof obligation was found within either assigned unit.

This review was independent of authorship and other current reviews. I read the complete four target LaTeX files, the actual dependency passages below, both author intakes, and the primary Kamp scans. I made no manuscript edit, software test, build, manuscript PDF inspection, render, admission action or subagent dispatch. Only this report was written. Root's shared route and notation review remains separate. The P5 result supplies NOW-03b, with NOW-03c's evidence-to-original-sentence construction and D3 still subsequent; Kamp Lemma 4 does not complete III.2.

## Frozen targets and complete reading

All paths in this report are relative to `C:/Dev/the-methods-of-reason`. The following hashes were checked at entry and again after the mathematical reading, unchanged.

| Target | Complete read range | SHA256 |
| --- | --- | --- |
| `handbook/parts/p05/pa-bounded-proof-builders.tex` | 1-486 | `8345A3C2C7702A5DD039BA6068CEBD7C0B69D2ABE387FB6FDFB29A5E46AFE480` |
| `handbook/annex/p05/pa-bounded-proof-builders.tex` | 1-676 | `0C3D2614397C7CF68D4B32E0179E4A023EB460A8815EAE67E58836326DFA260A` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma4.tex` | 1-318 | `1821FB12C4E77B1D531A3BB154581451A972745BAFFAE1FF0611E34152CF13EB` |
| `handbook/annex/p09/kamp-iii2-lemma4.tex` | 1-585 | `2C1DA5AE40BC16DD4533C64714DEF9868F93D2202202D30E6FFE10AA6DEB451E` |

## Per-result findings

Body/annex locations in this table refer to the corresponding target pair above.

| Result | Verdict | Checked mathematical content |
| --- | --- | --- |
| P5 logical templates, body 12-102; annex 4-58 | PASS | Exact projection/injection/disjunction-elimination/bottom/RAA rows; branch-specific filters; both copies of the excluded-middle assumption discharged; `Keep` retains the actual otherwise unused assumption. |
| P5 sum exhaustion, body 104-200; annex 60-197 | PASS | Both separately fixed addition orientations, their zero and successor stages, q3 minor, q1/q2 contradiction and peeling, exact arithmetic instance chains, recursive proof instantiation, nonvacuous discharge and all-variable freshness. |
| P5 range exhaustion, body 202-257; annex 199-269 | PASS | Strict-sum helper, weak range using the reversed sum, original comparison binder, arbitrary supplied indices including 0 and 1, strict zero and weak zero. |
| P5 case elimination, body 259-316; annex 271-370 | PASS | Actual finite disjunction recursion, self-substitution with shadowing, equality transport, zero cases, and quantified derivation with original term, guard and binder. |
| P5 fixed bounded builders, body 318-486; annex 372-676 | PASS | All eleven connective branches, all four quantified signs in both comparison orientations, zero/default cases, original literal roots, dependent bounds and witnesses, fixed-description totality and the two internal PA proof-construction implications for the selected predicate. |
| Kamp elementary intervals, body 13-115; annex 6-179 | PASS | All five E-generator parameter changes, finite ordered substitution histories, initial-segment source lists, repeated occurrences, both labelled recursions and realization directions, both R5 orientations and R6. |
| Kamp interval substitution, body 117-149; annex 181-240 | PASS | Exact I(x,y) premise on Com, modified unary interpretation for R7 including self-containing replacements, and both R8 endpoint placements. |
| Kamp conjunction, body 151-318; annex 242-585 | PASS | Complete finite total-preorder enumeration, required endpoint identifications, coincidence/interleaving, occurrence multiplicity, every odd/even slot, both input extractions and converse, all disjunct pairs, boundary examples and Lin-to-Com restriction. |

## P5 calculations supporting the verdict

The q3 instance is exactly `not(v_z = 0) -> exists x_1 (v_z = S v_1)`. Its elimination uses matrix `Eq(v_z,s(v_1))`, witness index w and label 3; the minor assumption is therefore exactly `v_z = S v_w`, marker 4. Since x,z,w are distinct and at least 3, w occurs in neither major nor conclusion nor the remaining temporary assumptions or allowed axiom leaves. This checks the stronger all-variable rule, not merely its free-variable counterpart (body 167-172; annex 160-184).

For either sum orientation, the zero alternative chains `v_x = g(v_x,0) = g(v_x,v_z) = nu(r)`. The predecessor alternative chains `S g(v_x,v_w) = g(v_x,S v_w) = g(v_x,v_z) = nu(r)`. At r = 0, q1 contradicts that exact equality; at r = S n, q2 gives `g(v_x,v_w) = nu(n)`, and the copied previous exhaustion implication gives the preceding disjunction. Appending equality to nu(r) produces exactly D(v_x,S r). Orientation 1 copies D_Z and D_L, so its extra arithmetic results are derived trees whose leaves stay in A_* (body 115-179; annex 74-195).

The strict helper proves `x + S z = nu(n) -> D(x,n)` after q5 and q2; its zero result is bottom. Weak comparison expands to `exists x_h (x_h + x_i = nu(n))`, and therefore correctly uses C_1 to enumerate the right addend. The fresh outer binders of the already closed sum theorem are instantiated before witness elimination; there is no unsafe replacement of index 0 by v_1 beneath the arithmetic axiom's original binder 1 (body 203-238; annex 201-267).

Cases(c,i,Q,n) retains precisely one marked D(v_i,n) major. Its right minor uses `nu(n) = v_i` and the supplied proof of `sub(c,i,nu(n))`; the proved identity `sub(c,i,v_i) = c` supplies its exact conclusion, even when i is absent freely or shadowed. The two equal label numbers in OE act on separate minor lists, so neither consumes the new major. U normalizes only inside the temporary original guard, obtains c through exhaustion and CI, discharges that original guard and then introduces the original binder i (annex 273-368).

Every connective clause uses the selected premise order and yields the exact positive formula or its literal negation. The success guard makes the two negative-conjunction and positive-implication alternatives exhaustive. Negative disjunction remains valid when both children coincide because its filters remain branch-specific. `Keep` makes the true-consequent implication introduction nonvacuous (body 350-396; annex 484-532).

Positive existential and negative universal use an actual bounded-search witness with a proof of the original instantiated guard. Positive universal obtains an actual quantified proof from all case proofs. Negative existential first constructs the bounded universal of the negative matrix, then uses the two copies of its conjunction minor; existential elimination removes both. Its y exceeds every variable index of E and is at least 3, so all remaining A_* leaves also pass freshness. At strict zero, only the valid universal-positive and existential-negative constructors succeed; weak zero retains case 0 (body 398-450; annex 534-650).

Numeral substitutions commute at distinct indices, stop at a matching binder and never rename another binder when the replacement is closed. Child tuple projections preserve surrounding witnesses and override a reused bound index only in its own scope. Each graph has a separately fixed finite formation; no description is an object-language input to an evaluator. The arithmetic inductions use the specified graph equations, Safe includes the actual Tree and leaf tests, and packing supplies exactly Gamma_d19 at output 1. This proves both final PA implications for the same selected Prf^19_PA (annex 374-482, 632-674).

## Kamp calculations and independent source checks

The finite quotient construction is sound: a fusion class contains at most one point tag from each chain; the mandatory endpoint coincidences make the first and last classes common and distinct. Taking all first-chain tags and the independent second-chain tags chooses exactly one representative per class, proving the source length formula. Every odd slot has a point tag. Every even slot lies between a unique consecutive pair of first-chain positions and also a unique consecutive pair of second-chain positions, so every conjunction is nonempty and belongs to E (annex 259-317).

For either extraction, any point inside an original interval is either an inserted fused point or lies in one unique fused gap. The strict inequalities defining f_F place that interval label in the corresponding odd or even slot. Conversely, the union of the two actual realizing chains induces one enumerated fusion; a required point tag is supplied by its input point, and a required interval tag by its original interval. The four odd-slot tag types and both even-slot interval types are all checked. This uses no density or completeness and creates no extra point (annex 324-441).

The sequential-history argument follows replacements at original occurrences and includes letters inserted by earlier steps. Fresh placeholders above every label's predicate indices, with identities at unused preceding indices, yield the literal source initial-segment presentation without later substitutions changing an earlier label. This proves actual Ep/Ef membership up to the explicitly permitted bound variation. R7 changes only a unary interpretation, leaving the complete order intact. Distribution applies the Lin fusion identity separately to every pair of the given Com disjuncts, then restricts to Com (annex 48-177, 185-238, 443-516).

The one-interval, adjacent-endpoint, singleton-order, false-pattern and empty-disjunction cases are valid. The three-point example forces coincidence; each strict fusion requires two distinct interior witnesses. The four-point example detects a false interval label specifically at the inserted point, even though all fused gaps are empty. These directly test the relevant failure modes (annex 518-583).

Held primary source: `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`, SHA256 `C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`. I inspected every page of the existing source scans for printed 63-68 and 73-78 (physical 72-77 and 82-87, one-based physical = printed + 9), including the complete Lemma 4 proof through its explicit end and Lemma 5's following statement. These are primary source pages, not manuscript PDF pages.

Independent correction checks: p. 68 display (13) says Com; p. 73 explicitly switches unqualified equivalence to Com but nevertheless prints Lin in the representation premises. The author's rational-cut example is valid: the sentence C_P is true on Com, whereas P = {q in Q : q < sqrt(2)} has no rational least upper bound, despite the tautological interval representation holding at (0,2). This disproves promotion of that given representation to Lin. The manuscript correctly retains the Com premises and proves only the elementary fusion identity on Lin.

On p. 76 the isolated display has an individual chi_i; p. 74 display (18) and p. 77's converse use the disjunction. The manuscript proves the latter, and its three-point example refutes an arbitrary individual-fusion equivalence. Page 77 does print `iff` for positive-label truth versus required-slot membership; the two-point all-true interpretation refutes the reverse implication, and the proof uses only membership implying truth. The same page conflates an odd singleton slot with the point index k(j) and cites (23) where endpoint condition (19) is needed; h_F and 2 h_F - 1 avoid that error in the supplied proof. The source point clause and its two interval clauses agree with all four clauses of f_F in the reconstruction.

## Actual dependency reading and identities

The following table records the dependency passages actually consulted. Unlisted portions of a dependency are not claimed fully reviewed. The selected targets above were read in full.

| Dependency | Read lines | SHA256 |
| --- | --- | --- |
| `handbook/parts/p05/pa-numeral-proof-builders.tex` | 1-501 | `413117B591123F5B12C78124D1EC13ACE9B15CB3CBB61445DBE9CB6ED8F97BD0` |
| `handbook/annex/p05/pa-numeral-proof-builders.tex` | 1-644 | `3ABD15F81D47E8D5078C46B496DFBE4361ECBF36C25C54CB589CD9D7DC84237E` |
| `handbook/parts/p05/pa-checker-arithmetization.tex` | 1-523 | `993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA` |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | 1-537 | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | 1-252 | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | 1-315 | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/annex/p05/internal-proof-predicate.tex` | 1-310 | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` |
| `handbook/restoration/inherited-09262-09327.tex` | 59-214 | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/restoration/inherited-08306-08438.tex` | 28-94 | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma1.tex` | 1-174 | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| `handbook/annex/p09/kamp-iii2-lemma1.tex` | 1-147 | `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma2.tex` | 1-93 | `49C59D4BDF9169590457F73F3841B35E9620F6C4A54083044DAD625598823677` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma3.tex` | 14-208 | `811AAA41E515F647CB6BC252A4AFEF59279B8338A0FBB43BE72DA3E572A29BA3` |
| `handbook/annex/p09/kamp-iii2-lemma3.tex` | 1-381 | `91E5182F2545CDA968E8B13FAB320988CEA3B24FC1E6572271A4EC4B66E53C0E` |
| `handbook/parts/p09/presentations/kamp-iii1-normal-form.tex` | 11-200 | `0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31` |

Context read: `n-c-012.tex:1-190` for Lin/Com, equality-free L, strict S/U and D; `EDITION-2026-WORK-PACKAGES.md:262-277` for NOW-03b's full constructor scope. These shared documents are not frozen by this report. Author intakes read: `spec/research/edition-2026-p5-bounded-proof-builders.md:1-75`, hash `3AA06BA86E8F6646472AFE40AAC6A785681253C4CDD5EC312D83C5EEDAF6C287`; `spec/research/edition-2026-c7-kamp-iii2-lemma4.md:1-199`, hash `D8891BAAD3FD275B8FE8496F8E84D32BB9BA65B3D1C50B55677684304B704BF8`.

The PDF skill directed primary scan inspection. Historical memory supplied only the workflow distinction between scoped text review and admission; mathematical verdicts use the current texts and primary passages recorded above.
