# P16.17 — Consistency-based diagnosis

## Completed writing and exact scope

The treatment supplies Reiter's finite-component diagnosis semantics,
the complete conflict and minimal-hitting-set characterization,
single-fault results, corrected shared-node search, both circuit
examples, measurement updates, the default correspondence and the
generalized set-cover representation. Fourteen reciprocal formal
statement/proof pairs are saved and routed.

The underlying semantic language is bivalent with classical Boolean
connectives, as in the source's Section 6.1 generalization. Component
names are finite; the background theory need not be finite.
The default correspondence is explicitly classical first-order.
Computational claims require a total consistency/conflict oracle;
the finite propositional oracle is supplied in full.

Files:

- handbook/parts/p16/consistency-based-diagnosis.tex
- handbook/annex/p16/consistency-based-diagnosis.tex
- spec/research/edition-2026-p16-consistency-based-diagnosis.md

Final body: 23,650 bytes, SHA-256
6CE6AD5B15F681C952DAFE1DFC1641C3CEB3D69C500422DD0A01E95B6C1748BD.

Final annex: 31,511 bytes, SHA-256
D610898F11751F63457E6BEEABBB835CD8C60D79F5FC75C358DE171530146438.

Chapter label: sec:p16-consistency-based-diagnosis.
Annex label: sec:annex-p16-consistency-based-diagnosis.
Shared body/annex drivers include the treatment. The earlier
finite-abduction boundary now links to it.

## Acquired and read primary sources

### Reiter 1987 journal original

Raymond Reiter, A Theory of Diagnosis from First Principles,
Artificial Intelligence 32(1), 57–95 (1987).
DOI: 10.1016/0004-3702(87)90062-2.
The original states received March 1986 and revised June 1986;
those are not substituted for the 1987 publication date.

Public academic copy:
https://www.cs.ru.nl/~peterl/teaching/KeR/reiter.pdf

Held file:
source/references/reiter-diagnosis-1987/reiter-diagnosis-1987.pdf

Size: 1,751,213 bytes. SHA-256:
9290CB0B84B1CCF8B7E030B585B9C08A62E3FC34B750225C7B8BDA77B1008556.

The complete 39-page original, printed pp. 57–95, was read.
Physical page equals printed page minus 56 throughout this file.
Text extraction was read for all sections, continued proofs,
examples and references. The portions lost from combined tool
output were read in smaller source-page calls before authoring.

Original images for physical pp. 4, 14, 17, 21, 22, 23, 24 and
27 were personally read. These cover the original Boolean
circuit, the large original search trees, both full-adder search
examples, the multiplier wiring and both corresponding search
trees, and the measurement-page component-name discrepancy.
Images are retained in tmp/pdfs/p16-diagnosis-source/.

Canonical bibliography key: Reiter1987Diagnosis.

### Greiner–Smith–Wilkerson author copy

Russell Greiner, Barbara A. Smith and Ralph W. Wilkerson,
A Correction to the Algorithm in Reiter's Theory of Diagnosis.
The journal publication is Artificial Intelligence 41(1), 79–88,
November 1989, DOI 10.1016/0004-3702(89)90079-9.
Publication identity and month are supported by the author's
own publications page and the publisher's record.

Author's publication page:
https://webdocs.cs.ualberta.ca/~rgreiner/other.html

Author-hosted full copy:
https://webdocs.cs.ualberta.ca/~rgreiner/PAPERS/correct.pdf

Held file:
source/references/greiner-smith-wilkerson-diagnosis-1989/greiner-smith-wilkerson-1989-author.pdf

Size: 155,121 bytes; five physical pages. SHA-256:
16D2FACF4E93E03FDD5C5BB4D620275CE16842BD59BA9CF840F80578C59CB50E.

This is an author-hosted five-page typeset version, not a held
ten-page journal scan. It ends with received July 1988 and revised
January 1989. It has no separately asserted version date.
Canonical bibliography key: GreinerSmithWilkerson1989Correction;
the bibliography note distinguishes its pagination.

Its font encoding produces unusable extracted characters. All
five actual pages were personally read as source images, including
all four diagrams, both algorithm definitions, all pruning rules,
Theorem 2, Lemma 1 with its continued final paragraph, footnotes,
acknowledgments and references. These images are source reading
only; no manuscript PDF was rendered.

The earlier CiteSeerX download lead redirected to an unavailable
Wayback capture. It produced no held correction PDF. The author
copy was then acquired successfully. A Linkoping academic mirror
was found as a separate lead but was not needed for the reading.
The exact paginated journal scan is not claimed acquired.

