# Bellman1952 Theorems 2–7: author return for P17 / D3

## Delivered source scope

Authored all six remaining original theorem presentations and their source qualifications in:

- handbook/parts/p17/bellman-original-constructions.tex
- handbook/annex/p17/bellman-original-constructions.tex

The unit contains 10 complete formal result/proof pairs: the corrected full-domain shrinking-resource result and its counterexample; the probability-vector stopping theorem; the two-resource priority theorem and its complete commensurate piecewise-linear construction; convex splitting and its concave counterexample; retrieval and location-only box search; and the exact threshold theorem.

The continuous domains are retained: an allocation cone over the entire interval [0,x0], the whole probability simplex, the entire nonnegative two-resource quadrant, and the scalar interval [0,1]. Finite words, support recursion and approximation sequences are actual constructions on those domains, not replacements by a finite grid.

One whole author read-through of the actual body and annex was completed. Its local corrections were saved, including the k=1 threshold-bound inequality, removal of an unnecessary continuous-second-derivative restriction, explicit box-prior support/coordinate roles, and the zero/uninspectable/end-parameter cases. No independent review, scanner, test, build, or manuscript render was run. Root owns shared integration and all previously returned files. This author return does not grant independent acceptance.

## Unchanged exact original and reading

Richard Bellman, On the Theory of Dynamic Programming, Proceedings of the National Academy of Sciences of the United States of America 38(8), August 1952, 716–719. DOI 10.1073/pnas.38.8.716. Communicated by J. von Neumann on 5 June 1952; source affiliation The RAND Corporation.

- Held original: source/references/bellman-1952-dynamic-programming/Bellman-1952.pdf
- Direct acquisition URL: https://www.derongliu.org/adp/adp-cdrom/refs/bellman19520716.pdf
- Authoritative identity: https://pmc.ncbi.nlm.nih.gov/articles/PMC1063639/
- SHA256: 58CCF880B967862F7B2C909844B71A0A195CEF6306429B637955F67FEFC3B204
- Size: 338942 bytes; 4 physical pages.
- Physical page = printed page minus 715.
- Existing bibliography key: Bellman1952DynamicProgramming.
- Reading images: tmp/pdfs/p17-sequential-decisions/bellman52-1.png through bellman52-4.png.
- Reading text: tmp/pdfs/p17-sequential-decisions/bellman1952.txt.

The complete four-page original had been read in the preceding sequential-decision block. This block personally reread the exact original images of pp. 717–719, including every statement, formula, bound, qualification and footnote for Theorems 2–7. The frozen source extent is:

| Original theorem | Exact source formulas and scope |
| --- | --- |
| 2, p. 717 | Equations (2.3)–(2.4): nonnegative allocations with sum x; continuous nonnegative a and b; a(0)=0; b <= c x, 0<c<1; the printed sum of h(c^j x0), with h(x) the maximum at resource exactly x; continuous zero-boundary solution claim. |
| 3, pp. 717–718 | Equations (2.5)–(2.7): probability vector p0,...,pN; absorbing x0; unit-cost probe to coordinate vectors or one of finitely many transformations; contraction of nonzero-state probability mass by c_l<1; bounded positive solution. No continuity of the transformations is stated. |
| 4, p. 718 | Equations (3.1)–(3.2): p1,p2,s1,s2 in (0,1), r1,r2>0; current-index comparison p_i r_i resource/(1-p_i); commensurability qualification s1^m=s2^n implying piecewise linearity. |
| 5, p. 718 | Equations (3.3)–(3.4): continuous resource splitting, 0<a,b<1, increasing g,h vanishing at zero with nonnegative second derivatives; reduction to endpoints; contrasting concave case; relation to the original resource-allocation example. |
| 6, pp. 718–719 | Equations (3.5)–(3.7): completed inspection cost t_i/(1-q_i); conditional remaining probabilities; one-possible-box boundary; index p_i(1-q_i)/t_i; distinct qualification for locating rather than obtaining the ball. |
| 7, p. 719 | Equations (3.8)–(3.9): f(0)=0, 0<a<1, 0<x<=1; probe x f(1) or transform f(ax); minimizing positive integer (k+1)/(1-a^k); threshold formula and both weak inequalities at the threshold. |

