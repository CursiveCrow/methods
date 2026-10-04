REVISE

# Round-one mathematical/proof review: N-c-012.c GPSS 1980

## Reviewer, independence, and method

- Stable agent identifier: `/root/schmidt_smolka_1991_research`.
- Seat: mathematical/proof.
- Runtime model/version: not exposed to this reviewer.
- I read `spec/research/boards/p09-n-c-012c/charter.md` completely before the substantive review.
- I did not inspect `ledger.md`, `transcript/chair.md`, any other reviewer's transcript, or any other reviewer's verdict. I did not contact another reviewer.
- I authored the research note, so I did not treat it as self-validating authority. I visually reread the complete source body and judged the reader-facing claims directly against the page images. I then reread the complete source note as a frozen artifact and checked it against those images.
- I made no edit outside this transcript. I ran no test, test harness, automated checker, repository script, TeX command, handbook-PDF inspection, or build. The only executable operations were read-only file inspection, SHA-256 identity checks, source-PDF metadata inspection, source-page image inspection, and retrieval of the named author-archive record.

## Frozen identities

I recomputed every chartered SHA-256 before substantive review and recomputed all eight immediately before filing. Both passes returned the same values:

| Frozen object | Recomputed SHA-256 |
|---|---|
| `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf` | `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2` |
| `tmp/pdfs/p09-gpss-1980/page-08-quantifier-symbols.png` | `D74FF885AC1010EA703749F215D1E47DFB3649595F3F8C0A282E073DB714C0F9` |
| `tmp/pdfs/p09-gpss-1980/page-10-closure-crop.png` | `F49C546E4F07A005BA548AB594C6F63B01B37FC62FE3D8DD89A3FAE44EAEA434` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `986A5CFFE2DB209557CA9325ABFC2CD2F47D54FD06B20CE0DEED01E2EEF6CD8B` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `DAE8982D6CAA548BEBCB916B197399B6499A7C6DB966E6972CC4E2C50AC163BA` |
| `handbook/bib/handbook.bib` | `BB4096F50E3359E2F07187E1B898F8A8E65CF4A3AC3C288E3FA58099A2A53380` |
| `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` | `17A8A21420B1655E29B08F08C536FD12D8F5195907AAF14B44C902F439FDE152` |
| `spec/research/p09-source-presentations-lot2-3.md` | `78D6CE5D2B9BE4EE508407F738FC39AB294D1B26BD1677DA2492C9DAD5A42D57` |

No frozen identity mismatch occurred.

## Authority pages visually read

I visually read every complete source image `page-01.png` through `page-11.png`; these are physical PDF pages 1--11 and printed pages 163--173 without a wrapper. I used the images, not OCR or the prior note, to settle the formulas.

| Printed page | Material checked directly |
|---:|---|
| 163 | Four-author title and affiliations; ACM notices; abstract; execution sequence; informal strict `F`, `G`, `X`, and infix `U` clauses. |
| 164 | Initial grammar; model; clauses (1)--(5); literal past-pointing `F` inequality; one-sided `X` clause; strict `U`; omega-model; syntactic `L(U)`; eliminations of `F` and `X`; program-execution frame; partial correctness. |
| 165 | Total correctness; invariance and eventuality inventories; motivation for response strengths. |
| 166 | Insistence; equivalent formula; busy-wait example; weakest semaphore behavior; scheduler-fairness and infinite-overtaking qualifications; start of persistence. |
| 167 | Persistence; semaphore and guarded-region formulas and implementation qualifications; impulse; unsolicited-response example. |
| 168 | Unsolicited-response continuation; `Pr`; FIFO request/response and semaphore instance; repeated-response refinement; four questions. |
| 169 | Kamp and earlier-calculus attributions; first-order comparison language; model/order definitions and examples; natural forward translation. |
| 170 | Theorems 2.1--2.3; future-formula definition; proof-outline heading; `At`, `Bet`, special formulas, Lemma 1, and decomposition formula. |
| 171 | Main Lemma; Proposition 2.4; event-expression argument; printed 2.1/2.2 tension; Theorem 2.5; DX/DUX axioms and rules; Theorems 3.1--3.2. |
| 172 | Maximal-theory facts; finite closure; quotient and relations; transitive-closure lemma; ultimately periodic fair path; formal sequence condition and missing adjacency; truth lemma; decidability paragraph. |
| 173 | Strict-versus-earlier convention; `F^0`, `G^0`, weak `U^0`; transformed A/U schemes; `D^0X`, `D^0UX`; complete reference boundary. |

I additionally read the controlling p. 170 enlargement `page-08-quantifier-symbols.png`; the two restricted quantifiers are inclusive, `\(\forall y\ge x\)` and `\(\exists y\ge x\)`. I read `page-10-closure-crop.png`; its second closure premise is literally `\(Xw\in\Gamma\)`, with conclusion `\(X\neg w\in\Gamma\)`, not a premise `\(\neg Xw\in\Gamma\)`.

