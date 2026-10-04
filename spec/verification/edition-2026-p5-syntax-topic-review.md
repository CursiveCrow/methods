# Edition 2026 P5 syntax arithmetization: independent topic review

Date: 7 September 2026. Role: independent mathematical topic reviewer.

## Verdict and scope

The explicit syntax construction, annotated ND derivation checker, certified
c.e. axiom checker, and both directions of the displayed standard-model
arithmetization theorem **PASS** the assigned mathematical review. The supplied
reader text has one localized **FAIL**, P5-TOP-01 below: its explanation of the
Sigma1 classification assumes an initial existential block that the preceding
choice of representing formula does not require. The classification itself is
correct by the actual hierarchy's closure rule, so this defect has a direct
local repair and does not invalidate the coding theorem.

Accordingly, the complete 519-line unit is not yet an unqualified topic-review
pass. The cited Q representation theorem and internal derivability obligations
retain their separate standing. No source acquisition, external-source
acceptance, formal admission, build, rendered-page inspection, or release
acceptance is established by this report.

The frozen reader file is
`handbook/restoration/inherited-09328-09438.tex`, SHA256
`87c2203ae4f94d78b973b592c9ca88013e7ef0641410e512b45c79a680ab9903`.
All its lines 1–519 were read. The author note was used to identify the claimed
scope and dependencies, not as evidence that its mathematics was correct.
The reviewer read no other new P5 review and discussed no findings before
filing this report. No manuscript, code, registry, or provenance file was edited;
the sole owned output is this report. The only numerical recomputation was a
small independent calculation of constructor and illustration codes.

## Component outcomes

| Component | Outcome | Mathematical assessment |
| --- | --- | --- |
| Arithmetic grammar and typed encodings | PASS | All four arithmetic function symbols, equality, bottom, primitive connectives, and both quantifiers are covered with exact tags and arities. |
| Injectivity, list inverses, projections, malformed inputs | PASS | Positive cons gives strict component descent; tags and arities distinguish the sorts and constructors; all invalid expression inputs have stated defaults. |
| Primitive recursion for syntax, variables, strings, and parsing | PASS | The accumulated row construction supplies course-of-values recursion; the explicit monotone bound B supports bounded parsing search. |
| Numerals and numeral substitution | PASS | Numeral formation is direct recursion; a closed replacement never requires binder renaming. |
| General substitution and frame bound | PASS | The preliminary renaming implements the exact least-fresh clause, preserves shape, and does not recurse into inserted terms. The quadratic bound is adequate for the specified macro-step convention. |
| Alpha comparison, both directions | PASS | Distinct free tags and nearest-binder positions preserve binding information; common globally fresh binder names give the converse. |
| Tree records and all 20 ND rules | PASS | Every actual rule form has the needed parameters and checks. Labels, branch ownership, nonvacuity, equality matrices, and quantifier side conditions agree with the core rules. |
| Finite axioms and axiom instantiation | PASS | Membership is membership in the fixed finite list of sentences. Universal instances use real forall-E steps and their supplied terms. |
| Fixed c.e. domain index and PR Comp evaluation | PASS relative to the accepted P4 interface | The domain convention matches P4. The fixed marked-bounded formula has a PR evaluator; no bound on obtaining an accepting witness is assumed. |
| Surviving leaves and certificates | PASS | The root open-occurrence list determines exactly the certificate positions; discharged leaves need none; empty lists are handled. |
| Proof-code-to-derivation direction | PASS | Row induction reconstructs the tree and its exact open leaves; accepted Comp truth puts every surviving leaf in T. |
| Derivation-to-proof-code direction | PASS | Postorder encoding supplies annotations; finitely many open T leaves obtain accepting histories from the accepted Comp theorem. |
| Separation of numerical and arithmetic proof predicates | PASS | The numerical checker theorem does not purport to prove the cited numeralwise Q representation or internal derivability. |
| Sigma1 classification of Prov_T | PASS for the conclusion; FAIL for the stated block-merging rationale | The declared hierarchy is closed under existential quantification, but the chosen representative need not begin with an existential block. See P5-TOP-01. |
| Complete Q representation proof and internal D1–D3 for the chosen predicate | UNRESOLVED as separate obligations | These are not proved or accepted through the standard-model coding argument. The representation theorem remains cited; downstream internal claims require their own evidence. |

## P5-TOP-01: an unrequired prefix shape is used in the explanation

**Location:** `handbook/restoration/inherited-09328-09438.tex:477–486`,
especially lines 484–485. **Outcome:** FAIL for this explanatory assertion;
the resulting Sigma1 classification is correct.

