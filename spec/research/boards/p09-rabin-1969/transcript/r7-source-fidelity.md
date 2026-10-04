# Round 7 source-fidelity review: Rabin 1969, `N-c-014.d`

## Decision and exact scope

I reject this unchanged Round 7 snapshot because one frozen cross-record
completion-status passage is factually stale.  I found no blocker or must-fix
defect in the reconstruction of Rabin's definitions, formula translations,
automata constructions, theorem roles, source numbering, Chapter II result
strengths, Meyer's later complexity correction, or the rights boundary.  The
single must-fix finding is `R7-SF-01` below.

This decision is limited to the manuscript-content snapshot for
`N-c-014.d`.  It neither rejects Rabin's or Meyer's printed work nor adjudicates
the rest of `N-c-014`, Part IX, any rendered handbook page, any build, any
typesetting result, any other part of the book, human review, user acceptance,
or book completion.

## Independence, evidence boundary, and method

I read `spec/research/boards/p09-rabin-1969/charter.md` completely before
substantive review.  I then used only the six Round 7 frozen objects and the two
original-detail render sets authorized by the charter.  In particular:

- I read the complete 1,437-line `handbook/parts/p09/presentations/n-c-014.tex`,
  including the Rabin reconstruction at lines 908--1437 and both adjacent
  authority boundaries.
- I read the complete 6,272-line `handbook/bib/handbook.bib`; the operative
  entries are McNaughton at lines 2290--2299, Thomas at lines 2346--2355, Meyer
  at lines 5938--5947, Rabin at lines 5973--5982, and Thatcher--Wright at lines
  5993--6002.
- I read the complete 660-line
  `spec/research/p09-rabin-1969-source-note.md` and the complete 915-line
  `spec/research/p09-source-presentations-lot2-3.md`, including the compact
  Rabin record at lines 660--672 and its consolidated status at line 913.
- I independently inspected every authorized Rabin and Meyer image at original
  detail.  The images were reading aids; the hash-pinned PDFs remained the
  controlling source objects.
- I did not read or use any earlier-round report, another Round 7 report,
  `ledger.md`, `transcript/chair.md`, another board, the staging draft, the
  layout extraction, a handbook PDF, conversation history, or memory.  I did
  not contact another reviewer and did not browse the web.
- I ran no test, automated checker, repository script, TeX command, interim
  build, handbook-PDF inspection, or build.  The only identity operation was
  native SHA-256 hashing.  No frozen object was edited.

The permitted printed corpus does not itself print the modern DOI metadata for
every later bibliographic item.  Within this evidence boundary, the DOI and URL
fields were audited for exact agreement among the charter and frozen textual
records; the Rabin scan independently confirms the article's author, title,
journal, volume, date, and printed pagination, and the Meyer pages independently
confirm that article's author, title, proceedings context, year, copyright, and
printed pagination.

## Frozen identities

I recomputed all six hashes before substantive review and rechecked them after
the page and text audit.  Every value matched the Frozen Round 7 table exactly.

| Frozen object | Recomputed native SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `73A700E83218BD1E0460CD836E72FB7EE86914C52D70D865B903CE367400C944` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `0EE7C6EAD01590636652D409EA51FD7A34555F410E3277121B165932A233D41F` | exact match |

## Original-detail page inspection record

Every mandated page was inspected individually.  The complete Rabin mapping
was:

- physical page 01: JSTOR/AMS custody-and-use cover;
- physical 02 = printed 1; physical 03 = printed 2; physical 04 = printed 3;
  physical 05 = printed 4; physical 06 = printed 5; physical 07 = printed 6;
- physical 08 = printed 7; physical 09 = printed 8; physical 10 = printed 9;
  physical 11 = printed 10; physical 12 = printed 11; physical 13 = printed 12;
- physical 14 = printed 13; physical 15 = printed 14; physical 16 = printed 15;
  physical 17 = printed 16; physical 18 = printed 17; physical 19 = printed 18;
- physical 20 = printed 19; physical 21 = printed 20; physical 22 = printed 21;
  physical 23 = printed 22; physical 24 = printed 23; physical 25 = printed 24;
- physical 26 = printed 25; physical 27 = printed 26; physical 28 = printed 27;
  physical 29 = printed 28; physical 30 = printed 29; physical 31 = printed 30;
- physical 32 = printed 31; physical 33 = printed 32; physical 34 = printed 33;
  physical 35 = printed 34; physical 36 = printed 35.

