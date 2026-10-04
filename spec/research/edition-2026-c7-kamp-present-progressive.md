# C7 author handoff: the final Kamp present-progressive argument

Date: 8 September 2026. Assigned author `/root/kamp_lemma7_author`, begun
11:45 UTC. The entire remaining substantive argument is written. Independent
reviews remain deferred under the user's current instruction.

## Files and source boundary

| File | Lines | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p09/presentations/kamp-present-progressive.tex` | 304 | 12784 | `DA5E20704F581948A3B00781A287037678E9741E777A657D729CD550643D280F` |
| `handbook/annex/p09/kamp-present-progressive.tex` | 574 | 20915 | `73766A963DE9025C061FCA23C77E11F30EC5832D9B4128784B3D09896DC7DA2F` |

All three assigned paths were unused at dispatch. Only these two files and
this note were written. Earlier author files and root's concurrent shared
edits were preserved.

Primary: Kamp, *Tense Logic and the Theory of Linear Order*, UCLA dissertation,
1968, `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`. Its SHA256 was rechecked:
`C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.
Institutional locator:
[Stuttgart thesis archive](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).

Personally read all of the final substantive discussion and proof on printed
pp. 112–117, PDF pages 121–126, before writing. Also read the referenced
one-input schema definition, progressive operation and announcement on
printed pp. 18–19, PDF pages 27–28. Verified the actual terminal boundary:
PDF page 127 is the bibliography divider; PDF page 128 is the bibliography,
printed p. 118. No substantive argument follows printed p. 117.

Research/PDF skill instructions were personally reread. Source scans supplied
primary evidence; manuscript content and comparisons used actual LaTeX.
No manuscript render, new tests, independent review or review wait was used.

## Exact formal target and its relation to Com

For **every infinite strict linear order** J = <T,<>, the operation
`PR(A) = {x : there exist a < x < b with [a,b] contained in A}` is not
defined, for all A subset T, by any finite one-input schema generated from
the present atom q0 using only negation, conjunction, strict existential
PAST and strict existential FUTURE. Other finite truth functions are Boolean
abbreviations. No other predicate parameter, named time point, immediate
neighbor, isolation operator, or arbitrary unary-tense alphabet is allowed.

The present atom remains mandatory in the progressive definition. Both
progressive proposals are false at actual first or last time points.
The theorem covers none, either, or both endpoints without density,
discreteness, completeness or countable-cofinality assumptions.

PR is nevertheless a first-order unary tense and has the all-Lin expression
`q0 and S(q0,q0) and U(q0,q0)` in the larger source TL1 language, with strict
witness-first S/U semantics. The result concerns the smaller TL0 P/F basis;
it is not a counterexample to the earlier Com first-order expressiveness
theorem and makes no nonexpressibility claim for the S/U basis.

## Source components retained and proved

| Source extent | Complete new content |
| --- | --- |
| 18–19, 112–113 | Both distinct equality-free proposals; correspondence of the revised proposal with the earlier closed-interval operation; dense equivalence; discrete three-point formula; endpoint behavior; present atom and S/U expression |
| 113–114 | Two-sided increasing markers, even-marker input with the filled central interval, exact progressive image and complete local four-choice induction |
| 114–116 | Increasing and decreasing one-sided families; the two original directional depth recursions; every Boolean/P/F case; full order-reversal argument; exact images and counterinterpretations |
| 117 | Separated increasing/decreasing marker chains and two filled intervals; correct two-depth inequalities; complete window induction and images |
| Entire announced target | A finite version of the source's two-chain construction that proves the theorem on every infinite order, including bounded orders without both infinite sequence orientations |

The source's linguistic suggestion connecting progressive grammar and a dense
conception of time is retained as an informal interpretive remark. The text
does not convert it into an empirical or mathematical claim about speakers.

## Corrections and exact evidence

1. The weak proposal omits predicate requirements at its two strict witnesses.
   On a discrete order it equals `A intersect T_*`, where T_* consists of
   points having both neighbors. It equals simple present on an endpoint-free
   discrete order, but fails at an actual first or last point. For instance
   at 0 in N it is false even when 0 is in A. The body gives the corrected
   P/F expression, retaining the present atom and existence of both sides.

2. An arbitrary chosen countable sequence is not necessarily cofinal in the
   entire order. For example, in the sum of three copies of Z choose all
   markers in the middle copy. The source input then has no past witness
   at a point in the first copy and no future witness at a point in the
   last copy, contrary to the printed global full-set claims. The new
   two-sided invariant is on the convex hull I of the markers. Operand
   values outside I are still included in both modal induction cases.

