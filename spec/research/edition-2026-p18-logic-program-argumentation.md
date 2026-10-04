# P18-A1: Dung's logic-program argumentation constructions

Author return, 8 September 2026. Twelve complete statement/proof pairs are saved. The actual LaTeX body and annex received one whole-batch mathematical read-back; the tool-output truncation in the unfounded-set passage was followed by a complete read of that passage. No independent review, scanner, test, build, manuscript render or acceptance run was performed.

## Frozen owned files

| File | Bytes | SHA256 |
| --- | ---: | --- |
| handbook/parts/p18/logic-program-argumentation.tex | 18719 | 813F7548328C872EA39F105AF7D0EB4E3F979515B145F5FEC0A44E30BB9298FB |
| handbook/annex/p18/logic-program-argumentation.tex | 28576 | B8AC337A3E3A7BD4B20EDC7396637F1852A7C024AD4BA8FD46BE711A487915EA |

This note and the two paths were unused before writing. Existing manuscripts and all shared routes, symbols, bibliography and admission records were preserved.

## Exact source scope

The unchanged Dung 1995 journal primary is source/references/dung-1995/dung-1995-ai77-n-games.pdf, SHA256 C78EE6D0864CA18A882E6CF79BB1356EFD86F1D32B38B55570FB572E4651FBA3. Reuse Dung1995.

The complete target frozen before authoring was Section 4.3, printed pp. 343–348, including both literal graph definitions, Remarks 48/53, Theorems 49–52 and 55–58, Lemma 54 and Corollaries 59–61, together with the required Appendices A–C, pp. 352–355. Every relevant passage was read in full. Physical page = printed page minus 320. Source pages 343–347 and all four appendix pages were additionally read as images in tmp/pdfs/p18-dung-programs. Appendix B's complete finite-tree cases and Proposition B.2 are explicitly proved in the new unfounded-set item.

The earlier arbitrary-framework unit supplies the typed extension definitions, transfinite grounded construction, maximality, coherence and residual-extension results. The new proofs explicitly bridge every use back to those results.

## New exact Fitting primary and bibliography intake

Acquired unchanged from the author's publication-page link:

https://id144254.securedata.net/melvinfitting/bookspapers/pdf/papers/KripkeKleene-Sem-LP.pdf

Held at source/references/fitting-1985-kripke-kleene/KripkeKleene-Sem-LP.pdf.

SHA256: 7814044D863544DCFAB821A46E1B13AE05C099970440AFFED04ACE6980646E2C

Size: 428953 bytes; 18 image-only journal pages. Identity: Melvin Fitting, A Kripke-Kleene Semantics for Logic Programs, Journal of Logic Programming 2 (1985), 295–312. The author's publication listing and the actual title page agree. Read actual pages 295–303, including the complete needed Kleene/signed-interpretation and partial-completion definitions in Sections 2–5, pp. 296–301. The important definition on p. 300 uses a special connective requiring equal truth values, including undefined/undefined. It is not ordinary strong-Kleene biconditional. The later intrinsic-fixed-point developments are not being claimed as reproduced here.

Root should add the cited bibliography key Fitting1985KripkeKleene, with author Melvin Fitting, the title above, journal Journal of Logic Programming, volume 2, year 1985, pages 295--312, and the exact author-hosted URL. No DOI is required for this intake. Reading derivatives are the fitting-01 through fitting-09 PNGs under tmp/pdfs/p18-dung-programs; the attempted text extraction is blank because the original is image-only. The original was not edited.

## Reciprocal pair list

Each body label below uses thm:p18- followed by the left suffix; the exact matching annex label is shown.

