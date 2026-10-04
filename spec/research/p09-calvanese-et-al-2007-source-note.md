# Calvanese et al. (2007), *Tractable Reasoning and Efficient Query Answering in Description Logics: The DL-Lite Family*

## Scope and source discipline

This note records the source truth needed for presentation N-c-010.b. It is based on the complete author-hosted *Journal of Automated Reasoning* article and, only for the later OWL 2 QL comparison, the dated W3C OWL 2 Profiles Recommendation. No secondary exposition was used.

All description-logic names below are source names. Each is given its syntactic category and semantics before it is used. Observations or repairs supplied by this note are explicitly marked as such and are not attributed to the article.

## Exact identity, access, and local custody

### Article

- Diego Calvanese, Giuseppe De Giacomo, Domenico Lembo, Maurizio Lenzerini, and Riccardo Rosati, “Tractable Reasoning and Efficient Query Answering in Description Logics: The DL-Lite Family,” *Journal of Automated Reasoning* 39(3), 385-429 (2007).
- DOI: <https://doi.org/10.1007/s10817-007-9078-x>.
- Received 1 May 2006; accepted 1 April 2007; published online 20 July 2007 (paper p. 385).
- Author publication page: <https://www.inf.unibz.it/~calvanese/papers-html/JAR-2007.html>.
- Author-hosted PDF: <https://www.inf.unibz.it/~calvanese/papers/calv-etal-JAR-2007.pdf>.
- Accessed 2026-08-22.
- Local PDF: tmp/pdfs/p09-calvanese-et-al-2007/calv-etal-JAR-2007.pdf.
- PDF byte length: 878,072.
- PDF SHA-256: 3ADF046934B01EAEDB9783F406B129C414515E6A187F2EC7E52008F072AA8164.
- PDF structure: 45 pages, unencrypted, PDF 1.3. The first PDF page is printed journal p. 385, so for this file
  \[
  \text{printed page}=\text{one-based PDF page}+384.
  \]
- Local layout-preserving text extraction: tmp/pdfs/p09-calvanese-et-al-2007/calv-etal-JAR-2007.txt, SHA-256 F9350B186A8F2121E7C4CBF5E64C127D98FA0921740D849CF86359A80188C2DE. This extraction is an aid only; all operative formulas, algorithm figures, and theorem statements were checked against rendered pages.
- Local author-page snapshot: tmp/pdfs/p09-calvanese-et-al-2007/author-landing-page.html, SHA-256 996AE3AEAA41CD12BBB97C6FC63F08C7571C81EEE1CFA7417D55B396C2BFE82D.

### Later canonical source used only for the OWL 2 QL boundary

- W3C, *OWL 2 Web Ontology Language Profiles (Second Edition)*, W3C Recommendation, 11 December 2012: <https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/>.
- Local snapshot: tmp/pdfs/p09-calvanese-et-al-2007/w3c-owl2-profiles-20121211.html, SHA-256 1599D792A39FE30000913822DEFFD78CB0905542C3EE3D956EFC9E51A7273C05.
- The 2009 first Recommendation postdates the 2007 article; the 2012 Second Edition is the fixed canonical text consulted here. It is not evidence for what the 2007 authors wrote.

## Page map

| Printed pages | PDF pages | Material |
|---|---:|---|
| 385-388 | 1-4 | Abstract and §1 introduction; contribution and complexity overview |
| 388-390 | 4-6 | §2 and §2.1: \(\mathrm{DL\mbox{-}Lite}_{core}\) grammar, KB/TBox/ABox syntax, interpretations, UNA, satisfaction |
| 390-392 | 6-8 | §2.2: \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\), \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\), functionality, Example 1, finite-model comparison |
| 392-393 | 8-9 | §2.3: FOL queries, CQs, UCQs, datalog notation, certain answers |
| 394-395 | 10-11 | §2.4-2.5: reasoning services, data/combined complexity, \(db(\mathcal A)\), FOL-reducibility |
| 395-405 | 11-21 | §3.1: PI/NI terminology, chase, canonical interpretation, NI-closure, satisfiability reduction |
| 405-410 | 21-26 | §3.2-3.3: implication reductions and traditional-reasoning complexity |
| 411-413 | 27-29 | §4: homomorphism from the canonical interpretation, UCQ evaluation, UCQ decomposition |
| 413-417 | 29-33 | §5.1: \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) query reformulation, Definition 32, Fig. 2 PerfectRef, Lemma 34, Examples 35-36 |
| 418 | 34 | §5.2: Answer, Theorem 37, Example 38, Fig. 3 |
| 419-421 | 35-37 | §5.3: Lemma 39 correctness proof and Theorem 40 |
| 421-422 | 37-38 | Theorem 41; §5.4, Lemma 42 and Theorems 43-44 |
| 422-424 | 38-40 | §6: transfer to \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\), Theorems 45-47 |
| 424-426 | 40-42 | §7, including Theorem 48 and extension boundaries |
| 426-427 | 42-43 | §8 conclusions and later DL-Lite extensions |
| 428-429 | 44-45 | References |

Rendered pages page-04.png through page-41.png correspond to printed pp. 388-425. The grammar, semantic equations, chase and consistency constructions, universal-model results, both algorithm figures, Examples 35-38, Lemmas 34/39/42, and Theorems 41/43/44/46/47/48 were visually inspected.

## The languages in §2 and §5

### Syntactic categories

The source assumes atomic concept names \(A\) and atomic role names \(P\). Their standing is syntactic: concepts denote unary sets and roles denote binary relations only after an interpretation is supplied.

For \(\mathrm{DL\mbox{-}Lite}_{core}\) (paper p. 389, §2.1):

\[
\begin{array}{rcl@{\qquad}rcl}
B &::=& A\mid \exists R,
&R&::=&P\mid P^{-},\\
C &::=& B\mid\neg B,
&E&::=&R\mid\neg R.
\end{array}
\]

- \(B\): basic concept.
- \(C\): general concept.
- \(R\): basic role.
- \(E\): general role.
- If \(R=P\), then \(R^{-}=P^{-}\); if \(R=P^{-}\), then \(R^{-}=P\).
- Double syntactic negation is normalized: \(\neg(\neg B)=B\) and \(\neg(\neg R)=R\).

The exact distinctions matter later: a core concept inclusion permits a basic concept, not an arbitrary general concept, on its left; PerfectRef rewrites only positive inclusions; query atoms use atomic concept and role names, not arbitrary \(B,C,R,E\).

### \(\mathrm{DL\mbox{-}Lite}_{core}\)

A knowledge base is an ordered pair
\[
\mathcal K=\langle\mathcal T,\mathcal A\rangle,
\]
where \(\mathcal T\) is a finite TBox and \(\mathcal A\) is a finite ABox (paper pp. 389-390).

- A core TBox contains inclusions \(B\sqsubseteq C\). Hence a positive right side is a basic concept and a negative right side is the complement of a basic concept. Cycles are allowed.
- A core ABox contains only atomic membership assertions \(A(a)\) and \(P(a,b)\).
- The paper does not take \(C(a)\) or \(E(a,b)\) as primitive ABox forms. It explains how \(C(a)\) can be simulated using a fresh atomic concept, and notes that the analogous role simulation requires an extension admitting role inclusions (pp. 389-390).

