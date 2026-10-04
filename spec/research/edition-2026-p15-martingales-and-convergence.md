# P15.16: martingales, strategies, stopping and convergence

Written 8 September 2026. The complete body and proof annex are connected
after the strong-law applications. The new material contains fifteen
reciprocal statement/proof pairs. Root read the entire saved LaTeX and
corrected its derivations and parameter declarations during authoring.
Consolidated reviews remain deferred until all manuscript changes are made.

Body at initial writing: handbook/parts/p15/martingales-and-convergence.tex,
16566 bytes, SHA-256
E090F1CB1114FC2FEAD7E6CA60E3DF1B8E27A8A41E43F8DE844B2B6590F7F949.
The later forward-reference integration points to the completed UI and
conditional-limit theorems; current body is 16715 bytes, SHA-256
9A95DE35CBD8867199BB939BEA9AF37BD5AB2E62E55A768800FF064903B42215.
Annex: handbook/annex/p15/martingales-and-convergence.tex, 31377 bytes,
SHA-256 79212866F2EE1234956350DD6272AA453E3D04A2A8C93B3FBAD9408851D1732D.

## Primary source and full read extent

Durrett, Probability: Theory and Examples, author Version 5 dated
11 January 2019, source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
SHA-256 AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
The existing bibliography key DurrettPTEAuthor2019 is used.

Printed pp. 217–224, physical pp. 225–232, were read completely as extracted
source text: Examples 4.2.1–3, Theorems 4.2.4–12, Examples 4.2.13–14 and
Exercises 4.2.1–10. Source physical pages 226, 229 and 231 were also viewed
to resolve the exponential expression, upcrossing display and exercise
domains. The source's potential-theory aside is not counted as a proved
discrete-time result. The first paragraph of Section 4.3 was read as a
continuation lead; its applications are not included in this chapter.

## Complete supplied results

The fifteen suffixes have body prefix thm:p15- and annex prefix annex:p15.:
martingale-examples; martingale-conditioning; martingale-convex;
predictable-transform; stopping-calculus; bounded-optional-sampling;
upcrossing-inequality; martingale-convergence; martingale-source-counterexamples;
localized-martingale-convergence; nontrivial-product-limit;
summable-product-compensation; supermartingale-switching; dubins-upcrossing;
martingale-boundary-calculations.

These include every source strategy and clipped-process step of the
upcrossing proof, a countable common event and separate exclusion of both
infinite limits, the stopped fair walk and the complete intermittent-process
example, all selected exercise constructions, the logarithmic product limit
in both finite and negative-infinite mean cases, switching and the full
Dubins exponential bound. Complete finite-horizon gambling calculations
and an independent rare-jump martingale expose the missing hypotheses.

## Direct corrections and declared domains

The source's product conditional display on p. 218 uses inconsistent
variable names; the active equation is E(M_(n+1) | H_n) = M_n.
Its exponential product needs the initial constant c: the initial-one
martingale is exp(theta(S_n-c))/phi(theta)^n. The unshifted exponential
has initial value exp(theta c). The active statement requires real theta
and finite phi(theta), and proves strict positivity of the normalizer.
The product-input filtration and increment filtration are distinct; the
larger increment-past martingale assertion is proved by independence.

Natural filtrations include time zero. Literal stopped-sigma-field
inclusion uses pointwise S <= T; the optional-sampling statement also
handles almost-sure bounds through stopped versions. Predictable bounds
may depend on the time index. Clipping deals with almost-sure coefficient
bounds without losing predictability.

The upcrossing marker T0=-1 is not claimed to be a stopping time in the
nonnegative-index filtration. All subsequent entrance/exit times are.
The unfinished clipped holding gain is nonnegative, and the complementary
strategy supplies the source expectation inequality.

The stopped walk's almost-sure hitting is deduced from martingale convergence,
not assumed. The intermittent source example has P(X_k != 0)=1/k and
E|X_k| = sum_(j<=k) 1/j - 1 + 1/k. Both its zero and nonzero subsequences
occur infinitely often. Localization uses the integrable upper increment
bound and retains X0's positive part.

The iid product proof includes zero factors and E log Y=-infinity.
Compensation requires deterministic summable lower multiplicative errors;
it introduces no unnecessary product-integrability premise. Dubins uses
0<a<b and positive integer crossing counts. The first-success stopping
time is unbounded when 0<p<1; p=1 is its separate deterministic case.

## Integration and notation

The body and annex are in the P15 driver after strong-law-applications.
Strong-law and conditional-expectation dependencies refer to their actual
proved statements. Canonical notation includes the filtrations, transforms,
stopping fields, upcrossing times/counts, product normalizers, compensation
and switching variables, and the explicitly defined example parameters.

The remaining probability work includes stronger martingale convergence,
unbounded sampling, the remaining applications and distributional/statistical
presentations. No independent review, new test or manuscript render ran.
