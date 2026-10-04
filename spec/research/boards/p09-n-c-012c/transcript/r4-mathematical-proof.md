ACCEPT

# Round-four mathematical/proof review: N-c-012.c GPSS 1980

## Reviewer identity, independence, and method

- Stable agent identifier: `/root/schmidt_smolka_1991_research`.
- Runtime model/version: not exposed by the runtime.
- Seat: mathematical/proof.
- I read the complete updated charter before substantive review and used only its frozen round-four snapshot.
- I did not read or seek `ledger.md`, `transcript/chair.md`, any round-one, round-two, or round-three transcript (including my own), or any other reviewer's transcript or verdict. I did not contact another reviewer.
- Although I authored the research note, I did not treat it as authority for its own claims. I judged the reader and shared theorem directly against a fresh visual reading of the complete primary article; the source note was checked afterward as a separate provenance surface.
- I made no manuscript, shared-file, bibliography, ledger, source-note, or board-record edit. This transcript is the only file I created.
- I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds. The only command-line operations were read-only text inspection, source-PDF metadata inspection, archive-record inspection, and SHA-256 identity hashing; the mathematical source was read from page images and the two controlling crops.

## Frozen identities

I recomputed all eight identities before substantive review and again immediately before filing. Each matched the charter's round-four value:

1. `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf` — `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2`.
2. `tmp/pdfs/p09-gpss-1980/page-08-quantifier-symbols.png` — `D74FF885AC1010EA703749F215D1E47DFB3649595F3F8C0A282E073DB714C0F9`.
3. `tmp/pdfs/p09-gpss-1980/page-10-closure-crop.png` — `F49C546E4F07A005BA548AB594C6F63B01B37FC62FE3D8DD89A3FAE44EAEA434`.
4. `handbook/parts/p09/presentations/n-c-012.tex` — `DD9DF6D66A6632D98DBF88DD9968C299320B103F317932C836D624D21E76033F`.
5. `handbook/parts/p09/logic-in-computer-science.tex` — `DAE8982D6CAA548BEBCB916B197399B6499A7C6DB966E6972CC4E2C50AC163BA`.
6. `handbook/bib/handbook.bib` — `BB4096F50E3359E2F07187E1B898F8A8E65CF4A3AC3C288E3FA58099A2A53380`.
7. `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` — `038BB890132E61EABB91540EA6CC8BAEC5BFF897FC749FD52CEBD69FCBE2B060`.
8. `spec/research/p09-source-presentations-lot2-3.md` — `F0681E77E779236104BF4B490FFCBA9400068AF0026F360A7F1CF0B740EE40CD`.

## Complete authority read

I visually reread every authority page from `page-01.png` through `page-11.png`, corresponding without a wrapper to printed pp. 163--173. I checked, page by page:

- p. 163: title/authors, rights notice, program-reasoning frame, and the informal strict (F,G,X,U) clauses;
- p. 164: complete grammar, arbitrary linear-order model, clauses (1)--(5), the reversed (F) inequality, the one-sided (X) clause, ω-models, (L(U)), the (F/X) eliminations, executions, and partial correctness;
- p. 165: total correctness, complete invariance/eventuality lists, and the transition to response conditions;
- p. 166: insistence, its equivalent form and global version, busy waiting, minimal fairness, infinite overtaking, and the start of persistence;
- p. 167: persistence, semaphore and guarded-region formulas, implementation qualifications, impulse, and the start of unsolicited response;
- p. 168: unsolicited response, Π/`Pr`, both FIFO displays, the repeated-response refinement, and all four questions;
- p. 169: Kamp attribution, the exact respective [P2]/[MY] proposal report, (L_1), models, completeness/discreteness/ω-model definitions, examples of order classes, and the natural translation assertion;
- p. 170: Theorems 2.1--2.3, the inclusive ≥ signs in the future-formula definition, [G2] referral, [SS] ownership, “Proof of 2.2 (outline),” Τ/`At`, `Bet`, special formulas, Lemma 1, and the decomposition display;
- p. 171: the Main Lemma, Proposition 2.4 and the complete printed event-expression argument, the printed “yields theorem 2.1” tension, Theorem 2.5, the exact DX/DUX schemes and rules, and Theorems 3.1--3.2;
- p. 172: maximal theories, Δ-selection, the three canonical facts, exact restricted order domain, literal Γ closure, finite-modulo-equivalence claim, quotient relations, transitive-closure lemma, path prose and formal recurrence condition, valuation, truth lemma, and unquantified decidability referral; and
- p. 173: the (F^0,G^0,U^0) equations, transformed schemes, transformed-system claims, [MY] sentence, and complete reference list.

