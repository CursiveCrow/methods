# Bekić elimination and scalarization of finite control products

Date: 2026-09-06. Status: a direct mathematical derivation of the finite
same-sign fixed-point elimination needed by an automaton-to-formula
translation. This note does not prove the separate tagged-product parity
formula's game characterization. It is not a manuscript build, software test,
render inspection, or an independent admission of the completed reverse
translation.

## 1. Scope, conventions, and provenance

The live manuscript `handbook/parts/p09/presentations/n-c-018.tex`, at
`sec:p09-modal-parity-automata`, defines a finite nonempty control set `Q`,
transition atoms `<a>q` and `[a]q`, positive Boolean transition syntax, and
acceptance by the least infinitely recurring priority being even. A dead
diamond loses and a dead box wins for Exists. The present derivation uses
those conventions. No finiteness or branching bound is imposed on the model
state set `S`.

The identity below is proved here from least/greatest fixed-point
characterizations. Its traditional name is a label for the result, not an
appeal to an external elimination theorem. Historical/source attribution,
if subsequently required, belongs in a source note rather than in place of
the proof.

The precise scope invariant is semantic: eliminate one simultaneous
**same-sign** block at a time, with its external variables held as parameters,
and preserve the original nesting of the block operators as parameterized
maps. One must not commute a least block with a greatest block. Literal
binder words, alternation-depth bounds, guardedness, and efficient output
size are not asserted to be preserved by the substitutions below.

## 2. Complete-lattice facts used in the proof

Let `L` be a complete lattice and `F:L -> L` a monotone map. A pre-fixed
point is an `x` with `F(x) <= x`; a post-fixed point satisfies `x <= F(x)`.
The least fixed point `mu F` is below every pre-fixed point. The greatest
fixed point `nu F` is above every post-fixed point. Both are fixed points.
These are the complete-lattice fixed-point characterizations used below.

Products have the componentwise order and componentwise suprema and infima,
so a finite product of complete lattices is complete. If `F <= G` pointwise,
then

\[
 \mu F\le\mu G,\qquad \nu F\le\nu G.
\]

Indeed, `mu G` is pre-fixed for `F`, whereas `nu F` is post-fixed for `G`.
This proves the monotonicity in the map without an iteration-continuity
assumption. All applications below are valid for arbitrary complete
lattices, in particular full powerset lattices.

## 3. The binary Bekić identity, including both signs

Let `L,M` be complete lattices, and let

\[
 f:L\times M\longrightarrow L,
 \qquad g:L\times M\longrightarrow M
\]

be monotone in the product order. Fix one sign `sigma`, either `mu` or
`nu`, and define

\[
 h(x)=\sigma y.\,g(x,y),\qquad
 F(x)=f(x,h(x)),\qquad
 a=\sigma x.\,F(x),\qquad b=h(a).
\]

### Monotonicity and the fixed-point equations

If `x <= x'`, then `g(x,-) <= g(x',-)` pointwise. The monotonicity in the
map proved above gives `h(x) <= h(x')`, for either sign. Consequently `F`
is monotone and `a` is defined. The definitions give

\[
 f(a,b)=f(a,h(a))=a,
 \qquad g(a,b)=g(a,h(a))=h(a)=b.
\]

Thus `(a,b)` is a fixed point of `(f,g)`.

### Least-fixed-point case

Suppose `(x,y)` is any pre-fixed point of the pair map:

\[
 f(x,y)\le x,\qquad g(x,y)\le y.
\]

The second inequality and the least-fixed-point characterization imply
`h(x) <= y`. Hence

\[
 F(x)=f(x,h(x))\le f(x,y)\le x.
\]

Therefore `a <= x`, and monotonicity of `h` gives

\[
 b=h(a)\le h(x)\le y.
\]

Our fixed point is below every pre-fixed point, so

\[
 (a,b)=\mu(x,y).\,(f(x,y),g(x,y)).
\]

### Greatest-fixed-point case

Suppose `(x,y)` is any post-fixed point of the pair map:

\[
 x\le f(x,y),\qquad y\le g(x,y).
\]

Now `y <= h(x)`. Consequently

\[
 x\le f(x,y)\le f(x,h(x))=F(x).
\]

Thus `x <= a`, and

\[
 y\le h(x)\le h(a)=b.
\]

Our fixed point is above every post-fixed point, so

\[
 (a,b)=\nu(x,y).\,(f(x,y),g(x,y)).
\]

This proves exactly the same displayed construction for both signs.
It does not prove, and must not be used as, an identity with different
signs in the two simultaneously eliminated coordinates.

### External parameters

