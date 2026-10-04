# Kozen consistency to nonrejection: a proved decorated-context bound

Date: 2026-09-06.

## Outcome and exact scope

The original threshold `N = 2^m`, where `m = |p0|`, is **not repaired by
this investigation**. A distinct result is proved below: the repaired
local consistency annotations exclude repeated **higher-identity
context signatures** at increments of a surviving counter, including
across modal steps. There are at most

\[
 M=2^m(m^2+1)^{m^2}
\]

such signatures in one reset-free interval. Consequently the tableau
with the explicitly changed overflow threshold `M` preserves consistency
and does not reject a consistent root. Its configuration encoding is
still polynomial and its finite safety computation is still exponential
time. This is a supplied alternative bound, not Kozen's stated bound,
not a claim that changing that bound is necessary, and not a proposal
silently adopted in the manuscript.

There is also an exact original-threshold special case: if every
higher-priority annotation is `1` throughout the interval, at most
`2^(m-1)` increments of the counter are possible there. In particular,
the original threshold excludes overflow of a highest-priority counter
in the consistency-selected tableau.

Source basis: Kozen's [author-hosted primary scan](https://www.cs.cornell.edu/kozen/Papers/mu.pdf),
printed pp. 343--349, especially equations (6.1.6)--(6.1.13) and
(6.3.2)--(6.3.15). The local copy of printed pp. 348--349 was visually
inspected for this investigation. The original source's equality
(6.3.14) is not used as an established lemma. The definitions and local
repair are those recorded in the final correction section of
`spec/research/p09-kozen-1983-source-note.md`; this note supplies a new
counting argument, rather than retranscribing the article.

## Definitions before counting

The input `p0` is closed, aconjunctive and positive-normal, with uniquely
named bound variables. Put `m = |p0| >= 1`. Let `Q` be the finite family
of raw subformulas used in the tableau, so `|Q| <= m`. Each raw formula
`p` has a fixed ordered active-variable list `A_p`; let `k_p` be the
number of its active mu-variables. Therefore

\[
 \sum_{p\in Q} k_p\leq m^2.
\]

A mu-counter is an identity, not just its variable and numerical value.
Distinct identities can belong to the same variable. At each node,
mu-identities occur in exactly one local formula list, and the global
priority order `G` is a shuffle of these lists. There are at most
`K = m^2` live mu-identities. Nu-identities can be shared; their flags
do not occur in the closing translation defined next.

For a live mu-identity `d`, its proof annotation `r(d)` is a closed
formula. To translate a raw `p`, replace an active mu-variable `Y`
whose local identity is `d` by

\[
 \mu Y.(r(d)\land b_Y),
\]

where `mu Y.b_Y` is its raw binder; make the other replacements by the
original binding formulas. Use the fixed ordered closing substitution,
not simultaneous substitution. Write the resulting closed formula as
`e'(s,p)` and the conjunction of the translated node label as `E_s`.
The conjunction of an empty family is `1`.
For comparing signature translations, use a fixed hygienic renaming
convention and simplify an annotation `1 and b_Y` to `b_Y`. These are
provable equalities, so they do not change consistency or any displayed
formula inequality.

New annotations are `1`. Inheritance keeps them unchanged. Every
numerical reset of a surviving mu-counter sets its annotation to `1`,
including resets caused by deletion. Discarding a counter discards its
annotation. At a mu-variable increment use the inherited-old-context
update below, before incoming-body collision disposal. These are proof
annotations only; the actual tableau need not store or compute them.

## Local lemma, valid for any finite overflow threshold

Suppose the raw variable `X` is unfolded at `s`, and its counter is `c`.
Let `R = r(s,c)`. Before inserting its body, keep each inherited old
occurrence `p != X` with its own old local list. In those lists retain
annotations of identities strictly higher than `c` and set lower ones
to `1`. Define

\[
 D_s=\bigwedge_{p\in\Gamma_s\setminus\{X\}}
       \widehat e_s(p;C(s,p)).                 \tag{1}
\]

