# Edition 2026 C7: final Kamp III.2 writing

Date: 8 September 2026. Author: /root/kamp_lemma7_author.
Repository: C:\Dev\the-methods-of-reason. Requirement: C7 / N-c-012.
Block: 08:46 UTC to the 09:31 UTC deadline.
Standing: the assigned Lemma 9, Lemma 10 and concluding Theorem III.2
authoring chain is complete. Consolidated reviews are deferred under the
user's new write-all-changes-first workflow; none was launched here.

## New files and identities

All seven assigned paths were checked absent before writing. Only the six
new manuscript files below and this handoff were edited.

| Artifact under handbook/ | Lines / bytes | SHA256 |
| --- | --- | --- |
| parts/p09/presentations/kamp-iii2-lemma9.tex | 86 / 4,372 | 8E9021B483BE6DE75B8B58AAB216B370D6ACF5A3883B46B474B3EFC6856FED5A |
| annex/p09/kamp-iii2-lemma9.tex | 95 / 4,885 | 6E79F17BAC3DD5001DAF6EFADF9CFA2DAE41CCAB0CB80B9B6FAC72DF8A271CA2 |
| parts/p09/presentations/kamp-iii2-lemma10.tex | 85 / 4,303 | BAE0AC014FA0554BF9E1C8C07296F68E113E5AF5DB99772121D53C7E45E48337 |
| annex/p09/kamp-iii2-lemma10.tex | 176 / 8,855 | 608460B03D8D4FE7AC8AF4E82E7DE0D0FCA3427D7E9E8DC09D54BE00641C170D |
| parts/p09/presentations/kamp-iii2-completion.tex | 187 / 9,491 | 3B9955A076F3116157212A4B492E7F193C5AA815683B4899BBDC0727472C0470 |
| annex/p09/kamp-iii2-completion.tex | 329 / 17,490 | F8D99C95A5620C6C8728D8C13B5C850A384D24EE2AE1BE0F6CB75C3616BDC407 |

## Source extent and actual reading

Primary: Kamp, *Tense Logic and the Theory of Linear Order*, UCLA, 1968;
existing key Kamp1968. Held PDF: tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf.
[Institutional source](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).
Verified unchanged SHA256:
C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA.
Physical page = printed page + 9, counted from one.

Before writing each construction, its full required source extent was read:
Lemma 9 occupies printed pp. 92-93, Lemma 10 p. 93, and the concluding
theorem proof pp. 93-94. The initial Theorem III.2 statement and reduction
through the primitive regional class occupy pp. 60-62 and were also read
completely before the conclusion was authored. Complete pp. 56-59 were
read for the standard-form corollary, derived operations and exact
expressibility convention. Complete pp. 95-97 were inspected only to
identify the subsequent Chapter IV boundary; no Chapter IV result is
counted as authored by this block.

The final pages were read from the held complete page images associated
with the verified source. Fresh complete images for printed pp. 56-62
are under the old task workspace's tmp/pdfs/kamp-iii2-final-source/.
The exact source construction ends on printed p. 94; Chapter IV begins
on p. 95. No manuscript PDF was rendered.

The actual source-class definitions, standard-form theorem, elementary
histories and closure interfaces were read from their current LaTeX.
The complete normal-form support/constant conversion proof was also read.
Research and PDF skill instructions were reread completely. Source reading
and checking the author's derivations were treated as authoring, with no
new independent review or subagent.

## Complete result/proof pairs

| Body result | Reciprocal annex | Supplied work |
| --- | --- | --- |
| thm:p09-kamp-iii2-lemma9 | annex:p9.kamp.iii2.lemma9 | All three finite families; guarded use of I representations; fresh basic skeletons; every elementary label restored by proper substitution; empty cases. |
| thm:p09-kamp-iii2-lemma10 | annex:p9.kamp.iii2.lemma10 | Bet stage zero and one, retention, existential and universal steps, endpoint At insertion and finite conjunction. |
| thm:p09-kamp-interval-boolean-normalization | annex:p9.kamp.interval.boolean.normalization | Negated At and Bet components; both guarded quantifier duals; CNF/DNF; fixed endpoint factors; strict witness and empty-region cases. |
| thm:p09-kamp-one-sided-closure | annex:p9.kamp.one.sided.closure | Past Ep closure and future closure through the actual same-word Ef presentation, with all disjuncts. |
| thm:p09-kamp-primitive-regions | annex:p9.kamp.primitive.regions | Existential past/future envelopes and universal primitive past/future components, including every normalized alternative. |
| thm:p09-kamp-regional-elementary | annex:p9.kamp.regional.elementary | Maximal proper regional occurrences, strict subtree recursion, fresh skeletons and restoration under the exact Com substitution semantics. |
| thm:p09-kamp-iii2 | annex:p9.kamp.iii2 | Full one-variable standard form to E-history to TL_1 construction; literal D-image output, uniform Com equivalence and positive-arity support. |

