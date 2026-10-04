REVISE

# Round-two adversarial publication/AGENTS review: N-c-012.c

## Reviewer, independence, and method

- Stable reviewer: `/root/mcnaughton_1966_research`.
- Assigned seat: adversarial publication/AGENTS compliance.
- Runtime model/version: not exposed to this reviewer.
- I read `spec/research/boards/p09-n-c-012c/charter.md` completely, including the round-two replacement snapshot and mandatory F01--F10 checks, before substantive review.
- This was a fresh blind review. I did not inspect `spec/research/boards/p09-n-c-012c/ledger.md`, `transcript/chair.md`, any round-one transcript (including my own), any other reviewer's transcript, or any other reviewer's verdict. I did not contact another reviewer.
- I edited no manuscript, shared surface, source note, source ledger, bibliography, authority, or build artifact. This assigned transcript is the only file I created.
- I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or build. The only command-line operations were read-only text inspection and SHA-256 identity computation. Visual inspection was confined to the source-page renders and the two controlling crops permitted by the charter.

## Frozen identity verification

Before substantive review and again immediately before filing, I recomputed all eight round-two SHA-256 identities. Each matched the charter exactly:

| Frozen object | Recomputed SHA-256 |
|---|---|
| `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf` | `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2` |
| `tmp/pdfs/p09-gpss-1980/page-08-quantifier-symbols.png` | `D74FF885AC1010EA703749F215D1E47DFB3649595F3F8C0A282E073DB714C0F9` |
| `tmp/pdfs/p09-gpss-1980/page-10-closure-crop.png` | `F49C546E4F07A005BA548AB594C6F63B01B37FC62FE3D8DD89A3FAE44EAEA434` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `07BE0B6362383269716548E068A868CB83A48D51363F434FB1996A60B103A3DB` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `DAE8982D6CAA548BEBCB916B197399B6499A7C6DB966E6972CC4E2C50AC163BA` |
| `handbook/bib/handbook.bib` | `BB4096F50E3359E2F07187E1B898F8A8E65CF4A3AC3C288E3FA58099A2A53380` |
| `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` | `17C426E0B40971D1CEBAF1AF7527314AE4CA9B2CEBE78276C0134D196D5C812E` |
| `spec/research/p09-source-presentations-lot2-3.md` | `F2E16E8E217B8F87F0A451C118DBCBD14E122F4C8101ABE4E2CDDEDF70696496` |

## Authority pages visually read

I visually reread the complete authority body from `tmp/pdfs/p09-gpss-1980/page-01.png` through `page-11.png`: printed pp. 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, and 173. No printed page was skipped. The `Sh:134` archive mark and printed-page identity were checked on every page. I separately inspected `page-08-quantifier-symbols.png`; the p. 170 future-fragment quantifiers visibly use the inclusive signs (y\ge x). I separately inspected `page-10-closure-crop.png`; p. 172 literally prints (Xw\in\Gamma\Rightarrow X\neg w\in\Gamma). Images, not OCR, memory, the repaired reader, or the source note, controlled the source-linked findings below.

## Steel-man of the replacement snapshot

The replacement repairs almost all of the prior high-risk surfaces with unusual care. The provenance block now reports the exact metadata omission and archive/ACM identity boundary. The initial grammar, formula-symbol/interpretation distinction, strict (G) reading, response calibration, program notation, FIFO assumption standing, Lemma 1 attribution, three displayed canonical facts, transformed-system languages, and p. 173 (U^0) conflict are all materially improved. In particular, the reader, source note, and ledger now preserve both conflicting (U^0) displays, give the separating omega-model, identify (GA\mapsto G^0A) only as an unprinted possible repair, and qualify the (D^0UX) claim. The shared (\tau/\sigma) bridge remains mathematically correct. Those repairs do not cure the three independent defects below.

## Findings

