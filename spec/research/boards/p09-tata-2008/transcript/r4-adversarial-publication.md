# TATA Round 4 — independent adversarial publication and terminology review

## Scope, independence, and method

I reviewed the complete Frozen Round 4 snapshot under the adversarial
publication and terminology mandate. I did not limit the review to the three
Round 4 repairs. I read the seven frozen textual objects completely, independently
recomputed the nine native SHA-256 identities, and visually inspected every one
of the twenty-seven named TATA renders and five named Thomas renders at original
detail.

I used only the Round 4 charter, the nine Frozen Round 4 objects, and the thirty-two
named renders. I did not read a prior-round report, `ledger.md`,
`transcript/chair.md`, another Round 4 report, another board or board transcript,
conversation history, memory, staging or layout material, a handbook PDF, or web
results. I did not contact another reviewer. I ran no test, test harness,
automated checker, repository script, TeX command, build, or handbook-PDF
inspection. Native read-only hashing and direct source/page inspection were the
only mechanical operations.

The admission question applied here is only whether the frozen TATA
reconstruction for `N-c-015.b` is fit for admission at manuscript-content level
on the nine identities below. Nothing in this report admits `N-c-015.a`,
`N-c-015` overall, Part IX, a build, a rendered handbook page, human or user
review, the book, or publication. The Thomas material is considered only for
the adjacent identity, custody, and 1996-report/1997-chapter boundary; no Thomas
mathematics is reviewed or admitted.

## Native identity recomputation

All nine recomputed values equal the Round 4 charter values byte for byte.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-tata-2008/tata-2008.pdf` | `3EB9C3F9A1A9A3BD45EC1E50BD50A1C10010789B542A2818F030A7246F9B5B22` | MATCH |
| `handbook/parts/p09/presentations/n-c-015.tex` | `69AC3973E247EF090D9C78E92991BCEEDB30C0145CC276DC2C45F85DE984B4AD` | MATCH |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` | MATCH |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | MATCH |
| `spec/research/p09-tata-2008-source-note.md` | `E8BB8448B3AAA119575EBC6EE16BD79A5F4F50A584875234513A61FC627FA948` | MATCH |
| `spec/research/p09-source-presentations-lot2-3.md` | `0A1E5537F20DC16D6421FE6FC21B846180B6548F8AA9B5B6A2CC5942FC0524B3` | MATCH |
| `spec/research/p09-thatcher-wright-1968-acquisition-note.md` | `547821EE7F3B8078C884C2145D4CE4857715F3E2B9775DC57B573098D96C7275` | MATCH |
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | MATCH |
| `spec/research/p09-thomas-1996-report-source-note.md` | `9B06269638D97345123D23434BB9B299EDACF6B1373C9190E92190E3FBE45581` | MATCH |

## Complete reading and visual-inspection record

I read these seven textual objects in full:

1. `handbook/parts/p09/presentations/n-c-015.tex`;
2. `handbook/parts/p09/logic-in-computer-science.tex`;
3. `handbook/bib/handbook.bib`;
4. `spec/research/p09-tata-2008-source-note.md`;
5. `spec/research/p09-source-presentations-lot2-3.md`;
6. `spec/research/p09-thatcher-wright-1968-acquisition-note.md`; and
7. `spec/research/p09-thomas-1996-report-source-note.md`.

I individually inspected the following twenty-seven TATA renders at original
detail:

- `core-rendered/page-001.png`, `page-002.png`;
- `core-rendered/page-012.png`, `page-013.png`, `page-014.png`;
- `core-rendered/page-020.png`, `page-021.png`, `page-022.png`, `page-023.png`,
  `page-024.png`, `page-025.png`, `page-026.png`, `page-027.png`, and
  `page-028.png`;
- `core-rendered/page-031.png`, `page-041.png`, and `page-044.png`; and
- `relevant-rendered/page-088.png`, `page-089.png`, `page-090.png`,
  `page-091.png`, `page-092.png`, `page-093.png`, `page-094.png`,
  `page-095.png`, `page-096.png`, and `page-097.png`.

