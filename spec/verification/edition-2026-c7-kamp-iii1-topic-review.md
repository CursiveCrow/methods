# Edition 2026 C7: independent topic review of Kamp III.1

Date: 7 September 2026. Reviewer: `/root/kamp_iii1_topic_review`.

## Verdict and scope

**PASS for the mathematical content of the frozen III.1 normal-form theorem, its full quantifier construction, its sentence corollary, and its separately stated starred support property.** No counterexample or omitted quantifier-position case was found in the active reconstruction. The output is a first-order normal form over every nonempty strict linear order with arbitrary unary interpretations. This review establishes neither Theorem III.2 nor temporal expressive completeness over `Lin`.

The scope is the complete new reader file, complete new annex, and the active Kamp language/order prerequisites in `n-c-012.tex`. The governing edition contract was read completely. The author note was used as a source locator and as a list of claims to challenge; its conclusions were not accepted as review evidence. No other new C7 review was read before this report was filed.

This is a topic review. No tests, manuscript build, static checker, manuscript rendering, admission operation, or delegation was performed. Existing images of the primary source pages were inspected directly under the PDF skill. Only this report was authored.

## Frozen artifacts and live verification

All paths in this table are relative to `C:/Dev/the-methods-of-reason`.

| Artifact | SHA256 verified during this review |
| --- | --- |
| `handbook/parts/p09/presentations/kamp-iii1-normal-form.tex` | `0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31` |
| `handbook/annex/p09/kamp-iii1-normal-form.tex` | `A46BFF4D11C868E8A865F2F9CC89690FCB4D03A550EB6CCB755B4C067A3B7F8B` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `A12201D510F6FE514BC4300F65A34AAA10B0DE0429979ABD10D8BE8F07AE4E5E` |
| `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf` | `C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA` |
| `spec/EDITION-2026-CONTRACT.md` | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `spec/research/edition-2026-c7-kamp-iii1.md` | `D576C1FA5FF57E20FDD28BE2B5CAD44D1A5C41F4402A99CDF8022F2E5F094B4D` |

Actual reading: all 231 lines of the new body; all 380 lines of the new annex; `n-c-012.tex` lines 1-363, including the operative prerequisites at lines 16-72 and the integration/scope passage at lines 133-167; and the complete author note. The body input occurs at `n-c-012.tex:138`. The root-owned annex input is present at `handbook/annex/p09.tex:6`, between `alc-general-tboxes` and `csl-corrections`. Reading this seam is not a build check.

Primary source inspection covered every page of printed pp. 43-56, physical PDF pp. 52-65, using the existing `source-c-052.png` through `source-c-065.png` images. Printed pp. 21-22, physical PDF pp. 30-31, were additionally inspected for the displayed language and interpretation convention. The scans, rather than their malformed extracted text, controlled the source comparisons.

## Mathematical findings

### 1. Language, prefixes and the quantifier-free basis: PASS

The active prerequisite fixes nonempty `T` and a strict asymmetric, transitive relation comparing distinct points (`n-c-012.tex:16-40`). The displayed language has only variables, Boolean connectives, quantifiers, `<`, and the countable unary predicates (`n-c-012.tex:42-72`; thesis p. 21). The new coincidence abbreviation is therefore legitimate: in a strict linear order, `not(x < y) and not(y < x)` holds exactly when the assigned points coincide. It introduces no predicate. The order constants `not(x < x)` and `x < x` have the stated truth values and retain their variable syntactically (body lines 11-24).

The ordered-partition construction covers all assignments of a finite nonempty set of variables. Its adjacent strict chain and representative equalities determine exactly one partition, and each partition is realizable in its finite chain. Thus different canonical prefixes are incompatible and their collection is exhaustive, without an assumption about unmentioned points (body lines 26-63; annex lines 24-36; thesis pp. 44-46).

The quantifier-free step preserves the whole named free-variable set even when a particular disjunct originally used fewer variables: it enumerates complete prefixes on that set. Under each prefix, replacing a unary literal's variable by its block representative is valid for every unary interpretation. The construction explicitly handles a missing order part, a missing unary part, inconsistent order conditions, contradictory unary conjunctions, and formulas with no unary predicate (annex lines 49-77). The two displayed order-negation rewrites are valid by linearity.

### 2. Both existential equality cases: PASS

When the quantified variable is nonessential, it appears in its unique representative equality and in no local component. Deleting that equality leaves the right residual prefix; the reverse implication assigns the existing representative point to the quantified variable. When the quantified variable is essential in a nonsingleton block, substitution by the first surviving member preserves each recursive component class after bound-variable renaming. The proposed replacement variable could not already have been a different component endpoint: it was a redundant member of this same block. The one-variable residual prefix is explicitly repaired to self-coincidence (annex lines 79-122; thesis pp. 50-51).

