# Kamp Lemma 8 foundations and single-peaked majority: independent mathematical review

Date: 8 September 2026. Reviewer: `/root/kamp8_foundation_median_topic_review`.
Block began at 07:28 UTC; the 45-minute deadline was 08:13 UTC.
The full target reading and prerequisite checks were completed before the
first 15-minute checkpoint was due. An interim report to the lead recorded
the full four-file reading and the subsequent prerequisite checks.

## Scoped verdict

**PASS for the seven supplied Kamp supporting results. PASS for the seven
single-peaked-majority results.** No mathematical correction is required in
these frozen targets on the evidence of this review.

The Kamp verdict covers the comparison, single-cut finite-family reduction,
normalization, fixed-endpoint accumulation representations, eleven-case
classification, hull interpolation, and guarded universal decomposition.
It does not establish the full elementary-representation induction in
Lemma 8. That obligation remains explicitly open at body lines 478-493 and
annex lines 757-760. In particular, a correct first-order boundary descriptor
has not thereby been proved to have property I.

The majority verdict includes the entire strict social ordering on the full
source interval, the odd and even median conclusions, all stated finite
algorithm claims, the worked examples, the full-interval parity example,
and compatibility with the exact unrestricted-domain Arrow theorem.

This is a mathematical text review. No manuscript PDF, rendering, build,
software test, canonical registry, generated lookup, or admission action
was used or performed. No other current review report or verdict was read.
The author intakes were treated as statements of intended scope, not as
acceptance evidence. Printed-source fidelity is a separate review role;
this reviewer checked the mathematics of the supplied countermodels without
claiming a fresh reading of the historical PDF pages.

## Frozen target identities and complete reading

All four files were read line by line in full, including every definition,
formula, example, proof, qualification, and final proof boundary. Their
hashes were checked before reading and again after the prerequisite checks.

