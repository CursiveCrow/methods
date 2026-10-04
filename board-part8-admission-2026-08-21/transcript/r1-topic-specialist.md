# Part VIII admission board — round-one topic-specialist report

Role: mathematical correctness and completeness specialist for philosophical, nonclassical, modal, temporal, and substructural logics.

Review basis: the complete current reader route rooted at `handbook/parts/p08.tex` and `handbook/annex/p08.tex`, all routed exact-source units and editorial supplements, every calculus sheet referenced by those units, and the Part VIII treatment-ceiling rows in `spec/registers/new-content.csv`. I did not read another Part VIII seat's transcript. This was a source review only: no manuscript, specification, tool, test, or generated file was edited, and no build or test was run.

The route is not yet mathematically/source-content admissible. Two statements are directly false as written (hybrid-tableau completeness and the candidate-extension definition of Reiter default logic); several further systems are underdefined at exactly the points needed by their semantic or proof claims; and multiple mandatory register rows are still either expressly open or absent from the live route.

## F1 — The advertised hybrid-
\(K\) tableau completeness theorem is false for the displayed sheet

Severity: **blocking / theorem false for the specified calculus**  
Status: **OPEN**

Evidence:

- `handbook/parts/p08/temporal-epistemic-supplement.tex:654-677` fixes the hybrid language/calculus and states the soundness-and-completeness theorem at lines 669-676.
- `handbook/registry/calculi/tableaux-hybrid-k.tex:3-10` supplies only conjunction, negated conjunction, positive satisfaction, diamond, box, and nominal-replacement rules. It supplies neither a fresh-nominal root convention nor negative-satisfaction and the remaining signed Boolean/modal rules needed for the stated unrestricted language.

Concrete harm: the formula
\[
  @_i\neg @_j p\;\land\;@_j p
\]
is unsatisfiable. With the standard fresh-root nominal \(k\), the initial item is
\[
  @_k\bigl(@_i\neg @_j p\land @_j p\bigr).
\]
The displayed conjunction and positive-\(@\) rules yield
\(@_i\neg @_j p\) and \(@_j p\). The first formula semantically forces
\(@_j\neg p\), but the sheet has no negative-\(@\) rule by which to derive it, so the branch remains open. Thus the sheet cannot support the asserted closed-tableau characterization. This witness deliberately separates the two formulas at different nominals; the superficially similar formula \(@_i(\neg @_j p\land @_j p)\) is not a witness when the sheet's closure rule is read schematically.

Exact correction: either (a) give a complete labelled hybrid-
\(K\) tableau with an explicit fresh-root initialization, full Boolean/NNF policy, positive and negative satisfaction rules, positive-diamond and negative-box witnesses, positive-box and negative-diamond propagation, and exact nominal equality/bridge and closure rules, then prove the stated theorem for that calculus; or (b) define a semantics-preserving preprocessing into a genuinely complete restricted input language and state/prove completeness only for the resulting calculus. Until then, withdraw the completeness theorem and its system-card status.

