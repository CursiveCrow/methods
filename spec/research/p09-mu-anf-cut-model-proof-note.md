# From a satisfiable ANF cut to an explicit finite model

Date: 2026-09-06. Scope: the sufficiency implication for the cut of a
closed, guarded, well-named ANF formula in the current manuscript's cover
grammar. The proof constructs a finite model of the original formula,
with no mu-variable returns in its winning evaluation strategy. It does
not assert truth of the original formula in the given cut model, and it
does not prove the converse satisfiability implication.

The ANF grammar and cover game are those of
`handbook/parts/p09/presentations/n-c-018.tex`, at
`sec:p09-mu-anf-grammar` and the preceding cover definitions. The already
proved evaluation-game truth theorem is used at the end. No semantic
completeness or unproved satisfiability-game assertion is used.

## 1. Original occurrences and the cut

Fix a closed, guarded, well-named ANF formula `phi`. Its finite syntax is
viewed in the cover presentation: a clause is a node labelled by

\[
 \chi_L\land\bigwedge_{a\in J}\nabla_a\Gamma_a,
\]

where `L` is a finite set of proposition literals, `J` is a finite set of
distinct actions, and each target formula in a finite `Gamma_a` is a child
occurrence of that clause. The remaining constructors are disjunction,
mu/nu binders, constants, proposition literals, and fixed-point variables.
Repeated written subformulas at different places have distinct occurrences.
Every variable occurrence has its original unique binding occurrence.

Let `O` be this original occurrence tree and let `n=|O|`. Count one tree
edge from a clause to each of its action-indexed target occurrences; call
these the cover edges. Let

\[
 t_\varphi=
 \sum_{c\text{ an original clause}}
                \ \sum_{a\in J_c}|\Gamma_{c,a}|.
\]

Thus `t_phi` is the number of cover-target occurrences in this presentation.
The literals decorating a clause need not be additional child vertices for
this count; including them in a larger syntax-size convention only weakens
the bounds below.

Define `K(u)` for every original subformula occurrence `u` by recursion
on this finite tree:

- Keep proposition literals and constants unchanged.
- Commute with disjunction.
- Erase an original binder: `K(sigma X.alpha)=K(alpha)`.
- Replace each original variable occurrence by `bottom` if its own original
  binder is mu, and by `top` if its own original binder is nu.
- Keep a clause's literal guard and action labels, replacing every target
  `gamma` by `K(gamma)`.

The cut of the input is `K(phi)`. All these formulas are variable-free
modal formulas: original closedness gives a binding sign for every variable
occurrence, including occurrences free in the particular subformula `u`.
The binding classification is performed in the original formula, not by
searching a formula after its binders have already been erased.

Different original targets can have the same cut. The cut's finite target
set may remove such duplicates, since conjunction and disjunction are
idempotent. The proof nevertheless retains **every original target
occurrence**, so no binding information is lost through that simplification.

Assume a pointed model `(T,w_*)` satisfies `K(phi)`. This model may be
infinite, infinitely branching, or nontotal. We use only finitely many
of its truth witnesses to select a finite original-syntax subtree.

## 2. Select an original-syntax tree without unfolding variables

Starting at `(phi,w_*)`, construct a selected subtree `T_sel` of `O`,
temporarily attaching a witness state `w_u` to each retained occurrence.
Maintain

\[
 T,w_u\models K(u).
\]

The construction is a recursion on proper original subformula occurrences.

1. At a binder, retain its body with the same witness state; its cut is
   precisely the binder's cut.
2. At a disjunction, choose one disjunct whose cut is true at the current
   witness state, retain that child, and record this fixed choice for the
   original disjunction occurrence. There is such a child by Boolean truth.
3. At a clause, keep the clause and all its original target occurrences.
   Its literal guard is true at `w_u`, hence contains no opposite literals.
   For every action `a` and every original target `gamma in Gamma_a`,
   choose a witness `w_gamma` with

   \[
    R_a^T(w_u,w_\gamma),\qquad T,w_\gamma\models K(\gamma).
   \]

   The diamond conjunct belonging to `K(gamma)` supplies such a witness.
   If multiple targets have the same cut, the same witness is available
   for each, but their original occurrences remain distinct. Retain their
   subtrees recursively. For an empty target set there is no child to create.
