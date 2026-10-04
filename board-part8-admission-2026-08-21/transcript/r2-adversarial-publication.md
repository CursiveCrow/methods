REJECT

# Part VIII R2 adversarial-publication admission review

## Scope and evidentiary boundary

This is a fresh review of the current live reader graph rooted at
`handbook/parts/p08.tex` and `handbook/annex/p08.tex`. I followed every routed
exact-source wrapper and editorial supplement, the reciprocal annex material,
the calculus sheets used by Part VIII cards, the central live rule-sheet
catalog, `generated/audit-p08.tex`, the named-theorem index, the symbol
registry/index, citations, cross-references, and the Part-VIII register
deliverables. I did not read another board transcript or conclusion. I made no
manuscript, specification, tool, test, or generated-source edit, and I ran no
test suite or TeX/PDF build.

The rejection is source/content based. It does not infer any rendered failure
from static source, and it does not decide the later provenance, build, visual,
human, or user gates.

## Source/content blockers

### F1 — Critical — the printed Lewis-VC completeness theorem is attached to a non-equivalent Nute calculus

**Status:** still open; admission blocker.

**Evidence.**

- `handbook/registry/calculi/hilbert-counterfactual-vc.tex:1-9` calls the sheet
  Lewis's `VC`/`C1` and gives CK plus ID, MOD, CSO, CV, conditional MP, and CS.
  This is the familiar Nute six-schema presentation.
- `handbook/parts/p08/conditionals-deontic-free.tex:276-283` nevertheless says
  that this sheet is sound and complete for Lewis's centered sphere semantics.
  The card repeats that adequacy at `:303-317`.
- The unsupported identity is promoted into reader retrieval surfaces at
  `handbook/generated/audit-p08.tex:108` and
  `handbook/generated/named-theorem-index.tex:346`.
- The governing must-row, `spec/registers/new-content.csv:88`, specifically
  requires source-exact completeness treatment for C1/VC; merely giving a
  popular neighboring axiom list does not meet it.

