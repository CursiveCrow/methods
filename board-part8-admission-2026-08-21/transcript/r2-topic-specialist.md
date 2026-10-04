REJECT

# Part VIII admission board, round 2 — topic-specialist report

## Mandate, scope, and method

I reviewed the current live reader graph rooted at handbook/parts/p08.tex and
handbook/annex/p08.tex as a correctness/nonclassical-logic specialist.  I did
not read any other reviewer's transcript, verdict, ledger, or chair record.
The reviewed graph included:

- all exact restoration wrappers SRC-12970 through SRC-14094 in their routed
  order;
- the routed source map and all current body additions:
  intuitionistic-supplement.tex, modal-logics-supplement.tex,
  temporal-epistemic-supplement.tex, conditionals-deontic-free.tex,
  many-valued-supplement.tex, imll-empty-context-erratum.tex,
  relevance-linear-supplement.tex, paraconsistent-and-nonmonotonic.tex,
  further-reading.tex, and the generated Part VIII audit;
- the complete annex route: source-sketch-map.tex,
  many-valued-supplement.tex, and modal-completeness-supplement.tex;
- every calculus sheet referenced by a live Part VIII system card or theorem;
  and
- the relevant bibliography records and every Part VIII row in
  spec/generated/depth-table.tex:96-133 and
  spec/generated/newcontent-table.tex:84-116, together with the three
  registered pointer-only ceilings at newcontent-table.tex:188-191.

The audit was source/content only.  I did not edit the handbook, specification,
generator, or calculus sources, and I did not run tests or a TeX/PDF build.
Accordingly this report does not decide provenance, compilation, visual,
human, or user-acceptance gates.

Seven source-content residuals remain.  F1 is a direct falsehood.  F2-F5 leave
required theorem or semantic surfaces false, underdefined, or ill-typed as
written.  F6 is an exact source-class defect whose theorem can be retained
after the intended class is stated.  F7 is a small but reader-visible domain
inconsistency.  F1-F5 independently prevent source/content admission.

## Findings

### F1 — BLOCKER — the asserted KC/LC non-inclusion is false

**Live location.** handbook/parts/p08/intuitionistic-supplement.tex:496-508
defines the KC and LC profiles; lines 510-538 state that neither is included
in the other; lines 540-555 draw the same relation by giving KC and LC only
separate arrows from IPC.  This is the registered intermediate-logic content
for D-P10-018 and N-b-031.

**Exact defect.** \(\mathsf{KC}\subsetneq\mathsf{LC}\), not incomparability.
Substitute \(B=\neg A\) in LC prelinearity:
\[
  (A\to\neg A)\lor(\neg A\to A).
\]
IPL proves
\[
  (A\to\neg A)\to\neg A
  \quad\text{and}\quad
  (\neg A\to A)\to\neg\neg A.
\]
Disjunction elimination therefore gives
\(\neg A\lor\neg\neg A\), the KC schema.  Thus every KC theorem is an LC
theorem.

The inclusion is strict.  Take the finite rooted frame
\[
 r<a<t,\qquad r<b<t,
\]
where \(a,b\) are incomparable and \(t\) is the unique greatest world.  This
is a standard KC frame.  With persistent valuations
\(V(p)=\{a,t\}\) and \(V(q)=\{b,t\}\), at \(r\) both \(p\to q\) and
\(q\to p\) fail.  Hence LC prelinearity fails on a KC frame.

**Concrete harm.** The prose and hierarchy figure teach the wrong order in
the lattice of intermediate logics, and directly contradict what follows
from the two displayed schemas.

