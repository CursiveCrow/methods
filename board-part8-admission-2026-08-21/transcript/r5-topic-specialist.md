ACCEPT

# Part VIII R5 topic-specialist verdict

## Scope and verification boundary

I reviewed the current live reader graph rooted at `handbook/parts/p08.tex` and
`handbook/annex/p08.tex`, including the forty exact restoration wrappers, all
routed editorial body and annex units, the generated Part VIII register, all
forty-eight referenced calculus identifiers (defined across forty-five sheet
files), the relevant bibliography roles, and the Part VIII register ceilings.
I did not read another seat's transcript or conclusion, edit manuscript/spec/
tool/generated source, run tests, or build TeX/PDF.

The body route remains complete and ordered: the driver routes the frozen
source intervals and all editorial supplements at
`handbook/parts/p08.tex:2-64`, then routes the generated lookup at `:66-74`.
The source map still records forty intervals reproducing authority lines
12970--14094, 1,125 lines without gap, overlap, duplicate, or reorder
(`handbook/parts/p08/source-map.tex:5-12`).  The annex driver still routes the
source-sketch map and the two live proof supplements
(`handbook/annex/p08.tex:1-10`).

## Exact R4 corrections

### 1. Misplaced Part IX vocabulary — fixed exactly

The nonmonotonic comparison table contains only the six Part VIII frameworks
that are actually defined: preferential consequence, ranked consequence,
Reiter default logic, circumscription, autoepistemic logic, and AGM revision
(`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:220-233`).  Its caption
now ends with the Gottlob attribution (`:236-238`); the former sentence naming
stable-model semantics and ASP is gone.

The framework-specific warning now ranges over the defined preference,
ranking, default, minimization, and revision objects and then requires separate
preservation theorems (`:495-500`).  The former `reduct object` phrase is gone.

I scanned all fifty-eight files directly on the live body/annex route and all
forty-five files defining its referenced calculus sheets for `ASP`,
`answer-set`, `stable model`/`stable-model`, and standalone `reduct`.  There are
no occurrences.  The autoepistemic phrase *stable expansion* remains, but it is
not stable-model vocabulary: it is explicitly defined as Moore's fixed point
at `paraconsistent-and-nonmonotonic.tex:420-438` and used consistently by the
autoepistemic system card at `:477-493`.

### 2. No regression in the neighboring Lewis package

The current Lewis definition includes the correct weak-centering conditions

\[
 w\in U_w,
 \qquad
 \forall S\in\mathcal S_w\,(S\ne\varnothing\to w\in S),
\]

at `handbook/parts/p08/conditionals-deontic-free.tex:268-300`.  The first
conjunct is necessary because closure under the empty union puts the empty
sphere in each sphere system; without `w in U_w`, a system containing only the
empty sphere would satisfy the second conjunct vacuously, make every
counterfactual true by the no-accessible-antecedent clause, and invalidate
conditional modus ponens.  With both conjuncts, whenever `A` is true at `w`
and `A > B` holds, the witnessing nonempty sphere contains `w`, hence `B` is
true at `w`.  Centering by `{w} in S_w` still implies weak centering by nesting.
This agrees with the VC sheet's separate weak-centering and centering side
conditions (`handbook/registry/calculi/hilbert-counterfactual-vc.tex:1-11`) and
does not introduce a regression.

## Prior accepted mathematical content

### Lot 1 — intuitionistic and intermediate logics: checked clean

The negative translations remain separately defined with their exact scopes;
Heyting and topological semantics retain their typed valuation clauses; the
BHK/realizability discussion remains a boundary rather than an unearned
formal semantics; and IQC keeps expanding domains, persistence, and the exact
constant-domain qualification.  The complete-lattice definition remains
correct: intermediate logics are theorem sets between IPL and CPC closed under
uniform substitution and modus ponens (`handbook/parts/p08/intuitionistic-
supplement.tex:484-494`); arbitrary meets are intersections and joins are the
least intermediate logics containing the unions, with empty meet CPC and empty
join IPC (`:496-507`).  The KC-to-LC derivation and all three strictness
countermodels remain valid (`:519-560`).

### Lot 2 — modal logic: checked clean

The normal-system catalog still matches each Hilbert sheet to its exact frame
class.  Canonical strong completeness for K, KT, S4, and S5 retains proved
standing and the full routed annex argument
(`handbook/parts/p08/modal-logics-supplement.tex:318-334`;
`handbook/annex/p08/modal-completeness-supplement.tex:4-64`).  Correspondence,
the restricted Sahlqvist statement, the IPL-to-S4 translation, bisimulation,
filtration, neighborhood semantics, general frames, and Kripke-incompleteness
boundaries remain scoped to their actual hypotheses.  Quantified modal logic
still separates varying, constant, increasing, and decreasing domain regimes
before giving the corresponding Barcan directions
(`modal-logics-supplement.tex:846-1009`).  No family-wide adequacy or decision
claim is inferred from one presentation.

### Lot 3 — temporal, epistemic, conditional, deontic, and free logics: checked clean