Lines 477–480 choose a specific Sigma1 formula numeralwise representing the
numerical proof relation. Neither that choice nor the cited theorem requires
the formula to begin with an existential block. The actual syntactic hierarchy,
`inherited-08306-08438.tex:61–94`, admits conjunctions, disjunctions and marked
bounded quantification as well as unbounded existential quantification; it is
not restricted to a displayed existential prefix followed by a bounded matrix.

A concrete allowed choice shows the problem. Given any permitted representative
`rho_0(p,x)`, the formula `(0=0) and rho_0(p,x)` is another Sigma1 numeralwise Q
representative of the same numerical relation. Q proves `0=0`, so both positive
and negative numeralwise representation clauses are preserved. This permitted
choice begins with a conjunction. There is no initial existential block into
which the new quantifier literally merges.

The necessary correction is confined to the rationale: invoke closure of the
declared Sigma1 class under unbounded existential quantification. For example,
“The declared Sigma1 class is closed under unbounded existential
quantification, so Prov_T is a Sigma1 formula.” This uses
`inherited-08306-08438.tex:79–82` directly. No prefix transformation, exchange
of bounded and unbounded quantifiers, or Q equivalence theorem is needed.
An alternative would be to impose and justify a suitable prefix on the selected
representative, but that adds work with no benefit to this conclusion.

## Construction checks and independent reasoning

### Lists, constructors, and bounded syntax operations

For positive `c`, inversion of `c-1` under Cantor pairing determines unique
`h(c), t(c)`, both strictly below `c`. Iterating the tail therefore reaches zero
in at most `c` steps. This proves both existence and uniqueness of the raw list
decoded from every natural, including `0` as the empty list. A tree child's
code lies below its argument-list code and then below its constructor code.
The simultaneous term/formula recognition rows therefore only read earlier
rows; the same invariant supports spelling, node count, Var and FV.

Tags 0–4 are terms, tags 5–12 formulas, 13 symbols, and 14 strings. The
arithmetic constant 0 has code `N_1()=2`, the variable x_0 has code
`N_0(0)=3`, and bottom has code `N_6()=22`. Thus none is the empty raw list.
The number `N_2()=4` is a concrete malformed expression: it has the successor
tag with zero arguments. The canonical empty string has code `N_14(0)=122`;
it is a string but no term or formula. Independently, `0=0` has code 523.
These calculations check distinctions in the supplied conventions; they are
not a finite test presented as proof of injectivity.

The list operations are bounded recursions on their supplied list lengths.
Appending accumulated rows can produce enormous numbers, but the primitive
recursion definition does not require a separate size bound on intermediate
values. Accessing a prior row by its bounded index is already PR. This avoids
using mere termination as a substitute for a primitive-recursion proof.

For the parser, take `b >= q+16`. Tags are at most 12, numerical variable
indices at most q, and all argument lists have length at most two. Monotonicity
of C bounds such lists by `L_2(b)` and their constructors by
`C(14,L_2(b))`. Since a canonical spelling with k tokens has at most k tree
nodes, induction on height gives the displayed `B(k,q)` bound. Searching the
bounded interval and checking canonical spelling is therefore PR. Unique
readability gives uniqueness, with zero as a safe failure result because zero
is no expression code. The empty-string convention q=0 is consistent.

### Substitution and alpha equivalence

The numeral routine agrees literally with the P2 substitution clauses: it
stops below the target binder and otherwise commutes with quantifiers because
the replacement has no variables.

For arbitrary replacement t, preliminary renaming uses the least index outside
`Var(psi) union Var(t) union {i,j}`. A bound of one plus the maximum of this
nonempty finite union suffices. The fresh variable is absent from the whole
matrix, so the preliminary `[x_z/x_j]` pass stops under another x_j binder and
cannot require another capture repair. It changes variable names and preserves
the entire term/formula tree shape.

The main traversal enters at most n nodes of the original tree. A returned
copy of t is treated as an already produced code, so its internal nodes do not
create new main visits. There are at most n preliminary passes, each through
at most n nodes. Each visit requires a fixed number of entry, child-return,
assembly, or continuation transitions; arity is at most two. Grouping the PR
tag/projection/Var/fresh-search work into one update, as the text explicitly
does, supports the conservative `20(n+1)^2` iteration bound. This is a bound
on PR macro updates, not on machine transitions, arithmetic bit operations,
or intermediate code magnitudes. That distinction is sufficient for the
claimed PR closure argument.

An edge case checks the exact deterministic operation. In the substitution
`(forall x_1 (x_1=x_1))[x_1/x_0]`, x_0 is absent freely. The P2 third
quantifier clause still fires and chooses x_2, giving
`forall x_2 (x_2=x_2)`. The new traversal does this. A shortcut that returned
the original formula merely because x_0 was absent would have checked a
different operation. With a numeral replacing x_0, no renaming occurs.

