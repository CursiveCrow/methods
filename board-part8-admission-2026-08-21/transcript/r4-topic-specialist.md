REJECT

# Part VIII R4 topic-specialist admission review

## Scope and method

I reviewed the current reader graph rooted at `handbook/parts/p08.tex` and
`handbook/annex/p08.tex` under the correctness/nonclassical-logic mandate.  The
body driver routes all forty frozen intervals covering source lines
12970--14094, interleaves the live editorial units, and ends in the generated
Part VIII theorem/definition register (`handbook/parts/p08.tex:2-74`;
`handbook/parts/p08/source-map.tex:5-12,55-86`).  I re-read those restored
units, every routed editorial body unit, all three routed annex units, all
forty-eight calculus sheets actually referenced by Part VIII, the relevant
bibliography records, and the Part VIII register ceilings.  I did not read
another reviewer's transcript or conclusion, edit any manuscript/spec/tool/
generated source, run tests, or build TeX/PDF.

The governing source/content invariants are definition before use, a fixed
syntax/semantics/calculus for each system, exact hypotheses, honest proof
standing, and no reader-visible OPEN/stub/owed/internal-row prose
(`board-part8-admission-2026-08-21/charter.md:11-16`).

## Blocking finding

### F-R4-1 — High — the row is gone, but undefined Part IX vocabulary remains on the live Part VIII route

**Status:** blocking/open.

**Locations:**

- `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:220-241`, especially
  `:236-239`;
- `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:496-501`, especially
  `:499-500`;
- scope confirmation: `spec/registers/depth-gaps.csv:134` (`D-P11-007`,
  answer-set programming and Datalog, homed in Part IX rather than Part VIII).

**Evidence and concrete harm.**  The framework table now contains only
preferential consequence, ranked consequence, Reiter default logic,
circumscription, autoepistemic logic, and AGM revision
(`paraconsistent-and-nonmonotonic.tex:227-233`).  Thus the misplaced ASP row
itself has been removed.  But the caption still says, verbatim, that
“Stable-model semantics and ASP are introduced in Part IX”
(`:238-239`), and the later framework warning still requires every claim to
fix a “reduct object” (`:496-501`).

No live Part VIII definition gives the syntax, model class, satisfaction
condition, or construction denoted by `stable-model semantics`, `ASP`, or the
nonmonotonic `reduct`.  The caption's assertion that these are “not used before
definition here” is also contradicted by the later use of “reduct object” as
one of the purportedly fixed semantic/operational objects.  A reader therefore
cannot eliminate the terms to any typed object or know what preservation
theorem the warning concerns.  This is exactly the cross-part definition-
before-use debt that the repair was meant to remove, and it violates both the
charter and the supplied technical-name rule.  Merely announcing that a term
will be defined in Part IX does not define it in Part VIII.

**Exact minimal correction.**

1. End the table caption after
   `autoepistemic bounds follow \textcite{Gottlob1992}.` and delete the sentence
   `Stable-model semantics and ASP are introduced in Part~IX rather than used
   before definition here.`
2. At `paraconsistent-and-nonmonotonic.tex:499`, delete `, or reduct`, so the
   warning ranges only over the preference, ranking, default, minimization, and
   revision objects actually defined in this Part.

No mathematical replacement is owed in Part VIII: `D-P11-007` already assigns
the omitted subject to Part IX.  The exact correction is deletion of the two
premature references, not migration of Part IX content into this Part.

## Targeted R4 repair verification

### Intermediate-logics complete lattice — accepted

The live text first defines an intermediate logic as a theorem set between IPL
and CPC, closed under uniform substitution and modus ponens
(`handbook/parts/p08/intuitionistic-supplement.tex:484-494`).  It then orders
such sets by inclusion, defines arbitrary meets by intersection, and defines a
join as the least intermediate logic containing the union (`:496-504`).  The
empty meet and join are explicitly CPC and IPC respectively (`:504-507`).
These clauses establish a complete lattice with the correct top and bottom.
For a nonempty family, the union already contains IPL and its substitution/MP
closure is the stated join; the immediately following empty-family convention
handles the sole case in which the bare union does not already contain IPL.
The standing/nonredundancy paragraph correctly says this is a metalinguistic
order on theorem sets, not an object-language connective, and does not mistake
the displayed IPC--KC--LC--CPC chain for the whole lattice (`:509-514,
:588-602`).

The adjoining inclusion proof remains sound.  Substituting `B=\neg A` in LC
prelinearity and applying the two displayed IPL implications yields KC's weak
excluded-middle schema (`:538-546`).  The four-world diamond with a unique
greatest world validates KC but refutes prelinearity under the displayed
valuation (`:547-554`); the two remaining Kripke countermodels establish the
outer strict inclusions (`:555-560`).

### Three variant-indexed free-logic quantifier surfaces — accepted

