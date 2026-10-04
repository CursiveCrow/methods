# Part VII admission board — blind round-one source-fidelity review

- seat: source-fidelity/evidence
- round: blind opening
- artifact: complete current reader graph rooted at `handbook/parts/p07.tex` and `handbook/annex/p07.tex`
- boundary: read-only; I did not read another Part VII seat transcript, edit manuscript/source/provenance/control/generated/test files, build, or run tests
- role standard: exact inherited correspondence and order; declared derivative lineage; exact source roles and claim scope; proof-status reciprocity; notation/register/apparatus standing; no reader-visible construction debt

## Findings

### F1 [blocker] [open] The required live Part VII theorem/definition register is intentionally OPEN and absent from the reader route

- location: `handbook/parts/p07.tex:31-32`; expected generated surface `handbook/generated/audit-p07.tex`
- claim: The body driver ends with a comment saying that `generated/audit-p07` is intentionally OPEN and unrouted because it still scans historical chapters rather than the reachable exact-source graph. Therefore the admitted Part VII reader has no live theorem/definition retrieval surface for its exact and editorial entries. This violates both the charter's generated-retrieval criterion and the Part VII navigation claim that status-bearing results are retrievable.
- evidence: The only routed body inputs are the nineteen exact wrappers and the eight editorial body files at `handbook/parts/p07.tex:3-29`; no generated register follows them. The comment at `:31-32` concedes that the available generated file is based on the wrong graph.
- exact correction: Make the audit generator traverse the current reachable Part VII route, regenerate `handbook/generated/audit-p07.tex` from those live inputs, give it an ordinary reader caption/label, and route it once after the final Part VII body addition. Exact-source entries must retain their printed `complete proof`/`proof sketch`/`cited theorem` standing; editorial `proved=`, `sketched=`, and `cited=` entries must retain their explicit destinations without importing dormant historical entries.
- status: open admission blocker.

### F2 [blocker, external boundary] [open] Part VII provenance and register admission remain administratively unbound

- location: `spec/register-obligation-closure.csv`, records `OBL::depth-gaps::D-P8-001` through `D-P8-007`, `D-P9-003`, `D-P9-004`, and the Part-VII new-content/apparatus records; exact-destination records `spec/provenance/SRC-11354-11413.json` through `SRC-12218-12248.json`
- claim: The current closure ledger still reports the selected Part VII obligations as `completion_status=OPEN`, with empty destination/presentation bindings and pending seat/static/build/visual fields. Exact artifact fidelity is mechanically clean, but that does not itself admit the destination provenance or any register obligation.
- evidence: The live closure rows inspected for the Part VII target all had `manifest_binding_disposition=open`, `completion_status=OPEN`, empty `handbook_unit_ids`, `presentation_packet_ids`, and `destination_labels`, and pending verification columns. The nineteen artifact comparison below is evidence for content identity only, not a substitute for those control records.
- exact correction: After the source/content blockers below are repaired, bind each Part VII obligation to its exact live labels/files and reviewed records, pin the derivative hashes and exact-source destinations, and run the separate static/build/visual/human/user gates. Do not promote any of those later gates from this source review.
- status: open external admission-control boundary.

### F3 [must-fix] [open] Several restoration supplements claim exact historical slices while silently changing or replacing them

- location: `handbook/parts/p07/normalization-and-curry-howard-supplement.tex:1-13`; `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:1-14,91-135`; `handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex:1-14,105-168`; corresponding historical files `handbook/parts/p07/normalization-and-curry-howard.tex:150-358`, `arithmetic-proof-theory.tex:65-112`, and `cut-elimination-and-interpolation.tex:253-272`
- claim: The derivative headers say the routed blocks are “exactly historical” slices. Static line comparison shows undeclared changes:
  - the normalization slice removes the apparatus identifiers from the three captions corresponding to historical lines 198, 255, and 348;
  - the arithmetic slice removes the `D-P8-005` caption identifier and replaces the historical one-line `N-a-049` stub at line 110 with a new 41-line ordinal-measure definition/table/theorem;
  - the cut/interpolation slice preserves historical lines 253-263, then replaces the two historical OPEN stubs at lines 264-272 with a new table and three reader-labelled proof paragraphs through current line 168.
  These may be defensible editorial repairs, but they are not exact copies and the current lineage declarations do not identify their deltas.
