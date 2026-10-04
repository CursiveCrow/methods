REJECT

Message verdict: REJECT -- the actual integrated N-c-014 LaTeX is not yet publication-admissible because several operative objects in the Elgot and Thomas passages remain undefined or under-typed at first use.

Report path: `spec/research/p09-n-c-014-integrated-publication-review-r2.md`

## Review scope and protocol

This is the fresh blind adversarial publication/terminology seat for integrated N-c-014 Round 2. I read `handbook/parts/p09/presentations/n-c-014.tex` directly and completely from line 1 through line 1671, then read the host `handbook/parts/p09/logic-in-computer-science.tex` directly at lines 836--946, including the insertion at line 937. I used the five permitted source notes, the permitted N-c-014 compact source-status section and consolidated open-source bullets, and the relevant bibliography entries only to check source identity, authority order, locator strength, rights boundaries, and the standing of source-owned versus handbook-owned claims. Prior verdicts and review histories mentioned inside permitted status records were not treated as review evidence.

I did not open or inspect a manuscript PDF, PNG, render, page image, or derivative. I did not open any prior review, admission record, independent-review record, board file, board ledger, charter, transcript, or chair file. I did not run TeX, a build, a test, a checker, a repository script, a hash operation, or any automated validation. No historical-source page visit was necessary: the permitted source notes resolved the source-level questions, while the defects below are defects in the manuscript's own local definitions and notation.

## Must-fix findings

### 1. Thomas's finite-word automaton is not actually defined at the finite strength needed by Theorem 3.1

At presentation lines 932--939 the manuscript says that Thomas's Section 3.1 uses

\[
 \mathcal A=(Q,\Sigma,q_0,\Delta,F),
 \qquad
 \Delta\subseteq Q\times\Sigma\times Q,
\]

but it never states there that (Q) is a finite state set, that \(\Sigma\) is a finite alphabet, that \(q_0\in Q\), or that \(F\subseteq Q\). Lines 940--945 then define a successful run and assert the effective finite-automaton/MSO equivalence for "such automata." Finiteness is an essential hypothesis, not recoverable decoration: with an unrestricted state set, "recognized by such automata" does not have the asserted finite-automaton strength. The missing memberships also leave the initial and terminal clauses typed only by inference.

The nearby host definition at `logic-in-computer-science.tex` lines 879--908 cannot silently supply these data. It defines a different object, a bottom-up automaton on finite ranked trees; the N-c-014 presentation itself later insists at lines 1373--1377 that Rabin's finite-tree run is not that host object. Earlier uses of the letters (Q\) and \(\Sigma\) likewise do not bind Thomas's new source tuple.

Minimum repair: immediately before or with the display at lines 935--939, state that (Q) is finite (and nonempty if that is the adopted source convention), \(\Sigma\) is a finite alphabet, (q_0\in Q\), and (F\subseteq Q\). Then make explicit that this complete tuple is what "such automata" denotes in line 943.

### 2. Thomas's singleton-set atomic basis uses undefined predicates and does not state the individual-to-singleton encoding

Presentation lines 952--957 say that Thomas passes to the "singleton-set version" \(\operatorname{MSO}_0\) and list atomic forms

\[
 X_j\subseteq X_k,
 \quad \operatorname{Sing}(X_j),
 \quad \operatorname{Suc}(X_j,X_k),
 \quad X_j\subseteq Q_a.
\]

No exact local definition is given for \(\operatorname{MSO}_0\), \(\operatorname{Sing}\), or \(\operatorname{Suc}\), and the symbol (Q_a\) is never defined anywhere in the 1--1671 presentation or the permitted host interval. The last omission is especially harmful because (Q) has just denoted the automaton state set at line 936; a reader cannot tell from the notation whether (Q_a) is a state subset, a position track, or some other source object. The intended standing appears to be the set of word positions carrying the input letter (a), but the actual LaTeX does not say that.

This prevents the claimed formula-to-automaton proof basis from being checked definition-before-use. Naming a "singleton-set version" is not a substitute for stating how an individual variable is represented by a singleton monadic track, and the undefined atomic forms do not meet the supplied technical-name rule's definition and standing requirements.

