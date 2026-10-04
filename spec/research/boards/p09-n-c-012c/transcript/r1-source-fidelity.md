REVISE

# Round-one source-fidelity review: N-c-012.c GPSS 1980

## Reviewer identity, exposure, and independence

- Stable agent identifier: `/root/schmidt_smolka_1991_research/gpss_primary_pass`.
- Seat: source fidelity.
- Runtime model/version: not exposed to this reviewer by the execution harness.
- Charter: `spec/research/boards/p09-n-c-012c/charter.md`, lines 1--62, was read completely before source or artifact review.
- Independence: I did not inspect `spec/research/boards/p09-n-c-012c/ledger.md`, `transcript/chair.md`, any other reviewer transcript, or any other reviewer verdict. I did not contact another reviewer. I did not use a prior research conclusion as a substitute for a fresh source reading.
- Mutation boundary: this transcript is the only file I created or edited.

## Frozen-hash verification

I verified every charter hash after reading the charter and before substantive review, and verified the same eight hashes again immediately before filing this verdict. Both passes matched exactly.

| Frozen object | Charter SHA-256 | Verified result |
|---|---|---|
| `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf` | `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2` | exact match |
| `tmp/pdfs/p09-gpss-1980/page-08-quantifier-symbols.png` | `D74FF885AC1010EA703749F215D1E47DFB3649595F3F8C0A282E073DB714C0F9` | exact match |
| `tmp/pdfs/p09-gpss-1980/page-10-closure-crop.png` | `F49C546E4F07A005BA548AB594C6F63B01B37FC62FE3D8DD89A3FAE44EAEA434` | exact match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `986A5CFFE2DB209557CA9325ABFC2CD2F47D54FD06B20CE0DEED01E2EEF6CD8B` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `DAE8982D6CAA548BEBCB916B197399B6499A7C6DB966E6972CC4E2C50AC163BA` | exact match |
| `handbook/bib/handbook.bib` | `BB4096F50E3359E2F07187E1B898F8A8E65CF4A3AC3C288E3FA58099A2A53380` | exact match |
| `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` | `17A8A21420B1655E29B08F08C536FD12D8F5195907AAF14B44C902F439FDE152` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `78D6CE5D2B9BE4EE508407F738FC39AB294D1B26BD1677DA2492C9DAD5A42D57` | exact match |

No identity mismatch or hash drift occurred during this review.

## Complete visual authority read

I visually reread all eleven page images in order, independently of the source note. The source PDF is the authority; the images and crops were used only as reading derivatives. No OCR text controlled a source claim.

| Image visually read | Source locator | Material checked against the frozen artifact |
|---|---|---|
| `page-01.png` | printed p. 163 / PDF p. 1 | Four-author printed title and affiliations; archive mark; abstract; publication and conditional-copying notices; introduction; informal strict-future `F`, `G`, `X`, and strict infix `U` descriptions. |
| `page-02.png` | printed p. 164 / PDF p. 2 | Language and linear-order model; clauses (1)--(5); the past-pointing inequality in printed `F` clause (4); the one-sided positive `X` clause; strict open-interval `U`; omega-models; `L(U)` grammar and expressive equation; execution-sequence frame; partial correctness. |
| `page-03.png` | printed p. 165 / PDF p. 3 | Total correctness; invariance and eventuality lists; discussion of response and why `U` is needed. |
| `page-04.png` | printed p. 166 / PDF p. 4 | Response to Insistence; `Gp \supset Fq` and `G(Gp \supset Fq)`; the equivalent negated-`G` form; busy-wait example; minimum scheduler fairness; beginning of Response to Persistence and `GFp \supset Fq`. |
| `page-05.png` | printed p. 167 / PDF p. 5 | Persistence formula and its equivalent form; semaphore warning; conditional-critical-section formulas and implementability claim; Response to an Impulse; beginning of unsolicited responses. |
| `page-06.png` | printed p. 168 / PDF p. 6 | Unsolicited-response formula; strict-FIFO `Pr` abbreviation and instances; repeated-response strengthening; the paper's four questions. |
| `page-07.png` | printed p. 169 / PDF p. 7 | Kamp attribution; earlier `DX`/`DUX` claims; first-order language; complete and discrete order classes; natural temporal-to-first-order direction. |
| `page-08.png` | printed p. 170 / PDF p. 8 | Theorems 2.1--2.3; future-formula definition; start of “Proof of 2.2 (outline)”; `At`, `Bet`, special formulas, and decomposition formulas. |
| `page-09.png` | printed p. 171 / PDF p. 9 | Main Lemma; Proposition 2.4 and its event-expression outline; Theorem 2.5 and undefined gap symbols; `DX`/`DUX`; A1--A5, U1--U2, R1--R3; Theorems 3.1--3.2. |
| `page-10.png` | printed p. 172 / PDF p. 10 | Maximal theories; finite `Gamma`; literal closure requirements; quotient relations; transitive-closure claim; fair path/thread condition; truth lemma; decidability corollary. |
| `page-11.png` | printed p. 173 / PDF p. 11 | `F^0`, `G^0`, weak/universal `U^0`; transformed A0/U0 schemes; `D^0X` and `D^0UX`; complete reference list. |

