# P15.21 author return: weak normalization with infinite means

Date: 8 September 2026. Scope: the three assigned new files only.
This is an author/source handoff for root integration. All manuscript
writing and corrections precede consolidated reviews.

## Files and complete mathematical scope

- handbook/parts/p15/infinite-mean-weak-normalization.tex
- handbook/annex/p15/infinite-mean-weak-normalization.tex
- This note.

Ten reciprocal complete statement/proof pairs are saved. Every result
has prefix thm:p15- and every annex uses annex:p15. followed by the
same suffix:

| Suffix | Complete content |
| --- | --- |
| positive-truncation-tools | Tail identities by both the source Stieltjes route and Tonelli; deletion error, truncated variance and limits. |
| relative-normalizer-properties | Bernoulli lower bound for linear growth; adjacent-ratio limit without monotonicity; uniqueness and replacement of scales. |
| positive-normalizer-construction | Positive lower anchor, nonempty crossing set, right continuity and no downward jumps, exact equation and nondecreasing normalizers. |
| positive-tail-equivalences | Both directions of slow variation and the strict/closed truncation equivalence, including atom bounds. |
| feller-positive-weak-normalization | Feller VII.7 Theorem 2: the source sufficiency and positive-summand necessity, including every real threshold and arbitrary normalizer signs. |
| positive-normalized-centers | All valid normalizers, both truncated centers and tails at those scales, finite/infinite mean growth. |
| positive-normalization-boundaries | Constant, two-point, critical continuous tail and Pareto laws; failures of independence and the all-zero boundary. |
| cauchy-weak-law-failure | Durrett's tail obstruction, density normalization, infinite absolute moment and direct convolution proof of the exact average law. |
| petersburg-array-calculation | Every cutoff condition, both endpoint tails, exact moments, full array application and an explicit integer choice. |
| petersburg-normalizers-and-prices | Separate Feller criterion route, exact implicit normalizers, numerical example, fee scales and the n-scale obstruction. |

Root owns shared routes, notation, bibliography and prior boundary
updates. No shared file was edited.

## Frozen primary presentations and reading