Thus the inspection covered the custody cover and every printed article page
1--35, without a pagination gap.  Physical page 01 identifies Michael O. Rabin,
the article title, *Transactions of the American Mathematical Society* volume
141 (July 1969), pp. 1--35, the AMS as publisher, the JSTOR stable record, and
personal/noncommercial-use restrictions absent further permission.  Physical
page 02 begins printed p. 1; physical page 36 ends printed p. 35 with the
remaining references and affiliations.

The complete Meyer mapping was:

- physical PDF 485 = printed 477;
- physical PDF 486 = printed 478;
- physical PDF 487 = printed 479;
- physical PDF 488 = printed 480;
- physical PDF 489 = printed 481;
- physical PDF 490 = printed 482.

Printed p. 477 gives Albert R. Meyer, the exact article title, the Vancouver
1974 ICM proceedings context, and the 1975 Canadian Mathematical Congress
copyright.  Printed p. 478 begins the tower lower-bound theorem.  Printed p.
479 continues its theorem list and includes item 5, "the theory of two
successors and prefix," attributed there to Meyer and Stockmeyer.  Printed pp.
480--481 continue the complexity comparison and examples; printed p. 482 gives
the remaining references and affiliation.  The six-page article is continuous
and complete at printed pp. 477--482.

## Source identity, pagination, attribution, and rights conclusions

The frozen records agree on Rabin's author, title, journal, volume, year, pp.
1--35, DOI, and EPFL research-scan URL.  The exact textual locators are source
note lines 5--8 and 44--65, compact record line 662, and bibliography lines
5973--5982.  The physical cover and printed p. 1 confirm the printed identity
and the physical-to-printed page map.

The Meyer identity agrees at source note lines 67--85, compact line 662, and
bibliography lines 5938--5947.  The physical/printed mapping 485--490 =
477--482 is exact.  The correction is also exact: Rabin's historical
elementary-recursive statement occurs on printed pp. 1 and 4; Meyer's theorem
begins on printed p. 478, and printed p. 479 expressly includes the
two-successors-and-prefix theory with Meyer--Stockmeyer attribution.  Because
that language is contained in Rabin's displayed binary language, the frozen
reader correctly withdraws the worst-case complexity qualification while
retaining decidability and effectiveness (`n-c-014.tex` lines 941--963 and
1392--1400; source note lines 151--173 and 609--613; compact line 662).

The auxiliary bibliography identities are internally exact and
nonconflated: McNaughton 1966 is at bibliography lines 2290--2299,
Thatcher--Wright 1968 has pp. 57--81 and DOI
`10.1007/BF01691346` at lines 5993--6002, and Thomas 1997 is at lines
2346--2355.  Rabin's own printed p. 18 attributes the external word-automaton
equivalence to McNaughton; printed p. 34 cites Doner and Thatcher--Wright for
the weak finite-tree decision dependency; and the reader explicitly keeps
Thomas's later basis route separate at lines 1432--1437.

The rights boundary is source-faithful.  Source note lines 87--98 do not turn
public research access into an open-content or republication licence and treat
the local PDFs/renders only as research objects.  This matches the JSTOR/AMS
custody terms visible on Rabin physical p. 01 and the copyright notice on Meyer
printed p. 477.  Neither the reader nor compact record claims permission to
redistribute the scans or reproduce the page images.

## R01--R29 audit

### Successor structures, formula translation, and sentence decision

- **R01 -- confirmed.** `n-c-014.tex` lines 914--917 retain Rabin's
  `\Lambda`; source note lines 142--149 and compact line 664 agree.  Rabin
  printed pp. 1 and 5 use `\Lambda` for the empty word/root.  No silent
  `\epsilon` substitution occurs in the Rabin reconstruction.

- **R02 -- confirmed.** Reader lines 918--952 give both distinguished orders,
  every `0<n\leq\omega`, `T_n=n^*`, the typed successors, finite-`n`
  definability, and the `T_\omega` exception.  Source note lines 151--160 and
  compact line 664 agree with Rabin printed pp. 3--5, especially Definition
  1.1 on p. 5.

- **R03 -- confirmed.** Reader lines 965--1014 distinguish arbitrary-root
  valued trees, transition tables, ordinary automata, runs, and the exact
  `\exists r\,\forall\pi` acceptance with
  `F\subseteq\mathcal P(S)`.  Source note lines 180--237 and compact line 664
  agree with Rabin printed pp. 5--7.

