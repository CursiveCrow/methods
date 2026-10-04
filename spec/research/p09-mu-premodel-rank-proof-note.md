# Ordinal signatures for universally good parity graphs

Date: 2026-09-06. Scope: a set-sized directed graph with finitely many
priorities and least-recurring-even acceptance. This note proves both
directions of the ordinal-signature characterization requested for the
premodel argument. The construction is valid for arbitrary branching and
dead ends; it gives a stronger coordinatewise property than the required
lexicographic one.

We work in the usual set-theoretic background with choice. The only
choice issue relevant to the argument is extracting an infinite chain
with finite path witnesses from a non-well-founded set relation; dependent
choice suffices. Well-founded recursion and replacement then supply the
ordinal ranks. Without such a choice principle, absence of a countable
descending chain must not simply be identified with well-foundedness of
an arbitrary set relation.

## 1. Statement and conventions

Let `H=(V,E)` be a directed graph with a set `V` of vertices, allowing
self-loops and dead ends. Let

\[
 p:V\longrightarrow\{0,\ldots,d\}
\]

be its finite-range priority map. An infinite path is a sequence
`v_0,v_1,...` with `(v_i,v_{i+1}) in E` for every `i`. It is good when
the least priority occurring infinitely often on it is even. Such a least
recurring priority always exists because the priority range is finite.

List the odd priorities actually occurring in the graph as

\[
 J=\{j_1<\cdots<j_k\}.
\]

For a tuple `r(v)=(r_{j_1}(v),...,r_{j_k}(v))`, its prefix `r_{<=m}(v)`
contains precisely the coordinates indexed by odd `j <= m`. The smallest
odd priority is the first, most significant coordinate. Use ordinary
lexicographic order on these ordinal tuples. The empty prefix is the
unique empty tuple, equal to itself.

**Theorem.** The following conditions are equivalent.

1. Every infinite path in `H` is good.
2. There is an ordinal-valued tuple `r(v)` for every vertex such that,
   on every edge `v -> w`,

   \[
    r_{\leq p(v)}(v)\ \geq_{\mathrm{lex}}\
                          r_{\leq p(v)}(w),
   \]

   with strict inequality whenever `p(v)` is odd.
3. There are ordinal functions `r_j` for `j in J` such that, on every
   edge `v -> w`,

   \[
   \begin{aligned}
    j\leq p(v)&\quad\Longrightarrow\quad r_j(v)\geq r_j(w),\\
    p(v)=j&\quad\Longrightarrow\quad r_j(v)>r_j(w).
   \end{aligned}
   \]

Condition 3 is the stronger coordinatewise-prefix property. At an even
source priority, the prefix of odd priorities `<= p(v)` is exactly the
prefix of odd priorities `< p(v)`, as required. No restriction is imposed
on coordinates indexed above the source priority. They may reset upward.

All coordinate values can be taken below one set ordinal. If `J` is
empty, the tuple is empty everywhere and every occurring priority is even.
The empty graph is included. Dead ends impose no outgoing-edge conditions.

The theorem concerns infinite paths only. In an application with separately
designated losing terminal positions, their exclusion is an additional
condition; the ranks do not turn a finite losing terminal into a winning one.

## 2. Source-threshold path relations

Assume every infinite path in `H` is good. For each odd `j in J`, define
a relation `R_j` on `V` as follows:

\[
\begin{split}
 v\ R_j\ w\quad\Longleftrightarrow\quad
 &\text{there is a finite path }
        v=v_0\to v_1\to\cdots\to v_\ell=w,
        \quad\ell\geq1,\\
 &p(v_i)\geq j\text{ for every }i<\ell,\quad
   p(v_i)=j\text{ for at least one }i<\ell.
\end{split}
\]

The priority restrictions concern the **sources of the path's edges**,
not its final endpoint. Thus an edge from a priority-`j` vertex to a
dead end, or to a vertex of lower priority, still witnesses `R_j`.
Conversely, a vertex whose own priority is below `j` has no `R_j` successor.

The orientation is the direction of rank descent: `v R_j w` will imply
`r_j(v)>r_j(w)`. Well-foundedness here means that every nonempty subset
has a member with no `R_j` successor in that subset, equivalently in the
usual choice background that there is no infinite chain
`v_0 R_j v_1 R_j v_2 ...` in this orientation.

