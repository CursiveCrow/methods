# Sequential decisions: author return for P17 / D3

## Delivered scope

Saved a complete finite sequential-decision method in:

- handbook/parts/p17/sequential-decisions.tex
- handbook/annex/p17/sequential-decisions.tex

There are 13 complete result/proof pairs, plus the model, return, example and computation definitions. The finite-horizon proof covers every admissible history, including histories null under a particular initial law, and every randomized history-dependent policy. The homogeneous discounted proof covers the same full policy class and supplies an attained deterministic stationary optimum from every state.

The construction includes the path probability law, finite-horizon backward recursion, uniform discounted tails, a complete contraction/fixed-point proof, the full original Bellman1952 Theorem 1 bounded-transformation result, value iteration and policy-loss certificates, the actual policy matrix inverse, finite exact elimination, both Blackwell improvement routines, policy iteration with a terminating tie rule, exact multistage computations and six families of counterexamples. The broader original-source obligations are itemized below.

One full author read-through of the actual body and annex was completed. Local corrections found in that read-through were saved in the same batch, including precise finite/infinite input boundaries and the exact generated-operator bridge. No independent review, scanner, test, build, or manuscript render was run. This author return does not grant independent acceptance. Root owns shared integration and every previous component.

## Source identities and complete reading

### Bellman1952: acquired complete original

Richard Bellman, On the Theory of Dynamic Programming, Proceedings of the National Academy of Sciences of the United States of America 38(8), August 1952, pp. 716–719. DOI 10.1073/pnas.38.8.716. The article identifies The RAND Corporation and communication by J. von Neumann on 5 June 1952.

- Original capture: source/references/bellman-1952-dynamic-programming/Bellman-1952.pdf
- Direct acquisition URL: https://www.derongliu.org/adp/adp-cdrom/refs/bellman19520716.pdf
- Authoritative identity: https://pmc.ncbi.nlm.nih.gov/articles/PMC1063639/
- SHA256: 58CCF880B967862F7B2C909844B71A0A195CEF6306429B637955F67FEFC3B204
- Size: 338942 bytes; 4 physical pages.
- Physical page = printed page minus 715.
- The capture contains the unchanged PNAS article with its later download stamp. The mirror's certificate was expired/untrusted; the public read used the tool's certificate-skip option, and the actual body identity was checked against PMC and the original first page.
- Reading derivatives: tmp/pdfs/p17-sequential-decisions/bellman1952.txt and bellman52-1.png through bellman52-4.png.

Personally read the complete original, all four pages, in text and original-page images. Frozen assigned source result: Theorem 1, p. 717, equations (2.1)–(2.2), and the successive-approximation qualification at the top of p. 718. The source requires an invariant region, finitely many transformations, uniform bounded nonnegative g_k, and 0 <= h_k <= c2 < 1. The manuscript proves the entire bounded-function result on an arbitrary nonempty set, which includes the original Euclidean-region scope. It does not replace that theorem by a finite-state case.

The original announces that detailed proofs of its results will appear elsewhere. The present full contraction proof supplies the missing proof for Theorem 1; a cited outline has not been counted as a proof. The source's other six theorems remain separate presentations.

### Blackwell1965: acquired complete original

David Blackwell, Discounted Dynamic Programming, The Annals of Mathematical Statistics 36(1), February 1965, pp. 226–235. DOI 10.1214/aoms/1177700285. Received 24 September 1964; author affiliation University of California, Berkeley.

- Original capture: source/references/blackwell-1965-discounted/Blackwell-1965.pdf
- Direct acquisition URL: https://jeromemathis.fr/wp-content/uploads/2020/01/Blackwell_1965.pdf
- Publisher locator: https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-36/issue-1/Discounted-Dynamic-Programming/10.1214/aoms/1177700285.full
- SHA256: BBC5DD1D9D391AE4E64BC08591DC493A08301739316D05257C1592772404625C
- Size: 1362298 bytes; 11 physical pages, consisting of the JSTOR cover and 10 article pages.
- Physical page = printed page minus 224.
- Reading text: tmp/pdfs/p17-sequential-decisions/blackwell1965.txt.
- Original-page images: bw65-06.png through bw65-10.png, and bw65-tail-05.png, in the same temporary directory.

