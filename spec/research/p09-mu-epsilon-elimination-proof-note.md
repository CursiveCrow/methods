# Parity-aware elimination of local syntax moves

Date: 2026-09-06. Status: a complete mathematical construction and strategy
proof, conditional only on the evaluation-game truth theorem and positional
determinacy already proved in the current manuscript. This note is not a
software test, a manuscript build, an independent review admission, or an
optimal translation-size claim.

## Source boundary and purpose

Bradfield and Stirling's acquired preprint, Section 5.3, defines transition
formulas using constants, conjunction, disjunction, and atoms of the form
`<a>q` and `[a]q`. In particular, a bare state `q` is not a transition atom.
Theorem 5.2 states the two expressive-equivalence directions without providing
the epsilon-elimination argument below. The repository manuscript supplies
the evaluation game and its positional truth theorem in the paragraphs
labelled `sec:p09-mu-evaluation-game`, `sec:p09-mu-game-truth-proof`, and
`sec:p09-parity-positional-proof`.

Primary source: [Bradfield--Stirling, *Modal Mu-Calculi*, acquired preprint,
Section 5.3 and Theorem 5.2](https://www.pure.ed.ac.uk/ws/files/16483207/Modal_Mu_Calculi.pdf).
The following detailed construction is a reconstruction proved here; it is
not represented as a transcription or as the source's own detailed proof.
It proves the closed-formula-to-modal-automaton direction, not the reverse
translation or automaton-normal-form theorem.

## 1. Fixed input, controls, and conventions

Fix a finite, closed, positive-normal-form formula `phi`, with all bound
variables renamed distinctly. Let `C` be its finite set of raw subformula
**occurrences**, retaining binder links. An occurrence of a bound variable
has a forced move to its unique binding-formula occurrence, and a binder has
a forced move to its body. Boolean moves and modal moves are exactly those
of the manuscript's evaluation game. Literals and constants are terminals.
There are no free-variable terminals because the input is closed.

Let `b` be the number of binders. At every occurrence of the variable `X`,
whose binding formula has `d_X` proper enclosing binders, put

\[
 \omega(X)=
 \begin{cases}
  2d_X+1,&X\text{ is a }\mu\text{-variable},\\
  2d_X,&X\text{ is a }\nu\text{-variable}.
 \end{cases}
\]

Set `D=2b+2` and assign `omega(c)=D` to every other control `c`.
Assigning it to terminal controls is just a harmless notational extension.
Write `K=omega(C)`; thus `D` belongs to `K`, `K` is finite, and every variable
priority is smaller than `D`. Infinite plays are winning for Exists when
the least priority recurring infinitely often is even. A finite terminal
play is decided by its specified terminal rule, not by the priorities in
its finite prefix.

Let `P` be the finite set of proposition constants actually used by `phi`,
excluding the Boolean constants. An input letter is `A` in `2^P`. It decides
all literal terminals: `p` is true exactly when `p` belongs to `A`, and
`not p` exactly when it does not. The Boolean constants have their fixed
truth values. The model may have arbitrary set-sized state and successor
sets; no totality or finite-branching hypothesis is used below.

Let `M` be the set of modal occurrences in `C`. If `m` is a modal occurrence,
write `body(m)` for its immediate subformula occurrence. Define the finite
set of colored ports

\[
 H=M\times K.
\]

The port remembers the occurrence `m`, not merely its printed formula.
In particular, distinct occurrences with the same printed text remain
distinct ports. This convention also identifies the appropriate body and
binder links without ambiguity.

## 2. The finite local games

For `A` in `2^P` and `U` a subset of `H`, define the finite game `L(A,U)`.
Its vertices are pairs `(c,k)` in `C x K`. The intended register `k` is
the minimum of the priorities already read in the current local episode,
including the current control `c`.

- At a Boolean control, preserve its usual choice owner. An edge from `c`
  to the chosen child `c'` becomes an edge from `(c,k)` to
  `(c',min(k,omega(c')))`. Binder and bound-variable moves obey the same
  update and remain forced.
- At a literal or Boolean constant, stop with the truth value fixed by `A`.
- At a modal control `m`, stop **before taking a model edge**. This terminal
  is won by Exists exactly when the port `(m,k)` belongs to `U`.
- On an infinite local play `(c_0,k_0),(c_1,k_1),...`, use the priorities
  `omega(c_0),omega(c_1),...`. Do **not** use `k_0,k_1,...` as the local
  parity priorities.

For a starting control `psi`, initialize the register to `D` and then read
that control's priority. Thus its actual starting vertex is

\[
 \iota(\psi)=(\psi,\min(D,\omega(\psi)))
             =(\psi,\omega(\psi)).
\]

This convention includes the start control in the first block minimum.
Equivalently one may add a priority-neutral initial bookkeeping move, but
one must not start at `(psi,D)` and forget to read `omega(psi)`.
Unreachable pairs with an inconsistent register do not affect a game
started at `iota(psi)`.

The game is finite, independently of the model, since only the current
letter `A` is used. Terminal outcomes may be totalized with absorbing even
and odd sinks. Define

\[
 f_{\psi,A}(U)=1
 \quad\Longleftrightarrow\quad
 \exists\text{ has a winning strategy in }L(A,U)
                \text{ from }\iota(\psi).
\]

This is a finite, effective definition. Positional determinacy supplies a
positional witness whenever its value is one. No assertion about acceptance
at successor model states is used to define `f`.

### Monotonicity and the exact positive formula

If `U` is contained in `V`, an Exists strategy winning for `U` is still
winning for `V`: the only changes make additional modal terminals winning;
all other terminals, edges, owners, and infinite-play priorities are
unchanged. Therefore `f_{psi,A}` is monotone.

Introduce a Boolean variable `z_h` for each `h` in `H`, and put

\[
 B_{\psi,A}(z)=
 \bigvee_{\substack{U\subseteq H\\f_{\psi,A}(U)=1}}
     \ \bigwedge_{h\in U}z_h.
\]

The empty disjunction is false and the empty conjunction true. Keep the
summands indexed by their supports `U`, and their atom occurrences indexed
by `h`; no quotient by identical printed modal formulas is required.

For a truth set `V` of the variables `z_h`, this formula is true exactly
when `f_{psi,A}(V)=1`. If the formula is true, a displayed winning support
`U` is contained in `V`, and monotonicity gives `f(V)=1`. Conversely, if
`f(V)=1`, the summand indexed by `V` is true. This proves equality with the
Boolean truth table, including the cases `H` empty and `f` constant.

Using every winning support, rather than only the minimal supports, makes
the later exact-support proof immediate. Restricting to minimal supports
would be a valid optional simplification, not a needed assumption.

## 3. The genuinely guarded automaton

Define the finite state set, priority map, and initial state by

\[
 Q=C\times K,\qquad
 \Omega_Q(\psi,j)=j,\qquad
 q_I=(\varphi,D).
\]

For a port `h=(m,k)`, substitute the following one-step modal atom:

\[
 \rho(m,k)=
 \begin{cases}
  \langle a\rangle(\chi,k),&m=\langle a\rangle\chi,\\
  [a](\chi,k),&m=[a]\chi.
 \end{cases}
\]

Set

\[
 \delta((\psi,j),A)=B_{\psi,A}[\rho(h)/z_h:h\in H].
\]

Every state occurrence in this transition is under exactly one modality.
Its modal depth is at most one; only positive Boolean operations and
constants occur. Thus its syntax is precisely the guarded transition
language at issue, not an epsilon-enriched variant.

The transition is independent of the incoming color `j`. This is
intentional: `j` records the minimum of the **preceding** completed local
episode. It contributes the one current automaton-state priority only.
The next local episode resets to `D` and reads `omega(psi)` afresh. In
particular, the running minimum is never carried cumulatively across model
steps.

Use the standard acceptance game for these transitions. At `(s,q)`, emit
the priority `Omega_Q(q)` and evaluate `delta(q,A_s)`: Exists chooses at
disjunctions, Forall at conjunctions, and at a modal atom the modal owner
chooses an appropriately labelled successor and reaches the indicated
state. True and false stop with their fixed outcomes; a dead diamond loses
and a dead box wins for Exists. Only state priorities need be recorded.
Equivalently, every intervening transition-syntax vertex can have priority
`D`: each transition formula has finite syntax and no bare-state atoms,
so every infinite acceptance play visits automaton states infinitely often,
and additional copies of the greatest priority `D` do not change its least
recurring priority.

## 4. The block-minimum lemma

Let an infinite sequence over a finite ordered priority set be partitioned
into infinitely many finite, nonempty consecutive blocks. Let `k_i` be the
minimum in block `i`. Then

\[
 \min\operatorname{Inf}(\text{original sequence})
 =\min\operatorname{Inf}(k_0,k_1,\ldots).
\]

Proof. Let the left side be `r`. Every priority smaller than `r` occurs
only finitely often, and there are only finitely many priorities. Thus
only finitely many positions, and hence only finitely many blocks, contain
a priority smaller than `r`. The priority `r` occurs in infinitely many
blocks: finitely many finite blocks could contain only finitely many of
its occurrences. After the finitely many exceptional blocks, every block
containing `r` has minimum exactly `r`. Hence `r` occurs infinitely often
as a block minimum, and no smaller value does. This proves the identity.

There is no uniform bound on block lengths in this argument.

For an evaluation play with infinitely many modal moves, take each block
from the starting control of an episode through and including its ending
modal control, but not the target body reached by the modal move. The
target body starts the next block. These blocks partition its controls;
they are finite and nonempty. If their minima are `k_0,k_1,...`, the
corresponding automaton-state colors are

\[
 D,k_0,k_1,k_2,\ldots.
\]

The initial `D` is a finite prefix, so the two infinite plays have the same
least recurring priority and the same winner.

## 5. Evaluation winner implies automaton winner

Fix a model and start `s_*`. Suppose Exists wins the evaluation game from
`(s_*,phi)`. By the manuscript's positional theorem, choose a positional
winning strategy `sigma`. A position reachable from the start by a finite
`sigma`-compatible history also has `sigma` as a winning continuation:
otherwise a losing continuation could be prefixed by that finite history,
contradicting that `sigma` wins. Finite prefixes change neither terminal
outcomes nor the parity of infinite plays.

Consider any such reachable `(s,psi)`. Restrict `sigma` to the local Boolean
choices at the fixed model state `s`, and lift those choices to the local
register game. Let `U_{s,psi}` be **exactly** the set of ports `(m,k)` reached
by finite local paths from `iota(psi)` compatible with this restriction.
These paths stop at their first modal control; Forall remains free at all
conjunctions. The set is finite because `H` is finite, even if infinitely
many finite local paths realize its elements.

This restricted strategy wins `L(A_s,U_{s,psi})` from `iota(psi)`:

1. Every reached literal or constant must be true; otherwise its local
   path, prefixed by a witnessing history to `(s,psi)`, loses against
   `sigma` in the evaluation game.
2. Every reached modal terminal belongs to `U_{s,psi}` by definition.
3. Every infinite local play projects to an infinite evaluation play at
   state `s` compatible with `sigma`. It is winning with the actual control
   priorities, which are precisely those used in the local game.

Thus `f_{psi,A_s}(U_{s,psi})=1`. In the automaton, choose the summand indexed
by `U_{s,psi}`. If it is empty, the transition is true and wins immediately.
Otherwise Forall can select any one of its indexed port atoms `(m,k)`.
By the definition of this exact support, choose a finite local witness
path to that port compatible with `sigma`.

If `m` is a diamond, follow the successor selected by `sigma` at `(s,m)`.
Such a successor exists: reaching a dead diamond would contradict the
winning continuation of `sigma`. If `m` is a box, allow Forall any model
successor. A dead box terminates with the correct winning outcome. In each
continuing case, the target `(t,body(m))` is evaluation-reachable under
`sigma`: concatenate the witness local path and this modal move with the
previous witnessing history. Repeat the construction from that target.

Positionality is what makes all these concatenations compatible with the
same `sigma`; neither the chosen local witness nor a different earlier
history can change its prescribed choice at an evaluation position.

This defines a winning automaton strategy. A finite compatible acceptance
play cannot end falsely: the chosen support is a summand, the conjunction
can expose only one of its ports, every chosen diamond has its selected
successor, and any dead box wins. An infinite compatible acceptance play
has infinitely many modal steps. Choose a finite realizing witness for
each of its selected ports and concatenate these witnesses and the actual
modal steps. The result is an infinite `sigma`-compatible evaluation play.
Each completed block has the color recorded at the next automaton state.
The block-minimum lemma therefore makes the acceptance play winning.

Notice that accepting local divergences are not required to become
automaton branches. They justify the truth of the chosen local summary.
Every infinite branch that the summary does expose still has the
realization just proved.

## 6. Automaton winner implies evaluation winner

Conversely, suppose Exists has a winning acceptance-game strategy `tau`
from `(s_*,(phi,D))`. Positionality of `tau` is not needed. We construct an
evaluation strategy with finite-history memory sufficient to maintain one
virtual `tau`-compatible acceptance-game history.

At the start of an evaluation episode at `(s,psi)`, the virtual history
ends at the matching automaton state `(s,(psi,j))`. Follow `tau` through
the disjunction selecting a summand of `B_{psi,A_s}`. It selects a support
`U` with `f_{psi,A_s}(U)=1`. Indeed, every non-false summand is indexed by
such a support by construction, and a winning strategy cannot reach a
false transition. Binary association of the displayed finite disjunction
only expands this into finitely many virtual choices.

Choose a winning strategy `lambda` for `L(A_s,U)` from `iota(psi)`.
One can fix a positional local witness in advance for each finite triple
`(psi,A,U)` with `f=1`. Run that strategy along the actual episode, updating
the local register from `D` and reading each control priority as specified.
Actual choices by Forall at conjunctions are simply its opponent moves in
this local game. Forced moves agree in both games.

There are three possible behaviors of the resulting episode.

1. **A literal or constant is reached.** Since `lambda` is winning, the
   terminal is true. The actual evaluation play wins. The virtual play need
   not be continued after the actual game has already ended.
2. **The episode is infinite without reaching a modality.** It is a
   `lambda`-compatible infinite local play, so the least actual control
   priority recurring in it is even. The preceding evaluation history is
   finite; consequently the complete evaluation play wins as well. The
   possibly stabilized register does not decide this case.
3. **The episode reaches a modal port `(m,k)`.** Since `lambda` is winning,
   this port is in `U`. In the virtual acceptance history let Forall select
   its indexed conjunct. Each conjunct of a nonempty finite conjunction
   can be selected by an appropriate finite sequence of binary Forall
   choices. At a diamond, follow the successor prescribed by `tau` at this
   virtual modal position. It exists, since a dead diamond would be a
   losing continuation of `tau`. At a box, use the actual successor chosen
   by Forall as its virtual choice. If there is none, both games give the
   correct immediate Exists win. Otherwise both histories now reach
   `(t,body(m))` and `(t,(body(m),k))` respectively. Start the next episode
   with a reset register and the extended virtual history.

For an empty support, case 3 is impossible: every modal terminal is losing
in `L(A_s,empty)`, and the winning `lambda` cannot reach one. An empty-support
transition may therefore be represented by true even when its actual
evaluation realization continues forever locally; case 2 proves that such
a continuation is harmless.

These instructions define an evaluation strategy on every history reachable
under it; extend it arbitrarily on irrelevant histories. Local choices and
virtual histories are allowed to depend on the finite actual history.

To verify it, take any maximal compatible evaluation play. If it terminates,
the cases above prove its terminal winning. If it has only finitely many
modal moves but is infinite, its last episode falls under case 2 and wins.
If it has infinitely many modal moves, every episode is finite and the
maintained virtual history forms one infinite play compatible with `tau`.
It wins by assumption. Its state colors are the initial `D` followed by the
successive local block minima, so the block-minimum lemma proves that the
actual evaluation play has the same winning parity.

Therefore the constructed strategy is winning in all cases. Crucially,
this proof never assumes that a port is true precisely when its successor
is already known to be accepted: the support comes from a concrete chosen
automaton summand, and its independent local winning strategy is then
concatenated with the concrete acceptance-game strategy.

Combining both directions with the proved truth/game equivalence yields

\[
 M,s\models\varphi
 \quad\Longleftrightarrow\quad
 \exists\text{ wins the acceptance game of the constructed automaton
 at }(s,(\varphi,D)).
\]

When automaton acceptance is defined by runs instead, apply the separately
proved run/acceptance-game equivalence. For arbitrary set-sized branching,
the run's branching index sets must be allowed to be set-sized too; an
indexing by finite sequences of natural numbers alone only supplies
countably branching runs. The strategy proof here has no such restriction.

## 7. Why the two minimum conventions cannot be confused

The finite register summarizes one **completed** episode. It is not a
substitute for the parity condition on an episode that never ends.

For example, consider

\[
 \mu X.\bigl(X\lor\nu Y.Y\bigr).
\]

There are local plays that choose `X` once, return to the outer binder,
then choose `nu Y.Y` and remain in its `Y` loop forever. Their actual
priorities eventually recur only at the even `Y` priority (and `D`), so
they win. Their cumulative local minimum retains the one earlier odd
`X` priority forever and would incorrectly make this very play losing.
The fact that another winning local strategy may avoid `X` does not repair
this incorrect playwise priority assignment.

Likewise, carrying a minimum from one modal episode into every later
episode would turn a finite low-priority prefix into an infinitely
recurring color. The incoming component `j` must therefore be emitted once
and then discarded for purposes of computing the next block minimum.

The two modal dead-end cases are external to `L(A,U)`: a local game stops
before inspecting any successor. After substitution, ordinary modal
acceptance makes a dead diamond false and a dead box true. Neither is
silently treated as a local accepting divergence or as a parity decision.

## 8. Explicit finite bounds and effectiveness

Put `n=|C|`, `h=|K|`, `m=|M|`, `r=|H|=mh`, and `p=|P|`.
Then `h <= b+1 <= n+1`, `m <= n`, and `p <= n`. The construction uses:

- exactly `nh` automaton states before removing unreachable copies;
- at most `nh` vertices in each local game before optional terminal
  totalization, which adds at most two shared absorbing vertices;
- at most `2^r` summands in each `B_{psi,A}`, with at most `r` port atoms
  in each summand;
- transition-formula size `O((r+1)2^r)` using ordinary binary connectives
  and constants;
- at most `O(nh 2^p (r+1)2^r)` symbols in a fully expanded transition
  table, ignoring only the usual logarithmic encoding cost of state names.

The transitions for different incoming `j` are identical and can be shared,
but the bound does not require sharing. These estimates give polynomially
many states and a crude `2^{O(n^2)}` explicit table-size bound with usual
finite encodings. They make no claim about optimality, optimal priorities,
the best known translation, or the complexity of satisfiability.

For each of the finitely many pairs `(A,U)`, solving the one finite local
game gives the values for every starting `psi`; thus at most `2^{p+r}`
finite game instances suffice. Effectiveness does not require importing
an efficient parity-game algorithm. Enumerate its finitely many positional
Exists strategies. For a fixed strategy and start, inspect the reachable
terminals and directed simple cycles in the graph retaining all Forall
choices. The strategy wins exactly when every reachable terminal is winning
and every reachable directed simple cycle has even minimum priority.

For that last finite criterion, a reachable odd-minimum cycle can be repeated
by the opponent. Conversely, if an infinite compatible path has odd least
recurring priority `d`, discard its finite prefix containing priorities
less than `d` and choose a recurrent vertex of priority `d`. A return to it
within this tail contains a simple cycle through it after removing internal
repetitions; that cycle has odd minimum `d`, contrary to the criterion.
All priorities in this check are the **actual local control priorities**.
Positional determinacy ensures that a winning start has a strategy found
by this finite enumeration. This proves the claimed effective construction
without a circular acceptance oracle or a uniform episode-length bound.
