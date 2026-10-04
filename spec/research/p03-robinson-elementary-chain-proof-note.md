# Robinson joint consistency by elementary diagrams and an alternating chain

Date: 2026-09-06.

## Exact statement and hypotheses

Work in classical set theory with the Axiom of Choice. All signatures,
theories, structures, and their domains are sets; domains are nonempty.
Signatures may have arbitrary set cardinality and may contain constants,
positive-arity function symbols, relation symbols of any finite arity,
and logical equality interpreted as identity.

Let `L_1,L_2` have compatible symbol kinds and arities on their overlap,
and let `L_0=L_1 intersect L_2`. Let `T_i` be a syntactically consistent
first-order `L_i`-theory. Suppose no `L_0`-sentence `sigma` satisfies

\[
T_1\vdash\sigma\quad\text{and}\quad T_2\vdash\neg\sigma.
\tag{R}
\]

Then `T_1 union T_2` has an `(L_1 union L_2)`-model and is consistent.
The proof below first finds one complete common theory and then uses
an alternating elementary chain. It does not use the Keisler-Shelah
ultrapower theorem, general saturation, or an amalgamation theorem.

## Active manuscript dependencies and routes

The current body statement is
`thm:p03-robinson-joint-consistency` in
`handbook/parts/p03/preservation-abstract-logic.tex`, section
`sec:p03-robinson-joint-consistency`. Its proof target is
`annex:p3.abstract.1` in `handbook/annex/p03/editorial-proofs.tex`.
The Part III body and annex drivers input these files.

The old proof read for this task first uses compactness of the Stone
space to find a common complete theory, then invokes isomorphic
ultrapowers. The present note supplies the requested elementary-diagram
replacement. Its initial common-theory argument can also replace the
Stone-space step.

The live definitions and theorems needed for the replacement are:

| Stable label | Active reader file | Content |
|---|---|---|
| `def:parameter-expansion` | `handbook/restoration/inherited-06332-06421.tex` | Fresh distinct constants naming a specified parameter set. |
| `def:diagrams` | same | `ElDiag_L(A)=Th_{L(A)}(A_A)`, the complete elementary diagram. |
| `thm:diagram-tests` | same | Models of the elementary diagram give elementary embeddings; equality inequalities ensure injectivity, and diagram atoms preserve functions and relations. |
| `thm:elementary-chain` | `handbook/restoration/inherited-06432-06493.tex` | Every stage of a compatible elementary chain is elementary in its union. |
| `thm:fol-compactness` | `handbook/restoration/inherited-04921-04967.tex` | Arbitrary-language compactness, including finite consequence, with the stated Choice hypothesis. |
| `thm:fol-completeness` | `handbook/restoration/inherited-04713-04920.tex` | Semantic consequence and syntactic derivability, with Choice for arbitrary signatures. |

`handbook/parts/p03.tex` routes the relevant restoration wrappers for
`06332-06421` and `06432-06493` near its beginning. The older labels
`thm:p03-diagram-tests` and `thm:p03-elementary-chain` in retained
`maps-elementarity.tex` are not the active inherited theorem identities.
The active proof should cite `thm:diagram-tests` and
`thm:elementary-chain`.

## 1. Obtain a common complete theory from the stated hypothesis

Let

\[
C=\{\sigma\in\operatorname{Sent}(L_0):T_1\vdash\sigma\}.
\]

The `L_2`-theory `T_2 union C` is consistent. Otherwise a finite
`C_0={sigma_1,...,sigma_n}` would already make it inconsistent.
Let `sigma=and C_0`, taking an empty conjunction as logical truth.
Then `T_1 proves sigma` and `T_2 proves not sigma`, contradicting (R).

By completeness, choose `B^* models T_2 union C` and put

\[
S=\operatorname{Th}_{L_0}(B^*\upharpoonright L_0).
\]

This is a complete consistent `L_0`-theory, and `T_2 union S` has the
model `B^*`. Also `T_1 union S` is consistent. If not, finitely many
sentences `rho_1,...,rho_m in S` would give

\[
T_1\vdash\neg(\rho_1\land\cdots\land\rho_m).
\]

That negated conjunction is an `L_0`-sentence and belongs to `C`, so
`B^*` satisfies it. But `B^*` satisfies every `rho_j` by definition of
`S`, a contradiction. The empty finite subset case would contradict
consistency of `T_1` itself.

Thus choose

\[
A_0\models T_1\cup S,
\qquad
B^*\models T_2\cup S.
\tag{1}
\]

This reduces the theorem to the usual common-complete-theory case
without presupposing joint consistency. Completeness may be used here
to pass between the displayed syntactic claims and finite semantic
inconsistency; it is a previously established dependency.

## 2. Initial embedding into a model of the second theory

Add one fresh constant `c_a` for each element `a` of `A_0`, with all
these symbols outside `L_1 union L_2`. Consider

