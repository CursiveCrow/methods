# P15-U1: convolution, gamma and normal laws

Written 8 September 2026 in the block beginning 09:17 UTC, deadline
10:02 UTC. The complete assigned writing is returned for integration and
continued authorship. All independent reviews remain deferred under the
user's current instruction; no review task or review wait was created.

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p15/convolution-gamma-normal.tex` | 372 | 16566 | `69BC989E02F7FA841B319D52B07DD86207E3881BCC2AC25186E5002F3C32F400` |
| `handbook/annex/p15/convolution-gamma-normal.tex` | 611 | 27338 | `F915D65409E2BF15BE1215DFDE65E7D807287B99906119C8DBCC916CB94BC44A` |

The three assigned paths were verified unused before writing. Only the
two new LaTeX files and this note were authored. The complete saved body
and annex were read, and the final changed qualifications were reread.

## Exact primary source and completed scope

Durrett, *Probability: Theory and Examples*, author Version 5 dated
11 January 2019, held as
`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`.
Current verified SHA-256:
`AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886`.
Reuse the existing `DurrettPTEAuthor2019` key; no new bibliography entry.

Before authoring, the exact selected presentation was frozen as results
2.1.15--2.1.20, printed pages 49--52 / physical pages 57--60. The complete
pages were personally read as text and source images. The exponential
and normal prerequisites, Examples 1.6.10--1.6.11 on printed pages 33--34 /
physical 41--42, were also read completely as text and images; their omitted
normalization and moment calculations are supplied here. Additional source
Exercises 2.1.1 and 2.1.10 are completed: their physical pages 62--63 were
read as text in the preceding independence block and reread as images here.
The source images are retained in the task workspace under
`tmp/pdfs/p15-convolution-source/` and, for the two exercise pages,
`tmp/pdfs/p15-independence-source/`.

The source's gamma convention is positive shape and positive rate; its
normal second parameter is variance. The normal density prerequisite
explicitly uses positive standard deviation on printed p. 34. The new
`normal(mu,0)=delta_mu` convention is explicitly declared as an extension
and proved through constant laws, never by dividing the density formula
by zero. Gamma and beta endpoint density values are explicitly zero;
the power formulas apply on the open positive support. The proved a.e.
uniqueness/replacement result justifies those versions of the same law.

## Ten complete statement/proof pairs

Each suffix has body label `thm:p15-<suffix>` and reciprocal annex label
`annex:p15.<suffix>`.

| Suffix | Supplied argument |
| --- | --- |
| `density-integrals` | Construction of a probability from a normalized nonnegative density, integration against that law, signed integrability, a.e. uniqueness, measurable nonnegative replacements and the point-mass distinction. |
| `affine-lebesgue` | Affine Borel measure scaling from interval lengths and uniqueness, positive/negative slopes, indicator/simple/monotone integral extension, signed case, transformed density and the zero-slope Dirac case. |
| `convolution-law` | Pushforward definition, source CDF identity with dG as a probability measure, nonnegative integral formula, commutativity/associativity/Dirac shifts, and integer convolution. |
| `convolution-density` | Source one-density and two-density cases, full Borel measurability and all-event calculation, the source CDF specialization, total normalization and possible null-set infinite values. |
| `factorized-joint-density` | Source Exercise 2.1.1 with unnormalized factors: repeated Tonelli forces every factor integral to be finite positive, their product one, and the normalized factors to be independent marginal densities. |
| `gamma-normalization` | Finiteness and positivity of Gamma, endpoint/tail estimates, recurrence and factorials, rate scaling, normalization, all integer moments, mean and variance, including the source exponential calculations. |
| `beta-gamma-convolution` | Beta finiteness and symmetry, exact source rescaling, both full source proof routes, gamma sum law and finite common-rate induction, exponential-sum consequence, and normalized beta moments. |
| `normal-normalization` | Gaussian integral from Tonelli and fixed-parameter affine substitutions, elementary antiderivative evaluation, absolute first moment, odd integral, second moment by bounded-interval integration by parts, and general normal mean/variance. |
| `normal-sums` | All affine normal transformations, the source's complete centered square expansion and every prefactor, restoration of means, separate zero-variance cases, and finite independent sums. |
| `convolution-calculations-boundaries` | Atomic binary and triangular uniform convolutions, explicit gamma/beta/normal calculations, unequal exponential rates, dependent normals summing to a point mass, and excluded gamma parameters. |

The gamma normalization route first constructs and normalizes both input
gamma densities without using the beta-gamma identity. The convolution's
unit mass then determines its constant. The second source route independently
uses Tonelli on the nonnegative triangle integral. Gaussian normalization
uses y=x t only as a one-variable affine substitution for each fixed x>0,
then a one-variable antiderivative; there is no polar-coordinate or general
multivariable change-of-variables theorem hidden in the derivation.

## Existing dependencies and root integration

The new arguments use the actual measure-extension, integration/expectation,
product-measure and independence files. The compact-interval C1/calculus
bridge is the explicit initial argument in `annex:p15.fubini-failures`;
all new unbounded endpoint steps use monotone convergence. Relevant fixed
identities, body / annex:

| Predecessor | Body SHA-256 | Annex SHA-256 |
| --- | --- | --- |
| `measure-extension` | `E1333244607DB51AE1EE5EC8FBF6AECA9AE8A2D85989677ED29ED9866119558E` | `D5179047198A9EDDE628274345D19DE75E30FC33CE065DAEC9F23F02DE83838F` |
| `integration-expectation` | `A29C887386C298112FC4E9820C6A37B3E934112EF32D704A9CC5EE77F5D909D5` | `F5F1AE8A99F95BE08E1C4A448EF1DF865D9B49E6D238A6DECED46BEF82EBC7FE` |
| `product-measures` | `9FFEDE5090864204636CEA69B317F2CEF9E82105A90A47DB8F75764FD23EE0AC` | `E62A873EE1BC0B6435F19ABE71F9B121FD4EB53BA0B3322863BBF61186E1CAB4` |
| `independent-random-variables` | `82F2529BE42722377C2F3D000F2AFDE1842E8E681F6185A61B5701A5171E29A4` | `016D354887C6A6B65D7EE42DBE53F859F158BBD34BC2A839C1CCE21BAE09A79B` |

At the observed return-time driver, P15 still ends with `product-measures`.
Root should append the completed independence pair first and then this
convolution pair. Their resulting scopes are P15.6 and P15.7. Root also
owns the predecessor's now-supplied convolution boundary/forward link.

Notation contributions for P15.7: density functions `f,g,h,p` and law
`\eta`; Borel measures `\lambda,\lambda^d,\mu,\nu`; Dirac `\delta_c`;
affine `T(x)=cx+d`; typed convolution `\mu*\nu`, `F*G`, `f*g`, and
Stieltjes `dF,dG`; factor integrals `c_i`; gamma `\Gamma(\alpha)`,
shape/rate `\alpha,\lambda`, density `g_{\alpha,\lambda}` and source
law name `\operatorname{gamma}`; beta `B(\alpha,\beta)` and
`\operatorname{beta}`; normal density `\phi_{\mu,a}`, source mean/variance
law `\operatorname{normal}(\mu,a)`; Gaussian half-integral `J`, gamma
convolution constant `c_{\alpha,\beta}` and the completed-square variance
`v=ab/(a+b)`. The scalar rate `\lambda` and the Lebesgue measure, and the
normal means `\mu,\nu` and earlier measure roles, are explicitly distinct
local types. Preserve those declarations in the canonical notation intake.

The existing scanner finds ten reciprocal statement/proof pairs and no
scoped findings; the existing citation key resolves. All new references
were checked against the new pair plus actual measurable-probability,
measure-extension, integration, product and independence pairs: none is
missing and no new label is duplicated there. No manuscript build/render,
new test, review task, review wait or admission claim was made.

## Exact next writing

Next supply Durrett Theorem 2.1.21 and Appendix A.3, the general Kolmogorov
extension for consistent laws on finite real-coordinate spaces, with its
actual measure-extension and approximation prerequisites. Then complete
Theorem 2.1.22 and its measurable coding/inverse/image details for the
source's stated measurable-space class. The earlier dyadic fair-bit
construction is already written and does not substitute for this general
extension theorem. Among the independence exercises, 2.1.1 and 2.1.10
are now supplied in addition to the preceding chapter's completed items.