Those pages establish, directly rather than through extraction, the HAL cover
and title identity; the 18 November 2008 footer; the monograph's express finite-
tree scope and exclusion of infinite-tree automata; the chapter opening and
finite ranked terms; the tuple, transition, run, acceptance, and recognizable-
language definitions; accessible-state reduction and reachable-subset
determinization; Boolean closure; linear-time emptiness; Exercise 1.4; WSkS
syntax and finite-set semantics; the restricted atoms; the finite-set encoding
and Example 3.3.3; both logical directions and their operations; the displayed
inclusion automaton; the local accepting-run formula; the “not very precise”
qualification; the closed-sentence reduction; and the weak/full and
finite/infinite boundary.

I also individually inspected these five Thomas renders at original detail:

- `inspect-title-01.png`;
- `inspect-title-02.png`;
- `inspect-title-03.png`;
- `inspect-body-start-04.png`; and
- `inspect-body-end-75.png`.

They establish that the acquired object is Wolfgang Thomas's May 1996 Kiel
`Bericht 9607`, physical pages 1--75 mapping through printed pages `i`, 1, and
72 as recorded. Most importantly, the abstract literally says that a modified
version would become a chapter of the *Handbook of Formal Language Theory*.
The frozen note correctly preserves that prospective wording separately from
the eventual registered title *Handbook of Formal Languages*.

## Finding register

No blocker, must-fix, should-fix, consider, or unresolved-user finding is
supported on the frozen Round 4 snapshot. In particular, I found no premature
technical name, undefined standing, source substitution, mathematical type
error, quantifier-range error, theorem-strength inflation, rights overclaim,
stale completion claim, or cross-record contradiction.

Because a supported must-fix is non-outvotable, I treated each candidate below
as potentially dispositive until the controlling page and every frozen record
agreed. Each candidate was falsified and is therefore discarded, not silently
waived:

| Adversarial candidate | Disposition |
|---|---|
| The stable key `ComonEtAl2007` might misdate the controlling object. | Discard. The bibliography records year 2008 and the 18 November 2008 release (`handbook.bib` lines 5847--5853); the reader distinguishes the register's evolving-work label from the fixed release (`n-c-015.tex` lines 6--10); the HAL cover/title and printed footers agree. |
| The different source and handbook tuple orders might conceal a definition change. | Discard. TATA's printed pp. 20--22 use `A=(Q,F,Q_f,Delta)`; reader lines 27--30 explicitly map source `F` to handbook `Sigma`, source `Q_f` to handbook `F`, and source ordering to the handbook tuple. Main lines 848--870 give the handbook tuple and the same run language. |
| The finite prefix-tree coding might silently become Rabin's infinite input tree. | Discard. Reader lines 73--83 restrict the represented domain to the finite position set `D`; main lines 879--897 type the finite structure and expressly reject Rabin nonconflation; TATA printed pp. 11--13 and 95--96 keep the finite/infinite constructions separate. |
| “Weak” and “full” might be used before their quantifier ranges are stated. | Discard. At the actual first weak/full use in the shared theorem, main lines 884--889 state finite-subset versus all-subset ranges and explain both finite-domain coincidence and infinite-successor-tree noncoincidence. Reader lines 49--60 and 131--139 give the operative WSkS and full-SkS ranges before relying on the distinction. |
| Public HAL availability might be expanded into a republication licence. | Discard. The HAL cover supports authorized public deposit; source-note lines 31--34 expressly deny a blanket licence, report that no Creative Commons licence was observed, and keep PDF/renders as research evidence rather than handbook assets. |
| The reader's small run or Exercise 1.4 proof might be silently attributed to TATA. | Discard. Reader lines 32--37 and 120--129 give the two handbook constructions; lines 154--160 expressly mark both as handbook-owned. The source pages supply the underlying definitions and exercise, not those handbook examples/proofs. |
| The constructive summary might claim reproduction of every TATA state table or proof. | Discard. Reader lines 154--160 limit the reconstruction to the operative steps and expressly deny reproducing every printed transition table or proof. This agrees with source-note lines 173--176 and compact-record lines 702 and 706. |
| TATA's modern ranked-tree/WSkS construction might be substituted for the missing Thatcher--Wright body. | Discard. Main lines 30--33 give Thatcher--Wright only abstract-level historical standing and TATA the operative role. Reader lines 141--152, TATA-note lines 187--197, compact-record lines 684--692, and the acquisition note lines 5--7 and 27--34 leave every body-dependent object open. RC-1713 is only an acquisition lead, and the owed artifact at acquisition-note lines 74--82 is deliberately unnamed. |
| The acquired Thomas file might again be treated as the registered 1997 chapter. | Discard. The Thomas title, abstract, contents, first numbered page, and last numbered page visually establish a May 1996 Kiel report. Thomas-note lines 13--22 and 51--58 call it a precursor; lines 79--89 leave registered-chapter acquisition and reconciliation open. The literal prospective and eventual titles are distinct. |
| Acquisition or manuscript integration might be described as review, admission, build, or publication completion. | Discard. TATA-note lines 5--12 and 178--185, reader line 161, compact-record lines 706 and 900--916, and Thomas-note lines 79--95 keep those statuses distinct and open. |

