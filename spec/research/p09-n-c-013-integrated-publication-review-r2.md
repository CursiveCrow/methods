REJECT

# Blind integrated publication and terminology review: N-c-013, Round 2

## Scope and method

This verdict concerns the current actual source text in:

- handbook/parts/p09/presentations/n-c-013.tex, lines 1--1300; and
- handbook/parts/p09/logic-in-computer-science.tex, lines 723--920, including the N-c-013 input at line 910.

Both ranges were read from line 1 (or the specified host start) through the specified endpoint. No prior integrated N-c-013 review or admission report was opened or used; no manuscript PDF, page image, or other rendering was inspected; and no build, test, checker, repository script, hash, or automated validation was run. The five permitted source records and the compact N-c-013 ledger were used only to distinguish source wording from handbook wording and to check access/version and locator boundaries. The verdict is based on the LaTeX text itself.

## Publication-blocking findings

### P1. The host calls an under-specified outline a “complete construction”

**Exact locations:** n-c-013.tex:97--160, especially :102--130, :134--145, and :157--160; host logic-in-computer-science.tex:746--756, especially :750--756.

The presentation gives the local-state set and two consistency schemata, then says in prose that the eventuality component “collects” and “carries” obligations. It never gives a typed transition relation for that component, never gives the product transition, and never formally relates a product transition to the closure-type letter being read. The subsequent projection introduces a new letter \(b\) in

\[
 b\longmapsto b\cap\mathit{Prop}
\]

without first declaring the intermediate alphabet or binding \(b\). Consequently the printed data \(N_M,N_{M0},F_M\) do not determine an automaton that a reader can construct. Nevertheless, the host theorem says that “The complete construction, conversion, and proof boundary” are in this presentation.

This is not merely omitted proof detail: it is missing defining data coupled to a false host-level completeness claim. Either supply the intermediate alphabet, both component transitions, the product transition, and the projection with all variables typed, or weaken host line 755 to say that the presentation gives the state-counting outline and source/proof boundary rather than the complete construction.

### P2. The closure-state definition has no admissible-variable scope

**Exact locations:** n-c-013.tex:98--130, especially :102--119 and the definition of \(N_L\) at :121--130.

The displayed clauses leave \(\psi\) and \(\xi\) unbound and do not say that the conjunction, next, or until clause is imposed only when the displayed compound formula belongs to \(cl(\varphi)\). A literal universal reading is wrong: it would impose

\[
 \xi\land\psi\in u\Longleftrightarrow \xi\in u\land\psi\in u
\]

even when \(\xi\land\psi\notin cl(\varphi)\). With no universal reading, “satisfies the displayed local consistency conditions” in the definition of \(N_L\) has no exact eliminable content. The same defect affects the consecutive-state clauses for \(X\psi\) and \(\xi U\psi\).

The repair is local: quantify the Boolean clauses over the relevant formulas of the closure and the temporal clauses over the relevant \(X\)- and \(U\)-formulas of the closure. Until that is done, \(N_L\), \(N_\varphi\), and therefore the product state set invoked by the host theorem are not exactly defined.

### P3. The Markov-chain definition leaves its carrier and normalization scope incomplete

**Exact locations:** n-c-013.tex:270--295, especially :271--287.

The new labelled Markov-chain tuple does not state that \(W\) is finite or otherwise give a summability condition, and the normalization equation

\[
 \sum_{v\in W}P(u,v)=1
\]

leaves \(u\) free instead of requiring the equality for every \(u\in W\). The same paragraph uses \(\Delta\) first as the Borel field in \((\Omega,\Delta,\mu)\), then as though \(\Delta(w_0,\ldots,w_n)\) were a cylinder-set constructor, and then as the formula-event constructor \(\Delta(\varphi)\), without defining either constructor or stating the admissible prefixes. The intended measure-one semantics is clear informally, but the displayed object is not an exact definition at the point on which the later probabilistic terminology depends.

State the carrier assumption and the missing universal quantifier, and give the cylinder and formula events distinct typed abbreviations (or explicitly define the two overloaded uses). This preserves the source notation while satisfying definition-before-use and free-variable scope.

### P4. The McNaughton paragraph promotes two unavailable source meanings to technical predicates

**Exact locations:** n-c-013.tex:837--845.

The text exactly defines an \(\omega\)-event as a set of infinite sequences, but it then uses “regular \(\omega\)-event” and “finite-state” as the two predicates in an if-and-only-if theorem effect even while acknowledging that the report supplies none of the article's alphabet, state-graph data, acceptance clause, constructions, or exact theorem wording. Calling the expressions “historical terms” supplies standing, but it does not supply an eliminable definition, an axiom, or the required nonredundancy distinction. Under the governing technical-name rule, the inaccessible meanings must remain an owed artifact rather than become predicates in a handbook-level mathematical sentence.

The paragraph may still report the historical evidence metalinguistically: say that the Project MAC report uses those two unanalyzed phrases and reports an equivalence between them, then state explicitly that their definitions and distinction remain open until the article body is read. Do not italicize or otherwise introduce either phrase as a locally usable technical term before that source visit.