### Well-foundedness

Suppose there were such an infinite chain. For each of its links choose
a finite witnessing path from the definition of `R_j` and concatenate
the paths. Every block is nonempty and finite, so the concatenation is
an infinite path of `H`.

Every vertex of this infinite concatenation is the source of some edge
in one of its blocks and hence has priority at least `j`. Although the
last endpoint of an individual block was not restricted, it becomes the
source at the start of the next block. A lower-priority endpoint could
not have a further `R_j` successor and therefore cannot occur in this
infinite chain.

Each block contains at least one edge source of priority `j`. Because
the blocks have positive finite lengths, these supply infinitely many
positions of priority `j` in the concatenated path. No priority below
`j` occurs. Its least recurring priority is consequently exactly `j`,
which is odd, contradicting the hypothesis.

If `R_j` were not well-founded, dependent choice, selecting the next link
together with a finite witness for it, would produce the prohibited chain
and concatenation. Thus `R_j` is well-founded. This argument applies
independently to every odd `j`.

There is no uniform bound on witness-path lengths in this reasoning,
and no finiteness or finite-branching assumption on the graph.

## 3. Define the ordinal ranks and prove their edge properties

By well-founded recursion, define

\[
 r_j(v)=\sup\{r_j(w)+1:v\ R_j\ w\},
 \qquad \sup\varnothing=0.
\]

Every value is an ordinal. Since `V` is a set, replacement gives a set
of values for each `j`. Finitely many coordinates can therefore be
bounded by one ordinal, for example

\[
 \kappa=\sup\left(\{1\}\cup
            \{r_j(v)+1:j\in J,\ v\in V\}\right),
 \qquad r(v)\in\kappa^k.
\]

Take an original edge `v -> w`.

If `p(v)=j`, the one-edge path itself witnesses `v R_j w`. The rank
equation gives

\[
 r_j(v)\geq r_j(w)+1>r_j(w).
\]

If `p(v)>j`, prepend this edge to any path witnessing `w R_j u`.
Its new source has priority at least `j`, and the old witness still
contains a priority-`j` source. Thus `v R_j u`. Consequently

\[
 \{u:w\ R_j\ u\}\subseteq\{u:v\ R_j\ u\},
\]

and the two rank equations yield

\[
 r_j(v)
   =\sup_{vR_ju}(r_j(u)+1)
   \geq\sup_{wR_ju}(r_j(u)+1)
   =r_j(w).
\]

The same inclusion argument also works for `p(v)=j`, but the direct
one-edge witness supplies the needed strictness there. If `p(v)<j`,
the definition gives `r_j(v)=0`, and no comparison with `r_j(w)` is
required. In particular, an edge of lower priority can lead from zero
to a positive value of this later coordinate.

This proves condition 3. It immediately implies condition 2: every
coordinate in the required prefix is nonincreasing, and when the source
priority is odd, its own coordinate is strictly decreasing. Such tuples
are respectively lexicographically nonincreasing and strictly decreasing.

### Why simultaneous higher-prefix slicing is unnecessary here

The construction never ranks arbitrary paths merely because they contain
one occurrence of priority `j`. Every edge source of an `R_j` witness
must satisfy the full threshold `p >= j`. This exclusion of all lower
priorities makes `R_j` well-founded before any higher-coordinate values
have been assigned.

The universal hypothesis therefore permits independent global ranks
for these particular threshold relations. No restriction to equal
higher-prefix slices is needed. This is stronger than constructing
lexicographic coordinates one slice at a time, and does not require
coordinate monotonicity on an edge of source priority below the coordinate's
index. Lower priorities retain exactly the freedom to reset later ranks.

## 4. Converse from the requested lexicographic conditions

Assume condition 2, without assuming the stronger coordinatewise property
of the constructed ranks. Suppose an infinite path

\[
 v_0\to v_1\to\cdots
\]

has odd least recurring priority `j`. Because only finitely many priorities
exist, a finite prefix contains every occurrence of any priority smaller
than `j`. After removing that prefix, all source priorities are at least
`j`, and priority `j` still occurs infinitely often.

Projection to an initial subtuple preserves a non-strict lexicographic
inequality. Every edge of the remaining path therefore satisfies

