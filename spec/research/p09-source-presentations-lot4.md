# Part IX source presentations, lot 4

**Scope.** This is the source-acquisition and reconstruction brief for
`N-c-019`--`N-c-026`, `N-c-028`, `N-x-015`, and depth rows `D-P11-006`,
`D-P11-007`, and `D-P11-008`. It treats every semicolon-delimited authority in
the audit as a separate authority. It does not admit prose to the handbook,
modify a register, or claim a proof/build/visual-review result.

**Evidence rule.** Publication identity is taken from a publisher, DOI landing
page, proceedings record, institutional repository, or author-hosted copy.
Technical claims below are tied to an accessible primary text whenever one was
acquired. A table of contents or retrospective is not treated as the theorem
text. Where the exact text was inaccessible, the gap is marked **OPEN** and no
claim is inferred from a secondary exposition. An adjacent primary source can
show what further material is needed, but cannot silently substitute for an
authority named in the audit.

**Terminology rule.** The note introduces no new handbook object merely to make
an outline sound finished. Established source terms are accompanied by their
source-side definitions and standing. Anything not yet justified is described
as an owed presentation or an open source acquisition, not named as if it were
already part of the theory.

## Corrections that must govern reconstruction

1. Dijkstra's `wp(S,R)` includes guaranteed proper termination; the 1975 paper
   is not a source for silently replacing it by weakest liberal precondition.
   The distinction is explicit in [Dijkstra, section 3.1, printed pp. 454--455](https://www.cs.utexas.edu/~EWD/ewd04xx/EWD472.PDF).
2. Cook's 1971 `P`-reducibility permits polynomially many oracle queries. The
   paper's exact theorem is therefore not literally the later many-one form of
   the Cook--Levin theorem; the two formulations need an explicit bridge. See
   [Cook, printed pp. 151--153](https://www.cs.cmu.edu/~15455/resources/Cook1971-complx-thm-proof.pdf).
3. Ladner's S5 polarity must be typed: S5 **nonprovability** (equivalently, in
   the standard semantics used there, satisfiability/nonvalidity) is
   NP-complete, so S5 provability/validity is coNP-complete. A bare “S5 is NP”
   is false or at best untyped. See [Ladner, abstract and Theorem 4.1](https://www.cs.man.ac.uk/~ezolin/ml/bib/Computational_complexity_of_provability_in_systems_of_modal_logic_%28SIAMJC_1977%29.pdf).
4. McMillan first says that the parameter is fixed at `k >= 0`, but the
   `FiniteRun` procedure, Theorem 3, and the termination argument use `k > 0`.
   A reconstruction must either impose the positive bound used by the proved
   algorithm or separately justify a zero case. See [McMillan, printed pp.
   5--7](https://mcmil.net/pubs/CAV03.pdf).
5. *Principles of Model Checking* supports finite discrete-time Markov chains,
   MDPs, PCTL, and PCTL*, but its quantitative chapter contains no CTMC or CSL
   treatment. CTMC/CSL claims therefore cannot be attributed to Baier--Katoen
   2008. Compare the [book's Chapter 10 contents and summary, printed pp.
   745--899](https://is.ifmo.ru/books/_principles_of_model_checking.pdf) with the
   separate primary article on [finite CTMCs and CSL](https://doi.org/10.1109/TSE.2003.1205180).
6. Feder--Vardi formulates and motivates the finite-template CSP dichotomy but
   does not prove it; the finite-domain dichotomy proofs belong to Bulatov and
   Zhuk. Its separate MMSNP/CSP theorem uses a deterministic Karp reduction
   from MMSNP to CSP and a randomized polynomial-time Turing reduction from
   CSP to MMSNP; on connected CSP inputs the latter is a **randomized** Karp
   reduction. Kun later derandomized the sparse-incomparability step. See the
   [official Feder--Vardi record](https://epubs.siam.org/doi/10.1137/S0097539794266766),
   the [dedicated reduction-source note](p09-feder-vardi-mmsnp-csp-source-note.md),
   [Kun's primary preprint](https://arxiv.org/pdf/0706.1701),
   [Bulatov, Theorems 1 and 4](https://www.cs.sfu.ca/~abulatov/papers/focs17.pdf),
   and [Zhuk, abstract and main theorem](https://ieee-focs.org/FOCS-2017-Papers/3464a331.pdf).
7. Kozen--Parikh's short completeness proof deliberately omits program tests
   and converse. The test-containing modern PDL presentation must be controlled
   by Harel--Kozen--Tiuryn, not retrofitted into the 1981 syntax. See
   [Kozen--Parikh, printed p. 113](https://www.cs.cornell.edu/~kozen/Papers/ElemPDL.pdf)
   and [Harel--Kozen--Tiuryn, Chapters 5--9 and 11](https://www.cs.cornell.edu/~kozen/Papers/HKT.pdf).

## `N-c-019` — Floyd/Hoare logic, weakest preconditions, and relative completeness

### Robert W. Floyd (1967)

**Identity and access.** Robert W. Floyd, “Assigning Meanings to Programs,” in
J. T. Schwartz (ed.), *Mathematical Aspects of Computer Science*, Proceedings
of Symposia in Applied Mathematics 19, American Mathematical Society, 1967,
pp. 19--32. No DOI was located in the authoritative publication data available
for this item; use the [primary facsimile](https://www.lem12.uksw.edu.pl/images/1/15/AssigningMeanings1967.pdf)
and its printed page numbers.

**Locator, notation, and standing.** Printed pp. 19--24 describe a program as a
flowchart, attach an assertion to selected edges, and generate a local condition
for each command or branch. Those assertions are statements about machine
states at control points; they are not commands and not a new class of program.
The source's “interpretation” is the assignment of such propositions to the
flowchart. Printed pp. 26--31 add strongest verifiable consequents and
well-founded termination functions. These source-side meanings and locators
must accompany any modernization of the notation [in the primary text](https://www.lem12.uksw.edu.pl/images/1/15/AssigningMeanings1967.pdf).

**System, hypotheses, and exact strength.** The system is a sequential
flowchart program with assignments, tests, branches, and joins. If the entry
assertion holds, every local verification condition is valid, and execution
reaches the exit, the exit assertion holds. That is partial correctness. The
separate termination method attaches values in a well-ordered domain and
requires a strict decrease around each relevant cycle; it does not follow from
the partial-correctness annotations alone [Floyd, printed pp. 19--24 and
30--31](https://www.lem12.uksw.edu.pl/images/1/15/AssigningMeanings1967.pdf).

**Proof status and full outline boundary.** Floyd gives the local rules and the
inductive path argument: a true assertion is carried across each traversed
command by its local condition, so any terminating path carries the entry fact
to the exit. For termination he gives the well-order descent idea and a worked
flowchart. He does not supply a later-style structural operational semantics,
a derivation-tree soundness theorem for a Hoare calculus, or Cook's relative
completeness theorem. A reader-facing proof outline may reproduce the path
induction and the no-infinite-descent argument; the later metatheorems must be
credited to later authorities [Floyd, printed pp. 20--24 and 30--31](https://www.lem12.uksw.edu.pl/images/1/15/AssigningMeanings1967.pdf).

**Examples, qualifications, and adjacent variants.** The running-sum
flowchart exhibits assertion placement and verification; the final flowchart
adds a decreasing quantity for termination. Floyd also discusses consistency,
completeness, and strongest consequences at a program-interpretation level,
but those remarks are not Cook's assertion-language-relative theorem. Machine
overflow, side effects, and a fully specified arithmetic state space are not
formalized in this paper [Floyd, printed pp. 24--31](https://www.lem12.uksw.edu.pl/images/1/15/AssigningMeanings1967.pdf).

**Reader-facing reconstruction owed.** Present one small flowchart, annotate
every join and loop entry, list its local verification conditions, prove the
terminating-path claim by induction on the executed path, and then add a
separate well-founded decrease proof. Explicitly bridge the flowchart notation
to Hoare triples without claiming that Floyd printed Hoare's later rule syntax.

### C. A. R. Hoare (1969)

**Identity and access.** C. A. R. Hoare, “An Axiomatic Basis for Computer
Programming,” *Communications of the ACM* 12(10), 1969, pp. 576--580,
[DOI 10.1145/363235.363259](https://doi.org/10.1145/363235.363259); an
[accessible primary scan](https://sites.cs.ucsb.edu/~kemm/courses/cs266/acmhoare69.pdf)
preserves the printed pagination.

**Locator, notation, and standing.** Printed pp. 576--578 explain `P{Q}R`,
where `P` and `R` are assertions and `Q` is a program fragment; the typography
places the command inside braces, unlike the now-common `{P} Q {R}`. The paper
states the assignment axiom schema, consequence, composition, conditional, and
while rules on pp. 577--578. A reconstruction may use modern typography only
after displaying this source bridge [Hoare, printed pp. 576--578](https://sites.cs.ucsb.edu/~kemm/courses/cs266/acmhoare69.pdf).

**System, hypotheses, and exact strength.** The assertions describe states of
a sequential imperative program. The assignment axiom requires capture-safe
substitution of the assigned expression for the assigned variable. The while
rule uses an invariant and establishes the postcondition on loop exit, assuming
the loop terminates; the paper explicitly treats this as partial correctness.
Consequence depends on the validity of the two assertion implications [Hoare,
printed pp. 577--578](https://sites.cs.ucsb.edu/~kemm/courses/cs266/acmhoare69.pdf).

**Proof status and full outline boundary.** The article motivates the axioms by
their intended semantics and derives program properties, but it is not Cook's
later formal soundness-and-relative-completeness treatment. A local handbook
proof should define triple validity, prove assignment by evaluating the
post-state, prove sequencing by an intermediate state, prove the conditional by
case analysis, and prove the partial while rule by induction on the number of
iterations. It must label that as the handbook's reconstruction rather than
misreporting a theorem proved in full metatheoretic form in 1969 [Hoare,
printed pp. 576--579](https://sites.cs.ucsb.edu/~kemm/courses/cs266/acmhoare69.pdf).

**Examples, qualifications, and adjacent variants.** Table III gives the
quotient/remainder program and its assertion chain. Hoare warns that an axiom
set depends on the implementation language and that overflow, range limits,
side effects, and expression evaluation can invalidate naive mathematical
axioms. Termination is a separate obligation; a later total-correctness rule
must therefore add a well-founded variant rather than relabel this rule [Hoare,
printed pp. 578--580](https://sites.cs.ucsb.edu/~kemm/courses/cs266/acmhoare69.pdf).

**Reader-facing reconstruction owed.** Define semantic partial correctness
before presenting the five rule schemas; state substitution side conditions;
give a short soundness proof for each schema; reconstruct the quotient/remainder
derivation; then display a separately labelled total-correctness while rule
with an explicit natural-number or well-founded variant. Do not make the latter
look like Hoare's 1969 printed rule.

### Edsger W. Dijkstra (1975)

**Identity and access.** Edsger W. Dijkstra, “Guarded Commands,
Nondeterminacy and Formal Derivation of Programs,” *Communications of the ACM*
18(8), 1975, pp. 453--457,
[DOI 10.1145/360933.360975](https://doi.org/10.1145/360933.360975). The
[author archive](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD472.html)
and [primary scan](https://www.cs.utexas.edu/~EWD/ewd04xx/EWD472.PDF) provide
the text.

**Locator, notation, and standing.** Section 2, printed pp. 453--454, gives the
guarded-command syntax `if B1 -> SL1 [] ... [] Bn -> SLn fi` and the analogous
`do ... od`. Section 3.1, printed pp. 454--455, defines `wp(S,R)` as the weakest
predicate on initial states guaranteeing that execution of statement `S`
terminates properly in a state satisfying postcondition `R`. Thus `wp` is a
predicate transformer, not a program-state relation and not merely an
abbreviation for a Hoare triple [Dijkstra, sections 2 and 3.1](https://www.cs.utexas.edu/~EWD/ewd04xx/EWD472.PDF).

**System, hypotheses, and exact strength.** If more than one guard is true, a
guarded alternative or repetition chooses nondeterministically; correctness is
demonic, so every allowed choice must establish the postcondition. If no
alternative guard is true, the alternative aborts; repetition terminates when
all guards are false. Dijkstra requires the “law of the excluded miracle”
`wp(S,false)=false`, monotonicity, distribution over conjunction, and equality
over disjunction only for deterministic statements. Assignment and sequencing
receive exact transformer equations [Dijkstra, printed pp. 453--455](https://www.cs.utexas.edu/~EWD/ewd04xx/EWD472.PDF).

**Exact repetition result and proof boundary.** Section 3.2 defines successive
approximants `H_k(R)` for guarded repetition and characterizes its weakest
precondition through the existence of a finite bound on iterations. Theorems 3
and 4 provide invariant/termination obligations, including an integer-valued
quantity bounded below and strictly decreased by each guarded body. The source
derives these laws and uses them to construct programs, but it does not give a
later domain-theoretic fixed-point semantics or a separate weakest-liberal-
precondition development. A full handbook outline must expand the base and
step cases for the approximants, show invariant preservation, and invoke
well-founded descent for termination; anything beyond that is cited [Dijkstra,
printed pp. 455--457](https://www.cs.utexas.edu/~EWD/ewd04xx/EWD472.PDF).

**Examples, qualifications, and adjacent variants.** The maximum-of-two
numbers example illustrates guarded choice; the Euclidean greatest-common-
divisor derivation illustrates repetition and invariant-driven program
construction. Because `wp` entails termination, the equivalence
`{P}S{Q}` iff `P => wp(S,Q)` expresses **total** correctness here. For partial
correctness one needs a liberal precondition or an explicit conditional-on-
termination semantics, neither of which may be smuggled into Dijkstra's
definition [Dijkstra, printed pp. 454--457](https://www.cs.utexas.edu/~EWD/ewd04xx/EWD472.PDF).

**Reader-facing reconstruction owed.** Print the guarded-command grammar and
the nondeterministic/abort behavior; define `wp` with termination in the same
sentence; derive assignment, sequence, and alternative equations; work either
maximum or gcd in full; and prove the invariant-plus-variant repetition rule.
Add a boxed comparison separating total `wp`, partial-correctness triples, and
weakest liberal preconditions.

### Stephen A. Cook (1978)

**Identity and access.** Stephen A. Cook, “Soundness and Completeness of an
Axiom System for Program Verification,” *SIAM Journal on Computing* 7(1),
1978, pp. 70--90, [DOI 10.1137/0207005](https://doi.org/10.1137/0207005);
the [author-hosted primary PDF](https://www.cs.toronto.edu/~sacook/homepage/soundness.pdf)
has printed pagination.

**Locator, notation, model class, and hypotheses.** Printed pp. 71--73 fix a
deterministic ALGOL-like language with assignments, conditionals, while loops,
blocks, and nonrecursive procedures, together with explicit restrictions on
parameters and global variables. Printed pp. 75--77 give the axiom system;
pp. 78--79 define semantic truth as partial correctness. The assertion
language is interpreted over the program domain and must be able to express
the relevant strongest post-relations for the completeness theorem [Cook,
sections 2--4 and 6](https://www.cs.toronto.edu/~sacook/homepage/soundness.pdf).

**Exact result strength.** Theorem 1 proves soundness for the stated system.
The completeness result in section 6 is **relative**: if the underlying
assertion theory is semantically complete and the assertion language is
expressive for the program language in Cook's stated sense, every semantically
true partial-correctness formula is derivable. It is neither an effective
absolute completeness theorem nor a total-correctness theorem [Cook, Theorem 1
and section 6, printed pp. 79--89](https://www.cs.toronto.edu/~sacook/homepage/soundness.pdf).

**Proof status and full outline boundary.** Soundness proceeds rule by rule
against the operational meaning of commands and procedure calls. Relative
completeness constructs the needed assertions from strongest post-relations,
uses them as loop invariants, and handles procedure calls by the source's
inlining/substitution machinery. Cook first proves an obstruction: an effective
complete proof system for all true partial-correctness assertions would decide
an undecidable program property, illustrated by formulas of the form
`true {A} false`. A handbook proof outline must include (i) the undecidability
obstruction, (ii) the exact expressiveness hypothesis, (iii) the construction
of strongest post-relations/invariants, and (iv) the structural induction over
commands; omitting any one of these changes the theorem [Cook, printed pp.
80--89](https://www.cs.toronto.edu/~sacook/homepage/soundness.pdf).

**Examples, qualifications, and adjacent variants.** The theorem is sensitive
to the fixed programming language, assertion language, domain, and procedure
discipline. “Complete” does not mean that a mechanical verifier proves every
correct program without an assertion oracle, and “relative” cannot be dropped.
Cook's theorem strengthens the metatheory around Hoare's calculus; it does not
replace Floyd's flowchart history or Dijkstra's predicate-transformer
derivation [Cook, introduction and sections 5--6](https://www.cs.toronto.edu/~sacook/homepage/soundness.pdf).

**Reader-facing reconstruction owed.** State the programming-language fragment
and triple semantics, prove soundness by cases, give the halting-based barrier
to effective absolute completeness, define the exact expressiveness condition,
and present the relative-completeness induction with the loop-invariant and
procedure cases expanded. The heading and theorem status must both say
“relative completeness for partial correctness.”

### Krzysztof R. Apt (1981)

**Identity and access.** Krzysztof R. Apt, “Ten Years of Hoare's Logic: A
Survey---Part I,” *ACM Transactions on Programming Languages and Systems* 3(4),
1981, pp. 431--483,
[DOI 10.1145/357146.357150](https://doi.org/10.1145/357146.357150). Use the
[CWI repository record](https://ir.cwi.nl/pub/10268) for provenance and the
[accessible article copy](https://www.cs.cornell.edu/courses/cs6860/2010fa/Handouts/Apt10years.pdf)
for the technical text.

**Locator, notation, and model classes.** The survey begins with while programs
and distinguishes partial from total correctness, then reviews soundness and
completeness results and extensions for recursive procedures, local variables,
and parameter mechanisms across printed pp. 431--483. Its notation is a
unifying retrospective presentation, not evidence that every rule or proof
originated in Apt 1981 [Apt, abstract, contents, and sections 2--6](https://www.cs.cornell.edu/courses/cs6860/2010fa/Handouts/Apt10years.pdf).

**Exact strength and proof boundary.** Apt is the controller for which theorem
belongs to which language fragment and whether it concerns partial correctness,
total correctness, soundness, or relative completeness. The article states and
analyzes several established results, supplies some proofs or proof sketches,
and critically notes difficulties in earlier proofs. It is not one monolithic
new completeness theorem. Any handbook reliance must cite the individual
section/theorem and preserve the stated language and assertion-theory
hypotheses; a generic “by Apt” citation is too weak [Apt, printed pp.
431--483](https://www.cs.cornell.edu/courses/cs6860/2010fa/Handouts/Apt10years.pdf).

**Examples, qualifications, and adjacent variants.** The survey shows that
apparently small language changes---recursion, local storage, call-by-name or
call-by-value parameters---alter the required axioms and completeness proof.
It also distinguishes genuine total-correctness systems from partial systems
supplemented with informal termination arguments. Those comparisons make Apt a
boundary authority between the foundational papers, not a substitute for their
primary definitions [Apt, sections on procedures and total correctness](https://www.cs.cornell.edu/courses/cs6860/2010fa/Handouts/Apt10years.pdf).

**Reader-facing reconstruction owed.** End the `N-c-019` presentation with a
source-indexed comparison table: flowchart assertions (Floyd), partial Hoare
calculus (Hoare), total predicate transformers (Dijkstra), relative
completeness under expressiveness (Cook), and later language-fragment
calibration (Apt). For every row state the command language, termination
standing, assertion assumptions, and whether the source contains a proof,
proof sketch, or survey report.

**Attribution correction applied to the handbook.** Apt's printed Rule 6,
while Rule II, assumes a natural-number-indexed assertion p(n) and has premises
p(n+1) implies e, {p(n+1)} S {p(n)}, and p(0) implies not e; its conclusion is
{exists n p(n)} while e do S od {p(0)}. Apt explicitly says that this rule was
formulated in Harel [23] and uses it on the successive-subtraction division
program [Apt, printed pp. 441--442](https://www.cs.cornell.edu/courses/cs6860/2010fa/Handouts/Apt10years.pdf).
The handbook sheet instead uses one decreasing integer expression and a rigid
old-value parameter. That sheet rule is now labelled editorial and proved
directly in the annex; it is **not** called a specialization of Apt's printed
rule.

**Reader-facing delivery status, 2026-08-22.** The presentation now supplies
the editorial Floyd flowchart with its entry/cycle/exit obligations and
separate descent; Hoare's quotient/remainder derivation and a separately
labelled modern total extension; Dijkstra's exact transformer laws, H_k
repetition equations, maximum derivation, and gcd derivation; Cook's post
relation, halting obstruction, sequence/assignment cases, finite-reachability
loop-invariant construction, and procedure-renaming spine; Apt's exact
Harel-attributed rule, division instance, nonstandard-model boundary, and an
expanded comparison table. The remaining proof-depth qualifications are
explicit: the article states Dijkstra's invariant/variant theorem without
proof, while the handbook now supplies an independent finite-approximant proof
including monotonicity of H_k, the zero-variant case, the strong-induction
step, and the final existential bound. Cook's full capture-avoiding
procedure-call substitution argument remains cited to the source rather than
reproduced line for line. This row is materially expanded but Part IX is not
declared source-frozen on that basis alone.

## `N-c-020` — separation logic, locality, and bi-abduction

### Peter W. O'Hearn, John C. Reynolds, and Hongseok Yang (2001)

**Identity and access.** Peter W. O'Hearn, John C. Reynolds, and Hongseok
Yang, “Local Reasoning about Programs that Alter Data Structures,” in Laurent
Fribourg (ed.), *Computer Science Logic*, LNCS 2142, Springer, 2001, pp. 1--19,
[DOI 10.1007/3-540-44802-0_1](https://doi.org/10.1007/3-540-44802-0_1).
Use the [Oxford institutional record](https://ora.ox.ac.uk/objects/uuid%3Af5c0e33c-6b0f-4d01-97f0-bc2430649b06)
for identity and the [accessible primary paper](https://citeseerx.ist.psu.edu/document?doi=219c95e028a1a8e2baebdecb8b998e12a03bc33b&repid=rep1&type=pdf)
for technical content.

**Locator, notation, and standing.** Sections 2--3 define a low-level store
and finite heap with lookup, update, allocation, deallocation, and unrestricted
address arithmetic. Assertions come from a possible-worlds semantics for
bunched implications: ordinary conjunction speaks about one heap, separating
conjunction says that the heap can be split into disjoint parts satisfying the
two conjuncts, and separating implication describes heap extension. These are
assertion-forming connectives; they are neither heap commands nor untyped
English uses of “and” [O'Hearn--Reynolds--Yang, abstract and sections
2--3](https://citeseerx.ist.psu.edu/document?doi=219c95e028a1a8e2baebdecb8b998e12a03bc33b&repid=rep1&type=pdf).

**System, hypotheses, and exact strength.** The paper's “small axioms” mention
only the cells accessed by a primitive heap command. Local reasoning then adds
an invariant describing disjoint, untouched storage. The intended triple is
fault avoiding: the precondition must provide the cells the command will
access, not merely make the postcondition true when an execution happens not to
fault. The source supports local specifications for pointer-manipulating
sequential programs; it is not a concurrency logic and it does not make
unrestricted aliasing disappear [O'Hearn--Reynolds--Yang, sections 3--5](https://citeseerx.ist.psu.edu/document?doi=219c95e028a1a8e2baebdecb8b998e12a03bc33b&repid=rep1&type=pdf).

**Proof status and full outline boundary.** The paper supplies the heap model,
small axioms, local inference principles, and worked derivations demonstrating
their validity. A full reader-facing soundness outline must define disjoint heap
union, prove each primitive axiom against command semantics, prove the locality
lemma saying that execution on a larger disjoint heap preserves the framed
part, and derive the frame rule subject to its variable-modification condition.
The paper does not prove completeness of separation logic or completeness of
an automatic symbolic executor; neither claim may be inferred [O'Hearn--Reynolds--Yang,
sections 3--6](https://citeseerx.ist.psu.edu/document?doi=219c95e028a1a8e2baebdecb8b998e12a03bc33b&repid=rep1&type=pdf).

**Examples, qualifications, and adjacent variants.** The examples manipulate
linked structures by describing only the footprint a command uses. They also
show why ordinary conjunction cannot encode disjoint ownership: two assertions
may both hold of a whole heap while saying nothing about whether their cells
overlap. Reynolds 2002 gives the more systematic survey and explicit frame-rule
soundness sketch; this 2001 paper remains the source for the local-reasoning
proposal and small-axiom presentation [O'Hearn--Reynolds--Yang, examples in
sections 4--6](https://citeseerx.ist.psu.edu/document?doi=219c95e028a1a8e2baebdecb8b998e12a03bc33b&repid=rep1&type=pdf).

**Reader-facing reconstruction owed.** Define the store/heap model, `emp`, a
singleton points-to assertion, separating conjunction, and separating
implication before using them. Give lookup, update, allocation, and deallocation
small axioms, one aliasing counterexample, one local pointer proof, and the
locality-to-frame proof outline. State explicitly that the row concerns
sequential fault-avoiding partial correctness.

### John C. Reynolds (2002)

**Identity and access.** John C. Reynolds, “Separation Logic: A Logic for
Shared Mutable Data Structures,” *Proceedings of the 17th Annual IEEE Symposium
on Logic in Computer Science*, IEEE Computer Society, 2002, pp. 55--74,
[DOI 10.1109/LICS.2002.1029817](https://doi.org/10.1109/LICS.2002.1029817);
the [author-hosted primary PDF](https://www.cs.cmu.edu/~jcr/seplogic.pdf) carries
the proceedings pagination.

**Locator, notation, and standing.** Printed pp. 56--59 model a state by a
stack mapping variables to integer values and a finite partial heap mapping
addresses to stored values. `emp` holds exactly on the empty heap; `E |-> E'`
holds on the singleton heap at the address denoted by `E`; `p * q` holds when
the current heap splits into disjoint subheaps satisfying `p` and `q`; and
`p -* q` holds when every disjoint extension satisfying `p` makes the combined
heap satisfy `q`. The magic wand is therefore a quantified assertion about
disjoint heap extension, not material implication [Reynolds, printed pp.
57--59](https://www.cs.cmu.edu/~jcr/seplogic.pdf).

**System, hypotheses, and exact strength.** The command language includes
heap lookup, mutation, allocation, and disposal, with recursive procedures and
extensions for arrays and address arithmetic discussed later. The frame rule
has the form `{p} c {q}` implies `{p * r} c {q * r}` provided `c` modifies no
variable free in `r`. Its soundness also depends on the locality/fault behavior
of the heap commands. Removing the side condition is unsound: the command
could change a stack variable on which the framed assertion depends [Reynolds,
printed pp. 60--62](https://www.cs.cmu.edu/~jcr/seplogic.pdf).

**Proof status and full outline boundary.** Printed pp. 61--63 sketch soundness
by restricting a larger initial heap to the footprint used by the command,
executing the command locally, and reattaching the unchanged disjoint frame.
The paper develops rule schemas and examples but does not give a completeness
theorem for all valid heap triples. A full handbook outline must spell out
heap decomposition, safety monotonicity, frame preservation, and the free-
variable side condition; it may cite, rather than reproduce, the source's
larger recursive-procedure and address-arithmetic development [Reynolds,
printed pp. 60--68](https://www.cs.cmu.edu/~jcr/seplogic.pdf).

**Examples, counterexamples, and adjacent variants.** The list-reversal proof
shows a loop invariant that separates the already reversed segment from the
unprocessed segment. The source also uses assertion examples to distinguish a
singleton cell from a heap merely containing that cell and to show how aliasing
can make an apparently obvious update rule false. “Shared” in the title means
mutable structures with sharing and aliases; it does not by itself assert a
concurrent interference model [Reynolds, printed pp. 58--60 and 63--68](https://www.cs.cmu.edu/~jcr/seplogic.pdf).

**Reader-facing reconstruction owed.** Give the exact satisfaction clauses for
all four spatial primitives, including singleton-heap exactness; prove the frame
rule from a stated locality lemma; work list reversal with the heap split shown
after each loop step; and include the variable-side-condition counterexample.
The proof status must say “soundness sketch/reconstruction,” not completeness.

### Cristiano Calcagno, Dino Distefano, Peter W. O'Hearn, and Hongseok Yang (2011)

**Identity and access.** Cristiano Calcagno, Dino Distefano, Peter W. O'Hearn,
and Hongseok Yang, “Compositional Shape Analysis by Means of Bi-Abduction,”
*Journal of the ACM* 58(6), Article 26, 2011, pp. 26:1--26:66,
[DOI 10.1145/2049697.2049700](https://doi.org/10.1145/2049697.2049700). Use the
[Oxford record and accepted manuscript](https://ora.ox.ac.uk/objects/uuid%3Abcfefe74-a79c-4155-8160-c51f92f05466)
or the [author-hosted JACM manuscript](https://www.cs.ox.ac.uk/people/hongseok.yang/paper/jacm11-biabduction-webversion.pdf).

**Locator, notation, and standing.** Sections 2--3, pp. 26:7 onward, set up
symbolic heaps, separated heap models, and abduction. The bi-abduction problem
has the source-side shape `A * ?anti-frame |- G * ?frame`: infer missing heap
resources that make the desired symbolic execution possible and, at the same
time, infer resources left untouched. The anti-frame and frame are assertions
to solve for, not new heap regions postulated independently of a solution
[Calcagno et al., sections 2--3](https://www.cs.ox.ac.uk/people/hongseok.yang/paper/jacm11-biabduction-webversion.pdf).

**System, hypotheses, and exact strength.** The analyzed programs are
procedural, heap-manipulating programs represented through the paper's
separation-logic abstraction. Compositional analysis infers procedure
pre/postconditions without beginning from whole-program call contexts. The
soundness theorem is conditional on termination of the inference procedure and
soundness of the primitive proof rules; it says inferred specifications denote
true tight, fault-avoiding Hoare triples. It does not say every true
specification is inferred [Calcagno et al., Theorem 4.14 and surrounding text](https://www.cs.ox.ac.uk/people/hongseok.yang/paper/jacm11-biabduction-webversion.pdf).

**Proof status and full outline boundary.** The paper proves soundness results
for abduction/bi-abduction components and states program-analysis soundness as
Theorem 4.14 in both abstract-interpretation and Hoare-logic forms. The authors
explicitly describe the final program-analysis statement as somewhat informal:
filling all details requires the cited operational semantics, after which the
argument is induction over the analysis's use of sound proof rules. A handbook
must not upgrade this to a fully reproduced mechanized proof. It should show
one sound bi-abduction step, explain specification propagation through calls,
and state the remaining semantic induction as cited [Calcagno et al., section
4, especially Theorem 4.14](https://www.cs.ox.ac.uk/people/hongseok.yang/paper/jacm11-biabduction-webversion.pdf).

**Examples, qualifications, and adjacent variants.** The source evaluates
compositional shape analysis on list-manipulating code and larger code bases,
while emphasizing that open questions concern precision, completeness, and
complexity rather than the claimed soundness. The abstraction can lose
precision for features such as arrays or pointer arithmetic, and the presented
analysis is not a concurrency verifier [Calcagno et al., experimental sections
and conclusion](https://www.cs.ox.ac.uk/people/hongseok.yang/paper/jacm11-biabduction-webversion.pdf).

**Reader-facing reconstruction owed.** Start from a failed symbolic heap step,
pose one explicit bi-abduction sequent, solve its anti-frame and frame, and show
how the result becomes a procedure summary. State Theorem 4.14 with its
termination and semantic assumptions, distinguish soundness from precision and
completeness, and point to tools only after the logical mechanism is defined.

### Peter W. O'Hearn (2019)

**Identity and access.** Peter W. O'Hearn, “Separation Logic,”
*Communications of the ACM* 62(2), 2019, pp. 86--95,
[DOI 10.1145/3211968](https://doi.org/10.1145/3211968). The [UCL institutional
record](https://discovery.ucl.ac.uk/id/eprint/10075346/) and [accepted manuscript](https://discovery.ucl.ac.uk/id/eprint/10075346/1/O%27Hearn_AAM_sl-cacm-cameraready.pdf)
provide an accessible authoritative copy.

**Locator, notation, model class, and role.** The article is a retrospective
overview. Printed pp. 86--90 introduce separation, small footprints, and the
frame rule; later pages connect those ideas to automatic reasoning,
bi-abduction, Infer, and industrial static analysis. It does not redefine the
heap satisfaction relation with the formal completeness of Reynolds 2002 or
the 2001 paper, and it must not be used as the sole proof authority [O'Hearn,
printed pp. 86--95](https://discovery.ucl.ac.uk/id/eprint/10075346/1/O%27Hearn_AAM_sl-cacm-cameraready.pdf).

**Exact result strength and proof boundary.** O'Hearn explains why local
reasoning made compositional automation possible and reports the path from
small axioms and the frame rule to bi-abductive analysis. These are historical
and engineering claims in a survey article, not a new soundness or completeness
theorem. Formal semantic clauses and soundness proofs must remain attached to
the 2001, 2002, and 2011 primary technical papers [O'Hearn, full article](https://discovery.ucl.ac.uk/id/eprint/10075346/1/O%27Hearn_AAM_sl-cacm-cameraready.pdf).

**Examples, qualifications, and adjacent variants.** The article's tools
discussion is appropriate for the register's requested tools paragraph, but a
production deployment demonstrates scalability and utility, not logical
completeness or absence of every bug. The retrospective also spans several
generations of separation logic; the handbook must say which cited paper
supports each formal claim [O'Hearn, later sections](https://discovery.ucl.ac.uk/id/eprint/10075346/1/O%27Hearn_AAM_sl-cacm-cameraready.pdf).

**Reader-facing reconstruction owed.** Close `N-c-020` with a short historical
and tools paragraph: local heap reasoning, frame-based composition,
bi-abductive summary inference, then deployment. Label every claim as semantic,
algorithmic, experimental, or historical. Do not let the tools paragraph
replace the exact heap model, frame soundness outline, or bi-abduction example.

**Reader-facing delivery status, 2026-08-22.** The presentation now contains
the exact stack--finite-heap satisfaction clauses for emp, singleton
points-to, separating conjunction, and separating implication; eliminable
one-cell and consecutive-block abbreviations; source-valid local lookup,
mutation, allocation, and deallocation triples with their side conditions and
direct operational justifications; the locality-to-frame proof; independent
aliasing and modified-stack-variable counterexamples; and a complete
list-reversal preservation derivation showing the three disjoint heap factors
before and after lookup, mutation, and pointer reassignment. It also solves one
bi-abduction sequent, propagates the anti-frame and frame through a concrete
mutation to obtain a path summary, states the conditional standing of Theorem
4.14, and leaves the historical/tools paragraph last. The lookup triple is
deliberately restricted to an address expression not containing its assigned
variable; Reynolds's more general primed auxiliary-variable schema remains
cited, as do the larger recursive-procedure development and the operational
framework delegated by the 2011 theorem. Those explicit citation boundaries
do not erase the delivered local reconstruction, and this row alone does not
freeze Part IX.

## `N-c-021` — propositional dynamic logic

### Vaughan R. Pratt (1976)

**Identity and access.** Vaughan R. Pratt, “Semantical Considerations on
Floyd--Hoare Logic,” *Proceedings of the 17th Annual Symposium on Foundations
of Computer Science*, IEEE, 1976, pp. 109--121,
[DOI 10.1109/SFCS.1976.4567894](https://doi.org/10.1109/SFCS.1976.4567894).
The expanded contemporaneous primary version is [MIT-LCS-TR-168, September
1976](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-168.pdf).

**Locator, notation, and standing.** Technical-report pp. 4--10 model a program
`a` as a set of state transitions, hence a binary relation. A partial-
correctness assertion is an ordered pair `(P,Q)` of state formulas; `P{a}Q`
means that every transition in `a` taking a `P`-state ends in a `Q`-state. Pratt
contrasts this external pair-based language with modal formulas in which a
program relation itself indexes an operator. Programs, state predicates, and
modal formulas therefore retain three distinct standings [Pratt, sections
2--3](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-168.pdf).

**System, hypotheses, and exact strength.** The relational model admits
nondeterministic programs. `[a]Q` expresses that every terminating `a`-
successor satisfies `Q`, while `<a>Q` expresses that some such successor does.
Thus `P -> [a]Q` represents Hoare partial correctness, whereas `<a>true`
expresses possible termination---something a bare partial-correctness pair
cannot positively demand. Pratt studies semantic theories and axiomatizations
for program operations under this relational interpretation; it is a precursor
to, not yet the exact modern regular-program PDL package [Pratt, technical-
report sections 2--5](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-168.pdf).

**Proof status and full outline boundary.** The report proves semantic
correspondences and results for the program constructs and fragments it
actually defines, including loop-free cases. It does not contain the later
Fischer--Ladner closure construction, Kozen--Parikh's completeness proof for
the Segerberg axioms, or the final EXPTIME classification. A handbook outline
should prove the relational satisfaction equations for composition, choice,
and the box/diamond duality, then stop and hand iteration, completeness, and
complexity to the later sources [Pratt, technical report](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-168.pdf).

**Examples, qualifications, and adjacent variants.** Pratt's transition-pair
semantics makes the nontermination limitation of partial-correctness assertions
explicit. It also exposes the difference between an **external** Hoare
assertion and an **internal** modal formula containing a program operator. A
historical paragraph should not call every construction in the report “PDL” in
the later Fischer--Ladner syntax [Pratt, pp. 5--10](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-168.pdf).

**Reader-facing reconstruction owed.** Begin with one binary-relation program,
define `P{a}Q`, `[a]Q`, and `<a>Q`, prove `P{a}Q` iff `P -> [a]Q` is valid, and
give a terminating/nonterminating pair showing why partial correctness cannot
assert existence of a final state. Only then pass to regular program terms.

### Michael J. Fischer and Richard E. Ladner (1979)

**Identity and access.** Michael J. Fischer and Richard E. Ladner,
“Propositional Dynamic Logic of Regular Programs,” *Journal of Computer and
System Sciences* 18(2), 1979, pp. 194--211,
[DOI 10.1016/0022-0000(79)90046-1](https://doi.org/10.1016/0022-0000(79)90046-1).
Use the [publisher article record](https://www.sciencedirect.com/science/article/pii/0022000079900461)
for identity and the [accessible primary scan](https://www.cs.man.ac.uk/~ezolin/dl/bib/Propositional_Dynamic_Logic_of_regular_programs_%28JCSS_1979%29.pdf)
for the printed text.

**Locator, notation, and standing.** Sections 1--2, printed pp. 194--199,
define formulas from propositional atoms and modalities indexed by regular
program terms. Atomic programs denote binary relations; choice denotes union,
composition denotes relational composition, iteration denotes reflexive-
transitive closure, and a test denotes the identity relation restricted to
states satisfying its test formula. `[alpha]A` quantifies over all
`alpha`-successors and `<alpha>A` over some successor [Fischer--Ladner,
sections 1--2](https://www.cs.man.ac.uk/~ezolin/dl/bib/Propositional_Dynamic_Logic_of_regular_programs_%28JCSS_1979%29.pdf).

**Closure, model class, and exact result strength.** The models are Kripke-style
relational structures for atomic programs plus a valuation of proposition
letters. The Fischer--Ladner closure is the least finite set containing the
input formula and closed not only under subformulas but under the one-step
unfoldings forced by composition, choice, test, and star. Filtration/types over
that closure yield an exponential finite-model bound. For length `n`, the paper
proves a deterministic exponential lower bound of the form `d^n/log n` for
some `d>1` and a nondeterministic exponential upper bound `c^n`; those are its
stated bounds, not yet the later deterministic EXPTIME-completeness slogan
[Fischer--Ladner, abstract and decision-procedure sections](https://www.cs.man.ac.uk/~ezolin/dl/bib/Propositional_Dynamic_Logic_of_regular_programs_%28JCSS_1979%29.pdf).

**Proof status and full outline boundary.** The source proves finiteness and a
linear-size bound for the closure up to its coding convention, establishes the
truth-preserving filtration/canonical-type lemmas needed for an exponential
model, and derives the decision bounds. A full handbook outline must show each
extra star/composition closure clause, count the possible truth types by
`2^{|FL(phi)|}`, prove the truth lemma by induction with the star case
expanded, and explain how the search procedure uses the finite model. The
matching deterministic EXPTIME upper/lower classification should then be cited
to the later synthesis rather than attributed verbatim to this paper
[Fischer--Ladner, printed pp. 199--211](https://www.cs.man.ac.uk/~ezolin/dl/bib/Propositional_Dynamic_Logic_of_regular_programs_%28JCSS_1979%29.pdf).

**Examples, qualifications, and adjacent variants.** The article applies the
decision method to regular expressions, Ianov schemes, and classical modal
systems. The finite-model theorem is for the stated propositional regular-
program logic; first-order dynamic logic and nonregular program operations do
not inherit it automatically [Fischer--Ladner, abstract and final sections](https://www.cs.man.ac.uk/~ezolin/dl/bib/Propositional_Dynamic_Logic_of_regular_programs_%28JCSS_1979%29.pdf).

**Reader-facing reconstruction owed.** Give mutually recursive program/formula
syntax, relational semantics, the exact closure clauses, an explicit closure
calculation for a formula containing star and test, the exponential small-model
proof outline, and the source's own complexity bounds. Keep the later exact
EXPTIME statement in a separately sourced theorem.

### Dexter Kozen and Rohit Parikh (1981)

**Identity and access.** Dexter Kozen and Rohit Parikh, “An Elementary Proof of
the Completeness of PDL,” *Theoretical Computer Science* 14(1), 1981,
pp. 113--118,
[DOI 10.1016/0304-3975(81)90019-0](https://doi.org/10.1016/0304-3975(81)90019-0);
use the [author-hosted primary PDF](https://www.cs.cornell.edu/~kozen/Papers/ElemPDL.pdf).

**Locator, notation, and standing.** Printed p. 113 defines programs from
primitive programs by union, composition, and star and formulas from
propositional connectives and modalities. The authors explicitly omit converse
and tests for simplicity. Printed pp. 113--114 list the axiom system commonly
attributed there to Segerberg: modal distribution and necessitation, reduction
axioms for choice and composition, star unfolding, and star induction [Kozen--Parikh,
printed pp. 113--114](https://www.cs.cornell.edu/~kozen/Papers/ElemPDL.pdf).

**Model class, hypotheses, and exact strength.** Atomic programs are binary
relations on states and compound programs receive the regular relational
operations. The theorem is weak deductive completeness for validity in this
test-free PDL: every valid formula is derivable in the displayed system. It is
not strong completeness for arbitrary premise sets, not first-order dynamic
logic, and not a complexity theorem [Kozen--Parikh, theorem on printed p.
114](https://www.cs.cornell.edu/~kozen/Papers/ElemPDL.pdf).

**Proof status and full outline boundary.** Printed pp. 114--118 give an
elementary finite canonical-model proof. Starting from a consistent formula,
the proof forms a finite Fischer--Ladner-style closure, builds states from
appropriate consistent subsets/types, and proves three lemmas culminating in a
truth lemma and a state satisfying the formula. The star case uses the induction
axiom to obtain the required reachability property. A reader-facing outline
must state all three lemmas and expand the star step; a one-sentence “canonical
model” pointer is not the full proof boundary [Kozen--Parikh, printed pp.
114--118](https://www.cs.cornell.edu/~kozen/Papers/ElemPDL.pdf).

**Examples, qualifications, and adjacent variants.** The paper notes the
resulting exponential finite-model bound but does not optimize a decision
algorithm. Because tests are omitted, its exact syntax cannot be used to prove
completeness of a handbook calculus that includes `?A` unless the extra axiom
and proof case are supplied from another source [Kozen--Parikh, printed pp.
113 and 118](https://www.cs.cornell.edu/~kozen/Papers/ElemPDL.pdf).

**Reader-facing reconstruction owed.** Display the exact test-free axiom list,
prove soundness of the star unfolding/induction axioms, then give the finite
canonical-model completeness proof with its closure and star lemma. Follow it
with an explicit notation-and-scope bridge to the test-containing presentation;
do not silently add `?` to the 1981 theorem.

### David Harel, Dexter Kozen, and Jerzy Tiuryn (2000)

**Identity and access.** David Harel, Dexter Kozen, and Jerzy Tiuryn,
*Dynamic Logic*, Foundations of Computing, MIT Press, 2000, ISBN
978-0-262-08289-1, [publisher DOI
10.7551/mitpress/2516.001.0001](https://doi.org/10.7551/mitpress/2516.001.0001).
Use the [MIT Press record](https://mitpress.mit.edu/9780262527668/dynamic-logic/)
for book identity, the [authors' authoritative contents/overview](https://www.cs.cornell.edu/~kozen/Papers/HKT.pdf)
for the chapter map, and the [published Chapters 4--10 hosted on the authors'
Cornell course site](https://www.cs.cornell.edu/courses/cs6860/2019sp/Handouts/HKT4-10.pdf)
for the operative text.

**Locator, notation, and model classes.** Chapter 5, pp. 163--188, gives PDL
syntax, relational semantics, computation sequences, the deductive system,
star, tests, and the Hoare-logic encoding. Chapter 6, pp. 191--202, gives
Fischer--Ladner closure, filtration, and the small-model theorem. Chapter 7,
pp. 203--209, treats deductive completeness. Chapter 8, pp. 211--225, gives a
deterministic exponential-time algorithm and lower bound. Chapter 10,
pp. 259--280, separates deterministic PDL, restricted tests, converse,
well-foundedness/total correctness, and concurrency [Harel--Kozen--Tiuryn,
authoritative table of contents](https://www.cs.cornell.edu/~kozen/Papers/HKT.pdf).

**Exact result strength and relation to adjacent variants.** For standard
propositional PDL with regular programs and tests, satisfiability and validity
are EXPTIME-complete, the logic has an exponential finite-model property, and
the displayed axiomatization is complete. The book's organization is also the
authority for keeping converse, deterministic programs, nonregular programs,
first-order dynamic logic, and total-correctness extensions out of the base
theorem [Harel--Kozen--Tiuryn, Chapters 5--11 as identified in the contents](https://www.cs.cornell.edu/~kozen/Papers/HKT.pdf).

**Exact internal source map.** The published chapter text was acquired from the
authors' Cornell course site. Axiom System 5.5 is the test-containing calculus.
Section 6.1 gives the simultaneous Fischer--Ladner closure; Lemma 6.4 is the
filtration lemma; and Theorem 6.5 gives the exponential finite-model bound.
Theorem 7.6 is the deductive completeness result. Algorithm 8.2 is the
type-deletion decision procedure, Theorem 8.4 proves deterministic
single-exponential time, and Theorem 8.5 proves EXPTIME hardness through the
computation tree of a linear-space alternating Turing machine. These statements
and their proof routes were inspected in the published Chapters 5--8. No claim
is transferred from these base-PDL results to a Chapter 10 extension without
its separate hypotheses.

**Examples and reader-facing reconstruction owed.** Use Harel--Kozen--Tiuryn
as the modern controller: present one small relational model, evaluate both a
box and diamond formula containing a test, calculate its Fischer--Ladner
closure, state the exponential small-model bound, give the Kozen--Parikh proof
boundary, and state EXPTIME membership and hardness with the algorithm and
reduction roles separated. End with a variants table whose base row is PDL and
whose other rows explicitly change syntax or model class.

**Reader-facing delivery status, 2026-08-22.** The presentation now begins
with Pratt's exact relational clauses for an external partial-correctness pair,
box, and diamond; proves the triple/modal bridge and the composition, choice,
and duality equations; and gives an explicit halting/empty-relation pair that
separates partial correctness from possible termination. It then prints all
regular-program relational clauses, calculates a ten-formula closure containing
both star and test obligations, and gives the quotient-state count and the
truth-lemma proof with the star propagation step exposed. Fischer--Ladner's
literal nondeterministic upper and deterministic lower bounds remain separate
from the later exact classification. For Kozen--Parikh, the manuscript now
prints the seven test-free Segerberg axiom groups, proves both star principles
sound, and reconstructs all three canonical-model lemmas, including the finite
atom-set argument where induction is actually used. It explicitly refuses to
insert tests into that 1981 theorem. Harel--Kozen--Tiuryn then controls the
test-containing sheet, a concrete test model, the exact small-model locators,
all three steps and the invariant of Algorithm 8.2, the alternating-machine
hardness roles, and a variant table that changes syntax or model class row by
row. This closes the reader-facing reconstruction owed by N-c-021; it does not
by itself freeze Part IX.

## `N-c-022` — definite and normal logic programs, SLD, and negation as failure

### Robert A. Kowalski (1974)

**Identity and access.** Robert A. Kowalski, “Predicate Logic as Programming
Language,” *Information Processing 74: Proceedings of the IFIP Congress*,
North-Holland, 1974, pp. 569--574. No DOI was located for this proceedings
paper. Identity and pagination are confirmed by the [author's bibliography](https://www.doc.ic.ac.uk/~rak/papers/rak.html);
use the [author-hosted primary PDF](https://www.doc.ic.ac.uk/~rak/papers/IFIP74.pdf).

**Locator, notation, and standing.** Printed pp. 569--571 treat clauses as both
logical sentences and executable procedures: a selected goal atom is matched
against a clause head, and the clause body supplies replacement subgoals.
Clauses are formulas/program components; goals are the questions under proof;
the selection rule is control information. This is the source of the
logic-plus-control distinction, not a warrant to identify one particular
depth-first implementation with logical consequence [Kowalski, printed pp.
569--574](https://www.doc.ic.ac.uk/~rak/papers/IFIP74.pdf).

**System, hypotheses, and exact strength.** The paper works with predicate-
logic clauses in a resolution-based operational reading and emphasizes
nondeterministic choices among applicable clauses. It gives computation/
and-or-tree presentations and examples of executing relations in more than one
direction. It predates the later fully separated least-Herbrand-model,
immediate-consequence-operator, and strong SLD completeness package [Kowalski,
full paper](https://www.doc.ic.ac.uk/~rak/papers/IFIP74.pdf).

**Proof status and full outline boundary.** This six-page conference paper is a
foundational conceptual and operational presentation. It does not prove the
later theorem that every correct answer has an SLD-computed answer under any
fixed computation rule, nor the fixpoint equality. The handbook may reconstruct
one resolution step and computation tree from the source; model/fixpoint and
SLD soundness/completeness proofs must be sourced below [Kowalski, full paper](https://www.doc.ic.ac.uk/~rak/papers/IFIP74.pdf).

**Examples, qualifications, and adjacent variants.** The examples illustrate
the same logical relation used under different input/output modes. They do not
establish termination, a search order, or Prolog's operational behavior. A
finite logical search tree and an interpreter's traversal of that tree are
different objects [Kowalski, examples on printed pp. 570--573](https://www.doc.ic.ac.uk/~rak/papers/IFIP74.pdf).

**Reader-facing reconstruction owed.** Give a definite-clause relation, run one
goal in two modes, draw the complete SLD-style branching tree, and separately
mark atom selection, clause choice, and tree-search strategy. Credit the
historical procedural reading here; postpone the exact semantics and
completeness theorem.

### Maarten H. van Emden and Robert A. Kowalski (1976)

**Identity and access.** Maarten H. van Emden and Robert A. Kowalski, “The
Semantics of Predicate Logic as a Programming Language,” *Journal of the ACM*
23(4), 1976, pp. 733--742,
[DOI 10.1145/321978.321991](https://doi.org/10.1145/321978.321991); use the
[author-hosted primary paper](https://maarten.vanemden.com/Publications/kowVE.pdf).

**Locator, notation, and standing.** Printed pp. 734--738 define Herbrand
interpretations and a transformation on interpretations induced by a set of
Horn clauses. In modern notation, for a definite program `P`, `T_P(I)` contains
the heads of ground clause instances whose body atoms all belong to `I`. This
modern subscripted notation is a reader bridge to the source transformation;
`T_P` is a monotone operator on sets of ground atoms, not a derivation step and
not a program predicate [van Emden--Kowalski, printed pp. 734--738](https://maarten.vanemden.com/Publications/kowVE.pdf).

**Model class, hypotheses, and exact strength.** For definite/Horn programs,
the least Herbrand model is the least fixed point obtained by iterating the
immediate-consequence transformation from the empty interpretation; it also
coincides with the operationally generated success set under the paper's
conditions. The equality depends on positivity/definiteness. Normal programs
with default negation do not inherit this monotone least-fixed-point semantics
[van Emden--Kowalski, theorem development on printed pp. 736--741](https://maarten.vanemden.com/Publications/kowVE.pdf).

**Proof status and full outline boundary.** The paper proves the connection
among model-theoretic, fixpoint, and operational semantics. The proof shows
monotonicity, identifies models with pre-fixed points, applies iteration from
the least interpretation, and relates finite stages to finite deductions. A
reader-facing proof must include both inclusions between the iterated fixed
point and the least Herbrand model and an induction relating iteration depth to
proof-tree height. Later mgu/computed-answer details belong to the SLD sources
[van Emden--Kowalski, printed pp. 736--742](https://maarten.vanemden.com/Publications/kowVE.pdf).

**Examples, qualifications, and adjacent variants.** A recursive relation can
require arbitrarily many finite iterations even though each derived ground atom
appears at a finite stage; a finite database need not reach a fixed point in a
fixed number independent of the input. The paper's declarative/operational
coincidence does not prove that Prolog's leftmost depth-first traversal will
find every consequence [van Emden--Kowalski, examples and concluding discussion](https://maarten.vanemden.com/Publications/kowVE.pdf).

**Reader-facing reconstruction owed.** Define terms, Herbrand universe/base,
ground instances, Herbrand interpretation, definite clause/program, `T_P`, and
its iterates. Work a recursive example through at least three stages, prove
`lfp(T_P)=M_P`, and then state exactly which operational success set coincides
with that model.

### Keith L. Clark (1978)

**Identity and access.** Keith L. Clark, “Negation as Failure,” in Hervé
Gallaire and Jack Minker (eds.), *Logic and Data Bases*, Plenum Press, 1978,
pp. 293--322,
[DOI 10.1007/978-1-4684-3384-5_11](https://doi.org/10.1007/978-1-4684-3384-5_11).
The [author's publication page and primary PDF](https://www.doc.ic.ac.uk/~klc/neg.html)
provide the text and reduced abstract.

**Locator, notation, and standing.** Clark defines negation as failure as an
operational inference: infer `not A` when every attempted proof of `A` finitely
fails. He also defines the completed database by collecting the clauses for
each predicate into an if-and-only-if definition, existentially quantifying
local variables, and adding an equality theory. Operational finite failure,
the completion formula, and classical negation in that formula are distinct
[Clark, sections 2--4](https://www.doc.ic.ac.uk/~klc/neg.html).

**System, hypotheses, and exact strength.** The base is a Horn-clause theorem
prover extended by the failure rule. Under the paper's stated database and
equality assumptions, negative answers obtained by finite failure are logical
consequences of the completed database. The result is a soundness direction:
failure-derived negative facts are licensed by completion. It is not the claim
that arbitrary nonderivability licenses negation, and it is not stable-model
semantics [Clark, abstract and main soundness development](https://www.doc.ic.ac.uk/~klc/neg.html).

**Proof status and full outline boundary.** The proof translates failure of all
branches into the completed definitions and proceeds through the finite failed
tree. A full handbook outline must define finite failure, translate each failed
leaf and internal node into a completion consequence, and state the equality
axioms used in the unification cases. Infinite search is outside that induction:
failure to return is not finite failure [Clark, proof sections](https://www.doc.ic.ac.uk/~klc/neg.html).

**Examples, counterexamples, and adjacent variants.** A closed-world database
example supports a negative answer when every defining clause finitely fails.
A recursive goal with an infinite branch is the required counterexample to the
naive equation “not proved = false.” Completion may also have classical models
that behave differently from stable models; `N-c-023` must therefore begin a
new semantic presentation, not continue this one as if the definitions were
identical [Clark, examples and qualifications](https://www.doc.ic.ac.uk/~klc/neg.html).

**Reader-facing reconstruction owed.** Print a small program and its Clark
completion side by side, include the equality theory at the stated level, draw
one finitely failed tree, prove its negative answer from the completion, and
show an infinite-branch example where negation as failure is not licensed.

### Krzysztof R. Apt and Maarten H. van Emden (1982)

**Identity and access.** Krzysztof R. Apt and Maarten H. van Emden,
“Contributions to the Theory of Logic Programming,” *Journal of the ACM* 29(3),
1982, pp. 841--862,
[DOI 10.1145/322326.322339](https://doi.org/10.1145/322326.322339). The [CWI
record](https://ir.cwi.nl/pub/10272) and [final primary PDF](https://ir.cwi.nl/pub/10272/10272D.pdf)
are authoritative.

**Locator, notation, and standing.** Sections 2--4 define interpretations,
least/greatest fixed points, definite clauses, and SLD trees. An SLD step
selects one atom in a goal, standardizes apart a program clause, takes a most
general unifier, and replaces the selected atom by the instantiated body. The
computation rule chooses the atom; the SLD tree branches over matching clauses;
the traversal strategy is still a third matter [Apt--van Emden, printed pp.
841--848](https://ir.cwi.nl/pub/10272/10272D.pdf).

**Model class, hypotheses, and exact strength.** For definite programs, section
5 proves that successful SLD computation is sound for the least fixed point;
Corollary 5.2 gives soundness of SLD refutations and Corollary 5.3 places the
success set inside the least model. Subsequent sections prove completeness via
continuity and analyze finite failure. Greatest-fixed-point characterizations
apply only under the paper's additional conditions; they are not the default
semantics of every logic program [Apt--van Emden, sections 5--8](https://ir.cwi.nl/pub/10272/10272D.pdf).

**Proof status and full outline boundary.** The soundness proof reads an SLD
derivation backwards and places every ground instance of the substituted atoms
remaining `i` steps before success in `T_P^i(empty)`. Continuity supplies the
finite stage needed for ground completeness. The first-order answer theorem
then needs the mgu lifting lemma, the fresh-constant identity-answer lemma, and
the combination of the component refutations; merely showing propositional
Horn completeness does not discharge computed answers. The finite-failure
proof is a separate finite-tree induction [Apt--van Emden, printed pp. 847--861](https://ir.cwi.nl/pub/10272/10272D.pdf).

**Examples, qualifications, and adjacent variants.** The append program
illustrates computed substitutions, not just yes/no refutation. The paper's
existential completeness of SLD refutations does not imply completeness of a
depth-first implementation that can remain forever on an infinite branch.
Finite failure is stronger than “no answer seen so far” [Apt--van Emden,
example after Corollary 5.3 and finite-failure sections](https://ir.cwi.nl/pub/10272/10272D.pdf).

**Reader-facing reconstruction owed.** Give an SLD derivation with variables
and mgus, prove soundness of its computed answer, state and outline the lifting
lemma, prove completeness for correct answers, and then draw distinct success,
finite-failure, and divergence trees. The fixed-point/model correspondence and
the operational theorem must be cross-referenced but not conflated.

### John W. Lloyd (1987)

**Identity and access.** John W. Lloyd, *Foundations of Logic Programming*,
second extended edition, Springer, 1987, XII + 212 pp.,
[DOI 10.1007/978-3-642-83189-8](https://doi.org/10.1007/978-3-642-83189-8).
The [Springer record](https://link.springer.com/book/10.1007/978-3-642-83189-8)
gives the authoritative edition and chapter pagination. A [University of Porto
Department of Computer Science-hosted scan of the corrected printing](https://www.dcc.fc.up.pt/~nam/resources/SLP21-/Foundations-of-Logic-Programming-%28Symbolic-Computation%29-by-John-W.-Lloyd-%28z-lib.org%29.pdf)
was inspected for the internal text; it is not a publisher-hosted copy.

**Locator, notation, and model classes.** Chapter 2, “Definite Programs,”
pp. 35--69, develops Herbrand/fixpoint semantics, SLD refutations, computed
answers, and computation-rule independence. Chapter 3, “Normal Programs,”
pp. 71--106, treats bodies containing positive and negative literals and
SLDNF-style execution. Chapters 4--5 broaden program statements and databases;
those broader classes must not be back-projected into the definite-program
theorems [Lloyd, authoritative contents](https://link.springer.com/book/10.1007/978-3-642-83189-8).

**Exact result strength.** In Chapter 2, Theorem 9.2 is computation-rule
independence; Theorem 9.3 identifies the `R`-success set with the least Herbrand
model; Theorem 9.4 gives an SLD refutation via any computation rule when a
definite program plus goal is unsatisfiable; and Theorem 9.5 gives strong
completeness for correct answers up to a further substitution. “Any computation
rule” means any atom-selection rule. It does not mean that any tree-search
strategy, especially depth-first Prolog search, finds the branch [Lloyd,
Chapter 2, §9, DOI edition](https://doi.org/10.1007/978-3-642-83189-8).

**Proof status and full outline boundary.** Theorem 9.2 is proved by the
switching lemma; Theorems 9.3--9.5 then strengthen the earlier soundness and
completeness results. The normal-program chapter develops SLDNF with additional
restrictions needed to avoid unsound treatment of nonground negative goals and
to relate execution to completion semantics. Printed pp. 84--89 define safe
selection and the ranked SLDNF refutation/finite-failure construction. Printed
pp. 88--90 distinguish admissible clauses, allowed clauses and goals, and the
allowedness of `P union {G}`; Proposition 15.1 then gives nonfloundering and
ground computed answers. Theorems 15.4 and 15.6 on printed pp. 92--94 give
finite-failure and computed-answer soundness without making allowedness a
soundness hypothesis. Theorem 16.3, printed pp. 98--101, gives completeness only
for hierarchical programs under allowedness and a safe computation rule
[Lloyd, institutional scan, Chapters 2--3](https://www.dcc.fc.up.pt/~nam/resources/SLP21-/Foundations-of-Logic-Programming-%28Symbolic-Computation%29-by-John-W.-Lloyd-%28z-lib.org%29.pdf).

**Examples, qualifications, and adjacent variants.** Lloyd's discussion of cut
and control shows that implementation features can destroy the completeness of
the pure logical procedure. Prolog's leftmost atom selection, clause order,
depth-first traversal, cut, arithmetic, and extra-logical predicates are not
all captured by the pure definite theorem. A standards-level description of
concrete Prolog behavior should use [ISO/IEC 13211-1](https://www.iso.org/standard/21413.html)
as an adjacent authoritative source, never as a replacement for the SLD proof.

**Access qualification and reader-facing reconstruction owed.** The official
Springer record exposes the edition and chapter ranges but not the body in open
HTML. The internal locators and exact SLDNF side conditions above were checked
in the institutionally hosted corrected-printing scan, not a publisher-hosted
copy. The mathematical locator gap is closed with that provenance qualification;
direct quotation from a publisher copy remains open. The reconstruction must
keep four layers visibly separate: declarative least-model semantics, SLD atom
selection, complete-tree search, and actual Prolog control; it must include a
floundering example and a depth-first divergence counterexample.

**Reader-facing delivery status, 2026-08-22.** The presentation now supplies
the two-mode append calculation; separates atom selection, clause choice, and
tree traversal; proves the least-model theorem and its finite proof-tree form;
works an SLD refutation with fresh variants and mgus; reconstructs soundness,
lifting, correct-answer completeness, switching, and the depth-first starvation
counterexample; prints completion beside a finite failed tree; and separates
negative success, negative failure, divergence, and floundering before stating
the exact allowedness, safeness, and hierarchical-program boundaries. This
closes the reader-facing reconstruction owed by `N-c-022`. The Lloyd theorem
locators retain the institutional-scan provenance above, and direct quotation
from a publisher copy remains open; this row's completion does not freeze Part
IX.

## `N-c-023` — stable models and answer-set programming

### Michael Gelfond and Vladimir Lifschitz (1988)

**Identity and access.** Michael Gelfond and Vladimir Lifschitz, “The Stable
Model Semantics for Logic Programming,” *Proceedings of the Joint International
Conference and Symposium on Logic Programming*, MIT Press, 1988,
pp. 1070--1080, ISBN 0-262-61056-6. No DOI was located for the original paper;
the [official proceedings index](https://www.sigmod.org/publications/dblp/db/conf/iclp/iclp88.html)
confirms its identity and pages. Lifschitz's
[live first-party publications page](https://www.cs.utexas.edu/~vl/papers-old.html)
identifies the same paper and links the former author-hosted file
`http://www.cs.utexas.edu/users/vl/mypapers/stable.ps`; that live file now
returns 404. The Internet Archive retains an
[archived capture of that exact first-party URL](https://web.archive.org/web/20030331145308id_/http://www.cs.utexas.edu:80/users/vl/mypapers/stable.ps),
timestamped 2003-03-31. The captured PostScript is 98,568 bytes with SHA-256
`27425678580AC9A1A3E6D460C200586B658B621B3285810AE0CE001697719DF5`.
It converts to a complete eleven-page author copy, and every page was rendered
and inspected. The authors' later
[primary retrospective on stable-model definitions](https://www.cs.utexas.edu/~vl/papers/12defs.pdf)
remains independent corroboration rather than a substitute.

**Locator, notation, and standing.** Section 5, printed p. 43, of Lifschitz's
author-hosted 2008 retrospective labels the original construction Definition C.
For a ground normal program `P` and a set `M` of atoms, the
Gelfond--Lifschitz reduct `P^M` is obtained in two steps:
delete every rule having a default-negated body atom `not A` with `A in M`, then
erase all remaining default-negated body literals. The result is a definite
positive program. `M` is stable exactly when it is the least model of `P^M`.
Here `M` is a candidate interpretation, `P^M` is a program derived relative to
that candidate, and stability is a property of the candidate; none is an SLD
search state [Gelfond--Lifschitz definition as documented by the authors](https://www.cs.utexas.edu/~vl/papers/12defs.pdf).

**System, hypotheses, and exact strength.** The original definition is for
ground normal rules with default negation; a nonground program is handled
through all of its ground instances. The paper explicitly permits an infinite
grounding when function symbols make the Herbrand universe infinite. A program
may have no stable set, one, or several. The source first calls the fixed points
`stable sets`; after Theorem 1 proves that every such set is a minimal Herbrand
model, it licenses `stable model` as a synonym. It reserves the phrase “the
stable model semantics is defined for P” for the unique-stable-model case,
where that model is selected as canonical. Later ASP usage broadens the phrase
to the candidate relation even when there are zero or many stable models; the
reduct itself is unchanged. Positive definite programs are the adjacent special
case: their reduct is the program itself and the unique stable model is their
least Herbrand model. Disjunctive heads, strong negation, first-order stable
models, and modern ASP aggregates require later definitions
[Gelfond--Lifschitz, Sections 2--3, author copy](https://web.archive.org/web/20030331145308id_/http://www.cs.utexas.edu:80/users/vl/mypapers/stable.ps)
and [authors' retrospective, Section 5](https://www.cs.utexas.edu/~vl/papers/12defs.pdf).

**Proof status and acquisition boundary.** The complete author copy is
**ACQUIRED AND INSPECTED**. Section 2 gives the reduct, states Theorem 1
(stable sets are minimal Herbrand models), and supplies its proof. Section 3
gives a nonstratified unique-model calculation, the no-model rule
`p <- not p`, and the two-model program `p <- not q; q <- not p`. Section 4
states Theorem 2 with explicit attribution to Van Gelder--Ross--Schlipf,
derives the locally-stratified/perfect-model and stratified/iterated-fixed-point
corollaries, defines the autoepistemic translation, and proves Theorem 3 through
the displayed stable-expansion lemma. The original content, theorem numbering,
and supplied proofs are closed against this primary author presentation. A
publisher proceedings facsimile was not inspected, so do not call the author
copy a publisher scan or assert publisher-specific typography/page markings.
The later NP classification still must not be attributed to the 1988 paper.

**Examples, counterexamples, and adjacent variants.** The program
`p <- not q; q <- not p` has the two stable models `{p}` and `{q}`; checking
each candidate requires computing a different reduct. The self-defeating rule
`p <- not p` has no stable model. These examples establish nonuniqueness and
nonexistence directly from the reduct definition. The separate positive loop
`p <- p` has only the empty stable model, while its Clark completion `p iff p`
has both classical interpretations; this is the needed direct witness that
stable semantics is not completion plus ordinary model selection.

**Reader-facing reconstruction owed.** Define ground normal rules and default
negation, print the two-step reduct algorithm, calculate all candidates for one
two-model and one no-model program, prove that positive definite programs
recover their least model, reconstruct Theorem 1's minimality argument, and
state the source's narrower original use of “the stable model semantics.”
Then record the well-founded/perfect/iterated-fixed-point comparisons and type
the autoepistemic translation before stating Theorem 3 and its proof lemma.
Do not import the later complexity results into the 1988 source role.

### Victor W. Marek and Mirosław Truszczyński (1999)

**Identity and access.** Victor W. Marek and Mirosław Truszczyński, “Stable
Models and an Alternative Logic Programming Paradigm,” in K. R. Apt et al.
(eds.), *The Logic Programming Paradigm: A 25-Year Perspective*, Springer,
1999, pp. 375--398,
[DOI 10.1007/978-3-642-60085-2_17](https://doi.org/10.1007/978-3-642-60085-2_17).
Use the [author-hosted primary PDF](https://cs.uky.edu/~marek/papers.dir/00.dir/alternative.pdf)
and the identical [arXiv manuscript](https://arxiv.org/abs/cs/9809032).

**Locator, notation, and standing.** Sections 2--4 restrict the programming
language to function-free stable logic programs and treat clauses as
constraints whose stable models encode solutions. The extensional database
`edb_Pi(I)` encodes a problem instance `I`; a fixed intensional program `P_Pi`
expresses the problem; a map `sol^I_Pi` decodes each stable model into a
solution. This triple is a uniform representation scheme, not a claim that the
stable model itself is literally the input structure [Marek--Truszczyński,
sections 2--5](https://cs.uky.edu/~marek/papers.dir/00.dir/alternative.pdf).

**Model class, hypotheses, and exact strength.** Function symbols are excluded,
so grounding is finite. Theorem 5.2 states that a decision problem is solvable
by a uniform stable-logic-program representation exactly when it is in NP.
The theorem concerns the authors' uniform encoding and function-free syntax;
it is not a blanket data-complexity statement about arbitrary ASP extensions
and not a claim that enumerating all stable models is polynomial [Marek--Truszczyński,
Theorem 5.2 and surrounding definition](https://cs.uky.edu/~marek/papers.dir/00.dir/alternative.pdf).

**Proof status and full outline boundary.** For the NP upper direction, a
candidate stable model/solution is polynomially checkable for the finite
grounded normal program. For the representation direction, the construction
uses nondeterministic stable choices together with constraints that eliminate
guesses failing the polynomial verifier. The paper cites an earlier proof for
the strengthened theorem and explains the construction methodology; the
handbook should reproduce one encoding and the two complexity directions but
may cite the general translation details [Marek--Truszczyński, section 5](https://cs.uky.edu/~marek/papers.dir/00.dir/alternative.pdf).

**Examples, qualifications, and adjacent variants.** Graph and combinatorial
search examples illustrate stable models as solutions. The authors explicitly
contrast this constraint-oriented style with Horn least-model programming and
note the expressive cost of removing function symbols. Their “well-attuned to
NP” thesis must not be generalized to disjunctive ASP, whose existence problem
rises to the second level of the polynomial hierarchy [Marek--Truszczyński,
sections 5--7 and conclusion](https://cs.uky.edu/~marek/papers.dir/00.dir/alternative.pdf).

**Reader-facing reconstruction owed.** Give one fixed function-free program
plus varying database facts, prove the one-to-one solution decoding for a small
instance, and outline both directions of Theorem 5.2. Make grounding size and
the fixed-program/unbounded-input division explicit.

### Gerhard Brewka, Thomas Eiter, and Mirosław Truszczyński (2011)

**Identity and access.** Gerhard Brewka, Thomas Eiter, and Mirosław
Truszczyński, “Answer Set Programming at a Glance,” *Communications of the ACM*
54(12), 2011, pp. 92--103,
[DOI 10.1145/2043174.2043195](https://doi.org/10.1145/2043174.2043195). The
[TU Wien institutional record](https://repositum.tuwien.at/handle/20.500.12708/162700)
confirms identity and pagination; an [accessible article copy](https://www.researchgate.net/publication/220421804_Answer_Set_Programming_at_a_Glance)
contains the technical overview.

**Locator, notation, and standing.** Printed pp. 93--97 distinguish default
negation `not a` from explicit/strong negation and extend rule syntax to
disjunctive heads. For a candidate set `M`, default negation is eliminated by a
reduct. In the normal case the reduct has a least model; in the disjunctive case
it can have several minimal models, and `M` is an answer set when it is an
appropriate minimal model of its reduct. Thus “answer set” is the modern
programming name for the selected stable-model object in the specified
language, not every model of the rules [Brewka--Eiter--Truszczyński, printed
pp. 93--97](https://www.researchgate.net/publication/220421804_Answer_Set_Programming_at_a_Glance).

**Model classes and exact complexity strength.** For finite propositional
normal programs, deciding whether some answer set exists is NP-complete. With
disjunctive rule heads, existence is complete for `NP^NP`/the second
existential level of the polynomial hierarchy. Nonground predicate programs
can incur an exponential grounding increase. These claims have different
syntax and input-size assumptions and must occupy separate rows [the article's
“Complexity of ASP” sidebar, printed p. 97](https://www.researchgate.net/publication/220421804_Answer_Set_Programming_at_a_Glance).

**Proof status and full outline boundary.** This is an authoritative overview,
not the primary proof of each complexity theorem. It explains the membership
intuition through candidate generation and reduct checking and cites the
hardness/expressiveness literature. A full handbook outline may show NP
membership for finite propositional normal programs and give a concrete SAT or
graph reduction, but the disjunctive second-level result should remain a cited
theorem unless its quantified reduction is actually reconstructed [Brewka--Eiter--Truszczyński,
complexity sidebar and references](https://www.researchgate.net/publication/220421804_Answer_Set_Programming_at_a_Glance).

**Examples, qualifications, and adjacent variants.** The overview organizes
ASP modeling around generating candidates, defining auxiliary relations, and
testing constraints. Strong negation and head disjunction are not cosmetic:
they change semantics or expressive/complexity strength. The register excludes
solver ecosystems, so brand lists, architecture comparisons, and deployment
claims are outside this presentation even though the survey discusses them
[Brewka--Eiter--Truszczyński, printed pp. 97--102](https://www.researchgate.net/publication/220421804_Answer_Set_Programming_at_a_Glance).

**Reader-facing reconstruction owed.** Extend the normal-rule definition only
after the Gelfond--Lifschitz base case; distinguish default from strong
negation; work one generate/define/test encoding; and give a complexity table
whose rows separately state normal propositional, disjunctive propositional,
and nonground cases. End before solver implementation material.

**Reader-facing delivery status, 2026-08-22.** The presentation now types the
ground rules, candidate atom set, reduct, and candidate-dependent least-model
map; calculates all candidates for the two-model and no-model examples; proves
the positive-program special case, antimonotonicity, ordinary-model soundness,
original Theorem 1's minimality conclusion, and the strict difference from
Clark completion. It preserves the source's stable-set/stable-model terminology
and narrower original canonical-model convention; records Theorem 2 and its two
corollaries at their attributed strength; and defines the autoepistemic
translation before reconstructing Theorem 3's proof lemma. It then gives a
fixed function-free three-coloring program,
computes a concrete two-vertex reduct, proves the stable-model/coloring
bijection, separates fixed-program data size from variable-program grounding
size, and outlines both directions and the search-problem limit of Theorem 5.2.
Finally it defines the strong-negation and disjunctive extensions at their own
strength, proves the normal existence/credulous/skeptical bounds, and leaves the
disjunctive second-level hardness as a cited result. This closes the
reader-facing reconstruction owed by `N-c-023` against the acquired author
copy. The publisher proceedings presentation remains uninspected, and other
Part IX source gaps remain open, so Part IX is not frozen.

## `N-c-024` — conjunctive queries and Datalog

### Ashok K. Chandra and Philip M. Merlin (1977)

**Identity and access.** Ashok K. Chandra and Philip M. Merlin, “Optimal
Implementation of Conjunctive Queries in Relational Data Bases,” *Proceedings
of the Ninth Annual ACM Symposium on Theory of Computing*, ACM, 1977,
pp. 77--90, [DOI 10.1145/800105.803397](https://doi.org/10.1145/800105.803397);
use the [accessible primary paper](https://www.cs.ubc.ca/~laks/cpsc504/chandra-merlin-1977.pdf).

**Locator, notation, and standing.** Printed pp. 78--82 define a conjunctive
query as an existentially quantified conjunction of relational atoms, with
distinguished output variables, and associate to it a canonical database/
finite relational structure. A homomorphism maps query variables/constants in
a way that preserves every relational atom and fixes the distinguished output
positions. A query, its canonical database, and a homomorphism between canonical
databases are different kinds of object [Chandra--Merlin, definitions on
printed pp. 78--82](https://www.cs.ubc.ca/~laks/cpsc504/chandra-merlin-1977.pdf).

**Model class, hypotheses, and exact strength.** Over finite relational
databases and conjunctive queries with compatible heads, `q1` is contained in
`q2`---that is, `q1(D) subseteq q2(D)` for every database `D`---iff there is a
head-respecting homomorphism **from the canonical structure of `q2` to that of
`q1`**. Equivalence is homomorphism in both directions. The paper also proves
NP-completeness of conjunctive-query evaluation in combined input and obtains a
unique minimal equivalent form up to isomorphism through folding [Chandra--Merlin,
main theorems, printed pp. 82--89](https://www.cs.ubc.ca/~laks/cpsc504/chandra-merlin-1977.pdf).

**Proof status and full outline boundary.** For the containment theorem, one
direction composes a valuation witnessing `q1` with a homomorphism from `q2`;
the converse evaluates `q2` on the canonical database of `q1` and reads the
witnessing assignment as a homomorphism. This canonical-instance step is the
essential reverse direction and must appear in a full proof outline. The
complexity proof reduces a finite combinatorial problem to query evaluation;
the minimization proof uses endomorphisms/foldings and mutual homomorphisms
[Chandra--Merlin, printed pp. 82--89](https://www.cs.ubc.ca/~laks/cpsc504/chandra-merlin-1977.pdf).

**Examples, counterexamples, and adjacent variants.** A two-edge path query
maps homomorphically into a query with a duplicated redundant atom, explaining
equivalence/minimization. Reversing the homomorphism direction gives the wrong
containment assertion; a one-edge versus two-edge path database supplies a
small counterexample. The theorem does not cover negation, inequality,
aggregation, recursion, or arbitrary first-order formulas [Chandra--Merlin,
query examples and theorem hypotheses](https://www.cs.ubc.ca/~laks/cpsc504/chandra-merlin-1977.pdf).

**Reader-facing reconstruction owed.** Define CQ syntax and answer semantics,
construct the canonical database of one Boolean and one non-Boolean query,
state containment with quantification over all databases, prove both directions
of the homomorphism theorem, and work a minimization example. Print the
contravariant homomorphism direction in words as well as symbols.

### Moshe Y. Vardi (1982)

**Identity and access.** Moshe Y. Vardi, “The Complexity of Relational Query
Languages (Extended Abstract),” *Proceedings of the Fourteenth Annual ACM
Symposium on Theory of Computing*, ACM, 1982, pp. 137--146,
[DOI 10.1145/800070.802186](https://doi.org/10.1145/800070.802186); use the
[author-uploaded full text](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract),
whose public record identifies Vardi as the uploader. The [author's publication
index](https://www.cs.rice.edu/~vardi/papers/index.html) lists the paper, but
its former direct `stoc82.pdf` link returned HTTP 404 on 2026-08-22 and is no
longer used as the access claim.

**Locator, notation, and standing.** The introduction, printed pp. 137--139,
defines three complexity measures. Data complexity fixes a query expression and
varies the database; expression complexity fixes a database and varies the
query expression; combined complexity varies both and measures their combined
size. These are metalinguistic input measures for evaluation problems, not
three query languages or three semantic notions of answer [Vardi, printed pp.
137--139](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract).

**Languages, hypotheses, and exact strength.** Vardi compares relational
calculus and extensions by transitive closure, fixpoint, and existential
second-order quantification with relational algebra and loop extensions. The
paper proves completeness classifications under both data and expression
measures and observes that, for the languages studied, expression complexity is
one exponential above data complexity; combined complexity is sufficiently
close to expression complexity that the paper concentrates on the two named
measures [Vardi, abstract and theorem tables](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract).

**Proof status and full outline boundary.** Membership arguments evaluate a
fixed operator language within the relevant resource bound; hardness arguments
encode machine configurations or complete problems into a fixed database or a
varying expression as appropriate. The extended abstract does not justify
copying a class label without its fixed/varying input convention. A handbook
proof outline must explicitly identify which component carries the reduction
and why its size remains fixed in a data-complexity lower bound [Vardi, theorem
development on printed pp. 139--146](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract).

**Examples, qualifications, and adjacent variants.** The same evaluation task
can be easy in data complexity and much harder in expression/combined
complexity because fixing a query removes its unbounded syntax from the input.
The distinctions apply to CQ and Datalog presentations but their exact class
labels must come from a theorem for the respective language. “Query complexity”
without a measure is therefore incomplete [Vardi, introduction and conclusion](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract).

**Reader-facing reconstruction owed.** Give one evaluation relation
`Eval(q,D,a)` and derive its three input conventions in a table. For CQ, state
fixed-query data complexity separately from NP-complete combined evaluation;
for Datalog, state fixed-program data complexity separately from the combined
problem. Every theorem label must say what is fixed.

### Serge Abiteboul, Richard Hull, and Victor Vianu (1995)

**Identity and access.** Serge Abiteboul, Richard Hull, and Victor Vianu,
*Foundations of Databases*, Addison-Wesley, 1995, ISBN 0-201-53771-0. No DOI was
located for the book. The [author's course page](https://abiteboul.com/TEACHING/DBCOURSE/)
links an author-authorized complete PDF; the [book's detailed DBLP contents](https://www.sigmod.org/publications/dblp/db/books/dbtext/abiteboul95.html)
supplies a stable chapter index. The technical locators below refer to the
[accessible complete scan](https://wiki.epfl.ch/provenance2011/documents/foundations%20of%20databases-abiteboul-1995.pdf).

**Locator, notation, and model classes.** Chapter 4, printed pp. 37--69, defines
conjunctive queries. Chapter 6 develops homomorphisms and query comparison;
Theorem 6.2.3 is on printed p. 118. Part D, especially Chapter 12 from printed
p. 275, defines function-free Datalog rules, proof/model/fixpoint semantics, and
bottom-up evaluation. Chapter 16 from printed p. 423 defines data complexity
and provides complexity tables [Abiteboul--Hull--Vianu, full contents and cited
pages](https://wiki.epfl.ch/provenance2011/documents/foundations%20of%20databases-abiteboul-1995.pdf).

**Exact CQ result strength.** Theorem 6.2.3 states `q subseteq q'` iff there is
a head-respecting homomorphism from `q'` to `q`. Its proof gives both the
homomorphism-composition direction and the canonical-instance converse.
Theorem 6.2.10 states NP-completeness of CQ containment and equivalence. These
results are for the book's finite relational CQ setting; adding comparisons,
negation, or dependencies changes the problem [Abiteboul--Hull--Vianu,
Theorems 6.2.3 and 6.2.10](https://wiki.epfl.ch/provenance2011/documents/foundations%20of%20databases-abiteboul-1995.pdf).

**Exact Datalog result strength.** A positive Datalog program has a monotone
immediate-consequence operator on the finite set of possible ground facts; its
least fixed point, least model, proof-tree semantics, and bottom-up evaluation
coincide. Fixed-program data complexity is polynomial-time (and the language's
data-evaluation problem is P-complete), while combined evaluation is
EXPTIME-complete under the book's conventions. General Datalog-query
containment is undecidable, in sharp contrast with CQ containment [Abiteboul--Hull--Vianu,
Chapters 12--13 and 16](https://wiki.epfl.ch/provenance2011/documents/foundations%20of%20databases-abiteboul-1995.pdf).

**Proof status and full outline boundary.** The book flags many arguments as a
“crux”: enough structure and intuition are supplied to locate the proof, while
some routine or lengthy details are omitted. A handbook must not relabel such a
source sketch as a fully reproduced proof. For Datalog it should prove
monotonicity, finite convergence, and the model/fixpoint equality locally; the
P/EXPTIME hardness reductions and undecidable containment reduction can remain
cited if their constructions are stated precisely [Abiteboul--Hull--Vianu,
proof conventions and Chapters 12--16](https://wiki.epfl.ch/provenance2011/documents/foundations%20of%20databases-abiteboul-1995.pdf).

**Examples, qualifications, and adjacent variants.** Transitive closure is the
canonical recursive Datalog example and is not expressible by an ordinary CQ.
A CQ is essentially a one-rule, nonrecursive positive query, but Datalog's
recursion changes evaluation and containment. The book uses “data complexity”
at printed p. 423; Vardi is the source for the explicit three-way data/
expression/combined taxonomy and should remain cited for that terminology
[Abiteboul--Hull--Vianu, Chapters 4, 12, and 16](https://wiki.epfl.ch/provenance2011/documents/foundations%20of%20databases-abiteboul-1995.pdf).

**Reader-facing reconstruction owed.** Follow the CQ homomorphism proof with a
new Datalog subsection: define safe function-free rules, the extensional/
intensional split, grounding, and `T_P`; compute transitive closure to its fixed
point; prove the four-way semantic coincidence; and print an evaluation/
containment table in which CQ and Datalog remain separate. State which book
proofs are reproduced and which are source sketches.

**Reader-facing delivery status, 2026-08-22.** The presentation now defines CQ
syntax and answer semantics; constructs Boolean and non-Boolean canonical
databases; proves evaluation by homomorphism and both directions of the
contravariant containment theorem; gives a one-edge/two-edge direction check;
and reconstructs retraction, core minimization, and uniqueness up to
isomorphism. It types Vardi's three input measures and locally proves fixed-CQ
`AC^0`, expression/combined NP-completeness, and containment NP-completeness.
The Datalog subsection defines the extensional/intensional split, active-domain
grounding, and the reused immediate-consequence operator; calculates every
stage of a transitive closure; proves its nondefinability by one CQ and the
four-way bottom-up/proof/fixed-point/model coincidence; and derives the
fixed-data upper bound and fixed-program monotone-circuit lower bound. A final
table keeps CQ evaluation, CQ containment, Datalog evaluation, and Datalog
containment separate. The combined EXPTIME-hardness and undecidable-containment
reductions remain cited at the book's declared crux boundary. This closes the
reader-facing reconstruction owed by `N-c-024`; Part IX is not frozen.

## `N-c-025` — finite-template CSPs and the dichotomy pointer

### Tomás Feder and Moshe Y. Vardi (1998)

**Identity and access.** Tomás Feder and Moshe Y. Vardi, “The Computational
Structure of Monotone Monadic SNP and Constraint Satisfaction: A Study through
Datalog and Group Theory,” *SIAM Journal on Computing* 28(1), 1998,
pp. 57--104,
[DOI 10.1137/S0097539794266766](https://doi.org/10.1137/S0097539794266766).
The [publisher record and abstract](https://epubs.siam.org/doi/10.1137/S0097539794266766)
were inspected directly. Feder's live
[Stanford publications page](https://theory.stanford.edu/~tomas/) links the
journal item to a complete first-party
[PostScript manuscript](https://theory.stanford.edu/~tomas/constraint.ps).
The retrieved 53-page file is 486,897 bytes and has SHA-256
`0808A6E91B49465838F0D4D7C5124656493A0BF2515F7478E014FB2F254F798C`.
Its title page bears the full journal title, and its Theorems 5--6 and complete
proofs were inspected on author-copy pp. 10--13. It is an author-hosted
complete manuscript, not a SIAM facsimile; SIAM-specific proof pagination and
typesetting remain open. Vardi's older
[full-version link](https://www.cs.rice.edu/~vardi/papers/stoc93rj.pdf) remains
dead and has different indexed numbering; it no longer controls the accessible
author-copy locators. The [official ACM record](https://doi.org/10.1145/167088.167245)
separately confirms the 1993 conference presentation.

**Locator, notation, and standing.** A nonuniform CSP fixes a finite relational
template `B`; an input finite relational structure `A` is accepted exactly
when there is a homomorphism `h:A -> B`. Thus `A` is the varying instance, `B`
the fixed template, and `h` the solution certificate. MMSNP is instead a
sentence fragment and associated problem class. In an equality-free normal
form its sentences are
`exists M forall x conjunction_i not(alpha_i(sigma,x) and beta_i(M,x))`,
where the existential predicates `M` are unary, `alpha_i` is a conjunction of
positive input-signature atoms, and `beta_i` is a conjunction of positive or
negative `M`-literals. A fixed sentence defines the language of finite input
structures satisfying it. This exact standing and syntax are directly readable
in [Madelaine--Stewart, Definition 3.1, printed p. 8](https://www.lix.polytechnique.fr/~madelaine/Download/SicompFinal.pdf).

**Model class, hypotheses, and exact strength.** Every fixed-template finite CSP
is MMSNP-definable, but some MMSNP languages are not literally fixed-template
CSP languages. For every MMSNP problem `Omega`, however, there is a CSP problem
`Omega'` such that:

- `Omega -> Omega'` is a deterministic polynomial-time Karp reduction; and
- `Omega' -> Omega` is a randomized polynomial-time Turing reduction.

For connected inputs to `Omega'`, the reverse reduction can be a
**randomized Karp reduction**; the general disconnected input is handled
component by component. This is problem-by-problem computational equivalence,
not equality of the two extensional classes. The formal orientation is
corroborated by [Kolaitis--Vardi, Theorem 1.8, printed p. 17](https://www.cs.rice.edu/~vardi/papers/ircsmv7.pdf)
and [Madelaine--Stewart, Theorem 3.2, printed p. 8](https://www.lix.polytechnique.fr/~madelaine/Download/SicompFinal.pdf).
The article's abstract explicitly says it **does not achieve** the desired
dichotomy, so this theorem is not a proof that every fixed-template CSP is in
P or NP-complete.

**Proof content and source boundary.** Complete author-copy proof content is
**CLOSED**. Theorem 5, author-copy pp. 10--11, defines relational girth by the
condition that at most `k` relation occurrences of arities `r_i` mention at
least `1 + sum_i(r_i-1)` elements. It makes `N=n^s` copies of each input
element, independently retains each lifted `r`-ary occurrence with probability
`N^(1-r+epsilon)`, deletes one occurrence from every short cycle, and uses
Markov's inequality to bound those deletions. Projection gives `S' -> S`; for
the converse, majority image classes of size at least `N/d`, a Cherno bound,
and a union bound over all relevant subset choices ensure that the majority
values define `S -> T` for every template of size at most `d`. The source
explicitly leaves derandomization open.

Theorem 6, author-copy pp. 12--13, first decomposes forbidden conjunctions into
source-defined biconnected components using existential zero-ary truth choices
for disconnected pieces and unary predicates for a single articulation
variable. It closes the formula under variable identifications and handles
repeated-argument atoms. It then replaces each conjunction `C` of input atoms
by a fresh input relation `R_C` on all distinct variables of the entire
forbidden conjunction, with closure for sub-conjunctions. Direct
expansion can create implicit `R_C` occurrences; Theorem 5 supplies high
relational girth, and biconnectedness forces each such forbidden occurrence
inside one explicit relation occurrence. Finally, allowed monadic truth types
form a finite template. Zero-ary choices give finitely many templates whose
disjoint union is separated by a new binary relation; connected inputs land in
one component, while arbitrary inputs are handled componentwise. This proves
the exact deterministic-Karp and randomized-Karp/Turing orientations.

Only comparison with the final SIAM typesetting and its proof pagination stays
**OPEN**. The directly inspected Madelaine--Stewart paper also has an internal
source-critical defect: the parenthesis after Theorem 1.1 on printed p. 2
reverses the reductions, whereas its explicitly more detailed Theorem 3.2
agrees with Feder--Vardi Theorem 6 and Kolaitis--Vardi. Use Theorem 3.2, not
that parenthesis.

**Examples, qualifications, and adjacent variants.** Fixed graph
`H`-colorability is the graph-homomorphism special case: the input graph maps to
the fixed graph `H`. Ordinary `k`-colorability fixes `H=K_k`. Triangle-freeness
is MMSNP-definable but is not `CSP(H)` for any finite graph `H`, giving a
concrete literal-nonidentity witness. Allowing the template to vary produces
the uniform/general CSP and changes the input problem; infinite-domain,
counting, optimization, and promise CSPs are outside the stated dichotomy.

**Reader-facing reconstruction required and now delivered.** Define finite
relational structures and homomorphisms, express one binary-relation CSP both
as constraints and as `A -> B`, and identify which structure is fixed. Define
MMSNP before use and state its standing and nonidentity with CSP. Reconstruct
the exact arity-sensitive relational-girth condition, Theorem 5's copied
structure and Markov/Cherno/majority proof, and Theorem 6's biconnected
normalization, relation replacement, hidden-occurrence obstruction,
high-girth repair, and finite-template construction. Give the exact asymmetric
reductions, retain `randomized` in the connected-input refinement, and
attribute Kun's later deterministic construction separately. Keep the 1998
conjectural program distinct from both 2017 dichotomy proofs.

### Andrei A. Bulatov (2017)

**Identity and access.** Andrei A. Bulatov, “A Dichotomy Theorem for
Nonuniform CSPs,” *58th Annual IEEE Symposium on Foundations of Computer
Science*, 2017, pp. 319--330,
[DOI 10.1109/FOCS.2017.37](https://doi.org/10.1109/FOCS.2017.37). Use the
[author-hosted FOCS paper](https://www.cs.sfu.ca/~abulatov/papers/focs17.pdf);
the author's [long 2017 manuscript](https://www2.cs.sfu.ca/~abulatov/papers/dichotomy.pdf)
contains the expanded proof.

**Locator, notation, and standing.** Section 2 defines a finite constraint
language `Gamma` as finitely many finitary relations over a fixed finite domain
`A`; `CSP(Gamma)` asks whether a finite conjunction of constraints using those
relations has a satisfying assignment. A polymorphism is an operation on `A`
that preserves every relation in `Gamma`. A weak near-unanimity operation `w`
is idempotent and gives the same value for all tuples having one `y` and all
other coordinates `x`; it is an algebraic operation preserving the template,
not a new constraint instance [Bulatov, section 2](https://www.cs.sfu.ca/~abulatov/papers/focs17.pdf).

**Model class, hypotheses, and exact strength.** Theorem 1 states that for every
finite constraint language over a finite set, `CSP(Gamma)` is solvable in
polynomial time or is NP-complete. After core and singleton-relation reductions,
Theorem 4 gives the algebraic criterion in terms of an associated finite
idempotent algebra: the tractable side has a weak-near-unanimity term operation,
while absence of such an operation gives NP-completeness. The result is
nonuniform and finite-domain [Bulatov, Theorems 1 and
4](https://www.cs.sfu.ca/~abulatov/papers/focs17.pdf). The theorem's further
equivalent algebraic clause is not used as an undefined shorthand in the
handbook presentation.

**Proof status and full outline boundary.** The hardness direction under
failure of the algebraic condition was established by earlier algebraic CSP
work; Bulatov identifies the main new achievement as a polynomial-time
algorithm for templates satisfying the tractability condition. The 12-page
FOCS version states the reductions, structural alternatives, and algorithmic
spine but necessarily delegates extensive lemmas to the full version. The
handbook row calls for a pointer only: state the criterion and independent proof
status, then cite the expanded manuscript rather than pretending to reproduce
the dichotomy proof [Bulatov, introduction and proof overview](https://www.cs.sfu.ca/~abulatov/papers/focs17.pdf).

**Examples, qualifications, and adjacent variants.** Boolean SAT fragments and
fixed graph-homomorphism problems are finite-template cases, but the theorem
does not classify counting CSPs, approximation, promise CSPs, or arbitrary
infinite templates. “Has a WNU polymorphism” must be evaluated after the source's
core/idempotent normalization; dropping that bridge produces a misleading
criterion [Bulatov, section 2 and Theorem 4](https://www.cs.sfu.ca/~abulatov/papers/focs17.pdf).

**Reader-facing reconstruction owed.** Define finite constraint language,
instance, polymorphism, core reduction, singleton expansion, and WNU at the
point of use. State the dichotomy and criterion, explain the prior-hardness/
new-algorithm division, and stop at a labelled citation boundary. No unnamed
algebraic intermediate object should be invented to make the pointer look like
a local proof.

### Dmitriy Zhuk (2017)

**Identity and access.** Dmitriy Zhuk, “A Proof of CSP Dichotomy Conjecture,”
*58th Annual IEEE Symposium on Foundations of Computer Science*, 2017,
pp. 331--342,
[DOI 10.1109/FOCS.2017.38](https://doi.org/10.1109/FOCS.2017.38). Use the
[official IEEE FOCS PDF](https://ieee-focs.org/FOCS-2017-Papers/3464a331.pdf)
and the [author's full arXiv version](https://arxiv.org/abs/1704.01914).

**Locator, notation, and standing.** Section I, printed pp. 331--332, defines
finite-domain constraint languages and their endomorphisms. Theorem 1 gives the
core reduction; Theorem 2 gives the singleton-unary-relation reduction for a
core; and the paragraph preceding Conjecture 2 defines weak near-unanimity.
The WNU equations require idempotence and equality of all one-exception tuples;
they do not require the common value to equal the repeated argument in the way
a full near-unanimity operation would [Zhuk, Section I and Theorems 1--2](https://ieee-focs.org/FOCS-2017-Papers/3464a331.pdf).

**Model class, hypotheses, and exact strength.** For a finite constraint
language, after passing to the source's core/singleton-normalized form, the
existence of a WNU polymorphism places the CSP in polynomial time; otherwise it
is NP-complete. Theorem 3 records the previously known hard direction. Sections
III--IV give the new polynomial-time algorithm and its correctness obligations,
and Section VIII proves the main theorems stated in Section IV. This completes
the remaining direction independently of Bulatov [Zhuk, abstract, Theorems
1--3, and Sections III--IV and VIII](https://ieee-focs.org/FOCS-2017-Papers/3464a331.pdf).

**Proof status and full outline boundary.** The conference paper gives the
algorithm's principal reductions and correctness architecture, but explicitly
omits proofs of auxiliary statements and points to the longer version. A full
proof depends on a long algebraic analysis of progressively simplified
instances. The reader-facing row must therefore call this a theorem with an
external proof, explain that the tractable algorithm is the new direction, and
link the full version; a few WNU equations are not a proof of polynomial time
[Zhuk, conference paper proof overview and references to the full version](https://ieee-focs.org/FOCS-2017-Papers/3464a331.pdf).

**Examples, qualifications, and adjacent variants.** The paper includes a
finite-domain example over `Z_4` to illustrate the transformations used by the
algorithm. That example is not a universal normal form. Zhuk and Bulatov are
independent proofs of the same finite nonuniform dichotomy with substantially
different technical routes; neither should be described as a corollary of the
other [Zhuk, example and introduction](https://ieee-focs.org/FOCS-2017-Papers/3464a331.pdf).

**Reader-facing reconstruction owed.** Give one paragraph each for Feder--Vardi
conjecture, Bulatov proof, and Zhuk proof; state the identical finite-template
scope; define WNU once with a visible normalization caveat; and label both 2017
proofs as citation-only beyond the theorem/algorithm outline. The requested
presentation is a dichotomy pointer, not a compressed imitation of either long
proof.

**Reader-facing delivery status, 2026-08-22.** The presentation now defines a
finite relational signature, finite structures, homomorphisms, fixed-template
`CSP(B)`, finite constraint languages, and the exact translation between a
constraint instance and a homomorphism `A_I -> B_Gamma`. It calculates one
binary `K_2` path instance in both notations and turns it into a negative
triangle instance. It now also defines MMSNP in equality-free normal form,
states its standing as a sentence/problem class, constructs the fixed-template
coloring translation, and uses triangle-freeness to separate literal class
membership from computational equivalence. It gives Feder--Vardi's exact
deterministic-Karp and randomized-Turing directions, preserves `randomized` in
the connected-input Karp refinement, and now reconstructs the complete
author-copy proofs of Theorems 5--6. The first proof defines relational girth
at exact source strength and gives the random-copy, cycle-deletion,
Markov/Cherno, and majority-map argument. The second gives the biconnected
normalization, variable-identification and repeated-argument preparations,
fresh-relation expansion, hidden-occurrence problem, high-girth repair, and
finite-template construction, including the zero-ary and connected-component
qualification. It then separates Kun's later deterministic finite-family
construction. The historical paragraph keeps the 1998 paper's unproved
dichotomy program separate from the two independent FOCS 2017 proofs.
The algebraic paragraph defines the image language, minimum-image core
reduction, singleton expansion, polymorphism, and WNU at their points of use;
proves why the singleton relations are exactly idempotence; and states the WNU
criterion only after both polynomial-equivalence normalizations. The final
paragraphs separate the previously known hard direction from each paper's new
polynomial-time algorithm and retain a labelled citation boundary around the
two long proofs. This closes the reader-facing reconstruction owed by
`N-c-025`; only the Feder--Vardi SIAM-typeset comparison remains source-open,
and Part IX is not frozen.

## `N-c-026` — SAT, quantified Boolean formulas, and modal complexity

### Stephen A. Cook (1971)

**Identity and access.** Stephen A. Cook, “The Complexity of Theorem-Proving
Procedures,” *Proceedings of the Third Annual ACM Symposium on Theory of
Computing*, ACM, 1971, pp. 151--158,
[DOI 10.1145/800157.805047](https://doi.org/10.1145/800157.805047). Use the
[ACM primary record](https://doi.org/10.1145/800157.805047), Cook's
[author publication page](https://www.cs.toronto.edu/~sacook/), and the
[accessible transcription of the primary paper](https://www.cs.cmu.edu/~15455/resources/Cook1971-complx-thm-proof.pdf).

**Locator, notation, and standing.** Printed pp. 151--153 define a query
machine and `P`-reducibility: a deterministic polynomial-time machine deciding
one language may ask an oracle whether strings belong to another. This is
polynomial-time Turing/oracle reducibility and may make multiple adaptive
queries. A recognition problem is a set of finite strings; a propositional
formula is the encoded oracle instance; the reduction is a computation between
the two [Cook, printed pp. 151--153](https://www.cs.cmu.edu/~15455/resources/Cook1971-complx-thm-proof.pdf).

**Machine class, hypotheses, and exact strength.** Theorem 1 states that every
set accepted by a nondeterministic Turing machine in polynomial time is
`P`-reducible to the set of propositional tautologies, with the target presented
through disjunctive-normal-form tautology. The construction builds, for input
`w`, a conjunctive formula `A(w)` satisfiable exactly when the machine has an
accepting computation; querying whether `not A(w)` is a DNF tautology decides
the source language [Cook, Theorem 1, printed pp. 153--156](https://www.cs.cmu.edu/~15455/resources/Cook1971-complx-thm-proof.pdf).

**Proof status and full outline boundary.** The proof fixes a polynomial time
bound, lays out a time-by-tape-position computation tableau, introduces Boolean
variables for tape symbols, state, and head position, and conjoins clauses
requiring a well-formed initial configuration, exactly one local symbol/state,
legal adjacent transitions, and an accepting configuration. Every accepting
computation yields a satisfying assignment and every satisfying assignment
decodes to an accepting computation. A full handbook proof must also count the
variables/clauses and show the mapping is polynomial-time computable [Cook,
printed pp. 153--156](https://www.cs.cmu.edu/~15455/resources/Cook1971-complx-thm-proof.pdf).

**Qualifications and relation to the modern theorem.** The tableau itself gives
a polynomial many-one map `w -> A(w)` to SAT once the target is stated that way,
but Cook's paper defines and advertises the broader oracle/query reduction to
tautology. The handbook must display that historical reduction notion before
giving the modern many-one SAT formulation. SAT membership in NP is a separate
witness-checking argument [Cook, definitions and Theorem 1](https://www.cs.cmu.edu/~15455/resources/Cook1971-complx-thm-proof.pdf).

**Independent attribution and reader-facing reconstruction.** Levin's primary
1973 paper, “Universal Sequential Search Problems,” is identified by the
[Math-Net journal record and full text](https://www.mathnet.ru/eng/ppi914), with
Russian pp. 115--116 and English-translation pp. 265--266. Its abstract states
the universal sequential-search result. This supplies the independently cited
Levin source for the compound historical name; the handbook's technical proof
still comes from the explicit modern many-one formulation rather than being
silently reconstructed from the two-page Russian note. For Cook's part, define
both reduction notions, reconstruct the tableau in enough detail to prove size
and correctness, state SAT NP-membership, and explain how negation changes
satisfiability to DNF tautology. Do not call Cook's original reduction many-one
without the explicit construction bridge.

### Larry J. Stockmeyer and Albert R. Meyer (1973)

**Identity and access.** Larry J. Stockmeyer and Albert R. Meyer, “Word
Problems Requiring Exponential Time: Preliminary Report,” *Proceedings of the
Fifth Annual ACM Symposium on Theory of Computing*, ACM, 1973, pp. 1--9,
[DOI 10.1145/800125.804029](https://doi.org/10.1145/800125.804029). Use the
[proceedings identity record](https://dblp.org/rec/conf/stoc/StockmeyerM73.html)
and the [accessible primary paper](https://esp.mit.edu/download/827dcf47cbc9cf4a3b04dbf773ea54fb/M3175_meyer-stockmeyer-word-probs.pdf).

**Locator, notation, and standing.** Printed p. 2 defines `B_k` as a language
of encoded Boolean expressions `A(X_1,...,X_k)` made true by `k` alternating
blocks of scalar Boolean variables, beginning existentially; `B_1` corresponds
to propositional satisfiability. `B_omega` is the union over all finite
alternation depths. Theorem 4.1 separately characterizes each polynomial-time
hierarchy level by bounded string quantifiers followed by a polynomial-time
predicate; that characterization is not the literal input syntax of `B_k`.
The source also defines log-space many-one reducibility with a read-only input,
write-only output, and logarithmic work tape. `B_omega` is a language of encoded
quantified formulas, not the polynomial hierarchy itself [Stockmeyer--Meyer,
printed pp. 2--4](https://esp.mit.edu/download/827dcf47cbc9cf4a3b04dbf773ea54fb/M3175_meyer-stockmeyer-word-probs.pdf).

**System, hypotheses, and exact strength.** Theorem 4.3, printed pp. 4--5,
states that `B_omega` is log-space complete for polynomial space. The source
uses bounded strings and its own `B_omega` syntax; identifying this with the
now-standard scalar-variable TQBF/QSAT problem requires a coding translation.
The reduction is log-space many-one, stronger than merely polynomial-time
many-one [Stockmeyer--Meyer, Theorem 4.3](https://esp.mit.edu/download/827dcf47cbc9cf4a3b04dbf773ea54fb/M3175_meyer-stockmeyer-word-probs.pdf).

**Proof status and full outline boundary.** For hardness, the proof encodes a
polynomial-space machine configuration as a fixed-length Boolean string,
expresses one-step reachability by a polynomial formula, and recursively squares
the reachable distance. A quantified midpoint plus a universally selected half
avoids duplicating the preceding formula, so polynomially many recursion layers
describe an exponentially long computation. The source says the resulting
formula has polynomial length and leaves the final verification that the map is
log-space computable to the reader. For membership it says it is not hard to
recognize `B_omega` in deterministic linear space [Stockmeyer--Meyer, proof of
Theorem 4.3, printed pp. 4--5](https://esp.mit.edu/download/827dcf47cbc9cf4a3b04dbf773ea54fb/M3175_meyer-stockmeyer-word-probs.pdf).

**Examples, qualifications, and adjacent variants.** Fixed `B_k` levels model
bounded alternation and are treated separately by Theorem 4.2; their union is
the unbounded-alternation PSPACE-complete problem. The preliminary report omits
or defers several long word-problem proofs, but the Theorem 4.3 configuration
construction is present. “Preliminary Report” must remain in the bibliographic
title and the omitted log-space output detail must not be hidden
[Stockmeyer--Meyer, sections 4--5](https://esp.mit.edu/download/827dcf47cbc9cf4a3b04dbf773ea54fb/M3175_meyer-stockmeyer-word-probs.pdf).

**Reader-facing reconstruction owed.** Define standard closed TQBF and give an
explicit linear/log-space bridge from the source's Boolean variable blocks to
scalar-variable prenex syntax. Do not insert a predicate-compilation step into
the definition of `B_k`. Prove membership by depth-first quantifier evaluation
using polynomial space. For hardness, define configuration encoding, the
one-step predicate, the recursively squared reachability formula, and the
midpoint/universal-selector device; prove formula size, truth equivalence, and
log-space constructibility. This is the register's required full QBF
PSPACE-completeness proof.

### Richard E. Ladner (1977)

**Identity and access.** Richard E. Ladner, “The Computational Complexity of
Provability in Systems of Modal Propositional Logic,” *SIAM Journal on
Computing* 6(3), 1977, pp. 467--480,
[DOI 10.1137/0206033](https://doi.org/10.1137/0206033). Use the [publisher
record and abstract](https://epubs.siam.org/doi/pdf/10.1137/0206033?download=true)
and the [accessible primary scan](https://www.cs.man.ac.uk/~ezolin/ml/bib/Computational_complexity_of_provability_in_systems_of_modal_logic_%28SIAMJC_1977%29.pdf).

**Locator, notation, and standing.** The paper treats decision problems whose
inputs are modal propositional formulas and asks provability in a specified
normal modal system. `K`, `T`, `S4`, and `S5` name different calculi/model
classes, not modal operators. Under their standard Kripke correspondences, `K`
uses arbitrary frames, `T` reflexive frames, `S4` reflexive-transitive frames,
and `S5` equivalence frames; the source's complexity results must stay attached
to the selected system and to provability or nonprovability [Ladner,
introductory definitions, printed pp. 467--470](https://www.cs.man.ac.uk/~ezolin/ml/bib/Computational_complexity_of_provability_in_systems_of_modal_logic_%28SIAMJC_1977%29.pdf).

**Exact result strength.** Every PSPACE problem is log-space many-one reducible
to provability in any modal system between `K` and `S4`. In particular,
provability for `K`, `T`, and `S4` is PSPACE-complete. By contrast, **S5
nonprovability** is log-space complete for nondeterministic polynomial time.
Equivalently, S5 satisfiability/nonvalidity is NP-complete and S5
provability/validity is coNP-complete [Ladner, abstract and main theorems](https://epubs.siam.org/doi/pdf/10.1137/0206033?download=true).

**Proof status and full outline boundary.** The PSPACE lower bound encodes
quantified Boolean evaluation into modal provability and is uniform across the
systems between `K` and `S4`; the upper bounds use finite proof/model search
that can be traversed in polynomial space without retaining the whole
exponential tree. For S5, a nonvalid formula has a polynomially bounded
certificate/countermodel, giving NP membership, while propositional
satisfiability embedded in S5 gives hardness. A handbook outline should state
the recursive QBF-to-modal translation and its induction invariant, explain
depth-first polynomial-space search, and give the S5 small-certificate argument;
the detailed modal reduction gadgets may remain cited [Ladner, proof sections,
printed pp. 470--479](https://www.cs.man.ac.uk/~ezolin/ml/bib/Computational_complexity_of_provability_in_systems_of_modal_logic_%28SIAMJC_1977%29.pdf).

**Qualifications and adjacent variants.** The lower-bound theorem for systems
between `K` and `S4` does not imply PSPACE membership for every intermediate
axiom set under an arbitrary representation; the explicit completeness rows
in the source are `K`, `T`, and `S4`. S5 is easier only after the decision
polarity is fixed. Modal model checking on a supplied finite model is yet
another problem and is not classified by this provability table [Ladner,
statement of results](https://epubs.siam.org/doi/pdf/10.1137/0206033?download=true).

**Reader-facing reconstruction owed.** Print a four-column table with system,
frame class, decision problem, and class/reduction. Use separate rows for S5
satisfiability/nonprovability and S5 validity/provability. Precede the table by
the exact QBF theorem and follow it by a proof-outline paragraph explaining why
`K/T/S4` use polynomial space while S5 has polynomial countermodels.

### Christos H. Papadimitriou (1994)

**Identity and access.** Christos H. Papadimitriou, *Computational Complexity*,
Reading, Massachusetts: Addison-Wesley, 1994, xv + 523 pp., ISBN
0-201-53082-1, LCCN 93005662. No DOI was located for the book. The
[Library of Congress record](https://www.loc.gov/item/93005662/) closes the
catalogue identity. The [Google Books volume record](https://books.google.com/books/about/Computational_Complexity.html?id=JogZAQAAIAAJ)
confirms the publisher, year, extent, and both ISBN forms; it is a Google scan
and catalogue record, not a publisher record. Its public search-within-volume
snippets expose primary text on printed pp. 455, 456, and 458 even though the
volume is marked `noview`. A matching
[Internet Archive library scan](https://archive.org/details/computationalcom0000papa)
is access-restricted, and neither the Library of Congress nor HathiTrust
supplied a readable body. The [nonpublisher scan of the primary book
text](https://djvu.online/file/ugtJZIrmGbFU7) remains the only continuous body
inspected for pp. 455--458 and p. 487. The records inspected do not establish
an ordinal edition statement or particular printing, so “1994 Addison-Wesley
edition” is safe and “first edition” is not added. See the
[dedicated acquisition note](p09-papadimitriou-qbf-source-note.md).

**Locator, notation, and standing.** Chapter 4, printed pp. 73--84, separates
propositional satisfiability and validity. Chapter 5, pp. 87--118, develops
first-order syntax, models, validity, proof, completeness, and consequences.
Chapter 8, especially the Cook theorem around printed pp. 171--173, presents
modern reductions and NP-completeness. Chapter 19, “Polynomial Space,” starts
at p. 455. That page defines `QSAT`; Theorem 19.1 and its proof occupy printed
pp. 456--458. Note 19.4.1 is on p. 487 [Papadimitriou, Chapters 4, 5, 8,
and 19](https://djvu.online/file/ugtJZIrmGbFU7).

**Exact syntax, source defect, and result strength.** The displayed QSAT
language has a conjunctive-normal-form matrix and one scalar Boolean quantifier
per variable, alternating strictly and beginning existentially. It is neither
the book's name for arbitrary TQBF syntax nor Stockmeyer--Meyer's literal
block-variable `B_omega`. Printed p. 455 contains a real contradiction: the
display, the parity clause for the last quantifier, and the p. 456 proof are
existential-first, while the prose immediately before the display describes
both truth values for `x_1`, hence a universal-first prefix. Google Books
independently exposes both readings, and the inspected author-titled errata has
no p. 455 correction. The display-and-proof-controlled existential-first
reading is coherent, but the prose defect must remain recorded.

Theorem 19.1 states that QSAT is PSPACE-complete. The book's reduction is a
single membership-preserving output function computed by a deterministic
logspace machine, so the exact current classification is deterministic
logspace many-one completeness, stronger than polynomial-time many-one
completeness. Note 19.4.1 says that the PSPACE-completeness of QSAT “was
established in” Stockmeyer--Meyer 1973. It does not literally say “first proof”;
moreover, that p. 487 sentence is presently visible only in the nonpublisher
body [Papadimitriou, Theorem 19.1 and note 19.4.1](https://djvu.online/file/ugtJZIrmGbFU7).

**Proof status and full outline boundary.** Unlike a mere textbook pointer,
Theorem 19.1 contains the proof. Membership treats all assignments as an
implicit depth-`n` tree whose existential levels are OR levels and universal
levels are AND levels, then evaluates it in linear space. Hardness encodes a
polynomial-space machine configuration as a Boolean block, defines equality or
one-step reachability, and recursively squares the reachability bound. The
single-copy recurrence existentially chooses a midpoint, universally chooses
two endpoint blocks, and guards one recursive occurrence so that it must hold
for both half-path pairs. This displayed recurrence with universally quantified
endpoints is not literally the selector-bit formula used in the reader-facing
Stockmeyer--Meyer reconstruction. After prenexing, the proof observes that the
CNF would be too large but the DNF is polynomial, emits the layered formula in
logspace, reduces first to the complement of the displayed CNF language, and
finishes with `PSPACE = coPSPACE` [Papadimitriou, printed pp.
456--458](https://djvu.online/file/ugtJZIrmGbFU7).

Google Books snippets independently confirm the membership argument and
configuration setup on p. 456 and the logspace/complement finish on p. 458.
They do not expose the continuous p. 457 recurrence. The latter agrees in
architecture with Stockmeyer--Meyer's author-hosted 1973 proof, but exact p.
457 typography and wording remain nonpublisher-body-only.

**Examples, qualifications, and adjacent variants.** QSAT is presented as a
two-player alternating-choice game, clarifying the existential/universal
semantics. Propositional validity is coNP-complete, whereas unrestricted
first-order validity is undecidable (though recursively enumerable by
completeness); the word “validity” therefore cannot be assigned one complexity
class without its logic. The modal classifications come from Ladner rather than
from merely placing them beside QSAT [Papadimitriou, Chapters 4--5, 10, and
19](https://djvu.online/file/ugtJZIrmGbFU7).

**Access qualification and reader-facing reconstruction owed.** Book identity,
the p. 455 definition, the Theorem 19.1 statement and pp. 456--458 locator, the
intended syntax with its printed contradiction, and deterministic-logspace
reduction strength are independently closed. Full publisher/library-body
comparison remains **OPEN** for the continuous p. 457 proof and p. 487 note.
Use the book as the modern synthesis, but distinguish its exact QSAT language
and recurrence with universally quantified endpoints from unrestricted TQBF
and the selector-bit Stockmeyer--Meyer reconstruction; do not turn “was
established in” into an exact “first proof” attribution.

**Reader-facing delivery status, 2026-08-22.** The presentation now defines
Cook's query machine and `P`-reducibility at their historical oracle strength,
then reconstructs a complete modern SAT reduction with an explicitly typed
tableau alphabet, exactly-one clauses, initial conditions, local transition
windows, an accepting row, both correctness directions, a polynomial size
count, and the independent NP-membership argument. It derives Cook's DNF
tautology query by negating the CNF tableau and keeps Levin's independent
historical role separate. For Stockmeyer--Meyer it corrects the old conflation
between the literal `B_k` Boolean-expression syntax and Theorem 4.1's separate
polynomial-time-predicate characterization; supplies the block/scalar logspace
bridge; and gives membership plus the complete selector-based reachability
proof, including recurrence size, induction, configuration bound, and logspace
output. For Ladner it prints separate system, frame, problem-polarity, and
reduction columns; states the exact `K`--`S4` theorem-set interval; exposes the
source's direct reduction to nonprovability and Fact 2.7 complement bridge;
states the quantifier-level induction invariant; records the three polynomial
space upper bounds; and proves the `m+1`-world `S5` certificate argument. The
presentation now also records Papadimitriou's CNF, existential-first QSAT
syntax, its p. 455 universal-first prose conflict, the exact Theorem 19.1
locator and reduction strength, the recurrence with universally quantified
endpoints, and the DNF/complement finish without conflating them with the
preceding Stockmeyer--Meyer presentation. This closes the reader-facing reconstruction
owed by `N-c-026`. The continuous p. 457 and p. 487 publisher/library-copy
comparison remains open, so that source row and Part IX are not frozen.

## `N-c-028` — interpolation-based model checking

### Kenneth L. McMillan (2003)

**Identity and access.** Kenneth L. McMillan, “Interpolation and SAT-Based
Model Checking,” in *Computer Aided Verification*, LNCS 2725, Springer, 2003,
pp. 1--13,
[DOI 10.1007/978-3-540-45069-6_1](https://doi.org/10.1007/978-3-540-45069-6_1);
use the [author-hosted primary PDF](https://mcmil.net/pubs/CAV03.pdf).

**Locator, notation, and standing.** Printed pp. 2--3 define a Craig
interpolant for an inconsistent pair `(A,B)`: a formula `P` implied by `A`,
inconsistent with `B`, and containing only symbols common to `A` and `B`. The
paper constructs `P` from a resolution refutation. Printed p. 4 models a Boolean
finite-state automaton as `M=(I,T,F)`, where formulas describe initial states,
the transition relation, and final/bad states; `T` is assumed total. A formula
`Cnf(f,U)` may introduce fresh variables `U` but must satisfy
`exists U. Cnf(f,U) <-> f` [McMillan, printed pp. 2--4](https://mcmil.net/pubs/CAV03.pdf).

**System, hypotheses, and exact result strength.** The `FiniteRun` procedure on
printed pp. 5--6 alternates bounded SAT checks with interpolants that
overapproximate states reachable from the current approximation while excluding
states that can reach `F` through the remaining suffix. A satisfiable bounded
formula supplies a real run; an unsatisfiable formula plus resolution proof
supplies the interpolant. Theorem 3 gives correctness of the procedure when it
terminates. In Theorem 4 the proof chooses `k` equal to the automaton's reverse
depth and then uses finiteness to force a fixed point [McMillan, Theorems 3--4,
printed pp. 5--7](https://mcmil.net/pubs/CAV03.pdf).

**Parameter discrepancy.** The prose introducing the generic procedure says
to fix `k >= 0`, but the displayed `FiniteRun` algorithm, Theorem 3, and the
subsequent termination development require `k > 0`. The handbook must use the
positive hypothesis proved with the procedure or supply a separately checked
zero-bound case. It must not normalize the two source statements silently
[McMillan, printed pp. 5--6](https://mcmil.net/pubs/CAV03.pdf).
Theorem 4's proof then sets `k` equal to the reverse depth without discussing
the edge case in which that depth is zero. The reader-facing reconstruction
therefore uses `k = max(1, reverse depth)`: this preserves the displayed
procedure's positive hypothesis, and the same proof applies because a suffix
bound at least the reverse depth excludes every state from which `F` is
reachable.

**Proof status and full outline boundary.** The interpolation theorem is proved
by assigning partial interpolants to resolution-proof nodes and inducting over
resolution steps. An `A`-root receives its shared literals, a `B`-root receives
`True`, and a resolution step uses disjunction for an `A`-local pivot and
conjunction otherwise. Procedure correctness then
uses the interpolant implications to show that each approximation safely covers
the required reachable states and never introduces a state capable of reaching
`F` within the protected suffix. Termination uses finiteness plus the reverse-
depth bound to reach a fixed point. A handbook pointer should state these three
invariants; it need not reproduce the SAT implementation [McMillan, printed
pp. 2--7](https://mcmil.net/pubs/CAV03.pdf).

**Examples, qualifications, and adjacent variants.** Interpolant choice affects
how quickly the approximation converges but not the stated soundness invariant.
The theorem is about Boolean finite-state safety/reachability and a proof-
producing resolution SAT solver; it is not a general temporal-logic model-
checking theorem. “Reverse depth” is defined in source prose; no new arrow or
rank notation should be invented unless it is separately defined and used
[McMillan, algorithm discussion and experiments](https://mcmil.net/pubs/CAV03.pdf).

**Reader-facing reconstruction owed.** Define interpolants and the variable
restriction, show the resolution construction on a two- or three-step refutation,
define the Boolean automaton and run formula, and trace one `FiniteRun`
iteration from UNSAT proof to state approximation. State Theorems 3--4 with
`k>0`, define reverse depth, state the edge-safe choice
`k = max(1, reverse depth)`, and label the remaining solver material as a
citation-only pointer.

**Reader-facing delivery status, 2026-08-22.** The main method and source
presentation now define the finite Boolean system, semantic run, projected
definitional CNF, exact `A/B` proof partition, Craig interpolant, and reverse
depth with their separate standing. The presentation calculates every label in
a two-resolution interpolation proof, then traces a one-bit safe system from
the UNSAT partition through `P = not x`, the unchanged reachability
approximation, and the resulting inductive invariant. It proves the three
iteration invariants, keeps a genuine first-iteration run separate from a later
spurious suffix, and derives the fixed-point closure implication. Finally it
states the source's `k > 0` discrepancy, uses
`k = max(1, reverse depth)`, and reconstructs the finite-state termination
argument by excluding all backward-reachable states before counting strict
semantic enlargements. This closes the reader-facing reconstruction owed by
`N-c-028`; it does not close the independent `N-x-015` authority gap or freeze
Part IX.

## `N-x-015` — probability logics and quantitative/stochastic model checking

The audit revokes the old exclusion. This row now owes two different
presentations: a logic of probability/uncertainty, and algorithms for checking
probabilistic transition models. Neither presentation can be used as a proxy
for the other.

### Joseph Y. Halpern (2003)

**Identity and access.** Joseph Y. Halpern, *Reasoning about Uncertainty*, MIT
Press, first edition, 2003, 497 pp., hardcover ISBN 978-0-262-08320-1. No DOI
was located for the first edition. The [MIT Press first-edition
record](https://mitpress.mit.edu/9780262083201/reasoning-about-uncertainty/)
distinguishes the 2003 hardcover from the later paperback; the Library of
Congress and named-library records independently identify the same physical
edition. The currently visible [Internet Archive
item](https://archive.org/details/reasoningaboutun0000halp) is not that object:
its public copyright-leaf OCR says `First MIT Press paperback edition, 2005`,
and its restricted BookReader exposes no main-text leaves or downloads. The
older Internet Archive identifier linked from Open Library's exact 2003 record
is now dark. Halpern's [author publication
page](https://www.cs.cornell.edu/home/halpern/abstract.html) calls the 2005
paperback “slightly revised,” so neither item may be substituted silently.
The [Cornell catalogue record](https://catalog.library.cornell.edu/catalog/5040957)
confirms an exact 2003 physical copy and exposes a chapter-scan request route,
but the copy is checked out through 2027-04-04 and no request, eligibility, or
fulfilment claim was made. The qualified
[first-edition contents](https://external.dandelon.com/download/attachments/dandelon/ids/CH00145F9D05BECEE6592C1257EDF0035D9B0.pdf)
provide chapter locators but no technical body.

**Locator and source role.** Chapter 7, “Logics for Reasoning about
Uncertainty,” begins at printed p. 239. The contents place measurable
probability at §7.3, p. 254; other quantitative measures at §7.4, p. 260;
relative likelihood at §7.5, p. 263; knowledge and probability at §7.6,
p. 268; independence at §7.7, p. 271; and expectation at §7.8, p. 273.
Chapter 8 begins at p. 287, so the inferred Chapter 7 interval is pp. 239--286.
The chapter therefore controls the
relationship among several uncertainty languages; it is not solely a PCTL or
model-checking source [Halpern, first-edition contents](https://external.dandelon.com/download/attachments/dandelon/ids/CH00145F9D05BECEE6592C1257EDF0035D9B0.pdf).

**Notation, hypotheses, exact strength, and proof-status gap.** The complete
first-edition technical text remains unavailable. Publisher and library records
close bibliographic identity, while the Dandelon scan closes contents-level
architecture only. Consequently, the exact grammars, model tuples,
measurability and additivity assumptions, satisfaction clauses, axiom systems,
theorem numbers, completeness hypotheses, small-model and decision results,
proof boundaries, examples, and edition-specific differences in Halpern 2003
are **OPEN**. No such field may be reverse-engineered from the 2005 or 2017
edition, or from a related article, and attributed to the 2003 book.

**Examples, qualifications, and adjacent variants.** The contents verify
separate headings for measurable probability, other quantitative
representations of likelihood, relative likelihood, knowledge and probability,
independence, and expectation [Halpern, Chapter 7
contents](https://external.dandelon.com/download/attachments/dandelon/ids/CH00145F9D05BECEE6592C1257EDF0035D9B0.pdf).
They do not expose the exact operators, their semantic standing, or whether a
particular conditional construction occurs. Those distinctions must be read
from the first-edition body rather than imported from adjacent papers.

**Reader-facing reconstruction owed.** Acquire the 2003 Chapter 7 body before
freezing text: readable pp. 239--286 from ISBN 0-262-08320-5 must be bound to
the 2003 title and copyright/ISBN pages. Then give, for each language actually
selected, its formula
grammar, model tuple, measurability/finite-additivity assumptions, satisfaction
relation, axioms, soundness/completeness status, decision/small-model result,
and one worked uncertainty example. Explicitly separate theorem text read in
Halpern 2003 from any result imported from the adjacent primary paper below.

#### Adjacent primary technical source, not a substitute for Halpern 2003

Ronald Fagin, Joseph Y. Halpern, and Nimrod Megiddo, “A Logic for Reasoning
about Probabilities,” *Information and Computation* 87(1--2), 1990,
pp. 78--128,
[DOI 10.1016/0890-5401(90)90060-U](https://doi.org/10.1016/0890-5401(90)90060-U);
use the [author-hosted primary PDF](https://theory.stanford.edu/~megiddo/pdf/fag-hal.pdf).

**Definitions and exact strength available from the adjacent source.** The
basic language forms weight terms as integer linear combinations of expressions
`w(phi)` and forms formulas as Boolean combinations of linear inequalities
between such terms. A probability structure supplies worlds, a truth assignment
for primitive propositions at each world, and a probability space in which the
events denoted by propositional formulas are measurable. The paper gives a
sound and complete axiomatization using propositional reasoning, valid linear-
inequality reasoning, normalization/nonnegativity, equivalence invariance, and
the exact split `w(phi and psi) + w(phi and not psi) = w(phi)`. Theorem 2.2
proves this system sound and complete; Lemma 2.1 derives `w(false)=0`, and
disjoint finite additivity follows [Fagin--Halpern--Megiddo, sections
2--3](https://theory.stanford.edu/~megiddo/pdf/fag-hal.pdf).

**Proof boundary and complexity.** Completeness expands event terms over
complete propositional atoms, reduces a consistent conjunction of weight
constraints to one feasible linear system, and constructs a probability model
from a solution. Theorem 2.4 gives at most `|f|` states when coefficient length
is counted as one symbol. Theorem 2.6 additionally chooses rational state
probabilities of size `O(|f| ||f|| + |f| log |f|)`, where `||f||` is the
largest binary coefficient length. This yields the NP upper bound in Theorem
2.9; sending `phi` to `w(phi) > 0` supplies the propositional SAT lower bound.
The paper
also treats nonmeasurable events via inner probability and discusses richer
conditional/nonlinear languages using real closed fields. Those extensions
require their own semantics and higher decision bounds; they cannot be
summarized by the linear-language theorem [Fagin--Halpern--Megiddo,
completeness, small-model, and complexity sections](https://theory.stanford.edu/~megiddo/pdf/fag-hal.pdf).

**Reader-facing delivery.** Definition `def:p09-likelihood-logic`, Theorem
`thm:p09-likelihood-logic`, and
`handbook/parts/p09/presentations/n-x-015.tex` now give the exact linear
language and measurable probability structure, the primitive splitting axiom
and its finite-additivity consequence, a worked inclusion--exclusion system,
Theorems 2.2, 2.4, 2.6, and 2.9 at their exact strength, and the
atom-expansion/linear-system/sparse-support proof spine. This closes the
adjacent 1990 primary-paper presentation. It does not close the explicit
Halpern 2003 source gap or supply stochastic model checking.

### Christel Baier and Joost-Pieter Katoen (2008)

**Identity and access.** Christel Baier and Joost-Pieter Katoen, *Principles of
Model Checking*, MIT Press, 2008, ISBN 978-0-262-02649-9. No book DOI was
located. Use the [MIT Press record](https://mitpress.mit.edu/9780262026499/principles-of-model-checking/)
for identity and the [complete primary book PDF](https://is.ifmo.ru/books/_principles_of_model_checking.pdf)
for technical locators.

**Exact scope and locators.** Chapter 10, printed pp. 745--899, is the
quantitative chapter. Discrete-time Markov chains begin at p. 747, reachability
at p. 759, PCTL at p. 780, finite-chain PCTL model checking at p. 785, PCTL* at
p. 806, chains with costs at p. 816, Markov decision processes at p. 832, MDP
reachability at p. 851, and MDP PCTL model checking at p. 866. The chapter
summary is at p. 896. There is no CTMC or CSL section in this book [Baier--Katoen,
Chapter 10 contents and summary](https://is.ifmo.ru/books/_principles_of_model_checking.pdf).

**Markov-chain notation, definitions, and standing.** A Markov chain has a
state set, a stochastic transition-probability matrix, an initial distribution,
atomic propositions, and a state-labeling function. Infinite paths receive a
probability measure generated from cylinder sets. A state formula denotes a set
of states; a path formula denotes a measurable set of paths; the probability
operator compares the measure of that path set with an interval/bound. These
three levels---transition probability, path measure, and truth of a probability
formula---must not be collapsed [Baier--Katoen, §§10.1--10.4](https://is.ifmo.ru/books/_principles_of_model_checking.pdf).

**PCTL/PCTL* language and hypotheses.** PCTL state formulas combine atomic
propositions and Boolean connectives with probability bounds on next, bounded-
until, or unbounded-until path formulas. PCTL* permits the fuller Boolean and
temporal nesting on paths. The model-checking algorithms and complexity
theorems below are for **finite** chains; the general measure definition alone
does not make an infinite-state algorithm finite [Baier--Katoen, PCTL syntax at
printed pp. 780--785 and PCTL* at pp. 806--815](https://is.ifmo.ru/books/_principles_of_model_checking.pdf).

**Exact finite-chain result strength.** Reachability probabilities are the
least/unique relevant solution of a linear equation system after graph analysis
separates target and impossible states. Bounded until is computed by finite
dynamic programming; unbounded until uses reachability equations. The PCTL
algorithm labels states bottom up by subformula. The theorem at printed
pp. 786--787 makes finite-chain PCTL model checking polynomial in the model and
linear in the formula and largest encoded step bound under the book's stated
cost convention [Baier--Katoen, §§10.1.1 and 10.4.1](https://is.ifmo.ru/books/_principles_of_model_checking.pdf).

**MDP notation, definitions, and exact strength.** An MDP adds nondeterministic
action choice to probabilistic transitions. A scheduler resolves those choices;
state formulas quantify through minimum or maximum path probabilities over the
relevant scheduler class. Reachability uses Bellman-style optimality equations
and linear-programming/iterative algorithms after graph preprocessing. Theorem
10.115, printed p. 869, states that PCTL model checking for a finite MDP is
polynomial in the MDP and linear in the formula/largest step bound under the
book's convention [Baier--Katoen, §§10.6--10.6.3](https://is.ifmo.ru/books/_principles_of_model_checking.pdf).

**Proof status and full outline boundary.** A full reader-facing outline should
construct the path measure from cylinders; prove the reachability equation by
conditioning on the first step; justify uniqueness after zero/one-state
classification; derive bounded-until recursion; and prove bottom-up PCTL
labeling by structural induction. For MDPs it should define schedulers before
`Pmin/Pmax`, derive the optimality equations, and state when extremal schedulers
exist. The automata-theoretic PCTL* and omega-regular developments can remain
cited if the product construction and acceptance objective are identified
[Baier--Katoen, Chapter 10](https://is.ifmo.ru/books/_principles_of_model_checking.pdf).

**Examples, counterexamples, and qualifications.** A finite coin/die chain can
separate “some path reaches the target,” “positive probability,” and
“probability one”: a measure-zero exceptional path need not falsify an
almost-sure property. An MDP example must show that different schedulers produce
different reachability probabilities and why both minimum and maximum are
reported. Numerical approximation and the encoding of rational probabilities
must be stated when an exact comparison is claimed [Baier--Katoen, reachability
and MDP examples in Chapter 10](https://is.ifmo.ru/books/_principles_of_model_checking.pdf).

**Reader-facing delivery.** Definitions `def:p09-dtmc-mdp` and `def:p09-pctl`,
Theorem `thm:p09-pctl-model-checking`, and the Baier--Katoen subsection of
`handbook/parts/p09/presentations/n-x-015.tex` now give the finite DTMC and MDP
tuples, scheduler and cylinder measures, a four-state graph and transition
matrix, a cylinder calculation, bounded/unbounded reachability calculations,
minimum/maximum MDP values, the finite PCTL algorithm and complexity boundary,
and a separately bounded PCTL*/cost paragraph. The subsection ends by stating
that the book contains no CTMC or CSL presentation. This closes the registered
Baier--Katoen 2008 role without borrowing continuous-time claims.

#### Required separate CTMC/CSL authority

Christel Baier, Boudewijn R. Haverkort, Holger Hermanns, and Joost-Pieter
Katoen, “Model-Checking Algorithms for Continuous-Time Markov Chains,” *IEEE
Transactions on Software Engineering* 29(6), 2003, pp. 524--541,
[DOI 10.1109/TSE.2003.1205180](https://doi.org/10.1109/TSE.2003.1205180). Use
the [authors' publication record](https://iccl.inf.tu-dresden.de/web/Christel_Baier/Publikationen/en)
and [institutional full PDF](https://ris.utwente.nl/ws/files/268940692/Baier2002model_checking.pdf).

**Definitions and exact source role.** The article treats finite labeled CTMCs
whose transition structure is given by rates rather than one-step
probabilities. Exponential residence times and the race among outgoing rates
induce a continuous-time path measure. CSL adds probability bounds on
time-bounded until and a steady-state operator. These definitions are genuinely
different from DTMC/PCTL: elapsed-time intervals and long-run state probability
cannot be reconstructed by renaming discrete steps [Baier et al., abstract and
model/logic sections](https://doi.org/10.1109/TSE.2003.1205180).

**Exact result strength and proof boundary.** The article reduces unbounded
until and steady-state checking to systems of linear equations; it characterizes
time-bounded until through transient probabilities/integral equations and gives
numerical algorithms based on uniformization. It also analyzes lumping
equivalences that preserve CSL and approximation. A full presentation must
derive the embedded discrete jump probabilities, exponential timing law, and
transient/uniformization computation before stating a CSL result [Baier et al.,
abstract and algorithm sections](https://ris.utwente.nl/ws/files/268940692/Baier2002model_checking.pdf).

**Exact internal source map.** The journal version's Definition 1 gives
`M=(S,R,L)`, types `R` on all of `S x S`, permits positive rate self-loops, and
sets `E(s)=sum_t R(s,t)`; Definitions 3--6 give timed paths, CSL syntax, and
state/path semantics. Proposition 2 gives the BSCC decomposition for the
steady-state operator. Corollary 1 gives the embedded-chain fixed point for
unbounded until. Theorem 1 gives the least-fixed-point Volterra equation.
Section 4.2, Theorems 2--3, gives the one- and two-transient-analysis reductions
for `[0,t]` and `[a,b]`. Section 4.3, equations (7)--(8), gives uniformization
and chooses the truncation index so that omitted Poisson mass is at most the
requested epsilon. Section 6 gives the operator-level and total cost analysis.
These locators and statements were manually reconciled against the rendered
institutional report and the journal text. The paper's Poisson-tail condition
does not itself certify floating-point roundoff or decide exact equality with a
threshold; those remain separate arithmetic obligations. A line-by-line audit
of every proof in the paper is not claimed.

**Reader-facing delivery.** Definition `def:p09-ctmc-csl`, Theorem
`thm:p09-csl-model-checking`, and the separate CTMC/CSL subsection of
`handbook/parts/p09/presentations/n-x-015.tex` now give the finite rate model,
exponential residence law, timed-path cylinders, typed CSL grammar and
semantics, embedded-chain and steady-state computations, the Volterra and
transient-analysis routes, uniformization with a Poisson-tail error interval,
the exact-equality boundary, and a worked rate-two timed reachability example.
This closes the Baier et al. 2003 reader-facing role and preserves its
separation from Baier--Katoen 2008.

## Depth crosswalks

### `D-P11-006` — SLD resolution, completeness, negation as failure, and Prolog

This depth row is a coordinated presentation of `N-c-022`; it is not an
additional semantics. The reader order should be:

1. **Definite declarative core.** Define a definite program, Herbrand base and
   interpretation, immediate-consequence operator, least fixed point, and least
   Herbrand model. Prove monotonicity, finite-stage derivability, and
   `lfp(T_P)=M_P` using [van Emden--Kowalski 1976](https://maarten.vanemden.com/Publications/kowVE.pdf).
2. **SLD operational core.** Define goals, standardization apart, selected atom,
   most general unifier, resolvent, derivation, refutation, computed answer, SLD
   tree, and computation rule. Prove soundness, state and prove the lifting
   spine, and prove strong completeness for correct answers using
   [Apt--van Emden 1982](https://ir.cwi.nl/pub/10272/10272D.pdf) and [Lloyd
   1987](https://doi.org/10.1007/978-3-642-83189-8).
3. **Control separation.** Show on one tree that atom selection, clause choice,
   and branch traversal are three choices. Lloyd's computation-rule
   independence concerns the first; it does not make leftmost depth-first
   traversal fair. Include one goal with a finite successful branch and an
   earlier infinite branch that a depth-first interpreter never leaves
   [Lloyd, Chapter 2, §9](https://doi.org/10.1007/978-3-642-83189-8).
4. **Finite failure and default negation.** Define a finitely failed SLD tree,
   Clark completion, and the relevant equality theory. Prove the completion-
   soundness direction for a finite failed tree, then define the SLDNF treatment
   of negative goals with safe ground selection, the separate allowedness
   condition, and the floundering boundary
   [Clark 1978](https://www.doc.ic.ac.uk/~klc/neg.html) and [Lloyd, Chapter
   3](https://doi.org/10.1007/978-3-642-83189-8).
5. **Prolog implementation paragraph.** State which pure fragment is being
   idealized, then separately describe leftmost selection, textual clause order,
   depth-first traversal, cut, arithmetic, and other extra-logical features.
   These may prune or diverge despite the pure SLD existence theorem. Exact
   standards claims require the [ISO/IEC 13211-1 record](https://www.iso.org/standard/21413.html),
   all three applicable corrigenda, and access to the relevant corrected
   normative clauses.

**Proof boundary.** The least-model/fixpoint proof, SLD soundness proof, lifting
lemma outline, and finite-failure induction are owed locally. The entire Lloyd
SLDNF development and language-standard semantics may remain cited only if all
side conditions are printed. “Prolog is complete” is prohibited: the source
theorem concerns existence of an SLD refutation/computed answer under a
computation rule, not success of every search strategy [Lloyd, Theorems
9.2--9.5](https://doi.org/10.1007/978-3-642-83189-8).

**Required worked sequence.** Use one append or ancestor program throughout:
compute `T_P` stages, identify the least-model answer, produce the same answer
by an SLD derivation with mgus, then alter the query/program order to exhibit
depth-first divergence. Use a separate closed database for finite failure and
a nonground negative goal for floundering. The examples must not suggest that
divergence makes the declarative answer false.

### `D-P11-007` — keep ASP and Datalog distinct

The depth row must coordinate `N-c-023` and `N-c-024` through an explicit
comparison, not merge them under “rule systems.”

| Dimension | Positive Datalog | Normal/disjunctive ASP |
|---|---|---|
| Rule form | Function-free positive Horn rule; recursion allowed | Rule may use default-negated body literals; later syntax may permit disjunctive heads |
| Semantic construction | One monotone immediate-consequence operator iterated from the empty instance | A candidate-dependent reduct followed by a least-model test (normal) or minimal-model test (disjunctive) |
| Intended result | Unique least fixed point/model and query relation | Zero, one, or many stable models/answer sets encoding solutions |
| Operational task | Derive all fixed-point consequences / answer a query | Search for a candidate model satisfying its own reduct condition |
| Representative complexity | Fixed-program data evaluation polynomial-time; combined evaluation EXPTIME-complete | Ground normal answer-set existence NP-complete; ground disjunctive existence complete at the second existential PH level |
| Containment | General Datalog query containment undecidable | Query containment is not the defining decision problem in the cited ASP sources |

The Datalog claims and complexity conventions are controlled by
[Abiteboul--Hull--Vianu, Chapters 12--16](https://wiki.epfl.ch/provenance2011/documents/foundations%20of%20databases-abiteboul-1995.pdf)
and [Vardi 1982](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract); the ASP
semantics and complexity rows are controlled by [Gelfond--Lifschitz's
definition](https://www.cs.utexas.edu/~vl/papers/12defs.pdf), [Marek--Truszczyński
1999](https://cs.uky.edu/~marek/papers.dir/00.dir/alternative.pdf), and
[Brewka--Eiter--Truszczyński 2011](https://www.researchgate.net/publication/220421804_Answer_Set_Programming_at_a_Glance).

**Proof boundary.** Prove Datalog finite convergence/model equality and work
transitive closure. For ASP, calculate reducts for every candidate of a small
normal program and prove the resulting stable-model set; outline NP membership
and give a sourced hardness reduction. Disjunctive complexity may remain cited
if its second-level quantifier structure is explained. Never reuse the Datalog
least fixed point as the semantics of a negative ASP program.

**Counterexample owed.** Use `p <- not q; q <- not p` to show two stable models.
No monotone iteration from the empty set yields that choice semantics. Conversely,
positive transitive closure has one least model and does not require guessing a
candidate. This pair is the shortest reader-visible proof that the two rows
cannot be collapsed.

### `D-P11-008` — keep Hoare/wp and separation logic distinct

The depth row coordinates `N-c-019` and `N-c-020` while preserving three
separate semantic presentations:

| Presentation | Assertions/transformer | State model | Correctness standing | Distinct theorem owed |
|---|---|---|---|---|
| Floyd/Hoare | Assertions before/after control points; triples | Whole sequential program state | Partial correctness, with termination separate | Local verification conditions and rule soundness |
| Dijkstra | `wp(S,R)` predicate transformer | Guarded-command states with demonic choice | Guaranteed proper termination plus `R` | Exact transformer equations and invariant/variant repetition proof |
| Separation logic | Spatial assertions `emp`, points-to, `*`, and `-*` | Stack plus finite heap split into disjoint parts | Fault-avoiding local partial correctness | Small axioms, locality lemma, and frame-rule soundness |

Floyd/Hoare/Dijkstra distinctions are source-controlled by [Floyd
1967](https://www.lem12.uksw.edu.pl/images/1/15/AssigningMeanings1967.pdf),
[Hoare 1969](https://sites.cs.ucsb.edu/~kemm/courses/cs266/acmhoare69.pdf), and
[Dijkstra 1975](https://www.cs.utexas.edu/~EWD/ewd04xx/EWD472.PDF). Relative
completeness requires Cook's assertion-language expressiveness hypotheses
[Cook 1978](https://www.cs.toronto.edu/~sacook/homepage/soundness.pdf).
Spatial semantics and the frame proof are controlled by [Reynolds
2002](https://www.cs.cmu.edu/~jcr/seplogic.pdf); automated bi-abductive summary
inference is a further algorithmic layer [Calcagno et al. 2011](https://www.cs.ox.ac.uk/people/hongseok.yang/paper/jacm11-biabduction-webversion.pdf).

**Reader-facing sequence owed.** First verify one scalar loop with a Hoare
invariant and a separate termination variant; compute its Dijkstra `wp` and
show why total and partial preconditions differ. Then switch state models,
define exact heap satisfaction, and verify one local list update with a frame.
Finally pose one bi-abduction problem that infers a missing precondition and an
untouched frame. A scalar assertion conjoined to a triple is not automatically
a separable heap frame.

**Proof boundary and counterexamples.** Locally prove Hoare-rule soundness,
Dijkstra's guarded-choice equation, the total repetition rule, and the frame
rule from locality. Cite Cook's full relative-completeness induction after
stating expressiveness. Include (i) a nonterminating loop satisfying a partial
triple but not Dijkstra's total `wp`, (ii) an aliasing update invalidating an
ordinary heap rule, and (iii) a frame-rule side-condition violation in which
the command modifies a free stack variable of the frame.

## Explicit acquisition-gap ledger

These are source gaps, not invitations to fill prose by inference.

| Row/source | Status | Exact unresolved item | Effect on reconstruction |
|---|---|---|---|
| `N-c-021`, Harel--Kozen--Tiuryn 2000 | **ACQUIRED; LOCATORS CLOSED** | Published Chapters 4--10 were acquired from the authors' Cornell course site; Axiom System 5.5, Section 6.1, Lemma 6.4, Theorems 6.5 and 7.6, Algorithm 8.2, and Theorems 8.4--8.5 were inspected. | Use those base-PDL statements at their exact strength; extensions in Chapter 10 retain separate hypotheses. |
| `N-c-022`, Lloyd 1987 | **INSTITUTIONAL SCAN INSPECTED; PUBLISHER BODY OPEN** | The corrected-printing scan gives safe selection, ranked SLDNF trees, Proposition 15.1, Theorems 15.4 and 15.6, and the hierarchical-only Theorem 16.3; the open Springer record does not expose the body. | Freeze the mathematical side conditions and exact strength with provenance qualified; reserve direct publisher-copy quotation. |
| `N-c-023`, Gelfond--Lifschitz 1988 | **AUTHOR COPY ACQUIRED; ORIGINAL CONTENT AND SUPPLIED PROOFS CLOSED; PUBLISHER FACSIMILE OPEN** | Lifschitz's live first-party bibliography identifies the paper and its former `stable.ps` link; the archived capture of that exact author URL supplies the complete eleven-page paper. Sections 2--4, Theorems 1--3, Corollaries 1--2, the stable-expansion lemma, examples, and the proofs actually supplied for Theorems 1 and 3 were inspected. The publisher proceedings pages were not independently inspected. | Freeze the original definition, terminology, theorem numbers, author-copy content, and supplied proof arguments. Keep the later NP classification separate, and do not describe the author copy as a publisher scan or claim publisher-specific page typography. |
| `N-c-025`, Feder--Vardi 1998 | **AUTHOR COPY AND COMPLETE PROOF BODY CLOSED; SIAM TYPESET COMPARISON OPEN** | Feder's live Stanford page supplies a complete 53-page first-party PostScript. The relational-girth definition, Theorem 5 and its proof on author-copy pp. 10--11, and Theorem 6 and its proof on author-copy pp. 12--13 were inspected. The source closes the random-copy/Markov/Cherno construction, the biconnected normalization, fresh-relation and hidden-occurrence steps, finite-template construction, exact reduction orientations, and connected-input qualification. SIAM exposes only the abstract, so journal-proof pagination and typesetting were not compared. | Reconstruct the complete author-copy arguments with author-copy locators. State deterministic Karp from MMSNP to CSP, randomized Turing from CSP to MMSNP, randomized Karp on connected CSP inputs, literal class nonidentity, and Kun's later derandomization. Do not describe the author file as a SIAM facsimile or assign its page numbers to the journal. |
| `N-c-026`, named Cook--Levin attribution | **PRIMARY RECORD ACQUIRED** | Math-Net identifies Levin's 1973 “Universal Sequential Search Problems,” supplies the full Russian text and English-translation metadata, and states the universal-search contribution in its abstract. | Use Levin for the independent historical attribution and the explicit modern source/handbook construction for the many-one SAT proof. |
| `N-c-026`, Papadimitriou 1994 | **THEOREM, LOCATOR, SYNTAX, AND REDUCTION CLOSED; FULL BODY OPEN** | Library of Congress closes identity. Google Books primary-text snippets independently confirm the p. 455 definition and contradiction, the p. 456 theorem/proof opening, and the p. 458 logspace/complement finish. Its volume is `noview`; no readable publisher or named-library body exposed the continuous p. 457 recurrence or p. 487 note. | State Theorem 19.1 on pp. 456--458 for existential-first, strict-alternation QSAT with a CNF matrix under deterministic logspace many-one reductions, preserving the p. 455 prose conflict. Qualify exact p. 457 and p. 487 wording and do not replace “was established in” by “first proof.” |
| `N-x-015`, Halpern 2003 | **OPEN, BLOCKING** | MIT Press, Library of Congress, and named-library records close the 2003 hardcover identity, while the qualified Dandelon contents scan closes Chapter 7's pp. 239--286 architecture only. The visible Internet Archive scan is conclusively the restricted 2005 paperback: its copyright-leaf OCR says `First MIT Press paperback edition, 2005`; the older exact-2003 identifier is dark. Cornell holds the exact 2003 copy and exposes a chapter-scan request route, but the copy is checked out through 2027-04-04 and no request or fulfilment was attempted. All body-level definitions, theorems, hypotheses, proofs, examples, and edition differences remain unread. | The mathematical linear-probability presentation is closed against Fagin--Halpern--Megiddo 1990, but the registered Halpern 2003 presentation is not source-closed. A lawful readable copy of Chapter 7, bound to the 2003 front matter, is required to finish the edition-specific audit. Do not substitute the revised 2005 paperback or the 2017 second edition. |
| `N-x-015`, Baier--Katoen 2008 for CTMC/CSL | **REFUTED SOURCE MATCH** | Chapter 10 has DTMC/MDP/PCTL/PCTL* and no CTMC/CSL. | Never attach CTMC/CSL claims to the 2008 book; use the distinct 2003 CTMC article. |
| `N-x-015`, Baier et al. 2003 | **ACQUIRED; LOCATORS CLOSED** | The institutional report was rendered manually and reconciled with the journal text: Definitions 1 and 3--6, Proposition 2, Corollary 1, Theorems 1--3, Section 4.3 equations (7)--(8), and Section 6. | Use the Poisson-tail truncation bound exactly as stated; separately bound retained-term/roundoff error and do not infer an exact equality decision from the numerical algorithm. |
| `D-P11-006`, concrete Prolog | **IDENTITY AND PUBLIC SCOPE CLOSED; CORRECTED FINAL CLAUSES OPEN** | ISO identifies edition 1 of ISO/IEC 13211-1:1995 as a current, confirmed 199-page standard and records Corrigenda 1:2007, 2:2012, and 3:2017. The public WG17 register identifies the 1993 committee draft and 1994 DIS as prepublication bodies; a current WG17 working page locates control constructs, cut, ordinary and occurs-check unification, arithmetic, and negation in separate clause groups. None exposes the corrected final normative clauses in this environment. | Attribute the pure SLD and common control account to the acquired logic-programming sources. State only the ISO identity and public scope; do not make clause-exact corrected-standard claims until the 1995 clauses and all applicable corrigenda are lawfully compared. |

Absence of a DOI is not itself an acquisition defect. No DOI was located for
Floyd 1967, Kowalski 1974, Gelfond--Lifschitz 1988,
Abiteboul--Hull--Vianu 1995, Papadimitriou 1994, Halpern 2003, or
Baier--Katoen 2008; each identity is instead tied above to an author,
institution, publisher, proceedings, ISBN, or primary facsimile.

## Minimum source-faithful reconstruction package

Before these rows can be called complete, the reader-facing material must
contain all of the following, with each theorem labelled `proved`, `proof
outline`, or `cited` rather than given one undifferentiated status:

1. partial and total Hoare rules, Dijkstra's termination-sensitive `wp`, Cook's
   relative-completeness hypotheses/proof spine, and Apt's language-fragment
   calibration;
2. exact heap satisfaction, small axioms, frame soundness, one symbolic
   execution, and one bi-abduction step, with the tools paragraph last;
3. regular-program PDL syntax and semantics, Fischer--Ladner closure, an
   exponential small-model proof, the test-free completeness boundary, and the
   exact EXPTIME theorem;
4. definite-program least-model/fixpoint semantics, SLD soundness and strong
   completeness, finite failure, Clark completion, SLDNF side conditions, and
   the Prolog control counterexample;
5. the exact Gelfond--Lifschitz reduct, zero/two-model examples, function-free
   NP representation, and syntax-indexed ASP complexity;
6. CQ canonical databases and the contravariant homomorphism theorem with both
   proof directions, followed by a separate recursive Datalog fixed-point and
   data/combined-complexity treatment;
7. fixed-template CSP-as-homomorphism, exact MMSNP syntax and standing, literal
   class nonidentity, Feder--Vardi's asymmetric reduction types with their
   connected-input qualification, Kun's later derandomization, and a
   theorem-status-only dichotomy pointer distinguishing the 1998 conjecture
   from both independent 2017 proofs;
8. Cook's historical reduction notion and tableau, a full QBF
   PSPACE-completeness proof, a polarity-correct `K/T/S4/S5` table, and the
   first-order validity recap;
9. McMillan's interpolation construction and finite-run invariants with
   `k>0`; and
10. separate probability-logic, finite-DTMC/PCTL, finite-MDP, and CTMC/CSL
    presentations, with every model class and numerical/measure hypothesis
    stated before its algorithm.

This research note records source evidence only. No manuscript, bibliography,
register, generator, test, TeX source, or PDF was changed, and no test or build
was run as part of this source-acquisition task.
