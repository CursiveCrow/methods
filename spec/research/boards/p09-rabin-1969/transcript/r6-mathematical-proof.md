# Rabin 1969 Round 6 — mathematical and proof-correctness review

## Outcome

I accept the frozen Round 6 snapshot for the mathematical-and-proof-correctness
seat. I found no blocker, must-fix, or advisory mathematical finding. No finding
identifier is issued, and no repair is required.

This is an independent whole-snapshot review. It is not an inference from an
earlier verdict and is not limited to the most recent compact-record repair.

## Evidence boundary and independence

I used only the following evidence authorized by the controlling charter:

1. `spec/research/boards/p09-rabin-1969/charter.md`, read completely;
2. the six objects in the charter's Frozen Round 6 snapshot, each read
   completely;
3. `tmp/pdfs/p09-rabin-1969/rendered/page-01.jpg` through `page-36.jpg`, viewed
   at original detail; and
4. `tmp/pdfs/p09-rabin-1969/meyer1975-rendered/page-485.png` through
   `page-490.png`, viewed at original detail.

The two hash-pinned PDFs, rather than the renders, controlled source identity
and printed content. The renders were reading aids. I did not read an earlier
round report, unfiled Round 4 work, another Round 6 report, the decision ledger,
the chair transcript, another board, a staging draft, a layout extraction, or
another reviewer's messages. I did not contact another reviewer. I used no
test, automated checker, repository script, TeX command, interim build,
handbook-PDF inspection, or build.

## Frozen identities

Before substantive review, I independently recomputed every identity with the
native PowerShell `Get-FileHash -Algorithm SHA256` command. Every observed
digest equals the charter's Round 6 digest exactly.

| Frozen object | Charter SHA-256 | Independently observed SHA-256 | Result |
|---|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `29DAF36E123A2900620D49F018BD5F76BC4EE2FE0AAA7E3F85AAB50B23F37D7B` | `29DAF36E123A2900620D49F018BD5F76BC4EE2FE0AAA7E3F85AAB50B23F37D7B` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `BB5D7220F75298C6DF3A1934D0DE36F25B9BD64AC5B2B71A141C2A41D3536236` | `BB5D7220F75298C6DF3A1934D0DE36F25B9BD64AC5B2B71A141C2A41D3536236` | exact match |

## Printed-page inspection

I visually inspected all thirty-six Rabin physical pages: physical page 1 is
the custody cover, and physical pages 2--36 are printed article pages 1--35.
I also visually inspected all six Meyer article pages: physical PDF pages
485--490 are printed pages 477--482. No page in either authorized render set
was skipped.

The Rabin inspection included the introductory claims and applications as well
as every page of Chapter III: ordinary acceptance on printed page 6; formula
translation on pages 7--10; the sequential-word dependency and Theorem 3.1 on
pages 17--19; marked and well-founded obligations on pages 19--24; dual
acceptance on pages 24--26; the two half-steps on pages 27--32; finite trees and
Lemmas 3.12--3.15 on pages 30--31; and emptiness on pages 32--34. The Meyer
inspection included the lower-bound theorem on printed page 478, the enumerated
theory list on page 479, the surrounding qualifications on pages 477--480, and
the remaining discussion and references on pages 481--482.

## Independent mathematical audit

### 1. Successor structures and ordinary tree semantics

The reconstruction keeps Rabin's root `\(\Lambda\)`, not `\(\epsilon\)`, and
states Definition 1.1 for every `\(0<n\leq\omega\)` with
`\(T_n=n^*\)`, the successors `\(r_i(x)=xi\)`, initial-segment order, and
lexicographic order. It also preserves the finite-`\(n\)` definability statement
and the `\(T_\omega\)` exception. These claims occur at
`n-c-014.tex:914--963` and `p09-rabin-1969-source-note.md:136--175` and agree
with Rabin printed page 5 (and the proof of Theorem 1.12 on printed page 11).

