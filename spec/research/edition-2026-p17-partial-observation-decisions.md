# Åström 1965: partial-observation decisions, P17 / D3

## Authored result

Saved:

- handbook/parts/p17/partial-observation-decisions.tex
- handbook/annex/p17/partial-observation-decisions.tex

The component has 11 complete result/proof pairs. It supplies the original five finite-horizon theorems, the belief-process lemma, both complete four-stage examples, the original perfect-information/open-loop comparisons, an explicit delayed-observation construction, and formal boundary examples. The hidden state and observation sets are finite; the original common control set remains an arbitrary nonempty compact subset of Euclidean space, with continuous transition entries and costs. The information state is the entire continuous probability simplex. No finite belief grid is substituted.

The source's finite-horizon existence premises are supplied by a complete weighted-posterior continuity proof and a constructed Borel minimizer on the compact control set. The policy proof covers the original deterministic observation-history class and a separately defined larger randomized history class. The latter extension includes exact conditional action independence and a prior-dependent Markov projection; the simultaneous deterministic optimum is proved independently.

There is no unresolved mathematical prerequisite in the assigned original five-theorem chain or either original example. The original paper contains no infinite-horizon theorem. General infinite-horizon partial-observation results and later general piecewise-linear or approximation theorems remain separate source presentations.

Root owns all shared routes, bibliography and notation integration. No shared file or earlier component was edited. The fixed review snapshot under build/review-2026-09-08-2130 was not touched. One complete author read-through of the actual body and annex was performed, with its corrections applied in the same batch. No independent reviewer, scanner, test, build, acceptance check or manuscript PDF render was run. This handoff does not grant independent acceptance.

## Complete exact primary acquired and read

K. J. Åström, Optimal Control of Markov Processes with Incomplete State Information, Journal of Mathematical Analysis and Applications 10(1), February 1965, pp. 174–205. DOI 10.1016/0022-247X(65)90154-X. The original first page identifies IBM Nordic Laboratory, Sweden, and says Submitted by Richard Bellman.

- Original capture: source/references/astrom-1965-incomplete-information/Astrom-1965.pdf
- Direct free institutional URL: https://lup.lub.lu.se/search/files/5323668/8867085.pdf
- Institutional record: https://lup.lub.lu.se/record/8867084
- Repository's current record: https://lup.lub.lu.se/search/publication/d677280f-74cf-4f52-bc01-2a8f358f4f92
- Publisher identity: https://www.sciencedirect.com/science/article/pii/0022247X6590154X
- SHA256: 91CE79CB812E01A6DF9707300E2A26A7200DDE27658D361B7CA366EA8F4C4385
- Size: 3416471 bytes.
- Extent: 34 PDF pages, comprising two preliminary pages and the complete 32-page original reprint.
- Physical page = printed page minus 171; original p. 174 is physical page 3, and p. 205 is physical page 34.
- Source-reading images: tmp/pdfs/p17-astrom-1965/ast65-03.png through ast65-34.png.
- Text derivative: tmp/pdfs/p17-astrom-1965/astrom1965.txt. This extracts the repository wrapper, not the scanned mathematical body; it was not treated as a full text of the paper.

Personally read every original page 174–205 in its page image, including all formulas, tables, both figures, discussion, qualifications, notes and references. The source target was frozen after that complete reading and before writing the manuscript. The figures provide plots of the displayed value functions; their mathematical content is supplied by complete exact formulas and the information bounds, without copying the scanned figures.

The repository metadata adds a terminal I to the title. The original title on p. 174 does not have that I; the new bibliography intake uses the actual original title. The institutional record also links a separate 1964 IBM Technical Paper, no. 18.137; that report was not acquired or silently equated with the 1965 journal article.

The institutional PDF has a generated cover and modern PDF producer metadata. Those wrapper dates are acquisition metadata and do not establish a different mathematical edition. The exact downloaded file is retained unchanged and its actual reprint body supplies the source identity.

## Frozen source scope

