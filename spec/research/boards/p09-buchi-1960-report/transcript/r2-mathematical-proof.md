# Round-two blind mathematical and proof-correctness review

## Scope, blindness, and evidentiary method

I reviewed the corrected six-object snapshot as the mathematical-and-proof-correctness seat. I did not read a chair file, a ledger, any round-one transcript, another round-two transcript or verdict, the Büchi 1962 board, or another reviewer’s work. I did not contact another reviewer.

Before making a substantive judgment, I independently recomputed all six frozen SHA-256 identities. I then read every in-scope frozen line, visually inspected rendered report pages page-01.jpg through page-48.jpg separately at original detail, and directly inspected Bruyère–Hansel–Michaux–Villemaire (1994), printed pp. 202–203. I did not use the repository OCR to control a formula. I did not run a test, test harness, automated checker, repository script, TeX command, build, or handbook-PDF inspection.

The physical report map is confirmed:

- rendered page 1 is the technical-report cover;
- rendered page 2 is the funding leaf;
- rendered pages 3–47 are continuous printed report pages 1–45;
- rendered page 48 is the endpoint/barcode leaf.

## Frozen identities

All recomputed hashes match the round-two charter.

| Artifact | Recomputed SHA-256 | Disposition |
|---|---|---|
| tmp/pdfs/p09-buchi-1960/buchi-1959-umr1083.pdf | 18D1BF4C44E9581932239B500DA8E220876AD7F9B602451BF6B9B22795F840FD | checked-clean |
| handbook/parts/p09/presentations/n-c-014.tex | 843C9FAE64849F6AE57239B05084D7C43D41095512439F00A3AA3F0EB0B208D6 | checked-clean |
| handbook/parts/p09/logic-in-computer-science.tex | 1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8 | checked-clean |
| handbook/bib/handbook.bib | BB5705BD2223275E25B32146540391D511D907FA779F3872C9CAAB1CAB102515 | checked-clean |
| spec/research/p09-buchi-1960-source-note.md | 1C7D1679188EA891D134FE7498822B365DCBB045C607FE2AD39C6610B2D362E2 | checked-clean |
| spec/research/p09-source-presentations-lot2-3.md | EDA1593FCF2F5784718086A7A9747E686E27ABAB992D399362E37F369D732FD3 | checked-clean |

## Nonblocking notation observation

### R2-MP-C01 — The reader transposes the 1994 survey’s ordered arguments for \(\in_2\)

- Severity: consider.
- Frozen locations: n-c-014.tex lines 212–220; p09-buchi-1960-source-note.md lines 265–267.
- Controlling later-source location: Bruyère–Hansel–Michaux–Villemaire (1994), printed p. 202.
- Invariants considered: R2-I9, R2-I13, R2-M09, R2-M15.

The 1994 survey writes \(\in_2(x,y)\) for “\(y\) is a power of two occurring in the binary expansion of \(x\).” The frozen reader instead defines the infix expression \(x\mathrel{\in_2}y\) to mean “\(x\) is a power of two occurring in the binary expansion of \(y\).” Therefore the reader’s relation is the transpose of the survey’s displayed ordered relation.

This is not a mathematical error. The reader supplies an exact local definition, and transposition is definitionally eliminable:
\[
  x\mathrel{\in_2^{\mathrm{reader}}}y
  \quad\Longleftrightarrow\quad
  \in_2^{\mathrm{survey}}(y,x).
\]
All claimed definability and equivalence results are invariant under this exchange of arguments. The standing of the symbol as a binary relation is clear, its necessity is explained by the insufficiency of unary \(P_2\), and it is used in the corrected signature. It therefore satisfies the terminology rule.

For literal historical clarity only, a future revision could say that the reader uses the transpose of the survey’s argument order and could explicitly identify the later survey’s \(P_2\) with the report presentation’s \(\operatorname{Pw}_2\). No theorem, proof, or verdict depends on that stylistic clarification.

## Exact Definition 2 and the printed Theorem 2 defect

