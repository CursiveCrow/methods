# Round 5 source-fidelity review: Rabin 1969

## Seat, scope, and evidence boundary

This is the fresh Round 5 Source fidelity, evidence, and historical language
review of the unchanged six-object snapshot for presentation N-c-014.d. The
admission scope considered here is manuscript content for N-c-014.d only.
Nothing in this report admits all of N-c-014, Part IX, any rendered page, any
build, another part, or the handbook as a whole; nor does it claim human or
user acceptance.

I read only:

1. spec/research/boards/p09-rabin-1969/charter.md;
2. the six objects in the charter's Frozen Round 5 snapshot;
3. tmp/pdfs/p09-rabin-1969/rendered/page-01.jpg through page-36.jpg; and
4. tmp/pdfs/p09-rabin-1969/meyer1975-rendered/page-485.png through
   page-490.png.

I did not read any earlier report, unfiled Round 4 work, another Round 5
report, ledger.md, transcript/chair.md, another board or transcript, the
staging draft, or the layout extraction. I did not use conversation history as
evidence and did not communicate with another reviewer. I ran no test,
checker, repository script, TeX command, interim build, handbook-PDF
inspection, or build. The detailed source note was treated as an authored
claim set and checked against the printed pages; it was never used in place of
them.

## Frozen identities

Before substantive review I recomputed each SHA-256 identity with native
PowerShell file hashing. I repeated the same native hash check after the
source-page and cross-record audit. Both passes returned the following
unchanged identities.

| Frozen object | Charter SHA-256 | Recomputed SHA-256 | Result |
|---|---|---|---|
| tmp/pdfs/p09-rabin-1969/rabin-1969.pdf | CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3 | CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3 | MATCH |
| tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf | 9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D | 9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D | MATCH |
| handbook/parts/p09/presentations/n-c-014.tex | BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695 | BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695 | MATCH |
| handbook/bib/handbook.bib | 408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0 | 408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0 | MATCH |
| spec/research/p09-rabin-1969-source-note.md | 78A859CC0069879650417FC27C3E07467D88BA2FB3DDA647574817561A878121 | 78A859CC0069879650417FC27C3E07467D88BA2FB3DDA647574817561A878121 | MATCH |
| spec/research/p09-source-presentations-lot2-3.md | E4C3EDA02743632864D1A056B36A6292667C9F1A23DB06AF88057A530C6D893E | E4C3EDA02743632864D1A056B36A6292667C9F1A23DB06AF88057A530C6D893E | MATCH |

The two PDF byte counts also agree with the detailed note: 912,831 bytes for
the Rabin research copy and 53,151,542 bytes for the complete Meyer
proceedings volume.

## Original-detail visual inspection

I visually inspected every authorized render at original detail:

- Rabin physical page page-01.jpg, the JSTOR/AMS custody-and-use cover;
- Rabin physical pages page-02.jpg through page-36.jpg, corresponding exactly
  to printed pp. 1--35; and
- Meyer physical pages page-485.png through page-490.png, corresponding
  exactly to printed pp. 477--482.

Thus the exact Rabin render set inspected was page-01, page-02, page-03,
page-04, page-05, page-06, page-07, page-08, page-09, page-10, page-11,
page-12, page-13, page-14, page-15, page-16, page-17, page-18, page-19,
page-20, page-21, page-22, page-23, page-24, page-25, page-26, page-27,
page-28, page-29, page-30, page-31, page-32, page-33, page-34, page-35, and
page-36. The exact Meyer render set inspected was page-485, page-486,
page-487, page-488, page-489, and page-490.

The Rabin pass included the source's title and custody statement; the
elementary-recursive claims on printed pp. 1, 4, and 7; Definition 1.1 and the
root symbol Lambda on p. 5; arbitrary-root valued trees, tables, runs, and
ordinary acceptance on p. 6; Theorems 1.3--1.7 on pp. 6--9; Theorem 1.10 and
the quantified run encoding on p. 10; all Chapter II application pages
11--17; the deterministic Muller product on p. 18; marked and well-founded
obligations on pp. 19--24; Definitions 3.5--3.6 and Lemmas 3.6--3.11 on
pp. 24--30; finite trees, Lemma 3.12, Corollary 3.13, Lemma 3.14, and
Corollary 3.15 on pp. 30--31; the two half-steps and one-letter emptiness
reduction on pp. 31--34; and the printed references on pp. 34--35.

The Meyer pass confirmed the tower lower-bound theorem beginning on printed
p. 478, and item 5 on printed p. 479: the theory of two successors and prefix,
credited there to Meyer and Stockmeyer. The remaining article pages and
references were also inspected. No Rabin definition or proof architecture was
taken from Meyer.