- **R04 -- confirmed.** Reader lines 1143--1188 place the finite pair sequence
  in Definitions 3.5--3.6, state the `\forall r\,\exists\pi` dual prefix, and
  explain no-run vacuity.  Source note lines 355--412 and compact lines 664 and
  668 preserve the same distinction.  Rabin printed pp. 24--25 control the
  definitions and the complement role.

- **R05 -- confirmed.** Reader lines 1016--1023 state the exact roles of
  Theorems 1.3--1.6; lines 1062--1065 describe track removal/addition locally,
  and lines 1093--1098 give Rabin's nonemptiness decision.  Source note lines
  239--246 and 271--287 and compact line 666 agree with Rabin printed pp. 6--10
  and 30--34.  No undefined coordinate-operation name replaces Theorem 1.4's
  two directions.

- **R06 -- confirmed.** Reader lines 1027--1065 type the bit-track bijection
  and separately state the principal-formula, finite-tree, Boolean, projection,
  and complement steps.  Source note lines 248--283 and compact line 666 agree
  with Rabin printed pp. 7--9 and 30--31.

- **R07 -- confirmed.** The worked formula is explicitly marked as
  handbook-owned at reader lines 1067--1077 and source note lines 298--323; the
  compact version is at line 666.  Its two-track interpretation faithfully
  instantiates Rabin's principal formula (printed p. 8) and finite-tree lift
  (printed pp. 30--31) without claiming that Rabin printed this transition
  table.

- **R08 -- confirmed.** Reader lines 1016 and 1079--1098 give Lemma 1.2's
  one-state normalization, the run tracks, the exact
  `\exists\bar B\,\forall C` prefix, and the closed-sentence-to-nonemptiness
  reduction.  Source note lines 239 and 289--296 and compact line 666 agree with
  Rabin printed pp. 6 and 9--10.  No basis theorem is inserted.

### Product, complementation, finite trees, and emptiness

- **R09 -- confirmed.** Reader lines 1102--1139 give the deterministic Muller
  word automaton, `K:U\times S\to U`, product state set `U\times S`, initial set
  `{u_0}\times S`, common update `K(u,s)`, and designated family.  Source note
  lines 325--353 and compact line 668 agree.  Rabin printed pp. 17--18 control
  the sequential convention and Theorem 3.1; the one-symbol indexing offset is
  harmless for the printed infinite-occurrence condition.

- **R10 -- confirmed.** Reader lines 1143--1188 exactly preserve the type and
  type-empty predicates, the ordinary/dual reversal, and complement role.
  Source note lines 355--412 and compact line 668 agree with Rabin printed pp.
  24--25.

- **R11 -- confirmed.** Reader lines 1218--1225 and 1235--1254 retain marked
  obligations, activated-copy simulation, same-state merging, the Theorem 3.1
  path check, and both dual half-steps.  Source note lines 416--442 and compact
  line 668 agree with Rabin printed pp. 17--24 and 27--32.

- **R12 -- confirmed.** At reader lines 1227--1233, the nonempty-set mapping
  `h\mapsto H_h\subseteq H` is called well founded exactly when it has no
  infinite dependency sequence; its standing, distinction from path acceptance
  and merging, ordinal characterization, and later Lemmas 3.4/3.11 uses are
  explicit through lines 1240--1254 and 1296--1303.  The detailed note's first
  substantive use at lines 421--431 and compact line 668 supply the same exact
  definition and role.  Rabin printed pp. 19--24 and 27--30 control these
  claims.

- **R13 -- confirmed.** Reader lines 1235--1256 preserve the sequence-length
  roles of Lemmas 3.7--3.11, distinguish the last-lower-set-empty and arbitrary
  half-steps, and enter induction only after the explicit zero-length
  normalization.  Source note lines 432--442 and compact line 668 agree with
  Rabin printed pp. 25--32.

- **R14 -- confirmed.** Reader lines 1259--1283 give finite predecessor closure,
  the exact frontier, the additional two-child property named `frontiered`, its
  standing as a property of `E`, its nonredundancy and use, valuation away from
  the frontier, the exact transition codomain, and `f\notin S` as an external
  frontier value.  The detailed note first defines the term at lines 307--320
  and restates the construction at lines 519--545; compact line 670 agrees.
  Rabin printed p. 30 controls the definition.