I also visually reread the controlling p. 170 crop and confirmed that both displayed restricted quantifiers are inclusive, ((\forall y\ge x)) and ((\exists y\ge x)), and the controlling p. 172 crop and confirmed all three literal Γ obligations, including the easily misread (XA\in\Gamma\Rightarrow X\neg A\in\Gamma). Images controlled over OCR and prior notes.

## Findings

No blocker, must-fix defect, unsupported mathematical assertion, source-strength inflation, unresolved terminology violation, or cross-file contradiction remains in the frozen round-four unit.

## Criterion-by-criterion disposition

### C1 — identity, provenance, page map, metadata, and rights: clean

The reader's identity/provenance paragraph at `n-c-012.tex:1208-1225`, the source note at lines 5--105, the ledger at lines 169--171, and `handbook.bib:194-206` agree on the four authors, title, POPL 1980 identity, pp. 163--173, DOI `10.1145/567446.567462`, eleven physical pages with no wrapper, archive URL, and the narrow rights boundary. The live author-archive record identifies the download as the published 11-page version. Read-only PDF metadata inspection independently showed 11 pages and an embedded `Author` field of `A. Pnueli, S. Shelah and J. Stavi`; the reader correctly says this omits Dov Gabbay and lets the printed four-author title page control. The hash is expressly limited to the author-archive object and is not represented as ACM byte identity.

### C2 — model, syntax, strict semantics, defects, and convention bridge: clean

`n-c-012.tex:1227-1328` exactly separates formula atoms (q_i) from their interpretations (Q_i), gives all four printed Boolean connectives and primitive (F,X,U), keeps (G=\neg F\neg) derived in the initial presentation, and keeps Section 3's later primitive-basis change distinct. The strict witness/open-interval semantics and reversed GPSS/Kamp operand order are exact. The literal p. 164 (m_1<m) defect remains visible at lines 1248--1258, while (m<m_1) is explicitly handbook-owned as the coherent repair. The absent no-successor half of the (X) clause and its handbook totalization are disclosed at lines 1243--1246 and 1259--1262. The (L(U)) grammar/expressive-power overload is correctly separated at lines 1300--1302.

The local “strict” symbols at lines 1264--1290 satisfy the terminology rule: necessity is the collision with the reused inclusive symbols and reversed Kamp prefix order; (\mathsf U_s) and the handbook-supplied (\mathsf S_s) receive exact eliminable clauses; they stand as formula constructors, not named new logics; nonredundancy is stated; and they are used throughout the presentation and bridge. The four bridge equations at lines 1307--1325 are mathematically correct on ω-words. In particular, (A\mathbin{\mathsf U_s}B\equiv\mathsf X(A\mathbin{\mathsf U}B)), its past dual, and both inclusive reconstructions preserve witness position and interval operand; lines 1325--1328 correctly reject (XA\equiv\bot\mathbin{\mathsf U}A).

### C3 — program frame, correctness, fairness examples, and `Pr`: clean

`n-c-012.tex:1330-1470` gives the exact execution-sequence standing, nondeterminism qualification, current location, current-value tuple, remembered-input tuple, precondition, and postcondition before using them. The partial- and total-correctness displays have the source's exact temporal force. The complete invariance and eventuality inventories are preserved and are not conflated with later semantic safety/liveness classes.

All response examples are present with the printed strict convention: local/global insistence, persistence, and impulse; both equivalent negative-(G) forms; busy waiting with weakest-acceptable-behaviour/minimal-fairness calibration and infinite-overtaking warning; semaphore persistence; both guarded-region conditions and their implementation boundary; unsolicited response; general FIFO; the implementation-specific semaphore axiom; and the repeated-response formula. Lines 1375--1379 correctly distinguish strict (Gp) from (FGp). Lines 1452--1460 correctly make the semaphore FIFO display a proposed implementation axiom rather than a temporal theorem.

