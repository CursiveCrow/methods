# P18-A1: Dung Section 5 argumentation meta-interpreters

Author block: 2026-09-08, starting 20:11:48 UTC; completed before the 20:56:48 UTC deadline. The exact source target was frozen before writing. The full owned body and annex were authored and received one whole-batch read-back of their actual saved LaTeX. This is an authoring handoff; independent review, scanners, tests, builds and manuscript renders were not run.

## Result and exact scope

The complete Section 5 construction is supplied: the two original processing clauses and extensional generator, the exact argument-name/grounding contract, all three parts of Theorem 62, the full signed grounded interpretation, the stable-model bijection, the well-founded/Fitting equality, the source's program-to-argumentation bridge through its literal support graph, and a proved edge specialization corresponding to the closing implementation remark. Ten statement/proof pairs include all needed domain, zero/empty, self-attack, infinite-attacker and limit cases.

The original two-rule program is named P^0_F and retains its own direct reduct proof. The guarded program P_D and sparse ground program Q_F are separately defined and connected to it by proved maps. Thus the source theorem is not replaced by an assertion about a different encoding.

No mathematical case in the assigned Section 5 chain remains open. Further program transformations suggested by the source are not automatically declared correct; the particular extensional edge specialization is fully proved here.

## Exact held primary and reading

Phan Minh Dung, “On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games,” Artificial Intelligence 77 (1995), 321–357.

- Original: source/references/dung-1995/dung-1995-ai77-n-games.pdf.
- SHA256: C78EE6D0864CA18A882E6CF79BB1356EFD86F1D32B38B55570FB572E4651FBA3, read again in this block and unchanged.
- Bibliography key: Dung1995; no new primary acquisition or bibliography entry is needed.
- Frozen target, read completely before the first manuscript write: Section 5 on printed pp. 348–350, physical pp. 28–30, through the paragraph immediately before Section 6. This includes C1/C2, both footnotes, the entire architecture figure, AGU/APU/P_AF, m(E), all three parts of Theorem 62 and its full printed proof, and the final partial-evaluation/program-transformation remark.
- Reread source prerequisites: Definition 13/Lemma 14 on p. 327; the exact support construction and Remark 48 on p. 343; reduct and Theorems 49–50 on p. 344; Theorem 55 and the Fitting operator/Theorem 56 passage on p. 346; the complete required Appendix B proof on pp. 352–354 and the completion definition in Appendix C on pp. 354–355.
- Reading derivative: tmp/pdfs/p18-dung-arbitrary/dung-1995.txt. Source-page images personally inspected: meta-source-28.png, meta-source-29.png, meta-source-30.png in the same directory. They are images of primary-source pages.
- Actual existing LaTeX read: the full used normal-program syntax/reduct, literal support/clause graphs, stable correspondence, unfounded-set and Appendix B interface, well-founded theorem, completion convention and Fitting theorem in logic-program-argumentation.tex and its annex; the used arbitrary-framework definitions, no-attack characterization, transfinite grounded result and proofs; the finite argumentation definitions and grounded procedure.

## Saved files and hashes

- handbook/parts/p18/argumentation-meta-interpreters.tex — 16867 bytes; SHA256 35D3921AC42D607129BD0448F3AC37B8631DF1E09233EFA1A26771C6DC28F3B2.
- handbook/annex/p18/argumentation-meta-interpreters.tex — 27229 bytes; SHA256 B6AB06ED57969C6BA5D1C1B1BC5EDAFB1CA1D253D3E5886A9A05D199FF542732.
- This note is the third owned file; its hash is provided in the final return.

All three owned paths were unused before creation. Existing and shared files were preserved.

## Ten completed proof pairs

Every body suffix below is prefixed thm:p18-meta-:

| Body suffix | Annex label | Exact completed content |
| --- | --- | --- |
| reduct | annex:p18.meta.reduct | Least model of every reduct, every extensional/dynamic atom, all three programs; Gamma(m(S)) = m(N(S)) and Gamma squared = m(F(S)). |
| stable | annex:p18.meta.stable | Both directions and inverse maps for stable extensions/models, including the original two-rule program and full total literal sets. |
| specialization | annex:p18.meta.specialization | All fixed background literals, every actual/nonedge/extra-name grounding case, full partial-model order isomorphism and least Fitting transport. |
| defense-steps | annex:p18.meta.defense.steps | All four successor quadruples, exact four-step identity, cofinal ordinal limits and grounded/Fitting equality. |
| completion | annex:p18.meta.completion | Every consistent partial fixed point is exactly L(E) for a complete E; preferred/maximal and stable/total correspondences in both directions. |
| positive-rank | annex:p18.meta.positive.rank | Full fixed-point equality of V and Phi under bounded positive rank, with all three interpreter rankings and arbitrary infinite clause sets. |
| full-correspondence | annex:p18.meta.full.correspondence | Correct full signed Theorem 62, both grounded directions, true/false/undefined cases, literal support/clause grounded bridges and both stable support-graph directions. |
| finite-procedure | annex:p18.meta.finite.procedure | Exact sparse program construction, finite grounded algorithm, stable enumeration, time/space and full-background-output qualifications. |
| boundary-examples | annex:p18.meta.boundary.examples | Single edge, isolated argument, extra names, empty framework, self-loop, mutual attack, classical-model substitution, predicate mismatch and non-defeat unit attacks. |
| infinite-input | annex:p18.meta.infinite.input | A decidable countable depth-one attack graph with undecidable acceptance, a unique stable/grounded answer, and total WFM/FM; full halting reduction and its diagonal premise. |