- **R15 -- confirmed.** Reader lines 1284--1294, source note lines 547--553,
  and compact line 670 keep distinct the Lemma 3.12 lift, Corollary 3.13
  principal-formula application, Lemma 3.14 compactness result, and Corollary
  3.15 return to frontiered-tree machinery.  This is exact against Rabin
  printed pp. 30--31 and does not convert the infinite input/full theory into a
  finite input/weak theory.

- **R16 -- confirmed.** Reader lines 1305--1333 and source note lines 450--463
  give Rabin's alphabet erasure, one-tree language, complement, dual-language
  conversion, and membership decision.  Compact line 670 agrees with Rabin
  printed pp. 32--34.  No regular-tree basis theorem is substituted.

- **R17 -- confirmed.** Reader lines 1335--1351 specify the current table and
  pair sequence at every recursive question and preserve Definition 3.7's
  formal state set/root boundary.  Source note lines 464--474 and compact line
  670 agree with Rabin printed pp. 33--34.

- **R18 -- confirmed.** Reader lines 1353--1371 range over every
  `H\subseteq U_k`, distinguish the empty direct-shorter branch from nonempty
  restricted-table branches, identify the completion as handbook-owned, and
  give the finite-stratum termination.  Source note lines 464--474 and
  487--508 and compact line 670 agree.  Rabin printed pp. 33--34, especially
  displays (3.5)--(3.6), control the preserved source clause and expose the
  printed nonempty omission.

- **R19 -- confirmed.** Reader lines 1373--1389 allow `m\geq0`, empty `U_0`,
  and the sole no-run tree `E_0` when `m=0`, while keeping the printed nonempty
  branch and attributing the weak-theory dependency externally.  Source note
  lines 475--485 and 487--508 and compact line 670 agree with Rabin printed p.
  34.  The no-infinite-run equivalence is correctly tied to Koenig compactness.

### History, application strength, records, rights, terminology, and scope

- **R20 -- confirmed.** Reader lines 952--960 and 1392--1396, source note lines
  162--171 and 609--613, and compact line 662 treat Rabin's
  elementary-recursive statement only as a historical source claim.  Rabin
  printed pp. 1 and 4 and Meyer printed pp. 478--479 support the correction,
  exact attribution, sublanguage consequence, and preservation of decidability
  and effectiveness.

- **R21 -- confirmed.** Reader lines 1404--1421, source note lines 555--585,
  and compact line 672 preserve the class-level distinctions among countable
  linear orders, weak arbitrary linear orders, countable unary-function
  structures, weak arbitrary unary functions, the specified Cantor-space and
  Boolean-algebra structures, and the encoded game statement.  Rabin printed
  pp. 11--17 control these application claims.

- **R22 -- confirmed.** Reader lines 910--912 and 1423--1437 explicitly state
  what is reconstructed, what remains in Rabin's full article, McNaughton's
  external word-theorem role, and Thomas's later separate basis route.  Source
  note lines 582--617 and compact line 672 agree.  Rabin printed p. 3 gives the
  article's chapter plan, pp. 11--17 contain the applications, p. 18 invokes
  McNaughton, and the article ends at p. 35; nothing in the reader projects the
  later Thomas route backward.

- **R23 -- confirmed.** The detailed page map at source note lines 107--138
  agrees with every inspected printed page.  The reader's numbered definitions,
  theorems, lemmas, corollaries, formula numbers, notation, strengths, and
  attributions agree with the printed locators stated above.  I found no silent
  renumbering, source/later-source substitution, or theorem-role reassignment.

- **R24 -- not fully satisfied.** The source identities, Meyer correction,
  Rabin scan URL, Thatcher--Wright pp. 57--81 and DOI, and nonterminal status
  language at source note lines 18--42 and compact lines 672 and 913 agree.
  Bibliography lines 2290--2299, 2346--2355, 5938--5947, 5973--5982, and
  5993--6002 are internally exact.  However, source note lines 618 and 649--660
  contain a contradictory pre-Round-6 status remnant.  This is finding
  `R7-SF-01`.

- **R25 -- confirmed.** Source note lines 87--98 accurately preserve the
  restrictive custody/rights boundary visible on Rabin physical p. 01 and the
  copyright boundary visible on Meyer printed p. 477.  No frozen reader or
  compact claim launders public access into an open-content or republication
  licence.

