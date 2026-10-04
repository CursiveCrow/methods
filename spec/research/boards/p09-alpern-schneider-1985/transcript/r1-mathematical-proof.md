# Blind opening: mathematical and proof-correctness seat

- Seat: Mathematical and proof-correctness
- Round: r1 blind opening
- Evidence boundary: direct visual reading of all sixteen supplied source-page
  images; direct reading of the seven frozen manuscript/source scopes; direct
  mathematical derivation only. No ledger, chair transcript, prior or current
  board transcript, handbook PDF, test, checker, repository script, TeX
  command, or build was read or run.

## Frozen-identity check

All seven recomputed SHA-256 values match the charter exactly.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf` | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` | match |
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf` | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` | match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `D1844530FA4BA9EC2E8F702763966F8AA3C57BE3A3E3DD5163EEA24E2905033D` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | match |
| `handbook/bib/handbook.bib` | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` | match |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | `B99757CEAADE0045D4663493403112892AC4A199176D7B4A0D244AF23168532F` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `35D27BCC4AE25DE83260CB9356D854F64E99FAAFC6B824A34B85366B553CE872` | match |

## Complete visual-source reading record

I visually read `journal-page-1.png` through `journal-page-5.png`, corresponding
to printed journal pp. 181--185, and `tr-page-01.png` through
`tr-page-11.png`, corresponding to the report cover, title/abstract leaf, and
internally numbered body pp. 1--9. In particular, the safety formula was read
on journal p. 182/report body p. 2; the liveness, uniform-liveness, and
absolute-liveness formulas on journal pp. 182--183/report body pp. 3--4; the
leads-to and predictive prose on journal p. 183/report body p. 5; and the
topology, Theorems 1--2, both corollaries, and Boolean-closure paragraph on
journal p. 184/report body pp. 6--8. The second corollary visibly says
“closed under intersection” in both versions.

## Findings

### F-MP-01 [must-fix] [open] The leads-to separation silently drops hypotheses needed by the printed counterexample

- author: Mathematical and proof-correctness seat r1
- location: `handbook/parts/p09/presentations/n-c-012.tex:2769-2778`;
  `spec/research/p09-alpern-schneider-1985-source-note.md:276-288`;
  `spec/research/p09-source-presentations-lot2-3.md:454-469`; controlling
  source journal p. 183, right column; comparison report body p. 5
  (`tr-page-07.png`).
- claim: The source prints the unqualified statement that any leads-to
  property is not absolute-liveness, then asks the reader to choose a
  satisfying execution containing neither an \(E_1\)- nor an \(E_2\)-event and
  prefix it by one \(E_1\)-event. The reader weakens this to “need not be
  absolutely live” but neither states the existence assumptions which make
  the displayed witness available nor records that this is a repair of an
  overbroad printed claim. For the state-predicate reconstruction at reader
  line 2770, the live-but-not-absolute separation requires at least
  \(E_1\ne\varnothing\), \(E_2\ne\varnothing\), and
  \(S\setminus(E_1\cup E_2)\ne\varnothing\). Merely having an available
  \(E_2\)-state proves liveness (indeed uniform liveness), but does not prove
  failure of absolute liveness. This leaves the nonredundancy example
  mathematically under-specified and silently changes source strength, against
  I3, I6, and I10.
- evidence: Let \(T(E_1,E_2)\) be the property that every \(E_1\)-occurrence is
  followed later by an \(E_2\)-occurrence. If \(e_2\in E_2\), the fixed suffix
  \(e_2^\omega\) works after every finite prefix: it answers all \(E_1\)
  occurrences already in the prefix, and if \(e_2\in E_1\) as well, every
  suffix occurrence is answered by the next suffix occurrence. Thus the
  handbook-owned uniform-liveness inference is correct under
  \(E_2\ne\varnothing\). For non-absolute liveness, however, the printed
  witness needs \(e_1\in E_1\) and a state
  \(c\in S\setminus(E_1\cup E_2)\): then \(c^\omega\in T(E_1,E_2)\), but
  \(e_1\mathbin{\smallfrown}c^\omega\notin T(E_1,E_2)\). Without such a
  neutral execution the conclusion can reverse. Take
  \(S=\{e_1,e_2\}\), \(E_1=\{e_1\}\), and \(E_2=\{e_2\}\). Every
  \(y\in T(E_1,E_2)\) contains an \(e_2\): if it contains an \(e_1\), its own
  obligation supplies a later \(e_2\), and if it contains no \(e_1\), every
  state is \(e_2\). Therefore for every finite \(u\), each \(E_1\)-occurrence
  in \(u\) is answered by an \(e_2\) in \(y\), while all obligations internal
  to \(y\) remain answered. Hence
  \(u\mathbin{\smallfrown}y\in T(E_1,E_2)\) for every \(y\in T(E_1,E_2)\):
  this leads-to property is absolutely live despite \(E_2\) being available.
- correction: At the reader paragraph and both source records, quote or
  paraphrase the source's universal printed claim at its actual strength,
  identify the missing-witness issue as a source-level qualification, and
  state the repaired separation with exact standing and hypotheses. For the
  present state-predicate rendering, one minimal form is: assume
  \(E_1,E_2\subseteq S\),
  \(E_1\ne\varnothing\), \(E_2\ne\varnothing\), and
  \(S\setminus(E_1\cup E_2)\ne\varnothing\); then the property is uniformly
  live but not absolutely live, by the two witnesses above. If “event type” is
  intended to have different standing from a state predicate, define that
  standing and state the analogous three existence assumptions there.
- discussion: pending
- disposition: pending

## Independent derivation record

### Universe, null cases, prefixes, and the two ordinary classes

At `n-c-012.tex:2634-2700`, the typed universe and quantifier order are
correct. \(S^0\) contains the empty word, so the empty word belongs to \(S^*\).
For \(S\ne\varnothing\), every \(u\in S^*\) has an infinite continuation and
every cylinder \([u]\) is nonempty.

The empty-state edge case is correctly repaired at `n-c-012.tex:2665-2670`.
If \(S=\varnothing\), then \(S^\omega=\varnothing\) and
\(S^*=\{\epsilon\}\). The only property, \(\varnothing\), is dense in the
empty space, but the liveness clause at `n-c-012.tex:2692-2694` is false at
\(u=\epsilon\) because there is no \(y\in S^\omega\). Theorem 1 also cannot
produce a liveness factor in that case. Thus \(S\ne\varnothing\) is material,
not cosmetic.

If \(|S|=1\), \(S^\omega\) is a singleton. Its only liveness property is the
whole space, whereas both the empty set and whole space are safety. Theorem 1
still works, but Theorem 2 fails for \(P=\varnothing\), exactly as stated at
`n-c-012.tex:2899-2902`.

The safety clause at `n-c-012.tex:2673-2683` has the required order

\[
 \forall x\in S^\omega\;(x\notin P\Rightarrow
 \exists n\in\omega\;\forall y\in S^\omega\;
 (x{\upharpoonright}n)\mathbin{\smallfrown}y\notin P).
\]

The witness \(n\) may depend on the violating execution, but the universal
suffix quantifier follows that witness. Taking \(n=0\) is legitimate; it says
that the empty prefix is already bad, which can occur only when \(P\) is empty.
The “live for \(P\)” relation at `n-c-012.tex:2685-2689` removes only the
outer universal prefix quantifier. It is therefore a relation between
\(u\in S^*\) and \(P\subseteq S^\omega\), not a property class. Restoring
\(\forall u\in S^*\) gives liveness. At \(u=\epsilon\), the suffix itself must
belong to \(P\), so liveness implies \(P\ne\varnothing\). These readings agree
with journal p. 182 and report body pp. 2--3.

### Uniform and absolute liveness

The definitions at `n-c-012.tex:2734-2757` have the correct dependencies.
For absolute liveness, choose \(y\in P\) using the explicit nonemptiness
conjunct; then the universal prefix clause makes this \(y\) a uniform witness.
For uniform liveness, reuse the one witness \(y\) after each \(u\) to obtain
ordinary liveness. Hence

\[
 \text{absolute}\Rightarrow\text{uniform}\Rightarrow\text{ordinary}.
\]

The first implication would not follow from the universal implication alone
if the empty property were allowed; the manuscript correctly retains the
source's nonemptiness conjunct.

The predictive property at `n-c-012.tex:2780-2800` is correct under its stated
nondegeneracy assumptions. For a nonempty prefix \(u\), if its first state is
in \(A\), append a constant \(B\)-state suffix; otherwise append a constant
\(S\setminus B\)-state suffix. For \(u=\epsilon\), choose an \(A\)-state as the
first state and then remain in \(B\) (or choose the complementary branch).
Thus the property is live. Given any proposed uniform suffix \(y\), if \(y\)
is eventually always in \(B\), prepend a state in \(S\setminus A\); the
required eventually-always-not-\(B\) branch fails. If \(y\) is not eventually
always in \(B\), prepend a state in \(A\); the required eventually-always-\(B\)
branch fails. The assumptions that \(A,S\setminus A,B,S\setminus B\) are all
nonempty supply every witness and make the separation nondegenerate.

### Neither-class examples and topology

The strong-until decomposition at `n-c-012.tex:2802-2810` is correct at its
stated generality qualifier: eventual \(E_2\) is liveness, while forbidding a
non-\(E_1\) event before the first \(E_2\) is safety. Their conjunction can
have both an irremediably bad prefix and a still-repairable all-\(E_1\) prefix,
so it is generally neither class. Total correctness likewise has the stated
partial-correctness/termination factorization. Neither example implies a
dichotomy.

For `n-c-012.tex:2812-2831`, the topology equivalences rederive as follows.
If \(P\) is safety, every \(x\notin P\) lies in a cylinder
\([x{\upharpoonright}n]\subseteq S^\omega\setminus P\), so the complement is
open and \(P\) is closed. Conversely, if the complement is open, a basis
cylinder about each \(x\notin P\) supplies the finite bad prefix. Also, the
liveness clause is exactly \([u]\cap P\ne\varnothing\) for every
\(u\in S^*\). Since \(S\ne\varnothing\) makes every cylinder nonempty and the
cylinders form a basis, this is equivalent to meeting every nonempty open set,
hence to density. The source states these equivalences on journal p. 184/report
body p. 6; the manuscript properly identifies the direction proofs as
handbook-supplied.

### Theorem 1 and Corollary 1.1

At `n-c-012.tex:2833-2866`, let \(X=S^\omega\), \(C=\overline P\), and
\(L_P=X\setminus(C\setminus P)=P\cup(X\setminus C)\). Then

\[
 C\cap L_P=(C\cap P)\cup(C\cap(X\setminus C))=P.
\]

The minimality argument is complete. If \(L_P\) were not dense, there would be
a nonempty open \(O\subseteq X\setminus L_P=C\setminus P\). Hence
\(P\subseteq C\setminus O\). The set
\(C\setminus O=C\cap(X\setminus O)\) is closed, contains \(P\), and is
strictly smaller than \(C\) because \(\varnothing\ne O\subseteq C\). This
contradicts that \(C\) is the least closed superset of \(P\). Thus \(L_P\) is
dense. No step supplies uniqueness of the full factorization, syntactic
expressibility, or an algorithm, so the boundaries at
`n-c-012.tex:2862-2866` are exact.

For Corollary 1.1 (`n-c-012.tex:2868-2875`), closure of the notation under
topological closure makes \(C=\overline P\) expressible; complement and
intersection make \(C\cap(X\setminus P)\) expressible; a final complement
makes \(L_P\) expressible. These are exactly the operations used by the stated
conditional result. The argument does not establish that a particular logic
has those closures.

### Theorem 2 and printed Corollary 2.1

At `n-c-012.tex:2877-2902`, if \(a\ne b\), any finite prefix extends by
\(a^\omega\) into \(E_a\), so \(E_a\) is dense; similarly \(E_b\) is dense. A
sequence in both would be eventually constantly \(a\) and eventually
constantly \(b\), forcing \(a=b\) beyond the larger of the two cutoffs. Thus
\(E_a\cap E_b=\varnothing\). Distributivity gives

\[
 (P\cup E_a)\cap(P\cup E_b)=P\cup(E_a\cap E_b)=P,
\]

and each factor is dense because it contains a dense subset. The alpha-renaming
from the source's \(L_a,L_b\) to \(E_a,E_b\) changes no content.

The denotation-family countermodel at `n-c-012.tex:2917-2936` is valid. In

\[
 \mathcal F=\{X,E_a,E_b,Q,\varnothing\},\qquad Q=\{a^\omega\},
\]

all intersections remain in \(\mathcal F\): \(Q\subseteq E_a\),
\(Q\cap E_b=\varnothing\), and \(E_a\cap E_b=\varnothing\). The only dense
members are \(X,E_a,E_b\). The singleton \(Q\) is not dense because the
cylinder \([b]\) misses it, and \(\varnothing\) is not dense because \(X\) is a
nonempty open set. Pairwise intersections of \(X,E_a,E_b\) yield only
\(X,E_a,E_b,\varnothing\), never \(Q\). This refutes printed Corollary 2.1 at
its literal intersection-closure strength. Replacing intersection closure by
union closure is sufficient: \(P\cup E_a\) and \(P\cup E_b\) then have
expressible denotations and the displayed intersection equals \(P\).
Complement-plus-intersection closure also yields those unions by De Morgan.
The manuscript correctly labels this repair as handbook-owned.

### Boolean closure and overlap

The table at `n-c-012.tex:2938-2956` is correct in its stated binary-operation
setting. Closed sets are closed under binary union and intersection (indeed,
finite unions and arbitrary intersections). A union containing a dense set is
dense. Dense sets are not intersection-closed when \(|S|>1\), since
\(E_a\cap E_b=\varnothing\). They are not complement-closed because \(X\) is
dense while its complement is empty and not dense. Safety is not
complement-closed in general: for \(S=\{a,b\}\), \(Q=\{a^\omega\}\) is closed,
because every execution outside it has a first non-\(a\) state furnishing a
disjoint cylinder; but \(X\setminus Q\) is not closed, because \(Q\) is not
open (no finite prefix of \(a^\omega\) isolates that execution). Finally, a
closed dense set equals its closure and that closure is \(X\), so only \(X\)
is both safety and liveness.

### Standing, terminology, and cross-record reconciliation

Apart from F-MP-01, the required introduced expressions satisfy the local
terminology rule. “Live for \(P\)” is defined as a finite-prefix/property
relation and distinguished from a property class at `n-c-012.tex:2685-2690`.
Uniform and absolute liveness have local definitions, property-class standing,
nonredundancy, and immediate use at `n-c-012.tex:2727-2800`. \(P_{A,B}\) is
explicitly eliminable at line 2793; \(L_P\) is an eliminable dependence-marking
renaming at lines 2842--2845; \(E_a,E_b\) are theorem-local alpha-renamings at
lines 2885--2889; and \(Q,\mathcal F\) have countermodel-only standing at lines
2924--2928. No new primitive is inferred from any of them.

The shared definition `logic-in-computer-science.tex:710-718`, detailed reader
`n-c-012.tex:2632-2975`, source note lines 1--634, and compact record
`p09-source-presentations-lot2-3.md:395-528` agree on the ordinary safety and
liveness quantifiers, full-sequence-space boundary, topology, theorem
strength, Corollary 2.1 countermodel and repair, and no-test/no-build boundary.
F-MP-01 is the one mathematical reconciliation defect: all three detailed
records repeat or compress the leads-to separation without exposing the
needed witness assumptions or the source's overbroad printed wording.

## Coverage map

- M01: checked-clean — all seven SHA-256 values recomputed and matched.
- M02: checked-clean — all five journal and eleven report PNG pages visually read.
- M03: not-checked — independent DOI/access-route validation is outside this mathematical mandate; visible title/date/page metadata and frozen-record consistency were observed only.
- M04: checked-clean — complete visual comparison found substantive agreement, including literal “intersection” in both second corollaries.
- M05: checked-clean — universe, empty word, concatenation, prefix, property/program standing, and terminal padding rederived, including \(S=\varnothing\) and \(|S|=1\).
- M06: checked-clean — exact safety quantifier order and \(n=0\) bad-prefix case rederived.
- M07: checked-clean — live-for relation, universal liveness closure, nonemptiness, and full-space boundary rederived.
- M08: checked-clean — motivation, maximality argument, examples, and stuttering qualification remain at their stated proof strength.
- M09: finding-linked — F-MP-01 affects the advertised absolute-versus-uniform separation; the definitions and inclusion chain themselves are checked-clean.
- M10: finding-linked — F-MP-01; the fixed-\(E_2\)-suffix inference is correct, but the non-absolute source example lacks its hypotheses and source-defect label.
- M11: checked-clean — predictive liveness and failure of uniform liveness rederived under all four nondegeneracy assumptions.
- M12: checked-clean — until and total-correctness decompositions do not assert a dichotomy.
- M13: checked-clean — both directions of safety/closed and liveness/dense proved from the cylinder basis.
- M14: checked-clean — Theorem 1 algebra, least-closed-superset contradiction, and scope boundaries rederived.
- M15: checked-clean — Corollary 1.1 uses the stated three expressibility closures and no language-specific strengthening.
- M16: checked-clean — Theorem 2 density, disjointness, factorization, alpha-renaming, and \(|S|>1\) materiality rederived.
- M17: checked-clean — printed Corollary 2.1 is false under the given denotation family; union closure and Boolean closure repairs verified.
- M18: checked-clean — every table entry, general closure fact, counterexample, and whole-space overlap claim rederived.
- M19: checked-clean — visual source reading confirms printed proofs for Theorems 1--2 and stated-only topology equivalences; handbook additions are identified.
- M20: checked-clean — every listed term/symbol (`live for P`, uniform, absolute, \(P_{A,B}\), \(L_P\), \(E_a,E_b\), \(Q\), and \(\mathcal F\)) has eliminable or relational standing, nonredundancy, and actual use.
- M21: finding-linked — F-MP-01 is repeated across the reader, source note, and compact presentation; all other mathematical claims reconcile.
- M22: not-checked — independent register and rights-status adjudication is outside this mathematical mandate; the frozen records' topic-only and no-test/no-build statements were read but not externally audited.

VERDICT: REJECT — F-MP-01