Union on the inclusion left and conjunction on the inclusion right would be eliminable shorthands: \(B_1\sqcup B_2\sqsubseteq C\) splits into two inclusions, and \(B\sqsubseteq C_1\sqcap C_2\) splits into two inclusions. The paper likewise notes that \(\bot\) on the left and \(\top\) on the right would add no expressive power (p. 389).

### \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\)

\(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) is \(\mathrm{DL\mbox{-}Lite}_{core}\) plus finite role inclusions
\[
R\sqsubseteq E
\]
with the \(R,E\) categories above (paper p. 390, §2.2). Thus it permits both positive basic-role inclusions \(R_1\sqsubseteq R_2\) and negative role inclusions \(R_1\sqsubseteq\neg R_2\). It does **not** add functionality assertions.

The paper says qualified existential restrictions on the right of concept inclusions can be simulated using role inclusions plus unqualified existentials and therefore are not included as primitive syntax (p. 390).

Section 5 is specifically about UCQ answering for \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\). Its rewriting consumes only positive inclusions in \(\mathcal T\); negative inclusions remain relevant to the prior consistency test.

### \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\)

\(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) is \(\mathrm{DL\mbox{-}Lite}_{core}\) plus assertions
\[
(\mathsf{funct}\ R)
\]
for a basic role \(R\) (paper p. 391, §2.2). It does **not** add role inclusions. Under an interpretation, \((\mathsf{funct}\ R)\) requires
\[
(o,o_1),(o,o_2)\in R^I\Longrightarrow o_1=o_2.
\]
Because \(R\) may be an inverse role, this also expresses inverse functionality of an atomic role.

The paper records that \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) has the finite-model property, while \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) does not; p. 392 gives a concrete \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) KB having only infinite models. This difference is not used by PerfectRef but prevents identifying the two variants.

## Interpretations, KB models, and the unique-name assumption

An interpretation \(I=(\Delta^I,\cdot^I)\) has a nonempty domain and assigns (paper p. 390):

\[
\begin{aligned}
A^I&\subseteq\Delta^I,\\
P^I&\subseteq\Delta^I\times\Delta^I,\\
(P^-)^I&=\{(o_2,o_1):(o_1,o_2)\in P^I\},\\
(\exists R)^I&=\{o:\exists o'\ (o,o')\in R^I\},\\
(\neg B)^I&=\Delta^I\setminus B^I,\\
(\neg R)^I&=(\Delta^I\times\Delta^I)\setminus R^I.
\end{aligned}
\]

Satisfaction is typed as follows:

- \(I\models C_1\sqsubseteq C_2\) iff \(C_1^I\subseteq C_2^I\).
- \(I\models E_1\sqsubseteq E_2\) iff \(E_1^I\subseteq E_2^I\).
- \(I\models A(a)\) iff \(a^I\in A^I\).
- \(I\models P(a,b)\) iff \((a^I,b^I)\in P^I\).
- \(I\models\mathcal K\) iff it satisfies every assertion in both \(\mathcal T\) and \(\mathcal A\).
- \(\mathcal K\) is satisfiable iff it has a model.
- \(\mathcal K\models\alpha\) (respectively \(\mathcal T\models\alpha\)) iff every model of \(\mathcal K\) (respectively \(\mathcal T\)) satisfies \(\alpha\).

The article explicitly assigns each individual constant a distinct domain object and says that it enforces the unique-name assumption (UNA) (p. 390). Consequently, equality of object-language names is not treated as an open possibility in this paper's semantics. This assumption must be stated whenever the 2007 construction is presented.

## Queries and certain answers

### FOL, CQ, and UCQ types

On pp. 392-393 (§2.3), a query is an open first-order formula with equality,
\[
q=\{\vec x\mid\varphi(\vec x)\}.
\]
Its arity is \(|\vec x|\), and \(q^I\) is the set of tuples making \(\varphi\) true in \(I\). A Boolean query has no free variables; its value is either the singleton containing the empty tuple or the empty set.

A conjunctive query (CQ) has the form
\[
\{\vec x\mid\exists\vec y\,\mathit{conj}(\vec x,\vec y)\},
\]
where the matrix is a conjunction of atoms and equalities. A union of conjunctive queries (UCQ) is a finite disjunction of such matrices with the same free tuple.

