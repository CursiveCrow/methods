# Round 1 — source-fidelity/evidence opening position

- seat: source-fidelity
- round: 1, blind opening
- scope: complete live reader graph rooted at `handbook/parts/p03.tex` and `handbook/annex/p03.tex`; I did not read another Part III seat transcript
- mandate: exact inherited source/artifact/order correspondence; exact source roles and claim scope; variant and proof-status separation; no duplicate or altered inherited unit; every reader-visible OPEN/owed statement; all four charter lots

### F1 [blocker] [open] Routed editorial units print OPEN, unadmitted, and internal register status

- author: source-fidelity r1
- location: `handbook/parts/p03/maps-elementarity-supplement.tex:2-14`; `handbook/parts/p03/types-ultraproducts-supplement.tex:2-8`; `handbook/annex/p03/types-ultraproducts-supplement.tex:2-4`; `handbook/parts/p03/qe-categoricity-games-supplement.tex:3-8`; `handbook/annex/p03/qe-categoricity-games-supplement.tex:3-6`; charter invariant 4 and construction-status criterion.
- claim: Five reader-routed surfaces state that material is OPEN, remains unadmitted, or does not close named internal obligations. They expose `A-162`, `D-P4-003`, `D-P4-004`, and `R-030` as workflow state rather than mathematical source/proof standing. Part III therefore fails its no-reader-facing-construction-debt invariant by its own printed text.
- evidence: The maps lookup calls itself evidence “toward the OPEN apparatus item A-162” and repeats the identifier in its caption. The types body says two `D-P4-*` rows remain OPEN and unadmitted, and its annex repeats one of those IDs. The QE body prints a bold OPEN notice and says the additions remain unadmitted; the QE annex prints `OPEN` and `R-030`. These are active TeX lines, unlike the driver comments at `handbook/parts/p03.tex:10-16,32-34`.
- correction: Review and disposition each retained editorial unit. For each accepted unit, replace its workflow notice with ordinary reader-facing attribution that states its controlling source or local-proof standing and its nonreplacement relation to the inherited chapter; remove A-/D-/R- identifiers from prose and captions unless the published book supplies a deliberate public lookup. Unroute every rejected body/annex unit together. Do not remove these notices before F3-F6 are resolved, and do not use their removal to promote register, build, visual, human, or user gates.
- status: open.

### F2 [blocker] [open] All Part III provenance and review controls remain unadmitted

- author: source-fidelity r1
- location: `spec/provenance/SRC-06049-06069.json:40-76,92-95`; `spec/provenance/SRC-06942-07134.json:49-86,102-105`; `spec/provenance/SRC-07469-07493.json:40-75,91-94`; `spec/provenance/reviewed-handbook-unit-records.json:2-5`; `spec/provenance/reviewed-register-obligation-records.json:2-6`; `spec/handbook-construction-snapshot.csv`; charter invariants 4-5.
- claim: Exact byte restoration is established, but no current control record admits any inherited or editorial Part III unit or any Part III register obligation. The stored construction snapshot describes older bytes.
- evidence: A read-only enumeration gives `part3_records=21 open_destinations=21 independent_source_pending=21 all_completeness_pending=21`. The representative beginning, middle, and end records cited above all retain `handbook_destination.status=open/missing`, every completeness dimension pending, and independent-source/build/visual fields pending. Both reviewed-record arrays are empty. `python tools/check_handbook_construction_snapshot.py` currently reports `FAIL (handbook source tree drifted (added=35, changed=80))`; several live Part III editorial file sizes/hashes differ from the stored snapshot, while their inventory units remain `open/unmapped` and semantically pending.
- correction: After the substantive Part III bytes freeze, regenerate the construction snapshot and unit inventory. Add one hash-bound reviewed-unit record for every accepted reachable inherited/editorial unit and a reviewed-obligation record for every obligation actually discharged, citing this board's exact scope. Update the 21 provenance destinations and applicable source/completeness fields individually. Preserve build, visual, human, and user acceptance as separate unpromoted gates.
- status: open.

### F3 [must-fix] [open] The R-030 annex item is an orphaned second proof of an inherited theorem already proved inline

