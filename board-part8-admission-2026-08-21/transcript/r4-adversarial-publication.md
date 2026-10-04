REJECT

# Part VIII R4 adversarial-publication review

## Decision and evidence boundary

The current Part VIII source/content snapshot has one blocking mathematical-publication defect: its displayed definition of **weak centering** admits an empty-union sphere system under which the advertised conditional-modus-ponens principle is invalid. The centered Lewis VC presentation, the four repairs named in the R4 brief, and the remaining reader/apparatus graph are source-clean on static inspection.

This was a read-only review of the complete route rooted at `handbook/parts/p08.tex` and `handbook/annex/p08.tex`, including recursively included source restorations and supplements, every referenced calculus sheet, the generated Part VIII audit, the named-theorem and symbol retrieval surfaces, bibliography keys, labels, references, source roles, and the P8 register deliverables. I did not run a TeX/PDF build, tests, or a visual/human inspection. Consequently, the clean dispositions below are source/content findings, not claims about pagination, line breaks, PDF destinations, makeindex order, or rendered link behavior.

## Blocking finding

### R4-AP-F1 — blocker — weak centering is missing its nonempty-sphere existence conjunct

**Locations.**

- `handbook/parts/p08/conditionals-deontic-free.tex:268-277` requires each `\mathcal S_w` to be a nonempty family of subsets, linearly nested and closed under the displayed unions/intersections. It does **not** require any member of that family to be nonempty. Indeed, closure under the union of the empty subfamily puts `\varnothing` in every `\mathcal S_w`.
- `handbook/parts/p08/conditionals-deontic-free.tex:279-286` makes `A\Box\!\!\to B` true whenever `[A]\cap U_w=\varnothing`, where `U_w=\bigcup\mathcal S_w`.
- `handbook/parts/p08/conditionals-deontic-free.tex:289-293` defines weak centering only by
  `\forall w\,\forall S\in\mathcal S_w(S\ne\varnothing\to w\in S)`.
- `handbook/parts/p08/conditionals-deontic-free.tex:296-298` identifies that condition with Lewis's `\mathsf{VW}` sphere class.
- `handbook/parts/p08/conditionals-deontic-free.tex:400-423`, specifically the `\mathsf{VW}` row at lines 410-411, says weakly centered spheres validate conditional MP and place the actual world among the closest antecedent worlds.
- `handbook/registry/calculi/hilbert-counterfactual-vc.tex:10` likewise assigns `(A>B)\to(A\to B)` the semantic condition “weak centering.”

**Concrete failure path.** Let `W={w}`, make `A` true and `B` false at `w`, and set `\mathcal S_w={\varnothing}`. This is a nonempty, linearly nested family. It satisfies the stated union closure; the stated intersection requirement has a false `\bigcap\mathcal T\ne\varnothing` antecedent; and the printed weak-centering formula is vacuously true. But `U_w=\varnothing`, so the first disjunct of the displayed counterfactual truth clause makes `A\Box\!\!\to B` true. Since `A\to B` is false at `w`, conditional MP fails in a model that the handbook currently calls weakly centered. The `\mathsf{VW}` comparison row and the sheet's semantic annotation therefore do not follow from the printed definition.

This is not a merely hypothetical convention dispute. Lewis's primary definition imposes both membership of the actual world in every nonempty sphere and existence of at least one nonempty sphere; see *Counterfactuals*, §1.7, p. 29: <https://fitelson.org/piksi/piksi_18/lewis_counterfactuals.pdf>.

**Exact correction.** Replace the weak-centering condition at lines 289-293 by

```tex
\forall w\in W\;
\left[
  \bigl(\exists S\in\mathcal S_w\;S\ne\varnothing\bigr)
  \land
  \forall S\in\mathcal S_w\,(S\ne\varnothing\to w\in S)
\right].
```

Equivalently, add `w\in U_w` to the existing universal condition. The existing centering clause at lines 294-295 still implies the corrected weak-centering condition because `{w}\in\mathcal S_w` supplies a nonempty sphere. Thus this correction does not disturb the centered, limit-free VC completeness statement at `handbook/parts/p08/conditionals-deontic-free.tex:356-364`; it repairs the weaker `\mathsf{VW}` boundary and the conditional-MP annotation.

**Disposition:** `still-open-source`. This blocks Part VIII source/content admission independently of every later build, visual, provenance, human, and user gate.

## R4-named repair verification

### Symbol registry: source-fixed and routed once

