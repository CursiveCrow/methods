REJECT

# Part VIII R3 topic-specialist admission review

## Decision

The current frozen Part VIII source/content route is mathematically sound on all
of the specifically repaired topics and on the remainder of the four charter
lots, with one admission-blocking exception.  The normal-ASP row in the
nonmonotonic comparison table uses a technical language, reduct semantics, and
query classes before any Part VIII definition supplies them.  The only live
definition is later in Part IX, and the depth register expressly assigns ASP to
that later owner.  This violates the charter's definition-before-use and
no-reader-construction-debt invariants and the repository's technical-name
rule.  F1 below is therefore still open; no other mathematical/source-content
defect was found.

This is a source/content verdict only.  I did not build TeX/PDF, run tests, or
perform a visual inspection, and I did not read any other reviewer's transcript
or conclusion.

## Scope actually checked

I followed the complete current reader route, not an earlier round's file list.
The body driver interleaves all forty exact-source intervals and all current
editorial units at `handbook/parts/p08.tex:1-74`; the source map records the
unbroken authority interval 12970--14094 and its 1,125 lines at
`handbook/parts/p08/source-map.tex:5-12`, then identifies every editorial unit
and its standing at `handbook/parts/p08/source-map.tex:44-86`.  I checked all
forty restored units, every routed editorial unit, the generated definition and
theorem register, the body-to-annex links, and all three annex units routed at
`handbook/annex/p08.tex:1-10`.

I also checked every one of the 48 calculus-sheet identifiers referenced from
the live body/annex graph: `affine-ill`, `cll-one-sided`, `hilbert-b`,
`hilbert-bl`, `hilbert-c`, `hilbert-common-knowledge`,
`hilbert-conditional-ck`, `hilbert-counterfactual-vc`, `hilbert-cpl`,
`hilbert-ctl`, `hilbert-ctl-star`, `hilbert-d`, `hilbert-da-costa-c1`,
`hilbert-e`, `hilbert-gl`, `hilbert-godel-fuzzy`, `hilbert-grz`, `hilbert-k`,
`hilbert-k4`, `hilbert-kd45`, `hilbert-kd45n`, `hilbert-ltl`,
`hilbert-lukasiewicz-infinite`, `hilbert-m`, `hilbert-mtl`, `hilbert-mu`,
`hilbert-n`, `hilbert-pal`, `hilbert-product-fuzzy`, `hilbert-r`, `hilbert-s4`,
`hilbert-s42`, `hilbert-s43`, `hilbert-s5`, `hilbert-s5n`, `hilbert-t`,
`ill-exponential-extension`, `imll`, `lambek-l`, `lj`, `nj`,
`reiter-default-extension`, `relevance-e`, `relevance-r`, `relevance-rm`,
`sol`, `tableaux-hybrid-k`, and `tableaux-matrix`.  For each I checked the
declared language and judgment shape, premises, schema/rule status, structural
rules, and side conditions against its body use.  Bibliographic existence and
source identity were checked in `handbook/bib/handbook.bib`, including the
repaired topics at lines 752--760, 1711--1773, 1995--2074, 2242--2269,
4526--4545, and 4835--4938.  The P8 treatment ceilings and cross-part owners
were checked in `spec/registers/depth-gaps.csv:90-122` and line 134.

## Open finding

### F1 — admission blocker — normal ASP is used before definition and outside its registered owner

