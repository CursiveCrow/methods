# Constructive cut elimination for the exact registered LJ

Date: 9 September 2026. Constructive helper for `requirements_integrator`.
This note owns no manuscript body, annex, driver or shared registry. It supplies
the complete local construction for the writer to integrate, rather than an
independent review or an acceptance decision.

## Exact target and dependencies

Read in full: `handbook/registry/calculi/lj.tex`, the active cut/mix chapter
`handbook/parts/p07/cut-elimination-and-interpolation.tex`, its current annex
`handbook/annex/p07/calculi-and-cut-elimination.tex`, and the context/derivation
definitions in `handbook/parts/p07/calculi-and-derivability.tex`.

The target has finite-multiset antecedents and **exactly one succedent formula**.
Its initial sequents are `A => A` and `bottom, Gamma => Z`. Exchange is built
into the multiset representation. WL and CL are explicit. There is no right
weakening or right contraction. The logical rules are precisely:

- conjunction-left with both conjuncts in its one premise;
- conjunction-right with the same antecedent in both premises;
- disjunction-left with the same side antecedent in both premises;
- the two disjunction-right rules;
- split-context implication-left and ordinary implication-right;
- forall-left and exists-right with total capture-avoiding term substitution;
- forall-right and exists-left with the displayed fresh eigenvariable;
- no primitive negation rule, since negation is implication to bottom;
- no equality, modal, arithmetic, induction or fixed-point rule.

Cut and the registered n-Mix are both eliminated. In this note a **reduction-free
derivation** contains neither Cut nor Mix. The output is therefore stronger than
merely satisfying a literal test for absence of a node named Cut.

No empty succedent is used at any stage. In particular, `Gamma => bottom` is a
single-succedent sequent and is not identified with `Gamma =>` or with the
classical empty sequent. The active empty-sequent corollary is LK_d-only.

The dependency order below is noncircular:

1. Capture-avoiding syntax and substitution on alpha-equivalence classes.
2. Height-preserving substitution and eigenparameter freshening of reduction-free
   alpha-class derivations.
3. Structural padding/contraction and bottom-succedent replacement, without Cut.
4. Marked multicut on alpha-class derivations, by the specified nested induction.
5. Normalize arbitrary alpha-class derivations bottom-up using marked multicut.
6. Build literal alpha-identity derivations by formula induction.
7. Realize the final reduction-free alpha-class derivation at the exact desired
   literal endsequent, without claiming height preservation.

The final two steps do not use marked multicut or the desired Cut theorem.

## Why the alpha-class stage must be explicit

The source syntax uses literal formulas with a least-fresh capture-avoiding
substitution convention. Literal alpha-conversion is not identity. For example,
`forall x P(x) => forall x P(x)` is an Id of height zero; independently changing
only the right binder to `z` does not leave an Id of height zero.

There is a second issue even for fresh free-variable renaming. Instantiate
`forall x forall y R(x,y)` at the term `y`. Its premise is an alpha-renamed
formula such as `forall w R(y,w)`. Renaming that free `y` to a wholly fresh `z`
gives `forall w R(z,w)`, whereas directly instantiating the unchanged principal
formula at `z` can give the literal `forall y R(z,y)`. The premises agree up to
alpha-equivalence, not necessarily as strings under least-fresh substitution.

Accordingly, the induction below is in an auxiliary calculus whose formulas are
alpha-equivalence classes, **not** a calculus with set antecedents, implicit
contraction or classical succedents. It retains every occurrence and every
registered rule shape. Free variables and logical rank are well defined on these
classes. The raw-to-alpha projection sends every registered rule to its
alpha-class rule and preserves tree height.

### Syntax facts needed for the auxiliary calculus

Capture-avoiding substitution respects alpha-equivalence and hence defines
`[B][t/x] := [B[t/x]]`. These are the elementary binding facts used below:

- substitution of terms changes no logical connective or quantifier count;
- a variable fresh for a formula and term can be used as a temporary parameter;
- if `z` is fresh for `B` and `t`, then
  `[(B[z/x])[t/z]] = [B[t/x]]`;
