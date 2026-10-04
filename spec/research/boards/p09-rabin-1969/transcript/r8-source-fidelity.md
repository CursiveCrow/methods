# Round 8 source-fidelity review: Rabin 1969, `N-c-014.d`

## Verdict and exact scope

I accept the frozen Round 8 reconstruction as source-faithful at the level of
`N-c-014.d` manuscript content. I found no blocker, must-fix, should-fix, or
advisory defect, and therefore issue no finding identifier.

This verdict is deliberately narrow. It does not admit all of `N-c-014`, any
other presentation, Part IX, a rendered handbook page, a TeX or repository
build, any executable artifact, human or user acceptance, any other part, or
the book. It also does not convert the source scans or renders into
redistributable handbook assets.

## Independence, evidence boundary, and procedure

I read the charter completely before substantive review. I then used only the
charter, the six objects in the Frozen Round 8 table, and the two render sets
that the charter authorizes. I did not read an earlier-round report, another
Round 8 report, `ledger.md`, `transcript/chair.md`, another board, an unfiled
Round 4 object, a staging draft, a layout extraction, conversation history, or
memory; I did not contact another reviewer or browse the web.

I read the complete textual frozen objects, not merely their Rabin excerpts:

- `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1437;
- `handbook/bib/handbook.bib`, lines 1--6272;
- `spec/research/p09-rabin-1969-source-note.md`, lines 1--665; and
- `spec/research/p09-source-presentations-lot2-3.md`, lines 1--915.

For the two frozen PDFs, I hashed each native file and read every page in the
charter-authorized article scope from the original-detail renders. The Meyer
PDF is a complete proceedings volume, but the authorized review scope within
it is only Meyer's six-page article; I did not treat unrelated proceedings
pages as evidence. I ran no test, automated checker, repository script, TeX
command, interim build, handbook-PDF inspection, or build. Native SHA-256
hashing was used only to establish frozen identity.

The historical assertions that prior reports and hashes are preserved in the
forbidden ledger and chair transcript were not imported as review evidence. I
checked the status language only for agreement among the charter and the
allowed frozen records. Thus this report is independent of every earlier
verdict.

## Frozen identity recomputation

All six native SHA-256 values were recomputed before the substantive audit and
match the charter's Frozen Round 8 table byte for byte.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `4C7FA2AFDCED52E1076F5604A826F5AC148707EE0A4AE1772B31F704259F104A` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `9B679F27B410F8FC65F0193AD0E85B4653C32B306002B9C0F19E2EFBACDC8DB2` | exact match |

## Source pages inspected

I visually inspected every mandated Rabin render at original detail:

`page-01.jpg`, `page-02.jpg`, `page-03.jpg`, `page-04.jpg`, `page-05.jpg`,
`page-06.jpg`, `page-07.jpg`, `page-08.jpg`, `page-09.jpg`, `page-10.jpg`,
`page-11.jpg`, `page-12.jpg`, `page-13.jpg`, `page-14.jpg`, `page-15.jpg`,
`page-16.jpg`, `page-17.jpg`, `page-18.jpg`, `page-19.jpg`, `page-20.jpg`,
`page-21.jpg`, `page-22.jpg`, `page-23.jpg`, `page-24.jpg`, `page-25.jpg`,
`page-26.jpg`, `page-27.jpg`, `page-28.jpg`, `page-29.jpg`, `page-30.jpg`,
`page-31.jpg`, `page-32.jpg`, `page-33.jpg`, `page-34.jpg`, `page-35.jpg`, and
`page-36.jpg`.

Rabin physical page 1 is the JSTOR/AMS custody-and-use cover. Physical pages
2--36 are, individually, printed article pages 1--35. The article pages confirm
the identity and introduction on printed p. 1; notation and Definition 1.1 on
pp. 3--5; ordinary tree automata and Theorems 1.3--1.7 on pp. 5--9; Theorem
1.10 and the decision reduction on pp. 9--10; Chapter II on pp. 10--17;
Theorem 3.1 on pp. 17--19; marked obligations and simultaneous runs on pp.
19--24; Definitions 3.5--3.6 and Lemmas 3.6--3.11 on pp. 24--30; finite-tree
results on pp. 30--32; the emptiness reduction on pp. 32--34; and the closing
base case and references on pp. 34--35.

I also visually inspected every mandated Meyer render at original detail:

`page-485.png`, `page-486.png`, `page-487.png`, `page-488.png`,
`page-489.png`, and `page-490.png`, corresponding individually to printed pp.
477, 478, 479, 480, 481, and 482. Printed p. 477 confirms the article identity
and proceedings copyright; p. 478 begins the tower lower-bound theorem; p. 479
lists “the theory of two successors and prefix” and attributes that case to
Meyer and Stockmeyer; pp. 480--481 give the report's supporting discussion;
and p. 482 contains the references, including Rabin 1969 and the cited
Stockmeyer/Meyer line of work.

## Source identity, attribution, and rights

The Rabin scan and manuscript records agree on Michael O. Rabin,
“Decidability of Second-Order Theories and Automata on Infinite Trees,”
*Transactions of the American Mathematical Society* 141 (1969), printed pp.
1--35. The bibliography gives the same title, journal, volume, pagination,
year, DOI `10.1090/S0002-9947-1969-0246760-1`, and EPFL research-scan URL at
`handbook.bib` lines 5973--5982. The source note gives the same identity and
local custody record at lines 5--16 and 48--69; the compact record agrees at
line 662.

The Meyer article and records agree on Albert R. Meyer, “The Inherent
Computational Complexity of Theories of Ordered Sets,” *Proceedings of the
International Congress of Mathematicians, Vancouver, 1974*, vol. 2 (1975),
printed pp. 477--482. The bibliography records those particulars and the
official IMU URL at lines 5938--5947; the detailed record is at source-note
lines 71--89; the compact record agrees at line 662.

The external dependencies are also bibliographically separated correctly:
McNaughton 1966 at bibliography lines 2290--2299, Thomas 1997 at lines
2346--2355, and Thatcher--Wright 1968 at lines 5993--6002. The last entry has
the exact printed pagination 57--81 and DOI `10.1007/BF01691346`.

Rights language is conservative and source-supported. Rabin physical p. 1
identifies AMS publication and restricts the archived copy to personal,
noncommercial use absent permission; source-note lines 91--97 accordingly
deny an open-content licence and redistribution authority. Meyer printed p.
477 bears the proceedings copyright, and source-note lines 99--102 correctly
say that official public research access does not establish an open-content or
republication licence. No frozen record inflates either access route into
permission to reproduce the scans or page images.

## Invariant-by-invariant source audit

Each result below is based on the printed source pages, with the PDFs—not OCR—
controlling symbols and wording. `Reader` means
`handbook/parts/p09/presentations/n-c-014.tex`; `note` means
`spec/research/p09-rabin-1969-source-note.md`; and `compact` means the
`N-c-014.d` record in `spec/research/p09-source-presentations-lot2-3.md`.

| Invariant | Frozen manuscript evidence and controlling source locator | Result |
|---|---|---|
| R01 | Reader 914--917 retains `\Lambda`; note 146--153 and compact 664 agree. Rabin printed pp. 3--5 use `\Lambda` for the empty word. | PASS |
| R02 | Reader 941--963 states every `0<n\leq\omega`, `T_n=n^*`, all successors and both orders, finite-`n` definability, and the `T_\omega` exception; note 155--177 and compact 664 agree. Rabin printed pp. 3--5 control. | PASS |
| R03 | Reader 965--1014 gives arbitrary roots, the distinct table and automaton tuples, `F\subseteq\mathcal P(S)`, and literal `\exists r\,\forall\pi` acceptance; note 184--241 and compact 664 agree. Rabin printed pp. 5--7 control. | PASS |
| R04 | Reader 1143--1188 gives `\Omega`, the `\forall r\,\exists\pi` dual clause, its complement role, and no-run vacuity; note 359--416 and compact 664, 668 agree. Rabin printed pp. 24--26 control. | PASS |
| R05 | Reader 1016--1023 assigns union/intersection, coordinate projection and unconstrained-coordinate addition, complement, and emptiness to Theorems 1.3--1.6 without an undefined operation label; note 243--250 agrees. Rabin printed pp. 6--7 control. | PASS |
| R06 | Reader 1027--1065 types the full-root bit-track bijection and separates principal formulas, finite-tree lift, Boolean closure, projection, and complement; note 252--287 and compact 666 agree. Rabin printed pp. 7--9 and 30--31 control. | PASS |
| R07 | Reader 1067--1077 gives `\exists x(x\in A\land r_0(x)\in B)`, labels it handbook-owned, and denies that it is a printed Rabin table; note 302--327 agrees, while compact 666 writes the definitionally identical `x0`. Rabin printed pp. 7--9 and 30--31 control the instantiated construction, not the handbook's example itself. | PASS |
| R08 | Reader 1079--1098 gives Lemma 1.2 normalization, finite run tracks, exact `\exists\bar B\,\forall C`, and the sentence-to-nonemptiness reduction with no basis theorem; note 289--300 and compact 666 agree. Rabin printed pp. 9--10 control. | PASS |
| R09 | Reader 1102--1139 types `K:U\times S\to U`, state set `U\times S`, initial set `\{u_0\}\times S`, the common update `K(u,s)`, and designated family by first projection. The finite indexing shift does not change infinite-occurrence acceptance. Note 329--357 and compact 668 agree. Rabin printed pp. 17--19 control. | PASS |
| R10 | Reader 1143--1188 gives the exact type and type-empty formulae, with the range-avoidance clause separate from the infinite-occurrence clause, and gives the exact dual quantifier reversal and complement role; note 361--416 agrees. Rabin printed pp. 24--26 control. | PASS |
| R11 | Reader 1218--1225 and 1235--1254 retains marked trees, simultaneous activation, same-state merging, Theorem 3.1's path check, and both later half-steps; note 418--446 and compact 668 agree. Rabin printed pp. 19--32 control. | PASS |
| R12 | Reader 1215--1233 and 1240--1254 separates the marked-run construction from the mapping `h\mapsto H_h\subseteq H`, defines no infinite descent, gives lower ordinal strata, and identifies Lemmas 3.4 and 3.11 as uses; 1296--1303 prevents the transfinite slogan from replacing the machinery. Note 425--435 and compact 668 explicitly state necessity, standing, nonredundancy, and use at their first substantive mention. Rabin printed pp. 19--32 control. | PASS |
| R13 | Reader 1235--1256 states that Lemma 3.7 preserves length, Lemma 3.8 keeps the same length while making the last lower set empty, Lemmas 3.9--3.10 use the strict prefix, Lemma 3.11 handles arbitrary sequences, and positive-`k` induction follows explicit zero normalization. Rabin printed pp. 25--32 control. | PASS |
| R14 | Reader 1259--1284 defines finite predecessor closure, the frontier, both-child property, the standing and nonredundancy of `frontiered`, valuation off the frontier, exact transition codomain, and external `f\notin S`. The first substantive source-note occurrence at 311--324 and compact 670 supply the same definition and later use. Rabin printed pp. 30--31 control. | PASS |
| R15 | Reader 1285--1294 assigns the lift to Lemma 3.12, principal-formula application to Corollary 3.13, compactness to Lemma 3.14, and complement construction to Corollary 3.15; compact 670 makes the same division. Reader 1397--1400 preserves the infinite/full-versus-finite/weak boundary. Rabin printed pp. 30--32 control. | PASS |
| R16 | Reader 1307--1333 performs one-letter erasure, complement, dual conversion, and the resulting membership question, explicitly denying a basis theorem; note 454--467 and compact 670 agree. Rabin printed pp. 32--34 control. | PASS |
| R17 | Reader 1335--1351 restates the current finite table and current pair sequence and preserves Definition 3.7's formal state set while restricting only nodes strictly below the root; note 468--478 and compact 670 agree. Rabin printed pp. 32--34 control. | PASS |
| R18 | Reader 1353--1371 ranges over every `H\subseteq U_k`, treats `H=\varnothing` as the direct shorter question, uses `R\setminus H` and length `k-1` for nonempty `H`, labels the repair, and terminates the arbitrary half-step by finite disjoint strata. Note 468--478 and 491--512 supplies the same boundary and a concrete counterexample. Rabin printed pp. 33--34, especially display (3.5) and its following reduction, control the inherited nonempty clause. | PASS |
| R19 | Reader 1373--1400 permits `m\geq0`, `U_0=\varnothing`, and `E_0,\ldots,E_m`; at `m=0`, `E_0` has no rooted run, with König equivalence. It labels the repair and the Doner/Thatcher--Wright weak-theory result external. Note 479--512 agrees. Rabin printed pp. 33--35 control the printed nonempty branch and external reference. | PASS |
| R20 | Reader 952--960 and 1392--1396 reports Rabin's elementary-recursive claim only historically, gives Meyer's non-elementary tower lower bound and Meyer/Stockmeyer credit, applies the sublanguage argument, and retains decidability/effectiveness. Note 104--109 and 166--175 and compact 662 agree. Rabin printed pp. 1 and 4 and Meyer printed pp. 478--479 control. | PASS |
| R21 | Reader 1404--1421 gives exact class-level statements for countable linear orders and well-orders, weak all-order corollary, countable unary-function structures and weak arbitrary-domain corollary, the Cantor-space/`F_\sigma` and unit-interval structures, both Boolean-algebra classes, and the encoded game statement. Note 559--589 agrees. Rabin printed pp. 10--17 control. | PASS |
| R22 | Reader 910--912, 1093--1098, 1114--1139, and 1423--1437 distinguishes its reconstruction boundary, Rabin's own nonemptiness proof, McNaughton's external word theorem, and Thomas's later basis route. Note 591--620 and compact 668--672 agree. Rabin printed pp. 9--10, 17--19, and 32--34 control the Rabin roles. | PASS |
| R23 | The numbered results, formulae, quantifier orders, page ranges, notation, historical strength, and attributions checked above agree with every controlling printed page. No theorem role or locator is shifted. | PASS |
| R24 | Reader citations use the bibliography identities at lines 2290--2299, 2346--2355, and 5938--6002. Note 48--109 and 653--665 and compact 662--672 agree on the Rabin/Meyer identities, correction, Rabin scan, Thatcher--Wright role, and Round 8 pending status. Compact 913 likewise says independent Rabin review remains pending. | PASS |
| R25 | Rabin physical p. 1 and Meyer printed p. 477 support the conservative boundary at note 91--102. No reader, compact, or bibliography language claims an open or republication licence. | PASS |
| R26 | The nonstandard names actually used have a local necessity, exact definition or source standing, nonredundancy, and later use: editorial order subscripts at reader 918--927; type/type-empty at 1143--1166; `\Omega^\dagger` at 1190--1213; obligation well-foundedness in the local architecture at 1215--1254 and note 425--435; and `frontiered` plus external `f` at reader 1259--1284, note 302--324, and compact 670. No hypothetical answer is prematurely named. | PASS |
| R27 | The checked text keeps finite and infinite trees, weak and full monadic logic, ordinary and dual acceptance, existence and effectivity, Rabin and later routes, and decidability and complexity distinct. The explicit boundaries at reader 1007--1013, 1182--1188, 1392--1400, and 1423--1437 are source-correct. | PASS |
| R28 | Note 45--46 and 662--665 and compact 672 and 913 all preserve pre-review/pending status and make no broader completion claim. This report's opening scope expressly limits its acceptance to `N-c-014.d` manuscript content. | PASS |
| R29 | Reader 1190--1213 and 1340--1342, note 393--411, and compact 668 state that Lemma 3.6's list may be empty, derive no-rooted-run dual semantics, and prove `\Omega^\dagger=((S,S))` has empty path language and exactly the same dual semantics. The text labels it an exact handbook-owned entry into positive-length induction, not a new acceptance condition. Rabin printed p. 25 and the positive-length development on pp. 31--32 control the gap. | PASS |

## Corrections, proof-role boundaries, and status reconciliation

Three handbook-owned completions are exposed rather than laundered into the
1969 source: the zero-pair normalization (Reader 1190--1213), the
`H=\varnothing` last-lower-set branch (1361--1371), and the `m=0`,
`U_0=\varnothing` base branch (1373--1389). Rabin printed pp. 25 and 34 show
the respective zero-length/positive-induction boundary and printed nonempty
clauses. The reader and both records preserve the printed branches, identify
the added cases as handbook-owned, and give exact semantics. In particular,
the empty `H` branch is the direct shorter dual question, and the empty `U_0`
branch is the finite no-run obstruction supplied by König's Infinity Lemma.
Nothing in the wording falsely attributes these repairs to Rabin.

Likewise, the reader does not silently retain Rabin's obsolete complexity
bound. The elementary-recursive statement remains a historical claim at
Rabin printed pp. 1 and 4; Meyer printed pp. 478--479 supplies the later
non-elementary lower bound and the exact Meyer/Stockmeyer attribution for the
two-successors-and-prefix sublanguage. The conclusion is calibrated: the
worst-case bound is withdrawn, while decidability and effectiveness remain.

All status passages are mutually consistent on the allowed evidence. The
charter states that Rounds 1--7 are closed and Round 4 was withdrawn; note
18--43 and 653--665 and compact 672 state the same history in compatible form.
Note 45--46, note 662--665, compact 672, and compact 913 all say that the
frozen snapshot is pending fresh Round 8 review and is not yet admitted. Those
historical sentences were checked for consistency only; they were not used as
evidence that the present reconstruction is correct.

## Findings

No blocker, must-fix, should-fix, advisory, or other actionable finding was
identified in the frozen Round 8 source/manuscript snapshot.

VERDICT: ACCEPT