If `f` and `g` also depend on a parameter valuation `e`, the preceding proof
applies separately to every fixed `e`. Thus the identity is an identity
of parameterized denotations, not merely of closed terms. If the maps are
jointly monotone in `e`, the resulting `h_e`, `a_e`, and `b_e` are monotone
in `e` as well: apply monotonicity in the map first to `h`, then to `F`
and `a`, and finally use monotonicity in both arguments for `h_e(a_e)`.

## 4. Finite elimination into ordinary scalar syntax

Work in finite positive-normal-form scalar modal mu-calculus syntax, with
unary binders `mu x.t` and `nu x.t`. Negations occur only on proposition
constants. Thus every free fixed-point variable is positive. Bound names
are alpha-renamed to be distinct and disjoint from all free parameter
names before substitution. Every copied subformula is alpha-renamed again
when needed to retain this convention.

Let `E` be a finite set of external variable names. Given distinct block
names `x_1,...,x_k`, suppose the scalar bodies

\[
 t_i(x_1,\ldots,x_k;E)\qquad(1\le i\le k)
\]

have no free variables outside the displayed names. Their internal binders
may use either sign; those already formed bodies are not reordered. For
every fixed model and valuation of `E`, their denotations are jointly
monotone maps on `P(S)^k`. We construct a tuple of finite **ordinary
scalar** formulas `A_1(E),...,A_k(E)` denoting the components of

\[
 \sigma(x_1,\ldots,x_k).\,(t_1,\ldots,t_k).
\]

The displayed simultaneous binder is only notation for the product-lattice
operation whose scalar elimination is being defined.

### Base case

For `k=1`, put `A_1 = sigma x_1.t_1`.

### Induction step

For `k >= 2`, isolate the final coordinate and form the scalar formula

\[
 H(x_1,\ldots,x_{k-1};E)
       =\sigma x_k.\,t_k(x_1,\ldots,x_k;E).
\]

For `i<k`, let

\[
 u_i=t_i[H/x_k],
\]

where the substitution is capture-avoiding and changes free occurrences
only. Apply the induction hypothesis with the **same sign** `sigma` to
the `(k-1)` bodies `u_1,...,u_{k-1}`. It yields formulas
`A_1(E),...,A_{k-1}(E)`. Finally put

\[
 A_k=H[A_1/x_1,\ldots,A_{k-1}/x_{k-1}].
\]

The last operation is simultaneous capture-avoiding substitution. The
inserted `A_i` have no free block variables, so they do not acquire new
substitutions into each other. They may share free names in `E`; these
remain free. Their bound names are refreshed separately in every copy.

For correctness, take `L=P(S)^{k-1}`, `M=P(S)`, `g=t_k`, and
`f=(t_1,...,t_{k-1})` in the binary theorem. The denotation of `H` is its
map `h`; the denotations of the `u_i` are the reduced map `f(-,h(-))`;
the induction hypothesis supplies `a`; and the final simultaneous
substitution denotes `h(a)`. Thus all `k` components are correct for
every valuation of the external parameters.

The construction terminates because the induction decreases `k`. Every
step performs finitely many unary binders and finite substitutions into
finite formulas. It therefore yields finite syntax. No size-efficiency
claim is needed: copying can be extensive.

### Why substitution has the stated semantics

For a scalar formula `t`, simultaneous capture-avoiding substitution of
formulas `r_j` for free variables `x_j` has the same denotation as
evaluating `t` after assigning `x_j` the denotation of `r_j` in the
original environment. This follows by structural induction. Boolean and
modal constructors preserve the induction equality. At a binder, first
choose its name fresh from the substituted formulas and substitute into
its body. The induction hypothesis then identifies its body maps for
every value of the bound variable, so their least or greatest fixed
points are identical. This also explains why a free parameter must never
be accidentally captured by a copied binder.

## 5. From the tagged product to components over the original model

Fix a finite nonempty set `Q`. The maps

\[
 \Theta(U)_q=\{s\in S:(s,q)\in U\},
 \qquad
 \Theta^{-1}((U_q)_{q\in Q})
       =\bigcup_{q\in Q}(U_q\times\{q\})
\]

are inverse complete-lattice isomorphisms

\[
 \mathcal P(S\times Q)\cong\mathcal P(S)^Q.
\]

They preserve arbitrary unions and intersections componentwise. If `T`
is a monotone map on the product powerset and
`T^Q=Theta o T o Theta^{-1}`, then

\[
 \Theta(\sigma T)=\sigma T^Q
 \qquad(\sigma=\mu,\nu).
\]

For example, in the least case the isomorphism carries pre-fixed points
in both directions and preserves the relation of being below all of
them; the greatest case uses post-fixed points. This proves the
fixed-point transport instead of assuming it.

Here is an explicit componentwise syntax translation adequate for the
usual tagged-product construction. Lift an original proposition `P` to
`S x Q`, and let `tag_r` hold precisely on `S x {r}`. For an original
action `a` and target control `r`, define

