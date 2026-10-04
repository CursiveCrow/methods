ACCEPT

# Round-four source-fidelity review: N-c-012.c

## Reviewer, independence, and method

- Stable agent identifier: `/root/schmidt_smolka_1991_research/gpss_primary_pass`.
- Runtime exposure: the exact serving model, version, and build identifier were not exposed to this seat. The runtime exposed only the Codex/GPT-5-family role context.
- Review date: 2026-08-23.
- I read the complete updated charter before substantive review and reviewed only the round-four frozen artifact snapshot.
- I independently reread every printed authority page, pp. 163--173, from `tmp/pdfs/p09-gpss-1980/page-01.png` through `page-11.png` at original image detail. I also reread both controlling high-resolution crops.
- I did not read `spec/research/boards/p09-n-c-012c/ledger.md`, `transcript/chair.md`, any round-one, round-two, or round-three transcript (including my own), or another reviewer's transcript or verdict. I did not contact another reviewer.
- I created only this assigned transcript. I did not edit the manuscript, shared integration, bibliography, source note, source-presentation ledger, charter, or any other file.
- This was book scholarship only. I ran no test, test harness, automated checker, repository script, TeX command, handbook-PDF inspection, or build. The only mechanical operation relevant to the verdict was the charter-required SHA-256 verification of the frozen files.

## Frozen round-four hash verification

Every round-four frozen hash was verified before substantive review and reverified immediately before filing. All eight matched exactly:

