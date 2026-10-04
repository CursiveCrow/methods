# TATA Round 3 adversarial publication and terminology report

## Seat, independence, and evidentiary scope

This is the fresh Round 3 adversarial-publication-and-terminology review of the frozen `N-c-015.b` snapshot. I read the charter completely before reviewing the evidence. I then read all seven permitted textual objects completely, independently recomputed the SHA-256 of all nine frozen objects, and visually inspected every one of the twenty-seven named TATA renders and five named Thomas identity/page-map renders at original detail.

I did not read a Round 1 or Round 2 report, another Round 3 report, `ledger.md`, `transcript/chair.md`, another board or board transcript, conversation history, memory, staging or layout material, a handbook PDF, or web results. I did not contact another reviewer. I ran no test, test harness, automated checker, repository script, TeX command, build, or handbook-PDF inspection. The only machine operations were native read-only hashing and direct source/page inspection. I edited only this assigned report.

The decision here is limited to whether the frozen TATA reconstruction for `N-c-015.b` may be admitted at manuscript-content level. It does not decide `N-c-015.a`, `N-c-015` overall, Part IX, the Thomas presentations, a build, any rendered handbook page, visual completion of the handbook, human or user review, the book, or publication.

## Independent hash recomputation

All nine recomputed hashes exactly match the charter.

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

## Complete-reading and original-detail page record

The seven complete textual reads were:

1. `handbook/parts/p09/presentations/n-c-015.tex`, lines 1--161;
2. `handbook/parts/p09/logic-in-computer-science.tex`, lines 1--2387;
3. `handbook/bib/handbook.bib`, lines 1--6284;
4. `spec/research/p09-tata-2008-source-note.md`, lines 1--197;
5. `spec/research/p09-source-presentations-lot2-3.md`, lines 1--916;
6. `spec/research/p09-thatcher-wright-1968-acquisition-note.md`, lines 1--82; and
7. `spec/research/p09-thomas-1996-report-source-note.md`, lines 1--93.

The twenty-seven TATA images inspected at original detail were:

- `core-rendered/page-001.png`, `page-002.png`, `page-012.png`, `page-013.png`, `page-014.png`, `page-020.png`, `page-021.png`, `page-022.png`, `page-023.png`, `page-024.png`, `page-025.png`, `page-026.png`, `page-027.png`, `page-028.png`, `page-031.png`, `page-041.png`, and `page-044.png`;
- `relevant-rendered/page-088.png`, `page-089.png`, `page-090.png`, `page-091.png`, `page-092.png`, `page-093.png`, `page-094.png`, `page-095.png`, `page-096.png`, and `page-097.png`.

Those images establish the HAL custody cover; internal title and title-page author order; 18 November 2008 footer; printed introduction pp. 11--13; printed Chapter 1 and section 1.1 pp. 19--27; printed pp. 30, 40, and 43; and the complete printed section 3.3 passage on pp. 87--96. Formula and symbol comparisons below use the printed pages rather than relying on prose extraction.

The five Thomas images inspected at original detail were `inspect-title-01.png`, `inspect-title-02.png`, `inspect-title-03.png`, `inspect-body-start-04.png`, and `inspect-body-end-75.png`. They establish that the frozen file is Wolfgang Thomas's May 1996 Kiel Bericht 9607, not an inspected 1997 chapter: physical page 1 is its title page, physical page 2 says a modified version would become the handbook chapter, physical page 3 is contents page `i`, physical page 4 is printed p. 1, and physical page 75 is printed p. 72.

## Adversarial recomputation of the reconstructed boundaries

### Finite versus infinite and weak versus full

TATA's printed introduction pp. 11--13 explicitly limits the monograph to finite trees and excludes infinite-tree automata. Printed pp. 20--22 define bottom-up automata on finite ranked ground terms. Printed p. 88 gives WSkS its finite-set semantics and distinguishes SkS by allowing infinite sets; printed pp. 95--96 again distinguish the weak finite-set construction from arbitrary-set full SkS and say the latter requires root-down automata on infinite inputs and a different complement construction. The reader's substantive account at `n-c-015.tex:6--10,49--60,131--139` preserves those distinctions. The shared theorem's finite-structure assertion is mathematically sound: on the finite position domain of one finite tree, every subset is finite. That fact does not identify a bottom-up finite-tree automaton with a Rabin automaton on an infinite tree.