For alpha records, `forall x_0 exists x_0 (x_0=x_1)` and
`forall x_2 exists x_3 (x_3=x_1)` have the same record: the left occurrence
has nearest-binder position 0 and the right occurrence is free x_1.
Replacing x_3 on the left in the second formula by x_2 instead gives bound
position 1, so the records differ. This checks shadowing and preservation of
free variables. In general each permitted fresh-renaming generator preserves
the record. In the reverse direction, select distinct common binder names
outside both original Var sets and rename outside inward; unused chosen names
stay absent at each relevant step. Equal records then give literally identical
renamed formulas. Constructor congruence and equivalence complete both
directions of the source's syntactic alpha relation.

### Rule-by-rule correspondence

The table below checks all 20 tags against the actual body and registry.
“Common check” means exact formula/term types, parameter length, premise
arity, earlier references, and zero marker at a nonassumption row.

| Tag | Rule | Checked correspondence beyond common checks |
| --- | --- | --- |
| 0 | assumption | No children or parameters; exactly its own leaf index is open; zero and positive markers encode unmarked and labelled assumptions. |
| 1 | and-I | Two premises in the ordered conjunct positions; open lists concatenate. |
| 2 | and-E1 | One conjunction premise; conclusion is its first child. |
| 3 | and-E2 | One conjunction premise; conclusion is its second child. |
| 4 | or-I1 | Premise is the first disjunct of the conclusion. |
| 5 | or-I2 | Premise is the second disjunct of the conclusion. |
| 6 | or-E | Three premises: disjunction and two identical conclusions; each specified label discharges at least one matching disjunct leaf in its own minor branch. |
| 7 | implication-I | One premise and supplied label; discharges exactly matching antecedent leaves, with nonvacuity. |
| 8 | implication-E | Body order is antecedent then implication. Registry order is implication then antecedent; the supplied two-child permutation is exact. |
| 9 | negation-I | Bottom premise; supplied label removes at least one open occurrence of the negated formula. |
| 10 | negation-E | Formula then its negation; conclusion bottom. |
| 11 | bottom-E | Sole bottom premise; arbitrary well-formed conclusion. |
| 12 | RAA | Bottom premise; at least one matching labelled negation of the conclusion is discharged. |
| 13 | forall-E | Supplied variable, matrix and term; quantified premise and exact computed capture-avoiding instance. |
| 14 | exists-I | The same witness data; premise is the computed instance and conclusion its existential formula. |
| 15 | forall-I | Literal matrix and binder; binder is absent from FV of every open premise leaf. |
| 16 | exists-E | Exact major existential, supplied matrix/eigenvariable/label, exact substituted temporary assumption; nonvacuous minor-branch removal; eigenvariable absent from all occurrences in the conclusion, major formula, and every surviving open assumption. |
| 17 | alpha | One premise and no parameters; comparison-record equality implements precisely syntactic alpha equivalence. |
| 18 | equality-I | No premise; supplied term; conclusion t=t; no open leaves. |
| 19 | equality-E | Supplied terms, matrix and variable; premises r=t and the computed r-instance, conclusion the computed t-instance; zero free occurrences of the variable are allowed. |

The governing body references are `inherited-02193-02340.tex:1–85` and
`inherited-03927-04061.tex:7–67`; all 20 registry forms are at
`handbook/registry/calculi/nd-fol.tex:10–29`. The registry makes the
exists-E nonvacuity and exact discharged formula explicit. No repetition,
arbitrary logical equivalence, implicit substitution, or extra logical axiom
is added by the new record definition.

Parent-count checks and strictly earlier child indices imply a connected tree:
every nonlast row has one parent, each parent step increases its index, and
the unique row without a parent is last. Child subtrees are disjoint because
a shared descendant would have two parents along the split paths. The stored
open lists can therefore be proved by induction to contain exactly the actual
open leaf occurrences, without duplication arising from shared subproofs.

Discharge is both formula-specific and branch-specific. A matching label in
the major disjunction premise, or in the other minor branch, cannot be removed
by the wrong branch's filter. A label on a different formula is also retained.
After a lower discharge, its removed occurrence is absent from every higher
open list. For exists-E, “every remaining open assumption” is checked after
the surviving minor list and the major list have been combined, so the major
assumptions are included in freshness. A bound occurrence of the eigenvariable
in the conclusion is forbidden by the actual stronger source condition;
the checker correctly uses Var here and FV for forall-I.