Printed report p. 7 (rendered page 9) says
\[
  U[Y^m]\equiv U[H(Y^m,\bot^n)].
\]
The corrected reader gives that exact pointwise identity at n-c-014.tex lines 47–56. The source note gives it at lines 155–163, and the compact record gives it at line 624. None of the corrected occurrences asserts \(U(\bot^m)=\top\) or replaces the free state tuple by a constant state.

The report’s behavior is eventual permanent output truth on special input:
\[
 \beta(E,H,U)=
 \{i:\ i\text{ is special and }
      \exists x\,\forall t\ge x\ U(q(t))\},
\]
where the actual run \(q\) is determined by
\[
 q(0)=E,\qquad q(t+1)=H(q(t),i(t)).
\]
The actual run need not be a finite predicate tuple. A weak second-order transit witness must be finite componentwise. The output predicate is eventually constant under all-false input, but it need not be finite. These standings remain distinct throughout the corrected presentation.

### Hand verification of the counterexample to printed formula (2)

Use one state bit and one input bit, and define
\[
 E=\top,\qquad H(y,x)=y,\qquad U(y)=y.
\]
For both values of \(y\),
\[
 U(y)=y=U(H(y,\bot)),
\]
so the printed Definition 2 holds. For every special input the unique actual run is constantly \(\top\), and its output is constantly true. Hence every special input belongs to the behavior.

In printed formula (2) on pp. 17–18, both \(r\) and \(j\) are weak predicate variables, so they are eventually false. The formula requires \(U(r(t))\) at every sufficiently late point where \(j(t)\) is false. At a still later point, \(r(t)=\bot\), so the formula requires \(U(\bot)=\top\). In this automaton \(U(\bot)=\bot\). Therefore no legal \(r,j\) satisfy printed formula (2), although the input is accepted. The frozen reader’s counterexample at lines 108–119 and the source note’s version at lines 208–216 are exact.

## First-principles proof of the handbook-owned repaired analysis construction

Fix an \(n/m\)-automaton \(E,H\) with output \(U\) satisfying the printed pointwise identity. Equalities between state tuples and input tuples below are componentwise. Quantify an \(m\)-tuple \(r\) of special predicates and one special predicate \(j\). Require
\[
\begin{aligned}
 \text{(A)}\quad&r(0)=E,\\
 \text{(B)}\quad&j(0),\\
 \text{(C)}\quad&\forall t\,
     (j(t+1)\rightarrow j(t)),\\
 \text{(D)}\quad&\forall t\,
     (j(t+1)\rightarrow
       r(t+1)=H(r(t),i(t))),\\
 \text{(E)}\quad&\forall t\,
     (\neg j(t+1)\rightarrow i(t)=\bot^n),\\
 \text{(F)}\quad&\forall t\,
     (j(t)\land\neg j(t+1)\rightarrow U(r(t))).
\end{aligned}
\]
These are exactly the clauses at n-c-014.tex lines 121–141 and source-note lines 218–230.

### Shape of the cutoff predicate

Because \(j\) is special, there is \(N\) such that \(j(t)=\bot\) for all \(t\ge N\). Clause (B) makes it nonempty. Clause (C) makes it downward closed. Hence there is a unique \(h\in\mathbb N\) such that
\[
 j(t)=\top\quad\Longleftrightarrow\quad t\le h.
\]
Equivalently, \(j(h)\land\neg j(h+1)\). No unbounded or nonstandard cutoff is being assumed.

### Forward direction: a finite witness implies behavior

Assume special \(r,j\) satisfy (A)–(F). Let \(q\) be the actual run of the automaton on \(i\).

1. By (A), \(r(0)=q(0)\).
2. If \(t<h\), then \(j(t+1)=\top\). Clause (D) therefore gives
   \[
     r(t+1)=H(r(t),i(t)).
   \]
   Induction on \(t\) yields \(r(t)=q(t)\) for every \(0\le t\le h\).
3. Since \(j(h)\land\neg j(h+1)\), clause (F) gives \(U(r(h))\), hence \(U(q(h))\).
4. For every \(t\ge h\), \(j(t+1)=\bot\). Clause (E) gives \(i(t)=\bot^n\).
5. For \(t\ge h\),
   \[
   U(q(t+1))
   =U(H(q(t),\bot^n))
   =U(q(t))
   \]
   by the actual recursion and printed Definition 2.

