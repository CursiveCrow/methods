# P16 finite counterfactuals and potential outcomes: author return

Date: 8 September 2026 UTC. Resumed author block began 10:38:11 UTC;
deadline 11:23:11 UTC. The earlier attempt stopped before manuscript
writing. The three owned output paths were verified unused. All work here
is authoring under the user's all-changes-before-consolidated-reviews
instruction; no independent review was started.

## Written component

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p16/finite-counterfactuals.tex` | 351 lines; five definitions and nine results | `8CA2E95DA56DD19E0D7E15A9A85C9027DB981E92219AE7F383066A1841E6A7EC` |
| `handbook/annex/p16/finite-counterfactuals.tex` | 428 lines; nine complete proofs | `42C22470336A2A2575526275DBCBA4E8D067929096725E93D8E399D51EF27DEB` |

Both actual LaTeX files were read back completely, with author corrections
incorporated. Only these two new files and this note were written in the
manuscript directory. Root retains all shared integration and prior-boundary
edits. No tests or manuscript builds/renders were created.

The nine reciprocal suffixes have body prefix `thm:p16-` and annex prefix
`annex:p16.`:

| Suffix | Complete proof content |
| --- | --- |
| `counterfactual-laws` | Effectiveness, factual consistency, composition at values attained in the same intervention world, overlapping-assignment override, compatible commutation, and nondescendant invariance. A three-node example disproves substitution of another world's value. |
| `counterfactual-calculation` | Normalized joint cross-world law; positive-evidence posterior pushforward; finite abduction/action/prediction procedure; grouping by the full disturbance tuple; counterexample to posterior disturbance independence. |
| `finite-twin-construction` | One shared latent root carrying the joint disturbance vector, explicit duplicated endogenous equations and graph, topological uniqueness, the full indicator-product mass formula, conditional evidence, and the failure of independently redrawing backgrounds. |
| `binary-po-bridge` | Pointwise binary consistency and intervention marginal identity; converse representation of any finite joint binary-treatment potential-outcome model by a shared-root acyclic structural model. |
| `back-door-exchangeability` | The already supplied auxiliary model gives potential-outcome exchangeability from the structural back-door condition before any positivity-dependent division. |
| `po-ate-identification` | Separate exchangeability for each potential outcome, explicit two-sided covariate-stratum overlap, distributional identification and the ATE weighted mean; counterexample to inferring joint exchangeability from the two separate assumptions. |
| `po-att-identification` | Only control-potential exchangeability, positive treated mass, control overlap on treated strata, and the exact treated-population weighting. |
| `cf-worked-calculation` | Full observed table, potential responses, every mean and weighting, positive-evidence posterior, equation replacement and predicted response. |
| `po-coupling-nonidentification` | Two fully specified randomized selector models; equality for every single-world intervention subset on (A,Y); unequal joint couplings, benefit probabilities and responder-specific counterfactuals; sharp binary benefit bounds with an attaining model for every permitted coupling. |

The worked model gives ATE 3/2, ATT 7/4 and unadjusted mean contrast 9/4.
Its evidence-conditioned control response probability is 1, compared with
population intervention probability 1/2 and observed control conditional 1/4.
The two randomized models have the same uniform observed (A,Y) law and
the same intervention laws, but benefit probabilities 0 and 1/2. This is
not a claim that all counterfactual quantities are nonidentifiable; the
sharp interval explicitly covers cases where its endpoints coincide.

## Exact source reading and scope

The research and PDF skills guided reading of the held primary files:

- `source/references/pearl-causal-overview-2009/pearl-2009-ucla-r350.pdf`,
  SHA256 `1A5ECB7CB7C55A9B4F2C09AAC091BC01A3EABFC94FC55EE692EFBC013A8B7581`.
  Complete extracted pages 119-122 and 127-132 were read. Complete images
  of pp. 120-121 and 127-129 were read for the used mathematical passages.
  Definition 4 and Eq. (27) give the same-unit submodel semantics;
  p. 121 describes joint counterfactuals and positive-evidence conditioning;
  Eqs. (36)-(38) give consistency, effectiveness and composition;
  Eqs. (39)-(40) give conditional exchangeability and its adjustment derivation.
- `source/references/pearl-causal-diagrams-1995/pearl-1995-ucla-r218-b.pdf`,
  SHA256 `0A9DD3218E541ACBF26AEFF5865E3C70CB662CD7DE50E1234D016F1AF5DA8927`.
  The author's rejoinder pp. 703-704 was read completely as text and images.
  Its Eq. (2) gives the structural counterfactual interpretation and Eq. (3)
  gives consistency. It permits broader systems subject to unique solutions;
  this component retains the established finite acyclic setting.

The held passages support the conditional counterfactual quantity and the
potential-outcome identities. They are not represented as containing the
explicit finite three-stage algorithm, twin construction, ATT proof or
coupling examples written here; those are handbook deductions. No general
completeness claim for the source's counterfactual axioms, cyclic-model
semantics, or identification algorithm is imported. The existing bibliography
keys `Pearl2009CausalOverview` and `Pearl1995CausalDiagrams` are used; no
new bibliography entry or acquisition was needed. Source-page images are
in the old task's `tmp/pdfs/p16-counterfactual-source` directory.

## Dependencies and integration

The actual finite structural-model, intervention and back-door construction
proofs were used. Their current file hashes were checked:

- Causal body: `489A65462DC4A3ADD88BE885F10142FC5E3F620044B9AE0E36B7DD464463E3E4`.
- Causal annex: `1393539308C2668996B75AED30D47025F337944E0FC0270E863A153A00794096`.
- Separation body: `F3C2AF46EFA37BE811B4468427D656E629570DF2C1618EEA4654734FFA6ABAF8`.
- Separation annex: `9B97C4938F35761CA336AE783562B6E02C7F194DCE44056880A33380FAE9FC2A`.

Input both new files after their matching do-calculus predecessors, within
the finite causal-model chapter, expected scope P16.2. Root should update
earlier forward boundaries to point here for this finite counterfactual and
binary potential-outcome component, while retaining the separate broader
counterfactual identification and algorithm-completeness obligations.

| Glyph family | Explicit local role |
| --- | --- |
| `V_J[I=x]`, `V[I=x;J=y]`, `I,J,x,y`, `\mathcal W,I_k,x^k,J_k,Q` | Same-unit single/sequential interventions, overriding assignments, finite world labels, and their jointly evaluated query tuple. |
| `E,D,q_E,U,\mathcal U,r_E,\widehat Q` | Positive evidence, a query-value event, posterior outcome weights, joint disturbance vector and its value set, grouped posterior and the background-indexed query. |
| `R,R_i,T_i^k,r(u),v^k` | Shared tuple-valued latent root, its components, duplicated endogenous world coordinates, joint background mass and complete copied assignments. |
| `A,L,Y,Y(0),Y(1),Y_a`, `t,r,C`, `\Delta,\operatorname{ATE},\operatorname{ATT}` | Binary treatment, baseline covariates, real response, two same-unit potential outcomes and source alias, structural coordinate indices, contrast and population/treated targets. |
| `\ell,\mu_a(\ell)`, `\Omega_0,q_0,a_0,\ell_0,y_0,y_1` | Positive covariate strata, observed conditional means, and the abstract finite law used in the converse representation. |
| `\mathcal M_{=},\mathcal M_{\ne},\kappa(i,j),(a,i,j),p_0,p_1,b` | The two coupling models, their latent pair law, randomized outcome coordinates, marginal success probabilities and probability of benefit. |
| `U_L,U_A,(u_L,u_A)` | The fully specified eight-outcome model used for posterior prediction, ATE and ATT. |

## Author checks and next requirement

The unchanged existing editorial scanner reports no findings, 25 labels,
nine statuses, nine annex items and nine reciprocal pairs. Both citation
keys are available. All four external references resolve in the actual
predecessor bodies; no label collisions with those bodies were found.
These are author source-structure checks, not independent acceptance.

The full assigned finite counterfactual component is written. Identification
algorithm soundness/completeness, including any general counterfactual
identification algorithm, remains a distinct required component. Consolidated
independent reviews begin only after the full manuscript change set is made.