| Original location | Actual content | Delivered treatment |
| --- | --- | --- |
| Section I, pp. 174–177 | Motivation from stochastic/adaptive control, state estimation and control synthesis, quantization discussion, outline of the paper. | Reader context and exact finite-model boundary. Finite fixed-parameter augmentation is proved; continuous stochastic control and quantization convergence are not claimed from this discussion. |
| Section II, pp. 177–179, equations (2.1)–(2.6) | Finite hidden states; compact Euclidean controls; transition/cost continuity; finite observation matrix; control histories; finite expected-cost criterion. | Full timing, initial observation law, private action randomization and conditional observation law are made explicit. Original deterministic history elimination is proved. |
| Section II remark, p. 179 | Delayed measurements, time-dependent delay, open-loop schedules. | Complete retained-information construction on a finite hidden-path augmentation, with exact delivered blocks and policy inclusion. The needed retention convention is stated; forced forgetting is distinguished. |
| Section III A, pp. 179–182, equations (3.1)–(3.14) | Backward conditional-cost derivation and introduction of the conditional state distribution. | Full conditional expectation definitions, current/future timing, finite-horizon backward proof and exact residual identity. |
| Section III B, pp. 182–183, equations (3.15)–(3.25) | Recursive filtering, unnormalized observation columns, their norms and posterior normalization. | Every numerator, denominator and likelihood; Borel update; null-branch default; conditional action-law justification and full induction. |
| Section III C, pp. 183–186, Theorems 1–2, equations (3.26)–(3.35) | Necessary Bellman equation, sufficient verification and minimum initial expected cost. | Continuous value existence, full compact minimizer construction, terminal condition, all-history policy proof, corrected conditional future costs, a.s. necessity and both verification directions. |
| Section IV, pp. 186–189, Lemma 1, Theorem 3, equations (4.1)–(4.9) | Belief transition process, complete-information reduction, offline policy and online filtering distinction. | Full belief kernel, at most m posterior atoms, Markov property under a belief policy, controlled-history distinction, both implementation/projection directions, common value and simultaneous deterministic attainment. |
| Section V, pp. 189–193, Theorems 4–5, equations (5.1)–(5.14) | Perfect observations, uniform uninformative observations, open-loop recursion, upper/lower information bounds and their differences. | All backward inequalities; ordered transition products; identical-row extension; current-belief versus pre-observation baseline; complete ex ante bounds and correctly based information values. |
| Section VI, Example 1, pp. 193–198, equations (6.1)–(6.13), Figure 1 | Binary switch with continuous control, noisy binary observation, terminal failure cost, four- and nine-case calculations, posterior formulas and information comparisons. | Full source matrices and all branch sums with tie conditions; symmetry/concavity derivation of all four value functions; all q and belief endpoints; explicit policies and a rational worked observation trace; exact perfect/open-loop comparisons. |
| Section VI, Example 2, pp. 198–204, equations (6.14)–(6.17), Figure 2 and tables | Four-action production example, expected profit maximization, exact/noisy/no-observation calculations over four stages. | Every input and unnormalized posterior column; all four action expressions at every backward stage; complete branch consistency, dominated-action comparisons and rational thresholds; every full-information action table and open-loop candidate table; exact information-value example. |
| Section VII and references, pp. 204–205 | Historical attributions and separate underlying works. | Read and retained as source context. No separate original body is claimed acquired by this paper's bibliography. |

The original has exactly five numbered theorems and one numbered lemma. The 11 manuscript pairs are an editorial proof organization, not a claim that the original printed 11 theorems.

## Eleven result/proof pairs

