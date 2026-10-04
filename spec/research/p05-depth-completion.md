# P5 research: arithmetic depth completion

Status: source-backed evidence ledger for the Phase-4 P5 depth-completion
visit. This is not handbook prose. It does not change a register, mark a row
`done`, add a bibliography record, or by itself satisfy a treatment
requirement. The migrated substrate is the frozen `v1.1-verified` arithmetic
material in `source/formal-logic-reference.tex`. External sources and metadata
were checked on 2026-08-11.

## Evidence policy and claim boundary

- **Source-verified** means that the stated fact or proof ingredient occurs in
  frozen v1.1 at the line range given.
- **Primary-verified** means that the claim or metadata was checked against the
  original publication or its publisher/archive record.
- **Standard-secondary** means that the formulation was checked against a
  standard monograph, textbook, author-hosted survey, or identified modern
  reference at the locator given.
- **Derived** means that the displayed formulation follows from the cited
  source facts by the argument recorded here. It is not a quotation and is not
  independently a source for a handbook `cited=` status.
- **Claim ceiling** is the strongest treatment licensed jointly by the live
  row, the Phase-4 handover, and the located evidence. `E`, `T`, `S`, and `P`
  remain entry, table/treatment, statement/survey, and pointer obligations;
  none is itself a proof status. A body theorem still needs exactly
  `proved=annex:<id>`, `sketched=annex:<id>`, or `cited=<bibkey>` under
  `handbook/CONVENTIONS.md`.
- **Do not claim** identifies a tempting strengthening, a missing hypothesis,
  or a formulation not supported at the advertised level.

## Binding P5 inventory and live conflicts

| row | exact topic | treatment / priority / effort | evidence-safe ceiling |
|---|---|---|---|
| `D-P6-002` | Tennenbaum's theorem (statement) | S / should / S | cited statement for countable nonstandard models of full first-order PA |
| `D-P6-003` | nonstandard PA order type and overspill | E / should / M | exact definitions and cited statements; no complete source proof |
| `D-P6-005` | relative interpretation with examples | S / could / S | exact one-dimensional definition, examples, and cited transfer result |
| `D-P6-006` | provable `Sigma_1`-completeness stated and proved | E / must / M | external theorem can be sketched from v1.1; formalized theorem can only be newly sketched without a complete proof-code compiler |
| `N-a-029` | Tarski--Mostowski--Robinson method, essential-undecidability transfer, interpretability-logic pointer | S / should / M | statement/survey; the logic pointer does not license a new modal development |
| `N-a-032` | nonstandard existence/order type, overspill and uses, Tennenbaum | E / must / M | entry-level package, but individual theorem statuses remain cited/sketched as specified below |

The prose handover at `spec/PHASE4-HANDOVER.md` 241--245 instead assigns the
P5 additions as follows: order type and overspill `S`, named
`Sigma_1`-completeness `S + annex sketch`, interpretability `S`, and
Tennenbaum `S cited`. This produces four live reconciliation points:

1. `D-P6-006` says “stated and proved,” but the handover requires an annex
   sketch and v1.1 supplies only ingredients and an implicit use. A complete
   formalized proof is not source-supported. The safe result status is
   `sketched=...` unless a new, independently checked proof-code compiler is
   supplied.
2. `N-a-032` says “Tennenbaum proof at T level,” while `D-P6-002` and the
   handover require only an S-level cited statement. The primary 1959 abstract
   is not a handbook-ready complete proof. The safe handover delivery is
   `cited=Tennenbaum1959`.
3. `D-P6-003` labels the order-type/overspill unit `E`, whereas the handover
   calls it `S`. The body may give an entry-level definition of blocks and an
   exact theorem statement, but the theorem evidence must remain cited.
4. `D-P6-005` says `could`, while `N-a-029` says `should` and materially adds
   the essential-undecidability transfer and logic pointer. Those additions
   are supportable, but they do not license transfer of plain undecidability
   or a full interpretability-logic chapter.

The register notation
`\(\mathbb N+\mathbb Z\mathbin{\cdot}\mathbb Q\)` is convention-sensitive.
The body should define it as the lexicographic sum of copies of the integer
order indexed by the rational order, rather than relying on multiplication
order alone.

## Frozen v1.1 arithmetic substrate

