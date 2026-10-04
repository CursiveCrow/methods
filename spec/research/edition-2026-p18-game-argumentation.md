# P18-A1: Dung's game and matching correspondences

Author block: 8 September 2026, /root/kamp_lemma7_author. Eleven complete statement/proof pairs are saved. The direct Dung Theorems 37–39, the printed three-player examples and corrected one-population pairing construction are complete. The exact Lucas game, core and superadditive-domain bridge are also proved; its remaining nonexistence proof is explicitly not counted as supplied.

## Frozen owned files

| File | Bytes | SHA256 |
| --- | ---: | --- |
| handbook/parts/p18/game-argumentation.tex | 15910 | 46003FF8FF49CB17F902988640DA37B15C1072BF6EEDC37E47E93C0DE4EF6773 |
| handbook/annex/p18/game-argumentation.tex | 17690 | 6BBF44E95C484739A44C766454DB4999FE617C7B30B79738B7DAA4FDCF224DF0 |

The complete actual LaTeX body and annex received the author read-through, including the final superadditive-cover and Lucas-core additions. No independent review, scanner, test, build, manuscript render or acceptance run was performed. Existing files and shared drivers, symbols, bibliography and records were preserved.

## Exact primary scope and new captures

Dung 1995: the complete Section 3 passage, printed pp. 334–338, was read, including every game definition, both NM conditions, Theorems 37–39, the two three-player solution descriptions, strict complete matching lists, both directions of the matching proof and the five-person triangle discussion. Source pp. 335–338 were additionally read visually. The held original remains source/references/dung-1995/dung-1995-ai77-n-games.pdf, with frozen SHA256 C78EE6D0864CA18A882E6CF79BB1356EFD86F1D32B38B55570FB572E4651FBA3. Reuse Dung1995.

Gale and Shapley: D. Gale and L. S. Shapley, College Admissions and the Stability of Marriage, American Mathematical Monthly 69(1), January 1962, pp. 9–15. The full seven-page paper was visually read, ending before the following article on p. 15. The new manuscript uses the balanced complete-list marriage existence proof and the quota-one specialization of the proposer-optimality proof. Its n-squared bound counts individual proposals; it does not misidentify that bound with the source's sharper statement about stages.

Successful institutional original URL:
https://iqua.ece.toronto.edu/baochun/ece1771f/papers/Gale-Shapley-1962.pdf

Held original: source/references/gale-shapley-1962/Gale-Shapley-1962.pdf

Bytes: 206606. SHA256: 3971EC3E3B048B6ACE92248FCC8FA8F021808CA76CBC09D439275B8C0A07BB41.

Root should add GaleShapley1962 with the above identity and URL. The publisher record supplies DOI 10.1080/00029890.1962.11989827; the 2018 online date is digitization, not the article's publication year. The quota/admissions generalization, strategic reporting properties and other matching variants are not counted as complete merely because this source was read.

Lucas: William F. Lucas, The Proof That a Game May Not Have a Solution, RAND Memorandum RM-5543-PR, January 1968. This is the exact detailed original report, separately identified from the 1967 announcement and the 1968 three-page Bulletin announcement.

Official original URL:
https://www.rand.org/content/dam/rand/pubs/research_memoranda/2008/RM5543.pdf

Official identity page:
https://www.rand.org/pubs/research_memoranda/RM5543.html

Held original: source/references/lucas-no-solution/RM5543.pdf

Bytes: 409896. SHA256: FAC4A2A15C21D496D6446958EA3B92AC1420F721B8770FC0D6AADB849625A0E9.

The held PDF has 27 physical pages. The title, preface and summary were read; the complete substantive pp. 1–6 were then read visually. Printed p. 1 is physical p. 9, hence physical = printed + 8. The exact characteristic function and core construction on pp. 4–5 were frozen before their new definition and complete proof were written. Section 4, Partition of A, begins on printed p. 6 and introduces the index convention for twelve regions. The region definitions and subsequent nonexistence argument are the next unread/unwritten construction.

Root should add Lucas1968NoSolutionProof as a techreport, with author William F. Lucas, the exact title above, institution RAND Corporation, number RM-5543-PR, year 1968, month January and the official URL. This citation supports the definitions and core foundation actually read; it is not an admission of the remaining theorem.

All originals were preserved unchanged. Source images and attempted text extractions are under tmp/pdfs/p18-dung-games. The two new source originals are image-only; their extracted text is blank. The research/PDF workflow was used for exact primary reading, not manuscript output inspection.

## Complete reciprocal pairs