Feller file:
source/references/feller-probability-volume2-second-edition/feller-volume2-second-edition.pdf.
SHA-256:
CB87C933D4175234F5F5958A74F3A466ECF13C29BE4E0DFEDF9C9B739F717486.
The existing key Feller1971ProbabilityII was personally read and reused.
The scan title identifies Volume II, second edition; its Mei Ya printing
is undated. The bibliographic second-edition year 1971 is established
by the prior acquisition and publisher record; no printing year is
inferred from the scan. Unchanged download provenance:
[Zenodo](https://zenodo.org/records/7108309); edition record:
[Wiley](https://www.wiley-vch.de/de/fachgebiete/mathematik-und-statistik/an-introduction-to-probability-theory-and-its-applications-volume-2-978-0-471-25709-7).

Read the complete VII.7 Theorem 2 statement, footnote 12 and both proof
parts on printed pp. 236–237, physical pp. 251–252. Both whole source
page images were read, including formulas missing in OCR. The manuscript
retains the complete content of VII.(7.10)–(7.15). The median chain above
the theorem belongs to the completed preceding presentation; it is not
an unstated premise of this positive-summand proof.

Read the full VIII.9 Theorem 2 referral: definitions on printed p. 282,
entire theorem and proof pp. 283–284, physical pp. 297–299. Both
theorem/proof page images were read. The surrounding VIII.9 definitions,
lemma and Theorem 1/proof on pp. 279–282 were also read to identify
the exact generality. Printed p. 278 was navigational context.
Only the needed specialization zeta = 1, eta = 0, limiting ratio zero
is claimed here. Its direct forward and complete dyadic converse
proofs are supplied. The general moment-order theorem is separately
owed. Its premise U_zeta(infinity) = infinity excludes finite mean;
the needed finite-mean equivalence is independently covered here.

The complete VII.7 truncation lemma and V.6 integration-by-parts
premise were read in the immediately preceding Feller author block.
Their actual body statements and complete proof LaTeX were reread
for this continuation. The earlier n-fold variance correction is
preserved.

Durrett file:
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
Exact presentation: author Version 5, 11 January 2019.
Existing key DurrettPTEAuthor2019.
Read complete Examples 2.2.15–2.2.16 on printed pp. 65–66,
physical pp. 73–74, including the final pricing paragraph, and both
whole primary page images.
Theorem 2.2.11, pp. 62–63, and the complete weak-tail criterion
chain pp. 63–64 were read in the preceding weak-law block and
reread for this continuation. Their actual complete body/proof
LaTeX was read. The direct convolution supplies the exact average
law mentioned in Example 2.2.15; it does not claim to supply the
separate source route in Exercise 3.3.6.

## Direct corrections and supplements

1. Feller's unanchored infimum over all positive s with
   n mu(s)/s <= 1 can be zero: X = c has mu(s) = 0 below c.
   The manuscript fixes s0 with mu(s0) > 0 and begins the crossing
   after n mu(s0)/s0 > 1. It proves the exact equation from right
   continuity and the absence of downward jumps.
2. Feller's final interpolation omits a proof of the adjacent-ratio
   bound; its displayed rho bound also drops the rho symbol before
   (2 a_n). The manuscript proves a_(n+1)/a_n -> 1 and uses the
   correct reciprocal delta bound at a first-crossing index.
   Arbitrary normalizers need not be monotone.
3. The exact strictly positive source domain is identified. The
   extension X >= 0 with P(X > 0) > 0 is proved explicitly, and
   the all-zero law is excluded. Any nonzero real normalizer giving
   relative limit one is eventually positive.
4. Atom terms are retained in every strict/closed comparison.
   The canonical exact construction uses the right-continuous
   closed truncated mean; strict means are proved asymptotically
   equivalent without asserting the same exact crossing equation.
5. Durrett's non-strict tail is retained as a valid upper bound for
   deletion beyond a closed cutoff; both tails are calculated
   exactly. The integer choice floor(log_2(n log_2 n)) satisfies
   every simultaneous cutoff condition in the source.
6. At n = 1024, the leading per-play scale 10 is distinguished from
   the chosen truncated center per play 13. The 40-unit benchmark
   and exact 2^40 trial count are retained as scale calculations,
   with no asserted finite-sample break-even probability or finite
   expectation. The historical quotation is not copied.
7. The Cauchy rational identity is integrated on [-R,R] before
   limits. No separate absolute integrability of the odd summands
   is assumed. Equality of densities is almost everywhere, which
   covers the single exceptional point for equal scales.

## Route and notation intake

Drafting scope P15.21. Body root:
sec:p15-infinite-mean-weak-normalization.
Annex root: sec:annex-p15-infinite-mean-weak-normalization.
Suggested import uses the saved filenames after the Feller median
presentation; root chooses final physical order.

At def:p15-positive-gain-normalization: X, X_k, F, S_n;
strict tail q(s); closed truncated mean mu(s); second moment v(s);
strict mean mu_<(s); closed tail q_ge(s); reciprocal ratios
delta(s), rho(s); normalizer a_n; positive anchor s0.
All roles are local to this positive-gain domain.
At thm:p15-positive-normalizer-construction: N0, s_n and anchored
infimum. At def:p15-positive-slow-variation: L and dilation c > 0.
At def:p15-cauchy-petersburg-laws the examples reset the common
law and S_n; Cauchy scales a,b > 0 and f_a are locally distinct.
At thm:p15-petersburg-array-calculation: K(n), integer m(n),
cutoff b_n, deletion overline X_(n,k), center a_n = n m(n).
At thm:p15-petersburg-normalizers-and-prices: ell(s).
Base-two logarithms are explicit; continuous Pareto formulas use
natural logarithms. No new macro or bibliography key is needed.

Actual prerequisites: product independence and disjoint groups;
bounded/dominated/monotone convergence; Tonelli and expectation
bounds; Feller Stieltjes integration by parts; variance addition;
thm:p15-triangular-array-weak-law; thm:p15-iid-weak-tail-criterion;
and the affine-density and independent-density convolution theorems.

## Authoring extent and continuation

One complete author read-back of the two-file batch was performed,
with direct revisions for the explicit law-domain reset, the source
integration-by-parts route and eventual positivity of any nonzero
real normalizer. No review, review wait, scanner, test, build,
manuscript render or acceptance procedure was run.

Separately owed: full Feller VIII.9 general regular variation and its
source proof; XVII.2a's alternate argument; the earlier Poisson/Bessel
example; Durrett's full weak-convergence, characteristic-function and
CLT presentations. This return does not complete those components.

The research skill directed this single repo note and exact primary
attribution. The PDF skill was used to read source equations and
page boundaries; no manuscript PDF was produced or inspected.