It follows inductively that \(U(q(t))=\top\) for every \(t\ge h\). Thus \(i\in\beta(E,H,U)\). The proof never uses \(U(\bot^m)\), and it places no transition condition on the truncated witness after \(h\).

### Reverse direction: behavior yields finite witnesses

Assume \(i\in\beta(E,H,U)\). Because \(i\) is special, choose \(a\) such that \(i(t)=\bot^n\) for every \(t\ge a\). By behavior, choose \(b\) such that \(U(q(t))=\top\) for every \(t\ge b\). Let
\[
 h=\max(a,b).
\]
Define
\[
 j(t)=\top\ \Longleftrightarrow\ t\le h
\]
and, componentwise,
\[
 r(t)=
 \begin{cases}
   q(t),&t\le h,\\
   \bot^m,&t>h.
 \end{cases}
\]
Both \(j\) and every component of \(r\) are special.

- (A) holds because \(r(0)=q(0)=E\).
- (B) holds because \(0\le h\).
- (C) holds because \(j\) is the initial segment through \(h\).
- If \(j(t+1)\), then \(t<h\), so \(r(t)=q(t)\), \(r(t+1)=q(t+1)\), and (D) follows from the actual recursion.
- If \(\neg j(t+1)\), then \(t\ge h\ge a\), so \(i(t)=\bot^n\), proving (E).
- The antecedent of (F) holds only at \(t=h\), where \(r(h)=q(h)\) and \(U(q(h))=\top\) because \(h\ge b\).

Therefore the repaired formula holds. This direction also does not assume \(U(\bot^m)=\top\).

### The \(h=0\) boundary case

If \(h=0\), then \(j(0)=\top\) and \(j(t)=\bot\) for all \(t\ge1\). Clause (D) imposes no transition equation, because \(j(t+1)\) is always false. Clause (E) requires \(i(t)=\bot^n\) from \(t=0\), and clause (F) requires \(U(r(0))=U(E)=\top\). Printed Definition 2 then keeps the actual output true on the all-false tail. Conversely, an accepted input already false at \(0\) with output true at \(0\) produces exactly these witnesses. Thus there is no hidden positive-cutoff hypothesis.

### Tuple and zero-component cases

For \(m>1\), the induction in the forward direction applies simultaneously to the componentwise equality \(r(t)=q(t)\), and truncating to \(\bot^m\) makes each component special. For \(n>1\), clause (E) forces every input component false from \(h\) onward, which is exactly what the transition identity uses. If a zero-length tuple is admitted, its equality and all-false clauses are vacuous and the same proof reduces to the constant-output case. No scalar-only step occurs.

### Advertised existential local successor form

Let the existential witness tuple be
\[
 \mathbf z=(r_1,\ldots,r_m,j).
\]
Put into \(K(\mathbf z(0))\) the conjunction \(r(0)=E\land j(0)\). Put into
\[
 B(i(t),\mathbf z(t),\mathbf z(t+1))
\]
the propositional conjunction of (C)–(F) at time \(t\). Each occurrence is at time \(t\) or \(t+1\), \(H\) and \(U\) are finite propositional formula data, and all equality abbreviations expand componentwise into propositional equivalences. The result is literally
\[
 (\exists\mathbf z)\,
 [K(\mathbf z(0))\land
   \forall t\,B(i(t),\mathbf z(t),\mathbf z(t+1))].
\]
The construction is effective at the same finite formula-manipulation level as the report’s theorem. The corrected clauses therefore prove the stated Theorem 2, while remaining explicitly handbook-owned rather than being attributed to printed formula (2).

## Theorem 3, Corollary 1, and Corollary 2

### Last true point versus printed length

Printed p. 8 defines the length of a special predicate as the least \(x\) such that it is false at every \(t>x\). A downward-closed predicate with last true point \(x\) therefore has length \(x\). Printed p. 19 uses the boundary
\[
 s(x)\land\neg s(x+1)
\]
but says in the surrounding prose that \(x+1\) is its length. Those statements conflict. The reader at n-c-014.tex lines 171–178 and the source note at lines 234–236 explicitly adopt the displayed last-true-point convention. It works at \(x=0\): \(s(0)\) is true and every later value is false.