## Findings

### MP-F1 — must fix — the reader falsely says that the embedded metadata omits Stavi

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1208-1212`.
- **Reader claim:** “the file's embedded metadata omits Gabbay and Stavi.”
- **Authority evidence:** the embedded PDF `Author` field is exactly `A. Pnueli, S. Shelah and J. Stavi`; it omits Dov Gabbay but includes J. Stavi. Printed p. 163 names Dov Gabbay, Amir Pnueli, Saharon Shelah, and Jonathan Stavi. The official author-archive record also names all four. The frozen source note states the metadata fact correctly at `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:30-34`, and the frozen source-presentation ledger states it correctly at `spec/research/p09-source-presentations-lot2-3.md:171`.
- **Harm:** this is a direct C1 source-identity error and creates an internal contradiction among the reader, source note, and ledger. It also misdescribes the precise reason the printed title page must control.
- **Exact correction:** at line 1212 replace “omits Gabbay and Stavi” with “omits Gabbay.” Retain the printed four-author title page as controlling.

### MP-F2 — must fix — the reader never states the article's initial formula grammar

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1223-1234` and `1287-1289`.
- **Reader state:** the subsection begins with the model and semantic discussion, then later says that source `\(L(U)\)` is obtained by deleting `\(X,F\)`, but it never defines the initial grammar from which those constructors are deleted.
- **Authority evidence:** printed p. 164 explicitly introduces `\(L(F,X,U)\)` from atoms `\(q_0,q_1,q_2,\ldots\)`, classical connectives `\(\neg,\land,\lor,\supset\)`, and temporal connectives `\(F,X,U\)`, and defines `\(Gw:=\neg F\neg w\)`. Section 3 later changes the primitive presentation to `\(G,X,U\)` with `\(F\)` defined from `\(G\)`; the reader correctly records that later basis at lines 1622--1624, but that does not supply the missing initial grammar.
- **Harm:** C2 expressly requires exact syntax as well as semantics, and C9 requires definitions before use. Without the initial production inventory, `\(L(U)\)`'s source standing and the initial-versus-Section-3 primitive-basis change are not self-contained in the reader.
- **Exact correction:** immediately before or at the start of the paragraph at line 1223, state that the initial source language `\(L(F,X,U)\)` is generated from the `\(q_i\)` by `\(\neg,\land,\lor,\to\)` and `\(F,X,U\)`, with `\(GA\defeq\neg F\neg A\)`. Preserve the separate later statement that Section 3 instead takes `\(G,X,U\)` as primitive and defines `\(F\)`.

### MP-F3 — must fix — the busy-wait account drops the paper's fairness calibration and infinite-overtaking qualification

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1369-1381`.
- **Reader state:** the reader gives `\(\neg G(\mathit{at}_m\land x>0)\)` and explains that it prevents indefinite waiting while the enabling condition remains true, but it moves directly to persistence without recording how the source classifies this condition.
- **Authority evidence:** printed p. 166 says that this is the weakest semaphore-behavior condition and the “minimal fairness requirement” on a scheduler: a process must eventually be scheduled. The same paragraph expressly warns that, for semaphores, the condition permits “infinite overtaking.” These qualifications explain why the later persistence and FIFO obligations are stronger.
- **Harm:** C3 requires the exact busy-wait/semaphore example, not just its displayed formula. Omitting the source's scheduler standing and overtaking boundary weakens the presentation's account of what GPSS means by fairness and obscures the logical progression to persistence and strict FIFO.
- **Exact correction:** after the explanation at line 1374, add that GPSS calls this both the weakest semaphore-behavior condition and the minimal scheduler-fairness requirement, requiring eventual scheduling, while explicitly allowing infinite overtaking. Attribute those characterizations to printed p. 166; do not turn them into modern fairness definitions.

### MP-F4 — must fix — the canonical-model paragraph suppresses the exact intermediate claims and their restricted domain

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1653-1664`.
- **Reader claim:** after defining `\(\Delta^+\)` and `\(\Delta<\Theta\)`, the reader says only that the source “asserts the needed successor, linearity, and eventuality facts.”
- **Authority evidence:** printed p. 172 states three specific facts: `\(\Delta^+\in S\)` for every `\(\Delta\in S\)`; the branching-linearity implication
  \[
  (x<y\land x<z\land y\ne z)\to(y<z\lor z<y);
  \]
  and, from `\(Fw\in\Delta\)`, existence of `\(\Theta\)` with `\(\Delta<\Theta\)` and `\(w\in\Theta\)`. It then concludes that `\(<\)` is a linear order only after restriction to the descendants of the chosen `\(\Delta_0\)`, consistent with `\(F\)`. None of the supporting derivations is printed.
