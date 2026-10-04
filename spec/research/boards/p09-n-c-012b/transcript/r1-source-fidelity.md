# N-c-012.b blind opening audit — source-fidelity seat

Reviewer: `/root/schmidt_smolka_1991_research`

Verdict: **REVISE**

## Opening position

### SF-F1 — must-fix — provenance wording and rights boundary

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:372-378`; `spec/research/p09-pnueli-1977-source-note.md:6-31`; compare `spec/research/p09-source-presentations-lot2-3.md:153`.
- **Claim:** The manuscript calls the access page “Pnueli's own NYU publication list.” The source note and ledger more accurately identify it as Pnueli's NYU memorial publication list. None of the reader-facing/provenance surfaces states the rights boundary required by C1.
- **Authority evidence:** The acquired object is linked from `https://cs.nyu.edu/home/people/in_memoriam/pnueli/c-and-j.html`; its image-only PostScript contains a May 1981 wrapper followed by the 1977 printed body, pp. 46-57. Nothing in the acquired body supplies a republication license.
- **Harm:** “Own” overstates the demonstrated hosting/curation provenance, and author-hosted access could be mistaken for a transfer of reuse rights.
- **Exact correction:** At manuscript line 373 replace “Pnueli's own NYU publication list” with “Pnueli's NYU memorial publication list.” Add locally to the source note, and preferably to the acquisition paragraph, that the copy is used for source scholarship, that no redistribution/republication license is inferred from access, and that the independently unperformed IEEE-file comparison remains open.

### SF-F2 — must-fix — printed ranking rule P2 is omitted

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:439-442`; `spec/research/p09-pnueli-1977-source-note.md:92-98`; the ledger's broad coverage claim is at `spec/research/p09-source-presentations-lot2-3.md:157,161`.
- **Claim:** The manuscript and source note paraphrase the well-founded ranking principle but do not reproduce Pnueli's printed P2 rule.
- **Authority evidence:** Printed p. 49 gives P2 with the premise that every `\varphi`-state has a natural-number rank and the transition premise
  \[
  \varphi(s)\Rightarrow\exists n\,A(s,n),\qquad
  \frac{A(s,n)\land R(s,s^1)\Rightarrow
        A(s^1,n-1)\lor\psi(s)}
       {\varphi\leadsto\psi}\;(P2).
  \]
  The following prose says that the natural-number version is presented there and that an extension to other well-founded sets is available elsewhere.
- **Harm:** C3 expressly requires the exact ranking principle. The current prose hides the printed placement of `\psi(s)`, the rank decrement, the quantification/existence premise, and the rule's exact conclusion.
- **Exact correction:** Print P2, with variables and source-side target occurrence exactly as on p. 49, immediately after P1; then separately retain the source's well-founded-set extension boundary. Expand the source note likewise.

### SF-F3 — must-fix — incomplete pure future-tense proof system and quantifier treatment

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:527-555`; `spec/research/p09-pnueli-1977-source-note.md:120-134`; ledger `spec/research/p09-source-presentations-lot2-3.md:157,161`.
- **Claim:** The manuscript gives G1-G3, classical tautologies, modus ponens, and RG/necessitation, but omits the two displayed F consequences, all four printed quantifier principles, and the source's qualification on unrestricted generalization.
- **Authority evidence:** Printed p. 52 derives
  `A => FA` (F2) and `FFA => FA` (F3), then warns that RG relies on homogeneous development and must be restricted when facts about the present are obtained by other means. Printed p. 53 states Q1-Q4:
  \[
  G(\forall x\,p)\equiv\forall x\,G(p),\quad
  F(\exists x\,p)\equiv\exists x\,F(p),
  \]
  \[
  F(\forall x\,p)\Rightarrow\forall x\,F(p),\quad
  \exists x\,G(p)\Rightarrow G(\exists x\,p).
  \]
- **Harm:** C5 requires exact syntax, quantifier treatment, and generalization restrictions. Saying merely that formulas “use quantifiers” does not present the quantified proof system, and unrestricted necessitation is misleading once system-specific present facts are admitted.
- **Exact correction:** Add F2-F3 as printed derived formulas; add Q1-Q4 with their exact directions/equivalences; state the p. 52 RG qualification before introducing system-dependent axioms; distinguish these source formulas from later LTL syntax. Extend the source note and ledger inventory so their closure claims no longer omit these clauses.

