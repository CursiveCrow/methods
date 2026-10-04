# N-c-010.a primary-source note: Baader, Brandt, and Lutz (2005), *Pushing the EL Envelope*

## Scope and evidentiary standing

This note is restricted to the 2005 IJCAI paper by Franz Baader, Sebastian Brandt, and Carsten Lutz and its expressly cited, author-institution technical report. The IJCAI paper is the controlling source for theorem numbering in the handbook presentation; the technical report supplies proofs and normalization details that the conference paper explicitly sends the reader to. A later W3C Recommendation is used only to prevent an anachronistic identification of the paper's \(\mathcal{EL}^{++}\) with the later standardized profile OWL 2 EL. [IJCAI §1, printed pp.364–365; IJCAI reference “Baader et al., 2005,” printed p.369; TR title page and §§1–7, printed pp.1–29; W3C, *OWL 2 Web Ontology Language Profiles (Second Edition)*, §§1–2.]

No handbook prose, bibliography entry, ledger, checker, test, or build artifact was inspected or changed for this note. The worked saturation in §8 below is newly constructed for this note and is explicitly separated from examples printed by the sources.

## 1. Exact source record, access, hashes, pagination, and rights

### 1.1 Controlling conference paper

- Franz Baader, Sebastian Brandt, and Carsten Lutz, “Pushing the \(\mathcal{EL}\) Envelope,” in *Proceedings of the Nineteenth International Joint Conference on Artificial Intelligence (IJCAI-05)*, 2005, printed pp.364–369. The official proceedings index gives the title, author order, and starting page 364; the next paper starts at page 370, and the official paper PDF contains six pages numbered 364–369. [Official IJCAI proceedings index, “KNOWLEDGE REPRESENTATION AND REASONING,” paper entry; IJCAI physical pp.1–6 / printed pp.364–369.]
- Official PDF: <https://www.ijcai.org/Proceedings/05/Papers/0372.pdf> (retrieved 2026-08-22). [Official IJCAI proceedings index and PDF.]
- Local scholarship copy: `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-2005.pdf`.
- SHA-256: `4C9CAA8C224506123B7EE06CFCC8F5759D3537F4C241BB7E6BDDCB89E0727A5A`.
- File facts: 170,023 bytes; six pages; unencrypted; US Letter; PDF 1.2; creator `TeX`; producer `pdfTeX-0.13d`; embedded creation date 2005-04-08. These are file-level observations from the acquired official PDF, not claims printed in the article.
- No DOI is printed in the paper or supplied by the inspected official IJCAI proceedings record. The stable identifier used here is the official proceedings URL. [IJCAI physical pp.1–6; official IJCAI proceedings index.]

Physical-to-printed page map and completed visual inspection:

| PDF physical page | Printed page | Visually checked contents |
|---:|---:|---|
| 1 | 364 | title, authors, abstract, §1 introduction, applications, tractability aim, role-value-map footnote |
| 2 | 365 | Table 1, §2 syntax and semantics, CBoxes, expressivity remarks, beginning of §3 and normal forms, Lemma 1 |
| 3 | 366 | Table 2 CR1–CR11, saturation state, reachability abbreviation, concrete conjunctions, p-admissibility, Lemmas 2–3 |
| 4 | 367 | Lemma 3 proof sketch, Theorem 4, \(\mathbb Q\) and \(\mathbb S\), Proposition 5, non-convex examples, Table 3 |
| 5 | 368 | Theorems 6–9, reductions for disjunction and \((\geq 2r)\), adjacent role-constructor result, beginning of inverse-role reduction |
| 6 | 369 | Theorem 10 and its open-bound sentence, Theorems 11–12, conclusion, references |

All six rendered pages were inspected rather than relying on text extraction alone. This matters for the mathematical notation in Tables 1–3 and for the printed defects recorded in §13.

The official proceedings page says “All rights reserved” and requires permission for reproduction of the publication or its parts. The accessible PDF is therefore evidence for reading and citation, not evidence of an open republication license. This note paraphrases the prose and records the indispensable formal clauses for scholarship; it does not purport to grant reuse rights. [Official IJCAI proceedings index, copyright notice immediately below “IJCAI-05 proceedings.”]

### 1.2 Expressly accompanying technical report

- Franz Baader, Sebastian Brandt, and Carsten Lutz, *Pushing the \(\mathcal{EL}\) Envelope*, LTCS-Report LTCS-05-01, Chair for Automata Theory, Institute for Theoretical Computer Science, Dresden University of Technology, 2005. [Official TU Dresden/ICCL publication record; TR cover and title page.]
- Official publication record: <https://iccl.inf.tu-dresden.de/web/LATPub682/en>. It identifies the authors, title, institution, report number LTCS-05-01, type, and year, and classifies the record among publications without DOI. [Official TU Dresden/ICCL record, bibliographic block and category list.]
- Official PDF: <https://lat.inf.tu-dresden.de/research/reports/2005/BaaderBrandtLutz-LTCS-05-01.pdf> (retrieved 2026-08-22).
- Local scholarship copy: `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-ltcs-05-01.pdf`.
- SHA-256: `374D73EB848E556DA759D89231385353996F44E6A6131F53D2794BB68D5AA3BA`.
- File facts: 396,587 bytes; 33 physical pages; unencrypted; A4; PDF 1.4. The current wrapper reports GPL Ghostscript 9.06 and 2019 wrapper dates, whereas the cover, official record, and bibliographic identity date the report content to 2005. These are file-level observations plus the official record, respectively.
- Page map: physical page 1 is an unnumbered report cover; physical pages 2–33 are printed report pages 1–32. Thus, for example, physical page 7 is printed p.6 (Figure 1), physical page 8 is printed p.7 (Table 2), and physical pages 12–15 are printed pp.11–14 (the completeness/model proof). [TR physical pp.1–33.]

The conference paper expressly says that proofs and further technical details are in this accompanying report and cites LTCS-05-01 in its references. Accessibility from the official institutional record does not itself state an open reuse license; the same reading-and-citation boundary is used here. [IJCAI §1, printed p.365; IJCAI references, printed p.369; official TU Dresden/ICCL publication record.]

### 1.3 Later standard used only for a nonidentity boundary

- W3C, *OWL 2 Web Ontology Language Profiles (Second Edition)*, W3C Recommendation, 11 December 2012: <https://www.w3.org/TR/owl2-profiles/>. The document defines OWL 2 EL as a profile of OWL 2 by its own functional-style grammar and global restrictions and cites the \(\mathcal{EL}^{++}\) work as a basis; it does not say that the 2005 paper's language and the standardized profile are literally identical. [W3C Recommendation, abstract, §§1–2.2 and Appendix 6.1.]

## 2. Source notation and exact standing of the language

The paper begins with sets \(N_C\) of concept names, \(N_R\) of role names, optionally \(N_I\) of individual names, and \(N_F\) of feature names. Here concept names denote unary predicates on individuals, role names denote binary relations on individuals, individual names denote individuals, and features denote partial functions from individuals to concrete values. These are source categories, not new terminology introduced by this note. [IJCAI §2, printed p.365; TR §2, printed pp.2–3.]

For concrete domains, the paper defines
\[
  \mathcal D=(\Delta^{\mathcal D},P^{\mathcal D}),
\]
where each \(p\in P^{\mathcal D}\) has an arity \(k>0\) and an extension \(p^{\mathcal D}\subseteq(\Delta^{\mathcal D})^k\). If the logic is equipped with \(\mathcal D_1,\ldots,\mathcal D_n\), their carriers must be pairwise disjoint:
\[
  \Delta^{\mathcal D_i}\cap\Delta^{\mathcal D_j}=\varnothing
  \quad(1\leq i<j\leq n).
\]
The resulting notation is \(\mathcal{EL}^{++}(\mathcal D_1,\ldots,\mathcal D_n)\). [IJCAI §2, before and after Table 1, printed p.365; TR §2, printed pp.2–3.]

The concept grammar implicit in the source prose and Table 1 is
\[
  C,D ::= A\mid \top\mid\bot\mid\{a\}\mid C\sqcap D
       \mid \exists r.C\mid p(f_1,\ldots,f_k),
\]
where \(A\in N_C\), \(a\in N_I\), \(r\in N_R\), each \(f_i\in N_F\), and \(p\in P^{\mathcal D_j}\) has arity \(k\). The source calls the last form the concrete-domain constructor. [IJCAI §2 and Table 1, printed p.365; TR §2 and Table 1, printed pp.2–3.]

An interpretation \(\mathcal I=(\Delta^{\mathcal I},\cdot^{\mathcal I})\) has a nonempty individual domain and assigns
\[
  A^{\mathcal I}\subseteq\Delta^{\mathcal I},\qquad
  r^{\mathcal I}\subseteq\Delta^{\mathcal I}\times\Delta^{\mathcal I},\qquad
  a^{\mathcal I}\in\Delta^{\mathcal I},
\]
and a partial function
\[
  f^{\mathcal I}:\Delta^{\mathcal I}\rightharpoonup
  \bigcup_{i=1}^{n}\Delta^{\mathcal D_i}.
\]
[IJCAI §2, printed p.365; TR §2, printed p.3.]

