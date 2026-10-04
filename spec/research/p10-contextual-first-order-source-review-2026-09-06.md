# Contextual first-order calculus: primary-source fidelity review

Date: 2026-09-06, local date.

## Final verdict

**Scoped source-fidelity pass after the owner restored Pitts's quantifier notation and repaired the abstraction header.** All primitive rule schemes of the five requested source figures are represented. The additional explicit existential-witness typing premise is disclosed as a well-sorted-instantiation clarification; the sheet is not described as a literal transcription of the printed fractions.

Reviewed:

- handbook/registry/calculi/contextual-first-order.tex, all 29 lines;
- source attributions, syntax conventions, and related interpretation passages in handbook/parts/p10/first-order-categorical-semantics.tex;
- the corresponding use of those conventions in handbook/annex/p10/first-order-categorical-semantics.tex.

I read the actual primary text and visually inspected the complete source pages containing Figures 1, 2, 3, 5, and 7, using in-memory source-page rendering. No source PDF was modified or re-exported to disk. No other review conclusions were read. Only this note was written; no manuscript edit, software test, build, or manuscript render was performed.

The independent mathematical review of the complete soundness proof is a separate task. This verdict covers source rules, notation, hypotheses, explicit presentation changes, and the scope of the attributions.

## Primary source and exact locators

Andrew M. Pitts, *Categorical Logic*, author manuscript dated **18 May 1995**, University of Cambridge Computer Laboratory report UCAM-CL-TR-367, DOI 10.48456/tr-367.