The datalog display
\[
q(\vec x')\leftarrow \mathit{conj}'(\vec x',\vec y')
\]
is obtained after eliminating equality atoms by identifying the relevant variables and constants. Thus the displayed tuples may contain constants or repeated variables. Variables in the head are distinguished; existential body-only variables are non-distinguished.

The source does not spell out the inconsistent identification case. Under its UNA, the type-correct preprocessing takes the equivalence closure generated by the equality atoms. If one equivalence class contains two distinct constants, that CQ is false in every source interpretation and its disjunct is removed from a UCQ. Otherwise each class is replaced by its unique constant when present, or by one representative variable, and the equality atoms are deleted. PerfectRef applies only to the surviving equality-free CQs. This is an eliminable consequence of the printed query grammar plus UNA, not a separately printed algorithm.

A CQ over \(\mathcal K\) uses only atoms \(A(z)\) and \(P(z_1,z_2)\), where \(A,P\) are atomic names in \(\mathcal K\) and each argument is a variable or a constant in \(\mathcal K\). A UCQ over \(\mathcal K\) is a finite union of these CQs.

### Certain-answer semantics

For a query \(q\) and KB \(\mathcal K\), the article defines
\[
\operatorname{ans}(q,\mathcal K)
=
\{\vec a:\vec a\text{ is a tuple of constants occurring in }\mathcal K
\text{ and }\vec a^{\,M}\in q^M\text{ for every }M\models\mathcal K\}.
\]

This is all-model, or certain-answer, semantics. For a Boolean query, the empty tuple is an answer exactly when the sentence holds in every model. If \(\mathcal K\) is unsatisfiable, universal quantification over its empty model class makes every appropriately sized tuple an answer. The source denotes this finite set by \(\operatorname{AllTup}(q,\mathcal K)\) (p. 393).

## Complexity parameters actually used

The article formally defines only the following two parameter regimes (p. 394, §2.4):

- **Data complexity:** only \(|\mathcal A|\), the ABox size, varies; \(\mathcal T\) and the query are fixed.
- **Combined complexity:** all inputs to the recognition problem vary. For query answering this is \(|\mathcal K|+|Q|\), made explicit immediately before Theorem 44 (p. 422).

The source also makes two one-parameter observations without defining new complexity names:

- It measures PerfectRef reformulation time in \(|\mathcal T|\), with the query fixed and independently of the ABox (Lemma 42 and Theorem 43). Reading the claim as total answering time in the single parameter \(|\mathcal T|\) additionally fixes the ABox.
- It notes that worst-case query answering is exponential in query size (p. 388) and uses the query-size parameter \(n\) in Lemmas 34 and 42.

The expressions **taxonomic complexity** and **query complexity** do not occur in this 2007 article. They must not be attributed to it. The later W3C OWL 2 Profiles Recommendation does use a four-column taxonomy (taxonomic, data, query, combined) for OWL profiles, but that later table is neither the vocabulary nor the exact language of the 2007 paper.

## The ABox database and FOL-reducibility

For a nonempty ABox \(\mathcal A\), the paper defines the finite interpretation \(db(\mathcal A)\) (pp. 394-395):

\[
\begin{aligned}
\Delta^{db(\mathcal A)}&=\{a:a\text{ occurs in }\mathcal A\},\\
a^{db(\mathcal A)}&=a,\\
A^{db(\mathcal A)}&=\{a:A(a)\in\mathcal A\},\\
P^{db(\mathcal A)}&=\{(a_1,a_2):P(a_1,a_2)\in\mathcal A\}.
\end{aligned}
\]

It is a minimal model of the ABox, not generally a model of the TBox.

The nonempty-ABox hypothesis is a typing boundary, not decoration: (db(\varnothing)) would have empty domain and would not be an interpretation under the paper's own nonempty-domain convention. Definitions 2--3 state the hypothesis explicitly, while several later uses of (db(\mathcal A)) omit it and one proof elsewhere uses an empty ABox. Every result presented through (db(\mathcal A)) must therefore retain (\mathcal A\neq\varnothing), or an independently typed empty-ABox case must be supplied. For these displayed DL-Lite variants, an empty ABox with any TBox is satisfiable in a nonempty one-element interpretation assigning every atomic concept and role the empty extension; non-Boolean active-domain answers then have no constants from which to form tuples.

Definition 2 says satisfiability in a DL \(L\) is FOL-reducible when, for each fixed \(L\)-TBox \(\mathcal T\), one Boolean FO query can be evaluated on every nonempty \(db(\mathcal A)\), returning false exactly for the satisfiable KBs \(\langle\mathcal T,\mathcal A\rangle\). The query is therefore a detector of a TBox/ABox contradiction.

Definition 3 says UCQ answering in \(L\) is FOL-reducible when, for every fixed \(\mathcal T\) and UCQ \(q\), there is an FO query \(q_1\), independent of \(\mathcal A\), such that for every nonempty \(\mathcal A\) and every tuple \(\vec a\) of constants occurring in \(\mathcal A\),
\[
\vec a\in\operatorname{ans}(q,\langle\mathcal T,\mathcal A\rangle)
\quad\Longleftrightarrow\quad
\vec a\in q_1^{db(\mathcal A)}.
\]

The printed definition says \(q_1\) is “over the alphabet of \(\mathcal T\).” In applications, the query vocabulary must also be available; Section 5 consistently assumes a query over \(\mathcal T\). A presentation should avoid turning this wording into the false claim that arbitrary predicates absent from \(\mathcal T\) can occur in \(q\) yet need not occur in \(q_1\).

FOL-reducibility is a uniform definability/rewrite property, not itself a complexity class. The paper derives a LOGSPACE data upper bound because the resulting FO query is fixed while only the finite structure \(db(\mathcal A)\) varies (Theorems 26, 43, and 47). It does not infer a LOGSPACE combined bound.

## Positive and negative inclusions used by the algorithms

At the start of §3 (p. 395), the paper introduces these metalinguistic classifications of TBox assertions:

- A positive inclusion (PI) is \(B_1\sqsubseteq B_2\) or, in \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\), \(R_1\sqsubseteq R_2\).
- A negative inclusion (NI) is \(B_1\sqsubseteq\neg B_2\) or, in \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\), \(R_1\sqsubseteq\neg R_2\).

Their standing is not that of new object-language constructors: they classify already well-formed inclusions according to the sign of the right side. The distinction is necessary because the chase and PerfectRef use PIs, whereas NIs and \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) functionality assertions are handled by consistency checking.

## Chase and canonical interpretation

### Role-orientation abbreviation

On p. 396 the source defines, for a basic role \(R\) and constants \(a,b\),
\[
\operatorname{ga}(R,a,b)=
\begin{cases}
P(a,b),&R=P,\\
P(b,a),&R=P^-.
\end{cases}
\]

This is a metalinguistic abbreviation for an ABox-shaped membership assertion. It is needed to state one chase rule for an atomic role and its inverse; it is not a role, concept, or KB assertion schema beyond the displayed expansion.

### Applicability to chase facts (Definition 4)

Let \(S\) be a set of membership assertions and \(\mathcal T_p\) a set of PIs. A PI \(\alpha\in\mathcal T_p\) is applicable in \(S\) to \(f\in S\) exactly in one of these cases:

1. \(\alpha=A_1\sqsubseteq A_2\), \(f=A_1(a)\), and \(A_2(a)\notin S\).
2. \(\alpha=A\sqsubseteq\exists R\), \(f=A(a)\), and no \(b\) satisfies \(\operatorname{ga}(R,a,b)\in S\).
3. \(\alpha=\exists R\sqsubseteq A\), \(f=\operatorname{ga}(R,a,b)\), and \(A(a)\notin S\).
4. \(\alpha=\exists R_1\sqsubseteq\exists R_2\), \(f=\operatorname{ga}(R_1,a,b)\), and no \(c\) satisfies \(\operatorname{ga}(R_2,a,c)\in S\).
5. \(\alpha=R_1\sqsubseteq R_2\), \(f=\operatorname{ga}(R_1,a,b)\), and \(\operatorname{ga}(R_2,a,b)\notin S\).

These five cases exhaust the possible positive inclusions obtained from the §2 grammars. Case 5 is available only in \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\).

### Definition 5, with the printed totality omission exposed

Let \(\Gamma_{\mathcal A}\) be the constants in \(\mathcal A\), let \(\Gamma_N\) be a fixed infinite set of fresh symbols, and let \(\Gamma_C=\Gamma_{\mathcal A}\cup\Gamma_N\) carry the fixed order used by the construction. The ABox facts are ordered first. The printed recursion starts with \(S_0=\mathcal A\). At stage \(j\), it chooses:

1. the first \(f\in S_j\) to which some PI is applicable;
2. the first applicable PI \(\alpha\);
3. a fresh \(a_{new}\in\Gamma_N\) ordered after all symbols already in \(S_j\).

It then adds exactly one fact according to:

\[
\begin{array}{lll}
\mathsf{cr1}:&A_1\sqsubseteq A_2,\ A_1(a)&\rightsquigarrow A_2(a),\\
\mathsf{cr2}:&A\sqsubseteq\exists R,\ A(a)&\rightsquigarrow \operatorname{ga}(R,a,a_{new}),\\
\mathsf{cr3}:&\exists R\sqsubseteq A,\ \operatorname{ga}(R,a,b)&\rightsquigarrow A(a),\\
\mathsf{cr4}:&\exists R_1\sqsubseteq\exists R_2,\ \operatorname{ga}(R_1,a,b)&\rightsquigarrow \operatorname{ga}(R_2,a,a_{new}),\\
\mathsf{cr5}:&R_1\sqsubseteq R_2,\ \operatorname{ga}(R_1,a,b)&\rightsquigarrow \operatorname{ga}(R_2,a,b).
\end{array}
\]

