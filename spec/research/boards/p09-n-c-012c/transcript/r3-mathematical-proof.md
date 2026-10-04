ACCEPT

# Round-three mathematical/proof review: N-c-012.c GPSS 1980

## Seat, verdict, and independence

- Stable agent identifier: /root/schmidt_smolka_1991_research.
- Seat: mathematical/proof correctness.
- Runtime model/version: not exposed in the review environment.
- Verdict: ACCEPT. I found no blocker, must-fix defect, unsupported mathematical assertion, source/manuscript mismatch, unresolved ambiguity, or incomplete item within the frozen N-c-012.c scope.
- I read the complete round-three charter before substantive review. I did not inspect the board ledger, chair record, any round-one or round-two transcript (including my own), or any other reviewer's transcript or verdict. I did not contact another reviewer.
- Although I authored the research note, I did not use it as self-validating authority. I first judged the presentation directly against the complete source images and the two controlling crops, and only afterward checked the source note, ledger subsection, bibliography entry, and shared surfaces for consistency.
- I made no manuscript, shared-file, bibliography, source-note, ledger, board-record, or other-agent edit. The only file created is this assigned transcript.
- I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds. The only command-line operations were read-only text display, PDF metadata inspection, and SHA-256 identity hashing. The official author-archive record and the source PDF/page images were used only for scholarship.

## Frozen round-three identities

Every controlling identity matched the charter before substantive review and matched again immediately before this transcript was filed:

| Frozen object | Verified SHA-256 |
|---|---|
| tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf | 2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2 |
| tmp/pdfs/p09-gpss-1980/page-08-quantifier-symbols.png | D74FF885AC1010EA703749F215D1E47DFB3649595F3F8C0A282E073DB714C0F9 |
| tmp/pdfs/p09-gpss-1980/page-10-closure-crop.png | F49C546E4F07A005BA548AB594C6F63B01B37FC62FE3D8DD89A3FAE44EAEA434 |
| handbook/parts/p09/presentations/n-c-012.tex | 3C62CB8706389EFA4572A45EE4321A5A985F2CEDC027C263F4E1B9D2F074F3E5 |
| handbook/parts/p09/logic-in-computer-science.tex | DAE8982D6CAA548BEBCB916B197399B6499A7C6DB966E6972CC4E2C50AC163BA |
| handbook/bib/handbook.bib | BB4096F50E3359E2F07187E1B898F8A8E65CF4A3AC3C288E3FA58099A2A53380 |
| spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md | D7DF8D78587EDFBB0E5EFBE90A92EC39ED154214A9D2CE47DF1E0D8D23F3C49A |
| spec/research/p09-source-presentations-lot2-3.md | 44538248682AA9229F049D27A32086FA8E65973B39DFA8FCDAB41ACD918008E0 |

The eleven ordinary page-image hashes, both high-resolution renders, the intermediate p. 170 crop, and both OCR-derivative hashes also agree with the complete derivative inventory in source-note lines 69--105. Those derivatives were not substituted for the frozen source object.

## Authority record and complete visual page record

I visually reread every printed source page, not merely the proof pages:

- Printed p. 163 / physical p. 1: four-author title and affiliations, abstract, ACM rights language, sequence model, and the informal strict clauses for \(F,G,X,U\).
- Printed p. 164 / physical p. 2: atoms and all four Boolean connectives, \(L(F,X,U)\), linearly ordered model, clauses (1)--(5), the reversed \(F\) inequality, \(\omega\)-models, \(L(U)\), the two eliminations, derived \(G\), execution sequences, and the partial-correctness display.
- Printed p. 165 / physical p. 3: total correctness, complete invariance/eventuality inventories, concurrent-execution discussion, and the claimed need for until.
- Printed p. 166 / physical p. 4: response to insistence, its equivalent formula, busy waiting, weakest acceptable semaphore behaviour, minimal scheduler fairness, infinite overtaking, and the beginning of persistence.
- Printed p. 167 / physical p. 5: semaphore persistence, both guarded-region conditions, implementation qualifications, response to an impulse, and the beginning of unsolicited response.
- Printed p. 168 / physical p. 6: unsolicited response, \(\operatorname{Pr}\), FIFO request/response and semaphore displays, the repeated-response refinement, and all four questions.
- Printed p. 169 / physical p. 7: Kamp and prior-system attributions, proof/referral boundaries, \(L_1\), model classes, and the beginning of the natural translation.
- Printed p. 170 / physical p. 8: literal Theorems 2.1--2.3, the inclusive future-formula quantifier signs, the [SS] statement, \(\operatorname{At}\), \(\operatorname{Bet}_n\), special formulas, Lemma 1, and the decomposition-formula display.
- Printed p. 171 / physical p. 9: Main Lemma, Proposition 2.4, event-expression outline, the 2.1/2.2 numbering tension, arbitrary-complete-order claim, Theorem 2.5, exact \(DX/DUX\) schemes, and Theorems 3.1--3.2.
- Printed p. 172 / physical p. 10: maximal theories, \(\Delta^+\), \(<\), the three canonical facts, the restricted domain above \(\Delta_0\), every \(\Gamma\)-closure condition, finite-modulo-equivalence statement, \(\bar S\), \(\rho_+,\rho_<\), transitive-closure lemma, path/fairness language, truth lemma, and the unquantified decidability referral.
- Printed p. 173 / physical p. 11: the strict/inclusive comparison, exact \(F^0,G^0,U^0\) equations, all transformed schemes, the \(D^0X/D^0UX\) claims, and the complete reference list including [SS].