\[
 r_{\leq j}(v_i)\geq_{\mathrm{lex}}r_{\leq j}(v_{i+1}).
\]

At each source with priority exactly `j`, the prefix required by condition
2 is this very prefix, so the inequality is strict. The sequence of
finite ordinal tuples is consequently lexicographically nonincreasing
with infinitely many strict steps.

That is impossible. For completeness, the first coordinate of a
lexicographically nonincreasing ordinal sequence cannot increase. Among
its attained ordinal values there is a least one; after its first
attainment the coordinate is constant. On that tail the second coordinate
cannot increase and likewise eventually becomes constant. Iterating over
the finitely many coordinates makes the entire tuple eventually constant,
contradicting infinitely many strict steps.

Thus no infinite path has odd least recurring priority. This proves
condition 1 and completes all three equivalences.

The argument uses the finite number of priorities twice: to remove one
finite prefix containing all lower-priority occurrences, and to obtain a
finite ordinal tuple. It does not require vertices or individual edges
of the path to recur.

## 5. Examples and necessary distinctions

### A lower-priority reset must not be included in a rank witness

Let `e -> o -> e` be a two-vertex cycle with `p(e)=0` and `p(o)=1`.
Every infinite path has least recurring priority zero and is good.
A relation defined only by the existence of a path containing priority
one would relate `e` to itself via the full cycle and would not admit
a strict ordinal ranking.

The correct threshold relation `R_1` contains `o R_1 e`, but cannot
continue through `e` as an edge source. Its ranks are

\[
 r_1(e)=0,\qquad r_1(o)=1.
\]

The priority-one edge strictly decreases this rank. The priority-zero
edge resets it from zero to one; its required odd-priority prefix is
empty, so that reset is allowed.

### A later coordinate can rise when an earlier one falls

On the cycle `u -> v -> w -> u`, let the priorities be respectively
`1,3,0`. The construction gives

\[
 r(u)=(1,0),\qquad r(v)=(0,1),\qquad r(w)=(0,0),
\]

with coordinates ordered `(1,3)`. The source-priority-one edge decreases
the first coordinate while increasing the later coordinate. The
source-priority-three edge decreases the second, and the source-priority-zero
edge is unrestricted. Every infinite path is good because zero recurs.
This explicitly exhibits the permitted reset behavior of the full tuple.

### Arbitrary branching can require a genuinely transfinite value

Let the vertices be a root `r`, a terminal `t`, and `(n,k)` for natural
numbers `n >= 1` and `1 <= k <= n`. Put edges

\[
 r\to(n,n),\quad
 (n,k)\to(n,k-1)\ (k>1),\quad
 (n,1)\to t.
\]

Give `r` and every `(n,k)` priority one, and give `t` priority zero.
Every path is finite, so the infinite-path hypothesis holds. Strictness
on each priority-one edge forces

\[
 r_1(n,k)\geq k,\qquad r_1(r)\geq n+1\text{ for every }n.
\]

No finite natural rank at `r` can suffice. The recursive construction
gives exactly `r_1(t)=0`, `r_1(n,k)=k`, and `r_1(r)=omega`. Thus the
ordinal formulation is substantive even on a countable graph in which
all paths terminate.

For comparison, if `V` is finite with `N >= 1`, each well-founded relation
`R_j` has a natural-valued rank at most `N-1`: the rank is the maximum
length of an `R_j` chain, which cannot repeat a vertex. This finite case
does not justify replacing ordinals by naturals for arbitrary branching
on an infinite graph.

## 6. Premodel-use boundary

The tuple coordinates are indexed by the odd priorities actually present,
in increasing order. Their comparison uses the priority of the **source**
of each edge, exactly as in the requested statement. Terminal vertices
require no special positive rank, since there is no outgoing edge on
which strictness must be imposed.

If an application assumes only that paths from a distinguished root are
good, first restrict to the vertices reachable from that root. Bad
unreachable components need not admit such ranks. If every infinite path
in the whole graph is assumed good, as in this note, the construction
applies to all vertices directly.

Connecting this graph theorem to premodel trace or game obligations,
and verifying any finite terminal requirements of that application,
remain separate tasks. The ordinal-signature equivalence itself is
proved here in both directions, with no finite-branching assumption.

Only this proof note was created. No manuscript edits, code, tests,
builds, renders, or additional agents were used.