- **Harm:** the generic phrase loses the types, hypotheses, and especially the descendant restriction. C6 requires the exact maximal-theory/canonical-model claims, while I7 requires their proof omissions to remain visible. As printed, the reader cannot distinguish global linearity of `\(<\)` on all maximal theories from the source's restricted conclusion.
- **Exact correction:** replace or expand lines 1663--1664 with the three displayed statements above, state explicitly that linearity is concluded only on the descendant set of `\(\Delta_0\)`, and state that the source supplies no derivations for these claims. Do not promote them into a completed proof.

## Criterion-by-criterion disposition

### C1 — REVISE

MP-F1 is a direct metadata error. Apart from it, I checked clean the work title, four printed authors, 1980 POPL identity, pp. 163--173, DOI `10.1145/567446.567462`, eleven-page published-version label, `Sh:134` archive provenance, rights boundary, no-wrapper physical/printed map, and the explicit archive-object-versus-ACM-byte-identity limitation. The archive record does contain the publisher, series, ISBN, pages, DOI, and published-version label claimed at reader lines 1209--1211.

### C2 — REVISE

MP-F2 leaves the initial source grammar unstated. The semantic content otherwise checked clean: the model and atom interpretations; strict existential `F`, strict universal `G`, immediate-successor `X`, and strict witness-requiring infix `U`; the p. 164 past-pointing `F` defect and explicitly owned coherent-future repair; the one-sided printed `X` clause and explicitly owned false-at-no-successor totalization; source `L(U)` grammar versus later expressive-equivalence notation; source-versus-handbook standing of `\(U_s,S_s\)`; reversed operands relative to Kamp prefix `U`; and the strict/inclusive equations on natural-number words.

The bridge is mathematically correct. For inclusive strong until, evaluating `\(A\mathbin U B\)` at the immediate successor gives exactly the source's strict open-interval condition, hence `\(A\mathbin{U_s}B\equiv X(A\mathbin U B)\)`. Conversely the current point is recovered by `\(B\lor(A\land(A\mathbin{U_s}B))\)`. The `S/Y` duals are correct, including at position zero under the stated false previous-time clause.

### C3 — REVISE

MP-F3 omits a source-critical fairness qualification. I otherwise checked clean the partial- and total-correctness displays; exact invariance/eventuality inventories; local and global insistence, persistence, and impulse conditions; both displayed logical equivalences; semaphore and guarded-region conditions and the queue/unbounded-counter versus semaphore-only qualification; the impulse/external-signal boundary; unsolicited-response formula and boundary disclaimer; the eliminable `Pr` definition and standing; FIFO request/response and semaphore instance; and the repeated-response refinement.

### C4 — ACCEPTED WITHIN THE ROUND, SUBJECT TO THE OVERALL REVISE

The four questions and their order are correctly represented. The Kamp IV.3 attribution is properly reported as GPSS's compressed attribution rather than silently turning Kamp's literal isolation-tense theorem into the missing `U`-from-`F,X` reduction. `L_1`, equality, order, unary predicates, complete/discrete/omega order classes and examples, and endpoint neutrality checked clean. The p. 170 crop confirms inclusive `\(\ge x\)` restrictions. The displayed temporal-to-first-order recursion is correctly marked as handbook-supplied, correctly typed as a metalinguistic map, and truth-preserving on linear orders under the disclosed `X` totalization.

### C5 — ACCEPTED WITHIN THE ROUND, SUBJECT TO THE OVERALL REVISE

Theorem 2.1 is correctly restricted to arbitrary one-free-variable `L_1` formulas at point zero of omega-models. Theorem 2.2 is correctly restricted to future formulas at every point of discrete complete models. Theorem 2.3 is the Boolean past/future separation over discrete complete models. Number 2.4 is correctly Proposition 2.4. Theorem 2.5 is correctly stated for arbitrary linear orders only after adding the undefined source symbols `S',U'`. The reader correctly separates `At`, `Bet_n`, `Bet`, special formulas, decomposition formulas, the Main Lemma, and the auxiliary event-expression argument; preserves the finite-complement architecture; records the absence of event-expression grammar/semantics/construction; preserves the printed “Proof of 2.2 (outline)” versus “yields theorem 2.1” tension; and assigns the direct Theorem 2.3 proof to [G2]. No local outline is promoted into a complete proof.

### C6 — REVISE

