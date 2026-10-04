# Emerson-Jutla formula automata: source conventions and a supplied proof route

Date: 2026-09-06.

## Outcome and scope

The existing guarded modal-parity-automaton construction can be converted
into the finite `OR/DAND/AAND` format of Emerson-Jutla Theorem 3.1.
Directional one-step Boolean normalization, two sinks, and the elementary
least-parity-to-Streett conversion supply a complete existence proof route.
Positional parity determinacy supplies precisely Definition 2.7's
history-free conclusion. This is a supplied construction for the theorem's
conclusion; it does not claim to reconstruct every step of the source's
regeneration construction or its original control graph.

Two details must be explicit. The source theorem's alphabet is the set of
proposition symbols occurring in the input. Also, its printed legal
strategies are total on all alternating state/direction histories, so the
constructed automaton should have an enabled move for every state and
input symbol. A rejecting sink handles a false transition, while an
accepting sink handles a true transition or an unrequired direction.

This note owns no manuscript changes. It checks the source and develops the
construction to be incorporated separately.

## Primary body and locators

The primary source is E. A. Emerson and C. S. Jutla, *Tree Automata,
Mu-Calculus and Determinacy (Extended Abstract)*, FOCS 1991, 368-377.
The [complete Cornell course-hosted primary copy](https://www.cs.cornell.edu/courses/cs6860/2021sp/Handouts/EmersonJutla91.pdf)
is already held at
`tmp/pdfs/p09-emerson-jutla-1991/emerson-jutla-1991.pdf`.
This pass read its text and the already existing page images for PDF pages
3-7 and 10; no new render was performed. These are physical PDF-page
locators because this copy has no printed proceedings pagination.

| Physical PDF page | Primary material checked |
|---|---|
| 3 | Finite-state standing convention, Definitions 2.1-2.3, Streett/Pairs acceptance, start of Definition 2.4. |
| 4 | Full alternating tuple; Definitions 2.5-2.7; threads, ithreads, legal strategies and history-freedom. |
| 5 | Formula/sentence distinction; singleton-symbol tree semantics, Definitions 3.0-3.2. |
| 6 | Theorem 3.1, its exact alphabet, non-tripartite parse diagram, regeneration, enclosing-binder substitution and precedence. |
| 7 | Heights, GREEN/RED sets, history-free conclusion; subsequent largest-recurring parity convention. |
| 10 | The dissertation citation [J90]. |

The current reader-facing passage is in
`handbook/parts/p09/presentations/n-c-018.tex`, under
`sec:p09-presentation-n-c-018-emerson-jutla`, paragraph
"Pre-models, regeneration, and the formula automaton".
It currently supplies the source proof sketch rather than the complete
transition construction below. The source history record remains
`spec/research/p09-emerson-jutla-1991-source-note.md`.

## Exact source data

### Tuple and finiteness

Definition 2.4 uses

\[
\mathcal A=(\Sigma,OR,DAND,AAND,\psi,\delta,\chi,L,s_0,\Phi),
\]

with

\[
\begin{gathered}
\psi\subseteq OR\times DAND,\qquad
\delta:DAND\times\{0,1\}\longrightarrow AAND,\\
\chi\subseteq AAND\times OR,\qquad
L:DAND\longrightarrow\Sigma,\qquad s_0\in OR,\qquad
\Phi\subseteq OR^\omega.
\end{gathered}
\]

`OR` is explicitly finite. Section 2 opens with the standing restriction
to finite-state automata. `DAND` and `AAND` are described as transition
nodes, without a separate adjective "finite" on each defining line.
The supplied construction below makes all three sets and all transition
tables finite, so no broader interpretation of the source is needed.
The input is a full tree `t:{0,1}* -> Sigma`.

### Moves, total strategies, and infinite acceptance

At current tree node `u` and state `q`, Player I chooses `d` satisfying
`psi(q,d)` and `L(d)=t(u)`. Player II chooses `i in {0,1}` and then
`r` satisfying `chi(delta(d,i),r)`. The next state position is `(ui,r)`.
Thus Player II chooses both the input direction and the universal
successor inside that direction.

Definition 2.5 writes Player I's strategy on
`{s0} . ({0,1} . OR)*`, with input-label compatibility and `psi`-legality
quantified over all such histories. In particular, it does not restrict
the displayed legal-strategy conditions to histories reachable under the
chosen strategy. Definition 2.6 quantifies every infinite thread produced
along every infinite input branch. The condition applies to the infinite
`OR` sequence, not to the interposed administrative nodes.

The source supplies no separate terminal payoff rule for an absent
`psi`-successor or an empty `chi`-successor set. The existence construction
below avoids both cases for every nonempty input alphabet. This is a
chosen total construction, not an attribution of a missing terminal
convention to the paper.

Definition 2.7 requires a winning strategy depending only on `(u,q)`,
where `u` is the current input node and `q` the current `OR` state.
It may depend on the particular input tree. The theorem does not assert
that choices depend only on `q`, or only on the current input letter.
Nor does it demand the separate Section 4.4 condition phrased using
identical remaining partial game trees.

### Formula class and exact alphabet

Theorem 3.1 identifies `Prop` with the proposition symbols occurring in
`f0`, so it is finite. Its inputs have the type
`t:{0,1}* -> Prop`; at `u`, proposition `P` holds exactly when `t(u)=P`.
To use the later modal-automaton alphabet `2^Prop`, evaluate transitions
only at singleton letters `{t(u)}`. Do not replace this source model
class by arbitrary subsets at a node.

Although Theorem 3.1 says "formula", the immediately preceding semantics
is for sentences and gives no variable environment as part of the tree
input. The exact existence statement should therefore use a closed input.
An open-formula version would need an explicitly supplied environment
encoding or other added input data.

If `Prop` is empty, there is no function from the nonempty set `{0,1}*`
to `Prop`. The source's literal input class is then empty, and its
acceptance equivalence and history-free property are vacuous. One may
treat that case separately with an automaton over the empty alphabet.
Alternatively, a nonempty finite ambient alphabet containing the occurring
propositions gives a useful extended statement, but adding a dummy symbol
must be declared as that extension rather than silently changing the
source's exact alphabet.

### Source precedence, height, and Streett pairs

After distinct binder renaming, an enclosing fixed-point subexpression
has higher precedence than a proper contained fixed-point subexpression.
Write `Y < X` when `Y` has lower precedence than `X`, so innermost
binders are minimal. The source height is

\[
h(X)=1\quad\text{if there is no }Y<X,
\qquad
h(X)=1+\max_{Y<X}h(Y)\quad\text{otherwise}.
\]

It uses the binder-closing map `H`: replace the free enclosing fixed-point
variables of a binder expression by their already constructed closed
binder formulas. Higher precedence makes this recursive definition
well founded. The source ties regeneration of `H(X)` to rederivation
without intervening rederivation of a higher-precedence `H(Y)`.

For each height `i`, its printed sets are

\[
GREEN_i=\{X:h(X)=i,\ X\text{ is }\mu\text{-bound}\},
\qquad
RED_i=\{X:h(X)\geq i,\ X\text{ is }\nu\text{-bound}\},
\]

understood as the corresponding variable nodes in its transition
diagram. Acceptance requires `GF GREEN_i -> GF RED_i` for every `i`.
The weak inequality in `RED_i` is literal.

The source explicitly acknowledges that its first parse-tree transition
diagram need not be tripartite. Its argument for history freedom first
invokes the existence of a well-founded strategy and selection by least
regeneration ranks; preserving the transition graph then preserves the
history-free property of that selected strategy. Changing acceptance
alone is not a general proof that an automaton has history-free winning
strategies. The supplied proof below instead invokes the independently
proved positional parity theorem.

## Supplied construction and proof outline

### 1. Directional model and guarded parity automaton

Fix a closed `f0` and nonempty finite source alphabet
`Sigma=Prop(f0)`. Put `U={0,1}*` and

\[
R_i=\{(u,ui):u\in U\},\qquad
V(P)=\{u:t(u)=P\},\quad i\in\{0,1\}.
\]

Translate the source modalities by

\[
EX\alpha\mapsto\langle0\rangle\widehat\alpha
                    \lor\langle1\rangle\widehat\alpha,
\qquad
AX\alpha\mapsto[0]\widehat\alpha\land[1]\widehat\alpha.
\]

All other constructors commute with this translation. Structural
induction proves equal denotations, including fixed points because the
translated bodies define the same monotone operator on `P(U)` for every
bound-variable value.

Apply `sec:p09-mu-automaton-construction` to `widehat(f0)`. This gives
finite controls `Q`, start `qI`, priorities `Omega:Q -> N`, and depth-one
positive Boolean transition expressions `Delta(q,A)` whose atoms are
`<i>r` and `[i]r`. That already proved construction handles unguarded
input and infinite local binder activity; no raw parse-tree loop is
mistaken for an input-consuming transition. It accepts precisely the
directional tree models of `widehat(f0)`.

Use `Delta(q,{a})` for source symbol `a in Sigma`. Since `R_i` has exactly
one successor, replace both `<i>r` and `[i]r` by the common directional
atom `(i,r)`. This identification is justified on these functional total
relations; it is not an equation for general transition systems.

### 2. Finite DNF and exact directional transition tables

Let `E={0,1} x Q`. For the resulting positive Boolean expression
`B(q,a)` define the finite family

\[
\mathcal F(q,a)=\{S\subseteq E:B(q,a)[1_S]=1\}.
\]

Monotonicity gives the identity

\[
B(q,a)\equiv
\bigvee_{S\in\mathcal F(q,a)}\bigwedge_{e\in S}e.
\]

Indeed, the support of any satisfying valuation is one listed term;
conversely, a valuation containing a listed term satisfies `B(q,a)`.
Repeated atoms need only one entry. A true expression has the empty
term; a false expression has no term. This complete truth-table DNF is
effective and finite; no optimal bound is asserted.

Adjoin distinct states `T` and `F` to `Q` and set
`OR=Q union {T,F}`. For every `(q,a,S)` with
`S in F(q,a)`, create a distinct `DAND` node `d=(q,a,S)` and two distinct
`AAND` nodes `(d,0),(d,1)`. Set

\[
\psi(q,d),\quad L(d)=a,\quad\delta(d,i)=(d,i).
\]

Let `S_i={r:(i,r) in S}`. The `chi`-successors of `(d,i)` are `S_i`
if nonempty, and `{T}` otherwise. Therefore choosing an unrequired
direction commits the play to acceptance; it adds no obligation.
For an empty term both directions go to `T`.

If `F(q,a)` is empty, create one `DAND` node for `(q,a)` whose two
`AAND` nodes both have the sole successor `F`. This makes the false
case losing with all plays infinite, rather than relying on an
undefined missing-transition payoff.

For each letter `a`, give `T` one labelled `DAND` choice with both
directions returning to `T`, and give `F` the analogous self-returning
choice. All objects are finite. Every `(q,a)` has an enabled `DAND`,
and every `AAND` has at least one `OR` successor. Hence total legal
strategies exist even on off-play histories.

Keep the old priorities on `Q`; give `T` priority 0 and `F` priority 1.
Only their eventual constant tails matter once they are entered, so
these values do not constrain the existing finite priority range.

### 3. Why Boolean normalization preserves the infinite game

Inside one transition, the original positive Boolean expression is a
finite acyclic game with existential disjunctions, universal
conjunctions, and directional atoms as exits. For any set `W` of exits,
Player I can force termination at a true terminal or an exit in `W`
exactly when `B[1_W]=1`, by structural induction on `B`.

From an original winning strategy, take the set `S` of directional exits
reachable under its local choices at a particular transition history.
Every terminal reached is true, so the finite-game fact makes `S` a
listed DNF term. Choose its `DAND`. For a selected exit, retain one
realizing original local path as virtual history and continue its
strategy. If Player II chooses an unrequired direction, the play wins
through `T`. Every infinite play avoiding `T` has an original play
with the identical successive `Q` controls and therefore identical
parity outcome.

Conversely, for a chosen listed term `S`, the finite-game fact supplies
local Boolean choices leading only to true terminals or members of `S`.
At a directional exit `(i,r)`, simulate Player II's matching direction
and `AAND` successor choice in the DNF game, then continue the original
transition strategy with that virtual history. True terminals win
immediately in the original game. A globally winning DNF strategy
cannot choose a false-case transition on a compatible history, since
every continuation from it reaches `F` and loses. Infinite plays again
have the same control sequence after the bounded local expansions.
This establishes both winner-preserving strategy translations without
assuming history freedom in advance.

### 4. Streett acceptance is precisely least-recurring even parity

For every odd priority `j` occurring in `OR` define

\[
G_j=\{q:\Omega(q)=j\},\qquad
R_j=\{q:\Omega(q)\text{ is even and }\Omega(q)<j\}.
\]

An infinite `OR` sequence satisfies all clauses
`GF G_j -> GF R_j` iff its least infinitely recurring priority is even.
If that least priority is odd `j`, its request recurs but no smaller
even response recurs. If it is even `e`, every infinitely recurring
odd `j` is larger than `e`, and recurrence of the `e`-states fulfils
that request. A request occurring only finitely often is vacuous.
This proves exact equivalence on every infinite sequence, hence on
every ithread for every strategy. `T` wins and `F` loses as required.

These are the source's Streett orientation, not its complementary
Pairs condition. The construction uses the least-priority convention
of the supplied automaton. It need not call its controls original
syntax variables or its priorities source heights.

For comparison only, if binder height ranges up to `H`, assigning
`2(H-h(X))+1` to a least binder and `2(H-h(X))` to a greatest binder
makes a lower even response to the least binder at height `i`
equivalent to a greatest binder at height at least `i`. This algebra
explains the source's displayed weak height inequality. It does not
identify all auxiliary states of the supplied construction with
nodes of the source sketch.

### 5. History-free accepting strategies in the exact source sense

The total constructed game has positions `(u,q)` owned by Player I,
administrative positions for its chosen `d`, and Player-II directional
and successor choices. Give each administrative vertex an even priority
larger than every `OR` priority. Every infinite play visits an `OR`
position after at most three graph steps, so these added priorities
do not change the least recurring priority.

Apply `sec:p09-parity-positional-proof` to this set-sized total arena
with finite priority range. If the root is winning, Player I has a
positional winning choice at `(u,q)`, hence a `DAND` choice depending
only on the input node and current state. This is Definition 2.7.
Extend the choice to all other `(u,q)` by any enabled transition;
the transition totality proved above makes this a total legal strategy
on the source's full printed history domain. Its initial winning
behavior is unchanged. Per-sequence parity/Streett equivalence makes
the same strategy Streett-winning.

Combining the directional semantic induction, guarded automaton theorem,
DNF strategy translations and Streett conversion proves the required
acceptance equivalence on exactly the source's singly labelled full
binary trees. Applying positional determinacy proves the additional
history-free property for every accepted tree.

## Dissertation availability: bounded local check

The primary reference [J90], PDF page 10, identifies C. S. Jutla,
*Automata on Infinite Objects and Modal Logics of Programs*, PhD thesis,
The University of Texas at Austin, May 1990. It gives no URL.

The live `p09-emerson-jutla-1991-source-note.md` and the corresponding
lot-2/3 source record refer to this dissertation but supply no primary
body link. The repository's visible and ignored file-name inventory
for Jutla/dissertation candidates found the held Emerson-Jutla article
and its extracted text, not a separately named Jutla dissertation body.
No accessible primary dissertation body was identified in this bounded
check. This does not establish that none exists online or under an
unrelated local filename; no broad acquisition search was performed.

## Incorporation checklist specific to this argument

- State the closed input and the exact finite source alphabet; handle its
  empty case or explicitly state an ambient-alphabet extension.
- Restrict the later powerset-letter transition table to singleton letters.
- Use the existing guarded automaton theorem before DNF, including its
  treatment of infinite local activity for unguarded formulas.
- Define both sinks and the false-transition default, ensuring total
  legality and nonempty universal successor sets.
- Prove the finite Boolean-exit game lemma and both infinite strategy
  translations; one-step truth-table equality alone is not the whole
  infinite-game proof.
- State Streett requests at odd priorities and responses at smaller even
  priorities; the source's subsequent parity convention is reversed.
- Derive history freedom from positionality of the total constructed arena,
  then extend choices to the full source history domain.
- Attribute this route as a supplied existence proof. Keep source heights
  and regeneration as source data unless their separate construction is
  actually reconstructed.

No software tests, manuscript builds, new renders, commits or pushes were
performed. The only authored file in this pass is this note.

## Directional-language correction to the reverse equivalence

### Primary definitions contain no direction-specific formula operator

A further reading of Definitions 2.1, 2.4, 3.0 and 3.2, and the
equivalence paragraph at the start of Section 4, confirms an actual
language distinction. Definition 3.0 lists only `EX alpha` and `AX alpha`.
Definition 3.2 gives

\[
u\models EX\alpha\iff\exists i\in\{0,1\}\ ui\models\alpha,
\qquad
u\models AX\alpha\iff\forall i\in\{0,1\}\ ui\models\alpha.
\]

These are modalities for the single unindexed successor relation
`R={(u,u0),(u,u1):u in {0,1}*}`. Neither that definition nor the
remaining primary formula clauses introduce `EX_0`, `EX_1`, named
direction relations, or built-in proposition letters marking left and
right children. The proposition valuation is exactly the input symbol
test, so arbitrary direction tags cannot be assumed.

In contrast, Definition 2.1 explicitly makes
`delta:AND x {0,1} -> OR` specify left and right successors, and
Definition 2.4 retains this direction argument. Those automata can
distinguish two different orderings of the same unindexed tree.

### Concrete two-tree counterexample

Take the finite alphabet `Sigma={P,Q}`. Define two full singly labelled
binary trees by

\[
t_L(u)=\begin{cases}P,&u=0,\\Q,&u\ne0,\end{cases}
\qquad
t_R(u)=\begin{cases}P,&u=1,\\Q,&u\ne1.\end{cases}
\]

Thus both roots have label `Q`. Only the immediate left child is labelled
`P` in `t_L`, and only the immediate right child is labelled `P` in `t_R`.
All other nodes have label `Q`. Define the involution

\[
h(\epsilon)=\epsilon,\qquad h(0v)=1v,\qquad h(1v)=0v.
\]

It is a root-preserving bijection with
`t_R(h(u))=t_L(u)`. It preserves the unindexed successor relation in
both directions: at the root it exchanges the two outgoing edges,
and below the root it preserves the final direction digit. Consequently
it is an isomorphism of the pointed transition models used by the
source's `EX/AX` semantics.

For completeness, isomorphism invariance here also covers nested fixed
points. The powerset bijection `H(A)=h[A]` preserves unions,
intersections and complements and commutes with the existential and
universal `R`-predecessor operators. Structural induction with
environments related by `eta_R(X)=H(eta_L(X))` therefore relates the
body operators by conjugation. This complete-lattice isomorphism takes
their least and greatest fixed points to each other. Hence every closed
formula in the printed `EX/AX` language has the same truth value at the
two roots.

Now construct a deterministic binary-tree automaton with states
`s,c,T,F`, initial state `s`, and transition table

| State | Input symbol | State sent to direction 0 | State sent to direction 1 |
|---|---|---|---|
| `s` | either | `c` | `T` |
| `c` | `P` | `T` | `T` |
| `c` | `Q` | `F` | `F` |
| `T` | either | `T` | `T` |
| `F` | either | `F` | `F` |

Give `F` odd priority 1 and all other states even priority 0. For each
state/symbol row, one labelled `AND` node realizes the displayed pair
of successor states, so this is literally Definition 2.1's format.
It accepts exactly when the root's direction-0 child is labelled `P`:
otherwise every branch that first takes direction 0 eventually remains
in `F`. Therefore it accepts `t_L` and rejects `t_R`.

If the statement is required in the source's Pairs rather than parity
acceptance, use the single pair `(OR,{F})`. The complement of its
Streett implication is `GF OR and not GF {F}`, equivalently finitely
many visits to `F`; the automaton's absorbing `F` makes this exactly
the same acceptance condition. Thus the counterexample already lies
in the nondeterministic Pairs class mentioned in the source-equivalence
paragraph; no stronger automaton model is needed.

### Exact mathematical correction

Theorem 3.1's forward statement remains valid: a closed unindexed
`EX/AX` formula has an equivalent ordered binary-tree automaton.
The construction above in this note proves that inclusion, with an
automaton whose accepted language retains the formula's invariance.

The unrestricted reverse statement is false for the printed unindexed
language on the same input alphabet and the same pointed trees. It must
use the modal fixed-point language with separate successor relations
`R_0` and `R_1`, that is, modalities `<0>`, `[0]`, `<1>` and `[1]`.
The counterexample property then has the formula `<0>P`.
The original operators embed by

\[
EX\alpha\equiv\langle0\rangle\alpha\lor\langle1\rangle\alpha,
\qquad
AX\alpha\equiv[0]\alpha\land[1]\alpha.
\]

The later manuscript's `sec:p09-mu-automaton-to-formula` already permits
separate action labels and supplies the scalar formula construction for
modal parity automata. Arbitrary ordered binary-tree transition rows
use precisely these two action labels. If starting with Pairs acceptance,
its conversion to parity must retain the established acceptance
conventions before invoking that theorem.

Accordingly the reader-facing equivalence/complementation paragraph
should state its full ordered-tree equivalence in the directional
language. The syntactic complementation of the smaller `EX/AX` language
alone does not give complementation of every ordered-tree automaton
language: the reverse translation required in that argument is exactly
the step which fails for the smaller language.

This conclusion follows from the source's actual definitions and the
explicit two-tree calculation. It is not an inference from a missing
proof or from source-history metadata. No manuscript change is made
by this note.