The article then writes
\[
\operatorname{chase}(\mathcal K)=\bigcup_{j\in\mathbb N}S_j,
\qquad
\operatorname{chase}_i(\mathcal K)=S_i.
\]

**Source omission:** Definition 5 does not say what \(S_{j+1}\) is when no PI is applicable in \(S_j\). As printed, the recursion is therefore partial for a finitely saturated chase, even though the infinite union is used later. The exact conservative completion is:
\[
\text{if no PI is applicable in }S_j,\quad S_{j+1}:=S_j.
\]
This adds no fact, changes no earlier stage, makes every \(S_j\) defined, and leaves the intended union unchanged. It is supplied here, not printed in the source.

Proposition 6 establishes fairness: if a PI is applicable to a fact at some finite stage, then the corresponding fact is eventually added. Its proof uses the finite number of facts preceding the selected fact and the finite number of PIs, each applicable at most once to a given fact (pp. 397-398).

### Canonical interpretation

On p. 398 the source defines
\[
\begin{aligned}
\Delta^{\operatorname{can}(\mathcal K)}&=\Gamma_C,\\
a^{\operatorname{can}(\mathcal K)}&=a\quad\text{for every symbol occurring in the chase},\\
A^{\operatorname{can}(\mathcal K)}&=\{a:A(a)\in\operatorname{chase}(\mathcal K)\},\\
P^{\operatorname{can}(\mathcal K)}&=\{(a_1,a_2):P(a_1,a_2)\in\operatorname{chase}(\mathcal K)\}.
\end{aligned}
\]

The finite-stage interpretation \(\operatorname{can}_i(\mathcal K)\) has the same domain and reads its predicate extensions from \(\operatorname{chase}_i(\mathcal K)\). In particular, the interpretations of the ABox predicates in \(\operatorname{can}_0(\mathcal K)\) agree with \(db(\mathcal A)\), though the canonical domain is larger.

Lemma 7 proves that \(\operatorname{can}(\mathcal K)\) satisfies the ABox and every PI. Each inclusion form is checked against fairness and the corresponding chase rule; the role-inclusion case is present only for \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) (pp. 398-399).

For \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\), Lemma 8 proves that canonical-model satisfaction of the functionality assertions is equivalent to their satisfaction already in \(db(\mathcal A)\). The local induction treats \(\mathsf{cr2}\) in detail, says \(\mathsf{cr4}\) is almost identical, and observes that the remaining rules cannot introduce a functionality violation (pp. 399-400).

Definition 9 forms the NI-closure \(cl_n(\mathcal T)\). Lemma 12 then proves
\[
\operatorname{can}(\mathcal K)\models\mathcal K
\quad\Longleftrightarrow\quad
db(\mathcal A)\models\langle cl_n(\mathcal T),\mathcal A\rangle.
\]
Lemma 14 proves that \(\operatorname{can}(\mathcal K)\models\mathcal K\) iff \(\mathcal K\) is satisfiable, and Theorem 15 combines these results (pp. 401-405).

### Homomorphism property needed for query answers

Lemma 28 (p. 411) states that for every satisfiable \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) or \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) KB \(\mathcal K\) and every model \(M\models\mathcal K\), there is a function
\[
\psi:\Delta^{\operatorname{can}(\mathcal K)}\to\Delta^M
\]
preserving all atomic concept and role facts. The proof maps each ABox constant to its denotation in \(M\), and when an existential chase rule creates a fresh symbol, maps that symbol to a witness supplied by \(M\).

**Source omission:** the induction assigns \(\psi\) only to ABox symbols and fresh symbols that actually enter the chase, although \(\Delta^{\operatorname{can}(\mathcal K)}=\Gamma_C\) also contains unused fresh symbols. Since \(\Delta^M\neq\varnothing\) and unused symbols occur in no canonical atomic fact, the exact completion is to map every unused symbol to any fixed element of \(\Delta^M\). This makes \(\psi\) total without affecting preservation. The completion is supplied here, not stated on p. 411.

Theorem 29 then proves, for satisfiable \(\mathcal K\) and any UCQ \(Q\),
\[
\operatorname{ans}(Q,\mathcal K)=Q^{\operatorname{can}(\mathcal K)}.
\]
As printed with the ordinary meaning of query extension, this equality is ill-typed: the left side contains tuples of constants occurring in \(\mathcal K\), whereas the right side can contain fresh chase elements. Its exact type-correct content for arity (r) is
\[
\operatorname{ans}(Q,\mathcal K)
=
\{\vec a\in\operatorname{Const}(\mathcal K)^r:
  \vec a^{\operatorname{can}(\mathcal K)}
  \in Q^{\operatorname{can}(\mathcal K)}\}.
\]
For example, from (A\sqsubseteq\exists P), \(\exists P^{-}\sqsubseteq B\), and (A(a)), the chase produces a fresh (e) with (B(e)); (e) belongs to the ordinary extension of (B(x)) but cannot be a certain-answer constant. The right-to-left direction for the restricted set composes a match of a CQ disjunct in the canonical interpretation with the homomorphism into an arbitrary model. The property is stated to extend to positive FO queries but not to arbitrary FO queries (p. 412).

Theorem 31 proves that certain answers distribute over a UCQ:
\[
\operatorname{ans}(Q,\mathcal K)=\bigcup_{q_i\in Q}\operatorname{ans}(q_i,\mathcal K).
\]
For inconsistent \(\mathcal K\), both sides are the appropriate all-tuples set; for satisfiable \(\mathcal K\), the proof uses Theorem 29. The printed proof says “by Theorem 28” at the decisive evaluation step on p. 413; the required citation is Theorem 29. Lemma 28 alone gives only the homomorphism.

## PerfectRef: complete typed specification

### Bound and unbound query arguments

On p. 414 (§5.1), an argument occurrence is **bound** exactly when it is:

- a distinguished variable;
- a shared variable, meaning a variable occurring at least twice in the query body; or
- a constant.

An argument is **unbound** exactly when it is a non-distinguished variable occurring only once in the body. The printed underscore \(\_\) represents such a variable. Each underscore occurrence is treated as a different variable during unification; it is not an object-language constant and two underscores are not automatically equal.

### When a PI is applicable to a query atom

For a unary atom \(A(x)\), a PI is applicable iff its right-hand side is \(A\).

For a binary atom \(P(x_1,x_2)\), a PI \(I\) is applicable exactly when at least one holds:

1. \(x_2=\_\) and the right side of \(I\) is \(\exists P\);
2. \(x_1=\_\) and the right side of \(I\) is \(\exists P^-\);
3. \(I\) is a role inclusion whose right side is \(P\) or \(P^-\).

The unbound-position conditions prevent a backward existential rewrite from deleting a join, output variable, or constant constraint.

### Definition 32: all rewrite atoms

For an applicable \(I\), \(\operatorname{gr}(g,I)\) is exactly:

| Atom \(g\) | PI \(I\) | \(\operatorname{gr}(g,I)\) |
|---|---|---|
| \(A(x)\) | \(A_1\sqsubseteq A\) | \(A_1(x)\) |
| \(A(x)\) | \(\exists P\sqsubseteq A\) | \(P(x,\_)\) |
| \(A(x)\) | \(\exists P^-\sqsubseteq A\) | \(P(\_,x)\) |
| \(P(x,\_)\) | \(A\sqsubseteq\exists P\) | \(A(x)\) |
| \(P(x,\_)\) | \(\exists P_1\sqsubseteq\exists P\) | \(P_1(x,\_)\) |
| \(P(x,\_)\) | \(\exists P_1^-\sqsubseteq\exists P\) | \(P_1(\_,x)\) |
| \(P(\_,x)\) | \(A\sqsubseteq\exists P^-\) | \(A(x)\) |
| \(P(\_,x)\) | \(\exists P_1\sqsubseteq\exists P^-\) | \(P_1(x,\_)\) |
| \(P(\_,x)\) | \(\exists P_1^-\sqsubseteq\exists P^-\) | \(P_1(\_,x)\) |
| \(P(x_1,x_2)\) | \(P_1\sqsubseteq P\) or \(P_1^-\sqsubseteq P^-\) | \(P_1(x_1,x_2)\) |
| \(P(x_1,x_2)\) | \(P_1\sqsubseteq P^-\) or \(P_1^-\sqsubseteq P\) | \(P_1(x_2,x_1)\) |

The first nine rows are concept-inclusion rewrites. The last two are the role-inclusion rewrites available in \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\).

### Replacement, reduction, and underscore normalization

