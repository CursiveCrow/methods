# P15-U1: independent events and random variables

Written 8 September 2026 in the 08:46--09:31 UTC author block. The assigned
writing is supplied and returned directly for integration under the user's
current writing-first instruction. No review task or review wait was created.

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p15/independent-random-variables.tex` | 403 | 19870 | `82F2529BE42722377C2F3D000F2AFDE1842E8E681F6185A61B5701A5171E29A4` |
| `handbook/annex/p15/independent-random-variables.tex` | 606 | 28751 | `016D354887C6A6B65D7EE42DBE53F859F158BBD34BC2A839C1CCE21BAE09A79B` |

The three assigned paths were verified unused before writing. Only these two
new LaTeX files and this note were authored; shared files remain root-owned.
The complete saved body and annex and the final changed passages were read.

## Exact source and completed extent

Durrett, *Probability: Theory and Examples*, author Version 5 dated
11 January 2019, held at
`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`.
Reverified SHA-256:
`AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886`.
Reuse `DurrettPTEAuthor2019`; no new bibliography entry is needed.

The selected core was frozen before authoring: Section 2.1 through
Section 2.1.2, printed pages 43--49 / physical 51--57, comprising the
definitions and numbered results 2.1.1--2.1.14. Every complete page was
personally read as text and as a source page image. Source results 2.1.6
and its Appendix A.1 pi-lambda proof use the already fully written
`thm:p15-measure-uniqueness` interface.

Additional completed source components are the finite construction on
printed p. 53; Exercises 2.1.2, 2.1.6, 2.1.9 and 2.1.15 on pp. 54--56;
and Theorem 2.2.1, Lemma 2.2.2 and Theorem 2.2.3 on pp. 56--57.
Complete physical pages 61--65 were personally read as text and images.
The intervening source convolution pages, physical 58--60, were read as
text to identify the exact next component. Source images are retained
under the task workspace's `tmp/pdfs/p15-independence-source/`.

The source's Lemma 2.1.5 proof on printed p. 46 displays an index set
selecting the whole-space factors in an equality that needs the other
factors. This was checked against the page image. The new proof directly
uses `K={i:A_i != Omega}`, with the empty case included. The original
source remains unchanged; no correction instruction is inserted into
the reader's derivation. The source's three-coin Example 2.1.4 is retained
on its actual eight-outcome model, separately from the earlier finite
chapter's four-outcome example.

## Ten complete statement/proof pairs

Each suffix has body label `thm:p15-<suffix>` and reciprocal annex label
`annex:p15.<suffix>`.

| Suffix | Supplied content |
| --- | --- |
| `independence-basic` | Event/indicator/generated-sigma-algebra equivalences; complements; finite/countable subfamilies; null and certain events; positive-event conditioning; measurable a.s. replacements. |
| `independence-generators` | Adjoining Omega, full-family versus subfamily tests, explicit lambda-system proof and coordinate-by-coordinate extension of independent pi-systems. |
| `independence-thresholds` | The source's real-plus-infinity threshold criterion, rational-plus-infinity sufficient criterion, and every-finite-subfamily form. |
| `independent-blocks` | Disjoint finite or countable groups, their finite-intersection pi-systems, empty groups, measurable outputs, the direct two-function inverse-image proof, and the source's past/future example. |
| `independent-product-law` | Joint law equals product exactly under independence, construction for arbitrary finite probability spaces and prescribed real CDFs, countable-valued point-mass criterion. |
| `independent-expectations` | Product-law integration and both iterated orders; signed a.e. section conventions; nonnegative zero/infinity cases; all finite integrable products; converse bounded-function tests. |
| `independent-moments` | Covariance existence and formula, correlation domain/bound, full weighted-sum variance formula, uncorrelated and pairwise-independent specializations. |
| `independence-counterexamples` | Source Examples 2.1.4 and 2.1.14 with complete calculations and full parameter range; Exercise 2.1.9 generator countermodel; an overlapping-group failure. |
| `dyadic-independent-coins` | Actual source Exercise 2.1.15 sequence on the existing uniform space; exact floor recurrence, all prefix cells, all finite bit patterns and dyadic endpoints. |
| `independent-l2-weak-law` | Source general moment-to-probability implication and first mean-square weak law under pairwise uncorrelated bounded variances, including an explicit fair-bit empirical-average bound. |

Random-element and countable-block formulations are explicitly proved
extensions of the source's finite real-variable statements. No missing
measurability, finite moment, or infinite-product existence is assumed.

## Verified dependencies and integration

The actual relevant definitions/proofs were read in the five preceding
chapter pairs. Current SHA-256 identities, listed body / annex:

| Predecessor | Body hash | Annex hash |
| --- | --- | --- |
| `finite-probability` | `934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1` | `7CE651CE52FE8BFA66E5BEC221BDF48EE6318538E6A99B8E987E18C90D6B67F3` |
| `measurable-probability` | `C249F33E0E0FC88084B05A7D44098DB87B3E4814083B34709D6DBE2B562340D9` | `FBB9E6C733A1F286F7E56FC31B7E76D4412D781E03711ED02D8D4B3AAEF8C8FC` |
| `measure-extension` | `E1333244607DB51AE1EE5EC8FBF6AECA9AE8A2D85989677ED29ED9866119558E` | `D5179047198A9EDDE628274345D19DE75E30FC33CE065DAEC9F23F02DE83838F` |
| `integration-expectation` | `A29C887386C298112FC4E9820C6A37B3E934112EF32D704A9CC5EE77F5D909D5` | `F5F1AE8A99F95BE08E1C4A448EF1DF865D9B49E6D238A6DECED46BEF82EBC7FE` |
| `product-measures` | `9FFEDE5090864204636CEA69B317F2CEF9E82105A90A47DB8F75764FD23EE0AC` | `E62A873EE1BC0B6435F19ABE71F9B121FD4EB53BA0B3322863BBF61186E1CAB4` |

Root should append the new body and annex after `product-measures` in the
P15 drivers, candidate chapter P15.6 at the observed driver. The predecessor
product chapter's independence boundary can then point to this actual
treatment while retaining its other owed representation results.

Notation intake for P15.6: indexed event families `A_i`; finite index sets
`I,J,K`; event collections `\mathcal C_i`, whole-space extensions
`\overline{\mathcal C}_i`, sigma-algebras `\mathcal F_i`, block index sets
`I_j`, generated `\mathcal G_j`, and the proof lambda-system `\mathcal L_D`;
random elements `X_i`, their spaces `(S_i,\mathcal S_i)`, threshold `t_i`,
and grouped `X_{i,j},f_i`; marginal measures `\mu_i,\mu,\nu`; finite
partial sums `S_n`; `\operatorname{Cov}`, `\operatorname{Corr}`, real means
`\mu_X,\mu_Y,\mu_i,\mu`, coefficients `a_i` and variance bound `C`;
dyadic `Y_n(u),q_n(u),C_k,\varepsilon_j` and floor.
The marginal-measure and real-mean uses of `\mu`/`\mu_i` have different
explicit local types in their respective theorem contexts. Keep those
roles declared when reconciling the canonical registry. Existing general
probability, expectation, variance, product and absolute-value rows can
be extended where compatible; no new macro is needed.

The existing scanner finds ten reciprocal proof pairs and no scoped
findings; the reused bibliography key resolves. New references were
checked against the actual twelve files comprising this pair and the five
predecessor pairs: none is missing and no new label is duplicated there.
No manuscript build, rendered-manuscript inspection, new test, independent
review or formal-admission claim was made. Completed writing is available
for immediate integration and continued authorship.

## Exact next required writing

Continue with source Section 2.1.3, results 2.1.15--2.1.20, printed
pp. 49--52: convolution CDF, the density case, gamma/beta normalization
and both source gamma-sum arguments, then the full normal-sum calculation.
Separately supply Theorem 2.1.21 / Appendix A.3 for general consistent
finite-dimensional laws and Theorem 2.1.22 with its missing measurable
inverse/image details. The completed fair-bit construction is not that
general extension theorem. Remaining independence exercises are
2.1.1, 2.1.3--2.1.5, 2.1.7--2.1.8 and 2.1.10--2.1.14.
The first mean-square weak law is now written; later weak-law regimes,
Borel--Cantelli, strong laws and zero-one theorems remain separate writing.