## Independent mathematical and boundary stress tests

These checks were performed from the frozen text and controlling rendered
pages, not accepted merely because the records asserted them.

1. **Nullary and positive arities.** Reader lines 12--25 cover `n=0` and
   positive arity uniformly. A nullary transition is a leaf rule, while
   `f(q_1,...,q_n)->q` supplies the parent state for positive arity. This matches
   TATA printed pp. 19--22 and main lines 848--870.

2. **Missing and partial runs.** The small automaton at reader lines 32--37
   accepts `f(a,b)` through the displayed root rule. Removing that rule does
   not merely reject a completed run: it leaves the root unlabelled and hence
   leaves the ground term with no run. This is correct under TATA printed
   pp. 20--22. The wording does not assume transition completeness.

3. **Reachable subset determinization.** TATA printed pp. 25--27 first gives
   the power-set transition equation, then an algorithm that constructs only
   accessible subset states and proves the same-language invariant. Reader
   lines 39--41 retain deterministic target uniqueness, language equality, and
   reachable-subset standing without importing an unreconstructed table.

4. **Unreachable states and emptiness.** The marking process begins at targets
   of nullary transitions and closes upward under rules whose child states are
   already marked. A language is nonempty exactly when the least such marked
   set meets the final set. This agrees with TATA printed p. 40. Reader lines
   41--46 do not claim a representation-independent complexity result: they
   attach linear time to the automaton representation/source implementation.

5. **Finite-set encoding and empty tracks.** The second coordinate in Example
   3.3.3 is bottom everywhere because `S_2` is empty, not zero everywhere.
   Reader lines 62--71 correctly distinguish membership `1`, proper-prefix
   continuation `0`, and absence `bottom`; only the all-bottom symbol is
   nullary. The root, positions `1`, `2`, `11`, and `22`, and the remaining
   padding leaves agree with TATA printed pp. 90--91.

6. **Restricted inclusion automaton.** Reader lines 85--96 retain the complete
   one-state transition list for `X subseteq Y`:
   `bottom bottom -> q`, `00(q,q)->q`, `01(q,q)->q`, `11(q,q)->q`,
   `bottom 0(q,q)->q`, and `bottom 1(q,q)->q`. The omitted coordinate pairs are
   exactly the incompatible ones. Missing tracks are added before union;
   negation uses complement; existential set quantification uses projection.
   This matches TATA printed pp. 91--93.

7. **Converse run formula.** Reader lines 98--110 quantify one position set per
   state, partition exactly the encoded finite domain, require the root to lie
   in some final-state set, and direct each transition from the children's
   states to the current node's state. In the local implication, the
   disjunction ranges only over transitions whose target is the current state,
   and the conjunction labels child `i` by the corresponding source state.
   The nullary case reduces correctly to an empty child conjunction. This
   matches TATA printed pp. 94--95.

8. **Closed sentences.** Reader lines 112--118 preserve TATA's warning that
   Theorem 3.3.7 is “not very precise” and defer exact strength to Lemmas 3.3.4
   and 3.3.6. With no free tracks, the source convention leaves only nullary
   `top`; validity is exactly the existence of `top -> q_f` for some final
   state. No all-zero-track surrogate remains. This matches printed p. 95.

