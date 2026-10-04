REJECT

# Part IX admission board, blind round 1: source-fidelity/evidence seat

Author: source-fidelity/evidence seat  
Mode: independent source/content review of the current live Part IX route; no other Part IX seat transcript or conclusion read  
Scope: the graph rooted at handbook/parts/p09.tex and handbook/annex/p09.tex, its cross-part imports, current bibliography, calculus registry, symbols, generated theorem/audit retrieval, and every P9 register ceiling  
Forbidden work observed: no manuscript/spec/tool/generated-source edit, no test, and no TeX/PDF build

## Snapshot and verdict

The bytes reviewed were:

| Live file | Lines | SHA-256 |
|---|---:|---|
| handbook/parts/p09.tex | 3 | a414f249cb2d46013d902176d09bbd11a176551775929f2837d62dab4fc3b0d1 |
| handbook/parts/p09/logic-in-computer-science.tex | 442 | c52cd51a24b1e878b4cbe9a4c0a9d7e881703677233bccd67eb08afab315763b |
| handbook/annex/p09.tex | 17 | 7d47d9ec73b8199f478844de3cfd5e3e095932c929d8215c85f5cfacc86491ef |
| handbook/generated/audit-p09.tex | 32 | 12f8a37d62a0dc1bf60e6aad2303f76d6227e4b57f858b6a9abb893b5aafb60f |

Part IX is **not source/content admissible on this snapshot**. The decisive reasons are not the later build or provenance gates: the reader currently prints a false-scope zero--one theorem, assigns at least one theorem to the wrong source role, presents a body proof under cited status, and does not deliver several mandatory theorem, calculus, algorithm, and source ceilings. Those are present reader/source defects under the charter's invariants at board-part9-admission-2026-08-21/charter.md:7-17.

## Findings

### F1 [critical] [open] The mandatory P9 register is represented mainly by capsules, not by the contracted theorem/algorithm/calculus artifacts

Author: source-fidelity/evidence seat  
Location: spec/registers/new-content.csv:108-135; spec/registers/depth-gaps.csv:133-137; spec/registers/apparatus.csv:23-24,37,52-53,80,96-98; handbook/parts/p09/logic-in-computer-science.tex:11-435  
Claim: the live route does not meet every P9 ceiling at the registered treatment scale and source standing.  
Evidence: the line-by-line dispositions below distinguish an actually supplied cross-part artifact from a local capsule and from an absent deliverable. In particular, mandatory long or exposition-scale items N-c-009, N-c-016, N-c-019, N-c-022, and N-c-026 are not reconstructible at their registered ceiling; the required Hoare and SLD sheets and the P9 family/comparison tables are absent from the live calculus/table route. handbook/parts/p14/rule-sheets.tex:10-94 exhaustively renders the current calculus registry but contains no Hoare or SLD sheet.  
Exact correction: repair the substantive records identified below; route each supplied theorem, proof, algorithm, sheet, and table from the reader; attach exact statement-level sources; then update the administrative dispositions only after the content exists. Do not satisfy an E or T row by merely changing its CSV status.  
Discussion: N-x-015 is an honest exclusion, not a false completion claim. A-044, A-052, and A-079 have genuine cross-part reader artifacts. The remaining open rows are not all equally severe, but the mandatory exposition/calculus failures independently block admission.  
Disposition: source/content blocker.

#### New-content and exclusion ceilings