The publication order nevertheless fails at the shared theorem's actual first use of the weak/full terminology; that is finding `TATA-R3-AP-01` below.

### TATA tuple, runs, and finite constructions

Printed p. 20 gives the literal source tuple `A=(Q,F,Q_f,Delta)`, including the ranked alphabet and final states before transitions. Printed pp. 20--22 supply the all-arity transition and run definitions, including nullary rules and final-root acceptance. The reader keeps this tuple at `n-c-015.tex:12--30` and explicitly maps source `F` to handbook `Sigma` and source `Q_f` to handbook `F`; the shared definition's alternate display order is therefore not silently attributed to TATA.

Printed pp. 25--27 establish same-language subset determinization and the accessible-state implementation. Printed p. 30 establishes Boolean closure. Printed p. 40 reduces nonemptiness to an accessible final state and identifies the linear least-fixed-point/Horn implementation boundary. Partial transition tables do not undermine the reconstruction: a term may have no run, deterministic means at most one target for a fixed symbol and child-state tuple, and completeness is not assumed. The reader's `f(a,b)` example is correct and explicitly handbook-owned; without its root transition the leaves have states but the ground term has no run.

### WSkS coding, both logical directions, and closed sentences

Printed pp. 87--90 establish word individuals, finite-set variables, Proposition 3.3.1, and the four restricted atoms. Printed pp. 90--91 establish the finite tree encoding over `{0,1,bottom}^n`. I recomputed Example 3.3.3: the root, positions `1`, `2`, `11`, and `22`, and every remaining nullary padding node have exactly the labels listed at `n-c-015.tex:62--71`. In particular, bottom padding is not an all-zero track.

The finite-tree MSO bridge at `n-c-015.tex:73--83` is correctly typed: the domain `D` is the finite position set of the encoded tree, label sets are subsets of `D`, child atoms use the appropriate successor, element quantifiers are restricted to `D`, and monadic quantifiers are restricted to subsets of `D`. The ambient prefix tree supplies codes; it is not the automaton's input.

Printed pp. 91--93 confirm the complete one-state transition list for inclusion and the induction operations: add missing coordinates before union for disjunction, complement for negation, and track projection for existential set quantification. Printed pp. 94--95 confirm the converse formula: one set per state, a partition of the encoded finite domain, a final state at the root, and a local parent-state implication whose disjunction ranges over transitions into that state and whose conjuncts assign the corresponding child states. Nullary transitions survive as empty child conjunctions. Printed p. 95 also calls Theorem 3.3.7 not very precise and makes the two lemmas controlling; the frozen reader preserves that qualification. For a closed sentence, printed p. 95 uses an empty alphabet or the sole nullary constant `top`, and validity reduces to a transition `top -> q_f` for a final state.

### Exercise 1.4

Printed p. 43 fixes exactly one nullary symbol `a` and one binary symbol `f` and asks for nonrecognizability of `{f(t,t):t in T(F)}`. The handbook-owned proof at `n-c-015.tex:120--129` is valid even for an initially partial deterministic automaton. Acceptance of every `f(t,t)` forces each `t` to have a run and hence reach a state. If distinct `t` and `u` reached one state, the transition accepting `f(t,t)` would also accept `f(t,u)`. Finiteness of the state set then contradicts the infinitely many ground terms.

### Source, ownership, access, and version boundaries

The TATA title, author order, HAL route, complete-object extent, hash, and release date agree across the frozen PDF, bibliography, reader, detailed note, and compact record. The HAL cover demonstrates authorized deposit/access, not a Creative Commons or blanket republication licence; all frozen records keep the PDF and renders as research evidence rather than handbook assets. The small run and Exercise 1.4 proof are handbook-owned, while source statements, source exercises, and operative outlines are not mislabelled as fully reproduced source proofs.

The Thomas evidence is also correctly corrected across the bibliography, main text, compact record, and source note: the acquired body is the May 1996 report precursor, while the registered 1997 chapter body, page-by-page reconciliation, independent precursor review, and admission remain open.

The Thatcher--Wright detailed and compact records correctly keep the technical body unavailable, limit present evidence to article identity and abstract-level scope, keep RC-1713 as an acquisition lead, and state the owed artifacts without naming a hypothetical construction. The chapter-level source-standing sentence does not preserve that same boundary at its own location; that is finding `TATA-R3-AP-02` below.

## Five-part terminology audit at actual first use

