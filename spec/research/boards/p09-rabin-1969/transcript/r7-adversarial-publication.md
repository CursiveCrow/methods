# Round 7 adversarial publication and terminology review — Rabin 1969

**Seat:** Adversarial publication and terminology  
**Presentation:** `N-c-014.d`, Michael O. Rabin (1969)  
**Frozen round:** Round 7  
**Review date:** 2026-08-23

## Decision in brief

I reject this frozen manuscript snapshot for one must-fix cross-record publication-status defect, `AP7-01`. The mathematical reconstruction in the reader survived my independent source and edge-case audit, including the ordinary/dual quantifier reversal, vacuous dual acceptance, the typed Theorem 3.1 product, the zero-length pair-sequence normalization, both source-owned and handbook-owned parts of the emptiness argument, and the later Meyer complexity correction. The detailed source note nevertheless closes by saying that fresh **Round 6** reviews are about to begin, despite its own opening, the compact record, and the controlling charter all identifying the frozen campaign as **Round 7**. That contradiction fails mandatory invariant R24 and makes the publication-status record unfit for admission as frozen.

This is a verdict only on the six-object Round 7 `N-c-014.d` manuscript snapshot. It is not a verdict on a rendered handbook page, a TeX build, all of `N-c-014`, Part IX, another part, the book, human review, user acceptance, final typesetting, or permission to redistribute either source PDF.

## Evidence boundary and review method

I used only the evidence authorized by the Round 7 charter:

1. `spec/research/boards/p09-rabin-1969/charter.md`, read completely;
2. the six frozen Round 7 objects named below, each read completely;
3. `tmp/pdfs/p09-rabin-1969/rendered/page-01.jpg` through `page-36.jpg`, each inspected visually at original detail; and
4. `tmp/pdfs/p09-rabin-1969/meyer1975-rendered/page-485.png` through `page-490.png`, each inspected visually at original detail.

I did not read an earlier-round report, another Round 7 report, a ledger, a chair transcript, another board or transcript, a staging draft, or the layout extraction as evidence. I did not contact another reviewer or browse the web. I ran no test, automated checker, repository script, TeX command, interim build, handbook-PDF inspection, or build. The only computation was native SHA-256 hashing of the six frozen objects, as the charter permits. File reads used the native text of the frozen objects; the printed articles were controlled by the required visual renders, not by an extraction.

The six-object text inspection covered the complete 1,437-line reader file, complete 6,272-line bibliography, complete 660-line detailed source note, and complete 915-line compact presentation record, as well as the two complete frozen PDFs through their mandated source-page renders.

## Frozen identity results

All six native SHA-256 values were independently recomputed before the substantive review. Every value exactly matches the Round 7 charter.

| Frozen object | Recomputed SHA-256 | Identity result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `73A700E83218BD1E0460CD836E72FB7EE86914C52D70D865B903CE367400C944` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `0EE7C6EAD01590636652D409EA51FD7A34555F410E3277121B165932A233D41F` | exact match |

## Printed-source pages inspected

### Rabin 1969: every physical page

I visually inspected all 36 physical pages in the required Rabin render set. The complete physical-to-printed map is:

- physical page **01**: JSTOR/AMS custody-and-use cover;
- physical **02→printed 1**, **03→2**, **04→3**, **05→4**, **06→5**, **07→6**, **08→7**, **09→8**, **10→9**;
- physical **11→printed 10**, **12→11**, **13→12**, **14→13**, **15→14**, **16→15**, **17→16**, **18→17**, **19→18**, **20→19**;
- physical **21→printed 20**, **22→21**, **23→22**, **24→23**, **25→24**, **26→25**, **27→26**, **28→27**, **29→28**, **30→29**; and
- physical **31→printed 30**, **32→31**, **33→32**, **34→33**, **35→34**, **36→35**.

The visual inspection confirmed, in particular:

