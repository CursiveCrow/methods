# Round 1 source-fidelity report: Rabin 1969 for `N-c-014.d`

## Seat, scope, and result

I reviewed the frozen six-object Round 1 snapshot in the source-fidelity,
evidence, and historical-language seat.  I find no blocker, must-fix,
should-fix, consider, discard, or unresolved-user item within this seat's
mandatory points R01--R25 and R28.  This result concerns only the manuscript
content assigned to `N-c-014.d`; it does not make any broader admission,
typesetting, build, visual-publication, human-review, or user-acceptance claim.

## Independence and evidence boundary

- I read the charter before reviewing any evidence.
- I used only the charter, the six frozen objects, and the two chartered
  original-detail render sets.  The authored source note was treated as a claim
  set to be checked against the printed pages, not as controlling source
  evidence.
- I did not read a ledger, the chair transcript, another reviewer report or
  transcript, a Trakhtenbrot board record, the staging Rabin draft, the layout
  extraction, a conversation summary, or another reviewer's messages.  I did
  not contact another reviewer.
- I read all four frozen textual objects in full: all 1,382 lines of
  `handbook/parts/p09/presentations/n-c-014.tex`, all 6,272 lines of
  `handbook/bib/handbook.bib`, all 550 lines of
  `spec/research/p09-rabin-1969-source-note.md`, and all 915 lines of
  `spec/research/p09-source-presentations-lot2-3.md`.
- I ran no test, automated checker, repository script, TeX command, build, or
  handbook-PDF inspection.  Formulae, symbols, pagination, and historical
  wording were judged from the hash-pinned PDFs through their original-detail
  page renders.

## Frozen-object identity

All six SHA-256 values were recomputed before substantive comparison and match
the charter exactly.

| Frozen object | Charter SHA-256 | Recomputed SHA-256 | Result |
|---|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `2EF14C7487380F2E08B48BD7A8E79533A8EAC6F44A939A057265F34F4EE0EAC5` | `2EF14C7487380F2E08B48BD7A8E79533A8EAC6F44A939A057265F34F4EE0EAC5` | match |
| `handbook/bib/handbook.bib` | `1EAADD6F25B9DFEE82265747ABEA78B782950217F397072EBA62D48004B79BE5` | `1EAADD6F25B9DFEE82265747ABEA78B782950217F397072EBA62D48004B79BE5` | match |
| `spec/research/p09-rabin-1969-source-note.md` | `2DC08752861ACD364E020FA441AC37A0E597B532C2ED3FE85013C03F8D907AA2` | `2DC08752861ACD364E020FA441AC37A0E597B532C2ED3FE85013C03F8D907AA2` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `4CFCA8E323720A9087604F7682664CDD41840FE3DCFB4EB9CD9F665696D945BB` | `4CFCA8E323720A9087604F7682664CDD41840FE3DCFB4EB9CD9F665696D945BB` | match |

The PDF lengths stated in the detailed note also agree with the frozen files:
912,831 bytes for Rabin and 53,151,542 bytes for the complete Meyer proceedings
volume.

## Printed-page inspection

- Rabin: I inspected `rendered/page-01.jpg` through `page-36.jpg`, each at
  original detail.  Physical page 1 is the JSTOR/AMS custody-and-use cover;
  physical pages 2--36 are printed article pp. 1--35.  Thus the cover and every
  one of the thirty-five printed article pages were inspected.
- Meyer: I inspected `meyer1975-rendered/page-485.png` through `page-490.png`,
  each at original detail.  These are printed pp. 477--482, the complete six-page
  Meyer article within the frozen official proceedings volume.
- The Rabin cover identifies the article, journal, volume, July 1969 date,
  pp. 1--35, AMS publisher, and JSTOR use restrictions.  Rabin printed p. 1
  identifies the article and author; printed p. 35 closes the reference list and
  author affiliations.  Meyer printed p. 477 identifies the article and author;
  printed pp. 478--479 contain the tower lower bound and the exact
  two-successors-and-prefix attribution; printed p. 482 closes the report and
  references.

