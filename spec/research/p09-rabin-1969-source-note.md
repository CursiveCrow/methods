# Rabin 1969 source note

## Admission status

This note controls the source reconstruction for presentation `N-c-014.d`:
Michael O. Rabin, “Decidability of Second-Order Theories and Automata on
Infinite Trees,” *Transactions of the American Mathematical Society* 141
(July 1969), 1--35.

The complete article body has been acquired and read.  Every one of the 36
physical PDF pages has been visually inspected: one JSTOR/AMS custody-and-use
cover followed by all 35 printed article pages.  Acquisition and body
inspection are complete.  The reader integration reconstructs the formula
translations, complementation architecture, source emptiness argument, worked
encoding, application boundary, and later complexity correction recorded
below.

Rounds 1--3 and Rounds 5--7 are closed and rejected; Round 4 was withdrawn
before any seat filed.  Round 1 exposed three mathematical and terminology
defects; all three repairs survived Round 2 source-fidelity, mathematical, and
adversarial review.
Round 2 nevertheless exposed two first-use defects in the finite-tree
discussion.  The discussion below now supplies each required exact definition,
standing, nonredundancy explanation, and later use.  Round 3 accepted that
substantive repair across the source-fidelity and mathematical seats, but found
that this opening history itself had defeated the claimed first uses by naming
both objects too early.  The history is now generic.  Before Round 4 filing,
the chair found one other undefined operation name in the earlier closure
summary; the reader and note now state the underlying coordinate operation
directly without naming it.  Round 5 mathematical and adversarial seats
accepted the full snapshot, while source fidelity found one compact-record
source-numbering and result-role defect.  The compact record now gives the
exact division among the lift, principal-formula application, compactness, and
complementation results.  Round 6 source-fidelity and mathematical seats
accepted that repair, but the adversarial seat found that this note and the
compact record used a technical source notion without an exact local definition
at first substantive use.  Both records now state the exact source definition,
standing, nonredundancy, and later proof use.  Round 7's three seats found one
remaining cross-record status contradiction in this note's final section: it
still described the pre-Round-6 state.  They found no other source,
mathematical, terminology, rights, or completion-scope defect.  The closing
history is now reconciled with this opening and the compact record.  A fresh
hash-pinned Round 8 is required before admission.

No claim of terminal admission, final typesetting approval, or user acceptance
is made here.

## Source identity, custody, and rights boundary

- Michael O. Rabin, “Decidability of Second-Order Theories and Automata on
  Infinite Trees,” *Transactions of the American Mathematical Society* 141
  (July 1969), 1--35.
- DOI: <https://doi.org/10.1090/S0002-9947-1969-0246760-1>.
- Author/institution record:
  <https://research.ibm.com/publications/decidability-of-second-order-theories-and-automata-on-infinite-trees>.
- Complete research scan:
  <https://lara.epfl.ch/w/_media/sav08/rabin69s2s.pdf>.
- Local research copy:
  `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf`.
- PDF size: 912,831 bytes.
- PDF SHA-256:
  `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3`.
- Layout-preserving extraction:
  `tmp/pdfs/p09-rabin-1969/rabin-1969-layout.txt`.
- Extracted-text SHA-256:
  `01EF5770C17E91C8F19D91B99EE45017E5A8C123773846D06A6892CB5EA94DEF`.
- Page render set:
  `tmp/pdfs/p09-rabin-1969/rendered/page-01.jpg` through
  `page-36.jpg`.

The later primary source controlling the complexity correction is:

- Albert R. Meyer, “The Inherent Computational Complexity of Theories of
  Ordered Sets,” in *Proceedings of the International Congress of
  Mathematicians, Vancouver, 1974*, vol. 2 (Canadian Mathematical Congress,
  1975), 477--482.
- Official IMU proceedings volume:
  <https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1974.2/ICM1974.2.ocr.pdf>.
- Local research copy:
  `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf`.
- PDF size: 53,151,542 bytes.
- PDF SHA-256:
  `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D`.
- Article location: physical PDF pages 485--490, which are printed pages
  477--482.
- Page render set:
  `tmp/pdfs/p09-rabin-1969/meyer1975-rendered/page-485.png` through
  `page-490.png`.
