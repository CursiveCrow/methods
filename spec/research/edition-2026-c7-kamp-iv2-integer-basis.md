# C7 author handoff: dense-order observation and Kamp IV.2

Date: 8 September 2026. Author assignment `/root/kamp_lemma7_author`, begun
10:54 UTC. Both assigned mathematical constructions are fully written.
Independent reviews remain deferred under the user's current workflow.

## Files and source extent

| File | Lines | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p09/presentations/kamp-iv2-integer-basis.tex` | 285 | 12559 | `D3F6D3378B7B1EE6438E98C65B7C983E8F66A6A4FE1FA008EDB1E73AA2514310` |
| `handbook/annex/p09/kamp-iv2-integer-basis.tex` | 539 | 24193 | `CCF320684F686ABC4C6EDDF802C91A8BAF4089955B1C6D154C495969B67A6717` |

All three owned paths were unused at the start. Only these two new files and
this note were written; shared files and earlier author files were preserved.

Primary: Kamp, *Tense Logic and the Theory of Linear Order*, UCLA dissertation,
1968. Held PDF: `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`, SHA256
`C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.
Institutional locator:
[Stuttgart thesis archive](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).

Personally read the exact dense-order observation across printed pp. 99–100,
Definition 2 on p. 100, every formula and proof paragraph of Theorem IV.2 on
pp. 100–105, and the transition into Theorem IV.3 on p. 105. Physical page
equals printed page plus nine. Higher-resolution source crops of p. 101
verified the actual P/F glyphs in the displayed markers and target formulas;
the errors below are present in the held scan. The full assigned extent was
read before writing. The IV.2 Q.E.D. occurs near the top of p. 105.

Research and PDF skill instructions were personally reread. Their use supplied
primary-source reading and this source note. Actual manuscript LaTeX was read
for content. No manuscript PDF was built or rendered; no new tests or
independent reviews were launched.

## Complete content supplied

The dense-order theorem retains exactly a particular dense strict linear
order with more than one element, with arbitrary unary tenses first-order
definable on that order. Neither completeness, absence of endpoints,
countability nor an automorphism of the whole order is assumed. The source
states this extension without supplying its detailed argument. The new
proof constructs a two-sided marker sequence inside a convex interval and
uses finite partial order/predicate maps with both extension directions.
Selected points outside the interval map to themselves. The proof therefore
handles arbitrary operand interpretations outside the interval and formulas
whose quantifiers range over the whole order. A direct first-order induction
establishes local four-choice closure. The generated eight-set field and the
two separating marker gaps then prove both S and U nonexpressibility. The
one-point exclusion is verified separately by a constant-false two-input
formula.

The integer treatment includes all four equality-free source definitions,
the exact six-operation basis, every unary integer clause and converse, all
three marker disjuncts, both outer guard conjuncts, and both final expressions.
The marker proof covers successful first exit, failed first exit, no exit,
and the source's separate no-witness alternative. A direction parameter proves
both orientations at arbitrary integer t; its conversion to every actual
P1/F1/S1/U1 neighbor and intervening interval is explicit. The outer proof
exhausts one-step success, failure at the first point, two-step success,
failure at the second point, and the longer-search case. Empty/full predicate
sets, unbounded tails, values at the current point and witness, and vacuous
adjacent intervals are all checked.

## Corrections applied directly to the new formulas

1. On printed p. 101, the source's displayed eta_1 looks forward: its first
   disjunct is `q0 and F1 not q0 and F1 q1`, its failure condition inspects
   one and two future points, and its last disjunct shifts that condition
   with P1. However zeta_1 uses `U1 eta_1`, while the successful-endpoint
   argument on p. 103 requires the marker to inspect preceding points.
   The corrected eta_1 is the printed eta_2, and corrected eta_2 is the
   printed eta_1. This preserves all three disjuncts while correcting their
   orientation for the respective future and past searches.

   Concrete failure of the displayed source zeta_1: at t = 0 let
   `A = {i in Z : i >= 3}` and `B = Z`. Strict U(A,B) is true. The printed
   forward-looking eta_1 is empty: its first disjunct would require an end
   of the upward-closed A-tail, and its other disjuncts require not B.
   Both short-witness disjuncts at 0 are false, while the isolation disjunct
   sees no marker. Thus the printed zeta_1 is false. In the corrected
   construction eta_1 holds exactly at 3 and its far neighbor is false.

