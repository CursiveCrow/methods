# TATA Round 3 source-fidelity and evidence report

## Disposition

I independently audited the complete nine-object Frozen Round 3 snapshot for
source identity, version, custody, rights, physical-to-printed pagination,
author order, literal formulas and transitions, result numbering, locators,
attribution, proof ownership, cross-record agreement, the repaired
Thatcher--Wright non-substitution boundary, the Thomas 1996-report/1997-chapter
boundary, terminology, and completion scope. I found no blocker, must-fix,
should-fix, consider, discard, or unresolved-user finding.

This acceptance is only an admission recommendation for the frozen
`N-c-015.b` manuscript content. It is not an admission of `N-c-015.a`,
`N-c-015` overall, either Thomas presentation, the Thomas report or registered
chapter, Part IX, a build, a rendered handbook page, human or user review, the
book, or publication.

## Independence and permitted-evidence record

I read the charter completely before judgment. I then read all seven textual
Round 3 objects completely:

| Textual object | Complete extent read |
|---|---:|
| `handbook/parts/p09/presentations/n-c-015.tex` | 161 lines |
| `handbook/parts/p09/logic-in-computer-science.tex` | 2,387 lines |
| `handbook/bib/handbook.bib` | 6,284 lines |
| `spec/research/p09-tata-2008-source-note.md` | 197 lines |
| `spec/research/p09-source-presentations-lot2-3.md` | 916 lines |
| `spec/research/p09-thatcher-wright-1968-acquisition-note.md` | 82 lines |
| `spec/research/p09-thomas-1996-report-source-note.md` | 93 lines |

I did not read any ledger, chair transcript, Round 1 or Round 2 report, another
Round 3 report, another board or board transcript, conversation history,
memory, staging or layout material, handbook PDF, or web result. I did not
contact another reviewer. I ran no test, test harness, automated checker,
repository script, TeX command, build, or handbook-PDF inspection. The only
commands used were native read-only hashing, file/line inspection, and visual
inspection of the charter-named renders.

## Independently recomputed native identities

