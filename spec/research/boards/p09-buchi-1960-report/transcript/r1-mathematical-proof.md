# Blind mathematical and proof-correctness review

## Seat, blindness, and method

I reviewed the frozen Büchi 1959 technical-report presentation as the mathematical-and-proof-correctness seat. I did not read a chair file, ledger, another reviewer transcript or verdict, the Büchi 1962 board, or any non-frozen presentation artifact. I did not contact another reviewer.

Before judging the mathematics, I independently recomputed every chartered SHA-256 identity. I then visually inspected every rendered source page, page-01.jpg through page-48.jpg, separately and at original detail. I read every line of each chartered textual artifact in scope. I did not run a test, automated checker, repository script, TeX command, handbook build, or handbook-PDF inspection.

The rendered-file/printed-page map established by inspection is:

- rendered page 1: report cover;
- rendered page 2: funding and administrative leaf;
- rendered pages 3–47: printed report pages 1–45;
- rendered page 48: endpoint and library-control leaf.

Thus, for example, printed report page 7 is rendered page 9, printed page 17 is rendered page 19, and printed page 24 is rendered page 26. Findings below cite the printed report page and, in parentheses where it is especially useful, the rendered file page.

## Frozen identities

All six recomputed identities match the charter exactly.

| Frozen artifact | Recomputed SHA-256 | Result |
|---|---|---|
| tmp/pdfs/p09-buchi-1960/buchi-1959-umr1083.pdf | 18D1BF4C44E9581932239B500DA8E220876AD7F9B602451BF6B9B22795F840FD | checked-clean |
| handbook/parts/p09/presentations/n-c-014.tex | 1D4E34CE6B2602BEF520146ECC6F78C492A969CE6C8FE884912DC0959AFF6713 | checked-clean |
| handbook/parts/p09/logic-in-computer-science.tex | 1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8 | checked-clean |
| handbook/bib/handbook.bib | FAACDA885C9671FD41509F0FCB24934CBA0B4AFD8BC1E6368C2DE355E8B03DFA | checked-clean |
| spec/research/p09-buchi-1960-source-note.md | 15165056F88D051DB0A5CB33B3C55A79F39AF2EEE62C507C756226CF851B411E | checked-clean |
| spec/research/p09-source-presentations-lot2-3.md | E7DD8167EA70A32F72F09C12A478637F8C5ECCB3C7AA6E98BCC7918ECFB00285 | checked-clean |

The review therefore concerns the exact frozen artifacts named in the charter.

## Findings

### MP-01 — Definition 2 is misquoted, changing the class of automata

- Severity: blocker.
- Exact presentation locations: n-c-014.tex lines 49–54; p09-buchi-1960-source-note.md lines 150–168; p09-source-presentations-lot2-3.md line 624.
- Exact source location: printed report page 7 (rendered page 9), Definition 2. Printed report pages 12–13 also use the actual identity in the proof of Lemma 5.
- Invariants violated: exact formula transcription; source/presentation separation; definition before theorem use; theorem hypotheses must be preserved; cross-artifact reconciliation.

The printed Definition 2 says that an output function \(U\) is special when
\[
  U[Y^m]\ \equiv\ U[H(Y^m,\bot^n)].
\]
This is a pointwise invariance assertion: for every transit-state tuple \(Y^m\), one all-false input transition preserves the truth value of the output. The proof of Lemma 5 on printed pages 12–13 independently confirms this reading by proving \(W[Y]\equiv W[H(Y,\bot)]\) and then calling \(W\) special.

The presentation instead displays
\[
  U[\bot^m]\ \equiv\ U[H(Y^m,\bot^n)].
\]
The source note and compact source record repeat that altered left-hand side. These two formulas are not variants of the same condition.

Two one-bit counterexamples establish non-equivalence.

