# P2b research: first-order new content

Status: source-backed research note for the Phase-4 P2b visit. This file is
evidence and calibration, not handbook prose. It does not assign handbook
status labels, create bibliography entries, or by itself satisfy a register
row.

## Evidence policy and scope

- **Source-verified** means that the claim is stated in the linked primary
  source or authoritative modern reference at the locator given.
- **Derived here** means that the claim follows by the displayed elementary
  argument from source-verified definitions/results. It may enter a handbook
  proof only if that argument is actually supplied in the annex.
- **Claim ceiling** is the strongest formulation licensed for P2b by both the
  evidence and the register treatment ceiling.
- **Do not claim** marks a tempting strengthening not licensed by the evidence
  or a statement whose truth depends on a convention that has not been fixed.

The live P2b depth rows covered here are `D-P3-001`--`D-P3-004`,
`D-P3-006`, `D-P3-011`, and `D-P3-012`. Two nearby rows are pointers only:
Robinson joint consistency is `D-P3-005`, homed in P3 at treatment E, and
many-sorted first-order logic is `D-P3-007`, homed in P2.4 at treatment E.
P2b must not mark either row done. Definitional-extension conservativity is
`D-P3-010`; it should be coordinated with Beth definability, but this note
does not enlarge its separately specified treatment.

The frozen v1.1 source remains normative for migrated results. In particular,
the clausal pipeline must preserve repairs `R-007` and `R-008`, and the
consolidated equality entry must preserve the exact congruence hypotheses at
`lem:equality-congruence`. External sources below calibrate the added content;
they do not authorize a status upgrade of migrated material.

## 1. Equality-free Hilbert FOL and the deduction theorem (`D-P3-001`, E)

### Exact supported presentation

