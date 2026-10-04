# A response-permutation monitor for Streett streams

Date: 2026-09-06.

This note proves the proposed conversion from a finite deterministic
Streett state stream to least-recurring-even parity. The memory records
the order of the Streett pair names. Its factorial factor is `k!`, where
`k` is the number of pairs; it is not a factorial in the number of
underlying states.

## Definitions and exact update

Let `Z` be a nonempty finite set of `m` underlying states. Fix `k >= 0`
Streett pairs `(G_i,R_i)`, for `i in K = {1,...,k}`, with
`G_i,R_i` subsets of `Z`. An infinite stream

`z_0,z_1,z_2,...`

satisfies the Streett condition precisely when, for every `i`, infinitely
many indices `t` with `z_t in G_i` imply infinitely many indices `t` with
`z_t in R_i`. Membership in both sets at the same time is permitted.

A record `pi = (pi(1),...,pi(k))` is a permutation of `K`; positions are
numbered **1 through k**. Write `pos_pi(i)` for the unique position of
`i`. Fix any initial permutation `pi_0`. At time `t`, before processing
`z_t`, the record is `pi_t`. Define

`T_t = {i : z_t in G_i}`,

`B_t = {i : z_t in R_i}`,

`A_t = T_t union B_t`.

Here `T_t` contains the triggers, `B_t` the responses, and `A_t` the
active pair names. Put `D = 2k+2`. If `A_t` is empty, emit `c_t = D`.
Otherwise let

`h_t = min {pos_(pi_t)(i) : i in A_t}`,

and let `i_t = pi_t(h_t)`. Emit

`c_t = 2h_t` if `i_t in B_t`,

`c_t = 2h_t+1` otherwise.

Thus a response takes precedence when the earliest active name is both
triggered and responded to. This is necessary: a pair whose green and
red events occur together infinitely often satisfies its Streett
implication.

Only after computing this output from the **old** positions, update

`pi_(t+1) = (pi_t restricted to K minus B_t)`
`             concatenated with (pi_t restricted to B_t)`.

Each restriction preserves the old relative order. In words, remove all
responding names simultaneously and append them, in their old order.
Names that do not respond preserve their relative order as well. If
there are no responses the permutation does not change. This is a
well-defined permutation, including when several or all names respond
at once.

An emitted value belongs to `{2,...,2k+2}`. We use the permitted priority
set `P_k = {0,...,2k+2}`, of cardinality `2k+3`; its two unused small
values cause no difficulty. The exact product bound below uses this full
set, without claiming that every bookkeeping state is reachable or that
the number of priorities is minimal.

## The frozen-prefix lemma

For the fixed infinite stream, let

`F = {i : z_t in R_i at only finitely many times t}`,

`J = K minus F`, and `f = |F|`.

There is a finite time after which the first `f` positions of every
record consist precisely of `F`, in a fixed order. Every remaining name
belongs to `J` and responds infinitely often.

To prove this, first choose a time after the last response of every
member of `F`; a common time exists because `F` is finite. From then on
members of `F` are never removed or appended, so their relative order
is fixed. Every member of `J` has a later response. Choose a time after
each member of `J` has responded at least once following that common
cutoff. When such a response occurs, its name is appended after every
member of `F`, since none of those members responds. Subsequent updates
cannot move that name in front of `F`. Consequently all names of `J`
are now behind all names of `F`. Future updates only reorder the suffix
of names in `J`, so the prefix is permanently frozen.

The proof uses neither single responses nor a particular tie order
between simultaneous responses. The specified stable tie order ensures
a unique deterministic update.

## Rejection when a Streett implication fails

Suppose the Streett condition fails. Then some member of `F` is triggered
infinitely often. After the frozen-prefix lemma applies, let `b` be the
least position in that prefix occupied by such a name, and put
`i_b = pi_t(b)`, independent of all sufficiently late `t`.

Every earlier prefix name responds only finitely often and, by the
choice of `b`, is also triggered only finitely often. Discard a further
finite prefix of the stream so that none of these earlier names is
ever active again, and no member of `F` responds again. Then:

- Whenever `i_b` is triggered, it is the earliest active name, has no
  response, and emits `2b+1`. This occurs infinitely often.
- No active name can occur in an earlier position.
- An event at position `b` cannot emit `2b`, since that frozen name
  never responds again.
- An event in a later position emits at least `2b+2`, and the default
  `D = 2k+2` is also greater than `2b+1`.

Thus the least infinitely recurring output priority is exactly `2b+1`,
which is odd. The monitor rejects.

## Acceptance when all Streett implications hold

Suppose the Streett condition holds. Every member of `F` then has only
finitely many triggers as well as finitely many responses. After a
common finite cutoff, the entire frozen prefix is inactive forever.

If `J` is empty, no name is ever active after this cutoff. The monitor
emits the even default `D` forever and accepts.

Otherwise `f < k`. Every subsequent active name lies at a position at
least `f+1`, so every subsequent output is at least `2(f+1)`. We show
that the even output `2(f+1)` occurs infinitely often.

