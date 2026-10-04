# Blackwell's general discounted decisions: P17 / D3 author return

## Saved scope and ownership

The following new files supply 13 complete result/proof pairs:

- handbook/parts/p17/blackwell-general-discounted.tex
- handbook/annex/p17/blackwell-general-discounted.tex

They give the complete assigned general Borel-space chain of Blackwell1965: Section 2 factorization, kernel products and the exact two-part selection lemma; Theorems 1–2 and their Markov corollary; all three original counterexamples, with an actual construction of the Borel set having non-Borel projection; all stationary/generated operator results in Theorems 3–5, including their finite-horizon interpretation; every part (a)–(f) of Theorem 6; both essential-countability/finiteness conclusions in Theorem 7; and both general improvement routines in Theorem 8.

The original arbitrary standard Borel state and action domains, bounded Borel reward, arbitrary Borel probability kernel, and discount 0 <= beta < 1 are retained. Every policy law is defined at null histories as well as reachable histories. The mean-selection conclusion is pointwise. Conditional action laws used to remove history are relative to the specified prior and current prefix law. The resulting domination and approximate optimality retain their exact prior-almost-everywhere quantifiers.

The mathematical prerequisites needed for the assigned source chain are supplied here or bridged to actual full proofs, as detailed below. No narrower finite case is used in place of the general theorem. No unresolved measurable-selector premise remains in this authored treatment.

Root owns shared routes, bibliography, symbol rows, earlier components and integration. The fixed snapshot build/review-2026-09-08-2130 was not edited. No independent reviewer, scanner, test, build, acceptance check or manuscript render was run. One full author read-through of the actual body and annex was performed; resulting clarifications were applied in the same batch. This is an author return, not independent acceptance.

## Exact original and reading record

David Blackwell, Discounted Dynamic Programming, The Annals of Mathematical Statistics 36(1), February 1965, pp. 226–235. DOI 10.1214/aoms/1177700285. University of California, Berkeley; received 24 September 1964.

- Unchanged held original: source/references/blackwell-1965-discounted/Blackwell-1965.pdf
- SHA256: BBC5DD1D9D391AE4E64BC08591DC493A08301739316D05257C1592772404625C
- Size: 1362298 bytes.
- Physical extent: 11 pages, consisting of the JSTOR cover and all 10 original article pages.
- Physical page = printed page minus 224.
- Existing bibliography key: Blackwell1965Discounted.
- Direct capture URL: https://jeromemathis.fr/wp-content/uploads/2020/01/Blackwell_1965.pdf
- Publisher identity: https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-36/issue-1/Discounted-Dynamic-Programming/10.1214/aoms/1177700285.full
- Complete text derivative personally reread in this block: tmp/pdfs/p17-sequential-decisions/blackwell1965.txt.
- Original pp. 227–228 personally read in new source-only images tmp/pdfs/p17-blackwell-general/bw65-foundation-03.png and bw65-foundation-04.png.
- Original pp. 232–234 personally reread in existing bw65-08.png, bw65-09.png and bw65-10.png under tmp/pdfs/p17-sequential-decisions.
- The prior sequential author block read the complete original and the original formula images of pp. 229–234, including the signed tail formula, finite-horizon generated recursion, essential-equivalence condition and both improvement proofs.

The full target was frozen before writing by rereading pp. 226–235, including the final bibliography. The original-page readings settled the extraction's missing inequality symbols, especially the selection lemma's event with >= at p. 228, Theorem 6(c)'s epsilon >= 0 at p. 232, the exact beta-scaled error on p. 233, and the weak inequalities and tie branch in Theorem 8 on p. 234.

Poppler reports missing display fonts for this held scan. Its original page images remain readable, and the original capture has been preserved byte for byte. The only newly produced images are source-reading derivatives, not manuscript output.

## Exact source-to-result and proof map

All body labels below begin thm:p17-; all proof labels begin annex:p17.

