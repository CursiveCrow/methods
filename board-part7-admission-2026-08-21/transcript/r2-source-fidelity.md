# Part VII admission board — blind round-two source-fidelity review

- seat: source-fidelity/evidence
- round: R2, current-live-byte verification from scratch
- scope: reader graph rooted at `handbook/parts/p07.tex` and `handbook/annex/p07.tex`, the nineteen exact artifacts, routed derivative/editorial files, active calculus sheets, bibliography, symbol registry/generated symbol surfaces, generated Part VII audit, and global named-result index
- independence: I did not read another Part VII seat transcript and did not use the prior R1 verdict as evidence
- boundary: review only; no handbook/spec/tool/generated/test edit, no test, and no TeX/PDF build

## Verdict summary

The repaired reader graph is substantially source-sound. The nineteen inherited artifacts remain exact; the source map and derivative headers now distinguish restored bytes from editorial descendants; all exact source-unit/result anchors line up; the live 128-row Part VII register and named-result index cover the reachable results; and every editorial proof status has the correct reciprocal annex/citation standing. The new LK--ND, canonical-LK completeness, Maehara, Church--Rosser, propositional-cut, and Haken routes are now evidence-calibrated.

Source/content admission nevertheless remains blocked. The current source-relative HA boundary is honest but expressly supplies citations rather than the proofs demanded by the unchanged `N-a-055` contract. The local ordinal table honestly defers rather than fulfills the unchanged must-level master `A-074` contract, for which no live master table or supersession exists. The latest categorical and cut-measure repairs introduced unregistered/colliding notation, the Jäger--Probst BibLaTeX identity remains malformed, and two route/sheet claims still disagree with the exact live evidence.

## Evidence checks that passed

### E1 — exact inherited source, order, and uniqueness: pass

- location: `handbook/parts/p07.tex:87-112`; `handbook/restoration/inherited-11354-11413.tex` through `inherited-12218-12248.tex`; authority `source/formal-logic-reference.tex:11354-12248`
- result: All 19 artifacts compare line-for-line equal to their authoritative intervals: 19/19 artifacts, 895/895 lines, zero mismatches. The body driver routes 19 distinct wrappers exactly once in increasing contiguous authority order. The hook blocks are switched off around every editorial insertion, so editorial `hb...` environments cannot advance the exact-source counters.

### E2 — reader source map and derivative standing: pass

- location: `handbook/parts/p07/source-map.tex:1-19`; derivative headers at `calculi-and-derivability-supplement.tex:1-14`, `cut-elimination-and-interpolation-supplement.tex:1-14`, `normalization-and-curry-howard-supplement.tex:1-13`, `arithmetic-proof-theory-supplement.tex:1-14`, and `handbook/annex/p07/calculi-and-cut-elimination-supplement.tex:1-12`
- result: The source map accurately names nineteen exact intervals and classifies the comparisons, Maehara proof, categorical extension, lambda/type theory, propositional assignment, calibration, functional-interpretation, generalized-calculus, proof-complexity, figures, sheets, and generated register as editorial. The derivative headers now disclose the exact retained ranges and substantive deltas: new complete LK--ND/completeness proofs, the free-variable-strengthened Maehara proof, the typed bicartesian extension, replacement of the old propositional-assignment stub, caption/source-route changes, and new annex proofs. They no longer present changed descendants as restored source.

### E3 — governed exact anchors and generated retrieval: pass

- location: anchor machinery `handbook/parts/p07.tex:5-84`; exact wrapper blocks `:86-112`; generated register `:120-128` and `handbook/generated/audit-p07.tex:1-144`; global `handbook/generated/named-theorem-index.tex`
- result: The exact artifacts contain 31 raw theorem/definition-class units and 11 theorem/lemma/corollary results. The driver defines exactly 31 unit destinations and maps all 11 result positions, retaining the four pre-existing public identities. The generated audit has 128 live data rows: 31 exact-source rows plus 97 editorial definition/theorem-class rows. Static ID comparison found all 97 reachable editorial IDs exactly once and no dormant historical ID. The named index contains all 39 editorial status-bearing results and all 11 governed exact results.

### E4 — proof-status/annex reciprocity: pass

