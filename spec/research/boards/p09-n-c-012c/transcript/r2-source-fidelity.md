REVISE

# Round-two source-fidelity review: N-c-012.c GPSS 1980

## Reviewer identity, runtime exposure, and independence

- Stable agent identifier: `/root/schmidt_smolka_1991_research/gpss_primary_pass`.
- Assigned seat: round-two source fidelity.
- Runtime model/version: not exposed to this reviewer by the execution harness.
- Charter: `spec/research/boards/p09-n-c-012c/charter.md`, lines 1--99, was read completely before substantive source or artifact review.
- Frozen scope: only the replacement hashes at charter lines 71--80 were reviewed. The round-one hashes were not used as the reviewed snapshot.
- Blind-review boundary: I did not read `ledger.md`, `transcript/chair.md`, any round-one transcript, any other reviewer transcript, or any other reviewer verdict. I did not contact another reviewer. The complete authority was reread visually; no prior conclusion or note was used as a substitute.
- Mutation boundary: this round-two source-fidelity transcript is the only file I created or edited.

## Round-two frozen-hash verification

I verified all eight replacement hashes after reading the charter and before substantive review. I repeated the same verification immediately before filing. Both passes matched the charter exactly.

| Frozen round-two object | Required SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf` | `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2` | exact match |
| `tmp/pdfs/p09-gpss-1980/page-08-quantifier-symbols.png` | `D74FF885AC1010EA703749F215D1E47DFB3649595F3F8C0A282E073DB714C0F9` | exact match |
| `tmp/pdfs/p09-gpss-1980/page-10-closure-crop.png` | `F49C546E4F07A005BA548AB594C6F63B01B37FC62FE3D8DD89A3FAE44EAEA434` | exact match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `07BE0B6362383269716548E068A868CB83A48D51363F434FB1996A60B103A3DB` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `DAE8982D6CAA548BEBCB916B197399B6499A7C6DB966E6972CC4E2C50AC163BA` | exact match |
| `handbook/bib/handbook.bib` | `BB4096F50E3359E2F07187E1B898F8A8E65CF4A3AC3C288E3FA58099A2A53380` | exact match |
| `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` | `17C426E0B40971D1CEBAF1AF7527314AE4CA9B2CEBE78276C0134D196D5C812E` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `F2E16E8E217B8F87F0A451C118DBCBD14E122F4C8101ABE4E2CDDEDF70696496` | exact match |

No replacement-snapshot identity mismatch or hash drift occurred before filing.

## Complete fresh visual read of the authority

I visually reread the eleven authority pages in order from `page-01.png` through `page-11.png`. The source PDF controls; the PNG pages and two specified crops were reading derivatives. OCR did not control any formula or source claim.

| Visual derivative | Exact authority locator | Complete material checked |
|---|---|---|
| `page-01.png` | printed p. 163 / PDF p. 1 | `Sh:134`; title; four authors and affiliations; abstract; overlapping historical and later conditional-copying notices; introduction; strict-future informal clauses for `F`,`G`,`X`, and infix `U`. |
| `page-02.png` | printed p. 164 / PDF p. 2 | Initial grammar with atoms `q_i`, all four printed Boolean connectives, and primitive `F,X,U`; model and `Q_i` interpretations; clauses (1)--(5); past-pointing `F` inequality; one-sided `X`; strict `U`; omega-validity; `L(U)`; program/execution frame; `at_l`; start of partial correctness. |
| `page-03.png` | printed p. 165 / PDF p. 3 | Partial-correctness explanation; total correctness; invariance and eventuality lists; expressiveness motivation for `U`. |
| `page-04.png` | printed p. 166 / PDF p. 4 | Insistence `Gp -> Fq` and global `G(Gp -> Fq)`; equivalent negated form; busy-wait formula; weakest-behaviour/minimal-fairness calibration; infinite-overtaking warning; start of persistence. |
| `page-05.png` | printed p. 167 / PDF p. 5 | Persistence and semaphore formula; scheduling warning; two guarded-region formulas and implementation claims; impulse response; start of unsolicited response. |
| `page-06.png` | printed p. 168 / PDF p. 6 | Unsolicited-response formula; `Pr`; FIFO; the semaphore display as a proposed implementation axiom; repeated-response strengthening; start of the four questions. |
| `page-07.png` | printed p. 169 / PDF p. 7 | Remaining questions; Kamp attribution; earlier `DX`/`DUX` claims; first-order comparison language; order classes; natural translation. |
| `page-08.png` | printed p. 170 / PDF p. 8 | Theorems 2.1--2.3; future formula; explicit statement that the presented proof of 2.2 follows `[SS]`; `Proof of 2.2 (outline)`; `At`,`Bet`, special formulas; Lemma 1 and its Kamp referral; decomposition formulas. |
| `page-09.png` | printed p. 171 / PDF p. 9 | Main Lemma; Proposition 2.4; event-expression architecture; numbering tension; Theorem 2.5 and gap-symbol omissions; Section 3 basis; A1--A5, U1--U2, R1--R3; Theorems 3.1--3.2. |
| `page-10.png` | printed p. 172 / PDF p. 10 | Maximal theories; three asserted canonical facts; descendants-of-`Delta_0` restriction; finite `Gamma`; quotient relations; path and missing formal adjacency; truth lemma; decidability boundary. |
| `page-11.png` | printed p. 173 / PDF p. 11 | Literal `F^0`,`G^0`,`U^0` equations; transformed A0/U0 schemes; exact `D^0X`,`D^0UX` languages and completeness claims; complete references, including `[SS]`. |

The two controlling crops were also read independently:

- `page-08-quantifier-symbols.png`, printed p. 170: the source signs are inclusive, `(forall y >= x)` and `(exists y >= x)`, not strict signs.
- `page-10-closure-crop.png`, printed p. 172: the literal additional closures are `Fw in Gamma -> Xw, XFw in Gamma`; `Xw in Gamma -> X not-w in Gamma`; and `w1 U w2 in Gamma -> Fw2, Xw1, Xw2, X(w1 U w2) in Gamma`. Reader lines 1711--1719 preserve them.

All eleven printed pages were readable. There is no unread-page, missing-symbol, or crop uncertainty.

## Complete replacement-artifact read

| Frozen artifact surface | Complete replacement range read |
|---|---:|
| `handbook/parts/p09/presentations/n-c-012.tex` | GPSS subsection, lines 1206--1818, ending immediately before the Sistla--Clarke subsection at line 1819 |
| `handbook/parts/p09/logic-in-computer-science.tex` | strict/inclusive integration and `thm:p09-ltl-fo`, lines 602--691 |
| `handbook/bib/handbook.bib` | `GabbayPnueliShelahStavi1980`, lines 194--207 |
| `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` | complete file, lines 1--1140 |
| `spec/research/p09-source-presentations-lot2-3.md` | complete N-c-012.c subsection, lines 169--183 |

The author-archive record `https://shelah.logic.at/papers/134/` was independently inspected on 2026-08-23. It names Gabbay, Pnueli, Shelah, and Stavi; gives the 1980 POPL venue, pp. 163--173, DOI `10.1145/567446.567462`, and ISBN; and labels the linked object “published version (11p).” The frozen PDF document information was independently read: its `Author` field is exactly `A. Pnueli, S. Shelah and J. Stavi`.