\[
 R_{a:r}((s,q),(t,u))
       \quad\Longleftrightarrow\quad R_a(s,t)\ \land\ u=r.
\]

These target-tagged relations do not depend on the source control.
For each product variable `Z`, allocate a family of distinct scalar
variables `(Z_q)_{q in Q}`. Different binding occurrences receive
different fresh families, even if the input reused a printed name.
Write `tr_q(t)` for the component formula at `q`. Its clauses are

\[
\begin{aligned}
 \operatorname{tr}_q(Z)&=Z_q,\\
 \operatorname{tr}_q(P)&=P,
 &\operatorname{tr}_q(\neg P)&=\neg P,\\
 \operatorname{tr}_q(\mathsf{tag}_r)
    &=\begin{cases}\top&q=r,\\\bot&q\ne r,\end{cases}\\
 \operatorname{tr}_q(\neg\mathsf{tag}_r)
    &=\begin{cases}\bot&q=r,\\\top&q\ne r,\end{cases}\\
 \operatorname{tr}_q(\top)&=\top,
 &\operatorname{tr}_q(\bot)&=\bot,\\
 \operatorname{tr}_q(t\circ u)
    &=\operatorname{tr}_q(t)\circ\operatorname{tr}_q(u)
       &&(\circ\in\{\land,\lor\}),\\
 \operatorname{tr}_q(\langle a:r\rangle t)
    &=\langle a\rangle\operatorname{tr}_r(t),\\
 \operatorname{tr}_q([a:r]t)
    &=[a]\operatorname{tr}_r(t).
\end{aligned}
\]

For a product binder `sigma Z.t`, first translate its body into the
tuple `(tr_q(t))_{q in Q}`, treating the fresh family `Z_q` as free
block variables. Recursively translated inner binders have already
become scalar formulas. Apply the finite same-sign elimination from
Section 4 to

\[
 \sigma(Z_q)_{q\in Q}.\,
                   (\operatorname{tr}_q(t))_{q\in Q}.
\]

Its scalar output component `q` is, by definition,
`tr_q(sigma Z.t)`. All families belonging to free product variables
remain external parameters at this step. Families belonging to outer
binders are likewise external at this step; they are bound only when
the recursive translation later handles those enclosing binders.

Structural induction now proves, for every product valuation `eta`,

\[
 (s,q)\in\llbracket t\rrbracket_{S\times Q,\eta}
 \quad\Longleftrightarrow\quad
 s\in\llbracket\operatorname{tr}_q(t)
            \rrbracket_{S,\eta^Q},
 \qquad \eta^Q(Z_q)=\Theta(\eta(Z))_q.
\]

The modal clauses follow directly from the definition of `R_{a:r}`,
including dead boxes and dead diamonds. The binder clause follows from
the body induction, fixed-point transport through `Theta`, and the
finite elimination theorem. This is a formula-by-formula correctness
proof, including all parameter valuations, rather than a correspondence
proved only for one closed input.

When the product formula is closed, each scalar output is closed. No
tag propositions or target-tagged action symbols survive in the scalar
output: only the original propositions, original actions, Boolean
constructors, and unary fixed-point binders remain.

## 6. Nested alternating blocks and an automaton-specific body

For a finite tuple of nested blocks, first translate the innermost body
and eliminate its innermost same-sign block, leaving all outer variable
families free. The parameter-uniform correctness already proved lets
one replace that body by its scalar component tuple at every valuation
of the outer families. Proceed outward one block at a time. This
preserves the denotation of the originally ordered composite

\[
 \sigma_0\mathbf Z_0.\,
 \sigma_1\mathbf Z_1.\,\cdots
 \sigma_d\mathbf Z_d.\,\mathbf T.
\]

There is no step replacing `mu ... nu ...` by `nu ... mu ...`, or
eliminating differently signed coordinates as one simultaneous block.
Substitution may put a copy of a scalarized outer component inside an
inner binder's body; the free parameter it replaces previously referred
to that outer component. This is correct lexical substitution, not an
interchange law. Hence a claim that the literal nesting word or the
alternation depth is unchanged would exceed this theorem.

To make the automaton connection concrete, for `A subseteq P_0` define
the original-model letter test

\[
 \chi_A=\bigwedge_{P\in A}P\ \land
                 \bigwedge_{P\in P_0\setminus A}\neg P,
\]

with empty conjunction equal to `top`. For fixed priority index `i`,
let `widehat(delta(q,A))_i` replace `<a>r` by `<a>Z_{i,r}` and `[a]r`
by `[a]Z_{i,r}`, preserving constants and Boolean connectives. Then
the source-priority-tagged one-step body has scalar components

\[
 T_q(\mathbf Z_0,\ldots,\mathbf Z_d)
    =\bigvee_{A\subseteq P_0}
       \left(\chi_A\land
            \widehat{\delta(q,A)}_{\Omega(q)}\right).
\]

