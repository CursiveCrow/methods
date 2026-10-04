# P15.27 — Characteristic-function criteria and moments

## Saved authoring scope

The body and annex complete the remaining Durrett Section 3.3 presentation:
Theorems 3.3.22–3.3.26, Examples 3.3.23–3.3.24, the three moment-problem
counterexamples, the Carleman remark, and every outstanding exercise in
Section 3.3. There are 29 reciprocal body/proof pairs. This is an authoring
handoff; consolidated independent reviews remain after the complete
manuscript change set.

Owned files:

- handbook/parts/p15/characteristic-function-criteria-and-moments.tex
- handbook/annex/p15/characteristic-function-criteria-and-moments.tex
- spec/research/edition-2026-p15-characteristic-function-criteria-and-moments.md

The chapter label is sec:p15-characteristic-function-criteria-and-moments;
the annex label is sec:annex-p15-characteristic-function-criteria-and-moments.
Root owns routing, bibliography, notation registration, source records,
progress records, and edits to earlier boundary paragraphs.

## Frozen primary source and reading

Rick Durrett, Probability: Theory and Examples, author Version 5 dated
2019-01-11, canonical bibliography key DurrettPTEAuthor2019.

Held original:
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf

SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886

The complete Section 3.3, printed pp. 125–143, was read in the preceding
characteristic-function author block. The remaining presentation on printed
pp. 136–143 was reread for this block, including every continued Pólya,
periodic-function, moment, and counterexample proof. Complete primary page
images for printed pp. 137–143 (physical pp. 145–151, one-based) were also
read. These were images of the source, not manuscript renders.

Other complete prerequisite passages read in this authoring chain:

- Printed p. 132, including the uniform-sum exercise and surrounding
  characteristic-function continuity presentation.
- Printed p. 133, Exercises 3.3.7–3.3.11, read in the complete prefix pass.
- Printed p. 124, Exercises 3.2.4, 3.2.5, and 3.2.10.
- Printed p. 24, Exercises 1.4.3–1.4.4.
- Printed p. 91, Exercises 2.5.9–2.5.12; the actual premises needed here are
  2.5.9 and 2.5.10.
- Printed p. 463, Exercise A.2.1, to resolve the erroneous interval
  approximation referral.
- Printed p. 470, Exercise A.4.7, for the weighted-measure integral identity.
- The earlier Section 2.2 alternating heavy-tail example, previously read
  for the weak-law chapter and used in the Pitman example.

The author read the applicable research and PDF skills. They influenced
the exact-version freeze, complete reading of referred premises, source
page inspection where mathematical extraction was ambiguous, and this
single durable source note. No new source acquisition or bibliography key
is required. The held original was not modified.

This is a reconstruction of Durrett's presentation of the Heyde and
Stoyanov examples. It does not claim that the original Heyde paper,
Stoyanov book, or Feller's separate historical presentation has been read
or reproduced independently.

## Reciprocal proof inventory

Each suffix below has body label thm:p15-SUFFIX and annex label
annex:p15.SUFFIX.

