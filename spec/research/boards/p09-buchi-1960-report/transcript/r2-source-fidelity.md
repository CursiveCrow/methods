# R2 source-fidelity and evidence report: corrected Büchi 1959 report presentation

Seat: source fidelity and evidence.

Owned file: `spec/research/boards/p09-buchi-1960-report/transcript/r2-source-fidelity.md`.

I followed the round-two blind constraints. I read `round2-charter.md`, recomputed the six frozen hashes before substantive judgment, read only the frozen artifact ranges named there, visually inspected all 48 rendered 1959 report pages, and directly read Bruyère--Hansel--Michaux--Villemaire (1994) at printed pp. 202--203. I did not read `chair.md`, `ledger.md`, any round-one transcript, the Büchi 1962 board, or another round-two transcript/verdict. I did not contact another reviewer. I did not edit any frozen artifact. I did not run a test, automated checker, repository script, TeX command, build, or handbook-PDF inspection.

## Frozen identity check

All six round-two frozen hashes matched the charter before I judged content.

| Frozen artifact | Charter SHA-256 | Recomputed result |
|---|---:|---|
| `tmp/pdfs/p09-buchi-1960/buchi-1959-umr1083.pdf` | `18D1BF4C44E9581932239B500DA8E220876AD7F9B602451BF6B9B22795F840FD` | matched |
| `handbook/parts/p09/presentations/n-c-014.tex` | `843C9FAE64849F6AE57239B05084D7C43D41095512439F00A3AA3F0EB0B208D6` | matched |
| `handbook/parts/p09/logic-in-computer-science.tex` | `1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8` | matched |
| `handbook/bib/handbook.bib` | `BB5705BD2223275E25B32146540391D511D907FA779F3872C9CAAB1CAB102515` | matched |
| `spec/research/p09-buchi-1960-source-note.md` | `1C7D1679188EA891D134FE7498822B365DCBB045C607FE2AD39C6610B2D362E2` | matched |
| `spec/research/p09-source-presentations-lot2-3.md` | `EDA1593FCF2F5784718086A7A9747E686E27ABAB992D399362E37F369D732FD3` | matched |

## Source-page inspection record

I visually inspected the report scan at original detail through `tmp/pdfs/p09-buchi-1960/rendered/page-01.jpg` through `page-48.jpg`. The physical map is confirmed: report cover, funding leaf, continuous printed pp. 1--45, and endpoint barcode leaf.