These are codes of annotated derivations. Matrices, terms, binder indices and
discharge labels are part of the object being checked. The construction does
not need to infer an arbitrary equality matrix or term substitution witness
from an unannotated sequence of formulas. Different valid annotations or
computation witnesses may yield different certified proof codes for the same
raw derivation, which is consistent with injective coding of the enriched
objects.

### Axiom membership, Comp, and both proof-meaning directions

The finite-axiom convention is exact. Q has the seven universal-closure
sentences in `inherited-09099-09111.tex:1–13`; their supplied universal
instances are derived by forall-E, rather than declared to be new axiom
leaves. The empty finite theory permits no surviving open leaf. The optional
direct finite-membership proof convention is explicitly distinct and must be
held fixed; the later definition selects the certified convention.

P4 defines c.e. sets by domains at `inherited-07753-07843.tex:9–12`, and its
accepted enumeration theorem supplies an index for each partial computable
function in the exact serialized numbering. Thus e_T is a domain index on
the new formula-tree codes. For an enumeration presentation, the familiar
conversion is to search its successive outputs for the supplied code and
write a fixed canonical output when found; the enumeration theorem then
indexes that partial function. This does not identify an enumerator's output
program index with the required domain index.

The accepted Comp formula checks acceptance with a valid numerical output,
not any halt. Its theorem states both that a successful code is such a history
and that a defined partial-function value has a history witness. The output
value itself need not be 1 because only the domain of e_T matters.

The new PR argument for V is valid for the fixed marked-bounded Comp
presentation. P4's in-matrix comparisons Lt and Le have bounded definitions
(`inherited-08710-08876.tex:160–180`), and the beta graph deliberately uses
a marked-bounded comparison (`inherited-08439-08709.tex:27–45`). Expanding
those relational abbreviations therefore does not add an unbounded matrix
quantifier to the presentation being evaluated. Terms, Boolean operations and
bounded sums/products are PR, and the bound variable is absent from the
bounding term. Structural induction for this one fixed formula yields a PR
characteristic function of its standard truth. The subsequent full
first-order expansion has the same truth value by the already declared
abbreviation semantics. No arbitrary-formula truth predicate or uniform
unbounded evaluator is inferred.

At the root, exactly one supplied history position corresponds to each
surviving open leaf occurrence. Repeated uses of the same axiom are distinct
leaf positions and receive the corresponding entries in W; histories may
coincide. A temporary discharged assumption needs no membership evidence.
In particular, a derivation consisting of the premise-free equality-I proof
of `0=0` has no surviving assumptions and uses W=0. Extra certificates fail
the exact-length check. An open assumption from the empty theory has no
certificate because the selected domain is empty.

For proof-code-to-derivation, induction first identifies each complete
subtree and its open occurrences, not only its root formula. The root graph
is connected, and each surviving sentence's successful V test supplies a
defined computation of e_T. The domain choice puts it in T. These facts give
the actual T derivation.

For derivation-to-proof-code, copy the finite tree into postorder, retain the
actual annotations needed by its rule instances, and use its labels. The
same induction proves every local and open-list check. Each of its finitely
many surviving T leaves belongs to the domain of e_T, so the accepted Comp
theorem supplies a history. Finite successive choices form W; there is no
claim that successful histories can be found within a PR bound as a function
of the axiom alone. The empty-open-list case supplies the empty W directly.
Both directions thus establish the displayed standard-model theorem.

The prime-power illustration is also arithmetically correct: its product is
600 and its paired total is 182706. The positive exponents retain trailing
zero entries; the explicit paired length can be projected. This illustration
does not govern the new tree/derivation codes, and Comp witnesses retain the
separate beta coding.

## Representation and downstream boundaries

`inherited-09262-09327.tex:4–18` defines relation representation
numeral by numeral, including both truth and falsity cases.
Lines 20–29 define the stronger, separately stated function representation;
lines 31–48 retain a cited theorem and a construction summary. The P5
numerical proof checker supplies a PR relation to which that cited relation
clause applies. It does not itself prove Q representation, uniform internal
proof checking, or arithmetic identities for all nonstandard codes.

The new explicit warning at lines 490–493 is appropriate. The downstream
`inherited-09750-09816.tex:13–47` separately states D1–D3 and a cited PA
assertion. This report does not accept that assertion for an arbitrary
numeralwise representative merely because the new numerical checker works.
The internal choice and verification needed by those consumers remain their
own obligation. The stronger claim is not used in either standard-model
direction reviewed here.

## Read manifest and hashes