| Body suffix | Annex suffix | Original extent and complete supplied content |
| --- | --- | --- |
| blackwell-factorization | blackwell.factorization | Section 2, pp. 227–228, and Section 3, p. 228: factorization, exact a.e. uniqueness, joint integrands, finite/countable products, measurable parameter dependence, policy future kernel and bounded Borel return. Correct two-policy signed tail from Theorem 2, p. 229. |
| blackwell-positive-selection | blackwell.positive.selection | Full auxiliary construction for the Section 2 selection lemma: Polish refinements with unchanged Borel sets, countable common refinement, closed projection fibers, normalized graph kernels, nested positive-probability balls and a Borel limit in each actual fiber. |
| blackwell-selection | blackwell.selection | Section 2 lemma, p. 228, clauses (1) and (2): measurable essential supremum, strict margin, exact mean improvement, essential-maximum attainment case, >= threshold null event, and the degenerate-kernel/Borel-map equivalence. |
| blackwell-prior-optimal | blackwell.prior.optimal | Theorem 1, p. 229: integrated supremum, countable approaching policy sequence, initial-state Borel pasting, proof that every competitor is bounded by the countable upper envelope a.e., and the exact prior-dependent quantifier. |
| blackwell-prior-markov | blackwell.prior.markov | Theorem 2, pp. 229–230, and corollary, p. 230: corrected tail truncation, every backward replacement, current-law disintegration, essential upper selection, conditional order given initial state, finite error allocation and Markov approximate optimality. |
| blackwell-projection-boundaries | blackwell.projection.boundaries | Examples 1–2, p. 229, and Example 3, p. 230: complete universal closed relation and diagonal proof of a non-Borel projection, Borel coding into the actual unit square, full no-attainment/no-uniform-optimum/no-uniform-Markov-domination calculations, tagged disjoint state space and beta = 0 qualification. |
| blackwell-generated-operators | blackwell.generated.operators | Theorems 3–4, p. 231; finite-horizon interpretation, pp. 231–232; Theorem 5, p. 232; countable-action bridge, p. 233: full bounded Borel operator properties, first-admissible-index selection, each backward finite-horizon error term, complete contraction interface, restart identity, and exact index-model equivalence. |
| blackwell-generated-value | blackwell.generated.value | Theorem 6(a), p. 232: every generated policy's upper bound by the fixed point, terminal-tail passage, generated stationary approximation and the epsilon(1-beta) residual condition. |
| blackwell-stationary-prior | blackwell.stationary.prior | Theorem 6(b), p. 232, and 6(c), pp. 232–233: prior-stationary epsilon allocation, jointly measurable parameterized continuation policies, exact mean selection, error epsilon/(1-beta), all-state scope, epsilon = 0 and beta = 0. |
| blackwell-general-verification | blackwell.general.verification | Theorem 6(d)–(f), pp. 232–233: full arbitrary-history verification by iterated kernel telescoping; the source's distinct Dirac-prior/stationary reduction; uniform Cauchy sequence of 1/n-optimal returns; generated fixed-point bridge; every inequality in the value equation; both directions of policy optimality; separately proved uniqueness of bounded Borel solutions. |
| blackwell-essential-optimum | blackwell.essential.optimum | Definition preceding Theorem 7, pp. 233–234, and Theorem 7(a)–(b), p. 234: source strong equivalence, proved operator-equivalent variant, countable covering equality of operators, all-policy value, finite covering with state-dependent bound, attained first-maximizer partition, countable/finite common action cases, and full general operator-equivalence criterion. |
| blackwell-general-improvement | blackwell.general.improvement | Theorem 8(a)–(b), p. 234: Howard monotone replacement and Eaton–Zadeh switching, exact restart semantics, both intermediate inequalities, Borel comparison/tie partition and uniform fixed-point limits on the original general state/action domain. |
| blackwell-borel-examples | blackwell.borel.examples | Editorial worked applications of Theorems 6–8: continuum of fixed states with countable unattained choices and exact iterates/errors; arbitrary Borel reward discontinuity with two actions; and strict switching improvement in an alternating two-state model. |

The thirteen proof labels are exactly the destinations of the thirteen body results; this is a manually supplied mapping, not an automated acceptance report.

## Necessary mathematical dependencies and their actual interfaces

The active P15 files were read at their needed full extents:

