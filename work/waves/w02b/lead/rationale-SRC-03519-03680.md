## SRC-03519-03680

The universal-quantifier clause of the satisfaction definition wrote the range of the witness as \(a\in\abs{\Meta}\), using vertical bars for the domain of the structure, while the corrected clause writes \(a\in\dom\Meta\). The change is notational only: the symbol registry (handbook/parts/p01/symbol-registry.tex, the paragraph on domain notation) records that bars around a structure denote its domain, so \(\lvert\mathcal M\rvert=\dom\mathcal M\), and fixes \(\dom\mathcal M\) as the editorial form for structure domains, leaving vertical bars to cardinality; the clause still quantifies over every element of the same domain.

The existential-quantifier clause of the same definition likewise wrote \(a\in\abs{\Meta}\) and now writes \(a\in\dom\Meta\), by the same registry rule (handbook/parts/p01/symbol-registry.tex, domain notation, \(\lvert\mathcal M\rvert=\dom\mathcal M\)); the witness still ranges over the same domain, so the satisfaction relation is unchanged.