### R2-AP-F1 — Must fix — the canonical construction uses an undefined, never-selected root theory

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1686-1710`, with the downstream dependence at lines 1732 and 1751-1753.
- **Authority evidence:** Printed p. 172 first defines (S) as the set of all maximal consistent theories, expressly glossed as maximal sets of formulas consistent relative to system I or II. It then says a standard argument yields some (Delta_0\in S) with (w_0\in\Delta_0). Only after that selection does the source restrict (<) to the theories (Delta\ge\Delta_0). The source note records the same steps at `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:829-862`.
- **Defect:** The reader says only that (S) is “the set of maximal theories,” without defining maximal consistency or its system-relative standing. It never states or makes the source's selection (Delta_0\in S) with (A_0\in\Delta_0). Nevertheless, line 1709 refers to “the selected (Delta_0),” and line 1732 starts from an unnamed quotient state containing (A_0). Line 1752 reports that the maximal-extension proof is absent, but the assertion whose proof is absent was itself never stated.
- **Publication harm:** The canonical construction has no defined root connecting the initial consistent formula to the descendant order, quotient path, and truth-lemma conclusion. A first reader cannot type “descendant of (Delta_0)” or recover why (A_0) belongs to the initial quotient state. This is a definition-before-use failure, an incomplete mandatory F08 repair, and a direct violation of the five-part technical-name rule for “maximal theory.”
- **Exact correction:** Define (S) as the set of formula sets maximally consistent, under inclusion, relative to the relevant system (DX) or (DUX). State the source assertion that a standard maximal-extension argument supplies (Delta_0\in S) with (A_0\in\Delta_0), while retaining that the argument is not printed. Replace the untyped word “descendants” by the exact restricted domain ({\Delta\in S:\Delta=\Delta_0\text{ or }\Delta_0<\Delta}), or give that set as its eliminable local definition.

### R2-AP-F2 — Must fix — the reader turns “finite up to logical equivalence” into a literally finite Boolean-closed formula set

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1710-1724`, especially line 1711.
- **Authority evidence:** Printed p. 172 says to extend ({w_0}) to a set (Gamma) satisfying the listed closure requirements and Boolean/subformula closure; it then says (Gamma) can be chosen with only finitely many distinct formulas **up to logical equivalence**. It does not say that the syntactic set (Gamma) itself is finite. The source note preserves the distinction at `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:863-877`.
- **Defect:** The reader says, “It then chooses a finite set (Gamma) ... closed under subformulas and Boolean operations,” and only afterward repeats that (Gamma) has finitely many members up to logical equivalence. Literal finiteness is stronger than the source and makes the second statement vacuous. Under ordinary syntactic closure by Boolean operations, a nonempty formula set has indefinitely many syntactically distinct Boolean compounds, so literal finite closure is not the printed construction.
- **Publication harm:** This silently repairs the proof outline by changing its object, obscures why (ar S) is finite, and contradicts the more exact source note. It compromises C6's required separation between the source's asserted finite-representation step and a completed filtration proof.
- **Exact correction:** Replace “a finite set (Gamma)” with “a formula set (Gamma) having only finitely many equivalence classes under the source's logical-equivalence relation,” while retaining every literal closure obligation. Explain that maximal theories agree on logically equivalent formulas, so intersections with (Gamma) are determined by finitely many equivalence classes; alternatively report the source's finiteness conclusion as asserted and its supporting detail as omitted. Do not select a finite representative set unless that additional construction is explicitly handbook-owned and its closure properties are re-established.