I also visually read both controlling high-resolution crops:

- `page-08-quantifier-symbols.png`, printed p. 170: the future-formula restrictions are visibly inclusive, `($\forall y\ge x$)` and `($\exists y\ge x$)`, not strict inequalities.
- `page-10-closure-crop.png`, printed p. 172: the literal additional closures are `Fw in Gamma` implies `Xw, XFw in Gamma`; `Xw in Gamma` implies `X not-w in Gamma`; and `w1 U w2 in Gamma` implies `Fw2, Xw1, Xw2, X(w1 U w2) in Gamma`. These are the symbols reflected at reader lines 1664--1672.

Every printed page required by I3 was read. There is no unread-page or illegible-symbol reservation.

## Complete frozen-artifact read

| Frozen artifact surface | Complete range read | Review use |
|---|---:|---|
| `handbook/parts/p09/presentations/n-c-012.tex` | lines 1206--1754 | Complete reader-facing GPSS presentation. |
| `handbook/parts/p09/logic-in-computer-science.tex` | lines 602--691 | Reused inclusive semantics, strict/inclusive bridge, recursive `tau`/`sigma`, and public discrete-word theorem. |
| `handbook/bib/handbook.bib` | lines 194--207 | Complete `GabbayPnueliShelahStavi1980` entry. |
| `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` | lines 1--1101 | Complete frozen primary-source note, checked against rather than substituted for the images. |
| `spec/research/p09-source-presentations-lot2-3.md` | lines 169--183 | Complete frozen N-c-012.c ledger entry. |

The author-archive record at `https://shelah.logic.at/papers/134/` was also inspected on 2026-08-23 for provenance. It identifies the four authors, title, 1980 POPL venue, pp. 163--173, DOI `10.1145/567446.567462`, and the linked eleven-page object as the published version. The embedded PDF `Author` field was read as `A. Pnueli, S. Shelah and J. Stavi`.

## Findings requiring revision

### F1 — The reader falsely says that the embedded metadata omits Stavi

This is a blocking identity/provenance error.

- Authority: the printed title page names Dov Gabbay, Amir Pnueli, Saharon Shelah, and Jonathan Stavi (printed p. 163 / PDF p. 1). The embedded PDF `Author` field is exactly `A. Pnueli, S. Shelah and J. Stavi`. It omits Dov Gabbay, but it includes J. Stavi.
- Defective reader text: `handbook/parts/p09/presentations/n-c-012.tex`, lines 1211--1212, says: “The printed title page names all four authors; the file's embedded metadata omits Gabbay and Stavi, so it does not control the authorship record.”
- Correct frozen cross-files: the source note, lines 30--34, records the exact three-name `Author` field and says it omits Dov Gabbay; the source-presentation ledger, line 171, likewise says only Dov Gabbay is omitted; the bibliography, lines 194--203, names all four authors and gives the correct title, venue, pages, year, and DOI.
- Consequence: C1 fails on the exact PDF-metadata defect; C8 fails because the reader contradicts the source note and ledger; C9 fails on source exactness and publication readiness.
- Required repair: at reader line 1212 replace “omits Gabbay and Stavi” with “omits Gabbay” or “omits Dov Gabbay.” No other identity-field repair is indicated by this review.

### F2 — The insistence gloss changes `Gp` into eventual permanence

This is a must-fix semantic prose error even though the displayed formulas are correct.

