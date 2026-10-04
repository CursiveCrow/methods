# Round 1 — adversarial publication and terminology

## Disposition

I reject the frozen Round 1 snapshot.  The reconstruction gets the ordinary
and dual semantics, the printed finite-state constructions, the Meyer
correction, the source/rights boundary, and the topic-level completion boundary
substantially right.  It nevertheless leaves the zero-length dual sequence
undischarged after expressly preserving vacuous dual acceptance, and the compact
record coins one redundant undefined tree term.  Both defects are local, but
both violate mandatory invariants.

## Identity, pages, and evidence boundary

I recomputed all six SHA-256 identities before substantive review:

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `2EF14C7487380F2E08B48BD7A8E79533A8EAC6F44A939A057265F34F4EE0EAC5` | exact match |
| `handbook/bib/handbook.bib` | `1EAADD6F25B9DFEE82265747ABEA78B782950217F397072EBA62D48004B79BE5` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `2DC08752861ACD364E020FA441AC37A0E597B532C2ED3FE85013C03F8D907AA2` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `4CFCA8E323720A9087604F7682664CDD41840FE3DCFB4EB9CD9F665696D945BB` | exact match |

I visually inspected at original detail every permitted source render: Rabin
physical p. 1, the JSTOR/AMS custody-and-use cover, and physical pp. 2--36,
which are all printed article pp. 1--35; and Meyer physical PDF pp. 485--490,
which are all printed article pp. 477--482.  Formulae, symbols, pagination, and
wording were judged from those renders and the hash-pinned PDFs, not OCR.

I read the complete 1,382-line reader file and the complete 550-line Rabin
source note; I read the charter-scoped `N-c-014.c`--`.e` compact records,
including lines 660--680, and the charter-named Rabin, Meyer,
Thatcher--Wright, McNaughton, and Thomas bibliography entries.  I used no
ledger, chair transcript, other reviewer text, Trakhtenbrot board material,
staging draft, layout extraction as evidence, conversation summary, or
handbook PDF.  I contacted no reviewer.  I ran no test, automated checker,
repository script, TeX command, build, or handbook-PDF inspection.

The positive description of Thomas's later route could be checked for internal
consistency and separation in the frozen reader, compact record, and
bibliography, but Thomas's chapter body was not one of the charter-permitted
source objects.  I therefore independently verified the controlling negative
claim—Rabin printed pp. 32--34 contain no regular-tree basis step—and the
attribution boundary, not Thomas's chapter line by line.  The bibliography
audit was correspondingly confined to the identities named in the charter's
review scope.

## Findings

### AP-R1-01 — must-fix — the zero-length dual sequence is lost despite vacuous acceptance

**Frozen manuscript locations.**  The reader defines a finite sequence
\(\Omega=((L_i,U_i))_{1\leq i\leq k}\) without requiring \(k>0\) at
`handbook/parts/p09/presentations/n-c-014.tex:1142-1165`, and correctly says
that \(D(\mathfrak A_0,\Omega,s)\) holds vacuously when there is no run from
\(s\) at lines 1166--1187.  It then summarizes the complementation induction
only through the last-lower-set-empty and arbitrary positive-length half-steps
at lines 1223--1227 and calls Corollary 3.15 the \(k=1\) base at lines
1251--1254.  The emptiness reconstruction likewise starts with a current
length-\(k\) sequence at lines 1298--1319, treats \(k>1\) at lines 1321--1325,
treats \(k=1\) at lines 1327--1336, and immediately claims closure of Theorem
1.6 at lines 1339--1345.  The same unqualified positive-length architecture is
asserted in `spec/research/p09-rabin-1969-source-note.md:323-379` and
`:387-418`, and compressed in
`spec/research/p09-source-presentations-lot2-3.md:668-670`.

**Controlling printed pages.**  Rabin printed p. 25 constructs Lemma 3.6's
sequence by enumerating \(\mathcal P(S)-F-\{\varnothing\}\); that set can be
empty.  Printed pp. 31--32 begin the displayed induction with the \(k=1\)
case, and printed pp. 32--34 reuse that induction in the emptiness decision.
Definition 3.6 on printed p. 25 makes an empty sequence semantically
nontrivial: since no path can be of an empty type sequence,
\(D(\mathfrak A_0,\varnothing,s)\) holds exactly when no run rooted at \(s\)
exists.

