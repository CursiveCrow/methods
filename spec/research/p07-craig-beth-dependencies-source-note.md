# Craig/Beth dependencies and the exact relational proof-search route

Date: 2026-09-06.

## Outcome

The existing Maehara lemma is for the purely relational, equality-free
restriction of the finite-multiset calculus `sheet:lk-defneg`, called
`LK_d`. Two legitimate routes can supply its cut-free derivation input:

1. Cite completeness and cut elimination for a precisely identified
   classical calculus, giving the short rule translations to `LK_d`.
2. Prove cut-free completeness directly for the exact relational `LK_d`
   rules by fair persistent proof search and a saturated countermodel.

The second route proposed during this research is sound and avoids
dependence on the older general cut-elimination sketch. Gallier's primary
author text gives directly relevant proof-search and Hintikka-set results,
with exact locators below. It is a source for this method; the new local
argument must still verify its own `LK_d` instances rather than silently
identify the two rule systems.

Completeness and cut elimination may be cited dependencies of a fully
supplied interpolation proof. There is no requirement to reproduce their
entire general proofs as part of that interpolation proof.

## Primary source read

Jean H. Gallier, *Logic for Computer Science: Foundations of Automatic
Theorem Proving*, second edition, Dover, 2015.

- [Author's book page](https://www.cis.upenn.edu/~jean/gbooks/logic.html).
- [Author-hosted full second-edition PDF](https://www.seas.upenn.edu/~jean/Logic-for-CS-2015.pdf).

The author page identifies this as the corrected second edition of the
1986 Wiley book. The actual PDF title page identifies the second edition,
Gallier, and Dover. The body has 520 physical PDF pages; the relevant
printed Arabic page numbers equal physical PDF page numbers minus 24.
This pass retrieved the primary PDF into memory and extracted the selected
pages as text. It created no source download, manuscript render, or
software-test artifact.

### Exact usable statements and surrounding conventions

| Primary location | Result or convention |
|---|---|
| Definition 5.4.1, pp. 180-181, PDF 204-205 | Equality-free first-order calculus `G`; contexted identity, propositional rules, persistent `forall L` and `exists R`, ordinary eigenvariable rules. |
| Definition 5.4.2, pp. 181-182, PDF 205-206 | Finite-sequent validity/falsifiability under every structure and assignment; empty antecedent and succedent are explicitly covered. |
| Lemma 5.4.3, p. 185, PDF 209 | Every `G`-provable sequent is valid. |
| Definition 5.4.7 and Lemma 5.4.5, pp. 188-190, PDF 212-214 | Saturated signed sets over a nonempty term domain; the induced structure and identity-on-variables assignment satisfy every signed member. |
| Section 5.4.7, Definitions 5.4.8-5.4.9, pp. 191-194, PDF 215-218 | Function-free, equality-free search; retained universal-type formulas, tracked instances, fresh witnesses, and systematic expansion. |
| Theorem 5.4.1, pp. 197-198, PDF 221-222 | A valid finite input sequent with no variable both free and bound produces a finite closed proof tree; a falsifiable input yields a finite or countably infinite countermodel. |
| Corollary following Theorem 5.4.1, p. 198, PDF 222 | A valid sequent in the stated function-free, equality-free language, with the same variable hygiene, is `G`-provable. |
| Definition 6.2.1, pp. 247-249, PDF 271-273 | Equality-free `LK`, uncontexted identity, explicit structural rules, split implication-left, four quantifier rules, and finite proof trees. |
| Theorem 6.2.1 and following Hauptsatz corollary, pp. 249-250, PDF 273-274 | A `G` proof converts into a proof in `LK` without Cut, and an `LK`-provable sequent has a cut-free `LK` proof. |
| Section 6.5.2, p. 276, PDF 300 | `LK_bot` adds the logical falsity axiom `bot =>`; the text explicitly states that cut elimination continues to hold, with its verification assigned as an exercise. |

The finite pure relational use needed here is a restriction of Theorem
5.4.1: no equality, no positive-arity function symbols, and no constant
symbols; free variables are allowed. The input sequent uses only finitely
many predicate symbols and finitely many formula occurrences. Formula
validity ranges over nonempty structures and all assignments. The
source's variable-hygiene assumption can be enforced by renaming bound
variables before applying its theorem.

Gallier's Section 5.4.7 also permits constants, but they are unnecessary
for the book's selected fragment. The term domain can consist entirely
of variable names. The source gives a nonempty initial term domain even
when the input has no free variables or constants, by supplying a fresh
variable. Root's proposed use of the entire countable variable set as
domain handles that case directly.

## Exact book calculus and source matching

The active sheet is
`handbook/registry/calculi/lk-defneg.tex`, label `sheet:lk-defneg`.
It has:

- two-sided finite-multiset sequents, with either context possibly empty;
- logical primitives `bot,and,or,imp,forall,exists` and defined negation
  `not A := A imp bot`;
- identity `A => A`, and the contextual falsity initial
  `bot,Gamma => Delta`;
- explicit left/right weakening and contraction; exchange built into
  multiset equality;
- split-context implication-left;
- the combined `and L` and `or R` rules;
- all four ordinary quantifier rules, with fresh eigenvariables for
  `forall R` and `exists L`;
- total capture-avoiding substitution; and
- Cut and Mix as displayed rules, both absent from a cut-free derivation
  supplied to Maehara.

The local Maehara fragment excludes equality, functions, and constants,
so every term is a variable. The logical constant `bot` is still
available; it is not an excluded nonlogical constant symbol.

Gallier's `G` is close to the desired proof-search presentation, but is
not literally this sheet. Its implication-left uses shared contexts,
it has primitive negation, and its universal-type quantifier rules
retain the principal formula. Gallier's `LK` has the same uncontexted
identity and split implication-left as the sheet, but uses sequence
exchange and unary alternative `and L` / `or R` rules.

For a cited-dependency route, these differences have explicit finite
cut-free simulations:

- Sequence exchange disappears when contexts are represented as multisets.
- Contextual identity is identity plus weakenings.
- A unary `and L` rule is simulated by weakening in the unused conjunct
  and applying the sheet's combined `and L`. A unary `or R` rule is
  simulated by weakening in the unused disjunct and applying combined
  `or R`.
- Shared-context implication-left is split implication-left followed by
  contraction of the duplicated context formulas on both sides.
- A persistent `forall L` instance is ordinary `forall L`, with the
  retained universal formula in the context, followed by contraction;
  persistent `exists R` is analogous on the right.
- Translate source primitive negation by `A imp bot`. For source negation
  left, apply split implication-left to the translated premise and
  `bot =>`. For source negation right, right-weaken by `bot` and apply
  implication-right. These simulations introduce no Cut.
- `bot,Gamma => Delta` follows from `bot =>` by weakening in the source's
  `LK_bot`; conversely the sheet contains `bot =>` as an instance.

The source uses the ordinary free-for-substitution proviso. The sheet's
total capture-avoiding substitution agrees after its stipulated bound
renaming. Fresh eigenvariables may be chosen outside the finite current
sequent and any finitely many names reserved in a proof fragment.

These simulations explain how to state a cited dependency accurately.
They do not upgrade the old local presentation-equivalence sketch merely
by mentioning that the variants are equivalent. Root's direct proof
route below can establish exactly the result needed without using that
sketch or the `LK_bot` extension as premises.

## Check of the direct persistent proof-search proposal

The proposed theorem is:

> For every finite sequent `Gamma => Delta` of the purely relational,
> equality-free `LK_d` language, if it is valid in all nonempty structures
> under all assignments, it has a finite derivation using the selected
> sheet's rules except Cut and Mix.

This is the exact cut-free input required by `thm:p07-maehara-partition`.
No flaw was found in the proposed proof route. The following details
make its connection to the exact calculus explicit.

### Persistent expansion and preservation of underivability

Assume the finite initial sequent has no cut-free derivation. Work with
finite sets of formulas as an enumeration convenience, interpreting each
as a multiset with one occurrence of each member. At every step retain
all preceding formulas and add the selected decomposition formulas.

For each backward expansion, if all candidate premises had cut-free
proofs, the sheet's matching logical rule followed by contractions would
give a cut-free proof of the current persistent conclusion. Therefore
at least one candidate premise is cut-free underivable. Choose one.
This argument must precede use of the phrase "choose an underivable
branch"; the choice is an ordinary classical existence construction,
not a claimed effective test for underivability.

For example, when `A imp B` is on the left, use the two candidates
`Gamma => Delta,A` and `B,Gamma => Delta`, keeping `A imp B` already
inside `Gamma`. Split implication-left on proofs of both candidates
would yield

\[
(A\to B),\Gamma,\Gamma\Rightarrow\Delta,\Delta.
\]

Contract all duplicated context occurrences, including any extra copy
of the principal implication, to recover the current sequent. This
validates the shared-context persistent expansion on the actual
split-context sheet.

The single-premise persistent quantifier steps similarly reintroduce
the retained principal formula and contract its duplicate. For an
eigenvariable step, select a variable absent from the current finite
sequent; retaining the quantified principal formula creates no freshness
problem. A variable absent from every variable occurrence of that sequent
is a convenient stronger choice.

No stage can contain the same formula on both sides, because identity
and weakening would close it. No stage can have `bot` on the left,
because that is an initial sequent. `bot` on the right is harmless and
is false in the constructed model.

### Fairness and the countable domain

Use a fixed countably infinite supply `v_0,v_1,...` of variables.
Schedule every persistent formula and, for `forall` on the left or
`exists` on the right, every pair of that formula with a variable in
this entire supply. A dovetail or repeatedly extended finite queue
ensures each applicable obligation is eventually processed.

For left `exists` and right `forall`, one fresh witness for each
occurrence obligation suffices. For left `forall` and right `exists`,
instantiating only currently free variables is insufficient if the model
domain is the entire fixed variable set. Every domain variable must
eventually be covered. Alternatively one may use Gallier's growing
activated-variable domain, but then its domain and fairness argument
must be stated in that different form.

Allow idle repetitions if a finite saturated underivable sequent is
reached. This gives a uniform infinite monotone chain without claiming
that a finite terminal branch does not yield a countermodel.

### Saturated model and truth induction

Take the unions `Gamma_infty,Delta_infty` of the two context chains.
Their consistent atomic requirements define a relational structure on
the nonempty countable variable set. Interpret

\[
P^{\mathcal M}(v_{i_1},\ldots,v_{i_r})
\quad\Longleftrightarrow\quad
P(v_{i_1},\ldots,v_{i_r})\in\Gamma_\infty.
\]

Unspecified tuples may be false. A tuple required false by an atom in
`Delta_infty` is not required true, because no atom belongs to both
unions. Set the variable assignment to the identity.

The induction simultaneously establishes that every formula in
`Gamma_infty` is true and every formula in `Delta_infty` is false.
The Boolean expansion clauses give its propositional cases. For
quantifiers, the universal instance requirements cover every domain
variable, while the existential-type expansions supply a witness.
Use the already established capture-avoiding substitution lemma to
identify truth of `A[v_i/x]` under the identity assignment with truth
of `A` under the assignment sending `x` to domain element `v_i`.

This model falsifies the initial sequent, contradicting its validity.
Thus a finite cut-free proof exists. The finite relational signature
actually occurring in the initial sequent suffices; any unused ambient
predicate symbols can be interpreted arbitrarily. This local argument
does not need the Axiom of Choice for arbitrary-language completeness.

The source grounding is Gallier's persistent universal rules
(Definition 5.4.1), the systematic repeated-instantiation construction
(Section 5.4.7), the Hintikka truth lemma (Lemma 5.4.5), and the
finite-sequent completeness theorem (Theorem 5.4.1). The choices of
defined negation, full fixed variable domain, and monotone underivable
chain are supplied adaptations to the book's exact sheet.

## Existing local completeness, compactness, and proof routes

The following are usable local dependencies or precise existing
boundaries, not grounds to re-prove every cited result:

- `handbook/restoration/inherited-04713-04920.tex`,
  `thm:fol-completeness`: for arbitrary signature, assuming the Axiom
  of Choice, semantic consequence from a set of formulas implies a
  finite classical natural-deduction derivation. Its full local proof
  is printed there.
- `handbook/restoration/inherited-04921-04967.tex`,
  `thm:fol-compactness`: with the same Choice hypothesis, semantic
  consequence of a sentence from a theory has a finite theory subset
  already entailing it. This is useful for an arbitrary-theory Beth
  argument and has a complete local proof.
- `handbook/parts/p07/calculi-and-derivability-supplement.tex`,
  `thm:p07-canonical-lk-completeness`, proved at
  `annex:p7.calculi.4`: finite equality-free sequents, arbitrary
  nonempty structures and assignments, empty contexts included. It
  uses Cut; for arbitrary signatures it states Choice, while its
  countable-language route does not require it.
- The same supplement's `thm:p07-lk-presentation-equivalence`, with
  `annex:p7.calculi.2`, remains a separate presentation-translation
  statement. Its inspected version was explicitly sketched and did
  not assert preservation of cut-freeness. Do not infer cut-free
  `LK_d` completeness from that claim alone.
- `handbook/restoration/inherited-11768-11823.tex` states general
  cut elimination for the inherited defined-negation `LK`/`LJ`
  surface with an explicitly sketched local proof and citations to
  Troelstra-Schwichtenberg and Negri-von Plato. A separately stated
  cited dependency or the direct exact-fragment proof above avoids
  using that sketch as if it supplied the omitted reductions.

## Craig and Beth: labels, active routes, and scope

Both original statements are in the active file
`handbook/restoration/inherited-11914-11960.tex`, reached by
`handbook/restoration/scope-SRC-11914-11960.tex`. The Part VII driver
`handbook/parts/p07.tex` inputs that wrapper and then the separately
authored `cut-elimination-and-interpolation-supplement.tex`.

The stable statement labels are:

- `thm:craig-interpolation` for the sentence interpolation theorem:
  if `models phi -> psi`, there is a sentence interpolant whose
  nonlogical symbols occur in both inputs; equality and logical
  falsity are permitted regardless of their occurrence in the inputs.
- `thm:beth` for the implicit-to-explicit definability theorem for
  a distinguished relation symbol in an arbitrary first-order theory;
  its conclusion is derivability of the universal defining equivalence.

These are ordinary restored theorem environments, not `hbtheorem`
environments with a status argument. Their inspected original statuses
were literal `Status: cited theorem` paragraphs inside the statements.
Root is authoring their new proof/status treatment concurrently; the
labels and wrapper route above are the stable connection points.

The local Maehara statement is
`thm:p07-maehara-partition` in
`handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex`.
Its complete annex proof is `annex:p7.interp.1` in
`handbook/annex/p07/interpolation-supplement.tex`, actively input by
`handbook/annex/p07.tex`. The old files without the `-supplement` suffix
are retained historical material and are not this active proof route.

The original Craig/Beth statements allow general signatures, including
functions, constants, and equality. A new pure-relational completeness
lemma and Maehara proof establish their pure-relational equality-free
base case. The eventual full proof must also justify its passage to
the original general statement, for example through an explicit
relationalization/equality treatment. Citing full completeness and
compactness as dependencies is compatible with supplying that argument
fully; silently dropping the original statement's signature scope is not.

Only this note was authored. No handbook edits, software tests,
manuscript builds, or renders were performed.