**Exact correction.** Replace the non-inclusion sentence by
\(\mathsf{IPC}\subsetneq\mathsf{KC}\subsetneq\mathsf{LC}\subsetneq
\mathsf{CPC}\); add the two-line derivation above and the four-world strictness
countermodel; and add a directed KC-to-LC edge to the figure.  The relevant
bibliography records are handbook/bib/handbook.bib:4495-4515
([Dummett 1959](https://doi.org/10.2307/2964753) and
[Jankov 1968](https://doi.org/10.1070/IM1968v002n05ABEH000690)).

### F2 — BLOCKER — the Lewis sphere class and VC completeness domain are not defined exactly

**Live location.** handbook/parts/p08/conditionals-deontic-free.tex:212-233
defines only a nonempty nested family of subsets and then mentions
“centering” and “strong centering” without defining either.
Lines 276-284 assert VC/C1 completeness for “the centered sphere semantics”
of that definition.  Lines 303-317 call the same class strongly centered,
while lines 329-334 separately name V, VW, and VC.  The registered sheet,
handbook/registry/calculi/hilbert-counterfactual-vc.tex:1-9, attaches
conditional MP to “weak centering” and CS to “strong centering,” again without
supplying either model condition.  This is required content N-b-016 and
D-P10-038.

**Exact defect.** A Lewis system of spheres is not merely an arbitrary
nonempty chain of subsets.  The source presentation supplies the nesting and
the relevant closure conditions, and distinguishes weak centering from
centering.  In the standard orientation, weak centering requires the base
world to belong to every nonempty sphere around it; centering requires the
singleton base world itself to be a sphere.  The live definition states none
of these clauses, does not say whether “strong centering” is its name for
Lewis's centering, and therefore does not determine the model class quantified
over by the completeness theorem.

Under only the clauses actually printed, even the sheet's conditional-MP
schema can fail.  Let \(W=\{w,u\}\), let
\(\mathcal S_w=\{\{u\}\}\), make \(A\) true at both worlds, and make \(B\)
true only at \(u\).  Then the displayed variably-strict clause makes
\(A\Box\!\!\to B\) true at \(w\), while \(A\to B\) is false there.  The
intended centering condition presumably excludes this model; the current
definition does not.

**Concrete harm.** The reader cannot check soundness of two displayed axiom
schemas or identify the class for which the stated completeness theorem is
claimed.  The terms also fail the local technical-name rule: their exact
eliminable definitions, standing, and nonredundant difference are absent at
the place of introduction.

**Exact correction.** At Definition def:p08-lewis-conditional:

1. type a sphere system \(\mathcal S_w\) and state the exact source-required
   nesting, arbitrary-union, and nonempty-intersection closure clauses;
2. define weak centering and centering by formulas, explicitly say whether the
   manuscript's “strong centering” is just the latter condition, and keep the
   limit assumption separate;
3. state V, VW, and VC against those exact classes; and
4. make Theorem thm:p08-vc-completeness quantify over the exact VC class.

If the authors instead intend a closure-free equivalent presentation, that
equivalence must be stated and cited rather than silently changing the source
class.  The controlling primary source is [Lewis,
Counterfactuals](https://fitelson.org/piksi/piksi_18/lewis_counterfactuals.pdf),
especially the system-of-spheres and centering clauses; the live bibliography
records are handbook/bib/handbook.bib:1700-1724.

### F3 — HIGH — the LTL card requires nondeterministic Büchi automata, but only deterministic runs are defined

**Live location.** handbook/parts/p08/temporal-epistemic-supplement.tex:21-40,
especially lines 36-38, says every LTL formula has an equivalent
nondeterministic Büchi automaton.  Definition def:p08-buchi-automaton at
lines 353-372 supplies \(\delta:Q\times\Sigma\to Q\) only “in the
deterministic case” and then defines only the unique deterministic recurrence
\(r_{n+1}=\delta(r_n,\sigma_n)\).  No transition relation, set-valued
transition, nondeterministic run, or existential acceptance clause is defined
before the card uses the nondeterministic object.

**Concrete harm.** The target named by the LTL translation is not a defined
mathematical object.  Deterministic Büchi automata are not an interchangeable
replacement: for example, the LTL language \(FG\,p\) (“only finitely many
\(\neg p\) positions”) is accepted by a nondeterministic Büchi automaton that
guesses the last \(\neg p\), but it is not deterministic-Büchi recognizable.

**Exact correction.** Define an NBW by
\[
 (Q,\Sigma,\delta,q_0,F),\qquad
 \delta:Q\times\Sigma\longrightarrow\mathcal P(Q),
\]
or equivalently by a typed transition relation.  Define a run by
\(r_0=q_0\) and \(r_{n+1}\in\delta(r_n,\sigma_n)\), and define word
acceptance by the existence of a run with
\(\operatorname{Inf}(r)\cap F\ne\varnothing\).  Then define the deterministic
specialization by singleton transitions.  This is the exact object needed by
the card's Vardi-Wolper claim; compare the author-hosted automata account in
[Vardi's formal-verification notes](https://www.cs.rice.edu/~vardi/comp607/2006/formalVerification.pdf),
pp. 27-31.  The cited Vardi-Wolper record is
handbook/bib/handbook.bib:2231-2238.

### F4 — HIGH — dyadic obligation uses an undefined preference class and a partial Best operator

**Live location.** handbook/parts/p08/conditionals-deontic-free.tex:139-158,
the required dyadic-obligation component of N-b-013.

**Exact defect.** The definition says only that each world has a “smooth
preference ordering” \(\preceq_w\), without typing its field, stating whether
it is a preorder or a strict order, defining its strict part and orientation,
or defining smoothness.  It then says that
\(\operatorname{Best}_w(B)\) is a nonempty set “when such worlds exist,” but
gives no value when there are no accessible \(B\)-worlds (or when accessible
\(B\)-worlds exist but no minimum does).  The satisfaction clause immediately
uses \(\operatorname{Best}_w(B)\) in all cases.

For example, accessible \(B\)-worlds
\(\{u_n:n\in\mathbb N\}\) with
\(u_{n+1}\prec_w u_n\) have no minimum.  A precise smoothness condition may
exclude that model, but no such condition is printed.  If there are no
accessible \(B\)-worlds, the live prose does not even assign a set to the
left side of the subset test.

**Concrete harm.** \(M,w\models O(A\mid B)\) is not a total recursively
specified satisfaction relation on the announced model class, so subsequent
claims about contrary-to-duty representation cannot be checked.

**Exact correction.** State a typed relation on \(R(w)\), its axioms,
preference orientation, and strict part.  Define, for every \(B\),
\[
 \operatorname{Best}_w(B)
   =\min_{\preceq_w}\bigl(R(w)\cap[B]\bigr),
\]
with the empty set as the explicit output when there are no candidates, and
state the exact smoothness/minimum-existence condition used for nonempty
candidate sets.  Then state explicitly whether empty Best makes the
obligation vacuously true or whether the truth clause has an existence
conjunct.  This also supplies the necessity/definition/standing/nonredundancy/
use data demanded for the new technical terminology.  The cited primary
record is Hansson 1969 at handbook/bib/handbook.bib:1667-1675
([DOI](https://doi.org/10.2307/2214372)).

### F5 — HIGH — the stated Lewis triviality theorem is false for arbitrary Boolean algebras

**Live location.** handbook/parts/p08/conditionals-deontic-free.tex:391-402,
the required Lewis-triviality component of N-b-017.

**Exact defect.** The theorem quantifies over every strictly positive finitely
additive probability on an otherwise arbitrary Boolean algebra.  That class
of probabilities can be empty, making the universal condition vacuous.

Let \(X\) be uncountable and take the Boolean algebra
\(\mathcal B=\mathcal P(X)\).  Partition \(X\) into four nonempty pieces and
let them be the four atoms determined by logically independent \(A,B\).
There is no strictly positive finitely additive probability on
\(\mathcal P(X)\): strict positivity would give every singleton
\(\{x\}\) a positive mass; for each \(n\), finite additivity permits at most
\(n\) singletons of mass at least \(1/n\); and every positive singleton mass
is at least \(1/n\) for some \(n\).  Thus \(X\) would be countable, a
contradiction.  Consequently the live universal quantifier ranges over no
probabilities and every fixed \(C\in\mathcal B\) vacuously satisfies it,
contrary to the theorem's conclusion.

**Exact correction.** State the finite four-atom form actually needed:
restrict to the finite Boolean algebra generated by \(A,B\), or add an exact
measure-richness/extension hypothesis ensuring that every positive assignment
to the four \(A,B\)-atoms is represented.  Then prove the conclusion by
varying the four positive atom weights.  Do not state it for arbitrary Boolean
algebras merely with a universal quantifier over possibly nonexistent
strictly positive measures.  The controlling paper is Lewis 1976,
handbook/bib/handbook.bib:1734-1743
([DOI](https://doi.org/10.2307/2184045)).

### F6 — MEDIUM — the KLM preferential-model class omits the source's transitivity clause

**Live location.** handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:86-112
defines \(\prec\) merely as “an irreflexive strict preference relation”;
lines 144-155 state the System-P and rational representation results.  This is
registered content N-b-032.

**Exact defect.** KLM Definition 16 calls the preferential ordering a strict
partial order and explicitly gives irreflexivity and transitivity.  The paper
also observes that the relevant results extend to arbitrary binary relations
when the smoothness condition is retained.  Thus there is no need to weaken
the mathematical theorem, but the handbook must say which of these two
classes it is defining.  “Strict preference relation” is not an eliminable
relation-axiom specification, and the current sentence expressly lists only
irreflexivity.

**Concrete harm.** A reader cannot tell whether the object is the source's
preferential model or a deliberate wider smooth-relation variant, so the
representation theorem's exact domain is ambiguous.

**Exact correction.** Either add
\[
 x\prec y\land y\prec z\Longrightarrow x\prec z
\]
and call the result the KLM preferential model, or explicitly name the wider
smooth binary-relation variant, cite KLM's extension observation, and state
that the representation theorem is being used in that broader form.  The
primary text is available as
[Kraus-Lehmann-Magidor 1990](https://arxiv.org/html/cs/0202021v1),
Definition 16 and the immediately following observation; the bibliography
record is handbook/bib/handbook.bib:1984-1993.

### F7 — LOW — the group domain changes after the inherited common-knowledge definition

**Live location.** The routed exact source at
handbook/restoration/inherited-13519-13551.tex:20-32 introduces \(E_G,C_G\)
for “a finite group \(G\subseteq I\),” without saying \(G\ne\varnothing\).
The later system card at
handbook/parts/p08/temporal-epistemic-supplement.tex:529-548 and the calculus
sheet handbook/registry/calculi/hilbert-common-knowledge.tex:1-6 restrict
throughout to a fixed nonempty finite \(G\).

**Exact defect and harm.** The first reader-visible language declaration
literally admits \(G=\varnothing\), while the later calculus and adequacy card
do not.  The handbook-wide empty-conjunction convention makes
\(E_{\varnothing}A=\top\), and the displayed reachability semantics makes
\(C_{\varnothing}A\leftrightarrow A\); so the edge case is mathematically
coherent, but it is not covered by the announced registered calculus.  The
problem is domain inconsistency, not undefined notation.

**Exact correction.** Add an editorial convention immediately after the exact
source wrapper that “group” means nonempty finite throughout this Part, or
retain the empty group explicitly, state the two identities above, and extend
the later language/card boundary accordingly.  The former is the smaller
repair and matches the current sheet.

## Checked-clean coverage

The following are affirmative source-content checks, not substitutes for the
findings above.

### Lot 1 — intuitionistic and intermediate logic

Checked the IPL/IQC syntax, Kripke persistence, forcing clauses, soundness and
completeness boundaries, propositional LJ scope restriction, disjunction and
existence-property boundaries, BHK and Brouwerian material, negative
translations, Heyting-algebra and topological semantics, varying-domain IQC
and constant-domain separation, intermediate-logic definitions, and their
registered source/status fields.  These were internally consistent at their
declared proof/citation ceilings except for F1.  In particular, the
propositional use of sheet:lj is now explicitly delimited rather than
silently advertised as an IQC calculus.

### Lot 2 — modal logic

Checked the normal modal cube, the K/T/D/B/4/5 axiom-to-frame
correspondences, canonical-model and truth-lemma proof, filtration and
bisimulation clauses, Sahlqvist statement boundary, normal versus
neighborhood/non-normal semantics, incompleteness caveats, quantified modal
syntax and assignments, constant/varying/actualist domain distinctions,
Barcan and converse-Barcan directions, rigid constants, and the corresponding
Hilbert/labelled-sequent sheets.  The annex's full K completeness proof has
the needed existence lemma and induction cases.  No residual mathematical
defect was found in this lot.

### Lot 3 — temporal, epistemic, conditional, deontic, and free logic

Checked LTL, CTL, CTL*, tense logic, modal \(\mu\)-calculus, parity-game and
complexity boundaries, S5/KD45 multi-agent systems, distributed and common
knowledge, public announcements, hybrid nominals/@, the signed hybrid
tableau, CK selection/premise semantics, Stalnaker selection, Lewis systems,
SDL and all routed paradox/contrary-to-duty examples, negative/positive/
neutral free-logic distinctions, descriptions, and all corresponding sheets.
The current parity-game statement remains correctly presented as an open
polynomial-time status rather than importing an unvetted announcement as a
settled theorem.  The residuals in this lot are F2-F5 and the domain cleanup
F7; F3 is the exact definition-before-use failure at the LTL automata bridge.

### Lot 4 — many-valued, substructural, paraconsistent, and nonmonotonic logic

Checked finite matrices, K3/LP/FDE designation and consequence, finite and
infinite Łukasiewicz systems, t-norm/residuum semantics and the stated
standard-completeness boundaries, supervaluational consequence, the complete
many-valued annex calculations, relevance-logic scope/decidability boundary,
classical and intuitionistic multiplicative linear logic, the empty-context
IMLL tensor correction, phase semantics, Lambek order sensitivity,
paraconsistency versus dialetheism, adaptive-logic and argumentation pointer
ceilings, KLM/System P/rational monotony, AGM, Reiter default logic,
circumscription, and autoepistemic logic.  The phase-space orthogonality and
facts clauses agree with the cited Girard presentation.  F6 is the sole
residual in this lot.

### Calculus, bibliography, route, and debt checks

All 46 calculus sheets referenced by the live Part VIII route were checked
against the system cards for language, consequence shape, rule premises, side
conditions, equality surface, and stated adequacy class.  Apart from F2's
undefined VC frame tags and F7's group-domain mismatch, the sheet/card
interfaces matched.  Every citation key used by the routed body, annex, and
these sheets has a live bibliography entry.  No reader-visible OPEN, stub, or
owed marker occurs in the routed Part VIII graph.  Similarly named combined
draft files outside the p08.tex/annex-p08.tex reader route were not treated as
reader content.

The new technical names introduced in the routed additions were checked for
necessity, local definition or explicit axiomatic status, standing,
nonredundancy, and later use.  F2, F4, and F6 are the remaining exact failures
of that rule; other introductions supply the required local explanation.

## Admission disposition and prioritized repair checklist

Part VIII cannot be admitted on mathematical/source-content grounds in the
current bytes.  The repair order is:

1. correct the false KC/LC order everywhere (prose, table explanation, and
   figure);
2. give the exact Lewis sphere/centering class and align the VC theorem and
   sheet to it;
3. define nondeterministic Büchi transition, run, and existential acceptance;
4. totalize and type the dyadic Best semantics;
5. add a nonvacuous finite/measure-rich hypothesis to the Lewis triviality
   theorem;
6. choose and state the exact KLM relation class; and
7. make the common-knowledge group domain uniform.

After those source repairs, the mathematical poll should be rerun against the
new live bytes.  Build, visual, provenance, human, and user gates remain
separate regardless of that later source verdict.
