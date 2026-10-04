# Cut elimination for the exact classical defined-negation sheet

Completed constructive support for `historical_first_half`,
9 September 2026, 20:13 UTC. Ownership:
this note and `tmp/pdfs/p07-classical-cut-construction/` only. The body,
annex, rule sheets, drivers and canonical records belong to their assigned
authors and root.

## 1. Exact calculus and source boundary

The complete `handbook/registry/calculi/lk-defneg.tex` was read. Its SHA-256
at this reading is
`EABDAA9FC4BAFB3E65CABA406E65E25DAF1FAF9EA916FF42039E2C0BA445267B`.
The target is `sheet:lk-defneg`, with finite multisets on both sides,
uncontexted identity `B => B`, contextual zero-premise bottom-left,
explicit weakening and contraction, shared contexts in conjunction-right
and disjunction-left, and split contexts in implication-left. Negation is
defined by implication to bottom. There are no equality, primitive-negation,
induction, modal or infinitary rules.

The exact first-order substitution definition
`def:p02-fol-capture-avoiding-substitution` and alpha-equivalence definition
`def:p02-fol-alpha-equivalence` in
`handbook/parts/p02/first-order-syntax-semantics.tex` were also read. They
distinguish literal syntax from alpha-equivalence and choose a least fresh
binder deterministically. Consequently the height induction below is
conducted in an explicitly defined auxiliary alpha-class presentation.
Section 3 proves cut-free realization with any prescribed exact endsequent
representatives. That realization can increase height; it is performed
after the induction and is not used as a hidden height-preserving step.

Here **cut-free** means containing neither Cut nor Mix. The exact registered
Mix deletes selected occurrences, not necessarily every occurrence of the
same formula. The source equivalence proof at `annex:p7.cut.1` was read:
Cut is the case m=n=1; for m,n positive, contract the m selected right
occurrences in the first premise to one and the n selected left occurrences
in the second premise to one, then apply Cut. Context occurrences are
retained. This equivalence is a derivability argument only. It does not
establish the cut-free admissibility proved below.

Primary comparison material actually acquired and read:

Richard Zach, *Cut Elimination and Normalization for Generalized Single and
Multi-Conclusion Sequent and Natural Deduction Calculi*,
[arXiv:2001.00662v2, 31 May 2021](https://arxiv.org/abs/2001.00662v2),
[exact PDF](https://arxiv.org/pdf/2001.00662v2).

- Local PDF: `tmp/pdfs/p07-classical-cut-construction/zach-2021-v2.pdf`.
- 381,620 bytes; 42 pages in this author manifestation.
- SHA-256: `6BBF2EAADB4EE1232246F4508911FBCF5B9CE3F5D6E9B1F30963DD7A15FC82F1`.
- Matching extracted text: `zach-2021-v2.txt`.
- Read extents: §2, Table 1 and the independent-context comparison,
  pp.3–6; §6 through the proof and conjunction example for Theorem 10,
  pp.15–17; all of §13, pp.38–40, including its eigenvariable discussion.

Theorem 10 explicitly supplies a sketch and uses an all-occurrences Mix
with a different branch-rank measure. Section 13 sketches a more general
quantifier method. Neither passage is silently counted as the missing full
proof for this sheet. The construction below supplies every exact-sheet
case syntactically, uses selected occurrence classes, and proves a
formula-rank/input-height induction. It uses no semantic completeness,
resolution-completeness theorem, unproved inversion theorem, or preexisting
cut-elimination theorem. It is not a transcription of the complete
Gentzen, Troelstra–Schwichtenberg or Negri–von Plato presentations.

## 2. Occurrence conventions and structural bookkeeping

A multiset is represented by finitely many occurrence tokens carrying
formulas. In the auxiliary induction these formulas are alpha classes,
as defined in Section 3. Reordering tokens changes nothing. A **selected class** is a
specified subset of those tokens; tokens outside it remain unselected,
even if they carry the same formula. The final sequent forgets these
temporary marks but retains the intended multiplicity of each formula.

For a fixed formula A write

```
D : Gamma => Delta, [A]^m
E : [A]^n, Pi => Sigma
```

where brackets designate selected classes only. The four context multisets
are unrestricted. In particular Gamma, Delta, Pi and Sigma may all contain
unselected occurrences of A. We seek the exact sequent

```
Gamma,Pi => Delta,Sigma.                         (Target)
```

When tracing a selected context occurrence above a rule, retain its
occurrence identity. In a shared-context binary rule it has one selected
ancestor in each premise. In a split-context implication-left it has an
ancestor only in its assigned premise. If the selected conclusion token
is formed by contraction, select **both** contracted ancestors. If that
conclusion token is unselected, both ancestors stay unselected. Auxiliary
formula tokens used to construct an unselected principal formula are
unselected, even if their displayed formula happens to be A.

Three elementary operations are available without Cut or Mix:

1. Add any specified finite multiset on either side by individual WL/WR steps.
2. Replace k copies of a specified finite multiset S, for k>=1, by one
   copy using CL or CR separately for each formula. If S contains r copies
   of B, reduce kr copies to r, not to one. This distinction preserves
   the target's existing multiplicities.
3. Exchange occurrences freely because contexts are multisets.

When copies of S overlap syntactically with active formulas, distinguish
the active tokens until they have been eliminated. Contract context copies
only after the specified active tokens have been removed. Thus coinciding
formulas, such as B=C in a principal case, cause no ambiguity.

## 3. Alpha-class induction and exact-syntax realization

### 3.1 Syntactic alpha facts

Write `cl(B)` for the class of B under the manuscript's syntactic
alpha-equivalence. This is not semantic equivalence. The following facts
follow from its fresh-binder generators and constructor congruence:

- Alpha-equivalent formulas have the same outer connective or quantifier,
  corresponding connective operands are alpha-equivalent, and their free
  variables and logical-symbol counts agree.
- If `Qx B =alpha Qz C` and y is fresh for the two formulas, then
  `B[y/x] =alpha C[y/z]`.
- Capture-avoiding substitution respects alpha-equivalence. Uniform
  variable permutations commute with substitution up to alpha-equivalence.
- If sigma fixes x and x is outside all variables in its ranges, then
  `(B[t/x]) sigma =alpha (B sigma)[t sigma/x]`, after freshening internal
  binders. Substitution for a nonfree variable leaves the alpha class fixed.

For completeness, these are syntax inductions. An alpha generator renames
one quantified binder; choose a common new binder outside the finitely many
formulas and substituted terms involved. Both sides then use that same
binder, and the claims reduce to the matrix induction hypothesis. A
generator strictly inside a connective or quantifier is handled by
congruence. Reflexivity and symmetry preserve the claims; for transitivity
choose the common fresh binder outside the entire finite chain and apply
transitivity to its matrices. Atomic formulas reduce to the recursive
substitution of terms, bottom is fixed, and binary connectives commute
with substitution. These cases also prove the composition identity by
formula induction. Different least-fresh choices in the literal algorithm
can affect representatives but cannot affect these classes.

### 3.2 The auxiliary calculus

Use the same occurrence-sensitive multiset rules on alpha classes. Id is
the uncontexted `cl(B) => cl(B)`. A quantified class may be displayed using
any representative `Qx B`; its active instance is `cl(B[t/x])`. A
forall-right or exists-left eigenparameter is absent from the free variables
of the entire conclusion class sequent. This is well-defined by Section 3.1.
It is an auxiliary proof presentation, not an extra rule added to the sheet.

Every exact registered proof maps to an auxiliary proof of the same tree
height by replacing its formula tokens with their alpha classes. In
Sections 4–11, formulas and equalities denote this auxiliary presentation
unless an exact representative is explicitly mentioned. Its height, not
the height after syntactic realization, is used in the Mix induction.

### 3.3 Renaming and substitution in the auxiliary calculus

**Renaming lemma.** A uniform permutation of individual variable names
throughout an auxiliary proof, including all terms and rule parameters,
preserves its height and all rule instances. Induct on the proof: the
substitution/permutation equality holds on classes, and a bijection
preserves absence from the free variables of a conclusion. Id,
bottom-left, structural rules and the shared/split arrangements are
unchanged. This would not justify arbitrary independent changes of
literal representatives in an exact Id sequent.

Consequently an eigenparameter y can be replaced in its entire premise
proof and rule annotation by z fresh for that proof and any further finite
data. Apply the transposition of y,z to the premise. Since y is not free
in the inference's conclusion and z is fresh, its conclusion **classes**
are unchanged. This supplies height-preserving local freshening before
contexts from another proof are added.

**Substitution lemma.** For a finite simultaneous substitution sigma of
terms for free individual variables, a cut-free auxiliary proof of
`Gamma => Delta` yields one of `Gamma sigma => Delta sigma` of the same
height. Occurrence selections are transported even if distinct formulas
become equal. One-variable substitution is the case needed below.

Here simultaneous substitution replaces each listed free variable by
its assigned term once, without substituting again inside an inserted
term. It commutes with term/function and logical constructors and freshens
quantifier binders to avoid all range variables. Section 3.1 makes the
resulting alpha class independent of the fresh representatives. Exact
one-variable instances at realization use the sheet's least-fresh algorithm.

Induct on proof height. Id becomes `cl(B sigma) => cl(B sigma)`;
bottom-left retains bottom. Each weakening and contraction remains the
same rule, and each of the six propositional rules follows by substitution
in its premises, with shared contexts still identical and split contexts
still concatenated in the same way.

At forall-left and exists-right, choose the bound variable x fresh for
the domain and range variables of sigma. The active premise after the
induction hypothesis is `cl((B sigma)[t sigma/x])` by Section 3.1, and the
same quantifier rule is reapplied. At forall-right and exists-left,
additionally freshen the eigenparameter z outside the domain and range
variables of sigma and the finite proof data. Sigma fixes z, and the
active instance becomes `cl((B sigma)[z/x])`. The substituted conclusion
is z-free because neither its old free variables nor sigma's ranges
introduce z. Reapply the eigenvariable rule. These are all four quantifier
cases. Each has the original tree shape, hence the original auxiliary
height.

In particular `[t/y]` can be applied to a cleaned premise proof after
freshening its internal eigenparameters. Retained conclusion classes in
which y is not free are fixed. Formula rank is invariant under term
substitution. No exact height-preserving alpha-conversion rule and no
Cut admissibility have been assumed.

### 3.4 Exact cut-free identity between alpha-equivalent formulas

If `B =alpha C`, there is a cut-free **exact-sheet** proof of `B => C`.
Prove this simultaneously for both orientations by induction on formula
rank, using the constructor facts from Section 3.1.

- For an atom, alpha-equivalence is literal equality of its free term
  syntax, so use Id. For bottom use Id or bottom-left.
- For `B=B1 and B2`, `C=C1 and C2`, the two inductive proofs
  `Bi => Ci`, followed by left weakening with the other B operand and
  conjunction-left, give `B => C1` and `B => C2`. Conjunction-right
  gives `B => C`.
- For disjunction, from `Bi => Ci` use right weakening with the other
  C operand and the sheet's single disjunction-right rule to get
  `Bi => C`. Disjunction-left combines the two results to `B => C`.
- For implication, use the inductive proofs `C1 => B1` and `B2 => C2`.
  Split implication-left gives `B1->B2,C1 => C2`, and implication-right
  gives `B1->B2 => C1->C2`.
- For `B=forall x U`, `C=forall z V`, choose y outside all variables
  in B,C. The exact formulas `U[y/x]` and `V[y/z]` are
  alpha-equivalent and have smaller rank. Their inductive identity,
  followed by forall-left with witness y and forall-right with
  eigenparameter y, proves `B => C`. The eigenparameter is absent
  from the exact conclusion's free variables.
- For `B=exists x U`, `C=exists z V`, the same smaller-rank identity
  followed by exists-right with witness y and exists-left with
  eigenparameter y gives `B => C`.

Every displayed instance uses the exact least-fresh substitution value;
alpha-equivalence is used only to invoke the smaller-rank induction.
There is no Cut. These identity proofs may have positive height even
though the auxiliary identity is an initial rule.

### 3.5 Exact realization with prescribed endsequent representatives

**Realization lemma.** For a cut-free auxiliary proof P, choose an arbitrary
exact representative for each occurrence of each class in its endsequent.
There is a cut-free registered-sheet proof of exactly those chosen
antecedent and succedent multisets.

Induct on the height of P. If its last rule is Id, its two prescribed
representatives can differ; use Section 3.4. If bottom-left, bottom's
class has the literal representative bottom and the prescribed sequent
is a registered bottom-left instance.

At weakening, choose the already prescribed new occurrence and realize
the premise with the other prescribed tokens, then weaken. At contraction,
prescribe **two identical copies** of the contracted conclusion's exact
representative in the premise; realize that premise and apply the exact
contraction. Copies of uncontracted context tokens keep their prescribed
representatives.

At a logical rule, decompose its prescribed principal formula into its
actual operands. Choose those exact operands as the active premise
representatives. In the shared rules give corresponding context tokens
the same prescribed representatives in every premise. In split
implication-left distribute the prescribed context tokens as the
auxiliary inference does. Realize the one or two premises recursively
and reapply exactly that logical rule. This covers the six propositional
rules and makes their matching requirements literal.

For forall-left and exists-right, retain the auxiliary proof's witness
term t. If the prescribed principal representative is `Qx U`, prescribe
the exact formula `U[t/x]` in its premise. Section 3.1 ensures this has
the required premise class, even if the auxiliary inference displayed
a differently named binder. Realize the premise and apply the sheet rule.

For forall-right and exists-left, first freshen the auxiliary inference's
eigenparameter y for every variable in the prescribed endsequent and
the finitely many chosen data. Section 3.3 changes its premise proof
without changing its auxiliary height or conclusion. If the prescribed
principal is `Qx U`, prescribe the exact active formula `U[y/x]` and the
given context representatives in its immediate premise. Their classes
match the freshly renamed auxiliary premise. Apply the realization
induction to that strictly shorter auxiliary proof, then reapply the
registered eigenvariable rule. Freshness holds literally for the
prescribed conclusion. No nonexistent alpha-conversion inference is used.

This completes every cut-free rule. The output's physical height need
not equal ht(P), because initial alpha identities can require several
steps. The lemma is used after auxiliary Mix elimination, never to
justify a same-rank height decrease during that elimination. In
particular it realizes the final conclusion using the exact original
endsequent strings, not merely some alpha-equivalent substitutes.

## 4. Selected right-bottom erasure

**Lemma.** Given a cut-free proof F of `Theta => Lambda,[bottom]^k`, for
any selected class of k>=0 succedent occurrences, there is a cut-free proof
of `Theta => Lambda` of height at most ht(F). Unselected bottom tokens,
including logical auxiliaries, are retained.

Induct on F's height, with the selected class part of the induction data.

- If k=0, keep F.
- If F is Id, a nonempty selected class is possible only for
  `bottom => bottom`. Replace it by the zero-premise bottom-left instance
  `bottom =>`.
- If F is bottom-left, the same left bottom token remains, so the
  erased endsequent is another bottom-left instance.
- At WR whose new token is selected, erase the selected old tokens in
  the premise by induction and omit this WR. At unselected WR, erase
  the selected old tokens and reapply the WR to its unselected token.
- At CR whose contracted conclusion token is selected, mark both
  ancestors, erase them by induction and omit this CR. At unselected
  CR, leave both ancestors unselected, erase the other selected tokens,
  and reapply CR to those two retained tokens.
- WL and CL act only on the antecedent: erase the selected succedent
  context tokens by induction and reapply the same rule.
- No logical right rule has bottom itself as its principal formula.
  Thus all selected bottom tokens of a logical conclusion are context
  tokens. At a unary logical rule, erase their ancestors and reapply
  the rule with its active tokens retained. At shared conjunction-right
  or disjunction-left, erase the corresponding context tokens in both
  premise proofs; the remaining contexts still match. At split
  implication-left, erase the selected tokens in whichever premises
  contain their ancestors, and reapply that split rule. Its active
  positive or negative formula is retained even when it is bottom.
- The four quantifier rules are included in that logical treatment.
  Instantiation terms and active instances are unchanged. For
  forall-right and exists-left, removing context formulas cannot
  introduce a free eigenparameter in the conclusion.

These are all cut-free rules. An erased structural rule lowers height;
otherwise one rule is reapplied above premise proofs of no greater
height. Hence the result has height at most ht(F). This proof never
deletes all syntactically equal bottom formulas indiscriminately.

## 5. Strengthened admissibility statement and induction

**Marked Mix lemma.** For every formula A, every two cut-free proofs D,E
as in Section 2, and every m,n>=0, there is a cut-free proof of Target.
This lemma is first proved in the auxiliary alpha-class presentation.
For m,n>=1, exact realization then gives the registered Mix conclusion
with its prescribed representatives. Zero multiplicities are a convenience
in the admissibility lemma, not a new primitive rule.

If m=0, D already proves `Gamma => Delta`; weaken with Pi and Sigma.
If n=0, E already proves `Pi => Sigma`; weaken with Gamma and Delta.
If both vanish, either construction works. These branches terminate
immediately and can ignore the other premise proof.

For positive multiplicities use well-founded induction on

```
(rank(A), ht(D)+ht(E)),                          (Measure)
```

lexicographically. Rank is the manuscript's number of logical symbols;
any of the standard rank conventions for atoms/bottom works provided
every proper matrix or immediate connective operand has smaller rank.
Height is zero for the two initial rules and one plus the maximum premise
height otherwise. The induction hypothesis quantifies over **all**
contexts, multiplicities, selected classes and cut-free input proofs.
It imposes no bound on the height of its constructed output.

The following sections exhaust the final-rule pairs. Initial and
structural cases are resolved first. If a last logical rule does not
create a selected token, commute on that side. Only when both last rules
create selected logical principal tokens do the principal cases apply.

## 6. Every initial case

With m,n positive:

| Last proof | Construction of Target |
| --- | --- |
| D is Id | It must be `A => A`, so m=1, Gamma is one A and Delta empty. In E contract its n selected left A tokens to one. The resulting `A,Pi => Sigma` is Target. |
| E is Id | It must be `A => A`, so n=1, Pi empty and Sigma one A. Contract D's m selected right A tokens to one, obtaining `Gamma => Delta,A`, exactly Target. |
| D is bottom-left | Its antecedent bottom remains in Gamma and hence in Target. Target is directly an instance of bottom-left. |
| E is bottom-left and has a retained antecedent bottom | That retained token lies in Pi, so Target is directly bottom-left. |
| E is bottom-left and has no retained antecedent bottom | Every antecedent bottom token is selected, so A is bottom. Erase the m selected succedent bottom tokens from D by Section 4; then weaken with Pi and Sigma. |

When m or n is zero, Section 5 already covers every initial combination.
The uncontexted Id rule was not replaced by a contexted identity axiom.
The contextual bottom-left rule is used exactly as it appears on the sheet.
No appeal to soundness or underivability of bottom is needed.

## 7. Every structural commuting case

Choose either side whose last inference is structural. Its immediate
premise is strictly shorter than the chosen original proof, so every
same-formula recursive call below has smaller Measure.

| Last structural rule | Mark propagation and reconstruction |
| --- | --- |
| D ends in WR creating a selected A | Use the same E and D's premise with m-1 selected right tokens; omit this WR afterward. The m-1=0 boundary is legitimate. |
| E ends in WL creating a selected A | Use D and E's premise with n-1 selected left tokens; omit this WL. |
| D ends in CR forming a selected A | Select both contracted ancestors, making m+1 selected tokens in D's premise. Apply the induction hypothesis there and omit CR. |
| E ends in CL forming a selected A | Select both ancestors, making n+1 selected tokens in E's premise. Apply induction and omit CL. |
| D ends in unselected WR or CR | Transport the other selected right tokens. Keep the new WR token, or both CR ancestors, unselected; after induction reapply exactly that WR or CR. |
| E ends in unselected WL or CL | The symmetric construction keeps the displayed antecedent token or tokens and reapplies that rule. |
| D ends in WL or CL | These antecedent tokens are never in D's selected succedent class. Apply induction to the premise and reapply the rule. |
| E ends in WR or CR | These succedent tokens are never in E's selected antecedent class. Apply induction to the premise and reapply the rule. |

For example, selected right contraction has the form

```
D0 : Gamma => Delta,[A]^(m+1)
-------------------------------- CR on two selected ancestors
D  : Gamma => Delta,[A]^m,
```

and the recursive problem is simply `(A,D0,E,m+1,n)`. Multiplicity may
increase while height decreases. There is no second same-rank cut on a
newly constructed proof of uncontrolled height. Unselected contractions
on a formula equal to A are handled by the unselected row, not by deleting
their tokens.

## 8. Nonprincipal logical commutations, including all quantifiers

Suppose D's last logical rule has no selected principal token. Mark the
ancestors of its selected succedent context and apply the induction
hypothesis to each immediate premise D_i and the original full E. If
commuting on E, use the original full D with each immediate premise E_i.
Each such pair has a strictly smaller original height sum. A branch with
no selected ancestor uses the zero-multiplicity boundary; it does not
need a fabricated marked formula.

The full reconstruction table is:

| Last rule | Reconstructed operation after recursive calls |
| --- | --- |
| conjunction-left | Keep both displayed antecedent auxiliaries and form their conjunction once. |
| conjunction-right | Apply the recursion in both shared-context premises. Their enlarged contexts agree; apply conjunction-right with that common context. |
| disjunction-left | Apply recursion in both shared-context premises, retaining their distinct active antecedent token. Their enlarged side contexts agree; reapply disjunction-left. |
| disjunction-right | Retain both succedent auxiliaries and form their disjunction once. |
| implication-right | Retain its active antecedent and succedent token; reapply implication-right to those exact tokens. |
| implication-left | Apply recursion in both split-context premises, then reapply split implication-left. This yields two copies of the opposite proof's retained contexts; contract those copies to one. |
| forall-left | Retain the active instance B[t/x] and reapply forall-left with exactly the same term t. |
| forall-right | First freshen its eigenparameter for the entire opposite proof. Retain B[y/x] in the transformed premise, then reapply forall-right. |
| exists-left | First freshen its eigenparameter for the entire opposite proof. Retain B[y/x] in the transformed premise, then reapply exists-left. |
| exists-right | Retain B[t/x] and reapply exists-right with the same term t. |

For clarity the quantified rows yield all eight side-specific cases:

| Last quantifier rule | Commuting on D | Commuting on E |
| --- | --- | --- |
| forall-left | Always nonprincipal for the succedent selection; call `(D0,E)`, restore the retained quantified antecedent. | If its quantified antecedent is unselected, call `(D,E0)` and restore it. |
| forall-right | If its quantified succedent is unselected, rename y outside E, call `(D0,E)`, restore it. | Always nonprincipal for the antecedent selection; rename y outside D, call `(D,E0)`, restore the retained quantified succedent. |
| exists-left | Always nonprincipal for the succedent selection; rename y outside E, call `(D0,E)`, restore the retained quantified antecedent. | If its quantified antecedent is unselected, rename y outside D, call `(D,E0)`, restore it. |
| exists-right | If its quantified succedent is unselected, call `(D0,E)` and restore it. | Always nonprincipal for the antecedent selection; call `(D,E0)` and restore the retained quantified succedent. |

Renaming is performed before the recursive call, preserving the height
of the original premise. The returned proof has the exact prescribed
endsequent. The added contexts therefore contain no free y, and the
original eigenvariable condition holds when the rule is reapplied.
Neither universal-left nor existential-right has an eigenvariable
condition. Their total substitutions remain the same rule instances.

Here is the split implication-left calculation when commuting on D.
Write D's immediate premises as

```
D1 : Gamma1 => Delta1,[A]^m1,B
D2 : C,Gamma2 => Delta2,[A]^m2,
```

where m1+m2=m and the retained conclusion contains `B->C`. The recursive
outputs are

```
Gamma1,Pi => Delta1,Sigma,B
C,Gamma2,Pi => Delta2,Sigma.
```

The registered split rule gives

```
B->C,Gamma1,Gamma2,Pi,Pi => Delta1,Delta2,Sigma,Sigma.
```

Contract the two Pi and Sigma copies to get Target. On E the same
calculation duplicates Gamma and Delta instead. In the shared binary
rules, the opposite contexts occur in both premise sequents but are
shared by the final rule, so they occur only once in its conclusion;
no additional contraction is needed there.

All active tokens of a nonprincipal logical inference are retained.
Deleting an active token merely because it has formula A would not be
this induction and can make the original logical rule impossible to
reapply.

## 9. Residual cleaning before a principal reduction

The remaining situation has a selected principal A introduced by D's
last right rule and by E's last left rule. Other selected occurrences
of A may remain as side context. Set

```
S = Gamma,Pi,      T = Delta,Sigma.
```

For every immediate premise D_i of D, its selected A ancestors are the
residual m-1 context tokens, except that split arrangements distribute
the relevant class as specified by the rule. Its newly active proper
subformula tokens are unselected. Apply the same-A induction hypothesis
to D_i and the **original full E**, deleting that residual class and E's
n selected tokens. This call has

```
ht(D_i)+ht(E) < ht(D)+ht(E).
```

Similarly apply the same-A hypothesis to the **original full D** and
each E_j, deleting all m selected D tokens and E_j's residual class.
That call has smaller height sum because E_j is an immediate premise.
If a residual class has size zero, use the zero branch of the lemma.
Do not first weaken an immediate premise and then use its enlarged
height as though it were the original smaller input.

After each recursive call has returned a cut-free proof, use weakening
to fill out any missing retained context, producing premises with the
common S,T displayed in Section 10. In a split rule a premise contains
only part of Pi or Sigma; this is where the missing part is added.
The newly enlarged output height is unrestricted. It is never used in
another same-rank recursive call in this principal construction.

The remaining compositions use only formulas of rank strictly smaller
than rank(A). The outer induction therefore applies to the cleaned
proofs regardless of their heights. This separates the two valid
decreases and removes the contraction-sensitive gap in a naive
single-cut height argument.

## 10. Every principal/principal reduction

The following lower-rank compositions mean calls to the already proved
smaller-rank Mix admissibility hypothesis, not primitive Cut steps left
in the output. Select only the one displayed active token at each such
call. Other equal formulas inside S,T remain unselected.

### 10.1 Conjunction A=B and C

The last rules are conjunction-right and conjunction-left. Residual
cleaning yields cut-free proofs of

```
S => T,B             S => T,C             B,C,S => T.
```

Mix the first and third on the displayed B, obtaining
`C,S,S => T,T`. Mix the second with this on its displayed C, obtaining
`S,S,S => T,T,T`. Contract the three copies to `S => T`.
The two formulas B,C have smaller rank than A. If B=C, the two active
tokens in the third premise are still selected and consumed separately.

### 10.2 Disjunction A=B or C

The sheet's disjunction-right has **one premise containing both**
succedent auxiliaries; disjunction-left has two shared-context premises.
Cleaning yields

```
S => T,B,C             B,S => T             C,S => T.
```

Mix the first and second on B to obtain `S,S => T,T,C`. Mix this
with the third on C to obtain `S,S,S => T,T,T`, then contract.
No single-injection version of disjunction-right is assumed.

### 10.3 Implication A=B->C

D's immediate premise has shape
`B,Gamma => Delta,[A]^(m-1),C`. E's split implication-left premises have
the shape

```
E1 : [A]^n1,Pi1 => Sigma1,B
E2 : C,[A]^n2,Pi2 => Sigma2,
```

where n1+n2=n-1, Pi=Pi1,Pi2 and Sigma=Sigma1,Sigma2. Cleaning D's
premise against E gives `B,S => T,C`. Cleaning E1 and E2 against D,
then adding their missing context portions by weakening, gives

```
S => T,B             C,S => T.
```

Mix the positive B proof with `B,S => T,C` on B to obtain
`S,S => T,T,C`. Mix that with `C,S => T` on C to obtain
`S,S,S => T,T,T`, then contract. The same-A calls used only the
original D/E immediate premises; both later calls have smaller formula
rank. This treats the sheet's split implication-left exactly.

### 10.4 Universal A=forall x B

The original final inferences have immediate premises

```
D0 : Gamma => Delta,[A]^(m-1),B[y/x]        (forall-right)
E0 : B[t/x],[A]^(n-1),Pi => Sigma          (forall-left).
```

Before proceeding, rename D's eigenparameter y to a variable absent
from the entire E proof, t and all retained contexts. It was already
absent from the free variables of D's conclusion, including all
occurrences of A. Thus y is not free in S,T or A. Bound formula variables
are consistently freshened as needed for the total substitution identity.

Apply the same-A smaller-height calls

```
Mix_A(D0,E; m-1,n)       gives F : S => T,B[y/x],
Mix_A(D,E0; m,n-1)       gives G : B[t/x],S => T.
```

Both calls are valid even when m=1 or n=1 because zero classes are part
of the strengthened lemma. Freshen internal eigenparameters of F away
from t and apply the independent substitution lemma to F with [t/y].
The contexts S,T do not change; the active formula becomes B[t/x].
Obtain

```
F[t/y] : S => T,B[t/x].
```

Its lower-rank Mix with G produces `S,S => T,T`; contract to Target.
Term substitution preserves logical rank, so
`rank(B[t/x])=rank(B)<rank(forall x B)`. There is no claim that the
cleaned proof's height is smaller than an original premise.

### 10.5 Existential A=exists x B

The final premises are

```
D0 : Gamma => Delta,[A]^(m-1),B[t/x]       (exists-right)
E0 : B[y/x],[A]^(n-1),Pi => Sigma         (exists-left).
```

Freshen E's eigenparameter y for the entire D proof and t. It is then
not free in S,T,A. Residual cleaning gives

```
Mix_A(D0,E; m-1,n)       gives F : S => T,B[t/x],
Mix_A(D,E0; m,n-1)       gives G : B[y/x],S => T.
```

Freshen G's internal eigenparameters away from t, then substitute t
for y throughout G. Its endsequent is `B[t/x],S => T` with the same
retained contexts. The lower-rank Mix of F and G[t/y] gives
`S,S => T,T`, and contraction gives Target. Again the rank falls
strictly while the transformed proof height is unrestricted.

There is no logical principal/principal case for an atomic A or for
bottom: no right logical rule introduces either. Bottom's exceptional
initial case was settled by the independently proved erasure lemma.
The five cases above therefore exhaust all logical principal pairs.

## 11. Exact decrease and termination argument

Every recursive call in the marked Mix construction has strictly smaller
Measure than its parent call:

| Case | Reason |
| --- | --- |
| Zero multiplicity or an initial rule | No recursive Mix call; only the independently terminating bottom erasure or finitely many structural steps. |
| A structural commutation | Same rank, one original proof replaced by its immediate premise; multiplicity can grow without affecting the decrease. |
| A nonprincipal logical commutation | Same rank, one immediate premise replaces its original proof; one or two separate calls each have smaller height sum. |
| Residual cleaning of a principal pair | Same rank, immediate premise on one side against the original full proof on the other. The strict input-height inequality is explicit in Section 9. |
| Composition of cleaned principal auxiliaries | A proper operand/matrix instance has lower rank; any finite constructed input heights are permitted. |

Structural padding and contraction are finite operations performed after
the appropriate recursive calls. Eigenparameter freshening is performed
before the call or inference that needs its freshness. None creates an
additional same-rank recursive problem on the larger output. Well-founded
recursion on pairs of natural numbers therefore yields a finite cut-free
output for every input of the strengthened lemma. This is a measure of
recursive problems. It is not asserted to decrease globally after every
arbitrary local rewrite of an entire proof tree.

To eliminate every Cut and Mix in a finite exact derivation, map it first
to its auxiliary alpha-class proof, preserving its tree height. Perform
structural recursion on that auxiliary proof. First eliminate them from its
immediate premise derivations. At an ordinary rule, reapply that rule;
the premise endsequents have not changed, so its side conditions remain
valid. At Cut or registered positive-multiplicity Mix, call the proved
marked Mix construction on the now cut-free premise proofs. The returned
proof is cut-free and has exactly the original inference's conclusion.
The outer structural recursion terminates, and each inner Mix construction
terminates by Measure. This gives a cut-free auxiliary proof of the same
endsequent classes. Finally apply the independent realization lemma with
the exact original endsequent as the prescribed representatives. Its
output is a registered-sheet cut-free proof of that exact endsequent.
The possibly increased physical height of realization is irrelevant to
the already completed well-founded induction.

No inversion theorem, semantics, NJ normalization or other form of the
cut theorem is used as a premise. Cut/Mix equivalence identifies the
rule surfaces; marked Mix admissibility is proved independently and
therefore does not use that equivalence circularly.

## 12. Concrete boundaries that the final authoring must retain

- Surviving copies of A in Delta or Pi, and in the opposite sides Gamma
  or Sigma, remain ordinary context tokens throughout. The induction
  never deletes all formulas merely by syntactic equality.
- In a principal case, residual copies are removed **before** the
  lower-rank composition. A repeated same-rank Cut on a transformed
  output of unknown height would not be justified by Measure.
- Weakening to align S,T occurs after the same-rank immediate-premise
  call. Its added steps must not be hidden in the claim that this
  recursive input is an immediate subproof.
- Eigenparameter renaming occurs before adding contexts or making the
  relevant recursive call; it is not a repair applied to an already
  invalid forall-right or exists-left inference.
- Renaming and substitution preserve the height of the auxiliary
  alpha-class proof. Arbitrary exact representative changes do not in
  general preserve physical proof height: even auxiliary Id can require
  a positive-height exact alpha-identity derivation. Realization is
  explicitly postponed until after the height induction.
- In bottom erasure and nonprincipal commutations, active auxiliaries
  remain unselected, including auxiliaries whose formulas equal bottom
  or A. The erased result must still instantiate the actual last rule.
- Both uncontexted Id and contextual bottom-left are treated directly.
  No contexted Id or equality rule is imported.
- The result is a specified terminating elimination construction. No
  claim of strong normalization of every arbitrary proof rewrite or a
  quantitative proof-size bound is made.

This note supplies constructive authoring material for the exact classical
sheet. No independent review, manuscript build, render or prose-test suite
has been run. The author owns incorporation into the new body and annex.

The complete written note was read through against the actual rule sheet,
the exact syntax definitions and the source's stated boundary. Every
same-rank call uses an original immediate premise before structural
padding; every call on a constructed principal auxiliary has lower
formula rank. The exact initial cases, marked bottom erasure, all eight
quantifier commutations, both quantified principal cases and exact final
realization have no remaining construction gap in this assigned subtask.
