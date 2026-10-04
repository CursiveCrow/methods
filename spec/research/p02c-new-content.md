# P02c Phase-4 new-content research: higher-order, many-sorted, free, and adjacent logics

## Scope and evidence policy

This note supplies source-truth evidence for the P2c work named in `spec/PHASE4-HANDOVER.md`. It covers:

1. the exact object language, semantics, rules, comprehension schema, choice schema, and completeness boundary needed for a displayed relational second-order calculus;
2. strict many-sorted first-order syntax and semantics and an exact reduction to one-sorted first-order logic;
3. the positive, negative, and neutral free-logic distinctions, including the limits of any common quantifier-rule or definite-description presentation;
4. short, honestly scoped pointers to \(L_{\omega_1\omega}\), generalized quantifiers, and the analytical hierarchy; and
5. the exact registered deliverables A-038, A-039, and A-091.

Evidence labels used below:

- **Source-verified** means the stated result or bibliographical fact was checked against the cited primary source or authoritative reference at the locator given.
- **Derived** means the formulation is a mathematical synthesis or consequence assembled for this handbook. It is not attributed verbatim to a cited source and must be proved or transparently reduced to a cited theorem.
- **Do not claim** marks a formulation that the located evidence does not support.

The frozen Part IX source is especially important here. Its pp. 81--91 reading of Henkin (1950) is correct: Henkin proves completeness for his own typed formula system under general semantics. That result does **not** automatically cover a newly assembled relational sequent sheet. The precise match obligations are therefore made explicit below.

## 1. Exact second-order target and the Henkin-completeness boundary

### 1.1 Source-verified theorem that may be cited

Henkin's paper studies a version of Church's simple theory of types, with typed variables, function application, functional abstraction, equality, extensionality, and a choice operator/axiom. The relevant source locators are:

- **Henkin (1950), pp. 81--83:** contrasts the standard interpretation with general models and specifies the formal system inherited from Church, including axioms 1--6, extensionality axiom 10, choice axiom 11, and rules I--VI.
- **Henkin (1950), pp. 83--84:** defines standard and general models by choosing domains at the types in such a way that interpretation of the formal operations is closed.
- **Henkin (1950), p. 85, Theorem 1:** every consistent set of closed formulas of that system has a general model whose domains are denumerable.
- **Henkin (1950), p. 88, Theorem 2:** a formula is a theorem of that system iff it is valid in the general sense.
- **Henkin (1950), p. 88, Theorem 3:** obtains the associated compactness consequence.
- **Henkin (1950), pp. 88--89:** explains which changes are required if choice, extensionality, or functional abstraction is removed. These are modifications of his typed system, not an identification with an arbitrary relational calculus.

