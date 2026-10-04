# Quantified NJ conversions and a terminating normalization strategy

Completed construction for `historical_tail_lead`, 9 September 2026,
19:09 UTC. Ownership is this
note and `tmp/pdfs/p07-nj-quantifier-conversions/` only. No calculus sheet,
manuscript driver, body, annex or canonical record is edited here.

## 1. Exact target and source boundary

The original `handbook/registry/calculi/nj.tex` was read. It requires nonempty
discharge classes for implication introduction, disjunction elimination and
existential elimination. This construction is for the separately authorized
standard calculus `sheet:p07-nj-vacuous`, supplied in
`handbook/registry/calculi/p07-nj-vacuous.tex`: the same finite-tree language
`bottom,and,or,imp,forall,exists`, with defined negation, no RAA, equality or
induction, but discharge classes may be empty. It is not a normalization proof
for the original nonvacuous sheet. The new sheet was read in full after it
was saved: all fourteen rules match this construction, including empty
discharge classes, arbitrary-formula bottom elimination and the strict
existential eigenvariable-absence conditions. Its read snapshot SHA-256 is
`E6CA02133619CF22E231E478A73C2E4901DE43521E177ADDDA8A4EF3DE565118`.

The selected normality condition is the absence, anywhere in a finite
derivation, of the following patterns:

1. A matching introduction immediately supplying an elimination's major premise.
2. A disjunction-elimination or existential-elimination result supplying the
   major premise of any elimination.
3. A bottom-elimination result supplying the major premise of any elimination.

Here the eliminations are the two conjunction projections, implication,
disjunction, universal, existential and bottom elimination: seven concrete
rows. No eta rule, arbitrary introduction commuting rule, permutation from a
minor premise, or atomic-only restriction on bottom elimination is added.
Alpha-renaming is an equality of representations, not an independent
reduction step that can be repeated indefinitely.

