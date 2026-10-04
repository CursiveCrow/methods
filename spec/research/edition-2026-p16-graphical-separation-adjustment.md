# P16 graphical separation and adjustment: author return

Date: 8 September 2026 UTC. Author: the agent reassigned from
`/root/constructible_foundation_publication_review` to manuscript writing.
Block began at 08:47:32 UTC; deadline 09:32:32 UTC. The previous review
assignment was cancelled and its existing report was left untouched.
This is completed authoring of the bounded component, with author checks;
consolidated independent reviews remain deferred until all changes are made.

## Written extent

All three output paths were checked unused before creation. Only the two
new LaTeX files and this note were authored; shared integration remains with
the lead. The body and every complete annex proof were read back from disk.

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p16/graphical-separation-adjustment.tex` | 315 lines; six definitions, seven results, one method | `6F26941A0B9AF00CE5101771113732958EE1926CDFF2D3BAEC1E440ECED62E2F` |
| `handbook/annex/p16/graphical-separation-adjustment.tex` | 439 lines; seven full proofs | `9B97C4938F35761CA336AE783562B6E02C7F194DCE44056880A33380FAE9FC2A` |

The seven reciprocal suffixes below have body prefix `thm:p16-` and annex
prefix `annex:p16.`.

| Suffix | Complete content supplied |
| --- | --- |
| `active-walk-reduction` | Shortest active walk; every repeated-vertex splice case; a forbidden new collider would make the repeated vertex an ancestor of conditioning. |
| `moral-separation-bridge` | Both directions between source path blocking and moral separation after ancestral restriction; expanded co-parent edges; elimination of bad collider occurrences by directed endpoint rerouting; termination and active-path reduction. |
| `ancestral-marginal` | Reverse-topological elimination with normalized total kernels, including empty marginals and zero probabilities. |
| `finite-global-markov` | Partition of the ancestral moral graph, family cliques, two nonnegative factor products, all marginal sums, and positive-stratum normalization. |
| `finite-back-door-adjustment` | Explicit auxiliary model deleting outgoing treatment edges, pointwise comparison with original and intervened solutions, graph separation, conditional independence, consistency, overlap, stratum identity, adjustment, and identification from partial observation. |
| `adjustment-numerical-example` | All eight endogenous masses; observed contrast 1/2; intervention values 3/8 and 5/8 and contrast 1/4; every adjustment ratio and graph condition. |
| `collider-numerical-example` | Full four-assignment law; collider and descendant conditioning; 1/3 versus 4/9 dependence; unchanged independent causes under equation replacement; same-graph inactive-parent counterexample to automatic dependence. |

## Actual prerequisites and primary reading

The governing contract and conventions had been read completely in this
context. The author read the complete current 418-line causal body and
377-line annex, plus its complete 199-line source intake. Their hashes are:

- Body: `331568E5FF2329B4498CA98DCA7DC8BE79D4EB77B8A2152DAB33F05F05BABA42`.
- Annex: `1393539308C2668996B75AED30D47025F337944E0FC0270E863A153A00794096`.
- `spec/research/edition-2026-p16-finite-causal-models.md`:
  `A31DCBDA331F66558C1A3E5A8462801A45213C30E8E09AA556B919390225E6C0`.

The held primary is Pearl, *Causal inference in statistics: An overview*,
Statistics Surveys 3 (2009), 96-146, author-hosted R-350:
[UCLA PDF](https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf).
Local file: `source/references/pearl-causal-overview-2009/pearl-2009-ucla-r350.pdf`;
SHA256 `1A5ECB7CB7C55A9B4F2C09AAC091BC01A3EABFC94FC55EE692EFBC013A8B7581`.
The existing capture identity was rechecked by hash; this is no new acquisition.

The author read extracted text for printed pp. 105-111 and 113-118, and
the complete page images for pp. 106-108, 110-111, and 113-115. Definition 1
on p. 106 supplies the collider/descendant blocking criterion. Sections
3.2.1-3.2.3 supply equation replacement and the factorization context.
Definition 3 on p. 114 and Eq. (25) on p. 115 supply the sufficient back-door
criterion and adjustment expression. Figure 4 and its surrounding text were
read but are not reproduced. No general correlated-error separation result,
do-calculus completeness result, or sample estimation guarantee is imported.

The research and PDF skills guided primary-source reading. Source-page PNGs
for pp. 114-115 were generated in the old task's `tmp/pdfs/p16-graphical-source`
directory; all other viewed images were existing source captures. No manuscript
PDF was built or rendered. The moral-graph proof, explicit auxiliary model,
positivity qualification, and numerical models are independently supplied
handbook derivations. The existing `Pearl2009CausalOverview` key is used;
no bibliography addition is needed.

## Integration and notation intake

Input the new body after `parts/p16/finite-causal-models`, and its annex
after `annex/p16/finite-causal-models`. It is a section of that causal
chapter, expected scope P16.2. The old causal body's final paragraph must
point to these newly supplied finite separation/adjustment results while
retaining the distinct general, front-door, do-calculus, counterfactual,
cyclic-model and potential-outcome obligations. The lead owns that edit.

| New or extended glyph family | Local role |
| --- | --- |
| `\operatorname{an}_G(J)`, `A,B,C,H`, `i_0,\ldots,i_m`, `r,s,w` | Reflexive ancestry; endpoint, conditioning and ancestral vertex sets; path/walk positions and repeated vertex. Strict descendants retain the earlier meaning. |
| `A\mathrel{\perp_G}B\mid C`, `G_H^{\mathrm m}`, `G_H^{\mathrm m}\setminus C` | Graphical d-separation; induced-ancestral moral graph; vertex deletion, performed after moralization. |
| `V_A\mathrel{\perp\!\!\!\perp}V_B\mid V_C`, `p,p_H,p_C` | Conditional independence on every positive conditioning stratum; coordinate law and marginals, also defined for a generic factorizing mass. |
| `D,F,\phi(d,c),\psi(f,c),g(a,c),h(b,c),g_C(c),h_C(c)` | Reachability partition, nonnegative factor products, marginal sums and their positive normalizers in the global Markov proof. These products need not themselves be probability laws. |
| `t,B,C,O,X,Y,Z,x,y,z`, `Y^{t=x},Z^{t=x},Y^{X=x}` | One treatment vertex, response/adjustment/observed sets, their random variables or tuples and values; singleton indexed intervention abbreviations defined before use. |
| `G_{\underline t}`, `M_x^\dagger`, `W,R` | Outgoing-edge-deleted graph, auxiliary structural model and its solution, and treatment nondescendants excluding the treatment. This graph differs from the incoming-edge-deleted intervention graph. |
| `U_Z,U_X,U_Y,\alpha(a),(z,a,u)`, `K,D,U_K` | Explicit independent disturbances and outcome coordinates in the confounded example; binary collider, copied descendant and extra fair disturbance in the counterexample. Numerical examples use locally named vertices. |

## Checks and next requirement

The unchanged existing `tools/check.py` editorial scanner, SHA256
`05F22DEE54E3F177EAD79DFAE16D88787E513A58441F443278679F8BC7443914`,
reports no findings on the two new files: 23 labels, seven statuses,
seven annex items and seven reciprocal pairs. All nine external references
resolve in the actual prior causal body; no label collides with it. The
existing bibliography has the sole cited key. This checks source structure,
not independent correctness or publication acceptance. No tests were written.

The assigned finite separation and sufficient single-treatment back-door
component is fully written. Next, supply a separate complete finite
front-door identification treatment with its own graph, observation and
positivity hypotheses, full derivation and numerical example; general
do-calculus and identification completeness remain further requirements.
Do not begin consolidated reviews until the full manuscript change set is
finished, as the user instructed.
