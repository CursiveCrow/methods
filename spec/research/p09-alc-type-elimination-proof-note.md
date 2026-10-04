# ALC type elimination for arbitrary finite TBoxes and ABoxes

Date: 2026-09-06.

## Scope and result

This is a supplied finite type-elimination procedure for exactly the
language and interpretations of `def:p09-alc` in
`handbook/parts/p09/logic-in-computer-science.tex`.
Its input is a finite TBox `T`, a finite ABox `A`, and an optional
tested concept `C_0` whose extension must be nonempty in the same model.

The concept constructors are

\[
\top,\bot,P,\neg C,C\sqcap D,C\sqcup D,\exists r.C,\forall r.C.
\]

The TBox contains arbitrary general concept inclusions `C subseteq D`.
The ABox contains concept assertions `C(a)` and positive role
assertions `r(a,b)`. Domains are nonempty. Individual names may denote
the same element; there is no unique-name assumption. No negative
role assertions, inequalities, number restrictions, inverse roles,
or additional role conditions are part of this input.

The procedure accepts exactly when the input has a model, including
the optional tested-concept requirement. Every accepted input has a
model with at most `2^m` elements, where `m` is the size of the finite
concept closure. With ordinary finite input length `N>=1`, including
the fixed delimiters of an empty input, `m=O(N)`. The explicit
deterministic procedure below runs in `2^{O(N^2)}` time; this is a
sufficient exponential-time bound, not an asserted optimal exponent.

## 1. NNF and a linear-size dual-closed closure

Use the structural negation normal form from the live host: negation
occurs only immediately before a concept name. For an NNF concept
`D`, write `bar D` for its NNF complement, defined by

\[
\begin{aligned}
\bar\top&=\bot,&\bar\bot&=\top,&\bar P&=\neg P,&\overline{\neg P}&=P,\\
\overline{D\sqcap E}&=\bar D\sqcup\bar E,
&\overline{D\sqcup E}&=\bar D\sqcap\bar E,\\
\overline{\exists r.D}&=\forall r.\bar D,
&\overline{\forall r.D}&=\exists r.\bar D.
\end{aligned}
\]

Choose this syntax so that `bar(bar D)=D`. Structural induction using
Boolean complementation and the two modal dualities proves, for every
interpretation `I`,

\[
\operatorname{nnf}(C)^I=C^I,
\qquad
(\bar D)^I=\Delta^I\setminus D^I.
\tag{1}
\]

For every GCI `C subseteq D`, form the global NNF concept

\[
g_{C,D}=\operatorname{nnf}(\neg C\sqcup D).
\]

Let `G` be the finite set of these concepts. Let `B` contain `G`,
every normalized concept in an ABox concept assertion, the normalized
`C_0` if present, and `top,bot`. Define

\[
\Sigma=\operatorname{Sub}(B)
       \cup\{\bar D:D\in\operatorname{Sub}(B)\}.
\tag{2}
\]

Here `Sub(B)` contains all syntactic sub-concepts, including each
member of `B` itself. This set is closed under sub-concepts and under
the NNF dual: sub-concepts of a dual are duals of corresponding
sub-concepts. Write `m=|Sigma|`.

NNF conversion changes neither modal depth nor Boolean tree size by
more than a constant factor; it does not distribute conjunctions and
disjunctions. Internalizing one GCI adds one disjunction while using
one copy of each operand. Taking sub-concepts and their duals therefore
gives `m=O(N)`. If raw input size is instead counted with the empty
input having length zero, the equivalent statement is `m=O(N+1)`.

The role names and individual names used by the procedure are just
those occurring in the input. Role-only ABox assertions add no new
concepts to (2).

## 2. Complete Boolean types and role compatibility

A candidate type is a subset `t subseteq Sigma` satisfying all of:

1. Exactly one of `D,bar D` belongs to `t`, for every `D in Sigma`.
2. `top in t` and `bot notin t`.
3. For each `D sqcap E in Sigma`, it belongs to `t` iff both `D,E`
   belong to `t`.
4. For each `D sqcup E in Sigma`, it belongs to `t` iff at least one
   of `D,E` belongs to `t`.
5. Every global GCI concept in `G` belongs to `t`.

Let `S_0` be the set of all candidate types. It is obtained by
enumerating the at most `2^m` subsets of `Sigma` and testing these
finite conditions. The word "complete" here refers to deciding each
concept/dual pair in this finite closure, not every concept in the
entire language.

For each input role `r`, define compatibility by

\[
t\longrightarrow_r u
\quad\Longleftrightarrow\quad
\text{for every }\forall r.D\in t,\ D\in u.
\tag{3}
\]

This is an effectively testable relation between candidate types.
It records all universal requirements on a possible `r`-successor.
It does not by itself assert that a successor exists.

## 3. Descending elimination

Define successively

