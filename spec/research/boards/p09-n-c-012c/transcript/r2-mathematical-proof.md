ACCEPT

# Round-two mathematical/proof review: N-c-012.c GPSS 1980

## Reviewer, independence, and method

- Stable agent identifier: `/root/schmidt_smolka_1991_research`.
- Seat: mathematical/proof.
- Runtime model/version: not exposed to this reviewer.
- I read `spec/research/boards/p09-n-c-012c/charter.md` completely, including the round-two replacement snapshot and mandatory F01--F10 checks, before substantive review.
- I did not inspect `ledger.md`, `transcript/chair.md`, any round-one transcript, any other round-two transcript, or any other reviewer's verdict. I did not contact another reviewer.
- Because I authored the source note, I did not treat it as authority. I freshly judged the mathematical and source claims against the complete source images, then reread the complete frozen source note as an artifact and checked it against those images.
- I made no edit outside this transcript. I ran no test, test harness, automated checker, repository script, TeX command, handbook-PDF inspection, or build. The only executable operations were read-only source/artifact inspection, SHA-256 identity checks, PDF metadata inspection, source-image inspection, and retrieval of the named official author-archive record.

## Frozen round-two identities

I recomputed all eight controlling SHA-256 values before substantive review and again immediately before filing. Both passes matched the charter exactly:

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

No identity mismatch or mid-review drift occurred.

## Complete authority and artifact coverage

I visually read every complete source derivative `page-01.png` through `page-11.png`, corresponding without a wrapper to printed pp. 163--173. Images controlled over OCR, memory, and the source note.

| Printed page | Material freshly checked from the image |
|---:|---|
| 163 | Four-author title and affiliations; rights notices; abstract; execution sequence; informal strict `F`, `G`, `X`, and infix `U` semantics. |
| 164 | Initial grammar; formula symbols versus truth sets; clauses (1)--(5); reversed `F` inequality; one-sided `X`; strict `U`; omega-validity; syntactic `L(U)`; `F/X` eliminations; execution frame; partial correctness. |
| 165 | Total correctness; invariance/eventuality inventories; expressiveness motivation. |
| 166 | Insistence; its equivalent form; busy wait; weakest acceptable semaphore behaviour; minimal scheduler fairness; infinite overtaking; persistence. |
| 167 | Semaphore persistence; guarded-region alternatives and implementation boundary; impulse; unsolicited response. |
| 168 | Unsolicited-response completion; `Pr`; FIFO implication; implementation-specific semaphore axiom; repeated-response refinement; first question. |
| 169 | Remaining questions; Kamp attribution; prior-system boundary; `L_1`; model/order classes; natural forward translation. |
| 170 | Theorems 2.1--2.3; inclusive future quantifiers; outline heading; `At`, `Bet`, special formulas, Lemma 1, decomposition formulas. |
| 171 | Main Lemma; Proposition 2.4; event-expression outline; numbering tension; Theorem 2.5; DX/DUX schemes and rules; Theorems 3.1--3.2. |
| 172 | Maximal theories; exact three canonical facts; `Gamma` closure; quotient relations; transitive-closure lemma; fair ultimately periodic path; formal adjacency omission; truth lemma; decidability referral. |
| 173 | `F^0/G^0/U^0` displays; transformed A/U schemes; `D^0X/D^0UX` claims; references. |

I separately inspected the controlling p. 170 crop. It shows inclusive `\(\forall y\ge x\)` and `\(\exists y\ge x\)`. I separately inspected the p. 172 closure crop. Its second premise is literally `\(Xw\in\Gamma\)`, with conclusion `\(X\neg w\in\Gamma\)`.

I then read the complete frozen reader subsection `handbook/parts/p09/presentations/n-c-012.tex:1206-1817`, the adjacent source boundary beginning at line 1819, the complete shared bridge and theorem at `handbook/parts/p09/logic-in-computer-science.tex:602-691`, the complete 1,140-line source note, ledger subsection `spec/research/p09-source-presentations-lot2-3.md:169-183`, and bibliography entry `handbook/bib/handbook.bib:194-207`.