- Authority: under the paper's strict convention, printed p. 166 gives Response to Insistence as `Gp \supset Fq`, or `G(Gp \supset Fq)` when stated over all future behaviours, and describes the antecedent as permanent holding of `p`. At a reference point `t`, `Gp` requires `p` at every point strictly later than `t`.
- Correct reader formulas: `handbook/parts/p09/presentations/n-c-012.tex`, lines 1343--1353, correctly displays local `Gp\to Fq` and globalized `G(Gp\to Fq)`, separately from persistence `GFp\to Fq` and impulse `p\to Fq`.
- Defective reader gloss: lines 1355--1356 say, “The first asks for a response only when `p` eventually remains true.” “Eventually remains true” ordinarily states an eventual-permanence condition of the form `FGp`; that is weaker than the displayed local antecedent `Gp` at the current reference point. It also blurs the distinction between the local and globally required forms that the preceding table correctly preserves.
- Consequence: C3 fails on the exact insistence condition, and C9 fails on exact prose and qualification.
- Required repair: describe local `Gp` as requiring `p` at every strictly future point from the current reference point (or as permanent holding from that reference point, with the current point excluded by the strict convention). If the globalized form is glossed separately, say that `G(Gp\to Fq)` imposes that obligation at every future reference point. Do not use “eventually remains true” for the local `Gp` antecedent.

No additional blocker or must-fix source-fidelity finding arose from the complete frozen scope.

## Criterion-by-criterion disposition

### C1 — REVISE

Finding F1 is decisive. The underlying identity materials are otherwise exact: the source note gives the complete physical/printed page map at lines 48--67; author-archive provenance, DOI, venue, pages, PDF properties, archive marking, metadata dates, and archive-versus-ACM byte-identity boundary at lines 12--38; and rights language at lines 40--46. The ledger line 171 and bibliography lines 194--207 preserve the same identity and rights boundaries. Reader lines 1208--1221 correctly preserve the archive provenance, frozen PDF hash, printed-page span, rights caution, and independent-reconstruction boundary, but lines 1211--1212 introduce the false assertion that Stavi is missing from metadata.

### C2 — checked clean

- Source: printed pp. 163--164 / PDF pp. 1--2.
- Artifact: reader lines 1223--1315; source note lines 107--251; ledger line 173.
- The model `(T,<,Q_0,Q_1,...)` with linear `(T,<)` and unary truth sets is exact. Strict `F`/`G`, positive immediate-successor `X`, and strict-witness/open-interval infix `U` are kept distinct.
- The printed p. 164 clause-(4) inequality `m_1<m` remains visible at reader lines 1235--1245 and the future direction is explicitly owned as a handbook repair. The no-successor false case for `X` is explicitly handbook-owned at lines 1246--1249.
- Local `U_s` is defined exactly at lines 1251--1260. `S_s` is explicitly identified as the handbook-supplied exact order dual because GPSS prints no `S` truth clause, lines 1261--1276. Necessity, standing, nonredundancy, and use are stated locally.
- The source identities and the distinction between `L(U)` as grammar and the later equality of expressive powers are exact at lines 1279--1292.
- The strict/inclusive strong `U`/`S` bridge is correct at lines 1294--1315 and does not conflate p. 173 weak `U^0`.

### C3 — REVISE

Finding F2 is decisive. Apart from that prose gloss, the formulas and example inventory are source-faithful.

- Source: printed pp. 164--168 / PDF pp. 2--6.
- Artifact: reader lines 1317--1439; source note lines 252--475; ledger line 175.
- Partial correctness at reader lines 1321--1329 constrains an exit without asserting termination; total correctness at lines 1330--1336 requires a future exit satisfying the postcondition.
- The source's invariance list (safety, partial correctness, mutual exclusion, clean performance, deadlock freedom) and eventuality list (liveness, total correctness, accessibility, livelock freedom) are preserved as source classifications rather than later semantic definitions, lines 1338--1343.
- The insistence, persistence, and impulse formula table itself is exact at lines 1345--1353. The defect is only the line-1355 insistence gloss stated in F2.
- Busy wait, semaphore persistence, guarded region, and the weaker guarded condition are exact at lines 1369--1397, including the scheduling-instant warning and the implementation boundary.
- Absence of unsolicited response, eliminable metalinguistic `Pr`, FIFO, semaphore FIFO, and repeated-response strengthening are exact at lines 1399--1439. `Pr` has an exact eliminable definition and is not promoted to an object-language connective or execution relation.

### C4 — checked clean

- Source: printed pp. 168--170 / PDF pp. 6--8; the high-resolution p. 170 crop controls the inclusive quantifiers.
- Artifact: reader lines 1441--1497; source note lines 476--536; ledger line 177.
- The four questions are retained: eliminability of `U` in favour of `F,X`; expressive completeness of the resulting `L(U)`; a deductive system for `L(F,X)`; and a deductive system for `L(F,X,U)`. The text correctly keeps these separate from computational-complexity questions.
- The literal Kamp IV.3 result and GPSS's unprinted reduction are distinguished at reader lines 1449--1455.
- `L_1`, equality, `<`, and the unary `Q_i`; complete and discrete order classes; and the examples `N`, `Z`, `R`, `Q` are exact at lines 1457--1464.
- The future-formula restrictions are correctly printed as inclusive `>=x` at lines 1466--1469.
- The source merely calls the temporal-to-first-order translation natural. Reader lines 1470--1495 explicitly own the displayed recursion as a handbook spelling-out and type `A -> A*(x)` as an eliminable metalinguistic translation.