### SF-F4 — must-fix — formal fairness premise for axiom N is only paraphrased

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:557-592`; `spec/research/p09-pnueli-1977-source-note.md:136-139`.
- **Claim:** The manuscript introduces a designated `A\subseteq R` and says N is relative to a scheduling premise, but it does not give the source's finite action partition or its formal restriction on admitted executions.
- **Authority evidence:** Printed p. 53 partitions the transition relation into finitely many actions, `R=\bigvee_i A_i`, and adds to executions the condition that no action is absent forever from some point onward; in the concurrent interpretation, no enabled processor/action may be delayed indefinitely. N is then justified by that weak inevitability/fairness condition.
- **Harm:** Without the admitted-execution restriction, N looks like a rule valid for an arbitrary subrelation `A\subseteq R`; it is not. This loses a theorem-critical side condition required by C2 and C5.
- **Exact correction:** Before N, define the finite action family/partition and print the source's “no action indefinitely delayed” execution restriction, including its concurrent-program reading. State N only relative to that restricted execution class. Mirror the condition in the source note.

### SF-F5 — must-fix — finite-state hypothesis and Theorem 5 proof-system extension are incomplete

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:599-617`; `spec/research/p09-pnueli-1977-source-note.md:145-164`; ledger `spec/research/p09-source-presentations-lot2-3.md:157,161`.
- **Claim:** The finite-state paragraph omits the source's simplifying no-halting/no-deadlock assumption, reduces Theorem 5 to decidability, and omits the exact extension of the proof system used in its adequacy clause.
- **Authority evidence:** Printed p. 55 assumes, for simplicity, no halting states or deadlocks so that only infinite execution paths are considered. After the SCC argument for Theorem 4, the paper adds the initial-state axiom
  \[
  \frac{p(s_0)}{\vdash p}\;(P)
  \]
  and replaces unrestricted RG by MRG: from `\vdash A` infer `\vdash GA` only when the proof of `A` did not use axiom P. Theorem 5 states both decidability of arbitrary tense-formula validity on a finite-state system and adequacy of the extended `K_b` system for all valid propositional tense formulas.
- **Harm:** The present text suppresses a model hypothesis, a rule side condition, and half of Theorem 5's literal strength, violating C6.
- **Exact correction:** State the no-halting/no-deadlock simplification; print P and MRG with the “proof did not use P” side condition; state Theorem 5's decidability and adequacy clauses separately; preserve that Appendix B supplies discussion/proof routes rather than a full local proof.

### SF-F6 — must-fix — Appendix A is absent from the reader presentation and under-recorded in the source note

- **Location:** The Pnueli presentation ends at `handbook/parts/p09/presentations/n-c-012.tex:618` and immediately changes source at line 619; `spec/research/p09-pnueli-1977-source-note.md:42-43,156-164,168-174`; ledger `spec/research/p09-source-presentations-lot2-3.md:157`.
- **Claim:** Appendix B is summarized, but Appendix A's printed derived tense formulas and locally printed lemma proof are absent. The source note only names “Appendix A derived tense rules” in its page map while claiming the proof-system rules and theorem statements closed.
- **Authority evidence:** Printed p. 57 attributes T2 and T3 to [23], prints their two corollaries, and then prints a separate lemma with a six-line local proof ending in `p => Fq`. Appendix B begins separately and discusses Theorem 5.
- **Harm:** The charter explicitly requires both appendices and warns against omitting printed rules, qualifications, or proof-system extensions. The current Appendix-B-only ending makes the coverage claim false.
- **Exact correction:** Add an Appendix A boundary paragraph inventorying T2, T3, both corollaries, and the separate locally proved lemma, distinguishing the [23]-owned results from Pnueli's local lemma proof. Expand the source note and ledger to the same proof-ownership granularity.

### SF-F7 — must-fix — closure claims are premature on this frozen snapshot

