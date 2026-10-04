# Part VIII admission audit — R1 source-fidelity/evidence seat

Date: 2026-08-21  
Mode: blind opening review, current live tree, read-only except for this transcript  
Decision scope: source/content only; provenance admission, build, rendered-page, human, and user gates remain independent

I did not read another Part VIII seat transcript. I did not run a TeX/PDF build, a test suite, or a generated-file writer. Exact locations below refer to the live snapshot whose two route hashes are:

- `handbook/parts/p08.tex`: `ffdbd4d341674cd6fb1fb5a95363dcd90692df4a2d6313c01e18dfa3e0e43784`
- `handbook/annex/p08.tex`: `656ce366ac816baa0cd53c2b4f0bcea0a90b0f77826c982095d7b32b673532c9`

The source/content decision is **REJECT**. The exact inherited corpus is clean, but the current reader graph is not admissible because it prints OPEN debt, gives several inherited sketches incompatible system-card standing while suppressing their governed annex routes, makes false literal-slice/derivative-lineage claims, lacks anchors for seven exact inherited results, introduces unregistered and in one case deliberately underdefined notation in P8.4/P8.7, and does not deliver several must/should registered P8.4 and P8.7 units. The literal register and presentation-admission projections also remain wholly open; I report those separately rather than treating a static or source-content check as their substitute.

## Exact inherited preservation — checked clean

`handbook/parts/p08.tex:2-46` routes exactly forty restoration wrappers. Their source intervals, in reader order, are:

```text
SRC-12970-12988  SRC-12989-13045  SRC-13046-13057  SRC-13058-13099
SRC-13100-13127  SRC-13128-13140  SRC-13141-13157  SRC-13158-13179
SRC-13180-13200  SRC-13201-13213  SRC-13214-13254  SRC-13255-13284
SRC-13285-13316  SRC-13317-13339  SRC-13340-13409  SRC-13410-13439
SRC-13440-13471  SRC-13472-13478  SRC-13479-13518  SRC-13519-13551
SRC-13552-13564  SRC-13565-13583  SRC-13584-13613  SRC-13614-13640
SRC-13641-13699  SRC-13700-13730  SRC-13731-13774  SRC-13775-13788
SRC-13789-13806  SRC-13807-13861  SRC-13862-13896  SRC-13897-13918
SRC-13919-13938  SRC-13939-13971  SRC-13972-14000  SRC-14001-14015
SRC-14016-14034  SRC-14035-14051  SRC-14052-14068  SRC-14069-14094
```

I compared every artifact line to `source/formal-logic-reference.tex` at the recorded inclusive interval, rather than trusting provenance metadata alone. Result: 40/40 intervals; exactly source lines 12970 through 14094; 1,125 lines; zero gaps, overlaps, reorders, duplicate intervals, line-count mismatches, or content mismatches. All forty `handbook/restoration/scope-SRC-*.tex` wrappers and all forty corresponding `spec/provenance/SRC-*.json` records exist. The two-root recursive graph contains 91 reachable files and 68 live labels; no input is missing and no live label is duplicated. No exact artifact is routed twice.

The inherited-unit control is nevertheless not admitted: all 66 P8 unit rows from `spec/source-unit-audit-crosswalk.csv:862-927` still say `provenance_disposition=open/missing`, `audit_result=pending/unclassified`, and `source_fidelity_ai_verification=pending`, although their static field is `pass`. That is an external control disposition, not a contradiction of the line comparison above.

## Findings

### F1 — Major — no current reader source map; the available audit map is historical, not the live route

**Location.** `handbook/parts/p08.tex:1-49`; `spec/inherited-source-map.csv:198-237`; `spec/provenance/SRC-12970-12988.json:30-50,98-108`; `spec/provenance/SRC-14069-14094.json:31-51,82-108`.

**Claim.** The reader moves immediately from the driver comment to forty exact inputs and interleaved supplements. Nothing visible tells a reader which surfaces are exact inherited source, which are edited descendants of former handbook files, which are wholly new editorial additions, or which proof statuses are inherited. The repository does contain an inherited-source audit map and exact-interval provenance records, but the audit map is a pre-restoration defect ledger: its first P8 row still says to restore 12970--12988 and its last still says 14069--14094 is omitted. It is therefore evidence of the restoration obligation, not a current reader-source map.

