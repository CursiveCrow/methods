ACCEPT

# Round-six mathematical/proof review: N-c-012.b Pnueli 1977

## Verdict and findings

I found no blocker, must-fix, should-fix, unresolved mathematical uncertainty,
unsupported theorem-strength claim, type error, quantifier error, invalid local
derivation, or source/handbook proof-ownership confusion in the round-six
snapshot. The reader now states the mathematics at the strength supported by
the printed source, and where the source itself is ill typed, unsound, under-
specified, or only sketched, the reader exposes that boundary rather than
silently repairing or strengthening it.

No findings are filed in this round.

## Reviewer, independence, and method

- Seat: mathematical/proof correctness.
- Stable agent identifier: `/root/p09_math_proof_review`.
- Runtime disclosure: the harness identifies the reviewer as Codex based on
  GPT-5; no more specific runtime model or version was exposed.
- I read the board charter before substantive review and treated only its
  Round-six repaired snapshot as controlling.
- I did not inspect `spec/research/boards/p09-n-c-012b/ledger.md`,
  `transcript/chair.md`, any round-one through round-five transcript, or either
  other round-six transcript. I did not request, infer, discuss, or receive
  another reviewer's conclusions, and I did not contact another reviewer.
- I visually read the archival wrapper for provenance and every printed body
  page 46--57 from `tmp/pdfs/p09-pnueli-1977/page-02.png` through
  `page-13.png`; those images controlled over OCR and memory. In particular, I
  reread the source image of printed p. 53 at original detail and independently
  read the tail condition as the negation of an eventual permanent absence,
  hence as `forall i exists j >= i`, not `j > i`.
- I read the full frozen reader scope
  `handbook/parts/p09/presentations/n-c-012.tex:370-1204` and
  `:1610-1617`, the shared scope
  `handbook/parts/p09/logic-in-computer-science.tex:599-823`, the complete
  source note, source-presentation ledger lines 151--167, the complete
  `Pnueli1977`, `McNaughton1966`, and `Landweber1969` bibliography entries, and
  the immediately adjacent Kamp/GPSS and version-boundary prose needed to test
  conflation.
- I made no manuscript, shared-surface, source-note, source-ledger,
  bibliography, authority, or other repository edit. This transcript is the
  only file I created. I ran no test, test harness, automated checker,
  repository script, TeX command, handbook-PDF inspection, or build. Hashing
  and source-image reading were the only mechanical operations.

## Frozen-identity verification

All eight identities matched the Round-six charter before substantive review
and again immediately before this filing:

| Frozen object | SHA-256 |
|---|---|
| `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` | `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB` |
| `tmp/pdfs/p09-pnueli-1977/focs77.ps` | `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F` |
| `tmp/pdfs/p09-pnueli-1977/focs77.pdf` | `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `3A4ECE9251B46ACAD8925FFCD34162BE3F9741C09DF912B70967C8FAAB7BE1BC` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394` |
| `handbook/bib/handbook.bib` | `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9` |
| `spec/research/p09-pnueli-1977-source-note.md` | `86EA6E1F4934B61D5D7E517C01466D6CDA98F80348B1233D52F953F9B1A821CA` |
| `spec/research/p09-source-presentations-lot2-3.md` | `05931057A05C0DCD81507394AF6152B02C3BC12B7E5A7E7AAB757A84A4B1F5C9` |

The immediate post-filing recheck returned these same eight identities. The
transcript write therefore did not change any frozen input.

## Mathematical and proof audit

### 1. Program model, reachability, and specification standing

At reader lines 384--443, against printed pp. 46--47, the tuple
`Sigma=<S,R,s_0>` and infinite initial execution are correctly typed. The
sequential maps have domains and codomains
`N:L x D -> L` and `T:L x D -> D`; substituting them into the displayed
transition equation returns a state in `L x D`. In the concurrent equation,
the selected processor updates exactly its own location and the shared data,
while every other location coordinate is unchanged. The existential processor
index is finite and correctly scoped. Determinism is attributed only as the
source's notational simplification, and atomic granularity is not promoted to a
logical theorem.

