# Necessity of the global cut for closed guarded ANF

Date: 2026-09-06. Status: a complete mathematical proof of the implication
`Sat(phi) -> Sat(cut(phi))` for the actual ANF grammar in
`handbook/parts/p09/presentations/n-c-018.tex`, at
`sec:p09-mu-anf-grammar`. The proof uses the manuscript's already proved
evaluation-game truth theorem and finite positional parity determinacy.
It does not use a fixed-point substitution argument that changes outer
parameters, nor only a top-level least-fixed-point lemma. No manuscript
edit, software test, build, render, or independent review admission is
claimed by this note.

## 1. Exact syntax, hypotheses, and cut

Fix a finite closed, guarded, well-named ANF formula `phi`. The actual
grammar has constants, proposition literals, fixed-point variables,
disjunction, the two fixed-point binders, and clauses

\[
 \chi_L\land\bigwedge_{i\in I}\nabla_{a_i}\Gamma_i,
 \qquad
 \nabla_a\Gamma
    =\bigwedge_{\psi\in\Gamma}\langle a\rangle\psi
           \ \land\ [a]\bigvee_{\psi\in\Gamma}\psi.
\]

Here `L` is a finite set of proposition literals, `I` is finite, the
actions `a_i` are pairwise distinct, and every `Gamma_i` is a finite
set of ANF formulas. Empty conjunction is true, and empty disjunction
is false. There is no arbitrary-conjunction formation rule. In
particular, a fixed-point variable is not allowed in `L`.

Use raw syntax occurrences and retain every original variable-to-binder
link. Well-naming gives each bound variable one unique binder. The
type of a variable occurrence is the sign of that original binder,
even if the occurrence is inside other, alternating binders.

Define the global cut by recursion on occurrences:

\[
\begin{aligned}
 \operatorname{cut}(\top)&=\top,&
 \operatorname{cut}(\bot)&=\bot,\\
 \operatorname{cut}(\ell)&=\ell
       &&(\ell\text{ a proposition literal}),\\
 \operatorname{cut}(\alpha\lor\beta)
   &=\operatorname{cut}(\alpha)\lor\operatorname{cut}(\beta),\\
 \operatorname{cut}(\sigma X.\alpha)
   &=\operatorname{cut}(\alpha),\\
 \operatorname{cut}(X)
   &=\begin{cases}
       \bot,&\text{the original binder of }X\text{ is }\mu,\\
       \top,&\text{the original binder of }X\text{ is }\nu,
      \end{cases}\\
 \operatorname{cut}\left(
       \chi_L\land\bigwedge_{i\in I}\nabla_{a_i}\Gamma_i\right)
   &=\chi_L\land\bigwedge_{i\in I}
        \nabla_{a_i}\{\operatorname{cut}(\psi):\psi\in\Gamma_i\}.
\end{aligned}
\]

The binder links are classified **before** any erasure. The construction
does not reclassify an outer-variable occurrence using the nearest
remaining binder. Because `phi` is closed, its cut is variable-free and
fixed-point-free. It remains a finite ANF formula.

For occurrence bookkeeping one may temporarily retain repeated target
images as a finite indexed family. Replacing that family by its set
of images leaves the cover formula unchanged, by idempotence of the
finite conjunction and disjunction. This avoids silently identifying
distinct original occurrences while constructing strategies.

## 2. A finite model-free ANF parity game

Define a game `G_phi` whose positions are the raw ANF subformula
occurrences of `phi`. A whole cover clause is one position; its
proposition-literal part is not a second recursively evaluated ANF
subformula. The start is the root occurrence. The rules are:

- At a disjunction, Exists chooses a disjunct.
- At a binder, move forcibly to its body.
- At a bound-variable occurrence, move forcibly to its original binder.
- A true constant wins and a false constant loses for Exists.
- A standalone proposition literal wins for Exists: a single literal
  has some valuation.
- At a cover clause, first inspect `L`. If it contains both `P` and
  `not P` for any proposition `P`, the clause is a losing terminal.
  Otherwise, Forall may choose any indexed target `(i,psi)` with
  `i in I` and `psi in Gamma_i`, and continue at that target occurrence.
  If no such target exists, the clause is a winning terminal.

Thus an empty cover contributes no target, and a consistent clause
whose covers are all empty is winning. The game imposes no model edge
at this stage; it records which successor formulas must independently
be satisfiable. The distinct-action requirement will be used when
constructing an actual model for the cut.

Use the manuscript's occurrence priorities. If `d_X` is the number of
proper enclosing binders of the binder for `X`, give every occurrence
of `X` priority `2d_X+1` when its binder is least and `2d_X` when it is
greatest. Give every other nonterminal position an even default `D`
larger than all these variable priorities. Infinite plays are winning
for Exists exactly when their least infinitely recurring priority is
even; finite terminal outcomes are as just specified.

This game is finite. Every edge other than a variable return descends
the finite syntax hierarchy; in particular every infinite play visits
variable occurrences infinitely often. Terminal outcomes can be
totalized by absorbing even/odd sinks when applying finite positional
determinacy. We will use only the following one-way semantic fact:

\[
 \operatorname{Sat}(\varphi)
       \quad\Longrightarrow\quad
       \exists\text{ wins }G_\varphi.
\]

A full equivalence between satisfiability and this parity game is not
assumed or needed for the necessity proof.

## 3. A satisfying model supplies a winning model-free strategy

Suppose `T,s_* |= phi`. By the evaluation-game truth theorem, fix a
winning evaluation strategy `tau` from `(s_*,phi)`. We construct a
strategy in `G_phi` with memory of one `tau`-compatible evaluation
history, ending at a matching model state and syntax occurrence.

At an abstract disjunction, use the choice prescribed by `tau` at its
matching evaluation position. Binder and variable moves agree with
their original binding links, so extend the matching histories by
their forced moves.

If a constant is reached, it cannot be false: that would give a finite
losing evaluation continuation. An abstract standalone literal is
winning; in fact the corresponding literal must also be true at the
maintained model state, because the virtual history follows a winning
strategy.

Now suppose the abstract game reaches a clause at model state `s`.
Each literal in `L` must be true at `s`: otherwise Forall could select
the false literal conjunct in the evaluation game, contradicting that
the maintained history has a winning continuation. Consequently `L`
is consistent and the abstract game cannot lose its consistency test.

If Forall selects an abstract target `(i,psi)`, extend the virtual
evaluation history by the corresponding conjunction choices: select
that action's cover, and then select its diamond obligation
`<a_i>psi`. A winning `tau` supplies an actual `a_i`-successor `t` and
continues at `(t,psi)`. Such a successor must exist, since an empty
diamond loses. Keep this successor and extended virtual history as
the memory for the next abstract position. If there are no targets,
the abstract play ends with its specified immediate win.

Only the diamond half of a cover is challenged in this extraction.
That is sufficient: every cover target is one of the mandatory diamond
obligations of any winning evaluation strategy. The box half remains
part of the original semantics; ignoring some opponent challenges
cannot turn a winning original strategy into a losing restricted one.

### Occurrences under cover expansion

The evaluation rules may be read directly on the cover abbreviation:
Forall selects a target as a diamond challenge, or selects the box
challenge and then a successor, after which Exists selects a target.
These are precisely the finite Boolean and modal moves of the
displayed expansion of `nabla`. If the ordinary evaluation theorem is
applied to fully expanded syntax, copy and alpha-rename each target
formula in that expansion and retain its projection to the original
target occurrence. Internal variable references use the corresponding
copied binder, while references to enclosing binders retain those
enclosing bindings.

The maintained virtual history identifies which copy is currently
being followed, so its next actual evaluation move is always defined.
Projection preserves each original variable's binder sign and number
of enclosing binders: expanding a cover adds only Boolean and modal
nodes, not new enclosing fixed-point binders. Thus variable priorities
are unchanged by this projection. No positionality of `tau` is
required for the extraction, since its entire virtual history is kept.

### Verification of winning

Every finite abstract play following the extracted strategy ends at a
winning abstract terminal, by the preceding cases. An infinite such
play expands to one infinite `tau`-compatible evaluation play. The
additional vertices used to challenge a cover and take its diamond
are only finite Boolean/modal paths. The same original variable
occurrences, with the same priorities, are visited in the same order.
All added nonterminal vertices have the harmless default priority.
Therefore the two infinite plays have the same least recurring
variable priority. The evaluation play wins, so the abstract play
wins. This establishes `Sat(phi) -> Exists wins G_phi`.

## 4. The first-variable-leaf argument eliminates every least return

By finite positional parity determinacy, choose a **positional** winning
strategy `sigma` in `G_phi` from its root. Form a finite game `G_cut`
by changing every original variable occurrence into a terminal:

- a formerly least-bound variable is losing;
- a formerly greatest-bound variable is winning.

Keep all other rules. Binder moves now merely pass to the body and
can be contracted; after contracting them and reading the variable
terminals as constants, this is the syntax game of `cut(phi)`.
There are no variable-return edges left, so every play is finite.
At its disjunctions, retain the choices made by `sigma` at the
corresponding original occurrences.

We show that no compatible play of `G_cut` can reach a least-bound
variable leaf. Suppose otherwise, and let `X` be that reached variable
occurrence. The path from the root to it contains **no earlier variable
occurrence**, because all such occurrences are now terminal. Hence
this path is a descent through the original syntax hierarchy, with
only binder-to-body, disjunct, and cover-target edges.

Let `b_X` be the original binder occurrence of `X`. Since the formula
is closed and binding is lexical, `b_X` is an ancestor of this occurrence
of `X`; the descent path therefore passes through `b_X`. Consider its
segment

\[
 b_X\longrightarrow\cdots\longrightarrow X.
\]

Restore the original forced return `X -> b_X`. This produces a cycle
in `G_phi`. The cycle is compatible with `sigma`: its disjunct choices
are exactly the positional choices already used on the descent, and
Forall can repeat the same cover-target choices. Its finite reaching
prefix is also compatible with `sigma`. Positionality is essential
here; a history-dependent strategy could prescribe a different
disjunct after returning to `b_X`.