| source lines | item | source evidence and P5 use |
|---:|---|---|
| 9099--9111 | Robinson arithmetic `Q` | exact axiom base for external `Sigma_1`-completeness |
| 9121--9149 | bounded-case enumeration in `Q` | complete proof; load-bearing finite-case step for true bounded formulas |
| 9151--9174 | dichotomy in `Q` | complete proof; supports closed bounded comparisons |
| 9176--9186 | Peano arithmetic | exact full-induction base for the safe overspill statement |
| 9192--9201 | standard/nonstandard models | source definition; standardness is an isomorphism-type classification |
| 9203--9226 | compactness produces countable nonstandard models | complete proof of existence, not classification of their order types |
| 9249--9260 | standard truth versus formal proof | explicitly mentions the restricted `Sigma^0_1` truth-to-`Q`-provability phenomenon |
| 9292--9309 | representability theorem and construction paragraph | cited coding substrate; not a proof of formalized `Sigma_1`-completeness |
| 9373--9390 | arithmetization of syntax | proof sketch; numeral substitution and proof checking are primitive recursive |
| 9392--9412 | fixed proof and provability predicates | exact intensional proof predicate to which any formalized theorem must be tied |
| 9762--9796 | Hilbert--Bernays--Loeb conditions | PA's D2/D3 are cited; arbitrary c.e. `T` extending `Q` takes all three as hypotheses |
| 16210--16220 | exercise-solution discussion of D1 | reinforces representability-based proof production, not a formalized completeness proof |

There is no v1.1 statement or proof of the PA order-type classification,
overspill, interpretability, or Tennenbaum's theorem. Those are new-content
claims and must use external evidence. The external `Sigma_1` theorem is
implicit in the warning and can be sketched from the displayed `Q` lemmas;
the formalized schema is only implicit in the cited D3 machinery.

## Research package 5.1: order type of countable nonstandard PA models

### Exact formulation

**Standard-secondary, claim-safe statement.** Let
`M \models \mathsf{PA}` be nonstandard. On its nonstandard elements define

\[
  a\sim b
  \quad\Longleftrightarrow\quad
  a+\bar n=b\ \text{or}\ b+\bar n=a
  \text{ for some externally standard }n\in\mathbb N.
\]

Each equivalence class is a convex block of order type
`\(\zeta=\operatorname{otp}(\mathbb Z)=\omega^*+\omega\)`, and the quotient
order `A` of the nonstandard blocks is a dense linear order without endpoints.
Consequently

\[
  \operatorname{otp}(M,<^M)=
  \omega+\sum_{a\in A}\zeta.
\]

If `M` is countable, then `A` is countable and hence isomorphic to
`\((\mathbb Q,<)\)`. Thus the unambiguous countable-model formulation is

\[
  \operatorname{otp}(M,<^M)=
  \omega+\sum_{q\in(\mathbb Q,<)}\zeta.
\]

Richard Kaye and Andrey Bovykin state the general result as Theorem 3.1 of
“Order-types of models of Peano arithmetic: a short survey”: every
nonstandard model of PA has order type `N + A Z`, with `A` dense and without
endpoints; their subsequent countable case identifies `A` with `Q`.

- Author-posted survey:
  <https://www.researchgate.net/publication/2832625_Order-types_of_models_of_Peano_arithmetic_a_short_survey>
- Standard monograph locator: Richard Kaye, *Models of Peano Arithmetic*,
  Chapter 6, “Models of PA,” pp. 69--77:
  <https://academic.oup.com/book/53349/chapter/422047794>

### Source relationship and ceiling

**Source-verified.** Lines 9192--9201 define nonstandard models and
9203--9226 prove that every arithmetic theory true in the standard model has
a countable nonstandard model. They do not analyze the order of that model.

**Derived.** Countability is used only after the block theorem, to invoke the
uniqueness of the countable dense order without endpoints. It is not needed
for the existence of integer blocks or for density of the block quotient.

**Do not claim.**

1. Do not write the register's product notation without defining the order of
   the lexicographic sum; conventions for products of order types differ.
2. Do not claim that every, including uncountable, nonstandard model has
   quotient order `Q`.
3. Equal order types do not make two nonstandard arithmetic structures
   isomorphic.
4. Tennenbaum's theorem does not imply that this underlying linear order has
   no computable presentation.
5. `Skolem1934` supports historical nonstandard-model existence, not this
   exact order classification.