### P5. The Safra correctness argument uses an unfixed input word

**Exact locations:** n-c-013.tex:1033--1061.

The proof begins “For \(i\le j\), write \(\alpha[i,j)\)” and then forms run segments over that word, but it never fixes \(\alpha\in\Sigma^\omega\) or says that the accepting determinized run under discussion is the run on \(\alpha\). The completeness direction likewise says only “let \(\rho\) be an accepting original run,” not an accepting \(\mathcal A\)-run on the same \(\alpha\). The generic occurrence of \(\alpha\) inside the earlier run definition at lines 885--887 does not bind the variable throughout this later proof paragraph.

Fix an input word and its target run before defining the factor notation, and bind the original run in the converse to that same word. This is required to make the two language-inclusion directions statements about one typed input rather than arguments with a free metavariable.

### P6. Thomas's infinity-set notation depends on an undefined quantifier glyph

**Exact locations:** n-c-013.tex:1125--1158, especially :1125--1129.

Thomas's source notation is printed as

\[
 \operatorname{In}(r)=\{q\in Q:\exists^\infty i\;r(i)=q\},
\]

but \(\exists^\infty\) is not defined. Earlier, this same file carefully defines Büchi's different source glyph \(\exists^\omega\) by an explicit \(\forall x\exists t>x\) expansion at lines 493--498. The new glyph is then used through \(\operatorname{In}(r)\) in all four acceptance clauses. Source-specific notation may be retained, but it needs the same exact eliminable expansion, for example

\[
 q\in\operatorname{In}(r)\Longleftrightarrow
 \forall m\in\mathbb N\;\exists i\ge m\;(r(i)=q).
\]

Without it, definition-before-use and the local technical-name rule are not met.

## Nonblocking editorial finding

### E1. A displayed sentence is closed before its dependent “where” clause

**Exact location:** n-c-013.tex:499--514, especially :507--508.

The display defining the \(\Sigma_1^\omega\) form ends with a full stop, after which line 508 begins the dependent clause with lowercase “where.” Remove the display-final period or capitalize and recast the following sentence. This does not affect the mathematics but is a publication-level copy defect.

## Audited areas with no further finding

- **Source and version boundaries:** Vardi--Wolper is consistently limited to the dated author preprint rather than a proceedings facsimile (n-c-013.tex:8--15); Büchi's original publication, later printing, reprint DOI boundary, and rights warning are separated (:424--436); McNaughton's article body is expressly unread and the game memo is kept separate (:829--853); Safra 1988 abstract-level claims are separated from the 1995-generated author-hosted expansion (:855--870, :1099--1106); and Thomas is consistently cited at May 1996 report-precursor strength rather than as the unreconciled 1997 chapter (:1108--1166, :1296--1300).

- **Theorem ownership:** the Vardi--Wolper upper bound and Sistla--Clarke lower bound are not conflated (:201--219); the worked product is labelled handbook-owned (:221--241); Büchi's modern automaton equivalence is marked as a handbook corollary (:516--548, :687--697); Safra's ordering, specificity, allocation, dead-state, and counting repairs are individually owned by the handbook (:904--1014, :1063--1080); and Thomas's mark lifetime, empty state, name discipline, and accepting-cycle repair are likewise owned (:1191--1272, :1274--1294). The host theorem preserves those ownership boundaries at logic-in-computer-science.tex:746--756 and :830--846, apart from P1's overclaim.

- **Technical names that do meet the local rule:** semi-determinism (n-c-013.tex:42--60), the three \(ETL\) languages (:249--268), the temporal fragments and both limit-equivalence relations (:311--381), \(SC\) and the source formula classes (:438--514), multiperiodicity (:550--588), \(SC_{\mathrm{fin}}\) and \(SC_{\mathrm{per}}\) (:730--780), Safra-specificity and the rejecting sink (:904--1014), determinism in the limit (:1082--1097), and Thomas's Safra-tree state and absorbing empty state (:1191--1272) each have adequate local standing, distinction, and later use. Büchi's unresolved phrase “arithmetically equivalent” is correctly quarantined as an unused source phrase rather than defined by guesswork (:782--800).

- **Host integration:** the single-start Rabin tuple, LTL translation theorem, product convention, SCC/cycle criterion, complexity ownership, and \(SC\) corollary are coherently placed before the input (logic-in-computer-science.tex:723--846), and the N-c-013 input is ordered between N-c-012 and N-c-014 at :909--912. No additional host-integration defect was found beyond P1.

- **Citations and locators:** the cited internal preprint pages, Büchi printed pages, Project MAC page, Safra expanded-manuscript pages, and Thomas report sections agree with the permitted source records; no locator is silently transferred from a precursor/expansion to the registered final publication. No additional citation or page-locator finding was found in the audited ranges.

The verdict remains **REJECT** until P1--P6 are repaired in the actual LaTeX. E1 may be repaired in the same pass but is not independently verdict-determinative.