- a simultaneous finite substitution commutes with a quantifier-rule instance
  after its bound variables and eigenparameter have been made fresh for the
  substitution's variables and term ranges.

These facts follow by induction on formula syntax. Atomic formulas reduce to
term substitution. Boolean connectives apply the induction hypothesis to their
children. At a quantifier, choose a binder absent from the finitely many free
variables under consideration, apply the induction hypothesis to the matrix,
and restore the alpha-class of the binder. This is why no assertion of literal
least-fresh-string equality is required.

### Height-preserving substitution and freshening

For a finite simultaneous substitution `theta`, a reduction-free alpha-proof of
`Gamma => Z` has a reduction-free alpha-proof of `Gamma theta => Z theta` of no
greater height. Prove this by induction on the input tree:

- Id remains Id; bottom-left remains bottom-left.
- WL/CL keep their displayed occurrences and reapply the same rule.
- Every propositional rule keeps its shape; shared contexts remain the same
  substituted multiset and split contexts remain their substituted union.
- For forall-left/exists-right, substitute in the witness term and use the
  alpha-class substitution fact to identify the required instantiated matrix.
- Before forall-right/exists-left, change the eigenparameter to a variable fresh
  for the finite substitution, all its term ranges and the required conclusion.
  Apply the induction hypothesis to the premise and reapply the same quantifier
  rule. Its fresh parameter cannot enter the substituted conclusion.

The parameter change itself uses the smaller premise tree: substitute the old
parameter by the fresh variable throughout that premise. The rule's freshness
condition says that this changes no formula in its conclusion. Formula syntax
is considered modulo alpha at this stage. Thus the parameter-renaming argument
does not assume the same substitution theorem at the unreduced height.

Iterating these changes gives distinct eigenparameters for all relevant
inferences and avoids any prescribed finite forbidden-variable set. Heights do
not increase. This is sufficient for commuting inferences below. The final raw
representative realization is a different lemma with no height guarantee.

## Structural operations and bottom replacement

### Padding and merging copies of a context

`Pad_Gamma` appends exactly the finite multiset `Gamma` by WL, one occurrence at
a time. It introduces no Cut or Mix. Its height may increase by the cardinality
of `Gamma`; no contrary bound is used.

`Merge_Gamma` changes `Gamma, Gamma, Xi => Z` into `Gamma, Xi => Z` by CL.
If a formula occurs `r` times in `Gamma`, there are `2r` designated copies in
the two copies of that context; make exactly `r` contractions to retain `r`.
Occurrences in `Xi` are not part of this contraction bookkeeping, even if their
formula is identical. For an empty `Gamma` this operation is the identity.

### Bottom-succedent replacement

If `D` is a reduction-free proof of `Gamma => bottom`, then for any formula `Z`
there is a reduction-free proof of `Gamma => Z`. This is proved directly by
induction on `D`, not by Cut or right weakening:

- Id can only be `bottom => bottom`; replace it by bottom-left with succedent Z.
- A bottom-left leaf stays bottom-left with succedent Z.
- Commute the replacement through WL, CL, conjunction-left and forall-left.
- For disjunction-left, replace the succedent in both premises and reapply the
  additive rule with its unchanged common context.
- For implication-left, retain its first premise `Sigma => B`, replace bottom
  by Z only in its second premise `C,Theta => bottom`, and reapply implication-left.
- For exists-left, first freshen its eigenparameter away from Z, use the induction
  hypothesis in its premise, and reapply exists-left. The new eigencondition holds.
- No logical right introduction concludes with the primitive formula bottom.
  There are no right structural rules and no Cut/Mix cases in the input grammar.

This exhausts the sheet. In the alpha calculus its height need not increase,
but only existence of a reduction-free replacement is needed in the main lemma.

## Marked multicut statement and exact measure

Let `D : Gamma => A` and `E : Omega => Z` be reduction-free alpha-proofs. Select
`n` individual antecedent occurrences of A in E's endsequent. Write

`Omega = A^[n], Pi`,

where the brackets indicate the selected occurrences and `Pi` contains every
unselected occurrence. Neither `Gamma` nor `Pi` is required to be A-free. The
operation

`M_A(D, E; selected occurrences)`

