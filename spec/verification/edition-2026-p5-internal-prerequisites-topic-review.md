# P5 internal prerequisites: independent topic review

Review date: 7 September 2026. Assignment window: 21:00–21:40 UTC; actual first source inspection at 21:06 UTC. Reviewer: fresh independent mathematical context, assigned by the lead integrator. Repository: `C:\Dev\the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The inspected manuscript files are live working-tree files; the hashes below identify the reviewed text.

## Verdict and scope

**PASS for the supplied mathematical prerequisites at the recorded hashes.** No mathematical error, missing hypothesis, circular internal derivation, or countermodel was found in the claims accepted below. This is a topic review of the supplied text. The particular PA proof checker, its exact arithmetic predicate, internal D2 and D3, the proof builder for bounded evidence, and GL integration remain **UNRESOLVED / OPEN**. They receive no PASS from this report.

Read the governing edition contract in full before substantive review. Read all three assigned targets in full and checked the actual Q and PA axioms, the marked-quantifier hierarchy, the actual P and B formulas, the natural-deduction rules and substitution convention, and the computation-certificate interface. No author conclusion or other new review was read before filing. No subdelegation, manuscript edit, test, build, or rendering was performed. The only written artifact is this report. Source fidelity, publication, and admission remain their separate assigned gates.

The inherited Q representability theorem at `inherited-09262-09327.tex:31–48` remains a cited theorem with its existing boundary. Its complete proof was not supplied in these targets and is not accepted here as an in-document proof. Its stated positive numeralwise clause is a legitimate explicit premise of the D1 proof reviewed below.

## Per-result decisions

In this table, `R1` is `handbook/restoration/inherited-09262-09327.tex`, `R2` is `handbook/restoration/inherited-09328-09438.tex`, and `A` is `handbook/annex/p05/internal-proof-predicate.tex`.

| Result | Location | Decision | Mathematical basis |
| --- | --- | --- | --- |
| Elementary PA arithmetic and least-number reasoning | A:15–43 | PASS | The displayed inductions use the actual right-recursion axioms and unrestricted induction with parameters. |
| Division, uniqueness, and quotient/remainder bounds | A:45–59 | PASS | Successor induction gives the two remainder cases; strict order separates unequal quotients. |
| Total, unique, invertible pairing with component bounds | A:61–95 | PASS | The triangular relation is constructed directly by induction; its consecutive intervals partition every supplied natural argument internally. |
| Total and unique actual beta entry, with value at most its code | A:97–107 | PASS | Division uses the exact divisor and every bound of the live B formula is justified. |
| Signed coefficients, two-modulus construction, product coprimality | A:109–143 | PASS | Least positive linear combination and division supply the coefficient identity before CRT is used. Signed coefficients have explicit natural-pair expansions. |
| Common multiple and beta extension in PA | A:145–203 | PASS | Both required inductions have arithmetic invariants with retained parameters; no pre-existing coded sequence or PR evaluator is assumed. |
| Finite evidence collection for each arithmetic formula R | A:205–227 | PASS | The implication itself is the induction formula; the successor appends one witness and preserves earlier witnesses. |
| Fixed PR-description graph formula and Sigma-0-1 class | R1:76–143; A:229–237, 278–285 | PASS | The finite formation tree supplies a syntactic formula; the declared hierarchy includes bounded universal closure over existential formulas. |
| Internal graph totality, uniqueness, and defining equations | R1:117–149; A:239–276 | PASS | PA induction proves existence and entrywise uniqueness on arbitrary internal lengths; append and prefix restriction prove both recursion equations. |
| Standard meaning and numeral-by-numeral functional representation in PA | R1:119–142; A:287–303 | PASS | External induction identifies numerical values; actual finite PA calculations and internal uniqueness establish the stronger displayed numeral instances. |
| Lifting a recursion invariant | R1:160–185 | PASS | The stated PA base and step implications prove the displayed universal invariant by PA induction. |
| Specified addition, triangular, pairing and cons graph examples | R1:187–233 | PASS | Graph equations identify addition and the triangular solution; composition identifies the existing pairing formula and the positive cons successor. |
| Bounded evidence for each fixed Sigma-0-1 formula | R1:235–253; A:312–405 | PASS | All evidence clauses are bounded; both directions are proved in PA, and dependent evidence under a bounded universal is collected internally. |
| Numerical syntax/checker prerequisites and certificate interface | R2:24–470 | PASS for the stated numerical use | The constructor/list operations, bounded traversals, actual rule checks and fixed bounded Comp evaluator supply the required PR numerical relation and proof-code equivalence. |
| D1 from numeralwise representation | R2:496–521 | PASS | The numerical coding theorem supplies a standard p; the cited positive Q numeralwise instance becomes a T derivation, then existential introduction proves the required instance. |
| Exact external numerical modus ponens constructor | A:408–472 | PASS | Premise indices, parent counts, subtree open lists, discharge behavior and the certificate positions survive the displayed concatenation. |
| Exact PA checker/predicate, internal mp invariants, D2, evidence-to-proof builder, D3, GL | A:474–524 | UNRESOLVED / OPEN | The text presents these as remaining proof obligations. The prerequisite PASSES do not discharge them. |

## Internal arithmetic audit

### The axioms and order conventions used

The actual Q definition gives the universal closures of successor nonzero, successor injectivity, the predecessor axiom, `x + 0 = x`, `x + Sy = S(x + y)`, `x × 0 = 0`, and `x × Sy = x × y + x`. The actual PA definition adds induction for every arithmetic formula with the other free parameters universally closed. There is no restriction to bounded induction.

The comparison abbreviations are `r < t := exists z (r + Sz = t)` and `r <= t := exists z (z + r = t)`. The different addend positions matter over Q. Here the annex first derives addition commutativity and cancellation in PA, so the subsequent use of ordered differences, endpoint decomposition, and equivalence of `v <= w` with `v < Sw` is justified in the stated theory. None is imported as a universal Q theorem.

The elementary arithmetic paragraph gives the requisite induction variables for the semiring identities. Trichotomy can be read as induction on one argument with the other argument universally quantified; the zero and successor decompositions are supplied by the actual predecessor and successor axioms. Least-number reasoning applies to each fixed formula of arbitrary complexity. Thus its later use for a positive signed linear combination is licensed by the full PA scheme.

### Division and the actual P/B formulas

For division, at `a = d q + r` with `r < d`, discreteness gives `Sr < d` or `Sr = d`. The proposed updates `(q, Sr)` and `(Sq, 0)` satisfy the next equation. If `q < q'`, then `d q + r < d(q + 1) <= d q' <= d q' + r'`; this contradiction proves quotient uniqueness, and cancellation proves remainder uniqueness. Positivity of d gives `q <= d q <= a`; the equation gives `r <= a`. The case `d = 1` is covered, including `a = 0`.

The live pairing formula is the atomic equation

`P(a,b,w) := (a+b) × S(a+b) + (b+b) = w+w`.

The annex's temporary `T(u)` abbreviates the unique solution to `2t = u(u+1)`, with `u <= t`. This relation is proved total by PA induction directly, before the PR-graph theorem. Its successor witness is `t + u + 1`. Therefore the later graph for the PR description H is not being used to establish the earlier pairing lemma. This was a central possible circularity and it does not occur.

For inverse pairing, the bounded maximum of those `u <= w` with `T(u) <= w` exists. If `u < w`, maximality excludes `T(u+1) <= w`; if `u = w`, `T(w+1) >= w+1` excludes it. Hence `T(u) <= w < T(u+1)`. The unique difference b satisfies `b <= u`, and the difference a with `a+b=u` exists. Strict increase of T and the consecutive interval bounds give inverse uniqueness. All temporary function terms can be eliminated through the previously proved unique-output relation.

The live beta formula is

`B(w,i,v) := exists t < Sw exists m < Sw exists q < St (P(t,m,w) and t = d q + v and exists u < d (v + Su = d))`,

where `d = S((Si) × m)`. After decoding `(t,m)` from w, division is applied to t by exactly this positive d. Its witnesses satisfy `t,m <= w`, `q <= t`, and `v <= t`. Thus the strict successor bounds in B admit the witnesses. If `v < d`, the difference witness u in `v + Su = d` satisfies `u < d`, so the final marked existential is equivalent to the remainder condition in PA. The converse is immediate from its equation. The case `m = 0` gives divisor 1 and remainder 0; there is no omitted positive-m hypothesis in beta totality.

### Common multiples and CRT without sequence circularity

The common-multiple induction proves, for fixed w,a, the formula

`exists m (m > w+a and forall k (0 < k and k <= r -> k divides m))`.

Its zero witness is `w+a+1`; the successor witness `(r+1)m` remains greater than w+a even when the multiplier is 1. This establishes all needed finite divisibility without invoking factorial or a product function on a coded sequence.

For Bezout coefficients, signed values are pairs of natural numbers with the displayed cross-addition equality and explicit pair operations. The property that a positive number is a signed linear combination is consequently an arithmetic formula. The least such positive delta exists, because A is one. Dividing A and D by delta produces remainders that are signed linear combinations. A positive remainder would contradict minimality, so both are zero. Coprimality then gives delta = 1. This proves the coefficient identity internally, without an assumed total Euclidean-algorithm code.

The two-modulus step follows by reducing both natural components of the signed value `s(v-r)` modulo D and selecting their difference, adding D when necessary. This gives `0 <= k < D`, including D = 1. The number `r + A k` preserves the first congruence and has residue v modulo D. Multiplying two coefficient identities proves the product coprimality property. Positive divisibility conclusions from signed equations follow by the ordered-difference and cancellation facts already proved; no integer sort is required.

For the moduli `d_i = 1+(i+1)m`, a positive common divisor h greater than 1 of `d_i,d_j` divides `(j-i)m`. The equation `d_i-(i+1)m=1` supplies a signed coefficient identity for h,m. Multiplying it by `j-i` makes h divide `j-i`. Thus `h <= j-i <= n`, so the chosen common multiple m is divisible by h, contradicting the same equation. This argument uses neither prime factorization nor a pre-existing finite CRT theorem.

The stated CRT induction can be expanded into a single formula with existential b,M, positive M, congruence to the unique target at every `i < k`, divisibility of M by each earlier modulus, and coprimality of M with all remaining moduli. At zero, b = 0 and M = 1 satisfy it. At a successor `k <= n`, the two-modulus result supplies `b' = b + M t`, and `M' = M d_k` preserves the divisibility and coprimality clauses. The induction formula can be written as `k <= n+1 -> invariant(k)`, so the final bound introduces no extra induction rule. Its target relation refers directly to `B(w,i,v)` for `i<n` and to a for `i=n`; it assumes no sequence of those targets.

At the last stage, congruence and division uniqueness identify each beta entry of the pair `(b,m)` with its target. The old entries satisfy `v <= w < m` and the new entry satisfies `a < m`; hence all target residues are below their moduli. The pairing bounds justify all B witnesses. In the empty-prefix case n = 0, only the new residue is imposed.

### Collection, graphs, and invariants

For finite collection the induction formula is the entire displayed implication, with the parameters of R retained. From the successor premise one obtains the prefix premise and a witness a for the last position. The induction hypothesis supplies a prefix code, and beta extension appends a. Old witnesses retain their B facts and acquire the new-code bound through beta totality. This proof works for each fixed R of arbitrary arithmetic complexity because PA has its full induction scheme.

For a fixed recursion description d, existence uses `exists y Gamma_d(x,n,y)` as the PA induction formula. Beta extension at position 0 gives the base history. Extension at position `Sn` preserves positions 0 through n and appends the h-output. Old step witnesses are within the preservation range because their B facts imply the old-code bounds. This is a derivation for arbitrary internal n, including nonstandard n in any model of PA.

For uniqueness, fix two witnessing codes and induct on i with the bounded target parameter n retained. The induction formula says that any two values satisfying the respective B facts at i are equal. The g uniqueness theorem establishes the base; the h uniqueness theorem establishes the step. At n it identifies the graph outputs. Prefix restriction of one witnessing code proves the forward successor equation; the same append operation proves its converse. A fresh code for the shortened prefix is unnecessary because Gamma constrains entries through a bound and does not require a canonical numerical prefix code.

The declared Sigma-0-1 class is closed under conjunction, disjunction, unbounded existential quantification, and both marked bounded quantifiers. Thus the literal graph construction has the claimed class, including its bounded universal over existential step witnesses. No quantifier interchange or normal-form theorem is being smuggled into this syntactic classification.

External induction on a fixed description and then on a standard recursion argument gives the standard numerical meaning. The separate numeral-instance argument constructs a finite PA derivation by the initial, composition, and recursion equations, then uses internal uniqueness for every y. It does not posit a uniformly total evaluator over all PR descriptions. The invariant corollary uses exactly its two displayed PA hypotheses, not merely their standard truth.

The graph examples avoid a second circularity: the general graph theorem has already been proved when H is introduced. The identity for H is then matched to the earlier independently constructed triangular relation. Addition and successor composition give the actual pairing and positive-cons graphs. A positive c has a unique predecessor w; pairing inverse components are at most w, hence strictly below c, including the smallest positive code c = 1.

## Fixed-formula evidence audit

The evidence construction starts with the fixed negation-normal-form conversion and gives priority to the wholly bounded case. This resolves overlap of clauses and permits bounded negation/implication through that base case. Auxiliary variables are freshened before substitution.

Each constructor uses only marked bounds. P is atomic and B is bounded under the live convention. For an unbounded existential, its original witness and matrix evidence are paired, so both are at most the pair code. A bounded existential retains the original term bound. The disjunction tag is restricted to 0 or 1, and the pairing witnesses give the appropriate alternative. The bound of a marked quantifier excludes its bound variable; the fresh evidence variable cannot occur in the original bound.

For a bounded universal, the forward implication extracts evidence separately at each index. In the converse, the induction hypothesis gives `forall y < t exists v Ev_psi(y,x,v)`, and the proved finite-collection lemma yields one e with the required B entries. This handles genuinely dependent witnesses: for example, a formula of the shape `forall y < x exists z (z = Sy)` receives evidence for each y and then a code of that evidence, rather than an unjustified single witness for all y. The empty strict bound is witnessed by e = 0. The `<=` variant follows by collection through the successor bound in PA.

Both implications are internal PA derivations for each fixed formula. This supplies the displayed equivalence with an existential bounded matrix. It asserts neither a uniform truth predicate over formula codes nor that an evidence number already is an ND proof code.

## Numerical checker, D1, and modus ponens audit

The governing codes are positive Cantor cons lists and constructor tags, with 0 as the empty list. Proper components are strictly smaller, so length, access, finite-loop updates and course-of-values computations have the stated primitive-recursion constructions. The arbitrary substitution traversal has at most n main visits and at most n auxiliary renamings of at most n nodes each; fresh renaming preserves tree shape and inserted terms are returned as codes without being traversed again. Its three binder cases match the actual total capture-avoiding substitution definition. Alpha comparison uses nearest binder positions and distinct free-variable tags, with a converse through fresh simultaneous binder choices.

The checker uses the actual twenty rules. In particular, tag 8 is implication elimination with the antecedent first and implication second in the body calculus. The rule sheet has the reversed presentation order, and R2:274–277 explicitly supplies that child-order translation. All parameters U are formula/term codes, variable indices or discharge labels. None is a row reference. Discharge is nonvacuous and restricted to the indicated premise branch and formula. The all-variable condition for existential elimination and the free-variable condition for universal introduction match the live calculus.

The parent-count and earlier-reference requirements give one connected tree. Open lists are computed from already constructed subtrees, with the exact discharge filters. A fixed c.e. axiom set is used through its fixed domain index e_T and a certificate for every root open leaf. The fixed bounded Comp formula is explicitly constructed from H1–H4 in `inherited-08710-08876.tex`; each relational expansion is marked bounded. Evaluating one such fixed bounded formula is primitive recursive by induction on its formation. The actual bounded-verification theorem gives exactly its numerical acceptance/domain interface, which is all the numerical proof-code equivalence needs.

D1 uses only a standard proof code supplied by that equivalence and the positive numeralwise representability clause. Since every Q axiom sentence is in T, its Q derivation is also a T derivation. The actual existential introduction rule admits the closed numeral p. No consistency, soundness, internal totality, internal checker invariance or standard-predicate derivability theorem is required for this metatheoretic implication.

For mp, let a be the length of the antecedent proof's row list and b the length of the implication proof's row list. Both are positive after the constructor's tests. Appending the row `[8,z,[a-1,a+b-1],0,0]` gives references strictly below the new row a+b, with the exact premise formulas in the correct order. Shifted old references `a+j` remain earlier than `a+i`. Every old nonroot retains its one parent, each old root gains the new parent, and the new root alone has no parent.

An induction over the copied rows preserves each formula and transforms every old open-leaf index j in the shifted copy into a+j. Every discharge filter therefore removes exactly the old leaves in its own subtree. Equal labels in the two copied trees cause no cross-discharge: their only new common ancestor is implication elimination, which discharges nothing. All old eigenvariable conditions see the same formulas and open assumptions in their own subtree. The new open list is exactly the antecedent proof's list followed by the shifted implication proof's list. The concatenated witness list consequently leaves every V call unchanged. No new axiom membership test or certificate is needed. Sentencehood of the consequent follows from the live free-variable union clause for implication.

Malformed constructor inputs return zero as prescribed. On valid certified inputs, the argument covers empty open lists and empty witness lists. It addresses the certified convention explicitly named in the lemma; it does not silently switch to the optional finite-axiom convention. The specified external algorithm is sufficient for the numerical PR-function assertion. A chosen PR description and arithmetic verification of its checker invariants remain among the explicitly open applications.

## Boundary and counterexample checks

No countermodel was found. The following edge cases were checked by mathematical recomputation and proof inspection:

- `P(0,0,0)` and `B(0,i,0)` for every i; beta totality does not require a positive code or positive second pairing component.
- Division by 1 and division of 0; both quotient/remainder bounds hold.
- Beta extension with n = 0; the old prefix condition is empty. As a separate concrete residue check, the code `9053 = pair_N(126,8)` has entries 0 and 7 at positions 0 and 1, because the divisors are 9 and 17 and the respective remainders of 126 are 0 and 7.
- Empty finite collection and empty bounded universal, witnessed by code 0.
- Nullary initial functions and composition through a nullary function; the displayed empty-conjunction convention leaves the correct graph.
- Minimal positive cons code 1, whose unique head and tail are both 0.
- Two proof trees with equal discharge labels, and inputs with no open assumptions; the new nondischarge root preserves the required open-list/certificate accounting.
- Arbitrary internal lengths in PA: the actual induction formulas retain the history codes, length bounds and other parameters, so the proofs are not restricted to standard finite computations.

These checks supplement the general derivations. Their finite numerical cases do not establish the internal theorems by themselves.

The proof boundary at A:474–524 is accurate. D2 requires a selected rho and internal row-shift, parent-count, open-leaf and certificate invariants. D3 requires a primitive recursive builder for each fixed Sigma-0-1 sentence and an internal verification that its output passes that rho. The evidence theorem alone does not provide that builder. Taking `sigma = exists p rho(p, numeral(code(phi)))` has the required closed Sigma-0-1 form once rho is appropriately chosen, but this remains a conditional downstream use. No GL text or later predicate construction is accepted here.

## Read extents and SHA-256 evidence

All line extents below are source-file line numbers. A partial extent is stated explicitly; hashing a whole file does not claim a whole-file read.

| File | Read extent / file lines | SHA-256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | 1–168 / 168 | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |
| `handbook/restoration/inherited-09262-09327.tex` | 1–253 / 253 | `b49a3b30aff36050841d4f384a6ba80fcf36f4661b3c4085e58d2371b4e003cb` |
| `handbook/restoration/inherited-09328-09438.tex` | 1–546 / 546 | `a6e37fa592e81b888c14a2da97cc70f1a05ec69bae0ce4d36e2e60c59f09c541` |
| `handbook/annex/p05/internal-proof-predicate.tex` | 1–524 / 524 | `c653bf3e1a42e541310435aaa9082238df6b78eedd349400dd252ed26a5083f2` |
| `handbook/restoration/inherited-09080-09098.tex` | 1–19 / 19 | `bfe54e8d15f8e35cd00fca3105029d9558312cc0a7a285e03c67d1e576157223` |
| `handbook/restoration/inherited-09099-09111.tex` | 1–13 / 13 | `38534e090c35db78d99d045d19b3c7f34f1f1aaa8999cf118c7a416cd41d9d2b` |
| `handbook/restoration/inherited-09175-09187.tex` | 1–13 / 13 | `0db98b87928aa115c82883993e2e25b18286779e7ded0399c7148633c0178430` |
| `handbook/restoration/inherited-07678-07752.tex` | 1–75 / 75 | `1b3a7277d05f42cd5e568cc12b851f2e460bdbab4244d11f91f30eff78aa02dd` |
| `handbook/restoration/inherited-08306-08438.tex` | 1–133 / 133 | `0b020970be72999cd771566ba0d6cdb4e4668728362cbd3c0d1606059ee9d2b8` |
| `handbook/restoration/inherited-08439-08709.tex` | 1–90 / 271; governing P/B and their proofs are 1–87 | `95eb4270559303fefc5de2d9bc804a04768ead87d68d9e5d9cbf65079714806a` |
| `handbook/restoration/inherited-08710-08876.tex` | 1–915 / 1104; all Comp definitions and bounded-verification proofs | `4d131a6631a148354f31066316e3b73977df71af66c06fc98158d6c402dbc102` |
| `handbook/restoration/inherited-07851-08048.tex` | 1–261 / 261 | `de01687b7f524f49d6b3e90c9acd038550f7be1551a1aabc771b8bbb3b4b0177` |
| `handbook/restoration/inherited-02193-02340.tex` | 1–148 / 148 | `5ba27894edf744d288008b613adf93eac3d65385f745135de776d5b6011316a3` |
| `handbook/restoration/inherited-03927-04061.tex` | 1–135 / 135 | `2ad2846970d4976177b0fbb8ac59ff8106253f5d155a5e4861956f7f651bf480` |
| `handbook/restoration/inherited-03240-03428.tex` | 1–189 / 189 | `36d7779d6b9bb3caf0c4ef514a79a1c7d8aa10bd4a72290256ea1d09d5db58cc` |
| `handbook/restoration/inherited-03022-03037.tex` | 1–16 / 16 | `2ed53b63d8f69db04f8019d830875b68ade5439932a689701b1e3c28661c5ce5` |
| `handbook/restoration/inherited-03038-03104.tex` | 1–67 / 67 | `8531b8fc91a659ab7c5b131a77fca7aff9c97f0a052e3b78fe0459adec25ffab` |
| `handbook/restoration/inherited-03105-03165.tex` | 1–61 / 61 | `5c062c8a2584c841ed74ec9b546fa502ef0ff4d667a5a702ec56b7c8a49463c9` |
| `handbook/restoration/inherited-03166-03239.tex` | 1–74 / 74 | `d7d08869229f450d219bcb06ffa8e990b60db10f195b76d53e9eccbbc480ac3c` |
| `handbook/registry/calculi/nd-fol.tex` | 1–29 / 29 | `f25549bc18fc4aae212eea32cadc9fffd08e03d712f5df10e9da62f660be5370` |
| `handbook/parts/p05.tex` | 1–40 / 52; checked the arithmetization theorem anchor | `068b90e56bfcf4538aff14f0dbbf428a228a34b12736ca55484b1e3d5e64b326` |
| `handbook/parts/p04/decision-problems-and-arithmetical-hierarchy.tex` | 36–126 / 430; comparison with inherited hierarchy | `7e7a5082c59955a9b539173fdaf105197aaef9eedbeb9f4bcceeea250df7eb4e` |

The three target hashes matched the assignment at initial verification and again at final verification at 21:16 UTC. The report's own final hash is returned separately to avoid a self-referential file hash.
