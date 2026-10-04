# P5: exact direct PA axiom presentation and numerical proof checker

Date: 7 September 2026. Bounded author block began at 21:08 UTC, with the
first saved-content checkpoint at 21:22 and the next construction checkpoint
before 21:39. This note reports author construction, not independent acceptance.

## Result and scope

The assigned numerical construction is supplied in full: seven fixed arithmetic
axiom codes; a canonical induction-axiom constructor; an explicit bounded
primitive-recursive recognizer; actual ND transport between parameter-closing
orders; the direct twenty-rule proof checker; both directions of its source
PA proof meaning; and a bridge to the separate c.e.-certificate convention.

The wider PT-1 arithmetic-predicate integration remains OPEN. No arithmetic
representative is selected by an arbitrary numeralwise condition. The exact
finite graph-description selection and the PA proofs of the D2/D3 invariants
remain subsequent work, at the original promised scope.

Only these three new files were written:

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | 261 lines, full reader definitions/theorems/examples | `4e77367fb719429fe8739a0f22072fd8817c76350c290259c960ac8f05974dde` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | 311 lines, every proof inside one annexitem | `458f700396868572b885555961aaa454ea010b10ade8f46609ba6c1cd6f4890a` |
| `spec/research/edition-2026-p5-standard-pa-checker.md` | This single handoff note | Supplied on delivery |

No existing representation, coding, derivability, GL, driver, registry or
provenance file was edited. No tests, builds, renders, source acquisitions or
subagents were used. The existing local primary definitions suffice for this
independently written construction; no external author's numbering or proof
was substituted for the actual calculus.

## Completed components

### The exact nonlogical axiom set

The source's two displayed variable roles in its seven Q axioms are fixed as
x_0 and x_1 before assigning literal codes. All seven q_j are written as exact
N_k constructor expressions, with v_i=N_0(i) and o=N_1(). Their primitive
negations, equality, function constructors, quantifier indices and prefix order
are explicit. The predecessor axiom retains a distinct existential variable.
Term instances and alpha variants are derived through real ND rules; the
finite constant test does not silently accept them as additional axioms.

F(m) scans indices j<m and returns the increasing list of distinct free
indices. U(P,c) wraps the supplied list from the inside outward, so increasing
indices appear outside inward. The induction constructor first builds

`(phi[0/x_i] and forall x_i (phi -> phi[Sx_i/x_i])) -> forall x_i phi`

and then closes exactly F(m) minus i in that order. Invalid matrices return
zero. An induction variable absent freely is allowed. Both substitution
instances use the exact existing operation; for these two replacement terms
its renaming clause never fires, and substitution stops at a binder for x_i.

### Bounded recognition, including malformed cases

The recognizer first checks sentence type and the seven constants. It then
strips the maximal universal prefix, requiring at most a updates for input
code a. From the residual implication's right universal child it recovers the
induction variable i and matrix m. Both are below a. It checks the left
conjunction/step shape and reconstructs the complete canonical axiom. Literal
equality decides acceptance. No unbounded search over matrices, variables,
alpha variants or proofs occurs.

The proof shows both directions: every constructed induction axiom is accepted,
and every nonconstant accepted code equals the displayed constructor for its
recovered matrix and variable. It verifies the free-variable and all-variable
identities, sentencehood, finite scan bounds, total defaults, and primitive
recursiveness. Wrong base/step instances, mismatched matrix copies, changed
bound occurrences, wrong arities, missing or noncanonical parameter prefixes,
and extra vacuous prefixes fail as specified.

### Actual ND transport and its freshness invariant

For two closures of the same core formula, peel one prefix with forall-E,
using each bound variable itself as the instantiating term. The proof first
establishes the literal substitution identity phi[x_i/x_i]=phi. Introduce the
other prefix with forall-I in reverse list order. The only open assumption is
the initial closed axiom, so every introduced universal meets its side
condition. This supplies both directions and includes empty, reordered,
repeated or vacuous source prefixes where those variants are used.

