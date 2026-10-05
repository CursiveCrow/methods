## SRC-01946-02186

Tseitin forward link (work/waves/w02/patches/w02-p02-010.json, index 0). After the proof of the normal-form theorem, the capture pointed to the Tseitin section and its main theorem but gave no route to the construction, the size result, or either proof. The sentence now names Definition~\ref{def:p02-tseitin-construction}, the equisatisfiability and projection statement Theorem~\ref{thm:p02-tseitin} with its proof Annex~\ref{annex:p2.prop.tseitin}, and the size bound Theorem~\ref{thm:p02-tseitin-size} with its proof Annex~\ref{annex:p2.prop.tseitin-size}. All five targets are defined on the live route: handbook/parts/p02/tseitin-transformation.tex (lines 28, 94, 125), input by handbook/parts/p02.tex, and handbook/annex/p02/tseitin-transformation.tex (lines 2, 110), input by handbook/annex/p02.tex. This only adds cross-references. No mathematics changes.

Negation-normal-form label (work/waves/w02/patches/w02-p02-045.json, index 3). The numbered theorem "Negation normal form" had no label, so nothing could cite it. The label thm:p02-w02-p02-045-negation-normal-form now sits on the line after \begin{theorem}. No text changes.

Functional-basis label (work/waves/w02/patches/w02-p02-045.json, index 4). The numbered theorem "A functionally complete basis" had no label. The label thm:p02-w02-p02-045-functional-basis now sits on the line after \begin{theorem}. No text changes.

CNF half of thm:prop-normal-forms (work/waves/w02/patches/w02-p02-045.json, index 5). Requirement ED26-REQ-R-011 requires that the CNF proof be a complete induction. The capture, which matches source/formal-logic-reference.tex in this interval, built the CNF by listing falsifying valuations, dual to the truth table. That argument is valid, but it is not an induction on formulas, so it does not meet the requirement. The new CNF half works as follows:
- Two facts are proved first. (a) A union of two clauses is satisfied exactly when one of them is. (b) The pairwise-union product of two clause sets is satisfied exactly when one of the factors is.
- Structural recursion, which is well defined by unique readability (\cref{thm:prop-unique-readability}), gives each formula a pair of finite clause sets K+ and K-. The recursion covers the grammar p_n, \bottom, \neg, \land, \lor, \to of the Propositional formula definition.
- A simultaneous structural induction shows that K+(phi) is satisfied exactly by the models of phi and K-(phi) exactly by its countermodels, and that only variables of phi occur in either set.
- The output C_phi is \topv when K+(phi) is empty. Otherwise it is N_1 over the clauses of K+(phi), listed by the injective weight sum of 2^code(L). This output meets the CNF definition exactly, and \cref{lem:prop-clause-satisfaction}(2) shows that it is equivalent to phi.
- The degenerate inputs are treated explicitly: \topv (which is \neg\bottom by the Defined connectives definition), \bottom, formulas without variables, and valid and unsatisfiable formulas that have variables.
- A worked example follows the proof.

I checked the recursion equations against the truth clauses for each connective, and I recomputed the degenerate cases and the worked example: codes 2, 5 and 6, weights 68 and 96, result ((p_1\lor p_3)\land(\neg p_2\lor p_3)). The theorem statement and the DNF half are unchanged.
