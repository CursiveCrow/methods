## SRC-03729-03907

In the proof of the explicit-definition theorem (clause 1), the capture wrote the set of defining tuples as \(R^*\subseteq\abs{\Meta}^n\), using vertical bars for the structure's domain. The corrected text reads \(R^*\subseteq(\dom\Meta)^n\). Justification: notation only, no change to the mathematics; structure domains are written with the registered domain operator \dom (handbook/handbook.sty, "structure domains: \dom\mathcal{M}"), so vertical bars keep their single registered role of cardinality.

In the same proof, the quantification over tuples read \((a_1,\ldots,a_n)\in\abs{\Meta}^n\). The corrected text reads \((a_1,\ldots,a_n)\in(\dom\Meta)^n\). Justification: the same notational alignment with the registered domain operator \dom, keeping the two occurrences in the proof consistent; the claim is unchanged.
