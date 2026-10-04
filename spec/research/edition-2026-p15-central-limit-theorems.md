# P15.31 — Central limit theorems: complete authoring return and exact remainder

## Frozen target

The assigned target is the whole of Durrett Section 3.4 in author Version 5
dated 2019-01-11: the introductory paragraph on printed p. 143, the
numbered content 3.4.1–3.4.19 on pp. 144–161, and every Exercise
3.4.1–3.4.13. The last Berry–Esseen proof continues onto printed p. 161
before Section 3.5 begins.

Held original:
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf

SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886

Bibliography key: DurrettPTEAuthor2019. No new bibliography key is needed.
The original PDF is unchanged.

The full target was read before authoring. Every continued source proof
was included. Required record-indicator premises in Example 2.3.10,
printed pp. 72–73, were read in full, with the surrounding p. 71 passage.
The exact source statements of the normal-domain theorem and the
Berry–Esseen rate remarks were reread while fixing the final boundary.
Complete source page images for printed pp. 156–161 (physical pp.
164–169, one-based) were read to resolve the prime moment formulas and
the smoothing/inversion/constant calculation. These are primary-source
images, not manuscript renders.

The existing actual LaTeX interfaces were read for the finite
permutation-cycle law, the weak-convergence probability bridge, the
maximal and variance-series results, the deferred three-series source
route, and the renewal inverse theorem. The previously authored
characteristic, integration, moment, Stirling, product, and independence
prerequisites remain the mathematical foundations.

## Saved scope and precise incomplete result

The saved body and annex contain 25 reciprocal result/proof pairs.
They supply all numbered Section 3.4 content except the full proof of
Theorem 3.4.14, together with all 13 section exercises.

Completed:

- Theorem 3.4.1, including zero variance as a separately stated case.
- Theorem 3.4.2 and Lemmas 3.4.3–3.4.4, retaining the source's complex
  product-comparison route separately from the earlier logarithm proof.
- All Examples 3.4.5–3.4.9 and Exercises 3.4.1–3.4.8.
- Full Theorem 3.4.10 for arbitrary finite row lengths, containing the
  source's n-entry rows, with every Lindeberg and variance hypothesis.
- Examples 3.4.11–3.4.13, including both the source upper/lower variance
  estimates and an exact truncated second moment in the infinite-variance
  example.
- Lemma 3.4.15 and the entire second, method-of-moments proof of
  Theorem 3.4.10.
- Every Exercise 3.4.9–3.4.13, including every Lyapunov parameter case
  and every sparse-jump regime.
- Theorem 3.4.16, retaining the source prime cutoff, comparison law,
  raw moment error and centered moment transfer. Its prime reciprocal
  premise is independently proved in full, not assumed.
- Theorem 3.4.17 and Lemmas 3.4.18–3.4.19, including the complete
  smoothing, quotient inversion, cutoff and constant-three calculation.

Not completed: the two-way general normal-domain characterization in
Theorem 3.4.14, including an explicit construction of normalizers and
the separately referred Gnedenko–Kolmogorov (1954) presentation.
The held Durrett text states this result and refers its proof to that
book; it does not contain the proof. The source referral has not been
acquired or independently identified/read in this block. The supplied
infinite-variance example and finite-variance necessity exercise do not
replace this missing general characterization.

The full Section 3.4 assignment therefore remains incomplete at this
specific theorem, despite the completed exercise, Erdős–Kac and
Berry–Esseen groups. The remaining source theorem is stated in the
body's explicit proof boundary, with its nondegeneracy and denominator
qualifications, not tagged as proved.

The source's separately cited Heyde rate equivalence and historical
references, Hardy–Wright's own Chapter XXII presentation, and the later
local-limit/stable-law sections are also not claimed reproduced.
The elementary prime estimate here fully supplies the premise of
Durrett's actual Erdős–Kac proof; it is not a substitute attribution
for an unread Hardy–Wright source presentation.

## Reciprocal labels

Each suffix below has body label thm:p15-SUFFIX and annex label
annex:p15.SUFFIX.