The new local mathematical vocabulary in the reader is generally introduced correctly. `n-c-015.tex:12--30` defines the finite ranked alphabet, ground terms, finite ordered tree standing, source tuple, run, acceptance, recognizability, and source-to-handbook map before reliance. Lines 49--60 define WSkS's two variable domains and the restricted atoms before use. Lines 62--83 define the encoding and finite-domain standing before the two logical directions rely on it. Lines 131--139 define full SkS by its arbitrary-set domain, distinguish it from WSkS and finite-tree automata, and immediately use the distinction. The shared finite-tree definition at `logic-in-computer-science.tex:845--874` supplies exact objects and relations, explains necessity, distinguishes them from word and Rabin automata, and identifies the later theorem that uses them. The Thatcher--Wright owed artifact remains unnamed, as required.

Two actual-first-location failures remain. First, the shared theorem relies on the named weak/full distinction before it types either quantifier domain. Second, the chapter source-standing paragraph gives Thatcher--Wright an unqualified finite-tree-automata source role before stating the only supportable abstract/historical standing and the non-substitution boundary. The later reader repairs do not retroactively make either earlier first use locally adequate.

## Must-fix findings

### TATA-R3-AP-01 — weak/full terminology is untyped at its actual first use

**Severity:** must-fix; non-outvotable under T21 and the adversarial seat mandate.

`handbook/parts/p09/logic-in-computer-science.tex:881--882` first says that weak and full monadic second-order quantification coincide on the finite structures, but it does not say there that weak quantification ranges over finite subsets and full quantification ranges over all subsets. No earlier line in that frozen main object types this distinction. The definitions appear only later in the inserted reader at `handbook/parts/p09/presentations/n-c-015.tex:49--52,131--139`, and that reader is not inserted until `logic-in-computer-science.tex:900`.

This ordering matters. TATA printed p. 88 distinguishes WSkS's finite sets from SkS's infinite sets, while printed pp. 95--96 distinguish finite-set WSkS from arbitrary-set full SkS and its infinite-input automata. Without the local ranges at line 881, a reader can misread the true finite-domain coincidence as a claim that weak and full semantics coincide on the infinite successor tree. The sentence therefore fails the required local definition and standing components, despite having a later use and despite being mathematically correct once the missing ranges are supplied.

**Required repair:** at the line 881 first use, state explicitly that weak monadic variables range over finite subsets of the finite position domain and full monadic variables range over all subsets of that domain; then derive coincidence because the domain is finite. Keep the finite position structure distinct there from the infinite successor-tree semantics discussed later.

### TATA-R3-AP-02 — the chapter source-standing sentence overstates Thatcher--Wright's inspected role

**Severity:** must-fix; non-outvotable under T19, T20, and the adversarial seat mandate.

`handbook/parts/p09/logic-in-computer-science.tex:30` says, without qualification, that finite-tree automata use both `ThatcherWright1968` and `ComonEtAl2007`. That is a chapter-level authority assignment, and it appears before the reader's later non-substitution paragraph. It conflicts with the frozen source boundary: `handbook/parts/p09/presentations/n-c-015.tex:141--152`, `spec/research/p09-thatcher-wright-1968-acquisition-note.md:27--48`, and `spec/research/p09-source-presentations-lot2-3.md:684--692` all say that the 1968 technical body is unacquired, that its abstract does not establish a finite-tree input claim or exact technical objects, and that TATA's modern tuple and WSkS construction may not be assigned to it.

The permitted printed evidence sharpens rather than cures the problem. TATA printed p. 11 reports a historical lineage following Doner, Thatcher, and Wright, and printed p. 95 cites `[TW68]` for the WSkS decision result; neither page is an inspection of the Thatcher--Wright body. No inspected Thatcher--Wright printed page controls an operative finite-tree definition or theorem in this snapshot. The chapter may report the historical/abstract connection, but the unqualified word `use` gives that unavailable body the same apparent technical source standing as the inspected TATA monograph.

**Required repair:** distinguish the two roles at line 30 itself. Attribute only abstract-level historical standing to Thatcher--Wright, and attribute the operative finite-ranked-tree definitions, constructions, and theorem used here to the inspected TATA release. Do not rely on the later reader paragraph to repair an earlier unqualified source assignment.

## Express disposition of T01--T22

