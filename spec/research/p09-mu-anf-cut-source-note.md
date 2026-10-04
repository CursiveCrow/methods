# ANF cut equisatisfiability: hypotheses, operation, and primary proof locations

Date: 2026-09-06.

## Bounded outcome

The current grammar at `sec:p09-mu-anf-grammar` in
`handbook/parts/p09/presentations/n-c-018.tex` includes the restrictions
needed to apply the original theorem to its stated **closed, guarded,
well-named output formulas**. In particular, fixed-point variables are
not proposition literals in a special conjunction, and action labels
are distinct within each cover clause. No missing original syntactic
restriction was found for those outputs.

The source conclusion is equisatisfiability over arbitrary rooted
transition models. It is not equivalence at each state, a pointwise
fixed-point identity, or a theorem for arbitrary conjunctions. The
linear bound concerns an already supplied disjunctive/ANF input, not
the cost of normalizing an arbitrary mu-calculus formula.

## Exact primary locators and proof status

1. Janin--Walukiewicz, [*Automata for the modal mu-calculus and related
   results*, author copy](https://www.labri.fr/perso/igw/Papers/igw-mu-aut.pdf):
   Definitions 2.1--2.3 and the convention after Proposition 2.4,
   internal p. 4; disjunctive Definition 4.1, p. 7; cut Theorem 4.6,
   p. 8; linear-time Corollary 4.7, p. 9. Internal pages equal PDF
   pages, not the proceedings' 552--562 pagination. The cut proof is
   a tableau/marking outline; its converse reconstructs a regular
   model without mu-regenerations.
2. Bradfield--Stirling, [*Modal Mu-Calculi*, 2005
   preprint](https://www.pure.ed.ac.uk/ws/files/16483207/Modal_Mu_Calculi.pdf),
   Section 5.4, internal p. 20 (PDF page 21): the binder-body version
   of the cut claim and the linear satisfiability statement follow
   Proposition 5.4. Its ordinal argument is illustrative, not a
   complete proof of simultaneous nested cutting.
3. Walukiewicz, [*Completeness of Kozen's Axiomatisation of the
   Propositional Mu-Calculus*, author
   copy](https://www.labri.fr/perso/igw/Papers/igw-kozen-compl.pdf),
   Theorem 18, internal p. 15: equation (2) cites the JW cut theorem
   and uses it in the provability induction. It does not supply the
   missing detailed cut proof.

The original JW theorem assumes a closed disjunctive formula under
the paper's guarded/well-named convention. Its operation replaces
occurrences of mu-bound variables with `bottom`, and nu-bound
variables with `top`. Removing the now-vacuous binders is the
explicit clarification below, consistent with Corollary 4.7's
fixed-point-free result.

## The exact recursive cut operation

Let `alpha` be the original closed, well-named input. Before removing
any binder, record its kind in the map

\[
 \kappa:\operatorname{BV}(\alpha)\longrightarrow\{\mu,\nu\}.
\]

Define `cut_kappa` on the original raw subformula occurrences by

\[
\begin{aligned}
 \operatorname{cut}_\kappa(\top)&=\top,&
 \operatorname{cut}_\kappa(\bot)&=\bot,\\
 \operatorname{cut}_\kappa(P)&=P,&
 \operatorname{cut}_\kappa(\neg P)&=\neg P,\\
 \operatorname{cut}_\kappa(X)&=
     \begin{cases}\bot,&\kappa(X)=\mu,\\
                   \top,&\kappa(X)=\nu,
     \end{cases}\\
 \operatorname{cut}_\kappa(\psi\lor\theta)
     &=\operatorname{cut}_\kappa(\psi)
            \lor\operatorname{cut}_\kappa(\theta),\\
 \operatorname{cut}_\kappa(\sigma X.\psi)
     &=\operatorname{cut}_\kappa(\psi),\\
 \operatorname{cut}_\kappa
   \left(\chi_L\land\bigwedge_{i\in I}\nabla_{a_i}\Gamma_i\right)
     &=\chi_L\land\bigwedge_{i\in I}
          \nabla_{a_i}
           \{\operatorname{cut}_\kappa(\psi):\psi\in\Gamma_i\}.
\end{aligned}                                                    \tag{1}
\]

Here `chi_L` contains only proposition literals. Constants inserted
at variable occurrences are Boolean constants, not new proposition
letters. The map `kappa` continues to refer to the **original** binder
of an occurrence after enclosing binders have been erased.

Write `cut(alpha)=cut_kappa(alpha)`. It contains neither fixed-point
binders nor fixed-point variables. This is not ordinary substitution
of free variables in the closed formula `alpha`, which would replace
nothing. It is an occurrence rewrite using the original binder links.
It also does not replace an entire mu-subformula by `bottom` or an
entire nu-subformula by `top`: for example

\[
 \operatorname{cut}(\mu X.P)=P,\qquad
 \operatorname{cut}(\nu X.\bot)=\bot.
\]

For a nested example, the well-named guarded ANF

\[
 \nu X.\left(P\land\nabla_a
     \{\mu Y.(Q\lor\nabla_b\{X,Y\})\}\right)
\]

cuts to

\[
 P\land\nabla_a\{Q\lor\nabla_b\{\top,\bot\}\}
 \equiv P\land\nabla_a\{Q\}.
\]

The outer variable `X` is replaced according to its nu-binder even
inside the erased mu-binder for `Y`. The inner `bottom` target makes
that particular `b`-cover impossible, explaining the simplification.

## The theorem's quantifiers

For a closed formula `theta`, define

\[
 \operatorname{Sat}(\theta)
   \quad\Longleftrightarrow\quad
   \exists\mathcal T\ \exists s\in S_{\mathcal T}\ 
           (\mathcal T,s\models\theta),
\]

where `T` ranges over ordinary nonempty transition models, with no
seriality, branching bound or acyclicity restriction. The source
result, at the promised input class, is exactly

\[
 \operatorname{Sat}(\alpha)
       \Longleftrightarrow\operatorname{Sat}(\operatorname{cut}(\alpha)).
                                                               \tag{2}
\]

The two existential witnesses need not be the same pointed model.
For example `nu X.nabla_a{X}` cuts to `nabla_a{top}`. A root with a
single edge to a dead end satisfies the cut but not the original;
the original is satisfiable on a one-state self-loop. This also shows
why (2) cannot simply be relativized to finite acyclic models.

## Comparison with the actual manuscript grammar

| Original restriction | Actual grammar/output condition inspected |
|---|---|
| Positive fixed-point variables | ANF is declared positive; negation is confined to proposition literals. |
| No bound `X` as conjunctive literal `X and gamma` | The literal part of a cover clause admits only `P, not P`, and the text explicitly excludes a bound variable there. |
| At most one cover per action in a special conjunction | Its clause requires the `a_i` to be pairwise distinct. |
| No general closure under conjunction | The grammar explicitly denies this closure. |
| Guarded, well-named formula | Required of output normal forms; guarding is relative to each binder's own body. |
| Closed input to the cut theorem | The final output is explicitly closed. |

Constants and zero-action/empty-literal clauses do not violate the
original restrictions. JW Section 2 includes Boolean constants among
propositions/literals and fixes the empty Boolean conventions.
An empty cover is allowed: it means no successor for that action.
Guardedness is not inferred from ANF membership alone, nor from a
modality outside a binder.

## Supplied witnesses that the restrictions matter

Allowing fixed-point variables as conjunctive literals would admit

\[
 \theta_1=\nu Y.(P\land\nabla_a\{Y\land\neg P\}).
\]

This formula is closed, positive, guarded and well-named, and has no
repeated action in a clause. Nevertheless it is unsatisfiable. Any
fixed point `U` of its body is included in `V(P)`; therefore
`U intersect V(not P)` is empty, so its required diamond cannot
hold and `U` is empty. Its proposed cut is

\[
 P\land\nabla_a\{\neg P\},
\]

which a `P` root with one `not P` child satisfies. The current grammar
correctly excludes `Y and not P` as a cover target formula.

Independently, allowing two covers for the same action would admit

\[
 \theta_2=\nu Y.(\neg P\land
                       \nabla_a\{P\}\land\nabla_a\{Y\}).
\]

Any fixed point `U` lies in `V(not P)`, while the two covers require
an `a`-successor in `V(P) intersect U`, impossible. Its cut

\[
 \neg P\land\nabla_a\{P\}\land\nabla_a\{\top\}
\]

is satisfiable. Apart from its repeated action, this formula obeys
the other restrictions. The current distinct-action condition
correctly excludes it.

The simpler non-ANF formula
`(mu X.(P or <a>X)) and not P` is also satisfiable while its cut is
unsatisfiable; unrestricted conjunction therefore cannot be admitted.

## Precise linear-time decision boundary

Once (2) has been established, the fixed-point-free cut is evaluated
bottom-up for satisfiability. Constants have their Boolean values;
each proposition literal alone is satisfiable; disjunction takes the
Boolean disjunction. For a clause, the exact recurrence is

\[
 \operatorname{Sat}
  \left(\chi_L\land\bigwedge_{i\in I}\nabla_{a_i}\Gamma_i\right)
 \quad\Longleftrightarrow\quad
 \operatorname{Cons}(L)\land
       \bigwedge_{i\in I}\bigwedge_{\gamma\in\Gamma_i}
                                    \operatorname{Sat}(\gamma).
                                                               \tag{3}
\]

The empty inner conjunction is true. For the right-to-left direction,
take disjoint pointed models for the child formulas, add a new root
satisfying the consistent literal set, and connect it to those roots
using the corresponding distinct actions. Both cover requirements
hold; empty covers get no successors. This is a direct proof of
(3), not a proof of the fixed-point cut theorem (2).

Count size in the written ANF syntax, including literal occurrences
and cover-target occurrences. The rewrite (1) does not duplicate
subformulas, and (3) visits each occurrence once. With the usual
interned atomic identifiers and original binder links, and a linear
literal-clash scan, this gives `O(n)` time. If raw identifier strings
are used, their processing cost belongs in the input size/cost model.
Repeated cover targets produced by the cut may be retained in the
representation: idempotence makes deduplication unnecessary for this
bound. No linear-size or linear-time bound for obtaining the ANF
from an arbitrary input follows.

## A fuller primary follow-up, with its applicability condition

Arnold--Janin's author-hosted [*A note on the satisfiability problem in
fixpoint calculi*, Draft Version](https://www.labri.fr/perso/janin/Papiers/csl97.pdf)
prints a longer algebraic proof. Definition 4.2, p. 8, gives lower
and upper cuts; Theorem 4.3 and Lemmas 4.4--4.5, pp. 8--10, prove
preservation of Boolean non-bottom projections; Corollary 4.6,
pp. 10--11, gives the linear bound assuming arity-linear primitive
Boolean projections.

Its algebra must be both disjunctive and compact. Specifically,
Definitions 2.1/2.3, p. 6, use a family `C_M` generated by bottom,
top, primitive operations and arbitrary meets, with

\[
 \bigwedge E=\bot\quad\Longleftrightarrow\quad
 \exists F\subseteq_{\mathrm{fin}}E\ (\bigwedge F=\bot)
 \qquad(E\subseteq C_M).
\]

Definition 3.2, p. 7, requires each primitive's non-bottom truth
value on `C_M` to depend only on its arguments' non-bottom truth
values. The greatest-fixed-point limit cases explicitly use the
compactness hypothesis. These are algebraic closed elements, not
merely syntactically closed formulas.

Thus this draft supplies useful detailed methodology, but invoking
it for modal ANF requires a specified interpretation algebra and
verification of these hypotheses. This bounded investigation does
not establish that applicability, and does not substitute the
generalized theorem for the exact JW modal result.

## Handoff boundary

Only this source note was written. No manuscript, other note, code,
test, build, render or additional agent was created or changed.
The grammar comparison, exact occurrence rewrite, counterexamples
and local cut-evaluation recurrence are supplied checks. A complete
independent proof of (2) is being developed separately and is not
claimed by this note.