## Finding requiring revision

### R2-SF-01 - the reader omits the source's explicit `[SS]` proof referral

This is a must-fix proof-ownership omission under C5's express requirement to preserve external proof referrals.

- Authority: at the top of the right column on printed p. 170 / PDF p. 8, immediately before `Proof of 2.2 (outline)`, GPSS states: “The proof of 2.2 presented here follows [SS].” Printed p. 173 / PDF p. 11 identifies `[SS]` as Shelah and Stavi, “Expressive Completeness for Temporal Logic,” forthcoming.
- Reader omission: the reader's complete proof-outline account runs from `handbook/parts/p09/presentations/n-c-012.tex`, lines 1554--1649. It records the Lemma 1 referral to Kamp at lines 1596--1601 and the Theorem 2.3 referral to `[G2]` at lines 1643--1647, but nowhere reports that GPSS says its presented proof of 2.2 follows `[SS]`.
- Correct frozen source-note locators: `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md`, lines 642--646, expressly records that the outline follows `[SS]`; lines 1099--1100 repeat the proof-ownership boundary.
- Ledger locator: the N-c-012.c proof-ownership summary at `spec/research/p09-source-presentations-lot2-3.md`, line 177, records the outline and several external dependencies but does not supply this missing reader statement.
- Consequence: C5 fails on complete external proof-referral ownership, and C9 fails on an omitted source qualification. The omission does not turn the outline into a claimed full proof, so I7 remains satisfied; it nevertheless leaves the reader's provenance account incomplete.
- Required repair: add, in the reader's proof-outline paragraph, that GPSS explicitly says the presented proof of Theorem 2.2 follows its reference `[SS]`, identified in the source as the forthcoming Shelah--Stavi manuscript. Do not imply that GPSS prints `[SS]`'s full proof or that the handbook independently verifies that manuscript.

