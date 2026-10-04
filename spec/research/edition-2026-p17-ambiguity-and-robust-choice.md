# Ambiguity and robust choice: author return for P17 / D2

## Delivered component

Saved the complete assigned ambiguity comparison in:

- handbook/parts/p17/ambiguity-and-robust-choice.tex
- handbook/annex/p17/ambiguity-and-robust-choice.tex

The reader treatment contains the original two-urn comparisons, the marked 200-ball construction and full pasting proof, Arrow's variant and proof, the 30-red/60-black-or-yellow construction and exact subjective-expected-utility contradiction, the original sampling qualifications, and a careful account of the nonexperimental observations. It also supplies a fully specified finite-set-of-priors maxmin method, its genuine formal properties, robust dominance, all worked urn values, randomization and fixed-prior averaging, Ellsberg's own confidence-weighted rule and numerical tables, and the precise regret-menu boundary.

There are 12 genuine formal result/proof pairs. Descriptive reports, philosophical qualifications and source commentary are prose with source citations; they are not counted as mathematical theorems.

One whole author read-through of the actual body and annex was completed, with its local corrections saved in the same batch. No independent review, scanner, test, build or manuscript render was run. Source PDF images were used to read the original tables and formulas. Root owns all shared integration and every previous unit. This return does not grant independent acceptance.

## Exact acquired originals

### Ellsberg1961

Daniel Ellsberg, Risk, Ambiguity, and the Savage Axioms, The Quarterly Journal of Economics 75(4), November 1961, 643–669. DOI 10.2307/1884324. The original identifies The RAND Corporation, Santa Monica, California.

- Original: source/references/ellsberg-1961-ambiguity/Ellsberg-1961.pdf
- Direct university-hosted source: https://sites.socsci.uci.edu/~bskyrms/bio/readings/ellsberg.pdf
- Publisher identity: https://academic.oup.com/qje/article-abstract/75/4/643/1913802
- SHA256: 229556CE959764DCD3932EF92D50BAC8775F2E9D80794BAA580A48CB4E6973D9
- Size: 2015781 bytes.
- 27 physical pages; physical page = printed page minus 642.
- The held PDF is the complete journal body, without a separate archive cover. Its later PDF metadata dates do not change the identified 1961 publication version.
- Reading text: tmp/pdfs/p17-ambiguity/ellsberg1961.txt.
- Source-only image ranges: ellsberg-cases-08.png through -14.png and ellsberg-rule-22.png through -26.png.

Personally read the entire original pp. 643–669. This includes all introductory arguments, every urn variant and footnote construction, P1/P2/P4 discussions, qualitative-probability properties, response/interview qualifications, all of Section III's decision-rule discussion, the numerical tables, and the final normative qualifications. Original images of pp. 651–652, 654–656, 664–665 and 667–668 were read to verify the exact tables, experimental disclaimers, color-index discrepancies and confidence formulas.

The frozen target was established before writing: preserve the original experiment and menu for each comparison; use a common nonconstant consequence utility for the additive contradiction; retain both strict orientations and the all-indifferent boundary; prove the marked/Arrow pasting chains; preserve the original confidence-weighted construction and its different information assumptions.

### Gilboa–Schmeidler1989

Itzhak Gilboa and David Schmeidler, Maxmin Expected Utility with Non-Unique Prior, Journal of Mathematical Economics 18(2), 1989, 141–153. DOI 10.1016/0304-4068(89)90018-9. The original title has no article before non-unique prior. Submitted December 1987; accepted August 1988.

- Original: source/references/gilboa-schmeidler-maxmin/Gilboa-Schmeidler-MMEU.pdf
- Direct author-hosted URL: https://www.tau.ac.il/~igilboa/pdf/Gilboa_Schmeidler_MMEU.pdf
- Actual author page linking that PDF: https://www.tau.ac.il/~igilboa/Personal/Journal_Articles.html
- Publisher identity: https://www.sciencedirect.com/science/article/pii/0304406889900189
- SHA256: 627AF622F540003F8041CBB00BB383E000D0C9AE2C8868E436E3EFEEBA701B3F
- Size: 1418381 bytes.
- 13 physical pages; physical page = printed page minus 140.
- The first original page confirms title, both authors, Journal of Mathematical Economics 18 (1989) 141–153, and the submission/acceptance dates.
- Reading text: tmp/pdfs/p17-ambiguity/gilboa-schmeidler-mmeu.txt.
- Exact required reading images: gs89-01.png through gs89-05.png.