### R2-AP-F3 — Must fix — the Section 2 outline omits its explicit [SS] proof-referral boundary

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:1554-1649`.
- **Authority evidence:** Immediately before the heading `Proof of 2.2 (outline)`, printed p. 170 says, “The proof of 2.2 presented here follows [SS].” Printed p. 173 identifies [SS] as Shelah and Stavi, “Expressive Completeness for Temporal Logic,” forthcoming. The source note records the referral at `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:642-646`; the same note separately records the Kamp and [G2] referrals.
- **Defect:** The reader carefully reports the Kamp basis for Lemma 1 and the [G2] referral for Theorem 2.3, but it never reports that the source attributes its Theorem 2.2 outline to [SS].
- **Publication harm:** The proof-ownership inventory is incomplete precisely where C5 requires external proof referrals. Readers are left with the impression that the displayed normal-form/event-order architecture is presented without an external source dependency, although GPSS expressly says otherwise.
- **Exact correction:** At the start of “What the proof outline actually contains,” state that GPSS labels the passage `Proof of 2.2 (outline)` and says it follows its reference [SS], identified in the source bibliography as the forthcoming Shelah--Stavi manuscript. Make clear that this is a source-reported referral and that no separate [SS] body or proof is being silently imported.

## Mandatory F01--F10 disposition

- **F01 — checked clean.** `n-c-012.tex:1208-1225`, source-note lines 12-46, ledger line 171, and bibliography lines 194-207 now agree: the metadata names Pnueli, Shelah, and Stavi, omits only Dov Gabbay, the printed page controls, and the hash pins the archive object rather than ACM byte identity.
- **F02 — checked clean.** `n-c-012.tex:1227-1242` gives atoms (q_i), all four printed Boolean operations, primitive (F,X,U), derived (G), the (q_i/Q_i) distinction, no initial past constructor, and the later Section 3 basis change at lines 1655-1657.
- **F03 — checked clean.** `n-c-012.tex:1363-1383` states that local (Gp) means (p) at every strictly later point, explicitly rejects (FGp), and separates the outer strict (G).
- **F04 — checked clean.** `n-c-012.tex:1391-1408` preserves weakest acceptable semaphore behaviour, minimal scheduler fairness, infinite overtaking, and the separate infinite-scheduling warning.
- **F05 — checked clean.** `n-c-012.tex:1330-1348` defines (at_\ell), (ar y), (ar\xi), (arphi), and (psi), with their atemporal/metalinguistic standing, before the correctness display.
- **F06 — checked clean.** `n-c-012.tex:1445-1458` labels the semaphore FIFO display an implementation-specific possible basic axiom and denies theoremhood from temporal logic alone.
- **F07 — checked clean.** `n-c-012.tex:1596-1601` states that Lemma 1 is an unprinted induction essentially following Kamp, Chapter II, Theorem 1.
- **F08 — REVISE (R2-AP-F1).** The three formulas at `n-c-012.tex:1696-1707` are typed correctly, the final linearity claim is verbally restricted, and the absent derivations stay absent. But the required (Delta_0) is never selected or defined, so the descendant restriction is not an exact typed statement and the root-to-(A_0) dependency is missing.
- **F09 — checked clean.** `n-c-012.tex:1801-1806` gives (D^0X) for (L(G^0,X)), (D^0UX) for (L(G^0,X,U^0)), attributes completeness to the source, and invents no separate p. 173 proof.
- **F10 — checked clean.** `n-c-012.tex:1758-1807`, source-note lines 941-998, and ledger line 181 all preserve the literal equation and (U^0 2), give the separating omega-model, refuse one coherent (U^0) standing, label (GA\mapsto G^0A) unprinted, and qualify (D^0UX) consistently.

## Criterion-by-criterion disposition

- **C1 — checked clean.** Work identity, eleven-page map, archive provenance, metadata defect, DOI/venue/pages, conditional rights language, independent-prose boundary, and archive-versus-ACM identity limitation agree across the reader, note, ledger, and bibliography.
- **C2 — checked clean.** The model and grammar, strict (F/G/U), one-sided (X), literal p. 164 direction defect, handbook repair/totalization ownership, (L(U)) overload, local (U_s/S_s) standing, and strict/inclusive bridge are exact.
- **C3 — checked clean.** The correctness, classification, three response strengths, busy-wait, semaphore, guarded-region, unsolicited-response, (\operatorname{Pr}), FIFO, and repeated-response inventory matches printed pp. 164-168 with definitions before use and assumption standing preserved.
- **C4 — checked clean.** The four questions, compressed Kamp IV.3 reduction, (L_1), order classes, inclusive p. 170 (y\ge x) quantifiers, and handbook-owned first-order recursion are exact.
- **C5 — REVISE (R2-AP-F3).** Numbered-result domains, At/Bet/special/decomposition classes, Main Lemma, event-expression omissions, numbering tension, and Kamp/[G2] boundaries are correct; the explicit [SS] referral for the Theorem 2.2 outline is missing.
- **C6 — REVISE (R2-AP-F1, R2-AP-F2).** Languages, axioms, rules, theorem strengths, the three displayed facts, literal (Gamma) implications, quotient relations, path/adjacency disclosure, truth lemma, and decidability limit were checked. The root maximal theory is undefined/unselected and (Gamma)'s finiteness is misstated.
- **C7 — checked clean.** Every p. 173 equation and scheme, the countermodel, possible-repair status, transformed-system languages/claims, and anti-conflation boundary are exact and cross-file consistent.
- **C8 — checked clean.** `logic-in-computer-science.tex:636-681` gives correct typed recursive translations in both directions: (\tau(U\,B\,A)=X(\tau(A)\,U\,\tau(B))), while (\sigma) reverses operand order and uses (X/Y) exactly where discreteness requires them. Lines 673-681 give metalinguistic standing, necessity, nonredundancy, and truth-preservation use. The theorem at lines 684-691 is correctly restricted to pointed infinite ((\mathbb N,<))-words and has the right citations.
- **C9 — REVISE (R2-AP-F1--F3).** The prose is independently reconstructed and most technical names now satisfy the five-part rule, but the canonical root/type failures, literal-finiteness overstatement, and missing proof referral prevent publication readiness.

## Invariant-by-invariant disposition

- **I1 — satisfied by this review.** Only complete source reading, mathematical reasoning, prose inspection, and identity hashing were used.
- **I2 — satisfied.** All eight round-two hashes matched twice before filing.
- **I3 — satisfied.** Every printed page 163-173 and both controlling crops were visually read.
- **I4 — manuscript checked clean.** The p. 164 (F) conflict, future repair, endpoint totalization, supplied (S_s), first-order recursion, and intended path adjacency remain explicitly handbook-owned.
- **I5 — checked clean.** GPSS strict infix (U), Kamp strict prefix (U/S), handbook inclusive strong (U/S), and the conflicting p. 173 (U^0) displays remain distinct; no coherent (U^0) is silently adopted.
- **I6 — checked clean.** Grammar, expressive equivalence, theorem domains, proof status, and deductive completeness are separated; (S,S',U') remain source-reported but undefined.
- **I7 — REVISE (R2-AP-F1--F3).** The major outline and omitted-proof labels remain, but the canonical root/finite-closure architecture is not exact and one explicit source referral is omitted.
- **I8 — checked clean.** No later LTL name, automata/Büchi translation, explicit small-model bound, PSPACE result, or model-checking theorem is retrojected.
- **I9 — REVISE (R2-AP-F1).** “Maximal theory” and “selected descendant of (Delta_0)” lack the local exact definitions/selections needed for their standing and use.
- **I10 — satisfied.** Blind independence, no-contact, and transcript-only ownership were preserved.
- **I11 — applied.** These defects require REVISE independently of any other seat.
- **I12 — preserved.** This verdict concerns only the round-two N-c-012.c topic snapshot. N-c-012.d, N-c-012 as a whole, Part IX, source-wide ledgers, publication build, rendered-page review, human review, final-book completion, and user acceptance remain open.

## Premortem

Assume this replacement shipped and later failed scholarly review. The likeliest failure would be a reader trying to reconstruct p. 172: the text invokes a “selected” (Delta_0) that was never selected, calls (Gamma) literally finite despite Boolean closure, and then claims an extracted finite quotient and a model satisfying (A_0). The proof would appear complete enough to trust but would not actually connect its initial formula to its root or preserve the source's finite-modulo-equivalence distinction. A source historian would separately notice that the explicit [SS] dependency vanished while less central referrals were retained. A repair-checklist-only review could miss all three because none is the headline (U^0) defect; a fresh end-to-end proof-architecture pass exposes them. The narrow closure condition is repair of R2-AP-F1--F3 and a new blind review of one replacement snapshot. No larger completion boundary follows.

REVISE