No other source-fidelity blocker or uncertainty arose from the complete round-two snapshot.

## Mandatory round-two checks F01--F10

### F01 - satisfied

- Authority: printed p. 163 / PDF p. 1; frozen PDF metadata; author-archive record.
- Artifact: reader lines 1208--1225; source note lines 12--46; ledger line 171; bibliography lines 194--207.
- The embedded `Author` field names Pnueli, Shelah, and Stavi and omits only Dov Gabbay. The printed four-author title page controls. Reader lines 1218--1220 and source-note lines 37--38 expressly state that the hash pins the author-archive object and does not establish byte identity with an ACM-hosted object.

### F02 - satisfied

- Authority: printed p. 164 / PDF p. 2, and the Section 3 basis on printed p. 171 / PDF p. 9.
- Artifact: reader lines 1227--1262 and 1651--1683; source note lines 144--250 and 760--825; ledger line 173.
- The initial grammar has formula symbols `q_i`, negation, conjunction, disjunction, implication, and primitive `F,X,U`; `G` is derived. The reader separates each formula symbol `q_i` from its truth-set interpretation `Q_i`, excludes a past constructor from the initial grammar, and separately reports Section 3's primitive `G,X,U` basis with `F` derived.

### F03 - satisfied

- Authority: printed p. 166 / PDF p. 4.
- Artifact: reader lines 1363--1389; source note lines 305--331; ledger line 175.
- Local `Gp` is correctly stated to require `p` at every strictly later point, not eventual permanence `FGp`. The prefixed form `G(Gp -> Fq)` is separately explained as repeating the local obligation at every strictly later reference point.

### F04 - satisfied

- Authority: printed p. 166 / PDF p. 4.
- Artifact: reader lines 1391--1408; source note lines 333--349; ledger line 175.
- The busy-wait formula is exact. Reader lines 1396--1400 preserve the paper's calibration as the weakest acceptable semaphore behaviour and minimal scheduler-fairness assumption, together with the explicit infinite-overtaking warning.

### F05 - satisfied

- Authority: printed pp. 164--165 / PDF pp. 2--3.
- Artifact: reader lines 1330--1356; source note lines 252--292; ledger line 175.
- Before either correctness display, the reader defines `at_l` as the about-to-execute program-state proposition; `bar y` as current program values; same-arity `bar xi` as logical variables retaining input values; `phi(bar xi)` as precondition; and `psi(bar xi,bar y)` as postcondition. Their atemporal/metalinguistic standing is explicit.

### F06 - satisfied

- Authority: printed p. 168 / PDF p. 6.
- Artifact: reader lines 1445--1458; source note lines 441--470; ledger line 175.
- The FIFO semaphore display is expressly a possible basic axiom for a particular FIFO implementation and is assumption-relative, not a theorem supplied by temporal logic alone.

### F07 - satisfied

- Authority: printed p. 170 / PDF p. 8.
- Artifact: reader lines 1596--1601; source note lines 699--703; ledger line 177.
- Lemma 1 is reported as an induction on the formula, essentially following Kamp Chapter II Theorem 1, and the reader says that GPSS does not print the induction.

### F08 - satisfied

- Authority: printed p. 172 / PDF p. 10; the closure crop controls the `Gamma` symbols.
- Artifact: reader lines 1686--1756; source note lines 827--925; ledger line 179.
- The reader types all three asserted facts exactly: `forall Delta in S (Delta+ in S)`; branching linearity for `x,y,z in S`; and the eventuality witness with `Delta,Theta in S`. Reader lines 1709--1710 restrict the resulting linearity statement to descendants of the selected `Delta_0`. Lines 1696 and 1751--1754 preserve the absence of supporting derivations and later canonical proof components.

