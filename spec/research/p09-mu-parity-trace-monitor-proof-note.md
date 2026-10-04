# A deterministic least-parity monitor for all traces of relation words

Date: 2026-09-06. Status: a complete finite construction and proof, reusing
the actual NBA-to-deterministic-Rabin construction already printed in
`handbook/parts/p09/presentations/n-c-013.tex`. The present note proves the
bad-trace NBA, exact complementation on its total deterministic run, and the
remaining deterministic Muller-to-least-parity conversion. It does not assume
an unproved McNaughton theorem or a parity-conversion theorem. It does not
prove the separate modal cover simulation that will consume this monitor.
No software test, manuscript build, render, or independent admission is
claimed by the existence of this note.

## 1. Fixed input and exact monitored language

Fix a finite nonempty control set `Q`, a distinguished initial control
`q_* in Q`, and a priority map

\[
 \Omega:Q\longrightarrow\{0,\ldots,d\}.
\]

Put `n=|Q|`. The finite input alphabet is

\[
 \mathsf R=\mathcal P(Q\times Q),\qquad
 |\mathsf R|=2^{n^2}.
\]

An input word is `rho=rho_0 rho_1 ... in R^omega`. A trace of this word
means an infinite sequence `q_0 q_1 ...` with

\[
 q_0=q_*,\qquad (q_i,q_{i+1})\in\rho_i
                 \quad(i\in\mathbb N).
\]

Thus the initial control is fixed, not universally quantified over `Q`.
Each trace has a nonempty set of infinitely recurring priorities because
the priority set is finite. A trace is good when its least infinitely
recurring priority is even, and bad when that priority is odd. Define

\[
\begin{aligned}
 \mathsf{BAD}
  &=\{\rho:\text{some trace from }q_*
                  \text{ has odd least recurring priority}\},\\
 \mathsf{GOOD}
  &=\mathsf R^\omega\setminus\mathsf{BAD}.
\end{aligned}
\]

Equivalently, GOOD says that every infinite trace is good. A word having
no infinite trace is GOOD. Finite trace prefixes are not assigned an
infinite parity outcome.

## 2. An explicit nondeterministic Büchi automaton for BAD

Let

\[
 J=\{j\in\Omega(Q):j\text{ is odd}\}.
\]

Using only occurring odd priorities is sufficient; adding nonoccurring
odd indices would merely add modes incapable of Büchi acceptance.
The NBA state set is the disjoint union

\[
 B=\{(q,\mathsf{search}):q\in Q\}
   \ \dot\cup\
   \{(q,j):q\in Q,\ j\in J,\ \Omega(q)\ge j\}.
\]

The initial state is `(q_*,search)`. Its accepting states are

\[
 F_B=\{(q,j):j\in J,\ \Omega(q)=j\}.
\]

For a relation letter `rho`, define every transition by

\[
\begin{aligned}
 \Delta((q,\mathsf{search}),\rho)
   ={}&\{(r,\mathsf{search}):(q,r)\in\rho\}\\
     &\cup\{(r,j):(q,r)\in\rho,\ j\in J,
                                      \ \Omega(r)\ge j\},\\
 \Delta((q,j),\rho)
   ={}&\{(r,j):(q,r)\in\rho,\ \Omega(r)\ge j\}.
\end{aligned}
\]

The first clause may continue searching or commit, at the next control,
to a permissible odd index. Once committed, the run never returns to
search and never changes its index. Empty successor sets are allowed.
The number of states is exactly

\[
 N=n+\sum_{j\in J}|\{q\in Q:\Omega(q)\ge j\}|
       \ \le\ n(1+|J|).
\]

The accepting set may be empty, including when `J` is empty; then the
NBA rejects every word, as BAD requires.

### Soundness

Suppose the NBA has an accepting run on `rho`. Projection to its first
coordinate gives a trace from `q_*`, by the transition definition.
Search states are nonaccepting, so an accepting run must commit at a
finite position to some fixed odd `j`. Every subsequent trace priority
is at least `j`; infinitely many subsequent accepting states have
priority exactly `j`. Hence the trace has least infinitely recurring
priority exactly `j`, and `rho` belongs to BAD.

