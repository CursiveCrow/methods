# P4 research: computability and complexity migration

Status: source-backed evidence ledger for the Phase-4 P4 visit. This is not
handbook prose. It does not change a register, mark a row `done`, add a
bibliography or symbol record, or by itself satisfy a treatment requirement.
The migrated substrate is the frozen `v1.1-verified` Part V of
`source/formal-logic-reference.tex`, lines 7494--9078. External sources were
checked on 2026-08-11.

## Evidence policy and treatment boundary

- **Source-verified** means that the stated fact is present in the frozen
  v1.1 source at the cited lines.
- **Externally verified** means that the claim or metadata was checked against
  a primary publication, a publisher record, an author-hosted text, or the
  identified authoritative modern reference at the locator given.
- **Derived** means that the formulation follows from cited facts by the
  argument printed here. It is not a quotation and is not independently a
  source for a handbook `cited=` status.
- **Claim ceiling** is the strongest treatment licensed by the binding row and
  the located evidence. `E`, `T`, `S`, and `P` remain entry, table/treatment,
  statement/survey, and pointer obligations respectively; none is a proof
  status. A body theorem still needs exactly `proved=annex:<id>`,
  `sketched=annex:<id>`, or `cited=<bibkey>` under
  `handbook/CONVENTIONS.md`.
- **Do not claim** identifies a tempting strengthening, a missing hypothesis,
  or a formulation for which the sources located here do not supply the
  advertised result.

The words “in full” in `N-a-017` specify the finite-injury construction as the
subject of the table/treatment. They do not override the treatment code `T`,
do not create a `proved=` obligation, and do not erase the narrower evidence
instruction in `D-P5-004` (“statement + method sketch”). The goal objective
also requests an `hbmethod` with a sketched annex. The compatible delivery is:

1. a body definition of the priority requirements and a body `hbmethod` that
   gives the stage mechanism, restraints, initialization, and finite-injury
   invariant;
2. a Friedberg--Muchnik theorem whose status is
   `sketched=annex:<finite-injury-id>`; and
3. an annex sketch beginning with `\sketchnote{...}` that names every omitted
   coding, convergence, and uniformity verification.

This is a **claim ceiling**, not a claim that the theorem has been proved. A
complete annex proof could justify `proved=` only if independently supplied
and checked; neither `D-P5-004` nor `N-a-017` requires that upgrade.

## Binding P4 inventory

### Depth rows

| row | exact topic | treatment / priority / effort | dependency | evidence consequence |
|---|---|---|---|---|
| `D-P5-001` | partial recursive functions and TM equivalence | E / must / L | `R-005` | define the recursive-function class before the equivalence and tie the theorem to the live acceptable numbering |
| `D-P5-002` | Church--Turing thesis | S / must / S | none | historical/philosophical calibration only; never label the thesis a theorem |
| `D-P5-003` | degree poset, join, and jump on degrees | E / should / M | `R-004` | prove or cite representative-independence and use the repaired convergence convention |
| `D-P5-004` | Post's problem, finite injury, Friedberg--Muchnik | S / should / M | `D-P5-003` | theorem statement plus method sketch; see the ceiling reconciliation above |
| `D-P5-005` | simple/creative sets, Myhill, Rice--Shapiro | S / should / M | none | exact numbering hypotheses are mandatory for index-set theorems |
| `D-P5-006` | Kolmogorov invariance, incompressibility, halting-probability pointer | S / could / M | none | fix plain versus prefix-free complexity; the halting probability is only a pointer |
| `D-P5-007` | PSPACE, hierarchy theorems, PH, class ladder | T / must / M | none | every containment edge must be tagged equality, known strict, inclusion only, or open |
| `D-P9-002` | analytical hierarchy and basic results | T / should / M | none | use the lightface hierarchy and state `Delta^1_1 = HYP` with its coding convention |

### New-content rows

| row | binding deliverable | treatment / priority / effort | claim ceiling and exclusions |
|---|---|---|---|
| `N-a-016` | degree poset, join, jump, Kleene--Post incomparable degrees below `0'` | E / must / M | full entry; distinguish the Kleene--Post degrees from c.e. incomparable degrees |
| `N-a-017` | Post's problem and Friedberg--Muchnik finite injury | T / must / M | table/method treatment with sketched theorem; infinite-injury and `0'''` priority methods excluded |
| `N-a-018` | simple/creative sets, `<=_m`, `<=_1`, Myhill isomorphism | T / should / M | table treatment; add Rice--Shapiro because `D-P5-005` binds it |
| `N-a-019` | hyperarithmetical/analytical hierarchy, `Delta^1_1=HYP`, `O` sketch | S / should / M | survey/statement; alpha-recursion excluded |
| `N-a-020` | Kolmogorov invariance, incompressibility, Chaitin incompleteness | T / should / M | table treatment; algorithmic randomness beyond basics excluded |
| `N-a-021` | MRDP and Hilbert's tenth problem, proof survey with Pell material | S / must / M | theorem statement and proof survey; a full MRDP proof is expressly out of scope |
| `N-a-022` | semigroup and group word problems | T / could / S | table; semigroup result may receive the stronger local treatment only if its reduction is actually supplied |
| `N-a-023` | Busy Beaver definition and Rado noncomputability | T / could / S | short definition/theorem unit; numerical values depend on the machine convention |
| `N-a-024` | computable presentations and structure indices | P / could / S | pointer only; do not silently close the P3-owned `D-P4-011` row |
| `N-a-063` | normal form, `s-m-n`, and TM/partial-recursive equivalence | E / must / L | full entry and equivalence theorem; depends on live numbering adequacy |
| `N-a-064` | complexity ladder, time/space hierarchies, completeness catalog | T / must / M | table/treatment; per-logic P9/P14 claims remain pointers |

`N-x-014` keeps Type-2 effectivity, represented spaces, and Weihrauch degrees
out of scope. A sentence pointing forward may name the excluded field, but no
new framework should be developed in P4.

### P4-relevant apparatus slice

| row | required artifact | acceptance condition |
|---|---|---|
| `A-045` | machine-equivalence table | each row fixes a model, function convention, equivalence theorem, evidence status, and source; the Church--Turing thesis is a pointer, not an equivalence edge |
| `A-046` | undecidability catalog | halting, Rice, H10, word problems, Wang tiling, and FOL validity each have an encoded instance set and a primary reduction/source |
| `A-047` | arithmetical-hierarchy table | preserve v1.1's closure/prefix convention, complete sets, Post theorem, and jump correspondence; cite `R-006` repair |
| `A-048` | analytical-hierarchy table | lightface `Sigma^1_n/Pi^1_n/Delta^1_n`, quantifier form, complete examples, and relation to second-order arithmetic |
| `A-049` | degree/jump facts | representative-independent definitions; join, jump, Kleene--Post, Post's problem, and Friedberg--Muchnik with separate evidence rows |
| `A-050` | complexity ladder | definitions, inclusions, known strict separations, open equalities, and canonical complete problems under one stated reduction |
| `A-052` | descriptive-complexity table | ESO/NP and FO(LFP)/P with finite-structure vocabulary and the order hypothesis exactly stated |
| `A-124` | arithmetical-hierarchy figure | no strict arrow unsupported by the cited theorem; labels agree with `A-047` |
| `A-125` | analytical-hierarchy figure | visibly lightface; `Delta^1_1=HYP`; no conflation with the boldface projective hierarchy |
| `A-126` | degree/jump figure | schematic, not metric; distinguish Kleene--Post incomparable degrees from c.e. Friedberg--Muchnik degrees |
| `A-127` | complexity inclusion figure | “Hasse-style” means layout only; edges encode inclusion/strictness/open status rather than unproved cover relations |
| `A-163` | computability/complexity symbols | intake every new glyph-role pair before first use; do not overload the live jump, reduction, or hierarchy notation |
| `A-182` | bibliography intake | use verified records below; do not repurpose the unrelated live `Rado1964` key |
| `A-186` | further reading | separate historical primaries from modern systematic references |
| `A-189` | body-to-annex cross-references | every finite-injury or other sketch target is bidirectional and lists omissions |

This is the part-relevant slice of the global Phase-4 apparatus registry, not a
claim that P4 owns or discharges all 129 apparatus rows. `A-051` is the later
master table of logics; P4 can supply complexity pointers but cannot close it.

### Repair and migration contracts

| row | frozen v1.1 locus | P4 preservation obligation |
|---|---:|---|
| `R-002` | 8710--8796 | keep one machine/history coding and the bounded extraction needed for `Comp` and the `Sigma^0_1` classification |
| `R-004` | 8931--9078 | use accepting-with-valid-output convergence throughout the jump; retain the cited/sketched status chain |
| `R-005` | 7904--8002 | retain the labeled enumeration theorem for the bespoke numbering and cite it at every numbering-dependent construction |
| `R-006` | 8309--8708 | retain the proved bounded-collection and closure-to-prefix-normal-form bridge |
| `R-035` | 7630--7639 | retain exactly one well-formed partial-computability biconditional |

Migration rows `S-007`, `S-008`, `L-010`, `L-012`, and `L-013` must be
accounted for by the P4 driver/finalizer. This research note does not change
their status.

## Frozen v1.1 Part V source inventory

The source has three chapters: Machines and Effective Procedures
(7497--7849), Universal Computation, Reductions, and Fixed Points
(7851--8246), and Logical Decision Problems and the Arithmetical Hierarchy
(8248--9078). The following inventory is source-verified and records every
status-bearing result plus the definitions and warnings on which new P4
material depends.

| source lines | item | frozen evidence / migration role |
|---:|---|---|
| 7509--7584 | Turing machine; configuration and computation | exact deterministic single-tape substrate |
| 7630--7639 | partial computable function | repaired `R-035` definition; keep output/divergence convention |
| 7670--7676 | machine formalism versus complexity warning | computability equivalence does not preserve exact time/space costs |
| 7681--7715 | primitive recursive functions/relations | base for the new partial-recursive definition |
| 7717--7732 | every primitive recursive function is total computable | proof sketch; do not upgrade on migration |
| 7756--7793 | decidable, c.e., relations, decision and recognition | standing vocabulary |
| 7795--7805 | machine form of decidability | complete proof in source |
| 7808--7828 | four forms of c.e. sets | proof sketch; empty-range exception is explicit |
| 7830--7842 | decidable iff set and complement are c.e. | complete proof in source |
| 7904--7933 | renaming invariance | complete proof; supports bespoke numbering |
| 7935--8002 | enumeration/adequacy theorem | complete proof; fixed `R-005`; load-bearing for equivalence, Rice, and priority |
| 8004--8024 | universal computation | proof sketch; exact invalid-output convention retained |
| 8026--8047 | parameter theorem (`s-m-n`) | cited theorem; compiler invariant omitted |
| 8052--8079 | many-one reduction, closure lemma, direction warning | definition plus complete proof |
| 8084--8121 | self-application domain `K` and complement | complete diagonal proof and corollary |
| 8123--8142 | binary application-domain equivalence | worked use of the parameter theorem |
| 8147--8176 | recursion theorem | proof sketch because the program transformation is omitted |
| 8190--8237 | extensional index property and Rice theorem | complete proof plus syntactic/semantic warning |
| 8256--8279 | FOL validity undecidable and c.e. | theorem cited to Church/Turing; corollary completely proved from calculus enumeration |
| 8283--8298 | restricted-signature warning and Trakhtenbrot | cited; do not transfer unrestricted/FOL claims to arbitrary signature fragments |
| 8309--8429 | arithmetic language and hierarchy definitions | exact source convention for `A-047/A-124` |
| 8439--8708 | pairing, beta coding, contraction, bounded collection, prefix normal form | complete proofs; fixed `R-002/R-006` dependencies |
| 8710--8796 | history coding and bounded verification | proof sketch; full transcription and step checks remain omitted |
| 8798--8816 | c.e.=`Sigma^0_1`, decidable=`Delta^0_1` | proof sketch inherited from bounded verification |
| 8818--8828 | many-one hardness/completeness | exact distinction from semantic/deductive/proof completeness |
| 8830--8849 | `K`, complement, and `TOT` hierarchy completeness | cited theorem; prefix-normal-form bridge explicit |
| 8851--8875 | arithmetical hierarchy strictness | cited theorem plus warning that syntax gives only an upper bound |
| 8905--8929 | oracle machines and Turing reducibility | exact decision and convergence conventions |
| 8931--8949 | Turing jump | repaired `R-004` definition using valid numerical output |
| 8951--8980 | relativized adequacy | proof sketch; uniform parameter map independent of oracle |
| 8985--9021 | jump theorem | proof sketch because it depends on sketched relativized adequacy |
| 9023--9048 | Post theorem | cited theorem; source explains the prefix/closure transfer |
| 9050--9078 | jump convention bridge and monotonicity | proof sketch; do not upgrade any downstream status through it |

The new P4 material must not lower these definitions or silently convert a
source sketch/citation into a complete proof. In particular, degree-level
jump claims must refer to the repaired `B'` convention or explicitly invoke
the source's convention bridge.