The transport of complete proof trees does not rely on the insufficient
argument that replacement axioms are merely closed. For induction, the
canonical leaf's all-variable set is Var(phi) union {x_i}, a subset of the
source closure's all-variable set. In the reverse direction choose the source
closure of exactly the free parameter set, giving equality of those sets.
The fixed arithmetic axioms are unchanged, and their two-variable prefix-order
variants have equal occurrence sets. Thus every old exists-E eigenvariable
still satisfies the actual all-occurrence absence condition. Universal
introduction, discharge labels and nonvacuity are checked as well.

Only surviving open axiom occurrences are replaced. New leaves are unmarked;
the replacement chains contain no discharge. Old conclusion formulas and
rule parameters remain unchanged. The proof also gives a PR tree construction:
an input record p with n rows produces at most n(1+2p) rows, with transformed
child blocks computed in the old postorder and their premise references shifted.

The seven arithmetic representative names are fixed before the code theorem;
the theorem does not identify differently named closed formulas as numbers.
The annex explains actual alpha conversion of bound-name variants separately.
Its full tree transport covers the active induction scheme and parameter
closure conventions, including the strong existential freshness condition.

### A separate direct standard proof sort

The new code is `N_19(N_15(R),0)`. Outer tag 19 is distinct from the earlier
certified tag 16; the trailing zero is an empty certificate field. The checker
imports every actual one of the twenty row tests and adds the direct axiom
test only at the final surviving open leaves. It includes exact outer arities,
row/parameter types, the parent-count tree condition, the sentence root and
matching requested conclusion. There is no Comp call in this convention.

The annex prints both complete twenty-entry premise-arity and parameter-length
lists and explicitly retains the corresponding formula/side-condition checks.
The lists are not presented as a replacement for those substantive checks.

The proof checks both directions of

`PA derives sigma iff there exists p StdProof_PA(p, code(sigma))`

for sentences. It decodes successful rows to their actual tree and open
assumptions, and conversely transports a source PA derivation, encodes it in
postorder with its actual annotations, and applies the direct membership test.
The empty-open-list case, a one-row equality-I proof, and a one-row arithmetic
axiom proof are supplied explicitly. A nonempty certificate field is rejected.

### Bridge and retained internal boundary

A successful earlier certified proof yields a source PA derivation by the
accepted Comp theorem. Transport its open axioms to the canonical presentation
and put the resulting tree in the tag-19 record. In general this is more than
discarding W, because noncanonical closure chains may need insertion.

Conversely, transport a direct proof to the source presentation and choose an
accepting Comp witness for each of its finitely many source axiom leaves.
The ordered witness list and outer tag 16 give a certified code. No PR bound
on finding those witnesses is asserted for an arbitrary c.e. domain index.
The code sorts are disjoint, although their existential proof meanings agree.
This gives no automatic PA equivalence between arithmetic representing formulas.

## Remaining standard-formula and internal targets

1. Freeze finite descriptions for the named numerical library operations and
   the exact new direct checker. Use their actual graph-construction formulas;
   do not choose a formula solely by numeralwise agreement with StdProof.
2. Give the direct-tag version of the proof-combining function and prove its
   row-shift, parent, open-leaf and axiom-check invariants in PA. Its new
   certificate convention avoids any arbitrary axiom-domain-index behavior.
3. Build PA-verifiable proofs of the direct axiom-recognizer's accepted
   instances and the bounded-evidence proof constructors, preserving the actual
   nonvacuous ND discharge and quantifier freshness tests. Then prove the
   internal Sigma1 completeness target and D3 for the exact selected formula.
4. Establish any arithmetic bridge actually required by later consumers before
   changing their predicate selector. D1–D3, GL soundness and Solovay claims
   must attach to that same completed construction.

The present checker does not depend on the new PA graph theorem for its
numerical correctness. That theorem is referenced only as the interface for
the next arithmetic-formula selection stage.

## Lead integration and notation intake

- Add `\input{parts/p05/standard-pa-proof-predicate}` after the removal of
  `hb-p5-arithmetization-anchor` in `handbook/parts/p05.tex`, before the existing
  model/interpretability supplement. This ensures all new ordinary theorems
  occur outside the inherited first-theorem hook.