| Frozen item | Required and observed SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf` | `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2` | exact match |
| `tmp/pdfs/p09-gpss-1980/page-08-quantifier-symbols.png` | `D74FF885AC1010EA703749F215D1E47DFB3649595F3F8C0A282E073DB714C0F9` | exact match |
| `tmp/pdfs/p09-gpss-1980/page-10-closure-crop.png` | `F49C546E4F07A005BA548AB594C6F63B01B37FC62FE3D8DD89A3FAE44EAEA434` | exact match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `DD9DF6D66A6632D98DBF88DD9968C299320B103F317932C836D624D21E76033F` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `DAE8982D6CAA548BEBCB916B197399B6499A7C6DB966E6972CC4E2C50AC163BA` | exact match |
| `handbook/bib/handbook.bib` | `BB4096F50E3359E2F07187E1B898F8A8E65CF4A3AC3C288E3FA58099A2A53380` | exact match |
| `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` | `038BB890132E61EABB91540EA6CC8BAEC5BFF897FC749FD52CEBD69FCBE2B060` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `F0681E77E779236104BF4B490FFCBA9400068AF0026F360A7F1CF0B740EE40CD` | exact match |

## Complete visual authority read record

The source PDF is the controlling authority. The page images and crops were used only as visual reading derivatives. No OCR reading was substituted for the printed pages.

| Image | Printed page | Material visually reread | Disposition |
|---|---:|---|---|
| `page-01.png` | 163 | title, all four authors and affiliations, abstract, both rights notices, introduction, informal strict (F,G,X,U) clauses | checked clean against artifact |
| `page-02.png` | 164 | grammar, model, clauses (1)--(5), the literal past-pointing (F) inequality, one-sided (X) clause, strict (U), omega-models, (L(U)), execution sequences, partial correctness | checked clean; defects and repairs are explicitly owned |
| `page-03.png` | 165 | total correctness, invariance/eventuality lists, claimed need for (U) | checked clean |
| `page-04.png` | 166 | insistence, busy wait, weakest acceptable behaviour, minimum scheduler fairness, persistence | checked clean |
| `page-05.png` | 167 | semaphore, conditional critical region, impulse, beginning of unsolicited-response example | checked clean |
| `page-06.png` | 168 | unsolicited response, (operatorname{Pr}), FIFO, proposed semaphore instance, printed repeated-response refinement, four questions | checked clean |
| `page-07.png` | 169 | Kamp and prior-system boundaries, (L_1), order classes, and the respective `[P2]`/`[MY]` attribution | checked clean |
| `page-08.png` | 170 | Theorems 2.1--2.3, future-formula signs, proof-of-2.2 heading, (operatorname{At}), (operatorname{Bet}), special and decomposition formulas | checked clean |
| `page-09.png` | 171 | Main Lemma, Proposition 2.4, event-expression outline, Theorem 2.5, (DX/DUX), Theorems 3.1--3.2 | checked clean |
| `page-10.png` | 172 | maximal-theory construction, literal (Gamma)-closure obligations, quotient relations, path construction, truth lemma, decidability | checked clean |
| `page-11.png` | 173 | (F^0,G^0,U^0), transformed schemes, (D^0X/D^0UX), and the complete source-local bibliography | checked clean |
| `page-08-quantifier-symbols.png` | 170 | controlling enlargement of the two future-formula quantifier restrictions | both signs are inclusive: ((\forall y\ge x)) and ((\exists y\ge x)) |
| `page-10-closure-crop.png` | 172 | controlling enlargement of the (Gamma)-closure symbols | confirms the three literal obligations reported below |

The page-to-content map in `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:48-105` agrees with this fresh visual read.

## Frozen artifact scope reread

I reread the complete frozen topic scope, not only the round-four edits:

- reader presentation: `handbook/parts/p09/presentations/n-c-012.tex:1206-1850`;
- shared strict/inclusive bridge and public theorem: `handbook/parts/p09/logic-in-computer-science.tex:602-691`;
- bibliography entry: `handbook/bib/handbook.bib:194-207`;
- complete source note: `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:1-1179`;
- source-presentation record: `spec/research/p09-source-presentations-lot2-3.md:169-184`.

## Source-local reference identities and acquisition boundary

I visually reread the complete reference list on printed p. 173 and checked the frozen source-key map at `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:107-124`. The following identities and uses are correctly separated from acquisition or independent verification:

| GPSS key | Identity printed on p. 173 | Topic use and verified boundary |
|---|---|---|
| `[FL]` | M. J. Fischer and R. L. Ladner, “Propositional Modal Logic of Programs,” Ninth ACM Symposium on Theory of Computing, Boulder, Colorado, May 1977 | GPSS comparison only; no proof body is imported. Source note lines 117 and 964--967. |
| `[G1]` | D. Gabbay, “Axiomatization of Logic of Programs,” manuscript, November 1977 | GPSS comparison only; no separate acquisition or verification is asserted. Source note lines 118 and 964--967. |
| `[G2]` | D. Gabbay, “The Separation Property of tense Logics,” manuscript, September 1979 | GPSS refers Theorem 2.3's direct syntactic proof to this manuscript; neither body acquisition nor independent verification is claimed. Reader lines 1654--1658; source note lines 119 and 619--624; source-presentation record line 177. |
| `[MP]` | Z. Manna and A. Pnueli, “The Modal Logic of Programs,” International Conference in Automata, Languages and Programming, Graz, July 1979 | Identification only in this topic; “Automata” is part of the venue title and supports no automata construction claim. Source note line 120. |
| `[MY]` | T. J. Myers and A. Pnueli, “The Temporal Situation Until Now,” University of Pennsylvania technical note, 1979 | Respectively the earlier (DUX/L(X,F,U)) proposal and the equivalent (D^0UX) attribution; no body acquisition or verification is claimed. Reader lines 1662--1673 and 1838--1840; source note lines 121 and 534--541; source-presentation record line 179. |
| `[P1]` | A. Pnueli, “The Temporal Logic of Programs,” “19th Annual Symp. on Foundations of Computer Science,” Providence, Rhode Island | The literal `19th` is preserved as GPSS's printed bibliographic discrepancy. The separately acquired/publisher-identified 1977 paper is the 18th FOCS paper, pp. 46--57, DOI `10.1109/SFCS.1977.32`; the frozen artifact does not silently repair GPSS. Source note line 122; source-presentation record line 181; publisher record `https://ieeexplore.ieee.org/document/4567924`. |
| `[P2]` | A. Pnueli, “The Temporal Semantics of Concurrent Programs,” International Symposium on Semantics of Concurrent Computation, Evian, July 1979 | Respectively the earlier (DX/L(X,F)) proposal; no body acquisition or verification is claimed. Reader lines 1662--1673; source note lines 123 and 534--541; source-presentation record line 179. |
| `[SS]` | S. Shelah and J. Stavi, “Expressive Completeness for Temporal Logic,” forthcoming | GPSS says its presented Theorem 2.2 outline follows this work; the body is neither reproduced, imported, nor independently verified. Reader lines 1556--1563; source note lines 124 and 666--785; source-presentation record line 177. |