At lines 1433--1445, `Pr` has an exact eliminable definition and is classified as a metalinguistic formula abbreviation, not a connective or execution relation. Its necessity/nonredundancy is the first-occurrence ordering condition, and its use statement names exactly the three following displays: general FIFO, semaphore-instance FIFO, and repeated-response refinement. Lines 1461--1467 call the last display the stronger source formula and use the word “refinement” in the immediately governing use statement; nothing calls it a handbook repair. This agrees with the source note's explicit “printed refinement” record at lines 491--501 and with printed p. 168.

### C4 — questions, Kamp boundary, first-order language, and forward translation: clean

The four questions are all present at `n-c-012.tex:1472-1478`. The reader does not inflate literal Kamp IV.3: lines 1480--1486 say that the thesis theorem is the integer-order `ISOLP`/`ISOLF` result and that GPSS does not print the extra reduction to (U)-nondefinability. Lines 1488--1503 exactly give equality, (<), unary (q_i), the nonempty-bounded completeness definition, discreteness with possible endpoints, the four source order examples, and the ≥-restricted future-formula definition. Lines 1502--1528 explicitly own the displayed recursive temporal-to-first-order translation as a handbook spelling-out of the source's merely “natural” map. Every constructor has the correct free-variable typing, strict witness/interval order, and homomorphic Boolean boundary.

### C5 — result strength and expressive-completeness proof ownership: clean

`n-c-012.tex:1531-1554` keeps the four unequal result domains separate: Theorem 2.1 is arbitrary one-free (L_1) only at 0 of ω-models; Theorem 2.2 is future (L_1) at every point of every discrete complete model; Theorem 2.3 is past/future separation over discrete complete models; and Theorem 2.5 reaches arbitrary linear orders only with the unsemantified (S',U'). Lines 1547--1551 correctly refuse to adopt the gap symbols as defined handbook operators.

Lines 1556--1660 reproduce the complete local architecture at its printed strength: [SS] ownership without importing that body; exact `At`, `Bet_n`, `Bet`, `Aft`, `Bef`; special-formula standing; Lemma 1's unprinted induction/Kamp referral; the full decomposition shape and cofinal conjunct; Main Lemma; Proposition 2.4; the only event-expression example and finite-order argument; the missing event-expression grammar/semantics/return translation; the printed “Proof of 2.2 (outline)” versus “yields Theorem 2.1” tension; and the omitted modifications. [G2] is expanded at first reader use as Dov Gabbay's September 1979 manuscript and remains an external, unacquired/unverified proof referral. No outline or referral is promoted to a complete local proof.

### C6 — DX/DUX, canonical outline, truth lemma, and decidability: clean

`n-c-012.tex:1662-1787` preserves the exact respective p. 169 report: [P2], expanded as Pnueli's Evian 1979 work, suggested (DX/L(X,F)); [MY], expanded as the Myers--Pnueli Pennsylvania technical note, suggested (DUX/L(X,F,U)); GPSS says completeness had been claimed without proofs. Lines 1669--1673 distinguish that report from body acquisition or independent verification.

The Section 3 primitive-basis change, languages, A1--A5, U1--U2, propositional-tautology rule, modus ponens, theorem-only (G)-generalization, Theorem 3.1 soundness standing, and both weak theoremhood-completeness clauses of Theorem 3.2 are exact at lines 1674--1703. The systems are formula-theorem systems, not model classes.

The canonical-model account at lines 1705--1787 is also exact at its deliberately incomplete strength. Maximal consistency is relative to the appropriate system; Δ₀'s standard unprinted selection with (A_0\in\Delta_0) is stated; Δ⁺ and (<) are typed; all three asserted facts are quantified; and linearity is restricted to the displayed set (\{\Delta\in S:\Delta=\Delta_0\text{ or }\Delta_0<\Delta\}). The reader does not call Γ literally finite: it preserves the exact closure obligations, says only finitely many formulas up to logical equivalence, reports the finite quotient as a source assertion, and does not silently pick representatives. Both quotient relations and the transitive-closure claim are exact. The intended ρ₊-path adjacency is retained while the later formal source paragraph's omission of that clause is expressly recorded. The valuation and truth lemma are correctly typed, and all major omitted derivations are listed. The decidability corollary remains only an unspecified formula-dependent finite-representation bound; no algorithmic complexity class is inferred.