- [Author-hosted PDF](https://www.cl.cam.ac.uk/~amp12/papers/catl/catl.pdf).
- [Official report record](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-367.html).
- Held copy: tmp/acquisition/src030/cambridge-categorical-logic-author.pdf.
- Existing citation key: Pitts1995Draft.

Printed pages inspected for the core rule comparison:

| Source | Printed page | Relevant content |
| --- | --- | --- |
| Definition 2.1.1, equations (2.2)–(2.5) | 6–7 | Finite contexts with distinct declared names, term formation, typed substitution and context extension |
| Figure 1 | 7 | Equation reflexivity, symmetry, transitivity, and substitutive congruence |
| Metalinguistic conventions; Remark 3.0.2 | 13–14 | Abstraction notation \((x)e\), application, and suppression of a common left-hand context |
| Section 5.1 | 39–40 | Formula and sequent formation; arbitrary equation and sequent axioms; full expansion of Subst |
| Figure 2 | 41 | Contract, Exchange, Id, Cut, variable-context Weaken, and Subst |
| Figure 3 | 48 | Intuitionistic propositional introduction/elimination rules |
| Section 5.5 and Figure 5 | 51–52 | Quantifier notation, four quantifier rules, and implicit eigenvariable conditions |
| Figure 7 and surrounding formation rule | 55 | Equality-formula introduction and elimination |
| Remark 5.6.7 | 59 | Separation of term equations from equality formulas; no automatic reflection |

Source page numbers are those printed in the draft, not offsets into a published book.

## Repairs reported and verified

### Quantifier notation

The initially saved form \(\forall_\sigma(x.\varphi)\), and its existential counterpart, was an added binder notation. It is not the source's printed form.

The actual owner edits, read back at approximately 04:53 UTC on 7 September, now restore
\[
\forall_\sigma(\varphi),\qquad \exists_\sigma(\varphi).
\]
The body explains that \(\varphi\) is a unary formula abstraction, \(\varphi=(x)e\), using Pitts's metalinguistic notation on p. 13. Its application is \(\varphi(M)=e[M/x]\), and \(\varphi(x)\) is interpreted in the extended context.

The four registry quantifier rules, the body interpretation equations, and the annex substitution calculation now use these forms consistently. The closed empty-sort example uses
\(\exists_\sigma((x)(x=_\sigma x))\), with the source's \((x)e\) abstraction notation.

The sheet header initially retained the incompatible sentence that \(\varphi(M)\) means \(\varphi[M/x]\). The final header now correctly says that, for \(\varphi=(x)e\), application means \(e[M/x]\). Its binary \(\psi(M,N)\) convention explicitly refers to simultaneous replacement in the displayed body \(\psi(x,y)\).

### Explicit existential-witness typing

Pitts Figure 5 prints \(\exists\)-Intr with the single sequent premise \(\Phi\vdash\varphi(M)\); unlike the displayed universal elimination rule, it does not separately print \(M:\sigma\). The handbook sheet retains the explicit premise \(M:\sigma\,[\Gamma]\).

That premise is appropriate for a typed instantiation, including a vacuous abstraction whose body does not use its argument. Well-formedness of the resulting formula alone should not be used to infer the sort of an erased witness. The revised body explicitly notes the omitted printed premise and states the well-sorted-instantiation convention being made explicit. The sheet's side condition likewise discloses it. This is a documented clarification, not a claim of identical printed fractions.

### Other conventions now explicit

The final body fixes a countably infinite variable-name supply, with sorts supplied by declarations, matching Section 2.1. It calls the connective constructors propositional, which matches the intuitionistic rule package and the Heyting semantics.

## Complete rule coverage

### Figure 1: equational judgments

Registry lines 5–8 correspond to source equations (2.6)–(2.9). Renaming the source metavariables \(M',M''\) to \(N,K\) in symmetry/transitivity changes no rule.

Eq-Subst has exactly the source context split:
\[
M=M':\sigma\,[\Gamma],\quad
N=N':\tau\,[\Gamma,x:\sigma,\Delta]
\]
with conclusion
\[
N[M/x]=N'[M'/x]:\tau\,[\Gamma,\Delta].
\]
The first equation is in the retained prefix; the remaining declarations are a disjoint suffix. The explicit disjointness conditions agree with Definition 2.1.1's well-formed-context convention.

Eq-Ax at registry line 3 makes the source's “provable from the theory's axioms” clause explicit. It does not add an independent non-source axiom scheme. Typed term formation is supplied in body prose, and term-substitution well-formedness is treated separately, as in source (2.2)–(2.5).

### Figure 2: structural sequents

Registry lines 9–14 contain all six schemes. The Id hypothesis list, the two distinct Cut antecedent lists, adjacent hypothesis exchange, and contraction agree with the figure.

Weaken extends the **variable context**. It is not a rule deleting declarations and is not being mistaken for antecedent weakening. Source p. 40 explicitly distinguishes these two notions; the annex correctly explains that adding hypotheses follows from Id and Cut.

The sequent Subst rule matches the source's fully expanded form on p. 40:
\[
\Phi(M)\vdash\psi(M')\,[\Gamma,\Delta].
\]
Its asymmetric use of the provably equal terms in antecedent and conclusion is preserved.

The restored common contexts follow Remark 3.0.2: only a common left-hand prefix was suppressed in the printed figures. This convention does not license erasure of an unused sort declaration.

### Figure 3: intuitionistic propositional rules

Registry lines 15–23 contain all nine schemes: false elimination; conjunction introduction and two eliminations; two disjunction introductions and elimination; implication introduction and elimination.

All hypothesis-list concatenations agree with the source. In particular, disjunction elimination retains the two branch hypothesis lists and the separate list proving the disjunction. Implication introduction discharges the displayed formula, and elimination retains both premise lists.

The source operators false, \(\&\), \(\vee\), and \(\Rightarrow\) are preserved. Negation and true are abbreviations, not added primitive connectives. No excluded-middle, double-negation-elimination, or other classical inference has been added.

### Figure 5: quantifier rules

Registry lines 24–27 contain all four schemes with the restored unary-abstraction notation.

Universal introduction retains the common context \(\Gamma\), appends fresh \(x:\sigma\) in its premise, and requires the hypotheses to be well formed without \(x\). Universal elimination keeps its witness term in \(\Gamma\), as the source's displayed typing premise requires.

Existential introduction includes the disclosed explicit witness-typing clarification. Existential elimination retains the two source hypothesis lists and excludes the eigenvariable from both undischarged lists and the conclusion. These are exactly the conditions made explicit in source p. 51, following the well-formed-sequent convention.

### Figure 7: equality formulas

Registry lines 28–29 preserve both schemes. Equality introduction permits an arbitrary finite hypothesis list. Elimination has the equality-formula premise and the separate premise \(\Phi'\vdash\psi(x,x)\) in the extended context; its conclusion is \(\Phi,\Phi'\vdash\psi(M,N)\).

The side conditions correctly type \(M,N\), retain the parameter context, require two fresh distinct argument variables for the binary abstraction, and prevent the discharged variable from appearing in the undischarged \(\Phi'\). These conditions are the expanded well-formedness requirements of the source rule.

Figures 4, 6, and 8 are accurately identified as the equivalent adjoint presentations. They are not silently added as further primitive inference rules.

## Axioms, equality levels, and attribution limits

Pitts allows theory axioms to be equations-in-context and sequents in Section 5.1, p. 40. The sheet's Eq-Ax and Seq-Ax, the arbitrary set of well-formed axioms in the body, and finite derivation trees conform to this scope. The soundness attribution does not impose a finite-theory hypothesis.

The body explicitly distinguishes \(M=N:\sigma\,[\Gamma]\), interpreted as equality of base arrows, from \((M=_\sigma N)\), interpreted as a fibre predicate. This matches Remark 5.6.7, p. 59. The sheet has no reflection rule from a proved formula to a term equation. The degenerate-doctrine example in the annex matches the source's reason that such reflection is not automatic.

The citations to Lemma 5.2.6 and Theorems 5.3.2/5.4.2 correctly identify substitution, structural soundness, and propositional soundness within the wider Sections 5.2–5.6 treatment. The handbook supplies its quantifier and equality checks directly; it does not mislabel Theorem 5.4.2 alone as full first-order soundness.

The leading-terminal context products follow the source's explicit recursive convention on p. 8. The many-sorted Tarskian comparison is appropriately attributed to Examples 5.5.3 and 5.6.3. The text retains empty sorts for its contextual semantics and separately states the nonempty-sort bridge. It does not silently add a context-erasing rule or claim completeness for the handbook's separate LJ presentation.
