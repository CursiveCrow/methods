# Round 2 topic-specialist deliberation

### F1 — accept-fixed
- reply: accept-fixed
- current location: handbook/parts/p09/logic-in-computer-science.tex:157-175
- reasoning: Every internalized GCI \(\neg C\sqcup D\) is now inserted into every existing and newly generated tableau node (lines 158-161), and blocking is applied only after exhaustive local decomposition and GCI insertion to completed labels (lines 165-172). The opening counterexample \(\{\top\sqsubseteq A\},\exists r.\neg A\) now closes: the successor receives the internalized GCI, hence \(A\), and clashes with \(\neg A\). The finite closure/subset-of-closure measure also states the termination argument that the opening method lacked.

### F2 — accept-fixed
- reply: accept-fixed
- current location: handbook/parts/p10/algebraic-and-categorical-logic.tex:27-37; handbook/parts/p14/master-tables.tex:212-214
- reasoning: The theorem now explicitly declares that “arbitrary direct products” include the empty product, identifies that product as the one-element \(\tau\)-algebra, and draws the required conclusion that an HSP-closed class is nonempty. The glossary repeats the same convention. Thus the empty-class counterexample from Round 1 is excluded without adding a redundant nonempty-class premise.

### F3 — accept-fixed
- reply: accept-fixed
- current location: handbook/parts/p09/logic-in-computer-science.tex:365-380; handbook/parts/p09/logic-in-computer-science.tex:390-405
- reasoning: The comprehension defining \(T_P\) now requires \(\theta\) to ground every variable of the selected clause, so every output \(A\theta\) is a ground atom and \(T_P\) is a self-map on the stated interpretations. Stable models are now defined first for finite propositional, already-ground programs, and the text separately requires explicit Herbrand grounding before a nonground program denotes that construction. The representation used by the NP-completeness sentence is therefore fixed.

### F4 — accept-fixed
- reply: accept-fixed
- current location: handbook/parts/p10/algebraic-and-categorical-logic.tex:205-226
- reasoning: The carrier/signature and all six universally quantified Chang equations are now displayed, followed by exact definitions of \(1\), implication, the induced order, and \(\odot\). This is an eliminable equational definition and fixes the algebra class used by the immediately following Chang-completeness and Mundici-equivalence claims.

### F5 — accept-fixed
- reply: accept-fixed
- current location: handbook/parts/p09/logic-in-computer-science.tex:113-124; handbook/parts/p14/master-tables.tex:23-31
- reasoning: Both surfaces now restrict the decidable monadic fragment to relational signatures with unary predicate symbols, explicitly allowed constants, and no positive-arity function symbols; equality is made an explicit convention rather than silently inherited. This removes the function-symbol ambiguity that made the opening complexity statement unsafe, while covering the standard relational monadic decision theorem.

### F6 — still-open
- reply: still-open
- current location: handbook/registry/calculi/mltt-intensional.tex:4-28; handbook/parts/p07/lambda-calculi-and-type-theories.tex:398-432; handbook/parts/p07/lambda-calculi-and-type-theories.tex:450-459
- reasoning: The immediate circularity is repaired: `Ctx-Empty`, `Ctx-Ext`, `Var`, `Conv`, `Universe`, `Russell-El`, `Cumulativity`, and the three universe-closure rules now derive \(\Gamma\vdash\mathcal U_i:\mathcal U_{i+1}\) and the advertised \(\Pi/\Sigma/\operatorname{Id}\) universe judgments. The record nevertheless cannot close because the reader-facing body simultaneously says “The MLTT calculus still owed” and “No such combined calculus is named here” (lines 400-415), then says the matched combined core “is now” supplied (lines 423-432). In addition, the sheet asserts admissible weakening/substitution and an equivalence/congruence closure for judgmental equality in prose (line 4) without displaying the structural and equality-generation rules demanded by that very owed-artifact boundary. The cited normalization theorem expressly covers a narrower one-universe calculus and excludes sums, identity types, and cumulative hierarchies (lines 450-458), so it cannot discharge the matched sheet’s remaining rule/metatheory obligation. Exact correction: either delete/replace the stale owed boundary and display the missing structural/judgmental-equality rules, or retain the boundary and withdraw the claim that the combined MLTT entry is supplied.