- **R26 -- confirmed.** The technical names material to this reconstruction are
  defined at first substantive use with standing and later role: the editorial
  order disambiguations at reader lines 918--927, the pair-sequence predicates
  at 1143--1166, the handbook-owned zero-length representative with necessity
  and equivalence at 1190--1213, the well-founded obligation mapping at
  1227--1233, and `frontiered` at 1259--1283.  The corresponding first uses in
  the detailed note are lines 298--320, 355--407, and 421--431; compact lines
  668 and 670 give the necessary local definitions.  No hypothetical primitive
  is named in place of an owed artifact.

- **R27 -- confirmed.** The reader keeps finite/infinite trees, weak/full
  monadic logic, ordinary/dual acceptance, existence/effectivity,
  source/later-source routes, and decidability/complexity distinct at lines
  1007--1013, 1182--1213, 1268--1283, 1392--1400, and 1423--1437.  The detailed
  note and compact record preserve the same boundaries.  No listed conflation
  survives.

- **R28 -- confirmed as a scope boundary, despite the rejection.** Source note
  lines 5 and 41--42 and compact line 672 limit the claim to `N-c-014.d` and
  deny terminal admission/user acceptance.  The present verdict is likewise
  limited to this frozen manuscript-content snapshot and makes none of the
  excluded completion claims.

- **R29 -- confirmed.** Reader lines 1190--1213 derive the zero-length dual
  semantics and prove `\Omega^\dagger=((S,S))` equivalent, then use it at lines
  1340--1342.  Source note lines 389--407 and 460--463 and compact line 668
  agree.  Rabin printed p. 25 supplies Lemma 3.6's potentially empty
  enumeration, while printed pp. 27--32 begin and use the positive-length
  induction.  The reader labels the one-pair representation as handbook-owned
  and does not introduce a new acceptance condition.

## Finding

### `R7-SF-01` -- must-fix -- stale pre-Round-6 status survives inside the Round 7 source note

**Frozen manuscript locators.**
`spec/research/p09-rabin-1969-source-note.md:618` labels its last section
"Reader-facing integration repaired after Rounds 1--4."  Lines 649--651 list
only Rounds 1, 2, 3, and 5 plus the Round 4 withdrawal.  Most decisively, lines
657--660 say that the objects must be newly frozen "before three fresh Round 6
reviews begin."

Those statements contradict the same frozen note at lines 18--39, which says
Rounds 5--6 are closed, records the Round 6 dispositions, and requires a fresh
Round 7.  They also contradict the compact record at line 672, which gives the
Round 6 outcome and says a newly frozen Round 7 remains required, and its
consolidated line 913, which says independent scholarly review remains pending.
The controlling Round 7 charter likewise fixes Round 7 at lines 155--175 and
its filing rule at lines 463--484.

**Printed-source locator and evidence status.** This is a metalinguistic board
status defect, so no Rabin or Meyer printed page can truthfully control the
round number.  I checked the terminal source pages, Rabin printed p. 35 and
Meyer printed p. 482: they contain references/affiliation, not campaign status.
The complete printed bodies to which the status attaches are Rabin pp. 1--35
and Meyer pp. 477--482, all inspected.  The controlling evidence for the
procedural fact is therefore the Round 7 charter and the contradictory frozen
record locators just stated; assigning an invented printed-page authority would
be source laundering.

**Defect and effect.** The broad claim "not admitted" remains true, so this is
not a false terminal-admission claim.  The exact audit provenance and next
review round are nevertheless false in one frozen section.  That defeats R24's
required cross-record agreement and makes the detailed source record internally
inconsistent about completion status.

**Minimum sufficient repair.** Rewrite the heading at line 618 and the status
paragraph at lines 649--660 so that they agree with the note's lines 18--42 and
the compact record's lines 672 and 913.  The repair must include the Round 6
disposition, must remove the prospective "before Round 6" statement, and must
continue to deny terminal admission.  A round-neutral prospective sentence
such as "admission requires three fresh independent ACCEPT verdicts on one
unchanged newly frozen snapshot" would avoid recreating this stale-round defect;
if individual rounds remain enumerated, the history must be updated through the
round completed when the replacement snapshot is frozen.  Because this is a
frozen-object content edit, the replacement must receive new hashes and a fresh
blind round under the charter.

No other blocker, must-fix, should-fix, consider, discard, or unresolved-user
finding is filed from this seat.

VERDICT: REJECT — R7-SF-01