- Add `\input{annex/p05/standard-pa-proof-predicate}` in the P5 annex route
  after the new internal-arithmetic prerequisite input. Every proof in this
  new file is already inside its single annexitem, whose closing token is last.
- New section/definition/theorem identities are in the two new files; the
  reciprocal annex target is `annex:p5.standard-pa-checker` and its principal
  body theorem is `thm:p05-standard-pa-numerical-proof`.
- Register q_1 through q_7 as fixed arithmetic-axiom code constants; v_i and o
  as term codes; F as the increasing free-index list; U(P,c) as this local
  numerical closure operation; b(m,i), s(m,i), J(m,i) and IndAx(m,i) as the
  base, successor, induction-core and closed induction code operations.
- Register Ax_PA^d as a numerical membership predicate, PA^d as its sentence
  axiom set, and StdProof_PA as a numerical proof relation, with new outer
  constructor tag 19 and an empty second field. These are not yet arithmetic
  formulas. Distinguish local U from the existing universal-machine operation,
  and J(m,i) from a derivation row's premise-index list J.
- The source's fixed-variable and closure-order choices belong to the
  representation convention. Preserve the direct/certified distinction in
  every subsequent graph formula and consumer update.

## Read evidence and preservation

The actual source definitions were read before choosing the presentation.
No other new independent review was read. Root reported independent outcomes
for the previous prerequisite unit; those outcomes are not author acceptance
of the new checker.

| Source | Actual read extent in this block | SHA256 |
| --- | --- | --- |
| `handbook/restoration/inherited-09099-09111.tex` | 1–13, full seven-axiom definition | `38534e090c35db78d99d045d19b3c7f34f1f1aaa8999cf118c7a416cd41d9d2b` |
| `handbook/restoration/inherited-09175-09187.tex` | 1–13, full PA definition | `0db98b87928aa115c82883993e2e25b18286779e7ded0399c7148633c0178430` |
| `handbook/restoration/inherited-09328-09438.tex` | 11–139, 141–222, 224–370, 391–494: code grammar, all syntax routines, all twenty rules, certificate convention and proof meaning | `a6e37fa592e81b888c14a2da97cc70f1a05ec69bae0ce4d36e2e60c59f09c541` |
| `handbook/restoration/inherited-03240-03428.tex` | 1–91, exact substitution and alpha conventions | `36d7779d6b9bb3caf0c4ef514a79a1c7d8aa10bd4a72290256ea1d09d5db58cc` |
| `handbook/restoration/inherited-03927-04061.tex` | 1–67, complete actual FOL rule definition and derivability | `2ad2846970d4976177b0fbb8ac59ff8106253f5d155a5e4861956f7f651bf480` |
| `handbook/registry/calculi/nd-fol.tex` | 1–29, full registry with all twenty rules | `f25549bc18fc4aae212eea32cadc9fffd08e03d712f5df10e9da62f660be5370` |
| `handbook/parts/p05.tex` | 1–52, full current driver for intake | `068b90e56bfcf4538aff14f0dbbf428a228a34b12736ca55484b1e3d5e64b326` |
| `handbook/annex/p05-route.tex` | 1–15, full root-updated route for intake | `cb9713160edeb4afc683ecb9d7d456a284bbc24f3b3a31a4ad600beaeef8a07f` |
| Both new LaTeX files | Complete sequential author read-back, including the final added examples and bounds | Current hashes above |

The governing 168-line edition contract and the full P2 grammar/FV/label
definitions read in the preceding task remain the declared prerequisites.
The new work keeps their exact local-calculus meanings. Locating searches for
universal-closure and renaming terminology returned other source hits; they
were not used as unproved transport lemmas.

The prior representation file remains at
`b49a3b30aff36050841d4f384a6ba80fcf36f4661b3c4085e58d2371b4e003cb`,
and the prior coding file at the hash in the table. Root moved only the old
prerequisite annexitem's closing token to include its mp proof; its current
root-reported and directly checked hash is
`f11b72e5ae8ff2407c58fa434320d08095c0c543ae8c610237eed42eafffa1c1`.
This author made no edit to any of those existing files. Read-only shell
escalation was used because the local child helper remained unavailable;
all writes used apply_patch on the three assigned new paths.