The paper announces successive approximation and says detailed proofs will appear elsewhere; it does not contain those omitted proof bodies. The new annex supplies full independent derivations rather than counting that announcement as a proof. The original credits the two-resource solution jointly with M. Shiffman and the threshold solution jointly with D. Blackwell; those historical qualifications remain attached to the source identity.

## Substantive correction to Theorem 2

The printed condition

    sum_j h(c^j x0) < infinity,  h(x)=max_{sum z_i=x} a(z)

does not control rewards at intermediate smaller resource levels. Nonnegative continuity alone does not make h nondecreasing.

The saved counterexample has one resource, x0=1, c=1/2 and b(x)=x/4. The reward is the sum of disjoint triangular bumps centered at (3/4)4^-j, supported on [(5/8)4^-j,(7/8)4^-j], with height 1/(j+1). It is continuous, nonnegative, and zero at zero. Every geometric-grid value h(2^-j) is zero, but the trajectory starting at 3/4 receives the divergent harmonic sequence. Choosing the tighter valid c=1/4 also leaves the printed grid values zero. Thus the failure is not caused by a loose shrinking constant.

The reader theorem is corrected directly, retaining the entire original allocation domain and continuous data:

- Define all finite-horizon values F_n and their canonical extended nonnegative value V=sup_n F_n.
- A continuous zero-boundary solution exists **if and only if** sup_{0<=x<=delta} V(x) tends to zero as delta tends to zero.
- When this holds, the solution is V and is unique, with uniform error bounded by that small-resource supremum at c^n x0.
- A usable sufficient condition is summability of the actual envelope H(t)=max_{sum z_i<=t}a(z). Its tail supplies an explicit uniform approximation bound.

This is not a silently added monotonicity restriction. The exact iff result classifies existence on the full original continuous domain, and the stronger envelope test is declared as a sufficient construction. The original grid condition is explicitly disproved. The counterexample satisfies full joint continuity on the compact allocation cone, so it does not rely on a weaker interpretation of fiberwise continuity.

## Ten complete result/proof pairs

| Body label | Annex label | Complete supplied construction |
| --- | --- | --- |
| thm:p17-bellman-shrinking | annex:p17.bellman.shrinking | Compact allocation maximum and continuity; finite trajectory expansion; exact small-resource iff, uniqueness and uniform approximation; summable envelope; full linear example. |
| thm:p17-bellman-shrinking-counterexample | annex:p17.bellman.shrinking.counterexample | Explicit disjoint continuous bumps, zero geometric-grid sum, harmonic trajectory, and contradiction to a continuous zero-boundary fixed point. |
| thm:p17-bellman-probability-stopping | annex:p17.bellman.probability.stopping | Entire-simplex value iteration; explicit proper two-step-block policy; boundedness; all bounded solutions automatically nonnegative; greedy properness and full-policy verification; uniform K^2/n error; failure without strict mass reduction. |
| thm:p17-bellman-two-resources | annex:p17.bellman.two.resources | Compatible bounded fixed points on invariant rectangles; canonical global value; continuity, convexity, homogeneity; adjacent interchange in both orientations, including a word never using the preferred action; ties, greedy attainment, axes and geometric error. |
| thm:p17-bellman-commensurate | annex:p17.bellman.commensurate | Exact integer recurrence on each ratio cone; finite entrance; coprime periodic orbit, action counts and common resource scaling; finite prefix/cycle coefficients and geometric closed form; all boundary cones and axes; exact example. |
| thm:p17-bellman-convex-split | annex:p17.bellman.convex.split | Nonnegative linear envelope; convexity of every iterate and limit; convexity in the split variable; both endpoint choices and ties; complete binary-series construction with tail; power-payoff formula and example. |
| thm:p17-bellman-concave-split | annex:p17.bellman.concave.split | Strict interior maximizer and two closed continuous value formulas showing endpoint reduction fails in the source's contrasting concave regime. |
| thm:p17-bellman-box-retrieval | annex:p17.bellman.box.retrieval | Conditional geometric inspection cost; posterior/zero-support/one-box cases; adjacent ordering; exact recursion for every prior; attempt-level verification against arbitrary history/randomized policies; uninspectable and zero-cost cases and a correlated-failure counterexample. |
| thm:p17-bellman-box-location | annex:p17.bellman.box.location | Optimization over the uninspected last box; sorted-prefix formula; full attempt-policy verification; both branches of the source's highest-index qualification; exact examples; one versus multiple uninspectable locations. |
| thm:p17-bellman-threshold | annex:p17.bellman.threshold | Exact probability-vector bridge; finite unrolling and integer minimization; finite search bound; threshold bounds and every tie; explicit pointwise formula, absorbing discontinuity and parameter endpoints; a=1/2 worked solution. |