Reader lines 445--490, against printed pp. 48--49, correctly totalize the
finite-power recursion with `R^0` as identity, so `R*` is reflexive-transitive
and `s_0` belongs to the reachable set `X`. A state assertion is defined before
use as a Boolean-valued map on `S`; invariance is correctly restricted to `X`.
Clean execution is kept distinct from partial correctness, and the distinction
is used by the invariant examples. The metalinguistic relation
`varphi leadsto psi` is exactly typed between state assertions and retains the
printed strict target quantifier `j>i`; it is explicitly not imported into the
handbook LTL grammar.

The early scheduling prose at reader lines 439--443 says only that a continually
enabled processor should not be postponed indefinitely. The later formal
condition at lines 937--953 quantifies over action occurrences. These have
different objects in their antecedents and are consistently described as
distinct; no implication, equivalence, or strength ordering is asserted. This
matches source-note lines 92--95 and 476--496 and ledger line 161.

### 2. P1, literal P2, and the two P2 counterexamples

Reader lines 492--526 reproduce the reachable-state induction direction and
the literal p. 49 P2 premise/conclusion correctly. Extending the rank predicate
to `S x N_0` is exactly the typing repair required by the printed `n-1` at
`n=1`, while rule instances remain quantified over `n>0`. Universal closures
and the metalinguistic standing are explicit. The target is the source's
current-state `psi(s)`, not a silently substituted successor-state target.

Both counterexamples at lines 528--552 calculate correctly:

- In the zero-rank example, `A(a,1)` supplies the first premise, and the only
  true positive-rank transition antecedent is the edge `a R b`; its consequent
  holds through `A(b,0)`. No state on the unique execution satisfies `psi`, so
  totalization alone is unsound even for inclusive eventuality.
- In the strictness example, the same ranked edge is discharged by `psi(a)`.
  Because `psi` is false at `b` and thereafter, no strictly later target exists,
  so the printed P2 premises do not imply the printed strict conclusion.

The proposed boundary `forall s not A(s,0)` is correctly identified as an
unprinted sufficient repair only for inclusive eventuality. If no `psi` occurs,
the transition premise must decrease a positive rank until it demands the
forbidden rank zero. It does not repair the independent strict-future example,
and it is not added to literal P2. The reader also keeps A2's current-state
problem, inclusive `F`, and Theorem 3's representation visible as separate
source tensions at lines 679--687.

### 3. Typed ER, R4 hygiene, induction metarule I, and Theorem 1

Reader lines 554--627, checked against printed pp. 49--50, give A1--A2 and
R1--R4 at correct types and directions. For R4, the nonempty parameter domain
`U`, family `widehat p:S x U -> Bool`, sections `widehat p_u`, and pointwise
existential state assertion are defined before the rule. The premise has the
right eigenparameter reading: one derivation uniform in arbitrary `u`, with
the consequent and all open assumptions independent of `u`. Thus the
conclusion eliminates a witness without confusing a parameterized assertion
family with a tense constructor.

The specialization to `N_0` at lines 608--627 correctly types metarule I. The
successor derivation is under the displayed temporary hypothesis for arbitrary
`n`; ordinary mathematical induction yields each derivation
`widehat p_n leadsto q`, after which the already typed R4 gives the pointwise
existential antecedent. This is a metarule, not an added object-language
operator.

The source's completeness sketch and its assumptions are accurately bounded at
reader lines 629--648 and source-note lines 248--264. The predicate
`P:S x N_0 -> Bool`, its sections, assertion-language expressiveness, and
pointwise finite branching are explicit. A uniform numerical out-degree bound
is not invented. The Koenig step is correct under pointwise finite branching:
if arbitrarily long target-avoiding prefixes of infinite continuations existed,
the finitely branching prefix tree would have an infinite target-avoiding
branch.

The new first gap and counterexample at reader lines 650--665 are exact. In

`S={s_0,u}`, `R={(s_0,s_0),(u,u)}`, with `p` true only at `u` and `q` false,

