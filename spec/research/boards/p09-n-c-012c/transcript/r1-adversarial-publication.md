REVISE

# Round-one adversarial publication/AGENTS review: N-c-012.c

## Reviewer, independence, and method

- Stable reviewer: `/root/mcnaughton_1966_research`.
- Assigned seat: adversarial publication/AGENTS compliance.
- Runtime model/version: not exposed to this reviewer.
- I read `spec/research/boards/p09-n-c-012c/charter.md` completely before substantive review.
- I did not inspect `spec/research/boards/p09-n-c-012c/ledger.md`, `transcript/chair.md`, any other reviewer's transcript, or any other reviewer's verdict, and I did not contact another reviewer.
- I made no manuscript, shared-surface, source-note, source-ledger, bibliography, authority, or build-artifact edit. This transcript is the only file I created.
- I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or build. The only command-line operations were read-only text inspection and SHA-256 identity computation. Visual inspection was confined to the scholarly source-page renders and the two controlling crops allowed by the charter.

## Frozen identity verification

Before substantive review, and again immediately before filing this transcript, I independently recomputed the eight frozen SHA-256 identities. Every identity matched the charter exactly:

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

## Authority pages visually read

I visually read the wrapper/archive marks and the complete printed authority body, one page at a time, from `tmp/pdfs/p09-gpss-1980/page-01.png` through `page-11.png`: printed pp. 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, and 173. No printed page was skipped. I also read the high-resolution p. 170 crop `page-08-quantifier-symbols.png`; the future-fragment quantifiers are visibly inclusive, (y\ge x). I read the high-resolution p. 172 crop `page-10-closure-crop.png`; the literal printed closure implication has antecedent (Xw\in\Gamma) and consequent (X\neg w\in\Gamma). Images, rather than OCR or the research note, controlled every source-linked judgment below.

## Steel-man of the frozen presentation

The presentation does substantial source-critical work correctly. It keeps the p. 164 past-pointing (F) inequality visible and labels the future-directed reading as a handbook repair; separately owns the no-successor (X) totalization and the supplied past clause; preserves strict witness/open-interval semantics and reversed Kamp operand order; distinguishes expressive equality from grammar equality; gives the strict/inclusive bridge rather than silently modernizing the source; preserves the unequal domains and proof statuses of the Section 2 results; transcribes the DX/DUX schemes, quotient construction, adjacency omission, truth lemma, and decidability limit without importing later complexity or automata results; and gives a correct shared two-direction translation over infinite discrete words. The bibliography record at `handbook/bib/handbook.bib:194-207` is accurate. These strengths do not cure the following seven publication-blocking defects.

## Findings

### AP-F1 — Must fix — the reader misreports the PDF metadata and omits the archive/ACM byte-identity boundary

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1208-1221`, especially lines 1211-1212.
- **Source and cross-file evidence:** The embedded `Author` field is `A. Pnueli, S. Shelah and J. Stavi`; it omits Dov Gabbay only. The printed title page names Dov Gabbay, Amir Pnueli, Saharon Shelah, and Jonathan Stavi (printed p. 163). The exact metadata fact and the archive-object boundary are correctly recorded at `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:30-38`, and the source ledger likewise says only Gabbay is omitted at `spec/research/p09-source-presentations-lot2-3.md:171`.
- **Defect:** The reader says the metadata “omits Gabbay and Stavi.” It therefore falsely reports a frozen object's provenance and contradicts both supporting records. The reader also says that the author archive identifies the linked object as the published version, but never records the necessary narrower fact that the archive hash does not establish byte identity with an ACM-hosted object.
- **Publication harm:** A reader cannot tell which authorship evidence is defective or what the acquired hash actually pins. C1 expressly requires both facts, and the current unit contradicts itself.
- **Exact correction:** Replace the metadata sentence with the exact fact that the field includes Pnueli, Shelah, and Stavi but omits Dov Gabbay, so the printed four-author title page controls. Add that the hash pins the author-archive object and that the archive's published-version label does not itself establish byte identity with an ACM-hosted file.

### AP-F2 — Must fix — the source language is used without its grammar or the standing of derived (G)

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1223-1292`, particularly the first uses of (L(U)) and (L(X,F,U)) at lines 1287-1289.
- **Source evidence:** Printed p. 164 introduces (L(F,X,U)) from atoms (q_0,q_1,\ldots), Boolean connectives (\neg,\land,\lor,\supset), and temporal operators (F,X,U), with (G w:=\neg F\neg w). The supporting transcription is at `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:144-153`.
- **Defect:** The reader starts with a model and semantics, then names two languages, but never supplies their generating grammar and never states at that location that (G) is initially derived. Later, at `n-c-012.tex:1622-1624`, it correctly records the Section 3 primitive-basis change, but that does not retroactively define the initial syntax.
- **Publication harm:** A first reader cannot determine which expressions belong to the source language or whether (G) is primitive. The omission is load-bearing because (L(U)) is first a syntactic deletion and later an expressive-power label, while the shared Part IX surface uses a different inclusive basis. It also violates definition-before-use and the five-part technical-name rule for the named language fragments.
- **Exact correction:** Before the model/semantic clauses, give the exact grammar: atoms (q_i), the four printed Boolean connectives, and primitive (F,X,U); define (G A\mathrel{:=}\neg F\neg A) and state its derived-formula standing. Then define the initial (L(U)) as the subgrammar obtained by deleting (F,X), before discussing the later expressive equivalence.