- location: 39 `hbtheorem`/`hblemma`/`hbcorollary` entries across the eight routed editorial body files; 10 live `annexitem` entries across the six routed Part VII annex files; generated audit and named index
- result: Every `proved=annex:...` or `sketched=annex:...` body token resolves to exactly one live annex item with the same target; every live annex item has exactly one body target; no `cited=...` entry has an annex item. The generated audit and named index repeat the same proof/sketch/citation standing.

### E5 — repaired local proofs and source ceilings: pass

- LK--ND and completeness: `handbook/annex/p07/calculi-and-cut-elimination-supplement.tex:50-217` now handles empty succedents, nonvacuous discharge, every structural/propositional/quantifier rule, RAA, eigenvariables, the reverse translation, multiplicity restoration, and the equality-free specialization of the proved natural-deduction completeness route. Body status and annex destinations agree at `handbook/parts/p07/calculi-and-derivability-supplement.tex:94-167,214-222`.
- Maehara: `handbook/annex/p07/interpolation-supplement.tex:7-120` supplies all initial placements, structural rules, the three one-premise and three two-premise propositional rules, both non-eigen quantifier rules, and all placements of the two eigenvariable rules, including the free-variable condition. The body correctly promotes only the partition lemma and leaves inherited Craig/Beth cited because the inherited cut-elimination premise is still a sketch (`cut-elimination-and-interpolation-supplement.tex:108-128,146-177`).
- Church--Rosser: `handbook/annex/p07/lambda-calculi.tex:4-124` now proves parallel reflexivity, capture-avoiding parallel substitution, complete development, the diamond property, equivalence of finite closures, the finite grid argument, and normal-form uniqueness.
- Propositional cut strategy: `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:94-152` fixes a maximal-rank/uppermost strategy; `handbook/annex/p07/arithmetic-proof-theory-supplement.tex:6-102` proves every leaf, commutation, contraction, and principal case and shows why duplicated internal cuts have lower rank. The natural-sum measure now decreases for the stated strategy rather than for arbitrary permutations.
- Haken: `handbook/annex/p07/proof-complexity.tex:5-47` gives the registered sketch—critical assignments, DAG routing, the source bottleneck lemma, charging, and the exponential conclusion—while explicitly listing the source lemma/counting details it omits.

### E6 — critical external source roles: pass, subject to F4

