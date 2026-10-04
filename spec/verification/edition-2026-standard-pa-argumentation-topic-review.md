# Standard PA checker and finite argumentation: independent topic review

Review date: 7 September 2026. Review context: fresh blind topic specialist.
Repository: `C:\Dev\the-methods-of-reason`.
Observed branch: `phase4-codex`.
Observed HEAD: `35d537c692bb74b532dc4aa750da381a7fe4daf2`.
The four target files are untracked additions in the live checkout; their
identities for this review are the frozen SHA-256 values below.

## Verdict

**PA numerical unit: PASS. Finite argumentation unit: PASS.**

Every line of both bodies and both annexes was read. No mathematical
counterexample, missing proof case, or unsupported mathematical conclusion was
found within their stated scope. The review checked the active PA axiom
definition, the exact syntax and substitution implementation, the inherited
twenty-rule numerical derivation checker, and the actual quantifier/equality
rule definitions. All six finite frameworks were independently recomputed from
their complete attack relations by enumerating their subsets.

The exact arithmetic formula for the direct PA checker, internal D2, and
internal D3 are **UNRESOLVED, explicitly subsequent work**. Neither the numerical
primitive-recursion proofs nor the certificate bridge closes those obligations.

This is the topic-specialist gate. Source acquisition and source attribution,
rendered output, static/build validation, separate admission, and final
publication acceptance require their own evidence. This review performed no
manuscript edits, builds, rendering, or subdelegation. It read no other new
review reports or author conclusions before filing.

## PA claims

References in this section use `PA body` for
`handbook/parts/p05/standard-pa-proof-predicate.tex`, `PA annex` for its annex
counterpart, and `coding` for
`handbook/restoration/inherited-09328-09438.tex`.

| Claim | Verdict | Evidence and mathematical check |
| --- | --- | --- |
| The seven actual arithmetic axiom codes | PASS | PA body 15-43 and PA annex 8-42. Each constructor expression decodes under coding 24-64 to the corresponding active Q axiom in `inherited-09099-09111.tex` 1-13. The distinct variables in the predecessor axiom remain distinct after binding. The two-variable closures in q2, q5, and q7 have the declared outside-in order. Negated equality, addition recursion, and multiplication recursion agree literally. |
| Canonical free-parameter list and closure | PASS | PA body 45-62; PA annex 92-107. An occurring variable index is below its constructor/argument-list code and hence below the formula code. The scan `j < m` includes every free index, once and in order. List reversal followed by wrapping implements precisely the displayed outside-in universal prefix. Invalid formulas have the stated zero default. |
| Induction constructor, absent induction variable, and shadowing | PASS | PA body 64-81, 149-171; PA annex 45-90. Self-substitution is literal identity. Substitution of 0 and Sx_i cannot invoke fresh renaming: an x_i binder stops substitution, and every different binder is absent from those replacement terms. Thus both displayed free-variable identities hold, as do FV(I(theta,i)) = FV(theta) minus {x_i} and Var(I(theta,i)) = Var(theta) union {x_i}. This covers arbitrary bound-variable shadowing and matrices with no free x_i. |
| Literal axiom recognition and exact accepted set | PASS | PA body 84-109, 111-117; PA annex 109-139. The induction core starts with implication, so maximal leading-universal stripping recovers exactly its parameter prefix. The implication's right child determines i and m. Reconstructing IndAx(m,i) and demanding literal equality establishes both inclusion directions. The recovered matrix and index are bounded by the input code. Reordered, repeated, omitted, and extra parameters fail the explicit prefix comparison. |
| Primitive recursiveness and totality of the new axiom operations | PASS | PA annex 92-131. Syntax recognition, free-variable lists, total substitution, and list operations have numerical constructions in coding 85-222. F uses a bounded scan; U uses list-length-many updates; IndAx uses composition; the recognizer uses bounded prefix stripping and literal tests. Its malformed-input defaults are present. Reconstruction can produce large numbers without invalidating primitive recursiveness. |
| Actual closure-order derivations in both directions | PASS | PA annex 141-169. Instantiating each prefix binder with its own variable removes it by the literal self-substitution identity. Generalizing in the reverse order of the desired list gives exactly that closure. Each universal-introduction side condition holds because the sole open assumption is the original sentence. Empty, repeated, and vacuous prefix binders are covered. The four-step example in PA body 157-162 has the correct order. |
| Insertion into complete ND derivations, including strong exists-E freshness | PASS | PA annex 171-195. Only surviving open axiom occurrences are replaced. New leaves are unmarked; old discharge witnesses therefore remain and no new labelled discharge is introduced. New leaves are sentences, preserving forall-I. For source-to-canonical induction transport the new leaf's all-variable set is a subset of the replaced source leaf's set. In the reverse direction the proof chooses an allowed source closure over exactly the free parameters, giving equal sets. The old exists-E eigenvariable consequently remains absent from every remaining open formula; its major formula and conclusion are unchanged. This establishes the stronger actual rule condition, rather than relying on closedness alone. |
| Effective, primitive-recursive proof transport | PASS | PA annex 197-215. Each replacement chain has at most 2p quantifier steps for input record code p; the resulting row count is at most n(1+2p). Child-block construction, index shifts, concatenation, and parent-row construction are bounded list operations. The proposed row-table computation supplies an implementation, without proof search. The reverse direction for the active PA scheme may choose its already permitted canonical closure. |
| Total direct numerical proof checker | PASS | PA body 174-207; PA annex 226-252. Exact outer tag 19, arity two, zero certificate field, tag-15 nonempty row record, all row tests, tree parent counts, sentence root, literal root equality, and direct testing of precisely the final surviving leaf list are present. Invalid inputs return zero. The empty open list passes its empty product. |
| All twenty inference rules | PASS | PA body 185-206 explicitly incorporates coding 224-319. PA annex 229-237 gives the correct twenty premise arities and parameter-list lengths. The detailed rule-by-rule audit appears below. |
| Both standard numerical proof-meaning directions | PASS | PA annex 254-274. A successful record reconstructs a finite ND tree with exactly the computed surviving assumptions; direct axiom recognition and the source transport produce a PA derivation. A source derivation transports in the other direction, retains its inference witnesses and discharge labels, and serializes into an accepted tag-19 record. The sentence restriction is stated for this theorem; the earlier axiom-presentation equivalence also allows formula conclusions. |
| Axiom proofs and empty-context proofs | PASS | PA body 209-221. The one-row q_j assumption has parameters, premises, and marker as required. The tag-18 rule row for 0 = 0 is premise-free identity introduction with parameter [o]; it has no surviving assumptions. A nonzero second outer field fails independently of the context. |
| Bridge to the c.e.-certificate convention | PASS | PA body 233-237; PA annex 276-302. A successful tag-16 code yields source axiom leaves using the existing domain-index and Comp theorem; the proved transport produces tag 19. Conversely, each of finitely many open source leaves belongs to the fixed program's domain, so the established bounded-verification theorem supplies a finite accepting history. Histories are placed in final open-list order, with W = 0 for no leaves. This proves existence in both directions; it claims no primitive-recursive compiler of histories for an arbitrary domain index. Injective constructor tags make the positive code sorts disjoint. |
| Exact arithmetic formula selection and internal D2/D3 | UNRESOLVED | PA body 243-252 and PA annex 304-314 explicitly leave the finite graph-description selection, internal invariants, internal modus ponens, and evidence-to-proof construction for the subsequent scope. The present PASS does not discharge them. |

