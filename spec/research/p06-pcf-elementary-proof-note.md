# Elementary pcf facts and conditional introductory consequences

Date: 2026-09-06.

This packet proves the elementary quotient and cofinality facts. The
existence of a largest possible cofinality for an infinite progressive
set, and its identification with the pointwise product cofinality, are
explicitly isolated as the basic-theorem premise (BT). That premise
is neither proved nor source-verified in this note.

Work in ZFC, with cardinals identified with their initial ordinals.
The current reader pointer was located in
handbook/parts/p06/cardinal-arithmetic-supplement.tex, beginning at
line 241 when read. Only this research note was written.

## 1. The product and its ultrafilter quotient

Let \(a\) be a nonempty set of infinite regular cardinals. Define
\[
 \prod a=
 \{f:\operatorname{dom}(f)=a\text{ and }
                    f(\kappa)<\kappa\text{ for every }\kappa\in a\}.
\]
The constant-zero function belongs to this product, so it is nonempty.
Let \(D\) be a proper ultrafilter on \(a\). Thus \(D\) contains \(a\),
does not contain the empty set, is closed under finite intersections
and supersets, and for each \(X\subseteq a\) contains exactly one of
\(X,a\setminus X\).

For \(f,g\in\prod a\), put
\[
 f=_D g\quad\Longleftrightarrow\quad
          \{\kappa:f(\kappa)=g(\kappa)\}\in D,
\]
\[
 f\leq_D g\quad\Longleftrightarrow\quad
          \{\kappa:f(\kappa)\leq g(\kappa)\}\in D.
\]
The notation \(\prod a/D\) means the set of \(=_D\)-equivalence
classes, ordered by
\[
 [f]_D\leq[g]_D\quad\Longleftrightarrow\quad f\leq_D g.
\]

### Equivalence and representative independence

Reflexivity and symmetry of \(=_D\) are immediate. If \(f=_D g\) and
\(g=_D h\), the intersection of their equality sets belongs to \(D\)
and is contained in the equality set of \(f,h\). Thus \(f=_D h\).

Suppose \(f=_D f'\) and \(g=_D g'\). Their two equality sets have an
intersection \(E\in D\). On \(E\), the comparisons \(f\leq g\) and
\(f'\leq g'\) coincide. If the first comparison set belongs to \(D\),
intersecting with \(E\) and using upward closure shows that the
second belongs to \(D\). The converse is symmetric. Hence the
quotient comparison is well defined.

### The quotient is a total order

Reflexivity follows from \(a\in D\). Transitivity follows by
intersecting the two comparison sets and using coordinatewise
transitivity. If both \(f\leq_D g\) and \(g\leq_D f\), the intersection
of the two comparison sets is the equality set, so \(f=_D g\).
This gives antisymmetry on equivalence classes.

For totality, let \(E=\{\kappa:f(\kappa)\leq g(\kappa)\}\).
If \(E\in D\), the first comparison holds. Otherwise
\(a\setminus E=\{\kappa:g(\kappa)<f(\kappa)\}\in D\), and therefore
\(g\leq_D f\). Thus every pair of quotient elements is comparable.
The induced strict comparison satisfies
\[
 [f]_D<[g]_D
 \quad\Longleftrightarrow\quad
 \{\kappa:f(\kappa)<g(\kappa)\}\in D.
\]

### There is no greatest element

For any \(f\in\prod a\), define \(g(\kappa)=f(\kappa)+1\).
Every infinite cardinal, viewed as its initial ordinal, is a limit
ordinal, so \(f(\kappa)+1<\kappa\). Thus \(g\in\prod a\) and
\[
 \{\kappa:f(\kappa)<g(\kappa)\}=a\in D.
\]
Consequently \([f]_D<[g]_D\). The quotient is a nonempty set-sized
linear order with no greatest element.

This does not assert that the quotient is well ordered.

## 2. Cofinality of a linear order without a greatest element

For a nonempty partially ordered set \(P\), define
\[
 \operatorname{cof}(P)=
 \min\{|C|:C\subseteq P\text{ and }
                       \forall p\in P\ \exists c\in C\ (p\leq c)\}.
\]
The minimum exists in ZFC because \(P\) itself is cofinal and cardinals
are well ordered. A set \(C\) satisfying the displayed condition is
cofinal.

**Lemma.** If \(L\) is a nonempty linear order without a greatest
element, then \(\mu=\operatorname{cof}(L)\) is an infinite regular
cardinal. There is a strictly increasing cofinal sequence
\((b_\alpha)_{\alpha<\mu}\) in \(L\).

First, no finite set is cofinal: a nonempty finite subset of a linear
order has a largest member, which would then be greatest in all of
\(L\). The empty set is not cofinal because \(L\) is nonempty.
Hence \(\mu\) is infinite.