\[
S_{j+1}=\{t\in S_j:
  \text{for every }\exists r.D\in t\text{ there is }u\in S_j
  \text{ with }t\longrightarrow_r u\text{ and }D\in u\}.
\tag{4}
\]

Stop when `S_{j+1}=S_j`, and write `S_*` for the resulting fixed set.
The sequence descends within the finite set `S_0`. There are at most
`|S_0|` strict deletion rounds; a final equality check detects
stabilization. In particular, if it becomes empty it is already fixed.

All existential obligations in a surviving type have compatible
witnesses in `S_*`. These witnesses may be the type itself. Cyclic
TBoxes and cyclic witness patterns are therefore handled without
requiring acyclic terminology or finite unfolding trees.

## 4. Acceptance, including named assertions and the optional test

Let `Ind(A)` be the set of individual names appearing anywhere in the
ABox, including role assertions. The procedure accepts iff:

- `S_*` is nonempty;
- there is a function

  \[
  f:\operatorname{Ind}(\mathcal A)\longrightarrow S_*
  \]

  such that each `C(a)` in the ABox has `nnf(C) in f(a)`, and each
  `r(a,b)` in the ABox has `f(a) ->_r f(b)`;
- if `C_0` is present, some type in `S_*` contains `nnf(C_0)`.

This finite function search is performed deterministically by
enumerating all assignments. The function need not be injective.
Repeated uses of the same name use its one assigned type.

When there are no individual names, there is one empty assignment.
The separate nonemptiness condition is still required. The tested
concept, when present, need not hold at a named individual; it has
its own existential point requirement in the same canonical model.

## 5. Accepted input yields a finite canonical model

Assume acceptance and choose one accepted name assignment `f`.
Define `I_*` by

\[
\Delta^{I_*}=S_*.
\]

For each concept name occurring in `Sigma`, set

\[
P^{I_*}=\{t\in S_*:P\in t\}.
\tag{5}
\]

For every input role, set

\[
r^{I_*}=\{(t,u)\in S_*^2:t\longrightarrow_r u\}.
\tag{6}
\]

Interpret an input individual `a` as `f(a)`. Unmentioned concept
names and roles can be empty, and any unmentioned individual names
can denote one fixed member of the nonempty set `S_*`.

The use of every compatible edge in (6) is safe. It satisfies all
positive existential requirements while respecting every universal
constraint stored in the source type. The dual obligations will
also ensure the converse directions of the truth lemma.

### Truth lemma

For every `D in Sigma` and every `t in S_*`,

\[
t\in D^{I_*}\quad\Longleftrightarrow\quad D\in t.
\tag{7}
\]

Prove this simultaneously for all closure concepts by their logical
complexity. Atomic names have the interpretation (5). For a negated
name, exact dual choice makes `not P in t` equivalent to `P notin t`,
which matches its complement semantics. Top and bottom have their
fixed interpretations, and the conjunction/disjunction cases are
exactly type conditions 3 and 4 plus the induction hypothesis.

For an existential `exists r.D`:

- If `exists r.D in t`, fixed-point survival supplies `u in S_*`
  with `t ->_r u` and `D in u`. By induction, `u in D^{I_*}`; the
  edge (6) makes the existential true at `t`.
- If `exists r.D notin t`, dual completeness puts `forall r.bar D`
  in `t`. Every compatible successor `u` therefore contains `bar D`.
  By induction and (1), it does not satisfy `D`. Thus there is no
  `r`-successor satisfying `D`, and the existential is false.

For a universal `forall r.D`:

- If `forall r.D in t`, every edge from `t` in (6) leads to a type
  containing `D`, hence by induction to a point satisfying `D`.
  The universal is true, including the case of no such edges.
- If `forall r.D notin t`, its dual `exists r.bar D` belongs to
  `t`. Survival supplies a compatible `u` containing `bar D`.
  Induction gives an actual `r`-successor falsifying `D`, so the
  universal is false.

Each filler `D` or `bar D` used here has smaller logical complexity
than the modal concept being proved. No same-complexity circularity
is introduced by the dual cases. These steps complete the induction.

### TBox, ABox, and tested concept

Every surviving type contains every `g in G`. By (7), all canonical
points satisfy those concepts. Equation (1) then gives
`C^{I_*} subseteq D^{I_*}` for every GCI `C subseteq D` in the TBox.

The conditions on `f` and (7) satisfy every ABox concept assertion.
Each asserted role pair is an edge by (3), (6), and the acceptance
test, so all role assertions hold. The optional chosen type containing
`nnf(C_0)` satisfies `C_0` by (1) and (7). These requirements all
hold in this one model, not in separately chosen models of the
individual types.

Finally,

\[
1\leq|\Delta^{I_*}|=|S_*|\leq|S_0|\leq2^m.
\tag{8}
\]

No extra elements are added for names. This uses the absence of a
unique-name assumption and the precise ABox language in the host.

## 6. Any model makes the procedure accept