These arguments cover, for example, a prefix `x = y` with `x` first in variable-name order and a local `At(x)` condition, as well as a prefix `y = x` with `y` first and a local `At(y)` condition. Both reduce to the appropriate condition at `y`, and neither needs a new order point.

### 3. All three strict existential positions, including empty regions: PASS

Deleting a singleton quantified block affects only its exterior cell and neighbor, or its two neighboring interior cells. Consequently every component independent of the quantified variable is still local for the residual prefix; the remaining components are exactly the three permitted unions listed in annex lines 131-138.

The equation at annex lines 151-163 retains `exists x (beta and D)` even when the dependent list is empty, using the starred true slot. This is exactly what its semantics requires. For the left ray, right ray, and adjacent gap, the resulting component lies respectively in `Bef`, `Aft`, and `Bet`. Finitely many constituent stages have a common finite bound, so the next stage contains the result. No existential point is inferred merely from an endpoint comparison.

Concrete boundary checks by direct semantics:

| Formula and assignment | Required result | Reconstruction |
| --- | --- | --- |
| `exists x (x < y and P(y))`, one-point order, `P(y)` true | False: no predecessor | Retained left-ray existential is false |
| `exists x (y < x and P(y))`, one-point order, `P(y)` true | False: no successor | Retained right-ray existential is false |
| `y < z and exists x (y < x and x < z)`, integers, `y=0`, `z=1` | False: empty open gap | Retained `Bet` existence condition is false |
| Same endpoints in the rational order | True: e.g. `x=1/2` | Retained `Bet` existence condition is true |

The first three checks refute the corresponding transformations with the existential region test deleted. They do not refute the active text.

### 4. Universal prefix restriction and full position grouping: PASS

For a residual prefix with `s` essential points, the proof includes both equality-representative operations and all singleton deletions, then groups by the residual prefix and all `2s+1` positions. These consist of `s` equalities, `s-1` open gaps, and two open rays. Under the residual prefix they are exhaustive and disjoint for any assignment to the quantified variable (annex lines 173-242; thesis pp. 52-55).

The displayed universal equivalence at annex lines 230-234 is justified assignment by assignment. Exactly one residual prefix is true; within it exactly one position is true at each domain point. No universal quantifier is distributed over the original unpartitioned disjunction. All residual prefixes are included, even when the inner normal form originally supplied no group for one of them.

A missing strict-position group receives a false consequent, forcing that region to be empty. A missing equality group also receives a false consequent and fails because its named point exists. For a residual prefix with one representative `y`, an inner disjunction supported only on `x < y` cannot accidentally become universally true: its missing equality group fails at `x=y`. An inner formula permitting equality and the two rays but omitting an interior gap between two representatives is universally true only when that gap is empty. This is the content of the source's missing-position conditions, retained in the reconstruction.

### 5. Universal CNF conversion and all dependent-disjunct cases: PASS

The position-group matrix is a positive disjunction of conjunctions of local components. Its finite conversion to conjunctive normal form introduces no negated component, so it does not assume closure of `At`, `Bef`, `Aft`, or `Bet` under arbitrary Boolean operations. Universal distribution is then over a finite conjunction (annex lines 244-255).

Equality positions reduce to the substituted local disjunction because the equality position has its named realization. For a strict position, the proof handles all dependent components, no dependent components, and a mixture separately (annex lines 257-317; thesis pp. 55-56). In the no-dependent case it retains the disjunct `forall x (beta implies false)`. In the mixed case the independent disjunction has one fixed truth value while `x` varies; if false, precisely the dependent universal remains. Each argument is valid also when the region is empty.

For example, on a one-point order with `P(y)` false, `forall x (x < y implies P(y))` is true. The active transformation at body lines 213-223 returns the true empty-ray disjunct. Deleting it would incorrectly return false. The same reasoning applies at a last point and between consecutive endpoints.

All newly quantified strict-position components fit the corresponding regional grammar. The independent disjuncts remain allowed local components of the residual prefix. Finite distribution of the resulting formulas therefore gives actual standard clauses with that prefix, completing the universal induction.

### 6. Finite stages, effectivity, free variables and unary support: PASS

Bound-variable renaming is explicit before free substitution (body lines 57-63; annex lines 107-116). The recursive guards retain each displayed endpoint, so regional components have exactly their displayed endpoint variables free. The prefix on the full original free-variable set prevents accidental loss of a named free variable in a constant or inconsistent output branch.