Scholarly comparison: the full labelled rule surface and fresh-root convention are exhibited in Areces and ten Cate, *Hybrid Logics*, Figure 9: [chapter copy](https://www.researchgate.net/publication/228734663_Hybrid_logics).

## F2 — The default-logic “extension” clause admits circular self-support

Severity: **blocking / definition is not Reiter's extension operator**  
Status: **OPEN**

Evidence: `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:109-121` tests both applicability and closure directly against the candidate extension. That omits the grounded least-fixed-point component of Reiter's definition.

Minimal counterexample: let
\[
  W=\varnothing,
  \qquad
  D=\left\{\frac{p:p}{p}\right\}.
\]
The live candidate test admits \(E=\operatorname{Th}(\{p\})\): its prerequisite and conclusion both already lie in \(E\), and the justification is consistent with \(E\). In Reiter's construction, however, \(\Gamma_E\) is the *least* deductively closed set beginning with \(W\); the prerequisite \(p\) is never grounded at any stage, so \(\Gamma_E=\operatorname{Th}(\varnothing)\), and \(E\) is not an extension.

Exact correction: for each candidate \(E\), define \(\Gamma_E\) as the least set \(U\) such that (i) \(W\subseteq U\), (ii) \(U\) is deductively closed, and (iii), for every default
\[
  \frac{\alpha:\beta_1,\ldots,\beta_n}{\gamma}\in D,
\]
if \(\alpha\in U\) and \(\neg\beta_i\notin E\) for every \(i\), then \(\gamma\in U\). Define \(E\) to be an extension exactly when \(E=\Gamma_E\), and display the corresponding grounded stage construction. This also supplies the missing distinction between candidate consistency checks and prerequisite derivability.

Primary source: Reiter, “A Logic for Default Reasoning,” [Artificial Intelligence 13 (1980)](https://doi.org/10.1016/0004-3702(80)90014-4). A searchable scholarly reproduction of the operator appears in [*Genetic Algorithms for Extension Search in Default Logic*](https://www.researchgate.net/publication/220481057_Genetic_Algorithms_for_Extension_Search_in_Default_Logic); see also the [Stanford Encyclopedia survey](https://plato.stanford.edu/entries/logic-nonmonotonic/).

## F3 — Counterfactual truth conditions are partial, and the registered C1/VC and CK families are not delivered

Severity: **blocking / semantic clauses underdefined and mandatory family treatment absent**  
Status: **OPEN**

Evidence:

- `handbook/parts/p08/conditionals-deontic-free.tex:77-105` makes Stalnaker's \(f(w,A)\) available only “when one is available,” but nevertheless uses it in an unconditional truth clause. No empty/impossible-antecedent policy is given.
- The Lewis paragraph appeals to a “relevant closest region” while expressly allowing failure of a minimum sphere; no exact variably-strict truth clause identifies that region.
- `spec/registers/new-content.csv:88-90` requires the C1/VC treatment, CEM/limit comparison, completeness status, and the CK/neighbor-family selection- versus premise-semantics comparison. Those systems and statuses do not occur in the routed text.

Concrete harm: if \([A]=\varnothing\), the Stalnaker clause has no value because \(f(w,[A])\) is undefined; hence it does not define a two-valued satisfaction relation. When \(A\)-worlds approach without attaining a closest sphere, “the relevant closest region” likewise does not select an object, although standard Lewis semantics still has a precise ordering/sphere condition.

Exact correction:

1. Fix the selection-function type and totality policy. For example, require \(f(w,X)\in X\) for nonempty \(X\), and state explicitly that an empty antecedent makes the conditional vacuously true (or state and consistently use a different source-backed impossible-antecedent policy).
2. Define a nested sphere system \(\mathcal S_w\) and use the exact variably-strict clause
   \[
     M,w\models A\Box\!\!\to B
     \quad\Longleftrightarrow\quad
     [A]\cap\bigcup\mathcal S_w=\varnothing
     \ \text{or}\ 
     \exists S\in\mathcal S_w
     \bigl(S\cap[A]\ne\varnothing\ \land\ S\cap[A]\subseteq[B]\bigr),
   \]
   with centering, uniqueness, and limit assumptions stated separately rather than silently built into “closest.”
3. Supply exact, source-pinned C1/VC calculus and completeness statuses and the registered CK-neighbor-family selection/premise comparison, or formally leave the corresponding register rows unadmitted.

Scholarly source: the empty-antecedent disjunct and the non-limit ordering/sphere treatment are surveyed precisely in the [Stanford Encyclopedia entry on counterfactuals](https://plato.stanford.edu/entries/counterfactuals/).

## F4 — AGM is misstated/incomplete, and the KLM representation claim omits its model hypothesis

Severity: **high / exact postulates and representation boundary missing**  
Status: **OPEN**

Evidence:

- `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:58-64` and `:86-105` condition AGM inclusion on \(\neg A\notin K\). Standard AGM inclusion \(K*A\subseteq K+A\) is unconditional; the stated condition belongs to vacuity, which provides the reverse inclusion. The two supplementary conjunction postulates are merely named, not stated.
- The registered Levi-and-Harper obligation in `spec/registers/new-content.csv:104` is not met: the live text gives no Harper identity.
- The KLM paragraph invokes “minimal worlds” without defining a preferential model, its strict preference relation, the minimum operator, or smoothness. Smoothness is the hypothesis that supports the System-P representation at the stated level; ranked structure is additionally needed for rational monotony.

Exact correction: display all eight AGM revision postulates, including
\[
K*A\subseteq K+A
\]
without a side condition, the vacuity reverse inclusion under \(\neg A\notin K\), and
\[
  K*(A\land B)\subseteq (K*A)+B,
  \qquad
  \neg B\notin K*A\Longrightarrow (K*A)+B\subseteq K*(A\land B).
\]
Add the Harper identity \(K-A=K\cap(K*\neg A)\). For KLM, define a preferential structure \((S,\ell,\prec)\), \(\mu(X)\), and smoothness, then define \(A\mathrel{\sim}B\) by \(\mu([A])\subseteq[B]\); state the ranked-model hypothesis separately for rational monotony.

Sources: Alchourrón, Gärdenfors, and Makinson, [“On the Logic of Theory Change”](https://doi.org/10.2307/2274239); Kraus, Lehmann, and Magidor, [“Nonmonotonic Reasoning, Preferential Models and Cumulative Logics”](https://doi.org/10.1016/0004-3702(90)90101-5). A modern source displaying the exact AGM postulates is [*Artificial Intelligence* (2023)](https://www.sciencedirect.com/science/article/pii/S000437022300053X).

## F5 — The free-logic semantics conflates partial denotation with outer-domain denotation; registered free/QML surfaces remain incomplete

Severity: **high / semantic type ambiguity and missing registered distinctions**  
Status: **OPEN**

Evidence:

- `handbook/parts/p08/conditionals-deontic-free.tex:7-43` permits “partial or outer-domain denotation,” then says atoms with *non-denoting* terms are false. In an outer-domain model a term may denote an object outside the inner/existing domain, so that condition says nothing about it.
- `spec/registers/new-content.csv:82` requires separate positive, negative, and neutral free-logical systems plus descriptions. The live comparison table does not define three exact semantics/calculi, and its definite-description clause is only said to be “selected.”
- `spec/registers/new-content.csv:81` requires rigid designators in the quantified-modal treatment. `handbook/parts/p08/modal-logics-supplement.tex:862-915` specifies variables and predicates but no constant/term interpretation and hence no condition defining rigidity.

Concrete harm: under the live disjunction of semantic presentations, a constant can have a total outer denotation \(d\notin D_E\). It is not non-denoting, yet the clause does not decide whether \(P(c)\) must be false. That is exactly the difference between negative and positive outer-domain free logic, so the text has not fixed one consequence relation.

Exact correction: choose and type each presentation separately. In a partial negative semantics, terms are partial into the existing domain and every empty-termed atom/equality is false. In a total dual-domain negative semantics, predicate extensions—and the chosen strict equality policy—must force every atomic tuple containing a nonexisting object to be false. Define positive and neutral variants independently, including equality and consequence. Give an exact description operator clause for each claimed system. In QML, add the term/constant signature, its world-indexed interpretation, and the exact condition for a rigid designator (or explicitly route an existing definition that satisfies the register row).

Scholarly source: the dual-domain positive semantics and negative atomic policy are distinguished in the [Stanford Encyclopedia entry on free logic](https://plato.stanford.edu/entries/logic-free/).

## F6 — Distributed knowledge is used and indexed before it is defined

Severity: **high / definition-before-use and cross-reference failure**  
Status: **OPEN**

Evidence:

- `handbook/parts/p08/temporal-epistemic-supplement.tex:525-526` first uses \(D_G\).
- `handbook/parts/p08/temporal-epistemic-supplement.tex:642-643` later points to a supposed “semantic entry above,” but no definition occurs in the live routed file.
- A definition occurs only in the unrouted legacy unit `handbook/parts/p08/temporal-dynamic-epistemic.tex:588-605`. The actual route at `handbook/parts/p08.tex:25` includes the supplement, not that legacy unit.

Exact correction: before the first live use, for each nonempty finite group \(G\), define
\[
  R_G^D=\bigcap_{i\in G}{\sim_i},
  \qquad
  M,w\models D_GA
  \Longleftrightarrow
  \forall u\,(wR_G^D u\Rightarrow M,u\models A).
\]
At the same location distinguish \(D_G\) from everyone-knows \(E_G\), based on the union/one-step conjunction, and common knowledge \(C_G\), based on the reflexive-transitive closure of that union. Repair the later cross-reference to the actual live definition.

## F7 — Mandatory deontic, indicative-conditional, and dialetheism treatments are absent

Severity: **high / registered treatment ceilings not met**  
Status: **OPEN**

Evidence:

- `handbook/parts/p08/conditionals-deontic-free.tex:47-73` gives SDL and a general Chisholm/dyadic paragraph, but `spec/registers/new-content.csv:85` requires Ross's paradox, the Good Samaritan paradox, exact Chisholm diagnoses, and dyadic treatment. Ross and Good Samaritan are absent, and neither the Chisholm encodings nor a dyadic semantics is fixed.
- `handbook/parts/p08/conditionals-deontic-free.tex:109-126` gives an Adams-style clause and says only that a Lewis triviality result holds “under strong assumptions.” `spec/registers/new-content.csv:89` also requires the material-implication paradoxes and a suppositional account; neither appears, and the hypotheses of the invoked triviality result are not stated.
- `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:23-35` distinguishes dialetheism from paraconsistency, but `spec/registers/new-content.csv:98` requires paradox motivation, an exact inclosure schema, and replies. None is supplied.

Exact correction: at the registered survey/example ceiling, add source-pinned artifacts rather than generic family language: a formal Ross derivation; explicit Good Samaritan and Chisholm encodings with their exact diagnosis; typed dyadic semantics; the relevant material-implication paradoxes; one precise Lewis-triviality theorem with every probability/conditioning hypothesis; a defined suppositional policy; and an exact inclosure schema with the promised response survey. If those artifacts are intentionally excluded, change their register disposition rather than treating the Part as content-complete.

## F8 — The Łukasiewicz E/must obligation is expressly OPEN in reader-visible text

Severity: **blocking / admitted route says its mandatory calculus is absent**  
Status: **OPEN**

Evidence:

- `handbook/parts/p08/many-valued-supplement.tex:187-198` explicitly says register item N-b-028 remains an OPEN inclusion obligation and refuses a system card because no calculus has been fixed.
- `spec/registers/new-content.csv:100` requires \(\L_3\), finite \(\L_n\), infinite \(\L\), an axiomatization, McNaughton's theorem, and real semantics at an E/must ceiling.
- The matrices and mathematical survey at `handbook/parts/p08/many-valued-supplement.tex:202-227` and `:325-347` do not supply the missing exact calculus/axiomatization or the resulting theoremhood/completeness status.

Exact correction: route a genuine source-matched axiomatization or calculus and provide entry surfaces that distinguish \(\L_3\), each finite \(\L_n\), and infinite-valued \(\L\); state exact theoremhood and finite-premise consequence statuses and the McNaughton theorem at their proper domains. Only then remove the OPEN boundary. The adjacent t-norm/fuzzy survey obligation is substantively present and is not part of this finding.

## F9 — IMLL semantics omits the empty antecedent admitted by its calculus

Severity: **moderate / one semantic case underdefined**  
Status: **OPEN**

Evidence:

- `handbook/restoration/inherited-13972-14000.tex:24-28` interprets \(A_1,\ldots,A_n\Rightarrow B\) using the product of antecedent interpretations but neither permits \(n=0\) nor defines the empty product.
- `handbook/registry/calculi/imll.tex:1-10` explicitly permits empty antecedents and contains \(\Rightarrow\mathbf 1\).
- The adequacy statement in `handbook/restoration/inherited-14001-14015.tex:1-5` therefore quantifies over a calculus containing sequents for which the displayed semantic interpretation has not been defined.

Exact correction: state \(n\ge 0\) and define
\[
  \bigotimes_{i=1}^{0}\llbracket A_i\rrbracket=1,
\]
where \(1\) is the monoidal unit. Then the empty-context case and unit-right have a typed semantic interpretation.

## F10 — The IPL system card points to a larger first-order calculus than its fixed language

Severity: **moderate / system identity is not exact**  
Status: **OPEN**

Evidence:

- `handbook/parts/p08/intuitionistic-supplement.tex:20-40` fixes a propositional language but points at `sheet:lj` as its calculus at line 31.
- `handbook/registry/calculi/lj.tex:1-19` is full first-order LJ and includes \(\forall\)- and \(\exists\)-rules.

The cited sheet is sound for propositional instances, but the card claims a fixed language/calculus surface and presently identifies two nonidentical systems. Exact correction: say explicitly that the card uses the propositional fragment of the LJ sheet, with a precise restriction, or supply a separate propositional-LJ sheet and point the card to it.

## F11 — Three required exclusion-pointer rows have no source-specific pointer in the reader route

Severity: **moderate / registered pointer ceiling not met**  
Status: **OPEN**

Evidence:

- `handbook/parts/p08/relevance-linear-supplement.tex:683-691` says only that quantum logic, adaptive logics, and formal argumentation are outside scope and cites Girard.
- `spec/registers/new-content.csv:177-180` requires source-specific P-level pointers for quantum logic (Birkhoff-von Neumann 1936), adaptive logics (Batens 2007), and formal argumentation (Dung 1995). None of those pointers/citations occurs in a routed Part VIII unit.

Exact correction: add one ordinary, source-backed ceiling sentence for each excluded subject, with the named source and an exact statement of what the reader should consult it for. This needs no technical expansion of Part VIII, but a generic exclusion sentence with an unrelated citation does not discharge the three distinct pointer rows.

## F12 — Reader-visible OPEN and internal register prose contradicts the admission charter

Severity: **blocking for admission / unresolved control debt exposed to the reader**  
Status: **OPEN**

Evidence:

- Reader notes at `handbook/parts/p08/intuitionistic-supplement.tex:15-17`, `modal-logics-supplement.tex:16-19`, `temporal-epistemic-supplement.tex:16-18`, `many-valued-supplement.tex:16-18`, and `relevance-linear-supplement.tex:15-18` retain OPEN/owed editorial language.
- `handbook/annex/p08/many-valued-supplement.tex:13-16` exposes the same control state in the annex.
- `handbook/parts/p08/many-valued-supplement.tex:187-198` tells the reader that register rows remain “OPEN inclusion obligations,” and `:484-490` labels “OPEN annex targets.”

This is not merely a style complaint: F8 shows that at least one such notice truthfully marks a missing mandatory system, so deleting the word OPEN without completing the artifact would conceal a substantive obligation. Exact correction: first close or formally redispose every underlying register item, then replace internal register/OPEN/owed language with ordinary mathematical attribution and exact proof-status prose. The comment-only note at `handbook/parts/p08.tex:50-52` is not reader-visible and is not independently blocking.

## Checked-clean coverage

### Lot 1 — intuitionistic and intermediate logics

Checked: routed exact source, supplement, relevant LJ/calculus references, and treatment-ceiling rows. The IPL Kripke persistence argument and countermodels; Glivenko, Gödel-Gentzen, Kolmogorov, and Kuroda translation boundaries; Heyting-algebraic and topological semantics; the BHK/realizability boundary; expanding- versus constant-domain IQC; and the KC/LC intermediate-logics treatment are mathematically clean at their stated local ceilings. Residuals are F10 and the reader-visible notice component of F12.

Not checked: none within the lot's reader graph.

### Lot 2 — modal logics and quantified modality

Checked: every routed normal-modal sheet/card for K, KD, KT, KTB, K4, S4, KD45, S4.2, S4.3, S5, GL, and Grz; canonical-model and correspondence arguments; the Sahlqvist boundary; the IPL/S4 and GL-arithmetic interfaces; bisimulation/van Benthem and filtration statements; neighborhood systems E, EM, EC, EN, and EMC; and the Barcan/converse-Barcan direction and countermodel. These are clean at their stated statuses. The residual is F5's missing term/rigid-designator semantics, plus the modal reader notice in F12.

Not checked: none within the lot's reader graph.

### Lot 3 — temporal, dynamic, epistemic, hybrid, conditional, deontic, and free logics

Checked: LTL syntax/semantics/calculus and proof-status sketch; CTL and CTL* syntax/semantics, the Reynolds AA sheet, and stated complexity; the Kozen/Walukiewicz modal \(\mu\)-calculus systems, parity-game boundary, automata interface, and complexity status; Kamp tense logic; S5/KD45 epistemic semantics; everyone/common knowledge and noncompactness; muddy children; and PAL reductions/unsuccessful-update examples. The Reynolds CTL* rules match the source: Mark Reynolds, [“An Axiomatization of Full Computation Tree Logic”](https://doi.org/10.2307/2695091). Residuals are F1, F3, F5, F6, and F7.

Not checked: none within the lot's reader graph.

### Lot 4 — many-valued, fuzzy, relevance, linear, Lambek, paraconsistent, adaptive, and nonmonotonic logics

Checked: the finite-matrix generic tableau/proof pattern; K3, LP, and FDE plus the annex duality; weak Kleene, Bochvar, and Post systems; the displayed Łukasiewicz matrices and McNaughton statement; t-norm fuzzy semantics; supervaluation; matched E/R/RM relevance frames and calculus sheets; classical linear-logic rules, phase semantics, exponentials, cut status, and complexity; and Lambek L. The relevance entries were cross-checked against Dunn and Restall, [“Relevance Logic”](https://consequently.org/papers/rle.pdf); the phase-semantic conventions were checked against Girard's treatment in [*Proofs and Types* preview](https://api.pageplace.de/preview/DT0400.9780511893179_A23680408/preview-9780511893179_A23680408.pdf). Residuals are F2, F4, F7, F8, F9, F11, and F12.

Not checked: none within the lot's reader graph.

REJECT
