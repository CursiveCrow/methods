# Edition 2026 C7: Kamp III.2, Lemma 2

Edition date: 7 September 2026. Assignment: NOW-04 / N-c-012.
Authoritative repository: `C:\Dev\the-methods-of-reason`.
Authoring began after the source identity and complete relevant scan extent
were verified; the block crossed midnight UTC into 8 September while remaining
on 7 September in the task's local timezone.

Editorial correction after independent source review: two glyph readings in
the initial author note were wrong. The preserved original is
`history/edition-2026-c7-kamp-iii2-lemma2.author-3363ca8a.md`, SHA256
`3363ca8ac3673de152c6d1d96745ed192b299c527ca3716f74aaccc1f74ea1c1`.
The source reviewer and lead independently inspected complete printed pages
66 and 70 at 300 dpi. Both show the correct witness variable and interval
endpoint. The current text and source dispositions below correct the
misattribution directly. The separate research repair note records the exact
changes; all current acceptance still requires the independent recheck.

## Saved result and standing

The complete limiting-pattern construction and proof are saved in:

- `handbook/parts/p09/presentations/kamp-iii2-lemma2.tex`, 212 lines,
  SHA-256 `49c59d4bdf9169590457f73f3841b35e9620f6c4a54083044dad625598823677`.
- `handbook/annex/p09/kamp-iii2-lemma2.tex`, 312 lines,
  SHA-256 `75bae1d38b195849018e8f573741a7f04b8f0984c6804fecff770d00602fa4f2`.

The source's Lemma 2 states that every member of `Lp union Lf` is expressible
over `Lin`. The new text gives the paired limiting definitions, explicit
finite temporal formulas, the complete past and future splices, endpoint and
adjacency cases, and an additional handbook comparison placing a predicate
at the current point. That comparison is not a definition from Kamp's scan.
The draft supplies the mathematical proof at this lemma's complete scope.

This is an author draft for integration and three fresh independent reviews.
The author has not independently accepted it. No tests, manuscript static
checks, manuscript builds, manuscript renders, formal admission, or subagents
were used. The accepted III.1 and Lemma 1 files were preserved. The only
repository writes by this author are the two named new LaTeX files and this
note.

## Exact held primary and actual reading

Primary: Johan Anthony Willem Kamp, *Tense Logic and the Theory of Linear
Order*, UCLA dissertation, 1968, held at
`tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`.