## Mandatory F01--F10 checks

### F01 — checked clean

Reader lines 1208--1225, source-note lines 12--46, ledger line 171, and bibliography lines 194--207 agree with the PDF and official archive record. The embedded `Author` field names A. Pnueli, S. Shelah, and J. Stavi and omits only Dov Gabbay. Printed p. 163 and the archive record name all four authors. The reader expressly limits the hash to the author-archive object and does not infer byte identity with an ACM-hosted object. DOI, POPL venue, pp. 163--173, eleven-page published-version label, series, publisher, ISBN, rights boundary, and no-wrapper page map are accurate.

### F02 — checked clean

Reader lines 1227--1242 exactly separate initial syntax from interpretation. The p. 164 grammar contains formula symbols `\(q_i\)`, all four printed Boolean connectives, and primitive `\(F,X,U\)`; `\(G\)` is initially derived. `\(Q_i\)` is the interpretation of `\(q_i\)`. No past operator is inserted into that grammar. Reader lines 1651--1657 separately record Section 3's later primitive basis `\(G,X,U\)` and derived `\(F\)`.

### F03 — checked clean

Reader lines 1363--1389 give the exact local and globally prefixed insistence, persistence, and impulse formulas. They state that local strict `\(Gp\)` requires `\(p\)` at every strictly later point and expressly distinguish it from `\(FGp\)`. They separately explain that the outer strict `\(G\)` repeats the local obligation at every strictly later reference point. This matches printed p. 166.

### F04 — checked clean

Reader lines 1391--1400 preserve the busy-wait formula, its weakest-acceptable-semaphore-behaviour classification, the minimal scheduler-fairness calibration, eventual scheduling, and the express infinite-overtaking warning from printed p. 166.

### F05 — checked clean

Reader lines 1330--1347 define before use: `\(\mathit{at}_{\ell}\)` as the about-to-execute program-state proposition; `\(\bar y\)` as current program values; same-arity `\(\bar\xi\)` as logical variables retaining input values; `\(\varphi\)` as precondition; and `\(\psi\)` as postcondition. Their atemporal/metalinguistic standing is explicit. The partial- and total-correctness displays and termination distinction match printed pp. 164--165.

### F06 — checked clean

Reader lines 1445--1458 distinguish the general FIFO condition from the particular semaphore display and identify the latter as a possible basic axiom for a chosen FIFO implementation. The text expressly says temporal logic alone does not prove that implementation FIFO. This matches printed p. 168.

### F07 — checked clean

Reader lines 1596--1601 state Lemma 1 exactly and say that GPSS reports an induction essentially following Kamp Chapter II Theorem 1 while printing no induction. No external proof is silently transferred into GPSS.

### F08 — checked clean

Reader lines 1686--1710 type the canonical objects and state all three p. 172 claims exactly:

\[
\forall\Delta\in S\;(\Delta^+\in S),
\]

\[
\forall x,y,z\in S\,
((x<y\land x<z\land y\ne z)\to(y<z\lor z<y)),
\]

and the typed `\(F\)`-eventuality witness property. The resulting linearity claim is restricted to descendants of the selected `\(\Delta_0\)`, and the supporting derivations remain explicitly unprinted. Reader lines 1711--1756 then preserve the literal `\(\Gamma\)` closure, quotient typing, relation lemma, path recurrence, missing formal adjacency, truth lemma, proof omissions, and unquantified decidability boundary.

### F09 — checked clean

Reader lines 1787--1810 print A0.1--A0.5 and U0.1--U0.2 exactly, give propositional tautologies, modus ponens, and `\(G^0\)`-generalization, and state the source claims with their exact languages: complete `\(D^0X\)` for `\(L(G^0,X)\)` and complete `\(D^0UX\)` for `\(L(G^0,X,U^0)\)`. The reader says p. 173 supplies the transformation claim and schemes but no separate completeness proof, and it qualifies the second claim by the unresolved `\(U^0\)` conflict.

