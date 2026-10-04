# P15.35 — Optional stopping and random walks

## Frozen target and completed scope

The complete target is Durrett's Section 4.8, printed pp. 255–262:
Theorems 4.8.1–4.8.9, Example 4.8.10, and Exercises 4.8.1–4.8.11.
The section ends immediately before Section 4.9 on printed p. 262.
All of this target is supplied in the new body and annex.
There are 20 reciprocal statement/proof pairs.

Owned files:

- handbook/parts/p15/optional-stopping-and-random-walks.tex
- handbook/annex/p15/optional-stopping-and-random-walks.tex
- spec/research/edition-2026-p15-optional-stopping-and-random-walks.md

Chapter label: sec:p15-optional-stopping-and-random-walks.
Annex label: sec:annex-p15-optional-stopping-and-random-walks.
Root owns shared drivers, bibliography, symbols, progress and changes to
older boundaries. The author's work did not alter those shared files.

## Primary source and reading extent

Rick Durrett, Probability: Theory and Examples, author Version 5
dated 2019-01-11.

Held original:
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf

SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886

Bibliography key: DurrettPTEAuthor2019. No new key or acquisition is needed.
The original PDF was not changed.

The entire exact Section 4.8 was read before writing, including every
continued proof and every exercise through 4.8.11. Complete source page
images for printed pp. 257–262 (physical pp. 265–270, one-based)
were then read to resolve the quadratic-martingale typo, the repeated
hitting event, the generating-function roots, and the exercise formulas.
The surrounding end of Section 4.7 and start of Section 4.9 were read
only to establish the boundary; neither was counted as new Section 4.8
content.

Actual manuscript prerequisites read included:

- martingales-and-convergence.tex: process definitions, martingale
  constructions, predictable stopping, stopped sigma-algebras, bounded
  conditional sampling, convergence, and boundary examples.
- The matching martingale annex: complete stopped-information and bounded
  conditional-sampling proofs.
- uniform-integrability-and-conditional-limits.tex: small-event/tail
  criteria, domination, Vitali convergence, and submartingale L1 limits.
- martingale-maximal-inequalities.tex: bounded stopping routes, finite
  maxima, the fair-walk endpoint, and orthogonality.
- predictable-quadratic-variation.tex: the existing stopping and
  square-integrability interfaces.
- The earlier probability foundations supply the complete binomial
  expansion, monotone and dominated convergence, product integration,
  independent sequences, and the finite/extended-mean strong laws.

The research and PDF skills guided the exact source freeze, full primary
reading, source-page formula reading, and this single durable note.
The only page images generated were images of the primary source.

## Reciprocal proof inventory and source mapping

Each suffix has body label thm:p15-SUFFIX and proof label
annex:p15.SUFFIX.

| Suffix | Complete scope |
| --- | --- |
| os-ui-stopped | 4.8.1 and 4.8.3: stopped positive-part argument, tail splitting, L1 limits and both expectation bounds. |
| os-residual-ui | 4.8.2: integrable terminal value and uniform residual-tail criterion, with the infinite-time limit specified. |
| os-conditional-sampling | Exercise 4.8.1: conditional and unconditional comparisons for unbounded or infinite L <= M. |
| os-nonnegative | 4.8.4 and Exercise 4.8.2: Fatou sampling, conditional version, strict and non-strict supremum bounds. |
| os-integrable-time | 4.8.5: the complete integrable total-variation majorant. |
| os-wald-first | 4.8.6: absolute integrability and first Wald identity, with the initial position retained. |
| os-wald-second | Exercises 4.8.3–4.8.4: stopped L2 convergence, second Wald identity and extended exit-time lower bound. |
| os-independent-restart | Full stopped future-increment independence needed by Exercises 4.8.5(b) and 4.8.6(c). |
| os-finite-exit | Independent block bound, finite exponential/time moments, and deterministic endpoint cases. |
| os-fair-exit | 4.8.7: both hitting probabilities, quadratic mean-time argument and almost-sure hitting of every integer. |
| os-fair-hitting | 4.8.8: exponential stopping, correct reciprocal root, full binomial inversion and infinite mean time. |
| os-biased-exit | 4.8.9(a)–(b) and 4.8.10: harmonic exponential, both exit probabilities, interval mean and roulette calculation. |
| os-drift-hitting | 4.8.9(c)–(d): one-sided hitting, integrable global minimum, and noncircular mean-time proof. |
| os-downward-variance | Exercise 4.8.5: stopped-square integrability, variance formula and the independent-sum explanation. |
| os-downward-pgf | Exercise 4.8.6: exponential identity, admissible root, endpoint cases, biased coefficient inversion and general-start convolution. |
| os-quartic-time | Exercise 4.8.7: b=3, c=2, justified stopped quartic limit, complete second moment and variance. |
| os-exponential-exit | Exercise 4.8.8: finite expected exit time, integrable unbounded exponential overshoot, exact identity and one-sided bound. |
| os-skip-free-ruin | Exercises 4.8.9–4.8.10: unique negative exponential root, infinite-time limit, exact ruin and the three-payoff calculation. |
| os-insurance | Exercise 4.8.11: full normal exponential integral, initial capital, independence and zero-variance case. |
| os-boundaries | Four fully specified counterexamples for missing UI, moment/increment control, or the stopping property. |

## Exact hypotheses and corrected formulas

Stopping values on a genuinely infinite stopping event are defined through
the stated terminal limit. The standalone residual-tail criterion
explicitly requires that limit on the infinite event. Conditional sampling
at L=infinity uses that M is then also infinity and that both values share
the same terminal limit. All integrability needed to condition is proved.
No completed-filtration assumption is introduced.

