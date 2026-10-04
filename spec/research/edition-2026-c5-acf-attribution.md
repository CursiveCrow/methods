# Edition 2026 C5 / S-011: active ACF categoricity attribution

Date: 7 September 2026. This is an author/source note for the bounded result, status and attribution repair. It is not independent acceptance or a reconstruction of the entire Steinitz paper.

## Assigned scope and frozen identities

Owned manuscript: handbook/restoration/inherited-07295-07468.tex. Only the ACF example immediately following the reviewed DLO theorem/proof was changed. Its original active range was 177–185; the corrected theorem and source explanation occupy 177–218.

Predecessor whole-file SHA-256, already containing the reviewed DLO proof:

    1958B3363DCAC80B5C7AF56F446E74591B4249D23C1C8543CC9EC7DE7BB93A89

Final whole-file SHA-256:

    A133AD43A7AF91BEC6DC90B1AC5335F0524C1447869CB382B05175138A9C0505

The protected DLO substring is lines 108–176: from the first byte of its theorem opening through its proof and following blank line, stopping immediately before the ACF opening. Its UTF-8, LF-only byte length is 3,539. Both before and after this edit its SHA-256 is:

    9AC556285A7ABB3F42E7652606A28BE92EE3C50102F5F045FB9805A20617A213

The entire prefix before the ACF result and the suffix beginning with the Ryll–Nardzewski theorem were also compared as actual strings and are unchanged. The final prefix SHA-256 is:

    32728FB93449503B1DFE1B47C934F06F48E559E885869FC04AF28B0925E8BC2A

The final file has 250 lines. Its complete current contents were read back with line numbers after the edit; no line of the final file remained unread. No test, build, manuscript render, provenance migration or shared-file edit was performed.

## Requirement and existing evidence

Original S-011 requires promoting the uncountable ACF_p categoricity example to a labelled statused result with direct Steinitz attribution. The current component inventory recorded the active example as missing its local label/status and direct citation; the separate classification table's Steinitz citation was only partial evidence.

Read as leads:

- spec/inventory/2026-09-06/complete-requirement-ledger.json, S-011 and its current component findings;
- spec/research/p03-steinitz-citation.md, the earlier source-locator note;
- inactive handbook/parts/p03/qe-categoricity-games.tex:282–293, the former intended theorem and explanation;
- active handbook/parts/p03/qe-categoricity-games-supplement.tex:59–83, the classification-table citation route;
- current handbook/parts/p03.tex:49–59, which routes the restoration file and supplies ordinal hooks for Ryll–Nardzewski and Morley;
- handbook/bib/handbook.bib:4000–4011, the existing Steinitz1910 record.

No ACF proof item was located in the current P3 annex fragments. The old theorem was already cited-only and needed no annex destination. No inactive result or old note was treated as current source-body evidence.

## Primary source actually read

