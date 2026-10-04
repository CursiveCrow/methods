# Modal parity automata to scalar mu-calculus: source and elimination note

Date: 2026-09-06.

## Outcome

Bradfield--Stirling supports the reverse expressive-equivalence claim,
but its Theorem 5.2 does not provide the reverse construction. The
ordered simultaneous-block semantics needed for a supplied construction
is elsewhere in the same preprint. A fully typed scalar-elimination
lemma is proved below; it does not depend on deductive completeness or
on the unsettled Kozen counter-overflow argument.

Live manuscript scope read for this task:

- `handbook/parts/p09/presentations/n-c-018.tex`, label
  `sec:p09-modal-parity-automata`;
- the same file, label `sec:p09-mu-automaton-construction`.

The first defines depth-one modal transition expressions and their
acceptance game. The second is currently the formula-to-automaton
construction, explicitly including unguarded input formulas. Neither
label alone is a reverse-construction proof.

## Primary-source locations

**B&S** denotes Bradfield and Stirling, [*Modal Mu-Calculi*, author
preprint dated 15 November 2005](https://www.pure.ed.ac.uk/ws/files/16483207/Modal_Mu_Calculi.pdf).
The repository cover identifies the published chapter as 2007,
pp. 721--756. Page numbers below are the preprint's printed numbers;
its PDF has one additional repository-cover page.

| Location | Retrieved content |
|---|---|
| Section 3.7, p. 12; PDF page 13 | Ordered homogeneous mu/nu blocks; componentwise fixed points; earlier variables are parameters and later blocks supply solutions. It gives a reverse substitution example and notes potential exponential duplication. |
| Section 4.3, p. 15; PDF page 16 | Parity means least infinitely recurring priority even. |
| Section 4.4, pp. 15--16; PDF pages 16--17 | Truth determines finite terminal winners; dead-end boxes win and diamonds lose. Theorem 4.6 identifies formula truth with a history-free winning strategy. |
| Section 5.3, p. 19; PDF page 20 | Positive depth-one modal grammar, mixture semantics and finite complete run branches. Infinite branches obey parity. |
| Theorem 5.2, pp. 19--20; PDF pages 20--21 | Closed formulas and modal automata are mutually expressively equivalent. No reverse construction follows before Section 5.4. |

The source indexes runs by a subset of `omega*`; the manuscript's
arbitrary set-sized branching is an explicit extension. No named Bekic
identity appears in B&S.

The printed reverse example in Section 3.7 is the two-block system

\[
 X_{00}=_{\mu}\langle a\rangle X_{10}\lor[b]X_{10};
 \qquad
 X_{10}=_{\nu}P\land[a](X_{00}\lor X_{10}),
\]

with scalar result, adding parentheses to expose binder scope,

\[
 \mu X.\Bigl(
   \langle a\rangle(\nu Y.(P\land[a](X\lor Y)))
   \lor[b](\nu Y.(P\land[a](X\lor Y)))
 \Bigr).
\]

This is an example of eliminating ordered singleton blocks, not a
printed general automaton-to-formula algorithm or a proof for a
multi-variable block. The displays are mathematical transcription;
the derivations below are supplied arguments.

## Supplemental primary mathematical texts

Robert Harper's author-hosted [*Tarski's Fixed Point Theorem for Power
Sets*, Spring 2020](https://www.cs.cmu.edu/~rwh/courses/chtt/pdfs/tarski.pdf),
Section 3, pp. 2--4, explicitly states and proves a two-variable Bekic
identity for least fixed points. In fresh notation its displayed
identity is

\[
 \mu(f,g)=
 \bigl(
   \mu x.f(x,\mu y.g(x,y)),
   \mu y.g(\mu x.f(x,y),y)
 \bigr).
\]

The types and complete-lattice variant used below are stated and proved
separately, so no implicit continuity or finite-state assumption is
imported from an abbreviated formula.

Stephan Kreutzer's institutional [*Pure and Applied Fixed-Point
Logics*, dissertation, 2002](https://www.logic.rwth-aachen.de/pub/kreutzer/kreutzer.pdf)
has the eliminate-last-variable substitution at Lemma 3.18, printed
pp. 40--41 (PDF pages 40--41), and the modal elimination statement at
Theorem 10.4, printed p. 113 (PDF page 113). Lemma 3.18 explicitly omits
the underlying proof, referring to Arnold--Niwinski, Lemma 1.4.2,
p. 27. Theorem 10.4 applies that elimination to modal mu-calculus.
It supplies a precise corroborating construction, not another completed
proof to cite as though it were printed there.

The [publisher record for Bekic's original
chapter](https://link.springer.com/chapter/10.1007/BFb0048939)
identifies *Definable operations in general algebras, and the theory of
automata and flowcharts*, reprinted in LNCS 177 (1984), pp. 30--55.
Only the record and subscription-preview information were available;
the chapter body was not inspected and is not used as identity evidence.

## Supplied typed Bekic elimination lemma

Let `L` and `K` be complete lattices, ordered by `<=`, and let

\[
 f:L\times K\longrightarrow L,
 \qquad g:L\times K\longrightarrow K
\]

be monotone in both arguments. Additional free parameters are fixed
during this argument. Fix one kind `sigma in {mu,nu}`, the same in
both coordinates. Define

\[
 h(x)=\sigma y.g(x,y),\qquad
 a=\sigma x.f(x,h(x)),\qquad b=h(a).          \tag{B1}
\]

Then

\[
 \sigma(x,y).(f(x,y),g(x,y))=(a,b).           \tag{B2}
\]

First, parameter monotonicity gives monotonicity of `h`: if `x <= x'`,
then the pointwise map `g(x,-)` is below `g(x',-)`, and least as well
as greatest fixed points preserve this comparison. For the least
case, the least fixed point of the larger map is a pre-fixed point of
the smaller one. For the greatest case, the greatest fixed point of
the smaller map is a post-fixed point of the larger one. This also
shows `x |-> f(x,h(x))` is monotone, so every term of (B1) exists.

Unfolding (B1) gives `f(a,b)=a` and `g(a,b)=b`.

For `sigma = mu`, take any product pre-fixed point `(u,v)`:
`f(u,v) <= u` and `g(u,v) <= v`. The latter inequality gives
`h(u) <= v`. Therefore

\[
 f(u,h(u))\leq f(u,v)\leq u.
\]

Minimality gives `a <= u`; monotonicity gives
`b=h(a) <= h(u) <= v`. Thus `(a,b)` is below every product
pre-fixed point, proving (B2).

For `sigma = nu`, take any product post-fixed point `(u,v)`:
`u <= f(u,v)` and `v <= g(u,v)`. The latter gives `v <= h(u)`;
then

\[
 u\leq f(u,v)\leq f(u,h(u)).
\]

Maximality gives `u <= a`, and
`v <= h(u) <= h(a)=b`. Thus `(a,b)` is above every product
post-fixed point, proving the greatest case as well.

This proof applies to arbitrary complete lattices, including
`L = P(S)` and products of such lattices for infinite sets `S`.
No finite convergence, omega-continuity, or determinacy is assumed.

## Supplied syntactic elimination rule and induction

For a homogeneous two-equation block with positive formulas
`F(X,Y)` and `G(X,Y)`, let

\[
 H(X)=\sigma Y.G(X,Y),\qquad
 A=\sigma X.F(X,H(X)),\qquad B=H(A).          \tag{B3}
\]

The first and second components are respectively denoted by `A` and
`B`, by (B1)--(B2) and the substitution lemma. Every substitution is
capture-avoiding; rename bound variables before duplicating a formula.
The placeholders `X,Y` may have other free parameters, whose valuations
must remain fixed throughout this elimination.

For an `n`-variable homogeneous block, with `n >= 2`, split the first
coordinate from the remaining `n-1` coordinates, taking the latter
product as `K`. Compute its parameterized fixed point `h(x)` recursively
by the induction hypothesis, then apply (B1). This strictly reduces
the number of simultaneously bound coordinates. The base `n=1` is
already scalar. Consequently every selected component of a finite
homogeneous block becomes a finite scalar mu-calculus formula.

For a finite sequence of nested blocks, eliminate the innermost block
first while keeping outer variables free; then continue outward.
Positivity in the remaining parameters is preserved by the positive
substitutions and fixed-point operators. This is not permission to
commute a mu-block with a nu-block or replace a mixed sequence by one
simultaneous fixed point. Finiteness of the output is proved; no
polynomial tree-syntax size estimate is asserted.

## Supplied product-coordinate bridge for the parent's construction

For any set of model states `S` and finite nonempty set of controls `Q`,
define

\[
 I:P(S\times Q)\longrightarrow P(S)^Q,
 \qquad I(U)_q=\{s:(s,q)\in U\},
\]

with inverse `I^{-1}((U_q)_q) = union_q (U_q times {q})`.
These maps preserve and reflect inclusion and commute with arbitrary
unions and intersections. They are therefore a complete-lattice
isomorphism.

If the scalar product construction gives a monotone map `F`, put
`F^Q = I o F o I^{-1}`. The isomorphism bijects pre-fixed points and
post-fixed points of these two maps. Taking their meets or joins gives

\[
 I(\mu F)=\mu F^Q,\qquad I(\nu F)=\nu F^Q.  \tag{C}
\]

Applying (C) from the innermost binder outward translates a nested
scalar fixed-point expression on `S times Q` into nested simultaneous
blocks on `P(S)^Q`, one vector of coordinates for each scalar binder.
This proves the algebraic coordinate step only. The parent construction
must separately show that its scalar product formula denotes the
acceptance game's winning set, and that its componentwise body is
expressible using the original model's modalities. Once those two
identifications are made, (B3) eliminates the simultaneous binders and
the `q0` component is an ordinary scalar formula on `S`.

## Actionable convention and scope checks

1. **Priority order.** For least-recurring parity, the block associated
   with a lower numerical priority is outer, with `nu` for even and
   `mu` for odd. A greatest-recurring convention requires an explicit
   finite parity-preserving order reversal; it cannot be substituted
   silently.
2. **Terminal outcomes.** Keep `top`, `bottom`, empty boxes and empty
   diamonds as finite outcomes before applying infinite parity. In
   particular a control of odd priority with transition `top` accepts;
   an even control with transition `bottom` rejects. A dead-end box
   accepts even at odd priority; an empty diamond rejects even at even
   priority. These are immediate calculations, not software tests.
3. **Coordinate type.** A scalar binder on `P(S times Q)` becomes a
   simultaneous `Q`-tuple binder, not one scalar binder evaluated
   independently at each control. Its component functions can refer
   to other controls' coordinates.
4. **Current versus next priority.** Specify whether the parity formula
   reads a current control's priority before its transition or a next
   control's priority after it. A one-step shift is harmless for an
   infinite finite-range priority sequence, but still requires a
   correspondence argument and the separate terminal treatment.
5. **Source versus supplied proof.** Attribute expressive equivalence
   to B&S Theorem 5.2 and block semantics to Section 3.7. Identify the
   product formula, coordinate proof and explicit elimination proof as
   supplied derivations. The source theorem's existence statement is
   not evidence that the manuscript's particular reverse construction
   has been checked.
6. **Alphabet finiteness.** The read automaton uses finite `P0`, so
   `P(P0)` is finite. If letter tests are expanded in scalar syntax,
   define the test for each letter, including the empty conjunction
   when `P0` is empty. This expansion can duplicate formulas; no
   succinctness conclusion follows merely from expressiveness.

## Handoff boundary

Only this note was created. No manuscript, previous research note or
algorithm was edited. No additional agents, code, tests, builds or
manuscript renders were used. Retrieved primary support, the supplied
elimination proof and the still-separate product-game correctness
obligation are deliberately distinguished.
