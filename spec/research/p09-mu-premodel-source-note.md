# B&S premodels: dependencies, coherent choices, and signature boundaries

Date: 2026-09-06.

## Source and scope

Primary source: Bradfield--Stirling, [*Modal Mu-Calculi*, preprint
dated 15 November 2005](https://www.pure.ed.ac.uk/ws/files/16483207/Modal_Mu_Calculi.pdf).
Use its printed page numbers, not the published chapter's pagination.
Printed p. 10 is PDF page 11, p. 11 is PDF page 12, and p. 12 is PDF
page 13.

Section 3.6 supplies a quasi-model, one choice function, dependency
trails and well-foundedness on p. 10. Theorem 3.1 is on p. 10;
Theorem 3.2 and signatures are on p. 11; the proof discussion and
converse construction finish on p. 12. The source attributes the
fundamental theorem to Streett--Emerson and distinguishes later
variants with relaxed choices.

The source presentation is compressed. The literal/environment base
conditions, root annotation, occurrence semantics and binder-entry
signature bookkeeping require explicit treatment in a formal host
presentation. The repairs below do not assert that the source's
intended theorem is false.

Live host sections read:

- `sec:p09-mu-evaluation-game` in
  `handbook/parts/p09/presentations/n-c-018.tex`;
- the opening and base cases of `sec:p09-mu-game-truth-proof`;
- the clean-name, free-variable, binder-link and priority conventions
  stated in those sections.

This is source research and a definition/representation comparison,
not an independent review of the new rank construction being written
elsewhere.

## Retrieved source structure

B&S first annotates states with subformulas. Its Boolean annotation
conditions are biconditionals; modal and fixed-point conditions are
forward obligations. This is called a quasi-model. A pre-model adds
one function selecting a disjunct or diamond witness at each annotated
state/formula pair. Dependencies use those selections, both conjuncts,
and every box successor. A trail is maximal; every infinite trail
must have a nu-variable as its outermost recurring variable.

Theorem 3.1 states truth of annotated formulas in a well-founded
pre-model. Theorem 3.2 supplies a witnessing annotation and choice
function from truth. Section 3.6 does not assume guardedness; its
signature discussion explicitly fixes a valuation and positive-normal
formula. Do not import the later JW guarded-ANF restriction here.

## Explicit local contract for an occurrence-based host formulation

Fix a positive-normal formula `phi`, a model
`T=(S,(R_a),V_Prop)`, and a valuation `eta` of genuinely free
variables. Bound names are pairwise distinct and disjoint from free
names. Let `O_phi` be the finite set of original syntax occurrences,
each variable occurrence retaining its original binder link. An
annotation is a set

\[
 A\subseteq S\times O_\varphi.
\]

For a root witness require `(s_*,phi) in A`. Each annotated position
obeys the following forward conditions. This is a supplied precise
contract corresponding to the existing occurrence game.

| Annotated occurrence at `s` | Required annotation and dependency edges |
|---|---|
| `alpha and beta` | Both `(s,alpha)` and `(s,beta)`; retain both edges. |
| `alpha or beta` | Select one annotated child by the fixed choice function; retain its edge. |
| `<a>alpha` | Select one actual `a`-successor `t` with `(t,alpha)` annotated; retain that edge. |
| `[a]alpha` | Annotate `(t,alpha)` for every actual `a`-successor; retain every such edge. |
| `sigma X.alpha` | Annotate `(s,alpha)` and retain the forced body edge. |
| Bound `X` | Retain the original binder/body continuation described below. |
| Proposition literal, constant, or genuinely free variable | Check its terminal truth under `V_Prop` or `eta`; there is no dependency continuation. |

A diamond annotation at an action dead end violates its witness
condition. An empty box has no dependency successors and is a true
finite terminal. All required box successors remain, regardless of
their number. There is no finite-branching assumption.

The B&S source makes a direct edge from a bound variable to its
binding body. The current game instead makes

\[
 (s,X)\longrightarrow(s,\sigma X.\alpha)
                       \longrightarrow(s,\alpha).
\]

Either convention is usable, but a host must specify which one is
meant. The latter adds a forced administrative subdivision. It
preserves infinite recurring variable sequences and finite terminal
outcomes; the binder node has only the larger default priority.
It also requires annotating the intermediate binder occurrence.

The table uses forward closure, sufficient for the dependency/game
witness. It does **not** transcribe the source's Boolean
biconditionals. If the host uses this weaker local convention, name
and prove that formulation rather than silently claiming all source
local clauses were copied literally. A witness obtained by retaining
only positions reachable under one strategy naturally has forward
closure without necessarily satisfying the converse annotation
implications.

## Terminal and valuation details that cannot be left implicit

The source's short list on p. 10 does not explicitly list literal or
free-variable terminal checks. They are necessary. Take a one-state
model where `P` is false and annotate only `P`. All displayed
constructor obligations are vacuous and there is no infinite trail,
yet the annotation is not true. Merely excluding a simultaneous
`P,not P` clash is insufficient; annotation must respect the given
model's actual valuation.

For a genuinely free `Z`, the correct terminal requirement is

\[
 (s,Z)\in A\quad\Longrightarrow\quad s\in\eta(Z).
\]

The environment remains fixed for the theorem. A variable bound in
the original `phi` is not such a terminal, even if its raw occurrence
or raw subformula is open when inspected in isolation.

Likewise, the phrase "an annotated subformula is true" needs its
original binding context. It must not mean evaluating every raw
subformula under an arbitrary `eta` for variables bound in `phi`.
One option is to close those outer bound parameters by their original
binding formulas in hygienic outer-parameter order. Another is to
state the occurrence version directly as winningness at annotated
positions of the original binder-linked game, using the game theorem
for the root. The host must identify its intended interpretation.

B&S's later constant semantics makes this context explicit: bound
fixed-point parameters are replaced by their associated fixed-point
constants, while genuinely free variables retain the given valuation.
For a closed root formula there are no genuine free parameters, but
its interior raw occurrences still require the binder links.

Theorem 3.2's intended witness also contains the original assertion
`s_*@phi`. Make this root condition explicit; without it an empty
annotation would satisfy a vacuous existence statement.

## One coherent choice function, not independently selected trails

The function is selected **once** for the pre-model. In occurrence
notation it chooses a legal successor for every annotated existential
position `(s,o)`. The resulting graph keeps that selected edge and
all universal edges. Well-foundedness quantifies over every maximal
trail in this single graph, not one favored trail, and not a new
choice of function separately for each trail.

Here is a supplied counterexample to mixing locally available winning
strategies. Let

\[
 \varphi=\mu X.(P\lor\langle a\rangle X)
\]

and take two states `s,t`, both satisfying `P`, with edges
`s -a-> t -a-> s`.

- The strategy that stops at `s` and continues at `t` wins from both
  starting states.
- The strategy that continues at `s` and stops at `t` also wins from
  both starting states.
- Combining their continuing choices produces an infinite trail
  through `X` and loses.

Thus "every current obligation has some winning strategy" does not
justify the union of those strategies, even if every selected move
lands in the winning region. A single positional winning strategy,
or an explicit coherent strategy-memory construction, is required.
The current game's definition already quantifies over every maximal
play following one strategy and is suitable for this purpose.

Occurrence tags also matter for bookkeeping. Use `f(s,o)` for the
actual host game; do not identify two printed formulas merely because
their strings agree unless their binder context and choice sharing
have been justified.

## Trails, priorities and the meaning of well-founded

The source's adjective does not mean that the dependency graph has
no infinite paths. A nu-only infinite trail is permitted. A finite
maximal trail must end in an allowed true terminal; an infinite one
must satisfy the stated recurring-variable condition.

The current priorities are

\[
 \Omega(s,X)=
 \begin{cases}
  2d_X+1,&X\text{ mu-bound},\\
  2d_X,&X\text{ nu-bound},
 \end{cases}
\]

where `d_X` counts proper enclosing binders; all other nonterminals
have priority `2b+2`. This is compatible with B&S's outermost-recurring
criterion. Every infinite dependency path has a recurring variable:
without returns, each move descends finite syntax. Recurrent
incomparable binder subtrees require recurrent returns through a
farther enclosing variable, giving an outermost recurring binder.
Its priority is lower than all properly inner priorities. Forced
binder subdivisions cannot affect the least recurring priority.

The source uses state/subformula pairs in its prose, while the host
uses clean syntax occurrences. Retaining occurrences and original
binder links is a precise representation refinement; it is not an
assumption that expanded formulas have freshly independent meanings.

## Retrieved signature mathematics and its omitted bookkeeping

On p. 11, B&S orders the mu-variables `Y_1,...,Y_n` compatibly with
binder inclusion, outer before inner, and uses ordinal signatures

\[
\sigma=(\alpha_1,\ldots,\alpha_n).
\]

When there is no mu-binder, this is the empty tuple and there are no
mu-descent constraints. Infinite nu-only trails are still permitted;
terminal truth and the other local obligations do not disappear.

Introduce constants `U_i` for mu-variables and `V_j` for nu-variables.
With outside bound parameters replaced by their corresponding
constants, its displays have the form

\[
 \llbracket U_i\rrbracket_\sigma
     =\llbracket\mu Y_i^{\alpha_i}.\psi_i'\rrbracket_\sigma,
 \qquad
 \llbracket V_j\rrbracket_\sigma
     =\llbracket\nu Z_j.\chi_j'\rrbracket_\sigma.
\]

Only variables free in the **binding formula** are replaced in its
body at this stage, not that formula's own bound variable. This
prevents turning the definition into an unexplained self-reference.
For a raw subformula `psi`, its free original fixed-point parameters
are replaced by these constants to define `s |=_sigma psi`; genuinely
free root parameters still use the fixed valuation.

The printed comparison clauses use lexicographic order: signatures
are unchanged or decrease along Boolean, modal and nu-variable
dependencies; at a mu-variable `Y_i`, component `i` strictly
decreases and the earlier components are unchanged. The source does
not there spell out the binder-entry cases, the scope of resets, or
all prefix comparisons needed to formalize the construction. Treat
this as the source's description, not a complete independently
verified rank-certificate definition.

In particular, imposing global nonincrease of a mu-only signature
on **every** dependency edge would be too strong. Consider

\[
 \nu Z.\mu Y.((P\land\langle a\rangle Z)
                         \lor\langle a\rangle Y)
\]

on a two-state `a`-cycle with `P` false at `s` and true at `t`.
A winning continuing play goes from `s` through a `Y` return at `t`,
then through the outer `Z` return at `s`, and repeats. `Y` is
regenerated infinitely, but the outermost recurring variable is the
nu-variable `Z`. A certificate that strictly decreases the only
mu-coordinate at every `Y` return must allow its reinitialization
when the outer cycle re-enters that mu-binder. This is why the
omitted binder/prefix bookkeeping cannot be filled by a universal
global-nonincreasing rule.

The source's proof discussion follows a false annotation through a
chosen disjunct, a false conjunct, a selected diamond witness, or a
false box successor; uses strict descent at mu-regeneration; and
introduces decreasing greatest-fixed-point approximants when a
nu-annotation is false. It then sketches obtaining signatures from
well-founded trails, and conversely annotating truth with least
signatures and selecting least-signature successors. The explicit
local contract must provide the base cases and coherent choices for
this argument.

## Approximant indexing warning

B&S Section 3.4, printed p. 9, distinguishes `alpha` from `<alpha`:

\[
 \mu X^{<0}.\psi=\bot,\qquad
 \nu X^{<0}.\psi=\top,
\]

while the displayed `alpha`-approximant applies the body to the
`<alpha` approximation. Consequently its plain `0`-approximant is
the body at bottom/top, not bottom/top itself. The source explicitly
contrasts this with the more usual transfinite convention.

On p. 12, the falsehood argument refers informally to reaching a
false "zeroth greatest approximant". A literal reconstruction must
use `<0` there, or first announce the standard shifted convention.
The host's current evaluation-game proof already uses standard
approximants `A_0=empty`, `A_(alpha+1)=F(A_alpha)` and limit unions.
New signature equations should align with that convention explicitly
rather than silently importing source superscripts.

## Handoff boundary

Only this source note was written. No manuscript, previous note,
code, tests, builds, renders or additional agents were changed or
created. The endpoint/valuation/choice clarifications and examples
above are supplied checks. No claim of independent completion of
the signature rank construction is made.