The source-presentation argument uses the active PA definition in
`handbook/parts/p05/diagonalization.tex` 48-58: all induction instances with
universally closed parameters are available. Its reverse insertion proof
explicitly chooses the source instance with exactly the free parameter set.
That choice is necessary to the stated all-occurrence freshness argument.

### Twenty-rule audit

The following list was checked against the full inherited numerical definition
and the actual `handbook/registry/calculi/nd-fol.tex` rule sheet. The numerical
checker uses the body order for implication elimination, and the inherited
definition explicitly supplies the exchange from the sheet's opposite order.

| Tag | Rule | Premises | Parameters | Audited condition |
| --- | --- | ---: | ---: | --- |
| 0 | assumption | 0 | 0 | Its own leaf index is the open list; zero denotes unmarked and positive marker l denotes label l-1. |
| 1 | and-I | 2 | 0 | Ordered premises are exactly the two conclusion conjuncts. |
| 2 | and-E1 | 1 | 0 | Select exactly the first conjunct. |
| 3 | and-E2 | 1 | 0 | Select exactly the second conjunct. |
| 4 | or-I1 | 1 | 0 | Premise equals exactly the first disjunct. |
| 5 | or-I2 | 1 | 0 | Premise equals exactly the second disjunct. |
| 6 | or-E | 3 | 2 | Major disjunction and two identical minor conclusions; nonvacuous, formula-specific discharge separately in the two minor branches. |
| 7 | implies-I | 1 | 1 | Conclusion antecedent identifies the formula removed by the nonvacuous labelled discharge. |
| 8 | implies-E | 2 | 0 | Body premise order is phi, phi implies psi; conclusion is psi. |
| 9 | not-I | 1 | 1 | Bottom premise; discharge exactly the labelled conclusion-negand assumptions, nonvacuously. |
| 10 | not-E | 2 | 0 | Premises phi and not-phi; conclusion bottom. |
| 11 | bottom-E | 1 | 0 | Bottom premise and any well-formed formula conclusion. |
| 12 | RAA | 1 | 1 | Bottom premise; nonvacuously discharge labelled negations of the conclusion. |
| 13 | forall-E | 1 | 3 | Supplied index, formula matrix, and term; exact quantified premise and computed substitution conclusion. |
| 14 | exists-I | 1 | 3 | Same typed witnesses; exact computed substitution premise and existential conclusion. |
| 15 | forall-I | 1 | 1 | Exact quantification of the premise; generalized index absent from every open assumption's free-variable list. |
| 16 | exists-E | 2 | 4 | Typed matrix/index/eigenvariable/discharge label; exact substituted minor assumptions, nonvacuous discharge, and eigenvariable absent from the major formula, conclusion, and every remaining open formula's all-variable list. |
| 17 | alpha | 1 | 0 | Both formulas pass type tests and their syntactic alpha-comparison records agree. |
| 18 | identity-I | 0 | 1 | Supplied term and literal t = t conclusion; empty open list. |
| 19 | identity-E | 2 | 4 | Supplied terms, matrix, and index; equality premise and both exact computed substitution instances; no free-occurrence requirement. |

