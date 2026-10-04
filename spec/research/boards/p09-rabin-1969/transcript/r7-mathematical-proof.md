# Round 7 mathematical-and-proof-correctness review: Rabin 1969 / `N-c-014.d`

## Verdict and exact scope

I reject this frozen Round 7 snapshot because one mandatory cross-record
review-status invariant remains false: the detailed source note correctly says
at its opening that a fresh Round 7 is required, but its concluding filing
instruction still says that fresh Round 6 reviews must begin.  I found no
mathematical or proof-architecture defect in the reconstruction itself.  The
single unresolved finding is `R7-MP-01` below.

This verdict is limited to the six hash-pinned objects constituting the Round 7
snapshot for `N-c-014.d`, assessed at manuscript-content level.  It does not
admit or reject all of `N-c-014`, any other presentation, Part IX, a rendered
handbook page, a build, typesetting, human or user acceptance, another part, or
the book.  I performed no test, automated check, repository script, TeX command,
interim build, handbook-PDF inspection, or build.  Native SHA-256 computation
was the only automated operation used on the frozen evidence.

## Evidence boundary and completeness

I read the charter completely before substantive review.  I used only the
charter, the six Round 7 frozen objects, and the two original-detail render sets
authorized by the charter.  I did not read any earlier-round report, any other
Round 7 report, `ledger.md`, `transcript/chair.md`, another board, a staging
draft, the layout extraction, conversation history, or memory; I did not
contact another reviewer and did not browse the web.

The four textual frozen objects were read in full, not only at the charter's
highlighted ranges:

