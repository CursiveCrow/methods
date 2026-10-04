# Round 3 source-fidelity report: Rabin 1969 / `N-c-014.d`

## Disposition and scope

I reviewed the complete Frozen Round 3 snapshot in the source-fidelity,
evidence, and historical-language seat.  The mandatory scope for this seat is
R01--R25 and R28--R29.  I found no blocker, must-fix, should-fix, consider,
discard, or unresolved-user finding.  The acceptance below is limited to the
frozen `N-c-014.d` manuscript content; it does not admit the rest of
`N-c-014`, Part IX, a rendered page, a build, another part, or the handbook.

## Evidence boundary and review acts

I used only the charter, the six objects in the Frozen Round 3 snapshot, and
the original-detail Rabin and Meyer render sets named by the charter.  I did
not read or use any Round 1 or Round 2 report, another Round 3 report,
`ledger.md`, `transcript/chair.md`, any other board or transcript, the staging
draft, the layout extraction, or conversation/history.  I did not contact
another reviewer.  The source note was treated as an authored claim set, not
as a substitute for the printed sources.

I read the charter and each of the four textual frozen objects completely.  I
recomputed the six Frozen Round 3 SHA-256 identities before the substantive
comparison.  I visually inspected every permitted source render at original
detail.  I performed no test, automated checker, repository script, TeX
command, interim build, handbook-PDF inspection, or build.  No frozen object
was edited.

## Frozen identity results

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact Round 3 match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact Round 3 match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `530EB0B226A239B260938F6BD1A9B247B60A19870F99050D32B879F22639AB23` | exact Round 3 match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact Round 3 match |
| `spec/research/p09-rabin-1969-source-note.md` | `4F5E6D98191DEA62094B88C81DD116809D05B970351CE99C8CE8ECF9C435D215` | exact Round 3 match |
| `spec/research/p09-source-presentations-lot2-3.md` | `DC8B5386F57C829DBAFFDB2CF78575682448762E30880AEAC5D1FD19CA492C93` | exact Round 3 match |

The two PDF sizes recorded in the detailed source note also agree with the
frozen files: 912,831 bytes for the Rabin research copy and 53,151,542 bytes
for the Meyer proceedings volume.

## Printed-source inspection

For Rabin I inspected all 36 files
`tmp/pdfs/p09-rabin-1969/rendered/page-01.jpg` through `page-36.jpg`.
`page-01.jpg` is the JSTOR/AMS custody-and-use cover.  Files `page-02.jpg`
through `page-36.jpg` are, without a gap, printed pp. 1--35.  The inspection
covered the title and introduction; notation and Definition 1.1; valued trees,
tables, ordinary automata, and closure results; both logical translations;
all Chapter II application pages; the sequential-automaton dependency and
Theorem 3.1; the complete marked-tree, well-foundedness, dual-language, and
two-half-step development; the finite-tree construction; the complete
emptiness argument; and the references.

For Meyer I inspected all six files
`tmp/pdfs/p09-rabin-1969/meyer1975-rendered/page-485.png` through
`page-490.png`, corresponding without a gap to printed pp. 477--482.  The
inspection included the article title and proceedings notice on p. 477, the
tower lower-bound statement beginning on p. 478, the p. 479 list item naming
“the theory of two successors and prefix” and crediting Meyer and Stockmeyer,
the remaining discussion, and the p. 482 references.

The Rabin custody cover limits the archived copy to personal,
noncommercial use absent further permission.  The public IMU route supplies
research access to Meyer but prints no open-content grant.  The frozen records
therefore correctly refuse to infer republication or page-image reuse rights
from public access.

## Whole-snapshot source reconciliation

The locations below are line numbers in the frozen textual objects.  Printed
page locators identify the controlling primary evidence; a range is used when
the source construction itself spans several pages.