- author: source-fidelity r1
- location: `handbook/restoration/inherited-07295-07468.tex:108-131`; `handbook/annex/p03.tex:3-4`; `handbook/annex/p03/qe-categoricity-games-supplement.tex:3-17`; `spec/registers/defects.csv:31`; `spec/register-obligation-closure.csv:558`; charter source-correspondence and proof-status criteria.
- claim: The exact inherited theorem `thm:dlo-countable-categorical` explicitly has `Status: complete proof` and supplies its back-and-forth proof inline. The routed editorial annex then creates `annex:p3.qe.5` targeting that same theorem and presents a second proof, but the body theorem has no `proved=annex:p3.qe.5` status or editorial forward note. The annex calls itself support for a “separately attributed historical addition,” although its live target is the inherited theorem. That leaves the proof's source standing and body/annex reciprocity false.
- evidence: The inherited proof already handles the finite cut and the density/no-endpoint back-and-forth construction at `inherited-07295-07468.tex:115-131`. The annex adds the four cut forms at lines 11-15, which is useful R-030 detail, but the only live body identity it names is the already complete inherited theorem. The current graph otherwise has one genuine editorial proved pair, `thm:p03-compactness-ultraproduct -> annex:p3.types.8`; `annex:p3.qe.5` is the unmatched second annex target.
- correction: Preserve the inherited theorem and inline proof unchanged. If the four-case R-030 detail is retained, add a separately attributed body note immediately after the exact QE/categoricity source block that explicitly links `annex:p3.qe.5` as supplemental proof detail and says it does not alter the inherited complete-proof status; revise the annex note to name that standing. Otherwise unroute and remove the redundant annex item. Bind R-030 only after one of those two reader routes is selected and reviewed.
- status: open.

### F4 [must-fix] [open] The bibliography key used as the original source of Los's theorem names a different 1955 paper

- author: source-fidelity r1
- location: `handbook/restoration/inherited-06942-07134.tex:78-98`; `handbook/bib/handbook.bib:393-400`; charter source-role and attribution criteria.
- claim: The inherited theorem says “The original source is `Los1955`,” but the live key resolves to *On the Extending of Models I*, Fundamenta Mathematicae 42 (1955), 38-54. The first explicit ultraproduct construction and fundamental theorem are instead in Łoś's *Quelques remarques, théorèmes et problèmes sur les classes définissables d'algèbres*, pp. 98-113 of *Mathematical Interpretation of Formal Systems* (1955).
- evidence: The publisher record for the current key confirms that it is the distinct paper [*On the Extending of Models (I)*, FM 42, 38-54](https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/42/1/94182/on-the-extending-of-models-i). The Polish Academy's history of its foundations group attributes the ultraproduct construction and fundamental theorem to [*Quelques remarques...*](https://www.impan.pl/images/schinzel.pdf), and the primary publisher page identifies that chapter as [volume 16 (1955), pp. 98-113](https://www.sciencedirect.com/science/article/pii/S0049237X09703064/pdf). The two works have different titles, containers, pages, and roles; sharing author and year does not make the current citation source-faithful.
- correction: Rebind `Los1955`—the only live reader uses are ultraproduct-source claims—to an `@incollection` record for *Quelques remarques, théorèmes et problèmes sur les classes définissables d'algèbres*, in *Mathematical Interpretation of Formal Systems*, Studies in Logic and the Foundations of Mathematics 16, pp. 98-113, North-Holland, Amsterdam, 1955, DOI `10.1016/S0049-237X(09)70306-4`. If *On the Extending of Models I* is needed elsewhere, retain it under a distinct `Los1955Extending` key. This corrects the citation without changing the exact inherited artifact.
- status: open.

### F5 [must-fix] [open] Vaught's two-cardinal theorem cites his 1961 countable-model paper instead of the 1965 theorem source

