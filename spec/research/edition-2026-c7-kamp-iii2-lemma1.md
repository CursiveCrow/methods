# Edition 2026 C7: Kamp III.2, first supporting lemma

Date: 7 September 2026. Author task: `/root/kamp_iii1_topic_review`,
reassigned by the lead to a bounded C7 / N-c-012 construction.

## Result and status

The complete reader definitions, statement and annex proof of Kamp's first
supporting lemma for Theorem III.2 are written. The exact source result is
**Lemma 1 on printed pp. 69-70**: every member of the basic one-variable
past and future classes `Bp(w)` and `Bf(w)` is expressible over `Lin`.

The construction supplies both temporal directions, all finite stages,
the predicate-word realization argument, the existential endpoint guards,
empty-interval and endpoint cases, free-variable conditions and an explicit
finite translation. No smaller prerequisite remains missing for this lemma.
The construction is ready for root integration and independent review;
this author note does not independently accept its own proof.

The result is about basic finite interval patterns. It does not prove
expressibility of every `Bef` or `Aft` formula and does not complete
Theorem III.2. The next genuine source lemma is Lemma 2, beginning on
printed p. 70, concerning the limiting classes `Lp` and `Lf`.

## Exact primary source and actual reading

Primary source: Johan Anthony Willem Kamp, *Tense Logic and the Theory of
Linear Order*, UCLA dissertation, 1968. The held PDF is
`tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`, supplied through the author's
[Stuttgart archive](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).
Its SHA256 was verified in this block:

`C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.

The main agent read the complete edition contract and the PDF and Research
skill instructions before this block's source and authoring work. The PDF
skill guided direct reading of the scans; the Research skill guided primary
source tracing and this single research note. The assignment's prohibition
on subdelegation controlled the Research skill's background-agent suggestion.

Actual primary reading in this block:

- Printed pp. 39-42, physical PDF pp. 48-51: the first-order temporal image,
  proper predicate substitution, strict first-order `S`/`U`, the map `D`,
  and its semantic relation to the temporal language.
- Every page of printed pp. 57-71, physical PDF pp. 66-80: conventions and
  derived operators, named-variable expressibility, the statement and
  opening reduction for III.2, the basic-pattern classes, their occurrence
  words and sequence satisfaction, the later elementary/limiting classes
  and interval property as context, the complete Lemma 1, and the start of
  Lemma 2 for the continuation boundary.
- Printed p. 64 was additionally inspected at higher source-image
  resolution to resolve the duplicated past-class name on the future
  closure definition line. Its right-hand side uses `Bf_n`; the duplicate
  is the left-hand class name.

Existing source images were used where present. Additional images of
physical pp. 70-83 were rendered into the separate current task workspace;
only pp. 70-80 of that rendered set were actually inspected. The source
PDF was not changed. These were source-page images, not manuscript renders.
No extracted text was used as formula authority.

The earlier independent III.1 topic review supplied directly read context
for the equality-free language, nonempty strict linear orders and the
existing normal form. Its core file hashes were rechecked in this block.
The active host's language, strict temporal argument order and `D` clauses
are at `handbook/parts/p09/presentations/n-c-012.tex:16-131`; those actual
passages had been read in full in that preceding review. The new text uses
their conventions and supplies its own named-variable expressibility
definition.

## Source-to-construction correspondence

| Required source content | New construction |
| --- | --- |
| p. 59 named-variable expression through an alphabetic variant of the image of `D` | Definition `def:p09-kamp-basic-expressibility`; capture-avoiding replacement of the current point is explicit. |
| p. 63 binary `Bp_1 = Bf_1` and their different recursive associations | Definition `def:p09-kamp-basic-classes`; both exact stages and both recursive forms are supplied. |
| pp. 63-64 strict existential abbreviations and unary closures | Both `Bp_n(y)` and `Bf_n(x)` are defined with their endpoint guard. |
| pp. 64-65 occurrence word and sequence satisfaction | Definition `def:p09-kamp-basic-word`, using `sigma` for the source's `S(phi)` to distinguish the occurrence word from the temporal operator. |
| pp. 65-66 existence of both syntactic forms, same-word equivalence and relation to first-order satisfaction | Annex proves word construction and both directions of the realization equivalence by simultaneous stage induction, including unordered endpoint assignments for same-word equivalence. |
| pp. 69-70 Lemma 1 and the finite reordering into expressible two-endpoint links | Explicit temporal recurrences `L_i` and `R_i`, with complete past and future semantic inductions and the matching `D` expansions. |

The source uses an auxiliary starred `Bp` presentation and proper predicate
substitution to organize its past proof; it abbreviates the future proof.
The reconstruction writes the same finite-chain rearrangement explicitly
and gives direct nested `S` and `U` formulas. It does not claim that its
`L_i`/`R_i` notation is Kamp's literal auxiliary notation. No auxiliary
predicate letters or unproved general substitution result are needed for
this explicit construction. The source's intermediate occurrence-word and
realization claims are proved rather than assumed.

The III.1 starred component classes are unrelated to the source's starred
auxiliary `Bp` construction. The new text introduces no additional starred
class and leaves the accepted III.1 presentation untouched.

## Mathematical checks performed by the author

1. **Exact scope of the binary grammar.** The binary base has no `x < y`
   conjunct. Its first-order formula can hold at coincident or reversed
   endpoint assignments. The chain characterization is first proved under
   ordered endpoints. The unary existential closures supply that strict
   order, so their translation is exact. At later binary stages an interior
   witness forces endpoint order. This also proves the full same-word
   equivalence asserted by the source.
2. **Both recursive associations.** A past constructor prepends one point
   and one interval to its constituent chain; a future constructor appends
   one interval and one point. The reverse directions choose the second
   and penultimate points respectively. Each step preserves every interval
   predicate and each endpoint predicate.
3. **Temporal argument order.** For the past word recurrence,
   `L_i = A_i and S(L_{i-1}, B_i)`, the first argument holds at the earlier
   witness and the second holds on its open interval to the current point.
   For the future recurrence,
   `R_i = A_i and U(R_{i+1}, B_{i+1})`, the first argument holds at the
   later witness. The recurrences follow the source convention already
   fixed by the host, not the later non-strict LTL convention.
4. **Empty intervals and absent witnesses.** At stage one, consecutive
   endpoints need no interval point, so the interval predicate is vacuous.
   A first point has no past closure witness, and a last point has no
   future closure witness. At stage two, even an everywhere-true predicate
   interpretation cannot supply the required three increasing points in a
   two-point order. Both displayed temporal formulas have the same failure.
5. **Stages and variables.** Stage `n` has `2n+1` predicate occurrences and
   `n+1` chain points. The stage index starts at one. The one-letter seeds
   for the temporal recurrences do not create a source stage zero.
   Binary formulas have exactly two free endpoints; guarded closures and
   renamed `D` outputs have exactly one. All inner bound variables are
   fresh. Repeated predicate symbols remain repeated occurrences in the
   word; no distinctness or independence of their interpretations is used.
6. **Finite construction.** Reading the occurrence word and following the
   two finite recurrences gives actual temporal formulas. The proof checks
   their `D` expansions directly; it does not assert a generic algorithmic
   result based merely on semantic equivalence. It introduces no new unary
   predicate and no order completeness assumption.

These are author reasoning and read-back checks. No software tests, static
checker, manuscript build, manuscript rendering or admission was performed.

## Source corrections and notation dispositions

### III.1 p. 47 source-index disposition

The separately owned existing note
`spec/research/edition-2026-c7-kamp-iii1.md` now contains `C7-SRC-03`.
It records that the p. 47 left-ray constructor prints unindexed `Bef(z)`
where the active staged reconstruction uses `Bef_n(z)`, gives the stage
induction support from pp. 60-61, and proves why the regularization does
not invalidate output membership in the source's unindexed classes.
This is the only change made to that existing file.

### C7-III2-L1-SRC-01: duplicated past name on the future closure line

On printed p. 64, the second one-variable definition again prints
`Bp_n(y)` on its left, while its right is the strict future closure of
`Bf_n(y,t_i)`. Read literally, that line assigns two incompatible
descriptions to the same class and leaves the intended future class
unnamed. The surrounding binary definitions on p. 63, the `Bp(y)`/`Bf(y)`
satisfaction remark on p. 66, and Lemma 1's union on p. 69 determine the
intended future name.

The active definition writes `Bf_n(x)` for that future closure, with the
endpoint renamed consistently. For a two-point order with all predicate
letters true, a one-piece future closure holds at the first point while
the corresponding past closure does not; the two names cannot simply be
identified. No binary constructor or strict guard is changed. The source
PDF remains unchanged.

### Symmetric proof and index conventions

The first proof paragraph on p. 69 repeats `Bp` while announcing the
same-way companion to the past argument. The lemma's stated `Bp`/`Bf`
union identifies the required companion; the active proof gives the future
case completely. The realization definition on p. 65 indexes a word with
`2n-1` occurrences by `n` points, whereas p. 64 indexes stage `n` by
`2n+1` occurrences. The new text consistently uses the stage index: `n`
intervals and `n+1` points. This is an explicit change of indexing, with
no additional or missing endpoint.

## Root integration and shared intakes

New body file:
`handbook/parts/p09/presentations/kamp-iii2-lemma1.tex`.

Suggested host seam: in `handbook/parts/p09/presentations/n-c-012.tex`,
after the existing III.2 overview ending with its pp. 48-94 citation
(currently line 147), before the paragraph beginning `Consequently
Chapter II Theorem 1`. Insert:

```tex
\input{parts/p09/presentations/kamp-iii2-lemma1}
```

New proof file:
`handbook/annex/p09/kamp-iii2-lemma1.tex`.

Suggested annex seam: immediately after the existing III.1 input in
`handbook/annex/p09.tex`, insert:

```tex
\input{annex/p09/kamp-iii2-lemma1}
```

The author did not edit either shared driver, the host, bibliography,
symbols, prior review records, or the accepted III.1 body/annex.

Bibliography intake: no new key; `Kamp1968` is already present in
`handbook/bib/handbook.bib:2269`. New precise citations concern
printed pp. 59-70, especially definitions pp. 63-66 and Lemma 1 pp. 69-70.

Notation intake for the root: parameterized binary and unary classes
`Bp_n`, `Bf_n`, their unindexed unions; occurrence word `sigma(phi)`
(source `S(phi)`); predicate-to-proposition correspondence `R-hat`;
local temporal recurrence names `L_i`, `R_i`; realization of a finite
predicate word. These are source classes and local construction notation,
distinct from `Bef/Aft/Bet` and the III.1 starred classes.

New anchors:

- `def:p09-kamp-basic-expressibility`
- `def:p09-kamp-basic-classes`
- `def:p09-kamp-basic-word`
- `thm:p09-kamp-iii2-lemma1`
- `sec:annex-p09-kamp-iii2-lemma1`
- `annex:p9.kamp.iii2.lemma1`

## File identities and continuation

| Written artifact | SHA256 at handoff |
| --- | --- |
| `handbook/parts/p09/presentations/kamp-iii2-lemma1.tex` | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| `handbook/annex/p09/kamp-iii2-lemma1.tex` | `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1` |
| `spec/research/edition-2026-c7-kamp-iii1.md` | `E7EDB297952B265B3EDD954868A0D9F3D73745811B9964B1455045D1D6D3154B` |

Preserved dependencies: III.1 body
`0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31`,
III.1 annex
`A46BFF4D11C868E8A865F2F9CC89690FCB4D03A550EB6CCB755B4C067A3B7F8B`,
and active `n-c-012.tex`
`A12201D510F6FE514BC4300F65A34AAA10B0DE0429979ABD10D8BE8F07AE4E5E`.

Next content dispatch: read and reconstruct the complete actual Lemma 2
starting at printed p. 70, using its `Lp_0/Lf_0` and higher-stage
definitions on pp. 66-67, the derived-operator conventions on pp. 57-59,
and this lemma's finite-pattern realization results. Continue the source
reading until the actual end of Lemma 2 before fixing its scope. This
block read only the start on pp. 70-71 and does not claim that lemma's
proof complete. Lemmas 2-10 and the concluding III.2 reduction remain
separate work.