Conversely, suppose `I` satisfies the knowledge base and the optional
tested concept has nonempty extension when present. Its domain may
be infinite. For every domain point `x`, define its closure type

\[
\tau_I(x)=\{D\in\Sigma:x\in D^I\}.
\tag{9}
\]

Boolean semantics and (1) give exact dual choice and the Boolean
conditions. The TBox makes each global GCI concept true at every
point, so `tau_I(x) in S_0` for every `x`.

We prove by induction on `j` that every realized type lies in `S_j`.
The base case was just checked. If `exists r.D in tau_I(x)`, choose
an actual `r`-successor `y` of `x` satisfying `D`. Every universal
`forall r.E` true at `x` is true of this successor's filler, so

\[
\tau_I(x)\longrightarrow_r\tau_I(y),\qquad D\in\tau_I(y).
\]

By the induction hypothesis `tau_I(y) in S_j`, making it a surviving
witness for (4). Thus no realized type is removed. At stabilization
every realized type belongs to `S_*`; nonemptiness of the original
domain makes `S_*` nonempty.

Assign each ABox name `a` the type `tau_I(a^I)`. Its concept
assertions have the required members, and every asserted actual
role edge implies the compatibility test (3). If `C_0` is present,
a point in its extension provides the required survivor containing
its normalized concept. Thus all acceptance conditions hold.

Sections 5 and 6 prove the required equivalence, and Section 5
supplies the finite-model bound.

## 7. Explicit deterministic running-time bound

Let `K=|S_0| <= 2^m`, let `k=|Ind(A)|`, and let `R` be the number
of input role names. Both `k` and `R` are at most `N`.

Candidate types can be listed in `2^m poly(N)` time. Compatibility
for every candidate pair and input role can be tabulated in
`O(R K^2 m)` elementary membership checks. A naive elimination round
checks at most `K m` existential obligations and scans at most `K`
candidate witnesses for each. At most `K` strict rounds plus the
stabilization check give an overall type phase bounded by

\[
\operatorname{poly}(N)\,2^{3m}.
\]

After checking `S_* != empty`, there are at most

\[
|S_*|^k\leq2^{mk}
\]

name assignments. Each is checked against the finitely many ABox
assertions in polynomial time using the compatibility table and
membership bitsets. The optional tested-concept check scans at most
`2^m` types. With no names the assignment count is one; there is no
need to interpret `0^0`, since empty survivors have already rejected.

Combining these estimates gives

\[
\operatorname{poly}(N)\bigl(2^{3m}+2^{mk}igr)
\leq2^{O(N^2)}.
\tag{10}
\]

This is a deterministic `2^{poly(N)}` bound for the combined input.
The type-elimination phase alone has a `2^{O(N)}` bound under these
estimates, but the naive name-assignment enumeration has exponent
`m k`; it is not justified to drop that factor and claim the same
single-linear-exponent bound for the entire displayed procedure.

## 8. Boundary cases and small checks by derivation

### Entirely empty input

With empty TBox and ABox and no tested concept, the host still puts
`top,bot` in `Sigma`. The sole candidate type is `{top}`. It has no
existential obligations and survives. The empty name assignment is
accepted, giving a one-point interpretation. This satisfies the
required nonempty-domain semantics.

If the only input consists of positive role assertions, the same
single type can interpret all names. Each mentioned role's compatibility
relation is unrestricted, so its self-loop satisfies every asserted
edge. No implicit distinct-name constraint is introduced.

### False concepts and impossible global requirements

A tested `bot` cannot occur in a survivor, and an assertion `bot(a)`
cannot pass the name-assignment check. The GCI `top subseteq bot`
leaves no Boolean candidate containing its false global concept.
Each case correctly rejects.

### Universal requirements without successor existence

A type containing `forall r.bot` has no compatible successor, because
no type contains `bot`. This is permitted when no existential along
`r` is required; its canonical role has no outgoing edge there, and
the universal is vacuously true.

If the same type also contains `exists r.top`, it is eliminated for
lack of a compatible witness. In particular, the two GCIs

\[
\top\sqsubseteq\exists r.\top,
\qquad
\top\sqsubseteq\forall r.\bot
\]

make the nonempty-domain TBox unsatisfiable, and all types are removed.

### Cyclic TBoxes

The GCI `P subseteq exists r.P` with assertion `P(a)` permits a
surviving P-type to witness itself. A one-point P-model with an
`r` self-loop satisfies it. Cyclic syntax is not unfolded indefinitely,
and no acyclicity hypothesis is used in the proof.

### Universals absent from a type

Absence of `forall r.D` is not ignored. Exact dual choice forces
`exists r.bar D`, whose surviving witness makes the universal false.
This is the indispensable converse half of the truth lemma when
all compatible pairs are included in the canonical role relation.

Only this proof note was authored. No handbook edits, software tests,
builds, or renders were performed.
