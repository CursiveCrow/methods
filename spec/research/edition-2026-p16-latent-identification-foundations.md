# P16 latent identification foundations: author return

Date: 8 September 2026 UTC. Block began 11:07:58 UTC; deadline
11:52:58 UTC. This is authoring under the user's all-changes-before-
consolidated-reviews instruction. The three manuscript output paths
were verified unused. No independent review was started.

## Complete authored component

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p16/latent-identification-foundations.tex` | 327 lines; five definitions and nine results | `927CF7629C68CF415B04E9054E9ED83F4EB06F4F67018809D24005573BC5C72E` |
| `handbook/annex/p16/latent-identification-foundations.tex` | 384 lines; nine complete proofs | `DDED1E9C327BD81BCA26481515E62E9ABCC6D1519A309DC9BA07C19B314ABE7D` |

All new LaTeX, including the complete proofs and author corrections,
was read back from disk. Only these files, this note, and the authorized
new primary capture were written in the manuscript directory. Root
retains shared routes, notation, bibliography and prior boundaries.

The nine reciprocal suffixes have body prefix `thm:p16-` and annex prefix
`annex:p16.`:

| Suffix | Complete content |
| --- | --- |
| `latent-kernel-semantics` | Explicit-root full-DAG bridge, independent input product space, exact indicator-sum Q kernel, normalization at every outside parameter, outside-parent dependence, and restriction after intervention with child sets intersected with H. |
| `latent-district-partition` | Bidirected connectivity equivalence relation, unique maximal partition, constructive spanning-tree equivalence, and assignment of every relevant latent input to one district. |
| `latent-ancestral-reduction` | Reverse-topological summation at each fixed latent tuple, exact retained indicators, and independence of newly displayed outside parameters. |
| `latent-target-reduction` | Ancestor reduction after a fixed intervention, harmless extra actions on remaining nonancestors, and restriction to original response ancestors with the correct marginal observed law. |
| `latent-district-decomposition` | Partition of the actual independent latent inputs, factorization of their finite sums, and identification of each resulting factor as its intervention kernel Q[D]. |
| `latent-prefix-chain` | Prefix ancestry, equality of prefix marginals and Q-prefix kernels, normalized positive conditional ratios, monotonic prefix masses and telescoping, including zero final numerators. |
| `latent-district-recovery` | Explicit partial district factors g(D,j), changes in only the current district, positive cancellation, grouped telescoping through the district's last index, and the resulting identification domain. |
| `latent-foundation-calculation` | All eight observed masses in the three-variable example, both district kernels, every prefix ratio, normalization, induced child-set restriction and ancestral singleton sums. |
| `latent-foundation-limits` | A zero-support response ambiguity, a strictly positive bow-graph ambiguity for a proper connected subset, and a calculated shared-input versus independent-pair-input comparison. |

## Exact primary acquisition and reading

Acquired the published AAAI proceedings version, not a substituted
conditional-identification paper or the differently hosted R-327 report:

- Ilya Shpitser and Judea Pearl, *Identification of Joint Interventional
  Distributions in Recursive Semi-Markovian Causal Models*, AAAI 2006,
  printed pp. 1219-1226.
- Verified publisher landing page: [AAAI article](https://aaai.org/papers/01219-aaai06-191-identification-of-joint-interventional-distributions-in-recursive-semi-markovian-causal-models/).
- Actual download: [AAAI proceedings PDF](https://cdn.aaai.org/AAAI/2006/AAAI06-191.pdf).
- Capture: `source/references/shpitser-pearl-joint-identification-2006/aaai06-191.pdf`.
- Eight pages, 492,898 bytes; SHA256
  `33B1FAAB38522381DE79C8A92CBDCD03F25336BD43BA917CB1677634062929BC`.
- The actual title, authors, conference metadata, page numbers and
  readable mathematical body were verified. PDF creation/modification
  metadata dates are May 2006; they are not used as a conference date.

All eight pages were read completely as extracted text and full page images,
including model definitions on p. 1220, Definition 3 and Q notation on
p. 1221, Figure 3 on p. 1223, all foundation Lemmas 4-8 and their proofs
on p. 1224, and the later algorithm/hedge/completeness statements through
p. 1226. Source-page images are in the old task's
`tmp/pdfs/p16-latent-id-source` directory. The research and PDF skills
guided acquisition and reading. No manuscript PDF was built or rendered.

The source supplies these foundation statements and re-proves them using
do-calculus. The new chapter supplies complete finite latent-sum proofs.
It does not claim a complete transcription of every materially distinct
source proof or of either identification algorithm. Tian's 2002 thesis
is cited by the source but was not acquired or claimed read in this block;
the needed foundation proofs in the acquired Shpitser/Pearl paper were read.

## Model and support decisions

The model definition on p. 1220 specifies finite independent latent inputs
and adds a bidirected edge when a latent input is shared. It does not impose
a two-child bound there. The chapter retains each full latent child set,
including roots shared by three or more observed variables. It proves only
the explicit-root expansion and the intervention restriction used in its
kernel identities. It assumes neither an arbitrary latent-projection theorem
nor a distribution-preserving conversion to independent pairwise roots.

Declared-input compatibility allows inactive arguments, matching the existing
SCM convention and the constant-response witness retained in the source's
Theorem 2. It is not a faithfulness or minimal dependence-graph assumption.
If extra latent-incidence, cardinality or distribution restrictions are given,
they remain additional model information rather than being discarded into G.

The source's p. 1220 sentence associates unsupported interventions with an
undefined intervention distribution. The active chapter instead retains the
proved equation-replacement definition: Q kernels exist at every fixed
parameter, while recovery by observed conditional ratios has its own support
requirements. The zero-support countermodel proves this distinction directly.
The district recovery identity is proved at `rho_(m(D)-1)(v) > 0`.
Full positive kernel support is sufficient for recovery at all assignments,
but is not necessary: the worked example has zero joint masses and positive
required prefixes throughout. No unspecified value is assigned to 0/0.

## Bibliography intake

The following key is new; root owns its canonical merge.

```bibtex
@inproceedings{ShpitserPearl2006JointIdentification,
  author = {Shpitser, Ilya and Pearl, Judea},
  title = {Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models},
  booktitle = {Proceedings of the Twenty-First National Conference on Artificial Intelligence},
  year = {2006},
  pages = {1219--1226},
  publisher = {AAAI Press},
  url = {https://cdn.aaai.org/AAAI/2006/AAAI06-191.pdf},
  urldate = {2026-09-08}
}
```

## Integration and notation intake

Input the two files after their corresponding finite-counterfactual
predecessors, within the finite causal chapter, expected scope P16.2.
The expanded-DAG proof uses the actual existing finite-SCM definition,
topological-order theorem and solution theorem. Their current body hash
is `489A65462DC4A3ADD88BE885F10142FC5E3F620044B9AE0E36B7DD464463E3E4`;
the matching causal annex hash is
`1393539308C2668996B75AED30D47025F337944E0FC0270E863A153A00794096`.

| Glyph family | Typed role |
| --- | --- |
| `N,V_i,S_i,\operatorname{pa}(i)`, `\Lambda,U_\alpha,\mathcal U_\alpha,r_\alpha,C_\alpha,\Lambda_i` | Observed indices/variables/value sets/parent inputs; independent latent indices, values, laws and actual child-incidence sets. |
| `G`, `i\to j`, `i\leftrightarrow j`, `G[H]`, `\mathcal D_H`, `\Lambda_D` | Declared observed mixed graph, two edge types, induced graph, maximal districts and their unique latent-input groups. |
| `Q[H](v)`, `Q[H](v_H;v_{N\setminus H})`, `p,p_H,P_x(y)` | Intervention kernels with output/parameter distinction, ordinary observed joint/marginal laws, and source effect notation. |
| `A,A_0,H,X,Y`, `\operatorname{an}_{G[H]}(A)` | Observed subsets and directed ancestry, including the target set; bidirected edges do not supply directed ancestors. |
| `h_j,H_j,k,\rho_j,\theta_j,m(D)`, `\delta_i(u;v),g_{D,j}(v)` | Topological indices/prefixes, prefix masses, positive conditional ratios, last district position, retained equation indicators and partial district factors. |
| `A,B,C,U,E_A,E_B,\alpha,\beta`, `R_{AB},R_{AC},R_{BC}` | Locally named observed/latent variables and explicit binary masses in the worked examples; pair-specific roots in the comparison construction. |

## Checks and exact next writing

The existing editorial scanner reports no findings, 25 labels, nine
statuses, nine annex items and nine reciprocal pairs. All three external
prerequisite references resolve in the current causal body, with no label
collisions against the existing P16 authoring sections. The new bibliography
key remains an integration intake until merged. No new tests, independent
reviews, admission records or manuscript renders were created.

Next write the algorithm in Figure 3, its recursive parameter/support
invariants and termination measure, then the complete hedge construction
and nonidentification/completeness argument from Theorems 4-6 and their
corollaries. The source's C-forest roots are observed vertices with no
observed children; that role must be distinguished from the parentless
latent roots defined here. Binary hedge witnesses also require explicit
handling of fixed observed domains, including singleton-domain trivialities.
Showing that every algorithm step is expressible by the three do-calculus
rules is an additional argument for do-calculus completeness. None of those
remaining results is claimed completed by these foundation identities.