- evidence: Exact comparison returned zero mismatch for the genuinely copied calculi block (historical 79-90), cut block (133-220), arithmetic block (7-46), and both calculi-annex blocks. It returned the concrete caption mismatches above and showed the new proof/measure material where the historical files contained stubs. The authoritative nineteen inherited artifacts are separately byte-clean; the problem is derivative provenance, not frozen-source alteration.
- exact correction: Change each header and provenance record to distinguish verbatim retained ranges from consumer-corrected derivative material. Enumerate every removed internal identifier, replaced stub, added proof table/paragraph, and source-consumer redirection; pin the current derivative hashes. Do not call a changed block “exactly historical.”
- status: open source-lineage defect.

### F4 [blocker] [open] The hand-maintained status/navigation tables contradict the current live sheets and omit live theorems

- location: `handbook/parts/p07/proof-complexity.tex:185-310`; `handbook/parts/p07/calculi-and-derivability-supplement.tex:170-225`; live counterevidence at `lambda-calculi-and-type-theories.tex:399-448`, `arithmetic-proof-theory-supplement.tex:92-132,326-392`, `functional-interpretations.tex:370-413`, and `structural-extensions.tex:144-216`
- claim: The route table says at `proof-complexity.tex:188-190` that it lists every status-bearing result exactly once, but it omits at least:
  - `thm:p07-prop-cut-termination` and `thm:p07-omega-cut-elimination`;
  - `thm:p07-ha-proof-term-canonicity`;
  - `thm:p07-four-modal-calculi`.
  It also says at `:244-246` that the MLTT remainder has no active sheet even though the body links `sheet:mltt-intensional`, and says at `:294-300` that the four generalized frameworks remain citation-only until exact modal sheets exist even though four sheets and four worked derivations are live. The A-071 calculi catalog likewise still describes labelled/display/deep systems as having no active sheet (`calculi-and-derivability-supplement.tex:209-222`).
- evidence: The live files directly hyperlink `sheet:mltt-intensional`, `sheet:gs5-avron`, `sheet:labelled-k-negri`, `sheet:display-k-wansing`, and `sheet:deep-s5-stouppa`; the named theorem environments above are reader-routed. The table's universal claim is therefore false on its own input graph.
- exact correction: Regenerate the status route from the same reachable graph as F1, or update it exhaustively. Add every live theorem/status destination, replace the “no active sheet” claims by the exact selected sheets and their cited adequacy boundaries, and keep cited results distinct from locally proved/sketched items. Update A-071 and A-189 together so they cannot disagree.
- status: open retrieval/source-standing blocker.

### F5 [must-fix] [open] Reader-visible construction debt and internal register language remain after the promised material

- location: `handbook/parts/p07/structural-extensions.tex:84-116,144-216`; `handbook/annex/p07/functional-interpretations.tex:31-36`; related stale row `handbook/parts/p07/proof-complexity.tex:294-300`
- claim: The generalized-framework definition says “the owed system-specific examples below” and its table caption says exact evidence is “still required,” although four examples, four sheets, and a separate adequacy theorem immediately follow. The annex tells readers that a “visible N-a-055 stub” records missing proof work, but no such live stub exists and the body now provides a cited canonicity theorem plus three extraction arguments. These sentences expose obsolete workflow IDs/debt and make false claims about the live surface.
- evidence: The four examples are at `structural-extensions.tex:146-205` and the adequacy theorem at `:207-216`. The HA proof-term/canonicity and extraction route is at `functional-interpretations.tex:370-413`. The only remaining `N-a-055 stub` assertion is the annex paragraph itself.
- exact correction: Replace “owed”/“still required” with ordinary attribution to the selected sheets and sources. Replace the annex's `N-a-055` sentence with an ordinary proof-status statement accurately distinguishing the cited canonicity theorem from the locally proved last-rule lemma and cited HA metatheorems. Remove the matching stale navigation row described in F4.
- status: open reader-debt defect.

### F6 [blocker] [open] The new propositional cut-termination theorem is not established by its stated multiset measure