Every nonassumption marker must be zero. Every row formula and every supplied
formula/term parameter is checked for its required type. Earlier references and
the single-parent conditions preclude cycles, sharing, and disconnected rows;
the last row is the unique root. These conditions establish the tree and open
occurrence invariant used in both proof-meaning directions.

## Finite argumentation claims

References use `argumentation body` for
`handbook/parts/p18/finite-argumentation.tex` and `argumentation annex` for its
annex counterpart.

| Claim | Verdict | Evidence and mathematical check |
| --- | --- | --- |
| Framework, attack, conflict, defense, characteristic operator, admissibility | PASS | Body 20-64. Domains are explicit; empty argument sets and self-attacks are allowed. The conflict-free equivalence S intersect S+ = empty includes self-conflict. Defense does not require membership, and unattacked arguments are defended even by the empty set. |
| Monotonicity and all claims in the first proof item | PASS | Body 66-77; annex 9-40. Enlarging S enlarges its attack set. An attack a to b inside F(S) produces s and t in S with attacks s to a and t to s, contradicting conflict-freeness, including a = b. Monotonicity then proves admissibility of F(S), admissible enlargement, and preservation of previously defended arguments. |
| Four extension definitions; maximal versus maximum; least versus minimal | PASS | Body 82-108. Preferred maximality is inclusion maximality. Least fixed-point terminology quantifies over all fixed points. Complete extensions retain admissibility and include every defended argument. The unequal-size example correctly witnesses distinct cardinalities of preferred extensions. |
| Finite grounded iteration and complete fixed points | PASS | Body 110-124; annex 42-79. The empty base is admissible, each iterate stays admissible, and the chain increases. No equality for all indices 0 through n would require n+1 strict increases. Induction against any fixed point, even a conflicting one, establishes leastness. Complete is equivalent to conflict-free fixed, and the grounded member of the complete family establishes the intersection equality. |
| Procedure and evaluation count | PASS | Body 126-137; annex 71-77. Each pass computes exactly the characteristic operator. Equality is detected at G_k on the (k+1)-st evaluation, so at most n+1 evaluations suffice. For A empty the first evaluation is the final equality check. The text correctly avoids equating this count with total runtime. |
| Preferred existence, preferred completeness, and stable inclusion | PASS | Body 139-157; annex 81-118. Largest cardinality among the finite admissible supersets provides an inclusion-maximal superset. Fundamental enlargement proves preferred completeness. Stability defends each member and precludes any conflict-free proper superset, proving preferredness. S = A minus S+ is equivalent to stability in both directions. |
| Fixed-point conflict warning | PASS | Body 159-165 and 212-216; annex 146-154. The singleton self-attacker is fixed and conflicting; only the empty set is admissible. This prevents silently dropping conflict-freeness from completeness. |
| All six complete extension lists | PASS | Body 170-246; annex 120-201. Independent exhaustive subset calculations from the stated edges agree with every family, grounded sequence, admissible list, and characteristic value supplied in the proofs. Results are recorded below. |
| Guarded credulous and skeptical queries | PASS | Body 251-274. The nonempty-family guard is explicit. An empty family produces no extensions and no acceptance labels; a family containing the empty extension is distinct. The shared case has preferred intersection {d} and grounded extension empty, as claimed. |
| Interpretation and coverage limits | PASS | Body 12-15 and 276-289. Argument identifiers and attack edges carry no premises, truth assignment, speaker reliability measure, or empirical evidence. The stated extension results entail only the defined graph properties. The finite chapter accurately limits its mathematical coverage. |

### Independent recomputation of the six graphs