All paths below are relative to `C:/Dev/the-methods-of-reason`. Hashes bind
whole files; the read column states the actual substantive read range and
does not imply review of unread passages. The complete accepted C6 scope is
used as a dependency at the standing recorded in its acceptance file; this
review did not independently re-prove every H1–H4 clause.

| File | Actual read lines | Whole-file SHA256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | 1–168, full | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |
| `spec/research/edition-2026-p5-syntax-arithmetization.md` | 1–78, full author/scope lead | `d518fc87200c34b0fbbfdcf1eff0ee488a77a29067e60d77a0b5ab17069f7d45` |
| `spec/verification/edition-2026-c6-text-acceptance.md` | 1–73, full accepted dependency boundary | `aeeffb41c4d21caf2ea0f6145fe07cdc1a26e9c7dc6b06aa10c9e8baec9ffc17` |
| `handbook/restoration/inherited-09328-09438.tex` | 1–519, full | `87c2203ae4f94d78b973b592c9ca88013e7ef0641410e512b45c79a680ab9903` |
| `handbook/restoration/inherited-02193-02340.tex` | 1–148, full | `5ba27894edf744d288008b613adf93eac3d65385f745135de776d5b6011316a3` |
| `handbook/restoration/inherited-03038-03104.tex` | 1–67, full | `8531b8fc91a659ab7c5b131a77fca7aff9c97f0a052e3b78fe0459adec25ffab` |
| `handbook/restoration/inherited-03105-03165.tex` | 1–61, full | `5c062c8a2584c841ed74ec9b546fa502ef0ff4d667a5a702ec56b7c8a49463c9` |
| `handbook/restoration/inherited-03166-03239.tex` | 1–74, full | `d7d08869229f450d219bcb06ffa8e990b60db10f195b76d53e9eccbbc480ac3c` |
| `handbook/restoration/inherited-03240-03428.tex` | 1–189, full | `36d7779d6b9bb3caf0c4ef514a79a1c7d8aa10bd4a72290256ea1d09d5db58cc` |
| `handbook/restoration/inherited-03927-04061.tex` | 1–135, full | `2ad2846970d4976177b0fbb8ac59ff8106253f5d155a5e4861956f7f651bf480` |
| `handbook/registry/calculi/nd-fol.tex` | 1–29, full | `f25549bc18fc4aae212eea32cadc9fffd08e03d712f5df10e9da62f660be5370` |
| `handbook/restoration/inherited-07678-07752.tex` | 1–75, full | `1b3a7277d05f42cd5e568cc12b851f2e460bdbab4244d11f91f30eff78aa02dd` |
| `handbook/restoration/inherited-07753-07843.tex` | 1–91, full | `e2b7284beabca82f440bb921d779243f1615f8d7077aba73dff6cbde28458b00` |
| `handbook/restoration/inherited-07851-08048.tex` | 1–261, full | `de01687b7f524f49d6b3e90c9acd038550f7be1551a1aabc771b8bbb3b4b0177` |
| `handbook/restoration/inherited-08306-08438.tex` | 1–133, full | `0b020970be72999cd771566ba0d6cdb4e4668728362cbd3c0d1606059ee9d2b8` |
| `handbook/restoration/inherited-08439-08709.tex` | 1–89; isolated locating hits elsewhere only | `95eb4270559303fefc5de2d9bc804a04768ead87d68d9e5d9cbf65079714806a` |
| `handbook/restoration/inherited-08710-08876.tex` | 1–100, 160–181, 640–720, 790–912, 940–1045; isolated locating hits elsewhere only | `4d131a6631a148354f31066316e3b73977df71af66c06fc98158d6c402dbc102` |
| `handbook/restoration/inherited-09099-09111.tex` | 1–13, full | `38534e090c35db78d99d045d19b3c7f34f1f1aaa8999cf118c7a416cd41d9d2b` |
| `handbook/restoration/inherited-09262-09327.tex` | 1–66, full | `75a27e87080116a235a904daedabe2a70dff472ba27ca8a454c448dfd4b58bb6` |
| `handbook/restoration/inherited-09750-09816.tex` | 1–67, full downstream boundary | `efa16565dc4206d722ba62585aa452a86394b5827c84b6201c6340815062d2de` |
| `handbook/parts/p05.tex` | 1–52, full route and first-theorem hook | `068b90e56bfcf4538aff14f0dbbf428a228a34b12736ca55484b1e3d5e64b326` |

Additional locating-only searches returned individual derivability-reference
lines in `inherited-09817-09876.tex` and `inherited-09877-09924.tex`; their
proof bodies were not read or used as acceptance evidence. A lightweight
memory lookup supplied the prior review discipline of frozen snapshots and
separate admission gates; all mathematical claims and current source hashes
in this report come from the live reads identified above.