the unique initial execution never sees `p`, so the initial-state strict
implication is vacuously true. The `u`-loop is nevertheless an infinite
all-start path with no `q`, so `P(u,n)` is false for every natural `n`. The
system has one successor at each state, hence is serial and pointwise finitely
branching. It therefore isolates the initial-state/arbitrary-state mismatch
from deadlock vacuity.

Each of the three stated alternatives is sufficient for only that mismatch:

1. If `S=X`, every arbitrary start `s` has a finite prefix from `s_0`; prefixing
   any infinite continuation from `s` produces an initial execution, so
   `p leadsto q` forces a later `q` on that continuation.
2. The same prefix argument works when assertion and rule semantics are
   consistently restricted to `X`.
3. If the theorem's implication quantifies over executions from every start,
   the required pointwise eventuality is immediate.

In each case, finite branching then converts pathwise eventuality to a finite
bound. The text accurately says the source states none of these alternatives
and does not use them to claim the theorem repaired.

The deadlock example at lines 667--677 is independent. With `S={d}` and empty
`R`, no infinite continuation from `d` exists. Consequently the universal
English reading of `P(d,0)` is vacuously true while `q(d)` is false. This breaks
the proof's base implication even after any of the three reachability repairs.
Requiring an infinite continuation from every state, or replacing `P` by a
nonvacuous finite-prefix/recursive definition with the intended zero case,
addresses this second issue; neither is silently installed. Conversely,
seriality does not repair the unreachable-state two-loop example. The two gaps
and their repair families are therefore neither conflated nor dependent on one
another.

### 4. Sequential/concurrent attachments and the producer--consumer proof

Reader lines 689--722 correctly type the location-indexed predicates and the
sequential attachment. Since `N(ell,u)` returns a location, the verification
condition uses `q_{N(ell,u)}` rather than an untyped integer index. Initial
truth and every per-instruction preservation implication are premises; P1
derives invariance only after they are proved. The finite-path ER statement is
correctly described as finitely many A1 instances composed by R2.

At lines 724--779, full attachment is one global state assertion with
`|I||J|` pair-indexed components. Partial attachment has the exact types
`p_i:L_2 x D -> Bool` and `q_j:L_1 x D -> Bool`; it remains one global
assertion and may mention the other process's control location. The sum/product
comparison is parameter-correct: the two-process displays have sum-size versus
product-size top-level cases; exponential cross-product growth requires the
number of process factors to vary. Avoiding explicit cross-product materialization
does not remove initiality and transition-preservation obligations.

The producer--consumer derivation at lines 781--828 is algebraically complete
at exactly the supplied indicator strength. The capacity `C>0`, load in
integers, semaphore values in naturals, and Boolean indicator maps are typed.
The text states both indicator directions it actually consumes, notably that
critical membership implies simultaneous `m_1=m_2=1` and that `m_i=1`
conversely locates process `i` in its critical section and makes it nonwaiting.
No complete support set is invented. The calculations are valid:

- `m_1=m_2=1` forces `mu=-1`, contradicting nonnegativity;
- `b=s_1+s_2+e >= 0` and
  `b <= r_1+r_2+e = C-f <= C`;
- mutex blocking gives `m_i=mu=0`, so the other `m` is one and the other
  process is not blocked;
- the remaining simultaneous empty/full wait gives
  `r_1=r_2=e=f=0`, forcing `C=0`, contrary to the positive-capacity premise.

Thus the stated mutual exclusion, load bound, and no-deadlock conclusions use
all and only the displayed premises.

### 5. Future calculus, complete S4 countermodel, and system rules

Reader lines 830--896 correctly distinguish the source's metalinguistic
`H(t,p)` from the object language and give recursive semantics for nested
Boolean/F/G formulas. Both `F` and `G` include the present, `F` is the Boolean
dual of `G`, and no `X` or `U` is imported. G1--G3, RT/RG/MP, F2--F3, and the
exact Q1--Q4 directions match printed pp. 52--53. The absent quantifier-domain
semantics and unresolved range of the metavariable in Q1--Q4 are disclosed;
the handbook's conservative atemporal-use policy is not attributed to the
source.