| Record | Current disposition | Current evidence / exact residual |
|---|---|---|
| N-c-001 | partial, open | handbook/parts/p09/logic-in-computer-science.tex:14-31 gives finite semantics and Trakhtenbrot, but omits the registered finite Craig/Beth failures and the EF method; handbook/parts/p03/finite-model-theory.tex:93-139 supplies compactness and points to EF material but P9 does not assemble the promised entry. |
| N-c-002 | defective duplicate, open | handbook/parts/p09/logic-in-computer-science.tex:33-59 duplicates the public P3 theorem and broadens it falsely; see F2. |
| N-c-003 | partial, open | handbook/parts/p09/logic-in-computer-science.tex:61-80 gives a definition-sized capsule, not separately statused Hanf and Gaifman results with exact normal-form/invariance hypotheses; see F3. |
| N-c-004 | content present | handbook/parts/p09/logic-in-computer-science.tex:82-100 correctly imports thm:p03-fagin and thm:p04-immerman-vardi; the ordered-structure qualification is preserved. |
| N-c-005 | open | handbook/parts/p09/logic-in-computer-science.tex:110-113 names two classes but supplies no prefix/reduction classification or table. |
| N-c-006 | partial/source-open | handbook/parts/p09/logic-in-computer-science.tex:107-110 states FO2 FMP/NEXPTIME in one sentence without the Mortimer source role or an exact language convention. |
| N-c-007 | partial/source-open | handbook/parts/p09/logic-in-computer-science.tex:108-110 says guarded decidability but does not state the registered modal correspondence or the Andreka--van Benthem--Nemeti source role. |
| N-c-008 | partial/source-open | handbook/parts/p09/logic-in-computer-science.tex:102-106 has a monadic capsule whose equality convention is described as something to be declared rather than actually fixed; Behmann's source role is absent. |
| N-c-009 | open | handbook/parts/p09/logic-in-computer-science.tex:118-164 lacks exact ABox/TBox satisfaction, a total tableau, and tableau correctness at T scale; see F4. |
| N-c-010 | open | handbook/parts/p09/logic-in-computer-science.tex:166-172 makes family-wide EL/DL-Lite prose claims with no variant/problem table; see F4. |
| N-c-011 | wrong source role, open | handbook/parts/p09/logic-in-computer-science.tex:138-144 assigns the Schild bridge to Schmidt--Schauß--Smolka; see F4. |
| N-c-012 | partial, open | handbook/parts/p09/logic-in-computer-science.tex:177-196 leaves past clauses “analogous” and omits the Gabbay--Pnueli--Shelah--Stavi result. |
| N-c-013 | partial, open | handbook/parts/p09/logic-in-computer-science.tex:198-216 has acceptance prose but not an automaton/run definition or separately scoped word/tree results. |
| N-c-014 | partial/source-open | handbook/parts/p09/logic-in-computer-science.tex:216-225 compresses BET, S1S, and S2S into prose and omits the Elgot, Trakhtenbrot, and Rabin source roles. |
| N-c-015 | pointer-scale text, source-open | handbook/parts/p09/logic-in-computer-science.tex:226-227 meets the requested pointer length but cites neither Thatcher--Wright nor Comon, so its transfer claim is not source-supported. |
| N-c-016 | partial, open | handbook/parts/p09/logic-in-computer-science.tex:229-255 gives two fixpoint equations but not the registered syntax, initialized total labelling algorithm, and correctness proof. |
| N-c-017 | partial, open | handbook/parts/p09/logic-in-computer-science.tex:269-278 is a useful boundary paragraph, but Bryant canonicity and the algorithmic claims remain unstatused prose. |
| N-c-018 | partial, open | handbook/parts/p09/logic-in-computer-science.tex:257-267 defines the binders but omits the alternation hierarchy and its registered sources. |
| N-c-019 | open | handbook/parts/p09/logic-in-computer-science.tex:289-330 has a status/proof contradiction, incomplete displayed calculus, no standard while-language semantics, and no worked example; see F6. |
| N-c-020 | partial, open | handbook/parts/p09/logic-in-computer-science.tex:332-349 gives heap splitting and the frame-rule shape but not command locality/semantics or frame-rule soundness standing. |
| N-c-021 | open | handbook/parts/p09/logic-in-computer-science.tex:280-284 is one survey paragraph, not the registered syntax, Segerberg calculus, completeness statement, and small-model theorem. |
| N-c-022 | partial, open | handbook/parts/p09/logic-in-computer-science.tex:354-377 gives a good least-model definition but no reconstructible SLD calculus or proved/cited adequacy theorem; see F7. |
| N-c-023 | partial/source-open | handbook/parts/p09/logic-in-computer-science.tex:379-396 defines the finite propositional reduct correctly, but its NP-completeness claim has no complexity source. |
| N-c-024 | partial, open | handbook/parts/p09/logic-in-computer-science.tex:398-404 gives the correct Chandra--Merlin containment direction, but replaces exact Datalog combined complexity by “strictly larger” and supplies no comparison artifact. |
| N-c-025 | meets pointer ceiling | handbook/parts/p09/logic-in-computer-science.tex:406-410 explicitly fixes the finite template, states the dichotomy boundary, and cites Zhuk. This does not purport to be a full CSP chapter. |
| N-c-026 | open | handbook/parts/p09/logic-in-computer-science.tex:431-435 has no labelled cross-references and imports only cited P4 TQBF, while the row expressly requires a QBF PSPACE proof; see F8. |
| N-c-028 | meets pointer ceiling | handbook/parts/p09/logic-in-computer-science.tex:274-278 gives the promised McMillan interpolation pointer with a source. |
| N-x-015 | honest exclusion, nonblocking | spec/registers/new-content.csv:186 deliberately excludes probabilistic/stochastic model checking beyond a pointer. The current qualitative chapter makes no false claim to complete that branch. |