Choose a cofinal set enumerated as \((c_\alpha)_{\alpha<\mu}\).
Fix a well-order of the underlying set of \(L\), used solely to make
the following choices definite. Suppose \(b_\beta\) has been chosen
for \(\beta<\alpha<\mu\). The set
\[
 \{b_\beta:\beta<\alpha\}\cup\{c_\alpha\}
\]
has cardinality less than \(\mu\), since \(\mu\) is an initial ordinal.
It is therefore not cofinal. In a linear order, failure of cofinality
means that there is an element strictly above every member of this
set. Choose the first such element in the fixed well-order as
\(b_\alpha\).

This recursion gives a strictly increasing sequence, and
\(c_\alpha<b_\alpha\) at every stage makes it cofinal in \(L\).
No regularity assumption on \(\mu\) was used in constructing it.

If \(\mu\) were singular, choose a cofinal set
\(I\subseteq\mu\) with \(|I|=\operatorname{cf}(\mu)<\mu\).
The subsequence \(\{b_\alpha:\alpha\in I\}\) would be cofinal in \(L\):
after any index witnessing a bound, some index in \(I\) is at least
that large. This contradicts the minimality of \(\mu\).
Thus \(\mu\) is regular.

Applied to the quotient in Section 1, the lemma proves that
\(\operatorname{cof}(\prod a/D)\) is an infinite regular cardinal and
is witnessed by a strictly increasing cofinal sequence.
Here this is an ordinary cofinality of a linear order. One must not
transfer this regularity assertion to arbitrary partial orders.

## 3. Definition of pcf, principal ultrafilters, and finite sets

Define
\[
 \operatorname{pcf}(a)=
 \{\operatorname{cof}(\prod a/D):
                         D\text{ a proper ultrafilter on }a\}.
\]
All ultrafilters are included, including principal ones. This is a
set of infinite regular cardinals by the preceding proof.

Fix \(\kappa\in a\), and let
\[
 D_\kappa=\{X\subseteq a:\kappa\in X\}.
\]
The evaluation map
\[
 [f]_{D_\kappa}\longmapsto f(\kappa)
\]
is an order isomorphism from \(\prod a/D_\kappa\) onto the ordinal
\(\kappa\). Indeed, equality and comparison modulo this ultrafilter
are exactly equality and comparison at coordinate \(\kappa\).
Every \(\alpha<\kappa\) is attained by the function taking value
\(\alpha\) at \(\kappa\) and zero elsewhere. Since \(\kappa\) is
regular,
\[
 \operatorname{cof}(\prod a/D_\kappa)
       =\operatorname{cf}(\kappa)=\kappa.
\]
It follows that
\[
 a\subseteq\operatorname{pcf}(a).
\]

If \(a\) is finite, every proper ultrafilter on \(a\) is principal.
Otherwise no singleton would belong to \(D\), so every complement
of a singleton would belong to \(D\); their finite intersection is
empty, contradicting properness. Once \(\{\kappa\}\in D\), upward
closure and properness identify \(D\) with \(D_\kappa\).
Therefore, for every finite nonempty set \(a\) of infinite regular
cardinals,
\[
 \operatorname{pcf}(a)=a.
\]
In particular its maximum in this finite case is simply \(\max a\).
This finite-case conclusion does not use the deep basic pcf theorem.

The factor regularity assumption matters here. For a principal
ultrafilter on a singular factor, the quotient is still isomorphic
to that factor as an ordinal, but its cofinality would be
\(\operatorname{cf}(\kappa)\), not \(\kappa\).

## 4. Unconditional cardinality bounds for possible cofinalities

For every ultrafilter \(D\),
\[
 \operatorname{cof}(\prod a/D)
       \leq|\prod a/D|
       \leq|\prod a|.
\]
The first inequality uses the whole quotient as a cofinal set.
The second follows from the quotient surjection, with cardinal
comparisons in ZFC.

Consequently
\[
 \sup a\leq\sup\operatorname{pcf}(a)\leq|\prod a|.
\]
These inequalities do not assert that the supremum of
\(\operatorname{pcf}(a)\) is attained. If a maximum is known to exist,
say \(\lambda=\max\operatorname{pcf}(a)\), they give
\[
 \sup a\leq\lambda\leq|\prod a|.
 \tag{1}
\]
The maximum, being a member of \(\operatorname{pcf}(a)\), is regular.

## 5. The separately assumed basic theorem

A nonempty set \(a\) of infinite regular cardinals is progressive when
\[
 |a|<\min a.
\]
The pointwise partial order on the full product is
\[
 f\leq_{\mathrm{pt}}g
       \quad\Longleftrightarrow\quad
       \forall\kappa\in a\ (f(\kappa)\leq g(\kappa)).
\]
Its cofinality means the least cardinality of a subset cofinal for
this comparison. This is not an eventual comparison, comparison
modulo an ideal, or comparison in one chosen ultrafilter quotient.

The conditional premise for the remaining consequences is:

**(BT)** For the progressive set \(a\) under consideration,
\(\operatorname{pcf}(a)\) has a largest member and
\[
 \max\operatorname{pcf}(a)
       =\operatorname{cof}(\prod a,\leq_{\mathrm{pt}}).
\]

The exact general theorem supplying (BT) is being established from
the specialist's source reading. Nothing in this packet is a proof
of (BT). The conclusions below hold assuming that premise.

In fact the bounds in (1) use only the existence of the maximum;
the additional equality in (BT) identifies that maximum with the
pointwise product cofinality. Thus, under (BT),
\[
 \sup a\leq
 \max\operatorname{pcf}(a)
 =\operatorname{cof}(\prod a,\leq_{\mathrm{pt}})
 \leq|\prod a|.
 \tag{2}
\]

## 6. Why the maximum is strictly larger than the supremum

Assume that \(a\) is progressive, has no largest element, and
satisfies (BT). Put
\[
 \mu=\sup a,\qquad \lambda=\max\operatorname{pcf}(a).
\]
The supremum of a set of cardinals is a cardinal. Since \(a\) has
no largest element, \(a\subseteq\mu\) is cofinal in \(\mu\); hence
\[
 \operatorname{cf}(\mu)\leq|a|<\min a\leq\mu.
\]
In particular \(\operatorname{cf}(\mu)<\mu\), so \(\mu\) is singular.
By Section 2, \(\lambda\) is regular. From (1), \(\lambda\geq\mu\).
Equality would make the same infinite cardinal both singular and
regular, which is impossible. Therefore
\[
 \max\operatorname{pcf}(a)>\sup a,
 \qquad
 \max\operatorname{pcf}(a)\geq(\sup a)^+.
 \tag{3}
\]

Progressiveness is used in the singularity argument. Absence of a
largest element by itself does not ensure that a supremum of regular
cardinals is singular: a cofinal set of regular cardinals below a
regular limit cardinal can have that regular cardinal as supremum.
Nor does the lack of a greatest element in an individual quotient
imply the strict inequality (3). The proof requires regularity of an
attained possible cofinality together with singularity of \(\sup a\).

## 7. The countable sequence below \(\aleph_\omega\)

Let
\[
 a=\{\aleph_{n+1}:n<\omega\},
 \qquad \mu=\aleph_\omega.
\]
In ZFC these factors are infinite regular cardinals: each is a
successor cardinal. For completeness, if an infinite successor
cardinal \(\kappa^+\) had a cofinal sequence of length at most
\(\kappa\), it would be a union of at most \(\kappa\) ordinals
of cardinality at most \(\kappa\), contradicting its cardinality.
Thus its cofinality is \(\kappa^+\).

The set \(a\) is countably infinite, has minimum \(\aleph_1\), has no
largest element, and has supremum \(\mu=\aleph_\omega\). Therefore
\[
 |a|=\aleph_0<\aleph_1=\min a,
\]
so it is progressive. Its displayed increasing sequence also gives
\(\operatorname{cf}(\mu)=\omega\).

Assuming (BT) for this \(a\), equation (3) gives
\[
 \max\operatorname{pcf}
       (\{\aleph_{n+1}:n<\omega\})
       \geq\aleph_{\omega+1}.
 \tag{4}
\]
This is a conditional application of (BT), not an elementary proof
that the maximum exists.

For the upper bound, each product function can be regarded as a
function \(\omega\to\mu\), and its graph is a subset of
\(\omega\times\mu\). Since \(|\omega\times\mu|=\mu\),
\[
 |\prod a|\leq\mu^\omega\leq 2^\mu.
 \tag{5}
\]
The second inequality also follows directly from the graph encoding.
If, in addition,
\[
 2^{\aleph_\omega}=\aleph_{\omega+1},
\]
then (2), (4), and (5) yield
\[
 \aleph_{\omega+1}
 \leq\max\operatorname{pcf}(a)
 \leq|\prod a|
 \leq2^{\aleph_\omega}
 =\aleph_{\omega+1}.
\]
Hence, under the two stated premises,
\[
 \max\operatorname{pcf}(a)=\aleph_{\omega+1}.
\]
The same squeeze also gives \(|\prod a|=\aleph_{\omega+1}\).
No extra strong-limit or GCH-below-\(\aleph_\omega\) hypothesis is
used in this calculation.

## Review outcome and scope

The quotient order, its increasing cofinal sequence and regular
cofinality, the principal-ultrafilter computation, and the finite-set
identity are proved unconditionally in the stated ZFC setting.
The bounds involving an actual maximum for an infinite progressive
set, and the \(\aleph_\omega\) example, are explicitly conditional
on (BT). Equality in the final example additionally assumes the
displayed value of \(2^{\aleph_\omega}\).

No theorem here identifies a general partial order's cofinality
with an ordinal order type, asserts that an ultrafilter quotient is
well ordered, or establishes the deep existence-of-maximum theorem.
No handbook changes, tests, builds, renders, or extra agents were used.
