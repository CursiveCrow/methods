# P8.5--P8.6 source-syntax correction

> **HISTORICAL MICRO-AUDIT, NOT A CONTENT PLAN (2026-08-12).** The individual
> source observations below remain leads for presentation-wide verification.
> They do not authorize isolated glyph replacement, selection among sources,
> or construction of a hybrid handbook presentation. The complete source
> presentation, not this correction list, controls transcription.

## Question and decision rule

This note checks only the disputed P8.5--P8.6 notation against the cited
primary presentations.  It distinguishes a symbol actually printed by a
source from a handbook typography or collision policy.  The operative rule is:
retain a cited source's notation and type it locally; do not manufacture a new
surface merely because a glyph already has another, differently typed use.

## Verified source syntax

### 1. Lukasiewicz implication and strong conjunction

Hajek fixes a generic continuous t-norm as `\(\ast\)` and its residuum as the
plain operation `\(\Rightarrow\)`.  Definition 2.1.5 on printed p. 29 calls
`\(x\Rightarrow y\)` the residuum, and Theorem 2.1.8 on p. 30 gives the
Lukasiewicz case with that same un-subscripted arrow.  Lemma 2.1.23 on p. 35
does introduce `\(\ast_{\text{\L}}\)` (with a stroked capital
`\(\text{\L}\)` subscript) for the Lukasiewicz t-norm:
`\(x\ast_{\text{\L}} y=\max(0,x+y-1)\)`.  On the same page, Definition 2.2.1 uses
object-language `\(\&\)` for strong conjunction and `\(\to\)` for implication;
their truth functions are `\(\ast\)` and `\(\Rightarrow\)`, respectively.

Therefore the cited modern presentation supports three separately typed
surfaces:

- formula connectives: `\(A\mathbin{\&}B\)` and `\(A\to B\)`;
- generic semantic operations: `\(x\ast y\)` and `\(x\Rightarrow y\)`;
- the specifically named Lukasiewicz t-norm:
  `\(x\ast_{\text{\L}} y\)`.

It does **not** support a paired semantic notation
`\(x\to_{\text{\L}} y\)` / `\(x\ast_{\text{\L}} y\)`, nor a subscripted
residuum `\(x\Rightarrow_{\text{\L}} y\)`.  The direct facsimile, rather than
its OCR layer, is decisive about the stroke.  With this handbook's T1 font
encoding and `amsmath`, the safe pdfLaTeX rendering is
`\(\mathbin{\ast_{\text{\L}}}\)`; a plain `\(L\)` or `\(\mathrm L\)` loses a
source-significant stroke.