**Evidence.**  The live table introduces “normal propositional ASP,” “the
Gelfond--Lifschitz reduct,” “stable model,” and credulous/skeptical stable-model
reasoning at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:220-240`, especially
line 233.  No rule grammar, candidate reduct, least-model test, input encoding,
or query convention precedes that row.  The Part VIII generated register has
nonmonotonic and autoepistemic definitions at
`handbook/generated/audit-p08.tex:170-180`, but no ASP or stable-model
definition.  The first live exact definition is instead the later
`def:p09-stable-model` at
`handbook/parts/p09/logic-in-computer-science.tex:379-391`, after which the
complexity statement begins at lines 393--394.  The register is explicit:
`spec/registers/depth-gaps.csv:119` assigns the P8.7 row only default logic,
circumscription, and autoepistemic logic and says “ASP under D-P11-007”; the
latter record assigns answer-set programming to P9 at
`spec/registers/depth-gaps.csv:134`.

**Concrete harm.**  The assertion is not reconstructible from Part VIII.  For
the minimal normal program

\[
 p\leftarrow\mathsf{not}\ q,
 \qquad
 q\leftarrow\mathsf{not}\ p,
\]

the Gelfond--Lifschitz definition gives precisely the stable models
\(\{p\}\) and \(\{q\}\), so \(p\) is credulous but not skeptical.  Nothing
before the table defines the rule arrow, default negation, candidate-dependent
deletion, positive-program least model, or whether the queried object is an
atom, literal, or arbitrary formula.  Those choices are load-bearing: changing
the admitted program syntax, for example from normal to disjunctive programs,
changes the standard complexity boundary.  A citation in the caption cannot
replace the missing local semantics.  The unexplained names also fail the
AGENTS rule's Definition, Standing, Nonredundancy, and Use-at-introduction
conditions.

**Exact correction.**  Apply the registered ownership already recorded by the
project: delete the ASP row at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:233` and delete the
caption's “the normal-program row follows ...” clause at lines 239--240.  The
complete definition and complexity treatment already belongs to Part IX.  If
the row is deliberately retained in Part VIII instead, the non-minimal
alternative is to insert before the table the complete finite-normal-program
grammar, the candidate-indexed Gelfond--Lifschitz reduct, the least-model stable
criterion, and the exact existence/credulous/skeptical input problems, then add
a P8 register owner; a forward definition in Part IX is not
definition-before-use.

**Status:** still open.

## Focused repair verification

### KC, LC, and all three strict inclusions — accept-fixed

`handbook/parts/p08/intuitionistic-supplement.tex:496-537` now defines the two
extensions at their exact strengths and proves the correct chain.  Substituting
\(B=\neg A\) into LC prelinearity and using the two displayed IPL implications
at lines 515--523 yields weak excluded middle, hence
\(\mathsf{KC}\subseteq\mathsf{LC}\).  The converging fork
\(r<a<t, r<b<t\) has a unique greatest point, so validates KC's finite-frame
condition, while the valuations \(V(p)=\{a,t\}\) and
\(V(q)=\{b,t\}\) make both directions of prelinearity fail at \(r\)
(lines 524--531).  The branching IPC countermodel to weak excluded middle and
the two-world linear countermodel to excluded middle at lines 531--537 establish
the outer strictness claims.  The table and diagram at lines 540--578 match the
proof rather than asserting a stronger lattice relation.  The Jankov and
Dummett source records are present at
`handbook/bib/handbook.bib:4526-4545`.

### Lewis spheres and the CA-based VC calculus — accept-fixed

The sphere definition at
`handbook/parts/p08/conditionals-deontic-free.tex:234-276` fixes a nonempty
family linearly ordered by inclusion, closed under arbitrary unions and the
stated nonempty intersections, and gives the correct limit-free existential
sphere truth clause.  Empty spheres are harmless: weak centering quantifies
only over nonempty spheres at lines 255--259, while \(\{w\}\)-centering and
nesting imply that same condition.  The limit assumption is separately and
correctly formulated at lines 264--272.  Thus V, VW, and VC are not conflated,
and centering does not silently impose a least antecedent-permitting sphere.

