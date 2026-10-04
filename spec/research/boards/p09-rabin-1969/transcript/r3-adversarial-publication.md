# Round 3 adversarial publication and terminology review

## Outcome

The frozen Round 3 snapshot is **REJECTED at manuscript-content level** because
one unresolved must-fix finding, **AP-01**, violates the repository's first-use
terminology rule.  The defect is narrow: the source note's admission-status
history names `frontiered` and the finite-tree symbol \(f\) before the later
passages that supply their definitions and claim to be their first use.  The
later substantive definitions themselves are source-exact, mathematically
correct, and complete.  I found no independent mathematical, source-fidelity,
rights, complexity, or completion-status defect.

This verdict concerns only the frozen `N-c-014.d` manuscript content.  It does
not admit or reject rendered pages, a build, another presentation, Part IX, the
book, typesetting, human review, or user acceptance.

## Independence, evidence boundary, and limitations

I reviewed only:

- `spec/research/boards/p09-rabin-1969/charter.md`;
- the six objects in the charter's Frozen Round 3 snapshot;
- `tmp/pdfs/p09-rabin-1969/rendered/page-01.jpg` through
  `page-36.jpg`; and
- `tmp/pdfs/p09-rabin-1969/meyer1975-rendered/page-485.png` through
  `page-490.png`.

I did not read a Round 1 or Round 2 report, another Round 3 report, the board
ledger, the chair transcript, another board or transcript, the staging draft,
the layout extraction, or conversation/history as review evidence.  I did not
contact another reviewer.  I did not inspect a handbook PDF, run a test or
automated checker, invoke a repository script or TeX command, or perform a
build.

The external URLs and DOI registries were not independently queried because
they lie outside the frozen evidence set.  Accordingly, bibliography checking
was limited to (i) agreement among the frozen reader, source note, compact
record, and bibliography and (ii) the identities and pagination visible in the
permitted Rabin and Meyer sources.  Claims in the frozen source note about
earlier review outcomes were treated as authored status claims, not as evidence
from the excluded reports.

## Frozen-object identity

I freshly recomputed SHA-256 for every frozen object before substantive review.
All six observed digests equal the charter's Round 3 values.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `530EB0B226A239B260938F6BD1A9B247B60A19870F99050D32B879F22639AB23` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `4F5E6D98191DEA62094B88C81DD116809D05B970351CE99C8CE8ECF9C435D215` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `DC8B5386F57C829DBAFFDB2CF78575682448762E30880AEAC5D1FD19CA492C93` | exact match |

## Page inspection disclosure

I visually inspected every permitted image at original detail:

- Rabin physical page 1, the JSTOR/AMS custody-and-use cover;
- Rabin physical pages 2--36, corresponding to every printed article page,
  pp. 1--35; and
- Meyer physical PDF pages 485--490, corresponding to every printed article
  page, pp. 477--482.

The Rabin render sequence is complete and correctly offset by the custody
cover.  The Meyer title, author, proceedings identity, printed pagination, and
1975 Canadian Mathematical Congress notice are visible on printed pp. 477 and
482.  The images were used as reading aids; the matching PDFs are the frozen
controlling objects.

## Adversarial reconstruction checks

### Quantifiers, indices, and types

The ordinary and dual conditions were recomputed rather than accepted from the
prose summaries.

- Ordinary acceptance on Rabin printed p. 6 is exactly one rooted run followed
  by every path, with \(F\subseteq\mathcal P(S)\):
  \(\exists r\,\forall\pi\).  The reader's lines 974--1013 preserve the table
  versus automaton tuples, arbitrary-root domain, initial-state condition, and
  infinitely-recurring-state family.
- Definition 3.5 on printed p. 24 requires, for some common index \(i\), that
  the infinitely recurring set meet \(U_i\) and avoid \(L_i\).  The additional
  type-empty condition uses a possibly different index \(j\) whose \(L_j\) is
  avoided by the entire range.  Reader lines 1142--1165 preserve both indices
  and do not interchange range with infinite occurrence.
- Definition 3.6 on printed p. 25 is exactly
  \(\forall r\,\exists\pi\), with the run condition in the antecedent.  Hence
  it is vacuously true when no run starts in the named state.  Reader lines
  1166--1187 state this explicitly and do not misidentify the pair sequence as
  ordinary \(F\).
- Lemma 3.6 on printed p. 25 enumerates
  \(\mathcal P(S)\setminus(F\cup\{\varnothing\})\), which may be empty.  For an
  empty list no path has a listed type, so dual acceptance is equivalent to
  absence of a rooted run.  For \(\Omega^\dagger=((S,S))\), every infinite
  path map into the finite nonempty state set has a nonempty infinitely
  recurring subset of \(S\); it therefore cannot both meet and avoid \(S\).
  Reader lines 1189--1212 give the same empty path language and exactly the
  same dual semantics, clearly labeled as a handbook-owned normalization.