All nine independently recomputed SHA-256 values equal the Round 3 charter
values exactly:

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-tata-2008/tata-2008.pdf` | `3EB9C3F9A1A9A3BD45EC1E50BD50A1C10010789B542A2818F030A7246F9B5B22` | exact match |
| `handbook/parts/p09/presentations/n-c-015.tex` | `69AC3973E247EF090D9C78E92991BCEEDB30C0145CC276DC2C45F85DE984B4AD` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `392E4123928A4DF4E40099104A85466D326E7DC548D43C36751C381778A9AA47` | exact match |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | exact match |
| `spec/research/p09-tata-2008-source-note.md` | `E8BB8448B3AAA119575EBC6EE16BD79A5F4F50A584875234513A61FC627FA948` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `0A1E5537F20DC16D6421FE6FC21B846180B6548F8AA9B5B6A2CC5942FC0524B3` | exact match |
| `spec/research/p09-thatcher-wright-1968-acquisition-note.md` | `547821EE7F3B8078C884C2145D4CE4857715F3E2B9775DC57B573098D96C7275` | exact match |
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | exact match |
| `spec/research/p09-thomas-1996-report-source-note.md` | `00401B053476E6F776FBBB92321D780E01F4F6F8E6A3FFE96B8DBF7168C557D2` | exact match |

The native byte lengths also agree with the custody notes: 2,292,046 bytes for
the TATA PDF and 478,293 bytes for the controlling Cornell-hosted Thomas PDF.

## Original-detail visual inspection record

I visually inspected all twenty-seven named TATA renders individually at
original detail:

- `core-rendered/page-001.png`, `page-002.png`, `page-012.png` through
  `page-014.png`, `page-020.png` through `page-028.png`, `page-031.png`,
  `page-041.png`, and `page-044.png`;
- `relevant-rendered/page-088.png` through `page-097.png`.

The TATA map is exact: physical page 1 is the HAL cover; physical page 2 is the
internal title page; and each relevant physical page `n+1` is printed page `n`.
The cover identifies the 262-page 2008 monograph, HAL id `hal-03367725`, the
official HAL route, submission on 6 October 2021, all eight authors in title-page
order, and HAL Authorization. The added cover plus the monograph gives 263
physical pages. No Creative Commons or blanket-republication licence appears
on the inspected object. The release footer reads 18 November 2008.

I also visually inspected all five charter-named Thomas renders individually at
original detail:

- `inspect-title-01.png`, `inspect-title-02.png`, `inspect-title-03.png`,
  `inspect-body-start-04.png`, and `inspect-body-end-75.png`.

They establish the exact Thomas map and boundary: physical page 1 is Wolfgang
Thomas's *Languages, Automata, and Logic*, May 1996, Bericht 9607, Kiel title
page; physical page 2 is the abstract saying a modified version would become
the handbook chapter; physical page 3 is contents page `i`; physical page 4 is
printed page 1; and physical page 75 is printed page 72. These pages identify a
complete 1996 report precursor, not a facsimile of the registered 1997 Springer
chapter.

## Literal source, result, and ownership audit

The following literal and result-level comparisons all agree with the
controlling TATA pages:

- TATA printed pp. 20--23 give the finite ranked-term standing, the tuple
  `A=(Q,F,Q_f,Delta)`, nullary and positive-arity transition cases, bottom-up
  runs, final-root acceptance, and recognition. Reader lines 12--30 preserve
  that tuple and give the explicit source-to-handbook map `F` to `Sigma` and
  `Q_f` to handbook `F`; shared lines 845--874 give the equivalent handbook
  tuple without confusing its alphabet and final-set uses of `F`.
- TATA printed pp. 25--27 give Theorem 1.1.9 and the accessible/reachable subset
  construction. Reader lines 39--41 preserve deterministic target uniqueness,
  same-language strength, and reachable subset states.
- TATA printed p. 30 gives Theorem 1.3.1 and its effective Boolean constructions.
  TATA printed p. 40 gives Theorem 1.7.4, accessible-state reduction, the final
  state criterion, and the linear least-fixed-point/Horn implementation.
  Reader lines 41--47 and shared lines 883--888 preserve those roles without
  claiming a stronger representation-independent complexity result.
- Reader lines 32--37 give a correct finite run on `f(a,b)` and the exact
  missing-root-rule failure. Reader lines 154--160 and source-note lines 61--65
  identify that run as handbook-owned; no claim is made that it is printed in
  TATA.
- TATA printed pp. 87--90 give WSkS's word and finite-set domains,
  Proposition 3.3.1, and the four restricted atoms. Reader lines 49--60 preserve
  the domains and the exact atoms `X subseteq Y`, `Sing(X)`, `X=Yi`, and
  `X=epsilon`.
- TATA printed pp. 90--91 give Definition 3.3.2 and Example 3.3.3. Reader lines
  62--71 preserve the `0`, `1`, and `bottom` coordinate meanings; the arity-`k`
  symbols; nullary all-bottom padding; and the exact labels for
  `S_1={epsilon,11}`, `S_2=empty`, and `S_3={11,22}`.
- TATA printed pp. 89--95 support the finite-position-domain bridge. Reader
  lines 73--83 explicitly give `D`, the symbol-label subsets, `x in X_f`,
  `y=xi`, element-quantifier restriction to `D`, monadic-quantifier restriction
  to subsets of `D`, and the distinction between the ambient prefix coding tree
  and the finite automaton input.
- TATA printed pp. 91--93 give Lemma 3.3.4. Reader lines 85--96 reproduce all
  six transitions of Figure 3.9's one-state `X subseteq Y` automaton, including
  nullary `bottom bottom -> q`; preserve the missing-coordinate/cylindrification
  step before union; and use complement and track projection in the printed
  directions.
- TATA printed pp. 94--95 give Lemma 3.3.6. Reader lines 98--110 quantify one
  state-position set per state, partition exactly the encoded finite domain,
  require a final root state, and reproduce the local implication with the
  disjunction over transitions `f(q_1,...,q_s)->q` and the child conditions
  `xi in Y_{q_i}` in the correct direction.
- TATA printed p. 95 gives Theorems 3.3.7 and 3.3.8. Reader lines 112--118 retain
  TATA's “not very precise” qualification and leave the exact directions to
  Lemmas 3.3.4 and 3.3.6. The closed-sentence reduction uses the empty alphabet
  or sole nullary `top` convention and the exact criterion `top -> q_f`; it does
  not substitute an all-zero-track slogan.
- TATA printed p. 43 gives Exercise 1.4 with precisely
  `F={a^(0),f^(2)}` and `{f(t,t):t in T(F)}`. Reader lines 120--129 supply a
  valid deterministic separation proof, including why every term first reaches
  a state and why two distinct terms cannot reach one state. Reader lines
  154--160 mark that proof as handbook-owned rather than source-printed.
- TATA printed pp. 95--96 separate finite-set WSkS from full SkS over arbitrary,
  possibly infinite subsets and state the root-down infinite-input and different
  complementation boundary. Reader lines 131--139 and shared lines 876--890
  retain both the finite-structure coincidence and the Rabin non-substitution.

The numbered-result locators agree everywhere: Theorem 1.1.9 on printed
pp. 25--27, Theorem 1.3.1 on p. 30, Theorem 1.7.4 on p. 40, Exercise 1.4 on
p. 43, Proposition 3.3.1 on pp. 89--90, Lemma 3.3.4 on pp. 91--93, Lemma
3.3.6 on pp. 94--95, and Theorems 3.3.7 and 3.3.8 on p. 95. The source note's
lines 139--142 correctly explain that the matching subsection and result
numbers require no silent repair.

## Historical and adjacent-source boundaries

The Thatcher--Wright boundary is repaired and source-honest. Reader lines
141--152 report only the registered identity, the authoritative abstract's
finite-algebra/closure/generalized-Kleene/positive-second-order scope, and
RC-1713 as an acquisition lead. Lines 154--160 do not transfer a TATA tuple,
logic, example, theorem, or proof. The compact record at lines 684--692 and 910,
the TATA source note at lines 187--197, and the acquisition note at lines 5--7,
27--34, and 64--82 all agree that the technical body is unacquired and that the
owed visit must determine, rather than name, its answer. The shared source-list
citation at `logic-in-computer-science.tex` line 30 makes no body-content claim;
the operative presentation supplies the controlling limitation. TATA printed
p. 95's `[TW68]` citation is not used as a substitute for Thatcher--Wright's
uninspected wording or proof.

The Thomas correction is also exact across records. Bibliography lines
2346--2356 identify `Thomas1996Report` as the May 1996 Kiel Bericht 9607 and
lines 2358--2367 separately register the 1997 Springer chapter. Shared lines
32, 741, and 2341--2347 cite the report for inspected content and use the 1997
entry only for the separate final-version boundary. Compact-record lines
606--616, 674--680, and 909 and Thomas-note lines 5--22, 24--41, 49--66, and
75--90 maintain precursor strength, leave the registered chapter body and
page-by-page reconciliation open, and do not claim Thomas mathematical
admission in this TATA round. The five controlling Thomas renders confirm every
identity and page-map statement used for that correction.

Bibliography lines 5847--5853 preserve the stable `ComonEtAl2007` key while
giving the inspected object's eight-author order, 2008 year, 18 November 2008
release, title, and HAL route. Lines 6005--6014 give the Thatcher--Wright author
order, title, journal, volume, issue, pages, year, and DOI consistently with the
acquisition note. No stale version, status, attribution, ownership, locator, or
rights contradiction remains among the frozen objects.

## Mandatory invariant dispositions

| Item | Disposition and exact evidence |
|---|---|
| **T01** | **Satisfied.** Reader lines 6--10, bibliography lines 5847--5853, source-note lines 14--29 and 147--159, and compact-record lines 694--698 agree with the HAL cover/internal title and printed release footers. Author order, title, HAL route, hash, 18 November 2008, 263/262-page custody, and the evolving-work 2007 label are distinct and exact. |
| **T02** | **Satisfied.** Source-note lines 31--34 match physical page 1's HAL Authorization/public-archive evidence. They claim authorized research access only, state that no Creative Commons licence was observed, and keep the PDF/renders as evidence rather than handbook assets. |
| **T03** | **Satisfied.** Reader lines 6--10 and 131--139 and shared lines 868--872 and 889--890 agree with TATA printed pp. 11--13 and 95--96: operative inputs are finite ranked terms, while infinite-tree automata are excluded and remain distinct from Rabin's devices. |
| **T04** | **Satisfied.** Reader lines 12--30 and shared lines 845--874 agree with TATA printed pp. 19--22 on finite ranked terms, nullary/positive arities, finite ordered trees, the tuple `A=(Q,F,Q_f,Delta)`, and the explicit nonconflicting symbol map. |
| **T05** | **Satisfied.** Reader lines 20--27 and shared lines 856--867 agree with TATA printed pp. 20--23 on the all-arity rule, bottom-up run, final-root acceptance, nullary case, and recognizable-language definition. |
| **T06** | **Satisfied.** Reader lines 39--41 and compact-record line 698 agree with TATA printed pp. 25--27: deterministic means target uniqueness for a fixed symbol/child-state tuple, Theorem 1.1.9 preserves the language, and the operative construction retains reachable subset states. |
| **T07** | **Satisfied.** Reader lines 41--47, shared lines 883--888, and source-note lines 67--72 agree with TATA printed pp. 30 and 40. Boolean closure is effective; the marking route starts at nullary rules; nonemptiness is exactly acquisition of a final marked state; and the linear claim stays within the automaton representation and printed proof boundary. |
| **T08** | **Satisfied.** Reader lines 32--37 give the correct `f(a,b)` run and explain the missing-root-rule failure; lines 154--160 and source-note lines 61--65 expressly mark it handbook-owned. TATA printed pp. 20--23 control the definitions but contain no claimed source instance. |
| **T09** | **Satisfied.** Reader lines 49--60 and source-note lines 82--86 agree with TATA printed pp. 87--90 on word-valued first-order variables, finite-word-set variables, Proposition 3.3.1, and all four restricted atoms. |
| **T10** | **Satisfied.** Reader lines 62--71 and source-note lines 88--93 agree literally with TATA printed pp. 90--91 on arities, all coordinate meanings, Example 3.3.3's sets and labels, and nullary all-bottom padding. |
| **T11** | **Satisfied.** Reader lines 73--83, source-note lines 95--102, and shared lines 876--882 give the exact finite-domain bridge supported by TATA printed pp. 89--95: `D`, label sets, label/child translations, both quantifier restrictions, and the coding-structure/input distinction are explicit. |
| **T12** | **Satisfied.** Reader lines 85--96 and source-note lines 104--109 agree with TATA printed pp. 91--93. Figure 3.9's transition list is complete, and cylindrification, union, complement, and projection occur in the printed roles. |
| **T13** | **Satisfied.** Reader lines 98--110 and source-note lines 111--114 agree with TATA printed pp. 94--95 on one set per state, exact-domain partition, final root, and every connective and direction in the local transition clause. |
| **T14** | **Satisfied.** Reader lines 112--118 and source-note lines 116--125 agree with TATA printed p. 95 on the “not very precise” qualification, the controlling lemmas, and the empty/sole-`top` closed-sentence criterion. |
| **T15** | **Satisfied.** Reader lines 120--129 and 154--160 and source-note lines 73--78 retain TATA printed p. 43's exact alphabet and language, give the required reachability and separation steps, and identify the proof as handbook-owned. |
| **T16** | **Satisfied.** Reader lines 131--139 and source-note lines 127--132 agree with TATA printed pp. 95--96 on full SkS's arbitrary-set domain, root-down automata on infinite inputs, different complementation route, finite-structure coincidence, and nonconversion of the finite automaton input. |
| **T17** | **Satisfied.** Shared lines 845--891 agree with reader lines 12--30, 39--47, 73--83, 112--118, and 131--139 and with TATA printed pp. 19--30, 40, and 87--96. Ranked trees, bottom-up runs, recognition, the MSO correspondence, effective operations, and the Rabin boundary have one consistent strength. |
| **T18** | **Satisfied.** Reader lines 154--160 and source-note lines 57--132 preserve the operative-reconstruction boundary and ownership across TATA printed pp. 25--27, 30, 40, 43, and 91--95. No omitted table or proof is claimed reproduced; the small run and Exercise 1.4 proof are handbook-owned. |
| **T19** | **Satisfied.** Reader lines 141--160, source-note lines 187--197, compact-record lines 684--692 and 910, and acquisition-note lines 5--7, 27--34, and 64--82 agree with the limited `[TW68]` provenance visible on TATA printed p. 95. No TATA object is substituted for the uninspected article body, RC-1713 remains only a lead, and the owed artifact has no hypothetical technical name. |
| **T20** | **Satisfied.** Bibliography lines 2346--2367, 5847--5853, and 6005--6014; reader lines 6--160; shared lines 30--34, 845--900, and 2341--2347; source-note lines 14--197; compact-record lines 606--616, 674--706, and 900--916; and both acquisition/version notes agree with all controlling TATA pages and the five Thomas renders. There is no author, date, numbering, locator, notation, ownership, bibliography, version, or status conflict. |
| **T21** | **Satisfied.** Reader lines 12--30, 49--60, 73--83, 98--110, 131--152 and shared lines 845--891 type the established source terms before operative reliance and give their object/relation/property standing. Reader lines 141--152 and acquisition-note lines 76--82 treat the missing Thatcher--Wright construction as owed evidence rather than naming a speculative answer. These uses agree with TATA printed pp. 20--23 and 87--96. |
| **T22** | **Satisfied.** Reader line 161, source-note lines 10--12 and 178--185, compact-record lines 706, 902, 909--910, and 916, and Thomas-note lines 82--90 keep independent review/admission and unread-source reconciliation open. Acceptance is expressly limited to `N-c-015.b` manuscript content on the nine hashes and implies none of the excluded completion categories. |

VERDICT: ACCEPT