**Evidence.** The exact driver order is clean, but the route itself supplies only `\input` statements. The global map's stale snapshot locators point to now-unreachable monoliths such as `handbook/parts/p08/intuitionistic-and-intermediate.tex`, while the live route uses exact wrappers plus `*-supplement.tex` files. The full-transcription contract requires source identity, exact locator, presentation identity, disposition, completeness coverage, and separated variants for every substantive unit (`spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md:86-100`).

**Exact correction.** Before the first exact wrapper, print an ordinary reader source map that (1) identifies the frozen authority, (2) gives the forty exact intervals in route order, (3) names every interleaved editorial file and its source/presentation standing, and (4) distinguishes exact source, historical derivative, and new editorial content. Either regenerate a current live-route projection from the historical audit map or label the latter unambiguously as historical so it cannot be mistaken for current reachability.

**Status.** OPEN.

### F2 — Blocker — reader-visible OPEN/internal-administration prose remains live

**Location.**

- `handbook/parts/p08/intuitionistic-supplement.tex:1-17`
- `handbook/parts/p08/modal-logics-supplement.tex:1-19`
- `handbook/parts/p08/temporal-epistemic-supplement.tex:1-18`
- `handbook/parts/p08/many-valued-supplement.tex:1-18,187-200,482-490`
- `handbook/parts/p08/relevance-linear-supplement.tex:1-18`
- `handbook/annex/p08/many-valued-supplement.tex:1-18`
- `handbook/parts/p08.tex:50-52`

**Claim.** Five body supplements and the routed annex supplement identify themselves to readers as “OPEN additions”; the many-valued body prints named open register rows and “OPEN annex targets”; the Part driver leaves the generated audit unrouted under an OPEN comment. These are not ordinary scholarly qualifications. They expose migration/admission state on the final reader route.

**Evidence.** The charter expressly requires “no reader OPEN/stub/owed/internal-row prose” (`board-part8-admission-2026-08-21/charter.md:11-16`). No live `\hbstub` remains, but the literal OPEN prose above is sufficient to violate the invariant.

**Exact correction.** After source/content repair, replace the printed OPEN notices with ordinary attribution and precise proof/source standing. Delete internal row IDs and admission language from reader prose. Keep unresolved administrative, build, visual, human, and user states solely in the control ledgers.

**Status.** OPEN.

### F3 — Blocker — several “historical slice” and derivative-lineage assertions are false or unauditable

**Location.** `handbook/parts/p08/intuitionistic-supplement.tex:1-14,19-564`; `modal-logics-supplement.tex:1-15,21-1004`; `temporal-epistemic-supplement.tex:1-15,20-693`; `many-valued-supplement.tex:1-15,20-499`; `relevance-linear-supplement.tex:1-14,20-696`; `handbook/annex/p08/many-valued-supplement.tex:1-12,18-97`. The compared retained antecedents are the byte-pinned but unreachable files `handbook/parts/p08/intuitionistic-and-intermediate.tex`, `modal-logics.tex`, `temporal-dynamic-epistemic.tex`, `many-valued-and-fuzzy.tex`, `substructural.tex`, and `handbook/annex/p08/many-valued-and-fuzzy.tex`.

**Claim.** Headers say each supplement is “exactly” the marked historical slices/derivatives with only displayed consumer/source-status corrections. Some ranges marked `HISTORICAL SLICE`, which semantically claims literal preservation, are not literal. Derivative ranges also lack a machine-auditable enumeration of transformations, and three wholly new routed files (`conditionals-deontic-free.tex`, `paraconsistent-and-nonmonotonic.tex`, and `further-reading.tex`) have no per-file external-presentation provenance header or admitted packet.

**Evidence.** Direct line comparison gives:

| Current marker | Current evidence | Retained antecedent evidence | Result |
|---|---|---|---|
| intuitionistic `SLICE 149-165` | `intuitionistic-supplement.tex:73-74` | `intuitionistic-and-intermediate.tex:161-162` | apparatus text removed; not literal |
| intuitionistic `SLICE 175-191` | `intuitionistic-supplement.tex:95` | `intuitionistic-and-intermediate.tex:189` | apparatus text removed; not literal |
| modal `SLICE 358-607` | `modal-logics-supplement.tex:334-335,391-394,462,514` | `modal-logics.tex:383-384,440-443,511,563` | multiple changed captions/rows; not literal |
| relevance `SLICE 125-145` | `relevance-linear-supplement.tex:35` | `substructural.tex:139` | apparatus text removed; not literal |
| relevance `SLICE 453-715` | `relevance-linear-supplement.tex:337` | `substructural.tex:531` | apparatus text removed; not literal |
| relevance `SLICE 716-866` | `relevance-linear-supplement.tex:577,607,627-628,665-668` | `substructural.tex:768,798,818-819,856-859` | multiple rewrites; not literal |
| relevance `SLICE 874-894` | `relevance-linear-supplement.tex:679-695` | `substructural.tex:874-894` | 17 lines replace 21 and remove the old stub/row wording |

Even the correctly named derivatives are not bounded merely by the printed old interval: current/antecedent line counts are 38/39 for intuitionistic 90--128, 322/286 for intuitionistic 396--681, 442/441 for modal 610--1050, 184/165 for temporal 610--774, 427/390 for many-valued 180--569, and 27/26 for relevance 398--423. Such changes may be legitimate editorial work, but “only the displayed” corrections are not an auditable provenance record. `spec/presentation-packet-admission.md:1-20` currently reports zero packet files and zero admitted packets.

**Exact correction.** Rename every altered `SLICE` marker to `DERIVATIVE`; for each derivative record the antecedent file hash, exact old interval, current destination/labels, and an exhaustive transformation list or content projection. Give wholly new files an authoritative presentation/source-role record. Do not retain “exactly” or “only” claims unless a literal comparison passes. Bind the admitted packet or equivalent provenance record before calling the addition complete.

**Status.** OPEN.

### F4 — Blocker — inherited source sketches are relabelled as citations and their governed annex routes are suppressed

**Location.** Exact inherited results and sketches:

- IPL: `handbook/restoration/inherited-13058-13099.tex:11-41`
- K/T/S4/S5: `handbook/restoration/inherited-13285-13316.tex:1-31`
- LTL: `handbook/restoration/inherited-13440-13471.tex:1-31`
- multi-agent S5: `handbook/restoration/inherited-13519-13551.tex:1-18`
- IMLL: `handbook/restoration/inherited-14001-14015.tex:1-14`

Conflicting active cards are at `handbook/parts/p08/intuitionistic-supplement.tex:20-39`, `modal-logics-supplement.tex:67-84,104-121,155-172,222-239`, `temporal-epistemic-supplement.tex:20-40,466-485`, and `relevance-linear-supplement.tex:228-248`. The annex suppression claim is `handbook/annex/p08.tex:3-8`; the governed but unreachable sketch bodies are `handbook/annex/p08/intuitionistic-and-intermediate.tex:12-35`, `modal-logics.tex:3-49`, `temporal-dynamic-epistemic.tex:4-50`, and `substructural.tex:5-48`.

**Claim.** The exact reader source honestly prints “Proof sketch.” The frozen status map requires these five adequacy families to remain `sketched=annex:...` if migrated (`spec/research/p08-new-content.md:144-175`, especially lines 153-161 and 175; modal reiteration at lines 405-415; IMLL control at `spec/research/p08-8.6-evidence.md:28-37,80-88,642-689`). The active system cards instead use `cited=...`, even while several say that the exact inherited source contains the inline sketch. The annex driver then says the historical annex files supply “no distinct governed addition.” That claim is false: those annexes enumerate omitted Lindenbaum, existence, truth-lemma, filtration, eventuality, residuation, and cut-reduction obligations that are not enumerated in the exact inline source.

**Evidence.** The generated audit correctly recovers the inherited standing—`handbook/generated/audit-p08.tex:19,47,49,51,132` prints these results as `sketched`—while the cards present a different status. In particular, `relevance-linear-supplement.tex:239-242` uses `cited=Girard1987` for the exact commutative-residuated-pomonoid theorem, although the inherited source itself uses Girard only for the broader classical calculus/origin statement at `inherited-14001-14015.tex:13-14`. Girard's primary paper is [Linear Logic, DOI 10.1016/0304-3975(87)90045-4](https://doi.org/10.1016/0304-3975(87)90045-4); no exact locator is supplied for the card's algebraic theorem.

