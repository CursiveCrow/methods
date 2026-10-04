# P6 constructible-hierarchy foundations: independent source and definition review

Reviewer: `/root/constructible_foundation_source_review`.
Review started 8 September 2026, 07:49:18 UTC. Maximum return: 08:34:18 UTC.
Source/definition assessment completed and read back at 07:57:17 UTC.

## Retrieved Content

### Source 1: `handbook/parts/p06/constructible-hierarchy-foundations.tex`, lines 4-10

```tex
The following derivation works in the theory \(\mathsf{ZF}\) fixed in
\cref{sec:zf-zfc-01}.  Its inputs are the definitions of transitive set,
ordinal, function, and satisfaction in
\cref{def:transitive-set,def:ordinal-cardinal,sec:zf-zfc-02,sec:fol-semantics-02}.
It supplies the recursion and definability details needed for
\cref{thm:p06-constructible-class}.  Class notation throughout abbreviates
formulas with set parameters.  The arguments below do not use Choice.
```

### Source 2: `handbook/restoration/inherited-00603-00647.tex`, lines 10-19

```tex
\begin{definition}[Ordinal and cardinal]
\label{def:ordinal-cardinal}
An \emph{ordinal} is a transitive set \(\alpha\) such that \(\in\) strictly
well-orders \(\alpha\).  For ordinals \(\alpha,\beta\), write
\(\alpha<\beta\) iff \(\alpha\in\beta\).  A \emph{cardinal} is an ordinal
\(\kappa\) for which no smaller ordinal is bijective with \(\kappa\).  Thus a
cardinal is already the least ordinal of its bijection type; the phrase
``initial ordinal'' will not be used as a second term.  A cardinal is
\emph{infinite} iff it is not bijective with any \(n\in\N\).
\end{definition}
```

### Source 3: `handbook/annex/p06/constructible-hierarchy-foundations.tex`, lines 49-59

```tex
Conversely, suppose that predicate holds of \(x\).  Membership on
\(x\) is irreflexive by Foundation and is linear by the last
conjunct.  If \(u\in v\in w\) with \(u,v,w\in x\), transitivity
of \(w\), supplied by the second conjunct, gives \(u\in w\).
Finally let \(B\subseteq x\) be nonempty.  Foundation applied to
the set \(B\) supplies \(b\in B\) with no member in \(B\).
For every distinct \(a\in B\), linearity gives \(a\in b\) or
\(b\in a\); the first is excluded.  Thus \(b\) is the least
member of \(B\).  Membership strictly well-orders \(x\), and
the first conjunct says that \(x\) is transitive.  This is exactly
the original definition of ordinal.
```

### Source 4: `handbook/restoration/inherited-10353-10451.tex`, lines 66-72

```tex
\begin{proof}
If the conclusion fails at some ordinal \(\delta\), separation applied to
\(\delta+1\) produces the nonempty set
\(\set{\beta\in\delta+1:\neg\varphi(\beta,\bar p)}\).  The ordinal
well-order supplies its least member \(\alpha\).  Every \(\beta<\alpha\) satisfies \(\varphi\), so
the displayed hypothesis gives \(\varphi(\alpha,\bar p)\), a contradiction.
\end{proof}
```

### Source 5: `handbook/annex/p06/constructible-hierarchy-foundations.tex`, lines 163-185