| Suffix | Complete content |
| --- | --- |
| criteria-real-integration | Interval and continuous approximation in L1, Riemann–Lebesgue, one-variable substitution, weighted measures. |
| criteria-weak-integration | Weak Fatou, unbounded continuous integration, finite quantile approximation. |
| criteria-complex-log | The local complex logarithm and the complex nth-power limit. |
| criteria-tight-transforms | Tight-family equicontinuity and compact uniform transform convergence. |
| criteria-uniform-sums | Uniform-sum transforms, inverse integral, explicit piecewise-polynomial density. |
| criteria-limit-operations | Gaussian variance convergence, independent weak sums, infinite products from almost-sure series. |
| criteria-series-examples | Binary uniform expansion and the singular Cantor law with nondecaying transform. |
| criteria-moment-identities | Gaussian moments, the absolute-moment integral, essential-supremum moment growth. |
| criteria-local-zero | Local transform convergence to one implies concentration at zero. |
| criteria-independent-series | Probability-Cauchy completeness, first-crossing inequality, weak-to-probability-to-almost-sure convergence. |
| criteria-pitman-law | All directions of Pitman's criterion, corrected derivative sign, full tail example. |
| criteria-convex-derivative | Right derivatives and the positive Stieltjes measure of a convex function. |
| criteria-polya | Pólya's criterion, source finite-support approximation route, direct construction, and nonzero tail limit. |
| criteria-binomial-series | General real binomial expansion and normalized positive coefficients. |
| criteria-stable-functions | Pólya and Spitzer routes, every stability parameter case and scaling. |
| criteria-periodic-example | Complete periodic triangular Fourier representation and normalization. |
| criteria-equality-sets | Arbitrary closed symmetric equality sets for two characteristic functions. |
| criteria-cancellation | Independent convolution noncancellation and cancellation against the same variable. |
| criteria-complex-gamma | Gamma integral on the right half-plane with the precise complex-power branch. |
| criteria-lognormal-family | Continuous and discrete lognormal families with common moments and distinct laws. |
| criteria-real-counterexample | The whole-line moment-indeterminate density family, including every moment. |
| criteria-compact-moments | Compact support of any competing law and the separate Bernstein determinacy proof. |
| criteria-analytic-determinacy | The source moment-growth criterion, full local analytic argument and propagation. |
| criteria-quasianalytic | Full derivative-envelope quasi-analytic lemma. |
| criteria-carleman | Carleman's moment criterion deduced from the proved lemma. |
| criteria-moment-method | Existence, moment transfer, determinacy, and full-sequence convergence. |
| criteria-generalized-gamma | All parameter domains, exact moments and growth classification. |
| criteria-stieltjes | Symmetric-square correspondence and the Stieltjes sufficient criterion. |
| criteria-positive-counterexample | Full nonnegative counterexample family and all integer moments. |

## Exact exercise coverage

This chapter supplies Exercises 3.3.5, 3.3.7–3.3.15, and 3.3.17–3.3.25.
The preceding characteristic-functions-and-inversion chapter supplies
Exercises 3.3.1–3.3.4, 3.3.6, and 3.3.16. Thus Exercises 3.3.1–3.3.25
are all supplied between the two chapters.

The source's exercise referrals are also discharged here where used:
Exercises 3.2.4, 3.2.5, 3.2.10; Exercises 1.4.3–1.4.4; the weighted
integration identity in A.4.7; and the actual independent-series
Exercises 2.5.9–2.5.10. The probability-Cauchy completeness argument is
proved directly.

The midpoint quantile construction uses exactly m atoms and obtains
uniform CDF error at most 1/(2m). Its positive-support case preserves
positive atoms, as needed in Pólya's source approximation route.
The weak-integration proof explicitly provides the tail control needed
for transferring every moment in the method-of-moments theorem.

## Source routes and direct corrections

Pólya's original finite-support approximation and continuity-theorem route
is retained in full. The direct mixture construction is separately
identified. The Stieltjes measure may be infinite near zero; its
right-derivative convention uses open right tails. The nonzero tail limit
c is an atom of mass exactly c at zero, with the remaining mixture scaled
by 1-c; c=1 gives the point mass at zero.

Both the direct convexity proof for stable parameters at most one and
Spitzer's positive binomial-mixture proof for parameters below two are
retained. The normal endpoint, impossibility beyond two, and exact
independent-sum scaling are included. The periodic example proves its
Fourier identity and coefficient sum through Abel logarithm series and
integration; no general Fourier theorem is silently invoked.

The analytic moment proof preserves the source's derivative and interval
propagation route, including odd absolute moments and the separate zero
growth-rate case. Compact-support determinacy has its distinct polynomial
proof. Carleman's remark has a complete derivative-envelope proof; it is
not left as a cited additional criterion. The method of moments first
constructs a limiting law, then transfers moments and applies uniqueness.

Corrections made directly in the mathematics:

- Exercise 3.3.14's derivative condition is +ia, not the printed -ia.
  The necessity proof controls the complex logarithm using connectedness;
  it does not choose an uncontrolled nth-root branch.