### F7 — accept-fixed
- reply: accept-fixed
- current location: handbook/parts/p12/smt-and-exchange-formats.tex:219-265
- reasoning: The abstraction map is now defined on both polarities, \(\mathcal A(p)=L\) and \(\mathcal A(\neg p)=\neg L\), and the checker receives the full signed image \(\mathcal A[\tau]\). The theorem also strengthens clausification from bare equisatisfiability to a two-direction definitional-extension invariant with explicit extension and projection. The success proof uses exactly those two repaired invariants, so the \(\neg(x=x)\) counterexample can no longer be accepted and model reconstruction is justified.

### F8 — still-open
- reply: still-open
- current location: handbook/registry/calculi/omega-arithmetic.tex:1-6; handbook/parts/p07/arithmetic-proof-theory-supplement.tex:326-350
- reasoning: The fix now binds the calculus to linked \(\mathsf{LK}\) with equality, states the arithmetic signature, adds true closed atomic initial sequents, removes primitive induction, and sketches how an induction instance is replaced by numeral derivations followed by \(\omega R\). Two exactness gaps remain. First, “the defining equations for the arithmetic symbols” is still an undisplayed axiom family, so the named base calculus is not eliminably determined at the sheet. Second, \(\omega R\) requires \(A\) to have only its displayed number variable free (sheet line 6), while the claimed embedding covers finitary PA induction instances without restricting or explaining their permitted parameter variables (body lines 332-335). The \(<\varepsilon_0\) theorem then refers to “the assigned notations” without identifying the selected notation system or binding the cited reduction theorem to this exact axiom/parameter presentation. Exact correction: display or link every arithmetic axiom/equation, state and prove the parameter-handling translation for induction, and name the ordinal-notation/reduction presentation; otherwise restore an OPEN boundary.

### F20 — still-open
- reply: still-open
- current location: handbook/parts/p11/philosophy-of-logic.tex:62-101
- reasoning: The revision correctly fixes \(\mathsf{PA}\), \(L_A\), \(L_T\), the coding convention, and the no-truth-induction policy, and it qualifies the names as \(\mathsf{TB}^{-}\), \(\mathsf{CT}^{-}\), \(\mathsf{KF}^{-}\), and \(\mathsf{FS}^{-}\). But only \(\mathsf{TB}^{-}\) is given an exact complete schema. \(\mathsf{CT}^{-}\) invokes unspecified “uniform compositional clauses” and displays only the universal clause; \(\mathsf{KF}^{-}\) names strong-Kleene positive/negative packages while listing selected clauses rather than the complete arithmetized schemes; and \(\mathsf{FS}^{-}\) inherits the still-unstated compositional axiom set. The promised “conservativity comparison below” is only the noncommittal prose “may be conservative” at lines 99-101, so the required later use is also not supplied. Exact correction: display the complete coded axiom/rule schemes and their formula/code side conditions for each variant, then state the exact comparison actually used, or revert these abbreviations to a nontechnical survey/owed-artifact boundary.

### F21 — accept-fixed
- reply: accept-fixed
- current location: handbook/registry/calculi/ordered-superposition.tex:3-7; handbook/parts/p12/first-order-automation.tex:224-246
- reasoning: Equality Factoring now states its MGU, instantiated-premise maximality, absence of a selected literal, and both orientation inequalities \(s\sigma\not\preceq t\sigma\) and \(u\sigma\not\preceq v\sigma\). These are the formerly hidden ordering/eligibility conditions, and they cohere with the sheet’s declared negative-selection policy and the body theorem’s complete-ordering, eligible-inference, redundancy, and fairness hypotheses. No “standard side conditions” placeholder remains.

### F22 — accept-fixed
- reply: accept-fixed
- current location: handbook/parts/p09/logic-in-computer-science.tex:227-238
- reasoning: S1S is now expanded and typed as the monadic second-order theory of \((\mathbb N;S)\), with number variables, set-of-number variables, and successor; S2S is typed analogously over \((\{0,1\}^*;S_0,S_1)\). The text also supplies necessity, standing, nonredundancy, the sole later use, and decision-result citations. The former one-use undefined acronyms are therefore fixed rather than merely expanded typographically.

## Round disposition

- accept-fixed: F1, F2, F3, F4, F5, F7, F21, F22.
- still-open: F6, F8, F20.
- needs-evidence: none.

This round inspected only the eleven agenda records and made no manuscript or control-file edits.