## Finding

### SF-R5-01

- Severity: must-fix.
- Exact frozen manuscript location:
  spec/research/p09-source-presentations-lot2-3.md:670, in both the clause
  saying that “Lemmas 3.12--3.14” require both children outside the frontier
  and the later sentence saying that “Lemmas 3.12--3.14 use such trees.”
- Controlling printed source: Rabin 1969, printed p. 31 (physical render
  page-32.jpg), read with the finite-tree definition on printed p. 30
  (physical render page-31.jpg).
- Defect: the compact record assigns a frontiered-finite-tree role to Lemma
  3.14. Printed Lemma 3.12 is the finite-initial-tree lift, and Corollary 3.13
  applies that lift to principal formulas. Printed Lemma 3.14 is instead a
  compactness statement about infinite runs: from a set of node--state
  obligations meeting every infinite run, it extracts a finite subfamily. It
  does not take or require a finite tree. Corollary 3.15 is the next result
  that combines Lemma 3.14 with the finite frontiered-tree machinery. The
  compact record therefore obscures the exact distinct role required by R15
  and disagrees with the accurate account at
  handbook/parts/p09/presentations/n-c-014.tex:1288--1291 and
  spec/research/p09-rabin-1969-source-note.md:530--535. This is a
  source-numbering and cross-record fidelity defect under R15, R23, and R24,
  not merely a stylistic compression.
- Minimum sufficient repair: at line 670, replace the two inclusive
  “Lemmas 3.12--3.14” attributions with the exact division of labor: Lemma
  3.12 and Corollary 3.13 use frontiered finite trees for the lift and
  principal-formula case; Lemma 3.14 is the intervening compactness lemma; and
  Corollary 3.15 returns to frontiered finite trees for the complementation
  construction. No change to the frozen reader or detailed note is needed for
  this finding.

No other blocker, must-fix, should-fix, consider, discard, or unresolved-user
finding was found within this seat's evidence and mandate.

## Controlling-invariant disposition

The following records the independent disposition of every invariant assigned
to this seat. R26 and R27 are not assigned to the Source fidelity, evidence,
and historical language seat, so this report does not purport to replace the
seats that control them.