- \(q[g/g']\) replaces the selected body atom \(g\) by \(g'\).
- \(\operatorname{reduce}(q,g_1,g_2)\) applies a most general unifier of the two body atoms to the whole CQ and identifies the now-duplicate atom. This is why the number of body atoms drops in Example 33 and Lemma 34.
- During that unification, every underscore occurrence is first treated as a distinct non-distinguished variable. A unifier substitutes an underscore on one side by the corresponding argument on the other; two matched underscores yield an underscore.
- \(\tau(q)\) replaces every variable that is non-distinguished and non-shared *after* reduction by an underscore. This second pass is necessary because unification can turn a formerly shared variable into an unbound one (pp. 415-416).

### Figure 2 control flow

The following preserves the source's variables, update expressions, and loop order; spacing and assignment arrows are normalized for Markdown:

~~~text
PerfectRef(q,T)
input: CQ q; TBox T
output: UCQ PR

PR := {q}
repeat
    PR' := PR
    for each q' in PR' do
        (a) for each atom g in q' do
                for each PI I in T do
                    if I is applicable to g then
                        PR := PR union { q'[g/gr(g,I)] }
        (b) for each pair g1,g2 in q' do
                if g1 and g2 unify then
                    PR := PR union { tau(reduce(q',g1,g2)) }
until PR' = PR
return PR
~~~

The outer collection is a set: adding an already present query changes nothing. Newly generated queries are processed in a later repeat-cycle, because the current cycle ranges over the saved \(PR'\).

## Lemma 34: termination, including the safe finite bound

**Exact scope and conclusion (p. 416):** for every \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) TBox \(\mathcal T\) and every CQ \(q\) over \(\mathcal T\), \(\operatorname{PerfectRef}(q,\mathcal T)\) terminates.

The local proof uses:

1. no generated body has more atoms than the initial body;
2. no new term other than the underscore is introduced;
3. if \(n\) is query size and \(m\) is the number of concept/role names in \(\mathcal T\) or \(q\), at most \(m(n+1)^2\) distinct unary-or-binary atoms can be formed;
4. generated queries remain in the set \(PR\).

The source prints \((m(n+1)^2)^n\) as an upper bound on the number of distinct generated CQs. Its \(n\) is only specified as a query-size measure proportional to the numbers of atoms and terms, so this is best read as a coarse coding bound rather than as an exact enumeration of head/body presentations. In particular, the proof does not spell out how shorter bodies and heads changed by unification are encoded within that power. None of this threatens the two conclusions for which the count is used: finiteness, and polynomial dependence on \(m\) when the input query is fixed.

A sufficient repaired bound is immediate. Put \(a=m(n+1)^2\). There are at most
\[
(n+1)^n\sum_{i=0}^{n}a^i
\le (n+1)^{n+1}a^n
\]
head/body presentations using the existing terms, for \(a\ge1\); quotienting by atom order, duplicate removal, or variable renaming only decreases this number. If the input has no body atom, termination is immediate and the displayed count is unnecessary. Thus the state space is finite. Every cycle that fails the stopping test adds at least one new set element, so termination follows. For fixed \(q\), this corrected bound is still polynomial in \(m\), preserving Lemma 42.

## Fully traced Examples 35 and 38

Example 35 (p. 417) uses the \(\mathrm{DL\mbox{-}Lite}_{core}\) TBox from Example 1:

\[
\begin{aligned}
\mathsf{Professor}&\sqsubseteq\exists\mathsf{TeachesTo},\\
\mathsf{Student}&\sqsubseteq\exists\mathsf{HasTutor},\\
\exists\mathsf{TeachesTo}^{-}&\sqsubseteq\mathsf{Student},\\
\exists\mathsf{HasTutor}^{-}&\sqsubseteq\mathsf{Professor},\\
\mathsf{Professor}&\sqsubseteq\neg\mathsf{Student}.
\end{aligned}
\]

The input query is
\[
q_0(x)\leftarrow
\mathsf{TeachesTo}(x,y),\mathsf{HasTutor}(y,\_).
\]

PerfectRef reaches the following queries:

1. Apply \(\mathsf{Student}\sqsubseteq\exists\mathsf{HasTutor}\) backward to the second atom:
   \[
   q_1(x)\leftarrow\mathsf{TeachesTo}(x,y),\mathsf{Student}(y).
   \]
2. Apply \(\exists\mathsf{TeachesTo}^{-}\sqsubseteq\mathsf{Student}\) backward:
   \[
   q_2(x)\leftarrow\mathsf{TeachesTo}(x,y),\mathsf{TeachesTo}(\_,y).
   \]
3. The two atoms of \(q_2\) unify. Reduction identifies them, and \(\tau\) makes the now-unbound second argument an underscore:
   \[
   q_3(x)\leftarrow\mathsf{TeachesTo}(x,\_).
   \]
4. Apply \(\mathsf{Professor}\sqsubseteq\exists\mathsf{TeachesTo}\) backward:
   \[
   q_4(x)\leftarrow\mathsf{Professor}(x).
   \]
5. Apply \(\exists\mathsf{HasTutor}^{-}\sqsubseteq\mathsf{Professor}\) backward:
   \[
   q_5(x)\leftarrow\mathsf{HasTutor}(\_,x).
   \]

The returned UCQ contains \(q_0,\ldots,q_5\). The negative inclusion is never used by PerfectRef; it belongs to consistency checking.

Example 38 (p. 418) evaluates that UCQ on
\[
\mathcal A=\{
\mathsf{Student}(\mathsf{John}),
\mathsf{HasTutor}(\mathsf{John},\mathsf{Mary}),
\mathsf{TeachesTo}(\mathsf{Mary},\mathsf{Bill})
\}.
\]

The atom-level evaluation is:

- \(q_0\): no answer, because the only \(\mathsf{TeachesTo}\) target is Bill and no \(\mathsf{HasTutor}(\mathsf{Bill},\_)\) fact is present;
- \(q_1\): no answer, because Bill is not asserted \(\mathsf{Student}\) in \(db(\mathcal A)\);
- \(q_2\): Mary, using the same \(\mathsf{TeachesTo}(\mathsf{Mary},\mathsf{Bill})\) tuple for both unifiable atoms;
- \(q_3\): Mary;
- \(q_4\): no direct \(\mathsf{Professor}\) fact;
- \(q_5\): Mary, from \(\mathsf{HasTutor}(\mathsf{John},\mathsf{Mary})\).

The union is therefore exactly \(\{\mathsf{Mary}\}\), as printed.

For completeness, Examples 36 and 38 also give a role-inclusion trace. Add
\[
\mathsf{HasTutor}^{-}\sqsubseteq\mathsf{TeachesTo}
\]
and start from \(q'(x)\leftarrow\mathsf{Student}(x)\). PerfectRef returns
\[
\mathsf{Student}(x),\qquad
\mathsf{TeachesTo}(\_,x),\qquad
\mathsf{HasTutor}(x,\_).
\]
On the second Example 38 ABox containing only \(\mathsf{HasTutor}(\mathsf{John},\mathsf{Mary})\) and \(\mathsf{TeachesTo}(\mathsf{Mary},\mathsf{Bill})\), these return John and Bill, respectively, so the answer is \(\{\mathsf{John},\mathsf{Bill}\}\). Without the added role inclusion, only Bill is returned.

## Lemma 39: exact correctness claim and proof structure

**Printed and type-corrected scope (pp. 419-421):** the lemma says “every ABox,” but its conclusion evaluates (db(\mathcal A)), which Definition 3 supplies only for nonempty ABoxes. Thus let \(\mathcal T\) be a \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) TBox, \(q\) a CQ over \(\mathcal T\), \(PR=\operatorname{PerfectRef}(q,\mathcal T)\), and \(\mathcal A\neq\varnothing\) an ABox such that \(\mathcal K=\langle\mathcal T,\mathcal A\rangle\) is satisfiable. Then
\[
\operatorname{ans}(q,\mathcal K)=PR^{db(\mathcal A)}.
\]

The satisfiability hypothesis is essential. Inconsistent KBs are handled later by Answer, which returns all tuples.

The proof first identifies a match of \(q(\vec t)\) in the chase with a finite set \(G\) of chase membership assertions produced by substituting the query's non-distinguished variables. For a CQ of arity \(r\), the constant-restricted form of Theorem 29 reduces the claim to the type-correct equation
\[
\{\vec a\in\operatorname{Const}(\mathcal K)^r:
  \vec a^{\operatorname{can}(\mathcal K)}
  \in q^{\operatorname{can}(\mathcal K)}\}
=
\bigcup_{\widehat q\in PR}\widehat q^{db(\mathcal A)}.
\]

### Rewriting-to-canonical direction

For a step-(a) rewrite, the applicable PI guarantees that every match of the rewritten atom in the canonical interpretation yields a match of the prior atom. The paper writes out \(A_1\sqsubseteq A\); all other Definition 32 forms are said to be analogous. For step (b), a match of the reduced query is also a match of the unreduced query. Iterating backward to the input gives
\[
\widehat q^{\operatorname{can}(\mathcal K)}\subseteq q^{\operatorname{can}(\mathcal K)}.
\]
Since every ABox fact is a chase fact and CQs are positive,
\[
\widehat q^{db(\mathcal A)}\subseteq\widehat q^{\operatorname{can}(\mathcal K)},
\]
which supplies the displayed inclusion needed for soundness.

### Canonical-to-rewriting direction

Any finite CQ match in the union chase lies in some finite \(\operatorname{chase}_k(\mathcal K)\). The proof retains only chase applications needed to produce its facts, chooses a parent provenance for each retained fact, and works backward from stage \(k\) to the ABox. At each reverse step:

- a chase-produced leaf is replaced in the query by the left side of the PI that generated it, which is exactly a PerfectRef step-(a) rewrite; and
- if two query atoms now correspond to one predecessor fact, PerfectRef step (b) unifies them, restoring equality between the number of query atoms and the number of retained predecessor facts.

At stage \(0\), the resulting query in \(PR\) has a match entirely in \(\mathcal A\), hence in \(db(\mathcal A)\). The source writes the \(\mathsf{cr2}\) case in detail, covers the inverse-role \(\mathsf{cr2}\) case in footnote 8, and says the \(\mathsf{cr1},\mathsf{cr3},\mathsf{cr4},\mathsf{cr5}\) cases are analogous. Thus Lemma 39 has a local proof, but not every constructor case is expanded.

### Printed slips inside the proof

These do not alter the intended induction, but should not be copied literally:

1. On p. 419 the proof at one point types a witness set as \(G\subseteq\operatorname{can}(\mathcal K)\). Its elements are membership assertions, so the typed relation is \(G\subseteq\operatorname{chase}(\mathcal K)\).
2. On p. 420, in the reverse-\(\mathsf{cr2}\) step, the new symbol is said to follow the symbols in \(\operatorname{chase}_i(\mathcal K)\). At that induction point the predecessor stage is \(\operatorname{chase}_{k-i}(\mathcal K)\); this is the required index.
3. On p. 421, after the final reduction, the paper writes \(|q_2|=|G_{k-i+1}|\). The induction claim requires, and the one-atom reduction gives, \(|q_2|=|G_{k-i}|\).
4. In the base reduction discussion the prose writes \(q_1=\operatorname{reduce}(q,g_1,g_2)\); Figure 2 actually inserts \(\tau(\operatorname{reduce}(q,g_1,g_2))\). Applying \(\tau\) changes only the notation for body-only, non-shared variables and is required for literal agreement with the algorithm.

## Answer and the exact proof chain

For \(\mathcal A\neq\varnothing\), Figure 3 (p. 418) has the following typed
semantics:

\[
\operatorname{Answer}(Q,\langle\mathcal T,\mathcal A\rangle)=
\begin{cases}
\operatorname{AllTup}(Q,\mathcal K),&\operatorname{Consistent}(\mathcal K)=\mathsf{false},\\
\left(\displaystyle\bigcup_{q_i\in Q}\operatorname{PerfectRef}(q_i,\mathcal T)\right)^{db(\mathcal A)},&\text{otherwise}.
\end{cases}
\]

- Lemma 16 proves termination and correctness of Consistent.
- Lemma 34 proves termination of PerfectRef.
- Theorem 37 therefore proves termination of Answer for \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\).
- Lemma 39 handles each CQ when \(\mathcal K\) is satisfiable.
- Theorem 31 combines the CQ answer sets into the UCQ answer set.
- The definition of certain answers for inconsistent \(\mathcal K\) validates the first branch.
- Theorem 40 prints exact correctness of Answer for every \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) KB; because Figure 3 evaluates (db(\mathcal A)), the displayed procedure is type-correct in the nonempty-ABox regime, with the empty-ABox case handled separately as above.

## Required named results: exact strength and proof status

### Lemma 34 (p. 416)

- **Hypotheses:** \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) TBox \(\mathcal T\); CQ \(q\) over \(\mathcal T\).
- **Conclusion:** PerfectRef terminates.
- **Status:** local proof by finiteness of the reachable-query state space. The printed numeric bound is a coarse query-size coding bound; the explicit finite head/body bound above removes any dependence on an unstated coding convention and preserves the lemma.

### Lemma 39 (pp. 419-421)

- **Hypotheses:** \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) TBox \(\mathcal T\); CQ \(q\) over \(\mathcal T\); \(PR\) returned by PerfectRef; nonempty ABox \(\mathcal A\); satisfiable \(\langle\mathcal T,\mathcal A\rangle\). The source omits “nonempty” here although the conclusion uses its nonempty-ABox database.
- **Conclusion:** \(\operatorname{ans}(q,\langle\mathcal T,\mathcal A\rangle)=PR^{db(\mathcal A)}\).
- **Status:** local two-direction proof through finite chase witnesses. Representative PI/chase cases are written; remaining cases are declared analogous. The four printed slips listed above require the displayed corrections.

### Theorem 41 (p. 421)

- **Hypotheses/parameterization:** Definition 3's regime: a fixed \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) TBox \(\mathcal T\), a fixed UCQ \(Q\), arbitrary nonempty ABoxes \(\mathcal A\), and answer tuples drawn from the constants of \(\mathcal A\).
- **Conclusion:** UCQ answering in \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) is FOL-reducible in the exact sense of Definition 3, including arbitrary satisfiable or unsatisfiable KBs and nonempty ABoxes.
- **Proof chain:** Theorem 40 gives a finite UCQ over \(db(\mathcal A)\). For satisfiable KBs, this is immediate. For arbitrary KBs, the prose says to add finitely many conjunctive cases that return every active-domain tuple when the consistency-violation query is true.
- **Status:** theorem stated locally; the satisfiable case is established locally. The explicit inconsistent-case FO formula is not printed. The paper refers to reference [10] for an analogous database-constraint construction.
- **Exact local completion:** let \(q_{\mathrm{unsat}}\) be the Boolean FO disjunction used by Consistent, true exactly when some assertion in \(cl_n(\mathcal T)\) is violated. If the answer arity is \(r>0\), disjoin the PerfectRef UCQ with
  \[
  q_{\mathrm{unsat}}\wedge\bigwedge_{i=1}^{r}(x_i=x_i);
  \]
  for a Boolean query, use \(q_{\mathrm{unsat}}\) itself. The domain of \(db(\mathcal A)\) is exactly the constants occurring in the nonempty ABox, so this added disjunct returns every domain tuple precisely when \(\mathcal K\) is inconsistent, without naming predicates outside the fixed TBox/query alphabet. Otherwise it returns none, leaving only the PerfectRef answer. This reconstruction uses only the paper's own \(db(\mathcal A)\), equality-bearing FOL query language, consistency query, and Definition 3, but is not printed verbatim.