- The full-book route includes `handbook/parts/p01.tex` once at `handbook/main.tex:24`; `handbook/parts/p01.tex:36` contains the sole live `\input{parts/p01/symbol-registry}`. The Part VIII source map links readers back to that registry at `handbook/parts/p08/source-map.tex:88-92`, and the master retrieval section routes the symbol tables/index at `handbook/parts/p14/master-tables.tex:219-241`.
- `handbook/registry/symbols.csv` has 633 registration rows. `handbook/generated/symbols-tables.tex` has 633 distinct entry destinations, and `handbook/generated/symbol-index.tex` has 633 distinct links. The destination and link sets agree exactly; there is no duplicate symbol-registry route.
- A noncomment scan of `handbook/parts/p01/symbol-registry.tex`, the two generated symbol surfaces, and their live P8 navigation prose found no apparatus row ID (`A-###`), source unit ID (`N-*`), disposition ID (`D-P*`), workflow/finalizer language, or reader-visible OPEN/stub/owed notice.

These checks establish 633 source destinations and matching retrieval links. Rendered destination placement and clickable-PDF behavior remain build/visual checks.

### N-b-031: source-fixed

`handbook/parts/p08/intuitionistic-supplement.tex:496-517` now defines the complete lattice of intermediate logics ordered by inclusion, identifies arbitrary meets as intersections and joins as the least intermediate-logic closure, and identifies the empty meet/join as CPC/IPC. Lines 509-513 explain why the complete lattice is required and distinguish it from the later display. The KC/LC development follows at lines 519-560, while the comparison table at lines 563-583 and figure caption at lines 599-602 explicitly identify the four-node IPC–KC–LC–CPC chain as a **local subdiagram**, not the whole lattice. The registered N-b-031 obligation at `spec/registers/new-content.csv:103` is therefore met without naming the local chain as the complete structure. The five-part technical-name gate is satisfied at the point of introduction: necessity, definition, standing, nonredundancy, and subsequent use are all explicit.

### Lewis triviality: source-fixed as citation-only

`handbook/parts/p08/conditionals-deontic-free.tex:471-483` now carries `cited=Lewis1976`, states the source result and its essential assumptions, and does not present an editorial finite partition argument as a proof of the general theorem. That standing agrees with the cited-status convention in `handbook/CONVENTIONS.md:60-72`. There is no local proof-completion claim or annex reciprocity debt.

### A-091 quantified free-logic surfaces: source-fixed

`handbook/parts/p08/conditionals-deontic-free.tex:7-27` fixes the negative free-logic semantics; lines 46-73 distinguish negative, positive, and neutral variants; lines 75-85 type the three semantic consequence relations; and the rule table at lines 87-114 gives universal-instantiation and existential-generalization surfaces for **all three** variants with the required `E!` guards. The public symbol registry supplies the eliminable meaning of `E!(t)` at `handbook/registry/symbols.csv:218` and registers the three typed consequence relations at line 586. Thus the A-091 entry at `spec/registers/apparatus.csv:92` no longer relies on an untyped or private existence predicate, nor does it extrapolate one variant's calculus to the other two.

### P8 ASP row: correctly absent

The live nonmonotonic comparison table at `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:220-240` has rows for preferential, ranked, Reiter default, circumscription, autoepistemic, and AGM presentations, but no undefined P8 ASP/stable-model row. Its caption at lines 236-239 expressly routes stable-model/ASP treatment to Part IX, where the definition is live at `handbook/parts/p09/logic-in-computer-science.tex:379-396`. This is a transparent later-part route, not a false claim that P8 itself supplies an ASP definition.

## Comprehensive preservation review by charter lot

### Lot 1 — intuitionistic and intermediate logics

Checked clean apart from unrun render gates. The exact inherited route and the editorial intuitionistic supplement retain distinct source standing. IPC/KC/LC/CPC notation is defined before the local hierarchy display; negative translations distinguish their hypotheses and targets; algebraic/topological semantics, realizability/existence-property boundaries, and IQC surfaces have live definitions and routes. The complete-lattice/local-chain repair described above removes the former scope ambiguity. No reader construction debt or unsupported claim was found in the live lot.

### Lot 2 — modal logics

Checked clean apart from unrun render gates. Normal and non-normal systems, correspondence statements, filtration and bisimulation, quantified modal logic, Barcan/domain-variation assumptions, and incompleteness boundaries have explicit system/semantic scope. Every calculus identifier used by the reviewed modal cards resolves through the live rule-sheet catalog. The modal proof appendix at `handbook/annex/p08/modal-completeness-supplement.tex:4-65` is reciprocally linked with its body status; no body theorem was silently promoted from cited/sketched to proved.

### Lot 3 — temporal, epistemic, conditional, deontic, and free logics