```tex
Let \(\lambda\) be nonzero and limit.  For each \(\beta\in\lambda\),
the induction hypothesis and the compatibility argument give
exactly one \(g\) satisfying \(\operatorname{App}_G(\beta,g)\).
The Replacement instance with domain \(\lambda\) and defining
formula \(\operatorname{App}_G(\beta,g)\) therefore forms the set
\[
 H=\{g:\exists\beta\in\lambda\;
                    \operatorname{App}_G(\beta,g)\}.
\]
Union supplies \(f=\bigcup H\).  Compatibility ensures that
two pairs in \(f\) with the same first coordinate have the same
second coordinate.  Its domain is
\(\bigcup_{\beta<\lambda}\beta=\lambda\), using
\cref{thm:p06-ordinal-foundation-facts}.
For \(\xi\in\lambda\), the ordinal \(\xi+1\) also belongs to
\(\lambda\).  The member \(f_{\xi+1}\) of \(H\) contains its
value at \(\xi\).  This graph is included in the union \(f\),
which is already a function, so
\(f\mathbin{\upharpoonright}(\xi+1)=f_{\xi+1}\); hence its recursion equation at
\(\xi\) is the equation for \(f\).  This proves existence at
\(\lambda\) and completes the induction.  No collection over
all ordinals was formed: the Replacement domain was the set
\(\lambda\) at that stage.
```

### Source 6: `handbook/restoration/inherited-10675-10769.tex`, lines 7-15

```tex
\begin{definition}[Definable subsets]
\label{def:p06-def-empty-base}
Set
\[
  \operatorname{Def}(\varnothing)\defeq\{\varnothing\}.
\]
For a nonempty set \(A\), let \(\operatorname{Def}(A)\) be the collection of subsets of
\(A\) definable over the structure \((A,\in)\) by a first-order formula with
parameters from \(A\):
```

### Source 7: `handbook/annex/p06/constructible-hierarchy-foundations.tex`, lines 228-238

```tex
For a fixed nonempty \(A\), Separation on \(\mathcal{P}(\omega\times A)\)
with the function and domain conditions gives \(S_A\).
Choose one \(a_0\in A\).  The graph
\(\{\langle i,a_0\rangle:i\in\omega\}\), formed by Separation
on \(\omega\times A\), is a member of \(S_A\).
This proves nonemptiness without a choice function on a family of
sets.  An update \(s[i\mapsto a]\) is the union of the singleton
\(\{\langle i,a\rangle\}\) with the subset of \(s\) whose first
coordinate is different from \(i\).  Separation, Pairing, and
Union give this set, and its domain and range show that it lies
in \(S_A\).
```

### Source 8: `handbook/annex/p06/constructible-hierarchy-foundations.tex`, lines 336-362

```tex
For nonempty \(A\), Separation on \(\mathcal{P}(A)\), using the formula
in the theorem statement, now gives a unique set of subsets.
Any witnessing code unfolds to a finite formula.  Only finitely
many of its variables other than \(v_0\) are free, so only the
corresponding finite tuple of values of \(s\) is relevant, by
the formula-coincidence lemma \cref{lem:fol-coincidence}.
Its subset is therefore definable with finitely many parameters
in the original sense.
Conversely, take an original defining formula and its finite
parameter tuple.  If its distinguished variable is not \(v_0\),
interchange its variable index with zero throughout the formula,
including bound occurrences, and move the parameter assignments
accordingly.  This bijective renaming preserves the truth clauses:
atomic indices are renamed together, Boolean clauses commute with
renaming, and updating a renamed bound index gives exactly the
renamed updated assignment in each quantifier clause.
Thus the distinguished variable may be taken to be \(v_0\).
Extend the finite assignments to \(s\in S_A\) by assigning
the fixed \(a_0\) to all other indices.  Separation on
\(\omega\times A\) constructs its graph.  A code for the formula
then witnesses precisely the required subset in the display.
The two definitions of \(\operatorname{Def}(A)\) agree.

For \(A=\varnothing\), Pairing forms \(\{\varnothing\}\).
Combining this branch with the nonempty branch gives one
formula defining a unique set value for every \(A\).
The empty branch does not call the satisfaction construction.
```

### Source 9: `handbook/annex/p06/constructible-hierarchy-foundations.tex`, lines 377-389

