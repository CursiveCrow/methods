# Edition 2026 planning coverage audit

Date: 7 September 2026. Scope: coverage and acceptance conditions in the approved completion plan. This is a bounded planning audit, not a new manuscript census, progress audit, or acceptance of the book. Only this note was written.

## Assessment

The nineteen-part architecture is suitable for the user's broad reference of reasoning and logic. Its five new parts cover the principal gaps in the old formal-logic-centered manuscript, and its distinction between reference entries and full attributed treatments is appropriate. The 26 initial chapters are a real organizational outline. They are not yet a decision-complete coverage catalog: several topic assignments and pass/fail rules still depend on unstated choices.

During this audit, root supplied the new EDITION-2026-WORK-PACKAGES.md. Its targeted read-back substantially addresses several recommendations below. The final update at the end of this note controls which recommendations remain planning gaps; the original ten observations are retained as their evidence trail.

The recommendations below concern explicit catalog and acceptance decisions. They do not require reproducing every chapter of a benchmark handbook, treating every citation as a missing proof, or extending the book into entire applied disciplines.

## Material read

All lines of the three assigned local files were read sequentially:

| File | Read range | SHA-256 at reading |
| --- | --- | --- |
| spec/EDITION-2026-EXECUTION-PLAN.md | 1–304 | AA39A98636AD6844C142BE99D328A0BD0C9FC8919DEBBFFCB1987B73154553EC |
| spec/EDITION-2026-CONTRACT.md | 1–168 | C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3 |
| spec/inventory/2026-09-06/MANUSCRIPT-INVENTORY.md | 1–150 | 7B91900D42309009F05361532BF8730DD9502619DD9E90151FCB99D8D1C5452C |

The inventory is used as the plan's stated baseline. Its historical “authoring stopped” and fourteen-part snapshot language was not treated as current task status; root is separately checking progress and ownership.

### Primary publisher comparison

