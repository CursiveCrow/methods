# P17.10 — Finite strategic games and Nash equilibrium

## Completed authoring and source scope

The treatment supplies the full finite normal-form existence
theorem through both original Nash routes, with complete
fixed-point premises. It also supplies the 1951 paper's
Theorems 2–5, all six small source games, the dominance
perturbation and face-union result, the exact zero-sum minimax
comparison, and additional fully proved recommendation,
welfare and finite-accuracy boundaries.

Sixteen reciprocal statement/proof pairs are saved and routed.
The source's separate three-person poker elimination chain,
its simply-connectedness assertion about undominated strategies,
and the negotiation applications are not included in that count.

Files:

- handbook/parts/p17/finite-strategic-games.tex
- handbook/annex/p17/finite-strategic-games.tex
- spec/research/edition-2026-p17-finite-strategic-games.md

Body: 21,495 bytes, SHA-256
04E2CFA174B251B8DC97BD249B6D7B969DC0BD8B66F15CAD5F865C9D222141A8.

Annex: 38,357 bytes, SHA-256
0F1AEB4823C43F7161576F5CE7E8CB9F912DAD197956E08A364F89E49790B961.

Chapter label: sec:p17-finite-strategic-games.
Annex label: sec:annex-p17-finite-strategic-games.

The original author saved both drafts before the account usage
limit stopped its turn. Root resumed locally, read the complete
body and annex, read both original papers and their relevant
source images, finished definitions and the zero-cost branch
of the approximation guarantee, and merged the source record,
bibliography, notation and routing. This was continuation of
writing, not an independent acceptance review.

## Held original sources

### Nash 1950

John F. Nash, Jr., Equilibrium Points in N-Person Games,
Proceedings of the National Academy of Sciences 36(1),
48–49 (January 1950).
DOI: 10.1073/pnas.36.1.48.
The note was communicated by S. Lefschetz on November 16,
1949; the communication date is not its publication year.

Canonical primary publication record:
https://pmc.ncbi.nlm.nih.gov/articles/PMC1063129/

Held original:
source/references/nash-1950-equilibrium/Nash-1950-equilibrium.pdf

Size: 207,636 bytes; two physical pages. SHA-256:
6C9CE718817AA8B4059D3E80492E0C74E1E74533F1D27BB31F7E185A89DCCA6A.

Canonical bibliography key: Nash1950EquilibriumPoints.
The first physical page also contains the ending of the
preceding article; the second contains the beginning of
Polya's next article. The entire actual Nash note, including
its footnotes and acknowledgment to Gale, was read within
those page boundaries. Neighboring article content is not
attributed to Nash.

### Nash 1951

John Nash, Non-Cooperative Games, Annals of Mathematics,
Second Series 54(2), 286–295 (September 1951).
The original states received October 11, 1950.
DOI: 10.2307/1969529.

Canonical publication record:
https://www.jstor.org/stable/1969529

Held original:
source/references/nash-1951-non-cooperative/Nash-1951-non-cooperative.pdf

Size: 784,117 bytes; eleven physical pages. SHA-256:
5C73C6BA86CB4F692D1A96992DC946587CB386E36AE5D525A0277EC8FC3FE631.

Canonical bibliography key: Nash1951NonCooperative.
The first physical page is a JSTOR capture cover dated
November 9, 2012. Physical pp. 2–11 are printed pp. 286–295;
printed page equals physical page plus 284 there.
The capture date and PDF metadata dates are not used as
publication dates.

The complete article was read, including every continued
proof, the dominance discussion, poker parameters,
applications, acknowledgments and bibliography. Actual
source images for physical pp. 4, 6, 7, 8, 9 and 10
were personally read. They identify the exact positive-gain
formula, solution definitions, all six payoff examples,
polyhedral inequalities, dominance-direction correction
and the separate poker formulas.
Images are retained under tmp/pdfs/p17-nash-source/.

Both originals had been acquired by the interrupted author.
Their local file identities and full source scopes were
verified during root's continuation. The canonical URLs
above identify the publications; no claim is made that
those were the interrupted author's precise download URLs.

## Reciprocal inventory

