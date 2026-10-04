# P16 finite structural causal models: author return

Date: 7 September 2026, America/Los_Angeles; work began 8 September
2026 at approximately 06:21 UTC. This is the author return for a bounded
P16-C3 component and a finite P16-C4 identification component. It is not
independent acceptance, formal admission, or completion of either whole
work package.

## Files and actual extent

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p16/finite-causal-models.tex` | 418 lines, 19,781 bytes | `331568E5FF2329B4498CA98DCA7DC8BE79D4EB77B8A2152DAB33F05F05BABA42` |
| `handbook/annex/p16/finite-causal-models.tex` | 377 lines, 17,472 bytes | `1393539308C2668996B75AED30D47025F337944E0FC0270E863A153A00794096` |

Both files are new, independently worded LaTeX. The author read both actual
files completely after writing. No prior manuscript file, shared driver,
canonical symbol file, bibliography, generator, checker, restoration or
admission record was edited. The chapter and annex still require root's
route, notation and bibliography integration.

The body contains definitions of the graph, finite probability space,
exogenous disturbances, structural functions, solutions, interventions,
structural kernels and identification. It includes eight complete theorem
and annex pairs, a source-chain specialization, a finite calculation method,
one full confounded calculation, and two nonidentification constructions.

## Acquired exact primary presentation

Judea Pearl, *Causal inference in statistics: An overview*, Statistics
Surveys 3 (2009), 96–146, DOI `10.1214/09-SS057`. The held artifact is
the author's freely available UCLA Technical Report R-350, September 2009,
in journal layout with the journal title, volume, pagination and DOI on
the title page. It is not the 2009 book or a later primer.

- Official author download: [UCLA R-350 PDF](https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf).
- Official author listing: [UCLA Cognitive Systems Laboratory papers](https://bayes.cs.ucla.edu/csl_papers.html), R-350.
- Journal lead independently found: [Statistics Surveys DOI page](https://projecteuclid.org/journals/statistics-surveys/volume-3/issue-none/Causal-inference-in-statistics-An-overview/10.1214/09-SS057.pdf). That direct download did not supply this capture; the UCLA PDF did.
- Local capture: `source/references/pearl-causal-overview-2009/pearl-2009-ucla-r350.pdf`.
- PDF size: 593,923 bytes; 51 readable pages.
- SHA256: `1A5ECB7CB7C55A9B4F2C09AAC091BC01A3EABFC94FC55EE692EFBC013A8B7581`.
- PDF metadata identifies Pearl, the article title and Statistics Surveys
  2009, volume 3, pages 96–146; creation and modification metadata date to
  21 September 2009. The title-page R-350 imprint says September 2009.
- The local `source/` and `tmp/pdfs/` filename inventories contained no
  Pearl/causal/SS057 capture before acquisition. This records the checked
  holdings scope, not a claim about every arbitrarily named historical file.

The author read the complete title page and complete printed pp. 103–113
(physical PDF pages 8–18), using both extracted text and all eleven full
page images. Title identity was also visually verified. Required mathematical
source extent for this component is pp. 104–112, with pp. 103 and 113 read
for section boundaries. Retained source images are `title-01.png` and
`source-08.png` through `source-18.png` in the capture folder. They are
primary-source reading evidence, not manuscript renders. Poppler reported
two missing display-font aliases during title rendering; the actual title,
author, DOI, journal and R-350 imprint were visible and read. No such
unreadable mathematical item was substituted with an extraction guess.

## Source mapping and necessary qualification

| Source location | Manuscript treatment |
| --- | --- |
| pp. 104–105, exogenous/endogenous distinction and directed assignment interpretation | `def:p16-finite-scm` explicitly declares allowed parents, total functions and a joint exogenous law; named parents may be inactive arguments. |
| p. 107, Eq. (5), autonomous structural functions | Finite structural functions and the explicit invariance stipulation in `def:p16-causal-intervention`. |
| pp. 107–108, Eqs. (6)–(7), equation replacement and post-intervention law | `def:p16-causal-intervention` and the solution/intervention theorems; simultaneous replacement is also included. |
| p. 108, Eq. (8), contrast of intervention means | Finite response-function mean and specified average intervention contrast. No empirical efficacy claim is imported. |
| p. 109, Definition 2 and Eq. (10) | Correct two-model observational-equality criterion in `def:p16-causal-identification`; finite-sample estimation explicitly distinct. |
| p. 110, Theorem 1 and Eq. (15) | Complete finite proof of the structural product, plus equality of kernels and observational conditionals only on positive parent events. |
| p. 111, Corollary 1 and Eq. (17) | Complete simultaneous-intervention truncated-product proof in terms of total structural kernels. |
| pp. 107–111, three-variable chain, Eqs. (5)–(7), (16)–(17) | `def:p16-causal-chain`, a finite specialization with explicit condition for the observational conditional expression. |
| p. 112, simultaneous interventions | Covered by the arbitrary intervention index set in the truncated theorem; no claim to reproduce the complete five-variable example or later sequential-treatment theory. |

Two source issues are handled directly in the mathematical statements.
First, the actual p. 109 image visibly prints `P(M1)=P(M1)` in Eq. (10).
The surrounding two-model definition and explanation require comparison
of `P(M1)` with `P(M2)`. The manuscript states that correct comparison;
this note preserves the printed reading. No reader instruction to repair
the active formula is inserted.

Second, the source's pp. 110–111 prose about identifying all interventions
in Markovian models does not state a positivity condition there. In the
finite setting adopted here, structural kernels exist even at unobserved
parent configurations, while observational conditional ratios do not.
The manuscript therefore proves the product without positivity, identifies
its kernels with conditionals only on positive parent events, and states a
full-observation/full-positive-support sufficient identification theorem.
The explicit `X=0, Y=0` versus `X=0, Y=X` pair proves why independence
and acyclicity alone do not identify an intervention at an unobserved
treatment level. This is a proved qualification, not an unverified
historical-emendation claim about other possible source conventions.

All finite constructions, topological proofs, null-event handling and binary
examples are supplied by the handbook. No source figure, protected paragraph,
empirical sample, empirical percentage or substantive result from an unread
part of the article is reproduced. The source's linear path-coefficient
discussion, general separation theorem and later identification/counterfactual
theory remain distinct obligations where required by the edition catalog.

## Complete proof pairs

Every body identifier below begins `thm:p16-`; every annex identifier begins
`annex:p16.`. Suffixes coincide.

| Suffix | Complete extent |
| --- | --- |
| `causal-topological-order` | A finite predecessor chain would produce a cycle; removal yields all vertices in parent-before-child order. |
| `causal-solution` | Existence by total topological evaluation, uniqueness by induction, independence of the chosen order, full law and marginal grouping including empty coordinate tuples. |
| `causal-intervention-laws` | Modified graph acyclicity, totality and unique law; support at the intervention value; pointwise consistency; all nonintervened nondescendants unchanged; empty intervention and commutation of disjoint fixed replacements. |
| `causal-factorization` | Finite rectangular independence, exact equivalence of a solution fiber and fixed-tuple equation events, product formula, dependence of earlier variables only on earlier disturbances, and the conditional kernel identity with its positive denominator. |
| `causal-truncation` | Independence survives replacement; intervened kernels are point masses; unchanged kernels retain their total original values; every intervention subset, full and empty cases, and marginalization. |
| `causal-positive-identification` | Positive full support supplies all parent-event denominators; rational expression in the observational law; equality for every model in the fixed class; marginal and finite-response consequences. |
| `causal-confounded-example` | All eight exogenous probabilities, all four observed pair masses, positive conditioning, both intervention values, zero versus one-quarter mean differences, and direct measured-common-cause adjustment. |
| `causal-nonidentification` | Two fully specified models with the same allowed binary graph and positive common observational table but targets 1/2 and 5/8; a second independent-disturbance pair with observational point mass and targets zero and one. |

The first binary pair permits dependent disturbances in its stated model
class. The reduced common-cause model's allowed edge is explicitly inactive,
which is permitted by the definition; no faithfulness or minimal-graph
assumption is silently added. The full three-variable common-cause model has
independent disturbances. Projecting its endogenous variables to X and Y
produces dependent disturbances, so the reduced model cannot reuse the
independent-kernel product theorem.

## Bibliography intake for the lead

Proposed new key, already used by the chapter and annex:

```bibtex
@article{Pearl2009CausalOverview,
  author = {Pearl, Judea},
  title = {Causal inference in statistics: An overview},
  journaltitle = {Statistics Surveys},
  volume = {3},
  date = {2009},
  pages = {96--146},
  doi = {10.1214/09-SS057},
  url = {https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf},
  urldate = {2026-09-07},
  note = {Author-hosted Technical Report R-350, September 2009, in journal layout}
}
```

No canonical bibliography write was performed by the author. The key must be
integrated before compilation or a full citation check can pass.

## Notation intake for the lead

Expected local chapter scope is `P16.2` after the existing finite-abduction
chapter. Confirm the actual integrated position before selecting canonical
first-use values. These are proposed typed families; no macro definitions
are introduced.

| Glyph family | Role and explicit standing |
| --- | --- |
| `N,n,G=(N,E),j\to i,\operatorname{pa}_G(i),\operatorname{de}_G(I)` | Finite endogenous index set and size; directed graph and allowed edge set; parents and strict-path descendants. A listed edge may be functionally inactive. |
| `i_1,\ldots,i_n,I,J,O` | A topological enumeration; arbitrary intervention/marginal coordinate sets; common observed coordinates in a model class. Empty coordinate products contain one tuple. |
| `S_i,S_J,v,v_J,s,x,()` | Nonempty finite value sets and indexed products; full and projected assignments; marginal tuple, fixed intervention tuple and empty parent tuple. |
| `M,\Omega,q,\mathbb P,\mathcal U_i,U_i,f_i` | Finite structural model, exogenous outcome space/mass/event law, finite disturbance value sets/functions, and total equation functions. Joint disturbances may be dependent unless explicitly restricted. |
| `V_i,V,V_J,p_M,p_{M,J}` | Uniquely evaluated endogenous random variables, full/projected solution tuple, full and marginal observational mass functions. |
| `M_{I=x},V^{I=x},p_M^{I=x},\operatorname{do}(V_I=x),\mathbb P_M(\cdot\mid\operatorname{do}(V_I=x))` | Equation-replaced model, pointwise solution, intervention law and traditional intervention notation. The bar naming do is an operation separator, not conditioning on an event. |
| `h,\mathbb E[h(V_J^{I=x})]` | Fixed real-valued response on a finite coordinate product and its intervention mean. |
| `r_i,k_i(b\mid a)` | Disturbance marginal and total structural kernel. Here a is a parent tuple and b an output value; the kernel exists even at observationally null parent inputs. |
| `\mathcal C,Q(M),M_1,M_2` | Specified model class, target functional and compared models for identification. Observational equality is across the two models, not a reflexive equality. |
| `Z,X,Y,z,x,y,U_Z,U_X,U_Y` | Named endogenous variables and values in finite chain and common-cause examples, with their named disturbances. |
| `\oplus,\alpha,\beta,q_B,(z,a,b),(c,d)` | Bit exclusive-or, two stated binary mass functions, second-model joint mass, and local exogenous coordinates; these local a,b are bits rather than the general kernel's tuple/output placeholders. |
| `M_A,M_A',M_B,M_C,M_D,\widetilde U_X,\widetilde U_Y` | Explicit common-cause, reduced, direct-cause and null-support witness models; reduced paired disturbances share a common bit. |
| `A_i(v),L,H,u_L` | Fixed-assignment disturbance fiber, preceding vertices in a topological order, nonintervened nondescendants, and an indexed earlier-disturbance tuple in the proofs. The proof's H is a vertex set, not abducible hypotheses from P16.1. |

