# Round 5 adversarial publication and terminology review: Rabin 1969

## Seat, scope, and decision basis

This is the fresh Round 5 **Adversarial publication and terminology** seat for
`N-c-014.d`.  I audited the entire unchanged six-object Round 5 snapshot, not
only the repair described as preceding this round.  The acceptance below is
limited to the manuscript content of `N-c-014.d`; it is not an admission of all
`N-c-014`, Part IX, a rendered handbook page, a build, another part, or the
book, and it is not human or user acceptance.

I used only the following evidence:

1. `spec/research/boards/p09-rabin-1969/charter.md`, read completely;
2. the six objects hash-pinned in the charter's Frozen Round 5 snapshot;
3. the complete Rabin original-detail render set; and
4. the complete Meyer original-detail render set.

I did not read any earlier report, partial or unfiled Round 4 work, another
Round 5 report, `ledger.md`, `transcript/chair.md`, another board or transcript,
the staging draft, the layout extraction, a handbook PDF, or conversation
history.  I did not contact another reviewer.  I ran no test, checker,
repository script, TeX command, interim build, or build.  The PDFs were used as
hash-pinned source identities; the permitted original-detail renders were used
for the page-by-page scholarly reading.

The frozen detailed note and compact record themselves contain generic process
history.  I reviewed that text as part of the frozen claim set for internal
consistency and publication implications; I did not consult the forbidden
reports to validate the history independently.

## Frozen identities independently recomputed

I recomputed each identity with the operating system's native SHA-256 file
hashing facility before substantive review.  Every observed identity exactly
matches the Frozen Round 5 value.

| Frozen object | Charter SHA-256 | Independently observed SHA-256 | Result |
|---|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `78A859CC0069879650417FC27C3E07467D88BA2FB3DDA647574817561A878121` | `78A859CC0069879650417FC27C3E07467D88BA2FB3DDA647574817561A878121` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `E4C3EDA02743632864D1A056B36A6292667C9F1A23DB06AF88057A530C6D893E` | `E4C3EDA02743632864D1A056B36A6292667C9F1A23DB06AF88057A530C6D893E` | exact match |

As a custody cross-check, the two PDF byte lengths are also exactly those
reported by the detailed note: 912,831 bytes for the Rabin research copy and
53,151,542 bytes for the complete Meyer proceedings volume.

## Original-detail visual inspection disclosure

I visually inspected every permitted source render at original detail.

The Rabin files inspected were exactly:

`page-01.jpg`, `page-02.jpg`, `page-03.jpg`, `page-04.jpg`, `page-05.jpg`,
`page-06.jpg`, `page-07.jpg`, `page-08.jpg`, `page-09.jpg`, `page-10.jpg`,
`page-11.jpg`, `page-12.jpg`, `page-13.jpg`, `page-14.jpg`, `page-15.jpg`,
`page-16.jpg`, `page-17.jpg`, `page-18.jpg`, `page-19.jpg`, `page-20.jpg`,
`page-21.jpg`, `page-22.jpg`, `page-23.jpg`, `page-24.jpg`, `page-25.jpg`,
`page-26.jpg`, `page-27.jpg`, `page-28.jpg`, `page-29.jpg`, `page-30.jpg`,
`page-31.jpg`, `page-32.jpg`, `page-33.jpg`, `page-34.jpg`, `page-35.jpg`, and
`page-36.jpg` in `tmp/pdfs/p09-rabin-1969/rendered/`.  Physical page 1 is the
JSTOR/AMS custody-and-use cover.  Physical pages 2--36 are printed Rabin pages
1--35, all inspected.

The Meyer files inspected were exactly `page-485.png`, `page-486.png`,
`page-487.png`, `page-488.png`, `page-489.png`, and `page-490.png` in
`tmp/pdfs/p09-rabin-1969/meyer1975-rendered/`.  They are printed Meyer pages
477--482, all inspected.

The Rabin page read established the formulae, symbols, source numbering, proof
architecture, and printed qualifications used below.  The Meyer page read
established the title and authorship on printed p. 477, the tower lower-bound
theorem beginning on p. 478, and item 5 on p. 479, which names “the theory of
two successors and prefix” and attributes that case to Meyer and Stockmeyer.
No OCR or layout extraction controlled any reading.