must return a reduction-free derivation of `Gamma, Pi => Z`, with **one** retained
copy of Gamma, independently of n.

The actual registered Mix has `n >= 1`. Use `n=0` only as a convenient derived
base operation: return `Pad_Gamma(E)`. No zero-multiplicity primitive Mix is
added to the sheet.

For `n>0`, induct lexicographically on

`(rank(A), height(D) + height(E))`.

Equivalently, assume the statement for every smaller formula rank and all finite
heights, and at the current rank induct on the premise-height sum. Rank is the
number of logical symbols after expanding defined negation. A term instance of
a quantifier matrix has smaller rank than that quantified formula, regardless
of the size of the term.

Every same-rank recursive call below uses an original immediate premise of D
or E, after at most height-preserving eigenparameter freshening. Its height sum
therefore strictly decreases. All calls using a newly constructed proof have
strictly smaller formula rank. The multiplicity n is not a measure coordinate.
An output proof is not claimed to have bounded height relative to the input.

### Mark transport

Marks are occurrence annotations for the construction, not new object-language
symbols. Copy context marks to the corresponding premise occurrences. Shared
contexts in conjunction-right and disjunction-left copy the marks into both
premises. Split implication-left distributes them between its two context parts.

If a contracted conclusion occurrence is marked, mark **both** displayed premise
occurrences. If it is unmarked, leave both displayed premise occurrences unmarked.
If a logical principal occurrence is unmarked, all its active subformulas are
unmarked, even when an active formula happens to have the same syntax as A.

These rules preserve all unselected assumptions. Formula coincidence is never a
license to delete an unmarked occurrence.

## Initial and zero-mark cases

Apply these before the remaining permutations:

1. `n=0`: the padding base above.
2. D is Id `A => A`: contract the n selected copies of A in E to one by `n-1`
   CL steps; leave Pi untouched. The result is `A,Pi => Z = Gamma,Pi => Z`.
3. D is bottom-left: Gamma contains an unselected bottom. Close
   `Gamma,Pi => Z` directly by bottom-left.
4. E is Id. Since `n>0` and Id is uncontexted, its antecedent has exactly one
   occurrence, necessarily the selected A, and its succedent is A. Thus `n=1`,
   `Pi` is empty and Z=A; return D.
5. E is bottom-left. If an unselected bottom remains in Pi, close the target
   directly. Otherwise its displayed bottom is selected, so A=bottom. Use
   bottom-succedent replacement on D to obtain `Gamma => Z`, then pad Pi.

The last case is essential: Gamma need not itself contain a literal bottom.
A proof of bottom can end in implication-left, for example.

## Commuting above a nonprincipal last inference of D

The left derivation's distinguished occurrence is its one succedent A. Its last
rule is nonprincipal precisely for a structural or logical left rule. For each
case below, every recursive call has smaller left-premise height and unchanged
original E. Let Pi denote the unmarked context in E throughout.

### Left WL

From `D0 : Gamma0 => A`, D concludes `B,Gamma0 => A`. Compute
`M_A(D0,E) : Gamma0,Pi => Z`, then use WL on B. This includes B=A: that newly
weakened left-context occurrence is not a selected right occurrence.

### Left CL

From `D0 : B,B,Gamma0 => A`, D concludes `B,Gamma0 => A`. Compute
`B,B,Gamma0,Pi => Z` by induction and reapply CL on the two designated B copies.

### Left conjunction-left

From `D0 : B,C,Gamma0 => A`, compute `B,C,Gamma0,Pi => Z` and reapply
conjunction-left, giving `B and C,Gamma0,Pi => Z`.

### Left disjunction-left

D has premises `D1 : B,Gamma0 => A` and `D2 : C,Gamma0 => A`. Their inductive
outputs are `B,Gamma0,Pi => Z` and `C,Gamma0,Pi => Z`. They have the same side
context, so additive disjunction-left gives `B or C,Gamma0,Pi => Z`.

### Left implication-left

