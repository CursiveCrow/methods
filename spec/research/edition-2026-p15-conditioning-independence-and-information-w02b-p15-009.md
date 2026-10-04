# P15 159.8, 159.9 (packet w02b-p15-009): provenance note

4 October 2026. Wave w02b, block 1. Accounting-mode packet; sections 159.8
and 159.9 are carried by existing treatments in P16
(`measurable-causal-graphs`) and P15 (`uniform-integrability-and-conditional-limits`).

## Gap closed in this block

ED26-P16-CH-measurable-causal-graphs-C012 (item 3 of
`thm:p16-measurable-mediation-fields`). The mediator-adjustment paragraph of
`annex:p16.measurable-mediation-fields` in
`handbook/annex/p16/measurable-causal-graphs.tex` (editable host) previously
said "by the preceding restoration argument" and "The third separation
survives restoration". It is replaced (now lines 392--567) by a full argument:

1. Facts about `T=(A,C,W_1,W_2)`: no mediator descendant in `T`; `T` misses
   `M` and `Y`; `Y` is not an ancestor of a mediator.
2. Restored graph `H_2 = G_{\underline M} + E_2`, where `E_2` is the set of
   mediator edges whose head is in `K = an_G(M)`; proof that `K = an_H(M)`.
3. Auxiliary models (natural equations on `K`, mediator inputs fed `m`
   elsewhere); joint measurability.
4. `M` and `T` unchanged pointwise (ancestral set `N_0`).
5. No new ancestral vertex: `an_{H_2}({Y} u M u T) = an_H({Y} u M u T)`.
6. Every new moral edge lies in `{v} u pa_{H_2}(v)` for a restored head `v`;
   `v` and every parent of `v` outside `T` lie in `D_M`; hence `D_Y` is still
   a component after deleting `T`, and `Y` is d-separated from `M` given `T`
   in `H_2` (via `thm:p16-moral-separation-bridge`).
7. Auxiliary response equals `Y_m` pointwise (topological induction on `D_Y`
   against the model intervened at `M=m`).
8. Response-component lemma (`thm:p16-measurable-response-component`) gives
   `Y_m = F_2(m,T,R_2)` for all `m`, `R_2 indep M | T`.
9. Worked boundary: `A->M_1->Z->M_2->Y`, `M_1->Y`, `A->Y`; adding `Z->Y`
   both breaks the auxiliary response and violates the third separation.

The argument is the handbook's own; it uses only handbook definitions
(`def:p16-active-path`, `def:p16-ancestral-moral-graph`,
`def:p16-measurable-scm`) and results. No new source locator, citation key
or global symbol was introduced. Local proof symbols (`H_2`, `E_2`, `K`,
`N_0`, `\mathcal A`, `\mathcal M`, `\mathcal M_2`, `D_Y`, `D_M`) are scoped
to the proof.

## Checks run

- `tools/find_fused_spaces.py` on the edited host: no hits.
- `tools/check.py --tree handbook` filtered to the edited host: no findings.
- Scratch compile (pdflatex, TeX Live 2025) of the P16 bodies
  finite-causal-models, graphical-separation-adjustment, causal-mediation,
  measurable-causal-graphs and the measurable-causal-graphs annex: exit 0;
  no overfull box in lines 392--567; the cross-references used in the new
  text resolve.
- `tools/waves.py unit-compile` on the packet fails because the packet's owned
  body/annex files do not exist; this block wrote no content for them (all
  work was in the editable host), and creating a stub chapter would duplicate
  existing treatment.

## Continuation

- C012 restoration argument: written in the host annex, lines 392--567.
- The parallel restoration in the cross-world paragraph (lines 336--356) uses
  the graph with exposure inputs cut; it was not part of this gap and is
  unchanged.
- Readonly units (uniform-integrability: w02b-p15-013; finite-causal-models:
  w02b-p15-070) were not touched.
- Open: the scoped unit-compile requires the owned body/annex files; the lead
  decides whether this packet needs owned files when its work sits in hosts.