1. Let \(H(y,\bot)=y\) and \(U(y)=y\). The printed identity is true for both values of \(y\), because \(U(y)=U(H(y,\bot))\). The presentation identity is false at \(y=\top\), because \(U(\bot)\ne U(\top)\).
2. Let \(H(y,\bot)=\bot\) and \(U(y)=y\). The presentation identity is true for every \(y\), since both sides are false. The printed identity is false at \(y=\top\).

The harm is structural. “Special output” is a hypothesis of Lemmas 4–6, Theorems 1–2, Definition 4 behavior, and the later string/regularity correspondences. Replacing pointwise invariance by the displayed constant-value condition silently changes which automata the presentation is describing. It also conceals the separate Theorem 2 defect in MP-02, because the altered condition forces \(U(\bot)\) to equal the output after every all-false transition.

Minimum repair: replace the left side by \(U[Y^m]\) everywhere the report definition is quoted or summarized, explicitly identify the formula as the printed Definition 2, and re-audit every dependent construction using the actual pointwise hypothesis. Any stronger condition introduced to repair a later proof must be identified as a handbook-owned strengthening, not attributed to Büchi’s Definition 2.

### MP-02 — The printed Theorem 2 cutoff construction is false under the printed Definition 2, but the presentation asserts it without disclosing or repairing the defect

- Severity: blocker.
- Exact presentation locations: n-c-014.tex lines 93–110, especially the claim at lines 108–110; p09-buchi-1960-source-note.md lines 181–205.
- Exact source location: printed report pages 17–18 (rendered pages 19–20), Theorem 2 and displayed formula (2).
- Invariants violated: theorem-direction correctness; witnesses must inhabit their stated domains; no hidden strengthening of a hypothesis; source defect versus handbook repair must be explicit; finite-witness edge cases must be proved.

The printed theorem seeks to define the behavior of an automaton with special output by an existential local W.2.A. formula. In the printed formula, both the transit witness \(r\) and the cutoff predicate \(j\) are weak second-order variables, so both are special predicates: each is false from some point onward. While \(j\) holds, the formula makes \(r\) follow the transition recurrence. After \(j\) ceases to hold, it requires the input to be all false and requires \(U[r(t)]\).

Because \(r\) is special, \(r(t)=\bot\) eventually. Because \(j\) is special, the tail clause eventually applies. Consequently the displayed formula has the hidden necessary condition \(U(\bot)=\top\). The printed Definition 2 does not imply that condition, even for an automaton accepting a given special input.

Here is a complete counterexample. Use one transit bit and any special input track, ignored by the transition. Put
\[
  E=\top,\qquad H(y,x)=y,\qquad U(y)=y.
\]
The printed special-output condition holds:
\[
  U(y)=y=U(H(y,\bot)).
\]
The unique run begins at \(\top\) and remains \(\top\), so its output is true at every time. Hence every special input is in the automaton’s behavior under the report’s eventual-truth acceptance definition. But no special \(r,j\) can satisfy printed formula (2): sufficiently far out, \(j(t)=\bot\) and \(r(t)=\bot\), so the tail clause demands \(U(\bot)=\top\), whereas \(U(\bot)=\bot\). Thus the behavior and the formula defined on pages 17–18 are not equivalent.

The presentation’s statement that “Specialness of \(U\) is what lets the transit witness be restricted to finite predicates” is therefore false for the report’s actual specialness condition. Together with MP-01, the presentation has the appearance of silently changing Definition 2 to a stronger condition that makes the printed truncation argument work.