- All six article pages have been visually inspected at original detail.

Physical page 1 is a JSTOR cover.  It identifies the AMS as publisher and
limits the archived copy to personal, noncommercial use absent further
permission.  Physical pages 2--36 are printed pages 1--35 of the article.
The scan therefore supports source-faithful independent reconstruction and
quotation within ordinary scholarly limits; it does not establish an
open-content licence, permission to redistribute the scan, or permission to
reproduce its page images in the handbook.

The official IMU route establishes public research access to the proceedings;
it does not by itself establish an open-content or republication licence.  The
local proceedings PDF and page renders are research objects, not handbook
assets authorized for redistribution.

Meyer's ICM report states a non-elementary tower lower bound and explicitly
includes “the theory of two successors and prefix” in the theorem's list,
crediting that case to Meyer and Stockmeyer (printed p. 479; the bound begins
on printed p. 478).  This is a later primary correction to Rabin's 1969
elementary-recursive complexity claim, not a replacement source for Rabin's
definitions or proof architecture.

## Complete page map

- Printed pp. 1--3: introduction, main result, applications, and automata
  overview.
- Printed pp. 3--5: notation, theories, words, the two orders, successor
  structures, Definition 1.1, and Theorem 1.1.
- Printed pp. 5--7: infinite binary trees, paths, valued trees, tables,
  automata, runs, ordinary acceptance, and Boolean/projection preliminaries.
- Printed pp. 7--10: Theorems 1.5--1.7, normal form, formula-to-automaton
  translation, the decision reduction, finite-set variables, and the converse
  automaton-to-formula translation in Theorem 1.10.
- Printed pp. 10--11: Corollary 1.11 and the interpretation proving the
  decidability of \(S\omega S\) in Theorem 1.12.
- Printed pp. 11--17: applications to countable linear orders, unary
  functions, Cantor space and its \(F_\sigma\) sets, Boolean algebras with
  ideals, and Gale--Stewart games.
- Printed pp. 17--18: sequential Büchi and deterministic Muller automata,
  the invoked McNaughton equivalence, and the path-language product in
  Theorem 3.1.
- Printed pp. 19--24: marked trees, iterative acceptance obligations, the
  condition excluding endless deferral among those obligations, simultaneous
  runs, and the finite-state merging of concurrently activated copies.
- Printed pp. 24--30: Definitions 3.5--3.6, dual acceptance, the reduction of
  complements to dual languages, and the inductive machinery for those
  languages.
- Printed pp. 30--31: finite-tree automata, Lemma 3.12, Corollary 3.13, the
  omitted principal-formula construction, and the compactness argument in
  Lemma 3.14.
- Printed pp. 31--32: completion of the complementation proof, Theorem 1.5.
- Printed pp. 32--34: the effective solution of the emptiness problem,
  Theorem 1.6.
- Printed pp. 34--35: final base-case reduction and references.

## Successor structures and the exact main theorem

For any set \(A\), the source writes \(A^*\) for its finite words.  Concatenation
is juxtaposition, \(\Lambda\) is the empty word, \(x\leq y\) means that \(x\) is
an initial segment of \(y\), and a second symbol denotes the lexicographic order
induced by the order on \(A\).  For \(a\in A\),
\[
 r_a:A^*\longrightarrow A^*,\qquad r_a(x)=xa.
\]
The predecessor fixes \(\Lambda\) and removes one final letter elsewhere.

Definition 1.1 applies to \(0<n\leq\omega\), not merely finite \(n\):
\[
 T_n=n^*=\{i:i<n\}^*.
\]
The structure \(\mathfrak N_n\) has domain \(T_n\), the successor functions
\((r_i)_{i<n}\), the initial-segment order, and the lexicographic order.  Its
monadic second-order theory is denoted \(SnS\).  For finite \(n\), the two
orders are second-order definable from the successor functions; the paper
retains them in the displayed structure because this is not true for
\(T_\omega\).