### C5 — checked clean

- Source: printed pp. 170--171 / PDF pp. 8--9.
- Artifact: reader lines 1499--1616; source note lines 537--747; ledger line 177.
- The unequal domains are preserved exactly: Theorem 2.1 is arbitrary one-free-variable `L_1` only at point 0 of every omega-model; Theorem 2.2 is future `L_1` at every point of every discrete complete model; Theorem 2.3 is past/future separation over discrete complete models; Proposition 2.4 is the complement step for decomposition formulas; Theorem 2.5 is arbitrary linear orders only with additional printed `S'`,`U'` symbols whose satisfaction clauses are absent.
- `At`, `Bet_0`, `Bet_{n+1}`, `Bet`, `Aft`, `Bef`, source “special” formulas, decomposition formulas, cofinal-occurrence conjuncts, and the Main Lemma are transcribed at reader lines 1523--1592 with their standing and uses.
- Reader lines 1594--1605 accurately identify the missing event-expression grammar, semantics, and return translation as the omitted core of Proposition 2.4.
- Lines 1607--1616 preserve the “Proof of 2.2 (outline)”/Theorem-2.1 numbering tension, the unprinted complete-order and past modifications, the absent local proof of Theorem 2.5, and Theorem 2.3's referral to [G2]. No outline or referral is promoted to a complete local proof.

### C6 — checked clean

- Source: printed pp. 169 and 171--172 / PDF pp. 7 and 9--10; the high-resolution p. 172 crop controls the closure symbols.
- Artifact: reader lines 1618--1709; source note lines 748--924; ledger line 179.
- The `DX` and `DUX` languages, A1--A5, U1--U2, and the three rules (propositional tautologies, modus ponens, theorem-only `G`-generalization) are exact at reader lines 1618--1641.
- Theorem 3.1 is correctly reported as soundness without a printed proof. Theorem 3.2 is correctly stated as theoremhood completeness over omega-model validity and retained as an outline, lines 1642--1651.
- Maximal theories, `Delta+`, `<`, the finite `Gamma`, all literal closure obligations, the quotient, `rho+`, `rho<`, and the transitive-closure assertion are exact at lines 1653--1683.
- Lines 1685--1693 retain intended `rho+` adjacency while disclosing that the later formal selection condition prints recurrence but omits adjacency.
- The valuation and truth-lemma statement are exact at lines 1694--1703. Lines 1704--1709 preserve the omitted maximal-extension, relation, fair-thread, and connective-case arguments, and state that the decidability paragraph gives neither an explicit bound nor a complexity class.

### C7 — checked clean

- Source: printed p. 173 / PDF p. 11.
- Artifact: reader lines 1711--1754; source note lines 925--1036; ledger line 181.
- The equations `F^0 A = A or FA`, `G^0 A = A and GA`, and `A U^0 B = GA or B or (A and (A U_s B))` are exact at reader lines 1711--1724.
- The reader explicitly separates weak/universal `U^0`, whose `GA` disjunct permits no `B` witness, from the handbook's inclusive strong until, lines 1725--1727.
- The transformed A0/U0 schemes and the standing of `D^0X`,`D^0UX` are exact at lines 1728--1745 and remain distinct from `DX`,`DUX` and the Part VIII strong-until calculus.
- Lines 1749--1754 correctly refuse to retroject the later name LTL, a Buchi translation, PSPACE, or a model-checking theorem into GPSS 1980.

### C8 — REVISE

The mathematical translation material is checked clean, but Finding F1 breaks required cross-file consistency.

- Artifact: shared integration lines 602--691; reader lines 1294--1315 and 1749--1754; source note lines 30--38 and 965--1036; ledger lines 171--181; bibliography lines 194--207.
- On natural-number words, the displayed strict/inclusive equations at shared lines 636--646 have the correct operand order and `X`/`Y` boundary.
- `tau` at lines 648--658 correctly translates Kamp strict prefix `U B A` and `S B A` to `X(tau(A) U tau(B))` and `Y(tau(A) S tau(B))`.
- `sigma` at lines 659--671 correctly defines next/previous using the strict constructors with `bottom`, and inclusive strong until/since by the current-target disjunct plus the current-left/open-interval conjunct.
- Lines 673--680 correctly type `tau`,`sigma` as eliminable metalinguistic functions and do not credit inclusive `U`,`S` without `X`,`Y` with next/previous expressiveness.
- The public theorem at lines 684--691 has the exact discrete-word domain and cites Kamp 1968 and GPSS 1980.
- Cross-file failure: reader lines 1211--1212 say Stavi is absent from metadata, while source note lines 30--34 and ledger line 171 correctly say that only Gabbay is absent.