- location: `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:92-132`, especially `:97-103,116-130`
- claim: The text assigns the multiset of all cut pairs `(formula rank, premise-height sum)` and says every critical reduction in the table strictly decreases it, hence every sequence terminates. That is not true for the unrestricted reductions as stated. Commuting a cut above a binary rule can duplicate the opposite premise; any cuts internal to that duplicated premise are duplicated too. The table accounts only for replacing the selected outer cut pair and gives neither a strategy ensuring the duplicated premise is cut-free nor a recursive measure that dominates duplicated subderivations. Principal reductions have the same duplication problem. Thus the displayed `M(D)`/natural-sum argument does not justify the universal decrease or termination conclusion.
- evidence: `:97-103` explicitly counts every cut node. The commutation and contraction rows at `:117-121` discuss only the selected cut pair. No maximal-rank/uppermost reduction strategy, premise-cut-freeness invariant, or duplication-sensitive recursive weight is stated in the definition or theorem. The exact inherited chapter itself correctly leaves the complete reduction table at proof-sketch status (`handbook/restoration/inherited-11768-11823.tex:18-55`).
- exact correction: Either (a) state and prove a deterministic strategy, such as reducing an appropriate uppermost/maximal-rank cut so duplicated premises satisfy the required invariant, and prove all table cases for that strategy; or (b) replace `M(D)` by a standard recursive ordinal/degree measure that counts duplicated subderivations correctly and prove strict decrease. Until then, downgrade `thm:p07-prop-cut-termination` to a method/proof-boundary sketch and do not cite the source as if it proved this exact newly invented measure.
- status: open mathematical and source-scope blocker; N-a-049 is not fulfilled by the present replacement of its old stub.

### F7 [blocker] [open] The Maehara/Craig/Beth “proof” does not meet the registered complete-proof obligation or its own status contract

- location: `handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex:64-115,117-168`; `handbook/annex/p07/interpolation-supplement.tex:14-33`; criteria `spec/registers/depth-gaps.csv` record `D-P8-004` and `spec/registers/new-content.csv` record `N-a-070`
- claim: The body lemma remains `sketched=annex:p7.interp.1`, the annex explicitly lists the complete rule-by-partition table as omitted, and the proof boundary says the method remains sketched. The later heading nevertheless says “Complete induction,” says “This proves” the lemma, and labels the Craig and Beth paragraphs as proofs. The generic two-premise/eigenparameter descriptions do not instantiate every principal-formula placement for every selected rule, and the Craig paragraph also loads the inherited cut-elimination sketch. The register explicitly requires Craig proved by Maehara and Beth as a corollary; that requirement is not met by relabelling the same omitted induction.
- evidence: Annex lines `17-22` enumerate the omitted initial/structural/propositional/quantifier cases, and `:31-32` says the case-by-case verification is not supplied. Body lines `106-115` say the local result remains sketched; lines `133-146` then assert completeness without adding the enumerated cases. `D-P8-004` says “Craig interpolation proved by Maehara's method”; `N-a-070` repeats the proof requirement and Beth corollary.
- exact correction: Either keep the lemma/method explicitly sketched and leave the two register rows open, removing “Complete induction” and proof-upgrade wording, or supply a genuinely complete rule-by-partition induction for the exact `LK_d` sheet, then a complete Craig derivation with its completeness/cut-elimination dependencies honestly discharged and the compactness/interpolation Beth derivation. Only then change the body/annex/generated statuses reciprocally.
- status: open register and proof-standing blocker.

### F8 [blocker] [open] The “selected proof-term presentation of HA” is not an exact calculus, so the canonicity source cannot carry the three promised proofs as written

- location: `handbook/parts/p07/functional-interpretations.tex:370-413`; `handbook/annex/p07/functional-interpretations.tex:31-36`; criterion `spec/registers/new-content.csv` record `N-a-055`
- claim: The body names a selected natural-deduction HA proof-term presentation but supplies no term grammar, typing rules, definitional equality/conversion, equality reductions, induction recursor computation, or exact erasure map. It then cites a blanket normalization/canonical-forms theorem for that unspecified presentation and uses it in three reader-labelled proofs. The definition itself says a bare HA formula does not determine a normalization algorithm, but it still does not fix one. Consequently the claimed source-to-calculus match and the proof obligations for IPC/HA disjunction and HA numerical existence are not auditable.
- evidence: `:370-380` gives only an informal constructor dictionary and one sentence about induction. `:384-390` asserts normalization, canonical forms, and erasure for “the selected presentation” without an exact source locator or sheet. The subsequent arguments at `:393-413` are valid only after those missing exact data and metatheorems are fixed. The annex simultaneously says a stub records the missing complete proof, confirming status drift.
- exact correction: Select and display or unambiguously import one exact HA proof-term calculus, including equality and induction computation and the erasure theorem, with theorem/page locators in the cited source. Then keep the canonicity theorem cited and present the three deductions at their actual evidence level, or provide reciprocal annex proofs. If the exact calculus is not supplied, remove the local “Proof” claims and retain the three theorems as directly cited metatheorems.
- status: open fixed-calculus/source-standing blocker.