The linear-valid formula at lines 907--915 is valid: for future witnesses `i`
for `p` and `j` for `q`, linearity gives `i<=j` or `j<=i`; the earlier witness
satisfies its atom and has the other atom in its inclusive future.

The displayed S4 witness at lines 916--927 is a complete model, not a bare
frame. Its relation consists of the three reflexive loops and the two root
edges to incomparable leaves. It is reflexive, and every possible two-edge
composition is already present, so it is transitive. The full truth evaluation
is:

| World | Atoms | Accessible worlds | Relevant evaluation |
|---|---|---|---|
| `r` | neither `p` nor `q` | `r,u,v` | `Fp` via `u` and `Fq` via `v` |
| `u` | `p` only | `u` | `Fq` false |
| `v` | `q` only | `v` | `Fp` false |

No accessible world from `r` satisfies `p and Fq`: `r` lacks `p`, `u` lacks
`Fq`, and `v` lacks `p`. Symmetrically, none satisfies `q and Fp`. Hence both
outer `F` disjuncts are false at `r` while the antecedent is true. This proves
only the stated point: an S4 referral does not establish completeness for the
preceding linear semantics. The reader correctly leaves Theorem 2's model
class unresolved and attributes no complexity bound or class to this paper.

At reader lines 937--997, against printed p. 53, the finite family is an exact
partition of `R`, and the condition
`forall a forall i exists j>=i a(s_j,s_{j+1})` is the literal tail negation
printed by the source. It is equivalent to every action relation occurring
infinitely often along an admitted execution. The I1/I2/E/N premises and
conclusions are correctly typed. N is explicitly restricted to action-fair
executions. Its raw-path counterexample is sound and independent of deadlock:
`a={(t,t)}` and `c={(s,s)}` are disjoint, nonempty action relations on a serial
two-loop graph; the initial `c`-loop satisfies both local N premises but never
takes `a` and never reaches `q`. The action symbol does not collide with the
producer load `b`.

The DI and DN displays at lines 999--1025 preserve the source's premise
directions, successor-side `p_2`, universal state closures, and designated
action. Their `Gp_2` side condition supplies `p_2` at each successor while DI
propagates `q` and DN waits for the first fair occurrence of `a`. They are
correctly marked as derived rules. Theorem 3 at lines 1027--1035 is not
overproved: the source's `p leadsto q` to `p=>Fq` instruction and claim that the
ER axioms are derivable are recorded as skeletal, with no fabricated local
derivations and with the strict/inclusive tension already exposed.

### 6. Finite-state semantics, SCC equivalence, and Theorems 4--5

Reader lines 1037--1069 correctly add finite seriality, define arbitrary-start
infinite action-fair paths, reserve `proper execution` for the initial-state
case, and define `Sigma |=_prop A` over those proper executions. These three
standings are distinct and used consistently. Seriality ensures every finite
path can be extended indefinitely; it is not back-projected into Theorem 1.

For Theorem 4 at lines 1071--1101, checking all source `p`-states is correctly
called sufficient. Restriction to raw reachable states `X` makes the test exact
for initial-state validity: any bad fair continuation from a reachable state
can be prefixed by a finite path from `s_0`, and the action condition is
tail-invariant; conversely every violating proper execution supplies such a
reachable state and suffix. No stronger source wording is claimed.

The internal-edge SCC criterion is typed and correct in both directions after
deleting `q`-states:

- If a reachable cyclic SCC has at least one internal edge from every action
  relation, select one such edge per action. Strong connectivity provides
  internal connecting paths, producing a closed walk that visits every chosen
  action; infinite repetition is a `q`-avoiding action-fair path.
- Any infinite path in the finite graph eventually remains within a single SCC
  because its condensation is a finite DAG. Its fair tail contains an internal
  occurrence of every action, and the infinitely traversed component is cyclic.