| Rendered page | Printed page | Source evidence checked |
|---:|---:|---|
| page-01 | cover | Title, author, University of Michigan/Logic of Computers Group technical-report identity, September 1959 date. |
| page-02 | funding leaf | UMR1083 handwritten identifier and funding/contract page. |
| page-03 | 1 | Introduction and Kleene synthesis/analysis framing. |
| page-04 | 2 | Variable sorts and formula/matrix standing. |
| page-05 | 3 | Tuple notation and explicit absence of a deductive structure for the syntactic frame. |
| page-06 | 4 | Truth values, predicates, special predicates, \(n\)-predicates, and \(W.2.A.\) interpretation. |
| page-07 | 5 | Lemma 1 statement and proof begins. |
| page-08 | 6 | Lemma 1 concludes; Definition 1 begins. |
| page-09 | 7 | Definition 1 recursion/output and Definition 2 exact special-output identity \(U[Y]\equiv U[H[Y,\Lambda]]\); Definition 3 begins. |
| page-10 | 8 | Behavior definition, length definition, property (*), Lemma 2, Definition 4, Lemma 3. |
| page-11 | 9 | Expanded-form construction. |
| page-12 | 10 | Expanded-form specialness and Lemma 4. |
| page-13 | 11 | Lemma 4 construction. |
| page-14 | 12 | Lemma 5 and its state-variable stability condition. |
| page-15 | 13 | Lemma 6; source again uses pointwise stability \(U[Y]\equiv U[H[Y,\Lambda,\Lambda]]\). |
| page-16 | 14 | Lemma 6 concludes; Lemma 7 begins. |
| page-17 | 15 | Lemma 7 construction. |
| page-18 | 16 | Theorem 1 synthesis proof. |
| page-19 | 17 | Theorem 2 statement and printed formulae (1)--(2), including the defective finite \(r,j\) formula. |
| page-20 | 18 | Theorem 2 proof conclusion; Definition 5 begins. |
| page-21 | 19 | Theorem 3 and the free-individual last-true-point/length prose. |
| page-22 | 20 | Corollary 1 decision proof with \(B(\Lambda,\Lambda)\) tail guard, inclusive \(x\le k\) bound, loop deletion; Corollary 2 begins. |
| page-23 | 21 | Corollary 2 ultimate-periodicity proof and effective phase/period extraction. |
| page-24 | 22 | Corollary 2 conclusion and Corollary 3. |
| page-25 | 23 | Binary expansion map and Theorem 4 statement. |
| page-26 | 24 | Theorem 4 proof, including the displayed bit-occurrence formula \(E(x,y)\). |
| page-27 | 25 | Corollary 5 and Theorem 5. |
| page-28 | 26 | Section 6 comparison with other automata notions. |
| page-29 | 27 | Many-input automaton Definition 1′. |
| page-30 | 28 | Definition 3′ and Theorems 1′--2′. |
| page-31 | 29 | Many-input proof sketch and special-predicate/string distinction. |
| page-32 | 30 | Section 7 finite-string encoding with terminal marker. |
| page-33 | 31 | Empty-word convention, Definition 6, Theorem 6 begins. |
| page-34 | 32 | Theorem 6 both directions; start of Theorem 7 setup. |
| page-35 | 33 | Theorem 7 and Theorem 8 four equivalent conditions. |
| page-36 | 34 | Definition 7, Theorem 8′, equi-response relation. |
| page-37 | 35 | Binary-expansion regularity and modified binary expansion. |
| page-38 | 36 | Theorem 9 and base-\(k\) setup. |
| page-39 | 37 | Base-\(k\) remarks and definability consequences. |
| page-40 | 38 | Ultimately periodic/base-regularity and power-predicate consequences. |
| page-41 | 39 | Base-comparison argument. |
| page-42 | 40 | Base-equivalence consequences and simple representatives. |
| page-43 | 41 | Tentative binary-to-ternary converter sentence and Section 8 feedback begins. |
| page-44 | 42 | Union, concatenation, star, finite-set quantification as feedback/Kleene star; Section 9 begins. |
| page-45 | 43 | Problem 1 and Theorem 10. |
| page-46 | 44 | Bibliography entries 1--12. |
| page-47 | 45 | Bibliography entries 13--15; numbered report endpoint. |
| page-48 | endpoint leaf | University of Michigan barcode/end leaf after bibliography. |

I also directly read Bruyère--Hansel--Michaux--Villemaire (1994), printed pp. 202--203, through the public PDF specified in the charter. Printed p. 202 reports the Büchi \(p=2\) weak-monadic/recognizability history, the faulty \(P_2\) equivalence claim, McNaughton's replacement by a binary bit-occurrence relation, Boffa's \(V_p\) replacement, the \(\in_2/V_2\) equivalence, and Semenov's nondefinability of \(V_2\) in \((\mathbb N,+,P_2)\). Printed p. 203 continues with the decidability/non-equivalence diagram for \((\mathbb N,+,P_p)\), \((\mathbb N,+,V_p)\), \((\mathbb N,+,p^x)\), and \((\mathbb N,+,V_p,p^x)\). This supports the later-correction attribution in the frozen reader and source records.

## Frozen manuscript and record material read

- `handbook/parts/p09/presentations/n-c-014.tex` lines 1--257.
- `handbook/parts/p09/logic-in-computer-science.tex` lines 811--816.
- `handbook/bib/handbook.bib` lines 6099--6134.
- `spec/research/p09-buchi-1960-source-note.md` lines 1--358.
- `spec/research/p09-source-presentations-lot2-3.md` lines 620--630 and line 898.

## Findings

No blocker, must-fix, should-fix, or consider finding within the source-fidelity seat's assigned mandate.

## Cross-record source-fidelity determinations

### Definition 2 and behavior

The corrected reader now gives the source's pointwise special-output identity, not the rejected constant-state identity:

- Source: printed report p. 7 (`page-09.jpg`): \(U[Y]\equiv U[H[Y,\Lambda]]\), followed by the eventual-constancy explanation.
- Reader: `n-c-014.tex:47-58` states \(U[Y^m]\equiv U[H(Y^m,\bot^n)]\), explicitly as an identity in state variables.
- Source note: `p09-buchi-1960-source-note.md:157-164` states the same pointwise identity and identifies the earlier left-side transcription error.
- Compact record: `p09-source-presentations-lot2-3.md:624` uses the same pointwise identity.

This satisfies R2-I1 and R2-I2. The reader also keeps \(E,H,U\), input \(i\), transit \(r\), output predicate \(u\), and behavior \(\beta(E,H,U)\) in separate standings at `n-c-014.tex:31-71`.