- printed pp. 1–5: the main decidability statement, Rabin's historical elementary-recursive claim, notation, Λ, Definition 1.1 for (0<n\leq\omega), both orders, and the finite/ω qualification;
- printed pp. 6–10: arbitrary-root valued trees, paths, tables, ordinary automata, ordinary acceptance, closure, Definition 1.7, both formula-to-automaton and automaton-to-formula directions, and the closed-sentence nonemptiness reduction;
- printed pp. 10–17: the exact Chapter II applications and their class-level strengths;
- printed pp. 17–19: sequential Büchi/Muller automata, McNaughton's external result, and Theorem 3.1's product construction;
- printed pp. 19–24: marked trees, simultaneous runs, same-state merging, Rabin's definition of a well-founded mapping, ordinal stratification, and the later finite-state use of those obligations;
- printed pp. 24–32: type and type-empty path conditions, dual acceptance, complement representation, the two half-steps, the arbitrary-sequence well-founded step, finite frontiered trees, and the lift/compactness/complementation division among Lemma 3.12, Corollary 3.13, Lemma 3.14, and Corollary 3.15;
- printed pp. 32–34: one-letter alphabet erasure, complement-to-dual conversion, restricted tables, the recursive length reduction, and the two printed nonempty-witness clauses on p. 34; and
- printed p. 35: the conclusion of the source bibliography and author affiliations.

The custody cover visibly states personal, noncommercial archive-use restrictions and directs further-use questions to the publisher. It therefore supports research custody, not an open-content or republication licence.

### Meyer 1975: every mandated article page

I visually inspected all six required Meyer renders:

- physical PDF **485→printed 477**: article title, author, opening complexity discussion, and copyright line;
- physical PDF **486→printed 478**: the general lower-bound form, its nondeterministic scope, and the weak-successor-theory lower-bound lead-in;
- physical PDF **487→printed 479**: the enumerated theory list, including item 5, “the theory of two successors and prefix,” credited to Meyer and Stockmeyer, plus the tower upper-bound comparison;
- physical PDF **488→printed 480**: consequences for practical feasibility and comparison of nearby theories;
- physical PDF **489→printed 481**: the finite-network consequence and the beginning of the references; and
- physical PDF **490→printed 482**: the remaining references, including Rabin 1969 and the Meyer/Stockmeyer complexity item, and the affiliation.

These pages support the reader's source/later-source boundary: Rabin controls the 1969 decidability proof; Meyer controls the later correction to Rabin's worst-case complexity qualification. Printed pp. 478–479 do not retract decidability or effectiveness.

## Finding

### AP7-01 — MUST-FIX — the detailed source note states an obsolete and contradictory review round

**Exact frozen manuscript locations.** In `spec/research/p09-rabin-1969-source-note.md`:

- lines 18–39 correctly say that Rounds 1–3 and 5–6 are closed/rejected, Round 4 was withdrawn, and a fresh hash-pinned **Round 7** is required;
- line 618 nevertheless labels the integration as repaired only “after Rounds 1--4”;
- lines 649–651 omit Round 6 from the preserved report history; and
- lines 658–660 say that the six objects must be frozen before three fresh **Round 6** reviews begin and that those reviews can admit the presentation.

The contradiction is not isolated to typography. `spec/research/p09-source-presentations-lot2-3.md:672` correctly says that a newly frozen Round 7 snapshot and fresh independent review remain required and that `N-c-014.d` is not admitted. The Round 7 charter's frozen-object table is at lines 163–170, and its controlling Round 7 filing rule is at lines 463–484. Thus the detailed note disagrees both with itself and with the other frozen status record.

**Controlling printed-page check.** No Rabin or Meyer printed page controls an internal repository review-round designation. Rabin printed p. 35 and Meyer printed p. 482 are the terminal pages of the two inspected articles and contain only source references/affiliations, not manuscript-admission history. For this procedural claim, the controlling frozen authority is therefore the charter's Round 7 table and filing rule, not an article page. This absence of a printed controller is itself why the repository status must agree internally rather than be presented as source-backed history.