The manuscript explicitly owns this set formula and proof as a handbook
formalization of the source's component-label sentence, rather than quoting it
as printed proof.

The P/MRG package at lines 1103--1117 has the correct dependency restriction:
MRG may be applied only when the proof used no P instance. The two-state path
example proves that unrestricted generalization after initial truth is unsound.
Theorem 5 at lines 1119--1124 retains both clauses--semantic decidability and
derivability of every valid propositional tense formula in the extended
calculus--while expressly saying that the paper prints no general construction
for the adequacy clause. Appendix B is not misrepresented as proving adequacy.

### 7. Appendix A and Appendix B proof boundaries

Reader lines 1126--1155 reproduce T2, its corollary, T3, and its corollary at
their printed strengths and assigns T2/T3 to reference [23]. The six-step local
lemma is correct: excluded middle for `Fq` becomes `Fq or G not q` by the dual
definition; the assumed implication covers the `G not q` case, the tautology
covers the `Fq` case, and propositional case analysis yields `p=>Fq`. The local
proof is not transferred to the external formulas.

At lines 1157--1204, the monadic-second-order and infinite-word approaches are
kept as alternative semantic decision routes. `L_prop(Sigma)` is a typed subset
of `S^omega` and denotes exactly the previously defined proper executions.
For an atomic assertion, each state is first embedded as a one-letter word in
`S^1 subset S*`, so `[[p]] S^omega` is well typed under the declared
finite-prefix/infinite-word concatenation and denotes exactly the words whose
first state satisfies `p`. The Boolean clauses are ordinary language
operations, `S*L(W)` implements inclusive eventuality, and
`L(GW)=L(not F not W)` implements the dual recursion.

The imported `omega`-regular name is eliminable as Büchi recognizability under
the shared definition at `logic-in-computer-science.tex:663-686`. Pnueli's
local, unproved proper-execution-acceptor assertion; reference [32]'s imported
language/closure machinery; and reference [33]'s inclusion decision remain
three separate proof-ownership claims. Neither the later LTL-to-Büchi theorem
at shared lines 688--697 nor the PSPACE model-checking result at lines 704--749
is attributed backward to Pnueli.

## Criterion-by-criterion result

- **C1 -- checked clean.** Reader lines 372--382, source-note lines 7--52,
  ledger line 153, and bibliography lines 2226--2237 agree on author, title,
  venue, year, pages, DOI, first-party access, hashes, wrapper/body page map,
  rights restraint, and open IEEE comparison. Wrapper page 1 was used only for
  provenance; printed pp. 46--57 controlled mathematics.
- **C2 -- checked clean.** Reader lines 384--490 and 937--953 match printed
  pp. 46--49 and 53 on system/execution types, atomicity, reflexive reachability,
  specification hierarchy, strict temporal implication, action partition, and
  the two non-equated fairness formulations.
- **C3 -- checked clean.** Reader lines 492--687 match printed pp. 49--50 on
  P1, literal P2, ER, R4, I, and Theorem 1; every typing repair and every
  counterexample/gap is mathematically valid, expressly handbook-supplied, and
  does not silently strengthen the source.
- **C4 -- checked clean.** Reader lines 689--828 match printed pp. 50--52 on
  sequential verification obligations, full/partial attachments, scope and
  growth parameters, and the complete positive-capacity invariant deduction.
- **C5 -- checked clean.** Reader lines 830--1035 match printed pp. 52--55 on
  recursive inclusive F/G semantics, pure axioms/rules, unresolved quantifier
  scope, RG restriction, I1/I2/E/N, DI/DN, and Theorems 2--3. The S4 model-class
  objection is fully proved and source strength is not overstated.
- **C6 -- checked clean.** Reader lines 1037--1204 match printed pp. 55--57 on
  finite seriality, proper executions, Theorems 4--5, P/MRG, SCC decision route,
  Appendix A, and Appendix B. Local proof, asserted proof, and external proof
  ownership are separated.
- **C7 -- checked clean.** The reader, shared lines 599--823, source note,
  ledger lines 151--167, and the three bibliography entries agree on definitions,
  source locators, theorem/gap status, external references, and the absence of
  retrojected later results.