```tex
For \(\exists u\in v\;\psi\), let \(b\in A\) be the value of
\(v\).  The quantified variables \(u,v\) are distinct, so this
value remains fixed when \(u\) is updated.  The structural truth
clause asks for an \(a\in A\) such that \(a\in b\) and \(\psi\)
holds under that update.  Transitivity gives \(b\subseteq A\).
The possible witnesses are therefore exactly the ambient members
of \(b\).  The induction hypothesis applies at each such update,
and the existential assertions agree.  For
\(\forall u\in v\;\psi\), the structural clause imposes \(\psi\)
on those \(a\in A\) that belong to \(b\), and no condition on
the other members of \(A\).  Again these relevant values are
exactly the members of \(b\), and the induction hypothesis gives
the ambient bounded universal assertion.
```

### Source 10: `handbook/annex/p06/constructible-hierarchy-foundations.tex`, lines 510-522

```tex
If \(\beta>0\), then \(0\in\beta\), so the induction
identity implies \(0\in A\).  Thus \(A\) is nonempty, and
its already established transitivity permits
\cref{thm:p06-bounded-transitive-absoluteness}.  The subset
defined over \(A\) by the parameter-free formula
\(\operatorname{Ord}_{\mathrm b}(v_0)\) is exactly
\[
 \{x\in A:(A,\in)\entails\operatorname{Ord}_{\mathrm b}(x)\}
   =\{x\in A:x\text{ is an ordinal}\}=\beta.
\]
It follows from the actual definition of \(\operatorname{Def}\)
that \(\beta\in\operatorname{Def}(A)=L_{\beta+1}\).
The preceding empty case supplies the same conclusion at zero.
```

### Source 11: `handbook/parts/p06/constructible-hierarchy-foundations.tex`, lines 218-220

```tex
These results establish the hierarchy and its height.  The axiom-by-axiom
relativization theorem for \(L\), its definable well-order, condensation,
and GCH require their separate proofs.
```

## Supplementary Notes

### Assessment of the frozen derivation

**PASS: source and definition fidelity for all eight new theorem/proof pairs.**
No mathematical premise, definition, source-attribution, or proof-standing
defect was identified in the frozen body and annex below. This is an independent
review of the supplied ZF derivation and its actual manuscript prerequisites.
It does not certify an unread Jech presentation. The author intake explicitly
identifies the argument as independently supplied and states that no Jech body
was available or read; the target body makes no contrary attribution.

The research skill was read completely. Its primary-source instruction guided
the direct prerequisite reading. This reviewer was the assigned background
reviewer; no further subagent was spawned. No other current reviewer report was
read. No manuscript file, canonical record, admission record, or tooling was
changed; no test, manuscript build, or manuscript render was run.

### Frozen targets and full read extents

All listed files were read completely, including ordinary proof prose, formulas,
examples and qualifications. The two new target files were read as actual LaTeX;
the proof reading was not limited to theorem/status lines.