The conditional increment bound uses one deterministic finite B.
Integrability of T alone is insufficient for a general martingale:
the doubling example has mean stopping time two and violates the required
uniform conditional increment bound.

Wald's second identity allows independent, non-identically-distributed
centered increments with the same finite variance. The proof first
establishes orthogonality of stopped increments, applies Fatou to the
finite stopped sums, and obtains L2 convergence. Only then does it
pass to stopped-square expectations or apply the quadratic martingale.
The zero-variance identity is covered separately, and the positive-variance
exit-time ratio is never divided by zero.

The source quadratic martingale on printed p. 257 is corrected from
S_n - n sigma squared to S_n squared - n sigma squared.
The repeated fair-walk hitting event on p. 258 is corrected:
P_1(T_M<T_0)=1/M and P_1(T_0<T_M)=(M-1)/M.
The monotone time sequence is T wedge n, not the printed T wedge T.
The biased exit identity uses the proper complementary event, repairing
the printed occurrence of P(T_a<T_a).

In the fair generating-function proof, u=exp(theta)>1 is the plus
quadratic root. The probability generating function is u inverse,
the minus-root expression. This distinction is explicit.
The biased downward root is exp(theta) in (0,1) itself.
Both binomial inversions are supplied with power-series uniqueness.
General initial integer x is handled by the proved independent restart
property, not by an assumed strong Markov theorem.

Interval endpoints and starting positions are integers for the
nearest-neighbor endpoint-hitting formulas. The positive integer width
gives a geometric block bound, which proves every needed time moment
before the quartic stopped identity is passed to its limit.
The source's upward drift mean uses the integrable global minimum;
the proof does not assume the unknown mean hitting time.

For downward ruin, the centered stopped sum equals -x+(q-p)V_0.
Its L2 integrability from Wald's second identity proves V_0 squared
integrable before its square is expanded. The exact variance is
4pq x/(q-p)^3. Degenerate p=0 and initial x=0 cases have deterministic
times and zero variance.

For the general exponential exit result, stopped positions can overshoot.
The manuscript proves exponential overshoot integrability by summing
over the exit time and conditioning one step earlier. The pre-exit
exponential residual is bounded, so the actual hypotheses of the
residual-tail theorem hold. The proof does not claim bounded terminal
overshoots for a general increment law.

For the skip-free downward model, existence and uniqueness of a negative
exponential root are proved. On the infinite nonruin event the stopped
exponential tends to zero by the positive-drift strong law. This proof
also covers infinite positive mean, since the negative part is bounded.
Ruin is an exact hit only because negative steps cannot skip the target
integer level.

The insurance application explicitly assumes independent normal claims.
It treats ruin as reaching zero or a negative value. The variance-zero
model is deterministic and uses no exponential formula with a zero
denominator.

## Worked calculations

The exact roulette success probability is
1/((10/9)^20+1)=0.10839798964516666, which rounds to 0.1084.
The source's 0.1083 arose from premature rounding.

The favorable three-payoff game has mean increment 2/3 and the
negative-exponential root exp(theta_0)=sqrt(2)-1. Its exact ruin
probability from integer i is (sqrt(2)-1)^i.
For example, at i=5 the value is approximately 0.01219330881975643.

For the symmetric exit from (-a,a), the quartic coefficients are
b=3 and c=2; E T squared=(5 a^4-2 a^2)/3 and
Var(T)=2 a^2(a^2-1)/3. At a=1 the time is deterministically one.

These were direct author calculations, not a new test suite.

## Notation intake for P15.35

- Filtration F_n, stopped information F_T, times L,M,T, terminal X_infinity,
  sampled X_T and Y_M, stopped process Z_n and residual R_n.
- Positive/negative parts, UI cutoff K, threshold lambda, testing events
  A,A_k, the total-variation majorant D and deterministic increment bound B.
- Walk increments xi_j, initial x, S_n, drift mu, variance sigma squared,
  natural filtration, P_x,E_x, first-hit T_a.
- Generating function G_T(s), the finite-time indicator convention,
  s in [0,1], and 0^0=1.
- Exponential moment varphi(theta), distinguished from a characteristic
  function with imaginary exponent.
- Simple-walk probabilities p,q, ratio r=q/p, drift d=p-q, interval
  tau_(a,b), width w, block index m and exponential time parameter c.
- Fair positive root u=exp(theta), its inverse generating function,
  the binomial coefficient index n.
- Biased exit probabilities alpha,beta; the minimum depth I.
- Negative drift rho=q-p, V_0, centered increments eta_j and sum R_T,
  increment variance v=4pq.
- Downward generating function f(s), Catalan numbers C_k and composition
  indices k_1,...,k_x.
- Quartic Y_n, coefficient variables b,c in that calculation only,
  symmetric width a and its exit time T.
- General exponential root theta_0; block increment threshold delta,
  p_delta and k; general exit tau and one-sided crossing T.
- Insurance claims zeta_n, premium c, claim mean mu, variance sigma squared,
  net drift d=c-mu and initial capital x.
- Counterexample martingale M_n, gain G_n and predictable doubling stake.

## Completion and next source work

All 20 proof groups and all 11 exercises are saved. One full author
read-back of the actual body and annex was completed, followed by the
direct corrections recorded above. No Section 4.8 proof or exercise
is left as an outline or an unproved imported assertion.

Root can route the new P15.35 chapter and update the older martingale
and UI optional-stopping boundaries to these precise results.
The next distinct source presentation is Section 4.9: reflection,
ballot and the rest of the source's combinatorial random-walk proofs.
The broader original Gnedenko–Kolmogorov general-array historical chain
and all other earlier source obligations retain their separate standing.

No independent reviews, scanners, tests, builds or manuscript renders
were run. This is completed authoring for the assigned Section 4.8
scope; consolidated independent review remains later in the user's
required sequence.
