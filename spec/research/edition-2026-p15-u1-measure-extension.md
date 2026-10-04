# P15-U1: measure extension and distribution existence

Date: 7 September 2026 Pacific / 8 September UTC. Author:
`/root/probability_measure_author`. Fresh author block began at 04:19 UTC.
Scope: the next measure-existence prerequisites for P15-U1 / N-x-008.
Status: six theorem/proof pairs authored and completely read back;
independent review, integration, production and admission remain due.

## Saved manuscript and verified prerequisites

| Artifact | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p15/measure-extension.tex` | 368 lines, one chapter and four sections | `E1333244607DB51AE1EE5EC8FBF6AECA9AE8A2D85989677ED29ED9866119558E` |
| `handbook/annex/p15/measure-extension.tex` | 551 lines, six complete proof items | `D5179047198A9EDDE628274345D19DE75E30FC33CE065DAEC9F23F02DE83838F` |

The actual accepted prerequisite body and annex were rehashed before and
after this block and remain unchanged:

- `handbook/parts/p15/measurable-probability.tex`:
  `C249F33E0E0FC88084B05A7D44098DB87B3E4814083B34709D6DBE2B562340D9`.
- `handbook/annex/p15/measurable-probability.tex`:
  `FBB9E6C733A1F286F7E56FC31B7E76D4412D781E03711ED02D8D4B3AAEF8C8FC`.

Their current text acceptance and active routes were checked in
`edition-2026-bounded-kamp4-probability-decision-integration.md` and both
P15 wrappers. The present proofs use the earlier nonnegative regrouping,
Borel generators, measure continuity, pi-lambda theorem, pushforward law
and cumulative-distribution uniqueness. They do not use an existence
claim from that prerequisite chapter. Real order completeness is the
additional background for the supplied compact-interval covering argument.

## Exact held source and actual reading

The source remains Rick Durrett, *Probability: Theory and Examples*,
author **Version 5, 11 January 2019**, held at
`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`.
The local file was rehashed before and after work:
`AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886`.
It remains a 490-page PDF. The prior acquisition record gives 2,195,717
bytes and the original version/title-page evidence.
Primary locator: [Duke author PDF](https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf).
The Cambridge printed manifestation was not substituted. No source
download or source modification was needed in this block.

Fresh complete text reading from that saved PDF covered printed pages
1-6, 11 and 455-460, using `pypdf`. These are physical PDF pages
9-14, 19 and 463-468 respectively. The reading includes the measure and
semialgebra definitions, all of the one-dimensional Stieltjes argument,
Theorem 1.2.2 with its quantile proof, and the entire Appendix A.1.
Complete printed pages 5, 6, 11, 455, 456, 458, 459 and 460 were also
rendered from the saved PDF in memory and visually inspected with
`pypdfium2`. The multidimensional material beginning on p. 6 was read
where it shares the page, but is not part of the new theorem scope.
No manuscript PDF or source-page image files were created.

The PDF skill guided source reading; the research skill guided primary
tracing and this single note. The assignment's explicit no-subagent
instruction controlled the research skill's delegation instruction.
The source acquisition/version record is the preceding
`edition-2026-p15-u1-measurable-probability.md` note.

## Results and source relation

All result suffixes below carry body prefix `thm:p15-` and proof prefix
`annex:p15.`. Every stated component is included in the indicated proof.

| Suffix | Exact source foundation | Supplied proof |
| --- | --- | --- |
| `semialgebra-extension` | Definitions pp. 3-4; Lemmas 1.1.7 and 1.1.10; Theorem 1.1.9 p. 5; Theorem A.1.1 pp. 455-456 | Annex 12-87: generated algebra, representation independence, finite additivity and finite cover bound, both countable-additivity inequalities and unique premeasure representation. |
| `caratheodory-measurable` | Splitting criterion p. 458; Lemma A.1.7 and its remark, pp. 459-460 | Annex 89-162: complete algebra/sigma-algebra closure, finite splitting, countable additivity, all infinite-value cases, and null-subset completeness. |
| `premeasure-extension` | Theorem A.1.3 and its existence proof, pp. 456-460; Theorem A.1.5 pp. 457-458 | Annex 164-272: countable cover bound on an algebra, cover-infimum outer measure, agreement and splitting for original sets, extension without sigma-finiteness, and sigma-finite uniqueness via finite restrictions and pi-lambda. |
| `stieltjes-construction` | Theorem 1.1.4, p. 3; full one-dimensional proof pp. 5-6 | Annex 274-413: interval semialgebra and Borel generation; allowed infinite endpoints; finite partitions; compact-cover lemma from real completeness; clipping unbounded covering pieces; right-continuity enlargement; countable cover inequality; unbounded-target truncations; sigma-finite existence and uniqueness. |
| `lebesgue-unit-interval` | F(x)=x specialization, p. 3; the probability space used in Theorem 1.2.2 p. 11; uniform example p. 12 in the prior reading | Annex 415-468: construction and uniqueness of Borel length measure, singletons and endpoint variants, translation invariance, trace sigma-algebra, normalization and uniform cumulative function including t=0,1. |
| `cdf-existence` | Theorem 1.2.2, p. 11, using the fully constructed measure above | Annex 470-551: probability Stieltjes measure, quantile finiteness from both tails, monotonicity, both ray-equivalence directions, right-continuity guard, measurability, endpoint probabilities, law identity/uniqueness, minimum characterization, jump fibers and flat portions. |

This is independently worded mathematical exposition using the source's
semialgebra framework and its exact supremum quantile construction.
The term *premeasure* distinguishes the source's measure-on-an-algebra
from the chapter's measures on sigma-algebras. The semialgebra definition
makes inclusion of the empty set explicit, as required by the source's
assignment of zero to it. All value domains are explicitly nonnegative
extended reals.

The source's unbounded-cover reduction on p. 6 is expanded into an actual
clipping argument before using right continuity and a compact subcover.
The compact-interval finite-subcover fact itself is proved. Infinite target
endpoints are then handled through interval increments and endpoint limits,
before a measure exists; measure continuity is not used circularly there.
The generic extension proof handles finite and infinite outer values
separately, and invokes finite subtraction only after restricting both
measures to a common finite-measure set.

The final display in the source's Lemma A.1.6 proof on p. 459 prints
`mu*(F^c intersect A)` where the required second split piece is
`mu*(F intersect A^c)`. The new proof uses `T setminus A` throughout
that split. It preserves the source's intended construction without
copying that incorrect complement placement.

The generalized inverse is named `Q_F`, avoiding an assertion that F
has an ordinary inverse. The jump-fiber inclusions distinguish the
potentially included lower endpoint `F(x-)`; they do not falsely identify
every fiber with `(F(x-), F(x)]`. The two-point example gives masses
1/3 at zero and 2/3 at two, with quantile value zero at u=1/3. The
right-discontinuous step example and the u=0,1 discussion verify the
continuity and domain boundaries. The non-sigma-finite interval assignment
has two explicit different Borel extensions: counting measure and the
measure assigning zero to countable sets and infinity to uncountable sets.
These supplementary deductions are proved here, not represented as
additional numbered source theorems.

## Bibliography, notation and root integration

The existing canonical key `DurrettPTEAuthor2019` was verified and reused.
No new bibliography entry is needed. All new notation is local to
`sec:p15-measure-extension`; root owns canonical symbol intake:

| First anchor | Roles |
| --- | --- |
| `def:p15-semialgebra-premeasure` | Omega; semialgebra S and generated algebra A(S); premeasure mu_0; elementary assignment m and algebra extension overline m; finite-measure cover E_n. |
| `def:p15-outer-measure` | Outer measure q on all subsets; splitting-domain M_q; arbitrary test set T and splitting set E; restriction notation. |
| `def:p15-cover-outer-measure` | Cover-induced mu*, covering sets A_n, extended infimum and sum; extension mu on sigma(A). |
| `def:p15-stieltjes-intervals` | I(a,b) with allowed extended endpoints, interval semialgebra S_R, real Stieltjes F, endpoint values F(-infinity)/F(infinity), interval assignment m_F and measure mu_F. |
| `thm:p15-lebesgue-unit-interval` | Borel length lambda, translated set B+t, trace space Omega_U/F_U, uniform measure blackboard U and identity variable U(u)=u. |
| `def:p15-quantile-map` | Probability cumulative F, quantile Q_F, u in (0,1), left limit F(x-), strict sublevel set L_u in the proof. |
| Proof-local collections | L_n for the finite-restriction equality class; H_n for its finite-measure exhaustion; J_i/K_n for interval clipping/truncation; delta and eta_i for endpoint adjustments. |

Root should input `parts/p15/measure-extension` after the accepted measurable
chapter and `annex/p15/measure-extension` after its proofs. The new chapter
label is `sec:p15-measure-extension`. No drivers, style, bibliography,
symbol rows or acceptance records were edited by this author.

Author read-back covered both complete saved files and all subsequent
small precision edits. All six promised proofs are supplied. No manuscript
test, build, rendering, subagent review or admission was performed.
The next substantive unit is integration on the now constructed measures:
simple-function integrals, nonnegative integration and monotone convergence,
then signed integrability, Fatou and dominated convergence. Density
representations and general conditional expectation require that foundation.
Multidimensional Stieltjes measures and product measures remain their own
theorems. The broader P15-U1 / N-x-008 obligation remains open.