For each complete edge list in body 175-186, the recomputation enumerated every
subset of the listed argument set. It formed outgoing targets from edges,
tested conflict directly, computed defense by quantifying over incoming edges,
and independently filtered for admissible, complete, inclusion-maximal
admissible, and stable sets. It also iterated defense from the empty set until
equality. This was a direct finite mathematical calculation in an ephemeral
tool cell; no source files or regression tests were created.

Write `0` for the empty set in the following table; braces outside sets denote
the extension family.

| Framework | Admissible sets | Complete family | Preferred family | Stable family | Grounded stages through first equality |
| --- | --- | --- | --- | --- | --- |
| chain | 0, {a}, {a,c} | {{a,c}} | {{a,c}} | {{a,c}} | 0, {a}, {a,c}, {a,c} |
| pair | 0, {a}, {b} | {0, {a}, {b}} | {{a}, {b}} | {{a}, {b}} | 0, 0 |
| self | 0 | {0} | {0} | empty family | 0, 0 |
| empty | 0 | {0} | {0} | {0} | 0, 0 |
| size | 0, {a}, {b}, {c}, {b,c} | {0, {a}, {b,c}} | {{a}, {b,c}} | {{a}, {b,c}} | 0, 0 |
| shared | 0, {a}, {b}, {a,d}, {b,d} | {0, {a,d}, {b,d}} | {{a,d}, {b,d}} | {{a,d}, {b,d}} | 0, 0 |

The recomputation also found conflicting fixed points where relevant:
{a,b} for pair, {a} for self, {a,b,c} for size, and {a,b,c,d} for shared.
The manuscript does not claim these are complete extensions. For shared,
F({a}) = F({a,d}) = {a,d}, symmetrically for b, and the preferred intersection
is exactly {d}. For size, {a} and {b,c} are both preferred with sizes one and
two. These checks cover the distinctions used in the text.

## Read manifest and frozen identities

All paths below are relative to `C:\Dev\the-methods-of-reason`. A full-file
SHA-256 identifies each dependency even when the review read only the stated
range. Search-result snippets were used to locate dependencies; they were not
substituted for the full reads of the four targets.

| File | Lines read | File lines | SHA-256 |
| --- | --- | ---: | --- |
| `spec/EDITION-2026-CONTRACT.md` | 1-168, full | 168 | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | 1-252, full | 252 | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | 1-315, full | 315 | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/parts/p18/finite-argumentation.tex` | 1-289, full | 289 | `685A2D6BF0125A07A5C85AEC0DA22CA9866B9799202750C758CA8BC1062C85AC` |
| `handbook/annex/p18/finite-argumentation.tex` | 1-201, full | 201 | `1B70FD5FA52B42BBCBA76976D484A0E2DFD1A67EDEEDDD1BB5D88713F9509BAA` |
| `handbook/restoration/inherited-09328-09438.tex` | 1-546, full | 546 | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/parts/p05/diagonalization.tex` | 1-71 | 349 | `63DC7704391E0CFD6C9BFA07465B0DFA905112F612F57A0B35932F2810C9DFB4` |
| `handbook/restoration/scope-SRC-09099-09111.tex` | 1-3, full | 3 | `56C8378D1D04F699B89EEDC85851E8DA68C675C414A62E1E17342EC042A4DE9F` |
| `handbook/restoration/inherited-09099-09111.tex` | 1-13, full | 13 | `38534E090C35DB78D99D045D19B3C7F34F1F1AAA8999CF118C7A416CD41D9D2B` |
| `handbook/restoration/inherited-03240-03428.tex` | 1-189, full | 189 | `36D7779D6B9BB3CAF0C4EF514A79A1C7D8AA10BD4A72290256EA1D09D5DB58CC` |
| `handbook/restoration/inherited-03927-04061.tex` | 1-135, full | 135 | `2AD2846970D4976177B0FBB8AC59FF8106253F5D155A5E4861956F7F651BF480` |
| `handbook/registry/calculi/nd-fol.tex` | 1-29, full | 29 | `F25549BC18FC4AAE212EEA32CADC9FFFD08E03D712F5DF10E9DA62F660BE5370` |
| `handbook/restoration/inherited-08710-08876.tex` | 805-907 | 1104 | `4D131A6631A148354F31066316E3B73977DF71AF66C06FC98158D6C402DBC102` |

The bounded-verification theorem and its proof were read to check the bridge's
use of the existing result. This report does not re-review every earlier
machine/history construction on which that theorem depends. No external
source body was needed for this mathematical review; primary-source fidelity
is the independent source review's scope.

The four target hashes were verified at entry and again after the mathematical
read. The report's own SHA-256 is returned with its handoff, outside the file,
so that the report does not purport to contain its own fixed-point hash.
