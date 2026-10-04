# Round 4 source-fidelity and evidence review

## Review declaration and evidence set

I independently audited the complete nine-object Round 4 snapshot for the
source-fidelity and evidence mandate. I read all seven textual objects from
beginning to end: the 161-line reader presentation, the 2,394-line shared Part
IX file, the 6,284-line bibliography, the 197-line TATA source note, the
916-line compact record, the 82-line Thatcher--Wright acquisition note, and the
95-line Thomas source note. I used no prior-round report, chair transcript,
ledger, other board, other reviewer report, conversation history, memory, web
result, staging or layout material, or handbook PDF, and I did not contact
another reviewer.

I visually inspected all thirty-two named renders at original detail. The TATA
inspection comprised `core-rendered/page-001.png`, `page-002.png`,
`page-012.png`--`page-014.png`, `page-020.png`--`page-028.png`,
`page-031.png`, `page-041.png`, and `page-044.png`, plus
`relevant-rendered/page-088.png`--`page-097.png`. The Thomas inspection
comprised `inspect-title-01.png`, `inspect-title-02.png`,
`inspect-title-03.png`, `inspect-body-start-04.png`, and
`inspect-body-end-75.png`. Formula, symbol, wording, identity, and pagination
judgments below come from those original-detail pages and the hash-pinned PDFs,
not from text extraction. I ran no test, automated checker, repository script,
TeX command, build, or handbook-PDF inspection.

## Independently recomputed native identities

All nine SHA-256 values match the Round 4 pins exactly.

| Frozen object | Independently recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-tata-2008/tata-2008.pdf` | `3EB9C3F9A1A9A3BD45EC1E50BD50A1C10010789B542A2818F030A7246F9B5B22` | match |
| `handbook/parts/p09/presentations/n-c-015.tex` | `69AC3973E247EF090D9C78E92991BCEEDB30C0145CC276DC2C45F85DE984B4AD` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` | match |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | match |
| `spec/research/p09-tata-2008-source-note.md` | `E8BB8448B3AAA119575EBC6EE16BD79A5F4F50A584875234513A61FC627FA948` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `0A1E5537F20DC16D6421FE6FC21B846180B6548F8AA9B5B6A2CC5942FC0524B3` | match |
| `spec/research/p09-thatcher-wright-1968-acquisition-note.md` | `547821EE7F3B8078C884C2145D4CE4857715F3E2B9775DC57B573098D96C7275` | match |
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | match |
| `spec/research/p09-thomas-1996-report-source-note.md` | `9B06269638D97345123D23434BB9B299EDACF6B1373C9190E92190E3FBE45581` | match |

The two custody lengths recorded in the notes also agree with the pinned local
objects: 2,292,046 bytes for TATA and 478,293 bytes for Thomas.

## Finding register

No blocker, must-fix, should-fix, consider, discard, or unresolved-user finding
is supported. In particular, I found no source mismatch, unread required page,
identity mismatch, silent source repair, stale cross-record status, or
body-dependent Thatcher--Wright claim.

## Mandatory invariant dispositions

- **T01 — PASS (identity and version).** TATA physical page 1 identifies HAL
  `hal-03367725`, a 262-page 2008 work and its public route; physical page 2
  displays the title and the author order Hubert Comon, Max Dauchet, Rémi
  Gilleron, Florent Jacquemard, Denis Lugiez, Christof Löding, Sophie Tison,
  Marc Tommasi; the rendered body footers state 18 November 2008. The reader
  distinguishes the fixed release from the register's evolving-work 2007 label
  at `n-c-015.tex:6-10`; the detailed 263/262-page custody and page map are at
  `p09-tata-2008-source-note.md:16-29,38-50`; the bibliography preserves the
  stable key while giving the inspected release's 2008 date at
  `handbook.bib:5847-5853`; and the compact record agrees at
  `p09-source-presentations-lot2-3.md:694-698`.

- **T02 — PASS (rights).** The HAL cover visibly presents an authorized public
  research deposit, but no Creative Commons or general republication licence.
  The bounded conclusion at `p09-tata-2008-source-note.md:31-34` correctly
  treats the PDF and renders as research evidence rather than handbook assets.