- `Alekseev2026`: the official Theory of Computing abstract calls an arbitrary-depth Frege superpolynomial lower bound a major open problem and an extended-Frege lower bound harder; it also says the paper's algebraic result does not itself give either Boolean lower bound. This exactly supports `proof-complexity.tex:124-137`. [Theory of Computing article](https://www.theoryofcomputing.org/articles/v022a004/)
- `AbelCoquandDybjer2007`: the author-hosted paper proves decidability of typed beta-eta equality via normalization by evaluation for MLTT with dependent functions and one Russell-style universe. The body now limits `thm:p07-mltt-normalization-decision` to that subcalculus and explicitly excludes Sigma, identity, and cumulative hierarchies (`lambda-calculi-and-type-theories.tex:419-451`). [Author-hosted paper](https://www.cse.chalmers.se/~peterd/papers/NbeMLTTEqualityJudgements.pdf)
- `JagerProbst2004`: Definition 1 and Theorem 2 state the displayed `PA-infinity` indexed derivability and the cut-elimination bound `2(0,alpha)=alpha`, `2(n+1,alpha)=2^{2(n,alpha)}`. The handbook formula at `arithmetic-proof-theory-supplement.tex:370-415` matches. [Article DOI](https://doi.org/10.1002/malq.200310097)
- `TroelstraVanDalen1988`: the cited Volume I, Chapter 3, section 5.6 is the standard source location for HA's disjunction and numerical-existence properties. The body now uses it only as an external proof source and explicitly refuses to infer the HA results from the smaller inherited normalization sketch (`functional-interpretations.tex:340-389`).

### E7 — active-sheet and symbol-surface mechanics: pass with F3/F7 qualifications

- location: active sheet references throughout the routed body; `handbook/registry/calculi/*.tex`; `handbook/registry/symbols.csv`; `handbook/generated/symbols-tables.tex`; `handbook/generated/symbol-index.tex`
- result: All 27 distinct `sheet:...` references on the current Part VII body route resolve to an active calculus sheet. The registry has 598 rows, of which 103 have Part VII scope or first use; every one of those 103 roles occurs in both generated symbol surfaces. F3 identifies new reader notation not yet represented by those otherwise one-to-one surfaces, and F7 identifies one sheet whose completeness claim exceeds its displayed rule surface.

## Residual findings

### F1 [blocker] [open] The new source-relative HA boundary is honest but does not fulfill the frozen `N-a-055` “with proofs” contract

- location: frozen requirement `spec/registers/new-content.csv:56`; open closure record `spec/register-obligation-closure.csv:197`; body `handbook/parts/p07/functional-interpretations.tex:325-389`; annex `handbook/annex/p07/functional-interpretations.tex:31-37`
- claim: The current body correctly leaves IPC disjunction, HA disjunction, and HA numerical existence at `cited=TroelstraVanDalen1988`, supplies only the cut-free LJ last-rule lemma locally, and expressly says it does not reproduce the HA proof-term grammar, equality/induction reductions, normalization, or erasure theorem. That is now source-faithful. It is not, however, the unchanged must-level obligation: `N-a-055` requires “disjunction and numerical existence properties for IPC and HA with proofs,” and its completion record remains OPEN with no supersession, destination, or fulfillment evidence.
- evidence: `functional-interpretations.tex:370-378` explicitly says the handbook does not provide the source formalism and does not label the three results locally proved. The frozen row says “with proofs,” while the closure record has an empty `contract_supersession_id` and `completion_status=OPEN`.
- exact correction: Either reproduce complete proofs against one exact IPC/HA calculus—including the equality and induction normalization/canonicity/erasure machinery required for HA—and give reciprocal `proved=` destinations, or formally supersede the frozen row with an authorized source-relative cited-treatment contract. Do not promote the present citation boundary; it is honest but incomplete relative to the current contract.
- status: open content-contract blocker.

### F2 [blocker] [open] The local ordinal table honestly defers, but no live master `A-074` table or supersession exists

- location: frozen requirement `spec/registers/apparatus.csv:75`; closure `spec/register-obligation-closure.csv:401`; local boundary `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:245-289`
- claim: The local six-row table is now accurately captioned as input to, not a substitute for, the master table, and it explicitly declines to place Robinson arithmetic or bounded-induction theories on its scale. That source boundary should be preserved. But `A-074` is a must-level table requiring Q-range fragments, PA, and stronger systems; it remains OPEN with no live master table anywhere on the handbook route and no contract supersession. Honest deferral is not completion under the charter's “every Part VII register commitment” criterion.
- evidence: The local rows begin at PRA and `I Sigma_n`; `arithmetic-proof-theory-supplement.tex:285-289` says the separate master must fix the lower endpoint. Repository-wide lookup found no live `A-074` implementation beyond this explicit deferral and the frozen/open control rows.
- exact correction: Supply the separate master table with defined lower-fragment presentations, one fixed calibration convention, and citation-qualified Q-range/PA/stronger rows, then bind `A-074`; or formally supersede/reassign that obligation before claiming Part VII content complete. Do not relabel the six-row local table as the master.
- status: open apparatus-contract blocker.

### F3 [must-fix] [open] The repairs introduce unregistered and colliding categorical/cut-measure notation

- location: new categorical syntax `handbook/parts/p07/normalization-and-curry-howard-supplement.tex:34-108`; new cut notation `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:94-124`; existing conflicting row `handbook/registry/symbols.csv:263`; generated symbol surfaces
- claim: The categorical repair introduces empty/unit types `mathbf 0`/`mathbf 1`, product/sum type formers, pair/projection/injection/case/abort constructors, and their typed beta-eta equality without a Part VII registry row. Bare `mathbf 0` is already registered as the computable Turing degree at `symbols.csv:263`, so the new empty-type use is not merely absent but collides with an existing global role. The cut repair likewise introduces `Cut(D)`, `A_c`, `h(c)`, `o(D)`, and Hessenberg natural sum `#` without registering their Part VII metalinguistic roles; the only registered `#` uses are later counting-complexity symbols.
- evidence: All 103 currently registered Part VII rows do occur one-to-one in both generated surfaces, but literal registry searches return no categorical-extension or cut-measure rows. Thus regeneration is internally consistent while still missing the newly introduced notation.
- exact correction: Prefer disambiguated typed glyphs such as `mathbf 0_ty`, `mathbf 1_ty`, and explicitly typed product/sum formers, then register the constructor/equality family. Register the cut-set, selected-cut fields, ordinal measure, and natural-sum operator as metalinguistic Part VII notation, with explicit disjointness from cardinality/counting and the P4 computable-degree role. Regenerate both symbol surfaces.
- status: open notation/source-standing defect.

### F4 [must-fix] [open] The Jäger--Probst bibliography identity is still malformed even though the theorem scope is correct

- location: `handbook/bib/handbook.bib:3530-3538`; consumers `handbook/registry/calculi/omega-arithmetic.tex:5` and `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:366,395,399-415`
- claim: The live BibLaTeX fields contain the literal byte strings `J{"a}ger` and `Sch{"u}tte`; the quotation mark is not preceded by the TeX accent backslash. They therefore do not correctly encode the names Jäger and Schütte.
- evidence: Automated scanning of all 57 live Part VII citation/status keys found zero missing keys and exactly one suspicious accent pattern: `JagerProbst2004 -> J{"a` with no TeX accent backslash. The DOI record identifies Gerhard Jäger and the title *Variation on a Theme of Schütte*. [Article DOI](https://doi.org/10.1002/malq.200310097)
- exact correction: Encode the fields with valid BibLaTeX accents, `J{\"a}ger` and `Sch{\"u}tte`, preserving article type, journal, volume/issue, pages, year, and DOI; regenerate bibliography-dependent surfaces.
- status: open bibliographic source-identity defect.

### F5 [must-fix] [open] The A-071 catalog still understates the newly proved canonical-LK completeness and uses a stale historical-part label

- location: `handbook/parts/p07/calculi-and-derivability-supplement.tex:39-92,229-267`, especially `:49-52,242-245`; counterevidence `:94-117,214-222` and `handbook/annex/p07/calculi-and-cut-elimination-supplement.tex:192-217`
- claim: The canonical-LK catalog row still says “completeness sketched” and does not mention the new proved `thm:p07-canonical-lk-completeness`, although the same current file and annex now present it as a complete proof. The structural table also calls the relevant inherited reduction “the Part-VIII reduction,” even though the reader route has moved that exact material into current Part VII and elsewhere refers to it by chapter/calculus. These are source/status-navigation inconsistencies inside A-071/A-070, not defects in the new proof.
- exact correction: Say that the inherited Part II completeness theorem retains its source sketch while the separate Part VII canonical-LK theorem is locally proved via `annex:p7.calculi.4`; preserve the no-cut-free/no-equality limitations. Replace “Part-VIII reduction” with the exact current chapter or `LK_d` inherited-reduction identity.
- status: open reader source-status defect.

### F6 [must-fix] [open] The hand route assigns Craig/Beth citation tokens that the exact source entries do not carry

- location: route table `handbook/parts/p07/proof-complexity.tex:226-245`; exact entries `handbook/restoration/inherited-11914-11960.tex:8-38`; generated evidence `handbook/generated/audit-p07.tex:44-45`; dormant-only tokens in `handbook/parts/p07/cut-elimination-and-interpolation.tex:222-239`
- claim: The route table prints `cited=Craig1957` and `cited=Beth1953` for the exact public theorem labels. The live exact artifacts instead carry generic “cited theorem” status and their adjacent reader proof routes cite Troelstra--Schwichtenberg and Hodges; the primary-key status tokens occur only in the dormant historical replacement file. The generated live audit correctly says `cited / source status`. The hand table therefore imports dormant metadata into exact-source identities.
- exact correction: Change the hand route cells to “source cited theorem” and name the actual live proof-route sources, or add a separately disclosed editorial primary-source note without pretending the exact inherited environment has those `cited=` tokens. Keep the exact bytes and generated status unchanged.
- status: open exact source-role defect.

### F7 [must-fix] [open] The selected Wansing sheet is only a worked-example core but the body attributes full K adequacy and cut to that displayed sheet

- location: `handbook/registry/calculi/display-k-wansing.tex:1-15`; worked example `handbook/parts/p07/structural-extensions.tex:178-197`; theorem `:220-224`; catalog `handbook/parts/p07/calculi-and-derivability-supplement.tex:280-285`
- claim: The sheet's own header says it is a “display core” and lists exactly the rules used by the worked example. It omits the full classical/display logical and structural rule surface required for a soundness, completeness, and cut-admissibility theorem for modal K. The worked three-rule cycle is reconstructible and honestly does not claim K adequacy, but `thm:p07-display-k-adequacy` then says the “selected display calculus” is sound and complete for K and cut-admissible. A fragmentary lookup cannot be the exact calculus to which Wansing's full metatheorem applies.
- evidence: The sheet displays only identity, implication, modal display/Box rules, and a small structural subset; unlike the GS5 and labelled sheets, it contains no clause importing the complete remaining source calculus. Wansing's cited paper concerns a complete sequent/display presentation, not merely the three rules used by this example. [Wansing article DOI](https://doi.org/10.1093/logcom/4.2.125)
- exact correction: Either reproduce/import the full exact Wansing K calculus and state precisely which source theorem applies to it, or rename the sheet as a worked-example fragment and attach adequacy/cut only to the full external presentation, explicitly denying that the fragment itself is complete.
- status: open fixed-calculus/source-scope defect.

### F8 [needs-evidence] [open] The broad MLTT sheet still gives the narrowed Abel--Coquand--Dybjer source a file-wide controlling role

- location: `handbook/registry/calculi/mltt-intensional.tex:1-58`, especially `:5`; body scope `handbook/parts/p07/lambda-calculi-and-type-theories.tex:399-451`
- claim: The body now correctly distinguishes the broad editorial sheet (Pi, Sigma, identity, and cumulative universes) from the Abel--Coquand--Dybjer dependent-function/one-universe theorem. The sheet itself nevertheless labels `MartinLof1984,AbelCoquandDybjer2007` jointly as its controlling source across the whole displayed rule surface, including the custom multi-sorted congruence schema and cumulative Sigma/Id universe closure. Abel--Coquand--Dybjer does not support those broader rows; the body instead invokes Martin-Lof, Nordstrom--Petersson--Smith, and Hofmann for the family boundary.
- exact correction: Mark the sheet explicitly as an editorial composite and give rule-cluster source roles: broad judgment/constructor/universe sources for the sheet, with Abel--Coquand--Dybjer attached only to typed equality and the narrowed subcalculus. Supply exact locators for the custom congruence and cumulative-universe presentation or replace it with a single published matched calculus.
- status: needs exact source-to-rule evidence; nonblocking only if the chair records it as an editorial composite rather than a source-matched sheet.

## Coverage by requested criterion

- 19 exact artifacts/order/bytes: checked clean (E1).
- reader source map: checked clean (E2).
- derivative standing: checked clean after disclosed derivative revisions (E2).
- governed source anchors: checked clean, 31 units and 11 results (E3).
- live generated Part VII register: checked clean, 128 reachable rows and no dormant row (E3).
- named-result index: checked clean, all 39 editorial and 11 exact governed results (E3).
- every body status/annex backreference: checked clean, 39 body results and 10 reciprocal annex items (E4).
- cited source roles/bibliography: critical roles checked; Alekseev, ACD, and Jäger--Probst scopes pass; F4, F6, F7, and F8 remain.
- active sheets and route table: all 27 sheet labels resolve; F5-F7 remain.
- notation/registry/generated surfaces: existing 103 Part VII rows are one-to-one; F3 remains for notation introduced by repairs.
- new source-relative HA boundary: source-faithful but frozen-contract-incomplete (F1).
- deferred master A-074 boundary: source-faithful deferral but no fulfillment/supersession (F2).
- reader-visible OPEN/unadmitted/stub/internal-workflow prose: checked clean; remaining uses of “open” are mathematical open problems, open assumptions, or comments.
- compilation, PDF navigation, visual inspection, administrative admission, human review, and user acceptance: deliberately not run or inferred.

## Required repair order

1. Resolve the two frozen contract blockers, F1 and F2, by fulfillment or authorized supersession.
2. Register/disambiguate the new notation and correct the Jäger--Probst identity (F3-F4), then regenerate the affected symbol/bibliography surfaces.
3. Align the catalog and exact source-role table with the live statuses (F5-F6).
4. Make the Wansing and MLTT sheet/source boundaries exact (F7-F8).
5. Re-run only the later static/build/visual/human/user gates after source/content bytes freeze.

REJECT