The selected negative semantics fixes nonempty outer and inner domains, total
ordinary-term denotation into the outer domain, predicates strict to the inner
domain, strict equality, the existence predicate, and inner-domain
quantification (`handbook/parts/p08/conditionals-deontic-free.tex:7-25`).  The
comparison table then distinguishes:

- negative two-valued strict predication and identity (`:52-56`);
- positive outer-domain predication and ordinary outer identity while retaining
  inner-domain quantification (`:57-61`); and
- neutral partial terms with Strong-Kleene propagation and only `t` designated
  (`:62-67`).

The consequence relation is separately indexed by `neg`, `pos`, and `neu` and
does not claim a family-wide proof calculus (`:75-85`).  The six displayed
semantic inferences are valid (`:87-113`): in the negative and positive rows a
true `E!(t)` is the existence guard placing the value of `t` in the inner
quantifier domain (`:93-102`); in the neutral row both premises must be
designated `t`, while an undefined or nonexisting term makes `E!(t)`
nondesignated (`:103-107`).  Universal instantiation then follows by the
quantifier/substitution clause and existential generalization uses that same
inner-domain witness.  The text correctly limits `exists x(x=t)` to the
corresponding existence/definedness guard (`:116-118`).

## Full mathematical regression by charter lot

### Lot 1 — checked clean

The exact inherited IPL material retains its stated proof status.  The
editorial supplement distinguishes the Glivenko, Kolmogorov, and Kuroda maps
before stating their separate scopes (`intuitionistic-supplement.tex:105-177`),
types Heyting algebra valuations and implication (`:248-290`), and gives the
open-set clauses with interior in the implication operation
(`:292-321`).  The BHK/realizability boundary does not promote a reading into a
formal semantics; existence extraction is appropriately hypothesis-bound.  IQC
uses expanding nonempty domains, persistent interpretations, and the correct
quantifier clauses before stating completeness and the constant-domain
principle boundary (`:418-480`).  The intermediate-logic package is disposed
above.  I found no new definition-order, hypothesis, countermodel, theorem-
strength, or proof-status defect in this lot.

### Lot 2 — checked clean

The modal supplement fixes each Hilbert system and exact frame class before
claiming adequacy.  The K/KT/S4/S5 canonical proof is explicitly proved in the
annex (`handbook/parts/p08/modal-logics-supplement.tex:318-334`;
`handbook/annex/p08/modal-completeness-supplement.tex:4-106`), while the other
systems retain cited rather than locally proved standing.  The correspondence
table, restricted Sahlqvist statement, Godel--McKinsey--Tarski translation,
bisimulation, filtration, neighborhood semantics, general-frame boundary, and
Kripke-incompleteness boundary keep their exact scopes
(`modal-logics-supplement.tex:32-61,287-635,636-790`).  Quantified modal logic
separates actualist varying, constant, increasing, and decreasing domains and
states the Barcan directions under the matching Fitting clauses
(`:846-1009`).  No family-wide soundness, completeness, FMP, or decidability
claim is inferred from a neighboring presentation.

### Lot 3 — checked clean apart from F-R4-1's cross-part vocabulary, which occurs in Lot 4

The temporal chapter types total transition structures, CTL state formulas,
CTL* state/path formulas, and the positive-variable modal mu-calculus before
use (`handbook/parts/p08/temporal-epistemic-supplement.tex:46-265`).  The Buchi
definition is genuinely nondeterministic: `delta:Q times Sigma -> P(Q)`, a run
chooses a successor at each letter, and acceptance existentially selects a run
whose recurrence set meets `F` (`:353-379`).  This no longer conflates the
illustrated deterministic automaton with the general LTL translation.

The group convention restricts every routed group modality to a nonempty
finite group (`handbook/parts/p08/group-operator-convention.tex:1-8`), matching
the common-knowledge sheet's language and every rule side condition
(`handbook/registry/calculi/hilbert-common-knowledge.tex:2-6`).  Distributed,
everyone, and common knowledge use respectively intersection, one-step union,
and reflexive-transitive closure (`temporal-epistemic-supplement.tex:517-570`).
PAL and basic hybrid K keep their update/tableau boundaries.

The deontic best-world semantics is total-preorder based, smooth on definable
candidate sets, and explicitly nonvacuous on impossible conditions
(`conditionals-deontic-free.tex:173-212`).  Stalnaker selection and Lewis
sphere semantics remain distinct.  The Lewis sphere family has the displayed
nesting, union, nonempty-intersection, weak-centering, centering, and optional
limit conditions, and its truth clause is limit-free (`:246-312`).  The VC
sheet is tied only to centered sphere semantics and the cited Lewis/Wen result
(`:356-364`).  The probabilistic theorem is now the exact fixed-event theorem
over the finite Boolean algebra generated by two logically independent events,
with strict positivity and same-algebra hypotheses (`:471-483`).  The free-
logic package is disposed above.

### Lot 4 — checked clean except F-R4-1

