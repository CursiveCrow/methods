# P15.20: Feller's separate median and symmetrization weak-law proof

Root integration: the body and annex are connected after the conditional-limit
unit. The earlier weak-law and rate boundaries now link the completed
Feller argument and its exact prerequisites. Canonical notation is merged;
the existing Feller1971ProbabilityII bibliography entry remains the source key.

Written 8 September 2026 in the author block beginning at the 13:54 UTC
clock checkpoint, with return due by 14:39 UTC. The full body and annex
are saved and have received the requested mathematical read-back.
Only the three assigned new files were edited. Root owns shared routes,
bibliography, notation and source import.

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| handbook/parts/p15/feller-weak-law-presentation.tex | 326 | 13955 | 82BBAE757126221A5B644AB2B7C72CF916912D7D95EBB37A18A050DD9670EE19 |
| handbook/annex/p15/feller-weak-law-presentation.tex | 553 | 22192 | 16EBD5426C691BA169502AC64D2894F642128B3CD8766A06E1775AA540A290E9 |

## Exact source identity and selected complete reading

William Feller, An Introduction to Probability Theory and Its
Applications, Volume II, second edition (bibliographic year 1971).
Canonical held file:
source/references/feller-probability-volume2-second-edition/feller-volume2-second-edition.pdf.
SHA-256:
CB87C933D4175234F5F5958A74F3A466ECF13C29BE4E0DFEDF9C9B739F717486.
The canonical file was verified to match the unchanged acquired scan.

The source is an undated Mei Ya reprint scan of the second edition.
Its exact physical printing year is not asserted. The title-page,
publisher-year verification, download provenance, missing copyright/date
leaf and MD5 record are in the preceding weak-law research note.
The requested canonical key Feller1971ProbabilityII was absent at the
start of this block and subsequently added by root. Its actual entry
was read before completing the new files. The body uses that existing
key; this author made no bibliography edit.

The frozen target is VII.7, its truncation lemma and Theorem 1,
printed pp. 234--236, including the median necessity chain and the
following finite-mean/symmetric-law remarks. The newly starting
positive-gain Theorem 2 on p. 236 is a distinct later component.
The complete required prerequisite passages were read before use:

| Passage | Printed pages | Physical pages | Reading |
| --- | --- | --- | --- |
| CDF/measure and expectation conventions in V.1 | 130--132 | 146--148 | Full text; relevant CDF/expectation images on 131--132. |
| Median definition and its local context in V.2 | 137 | 153 | Full text and image. |
| Reflection and direct symmetrization V.(5.1)--(5.3) | 148 | 164 | Full text and image. |
| Full Lemma 1, V.(5.6)--(5.8), and its proof | 149 | 165 | Full text and image. |
| Full Lemma 2, V.(5.9)--(5.13), continued largest-term proof | 149--150 | 165--166 | Full text and images. |
| V.(6.1)--(6.2), finite-interval integration by parts and complete partition proof | 150 | 166 | Full text and image. |
| VII.7 truncation lemma, functions and full Theorem 1 proof | 234--236 | 249--251 | Full text and images. |

The scan's page offsets are not globally constant: the required Chapter V
pages use printed+16, while the required Chapter VII pages use printed+15.
Images for this block are in the task workspace's
tmp/pdfs/p15-feller-weak-source/; the immediately preceding source read
also has the VII.7 page images in tmp/pdfs/p15-weak-law-source/.
Additional surrounding Chapter V text was read for context, not claimed
as an authored whole-chapter treatment.

## Complete source chain, without replacing it by Levy's proof

The new argument constructs actual product-space independent copies,
proves existence of a finite median and each lower/upper tail comparison,
and retains Feller's first-largest-absolute-term construction.
The selecting index is measurable and invariant under coordinate sign
changes. Partitioning by this index proves the fourfold joint sign
symmetry of the chosen summand and its remainder, without assuming
those two quantities are independent.

The source's sum-tail comparison then gives the exponential lower bound.
The main necessity proof uses V.(5.6), the strict consequence of
V.(5.9)--(5.10), and V.(5.7) in the source's order. The median radius is
its absolute value, and every step from the exponential bound to the
full real-parameter tail condition is supplied. No prior first-crossing
Levy proof or CLT replaces this chain.

Sufficiency retains Feller's clipping/union/Chebyshev proof. The complete
partition proof of Stieltjes integration by parts supplies the normalized
moment identity. The converse moment-to-tail implication, referred by the
source to a problem, is proved with an explicit dyadic estimate. Both
closed and half-open canonical centers are shown to work.

## Direct formula corrections and explicit endpoint treatment

- Reflection uses (-F)(x)=1-F((-x)-) at arbitrary atoms; the source's
  simpler expression is preserved as its continuity-point form.
