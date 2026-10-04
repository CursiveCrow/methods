# Cover modalities and the restricted-automaton-to-ANF construction

Date: 2026-09-06. Status: supplied mathematical proof. This note proves
capture-avoiding substitution closure of the specified ANF grammar,
ANF-preserving same-sign Bekic elimination, and a cover automaton to guarded,
well-named ANF translation with the actual successor-first box game. It does not prove
the general automaton-to-cover simulation, a deterministic trace-monitor
construction, or any output-size or alternation-depth bound.

The evaluation-game truth theorem, least-recurring-even convention, and
ordinary fixed-point semantics are those already proved in
`handbook/parts/p09/presentations/n-c-018.tex`. The source basis is
[Bradfield--Stirling, acquired preprint, Section 5.4 and Proposition
5.4](https://www.pure.ed.ac.uk/ws/files/16483207/Modal_Mu_Calculi.pdf).
That section introduces covers, a restricted automaton form, and ANF; the
construction below supplies the detailed proof for an already given cover
automaton. The source's Theorem 5.3, transforming a general modal automaton
to the restricted form, is a separate nontrivial obligation and is not
established by the present argument.

## 1. Covers and their semantics

Let `a` be an action and let `Gamma` be a finite set of positive-normal
modal fixed-point formulas. Define the cover abbreviation

\[
 \nabla_a\Gamma
   :=\left(\bigwedge_{\psi\in\Gamma}\langle a\rangle\psi\right)
      \land[a]\left(\bigvee_{\psi\in\Gamma}\psi\right).
\]

Empty conjunctions are `top` and empty disjunctions `bottom`. In particular

\[
 \nabla_a\varnothing=[a]\bot.
\]

For an environment `eta`, write `V_psi` for the denotation of `psi`.
Directly from the diamond and box clauses,

\[
\begin{split}
 s\models_\eta\nabla_a\Gamma
 \quad\Longleftrightarrow\quad
 &\bigl(\forall\psi\in\Gamma\ \exists t\,
          (R_a(s,t)\land t\in V_\psi)\bigr)\\
 &\land\bigl(\forall t\,
       (R_a(s,t)\Rightarrow
          \exists\psi\in\Gamma\ t\in V_\psi)\bigr).
\end{split}
\]

The first conjunct requires a witness for every listed target. The second
requires the listed targets to cover every successor. The target chosen
in the second conjunct may depend on that successor.

At an `a`-dead-end, the empty cover is true and every nonempty cover is
false. If `top` is a member of `Gamma`, it supplies an always-true target,
but its diamond still requires a successor. For example,

\[
 \nabla_a\{\top\}\equiv\langle a\rangle\top,
 \qquad
 \nabla_a\{\psi,\top\}\equiv\langle a\rangle\psi.
\]

The second equivalence follows because a witness for `psi` also witnesses
`top`, and the box disjunction is true at every successor. These identities
include the cases where `psi` is itself a constant.

Cover expansion is positive in each argument. For a fixed finite index
set `I`, if `psi_i <= theta_i` for every `i`, then

\[
 \nabla_a\{\psi_i:i\in I\}
       \leq\nabla_a\{\theta_i:i\in I\}.
\]

This is pointwise monotonicity of the arguments. It is not a claim of
monotonicity under adding or deleting members of the target set: changing
that set changes both witness demands and the covering condition.

### Why the box is a genuinely different one-step form

The box part is `[a](q or r)`, not `[a]q or [a]r`. In its game, Forall
chooses an `a`-successor first, and Exists then chooses `q` or `r` there.

Indeed, consider one-step target assignments at a root with two successors:
one satisfies `q` only and one satisfies `r` only. Compare a second root
with those two successors and an additional successor satisfying neither.
At both roots, `<a>q` and `<a>r` are true, and `[a]q` and `[a]r` are false.
But `[a](q or r)`, and consequently the cover `{q,r}`, is true only at
the first root. Thus even an arbitrary Boolean combination of those four
old modal atoms cannot supply the required general cover interpretation.
Nothing below rewrites this box as such a Boolean combination.

## 2. The precise ANF grammar

Fix distinct namespaces for proposition constants `P` and fixed-point
variables `X`. A literal is `P` or `not P`. Let `chi_L` be the conjunction
of a finite collection `L` of proposition literals, with empty collection
giving `top`. Contradictory literal collections are permitted syntactically
and denote `bottom`.

The class `ANF` is the least class satisfying all the following clauses:

1. `top`, `bottom`, proposition literals, and fixed-point variables are ANF.
2. If `alpha` and `beta` are ANF, then `alpha or beta` is ANF.
3. If `alpha` is ANF, then `mu X.alpha` and `nu X.alpha` are ANF.
4. If `I` is finite, the actions `a_i` for `i in I` are pairwise distinct,
   and each `Gamma_i` is a finite set of ANF formulas, then

   \[
    \chi_L\land\bigwedge_{i\in I}\nabla_{a_i}\Gamma_i
   \]

   is ANF.

All fixed-point-variable occurrences in this grammar are positive. A
cover is an abbreviation for the ordinary modal formula in Section 1,
not an additional semantic fixed-point operation. With `I` empty, the
last clause is simply a literal conjunction. With `L` empty and a single
action, it is a cover. No closure under arbitrary conjunction of ANF
formulas is asserted.

### Capture-avoiding substitution closure

**Lemma.** If `alpha` and `beta_1,...,beta_n` are ANF and
`X_1,...,X_n` are distinct variables, then the simultaneous substitution
of the `beta_i` for the free `X_i` in `alpha` is ANF. The substitution
does not recursively substitute into the formulas being inserted.

**Proof.** First rename bound variables of `alpha` away from the free
variables of all the `beta_i` and from the designated substitution
variables, preserving each binder's links. Alpha-renaming preserves every
clause of the grammar. Now proceed by structural induction on `alpha`.

Constants and proposition literals are unchanged. A designated free
variable is replaced by its specified ANF formula; any other variable is
unchanged. The disjunction case uses the two induction hypotheses. At a
fixed-point binder, freshness makes substitution commute with passage to
the body, and the induction hypothesis followed by that same binder gives
ANF again. Equivalently, before fresh renaming, substitution stops at a
binder that binds its designated variable.

At a clause, proposition literals remain unchanged and each finite target
set `Gamma_i` is replaced by its finite image under the substitution.
Every resulting target is ANF by induction. The action labels remain
pairwise distinct, so this is another admitted clause. If two targets
become identical, discarding the repeated member leaves the same expanded
formula up to idempotence of conjunction and disjunction. The empty-target
and empty-action cases need no exception. These are all grammar cases. QED.

Sequential capture-avoiding substitutions preserve ANF by repeated
application of the lemma. Thus any finite formula composition of this
specified kind is admitted; arbitrary conjunction remains unnecessary.

### The additional guardedness invariant

A variable `X` is guarded in a body `alpha` when every free occurrence
of `X` in that body lies below a modality. A binder `sigma X.alpha` is
guarded when `X` is guarded in `alpha`. Guarded ANF is the subclass in
which every binder is guarded. Modal depth here is measured in the cover
expansion: each occurrence of every target formula is below the cover's
diamond or box. A modality outside a binder does not guard that binder's
body; for example, putting `nu X.X` inside a cover does not repair its
unguarded `X`-binder.

There are two distinct substitution facts.

1. If every binder in `alpha` and in each replacement `beta_i` is guarded,
   their capture-avoiding substitution also has every binder guarded.
   Occurrences already bound in `alpha` keep their guarding modalities;
   freshness prevents replacement formulas from introducing newly captured
   occurrences. A copied binder in a replacement keeps its own guarded body.
2. To preserve guardedness of a designated **free** parameter `Z`, require
   its untouched occurrences in `alpha` to be guarded. For every replacement
   containing a free `Z`, it is sufficient that either all of that
   replacement's free `Z` occurrences are guarded or all positions at which
   that replacement is inserted are guarded in `alpha`. Every resulting
   occurrence then has a modality on its path. In particular, if every free
   variable of `alpha` is guarded, substitution at its free-variable
   positions keeps every remaining free variable guarded, irrespective of
   whether an inserted formula's free variables were guarded by themselves.

Both assertions follow by tracing an occurrence to an unchanged occurrence
or to an inserted copy; covers, binders, and Boolean syntax introduce no
other occurrences. They do not assert that an unguarded free variable is
guarded merely because the formula has no unguarded binders. The bare
formula `X` is ANF and has no binders, but its free `X` is unguarded.

## 3. Same-sign Bekic elimination, including ANF preservation

For complete lattices `L,M`, let `f:L x M -> L` and `g:L x M -> M`
be monotone. Fix one sign `sigma`, either least or greatest, and put

\[
 h(x)=\sigma y.g(x,y),\qquad
 a=\sigma x.f(x,h(x)),\qquad b=h(a).
\]

The parameter map `h` is monotone by fixed-point comparison. For least
fixed points, a pre-fixed point of the larger operator is pre-fixed for
the smaller one; for greatest fixed points, a post-fixed point of the
smaller operator is post-fixed for the larger one. Applying this to
`g(x,-) <= g(x',-)` proves the comparison when `x <= x'`.

The fixed-point equations give `a=f(a,b)` and `b=g(a,b)`. If `sigma=mu`
and `(u,v)` is pre-fixed for `(f,g)`, then

\[
 h(u)\leq v,\quad
 f(u,h(u))\leq f(u,v)\leq u,\quad
 a\leq u,\quad b=h(a)\leq h(u)\leq v.
\]

Hence `(a,b)` is below every pre-fixed pair and is the simultaneous least
fixed point. If `sigma=nu` and `(u,v)` is post-fixed, then

\[
 v\leq h(u),\quad
 u\leq f(u,v)\leq f(u,h(u)),\quad
 u\leq a,\quad v\leq h(u)\leq h(a)=b.
\]

Hence `(a,b)` is above every post-fixed pair and is the simultaneous
greatest fixed point. Both proofs allow fixed external parameters.

Now suppose `f` and `g` are given by ANF component bodies
`alpha(x,y,zbar)` and `beta(x,y,zbar)`, where `zbar` are external
variables. At the formula level define

\[
\begin{split}
 H(x,\bar z)&=\sigma y.\beta(x,y,\bar z),\\
 A(\bar z)&=\sigma x.\alpha(x,H(x,\bar z),\bar z),\\
 B(\bar z)&=H(A(\bar z),\bar z).
\end{split}
\]

Every displayed substitution is capture-avoiding. `H` is ANF by the
binder clause; `A` is ANF by substitution closure followed by the binder
clause; `B` is ANF by substitution closure. Their denotations are exactly
the simultaneous solution just proved. Rename copied internal binders
freshly, and keep the external parameters free until their surrounding
binders are applied.

For a finite `k`-component same-sign system, induct on `k`. The case
`k=1` is a scalar binder. For `k>1`, regard the first coordinate as `x`
and group the other coordinates in the second lattice. Inductively solve
that `(k-1)`-component system with `x` as a parameter, obtaining ANF
formulas `H_2(x,zbar),...,H_k(x,zbar)`. Put

\[
\begin{split}
 A_1(\bar z)&=\sigma x.
   \alpha_1(x,H_2(x,\bar z),\ldots,H_k(x,\bar z),\bar z),\\
 A_j(\bar z)&=H_j(A_1(\bar z),\bar z)\quad(2\leq j\leq k).
\end{split}
\]

Substitution closure proves that every `A_j` is ANF. Binary Bekic applied
to the grouped lattices proves that their tuple is the simultaneous
solution. This proves finite same-sign scalarization and ANF preservation.

For nested simultaneous blocks, eliminate the inner block with all outer
variables as free parameters, and then proceed outward. This preserves
the given nested solution. It neither commutes mixed signs nor preserves
a literal binder pattern after duplication. The argument is effective
and finite; it makes no economical-size claim.

### Guarded version of the scalarization lemma

The following are sufficient additional hypotheses for a same-sign block:

- every binder already present in each component body is guarded;
- every coordinate variable being solved is guarded at each of its free
  occurrences in every component body.

Then the scalar components just constructed have only guarded binders.
Moreover, any external parameter guarded in every component body remains
guarded wherever it is free in each scalar component.

For the binary construction, `y` is guarded in `beta`, so its new binder
in `H` is guarded. The free `x` occurrences in `H` are guarded because
those in `beta` were; each existing binder remains guarded. In `A`, old
free `x` occurrences in `alpha` were guarded, and any inserted free `x`
occurrences have both the guarding available inside `H` and the guarding
at the replaced `y` positions in `alpha`. Consequently the new `x` binder
is guarded. In `B=H(A,zbar)`, capture-avoiding substitution preserves all
existing and copied guarded binders. For any designated external `Z`,
the free occurrences inherited from the component bodies were guarded,
and the substitution facts above preserve that property at each step.

For `k` coordinates, the first coordinate `x` is a guarded external
parameter of the remaining `(k-1)`-coordinate system. The induction
hypothesis therefore gives guarded `H_j` with free `x` still guarded;
the same binary reasoning completes the inductive step. This also proves
preservation of any external parameters guarded throughout the original
component bodies.

The guarding hypothesis is essential for this conclusion. The one-component
body `X` is ANF, and same-sign scalarization may give `nu X.X`, which is
ANF but is not guarded ANF. The unrestricted substitution and Bekic lemmas
above assert ANF membership, not guardedness, without these extra hypotheses.

## 4. An already given cover automaton and its game

Let a cover automaton be

\[
 \mathcal C=(Q,2^{P_0},\delta,q_0,\Omega),
 \qquad Q\ne\varnothing,\quad
 \Omega:Q\to\{0,\ldots,d\},
\]

with finite `Q`, finite proposition set `P_0`, and a finite transition
table. For each `(q,A)`, its transition is a finite disjunction of clauses

\[
 C_{q,A,j}=\bigwedge_{a\in L_{q,A,j}}\nabla_a B_{q,A,j,a},
 \qquad B_{q,A,j,a}\subseteq Q\cup\{\top\},
\]

where each `L_{q,A,j}` is a finite set of distinct action labels. An empty
disjunction is `bottom` and an empty clause is `top`. This includes the
source's restricted form that lists every used action in every clause.
Here an omitted action imposes no constraint. The `top` target is not a
control state and carries no recurring priority.

For a model `T=(S,(R_a),V)` and a current control position `(s,q)`, read
the actual proposition letter `ell(s)` and emit priority `Omega(q)`.
The acceptance game then operates as follows.

1. Exists chooses a transition clause. If none exists, Exists loses.
2. Forall chooses an action-cover conjunct in that clause. If there is
   none, Exists wins.
3. At `nabla_a B`, Forall may select the diamond demand of any `r in B`,
   or may select the box demand.
4. For the diamond demand for `r`, Exists first chooses an `a`-successor
   `t`. If none exists, Exists loses. If `r=top`, the obligation now ends
   with an Exists win; otherwise continue at `(t,r)`.
5. For the box demand, Forall first chooses an `a`-successor `t`. If none
   exists, Exists wins. Exists then chooses a member `r in B` **at that
   chosen successor**. If `B` is empty, Exists loses. For `r=top` the
   obligation ends winning; otherwise continue at `(t,r)`.

This is exactly the evaluation game of the cover expansion, with target
controls treated as continuation ports. A conjunction over an empty set
of diamond demands is `top`; suppressing that additional immediately
winning challenge does not affect the winner. Finite plays use these
terminal outcomes. On infinite plays the least control priority recurring
infinitely often must be even. Each transition episode has finite syntax,
so every infinite play visits control positions infinitely often.

The target selected after a box move may depend on the entire history and
on `t`. No uniform target is selected before that move. There is no
branching restriction on the model, and the game does not need a finite
enumeration of its successor sets.

## 5. A product formula respecting successor-first choice

The previous product construction using only target-indexed real actions
does not directly provide a box over a union of controls. Instead use the
following explicit two kinds of product edges. Its sole purpose is to
prove correctness; these additional actions will disappear from the output.

The product has state set `S x Q`. Lift each original proposition along
the first coordinate, and let fresh tag `E_r` hold exactly at pairs with
second coordinate `r`. For every real action `a`, introduce a fresh
coordinate-preserving action `a^o`; for every control `r`, introduce a
fresh deterministic total control-switch action `h_r`:

\[
\begin{split}
 R_{a^\circ}((s,q),(t,u))
       &\quad\Longleftrightarrow\quad R_a(s,t)\land u=q,\\
 R_{h_r}((s,q),(t,u))
       &\quad\Longleftrightarrow\quad t=s\land u=r.
\end{split}
\]

All these new action symbols are pairwise distinct. The product signature
uses these actions, the lifted propositions, and the tags; no interpretation
of an additional original action on product states is required.

For each priority index `i`, use a fresh variable `X_i` and put

\[
 \kappa_i(r)=\langle h_r\rangle X_i\quad(r\in Q),
 \qquad\kappa_i(\top)=\top.
\]

Transform a transition by preserving its disjunctions and cover clauses
and replacing

\[
 \nabla_a B\quad\text{by}\quad
       \nabla_{a^\circ}\{\kappa_i(r):r\in B\}.
\]

Write the resulting ordinary-modal abbreviation as `delta(q,A)^[i]`.
Use the exact proposition cube `chi_A`, and define

\[
\begin{split}
 \Theta_{\mathcal C}
  &=\bigvee_{q\in Q,\ A\subseteq P_0}
       E_q\land\chi_A\land\delta(q,A)^{[\Omega(q)]},\\
 \Psi_{\mathcal C}
  &=\sigma_0X_0.\sigma_1X_1.\cdots\sigma_dX_d.
                               \Theta_{\mathcal C},\\
 \sigma_i&=\nu\text{ for even }i,\qquad
 \sigma_i=\mu\text{ for odd }i.
\end{split}
\]

Expand covers to view this as an ordinary scalar modal mu formula on the
product. It is closed and positive-normal. Every variable occurrence is
under a real-product modality and then a control-switch modality. This
intermediate product formula need not itself be ANF; the final component
formulas will be.

### Both strategy directions and parity

At `(s,q)` there is exactly one true selector `E_q and chi_ell(s)`.
A wrong selector can be challenged by Forall at a false literal or tag,
so a winning formula strategy must select the correct one. Every guard
challenge at the correct selector wins immediately, including any empty
cube represented by `top`.

In a diamond challenge for `r`, the real-product move reaches `(t,q)`
and the `h_r` move then has the unique successor `(t,r)`. In a box
challenge, Forall first chooses `(t,q)` through `a^o`; Exists **then**
chooses a cover member there and, if it is a genuine control `r`, takes
the unique `h_r` move to `(t,r)`. The next formula control is
`X_{Omega(q)}`. Thus the product implements exactly the cover game's
choice order, not a prior choice of one target for all successors.

Every `top` target terminates true immediately after the real-product
move. Empty covers, empty clauses, false transitions, and absent real
successors have exactly the finite outcomes of Section 4. Control-switch
moves never introduce a dead end or a new choice.

A winning cover-game strategy gives a formula strategy by choosing the
actual selectors and copying its clause, diamond, and successor-dependent
box choices, taking the unique control switches when needed. Maintain the
full virtual cover-game history, so no positionality assumption is used.
Guard or empty-conjunction challenges win immediately; every other play
follows the original play with finite syntax and control-switch moves
inserted.

Conversely, a winning formula strategy determines a cover-game strategy
while retaining its full virtual formula history. At each selector its
choice is correct, as proved above. Let virtual Forall continue into the
transition conjunct. Simulate each actual clause/action/demand choice;
after an actual box successor has been chosen, use the formula strategy's
choice of cover member at that very successor. For diamonds, use its real
successor choice. Insert the unique control switch, when present, and the
forced variable return and binder prefix before starting the next round.
An omitted trivial `top` challenge adds only an Exists-winning finite play.
All histories retained this way follow the winning formula strategy.

For an infinite nonterminal corresponding play with source controls
`q_0',q_1',...`, the formula's variable returns are exactly

\[
 X_{\Omega(q_0')},X_{\Omega(q_1')},\ldots.
\]

The variable `X_i` has `i` proper enclosing binders and hence priority
`g(i)=2i` for even `i`, and `g(i)=2i+1` for odd `i`. This map is strictly
increasing and parity-preserving. All other formula priorities are the
larger default. An infinite play cannot consist solely of administrative
or control-switch moves: each return requires a preceding real-product
move and all intervening syntax is finite. It follows that the two games
have the same least-recurring parity. Both strategy translations therefore
preserve winning for finite and infinite plays.

By the proved evaluation-game truth theorem,

\[
 T^Q,(s,q)\models\Psi_{\mathcal C}
 \quad\Longleftrightarrow\quad
 \exists\text{ wins the cover game from }(s,q).
\]

## 6. Component bodies are ANF before scalarization

For every `i` and `r`, introduce a distinct variable `X_{i,r}`. For a
cover target set `B` define

\[
 B_i^\flat
   =\{X_{i,r}:r\in B\cap Q\}
       \cup\begin{cases}\{\top\},&\top\in B,\\
                          \varnothing,&\top\notin B.
             \end{cases}
\]

For each control `q` define the base component body

\[
 F_q=
  \bigvee_{\substack{A\subseteq P_0\\j\text{ a clause of }\delta(q,A)}}
   \left(\chi_A\land
     \bigwedge_{a\in L_{q,A,j}}
       \nabla_a(B_{q,A,j,a})_{\Omega(q)}^\flat\right).
\]

Every summand is an admitted ANF clause: its guard contains only original
proposition literals, its actions are pairwise distinct, and its targets
are variables or `top`. Therefore every `F_q` is ANF. The construction
uses finite distribution of the selector conjunction across the displayed
disjunction of cover clauses. It never conjoins arbitrary ANF formulas.
Every occurrence of every free coordinate variable `X_{i,r}` is below
a cover modality, and the base bodies contain no binders. Thus they also
satisfy the stronger guarded scalarization hypotheses for every coordinate
and every coordinate that will temporarily be an external parameter.

Given a product environment `eta` for the `X_i`, let

\[
 \eta^\flat(X_{i,r})=\{s:(s,r)\in\eta(X_i)\}.
\]

For the deterministic total switch,

\[
 T^Q,(s,q)\models_\eta\langle h_r\rangle X_i
       \quad\Longleftrightarrow\quad
 s\in\eta^\flat(X_{i,r}).
\]

The coordinate-preserving real action then gives, for each finite target
set `B`,

\[
 T^Q,(s,q)\models_\eta
      \nabla_{a^\circ}\{\kappa_i(r):r\in B\}
 \quad\Longleftrightarrow\quad
 T,s\models_{\eta^\flat}\nabla_a B_i^\flat.
\]

Both existential witnesses and the universal successor condition agree,
including empty successor and target sets and the `top` member. Eliminating
the false selectors, the unique true tag, and distributing over the
remaining finite clause disjunction consequently proves

\[
 \{s:(s,q)\in\llbracket\Theta_{\mathcal C}\rrbracket_{T^Q,\eta}\}
       =\llbracket F_q\rrbracket_{T,\eta^\flat}.
\]

This is the needed component translation at the base of the nested
fixed-point construction. In general notation, the control-switch clause
is `tau_q(<h_r>psi)=tau_r(psi)`, while the real-action clause is
`tau_q(<a^o>psi)=<a>tau_q(psi)` and dually for boxes. The displayed direct
calculation avoids claiming ANF closure for arbitrary expanded conjunctions.

## 7. The nested ANF construction and its semantic induction

Put `F_q^{d+1}=F_q`. For `j=d,d-1,...,0`, form the finite same-sign block

\[
 \sigma_j(X_{j,r})_{r\in Q}.
                (F_r^{j+1})_{r\in Q}
\]

and let `F_q^j` be its scalar `q`-component obtained by the explicit
ANF-preserving Bekic construction of Section 3. At stage `j`, variables
`X_{i,r}` with `i<j` are held as free parameters. All binders and copied
formulas are renamed hygienically. Induction downward on `j` shows that
every `F_q^j` is ANF and that its only possible free variables have indices
`i<j`. Using the guarded scalarization lemma in the same induction shows
that every binder is guarded and every remaining free coordinate parameter
is guarded. In particular

\[
 \varphi_{\mathcal C}:=F_{q_0}^0
\]

is a closed ordinary scalar guarded ANF formula over the original vocabulary.
Renaming its finitely many copied binders globally distinctly makes it
well-named and changes neither ANF membership nor guarding nor denotation.

For correctness, put

\[
 \Psi^{d+1}=\Theta_{\mathcal C},\qquad
 \Psi^j=\sigma_jX_j.\Psi^{j+1}.
\]

We prove the component equality for `Psi^j` and `F_q^j` for every
environment of the outer variables. The base case `j=d+1` was established
in Section 6. For the inductive step, fix all outer variable values and
use the complete-lattice isomorphism

\[
 J:\mathcal P(S\times Q)\longrightarrow\mathcal P(S)^Q,
 \qquad J(U)_r=\{s:(s,r)\in U\}.
\]

Its inverse sends `(U_r)_r` to `union_r (U_r x {r})`; it preserves the
order, arbitrary joins, and arbitrary meets. Varying the value `U` of
`X_j`, the induction hypothesis identifies the body operator of `Psi^j`
with the vector operator whose components are `F_r^{j+1}`, assigning
`X_{j,r}` the component `J(U)_r`. Thus `J` carries pre-fixed and
post-fixed points bijectively to those of the vector operator and carries
its least or greatest fixed point to the simultaneous `sigma_j` fixed
point. Bekic scalarization preserves every component of that fixed point.
This proves the induction step for all fixed outer environments.

At `j=0` there are no outer variables. Combining this induction with the
product-game equivalence gives, for every original model and state,

\[
 T,s\models\varphi_{\mathcal C}
 \quad\Longleftrightarrow\quad
 T^Q,(s,q_0)\models\Psi_{\mathcal C}
 \quad\Longleftrightarrow\quad
 \exists\text{ wins the cover-automaton game from }(s,q_0).
\]

Every step is finite and effective: the input table, exact proposition
cubes, finite component tuples, and scalar substitutions are finite.
The model need not be finite, finitely branching, or total. Formula size
can increase through scalar copying, and no better bound is asserted.

## 8. Precise conclusion and excluded implication

An already given restricted cover automaton has an equivalent closed,
guarded, well-named ANF
formula under the stated game semantics. The proof handles a top target
as an accepting terminal after its real move, and handles the empty cover
as the assertion that there is no matching successor. It preserves the
box challenge's order: successor first, target second.

This establishes the restricted-automaton-to-ANF direction. It does not
show that an arbitrary old-syntax modal automaton has an equivalent cover
automaton. In particular, no determinization, trace-monitor property, or
general-automaton-to-ANF theorem follows merely by putting old transitions
in Boolean disjunctive normal form. That separate simulation must be
proved before combining the present result into a general ANF theorem.

Only this note was created. No manuscript edits, code, software tests,
builds, renders, or additional agents were used.