### C9 — REVISE

Findings F1 and F2 prevent exact, publication-ready prose. Otherwise, the frozen scope uses independently worded reconstruction, defines handbook-introduced notation before use, gives its standing and eliminability, preserves the exact types and quantifiers, and does not import unsupported LTL/automata/complexity claims. The principal technical names introduced by the handbook have local necessity and use: `U_s`,`S_s` at reader lines 1251--1278; `A*(x)` at lines 1466--1495; `Pr` at lines 1407--1417; and `tau`,`sigma` at shared lines 648--680. Undefined source `S'`,`U'` and event expressions are reported as missing source artifacts rather than adopted as defined handbook objects, reader lines 1515--1519 and 1594--1605.

## Invariant-by-invariant disposition

- **I1 — satisfied.** This review used complete visual source reading, mathematical reasoning, metadata/provenance inspection, and prose inspection only. I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds.
- **I2 — satisfied.** All eight frozen hashes matched before substantive review and again immediately before filing; the exact values are recorded above.
- **I3 — satisfied.** Printed pp. 163--173 were all visually reread from `page-01.png` through `page-11.png`. The p. 170 inclusive signs were settled from the controlling quantifier crop. Images, not OCR, controlled the source comparison.
- **I4 — satisfied.** The p. 164 past-pointing `F` inequality remains visible and the future repair is owned at reader lines 1235--1246; no-successor `X` totalization is owned at lines 1246--1249; handbook-supplied `S_s` and temporal-to-first-order recursion are owned at lines 1261--1276 and 1470--1495.
- **I5 — satisfied.** GPSS strict infix `U_s`, Kamp strict prefix `U/S`, handbook inclusive strong `U/S`, and p. 173 weak `U^0` remain distinct in operand order, present inclusion, witness requirement, and use of `X/Y`; reader lines 1251--1315 and 1711--1747, shared lines 636--680.
- **I6 — satisfied.** Grammar, expressive equivalence, theorem hypotheses, proof status, and deductive completeness remain distinct. No printed GPSS truth clause is claimed for `S`, `S'`, or `U'`; reader lines 1261--1276 and 1515--1519.
- **I7 — satisfied.** Theorem 2.2 and Theorem 3.2 remain outlines; Proposition 2.4's event-expression machinery, Theorem 2.3's referral, Theorem 2.5's absent gap semantics, Theorem 3.1's absent soundness proof, and canonical-model omissions are all disclosed at reader lines 1594--1616 and 1642--1709.
- **I8 — satisfied.** No later LTL name, Buchi/automata translation, explicit small-model bound, PSPACE classification, or model-checking theorem is attributed to GPSS; reader lines 1704--1709 and 1749--1754, ledger line 181.
- **I9 — satisfied as to terminology structure, but acceptance is still barred by F1/F2 under C9.** Handbook-introduced `U_s`,`S_s`,`Pr`,`A*(x)`,`tau`,`sigma` have local definitions, standing, nonredundancy/necessity, and actual use. Undefined source event expressions and `S'`,`U'` are reported as missing artifacts.
- **I10 — satisfied.** I filed independently, read none of the forbidden board files or other reviewer transcripts/verdicts, and contacted no reviewer.
- **I11 — requires REVISE.** F1 and F2 are supported must-fix defects. They cannot be outvoted, so this snapshot cannot be accepted.
- **I12 — observed.** This verdict addresses only the frozen N-c-012.c topic-level manuscript scope. It does not close N-c-012.d, N-c-012 as a whole, Part IX, any source-wide ledger, publication build, rendered-page review, human review, final-book completion, or user acceptance.

## Source-fidelity conclusion

The formulas, theorem scopes, proof-status boundaries, strict/inclusive bridges, proof-system inventory, closure symbols, and later-history exclusions are otherwise unusually careful and survived the complete source comparison. The frozen snapshot nevertheless contains two reader-facing must-fix defects: a plainly false statement about Stavi in the embedded metadata, and a semantic gloss that weakens local `Gp` to eventual permanence. Under the charter's no-majority and any-defect rules, the round-one source-fidelity verdict is **REVISE**.