Stable primary copy: [Henkin, *Completeness in the Theory of Types*](https://aaronxyliu.github.io/download/PL/Henkin.pdf). Stable record: [JSTOR 2266967](https://www.jstor.org/stable/2266967), DOI [10.2307/2266967](https://doi.org/10.2307/2266967).

Church's source fixes the typed antecedent even more sharply: [Church (1940), pp. 60--62](https://www.classes.cs.uchicago.edu/archive/2007/spring/32001-1/papers/church-1940.pdf) lists rules I--VI and discusses extensionality axiom 10 and choice axiom 11. In that system, definable predicates are supplied through typed functional abstraction. A relational comprehension schema added to a new sheet is therefore not literally one of Church's displayed rules.

The precise theorem safe to cite in prose is:

> **Henkin completeness for Henkin's 1950 typed system (source-verified).** For the typed formal system and proof notion fixed in Henkin (1950), validity in all of Henkin's general models coincides with theoremhood; equivalently, every consistent set of closed formulas has a general model (with the countability refinement stated in Theorem 1).

This citation must carry the scope phrase “for Henkin's typed system” or an equally explicit qualifier.

### 1.2 Exact relational language for the proposed displayed sheet

The following is a **derived proposed specification**. It is needed because Part IX uses a relational second-order language rather than Church--Henkin simple type theory.

Fix a relational second-order signature \(\Sigma\) with:

- object variables \(x,y,z,\ldots\);
- for each \(n\geq 1\), \(n\)-ary relation variables \(X^n,Y^n,Z^n,\ldots\);
- object constants and object function symbols, if the surrounding first-order sheet admits them;
- (n)-ary predicate constants (P^n); and
- object equality (=).

Object terms are the ordinary first-order terms. Atomic formulas are \(t=u\), \(P^n(t_1,\ldots,t_n)\), and \(X^n(t_1,\ldots,t_n)\). Formulas are closed under the handbook's classical connectives, object quantifiers \(\forall x,\exists x\), and relation quantifiers \(\forall X^n,\exists X^n\). There are no function variables, relation terms other than relation variables/constants, or relation equality. This last sentence is a standing restriction, not a notational convenience: adding any of those changes the language for which the calculus and semantics must be checked.

### 1.3 Full and Henkin semantics for exactly that language

For a nonempty object domain \(M\):

- under **full semantics**, an \(n\)-ary relation variable ranges over all of \(\mathcal P(M^n)\);
- under **relational Henkin semantics**, the structure supplies a nonempty family \(\mathcal R_n\subseteq\mathcal P(M^n)\) for every \(n\geq1\), and \(n\)-ary relation variables range over \(\mathcal R_n\).

Predicate constants receive elements of the matching \(\mathcal R_n\) in a Henkin structure. Satisfaction is Tarskian, with

\[
\mathcal M,s\models X^n(t_1,\ldots,t_n)
\quad\Longleftrightarrow\quad
(\llbracket t_1\rrbracket_s,\ldots,\llbracket t_n\rrbracket_s)\in s(X^n),
\]

and

\[
\mathcal M,s\models \forall X^n\varphi
\quad\Longleftrightarrow\quad
\mathcal M,s[X^n\mapsto R]\models\varphi
\text{ for every }R\in\mathcal R_n.
\]

Full semantics is the special case \(\mathcal R_n=\mathcal P(M^n)\) for every \(n\).

### 1.4 Exact additional sequent rules

The proposed sheet should state that it contains **all** rules and initial sequents of the handbook's fixed classical first-order sequent calculus with object equality, plus the four rules below. Otherwise “extends first-order logic” does not determine a calculus.

Let (U^n) be any relation variable or predicate constant of arity (n) that is free for (X^n) in (A), and let (Y^n) be a fresh relation variable of arity (n). Contexts are finite multisets, as on the inherited first-order sheet.

\[
\frac{A[U^n/X^n],\Gamma\Rightarrow\Delta}
     {\forall X^n A,\Gamma\Rightarrow\Delta}
\ (\forall^2L)
\qquad
\frac{\Gamma\Rightarrow\Delta,A[Y^n/X^n]}
     {\Gamma\Rightarrow\Delta,\forall X^n A}
\ (\forall^2R),
\]

where \(Y^n\notin FV(\Gamma,\Delta,\forall X^nA)\) in \((\forall^2R)\), and

\[
\frac{A[Y^n/X^n],\Gamma\Rightarrow\Delta}
     {\exists X^n A,\Gamma\Rightarrow\Delta}
\ (\exists^2L)
\qquad
\frac{\Gamma\Rightarrow\Delta,A[U^n/X^n]}
     {\Gamma\Rightarrow\Delta,\exists X^n A}
\ (\exists^2R),
\]

where \(Y^n\notin FV(\Gamma,\Delta,\exists X^nA)\) in \((\exists^2L)\). Capture-avoiding substitution and the inherited object-quantifier eigenvariable conditions remain in force.

These four rules quantify over members of the selected relation domains. They do not themselves ensure that a relation defined by a formula belongs to such a domain. That is the separate job of comprehension.

### 1.5 Exact comprehension and relational choice schemas

For every \(n\geq1\) and every formula \(\theta(x_1,\ldots,x_n,\bar p,\bar Q)\) of the exact relational language in which \(X^n\) is not free, include the universal closure of

\[
\exists X^n\,\forall x_1\cdots\forall x_n
\bigl(X^n(x_1,\ldots,x_n)\leftrightarrow
\theta(x_1,\ldots,x_n,\bar p,\bar Q)\bigr).
\tag{Comp}
\]

Here \(\bar p\) and \(\bar Q\) are the permitted object and relation parameters. Allowing arbitrary second-order \(\theta\) makes this the impredicative version. If the implementation intends only first-order, predicative, or parameter-free instances, it must say so; those are different schemas.

For every \(n\geq1\) and every formula \(\theta(\bar x,y,\bar p,\bar Q)\) in which the fresh \((n+1)\)-ary relation variable \(F^{n+1}\) is not free, include the universal closure of

\[
\begin{aligned}
&\forall\bar x\,\exists y\,\theta(\bar x,y,\bar p,\bar Q)\\
&\quad\to
\exists F^{n+1}\,\forall\bar x\,\exists y\,
\Bigl(F^{n+1}(\bar x,y)\land\theta(\bar x,y,\bar p,\bar Q)\\
&\hspace{47mm}\land
\forall z\bigl(F^{n+1}(\bar x,z)\to z=y\bigr)\Bigr).
\end{aligned}
\tag{Choice}
\]

This is graph choice in the relational language. It asserts an admissible single-valued selecting graph; it does not add function variables. Its necessity is exactly the requested distinction between definable relation comprehension and definable choice. Its standing is an axiom schema, not a motive, relation, or metalinguistic abbreviation. It is nonredundant with `(Comp)`: comprehension forms the relation defined by a given formula, whereas `(Choice)` selects one witness from every nonempty fibre, a step not supplied by comprehension alone in a choice-free metatheory. The distinction is used by the requested full/Henkin comparison and by any completeness statement for a sheet that actually includes choice.

Semantic qualifications:

- `(Comp)` is valid under full semantics.
- `(Choice)` is valid in full structures only relative to enough metatheoretic choice to select from the indicated family of nonempty fibres. A handbook working without such a background choice principle must not call it automatically full-valid.
- A relational Henkin model for this sheet must be restricted to families \(\mathcal R_n\) satisfying every eligible `(Comp)` instance and every eligible `(Choice)` instance. Merely requiring nonempty \(\mathcal R_n\subseteq\mathcal P(M^n)\) is too weak.

### 1.6 Precise completeness theorem the proposed sheet may state

There are two defensible routes. They must not be conflated.

#### Route A: direct definition by a many-sorted reduction

Translate the relational language into many-sorted first-order logic with one object sort (o), one relation sort (r_n) for each arity, and an incidence predicate

\[
\(E_n:r_n\times o^n\).
\]

Translate \(X^n(t_1,\ldots,t_n)\) to \(E_n(X^n,t_1,\ldots,t_n)\), commute with connectives and object quantifiers, and translate a relation quantifier to the matching first-order sorted quantifier. Translate all `(Comp)` and `(Choice)` instances as sorted first-order sentences. If derivability for the proposed sheet is **defined** by derivability of this translated many-sorted theory in a fixed sound and strongly complete many-sorted calculus, then the following is a **derived theorem by definition plus satisfaction preservation**:

\[
\Gamma\vdash_{\mathrm{sheet}}\varphi
\quad\Longleftrightarrow\quad
\Gamma\models_{\mathrm{Henkin}+\mathrm{Comp}+\mathrm{Choice}}\varphi.
\tag{HC}
\]

This route is exact but does not produce an independently justified native rule sheet; the displayed native rules are then explanatory projections of the sorted calculus.

#### Route B: a native second-order rule sheet

If derivability is instead generated by the inherited first-order sequent rules, the four displayed second-order rules, and zero-premise instances of `(Comp)` and `(Choice)`, `(HC)` is **not yet source-verified**. To mark it `status=sketched`, the annex must supply:

1. the exact translation just defined;
2. a satisfaction lemma in both directions between relational Henkin models and the matching many-sorted structures;
3. a proof that every native rule translates to a derivable sorted inference;
4. the converse deductive-correspondence argument, or a conservative-equivalence result strong enough to recover native derivability; and
5. an explicit statement that the model class satisfies exactly the same eligible comprehension and choice instances as the calculus.

Only after items 1--5 may `(HC)` be stated for the new sheet. It should then be cited as a **derived handbook theorem**, with Henkin (1950), Manzano (1996), and the annex proof cited as antecedents. It should not be written `status=cited` with `Henkin1950` as though Henkin printed this relational sequent calculus.

### 1.7 Unsupported second-order formulations and overclaim risks

- **Do not claim:** “Henkin (1950) proves completeness of `registry/calculi/sol.tex`.” The paper proves completeness for its own typed system.
- **Do not claim:** “The four second-order quantifier rules are complete for full semantics.” Full second-order validity has no sound recursively axiomatized complete calculus in an effective language.
- **Do not claim:** arbitrary substitution of a formula for a relation variable as a quantifier rule. In the language above, relation quantifiers instantiate with admissible relations represented by relation variables/constants; formula-defined relations require `(Comp)`.
- **Do not claim:** arbitrary relational Henkin families suffice. Closure/satisfaction of the chosen schema instances is part of the model class.
- **Do not claim:** `(Choice)` is valid in full semantics without declaring the required metatheoretic choice principle.
- **Do not claim:** dropping extensionality, choice, functional abstraction, relation equality, or function variables leaves “the same Henkin theorem.” Henkin pp. 88--89 describes proof changes, not automatic invariance.
- **Do not claim:** categorical full second-order arithmetic plus Henkin completeness yields a complete categorical proof system. The semantics differ.

## 2. Many-sorted first-order logic and exact one-sorted reduction

### 2.1 Strict syntax

The following formulation is **source-verified in substance** against Manzano and Aranda, SEP §§1.2--1.5, and **derived in notation** for this handbook.

A strict many-sorted signature is \(\Sigma=(S,F,R,\operatorname{tp})\), where \(S\) is a nonempty set of sorts; each function symbol has a type

\[
f:s_1\times\cdots\times s_n\to s;
\]

each relation symbol has a type

\[
R:s_1\times\cdots\times s_n;
\]

and each constant is a nullary function \(c:\to s\). For each sort \(s\), take a disjoint stock of variables \(x^s,y^s,\ldots\).

Terms are formed by type: a variable of sort \(s\) and a constant of sort \(s\) are terms of sort \(s\); if \(t_i\) has sort \(s_i\), then \(f(t_1,\ldots,t_n)\) has sort \(s\). Atomic formulas are \(R(t_1,\ldots,t_n)\) with the indicated argument sorts and \(t=u\) for terms of the same sort. Formulas close under the classical connectives and sorted quantifiers \(\forall x^s\) and \(\exists x^s\).

This fixes same-sort equality. A liberal equality comparing different sorts or liberal relation symbols is another legitimate convention, but it is not the convention reduced below unless additional clauses are supplied.

### 2.2 Semantics

A strict \(\Sigma\)-structure \(\mathcal M\) consists of:

- a nonempty domain \(M_s\) for each \(s\in S\), taken pairwise disjoint for the strict presentation;
- \(f^{\mathcal M}:M_{s_1}\times\cdots\times M_{s_n}\to M_s\);
- \(R^{\mathcal M}\subseteq M_{s_1}\times\cdots\times M_{s_n}\); and
- \(c^{\mathcal M}\in M_s\) for each \(c:s\).

An assignment sends each variable of sort (s) to (M_s). Terms are evaluated compositionally. Atomic satisfaction is membership in the typed relation, equality is genuine identity, Boolean clauses are classical, and

\[
\mathcal M,g\models\forall x^s\varphi
\Longleftrightarrow
\mathcal M,g[x^s\mapsto a]\models\varphi
\text{ for every }a\in M_s,
\]

with the existential dual. Manzano and Aranda §1.4 explicitly distinguishes strict (disjoint) from lax domains; §1.5 gives the sort-respecting assignment and satisfaction clauses. Stable authoritative entry: [Manzano and Aranda, “Many-Sorted Logic,” Winter 2022](https://plato.stanford.edu/archives/win2022/entries/logic-many-sorted/).

### 2.3 Exact one-sorted translation

Extend the one-sorted signature by a unary predicate \(Q_s\) for each sort \(s\in S\). Retain the same nonlogical symbols, now untyped. Define \(\tau\) on well-sorted formulas by leaving atomic formulas and Boolean connectives unchanged and setting

\[
\begin{aligned}
\tau(\forall x^s\varphi)&:=
\forall x\bigl(Q_s(x)\to\tau(\varphi)\bigr),\\
\tau(\exists x^s\varphi)&:=
\exists x\bigl(Q_s(x)\land\tau(\varphi)\bigr).
\end{aligned}
\]

Let \(\Pi_\Sigma\) contain:

\[
\exists x\,Q_s(x)
\quad(s\in S),
\tag{Nonempty}
\]

\[
Q_s(c)
\quad(c:s),
\tag{Constants}
\]

and, for every \(f:s_1\times\cdots\times s_n\to s\),

\[
\forall x_1\cdots\forall x_n
\left(\bigwedge_{i=1}^n Q_{s_i}(x_i)
\to Q_s(f(x_1,\ldots,x_n))\right).
\tag{Closure}
\]

For the strict/disjoint convention also include

\[
\forall x\,\neg(Q_s(x)\land Q_t(x))
\qquad(s\ne t).
\tag{Disjoint}
\]

No relation-typing axiom is needed merely to preserve truth of translations of well-sorted formulas: translated relation atoms are only ever fed elements already guarded into the correct sorts. Adding

\[
\forall\bar x\bigl(R(\bar x)\to\bigwedge_iQ_{s_i}(x_i)\bigr)
\]

is harmless and useful if the one-sorted expansion itself is meant to encode *only* typed tuples, but it is stronger than the minimum reduction theory and should be labelled as an encoding convention.

Given a strict many-sorted \(\mathcal M\), construct \(\mathcal M^\flat\) on the tagged union \(\bigsqcup_s M_s\), interpret \(Q_s\) by the \(s\)-tagged component, and extend typed functions arbitrarily off their typed inputs. Conversely, from any one-sorted \(\mathcal N\models\Pi_\Sigma\), take \(M_s=Q_s^{\mathcal N}\), restrict functions and relations to typed inputs, and use the closure axioms to ensure the restricted functions have the correct codomains. Induction on terms and formulas yields

\[
\mathcal M,g\models_{\mathrm{MS}}\varphi
\quad\Longleftrightarrow\quad
\mathcal M^\flat,g^\flat\models_{\mathrm{FOL}}\tau(\varphi).
\tag{Truth preservation}
\]

For sets of sentences \(\Gamma\cup\{\varphi\}\), the exact consequence statement is

\[
\Gamma\models_{\mathrm{MS}}\varphi
\quad\Longleftrightarrow\quad
\Pi_\Sigma\cup\tau[\Gamma]
\models_{\mathrm{FOL}}\tau(\varphi).
\tag{MS--FOL reduction}
\]

This is **derived**, with the standard construction source-verified at Manzano and Aranda §6.1 and historically in Wang (1952). It is strong enough to transfer soundness, completeness, compactness, and Löwenheim--Skolem results, subject to the ordinary signature/cardinality qualifications.

### 2.4 Many-sorted overclaim risks

- **Do not omit** `(Nonempty)` if the sorted semantics requires every sort to be nonempty.
- **Do not omit** `(Closure)` when the language has function symbols.
- **Do not mix** strict disjoint domains with a lax/overlapping reconstruction without saying which convention is in force.
- **Do not state** the consequence equivalence as \(\tau[\Gamma]\models\tau(\varphi)\); the sort axioms \(\Pi_\Sigma\) are essential.
- **Do not infer** a native many-sorted derivation correspondence from semantic truth preservation alone. A proof-system correspondence is a second lemma.

## 3. Free-logic variants and definite descriptions at S/table ceiling

### 3.1 Scope ceiling

The handover gives free logic depth `S`, while N-b-010 is homed in P8. P2c should therefore provide the A-091 comparison table and a precise pointer, not a standalone free-logic calculus or a claim to close the P8 entry. The authoritative overview is [Gratzl, Pavlović, and Nolt, “Free Logic,” Summer 2025](https://plato.stanford.edu/archives/sum2025/entries/logic-free/), especially §§1.1--1.3, 2.1--2.3, 3.3--3.5, and 5.1.

### 3.2 Common outer/inner-domain presentation

For the table only, fix a bivalent outer-domain presentation when applicable: a total stock \(D=D_i\cup D_o\), with \(D_i\ne\varnothing\) the inner domain of existing objects over which \(\forall,\exists\) range, and \(D_o\) the possible values of non-denoting/nonexisting terms. Let

\[
E!(t)\quad\Longleftrightarrow\quad \llbracket t\rrbracket\in D_i.
\]

This is one standard semantic presentation, not a definition of all free logics. Partial-term presentations and neutral many-valued semantics require their own clauses.

The guarded forms common to standard positive and negative presentations are:

\[
\forall x\,A\ \land\ E!(t)\ \to\ A[t/x],
\qquad
A[t/x]\ \land\ E!(t)\ \to\ \exists x\,A,
\]

with the usual capture and eigenvariable restrictions for their rule versions. The guard records that quantifiers range over (D_i), not every possible term value.

### 3.3 Exact A-091 comparison content

The following table is a **derived synthesis** of the source distinctions; it is not a quotation and should not be presented as three uniquely determined calculi.

| Variant | Atomic formula containing a term whose value is outside (D_i) | Existence/quantifier discipline | Additional proof-theoretic commitment | Definite-description ceiling |
|---|---|---|---|---|
| Positive free logic | May be true or false; predicate extensions can include outer-domain objects. | Quantifiers range over \(D_i\); instantiation and existential introduction are guarded by \(E!\). | Identity involving nonexistents may be true, depending on the selected identity/term semantics. No blanket atomic strictness rule. | Russellian or Lambertian description principles may be added, but are not forced by positivity. In particular, a Russell-style biconditional for \(F(\iota xA)\) is an added commitment because positive atoms with a failed description need not be false. |
| Negative free logic | Every ordinary atomic formula with a nonexisting term is false. | Same inner-domain quantifier discipline. Common systems define \(E!(t)\leftrightarrow t=t\). | Atomic strictness, schematically \(P(t_1,\ldots,t_n)\to\bigwedge_iE!(t_i)\), plus the corresponding strict identity principle. | Lambert's law makes a failed description nonexisting; Russell-style truth conditions then fit the negative treatment, subject to the exact description axioms chosen. |
| Neutral free logic | Such an atom has a truth-value gap or a third value rather than being simply true or false. | Quantification still requires a stated range, but the classical guarded formulas do not by themselves determine consequence. | One must choose a truth scheme (for example weak or strong Kleene) and a matching proof theory; the SEP surveys bisequent treatments. | Description formulas inherit the selected gap/third-value policy. There is no single neutral description table until the truth tables and consequence relation are fixed. |

The exact status sentence should be: positive, negative, and neutral free logics are **families distinguished first by their treatment of atomic formulas containing empty/nonexisting terms**; further choices about identity, equality, quantification, connectives, and descriptions determine particular systems.

### 3.4 Definite descriptions: formulas safe to display

Two different packages must remain visibly distinct.

The Russellian contextual conditions sampled in SEP §5.1 are represented by:

\[
E!(\iota xA(x))
\leftrightarrow
\exists x\bigl(A(x)\land\forall y(A(y)\to y=x)\bigr),
\tag{R1}
\]

and, when adopted,

\[
F(\iota xA(x))
\leftrightarrow
\exists x\bigl(A(x)\land\forall y(A(y)\to y=x)\land F(x)\bigr).
\tag{R2}
\]

Lambert's law is:

\[
\forall x\left(
x=\iota yA(y)
\leftrightarrow
\forall y\bigl(A(y)\leftrightarrow y=x\bigr)
\right).
\tag{LL}
\]

`(R1)`, `(R2)`, and `(LL)` are theory-forming principles, not consequences of the three variant labels alone. Russell (1905) is the primary source for contextual analysis of descriptions; Lambert (1967), Bencivenga (1986), and Lehmann (2002) are the requested free-logic sources. The table should cite the modern SEP overview for the exact cross-variant comparison and cite the primary/historical items for lineage.

### 3.5 Free-logic overclaim risks

- **Do not identify** free logic with first-order logic allowing an empty quantifier domain. Free logic concerns empty/non-denoting singular terms; inclusive empty-domain logic is a separate variation.
- **Do not say** positive atoms containing empty terms are true. They may be true; positivity permits rather than requires this.
- **Do not say** neutral free logic is simply a third bivalent option. It requires a specified gap/many-valued consequence treatment.
- **Do not give** one unqualified quantifier calculus for all three rows.
- **Do not treat** `(R2)` or `(LL)` as constitutive of every free logic.
- **Do not mark** N-b-010 complete from a P2c summary table; its registered home is P8.

## 4. Minimal pointer statements for adjacent extensions

These statements are intentionally short because their registered homes are P3 or P4. Each defines only enough to prevent a misleading pointer.

### 4.1 \(L_{\omega_1\omega}\): P3 pointer

**Source-verified definition.** \(L_{\omega_1\omega}\) extends first-order logic by permitting conjunctions and disjunctions indexed by countable sets of formulas, while every string of consecutive quantifiers is finite and every formula has only finitely many free variables in the standard formation discipline. Scott's title states the central boundary exactly: “denumerably long formulas and finite strings of quantifiers.” Primary record: [Scott (1965), chapter DOI 10.1016/B978-0-7204-2233-7.50036-8](https://doi.org/10.1016/B978-0-7204-2233-7.50036-8).

**Safe pointer sentence.** \(L_{\omega_1\omega}\) permits countable Boolean combinations but only finite quantifier strings; it fails ordinary compactness, admits Scott sentences characterizing countable structures among countable models, and has proof theories with genuinely infinitary apparatus. See Scott (1965) and Karp (1964); the P3 entry must state the exact proof system before attaching any completeness claim.

**Derived compactness witness.** In a language with \(P_n\) for \(n<\omega\), the set

\[
\left\{\bigvee_{n<\omega}P_n\right\}\cup
\{\neg P_n:n<\omega\}
\]

is finitely satisfiable but not satisfiable. This is enough for an S-level warning.

**Do not claim:** Karp's completeness work gives an ordinary finitary, effective, strongly complete calculus or restores compactness. Any P3 completeness statement must name Karp's exact infinitary derivations and semantic target.

### 4.2 Generalized quantifiers: P3 pointer

**Derived standard definition, source-verified in lineage.** A unary generalized quantifier \(Q\) assigns to each nonempty domain \(M\) an isomorphism-invariant class \(Q_M\subseteq\mathcal P(M)\), with

\[
\mathcal M,s\models Qx\,\varphi
\quad\Longleftrightarrow\quad
\{a\in M:\mathcal M,s[x\mapsto a]\models\varphi\}\in Q_M.
\]

For example, ordinary \(\exists\) takes the nonempty subsets; the quantifier “there exist uncountably many” takes the uncountable subsets. Higher-type generalized quantifiers require an explicitly given tuple of arities and a corresponding isomorphism-invariant class of relations; “generalized quantifier” alone does not determine one semantics.

**Safe pointer sentence.** Generalized-quantifier logics extend first-order formation and satisfaction by a specified isomorphism-invariant quantifier (Q); their compactness, Löwenheim--Skolem, axiomatizability, and completeness behavior depends on (Q). See [Mostowski (1957)](https://doi.org/10.4064/fm-44-1-12-36), [Lindström (1966)](https://doi.org/10.1111/j.1755-2567.1966.tb00600.x), and Keisler's special study of “there exist uncountably many,” [DOI 10.1016/S0003-4843(70)80005-5](https://doi.org/10.1016/S0003-4843(70)80005-5).

**Do not claim:** Keisler's theorem for the uncountability quantifier is a completeness theorem for arbitrary generalized quantifiers. **Do not claim:** all generalized-quantifier extensions lose or preserve the same metatheorems.

### 4.3 Analytical hierarchy: P4 pointer

**Derived standard definition, supported by the existing Kleene/Rogers/Moschovakis sources.** A lightface analytical-hierarchy formula is a formula of second-order arithmetic placed in prenex form with respect to set/function quantifiers and with an arithmetical matrix. For \(n\geq1\):

- \(\Sigma^1_n\) begins with an existential second-order block and has \(n\) alternating second-order blocks;
- \(\Pi^1_n\) begins with a universal second-order block and has \(n\) alternating second-order blocks;
- first-order number quantifiers may occur in the arithmetical matrix and do not raise the superscript level.

Lightface classes do not permit arbitrary real/set parameters; boldface \(\boldsymbol\Sigma^1_n,\boldsymbol\Pi^1_n\) do. Effective analytical classes must not be silently identified with the boldface projective pointclasses.

**Safe pointer sentence.** The analytical hierarchy classifies second-order-arithmetic definitions by alternations of set/function quantifiers over an arithmetical matrix; distinguish lightface effective classes from boldface classes with real parameters. The full table and any diagram belong in P4 (D-P9-002, A-048, A-125), with Kleene (1952), Rogers (1967), and Moschovakis (2009) as the existing source spine. Official current book record: [AMS, *Descriptive Set Theory*, 2nd ed.](https://www.ams.org/books/surv/155/), DOI [10.1090/surv/155](https://doi.org/10.1090/surv/155).

**Do not claim:** a lightface \(\Sigma^1_1\) set is the same object as a boldface analytic subset of an arbitrary Polish space. **Do not claim:** number-quantifier alternations generate the superscript levels.

## 5. Exact apparatus data and implementation-ready table content

### 5.1 Registry data, transcribed exactly

The following values were checked directly in `spec/registers/apparatus.csv`:

| ID | source line | category | item | exact specification | priority | effort | phase | current status |
|---|---:|---|---|---|---|---|---:|---|
| A-038 | 39 | table | Table: extensions of first-order logic | Many-sorted, free, infinitary, generalized-quantifier, and second-order extensions with the Lindström-theorem calibration of which metatheorems survive. | should | M | 4 | open |
| A-039 | 40 | table | Table: full versus Henkin second-order semantics | Comparison of completeness, compactness, Löwenheim--Skolem, and categoricity, resolving the D2 source gap. | must | S | 4 | open |
| A-091 | 92 | table | Table: free-logic variants | Positive, negative, and neutral variants with existence predicate, quantifier rules, and definite-description treatment. | should | S | 4 | open |

No implementation may silently narrow A-038 to only SOL, or A-091 to only positive/negative bivalent systems.

### 5.2 A-038: exact row content

The table below is a **derived synthesis**. The Lindström calibration must remain qualified: Lindström's theorem applies to abstract logics satisfying its regularity hypotheses, not to any arbitrary notation called an “extension.” Existing key `Lindstrom1969` is the relevant calibration source; stable DOI [10.1111/j.1755-2567.1969.tb00356.x](https://doi.org/10.1111/j.1755-2567.1969.tb00356.x).

| Extension/semantics | Added resource | Compactness | Löwenheim--Skolem calibration | Completeness/axiomatization | What the table may conclude |
|---|---|---|---|---|---|
| Strict many-sorted FOL | Typed variables, domains, functions, relations | Preserved via the exact one-sorted reduction | Ordinary cardinal-qualified downward/upward results transfer | Sound and strongly complete via reduction | This is a disciplined presentation of FOL-level expressivity, not a counterexample to Lindström. |
| Free logic | Empty/non-denoting terms with a chosen positive, negative, or neutral treatment | System-dependent until semantics/consequence are fixed | System-dependent | System-dependent; no single row-wide calculus | It is not one abstract logic merely by being called free logic; identify the chosen variant before metatheorems. |
| \(L_{\omega_1\omega}\) | Countable conjunctions/disjunctions, finite quantifier strings | Fails | Scott-style countable-model phenomena replace the ordinary blanket statement; state exact theorem in P3 | Infinitary proof systems exist; not ordinary finitary strong completeness | Greater formula length buys expressive power at the cost of compactness. |
| \(\mathrm{FOL}(Q)\) | A specified generalized quantifier | Depends on \(Q\) | Depends on \(Q\); the uncountability quantifier already defeats downward-to-countable behavior | Depends on \(Q\) | Never generalize a theorem for one \(Q\) to all generalized quantifiers. |
| Full relational SOL | Relation quantifiers range over all \(\mathcal P(M^n)\) | Fails | Both blanket downward and upward LS fail, as categorical infinite structures witness | No sound recursively axiomatized complete calculus for full validity in an effective language | Full semantics yields genuine categorical characterizations but loses the FOL package. |
| Henkin relational SOL with matched closure schemas | Relation quantifiers range over selected \(\mathcal R_n\), with the stated comprehension/choice instances | Preserved for an exactly matched finitary many-sorted presentation | FOL-style cardinal-qualified results transfer | Strongly complete only for an exactly matched calculus/model class | The FOL metatheorems return because the semantics has become many-sorted/model-relative; full categoricity does not. |

Safe Lindström caption sentence:

> Under the hypotheses of Lindström's abstract characterization, no regular extension of first-order logic is strictly more expressive while retaining both compactness and the downward Löwenheim--Skolem property; the rows show which assumption or metatheorem changes, but do not substitute for checking the theorem's hypotheses.

### 5.3 A-039: exact row content

| Property | Full relational second-order semantics | Henkin relational semantics with matched schemas |
|---|---|---|
| Relation-quantifier range | All \(\mathcal P(M^n)\) | Selected nonempty \(\mathcal R_n\subseteq\mathcal P(M^n)\) |
| Comprehension | Valid automatically | Must be imposed as closure/satisfaction of the eligible `(Comp)` instances |
| Choice | Valid only relative to adequate metatheoretic choice | Must be imposed by the eligible `(Choice)` instances/selector closure |
| Completeness | No sound recursively axiomatized complete calculus for full validity in an effective language | Strong completeness for an exact matched presentation, by an exact many-sorted reduction or a proved native deductive correspondence |
| Compactness | Fails | Holds for the finitary matched first-order presentation |
| Downward Löwenheim--Skolem | Fails in general; categorical infinite characterizations obstruct it | FOL-style version holds with the normal language/cardinality qualifications |
| Upward Löwenheim--Skolem | Fails in general; categorical infinite characterizations obstruct it | FOL-style version holds with the normal infinite-model/cardinality qualifications |
| Categoricity | Can categorically characterize, for example, the intended natural-number structure with full second-order induction | The same written axioms need not be categorical; nonstandard Henkin models remain |

Required caption qualification:

> “Complete” in the Henkin column is about the exact calculus paired with the exact selected-domain semantics; it is not completeness for full second-order validity.

### 5.4 A-091: exact row content

Use the table in §3.3, with the common guarded formulas and `(R1)`/`(R2)`/`(LL)` immediately below it. That layout meets the registered requests for existence predicate, quantifier rules, and definite descriptions without falsely promoting an S-level comparison into three complete calculi.

## 6. Register ownership and closure limits

Relevant registered rows and the maximum honest P2c action are:

| Row | Registered home/depth | P2c action supported by this note |
|---|---|---|
| N-a-071 / D-P9-001 | P2, `E` | Implement the exact SOL/Henkin entry and displayed sheet, but only with the match proof/defined reduction in §1.6. |
| D-P3-007 | P2.4, `E` | Implement the many-sorted syntax, semantics, exact reduction, and consequence theorem in §2. |
| D-P3-008 | P2.4 pointer to P8, `S` | Add only the free-logic pointer/table; do not close N-b-010. |
| D-P3-009 / N-a-059 | P2.4/P3, `S` | Add the minimal \(L_{\omega_1\omega}\) pointer; substantive ownership remains P3. |
| N-a-060 | P3, `S` | Add the minimal generalized-quantifier pointer; substantive ownership remains P3. |
| D-P9-002 | P4, `T` | Add only the analytical-hierarchy pointer; table/diagram ownership remains P4. |
| A-038 | P2c apparatus | Implement all rows in §5.2. |
| A-039 | P2c apparatus | Implement the comparison in §5.3. |
| A-091 | P2c apparatus | Implement §3.3 plus the nearby formula qualifications. |

## 7. Bibliography-key audit and exact intake metadata

### 7.1 Existing keys verified

The following keys already exist in `handbook/references.bib` and should be reused:

| Existing key | Verified identity | Locator/enrichment note |
|---|---|---|
| `Henkin1950` | Leon Henkin, “Completeness in the Theory of Types,” *Journal of Symbolic Logic* 15(2) (1950), 81--91 | DOI 10.2307/2266967; use pp. 81--89 and theorem numbers stated in §1.1. |
| `Church1940` | Alonzo Church, “A Formulation of the Simple Theory of Types,” *Journal of Symbolic Logic* 5(2) (1940), 56--68 | DOI 10.2307/2266170; use pp. 60--62 for rules/choice/extensionality. |
| `Andrews2002` | Peter B. Andrews, *An Introduction to Mathematical Logic and Type Theory: To Truth Through Proof*, 2nd ed. | Existing book key; no new key required for the P2c historical pointer. |
| `Shapiro1991` | Stewart Shapiro, *Foundations without Foundationalism: A Case for Second-Order Logic* | DOI 10.1093/0198250290.001.0001. |
| `Manzano1996` | María Manzano, *Extensions of First Order Logic*, Cambridge Tracts in Theoretical Computer Science 19, Cambridge UP, 1996 | Enrich existing entry with series/number and stable record [Google Books](https://books.google.com/books?id=GYSZ0AdppgMC) if bibliography policy permits. |
| `Lindstrom1969` | Per Lindström, “On Extensions of Elementary Logic,” *Theoria* 35(1) (1969), 1--11 | DOI 10.1111/j.1755-2567.1969.tb00356.x. |
| `Kleene1952` | Stephen Cole Kleene, *Introduction to Metamathematics* | Existing analytical-hierarchy source spine. |
| `Rogers1967` | Hartley Rogers Jr., *Theory of Recursive Functions and Effective Computability* | Existing analytical-hierarchy source spine. |
| `Moschovakis2009` | Yiannis N. Moschovakis, *Descriptive Set Theory*, 2nd ed., AMS, 2009 | Enrich with series *Mathematical Surveys and Monographs* 155 and DOI 10.1090/surv/155 if permitted. |

### 7.2 Genuinely necessary new keys

These keys are necessary if the register's named source spine and the new free-logic table are cited in the handbook. Metadata below is implementation-ready; key spelling may be adjusted only to the repository's duplicate policy.

| Proposed key | Exact metadata | Stable primary/publisher link | Exact use |
|---|---|---|---|
| `Wang1952` | Hao Wang, “Logic of Many-Sorted Theories,” *Journal of Symbolic Logic* 17(2) (1952), 105--116. DOI 10.2307/2266241. | [Cambridge Core record](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/logic-of-manysorted-theories/F6839F4A3250F5B179E5DCB1C6A96DAA) | Historical primary source for the many-sorted/one-sorted translation. Optional if the body cites only existing `Manzano1996`; necessary if Wang is named. |
| `ManzanoAranda2022` | María Manzano and Víctor Aranda, “Many-Sorted Logic,” in *The Stanford Encyclopedia of Philosophy*, Winter 2022 ed., Edward N. Zalta (ed.), Metaphysics Research Lab, Stanford University, 2022. | [Fixed Winter 2022 entry](https://plato.stanford.edu/archives/win2022/entries/logic-many-sorted/) | Authoritative locators §§1.3--1.5 and 6.1 for exact syntax, semantics, and reduction. |
| `Scott1965` | Dana Scott, “Logic with Denumerably Long Formulas and Finite Strings of Quantifiers,” in J. W. Addison, Leon Henkin, and Alfred Tarski (eds.), *The Theory of Models*, North-Holland, Amsterdam, 1965, 329--341. DOI 10.1016/B978-0-7204-2233-7.50036-8. | [ScienceDirect/DOI record](https://doi.org/10.1016/B978-0-7204-2233-7.50036-8) | Exact \(L_{\omega_1\omega}\) boundary and Scott-sentence pointer. |
| `Karp1964` | Carol R. Karp, *Languages with Expressions of Infinite Length*, Studies in Logic and the Foundations of Mathematics 33, North-Holland, Amsterdam, 1964. | [Stable Google Books record](https://books.google.com/books?id=H1sZAAAAMAAJ) | Infinitary proof-theory pointer; do not attach a theorem without exact system/locator. |
| `Mostowski1957` | Andrzej Mostowski, “On a Generalization of Quantifiers,” *Fundamenta Mathematicae* 44(1) (1957), 12--36. DOI 10.4064/fm-44-1-12-36. | [IMPAN journal record](https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/44/1/112086/on-a-generalization-of-quantifiers) | Primary generalized-quantifier lineage. |
| `Lindstrom1966` | Per Lindström, “First Order Predicate Logic with Generalized Quantifiers,” *Theoria* 32(3) (1966), 186--195. DOI 10.1111/j.1755-2567.1966.tb00600.x. | [Wiley/DOI record](https://doi.org/10.1111/j.1755-2567.1966.tb00600.x) | Generalized-quantifier model-theory pointer. |
| `Keisler1970` | H. Jerome Keisler, “Logic with the Quantifier ‘There Exist Uncountably Many’,” *Annals of Mathematical Logic* 1(1) (1970), 1--93. DOI 10.1016/S0003-4843(70)80005-5. | [ScienceDirect/DOI record](https://doi.org/10.1016/S0003-4843(70)80005-5) | Quantifier-specific result; never evidence for arbitrary (Q). |
| `Russell1905` | Bertrand Russell, “On Denoting,” *Mind* 14(56) (1905), 479--493. DOI 10.1093/mind/XIV.4.479. | [Oxford Academic record](https://academic.oup.com/mind/article-abstract/XIV/4/479/964157) | Historical contextual description analysis. |
| `Lambert1967` | Karel Lambert, “Free Logic and the Concept of Existence,” *Notre Dame Journal of Formal Logic* 8(1--2) (1967), 133--144. DOI 10.1305/ndjfl/1093956251. | [Project Euclid DOI record](https://doi.org/10.1305/ndjfl/1093956251) | Free-logic/existence lineage and Lambertian description context. |
| `Bencivenga1986` | Ermanno Bencivenga, “Free Logics,” in Dov M. Gabbay and Franz Guenthner (eds.), *Handbook of Philosophical Logic*, vol. III: *Alternatives to Classical Logic*, Synthese Library 166, D. Reidel, Dordrecht, 1986, 373--426. Chapter DOI 10.1007/978-94-009-5203-4_6. | [Springer book record](https://link.springer.com/book/10.1007/978-94-009-5203-4) | Survey source named by N-b-010. Use 1986, matching the publisher volume and register. |
| `Lehmann2002` | Scott Lehmann, “More Free Logic,” in Dov M. Gabbay and Franz Guenthner (eds.), *Handbook of Philosophical Logic*, 2nd ed., vol. 5, Kluwer Academic Publishers, Dordrecht, 2002, 197--259. Chapter DOI 10.1007/978-94-017-0458-8_4. | [Springer book record](https://link.springer.com/book/10.1007/978-94-017-0458-8) | Modern free-logic proof-theory/model-theory source named by N-b-010. |
| `GratzlPavlovicNolt2025` | Norbert Gratzl, Edi Pavlović, and John Nolt, “Free Logic,” in Edward N. Zalta and Uri Nodelman (eds.), *The Stanford Encyclopedia of Philosophy*, Summer 2025 ed., Metaphysics Research Lab, Stanford University, 2025. | [Fixed Summer 2025 entry](https://plato.stanford.edu/archives/sum2025/entries/logic-free/) | Exact current cross-variant and definite-description table support. |

New keys should be added only when a handbook citation actually uses them. `Wang1952` is not genuinely required if the exact reduction is cited solely to the already-existing `Manzano1996` plus a handbook derivation; it is listed to prevent an uncited name if Wang is retained in prose.

## 8. Source ledger

| Source | Status | Claims checked | Limits |
|---|---|---|---|
| Henkin (1950), pp. 81--91 | Primary, source-verified | Typed system, general models, Theorems 1--3, compactness, modification remarks | Does not print the proposed relational sequent sheet. |
| Church (1940), pp. 60--62 | Primary, source-verified | Typed rules I--VI, extensionality and choice setting | Functional/type-theoretic presentation, not relational `(Comp)`. |
| Wang (1952) record and Manzano--Aranda §§1, 6.1 | Primary plus authoritative reference, source-verified | Many-sorted syntax/semantics/reduction lineage | The displayed reduction here is normalized to strict same-sort equality and is derived notation. |
| Manzano (1996) | Authoritative monograph, existing key verified | Many-sorted and second-order/general-semantics source spine | Exact theorem-page use should be checked in the book before a page citation is printed. |
| Gratzl--Pavlović--Nolt (2025), §§1--3, 5.1 | Authoritative reference, source-verified | Positive/negative/neutral distinctions, quantifier restrictions, description packages | Surveys multiple systems; does not license one uniform calculus. |
| Russell (1905), Lambert (1967), Bencivenga (1986), Lehmann (2002) | Primary/historical and handbook sources; metadata verified | Registered free-logic source spine | Cross-variant table is synthesized from the modern authoritative overview. |
| Scott (1965), Karp (1964) | Primary sources; metadata verified | \(L_{\omega_1\omega}\) formation and proof-theory lineage | No exact Karp completeness theorem is claimed here. |
| Mostowski (1957), Lindström (1966), Keisler (1970) | Primary sources; metadata verified | Generalized-quantifier lineage and (Q_1)-specific study | No result for one (Q) is generalized to every (Q). |
| Kleene (1952), Rogers (1967), Moschovakis (2009) | Existing authoritative source spine | Analytical-hierarchy pointer | The P4 table/diagram still needs its own exact locators and review. |
| Lindström (1969) | Primary, existing key verified | Abstract characterization calibration | Caption must retain the theorem's regularity hypotheses. |

## 9. Consolidated unsupported formulations

The following formulations should block acceptance if they appear in the P2c implementation:

1. An unqualified `Henkin1950` citation on a newly assembled relational calculus.
2. A completeness theorem whose proof system, syntax, comprehension/choice eligibility, or Henkin model class differs across its two sides.
3. Full-semantic choice called valid without a metatheoretic choice qualification.
4. Many-sorted reduction without nonemptiness or function-closure axioms.
5. Positive/negative/neutral treated as three fully determined calculi rather than families requiring further choices.
6. A single description law presented as constitutive of all free logics.
7. Karp completeness described as ordinary finitary strong completeness, or \(L_{\omega_1\omega}\) described as compact.
8. Keisler's (Q_1) results generalized to arbitrary generalized quantifiers.
9. Lightface analytical hierarchy conflated with boldface/projective pointclasses.
10. A-038 missing any registered row, A-039 omitting a requested metatheorem, or A-091 omitting neutral logic/existence/quantifier/description qualifications.

## Binary evidence verdict

**PASS.** Primary and authoritative evidence is sufficient to implement the P2c new content, the many-sorted reduction, and A-038/A-039/A-091 at their registered ceilings. The pass is evidence-level, not a pre-approval of any future prose: the relational second-order completeness result must be marked **derived** and must use Route A or discharge all five Route B correspondence obligations. An implementation that merely cites Henkin (1950) for a syntactically different sheet has an evidence verdict of **FAIL**.