## Findings

No blocker, must-fix, should-fix, consider, discard, or unresolved-user finding
survived review.  In particular, I found no undefined or redundant new
technical name, quantifier reversal, vacuity suppression, index-changing
semantic error, frontier-state type error, silent basis theorem, complexity
overstatement, source laundering, rights inflation, cross-record contradiction,
or premature completion implication in the frozen snapshot.

The following sections record the positive basis for that no-finding result.

## Mandatory-invariant audit

### R01--R08: structures, ordinary acceptance, and logical translation

- **R01 — satisfied.**  The reader retains `\Lambda` at
  `handbook/parts/p09/presentations/n-c-014.tex:914-917`; the detailed note
  fixes the same boundary at `spec/research/p09-rabin-1969-source-note.md:133-140`
  and `:166-169`; and the compact record agrees at
  `spec/research/p09-source-presentations-lot2-3.md:664`.  Rabin printed pp. 2
  and 5 visibly use `\Lambda` for the root/empty word.  There is no silent
  `\epsilon` substitution.

- **R02 — satisfied.**  The reader's complete statement is at
  `n-c-014.tex:927-963`, the detailed reconstruction at
  `p09-rabin-1969-source-note.md:131-169`, and the compact statement at
  `p09-source-presentations-lot2-3.md:664`.  Against Rabin printed pp. 4--5,
  Definition 1.1 has exactly `0<n\leq\omega`, `T_n=n^*`, all successors, both
  orders, finite-`n` definability, and the `T_\omega` exception.  The predecessor
  map and both editorial order subscripts are defined before their use and do
  not pretend to be new source relations.

- **R03 — satisfied.**  At `n-c-014.tex:965-1014`, valued trees range over
  arbitrary roots `T_x`; paths, tables, automata, runs, and `In` are separately
  typed; ordinary acceptance is `\exists r\,\forall\pi`; and
  `F\subseteq\mathcal P(S)`.  The detailed note has the same distinctions at
  `p09-rabin-1969-source-note.md:171-237`; the compact record has them at line
  664.  Rabin printed pp. 5--7 control all of these clauses.  The move table is
  not silently totalized, and full-root formula tracks are not mistaken for the
  arbitrary-root language of an automaton.

- **R04 — satisfied.**  The reader defines the finite pair sequence and dual
  acceptance at `n-c-014.tex:1143-1188`; the detailed note does so at
  `p09-rabin-1969-source-note.md:346-403`; and the compact record maintains the
  ordinary/dual separation at lines 664 and 668.  Rabin printed pp. 24--26
  control Definition 3.5, Definition 3.6, and Lemma 3.6.  The pair sequence is
  not used as ordinary `F`, the prefix is `\forall r\,\exists\pi`, and the
  no-run branch is expressly recognized as vacuously true.

- **R05 — satisfied.**  `n-c-014.tex:1016-1023` states Theorems 1.3--1.6 at
  exactly the strength needed: effective union/intersection, deletion of one
  label coordinate, converse addition of a nodewise unconstrained coordinate,
  complementation, and emptiness.  The same direct coordinate description is
  at `p09-rabin-1969-source-note.md:230-237`.  Rabin printed pp. 6--7 control
  these results.  No undefined operation name is interposed.

- **R06 — satisfied.**  `n-c-014.tex:1027-1065` types Definition 1.7's track
  map and says explicitly that it is a bijection on full-root valued trees;
  it then separates normal-form/principal-formula recognition, the finite-tree
  lift, Boolean operations, projection, and complementation.  The detailed note
  agrees at `p09-rabin-1969-source-note.md:239-278`, and the compact record at
  line 666.  Rabin printed pp. 7--9 and 30--31 control the construction and its
  deferred principal-formula case.

- **R07 — satisfied.**  The worked formula occurs at `n-c-014.tex:1067-1077`
  and is explicitly labelled handbook-owned rather than a Rabin transition
  table.  Its complete finite-witness explanation is at
  `p09-rabin-1969-source-note.md:289-314`, and the compact record identifies it
  at line 666.  Rabin printed p. 8 controls the principal-formula shape and
  pp. 30--31 control its finite-tree realization.  The empty suffix and the
  suffix `0` give exactly `\exists x(x\in A\land r_0(x)\in B)`.