### Printed Theorem 2 defect and handbook-owned repair attribution

The report's Theorem 2 statement is source-located correctly, and the frozen reader does not pass off the repair as Büchi's printed proof:

- Source: printed pp. 17--18 (`page-19.jpg`, `page-20.jpg`) state Theorem 2 and printed formula (2).
- Reader: `n-c-014.tex:95-142` labels printed formula (2) defective, gives the counterexample, and introduces the corrected finite-witness clauses as a handbook-owned emendation.
- Source note: `p09-buchi-1960-source-note.md:196-232` gives the same defect/repair division and says Theorem 3, Corollaries 1--2, and Theorems 7--8 use the repaired analysis direction rather than printed formula (2).
- Compact record: `p09-source-presentations-lot2-3.md:626` says Theorem 2's statement is recoverable but its printed finite-transit-witness formula is false, and that the reader supplies a handbook-owned boundary formula.

I independently checked the printed-formula counterexample at source-fidelity level. With one state bit, \(E=\top\), \(H(y,x)=y\), and \(U(y)=y\), the printed special-output identity holds because \(U(y)=U(H(y,\bot))=y\). The actual run remains \(\top\), so every special input is accepted. But in printed formula (2) both \(r\) and \(j\) are weak second-order witnesses and therefore finite; eventually \(r(t)=\bot\) and the tail clause still demands \(U(r(t))\), which is false. The counterexample stated at `n-c-014.tex:108-119` and `p09-buchi-1960-source-note.md:208-216` is therefore correct and is attributed to the handbook reconstruction, not to the printed report.

### Theorem 3, Corollary 1, and dependent use of repaired analysis

The finite-decision and endpoint corrections are source-faithful:

- Source: printed p. 19 (`page-21.jpg`) uses a displayed boundary formula \(s(x)\land\neg s(x+1)\) while nearby prose says \(x+1\) is the length.
- Reader: `n-c-014.tex:172-178` reports the inconsistency and adopts the displayed last-true-point convention, including \(x=0\).
- Source note: `p09-buchi-1960-source-note.md:236-237` makes the same distinction.
- Source: printed p. 20 (`page-22.jpg`) first assumes \(B(\bot,\bot)\), then gives the finite search with \(x\le k\) and loop deletion.
- Reader: `n-c-014.tex:180-190` includes the \(B(\bot,\bot)\) guard, inclusive \(x\le k\) bound, all-false endpoint, and loop deletion.
- Source note: `p09-buchi-1960-source-note.md:238-246` agrees.

The zero-length edge case is covered by the reader's path \(Y_0,\ldots,Y_x\): when \(x=0\), the required endpoint is already \(Y_0=\bot\), so the all-false assignment is included exactly when the \(K\)-state and tail guard allow it.

### Theorem 4, Theorem 9, bit-formula counterexamples, and 1994 correction

The corrected snapshot now separates four claims that must not be blended: the report's source statement, the report's false reverse arithmetic translation, later correction by \(\in_2/V_2\), and the surviving decidability direction.

Source pages and frozen lines checked:

- Source: printed p. 23 (`page-25.jpg`) gives \(f(i)=\sum i(x)2^x\), defines \(P_{w2}\), and states Theorem 4.
- Source: printed p. 24 (`page-26.jpg`) displays the bit-occurrence formula
  \[
  E(x,y):=P_{w2}(x)\land\exists u\exists v\,
  (y=u+x+v\land u<v\land(v=0\lor 2x\le v)).
  \]
- Source: printed p. 25 (`page-27.jpg`) states Corollary 5.
- Source: printed pp. 35--36 (`page-37.jpg`, `page-38.jpg`) use Theorem 4 to formulate the "2-regular" and \(k\)-regular claims, including Theorem 9.
- Reader: `n-c-014.tex:192-223` identifies the reverse translation as false, gives two counterexamples plus the failed one-character repair, supplies \(\in_2/V_2\) as later correction, and keeps Corollary 5 only via the sound first-order-to-\(W.2.A.\) direction.
- Source note: `p09-buchi-1960-source-note.md:248-267` and `:312-313` make the same distinctions, including Theorem 9's inherited false reverse direction and the tentative binary-to-ternary consequence.
- Compact record: `p09-source-presentations-lot2-3.md:626` agrees.
- Bibliography: `handbook.bib:6122-6133` correctly adds Bruyère--Hansel--Michaux--Villemaire 1994 as the later-correction identity.