| File | Full extent read | SHA256 |
| --- | --- | --- |
| `handbook/parts/p06/constructible-hierarchy-foundations.tex` | 1-220 | `64E22FE49017819108160AF5C291E8507A94D4751C2D452EF2DBA8DE6F0E1B95` |
| `handbook/annex/p06/constructible-hierarchy-foundations.tex` | 1-587 | `4D13EF83F571C7D61BCBD25B0AAF07EA1A0EA4840D3152ED738FB2D7CFFBA43C` |
| `handbook/restoration/inherited-00603-00647.tex` | 1-45 | `B76C0E5AEE32C23E036F59F780A99690C9788636444A4456B8E6762A3307B795` |
| `handbook/restoration/inherited-10089-10271.tex` | 1-183 | `6E8EB080C5FC4C5D359798C48AFFB7692ACE514F702DABF643003AE57FFF4B29` |
| `handbook/restoration/inherited-10272-10352.tex` | 1-81 | `0FC1DB84F232FDC88F0860164281D9F0F1182565B6D510F376DE90E0F016A0F3` |
| `handbook/restoration/inherited-10353-10451.tex` | 1-99 | `6B0A7785FADE6927950AD97D90EC2B24FC90A335B7673AC0A3B75F6E6C791008` |
| `handbook/restoration/inherited-10452-10520.tex` | 1-69 | `EF5058570C685B60C04893267C8F57B4BFF5E214E344E0BF51DCF30DF347DFF4` |
| `handbook/restoration/inherited-10675-10769.tex` | 1-104 | `B745B19A1B07592A4CD59FEC1791B3102E88B3C53E30F276C06CA168EBC1D57A` |
| `handbook/restoration/inherited-03519-03680.tex` | 1-162 | `B1F502609BB084ACFF222A7431E05CAED5273ACD19C367B45CBDCCB63F306897` |
| `handbook/restoration/inherited-03429-03518.tex` | 1-90 | `EF123D37FB24D3D7194768867468E3E739E92C066E855195B0F7F6B040892D0B` |
| `handbook/restoration/inherited-03038-03104.tex` | 1-67 | `8531B8FC91A659AB7C5B131A77FCA7AFF9C97F0A052E3B78FE0459ADEC25FFAB` |
| `handbook/restoration/inherited-03105-03165.tex` | 1-61 | `5C062C8A2584C841ED74EC9B546FA502EF0FF4D667A5A702EC56B7C8A49463C9` |
| `handbook/restoration/inherited-03166-03239.tex` | 1-74 | `D7D08869229F450D219BCB06FFA8E990B60DB10F195B76D53E9ECCBBC480AC3C` |
| `handbook/restoration/inherited-10060-10088.tex` | 1-29 | `21DC5D4896EA787EB7AE605589C4126C11BA969B5FA41B0FA1D30B9D28C8C7B8` |
| `handbook/restoration/inherited-00444-00506.tex` | 1-63 | `F89DFC23FCC42B1ED8E4977653220D42BF6E6CF06E54BADAACE6FC0FC5799589` |

The complete author intake, `handbook/CONVENTIONS.md`, and the edition contract
were also read. Initial body and active annex drivers were read completely to
verify the inherited named-result hooks. The old unsuffixed constructibility
annex was not used as a proof source. Final integration deltas are recorded
separately below when supplied.

### Eight proof-pair findings

In the following table, body locations are in the frozen new body and annex
locations are in the frozen new annex.

| Result suffix | Body / annex read | Source and dependency assessment |
| --- | --- | --- |
| `ordinal-foundation-facts` | 37-53 / 3-113 | PASS. Original strict well-order ordinalhood is preserved. Both elementwise directions of the proper-subordinal step are supplied at annex 19-30. The intersection argument then gives comparison without assuming the old sketch. The bounded predicate's converse proves strict linearity and least elements by ambient Foundation, followed by successors, union, limit closure and the least-inductive-set argument for omega. |
| `definable-ordinal-recursion` | 55-87 / 115-204 | PASS. `App_G` records one fixed first-order formula with fixed set parameters. Restriction is Separation on a graph. Compatibility is proved before any Replacement image is formed. The limit image has the set domain lambda and a unique approximation for each input; its union has domain lambda and retains the required recursion equations. Arbitrary set restrictions use Replacement with a functional pair-valued formula. Competing definable classes are handled formula by formula. |
| `set-sized-definability` | 91-149 / 206-364 | PASS. Product, triple, list and assignment bounds are explicit power-set/Separation constructions. All nine record types match the actual membership-language syntax and Tarskian clauses. The finite truth operation is total even for arbitrary earlier set values, so the new recursion theorem applies. Uniform Sat quantifies over set computations; Separation on `C x S_A` forms the relation. The two-way formula construction distinguishes variable fields from earlier-position fields. Formula coincidence and a bijective variable renaming justify exactly finite parameters, and the empty branch agrees with the corrected base. |
| `bounded-transitive-absoluteness` | 151-164 / 366-396 | PASS. This is a scheme for each fixed bounded formula. Membership, identity and all five non-quantifier logical cases agree. The quantifier's bound variable differs from its bounding variable; updating preserves the latter value. Transitivity makes both quantifier ranges exactly the same set. No internal model-of-ZF assumption is introduced. |
| `def-transitive-growth` | 166-177 / 398-417 | PASS. `A in Def(A)` uses identity for nonempty A and the separate base for empty A. For transitive A each member x is defined as a subset by the parameter formula `v_0 in v_1`; this establishes the needed inclusion and transitivity. No monotonicity of Def on arbitrary pairs of transitive inputs is assumed. |
| `hierarchy-recursion-existence` | 181-192 / 419-470 | PASS. Zero/successor/nonzero-limit cases are exhaustive, and predecessor uniqueness and a set-valued range union are justified. Uniformity of Def comes from the new set construction; Power Set gives the V operation. The resulting first-order level formula reproduces the original L and V clauses and supports set restrictions. No old global V-hierarchy theorem or rank-existence claim is imported. |
| `constructible-level-height` | 194-211 / 472-569 | PASS. Transitivity and inclusion precede the height induction. The successor's defining formula is the proved bounded ordinal predicate, evaluated only after nonemptiness and transitivity of the input level are shown. Zero instead uses the corrected explicit base. Reverse height inclusion uses each ordinal member's containment in the previous level. Limit height uses the proved ordinal union identity. Strict growth and L/V inclusion follow with the original ordinal hypotheses. |
| `constructible-class-foundation` | 213-216 / 571-587 | PASS. Class transitivity and ordinal containment follow from the proved level results. Properness assumes a set extension only for contradiction; Separation then forms its ordinal members and Union gives an ordinal, whose successor produces self-membership. Neither unrestricted comprehension nor a union over a proper class is taken as a set. |