### Completeness

Suppose a trace from `q_*` is bad, with odd least infinitely recurring
priority `j`. Then `j in J`. Each priority below `j` occurs only
finitely often; because there are finitely many such priorities, choose
one finite `t>=1` after all their occurrences. Follow the trace in
search mode through position `t-1`. On its next relation edge, commit
to `(q_t,j)`, which is permissible because `Omega(q_t)>=j`.
Continue following the same trace in mode `j`. All its later priorities
are at least `j`, so all these transitions exist, and priority `j`
occurs infinitely often, so the resulting NBA run is Büchi accepting.

The requirement `t>=1` shows explicitly that no commitment at the
initial position is needed. Ignoring a finite initial priority prefix
does not alter the bad-trace condition. Thus

\[
 L(B,\Delta,F_B)=\mathsf{BAD}.
\]

### No infinite trace

Every infinite NBA run projects to an infinite trace, whether or not
it accepts. Therefore a word with no infinite trace has no infinite
NBA run and is rejected by this NBA.

There is also a finite-prefix description of this case. The tree of
finite trace prefixes is rooted at `q_*` and is at most `n`-branching.
If it had vertices at arbitrarily large depths, König's lemma would
give an infinite trace. Consequently, if there is no infinite trace,
some finite level is empty. At that level there are no reachable NBA
states: the search states follow precisely all finite traces, and every
committed state likewise projects to one. No later letter can restore
a run after that empty level.

## 3. Reuse the existing Safra construction, without replacing its proof

Apply the NBA-to-deterministic-Rabin construction already printed under
`sec:p09-presentation-n-c-013`, specifically the expanded-manuscript
presentation:

- current actual LaTeX lines 997--1079: finite states, invariants,
  deterministic letter update, and fixed name allocation;
- lines 1081--1107: total rejecting sink and green/red Rabin pairs;
- lines 1126--1157: soundness and completeness;
- lines 1159--1170: finite-state count and number of pairs.

These are locators in the actual manuscript inspected for this note,
not claims inferred from a theorem index. Its cited source is
`Safra1995Extended`, and its persistent vocabulary has `N` names for
an `N`-state input NBA. The distinct Thomas presentation with `2N`
names/pairs is not substituted or mixed into this application. The
Safra state and correctness proof are reused here, not reconstructed
anew.

The output is a finite **total deterministic** word automaton

\[
 D=(Z,\mathsf R,\eta,z_0,\{(G_v,B_v):v\in V\}),
 \qquad |V|=N,
\]

where `eta:Z x R -> Z` is total. Put `m=|Z|`; the existing construction
gives

\[
 m=2^{O(N\log(N+1))}.
\]

The harmless `N+1` inside the logarithm covers small inputs in the
asymptotic display. Let the unique run on `rho` be

\[
 z_0z_1\cdots,
 \qquad z_{i+1}=\eta(z_i,\rho_i),
 \qquad I=\operatorname{Inf}(z_0z_1\cdots).
\]

The existing proof gives the exact equivalence

\[
 \rho\in\mathsf{BAD}
 \quad\Longleftrightarrow\quad
 \exists v\in V\;
       (I\cap G_v\ne\varnothing\ \land\
                                  I\cap B_v=\varnothing).
\]

Here `G_v` is the infinitely recurring green/good event and `B_v` the
eventually absent red/bad event. The existing sink `z_dead` belongs to
every `B_v`, belongs to no `G_v`, and loops on every relation letter.
It is the deterministic state reached when no NBA run extends the
prefix. In particular, the no-infinite-trace case from Section 2
eventually reaches it.

## 4. Exact deterministic complementation as a Muller condition

Keep the same total deterministic transition system and define the
finite Muller family

\[
 \mathcal F_{\mathrm{good}}
   =\{I\subseteq Z:
       \forall v\in V\;
       (I\cap G_v=\varnothing\ \lor\
                                I\cap B_v\ne\varnothing)\}.
\]