Counter `c` belongs only to the old occurrence `X`, so (1) is independent
of its new annotation, even if the raw body of `X` is already an old
formula. In particular the old body occurrence is not translated with
the incoming body's provisional list.

Close the outside parameters of the `X` occurrence using their
inherited annotations, obtaining `b'(X)`. Positivity and fixed-point
monotonicity give

\[
 E_s\leq D_s\land\mu X.(R\land b'(X)).       \tag{2}
\]

Both `D_s` and `R` are closed. If `E_s` is consistent, the right side of
(2) is consistent. Apply the previously derived consistency consequence
of Proposition 5.7(vi) with `F(X) = R and b'(X)`. After dropping the
outer conjunct `R`, the formula

\[
 L_s=D_s\land
 b'(\mu X.(R\land\neg D_s\land b'(X)))       \tag{3}
\]

is consistent. Set the incoming `c` annotation to `R and not D_s`.
The conjunction in (3) is exactly the translation of the temporary
decorated successor family, keeping both the inherited and incoming
occurrences when the raw body collides with an old formula.

Actual collision disposal removes conjuncts from this temporary family.
Whichever list the priority rule retains, removing the other occurrence
weakens its conjunction. Subsequent deletion resets replace affected
annotations by `1`, again weakening the conjunction by positivity and
fixed-point monotonicity. Nu-only maximum collisions change no argument
of the closing translation. Thus

\[
 L_s\leq E_{s+},
\]

and the completed successor is consistent. If `c` is reset or discarded
at this collision, its new constraint disappears with that reset or
disposal, as required; nothing in the lemma retains a deleted history.

For completeness, the other local rules need no recurrence hypothesis.
Before collision disposal, a Boolean conjunction splits into its exact
two translated conjuncts; the two disjunctive successors have a union
whose disjunction is the translated parent. Hence some disjunctive
successor is consistent. A binder opening with new annotation `1`, or
a permitted nu-variable step, uses the appropriate fixed-point
equation. For each diamond successor, the modal axioms imply that the
translated parent entails the diamond of the temporary successor
conjunction; that conjunction cannot be derivably `0` if the parent is
consistent. Collision disposal and resets then weaken each temporary
family as above. Literal clashes and raw `0` are inconsistent.

These arguments construct a root-containing set `B` of consistent
annotated nodes, choosing at least one disjunctive successor and all
other required successors. The numerical overflow condition has not
yet been excluded. No semantic completeness theorem is used here.

## The fixed higher family in a reset-free interval

Fix a surviving counter `c` and an interval during which it is not
reset. Include the predecessor of each increment being counted. Let
`H` be the identities strictly higher than `c` at the beginning of the
interval, and let `h = |H|`.

The identities in `H`, their relative priorities, and their annotations
are fixed throughout the interval. Indeed:

1. Births are appended, hence cannot introduce a new identity above `c`.
2. Deletion above `c` changes its position and would reset it.
3. An increment above `c` resets it.
4. A reset above `c` must be caused by an even earlier increment or
   deletion, which also resets `c`.

Therefore none of those events occurs. Their holders can nevertheless
change. In particular this argument does not infer fixed local lists
or fixed translated contexts from the fixed family `H`.

At an increment predecessor `s`, the variable of `c` is a fixed raw
`X`, and `X in Gamma_s`. Define its context signature as follows.

- For each `p in Q \ {X}`, record either `absent` or `present`.
- In a present formula, for each of its `k_p` active-mu positions,
  record the identity `d in H` occupying that position, if any; otherwise
  record the symbol `*`.

Here `*` means the ordinary, unannotated mu-binding formula, since every
counter not in `H` is assigned annotation `1` for (1). The signature
does not record nu-flags, lower identities, or lower numerical values.
It does not quotient or modify the actual tableau configuration.

**Signature lemma.** Within this interval, equal signatures give equal
formulas `D_s` up to a fixed hygienic bound-variable renaming.