**Defect.**  The snapshot preserves all premises that make the omitted case
real: move tables may have an empty move set (reader line 986), dual acceptance
is a universal implication (lines 1166--1183), and Lemma 3.6 can produce no
pairs.  For a concrete witness, take \(S=\{s\}\), alphabet
\(\{a,b\}\), \(M(s,a)=\{(s,s)\}\), \(M(s,b)=\varnothing\), initial state
\(s\), and \(F=\mathcal P(S)\).  The ordinary language consists exactly of
the all-\(a\) tree; its complement consists of trees with a \(b\)-node, on
which there is no global run.  Lemma 3.6's enumerated set is empty, so the dual
description has \(k=0\), not the claimed \(k=1\) base.  The reconstruction's
own vacuity sentence therefore exposes an unproved case in both the
complementation and emptiness closures.  This is a mathematical completeness
defect under R04, R05, R13, R16, R17, R27, not merely an omitted expository
detail.

**Minimum sufficient repair.**  Add and label a handbook-owned zero-length
completion before both uses of the pair-length induction, and reconcile the
source note and compact record.  The shortest repair is to say that, whenever
Lemma 3.6's list is empty, it is replaced by the one-pair sequence
\(((S,S))\).  Because every map from an infinite path into finite nonempty
\(S\) has a nonempty infinitely-recurring set, it cannot simultaneously meet
and avoid \(S\); hence no path has that type, and
\(D(\mathfrak A_0,((S,S)),s)=D(\mathfrak A_0,\varnothing,s)\).  The existing
arbitrary length-one step and \(k=1\) base then apply.  An explicit separate
no-run proof would also suffice, but merely writing \(k\geq1\) would not.

### AP-R1-02 — must-fix — `full-frontiered` is undefined, redundant, unused terminology

**Frozen manuscript location.**  The compact record says that Section 3.10
defines “finite predecessor-closed, full-frontiered binary trees” at
`spec/research/p09-source-presentations-lot2-3.md:670`.  This is the sole
occurrence of `full-frontiered` in the frozen text.  The reader instead gives
the exact clauses at `handbook/parts/p09/presentations/n-c-014.tex:1230-1237`,
and both the reader at line 1329 and source note at
`spec/research/p09-rabin-1969-source-note.md:426-445` use the source term
`frontiered`.

**Controlling printed page.**  Rabin printed p. 30 calls \(E\)
`frontiered` when every nonterminal member has both binary successors; it then
declares that “finite tree” will mean finite frontiered tree.  The source does
not introduce `full-frontiered`.

**Defect.**  The added hyphenated name has no necessity because `frontiered`
already states the distinction, no exact definition at its occurrence, no
declared standing, no nonredundancy explanation, and no later use.  It also
breaks agreement between the compact record and the other two frozen records.
It therefore fails every prong of the repository's technical-name rule and
violates R24 and R26.

**Minimum sufficient repair.**  Replace `full-frontiered` with Rabin's already
defined `frontiered`; introduce no new synonym.

## Mandatory-point audit