The counterexamples in the reader/source note are correct:

1. \((x,y)=(1,1)\) is a genuine bit occurrence, but \(y=u+x+v\) forces \(u=v=0\), so \(u<v\) fails. The printed formula wrongly rejects it.
2. \((x,y,u,v)=(2,8,2,4)\) satisfies the printed formula: \(8=2+2+4\), \(2<4\), and \(2x=4\le4\). But the \(2\)-bit of \(8\) is zero, so the formula wrongly accepts it.
3. Replacing only \(u<v\) by \(u<x\) still fails, because \((x,y,u,v)=(2,8,0,6)\) satisfies \(8=0+2+6\), \(0<2\), and \(4\le6\), while again the \(2\)-bit of \(8\) is zero.

The 1994 correction source supports the reader's correction history. Printed p. 202 says Büchi stated equivalence with \((\mathbb N,+,P_2)\), McNaughton observed the equivalence was not correctly proved and suggested a binary bit-occurrence relation, and later work used \(V_p\). It also says \((\mathbb N,+,\in_2)\) and \((\mathbb N,+,V_2)\) are equivalent, \(P_2\) is definable from \(V_2\), and Semenov proved \(V_2\) is not definable in \((\mathbb N,+,P_2)\). Printed p. 203 continues the strict non-equivalence/decidability discussion. The reader's infix convention \(x\in_2 y\) at `n-c-014.tex:212-214` reverses the argument order of the displayed relational notation used in the 1994 prose, but it is explicitly defined at first use as "the bit \(x\) occurs in number \(y\)" and so is a harmless notational convention, not a source-fidelity error.

Corollary 5's decidability conclusion is retained at the correct strength: the source's first-order \([=,+,P_2]\)-to-\(W.2.A.\) translation is sound and suffices for decidability; the false converse and Theorem 9 exact-characterization claim are not used by the corrected reader.

### Finite-word bridge and repaired-analysis dependency

The finite-word material is source-faithful and the point at which repaired analysis is needed is explicit:

- Source: printed pp. 30--34 (`page-32.jpg`--`page-36.jpg`) define the terminal-marker encoding, empty word, string behavior, Theorems 6--8, and Theorem 8′.
- Reader: `n-c-014.tex:144-169` gives the data positions, terminal \(\top^n\) at \(h+1\), all-false tail, empty-word marker at 0, arbitrary-output string behavior, Theorem 6, and Theorems 7--8. Line 168--169 states that Theorem 7's analysis half uses the corrected finite-witness construction, not printed formula (2).
- Source note: `p09-buchi-1960-source-note.md:269-303` agrees.
- Compact record: `p09-source-presentations-lot2-3.md:628` agrees.

### Binary-to-ternary and feedback/status boundaries

The report's binary-to-ternary sentence remains tentative:

- Source: printed p. 41 (`page-43.jpg`) says the \(P_{w2}\) non-3-regular consequence "seems to mean" no finite automaton translates binary expansions into corresponding ternary expansions.
- Source note: `p09-buchi-1960-source-note.md:313` preserves the tentative wording and says the separate reduction is not printed.
- The reader does not make a stronger binary-to-ternary converter claim.

Section 8 feedback is also kept at its printed strength:

- Source: printed pp. 41--42 (`page-43.jpg`, `page-44.jpg`) identifies state recursion as feedback and finite-set quantification as the operation corresponding to feedback/Kleene star after union and concatenation.
- Reader: `n-c-014.tex:223-229` uses this only as a conceptual comparison after separating the sound finite-word theorem, repaired Theorem 2 route, and false arithmetic equivalence.
- Source note: `p09-buchi-1960-source-note.md:313-316` agrees.

### Bibliography, shared theorem, open status, rights, and scope

- `logic-in-computer-science.tex:811-816` cites the finite-word correspondence as the public Büchi--Elgot--Trakhtenbrot theorem and includes the 1959 report citation alongside the registered 1960 article, Elgot, and Trakhtenbrot. This is source/provenance-honest and does not claim journal page reconciliation.
- `handbook.bib:6099-6134` distinguishes the 1959 report, the registered 1960 article, and the 1994 later-correction article.
- `p09-source-presentations-lot2-3.md:630` says the corrected snapshot still requires fresh blind acceptance before closure and that literal 1960 journal reconciliation remains independently open.
- `p09-source-presentations-lot2-3.md:898` preserves the separate open obligation to acquire and reconcile the 1960 journal body or 1990 reprint.
- `p09-buchi-1960-source-note.md:19` gives the rights caution; `:350-356` preserves the remaining journal-reconciliation obligation; `:358` states no manuscript build, automated test, or checker was used in the source/reconstruction pass.