The induction applies to the finite original prenex quantifier prefix. Each step incorporates a quantifier into a regional component; it does not try to remove the newly constructed regional quantifiers again. Enumeration of finite ordered partitions, Boolean distribution, representative choice, fresh names, grouping, and substitution are effective finite operations. A common stage can always be chosen; when all constituents are `At`, stage zero suffices and the new regional formula is in stage one (annex lines 151-163, 300-340). No order-size, density, or completeness condition enters this argument. No output-size or complexity bound is claimed.

During the starred induction, only existing unary literals are relocated or repeated. Order-only true and false slots suffice even when the input has empty unary support. This proves the additional support property as stated, without imposing it on Kamp's literal grammar.

### 7. Literal source components and epsilon: PASS for output membership

The scan of thesis p. 47 confirms the `At` basis of unary-literal conjunctions together with the distinguished unary tautology. Thus neither order-only true nor order-only false is a literal source `At` formula. The body explicitly acknowledges this and creates starred classes for those two slots (body lines 66-127). The annex announces at its start that stars are suppressed only during that separate construction (annex lines 14-22). The later unstarred-looking uses of `bot_x` in the induction are covered by this express convention.

The epsilon map changes distinguished component slots only; it does not rewrite the order prefix or regional guards. At a base slot it yields the permitted tautology or contradictory unary conjunction at the same variable. Both have the same truth value as their starred antecedents in every strict linear order, for every interpretation of `P_0`. A stage induction then preserves the regional constructor, puts its converted constituents into the permitted source classes, and preserves truth. Clause structure and free variables remain unchanged (annex lines 342-360). Consequently the output lands in the source's unindexed component classes; equivalence alone is not being used as a membership rule. Only the explicitly disclosed constant encodings may introduce `P_0`.

One source notation detail should be retained in provenance: in the printed p. 47 `Bef` constructor, the constituent union displays an unindexed `Bef(z)` where the new body lines 96-98 display `Bef_n(z)`. The mirror `Aft` clause and the `Bet` clauses display their stage indices. The active staged recursion is well founded and is sufficient for the theorem and epsilon proof. Even reading the source occurrence literally as the eventual union, every component admitted by the reconstruction's stricter finite-stage rule is admitted by that source constructor, because `Bef_n(z)` is contained in `Bef(z)`. Thus this discrepancy supplies no counterexample to output membership or the normal-form theorem. It is nevertheless a concrete source-index regularization that the author provenance note should identify, rather than describing every finite-stage inscription as identical to the scan. This is a source-provenance observation, not a mathematical blocker for the reviewed theorem.

### 8. Sentence corollary and scope: PASS

At a top-level Boolean connective of a sentence, each immediate argument is itself closed because free-variable sets combine by union. At a closed `Qx psi`, either `psi` has exactly the free variable `x`, so the proved theorem gives a standard one-variable matrix, or `psi` is closed and the quantifier is vacuous. Removing that vacuous quantifier is valid on the stipulated nonempty domain. There are no closed atomic formulas in this constant-free language. The supplied true and false sentence encodings have the stated truth values on every nonempty order (annex lines 362-378).

This proves exactly the Boolean-combination corollary on thesis p. 56. The body lines 225-231 and the active continuation in `n-c-012.tex:140-167` preserve the further `Com` requirement for the temporal result. The III.1 proof does not use a supremum, infimum, endpointlessness, or density assumption, and its regional quantifiers remain first-order quantifiers.

## Independent assessment of the two reported source errors

**C7-SRC-01 is an actual printed error and the active repair is correct.** The p. 49 scan displays a conjunction of opposite strict inequalities as the replacement for negated equality. On the two-point strict chain `0 < 1`, assign `u=0` and `v=1`. Negated coincidence is true, but `u < v and v < u` is false. The active disjunction at annex line 62 is true, and linearity proves it equivalent to noncoincidence generally.

**C7-SRC-02 is an actual printed error and the active repair is correct.** The top of p. 52 explicitly drops the left-ray existential condition when none of the local conjuncts contains the quantified variable. On the singleton order with `P(y)` true, its matrix `x < y and P(y)` has no witness, although the result with the existential deleted is true. The active proof retains the existential with a true dependent slot. Its separate right-ray and interior-gap cases preserve the corresponding witness obligations as well. The universal no-dependent case in the source already retains its empty-region alternative; the active reconstruction also retains it.

## Remaining gates

There are no unresolved mathematical findings for the exact frozen III.1 body and annex reviewed here. The p. 47 omitted source index is recorded above for source-provenance adjudication. Independent source and publication verdicts, manuscript static/build/visual evidence, and a separate admission record remain outside this topic verdict. Content changes to the reviewed body, annex, or operative prerequisites require review of their affected mathematical scope.
