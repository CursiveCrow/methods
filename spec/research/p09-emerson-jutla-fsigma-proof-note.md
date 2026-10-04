# Emerson-Jutla Section 5: full fixed-point proofs for the on-line games

Date: 2026-09-06.

## Result and primary-source scope

The two Section 5 schemata have complete game-theoretic proofs using
constrained reachability, safety with an exit, outer entry ordinals, and
countable scheduling. For closed winning sets, prefix closure makes a
violated component permanently unavailable. For natural colors, increasing
the next target beyond the maximum already observed makes every phase
take a real round and produces unbounded colors.

Primary source: E. A. Emerson and C. S. Jutla, *Tree Automata,
Mu-Calculus and Determinacy (Extended Abstract)*, FOCS 1991, Section 5,
Theorems 5.1-5.2. The [complete Cornell copy](https://www.cs.cornell.edu/courses/cs6860/2021sp/Handouts/EmersonJutla91.pdf)
has this entire section on physical PDF page 9; the game convention at
the beginning of Section 4.1 is on PDF page 8. The local primary body is
`tmp/pdfs/p09-emerson-jutla-1991/emerson-jutla-1991.pdf`.
This pass read those existing page images and the primary text. No new
render was made.

The source's exact Section 5 hypotheses are:

- An infinite game tree with Player I choosing at OR nodes and Player II
  choosing at AND nodes. Its first application assigns a natural-number
  color to each OR node and explicitly writes the play as an OR-node
  sequence `x0,x1,... in OR^omega`.
- Player I wins that color play iff `exists i forall k c(xk)<i`.
  Thus the bound may depend on the resulting play; the source does not
  demand a single bound valid on every branch of a winning strategy.
- In the second application the winning set is `A=union_{i in omega} F_i`,
  with each `F_i` closed in the product topology of `X^omega`. It represents
  `F_i` as the infinite branches of a tree `T_i` on `X`. The predicate
  `T_i` at the last node of a finite game play means that the entire
  prefix belongs to that tree.

The source's Section 4.1 additionally makes each OR color equal to the
colors of its immediate AND successors. This identifies colors on the
full alternating play with those on its OR-round sequence. Section 5
already states its bounded-color condition on OR nodes, so its proof
does not require colors on AND nodes. The pairing convention is needed
only if one also states the objective on the full vertex sequence.

The detailed arguments below are supplied proofs. No finite-formula
syntax, algorithmic decision bound, finite-memory bound, or positional
strategy theorem for these infinitary objectives is asserted.

## 1. Arena, rounds, and set semantics

Work in the ordinary set-theoretic background with choice. Fix a
set-sized total bipartite game tree, rooted at an OR node, with

\[
V=O\mathbin{\dot\cup}D,
\qquad E\subseteq(O\times D)\cup(D\times O).
\]

Every vertex has at least one successor. Player I chooses at `O`, and
Player II chooses at `D`. A play is

\[
o_0,d_0,o_1,d_1,\ldots.
\]

One round consists of I choosing `d_k` and II choosing `o_{k+1}`.
The second player observes the first choice before responding.
Targets, safety predicates, and all fixed-point variables below are
subsets of `O`, tested at round boundaries, including the initial node.
The tree's nodes retain their entire preceding play histories.

For `X subseteq O`, define

\[
\begin{aligned}
P_I(X)&=\{o:\exists d\ (E(o,d)\land
                         \forall o'\,(E(d,o')\Rightarrow o'\in X))\},\\
P_{II}(X)&=\{o:\forall d\ (E(o,d)\Rightarrow
                         \exists o'\,(E(d,o')\land o'\in X))\}.
\end{aligned}
\]

These are `EX AX` and `AX EX` evaluated at OR nodes. Both are monotone.
Writing `bar B=O\B`, elementary quantifier duality gives

\[
\overline{P_I(\bar X)}=P_{II}(X).
\tag{1}
\]

For a monotone powerset map `H`, use the usual least and greatest
fixed points. Its least approximants are

\[
H^0=\varnothing,\quad H^{\alpha+1}=H(H^\alpha),\quad
H^\lambda=\bigcup_{\alpha<\lambda}H^\alpha
\quad(\lambda\text{ a limit}).
\]

They stabilize on a set-sized powerset lattice. Every member of `mu H`
therefore has a least entry stage, which is a successor ordinal. No
omega-continuity or finite-branching assumption is made.

The notations `exists i` and `forall i` in the source schemata mean
countable unions and intersections of denotations:

\[
\llbracket\exists i\,B_i\rrbracket
=\bigcup_{i\in\mathbb N}\llbracket B_i\rrbracket,
\qquad
\llbracket\forall i\,B_i\rrbracket
=\bigcap_{i\in\mathbb N}\llbracket B_i\rrbracket.
\]

They are infinitary set expressions indexed by natural numbers. They
are not first-order quantifiers added to the finitary modal language.
All unions, intersections, and fixed points are taken on the common
domain `O`.

## 2. Constrained reachability lemma

For arbitrary `B,C subseteq O`, put

\[
R_{II}(B,C)=\mu X\bigl(C\cap(B\cup P_{II}(X))\bigr).
\tag{2}
\]

This is exactly the region from which Player II can force a finite
round-boundary visit to `B`, while every boundary up to and including
that first visit belongs to `C`. If the initial node lies in `B cap C`,
the visit occurs at time zero. After the target is reached this local
objective imposes no further condition.

### Rank strategy from the fixed point

Let `R_alpha` be the least approximants of the operator in (2), and
assign each `o in R=R_II(B,C)` its entry rank

\[
\rho(o)=\min\{\alpha+1:o\in R_{\alpha+1}\}.
\]

If `o in R` already lies in `B`, the local objective has been achieved.
Otherwise, writing `rho(o)=alpha+1`, the approximant equation gives

\[
o\in C\cap P_{II}(R_\alpha).
\]

After every move `o -> d` by I, choose a successor `o' in R_alpha`.
This is possible by the definition of `P_II`. Its entry rank satisfies
`rho(o') <= alpha < rho(o)`, and `o' in C`.
Thus every round before the target strictly decreases an ordinal.
There cannot be infinitely many such rounds. A target is reached after
finitely many rounds, with all boundaries including the target in `C`.
Fixing these witness choices supplies a single strategy against all
opponent plays. The number of rounds need not have a uniform finite
bound over those plays.

### Converse without assuming determinacy

If `o` is outside `R` and outside `C`, the constrained objective already
fails at its initial boundary. If `o in C\R`, then `o notin B`, since
`B cap C subseteq R`. The fixed-point equation also gives
`o notin P_II(R)`. By (1), I has a move `o -> d` all of whose OR
successors remain outside `R`.

Repeat that choice whenever the current boundary is in `C\R`.
Either the play eventually leaves `C` before reaching a permitted
target, or it stays in `C\R` forever and never reaches `B`.
Both alternatives defeat the constrained objective. This explicit
opponent strategy proves the converse of the lemma.

## 3. Safety-or-exit lemma

For arbitrary `T,B subseteq O`, put

\[
S_I(T,B)=\nu X\bigl((T\cap P_I(X))\cup B\bigr).
\tag{3}
\]

This is exactly the region where Player I can ensure one of the
following outcomes: a finite visit to `B` with every earlier boundary
in `T`, or an infinite play whose every boundary stays in `T`.
The initial node is included: a node in `B` satisfies the exit
alternative immediately, with no requirement that it lie in `T`.

Let `S=S_I(T,B)`. Its fixed-point equation says that an `o in S\B`
lies in `T cap P_I(S)`. Choose a first-round move all of whose OR
successors remain in `S`. Continue until `B` is reached. Before that
event every boundary lies in `T`; if it never happens, safety holds
forever. This proves the forward implication.

For the converse, fixed-point complementation and (1) give

\[
\overline{S_I(T,B)}
=\mu X\bigl(\bar B\cap(\bar T\cup P_{II}(X))\bigr)
=R_{II}(\bar T,\bar B).
\tag{4}
\]

The constrained reachability lemma supplies a II strategy forcing a
visit outside `T` while every boundary through that visit is outside
`B`. That defeats both the safe-exit and infinite-safety alternatives.
This proves exactness of (3) without a separate determinacy theorem.

Both lemmas apply to arbitrary set-sized total bipartite arenas. Their
use below on a game tree allows the predicates `T_i` to depend on the
entire finite history, as the source requires.

## 4. The nested operators are complements

For a sequence `T_i subseteq O`, define the monotone maps

\[
\begin{aligned}
\mathcal F(Y)
&=\bigcup_{i\in\mathbb N}
        \nu X\bigl((T_i\cap P_I(X))\cup Y\bigr),\\
\mathcal G(Z)
&=\bigcap_{i\in\mathbb N}
        \mu X\bigl((\bar T_i\cup P_{II}(X))\cap Z\bigr).
\end{aligned}
\]

Monotonicity of each inner fixed point in its external parameter makes
both outer maps monotone. By (4) and De Morgan's law for the countable
union,

\[
\overline{\mathcal F(\bar Z)}=\mathcal G(Z).
\]

Consequently, for

\[
I^*=\mu Y\,\mathcal F(Y),\qquad
J^*=\nu Z\,\mathcal G(Z),
\tag{5}
\]

fixed-point complementation proves

\[
J^*=O\setminus I^*.
\tag{6}
\]

This algebraic identity uses no prefix-closure condition on `T_i`.
The interpretation of these complementary regions as the particular
winning sets is proved by the separate strategies below.

## 5. Player I's outer-rank strategy

Let `A_alpha` be the least approximants of `mathcal F`. Each `o in I*`
has outer entry rank

\[
r(o)=\min\{\alpha+1:o\in A_{\alpha+1}\}.
\]

At a phase start `o`, write `r(o)=alpha+1`. Since
`A_{alpha+1}=mathcal F(A_alpha)`, choose an index `i` with

\[
o\in S_I(T_i,A_\alpha).
\tag{7}
\]

The minimality of the entry stage gives `o notin A_alpha`, so the
phase does not begin with an already-satisfied exit. Retain this `i`
and `alpha` and follow the safety-or-exit strategy of Section 3.

If the phase never reaches `A_alpha`, all its subsequent boundaries
remain in `T_i` forever. If it reaches a boundary `o' in A_alpha`,
start a new phase there. Its outer entry rank satisfies

\[
r(o')\leq\alpha<\alpha+1=r(o).
\tag{8}
\]

No infinite sequence of phase restarts is possible, because it would
strictly decrease ordinals. Each phase which ends does so after a
finite positive number of rounds. Therefore every compatible infinite
play eventually enters one last phase and remains in one of the sets
`T_i` forever.

This yields, for arbitrary `T_i`, the conclusion

\[
\forall\text{ compatible plays }\pi\quad
\exists i\ \exists N\ \forall k\geq N\quad o_k\in T_i.
\tag{9}
\]

The index, final phase, and time `N` may depend on the play. This is
exactly the quantifier order supplied by the strategy construction;
no uniform branch-independent index or restart bound is claimed.

## 6. Closed sets and round-boundary prefix predicates

Let `mathcal P` be the legal infinite plays from the root, with the
prefix/product topology. One can code the successive moves in a
discrete set `X`, giving the source's `X^omega` presentation. Let
`F_i subseteq mathcal P` be closed, and define its prefix tree

\[
\widehat T_i
=\{s:s\text{ is a finite legal play prefix extendible to a play in }F_i\}.
\]

This set is prefix closed. A legal infinite play belongs to `F_i` iff
all its finite prefixes belong to `widehat T_i`. One direction follows
from the definition. For the other, if the play is outside the closed
set, its open complement contains a cylinder determined by some finite
prefix. That prefix has no extension in `F_i`, a contradiction.

For `o in O`, let `hist(o)` be the complete root-to-`o` play prefix,
and set

\[
T_i=\{o\in O:\operatorname{hist}(o)\in\widehat T_i\}.
\tag{10}
\]

These are precisely the source's prefix-dependent node predicates,
restricted to the OR-boundary domain of the schemata. The OR prefixes
are cofinal in the finite prefixes of any infinite play. Therefore
membership of all OR prefixes in `T_i` is equivalent to membership of
every prefix in `widehat T_i`, including those ending at AND nodes.
If an AND prefix already leaves `widehat T_i`, every subsequent OR
prefix is also outside it. No violation is lost by waiting for the
next boundary.

Prefix closure gives two useful properties:

1. If a boundary is outside `T_i`, every later boundary on that play
   is outside `T_i`. A violation is permanent.
2. If eventually every boundary lies in `T_i`, then every earlier
   prefix also belongs to `widehat T_i`: extend that earlier prefix
   to a later boundary in the final tail and apply prefix closure.
   Thus eventual membership in `T_i` already implies the complete
   play belongs to `F_i`.

From a nonroot node, the objectives retain the original root prefix
through (10). Replacing `T_i` by a freshly restarted subtree predicate
without that prefix would change the objective.

### Player I wins the countable union from I*

Apply the strategy of Section 5 to the predicates (10). Every compatible
play eventually stays in one `T_i`. Property 2 then puts the complete
play in `F_i`, hence in `A=union_i F_i`. This proves

\[
I^*\subseteq\operatorname{Win}_I(A).
\tag{11}
\]

## 7. Player II excludes every closed component from J*

The greatest-fixed-point equation `J*=mathcal G(J*)` gives, for every
index `i`,

\[
J^*\subseteq
\mu X\bigl(J^*\cap(\bar T_i\cup P_{II}(X))\bigr)
=R_{II}(\bar T_i,J^*).
\tag{12}
\]

At a current boundary `o in J*`, let

\[
D(o)=\{i:\operatorname{hist}(o)\notin\widehat T_i\}
=\{i:o\notin T_i\}.
\]

These are exactly the components already violated, including any
violation at an earlier AND prefix. By permanence, `D(o)` can only
grow on a continuing play.

If `D(o)=mathbb N`, the current prefix is incompatible with every
`F_i`; every continuation is already outside `A`. Choose any legal
continuation. No further obligation to stay in `J*` is needed in
this completed case.

Otherwise choose the least index `i` outside `D(o)`. By (12) and the
constrained reachability lemma, II can force a finite visit to
`bar T_i` while staying in `J*` through the target. Since the phase
starts in `T_i`, this visit cannot occur at time zero. The phase
therefore contains at least one real round. At its final boundary,
the chosen `i` and every previously violated index remain in `D`.
Repeat this construction there.

On every compatible play, each phase which starts finishes in finite
time. Either all indices are violated after finitely many phases, or
the least unviolated indices of successive phases strictly increase.
For every fixed `k`, after at most `k+1` phases all indices through
`k` are violated; any phase that skips some of them does so because
they have already been violated. Thus every `F_i` eventually receives
a finite incompatible prefix. The play belongs to none of them and
is outside their union. This proves

\[
J^*\subseteq\operatorname{Win}_{II}(\mathcal P\setminus A).
\tag{13}
\]

This schedule avoids infinitely many bookkeeping changes at a single
boundary. An index whose target already holds is not selected, and
if all targets hold the winning objective is already secured.

### Exact winning regions and determinacy

By (6), every starting boundary lies in exactly one of `I*` and `J*`.
The strategies in (11) and (13) win complementary objectives. A node
cannot admit winning strategies for both players: following those two
strategies against each other gives one legal infinite play, which
cannot lie both inside and outside `A`. Hence

\[
I^*=\operatorname{Win}_I(A),\qquad
J^*=\operatorname{Win}_{II}(\mathcal P\setminus A).
\tag{14}
\]

Equations (5) and (14) are the full asserted characterizations in
Theorem 5.2, with explicit round-boundary semantics. The proof derives
determinacy; it does not use a separate Borel determinacy theorem.

## 8. Natural colors and Theorem 5.1

Let `c:O -> mathbb N` assign exactly one natural color at each boundary.
For `i in mathbb N`, set

\[
T_i=\{o:c(o)<i\},\qquad \bar T_i=\{o:c(o)\geq i\}.
\tag{15}
\]

The source's abbreviated color disjunctions have exactly these
denotations. Use (5) with the predicates (15), retaining the algebraic
complement identity (6). These `T_i` need not be prefix closed;
therefore the permanent-violation proof of Section 7 is not applied
to them.

### Bounded colors from I*

Section 5 proves that every compatible play eventually has all its
colors below some `i`. A finite prefix has only finitely many natural
colors. If `N` starts the final tail, take

\[
b=\max\bigl(\{i\}\cup\{c(o_k)+1:k<N\}\bigr).
\]

Then `c(o_k)<b` for every `k`, including both prefix and tail. Thus I
wins the source objective `exists b forall k c(o_k)<b` from every
node in `I*`. When starting below the root, including the finitely
many earlier colors only changes this finite maximum.

### Unbounded colors from J*

For every finite bound `i`, equation (12) now supplies constrained
reachability of `{c>=i}` while staying in `J*`. At a phase boundary
take `M` to be the maximum natural color observed so far on the finite
play, including the current node, and choose the next target

\[
i=M+1.
\]

The present boundary does not meet this target. The reachability
strategy therefore takes a finite positive number of rounds and ends
at a boundary whose color is at least `M+1`, still in `J*`.
The maximum observed color has strictly increased. Start the next
phase there with a new bound above that maximum.

Every phase finishes and takes at least one real round. The strategy
therefore produces infinitely many phases along every compatible
infinite play, with strictly increasing observed maxima. Its color
sequence is unbounded. This is the complement of the bounded-color
objective. With (6) and the incompatibility of opposing winning
strategies, the two fixed points in Theorem 5.1 are exactly the two
winning regions.

The increasing-threshold schedule retains the historical maximum;
it does not pretend that leaving the present-state set `{c<i}` is
permanent. Subsequent colors may fall below earlier thresholds.

## 9. Hypotheses and proof boundaries to retain on incorporation

- Use a total bipartite game and the two-move round predecessors.
  Predicates and fixed-point variables range over OR boundaries.
- In the closed-set theorem, `T_i` depends on the entire original
  finite play prefix. Prefix closure justifies both the final-tail
  argument for I and permanent violations for II.
- Interpret the source's index quantifiers as countable union and
  intersection on one powerset lattice; retain transfinite entry
  ranks when the game has infinite branching.
- State that a forced reachability phase takes finitely many rounds
  on each play, without asserting one finite bound for all plays.
- For the closed-set schedule, choose an unviolated index, or declare
  the objective secured if none exists. This prevents empty phases.
- For the natural-color schedule, choose a bound strictly above the
  finite historical maximum. Its positive phase length makes the
  infinite schedule an actual infinite play.
- The source's color objective is on OR-node sequences. If it is
  stated on all vertices, keep the inherited paired-color convention.
- These are explicit strategies with phase information. Do not infer
  finite syntax, a decision procedure, or history-free strategies on
  a folded arena from these infinitary schemata.

Only this research note was authored. No manuscript edits, software
tests, builds, new renders, commits, or pushes were performed.