The exact p. 169 respective mapping is therefore:

1. `[P2]` (longmapsto DX) for (L(X,F));
2. `[MY]` (longmapsto DUX) for (L(X,F,U)).

The order is correct in `handbook/parts/p09/presentations/n-c-012.tex:1662-1673`, `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:534-541`, and `spec/research/p09-source-presentations-lot2-3.md:179`. No artifact reverses the two sources or treats either external completeness claim as independently proved.

## Criteria C1--C9

### C1 — ACCEPT

Printed p. 163 and the author-archive record establish the four-author title, POPL 1980 venue, pp. 163--173, DOI, and published-version standing. The embedded `Author` field omits Dov Gabbay but retains Pnueli, Shelah, and Stavi; the printed page controls. The later metadata dates, archive header, rights notice, public-inspection boundary, and lack of evidence for archive/ACM byte identity are all reported. Evidence: printed p. 163; reader `1208-1225`; source note `3-105`; bibliography `194-207`; source-presentation record `171`.

### C2 — ACCEPT

The artifact gives the exact linear-order model ((T,<,Q_0,Q_1,\ldots)), distinguishes atom (q_i) from its interpretation (Q_i), includes all four printed Boolean constructors and primitive (F,X,U), and keeps derived (G) and Section 3's basis change distinct. It preserves strict witness/order semantics, the literal p. 164 (m_1<m) conflict, handbook-owned coherent-future repair, handbook-owned no-successor totalization, syntactic-versus-expressive (L(U)), absent printed (S) semantics, local eliminable (U_s/S_s) standing, reversed Kamp operand order, and the strict/inclusive bridge. Evidence: printed pp. 163--164; reader `1227-1328`; shared integration `602-681`; source note `126-270`; source-presentation record `173`.

### C3 — ACCEPT

The presentation defines execution sequences, nondeterminism, program location, (mathit{at}_\ell), the current-value tuple, remembered-input tuple, precondition, and postcondition before use. It distinguishes partial and total correctness; preserves the invariance/eventuality lists without retrojecting later semantic classes; correctly separates insistence, persistence, and impulse; and accurately gives busy-wait, semaphore, guarded-region, unsolicited-response, (operatorname{Pr}), FIFO, implementation-specific semaphore, and repeated-response examples. The three exact (operatorname{Pr}) uses are identified. Evidence: printed pp. 164--168; reader `1330-1470`; source note `271-506`; source-presentation record `175`.

### C4 — ACCEPT

The four source questions remain four: eliminability of (U) from (F,X), expressive completeness of (L(U)), a system for (L(F,X)), and a system for (L(F,X,U)). The Kamp IV.3 attribution is reported at its literal boundary rather than promoted into an unprinted reduction. (L_1), equality, (<), unary predicates, complete and discrete orders, example order classes, and the inclusive future quantifier restrictions are exact. The temporal-to-first-order recursion and past clause are explicitly handbook-supplied. Evidence: printed pp. 168--170 and controlling p. 170 crop; reader `1472-1529`; source note `507-570`; source-presentation record `177`.

### C5 — ACCEPT

