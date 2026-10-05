## SRC-04968-05042

Substructure definition, domain inclusion (clause 1): the capture wrote the domains of the two structures as \(\abs{\mathcal N}\subseteq\abs{\Meta}\), using vertical bars that the handbook registers for cardinality. The corrected text reads \(\dom\mathcal N\subseteq\dom\Meta\). Justification: the registered domain operator \dom (handbook/handbook.sty; symbol registry in handbook/parts/p01/symbol-registry.tex, which fixes \(\dom\mathcal M\) as the notation for structure domains and bars for cardinality). The mathematics is unchanged.

Substructure definition, closure clause (clause 3): \(\abs{\mathcal N}\) is closed under every function becomes \(\dom\mathcal N\) is closed under every function, by the same registered notation; the statement is unchanged.

Substructure definition, relation clause (clause 4): the restriction of each relation to \(\abs{\mathcal N}\) becomes restriction to \(\dom\mathcal N\), by the same registered notation; the statement is unchanged.

Elementary substructure definition: the parameters \(a_1,\ldots,a_n\in\abs{\mathcal N}\) become \(a_1,\ldots,a_n\in\dom\mathcal N\), by the same registered notation; the statement is unchanged.

Tarski--Vaught test (thm:tarski-vaught-fol), parameter tuple: \(\bar a\in\abs{\mathcal N}^{n}\) becomes \(\bar a\in(\dom\mathcal N)^{n}\); the parentheses make explicit that the power applies to the domain, removing the ambiguity of a power applied to bars. Justification as above; the statement is unchanged.

Tarski--Vaught test, witness clause: the witness \(b\in\abs{\mathcal N}\) becomes \(b\in\dom\mathcal N\), by the same registered notation; the statement is unchanged.

Proof of the Tarski--Vaught test, forward direction: the witness belongs to \(\abs{\mathcal N}\) becomes belongs to \(\dom\mathcal N\), by the same registered notation; the argument is unchanged.

Proof of the Tarski--Vaught test, universal case: every instance at an element of \(\abs{\mathcal N}\) becomes an element of \(\dom\mathcal N\), by the same registered notation; the argument is unchanged.

Proof of the Tarski--Vaught test, universal case, failure direction: the witness condition supplies a witness in \(\abs{\mathcal N}\) becomes a witness in \(\dom\mathcal N\), by the same registered notation; the argument is unchanged.