D has premises `D1 : Sigma => B` and `D2 : C,Theta => A`, and concludes
`B implies C,Sigma,Theta => A`. Leave D1 unchanged. Induction on D2 and E gives
`C,Theta,Pi => Z`. Split-context implication-left now gives exactly
`B implies C,Sigma,Theta,Pi => Z`. No second succedent is introduced and the
first premise is not cut against E, even if its succedent happens to equal A.

### Left forall-left

D0 proves `B[t/x],Gamma0 => A`. Its inductive output is
`B[t/x],Gamma0,Pi => Z`. Reapply forall-left to obtain
`forall x B,Gamma0,Pi => Z`. The witness term is unchanged; the sheet has no
additional substitutability side condition.

### Left exists-left

Before any recursive call, freshen the last eigenparameter to z, avoiding all
variables of the two supplied proofs and in particular FV(Pi,Z). Its premise
is `B[z/x],Gamma0 => A`. Induction yields `B[z/x],Gamma0,Pi => Z`. Reapply
exists-left. The parameter is fresh for `exists x B,Gamma0,Pi => Z`, so the
registered side condition holds.

These seven cases exhaust nonprincipal last rules of D. The base cases handle
its leaves. Otherwise D's last rule introduces its succedent A and is one of
conjunction-right, a disjunction-right, implication-right, forall-right or
exists-right. Atoms and bottom have no such right introduction.

## Commuting above a last inference of E when its principal antecedent is unmarked

All last right introductions in E belong here: the selected occurrences are
in its antecedent, not its succedent. Each nonzero-mark inductive call uses
the unchanged original D and an original immediate E-premise of smaller height.
Use the padding base in any zero-mark premise.

### Right WL

If the newly weakened B is unmarked, transport all marks to E0, apply induction
and reweaken B. If B is selected (hence B=A), omit that weakening and transport
only the remaining `n-1` marks to E0. Induction, or padding when `n=1`, already
gives the required target. No cut against the weakened occurrence remains.

### Right CL

If the contracted conclusion occurrence is marked, the premise has `n+1`
marks: the two active copies and the `n-1` other selected copies. Apply induction
at this larger multiplicity and smaller height. Its output is already the
target; do not restore the selected A.

If the contracted occurrence is unmarked, its two active premise copies remain
unmarked. Induction gives `Gamma,B,B,Pi0 => Z`; one CL yields
`Gamma,B,Pi0 => Z`. This includes the case B=A with unmarked copies.

### Right conjunction-left, unmarked principal

For a last rule from `B,C,A^[n],Pi0 => Z` to
`B and C,A^[n],Pi0 => Z`, apply induction only to the context marks, obtaining
`B,C,Gamma,Pi0 => Z`, and reapply conjunction-left.

### Right conjunction-right

The premises are `A^[n],Pi => B` and `A^[n],Pi => C`. Induction gives
`Gamma,Pi => B` and `Gamma,Pi => C`. Their antecedents agree literally as
multisets of alpha-classes. Reapply additive conjunction-right. There is one
copy of Gamma in the conclusion; no contraction is required here.

### Right disjunction-left, unmarked principal

The premises are `B,A^[n],Pi0 => Z` and `C,A^[n],Pi0 => Z`. Induction gives
`B,Gamma,Pi0 => Z` and `C,Gamma,Pi0 => Z`; additive disjunction-left gives
`B or C,Gamma,Pi0 => Z`. Active B or C remains unmarked even if it equals A.

### Right disjunction-right

For either selected injection, apply induction to its one premise, retaining
the chosen succedent summand, and reapply that same injection. The unchanged
other summand imposes no context or multiplicity requirement.

### Right implication-left, unmarked principal

Write the premises as `E1 : Sigma => B` and `E2 : C,Theta => Z`, with `n1`
marks in Sigma and `n2` in Theta, where `n1+n2=n`. Let their unmarked remainders
be Sigma0 and Theta0. Induction or padding gives

`Gamma,Sigma0 => B` and `C,Gamma,Theta0 => Z`.

Reapply the split-context implication-left rule. It gives

`B implies C,Gamma,Sigma0,Gamma,Theta0 => Z`.

Apply `Merge_Gamma`, retaining the principal implication and every unmarked
context occurrence, to obtain `Gamma,B implies C,Sigma0,Theta0 => Z`.
The two zero/nonzero possibilities in each branch are covered by the padding
convention; there is never a classical extra right context.