## Source corrections and exact replacement mathematics

1. The printed processing rule uses attack, while the generator and diagram use attacks. The active signature declares one binary atk predicate uniformly. The one-edge counterexample proves why distinct predicate symbols cannot be silently mixed.
2. The printed m(E) unions AGU clauses with atoms. The active construction takes the heads of extensional facts as the positive atom set B_D^+.
3. Theorem 62(2), p. 349, omits negative acceptance literals for arguments defeated by the grounded extension and negative nonedge facts. The full reduced signed output is L_Q(E) = acc(E) union defeat(E^+) union not-defeat(E) union not-acc(E^+). The guarded output adds the complete fixed background B_D, including false domain and dynamic atoms at extra names. The original source program uses the same formula with all domain literals erased.
4. The source proof's equality at every ordinal cannot hold as printed: at stage zero its left side already contains AGU when there is an edge fact, while grounded program-argument stage zero has no conclusions. It also omits the negative literals described above. The active proof supplies the actual four-step Fitting identity on Q_F, gives all successor quadruples and limit-union details, and transports the least fixed point through the complete extensional specialization. It does not retain a false equal-successor-stage claim.
5. The source proof says that every attack in its full support graph comes from a defeat conclusion. This fails even for the required negative unit arguments: a proof of acc(a) attacks the unit for not-acc(a). The complete literal support graph is retained, and the already proved Theorem 50/Appendix B interface is applied with its exact atom base and finite-body premises.
6. Distinct argument names in a Herbrand universe do not by themselves say that the universe contains only those names. The literal source program is therefore stated with D=A nonempty and an explicit signature including isolated names. The guarded extension is separately proved for arbitrary nonempty D containing A, including A empty. The missing-guard examples establish the necessity of this distinction.
7. The source leaves part (3) as “Obvious.” The new positive-rank lemma proves it completely: at a Phi fixed point induction on rank makes every unfounded atom already false; at a V fixed point every unfounded positive premise is false directly. Thus U=Z at either fixed point, and the operators have the same least fixed point. Negative attack cycles do not violate the required positive ranks.

## Symbols, dependency interfaces and routing

Route the new body and annex after the existing program and arbitrary-framework prerequisites. Body chapter label: sec:p18-argumentation-meta-interpreters. Annex section label: sec:annex-p18-argumentation-meta-interpreters.

New definitions: def:p18-meta-input; def:p18-meta-specialization; def:p18-meta-finite-procedure.

New local notation: D for the Herbrand domain; P^0_F for the source program; P_D for the guarded program; Q_F for the sparse ground program; H_F and H_P_D for their specified bases; a-circle = acc(a), a-bullet = defeat(a); B_D^+ for extensional fact heads; B_D for the full signed background; m_Q/m_D/m_0 for positive maps; L_Q/L_D/L_0 for signed maps; iota_D for background lifting; d_X for the defeat component of a candidate positive model; tau_alpha for the four-successor ordinal schedule. The annex's explicitly local quadruple (T,Z,D,U) describes acceptance truth/falsity and defeat truth/falsity; its D is a component, not the Herbrand domain in the separate program definition.

Reused exact interfaces: thm:p18-arbitrary-admissibility; thm:p18-transfinite-grounded; thm:p18-grounded-iteration; def:p18-program-reduct; def:p18-unfounded-operators; def:p18-completion-semantics; def:p18-source-program-graphs; thm:p18-program-stable-correspondence; thm:p18-unfounded-support; thm:p18-program-well-founded; thm:p18-clause-fitting. Their original graphs and completion truth-value convention are unchanged.

The finite procedure counts indexed-name operations with finite Boolean-array membership. Its grounded bound is O((n+1)(n+m+1)); stable enumeration is O(2^n(n+m+1)). Sparse dynamic output has n+m clauses and 2n atoms. Listing the full negative attack background over D=A can require quadratic output, and an infinite D gives an infinite background. The source-independent infinite example retains decidable R and proves why these are finite-input bounds.

Known existing reader navigation update for root: the final paragraph of handbook/parts/p18/logic-program-argumentation.tex currently says that the game correspondence and Section 5 construction remain separate source presentations. Replace that sentence with direct links to sec:p18-game-argumentation and sec:p18-argumentation-meta-interpreters while retaining that chapter's Section 4.3/Appendices A–C scope.

## Remaining source obligations

None in the assigned original Dung Section 5 chain. The broader autoepistemic translations and Dung 1991 remain their separately recorded obligations. Shared routing, symbols, proof-pair records and the eventual consolidated reviews belong to root.