### F10 — checked clean

Reader lines 1758--1807, source-note lines 941--998 and 1072--1091, and ledger line 181 consistently preserve both literal p. 173 displays. The first is

\[
A\mathbin{\mathsf U^0}B
\equiv GA\lor B\lor(A\land(A\mathbin{\mathsf U_s}B)),
\]

with strict `\(G\)`, while U0.2 has right side

\[
B\lor(A\land X(A\mathbin{\mathsf U^0}B)).
\]

The stated omega-model is a valid separating countermodel: at time zero, take `\(A\)` false now and true at every later point, with `\(B\)` false everywhere. Strict `\(GA\)` makes the first displayed definition true, while current `\(A\)` being false makes the U0.2 right side false independently of any recursive value. Replacing strict `\(GA\)` by `\(G^0A=A\land GA\)` would repair the definition to the ordinary present-inclusive weak-until form, but every artifact labels that replacement possible and unprinted. None assigns `\(U^0\)` one coherent source standing, and all three prose records qualify the `\(D^0UX\)` completeness claim.

## Mathematical/proof checks beyond F01--F10

### Strict/inclusive translation

Reader lines 1264--1328 correctly distinguish GPSS strict infix `\(A\,U_s\,B\)` from Kamp prefix `\(U\,B\,A\)` and from the handbook's inclusive strong infix `\(A\,U\,B\)`. GPSS's right operand is the strict-future witness and its left operand labels only the open interval. The handbook-supplied past dual has the exact reversed-order clause and is not attributed to GPSS.

On `\(\mathbb N\)`, `\(X(A\,U\,B)\)` at position `\(i\)` evaluates inclusive until from `\(i+1\)`, so its witness is strictly after `\(i\)` and `\(A\)` holds exactly on the open interval. Thus it is equivalent to strict `\(A\,U_s\,B\)`. Splitting the inclusive case at a current `\(B\)` gives `\(B\lor(A\land(A\,U_s\,B))\)`. The displayed `S/Y` equations are the exact order duals, including the position-zero boundary.

### Shared `tau` and `sigma`

Shared lines 636--681 are correctly typed and truth preserving. In Kamp prefix notation, `\(U\,B\,A\)` has witness operand `\(B\)` and interval operand `\(A\)`, so

\[
\tau(U\,B\,A)=X(\tau(A)\,U\,\tau(B))
\]

has the correct operand order. Conversely, `\(\sigma(XA)=U\,\sigma(A)\,\bot\)` forces an empty open interval and therefore the immediate successor; the `Y/S` clause is dual. The reverse inclusive-until and inclusive-since clauses correctly split current witnesses from strict witnesses. Structural induction over the displayed grammars proves truth preservation at every position. The text correctly refuses to credit inclusive `U,S` alone with next/previous expressiveness.

### Numbered results and proof ownership

Reader lines 1486--1649 preserve all unequal result domains: Theorem 2.1 is arbitrary one-free-variable `L_1` only at point zero of omega-models; Theorem 2.2 is future `L_1` at every point of discrete complete models; Theorem 2.3 is past/future separation over discrete complete models; number 2.4 is a proposition; Theorem 2.5 reaches arbitrary linear orders only with undefined `S',U'`. The p. 170 quantifiers are inclusively bounded. The forward first-order recursion is labelled handbook-supplied. The normal-form, event-expression, external-referral, gap-operator, and 2.1/2.2 numbering boundaries are exact.

### DX/DUX and canonical outline

Reader lines 1651--1756 reproduce A1--A5, U1--U2, and the three rules without changing their implication structure. DX and DUX are theorem systems, not model classes. Theorem 3.1 is soundness with no printed proof; Theorem 3.2 is weak theoremhood completeness with an outline, not strong consequence completeness. The maximal-theory facts, quotient lemma, fair-path existence, and connective cases of the truth lemma remain reported as assertions or omissions. The source's later formal sequence condition still lacks explicit `\(s_n\rho_+s_{n+1}\)` even though earlier prose calls it a path. No automata construction or explicit complexity bound is inferred.