| Point | Result | Adversarial check against frozen manuscript and printed source |
|---|---|---|
| R01 | pass | Reader lines 914--917 retain \(\Lambda\); Rabin printed pp. 2, 5. |
| R02 | pass | Lines 918--963 type both orders, every \(0<n\leq\omega\), finite-\(n\) definability, and the \(T_\omega\) exception; printed pp. 3--5. |
| R03 | pass | Lines 965--1014 distinguish arbitrary-root valuations, tables, automata, and \(\exists r\forall\pi\) with \(F\subseteq\mathcal P(S)\); printed pp. 5--7. |
| R04 | must-fix | Lines 1142--1187 get the pair type, quantifier reversal, and vacuity right, but the vacuity is not carried through \(k=0\): AP-R1-01; printed pp. 24--25. |
| R05 | must-fix | Lines 1016--1022 state the exact dependencies, but the claimed Chapter III closure has the zero-length gap in AP-R1-01; printed pp. 7, 31--34. |
| R06 | pass | Lines 1026--1064 separately give the typed bijection, principal case, finite-tree lift, Boolean operations, projection, and complement; printed pp. 7--9, 30--31. |
| R07 | pass | Lines 1066--1076 mark the worked formula as handbook-owned and correctly require both witness nodes to be labelled; printed pp. 8, 30--31 control the construction. |
| R08 | pass | Lines 1078--1097 preserve one-initial-state normalization, state-track run encoding, \(\exists\bar B\forall C\), and the direct nonemptiness reduction; printed pp. 9--10. |
| R09 | pass | Lines 1099--1138 have \(K:U\times S\to U\), state set \(U\times S\), initial set \(\{u_0\}\times S\), update \(K(u,s)\) on both children, and the projected designated family.  The source's one-step update is exactly the word-run convention, and finite-prefix shifts would not alter `In`; printed pp. 17--19. |
| R10 | pass | Lines 1142--1187 distinguish `In` from full range in the \(\Omega\)-empty clause and preserve ordinary/dual reversal and complement role; printed pp. 24--25. |
| R11 | pass | Lines 1192--1228 retain marked obligations, simultaneous copies, same-state merging, and the Theorem 3.1 path check; printed pp. 19--24. |
| R12 | pass | Lines 1201--1207 and 1259--1266 give absence of infinite descent, lower ordinal strata, and the exact Lemma 3.3/3.11 transfinite loci without replacing finite constructions; printed pp. 19--20, 28--30. |
| R13 | must-fix | Positive lengths and both half-steps are reported at lines 1209--1227, but the claimed induction is not complete at length zero: AP-R1-01; printed pp. 25--32. |
| R14 | must-fix | Reader lines 1230--1247 correctly type the finite tree, omitted frontier valuation, \(f\notin S\), and transition codomain; the compact record's redundant name fails publication terminology: AP-R1-02; printed p. 30. |
| R15 | pass | Lines 1247--1257 keep the principal-formula lift, finite compactness/hitting role, and infinite/full-logic boundary distinct; printed pp. 30--31. |
| R16 | must-fix | Lines 1268--1296 correctly erase, complement, dualize, and pose one-tree membership without a basis theorem, but the resulting membership procedure omits \(k=0\): AP-R1-01; printed pp. 32--34. |
| R17 | must-fix | Lines 1298--1311 correctly name the current table/sequence and preserve the root-state boundary; the subsequent recursion begins only at positive length: AP-R1-01; printed pp. 33--34. |
| R18 | pass | Lines 1313--1325 retain finite disjoint strata, nonempty \(H\subseteq U_k\), restriction to \(R\setminus H\), and reduction to \(k-1\); printed pp. 33--34. |
| R19 | pass with AP-R1-01 boundary | Lines 1327--1336 reproduce the nonempty \(U_0=\{s_1,\ldots,s_m\}\), \(E_0,\ldots,E_m\), and external weak-theory dependency exactly for \(k=1\); it does not itself discharge \(k=0\); printed p. 34. |
| R20 | pass | Lines 941--960 and 1339--1345 report rather than retain Rabin's claim.  Meyer printed pp. 478--479 give the variable-height tower lower bound and list “the theory of two successors and prefix” under Meyer and Stockmeyer; the sublanguage conclusion is valid. |
| R21 | pass | Lines 1347--1366 preserve the class-level linear-order, unary-function, Cantor-space, Boolean-algebra, and game results; Rabin printed pp. 11--17. |
| R22 | pass within evidence boundary | Lines 1368--1382 state what remains in Rabin and keep Thomas's later basis route separate; lines 1113--1138 identify McNaughton as external.  Rabin printed pp. 18, 32--34 support both source boundaries. |
| R23 | pass except AP-R1-02 | Numbering, source locators, formulas, and attributions checked against all printed pages were accurate; the compact record alone substitutes the unsupported tree name in AP-R1-02. |
| R24 | must-fix | Meyer correction, scan URL, pending-review state, and the charter-named bibliography identities agree, but compact line 670 disagrees terminologically with the reader and detailed note: AP-R1-02. |
| R25 | pass | Source-note lines 66--77 expressly deny open-content/republication permission and classify local PDFs/renders as research objects; the Rabin cover and Meyer printed p. 477 support the custody caution. |
| R26 | must-fix | The reader's editorial symbols and distinctions are eliminable and typed where introduced; compact line 670's one-use `full-frontiered` fails necessity, definition, standing, nonredundancy, and use: AP-R1-02. |
| R27 | must-fix | The principal finite/infinite, weak/full, ordinary/dual, source/later, and decidability/complexity distinctions are preserved, but vacuous dual acceptance is not reconciled with the positive-length recursion: AP-R1-01. |
| R28 | pass | Source-note lines 3--21 and 514--550 and compact line 672 limit status to integrated, pending-review `N-c-014.d` manuscript content; no build, page, human, user, part, or book admission is asserted. |

VERDICT: REJECT — AP-R1-01, AP-R1-02