4. Retain a true proposition-literal or `top` leaf. A `bottom` leaf cannot
   be reached under the maintained truth assertion.
5. Retain an original nu-variable as a leaf, since its cut is `top`.
   An original mu-variable cannot be reached, since its cut is `bottom`.

There are finitely many recursive calls, because every call descends the
finite original occurrence tree. Each original occurrence is visited at
most once. The construction has chosen one child at each retained
disjunction, all original cover targets at each retained clause, and the
body of every retained binder. It has not unfolded either kind of variable.

The resulting finite tree therefore has these properties:

- no retained variable leaf is mu-bound;
- no retained constant is `bottom`;
- every retained literal guard is propositionally consistent;
- every retained variable's unique original binder is a retained ancestor;
- each retained clause still has all its original cover-target children.

These are the only properties of the cut model used from now on. The new
model will not reuse its states or its relations. In particular, the cut
model's box constraints are not preserved by a same-model argument; the
new model's box constraints will follow directly from its generated edges.

## 3. Restore nu returns and prove nonmodal termination

Form a finite directed graph `G` on the retained occurrence vertices.
Keep every selected downward tree edge. Mark clause-to-target edges as
cover edges with their action labels. Binder-to-body edges and the fixed
disjunction-choice edges are nonmodal. For each retained nu-variable
occurrence `X`, add its nonmodal return edge to the original binding
occurrence `nu X.alpha`. This return is to a retained proper ancestor.
There are no mu-variable returns because no such leaf was retained.

Let `G_0` be obtained from `G` by deleting all cover edges. Every vertex
of `G_0` has exactly one successor unless it is a clause, a proposition
literal, or `top`, in which case it has no successor. In particular, all
syntactic choices in `G_0` have already been fixed.

**Lemma.** The finite graph `G_0` is acyclic.

**Proof.** In a tree with downward edges and edges back to proper
ancestors, every simple directed cycle has exactly one ancestor return.
To verify this, begin a proposed simple cycle at a vertex of smallest
tree depth. Before its first return edge, its downward edges follow one
tree branch. The return target is an ancestor of its source. It cannot
lie above the starting vertex by minimality, and it cannot be a different
internal vertex of the already traversed branch, because that repeats an
internal vertex before the simple cycle closes. Thus the first return
already returns to the starting vertex and closes the cycle.

In `G`, such a cycle consists of a retained downward path from a nu-binder
to an occurrence of its own variable, followed by that variable's return.
Guardedness of that binder says that this downward path passes below a
modality in its body. In the ANF occurrence tree, that means it traverses
at least one clause-to-target cover edge. Therefore no such cycle survives
in `G_0`. Every finite directed graph containing a cycle contains a simple
cycle, so `G_0` is acyclic. QED.

The guarding is relative to the returning variable's own binder. An outer
modality above that binder would not suffice; this is why merely putting
an unguarded fixed point inside a cover would not justify the lemma.

Consequently every vertex `u` of `G_0` follows a unique finite path to an
endpoint. Denote it by `h(u)`. Let `E` be the set of endpoints; these are
exactly the retained clause, proposition-literal, and `top` occurrences.
The set is nonempty, since the root has an endpoint. Along every nonmodal
edge `u -> v`,

\[
 h(u)=h(v).
\]

In particular, for every retained variable return,

\[
 h(X)=h(\nu X.\alpha)=h(\alpha).
\]

This equality is the mechanism that makes the later binding return a move
at the **same model state**, as required by the evaluation game. We do
not redirect the variable's game move to a different model state.

## 4. Define the finite model from endpoints

Define a new model `M` with state set `E` and initial state `h(phi)`.
For an endpoint `c`, let `L_c` be its guard if it is a clause, its
singleton literal set if it is a proposition literal, and the empty set
if it is `top`. Interpret each original proposition `P` by