Theorem 1.1 states exactly that \(S2S\), the monadic second-order theory of two
successor functions, is decidable.  The introduction and Section 1.2 say that
the paper's procedures are elementary recursive in Kalmar's sense (printed
pp. 1 and 4).  That historical complexity claim is false as a worst-case bound
and must not be retained as a theorem of the handbook.  Meyer's later ICM
report states a non-elementary tower lower bound and credits the theory of two
successors and prefix to Meyer and Stockmeyer (printed pp. 478--479).  Because
that language is a sublanguage of Rabin's displayed binary theory, the lower
bound rules out an elementary-recursive decision procedure while leaving
decidability and effectiveness intact.
Theorem 1.12 subsequently obtains decidability of \(S\omega S\) by a definable
interpretation in the binary tree.

Any reader presentation that writes \(\epsilon\) for the root may do so as an
announced notational normalization; Rabin's printed root symbol is
\(\Lambda\).  It must not silently omit the two orders when purporting to give
Definition 1.1 literally.

## Valued trees, runs, and ordinary acceptance

The infinite binary tree is
\[
 T=T_2=\{0,1\}^*.
\]
For \(x\in T\), the rooted subtree is
\(T_x=\{y\in T:x\leq y\}\).  A path of \(T_x\) is a predecessor-closed set
containing \(x\) and choosing exactly one of \(y0,y1\) above every node \(y\)
on the path.

For a mapping \(\phi:A\to B\), the source defines
\[
 \operatorname{In}(\phi)
 =\{b\in B:|\phi^{-1}(\{b\})|\geq\omega\}.
\]
When \(B\) is finite, this is exactly the set of values that occur infinitely
often.

Let \(\Sigma\) be a finite alphabet.  A \(\Sigma\)-valued tree is a pair
\((v,T_x)\) with \(v:T_x\to\Sigma\).  Definition 1.3 distinguishes a transition
table
\[
 \mathfrak A_0=\langle S,M\rangle,
 \qquad M:S\times\Sigma\longrightarrow\mathcal P(S\times S),
\]
from an automaton
\[
 \mathfrak A=\langle S,M,S_0,F\rangle,
 \qquad S_0\subseteq S,
 \qquad F\subseteq\mathcal P(S).
\]
The move relation need not be total.  A run on \((v,T_x)\) is a mapping
\(r:T_x\to S\) satisfying
\[
 (r(y0),r(y1))\in M(r(y),v(y))
\]
for every \(y\in T_x\).

Definition 1.5 accepts \((v,T_x)\) exactly when
\[
 \exists r\left(
 r(x)\in S_0
 \;\land\;
 \forall\pi\subseteq T_x
 \bigl(\pi\text{ is a path}\Rightarrow
       \operatorname{In}(r\mathbin{\upharpoonright}\pi)\in F\bigr)
 \right).
\]
Thus the acceptance datum specified in Definition 1.5 is a family
\(F\subseteq\mathcal P(S)\), in the style of a Muller condition.  It is not a
list of Rabin pairs.  The quantifier order is existential over a single global
run and universal over all paths of that run.

The source defines \(T(\mathfrak A)\) over accepted valued subtrees rooted at
arbitrary \(x\), and observes that every such language is invariant under
re-rooting isomorphism.  Restricting a handbook display to the full-root tree
\(T=T_\Lambda\) is harmless only if that normalization is stated.

Lemma 1.2 permits replacement of the initial set by one initial state.
Theorem 1.3 gives effective union and intersection.  Theorem 1.4 effectively
projects away one label coordinate and, conversely, adds a coordinate left
unconstrained at every node.  Theorem 1.5 gives effective complement, and
Theorem 1.6 gives an effective emptiness decision.  Rabin additionally calls
the last construction elementary recursive, but that printed complexity
qualification is not retained for the later lower-bound reason stated above.
The last two theorems are announced on p. 7 and proved in Chapter III.

## Formula tracks and both definability directions

For \(A\subseteq T\), let \(\chi_A:T\to\{0,1\}\) be its characteristic
function.  Definition 1.7 associates to an \(n\)-tuple
\(\bar A=(A_1,\ldots,A_n)\) the full-root \(\Sigma_n\)-tree
\[
 \tau(\bar A)=(v_{\bar A},T),
 \qquad \Sigma_n=\{0,1\}^n,
 \qquad
 v_{\bar A}(x)
 =\bigl(\chi_{A_1}(x),\ldots,\chi_{A_n}(x)\bigr).
\]
This is a bijection between \(\mathcal P(T)^n\) and full-root
\(\Sigma_n\)-trees.