The complete article pp. 226–235 was read in text, including all definitions, examples, theorem statements, proofs, qualifications and references. The original images of pp. 229–234 were personally read to resolve the proof formulas, both improvement routines, the tail estimate and the action-equivalence issue. Poppler reported an xref reconstruction warning for the original capture and missing display-font warnings; the actual pages remained readable and the original file was preserved unchanged.

The selected exact source interfaces are: Sections 2–3 for the full history-policy model and reward timing; Theorems 3–5 for stationary/generated operators and contraction; the bounded upper-value and optimality assertions of Theorem 6(d)–(f); finite action attainment from Theorem 7(b); and both Howard and Eaton–Zadeh routines in Theorem 8. The source uses a common action set and calls nonrandomized sequences of state maps Markov plans. Both conventions are explicitly bridged in the manuscript.

The finite generated operator is identified by enumerating all common actions as constant state maps. Every statewise selection is then generated, and the source's U is exactly the manuscript's T. The extension to state-dependent feasible actions has a full policy-law proof, including erasure of redundant action names, conditional reconstruction on finite histories, and a full-support initial law that yields equality from every initial state.

### Source leads not acquired

- Bellman1957, A Markovian Decision Process, DOI 10.1512/iumj.1957.6.56038: the publisher page https://iumj.org/article/1116/ exposed only its one-page abstract PDF. No full original was acquired. The old/current metadata disagree on issue numbering; no new bibliography entry was made from that lead.
- Bellman1954, The Theory of Dynamic Programming, Bulletin of the AMS 60, 503–515, DOI 10.1090/S0002-9904-1954-09848-8: both publisher PDF URLs returned an access challenge. Neither response was accepted as a source PDF. The exact 1952 original was acquired instead, and its independent identity is retained.

The empty dedicated directories for those two acquisition attempts are not evidence of acquired source bodies. No attempt was made to purchase access.

## Thirteen full result/proof pairs

| Body label | Annex label | Delivered proof |
| --- | --- | --- |
| thm:p17-sequential-policy-law | annex:p17.sequential.policy.law | Finite cylinder products, normalization/consistency, exact countable extension, null-history continuation and the initial-law-dependent Markov marginal projection. |
| thm:p17-sequential-backward | annex:p17.sequential.backward | Full backward induction over all histories and randomized action distributions; simultaneous deterministic attainment; N=0 and gamma=0; exact finite rational computation. |
| thm:p17-sequential-tail | annex:p17.sequential.tail | Geometric limit, absolute/uniform reward convergence, expectation limit, truncation and terminal bounds, sharp signed two-policy factor. |
| thm:p17-sequential-contraction | annex:p17.sequential.contraction | Completeness of bounded functions, closure of bounded measurable functions, full successive-approximation existence and uniqueness, both error bounds and Blackwell's monotone/constant-shift criterion. |
| thm:p17-bellman-bounded-transformations | annex:p17.bellman.bounded.transformations | Complete Bellman1952 Theorem 1 on arbitrary nonempty E, all original bounds and positivity, finite maximum inequality, nonnegative solution and deterministic finite-MDP bridge. |
| thm:p17-sequential-stationary-optimum | annex:p17.sequential.stationary.optimum | Bellman inequalities telescoped under every randomized history policy, vanishing terminal term, stationary attainment, upper certificates and both directions of value-equation optimality. |
| thm:p17-sequential-value-iteration | annex:p17.sequential.value.iteration | Iteration and residual errors, eta-greedy policy-loss bound, exact stopping tolerances and zero-discount endpoint. |
| thm:p17-sequential-policy-evaluation | annex:p17.sequential.policy.evaluation | Stochastic matrix powers, matrix norm bounds, both sides of the Neumann inverse, exact policy equation, tail and pivot-by-pivot finite rational elimination. |
| thm:p17-sequential-improvement | annex:p17.sequential.improvement | Source first-action/restarted-policy meaning, Howard improvement and strict-state gain, full Eaton–Zadeh switching proof including ties. |
| thm:p17-sequential-policy-iteration | annex:p17.sequential.policy.iteration | Every evaluation and greedy choice, retain-on-tie rule, strict improvement, no revisits, finite policy-count bound, exact-input domain. |
| thm:p17-sequential-maintenance | annex:p17.sequential.maintenance | All action values in the three-period problem; both discounted evaluations, one policy improvement, fixed-point verification and exact 23-iteration certificate. |
| thm:p17-sequential-boundaries | annex:p17.sequential.boundaries | Undiscounted divergence/nonuniqueness/oscillation, unbounded rewards, full Blackwell countable-action nonattainment, forgotten observed bit, time-varying rewards and tie cycling. |
| thm:p17-sequential-source-bridge | annex:p17.sequential.source.bridge | Exact source time/discount/operator classes, generated-action enumeration, two-way feasible/common-action law bridge and corrected operator-equivalence criterion. |