Read the full relevant source extent pp. 141–145 in the original images: the urn interpretation and min-over-priors rule; its distinction from Choquet-core special cases and minimax regret; the actual X/Y/S/Sigma/L0/Lc domains; pointwise mixtures; axioms A.1–A.6; and the complete scope of Theorem 1. The source's u is affine on roulette lotteries Y; its C is a nonempty weak-star closed convex set of finitely additive probabilities on an algebra, and its main representation is on finite-step measurable acts L0.

The exact finite bridge is in the body: X=Z, Sigma=2^S, Y=Delta(Z), L0=Y^S, and source lottery utility u-hat(y)=sum_z y(z)u(z). Replacing the supplied finite prior list by its convex hull changes no minimum; the new annex proves that hull closed and proves countable additivity on the finite state algebra. No general representation converse or source prior-uniqueness theorem is claimed from this bridge.

The extracted later source pages were consulted to identify the continuation: Section 3, pp. 145–149, contains the main representation and uniqueness proof through Lemmas 3.1–3.5; Section 4, pp. 150–152, contains Proposition 4.1's extension and Proposition 4.2's product/independence construction. Their full mathematical reconstruction remains separately owed. The extraction has missing glyphs, so it is not counted as a complete source-image reading of those later proofs.

Two unsuccessful earlier downloads were accurately relabeled rather than retained as false PDF acquisitions: the HAL endpoint returned HTML, now tmp/pdfs/p17-ambiguity/gilboa-schmeidler-hal-access-response.html; the 1986 archive endpoint returned an empty file, now gilboa-schmeidler-1986-empty-response.bin in the same temporary directory. The complete 1989 author-linked journal article above is the source actually used.

## Twelve formal proof pairs

| Body label | Annex label | Supplied mathematics |
| --- | --- | --- |
| thm:p17-ambiguity-seu-benchmark | annex:p17.ambiguity.seu.benchmark | Exact pasting cancellation, binary-bet formula, complement/disjoint-union properties, and a counterexample to inferring a global representation from one indifference. |
| thm:p17-ellsberg-two-urns | annex:p17.ellsberg.two.urns | Both strict orientations, weak comparisons with one strict, and the all-indifferent boundary, without assuming numerical probabilities inferred from initial answers. |
| thm:p17-ellsberg-marked-arrow | annex:p17.ellsberg.marked.arrow | Every marked-urn common-column substitution and indifferent substitution; complete Arrow contradiction under P1 and P2. |
| thm:p17-ellsberg-three-colors | annex:p17.ellsberg.three.colors | Both sure-thing reversals and the exact common-utility additive contradiction, with no risk-neutrality or unquantified approximation assertion. |
| thm:p17-finite-maxmin-properties | annex:p17.finite.maxmin.properties | Attainment, complete/transitive ranking, monotonicity, Lipschitz continuity, convex-hull identity and closedness, finite probability bridge, finite prior expansion, affine utility invariance and degeneracy. |
| thm:p17-robust-dominance | annex:p17.robust.dominance | Priorwise partial preorder, implication to maxmin comparison, exact strictness condition and explicit failures of completeness/converse/one-prior strictness. |
| thm:p17-maxmin-mixtures | annex:p17.maxmin.mixtures | Pointwise mixture identity, concavity, certainty independence, uncertainty aversion and explicit alpha/beta construction for source mixture continuity. |
| thm:p17-maxmin-full-independence | annex:p17.maxmin.full.independence | Full mixture independence iff a single distinct prior on the full lottery-act domain with nonconstant utility; proof using an event, its complement and a calibrated constant lottery. |
| thm:p17-maxmin-urns | annex:p17.maxmin.urns | Every original urn/marked/Arrow value, exact finite endpoint reductions, full auxiliary coupling polytope, and a continuum of different prior sets matching the same strict comparisons. |
| thm:p17-ambiguity-randomization-averaging | annex:p17.ambiguity.randomization.averaging | Fair color randomization under every composition, its changed-menu meaning, and the exact collapse of fixed prior averaging to one-prior expected utility. |
| thm:p17-ellsberg-confidence-rule | annex:p17.ellsberg.confidence.rule | Contracted-prior-set identity, both original numerical tables and effective priors, rho=0/1 cases, uniform convergence as rho approaches 1, optimistic variant and known-chance switching threshold. |
| thm:p17-ambiguity-other-criteria | annex:p17.ambiguity.other.criteria | Raw-state min/max/Hurwicz ties, exact original regret matrices, and a fixed-menu complete/transitive regret rule that violates sure-thing. |