| Suffix | Result and source mapping |
| --- | --- |
| clt-complex-products | 3.4.2–3.4.4, complex powers and two elementary lemmas. |
| clt-iid | 3.4.1, the full i.i.d. CLT. |
| clt-perturbation | Complete perturbation/Slutsky and deterministic-limit premises. |
| clt-numerical-examples | 3.4.5–3.4.8 and Exercise 3.4.1. |
| clt-pairwise-boundary | 3.4.9, explicit recursive fair-sign construction. |
| clt-oscillation | Exercise 3.4.2, tail law and factorial-subsequence argument. |
| clt-sqrt-scale-necessity | Exercise 3.4.3, full conditional-sign symmetrization. |
| clt-transformed-sums | Exercises 3.4.4–3.4.5, square roots and self-normalization. |
| clt-random-index | Exercise 3.4.6, both maximal estimates, no index independence. |
| clt-renewal-random-index | Exercise 3.4.7, including the overshoot tail bound. |
| clt-renewal-interpolation | Exercise 3.4.8, distinct deterministic-window proof. |
| clt-lindeberg-feller | 3.4.10, full finite-row characteristic-function route. |
| clt-diagonal-truncation | 3.4.15 and the complete centered truncation estimates. |
| clt-moment-array-proof | Second source proof of 3.4.10, every multiplicity pattern. |
| clt-records-and-cycles | 3.4.11 and the whole actual record-rank premise. |
| clt-three-series-source | 3.4.12, now unconditional. |
| clt-infinite-variance-example | 3.4.13, density, cutoff, exact moment and both bounds. |
| clt-escaping-variance | Exercise 3.4.9, variance limit two and Lindeberg tail limit one. |
| clt-lyapunov | Exercises 3.4.10–3.4.12 and their finite-row extension. |
| clt-sparse-jumps | Exercise 3.4.13, all three parameter regimes. |
| clt-prime-reciprocals | Complete elementary prime estimate and its actual prerequisites. |
| clt-erdos-kac | 3.4.16, full source comparison and moment transfer. |
| clt-smoothing-bound | 3.4.18, reflection and approximation to the supremum. |
| clt-cdf-inversion | 3.4.19 with the actual quotient premise and smoothing application. |
| clt-berry-esseen | 3.4.17, all n, constant three, and the sharp order example. |

Chapter route label: sec:p15-central-limit-theorems.
Annex route label: sec:annex-p15-central-limit-theorems.
Owned files are the body/annex central-limit-theorems.tex pair and this
note. Root owns all shared routing, symbols, bibliography and progress.

## Direct corrections and author calculations

Theorem 3.4.14 needs an explicit nondegenerate law. For example, the
constant X=1 satisfies the printed tail ratio condition for large y,
but no deterministic centering and scaling of its deterministic sums
can have a nondegenerate Gaussian limit. The boundary therefore states
nondegeneracy and uses the denominator only when eventually positive.

The smoothing law H_L has infinite absolute first moment. Thus the
source's invocation of its mean-zero CDF inversion lemma on the smoothed
laws does not satisfy that lemma's stated first-moment premise. The
manuscript proves the general integrable-quotient form and verifies the
quotient condition from the original integrable laws. It also proves
the smoothing law's infinite first moment directly. This repairs the
application while retaining its inversion and Riemann–Lebesgue route.

The Lindeberg cubic estimate uses absolute t cubed, so the bound is valid
for negative t as well. Every row normalization is positive where used.
Lyapunov's criterion permits any delta > 0 and does not silently require
its cumulative standard deviation to diverge for a general array.

The pairwise-sign recursion is supplied with consistent indices:
X_(2^r+j)=X_j xi_(r+2), starting at r=0. It produces every claimed dyadic
sum and every pairwise joint law. The printed indexing is not copied
where it fails to produce that construction.

The uniform-prime comparison variables are independent, not identically
distributed: their success probabilities are 1/p. Actual divisibility
indicators are not treated as independent under finite uniform sampling.
The raw moment error is bounded by the number of ordered prime tuples
divided by n. This corrects the malformed equality and coefficient in
the printed p. 156 display without leaving a reader repair instruction.

The same prime section proves all needed elementary number theory:
unique prime factorization, the binomial coefficient bound for theta(x),
summation by parts, finite Euler products, and the prime reciprocal
estimate. No prime number theorem or unproved Mertens estimate is used.

