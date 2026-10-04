# Round-two mathematical and proof-correctness review

- Seat: mathematical and proof-correctness
- Round: 2, fresh blind review
- Frozen object: the charter's round-two repaired seven-object snapshot only
- Evidence used: direct SHA-256 identity checks; original-detail visual reading of
  every journal and report page image; full direct reading of every frozen text
  scope; independent set-theoretic and topological derivation
- Evidence not used: ledger, chair transcript, any round-one or other round-two
  transcript, any earlier Part IX board record, source extraction in place of page
  images, tests, automated checkers, repository scripts, TeX commands, builds, or
  handbook-PDF inspection

## Snapshot identity gate

All seven hashes were recomputed before substantive review and agree exactly with
the charter.

| Frozen artifact | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf` | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` | match |
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf` | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` | match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `4E58F17BC534504C5D43DE2EADBD365CE01B8D029CE8A67B2BBAFBF2DAD75736` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | match |
| `handbook/bib/handbook.bib` | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` | match |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | `786B63163F0EF1456561B974D1D4A38578A06AF619C4DAB0ADE05FFCC0D7EE13` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `915ECD5D1451D24E336A60616AF5F93EBE300774A1D29FABABD0531035F4838E` | match |

I then visually read `journal-page-1.png` through `journal-page-5.png` and
`tr-page-01.png` through `tr-page-11.png`, each at original detail. The journal
pages visibly run from printed pp. 181--185. The report has an outer cover, an
inner title/abstract leaf, and internally numbered body pp. 1--9. The formulas
and the word *intersection* in the second corollary were resolved from the page
images, not from extraction.

## Finding

### R2-MP-01 — The reader erases the source's printed qualification on the liveness half of the leads-to example

- Author/seat: mathematical and proof-correctness
- Round: 2
- Severity: must-fix
- Status: open
- Locations: journal p. 183, right column; TR body p. 5; `handbook/parts/p09/presentations/n-c-012.tex:2772-2775`; `spec/research/p09-alpern-schneider-1985-source-note.md:278-286`; `spec/research/p09-source-presentations-lot2-3.md:467-470`
- Claim: all three handbook records say, in substance, that the source claims
  without qualification that a leads-to property is live and not absolutely
  live. That is not the printed division of claims. The article and report
  explicitly condition the liveness assertion on satisfiability of (E_2).
  The unqualified assertion is the assertion that a leads-to property is not
  absolutely live, and its printed witness silently presupposes an (E_1)
  occurrence and an execution containing neither event type.
- Evidence: journal p. 183 and TR body p. 5 visibly say “When (E_2) is
  satisfiable” immediately before classifying the property as liveness. The
  subsequent non-absolute assertion and witness do not print the additional
  existence hypotheses. In the handbook's full-sequence state-set rendering,
  satisfiability of (E_2) is exactly (E_2\ne\varnothing).
- Mathematical harm: the repaired theorem is correct, but the present prose
  misreports which premise is source-owned and makes the handbook-owned
  strengthening to *uniform* liveness look less distinct than it is. This
  violates the source-versus-handbook boundary in I6 and the exact-strength
  requirement in I10.
- Smallest correction: at all three locations, say that the source (i) proves
  or asserts liveness when (E_2) is satisfiable and (ii) claims without the
  further needed qualifications that every leads-to property is not absolutely
  live. Then identify the state-set hypotheses, constant-(E_2) uniform witness,
  exact necessity argument, and two-state counterexample as handbook-owned.

No other blocker or must-fix was found.

## Independent mathematical derivations

### 1. Semantic universe, types, and degenerate state space

Let (X=S^\omega). With (S\ne\varnothing), (S^*=\bigcup_{n<\omega}S^n)
contains the unique empty sequence (\epsilon\), and (X\ne\varnothing) because
any (s\in S) gives (s^\omega\). If (u\in S^*) and (y\in X), then
(u\mathbin{\smallfrown}y\in X). If (x\in X) and (n\in\omega), then
(x{\upharpoonright}n\in S^n\subseteq S^*). Hence every displayed
concatenation and membership judgment in the reader and compact record is
typed.

The prefix clause

\[
u\preceq x\quad\Longleftrightarrow\quad
\exists y\in X\;x=u\mathbin{\smallfrown}y
\]

has the expected finite--infinite standing. A property is a subset of (X),
the source's satisfaction sign is membership, and a program satisfies a
property exactly by inclusion of its behavior set. Repeating a final state
turns a finite terminating run into an element of (X); the reconstruction
states this convention before using source examples that depend on it.

The nonempty-state repair is necessary. If (S=\varnothing), then
(X=\varnothing), while (S^*=\{\epsilon\}). The only property
(P=\varnothing) satisfies the safety formula vacuously. It is also dense in
the empty topological space, but it fails liveness because no
(y\in S^\omega) extends (\epsilon). Thus liveness iff density fails, and
Theorem 1 cannot factor (\varnothing) through a liveness property because no
liveness property exists. Lines 2635 and 2665--2670 state the needed repair.

### 2. Safety, liveness, the empty prefix, and the compact clause

The safety clause at `n-c-012.tex:2673-2683` and compact lines 430--435 is

\[
\forall x\in X\;
\bigl(x\notin P\Rightarrow
\exists n\in\omega\;\forall y\in X\;
(x{\upharpoonright}n)\mathbin{\smallfrown}y\notin P\bigr).
\]

Its quantifier order is exact: (n) may depend on the violating (x), but the
chosen finite prefix must reject every infinite continuation (y). In the
compact clause, (x\in S^\omega), (x{\upharpoonright}n\in S^*),
(y\in S^\omega), their concatenation is in (S^\omega), and
(P\subseteq S^\omega); there is no finite/infinite type mismatch. The shared
definition at `logic-in-computer-science.tex:710-718` is the same semantic
statement in word language.

For (u\in S^*), “(u) is live for (P)” is exactly the relation

\[
\exists y\in X\;u\mathbin{\smallfrown}y\in P.
\]

It is not a property class. Liveness universally closes this relation over
all (u\in S^*). Because (\epsilon\in S^*), liveness implies
(P\ne\varnothing). The suffix may depend on (u), so the definition neither
reduces liveness to one atomic eventuality nor to one fixed transition
system's path space.

Failure of liveness yields (u\in S^*) with no satisfying continuation. That
is an irremediable finite bad prefix. This proves the formal part of the
source's maximality argument. It does not prove that the informal words “good”
and “bad” uniquely determine this definition, and the manuscript correctly
keeps that further claim methodological.

The source examples are reported at the right strength. Mutual exclusion,
deadlock freedom, partial correctness, and first-come-first-serve are presented
as finite-bad-witness examples; starvation freedom, termination, and guaranteed
service are presented as future-extension examples. The changing-at-every-step
property is safety here because the first repeated adjacent state is a finite
bad prefix. It is not invariant under inserted finite stutters, so the reported
comparison with Lamport remains expressly conditional and attributed.

### 3. Uniform and absolute liveness

Uniform liveness has quantifiers

\[
\exists y\in X\;\forall u\in S^*\;
u\mathbin{\smallfrown}y\in P.
\]

Absolute liveness is the conjunction of (P\ne\varnothing) with

\[
\forall y\in X\;
\bigl(y\in P\Rightarrow
\forall u\in S^*\;u\mathbin{\smallfrown}y\in P\bigr).
\]

The nonemptiness conjunct is indispensable: without it, the universal clause
would accept (P=\varnothing). If (P) is absolute, choose any (y\in P);
that (y) is a uniform witness. A uniform witness can be reused after each
prefix, proving ordinary liveness. Therefore

\[
\text{absolute}\Rightarrow\text{uniform}\Rightarrow\text{ordinary liveness}.
\]

The definitions state semantic classes of properties, their quantifier
differences establish nonredundancy, and the following two examples use the
distinctions. The manuscript does not treat them as formula constructors.

### 4. Leads-to: exact repaired classification and witnesses

For this derivation only, let the eliminable abbreviation

\[
\operatorname{LT}(E_1,E_2)=
\{x\in X:\forall i\in\omega\,
(x_i\in E_1\Rightarrow
\exists j\in\omega\,(i<j\land x_j\in E_2))\}
\]

denote the displayed state-set interpretation of “every (E_1)-occurrence is
followed later by an (E_2)-occurrence.” It is a property, not a new primitive.

For nonempty (S), the repaired separation is exact:

\[
\operatorname{LT}(E_1,E_2)
\text{ is uniformly live but not absolutely live}
\]

if and only if

\[
E_1\ne\varnothing,
\qquad E_2\ne\varnothing,
\qquad S\setminus(E_1\cup E_2)\ne\varnothing.
\]

**Sufficiency and the overlap case.** Choose (e_2\in E_2). For every finite
(u), the suffix (e_2^\omega) answers every (E_1)-occurrence in (u).
If (e_2\in E_1\cap E_2), strict “later” is still satisfied: the occurrence
at suffix position (k) is answered by the occurrence at suffix position
(k+1). Hence the same constant suffix is a valid uniform witness even under
overlap. Choose (e_1\in E_1) and
(c\in S\setminus(E_1\cup E_2)). The execution (c^\omega) contains no
(E_1)-occurrence and is satisfying, while
(e_1\mathbin{\smallfrown}c^\omega) leaves its first request unanswered.
Thus absolute liveness fails.

**Necessity.** If (E_1=\varnothing), the property is all of (X), hence
absolute. If (E_2=\varnothing) and (E_1\ne\varnothing), a one-state prefix
from (E_1) has no satisfying continuation, so the property is not even live;
if both are empty, it is again all of (X) and absolute. Finally suppose
(E_1,E_2\ne\varnothing) but
(S\setminus(E_1\cup E_2)=\varnothing). Any satisfying execution must contain
an (E_2)-state: an execution with none would consist only of (E_1)-states
and violate its first obligation. For any satisfying (y) and finite (u),
obligations internal to (y) remain answered, and every still-unanswered
(E_1)-occurrence in (u) is answered by an (E_2)-occurrence in (y).
Therefore every satisfying (y) survives every finite prefix, so the property
is absolute. All three displayed hypotheses are consequently necessary as well
as sufficient for the advertised separation, and each is necessary for the
specific three chosen witnesses (e_1,e_2,c).

**Two-state counterexample.** For
(S=\{e_1,e_2\}), (E_1=\{e_1\}), and (E_2=\{e_2\}), the property is
nonempty because (e_2^\omega) satisfies it. If (y) satisfies it, then (y)
contains (e_2); otherwise (y=e_1^\omega), which violates the first request.
For arbitrary finite (u), every obligation in (y) remains answered by a
later position of (y), and every unanswered obligation in (u) is answered
by an (e_2) in (y). Thus (u\mathbin{\smallfrown}y) satisfies the property.
This proves absolute liveness, not merely liveness. The reader's two-state
example is mathematically valid.

The printed/source ownership is the one defect recorded as R2-MP-01. The
source prints the (E_2)-satisfiability qualification for liveness, then gives
an underqualified non-absolute claim. The exact three-condition equivalence,
the constant-suffix strengthening to uniform liveness, the overlap argument,
and the two-state refutation are handbook-owned.

### 5. Predictive property: standing and exact nondegeneracy

At `n-c-012.tex:2794-2815`, (A,B\subseteq S) are state conditions and
(P_{A,B}\subseteq X) is an eliminable name for the displayed property. Its
two branches require eventual permanence in (B) after an (A)-initial state,
and eventual permanence outside (B) after a non-(A)-initial state.

The four hypotheses

\[
A\ne\varnothing,\quad S\setminus A\ne\varnothing,\quad
B\ne\varnothing,\quad S\setminus B\ne\varnothing
\]

are sufficient. For a nonempty prefix, inspect its first state and append a
constant (B)-state or constant non-(B)-state as appropriate. For the empty
prefix, choose either compatible initial branch and its constant tail. Thus
(P_{A,B}) is live. No suffix (y) is uniform: if (y) is eventually always
in (B), prepend a state outside (A), after which the required eventual
always-outside-(B) branch fails; if (y) is not eventually always in (B),
prepend a state in (A), after which the required (B)-branch fails.

The hypotheses are also exact for the advertised separation. If (A) is
empty and the property is live, some state lies outside (B), and its constant
suffix works uniformly. If (A=S) and the property is live, some state lies in
(B), and its constant suffix works uniformly. Hence both initial branches
must be nonempty for live-but-not-uniform behavior. Liveness after a one-state
(A)-prefix forces (B\ne\varnothing); liveness after a one-state non-(A)
prefix forces (S\setminus B\ne\varnothing). The standing,
nondegeneracy, liveness proof, and failure-of-uniform proof are all correct.

### 6. Until, total correctness, and absence of a dichotomy

The strong-until property is the intersection of (i) the safety condition that
no non-(E_1) event occurs before the first (E_2) and (ii) the eventual-(E_2)
condition. Under the already stated (E_2\ne\varnothing) standing, the latter
is live because any finite prefix can be extended by an (E_2)-state. A
violation of the first factor is witnessed at the first forbidden pre-(E_2)
position, so it is safety. Depending on degeneracies, the intersection can
collapse to one class; the reader says “generally neither,” not “always
neither,” and therefore does not overclaim. Total correctness is likewise the
source's intersection of partial correctness and termination. These examples
show that a property need not itself be exactly one of safety or liveness.

### 7. Prefix topology: both equivalences

For (u\in S^*), the cylinder
([u]=\{x\in X:u\preceq x\}) is nonempty because (S\ne\varnothing), and the
cylinders form the declared basis.

If (P) is safety and (x\notin P), its bad prefix (x{\upharpoonright}n)
gives a basic neighborhood of (x) contained in (X\setminus P). Hence the
complement is open and (P) is closed. Conversely, if (P) is closed, each
(x\notin P) lies in some basic cylinder contained in the open complement;
the cylinder's defining prefix is an irremediable finite bad prefix. Thus
safety iff closed.

A set is dense iff it meets every nonempty basic cylinder. The equation
([u]\cap P\ne\varnothing) says exactly that some (y\in X) has
(u\mathbin{\smallfrown}y\in P). Quantifying over (u\in S^*) gives exactly
liveness. Thus liveness iff dense. The article states these equivalences; the
direction proofs are correctly identified as handbook-supplied.

### 8. Theorem 1 and its boundaries

Let (C=\overline P) and

\[
L_P=X\setminus(C\setminus P)=P\cup(X\setminus C).
\]

Then (C) is the least closed, hence least safety, superset of (P), and

\[
C\cap L_P=C\cap(P\cup(X\setminus C))=P.
\]

To prove density, suppose (L_P) is not dense. Some nonempty open (O) is
disjoint from (L_P), so (O\subseteq C\setminus P). Therefore
(P\subseteq C\setminus O). Since (C) and (X\setminus O) are closed,
(C\setminus O) is closed. Since (O\ne\varnothing) and (O\subseteq C), it
is strictly smaller than (C). This contradicts the minimality of (C).
Thus (L_P) is dense/live and (P=C\cap L_P).

The theorem proves existence. Only the chosen closure factor is least among
safety supersets. Nothing proves uniqueness of all factorizations,
expressibility in a chosen syntax, or cheap computation. The source prints
this theorem proof; the handbook's (L_P) is a defined alpha-renaming of the
source's (L).

### 9. Corollary 1.1

If the denotation family of a notation is closed under topological closure,
complement, and intersection, then (\overline P) is expressible and so is

\[
L_P=X\setminus(\overline P\cap(X\setminus P)).
\]

The intersection of the two factors is (P). These are exactly the operations
used by the construction. The corollary is conditional and makes no assertion
that a particular temporal syntax has the required closure. The stated source
and handbook versions are correct.

### 10. Theorem 2 and the singleton edge case

For distinct (a,b\in S), let (E_a) and (E_b) be the properties of being
eventually constantly (a) and eventually constantly (b), respectively.
Appending (a^\omega) or (b^\omega) after any finite prefix proves that both
are live. They are disjoint: if one execution were eventually all (a) and
eventually all (b), then after the maximum of the two cutoffs its state would
equal both distinct states. For arbitrary (P\subseteq X), unions with these
dense sets are live, and distributivity gives

\[
(P\cup E_a)\cap(P\cup E_b)=P\cup(E_a\cap E_b)=P.
\]

The alpha-renaming from the source's (L_a,L_b) to (E_a,E_b) is exact and
avoids collision with (L_P). If |S|=1, then (X) is a singleton and its only
dense subset is (X); (\varnothing) cannot be an intersection of two live
properties. Thus |S|>1 is material, and (E_a\cap E_b=\varnothing) also
supplies the promised failure of intersection closure for liveness.

### 11. Corollary 2.1: printed insufficiency, countermodel, and repair

The printed construction needs (P\cup E_a) and (P\cup E_b). Closure of a
denotation family under intersection does not imply that either union is
denotable. This already shows that the printed hypothesis does not support the
displayed proof.

The reader correctly proves the stronger statement that the hypothesis is
insufficient for the conclusion. Let

\[
Q=\{a^\omega\},\qquad
\mathcal F=\{X,E_a,E_b,Q,\varnothing\}.
\]

The symbols are explicitly presented as eliminable names for one property and
one possible denotation family. The full intersection table stays in
(\mathcal F): (X) and (\varnothing) behave as top and bottom;
(E_a\cap E_b=\varnothing); (Q\subseteq E_a); and
(Q\cap E_b=\varnothing). Thus a notation with precisely these denotations and
conjunction interpreted by set intersection satisfies the printed closure
hypothesis and contains disjoint expressible live properties (E_a,E_b).

Its live members are exactly (X,E_a,E_b). The singleton (Q) is not dense
because the nonempty cylinder ([b]) misses it, and (\varnothing) is not
dense because (X\ne\varnothing). Pairwise intersections of the three live
members are (X,E_a,E_b), or (\varnothing), never (Q). Hence the
expressible (Q) has no factorization of the printed kind. This is a valid
countermodel, so “insufficient hypothesis” is the right diagnosis.

Union closure is the one-operator repair used by the proof: it makes both
(P\cup E_a) and (P\cup E_b) expressible. Complement plus intersection also
suffices by De Morgan. Both source versions print *intersection*; the
countermodel and repairs are correctly identified as handbook-owned.

### 12. Boolean closure and overlap

Closed sets are closed under binary union and intersection (more generally,
finite union and arbitrary intersection). A union containing a dense set is
dense, so liveness is closed under binary union. The disjoint live sets
(E_a,E_b) show failure of intersection closure when |S|>1. Complements do
not preserve either class in general. If a property is both closed and dense,
its closure is both itself and (X), so it equals (X). Every Boolean-table
entry at `n-c-012.tex:2953-2971` is therefore correct and explicitly semantic,
not a claim about syntax.

## Terminology and source/proof ownership audit

- “live for (P)” is necessary to distinguish one prefix/property relation
  from the universally quantified property class; it is defined, typed, and
  used immediately.
- Uniform and absolute liveness are source-named semantic subclasses. Their
  exact definitions, standing, nonredundancy, inclusion, and later separating
  uses are local.
- (P_{A,B}) is expressly an eliminable name for a displayed property, with
  (A,B\subseteq S) and exact nondegeneracy assumptions.
- (L_P) is expressly an eliminable alpha-renaming of the source's constructed
  property (L), with its dependence on (P) exposed.
- (E_a,E_b) are expressly eliminable alpha-renamings of the source's
  (L_a,L_b), typed as properties and used in Theorem 2 and the countermodel.
- (Q) and (\mathcal F) are expressly eliminable countermodel abbreviations;
  their standing and use are given where introduced.
- The article prints the two theorem proofs. It states, but does not prove, the
  two topology equivalences. It states the absolute--uniform--ordinary chain
  without a numbered proof. The handbook correctly owns the expanded topology
  directions, quantifier proof, Corollary 2.1 countermodel and repair, and
  repaired leads-to mathematics. R2-MP-01 is the sole ownership wording defect.

The reader, shared definition, source note, compact record, and bibliography
otherwise agree on the sequence universe, property standing, theorem strength,
source version boundary, printed Corollary 2.1 word, journal/report identities,
and no-build/no-admission boundary.

## Mandatory coverage map

| Point | Status | Evidence/result |
|---|---|---|
| M01 | checked-clean | All seven SHA-256 values recomputed before substantive review; exact matches recorded above. |
| M02 | checked-clean | All five journal PNGs and all eleven TR PNGs visually read at original detail. |
| M03 | checked-clean within frozen scope | Title, authors, journal, volume/issue/date/pages, receipt/revision dates, TR number/dates, access routes, DOI record, and printed copyright/absence-of-open-licence treatment are internally consistent. No live URL/DOI resolution was attempted because the brief restricts this seat to the frozen snapshot. |
| M04 | checked-clean | Page maps match the images; substantive mathematics agrees; both versions visibly print *intersection* in the second corollary; numbering differs as reported. |
| M05 | checked-clean | Types, empty sequence, concatenation, prefix, property/program standing, membership, satisfaction, and terminal padding rederived; (S=\varnothing) failure shown. |
| M06 | checked-clean | Exact safety quantifier order and finite irremediable-prefix reading verified; compact clause is typed. |
| M07 | checked-clean | “Live for” relation, universal liveness, nonemptiness from the empty prefix, and full-space boundary verified. |
| M08 | checked-clean | Proof-method motivation, formal versus methodological maximality, examples, and stuttering qualification checked without strength promotion. |
| M09 | checked-clean | Uniform/absolute definitions, nonvacuity, semantic standing, nonredundancy, use, and both implications proved. |
| M10 | finding-linked: R2-MP-01 | Repaired leads-to mathematics is correct and exact; the source's printed (E_2)-satisfiability qualification is misreported at three handbook locations. |
| M11 | checked-clean | Predictive property typed; all four nondegeneracy conditions proved necessary and sufficient for live-but-not-uniform separation. |
| M12 | checked-clean | Until and total-correctness decompositions and the rejection of a dichotomy verified at the stated, qualified strength. |
| M13 | checked-clean | Cylinder basis and both directions of safety/closed and liveness/dense proved. |
| M14 | checked-clean | Theorem 1 algebra, least-closed-superset density contradiction, and nonuniqueness/syntax/algorithm boundaries verified. |
| M15 | checked-clean | Corollary 1.1 uses exactly complement, intersection, and topological closure; conditional strength preserved. |
| M16 | checked-clean | Theorem 2 alpha-renamings, liveness, disjointness, factorization, and cardinality-one obstruction verified. |
| M17 | checked-clean | Printed hypothesis checked in both sources; denotation-family countermodel and union/Boolean repairs independently proved. |
| M18 | checked-clean | Every Boolean-closure entry and the unique closed-dense property claim verified. |
| M19 | finding-linked: R2-MP-01 | Proof ownership is otherwise exact; leads-to source-strength sentence must preserve the printed qualification. |
| M20 | checked-clean | Every listed term/symbol has necessity or source standing, exact eliminable definition, standing, nonredundancy, and actual use. |
| M21 | finding-linked: R2-MP-01 | Five textual scopes otherwise reconcile claim by claim; the same inaccurate leads-to attribution recurs in reader, source note, and compact record. |
| M22 | checked-clean | Unlettered standing, rights boundary, topic-only review status, and explicit no-test/no-build boundary are preserved. |

VERDICT: REJECT — R2-MP-01