- **C8 -- checked clean.** The exposition is independently worded and defines
  each needed standing before use. New technical names have an exact eliminable
  definition or source standing, a stated distinction, and an actual later use.
  The open status and all neighboring gates remain narrow.

## Invariant-by-invariant result

- **I1 -- satisfied.** Source reading and mathematical/prose reasoning only;
  none of the prohibited test/build mechanisms was used.
- **I2 -- satisfied.** All eight controlling identities matched before review,
  immediately before filing, and immediately after filing.
- **I3 -- satisfied.** Wrapper plus every printed page 46--57 was visually
  reread; no OCR-only or partial-source verdict was used.
- **I4 -- satisfied.** Definitions, types, quantifiers, premises, side
  conditions, theorem strength, proof status, and external boundaries were all
  checked as detailed above.
- **I5 -- satisfied.** Strict `leadsto`, A2, inclusive F, and Theorem 3's
  representation remain visibly distinct and unreconciled at reader
  lines 473--483, 554--605, 830--856, 1027--1035, and 679--687.
- **I6 -- satisfied.** The Pnueli presentation imports no later X/U grammar,
  LTL-to-Büchi construction, safety/liveness syntax, or PSPACE classification;
  shared and GPSS material is explicitly separate.
- **I7 -- satisfied.** State assertion, parameterized family/pointwise
  existential, full/partial attachment, proper execution, restricted system
  validity, proper-execution language, and omega-regular standing each meet the
  five-part technical-name rule locally and are used later.
- **I8 -- satisfied.** The complete author-hosted body supports body-level
  review, while IEEE-direct comparison remains open at reader lines 1610--1617.
- **I9 -- satisfied.** This is one independent seat verdict only; the ledger and
  source note still require unanimous acceptance of the same snapshot.
- **I10 -- satisfied.** Acceptance here is confined to N-c-012.b mathematical/
  proof review. It does not close N-c-012, Part IX, any build or visual gate,
  human/final-book review, or user acceptance.

## Mandatory F27--F43 regression coverage

- **F27--F35 -- checked clean.** The raw-path action symbol has one relation
  type and does not collide with the producer load; full attachment is exactly
  defined and used; producer implications are neither missing nor inflated;
  state assertions precede use; arbitrary-start paths, proper executions, and
  restricted validity are distinct; size claims use the right parameters; the
  SCC formula/proof is exact and handbook-owned; Theorem 5 adequacy remains
  unproved locally; and the three Appendix B ownership levels are separate.
- **F36--F40 -- checked clean.** Zero-rank typing is separated from soundness;
  both P2 counterexamples and the limited false-at-zero repair work; R4's
  parameter family/eigenparameter hygiene and I's `N_0` specialization are
  exact; every used producer indicator direction is present; the linear-valid
  formula and full branching S4 refutation are correct; and the one-letter-word
  embedding makes Appendix B's atomic language clause typed.
- **F41 -- checked clean.** The serial finitely branching two-loop example
  refutes the initial-state-to-arbitrary-state pointwise step, the three
  alternatives fix exactly that reachability mismatch, and none is attributed
  to the source.
- **F42 -- checked clean.** The S4 witness includes `W`, reflexive-transitive
  `rho`, and `V`; the root has neither atom, satisfies both eventualities, and
  satisfies neither consequent disjunct under the full accessibility truth
  evaluation.
- **F43 -- checked clean.** Early enabled-processor prose and later
  action-occurrence fairness are described only as distinct. No typed
  correspondence, implication, equivalence, or ordering is claimed.

## Narrow closure boundary

This `ACCEPT` says only that the exact round-six N-c-012.b mathematical/proof
surface has no remaining substantive defect. It does not by itself supply the
other two independent acceptances, close the board, validate an IEEE-supplied
copy, admit neighboring N-c-012 presentations or Part IX, run a build or visual
handbook inspection, constitute human review, complete the book, or record user
acceptance.

ACCEPT
