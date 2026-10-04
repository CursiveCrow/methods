# Åström 1969 Part II: P17 / D3 author return

## Completed scope

Saved eight complete result/proof pairs in:

- handbook/parts/p17/astrom-incomplete-information-ii.tex
- handbook/annex/p17/astrom-incomplete-information-ii.tex

They supply the full original 1969 Part II: its two lemmas, main finite-horizon convexity theorem, final concavity remark, control-dependent observation extension and references back to the original Part I examples. The source's full nonnegative cone is retained, with a proved homogeneous interpretation outside the probability simplex and an explicit value at the origin. Every zero image, zero observation weight and mixture endpoint is handled.

The new material also supplies the arbitrary-family supremum/infimum step needed for the original uncountable compact control domain, exact policy-value semantics without presuming attainment, a full Lipschitz bound, and the regularity and Borel selector needed for an attained controlled-sensing policy. A concrete two-stage counterexample distinguishes the convexity result from an invalid unqualified attainment claim.

All eight pairs and their prerequisites are fully authored. There is no remaining mathematical dependency in this selected original source chain. The original four-page paper contains no infinite-horizon theorem, numerical algorithm with an error proof, new numerical example or general piecewise-linear representation theorem. Those claims are not manufactured from its introductory discussion.

Root owns shared integration, routes, bibliography and symbols. No other source or manuscript file, prior author return or review snapshot was edited. One full author read-through of the actual body and annex was completed, and its clarifications were applied in the same batch. No independent review, scanner, test, build, acceptance check or manuscript render was run. This author return does not grant independent acceptance.

## Exact free original, identity and full reading

K. J. Åström, Optimal Control of Markov Processes with Incomplete State-Information. II. The Convexity of the Lossfunction, Journal of Mathematical Analysis and Applications 26(2), May 1969, pp. 403–406. DOI 10.1016/0022-247X(69)90163-2.

The original first page identifies Lund Institute of Technology, Division of Automatic Control, Lund, Sweden. Its support footnote names the Swedish Board for Technical Development, contract 68-336-f.

- Unchanged original capture: source/references/astrom-1969-incomplete-information-ii/Astrom-1969-II.pdf
- Direct free institutional URL: https://lup.lub.lu.se/search/files/5282313/8867118.pdf
- Institutional record: https://lup.lub.lu.se/record/8867114
- Full publication record: https://lup.lub.lu.se/search/publication/52fef87e-3fe0-40f5-9ef7-2d61cb9f5b6c
- Source SHA256: 17A3F1D2E48572DDCC644BCF1850CBEBD13A7A34EC3E96C36DBFA159826A9529
- Size: 1901438 bytes.
- Extent: six PDF pages, consisting of two preliminary pages and the complete four-page original reprint.
- Physical page = printed page minus 400.
- Source-reading images: tmp/pdfs/p17-astrom-1969/ast69-3.png through ast69-6.png.

Every original page, 403–406, was personally read in its page image, including the complete equations, four scalar cases, both lemmas and proofs, main theorem and induction, final remark, support note and sole reference. The target was frozen before manuscript writing.

The institutional PDF has a generated cover and modern producer/date metadata. Those wrapper properties are acquisition metadata; the actual reprint identifies the original 1969 journal version. The downloaded capture is preserved unchanged.

A separate 1968 technical report, TFRT-7002, is listed by Lund under a closely related Part II title at https://portal.research.lu.se/en/publications/optimal-control-of-markov-processes-with-incomplete-stateinformat/. Its body was not acquired or compared. It is not silently treated as the same source version.

## Exact source and proof map

