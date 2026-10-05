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

## Gap closed in block 2 (4 October 2026): C007 semigraphoid variant

ED26-P16-CH-measurable-causal-graphs-C007. The assessment found only the
probabilistic (G)/(L)/(O)/(R) equivalence on the route. Lauritzen's
Theorem 2.44 states (G)<=>(L)<=>(O) for an arbitrary semigraphoid
independence model and proves it from (S1)-(S4); Corollary 2.45 adds order
invariance.

Source opened in this session: `source/references/lauritzen-graphical-lectures-2019/lauritzen-graphical-models-third-edition.pdf`
(held; key `Lauritzen2019GraphicalLectures2020`), extracted with pdftotext.
Locators seen: TOC "2.5.1 Independence models 51", "2.6.2 Markov properties
on directed acyclic graphs 64"; semigraphoid axioms (S1)-(S4) and Example
2.24 on p.52 (Example 2.24 continues to p.53); (O) on p.64, (L)/(G) and
Theorem 2.44 statement on p.65; proof pp.65-66; Corollary 2.45 p.66;
Theorem 2.49 and "follows from Theorem 2.44" on p.67. Notation kept:
`\perp_\sigma`, D, V, pa, nd, pr, de, `A \perp_D B | S`.

Written (editable hosts):
- Body `handbook/parts/p16/measurable-causal-graphs.tex` lines 122-261: new
  subsection with def:p15-w02b-p15-009-semigraphoid,
  def:p15-w02b-p15-009-directed-markov,
  thm:p15-w02b-p15-009-semigraphoid-trivial (lemma),
  thm:p15-w02b-p15-009-semigraphoid-markov (Theorem 2.44 variant),
  thm:p15-w02b-p15-009-order-invariance (Corollary 2.45),
  connecting paragraph to thm:p16-measurable-global-markov,
  def:p15-w02b-p15-009-chain-derivation (worked example),
  def:p15-w02b-p15-009-empty-vertex-set (boundary warning).
- Annex `handbook/annex/p16/measurable-causal-graphs.tex` lines 244-491:
  annex:p15-w02b-p15-009-sg-trivial, annex:p15-w02b-p15-009-sg-markov,
  annex:p15-w02b-p15-009-sg-order, all proofs from (S1)-(S4) only.

Handbook additions relative to the source proof (recorded in the annex's
closing paragraph): (L)=>(G) first enlarges the query to a partition of
the ancestral set (the source's "pa(v*) in A u S or B u S" step otherwise
misses parents outside the three query sets); statements with an empty side
are derived from (O) by contraction, which needs V nonempty; for V empty the
empty relation is a semigraphoid with (L),(O) vacuous and (G) failing, so the
theorem carries V nonempty and the warning records the exact V-empty
condition. Not stated as a source error; the source "does not single out
this case".

The earlier C012 restoration argument has shifted to annex lines 641-816.

Symbols: `handbook/registry/symbols-intake-p15-conditioning-independence-and-information-w02b-p15-009.csv`
(`\perp_\sigma`, `\perp_D`, pa/de/nd/pr, proof-local `\mathsf m`). Overlap:
registry row 1448 already types `\operatorname{pr},\operatorname{nd}` for the
measurable kernel construction with the same meaning.

Checks: find_fused_spaces no hits; check.py --tree filtered to the hosts no
findings; scratch pdflatex+biber of the four P16 body/annex pairs exit 0, no
overfull box in the new ranges, new labels resolve. `waves.py unit-compile`
fails only because the packet's owned body/annex files do not exist (all
work sits in editable hosts).

## Continuation

- C007 semigraphoid variant: written (body 122-261, annex 244-491).
- C012 restoration argument: written earlier, now annex 641-816.
- Readonly units untouched: uniform-integrability (w02b-p15-013);
  finite-causal-models (w02b-p15-070), including its C012/C016 disputes
  named in this block's task, which belong to that owner packet.
- Open: unit-compile needs owned body/annex files; lead decides.

## Block 3 (4 October 2026): C014 examples proof

ED26-P16-CH-measurable-causal-graphs-C014. The assessment found three gaps
in `annex:p16.measurable-graph-examples`: the third model named the
disturbance E instead of the observed response Y and never stated that
P(A=1/2)=0 forces Y=E a.s.; existence of all fixed structural interventions
for the singular chain was unwritten; and the corollary's mean premises
were not checked before the theta values. The proof (editable host annex,
now lines 933-1118) is rewritten as eight paragraphs:

1. Chain kernels (point-mass kernel measurability) and global Markov via
   `thm:p16-measurable-global-markov`.
2. Non-domination (unchanged argument).
3. Chain as a measurable SCM (one-point disturbances for Z, Y); explicit
   solution for every I in the eight subsets and t in R^I; joint
   measurability; law equals the delta-replaced kernel construction;
   do(Z=z) has law Unif x delta_z x delta_z though P(Z=z)=0.
4. Mediation example hypotheses: SCM, four separations of
   `thm:p16-mediation-four-set-criterion` checked edge by edge, atoms 1/2,
   (MS) from positive densities, delta_{a+m+am} as a version of the
   observed response kernel.
5. Mean premises: 0<=Y<3, absolute response integral <=3; then the four
   theta values via the mean form of the corollary, cross-checked
   structurally; PNDE 3/2, TNIE 1/3, TE 11/6.
6-8. Null-exposure pair: both SCMs written; P(A=1/2)=0 gives Y=E a.s. in
   the first model, so the observed law of (A,M,Y) is common; natural
   direct effects 1/2 and 0; atom premise fails.

Handbook's own argument; no source locator, citation key or global symbol
added. Body statement unchanged.

Checks: find_fused_spaces no hits; check.py --tree filtered to the host no
findings; scratch pdflatex of the four P16 pairs exit 0, no overfull box in
934-1118. unit-compile still fails only on the absent owned files.

## Continuation

- C014: examples proof written (annex 933-1118).
- C007 semigraphoid variant: written (body 122-261, annex 244-491).
- C012 restoration argument: written (annex 641-816).
- Readonly units untouched: uniform-integrability (w02b-p15-013);
  finite-causal-models (w02b-p15-070).
- Open: unit-compile needs owned body/annex files; lead decides.