| Invariant | Frozen manuscript and record locations examined | Controlling printed source | Source-fidelity determination |
|---|---|---|---|
| R01 | reader 914--917; detailed note 129--136, 162--164; compact record 664 | Rabin pp. 3--4 | Pass.  `\Lambda` is retained and any possible editorial `\epsilon` substitution is expressly disclaimed. |
| R02 | reader 918--963; detailed note 127--165; compact record 664 | Rabin pp. 3--5 | Pass.  The two orders are disambiguated without changing their standing; Definition 1.1 has every `0<n\leq\omega`, `T_n=n^*`, all successors and both orders, with the finite-`n` definability and `T_\omega` exception stated at the source's strength. |
| R03 | reader 965--1014; detailed note 167--232; compact record 664 | Rabin pp. 5--7 | Pass.  Arbitrary roots, the distinct table/automaton tuples, a possibly partial move table, one global run, `\exists r\,\forall\pi`, and `F\subseteq\mathcal P(S)` are all exact. |
| R04 | reader 1007--1011, 1140--1187; detailed note 341--398; compact record 664, 668 | Rabin pp. 24--26 | Pass.  The pair sequence belongs only to the dual construction; `\forall r\,\exists\pi` and vacuity in the absence of a rooted run are explicit. |
| R05 | reader 1016--1022, 1092--1097; detailed note 226--232, 271--273; compact record 666 | Rabin pp. 6--10 | Pass.  Union/intersection, projection/cylindrification, complement, and emptiness are assigned to Theorems 1.3--1.6 with their distinct roles in the sentence decision. |
| R06 | reader 1026--1064; detailed note 234--269; compact record 666 | Rabin pp. 7--9, 30--31 | Pass.  The bit-track map is typed and bijective on full-root trees; principal formulas, finite-tree lift, Boolean closure, projection, and complementation remain separate construction steps. |
| R07 | reader 1066--1076; detailed note 284--309; compact record 666 | Rabin pp. 8--9, 30--31 | Pass.  `\exists x(x\in A\land r_0(x)\in B)` correctly instantiates the source's principal-formula route and is unambiguously labelled handbook-worked rather than source-printed. |
| R08 | reader 1078--1097; detailed note 271--282; compact record 666 | Rabin pp. 9--10 | Pass.  The converse state-track encoding uses the one-initial-state normalization and the exact `\exists\bar B\,\forall C` prefix.  The closed sentence is reduced directly to automaton nonemptiness, with no regular-tree basis step inserted. |
| R09 | reader 1099--1138; detailed note 311--339; compact record 668 | Rabin pp. 17--18 | Pass.  The deterministic Muller word automaton, `U\times S`, initial set, common first-coordinate update, and projected designated family match Theorem 3.1.  The branch-coordinate sequence is typed consistently with infinite-occurrence acceptance. |
| R10 | reader 1140--1187; detailed note 341--398; compact record 668 | Rabin pp. 24--26 | Pass.  Type and type-empty conditions, the ordinary/dual quantifier reversal, and the complement role reproduce Definitions 3.5--3.6 without laundering the pair sequence into ordinary acceptance. |
| R11 | reader 1217--1232; detailed note 400--409; compact record 668 | Rabin pp. 19--24 | Pass.  Marking, simultaneous activated runs, same-state merging, and the path check absorbed by Theorem 3.1 all remain visible finite-state components. |
| R12 | reader 1226--1232, 1239--1256, 1295--1302; detailed note 407--425; compact record 668 | Rabin pp. 19--24, 27--30 | Pass.  Well-foundedness is absence of infinite descent, lower strata are stated, and the transfinite loci in Lemmas 3.3 and 3.11 are neither omitted nor substituted for the finite constructions. |
| R13 | reader 1189--1256; detailed note 375--425; compact record 668 | Rabin pp. 25--32 | Pass.  Lemmas 3.7--3.11, same-length transformations, the last-empty-lower-set case, both half-steps, and positive-`k` induction remain distinct after the explicit zero-length normalization. |
| R14 | reader 1258--1282; detailed note 284--306, 497--523; compact record 670 | Rabin pp. 30--31 | Pass.  `frontiered` is defined at first use as a property of `E`, distinguished from predecessor closure by the one-child case, and tied to later uses.  The valuation excludes the frontier; the exact transition codomain is given; and `f\notin S` is consistently an external frontier value, never a state. |
| R15 | reader 1283--1293; detailed note 525--531; compact record 670 | Rabin pp. 30--32 | Pass.  Lemmas 3.12--3.14 have distinct principal-formula, complementation, and compactness functions.  The finite-tree machinery is not said to make the input finite or full monadic logic weak. |
| R16 | reader 1304--1332; detailed note 428--442; compact records 666, 670 | Rabin pp. 32--34 | Pass.  The source's one-letter erasure, complement, conversion to a dual language, and specified membership decision are reconstructed in order; no basis theorem replaces them. |
| R17 | reader 1334--1350; detailed note 442--452; compact record 670 | Rabin pp. 26--29, 32--34 | Pass.  Each recursive question fixes its current table and pair sequence.  The restricted table retains the formal state set and constrains only states strictly below the root, so the root-state boundary is exact. |
| R18 | reader 1352--1370; detailed note 442--452, 465--486; compact record 670 | Rabin pp. 27--29, 33--34 | Pass.  The finite disjoint-stratum termination is stated.  The last-empty-lower-set reduction includes every `H\subseteq U_k`; `H=\varnothing` is the direct shorter question, while the nonempty cases use the restricted table.  The empty branch is expressly a handbook-owned completion of the printed p. 34 nonempty clause. |
| R19 | reader 1372--1388; detailed note 453--486; compact record 670 | Rabin pp. 30--34, especially p. 34 | Pass.  The base permits `m=0`, `U_0=\varnothing`, and the remaining `E_0` no-run obstruction; the K\"onig equivalence and external weak-monadic dependency are stated.  The repair is not passed off as Rabin's printed wording. |
| R20 | reader 949--960, 1391--1395; detailed note 54--92, 149--158, 488--491; compact record 662 | Rabin pp. 1, 4; Meyer pp. 478--479 | Pass.  Rabin's elementary-recursive statement is reported historically and withdrawn as a current bound.  Meyer prints the non-elementary tower lower bound and credits the two-successors-and-prefix case to Meyer and Stockmeyer.  The sublanguage inference withdraws only worst-case complexity, not decidability or effectiveness. |
| R21 | reader 1401--1420; detailed note 533--563; compact record 672 | Rabin pp. 11--17 | Pass.  Linear-order, unary-function, Cantor-space/`F_\sigma`, Boolean-algebra, and game applications are represented at the printed class-level strength, including weak/full distinctions and the Wolfe-theorem boundary. |
| R22 | reader 910--912, 1092--1097, 1113--1138, 1422--1436; detailed note 311--316, 565--625; compact record 672 | Rabin pp. 9--10, 17--18, 19--35 | Pass.  The reconstruction boundary is candid.  McNaughton's theorem is external rather than reproved, and Thomas's later basis route is explicitly separated from Rabin's Section 3.12 proof. |
| R23 | reader 908--1436; detailed note 94--595; compact record 660--672 | Rabin pp. 1--35; Meyer pp. 477--482 | Pass.  A whole-file and whole-article comparison found the cited definition/theorem numbers, locators, symbols, strengths, proof-status qualifications, and attributions consistent with the printed sources. |
| R24 | reader 908--1436; bibliography 2290--2299, 2346--2355, 5938--5947, 5973--5982, 5993--6002; detailed note 31--92, 596--637; compact record 660--672 | Rabin title p. 1 and references p. 35; Meyer title p. 477 and references p. 482 | Pass.  The reader, detailed note, compact record, and bibliography agree on Rabin and Meyer identity, pagination, DOI/URL data, the Meyer correction, the McNaughton/Thomas boundaries, the Thatcher--Wright entry, and the still-pending Round 3 status. |
| R25 | detailed note 31--92; compact record 662; bibliography 5938--5982 | Rabin custody cover; Meyer p. 477 and official proceedings article pp. 477--482 | Pass.  Public access is never inflated into an open-content or republication licence, and local PDFs/renders remain research objects rather than handbook assets. |
| R28 | reader 1422--1436; detailed note 25--29, 596--637; compact record 672 | Rabin pp. 1--35; Meyer pp. 477--482 | Pass.  Status language remains topic- and manuscript-content-specific and pending; it claims no build, visual-layout, human, user, part, or book admission. |
| R29 | reader 1189--1212, 1339--1341; detailed note 375--393, 440--441; compact record 668 | Rabin pp. 25--26, 31--34 | Pass.  The possible zero-length list is acknowledged.  The empty sequence has the no-rooted-run dual semantics, and `\Omega^\dagger=((S,S))` has empty path language and exactly the same dual semantics.  Its standing is an exact handbook-owned bridge into the printed positive-length induction, not a new acceptance condition. |