## Further source and scope qualifications applied

### Theorem 3

The source has no time discount and does not require continuous maps. The new proof does not import a strict sup-norm contraction. It builds a uniformly proper policy with cost K=2/(1-c_l), constructs the limit of truncated step costs, and proves greedy properness from the nonnegative bounded Bellman solution. Each fixed initial vector has a finitely branching history tree; its law is constructed without silently requiring global Borel measurability of the arbitrary S_l. The continuous scalar specialization in Theorem 7 is solved on every x in [0,1], not on finitely many selected vectors.

### Theorem 4

The original quadrant is unbounded, so the bounded-function theorem cannot be applied with one global bound on its immediate rewards. It is applied correctly on each invariant rectangle, whose unique solutions agree on overlaps. The value is thereby the unique function bounded on every such rectangle; the operational value automatically belongs to this class.

The commensurate piecewise-linear assertion is supplied in a precise form: countably many linear cones, locally finite away from the axes, with common boundary values established by continuity and separate explicit axis values. No finite global cone partition or unproved converse for incommensurate scales is asserted. The first action's p_i multiplies its immediate reward as well as its continuation, exactly as in the original equation.

### Theorem 5

No continuous-second-derivative assumption is imposed. The reader result is proved for continuous nondecreasing convex g,h, which contains the source's twice-differentiable nonnegative-second-derivative case. Convexity supplies the missing envelope automatically, so this construction survives the corrected Theorem 2.

The general exact solution is the limit/supremum of explicit binary endpoint rewards with a proved geometric tail. No unsupported universal threshold for arbitrary g,h is inferred from the source's informal comparison with its two-resource example. For power rewards the closed form is given. For the concave counterexample g=h=x-x^2/2, a=b=1/2, the full split value is 2x-x^2/3 and the endpoint-only value is 2x-2x^2/3.

### Theorem 6

The original equation is fully solved as a completed-inspection-cost equation for every normalized prior. Its boundary written with only one positive coordinate is the unit prior in that normalized domain. A p_i=1 branch has zero continuation and never evaluates division by 1-p_i. Zero-prior boxes are ignored.

To interpret t_i/(1-q_i) as repeated attempt cost, the constant failure probability must hold conditional on past attempts and ball location. The reader explicitly states this operational premise and gives a permanent-blockage counterexample if only a marginal failure chance is known. The abstract completed-cost recursion itself does not depend on such an attempt model.

Positive attempt costs give the printed ratio index. The zero-cost extension uses cross-product comparisons, puts free positive-prior boxes first, and explicitly requires almost-sure completion. An uninspectable positive-prior box makes retrieval impossible. Location can leave one such box uninspected, but cannot distinguish two positive-prior uninspectable boxes. The locating/obtaining distinction and the source's maximum-index-first-or-never qualification are both fully proved.

### Theorem 7

The boundary at zero is absorbing and discontinuous: the positive-state limit is 1, not 0. Continuity from Theorem 2 is not imported.
The minimizing integer is positive; immediate probing at x=1 cannot achieve a finite solution without a transformation. Multiple minimizing integers give the same threshold. At a=1/2, k=1 and k=2 both minimize and both policies are retained. The threshold bound uses 1-a^k <= k(1-a), with equality allowed at k=1. The excluded a=0 endpoint gives a different value (1 off zero), and a=1 admits no finite solution.

