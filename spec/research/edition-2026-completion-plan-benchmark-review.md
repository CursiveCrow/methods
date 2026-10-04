# Completion-plan benchmark review

Date: 7 September 2026. Bounded research/planning review, approximately 23:30--23:38 UTC. Owner: `standard_pa_argumentation_publication_review`. This note is the sole write; no manuscript, implementation, shared plan, test, rendering, or agent state was changed.

## Assessment

The nineteen-part plan supports the intended reference: it combines established logic with probabilistic, causal, strategic, informal, and empirical reasoning; preserves complete treatments; and requires subject and task lookup. The main improvements are explicit finite benchmark decisions and stronger acceptance cases for the actual lookup artifact. The external contents do not justify adding a new part or treating an entire external handbook as an automatic transcription obligation.

The complete edition contract and the complete initial 703-line work-package plan were read. The root then refreshed the starting state and immediate queue during this review. The updated starting-state section and NOW-01--12 queue were reread directly. Earlier NEXT-queue findings are therefore withdrawn: the refreshed section 5 explicitly supersedes them. This review does not independently reaccept the manuscript status claims in that refreshed queue.

## Official benchmark evidence and its exact extent

All external checks used current official publisher pages or their search-indexed contents. None was a full-book reading.

| Benchmark | Evidence actually obtained | Planning implication |
| --- | --- | --- |
| CRC Handbook of Chemistry and Physics, 107th edition, 2026 | The publisher's contents/features identify evaluated tables, standardized names/units, nomenclature, and uncertainty guidance. Its official help distinguishes document browsing from compound/property search. Direct opening sometimes failed; the official page's indexed contents and help text were available. [Publisher](https://www.routledge.com/CRC-Handbook-of-Chemistry-and-Physics/McEwen/p/book/9781041194620), [official help](https://hbcp.chemnetbase.com/help/tour.xhtml). | Use this as an organization/lookup benchmark: precise typed entries, qualifications, synonyms, and multiple routes to the same maintained result. |
| The Handbook of Rationality, 2021 | MIT's description explicitly covers normative/descriptive and theoretical/practical rationality. The official chapter identity for public understanding of science was also verified. The linked three-page contents PDF returned no text; its complete contents were not read in this block. [Publisher](https://mitpress.mit.edu/9780262361859/the-handbook-of-rationality/), [chapter 14.3](https://direct.mit.edu/books/oa-edited-volume/5525/chapter/4090515/Rationality-and-the-Public-Understanding-of). | Preserve the plan's distinct evidence standards. Add an explicit scope decision for public understanding of science and reliance on expert testimony. Complete the exact-edition contents crosswalk separately. |
| The Oxford Handbook of Thinking and Reasoning, 2012 | Official contents include gesture, aging, clinical thought disorder, medical reasoning, and knowledge transfer, alongside the already named core families. [Oxford contents](https://academic.oup.com/edited-volume/34559). | Give these boundary populations, representations, and applications explicit finite inclusion/nonselection decisions under P19 and the relevant P18 links. A broad cognition heading does not record the decision. |
| Handbook of Mathematical Logic | The official publisher presents model theory, set theory, recursion theory, and proof/constructive mathematics. Its displayed 1982 product manifestation must be distinguished from the 1977 volume's original publication. [Publisher](https://shop.elsevier.com/books/handbook-of-mathematical-logic/barwise/978-0-444-86388-1). | The existing core streams cover this organizational division. Pin exact manifestations in the benchmark list; this page supplies no chapter-body acceptance. |
| Handbook of Automated Reasoning, 2001 | Official contents separately identify inverse methods, automated induction, inductionless induction, and higher-order unification/matching, in addition to the listed standard automation subjects. [Publisher contents](https://www.sciencedirect.com/book/edited-volume/9780444508133/handbook-of-automated-reasoning). | Require explicit CAT-01 dispositions for these method families. Their treatment cannot be inferred solely from generic “unification,” “proof theory,” or “automation” headings. |

The CRC online service is a useful analogy, but the contracted deliverable remains the integrated PDF and maintained sources. These findings do not require building a separate website.

## Concrete proposed edits

Line references below refer to the concurrently refreshed work-package snapshot observed at approximately 23:36 UTC, SHA-256 `270DF9A21AFD0742CB354D883037227870E56A614E45F5C5F341EA127FAEC1AE`. Stable section/task names are supplied because the lead is actively editing this file.

### 1. Give every benchmark a role and exact edition before using it as a denominator

Relevant text: `EDITION-2026-WORK-PACKAGES.md:19`, CAT-01 at lines 150--155, and section 6's benchmark paragraph.

Add a finite benchmark manifest within the existing catalog work, recording `benchmark_role` as organization/lookup, subject coverage, or technical authority; exact edition/manifestation; publisher locator; accessible extent; and the crosswalk rows required. CRC supplies the first role. Logic, rationality, and cognitive handbooks supply declared subject-coverage leads. A technical theorem claim still needs its actual identified primary treatment.

**Pass:** every selected benchmark has an exact identity and role, every required contents row has a mapped unit/comparison or independently reviewed nonselection, and inaccessible rows remain explicit. **Fail:** a series title stands for an unspecified set of volumes, a product-page summary closes a chapter crosswalk, or chemistry contents become reasoning obligations merely because CRC supplied the design analogy. This sharpens the plan's existing boundary rather than expanding its subject list.

### 2. Add four explicit automation-family decisions

Relevant text: AUTO stream at `EDITION-2026-WORK-PACKAGES.md:328`, and the method-family decision table beginning at line 375.

Add CAT-01 decision rows for inverse methods, automated proof by induction, inductionless induction, and higher-order unification/matching. Each row can map to an already owed unit, add a specifically justified component inside P7/P12, or record reviewed nonselection under the existing rule. The official automation contents identify these as distinct treatments; no claim is made here that the live manuscript lacks them.

**Pass:** each included method has an exact problem and input language, solution/proof notion, assumptions, promised correctness/completeness and termination scope, and a separating failure case; its source-specific obligations are accounted for. **Fail:** a first-order procedure is silently credited for a higher-order regime, or the existence of an induction principle is credited as an automated induction procedure. These are proposed acceptance cases, not technical results established from the contents page.

### 3. Close explicit empirical and application scope decisions

Relevant text: P19-E5/E6 at `EDITION-2026-WORK-PACKAGES.md:459--460`, the cross-part families table, and P18-A4.

Add bounded decisions for gesture/embodied representation; aging and clinical boundary populations; medical reasoning as an application/transfer case; and public understanding of science/expert testimony. Existing P19/P18 units may satisfy these decisions after their actual component mappings are checked. No new chapter is required solely because an external contents entry names the topic.

**Pass:** each decision records the reasoning question, selected population/task or normative issue, exact included source/evidence extent, destination, and either its supplied components or a reviewed nonselection rationale explaining the covered inference principle. **Fail:** general-population evidence is silently extended to a distinct boundary population, or an application title is mapped to a chapter without identifying which reasoning principle and limits are covered.

### 4. Test each method's decision boundary through both lookup routes

Relevant text: APP-01 and APP-06 at `EDITION-2026-WORK-PACKAGES.md:524` and `:529`; current APP-06 executes cases per chapter/family while every method is only structurally checked for reachability.

Require a finite lookup-case matrix keyed by admitted method and materially distinct assumption regime. For every method, supply a positive applicability case and a case requiring rejection, qualification, or an explicit “insufficient information” result. Shared cases may cover several methods only when their expected answers and differing prerequisites are enumerated. Keep the existing per-chapter subject lookup as a navigational check.

**Pass:** a fresh reviewer starts with the declared question and information, reaches the correct maintained entry through both subject and task/property routes, identifies the applicable guarantee and its limitation, and can follow the exact full-treatment/proof destination. Expected answers are fixed before inspection. **Fail:** a route merely reaches a relevant-looking chapter, hides a disqualifying hypothesis, or requires knowledge of an internal label or the author's intended answer. The matrix closes when every required case passes; chapter-level sampling alone does not establish method-level use.

### 5. Add PDF search and text integrity to publication acceptance

Relevant text: APP-02/04/05, APP-06, and PUB-01; the common reference standard already requires stable terms, symbols, sources, and full-treatment links.

Add an explicit final-PDF check for representative aliases, core method names, symbols with text equivalents, and theorem/status labels. Verify ordinary reader search, bookmark/index navigation, and copying of selected mathematical statements and their hypotheses. Include cross-part comparisons and the most demanding table layouts in the sample; structurally enumerate all required search aliases in the generated apparatus.

**Pass:** search and index routes lead to the expected entries in the exact publication PDF, extracted/copied statements retain the meaning of essential symbols and hypotheses, and link targets match the admitted treatment. **Fail:** visually plausible glyphs have broken text encoding, a synonym is only recognized by internal source search, or apparent search success hides a wrong edition/variant. A full PDF accessibility standard would be a separately specified production target; this recommendation makes no unverified conformance claim.

## Bounded agent distribution for these edits

Preserve one lead plus at most three concurrent subagents and the current authoring/review rotation. These are additions to CAT-01/APP/PUB dispatch conditions, not four extra permanent roles.

| Assignment | Owner and output | Exact exit condition |
| --- | --- | --- |
| Benchmark identity/crosswalk intake | One catalog/source seat; exact benchmark identities, roles, accessible contents, and unresolved rows in the existing catalog mechanism. | All selected benchmark identities/roles fixed; every assigned contents row mapped or explicitly unresolved; no body-reading claims inferred from contents. |
| Automation and empirical family decisions | One relevant specialist at a time, in two disjoint bounded batches; proposed component mappings and reviewed inclusion/nonselection requests. | Each named family has an exact finite decision and required question/cases; the lead resolves the admission policy after the prescribed independent reviews. |
| Lookup case construction | One apparatus seat; a finite expected-answer matrix for one frozen group of admitted methods. | Every method/regime in that group has the two route cases and its disqualifying or insufficient-information case. |
| Lookup/publication review | Fresh reviewer contexts within the existing three-seat limit, after expected answers and artifact hashes are frozen. | Actual destinations, guarantees, exclusions, PDF search/text behavior, and all assigned failures recorded against the exact artifact. |

The root's refreshed NOW-01--12 queue is materially more dispatchable than the superseded NEXT queue. Maintain the same current task identities in section 13 and the milestone table. A source-preparation seat and a three-reviewer batch cannot occupy four simultaneous subagent slots: complete or release the source seat before the full three-seat review wave, or explicitly schedule fewer reviewers concurrently. This is a scheduling clarification; the existing three-review independence requirement remains unchanged.

## Limits and provenance

The edition contract hash read in full was `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3`. The inspected main driver hash was `58209C822E1344274E65E10D0E9DC41D059EC7973CB63464BD7E18666E747429`; its lines 23--40 show the available sixteen-part route. The root corrected the plan's starting-state text during this review, and this note retains no stale finding that all five new parts remain absent.

The research skill supplied the primary-source and single-note workflow. The assignment's explicit no-delegation instruction governed execution. No source body was claimed fully read from an abstract, description, contents list, or indexed excerpt. The MIT contents PDF's lack of extracted text remains an access/inspection limit for this block. The recommended decisions are planning findings; they grant no catalog freeze, manuscript admission, production acceptance, or release approval.