I found no completion inflation: the snapshot claims only corrected 1959-report precursor control with printed defects and handbook-owned repairs explicit, not journal-version fidelity, not Elgot/Trakhtenbrot literal completion, not a rendered handbook artifact, and not user or human acceptance.

## AGENTS terminology check

The corrected terms and notations satisfy the local AGENTS rule in the frozen text:

- "Special predicate" and \(n\)-predicate are source terms with exact definitions and standings at `n-c-014.tex:18-29` and `p09-buchi-1960-source-note.md:92-106`.
- "Special output" has necessity, exact eliminable definition, standing, nonredundancy, and use at `n-c-014.tex:47-58`, `p09-buchi-1960-source-note.md:155-164`, and `p09-source-presentations-lot2-3.md:624`.
- "Behavior" and "string behavior" are separately defined and later used at `n-c-014.tex:59-71` and `:144-169`; the text does not conflate eventual permanent truth with terminal-marker finite-word acceptance.
- "Handbook-owned emendation" / "repaired finite-witness construction" is necessary to distinguish the true theorem statement from printed formula (2); it is introduced where the corrected local clauses are displayed at `n-c-014.tex:121-142` and source note `:218-232`.
- \(\in_2\) and \(V_2\) are introduced with exact definitions and standing at `n-c-014.tex:212-220` and source note `:265-267`; they are explicitly later correction history, not 1959 report wording.
- No redundant new technical name, standing ambiguity, or unused distinction requiring a finding was found.

## Mandatory coverage ledger

| Item | Status | Source-fidelity determination |
|---|---|---|
| R2-M01 | checked-clean | All six frozen hashes were recomputed before substantive judgment and matched the round-two charter. |
| R2-M02 | checked-clean | All 48 report pages were visually inspected; cover/funding/printed pp. 1--45/endpoint map confirmed. |
| R2-M03 | checked-clean | Definition 2 is exact in the reader, source note, and compact record; all cross-artifact occurrences use pointwise \(U[Y^m]\equiv U[H(Y^m,\bot^n)]\). |
| R2-M04 | checked-clean | The counterexample to printed Theorem 2 formula (2) is independently valid and is correctly attributed as exposing a printed proof defect. |
| R2-M05 | not-checked with reason | Not assigned to this source-fidelity seat for full proof-correctness derivation; I checked source/repair attribution and local source consistency but do not claim the mathematical seat's full proof mandate. |
| R2-M06 | checked-clean | Theorem 3's displayed last-true-point boundary and the printed \(x+1\) length prose inconsistency are verified and correctly reported. |
| R2-M07 | checked-clean | Corollary 1's \(B(\bot,\bot)\) tail guard, inclusive \(x\le k\) bound, loop deletion, zero-length case, and all-false endpoint are correctly reflected. |
| R2-M08 | checked-clean | Both counterexamples to the printed bit formula and the counterexample to the one-character repair are correct. |
| R2-M09 | checked-clean | Bruyère--Hansel--Michaux--Villemaire 1994, printed pp. 202--203, supports the \(P_2/\in_2/V_2\) correction history and strict nondefinability/non-equivalence claim. |
| R2-M10 | checked-clean | The false Theorem 4 reverse claim is traced into Theorem 9 and base-regularity status; retained source-note sentences qualify the false signature and later corrected \(\in_2/V_k\) route. |
| R2-M11 | not-checked with reason | Not assigned to this source-fidelity seat for full proof-correctness derivation; I checked source attribution that Corollary 5 is retained only through the surviving direction. |
| R2-M12 | checked-clean | Theorems 6--8 preserve terminal-marker encoding, empty word, string behavior versus behavior, and identify Theorem 7 analysis as dependent on the repaired construction. |
| R2-M13 | checked-clean | The binary-to-ternary sentence is verified as tentative in the report and qualified in the source note; the reader does not overclaim it. |
| R2-M14 | checked-clean | Reader, source note, compact record, shared theorem, bibliography, and open ledger agree without completion inflation. |
| R2-M15 | checked-clean | AGENTS terminology rule applied; special output, finite witness, \(\in_2\), and \(V_2\) have necessity, exact definition, standing, nonredundancy, and later use. |
| R2-M16 | checked-clean | Report/journal/later-source attribution, page locators, rights boundary, topic-only scope, and no-test/no-build boundary are correct. |

VERDICT: ACCEPT
