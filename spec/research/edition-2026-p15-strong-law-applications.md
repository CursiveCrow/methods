# P15.15: extended means, renewal, empirical distributions and information

Written 8 September 2026 in the assigned 45-minute author block.
The first tool clock checkpoint was 12:17 UTC; the mathematical body
and annex were complete before 12:35 UTC. Only the three assigned new
files were authored. Their paths were unused at dispatch. Root owns
shared routes, bibliography, notation and progress integration.
Independent reviews remain deferred under the user's current instruction.

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| handbook/parts/p15/strong-law-applications.tex | 349 | 15787 | 98281F5718F019C1BBC8AE22688347F22E93762B9A3AA2E4DCBFD2EA04947C51 |
| handbook/annex/p15/strong-law-applications.tex | 546 | 25596 | FF5646A3BC68634EF199E806B080852C23BD55035F4C5441252DA294E4C8391B |

## Exact source and complete reading

Durrett, Probability: Theory and Examples, author Version 5 dated
11 January 2019, held at
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
Verified SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
Reuse bibliography key DurrettPTEAuthor2019; no new key is required.

The exact selected extent was frozen before writing: Theorem 2.4.5;
renewal Example 2.4.6 and the complete continued Theorem 2.4.7;
the random-index observation and its full Bernoulli counterexample
family; empirical-distribution Example 2.4.8 and the full quantile-grid
proof of Theorem 2.4.9; and finite-alphabet information Example 2.4.10.
Complete printed pages 78--80, physical pages 86--88, were personally
read as text and source page images. The source images are under the
task workspace's tmp/pdfs/p15-strong-law-applications-source/ directory.

The source's extended-mean clipping argument, renewal inverse inequality,
random-index reasoning, CDF values and left-limit grid argument, and
information-sum argument are all retained. Their integrable-law dependency
uses the already written Etemadi theorem, matching the source's use of
Theorem 2.4.1. All actual source theorem premises remain visible.

## Explicit extensions and corrections

The source renewal regime is strictly positive finite waiting times.
The new statement also permits zero waiting times, provided the probability
of a positive wait is nonzero. Its proof establishes positive extended
mean, escape of epochs to infinity, finiteness of every finite-time count,
and the last tied index. N(t) includes index zero, handles initial times
with no renewals, and is divided by only when it is positive. The all-zero
law is treated separately. Both finite and infinite positive means are
proved on one event valid for all real times tending to infinity.

The source's broad monotone-function observation needs tail qualifications
on the real line. The active deterministic lemma is stated for CDFs with a
continuous CDF limit, and proved. The moving point-mass example G_n(x)=1(x>=n)
shows why a merely bounded continuous pointwise limit is insufficient.
The general empirical theorem retains jumps: interior quantiles are proved
finite, repeated points create empty intervals, actual grid-point errors
are included, and both inequalities at left limits are supplied.
The supremum is proved equal to a rational supremum before it is used as
a random variable.

The source assumes strictly positive probabilities for every alphabet
symbol. The extension permits zero masses by using the positive support
and an everywhere real bounded information representative. It gives
the conventions -log(0)=infinity and 0 log(0)=0 their distinct roles.
Natural logarithms specify nats. Probability-one support holds for the
entire observed sequence. The entropy bound, variance calculation,
Chebyshev probability bound and both typical-set cardinality bounds,
including the lower bound for any high-probability word set, are proved
additions. The one-symbol support and empty finite typical sets are covered.

## Eleven complete statement/proof pairs

Each suffix below has body label thm:p15-<suffix> and reciprocal
annex label annex:p15.<suffix>.