The unequal domains are exact: Theorem 2.1 is arbitrary one-free-variable (L_1) formulas only at point 0 of all omega-models; Theorem 2.2 is future (L_1) formulas at every point of discrete complete models; Theorem 2.3 is past/future separation over discrete complete models; Proposition 2.4 is not renamed a theorem; Theorem 2.5 is arbitrary linear orders only with undefined (S',U'). The artifact accurately gives (operatorname{At}), (operatorname{Bet}_n), before/after, special and decomposition formulas, Main Lemma, and the cofinal conjuncts, while preserving the absent induction, event-expression grammar/semantics, complement construction, arbitrary-complete-order modifications, dual proof, Theorem 2.5 proof, Theorem 2.3 body, and 2.1/2.2 numbering tension. Evidence: printed pp. 170--171; reader `1531-1660`; source note `571-785`; source-presentation record `177`.

### C6 — ACCEPT

The artifact gives the exact (DX/DUX) languages, primitive-basis change, A1--A5, U1--U2, and the three rules; it separates source-reported earlier proposals, Theorem 3.1 soundness without proof, and Theorem 3.2 weak theoremhood completeness outline. Maximal consistency is typed relative to the relevant system. The unprinted selection of (Delta_0), three exact canonical assertions, restricted linear domain, literal (Gamma) closures, finite-up-to-equivalence statement, unprinted quotient-finiteness argument, quotient relations, transitive-closure claim, adjacency omission, fair-thread construction, truth lemma, proof omissions, and bound-free decidability claim are all preserved. Evidence: printed pp. 169 and 171--172 plus controlling p. 172 crop; reader `1662-1787`; source note `786-978`; source-presentation record `179`.

The crop confirms these exact closure obligations:

\[
FA\in\Gamma\Rightarrow XA,XFA\in\Gamma,
\qquad
XA\in\Gamma\Rightarrow X\neg A\in\Gamma,
\]

\[
A\mathbin{\mathsf U_s}B\in\Gamma
\Rightarrow FB,XA,XB,X(A\mathbin{\mathsf U_s}B)\in\Gamma.
\]

### C7 — ACCEPT

The artifact preserves (F^0A\equiv A\lor FA), (G^0A\equiv A\land GA), the literal (GA\lor B\lor(A\land(AU_sB))) equation, A0/U0 schemes, and the exact omega-model separating that equation from U0.2. Replacing (GA) by (G^0A) is labelled only a possible unprinted repair. (U^0) receives no silently coherent standing. The exact (D^0X/D^0UX) languages and source-claimed completeness strengths are stated without inventing a separate p. 173 proof, and (D^0UX) remains qualified by the source conflict. The topic is separated from Part VIII strong until and from later LTL, automata, complexity, and model-checking results. Evidence: printed p. 173; reader `1789-1849`; source note `979-1109`; source-presentation record `181`.

### C8 — ACCEPT

The recursive translations are mathematically and conventionally correct. In particular, strict (U,B,A) maps to (X(\tau(A)\,U\,\tau(B))), strict (S,B,A) maps to (Y(\tau(A)\,S\,\tau(B))), (X A) maps back to (U\,\sigma(A)\,\bot), and (Y A) maps back to (S\,\sigma(A)\,\bot). Inclusive (U,S) map back by the current-(B) or current-(A)-plus-strict-witness disjunctions. The functions are eliminable metalinguistic translations, not new connectives. The public theorem is exactly about pointed infinite words over ((\mathbb N,<)), and its citations and grammar requirements are consistent with the reader, note, ledger, and bibliography. Evidence: reader `1307-1328` and `1844-1849`; shared integration `625-691`; source note `1038-1109`; bibliography `194-207`.

### C9 — ACCEPT

The prose is independently reconstructed, source defects and handbook repairs are visibly separated, definitions precede uses, and all introduced warning notation and metalinguistic abbreviations have necessity, exact eliminable definitions, standing, nonredundancy, and actual downstream use. Undefined source labels (S,U',S'), event expressions, and (U^0) are reported as missing or conflicting artifacts rather than adopted as new defined handbook objects. No unsupported later theorem or source-body verification is added. Evidence: complete reader `1206-1850`, shared integration `602-691`, source note `1-1179`, and source-presentation record `169-184`.

## Invariants I1--I12