- **T01 — PASS.** The title, title-page author order, HAL route, frozen hash, 18 November 2008 release, 263-physical/262-monograph-page custody account, and evolving-work 2007 register distinction agree.
- **T02 — PASS.** Authorized HAL access is not inflated into a Creative Commons or blanket republication licence; source pages and renders remain research evidence.
- **T03 — PASS.** The operative input is a finite ranked term, and the introduction's exclusion of infinite-tree automata remains visible.
- **T04 — PASS.** Ranked terms, nullary and positive arities, finite ordered-tree standing, literal TATA tuple, and the nonconflicting handbook symbol/order map are exact.
- **T05 — PASS.** Transitions, bottom-up runs, final-root acceptance, and recognizable languages are correctly typed, including arity zero.
- **T06 — PASS.** Determinism is target uniqueness for a fixed symbol/child-state tuple; same-language subset determinization and reachable subsets are retained without overclaiming a fully reproduced proof.
- **T07 — PASS.** Boolean closure, accessible-state marking, the final-state nonemptiness criterion, and the source's linear implementation boundary are preserved.
- **T08 — PASS.** The `f(a,b)` run is correct, deletion of the root rule leaves no run, and ownership is explicitly handbook-side.
- **T09 — PASS.** Word and finite-set ranges, Proposition 3.3.1, and all four restricted atoms agree with printed pp. 87--90.
- **T10 — PASS.** Arity, coordinate meanings, all named Example 3.3.3 labels, and nullary bottom padding agree with printed pp. 90--91.
- **T11 — PASS.** The finite domain, label sets, label/child translations, and both quantifier restrictions are explicit; the prefix tree remains a coding structure.
- **T12 — PASS.** The complete inclusion transition list and the disjunction, union, negation, and projection operations agree with printed pp. 91--93.
- **T13 — PASS.** The state sets partition exactly the encoded finite domain, the root is final, and the local implication, transition disjunction, and child direction agree with printed pp. 94--95.
- **T14 — PASS.** The source's qualification of Theorem 3.3.7 and the empty-alphabet/nullary-`top` closed-sentence reduction are preserved.
- **T15 — PASS.** The exact alphabet and copying language are retained, and the handbook-owned deterministic separation proof supplies both required premises.
- **T16 — PASS on mathematical content.** Arbitrary-set full SkS, infinite root-down inputs, the different complement argument, and finite-domain coincidence are all correctly stated in the reader. The earlier first-use publication defect is separately rejected under T21 as `TATA-R3-AP-01`.
- **T17 — PASS on source and mathematical agreement.** The shared definition and theorem agree with the reader on finite ranked trees, bottom-up recognition, the MSO correspondence, effective operations, and Rabin nonconflation. Their first-use terminology defect remains `TATA-R3-AP-01` rather than a false theorem.
- **T18 — PASS.** Operative constructions are not inflated into complete reproduction of every source table or proof, and source exercise/source proof/handbook example/handbook proof ownership is visible.
- **T19 — FAIL: `TATA-R3-AP-02`.** The dedicated reader and records enforce non-substitution, but the earlier chapter source-standing sentence gives the unavailable Thatcher--Wright body an unqualified finite-tree-automata role.
- **T20 — FAIL as to cross-record source standing: `TATA-R3-AP-02`; PASS as to Thomas and all other checked fields.** The Thomas object is correctly a May 1996 report precursor, the 1997 body and reconciliation remain open, and TATA identity, notation, locators, ownership, and bibliography otherwise agree. The main line 30 authority assignment is inconsistent with the frozen Thatcher--Wright boundaries.
- **T21 — FAIL: `TATA-R3-AP-01`; additionally implicated by `TATA-R3-AP-02`.** The shared theorem does not type weak/full domains at actual first use, and the unqualified first source-standing assignment does not state the bounded historical versus operative standing locally. The unnamed Thatcher--Wright owed artifact itself complies.
- **T22 — PASS.** Acquisition and reconstruction are not represented as admission; independent review remains open; all completion exclusions remain explicit. Because the present snapshot has two must-fixes, this report admits nothing.

## Admission disposition

The frozen snapshot is mathematically substantial and the source-level TATA reconstruction survives the finite/infinite, weak/full, run, encoding, proof-ownership, access/licence, Thomas-version, and completion-boundary attacks. It is not yet admissible on these hashes because the charter makes each supported publication/terminology boundary defect a non-outvotable must-fix. Repairing only the two exact first-location defects identified above would require a newly frozen object and fresh disposition; this report does not pre-accept that future text.

VERDICT: REJECT — TATA-R3-AP-01, TATA-R3-AP-02
