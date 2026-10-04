# C7 author handoff: Kamp IV.4 and IV.5

Date: 8 September 2026. Assigned author `/root/kamp_lemma7_author`, begun
11:18 UTC. Both assigned separations and every proof component below are
written. Independent reviews remain deferred under the current user workflow.

## Files and exact source

| File | Lines | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p09/presentations/kamp-iv4-iv5-separations.tex` | 248 | 10712 | `09688C0DF98F003D763BF6CE437F93F7A133654AE1EDA8E06A9A12CEC8E5BAD1` |
| `handbook/annex/p09/kamp-iv4-iv5-separations.tex` | 421 | 18198 | `A799AC81FBE5EF0F39EF7D562B886EEB94408958C8F10334E8DA651C3713F182` |

The three owned paths were unused at dispatch. Only these two files and this
note were written. Earlier author files and all shared files were preserved.

Primary: Kamp, *Tense Logic and the Theory of Linear Order*, UCLA dissertation,
1968, `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`. SHA256 rechecked during
this block: `C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.
Institutional locator:
[Stuttgart thesis archive](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).

Personally read the complete Theorem IV.4 statement, eight-set list and
operation calculations on printed pp. 108–109; the complete IV.5 statement,
two interpretations, distinguishing-formula display, and induction through
its Q.E.D. on pp. 109–112. Physical page equals printed page plus nine.
The preceding III.3 tail on p. 107 and the next progressive-tense transition
on pp. 112–113 were also read for boundaries. A higher-resolution source
crop verified the reversed band endpoints and literal repeated endpoint in
the p. 110 formula. All assigned source content was read before authoring.

Research/PDF instructions were personally reread. The source scans supplied
primary evidence; manuscript content and dependencies were read as actual
LaTeX. No manuscript rendering, new tests, independent reviews or review
waits were performed.

## Source corrections and their mathematical evidence

### IV.4: the eight-set family

Printed row (vi) on p. 108 repeats the odd integers, already listed as row
(viii). The missing set is the complement of residue zero **modulo four**.
The printed list with the duplicate is not closed under complement: row
(v) is residue zero modulo four, but its complement is absent. The following
operation table on p. 109 confirms the intended missing set, because both
isolation operators on that complement give residue two modulo four.

The new family directly uses
`Z, empty, R2, complement(R2), R0, complement(R0), even, odd`, where
`Rr = {4k+r : k in Z}`. Its three atoms are R0, R2 and the odd integers.
Every one of the 32 unary table entries is proved, including both isolation
directions for the complemented residue classes. The full formula induction
then gives the two original nonexpressibility conclusions. Additional
occurring proposition letters may be used only when their interpretations
already belong to the field; the target one-input case uses q0 alone.

### IV.5: ordered bands and a genuinely distinguishing formula

The inserted intervals on printed p. 110 list
`sqrt(2)+1/(2j+1)` before `sqrt(2)+1/(2j+2)`. The first number is larger.
With ordinary ordered open-interval semantics these are empty. The new
definition directly writes the intended nonempty bands with the smaller
endpoint first: `(b_(2j+2), b_(2j+1)) intersect Q`, where
`b_n = sqrt(2)+1/n`. All union indices and their restrictions are explicit.
The same periodic input and the same altered band from the source are kept.

The printed distinguishing formula has the contradictory interval guard
`t3 < t4 < t3` in its final universal clause. Replacing the last t3 by t2
does not rescue the claimed distinction: both intended interpretations are
locally constant at every rational point, so that corrected formula still
holds at 3 in both models. Indeed choose its initial P-witness t1 = 2.
Every P-point between 2 and 3 has a right-hand all-P interval ending before
3. Every non-P point there has a left-hand all-non-P interval beginning
after 2. The literal final universal is already vacuous; its natural
single-index repair merely asks for the latter local property. Thus neither
version distinguishes the intended models. This is more than an interval
endpoint typo.

The active new definition replaces that failed separator directly by
`phi(t0) = not beta(t0)`, with beta saying:

- there is a non-P point y before the current point;
- there is a P-point between y and the current point;
- before every such P-point z there are y < p < q < z with P(p) and not P(q).

The complete equality-free formula in the body uses only `<,P0` and has
only t0 free. The nonvacuity existential is retained. The first-order formula
contains no real cut, real constant, or named rational parameter. Current
point three is specified by a semantic assignment `t0 -> 3`.

In periodic Q, every non-P starting point has a first subsequent P-band.
If any P-point occurs before the current point, a rational point z in that
first band defeats beta's universal clause. Thus beta is false everywhere
in that interpretation. In Q', at current point 3 choose y = 1. Every P-point
z in (1,3) lies above sqrt(2), and a sufficiently large j gives
`b_(2j) < z`. Choose rational p in the true band
`(b_(2j+2),b_(2j+1))` and rational q in the false band
`(b_(2j+1),b_(2j))`. They satisfy every required inequality and predicate
condition. The point 2 supplies nonvacuity. Hence beta is true at 3 in Q',
and phi has the source's claimed orientation: true in Q and false in Q'.

This is an explicit repair of the source's existential theorem and intended
two-interpretation construction, not an attribution of the new formula to
the literal p. 110 display. The time domain, input arity, two interpretations,
current point and strict S/U separation target are preserved. Every source
temporal comparison assertion is supplied; no weaker target replaces IV.5.

