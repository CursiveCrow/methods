# TATA WSkS encodings: canonical trees and projection with pruning

Date: 2026-09-06.

## Outcome

The current N-c-015 description needs two explicit ingredients to make
its logical induction correct as a construction of languages of canonical
codes:

1. A regular well-formedness language `W_n` of canonical `n`-track codes,
   used to restrict atomic automata and complements.
2. Projection as the arity-changing, child-erasing homomorphism of TATA
   Proposition 3.2.12, not simple label erasure with the tree shape fixed.

For this particular encoding, erasing a coordinate turns a node into a
nullary all-bottom symbol exactly when its surviving tracks are empty
throughout that subtree. The entire subtree must then be pruned. No
additional replacement of surviving zeros by bottoms is needed when the
input has already passed the canonical-code check.

The source calls this operation a linear tree homomorphism. It does not
state a separate padding-quotient theorem in Section 3.3. The explicit
well-formedness checker and projected-automaton construction below supply
the details needed by the handbook's proof.

## Primary version and checked passages

The primary is *Tree Automata Techniques and Applications*, release dated
18 November 2008, cited in the handbook as `ComonEtAl2007`.
The local body exists at
`tmp/pdfs/p09-tata-2008/tata-2008.pdf`; the bibliography's institutional
record is [HAL hal-03367725](https://inria.hal.science/hal-03367725).
This pass read the local PDF text and existing source images for Figures
3.7-3.11. No manuscript render was used.

| Printed pages | Physical PDF pages | Primary content |
|---|---|---|
| 76 | 77 | Tuple coding by overlapping component trees, Definition 3.2.1. |
| 80-81 | 81-82 | Relative relation operations; Definitions 3.2.10-3.2.11; projection/cylindrification in Proposition 3.2.12. |
| 87-90 | 88-91 | WSkS syntax/semantics and translation to finite-set variables, Proposition 3.3.1. |
| 90-91 | 91-92 | Canonical finite-set code, Definition 3.3.2 context and Example 3.3.3/Figure 3.7. |
| 91-93 | 92-94 | Lemma 3.3.4, Figures 3.8-3.11, and Boolean/projection induction. |
| 95 | 96 | Theorem 3.3.8 and the sole-nullary-symbol convention for no free variables. |

The active presentation read is
`handbook/parts/p09/presentations/n-c-015.tex`, label
`sec:p09-presentation-n-c-015`. Its current base example and six subset
transition rules match the source; the absent code guard and the
unspecified pruning in projection are the substantive completion points.

## 1. Canonical encoding, including the empty assignment

Fix `k >= 1` and let `K={1,...,k}`. For `n >= 1`, the ranked alphabet
is

\[
\Sigma_n=\{0,1,\bot\}^n.
\]

The symbol `bottom_n=(bot,...,bot)` has arity zero, and every other
symbol has arity `k`. The track alphabet is not ranked coordinatewise
with a fixed arity after projection: its vector's arity depends on
whether any coordinate is non-bottom.

For finite sets `S_1,...,S_n subseteq K*`, put

\[
U=\bigcup_{j=1}^nS_j,\qquad
\operatorname{Pref}(U)=\{p:\exists u\in U\ (p\preceq u)\}.
\]

The exact position domain of the code is

\[
D(\bar S)=\{\epsilon\}\cup
\{pi:p\in\operatorname{Pref}(U),\ i\in K\}.
\tag{1}
\]

At a position `p`, coordinate `j` of its label is

\[
\alpha_j(p)=
\begin{cases}
1,&p\in S_j,\\
0,&p\notin S_j\text{ and some strict extension of }p\text{ lies in }S_j,\\
\bot,&\text{no extension of }p\text{ lies in }S_j.
\end{cases}
\tag{2}
\]

The strict-extension phrasing in the middle case follows from the
source's nonmembership condition and its prefix-extension condition.
Every node in `Pref(U)` is internal; its complete family of `k`
children is present even when some child has no set element below it.
These children are the nullary padding leaves in (1). Thus (1) is
more than just the set of prefixes of members of `U`: it also contains
the one-step padding boundary.

If all sets are empty, `Pref(U)` is empty and the unique code is the
one-node tree `bottom_n`. No chain of zero nodes is part of that code.

Decoding reads `S_j={p:alpha_j(p)=1}`. Canonicality means that the
labels and position domain satisfy exactly (1)-(2), so this decoding
has the displayed code as its unique inverse.

## 2. A finite automaton for the canonical-code language W_n

Let `W_n` be the image of the canonical coding. A partial deterministic
bottom-up checker has states `H subseteq {1,...,n}`. The intended
meaning of `H` at a subtree is the set of tracks with at least one
membership mark `1` somewhere in that subtree.

The nullary rule is

\[
\bot_n\longrightarrow\varnothing.
\]

For an internal label `alpha != bottom_n` and child states
`H_1,...,H_k`, put `H=union_l H_l`. Permit a transition exactly when
each coordinate satisfies

\[
\begin{array}{ll}
\alpha_j=\bot&\Longrightarrow j\notin H,\\
\alpha_j=0&\Longrightarrow j\in H,\\
\alpha_j=1&\text{imposes no further child condition}.
\end{array}
\tag{3}
\]

Its target is `H union {j:alpha_j=1}`. Every checker state is final;
an invalid local combination has no transition. A total version may
add a rejecting sink, but the partial version is sufficient here.

Induction on subtrees proves the state's intended support meaning.
Condition (3) says exactly that bottom forbids later membership,
zero requires later membership, and one records membership now.
Every internal node therefore lies above some `1` in at least one
track. Conversely, a canonical code satisfies each local clause.
Since the ranked alphabet supplies all `k` children at an internal
node and only the all-bottom vector is nullary, these conditions also
force the position domain (1). Thus the checker recognizes exactly
`W_n`.

For example, in the binary two-track alphabet,

\[
00(\bot\bot,\bot\bot)
\]

is rejected: each zero claims a descendant membership mark, but neither
child has one. The source's one-state subset automaton accepts this
tree, demonstrating why that atomic transition table by itself is not
an exact recognizer of canonical assignment codes.

## 3. Example 3.3.3 checked completely

For `k=2`, `S_1={epsilon,11}`, `S_2=empty`, `S_3={11,22}`, the
nonpadding positions and labels are

| Position | Label |
|---|---|
| `epsilon` | `(1,bot,0)` |
| `1` | `(0,bot,0)` |
| `2` | `(bot,bot,0)` |
| `11` | `(1,bot,1)` |
| `22` | `(bot,bot,1)` |

The six padding leaves are exactly

\[
12,\ 21,\ 111,\ 112,\ 221,\ 222,
\]

each labelled `(bot,bot,bot)`. There are eleven positions in total.
This agrees with the actual Figure 3.7. The existing manuscript's
listed labels are correct; giving this complete domain makes its
padding convention explicit.

## 4. Atomic recognizers

The source's Figures 3.8-3.11 display binary automata. The following
formulas state the general `k`-successor versions. In every case, when
used over a larger free-variable list, lift by the normalized
projection/inverse-image operation of Section 6 and intersect `W_n`.

### Inclusion X subseteq Y

For two distinct variables in track order `(X,Y)`, the source has one
final state `q` and, for `k=2`, exactly

\[
\bot\bot\to q,\quad
00(q,q)\to q,\quad01(q,q)\to q,\quad11(q,q)\to q,\quad
\bot0(q,q)\to q,\quad\bot1(q,q)\to q.
\]

For general `k`, use the same five nonnullary labels with `k` children
all in `q`. Intersect this language with `W_2`.

If `X subseteq Y`, every prefix of a member of `X` is a prefix of a
member of `Y`. Thus a non-bottom X-track cannot face a bottom Y-track,
and every X membership mark must face a Y membership mark. Precisely
the displayed labels remain possible. Conversely, a canonical accepted
code has no `10` or `1bot` label, so every member of `X` is a member
of `Y`. The extra excluded label `0bot` is impossible on canonical
codes of a genuine inclusion, although it tests support rather than
current membership.

The sentence that the absent labels are incompatible with inclusion
must be read under this canonical-code hypothesis. It is not a
standalone characterization of well-formed tuples.

### Sing(X)

Use states `q,q'`, with only `q'` final:

\[
\bot\to q,\qquad 1(q,\ldots,q)\to q',
\]

and, for each child position `i`, a rule with label `0`, child `i`
in `q'`, all other children in `q`, and target `q'`.
State `q` is possible only on the empty code; a `q'` run follows
one zero-labelled prefix path to one membership node. Thus it accepts
exactly singleton codes. These are exactly Figure 3.8's rules when
`k=2`.

### X=Yi

The singleton interpretation is explicit in Section 3.3.4, printed p. 89,
and the converse translation on printed p. 90 is

\[
\operatorname{Sing}(X)\land\operatorname{Sing}(Y)\land
\exists x\exists y\,(x\in X\land y\in Y\land x=yi).
\]

It is not the whole-set shift equation `X={wi:w in Y}`. For example,
`X=Y=empty` satisfies that whole-set equation but makes TATA's atom
false. The manuscript's unique-word reading should be retained.

The atom requires distinct singleton sets `X={yi}` and `Y={y}` for
some word `y`. In track order `(X,Y)`, use states `q,q',q''`, only
`q''` final. The rules are

\[
\bot\bot\to q,\qquad 1\bot(q,\ldots,q)\to q',
\]

one `01` rule with child `i` in `q'`, the other children in `q`, and
target `q''`; and `00` rules with exactly one child in `q''`, all
other children in `q`, and target `q''`.

The `01` node is the Y membership position. Its `i`-child, labelled
`1bot`, is the X membership position. The `00` rules allow any common
prefix above that pair; every other branch is empty. This proves
exactly the required singleton successor relation and reproduces
Figure 3.10 for `i=1,k=2`.

### X=epsilon

Use `bot -> q` and `1(q,...,q) -> q'`, with `q'` the only final
state. No zero-propagation rule is present. The only accepted code
represents `{epsilon}`, as in Figure 3.11.

### Repeated variable names and first-order variables

If an atomic expression uses the same variable in both positions,
`X subseteq X` is true on all `W_1`, while `X=Xi` is false: no finite
word equals its proper one-letter successor. Coordinate order can be
permuted for distinct variables. Set equality is the conjunction of
two inclusions.

Proposition 3.3.1 guards quantified first-order variables by `Sing`
and also adds singleton guards for free first-order variables after
the recursive translation. These guards preserve the original
word-valued assignment domain; an arbitrary finite set is not itself
an encoding of a first-order value.

## 5. Projection includes rank reduction and pruning

Let `d_j(alpha)` remove coordinate `j` from an `n`-track symbol,
leaving `m=n-1 >= 1` tracks. Define a map on trees by

\[
h_j(\bot_n)=\bot_m,
\]

and for an internal source node

\[
h_j(\alpha(t_1,\ldots,t_k))=
\begin{cases}
\bot_m,&d_j(\alpha)=\bot_m,\\
d_j(\alpha)(h_j(t_1),\ldots,h_j(t_k)),&d_j(\alpha)\ne\bot_m.
\end{cases}
\tag{4}
\]

The first branch erases all children, because the projected symbol
has arity zero. This is the exact specialization of Proposition
3.2.12's homomorphism: the source retains only as many child images
as the projected symbol's arity.

For canonical input,

\[
h_j(\operatorname{code}(S_1,\ldots,S_n))
=\operatorname{code}(S_1,\ldots,S_{j-1},S_{j+1},\ldots,S_n).
\tag{5}
\]

To prove (5), if every surviving coordinate is bottom at a node,
the local code condition says there is no membership in any surviving
track below it. The projected code has only a padding leaf there.
Otherwise some surviving set has a member at or below the node, so
the node remains internal and the same argument applies to its
children. A surviving zero still has a surviving descendant one
in that same track, so there is no further zero-to-bottom operation.

For a concrete failure of shape-preserving relabeling, take retained
`X=empty` and deleted `Y={1}`. Its code has an internal root labelled
`(bot,0)`. After deleting Y, the surviving label is bottom and must
be a leaf, so the correct output is the one-node empty-set code.
Keeping the old children either violates the ranked alphabet or keeps
a padded noncanonical representative. Intersecting such padded output
with `W_1` would discard the legitimate empty assignment.

## 6. Explicit automaton construction for the pruned image

Suppose `A=(Q,Sigma_n,F,Delta)` recognizes a language contained in
`W_n`; the logical induction below enforces this invariant. Compute
the finite set `E subseteq Q` of states attainable by trees whose
surviving coordinates are all bottom at every node. These are the
subtrees supported entirely by the deleted track.

Compute `E` as the least set containing every target of a nullary
`bottom_n` rule and closed under old transitions

\[
\alpha(q_1,\ldots,q_k)\to q
\]

for which `d_j(alpha)=bottom_m` and every `q_l in E`. This is a
finite reachability calculation restricted to these labels.

The projected automaton retains `Q` and `F` and has:

1. `bottom_m -> q` for every `q in E`;
2. `d_j(alpha)(q_1,...,q_k) -> q` for every old internal transition
   with `d_j(alpha) != bottom_m`.

For completeness, take an accepted canonical input. At every pruned
subtree its surviving coordinates are bottom throughout, so the old
subtree-root state lies in `E` and is available at the new leaf.
All retained internal transitions are present by clause 2. Thus its
canonical projection is accepted.

For soundness, induct on a projected run. A new bottom leaf uses a
state in `E`, so choose an old finite subtree witnessing that state.
A retained internal transition combines the child witnesses using
the old transition from which it came. This constructs an old tree
accepted by `A`, with the projected tree as its image under (4).
Since `L(A) subseteq W_n`, the reconstructed accepted tree is canonical;
(5) shows that its projected tree is also canonical and represents
exactly the surviving assignment. Therefore this automaton recognizes
`h_j(L(A))` with no unwanted padding representatives.

This supplies the state-level normalization operation. It is not
the unsupported instruction to relabel transitions whose symbol
arity has changed.

### Cylindrification

For an automaton over a selected subset of variables, let `h` be the
successive normalized projections dropping all other coordinates.
Its lifted language on the larger variable list is

\[
W_n\cap h^{-1}(L(A)).
\tag{6}
\]

This is the inverse-homomorphic operation cited by Proposition 3.2.12.
For an explicit implementation, first make the smaller-coordinate
automaton deterministic and total. At an input node where `h` retains
the projected symbol, evaluate its corresponding transition on the
child states. Where `h` collapses the subtree to a nullary padding
symbol, assign the smaller automaton's state for that nullary symbol,
independently of the child states. Intersect with `W_n`.
This correctly allows the new tracks to extend beyond the original
tree shape.

More explicitly, for a larger `m`-coordinate alphabet and a retained
`n`-coordinate alphabet with `m>n>=1`, write `beta(alpha)` for the
retained coordinates of a label `alpha`. If `delta` is the total
deterministic transition function of the smaller automaton, use

\[
\delta'(\alpha,q_1,\ldots,q_k)=
\begin{cases}
\delta(\bot_n),&\beta(\alpha)=\bot_n,\\
\delta(\beta(\alpha),q_1,\ldots,q_k),&\beta(\alpha)\ne\bot_n.
\end{cases}
\]

At an input padding leaf, use `bottom_m -> delta(bottom_n)`.
Induction on the input tree says that its lifted state is exactly
the original automaton's state on the pruned image `h(t)`. In the
collapsed case, no child image is part of `h(t)`, explaining why
the fixed nullary-transition state ignores every child state.
For `n=0`, replace this fixed state by `delta(top)` at every node.
Intersecting with `W_m` then proves the variable-alignment claim on
canonical assignments. Totality matters: rejected child images still
receive states, so they cannot prevent an enclosing collapsed node
from taking its correct fixed state.

The generic finite-tree determinization, intersection, and reachability
proofs are outside this note; only their encoding-specific uses are
specified here.

## 7. The logical induction and the no-free-variable case

Maintain the exact invariant

\[
L(A_\phi)=
\{\operatorname{code}(\bar S):\bar S\models\phi\}
\subseteq W_n,
\tag{7}
\]

where `n` is the number of distinct free set variables in a fixed
order. Rename bound variables first so their occurrences are unambiguous.

- Atomic automata are the preceding constructions intersected with `W_n`.
- For disjunction, lift both operands by (6) to the union of their
  free-variable lists and take union.
- For negation, use relative complement `W_n\L(A_phi)`. An ordinary
  complement over all ranked trees must be intersected with `W_n`.
- For `exists X phi`, use the pruned image construction for X's track.
  Every preimage witness is a finite canonical code and hence a finite
  set assignment; every finite witness assignment supplies a preimage.
  If X is not free in `phi`, the quantifier is vacuous because the
  finite-set domain is nonempty, and the automaton is unchanged.

For zero free variables use the explicit source convention

\[
\Sigma_0=\{\top\},\qquad \operatorname{arity}(\top)=0,
\qquad W_0=\{\top\}.
\]

This is the unique empty tuple, not an actually empty ranked alphabet.
Definition 3.2.10 already makes `T(F)^0` a singleton, and Theorem
3.3.8 repeats the sole-nullary-symbol convention.

Deleting the last track maps every input tree to `top`. In the
automaton construction, `E` is then the set of all reachable states,
and the output consists of the rules `top -> q` for `q in E`.
It accepts `top` exactly when an old accepting code existed.
Cylindrifying a closed true formula gives all `W_n`; cylindrifying
a false one gives the empty language. Complement at level zero
exchanges the two languages `empty` and `{top}`.

Thus a closed sentence is true in the fixed WSkS structure exactly
when `top` is accepted, equivalently when the resulting bottom-up
automaton has a nullary rule `top -> q_f` with `q_f` final. This
uses the normalized last-track projection, so arbitrarily deep
finite witnesses are included rather than lost as padding.

## Required incorporation changes

The live N-c-015 should state the exact domain (1), define `W_n`,
and require the language invariant (7). Its existing subset rules
may be retained with the canonical-code guard. Supply the other
atomic constructions and the complete Example 3.3.3 padding list.
Replace the bare projection sentence by (4)-(5) and the state
construction through `E`, and make complements relative to `W_n`.
State the zero-variable alphabet directly as `{top}`.

These changes give a complete encoding/projection argument while
retaining TATA's actual finite-set code and its arity-erasing source
projection. No separate padding quotient is being attributed to the
source where it does not state one.

Only this proof note was authored. No handbook edits, software tests,
manuscript builds, or manuscript renders were performed.