9. **Exercise 1.4.** Reader lines 120--129 preserve the exact alphabet
   `{a^(0),f^(2)}` and language `{f(t,t):t in T(F)}` from printed p. 43. If a
   deterministic recognizer existed, acceptance of every `f(t,t)` forces every
   `t` to reach a state. Two distinct terms reaching one state would make the
   same parent transition give `f(t,t)` and `f(t,u)` the same final-root
   behavior, contradicting the language. Infinitely many terms would therefore
   require infinitely many states. The proof is valid and is marked
   handbook-owned.

10. **Weak/full and finite/infinite.** WSkS set variables range over finite
    word sets (reader lines 49--60; TATA printed pp. 87--90). Full SkS permits
    arbitrary subsets of the infinite successor tree and needs root-down
    automata on infinite inputs with a different complementation argument
    (reader lines 131--139; TATA printed pp. 95--96). Weak and full ranges
    coincide on an actually finite position domain because every subset of that
    domain is finite; that elementary coincidence does not change the
    automaton's finite input. Main lines 843--897 keep Rabin's entire infinite
    binary tree separate.

## Five-part terminology audit at actual first use

The audit distinguishes new handbook terminology from established source terms
that still require typing before reliance.

| First-use location | Necessity | Definition or source standing | Standing | Nonredundancy | Required later use | Result |
|---|---|---|---|---|---|---|
| Main lines 30--33: Thatcher--Wright versus TATA authority | The historical citation and operative modern construction must not be conflated. | Thatcher--Wright is expressly limited to abstract-level historical standing; TATA controls operative definitions, constructions, and theorem. | Metalinguistic source-standing distinction. | Historical provenance is not modern technical evidence. | Used by the finite-tree definition/theorem and reader boundary. | SATISFIED |
| Main lines 848--875: finite ranked tree and finite bottom-up tree automaton | Arity-indexed finite trees and bottom-up runs must be distinguished from word automata and Rabin runs. | Lines 849--870 define the ranked alphabet, least finite term set, tuple, transitions, runs, acceptance, and language. | Mathematical objects, run relation, and accepted-language construction. | Lines 871--874 expressly distinguish word and infinite-tree objects. | Used immediately by the theorem at lines 879--897 and by the reader. | SATISFIED |
| Main lines 884--889: weak/full monadic ranges | The finite-domain coincidence must be stated without erasing the infinite-domain distinction. | Weak variables range over finite subsets; full variables over all subsets; finite-domain equality and infinite-tree inequality are both stated. | Quantifier-range/property distinction for two statement families. | The two ranges coincide only on finite domains and differ on the infinite successor tree. | Used in the theorem boundary and reader lines 131--139. | SATISFIED |
| Reader lines 12--30: TATA ranked alphabet, term, automaton, run, recognizable language | The source notation differs from the handbook notation and must be fixed before use. | Every established source term is typed and the tuple/symbol map is explicit. | Finite objects, transition/run relations, and language property. | The source/handbook symbol collision is expressly eliminated. | Used by determinization, closure, emptiness, logic, and examples. | SATISFIED |
| Reader lines 49--60: WSkS and restricted atoms | First- and second-order ranges must be distinguished before the automata translation. | The word domain, finite-set range, singleton replacement, four atomic forms, and `X=Yi` meaning are locally supplied. | Logic, variable ranges, and formula family. | The restricted syntax removes first-order variables while preserving assignments. | Used by Lemma 3.3.4 and the finite-set coding. | SATISFIED |
| Reader lines 62--83: finite-set encoding and finite-tree bridge | A tuple of finite sets must become one finite automaton input without an infinite-input substitution. | Coordinate meanings, arities, finite domain `D`, label and child atoms, and quantifier restrictions are given. | Coding construction and translation relation. | Prefix-tree coding is explicitly not Rabin's input tree. | Used by both logical directions at lines 85--110. | SATISFIED |
| Reader lines 141--160 and Thatcher--Wright note lines 64--82: missing-source obligation | The historical gap must remain expressible without pretending to know its answer. | The extant abstract has bounded source standing; all body-dependent artifacts are enumerated as owed. | Metalinguistic acquisition and evidence status. | The open obligation is separated from TATA, Rabin, and RC-1713. | Governs later acquisition and prevents current attribution. | SATISFIED |
| Thomas note lines 13--22 and 49--68: “report precursor” | The acquired body and registered authority are different versions despite author/title identity. | The report is dated, numbered, and limited to precursor strength pending reconciliation. | Metalinguistic version/evidence status. | The literal prospective title and eventual registered title are kept distinct. | Governs citations, locators, reconciliation, and admission at lines 79--89. | SATISFIED |