#### Depth and apparatus ceilings

| Record | Current disposition | Evidence |
|---|---|---|
| D-P10-010 | content present across P8/P9 | The P8 system entries and A-079 table plus the P9 automata/model-checking discussion provide the qualitative bridge; no quantitative extension is inferred. |
| D-P11-006 | partial, open | SLD prose exists at handbook/parts/p09/logic-in-computer-science.tex:371-377; exact calculus, standardization-apart/mgu/answer conventions, and Prolog boundary are not supplied. |
| D-P11-007 | partial, open | ASP and Datalog are at handbook/parts/p09/logic-in-computer-science.tex:379-404, but exact complexity and the comparison apparatus remain absent. |
| D-P11-008 | partial, open | Hoare/separation prose is at handbook/parts/p09/logic-in-computer-science.tex:289-349; the rules table, exact calculus, soundness standing, worked example, and weakest-precondition table are not delivered. |
| A-022 | absent | No Hoare calculus is shown in handbook/parts/p14/rule-sheets.tex:10-94; the body prints only assignment and while shapes. |
| A-023 | absent | No SLD sheet is shown in handbook/parts/p14/rule-sheets.tex:10-94. |
| A-036 | partial | The global decision material does not supply the required four-fragment complexity/boundary table; P9 has only handbook/parts/p09/logic-in-computer-science.tex:102-113. |
| A-044 | content present | handbook/parts/p03/finite-model-theory.tex:111-132 is the finite/unrestricted comparison table. |
| A-051 | partial | handbook/parts/p14/master-tables.tex:11-50 and handbook/parts/p09/logic-in-computer-science.tex:415-429 are not a complexity disposition for every presented handbook logic. |
| A-052 | content present | handbook/parts/p04/complexity.tex:481-500 supplies the descriptive-complexity table with exact finite/order hypotheses. |
| A-079 | content present | handbook/parts/p08/temporal-dynamic-epistemic.tex:318-345 supplies the temporal comparison table with its finite explicit-structure convention. |
| A-095 | absent | No ALC-through-SROIQ/OWL reasoning-complexity table is routed. |
| A-096 | absent | No full Hoare/wp table with separation pointer is routed. |
| A-097 | absent | No SLD/completion/well-founded/stable/Datalog comparison table is routed. |

### F2 [critical] [open] The local zero--one theorem is false at its printed signature scope and duplicates the correct public theorem