The full Table 1 interpretation clauses are:

| Source form | Interpretation |
|---|---|
| \(\top\) | \(\Delta^{\mathcal I}\) |
| \(\bot\) | \(\varnothing\) |
| \(\{a\}\) | \(\{a^{\mathcal I}\}\) |
| \(C\sqcap D\) | \(C^{\mathcal I}\cap D^{\mathcal I}\) |
| \(\exists r.C\) | \(\{x\in\Delta^{\mathcal I}\mid \exists y\in\Delta^{\mathcal I}: (x,y)\in r^{\mathcal I}\land y\in C^{\mathcal I}\}\) |
| \(p(f_1,\ldots,f_k)\), \(p\in P^{\mathcal D_j}\) | \(\{x\in\Delta^{\mathcal I}\mid \exists y_1,\ldots,y_k\in\Delta^{\mathcal D_j}: f_i^{\mathcal I}(x)=y_i\ (1\leq i\leq k)\land(y_1,\ldots,y_k)\in p^{\mathcal D_j}\}\) |

Thus a concrete atom is false at \(x\) if one of its required feature values is undefined; this follows directly from the existential equality clause rather than from a separately printed default-value convention. [IJCAI Table 1 and §2, printed p.365; TR Table 1 and §2, printed pp.2–3.]

## 3. CBoxes, TBoxes, ABoxes, and role-inclusion scope

An \(\mathcal{EL}^{++}\) **constraint box**, abbreviated by the source as a CBox, is a finite set of two axiom types:

1. a general concept inclusion (GCI) \(C\sqsubseteq D\), satisfied exactly if \(C^{\mathcal I}\subseteq D^{\mathcal I}\);
2. a role inclusion (RI) \(r_1\circ\cdots\circ r_k\sqsubseteq r\), satisfied exactly if \(r_1^{\mathcal I}\circ\cdots\circ r_k^{\mathcal I}\subseteq r^{\mathcal I}\).

The paper says that a finite set of GCIs alone is commonly called a general TBox and that it uses “CBox” because RIs are also present. [IJCAI §2 and Table 1, printed p.365; TR §2 and Table 1, printed p.3.]

For a CBox \(\mathcal C\), subsumption is
\[
  C\sqsubseteq_{\mathcal C}D
  \quad\Longleftrightarrow\quad
  C^{\mathcal I}\subseteq D^{\mathcal I}
  \text{ for every model }\mathcal I\text{ of }\mathcal C.
\]
This is the main inference problem in the conference paper. [IJCAI §2, printed p.365.]

The admitted RI has a role chain only on the left and a single role name on the right. It covers a role hierarchy \(r\sqsubseteq s\), transitivity \(r\circ r\sqsubseteq r\), and the right-identity form \(r\circ s\sqsubseteq s\). This is the paper's “restricted form of role-value maps.” It must not be enlarged silently to arbitrary role-value maps with a chain on the right: the paper's introductory footnote says arbitrary role-value maps cause undecidability, and the report states this as its Theorem 12 even without concept inclusions in the CBox. [IJCAI §1 n.1, printed p.364; IJCAI §2, printed p.365; TR §5, Theorem 12, printed pp.20–21.]

The source also records two derived uses:

- \(C\sqcap D\sqsubseteq\bot\) expresses disjointness of \(C\) and \(D\). [IJCAI §2, printed p.365; TR §2, printed p.4.]
- A unique-name condition for selected \(a\neq b\) can be enforced by \(\{a\}\sqcap\{b\}\sqsubseteq\bot\); there is no global unique-name assumption built into the semantics. [IJCAI §2, printed p.365; TR §2, printed p.4.]

The technical report, but not conference Table 1, additionally defines an ABox as a finite set of assertions \(C(a)\) and \(r(a,b)\), interpreted by \(a^{\mathcal I}\in C^{\mathcal I}\) and \((a^{\mathcal I},b^{\mathcal I})\in r^{\mathcal I}\). It gives explicit polynomial reductions among concept satisfiability, subsumption, ABox consistency, and the instance problem. The conference paper merely says these reductions exist and cites the report. These ABox notions are reasoning-task context; they are not part of the completion state in Table 2. [IJCAI §2, printed p.365; TR §2 and Table 1, printed pp.3–4.]

## 4. Normal form and the exact normalization record

For a CBox \(\mathcal C\), \(\mathrm{BC}_{\mathcal C}\) is the smallest set containing \(\top\), every concept name used in \(\mathcal C\), and every nominal \(\{a\}\) or concrete atom \(p(f_1,\ldots,f_k)\) appearing in \(\mathcal C\). The report phrases the last item as all “(sub)concepts” of those forms. [IJCAI §3, printed p.365; TR §3.1, printed p.5.]

A CBox is in normal form exactly when every GCI is one of
\[
\begin{array}{ll}
  C_1\sqsubseteq D, & C_1\sqcap C_2\sqsubseteq D,\\
  C_1\sqsubseteq\exists r.C_2, & \exists r.C_1\sqsubseteq D,
\end{array}
\]
where \(C_1,C_2\in\mathrm{BC}_{\mathcal C}\) and \(D\in\mathrm{BC}_{\mathcal C}\cup\{\bot\}\), and every RI is one of
\[
  r\sqsubseteq s,\qquad r_1\circ r_2\sqsubseteq s.
\]
[IJCAI §3, printed p.365; TR Definition 1, §3.1, printed p.5.]