A repair is possible, but it is not the printed formula and must be labeled handbook-owned. Define \(j\) by the clauses
\[
 j(0),\qquad \forall t\,(j(t+1)\rightarrow j(t)).
\]
Since \(j\) is special, it is precisely a nonempty finite initial segment. Let its last true point be \(h\), characterized by \(j(h)\wedge\neg j(h+1)\). A finite transit witness \(r\) can then be constrained by
\[
\begin{aligned}
  &r(0)=E,\\
  &\forall t\,(j(t+1)\rightarrow
       r(t+1)=H(r(t),i(t))),\\
  &\forall t\,(\neg j(t+1)\rightarrow i(t)=\bot),\\
  &\forall t\,(j(t)\wedge\neg j(t+1)\rightarrow U(r(t))).
\end{aligned}
\]
The recurrence is required only through \(h\); after \(h\), \(r\) may be false so that it is a legal weak second-order witness. The input is false from time \(h\) onward. The printed pointwise identity \(U(y)=U(H(y,\bot))\) propagates \(U(r(h))\) along the actual infinite all-false tail. Conversely, for any accepted special input, choose \(h\) after the input has become all false and after the run’s output has become true, retain the actual run only through \(h\), and set the weak witness false afterward. This also covers \(h=0\).

Minimum repair: disclose that printed formula (2) is not valid under printed Definition 2, include a counterexample, and either provide and prove an explicit handbook-owned corrected formula such as the one above or reduce every dependent proof-strength claim. Theorem 3, Corollary 1, Theorem 7, and Theorem 8 must be stated as depending on that repair rather than on the printed proof as it stands.

### MP-03 — Theorem 4’s printed bit-occurrence formula is false, and the presentation claims the translation without identifying the required emendation

- Severity: blocker.
- Exact presentation locations: n-c-014.tex lines 157–160; p09-buchi-1960-source-note.md lines 221–231.
- Exact source location: printed report page 24 (rendered page 26), Theorem 4.
- Invariants violated: displayed encoding must express the claimed relation; both translation directions need valid formulas; literal source defects may not be silently normalized.

The report defines \(E(x,y)\) by a displayed arithmetic formula intended to mean that \(x\) is a power of two and that the \(x\)-bit occurs in the binary representation of \(y\). Its decomposition clause is printed as
\[
  y=u+x+v,\qquad u<v,\qquad
  (v=0\ \lor\ 2x\le v).
\]
The inequality \(u<v\) does not isolate the lower-order part of the binary expansion. The needed inequality is \(u<x\).

The printed formula gives both a false negative and a false positive.

1. False negative: take \(x=1,y=1\). The \(1\)-bit plainly occurs. If \(v=0\), the printed \(u<v\) becomes \(u<0\), impossible in the natural numbers. If \(v\ge 2x=2\), then \(u+x+v>1\). So the printed formula rejects \((1,1)\).
2. False positive: take \(x=2,y=8\) and choose \(u=2,v=4\). Then \(8=u+x+v\), \(u<v\), and \(2x\le v\), so the printed formula accepts. But the \(2\)-bit is absent from the binary representation of \(8\).

With \(u<x\), the intended decomposition is correct: \(u\) contains only positions below \(x\), the isolated summand \(x\) records the present bit, and \(v=0\) or \(v\ge2x\) puts every remaining contribution above \(x\).

The theorem being summarized may be repaired by this one-character mathematical emendation, but the frozen presentation presently says that the report effectively identifies the two theories without disclosing that the printed construction it relies on is false.

Minimum repair: quote the literal \(u<v\) formula as a source defect, give at least one decisive counterexample, replace it by \(u<x\) only in an explicitly labeled handbook-owned emendation, and then rederive the weak-second-order-to-first-order direction and Corollary 5 from that repaired relation.

### MP-04 — The free-individual encoding contains an undisclosed source off-by-one inconsistency

- Severity: should-fix.
- Exact presentation location: n-c-014.tex lines 139–148.
- Exact source location: printed report pages 8 and 19 (rendered pages 10 and 21).
- Invariants implicated: endpoint conventions; finite-predicate length; free-individual encoding; source ambiguity must not be hidden by compression.

Printed page 8 defines the length of a special predicate as the least \(x\) such that the predicate is false at every point strictly greater than \(x\). For a nonempty downward-closed predicate whose last true point is \(x\), that length is \(x\).

