# PA Sigma-one consumer correction

Date: 2026-09-07. Bounded NOW-03d implementation in the two assigned consumer files. The theorem label thm:p05-sigma-one-completeness and its reciprocal annex label annex:p5.sigma.1 are retained.

## Exact scope and result

The internal clause now states PA proves sigma implies Prv^19_PA of the original sentence code, where Prf^19_PA is literally Gamma_d19 with output one. The external clause remains: every true closed Sigma-one sentence in its original syntax is provable in Q.

Annex display (4) now uses the actual fixed bounded descriptions d_theta^+ and d_theta^-, their Gamma output graphs, and the finite selected numeral-substitution descriptions s_theta^+ and s_theta^-. Graph existence and uniqueness come from thm:p05-pa-pr-graphs; verification comes from thm:p05-fixed-bounded-builders and annex:p5.fixed-bounded-builders.

E_varphi is expressly an alias for the existing Ev_varphi: the same fixed marked normal form, bounded-leaf priority, auxiliary choices, associations and comparison binders. Its actual weak evidence guards are retained. Original bounded formulas therefore use the evidence leaf for their fixed normal forms. The proof includes both marked quantifiers, strict empty ranges, weak zero bounds, and dependent witnesses.

Display (9) now follows from the actual signed original-syntax description widehat d_varphi^+, its unique Gamma output, its original root, and the checked packing invariant. It cites thm:p05-original-sigma-evidence and annex:p5.original-sigma-evidence and explicitly deduces the closed-sentence schema by eliminating evidence and proof witnesses. No equivalence with an arbitrary earlier PA representative is asserted.

The external Q proof retains term evaluation and the two bounded-instance clauses. It now gives a separate strict-range enumeration for the original abbreviation u < v := exists z (u + Sz = v), alongside the existing weak-order enumeration. The fixed logical normal-form equivalence and the full evidence-to-original-formula deduction in Q preserve the original-syntax conclusion.

## Snapshot

| File | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| handbook/parts/p05/models-and-interpretability-supplement.tex | 6FF8A78906F572422862078DD5E75E07F6924BAAA16E73E37ADCD8F21D20E6C1 | 49F73D85C2ECF81812D194B9A079955AD8AE186934302581E21EA240BE415A41 |
| handbook/annex/p05/depth-completion-supplement.tex | C04CCF07077B183DC4BC8AB622CC49653CA6B927C40A81AE074D57A407808FF0 | 7BEA46720C677FF6384C3D512D064CD195FEA9B9646B24BF7F200FFC61A3B55A |

The selected positive-introspection dependencies were read and their supplied hashes verified:

- handbook/parts/p05/pa-positive-introspection.tex: 7310A4F7967AD376E54F799324ADDC214535520ACA5AD8174F2D73AA8F9B821B.
- handbook/annex/p05/pa-positive-introspection.tex: 46CCC2144A1599DD6C5118EFCC8CA3BFB7899B8234CEF37E28547D7F47DEB9D0.

The parent retains the exact before backups in tmp/edition-2026-bounded-kamp4-probability-decision/consumer-before/.

## Handoff

The two consumer files were read back and hashed. No remaining mathematical obstruction was identified in this bounded correction. Fresh affected reviews belong to the parent integration step. No tests, build, rendering, source acquisition, commit, or admission was performed.