- The largest-term hypothesis is stated for all Y_1,...,Y_n. The scan's
  Lemma 2 line begins at X_2 although its sum and proof include X_1.
- The source's two remainder-sign pieces need not have equal probability
  when the remainder is zero. The complete proof uses the valid
  at-least-half estimate, retaining the zero mass explicitly.
- V.(5.10)'s non-strict left threshold and its CDF tail are retained.
  Strict and non-strict exact absolute-tail variants are proved separately;
  a fair-sign atom shows why they cannot be silently interchanged.
- VII.(7.5) has the correct single-summand second-moment coefficient
  1/(n epsilon^2), obtained from n variance contributions. The scan prints
  n^2 in that denominator. A two-sign example gives an explicit failure
  of the smaller printed bound.
- In VII.(7.7), the integral of tau has no extra factor of its integration
  variable. The corrected half-open identity is
  sigma_h(t)=-tau(t)+(2/t) integral_0^t tau(y)dy.
- Closed clipping includes the possible atom at -t. Therefore
  sigma(t)=sigma_h(t)+t P(X=-t) and
  m(t)=m_h(t)-t P(X=-t). These relations are stated and proved;
  the source's tail tau(t)=t[1-F(t)+F(-t)] is retained unchanged.
- Arbitrary deterministic centers carry their index mu_n throughout the
  source necessity chain; no fixed-mean assumption is inserted.

All corrections are in the active formulas and proofs. The held source
PDF remains byte-for-byte unchanged. The constant X=-1 example computes
the endpoint correction explicitly, and the source's weak-law scope is
preserved for every real probability law, including atomic laws and laws
without finite expectations.

## Ten complete statement/proof pairs

Each suffix has body label thm:p15-<suffix> and reciprocal annex label
annex:p15.<suffix>.

| Suffix | Completed content |
| --- | --- |
| feller-symmetrization-structure | Median existence/nonuniqueness, reflection, product copies, convolution/CDF formula, symmetry and translation invariance. |
| feller-symmetrization-inequalities | Full V.(5.6)--(5.8), every parameter and the arbitrary-median radius specialization. |
| feller-largest-term-inequality | Measurable tie selection, separate sign invariance, the complete source largest-term proof and both exponential threshold variants. |
| feller-integration-by-parts | Full source partition proof, finite telescoping identity, both approximation errors and exact interval endpoints. |
| feller-tail-moment-equivalence | Closed/half-open identities, atom terms and both directions of all four vanishing conditions. |
| feller-truncation-inequality | Full clipping/union/Chebyshev bound and correct n normalization without original moments. |
| feller-generalized-weak-law | Both directions of VII.7 Theorem 1, its exact median chain and both canonical truncation centers. |
| feller-centering-corollaries | All admissible deterministic centers, finite-mean specialization and symmetric laws without a finite mean. |
| feller-symmetrization-examples | Exponential and uniform source examples, Bernoulli difference law, symmetric non-symmetrizable law and the endpoint atom calculation. |
| feller-proof-boundaries | Sharp constants, zero remainders, dependence/symmetry/median failures, threshold atoms, the normalization counterexample and a weak law with undefined expectation. |

## Integration, notation and exact next boundary

Use drafting scope P15.20. Body anchor:
sec:p15-feller-weak-law-presentation; annex anchor:
sec:annex-p15-feller-weak-law-presentation.
Existing prerequisites used are the complete CDF, finite-product,
generated-independence, integration and convolution results. In
particular the convolution law and density results in the actual
convolution-gamma-normal chapter supply the two continuous examples.

Notation intake: F(x), F(x-), F{dx}, reflected law -F, direct
symmetrization superscript circle on X,F,S; medians m and a as locally
declared scalar values; product probability Q; probability lower bound p
and radius a in V.(5.7); symmetric summands Y_i, sum S, tie index J,
largest signed term M and remainder R; common CDF G and strict/non-strict
tails q_>,q_>=; interval endpoints a,b, derivative bound M, mesh h,
partition x_j, increments Delta F_j,Delta u_j and sums A_N,B_N;
source tau(t), closed sigma(t), half-open sigma_h(t), means m(t),m_h(t),
absolute value W and strict normalized tail r(t); cutoff s, clipped
X_k', S_n', center m_n', canonical mu_n and arbitrary c_n; rate lambda
and difference density h. All scalar/function and interval/median role
changes are declared locally.

The whole saved authoring batch was read back. One truncated output span
was retrieved separately, and the small resulting edits were reread.
No independent reviews, scoped scanners, tests, builds or acceptance
checks were run.

There is no unresolved proof referral in the selected VII.7 Theorem 1
chain. Its separate alternative proof in XVII.2a remains future writing.
So do the positive-gain normalization Theorem 2 beginning on p. 236 and
continued on p. 237, and the optional Poisson/Bessel example V.(5.5).
Those are outside the referred median-chain component completed here.
