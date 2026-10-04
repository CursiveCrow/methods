# Nondeterminization of a total Streett alternating binary-tree automaton

Date: 2026-09-06.

This note supplies the construction, both correctness directions, and
the counts. The input parameters count the **normalized total**
presentation specified below. The proof uses the already established
full-state Muller permutation lemma, odd-threshold trace automaton,
Safra determinization, and pair-response record. It does not apply a
permutation record to the large Safra state set.

## 1. Input and claimed bounds

Let
\[
 \mathcal A=(\Sigma,Q,DAND,AAND,\psi,\delta,\chi,L,q_0,\Phi)
\]
be a finite alternating full binary-tree presentation. Thus \(q_0\in Q\),
\[
 \psi\subseteq Q\times DAND,\quad
 \delta:DAND\times\{0,1\}\to AAND,\quad
 \chi\subseteq AAND\times Q,\quad L:DAND\to\Sigma.
\]
Write \(n=|Q|\geq1\), \(m=|DAND|\), and suppose \(\Phi\) has \(k\geq1\)
Streett pairs \((G_j,R_j)\). Its condition is
\[
 \bigwedge_{j=1}^k(\operatorname{Inf}G_j
                         \Longrightarrow\operatorname{Inf}R_j).
\]
Assume that for every \(q\in Q\) and \(a\in\Sigma\), some \(d\in DAND\)
satisfies \(q\psi d\) and \(L(d)=a\). Assume also that every AAND control
has at least one \(\chi\)-successor. These are the totality assumptions.
The empty input alphabet has no full labelled trees and gives a
vacuous language-equivalence statement; the construction and counts
below concern the nonvacuous case \(\Sigma\ne\varnothing\).

We construct an equivalent nondeterministic Rabin/Pairs tree automaton
\[
 \mathcal N=(\Sigma,Q',AND',\psi',\delta',L',s'_0,\Omega).
\]
Its pair convention is existential infinite-green/finite-red. Put
\[
 S=n\,n!\,(2n+2).
\]
There is an integer \(B\leq S(n+2)\) such that the construction has
\[
 \begin{aligned}
 |Q'|&\leq(2^S-1)\,M\,B!\,(2B+3),
       &&M=2^{O(B\log(B+1))},\\
 |AND'|&\leq |Q'|\,m^S,\\
 \#\Omega&\leq B+1.
 \end{aligned}
\]
Consequently, with \(H=n\log(n+1)\),
\[
 \begin{aligned}
 |Q'|&\leq 2^{\,2^{O(H)}},\\
 |AND'|&\leq 2^{\,2^{O(H)}}\,m^{\,2^{O(H)}},\\
 \#\Omega&\leq 2^{O(H)}.
 \end{aligned}
\]
For \(k\geq1\), these imply the relaxed displayed source bounds
\[
 \begin{aligned}
 |Q'|&\leq 2^{\,k^2\,2^{O(H)}},\\
 |AND'|&\leq 2^{\,k^2\,2^{O(H)}}\,m^{\,2^{O(H)}},\\
 \#\Omega&\leq k\,2^{O(H)}.
 \end{aligned}
\]
For \(n\geq2\), \(n\log(n+1)=\Theta(n\log n)\), giving the source's usual
asymptotic notation. Using \(\log(n+1)\) keeps the small case \(n=1\)
explicitly covered. These are upper bounds, not assertions that every
constructed state or pair is necessary.

## 2. Turn the original Streett condition into parity

Define the Muller family on the original controls by
\[
 \mathcal F=\{I\subseteq Q:
   \text{for every }j,\ I\cap G_j=\varnothing
                    \text{ or }I\cap R_j\ne\varnothing\}.
\]
For an infinite sequence over the finite set \(Q\), its infinity set
belongs to \(\mathcal F\) exactly when it satisfies \(\Phi\). The family
is finite and effectively determined by the original pairs.

Apply only the full-state permutation lemma at
the manuscript anchor sec:p09-muller-parity-record, with the state
set \(Q\). An augmented control is
\[
 a=(q,\pi,c)\in
 \widehat Q=Q\times\operatorname{Perm}(Q)\times\{0,\ldots,2n+1\}.
\]
Its priority is \(\widehat p(a)=c\). The initial control is
\[
 a_0=(q_0,\pi_0,0)
\]
for any fixed permutation \(\pi_0\). This full set has exactly \(S\)
elements.