The [Open Logic Project complete text, release 9620cc7
(2026-07-12)](https://builds.openlogicproject.org/open-logic-complete.pdf)
gives one fully explicit equality-free Hilbert presentation in Chapter 22:

- propositional axiom schemas, Definition 22.5, p. 336;
- quantifier axioms
  \(\forall x\,\psi\to\psi(t)\) and
  \(\psi(t)\to\exists x\,\psi\), Definition 22.7, p. 336, with \(t\)
  a closed term;
- the two eigenconstant quantifier rules, Definition 22.8, p. 336: from
  \(\psi\to\varphi(a)\) infer \(\psi\to\forall x\varphi(x)\), and from
  \(\varphi(a)\to\psi\) infer \(\exists x\varphi(x)\to\psi\), provided
  \(a\) occurs in neither the premise context \(\Gamma\) nor \(\psi\);
- modus ponens, Definition 22.6, p. 336;
- soundness, Theorem 22.36, pp. 345--346;
- completeness for sets of sentences, Theorem 23.20 and Corollary 23.21,
  p. 360 (the equality-free case uses the unquotiented term model; the
  identity case is treated separately by quotienting).

Identity is not part of that calculus: it is added only in Section 22.13,
pp. 346--347. Thus “equality-free” has exact standing here: the language and
derivations omit the logical identity predicate and its axiom schemas.

### Deduction theorem

**Source-verified.** Theorem 22.25, pp. 342--343, states

\[
  \Gamma\cup\{\varphi\}\vdash\psi
  \quad\Longrightarrow\quad
  \Gamma\vdash\varphi\to\psi .
\]

The quantifier-rule induction case explicitly requires its eigenconstant to
occur in neither \(\chi\), \(\varphi\), nor \(\Gamma\). The reverse
implication follows from weakening plus modus ponens, exactly as in the
propositional deduction theorem (Theorem 22.23, p. 341).

**Derived here.** For this exact calculus, combining the source theorem with
that one-step reverse implication gives the biconditional

\[
  \Gamma\cup\{\varphi\}\vdash\psi
  \quad\Longleftrightarrow\quad
  \Gamma\vdash\varphi\to\psi .
\]

### Claim ceiling and variant warnings

The E entry may display the axiom/rule inventory by reference to the calculus
sheet, state soundness/completeness only at the evidence status actually
supplied, and give an annex proof of the deduction theorem for that inventory.
It should explicitly say that the theorem is a metatheorem about finite
derivations, not another object-language axiom.

**Do not claim.** There is no side-condition-free “Hilbert FOL deduction
theorem” independent of rule choice. Presentations with a primitive
generalization rule usually require that the generalized variable not occur
free in the discharged assumption (and often not free in any surviving open
hypothesis). The Open Logic presentation instead builds freshness into its
eigenconstant rules. Copying its theorem while displaying a different rule
inventory would be unsupported. Likewise, its quantifier axioms are stated for
closed terms; do not silently generalize the schema to arbitrary terms without
the relevant free-for/substitution lemma.

## 2. Classical first-order tableaux and countermodels (`D-P3-002`, E)

Raymond M. Smullyan, *First-Order Logic* (Springer, 1968), develops
first-order analytic tableaux on pp. 52--65 and the “Fundamental Theorem of
Quantification Theory” on pp. 70--79. The stable edition is
[DOI 10.1007/978-3-642-86718-7](https://doi.org/10.1007/978-3-642-86718-7).
The Open Logic Project gives a second explicit rule reference in Chapter 21:
quantifier rules and tableau construction on pp. 308--320, derivability and
quantifiers on pp. 322--327, soundness on pp. 327--330, and separate identity
rules on p. 330.

### Calibrated theorem package

Fix a standard signed or negation-normal-form tableau calculus for closed
classical first-order formulas. A branch is **saturated** only when every
applicable decomposition and witness obligation required by that calculus has
been met. A construction is **fair** only when no persistent applicable
formula is postponed forever.

**Source-verified at the cited chapter/page level.** The analytic-tableau
fundamental theorem supports these two directions:

1. A finite closed tableau for \(\Gamma\cup\{\neg\varphi\}\) certifies
   \(\Gamma\models\varphi\) (local soundness of each rule).
2. If a fair systematic construction has a saturated open branch, the branch
   data determine a term-generated/Hintikka model satisfying the branch and
   therefore a countermodel to the root entailment.

For an unsatisfiable finite root, completeness yields a finite closed tableau.
For an arbitrary set of premises, strong completeness is a compactness-level
claim and must be stated with whatever finiteness/compactness step its proof
uses.

### Claim ceiling and variant warnings

The E entry may define branch, closure, saturation, fairness, and the model
extracted from an open saturated branch; display no rules in the body (the
rules belong in `registry/calculi/`); and state soundness plus completeness for
the exact sheet. The countermodel construction should identify its domain and
the interpretation of constants, functions, and predicates rather than say
only “read off a model.”

**Do not claim.**

- First-order tableau search is not a decision procedure for validity merely
  because every valid formula has a finite closed tableau. Fair search may run
  forever on an invalid or satisfiable input before exposing a usable limit
  branch.
- An arbitrary open but unsaturated branch need not determine a model.
- The extracted countermodel need not be finite. It is normally countable and
  term-generated when the language/construction is countable.
- Equality-free completeness does not establish completeness for a sheet with
  equality. Equality tableaux need extra rules; countermodel extraction then
  normally quotients branch terms by the generated equality congruence.
- Formulas with free variables require a declared parameter/universal-closure
  convention. Do not move between those variants tacitly.

## 3. Herbrand universe, base, structure, expansion, and theorem (`D-P3-003`, E)

### Definitions and standing

Let \(L\) be a first-order signature containing at least one constant. If it
does not, first pass to the conservative signature expansion \(L(c)\) by a
fresh constant \(c\). Define:

- the **Herbrand universe** \(HU_L\) as the set of all ground \(L\)-terms;
- the **Herbrand base** \(HB_L\) as the set of all ground atomic
  \(L\)-formulas (for the clean version below, excluding logical equality);
- a **Herbrand structure** as the structure with domain \(HU_L\), each
  constant interpreted by itself, and
  \(f^{\mathcal H}(t_1,\ldots,t_n)=f(t_1,\ldots,t_n)\), while each predicate
  is interpreted by an arbitrary chosen subset of the matching atoms in
  \(HB_L\);
- for quantifier-free \(A(\vec x)\), a finite **Herbrand expansion** as a
  disjunction \(A(\vec t_1)\lor\cdots\lor A(\vec t_m)\) of ground instances
  with \(\vec t_i\in HU_L^{|\vec x|}\).

Lewis gives the ground-term “seed” convention and an expansion theorem on
pp. 319--320 of “Complexity Results for Classes of Quantificational Formulas”
([DOI 10.1016/0022-0000(80)90027-6](https://doi.org/10.1016/0022-0000(80)90027-6)).
That paper uses a satisfiability/functional-form variant; it must not be cited
as if its terminology were already the validity-form statement below.

### Validity form

**Source-verified, hard direction.** Afshari, Enqvist, and Leigh state in
Section 1, p. 1008, that if the prenex \(\Sigma_1\) sentence

\[
  \exists\vec x\,A(\vec x)
\]

with quantifier-free matrix \(A\) is valid, then there are finitely many
ground term tuples \(\vec t_1,\ldots,\vec t_m\) such that

\[
  A(\vec t_1)\lor\cdots\lor A(\vec t_m)
\]

is propositionally valid. See “Herbrand schemes for first-order logic,”
*Archive for Mathematical Logic* 64 (2025), 1007--1076,
[DOI 10.1007/s00153-024-00959-w](https://doi.org/10.1007/s00153-024-00959-w).
Smullyan's fundamental theorem on pp. 70--79 supplies the classical analytic
background; Chapter 5 of Jacques Herbrand's thesis is available in English in
*Logical Writings*, ed. Warren D. Goldfarb (Reidel, 1971),
[DOI 10.1007/978-94-010-3072-4](https://doi.org/10.1007/978-94-010-3072-4).

**Derived here, easy converse.** If a finite ground disjunction is
propositionally valid, it is true under the truth assignment induced by every
first-order structure. Each disjunct is an instance of
\(\exists\vec x A(\vec x)\), so the existential sentence is valid. Thus the
usual equality-free validity form may be written as an iff once this elementary
converse is actually included.

### Clause-set corollary and forward link

For a universal equality-free clause set \(S\), the dual satisfiability form
says that \(S\) is unsatisfiable iff some finite collection of its ground
instances is propositionally unsatisfiable. This is the bridge to resolution,
but it is a corollary/variant, not a substitute for the required validity-form
entry.

### Claim ceiling and variant warnings

The E entry must give all four definitions above, the fresh-constant convention,
the validity theorem with its prenex \(\Sigma_1\) hypothesis, and a separate
sentence identifying the clause-set corollary.

**Do not claim.**

- “Every valid existential sentence has a single witnessing ground term” is
  false in classical logic; the theorem provides a finite disjunction.
- Do not omit the ground-term seed when the original signature has no constant.
- Do not conflate a Herbrand expansion (a finite disjunction in the validity
  form) with the full Herbrand base or with an infinite set of clause instances.
- In a syntactic Herbrand structure, the equality atom \(s=t\) is not
  automatically actual identity unless equality is treated separately. State
  the clean theorem equality-free, or supply the quotient/equality-axiom
  machinery. Do not quietly import the equality-free theorem into a clause set
  with logical identity.
- Skolemization expands the signature and preserves satisfiability, not
  formula-by-formula logical equivalence in the original signature.

## 4. Craig interpolation and Beth definability (`D-P3-004`, S)

### Craig interpolation: sentence form

**Source-verified.** The Open Logic Project, Theorem 27.4, p. 407, states: if
\(\models\varphi\to\psi\), there is a sentence \(\chi\) such that

\[
  \models\varphi\to\chi,
  \qquad
  \models\chi\to\psi,
\]

and every constant, function, and predicate symbol other than equality in
\(\chi\) occurs in both \(\varphi\) and \(\psi\). The primary paper is
William Craig, “Three Uses of the Herbrand--Gentzen Theorem in Relating Model
Theory and Proof Theory,” *Journal of Symbolic Logic* 22(3) (1957), 269--285,
[DOI 10.2307/2963594](https://doi.org/10.2307/2963594).

The empty-common-vocabulary edge case depends on the logical vocabulary and
nonempty-domain convention. The cited Open Logic proof uses
\(\exists x\,x\ne x\) and \(\exists x\,x=x\) as contradiction/tautology
interpolants and treats equality as logical, hence exempt from the shared
nonlogical-vocabulary restriction.

### Beth definability: predicate form

Let \(L\) omit the new \(n\)-ary predicate \(P\), and let \(T(P)\) be an
\(L\cup\{P\}\)-theory. Let \(P'\) be a fresh \(n\)-ary predicate and let
\(T(P')\) be obtained by uniform renaming.

**Source-verified definitions and theorem.** Open Logic Definitions 27.5 and
27.6 and Theorem 27.7, p. 410, give:

- implicit definability:
  \[
    T(P)\cup T(P')\models
    \forall\vec x\,(P(\vec x)\leftrightarrow P'(\vec x));
  \]
- explicit definability: there is an \(L\)-formula \(\theta(\vec x)\) such
  that
  \[
    T(P)\models
    \forall\vec x\,(P(\vec x)\leftrightarrow\theta(\vec x));
  \]
- Beth's theorem: implicit definability iff explicit definability.

The primary source is Evert W. Beth, “On Padoa's Method in the Theory of
Definition,” *Proceedings of the Koninklijke Nederlandse Akademie van
Wetenschappen*, Series A 56 (1953), 330--339, also printed as *Indagationes
Mathematicae* 15 (1953), 330--339,
[DOI 10.1016/S1385-7258(53)50042-3](https://doi.org/10.1016/S1385-7258(53)50042-3).
Do not attach DOI `10.2307/2268764`: that identifies William Craig's later JSL
review, not Beth's paper.

### Claim ceiling and variant warnings

P2b's S treatment permits exact statements, status labels, citations, and
forward references to P7 for proofs. It does not license annex proofs here.
Use the sentence form of Craig interpolation and the predicate form of Beth
definability displayed above.

**Do not claim.**

- Do not state the stronger Lyndon polarity theorem under Craig's name.
- Formula/free-variable and theory-to-theory interpolation variants require
  their own hypotheses; the sentence theorem does not state them verbatim.
- Beth definability is not the same as conservativity of a supplied explicit
  definition. Coordinate the latter with `D-P3-010` rather than merging the
  results.
- “Same reduct implies the same \(P\)” is acceptable prose only after specifying
  that the two structures are expansions of the same \(L\)-structure (or after
  giving the equivalent renamed-predicate formula above).

## 5. Robinson joint consistency: P2b pointer only (`D-P3-005`, P3/E)

**Source-verified formulation for the future P3 entry.** Let
\(L_0=L_1\cap L_2\), let \(T\) be a complete \(L_0\)-theory, and let
consistent \(L_i\)-theories \(T_i\) extend \(T\). Then
\(T_1\cup T_2\) is consistent. An equivalent separation formulation assumes
there is no \(L_0\)-sentence \(\theta\) with
\(T_1\models\theta\) and \(T_2\models\neg\theta\).

For an authoritative modern locator, see Boolos, Burgess, and Jeffrey,
*Computability and Logic*, 5th ed. (Cambridge University Press, 2007),
Chapter 20, pp. 260--269, especially Section 20.2,
[chapter DOI 10.1017/CBO9780511804076.021](https://doi.org/10.1017/CBO9780511804076.021).
The primary paper is Abraham Robinson, “A Result on Consistency and its
Application to the Theory of Definition,” *Proceedings of the Koninklijke
Nederlandse Akademie van Wetenschappen*, Series A 59 (1956), 47--58 (also
*Indagationes Mathematicae* 18),
[DOI 10.1016/S1385-7258(56)50008-X](https://doi.org/10.1016/S1385-7258(56)50008-X).

**P2b claim ceiling.** One pointer sentence only: “Robinson joint consistency
is stated and treated in Part 3.” Do not reproduce the theorem as a P2.2 entry
or mark `D-P3-005` done.

**Do not claim.** The loose phrase “\(T_1\cap T_2\) is complete” is safe only
when the intersection is explicitly a theory in the common language and
actually decides every common-language sentence. The complete common theory
form and the no-separating-sentence form should not be mixed mid-statement.

## 6. Decidable-fragment catalog (`D-P3-006`, T)

The table must place syntax/semantics and complexity in the same row. A bare
fragment name is not enough because adding equality, function symbols,
distinguished orders, transitive relations, counting, or changing finite to
arbitrary satisfiability can change the result. **Derived catalog synthesis:**
the rows below assemble the separately source-verified results in the
subsections that follow; they are not quotations from any single source.

| Fragment | Exact catalog scope supported here | Model/decision fact | Complexity claim ceiling | Primary locator |
|---|---|---|---|---|
| Monadic FO | Closed relational FO using only unary predicate symbols, no identity and no function symbols; constants may be treated as zero-ary functions only if the chosen source convention says so | Decidable; exponential-size type/model analysis | Satisfiability is NEXPTIME-complete and, more sharply, has matching nondeterministic bounds of the form \(c^{n/\log n}\) for different constants; validity is coNEXPTIME-complete by complement | Lewis 1980, statement of conventions p. 319, Theorem 4.1/Corollary 4.2 pp. 327--331 and Theorem 5.1 pp. 331--332 |
| \(\mathrm{FO}^2\) | Relational first-order sentences using at most two distinct variable symbols, reusable under quantifiers; with or without equality; no nonconstant function symbols | Finite-model property and an exponential model bound | Satisfiability is NEXPTIME-complete; therefore finite satisfiability has the same bound | Grädel--Kolaitis--Vardi 1997, Theorem 5.1 and Corollary 5.4, pp. 64--66 |
| Guarded fragment GF | Relational FO in which every quantified tuple is relativized by an atomic guard containing all variables free in the quantified formula | Decidable; tree-model property; GF has the finite-model property | General GF satisfiability is 2EXPTIME-complete; bounded-variable GF or GF over bounded-arity relation vocabularies is EXPTIME-complete | Grädel 1999, abstract and main results, pp. 1719--1742 |
| Bernays--Schönfinkel / EPR | Closed, function-free relational sentences in prenex \(\exists^*\forall^*\) form with quantifier-free matrix; Lewis's proved complexity convention omits identity | Finite-model property; after Skolemizing the leading existentials, only fresh constants are introduced | Satisfiability is NEXPTIME-complete | Lewis 1980, Theorem 7.1 pp. 333--337 and Theorem 8.1 p. 337 |
| Presburger arithmetic | The complete first-order theory of \((\mathbb N,0,1,+,<)\), or an explicitly intertranslated integer version; multiplication of variables is excluded | Decidable by quantifier elimination | Do not give a falsely tight class: classical bounds are a nondeterministic doubly-exponential lower bound and a deterministic triply-exponential upper bound | Presburger 1929/1930; Fischer--Rabin 1974, pp. 27--41; Oppen 1978, pp. 323--332 |

### Source-verified details

**Monadic and EPR.** Harry R. Lewis, “Complexity Results for Classes of
Quantificational Formulas,” *Journal of Computer and System Sciences* 21(3)
(1980), 317--353,
[DOI 10.1016/0022-0000(80)90027-6](https://doi.org/10.1016/0022-0000(80)90027-6),
states on p. 319 that the paper's object language has neither identity nor
function signs. The monadic lower and upper bounds are Theorem 4.1/Corollary
4.2 (pp. 327--331) and Theorem 5.1 (pp. 331--332). The
Schönfinkel--Bernays lower bound is Theorem 7.1 (pp. 333--337), and the upper
bound is Theorem 8.1 (p. 337).

This evidence licenses NEXPTIME-completeness for the specified EPR problem.
For monadic satisfiability it licenses both NEXPTIME-completeness and the
sharper matching \(c^{n/\log n}\)-type nondeterministic bounds (with different
constants in the lower and upper bounds). The corresponding validity problem
is coNEXPTIME-complete by the elementary complementation reduction; that last
sentence is a derived summary, not Lewis's theorem wording.

**Two variables.** Erich Grädel, Phokion G. Kolaitis, and Moshe Y. Vardi,
“On the Decision Problem for Two-Variable First-Order Logic,” *Bulletin of
Symbolic Logic* 3(1) (1997), 53--69,
[DOI 10.2307/421196](https://doi.org/10.2307/421196), defines the fragment as
relational sentences with at most two distinct variables, proves the
exponential model property (Theorem 5.1), and states NEXPTIME-completeness
with or without equality (Corollary 5.4, p. 66). The
[Project Euclid/DML record](https://dml.mathdoc.fr/item/1182353488/) is a
stable full-text locator.

**Guarded fragment.** Erich Grädel, “On the Restraining Power of Guards,”
*Journal of Symbolic Logic* 64(4) (1999), 1719--1742,
[DOI 10.2307/2586808](https://doi.org/10.2307/2586808), states that GF and
loosely guarded fragment satisfiability are deterministic double-exponential
time complete; bounded-variable or bounded-relation-arity subfragments are
EXPTIME-complete; and GF has the finite-model property. The table should list
GF, not silently transfer the claims to loosely guarded or guarded fixed-point
logic.

**Presburger arithmetic.** Mojżesz Presburger's original paper is “Über die
Vollständigkeit eines gewissen Systems der Arithmetik ganzer Zahlen, in
welchem die Addition als einzige Operation hervortritt,” in *Comptes-rendus du
I Congrès des Mathématiciens des Pays Slaves, Warszawa 1929*, pp. 92--101
(published 1930). An English translation with commentary by Dale Jacquette is
“On the Completeness of a Certain System of Arithmetic of Whole Numbers in
Which Addition Occurs as the Only Operation,” *History and Philosophy of
Logic* 12(2) (1991), 225--233,
[DOI 10.1080/014453409108837187](https://doi.org/10.1080/014453409108837187).
Fischer and Rabin, “Super-Exponential Complexity of Presburger Arithmetic,”
*SIAM--AMS Proceedings* 7 (1974), 27--41, prove a doubly-exponential lower
bound even for nondeterministic decision procedures. No DOI was verified for
the 1974 original; the authors' February 1974 Project MAC Technical Memorandum
43 has a stable [MIT DSpace record](https://dspace.mit.edu/handle/1721.1/148872).
Oppen, “A
\(2^{2^{2^{pn}}}\) Upper Bound on the Complexity of Presburger Arithmetic,”
*Journal of Computer and System Sciences* 16(3) (1978), 323--332,
[DOI 10.1016/0022-0000(78)90021-1](https://doi.org/10.1016/0022-0000(78)90021-1),
proves that Cooper's quantifier-elimination procedure has that deterministic
upper bound for some constant \(p>1\).

### Catalog-wide variant warnings

**Do not claim.**

- Lewis explicitly excludes identity and function signs. Do not append “with
  equality” to his monadic/EPR rows without another exact source. In
  particular, monadic logic with function symbols is not the same fragment.
- \(\mathrm{FO}^2\) counts distinct variable symbols, not quantifier depth,
  predicate arity, or the number of quantifier occurrences. Adding counting
  quantifiers, transitive relations, built-in orders, or nonconstant function
  symbols is a different result. If constants are admitted by convention, state
  the convention or the reduction that eliminates them rather than silently
  attributing that variant to the cited theorem.
- GF's guard must contain all variables relevant to the quantified subformula.
  Merely putting an arbitrary atom beside each quantifier is not the definition.
- EPR is \(\exists^*\forall^*\), not \(\forall^*\exists^*\), and it admits no
  nonconstant function symbols. Its Skolemization introduces constants only;
  that fact is load-bearing for the finite-model argument.
- Presburger arithmetic allows addition and order (with standard definitional
  variants) but no multiplication of two variables. Numeral encoding and the
  choice of \(\mathbb N\) versus \(\mathbb Z\) must be stated before quoting
  complexity bounds. Do not label the classical double/triple bounds a tight
  NEXPTIME- or 2EXPTIME-completeness result.

## 7. Many-sorted first-order logic: P2b pointer only (`D-P3-007`, P2.4/E)

### Calibrated future statement

A many-sorted signature assigns input/output sorts to function symbols and
argument sorts to predicates. A standard many-sorted structure gives each
sort a nonempty carrier, interprets symbols at their declared sorts, and lets
variables range over their declared carriers.

**Source-verified.** The Stanford Encyclopedia of Philosophy entry
[“Many-Sorted Logic,” Section 6.1](https://plato.stanford.edu/entries/logic-many-sorted/)
describes the reduction to one-sorted FOL: add a unary predicate \(Q_s\) for
each sort, relativize quantifiers, add nonemptiness axioms for the \(Q_s\), add
output-sort closure axioms for functions, and add sort-membership axioms for
constants. Consequence is preserved modulo this one-sorted background theory.
Maria Manzano,
*Extensions of First Order Logic* (Cambridge University Press, 1996), Chapter
VI, is the book-length source; pp. 240--257 cover calculus and completeness.
The [official CUP front matter](https://assets.cambridge.org/97805210/19026/frontmatter/9780521019026_frontmatter.pdf)
identifies Cambridge Tracts in Theoretical Computer Science 19, hardback ISBN
978-0-521-35435-6 and paperback ISBN 978-0-521-01902-6. No DOI for the book was
verified.

**P2b claim ceiling.** One pointer sentence only: “Many-sorted first-order
syntax, semantics, and the reduction to one-sorted logic are treated in
Section 2.4.” Do not mark `D-P3-007` done from P2b.

**Do not claim.** The translation is not just erasure of sort annotations.
Nonempty-sort axioms and symbol-typing/closure axioms are required. Empty-sort
semantics is a different convention. Sort predicates need not be asserted
disjoint, exhaustive, or a partition unless the selected many-sorted semantics
requires those properties; the standard reduction must match the stated
carrier convention.

## 8. Clausal-form pipeline (`D-P3-012`, S)

### Exact pipeline and preservation labels

For a closed first-order formula \(\varphi\), the standard refutational
pipeline is applied to \(\neg\varphi\) when the target is a validity proof:

1. eliminate \(\to\) and \(\leftrightarrow\), and push negations to atoms
   using the first-order quantifier dualities (**logical equivalence**);
2. standardize bound variables apart by a capture-avoiding alpha-variant
   (**logical equivalence**);
3. move quantifiers to a rectified prenex prefix, checking the free-variable
   side condition at every quantifier shift (**logical equivalence**);
4. replace each existential variable by a fresh Skolem function of exactly the
   preceding universal variables, then delete the existential quantifier
   (**assuming the Axiom of Choice, equisatisfiability across a signature
   expansion**, not equivalence; the reduct direction needs no choice);
5. delete the remaining universal prefix under the convention that clause
   variables are implicitly universally quantified;
6. distribute the quantifier-free matrix to CNF and read each conjunct as a
   clause (**logical equivalence** for the distributive transformation; clause
   semantics uses universal closure).

Assuming the Axiom of Choice in the ambient set theory, the result is a set
\(C\) of clauses in an expanded signature such that \(\neg\varphi\) is
satisfiable iff \(C\) is satisfiable. The direction from a model of \(C\) to
a model of the original-signature formula uses only reduct and needs no
choice. Hence, under the stated ambient assumption, \(\varphi\) is valid iff
\(C\) is unsatisfiable. For a theory or a formula with free variables, first
state whether universal closure, existential closure, or parameter semantics
is intended.

**Source-verified.** Baaz, Egly, and Leitsch, “Normal Form Transformations,”
in Robinson and Voronkov (eds.), *Handbook of Automated Reasoning*, vol. I
(Elsevier, 2001), 273--333,
[DOI 10.1016/B978-044450813-3/50007-2](https://doi.org/10.1016/B978-044450813-3/50007-2),
treats prenex/Skolem/CNF transformations and distinguishes refutational
clausal form; Section 6 begins the conjunctive-normal-form treatment, with
nonstructural versus structural transformations in Section 6.1. Lewis 1980,
pp. 319--320, independently records standardization apart, the dependency of
Skolem functions on preceding universal variables, the fresh-constant seed,
and the expansion theorem.

The frozen v1.1 source supplies the campaign-specific repaired proofs:
`lem:fol-nnf`, `lem:rectified-variant`, `lem:prenex-extraction`, and
`thm:prenex-normal-form` preserve `R-007`; `thm:skolem-equisatisfiable`
preserves `R-008`, including its explicit induction and its separation of the
choice-using direction from the choice-free one. The P2b statement must point
to those migrated results rather than compress them into an unproved
“routine conversion.”

### Claim ceiling and variant warnings

The S entry may display the six-stage table, its per-stage preservation
column, and the final equisatisfiability/unsatisfiability statement, with a
source/annex pointer. It need not prove every normal-form theorem again.

**Do not claim.**

- The original formula and its Skolemization are generally not logically
  equivalent in one signature.
- A Skolem function's arguments are not “all variables in the formula”; in the
  standard prenex construction they are exactly the preceding universal
  variables (subject to the precisely selected Skolemization variant).
- Quantifier movement is not unconditional: freshness/free-variable side
  conditions are load-bearing.
- Dropping universal quantifiers changes the written formula unless the
  implicit universal-closure convention for clauses is stated.
- For theorem proving one clausifies the negation of the conjecture together
  with the premises. Do not say the clauses are unsatisfiable iff the original
  conjecture is satisfiable.
- Structural/Tseitin-style clausification has a different preservation and
  signature story. Do not mix it into the displayed classical distributive
  pipeline without a separate theorem.

## 9. Equality congruence and equality-axiom metatheory (`D-P3-011`, E)

### Two presentations that must be kept distinct

**Hilbert axiom presentation.** Open Logic Definition 22.39, p. 347, adds to
its equality-free calculus the schemas

\[
  t=t,
  \qquad
  t_1=t_2\to\bigl(\psi(t_1)\to\psi(t_2)\bigr)
\]

for closed terms in that presentation. Proposition 22.41 states reflexivity
for any term, and Proposition 22.42 states replacement. This creates a scope
point that must be checked rather than hidden: Definition 22.39 literally says
“closed terms,” while Proposition 22.41 says “any term.” The displayed axiom
text safely licenses symmetry and transitivity at least for the terms admitted
by its schema; it does not, by itself, license an arbitrary-open-term schema.
In an alternative symbolwise axiomatization, replacement is decomposed into
congruence schemas for every function and predicate symbol. These are
equivalent metatheoretic packages only after the translation between them is
proved; the entry should choose one as normative and describe the other as a
variant.

**Quotient/term-model presentation from the verified source.** For a maximal
consistent, deductively closed \(\Delta\), define on terms

\[
  r\sim_\Delta t
  \quad\Longleftrightarrow\quad
  \Delta\vdash r=t.
\]

The frozen v1.1 `lem:equality-congruence` states with exact hypotheses:

- \(\sim_\Delta\) is an equivalence relation;
- if \(r_i\sim_\Delta t_i\) for every \(1\le i\le n\), then for every
  \(n\)-ary function symbol \(f\),
  \[
    f(r_1,\ldots,r_n)\sim_\Delta f(t_1,\ldots,t_n);
  \]
- for every \(n\)-ary relation symbol \(R\),
  \[
    R(r_1,\ldots,r_n)\in\Delta
    \quad\Longleftrightarrow\quad
    R(t_1,\ldots,t_n)\in\Delta.
  \]

The proof uses equality introduction for reflexivity, derived symmetry,
equality elimination for transitivity and argumentwise compatibility,
deductive closure to put the replaced formulas in \(\Delta\), and symmetry
for the reverse relation implication. This is exactly what makes the function
and relation interpretations on equivalence classes independent of chosen
representatives.

### Claim ceiling and variant warnings

The E entry may consolidate the equality axioms, derived symmetry and
transitivity, the free-standing congruence lemma, and the quotient
well-definedness consequence. Its status must match the migrated proof; do not
promote any source exercise or sketch merely because the combined entry reads
smoothly.

**Do not claim.**

- Formula-context replacement must be capture-avoiding, and the substituted
  term must be free for the displayed variable. The closed-term Open Logic
  schema does not by itself state an arbitrary-open-term version.
- Logical equality is interpreted as actual identity. An arbitrary equivalence
  relation in a structure is not logical equality unless one passes to a
  congruence quotient and proves the relevant invariance.
- Function compatibility alone does not prove predicate compatibility, and a
  one-way predicate replacement does not give the displayed biconditional
  without symmetry/reverse replacement.
- Equality tableau completeness, Herbrand reasoning with equality, and
  resolution/superposition with equality require additional machinery; the
  equality-free metatheorems in Sections 2 and 3 do not automatically extend.

## 10. Implementation checklist and unsupported formulations

Before handbook prose is written, each of the following should be mechanically
visible in the P2b artifacts:

1. The Hilbert sheet and deduction theorem name one and the same rule inventory,
   including its eigenconstant conditions.
2. The tableau sheet declares whether it is signed or NNF, equality-free or
   equality-aware, and what fairness/saturation policy licenses countermodel
   extraction.
3. The Herbrand entry defines universe, base, structure, and finite expansion
   before stating the theorem; it handles the no-constant case.
4. Craig and Beth are statements/citations only, with P7 forward references;
   neither gains an annex proof or a stronger status in P2b.
5. Robinson and many-sorted logic remain prose pointers to P3 and P2.4,
   respectively; their rows remain open until treated at their actual homes.
6. Every decidability-table row contains vocabulary, equality/function-symbol
   convention, finite/arbitrary-model convention where relevant, and the exact
   complexity target (satisfiability or validity).
7. The clausal pipeline labels every stage “equivalent” or “equisatisfiable”
   and preserves the `R-007`/`R-008` repaired side conditions.
8. The equality entry includes both directions of predicate compatibility and
   explains quotient well-definedness.

The following formulations are unsupported and should be rejected during
verification:

- “The FOL deduction theorem has no side conditions.”
- “A nonclosing first-order tableau terminates with a finite countermodel.”
- “Every open tableau branch is a countermodel.”
- “Herbrand's theorem says a valid existential has a ground witness.”
- “Skolemization preserves equivalence.”
- “All standard decidable FOL fragments are NEXPTIME-complete.”
- “Monadic FOL remains the same fragment when arbitrary functions are added.”
- “EPR is the \(\forall^*\exists^*\) prefix class.”
- “Presburger arithmetic is first-order arithmetic with multiplication.”
- “Many-sorted logic reduces by simply deleting sort annotations.”
- “An equivalence relation on terms is automatically a congruence.”

## 11. Source ledger

Only verified metadata are recorded. “No DOI verified” means exactly that; it
is a warning not to invent one.

1. **Open Logic Project.** *Open Logic Project: Complete*. Release `9620cc7`
   (2026-07-12). Chapter 21, pp. 308--331 (first-order tableaux); Chapter 22,
   pp. 334--347, especially Definitions 22.5, 22.7, 22.8, Theorems 22.25 and
   22.36, Definition 22.39, Propositions 22.41--22.42; Chapter 23,
   Theorem 23.20 and Corollary 23.21 p. 360; Chapter 27, Theorem 27.4 p. 407
   and Definitions 27.5--27.6/Theorem 27.7 p. 410.
   Official stable build:
   <https://builds.openlogicproject.org/open-logic-complete.pdf>.

2. **Smullyan, Raymond M.** *First-Order Logic*. Ergebnisse der Mathematik
   und ihrer Grenzgebiete, 2. Folge, vol. 43. Springer, 1968. XII + 160 pp.
   First-order analytic tableaux pp. 52--65; Fundamental Theorem of
   Quantification Theory pp. 70--79.
   DOI: <https://doi.org/10.1007/978-3-642-86718-7>.

3. **Herbrand, Jacques.** *Logical Writings*. Edited and translated by Warren
   D. Goldfarb. Synthese Historical Library 3. D. Reidel, 1971. IX + 312 pp.
   Herbrand's thesis, Chapter 5.
   DOI: <https://doi.org/10.1007/978-94-010-3072-4>.

4. **Afshari, Bahareh; Enqvist, Sebastian; Leigh, Graham E.** “Herbrand
   Schemes for First-Order Logic.” *Archive for Mathematical Logic* 64
   (2025), 1007--1076. Validity-form statement in Section 1, p. 1008.
   DOI: <https://doi.org/10.1007/s00153-024-00959-w>.

5. **Craig, William.** “Three Uses of the Herbrand--Gentzen Theorem in
   Relating Model Theory and Proof Theory.” *Journal of Symbolic Logic* 22(3)
   (1957), 269--285.
   DOI: <https://doi.org/10.2307/2963594>.

6. **Beth, Evert W.** “On Padoa's Method in the Theory of Definition.”
   *Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen*,
   Series A 56 (1953), 330--339; also *Indagationes Mathematicae* 15 (1953),
   330--339.
   DOI: <https://doi.org/10.1016/S1385-7258(53)50042-3>.

7. **Robinson, Abraham.** “A Result on Consistency and its Application to the
   Theory of Definition.” *Proceedings of the Koninklijke Nederlandse
   Akademie van Wetenschappen*, Series A 59 (1956), 47--58; also
   *Indagationes Mathematicae* 18.
   DOI: <https://doi.org/10.1016/S1385-7258(56)50008-X>.

8. **Boolos, George S.; Burgess, John P.; Jeffrey, Richard C.**
   *Computability and Logic*. 5th ed. Cambridge University Press, 2007.
   Chapter 20, “The Craig Interpolation Theorem,” pp. 260--269; Robinson joint
   consistency in Section 20.2.
   Chapter DOI: <https://doi.org/10.1017/CBO9780511804076.021>.

9. **Lewis, Harry R.** “Complexity Results for Classes of Quantificational
   Formulas.” *Journal of Computer and System Sciences* 21(3) (1980),
   317--353. Language convention p. 319; expansion definitions pp. 319--320;
   monadic Theorems 4.1 and 5.1, pp. 327--332; Schönfinkel--Bernays Theorem
   7.1 and Theorem 8.1, pp. 333--337.
   DOI: <https://doi.org/10.1016/0022-0000(80)90027-6>.

10. **Grädel, Erich; Kolaitis, Phokion G.; Vardi, Moshe Y.** “On the
    Decision Problem for Two-Variable First-Order Logic.” *Bulletin of
    Symbolic Logic* 3(1) (1997), 53--69. Theorem 5.1 and Corollary 5.4,
    pp. 64--66.
    DOI: <https://doi.org/10.2307/421196>;
    stable full-text record: <https://dml.mathdoc.fr/item/1182353488/>.

11. **Grädel, Erich.** “On the Restraining Power of Guards.” *Journal of
    Symbolic Logic* 64(4) (1999), 1719--1742.
    DOI: <https://doi.org/10.2307/2586808>.

12. **Presburger, Mojżesz.** “Über die Vollständigkeit eines gewissen Systems
    der Arithmetik ganzer Zahlen, in welchem die Addition als einzige
    Operation hervortritt.” In *Comptes-rendus du I Congrès des
    Mathématiciens des Pays Slaves, Warszawa 1929*, 92--101. Published 1930.
    No DOI verified for the original. English translation with commentary by
    Dale Jacquette, “On the Completeness of a Certain System of Arithmetic of
    Whole Numbers in Which Addition Occurs as the Only Operation,” *History
    and Philosophy of Logic* 12(2) (1991), 225--233.
    Translation DOI: <https://doi.org/10.1080/014453409108837187>.

13. **Fischer, Michael J.; Rabin, Michael O.** “Super-Exponential Complexity
    of Presburger Arithmetic.” In *Complexity of Computation*, SIAM--AMS
    Proceedings 7, American Mathematical Society, 1974, 27--41. No DOI
    verified for the original publication. Stable author technical-memo version:
    Project MAC Technical Memorandum 43 (February 1974),
    <https://dspace.mit.edu/handle/1721.1/148872>. A later reprint appears in
    *Quantifier Elimination and Cylindrical Algebraic Decomposition* (Springer
    Vienna, 1998), pp. 122--135,
    DOI <https://doi.org/10.1007/978-3-7091-9459-1_5>; that reprint DOI must not
    be assigned to the 1974 original without labeling the version.

14. **Oppen, Derek C.** “A \(2^{2^{2^{pn}}}\) Upper Bound on the Complexity
    of Presburger Arithmetic.” *Journal of Computer and System Sciences*
    16(3) (1978), 323--332.
    DOI: <https://doi.org/10.1016/0022-0000(78)90021-1>.

15. **Manzano, María.** *Extensions of First Order Logic*. Cambridge Tracts
    in Theoretical Computer Science 19. Cambridge University Press, 1996.
    Chapter VI; calculus and completeness pp. 240--257. ISBN
    978-0-521-35435-6 (hardback), 978-0-521-01902-6 (paperback). No DOI
    verified. Official front matter:
    <https://assets.cambridge.org/97805210/19026/frontmatter/9780521019026_frontmatter.pdf>.

16. **Manzano, María.** “Many-Sorted Logic.” *Stanford Encyclopedia of
    Philosophy*, first published 15 December 2022. Syntax/semantics in
    Section 1; reduction to one-sorted logic in Section 6.1.
    <https://plato.stanford.edu/entries/logic-many-sorted/>.

17. **Baaz, Matthias; Egly, Uwe; Leitsch, Alexander.** “Normal Form
    Transformations.” In J. Alan Robinson and Andrei Voronkov (eds.),
    *Handbook of Automated Reasoning*, vol. I. Elsevier, 2001, 273--333.
    DOI: <https://doi.org/10.1016/B978-044450813-3/50007-2>.

### Bibliography intake warning

The live bibliography already contains at least `BaazEglyLeitsch2001`,
`BoolosBurgessJeffrey2007`, `Manzano1996`, `FischerRabin1974`, `Craig1957`,
and `Smullyan1968`, but some records lack the richer locators recorded here.
The existing key `Robinson1956` is the book *Complete Theories*, not the 1956
joint-consistency article; the article therefore requires a distinct key and
must not overwrite that record. The existing `OpenLogic2026` record names the
older release `9f12419` (2026-05-25), whereas this note verified release
`9620cc7` (2026-07-12); finalization must reconcile that version metadata
explicitly. This note does not authorize direct edits to
`handbook/bib/handbook.bib`. Any missing entries or metadata must go through
the visit's intake file, be checked against this ledger, and be deduplicated by
work and key during finalization.