### F9 [blocker] [open] The A-072 Curry--Howard categorical construction uses an arrow-only syntax that cannot supply the bicartesian closed structure it claims

- location: `handbook/parts/p07/normalization-and-curry-howard-supplement.tex:16-58,60-99,101-123`; active sheet `handbook/registry/calculi/stlc.tex:5-9`; criterion `spec/registers/apparatus.csv` record `A-072`
- claim: The definition says the selected syntactic category has the selected types as objects and unary beta-eta term judgments as morphisms, then presents it as the bicartesian closed leg of the dictionary. But the active STLC sheet is explicitly arrow-only and has no product, coproduct, unit, or empty types. The supplement itself concedes at `:95-97` that those rows describe a standard extension not present on the sheet. With types rather than contexts as objects, the stated selected syntax therefore does not provide the products/coproducts/initial/terminal objects required by the definition and figure.
- evidence: `stlc.tex:5` explicitly excludes products and sums. The categorical definition at `normalization...tex:25-49` requires finite products, finite coproducts, terminal/initial objects, and exponentials, while its morphism construction at `:40-44` refers only to the selected types/terms. The table then uses all four absent type formers.
- exact correction: Define and route an exact extended typed calculus with `1,0,product,sum,arrow`, their typing and beta-eta equations, and construct its syntactic bicartesian closed category; or restrict the categorical claim to the actual arrow-only/contextual structure and remove unsupported bicartesian rows/edges. Tie the Lambek--Scott source to the exact chosen construction rather than to a hybrid dictionary.
- status: open apparatus/source-correspondence blocker.

### F10 [must-fix] [open] The A-074 ordinal table explicitly omits part of its registered range

- location: `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:225-266`; criterion `spec/registers/apparatus.csv` record `A-074`
- claim: A-074 requires proof-theoretic ordinals for “Q-range fragments, PA, and stronger systems.” The table starts with modern PRA and `I Sigma_n`, then PA/HA/ACA0/ATR0; it contains no Q or other cited lower Q-range calibration, and `:264-266` explicitly says weaker first-order arithmetics are deliberately omitted. Thus the live artifact does not meet the table's registered scope.
- evidence: The six table rows are exactly PRA, `I Sigma_n`, PA, HA, ACA0, and ATR0/predicative progressions. The control row's scope and the reader's explicit omission are opposite.
- exact correction: Add carefully defined and cited lower-fragment rows under the same declared calibration convention, including the intended Q-range endpoint(s), or obtain an explicit control-level scope change before claiming A-074 complete. Do not silently treat PRA as the whole Q-range.
- status: open apparatus-completeness defect.

### F11 [must-fix] [open] The proof-complexity register asks for a Haken proof sketch, but the body supplies only a cited statement

- location: `handbook/parts/p07/proof-complexity.tex:63-96`; criteria `spec/registers/new-content.csv` record `N-c-027` and `spec/registers/depth-gaps.csv` record `D-P8-007`
- claim: The body carefully fixes the weak pigeonhole CNF and proof-size measure, then states Haken's exponential lower bound with citations. It contains no proof-sketch invariant, bottleneck lemma, random-restriction argument, or other outline of why the bound follows. N-c-027 expressly requires the resolution lower bound “proof sketch,” so the statement-only entry is below its registered treatment.
- evidence: Between the definition ending at `:87` and the next section beginning at `:98`, the only content is the theorem statement/citation at `:89-96`.
- exact correction: Add a source-faithful proof sketch tied to the exact CNF and DAG-size convention, naming the combinatorial measure and the lower-bound lemma actually used by Haken or the selected modern presentation, with an exact locator. Otherwise leave N-c-027/D-P8-007 open and describe the theorem as statement-only.
- status: open register-depth defect.

### F12 [must-fix] [open] The Jager--Probst bibliography record corrupts both author and title accents