**Not clean solely because of R4-AP-F1.** All other reviewed seams are source-fixed: Büchi acceptance is defined before its automaton display (`handbook/parts/p08/temporal-epistemic-supplement.tex:353-401`); group operators use the public nonempty-finite-group convention (`handbook/parts/p08/group-operator-convention.tex:1-8`) and the epistemic table/figure text at `handbook/parts/p08/temporal-epistemic-supplement.tex:517-578,679-683` respects it; the CA-based Lewis VC sheet is the live identity (`handbook/registry/calculi/hilbert-counterfactual-vc.tex:1-11`); the centered, limit-free VC completeness statement is source-specific (`handbook/parts/p08/conditionals-deontic-free.tex:356-397`); dyadic, free, and conditional comparisons expose their domains and consequence notions. Lewis triviality and A-091 have the corrected standings described above. The only remaining contradiction is the weaker VW/weak-centering boundary.

### Lot 4 — many-valued, relevance/linear/Lambek, paraconsistent, nonmonotonic, and apparatus

Checked clean apart from unrun render gates. The many-valued annex at `handbook/annex/p08/many-valued-supplement.tex:18-133` reciprocates the body's proof standings. Designated-value, t-norm, relevance, linear, affine, and Lambek surfaces keep their systems and structural assumptions separate. The affine sheet at `handbook/registry/calculi/affine-ill.tex:1-5` agrees with the worked treatment, comparison table, and figure at `handbook/parts/p08/relevance-linear-supplement.tex:528-677` and makes no adequacy/cut-elimination overclaim. The da Costa C1 treatment at `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:72-132` resolves to `handbook/registry/calculi/hilbert-da-costa-c1.tex:1-18`; the KLM and AGM presentations at lines 149-218 and 264-356 state their distinct assumptions and operations. Further reading is live at `handbook/parts/p08/further-reading.tex:7-44`.

## Static route, identity, and retrieval results

- `handbook/parts/p08.tex:1-74` routes forty exact-source wrappers, the editorial supplements, the source/navigation material, and `handbook/generated/audit-p08.tex`; `handbook/annex/p08.tex:1-10` routes the source-sketch map and the two proof supplements. Recursive inspection reached 93 P8 body input files and four P8 annex input files. Historical combined presentations are not on this route, so they do not create duplicate reader identities.
- The forty exact intervals named in `handbook/parts/p08/source-map.tex:1-37` are contiguous source lines 12970-14094 (1,125 lines). Static byte comparison of each routed restoration against `source/formal-logic-reference.tex` under the displayed SHA-256 found no mismatch, gap, overlap, duplicate, or reorder. The editorial/source distinction is stated explicitly at `handbook/parts/p08/source-map.tex:39-85`.
- The P8 surface contains 274 static label references; every referenced label has a live source definition. Its 48 referenced calculus-sheet labels resolve to 45 live sheet files (some files intentionally expose more than one sheet identity). No missing or duplicate live target was found.
- The body, annex, and referenced sheets cite 135 distinct bibliography keys; all 135 occur in the live bibliography database.
- Fifty-two editorial theorem-class items have syntactically valid `proved`, `sketched`, or `cited` standing. Sixteen body items pointing to `proved=annex:*` or `sketched=annex:*` have exactly the sixteen reciprocal annex destinations; no orphaned proof-status pointer was found.
- `handbook/generated/audit-p08.tex` has 168 distinct live links and a single P8 audit caption/label. `handbook/generated/named-theorem-index.tex` has 426 displayed rows and 474 total live links; its only raw `@` is the mathematical title `K(@)`, not an unprocessed makeindex sort separator. The 633-row symbol-table/index correspondence is recorded above.
- The registered P8 table/figure inventory has one live labeled reader artifact per routed obligation; captions do not print internal apparatus IDs. The system cards, rule sheets, source map, audit table, named index, symbol index, and further-reading routes are mutually navigable at source level.
- A noncomment scan of the complete live P8 body/annex/generated route and its P1/P14 retrieval surfaces found no reader-visible uppercase OPEN/TODO/FIXME, stub/unadmitted/owed notice, workflow/finalizer language, pointer-only substitute, or internal `A-###`, `N-*`, or `D-P*` identifier.

## Final ruling

The specifically requested symbol-registry, N-b-031, Lewis-triviality, A-091, and ASP repairs are accepted as source-fixed, and the previously accepted Part VIII repairs remain coherent. Nevertheless, R4-AP-F1 is a direct countermodel to a current reader-visible semantic definition and to the corresponding `\mathsf{VW}`/conditional-MP claims. Part VIII therefore remains **REJECTED for source/content admission** until the weak-centering existence conjunct is inserted and the affected definition, table row, and rule-sheet annotation are rechecked. Final provenance, build/reference, visual, human, and user acceptance gates remain separate and unrun.