\[
T_2\cup S\cup
\operatorname{ElDiag}_{L_0}(A_0\upharpoonright L_0).
\tag{2}
\]

This theory is finitely satisfiable. For a finite elementary-diagram
fragment, conjoin its formulas into `delta(c_{a_1},...,c_{a_n})`,
listing its distinct parameter names. Its existential closure

\[
\exists x_1\cdots\exists x_n\,\delta(x_1,\ldots,x_n)
\tag{3}
\]

is an `L_0`-sentence true in `A_0|L_0`. Since that reduct models the
complete theory `S`, sentence (3) belongs to `S`. Therefore `B^*|L_0`
has witnesses for (3). Interpret the finitely many displayed new
constants by those witnesses in the full `L_2`-structure `B^*`.
This satisfies the chosen finite fragment while preserving all of
`T_2 union S`. If no constants occur, (3) is simply `delta`.

By compactness, a model of (2) yields an `L_2`-structure `B_0` and an
elementary `L_0`-embedding

\[
e:A_0\upharpoonright L_0\longrightarrow B_0\upharpoonright L_0.
\tag{4}
\]

Transport `B_0` along this embedding as in Section 4 below. We may
then arrange literal inclusion and agreement on the old domain:

\[
A_0\upharpoonright L_0
\preccurlyeq B_0\upharpoonright L_0,
\qquad |A_0|\subseteq|B_0|.
\tag{5}
\]

This step does not claim that a preselected `L_2`-model already
contains `A_0|L_0`, or that accidental overlap of their original
underlying sets provides a common embedding. `B^*` was used as a
finite-satisfiability witness; `B_0` is the model obtained from (2).

## 3. The elementary-diagram extension lemma

Let `L_0 subseteq L` be signatures. Let `A` be an `L`-structure and
`B` an `L_0`-structure such that

\[
A\upharpoonright L_0\preccurlyeq B
\]

is a literal elementary substructure inclusion. There is an
`L`-structure `A'` for which

\[
A\preccurlyeq A',\qquad
B\preccurlyeq A'\upharpoonright L_0,
\qquad |A|\subseteq|B|\subseteq|A'|,
\tag{6}
\]

all as literal inclusions.

### Finite satisfiability

Give every element `b in B` a fresh constant `c_b`; the constants
for `a in A` are the same symbols in both diagrams. Consider

\[
\operatorname{ElDiag}_{L}(A)
\ \cup\
\operatorname{ElDiag}_{L_0}(B).
\tag{7}
\]

Take any finite subset. Let `alpha(c_a)` be the conjunction of its
`L(A)` sentences, all true in `A`. Let `delta(c_a,c_b)` be the
conjunction of its `L_0(B)` sentences, where the displayed `a` tuple
lists the finitely many named elements from `A` used in this fragment,
and the `b` tuple lists the distinct names from `B\A` that occur.

In `B`, the original `b` elements witness

\[
\exists\bar y\,\delta(\bar a,\bar y).
\tag{8}
\]

Because `A|L_0` is elementary in `B`, (8) is true in `A|L_0` as well.
Choose witnesses inside `A` and interpret the finitely many new
`c_b` names by them. Keep each `c_a` interpreted as its original
element. The full `L`-structure `A`, with this finite constant
expansion, satisfies both `alpha` and `delta`. Its extra `L` symbols
were never changed.

This remains correct when diagram fragments contain equalities,
inequalities, or nested function terms. Those are simply part of the
`L_0` formula in (8). A finite fragment may require a new `b` name to
be unequal to particular old parameters; elementarity supplies that
finite requirement too. It need not supply one simultaneous witness
inside `A` for all inequalities in the full infinite diagram.

Thus every finite subset of (7) is satisfiable. Compactness gives a
model `C` of (7). By `thm:diagram-tests`, the named-element maps give
elementary embeddings

\[
e_A:A\longrightarrow C\upharpoonright L,
\qquad
e_B:B\longrightarrow C\upharpoonright L_0.
\]

The maps agree on `A`, since the two diagrams used the same constant
`c_a` for each `a in A`. Full diagram inequalities make both maps
injective. Their function and relation clauses preserve all common
structure. The desired literal form (6) now follows by transport.

## 4. Transport to literal inclusions, including overlapping domains

Here is the precise transport step used in Sections 2 and 3. Suppose
`e:B -> C|L_0` is the chosen elementary embedding. Replace the domain
of `C` by

\[
D=B\cup E,
\]

where `E` is a fresh disjoint copy of `|C|\e[B]`. Let
`h:|C| -> D` be the bijection satisfying `h(e(b))=b`, and mapping the
remaining elements bijectively to `E`. Such a fresh tagged copy is
available for any sets involved; it is chosen disjoint from `B` even
when the original underlying sets of `B` and `C` overlap.

Transport every symbol through `h`. For a function symbol `f`, set