The primary proof source actually acquired and read is Philippe de Groote,
*On the Strong Normalisation of Intuitionistic Natural Deduction with
Permutation-Conversions*, author-hosted manuscript corresponding to
*Information and Computation* 178(2), 441–464 (2002). The
[author's publication list](https://members.loria.fr/PdeGroote/publi.html)
identifies this journal paper separately from his 1999 RTA paper and links
the [actual PDF](https://members.loria.fr/PdeGroote/papers/ic02.pdf).

- Local PDF: `tmp/pdfs/p07-nj-quantifier-conversions/de-groote-ic02.pdf`.
- 220,509 bytes; 30 physical pages, numbered 1–30 in this manifestation.
- SHA-256: `1C0FEDCF7F4DBA2C667FE69C6EE2453BB9FAF2848B09695152B61B3D3CCC37A8`.
- Complete extracted text: the matching `de-groote-ic02.txt`.
- Read: the complete paper, including the typing appendix. The relevant
  mathematical locations are Definitions 1–3, 6–10, 13–16, 19–20; Lemmas
  1–20; Theorems 1–3; and Appendix A. Theorem 4 and its postponement argument
  were also read, but the construction below needs only weak normalization
  and does not import that stronger conclusion.

The paper suppresses first-order terms in its proof-term grammar expressly
to obtain a normalization simulation (p.13, footnote 2). Sections 2–6 below
restore the quantifier annotations and discharge conditions needed for the
actual manuscript calculus. Sections 7–10 construct a precise termination
argument using its CPS and arithmetic-norm method. This is a separately
attributed proof route, not a claim that it reproduces the Prawitz 1965 or
Troelstra–Schwichtenberg 2000 maximal-segment proof. Those books' historical
presentation obligations remain with their author. Their complete primary
bodies were not acquired or personally read for this note.

## 2. Proof objects, names and copying

Use proof variables `a,b,c,...` for assumption classes and individual variables
`x,y,z,...` for the first-order language. These alphabets are disjoint. An open
proof variable has one declared formula. Multiple occurrences may have that
declaration; multiple distinct variables may also have the same formula.
An unused declared variable represents an empty discharge class. A proof term
codes a tree, not a shared graph. Removing a branch may shrink the set of open
assumption formulas.

The constructors and their meanings are:

| Proof term | Derivation operation |
| --- | --- |
| `a` | Assumption occurrence |
| `lam a.M` | Implication introduction, binding a in M |
| `M N` | Implication elimination, with M the major premise |
| `pair(M,N)` | Conjunction introduction |
| `pi_1 M`, `pi_2 M` | The two conjunction eliminations |
| `in_1 M`, `in_2 M` | Disjunction introductions, with the missing summand annotated |
| `case(M; a.N; b.O)` | Disjunction elimination, binding a only in N and b only in O |
| `allI(y.M)` | Universal introduction, binding the eigenparameter y in M |
| `allE(M;t)` | Universal elimination with first-order term t |
| `pack(t,M)` | Existential introduction, with existential formula annotated |
| `unpack(M; y,a.N)` | Existential elimination, binding eigenparameter y and assumption variable a only in N |
| `abort_C(M)` | Bottom elimination to the annotated formula C |

All omitted formula annotations are uniquely supplied by the given typing
derivation. An existential elimination has major premise `M: exists x A`,
branch `a:A[y/x] |- N:C`, and result C. Its y is absent from C, every other
open assumption formula, the major premise's open assumptions, and the
existential formula itself, exactly as required by the sheet. When the sheet
requires absence rather than only absence of free occurrences, choose y
fresh for all variable occurrences in those finite formulas. Bound formula
variables can first be alpha-renamed. Universal introduction uses the usual
free-variable condition on every open assumption of its premise.

Before a substitution or permutation, alpha-rename all binders whose scopes
are being enlarged or copied. Choose their names outside the finite set of
names in the target conclusion, retained open assumptions, inserted terms,
auxiliary derivations and their annotations. This operation changes bound
and locally eigen-bound occurrences only; it never renames an external free
individual variable or an open assumption's formula as a shortcut.

Every copied subtree receives fresh internal proof binders, discharge labels
and eigenparameters. Its free proof variables remain the same variables:
these are still open or are discharged by the same surrounding application.
Thus an enclosing discharge may discharge several copied occurrences, or no
occurrences after a branch is erased. Labels from two newly copied internal
discharges must not be conflated.

## 3. The two substitution facts used by the principal conversions

**Individual substitution.** If a derivation concludes B from actual open
assumptions Gamma, replacing a free individual parameter y by a term t in
all formulas and term annotations gives a derivation of `B[t/y]` from
`Gamma[t/y]`, after all internal eigenparameters and formula binders have
been renamed away from the variables of t. The replacement is total
capture-avoiding substitution.

Proof is induction on the last rule. Assumptions and propositional rules
commute with substitution. At universal elimination and existential
introduction, the substituted instantiation is the original instantiation
with its term also substituted; alpha-renaming makes the two substitutions
commute when required. At universal introduction choose its eigenparameter
z distinct from y and outside the variables of t. Since z was absent from
the open assumptions and cannot be introduced by t, its freshness condition
persists. At existential elimination do the same for its eigenparameter z;
z remains absent from the substituted conclusion, major formula and other
open assumptions. The distinguished branch assumption becomes the correct
instance of the substituted existential matrix. Discharge classes do not
change. This covers every rule.

**Proof substitution.** If `Gamma |- M:A` and
`Delta,a:A |- N:C`, grafting a fresh copy of M at every free occurrence of
a in N gives a derivation `N[M/a]:C` whose open assumption formulas are a
subset of `Gamma union Delta`. Only occurrences of the specified assumption
variable/class a are replaced. All internal binders of N are first renamed
away from the free proof variables, individual variables and open assumption
formulas of M. In particular an internal universal introduction or
existential elimination must not retain an eigenparameter that occurs in an
open assumption of M.

Induct on N. At a the result is M; at another assumption it is unchanged.
At nondischarging rules apply the induction hypothesis to each premise and
reapply the rule. At implication introduction and disjunction elimination,
rename their internal binders, apply the hypothesis within the corresponding
premises, and discharge exactly the renamed classes. These classes may
become empty. At universal introduction the chosen fresh eigenparameter
remains absent from the enlarged open support. At existential elimination
the fresh eigenparameter remains absent from M's open support, the final
conclusion and all retained contexts; its branch class is discharged after
grafting. Universal elimination and existential introduction use unchanged
first-order term annotations. Bottom elimination simply reapplies its
declared conclusion. If a has no occurrence, no copy of M is inserted.

These arguments also prove preservation under a surrounding derivation
context. Any enclosing discharge which loses its last occurrence remains
legal precisely because empty classes are licensed in the new calculus.

## 4. Complete principal-conversion table

There are seven concrete principal rows, of which the last two are quantified.

| Major introduction followed by matching elimination | Contractum |
| --- | --- |
| `(lam a.M) N` | `M[N/a]` |
| `pi_1 pair(M,N)` | `M` |
| `pi_2 pair(M,N)` | `N` |
| `case(in_1 M; a.N; b.O)` | `N[M/a]` |
| `case(in_2 M; a.N; b.O)` | `O[M/b]` |
| `allE(allI(y.M);t)` | `M[t/y]` |
| `unpack(pack(t,M);y,a.N)` | `N[t/y][M/a]` |

For the universal row, write the introduced formula as `forall x A`, with
the premise `M:A[y/x]`. The eigenparameter y is fresh for the premise's open
assumptions and is chosen absent from `forall x A`; the introduced formula
`forall y A[y/x]` is alpha-equivalent to `forall x A`. Rename it away from t
and from the enclosing context, without
renaming free occurrences of the old name in t. Individual substitution
then gives `M[t/y]:A[t/x]` with unchanged open assumption formulas. All
internal eigenparameters of M are separately fresh for t.

For the existential row, `M:A[t/x]`, and N proves C under a distinguished
class `a:A[y/x]` plus Delta. Choose y outside t, M, C, Delta and the
existential formula. First substitute t for y throughout N, so the branch
class has exactly formula `A[t/x]`; then graft M at that class. Freshen every
internal eigenparameter of N away from t and Gamma before either operation.
Because y is absent from C and Delta, the final conclusion and retained
open assumptions are unchanged. If a is unused, the major derivation M is
erased, although the individual substitution in N is still performed.
Formula binders are renamed so that
`(A[y/x])[t/y] = A[t/x]` modulo alpha-equivalence.

There is no bottom-introduction rule and hence no principal bottom detour.

## 5. All fourteen permutation rows

Let `D = case(M;a.N;b.O):C` and
`X = unpack(M;y,a.N):C`. The operation following D or X has the displayed
major premise and auxiliary derivations. The row result has the same final
formula as the original following elimination.

| Following elimination | Above disjunction elimination | Above existential elimination |
| --- | --- | --- |
| First projection | `pi_1 D -> case(M;a.pi_1 N;b.pi_1 O)` | `pi_1 X -> unpack(M;y,a.pi_1 N)` |
| Second projection | `pi_2 D -> case(M;a.pi_2 N;b.pi_2 O)` | `pi_2 X -> unpack(M;y,a.pi_2 N)` |
| Implication elimination | `D L -> case(M;a.N L;b.O L)` | `X L -> unpack(M;y,a.N L)` |
| Disjunction elimination | `case(D;c.L;d.R) -> case(M;a.case(N;c_1.L_1;d_1.R_1);b.case(O;c_2.L_2;d_2.R_2))` | `case(X;c.L;d.R) -> unpack(M;y,a.case(N;c.L;d.R))` |
| Universal elimination | `allE(D;t) -> case(M;a.allE(N;t);b.allE(O;t))` | `allE(X;t) -> unpack(M;y,a.allE(N;t))` |
| Existential elimination | `unpack(D;z,c.L) -> case(M;a.unpack(N;z_1,c_1.L_1);b.unpack(O;z_2,c_2.L_2))` | `unpack(X;z,c.L) -> unpack(M;y,a.unpack(N;z,c.L))` |
| Bottom elimination | `abort_B(D) -> case(M;a.abort_B(N);b.abort_B(O))` | `abort_B(X) -> unpack(M;y,a.abort_B(N))` |

Subscripts 1 and 2 mark alpha-renamed copies of the indicated complete
auxiliary derivation, with its distinguished binder renamed as well. An
implication minor L copied into both disjunction branches also receives
fresh internal binders/eigenparameters, even though that copying is omitted
from the compact term notation. The existential column does not duplicate
the auxiliary derivation, but it does enlarge its surrounding scope.

The following conditions cover the individual rows rather than merely
invoking unspecified capture avoidance:

- In the disjunction column, a and b are fresh for all following auxiliary
  derivations. Their scopes grow to include those derivations; free
  assumption occurrences there must not accidentally become discharged.
- In the existential column, both y and a are fresh for all following
  auxiliary derivations, their open assumptions, their term annotations
  and the final result B. They are also fresh for t in the universal row.
  Rename the bound y in the original existential branch before moving the
  elimination; a free old y occurring in the outside t is left untouched.
- In the two rows whose following elimination is existential, its
  eigenparameter z must be fresh for the earlier case assumptions (both
  summands in the disjunction column, `A[y/x]` in the existential column)
  and all formulas in the derivation under which it is moved. Original
  freshness for the following rule's open assumptions alone does not
  guarantee this: those earlier branch assumptions had already been
  discharged. Choose z globally fresh for this finite displayed region;
  choose separate `z_1,z_2` in the two copied disjunction branches.
- For the nested existential row choose y and z distinct. First freshen
  outer y away from the following elimination's entire data and result,
  then choose z away from the earlier existential branch and all retained
  data. The inner reconstructed existential rule discharges c, and the
  outer reconstructed rule discharges a; these are distinct classes.
- For the nested disjunction row choose the following c,d classes distinct
  from a,b and from all free classes in M,N,O. In the disjunction column,
  the two later case rules have separate copied `c_i,d_i` classes; the
  original earlier case still discharges a,b once at the new bottom.
- Projection and universal-elimination rows have no auxiliary proof trees.
  Universal elimination still requires first-order capture avoidance in
  `A[t/x]`; it requires no freshness of t for ordinary open assumptions.
- The bottom row introduces no binder. Its final formula B may contain
  arbitrary free parameters, so the existential column must freshen y
  away from B before enlarging y's scope.

For local preservation, each branch originally ends at C. Apply the same
following elimination to that branch conclusion and the fresh copies of its
auxiliaries. Its new conclusion is B. Reapply the earlier case/unpack rule
with conclusion B. The conditions above are exactly what lets that rule
retain its eigenvariable condition and discharge only its original classes.
No new assumption formula is introduced: the support is contained in the
union of the supports already present on the left. Duplicating an auxiliary
duplicates occurrences, not the set of open assumption formulas. Contextual
preservation follows from Section 3, including now-empty enclosing classes.

The table covers every elimination in the chosen calculus. In particular
`allI` and `pack` are introductions and are not additional permutation rows.

## 6. All seven bottom-absorption rows

Whenever the major premise supplied by `abort_C(M)` is eliminated to B,
replace the complete configuration by `abort_B(M)`:

| Original configuration | Contractum |
| --- | --- |
| `pi_1 abort_(A and B)(M)` | `abort_A(M)` |
| `pi_2 abort_(A and B)(M)` | `abort_B(M)` |
| `abort_(A imp B)(M) N` | `abort_B(M)` |
| `case(abort_(A or B)(M);a.N;b.O)` | `abort_C(M)`, where both branches concluded C |
| `allE(abort_(forall x A)(M);t)` | `abort_(A[t/x])(M)` |
| `unpack(abort_(exists x A)(M);y,a.N)` | `abort_C(M)`, where N concluded C |
| `abort_B(abort_bottom(M))` | `abort_B(M)` |

The retained M already derives bottom from assumptions that were open in
the original major premise. All auxiliary branches and their internal
discharges disappear. External discharge classes can become empty. The
new conclusion is exactly the old final conclusion, and the retained open
support is a subset. No eigenparameter is moved out of its scope: the
eigenparameter of a discarded existential branch was absent from the final
conclusion and never bound occurrences in M.

## 7. Erasure used only for termination

For the termination proof erase formula annotations, individual terms and
individual eigenparameter names from a derivation term. Retain the distinct
constructors `AI`, `AE`, `pack`, `unpack`, all propositional constructors and
proof-variable binding. Thus

```
erase(allI(y.M))       = AI erase(M)
erase(allE(M;t))       = AE erase(M)
erase(pack(t,M))       = pack erase(M)
erase(unpack(M;y,a.N)) = unpack(erase(M);a.erase(N)).
```

This erasure is not an equality of actual derivations. The actual conversions
remain annotated and were justified above. Structural induction gives
`erase(M[t/y]) = erase(M)` modulo renaming of proof binders, and
`erase(N[M/a]) = erase(N)[erase(M)/a]`. Hence every actual principal or
permutation step maps to the corresponding erased step, including a
universal principal step: `AE(AI U) -> U` still removes two constructors.
Erasing individual substitutions therefore does not erase the existence of
that principal step.

Fix distinct simple base types o and iota, and one base type p for each
predicate symbol. Predicate arguments are ignored by the type translation.
Write `A^c = (A^v -> o) -> o`, and define:

| Formula A | `A^v` |
| --- | --- |
| `P(t_1,...,t_n)` | Base type p assigned to P |
| bottom | o |
| `B imp C` | `B^c -> C^c` |
| `B and C` | `(B^c -> C^c -> o) -> o` |
| `B or C` | `(B^c -> o) -> (C^c -> o) -> o` |
| `forall x B` | `iota -> B^c` |
| `exists x B` | `(iota -> B^c -> o) -> o` |

Arrows associate to the right. Since individual terms and variables are
ignored, `A[t/x]^c = A^c` and `A[t/x]^v = A^v`. Introduce one fresh free
STLC variable `star:iota`. It is an inert marker, not an assumed individual
inhabitant inside the object calculus. All target types are arrow-only
simple types. Translate each open proof declaration `a:A` to `a:A^c`.

## 8. Complete arithmetic norm and its strict permutation decrease

For an erased term U define positive integers `n(U)` and `w(U)` by the
following table. The n column is de Groote's `#`; w is his permutation degree.

| U | `n(U)` | `w(U)` |
| --- | --- | --- |
| a | 1 | 1 |
| `lam a.M` | 1 | `w(M)` |
| `M N` | `n(M)` | `w(M)+n(M)w(N)` |
| `pair(M,N)` | 1 | `w(M)+w(N)` |
| `pi_i M` | `n(M)` | `w(M)+n(M)` |
| `in_i M` | 1 | `w(M)` |
| `case(M;a.N;b.O)` | `2n(M)(n(N)+n(O))` | `w(M)+n(M)(w(N)+w(O))` |
| `AI M` | 1 | `w(M)` |
| `AE M` | `n(M)` | `w(M)+n(M)` |
| `pack M` | 1 | `w(M)` |
| `unpack(M;a.N)` | `2n(M)n(N)` | `w(M)+n(M)w(N)` |
| `abort M` | `n(M)` | `w(M)+n(M)` |

All values are at least 1 by structural induction. For any one-step
elimination frame E whose hole is exactly its major premise, there are
positive integers `a_E,b_E`, independent of the term in the hole, such that

```
w(E[U]) = w(U) + n(U)a_E,
n(E[U]) = n(U)b_E.
```

| E | `a_E` | `b_E` |
| --- | --- | --- |
| `[-] L` | `w(L)` | 1 |
| `pi_1 [-]`, `pi_2 [-]`, `AE [-]`, `abort [-]` | 1 | 1 |
| `case([-];c.L;d.R)` | `w(L)+w(R)` | `2(n(L)+n(R))` |
| `unpack([-];c.L)` | `w(L)` | `2n(L)` |

Consequently, in a disjunction permutation the left and right n values
are both `2n(M)(n(N)+n(O))b_E`, and subtraction of the right w value from
the left w value gives exactly

```
n(M)(n(N)+n(O))a_E > 0.
```

Indeed the left adds `2n(M)(n(N)+n(O))a_E` to the unpermuted case's w,
whereas the right adds `n(M)(n(N)+n(O))a_E`. This calculation includes
both duplicated following branches of a later disjunction elimination,
the copied branch of a later existential elimination, and the quantifier
and bottom rows. No duplicated-tree size assumption is used.

For an existential permutation both n values are `2n(M)n(N)b_E`, and
the corresponding strict w difference is

```
n(M)n(N)a_E > 0.
```

These two calculations cover all fourteen rows. They also lift to any
one-hole term context. Induct on that context: equal n values remain equal
under every n recurrence, and the w recurrence is strictly increasing in
the hole's w once its n is held fixed, since every coefficient is positive.
Thus every contextual permutation preserves n and strictly decreases w.

The uniform calculation is supplied to avoid reliance on typographical
slips in individual arithmetic lines of the author manuscript (notably
some lines of Lemma 9 use `#P` where the recurrence requires `|P|`). The
recurrences and the displayed differences here have the indicated values.

## 9. Complete modified CPS translation and principal simulation

Define target arrow-only terms `T(M)=lam k.C(M,k)`, where k is fresh, using
the following simultaneous structural recursion. Every displayed target
binder is fresh for its operands. Each recursive T or C call concerns a
proper source subterm. The notation here is explicitly typed by Section 7,
although type annotations are suppressed for legibility.

| Source term M | `C(M,K)` |
| --- | --- |
| a | `a K` |
| `lam a.N` | `K (lam a.T(N))` |
| `N L` | `C(N, lam f.f T(L) K)` |
| `pair(N,L)` | `K (lam p.p T(N) T(L))` |
| `pi_1 N` | `C(N, lam p.p (lam u.lam v.u K))` |
| `pi_2 N` | `C(N, lam p.p (lam u.lam v.v K))` |
| `in_1 N` | `K (lam u.lam v.u T(N))` |
| `in_2 N` | `K (lam u.lam v.v T(N))` |
| `case(N;a.L;b.R)` | `C(N, lam s.s (lam a.C(L,K)) (lam b.C(R,K)))` |
| `AI N` | `K (lam xi.T(N))` |
| `AE N` | `C(N, lam f.f star K)` |
| `pack N` | `K (lam p.p star T(N))` |
| `unpack(N;a.L)` | `C(N, lam s.s (lam xi.lam a.C(L,K)))` |
| `abort N` | `C(N, (lam z.lam r.r) K)` |

The xi binders have type iota and are fresh dummy binders; they do not
reintroduce the erased individual eigenparameters. Proof binders a,b in
case/unpack are renamed away from K. In the bottom row z has the type of K
and r has type o. The uncontracted expression `(lam z.lam r.r) K` is
intentional. Replacing it in this definition by `lam r.r` would erase K
and invalidate the strict simulation of reductions in auxiliary subterms.

### 9.1 Typing, with every constructor covered

Prove simultaneously: if `Gamma |- M:A`, then `T(M):A^c` under
`Gamma^c,star:iota`; and if additionally `K:A^v -> o`, then `C(M,K):o`.
The following checks are the induction cases.

- Assumption: `a:A^c` applied to K gives o.
- Implication introduction: the induction hypothesis gives
  `lam a.T(N):B^c -> C^c`, so K accepts it.
- Implication elimination: for `f:B^c -> C^c`, `f T(L):C^c` and then
  `f T(L) K:o`; its abstraction is the required continuation for N.
- Pair: `lam p.p T(N) T(L)` has type `(B^c -> C^c -> o) -> o`.
- First projection: `lam u.lam v.u K` has type `B^c -> C^c -> o`;
  second projection uses `v K` with the corresponding result continuation.
- Left injection: `lam u.lam v.u T(N)` has type
  `(B^c -> o) -> (C^c -> o) -> o`; right injection uses v instead.
- Case: the two branch induction hypotheses make `lam a.C(L,K)` and
  `lam b.C(R,K)` continuations of types `B^c -> o` and `C^c -> o`.
  Their application to the translated sum value gives o.
- Universal introduction: `lam xi.T(N):iota -> B^c`.
- Universal elimination: `f:iota -> B^c` gives `f star:B^c`, which
  accepts the continuation for the instance, because substitution does
  not change translated types.
- Existential introduction: `lam p.p star T(N)` has type
  `(iota -> B^c -> o) -> o`.
- Existential elimination: `lam xi.lam a.C(L,K)` has type
  `iota -> B^c -> o`; applying the translated existential value to it
  gives o. The conclusion's translated type is independent of xi.
- Bottom elimination: the premise translates at `(o -> o) -> o`, and
  `(lam z.lam r.r) K` has type `o -> o`, as required.

Wrapping the C judgment in `lam k` establishes the T judgment. This direct
induction needs no normalization theorem or target subject reduction.

### 9.2 Substitution and continuation lemmas

First, `T(M) K ->beta C(M,K)` by one outer beta contraction, choosing k
fresh. Second, for a capture-avoiding proof substitution and any K,

```
C(M,K)[T(N)/a]
  ->beta* C(M[N/a], K[T(N)/a]),
T(M)[T(N)/a] ->beta* T(M[N/a]).
```

Prove these statements together by structural induction on M. For M=a,
the left side is `T(N) K[T(N)/a]` and the first fact contracts it to the
required C term. For another variable both sides are equal. In each
constructor row of the CPS table, substitution distributes through the
fresh target binders and the displayed applications. Apply the induction
hypothesis to each recursive C call and each recursive T call. The same
substitution is applied to its continuation argument, which accounts for
occurrences of a in an auxiliary branch or argument; no assumption that
these derived continuations are a-free is made. The introduction rows
have T calls only; the application, projection, AE and abort rows have
one major C call with a built continuation; case and unpack also have
C calls for their branches. The general hypothesis covers each of these
listed forms. The T statement follows by wrapping the C statement in
its fresh `lam k`. These are exactly all constructors.

The continuation lemma in the next paragraph is independent of substitution
and may be proved first. In the application case, for example, the major
induction gives `C(P[N/a],H)` with the substituted continuation H. The
minor induction reduces `T(Q)[T(N)/a]` inside H to `T(Q[N/a])`. Continuation
closure carries this finite reduction through `C(P[N/a],H)`. This explicitly
justifies normalizing recursive translations inside continuations after a
major recursive call; the same reasoning treats the branch continuations.

Third, if `K ->beta L`, then for every M,
`C(M,K) ->beta+ C(M,L)`. More generally a positive beta path in K gives
a positive beta path in C. Structural induction establishes that C retains
at least one occurrence of its continuation and finitely many copies. In
the variable and introduction rows it appears directly. In the application,
projection and AE rows it appears in the supplied continuation, and the
induction hypothesis for the major operand applies. In case and unpack
it appears in their branch C calls and hence in the major continuation;
reduce each copied occurrence. The abort row retains it as the argument
of the displayed erasing redex; reduce inside that argument before erasing
it. Every row therefore supplies a nonempty sequence. This strictness is
why retaining that bottom administrative redex matters.

### 9.3 Seven root principal simulations

In this subsection the source terms are erased, and substitutions are of
proof terms. Write `->beta+` for one or more target beta contractions and
`->beta*` for zero or more. Freshen the discharged variable away from K.

1. Implication:
   `C((lam a.M)N,K)` is
   `(lam f.f T(N) K)(lam a.T(M))`.
   It reduces through `(lam a.T(M)) T(N) K` to
   `T(M)[T(N)/a] K`, then by the substitution lemma and the wrapper
   contraction to `C(M[N/a],K)`. At least the first beta step occurs.
2. First projection:
   `C(pi_1 pair(M,N),K)` reduces by the displayed projection continuation
   applied to `lam p.p T(M) T(N)` to `T(M) K`, then to `C(M,K)`.
   The second projection has the identical sequence selecting `T(N) K`
   and `C(N,K)` instead. Both sequences are positive.
3. Disjunction-left:
   `C(case(in_1 M;a.N;b.O),K)` first applies
   `lam s.s (lam a.C(N,K))(lam b.C(O,K))`
   to `lam u.lam v.u T(M)`. Successive beta contractions select
   `(lam a.C(N,K)) T(M)`, then
   `C(N,K)[T(M)/a]`, which reaches `C(N[M/a],K)` by substitution.
   Disjunction-right selects `(lam b.C(O,K)) T(M)` and reaches
   `C(O[M/b],K)`. These are the fourth and fifth concrete rows.
4. Universal:
   `C(AE(AI M),K) = (lam f.f star K)(lam xi.T(M))`
   reduces to `(lam xi.T(M)) star K`, then `T(M) K`, then `C(M,K)`.
   The erased actual contractum `M[t/y]` is precisely erase(M), so the
   lost individual annotation does not change this simulation.
5. Existential:
   `C(unpack(pack M;a.N),K)` is
   `(lam s.s(lam xi.lam a.C(N,K)))(lam p.p star T(M))`.
   It reduces to `(lam xi.lam a.C(N,K)) star T(M)`, then
   `(lam a.C(N,K)) T(M)`, then `C(N,K)[T(M)/a]`, then
   `C(N[M/a],K)`. Individual substitution in the actual contractum
   erases, and proof substitution commutes with erasure.

This lists all seven root rules, counting the two projections and the two
sum selections separately. There is no root principal rule for bottom.

The simulation is contextual, not merely a root calculation. Induct on a
one-hole source context using the CPS table. A hole in a major operand uses
the inductive statement for every continuation. A hole in a minor operand,
branch or introduction operand occurs in one or more T/C subterms; reduce
those copies, and use continuation strictness whenever those subterms lie
inside the continuation of another C call. That lemma also covers the
bottom constructor. Thus for every actual principal step `M ->D N`,
`T(erase(M)) ->beta+ T(erase(N))`.

### 9.4 Every permutation translates to equality

The continuation contributed by an elimination frame E is:

| E | `H_E(K)` |
| --- | --- |
| `[-] L` | `lam f.f T(L) K` |
| `pi_1 [-]` | `lam p.p(lam u.lam v.u K)` |
| `pi_2 [-]` | `lam p.p(lam u.lam v.v K)` |
| `AE [-]` | `lam f.f star K` |
| `case([-];c.L;d.R)` | `lam s.s(lam c.C(L,K))(lam d.C(R,K))` |
| `unpack([-];c.L)` | `lam s.s(lam xi.lam c.C(L,K))` |
| `abort [-]` | `(lam z.lam r.r) K` |

By definition `C(E[U],K)=C(U,H_E(K))`. For a case subject, expand both
sides of its permutation with this identity:

```
C(E[case(M;a.N;b.O)],K)
 = C(M,lam s.s(lam a.C(N,H_E(K)))(lam b.C(O,H_E(K))))
 = C(case(M;a.E[N];b.E[O]),K).
```

For an existential subject:

```
C(E[unpack(M;a.N)],K)
 = C(M,lam s.s(lam xi.lam a.C(N,H_E(K))))
 = C(unpack(M;a.E[N]),K).
```

The alpha-renaming conditions of Section 5 ensure the identities, including
the copied c,d and dummy xi binders. They are syntactic equalities modulo
alpha-equivalence, without beta contraction. Induction through the CPS
recursion extends equality to every source context and to T. These seven
frame identities cover all fourteen actual permutation rows.

## 10. An actual well-founded strategy, including bottom

The independent prerequisite is strong beta normalization of the open-term
arrow-only STLC. A complete separately authored proof is available at
`handbook/parts/p07/stlc-metatheory.tex`,
`thm:p07-stlc-strong-normalization`, with full proof at
`handbook/annex/p07/stlc-metatheory.tex`,
`annex:p7.stlc.strong-normalization`. Its source note identifies the exact
Girard–Lafont–Taylor manifestation and the open-term reducibility proof.
The older inactive normalization chapter's sketch must not be substituted
for this completed prerequisite. The lead reports that root confirmed the
completed STLC theorem and its inert-constant corollary are routed; the
present proof uses the open-term theorem and a fresh free marker variable.

For a typed target term V, define `h_beta(V)` as the largest length of a
beta-reduction sequence from V. This is a natural number: the term has
finitely many immediate beta reducts modulo alpha-equivalence, and STLC
strong normalization plus the elementary finitely-branching-tree argument
excludes unbounded finite depths. Equivalently well-founded recursion gives
`h_beta(V)=0` when normal and
`1+max{h_beta(W): V ->beta W}` otherwise.

For any actual derivation term M set

```
mu(M) = (h_beta(T(erase(M))), w(erase(M))) in N x N,
```

ordered lexicographically, first coordinate first. Both coordinates are
defined above. A principal step strictly decreases the first coordinate
by its positive target simulation; the second may increase without harm.
A permutation leaves the translated target alpha-equivalent and hence
leaves the first coordinate fixed, while strictly decreasing the second
by Section 8. Therefore every compatible principal/permutation step
strictly decreases mu. This argument accounts for all copied branches and
all quantified instantiations. It does not assert that the size of the
whole proof, the number of detours, or a naive maximal-rank count decreases.

Use the following two-phase strategy.

**Phase I:** while any principal or permutation redex exists, choose one
by a fixed traversal of the finite annotated derivation and contract it
with the prescribed fresh names. The measure mu strictly decreases, so
this phase ends at a derivation normal for both these classes. Formula
and term annotations remain on the actual derivation throughout.

**Phase II:** while a bottom-absorption redex exists, contract it. Each of
the seven rows removes at least one proof constructor and possibly whole
auxiliary derivations, retaining a single `abort` on its previous bottom
premise. Hence ordinary constructor count strictly decreases.

A Phase II step preserves Phase I normality. Inside the retained M nothing
changes. The only new head at the replacement boundary is `abort`; it cannot
be the introduction, case or unpack head needed for a principal or
permutation redex in the surrounding context. A new permutation at the
replacement's own root would require M to have head case or unpack, but
then the original inner `abort(M)` was already a permutation redex before
the absorption, contradicting Phase I normality. No other new adjacency
is created. This argument includes the nested bottom row. Thus Phase II
ends with all three classes absent and never needs to restart Phase I.

If a single strategy-state measure is desired, order states by
`(phase,h,w,size)` lexicographically in `N^4`, using phase=1 during Phase I
and phase=0 during Phase II. Phase I steps decrease `(h,w)` regardless of
size; the one phase switch strictly decreases phase; Phase II steps keep
phase,h,w coordinates replaced by zero and decrease size. More explicitly
use `(1,h,w,0)` in Phase I and `(0,0,0,size)` in Phase II. This is a
well-founded measure of the specified strategy, not of arbitrary mixtures
of all three conversion classes.

Every step has the same conclusion and introduces no open assumption formula
by Sections 3–6. The final result therefore has the original conclusion
and an open support contained in the original support. This proves the
requested weak normalization theorem for the distinct standard NJ calculus
with empty discharge classes and the three declared normality conditions.

No assertion of strong normalization for arbitrary interleavings including
bottom absorption is required here. De Groote's Theorem 4 proves a stronger
result using additional postponement work; that result is a separate source
fact, not an unstated premise of the two-phase construction.

## 11. Integration requirements and authoring standing

The author should use the explicit source attribution if selecting this
termination route and preserve the Prawitz/Troelstra historical route as
its own identified presentation. Source permission to omit individual
terms from a simulation does not justify omitting them from the actual
quantifier reductions; Sections 2–5 provide those data.

The necessary normalization definitions are the seven principal rows,
fourteen permutations, seven bottom absorptions, compatible closure on
finite derivations modulo alpha-equivalence, and the three normality
conditions in Section 1. The termination construction consists of the
erasure lemma, arrow-only typing, full CPS table, strict principal
simulation, permutation equality, arithmetic norm and two phases.

This is constructive authoring support. No independent review, manuscript
build, render or test suite has been run. All manuscript and shared records
remain owned by the lead and root.

The author read this entire written note, checked the arithmetic differences
against the displayed recurrences, and read the final new rule sheet.
The lead's notation maps directly to this note: `lambda` to `lam`, its
`iota_i` to `in_i`, `Lambda x.M` to `allI(x.M)`, and `M[t]` to `allE(M;t)`;
formula-annotated `pack` and `abort` retain their annotations in the actual
derivation and lose them only in the termination erasure. There is no
remaining construction gap in the assigned quantified/permutation tables
or the specified weak-normalization termination route.