| Body suffix after thm:p17- | Annex suffix after annex:p17. | Supplied content |
| --- | --- | --- |
| mixed-payoffs | mixed.payoffs | Product normalization, separately affine expectation, uniqueness and positive affine payoff transformations. |
| best-response-geometry | best.response.geometry | All pure/mixed/support equilibrium equivalences, compact convex countering values, closed graph and polynomial equilibrium inequalities. |
| sperner-foundation | sperner.foundation | Full face-chain subdivision, common-face intersections, shrinking mesh, incidence argument and oddness lemma, including dimension zero. |
| brouwer-foundation | brouwer.foundation | Simplex labeling limit, Euclidean compactness premise, unique 1-Lipschitz nearest-point projection and every nonempty compact convex finite-dimensional domain. |
| kakutani-foundation | kakutani.foundation | The full needed closed-graph correspondence theorem from finite approximate selections and the proved Brouwer theorem. |
| nash-1950 | nash.1950 | The entire original countering-correspondence existence route. |
| nash-1951 | nash.1951 | The original normalized positive-gain map, both fixed-point directions and the independent continuous-map route. |
| nash-symmetry | nash.symmetry | Full automorphism-invariant equilibrium existence, with the actual nonempty invariant compact convex domain. |
| nash-subsolutions | nash.subsolutions | Maximal interchangeable products, existence via Zorn, closed convex factors, uniqueness/solvability equivalence and attained values. |
| nash-polyhedral | nash.polyhedral | The exact equilibrium slice inequalities and a complete finite-vertex proof for bounded polyhedra, including lower affine dimension. |
| finite-minimax | finite.minimax | Both minimax/existence implications, all optimal factor sets, common value, pure-saddle necessity for strong solvability and a counterexample to its converse. |
| nash-six-games | nash.six.games | Every pure and mixed equilibrium and payoff in all six original two-by-two games, all solution classifications and the exact perturbation calculation. |
| strategic-dominance | strategic.dominance | Finite pure-opponent criterion, exclusion, the correctly directed perturbation and the whole face-union conclusion. |
| product-and-correlation | product.and.correlation | Every recommendation-dependent randomized deviation, product-law equivalence and the explicit diagonal recommendation example. |
| strategic-welfare-boundaries | strategic.welfare.boundaries | Pareto inefficiency, scale-dependent aggregate rankings and the exact distinction among Nash profiles, Nash solutions and NM imputation sets. |
| finite-nash-approximation | finite.nash.approximation | Rational grid construction, rounding error, regret bound, finite candidate count and terminating accuracy guarantee. |

## Fixed-point premises and distinct routes

The 1950 countering correspondence is the product of best-response
faces. Its values, graph and domain properties are proved before
the correspondence fixed-point theorem is applied.

The 1951 map adds every positive pure-action gain to the
corresponding probability and normalizes by one plus the
sum of gains. At a fixed point, a supported action with
payoff no greater than the current average has zero gain
and positive probability. Its fixed-coordinate equation
forces all of that player's positive gains to vanish.
The converse is immediate from the explicitly supplied
deviation inequalities. No convergence of iterating the
map is inferred.

The host proof of the needed correspondence theorem uses
finite nets and continuous weighted approximate selections.
Closed graph plus compactness supplies upper approximation
near a fixed limit point; convexity brings the weighted
nearby values back near the value set at that point.
There is no assumption of a continuous exact selection.

The underlying Brouwer proof supplies all of its simplex
and general-domain premises. Barycentric subdivision is
verified using sorted coordinates and face-chain barycenters.
The parity argument proves the facet-incidence count.
Nearest-point projection is constructed and proved
1-Lipschitz before an enclosing simplex reduces a general
compact convex domain to the simplex case.

These are explicit host proofs of the required mathematical
interfaces. They do not claim to reproduce the separate
original historical publications of Sperner, Brouwer or
Kakutani.

## Completed examples and source corrections

All six source payoff arrays were read from the original
page images. The manuscript calculates the two complete
best-response differences for each array and solves all
sign and equality cases, including the boundary supports.
Game 1's unique mixture is (9/16,7/17), with payoffs
(-5/17,1/2). Game 5's mixture is (1/4,3/8), with payoff
(-1/4,-1/4). The pure equilibria and all remaining games
are included in the actual body and annex.

On printed p. 290, the subsolution paragraph refers to
condition (1). The required condition is interchangeability
(5). The manuscript defines and uses interchangeability
explicitly; it does not identify every subset of equilibria
as a subsolution.

On printed p. 292, the slice characterization refers to
Theorem 2 even though the relevant result is the product
structure in Theorem 3. It also misidentifies the preceding
inequality referral. The manuscript uses the proved product
theorem and the actual pure-deviation inequalities, including
the deviator equal to the varied player.