This is also the Streett reading: infinite recurrence of green requires
infinite recurrence of red, for each name. The displayed family is
simply the Boolean complement of the Rabin predicate on the same
infinity set. Since every word has exactly one infinite run,

\[
 \rho\in\mathsf{GOOD}
 \quad\Longleftrightarrow\quad
 \operatorname{Inf}(z_0z_1\cdots)
                  \in\mathcal F_{\mathrm{good}}.
\]

No nondeterministic complementation step is hidden here. Totality is
essential to using the unique run for every word. The existing
totalization already supplies it. In particular,
`{z_dead} in F_good`, so a word whose run remains in that sink is
accepted by the complemented condition, as vacuous trace goodness
requires. The family can be explicitly enumerated over `P(Z)`, but
membership can instead be computed by its displayed finite pair test.

## 5. A fully explicit Muller-to-least-parity record conversion

The next argument applies to any finite total deterministic Muller
word automaton `(Z,R,eta,z_0,F)`, not only the one just constructed.
Fix an arbitrary ordering of the `m>=1` states of `Z`. A record is a
permutation

\[
 \pi=(u_1,\ldots,u_m)
\]

written from least recent to most recent. Before every state has been
read, the order of unvisited states is just the chosen initial order.
That finite initialization will not affect the recurrence proof.

When a state `z=u_k` is read, define the **pre-move** suffix and the
updated permutation by

\[
 S(\pi,z)=\{u_k,u_{k+1},\ldots,u_m\},\qquad
 \operatorname{move}(\pi,z)
   =(u_1,\ldots,u_{k-1},u_{k+1},\ldots,u_m,u_k).
\]

The emitted priority is

\[
 e(\pi,z)=
  \begin{cases}
   2k,&S(\pi,z)\in\mathcal F,\\
   2k+1,&S(\pi,z)\notin\mathcal F.
  \end{cases}
\]

Both the hit position and the tested suffix are taken **before**
moving the read state to the end. Using its post-move position would
make every hit equal to `m` and would lose the required information.

### The recurrence lemma

Feed any infinite state sequence `w_1 w_2 ...` into the record, starting
from any permutation. Put

\[
 I=\operatorname{Inf}(w_1w_2\cdots),\qquad
 r=|I|,\qquad h=m-r+1.
\]

The set `I` is nonempty. Every state outside `I` appears only finitely
often. After its final appearances have all occurred, wait further
until every state of `I` has appeared at least once. At this point
and forever afterwards, the permutation has the form

\[
 (\text{the }m-r\text{ states outside }I,
                         \text{the }r\text{ states in }I).
\]

The first block is a frozen prefix: its members are never moved again.
The second block consists exactly of `I`, with its relative order
updated by further visits. It follows that all sufficiently late hit
positions are at least `h`, and that every sufficiently late hit at
position `h` has pre-move suffix exactly `I`.

Hits at `h` occur infinitely often. Indeed, at any sufficiently late
time, let `u` be the state occupying position `h`. It belongs to `I`,
so it will be read again. Until its next reading, every read state is
strictly to its right and is moved to the end; such moves leave `u`
at position `h`. Its next reading therefore hits `h`. Applying this
argument after any proposed last hit rules out a last hit.

Thus the smallest infinitely recurring hit is exactly `h`. At all
sufficiently late hits there, the emitted priority is the single value

\[
 p_I=
  \begin{cases}
   2h,&I\in\mathcal F,\\
   2h+1,&I\notin\mathcal F.
  \end{cases}
\]

It occurs infinitely often. Hits at smaller positions occur only
finitely often, while a hit at `k>h` emits at least
`2(h+1)>p_I`. Consequently

\[
 \min\operatorname{Inf}(\text{emitted priorities})=p_I.
\]

The emitted sequence therefore has even least recurring priority
exactly when `I in F`. This proves the Muller-to-parity assertion,
including its least-priority orientation, without an external record
conversion theorem.

## 6. Store each emitted priority at the next automaton state

For the GOOD Muller automaton of Section 4, take the monitor state set