Every family variable is positive, and the expression is finite. If a
separate parity-game argument establishes the appropriate meaning of

\[
 \nu\mathbf Z_0.\,\mu\mathbf Z_1.\,
 \nu\mathbf Z_2.\,\cdots\sigma_d\mathbf Z_d.\,
                   (T_q)_{q\in Q},
\]

where `sigma_i` is `nu` for even `i` and `mu` for odd `i`, this note
supplies a finite ordinary scalar formula for each component. In
particular its initial component is the output at `q_0`. This last
sentence is conditional on that separate game argument: scalarization
itself must not be used as an oracle for which nested parity expression
is correct.

## 7. Worked two-control elimination with an even and an odd control

Take controls `e,o`, priorities `Omega(e)=0`, `Omega(o)=1`, and initial
control `e`. Let `P_0={P}` and use the guarded transitions

\[
 \delta(e,A)=\langle a\rangle o,\qquad
 \delta(o,A)=
   \begin{cases}
    \langle a\rangle e,&P\in A,\\
    \langle a\rangle o,&P\notin A.
   \end{cases}
\]

All model moves are existential. A successful infinite play must visit
`e` infinitely often; otherwise only priority `1` eventually recurs.
Since every transition is a diamond, a finite play always loses.

The source-priority-tagged simultaneous expression is

\[
 \nu(X_e,X_o).\,\mu(Y_e,Y_o).\,
 \left(\langle a\rangle X_o,
       (P\land\langle a\rangle Y_e)
            \lor(\neg P\land\langle a\rangle Y_o)\right).
\]

For the inner least block, regard `X_e,X_o` as external parameters.
The binary construction gives

\[
\begin{aligned}
 H(y;X_o)&=\mu z.\,
       (P\land\langle a\rangle y)
             \lor(\neg P\land\langle a\rangle z),\\
 A_e(X_o)&=\mu y.\,\langle a\rangle X_o
                         =\langle a\rangle X_o,\\
 A_o(X_o)&=H(A_e(X_o);X_o)\\
   &=\mu z.\,
       (P\land\langle a\rangle\langle a\rangle X_o)
             \lor(\neg P\land\langle a\rangle z).
\end{aligned}
\]

Write the last formula as `D(X_o)`. The equality eliminating the
vacuous binder in `A_e` holds because a constant map has that same
value as both its least and greatest fixed point. The outer greatest
block becomes

\[
 \nu(X_e,X_o).\,
                  (\langle a\rangle X_o,D(X_o)).
\]

Applying the greatest version of the binary identity gives

\[
 B_o=\nu x.\,D(x),\qquad
 B_e=\nu y.\,\langle a\rangle B_o
                        =\langle a\rangle B_o.
\]

Thus its initial component is the ordinary scalar formula

\[
 \boxed{
  \langle a\rangle\nu x.\,\mu z.\,
       \left((P\land\langle a\rangle\langle a\rangle x)
             \lor(\neg P\land\langle a\rangle z)\right)
       }.
\]

This example can also be checked directly from the games, independently
of the general parity expression. The first diamond changes `e` to
`o`. While in `o`, a false `P` uses one edge and returns to the inner
least variable `z`; this can happen finitely many times between even
returns, but doing it forever loses. A true `P` uses one edge from `o`
to `e` and the next edge from `e` to `o`, returning to the outer greatest
variable `x`. Infinitely many such returns win because that outer
variable has the lower even priority. An existential strategy must
select the disjunct whose literal is true: otherwise Forall challenges
that literal and wins. In the true disjunct Forall can either end at
its true literal, a harmless immediate Exists win, or continue through
the modal conjunct. All modal conjuncts require real edges. Thus an
automaton strategy induces a formula strategy by these true-literal
choices, and a winning formula strategy induces an automaton strategy
by following the modal conjuncts. Every infinite continuing play has
the stated matching parity, and dead diamonds lose in both games.
The scalar formula therefore has exactly the acceptance behavior
claimed for this particular two-control automaton; it need not have
literally the same collection of finite plays.

## 8. Conclusion and boundaries

The binary identity is proved for both fixed-point signs, uniformly in
external parameters. Finite induction removes every finite same-sign
simultaneous block by explicit capture-avoiding scalar substitution.
The component translation removes a finite control product and its tag
vocabulary while preserving all free parameter meanings and all enclosing
binding scopes. Nested blocks are handled without exchanging unlike
signs.

What remains outside this note is the independent general proof that
the chosen tagged-product nested fixed-point expression denotes the
automaton's winning region. Once that proof is supplied, no additional
simultaneous fixed-point theorem, scalarization oracle, or finite-model
assumption is required for the reverse translation.