| Body label | Annex label | Complete proof |
| --- | --- | --- |
| thm:p17-astrom-filter | annex:p17.astrom.filter | Joint kernel law, action conditioning without atom division, initial Bayes rule, full posterior induction, zero-likelihood event probability, Borel maps and finite-support belief kernel. |
| thm:p17-astrom-information-state | annex:p17.astrom.information.state | Expected cost and controlled transition; belief-Markov policy; original implementation; conditional action disintegration and prior-dependent marginal projection; deterministic observation-history elimination. |
| thm:p17-astrom-continuous-selection | annex:p17.astrom.continuous.selection | Weighted zero-mass continuity, compactness/attainment facts, continuity of minima and a nested compact-cube Borel minimizing selector. |
| thm:p17-astrom-finite-optimum | annex:p17.astrom.finite.optimum | Complete continuous backward recursion, uniqueness, bounds, randomized-history domination, deterministic simultaneous equality and both model optima. |
| thm:p17-astrom-verification | annex:p17.astrom.verification | Exact residual telescoping, necessity and sufficiency almost surely, approximate loss, actual conditional future-cost recursion and null-history scope. |
| thm:p17-astrom-information-bounds | annex:p17.astrom.information.bounds | Perfect-state induction, no-future-observation schedule minimization, identical observation rows, identity observation matrix, all four initial inequalities and information values. |
| thm:p17-astrom-delays | annex:p17.astrom.delays | Finite tagged path state, appended transitions, exact likelihood of each newly delivered observation block, compact-control belief recursion and information inclusion. |
| thm:p17-astrom-example-one | annex:p17.astrom.example.one | All original four/nine branches, equality cases, every q endpoint, complete four-stage values, endpoint controls, exact posterior trace and information comparisons. |
| thm:p17-astrom-example-two | annex:p17.astrom.example.two | Every posterior column and every action value, both future-branch threshold checks, strict dominations and exact rational control thresholds. |
| thm:p17-astrom-example-two-bounds | annex:p17.astrom.example.two.bounds | All full-state action tables, all open-loop candidate tables and branch eliminations, exact schedule thresholds and the source's plotted bounds as formulas. |
| thm:p17-astrom-information-failures | annex:p17.astrom.information.failures | Zero likelihood, correlated sensor outputs, independent sensor variables coupled to hidden state, observed-cost information, uninformative feedback, unreachable-belief behavior, finite unknown-parameter augmentation and a 17/25 predictive counterexample. |

## Mathematical corrections applied directly to the reader treatment

1. **Timing and initialization, pp. 177–183.** The source writes an arrival-indexed transition p_ij(u,t) but chooses u(t) after observing y_t; its actual recursion (3.20) uses that control to pass from w(t) to w(t+1). The manuscript uses departure-indexed P_t(u) for X_t to X_{t+1}. Its first pre-observation law mu is explicit. If initialized from the source's X_0,p^0, the preliminary transition and initial control must be specified to determine X_1. No action is permitted to alter the state already observed.
2. **Observation independence, equation (3.18), p. 182.** The needed identity is the observation law conditional on the next hidden state and the full past. The one-time matrix q_ij does not imply it. The reader model states the precise controlled transition and observation kernels. The annex gives both a common-noise counterexample and a counterexample with mutually independent sensor variables coupled to the initial hidden state, establishing why their joint relationship must be specified.
3. **Zero observation likelihood, equations (3.19)–(3.25), pp. 182–183.** The source's ratio is derived only on positive-probability histories. The reader construction keeps that condition, assigns a fixed posterior default on impossible branches, proves their event probability zero, and proves zero-weight value invariance. The continuity proof concerns lambda times V(F), not a nonexistent continuous posterior at lambda = 0.
4. **Missing conditional expectations, equations (3.28) and (3.30), pp. 184–185.** A current conditional future value is not the sum of random future posterior costs. The actual reader value is E[sum future costs | current history]; its full conditional recursion and residual identity are proved.
5. **Necessity at null histories, Theorem 1, p. 184.** Optimality for one initial law constrains the Bellman residual almost surely along that policy. It cannot constrain all unreachable beliefs. The chapter proves the exact iff and gives a one-stage counterexample to the unrestricted necessity claim. A simultaneous optimal belief selector is constructed separately.
6. **Attainment and measurable selection, Theorem 2, p. 186.** The source's closing continuity assertion omits the zero-observation-mass and selector details. Both are supplied in full on the original compact continuous-control domain, including a Borel selector which need not be continuous.
7. **Belief support and Markov scope, Lemma 1, p. 187.** The transition has at most m distinct atoms, where m is the number of observations; the paragraph's n-point wording is corrected. Beliefs lie on the normalized simplex, not the whole positive orthant. Their uncontrolled Markov property is proved under a belief-based policy; arbitrary history control has the specified controlled transition instead.
8. **No-observation claims, pp. 190–193.** Identical observation rows add no new hidden-state information conditional on controls. Feedback through even uninformative readings can affect the chosen controls and hence later beliefs. The chapter proves equality of optimal values with a schedule and supplies a counterexample to a stronger all-feedback deterministic-belief interpretation.
9. **Ordered matrices, Theorem 5, p. 192.** With date- and control-dependent transitions, predictions use the ordered product of the actual matrices. The active schedule proof does not replace those products by a power of a single P(u).
10. **Initial information baseline, equations (5.12)–(5.14), p. 193.** Averaging O_1(w(1)) still permits use of the first observation before committing to a schedule. The fully unobserved initial baseline is O_1(mu). The reader treatment proves all four intermediate inequalities, preserving both conditional and ex ante meanings instead of calling these different baselines identical.
11. **Example 1 terminal time, equation (6.3), p. 193.** The displayed isolated terminal t = 0 is replaced by the coherent four-stage terminal X_4=2 cost used in the subsequent V_4,V_3,V_2,V_1 calculation. Posterior components are derived from the original unnormalized columns; the compact formulas avoid erroneous expanded component expressions. The state-two sum at stage three is z_2^1+z_2^2.
12. **Example 2 action tables, pp. 200–203.** All entries are derived from the exact original rational matrices and rewards. In particular the stage-three fourth action is 27.5x - 5.5; the stage-two fourth action is 27.375x + 1.775; the stage-one third action is 34.555x + 5.0925. The rounded source optimal values are replaced by exact terminating decimals. The final partial-information threshold is 1111/1911, and the final schedule threshold is 29/49; the source's printed schedule threshold 0.63 is not used.
13. **Perfect-state comparison on the simplex.** L_t(b) means first revealing the actual state drawn from b, then using perfect information thereafter. With Q=I, reachable post-observation beliefs are point masses. A linear ex ante perfect-information value is not silently identified with the original posterior recursion at every unreachable interior belief.