## Findings

None.

One apparent wording tension was checked and does not support a finding.
`n-c-014.tex:974--986` types $M$ as the total set-valued function
$S\times\Sigma\to\mathcal P(S\times S)$ and then says that the move table
need not be total.  In context, that sentence says that an input pair may have
no available move, equivalently $M(s,a)=\varnothing$; it does not make $M$
a partial function.  This is the possibility used explicitly at
`n-c-014.tex:1181--1184` to explain vacuous dual acceptance.  Rabin's printed
p. 6 supplies the displayed function type and permits the empty value through
the powerset codomain.  The surrounding exact type therefore eliminates the
possible colloquial ambiguity.

## Mandatory-point audit

| Point | Exact frozen manuscript location | Controlling printed evidence | Result and source-fidelity check |
|---|---|---|---|
| R01 | `n-c-014.tex:914--917` | Rabin p. 5 | Pass.  The empty word is $\Lambda$ in the print and $\Lambda$ is retained; the reader expressly rejects a silent $\epsilon$ substitution. |
| R02 | `n-c-014.tex:918--963`, especially `941--952` | Rabin pp. 3--5 and 10--11 | Pass.  The range (0<n\le\omega), (T_n=n^*), all successors, both orders, finite-(n) definability, the (T_\omega) exception, Theorem 1.1, and Theorem 1.12 have the printed strength. |
| R03 | `n-c-014.tex:965--1014` | Rabin pp. 5--7 | Pass.  Arbitrary roots (T_x), valued trees, the two distinct tuples, run type, (F\subseteq\mathcal P(S)), and ordinary (\exists r\,\forall\pi) acceptance agree with Definitions 1.2--1.5. |
| R04 | `n-c-014.tex:982--1011` and `1142--1187` | Rabin pp. 6 and 24--26 | Pass.  Ordinary (F) and the later finite pair sequence are kept distinct.  Definition 3.6 has (\forall r\,\exists\pi), and no-run vacuity is explicit. |
| R05 | `n-c-014.tex:1016--1022` and `1092--1097` | Rabin pp. 6--10 | Pass.  Theorems 1.3--1.6 supply union/intersection, projection/cylindrification, complement, and emptiness, and the sentence proof uses the last two without an inserted basis theorem. |
| R06 | `n-c-014.tex:1026--1064` | Rabin pp. 7--9 and 30--31 | Pass.  The (n)-track map is typed and bijective at the full root.  Principal formulas, the deferred finite-tree construction, Boolean operations, projection, and complement retain separate roles. |
| R07 | `n-c-014.tex:1066--1076` | Rabin pp. 8--9 and 30--31 | Pass.  The displayed two-track formula is visibly a handbook-worked instance of Rabin's construction, not a falsely quoted source table. |
| R08 | `n-c-014.tex:1078--1097` | Rabin pp. 9--10 | Pass.  Theorem 1.10's state tracks, Lemma 1.2 normalization, local move condition, path condition, and (\exists\bar B\,\forall C) prefix are exact.  The closed sentence goes directly to language nonemptiness. |
| R09 | `n-c-014.tex:1101--1138` | Rabin pp. 17--19 | Pass.  The deterministic Muller word automaton, (K:U\times S\to U), product (U\times S), starts, update, and projected designated family match Theorem 3.1.  The one-position shift does not change infinite-occurrence acceptance. |
| R10 | `n-c-014.tex:1142--1187` | Rabin pp. 24--26 | Pass.  Definition 3.5's type and type-empty clauses and Definition 3.6's ordinary/dual reversal have the printed quantifiers and complement role. |
| R11 | `n-c-014.tex:1192--1200` and `1223--1227` | Rabin pp. 19--24 and 31--32 | Pass.  Marking, iterative obligations, simultaneous copies, same-state merging, and Theorem 3.1's path check remain necessary finite-state constructions. |
| R12 | `n-c-014.tex:1201--1207` and `1259--1266` | Rabin pp. 19--20 and 28--30 | Pass.  Well-foundedness is absence of infinite descent, the ordinal strata are lower, and the two transfinite uses are assigned to Lemmas 3.3 and 3.11 without replacing the finite construction. |
| R13 | `n-c-014.tex:1209--1228` | Rabin pp. 25--32 | Pass.  Lemma 3.7 preserves length; Lemma 3.8 preserves length and empties the last lower set; Lemmas 3.9--3.11 and the two half-steps preserve the arbitrary, last-empty, and induction-on-(k) cases. |
| R14 | `n-c-014.tex:1230--1247` | Rabin pp. 30--31 | Pass.  The finite tree is finite, predecessor closed, and full before its frontier; the valuation excludes the frontier; (f\notin S) and the exact transition codomain are printed correctly. |
| R15 | `n-c-014.tex:1248--1257` and `1339--1345` | Rabin pp. 30--32 and 34 | Pass.  Lemma 3.12, Corollary 3.13, Lemma 3.14, and Corollary 3.15 retain their distinct witness, complement, compactness, and base-case roles.  The text explicitly denies a finite/full or weak/full conflation. |
| R16 | `n-c-014.tex:1270--1296` | Rabin pp. 32--33 | Pass.  The alphabet-erasure table, one-tree membership equivalence, complement, dual conversion, and final membership question reproduce Section 3.12; no regular-tree basis theorem is substituted. |
| R17 | `n-c-014.tex:1298--1311` | Rabin pp. 33--34 | Pass.  Each recursive question names its current finite table and pair sequence.  Definition 3.7 retains the formal state set and constrains only states strictly below the root. |
| R18 | `n-c-014.tex:1313--1325` | Rabin pp. 33--34 | Pass.  The arbitrary half-step terminates by disjoint finite-state strata.  The last-empty-lower-set half-step uses nonempty (H\subseteq U_k), restricts to (R\setminus H), and reduces the sequence to length (k-1). |
| R19 | `n-c-014.tex:1327--1345` | Rabin pp. 34--35 | Pass.  The exact nonempty (U_0=\{s_1,\ldots,s_m\}\subseteq U_1), family (E_0,\ldots,E_m), universal run condition below the root, and external Doner/Thatcher--Wright weak-theory dependency are retained. |
| R20 | `n-c-014.tex:952--960` and `1339--1341` | Rabin pp. 1, 4, 7, and 34; Meyer pp. 478--479 | Pass.  Rabin's elementary-recursive wording is reported only as historical.  Meyer prints the non-elementary tower lower bound and item 5 credits the theory of two successors and prefix to Meyer and Stockmeyer.  The sublanguage consequence removes only the worst-case bound, not decidability or effectiveness. |
| R21 | `n-c-014.tex:1349--1366` | Rabin pp. 11--17 | Pass.  The linear-order, unary-function, Cantor/(F_\sigma), Boolean-algebra/ideal, and game results retain their exact countable, weak, first-order, and monadic class qualifications. |
| R22 | `n-c-014.tex:910--912` and `1368--1382` | Rabin pp. 17--19 and 32--34; Thomas's later body is outside the two frozen PDFs | Pass within the chartered evidence.  The reader inventories what it reconstructs and leaves the remaining transition tables and inductions in Rabin.  McNaughton's word result is expressly external where Rabin invokes it.  The Thomas basis route is separately and later attributed, never made Rabin's emptiness proof. |
| R23 | `n-c-014.tex:910--1382` | Rabin pp. 1--35 and Meyer pp. 477--482 | Pass.  The numbered definitions, lemmas, corollaries, theorems, chapter/section locators, symbols, theorem strengths, source/later attribution, and page citations agree throughout. |
| R24 | Reader locations above; `p09-rabin-1969-source-note.md:1--84,86--117,119--512,514--550`; compact record `p09-source-presentations-lot2-3.md:660--672`; bibliography `handbook.bib:2290--2299,2346--2355,5938--5947,5973--5982,5993--6002` | Rabin cover and pp. 1--35; Meyer pp. 477--482; Rabin dependency references on pp. 34--35 | Pass.  Identity, scan URL, hashes, theorem map, Meyer correction, attribution, reader boundary, pending-review state, and bibliography agree.  The Thatcher--Wright entry is pp. 57--81 with DOI `10.1007/BF01691346`; McNaughton and Thomas remain separately attributed authorities. |
| R25 | `p09-rabin-1969-source-note.md:23--77`; compact record `p09-source-presentations-lot2-3.md:662` | Rabin physical cover; Meyer pp. 477--482 and the official-volume identity | Pass.  Public availability is not called an open-content or republication licence.  The local PDFs and renders are expressly research objects, not handbook assets authorized for redistribution. |
| R28 | `n-c-014.tex:1368--1382`; `p09-rabin-1969-source-note.md:3--21,514--550`; compact record `p09-source-presentations-lot2-3.md:672` | Scope is controlled by the charter; the source pages establish only the historical content | Pass.  Integration and manuscript review are distinguished from admission and every later publication gate.  This report accepts only `N-c-014.d` manuscript content. |