### AP-F3 — Must fix — the first program-correctness formulas contain undefined typed notation

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1317-1336`.
- **Source evidence:** Printed pp. 164-165 explain that (at_{\ell_i}) says the instruction at label (\ell_i) is about to execute, use (\bar y) for the current program-variable tuple and (\bar\xi) for the input/initial-value tuple, and use (\varphi) and (\psi) as precondition and postcondition. See the source record at `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:252-286`.
- **Defect:** The reader defines entry and exit locations but immediately uses (\mathit{at}_{\ell_0}), (\mathit{at}_{\ell_e}), (\bar y), (\bar\xi), (\varphi), and (\psi) without defining their meaning or standing.
- **Publication harm:** The two central program-correctness displays are not independently readable, and the notation's types must be inferred from a source the handbook is supposed to present. Repeated later use of (at_m) does not repair the initial definition-before-use failure.
- **Exact correction:** Immediately before the partial-correctness display, state that (at_{\ell}) is the state proposition “the instruction at (\ell) is about to execute,” (\bar y) is the tuple of current program-variable values, (\bar\xi) is the input/initial tuple, (\varphi(\bar\xi)) is the precondition, and (\psi(\bar\xi,\bar y)) is the postcondition. State explicitly that these are source program-state predicates/tuples and formula metavariables, not new temporal connectives.

### AP-F4 — Must fix — the FIFO semaphore formula loses its implementation-axiom standing

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1419-1429`.
- **Source evidence:** Printed p. 168 offers the semaphore-location display as a possible basic axiom for a particular FIFO semaphore implementation, not as a consequence of temporal logic. The source note records that boundary exactly at `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:447-458`.
- **Defect:** The reader calls it only “the semaphore-location instance.” It does not state the source's axiom/proof standing.
- **Publication harm:** The prose can be read as deriving FIFO behavior merely by substituting locations into the preceding temporal formula. That inflates proof ownership and erases the distinction between an implementation assumption and a logical consequence.
- **Exact correction:** After the display, state that GPSS proposes it as an implementation-specific basic axiom/specification for a FIFO semaphore realization; temporal conclusions using it are relative to that assumption, and the logic alone does not prove the implementation is FIFO.

### AP-F5 — Must fix — two load-bearing proof-outline obligations are replaced by vague labels

- **Artifact locations:** `handbook/parts/p09/presentations/n-c-012.tex:1565-1568` and `1653-1664`.
- **Source evidence:** Printed p. 170 says Lemma 1 is proved by induction and is essentially Kamp, Chapter II, Theorem 1; no induction is printed (`spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:687-691`). Printed p. 172 asserts exactly: (\Delta^+\in S); branching-linearity (x<y\land x<z\land y\ne z\Rightarrow y<z\lor z<y); and eventuality witnessing (Fw\in\Delta\Rightarrow\exists\Theta(\Delta<\Theta\land w\in\Theta)), with no supporting derivations (`source-note.md:824-846`).
- **Defect:** The reader states Lemma 1 without its printed proof/referral boundary, then compresses the three canonical-model assertions to “the needed successor, linearity, and eventuality facts.” Their exact statements disappear even though the subsequent descendant order, quotient paths, fair threading, and truth lemma depend on them.
- **Publication harm:** A skeptical reader cannot reconstruct the proof architecture or distinguish an asserted lemma from a proved step. This falls short of C5-C6's required exact inventory and makes the canonical outline look more complete than the source warrants.
- **Exact correction:** Add after Lemma 1 that GPSS reports an induction and identifies it as essentially Kamp Chapter II Theorem 1, but prints neither proof. At line 1663 replace the generic phrase by the three exact quantified statements above and say explicitly that their supporting axiomatic derivations are omitted.