- `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1437;
- `handbook/bib/handbook.bib`, lines 1--6272;
- `spec/research/p09-rabin-1969-source-note.md`, lines 1--660; and
- `spec/research/p09-source-presentations-lot2-3.md`, lines 1--915.

I visually inspected every required source render at original detail.  The
Rabin pages inspected were: physical p. 1 (custody-and-use cover); physical
p. 2 = printed p. 1; p. 3 = printed p. 2; p. 4 = printed p. 3; p. 5 = printed
p. 4; p. 6 = printed p. 5; p. 7 = printed p. 6; p. 8 = printed p. 7; p. 9 =
printed p. 8; p. 10 = printed p. 9; p. 11 = printed p. 10; p. 12 = printed
p. 11; p. 13 = printed p. 12; p. 14 = printed p. 13; p. 15 = printed p. 14;
p. 16 = printed p. 15; p. 17 = printed p. 16; p. 18 = printed p. 17; p. 19 =
printed p. 18; p. 20 = printed p. 19; p. 21 = printed p. 20; p. 22 = printed
p. 21; p. 23 = printed p. 22; p. 24 = printed p. 23; p. 25 = printed p. 24;
p. 26 = printed p. 25; p. 27 = printed p. 26; p. 28 = printed p. 27; p. 29 =
printed p. 28; p. 30 = printed p. 29; p. 31 = printed p. 30; p. 32 = printed
p. 31; p. 33 = printed p. 32; p. 34 = printed p. 33; p. 35 = printed p. 34;
and p. 36 = printed p. 35.  Thus the custody cover and every printed page
1--35 were inspected.

The Meyer pages inspected were: physical PDF p. 485 = printed p. 477;
physical p. 486 = printed p. 478; physical p. 487 = printed p. 479; physical
p. 488 = printed p. 480; physical p. 489 = printed p. 481; and physical p. 490
= printed p. 482.  The inspection therefore covered Meyer's complete six-page
article and no out-of-scope part of the proceedings volume.

The visual reading confirmed the page sequence and the relevant formulae and
symbols directly: Rabin's root symbol on printed pp. 3--5, ordinary automata on
pp. 5--7, formula/run translations on pp. 7--10, the product on pp. 17--19,
marked obligations and well-foundedness on pp. 19--24, dual acceptance and the
two half-steps on pp. 24--30, finite trees on pp. 30--32, and the emptiness
recursion on pp. 32--34.  Meyer printed pp. 478--479 contain the tower lower
bound and the listed two-successors-and-prefix case.  The PDFs, rather than OCR
or a text extraction, controlled this review.

## Recomputed native identities

All six identities were independently recomputed with native SHA-256 hashing,
both before substantive review and again immediately before filing.  Each
matches the Round 7 charter exactly:

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | match |
| `spec/research/p09-rabin-1969-source-note.md` | `73A700E83218BD1E0460CD836E72FB7EE86914C52D70D865B903CE367400C944` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `0EE7C6EAD01590636652D409EA51FD7A34555F410E3277121B165932A233D41F` | match |

## Independent mathematical reconstruction

### Successor structures; ordinary and dual acceptance

The reader's basic structure is exact.  At `n-c-014.tex:914--963`, the root is
Rabin's \(\Lambda\), and Definition 1.1 is given for every \(0<n\leq\omega\):
\(T_n=n^*\), \(r_i(x)=xi\), together with initial-segment and lexicographic
orders.  The qualification is also correct: for finite \(n\), both orders are
monadic-second-order definable from the successors, while the displayed orders
cannot simply be eliminated in the \(T_\omega\) case.  These claims are
controlled by Rabin printed pp. 3--5.

At `n-c-014.tex:965--1014`, a valued tree can be rooted at any \(x\), not just
at \(\Lambda\).  A table is \(\langle S,M\rangle\), with
\(M:S\times\Sigma\to\mathcal P(S\times S)\); an ordinary automaton adds
\(S_0\subseteq S\) and \(F\subseteq\mathcal P(S)\).  Ordinary acceptance is
literally
\[
  \exists r\,[r(x)\in S_0\ \land\
  \forall\pi\;(\operatorname{In}(r\!\upharpoonright\!\pi)\in F)],
\]
so a missing run makes ordinary acceptance false.  Rabin printed pp. 5--7
control these tuples and quantifiers.

Definitions 3.5--3.6 are correctly separated at `n-c-014.tex:1143--1188`.
For \(\Omega=((L_i,U_i))_{1\leq i\leq k}\), a path map \(\phi\) has type
\(\Omega\) precisely when some \(i\) satisfies
\(\operatorname{In}(\phi)\cap U_i\ne\varnothing\) and
\(\operatorname{In}(\phi)\cap L_i=\varnothing\).  It is type-empty only when
it also has some \(j\) with \(\operatorname{rng}(\phi)\cap L_j=\varnothing\).
Dual acceptance reverses the prefix to \(\forall r\,\exists\pi\), expressed as
a universal implication over runs rooted in the named state.  If there is no
such run, every implication is true, so the dual language contains the tree
vacuously.  Thus the pair sequence is not the ordinary \(F\); it belongs to
the complement construction.  Rabin printed pp. 24--26 control the definitions
and Lemma 3.6's complement role.

### Bit tracks, formula construction, converse run coding, and sentences

The bit-track map at `n-c-014.tex:1027--1046` is genuinely typed and bijective:
from \((A_1,\ldots,A_n)\) it forms the full-root label
\((\chi_{A_1}(x),\ldots,\chi_{A_n}(x))\).  Its inverse is explicit pointwise:
the \(i\)-th set is the set of nodes whose \(i\)-th label bit is \(1\).  Hence
neither injectivity nor surjectivity is merely asserted.

The formula-to-automaton direction is also reconstructed in the correct
dependency order at `n-c-014.tex:1048--1065`: eliminate equality and the two
orders in favor of set membership, move set quantifiers outward, reduce the
matrix to Boolean combinations of the printed principal-formula pattern, use
the Section 3.10 finite-tree construction and Corollary 3.13 for that pattern,
then use Boolean closure, projection of one label coordinate, and
complementation.  Theorem 1.4's converse is described locally as adding an
unconstrained coordinate; no unexplained operation name is used.  The example
\(\exists x(x\in A\land r_0(x)\in B)\) at lines 1067--1077 is correctly marked
as a handbook-owned instance: a finite labelled witness containing the node and
its left child realizes precisely the stated principal formula.  It is not
misrepresented as Rabin's printed transition table.  Rabin printed pp. 7--9
and 30--31 control the construction and its deferred finite-tree component.

For the converse, `n-c-014.tex:1079--1091` first uses Lemma 1.2 to normalize to
one initial state, encodes each finite state in finitely many monadic tracks,
and states the root, local-move, and path acceptance requirements.  The prefix
is exactly \(\exists B_1\cdots\exists B_m\,\forall C\), where \(C\) is tested
as a path.  This matches Theorem 1.10 on Rabin printed pp. 9--10.  For a closed
sentence, lines 1093--1098 correctly write it as \(\exists A_1F(A_1)\), build
the representing automaton for \(F\), and ask whether its language is nonempty.
Theorem 1.6 decides that question.  No regular-tree basis theorem is inserted.

### Theorem 3.1 product

The product at `n-c-014.tex:1102--1139` is correctly typed.  Starting with a
tree table \(\langle S,M\rangle\) and a path language \(B\subseteq S^\omega\),
the proof chooses a deterministic Muller word automaton
\(\langle U,K,u_0,H\rangle\), where \(K:U\times S\to U\) and
\(H\subseteq\mathcal P(U)\).  The tree product has state set \(U\times S\),
initial set \(\{u_0\}\times S\), and transition
\[
 ((u,s),a)\longmapsto
 \{((K(u,s),s_1),(K(u,s),s_2)):(s_1,s_2)\in M(s,a)\}.
\]
The same first-coordinate successor is sent to both children because the
current state symbol \(s\) is consumed before the two paths diverge.
Determinism therefore gives one coherent word-state history on their common
prefix.

There are two small equalities behind the designated family, and both check.
Along a branch the first coordinates are
\(u_0,u_1,u_2,\ldots\), with \(u_{n+1}=K(u_n,s_n)\).  If one's word-automaton
convention starts the recorded run after consuming \(s_0\), the two records
differ only by the single initial term \(u_0\), which cannot change an
infinitely recurring set.  Moreover, because \(S\) is finite, a first
coordinate \(u\) recurs infinitely often iff at least one pair \((u,s)\)
recurs infinitely often: the reverse direction is immediate, and the forward
direction is the finite pigeonhole principle over \(s\in S\).  Consequently
\(p_1(\operatorname{In}((u_n,s_n)))=\operatorname{In}((u_n))\), and the product
family \(\{C\subseteq U\times S:p_1(C)\in H\}\) accepts exactly the intended
path language.  This is Rabin's printed pp. 17--19 construction; the external
word theorem is correctly attributed to McNaughton rather than Rabin.

### Zero length, marked obligations, well-founded dependence, and the two half-steps

The zero-length completion at `n-c-014.tex:1190--1213` is mathematically exact.
Lemma 3.6 enumerates
\(\mathcal P(S)\setminus(F\cup\{\varnothing\})\), which can be empty.  For the
empty sequence, no path has a listed type, so
\[
 D(\mathfrak A_0,\langle\rangle,s)
 \quad\Longleftrightarrow\quad
 \text{there is no run rooted in }s.
\]
Because the named state entails \(S\ne\varnothing\), every map from an infinite
path into finite \(S\) has a nonempty infinitely recurring set.  For
\(\Omega^\dagger=((S,S))\), a path would therefore have to make that set both
meet and avoid \(S\), which is impossible.  Thus
\([\Omega^\dagger]=\varnothing\), and its dual semantics is exactly the empty
sequence's vacuous no-run semantics.  This changes no acceptance definition;
it only embeds the omitted zero-length output into the source's positive-length
induction.  Rabin printed pp. 24--26 control Lemma 3.6, while printed pp. 29--32
show that the ensuing induction starts at positive length.

The finite-state content of complementation is not replaced by an appeal to
transfinite induction.  At `n-c-014.tex:1220--1225`, Lemma 3.2 activates the
marked local obligations, runs the finitely many local automata simultaneously,
merges copies that reach the same state, and invokes Theorem 3.1 for the
remaining all-path check.  Rabin printed pp. 19--21 control this construction.

At lines 1227--1233, for nonempty \(H\), the relevant object has the stated
standing: it is a map \(h\mapsto H_h\subseteq H\).  It is well founded exactly
when no infinite sequence obeys \(h_{m+1}\in H_{h_m}\) at every step.  The
ordinal characterization in Lemma 3.3 is equivalent in both directions.  If
every dependency lies in a lower ordinal stratum, an infinite dependency
sequence would give an impossible infinite strict descent of ordinals.
Conversely, the no-infinite-sequence condition makes the dependency relation
well founded, so well-founded recursion assigns each element an ordinal above
all ordinals assigned to its dependencies.  Lemma 3.4 adds this condition to
the automaton-definable marked construction, and Lemma 3.11 later uses it to
prevent an obligation from being deferred forever.  It is neither ordinary
path acceptance nor same-state merging.  Rabin printed pp. 20--24 and 27--30
control these roles.

The lengths and cases of the two half-steps are preserved at
`n-c-014.tex:1235--1256`.  Lemma 3.7 preserves the pair-sequence length; Lemma
3.8 also stays at that length while producing a last lower set equal to
\(\varnothing\).  With \(L_k=\varnothing\), Lemmas 3.9--3.10 use the shorter
\(\Omega_{k-1}\), so induction decreases the positive integer \(k\).  For an
arbitrary length-\(k\) sequence, Lemma 3.11 supplies the local/deferred
obligations, Lemma 3.8 reaches the last-empty-lower-set case without silently
decreasing the length, and Lemma 3.4 imposes the well-founded condition.  The
zero-length normalization is performed before these cases.  Rabin printed
pp. 24--30 control the pair lengths, and printed pp. 31--32 control the final
induction.

### Finite trees and the exact four-result division

The finite-tree types at `n-c-014.tex:1259--1283` are correct.  The node set
\(E\subseteq T\) is finite and predecessor closed.  Its terminal-node frontier
is
\(\operatorname{Ft}(E)=\{x\in E:x0\notin E\land x1\notin E\}\), and \(E\) is
`frontiered` exactly when every node outside this frontier has both binary
children in \(E\).  This condition is not redundant with predecessor closure,
which alone permits exactly one child.  A valuation labels
\(E\setminus\operatorname{Ft}(E)\).  The finite-tree automaton has transition
codomain
\(\mathcal P((S\times S)\cup\{(f,f)\})\), where \(f\notin S\) is an external
frontier value and not a state.  Rabin printed pp. 30--31 control these
definitions.

The four successive result roles are also exact at `n-c-014.tex:1284--1294`:

1. Lemma 3.12 lifts an automaton-definable collection of finite trees to the
   infinite trees having an accepted finite initial subtree.
2. Corollary 3.13 applies that lift to the principal formulas needed by
   Theorem 1.7.
3. Lemma 3.14 is the intervening compactness argument: if every infinite run
   meets a collection of node--state obligations, a finite subcollection
   already meets every run.
4. Corollary 3.15 returns to frontiered finite-tree machinery to make the
   universal hitting condition automaton definable for complementation.

Rabin printed pp. 30--32 control that exact division.  None of these results
makes the infinite input tree finite or converts full monadic quantification
into weak monadic quantification.

### Section 3.12 emptiness recursion and both empty-set repairs

The opening reduction at `n-c-014.tex:1307--1333` is Rabin's.  Erasing the
alphabet replaces each transition set by the union over all original labels,
so a run on the unique one-letter full tree is precisely a run on some original
valuation: each original run is plainly retained, and for a run in the union
table one chooses at every node a label witnessing its displayed transition.
Theorem 1.5 complements that one-tree language; Lemma 3.6 converts the
complement automaton back to a specified dual language representing the
original one-tree language.  Original nonemptiness is therefore one membership
question for the unique one-letter full tree.  No basis theorem occurs.  Rabin
printed pp. 32--33 control this reduction.

The recursion properly restates its current finite table and current pair
sequence at `n-c-014.tex:1335--1342`, including the possibility that effective
reductions have changed the state set.  Definition 3.7 at lines 1343--1351
retains the formal state set \(R\) and restricts only transition pairs to
\(R'\times R'\).  Therefore states strictly below the root lie in \(R'\), while
the named root state may lie outside \(R'\).  Rabin printed p. 33 controls this
root exception.

For the arbitrary-sequence half-step, lines 1353--1359 correctly observe that
the disjoint strata computed from Lemma 3.11 can add a state only finitely many
times; over finite \(R\), no more than \(|R|\) nonempty strata can occur.  Each
stage membership question is reduced by Lemma 3.8 to the same-length case with
last lower set empty.  This supplies effective termination without pretending
that the transfinite proof itself is a finite-state construction.

For \(L_k=\varnothing\) and \(k>1\), lines 1361--1371 range over every
\(H\subseteq U_k\).  If \(H=\varnothing\), no first-hit state is supplied and
the condition is exactly the direct shorter dual question for
\(\Omega_{k-1}\).  If \(H\ne\varnothing\), restricting descendants to
\(R\setminus H\) via Definition 3.7 converts the clauses for
\(H\cup\{s_0\}\) into length-\(k-1\) questions.  Rabin printed p. 34 states the
equivalence with a **nonempty** \(H\subseteq U_k\), then says the finite
reduction ranges over restrictions associated with \(H\in\mathcal P(S)\).
The printed nonempty clause is not exhaustive because dual acceptance permits
the no-run and already-shorter-type branches.  Adding the empty branch as the
direct shorter question is therefore a necessary and correctly labelled
handbook-owned completion.

For the base \(k=1,L_1=\varnothing\), lines 1373--1389 correctly permit
\(m\geq0\), with \(U_0=\{s_1,\ldots,s_m\}\subseteq U_1\), and use finite
frontiered trees \(E_0,\ldots,E_m\).  In the source's nonempty case, every
finite run from \(s_i\) must reach a state of \(U_0\) below the root.  When
\(m=0\), \(U_0=\varnothing\), and the condition on \(E_0\) says that no finite
run from \(s_0\) exists.  This is exactly the finite obstruction to an infinite
run: compatible partial runs on successive finite full initial trees form a
finitely branching tree; if they existed at every depth, König's Infinity Lemma
would give an infinite compatible chain whose union is an infinite run.
Conversely, an infinite run restricts to every finite initial tree.  Thus no
infinite run is equivalent to some finite no-run obstruction.  Rabin printed
p. 34 prints **nonempty** \(U_0\); admitting \(U_0=\varnothing\) is the exact
missing vacuous branch, not an altered base theorem.

The existence of the required finite witnesses is then expressed in the weak
monadic theory of two successors, whose decision is an external Doner/
Thatcher--Wright dependency.  This use of weak logic concerns finite witness
trees only; it does not weaken the original full \(S2S\) input.  Rabin printed
pp. 33--34 control the recursion and its cited external base.

### Applications, complexity correction, and later-route boundary

At `n-c-014.tex:1404--1421`, the Chapter II applications retain their exact
class-level strengths: the stated monadic or weak theories of countable linear
orders and well-orders; countable unary-function structures and the weak theory
of all unary-function structures; the selected closed/\(F_\sigma\) Cantor-space,
lattice, and unit-interval structures; countable Boolean algebras with ideal
quantification and arbitrary Boolean algebras with distinguished ideals; and
the encoded Gale--Stewart determinacy statement for \(F_\sigma\) payoff sets.
Rabin printed pp. 10--17 control these claims.

The Meyer consequence at `n-c-014.tex:941--960` is valid.  Rabin printed p. 1
claims elementary-recursive procedures.  Meyer printed p. 478 states the
non-elementary tower lower-bound form, and printed p. 479 lists the theory of
two successors and prefix, crediting that case to Meyer and Stockmeyer.  The
language with the two successors and prefix is a sublanguage of the displayed
binary-tree language, which additionally has lexicographic order.  Any
elementary decision procedure for the full language would decide its
sublanguage simply by running on sentences that omit the extra symbol, contrary
to Meyer's lower bound.  This refutes only Rabin's claimed worst-case upper
bound; it does not refute decidability or the effectiveness of the construction.

Finally, `n-c-014.tex:1423--1437` states the reconstruction boundary accurately.
It says which definitions and proof dependencies the reader reconstructs and
which transition tables and inductions remain in the complete article.  It
attributes the later regular-tree-basis route to Thomas and does not project it
backward into Rabin.  McNaughton's word theorem is likewise kept external at
Theorem 3.1.

## Invariant-by-invariant result

| Invariant | Result | Evidence and reason |
|---|---|---|
| R01 | PASS | `n-c-014.tex:914--917`; Rabin printed pp. 3--5 use \(\Lambda\), with no silent \(\epsilon\) substitution. |
| R02 | PASS | `n-c-014.tex:941--963`; Rabin printed pp. 3--5 give \(0<n\leq\omega\), \(T_n=n^*\), both orders and successors, the finite definability qualification, and the \(T_\omega\) exception. |
| R03 | PASS | `n-c-014.tex:965--1014`; Rabin printed pp. 5--7 support arbitrary roots, distinct table/automaton tuples, \(F\subseteq\mathcal P(S)\), and \(\exists r\forall\pi\). |
| R04 | PASS | `n-c-014.tex:1143--1188`; Rabin printed pp. 24--26 support the pair sequence, \(\forall r\exists\pi\), its complement role, and no-run vacuity. |
| R05 | PASS | `n-c-014.tex:1016--1023`; Rabin printed pp. 6--7 give exactly Theorems 1.3--1.6 and the two coordinate directions are described without an undefined operation name. |
| R06 | PASS | `n-c-014.tex:1027--1065`; Rabin printed pp. 7--9 and 30--31 support the typed bijection and the separately stated principal-formula, finite-tree, Boolean, projection, and complement steps. |
| R07 | PASS | `n-c-014.tex:1067--1077`; the example is a correct instance and expressly handbook-owned, controlled by Rabin's printed pp. 7--9 and 30--31 construction. |
| R08 | PASS | `n-c-014.tex:1079--1098`; Rabin printed pp. 9--10 support the normalized run coding, \(\exists\bar B\forall C\), and direct sentence-to-nonemptiness reduction. |
| R09 | PASS | `n-c-014.tex:1102--1139`; Rabin printed pp. 17--19 support every product type and update; the one-term index difference cannot affect infinite occurrence. |
| R10 | PASS | `n-c-014.tex:1143--1188`; Rabin printed pp. 24--26 support the exact type, type-empty condition, quantifier reversal, and complement role. |
| R11 | PASS | `n-c-014.tex:1215--1225`; Rabin printed pp. 19--24 retain marked obligations, simultaneous runs, same-state merging, and the Theorem 3.1 path check. |
| R12 | PASS | `n-c-014.tex:1227--1233, 1240--1247, 1296--1303`; Rabin printed pp. 20--24 and 27--32 support the map's standing, exact no-infinite-dependency condition, ordinal equivalence, and Lemmas 3.4/3.11 uses. |
| R13 | PASS | `n-c-014.tex:1190--1213, 1235--1256`; Rabin printed pp. 24--32 support the exact lengths and separate zero, arbitrary, last-empty-lower-set, and positive-\(k\) cases. |
| R14 | PASS | `n-c-014.tex:1259--1283`; Rabin printed pp. 30--31 support finite predecessor closure, `frontiered`, its nonredundancy, valuation boundary, exact codomain, and external \(f\notin S\). |
| R15 | PASS | `n-c-014.tex:1284--1294`; Rabin printed pp. 30--32 support the exact Lemma 3.12 / Corollary 3.13 / Lemma 3.14 / Corollary 3.15 division and no finite/weak conflation. |
| R16 | PASS | `n-c-014.tex:1307--1333`; Rabin printed pp. 32--33 support one-letter erasure, complement, dual conversion, and membership, with no basis theorem. |
| R17 | PASS | `n-c-014.tex:1335--1351`; Rabin printed p. 33 supports the current-table/current-sequence discipline and the below-root restriction with root exception. |
| R18 | PASS | `n-c-014.tex:1361--1371`; Rabin printed p. 34 controls the printed nonempty clause and reduction; the manuscript correctly supplies \(H=\varnothing\), preserves nonempty branches, and proves finite-stratum termination. |
| R19 | PASS | `n-c-014.tex:1373--1400`; Rabin printed p. 34 controls the printed nonempty branch and external weak-theory appeal; the \(m=0\) no-run obstruction follows exactly by König's lemma. |
| R20 | PASS | `n-c-014.tex:941--960, 1392--1396`; Rabin printed p. 1 and Meyer printed pp. 478--479 support the historical claim, lower-bound correction, exact attribution, and sublanguage consequence. |
| R21 | PASS | `n-c-014.tex:1404--1421`; Rabin printed pp. 10--17 support each application at the stated class strength. |
| R22 | PASS | `n-c-014.tex:1423--1437`; Rabin printed pp. 1--35 control the stated reconstruction boundary; Thomas and McNaughton remain explicitly later/external. |
| R23 | PASS | The reader's source numbering and printed-page locators agree with the complete visual source: Definitions 1.1, 1.3, 1.5, 1.7, 3.2, 3.5--3.7; Theorems 1.1, 1.3--1.7, 1.10, 1.12, 3.1; and Lemmas/Corollaries 3.2--3.15 are used at their proper strength and role. |
| R24 | **FAIL: `R7-MP-01`** | Bibliographic identities and the Meyer correction agree, but `p09-rabin-1969-source-note.md:618, 649--660` retains a stale Round 6 closing instruction, contradicting its own lines 18--39 and the compact record at `p09-source-presentations-lot2-3.md:672`. |
| R25 | PASS | `p09-rabin-1969-source-note.md:87--98` distinguishes public research access from an open-content/republication licence and identifies local PDFs/renders as research objects only. |
| R26 | PASS | At first substantive use the reader gives exact standing, definition, nonredundancy, and later use for the potentially troublesome terms, especially the obligation map (`n-c-014.tex:1227--1233`) and `frontiered`/external \(f\) (`n-c-014.tex:1259--1287`). No unsupported new mathematical name survives. |
| R27 | PASS | The detailed derivations above confirm that finite/infinite, weak/full, ordinary/dual, existence/effectivity, source/later-route, and decidability/complexity boundaries remain distinct. |
| R28 | PASS | `p09-rabin-1969-source-note.md:38--42` and `p09-source-presentations-lot2-3.md:672` keep `N-c-014.d` pending and expressly avoid broader completion claims; this report's verdict has the same limited scope. |
| R29 | PASS | `n-c-014.tex:1190--1213`; Rabin printed pp. 24--26 and 31--32 support the possible empty list and positive-length induction; the derivation above proves \(((S,S))\) has empty path language and identical dual no-run semantics. |

The relevant bibliography entries are internally correct: McNaughton at
`handbook.bib:2290--2299`, Thomas at `handbook.bib:2346--2355`, Meyer at
`handbook.bib:5938--5947`, Rabin at `handbook.bib:5973--5982`, and
Thatcher--Wright at `handbook.bib:5993--6002`.  In particular, the Rabin DOI
and scan URL, Meyer article pagination, and Thatcher--Wright pp. 57--81 and DOI
match the other frozen records.  This does not cure the independent status
contradiction recorded next.

## Finding

### R7-MP-01 — must-fix — the detailed note's closing instruction is one round stale

- **Exact frozen manuscript location:**
  `spec/research/p09-rabin-1969-source-note.md:618` and
  `spec/research/p09-rabin-1969-source-note.md:649--660`, decisively lines
  658--659.  Cross-record comparators are the same note at lines 18--39 and
  `spec/research/p09-source-presentations-lot2-3.md:672`.
- **Controlling printed source page:** not applicable to this procedural
  statement.  Review-round status is not a claim in Rabin printed pp. 1--35 or
  Meyer printed pp. 477--482, all of which were inspected.  The controlling
  authority is therefore the Round 7 charter at lines 155--175 and 463--484;
  inventing a printed-page locator would be false.
- **Defect:** the opening of the detailed note correctly records that Rounds
  1--3 and 5--6 are closed, Round 4 was withdrawn, and a fresh hash-pinned Round
  7 is required.  The compact record likewise says that a newly frozen Round 7
  and fresh review remain required.  The detailed note's conclusion instead
  omits Round 6 from its preserved rejection history, retains the heading
  "repaired after Rounds 1--4," and directs that the objects be frozen before
  three fresh **Round 6** reviews begin.  On this Round 7 snapshot, that
  instruction is false and makes the reader/detailed-note/compact-record review
  status fail R24's agreement requirement.
- **Minimum sufficient repair:** update the detailed note's integration heading
  and closing history to include the completed Round 6, and replace "Round 6"
  at lines 658--659 with "Round 7," leaving the statement that three ACCEPT
  verdicts on one unchanged snapshot are required.  Freeze the resulting
  six-object snapshot under new exact hashes and conduct the new blind round
  required by the charter.

No other blocker, must-fix, should-fix, consider, discard, or unresolved-user
finding resulted from this seat's full-snapshot mathematical review.

VERDICT: REJECT — R7-MP-01