### C7 — p. 173 transformed systems and the (U^0) conflict: clean

`n-c-012.tex:1789-1849` preserves both coherent equations for (F^0,G^0), the literal printed (U^0) equation with strict (GA), all five transformed A-schemes, both transformed U-schemes, the inference-rule change, and the exact source-claimed completeness languages (L(G^0,X)) and (L(G^0,X,U^0)). It does not invent a separate p. 173 proof.

The displayed ω-countermodel is correct: (A(0)) false, (A(n)) true for (n>0), and (B) always false makes strict (GA) true at 0, hence makes the printed equation's right side true, while (B\lor(A\land X(A\mathbin{\mathsf U^0}B))) is false. The manuscript therefore correctly refuses one coherent defined standing for (U^0). Replacing (GA) by (G^0A) is labelled only a possible unprinted repair, and the (D^0UX) claim remains qualified by the unresolved source conflict. The Part VIII induction calculus, later LTL name, Büchi translation, PSPACE result, and model-checking classifications remain outside this source.

### C8 — shared recursive translations and public theorem: clean

The shared block at `logic-in-computer-science.tex:599-691` is mathematically correct and consistent with the reader. The strict-to-inclusive translation

\[
\tau(U\,B\,A)=\mathsf X(\tau(A)\mathbin{\mathsf U}\tau(B)),
\qquad
\tau(S\,B\,A)=\mathsf Y(\tau(A)\mathbin{\mathsf S}\tau(B))
\]

preserves GPSS/Kamp's witness-first prefix order after reversing it into inclusive infix order. Conversely,

\[
\sigma(\mathsf XA)=U\,\sigma(A)\,\bot,
\qquad
\sigma(A\mathbin{\mathsf U}B)=
\sigma(B)\lor(\sigma(A)\land U\,\sigma(B)\,\sigma(A))
\]

and the past-dual clauses are correct. The false open interval forces the immediate successor/predecessor, and the inclusive reconstruction handles the current-witness case separately. Atomic and Boolean clauses, domains, codomains, standing, nonredundancy, truth-preservation induction, and the need for (X,Y) are all explicit at lines 648--682.

Theorem `thm:p09-ltl-fo` at lines 684--691 is correctly restricted to pointed ω-words and one-free-variable first-order formulas. Its two formulations use either Kamp's strict (U,S) or inclusive strong (U,S) together with (X,Y); it does not falsely credit inclusive (U,S) alone with next-time expressiveness. Its Kamp/GPSS citations and the reader's source-boundary paragraph at `n-c-012.tex:1844-1849` are consistent.

The source note's boundary at lines 1040--1108 and owed-artifact paragraph at lines 1159--1179 agree with the supplied bridge and preserve the anti-automata/anti-complexity boundary. The ledger's N-c-012.c subsection at lines 169--183 and the bibliography entry at lines 194--206 agree with the same identity, theorem domains, proof ownership, (U^0) conflict, and open review status.

### C9 — prose independence, definition order, technical names, and omissions: clean

The presentation is independently worded and does not reproduce long primary-source prose. Every introduced local technical device has necessity, exact eliminable definition or disclosed source axiom, standing, nonredundancy, and actual later use: (\mathsf U_s/\mathsf S_s), `Pr`, the starred first-order translation, and τ/σ all meet the five-part rule at their first use. Source labels lacking definitions—event expressions and (S',U')—are reported as missing artifacts and are not adopted as defined handbook objects. The GPSS subsection begins at line 1206 and ends at line 1849; the Pnueli boundary at lines 1195--1205 and Sistla--Clarke boundary beginning at line 1851 remain distinct, with no attribution leakage.

## Invariant-by-invariant disposition