The final theorem is exactly the one-variable conclusion: for each L-formula
phi(w) with one free variable, the procedure constructs eta in TL_1 such
that Com entails phi(w) iff D(eta)[w/t_0]. At w=t_0 the output is a literal
member of the source image class C. No intermediate arbitrary E formula is
misidentified as a literal D-image member. The original strict S/U operand
order, all complete-order hypotheses, and arbitrary unary interpretations
are retained. Temporary predicate letters are all eliminated; only the
source's P_0 constant convention can add an inessential letter to an input
that did not already use it.

## Clarifications required for source fidelity

The final source paragraph concerns the primitive class D after the
preliminary reduction on pp. 60-62. It is not valid to assume directly
that every arbitrary Bef/Aft formula has only an existential root and
no nested regional component. The new text supplies the maximal-proper-
occurrence substitution reduction and both primitive quantifier cases.

The source's negation/distribution step on p. 62 is implemented with the
actual finite disjunctive output retained. No claim that D is closed under
disjunction, or that a finite disjunction is a single primitive formula,
is introduced. The worked example of a universal past condition produces
the two alternatives exists past Q and exists past R and verifies their
temporal expression, including first-point vacuity.

Future closure of an Ep formula is not declared an E seed directly.
Each word is first given its same-word Ef presentation; the actual
elementary future-closure history is then used. Recursive regional
equivalences are only over Com, and the proof reinterprets the fresh
unary letters in a complete structure before using substitution. It
does not invoke the Lin-only form of a substitution lemma with weaker
unverified premises.

No previous Lemma 8 correction was changed. The existing completion pair
remains 22D58367E4A6C31471D59825476ECA6BB18EACDC1D5DAA8210E1619565D1C9DD
and 544E30F8E028D5C19BF1505CF9C839EAF9512014A1C41EC08B364BB25438EC05.
The frozen original remains
0509750C13B88A4E18914BD52BDE171C725CBA14221CBFC2227D7693A2B421CC.

## Root integration and remaining boundary

Input the new bodies after kamp-iii2-lemma8-completion.tex, in order
lemma9, lemma10, completion, in handbook/parts/p09/presentations/n-c-012.tex.
Input their matching annexes in the same order in handbook/annex/p09.tex.
All bibliography references use existing Kamp1968.

Notation intake, local P9.4: the three finite families chi/Phi/Psi and
their aggregate universal U; fresh skeleton letters and per-occurrence
labels; positive interval Boolean expressions and their endpoint/local
factors; primitive regional class mathcal D(w) and existential envelopes;
maximal proper occurrences phi_i(y_i), fresh Q_i and elementary outputs
xi_i/xi'; the D-image class mathcal C and final Xi(w), eta and D(eta);
the worked example's unary Q,R, corresponding q,r and tautology tau.

All six new LaTeX files were read back completely; later small wording and
display changes were checked. The existing scanner reports zero findings,
seven reciprocal proof pairs, 31 labels and valid bibliography keys. No
test, build, manuscript render, generator, commit or independent review was
performed. This record is an authoring handoff for later consolidated review.

No step remains unwritten in the assigned Lemma 9--Lemma 10--Theorem III.2
chain. The next source chapter begins on printed p. 95. The separate
Chapter II Theorem 2 primitive-recursive strengthening is not established
merely by this effective termination proof and retains its separate proof
obligation; the new theorem does not claim a primitive-recursive bound.
Shared-route integration, notation integration and the user's consolidated
content/publication checks remain root work after the full writing phase.