- **R08 — satisfied.**  `n-c-014.tex:1079-1098` gives the one-initial-state
  normalization, state-track run encoding, exact `\exists\bar B\,\forall C`
  prefix, and the direct closed-sentence-to-nonemptiness reduction.  The
  detailed note agrees at `p09-rabin-1969-source-note.md:280-287`, and the
  compact record at line 666.  Rabin printed pp. 9--10 control Theorem 1.10,
  Corollary 1.11, and the sentence reduction.  No regular-tree basis step has
  been inserted.

### R09--R15: path product, dual complementation, and finite trees

- **R09 — satisfied.**  At `n-c-014.tex:1102-1139`, the path sequence is typed,
  the chosen word automaton is deterministic Muller with
  `K:U\times S\to U`, the product state set is `U\times S`, the initial set is
  `{u_0}\times S`, the child update is `K(u,s)`, and the designated family uses
  the first-coordinate image.  The detailed note agrees at
  `p09-rabin-1969-source-note.md:316-344`, and the compact record at line 668.
  Rabin printed pp. 17--19 control Theorem 3.1.  Independently tracing a branch
  gives first coordinates `u_0,u_1,\ldots` with
  `u_{n+1}=K(u_n,s_n)`; the apparent one-step shift therefore preserves the
  printed infinite-occurrence acceptance exactly.

- **R10 — satisfied.**  `n-c-014.tex:1143-1188` and
  `p09-rabin-1969-source-note.md:346-378` reproduce Definition 3.5's ordinary
  type and type-empty clauses and Definition 3.6's reversed quantifiers.
  Rabin printed pp. 24--25 control the definitions.  `\operatorname{In}` and
  the whole range are not conflated, and the complement role is explicit.

- **R11 — satisfied.**  The first item at `n-c-014.tex:1218-1225` preserves the
  marked-tree standing, simultaneous activation of runs, same-automaton/
  same-state merging, and Theorem 3.1's path check.  The detailed architecture
  is at `p09-rabin-1969-source-note.md:405-425`, and the compact record at line
  668.  Rabin printed pp. 19--24 and 31--32 control these finite-state steps.
  The account does not replace them with an unqualified transfinite slogan.

- **R12 — satisfied.**  `n-c-014.tex:1227-1233` defines a well-founded mapping
  by absence of an infinite descent and gives the lower-stratum condition;
  `:1296-1303` identifies transfinite induction precisely at Lemma 3.3 and the
  converse of Lemma 3.11.  The detailed note gives the same locus at
  `p09-rabin-1969-source-note.md:405-431`; the compact record agrees at line
  668.  Rabin printed pp. 19 and 28--30 visibly control those two transfinite
  constructions.

- **R13 — satisfied.**  `n-c-014.tex:1235-1256` preserves Lemma 3.7's length,
  Lemma 3.8's same-length last-empty-lower-set output, the shorter
  `\Omega_{k-1}` in Lemmas 3.9--3.10, arbitrary `\Omega` in Lemma 3.11, and
  the two positive-length half-steps after explicit zero-length normalization.
  The detailed account at `p09-rabin-1969-source-note.md:405-425` agrees.
  Rabin printed pp. 25--32 control these lengths and half-steps.

- **R14 — satisfied.**  The exact reader first use of the source adjective is
  `n-c-014.tex:1259-1271`: `Ft(E)` is defined, `frontiered` is defined as a
  property of `E`, predecessor closure is distinguished from the both-children
  condition, and its later need is stated.  The valuation and automaton are
  then typed at `:1272-1283`, with
  `M:S\times\Sigma\to\mathcal P((S\times S)\cup\{(f,f)\})` and `f\notin S`
  expressly an external frontier value.  The detailed note's actual first use
  supplies all five repository-rule elements at
  `p09-rabin-1969-source-note.md:289-314` and repeats the construction at
  `:502-536`; the compact record does so at line 670.  Rabin printed p. 30
  controls the definitions and pp. 30--34 their uses.  No undefined synonym
  or state/frontier conflation remains.

