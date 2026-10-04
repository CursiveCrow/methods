# Modal parity automata to the Emerson--Jutla layered game

Date: 2026-09-06.

Scope: the proposed bridge to the tuple and games at
`sec:p09-presentation-n-c-018-emerson-jutla` in
`handbook/parts/p09/presentations/n-c-018.tex`. The tuple, Streett convention,
and history-free definition were read at presentation lines 2389–2453;
the modal acceptance game was read at lines 4075–4118. The manuscript is
being edited concurrently. This note proves the proposed construction;
it does not claim to reproduce the deferred source proof of Theorem 3.1.

## Statement and required observations

Let `Q` be a nonempty finite control set, `q0` its initial control, and
`p: Q -> N` a priority map with least-recurring-even acceptance. Fix a
finite alphabet `Sigma` and a full binary input tree
`t: {0,1}* -> Sigma`. Each transition `B_(q,A)` is a finite positive Boolean
formula over atoms `(i,r)`, where `i` is 0 or 1 and `r` belongs to `Q`.
An atom continues to `(xi,r)` from the input node `x`.

This directional form covers the two modal conventions needed here.
On a tree with one designated successor in direction `i`, both the
diamond and the box for `i` become the atom `(i,r)`. For the source's
undirected child modalities, `EX r` becomes
`(0,r) or (1,r)`, while `AX r` becomes `(0,r) and (1,r)`.
Arbitrary action relations unrelated to those child relations are not
part of this binary-tree reduction.

Under these hypotheses the proposed construction is correct. One must
give the fresh true control legal transitions for every input letter,
and keep the source's single-symbol observations distinct from arbitrary
sets of simultaneously true propositions. Both details are made explicit
below.

## A finite DNF with controlled empty cases

For a positive Boolean expression `B`, define a finite family `F(B)` of
finite sets of atoms recursively:

- `F(true) = {empty set}` and `F(false) = empty family`.
- `F(a) = {{a}}` for an atom `a`.
- `F(C or D) = F(C) union F(D)`.
- `F(C and D) = {U union V : U in F(C), V in F(D)}`.

Then `B` is equivalent, under every truth valuation of its atoms, to the
disjunction over `U in F(B)` of the conjunction of the atoms in `U`.
This follows directly by induction and distributivity. An empty term is
true; an empty family is false. Repeated atoms inside a term disappear
by idempotence. Identical terms may also be merged. No negations or
auxiliary truth variables are needed.

The construction gives two useful strategy facts, proved at the same
time. First, a strategy for the existential player in the finite Boolean
evaluation game that never reaches false determines a member of `F(B)`
whose atoms are exactly the reachable atom labels: use the chosen child
at a disjunction, and take the union of the sets supplied by both children
at a conjunction. True leaves contribute the empty set. Second, for
every `U in F(B)`, there is a Boolean-game strategy that reaches only true
leaves or atoms belonging to `U`: value just the atoms in `U` as true and
use the ordinary winning strategy for the resulting true expression.
These facts justify the conversion at the game level, including formulas
with repeated atoms and formulas whose existential choices occur below
universal conjunctions.

## The layered automaton

Put `OR = Q union {q_top}`, where `q_top` is fresh, and set
`p(q_top) = 0`. For every `q in Q`, `A in Sigma`, and
`U in F(B_(q,A))`, create

`d(q,A,U) in DAND`, with `q psi d(q,A,U)` and `L(d(q,A,U)) = A`.

For each `i in {0,1}`, create `a(q,A,U,i) in AAND` and define

`delta(d(q,A,U),i) = a(q,A,U,i)`.

The set of `chi`-successors of that AAND control is

`S_i(U) = {r in Q : (i,r) in U}`

when this set is nonempty, and is `{q_top}` when it is empty.
There are no other successors at that control.

Complete the true control as follows. For every `A in Sigma`, add a
DAND control `d_top(A)` with label `A` and
`q_top psi d_top(A)`. Give it two directional AAND targets, each with
the unique `chi`-successor `q_top`. Thus every input label and every
choice of direction permits continued play at `q_top` forever. The
phrase “even self-loop” must include these legal DAND/AAND transitions;
an edge directly from one OR control to itself would not have the
source tuple's prescribed type.