3. The same issue affects the printed global one-sided tails. In omega +
   omega, choose markers in the first copy. FUTURE(q0) for the source
   alternating input is true throughout the first copy and false in the
   second; it is none of the printed four choices on the global tail.
   The repaired local domains I_+/I_- have the required cofinality by
   definition. The proof explicitly considers witnesses outside those
   domains and checks all time points, not only selected markers.

4. Exact block images require even block indices. On N, for the printed
   family with a_n = n and i = 1, the input contains every integer from
   2 through 6, so its progressive image is {3,4,5}, rather than (3,5)
   intersect N = {4}. The new families state even nonnegative i,j.
   Both source depths are always even, so choosing i and j equal to the
   candidate's respective depths preserves the full nonexpressibility target.

5. Both endpoints do not imply separated infinite increasing and decreasing
   chains. The infinite order omega + 1 has both endpoints and no infinite
   decreasing sequence. The new window lemma retains the source construction
   whenever those infinite chains are given, and also proves it for finite
   separated chains. For a candidate eta choose
   `N = max(d_minus(eta), d_plus(eta)) + 6`, two chains of N+1 points,
   `i = d_minus(eta)`, and `j = d_plus(eta)`. Every infinite order has
   the required finite number of distinct points, which can be sorted.
   The two compared input points are a_(i+3) and a_(i+6). Only the first
   is progressive. No infinite sequence or choice/cofinality premise is
   needed for this final finite selection.

6. The corrected window conditions are `d_minus(eta) <= i` and
   `d_plus(eta) <= j`. These put both filled intervals and the comparison
   points inside the window; the reversed inequalities and unrestricted
   later threshold inclusions printed on p. 117 cannot do so. Every
   past/future step and both exterior-witness cases are proved with the
   corrected bounds.

7. The closing basis label on p. 117 is not used to import isolation
   operators from the earlier S-double-prime basis. The language defined
   on p. 114 and all its induction cases are PAST, FUTURE, NOT and AND.
   The new theorem consistently states that exact permitted basis.

The finite-window proof is a proved completion of the source construction;
it is not represented as the literal unmodified argument on p. 117. All
corrections are in active definitions, formulas, hypotheses and proofs.

## Integration, proof pairs and notation

Root should add the body after the IV.4/IV.5 presentation and before the
next historical source presentation, with the matching final Kamp annex
input. The current `n-c-012.tex` contains no progressive discussion or formula
to replace; the relevant search was repeated after root's integration edits.
The final compared snapshot hash was
`9BEAD1D2370649EB62DF4C2AA1A830C18DF4F6CF57F79301F0F08919DA3C8DA2`.
Its existing strict P/F and S/U meanings are compatible. Bibliography key
`Kamp1968` already exists. No shared route or registry was edited here.

| Result | Reciprocal annex |
| --- | --- |
| `thm:p09-kamp-progressive-definitions` | `annex:p9.kamp.progressive.definitions` |
| `thm:p09-kamp-progressive-two-sided` | `annex:p9.kamp.progressive.two.sided` |
| `thm:p09-kamp-progressive-one-sided` | `annex:p9.kamp.progressive.one.sided` |
| `thm:p09-kamp-progressive-window` | `annex:p9.kamp.progressive.window` |
| `thm:p09-kamp-present-progressive` | `annex:p9.kamp.present.progressive` |

Local notation intake: TL0 and unary P/F at
`def:p09-kamp-progressive-language`; rho_0/rho and PR_0/PR at
`def:p09-kamp-progressive-two-definitions`; T_* and x^-/x^+ at
`thm:p09-kamp-progressive-definitions`; d_-/d_+ at
`def:p09-kamp-progressive-depths`; strictly monotone point markers a_n/b_n
(the source's t_n/t'_n), local convex domains I,I_+,I_-, tails H_m^+/H_m^-,
and filled inputs A,A_i^+,A_i^- at their sequence lemmas; separated input
A_ij and window C_mn at `def:p09-kamp-progressive-window`. H,K,C are explicitly
defined shorthand for the particular tails/window in the statements.
The reversed order J^op and syntax eta* are local to the complete duality
proof in the one-sided annex. The finite bound N is introduced in the
main theorem. No new macros were created.

## Author checks and completion boundary

Read the complete saved body and annex, including all final clarifications.
Existing scanner, cross-reference/proof and bibliography checks reported
zero findings, 17 labels and five reciprocal proof pairs, with no external
theorem references. These are author/structural checks, not independent
acceptance or publication clearance.

No proof obligation in this final substantive argument remains unwritten.
The source continuation is exhausted at printed p. 117; the following pages
are bibliography matter. This closes the assigned final Kamp writing boundary,
while root's integration and the deferred consolidated reviews remain separate.