- **R15 — satisfied.**  `n-c-014.tex:1284-1294` separates Lemma 3.12's lift,
  Corollary 3.13's principal-formula role, and Lemma 3.14/Corollary 3.15's
  compactness role.  The detailed note agrees at
  `p09-rabin-1969-source-note.md:530-536`.  Rabin printed pp. 30--32 control
  the distinctions.  Both the reader at `n-c-014.tex:1397-1400` and the note at
  `p09-rabin-1969-source-note.md:533-536` deny the finite/infinite and weak/full
  conflations.

### R16--R20 and R29: emptiness, edge completions, and complexity

- **R16 — satisfied.**  `n-c-014.tex:1305-1333` gives the source's exact chain:
  erase the alphabet to one letter, complement the one-tree language, apply
  Lemma 3.6 to its complement, and decide membership of the unique full tree in
  the resulting dual language.  The detailed reconstruction is at
  `p09-rabin-1969-source-note.md:433-500`; the compact record agrees at line
  670.  Rabin printed pp. 32--34 control the chain.  No basis theorem appears.

- **R17 — satisfied.**  `n-c-014.tex:1335-1351` expressly rebinds the current
  finite table, state set, and current pair sequence before recursion; it also
  states that reductions may change the state set.  Definition 3.7 retains the
  formal state set and restricts only states strictly below the root, so the
  root may be outside the chosen subset.  The detailed note agrees at
  `p09-rabin-1969-source-note.md:447-457`; the compact record at line 670.
  Rabin printed pp. 33--34 control this boundary.

- **R18 — satisfied.**  `n-c-014.tex:1361-1371` ranges over every
  `H\subseteq U_k`, not only the printed nonempty choices.  The empty choice is
  the direct current-root question for `\Omega_{k-1}`; each nonempty choice
  uses the restricted current table and length `k-1`.  The note both states and
  witnesses the repair at `p09-rabin-1969-source-note.md:447-491`; the compact
  record agrees at line 670.  Rabin printed p. 34 controls the defective
  “nonempty” clause, while pp. 27--28 control Lemmas 3.9--3.10.  Independently,
  when `H=\varnothing`, the local obligation says exactly that every rooted run
  already has an `\Omega_{k-1}` path; for nonempty `H`, excluding `H` strictly
  below the root gives Definition 3.7's restricted-table questions.  The added
  branch is therefore necessary and sufficient, not a changed acceptance
  condition.

- **R19 — satisfied.**  `n-c-014.tex:1373-1389` permits `m\geq0`, allows
  `U_0=\varnothing`, uses `E_0,\ldots,E_m`, and explains the `m=0` no-run
  obstruction.  The detailed proof and counterexample are at
  `p09-rabin-1969-source-note.md:458-491`; the compact record agrees at line
  670.  Rabin printed p. 34 controls the defective nonempty base clause;
  printed pp. 30--32 control the finite compactness step.  Independently, for
  `m=0` the required assertion that every finite run reach `U_0` below the root
  can hold only when the finite tree has no rooted run.  Finite branching plus
  König's Infinity Lemma makes the existence of such a finite obstruction
  equivalent to absence of an infinite run.  The weak-monadic theorem is kept
  external and is not confused with full `S2S`.

- **R20 — satisfied.**  Rabin's historical elementary-recursive language is
  reported but withdrawn at `n-c-014.tex:941-960` and `:1392-1400`; the detailed
  note does the same at `p09-rabin-1969-source-note.md:91-96`, `:153-162`, and
  `:493-500`; the compact record agrees at line 662.  Rabin printed pp. 1, 4,
  and 7 visibly make the historical claim.  Meyer printed p. 478 begins a
  lower-bound theorem with a tower whose height grows with input length, and
  printed p. 479 lists the two-successors-and-prefix theory with attribution to
  Meyer and Stockmeyer.  That theory is a sublanguage of the displayed binary
  theory, so a decision procedure for the latter would decide the former.  The
  handbook correctly preserves decidability/effectivity and rejects only the
  worst-case elementary bound.