### Bibliography verdict

The live `Kaye1991` record is the principal standard citation. The live
`BoolosBurgessJeffrey2007` may accompany it. No new order-type key is required.

## Research package 5.2: overspill

### Exact hypotheses and formulations

**Standard-secondary, claim-safe basic form.** Let
`M\models\mathsf{PA}` be nonstandard, let `\varphi(x,\bar a)` be an internal
first-order formula in the language of arithmetic, and let `\bar a\in M`.
If

\[
  M\models\varphi(\bar n,\bar a)
  \qquad\text{for every externally standard }n\in\mathbb N,
\]

then there is some `b\in M` outside the standard initial segment such that
`M\models\varphi(b,\bar a)`.

**Standard-secondary, useful strong form.** Under the same hypotheses there
is a nonstandard `c\in M` such that

\[
  M\models\forall x<c\,\varphi(x,\bar a).
\]

Boolos--Burgess--Jeffrey state the overspill principle in Chapter 25,
Lemma 25.8, for a nonstandard model of PA and a language formula satisfied by
all standard elements. The proof uses induction.

- Publisher-hosted Chapter 25 PDF, §25.8:
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9129366CB116D3A01043CABCAC16C297/9781139164931c25_p302-318_CBO.pdf/nonstandard_models.pdf>
- Kaye's standard secondary locator is Chapter 6, §6.1:
  <https://academic.oup.com/book/53349/chapter/422047794>

### Source relationship and ceiling

**Source-verified.** PA at 9176--9186 supplies full first-order induction.
The source definition at 9192--9201 makes clear that standardness is external
to the model. No overspill theorem occurs in v1.1.

**Derived.** The displayed strong form may be obtained by applying induction
and least-counterexample reasoning to the definable failure set. It is safe as
a worked consequence of overspill, but not as a source-migrated proof.

**Do not claim.**

1. Countability is not a hypothesis.
2. Parameters from `M` are allowed; PA's induction scheme allows parameters.
3. “Standard” is external/metalinguistic. Do not introduce a definable
   standardness predicate inside `M`.
4. The property must be expressed by an internal first-order formula, not an
   arbitrary external subset of `M`.
5. The conclusion supplies some nonstandard witness, not every nonstandard
   element.
6. Do not attribute this PA theorem merely to compactness or saturation.

### Bibliography verdict

The live `BoolosBurgessJeffrey2007` and `Kaye1991` records suffice. No new
overspill key is needed.

## Research package 5.3: external and formalized `Sigma_1`-completeness

The name “`Sigma_1`-completeness” is used for two related but nonidentical
results. The handbook must state them separately.

### External `Sigma_1`-completeness of `Q`

**Standard-secondary, exact named theorem.** For every closed
`\Sigma^0_1` sentence `\sigma`,

\[
  \mathcal N\models\sigma
  \quad\Longrightarrow\quad
  \mathsf Q\vdash\sigma.
\]

The Open Logic Project gives the exact theorem as Theorem inp.7, after lemmas
for closed atomic formulas and true bounded formulas:

<https://builds.openlogicproject.org/content/incompleteness/representability-in-q/sigma1-completeness.pdf>

Emil Jeřábek gives a detailed standard presentation in *Mathematical Logic*,
§3.2, Lemmas 3.7 and 3.9 and Theorem 3.10:

<https://users.math.cas.cz/~jerabek/teaching/mathlog/MathLogic.pdf>

**Source-backed annex sketch.** An honest sketch from v1.1 may proceed as
follows.

1. Put the true sentence in the form
   `\(\exists\bar x\,\delta(\bar x)\)`, with `\delta` bounded, and choose its
   actual standard witnesses.
2. Evaluate the resulting closed terms and atomic formulas at numerals using
   the defining axioms of `Q` at 9099--9111.
3. Reduce a standard bounded universal quantifier to finitely many numeral
   cases using the complete bounded-case theorem at 9121--9149; use the
   dichotomy at 9151--9174 where the chosen bounded-form convention requires
   comparison normalization.
4. Reassemble the Boolean and bounded-quantifier structure, then introduce
   the leading existential witnesses.

The sketch must explicitly omit the full structural induction for closed
bounded formulas, including closed multiplication evaluation, Boolean and
negation cases, the bounded-existential case, and conversion to the chosen
`Sigma_1` prefix convention. These omissions prevent a `proved=` claim.