- location: `handbook/bib/handbook.bib:3526-3534`; consumers `handbook/registry/calculi/omega-arithmetic.tex:5` and `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:372-391`
- claim: The live BibLaTeX fields use `J{"a}ger` and `Sch{"u}tte`: the quotation mark is not preceded by the TeX accent backslash. Those byte strings do not encode the names Jäger and Schütte correctly.
- evidence: The authoritative DOI record is [10.1002/malq.200310097](https://doi.org/10.1002/malq.200310097), identifying Gerhard Jäger and Schütte. The intended BibLaTeX spellings are `J{\"a}ger` and `Sch{\"u}tte`.
- exact correction: Correct the author/title fields to valid TeX accent commands (`J{\"a}ger`; `Sch{\"u}tte`) and regenerate bibliography-dependent surfaces. Preserve the article type, journal, volume 50(3), pages 258-264, year 2004, and DOI.
- status: open bibliographic identity defect.

### F13 [must-fix, needs exact evidence] [open] The 2026 Frege-status claim is assigned to a source about a different proof system

- location: `handbook/parts/p07/proof-complexity.tex:124-130`; `handbook/bib/handbook.bib:4090-4099`
- claim: The theorem's principal token is `cited=Alekseev2026` and states the current absence of superpolynomial lower bounds for Frege and extended Frege. The cited record is titled *A Lower Bound for Polynomial Calculus with Extension Rule*, not a Frege/extended-Frege status survey. Krajicek 2019 supports an older status boundary, but the manuscript dates the claim to 2026 and supplies no exact clause/locator showing that Alekseev's adjacent lower-bound paper establishes the two Frege assertions.
- evidence: The record's DOI is [10.4086/toc.2026.v022a004](https://doi.org/10.4086/toc.2026.v022a004); the local title and the claimed theorem concern different named systems. This does not prove the status claim false, but it leaves the current-source role unverified and therefore unable to close a source-fidelity audit.
- exact correction: Cite a current authoritative proof-complexity survey/status source with the exact Frege and extended-Frege clause and locator, or quote the precise Alekseev section that states both open problems and make Krajicek the historical survey. Retitle the entry as a dated status note rather than a formal theorem if appropriate.
- status: needs exact source evidence; open for source fidelity.

### F14 [must-fix] [open] The active MLTT sheet is an editorial composite without an exact source matching its full rule surface

- location: `handbook/registry/calculi/mltt-intensional.tex:1-56`; `handbook/parts/p07/lambda-calculi-and-type-theories.tex:399-448`; criterion `spec/registers/new-content.csv` record `N-c-030`
- claim: The sheet calls itself a matched core and names Martin-Lof 1984 and Abel--Coquand--Dybjer 2007 as controlling sources, but combines explicit structural/equality/congruence rules, Pi, Sigma, intensional identity, and a cumulative predicative Russell hierarchy. The body correctly limits the Abel--Coquand--Dybjer normalization theorem to dependent functions and one Russell universe and explicitly says it does not cover Sigma, identity types, or the cumulative hierarchy. No rule-level source map identifies one authority for the larger hybrid calculus, especially the custom multi-sorted congruence schema at sheet lines 17-36.
- evidence: Body lines `439-447` state the source ceiling. Sheet lines `38-56` add the formers and cumulative universe rules beyond it, while sheet line `5` labels both sources globally as controlling. Thus the metatheorem is scoped correctly, but the calculus/source identity is not.
- exact correction: Either select one published calculus whose judgments and every displayed rule match the sheet, citing exact chapter/page/rule locators, or label the sheet as an editorial composite and attribute each structural, Pi/Sigma/Id, equality, and universe cluster to its exact source. Keep the Abel--Coquand--Dybjer theorem attached only to its already narrowed subcalculus.
- status: open exact-source/rule-surface defect.

### F15 [must-fix] [open] The mandatory LK-completeness depth row is only a lookup to an existing sketch

- location: `handbook/parts/p07/calculi-and-derivability-supplement.tex:92-113`; criterion `spec/registers/depth-gaps.csv` record `D-P8-001`
- claim: D-P8-001 requires completeness of LK for arbitrary sequents in the proof-theory part. The routed addition creates a `hbmethod` lookup, explicitly calls both propositional and first-order completeness theorems “sketched,” and creates no Part VII theorem/proof or annex item. It also warns that the cut-elimination sketch is for a different LK presentation. This is honest source standing, but it does not supply the registered completeness treatment.
- evidence: `:94-108` gives only equivalence prose pointing to `thm:prop-lk-completeness` and `thm:fol-lk-completeness`; `:110-113` expressly says it creates no duplicate theorem or annex item. The register row is mandatory and was motivated by the source having only a soundness sketch.
- exact correction: Supply a status-bearing completeness theorem for the exact selected canonical LK presentation with a complete proof route at the registered depth, including the Choice hypothesis for the first-order form and the translation/presentation boundary; or leave D-P8-001 open and stop treating the lookup as fulfillment.
- status: open mandatory depth defect.

## Exact-source, route, proof-status, and citation checks that came back clean

- **Exact inherited artifacts:** All nineteen routed inherited files are line-for-line identical to `source/formal-logic-reference.tex:11354-12248`: 19/19 artifacts, 895/895 lines, zero mismatches. The driver routes each wrapper once, in contiguous authority order, with no duplicate exact interval.
- **No overlapping historical body on the reader route:** The dormant full historical files (`calculi-and-derivability.tex`, `cut-elimination-and-interpolation.tex`, `normalization-and-curry-howard.tex`, `arithmetic-proof-theory.tex`, and the old annex files) are not input by either reader root. Only the declared supplements and exact wrappers are reachable.
- **Reciprocal annex links:** The routed body/annex pairs agree for defined-negation soundness, LK-presentation equivalence, Maehara's lemma, Church--Rosser, beta-normal-form uniqueness, and cut-free LJ disjunction extraction. Locally proved/sketched targets have one corresponding annex item; cited Dialectica, realizability, epsilon, System-F/MLTT, proof-complexity, and modal adequacy claims have no manufactured annex item. F7/F8 concern adequacy of the evidence and status prose, not an orphaned label.
- **Exact source proof standings:** The exact cut/mix equipollence and cut-free subformula lemma retain complete inline proofs; the inherited cut-elimination, analytic-existence, empty-sequent, normalization, subject-reduction, strong-normalization, and Gentzen analyses retain their printed sketch/cited boundaries. No inherited byte was edited to promote them.
- **Scoped source distinctions:** The live lambda chapter cleanly separates untyped beta conversion, STLC, Church-style System F, Curry-style assignment, CoC, and the bounded MLTT theorem; it does not transfer System-F checking to Curry typability or CoC normalization to CIC. The HoTT/cubical and proof-net/GoI exclusions remain pointer-only as required by `N-x-001`, `N-x-002`, `N-x-011`, and `N-x-012`.
- **Epsilon-result separation:** The first, extended first/Herbrand, and second epsilon theorems retain distinct equality-free scopes and cited statuses at `structural-extensions.tex:12-79`; no equality variant or local proof is invented.
- **Citation resolution:** All 54 citation keys found on the routed Part VII exact/editorial graph exist in `handbook/bib/handbook.bib`. F12 and F13 are field/scope defects, not missing keys.

## Register and apparatus coverage map

- `D-P8-001`: F15.
- `D-P8-002`: checked-clean at statement/source-status level (`thm:p07-lk-nd-equivalence`, cited Gentzen); no stronger local-proof claim was made.
- `D-P8-003` / `N-a-069`: checked-clean at the registered statement/survey level; equality-free regularity, prenex scope, ground-term convention, and Herbrand limitation are explicit.
- `D-P8-004` / `N-a-070`: F7.
- `D-P8-005`: component inventory and the inherited Gentzen boundary are checked-clean; its propositional-core companion `N-a-049` is blocked by F6.
- `D-P8-006`: the relative-calibration definition is present; the table's registered range is incomplete under F10.
- `D-P8-007` / `N-c-027`: F11; statement/table content is present, required proof sketch is not.
- `D-P9-003` / `N-a-015`: checked-clean at theorem/sketch level; syntax, alpha/substitution, beta/conversion, parallel method, Church numerals, partial recursiveness, and S--K basis have distinct standing.
- `D-P9-004` / `N-c-029`: checked-clean; System F syntax, impredicativity, encodings, confluence, Girard normalization, Church/Curry decision boundary, and parametricity pointer are claim-bound to distinct sources.
- `N-a-049`: F6.
- `N-a-050`: checked-clean; Veblen and Feferman--Schuette are qualified, with no blanket philosophical identification.
- `N-a-051`: checked-clean; Skolem's historical precursor and Tait's analysis are not equated with all finitism.
- `N-a-052`: checked-clean at cited-theorem level; the exact omega-calculus, indexed derivability, and epsilon-zero boundary are separated from finitary Gentzen analysis. External verification of every Jager--Probst formula was not independently repeated after the stop request; F12 covers the definite bibliography defect.
- `N-a-053`: checked-clean at cited-source level; System T, the quantifier-free target theory, Dialectica clauses, extraction, and relative consistency are distinct.
- `N-a-054`: checked-clean at cited-source level; number realizability, almost-negative ECT, Markov validation, and the separate HA nonderivability method are not conflated.
- `N-a-055`: F8 and F5.
- `N-a-056`: checked-clean at cited statement level.
- `N-a-057`: four selected sheets/examples and a separate adequacy theorem exist; reader/apparatus claims remain blocked by F4/F5 and the MLTT-like source-map principle should be applied to these editorial sheets in repair.
- `N-a-058`: checked-clean as a pointer with explicit hypotheses/no bound claim.
- `N-c-030`: F14.
- `N-x-001`, `N-x-002`, `N-x-011`, `N-x-012`: checked-clean pointer boundaries.
- `A-070`: present and presentation-specific; LK/LJ/IMLL/Lambek/relevance/affine rows do not infer one family-wide structural profile.
- `A-071`: F4.
- `A-072`: F9.
- `A-073`: present and checked-clean on the stated confluence/normalization/checking/typability distinctions, subject to F14's MLTT sheet standing.
- `A-074`: F10.
- `A-075`: the comparison table is present and its simulation notion is explicitly uniform; F11 blocks the registered lower-bound sketch depth.
- `A-151`: figure present; its categorical vertex inherits F9.
- `A-152`: checked-clean: the STLC composition instance and ND counterpart are complete and link to the active rule rows.
- `A-186`: checked-clean: the routed Part VII further-reading section is claim-separated from theorem authority.
- `A-189`: F1/F4; rule-sheet links exist, but the promised exhaustive body/status/annex retrieval is false and no live Part VII generated register is routed.

## Four-lot coverage

1. **Exact proof-system/derivability/structural/cut/subformula/Herbrand/interpolation lot:** checked in full across all exact wrappers, the two body supplements, both annex supplements, and their active LK/LJ sheets. Exact restoration is clean. Findings F1, F3-F7, and F15 apply. External page-by-page re-fetch of every cited monograph proof was not repeated after the chair's stop request.
2. **Exact normalization/Curry--Howard/STLC plus untyped/System F/MLTT lot:** checked in full across the five exact wrappers, both body additions, lambda annex, and the STLC/System-F/MLTT/untyped/S--K sheets. Exact restoration and lambda proof reciprocity are clean. Findings F4, F9, and F14 apply.
3. **Arithmetic proof theory/ordinal/omega logic/realizability/Dialectica/constructive properties lot:** checked in full across both body chapters, functional annex, System-T and omega sheets, and the cited-source boundaries. Findings F5, F6, F8, F10, and F12 apply. The exact current PDFs/pages for Jager--Probst, Troelstra, and the older monographs were not independently fetched in this timeboxed opening.
4. **Epsilon/generalized calculi/proof mining/proof complexity/tables/figures/index/bibliography lot:** checked in full across both body chapters, the epsilon/four-modal/proof-complexity sheets, the live bibliography records used by the route, and all ten P7 apparatus rows. Findings F1, F4, F5, F11-F13 apply. Static one-to-one comparison of every P7 symbol-registry row against both generated symbol surfaces was not completed before the stop request; it remains explicitly **not checked** and cannot be inferred from source/content acceptance.

## Prioritized repair checklist and opening verdict

1. Repair the mathematical/proof-standing blockers: F6 (cut measure), F7 (Maehara/Craig/Beth), F8 (exact HA proof-term calculus), and F9 (categorical syntax).
2. Regenerate/reroute the live audit and repair all stale retrieval/status prose: F1, F4, F5, and A-189.
3. Complete the mandatory registered content: F10, F11, F14, and F15.
4. Correct and re-pin source lineage/bibliography/source roles: F3, F12, and F13.
5. Only after the content freezes, close F2's provenance/register records and run the separate static symbol, build, PDF/navigation, visual, human, and user gates.

**Opening verdict: blocked.** Exact inherited preservation is clean, and substantial new material has honest cited/sketched boundaries, but the live Part VII reader still lacks its generated register, contains false exhaustive-navigation and obsolete debt claims, and does not yet satisfy several proof/source/register obligations.