- In Theorem 3.1 on printed p. 18, the product state is \(U\times S\), the
  initial set is \(\{u_0\}\times S\), and a transition from \((u,s)\) sends
  both children to first coordinate \(K(u,s)\).  Along a branch this is the
  deterministic word run on the second-coordinate state sequence, beginning
  at \(u_0\).  The designated family is exactly
  \(\{C\subseteq U\times S:p_1(C)\in H\}\).  Reader lines 1101--1138 have no
  harmful index or type shift.

### Finite trees and the external frontier symbol

Rabin printed p. 30 first defines a finite binary tree as finite and
predecessor closed, then calls it `frontiered` when every nonterminal node has
both children, and thereafter uses “finite tree” for the frontiered case.  The
distinction is real: predecessor closure alone permits a node with one child.
The finite valuation has domain \(E\setminus\operatorname{Ft}(E)\).  The
finite-tree automaton is
\(\langle S,M,s_0,f\rangle\), with \(f\notin S\) and
\(M:S\times\Sigma\to\mathcal P((S\times S)\cup\{(f,f)\})\); \(f\) is the
external symbol assigned at terminal nodes, not an ordinary state.

Reader lines 1258--1293 and compact-record line 670 correctly give the
definition, standing, nonredundancy, and later uses of `frontiered`, and they
correctly type \(f\).  Source-note lines 293--306 and 499--526 do likewise.
AP-01 concerns only the earlier status-history occurrence in that same note.

### Complementation and emptiness architecture

The source pages support the reader's separation of constructions.

- Printed pp. 19--24 use marked trees, simultaneous activated copies,
  same-state merging, and Theorem 3.1's word check; these are not replaceable
  by the phrase “transfinite proof.”
- Printed pp. 19 and 23--29 locate well-foundedness in the no-infinite-descent
  definition, lower ordinal strata, and the converse construction in Lemma
  3.11.  Reader lines 1217--1256 and 1295--1302 retain these loci and the two
  positive-length half-steps.
- Printed pp. 30--31 give the finite-tree lift, principal-formula completion,
  and compactness lemma as distinct steps.  The reader does not turn the
  infinite input or full monadic theory into a weak theory.
- Printed pp. 32--34 first erase the input alphabet to one letter, complement
  the resulting one-tree language, convert it to a specified dual question,
  and then recurse on finite tables and pair sequences.  Reader lines
  1304--1389 preserve that path and do not insert a regular-tree basis theorem.
- Definition 3.7 on printed p. 33 restricts states below the root while leaving
  the root state formally available.  Reader lines 1342--1350 preserve this
  boundary.
- For the last-lower-set-empty half-step, the reader's added \(H=\varnothing\)
  branch reduces directly to the shorter dual question; every nonempty
  \(H\subseteq U_k\) uses the table restricted below the root to \(R\setminus
  H\).  This is the exhaustive completion of printed p. 34's nonempty clause,
  not a source attribution.
- At \(k=1\), permitting \(m=0\) makes \(U_0\) empty and requires one finite
  frontiered tree on which no run begins in \(s_0\).  König's Infinity Lemma
  makes that finite obstruction equivalent to absence of an infinite run.
  Reader lines 1372--1388 label this as a second handbook-owned edge repair and
  preserve the external weak-monadic decision dependency.

### Complexity, attribution, applications, and rights

Rabin printed pp. 1, 4, and 12 state elementary-recursive claims.  Meyer
printed p. 478 begins a tower lower-bound theorem for infinitely many inputs,
and printed p. 479 lists “the theory of two successors and prefix” as item 5,
credited to Meyer and Stockmeyer.  That language is contained in the displayed
binary successor/prefix theory, so an elementary-recursive worst-case upper
bound for the latter would contradict the lower bound.  Reader lines 941--963
and 1391--1399 therefore correctly reject only the historical complexity
qualification while retaining decidability and effectiveness.

Rabin printed pp. 10--17 support the stated class-level linear-order,
unary-function, Cantor-space, Boolean-algebra, and game applications.  Reader
lines 1401--1420 do not inflate their strength.  Reader lines 1422--1436 state
the reconstruction boundary, leave the omitted transition details in the
complete source, and keep Thomas's later basis route and McNaughton's external
word theorem out of Rabin's proof.

The custody cover limits the JSTOR copy to personal, noncommercial use absent
permission and directs further-use questions to the publisher.  Source-note
lines 74--85 expressly deny that either public route supplies an open-content
or republication licence and classify the local PDFs and renders as research
objects.  I found no rights inflation.

## R01--R29 disposition