Proof. The raw formula determines its ordered enclosing-variable and
active-variable positions. A recorded `d` selects the same fixed closed
annotation `r(d)` at both nodes; `*` selects the original binding
formula. Inactive positions and all nu-binding replacements are already
fixed by the raw syntax. Thus every term of the ordered substitution is
determined by the signature, as is their order. The presence bits
determine the same conjuncts in (1). No intervening tableau step, modal
or otherwise, enters this argument. QED.

## New recurrence lemma across arbitrary modal intervals

**Lemma.** Two increment predecessors `u < v` for the same surviving
`c`, with no reset of `c` between them, cannot have equal context
signatures if every node in question belongs to `B`.

Proof. At `u` the update adds `not D_u` to `r(c)`. Its increment survives
without reset or deletion, so that conjunct remains in `r(v,c)`.
At `v`, equation (2) gives `E_v <= D_v`. The translated raw `X`
conjunct is a least fixed point with body conjoined with `r(v,c)`;
unfolding gives

\[
 E_v\leq r(v,c)\leq\neg D_u.                \tag{4}
\]

Equal signatures give `D_v = D_u` by the signature lemma. Together
with (4), this yields `E_v <= D_u and not D_u = 0`, contradicting its
consistency. QED.

This proof compares two formulas at their own increment predecessors;
it never transfers a formula inequality through a modal transition.
It allows every higher identity to change holders arbitrarily between
the two endpoints. It is therefore a genuine cross-modal lemma, but
its pigeonholes are richer than raw labels.

## Explicit counting and the alternative threshold

For each raw `p != X`, the number of possible signature records is at
most `1 + (h+1)^(k_p)`: one absence record, or one of the positionwise
choices among `H` and `*`. Variable compatibility, uniqueness of
mu-identities, and active-prefix restrictions only reduce that bound.
Thus the number of signatures satisfies

\[
\begin{split}
 T(H,X)
 &\leq\prod_{p\in Q\setminus\{X\}}(1+(h+1)^{k_p})\\
 &\leq 2^{|Q|-1}(h+1)^{\sum_{p\ne X}k_p}\\
 &\leq 2^{m-1}(m^2+1)^{m^2}<M.
\end{split}                                                   \tag{5}
\]

All quantities in (5) count syntactic signatures; formulas `r(d)` may
be large, but they are fixed parameters here, not extra choices.

If a completed configuration has `c = M+1`, the counter has undergone
`M+1` surviving increments since its last reset. Choose their
predecessors. A higher-family `H` is fixed on this whole interval.
By (5), two predecessors have equal signatures, contrary to the
recurrence lemma. Thus no node of `B` has a counter above `M`.
Literal rejection is already impossible by the local lemma.

Finally a finite rejection derivation cannot contain a root in `B`:
at an existential/disjunction rejection both successors reject,
contradicting the selected successor by induction; at any universal
rejection some required successor rejects, contradicting that all
required successors lie in `B`. Therefore the changed-threshold
algorithm does not reject a consistent root. This argument uses
finite rejection ranks, not an assumption that every tableau branch
halts.

## What is proved for the original threshold

If `r(d) = 1` for every `d in H`, the annotations at the higher positions
also disappear. Consequently

\[
 D_s=\bigwedge_{p\in\Gamma_s\setminus\{X\}}e(p),
\]

independently of all identity attachments. There are at most
`2^(|Q|-1) <= 2^(m-1)` such contexts. The same recurrence proof, now
pigeonholing raw labels alone, excludes more than that many increments
in this interval. This includes `H` empty, hence highest-priority
overflow is impossible at the original threshold `N = 2^m`.

For a general lower-priority `c`, (5) does not imply `T(H,X) <= 2^m`.
No argument here bounds the number of *consistent reachable* signatures
by `2^m`, or supplies a coarser at-most-`2^m` context order that forces
one recorded `D_u` at a later increment. One of those additional
results, or a different proof at the same numerical threshold, remains
necessary for the exact source algorithm. The phase-swapping objection
to raw-label recurrence is neither ignored nor turned into a claim
that the source theorem or threshold is false.