\[
 W=Z\times\operatorname{Perm}(Z)\times
                              \{0,\ldots,2m+1\}.
\]

Choose an arbitrary initial permutation `pi_0` and put

\[
 w_0=(z_0,\pi_0,0),\qquad
 \Lambda(z,\pi,c)=c.
\]

Its initial priority could be any member of the displayed finite
priority range; `0` is only a representative choice. Define the total
deterministic transition on a relation letter `rho` by

\[
\begin{aligned}
 z'&=\eta(z,\rho),\\
 c'&=e(\pi,z')
       \quad\text{using }\mathcal F=\mathcal F_{\mathrm{good}},\\
 \gamma((z,\pi,c),\rho)
       &=(z',\operatorname{move}(\pi,z'),c').
\end{aligned}
\]

The permutation contains every `z'` exactly once, so the hit and the
update are uniquely defined. On input `rho_0 rho_1 ...`, this monitor
feeds `z_1,z_2,...` to the record and its state priorities are

\[
 0,c_1,c_2,\ldots,
 \qquad c_{i+1}=e(\pi_i,z_{i+1}).
\]

Omitting the initial deterministic state `z_0` from the record input
does not change its infinity set. Adding the single initial priority
`0` does not change the least infinitely recurring emitted priority.
The recurrence lemma and Section 4 therefore give

\[
 \boxed{\quad
  L(W,\mathsf R,\gamma,w_0,\Lambda)=\mathsf{GOOD}.
  \quad}
\]

This is a deterministic parity word automaton in the manuscript's
least-recurring-even convention. Its priority is an ordinary state
component, not a separate transition-acceptance convention.

### The totalized sink in this monitor

Suppose the deterministic component reaches `z_dead`. It remains there
forever. After the first reading of `z_dead` by the record, that state
is last in the permutation. Every later reading has hit position `m`
and pre-move suffix `{z_dead}`. Since this singleton belongs to
`F_good`, every such emission is `2m`, which is even. Any earlier
emission is a finite prefix. In particular, relation words with no
infinite trace are accepted; an empty reachable relation layer is
not accidentally treated as an infinite bad trace or as a missing
monitor run.

## 7. Explicit finite bounds and effectiveness

The NBA has the exact finite size `N` displayed in Section 2. The
existing Safra construction gives `N` pairs and
`m=2^{O(N log(N+1))}` deterministic states, including its sink. The
record construction above uses exactly the displayed Cartesian
product before deleting unreachable copies, so

\[
 |W|=m\,m!\,(2m+2),
 \qquad \Lambda(W)\subseteq\{0,\ldots,2m+1\}.
\]

Not all of these tuples need be reachable. Keeping them all makes the
definition and bound immediate. In particular,

\[
 |W|=2^{O(m\log(m+1))}
       =2^{\,2^{O(N\log(N+1))}}.
\]

These are deliberately crude upper bounds, not an optimal
determinization, optimal monitor, or normal-form size claim.

Every step is effective: enumerate relation letters and NBA
transitions; apply the already explicit finite Safra update; test
Muller-family membership by the finite green/red predicate; enumerate
permutations; and compute the old hit, suffix, move, and emitted
priority. An explicit monitor transition table has

\[
 2^{n^2}|W|
\]

entries before any sharing. Indexing states and priorities in binary
adds only their usual finite encoding costs. Enumerating the entire
Muller family is optional and is not an oracle: its displayed
membership predicate decides each suffix directly.

The complete dependency chain is therefore

\[
 \text{explicit bad-trace NBA}
 \ \longrightarrow\
 \text{existing proved deterministic Rabin construction}
 \ \longrightarrow\
 \text{Boolean complement on its unique run}
 \ \longrightarrow\
 \text{record conversion proved in this note}.
\]

There is no independent appeal to deterministic-Muller existence,
McNaughton equivalence, Muller-to-parity conversion, or
alternating-to-nondeterministic simulation within this chain. The
remaining modal cover simulation may now use this concrete total
GOOD-word monitor with its stated initial control and priority
convention.