### F09 - satisfied

- Authority: printed p. 173 / PDF p. 11.
- Artifact: reader lines 1787--1810; source note lines 977--998 and 1114--1118; ledger line 181.
- `D^0X` is correctly reported for `L(G^0,X)`, and `D^0UX` for `L(G^0,X,U^0)`, at the source-claimed completeness strength. Reader lines 1804--1806 explicitly state that p. 173 prints the transformation claim and schemes, not a separate completeness proof.

### F10 - satisfied

- Authority: printed p. 173 / PDF p. 11.
- Artifact: reader lines 1758--1810; source note lines 941--998, 1072--1090, and 1114--1118; ledger line 181.
- The literal equation `A U^0 B = GA or B or (A and (A U_s B))` and scheme `U^0 2`, `A U^0 B <-> B or (A and X(A U^0 B))`, are both preserved.
- The displayed omega-model separates them: `A` is false now and true at every later point; `B` is false everywhere. Strict `GA` makes the equation true now, while the recursive right side is false now.
- Reader lines 1781--1785 label `GA` to `G^0A` only as a possible unprinted repair and decline to assign `U^0` a coherent defined standing.
- The `D^0UX` claim is qualified by the unresolved conflict in all three prose records: reader lines 1805--1807; source note lines 995--998; ledger line 181.

## Criterion-by-criterion disposition

### C1 - checked clean

Exact work identity, complete page map, archive provenance, metadata defect, DOI/venue/pages, rights boundary, and archive-versus-ACM byte-identity limitation agree with printed p. 163, the archive record, and PDF information. Artifact locators: reader lines 1208--1225; source note lines 12--105; ledger line 171; bibliography lines 194--207.

### C2 - checked clean

The model, complete initial syntax, strict `F/G/X/U`, p. 164 `F` conflict, one-sided `X`, `L(U)` overload, local `U_s/S_s` standing, Section 3 basis change, and strict/inclusive bridge are exact. Authority: printed pp. 163--164 and 171. Artifact: reader lines 1227--1328 and 1651--1683; source note lines 107--250 and 760--825; ledger line 173.

### C3 - checked clean

Partial/total correctness, definitions of all displayed program metavariables, invariance/eventuality inventories, insistence/persistence/impulse, busy wait, semaphore, guarded region, unsolicited response, `Pr`, FIFO, the implementation-axiom standing, and repeated response match printed pp. 164--168. Artifact: reader lines 1330--1468; source note lines 252--486; ledger line 175.

### C4 - checked clean

The four questions, compressed Kamp IV.3 boundary, `L_1`, order classes, inclusive future quantifiers, and handbook ownership of the displayed temporal-to-first-order recursion are exact. Authority: printed pp. 168--170, with the p. 170 crop controlling `>=`. Artifact: reader lines 1470--1527; source note lines 488--547; ledger line 177.

### C5 - REVISE

R2-SF-01 is decisive: the reader omits the printed p. 170 statement that the presented proof of 2.2 follows `[SS]`. The remaining C5 material is checked clean: unequal Theorem 2.1/2.2/2.3/Proposition 2.4/Theorem 2.5 domains; `At`,`Bet`, special and decomposition formulas; Main Lemma; the Lemma 1 Kamp referral; event-expression omissions; 2.1/2.2 numbering tension; `[G2]` referral; missing gap semantics; and outline status. Artifact: reader lines 1529--1649; source note lines 549--758; ledger line 177.

### C6 - checked clean

`DX/DUX` languages, A1--A5, U1--U2, R1--R3, soundness and theoremhood-completeness strengths, all three canonical facts, descendant-restricted linearity, literal `Gamma` closure, quotient relations, path/adjacency boundary, truth lemma, omitted derivations, and decidability boundary are exact. Authority: printed pp. 169 and 171--172, with the p. 172 crop controlling closure. Artifact: reader lines 1651--1756; source note lines 760--939; ledger line 179.

### C7 - checked clean

The literal p. 173 equations and schemes, the separating countermodel, the possible-but-unprinted `GA` to `G^0A` repair, exact `D^0X/D^0UX` languages and source-claimed completeness, absent separate proof, unresolved `D^0UX` qualification, and later-history separations are all explicit. Authority: printed p. 173. Artifact: reader lines 1758--1817; source note lines 941--1070 and 1072--1090; ledger line 181.