Fresh concept and role names yield a conservative extension \(\mathcal C'\): every model of \(\mathcal C'\) is a model of \(\mathcal C\), and every model of \(\mathcal C\) can be expanded by interpretations of the fresh names to a model of \(\mathcal C'\). Conference Lemma 1 states that subsumption w.r.t. arbitrary CBoxes reduces in linear time to subsumption w.r.t. normalized CBoxes. [IJCAI §3, Lemma 1, printed p.365; TR Definition 1 and Lemma 2, printed p.5.]

The conference paper does not print the normalization rules. The report's Figure 1 gives the following exact replacement schemata; \(u\) is a fresh role name, \(A\) is a fresh concept name, and its caption says \(\widehat C,\widehat D\notin\mathrm{BC}_{\mathcal C}\). [TR §3.1, Figure 1, printed p.6.]

| Rule | Replace | By |
|---|---|---|
| NF1 | \(r_1\circ\cdots\circ r_k\sqsubseteq s\) | \(\{r_1\circ\cdots\circ r_{k-1}\sqsubseteq u,\ u\circ r_k\sqsubseteq s\}\) |
| NF2 | \(C\sqcap\widehat D\sqsubseteq E\) | \(\{\widehat D\sqsubseteq A,\ C\sqcap A\sqsubseteq E\}\) |
| NF3 | \(\exists r.\widehat C\sqsubseteq D\) | \(\{\widehat C\sqsubseteq A,\ \exists r.A\sqsubseteq D\}\) |
| NF4 | \(\bot\sqsubseteq D\) | \(\varnothing\) |
| NF5 | \(\widehat C\sqsubseteq\widehat D\) | \(\{\widehat C\sqsubseteq A,\ A\sqsubseteq\widehat D\}\) |
| NF6 | \(B\sqsubseteq\exists r.\widehat C\) | \(\{B\sqsubseteq\exists r.A,\ A\sqsubseteq\widehat C\}\) |
| NF7 | \(B\sqsubseteq C\sqcap D\) | \(\{B\sqsubseteq C,\ B\sqsubseteq D\}\) |

The report requires two phases: exhaust NF1–NF4 first, applying NF2 modulo commutativity of conjunction, and only then exhaust NF5–NF7. It states at most \(|\mathcal C|\) rule applications and a linear-size result. The two-phase order is essential to the stated linear-size bound: applying all rules in one phase can cause a quadratic blow-up because NF7 duplicates \(B\). [TR §3.1, proof of Lemma 2 and paragraph after Figure 1, printed pp.5–6.]

For an arbitrary query \(C\sqsubseteq_{\mathcal C}D\), both sources reduce to fresh concept names \(A,B\) by
\[
  C\sqsubseteq_{\mathcal C}D
  \quad\Longleftrightarrow\quad
  A\sqsubseteq_{\mathcal C'}B,
  \qquad
  \mathcal C'=\mathcal C\cup\{A\sqsubseteq C,\ D\sqsubseteq B\}.
\]
The reverse implication is obtained by expanding any countermodel with \(A^{\mathcal I}=C^{\mathcal I}\) and \(B^{\mathcal I}=D^{\mathcal I}\); the sources state the equivalence and freshness, while this last sentence makes its immediate model-theoretic justification explicit. [IJCAI §3, printed p.366; TR §3.2, printed p.6.]

## 5. Completion state, abbreviations, and p-admissibility

Let \(R_{\mathcal C}\) be the set of role names used in a normalized CBox \(\mathcal C\). The algorithm computes
\[
  S:\mathrm{BC}_{\mathcal C}\longrightarrow
    \mathcal P(\mathrm{BC}_{\mathcal C}\cup\{\top,\bot\}),
  \qquad
  R:R_{\mathcal C}\longrightarrow
    \mathcal P(\mathrm{BC}_{\mathcal C}\times\mathrm{BC}_{\mathcal C}).
\]
Its intended invariants are
\[
\begin{aligned}
  \text{(I1)}\quad&D\in S(C)\Longrightarrow C\sqsubseteq_{\mathcal C}D,\\
  \text{(I2)}\quad&(C,D)\in R(r)\Longrightarrow C\sqsubseteq_{\mathcal C}\exists r.D.
\end{aligned}
\]
Initialization is \(S(C)=\{C,\top\}\) for every \(C\in\mathrm{BC}_{\mathcal C}\) and \(R(r)=\varnothing\) for every \(r\in R_{\mathcal C}\). [IJCAI §3, printed p.366; TR §3.2, printed pp.6–7.]

The reachability-like relation printed as \(C\rightsquigarrow D\) is defined from the current \(R\), not introduced as an additional model relation. It holds iff there are \(C_1,\ldots,C_k\in\mathrm{BC}_{\mathcal C}\) such that:

1. \(C_1=C\) or \(C_1=\{b\}\) for some individual name \(b\);
2. for every \(1\leq j<k\), \((C_j,C_{j+1})\in R(r_j)\) for some \(r_j\in R_{\mathcal C}\);
3. \(C_k=D\).

The option to begin at a nominal is part of the printed definition and must not be dropped from CR6. [IJCAI §3 immediately after Table 2, printed p.366; TR §3.2 immediately after Table 2, printed p.7.]

For \(\Gamma\) a set of \(\mathcal{EL}^{++}(\mathcal D_1,\ldots,\mathcal D_n)\)-concept descriptions, the source defines
\[
  \operatorname{con}_j(\Gamma)
  :=\bigwedge_{\substack{p(f_1,\ldots,f_k)\in\Gamma\\p\in P^{\mathcal D_j}}}
     p(f_1,\ldots,f_k).
\]
Each feature name is treated as a first-order variable when satisfiability and implication of these concrete conjunctions are tested in \(\mathcal D_j\). [IJCAI §3 after Table 2, printed p.366; TR §3.2, printed p.8.]

A concrete domain \(\mathcal D\) is **p-admissible** exactly if:

1. satisfiability and implication in \(\mathcal D\) are decidable in polynomial time; and
2. \(\mathcal D\) is convex: whenever a conjunction of atoms \(p(f_1,\ldots,f_k)\) implies a disjunction of atoms of the same form, it implies at least one disjunct.

Both conditions are required. Polynomial satisfiability/implication makes CR7–CR8 executable in polynomial time; convexity is used in the completeness construction to choose one concrete assignment that avoids all absent basic concrete atoms at once. [IJCAI §3, definition immediately before Lemma 2, printed p.366; TR Definition 3, printed p.8, and Lemma 7 Claim 2, printed p.12.]

## 6. Every Table 2 completion rule

The following is a notation-faithful transcription of the rule conditions and their type-correct actions. Every variable \(C,C',C_1,C_2,D,D',E\) in these rules ranges over the basic descriptions required by the displayed membership or normal-form premise, and every role ranges over \(R_{\mathcal C}\). The source presents each as a monotone set/relation addition. [IJCAI §3, Table 2, printed p.366; TR §3.2, Table 2, printed p.7.]

| Rule | Exact trigger | Action |
|---|---|---|
| CR1 | \(C'\in S(C)\), \(C'\sqsubseteq D\in\mathcal C\), \(D\notin S(C)\) | \(S(C):=S(C)\cup\{D\}\) |
| CR2 | \(C_1,C_2\in S(C)\), \(C_1\sqcap C_2\sqsubseteq D\in\mathcal C\), \(D\notin S(C)\) | \(S(C):=S(C)\cup\{D\}\) |
| CR3 | \(C'\in S(C)\), \(C'\sqsubseteq\exists r.D\in\mathcal C\), \((C,D)\notin R(r)\) | \(R(r):=R(r)\cup\{(C,D)\}\) |
| CR4 | \((C,D)\in R(r)\), \(D'\in S(D)\), \(\exists r.D'\sqsubseteq E\in\mathcal C\), \(E\notin S(C)\) | \(S(C):=S(C)\cup\{E\}\) |
| CR5 | \((C,D)\in R(r)\), \(\bot\in S(D)\), \(\bot\notin S(C)\) | \(S(C):=S(C)\cup\{\bot\}\) |
| CR6 | \(\{a\}\in S(C)\cap S(D)\), \(C\rightsquigarrow D\), \(S(D)\nsubseteq S(C)\) | \(S(C):=S(C)\cup S(D)\) |
| CR7 | \(\operatorname{con}_j(S(C))\) is unsatisfiable in \(\mathcal D_j\), \(\bot\notin S(C)\) | \(S(C):=S(C)\cup\{\bot\}\) |
| CR8 | \(\operatorname{con}_j(S(C))\) implies in \(\mathcal D_j\) a concrete atom \(p(f_1,\ldots,f_k)\in\mathrm{BC}_{\mathcal C}\), and that atom is not in \(S(C)\) | add \(p(f_1,\ldots,f_k)\) to \(S(C)\) |
| CR9 | \(p(f_1,\ldots,f_k),p'(f'_1,\ldots,f'_{k'})\in S(C)\), \(p\in P^{\mathcal D_j}\), \(p'\in P^{\mathcal D_\ell}\), \(j\neq\ell\), and \(f_s=f'_t\) for some \(s,t\), with \(\bot\notin S(C)\) | \(S(C):=S(C)\cup\{\bot\}\) |
| CR10 | \((C,D)\in R(r)\), \(r\sqsubseteq s\in\mathcal C\), \((C,D)\notin R(s)\) | \(R(s):=R(s)\cup\{(C,D)\}\) |
| CR11 | \((C,D)\in R(r_1)\), \((D,E)\in R(r_2)\), \(r_1\circ r_2\sqsubseteq r_3\in\mathcal C\), \((C,E)\notin R(r_3)\) | \(R(r_3):=R(r_3)\cup\{(C,E)\}\) |

The type-correct CR11 action in the final column is supported by its trigger, by invariant (I2), and by the CR11 soundness case in the report. Both printed Table 2 versions actually show \(R(r_3):=R_i(r_3)\cup\{(C,E)\}\), although no \(i\) is introduced in the table; this printed defect is preserved and discussed in §13 rather than silently attributed to the source as correct. [IJCAI Table 2, printed p.366; TR Table 2, printed p.7; TR Lemma 6 CR11 case, printed p.11.]

The rules are deterministic forward additions in this precise sense: a satisfied trigger identifies a fixed element or pair to add, and no rule prints alternative conclusions. The source says to apply rules until none applies. It does not present a branching tableau, a nondeterministic choice rule, or a blocking condition. Because no addition is removed, exhaustive fair application computes the same least set of consequences generated by these finite rules; this least-fixed-point wording is an immediate inference from the printed monotone rules, not a phrase used by the article. [IJCAI §3 before/after Table 2, printed p.366; TR §§3.2–3.3, printed pp.6–9.]

The state space is finite. From the printed types, at most \(|\mathrm{BC}_{\mathcal C}|(|\mathrm{BC}_{\mathcal C}|+2)\) membership slots exist across all \(S(C)\), and at most \(|R_{\mathcal C}|\,|\mathrm{BC}_{\mathcal C}|^2\) ordered-pair slots exist across all \(R(r)\); the source itself states only the polynomial conclusion, not these loose explicit counts. Each successful rule adds a previously absent slot, so successful applications are polynomially bounded. Reachability for \(\rightsquigarrow\) is polynomial graph reachability, and concrete tests are polynomial by p-admissibility. [IJCAI proof explanation before Lemma 2, printed p.366; TR Lemma 5, printed p.9.]

## 7. Exact subsumption criterion

After no rule applies, conference Lemma 3 states, for concept names \(A,B\) occurring in the normalized CBox,
\[
  A\sqsubseteq_{\mathcal C}B
  \quad\Longleftrightarrow\quad
  \Bigl(S(A)\cap\{B,\bot\}\neq\varnothing\Bigr)
  \ \lor\ 
  \Bigl(\exists\{a\}\in\mathrm{BC}_{\mathcal C}:\bot\in S(\{a\})\Bigr).
\]
The three semantic cases are: \(B\in S(A)\) gives the requested subsumption; \(\bot\in S(A)\) makes \(A\) empty in every model; and \(\bot\in S(\{a\})\) for a nominal makes the whole CBox model-less because a nominal must denote the nonempty singleton \(\{a^{\mathcal I}\}\). [IJCAI Lemma 3 and following soundness paragraph, printed pp.366–367; TR Lemma 4, Lemma 6 conditions S1–S2, printed pp.8–11.]

This criterion is for concept names after normalization/query reduction. It is not printed as an arbitrary ABox instance-materialization test. [IJCAI Lemmas 1 and 3, printed pp.365–366; TR §§2–3, printed pp.3–14.]

## 8. A small worked saturation constructed from the source rules