### Functionality, set bounds, and source standing

The relevant ZF schemas were checked against their actual text in
`inherited-10089-10271.tex:67-98`, including the unique-value antecedent of
Replacement. The particular uses pass: graph restrictions and disagreement
sets are bounded by given sets; compatible approximations are unique before
the limit Replacement; values and ordered pairs are functional before forming
arbitrary set restrictions; truth subsets are uniquely determined by Separation
on the assignment set; Def is Separation on a power set; and hierarchy ranges
are images of set functions. Empty, Pairing, Union and Power Set supply the
other bounding objects. These arguments use no selection from a family of
nonempty sets. Picking one member of a fixed nonempty A to make a constant
assignment is ordinary existential reasoning, not Choice.

The earlier complete transfinite-induction argument at
`inherited-10353-10451.tex:54-72` is a valid prerequisite after the new ordinal
facts. Its counterexample set is bounded by a single successor ordinal. The
earlier ordinal comparison and definable recursion paragraphs at 28-52 and
85-95 remain sketches in the initially read source. The new annex independently
supplies their needed calculations and set constructions. The old general
membership-recursion sketch at `inherited-10272-10352.tex:40-62`, the cited
P1 recursion at `inherited-00603-00647.tex:29-44`, and the global V hierarchy
sketch at `inherited-10452-10520.tex:20-40` are not used to discharge missing
steps of these eight proofs.

The finite instruction language is auxiliary and its truth bridge is explicit;
it does not claim byte identity with the ordinary formula-string coding. The
actual membership language has no function symbols, so all its terms are
variables. The new atomic rows therefore match all its atom cases. Nonempty
ordinary structures, update semantics and term coincidence were checked in
`inherited-03429-03518.tex:7-74`; all Tarskian clauses and the complete formula
coincidence proof were checked in `inherited-03519-03680.tex:4-58`. The formula
and free-variable formation clauses were also read directly. No satisfaction
in the universe or in the empty structure is asserted by the construction.

The remaining relativization scheme at
`inherited-10675-10769.tex:90-104` retains a separately cited standing in the
initial source. The new body expressly leaves relativization, well-ordering,
condensation and GCH to their separate proofs. This PASS does not acquire the
unread Jech body or close those separate obligations.

### Separate integration scope

The parent will request a separate bounded addendum for the final routes,
canonical notation, and correction replacing the old constructible-class
proof-sketch paragraph. This completed assessment does not wait for those
changes. The PASS above applies to the frozen new derivation and the exact
prerequisites listed. It is not a static, build, visual, provenance-validation,
admission, or publication verdict.