## Original variants and qualifications retained

| Source extent | Original material and disposition |
| --- | --- |
| Section I, pp. 643–646 | Knight's risk/uncertainty distinction, Shackle's single-trial challenge, operational betting interpretation, preference versus belief identification, and descriptive/normative readings of axioms. The source's claim is about a pattern of choices satisfying constraints, not a proof that every uncertainty lacks numerical descriptions. This framing is retained in the reader introduction and source scope. |
| pp. 644 and 647–648 | Cricket illustration: an ace gives Australia first innings; any other die result gives England first innings; the later comparison uses a $10/zero bet and contrasts a coin. This is an original known-risk/operational illustration, distinct from betting on who will win a match. It is preserved here as part of the original conceptual presentation; the reader's general binary-bet theorem supplies its probability comparison when a fair die/coin model is specified. |
| pp. 648–650 | Qualitative-probability properties, P1 complete ordering, P2 common-column/sure-thing condition, P4 event-ranking independence from prize size, and the reference to P3 dominance. The reader proves the exact additive implications and defines the P2 premise used. This does not claim a full Savage1954 representation theorem or derive its omitted axioms. |
| pp. 650–651 | Urn I unknown red/black composition among 100 balls; Urn II verified 50/50; four offered pairwise comparisons. Within-urn indifference, known-urn preference, reversed preference and universal indifference remain distinct cases. Both nontrivial orientations are proved incompatible with one additive representation. |
| p. 651, footnotes 7–9 | The original does not offer free selection of both urn and color in one menu, and warns that randomization could matter under a changed menu. Color preferences and real-experiment complications are noted by the source. The reader proves the additional fair-coin act's constant success probability and keeps the menu change explicit. |
| pp. 651–652, footnote 1 | Marked 200-ball merged urn, six acts, three indifferences and the complete P1/P2 transformation chain. All six acts and the full proof are supplied. The marked experiment is not silently identified with the original choose-one-urn experiment. |
| p. 653 | Samples of two (one red, one black) or four (two of each) from Urn I; reported persistence of patterns and reduced reluctance. These are sampled-ball counts, not participant counts. The reader states the retained-choice conditional contradiction and does not invent a sampling/replacement protocol, posterior or population response curve. |
| pp. 653–655 | Three-color urn with 30 red and 60 unknown black/yellow; optional two-ball sample with one of each unknown color; four $100/zero acts and both strict response patterns. The literal act comparisons and complete proof are supplied. No-sample endpoint priors are explicitly limited to that information regime. |
| p. 654, footnote 4 | Arrow's four-act marked-urn comparison, two indifferences and A1>A2. The exact tables and the opposed consequences of transitivity and sure-thing are proved. |
| pp. 655–656 | Named examples of people who accepted the axioms, retained violations, or reconsidered; the source's account of reflective responses including Savage. The reader describes the categories without treating the names as a recruited sample or inventing participant counts. Source names are Debreu, Schlaiffer, Samuelson, Marschak, Dalkey, Raiffa and Savage, with different described responses. |
| p. 656 and footnote 7 | The original rules out raw-state minimum, maximum, fixed Hurwicz and pairwise regret explanations for the strict pattern. The exact finite calculations are supplied. Its blanket regret footnote requires the correction below. |
| pp. 657–661 | Ambiguity concerns the amount, type, reliability, relevance and unanimity of information, not just sample size or total ignorance. The known red fraction excludes many priors; evidence about the experimenter can affect estimates. Quantity of information can be high while evidence conflicts. These conceptual qualifications are retained. |
| p. 661 | R&D, an unfamiliar opponent, a new president, and a cricket novice illustrate conjectured ambiguity; the novice may assess a die/coin first-innings bet differently from a bet on winning the match. These are illustrative conjectures, not measured experimental findings. |
| pp. 661–664 | Best-estimate prior y0, reasonable-prior set, confidence in the information, security as worst reasonable expected payoff, objections about double counting and the conservative reply. The reader defines those inputs and distinguishes a minimizing prior from the person's asserted best belief. Maxmin is not declared the unique defensible response. |
| pp. 663–665 | Optimistic/maximax and fixed averaging alternatives; known-urn proportion 49:51; removal of a red ball; nonlexicographic tradeoffs; rho-weighted best-estimate/security index. The reader gives both alternatives, the exact fixed-averaging identity, the proposed index and a declared-input threshold q>rho/2. The one-red-removal remark remains a qualitative source example and is not assigned a fabricated measured threshold. |
| pp. 665 and 667–668 | Utility values 6/0, symmetric best estimate, confidence 1/4 and 3/4, two different worst-prior vectors and rho approaching 1. All original values and weight vectors are supplied with consistent colors. Uniform value convergence is proved; no statistical confidence-learning rule is inferred. |
| pp. 666–668 | Possible status-quo/innovation implications, potentially self-deceptive confidence, distinction between conservative decision weights and literal pessimistic belief, and comparison with Fellner's different proposed adjustment. These are the source's interpretive suggestions; the full Fellner presentation is separately owed. |
| p. 669 | Four proposed empirical claims: identifiable ambiguous information, violations by some otherwise reasonable people, deliberate persistence after reflection, and describable patterns. The paper leaves normative optimality open and acknowledges doubts about uniquely compelling rationales. The reader retains this boundary and makes no long-run superiority or unique-rationality claim. |