- handbook/parts/p15/regular-conditional-laws.tex and its annex: thm:p15-standard-conditional-law, thm:p15-value-conditional-law and thm:p15-kernel-joint-measure. Their full proofs construct regular conditional kernels from rational CDF versions, Borel real coding and common good sets; disintegration on the observed-value space; a.e. uniqueness as measures; and joint measurable kernel integration by sections and a pi-lambda argument.
- handbook/parts/p15/countable-product-measures.tex and its annex: thm:p15-metric-borel-representation and thm:p15-coded-space-extension. The exact codings have Borel images and measurable inverses. Countable extension is transported from the proved real-coordinate law after a full concentration argument. Here it is used only for a countable sequence of standard Borel coordinates with explicitly proved consistency.
- handbook/parts/p17/sequential-decisions.tex and its annex: thm:p17-sequential-contraction. Its full complete-space proof explicitly covers all bounded real functions on an arbitrary set and the closed subspace of bounded functions measurable for a specified sigma algebra. It supplies the fixed-point theorem here once preservation of M(S) is proved; the finite MDP's selector is not imported.

The new factorization proof adds the parameter-kernel argument that cannot be replaced by choosing an unrelated probability measure separately for each initial state: all finite cylinder probabilities are measurable in the parameter, and the events with measurable probability form a lambda-system containing the cylinder pi-system. It also proves jointly measurable continuation values needed at Theorem 6(c)'s null prefixes.

The positive-section proof is an independently worded complete reconstruction of the missing selector dependency. It does not appeal to an unproved measurable-selection theorem or to dense rational actions. Its sequence is:

1. Prove open-subspace complete metrizability using reciprocal distance to the complement.
2. Make a closed set clopen by a Polish disjoint union with its open complement.
3. Combine countably many finer Polish topologies using the closed diagonal in their countable product; verify both completeness and unchanged Borel sigma algebra.
4. Prove by a sigma-algebra argument that every Borel set, or countable collection of Borel sets, admits this clopen refinement.
5. Put a Polish topology on the Borel graph D and refine it so the projection into X is continuous. Its actual point fibers are closed.
6. Normalize the given kernel on each positive section, producing a Borel graph-space kernel supported on that closed fiber.
7. Select the first positive-probability ball at each shrinking nested step. Prove index measurability, Cauchy convergence in the graph space, Borel measurability of the limit and membership in the closed fiber.
8. Apply that construction to the explicitly positive section defined by the mean and essential supremum, treating equality of those two numbers separately.

The non-Borel-projection prerequisite is also proved in full here. Closed-projection analytic sets are shown closed under countable unions and intersections by explicit witness encodings. A sigma-algebra argument then puts all Borel sets in that class. An actual universal closed relation indexed by finite-prefix codes yields the diagonal non-Borel projection. The previously proved Borel real coding transports the relation into [0,1]^2 without assuming its image is Borel. The image is proved Borel using the measurable inverse on a Borel image.

These auxiliary constructions use ordinary countable choices in the manuscript's classical set-theoretic setting; they do not assume a Borel axiom of choice.

## Corrections, qualifications and source-route distinctions