## Actual calculations and corrections

The editorial maintenance example observes good/bad machine condition before each action. Running receives 3 now and yields next good/bad with probability 1/2 each; service receives 1 and leaves good; waiting in bad receives 0 and leaves bad; repair receives -2 and leaves good. The cost/benefit timing is declared before computation.

For N=3, gamma=1, zero terminal payoff, values in (G,B) order are:

    v3=(0,0), v2=(3,0), v1=(9/2,1), v0=(23/4,5/2).

For gamma=3/4, (run,wait) evaluates to (24/5,0); one improvement yields (run,repair), whose value is (72/11,32/11). All unused action values are explicitly smaller. The first two value iterates are (3,0) and (33/8,1/4). R=3 gives value error 12(3/4)^k and greedy-policy loss at most 72(3/4)^k; the exact integer comparison at k=23 proves loss below 1/10.

Source corrections are applied directly to the active formulas:

1. Blackwell p. 229, opening of Theorem 2's proof, gives the two-policy tail estimate without the factor 2. With bounded signed rewards the valid bound is 2 R gamma^N/(1-gamma). The manuscript proves it and gives a finite one-state example attaining equality. This does not invalidate approximation by truncation; it changes the quantitative bound.
2. Blackwell p. 234 describes equality of the realized reward functions and transition laws as equivalent to equality of the action operators. Equality of operators actually requires only equal expected one-step reward and equal transition row when gamma>0. The manuscript proves the iff using v=0 and coordinate indicators, and gives rewards (0,2) versus (1,1) with the same half-half row as a counterexample to the claimed necessity of pointwise reward equality. At gamma=0, transition equality is unnecessary as well.
3. All Markov-projection claims retain their exact quantifier over one initial distribution. Full simultaneous optimality is independently proved; it is not inferred from a different projected policy for each prior.
4. Null histories use a specified continuation law. They are not assigned a conditional probability by dividing by zero.
5. A generic policy-change stopping rule can cycle on ties. The active algorithm retains a current maximizing action and proves strict improvement whenever it changes.
6. Boundedness is automatic under finite homogeneous real reward tables. The unbounded-reward counterexample explicitly enlarges the state space; it is not falsely presented as a finite homogeneous counterexample.

## Existing manuscript interfaces and integration

Chapter label: sec:p17-sequential-decisions.
Annex section label: sec:annex-p17-sequential-decisions.
Reader computation method: def:p17-sequential-computation.
Parent requirement: D3; root assigns the printed subsection/chapter placement.

Read the actual relevant definitions and proofs in:

- P17 finite-expected-utility.tex: finite lottery reduction, expected-utility representation and its domain. The chapter declares additive time aggregation and discount as further model assumptions.
- P17 value-of-information.tex and annex: thm:p17-information-policy-value and its full finite signalwise optimization proof, including null signals.
- P15 countable-product-measures.tex and annex: thm:p15-kolmogorov-countable, its consistent real-coordinate domain and complete extension proof. The new proof explicitly embeds alternating finite state/action labels into those real coordinates and checks consistency.

No unproved matrix inverse, fixed-point theorem, geometric limit or generic history-policy dynamic-programming theorem is used as a placeholder. Their needed constructions are supplied in the new annex.