Theorem 1.7 effectively constructs, from every formula
\(G(A_1,\ldots,A_n)\) of \(S2S\), an automaton
\(\mathfrak A_G\) such that
\[
 \tau(\bar A)\in T(\mathfrak A_G)
 \quad\Longleftrightarrow\quad
 \mathfrak N_2\models G(\bar A).
\]
The proof first eliminates equality and the two order relations in favor of
set membership, then moves set quantifiers outward and writes the remaining
matrix as a Boolean combination of principal formulas
\[
 \exists x\,
 \bigwedge_{j=1}^{k} xw_j\,\eta_j\,A_{i_j},
\]
where \(w_j\in T\) and each \(\eta_j\) is membership or nonmembership.
Principal formulas are recognized by an explicit construction deferred to
Corollary 3.13.  Boolean combinations use Theorems 1.3 and 1.5.
Existential set quantification projects away its bit track by Theorem 1.4;
universal set quantification is reduced by complementation.  The paper itself
calls Corollary 3.13 the filling of a “small gap” remaining in the proof.

Section 1.6 applies Theorem 1.7 to a sentence, reduces truth to nonemptiness of
the representing automaton, and invokes Theorem 1.6.  There is no additional
regular-tree-basis step in this source proof.

The converse is Theorem 1.10.  Given a \(\Sigma_n\)-automaton representing a
relation on \(n\)-tuples of node sets, the paper codes a state-valued run by
finitely many monadic state tracks.  An \(S2S\) formula says that the root has
the initial state, every node and its two children satisfy the transition
table, and every set that is a path has an infinite-state set belonging to
\(F\).  The resulting prefix has the form
\(\exists\bar B\,\forall C\) with a set-quantifier-free matrix, yielding
Corollary 1.11 and its dual.

### Worked encoding required in the reader

For two sets \(A,B\subseteq T\), the formula
\[
 P(A,B)=\exists x\,(x\in A\land r_0(x)\in B)
\]
is principal: it uses the empty suffix for the first conjunct and the suffix
\(0\) for the second.  Its track tree has alphabet \(\{0,1\}^2\).  It satisfies
\(P\) exactly when some node has first bit \(1\) and its left child has second
bit \(1\).  At this first use, let \(E\subseteq T\) be finite and
predecessor-closed, put
\[
 \operatorname{Ft}(E)=\{x\in E:x0\notin E\ \land\ x1\notin E\},
\]
and follow Rabin in calling \(\operatorname{Ft}(E)\) the terminal-node frontier
and \(E\) *frontiered* exactly when every
\(x\in E\setminus\operatorname{Ft}(E)\) has both \(x0,x1\in E\).  The
adjective names a property of \(E\), not a separate tree object.  It is not
redundant with predecessor closure, which permits a node with exactly one
child; the finite-tree automaton, Lemma 3.12 lift, and p. 34 emptiness base all
require both children outside the frontier.  Such a finite subtree can contain
the witness node and child and record the witness condition; the finite-tree
definability fact plus Lemma 3.12 lifts this to an infinite-tree automaton.
This is a handbook-worked instance of the source's principal-formula
construction, not a diagram or fully printed transition table from Rabin's
article.

## Theorem 3.1 and the sequential-word dependency

Chapter III first recalls Büchi acceptance for nondeterministic sequential
automata and Muller acceptance for deterministic sequential automata.  It
invokes McNaughton's theorem that the two define the same \(\omega\)-word
languages.  That result is an external dependency, not reproved here.

Theorem 3.1 starts with a tree transition table
\(\mathfrak A_0=\langle S,M\rangle\) and an automaton-definable language
\(B\subseteq S^\omega\).  It considers the \(\Sigma\)-valued trees for which
there is one \(\mathfrak A_0\)-run \(r\) such that every path \(\pi\) has state
sequence \((r\mathbin{\upharpoonright}\pi)_\omega\in B\).  This tree language
is finite-automaton definable.