1. **Signed tail, original p. 229.** The source's two-policy estimate omits a factor 2. Both tails are retained in the active formula 2 R beta^N/(1-beta). The backwards replacement proof uses the corrected bound before allocating the remaining epsilon among N replacements. The finite chapter already contains a sharpness example.
2. **Source selection, original p. 228.** Both conclusions are pointwise for every conditioning argument. The second null event uses >=, so the selector is chosen strictly above essential-supremum minus eta. The mean-equals-essential-supremum case has probability-one equality and is handled separately. No almost-everywhere-in-x weakening is introduced.
3. **Prior quantifiers, original pp. 229–230 and 232.** The kernel eliminating history is conditional under a specific current prior law. Its resulting policy is only claimed to dominate the chosen policy rho-almost everywhere. For optimality, each competitor may have its own null exceptional set. The body distinguishes this from one policy uniformly good at all states.
4. **Theorem 6(c), original p. 232.** The printed statement includes epsilon = 0; extraction misreads the relation. The full proof keeps the exact mean inequality from selection, so the optimal-policy-implies-stationary-optimum conclusion is actually established.
5. **Theorem 6(d), original p. 233.** The source's stationary reduction is retained with its fixed-state Dirac prior and arbitrary positive tolerance. A separate direct telescoping proof gives the all-history policy-class argument through actual kernels. Neither proof assumes unrestricted Borel maximization.
6. **Uniqueness, original remark on p. 233.** The source reports uncertainty about uniqueness of a bounded solution even under 6(e). The reader treatment proves uniqueness among bounded Borel solutions directly by comparing two actual solutions with the beta norm inequality. It does not claim that the uncountable supremum maps every bounded Borel input back to a Borel function. In Example 2 the unrestricted value itself is non-Borel.
7. **Action equivalence, original p. 234.** The displayed equality of transition laws and pointwise reward functions is retained as strong equivalence. The printed identification with equality of action operators is too strong in one direction. The reader treatment proves the correct criterion: equal expected immediate rewards and equal transition measures for beta > 0; only equal expected immediate rewards for beta = 0. Both original strong-covering hypotheses remain sufficient. The additional operator-equivalent covering version is explicitly distinguished and proved.
8. **Graph-state union, original p. 230.** The graph and base state spaces are tagged, making their disjointness and Borel structure literal. Every off-path reward is specified, and the memory separation retains beta > 0.
9. **General improvement, original p. 234.** The source's weak inequalities and tie branch are kept. The Eaton–Zadeh value can strictly exceed the pointwise maximum; the alternating example proves this. An equality claim would be false. Howard's construction is explicitly defined with a restarted policy; the history-policy extension is proved through its kernel identity rather than inferred from ambiguous concatenation notation.
10. **Countable-action interpretation, original p. 233.** The new countable model uses integer n as the choice of f_n(s). Both directions on deterministic Markov maps are defined through Borel partitions, and the equality of state/reward laws is proved. Multiple indices may name the same original action.
11. **Effectiveness.** Theorem 1 chooses a sequence approaching an integrated supremum over all policies, as the source itself calls nonconstructive. The graph-space selector uses complete Borel constructions without promising a computable presentation from arbitrary Borel input. Finite arithmetic algorithms retain their separate exact-input domain in the earlier finite chapter.

No existing reader file was edited. The corresponding corrections already present in the finite chapter are consistent with this general treatment.

## Acquisition leads, actual access outcomes and remaining source presentations

The complete 1965 article is held and its assigned mathematical development is supplied. The following exact separate works are not thereby acquired or fully presented:

- Blackwell1964, Memoryless Strategies in Finite-Stage Dynamic Programming, Annals of Mathematical Statistics 35, 863–865, DOI 10.1214/aoms/1177703586. This is the 1965 selection lemma's reference [2]. The Celebratio collection https://celebratio.org/Blackwell_DH/article/248/ has an abstract and a Read PDF control whose returned target was only https://celebratio.org/media/ and failed. The DOI publisher lead returned an access incident; the direct publisher PDF lead did not yield a readable body. Celebratio's issue number 3 conflicts with Berkeley's bibliography and other records indicating issue 2; an original body has not settled this metadata here. No PDF or bibliography entry is fabricated from that lead.
- Blackwell and C. Ryll-Nardzewski1963, Non-Existence of Everywhere Proper Conditional Distributions, Annals of Mathematical Statistics 34(1), 223–225, DOI 10.1214/aoms/1177704259. The exact source identity is listed in the primary-author bibliography at https://celebratio.org/Blackwell_DH/article/254/. A publisher PDF lead returned an iframe response, not a readable PDF body. A secondary reference identified its Theorem 2 as a positive-section selector lead; that secondary description was not used as a proof or as evidence that the full original was acquired.
- Loève1960 Probability Theory, reference [7], is the source's background for Section 2. The necessary mathematical kernel, factorization and countable-product content is supplied by the explicit active P15 proofs. The complete separate Loève edition is not claimed read or reproduced.
- Dubins–Savage1963 dittoed draft How to Gamble If You Must, source reference [3]; Howard1960 Dynamic Programming and Markov Processes, source reference [5]; Eaton–Zadeh's original pursuit paper, source reference [4]; Karlin1955, source reference [6]; and Bellman's 1957 Dynamic Programming book, source reference [1], remain distinct source presentations. The self-contained proofs of the 1965 paper's stated results do not count as full acquisition or transcription of those works.