Theorem 3 first handles formulas without free individual variables by synthesis followed by analysis. Therefore its normal-form result, and the results using that normal form, depend on the repaired Theorem 2 rather than on printed formula (2). This dependency is explicit in source-note line 232 and compact-record line 626 and is not reassigned to the faulty printed formula.

### Corollary 1

For a normal sentence
\[
 (\exists\mathbf j)
 [K(\mathbf j(0))\land
  \forall t\,B(\mathbf j(t),\mathbf j(t+1))],
\]
every legal \(\mathbf j\) is eventually \(\bot\). Hence \(B(\bot,\bot)\) is necessary. If it fails, no witness exists.

Assume \(B(\bot,\bot)\). Let \(k\) be the number of Boolean states of \(\mathbf j\). A witness gives a finite sequence
\[
 Y_0,\ldots,Y_x
\]
such that \(K(Y_0)\), every adjacent pair satisfies \(B\), and \(Y_x=\bot\). Conversely, any such finite sequence extends by the constant \(\bot\) tail because the guard holds.

If \(x\ge k\), the \(x+1\) states contain a repeated state. Deleting the segment from the first occurrence up to, but not including, the second preserves the adjacent \(B\)-constraints: the predecessor of the first occurrence is now followed by the successor of the equal second occurrence. Repeating the deletion yields a shorter witness. The source records the safe inclusive search \(x\le k\), even though loop deletion can sharpen it.

For \(x=0\), the only finite path state is \(Y_0=\bot\); the case succeeds exactly when \(K(\bot)\) and the already checked \(B(\bot,\bot)\) hold. This is the all-false predicate assignment. The corrected presentation at lines 180–190 retains the guard, inclusive bound, loop deletion, zero-length path, and all-false edge.

### Corollary 2

Theorem 3 supplies a finite local recurrence with a finite set of relevant terminal states. Corollary 1 decides which such states have an all-false continuation. Iteration on the finite Boolean state space repeats, giving an effective phase and period. Conversely, fixed finite exceptions and fixed congruence classes are definable in W.2.A. The ultimate-periodicity theorem is therefore sound through the repaired analysis route; it is independent of the false arithmetic converse discussed below.

## Arithmetic counterexamples and the later correction

### Printed bit-occurrence formula

Printed report p. 24 defines
\[
 E(x,y):=
 \operatorname{Pw}_2(x)\land
 \exists u\exists v\,
 [y=u+x+v\land u<v\land(v=0\lor2x\le v)].
\]

The three chartered hand checks are:

1. Genuine occurrence rejected: \(x=1,y=1\). If \(v=0\), then \(u<v\) becomes \(u<0\), impossible in \(\mathbb N\). If \(v\ge2x=2\), then \(u+x+v\ge3\), so it cannot equal \(1\).
2. False occurrence accepted by the printed formula: \(x=2,y=8,u=2,v=4\). Then \(8=2+2+4\), \(2<4\), and \(2x=4\le v\), although the coefficient of \(2\) in the binary expansion \(8=2^3\) is zero.
3. False occurrence accepted after the proposed one-character change \(u<x\): \(x=2,y=8,u=0,v=6\). Then \(8=0+2+6\), \(0<2\), and \(4\le6\), again although the \(2\)-bit is zero.

The high part must have no contribution below \(2x\); merely requiring it to be numerically at least \(2x\) does not do that. The corrected snapshot accurately says that neither the printed formula nor the one-character proposal defines bit occurrence.

### What printed pp. 202–203 of the 1994 survey establish

The fixed later source reports the following:

- Büchi established the weak-monadic/2-recognizable correspondence and then stated equivalence with first-order \((\mathbb N,+,P_2)\).
- McNaughton’s 1963 review observed that the \(P_2\) equivalence was not correctly proved and proposed the binary bit-occurrence relation \(\in_2\).
- The structure \((\mathbb N,+,\in_2)\) is equivalent to \((\mathbb N,+,V_2)\).
- \(P_2(x)\) is definable from \(V_2\) by \(V_2(x)=x\).
- Semenov proved that \(V_2\) is not definable in \((\mathbb N,+,P_2)\).