**Exact correction.** Preserve the source theorem as `sketched`, create non-invasive wrapper anchors, and route one faithful annex item for each of IPL, K/T/S4/S5, LTL, S5-I, and IMLL, with the omission lists required by the frozen controls. A separately stated externally cited theorem may remain cited, but it must not overwrite the inherited theorem's source standing or borrow its title without a presentation-specific locator.

**Status.** OPEN.

### F5 — Major — seven exact inherited results have no stable anchors; the generated audit is live but unrouted under a stale reason

**Location.** Unanchored exact results: `handbook/restoration/inherited-13046-13057.tex:1-12`, `inherited-13058-13099.tex:11-41`, `inherited-13285-13316.tex:1-31`, `inherited-13440-13471.tex:1-31`, `inherited-13519-13551.tex:1-18`, `inherited-13641-13699.tex:1-59`, and `inherited-14001-14015.tex:1-14`. Generated symptoms: `handbook/generated/audit-p08.tex:15-20,44-52,107,132`; stale route statement: `handbook/parts/p08.tex:50-52`; generator implementation: `tools/audit_tables.py:52-74,169-184,408-412`.

**Claim.** Persistence, IPL adequacy, modal four-system adequacy, LTL adequacy, multi-agent S5 adequacy, finite-matrix tableau adequacy, and IMLL adequacy are exact named theorem-class units but have no label because exact artifacts cannot be edited. The audit therefore renders their IDs as `--`, and the named-result index cannot retrieve them. The driver says `audit-p08` scans retained historical files; current `reachable_part_files` demonstrably walks only the live `p08.tex` input graph, so that reason is stale.

**Evidence.** The audit rows at lines 17, 19, 47, 49, 51, 107, and 132 carry the right titles/statuses but no links. The current generated file hash is `3c9ce5e4e0a7a8f5803dcbece9846abcb19991f349dc280b759906f3fd407f02`. Forty-four already anchored P8 theorem results appear in the named-result index; these seven do not. The generator intentionally withholds system cards because there is no packet-admission input (`tools/audit_tables.py:408-412`), which is a separate control boundary and not evidence that the theorem/definition audit is unreachable.

**Exact correction.** Add wrapper-level anchors/hooks immediately adjacent to the seven exact environments without changing inherited bytes. Make the generated audit and named-result index consume those hooks. Route `handbook/generated/audit-p08.tex` after source/content admission, and replace the false driver comment with the actual packet-admission boundary for system cards.

**Status.** OPEN.

### F6 — Blocker — P8.4 and P8.7 introduce unregistered, colliding, and underdefined notation

**Location.** `handbook/parts/p08/conditionals-deontic-free.tex:7-17,47-66,77-96,109-123`; `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:12-19,46-64,86-104,109-135`; registry baseline `handbook/registry/symbols.csv:1,217-218`; generated surfaces `handbook/generated/symbols-tables.tex` and `symbol-index.tex`.

**Claim.** The registry has 131 rows whose scope contains P8, and every one is present in both generated symbol surfaces, but there is no P8.4- or P8.7-scoped row. The live files newly use at least (D_E), (OA), permission (PA), dyadic (O(A\mid B)), (f(w,A)), (A>B), (A\Box\!\!\to B), probability (P(A))/(P(B\mid A)), defeasible consequence \(\mathrel{|\!\sim}\), AGM (K*A)/(K-A), default notation, and circumscription parameters. The same bare (P) is permission at lines 49-54 and probability at lines 109-123. The dyadic-obligation paragraph explicitly admits that no ordering/neighborhood clause has been fixed, so the notation names an owed artifact rather than a defined semantics.

**Evidence.** Existing rows at `symbols.csv:217-218` register the P2.4 outer/inner-domain notation (D,D^{\mathrm{in}},D^{\mathrm{out}}) and (E!(t)), not the new (D_E). Searches of the registry and both generated symbol surfaces find none of the P8.4/P8.7 roles above. This violates both the charter's definitions-before-use/syntax invariant (`charter.md:11-14`) and the frozen five-part technical-name gate (`spec/research/p08-new-content.md:53-59`).