| Body result | Annex proof | Full supplied source content |
| --- | --- | --- |
| thm:p17-astrom-ii-mass-bridge | annex:p17.astrom.ii.mass.bridge | Section 1, pp. 403–404, equations (1.1)–(1.2): source cone, observation maps, controlled sensing, normalization, full mass identity, finite values, homogeneous extension, unnormalized recurrence and exact controlled-policy interpretation. Includes equality of deterministic and randomized extremal values without assuming a maximizer. |
| thm:p17-astrom-ii-maxima | annex:p17.astrom.ii.maxima | Lemma 1, pp. 404–405, equations (2.1)–(2.3): all four scalar cases and equality boundaries; the full two-function convexity proof; arbitrary nonempty finite-valued suprema, finite sums and the concave infimum dual. |
| thm:p17-astrom-ii-perspective | annex:p17.astrom.ii.perspective | Lemma 2, pp. 405–406, equations (2.4)–(2.7): positive linear map, additive norm on the nonnegative cone, exact renormalized mixture weights, both positive images, either zero image, both zero images, mixture endpoints, homogeneity and full concave counterpart. |
| thm:p17-astrom-ii-convexity | annex:p17.astrom.ii.convexity | Main theorem, p. 406: terminal linear reward, arbitrary control supremum, each fixed-control observation perspective, finite summation, every backward induction step and the attained-maximum special case. |
| thm:p17-astrom-ii-concavity | annex:p17.astrom.ii.concavity | Final remark, p. 406: exact reward-negation identity at the terminal and every earlier stage, minimum/maximum conversion, all zero cases and full concavity inequality. |
| thm:p17-astrom-ii-continuity | annex:p17.astrom.ii.continuity | Complete prerequisite/extension for the control-dependent Q assertion, p. 404: uniform Lipschitz value on the cone, continuity of the weighted posterior objective including zero mass, compact-control Borel optimizer, full 1965 filter/policy/verification/information bridges and ray-constant selection. |
| thm:p17-astrom-ii-examples | annex:p17.astrom.ii.examples | The source's Part I example references, pp. 404 and 406: exact previously proved four-stage formulas, their homogeneous cone extensions, strict convexity/concavity calculations, origin and nonunit-mass evaluations. Part II has no separate new example. |
| thm:p17-astrom-ii-boundaries | annex:p17.astrom.ii.boundaries | Fully proved boundary constructions for nonlinear cone maps, a nonadditive norm, signed images, belief-dependent control sets and discontinuous controlled sensing without an attained optimum. |

The original prints two numbered lemmas, one unnumbered main theorem and one final mathematical remark. Eight manuscript proof pairs are the editorial organization of the complete reconstruction and its needed boundaries, not a claim that the original printed eight results.

## Source corrections and qualifications

1. **Origin and zero images, equations (1.1) and (2.4).** The source chooses the whole cone S, including zero, but writes normalized expressions only where the norm is nonzero. The reader definitions assign zero to each vanishing weighted term and V_t(0)=0. The perspective proof treats both zero images, exactly one zero image and both positive images separately. No undefined 0/0 or 0 times an undefined value remains.
2. **The full cone versus a probability vector.** A conditional probability vector has mass one. The source's larger cone is retained as a homogeneous extension, proved to satisfy V_t(w)=||w||_1 V_t(w/||w||_1) for w nonzero. It is not silently reduced to a finite grid or to just the simplex, and a nonunit vector is not treated as a probability law.
3. **Arbitrary compact controls, main theorem p. 406.** The binary maximum lemma alone, by finite repetition, does not justify an uncountable maximum. The arbitrary-family proof is supplied explicitly and uses finite-valued pointwise suprema; no selected maximizing index is used in the convexity argument.
4. **Linearity in the information state.** The main theorem's short wording says the A_j are mappings into S. The earlier definition (1.2) makes them positive linear maps, which is the actual premise used in Lemma 2. The reader theorem states this premise explicitly. A(w)=sqrt(w) shows why mere mapping into the cone would not suffice.
5. **The norm identity.** The equality ||lambda Ax + mu Ay|| = lambda||Ax|| + mu||Ay|| is justified by coordinate nonnegativity and the particular l1 norm. It is not a general identity for all norms or signed images. Both failures have explicit counterexamples.
6. **Lemma 1's penultimate display, equation (2.3), p. 405.** The second maximum must be evaluated at y, as required by the conclusion lambda f(x)+mu f(y). The corrected derivation uses y throughout that term.
7. **Part I example references, p. 404 and final remark p. 406.** The source reverses the actual optimization directions when recalling the 1965 examples. The switch example minimizes terminal failure and gives concave value. The production example maximizes reward and gives convex value. The reader treatment uses the actual fully derived Part I formulas and supplies strict midpoint calculations in the correct directions.
8. **Control-dependent observation quality, p. 404.** The paper says the Part I results continue when Q depends on u, but does not spell out all regularity needed for attainment. The reader model gives the conditional next-observation law and Borel dependence explicitly. Convexity and the full Lipschitz value bound survive Borel observation dependence. The attained-control theorem uses additional continuity of Q in u, alongside the original compact controls and continuous P,g. A two-stage example with discontinuous Q has supremum one and no optimal policy at the fair prior, even allowing randomization. The stronger existence claim is therefore not inferred merely from convexity or compactness.
9. **Numerical and convergence language, p. 404.** The paper offers no algorithm, error bound, effective input representation or limit theorem supporting a universal numerical-computation assertion. The active reader boundary records the proved finite recursion and the additional data a numerical method needs. No later algorithm or piecewise-linear theorem is attributed to this four-page source.