The survey’s \(V_2\) convention, supplied in the same article and used on pp. 202–203, is
\[
 V_2(0)=1,\qquad
 V_2(y)=\text{the greatest power of two dividing }y
 \quad(y>0).
\]
Thus \((\mathbb N,+,P_2)\) is strictly weaker in first-order definability than \((\mathbb N,+,V_2)\): the unary predicate is definable in the latter, while the latter’s function is not definable in the former.

The equivalence of \(\in_2\) and \(V_2\) can also be checked directly. From bit occurrence, \(V_2(y)\) for \(y>0\) is the least occurring power, with the stipulated \(0\) case. From \(V_2\), the occurrence of a power \(x\) in \(y\) is expressed by a decomposition \(y=u+x+v\) with \(u<x\) and either \(v=0\) or \(x<V_2(v)\). The latter condition, unlike \(2x\le v\), forces the entire high part to be divisible by a power strictly above \(x\).

The reader and source note correctly treat the 1994 article as later correction evidence, not as wording from the 1959 report or the unreconciled 1960 article.

## Exact surviving force of Corollary 5 and Theorem 9

### Corollary 5

The sound direction of printed Theorem 4 translates a first-order
\((\mathbb N,=,+,P_2)\) formula into W.2.A.:

- addition is represented by the finite binary carry predicate;
- \(P_2(x)\) is represented by a singleton finite predicate;
- Boolean connectives and first-order quantifiers translate compositionally.

Given a first-order sentence, this effective translation produces a W.2.A. sentence. Corollary 1, using the repaired Theorem 2 through Theorem 3, decides the translated sentence. Therefore the decidability sentence of Corollary 5 survives.

For the definability/behavior sentence of Corollary 5, only one direction survives in the unary \(P_2\) signature:
\[
 \text{first-order \(P_2\)-definable}
 \quad\Longrightarrow\quad
 \text{W.2.A.-definable}
 \quad\Longrightarrow\quad
 \text{finite-automaton behavior}.
\]
The second implication is Theorem 1 synthesis. The converse behavior-to-\(P_2\)-definability fails because it would recover the false reverse direction of Theorem 4.

The frozen reader says only that Corollary 5’s decidability conclusion survives; the source note makes the same restriction. Neither artifact retains the false biconditional.

### Theorem 9

Printed Theorem 9 says that the \(P_2\)-definable relations are exactly the 2-regular relations. Its forward implication survives:
\[
 P_2\text{-definable}\Longrightarrow
 W.2.A.\text{-definable}\Longrightarrow
 2\text{-regular}.
\]
Its reverse implication is false. The bit-occurrence relation is synchronously 2-regular, but if it were first-order definable in \((\mathbb N,+,P_2)\), then the least occurring power would define \(V_2\), contradicting Semenov’s nondefinability theorem recorded on printed p. 202.

The exact automatic/first-order equivalence is instead obtained with \(\in_2\) or \(V_2\), and analogously with \(V_k\) in base \(k\). The source note at lines 305–316 correctly describes the report’s \(P_k\) statement as a claim whose reverse direction inherits the false unary-powers equivalence. It does not use that false reverse direction to certify the finite-word theorem.

The report’s p. 41 converter sentence says that the preceding result “seems to mean” there is no finite automaton translating all binary expansions to ternary expansions. The source note at line 313 preserves that tentative standing and explicitly says that no separate reduction is printed. The corrected reader does not strengthen it.

## Theorems 6–8 and the finite-word result

### Encoding and Theorem 6

For a nonempty word \(Y_0\cdots Y_h\), the report places its data at positions \(0,\ldots,h\), the terminal marker \(\top^n\) at \(h+1\), and \(\bot^n\) afterward. The empty word has the marker at \(0\) and the all-false tail afterward. The last nonfalse position is the marker, so the word is uniquely recovered even when a data letter itself is \(\top^n\).