Ernst Steinitz, “Algebraische Theorie der Körper,” Journal für die reine und angewandte Mathematik 137 (1910), 167–309, DOI [10.1515/crll.1910.137.167](https://doi.org/10.1515/crll.1910.137.167).

The current holdings inventory has no local PDF candidate for Steinitz1910. This task read the SUB Göttingen's live page OCR from the primary journal digitization, rather than claiming to have read an unavailable local PDF. The HTML OCR contains imperfect German and mathematical glyph recognition; the assertions used here are identifiable in their section/result context.

| Printed page and source locator | Live primary-page endpoint | Evidence used |
| --- | --- | --- |
| 287, §21(9) | [GDZ scan page 291 text](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000291?_format=xml) | Algebraic closure exists and is unique up to an isomorphism extending the given base-field isomorphism. The theorem and its explanation appear on this page. |
| 288, opening of §22 | [GDZ scan page 292 text](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000292?_format=xml) | Definitions and finite character of algebraic dependence; confirms that this page starts the next section rather than continuing §21(9). |
| 289, §22(5) and its preceding construction | [GDZ scan page 293 text](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000293?_format=xml) | Purely transcendental extensions are constructed from arbitrary sets of indeterminates; equal-cardinality independent systems give equivalent extensions. |
| 299, §23 and item 3 | [GDZ scan page 303 text](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000303?_format=xml) | Cardinal invariance of the independent generating system and definition of transcendence degree. |
| 300, §23 before items 5–6 | [GDZ scan page 304 text](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000304?_format=xml) | Absolute degree over the prime field; classes indexed by characteristic zero or prime and finite or transfinite degree; construction of a rational-function type and an algebraically closed algebraic extension in each class. |
| 301, §23(6) and §24 | [GDZ scan page 305 text](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000305?_format=xml) | A unique algebraically closed type in each characteristic/degree class; uncountable field cardinality equals absolute transcendence degree; cardinal argument explicitly invokes well-ordering. |

These six page responses were retrieved successfully with ordinary read-only requests and read as complete page text. They supply the needed source statements and their local explanations. The earlier 1910 article record and first-page text identify the author, title and original volume 137. The publisher's archival metadata uses volume 1910/issue 137; the existing canonical record correctly retains the original printed volume 137.

Access limitation: the old article resolver URL and a direct volume-page request returned a not-found response in this run, while the primary OCR endpoints above worked. The old DigiZeitschriften PDF URL redirects to its service-closure notice. No full PDF or source page image was downloaded or claimed inspected. The existing bibliographic key and fields suffice for this repair; root may separately refresh the access URL if desired. No canonical bibliography addition or edit is required here.

## Actual correction

The active result now uses:

    \begin{hbtheorem}{thm:p03-acfp-uncountable-categorical}{cited=Steinitz1910}{Uncountable categoricity of algebraically closed fields}

The intended stable label is reused from the inactive former result. A search before insertion found that inactive declaration as its only declaration in handbook LaTeX; the current reader route does not include that old file.

The result states the ambient Choice hypothesis, characteristic p=0 or prime, model existence and uniqueness for every uncountable cardinal, and failure of aleph-zero categoricity. This matches the active definition of categoricity at lines 4–8, which requires existence as well as uniqueness.

The following source explanation retains the original mathematical content: uncountable cardinality determines absolute transcendence degree; bases of equal cardinality give isomorphic rational-function fields and then isomorphic algebraic closures; countable algebraically closed fields can have different finite or countably infinite transcendence degrees. It defines the prime-field and transcendence-basis terminology, gives the source locators, and identifies the cited field-theoretic dependencies explicitly.

Existence at cardinal kappa is accounted for by the source's rational-function construction on kappa independent indeterminates followed by an algebraic closure. Steinitz's cardinality calculation gives exactly kappa. At the countable cardinal, closures of the prime field and its one-indeterminate rational-function field have degrees zero and one. Countability follows from the countable polynomial set and finitely many roots per nonzero polynomial; algebraically closed fields are infinite. These fields therefore witness the stated failure of countable categoricity.

The modern phrase “ACF_p is kappa-categorical” is presented as the model-theoretic application of Steinitz's field classification and cardinal calculation, not as his literal 1910 terminology. The short explanation is expressly not presented as a complete proof of the classification or algebraic-closure theorems.

## Navigation and source-preservation details

The hbtheorem form has the requested cited status and stable label, while avoiding a change in the count of ordinary theorem environments. This matters because the P3 driver attaches the Ryll–Nardzewski and Morley anchors to the third and fourth ordinary theorem openings in this restoration scope. Their theorem text and those hook positions remain unchanged. Both the prior source example and the new hbtheorem use the shared hbitem counter, so the replacement remains one numbered result at this position. These conclusions come from reading the actual driver and handbook.sty:461–495, not from a build.

No helper hook, driver, bibliography, registry or validator was edited. P4a's checker-support work remains separate; this author did not change the restoration provenance record.

## Remaining obligations and continuation

The requested active result/status/attribution repair has been authored and read back. Independent review of this frozen result and its cited-source mapping remains pending; no acceptance is claimed here. Its scope is S-011, not complete reconstruction of Steinitz's entire paper or complete ACF model theory. The source classification and closure results remain cited dependencies, and publication/provenance evidence is handled separately by root.