Corrections are made in the actual statements and derivations. The historical discrepancies stay in this note.

## Exact mathematical bridges and proof dependencies

The actual current Part I body and annex were read at the relevant extents, particularly:

- thm:p17-astrom-filter: initial and recursive Bayes updates, action conditioning, zero likelihood, finite joint laws and the Borel belief kernel.
- thm:p17-astrom-information-state: expected cost, implementation, conditional action disintegration and the prior-dependent Markov projection.
- thm:p17-astrom-continuous-selection: full compact minimizer proof, including the nested compact-cube Borel selector and weighted-zero-mass continuity.
- thm:p17-astrom-finite-optimum and thm:p17-astrom-verification: the actual finite-horizon backward and residual arguments.
- thm:p17-astrom-information-bounds: perfect-state and schedule comparisons with the exact initial-information baseline.
- thm:p17-astrom-example-one and thm:p17-astrom-example-two: the complete corrected original four-stage calculations.

The controlled-sensing bridge is literal: replace q_ij by q_ij,t(u) after conditioning on the known chosen action. The numerator is A_j,t(u)b, its mass is the observation probability, and the posterior is its normalized image on positive-mass branches. The sum of observation masses is one because both original matrices are stochastic. The control affects the next measurement; the already received current observation is not made retroactively dependent on the current control.

The cone bound uses C_t=sum from k=t to N of G_k, where G_k bounds the absolute immediate rewards. For every fixed control:

    sum_j ||A_j,t(u)w||_1 = ||w||_1,
    sum_j ||A_j,t(u)w - A_j,t(u)v||_1 <= ||w-v||_1.

The second identity with an inequality is proved by the coordinate triangle inequality and the stochastic row sums. It gives the full C_t Lipschitz estimate by backward induction on the unnormalized recursion.

The policy-value interpretation does not assume an optimizing selector. A fixed history policy has a bounded coefficient vector of expected rewards conditional on each initial hidden state, so its value is linear in the initial belief. The extremal value over the common policy family is Lipschitz, hence Borel. Upper bounds follow by the filtered conditional future law. Reverse inequalities use one nearly optimizing first control and finitely many nearly optimizing observation-contingent continuations. The approximating policies may be deterministic by induction. This proves the exact supremum/infimum recursion in both policy classes. It does not assert that the coefficient family is finite.

The main convexity proof then follows the actual source's different route through its two lemmas and the normalized perspective, with every induction step supplied.

Its broader algebraic formulation is stated explicitly as well: an arbitrary nonempty common control family of positive linear cone maps and linear rewards preserves convexity whenever the recursive suprema are finite. The corresponding finite-infimum statement preserves concavity. This does not need stochastic normalization, compactness or measurability and does not assert a policy existence theorem. The stochastic model's mass bound is the separate justification of finiteness in the actual decision application. Perfect-information and schedule inequalities are explicitly reversed when changing from cost minimization to reward maximization.

## Worked calculations and failure cases

For the 1965 switch with q=4/5:

    V1-(w) = min(w1,w2, (9w1+w2)/25, (w1+9w2)/25).
    V1-(2,1) = 11/25.
    V1-(1/10,9/10) = V1-(9/10,1/10) = 9/125.
    V1-(1/2,1/2) = 1/5 > 9/125.

For the production example:

    V3+(w) = max(27.5 w1, 24.5 w1 + 4.5 w2).
    V3+(2,1) = 55.
    V3+(1/2,1/2) = 14.5 < (27.5+4.5)/2 = 16.

