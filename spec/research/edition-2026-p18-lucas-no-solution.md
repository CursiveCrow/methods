# P18-A1: complete Lucas no-solution proof

Author block: 2026-09-08, starting 19:42:26 UTC; completed before the 20:27:26 UTC deadline. This is an authoring handoff. The complete source was read, the full owned body and annex were written, and their actual saved LaTeX received one whole-batch mathematical read-back. No independent review, scanner, test, build, or manuscript render was run. Integration and consolidated review remain root responsibilities.

## Exact question and result

Does the actual ten-player function in def:p18-lucas-game have no von Neumann--Morgenstern stable solution on its entire imputation space, and does the result transfer to its superadditive partition cover?

The complete answer is now supplied by nine statement/proof pairs. The source's regional route is retained: core dominion restricts a proposed solution to C union E union F; C union F cannot attack E; the three cyclic E regions have no relative solution. Explicit coordinate witnesses prove all G-region nonemptiness, predecessor identities and domination containments used in the contradiction. The optional F-immunity assertion and the Section 8 assertion that every positive coalition value is preserved by the cover are also proved. No remaining Lucas case or prerequisite is open in this assigned chain.

## Exact primary and read extent

William F. Lucas, The Proof That a Game May Not Have a Solution, RAND Memorandum RM-5543-PR, January 1968.

- Unchanged original: source/references/lucas-no-solution/RM5543.pdf.
- Official identity: https://www.rand.org/pubs/research_memoranda/RM5543.html.
- Official original PDF: https://www.rand.org/content/dam/rand/pubs/research_memoranda/2008/RM5543.pdf.
- SHA256: FAC4A2A15C21D496D6446958EA3B92AC1420F721B8770FC0D6AADB849625A0E9.
- Size: 409896 bytes; 27 physical pages; physical page = printed page + 8.
- Frozen current target, read completely before writing: printed pp. 6–18, Sections 4–8. Printed p. 19 references was also read. This includes all illustrations and their labels on printed pp. 8–10, the complete three-case core argument pp. 11–13, all incoming-region cases pp. 14–15, the complete cyclic geometry and contradiction pp. 16–17, and the superadditive continuation p. 18.
- Earlier source pp. 1–5 and the frozen actual game/core foundation are recorded in edition-2026-p18-game-argumentation.md. The actual LaTeX definitions, domination clause, core result, partition-cover theorem, and their full used proofs were read for this block.
- Reading derivatives: tmp/pdfs/p18-dung-games/lucas-14.png through lucas-27.png; these are source scan images, not manuscript renders. The original PDF is image-only; the blank text extraction was not treated as source evidence.
- Existing bibliography intake key: Lucas1968NoSolutionProof. No new primary or bibliography entry is needed. RM-5543-PR remains distinct from the RM-5518-PR announcement and the short Bulletin announcement.

## Saved files and hashes

- handbook/parts/p18/lucas-no-solution.tex — 11016 bytes; SHA256 B8824A0D6F6D09E1B9E66D8C90B33137FF000FFE59C87B10AF2482583C1E3035.
- handbook/annex/p18/lucas-no-solution.tex — 21395 bytes; SHA256 DC2F25195097D52838F83012E377C3EE347D265EC51C1671E5F26E379DCFB315.
- This note is the third owned file. Its hash is supplied in the final handoff.

The three target paths were unused before creation. Prior game files and all shared files were preserved.

## Exact proof pairs

Each theorem suffix below has body label thm:p18-lucas-SUFFIX and its listed annex label:

| Body suffix | Annex label | Completed construction |
| --- | --- | --- |
| region-partition | annex:p18.lucas.region.partition | Every E and F piece, disjoint five-part partition, all residual coordinate cases. |
| core-outside | annex:p18.lucas.core.outside | Explicit convex combination on each deficient pair, including zero coordinates. |
| core-remainder | annex:p18.lucas.core.remainder | Proportional slack construction, all five/four/three-player odd coalitions, both p/q orientations and the deficient triple with a coordinate equal to 1. |
| incoming-regions | annex:p18.lucas.incoming.regions | Exhaustive positive coalition list, C/F infeasibility or zero even coordinate, every F target, and the source's optional F-immunity claim. |
| cyclic-dominance | annex:p18.lucas.cyclic.dominance | Exact E_5 to E_3 to E_1 to E_5 relation, coalition payment 2-t+u+v, feasibility equality and zero-coordinate cases. |
| upper-regions | annex:p18.lucas.upper.regions | Explicit interior witnesses for nonempty G_h, both inclusions of every predecessor identity, and explicit dominators for the needed containment. |
| local-nonexistence | annex:p18.lucas.local.nonexistence | Full internal/external stability contradiction for arbitrary subsets of E. |
| no-solution | annex:p18.lucas.no.solution | Whole-imputation-space contradiction, nonempty unchanged core, and no stable argumentation extension. |
| positive-cover | annex:p18.lucas.positive.cover | Every positive coalition unchanged by the cover, exact graph bridge and no solution in the superadditive domain. |