### Lemma 42 (pp. 421-422)

- **Hypotheses:** \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) TBox \(\mathcal T\); fixed CQ \(q\) over \(\mathcal T\).
- **Conclusion:** PerfectRef runs in time polynomial in \(|\mathcal T|\).
- **Proof:** with \(n=|q|\) fixed and \(m\) linearly bounded by \(|\mathcal T|\), the finite query-state bound is polynomial in \(m\). Each applicability/unification pass is also polynomial. The corrected count supplied under Lemma 34 preserves the same parameterized conclusion.
- **Not claimed:** polynomial time when \(q\) is part of the varying input.

### Theorem 43 (p. 422)

- **Hypotheses/parameterization:** \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) KBs and UCQs; for the one-parameter TBox-size answering claim, the UCQ and ABox are fixed while the TBox varies; for data complexity, the TBox and UCQ are fixed while the ABox varies.
- **Conclusion:** UCQ answering in \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) is polynomial-time in TBox size with the UCQ and ABox fixed, and LOGSPACE in ABox size when the TBox and UCQ are fixed (data complexity). Independently, Lemma 42 shows that PerfectRef itself is polynomial in \(|\mathcal T|\) for fixed UCQ without inspecting the ABox.
- **Proof chain:** Theorem 40 (correctness), Lemma 42 (fixed-UCQ reformulation polynomial in \(|\mathcal T|\) and independent of \(\mathcal A\)), Theorem 26 (consistency complexity), and fixed-UCQ evaluation over a database in LOGSPACE.
- **Strength:** upper bounds only. The source does not say LOGSPACE-complete or PTIME-complete here.

### Theorem 44 (p. 422)

- **Hypotheses/parameterization:** the recognition problem for variable \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) KB \(\mathcal K\), variable UCQ \(Q\), and candidate answer tuple; the proof states the Boolean-query case for the NP upper bound, which is the standard decision form used for the combined bound.
- **Parameter:** combined size \(|\mathcal K|+|Q|\).
- **Conclusion:** UCQ answering in \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) is NP-complete.
- **Upper-bound proof status:** local proof sketch. A nondeterministic variant follows one PerfectRef derivation and returns one rewritten CQ; the source asserts that one such query is reachable after polynomially many rewrite/reduction steps, yielding nondeterministic polynomial time for Boolean recognition.
- **Lower-bound proof status:** local one-line reduction boundary: ordinary CQ evaluation over relational databases is already NP-hard; take an empty TBox.

### Theorem 46 (p. 423)

- **Hypotheses/parameterization:** Definition 3's regime for \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\): fixed TBox and UCQ, arbitrary nonempty ABoxes, and answer tuples drawn from their constants.
- **Conclusion:** UCQ answering in \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) is FOL-reducible.
- **Proof chain:** Theorem 45 removes the functionality assertions to form \(\mathcal K_I=\langle\mathcal T_I,\mathcal A\rangle\). Functionality does not participate in the chase, so \(\operatorname{can}(\mathcal K)=\operatorname{can}(\mathcal K_I)\); for satisfiable \(\mathcal K\), Theorem 29 and Lemma 39 transfer CQ answers, and Theorem 31 transfers UCQs. Inconsistent KBs use the Answer consistency branch.
- **Status:** no separate proof follows the theorem statement; the paper calls it an immediate consequence of Theorem 45 and analogous to Theorem 41. It therefore inherits Theorem 41's referred, rather than printed, inconsistent-case FO encoding.

### Theorem 47 (p. 424)

- **Hypotheses/parameterization:** \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) KBs and UCQs; fixed UCQ and ABox for the TBox-size answering measure, fixed TBox and UCQ for data complexity, and all recognition inputs variable for combined complexity.
- **Conclusion:** UCQ answering in \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) is polynomial-time in TBox size with the UCQ and ABox fixed, LOGSPACE in ABox size when both the TBox and UCQ are fixed (data complexity), and NP-complete in combined complexity.
- **Status:** stated without a proof body. The preceding sentence says the §5 bounds carry over. The transfer relies on Theorem 45 plus the \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) consistency treatment of functionality; it is not a new independent derivation.

### Theorem 48 (pp. 424-425)