This example is **not printed by Baader, Brandt, and Lutz**. It is included only to demonstrate the exact source rules. Let \(A,B,C,D,E,F,G\) be concept names and \(r,s,t,u\) role names, and take the already normalized CBox
\[
\begin{array}{rcl@{\qquad}rcl}
 A&\sqsubseteq&B, & A&\sqsubseteq&\exists r.C,\\
 C&\sqsubseteq&D, & \exists r.D&\sqsubseteq&E,\\
 B\sqcap E&\sqsubseteq&F, & r&\sqsubseteq&s,\\
 C&\sqsubseteq&\exists t.G, & s\circ t&\sqsubseteq&u.
\end{array}
\]
Each axiom has one of the four normalized GCI forms or two normalized RI forms. [Normal-form check against IJCAI §3, printed p.365; TR Definition 1, printed p.5.]

Initialization gives \(S(X)=\{X,\top\}\) for each basic concept name \(X\) and empty role relations. A possible fair sequence is:

1. CR1 adds \(B\) to \(S(A)\) and \(D\) to \(S(C)\).
2. CR3 adds \((A,C)\) to \(R(r)\) from \(A\in S(A)\) and \(A\sqsubseteq\exists r.C\).
3. CR3 adds \((C,G)\) to \(R(t)\) from \(C\in S(C)\) and \(C\sqsubseteq\exists t.G\).
4. CR4 uses \((A,C)\in R(r)\), \(D\in S(C)\), and \(\exists r.D\sqsubseteq E\) to add \(E\) to \(S(A)\).
5. CR2 now sees \(B,E\in S(A)\) and adds \(F\) to \(S(A)\).
6. CR10 uses \((A,C)\in R(r)\) and \(r\sqsubseteq s\) to add \((A,C)\) to \(R(s)\).
7. CR11 uses \((A,C)\in R(s)\), \((C,G)\in R(t)\), and \(s\circ t\sqsubseteq u\) to add \((A,G)\) to \(R(u)\).

Every step is an instance of Table 2 and makes a fixed monotone addition. At saturation, \(F\in S(A)\), so Lemma 3 yields \(A\sqsubseteq_{\mathcal C}F\). The role invariant also records \(A\sqsubseteq_{\mathcal C}\exists u.G\), but the paper's decision criterion for the requested atomic subsumption uses the membership \(F\in S(A)\). [IJCAI Table 2 and Lemma 3, printed p.366; TR Table 2 and Lemma 4, printed pp.7–8.]

## 9. Lemmas 2–3, Theorem 4, and the proof chain

### 9.1 Conference Lemma 2: termination and per-step cost

**Exact strength.** For a normalized CBox \(\mathcal C\), the Table 2 rules can be applied only polynomially many times, and each rule application is polynomial. It is not a linear-time claim. [IJCAI Lemma 2, printed p.366.]

The conference proof is a one-paragraph justification by monotone addition to polynomially bounded \(S\) and \(R\), polynomial graph reachability, and p-admissible concrete tests. The report supplies the formal version as Lemma 5: \(|\mathrm{BC}_{\mathcal C}|\) and \(|R_{\mathcal C}|\) are linear in \(|\mathcal C|\); each successful application adds one new concept membership or role pair; none is removed; and reachability is polynomial. [IJCAI paragraph immediately before Lemma 2, printed p.366; TR Lemma 5, printed p.9.]

### 9.2 Conference Lemma 3: soundness and completeness

**Exact strength.** Lemma 3 is the biconditional criterion in §7 for concept names after termination. [IJCAI Lemma 3, printed p.366.]

For soundness, the conference paper says initialization satisfies (I1)–(I2) and every rule preserves them, but works out only CR6. If \(\{a\}\in S(C)\cap S(D)\), then both \(C\) and \(D\) are subsumed by the same singleton. The condition \(C\rightsquigarrow D\) ensures either a chain from \(C\) to \(D\) or a chain from some nominal \(\{b\}\) to \(D\); in the first case \(D\) is nonempty whenever \(C\) is, and in the second \(D\) is nonempty in every model. Hence copying \(S(D)\) into \(S(C)\) preserves (I1). The paper explicitly warns that dropping \(C\rightsquigarrow D\) breaks (I1). [IJCAI soundness paragraph after Lemma 3, printed p.367; TR §3.2 final paragraph, printed p.8.]

The report proves all rule cases by induction in Lemma 6. CR1–CR2 use the corresponding GCIs; CR3 establishes the existential witness part of (I2); CR4 combines an edge witness with a successor label; CR5 propagates impossibility from an impossible successor; CR6 uses the nominal/path argument; CR7 contradicts concrete unsatisfiability; CR8 uses concrete implication; CR9 contradicts pairwise disjoint concrete carriers for a shared feature; CR10 uses a simple RI; and CR11 composes two witness edges using a binary RI. The final S1/S2 cases yield either ordinary subsumption, emptiness of \(A\), or absence of any model. [TR Lemma 6, printed pp.9–11.]

For completeness, the conference paper only sketches a countermodel and expressly cites the report for its detailed construction and proof. It says, in outline, to retain basic descriptions reachable from \(A\), identify descriptions carrying a common nominal, interpret concept and role names from \(S,R\), and select feature assignments satisfying \(\operatorname{con}_j(S(C))\). [IJCAI completeness sketch after Lemma 3, printed p.367.]

### 9.3 Report Lemma 7: full countermodel/model extraction

The report proves the contrapositive. Assume neither S1 nor S2 holds for \(A_0,B_0\). Write the final mappings as \(S,R\), and define
\[
  \mathrm{BC}_{\mathcal C}^{-}
  :=\{C\in\mathrm{BC}_{\mathcal C}\mid A_0\rightsquigarrow C\}.
\]
The superscript minus is the report's label for this restricted set; it is not a set complement. [TR Lemma 7, beginning of proof, printed p.11.]

On \(\mathrm{BC}_{\mathcal C}^{-}\), define
\[
  C\sim D
  \quad\Longleftrightarrow\quad
  C=D\ \text{or}\ \exists a\bigl(\{a\}\in S(C)\cap S(D)\bigr).
\]
Non-applicability of CR6 makes \(\sim\) an equivalence relation and supports Claim 1: if \(C\sim C'\), then \(S(C)=S(C')\), and every outgoing \(R(r)\)-edge from \(C\) transfers to \(C'\). [TR Lemma 7, Claim 1, printed pp.11–12.]

Claim 2 uses p-admissibility. For every class \([C]\) and concrete domain \(\mathcal D_i\), choose a solution \(\delta([C],i)\) of \(\operatorname{con}_i(S(C))\) such that, for every basic concrete atom \(D=p(f_1,\ldots,f_k)\) from \(\mathcal D_i\),
\[
  \delta([C],i)\models D
  \quad\Longleftrightarrow\quad
  D\in S(C).
\]
CR5 and the definition of \(\mathrm{BC}_{\mathcal C}^{-}\) ensure \(\bot\notin S(C)\); CR7 therefore gives at least one solution. If every solution satisfied at least one absent atom, the concrete conjunction would imply the disjunction of all such absent atoms; convexity would then make it imply one absent atom, and CR8 would have added that atom, a contradiction. [TR Lemma 7, Claim 2, printed p.12.]

The intended type-correct model extracted from the report is:
\[
\begin{aligned}
  \Delta^{\mathcal I}&=\{[C]\mid C\in\mathrm{BC}_{\mathcal C}^{-}\},\\
  A^{\mathcal I}&=\{[C]\in\Delta^{\mathcal I}\mid A\in S(C)\},\\
  a^{\mathcal I}&=[\{a\}]\quad\text{when }\{a\}\in\mathrm{BC}_{\mathcal C},\\
  r^{\mathcal I}&=\{([C],[D])\mid \exists D'\in[D]:(C,D')\in R(r)\},\\
  f^{\mathcal I}([C])&=\delta([C],i)(f)
  \quad\text{when }f\text{ occurs in an }\mathcal D_i\text{-atom in }S(C),
\end{aligned}
\]
with features partial elsewhere, concept/role names outside the relevant source sets interpreted as empty, and an individual whose nominal is absent interpreted arbitrarily as \([A_0]\). Equivalence classes make named individuals and roles well-defined; CR9 prevents a feature at one class from being forced into two disjoint concrete carriers. The report's displayed formulas have local variable/type slips recorded in §13; the clauses above are the readings required by Claim 2 and the subsequent truth proof. [TR Lemma 7, model definition and following bullets, printed p.13.]

Claim 3 is the following structural equivalence for every \([C]\in\Delta^{\mathcal I}\) and every \(D\in\mathrm{BC}_{\mathcal C}\cup\{\bot\}\):
\[
  [C]\in D^{\mathcal I}\quad\Longleftrightarrow\quad D\in S(C).
\]
The report checks separately \(D=\top\), \(D=\bot\), concept names, nominals, and concrete atoms. The nominal case uses the equivalence classes, and the concrete case uses the exact-choice property of \(\delta([C],i)\). [TR Lemma 7, Claim 3, printed p.13.]