\[
f^{C^h}(h(c_1),\ldots,h(c_n))
=h(f^C(c_1,\ldots,c_n));
\]

for a relation symbol `R`, use the coordinatewise image of its
interpretation; for a constant `d`, put `d^{C^h}=h(d^C)`.
Equality remains actual identity. The resulting `C^h` is isomorphic
to `C` and its `L_0`-reduct contains `B` elementarily via the literal
inclusion.

In Section 3, `e_A(a)=e_B(a)` for every old `a`, so the same transport
sends `e_A(a)` to `a`. Hence the full old `L`-structure `A` is an
elementary substructure of `C^h`. No previously fixed interpretation
on `A` is renamed or overwritten. Take `A'=C^h`.

At the initial step there is no designated common parameter model
between the independently chosen `A_0` and `B^*`. Their incidental
set-theoretic intersections are not identified by shared parameter
names. Only the embedding (4), established by the new diagram theory,
determines the identifications used in transport.

## 5. Alternate the two extension constructions

Starting with (5), apply the extension lemma to the full `L_1` model
`A_0` and the `L_0` structure `B_0|L_0`. It gives `A_1` such that

\[
A_0\preccurlyeq_{L_1}A_1,
\qquad
B_0|L_0\preccurlyeq A_1|L_0,
\qquad |B_0|\subseteq|A_1|.
\]

Apply the lemma with the languages exchanged, to the full `L_2` model
`B_0` and `A_1|L_0`. This gives `B_1` satisfying

\[
B_0\preccurlyeq_{L_2}B_1,
\qquad
A_1|L_0\preccurlyeq B_1|L_0,
\qquad |A_1|\subseteq|B_1|.
\]

Continue inductively. The common-language reducts form the literal
elementary chain

\[
A_0|L_0\preccurlyeq B_0|L_0\preccurlyeq
A_1|L_0\preccurlyeq B_1|L_0\preccurlyeq\cdots,
\tag{9}
\]

while the full structures form separate elementary chains

\[
A_0\preccurlyeq_{L_1}A_1\preccurlyeq_{L_1}\cdots,
\qquad
B_0\preccurlyeq_{L_2}B_1\preccurlyeq_{L_2}\cdots.
\tag{10}
\]

Every `A_n` satisfies `T_1`, and every `B_n` satisfies `T_2`, because
elementary extensions preserve sentences.

There is no hidden class-choice principle in this induction. If desired,
fix an infinite cardinal
`kappa >= |L_1 union L_2|+|A_0|+aleph_0`. Each diagram theory has at
most `kappa` sentences as long as the preceding domains have size at
most `kappa`. The standard Henkin construction behind completeness
has a model of size at most `kappa`: its witness language has that
size and its elements are equivalence classes of finite terms. Thus
all successive models can be chosen with that bound and transported
using fresh blocks of one fixed set of size `kappa`. The possible
stage structures then form a set, and ordinary dependent choice,
available from Choice, supplies the countable sequence.

## 6. The coherent unions give the joint model

Let

\[
A_\infty=\bigcup_{n<\omega}A_n,
\qquad
B_\infty=\bigcup_{n<\omega}B_n.
\]

By `thm:elementary-chain`, these are `L_1` and `L_2` models of `T_1`
and `T_2`, respectively. Their underlying domains agree, since

\[
|A_n|\subseteq|B_n|\subseteq|A_{n+1}|
\]

at every stage. Their `L_0`-reducts also agree: both are the compatible
union of the interleaving chain (9), and the even and odd subsequences
are cofinal in that chain.

In particular, each finite tuple from the common union domain lies
in a stage where every common function and relation has already
acquired its value. Later stages preserve it. Common constants and
nullary relation symbols agree as well. Therefore one can give the
union domain the `L_1` interpretations from `A_infty` and the `L_2`
interpretations from `B_infty`. Compatibility on the overlap makes
this one well-defined `(L_1 union L_2)`-structure. Its two reducts
satisfy `T_1` and `T_2`, so it satisfies their union. This proves (R).

## Why this is not arbitrary amalgamation

The extension lemma assumes an elementary inclusion of the entire
common reduct, not merely a shared substructure or an arbitrary
embedding. That hypothesis is used exactly to reflect (8).
Without it the diagram union can be inconsistent: let `L_0={P}`,
let `A={a}` with `P` empty, and let `B={a,b}` with `P={b}`. Then
`A` is a substructure of `B`, but `ElDiag(A)` contains `forall x not P(x)`
and `ElDiag(B)` contains `P(c_b)`. Their union is inconsistent.

The initial step chooses a suitable model of `T_2` admitting an
elementary embedding of the first reduct; it does not preserve an
arbitrarily prescribed identification between two given models.
The final conclusion is joint consistency of the two theories.
No amalgamation property over a chosen nonelementary base is asserted.

Only this proof note was authored. No manuscript edits, software tests,
builds, or renders were performed.