Repeat this cycle forever. It contains no other variable occurrence,
because the descent reached its first variable only at `X`. It may
contain any number of intermediate least or greatest **binders**, but
their positions carry only the default priority; none of their
variables is visited on this cycle. Its only recurring variable
priority is consequently the odd priority of the least-bound `X`.
The repeated play loses for Exists, contradicting that `sigma` wins
from the root.

Thus no least-bound variable leaf is reachable in `G_cut` under the
restricted strategy. A reached greatest-bound variable is a winning
leaf. Every other losing leaf, namely a false constant or a clause
with inconsistent `L`, would already be a reachable losing terminal
of `G_phi`, also contradicting the winning property of `sigma`.
Every finite compatible cut play therefore wins.

### Why this handles outer variables and alternation

The variable `X` need not be bound by the nearest binder: its binder
may lie outside arbitrarily many nested, alternating binders. The
path still passes through that **original** enclosing binder, and
the forced return still closes exactly the displayed cycle. The
intermediate binder signs do not change its winner because no
intermediate variable return lies on a first-variable descent.

This is not an argument that successively changes the parameter
values of nested least and greatest fixed points. No approximant
or nested argument is replaced during the proof. The one positional
strategy belongs to the one fixed occurrence game of the original
closed formula, and every least-variable leaf is excluded there by
the same local cycle contradiction. Greatest-variable leaves are
accepted terminals in the cut, so no removal of greatest returns
needs to be justified by a corresponding least-loop argument.

## 5. The finite cut game implies satisfiability of its cut formula

For completeness of the final implication, define a Boolean test
`b(theta)` on variable-free, fixed-point-free ANF syntax by

\[
\begin{aligned}
 b(\top)&=1,&b(\bot)&=0,&b(\ell)&=1,\\
 b(\alpha\lor\beta)&=b(\alpha)\lor b(\beta),\\
 b\left(\chi_L\land\bigwedge_{i\in I}\nabla_{a_i}\Gamma_i\right)
   &=\operatorname{Cons}(L)
           \land\bigwedge_{i\in I}\bigwedge_{\psi\in\Gamma_i}b(\psi).
\end{aligned}
\]

Here `Cons(L)` means that no proposition occurs with both polarities
in `L`, and empty conjunction is true. Ordinary backward induction
on the finite syntax tree shows that Exists wins the cut game
exactly when `b(cut(phi))=1`: disjunction is existential choice, a
consistent clause requires every target to win, and the terminal
rules agree. Erased binders are forced moves and do not change this
calculation.

We next prove by structural induction that `b(theta)=1` implies a
finite pointed model satisfying `theta`. This is only a witness
construction for the fixed-point-free cut, not a separate proof of
finite-model sufficiency for the original formula.

- For true, use a singleton model. For a standalone literal, use a
  singleton whose valuation satisfies that literal.
- For a true disjunction, use the induction model of a true disjunct.
- For a true clause, choose a fresh root `s` whose valuation satisfies
  the consistent set `L`. For each indexed target `(i,psi)`, take a
  fresh disjoint copy of a finite pointed induction model of `psi`.
  Add an `a_i`-edge from `s` to the root of every such copy. Add no
  other edges from `s`, and leave every copied model's valuations
  and outgoing edges unchanged.

Every target in `Gamma_i` has its required diamond witness. Conversely,
every `a_i`-successor of `s` is one of those copy roots and satisfies
its designated target, so it satisfies the disjunction in the box
part of the cover. If `Gamma_i` is empty, there is no `a_i`-edge from
`s`, and the cover is `[a_i]bot`, which holds. The actions are pairwise
distinct, so the witnesses selected for a different cover do not add
unwanted successors to this one. This is exactly where the grammar's
distinct-action condition is used.

Adding the fresh incoming root edges does not affect any formula at
a copied model state: its reachable forward transition structure and
valuation are unchanged, and these formulas have no backward
modalities. This preservation also follows directly by structural
induction on the fixed-point-free formulas. There are finitely many
targets, each induction model is finite, and the one added root keeps
the result finite. Thus the construction proves the clause case.

Consequently the winning cut strategy from Section 4 yields an actual
finite pointed model of `cut(phi)`.

## 6. Conclusion and exact dependency boundary

Combining the proved implications gives

\[
 \operatorname{Sat}(\varphi)
 \ \Longrightarrow\
 \exists\text{ wins }G_\varphi
 \ \Longrightarrow\
 \exists\text{ wins }G_{\operatorname{cut}(\varphi)}
 \ \Longrightarrow\
 b(\operatorname{cut}(\varphi))=1
 \ \Longrightarrow\
 \operatorname{Sat}(\operatorname{cut}(\varphi)).
\]

The first step uses the already established evaluation-game truth
theorem. The second uses finite positional determinacy and the fully
explicit first-variable-leaf cycle argument. The last steps use only
finite backward induction and the disjoint-copy witness construction
for fixed-point-free ANF. The procedure respects every original outer
binding link and permits arbitrary nesting of least and greatest
binders. No unproved equivalence between the model-free parity game
and full satisfiability, changing-parameter fixed-point identity,
finite-model theorem for the original formula, or sufficiency of the
cut criterion is used.