| Invariant | Disposition |
|---|---|
| R01 | PASS. The reader and records retain Rabin's printed root symbol Lambda and expressly reject a silent epsilon substitution. |
| R02 | PASS. Definition 1.1 is given for every 0 < n <= omega, with the word domain, successors, initial-segment order, and lexicographic order; finite-n definability and the T-omega exception match printed p. 5. |
| R03 | PASS. Arbitrary-root valued trees, the table/automaton tuple distinction, the existential-run/universal-path prefix, and F as a family of state subsets match printed p. 6. |
| R04 | PASS. The pair sequence belongs only to dual complementation; the universal-run/existential-path prefix and no-run vacuity are explicit and source-faithful. |
| R05 | PASS. Theorems 1.3--1.6 have the exact closure, coordinate-removal/addition, complement, and emptiness roles. The frozen reader and detailed note describe the converse coordinate operation directly and do not rely on an undefined operation name. |
| R06 | PASS. The full-root bit-track map is typed and bijective, and the principal-formula case, finite-tree lift, Boolean operations, projection, and complementation are separately represented. |
| R07 | PASS. The worked formula with a node in A and its 0-successor in B is explicitly handbook-owned and is not misrepresented as Rabin's printed transition table. |
| R08 | PASS. One-initial-state normalization, the converse state-track encoding, the exists-state-tracks/for-all-path-track prefix, and the direct sentence-to-nonemptiness reduction match printed pp. 9--10. No basis theorem is inserted. |
| R09 | PASS. The deterministic Muller word automaton, transition type, product state and initial sets, shared update, and designated family match printed p. 18. The chosen indexing convention preserves the same infinite-occurrence acceptance. |
| R10 | PASS. The type and type-empty clauses and Definition 3.6's ordinary/dual reversal match printed pp. 24--25. |
| R11 | PASS. Marked obligations, simultaneous activated runs, same-state merging, and Theorem 3.1's path check are retained as finite-state parts of complementation. |
| R12 | PASS. Well-foundedness is absence of infinite descent, the ordinal strata lower every obligation, and transfinite induction is located at Lemmas 3.3 and 3.11 rather than substituted for the finite constructions. |
| R13 | PASS. The exact lengths in Lemmas 3.7--3.11, the last-empty-lower-set half-step, the arbitrary half-step, and positive-length induction remain distinct after the explicit zero-length normalization. |
| R14 | PASS as to the frozen reader and detailed note. The finite predecessor-closed/full-branching definition, first-use standing and nonredundancy of frontiered, valuation domain, exact transition codomain, and external status of f match printed p. 30. SF-R5-01 concerns the compact record's later assignment of result roles, not these definitions themselves. |
| R15 | FAIL: SF-R5-01. The frozen reader and detailed note distinguish the lift, principal-formula, compactness, and complementation roles, but the compact record incorrectly folds Lemma 3.14 into the frontiered-tree results. |
| R16 | PASS. Section 3.12's one-letter erasure, complement, dual conversion, and final membership question are reconstructed without a regular-tree basis substitution. |
| R17 | PASS. Each recursive question fixes its current finite table and pair sequence, and Definition 3.7 keeps the formal state set while restricting states strictly below the root. |
| R18 | PASS. Every H subset of the last upper set is included; the empty branch is the direct shorter question, nonempty branches use the restricted table, and the empty branch is expressly handbook-owned. The finite-state stratum computation terminates for the stated reason. |
| R19 | PASS. The base permits m = 0 and an empty auxiliary set, uses E0 through Em, identifies the finite no-run obstruction at m = 0, preserves the printed nonempty branch, and identifies the weak-theory dependency as external. |
| R20 | PASS. Rabin's elementary-recursive assertion is reported only as a historical source claim. Meyer printed pp. 478--479 supply the non-elementary tower lower bound and exact Meyer--Stockmeyer attribution for the two-successors-and-prefix sublanguage; the inference withdraws the worst-case bound while retaining decidability and effectiveness. |
| R21 | PASS. The class-level strengths for countable linear orders and well-orders, arbitrary weak linear orders, countable unary-function structures and arbitrary weak unary functions, Cantor-space and interval structures, Boolean algebras, and the F-sigma game statement match printed pp. 11--17. |
| R22 | PASS. The reader states both its reconstruction coverage and what remains in the 35-page source. Rabin's use of McNaughton's external word theorem is explicit, while Thomas's later basis route is separately attributed and not projected backward. |
| R23 | FAIL: SF-R5-01. All other checked numbering, locators, notation, strength, and attribution agree with the printed pages, but line 670 misstates the role of printed Lemma 3.14. |
| R24 | FAIL: SF-R5-01. The Meyer correction, Rabin research-scan URL, bibliography identities, Thatcher--Wright pagination and DOI, and pending-review language agree; however, the compact record conflicts with the accurate reader and detailed note over Lemma 3.14's role. |
| R25 | PASS. The JSTOR/AMS cover supports only the stated personal, noncommercial custody boundary absent permission. The records do not inflate public access into an open-content or republication licence, and they keep local PDFs/renders as nonredistributable research objects. |
| R28 | PASS. This review and the frozen status language limit any eventual acceptance to N-c-014.d manuscript content. |
| R29 | PASS. The possible zero-length Lemma 3.6 sequence, its exact no-rooted-run dual semantics, and the handbook-owned one-pair sequence with empty path language are all stated as a normalization into the source's positive-length induction, not as a new acceptance condition. |

## Cross-record, bibliography, and historical-language checks

Except for SF-R5-01, the reader, detailed note, compact record, and relevant
bibliography entries agree on:

- Rabin's title, author, journal, volume 141, 1969 date, pp. 1--35, DOI, and
  complete research-scan URL;
- Meyer's title, ICM Vancouver 1974 proceedings identity, volume 2,
  publication year 1975, printed pp. 477--482, Canadian Mathematical Congress
  publisher, and official proceedings URL;
- the later lower bound's exact location and Meyer--Stockmeyer attribution;
- McNaughton's 1966 article title, journal, volume 9, pp. 521--530, and DOI;
- Thomas's 1997 chapter identity, pp. 389--455, and DOI;
- Thatcher--Wright's 1968 article identity, Mathematical Systems Theory 2(1),
  pp. 57--81, and DOI;
- the separation of Rabin's infinite-tree proof from Thomas's later route and
  from the external finite-tree and word-automaton dependencies;
- the fact that the source scan and proceedings access are research custody,
  not republication permission; and
- the pending Round 5 status and the absence of any premature completion,
  rendered-page, build, human-review, user-acceptance, Part IX, or book-level
  claim.

Because the evidence boundary forbade external sources, I compared the URLs
and bibliographic fields within the frozen records and against the printed
title/reference pages where available; I did not live-resolve any URL. That is
the only material evidence limitation for this seat.

VERDICT: REJECT — SF-R5-01