## Reciprocal inventory and source mapping

Every suffix below has body label thm:p16-SUFFIX and annex label
annex:p16.SUFFIX.

| Suffix | Supplied content and source extent |
| --- | --- |
| diag-semantics | Definitions 2.1–2.4 and Propositions 3.1–3.4, including full model proof, arbitrary abnormality interactions, empty/inconsistent input and the single-deletion criterion. |
| diag-conflicts | Definitions 4.1/4.3, Proposition 4.2, Theorem 4.4 and Corollary 4.5, with private witnesses and the explicitly additional full finite double-transversal identity. |
| diag-singletons | Corollary 4.10 and Theorems 4.11–4.12, with the necessary nonempty-conflict-family condition. |
| diag-hs-tree | Definition 4.6 and both original unpruned-tree claims, completely proved for arbitrary finite conflict families and choices. |
| diag-hs-dag | The corrected shared-node, closing and relabeling construction; full correctness and termination under the Greiner–Smith–Wilkerson graph route. |
| diag-oracle | Reiter Section 4.3's implicit conflict procedure, with retained-cache invariant, no repeated/superset returns, bounded-cardinality output and a complete finite propositional oracle. |
| diag-pruning-calculations | All six answers in original Example 4.7, private witnesses for each, and both correction-paper counterexamples with the surviving shared paths and correct labels. |
| diag-circuits | Complete Boolean full adder and integer multiplier-adder examples, all minimal conflicts, every diagnosis, explicit witness assignments and the exact total Boolean conflict count. |
| diag-measurements | Definition 5.1, Propositions 5.3–5.5, Theorem 5.7 and Corollaries 5.8–5.9, plus a directly proved extension beyond the source's decide-every-measurement assumption. |
| diag-measurement-calculations | Examples 5.2, 5.6 and 5.10, all updated conflict families, predictions and complete new diagnosis families. |
| diag-defaults | Theorem 6.1 and its prerequisite-free normal-default premise, including maximal consistent subsets, inverse and the missing inconsistent-background exception. |
| diag-set-cover | Section 7.1 and Theorem 7.1, both Boolean and named first-order constructions, empty cases and the exact inclusion/cardinality distinction. |
| diag-abduction-boundaries | Explicit complete examples separating observation consistency from observation entailment and exact from withdrawal assignments. |
| diag-probability-boundary | The correct independent-fault prior calculation, a counterexample to ranking incomparable assignments by size, and the additional likelihood premise for posterior ranking. |

## Corrected search and its proof

The manuscript includes the basic original tree route and the
corrected graph route separately. All edge labels add a component
not yet in the path set. Shared nodes are identified by the entire
path set; every incoming edge is preserved.

When a smaller conflict replaces a larger label, every node with
that label is updated, and exactly the edges outside the new label
are removed. Nodes reachable through another parent remain. The
explicit-family presentation deletes the now redundant larger
conflict; the correction also describes placing the subset ahead
of its superset in the ordered list. These preserve the same
disjoint-conflict existence test. No identity of graph shapes is
asserted.

The proof establishes a local graph invariant: every expanded
node has its valid disjoint conflict and every required successor;
every success has a certificate of hitting the full target family;
every closed node has a successful proper-subset witness.
Pruning preserves that invariant. Following an arbitrary target
minimal hitting set from the root proves completeness. At the
moment a larger nonminimal success could be reported, breadth-first
processing already supplies its smaller minimal hitting set,
forcing closure instead. This proves minimality and output order.

Termination is proved separately from correctness. The explicit
family admits finitely many strict redundancy deletions, and
between them at most one active state per subset is created.
For the implicit oracle, every old conflict retains a subset in
the cache. This prevents a new oracle call from returning the
same conflict or a superset of any earlier returned conflict.
Finitely many returns therefore bound the pruning events.

The graph has at most 2^n active nodes and n 2^n active edges.
This is an active-storage bound, not a claim that all runtime,
oracle cost or recreated-node counts equal 2^n. The theorem does
not infer a terminating first-order consistency procedure from
refutation completeness.

## Corrections incorporated in the actual LaTeX

- Reiter's original Theorem 4.8 is not asserted with the faulty
  combined closing/deletion rules. The actual procedure uses the
  corrected shared-node and relabeling rules, with their full proof.
- The correction's two examples both appear. The first retains
  {a,b} through the alternate parent after deleting the root's
  a-branch. The second updates the root's label before comparing
  it with the incomparable singleton conflict.