## Exact change, correctness transfer, and complexity of the alternative

The sufficient alternative changes exactly the overflow threshold from
`2^m` to the displayed integer `M`. Raw labels, rule scheduling,
active-variable lists, mu-priority comparisons, nu-sharing/maximum
flags, collision origins, deletion resets, and the completed-
configuration overflow convention are unchanged. The annotations and
signatures above are used in the proof, not added to the algorithm.

The nonrejection-to-model construction already supplied in
`handbook/parts/p09/presentations/n-c-018.tex` depends on the numerical
threshold only through its finiteness and the counter range. In that
argument replace `N` by `M`: a fixed prefix has at most `(M+1)^K`
lexicographic value vectors; an identity has at most `K` constant-rank
intervals; a collision continuation traverses at most `K` identities.
Hence a uniform finite continuation bound still exists. Nonmodal
saturation, the rank translations, their six saturation conditions,
the truth lemma and finite-configuration quotient are unchanged.
Together with deductive soundness, this preserves both directions of
the consistency/nonrejection/finite-model equivalence for this
alternative. This is a dependency-level transfer of the separately
supplied model proof, not a fresh independent review of that proof.

Numerically,

\[
 \log_2 M=m+m^2\log_2(m^2+1)=O(m^2\log(m+1)).
\]

At most `m^2` mu-values therefore occupy
`O(m^4 log(m+1))` bits altogether; raw formulas, list references,
nu-flags/sharing and priority order require no larger bound. The
threshold itself has a polynomial-size binary representation and is
computable by elementary polynomial-bit integer arithmetic. There are
at most `2^(O(m^4 log(m+1)))` normalized configurations; each has at
most `m` successors, generated from its finite rule data. The greatest
fixed point of the ordinary safe-configuration operator can be
computed by descending deletion on this finite graph in time
`2^(O(m^4 log(m+1)))`. Thus the proved alternative remains an
exponential-time decision procedure. This does not recover the
source's sharper particular bound or the manuscript's `O(m^3)`
configuration estimate for its unchanged original threshold.

## Handoff boundary

This investigation changed only this research note. It did not change
the manuscript or a tableau implementation, adopt the alternative
threshold, create code, run software tests or builds, or render the
manuscript. The completed new results are the signature recurrence
lemma, its explicit finite bound, the original-threshold highest-
priority special case, and the precisely delimited larger-threshold
alternative. The original global `consistency -> nonrejection` claim
at `N = 2^m` remains open in this supplied reconstruction.

## Subsequent manuscript incorporation

Later in the same 6 September writing continuation, the root author
incorporated the M-cap construction into the actual manuscript at
sec:p09-kozen-context-completeness. The procedure is now explicitly
parameterized by a finite cap, with the N source presentation and M
context-counted proof distinguished. Only the numerical threshold differs;
the raw formula keys, structural rules and collision conventions are
unchanged. The reader-facing result is the proved consistency /
M-nonrejection / finite-directed-model equivalence with the larger explicit
exponential bounds. It does not claim the original N-bound recurrence.

Before incorporation, a separate bounded mathematical reader checked this
note against the local rules, ordered closing substitution and existing
model construction. No substantive defect was found. The requested
explicitness changes were incorporated: raw formula keys distinguished
from game occurrences; fixed conjunction enumeration; closed formula
values rather than dynamic annotation references; and explicit finite-cap
dependence of the identity, continuation and configuration bounds.

The same reader then checked the actual LaTeX insertion. Its requested
definition bridge now explicitly quotients occurrences to raw formula keys
and proves representative independence of the active lists and closing
translations. The counter-entry count and theorem's full standing
hypotheses were clarified. A final bounded rereading confirmed these repairs.
The earlier handoff boundary describes the investigation's own actions;
this later addition records the actual subsequent manuscript change.
