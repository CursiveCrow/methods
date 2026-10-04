# Emerson-Jutla parity formulas and history-free strategies

Date: 2026-09-06.

## Purpose and sources

This note supplies a proof of the nested formulas in the manuscript's
`Parity fixed points and determinacy` paragraph. It uses the evaluation-game
theorem and positional determinacy already proved in
`handbook/parts/p09/presentations/n-c-018.tex`, under the labels
`sec:p09-mu-evaluation-game` and `sec:p09-mu-game-truth-proof`, and the
subsequent arbitrary-arena positional-determinacy proof. It supplies no
second general determinacy argument.

The primary source is Emerson and Jutla, *Tree Automata, Mu-Calculus and
Determinacy*, [Definition 4.0 and Theorems 4.1-4.4, PDF pages 7-9](https://www.cs.cornell.edu/courses/cs6860/2021sp/Handouts/EmersonJutla91.pdf).
Definition 4.0 uses the largest recurring color. Theorems 4.1 and 4.2 print
the two formulas below; Corollary 4.3 gives parity determinacy. Section 4.2
defines history freedom by identical remaining partial game trees and
Theorem 4.4 proves the corresponding strategy result. The source's proof
of Theorem 4.1 uses induction and well-foundedness, and its Theorem 4.4 uses
ordinal ranks. The derivations here instead use the manuscript's existing
game results, with the representation maps made explicit.

## 1. Exact arena and parameter conventions

Work in ZFC and fix a set-sized, total, bipartite arena

\[
 V=O\mathbin{\dot\cup}A,\qquad
 E\subseteq(O\times A)\cup(A\times O).
\]

Every vertex has a nonempty set of successors. Player I chooses successors
at vertices in `O`; Player II chooses at vertices in `A`. There is no
finiteness or countability assumption on either the arena or its branching.
The source case is an unfolded tree rooted at a vertex of `O`.

Fix `n >= 0` and a coloring

\[
 c:V\longrightarrow\{0,\ldots,n\},\qquad
 (o,a)\in E\Longrightarrow c(a)=c(o).
 \tag{1}
\]

The proposition `color_i`, written `C_i` below, holds exactly where
`c(v)=i`. Thus the color predicates partition the vertex set. An infinite
play from an OR vertex has the form

\[
 o_0,a_0,o_1,a_1,o_2,a_2,\ldots.
 \tag{2}
\]

Its **round trace** is `o_0,o_1,...`. By (1), a color occurs infinitely often
on the full play exactly when it occurs infinitely often on the round
trace. Let `even_n` mean that the largest such color is even, and `odd_n`
mean that it is odd. These are complementary because the color range is
finite and every play is infinite.

Fix a target set `T` of OR vertices. The event `F T` means that some `o_j`
belongs to `T`, including `j=0`. Equivalently, stop the play at its first
target OR vertex and award it to the player whose reach-target objective
is being considered. A target need not be reached within a bound uniform
over all plays of a winning strategy.

If the displayed parameter `t` is a formula, first fix the environment of
all of its free variables and set

\[
 T=O\cap\llbracket t\rrbracket_\eta.
 \tag{3}
\]

Choose all `x_i` fresh for `t` and its environment. For the proof, replace
`t` by a fresh proposition `P` denoting `T` on `O`. Semantic substitution
then gives the displayed formula with `t` restored. This treatment permits
nested fixed points inside `t` and open external parameters without making
their truth depend on the new `x_i` binders. In particular, `t` is a target
condition; it is not the name of the input tree.

The printed two-step formulas test the target on the round trace. An
alternative convention that tests it at every AND and OR vertex requires
a different body; see Section 8.

Write

\[
\begin{aligned}
 I_n(T)&=\{o\in O:\text{I has a strategy forcing }even_n\lor F T\},\\
 II_n(T)&=\{o\in O:\text{II has a strategy forcing }odd_n\lor F T\}.
\end{aligned}
\tag{4}
\]

These definitions refer to separate objectives. For nonempty `T`, they
are not two complementary winning regions of one game: both players are
awarded success upon reaching `T` in their respective objectives.

The source also sets `I_(-1)(T)=T`. Treat this as the boundary convention
for its induction, with no permitted continuing color. It is the target
test itself, rather than a claim about ordinary reachability in an arena
that still permits moves of unspecified colors. One may set
`II_(-1)(T)=T` in the symmetric induction as well.

## 2. The two round predecessor operations

For `U` contained in `O`, define

\[
\begin{aligned}
 P_I(U)
  &=\{o\in O:\exists a\,[E(o,a)\land
                   \forall o'\,(E(a,o')\Rightarrow o'\in U)]\},\\
 P_{II}(U)
  &=\{o\in O:\forall a\,[E(o,a)\Rightarrow
                   \exists o'\,(E(a,o')\land o'\in U)]\}.
\end{aligned}
\tag{5}
\]

Here `EX` and `AX` are the diamond and box for the single successor
relation `E`. Thus `P_I(U)` is the OR restriction of `EX AX U`, and
`P_II(U)` is the OR restriction of `AX EX U`. The quantifier order must
remain as written: I moves first in each round, and II observes that
choice before responding. Flattening a round to one ordinary relational
edge would discard this distinction.

Both operations are monotone. With complements taken in `O`, De Morgan
duality gives

\[
 O\setminus P_I(O\setminus U)=P_{II}(U).
 \tag{6}
\]

Although modal formulas are interpreted over `V`, their values at OR
vertices depend only on the OR restrictions of the variable valuations:
each recursive occurrence is reached after exactly two modal moves.
Restriction to `O` therefore commutes with each body operation. It also
commutes with unions and intersections, so induction on the transfinite
approximants shows that it commutes with each nested least or greatest
fixed point. We may consequently compute all the displayed fixed points
in `P(O)` using (5). There is no assumption about valuations on the
intermediate AND vertices.

## 3. Exact nested formulas, including n = 0

Define the two binder sequences for every `i >= 0` by

\[
\lambda_i=
 \begin{cases}\nu&i\text{ even},\\\mu&i\text{ odd},\end{cases}
\qquad
\bar\lambda_i=
 \begin{cases}\mu&i\text{ even},\\\nu&i\text{ odd}.\end{cases}
\tag{7}
\]

Put

\[
\begin{aligned}
 \Phi_n^I(P)
 &=\lambda_n x_n.\lambda_{n-1}x_{n-1}.\cdots\lambda_0x_0.
     \left[P\lor\bigvee_{i=0}^n(C_i\land EX\,AX\,x_i)\right],\\
 \Phi_n^{II}(P)
 &=\bar\lambda_n x_n.\bar\lambda_{n-1}x_{n-1}.\cdots\bar\lambda_0x_0.
     \left[P\lor\bigvee_{i=0}^n(C_i\land AX\,EX\,x_i)\right].
\end{aligned}
\tag{8}
\]

For `n >= 1`, the second prefix agrees with the source's notation
`lambda_(n-1) x_n ... nu x_1 mu x_0`. Definition (7) also covers the
`n=0` endpoint without needing a negative-index convention for
`lambda_(-1)`. Equivalently, extending the parity rule to that index
would set `lambda_(-1)=mu`. Explicitly,

\[
 \Phi_0^I(P)=\nu x_0.(P\lor(C_0\land EX\,AX\,x_0)),\qquad
 \Phi_0^{II}(P)=\mu x_0.(P\lor(C_0\land AX\,EX\,x_0)).
 \tag{9}
\]

The claim is

\[
 O\cap\llbracket\Phi_n^I(P)\rrbracket=I_n(T),\qquad
 O\cap\llbracket\Phi_n^{II}(P)\rrbracket=II_n(T).
 \tag{10}
\]

## 4. Proof by the evaluation game

### Player I

Consider the evaluation game of `Phi_n^I(P)` at an OR vertex. Its
existential player represents I; its universal player represents II.
At every visit to the body, the existential player can choose the target
disjunct `P`. This ends successfully exactly on `T`.

When continuing at an OR vertex of color `i`, a winning existential
strategy must choose its actual color disjunct: any different choice lets
the universal player challenge a false color literal. At the actual
disjunct, the universal player can challenge the true literal, ending
successfully for the existential player, or continue into `EX AX x_i`.
The diamond selects an AND successor by I's choice; the box then selects
an OR successor by II's choice. The resulting occurrence of `x_i` returns
to its binder, traverses the remaining finite prefix, and reaches the
body at that new OR vertex.

Thus every infinite continuing evaluation play projects to (2), and
its successive bound-variable returns are

\[
 x_{c(o_0)},x_{c(o_1)},x_{c(o_2)},\ldots.
 \tag{11}
\]

Conversely, every play of the original arena expands in this manner if
the universal player always continues past true color guards. Each round
has finitely many syntax moves and exactly two arena moves. There is no
infinite play trapped in the Boolean or binder administration.

For a completely explicit priority comparison, choose an even integer
`M >= n` and put `r_I(i)=M-i`. This reverses the order of colors and
preserves their parity. The literal evaluation-game priorities from the
manuscript, at depth `n-i`, are

\[
 \omega_I(x_i)=2(n-i)+(i\bmod2).
 \tag{12}
\]

As `i` increases, these priorities strictly decrease; their parity is
that of `i`. Hence (12) and `r_I` give the same winner on every sequence
of variable returns. All other nonterminal priorities are larger
defaults. By (11),

\[
 \min\operatorname{Inf}_{r_I}=M-\max\operatorname{Inf}_c.
 \tag{13}
\]

The existential player wins an infinite evaluation play exactly when
the original play satisfies `even_n`.

An I-strategy for `even_n or F T` gives a winning evaluation strategy:
choose `P` at the first target, otherwise choose the true color and copy
the I-move. All guard challenges win, and any infinite remaining play
avoids the target and has even winning parity. Conversely, from a winning
evaluation strategy maintain one virtual evaluation history while playing
the arena. Before the first target it cannot select `P` or a wrong color,
because either would permit immediate defeat. Continue past true guards,
copy its diamond choice, and enter the actual opponent's box choice into
the virtual history. If a target is reached, the objective is already
satisfied; otherwise every infinite play expands to a winning evaluation
play. This constructs one coherent strategy, not a union of separately
selected strategies. The established evaluation-game theorem proves the
first equality in (10).

### Player II

Now the existential evaluation player represents II, and the universal
evaluation player represents I. Target and color-guard choices work
exactly as above. The continuing subformula is `AX EX x_i`: the universal
player first chooses the AND successor, which is precisely I's original
move at the OR vertex, and the existential player then chooses the OR
successor, which is II's move at that AND vertex. No ownership of the
original arena has been silently reversed.

The variable-return sequence is still (11), while the priorities are

\[
 \omega_{II}(x_i)=2(n-i)+(1-(i\bmod2)).
 \tag{14}
\]

They reverse the color order and have the opposite color parity. They
are equivalent for parity evaluation to `r_II(i)=M-i+1`. Consequently the
existential player now wins exactly when the largest recurring original
color is odd. The same virtual-history translations, with the roles just
identified, establish the second equality in (10).

These arguments prove the formulas for both parities of `n`, including
the base case. They use neither finite branching nor finite convergence
of fixed-point approximants. Restoring the parameter formula by (3) and
semantic substitution proves the stated `I_n(t)` and `II_n(t)` identities.

## 5. Duality and the precise determinacy specialization

For a monotone operation `F` on a powerset, define
`F^d(U)=O \ F(O \ U)`. Complementation exchanges fixed points of `F`
and `F^d` and reverses inclusion. Therefore it exchanges their least and
greatest fixed points. Apply this identity successively to the nested
prefix in (8), using (6).

Because exactly one `C_i` holds, the Boolean identity

\[
 \bigwedge_{i=0}^n(\neg C_i\lor Y_i)
       =\bigvee_{i=0}^n(C_i\land Y_i)
 \tag{15}
\]

holds pointwise. Define

\[
 \Psi_n^{II}(U)=
 \bar\lambda_n x_n.\cdots\bar\lambda_0x_0.
 \left[U\land\bigvee_{i=0}^n(C_i\land AX\,EX\,x_i)\right].
 \tag{16}
\]

The exact complement identity is

\[
 O\setminus I_n(T)=\llbracket\Psi_n^{II}(O\setminus T)\rrbracket_O.
 \tag{17}
\]

The right side describes II's objective `odd_n AND G(not T)`. It is not
`II_n(T)` and in general is not `II_n(O \ T)`. Its conjunction with the
safety parameter is essential. Dually, complementing `II_n(T)` gives I's
even-parity-and-avoidance objective.

To identify (17) with the complementary game objective independently of
syntax, stop at `T` and award that terminal to I. Totalize the terminals
with an even absorbing priority in the least-recurring presentation.
At other vertices use `M-c`. The established positional-determinacy
theorem applies to this set-sized arena, preserving all original
successor choices and their outcomes. II wins precisely when the target
is avoided forever and the largest recurring original color is odd.
This is an application of the earlier theorem, not a new proof of it.

For **pure parity**, set `T=emptyset`. Then the safety conjunct in (16)
is true, and the absent target disjunct in (8) is false. Thus

\[
 I_n(\varnothing)=O\setminus II_n(\varnothing).
 \tag{18}
\]

Every OR root therefore has a winner, which is the asserted parity
determinacy consequence. For an AND root, introduce one fresh OR root
with that vertex as its only successor and give the new root the same
color. Its first move is forced and its added finite prefix does not
change parity. This reduces that case to (18).

The qualification `T=emptyset` cannot be omitted: for `T=O`, both
`I_n(T)` and `II_n(T)` equal `O`. When `t` is open, formula-level notation
for its negation must also respect the fixed external environment;
syntactically dualizing while keeping the same free-variable valuations
is not automatically semantic complementation. The fresh target atom
used above avoids that ambiguity.

## 6. Identical remaining game trees and the quotient arena

Positionality on a tree's occurrence vertices alone does not establish
the source's history freedom: different occurrences are different tree
vertices, even when their future games are identical. A quotient is
required.

Present the given game tree by a prefix-closed set `D` of finite move
sequences over a set of move names. Each node carries its owner and
color. For a node `u`, its remaining partial game tree `gamma_u` has
relative domain

\[
 D_u=\{w:uw\in D\}
 \tag{19}
\]

and the inherited owner/color labeling `w |-> label(uw)`. Define

\[
 u\sim v\quad\Longleftrightarrow\quad\gamma_u=\gamma_v.
 \tag{20}
\]

Equality here includes the available relative move names and their
continuations. Thus it gives the exact meaning of making the same
corresponding successor choice. Unspecified isomorphism of unordered
trees would not by itself name a corresponding successor. The source
uses identical partial games, and (19)-(20) make that notion explicit.

Let `Q=D/sim`. The map `p(u)=[u]` preserves owners and colors. Moreover,
if `u~v`, then a move name `a` is available at `u` exactly when it is
available at `v`, and

\[
 ua\sim va.
 \tag{21}
\]

Therefore define an edge in the quotient, retaining its move name, by

\[
 [u]\xrightarrow{a}[ua].
 \tag{22}
\]

This is well defined and total. The quotient is a set because its
vertices are equivalence classes of nodes of this one set-sized tree;
it does not require a set of all possible game trees. It may have cycles
even though the original occurrence tree has none.

Every tree play projects to a quotient play with the same owner and
color sequence. Conversely, after fixing a starting occurrence `u`,
every legal sequence of named quotient moves lifts recursively to a
unique tree play from `u`, by (21). These statements apply to finite
histories as well as infinite plays.

Winning strategies transfer in both directions. A quotient strategy
lifts by projecting the current history and selecting its prescribed
move name. To transfer a tree strategy to the quotient from `[u]`, keep
the unique virtual tree history starting at `u`: copy the tree strategy
on its player's turns, and extend that history with the opponent's actual
quotient move on the other turns. Every resulting quotient play lifts to
a play compatible with the original winning strategy and has the same
parity. This transferred strategy may depend on history, which is
sufficient for the next step.

Apply the already proved positional-determinacy theorem to `Q`, using
the even reversal `M-c` if the theorem is stated with least recurring
priorities. Since the player's winning tree strategy has just transferred,
its starting quotient vertex belongs to that player's winning region.
The theorem supplies a positional strategy on that region. If the theorem
selects only a successor vertex, choose once for each owned quotient
vertex a move name realizing that selected edge. Retaining this choice
also handles two distinct moves leading to the same quotient vertex.

Lift this positional strategy to the tree. At any two occurrences with
identical remaining partial game trees, it chooses the same move name
because both project to the same quotient vertex. Every resulting play
projects to a winning quotient play. Extend the strategy, if desired,
to the player's other quotient vertices by arbitrary fixed legal choices;
this makes it a total strategy and retains identical choices even at
unreachable occurrences. This proves the precise history-free conclusion
of Theorem 4.4 for either player.

For the reach-target extension, include membership in `T` in the
remaining-tree labeling and stop at the target before taking an outgoing
move. Equality must preserve this marking, or it need not preserve the
remaining objective. The source's pure-parity conclusion needs only the
owner/color/move data. This notion remains distinct from the automaton
notion based on a current input node and automaton control in Definition
2.7.

## 7. Why the hypotheses do actual work

1. **Color-copy condition.** If every OR node on a unique infinite chain
   has color 0 and every AND node has color 1, `nu x.EX AX x` holds at
   its root, but the largest color recurring on the full play is odd.
   Condition (1), or an explicit convention of considering only OR colors,
   is needed for the identification.

2. **Round targets.** On a unique infinite chain of color 1, put the
   target only at AND nodes. From an OR root, the printed I-formula is
   false: every recursive return is at an OR node and the sole recurrent
   variable is least. Nevertheless every full play immediately visits
   a target AND node. Thus `F t` in (10) is a round-trace event.

3. **Active color range.** The formula for `n` has no continuing disjunct
   at a vertex of color greater than `n`. Without a target at that
   vertex, it loses immediately in its evaluation game. For example,
   on a unique round trace with colors `0,1,0,1,...` and empty target,
   the `n=0` I-formula is false, whereas a condition that merely ignores
   color 1 when computing `even_0` would be true. Apply (10) to colors
   `0,...,n`; in particular use `n=m` for the source's whole game.
   Intermediate truncated formulas require explicitly stopping at or
   treating the excluded colors as boundary conditions. They cannot
   silently inherit an objective that just ignores higher colors.

4. **Parity of the reversal.** Choosing even `M` is essential for
   `M-c` to preserve the even player's objective. An odd `M` swaps
   the parity, and is valid only when that swap is accounted for.

5. **Infinite branching.** A single round can offer arbitrarily many
   choices, but still consists of two moves on each play. All strategy
   translations above use these actual choices. No compactness, finite
   response enumeration, finite convergence, or uniform hitting-time
   bound is used.

## 8. If targets must be detected at every vertex

This is a separate representation convention, not the literal body in
(8). If `T` is a target predicate on all of `V`, the correct continuation
bodies at OR vertices are

\[
\begin{aligned}
 H_I(\vec x)
 &=T\lor\bigvee_{i=0}^n
    \left(C_i\land EX\bigl(T\lor AX\,x_i\bigr)\right),\\
 H_{II}(\vec x)
 &=T\lor\bigvee_{i=0}^n
    \left(C_i\land AX\bigl(T\lor EX\,x_i\bigr)\right).
\end{aligned}
\tag{23}
\]

Keep the prefixes from (8). The additional target test occurs at the
AND vertex before its owner's next move. The same evaluation-game proof
then gives the full-play eventual-target objective. The original formulas
are recovered if AND targets are absent, or if an explicit convention
makes every target AND vertex's continuing OR successors targets as well,
so that detecting the target one half-round later changes no outcome.

## 9. Incorporation corrections and dependency boundary

The existing manuscript paragraph can be made precise with the following
changes when its full proof is incorporated:

- State that the displayed formulas are evaluated at OR roots, with target
  truth checked at OR round boundaries and active colors `0,...,n`.
- Define both binder sequences in (7), or separately state the `n=0`
  II-formula, or explicitly extend the parity rule by
  `lambda_(-1)=mu`; the existing `lambda_(n-1)` notation needs this
  endpoint convention.
- Specialize to `t=bottom` before asserting that the two displayed
  formulas are complements. For a general parameter, use the
  reachability/safety duality in (16)-(17).
- Give the explicit variable-return/priority correspondence and the
  quotient map for identical remaining partial game trees. Invoking
  positionality on occurrence vertices without that quotient is
  insufficient for the source's precise history-free condition.
- Attribute the supplied derivation to the established manuscript game
  theorems while retaining the source's actual printed proof methods as
  source context.

No new mathematical dependency remains for these corrected statements
beyond the established evaluation-game theorem, semantic substitution
and fixed-point duality, and uniform positional determinacy for arbitrary
set-sized finite-priority arenas. If the intended statement instead
requires targets at every AND and OR node, or the literal truncated
`even_k` reading on a larger color range, it requires the corresponding
explicit change described above; (8) does not prove those readings.

Only this note was created. No manuscript files, tests, builds, renders,
or other agents were created or changed by this task.
