# Round 1 mathematical and proof-correctness review

## Seat, snapshot, and evidence boundary

I reviewed only the mathematical-and-proof seat assigned by the charter.  The
evidence used was the charter, the six frozen objects, the thirty-six allowed
Rabin page renders, and the six allowed Meyer page renders.  I did not read the
ledger, the chair transcript, another review report or transcript, a
Trakhtenbrot board object, the staging Rabin draft, the layout extraction,
conversation summaries, or another reviewer's messages.  I did not contact
another reviewer.

No test, automated checker, repository script, TeX command, build, handbook-PDF
inspection, or rendered-handbook inspection was run.  Hash computation and
read-only inspection of the frozen objects and allowed source renders were the
only mechanical operations.

## Frozen-object identity

I independently recomputed SHA-256 for all six frozen objects before the
substantive review.  Every result equals the charter value:

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `2EF14C7487380F2E08B48BD7A8E79533A8EAC6F44A939A057265F34F4EE0EAC5` | exact match |
| `handbook/bib/handbook.bib` | `1EAADD6F25B9DFEE82265747ABEA78B782950217F397072EBA62D48004B79BE5` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `2DC08752861ACD364E020FA441AC37A0E597B532C2ED3FE85013C03F8D907AA2` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `4CFCA8E323720A9087604F7682664CDD41840FE3DCFB4EB9CD9F665696D945BB` | exact match |

## Source pages inspected

I visually inspected the complete Rabin render set at original detail:
`page-01.jpg` (the custody-and-use cover) and `page-02.jpg` through
`page-36.jpg` (printed pp. 1--35).  I also visually inspected the complete
Meyer article render set at original detail: physical PDF pp. 485--490,
corresponding to printed pp. 477--482.  Formulae, quantifier order, subscripts,
pair-sequence lengths, and source pagination were judged from those page
images, with the matching hash-pinned PDFs as the controlling objects.

The external McNaughton, Doner, Thatcher--Wright, and Thomas bodies are not in
the permitted frozen evidence set.  I therefore checked how Rabin uses or
attributes them and whether the manuscript preserves that external standing;
I did not independently re-review those external bodies.

## Independent mathematical reconstruction

### Ordinary and dual semantics

For an ordinary table run (r:T_x\to S), Definition 1.5 first existentially
chooses one global run and then universally tests every branch.  Its condition
is
\[
  \exists r\,[r(x)\in S_0\land
  \forall\pi\;\operatorname{In}(r|\pi)\in F],
  \qquad F\subseteq\mathcal P(S).
\]
The manuscript gives that typing and prefix at lines 974--1013, matching
printed pp. 5--6.

Definition 3.5 instead gives a finite pair sequence
\(\Omega=((L_i,U_i))_{1\le i\le k}\).  A branch is of type \(\Omega\) when
one pair has an infinitely recurring upper state and no infinitely recurring
lower state.  Definition 3.6 reverses the game:
\[
  \forall r\,[r(x)=s\Longrightarrow
  \exists\pi\;r|\pi\in[\Omega]].
\]
Thus a missing run makes the implication true.  Lines 1142--1187 correctly
state both the reversal and this vacuity, matching printed pp. 24--25.  That
vacuity is also what exposes finding MP-R1-01 below.

### Formula and run translations

The bit-track map at lines 1026--1045 is a typed bijection: each tuple of node
sets has exactly one full-root \(\{0,1\}^n\)-valuation, and each such valuation
recovers exactly one tuple.  The principal-formula reduction, Boolean
operations, projection, and complementation at lines 1047--1064 reproduce the
separate logical constructors on printed pp. 7--9 and the finite-witness lift
on printed pp. 30--31.  The handbook-owned example at lines 1066--1076 is a
valid instance: choose a finite full-frontiered tree in which both the witness
node and its left child are nonfrontier, hence labelled.

Conversely, after coding \(S\) by \(m\) bits, the state tracks determine a
mapping \(T\to S\).  The root clause and transition clauses inductively keep
every node in \(S\), while the universally quantified path track tests the
Muller family.  The resulting set prefix is exactly
\(\exists B_1\cdots\exists B_m\,\forall C\), as stated at lines 1078--1090
and printed on p. 10.

For a sentence, writing it as \(\exists A_1 F(A_1)\) makes truth equivalent to
the existence of one full-root track accepted by the automaton for \(F\).
That is precisely automaton nonemptiness.  Lines 1092--1097 correctly invoke
Theorem 1.6 and insert no basis theorem, matching printed p. 9.

### Theorem 3.1 product and index

Let a branch's tree-table states be \(s_0,s_1,\ldots\), and let the unique
deterministic word run be
\[
  q_0=u_0,\qquad q_{n+1}=K(q_n,s_n).
\]
The product transition at lines 1120--1126 labels the branch by
\((q_n,s_n)\) at depth \(n\).  It therefore has no substantive index error:
the root carries \(q_0\), and both children carry the common next state
\(K(q_0,s_0)\) before their tree-state sequences diverge.  Moreover, because
the second coordinate is finite,
\[
  p_1(\operatorname{In}((q_n,s_n)_{n<\omega}))
  =\operatorname{In}((q_n)_{n<\omega}).
\]
Hence the designated family at lines 1130--1133 accepts exactly when the word
automaton does.  This matches printed p. 18.  Even a convention that dropped
or added only the initial word state would leave the infinite-occurrence set
unchanged, but the displayed construction already matches Rabin's run index.