The finite-matrix tableau surface preserves formula occurrences, closes empty
preimages, and handles empty root families; the annex proofs match that sheet.
FDE support pairs and both orders, K3/LP dual facts, finite and standard
Lukasiewicz semantics, Bochvar, Post matrices, t-norm residua, and
supervaluation are all typed before their claims
(`handbook/parts/p08/many-valued-supplement.tex:74-535`;
`handbook/annex/p08/many-valued-supplement.tex:18-124`).

The relevance/linear supplement keeps E, R, and RM distinct; gives the matched
Routley--Meyer semantics only at its cited ceiling; and fixes full CLL syntax,
phase semantics, associative unit-free Lambek L, the IMLL boundary, and the
selected commutative affine calculus
(`handbook/parts/p08/relevance-linear-supplement.tex:45-245,266-566`).  The
affine sheet has antecedent weakening but no antecedent contraction, as the
body claims.  The IMLL empty-context erratum supplies the empty tensor needed
by the inherited algebraic semantics without changing inherited bytes.

The da Costa C1 body and sheet agree on primitive consistency notation,
restricted reductio/controlled explosion, and nonexplosion
(`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:72-132`;
`handbook/registry/calculi/hilbert-da-costa-c1.tex:1-24`).  KLM preferences use
an irreflexive transitive strict order and separately define smooth and ranked
models; System P and rational representation claims retain their precise
model-class hypotheses (`paraconsistent-and-nonmonotonic.tex:149-218`).  AGM
revision and contraction list the eight postulates for each operation, state
Levi/Harper in the correct directions, and restrict the faithful-preorder
representation theorem to finite propositional belief sets (`:245-356`).
Reiter extensions, circumscription, and autoepistemic expansions remain
separate, typed constructions (`:360-494`).  The only residual is the undefined
Part IX vocabulary in F-R4-1.

## Calculus, bibliography, register, and reader-debt checks

- All forty-eight calculus identifiers on the live Part VIII route resolve to
  a concrete sheet.  I rechecked the complete surfaces, including LJ/NJ,
  normal and non-normal modal systems, CTL/CTL*/LTL/mu/PAL/common knowledge,
  CK/VC, hybrid tableaux, matrix tableaux, Lukasiewicz/t-norm calculi,
  E/R/RM, CLL/IMLL/affine/Lambek, C1, and Reiter extensions.  Their languages,
  consequence shapes, rule side conditions, and body uses agree.
- The newly relevant bibliography records exist and identify the intended
  scholarly sources: `ChagrovZakharyaschev1997`
  (`handbook/bib/handbook.bib:1554-1561`) and the free-logic records
  `Russell1905`, `Lambert1967`, `Bencivenga1986`, `Lehmann2002`, and
  `GratzlPavlovicNolt2025` (`:3460-3519`).  The previously repaired Lewis,
  Buchi/Vardi, AGM/KLM, da Costa, Dummett/Jankov, Dunn/Restall, and linear-
  logic source roles remain correctly matched to cited rather than locally
  proved claims.
- The generated live register includes the new intermediate-logic lattice and
  the variant-indexed free-logic consequence definition, and it preserves the
  declared proved/sketched/cited statuses
  (`handbook/generated/audit-p08.tex:41-44,102-113,167-182`).
- A live-route scan found no construction `OPEN`, `stub`, `owed`, `TODO`,
  `FIXME`, or placeholder prose.  Occurrences such as “open set,” “open
  assumption,” “open branch,” and the documented open P-versus-quasipolynomial
  complexity problem are mathematical uses, not reader construction debt.
- The register ceiling `D-P11-007` remains external to Part VIII.  Accordingly,
  removing the two residual names in F-R4-1 respects rather than weakens the
  registered boundary.

## Coverage ledger

| Charter lot | Coverage | Disposition |
|---|---|---|
| 1. Intuitionistic/intermediate, translations, algebraic/topological, realizability/existence, IQC | complete live-body, exact-source, sheet, annex, bibliography, and ceiling check | checked clean |
| 2. Modal/canonical/correspondence/Sahlqvist/bisimulation/filtration/neighborhood/QML | complete live-body, sheet, annex, bibliography, and ceiling check | checked clean |
| 3. Temporal/CTL/CTL*/mu/epistemic/PAL/hybrid/conditional/deontic/free | complete live-body, sheet, annex, bibliography, and ceiling check | checked clean |
| 4. Many-valued/fuzzy/supervaluation/relevance/linear/Lambek/paraconsistent/adaptive/nonmonotonic plus apparatus | complete live-body, sheet, annex, bibliography, register, and route check | **blocking only at F-R4-1** |

No charter lot was left unchecked.  I found no mathematical or source-content
regression outside the exact residual recorded in F-R4-1.  Because that
residual directly fails the requested “no undefined Part-IX concepts remain in
P8” condition, the current frozen source/content snapshot is not admissible.