## Corrections made directly in the reader treatment

1. **Colors and indices.** The p. 655 probability footnote names coordinates red/yellow/black while using the black-bet formulas as though the second coordinate were black. The p. 665 table also exchanges the two unknown color names relative to p. 654. The active act definitions consistently use (R,B,Y); the later source table is connected by an explicit exchange of B/Y names. The numerical values and the symmetric reasonable-prior information are unchanged under that permutation.
2. **Marked-table label.** The transformation table on p. 652 repeats a BII label where the declared four-state order requires BI. The active table and proof retain (RI,BI,RII,BII) throughout.
3. **Exact versus approximate representation.** The literal strict pattern has no exact one-prior expected-utility representation. The source's unqualified phrase about rough or approximate representation is not promoted to a quantitative theorem without an error metric. The new uniform bound |W_rho(f)-E_p0(f)| <= (1-rho)D_u shows that values can approach one-prior values while strict urn reversals persist at every rho<1.
4. **Regret scope.** The p. 656 footnote's broad claim about all regret-based decisions is not valid without a menu convention. Pairwise regret matrices do tie the original pairs. A fixed-menu maximum-regret score gives a complete transitive order but can violate sure-thing; the active theorem proves a concrete two-state counterexample. No general impossibility of transitivity for regret is asserted.
5. **Information versus prior inference.** Finite physical urn compositions and a convex set of subjective one-draw priors are distinguished. Endpoint reduction is proved, rather than treating the 90-ball composition as literally a continuum of fractional balls. Neither symmetry nor a small balanced sample is declared to compel a uniform subjective prior.
6. **Axioms and domain.** Event-pasting sure-thing, constant-act mixture independence, full mixture independence and probabilistic independence are defined separately. Full independence's single-prior iff retains the nonconstant utility and full act-domain hypotheses. The finite model verifies forward A.1–A.5; it does not prove the general representation converse or identify C from four choices.

## Source and mathematics intake

Exact source-to-host bridge for the modern method:

- Finite state set S and finite consequence set Z are supplied.
- Affine lottery utility is u-hat(y)=sum_z y(z)u(z).
- All state acts are finite-step measurable on Sigma=2^S.
- Each listed p is a probability vector; its measure is countably additive because the state set is finite.
- C-hull is closed and convex, and min over C-hull equals min over the listed priors, proved explicitly.
- The method ranks by a given min functional and compares finite menus. It is not a proof that the six source axioms yield such a functional on arbitrary algebras.

Existing active interfaces read: def:p17-finite-lottery and thm:p17-lottery-reduction; def:p17-finite-bets, def:p17-bet-axioms and thm:p17-finite-bet-representation for the distinct monetary-additivity scope; def:p17-monetary-lottery for the declared utility/risk interpretation. No risk-neutral monetary utility is imported into the Ellsberg contradiction.

Chapter label: sec:p17-ambiguity-and-robust-choice.
Annex label: sec:annex-p17-ambiguity-and-robust-choice.
Computation entry: def:p17-ambiguity-computation.
Parent requirement: D2.

New local roles: S,Z,Delta(Z); f, g, h and pasted f_E h; common consequence utility u, state utility x_f and source affine u-hat; prior p and expectation E_p; H/L prizes; RI/BI/RII/BII bets and marked events; marked acts M1–M6; Arrow acts A1–A4; three-color acts F1–F4 and states R/B/Y; prior list C, menu M, maxmin V_C and its preference; robust dominance; sup norm; mixture lambda and continuity alpha/beta; point priors delta_i; urn sets C2/C3, composition theta, nonidentification d; auxiliary coupling coordinates a,b,xi,zeta; fixed prior-averaging weights w_j and pbar; best estimate p0, source confidence rho, W_rho and contracted C_rho; utility span D_u; and fixed-menu Reg_M. These are local chapter roles for root's symbol intake.

## Bibliography intake

    @article{Ellsberg1961Ambiguity,
      author = {Ellsberg, Daniel},
      title = {Risk, Ambiguity, and the Savage Axioms},
      journal = {The Quarterly Journal of Economics},
      volume = {75},
      number = {4},
      year = {1961},
      pages = {643--669},
      doi = {10.2307/1884324},
      url = {https://academic.oup.com/qje/article-abstract/75/4/643/1913802}
    }

    @article{GilboaSchmeidler1989Maxmin,
      author = {Gilboa, Itzhak and Schmeidler, David},
      title = {Maxmin Expected Utility with Non-Unique Prior},
      journal = {Journal of Mathematical Economics},
      volume = {18},
      number = {2},
      year = {1989},
      pages = {141--153},
      doi = {10.1016/0304-4068(89)90018-9},
      url = {https://www.tau.ac.il/~igilboa/pdf/Gilboa_Schmeidler_MMEU.pdf}
    }

Root should reconcile these keys with any existing catalog entries. No shared bibliography, symbol or driver file was edited.

## Remaining D2 and original-source boundary

The assigned original Ellsberg comparisons, their complete incompatibility proofs, and the stated finite maxmin method have no unsupplied mathematical dependency.

The following remain separate source presentations:

- Gilboa–Schmeidler1989 Theorem 1's general representation converse and uniqueness, including its utility representation premise, functional extension, separation construction and finitely additive measure machinery, pp. 145–149.
- Its Proposition 4.1 extension, and the product/independence definition and Proposition 4.2, pp. 150–152. Those are not the finite mixture-independence result proved here.
- Full Savage1954 axioms/representation; the original Ramsey, de Finetti, Knight and Shackle presentations; the full Anscombe–Aumann1963 construction; Bewley1986 incomplete preferences; and the separate empirical Chipman and later Ellsberg experiments.
- Hodges–Lehmann1952 restricted Bayes construction, Hurwicz's original generalized Bayes/minimax presentation, and Fellner's accompanying 1961 model. Their relationship to Ellsberg is recorded as reported source provenance, without claiming those primary bodies or proofs acquired.
- General minimax regret, Choquet/capacity models and their exact comparison with maxmin, ambiguity updating, dynamic consistency/rectangularity, elicitation and inference for prior sets, and measured prevalence/prediction across populations.

Ellsberg's normative discussion is preserved as discussion rather than converted into a uniquely-rational-rule theorem. No empirical participant count, frequency estimate, accuracy score or experimental validation was invented.