| Suffix | Supplied content |
| --- | --- |
| extended-mean-strong-law | Full positive-infinite clipping proof, finite case, negative case and exact expectation domain. |
| random-index-limits | Measurability and pointwise finite/infinite limits; the full a_n->0, sum a_n=infinity Bernoulli family, with first-hit exceptions explicitly defined. |
| renewal-inverse-law | Positive mean, escape, finite last tied count, count measurability, common-event real-time inversion, infinite mean and all-zero degeneration. |
| empirical-cdf-structure | Empirical measure, right/left limits, rational supremum measurability, finite quantiles and endpoint/repetition inequalities. |
| continuous-cdf-uniform | Full deterministic finite-grid argument with CDF tail normalization. |
| glivenko-cantelli | Both indicator strong laws, countable common event, actual grid points, repetitions, tails and both full interpolation chains. |
| finite-alphabet-entropy | Joint mass normalization, support event, logarithm sum, bounded information, entropy and variance, including H<=log(m). |
| finite-alphabet-aep | Source information strong law and limiting typical probability with zero word masses handled. |
| typical-set-bounds | Finite Chebyshev probability bound, two size bounds and the lower size bound for any high-probability set. |
| strong-law-application-calculations | Zero/two and infinite-mean renewal laws, exact atomic-CDF error and repeated grid, biased three-symbol example, and uniform/one-symbol alphabets. |
| strong-law-application-boundaries | Undefined symmetric mean with no extended average limit, degenerate counts, dependence, escaping CDF mass, all-Borel-set uniformity failure and dependent product-information failure. |

## Root integration and notation

The reserved chapter scope is P15.15, after the integrable strong laws.
Use body anchor sec:p15-strong-law-applications-chapter and annex anchor
sec:annex-p15-strong-law-applications. The shorter body anchor without
-chapter already belongs to a section of the preceding strong-law chapter;
it was preserved and the new chapter's label was changed to avoid collision.

The preceding strong-law dependency was checked at body SHA
FF74422B72E9610D2153CC6319AE99D0F9285A09F3D6F159A30782CCD1AA6DDB
and annex SHA
ACF700405F83D58521E4F18F7E51A7227BAC6D92ACB00C027CD6C8857BCB10DB.
Other used prerequisites are signed integration, monotone/bounded
convergence, CDF laws and measure uniqueness, generated independence,
variance/Chebyshev, Borel--Cantelli, tail zero-one and countable products.

Notation intake: X^+,X^-, S_n, clipped X_i^[M],S_n^[M];
extended observations Z_n,Z, finite indices J_m and extended first hits K_m,
Bernoulli B_n with probabilities a_n and the infinitely-often event H;
epochs T_n,T_0, nonnegative-index set N_0, inverse N(t), mean mu, event Omega_0;
laws nu, empirical measures nu_n, CDF F,F_n and left limits, rational
supremum D_n, grid x_(j,k), deterministic G_n and N_k, random threshold n_k,
common event Omega_1; alphabet A, support A_+, size m, symbol probabilities p,
word w and random word W_n, mass pi_n, real information I_0, entropy H,
variance sigma_I^2, information average L_n, typical sets T_n(epsilon),
atypical probability eta_n, tolerance epsilon, failure budget delta and
candidate word set C. Also K_n for atom counts, E_+,E_- for infinite-limit
events, and B_n for an outcome-selected finite Borel set in the last
counterexample. The glyph bot denotes a third alphabet symbol in the
worked example, not a logical falsity constant. All these local roles are
declared where used; the note's plain-text names stand for the actual LaTeX.

## Authoring checks and next block

The saved body and annex were read completely, and subsequent corrections
were reread in the actual LaTeX. The existing scoped scanner reports eleven
reciprocal proof pairs, no findings, no missing references and no duplicated
new labels. The source key resolves. No independent review, manuscript
build/render, new test or acceptance report was run.

The exact next random-series block remains the finite-variance rate
Theorem 2.5.11, Marcinkiewicz--Zygmund Theorem 2.5.12 and Feller's
infinite-mean normalization Theorem 2.5.13, printed pp. 87--90.
The Section 2.4 renewal-reward and further exercises remain separate
applications. Root's martingale work keeps its reserved P15.16 scope.