- **R29 — satisfied.**  `n-c-014.tex:1190-1213` treats the zero-length sequence
  explicitly, proves that its dual language consists exactly of no-run cases,
  defines `\Omega^\dagger=((S,S))`, and proves the same empty path language;
  `:1340-1342` applies the normalization before positive-length recursion.  The
  detailed note agrees at `p09-rabin-1969-source-note.md:380-398`; the compact
  record at line 668.  Rabin printed pp. 25--26 show how Lemma 3.6's list can be
  empty, while printed pp. 31--34 begin only with positive length.  Independently,
  a path map can never have an infinitely recurring set that both meets and
  avoids all of `S`; hence `[\Omega^\dagger]=\varnothing`, exactly as for the
  empty pair sequence.  The normalization is extensionally exact.

### R21--R28: applications, authority, integration, rights, and publication

- **R21 — satisfied.**  `n-c-014.tex:1404-1421` preserves the class-level
  strengths for countable linear orders, weak arbitrary linear orders,
  countable well-orders, countable unary-function structures, weak arbitrary
  unary-function structures, the Cantor-space and unit-interval results, the
  two Boolean-algebra results, and the encoded `F_\sigma` game statement.  The
  detailed map is at `p09-rabin-1969-source-note.md:538-568`; the compact record
  at line 672.  Rabin printed pp. 10--17 control all of these statements.  No
  class is silently strengthened to a result about each arbitrary structure.

- **R22 — satisfied.**  `n-c-014.tex:1423-1437` says exactly what is
  reconstructed, what remains in Rabin's fourteen-page complementation
  development, and why Thomas's later basis route is separate.  The detailed
  boundaries are at `p09-rabin-1969-source-note.md:570-630`; the compact Rabin
  and Thomas records are at `p09-source-presentations-lot2-3.md:672-680`.
  Rabin printed pp. 7--10 and 32--34 show the source's own route, and printed
  pp. 17--19 show the external McNaughton dependency.  Neither McNaughton nor
  Thomas is projected backward as Rabin's proof.

- **R23 — satisfied.**  I checked numbering, notation, locators, strength, and
  attribution across the complete reader reconstruction (`n-c-014.tex:908-1437`),
  the complete detailed note, the compact Rabin record at lines 660--672, the
  relevant bibliography entries, all Rabin printed pp. 1--35, and all Meyer
  printed pp. 477--482.  The symbols and theorem/lemma numbers agree with the
  pages inspected.  The handbook-owned worked example and three edge
  completions are identified as such rather than laundered into Rabin's text.

- **R24 — satisfied.**  The source identity/custody record is at
  `p09-rabin-1969-source-note.md:35-96`; integration and pending status are at
  `:601-643`; the compact record is at
  `p09-source-presentations-lot2-3.md:660-672`.  Bibliographic identities are at
  `handbook/bib/handbook.bib:2290-2299` (McNaughton), `:2346-2355` (Thomas),
  `:5938-5947` (Meyer), `:5973-5982` (Rabin), and `:5993-6002`
  (Thatcher--Wright).  Rabin's cover and printed title page agree on author,
  title, journal, volume 141, July 1969, and pp. 1--35.  Meyer printed pp.
  477--482 agree on author, title, proceedings identity, year/publisher notice,
  pagination, lower-bound wording, and Meyer--Stockmeyer attribution.  The
  Rabin DOI and research-scan URL, Meyer official-volume URL, and
  Thatcher--Wright pagination/DOI are internally consistent across the frozen
  records.  The detailed note and compact record both say Round 5 review is
  required/pending; neither claims admission.

- **R25 — satisfied.**  `p09-rabin-1969-source-note.md:78-89` accurately
  distinguishes access from permission.  Rabin physical p. 1 visibly limits
  the JSTOR archive copy to personal, noncommercial use absent permission and
  directs further-use questions to the publisher.  Meyer printed p. 477 bears
  a 1975 Canadian Mathematical Congress copyright notice.  The note therefore
  does not call either route open content, does not infer a republication
  licence, and identifies PDFs/renders as research objects rather than
  redistributable handbook assets.