The proof selects a deterministic Muller word automaton
\[
 \mathfrak B=\langle U,K,u_0,H\rangle,
 \qquad H\subseteq\mathcal P(U),
\]
for \(B\).  The tree automaton has product state set \(U\times S\), simulates
the unique word-automaton run along each path together with the tree-table
run, and designates
\[
 \overline F
 =\{C\subseteq U\times S:p_1(C)\in H\}.
\]
This proves the path-language absorption directly.  The deterministic word
automaton is essential to having one coherent first-coordinate run shared by
the branching product.

## Dual acceptance and the complementation proof

Definition 3.5 introduces a finite sequence
\[
 \Omega=((L_i,U_i))_{1\leq i\leq k}
\]
of pairs of state sets.  A mapping \(\phi\) is *of type* \(\Omega\), written
\(\phi\in[\Omega]\), when for some \(i\),
\[
 \operatorname{In}(\phi)\cap U_i\neq\varnothing
 \quad\text{and}\quad
 \operatorname{In}(\phi)\cap L_i=\varnothing.
\]
It is *of type \(\Omega\)-empty*, written \(\phi\in[\Omega,e]\), when it is of
type \(\Omega\) and, for some \(j\), its entire range avoids \(L_j\).

Definition 3.6 then defines
\[
 (v,T_x)\in D(\mathfrak A_0,\Omega,s)
\]
to mean that every run of \(\mathfrak A_0\) rooted in state \(s\) has at least
one path whose state sequence is of type \(\Omega\):
\[
 \forall r\,
 \bigl(r\in\operatorname{Rn}(\mathfrak A_0,(v,T_x))
       \land r(x)=s
       \Rightarrow
       \exists\pi\subseteq T_x\;
       r\mathbin{\upharpoonright}\pi\in[\Omega]\bigr).
\]
This is dual to Definition 1.5's \(\exists r\,\forall\pi\) prefix.  Because
the transition table may have no run from \(s\), dual acceptance can hold
vacuously; the universal implication is the literal source clause.

Lemma 3.6 enumerates
\(\mathcal P(S)\setminus(F\cup\{\varnothing\})\), and this list can be empty.
For the zero-length sequence \(\langle\rangle\), no path is of the indicated
type, so
\[
 D(\mathfrak A_0,\langle\rangle,s)
\]
holds exactly when there is no run rooted in \(s\).  Rabin's positive-length
induction does not state this case.  The handbook therefore defines the
one-pair sequence \(\Omega^\dagger=((S,S))\) solely for this repair.  Every
infinite path map into finite nonempty \(S\) has a nonempty infinitely
recurring set and hence cannot both meet and avoid \(S\).  Thus
\([\Omega^\dagger]=\varnothing\) and
\[
 D(\mathfrak A_0,\Omega^\dagger,s)
 =D(\mathfrak A_0,\langle\rangle,s).
\]
This exact normalization supplies the omitted input to the source's
length-one base; it is not a new acceptance semantics.

Lemma 3.6 effectively transforms the complement of an ordinary automaton
language into one of these dual languages.  The pair sequence is therefore
internal to the complementation construction; it must not be retrofitted into
Definition 1.5 as the ordinary automaton's acceptance component.

The remainder of the proof has the following exact architecture.

1. Lemma 3.2 shows that a recursively marked family of local ordinary
   automaton obligations is automaton definable.  Its simultaneous-run
   construction merges active copies that reach the same state, retaining
   only finitely many representatives at each node.  A sequential automaton
   checks the necessary condition along paths, and Theorem 3.1 absorbs it.
2. Endless deferral chains among activated obligations must be excluded.  For
   a nonempty set \(H\) of obligations, Rabin fixes a mapping
   \(h\mapsto H_h\subseteq H\) and calls it *well founded* exactly when there is
   no infinite sequence \(h_1,h_2,\ldots\) such that
   \(h_{m+1}\in H_{h_m}\) for every \(m\).  This condition constrains the
   obligation-dependency relation; it is neither the ordinary path-acceptance
   condition nor the simultaneous-run merge in Lemma 3.2.  Lemma 3.3
   equivalently decomposes \(H\) into disjoint ordinal strata with every member
   of \(H_h\) in a strictly lower stratum.  Lemma 3.4 uses that characterization
   to convert the resulting marked family into an ordinary tree automaton, and
   Lemma 3.11 uses the same condition in the arbitrary-sequence half-step.
