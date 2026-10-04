# Kamp III.2, Lemma 8 completion: independent mathematical review

Date: 8 September 2026. Reviewer: /root/kamp8_completion_topic_review.
Start: 08:23:30 UTC. Assignment deadline: 09:08:30 UTC.

## Verdict

**PASS for the mathematical content of the complete new Lemma 8 construction at the identities below.** I found no unresolved false assertion, missing proof case, unjustified elementary-membership step, or circular induction in the eight new proof pairs. The final result supplies the original finite-family property-I conclusion over Com, including the empty family and both orientations. This verdict evaluates the new completion itself; the earlier foundation's limited standing was not used as acceptance of the new conclusion.

This is an independent topic verdict. I read no other current review conclusions. I did not run tests, scan the manuscript mechanically, build or render it, inspect a manuscript PDF, modify content or shared files, or perform admission. I did not reread the primary dissertation in this role; source fidelity and production remain their separately assigned reviews.

## Exact objects and reading extent

| Object | Personally read | SHA256 |
| --- | --- | --- |
| `handbook/parts/p09/presentations/kamp-iii2-lemma8-completion.tex` | All 373 lines, 17,171 bytes | `22D58367E4A6C31471D59825476ECA6BB18EACDC1D5DAA8210E1619565D1C9DD` |
| `handbook/annex/p09/kamp-iii2-lemma8-completion.tex` | All 728 lines, 38,911 bytes; all eight complete proofs | `544E30F8E028D5C19BF1505CF9C839EAF9512014A1C41EC08B364BB25438EC05` |
| `spec/research/edition-2026-c7-kamp-iii2-lemma8-completion.md` | All 169 lines | `AFDC2B16402ABDE0182032E7F836FE490A3747ED981924AFFC92D774E52631DF` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma8.tex` | All 493 lines | `ECC3896B4F0C25C58914FFBB9D03A49447D89F5146FF8949EF2CF9B34AD6F61E` |
| `handbook/annex/p09/kamp-iii2-lemma8.tex` | All 762 lines; all seven foundation proofs | `8740AE1FCC283B7313511073AD8D05B167FD92C1E207C37A984D53D00870BF8F` |

Both governing documents were read completely: `handbook/CONVENTIONS.md`, SHA256 `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242`, and `spec/EDITION-2026-CONTRACT.md`, SHA256 `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3`.

The actual additional prerequisite readings were:

| Prerequisite | Personally read | SHA256 |
| --- | --- | --- |
| Lemma 1 body | All 202 lines | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| Lemma 1 annex | All 212 lines | `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1` |
| Lemma 2 body | Lines 1–121: the strict limits, all limiting-class definitions and the opening translation definitions | `49C59D4BDF9169590457F73F3841B35E9620F6C4A54083044DAD625598823677` |
| Lemma 3 body | Lines 1–160: proper substitution, its theorem and the complete E grammar | `811AAA41E515F647CB6BC252A4AFEF59279B8338A0FBB43BE72DA3E572A29BA3` |
| Lemma 3 annex | All 410 lines, including the full first-order substitution identity and finite-closure proof | `91E5182F2545CDA968E8B13FAB320988CEA3B24FC1E6572271A4EC4B66E53C0E` |
| Lemma 4 body | All 318 lines | `1821FB12C4E77B1D531A3BB154581451A972745BAFFAE1FF0611E34152CF13EB` |
| Lemma 4 annex | All 585 lines, including every fusion direction and R5–R8 | `2C1DA5AE40BC16DD4533C64714DEF9868F93D2202202D30E6FFE10AA6DEB451E` |
| Lemma 5 body | All 250 lines | `3FF96929A113AE7273508A7278D42A8DC883D014A592B98E780208BD243480EF` |
| Lemma 5 annex | All 464 lines | `26381378ADECC27A479724DBFAEA4650ACAF4DF29D62B4DF999FD42F758C8963` |
| Lemma 6 body | All 171 lines | `EBB6DEAE8B3C2538DDB8CF5AB9CF24C7C52AA0EB6202585A7E7B33B188AE99DB` |
| Lemma 6 annex | All 271 lines; both switch constructions and every joining-gap case | `9EA42EBBDFFE6A6A9071C581E2F10721CF2D2504B96EC1CE51FE15658469D171` |
| Lemma 7 body | All 278 lines | `3411BB4A552755CAFEF4675851A764A8605CBE36D402C6CFE022E397DE9F9778` |
| Lemma 7 annex | All 489 lines, including all cuts, both universal reductions and both residual bounds | `3E71146A7142A8A2BA26983A6A23634D9E7D3B52AA8A5F4FD2C9CC8793BD817F` |

These names refer to the corresponding `kamp-iii2-lemmaN.tex` under `handbook/parts/p09/presentations/` and `handbook/annex/p09/`. I also read the actual literal At definition at `kamp-iii1-normal-form.tex:66–101` (file SHA256 `0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31`) and the Lin/Com definitions at `n-c-012.tex:14–39`. The new construction uses the limiting classes as literal E generators and their displayed quantified meanings; it does not need a new invocation of their temporal-expressibility proof. No claim of a personal reading of the Lemma 2 annex is made here.

## Verification of all eight new proofs

Line references in this section are to the new completion body or annex, respectively.

| Result | Evidence and mathematical conclusion |
| --- | --- |
| Elementary duality | Body 14–49; annex 6–79. The semantic order reversal is a structural induction. Every one of the five E seed classes has a constructed dual seed presentation; basic past/future and limiting past/future exchange through the actual finite-word realization semantics. Boolean nodes and proper-substitution nodes have explicit finite-history constructions. Raw dual labels are implemented by those representatives. Reversal preserves the exact Com definition and the number of basic-word occurrences. |
| Unary accumulation | Body 51–87; annex 81–138. Neighborhoods come from the one-interval elementary past/future constructors using fresh placeholders. The no-neighbor disjunct is needed and correct at first/last points. Where a neighbor exists, the fixed-endpoint proof supplies the initial/final predicate, the first/last-gap neighborhood and the complete limiting suffix/prefix. The converse uses the smaller/larger of the neighborhood witness and the tested bound. The one-letter limit is handled separately from positive-stage words. |
| Remote limits | Body 89–140; annex 140–246. Nonemptiness follows from the tested outer endpoint. The least cofinal position k yields a bound r on all preceding positions. A selected realization with its k-th point d above r supplies a fixed prefix; its old gap covers points below d, while later cofinal realizations cover every point at or above d and below the remote endpoint. This checks the discarded endpoint d itself and needs no common prefix. The suffix is wholly inside each limiting interval. Conversely the limiting suffix joins the fixed prefix through the prescribed gap. The opposite candidate index is k = n − j + 1, and yields precisely the displayed prefix-limit words. |
| Interior approach | Body 142–173; annex 248–297. Each true fixed prefix has one fixed truth value at the cut. If every such cut failed suffix accumulation, finitely many failure bounds would have a minimum contradicting the approach condition. The converse joins the selected true prefix to each accumulating suffix. Every suffix-accumulation label has the already constructed E history. The no-future case is true on both sides and has an endpoint I representation. Duality supplies the left-approach case. |
| Segmented assembly | Body 175–192; annex 299–372. Basic cut factorization is legitimately transferred to elementary labels using fresh predicate truth sets in the whole structure. Every original edge is cut at every intervening named point and every alternative retained. Adjacent edges are fused with all point and open-gap tests. Missing edges receive the neutral one-interval word. The actual midpoint theorem concatenates the adjacent words and recovers the same named points at specified positions in the converse. Thus all fixed-side conditions and point labels survive elimination of interior names. |
| Localization | Body 194–240; annex 374–463. Both crossing orientations retain every selected fixed prefix/suffix and use the corresponding residual disjunction. All subsets and their finite Cartesian product are enumerated. Selecting all actually true fixed factors proves the forward implication; each positive factor together with its residual reconstructs the original input in the converse. The native-endpoint cases add no cut, and all four placements are included. Every local call has the exact At/Bp form with a fresh atom Q. Only after that call is the actual one-variable E label substituted for Q through R7. |
| Positive supports | Body 242–300; annex 465–564. Actual descriptors imply the indicated supports in all nine type combinations. Conversely every lower support supplies a fixed-start realization strictly before a middle point and every upper support supplies one strictly after it. The four-point hypotheses of the actual Lemma 6 are therefore available. All outside D conditions, unattained-boundary D tests and attained-boundary H witnesses are retained. Empty and singleton truth sets are proved separately. No arbitrary first-order descriptor is declared elementary. |
| Full Lemma 8 | Body 302–351; annex 566–728. The empty/point-only base has the actual one-interval word. Every regional call removes the distinguished maximal input before localization. Positive supports and every boundary D disjunct become actual E point labels or supplied I edges with original endpoints. Finite expansion followed by segmented assembly handles every branch. Right-oriented inputs are reversed, processed by the already proved left construction from strictly smaller hypotheses, and reversed back. This is not a same-rank recursive invocation. Finite branching and the well-founded rank prove termination. |

## Delicate cases checked explicitly

For a basic word of length `2n + 1`, a point cut has left/right lengths `2k + 1` and `2(n − k) + 1`, both shorter. A gap cut has lengths `2k + 1` and `2(n − k + 1) + 1`. Only the last left gap cut or first right gap cut reaches the original length. Therefore an arbitrary selected subset of cuts from one original member supplies at most one residual at that member's original length. Other shorter residuals can be numerous without invalidating the proof. Removing the distinguished maximal member gives at most `c(F) − 1` local members of length `M(F)`; native members, coincident outputs and the new length-one atom obey that count. Fixed-side formulas are outside the local family but are preserved as edges for assembly.

The eleven positive branches were checked individually through their exhaustive type table:

| Case | Lower / upper types | Required interior boundary D tests |
| --- | --- | --- |
| 1 | Empty-set alternative, universal D on the entire original interval | None |
| 2 | 0 / 0 | None |
| 3 | 0 / 1 | None |
| 4 | 0 / 2 | D(h) |
| 5 | A witnessed H(c), with universal D on both remaining subintervals | None at c |
| 6 | 1 / 0 | None |
| 7 | 1 / 1 | None |
| 8 | 1 / 2 | D(h) |
| 9 | 2 / 0 | D(l) |
| 10 | 2 / 1 | D(l) |
| 11 | 2 / 2 | D(l) and D(h) |

For each two-boundary row, every nonempty outside region requires D and the middle requires D or P. The lower supports are, respectively, fixed-start accumulation at a, the attained H(l), and fixed-start approach from the right of l. The upper supports are, respectively, fixed-start cofinality below b, the attained H(h), and fixed-start cofinality below h. This supplies both strict brackets in each of the nine combinations. At a type-1 interior point H itself suffices. At a type-2 point the original D test remains, evaluated with both original outer endpoints. Type-0 points are the outer endpoints and are not tested by the original universal quantifier. Equal regional endpoints make that regional universal condition a tautology; they do not manufacture a new witness.

The old erroneous unbracketed implication is not reintroduced. A positive branch can hold without the full negative absence assertions, but its outside D clauses cover the additional points and its two positive supports still establish both witnesses used by Lemma 6. The forward proof uses a real descriptor only to choose a successful positive branch.

In particular, when a point test D(l) contains a member of Bp(l,b), the final proof retains that edge to b. Localization similarly retains an original left input's prefix on (a,r) and an original right input's suffix on (s,b). Edges spanning other named points are handled by the independently justified elementary cut transfer; their endpoints are not relabeled to make them adjacent.

I checked the endpoint and gap cases directly from the formulas. At a last point C-plus and e-plus are both vacuously true; at a first point the past counterparts agree. Remote cofinality under ordered outer endpoints is not vacuous, and fails at adjacent endpoints. At one interval the remote formula correctly uses the strict terminal limit and does not require its unary label at the terminal endpoint itself. The real-line and two-point examples have the stated truth values. A false gap label still permits an empty gap, whereas a false point label prevents a realization. The point-only empty-family base therefore expresses precisely emptiness of the open interval.

## Result and remaining scope

There are no actionable mathematical corrections from this review at the frozen target identities. The completion proves the full selected Lemma 8 conclusion and supplies actual E/Ep construction histories where required. The proof's complete-order dependence is confined to obtaining truth-set bounds and using supplied property-I equivalences; the auxiliary finite-word identities keep their stronger Lin scope. No Lemma 9, Lemma 10, or Theorem III.2 conclusion is used to establish this result.

This mathematical PASS does not itself decide source fidelity, publication quality, the shared navigation/symbol integration, formal admission, or whole-manuscript completion.