I separately inspected the controlling p. 170 enlargement. It unambiguously prints \((\forall y\ge x)\) and \((\exists y\ge x)\), so the manuscript's inclusive \([x,\infty)\) definition is correct. I separately inspected the controlling p. 172 enlargement. It unambiguously prints
\[
Fw\in\Gamma\Rightarrow Xw,XFw\in\Gamma,\qquad
Xw\in\Gamma\Rightarrow X\neg w\in\Gamma,
\]
and the four \(U\)-closure conclusions, followed by closure under subformulas and Boolean operations and the statement that only finitely many distinct formulas are needed up to logical equivalence.

The official Shelah archive record identifies Sh:134 as the four-author 1980 POPL paper, pp. 163--173, DOI 10.1145/567446.567462, and labels its linked eleven-page file the published version. The frozen PDF metadata independently reports eleven pages, title and venue subject, but its Author field contains Pnueli, Shelah, and Stavi only. Thus the printed title page correctly controls authorship. These facts agree with reader lines 1208--1225, source-note lines 12--46, ledger line 171, and the bibliography entry at handbook.bib lines 194--207.

## Criterion-by-criterion mathematical and proof disposition

### C1 — identity, provenance, pagination, metadata, and rights: clean

Reader lines 1208--1225 accurately distinguish the inspected author-archive object from an unverified byte-identical ACM object, give the correct eleven-page printed span, preserve the metadata omission, and limit archive hosting to inspection rather than an open-content licence. Source-note lines 12--105 give a correct physical/printed page map and exact derivative inventory. The bibliography gives the four printed authors, exact title, proceedings, pages, year, ISBN, DOI, archive URL, access date, and a cautious archive/rights note. Ledger line 171 agrees. No version, locator, or rights assertion exceeds the checked evidence.

### C2 — syntax, semantics, operand order, and convention bridge: clean

Reader lines 1227--1305 preserve the initial grammar's atoms, negation, conjunction, disjunction, implication, and primitive \(F,X,U\), while keeping \(q_i\) distinct from \(Q_i\), \(G\) derived, and past absent. They retain the p. 164 clause-(4) text \(m_1<m\) and explicitly own the coherent \(m<m_1\) future direction as a handbook repair supported by p. 163, clause (5), and \(FA\equiv\top U A\). The source's one-sided \(X\) clause and the handbook's no-successor false case are likewise separated.

The local definition at lines 1264--1289 is exact:
\[
M,t\models A\mathbin{\mathsf U_s}B
\iff
\exists u>t\bigl(M,u\models B\land
\forall v(t<v<u\to M,v\models A)\bigr).
\]
It correctly records that GPSS infix \(A\,U\,B\) reverses Kamp prefix operands and equals Kamp \(U\,B\,A\). The supplied past dual is expressly handbook-owned because GPSS prints no \(S\) truth clause.

The four \(\omega\)-word bridge equations at reader lines 1307--1328 and shared lines 636--671 are mathematically exact. Evaluating inclusive until one step later gives
\[
A\mathbin{\mathsf U_s}B\equiv
\mathsf X(A\mathbin{\mathsf U}B),
\]
and adjoining the current case gives
\[
A\mathbin{\mathsf U}B\equiv
B\lor(A\land(A\mathbin{\mathsf U_s}B)).
\]
The past equations are their exact order duals. The manuscript correctly retains \(\mathsf X,\mathsf Y\): inclusive \(U,S\) alone do not provide the strict next/previous test. The equations \(FA\equiv\top\mathbin{\mathsf U_s}A\), \(XA\equiv\bot\mathbin{\mathsf U_s}A\), and \(GA\equiv\neg F\neg A\) are correct on arbitrary linear orders under the disclosed \(X\) totalization.