3. Lemmas 3.7--3.8 turn the local dual conditions into new dual languages,
   with Lemma 3.8 producing a sequence whose last lower set is empty.
4. Lemmas 3.9--3.10 handle the half-step in which
   \(L_k=\varnothing\).  Lemma 3.11 handles arbitrary \(\Omega\) by a
   well-founded family.  The converse direction of Lemma 3.11 defines its
   stages by transfinite induction.
5. After the handbook-owned zero-length normalization, Section 3.11 inducts
   on positive lengths.  First it proves ordinary
   automaton definability for \(L_k=\varnothing\) using Lemma 3.2; then it
   proves the arbitrary case using Lemma 3.4.  Together with Lemma 3.6 this is
   Theorem 1.5.

It is therefore accurate to say that transfinite induction occurs inside the
complementation proof, specifically in the well-founded decomposition and the
construction used for Lemma 3.11.  It is too vague to replace the displayed
finite-state, marked-tree, dual-language, and induction-on-\(|\Omega|\)
architecture by the phrase “a transfinite complementation proof.”

## The source's actual emptiness argument

Section 3.12 does not invoke a regular-tree basis theorem.  Its effective
emptiness proof is as follows.

1. Given \(\mathfrak A=\langle S,M,s_0,F\rangle\) over \(\Sigma\), form a
   one-letter automaton by replacing \(M(s,\sigma)\) with the union over all
   \(\sigma\in\Sigma\).  A run of the one-letter table is a run on some
   \(\Sigma\)-labelled tree, so original nonemptiness reduces to acceptance of
   the unique one-letter full tree.
2. Effectively complement that automaton and apply Lemma 3.6.  Emptiness is
   thereby reduced to deciding whether the unique full tree lies in
   \(D(\mathfrak A_0,\Omega,s_0)\).  If \(\Omega\) is empty, replace it by
   \(((S,S))\) using the exact equivalence above.
