# Round-three mathematical and proof-correctness review

## Scope, evidence boundary, and frozen identity

I reviewed only the round-three seven-object snapshot named in the charter. I
did not read `ledger.md`, `transcript/chair.md`, any round-one or round-two
transcript, either other round-three transcript, or any earlier Part IX board
record, and I did not contact another reviewer. I ran no test, test harness,
checker, repository script, Python utility, TeX command, handbook build, or
handbook-PDF render. The only command used beyond direct line reading was the
platform `Get-FileHash -Algorithm SHA256` command for the permitted identity
check.

All seven recomputed identities agree exactly with the charter:

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf` | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` | match |
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf` | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` | match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `0C72F461A83E421AAFF950E2CBA03FD386EEA088BAC70E9D8E30E86052E977D2` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | match |
| `handbook/bib/handbook.bib` | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` | match |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | `75D66211C3520522D7530C609221AB20C0409EBBA6CBCD29BD9C3CD9B8D8DD27` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `C2526F8FF7FAFFE4DB2902799BB968E0B21491B57CCC40F6548EEB6BAA534031` | match |

## Source pages and manuscript records inspected

I visually inspected the following existing page images at original detail:

- `journal-page-1.png` through `journal-page-5.png`, printed journal pp.
  181--185: metadata and execution convention; safety and liveness clauses;
  uniform and absolute liveness, leads-to, predictive, and until examples;
  topology, Theorems 1--2 and both proofs, Corollaries 1.1--2.1, Boolean
  closure; conclusion and references.
- `tr-page-01.png` through `tr-page-11.png`: outer cover; title/abstract leaf;
  all internally numbered body pp. 1--9, including the two unnumbered
  corollaries and the report references.

I directly read every in-scope line of the five textual records:

- `handbook/parts/p09/presentations/n-c-012.tex`, lines 2632--3011;
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 710--718;
- `handbook/bib/handbook.bib`, lines 6056--6080;
- `spec/research/p09-alpern-schneider-1985-source-note.md`, lines 1--681; and
- `spec/research/p09-source-presentations-lot2-3.md`, lines 395--552.

The journal image gives the title, authors, journal, volume 21 number 4, date
7 October 1985, pp. 181--185, communicating editor, receipt 5 November 1984,
revision 20 February 1985, and the printed Elsevier/North-Holland copyright.
The report cover and title leaf give TR 85-650, October 1984, the exact inner
date 30 October 1984, and revision 20 February 1985. The DOI and Cornell access
routes are stated consistently in the bibliography, source note, and compact
record. The report and journal have the same substantive definitions,
examples, theorems, proofs, and closure statements. In particular, journal
p. 184 and report body p. 8 both say “closed under intersection” in the second
corollary. The report is kept separate from, and does not replace, the journal.

## Independent mathematical derivation

### 1. Universe, typing, empty prefix, and the null universe

Let (X=S^\omega) and (S^*=\bigcup_{n<\omega}S^n). The empty word
\(\epsilon\) is the unique member of (S^0), hence belongs to (S^*). For
(s\in S), the objects \(\langle s\rangle\in S^1\) and
\(s^\omega\in X\) have different types. If (u\in S^*) and (y\in X),
then (u\mathbin{\smallfrown}y\in X). These typings make the leads-to and
Theorem 2 witnesses well formed.

The explicit hypothesis (S\ne\varnothing) at reader lines 2635 and
2669--2674 is necessary. If (S=\varnothing), then (X=\varnothing) while
(S^*=\{\epsilon\}). The only property (P=\varnothing) is dense in the
empty topological space, but the continuation clause at (u=\epsilon) is
false because no (y\in X) exists. Thus “liveness iff dense” fails. Moreover,
there is no liveness property at all, so Theorem 1 cannot factor the only
property into safety and liveness factors. This is exactly the disclosed
hypothesis repair, not an added restriction on an ordinary state space.

For (S\ne\varnothing), (X\ne\varnothing) by a constant execution. The
empty-prefix instance of liveness is
\(\exists y\in X\;(\epsilon\mathbin{\smallfrown}y=y\in P)\), so every live
property is nonempty. The terminating-run convention of repeating the final
state gives an element of (X), rather than confusing a terminal finite word
with an execution. Property satisfaction is correctly typed as membership
(x\in P\) and program satisfaction as inclusion of its execution set in
(P\).

### 2. Safety and liveness quantifiers

The safety clause at reader lines 2677--2686 has the required quantifier
order:

\[
 \forall x\in X\;
 \bigl(x\notin P\Rightarrow
 \exists n\in\omega\;\forall y\in X\;
 (x{\upharpoonright}n)\mathbin{\smallfrown}y\notin P\bigr).
\]

Thus the finite prefix may depend on the violating execution, but the failure
must persist for every continuation. The article's phrase “(u) is live for
(P)” is exactly the relation
\(\exists y\in X\;u\mathbin{\smallfrown}y\in P\). Universally closing it
over (u\in S^*) yields ordinary liveness. Failure of that universal clause
gives one finite (u) for which every continuation violates (P), hence an
irremediable finite bad prefix. This validates the formal part of the source's
maximality argument; it does not prove uniqueness or correctness of the
informal “good thing” intuition, and the reader does not promote it.

The safety/liveness examples and the proof-method motivation are reported at
their proper strength. In particular, a repeated adjacent value finitely
witnesses violation of “the value changes at every step,” so the property is
safety under the displayed definition. The source's comparison with Lamport
is only asserted under finite-stuttering invariance and is not presented as an
independent proof about the cited formulation.

### 3. Uniform and absolute liveness

Uniform liveness is

\[
 \exists y\in X\;\forall u\in S^*\;
 u\mathbin{\smallfrown}y\in P,
\]

while absolute liveness is nonemptiness of (P) together with

\[
 \forall y\in X\;
 (y\in P\Rightarrow\forall u\in S^*\;
 u\mathbin{\smallfrown}y\in P).
\]

If (P) is absolutely live, choose one (y\in P); the universal prefixing
clause makes that (y) a uniform witness. A uniform witness can be reused for
each prefix, proving ordinary liveness. Hence
absolute \(\Rightarrow\) uniform \(\Rightarrow\) ordinary, with neither
quantifier order silently collapsed into another.

The names have admissible standing: each names a semantic class of properties,
its exact definition is local, the distinction from ordinary liveness and
from the other stricter class is explicit, and the leads-to and predictive
examples immediately use it.

### 4. Leads-to: exact characterization and every degeneration

For the reader's state-set rendering, define

\[
 P_{12}=\{x\in X:\forall i\in\omega\,
 (x_i\in E_1\Rightarrow\exists j>i\;x_j\in E_2)\}.
\]

This formalizes “followed later,” with strict (j>i). The round-three claim is
correct:

\[
 P_{12}\text{ is uniformly live but not absolutely live}
 \quad\Longleftrightarrow\quad
 E_1\ne\varnothing,
 E_2\ne\varnothing,
 S\setminus(E_1\cup E_2)\ne\varnothing.
\]

Sufficiency: choose (e_2\in E_2). For every finite (u), the suffix
(e_2^\omega) answers every (E_1)-occurrence in (u). If
(e_2\in E_1\cap E_2), every request inside the suffix is answered by its next
occurrence, so (e_2^\omega) is still a uniform witness. Next choose
(e_1\in E_1) and neutral
(c\in S\setminus(E_1\cup E_2)). The execution (c^\omega) has no requests
and satisfies (P_{12}), but
\(\langle e_1\rangle\mathbin{\smallfrown}c^\omega\) has an unanswered
request. Therefore absolute liveness fails.

Necessity: if (E_1=\varnothing), then (P_{12}=X), which is absolutely
live. If (E_1\ne\varnothing) and (P_{12}) is uniform, apply the common
suffix after \(\langle e_1\rangle\); that suffix must contain an (E_2)-state,
so (E_2\ne\varnothing). Finally suppose the neutral set is empty. Every
satisfying (y\in P_{12}) contains an (E_2)-state: if it contains an
(E_1)-state, satisfaction supplies a later (E_2)-state; if it contains no
(E_1)-state, (S=E_1\cup E_2) forces every state of (y) into (E_2).
Consequently, after any finite (u), some (E_2)-state in (y) answers all
requests in (u), while (y\)'s own obligations remain satisfied. Since
(E_2\ne\varnothing) also makes (e_2^\omega\in P_{12}), the property is
absolutely live. Failure of absolute liveness therefore forces a neutral
state.

This also exhausts the degeneracies, including overlaps between (E_1) and
(E_2):

| Case, with (S\ne\varnothing) | Exact status |
|---|---|
| (E_1=\varnothing) | (P_{12}=X); absolute, uniform, and ordinary liveness all hold. |
| (E_1\ne\varnothing, E_2=\varnothing) | The prefix \(\langle e_1\rangle\) has no satisfying continuation; ordinary and uniform liveness fail. |
| (E_1,E_2\ne\varnothing), neutral set nonempty | Uniform liveness holds and absolute liveness fails. |
| (E_1,E_2\ne\varnothing), neutral set empty | Absolute liveness holds, hence so do uniform and ordinary liveness. |

The journal p. 183/report body p. 5 source ownership is accurately separated:
the source conditions liveness on satisfiable (E_2), makes an unqualified
non-absolute claim, and gives a witness that presupposes an (E_1)-event and a
neutral execution. The exact three-condition theorem and proof are visibly
handbook-owned, and source-critical finding AS-06 records the printed defect.

### 5. Predictive property and all (A,B) degeneracies

For the eliminable property name (P_{A,B}) at reader lines 2813--2819, assume
the four stated nondegeneracy conditions. Given a nonempty prefix (u), if
(u_0\in A), append (b^\omega) for any (b\in B); otherwise append
(c^\omega) for any (c\in S\setminus B). Given the empty prefix, choose
(a\in A) and then an eventually all-(B) continuation. Thus every prefix has
a satisfying continuation.

No suffix (y) is uniform. Choose (a\in A) and (d\in S\setminus A). If
(y) is eventually always in (B), prefixing (d) selects the eventually
always outside-(B) branch and fails it. If (y) is not eventually always in
(B), prefixing (a) selects and fails the eventually always-(B) branch.
This proves the exact ordinary-but-not-uniform separation.

For completeness, without the four hypotheses the liveness clause holds
exactly when

\[
 (A=\varnothing\ \text{or}\ B\ne\varnothing)
 \quad\text{and}\quad
 (S\setminus A=\varnothing\ \text{or}\ S\setminus B\ne\varnothing).
\]

The first conjunct is forced by prefixes whose first state lies in (A); the
second is forced by prefixes whose first state lies outside (A). If both
(A) and its complement are nonempty, no suffix can be uniform, because it
would have to be eventually always in both (B) and its complement. If
(A=S), a constant (B)-suffix is uniform exactly when (B\ne\varnothing);
if (A=\varnothing), a constant outside-(B) suffix is uniform exactly when
(S\setminus B\ne\varnothing). Thus the reader's four assumptions are exactly
adequate for the advertised separation and do not conceal a degenerate case.

### 6. Until, total correctness, and absence of a dichotomy

The source-exact name is “until.” Its property is the conjunction of eventual
(E_2) and the requirement that every state preceding the first witnessing
(E_2) be in (E_1). The latter conjunct is safety: a first state outside
(E_1) seen before any (E_2) is a finite irremediable witness. Eventual
(E_2) is liveness when (E_2\ne\varnothing), because any finite prefix can
be extended by an (E_2)-state. Their conjunction is generally neither. For
example, if (e_1\in E_1\setminus E_2), (e_2\in E_2), and
(c\in S\setminus(E_1\cup E_2)), the execution (e_1^\omega) violates until
but every one of its finite prefixes remains extendible by (e_2^\omega), so
until is not safety; the prefix \(\langle c\rangle\) has no satisfying
extension, so until is not liveness. Degenerate choices can collapse it to one
class or to (X) or \(\varnothing\), which is why the reader correctly says
“generally neither.” Total correctness is likewise reported only as the
intersection of partial correctness and termination. Neither example supports
a safety/liveness dichotomy, and the reader asserts none.

### 7. Prefix topology

For (u\in S^*), the cylinder
\([u]=\{x\in X:u\preceq x\}\) is nonempty because (S\ne\varnothing), and
the cylinders form the prefix basis.

Safety implies closedness: if (x\notin P), safety supplies (n) such that
every continuation of (x{\upharpoonright}n) lies outside (P). Hence
\([x{\upharpoonright}n]\subseteq X\setminus P\), so every point of the
complement has a basic open neighborhood in the complement. Conversely, if
(X\setminus P) is open and (x\notin P), a basic cylinder containing (x)
lies in (X\setminus P), and its defining finite prefix is a bad prefix.

Liveness implies density: every nonempty basic cylinder \([u]\) meets (P)
at the satisfying continuation of (u), and hence every nonempty open set
meets (P). Conversely, if (P) is dense, every nonempty \([u]\) meets
(P), so some (u\mathbin{\smallfrown}y\in P). Thus safety is exactly
closedness and liveness exactly density. The source states these equivalences;
the direction proofs are correctly identified as handbook-supplied.

### 8. Theorem 1 and Corollary 1.1

For arbitrary (P\subseteq X), let (C=\overline P) and
(L_P=X\setminus(C\setminus P)=P\cup(X\setminus C)). Then (C) is closed and

\[
 C\cap L_P=C\cap\bigl(P\cup(X\setminus C)\bigr)=P.
\]

If (L_P) were not dense, a nonempty open (O) would be disjoint from it, so
(O\subseteq C\setminus P). Therefore (P\subseteq C\setminus O). The set
(C\setminus O=C\cap(X\setminus O)) is closed, contains (P), and is strictly
smaller than (C) because nonempty (O\subseteq C). This contradicts the
minimality of (C=\overline P). Thus (L_P) is dense and the factorization is
valid, including the edge cases (P=\varnothing) (factors \(\varnothing,X\))
and (P=X) (factors (X,X)).

Only the closed factor is canonical as the least closed superset. The theorem
does not establish uniqueness of the pair, computability, or preservation by
a formula language. The source prints this proof; the reader's (L_P) is a
declared eliminable alpha-renaming of its (L).

If a denotation family is closed under complement, intersection, and
topological closure, then (C=\overline P) is expressible and

\[
 L_P=X\setminus\bigl(C\cap(X\setminus P)\bigr)
\]

is expressible. This proves Corollary 1.1 under exactly its stated hypotheses,
without claiming that an arbitrary temporal syntax has those closures. The
subsequent Plotkin temporal-logic decomposition is correctly reported only as
an independently unverified 1983 private-communication claim.

### 9. Theorem 2 and the singleton state space

Assume (|S|>1), choose distinct (a,b\in S), and define (E_a,E_b) as the
eventually constant all-(a) and all-(b) properties. For any finite (u),
(u\mathbin{\smallfrown}a^\omega\in E_a), so (E_a) is live; similarly
(E_b) is live. If an execution belonged to both, after the maximum of the two
eventuality bounds all its states would equal both (a) and (b), impossible.
Thus (E_a\cap E_b=\varnothing), and distributivity gives

\[
 (P\cup E_a)\cap(P\cup E_b)=P\cup(E_a\cap E_b)=P.
\]

Each factor is live because it contains a live set. This proves Theorem 2.
The reader's (E_a,E_b) are exact eliminable alpha-renamings of the source's
(L_a,L_b).

If (|S|=1), then (X=\{s^\omega\}). Its only dense subset is (X), so the
empty property cannot be an intersection of two live properties. The
cardinality hypothesis is therefore material, not a proof convenience. In
this singleton case the only live, uniformly live, and absolutely live
property is (X); both subsets \(\varnothing\) and (X) are safety.

### 10. Corollary 2.1, countermodel, and exact repair

Both source versions require only intersection closure, while Theorem 2 needs
the unions (P\cup E_a) and (P\cup E_b). The printed statement is false,
not merely unproved by that construction.

Let (Q=\{a^\omega\}) and

\[
 \mathcal F=\{X,E_a,E_b,Q,\varnothing\}.
\]

This family is intersection-closed: (Q\subseteq E_a),
(Q\cap E_b=\varnothing), (E_a\cap E_b=\varnothing), and intersections
with (X), self, or \(\varnothing\) stay in the family. It contains the
disjoint expressible liveness properties (E_a,E_b). Its live members are
exactly (X,E_a,E_b): (Q) is not dense because
\([\langle b\rangle]\cap Q=\varnothing), and \(\varnothing\) is not dense.
Intersections of two members of \(\{X,E_a,E_b\}\) are only
(X,E_a,E_b,\varnothing), never (Q). Hence the expressible (Q) has no
factorization of the printed kind.

Replacing “intersection” closure by union closure is sufficient and minimal
for the displayed construction: (P\cup E_a) and (P\cup E_b) are then
expressible live properties with intersection (P). Complement plus
intersection closure also suffices by De Morgan. Reader lines 2938--2971 keep
the literal source wording, countermodel, and handbook-owned repair distinct.

### 11. Every Boolean-closure entry

Closed sets are closed under arbitrary intersections and finite unions, so
safety is closed under the two binary operations in the table. Any union
containing a dense set is dense, so liveness is closed under binary union.
For (|S|>1), (E_a,E_b) are dense but have empty, hence nondense,
intersection, proving failure of intersection closure.

Complement closure also fails in general. For distinct (a,b\in S), the
singleton (Q=\{a^\omega\}) is closed: every (x\ne a^\omega) first differs
from (a) at some finite position, giving a cylinder disjoint from (Q).
But (X\setminus Q) is not closed, because every cylinder about (a^\omega)
contains an execution that later switches to (b). Thus safety is not closed
under complement. Also (X\setminus Q) is dense—every finite prefix can be
continued to an execution other than (a^\omega)—whereas its complement (Q)
is not dense because \([\langle b\rangle]\) misses it. Thus liveness is not
closed under complement. Finally, if (P) is closed and dense, then
(P=\overline P=X); the whole space is itself both. Every table entry and the
“only the whole space” claim are correct.

### 12. Terminology, ownership, and cross-record reconciliation

The terms and symbols singled out by M20 satisfy the local terminology rule:

- “live for (P)” is defined as a finite-prefix/property relation, distinguished
  from the universally closed property class, and then used to define it;
- uniform and absolute liveness have exact local quantifiers, semantic-class
  standing, proved nonredundancy, and immediate use;
- (P_{A,B}) is explicitly an eliminable name for one displayed property;
- (L_P) and (E_a,E_b) are explicitly eliminable alpha-renamings used in
  the corresponding proofs; and
- (Q) and \(\mathcal F\) are explicitly eliminable names for a singleton
  property and a denotation family used only in the countermodel.

The detailed reader, shared definition, bibliography, source note, and compact
presentation agree claim by claim. The shared definition is the same semantic
bad-prefix/extension definition at a deliberately shorter level and does not
classify formula typography. Source ownership is consistently disclosed:
the article prints the formal definitions, examples, Theorems 1--2 and their
proofs, both corollary texts, and Boolean claims; it states but does not prove
the topological equivalences; the reader supplies those direction proofs, the
typed state-set examples, the leads-to repair, and the Corollary 2.1
countermodel and correction. No source repair is laundered into source text.

## Findings

No blocker, must-fix, should-fix, consider, discard, or unresolved-user record
arises under the mathematical and proof-correctness mandate. The repaired
leads-to characterization, the Theorem 1 minimality proof, Theorem 2, the
Corollary 2.1 countermodel and repair, and every edge case and closure claim are
mathematically correct on the frozen snapshot.

## Mandatory coverage

| Point | Status | Evidence/result |
|---|---|---|
| M01 | checked-clean | All seven SHA-256 identities recomputed and matched before substantive review. |
| M02 | checked-clean | Journal pp. 181--185 and all eleven report file pages visually read at original detail. |
| M03 | checked-clean | Identity, venue/date/pages, DOI record, receipt/revision dates, TR number/dates, access routes, and rights statement reconciled. |
| M04 | checked-clean | Separate page maps and substantive agreement verified; both versions print intersection in the second corollary. |
| M05 | checked-clean | (S\ne\varnothing), (S^*,S^\omega), empty word, concatenation, prefix, singleton words, constant runs, property/program standing, membership, and terminal padding checked. |
| M06 | checked-clean | Exact safety quantifier order and bad-prefix equivalence rederived. |
| M07 | checked-clean | “Live for (P),” universal liveness, nonemptiness, empty prefix, and full-space boundary checked. |
| M08 | checked-clean | Motivation, maximality argument, examples, and stuttering qualification retained without strength promotion. |
| M09 | checked-clean | Uniform/absolute definitions, standing, necessity, nonredundancy, use, and inclusion chain proved. |
| M10 | checked-clean | Printed leads-to strengths separated from the handbook fixed-suffix theorem; exact iff and all degeneracies proved. |
| M11 | checked-clean | Predictive property, all four hypotheses, liveness, nonuniformity, and degenerate cases proved. |
| M12 | checked-clean | Source-exact “until,” total-correctness factorization, and no-dichotomy claim checked. |
| M13 | checked-clean | Cylinder basis and both directions of both topological equivalences proved, including the (S=\varnothing) failure. |
| M14 | checked-clean | Theorem 1 algebra, strict minimality contradiction, edge properties, and nonuniqueness/syntax/algorithm boundaries checked. |
| M15 | checked-clean | Corollary 1.1 derived from exactly complement, intersection, and topological-closure expressibility. |
| M16 | checked-clean | Theorem 2 renamings, density, disjointness, factorization, and material (|S|>1) hypothesis checked. |
| M17 | checked-clean | Printed Corollary 2.1 refuted by the stated intersection-closed family; union and Boolean repairs proved. |
| M18 | checked-clean | Every union/intersection/complement entry and the unique closed-dense property proved. |
| M19 | checked-clean | Printed theorem proofs, merely stated topological equivalences, and handbook-owned arguments separated. |
| M20 | checked-clean | Every named term/symbol passes necessity/definition/standing/nonredundancy/use or is expressly eliminable. |
| M21 | checked-clean | Reader, shared definition, bibliography, source note, and compact presentation reconciled claim by claim. |
| M22 | checked-clean | Unlettered standing, rights boundary, topic-only status, and explicit no-test/no-build boundary preserved. |

VERDICT: ACCEPT