On printed page 19, the displayed encoding of a free individual \(x\) uses a special predicate \(s\) satisfying \(s(0)\), downward closure, and a boundary occurrence \(s(t)\wedge\neg s(t+1)\) at \(t=x\). This again makes \(x\), not \(x+1\), the length under page 8’s definition. The surrounding prose nevertheless says that \(x_1+1,x_2+1\) are the lengths of the corresponding predicates.

The displayed boundary construction is mathematically usable, including at \(x=0\), but it does not agree with that prose. The presentation’s phrase “representing a number as the length of a special initial-segment predicate” suppresses the inconsistency and leaves the endpoint convention unresolved.

Minimum repair: record the printed \(x+1\) sentence as an off-by-one source inconsistency and adopt one explicit convention. The simplest is to say that the encoded number is the last true point, characterized by \(s(x)\wedge\neg s(x+1)\); then do not call \(x+1\) its length under Definition 3.

### MP-05 — The source note turns a tentative base-conversion remark into an asserted theorem

- Severity: should-fix.
- Exact presentation location: p09-buchi-1960-source-note.md line 277.
- Exact source location: printed report page 41 (rendered page 43).
- Invariants implicated: exact proof strength; source qualification; application claims must not be stronger than the cited text.

After showing that \(\mathrm{Pw}_2\) is not \(3\)-regular, the report says this “seems to mean” that there is no finite automaton translating binary expansions into ternary expansions. The source note instead says that the report “says there is no finite automaton” performing the translation. That drops the author’s explicit qualification, and the report does not supply a separate reduction from a converter to \(3\)-regularity of \(\mathrm{Pw}_2\) at that point.

Minimum repair: preserve “seems to mean” or another unmistakably tentative paraphrase. An unqualified impossibility claim requires a separately supplied and proved reduction.

## Independent mathematical reconstruction

### Language and automata

The report’s W.2.A. language has individual variables ranging over nonnegative integers and predicate variables ranging over predicates that are false from some point onward. Its primitive arithmetic is zero and successor; its logical formation rules are weak second-order quantification plus the ordinary propositional connectives and first-order quantification. The report does not present a proof calculus or derive completeness of a calculus. The frozen presentation states these boundaries correctly at n-c-014.tex lines 18–29.

An automaton has a Boolean initial transit tuple \(E^m\), deterministic Boolean transition tuple \(H^m[Y^m,X^n]\), and Boolean output \(U[Y^m]\). Given input \(i\), the run begins at \(r(0)=E\) and obeys \(r(t+1)=H(r(t),i(t))\); the output is \(u(t)=U(r(t))\). For the report’s behavior notion, the input predicates are special and acceptance is eventual output truth. This is distinct from:

- the run predicates \(r\), which need not be special in the actual infinite run;
- the output predicate \(u\), which is eventually true rather than special;
- the finite weak-second-order witness substituted for a run in Theorem 2; and
- the arbitrary final-output function used in the later string behavior.

Those distinctions are essential to MP-02.

### Sequential Lemma and formula-to-automaton direction

The Sequential Lemma on printed pages 4–6 gives the following normalization sequence.

1. Occurrences of zero are replaced using a formula that uniquely defines zero.
2. Iterated successor terms and successor inside predicate arguments are replaced by newly quantified predicates linked by local successor clauses.
3. The formula is put into prenex form.
4. Behmann’s transformation moves individual quantifiers into the matrix portion.
5. Each remaining individual quantifier is represented by a special finite initial segment, leaving a prefix of weak predicate quantifiers over a local matrix involving only values at a point and its successor.

The presentation’s local schema \(K(q(0))\wedge\forall t\,B(q(t),q(t+1))\) accurately captures the final form, subject to the free-individual endpoint issue in MP-04.

The source’s Lemmas 2–7 support the synthesis induction:

- Lemma 2 complements output.
- Lemma 3 expands a machine so its output can be treated as an added explicit track.
- Lemma 4 realizes the required guessed-track/backward finite-witness construction.
- Lemma 5 constructs the finite-lookahead output and proves its pointwise special-output identity.
- Lemma 6 removes an existentially quantified predicate track.
- Lemma 7 constructs an automaton for the quantifier-free local base.