Minimum repair: define the position structure for a word, define (Q_a\) (or preferably a non-state-conflicting notation such as (P_a\)) as its (a)-labelled position set, define \(\operatorname{Sing}(X)\) and \(\operatorname{Suc}(X,Y)\) exactly, and state that each first-order variable is replaced by a monadic variable constrained to be singleton. If these definitions are deliberately inherited from an earlier numbered definition, cite that definition explicitly and state the notation mapping here; do not rely on an unannounced cross-file scope.

### 3. The handbook-owned unary-window repair is ill-scoped at the symbol (A)

In the erratum discussion, presentation lines 452--463 define, for each relation (R_j\), its field (A_j=\operatorname{field}(R_j)\) and the associated (R_j\)-sequences. Lines 466--482 then give the tagged construction in those locally typed fields. The separate unary case at lines 484--490 suddenly says

\[
 R_j\subseteq A
\]

without introducing any ambient (A\) for this construction. The only earlier capital (A\) in the Elgot presentation is the transducer input alphabet fixed at lines 345--393. It is not the field of the (d)-coordinate local relation in Section 8.6 and cannot type this later (R_j\) merely by symbol reuse. The actual locally available type is (A_j\), or an explicitly introduced common characteristic-column alphabet.

Because the unary case is a handbook-owned completion rather than printed erratum wording, its type must be fully owned and stated by the handbook. The historical source cannot cure an undefined manuscript symbol.

Minimum repair: replace the unbound (A\) with the correctly defined local carrier, or define a common carrier before use. Also state explicitly how the retained one-letter prefix set (E_j\) is used after promoting the window relation to arity two, since the preceding general template at lines 459--463 had (E_j\subseteq A_j^n\). The underlying idea is recoverable -- use (R_j\times R_j\) and retain the original first-letter constraint -- but the published definition must say this with typed carriers.

### 4. Thomas's infinite-tree automaton is also missing its finite carrier and acceptance-family types

Presentation lines 1528--1547 introduce

\[
 \mathcal A=(Q,\Sigma,q_0,\Delta,\mathcal F),
 \qquad
 \Delta\subseteq Q\times\Sigma\times Q\times Q,
\]

and define successful runs by requiring \(\operatorname{In}(r\restriction\pi)\in\mathcal F\). The actual LaTeX does not state there that (Q) is finite, that \(\Sigma\) is a finite alphabet, that (q_0\in Q\), or that \(\mathcal F\subseteq\mathcal P(Q)\). Those facts are required both to type the acceptance clause and to support the later finite-memory, finite-game, effective complementation, and regular-generator conclusions at lines 1567--1661.

Rabin's earlier (S,M,S_0,F\) definition at lines 1037--1074 is source-specific and uses different data. Thomas is expressly presented at lines 1526--1528 and 1666--1671 as a separate later route, so its tuple cannot inherit Rabin's omitted memberships or finiteness by silence.

Minimum repair: give the complete local type declaration at Definition 6.1 strength, including (Q) finite, \(\Sigma\) finite, (q_0\in Q\), \(\mathcal F\subseteq\mathcal P(Q)\), and the intended nonemptiness conventions. When the chain form is introduced at lines 1553--1564, also quantify its finite positive length (m\) or state the source's exact empty-chain convention.

### 5. Elgot's deletion proof introduces an undefined technical object, "complete states"

Presentation lines 374--381 define (A\)-extendability, strong (A\)-extendability, and the maximal language \(\gamma_A\). Line 380 then says that Lemma 6.1 constructs it "by repeatedly deleting finite complete states which lack a continuation for some input letter." Neither "complete state" nor "finite complete state" is defined, and the sentence does not identify the automaton from whose finite state set deletion occurs. The phrase is not eliminable from the sentence as written: it is the only stated operational description of the construction.

Minimum repair: avoid the unsupported name and say directly what finite object is computed -- for example, start from a finite automaton recognizing \(\gamma\) and iteratively remove every surviving state for which some input letter has no compatible output-and-successor continuation -- with any reachability convention needed by the source construction. This states the owed operation without inventing an undefined state species.