New local notation includes S; common A, feasible A_t(s), chosen random action A_t; X_t; P_t/P; r_t/r and expected reward rbar_t/rbar; history h_t and kernel pi_t; initial rho; Markov maps f_t and stationary f; N,g,gamma; J_{t,N}^pi, J^pi, V*, V^f; reward bound R; optimality T and fixed-policy T_f; supremum/vector and matrix infinity norms; abstract bounded-function E,B,u_k,w; Bellman indices k, transformations S_k, rewards g_k, continuation factors h_k, C,b,F; iteration residual delta(v), eta-greediness and epsilon tolerance; P_f,r_f,B_f; improvement d and switching policy h; maintenance states G,B and four named actions; source beta and generated U; action erasure kappa_s; and action functional L_a. The multiple local roles of B and g are explicitly bound in their respective constructions and should be recorded as local roles rather than merged.

Root owns all shared drivers, bibliography and symbol rows. Neither existing P17 nor P15 files were edited.

## Bibliography intake

Add or reconcile these complete entries during root integration:

    @article{Bellman1952DynamicProgramming,
      author = {Bellman, Richard},
      title = {On the Theory of Dynamic Programming},
      journal = {Proceedings of the National Academy of Sciences of the United States of America},
      volume = {38},
      number = {8},
      year = {1952},
      pages = {716--719},
      doi = {10.1073/pnas.38.8.716},
      url = {https://pmc.ncbi.nlm.nih.gov/articles/PMC1063639/}
    }

    @article{Blackwell1965Discounted,
      author = {Blackwell, David},
      title = {Discounted Dynamic Programming},
      journal = {The Annals of Mathematical Statistics},
      volume = {36},
      number = {1},
      year = {1965},
      pages = {226--235},
      doi = {10.1214/aoms/1177700285},
      url = {https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-36/issue-1/Discounted-Dynamic-Programming/10.1214/aoms/1177700285.full}
    }

## Exact remaining original-source obligations

There is no remaining mathematical prerequisite for the assigned finite-horizon and bounded discounted finite-state/action method.

Full source presentation is a larger claim:

- Bellman1952 Theorem 1 is fully supplied here. The remaining six original presentations are now supplied in handbook/parts/p17/bellman-original-constructions.tex and its matching annex, with ten complete proof pairs. The original continuous resource, simplex, quadrant and threshold domains are retained. The false geometric-grid condition in Theorem 2 is replaced by a proved exact full-domain continuity criterion, a constructive sufficient envelope condition and a continuous counterexample. See edition-2026-p17-bellman-original-constructions.md for all original locators, constructions and corrections. Together the two chapters supply the seven theorem presentations of the held 1952 note.
- Blackwell1965's Section 2 general Borel factorization and selection lemma (pp. 227–228), its non-Borel-projection counterexamples 2 and 3 (pp. 229–230), and Theorems 1–2 on prior-almost-everywhere approximate policies remain general-state presentations. The finite marginal projection is not a substitute for that measurable selection theorem.
- Blackwell's complete general generated-policy Theorem 6(a)–(c), pp. 232–233, and its essentially countable/finite Borel-state Theorem 7, pp. 233–234, require their own broader source treatment. The finite upper-certificate, Bellman optimality, attainment and both improvement constructions are proved here at the exact finite state/action scope.
- Theorem 5's contraction argument and its fixed-point premise are fully supplied, including the closed bounded-measurable-function space. This does not by itself create measurable optimizing selectors in an uncountable action space.
- Bellman1954 and Bellman1957 full originals remain acquisition leads, as above. Blackwell1964 Memoryless Strategies in Finite Stage Dynamic Programming, Howard1960, Eaton–Zadeh1961, and the Dubins–Savage manuscript cited by Blackwell remain separately identified source presentations; their complete bodies were not acquired in this block.
- Average reward, undiscounted total reward, stochastic shortest-path assumptions, partial observation/belief-state control, learning unknown transitions, unbounded rewards and general measurable action selection remain outside this finite method and must not be marked complete from these files.

The next sequential-decision source continuation can now start from these proved finite interfaces and select the precise outstanding source and state-space/criterion regime. No unrestricted Bellman equation or finite surrogate has been presented as closing those broader obligations.