Primary source: Petr Hajek, *Metamathematics of Fuzzy Logic* (1998),
Example 2.1.2 (p. 28), Definition 2.1.5 (p. 29), Theorem 2.1.8 (p. 30),
Lemma 2.1.23 and Definition 2.2.1 (p. 35),
[Springer book record and DOI](https://link.springer.com/book/10.1007/978-94-011-5300-3),
[searchable university-hosted scan](https://dai.fmph.uniba.sk/~guller/fuzzy/matlab_documentation_22/hajek.pdf).

### 1a. Finite `n`-valued identifier and carrier

None of the inspected cited presentations supports the handbook pair
`\(\mathbf L_n\)` (logic or matrix) and `\(\mathsf V_n\)` (its carrier) as an
exact source package.  The closest verified notation is Cignoli,
D'Ottaviano, and Mundici's **unbold** stroked `\(\text{\L}_n\)`, but there it
names the `\(n\)`-element Lukasiewicz **chain itself**.  Printed p. 8 defines

\[
  \text{\L}_n=\left\{0,\frac1{n-1},\ldots,
  \frac{n-2}{n-1},1\right\},
\]

and printed p. 70 repeats the definition.  The direct facsimile of the index,
printed p. 225, confirms the stroked glyph in the entry
"`\(\text{\L}_n\)`, the `\(n\)` element Lukasiewicz chain, 70."  The book
describes the `\(n\)`-valued Lukasiewicz propositional calculus in prose on
pp. 78--80 and types semantic equivalence by the chain; it does not introduce
a second value-set name `\(\mathsf V_n\)` or the bold system name
`\(\mathbf L_n\)`.

The other cited sources do not supply the missing pair.  Lukasiewicz's 1920
note presents one three-valued logic (printed pp. 170--171), not a uniformly
named finite family.  Lukasiewicz--Tarski 1930 is the cited infinite-valued
presentation.  Hajek explicitly says on printed p. 3 that, although logics
with finitely many truth degrees can be developed, his book chooses not to
exclude any real and will always take `\([0,1]\)`.

Consequently the source-safe boundary is: use `\(\text{\L}_n\)` only when the
operand is the Cignoli--D'Ottaviano--Mundici chain, and refer in prose to the
`\(n\)`-valued Lukasiewicz system or its matrix.  Do not manufacture a bold
logic identifier plus a sans-serif carrier.  Under the handbook's T1
pdfLaTeX setup, `\(\text{\L}_n\)` is the safe rendering of the stroked chain
label, just as `\(\mathbin{\ast_{\text{\L}}}\)` is the safe rendering of
Hajek's t-norm symbol.

Primary/authoritative sources: Cignoli, D'Ottaviano, and Mundici,
*Algebraic Foundations of Many-Valued Reasoning* (2000), pp. 8, 70, 78--80,
and index p. 225,
[Springer book record](https://link.springer.com/book/10.1007/978-94-015-9480-6),
[publisher-authorized Google Books facsimile, p. 225](https://books.google.com/books?id=VMzrCAAAQBAJ&pg=PA225);
Lukasiewicz, "O logice trojwartosciowej" (1920), printed pp. 170--171,
[original journal-issue scan](https://kpbc.umk.pl/Content/247342/PDF/EOD_OPEN_006_12_nr_09.pdf);
Hajek, printed p. 3,
[scan](https://dai.fmph.uniba.sk/~guller/fuzzy/matlab_documentation_22/hajek.pdf).

### 2. Product-logic identifier

Hajek, Section 4.1, printed p. 89, says that product logic is denoted by the
plain Greek capital `\(\Pi\)`.  The same page uses `\(\ast_{\Pi}\)` for the
product t-norm and `\(\odot\)` for the object-language product conjunction;
the implication is an un-subscripted `\(\to\)` within that locally declared
section.  Thus `\(\mathbf\Pi\)` is a handbook boldface/collision choice, not
Hajek's identifier.  Local typing, rather than bolding the identifier, is the
source-faithful way to distinguish it from a formula-context metavariable.

Primary source: Hajek, Section 4.1 and Definition 4.1.1, p. 89,
[Springer](https://link.springer.com/book/10.1007/978-94-011-5300-3),
[scan](https://dai.fmph.uniba.sk/~guller/fuzzy/matlab_documentation_22/hajek.pdf).

### 2a. Godel-logic identifier

Hajek's Section 4.2 uses the single plain italic capital `\(G\)` for Godel
logic.  Its opening calls the system "Godel logic `\(G\)`," and Definition
4.2.1 defines "the axiom system of `\(G\).`"  No infinity subscript is part of
the identifier.  Thus `\(\mathsf G_\infty\)` is a normalized handbook name,
not Hajek's surface; the source-faithful identifier is locally typed `\(G\)`.

Primary source: Hajek, Section 4.2 and Definition 4.2.1, printed p. 97,
[Springer](https://link.springer.com/book/10.1007/978-94-011-5300-3),
[scan](https://dai.fmph.uniba.sk/~guller/fuzzy/matlab_documentation_22/hajek.pdf).

### 2b. `BL` and `MTL` typography and attribution

Hajek's Section 2.2 prints the basic logic identifier in upright Roman type as
`\(\mathrm{BL}\)`; Definition 2.2.4 on printed p. 36 is a direct example.  A
safe local TeX rendering is `\(\mathrm{BL}\)`, not sans-serif
`\(\mathsf{BL}\)`.

`\(\mathrm{MTL}\)` is not a Hajek identifier.  Esteva and Godo introduced the
system later; the authoritative publisher rendering of their 2001 article
uses upright Roman `MTL` in the title/abstract and says that it is the weaker
logic investigated for left-continuous t-norms and their residua.  The safe
local rendering is `\(\mathrm{MTL}\)`.  Its source attribution must be
Esteva--Godo, not Hajek.

Primary sources: Hajek, Section 2.2 and Definition 2.2.4, printed p. 36,
[scan](https://dai.fmph.uniba.sk/~guller/fuzzy/matlab_documentation_22/hajek.pdf);
Francesc Esteva and Lluis Godo, "Monoidal t-norm Based Logic: Towards a Logic
for Left-Continuous t-norms" (2001), pp. 271--288,
[publisher article and DOI](https://www.sciencedirect.com/science/article/pii/S0165011401000987).

### 3. Generic t-norm residuum

The source fixes the t-norm first and then writes its residuum simply as
`\(\Rightarrow\)`.  Lemma 2.1.4 and Definition 2.1.5, printed p. 29, give

\[
  x\ast z\leq y \quad\Longleftrightarrow\quad z\leq x\Rightarrow y,
  \qquad
  x\Rightarrow y=\max\{z:x\ast z\leq y\}.
\]

Consequently `\(\Rightarrow_{\ast}\)` is explanatory handbook notation, not
the cited source surface.  The operands and the preceding declaration of
`\(\ast\)` supply the local type in Hajek's presentation.

Primary source: Hajek, Lemma 2.1.4 and Definition 2.1.5, p. 29,
[Springer](https://link.springer.com/book/10.1007/978-94-011-5300-3),
[scan](https://dai.fmph.uniba.sk/~guller/fuzzy/matlab_documentation_22/hajek.pdf).

### 4. Fine's precisifications and `\(\operatorname{Adm}\)`

Fine does not introduce a precisification set named `\(\operatorname{Adm}\)`.
In Section 2, printed pp. 271--272, he defines a *specification space* as a
nonempty collection of specification-points partially ordered by extension;
an appropriate space has one point for each precisification.  He then treats
admissibility as primitive and calls a specification admissible when the space
is appropriate for some precisification.  On pp. 272--273 he uses point
variables such as `\(t\)` and `\(u\)` and states truth at a partial point in
terms of all complete extensions.  Later, in the statement of super-truth
(printed p. 278), he again says in prose that a sentence is true on all
complete and admissible specifications.  A searchable full-text check finds
no occurrence of the literal name `Adm`.

Thus a set `\(\operatorname{Adm}\)` may be declared as new handbook
metanotation only if it is explicitly labelled as such; it must not be
attributed to Fine.  The closest source-faithful presentation is the
specification space, its extension relation, and typed point variables, not a
new named carrier of admissible valuations.

Primary source: Kit Fine, "Vagueness, Truth and Logic," *Synthese* 30
(1975), Section 2, pp. 271--273, and the super-truth discussion on p. 278,
[DOI](https://doi.org/10.1007/BF00485047),
[searchable scan](https://paperzz.com/doc/7634624/vagueness--truth-and-logic).

### 5. Girard phase-space notation

Girard's Section 2.1.1, printed p. 23, defines a phase space as the pair
`\((M,\perp)\)`, where `\(M\)` is a commutative monoid, usually written
multiplicatively, and `\(\perp\subseteq M\)`.  Multiplication is juxtaposition
`\(mn\)`, and Section 2.1.2 names the neutral element `\(1\)`.  For subsets he
writes

\[
  X\multimap Y=\{m\in M:\forall n\in X\;mn\in Y\},
  \qquad X^\perp=X\multimap\perp.
\]

The source deliberately says that the same connective notation will be used
for interpretation on facts.  Theorem 2 on printed p. 24 then writes the
interpretation of a formula as `\(A^*\)` and validity as `\(1\in A^*\)`.

Girard also keeps the same metavariables when he specializes the operations
to facts: Section 2.1.2 writes `\(X,Y\)` for subsets and then uses those same
letters in the displayed fact operations.  A separate alphabet `\(F,G\)` for
facts is therefore a handbook typing convention, not Girard's presentation.

The literal source package is therefore
`\((M,\perp)\)`, juxtaposition, `\(1\)`, `\(X^\perp\)`, and `\(A^*\)`.
The following are not Girard's printed syntax:

- a named product glyph such as a phase-only bullet;
- a renamed unit `\(e\)`;
- a doubled pole glyph `\(\Perp\)`;
- a phase-only orthogonality subscript;
- semantic brackets, with or without a phase subscript, in place of `\(A^*\)`.

Formula negation and subset orthogonality reuse `\({}^{\perp}\)` in the
source; their operand types distinguish them.

Primary source: Jean-Yves Girard, "Linear Logic: Its Syntax and Semantics,"
Sections 2.1.1--2.1.3, printed pp. 23--24,
[author-hosted PDF](https://girard.perso.math.cnrs.fr/Synsem.pdf).

### 6. The inherited IMLL algebra presentation

The authoritative v1.1 source being migrated fixes its own IMLL semantic
presentation at source/formal-logic-reference.tex lines 13972--13999.  It
literally writes \(\mathcal A=(A,\leq,\otimes,1,\multimap)\), uses
\(\sem{A}\) for formula values, and states sequent validity by comparing the
tensor product of antecedent values with the succedent value.  Those glyphs
therefore remain the controlling syntax for the inherited statement; they are
not a collision-avoidance reconstruction.

Galatos, Jipsen, Kowalski, and Ono use the standard structure/carrier
typographic distinction rather than a new carrier function.  In Section 3.2,
printed p. 149, a residuated pogroupoid is
`\(\mathbf G=(G,\mathbin{\cdot},\backslash,/ ,\leq)\)`, and a residuated
partially ordered monoid is
`\(\mathbf G=(G,\mathbin{\cdot},\backslash,/ ,1,\leq)\)`; `\(G\)` is the
carrier in both tuples.  The commutative specialization can identify the two
residuals, but that does not create a carrier named `\(U_{\mathcal A}\)`.

Accordingly `\(U_{\mathcal A}\)` is a handbook collision-avoidance invention,
not source notation.  Galatos et al.'s different tuple is useful background
but must not be described as the source of the inherited v1.1 typography.

The other inspected external citation does not control that surface either.
Girard's 1987 phase-semantics presentation uses a phase space `\(P\)`
(Definition 1.1, printed p. 18) and an interpretation `\(S(A)\)` (Definition
1.14, printed p. 22), not the inherited ordered-algebra tuple or double
brackets.  Lincoln's publisher places the cited chapter under "Complexity and
expressivity"; it is the complexity source, not the algebra-notation source.
The smallest honest boundary is consequently attributional: call the tuple
and brackets inherited v1.1 syntax and cite Galatos et al. only as background
for the algebraic class.  Without the inherited controller, the inspected
external sources would justify prose naming the semantic class, but not
reconstruction of this exact symbolic package.

Primary source: Nikolaos Galatos, Peter Jipsen, Tomasz Kowalski, and Hiroakira
Ono, *Residuated Lattices: An Algebraic Glimpse at Substructural Logics*
(2007), Section 3.2, p. 149,
[bibliographic record](https://books.google.com/books?id=Gy46SP7px7gC),
[ANU repository record](https://dspace-test.anu.edu.au/items/4e2f04cd-3032-474e-ab39-6e8ad6e9b151/full);
Jean-Yves Girard, "Linear Logic" (1987), Definitions 1.1 and 1.14,
printed pp. 18 and 22,
[author-hosted restored scan](https://girard.perso.math.cnrs.fr/linear.pdf);
Patrick Lincoln, "Deciding Provability of Linear Logic Formulas" (1995),
pp. 109--122,
[publisher chapter record](https://www.cambridge.org/core/books/advances-in-linear-logic/deciding-provability-of-linear-logic-formulas/960C431D7336A81B6EDC04E4F6554FE3).

### 7. Relevance-system typography

Dunn and Restall print the system identifiers in **bold Roman** type.  Their
printed p. 2 sets `\(\mathbf R\)` and `\(\mathbf E\)` apart from surrounding
Roman prose in bold; the PDF font is Computer Modern Bold Extended.  Printed
pp. 80--81 likewise print `\(\mathbf{RM}\)` in bold Roman, including the
Section 3.10 heading and running prose.  Thus
`\(\mathbf E,\mathbf R,\mathbf{RM}\)` is source-faithful for this cited
presentation; the source typography, rather than a handbook-wide convention,
controls those identifiers.

The pure implicational fragments keep those bold bases, but Dunn and Restall
place the arrow as a **subscript**.  Printed p. 9 repeatedly uses
`\(\mathbf R_{\to}\)` and `\(\mathbf E_{\to}\)`, including in running prose
and Theorem 2.  Consequently `\(\mathbf R^{\to}\)` and
`\(\mathbf E^{\to}\)` change the source identifier rather than merely its
typography.

Primary source: J. Michael Dunn and Greg Restall, "Relevance Logic" (2002),
pp. 2, 9, 80--81,
[author page](https://consequently.org/writing/rle/),
[author-hosted PDF](https://consequently.org/papers/rle.pdf).

## Classification of the disputed handbook surfaces

| handbook surface | status against the primary presentation |
|---|---|
| `\(x\to_{\text{\L}} y\)` as the Lukasiewicz truth function | not Hajek's surface; use locally typed `\(x\Rightarrow y\)` |
| `\(x\ast_{\text{\L}}y\)` | verified Hajek surface: the subscript is a stroked capital `\(\text{\L}\)`, safely rendered under pdfLaTeX as `\(\ast_{\text{\L}}\)` |
| `\(\mathbf L_n\)` as a finite logic or matrix identifier | not verified in the cited presentations; Cignoli et al. use unbold `\(\text{\L}_n\)` for the finite chain, while the calculus is described in prose |
| `\(\mathsf V_n\)` as a distinct finite carrier | handbook invention; Cignoli et al.'s chain symbol already names the displayed set |
| `\(\mathbf\Pi\)` for Product logic | collision-avoiding boldface, not Hajek's plain `\(\Pi\)` |
| `\(\Rightarrow_\ast\)` | explanatory subscript added by the handbook, absent from Hajek |
| `\(\operatorname{Adm}\)` | locally invented metanotation, absent from Fine |
| phase bullet, `\(e\)`, `\(\Perp\)`, phase-subscripted orthogonality, phase brackets | replacements for Girard's juxtaposition, `\(1\)`, `\(\perp\)`, `\({}^{\perp}\)`, and `\({}^{*}\)` |
| `\(U_{\mathcal A}\)` | locally invented carrier name; Galatos et al. use the carrier letter already present in the structure tuple |
| `\(\mathbf E,\mathbf R,\mathbf{RM}\)` | verified Dunn--Restall typography, not a house-only bolding |
| `\(\mathbf E^{\to},\mathbf R^{\to}\)` | not Dunn--Restall's surface; printed p. 9 has arrow subscripts `\(\mathbf E_{\to},\mathbf R_{\to}\)` |

## Access limits and unresolved points

- The exact claims above about Lukasiewicz and Product notation are verified
  in Hajek's cited 1998 presentation.  I did not obtain a reliable facsimile
  of the 1930 Lukasiewicz--Tarski paper during this check, so this note makes
  no claim about an uninspected finite-system glyph there.  The 1920 note was
  inspected in the original journal-issue scan and is specifically
  three-valued; it supplies no uniform `\(n\)`-indexed surface.
- Dunn--Restall typography is verified directly.  Anderson--Belnap's 1975
  volume was not directly inspected, so no independent claim about its fonts
  is made here.
- The ANU repository's downloadable Galatos-et-al. files are marked restricted
  until 2037.  The tuple and carrier claim was checked against the book text at
  printed p. 149 and is bibliographically anchored by the publisher/ANU
  records; the restriction should be recorded if a reviewer requires an
  official-repository facsimile.