| Body suffix | Annex label | Construction |
| --- | --- | --- |
| support-reduct | annex:p18.support.reduct | Finite proof trees, least positive models, all support/reduct directions |
| support-operator | annex:p18.support.operator | Exact literal support-graph no-attack and characteristic identities |
| program-stable-correspondence | annex:p18.program.stable.correspondence | Stable-model bijection, both directions |
| unfounded-support | annex:p18.unfounded.support | Greatest unfounded sets, full Appendix B tree path, saturation identity |
| program-well-founded | annex:p18.program.well.founded | Original/accelerated least fixed points and every ordinal stage |
| clause-completion | annex:p18.clause.completion | Completion truth convention; partial-model/complete-extension order isomorphism; maximal and total cases |
| clause-fitting | annex:p18.clause.fitting | Actual accelerated successor operator and equal Fitting fixed points |
| used-support-reduction | annex:p18.used.support.reduction | Literal/used-support complete-extension isomorphism with consistency guard; all semantics preserved |
| program-graph-transfer | annex:p18.program.graph.transfer | All signed walk, zero-walk, rank and finite-predicate cases |
| program-coincidence | annex:p18.program.coincidence | All semantic Corollary 59–61 directions, including signed skeptical queries |
| program-computability | annex:p18.program.computability | Finite clause matching, support semidecision, explicit universal-machine Horn reduction, finite graph algorithms |
| program-examples | annex:p18.program.examples | Delay, positive loop, unused-support fact and complete Appendix A omega + 1 calculation |

## Corrections incorporated directly

Theorem 56's printed same-ordinal successor identity is false: p <- not q, with no rule for q, gives first Fitting stage {not q} but first clause-graph conclusions {p,not q}. The new actual operator Psi uses the newly derived negative component inside its positive-body test. Phi and Psi are proved to have exactly the same fixed points, preserving the original least-fixed-point theorem.

The literal AF_napif support definition allows unused assumptions. Therefore the fact p <- has the self-attacking argument ({not p},p), refuting the literal graph conclusions of the printed stratified/strict/call-consistent transfer. The source graph remains unchanged throughout its stable and well-founded correspondences. A separately defined used-support graph has a fully proved complete-extension order isomorphism with it, parametrized by accepted negative units and an explicit consistency condition. Graph claims are stated only for the valid used-support or clause graph; their semantic consequences transfer to the literal source graph. The skeptical-query proof applies the residual lemma in the uncontroversial used graph, not in the possibly controversial literal graph.

Lemma 51's inference from an arbitrary non-total partial recursive function to an undecidable graph is not valid. The new proof gives an explicit finite Horn simulation of a fixed universal Turing machine and reduces its undecidable halting language to empty-support argument membership. It separately reduces semantic truth queries on definite programs, whose stable/preferred conclusion interpretation is unique. Undecidability of argument membership is not used as a bare implication about all semantics.

The exact Appendix A six-clause program is retained, with e as a declared abbreviation for even. Both graphs are non-finitary. All finite support-graph conclusion stages are calculated, followed by the precise addition of r and not p at omega + 1.

## Scope, symbols and integration

The semantic correspondences allow any set of ground clauses with finite bodies. The source's finite first-order program can have infinitely many ground instances. Effective membership and predicate-graph transfer claims keep their finite source-program hypothesis; finite extension enumeration requires a finite ground base and explicitly grounded program.

Route both new files after arbitrary-argumentation. New local symbols include H, Q = G_P, signed literals/l-star, I-plus/I-minus as truth components, total interpretation M-hat, positive T_D, reduct Gamma, graphs A_infinity/A_c/A_u, units nu_p, conclusion con, characteristic F_infinity/F_c, extension constructors E_infinity/E_c, unfounded U_Q, V_Q/W_Q, positive saturation T_Q-star, completion Z_Q/Phi_Q/Psi_Q and the signed predicate graph. I-plus is explicitly not the earlier attack-target superscript. Root owns all registry entries and the new Fitting bibliography key.

The prior arbitrary-argumentation unit's final continuation and research remainder can now point here for the formal Section 4.3 and Appendix A–C chain. Section 3 is the game correspondence; Section 4.1 is default/autoepistemic translation; Section 5 is the meta-interpreter construction. They remain separate assignments. The incidental identification after Remark 48 with Dung's 1991 preferential semantics refers to a different primary that was not acquired or proved equivalent in this block; no such external identity is claimed by the new manuscript. Consolidated independent review and shared integration remain with root.
