# Round 2 independent integrated-publication review: Part IX N-c-012

## Scope and review boundary

I independently read the complete current actual LaTeX file `handbook/parts/p09/presentations/n-c-012.tex`, directly from line 1 through EOF at line 3000. I did not open or rely on another review report or carry forward a prior verdict.

I also directly reread the current actual LaTeX in `handbook/parts/p09/logic-in-computer-science.tex` that controls this presentation: the reused LTL and past definition (`604-625`), the strict/inclusive bridge (`627-684`), the discrete-word and PSPACE theorem statements (`686-710`), the safety/liveness definition (`712-720`), the automata-theoretic method and theorem (`763-811`), and the input seam (`899-906`).

I did not inspect or create any manuscript PDF, PNG, page render, screenshot, or other derived manuscript artifact. I did not create or run a test, checker, repository script, TeX command, build, or hash operation. I did not edit the manuscript. This report concerns only the content of the two live `.tex` sources and makes no layout or final-publication claim.

## Outcome

The current revision resolves the five specifically identified former defects at their substantive sites. It nevertheless remains short of manuscript-content readiness for two independently observed reasons: one rendered acquisition-workflow phrase remains, and the named `\mathsf{ETL}` language is used in the complexity classification without an exact local formation definition satisfying the workspace five-part technical-name rule.

## Current verification of the five former issue classes

### Former PUB-01 — substantive digest and acquisition-log blocks removed, but one residual workflow phrase remains

The prior digest/PDF-offset style of source-object prose is absent from the current file. The current source introductions give concise bibliographic and rights boundaries at `n-c-012.tex:8-14`, `365-370`, `1201-1210`, `1838-1861`, and `2973-2985`; none prints a hash, physical-PDF offset, review-board result, test result, render status, or “read separately” claim. A complete current keyword-sensitive reread found no SHA digest, hash, checker, board, test-run, screenshot, or rendering-pipeline language.

The publication-language category is not entirely clear, however, because `n-c-012.tex:1642-1643` still says that “no separate acquisition record” is asserted. That residual is recorded as R2-PUB-01 below; it is not a reinstatement of the removed digest blocks.

### Former TERM-01 — resolved

`n-c-012.tex:480-489` now binds the source label `({\rm P1})` at the displayed reachable-state induction rule before the later uses at `697-706`. The label has a definite referent and no longer requires retrospective inference.

### Former TERM-02 — resolved

`n-c-012.tex:887-898` now defines `K_b` exactly as the pure propositional future theorem system with derived `F:=\neg G\neg`, G1--G3, and RT, RG, MP. The same passage states its standing as a theorem system, distinguishes it from `DX` and `DUX`, and explains the broader unnamed external system without conflating their axiom sets. Its later uses at `1020-1024` and `1112-1117` are consistent with that definition. Necessity, definition, standing, nonredundancy, and use are all locally supplied.

### Former BND-01 — resolved

The final boundary paragraph now calls Pnueli's `\leadsto` a “relation between state assertions” and says that it uses a strict later witness (`n-c-012.tex:2989-2992`). This preserves the standing established at `461-470`; it no longer recasts the statement family as an LTL operator.

### Former BND-02 — resolved

The final boundary paragraph now assigns the exact bridge to the handbook, not to GPSS: `n-c-012.tex:2992-2996` distinguishes GPSS's strict future language, the handbook-supplied strict past dual, the handbook's inclusive word language, and the need for `\mathsf X,\mathsf Y`. This agrees with the local ownership statement at `1259-1275`, the exact equations at `1292-1313`, GPSS's unresolved `\mathsf U^0` conflict at `1774-1801`, and the parent handbook translations at `logic-in-computer-science.tex:638-684`.

## Remaining must-fix findings

### R2-PUB-01 — A rendered “acquisition record” clause remains in the source-proof discussion

**Classification:** must fix for reader-facing publication tone.

At `n-c-012.tex:1634-1645`, the manuscript correctly explains that Theorem 2.3 is referred to an external Gabbay manuscript and that GPSS does not print the proof locally. But `1642-1643` adds that “no separate acquisition record or independent verification of that manuscript is asserted here.” The proof-ownership qualification is reader-relevant; the state of an acquisition record is an internal research-workflow fact. It neither narrows the theorem nor identifies who owns a printed proof.

The surrounding text already supplies the necessary scholarly boundary: GPSS makes an external referral, the external body is not imported as a local proof, and the construction is recorded only as a source outline (`1541-1548`, `1634-1645`). The minimum repair is therefore to delete “no separate acquisition record or” and retain only a directly stated proof-evidence limitation, or to delete the whole sentence and let the immediately following source-outline sentence carry the boundary. This finding does not treat mathematical uses of “verification,” “tests,” “accepts,” “reject,” or “renders” elsewhere as workflow language; those occur inside proofs and algorithm definitions.