- Reiter p. 78 says the full adder has twelve possible conflict
  sets. The two established minimal conflicts generate ten:
  2^3 + 2^2 - 2 = 10. The actual manuscript gives ten and proves
  both the conflict characterization and the count.
- Reiter p. 83's introductory list in Example 5.6 names {A2,M3};
  the correct diagnosis is {M2,A2}, as the equations and the
  subsequent prediction row require. The manuscript consistently
  uses {M2,A2} and provides its witness assignment.
- The source's statement about intersecting all conflicts needs
  a nonempty conflict family. With no conflict the sole diagnosis
  is the empty set. This case is handled explicitly.
- The default correspondence needs a consistent background.
  If the background is inconsistent, Reiter's operator has the
  one inconsistent extension while there are no diagnoses.
  The actual theorem states and proves both cases.
- The source's interpretation of unchanged diagnosis families
  as no new information is too strong. A fresh measured atom
  can add predictions without changing the sole diagnosis.
  The manuscript gives the exact invariant-family theorem and
  a complete counterexample to the broader reading.
- Independence alone does not make every single-fault assignment
  more probable than every multiple-fault assignment. The exact
  product-of-odds formula, numerical counterexample, common-p
  special case and posterior likelihood factor are supplied.
- The all-faulty exact assignment need not be consistent merely
  because the background is. Only the full withdrawal set has
  that automatic consistency property. The model proof retains
  arbitrary logical interactions between fault indicators.
- The set-cover construction keeps inclusion minimality distinct
  from minimum cardinality, states empty disjunctions, and gives
  a nonempty first-order domain even when all named sets are empty.

The measurement proof is stronger than the source's stated
Theorem 5.7, with its additional reasoning shown explicitly:
an old diagnosis survives precisely when it does not predict
the negation of the measurement. Every old diagnosis contained
in a genuinely new diagnosis must therefore predict that negation.
The source's special case where every diagnosis decides the
measurement follows without replacing its circuit presentation.

## Notation and integration

- C, c, a_c, S, O, W, Normal(N), W^-_Delta, W^=_Delta,
  D(W), A(M): component universe, designated abnormality sentences,
  system/observations, withdrawal/exact theories, diagnosis family
  and a structure's exact abnormality set.
- K(W), K_min(W), F, G, H, Tr(F), K_c: conflict families,
  hitting sets, minimal transversals and private witnesses.
- H, J, K, K', K*, n, q, k, v: graph identities, success witnesses,
  old/new/cached conflicts, universe size, initial conflict count,
  search depth cutoff and common propositional atom count.
- X1, X2, A1, A2, O1 and x,u,v,y,z: Boolean circuit components
  and fully specified Boolean wire values.
- M1, M2, M3, A1, A2 and x1,x2,x3: multiplier network components
  and integer wire values. Its variables are locally distinct
  from the first circuit's variables.
- pi, W', D': measured sentence, updated theory and a new diagnosis.
- T_W, Th, Gamma, E, alpha_i, A_E: normality default theory,
  closure, Reiter operator, extension and licensed consequents.
- D, M, R, M+, R_m, p_d, o_m and the four named first-order
  predicates: covering input and its logical representations.
- p_c, P(Delta), E: independent fault prior, exact fault event
  probability and a separately declared positive-probability
  observed event for Bayesian updating.

Shared bibliography contains both new keys. Canonical notation
and the progress record are updated in the same authoring batch.
The earlier finite-abduction chapter links the diagnosis result
and the explicit entailment/consistency distinction.

## Authoring completion and retained obligations

The complete saved body and annex were personally read once.
Final changes state the oracle's complete atom universe, make
background-relative entailment explicit, separate the probabilistic
data event from the logical observation set, and complete every
private-witness and first-order model assignment. Final hashes
above were then read from the actual files.

The research and PDF skills guided acquisition, source identity
and reading. The PDF skill was used solely to read primaries,
including the correction whose text encoding is unusable.
No independent review, scanner, test, build, manuscript render
or admission procedure was run.

The exact paginated correction journal scan remains distinct from
the fully read author copy. Reiter's reference to Ginsberg's
protected-premise counterfactual correspondence does not itself
supply Ginsberg's formal semantics; that original source remains
a separate treatment. The original de Kleer–Williams probabilistic
diagnosis, Reggia–Nau–Wang versions, richer fault-mode and
first-order abduction accounts are not claimed completed here.
These local source/subject continuations do not reduce the full
approved manuscript scope.