| Invariant | Disposition |
|---|---|
| R01 | Pass: \(\Lambda\) is retained; no silent \(\epsilon\) substitution. |
| R02 | Pass: \(0<n\leq\omega\), both orders, successors, finite definability qualification, and \(T_\omega\) exception are exact. |
| R03 | Pass: arbitrary roots, distinct table/automaton tuples, \(\exists r\,\forall\pi\), and \(F\subseteq\mathcal P(S)\) are exact. |
| R04 | Pass: the finite pair sequence is dual, the prefix is \(\forall r\,\exists\pi\), and no-run vacuity is explicit. |
| R05 | Pass: Theorems 1.3--1.6 retain the exact closure, complement, and emptiness dependencies. |
| R06 | Pass: the full-root bit-track bijection and the separate principal-formula, finite-lift, Boolean, projection, and complement steps are stated. |
| R07 | Pass: the worked two-track formula is explicitly handbook-owned. |
| R08 | Pass: one-initial-state normalization, run encoding, \(\exists\bar B\,\forall C\), and direct nonemptiness reduction are exact. |
| R09 | Pass: the Muller product is exactly typed and its indexing is sound for infinite-occurrence acceptance. |
| R10 | Pass: type, type-empty, quantifier reversal, and complement role are exact. |
| R11 | Pass: marked obligations, simultaneous runs, merging, and the path check are retained as necessary machinery. |
| R12 | Pass: no-infinite-descent well-foundedness, lower strata, and both transfinite loci are exact and not substituted for finite constructions. |
| R13 | Pass: Lemmas 3.7--3.11 retain their lengths and the positive-length induction follows an explicit zero-length normalization. |
| R14 | **Fail (AP-01):** the substantive finite-tree account is exact, but the source note first names `frontiered` and \(f\) before supplying the mandatory first-use bundle. |
| R15 | Pass: finite-tree lift, principal-formula use, compactness, and complement roles remain distinct; no weak/full conflation. |
| R16 | Pass: one-letter erasure, complement, dual conversion, and membership decision are preserved; no basis substitution. |
| R17 | Pass: current table/sequence typing and the Definition 3.7 root-state boundary are explicit. |
| R18 | Pass: all \(H\subseteq U_k\), including the direct empty branch, are covered and correctly labeled. |
| R19 | Pass: \(m\geq0\), empty \(U_0\), \(E_0,\ldots,E_m\), the no-run obstruction, König equivalence, and external weak-theory dependency are exact. |
| R20 | Pass: Rabin's claim is historical, Meyer supplies the later lower bound and attribution, and the sublanguage consequence is valid. |
| R21 | Pass: Chapter II applications are stated at their source class-level strength. |
| R22 | Pass: reconstruction limits, Thomas's later route, and McNaughton's external theorem are explicit. |
| R23 | Pass: no source-number, locator, notation, strength, or attribution defect found in the permitted evidence. |
| R24 | Pass subject to the stated external-registry limitation: the frozen records agree on identities, correction, custody, bibliography data, and pending status. |
| R25 | Pass: public access is not represented as an open or republication licence; research objects are not declared distributable assets. |
| R26 | **Fail (AP-01):** the source note violates the five-part first-use terminology rule. |
| R27 | Pass: no finite/infinite, weak/full, ordinary/dual, existence/effectivity, source/later-route, or decidability/complexity conflation found. |
| R28 | Pass: all status language leaves Round 3 pending and limits possible admission to `N-c-014.d` manuscript content. |
| R29 | Pass: the empty sequence and \(\Omega^\dagger=((S,S))\) have exactly the same dual semantics and the normalization is editorially owned. |

## Finding

### AP-01 — Must-fix — the source note defeats its own claimed first use of `frontiered` and \(f\)

- **Exact frozen manuscript location:**
  `spec/research/p09-rabin-1969-source-note.md:22--24`.  The internal
  contradiction is visible at lines 293--306 (“At this first use”), lines
  499--520 (the later finite-tree and \(f\) definitions), and lines 629--632
  (the claim that the source note now defines the terminology at first use).
- **Controlling printed source page:** Rabin printed p. 30.
- **Defect:** The admission-status history at lines 22--24 is the source note's
  first occurrence of the technical adjective `frontiered` and of the
  finite-tree symbol \(f\).  That location reports that `frontiered` formerly
  lacked standing and nonredundancy, and that \(f\) was formerly called a
  state, but it does not itself supply the required five-part bundle.  For
  `frontiered`, it gives neither the exact condition on \(E\), the property's
  standing, its distinction from predecessor closure, nor the later use that
  needs full branching.  For \(f\), it omits \(f\notin S\), the exact
  transition codomain, its terminal-node role, and the reason it cannot be an
  ordinary state.  Those facts appear only later.  Therefore line 293's “At
  this first use” and lines 629--630's claim of definition at first use are
  false in the frozen note.  A change-history paragraph does not suspend the
  repository's rule that the definition, standing, nonredundancy, necessity,
  and use appear where a technical name first appears.
- **Minimum sufficient repair:** Remove the two technical names from the
  admission-history paragraph, for example by replacing lines 22--25 with
  prose saying only that Round 2 exposed two first-use terminology defects in
  the finite-tree discussion and that the discussion below now supplies the
  required definitions, standing, distinctions, and uses.  This leaves
  `frontiered` to be introduced with its complete five-part bundle at lines
  293--304 and leaves the finite-tree \(f\) to be introduced with
  \(f\notin S\), its transition type, external standing, nonredundancy, and use
  at lines 510--520.  Alternatively, the full five-part bundles could be
  repeated at lines 22--24, but that is a larger and less economical repair.

Because AP-01 is a must-fix on the hash-pinned snapshot, the present report
cannot accept it even though all mathematical and source-critical checks were
otherwise clean.  Any content repair changes a frozen object and therefore
requires a newly hash-pinned blind round under the charter.

VERDICT: REJECT — AP-01