| Body label | Annex label |
| --- | --- |
| thm:p18-imputation-core | annex:p18.imputation.core |
| thm:p18-nm-argumentation | annex:p18.nm.argumentation |
| thm:p18-three-player-solutions | annex:p18.three.player.solutions |
| thm:p18-marriage-argumentation | annex:p18.marriage.argumentation |
| thm:p18-deferred-acceptance | annex:p18.deferred.acceptance |
| thm:p18-matching-assumption-boundaries | annex:p18.matching.assumption.boundaries |
| thm:p18-roommate-argumentation | annex:p18.roommate.argumentation |
| thm:p18-five-person-pairing | annex:p18.five.person.pairing |
| thm:p18-matching-welfare-boundary | annex:p18.matching.welfare.boundary |
| thm:p18-superadditive-cover | annex:p18.superadditive.cover |
| thm:p18-lucas-core-foundation | annex:p18.lucas.core.foundation |

The unit gives efficient and individually rational imputations; finite-player superadditivity and actual coalition feasibility; both core definitions with an explicit extension of a blocking allocation to an imputation; the NM/stable equivalence and core = F(empty); preferred existence on potentially uncountable imputation sets; both three-player solution families and the exact fixed-share range 0 <= c < 1; strict finite matching and empty instances; deferred acceptance with both side-optimality claims; ties, unacceptable-pair and equal-infinite-cardinality counterinstances; the exact unordered-pair model and complete five-person calculation; and a stipulated-utility counterexample to aggregate-optimality inference.

## Direct source corrections and additional closed construction

Dung's one-population reuse of P times P does not encode a physical matching: the two coordinates behave as independent roles. With the source's top choices, the permutation consisting of (m,w), (w,m), (p1,p2), (p2,p3), (p3,p1) is a stable extension under the same-coordinate attack rule. It stays stable even if diagonal pairs are deleted. The new manuscript proves this counterinstance and defines the valid distinct unordered-pair graph explicitly.

On that corrected graph, all strict completions of the source's specified first choices have exactly the admissible sets empty and {{m,w}}. The latter is grounded and uniquely preferred, and no stable extension exists. It matches only two people although an ordinary matching can match four. Thus preferred maximal admissibility is not described as maximizing the number matched.

The source's coalition-feasibility sign is weak <=, as confirmed from its actual page. Equality is essential to the three-point solution proof. The source's second informal fixed-share description is made explicit as S_c = {(t,2-c-t,c):0 <= t <= 2-c}; its full stability range and both outsider cases are proved, including c = 0, 1 and 2.

Lucas's printed characteristic function is not superadditive: two disjoint value-one pairs can have a value-zero union. The new partition-cover theorem proves that superadditive closure preserves the entire imputation dominance graph whenever it preserves the grand-coalition value. For Lucas's exact table, every coalition value is at most its number of odd-numbered players, so the cover leaves grand value 5 unchanged. Singleton values also stay zero. The exact core is proved to be the five-dimensional pair-sum cube intersected with odd-coordinate sum >= 4, equivalently the convex hull of the six original listed vertices. This completes the domain bridge and core foundation needed before the remaining no-solution proof.

## P17 links and root integration

The approved work-package file identifies P17-D4 as games/best responses/equilibria/information and P17-D5 as aggregation/collective rationality; BR-05 links equilibrium and welfare. The actual finite-preference chapter was read in full.

Exact navigation connections to add when the P17 strategic chapter is written:

- From P17-D4's cooperative-solution comparison to def:p18-cooperative-game, def:p18-nm-solutions and thm:p18-nm-argumentation. The inputs are coalitional values and sets of imputations, not strategic action profiles.
- From P17-D4's matching/implementation examples to def:p18-marriage-model, thm:p18-marriage-argumentation and thm:p18-deferred-acceptance.
- From P17-D4/D5 and BR-05 to thm:p18-matching-welfare-boundary and thm:p18-five-person-pairing. These distinguish stability, side-optimality, Pareto comparison and maximum cardinality/aggregate utility.
- The new body already links back to sec:p17-finite-preferences; thm:p17-ordinal-boundary is the more specific existing uniqueness/intensity boundary to connect in the shared navigation.

No P17 route or nonexistent future theorem label was edited or invented. This unit does not by itself complete P17-D4's required Nash-equilibrium treatment.

Route the new body and matching annex after the existing P18 foundations. New local notation includes N, v, x(K), I(v), coalition and existential domination, core script-C, framework A_v, S_triangle and S_c, strict person-indexed preference orders, matching mu and its inverse, unmatched bottom, unordered pair set, ordered-role permutation, stipulated welfare sum U, superadditive cover v-hat, Lucas ell/O/Q_j/A_ell/B_ell and core vertices c^(2j).

## Exact remaining step

The direct Dung Theorems 37–39 and the source examples as corrected above have complete proofs. The remaining external construction is Lucas RM-5543-PR Section 4 from printed p. 6 onward: define every region and domination relation used in the partition/exclusion proof and prove that the displayed ten-player game has no NM solution. The new body explicitly keeps that nonexistence theorem unclaimed. Its characteristic function, superadditive transfer and full core formula are now proved prerequisites.

Gottlob's general ordinary-AEL translation, Konolige 1988/erratum, Dung Section 5 meta-interpreters and Dung 1991 remain their separate existing obligations. Shared integration, the two new bibliography keys and consolidated independent review belong to root.