**Exact correction.** Either reuse the already governed free-logic notation or register the new typed variant and explain the distinction. Register every remaining symbol with exact operand types, scope, precedence, standing, and collision notes; separate permission from probability typographically or by an explicit local typed convention. For (O(A\mid B)), supply the exact selected semantics/calculus and source, or remove the notation and state the owed artifact without naming a hypothetical formal answer.

**Status.** OPEN.

### F7 — Blocker — the live P8.4 chapter does not meet its registered deontic/conditional scope

**Location.** Register authorities: `spec/registers/new-content.csv:85,88-90`; `spec/registers/depth-gaps.csv:121-122`; `spec/registers/apparatus.csv:90-94`. Live chapter: `handbook/parts/p08/conditionals-deontic-free.tex:45-73,75-105,107-126`.

**Claim.** The chapter gives a useful SDL definition, Chisholm paragraph, Stalnaker/Lewis semantic contrast, and Adams/Lewis survey. It does not deliver the registered unit at its declared ceiling:

- N-b-013/D-P10-037/A-090 require Ross, Good Samaritan/gentle-murder, Chisholm, and a dyadic semantics. Only Chisholm is treated, and lines 63-66 explicitly leave dyadic semantics unspecified.
- N-b-016/D-P10-038/A-089 require C1/VC completeness statements and the system comparison. Lines 77-105 give semantic clauses and selected failures but no C1 or VC calculus, statement/status, sheet, or table.
- N-b-017 requires the indicative-conditionals package with a statused triviality theorem at T level. Lines 120-126 give only a prose attribution under unspecified “strong assumptions”; the exact theorem and hypotheses are not stated.
- N-b-018 requires CK and neighbors, selection-function and premise semantics, and a correspondence table. None is present.

The free-logic variant table at lines 29-39 is substantive progress toward N-b-010/A-091; its presence does not discharge the independent rows above.

**Exact correction.** Supply the missing paradox formulations and diagnoses; select and define one dyadic obligation presentation; add exact C1/VC and CK-family cards/sheets/statused results at the registered ceilings; state Lewis triviality with its exact hypotheses and source locator; and add the A-089/A-090 comparison data. If a row remains intentionally outside P8, record a frozen supersession/exclusion rather than printing or silently implying completion.

**Status.** OPEN.

### F8 — Blocker — the live P8.7 chapter does not meet its registered paraconsistent/nonmonotonic scope

**Location.** Register authorities: `spec/registers/new-content.csv:98,104-105`; `spec/registers/depth-gaps.csv:119-120`; `spec/registers/apparatus.csv:93-95,104`. Live chapter: `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:10-42,44-82,84-105,107-143`.

**Claim.** The chapter accurately distinguishes paraconsistency from dialetheism and gives a concrete LP nonexplosion valuation; it also sketches System P/rational monotony and several nonmonotonic frameworks. The remaining registered content is not delivered:

- N-b-026 requires the inclosure schema and replies; lines 10-42 contain neither.
- N-b-032/D-P10-036/A-093 require the exact AGM postulate table, Levi and Harper identities, and representation results at T level. Lines 86-105 paraphrase the postulates, leave the two conjunction postulates unnamed, give Levi but omit Harper, and do not state a representation theorem with hypotheses.
- D-P10-035/N-b-033/A-092 require default logic, circumscription, and autoepistemic logic, including default/circumscription entry cards. Autoepistemic logic is absent. The live default and circumscription definitions are prose definitions, not the required cards; the circumscription sentence is described rather than displayed with its exact second-order quantifiers and fixed/varying-symbol parameters.

**Exact correction.** Add the source-scoped inclosure schema/reply survey; print the exact AGM postulates, both identities, and a statused representation statement; add the missing autoepistemic unit; and provide exact default/circumscription cards and formulas at the registered ceiling. Keep framework-specific hypotheses explicit rather than transferring System P, AGM, default, or circumscription results across presentations.

**Status.** OPEN.

### F9 — Major — three point-of-use source roles are too broad for the cited evidence

**Location.** `handbook/parts/p08/intuitionistic-supplement.tex:319-337`; `many-valued-supplement.tex:276-303,305-323`; `relevance-linear-supplement.tex:228-248`; bibliography records `handbook/bib/handbook.bib:223-231,4360-4376,4763-4774,5414-5435`.

**Claim and evidence.**

