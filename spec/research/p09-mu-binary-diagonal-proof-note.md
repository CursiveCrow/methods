# Supplied binary game-tree diagonal proof of alternation strictness

Date: 2026-09-06.

## Status and dependencies

This note gives the full game-tree reduction, productive construction,
prefix-contraction proof, fixed-tree diagonal argument, and a separate
first-level proof. The construction follows Arnold's
[*The mu-calculus alternation-depth hierarchy is strict on binary
trees*, Sections 2--3, printed
p. 333](https://www.numdam.org/item/ITA_1999__33_4-5_329_0.pdf).
The prefix-iteration proof below replaces an appeal to Banach's
theorem. Mathematical details are supplied here, not quoted from the
article.

For the conclusion about the **Niwinski syntax classes**, the following
bridge is a named dependency, being proved separately:

> **Index bridge `B_n`, for `n >= 2`.** Every closed formula in
> `Sigma^N_n`, interpreted on full binary trees over a fixed finite
> alphabet, has an equivalent finite alternating tree automaton with
> priorities in `{1,...,n}`, least-recurring-even acceptance, and
> terminal-free positive Boolean transitions over control/direction
> pairs. Equivalence holds on every tree of that alphabet.

This is stronger than ordinary formula/automaton expressive equivalence;
the rank bound and Niwinski substitution closure are essential. Nothing
below proves or silently assumes this bridge for `n=1`.

Other dependencies are the already established modal evaluation-game
theorem, ordinary transfinite fixed-point semantics, duality of the
positive Niwinski classes, and (only for the last transfer) the full
finite-model property. No automaton-complementation theorem or
topological determinacy theorem is needed in the diagonal argument.

## 1. Canonical full binary trees and the witness formula

For `n >= 2`, put

\[
 A_n=\{c_1,d_1,\ldots,c_n,d_n\},\qquad
 U=\{1,2\}^{*},\qquad \mathcal T_n=A_n^U.
\]

An element `t` is a full binary labelled tree. Its canonical pointed
Kripke model `K_t` has states `U`, root the empty word, and the unique
directional edges `u -1-> u1` and `u -2-> u2`. Exactly one of
`C_i,D_i` holds at each node: `C_i` when its label is `c_i`, and
`D_i` when its label is `d_i`. Other propositions are false and other
actions have no edges. These conventions are part of the restricted
model class, not formulas that must be tested by the automaton.

On `t`, define a game in which the universal player `C` chooses a
direction at a `c_i` node and the existential player `D` chooses at a
`d_i` node. All plays are infinite. Player `D` wins exactly when the
least label index recurring infinitely often is even. Let

\[
 \mathsf W_n=\{t\in\mathcal T_n:D\text{ has a winning strategy on }t\}.
\]

Let `sigma_i=mu` for odd `i` and `sigma_i=nu` for even `i`, and put

\[
 W_n=\mu X_1.\nu X_2.\cdots\sigma_n X_n.
 \bigvee_{i=1}^{n}
 \left[
   \bigl(C_i\land([1]X_i\land[2]X_i)\bigr)
       \lor
   \bigl(D_i\land(\langle1\rangle X_i\lor\langle2\rangle X_i)\bigr)
 \right].                                                       \tag{1}
\]

This is a closed, guarded simple `Sigma_n` formula, hence a
`Sigma^N_n` formula. Its body is fixed-point-free and its prefix
contains exactly the indicated alternating sequence, starting with
mu outside. We claim

\[
 K_t,\epsilon\models W_n\quad\Longleftrightarrow\quad t\in\mathsf W_n.
                                                               \tag{2}
\]

### Proof of the witness interpretation

At a model node, exactly one guard `C_i` or `D_i` is true. A winning
existential formula-game strategy must choose that guarded disjunct:
any other choice lets the universal player challenge its false guard.
At the true `C_i` branch, the universal player may either end at the
true guard or choose one of the two boxes. Each direction has a
unique successor. At the true `D_i` branch, the existential player
chooses one of the two diamonds, again with a unique successor.

After this model move, the formula game reaches `X_i`, returns to
its binder, traverses the remaining binder prefix, and evaluates the
body at the new model node. Thus a continuing play has exactly one
bound-variable return for each model move. Its variable index is
the preceding model node's label index. All intervening binder and
Boolean moves are finite.

Assigning priority `i` to `X_i` is a valid parity presentation of
this formula game: outer variables have lower indices and mu/nu
have respectively odd/even indices. The manuscript's spaced
binder-depth priorities give the same order and parities. Larger
default priorities at other nonterminals do not affect infinite
acceptance. Therefore the recurring variable indices and recurring
tree-label indices have the same minimum and parity.

A winning tree-game strategy gives a formula-game strategy by choosing
the true guard and copying its directional choices at `D` nodes.
Every finite guard challenge is true and every infinite continuing
play has the corresponding winning tree parity. Conversely, simulate
a winning formula-game strategy while never taking the optional true
guard terminals. At `C` nodes simulate the actual universal direction;
at `D` nodes use the formula strategy's direction. Every infinite tree
play thus expands to one compatible winning formula play. These are
history-by-history translations of single strategies, not a union of
independently chosen strategies. The evaluation-game theorem proves
(2). QED.

## 2. The automaton representation assumed by the index bridge

Let `A` have finite nonempty controls `Q`, initial control `q_*`,
rank map `r:Q->{1,...,n}`, and a transition `delta(q,a)` for every
`q in Q,a in A_n`. Each transition is a finite binary expression
tree whose internal nodes are conjunctions or disjunctions and
whose leaves are pairs `(q',i)` with `i in {1,2}`. There are no
constant terminals and no empty Boolean operations.

In its acceptance game, at control `(u,q)` enter `delta(q,t(u))`.
The existential player chooses at disjunctions and the universal
player at conjunctions. Reaching `(q',i)` makes the forced move to
`(ui,q')`. A play consists of infinitely many such finite transition
blocks, and accepts when the least infinitely recurring control rank
is even. Write `L(A,q)` for its accepted tree language from `q`.

Repeated leaf labels and repeated subexpressions are retained as
distinct occurrences. If a representation shares a finite Boolean
DAG, unfold it to a finite expression tree first. No bound on this
finite expansion is claimed here.

For `n >= 2`, terminal-free normalization is compatible with the
rank range: constant acceptance and rejection can be represented
by sinks of ranks 2 and 1 respectively. At rank one this argument
is unavailable; this is precisely why Section 7 below supplies a
separate formula-level base case.

## 3. Padding and the productive game-tree transformation

Replace every transition by

\[
 \Delta(q,a)=\delta(q,a)\lor\delta(q,a),                         \tag{3}
\]

with two distinct copies. This leaves `L(A,q)` unchanged: an
existential player chooses one of two identical games. From an
original strategy, choose the first copy at each added disjunction
and otherwise copy its choices. In the reverse direction maintain
one virtual padded history: let the padded strategy choose its copy
there and then follow that copy while making the corresponding
original choices. The virtual history is determined recursively by
the actual history and those internal choices, so this gives one
coherent original strategy, possibly using history. Control
transitions and their ranks are unchanged.

For each `q`, construct

\[
 G_q:\mathcal T_n\longrightarrow\mathcal T_n
\]

recursively as follows. If `t=a(t_1,t_2)`, take the finite tree
`Delta(q,a)` and replace

- each conjunction by the label `c_(r(q))`;
- each disjunction by the label `d_(r(q))`;
- each leaf `(q',i)` by the whole tree `G_(q')(t_i)`.

This is a well-defined productive construction. To determine a label
at an output address of length `k`, traverse the corresponding
finite transition tree. When a leaf is reached, pass to the indicated
input subtree and next control. Every new transition tree has the
added internal root from (3). Hence another recursive invocation
requires passing at least one further output edge. Determining a
finite output address makes only finitely many recursive invocations
and consults only a finite input prefix. Every output node is binary
and receives a label in `A_n`, so the output is a full tree.

In particular its root is always

\[
 G_q(t)(\epsilon)=d_{r(q)},                                    \tag{4}
\]

independently of the input root letter. This independence, not
merely existence of a modal move, produces strict contraction.

## 4. Strategy and parity-block equivalence

For every `q` and `t`,

\[
 t\in L(A,q)\quad\Longleftrightarrow\quad G_q(t)\in\mathsf W_n.
                                                               \tag{5}
\]

To prove this, first use the padded automaton from (3). An internal
node of each output transition block has exactly the owner of the
corresponding Boolean node. Selecting its first or second child
selects the corresponding expression child. At a leaf `(q',i)`,
the next output block is exactly the continuation at input subtree
`t_i` and control `q'`. The leaf/control transfer itself is forced
and introduces no additional choice in the output game.

Every infinite output path crosses infinitely many blocks: one
block is a finite acyclic expression tree. It determines the same
sequence `q_0,q_1,...` of automaton controls as an infinite expanded
automaton play. Conversely, every expanded play determines such
an output path. Finite play histories correspond in the same manner
up to the forced leaf/control steps. This includes histories that
reach the same printed expression through different occurrences.

The output labels within block `j` all have rank `r(q_j)`, repeated
a finite positive number of times. The number is positive because
of padding. Therefore a rank occurs infinitely often in the output
path iff it occurs for infinitely many of the controls `q_j`.
Indeed, finitely many finite blocks cannot supply infinitely many
occurrences, whereas infinitely many positive blocks do. The least
recurring rank and its parity are preserved.

Transfer a strategy at each finite history through this correspondence.
All opponent choices are retained, and every resulting infinite play
has the same winner. Hence winning strategies exist on exactly the
same side, proving (5). The padding equivalence gives (5) for the
original automaton too. No independent-strategy splicing or automaton
complementation result is used. QED.

## 5. One-level prefix gain and the unique fixed tree

Write `t =_k u` when `t` and `u` agree at every address of length
strictly less than `k`. Thus `=_0` is the universal relation and
`=_1` means root agreement. We prove simultaneously for all controls
that

\[
 t=_k u\quad\Longrightarrow\quad G_q(t)=_{k+1}G_q(u).
                                                               \tag{6}
\]

For `k=0`, (4) proves the claim. Suppose (6) holds for `k`, and
`t =_(k+1) u`. Their root letters agree, so the same finite padded
transition template is used. Their corresponding input subtrees
agree through depth `k`. At each recursive leaf `(q',i)`, the
induction hypothesis gives agreement of the attached output trees
through depth `k+1`. Every such attachment lies at output depth at
least one. Consequently all output labels at depths below `k+2`
agree, whether they lie in the common finite template or an attached
tree. This proves (6).

Equivalently, for the prefix distance `d(t,u)=2^(-m)` at the first
differing depth `m`, with `d(t,t)=0`,

\[
 d(G_q(t),G_q(u))\leq\tfrac12d(t,u).                           \tag{7}
\]

Fix `q=q_*`, choose any initial tree `t_0`, and define
`t_(j+1)=G_q(t_j)`. From (6), induction gives

\[
 t_{j+1}=_j t_j\qquad(j\geq0).
\]

For an address `v` of depth `h`, its label is therefore constant
from `t_(h+1)` onward. Let `t_*(v)` be that stable label. This
defines a member of `T_n`, and `t_j =_j t_*` for every `j`.
Applying (6) gives

\[
 G_q(t_j)=_{j+1}G_q(t_*),\qquad
 G_q(t_j)=t_{j+1}=_{j+1}t_*.
\]

Thus `G_q(t_*)` and `t_*` agree at every finite depth and are equal.
If two trees were fixed by `G_q`, their vacuous `=_0` agreement
would improve by (6) to `=_k` agreement for every `k`; hence they
would be identical. The fixed tree exists and is unique. No
completeness/compactness or Banach theorem has been assumed; the
stabilized-prefix argument supplies the required fact directly.

## 6. The diagonal contradiction for n >= 2

Suppose a closed `Pi^N_n` formula `B` were equivalent to (1) on all
the canonical trees in `T_n`. Any equivalence over all pointed models
would in particular have this property. Its positive syntactic dual `B^dual` belongs to
`Sigma^N_n` and denotes its complement. This class-duality fact
follows by induction on the class-generation rules; De Morgan
duality exchanges mu/nu and preserves the no-capture side condition.

On the canonical one-hot trees, `B^dual` therefore defines
`T_n \ W_n`. By the explicit index bridge `B_n`, take a terminal-
free automaton `A` of ranks `{1,...,n}` with that language. Apply
Sections 3--5 to its initial control. At the fixed tree `t_*`,

\[
\begin{aligned}
 t_*\notin\mathsf W_n
 &\Longleftrightarrow t_*\in L(A,q_*)\\
 &\Longleftrightarrow G_{q_*}(t_*)\in\mathsf W_n\\
 &\Longleftrightarrow t_*\in\mathsf W_n,
\end{aligned}
\]

a contradiction. Therefore (1) is not equivalent to any `Pi^N_n`
formula.

If an opponent mentions additional proposition letters or action
labels, interpret those as false propositions and empty relations
on the canonical tree class. Equivalently, before applying the
bridge, replace additional literals by their constants and modalities
for empty relations by `top` for boxes and `bottom` for diamonds.
This restriction preserves each Niwinski class: induct on its
generation, observing that the restriction commutes with binders
and capture-avoiding substitution and replaces removed subformulas
by level-zero constants. Thus extra vocabulary does not evade the
argument.

This proves every level `n >= 2` conditional on the separately
specified exact index bridge. It does not identify the required
bridge with a general automaton translation that increases ranks.

## 7. Independent first-level separation

Let `T_P={0,1}^U` be the space of full binary trees, with `P` true
exactly at nodes labelled `1`. A basic prefix cylinder specifies
finitely many initial levels. These cylinders define the prefix
topology; root proposition tests are clopen.

For `i in {1,2}`, the subtree map

\[
 s_i:T_P\longrightarrow T_P,\qquad s_i(t)=t_i
\]

is continuous: specifying finitely many levels of `t_i` specifies
only finitely many nodes of `t`. Give `T_P` itself the canonical
Kripke structure with the unique directional successors `s_1,s_2`
and root-label proposition valuation. The map from node `u` of
`K_t` to subtree `t_u` preserves proposition truth and both
directional successors, including the backward successor condition.
Hence, by the established bisimulation invariance (or by induction
on all fixed-point approximants), evaluating a closed formula at
tree `t` in this global structure agrees with evaluating it at the
root of `K_t`.

### Nu-only formulas define closed tree languages

More generally, give every free fixed-point variable a closed subset
of `T_P`. Structural induction shows that every positive nu-only
formula has a closed denotation in the global tree structure:

- constants and proposition literals denote clopen sets; free
  parameters are closed by assumption;
- finite conjunction and disjunction preserve closedness;
- each directional box and diamond is inverse image under the
  corresponding continuous subtree map, and preserves closedness;
- at `nu X.psi`, start the descending approximants from all of
  `T_P`; successor stages are closed by the induction hypothesis
  with closed parameters, and limit stages are arbitrary
  intersections of closed sets. Their eventual fixed point is
  therefore closed.

The argument permits nested nu-binders and arbitrary transfinite
approximation lengths. It does not assume finite convergence or
continuity of the fixed-point operator. Extra propositions fixed
false and extra actions fixed empty give clopen/constant operations
and do not change the conclusion.

Every `Pi^N_1` formula is nu-only. Indeed, level zero has no binders,
the level-one `Pi` binder rule adds only nu, and substituting a
nu-only formula into another introduces no mu. Induction on the
Niwinski class generation proves the assertion. Consequently every
closed `Pi^N_1` formula defines a closed language on `T_P`.

### A Sigma_1 language which is not closed

Put

\[
 F=\mu X.(P\lor\langle1\rangle X\lor\langle2\rangle X).
                                                               \tag{8}
\]

This is a closed simple `Sigma_1` formula. Its least-fixed-point
semantics is precisely finite reachability of a `P` node: induction
on path length puts every such node in the least pre-fixed set,
while the set of states with a finite path to `P` is itself fixed.
Therefore its root language consists of trees having at least one
node labelled `1`.

For each `k`, let `t^(k)` have its only `1` at address `1^k` and
zeros elsewhere. Each satisfies (8), but these trees converge in
the prefix topology to the all-zero tree `t^infty`, which does not.
Equivalently, every prefix neighborhood of the all-zero tree contains
some `t^(k)`, so that tree lies in the closure of the language.
The language is not closed and cannot equal the language of a
`Pi^N_1` formula. This establishes the missing first level without
using a rank-one automaton bridge.

## 8. Consequence over finite models

For each `n >= 1`, take the witness from (1) when `n >= 2` and from
(8) when `n=1`. For any proposed opposite-class formula `B`, the
arguments above produce inequivalence on some full binary tree.
Thus the modal formula

\[
 (W\land\neg B)\lor(\neg W\land B)
\]

is satisfiable. By the already established full finite-model
property, it has a finite pointed model. That finite model separates
`W` from this particular `B`.

The quantifier order is

\[
 \forall B\in\Pi^N_n\ \exists\text{ finite }(M_B,s_B)
             \quad M_B,s_B\models W\mathbin{\triangle}B.
\]

There is no assertion of one common finite separating model, a
uniform bound independent of `B`, or preservation of the canonical
full-binary-tree representation in the finite witness. This transfer
is over the class of all finite transition models and makes no new
automaton-index or complexity claim.

## Handoff boundary

Only this proof note was created. No manuscript, other note, code,
tests, builds, renders or additional agents were changed or created.
The direct diagonal and first-level proof are supplied in full;
the exact `Sigma^N_n`-to-rank-n bridge for `n >= 2` remains the
explicit separately assigned dependency of the final Niwinski
strictness conclusion.