### 6. The false Büchi arithmetic classification is named but not given a standing

Presentation lines 212--223 carefully define the corrected bit-occurrence relation \(\in_2\), the function (V_2\), and the weaker unary-predicate structure. Line 223 then calls the source's ensuing claim the "exactly 2-regular" Theorem 9, but "2-regular" is not defined in this presentation. Quotation marks identify it as source wording; they do not tell the reader whether it names a language class, a relation class under a base-two encoding, or a property of numerical sets. The source note confirms that this is a base-dependent relation classification, but that standing is absent from the reader text.

Minimum repair: either define the source's base-two regularity notion and its encoding before naming it, or replace the unexplained technical label by a direct description such as "the ensuing claimed characterization of relations whose base-two encodings are regular." The correction and rejection of the source theorem can remain exactly as strong as they are now.

## Findings that do not independently block admission

- Presentation line 633 uses (f\) in the equation defining the expansion's sense of "periodic" without first writing "a stream (f\)." The grammatical antecedent makes the intended standing recoverable, but binding the symbol explicitly would improve the exactness expected elsewhere in the presentation.
- Presentation line 767 first writes \(\overline M\) without an explicit notation clause. The same sentence characterizes it as the streams whose every finite prefix extends to a member of (M\), and lines 668 and 740 supply the topology and closedness hypothesis, so this is recoverable rather than an independent blocker. Writing "the closure \(\overline M\)" would remove the avoidable hesitation.
- Presentation lines 145--157 write a nonempty word as (Y_0\cdots Y_h\) and then handle the empty word separately. The cases are mathematically disjoint and coherent, but saying "for a nonempty finite word" in line 145 would make the domain split literal.

## Criteria audit

### Definition before use and notation scope

This criterion fails for the reasons above: the two Thomas automaton tuples omit essential finite/type declarations; Thomas's \(\operatorname{MSO}_0\) atomic basis leaves several predicates undefined; the Elgot unary repair uses an unbound or wrongly inherited (A\); and "complete states" and "2-regular" appear without sufficient local standing. These are local manuscript defects, not unresolved historical ambiguities.

Outside those findings, the presentation is unusually careful. It defines Büchi's special predicates, formula-tuple automata, special output, behavior, and terminal-marker encoding before use; distinguishes Elgot's acceptor, transducer, admissible encodings, extendability notions, and arbitrary-set correction; gives Trakhtenbrot's exact language, syntactic classes, anticipation/memory/operator distinctions, portions, residual operators, homogeneity, solutions, and finite-word notions; and separates Rabin's ordinary and dual automata, frontiered finite trees, marked obligations, well-founded dependency mapping, and source emptiness construction.

### Technical-name necessity, definition, standing, nonredundancy, and use

The major handbook-owned names generally satisfy the supplied rule. In particular, "residual stream operator," the unary-window case, the zero-length dual normalization, "frontiered," the external frontier value, the completed chain automaton, and "order-vector with hit" are accompanied by definitions, object standings, distinctions from neighboring notions, and later proof uses. The two failures are the undefined "complete states" at line 380 and the unexplained "2-regular" label at line 223; Thomas's undefined atomic predicates are additional definition/standing failures rather than merely naming preferences.

### Source ownership, versions, and rights

No rejection is based on the unavailable literal Büchi 1960 journal body or the unreconciled Thomas 1997 final chapter. Presentation lines 8--16 and 924--930 bound Büchi claims to the complete 1959 report precursor and expressly keep journal wording, numbering, examples, proof detail, and pagination open. Lines 231--236 and 512--522 make Elgot's 1961 article controlling, keep the 1959 report as precursor evidence, and assign corrections to the published 1962 errata. Lines 524--534 and 623--631 keep Trakhtenbrot's 1961 announcement and 1962 expansion distinct, including their official title and terminology differences. Lines 973--1026 and 1496--1524 keep Rabin's complete 1969 article and Meyer's later complexity correction in separate roles. Lines 932--969 and 1526--1671 consistently attribute Thomas locators to the May 1996 report and refuse final-chapter or backward-to-Rabin strength.