## Dependencies and checks actually performed

The governing contract and conventions were read completely. The relevant
P16-C3/C4/C5 work-package rows and their identification criterion were read.
The actual finite-probability definitions/theorems and finite-abduction
interface were inspected. Current hashes checked in this block:

- `handbook/CONVENTIONS.md`: `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242`.
- `spec/EDITION-2026-CONTRACT.md`: `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3`.
- `handbook/parts/p15/finite-probability.tex`: `934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1`.
- `handbook/annex/p15/finite-probability.tex`: `7CE651CE52FE8BFA66E5BEC221BDF48EE6318538E6A99B8E987E18C90D6B67F3`.
- `handbook/parts/p16/finite-abduction.tex`: `0F7D93E64D6EAB11CD2904C509DB168621ADB93D9D5A9AE3F448D62BF7E1C6B6`.
- `handbook/annex/p16/finite-abduction.tex`: `D027F796A1A887DD7217C412DDF95FAC42F69A34CCE4F1DCFECB224C76E1A4B4`.

The existing `tools/check.py` scanner, hash
`05F22DEE54E3F177EAD79DFAE16D88787E513A58441F443278679F8BC7443914`,
was applied to these two new editorial files: 32 labels, eight body statuses,
eight annex items, all pairs reciprocal, no duplicate labels and no local
scanner findings. The sole citation key is the proposed Pearl entry above.
The three external references are `sec:p15-finite-conditioning`,
`sec:p15-finite-independence` and `sec:p16-finite-abduction`; their exact
labels exist in the current prerequisite body files. This is a scoped
structural diagnostic, not a full-tree or mathematical acceptance claim.

No manuscript build or rendering, prose-mirroring test, independent review,
formal acceptance or admission was performed. Fresh source/topic/publication
review, canonical intake, scoped production and the remaining P16 obligations
belong to subsequent work. The broader outstanding material includes general
graphical separation and identification methods, estimation assumptions and
procedures, counterfactual identification, cyclic models and separately
presented potential-outcome frameworks with proved bridges where required.