| File | Exact extent read | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p09/presentations/kamp-iii2-lemma8.tex` | 1-493, complete | ECC3896B4F0C25C58914FFBB9D03A49447D89F5146FF8949EF2CF9B34AD6F61E |
| `handbook/annex/p09/kamp-iii2-lemma8.tex` | 1-762, complete | 8740AE1FCC283B7313511073AD8D05B167FD92C1E207C37A984D53D00870BF8F |
| `handbook/parts/p17/single-peaked-majority.tex` | 1-309, complete | BA7EF43E3E28026890EE178439A32CF13614D6E430CF916350FEFC479D423063 |
| `handbook/annex/p17/single-peaked-majority.tex` | 1-404, complete | 1AA78E18617B8DE56578E7DA915F5A02F276FEA09737A21811EB21705E3AC3E0 |

Both author intakes were read completely:
`spec/research/edition-2026-c7-kamp-iii2-lemma8.md`, 217 lines,
1F4F79991AB23E61A20ACC5FAA9D2925ED29E85E056DBCFFA462C8FE7ECE59FC;
and `spec/research/edition-2026-p17-single-peaked-majority.md`, 143 lines,
6FEE2C27D11C89679F1294151D1E5A2417B1A1112C4D98AC682DF78D0B840128.

The governing contract was read completely, 168 lines,
C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3.
`handbook/CONVENTIONS.md` was read completely, 251 lines,
4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242.

## Kamp: proof checks

| Result / annex extent | Mathematical checks and conclusion |
| --- | --- |
| `kamp-family-rank`, 6-70 | The existential comparison really is lexicographic in the maximum length and its multiplicity. A witnessing length must occur in F, so it lies between the two maxima; equality forces the exact multiplicity comparison. Empty families, deletion of the sole member, unbounded numbers of shorter outputs, and coincidences among outputs are all covered. Removing one maximal member leaves at most c(F)-1 maximal outputs. PASS. |
| `kamp-family-cut`, 72-176 | The full Cartesian product of cut power sets is enumerated, with the exact cardinality and the one empty tuple at k=0. In the forward left direction each subset consists of all true fixed suffixes; in the right direction it consists of all true fixed prefixes. These choices are independent of the varying universal point. The converse uses every selected fixed-side conjunct. Arbitrary auxiliary formulas retain their displayed quantifier scopes, including a free v in the outer auxiliary. The rank application explicitly requires an actual eligible residual family. PASS. |
| `kamp-family-normalization`, 178-273 | Whole At formulas are replaced by one fresh atom, preserving the literal At grammar and the declared length-one convention even for its particular tautology. Basic occurrences receive separate fresh letters. Disjoint fresh targets make the restoration sequence faithful and preserve family cardinality. The empty-family base represents an empty open interval rather than manufacturing a witness. Adding Q changes neither maximal count nor predecessor class when M>1. Substitution of falsehood removes the disjunct. PASS. |
| `kamp-fixed-endpoint-limits`, 275-386 | For n=1 the limiting label is a unary strict limit; for n>1 it is the actual positive-stage suffix or prefix limit with n-1 intervals. The forward proof extracts a genuine first or last gap from the outer endpoint instance. The reverse uses the minimum or maximum of two supplied points and extends the exact suffix or prefix. Both displayed two-interval words therefore have the claimed guarded Lin identities and explicit E labels. Adjacent endpoints and vacuous unrelated gaps are correctly handled. PASS. |
| `kamp-eleven-boundaries`, 388-523 | A nonempty truth set is bounded by the two outer endpoints. Completeness supplies both extrema; coincident extrema give exactly the singleton case. Otherwise the lower and upper endpoint/attained/unattained alternatives give nine disjoint cases with l<h. All six first-order type formulas were checked in both directions, including their actual-member instances at a or b. These formulas keep the original fixed endpoint. PASS. |
| `kamp-hull-interpolation`, 525-609 | A point strictly inside the infimum/supremum bounds has actual truth-set members strictly on both sides. The left orientation applies the precise four-point Lemma 6. The right orientation explicitly reverses the order, word, point sequence, gaps, and guarded closure; it does not assume that the two syntactic orientations coincide. The assertion is conditional over Lin and does not assume missing extrema. PASS. |
| `kamp-corrected-boundary-decomposition`, 611-762 | The open interval is exhaustively partitioned into two side regions, two possible boundary points, and the middle region. Outside the hull H is false, attained interior boundaries satisfy H, unattained interior boundaries require D, and outer endpoints receive no test. Interpolation justifies D-or-P only inside the actual hull. Every one of the nine displayed matrices and the empty and singleton branches agrees with this partition. Both implications retain the descriptor, every required endpoint test, and the original endpoints inside D and H. Completeness is used only for existence of a descriptor in the forward implication. PASS. |

The exact cut lengths were checked against the actual preceding definitions
and proof: a point cut has lengths 2k+1 and 2(n-k)+1, both shorter than
2n+1; a gap cut has lengths 2k+1 and 2(n-k+1)+1. Only the last gap on the
left and the first gap on the right retain the original length. This
includes n=1, where each side has its single length-three residual. The
new finite-family proof therefore invokes the predecessor's actual bound.

Both correction countermodels are valid as mathematical examples. On
0<1<2 with all basic letters false, the original universal fails at 1,
while a tautological added disjunct makes it true. On the six-point order,
H(1) holds through the empty gap, H(4) fails at the B-false point 2, and
the other interior points fail C. Thus the fixed-start truth set is exactly
{1}; Q fails at 4 while the unrestricted past pattern holds through (3,4).
The weakened first-witness branch is true and the original target false.
The retained singleton descriptor and its Q requirement reject that case
correctly. The separate rational-cut illustration also correctly shows why
the eleven-case exhaustion requires completeness.

No proof of full Lemma 8 is smuggled into the prerequisites: normalization
transports an assumed representation, and the accumulation representatives
are constructed directly. The final guarded decomposition alone leaves
the declared remote-endpoint representations and all induction assembly
work to be supplied.

## Single-peaked majority: proof checks

| Result / annex extent | Mathematical checks and conclusion |
| --- | --- |
| `single-peaked-structure`, 11-51 | The peak is greatest and unique. On every a<b<c, b is above at least one endpoint. The converse correctly retains existence of a greatest alternative on infinite X; the finite greatest-element argument supplies it only in the finite case. The four listed rankings are exactly the permitted triple restrictions. PASS. |
| `single-peaked-majority`, 53-105 | Odd integer counts orient every distinct pair. The two voter-set inclusions rule out both possible orientations of a directed three-cycle. Failure of full transitivity would produce one of those cycles. This proves the entire ordering, including on an infinite X; weak transitivity is then checked for diagonal and strict cases. PASS. |
| `median-peak-winner`, 107-150 | The two k+1 coalitions use the correct sides of the median peak. They prove strict defeat of every rival independently of transitivity, uniqueness of both strict and weak winners, and the two same-side conditions for single-peakedness of the already established social ordering. Repetition, endpoint peaks, one voter and a singleton alternative set are covered. PASS. |
| `even-median-interval`, 152-186 | Every point between the central peaks has at least k supporting voters against every rival. Every point outside loses to a central peak by at least k+1 votes. Coincident central entries provide strict majorities in both directions away from their common value. Distinct central peaks are distinct weak winners and exclude any strict winner. No transitivity claim is made for the even weak relation. PASS. |
| `single-peaked-algorithm`, 188-263 | A valid permutation gives exactly a strict ordering with the forced rank-one peak. Adjacent same-side inequalities are necessary and chain to all required comparisons, establishing sufficiency. The histogram handles repeated peaks. In the odd strict social ordering, victories increase strictly with social preference and occupy exactly 0,...,q-1, so the count-indexed output recovers the complete ranking. The O(nq), O(n+q), and exact nq(q-1)/2 rank-comparison bounds agree with the stated representation and unit-cost assumptions. PASS. |
| `single-peaked-boundaries`, 265-352 | All ten unordered-pair counts were independently recomputed from the five rankings and agree with the displayed matrix and c>b>d>a>e order. The comparison a versus e genuinely differs from the median-peak voter's ordering. The three-voter cycle and four-voter tie failure have their claimed votes. The interval distance-and-tie-break relation is complete, irreflexive and transitive, remains strictly single-peaked, and restricts to the required four rankings at 0, 1/2, 1. PASS. |
| `single-peaked-arrow`, 354-404 | Pareto and anonymity follow from the exact counts. IIA is quantified over two admissible profiles and preserves the full pair comparison. For every candidate dictator, the opposing endpoint profile is admissible on the whole interval and refutes that candidate when n>=3. The explicit first-three-then-remainder ordering is a valid strict ordering outside the domain. The unrestricted-domain premise in the actual preceding Arrow theorem is therefore absent. PASS. |

The even example has peaks x,x,y,z and exact weak winners x,y on its
three-point axis, in agreement with the full [l,u]_X theorem. In the
interval extension, the weak winners form the full interval [0,1/2]; the
displayed three comparisons suffice to witness nontransitivity on that
larger domain. No claim that the median voter's complete preference is
dictatorial, no continuity premise, and no conclusion about strategic
truthful reporting is used in these proofs.

## Actual prerequisite reading

These are direct current-file readings of the used definitions and
arguments. A partial extent below is not a claim to have reread the whole
predecessor unit.

| Prerequisite | Extent read | SHA-256 |
| --- | --- | --- |
| `parts/p09/presentations/n-c-012.tex` | 1-48: actual Lin, Com and language standing | Driver remains root-owned; no dependency-wide acceptance claimed. |
| `parts/p09/presentations/kamp-iii1-normal-form.tex` | 1-120, including the complete At and truth/falsehood definitions | 0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31 |
| `parts/p09/presentations/kamp-iii2-lemma1.tex` | 1-160: basic grammar, words, guarded realization interface | 3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6 |
| `annex/p09/kamp-iii2-lemma1.tex` | 1-120: complete binary realization induction and construction from words | 631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1 |
| `parts/p09/presentations/kamp-iii2-lemma2.tex` | 1-145: exact unary and positive-stage limiting clauses | 49C59D4BDF9169590457F73F3841B35E9620F6C4A54083044DAD625598823677 |
| `parts/p09/presentations/kamp-iii2-lemma3.tex` | 1-165: proper substitution, exact E grammar and finite closure | 811AAA41E515F647CB6BC252A4AFEF59279B8338A0FBB43BE72DA3E572A29BA3 |
| `parts/p09/presentations/kamp-iii2-lemma4.tex` | 1-150: elementary labelled words, I and substitution interface | 1821FB12C4E77B1D531A3BB154581451A972745BAFFAE1FF0611E34152CF13EB |
| `annex/p09/kamp-iii2-lemma4.tex` | 1-240: complete elementary-word and I-substitution proofs | 2C1DA5AE40BC16DD4533C64714DEF9868F93D2202202D30E6FFE10AA6DEB451E |
| `parts/p09/presentations/kamp-iii2-lemma6.tex` | 1-171, complete | EBB6DEAE8B3C2538DDB8CF5AB9CF24C7C52AA0EB6202585A7E7B33B188AE99DB |
| `annex/p09/kamp-iii2-lemma6.tex` | 1-271, complete | 9EA42EBBDFFE6A6A9071C581E2F10721CF2D2504B96EC1CE51FE15658469D171 |
| `parts/p09/presentations/kamp-iii2-lemma7.tex` | 1-278, complete | 3411BB4A552755CAFEF4675851A764A8605CBE36D402C6CFE022E397DE9F9778 |
| `annex/p09/kamp-iii2-lemma7.tex` | 1-181: complete cut factorization, both directions and exact lengths | 3E71146A7142A8A2BA26983A6A23634D9E7D3B52AA8A5F4FD2C9CC8793BD817F |
| `parts/p17/social-choice.tex` | 1-217: strict/weak domain, counts, IIA, dictatorship and exact Arrow statement | 224340F36A0774478ED6CFD8713601190B23F97BE7950106DD4CD8F8B71E64FA |
| `annex/p17/social-choice.tex` | 87-223: complete extreme-alternative and Arrow proofs, including the unrestricted profile constructions | C76738A8942F81BD5BF37E3701A30820AD24992E5B3805EC448CD9D883D69E6F |
| `parts/p17/finite-preferences.tex` | 1-52: complete weak/strict/indifference interface | 58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C |

All abbreviated prerequisite paths in this table are relative to `handbook/`.
No manuscript or shared file was edited. The only authored artifact of this
review is this report. The lead may use the scoped mathematical passes with
the other independent roles; formal admission and completion of the whole
book remain separate actions with their actual requirements.

## Focused recheck: explicit distance and completed Problem 2 reference

At 08:05 UTC the lead requested a recheck limited to two changes, with a
five-minute limit. **PASS for both changes.** The preceding mathematical
passes remain applicable to the resulting targets and the unchanged proofs.

The exact saved predecessors and current files were hash-verified and
compared in full with `git diff --no-index`. The comparison shows one local
passage changed in the median annex and only the final proof boundary
changed in the social-choice body; all other text is preserved.

| Artifact | Predecessor SHA-256 | Current SHA-256 |
| --- | --- | --- |
| `handbook/annex/p17/single-peaked-majority.tex`, now 408 lines | 1AA78E18617B8DE56578E7DA915F5A02F276FEA09737A21811EB21705E3AC3E0 | 5DDA4E25ADEF9987B45CE7050836D5BB2BEC11D9A55959FBDE460B8CEDE25E89 |
| `handbook/parts/p17/social-choice.tex`, now 323 lines | 224340F36A0774478ED6CFD8713601190B23F97BE7950106DD4CD8F8B71E64FA | 83E82EB6AF1353725E3D48799390AD9F4F3CAFCF566E694514C0D1AC2E5CCDCB |

The predecessor files are respectively `median-annex.tex` and
`social-body.tex` under
`tmp/edition-2026-bounded-kamp4-probability-decision/kamp8-median/before/`.

I reread current median annex lines 265-408, including the entire affected
counterexample proof and the following Arrow proof. The definition
`d_p(t)=max{t-p,p-t}` gives `p-t` for `t<=p` and `t-p` for `t>=p`, as
stated. These agree at t=p. Ordering by smaller distance and then larger
alternative preserves exactly the original strict comparison. The proof
still covers unequal distances and equal-distance tie-breaks, establishes
transitivity, and excludes self-comparison. The two same-side formulas
prove the required strict improvement toward the peak without assuming
continuity. At peaks 0,0,1/2,1 the restrictions to 0,1/2,1 remain the
specified four strict rankings. Thus the full-interval nontransitivity
example and the complete weak-winner interval remain valid.

I reread the final 35 lines of the current social-choice body, including
the entire changed boundary at lines 312-323. Its reference names the
actual `sec:p17-single-peaked-majority` chapter, whose complete body and
proofs were read above. That chapter supplies the indicated full majority
ordering and median results. The new boundary retains other preference
domains, aggregation methods, strategic questions, the related-results
discussion and Problems 3-5. It does not infer a strategy theorem from
Arrow or from a median-winner theorem. The change is mathematically and
logically consistent with the reviewed completion of Problem 2.

The unchanged median body and both Kamp target hashes were verified again
and still equal the initial frozen identities. No unchanged proof was
reopened. No other current reviewer report was read, and only this report
was edited for the recheck.