- **T03 — PASS (finite/infinite domain).** TATA printed pp. 11--13 expressly
  limit the monograph to finite trees and say infinite-tree automata are not
  presented. The reader preserves that exclusion at `n-c-015.tex:6-10`, the
  shared definition types finite terms and bottom-up runs at
  `logic-in-computer-science.tex:848-875`, and the shared theorem preserves the
  Rabin nonconflation boundary at `logic-in-computer-science.tex:879-898`.

- **T04 — PASS (ranked terms and tuple).** TATA printed pp. 19--20 support the
  finite ranked ground-term presentation and printed p. 20 gives
  `A=(Q,F,Q_f,Delta)` in exactly that order. The reader reproduces term
  formation, finite ordered-tree standing, tuple order, and the nonconflicting
  `F_TATA -> Sigma`, `Q_f -> F_handbook` map at `n-c-015.tex:12-30`. The shared
  definition's handbook tuple is explicit at
  `logic-in-computer-science.tex:848-870`, and the compact record gives both
  conventions at `p09-source-presentations-lot2-3.md:698`.

- **T05 — PASS (runs and recognition).** TATA printed pp. 20--22 give the
  all-arity ranked transition, including nullary rules, the position-to-state
  bottom-up run, final-root acceptance, and recognizable-language definition.
  The reader states all four without type drift at `n-c-015.tex:20-27`, and the
  shared definition agrees at `logic-in-computer-science.tex:859-870`.

- **T06 — PASS (determinization).** TATA Theorem 1.1.9 and its construction on
  printed pp. 25--27 give same-language determinization, at most one target for
  a fixed symbol/child-state tuple, and the algorithmically reachable subset
  states. The exact bounded claim appears at `n-c-015.tex:39-41` and agrees with
  `p09-tata-2008-source-note.md:67` and
  `p09-source-presentations-lot2-3.md:698`; none claims untranscribed source
  details.

- **T07 — PASS (closure and emptiness).** TATA Theorem 1.3.1 on printed p. 30
  gives union, complementation, and intersection, and Theorem 1.7.4 on printed
  p. 40 makes emptiness linear through accessible-state/least-fixed-point
  marking. The reader correctly initializes at nullary rules, iterates upward,
  and uses “some final state is marked” as the exact nonemptiness criterion at
  `n-c-015.tex:41-46`. The detailed and compact records agree at
  `p09-tata-2008-source-note.md:67-72` and
  `p09-source-presentations-lot2-3.md:698`; no stronger representation claim is
  made.

- **T08 — PASS (small-run ownership).** The rules and unique displayed
  assignment at `n-c-015.tex:32-37` form an accepting run on `f(a,b)` under the
  source semantics of printed pp. 20--22; deleting the sole root rule leaves no
  licensed root state and hence no run. `n-c-015.tex:154-160` expressly labels
  the example handbook-owned, as do `p09-tata-2008-source-note.md:61-65` and
  `p09-source-presentations-lot2-3.md:704`.

- **T09 — PASS (WSkS semantics and restricted atoms).** TATA printed pp. 87--90
  give word-valued first-order variables, finite-word-set monadic variables,
  Proposition 3.3.1, and the exact atoms `X subseteq Y`, `Sing(X)`, `X=Yi`, and
  `X=epsilon`. The reader transcribes their standing and meanings at
  `n-c-015.tex:49-60`; the detailed and compact records agree at
  `p09-tata-2008-source-note.md:82-86` and
  `p09-source-presentations-lot2-3.md:700`.

- **T10 — PASS (finite-set encoding).** Printed pp. 90--91 define the
  `{0,1,bottom}^n` alphabet, make every symbol containing `0` or `1` `k`-ary,
  make `bottom^n` nullary, and display Example 3.3.3. The reader's coordinate
  meanings and labels for `S_1={epsilon,11}`, `S_2=empty`, and
  `S_3={11,22}` at `n-c-015.tex:62-71` agree node for node with Figure 3.7,
  including nullary all-bottom padding rather than an all-zero-track slogan.

- **T11 — PASS (bridge to finite-tree MSO).** TATA printed pp. 89--95 support
  the finite position domain, symbol-label partition/arity clauses, successor
  atoms, and both coded directions. `n-c-015.tex:73-83` explicitly names the
  finite domain `D`, translates label and child atoms, restricts element
  quantifiers to `D` and monadic quantifiers to subsets of `D`, and denies that
  the ambient prefix tree is the automaton's infinite input. The same bridge is
  recorded at `p09-tata-2008-source-note.md:95-102` and
  `p09-source-presentations-lot2-3.md:700`.