### Formalized or provable `Sigma_1`-completeness

**Standard-secondary, claim-safe schema for the live setup.** Fix PA's exact
arithmetization and the proof predicate of v1.1 lines 9392--9412. For every
`\Sigma^0_1` formula `\sigma(\bar x)`, PA proves the corresponding instance

\[
  \mathsf{PA}\vdash
  \sigma(\bar x)\to
  \mathsf{Prov}_{\mathsf{PA}}
  \bigl(\operatorname{Sub}(\ulcorner\sigma\urcorner,
  \operatorname{Num}(\bar x))\bigr).
\]

Here `Sub` and `Num` denote the fixed primitive-recursive code operations for
substituting the numeral codes of the free variables. The familiar notation
`\(\ulcorner\sigma(\dot{\bar x})\urcorner\)` is only an abbreviation after
those operations have been fixed. This is a metatheoretic schema indexed by
formulas, not automatically one internal sentence quantifying over all
formula codes.

Jeřábek's Theorem 3.30 and its proof discussion use formalized
`Sigma_1`-completeness to obtain positive introspection; the free-variable
form and numeral-substitution coding are essential. The same text also warns
that its chosen weak base `Q` does not by itself establish all of the HBL
machinery used there.

**Source relationship.** Lines 9373--9390 only sketch the primitive-recursive
syntax operations. Lines 9392--9412 fix the proof predicate. Lines 9790--9796
assert D2 and D3 for PA by citation and take D1--D3 as hypotheses for an
arbitrary c.e. `T\supseteq Q`. Thus v1.1 implicitly uses the formalized result
but does not prove it.

**Evidence-safe annex sketch.** A new sketch may say that the external
structural induction is arithmetized, each `Q` derivation step is replaced by
a primitive-recursive proof-code constructor, and the constructors are
composed for the fixed PA proof predicate. It must name as omissions the full
compiler, the verification in PA of every constructor and composition step,
and the exact numeral-substitution invariant. This supports `sketched=...`,
not `proved=...`.

**Do not claim.**

1. External truth-to-provability and the internal schema are not the same
   theorem.
2. `Sigma_1`-completeness is not reflection; it does not give
   `\(\mathsf{Prov}_T(\ulcorner\sigma\urcorner)\to\sigma\)`.
3. It does not make every true arithmetic sentence provable.
4. Do not infer the formalized schema for every arbitrary c.e.
   `T\supseteq Q` from the current source. State it for PA and its fixed proof
   predicate, or supply a separately verified internal proof compiler and
   normalization bridge for the stronger generality.
5. Do not hide the intensional dependency on the exact proof predicate or the
   primitive-recursive instance-code operation.

### Bibliography verdict

The live `Shoenfield1967` and `BoolosBurgessJeffrey2007` records suffice for
the external theorem and its standard background. The live
`HilbertBernays1939` and `Lob1955` records support the HBL use. A new key is
not mandatory. If a direct modern locator for the exact formalized schema is
desired, the verified optional record is:

```bibtex
@online{Jerabek2026,
  author       = {Je{\v r}{\'a}bek, Emil},
  title        = {Mathematical Logic},
  organization = {Charles University, Faculty of Mathematics and Physics},
  note         = {Based on course notes taken by Jind{\v r}ich Nov{\'a}k},
  year         = {2026},
  month        = jan,
  url          = {https://users.math.cas.cz/~jerabek/teaching/mathlog/MathLogic.pdf},
  urldate      = {2026-08-11},
}
```

## Research package 5.4: relative interpretability

### Exact definition and standing

**Primary/standard-backed, claim-safe definition.** A one-dimensional,
parameter-free interpretation `I` of a source theory `U` in a target theory
`V` consists of:

1. a target-language domain formula `\delta(x)` with
   `\(V\vdash\exists x\,\delta(x)\)`;
2. a target formula `R^I` for every source relation symbol `R`;
3. a target definable graph for every source function and constant, with `V`
   proving domain closure, existence, and uniqueness;
4. a recursive translation commuting with Boolean connectives and satisfying

   \[
     (\exists x\,\varphi)^I
       :=\exists x(\delta(x)\land\varphi^I),
     \qquad
     (\forall x\,\varphi)^I
       :=\forall x(\delta(x)\to\varphi^I);
   \]