| Invariant | Disposition and evidence |
|---|---|
| I1 | ACCEPT. Review used visual source reading, mathematical reasoning, and prose inspection only; no prohibited tests, scripts, TeX, handbook PDF, or builds. |
| I2 | ACCEPT. All eight round-four frozen hashes matched twice; no mismatch occurred. |
| I3 | ACCEPT. Every printed page 163--173 was visually reread; images controlled, and the p. 170 crop settled both inclusive signs. |
| I4 | ACCEPT. The literal p. 164 past-pointing (F) inequality remains visible; coherent future, no-successor (X), translations, and past clauses are all explicitly handbook-owned where supplied. Reader `1243-1262`, `1274-1286`, `1502-1527`. |
| I5 | ACCEPT. GPSS strict infix (U), Kamp strict prefix (U/S), handbook inclusive strong (U/S), and conflicting (U^0) are kept separate in semantics, operand order, present inclusion, and witness requirement. Reader `1264-1328`, `1789-1842`; shared integration `625-681`. |
| I6 | ACCEPT. Grammar, expressive equivalence, theorem hypotheses, and deductive completeness are distinct; absent (S,S',U') semantics and proof are not supplied. Reader `1233-1242`, `1300-1302`, `1531-1554`, `1662-1703`. |
| I7 | ACCEPT. Theorem 2.2 and Theorem 3.2 remain outlines; Proposition 2.4 machinery, Theorems 2.3 and 2.5, Theorem 3.1 proof, and canonical-model derivations remain omitted. Reader `1556-1660`, `1694-1703`, `1720-1787`. |
| I8 | ACCEPT. No later LTL name, Büchi/automata translation, small-model bound, PSPACE class, or model-checking theorem is attributed to GPSS. Reader `1472-1478`, `1782-1787`, `1844-1849`; source-presentation record `181`. |
| I9 | ACCEPT. Local (U_s/S_s), (A^*), (operatorname{Pr}), (	au), and (sigma) satisfy the terminology rule; missing source notions remain explicitly owed/missing. Reader `1264-1291`, `1433-1445`, `1498-1506`, `1547-1551`, `1636-1647`; shared integration `648-681`. |
| I10 | ACCEPT. I filed independently and did not inspect any prohibited board ledger, chair transcript, prior transcript, reviewer transcript, or verdict, and contacted no reviewer. |
| I11 | ACCEPT. This verdict records only this seat's independent conclusion and does not infer acceptance from another seat or a vote. |
| I12 | ACCEPT. The source-presentation record line 183 expressly limits topic acceptance and leaves section admission, final build, rendered inspection, human review, final-book completion, and user acceptance open. |

## Mandatory checks F01--F16