R26 and R27 are not mandatory points for this seat and are not independently
adjudicated here.  The source distinctions relevant to this seat, including
finite/infinite tree, weak/full logic, ordinary/dual acceptance,
decidability/complexity, and source/later route, were nevertheless checked under
R01--R25 and found preserved.

## Cross-record reconciliation

1. **Rabin identity and custody.**  The cover and printed pp. 1 and 35 agree
   with the detailed note, compact record, and `Rabin1969` bibliography entry on
   author, title, journal, volume 141, 1969, pp. 1--35, and DOI.  The EPFL scan
   URL is identical in the detailed note, compact record, and bibliography.
2. **Meyer correction.**  Printed p. 478 states the tower lower bound and
   printed p. 479 lists “the theory of two successors and prefix,” credited to
   Meyer and Stockmeyer.  The reader, detailed note, compact record, and
   `Meyer1975Complexity` entry all preserve the 1974-congress/1975-volume
   distinction and pp. 477--482.
3. **External dependencies.**  Rabin p. 18 invokes McNaughton's equivalence;
   Rabin pp. 34--35 cite Doner and Thatcher--Wright for the weak two-successor
   base.  The reader does not turn either external dependency into Rabin's own
   theorem.  The bibliography gives the McNaughton and published
   Thatcher--Wright identities expected by the frozen records.  Thomas remains
   an explicitly later survey route.
