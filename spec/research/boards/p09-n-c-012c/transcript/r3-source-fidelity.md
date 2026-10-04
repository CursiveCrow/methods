ACCEPT

# Round-three source-fidelity review: N-c-012.c

## Reviewer, runtime, independence, and method

- Stable agent identifier: `/root/schmidt_smolka_1991_research/gpss_primary_pass`.
- Runtime model/version: the exact serving model and build version were not exposed to this reviewer.
- Review basis: the complete updated charter at `spec/research/boards/p09-n-c-012c/charter.md`, the frozen round-three artifacts, the complete eleven-page authority, and the two controlling crops.
- Independence: I did not read `spec/research/boards/p09-n-c-012c/ledger.md`, `transcript/chair.md`, any round-one or round-two transcript (including my own), or any other reviewer's transcript or verdict. I did not contact another reviewer. Filename discovery did not include reading any prohibited transcript.
- Method: direct visual reading of every authority page, direct inspection of the frozen prose and formulas, mathematical comparison of the displayed semantics and translations, archive-record inspection, and PDF-property inspection only. I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds.

## Frozen round-three hash verification

I verified every frozen hash before substantive review and verified all eight again immediately before filing. Every value matched the charter exactly.

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf` | `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2` |
| `tmp/pdfs/p09-gpss-1980/page-08-quantifier-symbols.png` | `D74FF885AC1010EA703749F215D1E47DFB3649595F3F8C0A282E073DB714C0F9` |
| `tmp/pdfs/p09-gpss-1980/page-10-closure-crop.png` | `F49C546E4F07A005BA548AB594C6F63B01B37FC62FE3D8DD89A3FAE44EAEA434` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `3C62CB8706389EFA4572A45EE4321A5A985F2CEDC027C263F4E1B9D2F074F3E5` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `DAE8982D6CAA548BEBCB916B197399B6499A7C6DB966E6972CC4E2C50AC163BA` |
| `handbook/bib/handbook.bib` | `BB4096F50E3359E2F07187E1B898F8A8E65CF4A3AC3C288E3FA58099A2A53380` |
| `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` | `D7DF8D78587EDFBB0E5EFBE90A92EC39ED154214A9D2CE47DF1E0D8D23F3C49A` |
| `spec/research/p09-source-presentations-lot2-3.md` | `44538248682AA9229F049D27A32086FA8E65973B39DFA8FCDAB41ACD918008E0` |

The PDF properties independently read from the frozen object were: title `On the Temporal Analysis of Fairness`; subject `Seventh Annual ACM Symposium on Principles of Programming Languages`; embedded Author field `A. Pnueli, S. Shelah and J. Stavi`; 11 pages; 778,981 bytes; page size 623 by 799 points; PDF 1.3; not encrypted. The live author-archive record `Sh:134` named all four authors, the 1980 proceedings, pp. 163--173, DOI `10.1145/567446.567462`, ISBN `0-89791-011-7`, and the linked object as the published version with 11 pages. This supports the artifact's metadata/provenance distinctions but does not establish byte identity with an ACM-hosted object.

## Complete authority-page read record

I visually read every complete 180-dpi page image at original detail. Physical page 1 is printed p. 163 and there is no wrapper. The source PDF, not OCR, controlled the review.

| Local image | Printed page | Material visually checked against the frozen artifacts |
|---|---:|---|
| `tmp/pdfs/p09-gpss-1980/page-01.png` | 163 | Sh:134 header; title; Dov Gabbay, Amir Pnueli, Saharon Shelah, Jonathan Stavi; affiliations; abstract; ACM notices; introduction; strict future readings of `F`, `G`, `X`, and infix `U`. |
| `tmp/pdfs/p09-gpss-1980/page-02.png` | 164 | Initial atoms and all four printed Boolean connectives; primitive `F,X,U`; linearly ordered model and `q_i`/`Q_i`; clauses (1)--(5); one-sided `X` clause; past-pointing `F` inequality; strict `U`; omega-validity; syntactic `L(U)`; `F`/`X` eliminations; execution frame; `at_l`; partial correctness. |
| `tmp/pdfs/p09-gpss-1980/page-03.png` | 165 | Partial-correctness explanation; total-correctness display; complete invariance/eventuality lists; transition to the need for `U`. |
| `tmp/pdfs/p09-gpss-1980/page-04.png` | 166 | Insistence, its global form and equivalent negated-`G` form; busy-wait formula; weakest acceptable behaviour; minimal fairness; eventual scheduling; infinite-overtaking warning; start of persistence. |
| `tmp/pdfs/p09-gpss-1980/page-05.png` | 167 | Persistence and its equivalent form; semaphore example and scheduling caveat; conditional critical region, strong and weak formulas and implementation calibration; impulse; external-signal limitation; start of unsolicited response. |
| `tmp/pdfs/p09-gpss-1980/page-06.png` | 168 | Unsolicited-response display and boundary caveat; strict fairness; `Pr`; FIFO request/response formula; proposed FIFO semaphore axiom; repeated-response refinement; four questions. |
| `tmp/pdfs/p09-gpss-1980/page-07.png` | 169 | Kamp attribution and compressed boundary; prior-system ownership; `L_1`; model/equivalence convention; complete and discrete order definitions and examples. |
| `tmp/pdfs/p09-gpss-1980/page-08.png` | 170 | Theorems 2.1--2.3 and unequal hypotheses; inclusive future-quantifier bounds; explicit sentence that the proof of 2.2 presented there follows `[SS]`; `Proof of 2.2 (outline)`; `At`, `Bet_n`, special formulas, Lemma 1, decomposition formula, cofinal conjunct. |
| `tmp/pdfs/p09-gpss-1980/page-09.png` | 171 | Main Lemma; printed “yields theorem 2.1” sentence; Proposition 2.4; event-expression example and missing machinery; complete-order modification assertion; Theorem 2.5 and undefined gap symbols; exact DX/DUX basis, rules, languages; Theorems 3.1--3.2; start of completeness outline. |
| `tmp/pdfs/p09-gpss-1980/page-10.png` | 172 | Maximal theories relative to I or II; unprinted selection of `Delta_0`; `Delta^+` and `<`; three asserted canonical facts; exact restricted domain; `Gamma` paragraph and literal closure lines; finite-up-to-equivalence claim; quotient and relations; transitive-closure lemma; path/fairness prose and later adjacency omission; `s_0`; valuation; truth lemma; decidability boundary. |
| `tmp/pdfs/p09-gpss-1980/page-11.png` | 173 | Exact `F^0,G^0,U^0` equations; existential/universal prose; transformed `A^0`/`U^0` schemes; `D^0X,D^0UX`; absence of a separate proof; complete reference list, including `[SS]` as Shelah--Stavi, “Expressive Completeness for Temporal Logic,” forthcoming. |

I also visually read both controlling enlargements:

- `page-08-quantifier-symbols.png` controls printed p. 170: the signs are inclusive `(forall y >= x)` and `(exists y >= x)`, not strict signs.
- `page-10-closure-crop.png` controls printed p. 172: the literal obligations are `Fw in Gamma -> Xw, XFw in Gamma`; `Xw in Gamma -> X~w in Gamma`; and `w_1 U w_2 in Gamma -> Fw_2, Xw_1, Xw_2, X(w_1 U w_2) in Gamma`.

## Frozen artifact coverage

- Reader presentation: `handbook/parts/p09/presentations/n-c-012.tex:1206-1836` (the complete GPSS subsection; the next presentation begins at line 1838).
- Shared bridge and public theorem: `handbook/parts/p09/logic-in-computer-science.tex:602-691`.
- Bibliography: `handbook/bib/handbook.bib:194-207`.
- Source note: `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:1-1153`, read completely.
- Source-presentation ledger subsection: `spec/research/p09-source-presentations-lot2-3.md:169-183`.

## Mandatory F01--F13 dispositions

- **F01 -- PASS.** Printed p. 163 and the archive record establish four authors; the embedded Author field contains Pnueli, Shelah, and Stavi and omits only Dov Gabbay. The hash is correctly limited to the author-archive object, without an ACM byte-identity claim. Artifact locators: reader `1208-1225`; source note `12-46`; bibliography `194-207`; source-presentation ledger `169-171`.
- **F02 -- PASS.** Printed p. 164 has atoms `q_i`, negation, conjunction, disjunction, implication, and primitive `F,X,U`; `G` is derived there. Formula symbols `q_i` are distinguished from truth sets `Q_i`, and Section 3's later primitive basis `G,X,U` with derived `F` is kept separate. Artifact locators: reader `1227-1242`, `1662-1664`; source note `107-250`, `762-773`; ledger `173`.
- **F03 -- PASS.** Printed pp. 163 and 166 use strict `G`: local `Gp` quantifies over every strictly later point, not eventual permanence; the outer `G` separately repeats the local obligation. Artifact locators: reader `1364-1389`; source note `305-331`, `351-372`; ledger `175`.
- **F04 -- PASS.** Printed p. 166's busy-wait formula retains the source's “weakest acceptable” and “minimal fairness” calibration, eventual-scheduling interpretation, and explicit infinite-overtaking warning. Artifact locators: reader `1391-1400`; source note `333-349`; ledger `175`.
- **F05 -- PASS.** The program-state proposition `at_l`, current tuple `bar y`, remembered-input tuple `bar xi`, precondition, and postcondition are defined and typed before the partial/total displays. Artifact locators: reader `1330-1356`; source note `252-292`; ledger `175`.
- **F06 -- PASS.** Printed p. 168's FIFO semaphore display is reported as a possible basic axiom for a particular implementation, not a theorem of temporal logic. Artifact locators: reader `1445-1458`; source note `459-470`; ledger `175`.
- **F07 -- PASS.** Printed p. 170's Lemma 1 is identified as an induction essentially following Kamp Chapter II Theorem 1, and the induction is explicitly marked unprinted. Artifact locators: reader `1603-1608`; source note `687-705`; ledger `177`.
- **F08 -- PASS.** Printed p. 172's three facts are typed over `S`: closure of `Delta^+`, branching linearity, and eventuality witnessing. The resulting linear-order claim is restricted to `{Delta in S : Delta = Delta_0 or Delta_0 < Delta}`, and the supporting derivations remain absent. Artifact locators: reader `1708-1725`; source note `852-872`; ledger `179`.
- **F09 -- PASS.** Printed p. 173's transformed schemes, inference rules, exact languages `L(G^0,X)` and `L(G^0,X,U^0)`, and source-claimed completeness of `D^0X,D^0UX` are preserved; no separate proof is invented. Artifact locators: reader `1806-1829`; source note `990-1011`; ledger `181`.
- **F10 -- PASS.** Both literal p. 173 `U^0` displays are retained. The stated omega-model (current `A` false, all later `A` true, `B` always false) separates the defining equation from `U^0 2`; replacing strict `GA` by `G^0A` is labelled only a possible unprinted repair; and the `D^0UX` claim is consistently qualified. Artifact locators: reader `1777-1829`; source note `954-1011`, `1085-1103`; ledger `181`.
- **F11 -- PASS.** Maximal consistency is explicitly relative to `DX` or `DUX`; the source's unprinted standard selection of `Delta_0` containing `A_0` is reported; the exact restricted domain is displayed without an undefined “descendant” term; and `s_0=Delta_0 cap Gamma` contains `A_0`. Artifact locators: reader `1693-1707`, `1721-1725`, `1750-1770`; source note `829-872`, `911-929`; ledger `179`.
- **F12 -- PASS.** The artifacts do not rely on the source's earlier informal description of `Gamma` as literally finite. They preserve the exact closure obligations, state only finitely many formulas up to logical equivalence, report the asserted finite quotient, and mark the supporting finiteness argument unprinted without silently choosing representatives. Artifact locators: reader `1726-1748`; source note `873-910`; ledger `179`. The p. 172 controlling crop confirms every closure symbol.
- **F13 -- PASS.** The reader states that GPSS says the presented proof of 2.2 follows `[SS]`, identifies `[SS]` from printed p. 173 as the forthcoming Shelah--Stavi manuscript, and explicitly neither imports nor claims independent verification of that manuscript's full proof. Artifact locators: reader `1554-1561`; source note `642-648`, `1106-1115`; ledger `177`.

## Criteria C1--C9

- **C1 -- PASS.** Identity, page map, author-archive provenance, DOI, venue, pages, PDF metadata defect, rights boundary, and archive-versus-ACM byte-identity limitation agree with printed p. 163, all eleven Sh:134 page headers, the PDF properties, and the author-archive record. Artifact evidence: reader `1208-1225`; source note `1-105`; bibliography `194-207`; ledger `169-171`.
- **C2 -- PASS.** The model, initial grammar, strict `F/G/X/U` semantics, p. 164 reversed-inequality conflict, no-successor omission, expressive rather than grammatical `L(U)` equality, local `U_s/S_s` standing, reversed Kamp operand order, and strict/inclusive bridge are exact and ownership-labelled. The source's `S`, `S'`, and `U'` omissions remain omissions. Artifact evidence: reader `1227-1328`, `1545-1552`; source note `107-250`, `1013-1068`; shared file `602-682`; ledger `173`, `177`.
- **C3 -- PASS.** The partial/total correctness formulas, full invariance/eventuality inventories, insistence/persistence/impulse distinctions, busy wait, semaphore, guarded region, unsolicited response, `Pr`, FIFO, proposed implementation axiom, and repeated-response refinement correspond to printed pp. 164--168. Artifact evidence: reader `1330-1468`; source note `252-486`; ledger `175`.
- **C4 -- PASS.** The four questions are separated from complexity; the Kamp IV.3 statement is reported as GPSS's compressed attribution rather than treated as the locally printed missing reduction; `L_1`, all order classes and examples, inclusive future quantifier bounds, and handbook ownership of the recursive temporal-to-first-order map are explicit. Artifact evidence: reader `1470-1527`; source note `488-547`; ledger `177`.
- **C5 -- PASS.** Theorems 2.1, 2.2, 2.3, Proposition 2.4, and Theorem 2.5 retain their unequal source/target languages, model classes, and point domains. `At`, `Bet`, special and decomposition formulas, the Main Lemma, the event-expression example and omitted machinery, the 2.1/2.2 numbering tension, Kamp/G2/SS referrals, and the absent gap semantics are all visible. Artifact evidence: reader `1529-1656`; source note `549-760`; ledger `177`.
- **C6 -- PASS.** `DX/DUX`, A1--A5, U1--U2, R1--R3, theorem-only generalization, soundness and weak theoremhood completeness, maximal-theory construction, exact `Gamma` closure, quotient relations, transitive-closure lemma, path recurrence, omitted formal adjacency, truth lemma, proof omissions, and decidability-only boundary match printed pp. 171--172. Artifact evidence: reader `1658-1775`; source note `762-952`; ledger `179`.
- **C7 -- PASS.** The exact p. 173 equations and transformed schemes are retained; the `U^0` countermodel is correct; a `GA`-to-`G^0A` change is only a disclosed possible repair; `D^0X/D^0UX` languages and claims are exact; and the text does not import the Part VIII induction rule, later LTL terminology, automata, or complexity. Artifact evidence: reader `1777-1836`; source note `954-1011`, `1038-1083`; ledger `181`.
- **C8 -- PASS.** In the shared file, `tau` correctly maps Kamp prefix strict `U B A` to `X(tau(A) U tau(B))` and strict `S B A` to `Y(tau(A) S tau(B))`; `sigma` correctly maps inclusive next/previous and inclusive `U/S` back to the strict prefix language. The types, grammar directions, operand order, present inclusion, witness requirement, and need for `X/Y` are explicit, and structural truth preservation on pointed omega-words is correct. The discrete-word first-order theorem has the proper domain and citations. Artifact evidence: shared file `602-691`; reader `1264-1328`, `1831-1836`; source note `1013-1068`; source ledger `173`, `177`, `181`; bibliography `194-207`.
- **C9 -- PASS.** The reader is independently worded, source page citations are calibrated, definitions precede use, types and quantifiers are explicit, source labels lacking definitions are not promoted into handbook objects, supplied repairs/translations are ownership-marked, and no unsupported later result is added. Artifact evidence: reader `1206-1836`; source note `1085-1153`; shared file `648-682`; ledger `169-183`.

## Invariants I1--I12

- **I1 -- PASS.** Book-scholarship methods only; no prohibited test, checker, script, TeX, handbook-PDF, or build activity.
- **I2 -- PASS.** Every frozen round-three hash matched twice; the verdict applies only to those values.
- **I3 -- PASS.** Every printed page 163--173 was visually read in full; source images controlled; both required crops were read and used.
- **I4 -- PASS.** The past-pointing p. 164 `F` inequality remains visible; coherent future `F`, endpoint-totalized `X`, past `S_s`, and temporal-to-first-order recursion are all expressly handbook-owned.
- **I5 -- PASS.** GPSS strict infix `U`, Kamp strict prefix `U/S`, inclusive strong `U/S`, and conflicting `U^0` are kept distinct in operand order, inclusion, witness requirement, and `X/Y` dependence.
- **I6 -- PASS.** Grammar, expressive equivalence, theorem hypotheses, proof status, and deductive completeness remain distinct; undefined `S`, `S'`, and `U'` are not treated as fully supplied source operators.
- **I7 -- PASS.** Every named proof outline, referral, missing soundness proof, event-expression omission, gap omission, canonical omission, and numbering tension remains explicit.
- **I8 -- PASS.** No LTL name, Buchi/automata translation, explicit small-model bound, PSPACE result, or model-checking theorem is retrojected into the 1980 paper.
- **I9 -- PASS.** Local handbook names and abbreviations (`U_s`, `S_s`, `Pr`, the `A -> A*(x)` map, `tau`, and `sigma`) have necessity, exact eliminable definitions, standing, nonredundancy, and actual use; missing source definitions remain owed artifacts.
- **I10 -- PASS.** Independent review; no prohibited board ledger or transcript was read and no reviewer was contacted.
- **I11 -- PASS.** This verdict is independent and not based on a majority or another seat's judgment.
- **I12 -- PASS.** This acceptance is limited to the frozen N-c-012.c topic-level manuscript scope. It does not close N-c-012.d, N-c-012 as a whole, Part IX, any source-wide ledger, final build, rendered-page review, human review, final-book completion, or user acceptance.

## Findings and verdict basis

No blocker, must-fix item, unsupported source claim, missing required qualification, hash mismatch, unread authority page, or unresolved reviewer uncertainty was found in the frozen round-three scope. The presentation does not conceal the source's defects: it preserves the p. 164 `F` conflict, p. 171 numbering tension and missing proof machinery, p. 172 proof omissions and adjacency gap, and p. 173 `U^0` inconsistency. Conversely, it does not turn the handbook's repairs, supplied clauses, recursive translations, or cross-convention bridge into claims about what GPSS printed. C1--C9, I1--I12, and F01--F13 therefore pass on the exact frozen hashes recorded above.