No new exact primary was successfully acquired in this block. The new topology/selector and universal-relation arguments are supplied mathematical proofs supporting the held 1965 statements; they are not attributed as a reading of the unacquired 1963 or 1964 proof bodies.

There is no unfinished mathematical dependency in the assigned Blackwell1965 chain. Wider sequential-decision obligations remain: general undiscounted/average reward, unbounded reward, partial observation, universally measurable policies and analytic-state formulations, stochastic shortest paths, learning transitions, and the other separately identified original sources. None is closed by this bounded discounted Borel-policy chapter.

## Routes, notation and bibliography intake

Integrated on 9 September 2026 as P17.15 in both active reading drivers.
The canonical Blackwell1965Discounted key is reused and ten typed notation
rows are merged. The finite sequential-decision method now links to this
complete general Borel treatment. All thirteen authored pairs retain their
pointwise or prior-dependent quantifiers. Consolidated reviews and admission
remain pending.

Root can route the body and annex as a general continuation after the finite sequential-decision and original Bellman constructions. Chapter label: sec:p17-blackwell-general-discounted. Annex section: sec:annex-p17-blackwell-general-discounted. Parent requirement: D3.

No new bibliography key is required. Reuse Blackwell1965Discounted, already identified and integrated through the finite sequential unit.

New locally bound notation for shared symbol intake:

- X,Y and other standard Borel spaces; M(X), P(X), Q(Y | X); k and its integrated action kv; product factorization p k.
- S,A,q,r,R,beta; histories H_n,h_n; random states S_n and actions A_n; policy kernels pi_n; deterministic maps f_n; stationary f-infinity; future kernel K^pi; return I^pi; initial rho.
- Prior and uniform epsilon optimality; epsilon-domination; rho-optimality; tolerance eta and truncation N; conditional action kernel kappa_i; later return V_{i+1}; discounted local contribution w_i.
- Borel relation D and sections D_x in selection; its projection p; refined topologies tau_n; the diagonal Delta; complete metrics d,d_O; graph probability nu_x; closed fiber F_x; nested balls O_n(x), centers c_n(x), limit z(x); selector f.
- Local mean a(x), essential supremum m(x), and the selection relation; the mean a is a local real function, distinct from a model action a.
- Baire space calligraphic N, finite-prefix enumeration e, universal closed relation calligraphic F, universal projection U, diagonal E, closed B_0 and coded unit-square B; phi and its Borel image J. This local U is a set relation in the counterexample proof, distinct from the generated value operator later.
- Stationary operators T_f,T_a; generated sequence (f_n), its Borel pieces E_n; generated operator U and fixed point u-star; generic operator B in the contraction assertion; terminal payoff u; finite-horizon loss d_i; countable model q-hat and r-hat; restarted policy (g,pi) and parameterized continuation pi-star_{s,a}.
- Optimal return V; approximation values v_n; expected reward rbar_a; essential finite pieces E_m; first-maximizer pieces B_n; switching map h.

All multiple roles are explicitly local. In particular the relation B, generic contraction operator B and first-maximizer sets B_n are different typed objects and must not be collapsed into one role.

Source-reading skills used personally: research and pdf. Their instructions governed primary/version capture and source-only PDF reading. The user's authoring sequence governed actual LaTeX writing and the single whole-batch author read-through.

## Frozen authored files

- Body: 18671 bytes; SHA256 79980EDC42A734F835E051A6244A8F52C56155C16B84D9A3900429F5DFA79957.
- Annex: 40407 bytes; SHA256 9EAE971020C901154EF41596D7ED6A58B4BD05A8DB1BC483E4E23ADD9EDE0E75.

The final author pass includes the explicit product-sigma-algebra/topology bridge, complete metric on the countable ambient product, initial probability kernel, mean-equality case, empty closed-set case in the limit-map proof, exact finite/common-action interface, countable generated-index bridge, and the source's alternative verification proof. Newly inserted paragraphs were read back from the actual saved files. The body and annex above are ready for root integration and the later consolidated reviews required by the governing workflow.