Author: source-fidelity/evidence seat  
Location: handbook/parts/p09/logic-in-computer-science.tex:14-16,33-56; handbook/parts/p02/first-order-syntax-semantics.tex:23-33,69-73; handbook/parts/p03/finite-model-theory.tex:14-40; handbook/generated/named-theorem-index.tex:163-165  
Claim: “For every finite relational signature” at handbook/parts/p09/logic-in-computer-science.tex:52 is false under the handbook's live definition of signature.  
Evidence: P2 permits arity zero and explicitly writes a zero-ary relation as \(R\). In the finite signature containing just that nullary \(R\), the sentence \(R\) is true in exactly one of the two interpretations on every fixed nonempty universe, so its uniform asymptotic probability is \(1/2\), not \(0\) or \(1\). The correct public theorem already fixes a finite, purely relational, **positive-arity** vocabulary with no constants or functions at handbook/parts/p03/finite-model-theory.tex:14-20 and states thm:p03-fol-zero-one at :25-33. The generated named index exposes both the false-scope P9 identity and the correct P3 identity.  
Exact correction: delete the duplicate P9 theorem identity and cross-reference thm:p03-fol-zero-one, or make P9's local probability space explicitly exclude nullary relations, constants, and functions and still retain one public theorem identity. Preserve the P3 attribution to both Glebskii et al. and Fagin. [Fagin's publication record](https://ronfagin.com/papers/) identifies the 1976 zero--one-law paper; the decisive scope correction is already explicit in the live P3 statement.  
Discussion: this is a direct counterexample to a reader-visible theorem, not merely a missing citation.  
Disposition: source/content blocker.

### F3 [major] [open] Finite locality and classical decidable-fragment claims lack exact theorem variants and their controlling sources

Author: source-fidelity/evidence seat  
Location: handbook/parts/p09/logic-in-computer-science.tex:61-80,102-113; spec/registers/new-content.csv:108,110,112-115; spec/registers/apparatus.csv:37  
Claim: the prose does not establish the exact source-to-statement correspondence required for Gaifman/Hanf locality, the finite Craig/Beth and EF boundaries, or the prefix/FO2/guarded/monadic decision results.  
Evidence: “Every first-order formula has a Gaifman-local normal form” at handbook/parts/p09/logic-in-computer-science.tex:75 neither defines Gaifman's basic/scattered local sentences nor separates that normal-form theorem from Hanf equivalence; both are attributed only to textbooks. The finite Craig/Beth failures are absent. The fragment paragraph states no prefix forms, equality/function conventions per result, reduction classes, or decision-problem table. The declared monadic “equality convention” at :105 is not actually declared. Its two citations cover the two-variable and guarded discussions, but the registered controlling roles Hanf 1965, Gaifman 1982, Lewis 1979, Börger--Grädel--Gurevich 1997, Mortimer 1975, Andréka--van Benthem--Németi 1998, and Behmann 1922 are not attached to their respective statements, and several have no current bibliography record.  
Exact correction: (1) state Gaifman's normal form by defining the basic local/scattered sentence form; (2) state a separately scoped Hanf-equivalence/locality theorem with its radius/count threshold hypotheses; (3) cross-reference the existing finite EF material and state the finite Craig/Beth failures; (4) supply A-036 with one row per exact vocabulary/equality/function convention, decision problem, upper/lower bound, and undecidable boundary; (5) attach each primary/authoritative source to the record it controls.  
Discussion: textbook citations may support a survey sentence, but they do not make the unseparated theorem variants or missing table reconstructible.  
Disposition: source/content blocker as part of F1.

### F4 [critical] [open] The ALC correspondence has the wrong source role, and the tableau/family material does not reach its declared ceiling

Author: source-fidelity/evidence seat  
Location: handbook/parts/p09/logic-in-computer-science.tex:118-172; spec/registers/new-content.csv:116-118; spec/registers/apparatus.csv:96; handbook/bib/handbook.bib:2187-2195  
Claim: N-c-011 is not source-faithful, and N-c-009/N-c-010/A-095 remain substantively incomplete.  
Evidence: thm:p09-alc-modal at :138-144 is marked cited=SchmidtSchaussSmolka1991, while the frozen row explicitly assigns the ALC/multimodal-K correspondence to Schild 1991. Schmidt--Schauß--Smolka is the ALC concept-description/subsumption source, not the named correspondence source. [Schild's IJCAI record](https://dblp.org/rec/conf/ijcai/Schild91) is the fetchable authoritative record for *A Correspondence Theory for Terminological Logics*. The tableau at :146-164 omits negation-normal-form conversion, exact rule saturation/standard scheduling, complete clash/success conditions, model extraction, and soundness/completeness standing; its termination paragraph cannot by itself license “decision procedure.” ABox and TBox syntax is named, but satisfaction of either is not defined. The family paragraph at :166-172 transfers tractability/rewrite claims across “EL-family” and “DL-Lite families” without fixing a constructor set, reasoning/query problem, TBox regime, or complexity measure. No A-095 table is routed.  
Exact correction: add a verified Schild1991 bibliography record and make it the correspondence theorem's cited source; retain Schmidt--Schauß--Smolka only for the exact ALC reasoning role it supports. Define TBox/ABox satisfaction. Supply a terminating NNF blocking tableau as a total algorithm with explicit open/closed acceptance and a statused correctness theorem/proof. Replace the family prose by A-095, one exact logic/problem/complexity/source per row, including the OWL mapping only where the source supports it.  
Discussion: this finding applies the charter's prohibition on transferring a bound from one fragment to a whole family.  
Disposition: independent source/content blocker.

### F5 [critical] [open] Temporal, automata, model-checking, modal-mu, and PDL source boundaries are compressed past reconstructibility

Author: source-fidelity/evidence seat  
Location: handbook/parts/p09/logic-in-computer-science.tex:174-284; spec/registers/new-content.csv:119-125,128; handbook/parts/p08/temporal-dynamic-epistemic.tex:17-70,318-345; handbook/bib/handbook.bib:4711-4719  
Claim: the route does not supply exact syntax/semantics/acceptance/algorithm clauses and distinct source roles for the registered temporal and automata results.  
Evidence: past LTL is left to “analogous prefix clauses” at handbook/parts/p09/logic-in-computer-science.tex:183-184, although the GPSS expressiveness/adequacy source role is required and P8 already offers a public exact LTL system entry. The omega-automata definition at :198-209 never defines the automaton tuple, transition/run relation, initial condition, or word/tree type; BET finite words, S1S omega words, and S2S binary trees are then blended at :216-227. Rabin's S2S theorem is cited only through Buchi/Thomas, while the register assigns Rabin 1969; the [authoritative Rabin publication page](https://research.ibm.com/publications/decidability-of-second-order-theories-and-automata-on-infinite-trees) identifies the decision procedure for second-order theories via automata on infinite trees. The CTL equations at :242-255 omit least/greatest initialization, full syntax and acceptance/output, and the required correctness proof. The modal-mu entry omits alternation; Walukiewicz2000 is a completeness-of-Kozen-axiomatization record, not a substitute for the registered parity/alternation sources. PDL receives only :280-284, with no registered calculus or small-model theorem.  
Exact correction: reuse/cross-reference P8's single public LTL/CTL/CTL-star/mu systems rather than introduce partially overlapping local presentations. Give word and tree automata separate typed definitions and statused BET/S1S/S2S statements, with Elgot/Trakhtenbrot/Rabin attached to the exact variants. State a total CTL labelling algorithm (initialization, monotone iteration, termination, output) and route its correctness proof. Add the modal-mu alternation statement with its controlling source. Supply a PDL system entry and registered Segerberg/Kozen--Parikh sheet plus completeness/small-model statuses.  
Discussion: the P8 A-079 table at handbook/parts/p08/temporal-dynamic-epistemic.tex:318-345 is checked clean as a cross-part comparison; it does not repair the missing P9 algorithm and source roles without explicit public references.  
Disposition: source/content blocker as part of F1.

### F6 [critical] [open] Hoare soundness has a status/proof contradiction and depends on undisplayed rules and undefined semantics

Author: source-fidelity/evidence seat  
Location: handbook/parts/p09/logic-in-computer-science.tex:289-349; handbook/annex/p09.tex:14-16; handbook/CONVENTIONS.md:60-72; handbook/parts/p14/rule-sheets.tex:10-94; spec/registers/new-content.csv:126-128; spec/registers/apparatus.csv:23,97  
Claim: thm:p09-hoare-soundness cannot truthfully be both cited=Apt1981 and followed by a new reader proof; the proof is also not complete relative to a displayed calculus.  
Evidence: the status grammar says cited=<bibkey> means “statement only; source carries the proof” and requires new editorial proof material in the annex. The theorem at handbook/parts/p09/logic-in-computer-science.tex:309-313 is cited=Apt1981, but :315-322 prints an induction proof, and the annex expressly calls it “the induction proof” at handbook/annex/p09.tex:14-16. Only assignment and while are displayed at :300-305; consequence, sequence, and conditional are named but not shown, although both theorem and proof quantify over them. No syntax or operational/denotational semantics for the “standard deterministic while-language” is fixed, no Hoare sheet is routed, and the required worked verification example is absent. The [CWI record for Apt's survey](https://ir.cwi.nl/pub/10268) is an appropriate source for the historical/result role, but a citation cannot certify a different locally printed calculus whose rules and semantics are not fixed.  
Exact correction: define the while-language and state semantics; create and route the attributed A-022/A-096 Hoare calculus with every rule and side condition; change the theorem to proved=annex:<id> and supply the complete rule-induction proof against that exact calculus in the annex (or delete the local proof and leave a genuinely statement-only cited theorem, which would still not satisfy N-c-019's proof ceiling). Add the required worked example and exact wp/wlp table. For separation logic, define command locality/heap-state semantics and give the frame-rule soundness statement/status before calling the rule sound.  
Discussion: this is a proof-status reciprocity defect even if every informal induction sentence is mathematically standard.  
Disposition: independent source/content blocker.

### F7 [major] [open] SLD, stable-model complexity, and Datalog claims do not have exact procedural/source standing

Author: source-fidelity/evidence seat  
Location: handbook/parts/p09/logic-in-computer-science.tex:351-410; spec/registers/new-content.csv:129-132; spec/registers/depth-gaps.csv:133-134; spec/registers/apparatus.csv:24,98  
Claim: the least-model and stable-model definitions are useful and mostly correctly scoped, but the promised operational and complexity claims are not recoverable from the route.  
Evidence: the definite-program operator at :354-369 fixes grounding and least-fixed-point semantics and is source-supported. By contrast, SLD at :371-377 has no goal-state syntax, standardization-apart convention, selected clause/mgu transition, computed-answer substitution, success/failure clause, or registered selection/search sheet; “fair” is not made into a total enumeration. Stable-model existence is stated NP-complete at :393-396 without a complexity citation; Gelfond--Lifschitz 1988 at :388 controls the reduct semantics, not by itself this later complexity role. The Chandra--Merlin homomorphism direction at :398-401 is correct, but Datalog combined complexity is only “strictly larger” at :403-404, not an exact class under an explicit input convention. A-023 and A-097 are absent.  
Exact correction: route an SLD sheet fixing clauses, goals, standardization apart, mgu, transition, computed answers, fair search, and the negation-as-failure boundary; give separately statused soundness/completeness results. Attach an authoritative complexity source to finite propositional normal-program stable-model existence. State exact Datalog data and combined decision problems/classes. Supply A-097 so SLD, completion, well-founded, and stable semantics are not conflated.  
Discussion: handbook/parts/p09/logic-in-computer-science.tex:406-410 is checked clean at its pointer-only CSP ceiling: the template is explicitly fixed and no unrestricted tractability transfer is made.  
Disposition: source/content blocker as part of F1.

### F8 [major] [open] Complexity imports and apparatus do not point to the exact public results required by N-c-026

Author: source-fidelity/evidence seat  
Location: handbook/parts/p09/logic-in-computer-science.tex:412-435; handbook/parts/p04/complexity.tex:227-248,412-499; spec/registers/new-content.csv:133,135; spec/registers/apparatus.csv:52-53,80,96-98  
Claim: the local table is a partial boundary summary, not the registered complexity proof/table closure.  
Evidence: handbook/parts/p09/logic-in-computer-science.tex:431-433 names “Parts IV and V” without labelled theorem references. P4's Cook--Levin and TQBF statements at handbook/parts/p04/complexity.tex:227-248 are cited statements; they do not provide the QBF PSPACE proof expressly required by N-c-026. The modal row is one sentence, not the requested exact K/S4/S5 table. The public Fagin and Immerman--Vardi imports at handbook/parts/p09/logic-in-computer-science.tex:82-100 are source-faithful and point to the correct identities at handbook/parts/p03/finite-model-theory.tex:80-91 and handbook/parts/p04/complexity.tex:471-475. A-052 and A-079 exist, but A-051 is incomplete and A-095/A-096/A-097 do not exist on the reader route.  
Exact correction: replace prose part names by exact theorem/table references; route a complete QBF PSPACE proof with truthful status; supply the exact modal decision-problem table and the missing P9 apparatus; preserve the existing finite/order hypotheses on the Fagin/Immerman--Vardi imports.  
Discussion: N-c-028's McMillan pointer at handbook/parts/p09/logic-in-computer-science.tex:274-278 is source-supported and needs no expansion beyond its pointer ceiling.  
Disposition: source/content blocker as part of F1.

### F9 [major] [open] Most named result claims evade theorem status, and the P9 audit/annex navigation is not a truthful reachable record

Author: source-fidelity/evidence seat  
Location: handbook/parts/p09.tex:1-3; handbook/annex/p09.tex:4-16; handbook/parts/p09/logic-in-computer-science.tex:26-31,75-100,190-227,242-255,280-284,309-322,371-404,431-435; handbook/generated/audit-p09.tex:15-30; handbook/generated/named-theorem-index.tex:163-165  
Claim: proof/source statuses are not reciprocal with the prose and generated retrieval.  
Evidence: the generated P9 audit contains sixteen local environments but only three statused theorems (handbook/generated/audit-p09.tex:15-30). Trakhtenbrot, Gaifman/Hanf, Kamp, LTL PSPACE, LTL-to-Buchi, BET/S1S/S2S, CTL correctness/complexity, PDL completeness, Cook relative completeness, SLD adequacy, stable-model NP-completeness, Chandra--Merlin, Datalog, CSP, and Ladner bounds remain ordinary prose with no exact theorem status or public identity. handbook/parts/p09.tex:3 inputs only the body, not the generated P9 audit. The annex says zero--one, Fagin, and Immerman--Vardi are “stated” in P9 and says Fagin's proof idea is immediately after “the statement” (handbook/annex/p09.tex:7-10), but the actual Fagin and Immerman--Vardi statements live in P3/P4 and only cross-references live in P9. The Hoare annex item repeats the status contradiction in F6.  
Exact correction: create no duplicate theorem identities. Convert each locally asserted named result into a truthful cited, proved-annex, or sketched-annex environment, or replace it with an exact cross-reference to its one public identity. Route the generated P9 audit from the book's intended audit surface. Rewrite the annex to point to the actual statement and proof locations and add reciprocal annex items only where a local proof/sketch genuinely exists.  
Discussion: the named index correctly exposes the current identities; its duplicate zero--one rows reveal rather than cause F2.  
Disposition: source/content and reader-retrieval blocker.

### F10 [major] [open] P9's symbol and calculus uses are not registered at their actual typed scopes

Author: source-fidelity/evidence seat  
Location: handbook/registry/symbols.csv:14,91-107,316,519-541; handbook/parts/p09/logic-in-computer-science.tex:15,39,125-130,177-184,198-205,242-249,327-340,354-388; handbook/parts/p14/rule-sheets.tex:70-78,96-100  
Claim: the generated symbol surfaces faithfully expose the registry, but the registry does not license most P9 roles and one P9 use collides with an existing global role.  
Evidence: the only live symbol row whose scope reaches P9 is the LFP constructor at handbook/registry/symbols.csv:316. Temporal calculus identifiers/operators and the Buchi automaton datum are scoped to P8.3 at :519-541, not P9. P9 independently uses \(\mu(\varphi)\), \(\sigma\) as a signature, \(\Delta^I\), \(\mathsf{AP}\), \(w_i\), \(\operatorname{Pre}_{\exists}\), wp/wlp, heap \(\perp,\uplus,*\), \(T_P\), and \(P^M\)/default not with no P9-scoped row. The global registry already reserves capital Greek context letters at :14; the P9 lower-case signature role must still be explicitly typed rather than inferred by typography. P8 has exact temporal/automata symbols and sheets, but P9 never says it is reusing that registered presentation. No Hoare, PDL, separation, or SLD calculus appears in the current central route.  
Exact correction: either point P9 explicitly to the existing P8 presentations and widen only the exact symbol scopes being reused, or register each distinct P9 glyph-role with type, standing, precedence, and noncollision note. Register and route the missing calculi before displaying their rule shapes. Keep signature/context and least-fixed-point/probability uses distinct. Regenerate retrieval only after the authoritative registry is correct.  
Discussion: this finding concerns authoritative registry coverage, not whether the generated TeX mechanically mirrors its CSV.  
Disposition: source/content/navigation blocker as part of F1.

### F11 [major] [open] The reader is not told that current P9 is wholly editorial while the inherited source intervals carrying the historical Part IX title are routed elsewhere

Author: source-fidelity/evidence seat  
Location: handbook/parts/p09.tex:1-3; handbook/parts/p09/logic-in-computer-science.tex:1-9; handbook/annex/p09.tex:1-5; handbook/parts/p02.tex:47-58  
Claim: source and presentation standing is not explicit at the P9 entry point.  
Evidence: the P9 driver reaches only one 442-line editorial body and contains no exact-restoration wrapper or source map. The annex is navigation-only. The eleven exact wrappers for frozen source intervals SRC-12249-12969 are routed under P2 at handbook/parts/p02.tex:47-58, because that inherited material concerns second/higher-order logic rather than the new computer-science chapter. Relocation may be editorially correct, but a reader entering P9 is given no note distinguishing “new synthesized Part IX” from an inherited Part IX source unit or pointing to the rehomed exact material.  
Exact correction: add an ordinary reader-facing source-standing note at the P9 entry: this chapter is editorial synthesis; enumerate its controlling sources by local record; point to the exact inherited-Part-IX-labelled intervals at their P2 route without exposing internal artifact IDs. Do not fabricate a derivative lineage where there is none.  
Discussion: no byte-preservation failure was found inside P9 because there are no exact wrappers in its closure. The eleven P2 wrappers were checked for route existence only; their bytes are outside this board's P9 editorial graph and were not re-audited as a new exact-preservation lot.  
Disposition: source-standing blocker, repairable without altering inherited source.

## Bibliography/source-role result

The chapter's 49 distinct citation/status keys all resolve to non-stub records in handbook/bib/handbook.bib; there is no dangling-key blocker. That mechanical result does **not** cure statement/source mismatches. The concrete missing or misassigned roles above include:

- locality and fragments: Hanf 1965, Gaifman 1982, Lewis 1979, Börger--Grädel--Gurevich 1997, Mortimer 1975, Andréka--van Benthem--Németi 1998, Behmann 1922;
- description logic: Schild 1991, Baader--Brandt--Lutz 2005, Calvanese et al. 2007;
- automata and fixed points: Elgot 1961, Trakhtenbrot 1961, Rabin 1969, Emerson--Jutla, Bradfield--Stirling;
- PDL/program/database roles: Pratt, Harel--Kozen--Tiuryn, O'Hearn--Reynolds--Yang, the registered stable-model complexity sources, and the registered CSP historical sources.

The correction is not a bibliography dump: each record must be attached to the exact statement variant, problem convention, proof standing, or family row it controls.

## Checked-clean evidence

- **No reader construction debt found:** no reader-visible OPEN, stub, owed, or internal N/D/A register identifier occurs in the current P9 body or annex. “Open blocked branch” at handbook/parts/p09/logic-in-computer-science.tex:157 is mathematical tableau language, not workflow debt.
- **Cross-part descriptive-complexity identity:** P9's Fagin and Immerman--Vardi references at handbook/parts/p09/logic-in-computer-science.tex:82-100 preserve the public P3/P4 identities and the crucial built-in-order qualification.
- **Finite-template CSP boundary:** handbook/parts/p09/logic-in-computer-science.tex:406-410 fixes the template and does not transfer tractability to unrestricted homomorphism.
- **ASP semantic scope:** handbook/parts/p09/logic-in-computer-science.tex:379-390 explicitly restricts the reduct definition to finite propositional ground normal programs and separately requires grounding for nonground syntax.
- **Verification caveats:** handbook/parts/p09/logic-in-computer-science.tex:269-278,437-442 correctly separates a bounded counterexample search from unbounded proof and a solver/build outcome from a mathematical theorem.
- **Mechanical citations:** all cited keys resolve; no citation is marked as a stub.
- **Generated mirrors:** the current named theorem and symbol outputs reflect their underlying theorem environments/registry; the defect is incomplete/duplicated authoritative content and reachability, not an observed generated-text corruption.

## Exact-source, external-gate, and not-checked boundaries

These do not replace or soften the source/content rejection above:

- **Exact-source preservation:** checked for route shape. P9 contains no exact wrapper; the inherited SRC-12249-12969 wrappers are present under P2 at handbook/parts/p02.tex:47-58. Their byte equality was not re-audited because they are outside the live P9 editorial closure.
- **Provenance/inventory gate:** remains external and stale on this snapshot. spec/handbook-source-inventory.csv:32929 records the P9 body as 477 lines with hash 398bf9..., while the reviewed file is 442 lines with hash c52cd5...; :3944 records the annex as 258 lines with hash 718635..., while the reviewed annex is 17 lines with hash 7d47d9.... This must be regenerated/verified later, but it is not the basis for the source/content rejection.
- **Administrative register closure:** literal CSV disposition rows remain open. They should change only after the corresponding live artifacts are repaired and independently checked.
- **Build/test:** deliberately not run. Compilation, reference resolution in a real build, and generated-file freshness are not established by this review.
- **Visual:** not checked. Page breaks, table legibility, hyperlinks, overfull boxes, and figure/table rendering remain for the visual gate.
- **Human/user:** not checked and not inferred. Editorial approval, rights/reproduction, and final user acceptance remain external.

## Four-lot coverage

| Charter lot | Coverage |
|---|---|
| 1. Finite model theory, zero--one/locality, descriptive complexity, fragments/prefix | checked; F2-F3 plus the relevant F1 rows |
| 2. Description logics, modal bridge, blocking, families, ontology/query | checked; F4 plus F1/A-095 |
| 3. Temporal, omega/tree automata, MSO, model checking, modal mu | checked; F5 plus F1 and P8 cross-imports |
| 4. Hoare/PDL/separation, logic programming/ASP/Datalog/CQ/CSP, complexity, symbols/citations/navigation | checked; F6-F11 |

Current source/content vote: **REJECT**.
