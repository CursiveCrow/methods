# Positional determinacy on arbitrary set-sized parity arenas

## Purpose, sources, and standing

This note supplies a complete attractor proof for a possibly infinite,
infinitely branching, total turn-based arena with finitely many priorities.
The conclusion is uniform: each player has one positional strategy winning
from every vertex in that player's winning region.

The source conventions relevant to N-c-018 are different. Emerson--Jutla,
Definition 4.0, uses the largest infinitely recurring color; its Section 4.2,
Theorem 4.4, proves a history-free-strategy result by ordinal ranks on game
trees. [Emerson--Jutla (1991), Section 4, PDF pages 7--9](https://www.cs.cornell.edu/courses/cs6860/2021sp/Handouts/EmersonJutla91.pdf)
Bradfield--Stirling's accessible preprint, dated 15 November 2005, uses the
least infinitely recurring priority. Section 4.4 states the model-checking
game theorem as Theorem 4.6, then discusses graph parity games obtained from
finite structures. [Bradfield--Stirling, 2005 preprint, Section 4.4, printed pages 15--16](https://www.pure.ed.ac.uk/ws/files/16483207/Modal_Mu_Calculi.pdf)

The proof below is an independent, fully specified reconstruction. It is not
claimed to be either source's printed proof or to extend the literal scope
of a source passage by attribution. In particular, the arbitrary-arena
claim is proved here, not inferred from Bradfield--Stirling's finite-graph
discussion. This is a mathematical proof-development note, not independent
review, manuscript incorporation, a build, visual verification, or topic
acceptance.

## 1. Arena, plays, and the strengthened theorem

Work in ZFC. Choice is used for successor selections and for the inductive
strategy data. All arenas are sets; the ordinal constructions below are
bounded by a set ordinal. No countability or finite-branching hypothesis is
made.

An arena is

\[
G=(V,V_0,V_1,E,c),\qquad V=V_0\mathbin{\dot\cup}V_1,
\qquad E\subseteq V\times V,
\qquad c:V\longrightarrow\{0,\ldots,d\},
\]

where \(d\in\mathbb N\) and
\(E(v)=\{w\in V:(v,w)\in E\}\ne\varnothing\) for every \(v\in V\).
The empty arena is permitted. At a vertex in \(V_i\), player \(i\) chooses
the successor. A play is an infinite sequence \(v_0v_1\ldots\) with
\(v_{n+1}\in E(v_n)\) for all \(n\in\mathbb N\). Put

\[
\operatorname{Inf}_c(v_0v_1\ldots)
 =\{j\le d:\{n:c(v_n)=j\}\text{ is infinite}\}.
\]

Because there are finitely many priorities, this set is nonempty. Player
\(i\in\{0,1\}\) wins the play iff

\[
\max\operatorname{Inf}_c(v_0v_1\ldots)\equiv i\pmod2.
\]

Priorities, not vertices, recur in this definition: a play through infinitely
many distinct vertices still has a winner. Removing or adding a finite play
prefix does not change the winner.

For \(U\subseteq V\), write \(G[U]\) for the induced arena, with
\(E_U(v)=E(v)\cap U\) and the inherited ownership and priorities. It is a
total subarena exactly when every \(v\in U\) has \(E_U(v)\ne\varnothing\).

A **positional \(i\)-dominion** consists of a set \(D\subseteq V\) and a
function \(\sigma:D\cap V_i\to D\) such that:

1. \(\sigma(v)\in E(v)\) for every \(v\in D\cap V_i\);
2. \(E(v)\subseteq D\) for every \(v\in D\cap V_{1-i}\); and
3. every play starting in \(D\) and satisfying
   \(v_{n+1}=\sigma(v_n)\) whenever \(v_n\in V_i\) is won by \(i\).

The first two clauses make the region invariant against every opponent
choice. The third quantifies over all starting vertices in the region and
all opponent behaviors, including history-dependent ones.

**Theorem.** Every arena above admits a partition
\(V=D_0\mathbin{\dot\cup}D_1\) into positional dominions for players 0 and
1, respectively. Thus each player has a single positional strategy winning
simultaneously from all of its winning vertices.

We prove the stronger dominion statement by induction on \(d\).

## 2. Transfinite attractors

Let \(G[U]\) be a total subarena, let \(X\subseteq U\), and let
\(i\in\{0,1\}\). Define the attractor approximants in this subarena by

\[
\begin{aligned}
B_0&=X,\\
B_{\xi+1}&=B_\xi
 \cup\{v\in U\cap V_i:E_U(v)\cap B_\xi\ne\varnothing\}\\
&\hspace{2.8em}\cup
 \{v\in U\cap V_{1-i}:E_U(v)\subseteq B_\xi\},\\
B_\lambda&=\bigcup_{\xi<\lambda}B_\xi
 \quad(\lambda\text{ a nonzero limit ordinal}).
\end{aligned}
\]

This increasing sequence stabilizes. For a precise bound, let \(\kappa\)
be an ordinal with no injection into \(U\), for example the initial ordinal
of the successor cardinal of \(|U|\). If every successor step indexed by
\(\xi<\kappa\) were strict, choosing one vertex in
\(B_{\xi+1}\setminus B_\xi\) would give an injection \(\kappa\to U\):
these differences are pairwise disjoint. Thus
\(B_{\zeta+1}=B_\zeta\) for some \(\zeta<\kappa\), after which all
approximants agree. Define

\[
\operatorname{Attr}_i^{G[U]}(X)=B_\zeta.
\]

The attractor is the least superset of \(X\) closed under the two
predecessor clauses. Indeed, transfinite induction puts every approximant
inside any such closed superset, and the stabilized approximant itself is
closed. Consequently the attractor operation is monotone and idempotent.
Totality also gives \(\operatorname{Attr}_i^{G[U]}(\varnothing)=\varnothing\).

For \(v\) in the attractor, let

\[
r_X(v)=\min\{\xi\le\zeta:v\in B_\xi\}.
\]

It is zero exactly on \(X\). Every positive entry rank is a successor
\(\eta+1\), because a limit approximant is a union. If
\(r_X(v)=\eta+1\), then:

- at an \(i\)-owned vertex, some successor lies in \(B_\eta\);
- at a \((1-i)\)-owned vertex, every successor in \(G[U]\) lies in
  \(B_\eta\).

Fix once and for all a successor of smaller rank at each \(i\)-owned
vertex outside \(X\). This is a positional attraction rule. While a play
following it remains outside \(X\), its ranks strictly decrease at every
step, whatever the opponent does. There is no infinite strictly decreasing
sequence of ordinals, so the play reaches \(X\) after finitely many moves,
remaining in the attractor until then. No uniform finite bound on that
number of moves is asserted.

Two complementary closure facts will be used repeatedly. If
\(A=\operatorname{Attr}_i^{G[U]}(X)\) and \(v\in U\setminus A\), then

\[
\begin{array}{ll}
v\in V_i &\Longrightarrow E_U(v)\subseteq U\setminus A,\\
v\in V_{1-i}&\Longrightarrow E_U(v)\cap(U\setminus A)\ne\varnothing.
\end{array}
\tag{1}
\]

Otherwise the appropriate predecessor clause would put \(v\) in the
closed set \(A\). In the first line the successor set is nonempty because
\(G[U]\) is total. Hence \(G[U\setminus A]\) is total. The same conclusion
holds whenever \(A\) is attractor-closed,
\(\operatorname{Attr}_i^{G[U]}(A)=A\).

Attractor closure alone does **not** say that every vertex inside the
attractor has all its successors inside. Target vertices may have outgoing
edges to its complement. All uses of invariance below therefore verify the
target-region exits separately.

## 3. Why outer limit stages must be closed again

An increasing union of attractor-closed sets need not be attractor-closed
when the arena is infinitely branching. Let \(q\in\{0,1\}\) and
\(p=1-q\). Take a \(p\)-owned vertex \(u\), \(q\)-owned vertices
\(w_n\) for \(n\in\mathbb N\), and edges

\[
E(u)=\{w_n:n\in\mathbb N\},\qquad E(w_n)=\{w_n\}.
\]

For each \(n\), the finite prefix
\(R_n=\{w_0,\ldots,w_{n-1}\}\) is \(q\)-attractor-closed. But their union
contains every successor of \(u\), so its \(q\)-attractor also contains
\(u\). Simply removing \(\bigcup_nR_n\) would leave the dead-end arena
\(\{u\}\). Taking the attractor of the union removes \(u\) as well.

This is why the outer construction below uses
\(R_\lambda=\operatorname{Attr}_q^G(\bigcup_{\beta<\lambda}R_\beta)\)
at limit stages. The union rule for the **inner attractor approximants** in
Section 2 is still correct: their full transfinite iteration performs the
additional predecessor steps after a limit.

## 4. Induction and the outer removal construction

For \(d=0\), every infinite play has largest recurring priority 0. Take
\(D_0=V\), choose an arbitrary legal successor at each 0-owned vertex, and
take \(D_1=\varnothing\). These are the required dominions. Empty arenas
are trivial for every \(d\).

Assume \(d>0\) and the theorem for priorities in \(\{0,\ldots,d-1\}\).
Put

\[
p=d\bmod2,\qquad q=1-p.
\]

We construct increasing \(q\)-attractor-closed subsets \(R_\alpha\) of
the **original** arena \(G\). Their winning strategies will be assembled
in Section 5; no winning-region assumption is needed in order to define
the sets or their residual arenas.

Start with \(R_0=\varnothing\). Whenever \(R_\alpha\) is defined, put

\[
\begin{aligned}
H_\alpha&=V\setminus R_\alpha,\\
T_\alpha&=\{v\in H_\alpha:c(v)=d\},\\
A_\alpha&=\operatorname{Attr}_p^{G[H_\alpha]}(T_\alpha),\\
K_\alpha&=H_\alpha\setminus A_\alpha.
\end{aligned}
\tag{2}
\]

Since \(R_\alpha\) is \(q\)-attractor-closed in \(G\), (1) makes
\(G[H_\alpha]\) total. Applying (1) again makes \(G[K_\alpha]\) total.
The latter arena has no priority-\(d\) vertices, so the induction
hypothesis supplies a partition into positional \(p\)- and \(q\)-dominions.
Denote its \(q\)-dominion by \(W_\alpha\), with positional strategy
\(\tau_\alpha:W_\alpha\cap V_q\to W_\alpha\).

If \(W_\alpha=\varnothing\), stop at \(\theta=\alpha\). Otherwise put

\[
R_{\alpha+1}
 =\operatorname{Attr}_q^G(R_\alpha\cup W_\alpha).
\tag{3}
\]

At a nonzero limit stage reached before stopping, put

\[
U_\lambda=\bigcup_{\beta<\lambda}R_\beta,
\qquad
R_\lambda=\operatorname{Attr}_q^G(U_\lambda).
\tag{4}
\]

Every \(R_\alpha\) is \(q\)-attractor-closed by idempotence, including
\(R_0\) by totality. The sets increase by (3), (4), and monotonicity.
Whenever a successor step is taken, it is strict: the nonempty set
\(W_\alpha\) is contained in \(H_\alpha\), is therefore disjoint from
\(R_\alpha\), and is contained in \(R_{\alpha+1}\).

The construction stops. Let \(\kappa\) be the initial ordinal of the
successor cardinal of \(|V|\). If it did not stop at an index below
\(\kappa\), choosing \(w_\alpha\in W_\alpha\) for each
\(\alpha<\kappa\) would inject \(\kappa\) into \(V\). For
\(\alpha<\beta\),
\(w_\alpha\in R_{\alpha+1}\subseteq R_\beta\), whereas
\(w_\beta\notin R_\beta\). This contradicts the choice of \(\kappa\).
Thus a stopping index \(\theta<\kappa\) exists. This also shows that all
sets and strategy data used here belong to a set-indexed construction;
there is no proper-class union or choice of strategies.

The key exit fact for the seed \(W_\alpha\) is

\[
\begin{aligned}
v\in W_\alpha\cap V_q
 &\Longrightarrow \tau_\alpha(v)\in W_\alpha,\\
v\in W_\alpha\cap V_p
 &\Longrightarrow E(v)\subseteq R_\alpha\cup W_\alpha.
\end{aligned}
\tag{5}
\]

The first line is the inductive dominion condition. For the second, every
successor outside \(H_\alpha\) lies in \(R_\alpha\). Every successor
inside \(H_\alpha\) lies in \(K_\alpha\), because \(v\) is \(p\)-owned
and is outside the \(p\)-attractor \(A_\alpha\), by (1). Every such
\(K_\alpha\)-successor belongs to \(W_\alpha\), by the opponent-closure
clause for the inductive \(q\)-dominion. Thus a play following
\(\tau_\alpha\) inside \(W_\alpha\) can leave that seed only through an
opponent move into the already removed set \(R_\alpha\), never into
\(A_\alpha\).

## 5. One positional strategy on all removed vertices

For \(v\in R_\theta\), define its least-entry stage

\[
e(v)=\min\{\gamma\le\theta:v\in R_\gamma\}.
\tag{6}
\]

This ordinal is positive since \(R_0=\varnothing\). It may be a limit
ordinal, because (4) can add vertices not in any earlier removed set.

For each successor stage \(\gamma=\alpha+1\le\theta\), let
\(r_\gamma\) be the attractor rank in (3), with target
\(R_\alpha\cup W_\alpha\), and fix a rank-decreasing \(q\)-attraction
rule \(a_\gamma\) on the non-target vertices. For each nonzero limit
\(\lambda\le\theta\), let \(r_\lambda\) be the attractor rank in (4),
with target \(U_\lambda\), and fix its rule \(a_\lambda\).

Define \(\sigma_q\) at every \(v\in R_\theta\cap V_q\) by its unique
entry stage:

\[
\sigma_q(v)=
\begin{cases}
\tau_\alpha(v),
 &e(v)=\alpha+1\text{ and }v\in W_\alpha,\\
a_{\alpha+1}(v),
 &e(v)=\alpha+1\text{ and }v\notin W_\alpha,\\
a_\lambda(v),
 &e(v)=\lambda\text{ is a nonzero limit}.
\end{cases}
\tag{7}
\]

These rules are defined where used. In the second case,
\(v\notin R_\alpha\) by least entry and
\(v\notin W_\alpha\), so its attractor rank is positive. In the third
case, \(v\notin U_\lambda\), again by least entry, so its rank is positive.
The first case uses the inductive strategy on its stated domain. The
entry stage, seed membership, and selected edge are fixed data of the
vertex, so (7) has no dependence on the play history or starting vertex.

**Stage monotonicity.** Suppose \(v\in R_\theta\), and take any successor
\(w\in E(v)\), requiring \(w=\sigma_q(v)\) when \(v\in V_q\). Then

\[
w\in R_{e(v)},\qquad e(w)\le e(v).
\tag{8}
\]

To prove this, first suppose \(e(v)=\alpha+1\) and \(v\in W_\alpha\).
Equation (5) puts \(w\) in \(R_\alpha\cup W_\alpha\), hence in
\(R_{\alpha+1}\). In every other case, \(v\) is a non-target vertex in
the attractor belonging to its entry stage. Section 2 gives

\[
w\in R_{e(v)},\qquad r_{e(v)}(w)<r_{e(v)}(v),
\tag{9}
\]

at \(q\)-vertices by the chosen edge, and at \(p\)-vertices for every
edge in the original arena. This proves (8) and also records strict rank
descent away from the fresh seed.

In particular, (7) always selects a legal edge into \(R_\theta\), and
every opponent edge from \(R_\theta\) stays in \(R_\theta\). It remains
to prove winning, not merely invariance.

Take an arbitrary play \(v_0v_1\ldots\) starting at an arbitrary
\(v_0\in R_\theta\) and following \(\sigma_q\). Its entry stages form a
nonincreasing sequence of ordinals by (8). Such a sequence is eventually
constant: the set \(\{e(v_n):n\in\mathbb N\}\) has a least element,
which occurs at some index \(N\), and all later values must equal it.
Write this eventual stage as \(\gamma\).

If \(\gamma\) is a nonzero limit, every vertex of the tail is outside
\(U_\gamma\), for otherwise it would have a smaller entry stage.
Equation (9) therefore strictly decreases \(r_\gamma(v_n)\) at every
tail step. That is impossible for an infinite sequence of ordinals.

Consequently \(\gamma=\alpha+1\) for some \(\alpha<\theta\). As long as
the tail avoids \(W_\alpha\), (9) strictly decreases its
\(r_{\alpha+1}\)-rank. It must therefore reach \(W_\alpha\) after
finitely many more steps. Once it reaches \(W_\alpha\), equation (5)
allows only successors in \(W_\alpha\) or in \(R_\alpha\). The second
possibility would strictly lower the entry stage, which is impossible on
the constant-stage tail. Hence the play thereafter remains in
\(W_\alpha\), using \(\tau_\alpha\) at every \(q\)-owned vertex. It is
a legal play of \(G[K_\alpha]\) won by \(q\), by the induction hypothesis.
Parity is unchanged by its finite prefix, so the original play is won by
\(q\).

The start and all opponent choices were arbitrary. Thus
\((R_\theta,\sigma_q)\) is a positional \(q\)-dominion. This argument
explicitly covers newly attracted limit-stage vertices. Jumps into older
regions strictly decrease entry stages and cannot occur infinitely often;
they do not require a finite-branching compactness argument or a
history-dependent strategy switch.

## 6. One positional strategy on the final residual arena

At the stopping stage, \(W_\theta=\varnothing\). By the inductive
partition, the whole lower-priority arena \(G[K_\theta]\) is a positional
\(p\)-dominion. Write its uniform strategy as \(\tau_p\). Let \(b\) be
the positional attraction rule in

\[
A_\theta=\operatorname{Attr}_p^{G[H_\theta]}(T_\theta).
\]

Define \(\sigma_p\) on \(H_\theta\cap V_p\) as follows:

\[
\sigma_p(v)=
\begin{cases}
\tau_p(v),&v\in K_\theta,\\
b(v),&v\in A_\theta\setminus T_\theta,\\
\text{a fixed element of }E_{H_\theta}(v),&v\in T_\theta.
\end{cases}
\tag{10}
\]

Every chosen edge exists and stays in \(H_\theta\): use the inductive
strategy, the attraction rule, or totality, respectively. At a
\(q\)-owned vertex of \(H_\theta\), every original-arena successor also
lies in \(H_\theta\), because \(R_\theta\) is \(q\)-attractor-closed and
(1) applies. Thus the region is invariant under (10) against every
opponent choice.

Take any play in that region following \(\sigma_p\). If it visits
\(T_\theta\) infinitely often, priority \(d\) occurs infinitely often;
since no larger priority occurs, the play is won by \(p=d\bmod2\).

If it visits \(T_\theta\) only finitely often, choose \(N\) so that there
are no such visits at or after \(N\), taking \(N=0\) if there are none.
The play then remains in \(K_\theta\) from \(N\) onward. To justify that
assertion, every visit to
\(A_\theta\setminus T_\theta\) under (10) forces a later visit to
\(T_\theta\), by strict attraction-rank descent against all opponent
moves. Therefore a visit to \(A_\theta\) at or after \(N\) is impossible.
The remaining tail is a play of
\(G[K_\theta]\) following \(\tau_p\), and so it is won by \(p\) by
induction. Its finite prefix cannot change that winner.

This proves that \((H_\theta,\sigma_p)\) is a positional \(p\)-dominion.
Together with Section 5 and
\(V=R_\theta\mathbin{\dot\cup}H_\theta\), it completes the induction
and proves the theorem.

## 7. Winning regions, priority reversal, and terminal positions

The dominion partition gives determinacy against arbitrary strategies, not
only positional opponents. It is also the actual winning-region partition.
If a player had any winning strategy at a vertex in the other player's
dominion, play the two strategies against each other. Totality and their
specified choices generate an infinite play, and both strategies would
require it to have their different winning parities. This contradicts the
definition of the winner. Positional strategies on dominions may be
extended arbitrarily to the player's other vertices if a strategy is
required to be a function on all owned vertices.

For the least-recurring convention, suppose a finite-range priority map
\(f:V\to\mathbb N\) is given. For nonempty \(V\), choose an even integer
\(M\ge\max f(V)\) and set

\[
c(v)=M-f(v).
\]

On every infinite play,

\[
\max\operatorname{Inf}_c=M-\min\operatorname{Inf}_f,
\qquad
\max\operatorname{Inf}_c\equiv\min\operatorname{Inf}_f\pmod2.
\]

Thus the theorem applies with exactly the same winning plays and strategies
under the least-recurring-even convention. For an empty arena the choice of
\(M\) is immaterial. The evenness of \(M\) matters: reversal around an odd
integer would exchange the two players' winning parities.

If an application has designated terminal vertices with prescribed winners,
replace each terminal by a vertex with its sole self-loop and assign that
vertex priority 0 or 1 according to its prescribed winner. Ownership at
such a vertex is immaterial because there is only one available edge. The
modified arena is total; a play reaching a terminal has a constant tail
with precisely the prescribed winner. Plays not reaching terminals retain
their original priorities and winners. Restricting a winning positional
strategy back to nonterminal vertices therefore gives the corresponding
result for the original finite-or-infinite-play game. The priority range
remains finite.

## 8. Exact boundary of what this note establishes

The proof establishes positional determinacy, including uniform positional
winning strategies, for all set-sized total turn-based parity arenas with a
finite priority range, with arbitrary branching. Its only well-foundedness
arguments use actual ordinal entry stages and actual ordinal attractor
ranks. The outer construction closes the removed union again at every
limit, so residual totality is proved and not smuggled in through an
unstated finite-branching assumption.

It does not prove the model-checking game truth lemma, the syntax-to-priority
assignment, an automaton translation, or a complexity bound for finite parity
games. Those are separate claims. No manuscript files were edited, and no
software tests, manuscript builds, or manuscript renders were performed for
this note.

## Subsequent independent review and incorporation

A separate mathematical reader checked the full proof and reported no
defects under the stated ZFC, set-sized, total-arena and finite-priority
hypotheses. The check included the limit-stage closure, seed exit
conditions, uniform strategies, cardinal stabilization, and target exits.
The proof is now incorporated in n-c-018.tex under
sec:p09-parity-positional-proof, followed by the least-recurring
convention, the positional model-checking corollary, and the
bounded-branching tree-model argument.
This is bounded proof review and incorporation, not whole-topic or
publication acceptance.