On printed p. 293, the final dominance perturbation sentence
reverses the direction: t_i'=t_i+rho(s_i'-s_i) dominates
t_i, when s_i' dominates s_i. The actual manuscript gives
this corrected direction, a strictly positive admissible
rho bound, and the full affinity proof.

The original statement that a strongly solvable zero-sum
game requires a pure saddle is retained as a necessity.
It is not turned into a biconditional: the matrix
[[1,1],[1,0]] supplies a pure saddle without strong
solvability.

The source's informal instability description for Game 6
is replaced by the exact gain epsilon(1-epsilon) at
(epsilon,epsilon). No unprovided learning or adjustment
dynamics is assumed.

The source's empirical tendency comment for Game 5 supplies
no participant count, protocol or observations. It is not
counted as an empirical study or used to prove equilibrium
selection.

The finite-accuracy theorem treats ML=0 separately and
returns a pure equilibrium immediately. Its grid-count
formula applies to the branch where k is actually chosen.
It does not imply efficient computation or an exact
finite representation of an arbitrary irrational
equilibrium.

## Notation intake and shared interfaces

- N, A_i, mathcal A, X, X_-i, mathcal A_-i, x_i, delta_a,
  P_x, u_i, U_i, x[j<-z_j]: players, finite actions,
  pure/mixed profiles, independent law, payoff data,
  expected payoff and sequential coordinate replacement.
- v_i, BR_i, mathcal B, mathcal E: pure best value,
  best-response face, countering correspondence and
  equilibrium set.
- Delta_d, d, F_k, b_F, lambda_j, mu_k, sigma, mesh:
  simplex, dimension, face chains, barycenters, original
  and subdivision coordinates and coordinate ordering.
- K, pi_K, S, R, dist, mathcal C, eta, delta, epsilon,
  z_j, w_j, theta_j, f_epsilon: compact convex domain,
  projection, enclosing simplex, correspondence and
  approximate-selection construction.
- g_(i,a), G_i, T_i, T, sigma, h_i: positive gains,
  normalization and game automorphisms.
- C, C_i, v_i^+, v_i^-: interchangeable set, factors
  and attained equilibrium payoff values.
- M, f, v, X*, Y*, e_a, e_b: zero-sum matrix,
  bilinear payoff, value and optimal factors.
- p, q, D_1(q), D_2(p), rho: the two-by-two game
  mixtures, best-response differences and dominance
  perturbation size.
- mu, d_i(b_i|a_i): joint recommendations and
  recommendation-dependent randomized deviations.
- M, L, k, epsilon, r(x): local payoff magnitude,
  dimension bound, probability grid, requested accuracy
  and maximum unilateral regret.

Local overloads are explicit: M is first a zero-sum
matrix and later a scalar magnitude bound; sigma is
used for a coordinate ordering in a simplex proof
and for a player permutation in the automorphism
definition.

The finite lottery, expected-utility and positive-affine
uniqueness interfaces are linked to their existing
P17 definitions and proofs. The NM/cooperative comparison
links to the existing P18 game and Lucas results.
P17's social-choice navigation now links this new chapter.

## Exact source continuations still owed

The source's assertion on printed p. 293 that the
undominated set is simply connected is not established
by the face-union proof. A separate topological argument
is still needed; the chapter does not assert it as proved.

The poker section on printed pp. 293–294 has been read,
but its behavioral/normal-form equivalence, all elimination
and contradiction cases, and the exact four-parameter
equilibrium/payoff calculation have not been authored.
The source refers to Nash and Shapley, A Simple Three-Person
Poker Game, Contributions to the Theory of Games,
Annals of Mathematics Studies 24 (1950), for the separate
ante/bet-parameter and coalition treatment. That original
presentation is a further required source treatment.

The negotiation application on printed p. 295 explicitly
admits an infinity of pure strategies. The finite-game
existence theorem is not asserted for such a game without
additional hypotheses. Its original bargaining and
extensive-game sources remain separate.

The recommendation and minimax consequences supplied here
are complete mathematical comparisons. The separate
original Aumann correlation and von Neumann minimax
presentations are not claimed reproduced.

The research and PDF skills supported source reading
and provenance. No independent review, test, scanner,
manuscript build, manuscript render or admission check
ran. All manuscript changes precede consolidated reviews.