### Right implication-right

Its premise is `B,A^[n],Pi => C`. Mark only the inherited A occurrences, not
the active discharged B. Induction gives `B,Gamma,Pi => C`; implication-right
then gives `Gamma,Pi => B implies C`. This remains valid if B happens to equal A.

### Right forall-left, unmarked principal

Its premise is `B[t/x],A^[n],Pi0 => Z`. Induction gives
`B[t/x],Gamma,Pi0 => Z`; reapply forall-left with the same t. The active instance
is not marked merely because its formula equals A.

### Right forall-right

Freshen its eigenparameter to z before induction, avoiding FV(Gamma) and all
variables in D and E. Its premise is `A^[n],Pi => B[z/x]`. Induction gives
`Gamma,Pi => B[z/x]`. Freshness for `Gamma,Pi => forall x B` is now explicit,
so forall-right applies. The original eigencondition alone would not suffice
if the old parameter were free in the newly inserted Gamma.

### Right exists-left, unmarked principal

Freshen its eigenparameter to z, avoiding FV(Gamma) and the supplied proofs.
Induction on `B[z/x],A^[n],Pi0 => Z` gives
`B[z/x],Gamma,Pi0 => Z`. Reapply exists-left. Its new conclusion contains no
free z. The active matrix instance remains unmarked.

### Right exists-right

Induction on `A^[n],Pi => B[t/x]` gives `Gamma,Pi => B[t/x]`.
Reapply exists-right with the same t. No eigenvariable side condition exists
for this rule on the actual sheet.

There are no other right structural, primitive-negation or equality cases.
If D introduced A on the right and none of these right permutations/base cases
applies, E's last logical left rule has a selected occurrence of A as principal.

## Principal/principal reductions with residual marks

The decisive order is: **remove residual marks at rank A first, using the
original D and original immediate premises of E; then use smaller-rank
multicuts.** Never make a same-rank recursive call against an arbitrary proof
just manufactured by a previous multicut.

Write E's selected principal occurrence separately; there are `n-1` other marks.
All lower-rank calls below select exactly the displayed active occurrence.
If Gamma itself contains formulas of the same shape, those are retained.

### A = B and C

D has premises `D_B : Gamma => B` and `D_C : Gamma => C`.
E has premise `E0 : B,C,A^[n-1],Pi => Z`.

1. The residual-mark call `M_A(D,E0)` gives `B,C,Gamma,Pi => Z`.
   For `n=1`, this is just padding of E0. The nonzero case has smaller E-height.
2. A lower-rank multicut on B using D_B gives `Gamma,C,Gamma,Pi => Z`.
3. Merge the two copies of Gamma, yielding `C,Gamma,Pi => Z`.
4. A lower-rank multicut on C using D_C gives `Gamma,Gamma,Pi => Z`.
5. Merge Gamma again, obtaining the exact target.

Both component ranks are strictly smaller than rank(A); the heights of the
constructed right proofs are irrelevant to those outer-induction calls.

### A = B or C

If D ends in the first injection, let `D_B : Gamma => B`. Choose E's B-premise
`E_B : B,A^[n-1],Pi => Z`. Remove its residual A marks with the original D,
giving `B,Gamma,Pi => Z`. Cut the displayed B by the smaller-rank lemma using
D_B, and merge the two copies of Gamma. E's C-premise is not used.

For the second injection, choose its proof D_C and E's C-premise instead.
The same steps on C give the target. Both branches of the injection choice
are covered; there is no need to keep a superfluous disjunction proof.

### A = B implies C

D's premise is `D0 : B,Gamma => C`. E's implication-left premises are
`E1 : Sigma => B` and `E2 : C,Theta => Z`. Residual selected copies of A are
distributed between Sigma and Theta. Let their unmarked remainders be Sigma0
and Theta0; the target Pi is `Sigma0,Theta0`.

1. Residual cleanup with the original D gives
   `R1 : Gamma,Sigma0 => B` and `R2 : C,Gamma,Theta0 => Z`.
   Each nonzero call has smaller original E-premise height; use padding in a
   zero-mark branch.
