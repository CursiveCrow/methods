# P15.14: the two integrable strong-law proofs

Written 8 September 2026 in the author block beginning 11:53 UTC,
with return due by 12:38 UTC. The two assigned LaTeX files are saved,
and this note supplies source and notation intake for root integration.
All three paths were unused at dispatch. Only these assigned files were
edited; root retains ownership of shared routes, bibliography and symbols.
Independent reviews remain deferred under the current writing-first
instruction.

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p15/strong-laws-of-large-numbers.tex` | 305 | 13679 | `FF74422B72E9610D2153CC6319AE99D0F9285A09F3D6F159A30782CCD1AA6DDB` |
| `handbook/annex/p15/strong-laws-of-large-numbers.tex` | 551 | 23959 | `ACF700405F83D58521E4F18F7E51A7227BAC6D92ACB00C027CD6C8857BCB10DB` |

## Frozen presentation and complete source reading

Durrett, *Probability: Theory and Examples*, author Version 5 dated
11 January 2019, held at
`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`.
SHA-256:
`AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886`.
Reuse `DurrettPTEAuthor2019`; no new source key is needed.

Before writing, the selected presentation was fixed as the entire
pairwise-independent Theorem 2.4.1, including Lemmas 2.4.2--2.4.4 and
its continued geometric-subsequence/interpolation argument; Kronecker's
Theorem 2.5.9; and the distinct i.i.d. strong-law proof, Theorem 2.5.10.
Complete printed pages 76--78 and 85--87, physical pages 84--86 and
93--95, were read as text and source page images. The source images are
in the task workspace's `tmp/pdfs/p15-strong-law-source/` directory.
Printed pages 75, 79--80 and 88--90 were additionally read as text to
identify applications and next boundaries; their whole content is not
claimed authored here.

The source's references to the earlier truncation steps in Theorem 2.5.10
are resolved to the complete probability bound in Lemma 2.4.2 and the
complete variance bound and numerical estimate in Lemmas 2.4.3--2.4.4.
The needed first and second tail-integral formulas are supplied explicitly,
using the already written layer-cake and Tonelli results. All sum/integral
interchanges have nonnegative measurable integrands on sigma-finite factors.

The earlier theorem retains **pairwise** independence and the later route
retains **mutual** independence. They have separate statement/proof pairs.
The later proof invokes independent random-series convergence, not the
earlier strong law. The common-law truncation estimates themselves are
proved without any independence assumption.

## Eleven complete statement/proof pairs

Each suffix has body label `thm:p15-<suffix>` and reciprocal annex label
`annex:p15.<suffix>`.

| Suffix | Completed proof content |
| --- | --- |
| `cesaro-average` | Finite-head/small-tail estimate for numerical averages. |
| `strong-law-tail-bounds` | First and second tail integrals, the integer tail-probability bound, and both y-ranges of the reciprocal-square estimate. |
| `strong-law-truncation` | Exact moving deletion cutoff, first Borel--Cantelli, a finite random bound on changed sums, full scaled-variance series, common-law dominated convergence and averaged means. |
| `geometric-subsequence` | Floor and ratio limits, complete geometric tail bound, pairwise variance addition, Chebyshev, both counting sums and a countable family of deviation thresholds. |
| `etemadi-strong-law` | Complete nonnegative proof, repeated-index handling, interpolation, countable ratios approaching one, finite modifications and positive/negative-part reduction. |
| `kronecker-lemma` | Every summation-by-parts reindexing, normalized nonnegative weights, vanishing finite-head weight, a bound valid when all errors vanish, and the finite-prefix extension. |
| `weighted-independent-strong-law` | Centered scaled independent series, variance summability and pointwise Kronecker, including the nonidentical mean-average consequence. |
| `iid-series-strong-law` | Complete source Theorem 2.5.10 route with its actual truncation prerequisites and the final three limits. |
| `strong-law-applications` | Integrable measurable observations, countable simultaneous limits, fixed-event frequencies, uniform-square mean 1/3, and normalized density (3/2)x^(-5/2) with mean 3 and infinite second moment. |
| `pairwise-block-example` | Full independent-sign construction and pairwise joint laws for blocks (U,V,UV), triple failure of mutual independence and the resulting average-zero strong law. |
| `strong-law-counterexamples` | Shared-sign dependence, independent nonidentical rare jumps despite uniformly bounded first absolute moments, a positive infinite-mean dyadic law, nonmonotone divergent Kronecker weights and nondivergent weights. |

Kronecker's source condition is made explicit through positive finite
nondecreasing weights tending to infinity, followed by a proved extension
to any nonzero weights that are positive and nondecreasing eventually.
Repeated weights are allowed, and the auxiliary value a_0=0 is never a
denominator. This also covers finite initial nonpositive weights wherever
the original weighted series is defined. The source's auxiliary error-bound
argument is written without division by a bound that might be zero.

## Dependencies, routes and symbols

The main prerequisites are the existing measurable-limit and integral
theorems, layer cake, Tonelli, Chebyshev, pairwise variance addition,
measurable preservation of independence, both Borel--Cantelli lemmas,
countable independent-sequence construction and the new random-series
variance-summability theorem. The random-series dependency was checked at
body SHA `9E0C548249191087AB7F68F10868745C6C77AD0CD63ECBEBF6FA1C1D0780D107`
and annex SHA `831ED99DBD3929DEDDB5371311E3708686FC0F3F03C2E702FECD36480D27D509`.
No conditional-expectation, central-limit or infinite-mean strong-law
theorem is used to establish either integrable strong law.

Root reserved notation scope **P15.14**, after independent random series
P15.13. Body root: `sec:p15-strong-laws-of-large-numbers`; annex root:
`sec:annex-p15-strong-laws-of-large-numbers`.

Notation intake: samples `X_n`, sums `S_n,S_0`, averages `\overline X_n`,
common mean `\mu`; deletion variables `Y_k` and sums `T_n,T_0`, finite
modification bound `R`; nonnegative variable `W`, tail levels `t,y`,
numerical averages `u_k,u`; geometric ratio `\alpha`, indices
`k(j)=\lfloor\alpha^j\rfloor`, first index `j_0`, probability-one events
`E_\alpha,E`, countable ratios `\alpha_\ell=1+1/\ell`; positive/negative
parts `X_n^+,X_n^-`; weights `a_n,a_0`, numerical summands `x_n`, weighted
partial sums `b_n,b_0` and limit `b`, normalized weights `q_{n,m}`, finite
head error `H_M`, shifted sequences `\widetilde a_j,\widetilde x_j`;
nonidentical means `\mu_n` and centered/scaled variables `Z_n`; common
law `\nu`, observation `g`, Borel event `B`; uniform variables `U_k`,
density `f`, fair signs `U_j,V_j,\varepsilon`, rare-jump events `A_n`,
clipping `X_n\wedge2^r`, and harmonic sums `H_j`. The roles of `U`, `H`
and `Z` are locally redeclared in their separate proofs and examples.

## Authoring checks and exact next writing

The complete saved body and annex were read from the actual LaTeX, and
the subsequent notation and reference corrections were reread. The
existing scoped scanner reports eleven reciprocal pairs, no findings,
no missing references and no duplicated new labels. The cited source key
resolves. No independent review, manuscript build/render or new test ran.

Next general infinite-mean treatment: Theorem 2.4.5, with infinite positive
part and finite negative part, and its corresponding negative case. The
dyadic positive example proves only its stated special case. Next source
applications: complete renewal Theorem 2.4.7, uniform empirical-distribution
Theorem 2.4.9 and finite-alphabet information application 2.4.10. The fixed
event/countable-observation consequence here is not a uniform empirical law.

Next random-series component: the finite-variance rate 2.5.11 and the full
Marcinkiewicz--Zygmund rate 2.5.12, pp. 87--88, followed by Feller's
infinite-mean normalization theorem 2.5.13, pp. 89--90. Their precise
normalizations, endpoint conventions and proofs remain separate writing.