| Check | Disposition and precise evidence |
|---|---|
| F01 | ACCEPT. Embedded `Author` is Pnueli, Shelah, and Stavi, omitting only Gabbay; printed authorship controls; the hash pins the archive object without asserting ACM byte identity. Printed p. 163; reader `1208-1225`; source note `20-46`; ledger line `171`. |
| F02 | ACCEPT. Initial grammar has (q_i), negation, conjunction, disjunction, implication, primitive (F,X,U), and derived (G); (q_i\ne Q_i); Section 3's primitive (G,X,U) with derived (F) remains distinct. Printed pp. 164, 171; reader `1227-1242`, `1674-1676`; ledger line `173`. |
| F03 | ACCEPT. Local (Gp) means (p) at every strictly later point and is not eventual permanence; the globally prefixed form repeats the local obligation at every later reference. Printed p. 166; reader `1363-1389`; ledger line `175`. |
| F04 | ACCEPT. Busy wait retains “weakest acceptable semaphore behaviour,” “minimal fairness requirement,” and the explicit infinite-overtaking warning. Printed pp. 166--167; reader `1391-1408`; ledger line `175`. |
| F05 | ACCEPT. (mathit{at}_\ell), current tuple (\bar y), remembered-input tuple (\bar\xi), precondition (\varphi), and postcondition (\psi) are exactly typed before use. Printed pp. 164--165; reader `1331-1356`; ledger line `175`. |
| F06 | ACCEPT. The FIFO semaphore formula is an implementation-specific possible basic axiom, not a theorem of temporal logic. Printed p. 168; reader `1452-1460`; ledger line `175`. |
| F07 | ACCEPT. Lemma 1 is an unprinted induction essentially following Kamp Chapter II Theorem 1. Printed p. 170; reader `1605-1610`; ledger line `177`. |
| F08 | ACCEPT. The three canonical assertions are exactly typed; branching linearity is over members of (S), and the resulting order claim is restricted to ({\Delta\in S:\Delta=\Delta_0\text{ or }\Delta_0<\Delta}); absent derivations remain absent. Printed p. 172; reader `1705-1737`; ledger line `179`. |
| F09 | ACCEPT. (D^0X) is claimed complete for (L(G^0,X)), (D^0UX) for (L(G^0,X,U^0)), and no separate p. 173 proof is invented. Printed p. 173; reader `1818-1841`; ledger line `181`. |
| F10 | ACCEPT. Literal (U^0) equation and U0.2 are both preserved; the omega-countermodel separates them; (GA\mapsto G^0A) is only a possible unprinted repair; no coherent (U^0) standing is assigned; the (D^0UX) qualification is consistent. Printed p. 173; reader `1789-1838`; ledger line `181`. |
| F11 | ACCEPT. Maximal consistency is relative to (DX) or (DUX); the unprinted standard choice of (Delta_0\ni A_0) is identified; the restricted domain is displayed without relying on an undefined “descendant”; (s_0=\Delta_0\cap\Gamma) contains (A_0). Printed p. 172; reader `1705-1712`, `1733-1737`, `1762-1763`; ledger line `179`. |
| F12 | ACCEPT. The reader does not call syntactic (Gamma) literally finite. It reports only finitely many formulas up to logical equivalence, preserves every crop-confirmed closure obligation, and leaves the finite quotient and unprinted supporting argument explicit without selecting representatives. Printed p. 172 and controlling crop; reader `1738-1755`; ledger line `179`. |
| F13 | ACCEPT. GPSS's proof-of-2.2 outline is reported as following `[SS]`, the forthcoming Shelah--Stavi manuscript; no body import or independent verification is claimed. Printed pp. 170, 173; reader `1556-1563`; source note lines `124`, `666-785`; ledger line `177`. |
| F14 | ACCEPT. `[G2]`, `[P2]`, and `[MY]` are expanded at first reader-facing use; the `[P2]`/`[MY]` respective mapping is exact; all proof/proposal attributions distinguish GPSS's report from external acquisition or verification; the source note maps `[FL]`, `[G1]`, `[G2]`, `[MP]`, `[MY]`, `[P1]`, `[P2]`, `[SS]`; the P1 `19th`/18th discrepancy is preserved; every key used in the ledger is locally identified. Printed pp. 169, 173; reader `1654-1658`, `1662-1673`, `1838-1840`; source note `107-124`, `534-541`, `619-624`, `964-967`; ledger `177-183`. |
| F15 | ACCEPT. The p. 168 formula is identified as the source's printed repeated-response refinement and is nowhere called a handbook repair. Reader `1441-1443`, `1461-1467`; source note `460-506`; ledger line `175`. |
| F16 | ACCEPT. (operatorname{Pr}) is locally defined and typed as a metalinguistic formula abbreviation, and its use statement identifies exactly the next three displays: general FIFO, implementation-specific semaphore instance, repeated-response refinement. Reader `1433-1467`; ledger line `175`. |

## Findings and verdict basis

No source-fidelity defect, ambiguity left undisclosed, unsupported acquisition claim, incorrect source-local identity, reversed `[P2]`/`[MY]` mapping, silent P1 venue repair, convention conflation, proof promotion, technical-name violation, or cross-file inconsistency remains in the frozen round-four scope. I have no unresolved uncertainty. C1--C9, I1--I12, and F01--F16 are all checked clean, so the required verdict is **ACCEPT**.
