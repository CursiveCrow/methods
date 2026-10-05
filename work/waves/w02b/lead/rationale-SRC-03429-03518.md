## SRC-03429-03518

Domain clause of the first-order structure definition (request w02-p01-026 #8). The capture wrote the domain of a structure as \(\abs{\Meta}\), which gives the vertical bars a second meaning beside their registered role of cardinality. It now reads "a nonempty set \(\dom\Meta\), called its domain". The justification is the symbol registry (handbook/parts/p01/symbol-registry.tex, the \(\dom\mathcal M\) entry and the note that new text writes structure domains only as \(\dom\mathcal M\)), with \dom defined in handbook/handbook.sty. This is a change of notation only. The mathematics is the same, since the registry identifies \(\lvert\mathcal M\rvert=\dom\mathcal M\).

Function-symbol clause (request #9). The interpretation type \(f^{\Meta}:\abs{\Meta}^{n}\to\abs{\Meta}\) now reads \(f^{\Meta}:(\dom\Meta)^{n}\to\dom\Meta\). The parentheses mark the Cartesian power as applying to the domain. The justification is the same registry convention, and the meaning does not change.

Relation-symbol clause (request #10). \(R^{\Meta}\subseteq\abs{\Meta}^{n}\) now reads \(R^{\Meta}\subseteq(\dom\Meta)^{n}\). The justification is the same registry convention, and the meaning does not change.

Constants and equality (requests #11 and #12). The constant value \(c^{\Meta}\in\abs{\Meta}\) and "actual identity on \(\abs{\Meta}\)" now use \(\dom\Meta\). The justification is the same registry convention, and the meaning does not change.

Variable assignments (request #13). In the assignment definition, \(s:\Var\to\abs{\Meta}\) and \(a\in\abs{\Meta}\) now read \(s:\Var\to\dom\Meta\) and \(a\in\dom\Meta\). The justification is the same registry convention, and the meaning does not change.
