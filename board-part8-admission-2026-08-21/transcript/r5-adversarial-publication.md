ACCEPT

# Part VIII R5 adversarial-publication verdict

## Verdict and boundary

The current frozen Part VIII reader graph is source/content clean for the adversarial-publication mandate. The R4 weak-centering blocker is corrected, the orphaned ASP vocabulary is absent from the live Part VIII route, and the previously accepted repair and retrieval seams show no source regression.

This was a read-only source inspection of the graph rooted at `handbook/parts/p08.tex` and `handbook/annex/p08.tex`, its referenced sheets, and its public generated retrieval surfaces. I did not read another seat's transcript or conclusion, edit a manuscript/spec/tool/generated source, run tests, run a TeX/PDF build, or perform visual/human verification. Accordingly, `ACCEPT` is a source/content verdict only; final compilation, reference rendering, pagination, destination placement, visual, provenance, human, and user gates remain external.

## R4 blocker closure: weak centering now validates conditional MP

`handbook/parts/p08/conditionals-deontic-free.tex:268-286` retains the typed sphere family, `U_w=\bigcup\mathcal S_w`, and the limit-free variably strict truth clause. The corrected definition at lines 289-295 now requires, for every `w`, both

```tex
w\in U_w
```

and

```tex
\forall S\in\mathcal S_w\,(S\ne\varnothing\to w\in S).
```

This removes the former `\mathcal S_w={\varnothing}` countermodel. More directly, suppose `A` is true at `w` and `A\Box\!\!\to B` is true. Because `w\in U_w`, `[A]\cap U_w` is nonempty, so the vacuity disjunct at lines 281-284 is false. The second disjunct supplies a sphere `S` with `S\cap[A]\ne\varnothing` and `S\cap[A]\subseteq[B]`. That sphere is nonempty, so weak centering gives `w\in S`; with `w\in[A]`, it follows that `w\in[B]`. Hence `(A\Box\!\!\to B)\to(A\to B)` is valid on the printed weakly centered class.

The classification at `handbook/parts/p08/conditionals-deontic-free.tex:296-312` remains coherent: `{w}\in\mathcal S_w` still makes centering imply both corrected weak-centering conjuncts, while neither condition introduces the separate limit assumption. The `\mathsf{VW}` table row at lines 410-411 and the Conditional-MP annotation at `handbook/registry/calculi/hilbert-counterfactual-vc.tex:10` are therefore supported. The centered, limit-free VC result at `handbook/parts/p08/conditionals-deontic-free.tex:356-397` is unchanged.

**Disposition:** R4 weak-centering blocker `accept-fixed`.

## ASP/stable-model/reduct cleanup

A recursive expansion of the two live Part VIII roots reached 97 routed TeX files. After removing TeX comments, a case-insensitive source search over that exact route found zero occurrences of:

- the standalone abbreviation `ASP`;
- `stable-model` or `stable model`; or
- `reduct` or `reducts`.

The current nonmonotonic table at `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:220-240` ends with the AGM-revision row and makes only the claims supported by the definitions present in Part VIII. It contains no dangling ASP row, caption promise, stable-model semantics, or undefined reduct reference. This lexical result is deliberately scoped to the Part VIII reader graph; occurrences in the separately routed Part IX subject matter or nonprinting global control data are not Part VIII reader prose.

**Disposition:** orphaned Part VIII ASP vocabulary `accept-fixed`.

## Regression check of previously accepted publication repairs

### Source identity and route