**Defect.** Mandatory invariant R24 requires the reader, detailed note, compact record, and bibliography to agree, expressly including pending-review status. The detailed note falsely places the frozen snapshot before Round 6 while its opening and compact record place it before/during Round 7. A reader or chair using only that note cannot tell which blind round controls admission. The stale line also makes the closing admission condition point to a round that the same note says has already closed and been rejected.

**Minimum sufficient repair.** Replace the stale section heading and closing history/status paragraph with the complete, truthful round history and the actual next required blind round. The revised text must include the Round 6 disposition, retain the statement that the topic is not admitted, and identify the next fresh hash-pinned round consistently in both the detailed and compact records. Because the charter says that any content edit invalidates all Round 7 verdicts, a repair made after this rejection must be refrozen under new hashes and reviewed in a new blind round; it cannot cure this already frozen Round 7 snapshot in place. Under the current sequence, that successor would ordinarily be Round 8.

## R01–R29 invariant audit

| Invariant | Result | Independent audit and locators |
|---|---|---|
| R01 | PASS | Reader lines 914–917 retains Rabin's Λ and expressly rejects a silent ε substitution; printed pp. 2 and 5 confirm the source symbol. Editorial order subscripts are identified as disambiguations, not new relations (reader 918–927). |
| R02 | PASS | Reader 941–963 states Definition 1.1 for every (0<n\leq\omega), types (T_n=n^*), successors and both orders, and gives the exact finite-(n)/(T_\omega) qualification. This agrees with printed p. 5. |
| R03 | PASS | Reader 965–1014 defines (T_x), path, arbitrary-root valued trees, the distinct table and automaton tuples, (F\subseteq\mathcal P(S)), runs, and ordinary (\exists r\,\forall\pi) acceptance. Printed pp. 5–7 agree. |
| R04 | PASS | Reader 1143–1188 places Ω only in Definition 3.5/3.6 dual acceptance, gives (\forall r\,\exists\pi), distinguishes it from ordinary (F), and states no-run vacuity. Printed pp. 24–25 agree. |
| R05 | PASS | Reader 1016–1023 gives the exact roles of Theorems 1.3–1.6. Theorem 1.4 is described locally as removing one coordinate and conversely adding an unconstrained coordinate; no unsupported operation name is introduced. Printed p. 7 controls. |
| R06 | PASS | Reader 1027–1065 types Definition 1.7's bijection (\mathcal P(T)^n\leftrightarrow\{0,1\}^n)-valued full-root trees and separately records the principal-formula, finite-tree, Boolean, projection, and complement steps. Printed pp. 7–9 and 30–31 support the division. |
| R07 | PASS | Reader 1067–1077 clearly labels (\exists x(x\in A\land r_0(x)\in B)) as a handbook-worked two-track instance, not a Rabin-printed transition table. The construction faithfully instantiates printed pp. 8 and 31. |
| R08 | PASS | Reader 1079–1098 gives state tracks, Lemma 1.2's one-initial-state normalization, the exact (\exists\bar B\,\forall C) form, and the sentence-to-nonemptiness reduction without a basis theorem. Printed pp. 9–10 agree. |
| R09 | PASS | Reader 1102–1139 exactly types (K:U\times S\to U), (U\times S), (\{u_0\}\times S), the shared child update (K(u,s)), and designated projection family. The one-symbol shift does not change infinite-occurrence acceptance. Printed p. 18 agrees. |
| R10 | PASS | Reader 1143–1188 gives the exact type and type-empty clauses, range versus infinitely-recurring-set distinction, quantifier reversal, and complement role. Printed pp. 24–25 agree. |
| R11 | PASS | Reader 1218–1225 retains marked labels, simultaneous activated copies, same-state merging, and Theorem 3.1's path check as distinct necessary finite-state components. Printed pp. 19–24 support them. |
| R12 | PASS | Reader 1227–1233 defines the nonempty-(H) mapping (h\mapsto H_h\subseteq H), exact no-infinite-chain condition, ordinal equivalent, and later Lemma 3.4 use; reader 1244–1247 and 1296–1303 give the Lemma 3.11 use and precise transfinite locus. Detailed note 421–448 and compact record 668 supply the same definition, standing, nonredundancy, and use at first substantive occurrence. |
| R13 | PASS | Reader 1235–1256 preserves the pair-list lengths in Lemmas 3.7–3.11, separates last-lower-set-empty from arbitrary cases, and states the two positive-length half-steps after normalization. Printed pp. 25–32 agree. |
| R14 | PASS | Reader 1259–1283 gives finite predecessor closure, the exact frontier, both-child condition, property standing of “frontiered,” its nonredundancy, later need, frontier-excluding valuation, transition codomain, and (f\notin S) as an external value. Detailed note 307–320 and compact record 670 do likewise at their first substantive uses. Printed p. 30 controls. |
| R15 | PASS | Reader 1284–1293 assigns the lift to Lemma 3.12, the principal-formula application to Corollary 3.13, compactness to Lemma 3.14, and complement use to Corollary 3.15. It does not turn an infinite input or full monadic theory into a weak one. Printed pp. 30–32 agree. |
| R16 | PASS | Reader 1307–1333 follows printed pp. 32–33: erase the alphabet to one letter, complement that language, convert it to a dual language, and decide membership. It expressly excludes a regular-tree basis substitution. |
| R17 | PASS | Reader 1335–1351 retypes the current state set/table/pair list at the recursive boundary and gives Definition 3.7's formal-state/root exception exactly. Printed p. 33 agrees. |
| R18 | PASS | Reader 1353–1371 exhausts every (H\subseteq U_k), makes (H=\varnothing) the direct shorter question, uses restriction for nonempty (H), labels the empty case handbook-owned, and gives finite-stratum termination. Printed pp. 33–34 show the source's narrower nonempty wording. |
| R19 | PASS | Reader 1373–1389 permits (m=0), (U_0=\varnothing), and the finite no-run obstruction, while retaining the printed nonempty branch and identifying Doner/Thatcher–Wright as external. Printed p. 34 controls the source gap; the correction is accurately owned by the handbook. |
| R20 | PASS | Reader 952–960 reports but does not retain Rabin's elementary-recursive qualification. Meyer printed pp. 478–479 states the non-elementary tower form and credits the two-successors-and-prefix case to Meyer and Stockmeyer. The reader withdraws only the bound, not decidability/effectiveness. |
| R21 | PASS | Reader 1404–1421 maps the countable/full/weak strengths of the linear-order, unary-function, Cantor-space, Boolean-algebra, and game applications to Rabin printed pp. 10–17 without broadening them. |
| R22 | PASS | Reader 1423–1437 states what is reconstructed, leaves the detailed transition tables and inductions in Rabin, and separates Thomas's later basis route and McNaughton's external word theorem. |
| R23 | PASS | Numbering and locators agree with all inspected source pages. Relevant bibliography entries are correctly identified at `handbook.bib:2290–2299` (McNaughton), `2346–2355` (Thomas), `5938–5947` (Meyer), `5973–5982` (Rabin), and `5993–6002` (Thatcher–Wright). No strength or attribution laundering was found. |
| R24 | **FAIL — AP7-01** | Meyer correction, Rabin scan URL, and Thatcher–Wright pagination/DOI agree, but the detailed note's lines 618 and 649–660 contradict its own 18–39 and compact-record line 672 about the pending round. |
| R25 | PASS | Detailed note 87–93 and the inspected custody cover limit the inference to research access and ordinary scholarly reconstruction; they expressly deny an open-content, redistribution, or page-reproduction licence. |
| R26 | PASS | The technical-name audit below found exact local necessity, definition/axiom status, standing, nonredundancy, and later use for every newly introduced technical name in scope. No merely hypothetical name substitutes for an owed construction. |
| R27 | PASS | The reader keeps finite/infinite tree, weak/full logic, ordinary/dual acceptance, existence/effectivity, 1969 source/later route, and decidability/complexity boundaries separate. The stress tests below record the decisive cases. |
| R28 | PASS | All status language at reader 1423–1437 and compact record 672 is manuscript-limited and expressly pending. This report's rejection is equally limited and establishes no build, render, human, user, part, or book verdict. |
| R29 | PASS | Reader 1190–1213 identifies the possible zero-length enumeration, proves the no-rooted-run semantics, defines (\Omega^\dagger=((S,S))), proves its path language empty, explains semantic equivalence, states necessity, and uses it to enter the source's positive-length induction. |