The exact sheet at
`handbook/registry/calculi/hilbert-counterfactual-vc.tex:1-11` inherits CK and
adds ID, **CA**, CSO, CV, conditional MP for weak centering, and CS for
centering.  In particular, line 7 has
\(((A>C)\land(B>C))\to((A\lor B)>C)\), and the sheet explicitly says CA
replaces the non-equivalent MOD presentation.  The cited completeness statement
at `handbook/parts/p08/conditionals-deontic-free.tex:322-329` is limited to the
centered, limit-free semantics actually defined.  This matches Lewis's
completeness result (DOI `10.1111/j.1755-2567.1971.tb00061.x`) and Wen's
correction of the Nute-style axiomatization
([arXiv:1910.06202](https://arxiv.org/abs/1910.06202)); the corresponding
bibliography records are exact at `handbook/bib/handbook.bib:1711-1755`.

### Nondeterministic Büchi semantics — accept-fixed

`handbook/parts/p08/temporal-epistemic-supplement.tex:353-380` types
\(\delta:Q\times\Sigma\to\mathcal P(Q)\), defines a run by membership in the
transition set, defines \(\operatorname{Inf}(r)\), and accepts iff **there
exists** a run visiting an accepting state infinitely often.  Singleton-valued
transition sets are then correctly isolated as the deterministic
specialization.  The semantics therefore matches the existential run choice
used by the LTL automata card and does not accidentally present a deterministic
or universal-run automaton.  The Büchi and Vardi--Wolper records appear at
`handbook/bib/handbook.bib:2242-2269`.

### Total smooth dyadic semantics — accept-fixed

At `handbook/parts/p08/conditionals-deontic-free.tex:139-178`, the preference
relation is a total preorder on the typed accessible set \(R(w)\), with the
orientation and strict part stated explicitly.  Smoothness is restricted to
formula-definable candidate sets and guarantees a best candidate whenever that
set is nonempty.  `Best` is total as a set-valued operation, including the
empty-candidate case, and the explicit existence conjunct at lines 164--171
makes impossible-condition obligations false rather than vacuously true.  The
scope paragraph correctly distinguishes this selected binary preference
semantics from all dyadic deontic logics and from \(O(B\to A)\).

### Finite measure-rich probability boundary — accept-fixed

The theorem at
`handbook/parts/p08/conditionals-deontic-free.tex:437-452` states only the
finite Boolean-algebra/fixed-event result it proves.  For four positive atom
masses \(x,y,z,t\), an event has one fixed subset-sum polynomial while
\(P(B\mid A)=x/(x+y)\).  Varying the split between \(z,t\), and then \(x,y\)
with their sum fixed, excludes every subset.  The theorem expressly retains
finiteness (or an explicit measure-rich extension hypothesis), strict
positivity, a fixed event, and membership in the same algebra as essential
boundaries; it does not overstate this elementary witness as every version of
Lewis triviality.  The cited Lewis article and DOI are present at
`handbook/bib/handbook.bib:1765-1773`.

### KLM order and smoothness — accept-fixed

`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:149-172` now defines
\(\prec\) as an irreflexive and transitive strict partial order, defines
minimality, restricts smoothness to formula-definable sets, and distinguishes
smooth preferential models for System P from totally layered ranked models for
Rational Monotony.  The representation claims do not infer ranking from mere
minimal-point existence.  The KLM and Lehmann--Magidor records and DOIs are
present at `handbook/bib/handbook.bib:2015-2034`.

### Nonempty group convention — accept-fixed

The convention is local and unambiguous at
`handbook/parts/p08/group-operator-convention.tex:1-8`: every epistemic group
on this route is a nonempty finite subset of the agent index set, while the
mathematically coherent empty-group identities are explicitly outside the
fixed language.  This agrees with the common-knowledge sheet's language and
all three side conditions at
`handbook/registry/calculi/hilbert-common-knowledge.tex:2-6`.  There is no
empty-conjunction or length-zero-path edge case left inside the calculus.

### AGM revision and contraction — accept-fixed

The operations and expansion are typed at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:246-263`.  The eight
revision postulates at lines 265--283 have unconditional Inclusion, put the
consistency hypothesis exactly on Vacuity, and state the two conjunction
postulates in the correct directions and with the correct condition.  The
eight contraction postulates at lines 286--307 correctly exclude tautologies
from Success and state Recovery, conjunctive overlap, and conjunctive inclusion.
Levi and Harper are correct at lines 310--316.  Finally, the finite-signature,
consistent-\(K\), faithful-total-preorder hypotheses and the inconsistent-input
edge case are explicit at lines 324--356; database update, iterated revision,
and base revision are excluded.  The AGM and Katsuno--Mendelzon bibliography
records are at `handbook/bib/handbook.bib:1995-2013`.

### da Costa \(C_1\) — accept-fixed

The body fixes one exact calculus, defines
\(A^\circ=\neg(A\land\neg A)\), and gives its object-language standing and
contrast with LP at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:72-93`.  The complete
15-postulate source presentation, uniform substitution, and modus ponens are on
`handbook/registry/calculi/hilbert-da-costa-c1.tex:1-18`.  Unrestricted
explosion is not claimed, while controlled explosion has the additional
\(A^\circ\) premise at body lines 95--108.  The comparison table at lines
110--132 correctly distinguishes LP's designation-based nonexplosion from
\(C_1\)'s formula-level consistency recovery.  This matches the source
identified at `handbook/bib/handbook.bib:752-760`.

### Affine apparatus — accept-fixed

The selected-system boundary at
`handbook/parts/p08/relevance-linear-supplement.tex:528-545` fixes precisely
commutative affine ILL: the IMLL language and exactly-one-succedent judgment,
finite-multiset antecedents, all IMLL rules, unrestricted left weakening,
exchange built into the contexts, and no contraction.  The registry sheet says
the same and displays the only added rule at
`handbook/registry/calculi/affine-ill.tex:1-5`; Cut is inherited and no new
adequacy or cut-elimination theorem is claimed.  The family qualifiers in the
tables/structural map therefore do not turn this selected presentation into a
claim about every affine logic.  The Lincoln source is exact at
`handbook/bib/handbook.bib:4927-4938`.

## Complete lot coverage

### Lot 1 — checked clean

I checked the inherited and supplemental IPL/IQC languages and consequence
relations; Kripke persistence and expanding-domain quantifier clauses; the IPL
soundness/completeness and disjunction/existence-property boundaries; BHK and
realizability standing; Gödel--Gentzen, Kolmogorov, Kuroda, and Glivenko scope;
Heyting-algebra and topological semantics; intermediate systems including the
KC/LC repair; Markov and constant-domain principles; all LJ/NJ/SOL references;
and every local proof/countermodel.  Definitions precede their uses and no
constructive principle is promoted beyond its stated hypotheses.

### Lot 2 — checked clean

I checked the normal modal cube and exact Hilbert extensions; correspondence
claims and countermodels; canonical-model and filtration arguments;
Sahlqvist/canonicity scope; standard translation and bisimulation invariance;
neighborhood semantics for non-normal systems; actuality/two-dimensional
indexing; Thomason/incompleteness boundaries; and quantified-modal actualist
quantifiers, existence predicates, and constant/increasing/decreasing-domain
Barcan directions.  The canonical completeness annex is correct for K, KT,
S4, and S5 at its stated propositional scope.  No frame condition or domain
hypothesis is omitted from a theorem that uses it.

### Lot 3 — checked clean

I checked LTL, CTL, CTL*, and modal \(\mu\)-calculus syntax, path/state typing,
fixed-point polarity, unfolding/induction principles, and complexity/status
boundaries; Kamp and automata translations; the repaired Büchi definition;
multi-agent S5, distributed and common knowledge, noncompactness, muddy
children, PAL reduction, and hybrid nominals/@/binder boundaries; CK selection
semantics, Stalnaker selection, Lewis spheres and VC; monadic and repaired
dyadic deontic semantics; contrary-to-duty examples; and positive/negative
free-logic quantifier and denotation conventions.  The nonempty-group policy is
consistent across prose, semantics, and sheet.

### Lot 4 — checked clean except F1

I checked K3, LP, FDE, weak Kleene, Bochvar, Post, finite and infinite
Łukasiewicz, MTL/BL/Gödel/product, matrix tableaux, t-norm and standard
completeness qualifications, and supervaluation consequence; the annex proofs
of K3's absence of tautologies, LP's classical tautologies, and K3--LP duality;
relevance E/R/RM syntax, Routley--Meyer clauses, frame conditions,
variable-sharing, decidability/undecidability boundaries, and the source-exact
E distribution schema; IMLL/CLL/exponentials, units and the empty-context
erratum, phase semantics, focusing, decision boundaries, Lambek L, and the
repaired affine comparison; LP versus da Costa \(C_1\); adaptive-logic status;
Reiter defaults, circumscription, autoepistemic expansions, KLM preferential
and ranked consequence, and AGM.  The only exception is the undefined ASP row
in F1.  The `relevance-e` schema was checked directly against Dunn and Restall's
scholarly source rather than normalized into a different-looking distributive
law ([source PDF](https://consequently.org/papers/rle.pdf)); its present form is
source-exact.

## Coverage disposition

| Charter lot | Disposition | Residual |
|---|---|---|
| 1. Intuitionistic/intermediate/IQC/semantics | checked clean | none |
| 2. Modal/correspondence/QML | checked clean | none |
| 3. Temporal/epistemic/hybrid/conditional/deontic/free | checked clean | none |
| 4. Many-valued/substructural/paraconsistent/nonmonotonic/apparatus | checked with blocker | F1 only |

No routed source, supplement, annex unit, referenced sheet, P8 ceiling, or
relevant bibliography role was left unchecked.  Admission remains rejected
until F1 is removed or fully defined and registered before use.
