# P15.36 — Reflection, ballot counts and arcsine laws

## Frozen source scope and completed writing

The target is the complete Durrett Section 4.9, beginning on printed
p. 262 and ending on p. 267. Printed p. 268 is blank apart from the
running heading; Chapter 5 starts on p. 269. The numbered content is
Theorems/Lemmas 4.9.1–4.9.6 and the single Exercise 4.9.1.
There are no further exercises on the blank following page.

All six numbered results and both parts of the exercise are supplied.
The chapter also proves the exact return-time limit asserted in the
source's discussion after equation (4.9.2), including a normalized
positive half-stable density and its transform. Ten reciprocal
statement/proof pairs are saved.

Owned files:

- handbook/parts/p15/reflection-and-ballot-counts.tex
- handbook/annex/p15/reflection-and-ballot-counts.tex
- spec/research/edition-2026-p15-reflection-and-ballot-counts.md

Chapter label: sec:p15-reflection-and-ballot-counts.
Annex label: sec:annex-p15-reflection-and-ballot-counts.
Root owns shared routing, bibliography, symbols and older boundaries.
The frozen normal-domain and optional-stopping pairs were not edited.

## Exact primary source and reading

Rick Durrett, Probability: Theory and Examples, author Version 5
dated 2019-01-11.

Held original:
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf

SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886

Bibliography key: DurrettPTEAuthor2019.
No new bibliography entry or source acquisition is required.
The original was not changed.

The complete Section 4.9 was read before authoring, including every
continued proof, the return-time discussion, both arcsine arguments,
the single exercise, and the actual section ending.
Complete source page images for printed pp. 263–268 (physical pp.
271–276, one-based) were personally read. These include Figure 4.5,
all the reflected/ballot count formulas, the malformed step-density
index, the occupation induction, the exercise, and the blank page.

The actual source Example 3.8.5, printed p. 190, was read to resolve
the source's return-time and level-hit terminology. Theorems 3.8.8
and 3.8.9 with the latter's continuation on pp. 191–192 were read
to identify the actual stable-limit referral. They do not constitute
the tail-domain theorem invoked by the prose following (4.9.2).
The source's stable-domain theorem is the separate Section 3.8
Theorem 3.8.2; its actual statement on printed p. 186 was located
and read to confirm the referral. Its general Poisson-process proof
was not imported, and no unproved version of it is used here.

The source's forward Brownian references point to its later
first-passage and invariance-principle developments. Their existence
was located, but their full proofs were not imported into this chapter.
The direct density/limit proved here does not claim completion of
those later presentations.

Actual prior manuscript material consulted included:

- de-moivre-laplace-and-stirling.tex for the complete factorial/local
  binomial premise and its exact conventions.
- exchangeability-and-definetti.tex to preserve the distinction from
  the source's separate reverse-martingale ballot identity.
- characteristic-function-criteria-and-moments.tex for the complete
  compact moment determinacy and method-of-moments interfaces.
- The completed optional-stopping restart result
  thm:p15-os-independent-restart, used only for independence of
  successive passage durations.

Root reported the new P15.34 Feller compact-moment and positive-series
results as another available route. This author batch retains the
already supplied P15.27 compact-moment dependency and does not
silently substitute the separate Feller presentation.

## Reciprocal result inventory

Each suffix has body label thm:p15-SUFFIX and proof label
annex:p15.SUFFIX.

| Suffix | Complete result and source mapping |
| --- | --- |
| rb-reflection | Path count, parity, first-zero bijection and its inverse; source 4.9.1. |
| rb-ballot | Source 4.9.2 strict ballot count, plus separately proved weak boundary and empty-word conventions. |
| rb-return-counts | Source 4.9.3, the telescoping no-return count, first-return masses, the independent T_1 identification, asymptotics and moment threshold. |
| rb-renewal | Both parts of Exercise 4.9.1, with a complete measurable-state Markov-kernel premise, positive returns, complex disk and endpoint cases. |
| rb-last-zero | Source 4.9.4, fixed-time last-zero decomposition and exact finite normalization. |
| rb-arcsine-limit | Source 4.9.5, rounded step-density proof, integral/CDF calculation and full endpoint control. |
| rb-occupation | Source 4.9.6, edge-count parity, separate endpoint argument and full first-excursion induction. |
| rb-laplace-premise | Normalized half-stable density, its complete Laplace integral, uniqueness and convergence criterion, and exact sum scaling. |
| rb-return-scaling | Exact R_m =d m+T_m identity and both square-scale limits with their constant. |
| rb-calculations | Worked counts, finite moments, mass-shape calculation, arcsine probabilities and countermodels for omitted assumptions. |

## Distinct source routes preserved

Reflection is an explicit path involution: it reflects precisely the
prefix through the first zero and preserves that first-zero time.
The inverse has the correct starting point. The proof includes
unreachable endpoints, parity, length zero and zero-count cases.

The strict ballot theorem is proved by subtracting the reflected
bad-path count from the first-up-step count. It is not replaced by
the earlier reverse-martingale ballot theorem. A separate height
shift proves the weak ballot formula. Binomial zero conventions
handle boundary vote counts without factorials of negative integers.

The no-return identity is proved by the source's finite telescoping
sum over strictly positive endpoints and whole-path reflection.
Return masses and the one-level hitting masses then come from
tail differences and fixed-time independence. The earlier
optional-stopping generating function is not used to replace this
combinatorial calculation.

The first arcsine law uses the last-zero decomposition and the
source's step-density/Riemann integral. The proof establishes uniform
local approximation only on compact subintervals of (0,1), then
controls the endpoint probabilities through normalization. It does
not apply a uniform density approximation at singular endpoints.