For a table `\(\langle S,M\rangle\)`, the reconstruction correctly derives a
run on an arbitrary-root valued tree `\((v,T_x)\)` as a map
`\(r:T_x\to S\)` obeying the two-child transition at each node. Ordinary
acceptance is exactly

\[
 \exists r\bigl(r(x)\in S_0\ \land\
   \forall\pi\,[\pi\text{ a path}\Rightarrow
       \operatorname{In}(r\!\upharpoonright\!\pi)\in F]\bigr),
 \qquad F\subseteq\mathcal P(S).
\]

Thus a transition table and an automaton have different tuples, valued trees
may have roots other than `\(\Lambda\)`, and failure of the table to have a
rooted run makes ordinary acceptance false. This is exact at
`n-c-014.tex:965--1014` and `p09-rabin-1969-source-note.md:176--243`, against
Rabin printed pages 5--7. Theorem 1.4 is also correctly described in both
directions at `n-c-014.tex:1016--1023`: one label coordinate is projected away,
and conversely one coordinate is added with no nodewise constraint. No unnamed
operation is used in place of those statements.

### 2. Formula tracks, run tracks, and the closed-sentence reduction

The map

\[
 (A_1,\ldots,A_n)\longmapsto (v_{\bar A},T),\qquad
 v_{\bar A}(x)=(\chi_{A_1}(x),\ldots,\chi_{A_n}(x)),
\]

is correctly typed as a bijection from `\(\mathcal P(T)^n\)` to full-root
`\(\{0,1\}^n\)`-valued trees. The forward translation separately retains the
principal-formula normal form, finite-tree witness and Lemma 3.12 lift, Boolean
operations, projection, and complement. The worked formula
`\(\exists x(x\in A\land r_0(x)\in B)\)` is a valid two-track instance: a
finite frontiered initial subtree can label both the witness and its left child.
The text explicitly marks that instance as handbook-owned rather than a printed
transition table. See `n-c-014.tex:1027--1077` and
`p09-rabin-1969-source-note.md:244--320`, against Rabin printed pages 7--9 and
30--31.

For the converse, coding the finite state set in `\(m\)` Boolean tracks yields
exactly the existential choice of one run; the root, move, and path conditions
then yield the prefix
`\(\exists B_1\cdots\exists B_m\,\forall C\)` with a set-quantifier-free
matrix. Lemma 1.2 supplies the single initial state. Starting from that state,
the move clauses force every descendant track value to code a genuine state,
so no uncoded bit vector creates a spurious run. This agrees with
`n-c-014.tex:1079--1091` and Rabin printed page 10.

For a closed sentence, writing it without loss as `\(\exists A_1F(A_1)\)` and
asking whether the automaton representing `\(F\)` has nonempty language is the
complete reduction. Theorem 1.6 decides that question. No regular-tree basis
step occurs or is needed. The reconstruction is exact at
`n-c-014.tex:1093--1098` and `p09-rabin-1969-source-note.md:279--292`, against
Rabin printed pages 9--10.

### 3. Theorem 3.1 product

I recomputed the product rather than checking only its tuple. Let a product run
on a branch have states `\((u_n,s_n)\)`. The displayed transition at
`n-c-014.tex:1121--1127` forces