### C8 - checked clean

The strict/inclusive equations and recursive translations are mathematically correct on `N`: shared lines 636--680. `tau` has the correct witness/interval operand reversal and `X/Y` shift; `sigma` defines next/previous with strict prefix `U/S` and `bottom`, and translates inclusive strong until/since by the current-target disjunct plus current-left/strict-interval case. The public theorem has the exact pointed-infinite-word domain and citations at lines 684--691. Reader, source note, ledger, and bibliography contain no contradictory identity, semantics, theorem-domain, or `U^0/D^0UX` claim. R2-SF-01 is an omitted reader referral, not a contradictory translation or bibliographic claim.

### C9 - REVISE

The terminology rule, definition-before-use order, typed translations, exact quantifiers, source-defect ownership, and anti-retrojection boundaries are otherwise satisfied. Handbook-introduced `U_s`,`S_s`,`Pr`,`A*(x)`,`tau`, and `sigma` have local definitions, standing, necessity/nonredundancy, and use; undefined source `S'`,`U'` and event expressions remain reported as missing artifacts. R2-SF-01 is nevertheless an omitted qualification in a paragraph presented as the complete proof-ownership account, so the prose is not yet complete for its stated scope.

## Invariant-by-invariant disposition

- **I1 - satisfied.** I used complete source reading, mathematical reasoning, provenance/metadata inspection, and prose inspection only. I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds.
- **I2 - satisfied.** Every replacement hash matched twice; only the round-two snapshot was reviewed.
- **I3 - satisfied.** Printed pp. 163--173 were all visually reread. Images controlled over OCR, prior notes, and memory. The p. 170 crop settled the inclusive signs.
- **I4 - satisfied.** The p. 164 inequality remains visible and its future direction is a handbook repair; no-successor `X`, handbook `S_s`, and temporal-to-first-order recursion retain explicit ownership. Reader lines 1248--1286 and 1500--1525.
- **I5 - satisfied.** GPSS strict infix `U_s`, Kamp strict prefix `U/S`, handbook inclusive strong `U/S`, and the conflicting p. 173 `U^0` displays remain separate. No coherent `U^0` standing is silently imposed. Reader lines 1264--1328 and 1758--1810; shared lines 636--680.
- **I6 - satisfied.** Grammar, expressive equivalence, theorem hypotheses, proof status, and deductive completeness remain distinct. No GPSS truth clause or arity is invented for `S`,`S'`, or `U'`. Reader lines 1274--1286 and 1545--1552.
- **I7 - satisfied.** Theorem 2.2 and Theorem 3.2 remain outlines; Proposition 2.4, Theorem 2.3, Theorem 2.5, Theorem 3.1, and the canonical-model omissions are not promoted. R2-SF-01 concerns missing referral ownership, not a false full-proof claim.
- **I8 - satisfied.** No later LTL name, automata/Buchi translation, small-model bound, PSPACE classification, or model-checking theorem is retrojected. Reader lines 1751--1756 and 1812--1817.
- **I9 - satisfied.** Every handbook-introduced technical name has local definition/axiom, standing, nonredundancy, necessity, and actual use; undefined source labels remain missing artifacts rather than new handbook objects.
- **I10 - satisfied.** I filed independently, did not open any prohibited board/reviewer file, and contacted no reviewer.
- **I11 - requires REVISE.** The supported C5/C9 omission keeps N-c-012.c open regardless of the ten successful mandatory repairs.
- **I12 - observed.** This verdict concerns only the frozen round-two N-c-012.c topic scope. It does not close N-c-012.d, N-c-012 as a whole, Part IX, source-wide ledgers, a publication build, rendered-page review, human review, final-book completion, or user acceptance.

## Conclusion

The round-two snapshot correctly incorporates all mandatory repairs F01--F10 and is otherwise source-faithful across C1--C9 and I1--I12. It still omits one explicit proof-provenance sentence from printed p. 170: GPSS says its presented proof of Theorem 2.2 follows `[SS]`. Because C5 expressly requires the external proof referrals and the charter makes any supported omission non-outvotable, the source-fidelity verdict is **REVISE**.