### Shared discrete-word theorem

Shared lines 684--691 correctly state the one-free-position-variable first-order equivalence on pointed `\((\mathbb N,<)\)` words. Kamp's strict `U,S` can define next and previous on this discrete order with bottom on the open interval. The equivalent inclusive presentation retains explicit `X,Y`; it does not claim inclusive `U,S` alone suffice. The Kamp/GPSS citations and surrounding arbitrary-order limitation are consistent with the reader and source note.

## Criterion-by-criterion disposition

- **C1 — ACCEPT.** Identity, provenance, metadata defect, DOI/venue/pages, page map, rights language, archive-record fields, and byte-identity limitation are exact.
- **C2 — ACCEPT.** Initial grammar, model, strict semantics, reversed `F` defect, owned future repair, `X` endpoint omission/totalization, `L(U)` overload, `U_s/S_s` standing, operand order, and strict/inclusive bridge are exact.
- **C3 — ACCEPT.** Correctness formulas, inventories, three response strengths, all worked examples, implementation qualifications, `Pr`, FIFO, and repeated-response formulas are exact.
- **C4 — ACCEPT.** Four questions, Kamp IV.3 boundary, first-order language, order classes, inclusive future quantifiers, and handbook ownership of the forward recursion are exact.
- **C5 — ACCEPT.** Theorems 2.1--2.3, Proposition 2.4, Theorem 2.5, normal forms, Main Lemma, event-expression omissions, numbering tension, and referrals preserve their exact strengths and ownership.
- **C6 — ACCEPT.** DX/DUX languages, all schemes/rules, soundness and completeness strengths, typed canonical claims, finite closure, quotient, path and adjacency boundary, truth lemma, proof omissions, and decidability boundary are exact.
- **C7 — ACCEPT.** Both conflicting `U^0` displays, countermodel, possible-unprinted-repair status, transformed schemes, exact `D^0X/D^0UX` claims/languages, proof omission, and later-calculus boundary are exact.
- **C8 — ACCEPT.** `tau/sigma`, discrete-word theorem, citations, bibliography, source note, ledger, and reader are mathematically and terminologically consistent.
- **C9 — ACCEPT.** Prose is independently worded; definitions precede use; types and quantifiers are explicit; handbook-introduced names satisfy necessity, definition, standing, nonredundancy, and use; undefined source names remain undefined; no unsupported addition or omitted qualification remains.

## Invariant-by-invariant disposition

- **I1:** satisfied; scholarship and prose reasoning only.
- **I2:** satisfied; both hash passes matched the exact round-two snapshot.
- **I3:** satisfied; all eleven pages and both controlling crops were visually read.
- **I4:** satisfied; the reversed `F`, coherent owned repair, `X` totalization, `S_s`, and supplied translations retain their exact ownership.
- **I5:** satisfied; GPSS strict infix, Kamp strict prefix, handbook inclusive strong operators, and the internally conflicting p. 173 `U^0` displays are not conflated.
- **I6:** satisfied; grammar, expressive equivalence, theorem domains, proof status, deductive completeness, and absent `S/S'/U'` clauses remain distinct.
- **I7:** satisfied; every outline, omission, and external proof boundary remains visible.
- **I8:** satisfied; no LTL name, Buechi/automata translation, explicit small-model bound, PSPACE class, or model-checking theorem is retrojected.
- **I9:** satisfied; every handbook-introduced technical name meets the five-part local rule, while undefined source symbols are not adopted as definitions.
- **I10:** satisfied; review remained blind and independent under the charter's exclusions.
- **I11:** satisfied; this verdict follows complete independent checking, not a vote or another seat's conclusion.
- **I12:** preserved; acceptance is narrow to the frozen N-c-012.c topic-level round-two manuscript review and closes none of the expressly excluded downstream scopes.

## Findings and verdict

No blocker, must-fix item, unsupported assertion, mathematical mismatch, proof-status inflation, terminology defect, or unresolved uncertainty remains in the frozen round-two scope.

ACCEPT