All sets are finite. The displayed `delta` is total on
`DAND x {0,1}`, and every AAND control has a successor. At `(x,q)`,
Player I may select precisely a term for `B_(q,t(x))`, because the label
test excludes DAND controls for other letters. Player II chooses a
direction and then a member of its successor set. The order of these
two universal choices permits exactly the same real challenges as a
single choice of an atom in the term, together with the harmless
challenges into `q_top` for directions omitted from the term.

An empty DNF supplies no legal Player-I choice at that position and
therefore rejects there. This is permitted by the tuple: `psi` need not
be total. An empty term supplies `q_top` for both directions and therefore
accepts immediately in the sense of an accepting infinite continuation.

## From the original Boolean game to the layered game

Suppose `sigma` is a winning strategy in the original modal automaton
game. It may depend on the entire history. Construct a layered-game
strategy while retaining a virtual original-game history whose last
position is the current real `(x,q)`.

At `(x,q)`, restrict `sigma` to the finite evaluation of
`B_(q,t(x))` after that virtual history. All opponent conjunction choices
remain available. No reachable leaf is false, because the resulting
finite losing play would contradict that `sigma` wins. By the first
DNF strategy fact, its reachable atom labels form a term `U` in the
DNF family. Choose `d(q,t(x),U)`.

If Player II selects a direction omitted by `U`, enter `q_top` and use
its perpetual legal strategy. That play wins since only priority 0
recurs after entry. Otherwise Player II selects some `r` with
`(i,r) in U`. Choose one finite Boolean path realizing this atom under
the restricted original strategy. Such a path exists by the construction
of `U`. Extend the virtual history by that path and the direction-`i`
move to `(xi,r)`, and repeat.

Each finite realization is chosen relative to the entire current virtual
history. It therefore fits the same strategy even when `sigma` is not
positional, or when several Boolean occurrences have the same atom
label. Their distinct old histories need not be kept as separate layered
controls; one compatible realization is enough for the opponent's
selected atom.

An infinite layered play either enters `q_top`, and wins there, or
produces by concatenation an infinite original play following `sigma`.
In the latter case the OR sequences are exactly the original control
sequences, so their least-recurring priorities agree. No consistent
layered play can reach a position with no legal Player-I move: its
virtual history is still compatible with the winning original strategy
and therefore supplies the next term. The constructed strategy wins.

## From the layered game to the original Boolean game

Suppose `tau` is an accepting layered-game strategy. Retain a virtual
layered history ending at the current original-game position `(x,q)`.
The strategy selects `d(q,t(x),U)` for some legal term `U`.
By the second DNF strategy fact, choose a local Boolean strategy that
reaches only true leaves or atoms in `U`, and follow it in the actual
original expression game.

A reached true leaf ends the original play with the required win. A
reached atom `(i,r)` belongs to `U`, so the selected direction has the
real successor `r`; it does not use the padding successor. Extend the
virtual history by Player II selecting direction `i` and that successor
`r`, and continue at `(xi,r)` in both games.

These virtual choices are legal even though the actual opponent chose
through a Boolean syntax tree instead. If several occurrences print the
same atom, each gives the same legal virtual continuation. A layered
history cannot require retaining an omitted Boolean occurrence: it is
exactly the layered strategy's own history that is being retained.

Every finite original play under this strategy ends at true. Every
infinite original play completes infinitely many finite Boolean episodes
and produces an infinite virtual layered play following `tau`, with
exactly the same control sequence. The original play therefore satisfies
the layered game's parity condition. This proves the converse and hence
equality of the accepted tree languages.

## The Streett pairs equal least-even parity

For each odd priority `j` used by the original controls, set

`G_j = {q in OR : p(q) = j}`,

`R_j = {q in OR : p(q) is even and p(q) < j}`.