4. **Status and authority.**  The detailed note and compact record both say
   integration is delivered but independent review and admission are pending.
   Nothing in the reader or bibliography inflates that status.
5. **Rights.**  The detailed note's personal/noncommercial-use and
   no-republication-inference language is supported by the Rabin custody cover.
   The Meyer access route is likewise described as research access, not as an
   open licence.

## Relevant limitations

- The charter does not freeze the McNaughton, Thomas, or Thatcher--Wright bodies.
  I therefore checked their bounded use, bibliographic identities, and
  cross-record agreement inside this snapshot, and checked McNaughton's and
  Thatcher--Wright's roles against Rabin's printed invocation/reference pages;
  I did not claim a fresh body-level review of those external works.
- I did not test live URL availability or obtain external DOI metadata.  The
  report establishes agreement among the frozen records and the controlling
  printed Rabin/Meyer pages, not a new web-access audit.
- The detailed note records a layout-extraction hash, but the charter forbids
  reviewers to read that extraction.  I did not access it or rely on it.
- The frozen Meyer object is a complete proceedings volume, but this seat's
  mandated visual scope is the six-page Meyer article, printed pp. 477--482.
  I authenticated the complete PDF by hash and inspected those six article
  pages at original detail; I did not claim to inspect the rest of the volume.
- No manuscript-content acceptance here establishes rendering quality,
  compilation, static checks, human review, or any wider handbook state.

VERDICT: ACCEPT
