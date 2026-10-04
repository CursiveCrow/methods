# P15-U1: product measures and iterated integration

Date: 8 September 2026. Authoring block began at 06:19 UTC, with a
07:04 UTC deadline. Requirement scope: P15-U1 / N-x-008, following the
approved probability-foundation continuation. This is a completed author
draft of the bounded component below; independent review and integration
are still required. It does not close U1 or any whole-book release gate.

## Saved component

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p15/product-measures.tex` | 391 | 17874 | `9FFEDE5090864204636CEA69B317F2CEF9E82105A90A47DB8F75764FD23EE0AC` |
| `handbook/annex/p15/product-measures.tex` | 571 | 28093 | `E62A873EE1BC0B6435F19ABE71F9B121FD4EB53BA0B3322863BBF61186E1CAB4` |

Only these two new LaTeX files and this note were authored. Shared drivers,
bibliography, registry, generated files and existing manuscript text were
left to the lead integrator. The author read the saved body and annex in
full, then reread the final changed hypothesis and grouping passages.

## Frozen source and complete assigned extent

Rick Durrett, *Probability: Theory and Examples*, author Version 5 dated
11 January 2019. Existing local file:
`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`.
The title/version page was personally read; the file has 490 physical
pages, 2,195,717 bytes, and SHA-256
`AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886`.
The existing bibliography key is `DurrettPTEAuthor2019`; no new entry is needed.
The held author PDF originated at
[Durrett's Duke author site](https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf).

The assigned core was frozen before authoring as Section 1.7's opening,
Theorem 1.7.1 and finite-product paragraph, Theorem 1.7.2 with its full
proof, Lemmas 1.7.3 and 1.7.4, and Examples 1.7.5--1.7.8: printed
pages 37--41, physical pages 45--49. Those five complete pages were
personally read both as extracted text and as rendered source pages.
The retained source-reading images are under the task workspace's
`tmp/pdfs/p15-product-source/page-045.png` through `page-049.png`.
They are primary-source reading evidence, not manuscript production evidence.

Exercises 1.7.1 and 1.7.2 on printed page 41 are also fully supplied.
The later exercise extent on printed pages 41--42 was read as text to
identify the next boundary. Exercises 1.7.3--1.7.5 are not claimed complete
by this component.

Personally read source prerequisites include Theorem 1.1.9 and its
adjacent semialgebra material on printed pages 5--6 (physical 13--14),
the integral and convergence context on printed pages 24--28
(physical 32--36), including Theorem 1.5.7 and Exercise 1.5.6, and
the complete extension/pi-lambda development in Appendix A.1 on printed
pages 455--460 (physical 463--468). These prerequisite pages were read
as text. The new proof uses the already written manuscript's direct
monotone-convergence construction and its proved agreement with the
source integral, rather than copying the source's dependency order.

## Exact manuscript dependencies

| Existing file | SHA-256 |
| --- | --- |
| `handbook/parts/p15/measurable-probability.tex` | `C249F33E0E0FC88084B05A7D44098DB87B3E4814083B34709D6DBE2B562340D9` |
| `handbook/annex/p15/measurable-probability.tex` | `FBB9E6C733A1F286F7E56FC31B7E76D4412D781E03711ED02D8D4B3AAEF8C8FC` |
| `handbook/parts/p15/measure-extension.tex` | `E1333244607DB51AE1EE5EC8FBF6AECA9AE8A2D85989677ED29ED9866119558E` |
| `handbook/annex/p15/measure-extension.tex` | `D5179047198A9EDDE628274345D19DE75E30FC33CE065DAEC9F23F02DE83838F` |
| `handbook/parts/p15/integration-expectation.tex` | `A29C887386C298112FC4E9820C6A37B3E934112EF32D704A9CC5EE77F5D909D5` |
| `handbook/annex/p15/integration-expectation.tex` | `F5F1AE8A99F95BE08E1C4A448EF1DF865D9B49E6D238A6DECED46BEF82EBC7FE` |

The actual prerequisite LaTeX was read for sigma-algebras and generation,
measure continuity, countable nonnegative sums, Borel generators,
measurability and simple approximation, the full pi-lambda proof,
semialgebra extension and its countable-cover existence/uniqueness proof,
Borel Lebesgue lengths and the uniform restriction, nonnegative and signed
integration, monotone convergence, null-set invariance and zero/finite
integral criteria. Unrelated prior chapter results are not independently
reaccepted here. The governing contract and conventions were read at hashes
`C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3`
and `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242`.

## Nine complete statement/proof pairs

Each suffix below has body label `thm:p15-<suffix>` and reciprocal annex
label `annex:p15.<suffix>`.

| Suffix | Supplied content and source relationship |
| --- | --- |
| `product-sections` | Full set and function sections at every point; coordinate measurability criterion; Borel finite-dimensional product identity. Lemma 1.7.3 plus proved consequences. |
| `product-existence` | Well-defined rectangle mass, semialgebra complement decomposition, countable disjoint rectangle identity by one-variable integration, premeasure extension, sigma-finite uniqueness and probability case. Theorem 1.7.1; unrestricted existence explicitly derives from the earlier extension theorem. |
| `finite-product-measures` | Inductive finite products, domain equality, common finite-rectangle uniqueness, grouping and permutation, Borel Euclidean volume. Full source finite-product consequence and proved identifications. |
| `section-measures` | Explicit finite-box functions, lambda-system closure with only finite subtraction, two increasing exhaustions, both section-integral identities and null-section criterion. Full Lemma 1.7.4. |
| `tonelli` | Indicator, simple and general nonnegative cases; measurable section integrals at every point; three monotone-convergence steps; infinite values and a.e. invariance. Nonnegative branch of Theorem 1.7.2. |
| `fubini` | Extended real integrable input, measurable absolute-section functions and null sets, finite representatives of positive/negative section integrals, both signed equalities, absolute bound and measurable a.e. replacements. Signed branch of Theorem 1.7.2. |
| `fubini-failures` | Complete Examples 1.7.5--1.7.8: two distinct orders of the counting series, continuous exponential example with both product parts proved infinite, measurable diagonal with a nonsigma-finite counting factor, and the CH/choice-dependent order example showing separate measurability is insufficient. Includes the elementary one-variable integral justification used by the worked square example. |
| `absolute-iterated-series` | Three equivalent absolute-integrability criteria, measurable encoding of a sequence on the counting product, a.e. absolute convergence, measurable sum and absolute numerical convergence. Exercise 1.7.1 and its corollary. |
| `layer-cake` | Countable-rectangle description of the subgraph, all zero/finite/infinite section lengths, area and tail formula and expectation specialization. Exercise 1.7.2. |

The body additionally supplies the worked triangular integral on the unit
square, a product-integrable function whose section at one null point is
not integrable, a method entry for choosing an order, and the explicit
product-domain/completion boundary. The example calculations use ordinary
one-variable calculus with its relation to the constructed Lebesgue
integral justified by simple-function bounds in the annex.

Source precision: the source calls both branches Fubini; this chapter
explicitly declares the Tonelli/Fubini naming split. The source's
`\mathcal A\times\mathcal B` notation is retained with its generated
sigma-algebra type; `\otimes` is an explicitly identical alternative.
The variable/measure mismatch in the last displayed line of the source's
Example 1.7.7 is resolved directly in the new formulas: the inner integral
over X uses `d\mu_1(x)` and the outer integral over Y uses `d\mu_2(y)`.
The two values and all source hypotheses are retained. The new signed
statement does not silently assign `infinity - infinity` on exceptional
sections, and the construction never replaces the product sigma-algebra
by a completion.

## Root integration and notation contributions

Append the body after `integration-expectation.tex` in `handbook/parts/p15.tex`
and the matching annex after that prerequisite in `handbook/annex/p15.tex`.
The next chapter scope is P15.5 if the existing four-chapter order is retained;
the root must verify that scope against its current driver. No canonical
symbols or generated tables were changed by this author.

The following are local notation contributions for root reconciliation;
reuse existing compatible general rows and record each actual distinct
typed role where needed. First use is the new P15 chapter.

| Glyphs | Local types and roles |
| --- | --- |
| `X,Y,\mathcal A,\mathcal B` | Factor sets and their sigma-algebras, declared separately. |
| `\mathcal S,\mathcal A\times\mathcal B,\mathcal A\otimes\mathcal B` | Rectangle family; generated product sigma-algebra and its explicit alias. |
| `A\times B,m(A\times B)` | Measurable rectangle and its nonnegative preliminary mass. |
| `\mu_1,\mu_2,\mu_1\times\mu_2,\rho` | Factor measures; specified product construction and its local measure alias. |
| `E_x,E^y,f_x,f^y` | Set sections and function sections in the two coordinate directions. |
| `\pi_X,\pi_Y` | Coordinate projection maps. |
| `\lambda^n` | Finite product Borel Lebesgue measure on Euclidean n-space. |
| `T_1f,T_2f` | Everywhere-defined nonnegative extended section-integral functions. |
| `H_1,H_2,N_1,N_2` | Absolute-section integral functions; their measurable infinite-value null sets. |
| `I_1f,I_2f` | Real measurable signed section-integral versions, zero on the displayed exceptional sets. |
| `F_n,G_n,H_n,F_{i,k}` | Increasing finite-measure factor covers and product rectangles, local to the relevant proofs. |
| `g_{n,E},\mathcal L_n` | Finite-box section-measure function and its lambda-system of valid product sets. |
| `P_i,Q_i,\widetilde P_i,\widetilde Q_i` | Nonnegative positive/negative section integrals and their finite null-set replacements. |
| `\phi,c_+,c_-` | Exponential difference as a function of the product coordinate, and strictly positive compact-interval bounds in the second counterexample. |
| `\omega_1,b,<'` | Countable-ordinal domain, explicitly assumed CH bijection, and transported order in the conditional fourth counterexample. |
| `\kappa,F(n,y),H(y),N,S` | Counting measure, sequence encoding, absolute sum, exceptional set and measurable signed-sum version in the series proof. |
| `D_g` | Measurable strict subgraph for the layer-cake formula. |

## Checks and next boundary

The existing `tools/check.py` scanner was applied to the two new files.
It reports no scoped grammar/label/body-proof/citation findings, nine
statuses and nine annex items, all reciprocal, with no duplicate labels.
The bibliography check finds the reused key among 639 entries with zero
intake stubs. New cross-references were checked against the actual eight
LaTeX files consisting of this pair and the three prerequisite pairs:
none is missing and none of the new labels is duplicated there.
These are bounded structural checks, not a whole-tree or admission claim.
No software tests were written, no manuscript build or rendering was run,
and no publication output was changed.

The next writing boundary remains the explicitly identified source
Exercises 1.7.3--1.7.5 and the separate infinite-product, completion,
density/Radon--Nikodym, conditional-expectation and independence treatments.
Root integration, canonical notation review, three independent text roles,
scoped production and formal admission remain separate required actions.