3. Repeat the same two half-steps used in complementation.  An arbitrary
   length-\(k\) sequence reduces to finitely many length-\(k\) sequences with
   \(L_k=\varnothing\).  In the second reduction, the exhaustive statement
   must permit every \(H\subseteq U_k\), including \(H=\varnothing\).  The
   empty choice is the direct shorter question at the current root; each
   nonempty choice gives the source's restricted-table questions of length
   \(k-1\).  Definition 3.7 retains the current
   table's state set \(S\) and replaces each transition set \(M(s)\) by
   \(M(s)\cap(S'\times S')\).  Its runs are precisely the original runs whose
   states strictly below the root lie in \(S'\); the root state need not lie
   there.
4. In the base case \(k=1\), \(L_1=\varnothing\), Lemmas 3.9 and 3.14 reduce
   the question to a finite set
   \(U_0=\{s_1,\ldots,s_m\}\subseteq U_1\), with \(m\geq0\), and finite
   frontiered trees \(E_0,\ldots,E_m\) meeting the universal finite-run
   condition.  When \(m=0\), only \(E_0\) remains and it must admit no run
   from the current root state.  König compactness makes this finite
   obstruction equivalent to absence of an infinite run.
5. That last existence statement is expressible in the weak monadic
   second-order theory of the two-successor tree.  Rabin cites Doner and
   Thatcher--Wright for its decidability.  This is an external theorem
   dependency at the base of the source's emptiness proof.

Rabin's printed p. 34 says that both \(H\) and \(U_0\) are nonempty.  That
wording is not an exhaustive equivalence.  For the first clause, take
\[
 R=\{s,a,u,b\},\quad
 N(s)=\{(a,a)\},\quad N(a)=\{(a,a)\},\quad
 N(u)=\{(b,b)\},\quad N(b)=\{(b,b)\},
\]
and
\(\Omega=((\varnothing,\{a\}),(\varnothing,\{u\}))\).  The unique run from
\(s\) already has an \(\Omega_1\)-type path, while the only nonempty choice
\(H=\{u\}\) fails from \(u\); \(H=\varnothing\) is the required branch.  For
the base clause, take
\[
 R=\{s,u,a\},\quad N(s)=\varnothing,\quad
 N(u)=\{(a,a)\},\quad N(a)=\{(a,a)\},\quad
 \Omega=((\varnothing,\{u\})).
\]
Dual acceptance from \(s\) is vacuous, while the only nonempty candidate
\(U_0=\{u\}\) cannot be hit below a run rooted in \(u\).  The empty choice
and a finite no-run obstruction are necessary.  The handbook preserves the
printed nonempty branches and explicitly adds these two empty branches as its
own correction.

With the zero-length normalization and the two empty-witness completions,
Theorem 1.6 is effective.  Rabin announces an elementary-recursive
qualification, but the handbook records it only as a false historical
complexity claim and does not retain it in view of Meyer's later lower bound.
The article closes the base case by the finite-tree/weak-second-order result,
not by proving a modern regular-tree-model or basis theorem.  A later survey
may supply a basis-theorem route, but it must be attributed separately rather
than projected backward onto Rabin 1969.

## Finite trees inside the infinite-tree proof

Section 3.10 defines a finite binary tree as a finite predecessor-closed
\(E\subseteq T\), with
\[
 \operatorname{Ft}(E)=\{x\in E:x0\notin E\ \land\ x1\notin E\},
 \qquad
 x\in E\setminus\operatorname{Ft}(E)\Longrightarrow x0,x1\in E.
\]
As fixed at first use above, \(\operatorname{Ft}(E)\) is the terminal-node
frontier and *frontiered* is the source's name for the second displayed
property of \(E\).  Predecessor closure alone does not imply that property.
A finite valued tree labels only \(E\setminus\operatorname{Ft}(E)\).  A
finite-tree automaton is
\[
 \langle S,M,s_0,f\rangle,
 \qquad f\notin S,
 \qquad
 M:S\times\Sigma\longrightarrow
   \mathcal P\bigl((S\times S)\cup\{(f,f)\}\bigr).
\]
It accepts when some run begins in \(s_0\) and assigns the distinguished
external symbol \(f\) at every \(x\in\operatorname{Ft}(E)\); because
\(f\notin S\), this reserved frontier value is not a state.  The source states
that these
finite-tree languages form a Boolean algebra and correspond to relations on
finite node sets definable in weak second-order logic.

Lemma 3.12 lifts an automaton-definable collection of finite trees to the
infinite trees having some accepted finite initial subtree.  Corollary 3.13
uses that lemma to supply the principal-formula case deferred in Theorem 1.7.
Lemma 3.14 uses König's Infinity Lemma to extract a finite set of run-state
obligations from a condition meeting every infinite run.  These finite-tree
results support the infinite-tree construction; they do not change \(S2S\)
into weak logic or make the input a finite tree.

## Chapter II applications and their standing

The article is not only a proof of Theorem 1.1.  Its application chapter must
at least be accounted for even when the handbook gives the tree-automata
presentation primary emphasis.

- Theorem 2.1 decides the monadic second-order theory of countable linear
  orders by interpreting each such order in the rational order coded inside
  the binary tree.  Corollary 2.2 decides the weak second-order theory of all
  linear orders; Corollary 2.3 treats countable well-orders.
- Theorem 2.4 decides the monadic second-order theory of a unary function on a
  countable domain by embedding its connected components in definably coded
  enveloping algebras.  Corollary 2.5 gives the weak theory for arbitrary
  unary functions.
- Theorem 2.6 represents the closed subsets and the \(F_\sigma\) subsets of
  Cantor space by node sets.  Theorems 2.7--2.9 derive decidability results for
  ordered Cantor space, its \(F_\sigma\)-set lattice with the closed sets
  distinguished, and the unit interval analogue.
- Theorems 2.10--2.11 pass through Stone representation to countable Boolean
  algebras with quantification over ideals and arbitrary Boolean algebras with
  a sequence of distinguished ideals.
- Section 2.5 codes a Gale--Stewart strategy by a subset of \(T\) and writes an
  \(S2S\) sentence expressing that every \(F_\sigma\) payoff set is determined.
  Rabin presents this as showing that Wolfe's theorem is among the statements
  decided by the procedure, not as a new proof of the strongest determinacy
  theorem mentioned there.

The reader need not reproduce every application proof inside `N-c-014.d`, but
it must not describe the 35-page paper as if pp. 11--17 did not exist.  A
compact application map with the interpretation method and result boundaries
is sufficient unless another registered obligation requires a full treatment.

## Source qualifications and noninterchangeable presentations

1. Rabin's ordinary automaton uses a designated family
   \(F\subseteq\mathcal P(S)\).  The \((L_i,U_i)\) sequence belongs to the
   dual-complement construction.
2. The input is an entire infinite labelled binary tree.  Acceptance examines
   every infinite path of one global run.  This is neither finite-word
   recognition nor finite-tree/weak-set recognition.
3. The formula-to-automaton proof depends crucially on complementation for
   negation and universal set quantification.
4. Theorem 3.1 depends on the deterministic Muller presentation supplied by
   McNaughton's theorem for \(\omega\)-words.
5. The complementation proof contains transfinite reasoning but is also an
   explicit finite-state construction organized through marked trees,
   simultaneous runs, dual languages, and induction on the number of pairs.
   Lemma 3.6 can produce zero pairs; the handbook-owned \(((S,S))\)
   normalization supplies the source's omitted initial case.
6. The emptiness proof uses the weak second-order finite-tree result of Doner
   and Thatcher--Wright at its base.  A later regular-tree basis proof is a
   distinct presentation.  Rabin's printed nonempty \(H\) and \(U_0\)
   clauses omit required empty branches, which the handbook restores and
   proves separately.
7. The article states an elementary-recursive decision-procedure strength.
   Meyer's 1975 ICM report states a non-elementary tower lower bound and credits
   the theory-of-two-successors-and-prefix case to Meyer and Stockmeyer, so the
   handbook must identify Rabin's complexity qualification as a false
   historical claim and retain only decidability and effectiveness.
8. The paper's Buechi/Muller word-automaton discussion, its infinite-tree
   automata, and its Chapter II interpretation results have separate roles and
   must not be collapsed into one generic “automata-theoretic method.”

## Reader-facing integration and review history

The integrated presentation in
`handbook/parts/p09/presentations/n-c-014.tex` preserves the ordinary/dual
acceptance distinction and contains all of the following:

- the binary specialization of Definition 1.1 with the two orders and the
  source's \(\Lambda\)-versus-editorial-\(\epsilon\) notation boundary;
- the arbitrary-root valued-tree definition or an explicit full-root
  normalization;
- Theorems 1.3--1.6 as the exact closure/decision dependencies;
- the typed \(n\)-bit track map, Theorem 1.7's normal-form construction, and
  the worked two-track principal-formula example above;
- Theorem 1.10's converse run encoding and the exact sentence-to-nonemptiness
  conclusion;
- the full two-half-step complementation architecture and the precise locus
  of transfinite induction, with the zero-length pair sequence normalized by
  an exact handbook-owned one-pair equivalent;
- the source's one-letter/dual-language/weak-theory emptiness argument in
  place of the current regular-tree suggestion, with Rabin's two printed
  nonempty-witness gaps exposed and repaired;
- Rabin's printed elementary-recursive qualification identified as a
  historical claim refuted by the later non-elementary lower bound recorded in
  Meyer's ICM report, while preserving the decidability and effectiveness
  result;
- a compact map of Chapter II's applications;
- an explicit attribution of the modern basis-theorem route to Thomas rather
  than Rabin; and
- a proof-status sentence saying what is reconstructed in the handbook and
  what remains in the 35-page source.

The Round 1--3 and Round 5--7 report hashes and rejections, together with the
pre-filing Round 4 withdrawal, are preserved in the Rabin board ledger and chair
transcript.  The reader, source note, and compact record define `frontiered` at
first use, state that it is a property of the finite tree, distinguish it from
predecessor closure, and identify the later arguments that require it.  They
also identify \(f\notin S\) as a distinguished external frontier value rather
than a state.  The bibliography retains the inspected institutional scan URL
and AMS DOI and the later Meyer source.

Admission requires three fresh independent ACCEPT verdicts on one unchanged
hash-pinned snapshot and no unresolved blocker or must-fix.  At the time of this
revision the next such review is Round 8.  This paragraph records the
pre-review state of that snapshot; it does not itself claim terminal admission.