Total transition structures, CTL state syntax, CTL* state/path syntax, and the
positive-variable modal mu-calculus remain definition-before-use exact
(`handbook/parts/p08/temporal-epistemic-supplement.tex:46-265`).  Buchi
automata remain nondeterministic, with transition sets, existential run choice,
and recurrence-set acceptance correctly separated from the deterministic
illustration (`:353-379`).  The nonempty finite group convention continues to
match distributed, everyone, common-knowledge, and common-knowledge-sheet
domains (`handbook/parts/p08/group-operator-convention.tex:1-8`;
`handbook/registry/calculi/hilbert-common-knowledge.tex:2-6`).  PAL and hybrid K
retain their update and tableau boundaries.

The deontic best-world semantics remains total-preorder based, smooth on
definable candidate sets, and explicitly nonvacuous on impossible conditions
(`conditionals-deontic-free.tex:173-214`).  Stalnaker selection, CK selection,
and Lewis sphere semantics remain distinct.  The corrected VC sheet uses CA,
not the non-equivalent MOD schema, and the cited completeness claim is tied
only to centered, limit-free sphere semantics (`:316-400` and the VC sheet
above).  The finite probability-rich triviality theorem retains its fixed
event, four nonempty atoms, strict positivity, and same-algebra hypotheses
(`:473-485`).

The free-logic comparison still fixes negative, positive, and neutral term,
atomic, equality, quantifier, and description policies before defining the
three indexed consequence relations
(`conditionals-deontic-free.tex:7-85`).  Each universal-instantiation and
existential-generalization surface has the exact existence/designation guard
needed to put the term's value in the inner quantifier domain (`:87-118`), and
the text claims no interderivability of proof calculi.

### Lot 4 — many-valued, substructural, paraconsistent, and nonmonotonic logics: checked clean

The finite-matrix tableau, FDE support-pair matrix and orders, K3/LP facts,
Lukasiewicz systems, Bochvar and Post matrices, t-norm residua, and
supervaluation continue to match the current sheets and annex proofs
(`handbook/parts/p08/many-valued-supplement.tex:74-535`;
`handbook/annex/p08/many-valued-supplement.tex:18-124`).  E, R, and RM remain
distinct; CLL, phase semantics, IMLL with its empty-context erratum,
associative unit-free Lambek L, and the selected affine calculus retain their
correct structural boundaries
(`handbook/parts/p08/relevance-linear-supplement.tex:45-566`).

The da Costa C1 body still agrees with its sheet on primitive consistency,
restricted reductio, controlled explosion, and nonexplosion
(`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:72-132`).  KLM uses an
irreflexive transitive preference and distinguishes smooth from ranked models
before its two representation statements (`:149-218`).  AGM revision and
contraction retain all eight postulates each, the correct Levi and Harper
directions, and the finite-propositional faithful-preorder hypothesis
(`:244-355`).  Reiter extensions, typed circumscription, and Moore stable
expansions remain separate constructions (`:359-493`).

## Apparatus, sources, and status surfaces

- All forty-eight live `sheet:` identifiers resolve to concrete calculus
  definitions across forty-five registry files.  Their languages, judgment
  shapes, side conditions, and body uses remain aligned.
- The relevant bibliography entries remain present and matched to the claim
  they control, including `ChagrovZakharyaschev1997` for the intermediate-
  logic lattice; `Lambert1967`, `Bencivenga1986`, `Lehmann2002`, and
  `GratzlPavlovicNolt2025` for free logic; and the Lewis/Wen, Buchi/Vardi,
  AGM/KLM, da Costa, Dummett/Jankov, Dunn/Restall, and linear-logic sources.
- The generated register still records the intermediate-lattice and free-
  consequence definitions, VC completeness and Lewis triviality as cited, and
  the framework-specific nonmonotonic warning without changing proof standing
  (`handbook/generated/audit-p08.tex:42,103,110,112,182`).
- A current live-route scan finds no reader construction `OPEN`, `stub`,
  `owed`, `unadmitted`, `TODO`, `FIXME`, or placeholder prose.  The surviving
  uses of “open” are ordinary mathematical terms: open sets/assumptions/
  branches and the stated open P-versus-quasipolynomial complexity problem.

## Coverage ledger

| Charter lot | Current disposition |
|---|---|
| 1. Intuitionistic/intermediate, translations, algebraic/topological, realizability/existence, IQC | checked clean |
| 2. Normal/non-normal modal, correspondence, Sahlqvist, bisimulation, filtration, QML/Barcan | checked clean |
| 3. Temporal/CTL/CTL*/mu, epistemic/common knowledge/PAL/hybrid, conditional/deontic/free | checked clean |
| 4. Many-valued/fuzzy/supervaluation, relevance/linear/Lambek, paraconsistent/adaptive/nonmonotonic, sheets/apparatus | checked clean |

No charter lot was left unchecked.  Both R4 corrections are present, no
forbidden Part IX vocabulary remains anywhere on the Part VIII reader or
active-sheet route, and no mathematical/source-content regression remains.