5. `\(V\vdash\alpha^I\)` for every axiom `\alpha` of `U`.

This term names a metalinguistically specified translation between theories,
not a new arithmetic object. It is necessary because literal inclusion and
definitional extension cannot express definable domains or quotient
structures. If source equality is not translated as actual target equality,
the quotient variant must separately specify a target-definable equivalence
relation `E`; `V` must prove that `E` is an equivalence relation and that all
interpreted symbols are `E`-invariant. Multidimensional and parameter-using
interpretations are variants and must not be silently mixed into this base
definition.

### Safe consequences and examples

**Derived by induction on derivations.**

\[
  U\vdash\varphi
  \quad\Longrightarrow\quad
  V\vdash\varphi^I.
\]

Consequently, if `V` is consistent, then `U` is consistent.

**Primary/modern-secondary, essential-undecidability transfer.** If `U` is an
essentially undecidable effectively axiomatized theory and a consistent
effectively axiomatized theory `V` effectively interprets `U`, then `V` is
essentially undecidable, and therefore undecidable. This is the safe upward
transfer: `U` is the interpreted source and `V` is the host.

Tarski, Mostowski, and Robinson develop the general method in Chapter I,
§§3--4, especially Theorems 6--8:

- Publisher book record:
  <https://www.sciencedirect.com/bookseries/studies-in-logic-and-the-foundations-of-mathematics/vol/13/suppl/C>
- Chapter I and DOI `10.1016/S0049-237X(09)70292-7`:
  <https://www.sciencedirect.com/science/article/pii/S0049237X09702927>

Pakhomov and Visser give the exact modern essential-undecidability transfer in
Theorems 2.1--2.2 of “There are no minimal essentially undecidable theories”:

<https://academic.oup.com/logcom/article/34/6/1159/7080260>

**Safe examples.** PA interprets `Q` by the identity translation because PA
extends `Q`. A definitional extension interprets back into its base theory by
eliminating the defined symbols.

**Do not claim.**

1. “`U` is interpretable in `V`” makes `V` the host; reversing this direction
   reverses the intended transfer.
2. Plain undecidability does not in general transfer under ordinary
   interpretability. Use essential undecidability and its exact effective and
   consistency hypotheses.
3. Interpretation is not conservativity, definitional equivalence,
   bi-interpretability, faithful interpretation, elementary embeddability, or
   literal substructure.
4. Target consistency is load-bearing; an inconsistent target proves every
   translated axiom.
5. Do not claim a many-one reduction of complete theorem sets without an
   additional effective reflection or faithfulness property.

### Bibliography verdict and verified intake

No live handbook key adequately supports the interpretation definition and
Tarski--Mostowski--Robinson transfer. The minimum required new key is:

```bibtex
@book{TMR1953,
  author    = {Tarski, Alfred and Mostowski, Andrzej and Robinson, Raphael M.},
  title     = {Undecidable Theories},
  series    = {Studies in Logic and the Foundations of Mathematics},
  volume    = {13},
  publisher = {North-Holland},
  location  = {Amsterdam},
  year      = {1953},
  pages     = {1--98},
  isbn      = {9780444533784},
}
```

If the registered interpretability-logic pointer is retained, add the
verified report record rather than treating TMR as a source for that later
modal subject:

```bibtex
@techreport{Visser1997,
  author      = {Visser, Albert},
  title       = {An Overview of Interpretability Logic},
  institution = {Department of Philosophy, Utrecht University},
  series      = {Logic Group Preprint Series},
  number      = {174},
  location    = {Utrecht},
  year        = {1997},
  pagetotal   = {53},
  url         = {https://hdl.handle.net/11245/1.135125},
}
```

Authoritative repository metadata:
<https://dare.uva.nl/record/1/135125>. A published version appeared in 1998;
the `Visser1997` key above deliberately denotes the registered 1997 preprint.

For a modern systematic reference, especially if the exact definition and
its variants receive more than a short survey, use:

```bibtex
@book{Lindstrom2003,
  author    = {Lindstr{\"o}m, Per},
  title     = {Aspects of Incompleteness},
  edition   = {2},
  series    = {Lecture Notes in Logic},
  volume    = {10},
  publisher = {A K Peters},
  location  = {Natick, MA},
  year      = {2003},
  isbn      = {9781568811734},
}
```