### AP-F6 — Must fix — the p. 173 systems omit both target languages and the source's stated completeness standing

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1741-1747`.
- **Source evidence:** Printed p. 173 says the earlier systems can be transformed into complete axiomatic systems (D^0X) for (L(G^0,X)) and (D^0UX) for (L(G^0,X,U^0)), respectively. It then says a system equivalent to (D^0UX) appears in [MY].
- **Defect:** The reader says only which schemes “form” (D^0X) and (D^0UX). It omits the two target languages and omits that completeness is the source's explicit claim. The source note at `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:960-963` and source ledger at line 181 also fail to make the exact target-language/completeness standing explicit.
- **Publication harm:** The transformed names lack a precise language domain and theorem standing, violating the five-part technical-name rule. A reader cannot tell whether these are mere scheme collections, sound systems, complete systems, or calculi for the same language as DX/DUX.
- **Exact correction:** State the exact source claim and domains: (D^0X) is claimed complete for (L(G^0,X)), and (D^0UX) is claimed complete for (L(G^0,X,U^0)). Attribute that completeness to GPSS and state that p. 173 gives a transformation assertion and schemes, not a separate detailed proof. Qualify the claim further in light of AP-F7 rather than silently endorsing it.

### AP-F7 — Blocker — the literal p. 173 (U^0) equation conflicts with (U^0 2), but all three integration surfaces silently identify it as a coherent weak-until operation

- **Artifact locations:** `handbook/parts/p09/presentations/n-c-012.tex:1711-1746`; `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:932-963`; `spec/research/p09-source-presentations-lot2-3.md:181`.
- **Source evidence:** Printed p. 173 literally defines
  
  \[
  A\mathbin{U^0}B\equiv GA\lor B\lor\bigl(A\land(A\mathbin{U_s}B)\bigr),
  \]
  
  where the paper's (G) is strict, and then prints
  
  \[
  (U^0 2)\qquad A\mathbin{U^0}B\leftrightarrow B\lor\bigl(A\land X(A\mathbin{U^0}B)\bigr).
  \]
- **Defect:** Those two displays are not equivalent under the frozen source semantics. On an omega-model at time (0), let (A) be false at (0) and true at every later time, and let (B) be false everywhere. The defining display is true through strict (GA), but the right side of (U^0 2) is false because both (B) and current (A) are false. The manuscript, note, and ledger instead call the equation a coherent “present-inclusive weak/universal until” and discuss only its witness-optional (GA) disjunct. None discloses this printed conflict. The source's sentence that (F^0,G^0,U^0) include the present does not resolve the counterinstance.
- **Publication harm:** This is a direct mathematical contradiction inside the exact p. 173 inventory required by C7 and I5. It also makes the transformed completeness claim unsafe: the literal semantic definition and printed axioms cannot both govern one operation without a disclosed repair. Calling it standard present-inclusive weak until collapses the convention-sensitive surface the charter requires the review to protect.
- **Exact correction:** Record the conflict and the counterinstance in the reader, source note, and ledger. Do not claim the literal equation and (U^0 2) jointly define one coherent operation. Either (a) retain both as conflicting printed source artifacts and leave the exact repair open, or (b) adopt the coherent fixed-point repair replacing the first disjunct (GA) by (G^0A\equiv A\land GA), explicitly label that replacement a handbook repair, and keep the literal source equation visible. In either case, qualify the p. 173 completeness assertion by its dependence on the repaired/axiomatic reading.

## Criterion-by-criterion disposition

- **C1 — REVISE (AP-F1).** I checked printed p. 163, the eleven-page map, archive header, DOI/venue/pages, bibliography, conditional ACM copying language, later digital-copy notice, and independent-prose boundary. The metadata and byte-identity statements in the reader are not publication-ready.
- **C2 — REVISE (AP-F2).** Strict (F,G,U), one-sided (X), the literal p. 164 (m_1<m) defect, handbook future repair, no-successor totalization, (L(U)) overload, local (U_s/S_s) standing, and the strict/inclusive bridge were checked. The omitted initial grammar/derived-(G) standing remains substantive.
- **C3 — REVISE (AP-F3, AP-F4).** I checked partial/total correctness, both source classification lists, insistence/persistence/impulse, busy wait, semaphore, guarded region, unsolicited response, the eliminable (\operatorname{Pr}), FIFO, and repeated response against printed pp. 164-168. Undefined program notation and the missing FIFO axiom standing remain.
- **C4 — checked clean.** The four p. 169 questions, compressed Kamp IV.3 boundary, (L_1), order classes, visibly inclusive p. 170 (y\ge x) future quantifiers, and handbook ownership of the recursive temporal-to-first-order translation are stated without promoting the source's “natural translation” phrase to a printed recursion.
- **C5 — REVISE (AP-F5).** The unequal domains of Theorems 2.1-2.3, Proposition 2.4, and Theorem 2.5; At/Bet/special/decomposition classes; Main Lemma; missing event-expression grammar; numbering tension; missing gap semantics; and external proof referrals were checked. Lemma 1 and the three canonical load-bearing facts remain underreported.
- **C6 — REVISE (AP-F5).** DX/DUX languages, A1-A5, U1-U2, R1-R3, weak theoremhood completeness, absent soundness proof, maximal theories, literal Gamma closure, quotient relations, path/adjacency omission, fair threading, truth lemma, and no-bound/no-complexity decidability boundary were checked. The exact successor/linearity/eventuality assertions are missing from the reader.
- **C7 — REVISE (AP-F6, AP-F7).** I checked every literal p. 173 equation and transformed scheme directly from the image. The target-language/completeness standing is missing, and the printed (U^0)/(U^0 2) contradiction is undisclosed. Separation from Part VIII strong until and later LTL/automata/complexity material is otherwise explicit.
- **C8 — checked clean.** At `handbook/parts/p09/logic-in-computer-science.tex:636-681`, the recursive (\tau) and (\sigma) maps have the correct strict/inclusive directions and operand order, their metalinguistic standing and need for (X/Y) are explicit, and structural induction establishes the declared infinite-word domain. The theorem at lines 684-691 is correctly limited to pointed ((\mathbb N,<))-words and cites Kamp and GPSS. The reader's local bridge is consistent with it; the bibliography entry is accurate.
- **C9 — REVISE (AP-F1-AP-F7).** The prose is independently written and generally careful, but definition-before-use, exact standing, source/proof ownership, cross-file consistency, and convention separation fail at the locations above.

## Invariant-by-invariant disposition

- **I1 — satisfied by this review.** Only source scholarship, mathematical reasoning, prose inspection, and SHA-256 identity hashing were used.
- **I2 — satisfied.** All eight frozen identities matched before review and immediately before filing.
- **I3 — satisfied.** Every printed page 163-173 was visually read; p. 170 and p. 172 controlling crops were separately read.
- **I4 — manuscript checked clean.** The p. 164 conflict, coherent-future repair, no-successor (X) totalization, supplied (S_s) clause, recursive FO map, and intended adjacency are all explicitly owned by the handbook.
- **I5 — REVISE (AP-F7).** Strict GPSS (U), strict Kamp (U/S), and inclusive strong handbook (U/S) are separated, but the p. 173 (U^0) surface is not coherent as presented.
- **I6 — REVISE (AP-F2, AP-F6).** Most grammar/expressive/theorem/proof distinctions and the missing (S,S',U') semantics survive, but the initial grammar and p. 173 calculus domains/standing do not.
- **I7 — REVISE (AP-F5).** The major outline/missing-proof labels survive; Lemma 1's source referral and the exact canonical assertions do not.
- **I8 — satisfied.** No later LTL name, automata/Büchi translation, explicit small-model bound, PSPACE class, or model-checking theorem is attributed to GPSS.
- **I9 — REVISE (AP-F2, AP-F3, AP-F6, AP-F7).** The five-part technical-name rule fails for the initial language labels, program notation, transformed-system domains, and the incoherent (U^0) label.
- **I10 — satisfied.** Blind independence and transcript-only ownership were preserved.
- **I11 — applied.** These defects require REVISE regardless of another seat's result.
- **I12 — preserved.** This verdict concerns only the frozen N-c-012.c topic-level manuscript review. N-c-012.d, N-c-012 as a whole, Part IX, source-wide ledgers, publication build, rendered-page review, human review, final-book completion, and user acceptance remain open.

## Premortem

Assume this snapshot shipped and later failed scholarly review. The most likely cause would not be a missing modern result; it would be source-critical overconfidence at precisely the points where the presentation is otherwise strongest. A bibliographer would catch the false metadata claim, a first-time reader would encounter undefined syntax and program notation, and a logician would produce the one-line (U^0) countermodel showing that the literal p. 173 definition and (U^0 2) cannot both be right. An ordinary prose-only checklist could miss the last defect because the labels “weak” and “universal” sound familiar and the two displays are separated by explanatory prose. Direct model evaluation against the source image exposes it. The narrow safe closure condition is therefore repair of AP-F1-AP-F7 followed by a fresh blind review of a new frozen snapshot; no larger completion boundary is implied.

REVISE