## Five-part technical-name audit

I treated first use as a publication constraint, not merely a glossary check. The following are the names most capable of creating hidden reader debt; each passed the repository's five-part rule in the reader and, where used, the detailed and compact records.

| Name or notation | Necessity and exact definition | Standing, nonredundancy, and later use |
|---|---|---|
| Editorial order subscripts | Reader 918–927 defines the initial-segment relation by (y=xz) and identifies the other as the induced lexicographic order. | They are relations and typographic disambiguations of Rabin's two symbols, expressly not additional relations; later definitions of (\mathfrak N_n), subtree, and applications require the distinction. |
| Path | Reader 969–971 gives the root, unique-child, and predecessor clauses. | A path is a node set, not a run or word automaton; ordinary and dual acceptance and the formula encoding use it. |
| Transition table, automaton, and run | Reader 974–1005 gives the distinct tuples, transition type, run map, and acceptance data. | Their standings differ: a table supplies moves, an automaton adds initial/designated data, and a run is a state map. That distinction is later indispensable to ordinary acceptance, Theorem 3.1, and dual acceptance. |
| Principal formula | Reader 1048–1061 supplies the exact formula schema and suffix/member types. | It is a formula family, not an automaton or new primitive; it differs from an arbitrary matrix by its displayed finite witness form and is used by Corollary 3.13 and Theorem 1.7. |
| Deterministic Muller word automaton | Reader 1114–1121 types (\langle U,K,u_0,H\rangle), (K), and (H). | It is a word automaton, not Rabin's tree automaton; determinism supplies one coherent first-coordinate history in the later (U\times S) product. |
| Type, type-empty, and dual acceptance | Reader 1143–1188 gives exact set/range/recurrence clauses and the (\forall r\exists\pi) semantics. | These are path-map predicates and a relation among a table, pair sequence, state, and valued tree. They differ from ordinary (F)-acceptance and are used only in complement/emptiness constructions. |
| Marked tree | Reader 1218–1225 defines the augmented label at every node. | It is a valued tree over an augmented alphabet, not a new underlying tree; simultaneous local obligations require the added finite marker set. |
| Well-founded mapping | Reader 1227–1233, detailed note 421–431, and compact record 668 state the need to exclude endless deferral and the exact no-infinite-chain definition for (h\mapsto H_h\subseteq H). | It is a dependency mapping among obligations, not path acceptance or the simultaneous-run merge; Lemmas 3.3, 3.4, and 3.11 require precisely that distinction. |
| Frontier, frontiered, and external (f) | Reader 1259–1287 and detailed note 307–320 define the frontier and both-child property at first use, explain why predecessor closure is weaker, and type (f\notin S). | The frontier is a node set; “frontiered” is a property of (E), not another tree; (f) is an external frontier value, not a state. Finite automata, the lift, complement base, and emptiness base use those differences. |
| Restricted table | Reader 1343–1351 defines (N_{R'}(s)=N(s)\cap(R'\times R')). | It remains a table on the formal state set (R); only states below the root are restricted. The root-boundary distinction is used in the shorter-sequence reduction. |
| (\Omega^\dagger) | Reader 1190–1213 gives the necessity (Lemma 3.6 may enumerate no pairs), exact one-pair definition, empty path language, and semantic equality with the empty sequence. | It is a handbook-owned pair sequence, not a new acceptance semantics; unlike the empty list it lies in the source's positive-length induction, where it is subsequently used. |

I found no introduced name whose sole role was to suggest an unproved object. Where the source argument owed a repair—zero-length normalization and the two empty witness branches—the manuscript describes and proves the exact artifact rather than inventing an unexplained primitive.

## Adversarial boundary and edge-case checks

### Ordinary versus dual

The ordinary tree automaton is (\langle S,M,S_0,F\rangle), (F\subseteq\mathcal P(S)), and accepts by one run satisfying every path. The dual object starts from a table, state, and pair sequence and universally quantifies runs before existentially choosing a path. The no-run case is therefore false for ordinary acceptance and vacuously true for dual acceptance. Reader 1007–1013 and 1167–1188 state all three differences. Neither source note nor compact record reuses Ω as ordinary (F).

### Finite versus infinite; weak versus full

The finite-tree object at reader 1259–1283 is finite, predecessor closed, and fully binary off its frontier; its valuation omits frontier nodes and its run uses external (f). Lemmas 3.12 and 3.14 have different roles. The weak monadic theorem enters only to decide existence of finite base witnesses in the source's emptiness recursion. Reader 1392–1400 expressly denies that this makes the original infinite input finite or converts full (S2S) quantification to weak quantification.

### Empty pair list, empty (H), and empty (U_0)

The three edge cases are not conflated:

1. (k=0) is normalized by the semantically equivalent (\Omega^\dagger) before positive-length induction (reader 1190–1213, 1340–1342).
2. For (k>1) with (L_k=\varnothing), (H=\varnothing) is the direct shorter dual question; nonempty (H) uses the restricted table (reader 1361–1371).
3. At (k=1), (m=0) and (U_0=\varnothing) express a finite no-run obstruction, equivalent by König's lemma to no infinite run (reader 1373–1389).

The detailed note additionally supplies concrete finite-table counterexamples showing why the two printed “nonempty” clauses are not exhaustive (note 487–508). The reader accurately labels all three completions as handbook-owned rather than attributing them to Rabin.

### Decidability versus complexity; source versus later source

Rabin printed p. 1 and p. 4 make the historical elementary-recursive claim. Meyer printed pp. 478–479 gives the later tower lower-bound form and lists the two-successors-and-prefix theory with Meyer/Stockmeyer credit. Since that theory is a sublanguage of the displayed binary structure, the reader's inference against Rabin's worst-case claim is valid. It does not infer undecidability or ineffectiveness. McNaughton's word result and Thomas's later basis-theorem route are separately attributed and not laundered into the 1969 article.

### Proof reconstruction versus proof outline and completion scope

Reader 1423–1430 states the reconstructed components and leaves every detailed transition table and induction in the complete article. The complement account does not reduce the proof to the phrase “transfinite complementation”: it names the finite marked-tree machinery, path product, exact well-founded mapping, two half-steps, and positive-length induction, and confines transfinite induction to Lemmas 3.3 and 3.11. This is a fair scholarly reconstruction rather than a claim to reproduce every proof line.

### Rights and publication language

The custody cover, note 87–93, and compact record use public access only as research custody. No frozen record calls the scans open content or makes them handbook assets. The one publication-language failure is `AP7-01`: an obsolete internal round number in the detailed note. I found no broader claim of final admission, final typesetting, Part IX completion, book completion, or user acceptance.

## Verdict scope

The must-fix finding concerns agreement and truthful pending-review status in this exact hash-pinned six-object snapshot. It does not negate the source-faithful mathematical work that passed R01–R23 and R25–R29, and it does not assess any artifact outside the charter's evidence set. Nevertheless, R24 is mandatory, and a frozen record that points to an already rejected prior round cannot support publication admission. This Round 7 snapshot therefore cannot be accepted unchanged.

VERDICT: REJECT — AP7-01