- **T12 — PASS (Lemma 3.3.4).** TATA printed pp. 91--93 show the complete
  one-state Figure 3.9 automaton for `X subseteq Y`: `bottom bottom -> q`,
  `00(q,q) -> q`, `01(q,q) -> q`, `11(q,q) -> q`, `bottom 0(q,q) -> q`, and
  `bottom 1(q,q) -> q`. `n-c-015.tex:85-96` transcribes all six and correctly
  describes cylindrification of missing coordinates before union,
  complementation for negation, and projection for existential set
  quantification.

- **T13 — PASS (Lemma 3.3.6).** On TATA printed pp. 94--95 the converse
  quantifies one position set per state, partitions exactly the encoded term
  domain, requires a final state at the root, and uses the implication from a
  node's symbol/state pair to the disjunction of incoming transitions and the
  conjunction of child-state memberships. The formula and child direction at
  `n-c-015.tex:98-110` are literal and correctly typed; the detailed and compact
  summaries at `p09-tata-2008-source-note.md:111-114` and
  `p09-source-presentations-lot2-3.md:702` agree.

- **T14 — PASS (theorem qualification and closed sentences).** TATA printed p.
  95 calls Theorem 3.3.7 “not very precise,” assigns exact force to Lemmas 3.3.4
  and 3.3.6, and reduces a closed sentence to the empty alphabet or the sole
  nullary `top`, accepted exactly via `top -> q_f`. The reader preserves all of
  this at `n-c-015.tex:112-118`; the source note and compact record agree at
  `p09-tata-2008-source-note.md:116-125` and
  `p09-source-presentations-lot2-3.md:700`.

- **T15 — PASS (Exercise 1.4).** TATA printed p. 43 gives precisely the ranked
  alphabet with nullary `a`, binary `f`, and the copying language
  `{f(t,t):t in T(F)}`. The handbook-owned proof at `n-c-015.tex:120-129`
  correctly uses Theorem 1.1.9, first proves that every `t` reaches a state
  because `f(t,t)` must run and be accepted, and then separates distinct terms
  by the crossed pair `f(t,u)`. Ownership is explicit at
  `n-c-015.tex:158-160` and `p09-tata-2008-source-note.md:73-78`.

- **T16 — PASS (weak/full boundary).** Immediately after Theorem 3.3.8 on
  TATA printed pp. 95--96, full SkS permits arbitrary, possibly infinite sets
  and requires top-down automata on infinite inputs plus a different
  complementation argument. `n-c-015.tex:131-139` preserves that boundary. At
  its actual first use, `logic-in-computer-science.tex:884-889` types weak
  variables as finite subsets and full variables as all subsets, limits their
  coincidence to a genuinely finite position domain, and expressly refuses to
  transfer it to the infinite successor tree.

- **T17 — PASS (shared main theorem).** The current shared definition at
  `logic-in-computer-science.tex:848-877` and theorem at
  `logic-in-computer-science.tex:879-898` agree with the reader and TATA printed
  pp. 19--30, 40, and 87--96 on finite ranked inputs, bottom-up runs,
  recognition, finite-tree MSO, effective operations, reachability-based
  emptiness, and the Rabin nonconflation boundary. The Round 4 source-standing
  repair occurs before technical reliance: `logic-in-computer-science.tex:30-33`
  assigns Thatcher--Wright abstract-level historical standing only and assigns
  the operative definitions, constructions, and theorem to TATA.

- **T18 — PASS (proof and reconstruction boundary).** The numbered results and
  locators agree with TATA: Theorem 1.1.9 at printed pp. 25--27, Theorem 1.3.1
  at p. 30, Theorem 1.7.4 at p. 40, Exercise 1.4 at p. 43, Lemma 3.3.4 at pp.
  91--93, Lemma 3.3.6 and Theorems 3.3.7--3.3.8 at pp. 94--95. The reader's
  explicit boundary at `n-c-015.tex:154-160` claims an operative constructive
  reconstruction, not every source table or proof, and separates TATA's
  printed constructions and exercise from the handbook-owned run and proof.
  The source note and compact record agree at
  `p09-tata-2008-source-note.md:136-176` and
  `p09-source-presentations-lot2-3.md:702-706`.