String behavior reads arbitrary output \(U\) at \(r(h+1)\), after all data letters and before the terminal marker is consumed. For the empty word it reads \(U(E)\).

Theorem 6 is sound independently of Theorem 2:

- From arbitrary string output \(U\), add a state bit that is set to \(U\) when the marker is read and persists on the all-false tail. The new state bit is a special output in the pointwise Definition 2 sense. Behavior reads it one transition after the marker and therefore agrees with the original endpoint test.
- From special behavior output \(W\), define
  \[
    U(Y)=W(H(Y,\top^n)).
  \]
  At the finite endpoint this equals the behavior output after the encoded marker. For the empty word it is \(W(H(E,\top^n))\), exactly the first-state value used by the behavior of the marker-only predicate.

No arithmetic equivalence is used.

### Theorem 7

The analysis direction has the route
\[
 \text{arbitrary-output string behavior}
 \xrightarrow{\text{Theorem 6}}
 \text{special-output behavior}
 \xrightarrow{\text{repaired Theorem 2}}
 \text{W.2.A. string formula}.
\]
It therefore depends precisely on the repaired finite-witness construction.

The synthesis direction has the route
\[
 \text{W.2.A. string formula}
 \xrightarrow{\text{Theorem 1}}
 \text{special-output behavior}
 \xrightarrow{\text{Theorem 6}}
 \text{arbitrary-output string behavior}.
\]
It does not require Theorem 2.

The reader explicitly identifies the analysis dependency at n-c-014.tex lines 168–169.

### Theorem 8

The four conditions remain equivalent:

1. arbitrary-output string behavior;
2. special-output behavior;
3. W.2.A. definability on the word encodings;
4. regularity.

Theorem 6 proves (1)\(\leftrightarrow\)(2). Theorem 1 proves the formula-to-behavior implication. The repaired Theorem 2 proves behavior-to-formula. The classical finite-automaton characterization supplies (1)\(\leftrightarrow\)(4). The shared theorem at logic-in-computer-science.tex lines 811–816 states the modern MSO/regular-language result at exactly this finite-word level.

Therefore the full Theorems 7–8 survive. Their logic/automata equivalence is independent of the false \(P_2\) arithmetic converse. The many-input Theorem 8′ likewise survives by grouping the input tuples and applying the same repaired analysis proof componentwise.

## Cross-artifact and publication reconciliation

The six frozen artifacts agree on the following:

- Definition 2 is pointwise and does not imply \(U(\bot)=\top\).
- Printed Theorem 2 formula (2) is defective; the displayed boundary construction is handbook-owned.
- Theorem 3’s displayed last-point encoding is used, while the printed \(x+1\)-length prose is identified as inconsistent.
- Corollary 1 retains \(B(\bot,\bot)\) and the inclusive \(x\le k\) bound.
- Printed Theorems 4 and 9 are false for unary \(P_2\).
- Corollary 5’s decidability conclusion survives through the sound translation direction.
- The exact later arithmetic signature is \(\in_2\), equivalently \(V_2\).
- Theorems 6–8 remain the sound finite-word correspondence, with repaired analysis used only where required.
- The binary-to-ternary converter sentence is tentative.

The bibliography separately identifies the September 1959 UMR1083 report, the 1960 journal article, and the 1994 correction source. The reader lines 8–16 and 252–256, source-note lines 21–43 and 350–356, compact-record lines 622 and 630, and open-record line 898 all leave literal 1960 journal reconciliation open. The 1994 source is later correction evidence, not proof of wording in either Büchi version.

The public report and survey access routes are not described as redistribution licences. The source note expressly preserves the report rights caution. The open record does not mark the presentation closed before this fresh round.

## Terminology audit

- “Special predicate” and “special output” are source terms, locally defined with their distinct standings and used by the correspondence theorems.
- “Finite witness” is a metalinguistic description of the explicitly quantified special predicates \(r,j\), not a new primitive. Its exact clauses and difference from the actual run are supplied where it is used.
- \(\in_2\) is explicitly defined as a binary bit-occurrence relation, is needed because unary \(P_2\) cannot recover bit occurrence, is distinguished from \(P_2\), and is used in the corrected signature.
- \(V_2\) is explicitly defined as a unary function, including its value at zero; its definitional equivalence with \(\in_2\), strict difference from \(P_2\), and later use are all supplied.
- “String behavior” is the source’s endpoint-output notion and is explicitly distinguished from eventual-truth behavior.