- **Location:** `spec/research/p09-pnueli-1977-source-note.md:3-4,168-179`; `spec/research/p09-source-presentations-lot2-3.md:161`; manuscript version boundary `handbook/parts/p09/presentations/n-c-012.tex:1023-1027`.
- **Claim:** The source note and ledger say the mathematical presentation, proof-system rules, theorem statements, and body-level reader reconstruction are closed. Findings SF-F2 through SF-F6 show that the frozen reader presentation and note omit printed source material required by the declared scope.
- **Authority evidence:** Printed pp. 49, 52-53, 55, and 57 contain the omitted P2, F2-F3, Q1-Q4, RG qualification, formal fairness premise, P/MRG extension, Theorem 5 adequacy clause, and Appendix A material.
- **Harm:** A provenance boundary may be closed while a reader-facing reconstruction remains incomplete, but the current status text conflates those states and would allow premature topic admission.
- **Exact correction:** Keep author-copy acquisition/body access closed and IEEE-direct comparison open, but mark the reader-facing reconstruction and topic review open pending repair and fresh unanimous review. Restore the stronger closure wording only after the repaired snapshot is independently accepted.

## Checked-clean coverage

- The identity, title, author, FOCS venue/year, printed pagination, DOI, PostScript hashes, 1981-wrapper/1977-body distinction, and IEEE-comparison boundary are otherwise consistent across the manuscript, source note, ledger, and `Pnueli1977` bibliography entry.
- The dynamic-system tuple, nondeterministic infinite execution model, sequential and concurrent state decompositions, atomic statement execution, fairness motivation, invariance examples, strict temporal-implication clause, ER A1-A2/R1-R4, first-order-axiom inclusion, Theorem 1 strength and proof-sketch assumptions, sequential attachment, concurrent full/partial/global attachment comparison, producer-consumer example scope, inclusive F/G semantics, G1-G3/RT/MP basis, system axioms I1-I2/E/N as displayed, Theorems 2-4, Theorem 3 corollary, SCC route, and Appendix B's two cited routes otherwise correspond to printed pp. 46-57.
- The manuscript explicitly preserves the strict `j>i` / A2 / inclusive F / Theorem 3 tension and does not retroject X/U, a later Buchi construction, modern safety/liveness syntax, or a PSPACE classification into Pnueli 1977. The adjacent GPSS presentation begins at line 619 and is visibly separate.
- The shared Part IX surfaces define the later LTL/automata results under their own sources and input N-c-012 at line 820; no direct Pnueli-1977 attribution collision was found there.

## Criterion-by-criterion coverage

- **C1 — REVISE:** identity/version/page map/hash boundary checked; provenance wording and rights statement require SF-F1.
- **C2 — REVISE:** program/execution/atomicity hierarchy checked; formal fairness condition requires SF-F4.
- **C3 — REVISE:** P1, ER, Theorem 1, and sketch assumptions checked; exact P2 requires SF-F2.
- **C4 — ACCEPT on this criterion:** sequential and concurrent applications and example scope checked against pp. 50-52.
- **C5 — REVISE:** F/G and system axioms checked; F2-F3, Q1-Q4, and RG qualification require SF-F3, and N's premise requires SF-F4.
- **C6 — REVISE:** Theorem 4/SCC and Appendix B checked; finite-path hypothesis, P/MRG, Theorem 5 adequacy, and Appendix A require SF-F5-SF-F6.
- **C7 — REVISE:** bibliography/shared surfaces are consistent, but note/ledger closure claims require SF-F7.
- **C8 — REVISE:** anti-conflation and strict/inclusive distinctions are clean; completeness and source-defined-before-use fail because of SF-F2-SF-F6.

## Hash and independence record

Every charter hash was verified before substantive review and rechecked after all reading; all eight matched exactly:

- `focs77.ps.gz` — `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `focs77.ps` — `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `focs77.pdf` — `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `n-c-012.tex` — `0DADDC029C1ED7574B14BA6A48ACEBE712F93A125AD7641747E336FAE2788C19`
- `logic-in-computer-science.tex` — `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook.bib` — `AC811C3E21F76830822D4A78B3786AC2D36660BB919F6C5FEC16217BD663D8E2`
- Pnueli source note — `539E0CEBE721A1F75D87223C41E6DEA2F139543E86EEF016750E56D169DE2D16`
- source ledger — `C3ACAF3670EF0BCDB58C67138FBA68565817814F19307DF5E25F329D093D2A35`

I visually read all twelve printed authority pages 46-57. I did not inspect the board ledger, chair record, or another seat's transcript/output, did not contact another reviewer, and made no edit outside this transcript. I ran no tests, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds. The research skill's normal delegation step was not used because the charter requires a blind independent seat and forbids reviewer contact.

Runtime model/version: the harness did not expose it.

## Verdict

**REVISE**