There is a concrete countercheck against the asserted identity. The published
analysis [Wen, *On Axiomatization of Lewis' Conditional Logics*
(2019)](https://arxiv.org/abs/1910.06202) proves that the Nute package is not
equivalent to either of Lewis's original VC axiomatizations: in particular,
Lewis VC derives CA while the Nute package does not. The current sheet is the
package identified there—it contains MOD and not CA—so the body cannot use it
as an exact complete calculus for Lewis's centered sphere logic.

**Reader failure path.** A reader follows the named-theorem index to
`thm:p08-vc-completeness`, follows the theorem to the registered sheet, and is
licensed to treat derivability on that sheet as exactly centered-sphere VC
validity. That license is false; it loses at least the Lewis-valid CA principle.

**Exact correction.** Replace the sheet by one of Lewis's original VC
axiomatizations or a proved equivalent corrected presentation (for example,
the amended Nute-style package with CA in place of the offending MOD schema),
and cite the equivalence/completeness source. Alternatively, if the present
sheet is intentionally retained, rename it as the Nute presentation and
withdraw the Lewis-VC completeness theorem/card claim. Because the frozen
register requires VC completeness, the former course is the admitting repair.
Regenerate the Part-VIII audit table and named-theorem index after fixing the
source; do not hand-edit those generated files.

### F2 — Major — the sphere model class used by the VC theorem is underdefined

**Status:** still open; admission blocker independent of F1.

**Evidence.**

- `handbook/parts/p08/conditionals-deontic-free.tex:212-231` defines a nested
  sphere family and the limit-free truth clause, but says only that centering
  and strong centering are “further separate conditions.” Neither condition is
  stated as a formula on `\mathcal S_w`.
- The completeness theorem then quantifies over “centered sphere semantics” at
  `:276-283`; the card says “centered” at `:303-310` and “strong centering” at
  `:313-314`.
- The comparison table distinguishes no centering, weak centering, and strong
  centering at `:326-338`, while the sheet annotates conditional MP as weak
  centering and CS as strong centering at
  `handbook/registry/calculi/hilbert-counterfactual-vc.tex:8-9`.

**Reader failure path.** Even after choosing the right calculus, a reader
cannot reconstruct the theorem's frame class or verify the MP/CS
correspondences: “centered” has three incompatible-looking uses and no
elimination clause. The exact frame hypothesis demanded by
`board-part8-admission-2026-08-21/charter.md:11-14` is therefore missing.

**Exact correction.** At the Lewis sphere definition, give exact quantified
conditions for weak centering and strong centering on every `\mathcal S_w`,
state unambiguously which condition defines the VC/C1 model class, and use the
same term in the theorem, card, table, and rule annotations. Preserve the
limit-free truth clause as a separate hypothesis rather than folding a least-
sphere assumption into either centering condition.

### F3 — Major — mandatory AGM apparatus omits the contraction postulates

**Status:** still open; admission blocker.

**Evidence.**

- The must-row `spec/registers/apparatus.csv:94` requires “Contraction and
  revision postulates with the Levi and Harper identities.”
- `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:183-215` defines
  revision and prints only the eight revision postulates.
- Contraction receives one informal sentence and the Levi/Harper identities at
  `:218-230`; no contraction-postulate family is displayed anywhere on the live
  Part-VIII route.

**Reader failure path.** A reader retrieving `tab:p08-agm-postulates` obtains a
table captioned as the AGM postulates but cannot reconstruct or compare AGM
contraction, including Recovery and the conjunctive contraction constraints.
Levi and Harper do not substitute for the required explicit postulates.

**Exact correction.** Extend the apparatus with a source-attributed, fully
typed contraction-postulate column/table for `K-A`, alongside the existing
revision postulates, and retain the Levi and Harper identities with their
direction and hypotheses explicit. Update the caption and surrounding prose so
the retrieval surface says exactly which two AGM operators it records.

### F4 — Major — the affine comparison denies the exact live sheet that the catalog renders

**Status:** still open; admission blocker.

**Evidence.**

- `handbook/parts/p08/relevance-linear-supplement.tex:528-539` says no exact
  cited affine calculus and matching registry sheet is supplied. Its family
  table consequently says “no sheet” at `:569-570`, and its consequence table
  again says no independent calculus at `:653-655`.
- The live registry contradicts that statement:
  `handbook/registry/calculi/affine-ill.tex:1-5` defines
  `sheet:affine-ill` as IMLL plus unrestricted antecedent weakening, with
  exchange built in and contraction absent.
- The central reader catalog renders that sheet at
  `handbook/parts/p14/rule-sheets.tex:85-93` and asserts at `:95-102` that every
  live calculus file is rendered exactly once.
- The Part-VIII source map itself calls the supplement an affine treatment at
  `handbook/parts/p08/source-map.tex:71-73`.
- The must-row `spec/registers/apparatus.csv:87` requires the affine system in
  the substructural family table and paired figure.

**Reader failure path.** A reader moves from the Part-VIII table to the
rule-sheet catalog and encounters two mutually exclusive publication claims:
the body says no exact affine sheet exists, while the catalog supplies one.
The body comparison also withholds the exact context profile already fixed by
that sheet.

**Exact correction.** Replace the stale no-sheet boundary with a hyperlink to
`sheet:affine-ill`; give its exact finite-multiset/single-succedent profile,
built-in exchange, unrestricted weakening, and absent contraction in both
comparison tables and the paired figure. If no affine adequacy theorem is being
claimed, say that explicitly; absence of an adequacy theorem is not absence of
the calculus. Preserve any Part-VII consumer of the shared sheet.

### F5 — Major — the registered paraconsistent-systems comparison is absent

**Status:** still open; admission blocker.

**Evidence.**

- `spec/registers/apparatus.csv:95` requires a Part-VIII comparison of LP and
  da Costa C-systems, including explosion failure and the distinct
  designated-value versus consistency-operator mechanisms. It is a `should`
  row, and this admission brief includes P8-targeted must/should deliverables.
- The routed paraconsistent chapter contains the general definition,
  dialetheism/inclosure discussion, and one LP countervaluation at
  `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:10-70`, then moves
  directly to nonmonotonic consequence at `:72`.
- The only nearby matrix comparison,
  `handbook/parts/p08/many-valued-supplement.tex:266-308`, covers K3, LP, weak
  Kleene, FDE, and finite Lukasiewicz systems; it contains no da Costa system
  or consistency operator. No `tab:p08-*` surface supplies A-094.

**Reader failure path.** The register promises a mechanism-level comparison,
but retrieval reaches only LP's designated-value semantics. A reader cannot
learn which da Costa system is meant, what its consistency operator denotes,
or how its restricted explosion differs from LP.

**Exact correction.** Supply the registered comparison only after selecting
and defining the exact cited da Costa system(s): fix language, consistency
operator, calculus/semantics, proof status, and explosion boundary, then
compare that mechanism with LP's designated values. Do not introduce an
undefined umbrella “C-system” name merely to populate a row; if the campaign
will not admit an exact presentation, the frozen obligation must be formally
redisposed rather than silently omitted.

## Additional publication defect

### F6 — Moderate — the epistemic-table caption contradicts its own row

**Status:** source correction required; not independently decisive once the
blockers above are repaired.

`handbook/parts/p08/temporal-epistemic-supplement.tex:660-663` actually prints
the common-knowledge fixed-point axiom and theorem-only induction rule. The
caption at `:671-673` says the table “points to, rather than redisplays” that
rule. A reader cannot tell whether this is a synopsis or a pure pointer. Change
the caption to say that the table displays the common-knowledge surface while
pointing to the sheet for the complete calculus; its statement about the PAL
reduction schemas may remain a pointer.

## Checked-clean source areas

- **Exact-source route and editorial standing.** The authority hash printed at
  `handbook/parts/p08/source-map.tex:5-12` matches the current frozen source.
  The forty intervals at `:25-40` are contiguous from 12970 through 14094, and
  `handbook/parts/p08.tex:2-71` routes them once in order while clearly
  interleaving editorial supplements. The alternate historical body files are
  not on the live route. The annex route at `handbook/annex/p08.tex:2-10` is
  reciprocal rather than a duplicate presentation.
- **Reader debt.** No noncomment live-route occurrence of a workflow row ID,
  finalizer instruction, reader-facing `OPEN`, `stub`, `owed`, or `unadmitted`
  debt was found. The phrase “P open” at
  `handbook/parts/p08/temporal-epistemic-supplement.tex:290` is the honest open
  complexity status of parity-game model checking, not campaign workflow.
- **Lot 1.** IPL/IQC definitions, negative translations, algebraic and
  topological semantics, constructive boundaries, KC/LC tables and figures,
  source-sketch reciprocity, and the NJ/LJ routes were checked without a
  further source/content blocker.
- **Lot 2.** The modal catalog, frame/domain clauses, correspondence and
  translation tables, bisimulation, filtration, neighborhood/general-frame
  boundaries, two-index semantics, QML/Barcan treatment, and the complete
  K/KT/S4/S5 canonical proof at
  `handbook/annex/p08/modal-completeness-supplement.tex:4-65` were checked
  without a further blocker.
- **Lot 3 apart from F1/F2/F6.** LTL, CTL, CTL*, modal mu, tense/fusion,
  S5/KD45 group semantics, distributed/common knowledge, PAL, hybrid logic,
  free logic, deontic logic, and indicative-conditionals boundaries have
  explicit system-specific syntax/semantics/status. One propositional
  conditional sheet is not being generalized to the whole family.
- **Lot 4 apart from F3-F5.** K3/LP/FDE, finite and infinite Lukasiewicz,
  Bochvar/Post, t-norm, supervaluation, relevance E/R/RM, IMLL, full CLL phase
  semantics, Lambek, System P/rational consequence, default logic,
  circumscription, and autoepistemic logic retain distinct calculi and honest
  proved/sketched/cited boundaries. Adaptive logic is expressly excluded by
  `spec/registers/new-content.csv:178`; its source pointer at
  `handbook/parts/p08/relevance-linear-supplement.tex:689-695` does not pretend
  to be a technical admission.
- **Calculus retrieval.** Every Part-VIII `entrycalculus` target inspected has
  a live registered destination. The central catalog currently lists all 71
  registry files exactly once, with no missing file or duplicate rendering.
  F4 is a semantic/catalog contradiction, not a missing physical sheet.
- **Generated retrieval.** `handbook/generated/audit-p08.tex` has one Part-VIII
  register caption/label and 164 linked entries. The current named-theorem
  index has 425 linked rows, including the newly routed Part-VIII results; the
  literal `@` in `K(@)` is display content, not a leaked makeindex sort key.
  The symbol registry and symbol index each contain the same 630 unique
  `entry:symbol-registry-*` destinations/links, including the Part-VIII
  conditional, QML, epistemic, many-valued, relevance, linear, Lambek, and
  nonmonotonic notation.
- **Citations and references.** Static inspection found no missing bibliography
  key in the live Part-VIII plus referenced rule-sheet route, and no concrete
  broken label among the body/annex/card/index references inspected. This is
  source evidence only; it is not a claim that a compiled link is clickable.
- **Other P8 apparatus.** A-076 through A-092 were located and checked apart
  from A-086 and the caption defect in A-080. A-113, A-159, A-165, A-186, and
  A-189 have current static reader surfaces. A-093 and A-094 remain the omitted
  apparatus blockers recorded above.

## Prioritized repair checklist

1. Replace or relabel the Nute VC sheet, restore an exact Lewis-VC-equivalent
   calculus, and correct the completeness/card/index claims (F1).
2. Define weak and strong centering formally and make the VC model-class term
   uniform across definition, theorem, card, table, and sheet (F2).
3. Complete the AGM table with contraction postulates and add the registered
   LP/da-Costa mechanism comparison with exact technical standing (F3, F5).
4. Reconcile the Part-VIII affine table/figure with the already-live
   `sheet:affine-ill`, without inventing an adequacy theorem (F4).
5. Correct the epistemic caption (F6).
6. Regenerate affected audit/index/symbol surfaces from their generators, then
   run the separately authorized static, bibliography, build, reference, and
   visual gates.

## Explicit non-build/non-visual boundary

Not checked here: TeX compilation, bibliography or index program execution,
destination resolution in the built PDF, page references, float placement,
table width, line breaking, overfull boxes, figure legibility, font/glyph
coverage, bookmarks, page count, or human visual acceptance. Those remain
later gates and cannot cure F1-F5 at source level.