### R2-TERM-01 — `\mathsf{ETL}` is named and classified without an exact local language definition

**Classification:** must fix under the workspace technical-name rule.

`n-c-012.tex:2428-2462` says that Section 5 calls its extended language `\mathsf{ETL}`, defines regular right-linear grammars, and gives the semantics of a grammar-indexed constructor `N_j(f_1,\ldots,f_n)`. The passage does not state an exact formation definition for `\mathsf{ETL}`: it does not say which prior temporal grammar is the base, which Boolean and temporal formation clauses remain available, or that the language is the least class closed under those clauses and all displayed grammar-indexed constructors. No other `\mathsf{ETL}` definition occurs in the current parent file or presentation.

The later use is load-bearing. `n-c-012.tex:2525-2536` states Theorem 5.4 for formulas with input grammars, and the complete classification table places `\mathsf{ETL}` in a PSPACE-complete row at `2580-2610`. The constructor's standing and its distinction from ordinary `U` are supplied at `2460-2462`, and later use establishes necessity, but those facts do not eliminate the named language class. As written, two readers can assign different base grammars to the same table row.

The minimal compliant repair is a local eliminable formation clause, for example: define `\mathsf{ETL}` as the least Boolean temporal formula class extending the explicitly named base fragment and closed under every constructor `N_j(f_1,\ldots,f_n)` associated with the displayed regular right-linear grammars, then give the already printed satisfaction clause. If the source does not determine that exact base and closure, the manuscript should instead say that an exact language definition is owed and should not use `\mathsf{ETL}` as a fully determined classification row. This is precisely the distinction the same presentation already enforces for GPSS's undefined `U',S'` at `1532-1539`.

## Interfaces and coherence that pass the current review

- **Definition and seam order:** the parent introduces inclusive `\mathsf Y,\mathsf S`, the discrete strict/inclusive translations, the first-order and PSPACE theorem interfaces, safety/liveness, and the relevant automata notions before `\input{parts/p09/presentations/n-c-012}` at `logic-in-computer-science.tex:903`. The presentation's backward references are therefore defined before the input seam.
- **Strict/inclusive separation:** Kamp's strict witness/open-interval semantics is explicit at `n-c-012.tex:74-98`; Pnueli's strict `\leadsto` and inclusive `F,G` are kept distinct at `461-478`, `668-676`, and `819-845`; GPSS's strict `\mathsf U_s`, handbook-supplied `\mathsf S_s`, and inclusive discrete bridge are separated at `1212-1313`; and Sistla--Clarke's inclusive current-point witnesses are explicit at `1863-1930`.
- **Model domains:** the presentation separately tracks Kamp's complete strict orders and rational counterexample (`16-40`, `133-165`), Pnueli's initial-state executions and arbitrary-start finite-state continuations (`618-676`, `1030-1062`), GPSS's point-zero omega, discrete-complete future, separation, and arbitrary-order packages (`1473-1539`), Sistla--Clarke's word and existential `R`-path problems (`1932-1970`), and Alpern--Schneider's full nonempty `S^\omega` domain (`2612-2654`, `2706-2709`).
- **Safety/liveness:** the exact bad-prefix and continuation quantifiers at `n-c-012.tex:2656-2684` support `logic-in-computer-science.tex:712-720`. Source lists of “safety” and “liveness” formulas are expressly kept separate from the later semantic property classes at `n-c-012.tex:1343-1348`.
- **Theorem ownership:** source statements, sketches, external referrals, and handbook repairs remain explicitly separated throughout. Representative boundaries include Kamp's parity correction (`272-341`), Pnueli's P2 and completeness counterexamples (`517-541`, `639-676`), GPSS's outline and missing event-expression translations (`1541-1645`), Sistla--Clarke's directed-cycle repair (`2177-2194`), and Alpern--Schneider's Corollary 2.1 repair (`2918-2951`).
- **Cross-presentation closure:** `n-c-012.tex:2987-3000` accurately closes all five presentations without introducing a new technical name or transferring a definition or proof from one source to another. Its distinctions agree with `logic-in-computer-science.tex:627-710` and with the safety/liveness definition at `712-720`.
- **Other terminology:** the remaining major local names generally satisfy the five-part rule. Examples include “tense-defining formula” (`42-72`), `\models_{\rm prop}` (`1051-1062`), `L_{\rm prop}(\Sigma)` (`1150-1165`), `\mathsf U_s,\mathsf S_s` (`1249-1313`), `DX,DUX` (`1647-1687`), and uniform versus absolute liveness (`2711-2751`). R2-TERM-01 is a bounded exception, not a reason to redesign those definitions.

VERDICT: REJECT -- R2-PUB-01, R2-TERM-01