2. Apply the smaller-rank lemma on B to R1 and D0, selecting only D0's displayed
   active B. This gives `Gamma,Sigma0,Gamma => C`.
3. Merge Gamma, giving `R3 : Gamma,Sigma0 => C`.
4. Apply the smaller-rank lemma on C to R3 and R2, selecting R2's active C.
   It gives `Gamma,Sigma0,Gamma,Theta0 => Z`.
5. Merge Gamma to obtain `Gamma,Sigma0,Theta0 => Z`.

This is the contraction-sensitive implication reduction. In particular, R1's
single succedent is B and D0's single succedent is C. No formula is moved to
a second succedent, and no same-rank cut is applied to R1, R2 or R3.

### A = forall x B

After freshening D's last eigenparameter to z, its premise is
`D0 : Gamma => B[z/x]`. Choose z outside all variables of E and its witness t,
and outside Gamma and B. E's premise is
`E0 : B[t/x],A^[n-1],Pi => Z`.

1. Remove E0's residual A marks using the original D. Obtain
   `R : B[t/x],Gamma,Pi => Z`.
2. Substitute `[t/z]` in D0. It leaves Gamma unchanged and gives a reduction-free
   alpha-proof `D_t : Gamma => B[t/x]`, by the fresh-instance substitution fact.
3. Apply the smaller-rank lemma on the instance `B[t/x]` to D_t and R.
4. Merge the resulting two copies of Gamma.

The residual call precedes the lower-rank work and has smaller original
E-height. The substitution can enlarge terms, but never formula rank.

### A = exists x B

D's premise is `D0 : Gamma => B[t/x]`. Freshen E's last eigenparameter to z,
avoiding D, t, Gamma, Pi and Z. Its premise is
`E0 : B[z/x],A^[n-1],Pi => Z`.

1. Remove residual A marks using the original D and E0. Obtain
   `R : B[z/x],Gamma,Pi => Z`.
2. Apply `[t/z]` to this reduction-free alpha-proof. Its endsequent becomes
   `B[t/x],Gamma,Pi => Z`; Gamma, Pi and Z are unchanged by freshness.
3. Apply the smaller-rank lemma on `B[t/x]` using D0, then merge Gamma.

Here substitution is applied after residual cleanup, but the only subsequent
multicut has smaller rank. There is no same-rank call using the substituted
constructed proof.

### Atoms and bottom

There is no principal/principal logical pair for an atom or bottom because
neither has a logical right-introduction rule. Their derivations have already
been handled by the initial cases and left-side permutations. A selected
bottom in an E bottom-left leaf uses the separate bottom replacement lemma.
Defined negation expands to implication and therefore uses the implication
case; no new negation case is added.

## Termination and elimination of arbitrary Cut/Mix nodes

The case list is exhaustive. For nonzero marks, either a leaf case applies,
D ends in a nonprincipal left/structural inference, E has a commuting inference,
or both displayed logical occurrences are principal. Same-rank recursion
strictly lowers the premise-height sum. Principal reductions use only finitely
many smaller-rank calls after the residual cleanup. Padding, substitution,
freshening and finite contractions terminate independently. Thus lexicographic
induction proves the operation for every finite input pair and every finite
selected multiplicity.

Now induct on the original finite derivation tree in the alpha calculus.
Normalize each immediate premise first. For an ordinary rule reapply that
same rule to its normalized premises, whose endsequents are unchanged. For a
Cut use the marked multicut with one selected occurrence; for a registered
Mix use its displayed n selected occurrences. Its inputs are reduction-free
because they have already been normalized. The local lemma returns a
reduction-free proof of the same conclusion.

This bottom-up procedure avoids an unsupported claim that one naive global
height sum decreases during arbitrary contractions and duplications of a
whole proof containing other Cuts. Its well-founded measures are the finite
original tree recursion and the proved local rank/height recursion.

## Cut-free literal alpha identity

Prove by induction on formula rank that if literal formulas A and A' are
alpha-equivalent, there is a reduction-free proof `A => A'` on the exact raw
sheet. The claim is symmetric, so smaller-rank instances are available in
either direction. No quotient identity is assumed to be a literal identity.

