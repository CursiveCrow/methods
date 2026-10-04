# Edition 2026 C7: Kamp III.1 normal-form construction

Date: 7 September 2026. Author task:
`/root/p4b_corrected_admission/terminal_selection_check`, reassigned to C7 /
`N-c-012.a` by the root integrator. This is an author reconstruction of the
specified first-order normal-form theorem. Independent source, topic and
publication review remain pending.

## Result and exact scope

The reader presentation and complete annex proof of Kamp's Theorem III.1
and its sentence corollary are written. The construction covers arbitrary
nonempty strict linear orders, arbitrary unary interpretations, every
quantifier-position case, both equality-representative cases, missing
universal positions, and empty rays and gaps. It introduces no density,
endpointlessness or order-completeness hypothesis.

The normal form is still first-order. This work does not reconstruct
Theorem III.2, its Lemmas 1-10, or the further passage to temporal formulas
over `Com`. The original III.2 summary and the later Kamp material were
preserved. No result here extends temporal expressive completeness to all
of `Lin`.

## Primary source and actual reading

The exact held source is Johan Anthony Willem Kamp, *Tense Logic and the
Theory of Linear Order*, UCLA dissertation, 1968, supplied by the author's
[Stuttgart institutional archive](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).
The local file is
`tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`, SHA256
`C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.
That hash was verified in this authoring block.

Read before authoring: the complete `spec/EDITION-2026-CONTRACT.md`; the
actual Kamp section of `handbook/parts/p09/presentations/n-c-012.tex`,
lines 1-361; and the relevant locator and scope passages of
`spec/research/p09-kamp-1968-source-note.md`. The source note supplied
locations; its earlier closure assessments were not used as proof authority.

Actual primary reading in this block:

- Visually read all fourteen source scans for printed pp. 43-56, physical
  PDF pp. 52-65, including the complete definitions and III.1 proof.
- Additionally visually read printed pp. 21-22, physical PDF pp. 30-31,
  for the exact displayed language and interpretation conventions, and
  printed p. 39, physical PDF p. 48, for Chapter III's opening notation.
- Used the adjacent layout text only as an attempted reading aid. Its
  extracted glyphs are malformed; the actual scans controlled all formulas
  and case distinctions. Existing source-page images were inspected. No
  manuscript rendering was performed.

The language definition on printed p. 21 lists the binary order predicate
and unary predicates, without a primitive equality sign. Chapter III's
prefixes nevertheless use displayed equality. The exposition explicitly
represents it over `Lin` by
`x ≐ y := not(x < y) and not(y < x)`, so no new predicate is silently
added. Every substitution is specified to concern free occurrences after
bound-variable renaming.

## Source-to-construction coverage

| Source location, printed pages | Reader reconstruction |
| --- | --- |
| 43-44, conventions and Definitions 4-5 | `Lin` validity/consistency, variable-name order, free-before-bound and outer-before-inner precedence, and capture avoidance. |
| 44-46, Definition 6 and remarks | Complete temporal prefixes; essential representatives; first, last and successive representatives; `l(pi)`; standard prefix as adjacent-chain comparisons plus block equalities. Exhaustiveness and mutual incompatibility are proved by finite ordered partitions. Same-block equality order is fixed explicitly for a deterministic written representative. |
| 47-48, Definition 7 | Literal source `At`, `Bef`, `Aft`, `Bet` and their finite stages, all three guards, existential conjunction and universal disjunction constructors, and unions over stages. |
| 48, Definition 8 and Theorem 1 | Exact source-standard clause/formula shape, all named free variables, nonempty free-variable hypothesis, and the `Lin` equivalence target. |
| 49-50, proof case 1 | Prenex reduction; disjunctive normal form; complete order types; representative substitution in unary literals; empty order/unary parts and inconsistent branches. |
| 50-51, proof cases 2(a)-(b) | Existential distribution; nonessential quantified variable equal to an existing representative; essential quantified variable with a surviving block member; forced witnesses and component endpoint renaming. |
| 51-52, proof case 2(c)(i)-(iii) | Explicit left-ray, right-ray and interior-gap existential cases, with finite-stage membership and preserved witness existence even if every old local conjunct is independent of the quantified variable. |
| 52-53, proof cases 3(a), 3(b), 3(c1), 3(c2) | All universal prefix restrictions and representative substitutions; grouping by residual prefix. |
| 54-55, equations (7)-(10) | Grouping by the full set of `2s+1` positions; finite conjunctive-normal-form conversion; source missing-position `gamma` clauses represented explicitly by false consequents. Missing equality positions and missing strict regions are distinguished. |
| 55-56, equation (11) and its cases | Equality positions; strict regions with all, none, or a mixture of variable-dependent disjuncts; explicit empty-region universal conditions; distribution back to standard form. |
| 56, Definition 9 and Corollary 1 | Standard sentences and a complete structural proof of the Boolean-combination corollary, including vacuous quantifiers and nonempty-domain constant cases. |

## Corrections to specific printed proof steps

### C7-SRC-01: negated equality in the quantifier-free basis

On printed p. 49, the scan's displayed rewrite for a negated equality
uses `y < z and z < y`. This conjunction is false in every strict order
and cannot express unequal points. For the two-point order `0 < 1`, the
assignment `y = 0, z = 1` makes the negated coincidence true and the
printed conjunction false.

The active proof uses the correct disjunction,
`not(y ≐ z) iff (y < z or z < y)`, justified by linearity, and retains
the source's correct companion rewrite of `not(y < z)` into coincidence
or reverse order. The source PDF is preserved unchanged. This is a
correction of that printed proof line, not a different normal-form theorem.

### C7-SRC-02: existential region existence cannot be discarded

At the top of printed p. 52, the explicitly written leftmost-witness case
discards the existential region condition when none of the local
conjuncts contains the quantified variable. Its asserted equivalence then
fails at a first point. For example, with `P(y)` true in a one-point
order, `exists x (x < y and P(y))` is false while `P(y)` is true.
The subsequent rightmost and interior cases are abbreviated as similar;
the reconstruction supplies each separately and preserves its region test.

The corrected transformation is
`exists x (pi and I and D) iff rho and I and exists x (beta and D)`,
where `I` has no free `x`, `D` contains the local conjuncts with free `x`,
and `beta` is respectively `x < y`, `y < x`, or `y < x and x < z`.
If the dependent list is empty, `D` is an explicitly true component. The
remaining existential then still requires the region to contain a point.
The reader examples check a first point, a last point, and the empty gap
between consecutive integers. The same gap has a witness in the rational
order, showing why density must not be assumed implicitly.

The universal proof retains the source's missing-position conditions and
its all/none/mixed dependent-disjunct cases. In the no-dependent-disjunct
case, the result includes `forall x (beta implies false)`; an empty region
is handled by vacuous truth. An absent equality position is false because
the named point itself supplies a realization. No universal position is
silently omitted.

### C7-SRC-03: the stage index in the printed left-ray constructor

Disposition added on 7 September 2026 by `/root/kamp_iii1_topic_review`,
after direct inspection of printed p. 47, physical PDF p. 56, in the held
source with the hash recorded above. In the constituent union for
`Bef_{n+1}(x)`, the scan prints unindexed `Bef(z)`, alongside indexed
`Bet_n(z,x)`. The mirror `Aft` clause and the `Bet` clauses print their
stage indices. The active body supplies `Bef_n(z)` at that occurrence.
This is a source-index regularization, rather than a claim that the
finite-stage inscriptions are identical to the scan.

The staged reading is supported by the stated recursive construction and
by the subsequent induction on `Bef_n` and `Aft_n` at printed pp. 60-61.
It makes each stage depend only on earlier stages. It does not add a new
component constructor or enlarge the unindexed normal-form language.
Even if the p. 47 occurrence is read literally as the eventual union,
every component generated by the active rule is admitted by that source
constructor, since `Bef_n(z)` is contained in `Bef(z)`. The finite-stage
induction for the active construction and its epsilon conversion remains
valid, and its output still belongs to the source's unindexed classes.

The accepted III.1 body and annex are unchanged by this disposition. The
source PDF is unchanged. The independent topic report recorded the same
notation discrepancy while passing the normal-form mathematics; this
paragraph supplies its correction provenance without inserting a repair
instruction into the reader's derivation.

## Literal source grammar and the separate support property

Kamp's `At(x)` is a particular syntactic class: conjunctions of unary
literals, together with `P0(x) or not P0(x)`. A contradictory unary
conjunction supplies falsehood. Order atoms are not members of this literal
unextended class. The principal theorem in the new text therefore retains
the source-standard grammar, including its allowed use of the language's
fixed `P0` for constants.

A separately named starred rendition uses
`top_x := not(x < x)` and `bottom_x := x < x` as distinguished constant
slots, retaining the same variable and introducing no unary predicate.
The annex explicitly proves the quantifier construction in those starred
classes. This supports the separately stated handbook property that the
starred output preserves the input unary-predicate support.

The map `epsilon` then replaces the starred true and false slots by
`P0(x) or not P0(x)` and `P0(x) and not P0(x)`, respectively. The annex
proves by finite-stage induction that this conversion lands in Kamp's
literal component classes, preserves truth under every unary interpretation,
and preserves every free variable. Thus the literal source-standard theorem
is actually obtained; the additional support property is not confused with
the source's syntactic membership condition. The optional support property
belongs to the starred output, and the final source-grammar conversion can
introduce only the semantically inessential `P0` constant encodings.

## Files and root integration seam

New reader file:
`handbook/parts/p09/presentations/kamp-iii1-normal-form.tex`.
It contains the three `hbdefinition` items, the proved theorem and sentence
corollary, the constant-convention bridge and endpoint/gap examples.

New proof file:
`handbook/annex/p09/kamp-iii1-normal-form.tex`.
It contains section `sec:annex-p09-kamp-iii1` and annex item
`annex:p9.kamp.iii1`, linked to `thm:p09-kamp-iii1`.

The only edit to the existing presentation replaces its III.1 summary by an
accurate bridge and inserts, at line 138,
`input{parts/p09/presentations/kamp-iii1-normal-form}` with the TeX command
backslash. The following III.2 summary remains as it was.

The root integrator must add exactly this line to `handbook/annex/p09.tex`:

```tex
\input{annex/p09/kamp-iii1-normal-form}
```

The author did not edit that shared annex driver. No bibliography, symbol
register, other manuscript, code, provenance or admission record was edited.

## Author verification and hashes

The full new reader file, full new annex file, and edited integration
paragraph were read back after writing. The additional single-line
clarification that the representative chain is omitted for `s = 1` was
then checked in the reader definition. The complete proof was checked
against the source case structure above and the explicit finite-order
boundary examples. This is author reasoning and read-back, not an
independent review or a software test.

| Artifact | SHA256 at author handoff |
| --- | --- |
| `handbook/parts/p09/presentations/kamp-iii1-normal-form.tex` | `0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31` |
| `handbook/annex/p09/kamp-iii1-normal-form.tex` | `A46BFF4D11C868E8A865F2F9CC89690FCB4D03A550EB6CCB755B4C067A3B7F8B` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `A12201D510F6FE514BC4300F65A34AAA10B0DE0429979ABD10D8BE8F07AE4E5E` |

The held PDF's hash is stated in the source section above. No tests,
manuscript build, manuscript rendering, generated crosswalk, or formal
admission was performed. The PDF skill guided direct inspection of the
scanned mathematical source; the Research skill guided source tracing and
this durable author note. III.1 and its corollary are complete at the
author-construction scope; root integration and the independent review and
output gates remain due.
