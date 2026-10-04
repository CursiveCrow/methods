# PCF foundations: primary statements, elementary proofs, and Silver's scope

Date: 2026-09-06.

## Purpose and primary sources

This packet supports the introductory reference section now inserted at
`sec:p06-pcf` in `handbook/parts/p06/cardinal-arithmetic-supplement.tex`.
The elementary statements below have explicit proofs;
the basic PCF theorem and the singular-cardinal power bound retain cited
standing. No reconstruction of the monograph is needed for this scope.

The main source is Saharon Shelah, **Cardinal Arithmetic for Skeptics**,
*Bulletin of the American Mathematical Society (New Series)* **26**(2)
(1992), 197-210, DOI
[10.1090/S0273-0979-1992-00261-6](https://doi.org/10.1090/S0273-0979-1992-00261-6).
The [author-hosted published scan](https://shelah.logic.at/files/95288/400a.pdf)
and [author's publication record](https://shelah.logic.at/papers/400a/)
were consulted. Exact locators are:

- Section 1, printed p. 199: reduced products, filters, ultrafilters, and
  the order distinction.
- Definition 4.1 and Main Theorem 4.3, printed p. 202: possible cofinalities,
  a largest possible cofinality, and the cofinality of the pointwise product.
- The remark immediately following Main Theorem 4.3: the conclusion gives
  a cofinal family, not necessarily a nondecreasing cofinal sequence.
- Theorem A, printed p. 197: the strict bound at a strong-limit
  `aleph_omega`.

The [author's 1993 typeset version](https://shelah.logic.at/files/198206/400a.pdf)
corroborates the formulas with clearer text extraction. It is a separate
15-page version; the printed journal locators above refer to the 14-page
published scan. Shelah's [You Can Enter Cantor's Paradise](https://shelah.logic.at/files/184520/E25.pdf),
Definition 6 and Theorem 7, pp. 5-6, independently states the same basic
PCF theorem in the progressive setting.

For Silver, the primary source is Jack Silver, **On the Singular Cardinals
Problem**, *Proceedings of the International Congress of Mathematicians,
Vancouver 1974*, vol. 1 (Canadian Mathematical Congress, 1975), 265-268.
All four printed pages were read from the
[official IMU proceedings PDF](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1974.1/ICM1974.1.ocr.pdf#page=321)
(PDF pages 321-324). The large PDF was read in memory for text extraction;
no local copy or rendered pages were created.

## 1. Standing hypotheses and the product

Work in ZFC, identifying cardinals with their initial ordinals. A
**progressive set** here means a nonempty set `a` of infinite regular
cardinals such that

\[
 |a|<\min a.
 \tag{1}
\]

The product is the set

\[
 \prod a=\{f:\operatorname{dom}(f)=a\text{ and }
                       f(\kappa)<\kappa\text{ for every }\kappa\in a\}.
 \tag{2}
\]

It is ordered pointwise:

\[
 f\leq g\quad\Longleftrightarrow\quad
             \forall\kappa\in a\;f(\kappa)\leq g(\kappa).
 \tag{3}
\]

This is a partial order, generally not a linear order. Its cofinality is
the least **cardinality** of a cofinal family:

\[
 \operatorname{cof}(P,\leq)=
 \min\{|C|:C\subseteq P\text{ and }
             \forall p\in P\;\exists c\in C\;(p\leq c)\}.
 \tag{4}
\]

Do not replace (4) for an arbitrary partial order by the length of an
increasing cofinal sequence. The cofinal family need not be a chain.
Also distinguish the set (2), its cardinality `|prod a|`, and its
order-theoretic cofinality.

Every infinite cardinal is a limit ordinal, so `f(kappa)+1 < kappa`.
Thus `f^+(kappa)=f(kappa)+1` is a member of the product, strictly above
`f` in every coordinate. The product has no greatest element.

## 2. Filters, reduced orders, and ultrafilter quotients

A proper filter `D` on `a` contains `a`, omits the empty set, and is
closed under supersets and finite intersections. Define

\[
\begin{aligned}
 f=_D g
  &\quad\Longleftrightarrow\quad
       \{\kappa\in a:f(\kappa)=g(\kappa)\}\in D,\\
 f\leq_D g
  &\quad\Longleftrightarrow\quad
       \{\kappa\in a:f(\kappa)\leq g(\kappa)\}\in D.
\end{aligned}
\tag{5}
\]

The first is an equivalence relation and the second induces a partial
order on its classes. Reflexivity and transitivity follow from the
filter laws. If both comparisons hold, their intersection is a set on
which the values agree, proving antisymmetry on classes. Changing either
representative on a set whose complement belongs to `D` does not change
the comparison, so the induced order is well defined. Denote this
reduced product by `prod a/D`.

An ultrafilter is a proper filter such that, for every subset `X` of
`a`, exactly one of `X` and `a \ X` belongs to it. For an ultrafilter,
the quotient is linearly ordered: apply this dichotomy to the set of
coordinates where `f <= g`. If that set is not in the ultrafilter,
then `f > g` on an ultrafilter-large set. Equivalently its strict order is

\[
 [f]_D<_D[g]_D
   \quad\Longleftrightarrow\quad
       \{\kappa:f(\kappa)<g(\kappa)\}\in D.
 \tag{6}
\]

The successor function `f^+` shows that this linear order has no greatest
element.

In ideal notation, the dual proper ideal is
`J={X subset a:a \ X in D}`. Then the same definitions become

\[
 f=_J g\iff\{\kappa:f(\kappa)\ne g(\kappa)\}\in J,
 \qquad
 f\leq_J g\iff\{\kappa:f(\kappa)>g(\kappa)\}\in J.
 \tag{7}
\]

For a general ideal, the commonly used stronger comparison
`{kappa:f(kappa)>=g(kappa)} in J` need not be the strict part of the
quotient order in (7). For an ultrafilter's dual maximal ideal it agrees
with (6). The introductory definition of `pcf` below uses ultrafilters,
so this distinction introduces no ambiguity into it.

## 3. Elementary facts and the definition of pcf

First, a nonempty linear order `L` without a greatest element has an infinite
regular cofinality. Let `lambda=cof(L)`, and enumerate a cofinal set
as `{c_alpha:alpha<lambda}`. A set of fewer than `lambda` elements is
not cofinal; in a linear order it therefore has a strict upper bound.
Recursively choose `d_alpha` above `c_alpha` and all the earlier
`d_beta`. The resulting sequence is increasing and cofinal. If
`lambda` were singular, restricting it to a cofinal set of indices of
size `cf(lambda)<lambda` would give a smaller cofinal set in `L`, a
contradiction. Finite cofinality is impossible because a finite cofinal
set would have a largest member, which would then be greatest in `L`.

Define

\[
 \operatorname{pcf}(a)=
 \left\{\operatorname{cof}(\prod a/D):
                D\text{ is an ultrafilter on }a\right\}.
 \tag{8}
\]

All ultrafilters are included; there is no requirement of
nonprincipality, uniformity, normality, or countable completeness. By
the preceding proof, every member of `pcf(a)` is an infinite regular
cardinal. Formula (8) agrees with Shelah's Definition 4.1.

### Principal ultrafilters

For `kappa in a`, let `D_kappa={X subset a:kappa in X}`. The map

\[
 [f]_{D_\kappa}\longmapsto f(\kappa)
 \tag{9}
\]

is an order isomorphism from `prod a/D_kappa` onto the ordinal `kappa`.
It is well defined and injective by the equality clause in (5), preserves
order by its comparison clause, and is onto by assigning the desired
value at `kappa` and zero elsewhere. Regularity of `kappa` gives

\[
 a\subseteq\operatorname{pcf}(a).
 \tag{10}
\]

### A useful lower bound

Any family `F` in the product of size less than `min a` has a strict
pointwise upper bound

\[
 g(\kappa)=\sup\{f(\kappa)+1:f\in F\}<\kappa.
 \tag{11}
\]

The inequality follows from regularity of each coordinate cardinal.
This bounds the family in every ultrafilter quotient too. Therefore
every possible cofinality is at least `min a`, and (10) yields
`min pcf(a)=min a`. This argument proves a lower bound; it does not
prove existence of a maximum possible cofinality.

### Restriction to a subset

If `emptyset != b subset a`, an ultrafilter `D` on `b` extends to
`D'={X subset a:X intersect b in D}` on `a`. Restriction of functions
is onto and induces an order isomorphism of the two corresponding
quotients; extend functions by zero outside `b` for the inverse on
classes. Hence `pcf(b) subset pcf(a)`.

## 4. The basic PCF theorem: cited deep result

**Shelah's basic PCF theorem.** If `a` is a nonempty progressive set
of infinite regular cardinals, then

\[
\begin{gathered}
 \operatorname{pcf}(a)\text{ has a largest member }
       \lambda_* =\max\operatorname{pcf}(a),\\
 \operatorname{cof}(\prod a,\leq)=\lambda_*,\qquad
 |\operatorname{pcf}(a)|\leq 2^{|a|}.
\end{gathered}
\tag{12}
\]

This is Main Theorem 4.3(1)-(3), printed p. 202 of *Cardinal Arithmetic
for Skeptics*. The hypotheses are exactly ZFC and (1), with distinct
regular coordinates because `a` is a set. No GCH, strong-limit, large-
cardinal, or countability hypothesis is added. The maximum is attained
by the cofinality of some ultrafilter quotient by definition (8).

One direction of the cofinality equality is elementary. The image of
any pointwise cofinal family is cofinal in every quotient, so

\[
 \sup\operatorname{pcf}(a)
       \leq\operatorname{cof}(\prod a,\leq).
 \tag{13}
\]

The existence of a maximum and a pointwise cofinal family of that
cardinality are the substantive conclusions supplied by the cited theorem.
They are not consequences just of the linearity of each quotient.

## 5. Worked examples and the family/chain distinction

For a singleton `a={kappa}`, its only ultrafilter is principal, so
`pcf(a)={kappa}` and the product cofinality is `kappa`.

More generally, every ultrafilter on a finite nonempty set is principal.
If no singleton belonged to it, all singleton complements would belong
to it, and their finite intersection would be empty. Thus for finite `a`,

\[
 \operatorname{pcf}(a)=a,
 \qquad \operatorname{cof}(\prod a,\leq)=\max a.
 \tag{14}
\]

The second assertion also has an elementary proof: the principal
quotient at the largest factor gives the lower bound, and the whole
finite product is a cofinal family of cardinality `max a`, by the
already proved arithmetic of finite products of infinite cardinals.

For example, `a={aleph_0,aleph_1}` is progressive and has pointwise
product cofinality `aleph_1`, but has no nondecreasing cofinal sequence
indexed by `omega_1`. If such a sequence existed, its first coordinates
would form a nondecreasing map `omega_1 -> omega`. Cofinality would
make that map unbounded. Choose an index witnessing each finite bound;
the supremum of these countably many indices is still below `omega_1`,
where monotonicity would require one natural number above every finite
bound. This is impossible. The cofinality conclusion in (12) is a
statement about a family, not an assertion of a pointwise scale.

An infinite progressive example is

\[
 a=\{\aleph_{n+1}:n<\omega\}.
 \tag{15}
\]

Here `|a|=aleph_0 < aleph_1=min a`. Including `aleph_0` in that
countable set would violate progressiveness. By (10) and (12),
`max pcf(a)` is a regular cardinal at least `aleph_omega`; since
`aleph_omega` is singular, it is at least `aleph_(omega+1)`. Thus some
nonprincipal ultrafilter quotient has cofinality above every coordinate
in (15). No particular value of that maximum is asserted here.

## 6. One singular-cardinal consequence with exact scope

A cardinal `kappa` is strong limit when `2^lambda < kappa` for every
cardinal `lambda < kappa`. For `kappa=aleph_omega`, this is equivalent
to `2^(aleph_n) < aleph_omega` for every `n<omega`: any smaller infinite
cardinal is some `aleph_n`, and finite powers are automatically smaller.

**Shelah's bound.** In ZFC,

\[
 \aleph_\omega\text{ strong limit}
      \quad\Longrightarrow\quad
      2^{\aleph_\omega}<\aleph_{\omega_4}.
 \tag{16}
\]

This is Theorem A, printed p. 197 of the published paper. There is
no additional GCH, CH, large-cardinal, or other arithmetic hypothesis.
The inequality is strict. Here `omega_4` is the fourth uncountable
initial ordinal, namely the initial ordinal of cardinality `aleph_4`.
It is not `omega*4`, `omega+4`, or a finite fourth successor of
`aleph_omega`.

Cantor's theorem supplies the elementary lower bound, so (16) gives

\[
 \aleph_{\omega+1}\leq 2^{\aleph_\omega}<\aleph_{\omega_4}.
 \tag{17}
\]

It does not determine the exact value of the power set and does not
assert GCH at `aleph_omega`. It is a cited application of the deeper
PCF theory, not a consequence claimed to follow from (12) alone.

For intuition about the strong-limit hypothesis, a short elementary
calculation gives `2^(aleph_omega)=(aleph_omega)^(aleph_0)` in that
case. A subset of `aleph_omega` is determined by its restrictions to
the `aleph_n`, so

\[
 2^{\aleph_\omega}
   \leq\prod_{n<\omega}2^{\aleph_n}
   \leq(\aleph_\omega)^{\aleph_0}
   \leq(2^{\aleph_\omega})^{\aleph_0}
   =2^{\aleph_\omega}.
\]

This equality illustrates the shift to a small exponent; it does not
replace the deep bound in (16).

## 7. Silver: correct the stated reformulation to GCH

The actual Silver theorem in the manuscript states:

\[
 \operatorname{cf}(\kappa)>\aleph_0,
 \quad\kappa\text{ singular},\quad
 \forall\lambda<\kappa\text{ infinite}\;
             2^\lambda=\lambda^+
       \quad\Longrightarrow\quad 2^\kappa=\kappa^+.
 \tag{18}
\]

This is correctly stated. Its exact first-failure reformulation is:

> The first failure of GCH cannot occur at a singular cardinal of
> uncountable cofinality.

The initially inspected paragraph used `SCH` in that purported equivalent
reformulation. The actual passage has now been changed to `GCH`.
The antecedent in (18) asserts GCH at
**every** smaller infinite cardinal. A hypothesis mentioning only
singular strong-limit cardinals is a different condition.

The primary article's actual **Theorem 2.1**, printed p. 267, is stronger:
if `kappa` is singular of uncountable cofinality and the set of cardinals

\[
 \{\nu<\kappa:2^\nu=\nu^+\}
 \tag{19}
\]

is stationary in `kappa`, then `2^kappa=kappa^+`. The article defines
stationary here as meeting every closed cofinal subset of `kappa`.
The current hypothesis of GCH everywhere below `kappa` implies this
stationarity, giving (18); the article also states (18) in its
introduction on p. 265.

Silver's stronger results support additional reflection formulations,
but these should not be silently identified with (18). The name SCH is
used with different scopes in the literature, including the strong-limit
version and formulations concerning `kappa^(cf kappa)`. No such additional
version is needed for the proposed introductory section. State (18),
use its GCH reformulation, and state the PCF consequence (16) with its
own explicit strong-limit hypothesis.

## 8. Bibliography and incorporation packet

The existing `Shelah1994Cardinal` entry remains the comprehensive
reference. The added `Shelah1992Skeptics` entry has the following
metadata (the actual bibliography separates the journal name and
`New Series` into its journal and series fields):

```bibtex
@article{Shelah1992Skeptics,
  author       = {Shelah, Saharon},
  title        = {Cardinal Arithmetic for Skeptics},
  journaltitle = {Bulletin of the American Mathematical Society (New Series)},
  volume       = {26},
  number       = {2},
  pages        = {197--210},
  year         = {1992},
  doi          = {10.1090/S0273-0979-1992-00261-6},
  url          = {https://shelah.logic.at/files/95288/400a.pdf}
}
```

## 9. Actual source-alignment review

The inserted section and bibliography were read after the source packet
was drafted. The source-alignment checks pass:

- `thm:p06-pcf-maximum` has the exact progressive-set hypothesis and
  states both existence of a maximum and its equality with the pointwise
  product's cofinality. Main Theorem 4.3 on printed p. 202 supports it.
  The extra cardinality bound in (12) is not needed for the narrower
  statement selected for the reader.
- `thm:p06-shelah-aleph-omega-bound` states the strict inequality in
  Theorem A with exactly ZFC and the strong-limit hypothesis. The
  meaning of `omega_4` and the equivalent family of finite-index
  power-set hypotheses are correct.
- `thm:p06-silver` now says first failure of GCH, which matches its
  displayed hypothesis and conclusion. Its statement is the original
  paper's explicitly described corollary of Theorem 2.1.
- `Shelah1992Skeptics` records the correct title, journal, series,
  volume, issue, pages, year, DOI, and author-hosted published scan.

No source-scope repair was identified. Another reader is assigned the
elementary proofs and examples; this final check does not duplicate or
claim that independent review. The source packet itself contains the
elementary derivations above. The resulting section is a substantive
introductory treatment with accurately cited deep results, without a
generator theorem, pseudopower calculus, or monograph reconstruction.

Only this note was created. No handbook files were edited, no tests,
builds, or renders were run, and no additional agents were started.
