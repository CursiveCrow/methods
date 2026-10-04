# N-c-014.a — Büchi 1960 source note

**Outcome:** **COMPLETE 1959 PRIMARY PRECURSOR ACQUIRED AND RECONSTRUCTED WITH ITS DEFECTS EXPLICIT; 1960 JOURNAL VERSION NOT PAGE-RECONCILED.** The University of Michigan preserves Büchi's complete September 1959 technical report under the same title as the registered 1960 article. It supplies the literal weak second-order language, finite automaton, special-output behavior, correspondence construction, finite-word encoding, regularity theorem, decision proof, arithmetic claims, and examples needed for the reader. Direct mathematical review found a miscopied Definition 2 in the first reconstruction, a repairable defect in the report's printed Theorem 2 proof, an off-by-one inconsistency in Theorem 3's prose, and a false Theorem 4/9 equivalence for the unary powers-of-two signature. The reader now separates the report's statements, handbook-owned repairs, and the later published correction history. The report is not evidence that the 1960 article has identical wording, numbering, pagination, corrections, or proof detail.

**Retrieved:** 2026-08-23  
**Repository item:** <https://deepblue.lib.umich.edu/items/3ddcc1ff-f04d-406e-805e-582ff238ce01>  
**Permanent handle:** <https://hdl.handle.net/2027.42/3930>  
**Repository identifier:** UMR1083  
**Unaltered PDF:** tmp/pdfs/p09-buchi-1960/buchi-1959-umr1083.pdf  
**Repository OCR:** tmp/pdfs/p09-buchi-1960/buchi-1959-umr1083.txt  
**Saved item metadata:** tmp/pdfs/p09-buchi-1960/deepblue-item-metadata-2026-08-23.json

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| PDF scan | 3,135,482 | 18D1BF4C44E9581932239B500DA8E220876AD7F9B602451BF6B9B22795F840FD |
| Repository OCR/SGML | 74,673 | 9AD26515AE6689320FC031030C361842DDDD30067FF94E2F7D9324DF758599D1 |
| DSpace item metadata | 6,219 | ED876B198344B7B03EEFCC18AC57C73805DDDE5A2FEE93C5E500B482F0F42962 |

**Rights caution:** the repository makes the files publicly readable but supplies no open-content licence in the item metadata. Its site-wide notice treats deposited works as copyright protected unless otherwise indicated. The local files are research copies; no redistribution permission is inferred.

## Exact identities and version boundary

### Acquired report

The cover reads:

> J. Richard Büchi, *Weak Second-Order Arithmetic and Finite Automata*, Technical Report, University of Michigan, College of Literature, Science, and the Arts, Logic of Computers Group, September 1959.

The repository supplies identifier UMR1083 and classifies the object as a technical report. The funding page names NSF grant G-4790, ONR contract NONR-1224(21), Army Ordnance contract DA-20-018-ORD-16971, and Army Signal Supply Agency contract DA-36-039-sc-78057.

### Registered journal article

The registered bibliography remains:

> J. Richard Büchi, “Weak Second-Order Arithmetic and Finite Automata,” *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik* 6, nos. 1–6 (1960): 66–92. DOI <https://doi.org/10.1002/malq.19600060105>.

Wiley's live record verifies author, title, year, volume, issue, pages, DOI, and bibliography. On 2026-08-23, the technical PDF required institutional/member access or purchase; no purchase was authorized. The 1990 collected-works reprint, pp. 398–424, DOI <https://doi.org/10.1007/978-1-4613-8928-6_22>, was likewise access-controlled.

The report predates the article, bears the same title, and contains the complete mathematical development. The journal has 27 printed pages, while the report has 45 numbered pages in a technical-report layout. No claim of textual or theorem-number identity is made without the journal body. Reader locators therefore cite Buchi1959WeakReport; Buchi1960 controls journal identity only.

### Later correction record for the arithmetic claim

Véronique Bruyère, Georges Hansel, Christian Michaux, and Roger Villemaire, “Logic and \(p\)-Recognizable Sets of Integers,” *Bulletin of the Belgian Mathematical Society -- Simon Stevin* 1(2) (1994), 191–238, DOI <https://doi.org/10.36045/bbms/1103408547>, supplies the later historical and mathematical correction at printed pp. 202–203. It reports that McNaughton's 1963 review identified the failure of Büchi's claimed equivalence with the unary predicate \(P_2\), replaces that signature by the binary bit-occurrence relation \(\in_2\), notes its equivalence with the greatest-power-divisor function \(V_2\), and cites Semenov for the nondefinability of \(V_2\) in \((\mathbb N,+,P_2)\). Its openly readable journal PDF was inspected at the controlling pages through the EuDML/EPFL public record. This later article is correction evidence, not a substitute for the 1959 report's own wording.