The body also supplies worked numerical examples on the active feasibility plane, immediately beyond it, on a zero coordinate, at x_7+x_9=1, at the F_135 top face, and at the core boundary.

## Source corrections and expanded omitted calculations

1. Printed p. 12, case (i), ends with the even coalition 2,4,6,8,10 as the alleged domination witness. The preceding construction improves the odd coordinates and gives their sum 4. The correct witness is O = {1,3,5,7,9}, of value 4. The active statement and proof use O directly.
2. Printed p. 15, the F_135 paragraph, prints the first odd coordinates as 0 and then concludes that their paired evens are 0. The defining source region on p. 7 has x_1=x_3=x_5=1. The active proof uses that definition, yielding even coordinates 0.
3. The source's p. 16 statement that the G regions are nonempty and p. 17 predecessor/coverage assertions omit explicit coordinates. The new proofs supply delta=(1-z_7-z_9)/4, midpoint witnesses between z and a proposed predecessor, and epsilon=(1-x_7-x_9)/4 for dominators above any point of G_i. All witnesses stay strictly below the sum-1 boundary. No extra closure or attainment premise is introduced.
4. The optional F-immunity claim at the end of p. 15 is stated without proof by Lucas. Its complete coalition-by-coalition proof is now included; the final nonexistence contradiction does not depend on it.
5. The original function is not superadditive. The active theorem uses the already proved exact partition-cover bridge rather than importing the source game into a superadditive theorem without justification. The argumentation equivalence for the original graph is also established directly from internal/external stability definitions.

## Interfaces, symbols and routing intake

Insert the new body after game-argumentation.tex and its annex after the matching game annex. Chapter label: sec:p18-lucas-no-solution. Annex section label: annex:sec:p18-lucas-no-solution.

Reused exact premises: def:p18-lucas-game; thm:p18-lucas-core-foundation and annex:p18.lucas.core.foundation; def:p18-superadditive-cover; thm:p18-superadditive-cover and annex:p18.superadditive.cover. The ordinary game/argumentation correspondence is thm:p18-nm-argumentation, applied to the identical superadditive-cover graph when its declared game domain matters.

New local definitions: def:p18-lucas-regional-notation; def:p18-lucas-regions; def:p18-lucas-upper-regions. Chapter-local symbols are A=A_ell, B=B_ell, C=C_ell, H={1,3,5}, rho cycling 1 to 3 to 5 to 1, (i,j,k) cyclic, r=j+1, M_i={i,j+1,7,9}, (p,q)=(7,9) or (9,7), E_i and E, F_jk/F_p/F_79/F_135 and F, R, e_i(t,u,v), G_h(z), Dom_E and Pred_E. Pair subscripts F_ab are explicitly unordered. The coordinate map e_i has parameter domain [0,1]^3; each E_i and G_h imposes its additional strict conditions. Dom points from attacker to target; Pred_E collects possible attackers existentially.

Known direct integration updates in the preserved game body:

- In thm:p18-lucas-core-foundation, replace the final pending-construction sentences beginning “The subsequent proof that it has no NM solution...” with a reference to thm:p18-lucas-no-solution and thm:p18-lucas-positive-cover.
- Replace the final paragraph beginning “Lucas's separate ten-player nonexistence construction is the remaining external proof...” with: “The complete regional exclusion argument is supplied in \cref{sec:p18-lucas-no-solution}. It rules out an NM solution for both the original ten-player function and its superadditive cover.”

The strategic-reasoning link remains the original P17 distinction between coalitional NM solutions, Nash equilibria, matching stability and welfare. This unit closes the exact coalitional stable-set counterexample; it does not supply the separate strategic-equilibrium treatment.

## Remaining source obligations

None in the assigned Lucas RM-5543-PR proof chain. Dung Section 5 meta-interpreters, the broader autoepistemic translations (including the separate Gottlob and Konolige sources/erratum), and Dung 1991 remain their existing separate source assignments. Root still needs to route these files, update the stated pending reader paragraphs and record the new symbols and nine proof pairs before the eventual consolidated review.