- **Hypotheses/parameterization:** the data-complexity recognition problem, so the relevant extended-language TBox and CQ are fixed while the ABox varies.
- **Base language:** \(\mathrm{DL\mbox{-}Lite}_{core}\).
- **Problem and parameter:** CQ answering; ABox/data complexity.
- **Conclusion:** coNP-hardness results if **any one** of the following extensions is admitted:
  1. \(\forall R.A\) or \(\neg A\) on the left of an inclusion;
  2. \(\forall R.A\) or \(\neg A\) as a query atom;
  3. concept union on the right of an inclusion.
- **Status:** no local proof. The preceding paragraph says the argument used for the coNP-hardness of \(\mathcal{ALE}\), \(\mathcal{FLE}^{-}\), and \(\mathcal{ALU}\) in reference [19] immediately implies the theorem. The exact theorem strength is only coNP-hard, not complete, and only in data complexity.

## FOL-reducibility is not the LOGSPACE theorem

The following implications are the article's actual chain:

1. For fixed \(\mathcal T,Q\), PerfectRef produces a finite FO/UCQ rewriting independent of \(\mathcal A\).
2. The consistency test is likewise a fixed Boolean FO query over \(db(\mathcal A)\).
3. Therefore Definition 3's FOL-reducibility property holds (Theorems 41 and 46).
4. Evaluating a fixed FO formula over a varying finite structure is in LOGSPACE according to the source's cited database-complexity result.
5. Hence the paper obtains a LOGSPACE **data upper bound** (Theorems 43 and 47).

The definability claim in steps 1-3 and the machine-complexity bound in steps 4-5 are different statements. FOL-reducibility also supplies the architectural separation between TBox compilation and database evaluation. The 2007 article does not claim that materializing all PerfectRef rewrites is LOGSPACE in combined input, nor could Theorem 44 permit that conclusion unless NP collapsed to LOGSPACE.

## Why this paper is not “OWL QL”

The string “OWL QL” does not occur in the 2007 paper. On p. 391 it instead says:

- \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) is a strict subset of then-current OWL, in fact OWL Lite; and
- \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) can be viewed as extending the DL-like portion of RDFS.

OWL 2 QL was standardized later. The W3C 2012 Recommendation, §3, says that OWL 2 QL is **based on** the DL-Lite family and that \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) supplies its logical underpinning. “Based on” and “logical underpinning” are not identity assertions. Exact nonidentity is visible in the canonical definitions:

1. The 2007 article formally enforces UNA on individual constants (p. 390). The W3C profile explicitly avoids requiring UNA and explains why it based OWL 2 QL on the non-UNA use of \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) (§3).
2. OWL 2 QL is a profile of OWL 2 structural syntax. It has named individuals, object and data properties, datatypes, and a specified collection of OWL axiom forms and global restrictions. The 2007 \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) grammar has only the concept/role categories, inclusions, and atomic ABox assertions displayed above.
3. The W3C profile supports such OWL forms as property domain/range, equivalence, disjoint properties, reflexive/irreflexive/asymmetric/symmetric properties, data-property forms, and \(\mathsf{DifferentIndividuals}\), subject to its profile grammar. Their relationship to DL-Lite is mediated by the OWL semantics and translations; they are not literally productions in the 2007 grammar.
4. OWL 2 QL disallows functional and inverse-functional property axioms, keys, \(\mathsf{SameIndividual}\), and several other constructs. The 2007 paper separately studies \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) with functionality and \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) with role inclusions; it never defines their union as OWL QL.
5. The W3C Recommendation gives its own four-way complexity table and states AC\(^0\) data complexity for OWL 2 QL CQ answering. The 2007 paper states the weaker LOGSPACE data upper bound for its named DL-Lite variants and formally defines only data and combined complexity.

A faithful handbook may say that \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\) later supplied the logical underpinning for OWL 2 QL, with the W3C source cited. It must not rename the 2007 logic “OWL QL,” identify PerfectRef as the normative OWL 2 QL specification, or transfer the paper's UNA without qualification.

## Source-critical cautions and exact corrections

The following are all visible in the primary paper and matter to a proof-accurate presentation:

1. **Section-order typo (p. 388):** the introduction says §§5 and 6 treat \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\) and \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\), respectively. The actual headings and contents are §5 \(\mathrm{DL\mbox{-}Lite}_{\mathcal R}\), §6 \(\mathrm{DL\mbox{-}Lite}_{\mathcal F}\).
2. **Partial chase recursion (p. 397):** add \(S_{j+1}=S_j\) when no PI is applicable.
3. **Totality of Lemma 28's map (p. 411):** map unused members of \(\Gamma_N\) arbitrarily into the nonempty target domain.
4. **Wrong dependency number (p. 413):** Theorem 31 needs Theorem 29, not Theorem 28, at the canonical-evaluation step.
5. **Lemma 34 count convention (p. 416):** the printed \((m(n+1)^2)^n\) uses a query-size parameter specified only up to proportionality and does not give a literal head/body encoding. Quote it as the paper's coarse bound; for a convention-independent enumeration, use the explicit finite bound displayed in this note. Termination and fixed-query polynomiality remain valid.
6. **Lemma 39 witness type (p. 419):** write \(G\subseteq\operatorname{chase}(\mathcal K)\), not \(G\subseteq\operatorname{can}(\mathcal K)\).
7. **Lemma 39 predecessor index (p. 420):** in the reverse step use \(\operatorname{chase}_{k-i}(\mathcal K)\), not \(\operatorname{chase}_i(\mathcal K)\).
8. **Lemma 39 cardinality index (p. 421):** after reduction use \(|q_2|=|G_{k-i}|\), not \(|G_{k-i+1}|\).
9. **Lemma 39 algorithm literalness (p. 420):** retain \(\tau\circ\operatorname{reduce}\) when quoting PerfectRef, even where the proof abbreviates it to reduce.
10. **Theorem 41 proof status (p. 421):** the inconsistent-KB FO encoding is described and referred to [10], not printed in full; distinguish that referral from the local reconstruction above.
11. **Theorems 46-48 proof status (pp. 423-425):** 46 is an immediate corollary, 47 is stated by transfer with no proof body, and 48 is imported from the argument in [19]. None should be presented as having a new full local proof in this article.
12. **Equality preprocessing under UNA (pp. 390, 392-393):** identifying query terms has a failure case when one equivalence class contains two distinct constants; remove that unsatisfiable CQ disjunct rather than identifying the constants.
13. **Nonempty active-domain boundary (pp. 394-395):** (db(\mathcal A)) is defined only for nonempty \(\mathcal A\). Preserve that hypothesis in Lemmas 8, 12, 14, and 39 and in Figure 3/Theorem 40 whenever their presentation evaluates (db(\mathcal A)); treat an empty ABox separately.
14. **Theorem 29 answer type (p. 412):** restrict the canonical query extension to tuples denoted by constants occurring in the KB. The unrestricted extension can contain fresh chase witnesses and is not equal to the source's certain-answer set.

With those explicit corrections and attribution boundaries, the construction, PerfectRef trace, satisfiable-KB correctness argument, parameterized complexity conclusions, and DL-Lite/OWL 2 QL distinction can be presented at their exact source-supported strength.