The nonattainment example has a fixed hidden fair bit, U=[0,1], zero first reward, and second-stage reward u in state one and 1-u in state two. The sensing accuracy is h(u)=(1+u)/2 for u<1, and h(1)=1/2. It is Borel and never equals one. The best reward after choosing u is h(u), so the supremum is one but unattained. For any randomized first action, E[1-h(U1)]>0, proving randomization cannot attain it. Its supremum value on the entire cone is w1+w2, which is linear and convex.

Other counterexamples prove the failures of a nonlinear cone map, replacing the additive norm, allowing signed images and allowing belief-dependent control availability. They identify the premise of the algebraic or control argument that is unavailable and are clearly presented as boundary examples.

## Remaining distinct source work

There is no unfinished proof or reading extent for the selected 1969 Part II.

Separate obligations remain:

- The 1968 TFRT-7002 report, whose body was not acquired or version-compared.
- General infinite-horizon partial-observation decisions, whether discounted, undiscounted or average reward.
- Numerical algorithms with actual input encodings and error guarantees.
- General finite piecewise-linear representations and later pruning/convergence methods.
- The other primary filtering and control references already retained in the Part I source handoff.

The 1969 article cites only the 1965 Part I. No unacquired third-party proof is used as a substitute for a required proof here.

## Root integration intake

Integrated on 9 September 2026 as P17.17 after the 1965 treatment, in both
active drivers. Astrom1969IncompleteInformationII and six typed notation rows
are in the canonical bibliography and symbol register. The eight authored
pairs retain the whole cone, zero-mass conventions and distinct convexity
and attainment conditions. Consolidated reviews and admission remain pending.

Chapter label: sec:p17-astrom-incomplete-information-ii.
Annex section: sec:annex-p17-astrom-incomplete-information-ii.
Parent requirement: D3. Route after the Part I partial-observation unit, retaining its separate source identity.

Add or reconcile this bibliography entry:

    @article{Astrom1969IncompleteInformationII,
      author = {{\AA}str{\"o}m, Karl Johan},
      title = {Optimal Control of Markov Processes with Incomplete State-Information. {II}. The Convexity of the Lossfunction},
      journal = {Journal of Mathematical Analysis and Applications},
      volume = {26},
      number = {2},
      year = {1969},
      month = may,
      pages = {403--406},
      doi = {10.1016/0022-247X(69)90163-2},
      url = {https://lup.lub.lu.se/record/8867114}
    }

Local notation:

- S=R_+^n is the full cone; Delta_n is its unit-mass probability section; w,v are nonnegative weight vectors; ||.||_1 is the source norm.
- U,u,U_t; hidden X_t, observation Y_t, observed history H_t; P_t(u),Q_t(u), entries p_si,t(u),q_ij,t(u); vector g_t(u), bound G_t and cumulative bound C_t.
- A_j,t(u) is the source's A_j with its previously suppressed control/time arguments restored; observation index j runs through m possibilities.
- V_t+ and V_t- distinguish the source's use of V_t for the maximum equation and minimum remark; ext is sup or inf accordingly. Nonnegative c scales a cone vector.
- Perspective calligraphic P_A f; source mixture lambda,mu correspond to theta,1-theta; source lambda_1,mu_1 correspond to theta a/c,(1-theta)b/c in the proof, with a=||Ax||_1,b=||Ay||_1,c=theta a+(1-theta)b.
- Fixed-policy coefficients a_i^pi; policy extrema W_t+,W_t-; scalar convex functions f_alpha,F; Borel optimizer f_t and ray extension fhat_t.
- The failure example's h(u) is sensing accuracy, not a history; signed/nonlinear maps and Euclidean norm are confined to their explicit counterexamples.

## Frozen authored files

- Body: 12009 bytes; SHA256 C670A42B33CC2C31D886500BD2898E33580D56CD3A59DC6DDA25D60615FAC54A.
- Annex: 22418 bytes; SHA256 3F596C13B7CD09DB8F6BFD13D35772BE4229CFF050074FEBD1DCEE35ADF088AA.

Research and PDF skills were personally read and used for the complete primary acquisition and source-page reading. The governing all-authoring-before-consolidated-review workflow was preserved.