## Exact examples and computations

- Shrinking linear allocation: V(x)=x max_i r_i/(1-d_i), attained by a maximizing activity throughout.
- Commensurate two-resource example p1=p2=s1=s2=1/2, r1=r2=1: V=(4x+2y)/7 on 1<=x/y<=2 and V=(2x+4y)/7 on 1/2<=x/y<=1; V(3/2,1)=8/7.
- Convex split: g=x^2, h=2x^2, a=1/2, b=1/4 yields 32x^2/15.
- Concave split: at x=1, the interior policy has value 5/3 while endpoint-only choices yield 4/3.
- Retrieval with p=(1/2,3/10,1/5), t=(2,1,4), q=0: order 2,1,3, value 16/5. Location omits box 3, value 12/5; the other omission values are 19/5 and 4.
- With p=(4/5,1/5), t=(1,3/10), q=0, retrieval starts with the highest-index box and costs 53/50; location omits that box and costs 3/10.
- Threshold a=1/2: C=4, tau=1/2, f(x)=1+4x on (0,1/2], f(x)=2+2x on [1/2,1], and f(0)=0.

## Integration and notation intake

Body chapter: sec:p17-bellman-original-constructions.
Annex section: sec:annex-p17-bellman-original-constructions.
Parent requirement: D3.

Reused exact active interfaces:

- thm:p17-bellman-bounded-transformations, applied only on invariant rectangles where the required reward bound and continuation factors below one hold.
- thm:p15-kolmogorov-countable, through a checked finite-alphabet history-tree embedding for each fixed initial probability vector.

The entire needed compact-maximum argument, limit/uniqueness arguments, proper-policy verification, interchange proofs, integer-period construction, search ordering, and threshold minimization are in the new annex. No old shared or manuscript file was edited. No new bibliography key is needed.

New local notation:

- Shrinking domain x0, dimension m, allocations D/D(x), reward a and successor b, shrinking c, operator T, finite values F_n, canonical extended V, exact-level h, envelope H, small-state bound eta; linear r_i/d_i/K; positive-part bump notation.
- Probability-vector simplex Delta_d with coordinates 0,...,d; unit vectors e_i (source x_i), absorbing e0; maps S_l, factors c_l, absorption time tau, proper-policy bound K and truncated values.
- Two-resource p1/p2 multipliers, s1/s2 resource fractions, r1/r2 rewards, x/y, current indices I1/I2; bar p; action words w; prior-action counts N_i(j), total counts n_i(w); prefix multiplier D_w and coefficients A_w/B_w.
- Commensurate q, coprime u/v, cone integer k and fractional exponent theta; entrance word w and cycle z.
- Split constants a,b, reward functions g,h, exponent lambda, coefficients A/B, and local K,c.
- Box prior p on coordinates 1,...,d, separately rebound unit priors e_i, support, attempt times t_i, failure probabilities q_i, completed costs c_i, normalized p^(-i), order sigma, retrieval F, omission L_l and location L.
- Scalar threshold parameter a, solution f, C=f(1), minimizing integer k, threshold tau, first-crossing n(x) and affine candidates g_n(x).

The same letters denote different explicitly local roles in these different source constructions. Root should retain those typed roles in the symbol intake rather than merge the domains.

## Completion boundary

All six assigned source presentations are fully authored. Theorem 2's printed assertion is false under its literal hypotheses; its complete counterexample and exact corrected full-domain result are supplied directly. No open mathematical dependency or sketch is being reported as a completed proof.

The source's previously supplied Theorem 1 plus this unit cover all seven theorem presentations of the held four-page Bellman1952 note. The note's referenced Arrow–Blackwell–Girshick, Arrow–Harris–Marschak and Wald works, and the unpublished/detailed-proof versions alluded to in the note, remain distinct source/version obligations. Bellman1954/1957 and Blackwell1965's broader source scopes remain governed by the preceding sequential-decision inventory. Author completion of this source chain is not manuscript-wide completion or independent admission.