At any time after the cutoff, consider the name currently at position
`f+1`. It is the oldest name in the responding suffix. While this name
does not itself respond, updates to other names cannot change its
position: no name lies between the inactive prefix and this name, and
removing and appending later names leaves it first in the suffix. Since
the name belongs to `J`, it has a later response. At its first such
response, it still occupies position `f+1`. The frozen prefix is
inactive, so it is the earliest active name, and the output is
`2(f+1)`.

This event occurs arbitrarily late. Equivalently, after any proposed
last occurrence of `2(f+1)`, the oldest suffix name would eventually
respond and produce another one. Hence `2(f+1)` recurs infinitely often.
No smaller priority recurs, so the least recurring priority is even.

This argument includes simultaneous responses. If the oldest suffix
name responds together with other names, it is still the earliest active
name in the old record and therefore still emits the even priority.
After the update, the oldest name may change or remain the same; the
argument does not assume either outcome. Intervening triggers at the
oldest position may emit the next odd value, but the smaller even value
recurs infinitely often and decides parity.

Combining the two cases proves, for every infinite underlying stream,

`Streett(z_0 z_1 ...) iff min Inf(c_0 c_1 ...) is even`.

## The case k = 0

There are no pair names, the unique permutation is the empty sequence,
and every active set is empty. The output is always `D = 2`, an even
priority. The Streett condition is the empty conjunction and therefore
accepts every infinite stream. Both the update and the proof remain
valid, with `0! = 1`.

## A deterministic product with delayed state priorities

Let the underlying deterministic automaton have a total transition map
`delta: Z x Alphabet -> Z` and initial state `z_init`. Write its run as
`z_(t+1) = delta(z_t,a_t)`. Fix the initial permutation `pi_0` and initial
color `D`.

Use the product state space

`Z' = Z x Perm(K) x P_k`,

initial state `(z_init,pi_0,D)`, and state priority

`p'(z,pi,c) = c`.

For one input symbol `a`, define the deterministic transition by

`delta'((z,pi,c),a)`
`    = (delta(z,a), update(pi,z), output(pi,z))`,

where `update` and `output` are exactly the functions defined above.
Both use the current underlying state `z` and the old permutation `pi`;
the incoming stored color is only emitted as the current state's
priority and is not fed into the new computation.

At time `t`, the product run has the form

`(z_t,pi_t,c_(t-1))`, with `c_(-1) = D`.

Its priority stream is therefore

`D,c_0,c_1,c_2,...`.

The one-step delay and the single initial priority do not change which
priorities occur infinitely often. The product accepts exactly the
underlying Streett language. This convention avoids silently processing
the same underlying state twice or skipping the initial state.

The full product has exactly

`m * k! * (2k+3)`

states and uses the priority set `{0,...,2k+2}`. Pruning unreachable states
can only decrease that count. No intermediate transition controls are
needed for this deterministic monitor. For `k >= 1`, the convenient
estimate `k! <= k^k` also gives

`|Z'| <= m * (2k+3) * k^k`.

Thus the permutation contribution to the logarithm of the number of
states is `O(k log(k+1))`, independent of any factorial in `m`.

## Conversion of the resulting parity condition to Rabin pairs

We state the pair convention explicitly. A Rabin/Pairs family
`(A_d,B_d)` accepts a run when, for at least one pair, the run visits
`A_d` infinitely often and `B_d` only finitely often. This is the source's
existential green-infinitely/red-finitely convention. In the alternate
notation `(E_d,F_d)` with finite `E_d` and infinite `F_d`, use
`E_d = B_d` and `F_d = A_d`.

For each even `d in {0,2,...,2k+2}`, put

`A_d = {v in Z' : p'(v) = d}`,

`B_d = {v in Z' : p'(v) < d}`.

If the least recurring priority is even `d`, then `A_d` is visited
infinitely often, while all priorities below `d` occur only finitely
often. Since the priority set is finite, their union `B_d` is visited
only finitely often, and this Rabin pair accepts. Conversely, if one
pair accepts, priority `d` recurs and no smaller priority recurs, so
the least recurring priority is the even value `d`.

This conversion adds no states and gives `k+2` pairs, which is
`O(k+1)`. In this particular monitor, priority 0 is never emitted after
the initial position and the chosen initial priority is `D`, so the
pair for `d = 0` cannot witness acceptance from the designated start.
It may be omitted, leaving exactly `k+1` pairs with even values
`2,4,...,2k+2`. When `k = 0`, this leaves the single pair for priority 2,
which accepts all runs, as required.

These are newly constructed Rabin pairs for the monitor's parity
condition. One does not obtain them by simply interpreting the original
Streett pairs with their complemented acceptance convention.

## Review outcome

The proposed record is correct with the old-position computation,
response precedence, and simultaneous stable update stated above. The
deterministic product uses `m * k! * (2k+3)` states, at most `2k+3`
priorities, and a Rabin conversion with `k+2` pairs (or `k+1` after the
specified harmless omission). No manuscript edits, software tests,
builds, or renders were performed for this proof.