- **R26 — satisfied.**  I performed a hostile first-use pass over the complete
  Rabin reader, detailed note, and compact record.  The names that carry special
  theoretical load are defined where introduced: the two editorial order
  subscripts and predecessor map (`n-c-014.tex:918-940`); paths, valued trees,
  tables, automata, runs, and `In` (`:965-1005`); principal formula (`:1048-1061`);
  the path-sequence notation and product projections (`:1102-1135`); type
  `\Omega`, type `\Omega`-empty, and dual acceptance (`:1143-1188`);
  `\Omega^\dagger` (`:1190-1213`); marked-tree standing and well-founded
  mapping (`:1218-1233`); the two half-steps (`:1249-1256`); `Ft(E)`,
  `frontiered`, finite valuation, and external `f` (`:1259-1283`); the current
  restricted table (`:1335-1351`); and the two handbook-owned empty branches
  (`:1361-1389`).  At their first operative uses, each distinction has a
  necessity, exact eliminable definition, standing, nonredundancy explanation,
  and later use.  Generic process history in the note does not pre-name either
  source-specific finite-tree object.  No hypothetical new name is offered in
  place of an owed artifact.

- **R27 — satisfied.**  The reader repeatedly and correctly separates
  arbitrary-root/full-root, finite/infinite tree, weak/full logic,
  ordinary/dual acceptance, existence/effectivity, source/later route, and
  decidability/complexity.  The detailed note's explicit noninterchangeability
  ledger at `p09-rabin-1969-source-note.md:570-599` agrees with the reader and
  compact record.  I found no surviving conflation.

- **R28 — satisfied.**  `p09-rabin-1969-source-note.md:3-33` and `:601-643`
  deny terminal admission, typesetting approval, and user acceptance; the
  compact record at `p09-source-presentations-lot2-3.md:672` says
  `N-c-014.d` remains unadmitted pending the fresh round.  Those statements do
  not imply completion of a build, visual handbook inspection, another topic,
  Part IX, or the book.  This report's own acceptance is expressly limited to
  the unchanged `N-c-014.d` manuscript-content snapshot.

## Adversarial publication synthesis

### Hostile graduate-reader attack

I attempted to read each overloaded symbol as the wrong kind of object.  That
attack fails because the frozen reader keeps the standings explicit:
`F` is a family of recurring-state sets for an ordinary automaton; `\Omega` is
a finite sequence used only by the dual construction; a valued tree is not a
run; a run is one global state labelling, not one run per path; `frontiered` is
a property of `E`; and `f\notin S` is not an ordinary state.  The one-letter
tree is still infinite, and the weak finite-tree theorem appears only as an
external base-case decision theorem.

I also attempted the expected vacuity attacks.  With no rooted run, ordinary
acceptance fails while dual acceptance succeeds.  The empty pair sequence and
`((S,S))` both have empty path language, so both capture exactly that no-run
case.  The printed nonempty `H` clause misses the already-shorter dual branch,
and the printed nonempty `U_0` clause misses the finite no-run obstruction;
the handbook supplies exactly those two branches and no broader semantics.

### Source and later-authority boundary

The reader does not treat the worked principal formula as a printed Rabin
table, the three edge repairs as source wording, McNaughton's word theorem as
proved by Rabin, Thomas's regular-tree-basis route as Rabin's emptiness proof,
or Meyer's complexity result as a replacement for Rabin's definitions.  Each
later or handbook-owned contribution is labelled at the point where it enters.

### Bibliographic and rights attack

The identities agree across the reader citations, detailed note, compact
record, bibliography, and inspected pages.  Public availability is never
equated with an open-content licence.  In particular, the detailed note does
not propose that the local scan or any render be shipped with the handbook.

### Completion-language attack

Statements such as “acquisition and body inspection are complete” and “the
source construction closes Theorem 1.6 effectively” have local, declared
objects: source custody/body inspection and the reconstructed theorem argument.
They are immediately bounded by pending-review and no-terminal-admission
language.  They do not imply a build, rendered-page approval, human review,
topic-family admission, Part IX completion, or book completion.

## Limitations relevant to the verdict

The evidence protocol intentionally excluded external retrieval.  Consequently,
for later bibliography fields not printed in the Rabin or Meyer pages, I could
test frozen-record consistency and, where applicable, Rabin's own reference
list, but I did not independently query publishers.  That is not an unresolved
finding within this charter: the hash-pinned bibliography and records agree,
and the two primary authorities controlling the reconstruction and complexity
correction were read in full.  Likewise, this is manuscript-content review,
not a TeX/build/rendered-handbook review.

VERDICT: ACCEPT