The final body states the corrected definitions, values and policies directly. This note retains the source discrepancies; readers are not instructed to repair an earlier false formula.

## Exact calculations useful for integration

Example 1, with q = 4/5 and current state-one belief x = 1/10:

    (V4,V3,V2,V1) = (9/10, 1/10, 1/10, 9/125).

One optimal implementation keeps u = 0 for the first two transitions, then flips state two when the stage-three posterior regards it as more likely. The two-reading failure probability is 0.1(1 - 0.8^2) + 0.9(0.2^2) = 0.072.

Example 2:

    V4(x) = 25x - 5
    V3(x) = max(27.5x, 20x + 4.5)
    V2(x) = max(27.375x + 7.65, 20.25x + 11.775)
    V1(x) = max(27.38875x + 15.0925, 20.2225x + 19.25875)

The stage 3,2,1 switching thresholds are 3/5, 11/19 and 1111/1911. The source's production interpretation and changed payoff table are stated explicitly.

The exact stage-one schedule value is max(26.95x + 14.05, 19.6x + 18.4), with threshold 29/49. The perfect-information value is 23.32x + 20.98. At current belief 1/2:

    schedule = 28.2; incomplete observations = 29.37; perfect information = 32.64.

The corresponding increases over that common schedule baseline are 1.17 and 4.44. These are model calculations, not empirical estimates or measured manufacturing outcomes.

## Actual prerequisites and source boundaries

The current P15 regular-conditional-laws and countable-product-measures statements and proofs were read at their required scopes in the immediately preceding author block. The new chapter uses:

- thm:p15-kernel-joint-measure for finite laws and integrals with joint measurable integrands.
- thm:p15-value-conditional-law for the conditional action kernel on the compact standard Borel control set.
- thm:p15-coded-space-extension only for the optional indefinitely specified joint law, not to infer an infinite-horizon optimum.

No unproved complete-information dynamic-programming theorem is imported. The finite-horizon induction, both directions of the belief bridge and the compact-control minimizing selector are proved in the new annex. The previous finite-state/action method is a comparison, not a substitute for the continuous belief/control domains here.

The source's variable-delay remark is given a physical delivery interpretation with a nondecreasing delivered prefix and retention of earlier readings. The full posterior on the finite hidden path accounts for delayed measurements of earlier states. A decreasing enforced memory cutoff would mean forced forgetting and a different information structure; the paper does not specify or prove a distinct theorem for that regime.

The full 1965 original has no infinite-horizon theorem. Discounted stationary partial-observation control, unbounded costs, average rewards and convergence of finite-horizon approximations are therefore separate next presentations. The existing complete weighted-posterior continuity and compact selector are possible prerequisites for a later discounted construction, but no such later source theorem is credited to 1965.