The second arcsine law has its own first-excursion induction.
The all-positive/all-negative cases are established separately;
the induction then uses the renewal equation for the interior.
The count is of positive-side edges, including 0-to-1 and 1-to-0,
and its even parity is proved before the induction.

The return-time limit is proved directly from the combinatorially
derived return generating function. A Gaussian substitution normalizes
the limiting density; a differentiated integral with an explicit
integrable derivative majorant proves its Laplace transform
exp(-sqrt(2 lambda)). Laplace uniqueness/convergence is proved by
mapping to U=exp(-Z), applying the existing compact moment results,
and returning through CDF thresholds. No logarithm continuity at zero
is assumed. The exact stability relation is proved by transform
multiplication and uniqueness.

## Corrections and precise interpretation boundaries

The reflection inverse on source p. 263 starts at +x, not the
repeated -x printed in the inverse paragraph. The manuscript
defines both maps explicitly.

The source step density on p. 266 must use
n P(L_(2n)=2k) on [k/n,(k+1)/n), not n P(L_(2n)=k).
The manuscript uses the corrected mass, a_n=ceil(na)/n,
b_n=floor(nb)/n and the exact upper integration endpoint b_n+1/n.

The source's reference to Theorem 3.8.8 after the tail estimate
does not supply a stable tail-domain theorem: that result concerns
which laws can occur as i.i.d. limits. The current chapter proves
the needed particular limit directly and retains the full general
stable-domain presentation separately.

Return times and positive level-hit times are not identical finite laws.
The source Example 3.8.5 conflates the sum of one-level passage times
with the time of the corresponding return to zero. The manuscript
proves R =d 1+T_1 and R_m =d m+T_m. Both normalized by m squared
have the same limit, with Laplace transform exp(-sqrt(2 lambda)).

The general renewal exercise needs a regenerative premise. It is
supplied for a given time-homogeneous Markov chain on a measurable
space with measurable singleton {a}, including the countable-state
case. The proof derives the multi-step conditional return probability
from the kernel and tower identities. It does not assume a strong
Markov theorem or a countable-state construction that has not been
written. An explicit deterministic nonhomogeneous process shows
why the renewal identity is false for an arbitrary process.

The exercise's T_a must mean a first positive return, not the
initial hit at time zero. The manuscript uses tau_a^+ and gives
the one-state chain as an explicit counterexample to the wrong
convention.

Equal laws of L_(2n) and the positive-edge count do not mean
pathwise equality. The count of positive sampled vertices is also
a different quantity. Concrete four-step paths separate all three
interpretations.

The source's gambling interpretation is stated as a limit over
even horizons. No exact calendar-year probability is inferred.
The limiting arcsine law has no point masses at the endpoints,
even though its density diverges there. The finite distribution's
largest masses are at the endpoints and its smallest at the one or
two central admissible indices, with the parity qualification explicit.

## Worked results

- Length-four paths from 1 to 1: six total, four touching zero, two positive.
- Three A votes and two B votes: two strict-lead words and five weak-lead
  words out of ten, all listed in the annex.
- Four-step last-zero/occupation masses: 3/8, 1/4, 3/8 at 0,2,4.
- For K=L_(2n)/2 or A_(2n)/2:
  E K=n/2 and Var(K)=n(n+1)/8, proved by differentiated generating series.
- Limiting arcsine mass in [1/4,3/4]: 1/3; the outer quarters: 2/3.
- The finite biased reflection example has probabilities qp and p squared,
  demonstrating that the count bijection is not generally weight-preserving.

## Notation intake for P15.36

- Integer path coordinates s_j, reflected s'_j, first-zero K; endpoints x,y;
  n in N_0; path count N_(n,z), zero-binomial convention and fair mass p_(n,z).
- Fair walk S_n, increments xi_j, u_n; level hitting T_j; positive return R;
  successive return times R_m and return masses f_(2n).
- Vote counts alpha,beta, word length n, endpoint lead h and letters A,B.
- Measurable state space (E,Ecal), measurable singleton {a}, kernel P,
  laws P_a, Markov process X_n, sigma-algebras F_m, return tau_a^+,
  general f_n,v_n and kernel iteration h_r.
- General generating series V(s),F(s); fair return series F(s) with
  its explicitly stated local specialization.
- Last-zero L_(2n), occupation A_(2n) corresponding to source pi_(2n);
  occupation probabilities beta_(k,n).
- Arcsine density h, CDF H, rounded a_n,b_n, step function h_n,
  cutoff delta, substitution variables y,theta.
- Half-stable density g, variable Y, Laplace parameter lambda,
  Gaussian integral J(a), derivative domination constant c,
  transformed compact variables U_n,U and original nonnegative Z_n.
- Passage-copy notation R^(j),T_1^(j), small quantity b_m, scale m squared.
- Finite mass weights w_j and generating function W(z), count K,
  radius 0<r<1 in the power-series justification.
- Biased up-step p and down-step q=1-p in the boundary example only.

## Author completion and next source work

All ten proof groups and the full source exercise are saved.
One complete author read-back of the actual body and annex was
performed, followed by direct definition and endpoint corrections.
There is no unwritten numbered Section 4.9 result or exercise.

Root can route P15.36 and update P15.35's prior combinatorial
boundary. The general stable-law source proof and Brownian
first-passage/invariance-principle interpretation remain separate.
The broader original Gnedenko–Kolmogorov general-array chain,
Kesten–Stigum and other historical-source obligations keep their
existing separate standing.

The research and PDF skills guided primary reading and provenance.
No independent reviews, scanners, tests, builds or manuscript renders
were run. The generated images were solely primary-source page reads.