The source alternating-series estimate in the Berry–Esseen proof is
retained; an integral-remainder extension is distinguished. Both the
source integration-by-parts calculation and a direct substitution
compute the cubic Gaussian integral. The final constant is proved
strictly below three using exact elementary inequalities.

Direct numerical evaluation of the displayed formulas gave:

| Quantity | Value before rounding |
| --- | --- |
| Roulette upper normal tail at 19/sqrt(360) | 0.1583196495980154 |
| Fair-coin normal interval [-2,2] | 0.9544997361036417 |
| Exact binomial mass at eight of sixteen | 0.196380615234375 |
| Histogram normal approximation to that mass | 0.19741265136584743 |
| Die-count normal tail at -1.1 | 0.13566606094638267 |
| Berry–Esseen constant from the displayed integral | 2.880164160344324 |

These computations support the author's worked calculations; no tests
or proof-mirroring scripts were added.

## Notation intake for P15.31

- Normal notation: phi_0, Phi, chi, N(0,sigma squared), mu, sigma, rho.
- Array notation: k_n, X_(n,j), S_n, v_(n,j), v_n, L_n(epsilon);
  no independence between rows.
- Asymptotic notation: O_P, o_P, tightness, deterministic asymptotic ratio.
- Complex comparison: z_j,w_j,theta,b,c_n,c,gamma, with local roles.
- Perturbations: Z_n,R_n,A_n,B_n,a,b and uniform law distance d.
- Numerical examples: roulette gain, Bernoulli sums, die count D,
  Poisson Z_lambda; lambda is locally a Poisson mean here.
- Pairwise example: xi_j, X_j, integer r and dyadic sum S_(2^r).
- Oscillation: tail limsup L and factorial-block A_m,B_m.
- Symmetrization: X'_j,Y_j,U_j,V_j, cutoff A, magnitudes R_j,
  signs epsilon_j and truncated variance tau_A squared.
- Random indices: N_n,a_n,delta,r; renewal T_m,N(t),u,D_t,M_t.
- Truncation: N_r,epsilon_n,Y_(n,j),Z_(n,j),R_(n,j),U_n.
- Moment arrays: q_(n,j),q_n,r,k,r_l,i_l,b_n.
- Records/cycles: B_j,H_n,V_j,A_j and strict rank permutations.
- Three-series source route: cutoff A,Y_j,c_n,U_n,V_n.
- Infinite-variance example: R,c_n,Y_(n,j).
- Sparse jumps: beta,u_(n,j),f_t,Q.
- Prime proof: p,vartheta(x),C,A(x),P(x),delta,s;
  delta and P have separate local roles here.
- Erdős–Kac: P_n,E_n,delta_p,g,g_n,ell_n,alpha_n,B_p,V_n,b_n,a_n,q.
- Smoothing: L,h_L,H_L,omega_L,F,G,D,eta,eta_L,lambda,
  x_0,delta,t,e,q and reflected CDFs.
- CDF inversion: K_i,k_i,kappa_i,phi_F,phi_G.
- Berry–Esseen: alpha,beta,gamma,theta,L,F_n,rho, local to that proof.

## Root integration and next author block

The 25 full proof groups and the complete body/annex author read-back
are finished. Root can route P15.31 and update the independent-random-series
chapter's former Lindeberg–Feller boundary: its exact missing premise
is now supplied by thm:p15-clt-lindeberg-feller, and the full source
necessity route is repeated unconditionally here.

The next narrowly defined author block is Theorem 3.4.14: identify and
read the exact Gnedenko–Kolmogorov source, then prove necessity,
sufficiency, normalizer construction, eventual denominator positivity,
centering and nondegeneracy. Keep the separately cited rate-history
presentations and the remaining Section 3.2 exercises visible as
distinct obligations. The later local-limit and stable-law sections
are not included in this return.

The research and PDF skills guided exact primary reading, preservation
of the held source, and this one source note. A quick memory lookup
supplied only the existing discipline of separating source/text work
from other acceptance claims; all manuscript claims above come from
the current files and primary reading.
No independent review, scanner, test, build, manuscript rendering or
manuscript PDF inspection was performed. This return records completed
authoring and an explicit remaining theorem, not acceptance of the
whole Section 3.4 assignment.