No proposed repair introduces an unnamed motive or hypothetical formal object. Every corrected term has a definition, standing, reason for introduction, distinction from existing terms, and subsequent use.

## R2-M01–R2-M16 disposition

“Finding-linked” below means the item was fully checked and carries the nonblocking notation observation R2-MP-C01; it does not mean the item was skipped.

| Item | Disposition | Basis |
|---|---|---|
| R2-M01 | checked-clean | All six frozen SHA-256 identities were recomputed before substantive judgment and match. |
| R2-M02 | checked-clean | All 48 report images were inspected separately at original detail; the cover/funding/pp. 1–45/endpoint map is continuous. |
| R2-M03 | checked-clean | Printed Definition 2 and every frozen occurrence use \(U[Y]\equiv U[H(Y,\bot)]\). |
| R2-M04 | checked-clean | The one-bit identity-transition counterexample to printed formula (2) was independently evaluated and is decisive. |
| R2-M05 | checked-clean | Clauses (A)–(F), both semantic directions, cutoff existence, \(h=0\), tuple states/inputs, and existential local form were derived from first principles. |
| R2-M06 | checked-clean | Printed p. 8 length, printed p. 19 \(x+1\) prose, displayed boundary, and reader’s last-true-point convention were compared exactly. |
| R2-M07 | checked-clean | Tail guard, inclusive \(x\le k\), loop deletion, zero-length path, and all-false assignment are all present and sound. |
| R2-M08 | checked-clean | \((1,1)\), \((2,8,2,4)\), and the proposed-repair witness \((2,8,0,6)\) were verified by hand. |
| R2-M09 | finding-linked: R2-MP-C01 | Printed pp. 202–203 verify the McNaughton history, \(\in_2/V_2\) equivalence, \(P_2\) definability from \(V_2\), and Semenov strict nondefinability; the reader’s transposed argument convention is harmless and explicitly defined. |
| R2-M10 | checked-clean | The false Theorem 4 reverse is traced into the false reverse of Theorem 9; the source note retains only sound or explicitly qualified base statements. |
| R2-M11 | checked-clean | Corollary 5 decidability follows from the effective first-order-to-W.2.A. translation plus repaired-route W.2.A. decision; its definability biconditional does not survive. |
| R2-M12 | checked-clean | Marker position, empty word, both Theorem 6 constructions, both Theorem 7 directions, and all four Theorem 8 conditions were rederived; repaired analysis is needed only for behavior-to-formula. |
| R2-M13 | checked-clean | Printed p. 41 says “seems to mean”; the source note preserves the tentative qualification and notes the absent reduction. |
| R2-M14 | checked-clean | Reader, source note, compact record, shared theorem, bibliography, and open record agree without claiming journal reconciliation or pre-verdict closure. |
| R2-M15 | finding-linked: R2-MP-C01 | All corrected terms satisfy the local terminology rule; the survey/reader argument-order difference is definitionally eliminable but recorded for precision. |
| R2-M16 | checked-clean | Report, journal, and later source identities, page locators, public-access/rights boundary, topic scope, and no-test/no-build boundary are exact. |

## Determination

The repaired Theorem 2 formula is sound in both directions, including the zero cutoff and arbitrary finite tuples, and it has the promised existential local successor form. The arithmetic correction is also accurately delimited: all three counterexamples work, the 1994 source supports the strict \(P_2\) versus \(V_2\) distinction, Corollary 5 retains decidability but not its full definability equivalence, and Theorem 9 retains only the \(P_2\)-definable-to-regular direction. The finite-word Theorems 6–8 remain sound and are not contaminated by the false arithmetic equivalence.

R2-MP-C01 is a nonblocking notation observation because the frozen reader defines its transposed relation exactly and transposition preserves every claimed result. No blocker or must-fix remains.

VERDICT: ACCEPT