## Research package 4.1: recursive-function models and thesis calibration

### Definitions that must precede the equivalence

**Externally verified formulation.** For each arity, define the partial
recursive functions as the least class of partial maps
`N^k \rightharpoonup N` containing zero, successor, and projections and closed
under composition, primitive recursion, and unbounded minimization. For
minimization, `mu y[g(x,y)=0]` is defined at `x` only when a least zero is
reached with every earlier required computation defined. This divergence
clause is load-bearing for an equivalence of *partial* functions. Source:
Kleene, *Introduction to Metamathematics* (1952), Chapter XI, especially
§§54--57 (`Kleene1952`); Kleene, “General Recursive Functions of Natural
Numbers,” §§1--7 (`Kleene1936`, DOI
[`10.1007/BF01565439`](https://doi.org/10.1007/BF01565439)).

**Externally verified theorem (safe ceiling).** For every `k >= 1` and every
partial map `f:N^k \rightharpoonup N`, the following are equivalent after the
book's input/output encodings have been fixed:

1. `f` is computed by a Turing machine in the v1.1 sense;
2. `f` is partial recursive in the preceding closure sense.

The historical Turing paper proves identity of Turing-computable,
lambda-definable, and general recursive numerical functions by proving the two
directions then missing and invoking the already available third direction.
Source: Turing, “Computability and lambda-definability,” *Journal of Symbolic
Logic* 2(4) (1937), 153--163, opening extract and §§1--8, DOI
[`10.2307/2268280`](https://doi.org/10.2307/2268280). For a modern
partial-function presentation, use `Kleene1952`, Chapter XI, or `Soare2016`,
Chapters 1--2. This supplies `D-P5-001/N-a-063`; it does not by itself prove
equivalence to the handbook's bespoke numbering, so the implementation must
also cite the source-verified enumeration theorem at 7935--8002 (`R-005`).

**Externally verified normal form.** For each input arity `k` there are
primitive recursive `T_k(e,x_1,...,x_k,y)` and `U(y)` such that every partial
recursive `f` has an index `e` satisfying

`f(x_1,...,x_k) \simeq U(mu y T_k(e,x_1,...,x_k,y))`.

Conversely, every function displayed in this form is partial recursive. The
predicate must be tied to the chosen computation-code convention; “`T` is
primitive recursive” is not permission to reuse the letter for the v1.1
bounded formula `Comp` without a bridge. Source: Kleene, *Introduction to
Metamathematics*, §52 and Chapter XI (`Kleene1952`); compare the normal-form
result used in Moschovakis, “Hyperarithmetical Sets,” Appendix 5 and §3D,
author PDF pp. 15--16
([PDF](https://www.math.ucla.edu/~ynm/papers/hyp.pdf)).

**Source-verified parameter theorem.** For `m,n >= 1`, v1.1 has a total
computable `par_n^m` with
`phi_{par_n^m(e,a)}(x) \simeq phi_e(a,x)` at 8026--8047. This is the `s-m-n`
theorem under the local name. Preserve that map rather than creating a second
unrelated compiler. The source status is `cited=Kleene1952`; a new proof would
need to supply the omitted concrete table compiler and invariant.

### Register-machine and lambda columns for `A-045`

**Externally verified exact URM.** Shepherdson and Sturgis's Unlimited
Register Machine has registers `1,2,...`, each storing a natural number, while
each finite program mentions only finitely many registers. Its six displayed
instruction forms are: `P(n)` (increment register `n`); `D(n)` (decrement a
nonzero register `n`); `O(n)` (set register `n` to zero); `C(m,n)` (copy the
content of `m` to `n`, with `m != n`); `J[E1]` (unconditional transfer); and
`J(m)[E1]` (transfer through exit 1 exactly when register `m` is zero, otherwise
take the normal next-line exit). A program is a finite sequence of such
instructions; execution begins at line 1 and halts on reaching the
nonexistent line after the last. Source: J. C. Shepherdson and H. E. Sturgis,
“Computability of Recursive Functions,” *Journal of the ACM* 10(2) (1963),
217--255, §2, pp. 219--221
([paper PDF](https://www.cs.cmu.edu/~15455/resources/ShepherdsonSturgis1963.pdf)),
DOI
[`10.1145/321160.321170`](https://doi.org/10.1145/321160.321170).

**Externally verified result and standing.** Section 3 defines partial
recursive functions using successor, zero, projections, composition,
primitive recursion, and least-number search, including the definedness of
all earlier search values. It constructs a URM routine for every such partial
recursive function and says that undefined inputs run without stopping; see
§3, pp. 222--224. The paper then reduces through restricted machines to a
two-symbol Turing machine; see the program announced in the introduction and
§9. Thus `A-045` may name *the Shepherdson--Sturgis URM* and state equivalence
at the level of partial numerical functions. It must not use the bare label
“register machine” as though the theorem covered an unspecified instruction
set, and it must not replace the six source instructions with a modern
three-instruction variant without a separate simulation proof/source.

**Externally verified.** The lambda-definability row may cite Turing's 1937
paper above. State what counts as the represented natural-number function and
avoid treating equality of raw lambda terms as equality of computed partial
functions. If the table includes pairwise arrows, each arrow needs a source or
a derivation from two explicitly stated equivalences; transitive arrows should
be labelled derived rather than primary.

### Church--Turing discussion (`D-P5-002`)

**Externally verified historical claim.** Church and Turing proposed formal
explications of the informal notion of effective calculability; Turing's
machine argument and the subsequent equivalence results supply evidence for
the identification, not a theorem whose conclusion quantifies over a formally
defined class of all intuitive procedures. Turing's 1937 paper explicitly
describes “effective calculability” as the intuitive idea whose exact formal
counterparts are being compared. Soare distinguishes Church's identification
with general recursion from Turing's analysis via machines and emphasizes the
thesis/theorem boundary. Sources: Turing 1937, opening extract and pp. 153--154
([Cambridge record](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/computability-and-definability/FE8B4FC84276D7BACB8433BD578C6BFD));
Soare, “Computability and Recursion,” *Bulletin of Symbolic Logic* 2(3)
(1996), 284--321, §§1--3, DOI
[`10.2307/420992`](https://doi.org/10.2307/420992).

**Claim ceiling.** The body may say that the Church--Turing thesis identifies
effectively calculable numerical functions with Turing-computable functions,
explain why model equivalences and robustness support it, and state that it is
not proved by those equivalences. Do not write “Turing proved the
Church--Turing thesis,” “every physical process is Turing computable,” or
“equivalent models have equal complexity.” The last claim is already blocked
by the source warning at 7670--7676.

### `A-045` recommended columns

| model | exact object/function convention | verified result | evidence |
|---|---|---|---|
| v1.1 single-tape TM | partial numerical function with valid-output convergence | local numbering enumerates exactly the TM-computable partial functions | source 7630--7639 and 7935--8002, complete proof |
| partial recursive | least partial-function class under the listed schemes | same partial numerical functions as TMs | `Kleene1936`, `Kleene1952`, Turing 1937 lambda paper |
| Shepherdson--Sturgis URM | countably many natural-number registers; finite programs using `P,D,O,C,J,J-zero` exactly as specified above | computes exactly the partial recursive numerical functions; paper reduces to a two-symbol TM | Shepherdson--Sturgis 1963, §§2--3 and §9 |
| lambda calculus | fixed numeral representation and conversion/evaluation convention | same numerical functions in Turing's historical result | Turing 1937 lambda paper |
| effective calculability | informal explicandum, not a fourth formal model | Church--Turing thesis pointer | Turing 1937; Soare 1996 |

## Research package 4.4: degrees, priority, and c.e.-set structure

### Exact degree definitions (`D-P5-003`, `N-a-016`, `A-049`)

Fix subsets of `N` and the source-verified reducibility `<=_T` from
8905--8922.

- **Definition.** `A \equiv_T B` iff `A <=_T B` and `B <=_T A`. A Turing
  degree is an equivalence class `[A]_T`. Its standing is a class of subsets
  of `N`, not a set or an index. The order is `[A]_T <= [B]_T` iff
  `A <=_T B`. Well-definedness is derived from transitivity of `<=_T`.
  Source: Kleene--Post, “The Upper Semi-Lattice of Degrees of Recursive
  Unsolvability,” §§1--2 (`KleenePost1954`, DOI
  [`10.2307/1969708`](https://doi.org/10.2307/1969708)); Moschovakis,
  “Hyperarithmetical Sets,” §1A, author PDF pp. 2--3.
- **Definition.** For a fixed computable pairing, let
  `A \oplus B={2x:x in A} union {2x+1:x in B}`. Then
  `[A]_T join [B]_T := [A \oplus B]_T`. **Derived verification:** each side
  reduces to the join by parity; if both reduce to `C`, dispatch on parity to
  reduce the join to `C`. Thus it is the least upper bound. Source for the
  upper-semilattice setting: `KleenePost1954`, title and §§1--2.
- **Definition.** The jump of a degree is `[A]_T' := [A']_T`, with `A'` the
  repaired v1.1 jump at 8931--8949. Representative-independence uses jump
  monotonicity: `A <=_T B` implies `A' <=_m B'`, sketched in v1.1
  9050--9078. Consequently the body must not label that local derivation
  `proved=` unless the omitted uniform table transformation is supplied.
  Source: v1.1 8931--9078; `R-004`.
- **Definition.** `0=[emptyset]_T` and `0'=[emptyset']_T`. A c.e. degree is a
  degree containing a c.e. set. This is not the same as a degree c.e. as an
  object.

**Externally verified Kleene--Post theorem.** There are degrees `a,b < 0'`
with neither `a <= b` nor `b <= a`. The classical Kleene--Post construction
produces sets computable in `0'` (equivalently `Delta^0_2` under the standard
limit lemma), not the later c.e. solution to Post's problem. Source:
`KleenePost1954`, especially the incomparable-degree construction; modern
statement in `Soare2016`, Chapters 7--8. Do not caption the Kleene--Post nodes
in `A-126` “incomparable c.e. degrees.”

### Post's problem and finite injury (`D-P5-004`, `N-a-017`)

**Externally verified problem and theorem.** Post asked whether there is a
c.e. set `A` with `0 < deg_T(A) < 0'`. Friedberg and Muchnik independently
proved the stronger symmetric form: there are c.e. sets `A,B` such that
`A not<=_T B` and `B not<=_T A`. Sources: Post, “Recursively Enumerable Sets
of Positive Integers and Their Decision Problems,” pp. 284--316
(`Post1944`, DOI
[`10.1090/S0002-9904-1944-08111-1`](https://doi.org/10.1090/S0002-9904-1944-08111-1));
Friedberg, “Two Recursively Enumerable Sets of Incomparable Degrees of
Unsolvability,” pp. 236--238 (`Friedberg1957`, DOI
[`10.1073/pnas.43.2.236`](https://doi.org/10.1073/pnas.43.2.236)); Muchnik,
“On the Unsolvability of the Problem of Reducibility in the Theory of
Algorithms,” *Doklady Akademii Nauk SSSR* 108 (1956), 194--197
(`Muchnik1956`).

**Derived pedagogical construction schema.** Relative to the acceptable
enumeration of oracle computations, list requirements

`R_e: Phi_e^B != A` and `S_e: Phi_e^A != B`

in a computable priority ordering. A strategy chooses a fresh witness outside
the set it controls, waits for the relevant oracle computation to converge
with the diagonal value, enumerates the witness into the opposite set, and
restrains the oracle below the use of that computation. Action by a
higher-priority strategy initializes lower-priority strategies and cancels
their witnesses/restraints. The induction invariant is: after the last action
of higher-priority strategies, a strategy is injured no more; it either never
sees the convergence needed for the alleged reduction, or acts once and
preserves a disagreement below its final restraint. This is a derived method
outline from Friedberg--Muchnik as systematized in Rogers, *Theory of Recursive
Functions and Effective Computability*, Chapters 10--11 (`Rogers1967`), and
Soare, *Turing Computability*, the finite-injury chapters (`Soare2016`).

The annex sketch must make the following hypotheses and omissions explicit:

1. the stage approximation to c.e. sets and the enumeration of oracle
   functionals are effective and agree with the live numbering;
2. witnesses are chosen fresh above all active higher restraints;
3. “use” means the largest oracle position queried by a convergent finite
   computation, with a stated convention if no query occurs;
4. enumeration below a protected use is prohibited unless a higher-priority
   strategy acts;
5. initialization discards a lower witness and restraint but never removes an
   already enumerated number;
6. induction on priority proves finitely many injuries and final satisfaction;
7. c.e.-ness follows because enumeration actions are effective stage actions;
8. the proof that every alleged reduction occurs in the requirement list and
   the translation from the local machine numbering are either written or
   named as omissions.

The body must not say “each strategy acts once” without the qualifier “after
its last injury,” must not infer incompleteness merely from simplicity, and
must not extend this finite-injury sketch to infinite-injury or `0'''`
constructions.

### Simple, creative, and extensional c.e. index sets (`D-P5-005`, `N-a-018`)

Use an acceptable numbering `(W_e)` of the c.e. subsets of `N`; for example
`W_e=dom(phi_e)`. The numbering hypothesis is essential for Myhill and
Rice--Shapiro.

- **Definition.** `A <=_m B` iff a total computable `f` satisfies
  `x in A <=> f(x) in B` for every `x`. This is already source-verified at
  8052--8060. `A <=_1 B` has the additional requirement that `f` is injective.
  Source: Moschovakis, “Hyperarithmetical Sets,” §1A, pp. 2--3.
- **Definition.** A c.e. set `S` is simple iff its complement is infinite and
  contains no infinite c.e. subset. Source: `Post1944`, §§4--6; `Rogers1967`,
  Chapter 8.
- **Definition.** A set `P` is productive iff there is a partial computable
  function `p` such that whenever `W_e subseteq P`, `p(e)` is defined and lies
  in `P \ W_e`. A c.e. set `C` is creative iff its complement is productive.
  The partial-versus-total convention for the productive function must match
  the selected source. Source: Myhill, “Creative Sets,” §§1--3, *Zeitschrift
  fuer mathematische Logik und Grundlagen der Mathematik* 1(2) (1955),
  97--108, DOI
  [`10.1002/malq.19550010205`](https://doi.org/10.1002/malq.19550010205).
- **Externally verified Myhill package.** Under an acceptable numbering,
  creative sets are exactly the c.e. sets complete under many-one reduction;
  any two creative sets are computably isomorphic, meaning a computable
  permutation `pi` of `N` maps one onto the other. Source: Myhill 1955,
  especially the completeness/isomorphism results; `Rogers1967`, Chapters
  8--9. Keep “many-one complete” and “one-one equivalent/isomorphic” as
  distinct conclusions.
- **Externally verified Rice--Shapiro formulation.** Let `C` be an extensional
  class of c.e. sets and `I_C={e:W_e in C}`. Then `I_C` is c.e. iff there is a
  c.e. family `F` of codes of finite sets such that, for every c.e. `W`,
  `W in C <=> (exists D in F)(D subseteq W)`. This includes the empty class by
  allowing `F` empty. Source: `Rogers1967`, the Rice--Shapiro theorem. An
  authoritative exact restatement appears in Nancy Johnson, “Rice Theorems
  for `Sigma_n^{-1}` Sets,” *Canadian Journal of Mathematics* 29(4) (1977),
  794--805, opening extract, DOI
  [`10.4153/CJM-1977-082-3`](https://doi.org/10.4153/CJM-1977-082-3). Johnson
  records that Rice conjectured the theorem and McNaughton, Shapiro, and Myhill
  proved it independently.

**Do not claim.** A simple set need not have intermediate Turing degree;
simplicity alone does not rule out completeness. Rice--Shapiro is not a claim
about every semantic property of arbitrary programs: it concerns c.e. index
sets in an acceptable numbering and an effective finite-witness condition.
Myhill isomorphism supplies a computable permutation, not literal equality of
creative sets.

### `A-049/A-126` fact and figure rows

| fact/node | exact statement | source/status |
|---|---|---|
| `0` | least Turing degree | derived from computable-set definition |
| join | `[A] join [B]=[A\oplus B]`, least upper bound | `KleenePost1954`; short derivation above |
| jump | well-defined degree operator and `[A] < [A]'` | v1.1 8985--9078, sketch-dependent locally; cite source if stated as theorem |
| Kleene--Post `a,b` | incomparable degrees below `0'`, not asserted c.e. | `KleenePost1954`, cited |
| Friedberg--Muchnik `a,b` | incomparable c.e. degrees, hence both strictly between `0` and `0'` | `Friedberg1957`, `Muchnik1956`, cited/sketched |

The figure must say “schematic; not to scale.” A vertical position means only
the displayed order relation. Do not draw a cover edge, a distance, a lattice
meet, or an exhaustion of all degrees. If jump arrows `x -> x'` appear, do not
identify the jump of an arbitrary intermediate degree with `0'`.

## Research package 4.5: frontiers of computability

### Lightface analytical and hyperarithmetical hierarchy (`N-a-019`, `D-P9-002`)

Fix the two-sorted language of second-order arithmetic with number variables
over `N` and function (equivalently, coded set) variables over `N^N`. A matrix
is *arithmetical* when it contains only number quantifiers after its displayed
function parameters are treated as predicates/functions.

**Externally verified definitions.** A lightface `Sigma^1_n` relation has a
definition with `n` alternating blocks of function quantifiers, beginning
existentially, followed by an arithmetical matrix; `Pi^1_n` begins universally;
`Delta^1_n=Sigma^1_n intersection Pi^1_n`. Parameters change the pointclass
and must be displayed if permitted. Source: Moschovakis, “Hyperarithmetical
Sets,” §3A, author PDF pp. 14--15
([PDF](https://www.math.ucla.edu/~ynm/papers/hyp.pdf)); Kleene,
“Hierarchies of Number-Theoretic Predicates,” §§1--3, *Bulletin of the AMS*
61(3) (1955), 193--213, DOI
[`10.1090/S0002-9904-1955-09896-3`](https://doi.org/10.1090/S0002-9904-1955-09896-3).

**Externally verified fundamental theorem.** For subsets of `N`, the
hyperarithmetical sets are exactly the lightface `Delta^1_1` sets, uniformly
in the standard effective codings. Moschovakis states the two inclusions as
Theorem 3D.4 (`HYP subseteq Delta^1_1`) and Theorem 3E.1
(`Delta^1_1 subseteq HYP`), author PDF p. 16. This supports the exact displayed
equality `Delta^1_1=HYP`; it does not identify HYP with `Sigma^1_1` or
`Pi^1_1`.

**Externally verified complete examples.** Let `WF` be the set of indices for
recursive binary relations that are well-orders on their fields under a fixed
effective coding. `WF` is `Pi^1_1`-complete, and its complement `IF` (the
ill-founded recursive relations) is `Sigma^1_1`-complete. Moschovakis uses
`W` for the well-order codes and gives the uniform completeness reduction in
§3E, especially Lemmas 3E.2--3E.3 and the discussion on pp. 17--18. The
handbook must define whether invalid relation codes are outside `WF` before
using the complement statement.

**Ordinal-notation sketch ceiling.** Kleene's `O` is a coding-dependent set
generated by effective clauses for a base notation, successors, and effective
limits, together with a partial ordering of notations. Its elements denote
recursive ordinals, but distinct elements can denote the same ordinal.
`N-a-019` licenses only a sketch: give the clauses and the role of `O` in
iterating the jump; cite the classification results rather than proving them.
Sources: Kleene 1955, §§6--8; Rogers 1967, Chapter 16; Moschovakis 2016,
§§2--3. Do not write as though `O` were an injective canonical numbering of
all countable ordinals, and do not open the excluded alpha-recursion topic.

#### `A-048` table content

| level | allowed normal form | canonical evidence row | ceiling/source |
|---|---|---|---|
| arithmetical | number quantifiers only | all arithmetical sets lie in `Delta^1_1` | Moschovakis 2016 §§3A--3D |
| `Sigma^1_1` | `exists alpha theta(n,alpha)` with arithmetical `theta` | `IF` under the fixed recursive-relation coding | `Sigma^1_1`-complete; Moschovakis §3E |
| `Pi^1_1` | `forall alpha theta(n,alpha)` with arithmetical `theta` | `WF` | `Pi^1_1`-complete; Moschovakis §3E |
| `Delta^1_1` | both `Sigma^1_1` and `Pi^1_1` | `HYP` | equality by Theorems 3D.4 and 3E.1 |
| `Sigma^1_n/Pi^1_n`, `n>1` | alternating function-quantifier blocks | no new complete example required by the live row | definition/table only; Kleene 1955 |

`A-125` should place the arithmetical sets inside `Delta^1_1`, display
`Delta^1_1=Sigma^1_1 intersection Pi^1_1=HYP`, and use separate branches for
`Sigma^1_n` and `Pi^1_n`. The caption must say “lightface analytical
hierarchy.” A figure copied from the boldface projective hierarchy is not an
acceptable substitute.

### Kolmogorov complexity (`N-a-020`, `D-P5-006`)

Fix finite binary strings. Two notions must not be mixed:

- for a partial computable decompressor `V:{0,1}^* \rightharpoonup {0,1}^*`,
  plain complexity is `C_V(x)=min{|p|:V(p)=x}`;
- for a prefix-free partial computable machine `V`, prefix complexity is
  `K_V(x)=min{|p|:V(p)=x}`.

The minimum is infinite if there is no program, though an optimal universal
machine gives every finite string a finite description. Source: Grunwald and
Vitanyi, “Shannon Information and Kolmogorov Complexity,” §§2.2--2.3, author
PDF pp. 11--13
([PDF](https://homepages.cwi.nl/~paulv/papers/info.pdf)); Li and Vitanyi,
*An Introduction to Kolmogorov Complexity and Its Applications*, 3rd ed.,
Chapters 2--3, DOI
[`10.1007/978-0-387-49820-1`](https://doi.org/10.1007/978-0-387-49820-1).

**Externally verified invariance theorem.** There is an optimal machine `U`
such that for every machine `V` there is a constant `c_V` satisfying
`C_U(x) <= C_V(x)+c_V` for every string `x`; the prefix-free version has the
same form with `K`. The constant depends on `U` and `V`, not on `x`. Source:
Grunwald--Vitanyi, §2.2, pp. 11--12; Kolmogorov, “Three approaches to the
definition of the concept ‘quantity of information’,” *Problemy Peredachi
Informatsii* 1(1) (1965), 3--11
([MathNet record](https://www.mathnet.ru/eng/ppi68)).

**Derived incompressibility count.** For fixed plain `U`, fewer than
`2^(n-c)` strings of length `n` have `C_U(x)<n-c`, because there are fewer
than `2^(n-c)` programs shorter than `n-c`. Hence the fraction of length-`n`
strings compressed by at least `c` bits is less than `2^(-c)`. This counting
argument is derived; the externally verified probability formulation and
noncomputability discussion appear in Grunwald--Vitanyi §2.3, p. 13. Do not
replace “fewer than” with an equality, and do not infer that a particular
string is incompressible without a separate argument.

**Externally verified computability boundary.** For an optimal effective
machine, `C` and `K` are upper semicomputable but not computable. Source:
Grunwald--Vitanyi §2.3; Li--Vitanyi, Chapter 2. The numerical value is machine
dependent up to an additive constant, so short-string comparisons are not
canonical.

**Chaitin-style incompleteness, safe hypothesis form.** Fix an optimal
prefix-free machine `U`, an arithmetic coding of strings/programs, and a
computably axiomatized theory `T` capable of formalizing the relevant finite
computations. Assume `T` is sound for the complexity lower-bound sentences it
proves. Then there is a constant `b_{T,U}` such that `T` proves no true
sentence `K_U(x)>n` with `n>b_{T,U}`. The bound depends on the theory, machine,
and coding. Source: Chaitin, “Information-Theoretic Limitations of Formal
Systems,” *Journal of the ACM* 21(3) (1974), 403--424, DOI
[`10.1145/321832.321839`](https://doi.org/10.1145/321832.321839); modern
formulation in Li--Vitanyi, the incompleteness section of Chapter 2. The
handbook should either quote the exact source's soundness/consistency
hypothesis or use the stronger soundness formulation above; it must not state
the result for an arbitrary merely consistent c.e. theory without a matching
source.

**Halting-probability pointer only.** For a universal prefix-free machine `U`,
`Omega_U=sum_{U(p) halts}2^(-|p|)` converges by prefix-freeness/Kraft's
inequality and is the measure of the halting domain under the fair-coin
product measure. Source: Chaitin, “A Theory of Program Size Formally
Identical to Information Theory,” *Journal of the ACM* 22(3) (1975),
329--340, DOI
[`10.1145/321892.321894`](https://doi.org/10.1145/321892.321894);
Li--Vitanyi, Chapter 3. `D-P5-006` asks only for this pointer. Do not define
`Omega` for an arbitrary plain machine and call it a probability, and do not
expand into a general algorithmic-randomness chapter.

### Hilbert's tenth problem and MRDP (`N-a-021`)

**Definition.** A set `A subseteq N^k` is Diophantine iff there is a polynomial
`p` with integer coefficients such that

`x in A <=> (exists y_1,...,y_m in N) p(x,y_1,...,y_m)=0`.

State separately how natural-number solutions are converted to integer
solutions if the decision problem is posed over `Z`. Source: Davis,
“Hilbert's Tenth Problem is Unsolvable,” Definition 8.1, p. 264 of the
article PDF
([author-hosted scan](https://math.uchicago.edu/~shmuel/lg-readings/martin%20davis%2C%20hilbert%2010.pdf));
`Davis1973`, pp. 233--269.

**Externally verified MRDP theorem.** A subset of `N^k` is Diophantine iff it
is computably enumerable. Davis states this as Theorem 8.1. The easy direction
enumerates tuples and tests polynomial equality; the difficult direction is
the Davis--Putnam--Robinson--Matiyasevich theorem. Sources:
Davis--Putnam--Robinson, “The Decision Problem for Exponential Diophantine
Equations,” *Annals of Mathematics* 74(3) (1961), 425--436
(`DavisPutnamRobinson1961`, DOI
[`10.2307/1970289`](https://doi.org/10.2307/1970289)); Matiyasevich,
“Enumerable Sets are Diophantine,” *Doklady Akademii Nauk SSSR* 191 (1970),
279--282, English translation *Soviet Mathematics Doklady* 11 (1970),
354--358 (`Matiyasevich1970`); `Davis1973`, §8.

**Derived negative solution.** Choose a fixed c.e. nondecidable set `K`.
MRDP supplies a polynomial family whose parameter fiber has a solution iff
the parameter lies in `K`. An algorithm deciding solvability for arbitrary
integer-coefficient polynomials would decide `K`, contradiction. This
reduction is derived from MRDP plus the source-verified nondecidability of `K`
at v1.1 8084--8112.

**Proof-survey spine, not proof.** Davis--Putnam--Robinson establish that c.e.
sets have exponential-Diophantine representations. Julia Robinson isolates a
growth condition sufficient to make exponentiation Diophantine.
Matiyasevich's Fibonacci-growth argument supplies that condition. Davis's
1973 exposition develops Pell equations and the required recurrence/growth
lemmas before stating MRDP. Sources: `DavisPutnamRobinson1961`; the historical
and Pell-equation development in `Davis1973`, §§5--8; `Matiyasevich1970`.
The body may call this a “proof survey with Pell-equation core,” but must not
claim that the displayed Pell lemmas constitute the full MRDP proof or that
Matiyasevich's short original paper is literally a Pell-equation proof.

### Undecidable word problems (`N-a-022`)

**Exact decision problem.** For one fixed finite presentation
`<X | R>` of a semigroup (or group), the instance is a pair of words over the
finite generator alphabet and the yes predicate is equality of the represented
elements. This fixed-presentation theorem is stronger than the uniform problem
whose input also contains a presentation, and the table must say which form it
uses.

**Externally verified semigroup theorem.** There exists a finitely presented
semigroup with undecidable word problem. Source: Post, “Recursive
Unsolvability of a Problem of Thue,” *Journal of Symbolic Logic* 12(1)
(1947), 1--11, DOI
[`10.2307/2267170`](https://doi.org/10.2307/2267170). Markov obtained an
independent 1947 result, but no new `Markov1947` record should be added until
the original Russian/translation metadata used by the bibliography is checked
directly.

**Externally verified group theorem.** There exists a finitely presented
group with undecidable word problem. Sources: P. S. Novikov, *On the
Algorithmic Unsolvability of the Word Problem in Group Theory*, Trudy
Matematicheskogo Instituta imeni V. A. Steklova 44 (1955), 3--143
([MathNet record](https://www.mathnet.ru/eng/tm1180)); Boone, “The Word
Problem,” *Proceedings of the National Academy of Sciences* 44(10) (1958),
1061--1065, DOI
[`10.1073/pnas.44.10.1061`](https://doi.org/10.1073/pnas.44.10.1061), and
the full article “The Word Problem,” *Annals of Mathematics* 70(2) (1959),
207--265, DOI
[`10.2307/1970103`](https://doi.org/10.2307/1970103).

`N-a-022` assigns `T` to the semigroup item and `S` to the group item. A body
reduction from the live Turing-machine coding can support a local sketch only
if every encoding and equivalence step is actually present; the cited
existence result alone does not license `proved=`.

### Busy Beaver (`N-a-023`)

Fix first an exact finite-state, two-symbol Turing-machine convention, blank
input, the halting states counted or excluded, and what counts as a step.
Among the finitely many halting machines with exactly `n` nonhalting states,
define `S(n)` as the maximum number of steps before halting and `Sigma(n)` as
the maximum number of marked cells (or printed `1`s, if that is the fixed
convention) on halt. Numerical values change when this model changes.

**Externally verified theorem.** Rado introduced these maximum functions and
proved them noncomputable. Source: Tibor Rado, “On Non-Computable Functions,”
*Bell System Technical Journal* 41(3) (May 1962), 877--884, DOI
[`10.1002/j.1538-7305.1962.tb00480.x`](https://doi.org/10.1002/j.1538-7305.1962.tb00480.x).

**Derived reduction.** If `S(n)` were computable, simulate any `n`-state
machine for `S(n)` steps; it halts on blank input iff it has halted by then.
This would decide the corresponding blank-input halting problem. Thus `S` is
not computable. The same style of reduction for `Sigma` needs a stated link
between output maximum and halting, or a citation to Rado; do not silently use
the `S` proof for both functions.

The live key `Rado1964` is **not** this source: it is Richard Rado,
“Universal Graphs and Universal Functions,” *Acta Arithmetica* 9 (1964),
331--340. Use a new key such as `Rado1962BusyBeaver`.

### Computable-structure pointer (`N-a-024`)

For a computable signature and a countable structure with domain `N`, a
computable presentation has uniformly computable basic functions and
relations (equivalently, a computable atomic diagram under the stated
relational/signature convention). An index of a presentation is a program
index for this coded diagram relative to one fixed enumeration; an index set
of a class of structures is meaningful only after that coding and the
isomorphism-closure convention are stated. Source: C. J. Ash and J. Knight,
*Computable Structures and the Hyperarithmetical Hierarchy*, Studies in Logic
and the Foundations of Mathematics 144, Elsevier, 2000, Chapters 1--3
([publisher record](https://shop.elsevier.com/books/computable-structures-and-the-hyperarithmetical-hierarchy/ash/978-0-444-50072-4)).

This is a `P`/could row. Supply an `\hbstub` or short reading pointer and a
backlink to model theory if appropriate. Do not claim that every countable
structure has a computable copy. `D-P4-011` is P3-owned and remains separately
open unless the P3 artifact itself meets its register condition; a P4 pointer
cannot mark it done by cross-reference alone.

## Research package 4.6: computational complexity (`D-P5-007`, `N-a-064`)

### Shared conventions and exact hypotheses

Fix languages `L subseteq {0,1}^*`, a standard deterministic/nondeterministic
multitape Turing-machine model, input length `n=|x|`, and polynomial-time
many-one reductions unless a row explicitly states another reduction. A class
completeness claim consists of both membership and hardness under that fixed
reduction. These conventions are necessary because neither “complete” nor a
time/space bound is meaningful without an encoding and machine convention.
Source: Arora and Barak, *Computational Complexity: A Modern Approach*,
Chapters 1--5 (`AroraBarak2009`; author
[PDF](https://theory.cs.princeton.edu/complexity/book.pdf)).

Use the following class definitions:

- `P=union_{k>=1} DTIME(n^k)` and
  `NP=union_{k>=1} NTIME(n^k)`; `coNP={complement(L):L in NP}`. Source:
  `AroraBarak2009`, Chapters 1--2.
- `Sigma^p_0=Pi^p_0=P`,
  `Sigma^p_{k+1}=NP^{Sigma^p_k}`,
  `Pi^p_{k+1}=co(Sigma^p_{k+1})`, and
  `PH=union_k Sigma^p_k`. Equivalently, use bounded alternating polynomial
  quantifiers only after proving or citing the equivalence. Source:
  `Stockmeyer1976`; `AroraBarak2009`, §5.2.
- `PSPACE=union_{k>=1} SPACE(n^k)` and
  `EXPTIME=union_{k>=1} DTIME(2^{n^k})`; if `EXPSPACE` is displayed, define it
  analogously as `union_k SPACE(2^{n^k})`. Source: `AroraBarak2009`, §§3--4.

**Externally verified deterministic time hierarchy.** If `f` and `g` are
time-constructible and `f(n) log f(n)=o(g(n))`, then
`DTIME(f(n)) proper-subset DTIME(g(n))`. Source: Arora--Barak, Theorem 3.1,
author PDF p. 81; Hartmanis and Stearns, “On the Computational Complexity of
Algorithms,” *Transactions of the AMS* 117 (1965), 285--306
(`HartmanisStearns1965`, DOI
[`10.1090/S0002-9947-1965-0170805-7`](https://doi.org/10.1090/S0002-9947-1965-0170805-7)).
Do not omit constructibility or the simulation-overhead gap.

**Externally verified deterministic space hierarchy.** If `f` and `g` are
space-constructible and `f(n)=o(g(n))`, then
`SPACE(f(n)) proper-subset SPACE(g(n))`. Source: Arora--Barak, Theorem 3.2,
author PDF p. 81; Stearns, Hartmanis, and Lewis, “Hierarchies of Memory
Limited Computations,” *Proceedings of the Sixth Annual Symposium on
Switching Circuit Theory and Logical Design* (1965), 179--190, DOI
[`10.1109/FOCS.1965.11`](https://doi.org/10.1109/FOCS.1965.11).

**Externally verified Savitch theorem.** If `S(n)>=log n` is
space-constructible, then
`NSPACE(S(n)) subseteq SPACE(S(n)^2)`. Hence `NPSPACE=PSPACE`. Source:
Savitch, “Relationships between Nondeterministic and Deterministic Tape
Complexities,” *Journal of Computer and System Sciences* 4(2) (1970),
177--192, DOI
[`10.1016/S0022-0000(70)80006-X`](https://doi.org/10.1016/S0022-0000(70)80006-X);
Arora--Barak, Theorem 4.12, author PDF p. 97. The lower bound on `S` and
constructibility must remain in the general theorem even though the
polynomial-space corollary suppresses them.

### Verified class ladder (`A-050`)

| relation | classification | evidence |
|---|---|---|
| `P subseteq NP` | inclusion; equality open | definitions; `AroraBarak2009` Ch. 2 |
| `NP` and `coNP` both lie in `PH` | inclusions; `NP=coNP` open | `Sigma^p_1=NP`, `Pi^p_1=coNP`; `Stockmeyer1976` |
| `NP subseteq PH subseteq PSPACE` | inclusions; adjacent strictness open | alternating-quantifier evaluation in polynomial space; `AroraBarak2009` Ch. 5 |
| `PSPACE=NPSPACE` | equality | Savitch 1970 |
| `PSPACE subseteq EXPTIME` | inclusion; strictness open | configuration enumeration; `AroraBarak2009` Ch. 4 |
| `P proper-subset EXPTIME` | known strict | deterministic time hierarchy |
| `PSPACE proper-subset EXPSPACE` | known strict | deterministic space hierarchy |

The single visual chain
`P subseteq NP subseteq PH subseteq PSPACE subseteq EXPTIME subseteq EXPSPACE`
is correct only as an inclusion chain. It is false to mark every adjacent edge
strict. In particular, `P` versus `NP`, `NP` versus `coNP`, collapse of `PH`,
`PH` versus `PSPACE`, and `PSPACE` versus `EXPTIME` remain open. The two
unconditional separations above do not settle those adjacent questions.

### Logic-relevant completeness catalog

| problem | encoded yes instances | exact classification | source and status |
|---|---|---|---|
| `SAT` | satisfiable encoded CNF Boolean formulas | NP-complete under polynomial-time many-one reductions | Cook 1971; `AroraBarak2009`, Theorem 2.10 |
| `3SAT` | satisfiable encoded 3CNF formulas | NP-complete under the same reductions | Cook--Levin conversion; `AroraBarak2009`, Theorem 2.10; Karp 1972 |
| `TAUT` | Boolean formulas true under every assignment | coNP-complete | **derived** from SAT completeness by complement/negation after fixing the formula encoding; `AroraBarak2009`, p. 95 |
| `Sigma_k-SAT` | true prenex QBF with `k` alternating blocks beginning existentially | `Sigma^p_k`-complete for fixed `k>=1` | `Stockmeyer1976`; `AroraBarak2009`, §5.2.2 |
| `Pi_k-SAT` | dual prefix beginning universally | `Pi^p_k`-complete | `Stockmeyer1976`; `AroraBarak2009`, §5.2.2 |
| `TQBF` | true closed quantified Boolean formulas with unbounded alternation | PSPACE-complete | Stockmeyer--Meyer 1973; `AroraBarak2009`, Theorem 4.11 |
| FOL validity | codes of valid first-order sentences under the fixed v1.1 coding | c.e. and undecidable | source 8256--8279; `Church1936`, `Turing1937` |

**Cook--Levin exact ceiling.** Cook proves polynomial-time theorem-proving
procedures yield a complete satisfiability problem; the handbook can use the
modern statement that SAT is NP-complete under polynomial-time many-one
reductions. Source: Cook, “The Complexity of Theorem-Proving Procedures,”
STOC 1971, 151--158 (`Cook1971`, DOI
[`10.1145/800157.805047`](https://doi.org/10.1145/800157.805047));
Arora--Barak, Theorem 2.10, pp. 60--61. Membership and hardness must both be
stated.

**TQBF exact ceiling.** A quantified Boolean formula is closed, quantifies
over `{0,1}`, and has an explicitly encoded propositional matrix. `TQBF` is
the language of true such formulas and is PSPACE-complete under
polynomial-time many-one reductions. Source: Stockmeyer and Meyer, “Word
Problems Requiring Exponential Time,” STOC 1973, 1--9
(`StockmeyerMeyer1973`, DOI
[`10.1145/800125.804029`](https://doi.org/10.1145/800125.804029));
Arora--Barak, Theorem 4.11, pp. 95--97. Do not call unrestricted QBF
“NP-complete,” and do not call a fixed-alternation fragment PSPACE-complete.

`A-127` must be an inclusion diagram rather than a literal Hasse diagram of
known cover relations. Suggested legend: solid arrow = proved inclusion;
heavy barred annotation = proved strict separation; dashed connector/question
label = equality unresolved. Place `coNP` as a branch meeting `PH`, not between
`NP` and `PH` in a claimed linear order. Captions should cite the hierarchy
theorems and say that unmarked adjacent strictness is not known.

## `A-052`: descriptive-complexity pointer

Fix a finite relational vocabulary, finite structures, isomorphism-invariant
properties, and a reasonable encoding. Say explicitly when the finite
structures carry a built-in total order.

- **Externally verified Fagin theorem.** A class of finite structures closed
  under isomorphism is definable by an existential second-order sentence iff
  its encoded membership problem is in NP. A built-in order is not needed for
  this theorem. Source: Fagin, “Generalized First-Order Spectra and
  Polynomial-Time Recognizable Sets,” *SIAM--AMS Proceedings* 7 (1974),
  43--73, especially §§1 and 4 (`Fagin1974`; author
  [PDF](https://kenclarkson.org/RonFaginPaper/genspec.pdf)).
- **Externally verified Immerman--Vardi theorem.** Over finite ordered
  structures, first-order logic extended by a least fixed-point operator
  captures polynomial time. The total-order hypothesis is essential to this
  formulation. Source: Immerman, “Relational Queries Computable in Polynomial
  Time,” *Information and Control* 68(1--3) (1986), 86--104
  (`Immerman1986`, DOI
  [`10.1016/S0019-9958(86)80029-8`](https://doi.org/10.1016/S0019-9958(86)80029-8));
  Vardi, “The Complexity of Relational Query Languages,” STOC 1982, 137--146
  (`Vardi1982`, DOI
  [`10.1145/800070.802186`](https://doi.org/10.1145/800070.802186)).
- **Pointer-only FO row.** Plain first-order logic is the baseline formalism.
  Do not print `FO=AC0` without specifying ordered finite structures,
  built-in numerical predicates such as `<`/`BIT`, and the uniformity notion.
  `A-052` does not require that stronger correspondence; `Immerman1999` is the
  systematic reading source.

Recommended table:

| logic | structure convention | captured class | source |
|---|---|---|---|
| FO | finite relational structures; baseline only | no unqualified machine-class equality in this table | `Immerman1999` pointer |
| ESO | finite relational structures, no order required | NP | `Fagin1974` |
| FO(LFP) | finite relational structures with a built-in total order | P | `Immerman1986`, `Vardi1982` |

Do not conflate “captures a complexity class on finite structures” with
ordinary first-order definability over arbitrary structures, and do not use
the analytical-hierarchy notation `Sigma^1_1` for ESO here without warning
that descriptive complexity is a finite-structure, machine-complexity
correspondence.

## `A-046`: exact undecidability catalog

Every row must name the encoded instance and yes predicate, not merely a topic.

| problem | instance / yes predicate | verified result and source | formulation warning |
|---|---|---|---|
| self-application halting/domain | program index `e`; yes iff `phi_e(e)` has valid-output convergence | c.e., undecidable; v1.1 8084--8112, `Turing1937` | retain the local convergence convention |
| Rice index problem | index `e`; yes iff computed unary partial function has a fixed nontrivial extensional property | undecidable; v1.1 8190--8231, `Rice1953` | syntactic program properties are outside Rice |
| Hilbert's tenth | integer-coefficient polynomial; yes iff it has a solution in the stated integer/natural domain | undecidable; MRDP sources above | state domain and encoding |
| semigroup word problem | two words for one fixed finite semigroup presentation; yes iff equal | undecidable for some fixed presentation; `Post1947` | do not substitute only the uniform-presentation problem |
| group word problem | two words for one fixed finite group presentation; yes iff equal | undecidable for some fixed presentation; `Novikov1955`, `Boone1958/1959` | keep group and semigroup results separate |
| domino/Wang tiling | finite set of unit-square tile types with colored edges; yes iff copies tile the entire integer plane with matching adjacent colors | undecidable; Berger 1966 | not the finite-region tiling problem |
| FOL validity | code of a first-order sentence; yes iff valid in all structures under the fixed signature convention | c.e. and undecidable; v1.1 8256--8279, `Church1936`, `Turing1937` | restricted signatures may behave differently |

**Externally verified tiling source.** Berger's domino problem takes a finite
set of square tile types, unlimited copies, translation without rotation under
the fixed convention, and asks whether the whole plane can be tiled subject to
the edge-adjacency rules. Berger proves this problem undecidable by a reduction
from a Turing-machine halting problem. Source: Robert Berger, *The
Undecidability of the Domino Problem*, Memoirs of the American Mathematical
Society 66 (1966), 72 pp.
([AMS record](https://bookstore.ams.org/view?ProductCode=MEMO%2F1%2F66));
DOI [`10.1090/memo/0066`](https://doi.org/10.1090/memo/0066). Hao Wang's
originating tile formalism is in “Proving Theorems by Pattern Recognition II,”
*Bell System Technical Journal* 40(1) (1961), 1--41, DOI
[`10.1002/j.1538-7305.1961.tb03975.x`](https://doi.org/10.1002/j.1538-7305.1961.tb03975.x).
Do not cite a modern finite-board tiling result as evidence for this row.

## Apparatus construction specifications

### `A-047/A-124`: arithmetical hierarchy

Use exactly the v1.1 source convention at 8309--8429 and the proved
closure/prefix equivalence at 8439--8708. The table should include normal form,
closure behavior, a complete set, and jump characterization for each displayed
level. `K`/its complement and `TOT` have cited completeness at 8830--8849;
Post's theorem is cited at 9023--9048. `R-006` forbids treating a displayed
prefix as automatically identical to the closure-defined class without the
proved bridge. The figure may mark the strictness stated at 8851--8868, but
must cite that theorem and must not infer completeness from a mere syntactic
upper bound (warning 8870--8875).

### `A-125`: analytical hierarchy

Use the exact rows in the analytical package above. The minimum useful figure
shows the arithmetical sets inside `Delta^1_1=HYP`, the intersection of the
`Sigma^1_1` and `Pi^1_1` branches, and their continuing alternating levels.
Label `IF` and `WF` only after the recursive-relation coding is stated. Avoid
an unlabeled vertical “strictness” axis unless each strictness claim is cited.

### `A-126`: degrees and jump

Use the fact table in package 4.4. Draw separate annotations for
Kleene--Post's (not necessarily c.e.) incomparable degrees below `0'` and the
Friedberg--Muchnik incomparable c.e. degrees. A join node is justified only
for the displayed pair; do not make the entire degree structure look like a
lattice. Every jump arrow must have the form `x -> x'` and may not terminate at
`0'` unless that equality was actually established.

### `A-127`: complexity classes

Pair the diagram with `A-050`. The graphic grammar itself should encode the
epistemic status: ordinary solid inclusion, explicitly marked proper
inclusion, and dashed/open equality question. The only global separations this
ledger licenses for the requested scale are `P proper-subset EXPTIME` and
`PSPACE proper-subset EXPSPACE`; other separations require their own cited
theorem. “Hasse-style” is a visual instruction, not a mathematical assertion
that an edge is a cover.

## Bibliography audit and intake ledger (`A-182`, `A-186`)

### Verified live keys: do not duplicate

The following keys already occur in `handbook/bib/handbook.bib`; their live
metadata was checked against the cited DOI/publisher record during this visit:

| key | use in P4 |
|---|---|
| `Church1936` | undecidability of FOL validity; historical thesis context |
| `Turing1937` | Turing machines, universal computation, Entscheidungsproblem |
| `Kleene1936` | general/partial recursive functions |
| `Kleene1952` | normal form, `s-m-n`, recursive-function theory |
| `KleenePost1954` | degree upper semilattice and incomparable degrees |
| `Rogers1967` | acceptable numberings, c.e. sets, priority, Rice--Shapiro |
| `Soare2016` | modern systematic computability/degree reference |
| `Post1944` | Post's problem and simple sets |
| `Friedberg1957` | c.e. incomparable degrees |
| `Muchnik1956` | independent c.e. incomparable-degree theorem |
| `DavisPutnamRobinson1961` | exponential-Diophantine stage of MRDP |
| `Matiyasevich1970` | c.e. sets are Diophantine |
| `Davis1973` | H10 survey, Pell development, MRDP statement |
| `Moschovakis2009` | background descriptive-set-theory reading, not the principal lightface-HYP locator |
| `HartmanisStearns1965` | deterministic time hierarchy |
| `Cook1971` | SAT/NP completeness |
| `Karp1972` | polynomial reducibility and NP-complete catalog |
| `Stockmeyer1976` | polynomial hierarchy |
| `StockmeyerMeyer1973` | TQBF/PSPACE historical source |
| `Papadimitriou1994` | systematic complexity reference |
| `AroraBarak2009` | exact modern hierarchy/completeness formulations |
| `Fagin1974` | ESO captures NP |
| `Vardi1982` | fixed-point/query-language capture result |
| `Immerman1986` | FO(LFP) captures P on ordered finite structures |
| `Immerman1999` | descriptive-complexity further reading |

`Rado1964` is live but unrelated to Busy Beaver and must not be cited for
`N-a-023`.

### Verified records needed by the P4 intake

Keys below are proposed mnemonic keys. A wave finalizer may rename one only if
all P4 citations are updated consistently. Metadata, not key spelling, is the
source-verified fact.

| proposed key | verified bibliographic record | primary locator / use |
|---|---|---|
| `Turing1937Lambda` | A. M. Turing, “Computability and lambda-definability,” *Journal of Symbolic Logic* 2(4) (1937), 153--163, DOI `10.2307/2268280` | [Cambridge](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/computability-and-definability/FE8B4FC84276D7BACB8433BD578C6BFD); formal-model equivalence |
| `Soare1996ComputabilityRecursion` | Robert I. Soare, “Computability and Recursion,” *Bulletin of Symbolic Logic* 2(3) (1996), 284--321, DOI `10.2307/420992` | [Cambridge](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/abs/computability-and-recursion/21DB3D692FCB1FFD2BE365C0B4A04FD6); thesis calibration |
| `ShepherdsonSturgis1963` | J. C. Shepherdson and H. E. Sturgis, “Computability of Recursive Functions,” *Journal of the ACM* 10(2) (April 1963), 217--255, DOI `10.1145/321160.321170` | [primary-paper PDF](https://www.cs.cmu.edu/~15455/resources/ShepherdsonSturgis1963.pdf); exact URM |
| `Kleene1955Hierarchy` | Stephen C. Kleene, “Hierarchies of Number-Theoretic Predicates,” *Bulletin of the American Mathematical Society* 61(3) (1955), 193--213, DOI `10.1090/S0002-9904-1955-09896-3` | analytical/hyperarithmetical hierarchy |
| `Moschovakis2016Hyperarithmetical` | Yiannis N. Moschovakis, “Hyperarithmetical Sets,” in E. G. Omodeo and A. Policriti (eds.), *Martin Davis on Computability, Computational Logic, and Mathematical Foundations*, Outstanding Contributions to Logic 10, Springer, 2016, 107--149, DOI `10.1007/978-3-319-41842-1_5` | [author PDF](https://www.math.ucla.edu/~ynm/papers/hyp.pdf); exact `HYP=Delta^1_1` locators |
| `Myhill1955` | John Myhill, “Creative Sets,” *Zeitschrift fuer mathematische Logik und Grundlagen der Mathematik* 1(2) (1955), 97--108, DOI `10.1002/malq.19550010205` | creative sets and isomorphism |
| `Rice1953` | H. G. Rice, “Classes of Recursively Enumerable Sets and Their Decision Problems,” *Transactions of the American Mathematical Society* 74 (1953), 358--366, DOI `10.1090/S0002-9947-1953-0053041-6` | [AMS PDF](https://www.ams.org/journals/tran/1953-074-02/S0002-9947-1953-0053041-6/S0002-9947-1953-0053041-6.pdf); index properties |
| `Johnson1977Rice` | Nancy Johnson, “Rice Theorems for `Sigma_n^{-1}` Sets,” *Canadian Journal of Mathematics* 29(4) (1977), 794--805, DOI `10.4153/CJM-1977-082-3` | [Cambridge](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/rice-theorems-for-n-1-sets/216B53B8905C6AD0360AFDB0C9E4F87A); exact Rice--Shapiro restatement |
| `Kolmogorov1965` | A. N. Kolmogorov, “Three approaches to the definition of the concept ‘quantity of information’,” *Problemy Peredachi Informatsii* 1(1) (1965), 3--11 | [MathNet](https://www.mathnet.ru/eng/ppi68); algorithmic information |
| `Chaitin1974` | Gregory J. Chaitin, “Information-Theoretic Limitations of Formal Systems,” *Journal of the ACM* 21(3) (1974), 403--424, DOI `10.1145/321832.321839` | incompleteness |
| `Chaitin1975` | Gregory J. Chaitin, “A Theory of Program Size Formally Identical to Information Theory,” *Journal of the ACM* 22(3) (1975), 329--340, DOI `10.1145/321892.321894` | prefix complexity/halting-probability pointer |
| `LiVitanyi2008` | Ming Li and Paul Vitanyi, *An Introduction to Kolmogorov Complexity and Its Applications*, 3rd ed., Texts in Computer Science, Springer New York, 2008, xxiii+790 pp., DOI `10.1007/978-0-387-49820-1` | [Springer](https://link.springer.com/book/10.1007/978-0-387-49820-1); exact modern formulations |
| `Post1947` | Emil L. Post, “Recursive Unsolvability of a Problem of Thue,” *Journal of Symbolic Logic* 12(1) (1947), 1--11, DOI `10.2307/2267170` | semigroup/Thue word problem |
| `Novikov1955` | P. S. Novikov, *On the Algorithmic Unsolvability of the Word Problem in Group Theory*, Trudy Matematicheskogo Instituta imeni V. A. Steklova 44 (1955), 3--143, in Russian | [MathNet](https://www.mathnet.ru/eng/tm1180); group word problem |
| `Boone1958` | William W. Boone, “The Word Problem,” *Proceedings of the National Academy of Sciences* 44(10) (1958), 1061--1065, DOI `10.1073/pnas.44.10.1061` | short announcement matching register year |
| `Boone1959` | William W. Boone, “The Word Problem,” *Annals of Mathematics* 70(2) (1959), 207--265, DOI `10.2307/1970103` | full group result |
| `Rado1962BusyBeaver` | Tibor Rado, “On Non-Computable Functions,” *Bell System Technical Journal* 41(3) (May 1962), 877--884, DOI `10.1002/j.1538-7305.1962.tb00480.x` | [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1962.tb00480.x); Busy Beaver |
| `AshKnight2000` | C. J. Ash and J. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Studies in Logic and the Foundations of Mathematics 144, Elsevier, 2000, ISBN-10 `0-444-50072-3`, ISBN-13 `978-0-444-50072-4` | [Elsevier](https://shop.elsevier.com/books/computable-structures-and-the-hyperarithmetical-hierarchy/ash/978-0-444-50072-4); pointer |
| `StearnsHartmanisLewis1965` | R. E. Stearns, J. Hartmanis, and P. M. Lewis II, “Hierarchies of Memory Limited Computations,” *Proceedings of the Sixth Annual Symposium on Switching Circuit Theory and Logical Design* (1965), 179--190, DOI `10.1109/FOCS.1965.11` | space hierarchy |
| `Savitch1970` | Walter J. Savitch, “Relationships between Nondeterministic and Deterministic Tape Complexities,” *Journal of Computer and System Sciences* 4(2) (April 1970), 177--192, DOI `10.1016/S0022-0000(70)80006-X` | [Elsevier](https://www.sciencedirect.com/science/article/pii/S002200007080006X); Savitch theorem |
| `Berger1966` | Robert Berger, *The Undecidability of the Domino Problem*, Memoirs of the American Mathematical Society 66, 1966, 72 pp., DOI `10.1090/memo/0066` | [AMS](https://bookstore.ams.org/view?ProductCode=MEMO%2F1%2F66); tiling |
| `Wang1961PatternII` | Hao Wang, “Proving Theorems by Pattern Recognition II,” *Bell System Technical Journal* 40(1) (1961), 1--41, DOI `10.1002/j.1538-7305.1961.tb03975.x` | Wang-tile formalism |

`Markov1947` is intentionally not supplied as a verified intake record here:
the theorem is independently covered by the verified Post primary, and the
exact original/translation metadata was not established from a primary
publisher record in this visit. Do not invent that entry merely because the
register prose says “Post--Markov.”

### Further-reading split

For `A-186`, historical primaries are Turing 1937 lambda, Kleene--Post 1954,
Post 1944, Friedberg 1957, Myhill 1955, Kolmogorov 1965, Chaitin 1974/1975,
DPR 1961, Matiyasevich 1970, Post 1947, Novikov 1955, Boone 1959,
Rado 1962, Hartmanis--Stearns 1965, Cook 1971, Stockmeyer--Meyer 1973,
Fagin 1974, and Immerman 1986. Systematic modern reading is `Rogers1967`,
`Soare2016`, `LiVitanyi2008`, `AshKnight2000`, `Papadimitriou1994`,
`AroraBarak2009`, and `Immerman1999`. Label the two lists; do not make a
modern textbook look like the historical source of a theorem.

## Unsupported or unsafe formulations

The following wordings are not licensed by this ledger:

1. **“The Church--Turing thesis is proved by model equivalence.”** Formal
   equivalences compare precise models; the thesis connects those models to an
   informal notion. Use `D-P5-002`'s discussion ceiling.
2. **“All register machines are equivalent to Turing machines.”** `A-045` has
   evidence for the exact Shepherdson--Sturgis URM defined above. Another
   instruction set needs its own definition and simulation source.
3. **“Normal form follows from the local universal machine.”** Kleene normal
   form requires a primitive-recursive computation predicate and output map;
   v1.1's universal machine is only sketched.
4. **“The jump is obviously well-defined on degrees.”** The claim uses jump
   monotonicity and the repaired convergence convention; v1.1's local bridge
   is a proof sketch (`R-004`).
5. **“Kleene--Post solved Post's problem.”** Kleene--Post constructed
   incomparable degrees below `0'`; Friedberg--Muchnik constructed
   incomparable *c.e.* degrees and solved Post's problem.
6. **“The finite-injury theorem is proved in full.”** The requested P4
   artifact is a table/method plus a sketched annex unless a complete proof is
   independently written and verified. “In full” in `N-a-017` does not itself
   assign proof status.
7. **“A simple c.e. set has intermediate degree.”** Simplicity alone does not
   imply Turing incompleteness.
8. **“Rice--Shapiro characterizes every semantic program property.”** The
   stated theorem uses an acceptable c.e.-set numbering and c.e. extensional
   index sets with effective finite witnesses.
9. **“Kolmogorov complexity is machine independent.”** It is invariant only
   up to a machine-dependent additive constant. Plain `C`, prefix `K`, and
   resource-bounded complexity are distinct notions.
10. **“Omega is the halting probability of any universal program notation.”**
    The displayed series needs a universal prefix-free machine and its exact
    domain convention.
11. **“Consistency alone gives the stated Chaitin bound.”** Use the exact
    source hypothesis; the safe formulation here assumes soundness for the
    complexity lower-bound sentences.
12. **“`Delta^1_1=HYP` is a statement about the boldface projective
    hierarchy.”** It is the lightface effective theorem on subsets of `N`
    under the fixed coding.
13. **“Kleene's `O` canonically enumerates the countable ordinals.”** Notations
    are coding-dependent and nonunique; only a sketch is licensed.
14. **“The Pell-equation lemmas are the full proof of MRDP.”** They are part of
    Davis's proof survey; the full hard direction is out of scope.
15. **“The word problem is undecidable” without a presentation/input
    convention.** Distinguish a fixed finitely presented semigroup/group from
    the uniform presentation problem.
16. **“Busy Beaver has canonical small values.”** Values depend on the state,
    symbol, blank, step, and halting conventions. `Rado1964` is the wrong
    author/paper.
17. **“Every countable structure has a computable presentation.”** The pointer
    defines computable copies and their indices; it supplies no such existence
    theorem.
18. **“Every adjacent class-ladder inclusion is strict.”** Only cited
    hierarchy separations may be marked strict. `A-127` is not a literal Hasse
    diagram of established cover relations.
19. **“FO captures AC0” without vocabulary/order/uniformity data.** `A-052`
    needs only the baseline FO pointer, Fagin's ESO/NP theorem, and the ordered
    FO(LFP)/P theorem.
20. **“FOL validity is NP-complete.”** The unrestricted classical validity set
    in v1.1 is c.e. and undecidable; finite propositional SAT and QBF occupy the
    finite complexity classes in `A-050`.
21. **“The domino theorem is about tiling a supplied finite board.”** Berger's
    input is a finite tile set and the question is tiling the whole plane.

## Complete row-to-evidence map

### Depth/new-content coverage

| live row | evidence package in this note | principal source keys | required body/annex outcome |
|---|---|---|---|
| `D-P5-001` | 4.1 definitions/equivalence | `Kleene1936`, `Kleene1952`, `Turing1937Lambda`, `ShepherdsonSturgis1963` | entry with definitions, normal form, exact TM/partial-recursive theorem; preserve `R-005` |
| `D-P5-002` | 4.1 thesis calibration | `Turing1937Lambda`, `Soare1996ComputabilityRecursion` | statement/discussion; no theorem/proof label |
| `D-P5-003` | 4.4 degree definitions | `KleenePost1954`, `Soare2016` plus v1.1 8931--9078 | entry defining degree/order/join/jump and status of well-definedness |
| `D-P5-004` | 4.4 finite injury | `Post1944`, `Friedberg1957`, `Muchnik1956`, `Rogers1967`, `Soare2016` | theorem statement + `hbmethod` + `sketched=` annex with omissions |
| `D-P5-005` | 4.4 c.e.-set structure | `Post1944`, `Myhill1955`, `Rogers1967`, `Johnson1977Rice` | statement/table for simple, creative, Myhill, Rice--Shapiro |
| `D-P5-006` | 4.5 Kolmogorov | `Kolmogorov1965`, `Chaitin1974`, `Chaitin1975`, `LiVitanyi2008` | statement/survey; Omega pointer only |
| `D-P5-007` | 4.6 complexity | `HartmanisStearns1965`, `StearnsHartmanisLewis1965`, `Savitch1970`, `Cook1971`, `Stockmeyer1976`, `StockmeyerMeyer1973`, `AroraBarak2009` | class definitions plus `A-050/A-127` and status-safe results |
| `D-P9-002` | 4.5 analytical hierarchy | `Kleene1955Hierarchy`, `Moschovakis2016Hyperarithmetical` | `A-048/A-125`, basic results, lightface warning |
| `N-a-016` | 4.4 degree structure/Kleene--Post | `KleenePost1954`, `Soare2016` | full entry; incomparable-below-`0'` theorem cited |
| `N-a-017` | 4.4 finite-injury schema | `Post1944`, `Friedberg1957`, `Muchnik1956` | treatment table/method and sketch, not automatic full proof |
| `N-a-018` | 4.4 simple/creative/reducibilities/Myhill | `Post1944`, `Myhill1955`, `Rogers1967` | definitions and comparison table; add Rice--Shapiro for depth row |
| `N-a-019` | 4.5 analytical/HYP/`O` | `Kleene1955Hierarchy`, `Moschovakis2016Hyperarithmetical` | statement/survey with `Delta^1_1=HYP`; `O` sketch; no alpha-recursion |
| `N-a-020` | 4.5 Kolmogorov | `Kolmogorov1965`, `Chaitin1974`, `LiVitanyi2008` | table treatment with exact machine/soundness hypotheses |
| `N-a-021` | 4.5 MRDP | `DavisPutnamRobinson1961`, `Matiyasevich1970`, `Davis1973` | theorem statement and proof survey; no full-proof claim |
| `N-a-022` | 4.5 word problems | `Post1947`, `Novikov1955`, `Boone1958`, `Boone1959` | semigroup T row and group S row with fixed presentations |
| `N-a-023` | 4.5 Busy Beaver | `Rado1962BusyBeaver` | exact model definition and cited/derived noncomputability |
| `N-a-024` | 4.5 computable structures | `AshKnight2000` | pointer/stub only; P3 cross-row stays separate |
| `N-a-063` | 4.1 normal form/`s-m-n`/equivalence | `Kleene1936`, `Kleene1952`, `Turing1937Lambda`, `ShepherdsonSturgis1963` | full entry and A-045 rows; tie to local numbering |
| `N-a-064` | 4.6 ladder/hierarchies/catalog | complexity source package above | treatment table and diagram; P9/P14 per-logic claims are pointers |

### Apparatus coverage

| live row | source-backed specification in this note | completion test |
|---|---|---|
| `A-045` | 4.1 exact models and URM repertoire | no generic register machine; each equivalence edge has a source or labelled derivation |
| `A-046` | dedicated undecidability catalog | all seven instance predicates present; Berger 1966 is the tiling source |
| `A-047` | apparatus specification plus frozen source | closure/prefix bridge and complete-set/jump rows cite v1.1 statuses |
| `A-048` | 4.5 analytical table | lightface normal forms, `WF/IF`, `Delta^1_1=HYP` |
| `A-049` | 4.4 fact table | joins/jumps well-defined; KP/FM distinction visible |
| `A-050` | 4.6 ladder | definitions, inclusion status, complete examples, open problems |
| `A-052` | descriptive-complexity section | ESO/NP with no unnecessary order; FO(LFP)/P with total order |
| `A-124` | arithmetical figure specification | labels and strictness agree with `A-047`/v1.1 |
| `A-125` | analytical figure specification | visibly lightface; arithmetical subset and HYP equality |
| `A-126` | degree figure specification | schematic caption; KP and c.e. FM nodes separated |
| `A-127` | complexity figure specification | legend distinguishes inclusion, strictness, and open equality |
| `A-163` | binding inventory | every new P4 glyph audited before use |
| `A-182` | bibliography audit/intake ledger | no undefined citation keys; no `Rado1964` misuse; full metadata verified |
| `A-186` | further-reading split | primaries and systematic texts are labelled separately |
| `A-189` | evidence-policy/treatment reconciliation | every `sketched=` target has one matching annex item and named omissions |

### Defect/dependency trace

| row | downstream mapped rows/apparatus | gate |
|---|---|---|
| `R-002` | `A-047`, `A-124`, `N-a-021` reduction interface | bounded extraction and `Comp` remain coherent |
| `R-004` | `D-P5-003`, `N-a-016`, `A-049`, `A-126` | one convergence notion and no proof-status upgrade |
| `R-005` | `D-P5-001`, `N-a-063`, finite injury, Rice--Shapiro | all functionals/index sets use the adequate numbering |
| `R-006` | `A-047`, `A-124`, `D-P9-002` boundary | closure and prefix forms linked by the proved theorem |
| `R-035` | `D-P5-001`, `N-a-063` | exactly one partial-function biconditional retained |

## Implementation and adversarial verification checklist

1. Every technical definition precedes its first theorem/table use; no new
   hypothetical term is named without necessity, exact standing,
   nonredundancy, and downstream use.
2. `A-045` names the exact Shepherdson--Sturgis URM and prints or points to all
   six instruction forms. Its equivalence cells concern partial numerical
   functions, not time/space preservation.
3. The Church--Turing thesis has no theorem-status macro.
4. The degree order, join, and jump are definitions on equivalence classes,
   with representative-independence proved, sketched, or cited explicitly.
5. `A-126` never labels Kleene--Post degrees c.e.; the c.e. incomparable nodes
   cite Friedberg--Muchnik.
6. The finite-injury annex opens with `\sketchnote` and lists the eight
   omissions/obligations in package 4.4. No infinite-injury material appears.
7. Simple does not imply intermediate; creative/m-complete/isomorphic claims
   use the exact acceptable-numbering hypotheses.
8. Rice--Shapiro states a c.e. finite-witness family and treats the empty class.
9. The analytical material says lightface, fixes function/set quantifiers, and
   does not depict the boldface projective hierarchy.
10. Plain and prefix Kolmogorov complexity use different notation and machine
    conditions; every invariance constant has its dependency.
11. Chaitin's theorem states the theory's effectiveness, expressive strength,
    and soundness hypothesis; Omega uses a prefix-free universal machine.
12. MRDP separates the easy enumeration direction, hard theorem, derived H10
    reduction, and Pell-based survey. It never advertises a full proof.
13. Word-problem rows distinguish semigroup/group and fixed/uniform problems.
14. Busy Beaver fixes the machine convention and cites Tibor Rado 1962, not
    Richard Rado 1964.
15. The computable-structure row remains a pointer and does not close
    `D-P4-011` by proxy.
16. Time and space hierarchy statements retain constructibility and asymptotic
    gap hypotheses; Savitch retains `S(n)>=log n`.
17. Cook--Levin and TQBF rows state both membership and hardness under the
    selected polynomial many-one reduction.
18. `A-050/A-127` mark only `P proper-subset EXPTIME` and
    `PSPACE proper-subset EXPSPACE` as the requested unconditional global
    separations; all unresolved adjacent relations are visually distinct.
19. `A-052` retains the total-order hypothesis for FO(LFP)/P and does not add
    it as a false necessity to Fagin's ESO/NP theorem.
20. `A-046` defines the whole-plane Wang-tile problem and cites Berger 1966.
21. All proposed bibliography keys resolve through the P4 intake before
    compile; all new glyphs resolve through the P4 symbol intake.
22. The body has no `proof` environments, every result has a valid status, and
    every `proved=`/`sketched=` body target is bidirectionally paired with one
    annex item.

## External locator ledger

All links below were accessed on 2026-08-11. They are grouped by the claims
they support; the body should cite bibliography keys, not web URLs.

- Turing model equivalence: Cambridge record and opening extract,
  <https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/computability-and-definability/FE8B4FC84276D7BACB8433BD578C6BFD>.
- Shepherdson--Sturgis exact URM: primary-paper PDF, §§2--3 and §9,
  <https://www.cs.cmu.edu/~15455/resources/ShepherdsonSturgis1963.pdf>.
- Soare thesis calibration: Cambridge record,
  <https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/abs/computability-and-recursion/21DB3D692FCB1FFD2BE365C0B4A04FD6>.
- Moschovakis lightface hierarchy/HYP: author PDF, §§1A and 3A--3E,
  <https://www.math.ucla.edu/~ynm/papers/hyp.pdf>.
- Rice primary: AMS scan,
  <https://www.ams.org/journals/tran/1953-074-02/S0002-9947-1953-0053041-6/S0002-9947-1953-0053041-6.pdf>.
- Rice--Shapiro exact restatement: Cambridge/CJM record,
  <https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/rice-theorems-for-n-1-sets/216B53B8905C6AD0360AFDB0C9E4F87A>.
- Kolmogorov primary metadata: MathNet,
  <https://www.mathnet.ru/eng/ppi68>.
- Kolmogorov definitions/invariance: Grunwald--Vitanyi author PDF, §§2.2--2.3,
  <https://homepages.cwi.nl/~paulv/papers/info.pdf>.
- MRDP/Pell survey: Davis article scan, §§5--8,
  <https://math.uchicago.edu/~shmuel/lg-readings/martin%20davis%2C%20hilbert%2010.pdf>.
- Busy Beaver: Wiley primary record,
  <https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1962.tb00480.x>.
- Computable structures: Elsevier book record,
  <https://shop.elsevier.com/books/computable-structures-and-the-hyperarithmetical-hierarchy/ash/978-0-444-50072-4>.
- Complexity definitions/hierarchies/completeness: Arora--Barak author PDF,
  Theorems 2.10, 3.1, 3.2, 4.11, and 4.12,
  <https://theory.cs.princeton.edu/complexity/book.pdf>.
- Savitch primary record: Elsevier,
  <https://www.sciencedirect.com/science/article/pii/S002200007080006X>.
- Fagin primary text: author-hosted PDF, §§1 and 4,
  <https://kenclarkson.org/RonFaginPaper/genspec.pdf>.
- Immerman primary record: Elsevier,
  <https://www.sciencedirect.com/science/article/pii/S0019995886800298>.
- Berger domino problem: AMS publisher record,
  <https://bookstore.ams.org/view?ProductCode=MEMO%2F1%2F66>.