The exact locator is Chapter 6, “Interpretability,” pp. 75--93; Chapter 7,
pp. 94--118, concerns degrees of interpretability. Publisher/reprint record:
<https://www.cambridge.org/core/books/aspects-of-incompleteness/A5DD4A21A97228C01CC34A3F362BCA82>.

## Research package 5.5: Tennenbaum's theorem

### Exact hypotheses and safe statement

**Primary/standard-backed, registered-strength theorem.** No countable
nonstandard model `M\models\mathsf{PA}` has a computable presentation.
Explicitly, there is no bijection `e:\mathbb N\to M` for which both
transported operations

\[
  (m,n)\longmapsto e^{-1}(e(m)+^M e(n))
  \quad\text{and}\quad
  (m,n)\longmapsto e^{-1}(e(m)\times^M e(n))
\]

are computable functions on `\mathbb N^2`.

Tennenbaum's original abstract is “Non-Archimedean Models for Arithmetic,”
*Notices of the American Mathematical Society* 6 (1959), p. 270. It derives
the corollary that there is no recursive non-Archimedean model for all
provable arithmetic sentences.

- Primary AMS issue scan, p. 270:
  <https://www.ams.org/journals/notices/195906/195906FullIssue.pdf>
- Standard modern chapter summary, Richard Kaye, “Tennenbaum's theorem for
  models of arithmetic,” pp. 66--79, DOI
  `10.1017/CBO9780511910616.005`:
  <https://www.cambridge.org/core/books/abs/set-theory-arithmetic-and-foundations-of-mathematics/tennenbaums-theorem-for-models-of-arithmetic/EEF8A22A2DBF156464F174EC467A531B>

### Exact ceiling and stronger reduct warning

Countability is part of the external presentation formulation. “Computable”
refers to the transported operations on a computable copy, not to what the
model internally believes about algorithms. The safe model fragment is full
first-order PA. The registered theorem rules out simultaneous computability
of addition and multiplication.

The stronger fact that neither the additive reduct nor the multiplicative
reduct alone is recursive is true, but it belongs to later reduct
strengthenings and should not be attributed solely to the 1959 abstract.
James Schmerl's “Tennenbaum's theorem and recursive reducts” records the
separate additive and multiplicative history:

<https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1E85D80DCF61BF68846D519E5F7AC768/9780511910616c7_p112-149_CBO.pdf/tennenbaums_theorem_and_recursive_reducts.pdf>

**Do not claim.**

1. The theorem does not deny the existence of countable nonstandard models;
   v1.1 lines 9203--9226 prove such existence.
2. It does not say that the arithmetic order has no computable presentation.
3. It does not apply adversely to the standard model `\mathbb N`.
4. Do not weaken PA to `Q`, `PA^-`, `I\Delta_0`, or `I\Sigma_1` without a
   separate theorem.
5. Do not replace “both operations are computable” with “either operation is
   computable” while citing only `Tennenbaum1959`.
6. Do not conflate a computably enumerable graph with a computable operation.
7. The theorem quantifies over presentations; it is not a claim about one
   privileged coding of the domain.

### Bibliography verdict

The live `Tennenbaum1959` record is the exact primary record for the
registered-strength cited statement. The live `Kaye1991` is an adequate
standard secondary source. No new Tennenbaum key is required. The live
`Skolem1934` belongs with nonstandard-model existence, not Tennenbaum's
computability obstruction.

## Consolidated bibliography and claim map

| claim | evidence class | principal handbook key(s) | intake verdict |
|---|---|---|---|
| countable PA order type | standard-secondary | `Kaye1991`, optionally `BoolosBurgessJeffrey2007` | live keys suffice |
| overspill | standard-secondary | `BoolosBurgessJeffrey2007`, `Kaye1991` | live keys suffice |
| external `Sigma_1`-completeness of `Q` | source-supported sketch + standard-secondary theorem | `Shoenfield1967`, `BoolosBurgessJeffrey2007` | live keys suffice; `Jerabek2026` optional |
| formalized `Sigma_1` schema for PA | standard-secondary; only implicit/cited in v1.1 | `HilbertBernays1939`, `Lob1955`, optionally `Jerabek2026` | no new key mandatory, but status must be sketched |
| relative interpretation/TMR transfer | primary + modern standard-secondary | `TMR1953`; optionally `Lindstrom2003` | `TMR1953` required |
| interpretability-logic pointer | standard-secondary | `Visser1997` | required only if pointer retained |
| Tennenbaum registered-strength theorem | primary + standard-secondary | `Tennenbaum1959`, `Kaye1991` | live keys suffice |
| nonstandard-model existence/history | source-verified + primary | `Skolem1934` | live key suffices; not a substitute for order type |