\[
 u_{n+1}=K(u_n,s_n),\qquad u_0\text{ the word automaton's initial state},
\]

while the second coordinates obey the original tree table. Therefore the first
coordinates are exactly the unique deterministic Muller run on the branch's
second-coordinate word. Since `\(S\)` is finite,

\[
 p_1(\operatorname{In}((u_n,s_n)_{n<\omega}))
 =\operatorname{In}((u_n)_{n<\omega});
\]

if a first coordinate occurs infinitely often, some paired second coordinate
does too. Hence the designated family
`\(\{C\subseteq U\times S:p_1(C)\in H\}\)` is exact. The shared deterministic
first-coordinate history is coherent before a branch splits. The state set,
initial set, transition type, update, and Muller family at
`n-c-014.tex:1102--1139` and `p09-rabin-1969-source-note.md:321--350` agree with
Rabin printed page 18 and its continuation on page 19. There is no harmful
index shift.

### 4. Dual semantics, well-founded strata, and both half-steps

The pair sequence is correctly confined to the dual construction. Its type and
type-empty clauses are

\[
 \phi\in[\Omega]\iff
 \exists i\bigl(\operatorname{In}(\phi)\cap U_i\ne\varnothing
 \land\operatorname{In}(\phi)\cap L_i=\varnothing\bigr),
\]

and

\[
 \phi\in[\Omega,e]\iff \phi\in[\Omega]\land
 \exists j\bigl(\operatorname{rng}(\phi)\cap L_j=\varnothing\bigr).
\]

Dual acceptance is exactly the reversal

\[
 \forall r\,[r\text{ a run rooted in }s\Rightarrow
              \exists\pi\;r\!\upharpoonright\!\pi\in[\Omega]].
\]

Consequently it is true vacuously when no rooted run exists, unlike ordinary
acceptance. These details at `n-c-014.tex:1143--1188` and
`p09-rabin-1969-source-note.md:351--408` agree with Rabin printed pages 24--26.

The zero-length completion is also correct. With an empty pair list no path has
a listed type, so the universal dual implication holds exactly when there is no
rooted run. For `\(\Omega^\dagger=((S,S))\)`, every infinite path map into the
finite nonempty state set has a nonempty infinitely recurring set contained in
`\(S\)`; it cannot simultaneously meet and avoid `\(S\)`. Thus
`\([\Omega^\dagger]=\varnothing\)` and the positive-length representative has
exactly the empty list's dual semantics. Necessity, exact definition, standing
as a one-pair sequence, nonredundancy, and later use are all supplied together
at `n-c-014.tex:1190--1213`; its use in emptiness is explicit at
`n-c-014.tex:1340--1342`. The detailed note gives the same derivation at
`p09-rabin-1969-source-note.md:385--403`.

For a nonempty obligation set, absence of an infinite chain
`\(h_{m+1}\in H_{h_m}\)` is equivalent to an ordinal stratification in which
every member of `\(H_h\)` has smaller rank than `\(h\)`: strict ordinal descent
precludes a chain, while the successive minimal strata exhaust any
well-founded relation. The manuscript places this at Lemma 3.3 and places the
second transfinite construction in the converse of Lemma 3.11. It does not use
the word "transfinite" as a replacement for the marked trees, simultaneous
runs, same-state merging, or Theorem 3.1 path check. See
`n-c-014.tex:1218--1256,1296--1303` and
`p09-rabin-1969-source-note.md:410--436`, against Rabin printed pages 19--32.

The pair-sequence lengths also remain exact: Lemma 3.7 preserves length;
Lemma 3.8 preserves length while making the final lower set empty; Lemmas
3.9--3.10 use the length-`\(k-1\)` prefix in the last-lower-set-empty half-step;
and Lemma 3.11 plus Lemma 3.8 handles arbitrary length `\(k\)` before the
positive-`\(k\)` induction closes. No arbitrary case, last-lower-set-empty case,
or induction case is collapsed.

### 5. Finite trees and the exact Lemma 3.12--Corollary 3.15 division

At first use in each frozen record, `frontiered` is defined as Rabin's property
of a finite predecessor-closed set `\(E\subseteq T\)`: every node outside
`\(\operatorname{Ft}(E)\)` has both children in `\(E\)`. The text explains why
predecessor closure alone is insufficient, identifies the term's standing as a
property rather than a second tree object, and ties the distinction to later
uses. A finite valuation excludes the terminal-node frontier. The finite-tree
automaton has

\[
 M:S\times\Sigma\to
   \mathcal P((S\times S)\cup\{(f,f)\}),\qquad f\notin S,
\]

and `\(f\)` is correctly an external frontier value, not an ordinary state.
See `n-c-014.tex:1259--1287`, the genuine first use in the detailed note at
`p09-rabin-1969-source-note.md:294--319`, and the complete local definition in
the compact record at `p09-source-presentations-lot2-3.md:670`, against Rabin
printed page 30.

The four numbered results are assigned their exact roles:

- Lemma 3.12 lifts an automaton-definable finite-tree language to infinite
  trees with an accepted finite initial subtree.
- Corollary 3.13 uses that lift to close the principal-formula case.
- Lemma 3.14 is the König compactness statement extracting a finite subset of
  node--state obligations that still meets every infinite run.
- Corollary 3.15 applies Lemmas 3.14 and 3.12 to make the universal marked
  hitting condition automaton definable.

That division at `n-c-014.tex:1284--1294`,
`p09-rabin-1969-source-note.md:507--541`, and
`p09-source-presentations-lot2-3.md:670` agrees with Rabin printed pages 30--31.
Nothing in it changes an infinite input into a finite one or full monadic logic
into weak monadic logic.

### 6. The actual emptiness proof, root boundary, and finite base

The one-letter erasure at `n-c-014.tex:1307--1322` is exact. A run of the
unioned table chooses at every node a transition that came from at least one
original input letter, so nodewise choices reconstruct a valuation; erasing an
original valuation gives the converse. Original nonemptiness is therefore
acceptance of the unique one-letter full tree. Complementing that one-tree
language and applying Lemma 3.6 to its complement correctly converts the
original language into the dual membership question at
`n-c-014.tex:1323--1333`. This agrees with Rabin printed pages 32--33 and does
not insert a basis theorem.

Definition 3.7 is used with its exact root boundary. The restricted table keeps
the formal state set `\(R\)` and replaces transitions by
`\(N(s)\cap(R'\times R')\)`. Thus all states strictly below the root lie in
`\(R'\)`, while the specified root state may lie outside `\(R'\)`. This is
stated at `n-c-014.tex:1343--1351` and
`p09-rabin-1969-source-note.md:458--462`, matching Rabin printed pages 33--34.

For the first finite half-step, disjoint state strata terminate after at most
`\(|R|\)` nonempty additions. For `\(L_k=\varnothing\)` and `\(k>1\)`, the
exhaustive witness range must include every `\(H\subseteq U_k\)`. The empty
choice is exactly the already-shorter question at the root; every nonempty
choice uses the restricted table on `\(R\setminus H\)` for the resulting
length-`\(k-1\)` questions. The reconstruction explicitly distinguishes the
printed nonempty display from this handbook-owned exhaustive completion at
`n-c-014.tex:1353--1371` and
`p09-rabin-1969-source-note.md:452--496`, against Rabin printed pages 33--34.
The supplied finite-state example in the note correctly demonstrates that the
empty branch is not eliminable.

For `\(k=1\)` and `\(L_1=\varnothing\)`, the finite criterion is also exact.
It permits `\(m=0\)` and
`\(U_0=\{s_1,\ldots,s_m\}\subseteq U_1\)` to be empty, and for each
`\(0\leq i\leq m\)` requires a finite frontiered tree on which every run
beginning in `\(s_i\)` reaches `\(U_0\)` strictly below the root. If
`\(m=0\)`, this universal condition says precisely that the rooted finite tree
`\(E_0\)` has no compatible run from `\(s_0\)`. Because the transition choices
are finite, König's Infinity Lemma gives such a finite obstruction exactly when
there is no infinite rooted run. That is the vacuous dual-acceptance branch
omitted by Rabin's printed word "nonempty," and the manuscript clearly labels
its inclusion as a handbook-owned correction. See
`n-c-014.tex:1373--1389`, `p09-rabin-1969-source-note.md:463--496`, and
`p09-source-presentations-lot2-3.md:670`, against Rabin printed page 34. The
finite-tree existence question is correctly left as an external weak-monadic
decision-theorem dependency rather than misrepresented as a weak version of
the original full theory.

Together with the exact zero-length normalization, these finite reductions
close the effective emptiness argument stated at `n-c-014.tex:1392--1400` and
`p09-rabin-1969-source-note.md:498--505`.

### 7. Meyer consequence and complexity boundary

Meyer printed page 478 states a lower bound whose exponential-tower height
grows proportionally to the logarithm of sentence length for infinitely many
sentences in each listed theory. Printed page 479 lists “the theory of two
successors and prefix” and credits that case to Meyer and Stockmeyer. That
language is a literal sublanguage of Rabin's displayed binary structure, which
also contains the lexicographic order. Therefore an elementary-recursive
worst-case decision procedure for the displayed theory would restrict to one
for the listed sublanguage, contradicting the variable-height tower lower
bound. This leaves decidability and effectiveness untouched while refuting the
historical elementary-recursive qualification.

The reader states exactly that consequence, with its later-source standing, at
`n-c-014.tex:949--963`; the detailed note does so at
`p09-rabin-1969-source-note.md:157--174,498--501`; and the compact record does
so at `p09-source-presentations-lot2-3.md:662`. These agree with Rabin printed
pages 1 and 4 and Meyer printed pages 478--479. No stronger complexity claim is
made.

### 8. Applications, boundaries, bibliography, and cross-record consistency

The class-level application claims at `n-c-014.tex:1404--1421` match Rabin
printed pages 10--17: countable linear orders; the weak theory of arbitrary
linear orders; countable well-orders; countable unary-function structures and
the weak arbitrary-domain consequence; the stated Cantor-space,
`\(F_\sigma\)`, interval, and Boolean-algebra structures; and the encoded
Gale--Stewart determinacy assertion for `\(F_\sigma\)` payoff sets. The
detailed note at `p09-rabin-1969-source-note.md:543--573` and compact record at
`p09-source-presentations-lot2-3.md:672` preserve the same strength.

The reader's proof boundary at `n-c-014.tex:1423--1437` is accurate: it says
which proof architecture has been reconstructed, leaves the unprinted-in-the-
reader transition tables and inductions in Rabin's complete source, and does
not project Thomas's later basis route backward onto Section 3.12. Likewise,
McNaughton's word theorem remains explicitly external to Rabin's product
argument.

The frozen bibliography entries are internally consistent with the inspected
sources and manuscript uses: McNaughton at `handbook.bib:2290--2299`, Thomas at
`handbook.bib:2346--2355`, Meyer at `handbook.bib:5938--5947`, Rabin at
`handbook.bib:5973--5982`, and Thatcher--Wright at
`handbook.bib:5993--6002`. The reader, detailed note, and compact record agree
on ordinary versus dual acceptance, the product, all three handbook-owned edge
completions, the exact four-result finite-tree division, the Meyer correction,
and the restriction of any eventual acceptance to `N-c-014.d` manuscript
content. No undefined or redundant technical name survives: in particular,
`frontiered`, the external frontier value `\(f\)`, and
`\(\Omega^\dagger\)` each receive their necessity, definition, standing,
nonredundancy, and later use at first introduction.

## Mandatory-invariant disposition

R01--R23 and R26--R29 all pass. In particular, the audit found no
finite/infinite-tree, weak/full-logic, ordinary/dual, existence/effectivity,
source/later-route, or decidability/complexity conflation. The snapshot does not
claim acceptance of a render, build, neighboring presentation, Part IX, or the
book.

## Limitations

The evidence boundary did not authorize opening the McNaughton, Doner,
Thatcher--Wright, or Thomas works themselves. I therefore checked those items
as external dependencies and later-route boundaries exactly as Rabin's printed
article and the frozen manuscript state them; I did not independently audit the
proofs in those excluded publications. The two allowed Meyer/Rabin PDFs were
the only controlling printed sources. I also made no typographic or compiled-
output claim because no build or handbook-PDF inspection was authorized.

## Findings

None. Because no defect was found, there is no severity, finding identifier, or
minimum repair to report.

VERDICT: ACCEPT