### C3 — all worked source obligations and examples: clean

Reader lines 1330--1468 define every program metavariable before use and then reproduce the source's partial/total correctness distinction, both complete classification lists, and all three response strengths. In particular, lines 1375--1389 correctly explain strict local \(Gp\): it requires \(p\) at every strictly later point, not merely eventual permanence.

The busy-wait, semaphore, and both guarded-region formulas at lines 1391--1423 match printed pp. 166--167, including the weakest/minimal-fairness calibration, infinite-overtaking warning, the warning that infinitely many schedules can coincide with \(x=0\), and the exact implementation qualifications. Lines 1425--1468 preserve unsolicited-response boundary effects, the eliminable and correctly typed \(\operatorname{Pr}\) abbreviation, request/response FIFO, the implementation-specific semaphore axiom, and the fresh-\(p\)-between-successive-\(q\) formula. None is promoted from an assumption or example to a theorem of temporal logic.

### C4 — first-order comparison and translation direction: clean

Reader lines 1470--1484 state the four source questions in order and correctly isolate GPSS's compressed Kamp attribution from literal Kamp IV.3. Lines 1486--1527 give the exact \(L_1\) vocabulary, complete/discrete definitions, all four example orders, and the inclusive future-formula quantifiers confirmed by the p. 170 crop.

The displayed temporal-to-first-order recursion is explicitly handbook-owned. Each clause is truth preserving on every linear order:

- \(F\) uses a strict later witness;
- \(X\) uses a later point with no intermediate point;
- \(A\mathsf U_sB\) uses a strict \(B\)-witness and \(A\) only on the open interval;
- the supplied \(S_s\) clause is the exact order dual;
- Boolean clauses commute homomorphically.

The text does not misattribute that recursion to a source which merely calls the map natural.

### C5 — numbered result strength and proof ownership: clean

Reader lines 1529--1552 keep all four unequal domains separate:

- Theorem 2.1: arbitrary \(L_1\) formula, point \(0\), every \(\omega\)-model;
- Theorem 2.2: future \(L_1\) formula, every point, every discrete complete model;
- Theorem 2.3: \(L(S,U)\) separation over discrete complete models;
- Theorem 2.5: arbitrary \(L_1\) formula over arbitrary linear orders only after adding source symbols \(S',U'\), whose arity, semantics, and translation are absent.

Lines 1554--1656 accurately reconstruct every printed proof-outline object: [SS] ownership, \(\operatorname{At}\), the signed \(\operatorname{Bet}_{n+1}\) recursion, \(\operatorname{Aft}/\operatorname{Bef}\), special formulas, Lemma 1 and its Kamp referral, decomposition formulas, the cofinal-occurrence clause, Main Lemma, Proposition 2.4, and the event-order architecture. They mark the event-expression grammar/semantics and the hard translations absent. They preserve the source's sentence that the \(\operatorname{Bet}(x,\infty)\) application yields Theorem 2.1 under a heading for the proof of Theorem 2.2, rather than repairing the number. They also keep Theorem 2.3's [G2] proof and the arbitrary-order modifications outside the local proof.

The new [SS] paragraph at lines 1554--1561 is especially precise: it reports GPSS's statement that its outline follows [SS], identifies [SS] from p. 173 as the forthcoming Shelah--Stavi manuscript, and expressly declines to import or independently verify that separate manuscript's full proof.

### C6 — \(DX/DUX\), canonical outline, and decidability: clean

Reader lines 1658--1691 reproduce the exact Section 3 basis, A1--A5, U1--U2, R1--R3, theorem-only generalization, languages, soundness clauses, and weak theoremhood-completeness clauses. The U2 recursion has the required one-step shift:
\[
A\mathbin{\mathsf U_s}B
\leftrightarrow
XB\lor(XA\land X(A\mathbin{\mathsf U_s}B)).
\]
Theorem 3.1 remains an unproved soundness statement; Theorem 3.2 remains an outline rather than strong consequence completeness.

The repaired canonical passage at lines 1693--1775 is source-faithful and mathematically disciplined:

1. Maximal consistency is explicitly relative to \(DX\) or \(DUX\), depending on the language.
2. The source's standard but unprinted maximal-extension selection is stated: \(\Delta_0\in S\) and \(A_0\in\Delta_0\).
3. \(\Delta^+\), \(<\), and all three asserted canonical facts have exact types and quantifiers.
4. The source's linear-order conclusion is confined to the explicit domain
   \[
   \{\Delta\in S:\Delta=\Delta_0\text{ or }\Delta_0<\Delta\},
   \]
   with no undefined descendant terminology.
5. \(\Gamma\) contains \(A_0\), is closed under subformulas and Boolean operations, and retains every literal \(F,X,U\) closure obligation.
6. The manuscript does not call \(\Gamma\) a literally finite syntactic set. It states the exact source claim of finitely many formulas up to logical equivalence.
7. It reports \(\bar S=\{\Delta\cap\Gamma:\Delta\in S\}\) as the source-asserted finite quotient and explicitly leaves the finite-equivalence-class-to-finite-\(\bar S\) argument unprinted. It neither chooses representatives nor manufactures a missing proof.
8. The quotient relations and the A5-dependent transitive-closure lemma are exact.
9. \(s_0=\Delta_0\cap\Gamma\) is explicitly stated to contain \(A_0\).
10. The intended \(\rho_+\)-path adjacency condition is retained while the later source paragraph's omission of that condition is disclosed. The recurrence requirement, ultimately periodic path, valuation, truth lemma, and all omitted existence/connective proofs remain separately calibrated.

The decidability corollary is not upgraded: the manuscript reports only a formula-dependent finite-representation bound, with no displayed bound, algorithmic complexity, or named class.

### C7 — p. 173 conflict and transformed systems: clean

Reader lines 1777--1829 retain both literal source artifacts. The countermodel at lines 1793--1804 is correct: at time \(0\), let \(A\) be false now and true at every strict future point, and \(B\) false everywhere. Then strict \(GA\) makes the source's displayed definition
\[
A\mathbin{\mathsf U^0}B
\equiv
GA\lor B\lor(A\land(A\mathbin{\mathsf U_s}B))
\]
true, while the right side of printed U0.2,
\[
B\lor(A\land X(A\mathbin{\mathsf U^0}B)),
\]
is false. Replacing \(GA\) by \(G^0A\) would remove this counterexample and give the usual present-inclusive weak fixed point, but the reader correctly labels that replacement unprinted and does not assign \(\mathsf U^0\) one coherent standing.

All transformed A0/U0 schemes, inference-rule change, exact \(D^0X/D^0UX\) languages, claimed completeness strengths, absent separate proof, [MY] referral, and resulting qualification of \(D^0UX\) are correct. The presentation excludes the Part VIII induction rule and later LTL, Büchi, automata, PSPACE, and model-checking results.

### C8 — shared translations and discrete-word theorem: clean

Shared lines 602--691 define the modern inclusive \(Y,S\) clauses before use and then give typed recursive maps \(\tau,\sigma\). Operand order is correct:
\[
\tau(U\,B\,A)=\mathsf X(\tau(A)\mathbin{\mathsf U}\tau(B)),
\]
while
\[
\sigma(\mathsf XA)=U\,\sigma(A)\,\bot
\]
places \(\sigma(A)\) at the strict witness and \(\bot\) on the open interval. The corresponding \(S/Y\) clauses are exact, and the inclusive \(U/S\) clauses correctly add the current witness case. A structural induction proves truth preservation at every natural-number position.

Theorem thm:p09-ltl-fo has the correct domain: pointed infinite words over \((\mathbb N,<)\), first-order formulas with one free position variable, Kamp's strict two-direction \(U,S\), and equivalently the inclusive two-direction language only when \(X,Y\) are retained. It neither claims GPSS's future-only Theorem 2.2 at arbitrary first-order points nor imports the undefined \(S',U'\). Reader lines 1307--1328 and 1831--1836 agree with this shared bridge. The adjacent Pnueli and Sistla--Clarke subsections remain visibly separate.

### C9 — prose, definitions, additions, and technical names: clean

The presentation is independently worded and definitions precede substantive use. Every handbook-added symbol has local standing and eliminability:

- \(\mathsf U_s,\mathsf S_s\) are local convention warnings with exact clauses, necessity, nonredundancy against the inclusive operators, and later use;
- \(A\mapsto A^*(x)\) is a metalinguistic translation with a constructor-by-constructor definition and a stated purpose;
- shared \(\tau,\sigma\) are typed metalinguistic maps, not object-language connectives.

Source labels with missing definitions are not converted into invented handbook objects: event expressions and \(S',U'\) are explicitly recorded as missing/owed artifacts. No unsupported theorem, proof, algorithm, complexity result, automata result, or later terminology is attributed to GPSS.