- author: source-fidelity r1
- location: `handbook/parts/p03/qe-categoricity-games-supplement.tex:123-138`; `handbook/bib/handbook.bib:698-705`; `spec/registers/new-content.csv:6`; charter source-role and theorem-attribution criteria.
- claim: The two-cardinal statement is attributed by `cited=Vaught1961`, whose record is *Denumerable Models of Complete Theories*. That work is the source of the never-two/countable-model discussion, not the cited two-cardinal theorem. The registered source row itself calls for Vaught 1965.
- evidence: The theorem's displayed `(\kappa,\lambda)`-to-`(\aleph_1,\aleph_0)` scope is the result associated with Vaught's *A Löwenheim-Skolem Theorem for Cardinals Far Apart*. The authoritative bibliographic record places it in *The Theory of Models*, Proceedings of the 1963 Berkeley symposium, edited by Addison, Henkin, and Tarski, North-Holland, 1965, pp. 390-401: [Cambridge/JSL record](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/r-l-vaught-a-lowenheimskolem-theorem-for-cardinals-far-apart-the-theory-of-models-proceedings-of-the-1963-international-symposium-at-berkeley-edited-by-j-w-addison-leon-henkin-and-alfred-tarski-studies-in-logic-and-the-foundations-of-mathematics-northholland-publishing-company-amsterdam1965-pp-390401/B772C31774DF696C8B1A9C7E280AE402), [publisher contents](https://www.sciencedirect.com/book/9780720422337/the-theory-of-models). The current 1961 record's title, container, and pages identify another work.
- correction: Add `Vaught1965TwoCardinal` as an `@incollection` with the authoritative 1965 title, editors, container, pages 390-401, publisher, and location; cite that key at `qe-categoricity-games-supplement.tex:123`. Retain `Vaught1961` for the never-two theorem and Vaught-conjecture history required by its own register row.
- status: open.

### F6 [blocker] [open] The declared Part III new-content scope remains materially incomplete

- author: source-fidelity r1
- location: `spec/registers/new-content.csv:2-14,62`; `spec/register-obligation-closure.csv:143-155,203`; `handbook/parts/p03/classification-theory.tex:3-248`; `handbook/parts/p03/preservation-abstract-logic.tex:15-39,164-202`; `handbook/parts/p03/finite-model-theory.tex:16-131`; charter purpose, lot 4, and zero-unresolved-content requirement.
- claim: The live chapters partially cover the Part III shopping list, but several `target_part=P3` obligations remain absent or below their registered treatment ceiling. Every corresponding closure row is still OPEN with no evidence. The current reader surface therefore is not complete for its declared Part III scope even if the material it does contain is correct.
- evidence: Concrete gaps are:
  1. `N-a-001/N-a-002`: the Ryll--Nardzewski statement is inherited, but the required random-graph omega-categoricity example and the Fraisse hereditary/JEP/AP construction, existence/uniqueness theorem, limit, and extension axioms are absent.
  2. `N-a-004`: Vaught's never-two theorem and the current status of Vaught's conjecture are absent.
  3. `N-a-006`: the inherited Morley categoricity statement remains, but Morley rank, total transcendence, the proof outline, and Baldwin--Lachlan refinement are absent.
  4. `N-a-007/N-a-008`: the chapter defines stability/forking and states EM existence, but omits the stability spectrum, superstable and omega-stable distinctions, the registered nonforking-extension survey, and EM applications to nonisomorphic models.
  5. `N-a-009`: o-minimality is defined and RCF is named, but the registered monotonicity and cell-decomposition statements are absent.
  6. `N-a-012`: model companions, Robinson's model-completeness test, and existentially closed worked examples are absent.
  7. `N-a-013`: only Robinson joint consistency is stated; Beth definability, the model-theoretic proofs, and the Craig/Beth equivalence are absent from this target.
  8. `N-a-061`: Lindstrom's theorem is citation-only at `preservation-abstract-logic.tex:184-202`, although the row explicitly requires the full proof.
- correction: Supply each missing artifact at its registered treatment ceiling, with definition-before-use, exact hypotheses, citations, and honest local/cited proof standing, or formally supersede/rescope the corresponding P3 register row before claiming Part III completeness. Do not close a whole row from a neighboring definition or a theorem statement that omits the row's proof/application requirement. Bind each final unit to its own reviewed-obligation record under F2.
- status: open.

## Coverage note

### Cross-cutting route and source checks

- checked clean: The two roots reach 52 files through 50 input edges: two roots, 21 wrappers, 21 exact artifacts, six editorial body files, and two editorial annex files. `handbook/parts/p03.tex:2-35` routes 21 distinct restoration IDs exactly once and in increasing order; their contiguous intervals cover source lines 6049-7493 without a gap or overlap.
- checked clean: `python tools/check_inherited_restoration.py` passed every Part III record's frozen authority digest, interval digest, artifact digest, and ordered content-token comparison. Across the whole corpus it reported 282 source/static passes and explicitly left independent-source, build, visual, and human review pending.
- checked clean: The reachable graph has no duplicate body/section/annex ID and no unresolved scoped Part III reference under the custom theorem/annex environments. All 37 citation and `cited=` authority keys exist in `handbook/bib/handbook.bib`. F3 identifies the one proof-reciprocity exception rather than treating it as clean.
- checked clean subject to filed findings: The Keisler--Shelah statement matches Shelah's 1971 theorem ([authoritative publication record](https://cris.huji.ac.il/en/publications/every-two-elementarily-equivalent-models-have-isomorphic-ultrapow/)); Kozen's Boolean-algebra class and subclass scope match the [IBM primary abstract](https://research.ibm.com/publications/complexity-of-boolean-algebras); Grigor'ev's parameterized ACF bound matches the [MathNet primary abstract](https://www.mathnet.ru/eng/im1566); and the Fagin, preservation, finite-model, and classification citations resolve to sources of the stated variants. F4-F5 record the two source-role failures found.
- not checked: final TeX compilation, fresh bibliography/index/reference resolution, rendered-page inspection, layout/overflow, human review, or user acceptance. This review ran no build. I did not inspect every page of every closed-access monograph; local key existence is not a substitute for those independent source gates.

### Lot 1 — maps, substructures, elementarity, symbol supplement

- checked clean: all eight exact source intervals from `SRC-06049-06069` through `SRC-06494-06509`; term/map preservation, substructure and image constructions, elementary maps, Tarski--Vaught, diagrams, elementary chains, exercises; exact byte/order correspondence; table terms against the live symbol registry.
- findings: F1 (printed A-162 workflow state), F2 (unadmitted controls), F6 (cross-lot P3 completeness).
- not checked: build/visual/human/user gates.

### Lot 2 — types, ultrafilters, ultraproducts, Los, saturation, proof supplement

- checked clean: all ten exact intervals from `SRC-06510-06629` through `SRC-07135-07149`; type-space topology, realization/saturation convention, homogeneity proof, omitting types, ultrafilter existence calibration, ultraproduct construction, Los induction and diagonal embedding; editorial Keisler--Shelah statement and compactness-via-ultraproduct proof.
- findings: F1, F2, F4.
- not checked: build/visual/human/user gates and closed-book page-by-page locators.

### Lot 3 — quantifier elimination, categoricity, back-and-forth, games, retained additions

- checked clean: all three exact intervals from `SRC-07150-07294` through `SRC-07469-07493`; DLO/ACF QE scope, completeness distinctions, back-and-forth, DLO categoricity, Ryll--Nardzewski and Morley statement boundaries; editorial EF definitions and finite inexpressibility variants; high-risk catalog claims checked against their cited primary scopes.
- findings: F1, F2, F3, F5.
- not checked: build/visual/human/user gates.

### Lot 4 — classification, finite model theory, preservation/abstract logic, routes and debt

- checked clean within present content: atomic/prime definitions; order indiscernibles; stability/dividing/forking/simple/NIP/o-minimal variant separation; zero--one, Fagin, Trakhtenbrot, and finite/unrestricted boundaries; Robinson, Los--Tarski, Chang--Los--Suszko, Lyndon, and Lindstrom statement hypotheses. No present claim was flattened across its named variant.
- findings: F2 and F6; F1 also covers the construction-status notices that block whole-Part admission.
- not checked: absent registered artifacts cannot be marked clean; build/visual/human/user gates remain separate.