\[
 V_M(P)=\{c\in E:P\in L_c\}.
\]

No `L_c` contains both `P` and `not P`. Thus every positive and every
negative literal in `L_c` is true at `c`. Interpret `top` and `bottom`
in the usual way. Propositions not required positively are simply false.

For every original action `a`, set

\[
 R_a^M=
 \{(c,h(\gamma)):
     c\in E\text{ is a clause},\
     a\in J_c,\ \gamma\in\Gamma_{c,a}\}.
\]

Here `gamma` denotes the corresponding retained original target occurrence.
There are no other edges. Literal and `top` endpoints have no outgoing
edges. At a clause endpoint, an omitted action or an empty target set
therefore has no successors of that action. Duplicate generated pairs
are identified, as they should be in a binary relation.

This construction assigns literals to distinct endpoint occurrences. A
nu return can make a target's endpoint be an already existing ancestor
endpoint, but no conflicting literal guard is merged into it: the route
from that target to its endpoint contains only binders, fixed disjunction
choices, and variable returns, not another clause whose guard was ignored.
The first clause reached is the endpoint itself.

The distinct-action condition is essential. At a clause `c`, every
`a`-edge in the new model is generated by a target of its one cover
`nabla_a Gamma_{c,a}`. There is no second independent cover with action
`a` whose target constraints would also have to hold on that edge.
No closure under arbitrary conjunction is used.

## 5. A winning evaluation strategy for the original formula

Use the manuscript's ordinary evaluation game, with covers understood by
their displayed expansion and successor-first box choice. Working in the
cover presentation just suppresses its finite Boolean administration.
If expansion copies a target formula, make the copies capture-avoiding
and carry the same occurrence recipe into each copy, with corresponding
binder links. This is the usual macro expansion of the cover game; the
same formula target has the same available continuation in either its
diamond or its box occurrence. The argument does not merge distinct
original binders.

We maintain the following invariant whenever a retained original formula
occurrence `u` is the current formula control:

\[
 \text{the current model state is }h(u).
\]

Initially it holds by the choice of root state. The strategy is defined
as follows.

- At a disjunction occurrence, choose its previously selected child.
  This is a nonmodal edge of `G_0`, so the endpoint and current state
  remain the same.
- Binder openings are forced edges of `G_0` and preserve the invariant.
- At a retained nu-variable, take its forced return to its original
  binder. The equality of endpoints proved in Section 3 means this is
  indeed a return to that binder at the unchanged model state. Its body
  is then exposed and the same fixed syntax choices are followed again.
- At a proposition literal or `top`, the terminal is true by construction.
  No retained `bottom` or mu-variable control exists.
- At a clause endpoint `c`, every literal challenge is true. If Forall
  selects the diamond demand for `gamma in Gamma_{c,a}`, Exists uses the
  edge `c -> h(gamma)` labelled `a`. The target occurrence is then `gamma`
  at state `h(gamma)`, preserving the invariant.
- If Forall selects the box demand for action `a` and chooses an actual
  successor `v`, the definition of `R_a^M` gives at least one original
  target `gamma in Gamma_{c,a}` with `h(gamma)=v`. **After** this successor
  choice, Exists selects such a target from the box disjunction. Its
  current state is already `v=h(gamma)`, so the invariant resumes there.

When different targets generate the same successor, any one of their
recorded origins can be used for the box response. Every diamond demand
still has its own required witness, even if witnesses coincide. A finite
choice of origin for each generated edge fixes this response in advance;
history may also retain the current cover occurrence if desired.

These cases include all terminal situations. An empty clause or empty
literal conjunction is true. An empty cover has no generated successors,
so its box challenge wins. A nonempty cover has the specified edge for
every diamond demand, including a `top` target. A `top` target's terminal
endpoint wins when reached. An original nu-variable whose cut was `top`
is **not** treated as a terminal in this game; it follows the restored
binding return and the endpoint invariant. That is precisely the part
not licensed by a same-model substitution argument.