## Mandatory fresh-check disposition

- F01 clean: the embedded Author field names Pnueli, Shelah, and Stavi and omits only Gabbay; the hash pins the author-archive object, not ACM byte identity (reader 1208--1225; source note 12--46).
- F02 clean: the full initial grammar and the later Section 3 basis are both exact and separate (reader 1227--1242, 1658--1664).
- F03 clean: local strict \(Gp\) and global repetition are distinguished; no eventual-permanence substitution occurs (reader 1366--1389).
- F04 clean: the busy-wait condition retains weakest acceptable behaviour, minimal fairness, and infinite overtaking (reader 1391--1400).
- F05 clean: \(\mathit{at}_{\ell}\), current values, remembered inputs, precondition, and postcondition all have exact standing before the correctness displays (reader 1330--1356).
- F06 clean: the FIFO semaphore display is explicitly an implementation-specific possible basic axiom, not a temporal theorem (reader 1445--1458).
- F07 clean: Lemma 1 is an unprinted induction essentially following Kamp Chapter II Theorem 1 (reader 1591--1608).
- F08 clean: the three canonical facts are typed exactly, the linearity domain is restricted above \(\Delta_0\), and absent derivations remain absent (reader 1708--1725).
- F09 clean: \(D^0X,D^0UX\), their languages, rules, claims, and absent separate proof are exact (reader 1806--1829).
- F10 clean: both conflicting \(U^0\) displays, the separating \(\omega\)-countermodel, and the merely possible unprinted repair remain explicit (reader 1777--1829; source note 954--1011; ledger 181).
- F11 clean: maximal consistency is system-relative; the standard unprinted \(\Delta_0\) selection is stated; the exact domain \(\Delta=\Delta_0\) or \(\Delta_0<\Delta\) is displayed; \(s_0=\Delta_0\cap\Gamma\) contains \(A_0\) (reader 1693--1725, 1750).
- F12 clean: \(\Gamma\) is finite only modulo logical equivalence, every closure obligation is literal, and the finite quotient plus its missing supporting argument are reported without a representative choice (reader 1726--1748; source-note 873--910; ledger 179).
- F13 clean: [SS] is identified as the forthcoming Shelah--Stavi manuscript, ownership is limited to GPSS's attribution, and no external full proof is imported (reader 1554--1561; source-note 642--648; ledger 177).

## Invariant-by-invariant disposition

- I1 satisfied: scholarship and mathematical reasoning only; prohibited mechanical/build activities were not run.
- I2 satisfied: all eight round-three identities matched twice.
- I3 satisfied: all eleven printed pages and both controlling crops were visually read; images controlled over OCR, memory, and the note.
- I4 satisfied: the p. 164 \(F\) defect, \(X\) endpoint omission, and handbook-supplied clauses/translations retain explicit ownership.
- I5 satisfied: GPSS infix strict \(U\), Kamp prefix strict \(U/S\), modern inclusive strong \(U/S\), and p. 173 \(U^0\) remain four distinct surfaces.
- I6 satisfied: grammar, expressiveness, theorem hypotheses, and deductive completeness remain separate; the missing \(S,S',U'\) clauses are not invented.
- I7 satisfied: every outline, referral, omitted proof, and missing semantic clause is calibrated exactly.
- I8 satisfied: no later LTL, automata, small-model bound, PSPACE, or model-checking claim is retrojected.
- I9 satisfied: handbook technical notation meets necessity, definition, standing, nonredundancy, and use; missing source objects remain owed artifacts.
- I10 satisfied: blind independence and no-contact requirements were maintained.
- I11 satisfied: this verdict is independent and does not rely on majority voting.
- I12 satisfied: ACCEPT closes only this seat's round-three review of the frozen N-c-012.c topic. It does not close N-c-012.d, N-c-012 as a whole, Part IX, any source-wide ledger, the final publication build, rendered-page review, human review, final-book completion, or user acceptance.

## Final scope statement

I reviewed the complete frozen GPSS subsection at n-c-012.tex lines 1206--1837, adjacent source boundaries at lines 1180--1205 and 1838--1860, shared Part IX lines 599--691, the complete 1,153-line source note, ledger lines 169--183, the complete GabbayPnueliShelahStavi1980 bibliography entry, the official archive record, the frozen PDF metadata, all eleven source pages, and both controlling crops. Within that narrow frozen scope, the presentation is source-faithful and mathematically correct at the claimed proof strength.

ACCEPT