## Cross-record and historical-language conclusions

The detailed note and compact record do not silently strengthen the reader.
They preserve the same ordinary/dual distinction, arbitrary-root boundary,
finite-tree standing, source-owned versus handbook-owned status, two explicit
p. 34 edge completions, zero-length normalization, Meyer correction,
application classes, and proof boundary.  The bibliography gives the same
Rabin and Meyer identities used by the prose; its Rabin URL and Meyer
proceedings URL agree with the records.  Its relevant McNaughton, Thomas, and
Thatcher--Wright entries do not cause those later or external works to be
projected backward into Rabin's article.

The strongest historical repair is worded correctly: the manuscript does not
say that Rabin lacked an effective decision procedure, nor does it credit the
non-elementary result to Rabin.  It says that Rabin printed an
elementary-recursive qualification, Meyer later printed a tower lower bound,
and Meyer credited the two-successors-and-prefix case to Meyer and
Stockmeyer.  This is exactly what the two permitted printed sources support.

Likewise, the manuscript is transparent about its three handbook-owned edge
repairs.  It does not silently attribute the zero-length normalization,
`H=\varnothing` branch, or `U_0=\varnothing` base branch to the printed
article.  The source's nonempty cases remain present; the added cases are
identified, motivated by the literal dual semantics, and localized to the
points at which printed p. 34 is nonexhaustive.

## Limitations fixed by the charter

The allowed source set does not include the full Thomas, McNaughton, Doner, or
Thatcher--Wright works.  I therefore checked Rabin's own invocation and use of
those external dependencies, the frozen bibliographic identities and
cross-record agreement, and the absence of backward projection; I did not
independently review the external works' proofs or wording.  Similarly, the
detailed note's layout-extraction hash and its descriptions of forbidden
earlier reports were not verified against those excluded objects.  Neither
excluded item controlled any technical or historical determination in this
report.  These are the charter's evidence limits, not unresolved defects in
the frozen Rabin/Meyer reconstruction.

## Findings

None.

VERDICT: ACCEPT