## Full inductions and boundary cases

IV.4 includes atomic, negation, conjunction, both isolation operators and
ordinary strict past/future. Empty/full sets, every residue/parity choice,
strict nearest occurrences and empty intervening integer intervals are proved.
Immediate past maps R2 to R3; immediate future maps R2 to R1; both split the
odd atom which the permitted basis cannot split.

IV.5 proves local constancy at every rational point, including arbitrarily
near the missing cut, and unboundedness of both colors in both directions.
Every endpoint and the cut itself are irrational and cannot be a time or
witness. The table gives all 16 input pairs for each of S and U, with witness
operand indexing rows and interval operand columns. Its proof uses neighborhoods
at the current point and at an opposed witness, with both past/future choices.
The four corresponding truth-set pairs are closed under atom, negation,
conjunction, S and U. This yields both within-model comparisons and the
cross-model comparison, and hence equality of every unary temporal formula
at 3. The corrected first-order values contradict any candidate definition.

## Required root integration

Input the new body after the existing IV.3 presentation and add its annex
after the preceding Kamp Chapter IV annex inputs. Existing bibliography key
`Kamp1968` is sufficient. No shared files were edited by this author.

The current `n-c-012.tex` paragraph headed `Why the order hypothesis cannot
be deleted`, around lines 178–186 in the read snapshot, incorrectly says
that the displayed first-order tense distinguishes the two models. Replace
that paragraph directly with wording such as:

```latex
\paragraph{Why the order hypothesis cannot be deleted.}
\Cref{thm:p09-kamp-iv5} supplies the rational-order obstruction using
the periodic and accumulating interpretations of
\cref{def:p09-kamp-rational-cut-models}.
The corrected first-order formula of
\cref{def:p09-kamp-rational-distinguishing-formula} distinguishes them
at the rational current point three, whereas
\cref{thm:p09-kamp-iv5-temporal-induction} proves agreement there
for every one-input formula built from negation, conjunction and
the source's strict SINCE and UNTIL.
Thus the complete-order basis does not extend unchanged to all
linear orders \cite[ch.~IV, pp.~109--112]{Kamp1968}.
```

The later `Adjacent separations and proof status` paragraph, near lines
370–374, has a correct IV.4 summary; connect it to `thm:p09-kamp-iv4`.
Its IV.5 sentence should link to `thm:p09-kamp-iv5` and the corrected
construction rather than leave the printed formula's claim in place.
No full modulo-four or rational formula construction already appears in
that compared n-c-012 scope, so the new files fill those proof boundaries.
The snapshot read before integration had SHA256
`2734611F8F77D62408E3902B17E97B3077298F09840BE3EE905313A483705FBF`.

## Result and notation intake

| Result | Reciprocal annex |
| --- | --- |
| `thm:p09-kamp-iv4-field` | `annex:p9.kamp.iv4.field` |
| `thm:p09-kamp-iv4` | `annex:p9.kamp.iv4` |
| `thm:p09-kamp-rational-local-table` | `annex:p9.kamp.rational.local.table` |
| `thm:p09-kamp-iv5-temporal-induction` | `annex:p9.kamp.iv5.temporal.induction` |
| `thm:p09-kamp-iv5` | `annex:p9.kamp.iv5` |

The single external theorem reference is
`thm:p09-kamp-iv2-unary-semantics`. Its unchanged source pair was reread
in the preceding block and its hashes rechecked here: body
`D3F6D3378B7B1EE6438E98C65B7C983E8F66A6A4FE1FA008EDB1E73AA2514310`;
annex `CCF320684F686ABC4C6EDDF802C91A8BAF4089955B1C6D154C495969B67A6717`.

New local typed symbols: S-double-prime = specified integer operation basis;
R_r = residue class modulo four; V/W = even/odd integers; B_4 = eight-set
field, all first defined in `def:p09-kamp-iv4-basis` and
`thm:p09-kamp-iv4-field`. In the rational subsection, Ra = rational order,
`(a,b)_Q` = rational points between real endpoints, alpha = sqrt(2), b_n =
reciprocal endpoints, Q/Q' = the two unary propositions, and M/M' = their
one-predicate structures, first defined in `def:p09-kamp-rational-cut-models`.
Beta is the accumulating-obstruction formula and phi its negation, first
defined in `def:p09-kamp-rational-distinguishing-formula`. Complement changes
its explicitly declared domain from Z to Q between the two subsections.
No new macros or shared registry changes were made.

## Author checks and next boundary

Both complete saved LaTeX files were read. Existing scanner/bibliography checks
reported 16 owned labels and five owned reciprocal proof pairs. Joined
cross-reference/proof checks with the verified IV.2 dependency pair reported
zero findings, 33 labels and ten pairs. These are structural and author
checks, not independent acceptance. No assigned IV.4 or IV.5 proof step remains
unwritten.

IV.5 ends at its Q.E.D. on printed p. 112. The chapter then continues with a
separate present-progressive nonexpressibility construction beginning on
p. 112 and discussing alternative definitions on p. 113. Only that transition
was read here; its full continuation remains the next source boundary.
Completing IV.4/IV.5 does not claim that the entire Chapter IV tail is written.