- `handbook/parts/p08.tex:1-74` still routes exactly forty `restoration/scope-SRC-*` wrappers in source order, interleaves the attributed supplements once, and routes the generated Part VIII audit once.
- `handbook/parts/p08/source-map.tex:1-85` still identifies `source/formal-logic-reference.tex`, its SHA-256, the contiguous authority interval 12970-14094, all 1,125 exact lines, and the exact-source/editorial distinction.
- `handbook/annex/p08.tex:1-10` still routes only the reciprocal source-sketch map, many-valued proof supplement, and modal-completeness supplement. The historical combined presentations remain outside the live route.
- A noncomment scan of the 97 reachable Part VIII TeX files found no uppercase OPEN/TODO/FIXME, `\hbstub`, internal `A-###`, `N-*-###`, or `D-P*` identifier, workflow/finalizer language, or pointer-only substitute.

### Definitions, status, and system identity

- N-b-031 remains fixed at `handbook/parts/p08/intuitionistic-supplement.tex:496-517`: intermediate logics form the complete lattice under inclusion, with the displayed KC/LC chain explicitly identified as a local subdiagram at lines 509-513 and in the figure caption at lines 599-602.
- The Lewis triviality result remains honestly citation-only at `handbook/parts/p08/conditionals-deontic-free.tex:473-484`; it states its finite four-atom scope and expressly disclaims an internal proof.
- The A-091 surfaces remain complete at `handbook/parts/p08/conditionals-deontic-free.tex:7-27,46-118`: negative, positive, and neutral free-logical semantics are distinguished; the three consequence relations are typed; and universal instantiation plus existential generalization are printed with the `E!` guard for all three variants.
- The live Lewis VC sheet at `handbook/registry/calculi/hilbert-counterfactual-vc.tex:1-11` remains the CA-based corrected identity; it does not restore the rejected MOD presentation or make a limit-assumption claim.
- The exact dyadic best-world semantics and its nonvacuity convention remain at `handbook/parts/p08/conditionals-deontic-free.tex:173-214`.
- The Buechi automaton definition still fixes the run and recurrence acceptance condition before its figure at `handbook/parts/p08/temporal-epistemic-supplement.tex:353-401`; the group convention remains nonempty and finite at `handbook/parts/p08/group-operator-convention.tex:1-8`; and the epistemic caption at `handbook/parts/p08/temporal-epistemic-supplement.tex:679-683` continues to distinguish synopsis-level material from complete sheet-level rules.
- Da Costa's exact `\mathsf C_1` presentation still resolves from `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:72-132` to `handbook/registry/calculi/hilbert-da-costa-c1.tex:1-18`; the smooth/ranked KLM distinction remains explicit at `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:149-218`; and the AGM revision, contraction, Levi/Harper, and faithful-preorder surfaces remain distinct at lines 244-355.
- The affine body/table/figure at `handbook/parts/p08/relevance-linear-supplement.tex:528-677` still agrees with `handbook/registry/calculi/affine-ill.tex:1-5`: weakening is present, contraction absent, exchange built into finite-multiset contexts, and no affine adequacy or cut-elimination theorem is claimed.

### Reader retrieval apparatus

- `handbook/parts/p01.tex:36` remains the sole live input of `parts/p01/symbol-registry`. `handbook/registry/symbols.csv` has 633 rows; `handbook/generated/symbols-tables.tex` has 633 distinct public destinations; and `handbook/generated/symbol-index.tex` targets exactly the same 633 identifiers, with zero set difference and no internal apparatus IDs.
- `handbook/generated/audit-p08.tex` still exposes 168 reader links under the single Part VIII register route.
- `handbook/generated/named-theorem-index.tex` still contains 426 displayed hyperlinked rows. The corrected sort/display seam has not regressed.
- Public symbol, precedence, rule-sheet, named-theorem, further-reading, and source-map routes remain present through `handbook/parts/p08/source-map.tex:88-92`, `handbook/parts/p08/further-reading.tex:1-44`, and `handbook/parts/p14/master-tables.tex:212-241`.

## Final disposition

No source/content publication blocker remains in the current Part VIII route. The R4 mathematical defect is fixed rather than merely relabeled, the undefined ASP vocabulary is absent from the reader graph, and the accepted source/status/navigation repairs remain coherent. **ACCEPT.**