1. The BHK definition puts one citation cluster after all six modern packaged clauses. The frozen research control expressly says not to attribute the modern acronym or every clause to Brouwer 1908 (`spec/research/p08-new-content.md:249-257`). Brouwer's primary 1908 paper is about the reliability of logical principles, especially excluded middle, not a source locator for the full later BHK clause package: [publisher record and translation](https://doi.org/10.1016/B978-0-7204-2076-0.50009-X). The live prose correctly calls BHK a metalinguistic abbreviation, but its citation scope still needs splitting.
2. The Bochvar record supports the three-valued calculus/external operators; the primary paper is [Bochvar, 1938, MathNet](https://www.mathnet.ru/eng/sm5749), and the bibliography correctly records the 1981 English translation. It is not, without a precise locator, evidence for the handbook's generic value-labelled tableau. `thm:p08-bochvar-tableau` is an editorial specialization of the exact generic finite-matrix theorem and sheet, so citing Bochvar as the theorem's entire standing conflates source definition with local derivation.
3. The IMLL card's `cited=Girard1987` problem is described in F4: the evidence package and exact inherited source assign the exact algebraic adequacy/cut result sketch standing, while Girard is the broader classical-linear source.

`thm:p08-post-matrix` has the same smaller role-boundary issue: exhaustive finite-matrix decidability at lines 317-319 is a local elementary consequence, while Post 1921 is the source for the operations/generation claim. Its two roles should be separated rather than represented by one undifferentiated `cited=Post1921` status.

**Exact correction.** Split historical, definition, and theorem roles at point of use. Put Brouwer only on the historical/excluded-middle boundary and Heyting/Troelstra--van Dalen on the packaged explanatory clauses with exact locators. Cite Bochvar on the language/matrix; prove the tableau specialization locally from the exact generic theorem or cite a source that proves that exact tableau. Split Post decidability (`derived`/local proof) from Post generation (`cited`). Restore IMLL to inherited sketch standing.

**Status.** OPEN.

### F10 — Admission-control boundary — every literal P8 register projection remains OPEN and unbound

**Location.** `spec/register-obligation-closure.csv:26,85-122,214-246,318-321,346-516`; representative rows include D-P10-001 at line 85, D-P10-038 at line 122, N-b-001 at line 214, N-b-033 at line 246, A-070 at line 397, A-089--A-094 at lines 416-421, A-165 at line 492, A-182 at line 509, A-186 at line 513, and A-189 at line 516. Packet projection: `spec/presentation-packet-admission.md:1-20` and the header-only `spec/presentation-packet-admission.csv`.

**Literal disposition.** The following current P8-linked rows all say `manifest_binding_disposition=open`, `completion_status=OPEN`, empty `handbook_unit_ids`, empty `presentation_packet_ids`, empty `destination_labels`, and pending review/build/visual fields:

- **35 depth rows:** D-P3-008; D-P10-001--009; D-P10-011--021; D-P10-023--030; D-P10-032--033; D-P10-035--038.
- **30 new-content rows:** N-b-001--018; N-b-025--033; N-x-006, N-x-007, N-x-009.
- **42 P8 apparatus rows:** A-019, A-020, A-070, A-076--A-094, A-100, A-103, A-123, A-136--A-147, A-153, A-165, A-182, A-186, A-189.

The three N-x rows are frozen exclusions, so their open state is an unrecorded exclusion/supersession decision, not evidence that quantum, adaptive, or formal-argumentation content must be added to Part VIII. Conversely, several apparatus rows already have visible content—e.g. A-091's free-logic comparison and A-186's further-reading chapter—but the literal closure ledger has not bound or admitted it. Presence is not admission. There are currently zero presentation packet files and zero independently admitted packets.

**Exact correction.** For every substantively completed row, bind exact live unit IDs, destination labels, source/presentation packet, and independent evidence. For frozen exclusions, record the governing supersession/exclusion contract. Leave genuinely incomplete rows OPEN. This boundary must not be promoted by this source-content review; it remains independent under `charter.md:14-16` and `spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md:167-195`.

**Status.** OPEN, explicitly external to the source/content verdict except where F7/F8 identify substantive non-delivery.

## Checked-clean source and apparatus surfaces

- **No duplicate or altered inherited unit:** forty exact intervals, 1,125 source lines, strict order, exact line equality, one live route each.
- **Calculus-sheet identity:** 36 distinct live `sheet:*` references; every target file exists under `handbook/registry/calculi`, and each file declares the matching sheet ID. I inspected the high-risk LJ/modal/temporal/epistemic/matrix/relevance/IMLL/CLL/Lambek surfaces for source-role and side-condition drift; no additional source-fidelity blocker was established beyond F4/F9.
- **Currently routed proved-annex reciprocity:** the seven K3/LP/FDE adequacy/decision and K3--LP duality targets in `handbook/parts/p08/many-valued-supplement.tex:20-169` match exactly seven reachable annex items in `handbook/annex/p08/many-valued-supplement.tex:19-96`; no active proved target is missing or orphaned. This clean result does not cure the suppressed inherited sketch annexes in F4.
- **Bibliographic existence:** 114 distinct citation/entry-source keys occur on the reachable body/annex graph; all 114 have a BibLaTeX record. The defects in F9 concern claim-to-source role and locator, not missing keys.
- **Existing generated symbol fidelity:** all 131 registry rows whose scope contains P8 occur in both `handbook/generated/symbols-tables.tex` and `handbook/generated/symbol-index.tex`. F6 concerns live notation for which no row exists.
- **Generated retrieval:** the current audit is reachability-backed, and labeled audit targets resolve in the live graph. Forty-four anchored P8 named results are present in `handbook/generated/named-theorem-index.tex`; only the seven exact unanchored results in F5 remain unavailable there.
- **Kamp source boundary:** `handbook/parts/p08/temporal-epistemic-supplement.tex:398-430` uses the prefix convention in which the first U/S operand holds at the witness and the second throughout the intervening interval, restricts the converse expressive-completeness direction to Dedekind-complete chains, and reserves arbitrary linear orders for Stavi operators. This agrees with Kamp's thesis identity in the [Hans Kamp institutional archive](https://www.ims.uni-stuttgart.de/archiv/kamp/bibliography.html) and the standard published convention; the bibliography's `@thesis` role at `handbook/bib/handbook.bib:2085-2090` is correct.
- **Dated verification evidence not promoted:** the three 2026-08-17 P8 visual records (`spec/verification/restoration-visual-evidence-part8-lines-12970-13200-2026-08-17.md:1-15`, `...13201-13583...md:1-15`, and `...13584-14094...md:1-15`) are candidate-bound and explicitly leave whole-publication/semantic/user acceptance OPEN. They support the historical exact-source tranches only; they are not a current final-PDF or source/content admission.

## Four-lot coverage

1. **Lot 1 — checked, not clean.** Exact IPL/intermediate source, negative translations, algebraic/topological semantics, BHK/realizability boundary, IQC, live cards/sheets/citations, and related apparatus were checked. Blockers/residuals: F1--F6 and F9; exact inherited bytes themselves are clean.
2. **Lot 2 — checked, not clean.** Normal/non-normal modal systems, correspondences, filtration/bisimulation, actuality/QML/Barcan material, all active modal sheets, source roles, and exact modal source were checked. Blockers/residuals: F1--F5 and the literal control boundary F10; no additional modal claim/source blocker was established.
3. **Lot 3 — checked, not clean.** LTL/CTL/CTL-star/mu-calculus, automata, tense/Kamp, epistemic/common knowledge/PAL/hybrid, conditionals/deontic/free logic, sheets, citations, and routes were checked. Blockers/residuals: F1--F7, F9, and F10. Kamp's convention and order hypothesis are checked clean.
4. **Lot 4 — checked, not clean.** Many-valued/fuzzy/supervaluation, relevance/linear/Lambek, paraconsistent/nonmonotonic, routed annex, sheets, comparison apparatus, bibliography, audit/named/symbol surfaces, and further-reading route were checked. Blockers/residuals: F1--F6 and F8--F10. The seven currently routed many-valued annex pairs are clean.

**Explicitly not checked/promoted:** no TeX/PDF build, generated-file rewrite, visual inspection of a current final PDF, human review, user acceptance, or whole-corpus acquisition audit was performed. This seat did not independently re-prove every externally cited theorem; it checked exact inherited correspondence, source/presentation roles, targeted primary/authoritative boundaries, proof-status honesty, and the complete current Part VIII route. Those unperformed gates remain separate and cannot be inferred from this verdict.

REJECT