## Writer and adversarial-verification checklist

1. Define integer blocks and print the lexicographic sum before using the
   shorthand `Z dot Q`.
2. State countability only in the step identifying the dense block quotient
   with `Q`; do not import it into overspill.
3. Keep “standard natural number” explicitly external in both the block
   relation and overspill.
4. Give overspill an internal formula and allow model parameters; do not use
   an internal standardness predicate.
5. Name the external theorem “`Sigma_1`-completeness of `Q`” and keep its
   annex omissions explicit.
6. State formalized completeness separately, for PA's fixed proof predicate,
   with an explicit instance-code operation and a `sketched=` status.
7. Do not infer reflection, general arithmetic completeness, or the schema for
   arbitrary c.e. extensions of `Q`.
8. Define the direction of an interpretation before stating any transfer.
   If quotient equality is used, state all congruence obligations.
9. Transfer essential undecidability, not plain undecidability; retain
   effectiveness and target-consistency hypotheses.
10. State Tennenbaum for countable nonstandard models of full PA and for
    simultaneous computability of the transported addition and multiplication
    operations.
11. If the stronger one-reduct theorem is mentioned, cite later reduct work
    rather than upgrading `Tennenbaum1959`.
12. Resolve the live handover/register conflicts explicitly in the
    verification note; do not report `D-P6-006` or the Tennenbaum T-level
    request as fulfilled by a weaker or differently statused item.

## External locator ledger

All links were accessed on 2026-08-11. Handbook prose should cite resolved
bibliography keys, not raw web URLs.

- PA order types: Bovykin--Kaye survey, Theorem 3.1 and countable corollary,
  <https://www.researchgate.net/publication/2832625_Order-types_of_models_of_Peano_arithmetic_a_short_survey>.
- Models of PA and overspill: Kaye, Chapter 6,
  <https://academic.oup.com/book/53349/chapter/422047794>.
- Overspill: Boolos--Burgess--Jeffrey, Chapter 25, Lemma 25.8,
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9129366CB116D3A01043CABCAC16C297/9781139164931c25_p302-318_CBO.pdf/nonstandard_models.pdf>.
- External `Sigma_1`-completeness: Open Logic Project, Theorem inp.7,
  <https://builds.openlogicproject.org/content/incompleteness/representability-in-q/sigma1-completeness.pdf>.
- External and formalized `Sigma_1`-completeness: Jeřábek, §3.2 and
  Theorem 3.30,
  <https://users.math.cas.cz/~jerabek/teaching/mathlog/MathLogic.pdf>.
- Tarski--Mostowski--Robinson primary book and Chapter I,
  <https://www.sciencedirect.com/bookseries/studies-in-logic-and-the-foundations-of-mathematics/vol/13/suppl/C>,
  <https://www.sciencedirect.com/science/article/pii/S0049237X09702927>.
- Essential-undecidability transfer: Pakhomov--Visser, Theorems 2.1--2.2,
  <https://academic.oup.com/logcom/article/34/6/1159/7080260>.
- Interpretability logic: Visser 1997 repository record,
  <https://dare.uva.nl/record/1/135125>.
- Modern interpretability monograph: Lindström, Chapter 6,
  <https://www.cambridge.org/core/books/aspects-of-incompleteness/A5DD4A21A97228C01CC34A3F362BCA82>.
- Tennenbaum primary abstract: AMS 1959 issue, p. 270,
  <https://www.ams.org/journals/notices/195906/195906FullIssue.pdf>.
- Tennenbaum standard chapter:
  <https://www.cambridge.org/core/books/abs/set-theory-arithmetic-and-foundations-of-mathematics/tennenbaums-theorem-for-models-of-arithmetic/EEF8A22A2DBF156464F174EC467A531B>.
- Stronger recursive-reduct results: Schmerl chapter,
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1E85D80DCF61BF68846D519E5F7AC768/9780511910616c7_p112-149_CBO.pdf/tennenbaums_theorem_and_recursive_reducts.pdf>.