- For atoms and bottom, alpha-equivalence is literal equality: use Id.
- If `A=B and C` and `A'=B' and C'`, use the inductive proofs `B=>B'` and
  `C=>C'`. Weaken each to antecedent `B,C`, combine by additive conjunction-right,
  and use conjunction-left.
- If `A=B or C` and `A'=B' or C'`, inject the inductive proof `B=>B'` into
  the left summand of A', and `C=>C'` into the right summand. Combine by
  disjunction-left with empty shared side context.
- If `A=B implies C` and `A'=B' implies C'`, use `B'=>B` and `C=>C'`.
  Split-context implication-left gives `B implies C,B' => C'`; implication-right
  discharges its displayed B', producing `A=>A'`.
- If `A=forall x B` and `A'=forall y B'`, choose z fresh for both formulas.
  The instances `B[z/x]` and `B'[z/y]` are alpha-equivalent and have smaller
  rank. Their inductive alpha-identity proof, followed by forall-left on A and
  forall-right on A', gives the result. The eigenvariable z is fresh for the
  conclusion `A=>A'`.
- If `A=exists x B` and `A'=exists y B'`, use the same smaller-rank instance
  proof, then exists-right on A' and exists-left on A. Its eigencondition holds
  by the same chosen freshness.

All uses of term substitution in this paragraph are the raw total least-fresh
operation. The inductive hypothesis relates the resulting literal alpha-variants,
so no literal substitution-composition identity has been smuggled in.

## Realizing the final alpha-proof at literal representatives

Prove by induction on a reduction-free alpha-proof that **any** chosen literal
representatives of its endsequent occurrences have a reduction-free raw proof.

- At an alpha-Id leaf, the two chosen representatives need only be alpha-equivalent.
  Use the literal alpha-identity proof just constructed.
- At bottom-left, the chosen bottom representative is the literal bottom, so
  use the registered bottom-left leaf with the chosen remaining context.
- At WL choose the premise representatives by deleting its weakened occurrence.
  At CL choose both active premise copies to be the *same* literal representative
  of the contracted conclusion occurrence. Induction then permits the exact raw
  structural rule.
- For each propositional logical rule, choose premise active formulas to be the
  literal children of the chosen principal conclusion formula. Copy each shared
  context representative identically to both premises, and keep the recorded
  split partition for implication-left. Induction supplies those literal premises,
  to which the exact raw rule applies.
- For forall-left and exists-right, keep the given witness term and form the
  raw least-fresh instance of the chosen quantified representative. It belongs
  to the required alpha premise class by substitution congruence. Induction
  realizes that literal premise, and the registered rule applies.
- For forall-right and exists-left, use the alpha-rule's eigenparameter and
  form the raw instance of the chosen quantified representative. Alpha-equivalent
  formulas have the same free variables, so the eigenparameter remains fresh
  for the chosen literal conclusion. Again the instance is in the required
  premise class, and induction supplies its exact literal derivation.

These cases exhaust the reduction-free grammar. This realization can increase
height, especially at alpha-Id leaves. It is performed **once after the entire
alpha-level normalization**, never inside a same-rank multicut-height argument.
Choosing the original literal endsequent as representatives therefore proves
Cut and Mix elimination for the exact registered `sheet:lj`.

## Writer integration checklist

This is a construction inventory, not an independent review checklist:

- State the auxiliary alpha-class stage and the lack of a final height bound.
- Require both local inputs to contain neither Cut nor Mix.
- State that marks select occurrences, allowing unmarked A in Gamma and Pi.
- Keep the zero-mark padding convention derived, not a new Mix rule.
- Use residual cleanup before lower-rank principal reductions.
- Retain all seven left permutations, all right-rule families above, and all
  five logical principal families with both disjunction injections.
- Retain bottom-succedent replacement and raw alpha-identity realization.
- Preserve exactly one succedent everywhere; do not transfer the LK_d empty
  sequent or interpolation claims into this LJ theorem.

No manuscript files, builds, renders, tests or review-board artifacts were
produced by this helper assignment.