- **I1: satisfied.** Review was source-image scholarship, mathematical reasoning, prose inspection, metadata inspection, and identity hashing only; prohibited mechanical/build activities were not performed.
- **I2: satisfied.** All eight round-four hashes matched before substantive review and immediately before filing.
- **I3: satisfied.** Every printed page 163--173 and both controlling crops were visually read; the crops settled ≥ and the literal Γ clauses.
- **I4: satisfied.** The reversed p. 164 inequality, handbook future repair, endpoint totalization, recursive translation, and past clause all retain explicit ownership.
- **I5: satisfied.** GPSS strict infix, Kamp strict prefix, reused inclusive strong operators, and the conflicting (U^0) artifacts remain distinct in time inclusion, operand order, witness status, and (X/Y) dependence.
- **I6: satisfied.** Grammar, expressive equivalence, semantic theorem hypotheses, and proof-system completeness remain separate; (S,S',U') are not supplied unprinted source clauses.
- **I7: satisfied.** Every proof outline, referral, and omission is calibrated exactly; none is promoted to a complete local proof.
- **I8: satisfied.** No later LTL, Büchi/automata, explicit small-model, PSPACE, or model-checking claim is retrojected.
- **I9: satisfied.** The five-part technical-name rule is met locally; undefined source terms remain owed/missing artifacts.
- **I10: satisfied.** The review was blind and independent under the stated no-contact/no-transcript boundary.
- **I11: satisfied.** This verdict is independent and not based on a majority or another seat's conclusion.
- **I12: satisfied.** Acceptance is expressly narrow: it supports only N-c-012.c topic-level manuscript review on this exact snapshot. It does not close N-c-012.d, N-c-012 overall, Part IX, source-wide ledgers, a final publication build, rendered-page review, human review, final-book completion, or user acceptance.

## Mandatory repair checks

- **F01: clean.** Embedded author metadata omits only Dov Gabbay; archive-object versus ACM byte-identity boundary is explicit.
- **F02: clean.** Full initial grammar, (q_i/Q_i), derived (G), and the Section 3 basis change are exact.
- **F03: clean.** Local strict (Gp), global prefixed obligation, and (FGp) are not conflated.
- **F04: clean.** Busy-wait calibration and infinite-overtaking qualification are retained.
- **F05: clean.** Program-location and value/formula metavariables are defined with standing before use.
- **F06: clean.** The FIFO semaphore display is implementation-assumption-relative.
- **F07: clean.** Lemma 1's induction and Kamp ownership remain unprinted/referred.
- **F08: clean.** The three typed canonical facts, restricted order domain, and absent derivations are exact.
- **F09: clean.** (D^0X,D^0UX), their languages, and their exact source-claimed completeness strength are preserved without a new proof.
- **F10: clean.** Both conflicting (U^0) displays, the separating model, possible unprinted repair, and qualified transformed completeness claim are consistent across reader, note, and ledger.
- **F11: clean.** Relevant-system maximal consistency, unprinted Δ₀ selection, literal restricted domain, and (s_0=\Delta_0\cap\Gamma\ni A_0) are explicit.
- **F12: clean.** Γ is finite only modulo logical equivalence; the quotient finiteness argument remains unprinted and no representatives are invented.
- **F13: clean.** [SS] is identified, GPSS ownership language is exact, and no external-body verification is claimed.
- **F14: clean.** [G2], [P2], and [MY] are expanded at first reader use with exact respective mappings and body-status boundaries. Source-note lines 107--124 map [FL], [G1], [G2], [MP], [MY], [P1], [P2], and [SS]; the literal p. 173 `19th` for [P1] remains distinguished from the separately acquired Eighteenth-FOCS authority. Every key used in the ledger is locally identifiable.
- **F15: clean.** The p. 168 formula is source-owned as the repeated-response refinement and is never labelled a handbook repair.
- **F16: clean.** `Pr` has formula-abbreviation standing and exactly three named following display uses.

## Final scope boundary

The accepted object is only the eight-identity round-four N-c-012.c snapshot named above. No conclusion is drawn about another hash, another topic, a generated handbook, visual typesetting, human review, or publication completion.

ACCEPT