Let `Phi` require, for every such `j`, that infinitely many occurrences
of `G_j` imply infinitely many occurrences of `R_j`. Extra pairs for odd
priorities not used by any control have empty green sets and can be
included or omitted.

Consider an infinite OR sequence and let `m` be its least infinitely
recurring priority. Such an `m` exists since the priority range is finite.
If `m` is even and `G_j` recurs infinitely, then `j >= m`, and because
`j` is odd it follows that `j > m`. A priority-`m` control recurs infinitely
and belongs to `R_j`, so the Streett implication holds. If `m` is odd,
then `G_m` recurs infinitely while every priority less than `m` occurs
only finitely often. The finite union `R_m` therefore occurs only finitely
often, violating its implication. Thus `Phi` and least-even parity agree
on every infinite OR sequence.

This conversion uses the stated least-recurring convention. It does not
identify it with the source's separate largest-recurring color convention
in Section 4. The sets just constructed are Streett pairs on the source's
OR sequences and satisfy its definition directly.

## History-free accepting strategies

Fix an accepted input tree `t`. Form its layered acceptance arena with
Player-I positions `(x,q)`, directional Player-II positions `(x,d)`, and
successor-choice Player-II positions indexed by the current input node
and AAND control. The only Player-I decisions are the choices of DAND
controls at `(x,q)`. Label OR positions by `p(q)` and assign every
intermediate position a fixed priority larger than every OR priority.
Every continuing round takes a bounded positive number of moves to the
next OR position, so the least recurring priority of an infinite arena
play equals that of its OR sequence.

If required to invoke the total-arena formulation of positional parity
determinacy, totalize a missing Player-I move by a fresh losing arena
sink. This is only a proof device; an accepting strategy never reaches
such a position. The input tree may be infinite, but the priority range
is finite, so the manuscript's positional parity theorem applies.

By the preceding pointwise Streett/parity equivalence, an accepting
strategy for `Phi` is winning for this parity arena. Positional
determinacy supplies a positional winning strategy in the arena. Its
choice at an OR position is consequently a function of `(x,q)` alone.
Since `t` is fixed, the current input letter is already determined by
`x`. This is exactly Definition 2.7's history-free condition. Each play
following this strategy still satisfies `Phi`, by the same pointwise
equivalence of objectives.

This proves history-freedom for the constructed automaton. It does not
use a claim that an arbitrary change in acceptance condition preserves
the existence of strategies with a particular memory restriction. The
existing sentence “Because only the acceptance condition changes, the
construction preserves history-freedom” is not a valid general inference;
the parity argument supplies the needed justification for this specific
construction.

## Alphabet fidelity and finiteness

For a modal formula using the finite set `P0` of proposition symbols, a
general transition-system automaton observes letters in `2^P0`. For the
source's single-symbol tree `t(x) in Prop`, the correct observation map is

`obs(a) = {P in P0 : a = P}`.

Its finite image consists of singleton observations for symbols in `P0`
and, when other symbols are possible, the empty observation. The node
labels of the observed tree are `obs(t(x))`. One can carry out the entire
finite construction over this image, or over `2^P0` and restrict to these
observed trees. Satisfaction of the original formula is preserved because
each relevant proposition has exactly its original truth value.

This relabelling must be stated. An arbitrary `2^P0`-labelled tree can
make two distinct source proposition symbols true at one node, which is
not a source model under its single-symbol convention. Conversely, a
finite explicit DAND set with a single-valued label map cannot directly
recognize all labels of an infinite original alphabet: only finitely
many labels occur in the image of that map. If an automaton over the
original source alphabet is wanted literally, assume that alphabet is
finite and create the labelled DAND copies for each original letter,
using its observed transition. Otherwise state the finite observation
relabelling and describe acceptance on those observed trees.

## Review outcome

The proposed bridge, both strategy translations, the Streett conversion,
and the positional proof of history-freedom are valid with the finite
alphabet/observation convention and the full layered transitions for
`q_top` stated above. Repeated atoms, omitted directions, empty terms,
empty DNFs, and current-letter legality are all covered. No manuscript
edits, tests, builds, or renders were performed by this reviewer.