The permitted notes establish that the local source scans and report PDFs are research evidence without open-content or republication licences. The actual LaTeX does not embed or direct the handbook to reproduce those source files, page images, or long source passages. It paraphrases, gives mathematical displays, and uses brief attributed terminology. I found no reader-facing claim that public access confers redistribution rights. Rights are therefore bounded adequately for this text-only presentation.

### Locator precision and bibliography

The source claims are normally followed by source-specific page, section, or theorem locators. Büchi report pages are not presented as 1960 journal pages. Elgot article, report, and errata locators remain separate. Trakhtenbrot announcement and expansion locators are paired only where the sentence actually combines them. Rabin's theorem and page ranges remain Rabin locators, while McNaughton's theorem is identified as an external dependency invoked by Rabin. Thomas's Section 3.1 and Sections 6.1--6.3 locators are explicitly report locators.

The manually read relevant bibliography entries have the expected distinct identities: `Buchi1959WeakReport`, `Buchi1960`, `BruyereEtAl1994`, `Elgot1959Report`, `Elgot1961`, `Elgot1962Errata`, `Trakhtenbrot1961`, `Trakhtenbrot1962Expanded`, `Rabin1969`, `Meyer1975Complexity`, `McNaughton1966`, `Thomas1996Report`, `Thomas1997`, and `ComonEtAl2007`. I found no bibliography-identity defect that independently changes the verdict. This was a direct entry read, not an automated citation check.

### Proof-status wording and handbook-owned repairs

The presentation consistently distinguishes printed source assertions, source proof architecture, later correction evidence, handbook counterexamples, and handbook-owned repairs. Büchi's repaired finite-witness analysis, Elgot's erratum-controlled finite union and handbook unary case, Trakhtenbrot's graph-degree counterexample and empty-language/empty-set completions, Rabin's zero-length and empty-witness repairs, and Thomas's rejecting-state completion are all expressly owned rather than silently attributed. The narrative also states what proof detail remains in the complete sources. I found no proof-status conflation that independently blocks publication.

### Cross-source nonconflation and reader coherence

The major source packages are not conflated. The manuscript distinguishes Büchi's finite predicates, Elgot's finite-set arithmetic and design calculus, Trakhtenbrot's arbitrary-predicate stream operators, Thomas's modern finite-word construction, Rabin's original infinite-tree architecture, and Thomas's later game-and-regular-basis route. Ordinary Rabin acceptance is kept separate from the dual pair construction, and Rabin's source emptiness proof is not replaced by Thomas's basis theorem.

Reader coherence nevertheless fails at the exact local points in Findings 1--6. In particular, a reader reaches Thomas's finite-word theorem and formula basis without a complete automaton type or letter-track semantics, and later reaches Thomas's tree proof without the finite Muller type on which effectiveness depends.

### Host integration

The insertion at `logic-in-computer-science.tex` line 937 is structurally coherent with the host. The host first states the bounded modern finite-word theorem at lines 836--851, separately states S2S at lines 874--877, and distinguishes finite ranked bottom-up automata from Rabin's infinite-tree objects at lines 879--929. The N-c-014 input then supplies the source presentations without claiming that the modern compound theorem is verbatim in each original. I found no label, section-order, or source-boundary defect in the inspected host interval. Host coherence does not cure the local type omissions inside the included presentation.

## Verdict and register disposition

The explicit precursor boundaries are admissible in principle, and the two still-open literal reconciliations are not grounds for this rejection. The rejection rests on current, directly observed LaTeX: essential finite/type declarations and atomic semantics are missing in the Thomas passages, the Elgot unary repair has an ill-scoped carrier, and two additional technical labels lack local definitions. Until those exact line-level defects are repaired and the integrated LaTeX is freshly reviewed, N-c-014 cannot be admitted as publication-ready even at its otherwise careful bounded source strength.

REGISTER STATUS: OPEN