It then verifies the four normalized GCI forms with CR1–CR4 and the two normalized RI forms with CR10–CR11. Finally, \(A_0\in S(A_0)\) by initialization while \(B_0\notin S(A_0)\) by failure of S1, so Claim 3 gives
\[
  [A_0]\in A_0^{\mathcal I}\setminus B_0^{\mathcal I}.
\]
This is the required countermodel. [TR Lemma 7, end of proof, printed pp.13–14.]

### 9.4 Conference Theorem 4

**Exact statement.** If \(\mathcal D_1,\ldots,\mathcal D_n\) are p-admissible concrete domains, then subsumption in \(\mathcal{EL}^{++}(\mathcal D_1,\ldots,\mathcal D_n)\) with respect to CBoxes can be decided in polynomial time. [IJCAI Theorem 4, printed p.367.]

The proof chain is: normalize and reduce to concept names by Lemma 1 and the fresh-name query reduction; saturate in polynomially many polynomial-cost applications by Lemma 2; decide the saturated query by the sound-and-complete Lemma 3 criterion. [IJCAI §3, Lemmas 1–3 and Theorem 4, printed pp.365–367.]

The report's corresponding Theorem 8 is stronger in the tasks it lists: satisfiability, subsumption, ABox consistency, and the instance problem in \(\mathcal{EL}^{++}\) are polynomial-time decidable. That stronger task list depends on the report's §2 reductions and must not be quoted as the literal statement of conference Theorem 4. The report additionally derives a linear-size small-model property as Theorem 9; the conference paper does not state that theorem. [TR Theorems 8–9, printed p.14; IJCAI Theorem 4, printed p.367.]

## 10. Source concrete-domain examples

### 10.1 The rational domain \(\mathbb Q\)

The source defines \(\mathbb Q=(\mathbb Q,P^{\mathbb Q})\) with:

- unary \(\top_{\mathbb Q}\), whose extension is all rationals;
- unary \(=_{q}\) and \(>_{q}\) for each \(q\in\mathbb Q\);
- binary equality \(=\);
- binary \(+_{q}\) for each \(q\in\mathbb Q\), with
  \((+_q)^{\mathbb Q}=\{(q',q'')\in\mathbb Q^2\mid q'+q=q''\}\).

The conference paper says polynomial reasoning reduces to linear programming and sends convexity to the report; Proposition 5 states that \(\mathbb Q\) is p-admissible. The report proves polynomial implication via polynomial satisfiability in an auxiliary predicate expansion and gives a constructive convexity proof. [IJCAI concrete-domain subsection and Proposition 5, printed p.367; TR §4, Proposition 10, printed pp.14–17.]

### 10.2 The string domain \(\mathbb S\)

Let \(\Sigma\) be the ISO 8859-1 (Latin-1) character set. The source defines \(\mathbb S=(\Sigma^*,P^{\mathbb S})\) with:

- unary \(\top_{\mathbb S}\), extension \(\Sigma^*\);
- unary \(=_{w}\) for each \(w\in\Sigma^*\);
- binary equality \(=\);
- binary \(\operatorname{conc}_{w}\) for each \(w\in\Sigma^*\), intended to contain \((w',w'')\) exactly when \(w''=w'w\).

The conference paper cites earlier work for polynomial reasoning and sends convexity to the report; Proposition 5 states that \(\mathbb S\) is p-admissible. The report gives the reduction and constructive convexity argument as Proposition 11. Both sources misprint the concrete-domain superscript on the concatenation extension as \(\mathbb Q\), although the surrounding definition is of \(\mathbb S\); §13 records this. [IJCAI concrete-domain subsection and Proposition 5, printed p.367; TR §4, Proposition 11, printed pp.14 and 17–19.]

### 10.3 Printed non-convex examples

The conference paper illustrates fragility of convexity with:

- \(\mathbb Q_{\leq q,>q}\), extending \(\mathbb Q\) with unary \(\leq_q\). The conjunction \(>_0(f')\) implies \(\leq_0(f)\lor>_0(f)\) but neither disjunct, so the domain is not convex. [IJCAI p-admissible/non-admissible subsection, printed p.367.]
- A string domain \(\mathbb S^*\) over finite alphabet \(\Sigma=\{a_1,\ldots,a_n\}\) with prefix and suffix predicates. The conjunction \(\operatorname{suff}_{a_1}(f)\) implies \(\operatorname{pref}_{a_1}(f)\lor\cdots\lor\operatorname{pref}_{a_n}(f)\) but no single disjunct. [IJCAI same subsection, printed p.367.]

The report uses a slightly different rational witness domain with \(<_q\), \(=_0\), and \(>_0\), and gives additional string variants before the lower-bound section. These variants are report examples, not literal replacements for the two conference examples. [TR §4, end of printed pp.19–20.]

The introduction's application examples are also source claims, not worked formal derivations: SNOMED is described as using \(\mathcal{EL}\) with an acyclic TBox, large parts of GALEN as expressible in \(\mathcal{EL}\) with GCIs and transitive roles, and Gene Ontology as an acyclic \(\mathcal{EL}\)-TBox with one transitive role. They are historically framed claims made in 2005 and should not be silently updated into claims about current versions of those resources. [IJCAI §1, printed p.364; TR §1, printed p.2.]

## 11. Additional constructors and exact Theorems 6–12 boundaries

Section 4 of the conference paper now restricts to the sublanguage \(\mathcal{EL}\), containing only concept names, \(\top\), conjunction, and existential restriction, and to general TBoxes (finite sets of GCIs). The negative results do not automatically concern the full positive CBox language with every \(\mathcal{EL}^{++}\) feature simultaneously. [IJCAI §4 opening, printed p.367; TR §5 opening, printed p.20.]

Table 3 supplies the additional semantics:
\[
\begin{array}{rcl}
 (\neg C)^{\mathcal I}&=&\Delta^{\mathcal I}\setminus C^{\mathcal I},\\
 (C\sqcup D)^{\mathcal I}&=&C^{\mathcal I}\cup D^{\mathcal I},\\
 (\forall r.C)^{\mathcal I}&=&\{x\mid\forall y((x,y)\in r^{\mathcal I}\Rightarrow y\in C^{\mathcal I})\},\\
 (\geq n\ r)^{\mathcal I}&=&\{x\mid \#\{y\mid(x,y)\in r^{\mathcal I}\}\geq n\},\\
 (\leq n\ r)^{\mathcal I}&=&\{x\mid \#\{y\mid(x,y)\in r^{\mathcal I}\}\leq n\},\\
 (\exists r^{-}.C)^{\mathcal I}&=&\{x\mid\exists y((y,x)\in r^{\mathcal I}\land y\in C^{\mathcal I})\}.
\end{array}
\]
[IJCAI Table 3, printed p.367; TR Table 3, printed p.20.]

### 11.1 Theorem 6: atomic negation

Let \(\mathcal{EL}^{\neg}\) be \(\mathcal{EL}\) with unrestricted concept negation and \(\mathcal{EL}^{(\neg)}\) restrict negation to concept names. The paper observes that \(\mathcal{EL}^{\neg}\) is a notational variant of \(\mathcal{ALC}\), and replaces a complex \(\neg C\) by \(\neg A\) for fresh \(A\) together with \(A\sqsubseteq C\) and \(C\sqsubseteq A\). **Theorem 6 states that both satisfiability and subsumption in \(\mathcal{EL}^{(\neg)}\) with respect to general TBoxes are ExpTime-complete.** This is the only theorem among 6–12 that explicitly states both tasks. [IJCAI atomic-negation subsection and Theorem 6, printed p.368; TR Theorem 13, printed p.21.]

### 11.2 Theorem 7: disjunction

Let \(\mathcal{ELU}\) extend \(\mathcal{EL}\) by disjunction. The ExpTime upper bound comes from its being a fragment of \(\mathcal{ALC}\). For the lower bound, from an \(\mathcal{EL}^{(\neg)}\) TBox \(\mathcal T\) and concept name \(A_0\), take a fresh \(A'\) for every concept name \(A\), replace \(\neg A\) by \(A'\), take another fresh concept name \(L\), and add the schemata
\[
  \top\sqsubseteq A\sqcup A',\qquad A\sqcap A'\sqsubseteq L,
  \qquad \exists r.L\sqsubseteq L.
\]
The first two are for every concept name \(A\) occurring in \(\mathcal T\). The paper prints the last GCI schematically with \(r\) but does not append an explicit “for every relevant role” phrase in the bullet; its use as propagation along connected countermodels requires the relevant role instances. It concludes
\[
  A_0\text{ satisfiable w.r.t. }\mathcal T
  \quad\Longleftrightarrow\quad
  A_0\not\sqsubseteq_{\mathcal T^*}L.
\]
**Theorem 7 states only that subsumption in \(\mathcal{ELU}\) with respect to general TBoxes is ExpTime-complete.** [IJCAI disjunction subsection and Theorem 7, printed p.368; TR disjunction subsection and Theorem 14, printed p.21.]

### 11.3 Theorem 8: the fixed at-least-two constructor

\(\mathcal{EL}^{\geq2}\) adds restrictions of the form \((\geq2\ r)\), not arbitrary qualified number restrictions. The upper bound comes from an \(\mathcal{ALC}\) language with number restrictions. For the lower bound, normalize an \(\mathcal{ELU}\) TBox so its GCIs have the five forms
\[
 C\sqsubseteq D,\quad C_1\sqcap C_2\sqsubseteq C,\quad
 C\sqsubseteq C_1\sqcup C_2,\quad
 C\sqsubseteq\exists r.D,\quad \exists r.C\sqsubseteq D,
\]
with the displayed metavariables concept names or \(\top\). Replace each \(C\sqsubseteq C_1\sqcup C_2\), using fresh concept names \(A,B\) and fresh role \(r\), by
\[
  C\sqsubseteq\exists r.A\sqcap\exists r.B,
  \qquad C\sqcap\exists r.(A\sqcap B)\sqsubseteq C_1,
  \qquad C\sqcap(\geq2\ r)\sqsubseteq C_2.
\]
Coincident witnesses force the \(C_1\) branch and distinct witnesses force the \(C_2\) branch. The source states preservation of the queried subsumption. **Theorem 8 states that subsumption in \(\mathcal{EL}^{\geq2}\) with respect to general TBoxes is ExpTime-complete.** [IJCAI at-least subsection and Theorem 8, printed p.368; TR at-least subsection and Theorem 15, printed p.22.]

Immediately after Theorem 8, the conference paper says similar reductions give ExpTime-completeness when \(\mathcal{EL}\) is extended by role negation, role union, or transitive closure. This is not numbered among conference Theorems 6–12. The report states the three-language result as Theorem 16 and prints the corresponding reductions. [IJCAI paragraph after Theorem 8, printed p.368; TR Theorem 16, printed p.23.]

### 11.4 Theorem 9: a non-convex concrete domain

For any non-convex concrete domain \(\mathcal D\), \(\mathcal{EL}(\mathcal D)\) is \(\mathcal{EL}\) plus features \(\Delta^{\mathcal I}\rightharpoonup\Delta^{\mathcal D}\) and atoms \(p(f_1,\ldots,f_k)\). The proof first strengthens Theorem 7 to TBoxes containing ordinary \(\mathcal{EL}\) GCIs and at most one disjunctive GCI \(A\sqsubseteq B_1\sqcup B_2\). [IJCAI non-p-admissible subsection, printed p.368; TR Theorem 17 and following reduction, printed pp.23–24.]

Non-convexity supplies a satisfiable conjunction \(c\) implying a minimal disjunction \(a_1\lor\cdots\lor a_m\) but no individual disjunct. Minimality gives assignments satisfying \(c\land a_1\land\neg(a_2\lor\cdots\lor a_m)\) and \(c\land(a_2\lor\cdots\lor a_m)\land\neg a_1\). Replace the one GCI \(A\sqsubseteq B\sqcup B'\) by
\[
  A\sqsubseteq c,\qquad a_1\sqsubseteq B,
  \qquad a_i\sqsubseteq B'\ (2\leq i\leq m).
\]
The queried subsumption is preserved. **Theorem 9 states ExpTime-hardness, not completeness, for subsumption in \(\mathcal{EL}(\mathcal D)\) with respect to general TBoxes for every non-convex \(\mathcal D\).** It assumes non-convexity; it does not require polynomial satisfiability/implication. The report notes a matching upper bound only under an additional ExpTime bound for \(\mathcal D\)-satisfiability. [IJCAI Theorem 9, printed p.368; TR Theorem 18, Corollary 19, and following upper-bound sentence, printed pp.24–25.]

The prose calls p-admissibility “necessary,” but the formal theorem isolates the convexity failure and proves hardness. It does not prove the converse that every failure of either clause of p-admissibility has exactly that complexity. [IJCAI non-p-admissible subsection and Theorem 9, printed p.368; TR corresponding subsection, printed pp.23–25.]

### 11.5 Theorem 10: inverse roles and the open gap

\(\mathcal{ELI}\) extends \(\mathcal{EL}\) with \(\exists r^{-}.C\). The lower bound reduces satisfiability for \(\mathcal{ALE}\) with primitive TBoxes, where \(\mathcal{ALE}\) supplies value restrictions and atomic negation and a primitive GCI has a concept name on the left. [IJCAI inverse-role subsection, printed pp.368–369; TR inverse-role subsection, printed p.25.]

For fresh \(L\), the transformed \(\mathcal{ELI}\) TBox keeps \(A\sqsubseteq D\) when \(D\) is a concept name or \(\exists r.B\), converts \(A\sqsubseteq\forall r.B\) to \(\exists r^{-}.A\sqsubseteq B\), converts \(A\sqsubseteq\neg B\) to \(A\sqcap B\sqsubseteq L\), and adds \(\exists r.L\sqsubseteq L\). Since \(\exists r^{-}.A\sqsubseteq B\) is equivalent to \(A\sqsubseteq\forall r.B\), and \(L\) behaves as bottom in connected countermodels, satisfiability of \(A_0\) is equivalent to \(A_0\not\sqsubseteq L\) in the transformed TBox. [IJCAI inverse-role reduction, printed pp.368–369; TR inverse-role reduction, printed p.25.]

**Theorem 10 states only PSPACE-hardness of subsumption in \(\mathcal{ELI}\) with respect to general TBoxes.** The very next sentence says the exact complexity was still open and that the best upper bound known to the authors was ExpTime, inherited from \(\mathcal{ALCI}\). This is a 2005 source-status statement: it must not be upgraded to PSPACE-completeness, ExpTime-completeness, or an unqualified present-day open-problem claim without separate later research. [IJCAI Theorem 10 and following sentence, printed p.369; TR Theorem 20 and following sentence, printed pp.25–26.]

The conference display of the assumed primitive normal forms omits \(A\sqsubseteq B\sqcap B'\) even though its following sentence mentions \(B'\). The report includes that conjunction form, but its printed transformation list does not explicitly say to split or carry it; the harmless intended repair is to split it into \(A\sqsubseteq B\) and \(A\sqsubseteq B'\) before the displayed transformation. This is a source-detail boundary, not an additional theorem. [IJCAI inverse-role normal-form display, printed p.368; TR inverse-role normal-form display and transformation, printed p.25.]

### 11.6 Theorem 11: at-most one and functional-role boundary

\(\mathcal{EL}^{\leq1}\) adds only \((\leq1\ r)\). The upper bound again comes from an \(\mathcal{ALC}\) language with number restrictions. The lower bound uses \(\mathcal{FL}^{tf}_0\), whose concept constructors are conjunction and value restriction and whose roles are required to be total functions. [IJCAI at-most subsection, printed p.369; TR at-most subsection, printed pp.26–27.]

Given a general \(\mathcal{FL}^{tf}_0\) TBox \(\mathcal T\), replace each occurrence of \(\forall r.C\) on a GCI left-hand side by \(\exists r.C\), and each occurrence on a GCI right-hand side by \((\leq1\ r)\sqcap\exists r.C\), obtaining \(\mathcal T^*\). The source states
\[
  A_0\sqsubseteq_{\mathcal T}B_0\text{ in }\mathcal{FL}^{tf}_0
  \quad\Longleftrightarrow\quad
  A_0\sqsubseteq_{\mathcal T^*}B_0\text{ in }\mathcal{EL}^{\leq1}.
\]
**Theorem 11 states that subsumption in \(\mathcal{EL}^{\leq1}\) with respect to general TBoxes is ExpTime-complete.** [IJCAI at-most subsection and Theorem 11, printed p.369; TR Lemma 21 and Theorem 22, printed pp.26–27.]

The report proves the equivalence in Lemma 21 by contraposition: from an \(\mathcal{EL}^{\leq1}\) countermodel, delete all outgoing \(r\)-edges at points with more than one, then add a fresh sink to totalize each partial role function; conversely, in a total functional interpretation \(\exists r.C\) and \(\forall r.C\) coincide. The report explicitly excludes \(\top\) from the \(\mathcal{FL}^{tf}_0\) concepts needed for the fresh-sink preservation step. [TR Lemma 21, printed pp.26–27.]

After its Theorem 22, the report says an analogous ExpTime-completeness result holds if \((\leq1\ r)\) is replaced by a CBox assertion \(\operatorname{Funct}(r)\), satisfied when \(r^{\mathcal I}\) is a partial function. The conference section heading mentions functional roles but does not print this separate assertion or theorem. [TR paragraph after Theorem 22, printed p.27; IJCAI section heading and Theorem 11, printed p.369.]

### 11.7 Theorem 12: \(\mathcal{FL}_0\)

Here \(\mathcal{FL}_0\) has conjunction and value restriction with arbitrary binary role interpretations; \(\mathcal{FL}^{tf}_0\) additionally requires roles to be total functions. The conference paper cites the report for the fact that, for a general TBox \(\mathcal T\), atomic subsumption in these two semantics coincides. [IJCAI paragraph before Theorem 12, printed p.369; TR Lemma 23, printed pp.28–29.]

The report's countermodel direction starts from an \(\mathcal{FL}_0\) countermodel at \(x_0\), takes as its new domain all finite sequences of role names (including the empty sequence \(\epsilon\)), sets
\[
  A^{\mathcal J}=\{S\mid S^{\mathcal I}(x_0)\subseteq A^{\mathcal I}\},
  \qquad
  r^{\mathcal J}=\{(S,Sr)\},
\]
and checks the four normalized GCI shapes \(A\sqsubseteq B\), \(A\sqsubseteq\forall r.B\), \(A\sqcap A'\sqsubseteq B\), and \(\forall r.A\sqsubseteq B\). Every \(r^{\mathcal J}\) is a total function and \(\epsilon\) remains in \(A_0^{\mathcal J}\setminus B_0^{\mathcal J}\). [TR Lemma 23, printed pp.28–29.]

**Theorem 12 states that subsumption in \(\mathcal{FL}_0\) with respect to general TBoxes is ExpTime-complete.** The upper bound is inherited from \(\mathcal{ALC}\); the lower bound transfers the known ExpTime-hardness for \(\mathcal{FL}^{tf}_0\) through Lemma 23. The theorem does not state an ABox, data-complexity, or satisfiability result. [IJCAI Theorem 12, printed p.369; TR §6, Lemma 23 and Theorem 24, printed pp.28–29.]

### 11.8 Exact conference/report numbering crosswalk

| Conference result | Report locus | Difference in printed scope/detail |
|---|---|---|
| Lemma 1, p.365 | Lemma 2, p.5 and Figure 1, p.6 | report prints NF1–NF7 and the two-phase linear-size proof |
| Lemma 2, p.366 | Lemma 5, p.9 | report prints the monotone-cardinality proof |
| Lemma 3, pp.366–367 | Lemma 4, p.8; Lemmas 6–7, pp.9–14 | report separates soundness/completeness and prints the full countermodel |
| Theorem 4, p.367 | Theorem 8, p.14 | report includes satisfiability, ABox consistency, and instance checking, not just subsumption |
| Proposition 5, p.367 | Propositions 10–11, pp.14–19 | report prints the p-admissibility proofs for \(\mathbb Q\) and \(\mathbb S\) |
| Theorem 6, p.368 | Theorem 13, p.21 | same two-task complexity statement; report supplies expanded context |
| Theorem 7, p.368 | Theorem 14, p.21 | same subsumption statement; report expands comparison and reduction context |
| Theorem 8, p.368 | Theorem 15, p.22 | same fixed-\(\geq2\) subsumption statement |
| unnumbered role-constructor paragraph, p.368 | Theorem 16, p.23 | report states the three ExpTime-completeness results as a theorem and prints reductions |
| Theorem 9, p.368 | Theorems 17–18 and Corollary 19, pp.24–25 | report proves the single-disjunction strengthening and enumerates concrete-domain corollaries |
| Theorem 10, p.369 | Theorem 20, p.25 and open-bound sentence, p.26 | same PSPACE-hard statement and same ExpTime/open gap |
| Theorem 11, p.369 | Lemma 21 and Theorem 22, pp.26–27 | report prints both directions of the transformation proof and the functional-role analogue |
| Theorem 12, p.369 | Lemma 23 and Theorem 24, pp.28–29 | report prints the \(\mathcal{FL}_0/\mathcal{FL}^{tf}_0\) coincidence proof |

All crosswalk entries are based on the result statements and immediately surrounding proof text in the cited primary sources. [IJCAI §§3–4, printed pp.365–369; TR §§3–6, printed pp.5–29.]

## 12. Exact proof-printing boundaries

The conference paper explicitly delegates “Proofs and further technical details” to the report. The resulting boundaries are:

- It states conservative linear normalization and Lemma 1, but does not print NF1–NF7, their two-phase order, or the quadratic-blow-up warning. [IJCAI §3, p.365; TR §3.1, pp.5–6.]
- It gives the polynomial-count reasons for Lemma 2, but not the report's formal monotone-cardinality proof. [IJCAI p.366; TR Lemma 5, p.9.]
- It details only CR6 soundness and gives only a “basically” countermodel sketch for Lemma 3. All other rule cases, concrete witness selection, equivalence-class model, the displayed structural equivalence, and axiom verification are report-only. [IJCAI pp.366–367; TR Lemmas 6–7, pp.9–14.]
- It asserts mutual polynomial reducibility of standard reasoning tasks by citation. The report prints the reductions and then states the stronger four-task Theorem 8. [IJCAI §2, p.365; TR §2, pp.3–4 and Theorem 8, p.14.]
- It states Proposition 5 after brief references to linear programming/earlier work and says convexity is shown in the report. The report prints the two long convexity proofs. [IJCAI p.367; TR Propositions 10–11, pp.14–19.]
- Theorem 6's complex-to-atomic-negation replacement is printed in both versions; neither re-proves the cited \(\mathcal{ALC}\) ExpTime result. [IJCAI p.368; TR p.21.]
- The conference paper sketches the reductions for Theorems 7–10; the report expands their normal forms, intermediate Theorems 16–18, and corollary, but still uses phrases such as “not hard to verify” at some equivalence points. [IJCAI pp.368–369; TR pp.21–25.]
- The conference paper prints only the transformation equation behind Theorem 11 and cites the report for the \(\mathcal{FL}_0\) coincidence behind Theorem 12. The report prints Lemmas 21 and 23 in full. [IJCAI p.369; TR pp.26–29.]
- The underlying hardness/upper-bound inputs from Schild, Calvanese, De Giacomo–Lenzerini, Lutz, Toman–Weddell, and others remain cited results; neither primary source re-proves those external theorems. [IJCAI §4 and references, pp.368–369; TR §§5–6 and references, pp.20–32.]

No stronger proof status should be assigned to a conference sketch merely because the report contains a fuller argument; when report details are used, the report locator should be cited explicitly.

## 13. Printed defects and type-correct readings

These defects were checked against rendered pages, not inferred only from OCR.

### 13.1 Conference paper

1. The affiliation prints “Intitute for Theoretical Computer Science.” This is bibliographic typography, not a different institution. [IJCAI title block, printed p.364.]
2. The prose prints “can by found” for “can be found,” “it shown” for “it is shown,” “polynominal” twice, and the heading “P-admissibile.” These are ordinary typographical errors. [IJCAI pp.365–367.]
3. Table 2 CR11 prints
   \[
     R(r_3):=R_i(r_3)\cup\{(C,E)\},
   \]
   although no stage \(i\) is defined there. The type-correct update is \(R(r_3):=R(r_3)\cup\{(C,E)\}\), as required by the trigger and the soundness proof. [IJCAI Table 2, printed p.366; TR Lemma 6 CR11, printed p.11.]
4. The prose below Table 2 refers to \(\operatorname{con}_j(S_i(C))\), whereas the table uses \(\operatorname{con}_j(S(C))\) and no iteration-indexed \(S_i\) has yet been introduced. The defined operator is \(\operatorname{con}_j(\Gamma)\), and the completion trigger uses the current \(S(C)\). [IJCAI printed p.366; TR printed p.8.]
5. In the definition of the string-domain concatenation predicate, the extension is printed with a \(\mathbb Q\) superscript even though it is an \(\mathbb S\) predicate over strings. The intended standing is fixed by the surrounding definition \(\mathbb S=(\Sigma^*,P^{\mathbb S})\) and the string equation \(w''=w'w\). [IJCAI printed p.367; TR printed p.14.]
6. In the inverse-role reduction, the conference normal-form display omits \(A\sqsubseteq B\sqcap B'\) but the following sentence still says \(A,B,B'\) are concept names. The report prints the conjunction form. Splitting such a right-hand conjunction into two atomic inclusions is the type-correct way to make the displayed transformation exhaustive. [IJCAI printed p.368; TR printed p.25.]

### 13.2 Technical report

1. Report Table 2 repeats the conference CR11 \(R_i(r_3)\) defect. [TR Table 2, printed p.7.]
2. In Lemma 7, Claim 1's CR3 case concludes with \((D,E)\in R(r)\), but the claimed transferred edge is \((C',D)\in R(r)\). The same proof's CR10 and CR11 cases cite nonexistent rules CR12 and CR13; the only matching rules in Table 2 are CR10 and CR11. [TR Lemma 7, Claim 1, printed p.12; TR Table 2, printed p.7.]
3. Claim 2 quantifies a concrete-domain index \(i\) but once prints \(\delta([C],t)\models D\); the consistent index is \(i\). [TR Lemma 7, Claim 2, printed p.12.]
4. The displayed role interpretation binds \(D'\in[D]\) but prints the edge condition \((C,D)\in R(r)\). The later model verification uses \((C,D')\in R(r)\), which is the bound-variable-correct clause recorded in §9.3. [TR model definition, printed p.13; RI/GCI verification, printed p.14.]
5. A concrete solution \(\delta([C],i)\) is defined as a mapping from feature names to concrete values, but the displayed feature interpretation assigns the whole mapping to \(f^{\mathcal I}([C])\). The type-correct value is \(\delta([C],i)(f)\), as required by the concrete-atom truth case. [TR solution definition, printed p.9; Claim 2, p.12; model definition and Claim 3, p.13.]
6. In the final verification of \(r_1\circ r_2\sqsubseteq s\), the report prints generic \(R(r)\) for both component edges and invokes CR10. The required typed premises are in \(R(r_1)\) and \(R(r_2)\), and the required composition rule is CR11. [TR end of Lemma 7, printed p.14; Table 2, printed p.7.]
7. The report's disjunction reduction once says “\(C\) is satisfiable” where the reduction input is the concept name \(A_0\); the equivalence and theorem use \(A_0\). [TR disjunction subsection, printed p.21.]
8. The report includes \(A\sqsubseteq B\sqcap B'\) in the inverse-role source normal form but does not explicitly include that form in the subsequent transfer list. Splitting it into \(A\sqsubseteq B\) and \(A\sqsubseteq B'\) before translation makes the list exhaustive and agrees with ordinary conjunction semantics; this repair is not printed as a separate lemma. [TR inverse-role subsection, printed p.25.]

These are local printed defects in formulas/references. They do not license strengthening a theorem, deleting a rule side condition, or attributing the repaired text verbatim to the authors.

## 14. Terminology and OWL nonidentity boundary

The source's names have the following standing:

- \(\mathcal{EL}\) is the base description logic with \(\top\), conjunction, and existential restriction. [IJCAI §§1 and 4, printed pp.364 and 367.]
- \(\mathcal{EL}^{++}\) is the paper's research language adding \(\bot\), nominals, p-admissible concrete-domain atoms, GCIs, and the one-role-right-hand-side RIs defined above. [IJCAI §§1–3, printed pp.364–367.]
- A CBox is the paper's finite GCI-plus-RI axiom set; a general TBox is a finite GCI set. [IJCAI §2, printed p.365.]
- “Completion” in Table 2 means finite forward saturation of \(S\) and \(R\). It is not a branch-generating tableau in this source. [IJCAI §3, printed p.366; TR §3, printed pp.6–14.]
- \(\mathcal{EL}^{(\neg)}\), \(\mathcal{ELU}\), \(\mathcal{EL}^{\geq2}\), \(\mathcal{EL}(\mathcal D)\), \(\mathcal{ELI}\), \(\mathcal{EL}^{\leq1}\), \(\mathcal{FL}_0\), and \(\mathcal{FL}^{tf}_0\) are separately defined comparison languages in the negative-results section. Their theorems must not be folded into the positive \(\mathcal{EL}^{++}\) grammar. [IJCAI §4, printed pp.367–369; TR §§5–6, printed pp.20–29.]

The 2005 paper refers generically to the then-current W3C language “OWL” as an ontology language and investigates constructors available in languages “like OWL.” It nowhere uses the later name “OWL 2 EL,” nowhere prints the later profile grammar, and nowhere states \(\mathcal{EL}^{++}=\) OWL 2 EL. [IJCAI §1, printed p.364; complete IJCAI paper, printed pp.364–369.]

The 2012 W3C Recommendation defines OWL 2 EL as a syntactic subset of OWL 2 with its own supported class expressions, axioms, datatype inventory, and global restrictions. It cites \(\mathcal{EL}^{++}\) as a basis and says the “EL” name reflects the profile's basis in the EL family. Its feature list includes, among other OWL constructs, self restrictions, assertions, reflexive object properties, functional data properties, and keys. This establishes influence, not literal identity of the two formal languages. [W3C *OWL 2 Profiles (Second Edition)*, §§1–2.2, especially §§2.1 and 2.2.5–2.2.6.]

Accordingly, a handbook presentation faithful to this source should call the subject the paper's \(\mathcal{EL}^{++}\), cite the later OWL profile only as later standardization context, and avoid importing OWL 2 syntax/global restrictions back into the 2005 definitions.

## 15. Separation from later reasoning machinery

The following boundaries are source-exact and prevent terminology drift:

- The completion state is indexed by basic concept descriptions and role names. It does not contain ABox individuals, assertion labels, generated anonymous nodes, or an ABox edge relation. [IJCAI §3, printed p.366; TR §3.2, printed pp.6–8.]
- Nominals are concept descriptions interpreted as singletons. Their presence in \(S(C)\) drives CR6 and the global-inconsistency limb of Lemma 3; this is not an ABox equality-merging rule stated in later ABox terminology. [IJCAI Table 1, CR6, and Lemma 3, printed pp.365–367.]
- The algorithm terminates because \(S\) and \(R\) range over finite source sets and only gain entries. No blocking condition appears or is needed. [IJCAI Lemma 2, printed p.366; TR Lemma 5, printed p.9.]
- A CBox is not interchangeable with a general TBox: the former includes RIs and the latter, in the paper's terminology, contains GCIs only. [IJCAI §2, printed p.365.]
- Inverse roles are not part of the positive completion algorithm. They are examined separately in Theorem 10, with only PSPACE-hardness and a source-era ExpTime upper bound. [IJCAI Table 1 and Theorem 10, printed pp.365 and 369.]
- The source imposes pairwise disjoint concrete carriers and p-admissibility; replacing this by an arbitrary datatype theory invalidates CR9 and/or the polynomial-completeness argument. [IJCAI §§2–4, printed pp.365–368; TR Definition 3 and Lemma 7 Claim 2, printed pp.8 and 12.]

No later ABox calculus, TBox absorption procedure, OWL 2 profile checker, role-chain regularity regime, or tableau-blocking method is owed by the 2005 source presentation unless separately introduced, defined, typed, distinguished from the source algorithm, and actually used. That is an integration boundary, not a new component of Baader–Brandt–Lutz's procedure.

## 16. Compact theorem-strength ledger

| IJCAI result | Input language / axiom regime | Task(s) | Exact strength |
|---|---|---|---|
| Lemma 1 | \(\mathcal{EL}^{++}\), arbitrary CBox | normalize subsumption | linear-time reduction to normalized CBoxes |
| Lemma 2 | normalized \(\mathcal{EL}^{++}\) CBox; p-admissible domains used by rules | saturation | polynomially many, polynomial-cost applications |
| Lemma 3 | normalized saturated CBox; concept names | subsumption | exact membership/global-nominal-bottom criterion |
| Theorem 4 | \(\mathcal{EL}^{++}(\mathcal D_1,\ldots,\mathcal D_n)\), CBoxes, every \(\mathcal D_i\) p-admissible | subsumption | polynomial time |
| Proposition 5 | source domains \(\mathbb Q,\mathbb S\) | p-admissibility | both are p-admissible |
| Theorem 6 | \(\mathcal{EL}^{(\neg)}\), general TBoxes | satisfiability and subsumption | ExpTime-complete |
| Theorem 7 | \(\mathcal{ELU}\), general TBoxes | subsumption | ExpTime-complete |
| Theorem 8 | \(\mathcal{EL}^{\geq2}\), general TBoxes | subsumption | ExpTime-complete |
| Theorem 9 | \(\mathcal{EL}(\mathcal D)\), general TBoxes, any non-convex \(\mathcal D\) | subsumption | ExpTime-hard only |
| Theorem 10 | \(\mathcal{ELI}\), general TBoxes | subsumption | PSPACE-hard; source-era upper bound ExpTime; exact complexity stated open |
| Theorem 11 | \(\mathcal{EL}^{\leq1}\), general TBoxes | subsumption | ExpTime-complete |
| Theorem 12 | \(\mathcal{FL}_0\), general TBoxes | subsumption | ExpTime-complete |

The ledger is a reformatting of the cited result statements, not a replacement for the hypotheses and proof boundaries above. [IJCAI §§3–4, printed pp.365–369.]

## 17. Integration checklist for N-c-010.a

- Use IJCAI numbering, not technical-report numbering. [Crosswalk in §11.8.]
- State all six concept constructors and both CBox axiom types before the algorithm. [IJCAI Table 1, p.365.]
- State pairwise disjoint concrete carriers and both p-admissibility clauses. [IJCAI pp.365–366.]
- State all four normalized GCI forms, both normalized RI forms, and the conservative/linear normalization boundary. [IJCAI Lemma 1, p.365; TR Figure 1, p.6.]
- Preserve every CR1–CR11 premise, especially \(C\rightsquigarrow D\) in CR6, the shared-feature/different-domain premises in CR9, and both edge premises in CR11. [IJCAI Table 2, p.366.]
- Print the type-correct CR11 action but disclose the source's \(R_i\) defect. [§§6 and 13.]
- Give the global nominal-bottom disjunct in Lemma 3, not just \(B\in S(A)\). [IJCAI Lemma 3, p.366.]
- Cite the report for full soundness/completeness/model extraction and distinguish its stronger Theorem 8 from conference Theorem 4. [TR pp.9–14.]
- Label any pedagogical saturation as newly constructed; do not attribute §8 to the paper. [§8.]
- Preserve “hard” versus “complete,” task lists, and the inverse-role open gap exactly. [IJCAI Theorems 6–12, pp.368–369.]
- Do not identify the source logic with OWL 2 EL, and do not describe the source completion as ABox tableau/blocking. [§§14–15.]