MP-F4 removes exact intermediate canonical claims and their descendant restriction. The remaining system material checked clean: the Section-3 primitive basis and languages; A1--A5 and U1--U2, including the implication form of A3; R1--R3 and theorem-only `G`-generalization; DX versus DUX standing; separate two-clause soundness and weak theoremhood-completeness strengths; maximal theories and the definitions of `\(\Delta^+\)` and `\(<\)`; the literal finite `\(\Gamma\)` closure obligations (including `\(XA\in\Gamma\Rightarrow X\neg A\in\Gamma\)`); quotient state set; `\(\rho_+,\rho_<\)` typing; transitive-closure lemma and A5 dependency; finite fair ultimately periodic path; the source's later omission of explicit adjacency; atom valuation; truth lemma; listed proof omissions; and the formula-dependent but unquantified decidability referral with no complexity class.

### C7 — ACCEPTED WITHIN THE ROUND, SUBJECT TO THE OVERALL REVISE

The p. 173 equations for present-inclusive `F^0,G^0` and weak/universal `U^0` are exact. The manuscript correctly explains that `U^0` is not inclusive strong until because its `GA` disjunct permits no right-operand witness. A0.1--A0.5, U0.1--U0.2, unchanged propositional/MP rules and `G^0`-generalization, and `D^0X/D^0UX` standing checked clean. The manuscript correctly prevents transfer of the Part VIII strong-until induction rule, the later LTL name, automata/Buechi translations, PSPACE, and model-checking claims into GPSS 1980.

### C8 — ACCEPTED WITHIN THE ROUND, SUBJECT TO THE OVERALL REVISE

The shared strict/inclusive equations and both recursive translations are correct. Kamp prefix `U B A` places `B` at the strict witness and `A` on the open interval, so
`\(\tau(U B A)=X(\tau(A)\,U\,\tau(B))\)` has the right operand order. Conversely, `\(\sigma(XA)=U\,\sigma(A)\,\bot\)` forces the strict witness to be the immediate successor, and the inclusive-until clause correctly adds the present case. The `S/Y` equations are the exact duals. The types, Boolean recursion, standing, necessity, nonredundancy, use, and structural truth-preservation argument are locally supplied. The discrete-word theorem states one-free-variable first-order expressive completeness over pointed `\((\mathbb N,<)\)` words and correctly retains `X,Y` on the inclusive side. Its Kamp/GPSS citations and anti-conflation qualifications are sound.

The source note, ledger, and bibliography otherwise agree on title, authors, DOI, venue, pages, operator conventions, theorem domains, and proof boundaries. MP-F1 is the one direct cross-file inconsistency.

### C9 — REVISE

MP-F1--MP-F4 are unsupported, omitted, or insufficiently exact reader-facing claims. Outside those findings, the prose is independently worded and the handbook-introduced names satisfy the five-part rule: `U_s/S_s`, `Pr`, the metalinguistic first-order translation, and shared `tau/sigma` each have local necessity, eliminable definitions, standing, nonredundancy, and actual use. Source names lacking definitions, especially `S',U'`, remain explicitly source-reported symbols rather than adopted handbook operators.

## Invariant-by-invariant disposition

- **I1:** satisfied. This was source scholarship and mathematical/prose review only; no prohibited verification or build activity occurred.
- **I2:** satisfied. Both hash passes matched every frozen identity exactly.
- **I3:** satisfied. All eleven printed pages 163--173 were visually read; the two controlling crops settled the faint quantifiers and literal closure line.
- **I4:** satisfied apart from no finding. The reversed `F` inequality stays visible; coherent future `F`, endpoint-totalized `X`, supplied `S_s`, and the first-order recursion retain handbook ownership.
- **I5:** satisfied apart from no finding. GPSS strict infix `U_s`, Kamp strict prefix `U/S`, handbook inclusive strong `U/S`, and weak `U^0` remain distinct in operand order, present inclusion, witness requirement, and need for `X/Y`.
- **I6:** satisfied apart from MP-F2's missing initial grammar. Grammar versus expressive power, theorem hypotheses, theoremhood completeness, and the missing GPSS clauses for `S,S',U'` are otherwise distinguished.
- **I7:** satisfied apart from MP-F4's insufficiently exact intermediate statements. Every named proof and referral boundary remains an outline or omission rather than a completed local proof.
- **I8:** satisfied. No later LTL, automata, explicit bound, PSPACE, or model-checking result is attributed to GPSS.
- **I9:** satisfied for every introduced technical name, as detailed under C9. MP-F2 remains a separate definition-before-use failure for the source's initial language.
- **I10:** satisfied. The review was blind and independent under the stated exclusions.
- **I11:** applied. Four must-fix findings require `REVISE`; no majority can override them.
- **I12:** preserved. This verdict concerns only the frozen N-c-012.c round-one topic-level review. It does not close N-c-012.d, N-c-012 as a whole, Part IX, source-wide ledgers, any publication build, rendered-page review, human review, final-book completion, or user acceptance.

## Verdict

The frozen snapshot requires the four exact corrections above and a fresh blind review on a new frozen identity.

REVISE