The 1969 paper Optimal Control of Markov Processes with Incomplete State-Information II. The Convexity of the Lossfunction is distinct. A free original lead appears at https://lup.lub.lu.se/search/files/5282313/8867118.pdf; its full body was not acquired or read in this block. The 1964 IBM report is also distinct, as above.

Section VII attributes the conditional-process idea to Stratonovich and cites separate earlier control, filtering and decision sources. The exact needed finite filtering algebra is proved here. Those separate primary source presentations are not counted as acquired merely because their bibliography was read.

## Bibliography and notation intake for root

Integrated on 9 September 2026 as P17.16, with both active routes, the exact
Astrom1965IncompleteInformation bibliography record and ten typed notation
rows. The reader's finite-horizon boundary now links to the acquired and
fully authored 1969 continuation, integrated separately as P17.17; the earlier
acquisition-boundary paragraph records the state at the 1965 author return.
The eleven pairs retain their complete simplex and compact-control domains.
Consolidated reviews and admission remain pending.

Add the following key after reconciling any existing record:

    @article{Astrom1965IncompleteInformation,
      author = {{\AA}str{\"o}m, Karl Johan},
      title = {Optimal Control of Markov Processes with Incomplete State Information},
      journal = {Journal of Mathematical Analysis and Applications},
      volume = {10},
      number = {1},
      year = {1965},
      month = feb,
      pages = {174--205},
      doi = {10.1016/0022-247X(65)90154-X},
      url = {https://lup.lub.lu.se/record/8867084}
    }

Chapter label: sec:p17-partial-observation-decisions.
Annex section: sec:annex-p17-partial-observation-decisions.
Parent requirement: D3. The new unit follows general discounted decisions as a distinct partially observed finite-horizon source presentation.

Local notation to merge:

- Hidden state X_t and finite state set X; observation Y_t and alphabet Y; N,n,m,d; compact control set U, realized control U_t, deterministic maps c_t,f_t and kernels pi_t.
- Transition P_t(u), entries p_si,t; observation Q and q_ij; cost g_t and expected cost J^pi; initial pre-observation mu, source p^0 and fixed preliminary u_0/P_0.
- History H_t and sigma algebra I_t; simplex Delta_n; belief B_t and point b; source w alias; default b-dagger.
- Predicted probabilities a_i; unnormalized columns z^j; likelihood lambda_j; posterior F_j; initial lambda_j^0,F_j^0; belief transition calligraphic R_t.
- Expected immediate cost ell_t; Bellman candidate calligraphic H_t, distinct from the ordinary history H_t; V_t; residual delta_t; conditional future value W_t^pi; loss tolerance eta_t.
- Markov-projection kernel kappa_t and belief marginal nu_t; compact selector cubes C and C_0, restricted minimum h_C, generic continuous objective H.
- Perfect-state values S_t,L_t; no-further-observation value O_t; delivery prefix d_t; augmented hidden path Z_t.
- Example 1 x=b_1, q, e=q_0, alpha=alpha_0, zeta=beta_0, predicted a; local unnormalized entries A,B,C,D; branch functions Phi_2,Phi_1; affine L(a), constants K,c.
- Example 2 predicted a_u and reward offsets c_u; its V_t,L_t,O_t explicitly rebind to reward maximization and reverse the cost inequalities; open-loop candidate calligraphic H_t^{open}.
- Boundary bits X,E,E_1,E_2; xor; unknown fixed parameter Theta and its finite possible values theta; augmented transition p_si,t^theta.

All reward/cost role changes and source/host aliases are explicit. The new primary has no relation to the manuscript's use of Blackwell1965Discounted beyond their stated mathematical interfaces.

## Frozen authored files

- Body: 19595 bytes; SHA256 B563F6EE3FCEF0B77ECEB2626C9CB086DF229B80C8037739E5ED166971D518C8.
- Annex: 36664 bytes; SHA256 75F8D8199FDC705E3D590FCC60CCE7490818008CF9B0DFF54536D8A6582B857E.

The research and PDF skills were personally read and used for source acquisition, identity/version verification and the complete original-page reading. The authoring and corrections follow the governing all-writing-before-consolidated-review sequence.
