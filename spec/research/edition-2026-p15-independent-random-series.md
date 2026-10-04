# P15.13: independent random series

Written 8 September 2026 in the author block beginning 11:16 UTC,
with return due by 12:01 UTC. The assigned body and annex are saved.
Root owns shared routes, bibliography, notation and progress integration.
The three assigned paths were unused before authoring; no other manuscript
file was edited. Independent reviews remain deferred until the complete
change set is written, as instructed.

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p15/independent-random-series.tex` | 292 | 13218 | `9E0C548249191087AB7F68F10868745C6C77AD0CD63ECBEBF6FA1C1D0780D107` |
| `handbook/annex/p15/independent-random-series.tex` | 549 | 25253 | `831ED99DBD3929DEDDB5371311E3708686FC0F3F03C2E702FECD36480D27D509` |

## Exact source extent

Durrett, *Probability: Theory and Examples*, author Version 5 dated
11 January 2019, held at
`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`.
SHA-256 was verified as
`AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886`.
Reuse `DurrettPTEAuthor2019`; no new bibliography key is required.

The selected scope was fixed before writing: Theorems 2.5.5--2.5.6,
**Example** 2.5.7, and the complete three-series Theorem 2.5.8,
including the necessity argument deferred by the source to Example 3.4.12.
Complete printed pages 84--85 (physical 92--93) and 148--151
(physical 156--159) were read as text and primary-source page images.
This includes the complete statement/proof of Lindeberg--Feller 3.4.10
and the complete continued Example 3.4.12. Source page images are under
the task workspace's `tmp/pdfs/p15-independent-series-source/`.
Printed pages 86--89 were additionally read as text to identify the next
source component; those results are not claimed written here.

The source proves three-series sufficiency on p. 85, and defers necessity
to pp. 150--151, where it uses the later Lindeberg--Feller theorem.
This chapter supplies a complete independent elementary necessity proof
now. It also retains the full source route in a separate conditional
statement/proof pair, with the precise LF premise displayed in the body.
Its CDF perturbation step is proved directly; initial rows with zero
normalizing variance are explicitly defined. The only remaining theorem
premise of that alternate route is LF, not a hidden appeal to an exercise.
The proof of LF itself remains assigned to the later central-limit work.

## Ten complete statement/proof pairs

Every suffix below has body label `thm:p15-<suffix>` and reciprocal
annex label `annex:p15.<suffix>`.

| Suffix | Completed content |
| --- | --- |
| `series-event-calculus` | Countable Cauchy event, measurable tail oscillations, tail sigma-algebra membership, term-to-zero necessity, finite changes and zero-one consequence. |
| `kolmogorov-maximal` | Full first-crossing decomposition, independent past/future factors, integrable cross terms and variance addition. |
| `variance-series-convergence` | Finite and infinite maximal bounds, one common Cauchy event, measurable finite limit, plus proved mean-square convergence and exact tail second moments. |
| `bounded-fourth-moment` | Fourth-moment expansion and lower probability bound; the resulting complete centered bounded converse. |
| `series-independent-copy` | Actual finite product construction, combined-family independence, grouped differences, zero means, doubled variances, swap symmetry and copied convergence. |
| `bounded-series-criterion` | Both directions; necessity uses copied differences and the fourth-moment converse, followed by deterministic mean-series subtraction. |
| `three-series` | Both directions for every fixed positive deletion cutoff; exact strict/weak threshold conventions, no original moments assumed, cutoff independence and probability-zero failure. |
| `three-series-source-route` | Complete alternate source necessity argument conditional on the displayed LF assertion, including all triangular-array checks, CDF perturbation and deterministic-law contradiction. |
| `signed-power-series` | Complete source Example 2.5.7 classification for all real alpha, with the numerical dyadic-block power-series proof and absolute/conditional thresholds. |
| `series-boundary-examples` | Conditionally convergent means, separate failure of each three-series condition, unbounded summable-series/infinite-variance example, and explicit dependence/centering failures. |

The elementary necessity proof does not use a characteristic function,
central-limit theorem, conditional expectation, or an assumed infinite
product. Only a finite product of the already given probability space is
needed for the copied sequence. Independent discrete example sequences use
the existing countable-product construction.

## Dependencies and notation for root integration

Use the existing measure-continuity, measurable-limit, integration,
Cauchy--Schwarz, finite-product, generated-independence, variance-addition,
countable-product, Borel--Cantelli and tail-zero-one results. The alternate
LF route also uses the already normalized standard normal law. All new
references resolve against the actual P15 body/annex files.

Insert the two chapter inputs after their prerequisites in the planned
**P15.13** scope. Body root label:
`sec:p15-independent-random-series`; annex root label:
`sec:annex-p15-independent-random-series`.

Notation intake for P15.13: partial sums `S_n,S_0,S_\infty`, convergence
event `C_X`, oscillations `w_M`; crossing events `A_k` and future increments
`T_k`; finite variance sum `V`; bounded centered summands `U_j`, bound `M`,
sum `W`, block variance `v`, excursion event `D`, converse sums `T_n`
and oscillations `q_m`; copied variables `\widehat Y_n,\widetilde Y_n,Z_n`
and finite product `\Omega^2`; cutoff `A` and deletion variables
`Y_n^{(A)},p_n^{(A)},\mu_n^{(A)},v_n^{(A)}`; standard normal variable `G`
and CDF `\Phi`, named premise `\mathrm{LF}`, triangular array `U_{n,m}`,
limiting standard deviation `\sigma`, raw sums `R_n`, normalization
`c_n`, standardized sums `Z_n,V_n`, deterministic normalized drift `d_n`;
fair signs `\varepsilon_n,\varepsilon`, exponent `\alpha`, auxiliary
power exponent `p`, and alternating numerical partial sums `a_n`.
Every reused letter has its local role declared before use. In particular
`M` is a starting index in the convergence proof and a uniform bound in
the separate fourth-moment lemma; `Z_n` is a copied difference in one
lemma and a standardized row sum in the separate LF route.

## Authoring checks and next writing

The saved body and annex were read in full, and the subsequent definition,
index and source-page corrections were checked in the actual files. The
existing scanner reports ten reciprocal pairs, no scoped structural
findings, no missing references and no duplicate new labels. The existing
bibliography has the cited key. These are bounded authoring checks, not
independent mathematical or source reviews. No manuscript build/render,
new test or review task was run.

The next sequential source writing is Theorem 2.5.9 (Kronecker's lemma,
statement on p. 85, proof on p. 86) and Theorem 2.5.10 (the integrable
i.i.d. strong law, pp. 86--87), supplying the truncation estimates the
source imports from Theorem 2.4.1(a)--(b). Further rate results begin after
that. Separately, the precise later obligation that discharges the retained
source route is Durrett Theorem 3.4.10, including its characteristic-function
prerequisites, rather than just a special normal approximation claim.