Verified SHA-256:
`C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.

Printed page n corresponds to physical PDF page n + 9, with physical pages
counted from one. The complete actual source reading was:

| Printed pages | Physical pages | Extent read |
| --- | --- | --- |
| 57-59 | 66-68 | Temporal and first-order derived operations, named-variable expressibility, and the relevant closure convention. The construction proves the needed limit-operation closure directly rather than relying on the continuation of R4. |
| 63-65 | 72-74 | Basic past/future grammar, guarded existential closures, predicate occurrence words, and their finite-chain realization conditions. |
| 66-67 | 75-76 | Full limiting-class definitions, including the witness-point future base and positive-stage subscripts; the elementary closure E and its role as context. The initial variable misreading is corrected below. |
| 68-69 | 77-78 | Immediate surrounding definitions and the beginning of the previously completed Lemma 1, read as source context. |
| 70-73 | 79-82 | End of Lemma 1, the complete statement and proof of Lemma 2, its one-interval case, induction, and splice; then the next Lemma 3 statement/proof and the following switch to the Com convention as handoff context. |

Every listed source page was inspected as an actual rendered scan. Printed
p. 66 was additionally inspected at 250 dpi to resolve the future-base
variable and the positive-stage subscript. The PDF skill guided this visual
inspection. Its read-only source workflow was used; no output PDF was authored
or re-exported.

The held layout-text extraction is malformed and was not used as formula
authority. A fresh MiKTeX text-extraction attempt encountered its local-cache
access restriction; the available Poppler renderer supplied the actual source
pages. These were source-page images in a temporary directory, not manuscript
renderings. The source PDF was unchanged.
The generated source-page images were removed after inspection; the unchanged
held PDF is sufficient to regenerate them.

## Source findings and correction dispositions

The active reconstruction supplies the complete proof with explicit indexing
and boundary cases. It also includes a separately identified handbook
comparison. The source itself remains unchanged; the two corrected reading
errors below belong to the initial author note, not to Kamp.

| Source locator | Actual issue | Disposition in the saved construction |
| --- | --- | --- |
| p. 66, displayed `Lf_0(y)` | The actual scan has `P_i(z)` in `exists z (y < z < x and P_i(z))`, matching the past witness-point convention. The initial author note misread the glyph as y. | Both active base definitions agree with the source. The additional `CurF_A` current-point condition is explicitly a handbook comparison with its own proof and counterexample; it is not attributed to Kamp. |
| pp. 66-67, positive-stage definitions; pp. 70-72, proof | The definition labels the constructor from `Bp_n` as `Lp_(n+1)` / `Lf_(n+1)`, although the basic stages begin with `Bp_1`. The proof then treats a one-interval matrix as `Lp_1` and an `(n+1)`-interval word as `Lp_(n+1)`. | Index the active positive limiting stages by their actual number n >= 1 of basic interval pieces, matching the proof's one-interval base and its induction. The zero stage retains its one-letter limit. The positive union still contains precisely all displayed finite-pattern constructors; no `Bp_0` is invented. |
| p. 70, displayed one-interval limiting formula | The actual universal interval condition is `u < z < v`. The initial author note misread v as y. | The active `Bp_1(u,v)` matrix already matches the source. No source-formula correction is needed at this location; the false correction claim is removed. |
| p. 72, claim of membership in `Bf` before (16) | The printed membership assertion attaches `Bf` to the outer limit expression. It is the inner guarded existential whole-pattern formula that is a basic future formula. | Apply the accepted basic-pattern lemma to that inner formula, then apply the explicitly proved P' operation. The reconstruction makes no membership claim for the outer limiting formula. |
| p. 72, crossing index in the converse of (16) | A realization with points indexed 1 through n+2 can first reach/pass the current point between any consecutive pair; the displayed `k < n` does not cover all such crossings. | Use zero-based words with n intervals and choose the greatest k with `u_k < t`. Its full range is `0 <= k < n`, where this n is the actual interval count. In the source's n+2-point indexing, the correct range is `1 <= k <= n+1`. The new proof explicitly permits the last crossing and equality with t. |
| pp. 70-73, source proof direction | The source develops the past direction and leaves the future counterpart implicit. | Supply a separate future decomposition, first crossing index `1 <= k <= n`, prefix splice, all new-gap checks, and its two extreme crossing positions. |
| p. 73, convention after Lemma 3 | The default changes from Lin to Com only after Lemma 3. | Lemma 2 is proved over Lin throughout; its next handoff identifies Lemma 3 as still a Lin result. No order-completeness hypothesis enters either splice. |

The high-resolution scan determines both repaired readings directly.
No inference about the author's intended meaning is needed at those two
locations. The preserved author note records how the misreadings entered
the draft; the current source claims and reader text no longer repeat them.

## Source-to-construction mapping

| Mathematical component | Saved content |
| --- | --- |
| P', F' and their strict interval meaning | `def:p09-kamp-limit-operators`; annex equations (1)-(2) derive the quantified meanings directly from S/U. |
| Base and higher limiting classes | `def:p09-kamp-limiting-classes`; explicit guarded formulas with free-variable and interval-count conventions. |
| Basic whole-pattern expressions | `E^-_sigma`, `E^+_sigma` refer to the accepted Lemma 1 recurrences and their exact word realizations. |
| Explicit finite translation | `def:p09-kamp-limit-translation`: delete the first interval for the past recurrence, the last interval for the future recurrence; the one-letter seeds are P'(A) and F'(A). |
| Complete source lemma statement | `thm:p09-kamp-iii2-lemma2`, with named-variable D equivalence over every nonempty strict linear order. |
| Past induction and source (14)/(16) construction | Annex equation (3), including its n=1 specialization and the full splice (4)-(5). |
| Future direction | Annex equation (6) and the independently written crossing/prefix splice (7)-(8). |
| Scope and endpoint cases | Endpoint, adjacency, singleton, equality-at-crossing, and empty-gap analysis; no density or completeness premise. |
| Worked formulas and countercases | One-interval formulas; examples showing that the second conjunct is necessary; last past crossing and both extremal future crossings. |
| Additional current-point comparison | Handbook-defined CurF_A condition, exact temporal expression, direct proof, and a counterexample to replacing the source's witness-point base by a current-point predicate. |

## Direct mathematical checks in the authoring block

1. **Past splice and interval predicates.** From a whole pattern beginning
   below t, if its last point reaches or passes t, choose the last old point
   u_k below t. The suffix condition gives v_1 < ... < v_n between u_k and t.
   The new chain is `u_0,...,u_k,v_(k+1),...,v_n`. Its sole new gap is a
   subinterval of `(u_k,u_(k+1))`, so it has precisely the required B_(k+1)
   predicate. All point positions retain their corresponding A_i predicate.
   The count is n+1 points, including k = 0 and k = n-1.
2. **Future splice.** If a whole pattern ending above t starts at or below t,
   choose the first old point u_k above t. A prefix realization lies between
   t and u_k. The joined chain is `v_0,...,v_(k-1),u_k,...,u_n`; its new gap
   lies inside `(u_(k-1),u_k)`. Both k = 1 and k = n, including equality of
   u_(k-1) with t, are covered.
3. **Endpoint vacuity.** A first point has no past cut, and a last point has
   no future cut. The corresponding limiting condition and every derived
   temporal limit factor are true. An immediate predecessor/successor gives
   an empty intervening interval and makes the corresponding family false.
   On a singleton both families hold regardless of all predicates.
4. **Necessary conjuncts.** On R at zero, A = (-infinity,0), B = R, C = {1}
   makes the first past conjunct true but the second conjunct and limiting
   pattern false. The future counterpart A = {-1}, B = R, C = (0,infinity)
   has the corresponding outcome. A provisional chain may cross the current
   point, so the suffix/prefix condition cannot be omitted.
5. **Extremal crossings.** With all predicates true, the past chain (-3,-1,0)
   at t = 0 and suffix (-1/2,-1/4) splice to (-3,-1,-1/4), exercising the
   last crossing and equality at t. Future examples (0,1,3) and (-2,0,1)
   with prefix (1/4,1/2) exercise the first and last future crossings.
6. **Current-point comparison.** At zero on R with A = {0}, the current-point
   predicate is true and every right interval contains a witness, so CurF_A
   is true. The source's A(z) witness limit is false. The comparison formula
   is expressed by `no strict future point OR (A AND F'(true))`.

These are explicit semantic calculations and proofs in the saved annex, not
software tests that mirror the manuscript.

## Integration, notation and next assignment

The lead should include the new body immediately after
`\input{parts/p09/presentations/kamp-iii2-lemma1}` in
`handbook/parts/p09/presentations/n-c-012.tex` (currently line 149), and include
the new annex after `\input{annex/p09/kamp-iii2-lemma1}` in
`handbook/annex/p09.tex` (currently line 7). The source key is the existing
`Kamp1968`; no bibliography or shared symbol file was edited.

New main identities are `sec:p09-kamp-iii2-lemma2`,
`thm:p09-kamp-iii2-lemma2`, `sec:annex-p09-kamp-iii2-lemma2`, and
`annex:p9.kamp.iii2.lemma2`. New local notation includes the typed formula
operations H', G', P', F', partial-minus/partial-plus, the indexed limiting
classes, E-minus/E-plus for the old basic expressions, Lambda-minus/Lambda-plus
for the new expressions, and the additional CurF_A current-point comparison. The
source's occurrence sequence remains the already adopted sigma notation.

The next exact source task is **Lemma 3 on printed p. 73**, concerning the
class E defined on pp. 67-68 by Boolean and proper predicate-substitution
closure of current-point, basic and limiting classes. Its assignment must
read the full applicable proper-substitution definition and closure result,
give the finite compositional construction and capture-avoidance argument,
and preserve Lin as its class of structures. The switch to Com occurs only
after that lemma. The later interval lemmas, Lemmas 4-10, and the concluding
III.2 construction remain separate obligations. This block establishes none
of those larger completions.

## Pass, fail and unresolved conditions

Author conditions satisfied by the saved proof text: actual complete source
extent read; every basic/limiting definition needed for Lemma 2 supplied or
linked to its accepted interface; both temporal directions constructed;
all crossing/endpoint/empty-gap cases proved; additional current-point
comparison supplied and proved; no claimed order-completeness dependency; exact
continuation given.

Independent acceptance must fail or remain unresolved if a source reading,
index translation, formula operation, new-gap argument, free-variable
condition, endpoint case, or scope-preserving correction is found incorrect.
It must also fail if an unproved general predicate-substitution theorem is
used to replace the explicit construction, or if this lemma is credited as
all of III.2. Three fresh reviews, integration, scoped production, correction
provenance admission, and final acceptance remain unresolved. No new
mathematical prerequisite is missing for the lemma proved in these files.

## Read manifest

| Local file | Actual extent read | SHA-256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | Full, 1-168 | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `spec/EDITION-2026-WORK-PACKAGES.md` | Relevant NOW-04 task and cited block/continuation/status matches, including current line 252 | `F49DE88FC33093390FD0CC377E7647019F74FD0529F7DCC07B503E559545160E` |
| `handbook/parts/p09/presentations/n-c-012.tex` | 1-135 for language, structures, S/U and D; input matches at 138 and 149 for integration | `35F9137094A285A4847D351FF868CC206EBF3A6F8F7A75DAC767F0C0AFCE2590` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma1.tex` | Full, 1-202 | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| `handbook/annex/p09/kamp-iii2-lemma1.tex` | Full, 1-212 | `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1` |
| `spec/research/edition-2026-c7-kamp-iii2-lemma1.md` | 1-140, interface/source extent and prior indexing context | `F3254DA85D895833F625D5E5998A1F874917AC4FBB67D89CE4DFDF54B1E217D2` |

The primary PDF's full identity and actual page extents are recorded above.
The new files' hashes are recorded at the start; this note's own final hash
is returned separately. Historical memory was used only to retain the
frozen-source and separate-admission review discipline; all mathematical and
source readings here were checked against the current files and actual scan.