- **T19 — PASS (Thatcher--Wright non-substitution).** TATA printed p. 95 cites
  `[TW68]` for the historical theorem, but the frozen records do not turn that
  citation into access to the 1968 body. `n-c-015.tex:141-152` restricts the
  article to authoritative abstract-level language, with RC-1713 as an
  acquisition lead only. `p09-thatcher-wright-1968-acquisition-note.md:5-34`
  and `:64-82`, `p09-source-presentations-lot2-3.md:684-692`, and
  `p09-tata-2008-source-note.md:187-197` keep the exact signature,
  recognizability relation, language, results, examples, and proof open. The
  owed artifact is stated descriptively and receives no hypothetical technical
  name or imported TATA tuple.

- **T20 — PASS (bibliography and cross-record agreement).** The TATA and
  Thatcher--Wright entries at `handbook.bib:5847-5853,6005-6014` agree with the
  title pages, source notes, reader, compact record, and current source
  standing. The Thomas evidence is also reconciled rather than conflated:
  `handbook.bib:2346-2367` has separate report and chapter entries;
  `logic-in-computer-science.tex:35,2352-2354` relies on
  `Thomas1996Report` and keeps `Thomas1997` a separate version boundary;
  `p09-source-presentations-lot2-3.md:606-616,674-680,909` identifies the
  acquired body as the May 1996 Kiel Bericht 9607 precursor and keeps final
  reconciliation open. Thomas physical page 1 visibly confirms author, title,
  May 1996, Bericht 9607, and Kiel; physical page 2 literally says a modified
  version would be a chapter of the prospective *Handbook of Formal Language
  Theory*. `p09-thomas-1996-report-source-note.md:51-58` preserves that literal
  prospective title separately from the eventual registered *Handbook of
  Formal Languages*, while `:60-68,79-92` limits locators to precursor strength
  and keeps the 1997 body open. Thomas physical pages 3, 4, and 75 confirm the
  contents and direct `4 -> printed 1`, `75 -> printed 72` page map recorded at
  `p09-thomas-1996-report-source-note.md:36-41`.

- **T21 — PASS (terminology rule).** Every technical term used in the TATA
  reader is either source-established and locally typed before reliance
  (`n-c-015.tex:12-30,49-60,62-83`) or a metalinguistic source/ownership
  boundary. No speculative term is assigned to the missing Thatcher--Wright
  body. Its next visit is instead stated as an owed artifact with exact
  evidence requirements at
  `p09-thatcher-wright-1968-acquisition-note.md:64-82` and
  `p09-source-presentations-lot2-3.md:690-692`, satisfying necessity,
  definition/source standing, category, nonredundancy, and use constraints.

- **T22 — PASS (completion scope).** `n-c-015.tex:154-161` says exactly what was
  reconstructed, separates source and handbook ownership, and leaves
  independent topic review open. `p09-tata-2008-source-note.md:10-12,178-185`
  and `p09-source-presentations-lot2-3.md:706` likewise distinguish source
  sufficiency and manuscript integration from review and admission. The
  Thomas and Thatcher--Wright bodies remain separately open at
  `p09-thomas-1996-report-source-note.md:84-92` and
  `p09-thatcher-wright-1968-acquisition-note.md:64-82`. This disposition admits
  only the hash-pinned `N-c-015.b` manuscript content; it says nothing about
  `N-c-015.a`, `N-c-015` overall, Part IX, another presentation, a build,
  rendering, human or user review, the final book, or publication.

## Source-fidelity conclusion

The frozen Round 4 reconstruction is source-faithful at the chartered
manuscript-content scope. Its source identity and custody are pinned; formulas,
transitions, numbered results, page locators, author order, attribution, proof
ownership, weak/full ranges, and finite/infinite boundaries agree with the
controlling pages; Thatcher--Wright remains historical and unacquired rather
than silently reconstructed from TATA; and the Thomas evidence preserves the
literal 1996 prospective-title/final-title distinction. No supported finding
prevents admission of `N-c-015.b` on these nine hashes.

VERDICT: ACCEPT