## Access-route ledger

| Route | Result | Body delivered? |
|---|---|---:|
| [Deep Blue item page](https://deepblue.lib.umich.edu/items/3ddcc1ff-f04d-406e-805e-582ff238ce01) | Public metadata exposed the PDF/TXT filenames and bitstream UUIDs. The web front door intermittently presented a Cloudflare challenge. | Metadata only through the front door. |
| Deep Blue public backend PDF endpoint | HTTP 200, Content-Type application/pdf, Content-Length 3135482, filename bab9796.0001.001.pdf. Saved unaltered. | **Yes.** |
| Deep Blue public backend TXT endpoint | HTTP 200, Content-Type text/plain, Content-Length 74673, filename bab9796.0001.001.txt. Saved unaltered. | **Yes, repository OCR.** |
| [Wiley DOI record](https://onlinelibrary.wiley.com/doi/10.1002/malq.19600060105) | Complete metadata and reference list; journal PDF access-controlled. | No. |
| [Springer collected-works chapter](https://link.springer.com/chapter/10.1007/978-1-4613-8928-6_22) | Reprint metadata; chapter PDF access-controlled. | No. |
| [Bruyère--Hansel--Michaux--Villemaire journal record](https://eudml.org/doc/232407) | Public complete 1994 survey; printed pp. 202–203 give the correction history and distinguish \((\mathbb N,+,P_2)\), \((\mathbb N,+,\in_2)\), and \((\mathbb N,+,V_2)\). | **Yes, later correction evidence.** |
| [NTIS record AD225753](https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/AD225753.xhtml) | Corroborates 1959, Büchi, University of Michigan, 50-page report, and ONR contract; exposes no downloadable file. | No. |
| Logic Library catalogue, ResearchGate, Internet Archive title/filename search, and general title/PDF search | Catalogue entry, request-full-text page, or no matching downloadable object. | No additional verified body. |

The successful backend endpoints are repository infrastructure, not a bypass of a restricted document: the item is marked inArchive true, discoverable true, withdrawn false, and both content requests returned ordinary anonymous HTTP 200 responses.

## Visual page-completeness audit

pdfinfo reports 48 unencrypted A4 pages. All 48 pages were rendered with Poppler and inspected visually. Contact sheets were also inspected, followed by full-size inspection of the title, syntax, automaton, synthesis/analysis, finite-word, regularity, arithmetic, feedback, and endpoint pages.

| PDF pages | Printed material | Finding |
|---|---|---|
| 1 | Technical-report cover | Title, author, institutional series, and September 1959 date present. |
| 2 | Funding/contract page | Complete; no numbered mathematical content. |
| 3–45 | Numbered pp. 1–43 | Continuous introduction and §§1–9. No missing, duplicated, clipped, or substituted page. Displayed formulae are visually legible. |
| 46–47 | Numbered pp. 44–45 | Complete bibliography, entries 1–15. |
| 48 | Repository barcode/end leaf | Confirms physical endpoint after the bibliography. |

The repository OCR is useful for search and prose extraction but corrupts many logical symbols, vector accents, superscripts, and inequalities. It was never treated as proof of a formula. Every formula used in the reader was reconciled against the rendered scan.

## Exact report map

| Printed pages | Source division | Reader use |
|---:|---|---|
| 1 | Introduction | Relation to Kleene synthesis/analysis; scope and announced contribution. |
| 2–4 | §1, “Notations and Terminology” | Variable sorts, formula standing, vector notation, semantics, special predicates. |
| 4–6 | §2, “Weak Second-Order Arithmetic” | Intended structure and Lemma 1 normal form. |
| 6–14 | §3, “Finite Automata” | Definitions 1–4 and Lemmas 2–6. |
| 14–18 | §4, “Analysis and Synthesis” | Lemma 7; Theorems 1–2 and their constructions. |
| 18–26 | §5, “Definability in W.2.A.” | Definition 5; Theorems 3–5; Corollaries 1–5. |
| 26–30 | §6, “Other Concepts of Finite Automata” | Comparison with Church and other automata; many-input extension; Theorems 1′–2′. |
| 30–41 | §7, “Finite Strings versus Special Predicates; Regular Relations” | Exact word encoding; Definitions 6–7; Theorems 6–9 and 8′; base-dependent regularity. |
| 41–42 | §8, “Remarks on Feedback” | Finite-set quantification as the feedback/Kleene-star operation. |
| 42–43 | §9, “An Unsolved Problem” | Open branching-arithmetic question and Theorem 10. |
| 44–45 | Bibliography | Source context and endpoint. |

## Controlling mathematical reconstruction

### Language, domains, and the meaning of “weak”

The formal syntax has individual variables \(x,y,z,t,\ldots\), propositional variables \(X,Y,Z,\ldots\), and monadic predicate variables \(i,j,r,s,\ldots\). Formulas are those of the restricted—monadic—second-order predicate calculus over \(0\), successor, Boolean connectives, and both sorts of quantifiers.

The intended interpretation fixes:

- individuals as natural numbers;
- \(0\) as zero and \( '\) as successor;
- predicates as Boolean functions on the natural numbers;
- **special predicates** as predicates eventually equal to false, equivalently finite subsets of the natural numbers; and
- predicate quantifiers as ranging only over special predicates.

The interpreted system is \(W.2.A.\). The report says it will not use a deductive structure on the syntactic frame. Thus the standing is an interpreted language/theory, not a proof calculus. “Weak” is exactly the finite-set restriction; it is not a quantifier-alternation fragment and not the later full-set infinite-word theory.

An \(n\)-predicate is an \(n\)-tuple of predicates. Büchi uses vector notation and at times intentionally overloads a syntactic formula with its interpretation. The handbook removes that ambiguity whenever a standing matters.

### Lemma 1: local successor normal form

For every formula \(C(i^n)\), Lemma 1 effectively constructs an equivalent formula

\[
 C^*(i^n)=
 (\mathbf Q\mathbf j)
 \left[
   K(\mathbf j(0))
   \land
   (\forall t)
   B(i^n(t),\mathbf j(t),\mathbf j(t'))
 \right],
\]

where \(\mathbf Q\mathbf j\) is a finite prefix of existential and universal special-predicate quantifiers, \(K\) and \(B\) are propositional matrices, and \(t'\) is successor. The proof:

1. removes the constant \(0\) from arbitrary positions by defining zero;
2. removes iterated successor and successor inside predicate arguments using new predicate variables;
3. passes to prenex form;
4. moves individual quantifiers into the matrix using Behmann's monadic device; and
5. replaces remaining individual existential/universal clauses by special-predicate quantifiers that encode finite initial segments.

This lemma is the source of the finite local-state presentation. It is not itself an automaton theorem.

### Definition 1: automaton

For input variables \(X^n\) and transit variables \(Y^m\), an \(n/m\)-automaton is the \(2m\)-tuple of propositional formulas written as

\[
 E^m,\qquad H^m[Y^m,X^n].
\]

\(E^m\) supplies the initial \(m\)-bit transit state and \(H^m\) supplies its update. Given an input \(n\)-predicate \(i\), the transit recursion is

\[
 r(0)=E,\qquad r(t')=H[r(t),i(t)].
\]

The recursion defines the transit predicate \(r=\psi(E,H,i)\). A binary output is a propositional formula \(U[Y^m]\), and the output recursion adds

\[
 u(t)=U[r(t)].
\]

The source object is therefore not the modern set/function tuple \((Q,\Sigma,\delta,q_0,F)\). It is finite Boolean formula data inducing a deterministic bit-state recursion. The state set is eliminably \(\{\bot,\top\}^m\), but the report presents the formula tuple first.

### Definitions 2–3: special output and behavior

\(U\) is a **special output** of \(E,H\) exactly when the propositional identity

\[
 U[Y^m]\equiv U[H(Y^m,\bot^n)]
\]

holds identically in the state variables \(Y^m\). It is pointwise invariance of the output under one all-false-input transition. Once a special input has become permanently \(\bot^n\), repeated use of this identity makes the output eventually constant. For a special input \(i\), either \(u\) or its Boolean complement is consequently special. The earlier frozen reconstruction incorrectly put \(U[\bot^m]\) on the left; three blind reviewers independently identified that non-equivalent transcription error.

The behavior is

\[
 \beta(E,H,U)=
 \{i:\ i\text{ is a special }n\text{-predicate and }
       (\exists x)(\forall t\ge x)\,u(t)\}.
\]

Thus acceptance means eventual permanent truth. The special-output condition belongs to \(U\) relative to \(E,H\); it is not an acceptance set and not a condition on arbitrary infinite inputs.

### Lemmas 2–7: closure and input removal

- Lemma 2 replaces \(U\) by \(\neg U\), obtaining the complement of the behavior among special inputs.
- Lemma 3 converts an automaton/output to the source's **expanded form**: transition and output formulas are disjunctive state tests. This form is a derived presentation required for later input manipulation, not a new automaton kind.
- Lemma 4 analyzes how a guessed binary input track can be incorporated into an expanded transition.
- Lemma 5 constructs finite look-ahead output formulas needed to preserve specialness.
- Lemma 6 effectively removes one input component: existential projection of one special predicate is again the behavior of an automaton with special output.
- Lemma 7 constructs a special-output automaton for a quantifier-free local formula \(K[i(0)]\land\forall t\,B[i(t),i(t')]\).

The roles matter. Complement realizes universal predicate quantification through duality; Lemma 6 realizes existential finite-set quantification; Lemma 7 is the propositional/local base case.

### Theorems 1–2: synthesis and analysis

**Theorem 1 (synthesis).** From every \(W.2.A.\) formula \(C(i^n)\), one can effectively construct an \(n/m\)-automaton \(E,H\) with special output \(U\) such that

\[
 \beta(E,H,U)=\{i:\ C(i)\}.
\]

The proof first applies Lemma 1, constructs the quantifier-free automaton with Lemma 7, and then realizes the finite-set quantifier prefix through repeated projection, complement, and restoration of expanded form.

**Theorem 2 (analysis).** The report states that from every \(n/m\)-automaton with special output one can effectively construct a formula \(C(i^n)\) with the same behavior and of the exact form

\[
 (\exists\mathbf j)
 \left[
   K(\mathbf j(0))
   \land
   (\forall t)
   B(i(t),\mathbf j(t),\mathbf j(t'))
 \right].
\]

The intended witness tuple contains the transit recursion and a finite initial-segment predicate encoding the eventual-truth cutoff. The proof explicitly notes the real problem that an unrestricted transit run need not be special. Its displayed formula (2) does not solve that problem. Both the transit witness \(r\) and cutoff predicate \(j\) are weak second-order variables and therefore finite. On the tail where \(j(t)\) is false, formula (2) requires \(U[r(t)]\); because finite \(r\) is eventually \(\bot^m\), this imposes \(U(\bot^m)=\top\). Printed Definition 2 does not imply that condition.

A one-bit counterexample is

\[
 E=\top,\qquad H(y,x)=y,\qquad U(y)=y.
\]

The printed special-output identity \(U(y)=U(H(y,\bot))\) holds. The unique run remains \(\top\), so every special input is accepted. But no finite \(r,j\) satisfy formula (2), since eventually \(r(t)=\bot\) while its tail clause demands \(U(r(t))=\top\).

The analysis theorem is nevertheless recoverable by a local finite-witness formula. Quantify finite predicates \(r,j\), require \(j(0)\), and impose

\[
\begin{aligned}
 r(0)&=E,\\
 \forall t\;&(j(t+1)\rightarrow j(t)),\\
 \forall t\;&(j(t+1)\rightarrow r(t+1)=H(r(t),i(t))),\\
 \forall t\;&(\neg j(t+1)\rightarrow i(t)=\bot^n),\\
 \forall t\;&(j(t)\land\neg j(t+1)\rightarrow U(r(t))).
\end{aligned}
\]

Because \(j\) is finite, nonempty, and downward closed, it is exactly an initial segment ending at some \(h\). The witness \(r\) follows the actual run through \(h\), the input is false from \(h\) onward, and the boundary test \(U(r(h))\), together with pointwise special-output invariance, propagates truth along the actual omitted tail. Conversely, for an accepted special input choose \(h\) after input extinction and eventual output truth, retain the actual run through \(h\), and set \(r\) false afterward. The clauses are local in \(t,t+1\), including the case \(h=0\), so propositional expansion yields the theorem's advertised existential local normal form.

This repaired formula is handbook-owned. The report's theorem statement is correct, but its displayed proof formula is not. Theorem 3, Corollaries 1–2, and Theorems 7–8 use the repaired analysis direction in the reader; they are not credited to formula (2) as printed.

### Theorem 3 and the sentence decision procedure

Definition 5 calls a formula normal when it has the local existential state form plus propositional tests \(A_v[\mathbf j(x_v)]\) at its free individual variables. Theorem 3 converts any formula \(C(i,x_1,\ldots,x_p)\) effectively to this form. Its displayed encoding represents \(x_v\) by a downward-closed special predicate with boundary \(s(x_v)\land\neg s(x_v+1)\), so \(x_v\) is the last true point. Printed p. 19 says instead that \(x_v+1\) is the predicate's length, which conflicts with p. 8's definition of length as the least \(h\) such that the predicate is false at every \(t>h\). The displayed boundary is coherent, including at \(x_v=0\), and is the convention adopted by the reader; the off-by-one source prose is not silently repeated.

Corollary 1 decides closed sentences. A normal sentence asks for a special state predicate \(\mathbf j\) such that:

1. \(\mathbf j(0)\) satisfies \(K\);
2. every adjacent pair satisfies \(B\); and
3. the sequence reaches the all-false tail required by specialness.

The report first requires \(B(\bot,\bot)\). If this tail guard is false, the sentence is false because every finite predicate is eventually the constant all-false state. If the guard is true and \(k\) is the number of Boolean states, the report searches for \(x\le k\) and states \(Y_0,\ldots,Y_x\) such that \(K(Y_0)\), each consecutive pair satisfies \(B\), and \(Y_x=\bot\). Any longer witnessing path repeats a state, and deleting the intervening loop preserves every local \(B\)-constraint. The previous reconstruction omitted the tail guard and called the bound strict; the reader now retains both the guard and the report's inclusive \(x\le k\) formulation. This finite loop-deletion argument is the report's proof of decidability.

Corollary 2 sharpens the unary case: a set of natural numbers is \(W.2.A.\)-definable iff it is ultimately periodic. The recurrence used in the normal form effectively supplies a phase and period, and Corollary 1 makes the necessary reachable-state selection effective.

### Binary arithmetic presentation

The report maps each special predicate \(i\) to

\[
 f(i)=\sum_{x\in i}2^x.
\]

This is a bijection from finite subsets of \(\mathbb N\) to natural numbers. Theorem 4 *claims* effective equivalence between \(W.2.A.=[0,',\exists_0 i]\) and first-order \([=,+,\operatorname{Pw}_2]\), where \(\operatorname{Pw}_2(x)\) says that \(x\) is a power of two. The first-order-to-weak-second-order direction formalizes binary addition by a finite carry predicate and is sound. The reverse direction depends on the displayed formula

\[
 E(x,y):=\operatorname{Pw}_2(x)\land\exists u\exists v\,
 \bigl(y=u+x+v\land u<v\land(v=0\lor 2x\le v)\bigr),
\]

which the report says expresses that the \(x\)-bit occurs in \(y\). It does not. The genuine occurrence \((1,1)\) is rejected. Conversely, \((x,y,u,v)=(2,8,2,4)\) satisfies the formula although the \(2\)-bit of \(8\) is zero. Replacing only \(u<v\) by \(u<x\) still leaves \((2,8,0,6)\) as a false witness. The intended arithmetic decomposition would require the high part to be divisible by \(2x\), not merely at least \(2x\).

The later correction changes the signature. Define \(x\mathrel{\in_2}y\) to mean that \(x\) is a power of two whose coefficient in the binary expansion of \(y\) is 1. Equivalently, define \(V_2(0)=1\), and for \(y>0\) let \(V_2(y)\) be the greatest power of two dividing \(y\). Bruyère--Hansel--Michaux--Villemaire, printed pp. 202–203, report McNaughton's replacement of \((\mathbb N,+,P_2)\) by \((\mathbb N,+,\in_2)\), explain the equivalence with \((\mathbb N,+,V_2)\), and cite Semenov for the fact that \(V_2\) is not definable in \((\mathbb N,+,P_2)\). Thus Büchi's Theorem 4 equivalence, and Theorem 9's resulting claim that the \([=,+,P_2]\)-definable relations are exactly the 2-regular relations, are false as stated. They cannot be repaired by a one-character emendation.

Corollary 5's decidability conclusion survives: only the sound translation from first-order \([=,+,P_2]\) into decidable \(W.2.A.\) is needed for it, and the later survey also records decidability of \((\mathbb N,+,P_p)\). The exact automatic/weak-monadic definability equivalence belongs instead to the \(\in_2\) or \(V_2\) signature. All of these claims remain about definability under an explicit encoding; no finite predicate is identified with a natural number without the map \(f\).

### Exact finite-word encoding

Let \(\Sigma_n=\{\bot,\top\}^n\). For a nonempty finite word

\[
 \bar Y=Y_0Y_1\cdots Y_h\in\Sigma_n^*,
\]

§7 defines its associated special predicate by

\[
 f(\bar Y)(t)=
 \begin{cases}
   Y_t,&0\le t\le h,\\
   \top^n,&t=h+1,\\
   \bot^n,&t>h+1.
 \end{cases}
\]

The empty word is encoded by \(\top^n\) at \(0\) followed by \(\bot^n\) forever. The terminal \(\top^n\) marker is essential. It lets the automaton detect the source's endpoint while the whole object remains a finite predicate.

Definition 6 calls the set of words accepted at their terminal point the **string behavior** (“sg-behavior” in the report). If \(r\) is the transit recursion for \(Y_0\cdots Y_h\), the word is accepted exactly when \(U[r(h+1)]\). Unlike behavior \(\beta\), string behavior permits an arbitrary output because acceptance is read at one finite endpoint.

Theorem 6 proves that a word set is an arbitrary-output string behavior iff it is a special-output behavior. Its construction adds a state bit recording the output at the encoded terminal marker; the converse substitutes the all-false continuation into a special output.

Theorem 7 then states effective analysis and synthesis for string behavior and finite-word formulas. Theorem 8 combines this with the classical finite-automaton result already cited by the source:

1. arbitrary-output string behavior;
2. special-output behavior;
3. \(W.2.A.\)-definability by a formula whose assignments are word encodings; and
4. regularity

are equivalent conditions on a set of finite \(n\)-strings.

Theorem 8′ extends regularity from languages to relations among several finite words by using the report's many-input automata. This is a defined extension: a relation is regular when an extended \(W.2.A.\) formula defines exactly tuples of word encodings.

### Source examples and consequences

The reader uses source-controlled examples rather than inventing a modern automaton run and attributing it to Büchi:

- The terminal-marker map above is the report's explicit bridge from words to finite predicates.
- Corollary 2 gives the exact unary example class: ultimately periodic sets and only those sets.
- Theorem 4's carry-predicate formula supplies a concrete and sound binary-addition construction in the first-order-to-weak-second-order direction.
- Theorem 9 claims that relations definable in \([=,+,\operatorname{Pw}_k]\) are exactly the \(k\)-regular relations under modified base-\(k\) expansion. Its reverse direction inherits the false unary-powers equivalence; the corrected exact characterization uses the bit-occurrence relation or \(V_k\).
- The report develops a base-comparison argument and then says the binary/ternary result “seems to mean” that there is no finite automaton translating every binary expansion into its corresponding ternary expansion. The tentative wording is preserved; the report does not print the separate reduction needed for an unqualified converter-impossibility theorem.
- Section 8 identifies the recursive state update with feedback and shows at formula level that union, concatenation, and Kleene star are definable; the finite-set quantifier is the operation corresponding to star/feedback.

These examples have different standings: the first is an encoding, the second a definability classification, the third a sound formula construction, the fourth a false source claim with a corrected signature, the fifth a tentative application, and the sixth an operator comparison.

## Source qualifications and transcription cautions

1. The report repeatedly uses “special predicate” and occasionally “restricted predicate” for the same finite-set domain. The reader defines the source term once and uses it consistently.
2. The source intentionally overloads tuple notation and sometimes a formula with its interpretation. The reader restores typed distinctions among formula tuples, time predicates, and behavior sets.
3. Printed p. 19's statement that \(x+1\) is the “length” of the initial segment conflicts with p. 8's definition; the reader uses the exact last-true-point boundary formula instead.
4. The report's finite-string “length” convention is indexed by the last data position and then adds a terminal successor position. The reader writes the encoding explicitly instead of relying on that convention.
5. The report's automaton is deterministic formula-defined bit-state recursion. A modern nondeterministic tuple may explain the later theorem but cannot replace this literal source object.
6. Theorem 2's printed cutoff formula is false under printed Definition 2; the reader labels and proves a handbook-owned corrected formula rather than silently strengthening “special output.”
7. Theorems 4 and 9 are false for the unary \(P_2\) signature. The corrected \(\in_2/V_2\) result is later scholarship and is explicitly distinguished from the report.
8. The OCR is materially unreliable for mathematical symbols. Formulae are controlled by the rendered scan.
9. The 1959 report closes the source reconstruction at precursor strength only. It does not close the registered 1960 article's literal pagination, wording, numbering, revisions, or corrections.
10. Büchi 1962 is a different paper about full monadic set quantification and infinite sequences. Nothing in this note imports its acceptance condition or theorem hierarchy into the 1959 report.

## Reader-facing integration

Updated handbook/parts/p09/presentations/n-c-014.tex now supplies:

- the report/article version boundary;
- the literal finite-set domain and meaning of “weak”;
- the source \(E,H,U\) automaton and its typed recursion;
- the exact special-output identity and eventual-truth behavior;
- Lemma 1 normal form;
- Theorems 1–2 with the roles of complement, expanded presentation, and input projection, plus the counterexample to printed formula (2) and an explicit corrected construction;
- the exact terminal-marker word encoding;
- Theorems 6–8 and their four equivalent conditions;
- Theorem 3's exact last-true-point convention and its printed off-by-one prose;
- Corollary 1's false-tail guard, inclusive finite bound, and loop-deletion decision proof;
- ultimate periodicity, the false unary-powers equivalence and corrected \(\in_2/V_2\) signature, and the feedback/Kleene-star comparison; and
- an explicit statement that journal reconciliation remains open.

Added Buchi1959WeakReport and BruyereEtAl1994 to handbook/bib/handbook.bib and added Büchi to the source field and citation of the public finite-word correspondence theorem in handbook/parts/p09/logic-in-computer-science.tex.

## Remaining obligation

Acquire a lawful complete copy of the 1960 journal article or the 1990 reprint and compare it page by page with UMR1083. Record every change in definitions, theorem numbering, proof detail, examples, references, and terminology. Until then:

- the **mathematical precursor presentation may close only with the report's defects and handbook repairs explicit**;
- the **1960 journal-version fidelity check remains open**; and
- no journal page number may be used as a locator for a claim verified only in the report.

Round 1 independent scholarly review rejected the first frozen reconstruction
and produced the corrections recorded above. Round 2 then returned three
independent **ACCEPT** verdicts on one unchanged corrected snapshot. The 1959
report-precursor presentation is therefore closed at that explicit strength;
literal 1960 journal-version fidelity remains open. The exact hashes, reports,
finding disposition, and admission boundary are preserved in
[the independent review record](p09-buchi-1959-report-independent-review-record.md).
No manuscript build, automated test, checker, repository script, TeX command,
or handbook-PDF inspection was used in this source/reconstruction or review
pass.

## Reader exposition updated on 2026-09-06

The active N-c-014 text now states the mathematics directly. The error
history above remains provenance and supersedes any earlier requirement to
repeat defective formulas in the reader. The finite-witness analysis proof
retains its corrected boundary clauses, while the counterexample to the
report's formula (2) and its source ownership remain in this note. The
individual-variable encoding now states its support exactly as `{0,...,x}`.

The arithmetic section uses the binary relation `x in_2 y`, with `x` a
power of two occurring as a binary digit of `y`. It no longer displays the
false unary-powers definition or asserts the report's incorrect reverse
characterization. The direct proof represents an individual `t` by `2^t`
and a finite predicate `I` by `F(I)`, translates individual quantifiers with
the guard `Pow(x) := x in_2 x`, and translates set quantifiers to arbitrary
natural-number quantifiers. In the other direction each number is its
finite set of binary positions; singleton membership expresses `in_2` and
a finite carry predicate expresses addition. The displayed old/current/next
bit equations prove this translation without using the defective formula.

The numerical relation theorem is stated for simultaneous, least-significant
bit first canonical encodings, with the zero tuple encoded by the empty
word. Appending or right-quotienting by the fixed terminal marker connects
that convention to the earlier word theorem. This is the corrected
binary-relation signature supported by the 1994 article at pp. 202-203,
with the explicit atomic translation proof supplied in the handbook. It
is not a claim that the 1959 report printed that signature or proof.

No build, software test, or render was performed for this edit. The older
review verdicts record their historical snapshots and do not constitute
independent review of the present changes.