Starting from Lemma 7, existential predicate quantifiers are removed by Lemma 6. A universal predicate quantifier is handled by complementing, removing an existential predicate, and complementing again. Where the complement operation destroys the presentation needed by the next elimination, Lemma 3 restores an expanded presentation. Iterating this procedure over the finite quantifier prefix yields Theorem 1’s formula-to-automaton direction. This architecture is mathematically coherent when Definition 2 is read as printed; MP-01 must be repaired so that the presentation actually states the hypothesis used by Lemma 5.

### Automaton-to-formula direction

Theorem 2’s intended direction is to encode an accepting infinite run using only finite predicate witnesses. The obstacle is real: the actual transit sequence can remain nonzero forever, so it is not itself a legal weak predicate tuple. One must choose a finite point after both the special input has become all false and the eventual output has become true, retain the run only through that point, and use the pointwise all-false invariance of \(U\) to justify the omitted tail.

That reasoning is valid with the repaired boundary formula derived in MP-02. It is not valid with printed formula (2), because the latter continues testing \(U\) on the weak witness after the witness has been forced to \(\bot\). Thus the semantic idea can be salvaged, but the report’s displayed proof cannot be cited as a correct realization of it.

### Free individuals, decidability, and eventual periodicity

Definition 5 allows individual parameters to occur in the initial and transition tests. For no free individuals, Theorem 3 combines Theorems 1 and 2. A free natural number can be encoded by a downward-closed special predicate with a unique last true point. This step works with the explicit boundary convention in MP-04.

Corollary 1 reduces satisfiability to finite-state reachability only after checking the all-false terminal condition. If the local terminal condition at \((\bot,\bot)\) is false, no weak-predicate valuation can satisfy the formula. If it is true, a satisfying valuation corresponds to a finite path from an allowed initial Boolean state to \(\bot\); any repeated state in a shortest path can be deleted. The zero-length path and an all-false assignment must be retained as edge cases. The report’s finite bound is safe, though not optimized: with \(k\) Boolean states a shortest simple path has fewer than \(k\) transitions, while checking through the stated \(k\)-scale bound remains sound.

For Corollary 2, after normal form and automaton conversion, the finitely many Boolean states can be refined by whether they have an accepting all-false continuation. Iterating the deterministic successor transition on this finite state space must repeat, yielding an effective finite preperiod and period for a unary definable set. Conversely, a fixed finite exceptional part and a congruence class modulo a fixed positive period are definable using zero, successor, order, and a finite number of weak predicate tracks. The equivalence is correct as a finite-state argument, but the route through Theorem 3 inherits MP-02 until the analysis construction is repaired.

### Binary arithmetic

For a finite predicate \(i\), the map
\[
  f(i)=\sum_{i(x)=\top}2^x
\]
is a bijection between weak predicates and natural numbers. The Boolean full-adder recurrence used by the report is correct: the next carry is the majority of the two input bits and the current carry, and the output bit is their parity. A singleton predicate therefore defines the powers of two.

The first-order-to-weak-second-order translation is direct once a natural number variable is replaced by its finite binary predicate and addition is represented by the carry recurrence. The converse requires a correct first-order definition of bit occurrence. The printed \(u<v\) clause fails, as MP-03 proves; the corrected \(u<x\) clause restores the argument. Therefore Theorem 4 and Corollary 5 are mathematically recoverable, but the printed derivation is not correct without the disclosed emendation.

### Finite words and regularity

For a nonempty word with data letters at positions \(0,\ldots,h\), the report encodes the word by its data tracks at those positions, places the all-true marker at \(h+1\), and makes all tracks false afterward. For the empty word the marker occurs at position \(0\), followed immediately by the all-false tail. This convention is injective and handles the empty word.

String behavior differs from infinite behavior. An arbitrary output function is evaluated at the transit state at the marker, before the marker is consumed by a transition. Theorem 6 relates the two forms:

- From arbitrary marker output \(U\), add a Boolean state component that records \(U\) when the marker is encountered and then persists on the all-false tail; output that component. Its output is special in the printed pointwise sense.
- From a special infinite-output machine with output \(W\), define the marker output by \(U(Y)=W(H(Y,\top^n))\), so that it reports the relevant state at the endpoint.

The empty word is covered because the initial state is the state presented to the marker at position \(0\).

Theorem 7’s formula/string-behavior correspondence is obtained by composing Theorems 1, 2, and 6, and the report states the construction as effective. Theorem 8 then relates:

1. string behavior of an automaton with arbitrary output;
2. behavior of an automaton with special output;
3. W.2.A. definability of the coded strings; and
4. regularity in the cited finite-automata sense.

The step from the automaton descriptions to the Kleene-style regular language characterization is a cited classical dependency, not proved from first principles in the report. The shared handbook theorem at logic-in-computer-science.tex lines 811–816 properly identifies the modern MSO/regular-language equivalence and cites Büchi, Elgot, and Trakhtenbrot. The report-controlled directions through Theorem 2, however, remain conditional on repairing MP-02.

### Regular relations, changes of base, and regular operations

Definition 7 extends W.2.A. by relation symbols and calls a relation regular when its added predicate is definable in the extended language. Theorem 8′ gives the corresponding automaton behavior characterization. Theorem 9 identifies addition, multiplication by fixed constants, and the stated base-\(k\) relations as regular by finite-state or definability constructions.

The base-comparison result uses the ultimately periodic length sets obtained from Corollary 2. The report’s exact dependence criterion is that some positive powers agree, \(n^q=k^p\); this is multiplicative dependence, not equality of bases. The binary-to-ternary converter sentence must retain the report’s tentative status, as MP-05 explains.

Section 8’s closure correspondence is also reconstructible:

- disjunction represents union;
- concatenation existentially chooses an individual split point and applies prefix and suffix formulas;
- iteration existentially chooses a finite predicate of cut positions and requires the base formula on each consecutive segment, with separate initial and final segment clauses.

The finite set of cuts is a weak predicate, so its quantification supplies exactly the finite feedback/iteration resource used in the displayed construction. This is a conceptual and formula-level comparison; the presentation should not strengthen it into a claim of a fully formal machine-level identity that the report does not state.

## Cross-artifact reconciliation

The report/article boundary is stated correctly. The cover identifies the September 1959 University of Michigan Research Institute technical report. The bibliography gives both the technical report and the distinct 1960 journal article, including the journal DOI. The source note also correctly says that the frozen scan is the report and that the journal article was not used as a substitute for the report’s page-level proof content.

The compact record and source note accurately map most report sections and theorem numbers. They do not, however, close the mathematical reconstruction at “complete 1959-report strength” while MP-01 through MP-03 remain:

- MP-01 appears in the presentation, source note, and compact record, so it is a reconciled but source-inaccurate formula rather than an isolated typographical slip.
- MP-02 is a defect in the printed source proof that the presentation and source note endorse without disclosure; MP-01’s stronger formula obscures it.
- MP-03 is another printed proof defect that the presentation and source note silently pass over.
- MP-04 and MP-05 concern exact endpoint and qualification control.

No evidence in the inspected artifacts licenses transferring the 1960 journal article’s contents into the report reconstruction. Any future journal reconciliation must remain separately identified.

## M01–M25 disposition

Every charter item was examined. “Finding-linked” means the item was checked and the stated finding records a defect; it does not mean the item was skipped.