For \(a=(q,\pi,c)\) and an original successor \(r\), let \(h\) be the
position of \(r\) in the old permutation, with positions numbered
\(1,\ldots,n\). Let \(I_h\) be the set of names in the suffix beginning
at that position. Move \(r\) to the end to obtain \(\pi'\), and put
\[
 \theta(a,r)=
 \begin{cases}
 (r,\pi',2h),& I_h\in\mathcal F,\\
 (r,\pi',2h+1),& I_h\notin\mathcal F.
 \end{cases}
\]
At \((x,a)\), where \(a\) projects to \(q\), Player I chooses an
original enabled DAND control \(d\) with \(q\psi d\) and \(L(d)=t(x)\).
Player II chooses direction \(i\), then any
\[
 r\in\operatorname{Succ}(d,i)
       :=\{r:\chi(\delta(d,i),r)\},
\]
and the augmented game continues at \((xi,\theta(a,r))\).
One may implement these choices by DAND and AAND copies tagged with
\(a\). Each augmented control still has at most \(m\) original choices;
the final transition count uses these original choices, not the number
of tagged copies.

Every original finite history has a unique augmentation from \(a_0\).
Conversely, projecting any augmented history gives an original history.
For each infinite sequence the permutation lemma makes the least
recurring augmented priority even exactly when its original infinity
set lies in \(\mathcal F\). The record processes successors after the
initial original control; omitting that single initial control and
adding the initial priority 0 do not affect recurrence.

An original winning strategy lifts to the augmented game by projection.
An augmented winning strategy gives an original strategy by updating
the finite record along the actual original history. Thus the original
Streett game and this parity game accept the same input trees, without
any prior assumption that the original Streett strategy is positional.

Fix an accepted input tree. The augmented parity arena has finitely
many priorities, and Player-I choices occur only at positions \((x,a)\).
Giving the two intervening Player-II layers a priority above all
augmented-control priorities preserves the winner: every infinite play
returns to augmented controls after a fixed finite number of moves.
The established positional parity theorem therefore supplies a winning
strategy \(\lambda(x,a)\). Extend it outside its winning region by any
enabled choice of the current letter, which exists by totality.

This positional step is used before merging histories into obligation
sets. It ensures that all histories reaching the same input node and
augmented control can use one common DAND choice.

## 3. A deterministic monitor for all augmented relation traces

Let
\[
 \mathcal R=\mathcal P(\widehat Q\times\widehat Q).
\]
A trace of a relation word \(\rho_0\rho_1\cdots\) is an infinite
sequence \(a_0,a_1,\ldots\) beginning at the fixed initial augmented
control and satisfying \((a_t,a_{t+1})\in\rho_t\) at every step.
The word is GOOD when every such trace has even least recurring
priority. If it has no infinite trace, it is GOOD.

For completeness, the odd-threshold construction at
sec:p09-mu-trace-monitor recognizes BAD as follows. Use search states
\((a,*)\), and committed states \((a,j)\), where \(j\) is an odd priority
and \(\widehat p(a)\geq j\). The initial state is \((a_0,*)\). Every
transition on \(\rho\) follows an edge \((a,b)\in\rho\). A search state
may remain searching or commit to any odd \(j\leq\widehat p(b)\).
A committed state retains its \(j\) and requires
\(\widehat p(b)\geq j\). The Büchi states are precisely the committed
states satisfying \(\widehat p(a)=j\).

Every Büchi run therefore identifies a trace eventually avoiding
priorities below a fixed odd \(j\) and visiting \(j\) infinitely often.
Conversely, a bad trace can commit to its odd least recurring priority
after the last smaller value. Commitment may be delayed past the first
letter without affecting recurrence. Thus this automaton recognizes
exactly BAD.

Its number of states is
\[
 B=S+\sum_{\substack{j\text{ odd}\\0\leq j\leq2n+1}}
            |\{a\in\widehat Q:\widehat p(a)\geq j\}|
   \leq S(n+2).
\]
There are \(n+1\) possible odd values in this full priority range.
Unreachable states or unused thresholds may be retained for this bound.

Apply the established Safra construction at
sec:p09-safra-determinization. Its total deterministic Rabin automaton
has \(M=2^{O(B\log(B+1))}\) states and \(B\) pairs
\((G_v^{\rm bad},R_v^{\rm bad})\). It accepts BAD by
\[
 \exists v\,
   (\operatorname{Inf}G_v^{\rm bad}
      \land\operatorname{Fin}R_v^{\rm bad}).
\]
Its empty-root sink is included in \(M\). Complementing this condition
on the same deterministic run gives the \(B\)-pair Streett condition
\[
 \bigwedge_v
  (\operatorname{Inf}G_v^{\rm bad}
      \Longrightarrow\operatorname{Inf}R_v^{\rm bad}),
\]
which recognizes exactly GOOD.

Now apply the pair-response monitor proved in
p09-streett-response-record-proof-note.md. Its permutation is a
permutation of these \(B\) pair names. It produces a deterministic
parity monitor with
\[
 N_G=M\,B!\,(2B+3)
\]
states. The delayed stored priority changes only a finite initial
prefix. Converting its parity to Rabin adds no states and leaves
\(B+1\) pairs after omitting the nonrecurring priority-0 pair, exactly
as proved in that note.

Denote this total deterministic GOOD monitor by
\[
 \mathcal G=(Z_G,\mathcal R,\zeta,z_G^0,\mathcal P_G).
\]
It accepts a relation word if and only if every trace from \(a_0\)
is parity accepting. This construction uses \(B!\), not \(M!\).
Indeed,
\[
 \log N_G=O(B\log(B+1)).
\]
The finite relation alphabet may be large, but it contributes no
additional state factor in these constructions.

## 4. The nondeterministic tree automaton

Let the nondeterministic OR controls be
\[
 Q'=\{(D,z):\varnothing\ne D\subseteq\widehat Q,\ z\in Z_G\},
 \qquad s'_0=(\{a_0\},z_G^0).
\]
The set \(D\) records current obligations; it is not a guessed run of a
single thread.

For a source state \(s=(D,z)\), a legal choice map is a function
\[
 f:D\longrightarrow DAND
\]
such that, for each \(a\in D\) projecting to \(q\), \(q\psi f(a)\),
and all \(f(a)\) have the same label \(\ell\in\Sigma\).
The set \(D\) is nonempty, so this common label, if present, is
uniquely determined by \(f\).

For direction \(i\), form the entire relation
\[
 \rho_i^{D,f}
 =\{(a,\theta(a,r)):
           a\in D,\ r\in\operatorname{Succ}(f(a),i)\}.
\]
Every allowed successor is included. Define
\[
 D_i=\rho_i^{D,f}[D]
     =\{b:\text{some }a\in D\text{ has }(a,b)\in\rho_i^{D,f}\},
 \qquad z_i=\zeta(z,\rho_i^{D,f}).
\]
The relation has domain exactly \(D\), because every directional AAND
target has a successor. In particular, \(D_i\ne\varnothing\), so
\((D_i,z_i)\in Q'\).

Create one AND choice \(d'=(s,f)\) with
\[
 s\psi'd',\qquad L'(d')=\ell,\qquad
 \delta'(d',i)=(D_i,z_i).
\]
At an input node, the nondeterministic automaton chooses \(f\) once
and thereby fixes its two child states. Its only universal choice is
the input direction, as required by the nondeterministic source tuple.
For every state \((D,z)\) and input letter, at least one legal \(f\)
exists, since each augmented obligation has an enabled original
choice of that letter.

Lift every Rabin pair \((A,B)\) of \(\mathcal G\) to
\[
 \bigl(\{(D,z):z\in A\},\{(D,z):z\in B\}\bigr).
\]
Thus a branch of a nondeterministic run accepts exactly when its
unique GOOD-monitor run accepts. The Rabin witness pair may differ
between input branches, as the ordinary tree acceptance condition
permits.

## 5. Obligation endpoints and the exact ithread condition

Fix a nondeterministic run on an input tree, including its selected
choice map \(f_x\) at every node \(x\). Write its state there as
\((D_x,z_x)\). Along a branch \(x_0=\epsilon,x_1,x_2,\ldots\), with
\(x_{t+1}=x_t i_t\), let
\[
 \rho_t=\rho_{i_t}^{D_{x_t},f_{x_t}}.
\]
Then \(z_{x_t}\) is precisely the deterministic monitor state after
the prefix \(\rho_0\cdots\rho_{t-1}\). This is immediate from the
transition definition.

The more important invariant is
\[
 D_{x_t}
  =\{a_t:\text{there is a finite trace }
          a_0a_1\cdots a_t
          \text{ following }\rho_0,\ldots,\rho_{t-1}\}.
\]
It holds initially because \(D_\epsilon=\{a_0\}\), and its induction
step is exactly \(D_{x_{t+1}}=\rho_t[D_{x_t}]\).
Consequently no unrelated augmented start state is introduced when
obligations are merged, and every represented obligation has a
reaching history.

Define a strategy in the augmented alternating game by choosing
\(f_x(a)\) whenever \(a\in D_x\). Extend it by enabled choices outside
these domains. A finite generated augmented thread along the branch
is now exactly a finite relation trace from \(a_0\): the direction
is the next input edge, and the relation includes precisely all
legal \(\chi\)-successors under the prescribed DAND choice.

The same equivalence holds for infinite sequences. An infinite
relation trace supplies one legal play because every one of its
edges is a legal successor under that strategy. Conversely, an
infinite play supplies every required relation edge. Equivalently,
the finite-prefix definition of an ithread is exactly satisfied
by these relation traces. There is no additional fairness
assumption and no selection of only one universal successor.

Since the strategy is a fixed function of the node and augmented
control, a finite-prefix consistency issue cannot arise from merging
two different histories at the same augmented control. On reachable
nodes every obligation has at least one successor in each direction,
so the relation words generated here have infinite traces; the
monitor's vacuous treatment of words without infinite traces is
nevertheless harmless and keeps its definition total.

## 6. From an accepting alternating strategy to a nondeterministic run

Suppose the original Streett automaton accepts the input tree.
Section 2 gives a positional winning strategy \(\lambda(x,a)\) for
the augmented parity game, extended to all positions by legal choices.

Construct the nondeterministic run recursively. Start at
\((\{a_0\},z_G^0)\). At a node \(x\) with obligations \(D_x\), choose
\[
 f_x(a)=\lambda(x,a)\quad(a\in D_x),
\]
and use the two successor states prescribed in Section 4.
All these choices have label \(t(x)\), so each transition is legal.

Fix any infinite input branch. By the endpoint invariant and the
exact trace correspondence, every relation trace from \(a_0\) is
an augmented play compatible with \(\lambda\). Each such play is
parity accepting, so its relation word is GOOD. The deterministic
GOOD monitor therefore accepts this branch, and the lifted Rabin
condition accepts the branch of the nondeterministic run.
Since the argument holds for every input branch, the run is
accepting.

This direction is where the positional strategy obtained before
forming obligation sets is essential. The proof never assumes
that arbitrary history-dependent Streett choices can simply be
merged when their current original controls agree.

## 7. From an accepting nondeterministic run to an alternating strategy

Conversely, fix an accepting nondeterministic run and all its
selected maps \(f_x\). Use the strategy from Section 5:
at a reachable augmented position \((x,a)\), choose \(f_x(a)\).
The endpoint invariant ensures \(a\in D_x\), so this prescription
is defined at every reachable position. Outside that domain use
any enabled choice of \(t(x)\).

Consider any compatible infinite augmented play. Its input
directions specify a branch of the fixed nondeterministic run.
Its control sequence is a trace from \(a_0\) through that branch's
relations. Since the nondeterministic run accepts, the corresponding
GOOD-monitor run satisfies its Rabin condition. The relation word
is therefore GOOD, and every trace through it, including the
chosen play, is parity accepting. Thus the augmented strategy wins.

Finally, implement this augmented strategy in the original
alternating game by updating the permutation and stored color
from the original control history. Every compatible original
ithread has its unique augmented parity-accepting counterpart.
The Muller-record equivalence makes its original control
sequence Streett accepting. The resulting original strategy
therefore accepts the input tree.

The strategy is total where the source requires legal choices,
because the input presentation is total. No claim that this
reconstructed original Streett strategy is history-free is
needed; its finite record is retained. Together with Section 6
this proves equivalence of the two tree languages.

## 8. State, transition, alphabet, and pair counts

The augmentation uses
\[
 S=n\,n!\,(2n+2)=2^{O(n\log(n+1))}
\]
controls and \(O(n)\) priorities. The odd-threshold automaton has
\[
 B\leq S(n+2)=2^{O(n\log(n+1))}.
\]
Safra followed by the response record gives
\[
 \begin{aligned}
 N_G&=M\,B!\,(2B+3),\\
 \log N_G&=O(B\log(B+1)),\\
 N_G&=2^{\,2^{O(n\log(n+1))}}.
 \end{aligned}
\]
Multiplication by \(2^S-1\) adds at most \(S\) to the base-2
logarithm, which remains \(2^{O(n\log(n+1))}\). Hence
\[
 |Q'|=(2^S-1)N_G\leq 2^{\,2^{O(n\log(n+1))}}.
\]

For each fixed \((D,z)\), at most \(m^{|D|}\) functions
\(D\to DAND\) exist. The enabledness and common-label requirements
only remove functions. A compatible function determines its
input letter because \(D\ne\varnothing\), so there is no additional
\(|\Sigma|\) factor. Therefore
\[
 |AND'|\leq\sum_{(D,z)\in Q'}m^{|D|}
          \leq |Q'|m^S.
\]
The same count covers all source letters together.
Totality also implies \(|\Sigma|\leq m\): fix the original initial
control and, for each letter, select one enabled DAND control;
distinct letters require distinct such controls because \(L\)
has one value per DAND control.

Each selected map determines both relations, both obligation
sets, and both monitor successors. There is no further choice
of a relation, monitor transition, or universal successor in a
nondeterministic AND node. The potentially large relation alphabet
therefore supplies no extra multiplicative factor in this AND
count.

There are at most \(B+1\) lifted Rabin pairs, independent of
the obligation coordinate. This is \(2^{O(n\log(n+1))}\).
The original \(k\) pairs enter the computation of the Muller
family, but not these state-count estimates. Since \(k\geq1\),
inserting the relaxed factors \(k^2\) in the outer exponent and
\(k\) in the pair count gives the stated source-shaped upper
bounds. This argument does not claim a bound on the size or
running time of every intermediate explicit transition table.

## 9. Meaning of the parameters after partial-game normalization

The parameters \(n,m,k\) in every displayed count above refer to
the total presentation in Section 1. They do not silently refer
to an earlier partial presentation.

For a partial presentation with \(n_0\) original OR controls,
\(m_0\) original DAND controls, \(k_0\) pairs, and finite alphabet
\(\Sigma\), under the rule that a player unable to move loses,
the stated accepting/rejecting-sink normalization gives
\[
 n\leq n_0+2,\qquad
 m\leq m_0+(n_0+2)|\Sigma|,\qquad
 k=\max(k_0,1).
\]
A missing Player-I choice is sent to the rejecting sink. An
empty universal AAND choice is sent to the accepting sink.
Both sinks have a directional self-continuation at every letter.
At most \(n_0|\Sigma|\) missing state-letter choices and
\(2|\Sigma|\) sink choices account for the displayed DAND bound;
repairing an empty AAND successor set needs no additional
original DAND choice.

Acceptance can use the original pair family, extended so that
the rejecting sink violates one pair and the accepting sink
satisfies every pair. When \(k_0=0\), the added pair has the
rejecting sink as its green set and an empty red set; old
infinite plays remain accepting and the two terminal outcomes
are represented correctly.

If the final statement is expressed in the pre-normalization
parameters, it must substitute these bounds. In particular,
the transition factor is bounded using
\[
 \bigl(m_0+(n_0+2)|\Sigma|\bigr)^{
          2^{O((n_0+2)\log(n_0+3))}},
\]
not by silently reusing \(m_0^{2^{O(n_0\log n_0)}}\).

## Review outcome

The construction proves the full alternating-to-nondeterministic
language equivalence, including every ithread on every input
branch. It attains the stated double-exponential upper bounds
in the normalized parameters. Only this proof note was written;
no manuscript edits, software tests, builds, or renders were
performed.