### Well-founded strata and the two half-steps

For a mapping \(h\mapsto H_h\), the absence of an infinite descent is
equivalent to an ordinal rank \(\rho\) with
\(h'\in H_h\Rightarrow\rho(h')<\rho(h)\).  Lemma 3.3 obtains the rank by
transfinite stage formation; the converse construction in Lemma 3.11 again
uses transfinite stages.  The manuscript places these uses correctly at lines
1201--1207 and 1259--1266 and does not replace simultaneous runs, marked
obligations, or finite-state merging by the ordinal argument.

For complementation, the first half-step assumes the last lower set empty and
reduces local obligations to a sequence of length \(k-1\); the second handles
arbitrary length \(k\) by Lemma 3.8's same-length sequence with empty last
lower set and Lemma 3.11's well-founded deferral.  Lines 1209--1227 preserve
those lengths.  For emptiness, the arbitrary same-length stage computation is
finite because its disjoint strata add states at most \(|R|\) times, and the
last-empty step then reduces the pair-sequence length.  The manuscript gives
that plan at lines 1298--1325.  Its exclusion of the empty choice in the
last-empty step is, however, false; see MP-R1-01.

### Restricted tables and the finite base

Definition 3.7 retains the formal state set \(R\) and changes only the
transition values to
\(N(s)\cap(R'\times R')\).  Thus the named root state may be outside \(R'\),
while all strict descendants lie in \(R'\).  Lines 1303--1311 state this
boundary exactly, matching printed p. 33.

The finite base is obtained from Lemma 3.14's finite hitting witness and the
weak monadic finite-tree decision theorem.  The finite family may be empty in
the no-run case.  Lines 1327--1336 instead require it to be nonempty; that
requirement is the second part of MP-R1-01.

### Meyer consequence

Rabin's printed pp. 1, 4, and 7 claim elementary-recursive procedures.  Meyer
printed p. 478 states a tower lower bound whose height grows with input length,
and printed p. 479 item 5 includes “the theory of two successors and prefix,”
credited there to Meyer and Stockmeyer.  The language using only the two
successors and prefix is a literal sublanguage of the displayed binary
successor structure, which additionally has lexicographic order and monadic
quantification.  Restricting any decision procedure for the displayed theory
to those sentences would decide the listed sublanguage.  The non-elementary
lower bound therefore rules out Rabin's elementary worst-case claim while
leaving decidability and effectiveness untouched.  Lines 941--963 and
1339--1345 report exactly that consequence.

## Finding

### MP-R1-01 — must-fix — the emptiness recursion wrongly excludes the empty obligation set

- **Frozen manuscript location:**
  `handbook/parts/p09/presentations/n-c-014.tex` lines 1181--1183,
  1321--1325, and 1327--1336.
- **Controlling printed source:** Rabin printed p. 25, Definition 3.6; p. 27,
  Lemma 3.9; p. 31, Lemma 3.14; and p. 34, displays (3.5)--(3.6) and the
  final base-case paragraph.
- **Affected mandates:** R04, R16, R18, R19, R23, and R27.

**Defect.**  Lines 1181--1183 correctly say that dual acceptance is vacuous
when no run begins in the named state.  Lines 1321--1325 then say that the
last-empty-lower-set reduction ranges only over a *nonempty*
\(H\subseteq U_k\), and lines 1327--1336 similarly require the base witness
\(U_0\subseteq U_1\) to be nonempty.  Neither nonemptiness condition follows.
The relevant set in Lemma 3.9 may be empty when there is no run, or when every
run already has an \(\Omega_{k-1}\)-type path.  Lemma 3.14 extracts a finite
subset, not a nonempty one.  Rabin's p. 34 itself prints “nonempty” in both
places; the handbook has repeated a source proof gap as though it were an
exact exhaustive reduction.

The failure is not merely the degenerate absence of a run.  Consider the
one-letter table with
\[
 R=\{s,a,u,b\},\quad
 N(s)=\{(a,a)\},\quad N(a)=\{(a,a)\},\quad
 N(u)=\{(b,b)\},\quad N(b)=\{(b,b)\},
\]
and
\[
 \Omega=((\varnothing,\{a\}),(\varnothing,\{u\})).
\]
The unique run from \(s\) has every branch eventually constantly \(a\), so it
already has type \(\Omega_1\), and
\(T\in D(\langle R,N\rangle,\Omega,s)\).  The only nonempty
\(H\subseteq U_2\) is \(\{u\}\).  From \(u\), however, the unique run is
eventually constantly \(b\): it has no \(\Omega_1\)-type path and no strict
descendant in state \(u\).  Thus p. 34's clause (3.5) fails for the required
state \(u\), and no nonempty \(H\) witnesses the asserted equivalence.  The
empty choice \(H=\varnothing\) is exactly the missing branch.

The base case fails for the stated reason as well.  Let
\[
 R=\{s,u,a\},\qquad N(s)=\varnothing,
 \qquad N(u)=\{(a,a)\},\qquad N(a)=\{(a,a)\},
 \qquad \Omega=((\varnothing,\{u\})).
\]
There is no run from \(s\), so Definition 3.6 accepts vacuously.  The only
nonempty candidate is \(U_0=\{u\}\), but every finite run beginning in \(u\)
labels every strict descendant by \(a\), and therefore never reaches \(U_0\)
below the root.  No family with nonempty \(U_0\) satisfies lines 1329--1331.
Allowing \(U_0=\varnothing\) and \(m=0\) leaves only a finite tree \(E_0\)
on which no run from \(s\) exists; König compactness supplies such a finite
obstruction exactly when no infinite run exists.

**Minimum sufficient repair.**  Preserve Rabin's printed nonempty branch but
add the missing empty branch explicitly and label the addition as a
handbook-owned repair:

1. in the last-empty half-step, range over all \(H\subseteq U_k\), or first
   handle \(H=\varnothing\), which is the direct
   \(\Omega_{k-1}\)-question for the root state, and then enumerate the
   nonempty choices using the stated restriction to \(R\setminus H\);
2. in the \(k=1\) base, allow the finite set
   \(U_0=\{s_1,\ldots,s_m\}\) to be empty (\(m=0\)), or add a separate
   finite no-run-obstruction branch before the nonempty-family branch; and
3. update the source note and compact record only if their prose is made to
   assert the erroneous nonemptiness, while preserving the fact that p. 34 is
   the source of the gap.

This is a local repair, but it is mandatory: without it the claimed recursive
decision equivalence is false on permitted nontotal tables and does not prove
Theorem 1.6 in the cases above.

## Mandatory-invariant disposition

| Mandate | Disposition |
|---|---|
| R01 | Satisfied: \(\Lambda\) is retained and the editorial non-substitution is explicit at lines 914--917. |
| R02 | Satisfied: Definition 1.1 has \(0<n\le\omega\), both orders, successors, and the finite/\(\omega\) definability boundary at lines 914--963. |
| R03 | Satisfied: arbitrary roots, distinct table/automaton tuples, nontotal moves, \(\exists r\forall\pi\), and \(F\subseteq\mathcal P(S)\) are explicit at lines 965--1014. |
| R04 | Definition satisfied at lines 1142--1187, but its vacuity is contradicted by the later nonempty-only recursion in MP-R1-01. |
| R05 | Satisfied at lines 1016--1022. |
| R06 | Satisfied at lines 1026--1064 and 1230--1257. |
| R07 | Satisfied at lines 1066--1076; the example is expressly handbook-owned. |
| R08 | Satisfied at lines 1078--1097. |
| R09 | Satisfied at lines 1099--1138; the product index and designated family are correct. |
| R10 | Satisfied at lines 1142--1187. |
| R11 | Satisfied at lines 1192--1199. |
| R12 | Satisfied at lines 1201--1207 and 1259--1266. |
| R13 | Satisfied for the complementation construction at lines 1209--1227; the emptiness specialization needs MP-R1-01. |
| R14 | Satisfied at lines 1230--1247. |
| R15 | Satisfied at lines 1248--1257 and 1342--1345. |
| R16 | Not fully satisfied: the overall source route is present, but its final recursive equivalence omits the empty branch (MP-R1-01). |
| R17 | Satisfied at lines 1298--1311. |
| R18 | Not satisfied as an exhaustive half-step; retain the nonempty choices but add the missing \(H=\varnothing\) branch (MP-R1-01). |
| R19 | Not satisfied: the finite base must permit \(m=0\) or separately decide the no-run case (MP-R1-01). |
| R20 | Satisfied at lines 941--963 and 1339--1345, controlled by Meyer printed pp. 478--479. |
| R21 | Satisfied at exact class level by lines 1349--1366. |
| R22 | Satisfied at lines 1113--1138 and 1368--1382. |
| R23 | Not fully satisfied because p. 34's erroneous “nonempty” is reproduced without a source-defect qualification (MP-R1-01); other checked numbering, locators, notation, strength, and attributions agree. |
| R26 | Satisfied for the technical distinctions material to this seat; no unneeded hypothetical construction name is introduced in the Rabin reconstruction. |
| R27 | Not fully satisfied: ordinary/dual semantics are distinguished, but the nonempty-only recursion loses dual vacuity (MP-R1-01). |
| R28 | Satisfied: this report and any possible later acceptance are limited to frozen `N-c-014.d` manuscript content. |

No other blocker or must-fix finding was found within this seat's permitted
evidence.  MP-R1-01 prevents acceptance of the frozen Round 1 snapshot.

VERDICT: REJECT — MP-R1-01