| Item | Disposition | Basis |
|---|---|---|
| M01 | checked-clean | All six frozen SHA-256 identities were independently recomputed and match. |
| M02 | checked-clean | All 48 rendered pages were separately inspected at original detail; cover, numbered pages, and endpoint map were confirmed. |
| M03 | checked-clean | Report identity, 1959 date, institutional provenance, access/rights record, and report/article boundary agree across the frozen artifacts. |
| M04 | checked-clean | W.2.A. individual and weak-predicate domains, primitives, and absence of a proof calculus are stated within source strength. |
| M05 | checked-clean | \(E,H,U\), deterministic recurrence, and time indexing agree with printed pages 6–7. |
| M06 | finding-linked: MP-01 | The printed special-output identity is changed to a non-equivalent condition. |
| M07 | checked-clean | Special inputs, actual run, eventual-truth output, finite witness, and later string behavior are distinguishable; MP-02 records the one place the presentation conflates their consequences. |
| M08 | checked-clean | The five normalization moves of the Sequential Lemma were independently traced on printed pages 4–6. |
| M09 | checked-clean | Lemmas 2–7 support complement, expansion, finite guessing/lookahead, projection, and the local base as summarized, once MP-01 is corrected. |
| M10 | checked-clean | Theorem 1’s induction over the predicate-quantifier prefix, including universal quantification by complement–projection–complement, is coherent. |
| M11 | finding-linked: MP-02 | Theorem 2’s printed finite-witness formula is false; an explicit automaton counterexample and a minimum corrected construction are given. |
| M12 | finding-linked: MP-02, MP-04 | Theorem 3’s analysis dependency and the free-individual endpoint/length convention require repair or disclosure. |
| M13 | checked-clean | Corollary 1’s terminal check and bounded reachability, and Corollary 2’s finite-state eventual-periodicity argument, are sound after the Theorem 2 repair; zero-length and all-false cases were checked. |
| M14 | finding-linked: MP-03 | The binary-predicate bijection and addition recurrence are correct, but the printed bit-occurrence relation is false as written. |
| M15 | checked-clean | Nonempty and empty word encodings, marker position, and all-false tail agree with printed pages 26–27. |
| M16 | checked-clean | Theorem 6’s two constructions and marker-before-transition endpoint semantics were independently checked, including the empty word. |
| M17 | finding-linked: MP-02 | Theorems 7–8 have the stated directions and classical regularity dependency, but the analysis direction inherits the unrepaired Theorem 2 defect. |
| M18 | finding-linked: MP-05 | Regular relations and multiplicative dependence are correctly bounded; the binary/ternary application loses the source’s tentative wording. |
| M19 | checked-clean | Union, concatenation, and iteration formulas match the source’s disjunction, split-point, and finite-cut-set constructions. |
| M20 | finding-linked: MP-01, MP-02, MP-03 | Cross-artifact formula agreement does not equal source accuracy; the three mathematical defects are not reconciled as defects. |
| M21 | checked-clean | Theorem numbering and principal printed-page locators are accurate; source, handbook-owned explanation, and modern theorem are generally separated except where the findings say otherwise. |
| M22 | finding-linked: MP-01 | Established source terminology has clear standing and use, but “special output” is assigned the wrong definition. No otherwise unsupported new technical object is required by the presentation. |
| M23 | checked-clean | The 1959 report, 1960 journal publication, and modern MSO/regular-language statement are not bibliographically collapsed. |
| M24 | finding-linked: MP-01, MP-02, MP-03, MP-04 | Exact formula, hidden-hypothesis, finite-witness, and endpoint edge cases were tested by derivation and counterexample. |
| M25 | checked-clean | Review scope, evidence categories, rights/access limits, and the prohibition on build/test substitution were respected. |

## Acceptance determination

MP-01 changes a central source definition. MP-02 supplies a counterexample to the report’s printed automaton-to-formula construction and shows that the frozen presentation silently relies on a stronger, misquoted definition rather than disclosing the source defect. MP-03 shows that the displayed formula used for the reverse binary-arithmetic interpretation is false. These are not cosmetic source-transcription issues: they affect claimed theorem directions and the stated “complete 1959-report strength.” Each has a bounded repair, but none is repaired in the frozen presentation.

VERDICT: REJECT — MP-01, MP-02, MP-03