- Exercise 1.4.3's A.2.1 referral does not establish interval approximation
  in the held version. The required approximation is proved from the
  supplied interval outer-measure construction.
- Exercise 3.3.18's referral to 2.5.11 does not establish probability
  completeness. Completeness is proved, and the actual first-crossing
  and independent-series premises 2.5.9–2.5.10 are supplied.
- The moment proof uses the actual Taylor lemma 3.3.19 and derivative
  theorem 3.3.18, correcting its mismatched internal referrals.
- The generalized-gamma substitution uses
  dx = lambda^(-1) y^(1/lambda-1) dy; lambda > 0 and alpha > -1.
- Lognormal densities are defined as zero on the nonpositive half-line;
  no expression evaluates log(0). Distinct continuous parameters give
  distinct laws. Discrete lognormal parameters differing by exp(j) give
  the same law; parameters in [1,e) provide distinct representatives.
- The complex gamma power uses arg(a+ib)=arctan(b/a) for a>0.
  Both moment counterexample normalizers are derived explicitly.
- All finite/infinite moment qualifications, the atom at zero in the
  symmetric-square correspondence, and the class of competing laws are
  explicit. A density's assigned value at zero creates no point mass.

## Notation intake for provisional P15.27

The following symbols are local to their stated definitions or proofs.
Root should preserve that locality in the shared notation record.

- Integration: intervals I,J, monotone substitution T, Lebesgue measure
  lambda, step functions, and continuous cutoffs chi_R.
- Weak integration: law mu, quantile Q_F, midpoint atoms x_(m,j),
  approximants mu_m,F_m, and controlling functions g,h.
- Transform limits: local complex logarithm L, characteristic functions
  phi,Psi_n, complex variables z,w, and a tight family indexed by I.
- Uniform sums: f_n and positive part (u)_+.
- Independent series: partial sums S_(m,j), probability-Cauchy variables
  Z_n, subsequence indices N_j, and first-crossing events.
- Pitman: real centering a, logarithmic functions A_n,D_n, and the local
  positive normalizer c of the alternating heavy-tail law.
- Pólya: right derivative d, locally finite positive measure eta,
  weighted probability nu, positive scale s, tail limit c, and nu_c.
- Binomial and stable laws: real beta, coefficients c_n, parameter alpha,
  and characteristic functions psi.
- Equality sets: closed symmetric A, cutoff chi, perturbation v and phi_2.
- Moments: m_k, absolute moments nu_k, essential bound Lambda, growth
  parameter r and local expansion center theta.
- Complex gamma: p>0, q in the right half-plane, and its fixed argument.
- Lognormal families: f_0,f_a, masses a_k, normalizer c_a, variable Y_a.
- Counterexamples: lambda,beta,c_lambda; the whole-line and nonnegative
  normalizers are different local quantities.
- Quasi-analytic proof: M_n,a_n,B,x_N,y_N,L_N, all defined before use.
- Generalized gamma: alpha,lambda,C,nu_n.
- Stieltjes correspondence: an independent symmetric sign epsilon and
  epsilon sqrt(X), with the atom at zero retained.

## Authoring completion and continuation

All 29 proof groups are saved. One complete author read-back of the body
and annex was performed, followed by the direct corrections recorded
above. No independent review, scanner, test, build, or manuscript PDF
inspection was performed for this author block.

No theorem, example, counterexample, or exercise proof group remains
unwritten in the assigned Durrett Section 3.3 batch. Root can close the
preceding chapter's Section 3.3 source-writing boundary and update the
weak-convergence chapter's outstanding list for Exercises 3.2.4, 3.2.5,
and 3.2.10.

The next distinct source chain is Section 3.4's general central-limit
presentation. Its separate source proof routes, the other still-outstanding
Section 3.2 exercises, and the later full stable-law presentation in
Section 3.8 remain separate writing obligations. The direct complex
logarithm and power limit proved here do not silently count a later,
different source proof as reproduced. No central-limit theorem was used
in this chapter.