2. The second conjunct of printed zeta_2 contains `F1 P1 q0` in its short
   second-witness disjunct and `P1 F1 (not q0 and q1)` in its long-search
   disjunct. These are mixed shifts, which evaluate the current point on Z.
   Both are replaced directly by two past shifts: `P1 P1 q0` and
   `P1 P1 (not q0 and q1)`. The guard and all disjuncts remain present.

   Concrete false positive from the first mixed shift: at t = 0 let
   `A = {0}` and `B = {-1,-2}`. The source past guard is true, and its
   short disjunct is true because `P1 q1` is true and `F1 P1 q0` reads A
   at the current point. But strict S(A,B) is false because there is no
   past A-point. The corrected zeta_2 is false. The second mixed shift also
   introduces an impermissible current-point requirement in the long branch;
   its corrected two-step position is explicitly proved in equation (6).

The displayed source proof on p. 103 also uses F1 while verbally evaluating
the predecessor. The new derivation consistently uses the correct shift
semantics. Historical readings and the exact counterexamples remain here;
the reader receives corrected formulas and complete proofs.

## Existing manuscript comparison and integration

Read the actual current unary definitions in
`handbook/parts/p09/presentations/n-c-012.tex`, around lines 188–249, and
the adjacent-result summary around lines 364–376. Snapshot SHA256:
`2734611F8F77D62408E3902B17E97B3077298F09840BE3EE905313A483705FBF`.

No existing eta_1/eta_2/zeta_1/zeta_2 construction occurs there. The four
integer clauses under the paragraph beginning `The literal Chapter IV
Theorem 3` are compatible: PAST1 reads i-1, FUTURE1 reads i+1, ISOLP checks
the nearest past occurrence and j-1, ISOLF checks the nearest future
occurrence and j+1. The nearby explanatory sentence says these operations
are used by IV.2–IV.4, which remains correct. No existing mathematical
formula in that compared scope requires replacement for this correction.

Root should input the new body after the IV.1 presentation and before the
IV.3 development, and input the new annex after IV.1. The sentence near
line 369, `Theorem IV.2 positively expresses S,U on the integers from a
basis which includes the two isolation tenses`, is correct and should link
to `thm:p09-kamp-iv2`. The exact six-operation basis is provided in
`def:p09-kamp-iv2-basis`. The dense-order observation has its own result
identity and should remain distinct from the integer theorem. Bibliography
key `Kamp1968` already exists.

## Result/proof and notation intake

| Result | Reciprocal annex |
| --- | --- |
| `thm:p09-kamp-dense-local-unary` | `annex:p9.kamp.dense.local.unary` |
| `thm:p09-kamp-dense-unary-separation` | `annex:p9.kamp.dense.unary.separation` |
| `thm:p09-kamp-iv2-unary-semantics` | `annex:p9.kamp.iv2.unary.semantics` |
| `thm:p09-kamp-iv2-marker-lemma` | `annex:p9.kamp.iv2.marker.lemma` |
| `thm:p09-kamp-iv2` | `annex:p9.kamp.iv2` |

Local notation to merge through root's existing registry process:

| Definition or proof scope | Typed symbols |
| --- | --- |
| `def:p09-kamp-dense-local-language` | J = fixed order; TM_J = its full unary sentential language; I = convex interval; d_n = two-sided markers |
| Dense local proof | D = marker set; h = integer index translation; u,v = compared points |
| Dense theorem proof | E,H = even/odd-indexed markers; B_I = field relative to I |
| `def:p09-kamp-iv2-basis` | In = integer order; bot_P0(z) = contradictory source formula; pi_-/pi_+, iota_-/iota_+ = four defining formulas; S = six-operation basis; TS = its sentential language |
| Same basis definition | P1/F1 = unary neighbor symbols; S1/U1 = unary isolation symbols, with different arity and role from binary S/U and first-order predicate P1 |
| `def:p09-kamp-iv2-marker-formulas` | C = continuation formula; B_P/B_F = failure formulas; eta_1/eta_2 = corrected markers; delta = direction; N_delta/J_delta = directional shift/isolation; eta_delta = stated directional abbreviation |
| `def:p09-kamp-iv2-target-formulas` | G_F/G_P = source guards; zeta_1/zeta_2 = corrected two-input target formulas |
| Integer annex | a_m,b_m,c_m,r_m,k_m,e_m = Boolean values at directed integer offsets; g and ell = Boolean values of the two outer conjuncts |

No new macros or shared registry/bibliography changes were made.

## Author verification and next source boundary

Read both complete saved LaTeX files and checked the stated derivations,
including the final explicit language mapping. Existing `tools/check.py`
scanner, cross-reference/proof checks and bibliography check on this pair
reported zero findings, 17 labels, five reciprocal proof pairs, and no
external theorem references. These are author and structural checks, not
independent mathematical/source/publication acceptance.

No proof obligation in the assigned dense-order observation or IV.2 remains
unwritten. The next source theorem is IV.3 beginning on p. 105, whose current
separation treatment already exists in n-c-012.tex. IV.4 is the next separate
adjacent source result beyond that existing treatment; its full source proof
was not read or written in this block. Review and admission remain deferred.