It remains to check infinite plays. Any nonterminating compatible play,
after suppressing only the finite Boolean administration of guards and
covers, follows `G`: ordinary syntax follows its selected downward edges,
modal challenges follow one cover edge to the chosen original target,
and variable returns follow its restored ancestor edges.

A path with only finitely many ancestor returns would eventually descend
the finite original occurrence tree forever, which is impossible. Thus
an infinite compatible play has infinitely many variable returns. Every
one of them is to a nu-variable; no mu-variable was retained. Under the
manuscript's priority assignment, each such variable priority is even,
including when there are mu-binders among its enclosing binders. The
remaining priorities are larger defaults. The finite priority range
therefore has an even least recurring member, and Exists wins.

In addition, acyclicity of `G_0` shows that there must be infinitely many
actual modal moves on any infinite compatible play. No accepted play is
being supplied by an unguarded administrative loop. Mu-binders may still
be opened, or even reopened infinitely often after nu returns; what is
excluded is an actual mu-variable return, the event carrying its odd
evaluation priority.

All compatible finite and infinite maximal plays are winning. Extend the
strategy arbitrarily on irrelevant histories if a globally defined
strategy is required. The already proved evaluation-game truth theorem
now gives

\[
 M,h(\varphi)\models\varphi.
\]

This proves sufficiency, including arbitrarily nested alternation and
references to outer binders. The construction uses original binding links
and the same-state endpoint invariant, rather than assigning a closed
semantic value independently to each open target subformula.

## 6. Explicit bounds and two scope checks

The endpoint model has

\[
 1\leq|E|\leq|T_{\mathrm{sel}}|\leq n
\]

states. Each generated action-labelled edge is contributed by one
retained original cover-target occurrence, so

\[
 \sum_a|R_a^M|\leq
 \sum_{c\text{ a retained clause}}\sum_{a\in J_c}|\Gamma_{c,a}|
 \leq t_\varphi.
\]

The sum counts labelled pairs `(a,c,v)`, so edges with different action
labels remain distinct. Duplicate pairs for the same action can only
reduce the count. These are linear bounds in the original ANF occurrence
presentation, not in the size of some earlier formula before its possibly
large conversion to ANF. Computing `h` on the selected finite graph and
forming these relations are explicit finite operations. Selection from a
cut-satisfying witness was proved above; a separate model-free decision
procedure may provide the same finite choices, but is not needed here.

For the simplest nontrivial example, take

\[
 \varphi=\nu X.\nabla_a\{X\},\qquad
 K(\varphi)=\nabla_a\{\top\}=\langle a\rangle\top.
\]

A two-state model with just `s -> t`, with `t` dead, satisfies the cut at
`s` but not the original formula: the dead state cannot satisfy its
nonempty cover, and then neither can its predecessor. The construction
instead has one endpoint, the cover clause, and generates an `a`-self-loop.
That finite model satisfies the original formula. Thus the theorem is
equisatisfiability in this direction, not same-model truth equivalence.

For nested alternation, consider

\[
 \nu X.\mu Y.
     \bigl(\nabla_a\{X\}\lor\nabla_b\{Y\}\bigr).
\]

Its cut's `b`-disjunct has a bottom target and cannot be satisfied; the
selected disjunct is the `a`-cover. The model is again a one-state `a`-loop.
Each loop returns through `X` and reopens the inner mu-binder for `Y`, but
never returns through `Y`. This illustrates why repeated mu-binder visits
do not invalidate the even-priority argument.

## 7. Exact conclusion

For every closed, guarded, well-named ANF formula `phi`, if its specified
original-binding cut is satisfiable, then `phi` is true in the explicit
finite endpoint model above. Its selected evaluation graph has no
mu-variable returns, and every infinite play takes real modal steps
between its nu recurrence cycles. The proof does not require the cut's
given satisfying model to be finite or finitely branching.

The converse implication, any model-free Boolean satisfiability test,
and any claim that the original formula and its cut agree in the same
model are outside this note's proved scope.

Only this proof note was created. No manuscript edits, code, tests,
builds, renders, or additional agents were used.