**CRC Handbook of Chemistry and Physics, 107th edition (2026).** The [Routledge publisher page](https://www.routledge.com/CRC-Handbook-of-Chemistry-and-Physics/McEwen/p/book/9781041194620) describes expert evaluation, standardized representations and organized tables, and exposes contents concerning evaluation, uncertainty, nomenclature and retrieval. This supports the plan's reference-function analogy. It does not establish a requirement that a logic handbook imitate chemical data tables or reproduce all external literature. Direct page fetches returned 403; the publisher-owned description and contents were accessible through the web tool's indexed extraction. The returned contents skipped some numbered sections, so a complete CRC contents audit is not claimed.

**The Handbook of Rationality (MIT Press, 2021).** The [publisher description](https://mitpress.mit.edu/9780262045070/the-handbook-of-rationality/) explicitly integrates normative and descriptive accounts and identifies theoretical, practical and cross-cutting rationality. Its described scope includes resource limitations and links among rationality, law and morality. The publisher links a [three-page contents PDF](https://mitp-content-server.mit.edu/books/content/sectbyfn?collid=books_pres_0&fn=toc.pdf&id=11252). That PDF was reachable but had no extractable text; its page images were not available for actual reading in this tool context. Therefore this audit verifies MIT's publisher-described breadth, not its full chapter-by-chapter contents. The open-access edition link is a source-acquisition lead, not a claim that its full body was read.

**The Oxford Handbook of Thinking and Reasoning (Oxford University Press, 2012).** The [publisher's actual contents](https://academic.oup.com/edited-volume/34559) were read through chapters 1–40, including the general approaches, inference, judgment, problem solving, developmental/cultural, modes-of-thinking and applied groups. The website exposes topics extending beyond the plan's explicit labels: representation/categorization, neural and computational accounts, motivational influences, creativity/insight, linguistic/cultural variation and transfer. These are chapter-level coverage evidence, not an independent review of their empirical conclusions. No chapter body is claimed read. The [publisher preface](https://academic.oup.com/edited-volume/34559/chapter/293245832) also identifies the reference audience and the need to update a changing research field.

## Ten concrete planning recommendations

### 1. Define the finite catalog's inclusion and freeze decision

Evidence: [plan:27–46](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:27), [contract:31–42](C:/Dev/the-methods-of-reason/spec/EDITION-2026-CONTRACT.md:31). “Major,” “substantive coverage record,” “required topic,” and “bounded content unit” do not yet specify how an overlooked pre-cutoff candidate becomes an obligation. The source-date cutoff alone does not make that decision finite.

Recommendation: record a reviewed method-family/topic list, exact benchmark editions and contents ranges, the inclusion rationale for each new candidate, and a freeze decision. Preserve all already owed components. Distinguish a previously owed obligation from a new external lead whose relevance still needs a decision.

Pass: every assessed candidate has a reproducible disposition and every admitted family has a finite component list. Fail: an arbitrary newly discovered old title automatically expands the edition, or a substantive lead is renamed metadata merely to close reconciliation.

### 2. Require a benchmark crosswalk, including its unread cells

Evidence: [plan:42–46](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:42). The plan names handbook families and two reasoning benchmarks, but the success rule does not require a topic-by-topic crosswalk or record partial contents access.

Recommendation: add one reviewed crosswalk from each selected benchmark topic to an existing requirement, new catalog unit, justified comparison, or reasoned nonselection. Record the precise edition and whether the evidence is publisher description, contents, or technical body. Complete the MIT contents reading before marking that benchmark reconciled.

Pass: all selected benchmark rows have explicit mappings and unresolved-access cells remain visible. Fail: a publisher description or chapter heading is treated as a full coverage check.

### 3. Make the remaining cognitive families explicit within P19

Evidence: [plan:62](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:62), compared with the Oxford contents, especially chapters 4–11, 20, 23–24, 28–29 and 40. P19 now expressly includes problem solving and visual/spatial reasoning, but the other families identified in the publisher comparison remain implicit.

Recommendation: allocate representation/categorization and computational/neural accounts to E1/E2; creativity and insight to E4/E5; motivational influences to E2/E3; and linguistic/cultural variation and transfer to E6, or record another justified allocation. No extra part is necessary.

Pass: each family has defined source presentations, questions and evidence requirements. Fail: broad words such as “expertise,” “development” or “problem solving” are credited without identifying the corresponding intellectual units.

### 4. Specify resource-bounded and machine-assisted reasoning

Evidence: [plan:60](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:60), [plan:209](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:209), and MIT's publisher-described treatment of bounded rationality. The chapter list gives idealized preference/decision foundations; AI-assisted reasoning appears only as a phrase in the P12 stream.

Recommendation: give resource-bounded choice and metareasoning explicit P17/P19 units, and enumerate the P12 AI-assisted scope: generation versus search, retrieval-supported claims, proof reconstruction/certification, uncertainty/calibration and human verification. Keep contemporary empirical performance claims dated and task-specific.

Pass: finite inputs, objectives, resource restrictions and warranted outputs are specified. Fail: an ideal optimizer or a successful generated answer is treated as evidence about bounded agents or certified reasoning generally.

### 5. Extend the statistical acceptance scenarios to data and procedure assumptions

Evidence: [plan:58](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:58), [plan:230–231](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:230). The existing odds and interval-interpretation examples are useful but do not establish the validity of U4–U6 procedures.

Recommendation: require the estimand, sampling/data-generation model, selection and stopping rules, applicable error or predictive guarantee, and sensitivity/robustness conditions for each statistical method. Include concrete failure cases for dependent/unrepresentative samples, selection or multiple comparison, and model misspecification wherever applicable.

Pass: the numerical conclusion follows under the stated data/procedure assumptions and the failure case shows their role. Fail: correct arithmetic alone licenses an inferential claim about a population or model.

### 6. Give causal identification a stronger pass/fail case

Evidence: [plan:59](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:59), [plan:233](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:233). Distinguishing conditioning from intervention is necessary but does not by itself establish C4's promised identification-and-estimation development.

Recommendation: require one positive identification derivation under its exact graphical/structural assumptions and one pair of admissible causal models with the same observational distribution but different target effects. Require an explicit hypothesis-preserving bridge when comparing structural and potential-outcome presentations.

Pass: the entry tells the reader when the target is identified, what formula identifies it, and which assumptions make estimation relevant. Fail: a confounding illustration or fitted association is presented as an identification result.

### 7. Add a distinct normative-argument acceptance rule

Evidence: [contract:67–74](C:/Dev/the-methods-of-reason/spec/EDITION-2026-CONTRACT.md:67) distinguishes formal, normative and empirical claims, but [plan:263–270](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:263) names only mathematical or empirical validity. The philosophy stream's “without warrant” condition at line 208 is too indefinite for reviewers.

Recommendation: require explicit evaluative aims, normative premises, scope, inference to the recommendation, and relevant competing positions/objections. Apply it to rational choice, practical/legal argument and the relation of rationality to moral judgment. Preserve distinct source positions.

Pass: the recommendation is warranted conditional on its declared standards. Fail: a preference axiom is reported as an empirical law, a descriptive regularity becomes an “ought,” or a disputed normative conclusion is presented as an unqualified theorem.

### 8. Define empirical evidence selection and conflict evaluation

Evidence: [plan:84](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:84), [plan:236](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:236), [contract:70–72](C:/Dev/the-methods-of-reason/spec/EDITION-2026-CONTRACT.md:70). Required reporting fields are present, but there is no procedure for selecting a representative evidence set or evaluating contradictory findings.

Recommendation: record the search/corpus cutoff, inclusion criteria, study/task comparability, methodological limitations, effect estimates and uncertainty, and treatment of replication, publication/selection bias and conflicting results. An unreplicated result may be reported at its actual standing; lack of replication must not be hidden or mechanically converted into a universal prohibition.

Pass: another reviewer can reconstruct why the cited evidence set and strength of conclusion were chosen. Fail: a favorable study is selected without explaining the competing evidence or a broad claim exceeds the populations/tasks examined.

### 9. Test reference usability with actual reasoning questions

Evidence: [plan:5–7](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:5), [plan:244–257](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:244). Dual reachability and an index count do not establish the CRC-like function of finding the appropriate qualified result.

Recommendation: add a fixed set of manual lookup scenarios spanning each method family. Examples include handling inconsistent premises; distinguishing a decider from a semidecision procedure; evaluating evidence versus selecting an action; identifying a causal effect; and choosing a statistical guarantee. Review the entry, assumptions, alternative methods and full-treatment route returned.

Pass: the lookup gives relevant methods and the conditions limiting their conclusions. Fail: links resolve but the route omits an applicable family, conflates different tasks or recommends a method whose assumptions the query violates.

### 10. Define required source extent and update handling per obligation type

Evidence: [plan:76,86](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:76), [plan:190–192](C:/Dev/the-methods-of-reason/spec/EDITION-2026-EXECUTION-PLAN.md:190), [contract:21–42](C:/Dev/the-methods-of-reason/spec/EDITION-2026-CONTRACT.md:21), and [inventory:118–134](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/MANUSCRIPT-INVENTORY.md:118). “Full required extent” needs a claim-level definition; the baseline contains many citation-only records and explicit source-sketch boundaries.

Recommendation: distinguish a full source presentation, a required supplied proof, a cited dependency, a historical attribution, and an empirical evidence set. For each, fix the pages/claims needed to verify it and the local capture/hash requirements, including HTML or scanned sources. Also state how errata/retractions or corrections discovered after the cutoff affect an existing claim, without automatically adding new topics.

Pass: source access is sufficient for the obligation actually asserted, all promised proofs remain owed, and changed evidence reopens the affected claim. Fail: a contents page passes as a technical body, every citation silently creates an obligation to reconstruct a whole monograph, or the cutoff preserves a known erroneous or retracted claim unchanged.

## Recommended planning disposition

Retain the approved architecture and its substantive scope. Before declaring the edition catalog frozen, resolve recommendations 1–4 and 10 in the catalog and its source crosswalk. Add recommendations 5–9 to the relevant chapter/entry dispatch and review conditions. These are explicit finishing conditions, not reasons to stop well-scoped correction work already authorized by the plan.

Only this Markdown note was written. No manuscript, plan, contract, register, bibliography or review record was changed. No agents, tests, builds or manuscript renders were used. The source-only MIT contents extraction returned no text; an attempted source-image forwarding route was unavailable, so no visual reading of that PDF is claimed.

## Final update against the newly supplied work packages

The supplemental planning file was evolving while it was read. The final observed snapshot had 442 lines and SHA-256:

    93F735C95CB7635E1FDA7A0058CDD419FB97B84335CAA15B03E7BB8A7C608209

I read the CAT-01 definition and conditions, relevant source/benchmark paragraphs, all five new-part tables, entry/comparison standards, apparatus conditions and admission gates. I did not conduct a full ownership/progress audit of this additional file.

The following recommendations are now substantially represented in the work-package plan:

- **Recommendation 2:** [lines 220–226](C:/Dev/the-methods-of-reason/spec/EDITION-2026-WORK-PACKAGES.md:220) explicitly require accessible-contents evidence and CAT-01's unit-level crosswalk. Completing that mapping remains catalog work; it is no longer an omitted planning requirement.
- **Recommendation 5:** [U1–U6, lines 271–276](C:/Dev/the-methods-of-reason/spec/EDITION-2026-WORK-PACKAGES.md:271) now name null-event/support, misspecification, multiplicity/stopping, leakage/shift, dependent evidence and publication-bias cases. Specific source units must instantiate them, but the area-level acceptance omission is addressed.
- **Recommendation 6:** [C4, line 289](C:/Dev/the-methods-of-reason/spec/EDITION-2026-WORK-PACKAGES.md:289) now requires identified and nonidentified cases and the appropriate causal assumptions. The two-model witness remains a concrete way to discharge a claimed nonidentifiability result, not a request for another chapter.
- **Recommendation 7:** [PHIL, line 245](C:/Dev/the-methods-of-reason/spec/EDITION-2026-WORK-PACKAGES.md:245) requires argument, assumptions, objections and replies; [the topic gate, line 379](C:/Dev/the-methods-of-reason/spec/EDITION-2026-WORK-PACKAGES.md:379) now includes argumentative evidence. Apply that same discipline to normative P17/P18 units.
- **Recommendation 9:** [APP-06 and lines 365–371](C:/Dev/the-methods-of-reason/spec/EDITION-2026-WORK-PACKAGES.md:365) provide actual reader tasks, expected answers fixed in advance, and an independent usability review. This planning gap is addressed.
- Representation and insight are now explicit in [P19-E5, line 328](C:/Dev/the-methods-of-reason/spec/EDITION-2026-WORK-PACKAGES.md:328); do not continue to list them as missing chapter coverage.

### Concrete topic-to-chapter decisions still needed in CAT-01

These are explicit catalog assignments or reviewed scope decisions, not demands for additional parent chapters. They follow from the already cited publisher breadth comparison and the current chapter tables.

| Topic family needing an explicit disposition | Suitable existing home | Required boundary |
| --- | --- | --- |
| Cognitive representation, categorization and similarity | P19-E2/E4, with E5 for problem representation | Distinguish empirical accounts from formal knowledge-representation systems and algorithmic learning in P9/P15. |
| Computational and neural methods for studying reasoning | P19-E1/E2 | Identify the methods and inferential limits actually needed; a reviewed choice can exclude specialist genetic/clinical subfields without pretending they are non-content metadata. |
| Motivational and affective influences on judgment | P19-E3/E6 | Name the tasks, measured effects, rival accounts and limits; do not subsume the entire family silently under “biases.” |
| Language and cultural variation in reasoning | P19-E2/E6 | Separate task interpretation, linguistic representation and sampled cultural/population differences. |
| Creative generation and learning transfer | P19-E5/E6 | Insight and transfer limits are already named; identify whether constructive creativity and positive transfer mechanisms have their own required units. |
| Resource-bounded rationality and metareasoning | P17-D2/D3, with P19-E3 for behavior | State resource costs, stopping/selection criteria and conditional normative standards. |
| Practical/legal and moral reasoning | P18-A4 and appropriate P17/P19 units | Limit coverage to reasoning principles and evidence; distinguish institutional, normative and empirical claims without opening entire applied disciplines. |
| AI-assisted reasoning | P12 AUTO, linked to P15/P19 | The phrase is present at line 246; CAT-01 still needs finite method/evidence units distinguishing generated claims, search, retrieval and independently checked proof. |

The remaining cross-cutting finishing decisions are therefore the catalog's inclusion/freeze rule, the explicit dispositions in this table, empirical corpus-selection/conflict criteria, and source-extent/update rules appropriate to each obligation type. The improved work packages already provide the main area-level pass/fail scenarios and reference-usability gate. No further acquisition or chapter-body reading was attempted after root's stop instruction.