No hypothetical name is assigned to the missing Thatcher--Wright construction.
The charter labels `T01`--`T22` are used only as metalinguistic review
identifiers. Established names such as WSkS, SkS, ranked alphabet, run,
recognizable language, and bottom-up automaton are typed before the frozen
manuscript relies on them.

## Mandatory T01--T22 dispositions

| Item | Disposition and controlling evidence |
|---|---|
| **T01 — identity and version** | **SATISFIED.** The HAL cover, internal title, and printed footers agree with source-note lines 5--29, reader lines 6--10, compact-record lines 694--696, and bibliography lines 5847--5853 on title, title-page author order, official HAL route, hash, 18 November 2008 release, and 263-physical/262-monograph custody. The `2007` register/key label is expressly distinguished from the fixed 2008 release. |
| **T02 — rights** | **SATISFIED.** The HAL cover establishes authorized public deposit, while source-note lines 31--34 deny a demonstrated Creative Commons or blanket republication licence and classify the PDF/renders as research evidence, not assets. |
| **T03 — finite/infinite domain** | **SATISFIED.** TATA printed pp. 11--13 expressly treats finite trees and excludes infinite-tree automata. Reader lines 6--10 and 131--139 and main lines 843--897 preserve the separation from Rabin's entire infinite labelled tree. |
| **T04 — ranked terms and tuple** | **SATISFIED.** Reader lines 12--30 define nullary and positive-arity term formation and finite ordered trees, reproduce TATA's `A=(Q,F,Q_f,Delta)` from printed pp. 19--20, and give a nonconflicting source-to-handbook map. |
| **T05 — runs and recognition** | **SATISFIED.** Reader lines 20--27 and main lines 859--870 correctly type transitions, bottom-up runs, final-root acceptance, and recognized languages for all arities, including nullary rules, in agreement with printed pp. 20--22. |
| **T06 — determinization** | **SATISFIED.** Reader lines 39--41 state at-most-one target per fixed symbol/child-state tuple, same-language strength, and reachable subset states. Printed pp. 25--27 support all three and no extra source detail is claimed. |
| **T07 — closure and emptiness** | **SATISFIED.** Reader lines 41--47 accurately retain effective union/complement/intersection from printed p. 30 and upward accessible-state marking with final-state nonemptiness from printed p. 40. The linear claim remains attached to the source's automaton representation/proof route. |
| **T08 — small run ownership** | **SATISFIED.** Reader lines 32--37 give a correct finite run on `f(a,b)` and explain that deletion of the root rule leaves no run; lines 154--160 and source-note lines 61--65 identify it as handbook-owned. |
| **T09 — WSkS semantics and restricted atoms** | **SATISFIED.** Reader lines 49--60 type first-order words and finite word-set variables before use and reproduce `X subseteq Y`, `Sing(X)`, `X=Yi`, and `X=epsilon` from printed pp. 87--90. |
| **T10 — finite-set encoding** | **SATISFIED.** Reader lines 62--71 match printed pp. 90--91 on arities, `1/0/bottom` meanings, all named Example 3.3.3 labels, empty `S_2`, and nullary all-bottom padding. No all-zero-track slogan remains. |
| **T11 — bridge to finite-tree MSO** | **SATISFIED.** Reader lines 73--83 specify finite `D`, symbol-label subsets, `x in X_f`, `y=xi`, and restrictions of element and monadic quantifiers to `D` and its subsets; state sets partition the same domain. Main lines 879--889 give the finite structure. The ambient prefix tree is only the coding structure. |
| **T12 — Lemma 3.3.4** | **SATISFIED.** Reader lines 85--96 reproduce the complete six-rule inclusion automaton and the missing-coordinate/cylindrification step, union, complement, and projection, matching printed pp. 91--93. |
| **T13 — Lemma 3.3.6** | **SATISFIED.** Reader lines 98--110 quantify one position set per state, partition exactly the finite encoded domain, require a final root, and preserve the implication, matching-transition disjunction, and child-state direction from printed pp. 94--95. |
| **T14 — theorem qualification and closed sentences** | **SATISFIED.** Reader lines 112--118 retain TATA's “not very precise” qualification, put exact strength in Lemmas 3.3.4/3.3.6, and give the empty-alphabet/single-nullary-`top` convention and `top -> q_f` validity test from printed p. 95. |
| **T15 — Exercise 1.4** | **SATISFIED.** Reader lines 120--129 preserve the exact `{a^(0),f^(2)}` alphabet and copying language from printed p. 43. The handbook-owned proof supplies both total reachability forced by `f(t,t)` acceptance and deterministic state separation for distinct terms. |
| **T16 — weak/full boundary** | **SATISFIED.** Reader lines 131--139 and main lines 884--897 distinguish finite WSkS sets from arbitrary full-SkS subsets and finite-domain coincidence from infinite-successor-tree difference. Printed pp. 95--96 support root-down infinite inputs and the different complementation boundary. |
| **T17 — shared main theorem** | **SATISFIED.** The current shared definition is at main lines 848--877 and the theorem at lines 879--898. They agree with reader lines 12--139 and the controlling TATA pages on ranked finite trees, bottom-up runs, recognition, finite-tree MSO, effective determinization/Boolean closure/emptiness, and Rabin nonconflation. |
| **T18 — proof and reconstruction boundary** | **SATISFIED.** Reader lines 154--160 and source-note lines 173--176 describe an operative constructive outline, do not claim every source table or proof, and preserve source exercise/source theorem versus handbook example/proof ownership. |
| **T19 — Thatcher--Wright non-substitution** | **SATISFIED.** Main lines 30--33; reader lines 141--152; TATA-note lines 187--197; compact-record lines 684--692; and acquisition-note lines 5--7, 27--34, and 64--82 keep only identity and abstract-level historical scope. No algebraic signature, relation, theorem, weak logic, example, or proof is reconstructed from TATA. RC-1713 is only a lead. The owed artifact is enumerated without a hypothetical answer-name. |
| **T20 — bibliography and cross-record agreement** | **SATISFIED.** Bibliography lines 2346--2367, 5847--5853, and 6005--6014 agree with the reader, main, detailed notes, and compact record. Author order, dates, numbering, locators, notation maps, ownership, and status contain no stale contradiction. The Thomas renders and Thomas-note lines 5--22, 36--41, 51--68, and 79--89 identify the May 1996 report precursor, preserve its literal prospective *Handbook of Formal Language Theory* separately from eventual *Handbook of Formal Languages*, and keep the registered 1997 body/reconciliation open. |
| **T21 — terminology rule** | **SATISFIED.** The actual-first-use audit above confirms necessity, definition/source standing, standing, nonredundancy, and later use for every material new distinction. Established source terms are typed before reliance. Open obligations are owed artifacts, not speculative terminology. |
| **T22 — completion scope** | **SATISFIED.** Source-note lines 5--12 and 178--185, reader line 161, compact-record lines 706 and 900--916, and Thomas-note lines 79--95 distinguish acquisition, reconstruction, review, admission, build, visual, human/user, book, and publication statuses. This verdict is limited to `N-c-015.b` manuscript content on the nine hashes above. |

## Conclusion

The complete Frozen Round 4 snapshot is source-faithful within its stated page
and source boundaries, mathematically coherent at the reconstructed strength,
definition-before-use compliant, terminologically disciplined, and fit for the
narrow manuscript-content admission question. All T01--T22 invariants are
satisfied. There is no supported blocker or must-fix to prevent this seat's
acceptance, and no acceptance statement here extends beyond `N-c-015.b` on the
nine frozen identities.

VERDICT: ACCEPT
