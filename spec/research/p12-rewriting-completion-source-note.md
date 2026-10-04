# Ordinary first-order rewriting: corrected critical pairs and complete host proofs

Date: 9 September 2026. Assignment: correct the ordinary critical-pair
criterion directly, supply all overlap cases, move Newman's proof into the
reciprocal annex, and complete the conditional completion-correctness chain.
This is authoring for the current handbook, not independent admission or a
claim that every source presentation in N-c-037 has been reconstructed.

## Delivered files

- `handbook/parts/p12/rewriting.tex`:
  `BB945E92F46C8C2BF2DA636C70D1B230E1F7F2861F0933FBCE28F888F82F9DC5`.
- `handbook/annex/p12/rewriting.tex`:
  `86D80AB84D6E0849145E4D593F418B950578C281C866D82E0B13A08E5F662E36`.
- `handbook/bib/intake-p12-rewriting-completion.bib`:
  `0CD096260AA9C9A4C849DA9C69979B444114272AA67D4AE84721B1CC7E63B6DE`.
- `handbook/registry/symbols-intake-p12-rewriting-completion.csv`:
  `64BEC4FCAD34BA9BC67A0663D0B56D54F96A577A7366E2DC9B00D2B53AC4B9FC`.

The existing body labels are retained. Seven body results now point to seven
complete ordinary proofs in new reciprocal `annexitem` wrappers. The lead
must route the new annex and merge the one bibliography key and eleven
symbol rows. This writer did not change a shared driver, existing calculus
sheet, canonical bibliography or canonical symbol registry.

## Exact source acquired and read

Salvador Lucas, *Local Confluence of Conditional and Generalized Term
Rewriting Systems*, Journal of Logical and Algebraic Methods in Programming
136 (2024), article 100926. DOI
[10.1016/j.jlamp.2023.100926](https://doi.org/10.1016/j.jlamp.2023.100926).
The actual title page identifies the 2024 volume and says available online
31 October 2023. It is a 23-page version-of-record PDF, 974,021 bytes.

The exact open university repository object was downloaded from
[the Universitat Politècnica de València repository](https://riunet.upv.es/server/api/core/bitstreams/4342f2a0-785b-4622-8bde-bf9df6d7a4a9/content)
to `tmp/pdfs/p12-rewriting-completion/lucas-2024-local-confluence.pdf`.
SHA-256:
`F69FA5CB94F0FBA021DA314BB50974B06E63ABB2D63F98816E4D0FA904C1EFBA`.
The DOI landing-page fetch returned 403; the ordinary open repository
download succeeded. No access restriction was bypassed.

The writer read the title/abstract and complete physical pages 1-4 directly
from the acquired PDF. Page 2 explicitly attributes the ordinary-TRS
equivalence between local confluence and joinability of all critical pairs
to Huet 1980, Lemma 3.1, and Baader-Nipkow Theorem 6.2.4. It defines the
nonvariable overlap and MGU construction. Pages 3-4 state the term,
position, substitution, context and TRS conventions; a TRS is the
unconditional type-1 case, with no extra right-hand variables. The opening
examples distinguish conditional semantics, explaining why their additional
variable-pair obligations cannot be transferred to ordinary rewriting.

The remaining pages develop the paper's separate conditional/generalized
theorems and were not read in this bounded source pass. Their full
reconstruction is not claimed. No original Huet 1980 body was acquired or
read in this task; the lead had already reported an unsuccessful ACM
fetch. The original Huet presentation remains a distinct source obligation.
The new host proof is independently written and complete at the stated
ordinary-TRS scope, with the source attribution corroborated by Lucas.

## Direct mathematical corrections

The old body unnecessarily required left-linearity for the ordinary
critical-pair criterion and suggested that nonlinear systems require a
stronger criterion. The active theorem now states the exact unrestricted
ordinary result. Its proof includes:

1. Disjoint redex occurrences commute.
2. Nonvariable nesting is an instance of a critical pair through an MGU and
   its residual substitution. The selected MGU fixes other rule variables,
   preventing unintended identifications outside the unified subterms.
3. For nesting inside a substituted variable, reduce every remaining copy
   in the left-hand pattern to restore the root match, perform that root
   step, and reduce every copy on the right-hand side to the same instance.
4. Repeated left variables, duplicated right variables, erased variables,
   empty residual reductions, root overlaps and self-overlaps are explicit.

The unrelated `Huet1973` citation was removed from the critical-pair
definition. That key denotes third-order unification undecidability; it is
not a rewriting-source citation. Correction provenance stays in this note.

The critical-pair proof imports the exact *existence and factorization*
part of first-order syntactic MGU theory through
`thm:p12-unification-mgu`. It does not rely on a uniqueness assertion about
arbitrary residual substitutions. The broader unification/source-proof
obligation remains with its assigned treatment.

## Complete proof and example content

Newman's former prose proof was replaced by a `proved=` status pointing to
the new annex. Its proof identifies both first reducts, their local join,
the two tail joins, and the final induction at that local join. Empty
reductions and the strict-descendant condition are stated. The chapter
clarifies the well-founded form of termination used by this induction and
its usual classical-with-Choice equivalence to absence of infinite chains;
strategy termination is not substituted for full termination.

The context/substitution lemma proves closure step by step and supplies
the structural induction that changes every occurrence of one substituted
variable. The normal-form lemma proves termination from a reduction
ordering, existence, uniqueness and the conversion equivalence.

The completion invariant proves both inclusions of the generated
equational relation for Orient, Simplify, Compose, Collapse and Deduce.
Compose and Collapse explicitly use retained rules, excluding the rule
being replaced or removed. The final correctness theorem then uses the
empty equation set, the preserved theory, the final reduction ordering and
joinability of every final critical pair. These final conditions suffice
without an unused scheduling hypothesis; successful fair runs remain
included. No theorem that fairness forces termination was introduced.

The worked completion starts with `a ≈ c` and `f(a) ≈ b`. The nonjoinable
critical pair `(b,f(c))` requires a new equation, oriented as `f(c) → b`.
The proof enumerates all final critical pairs and gives an actual reduction
ordering using natural-number interpretation `a=2`, `c=1`, `b=0`,
`f(n)=n+1`. Universal comparison under variable assignments is proved
well-founded, context-compatible and substitution-stable. Explicit normal
forms prove both positive equalities and the negative word-problem example
`f(b)` versus `b`. The nonlinear/copying and erasing examples are also
calculated directly in the body.

## Author checks and remaining scope

The complete edited body and complete new annex were read sequentially.
The definition of reflexive-transitive closure was moved before its first
use, and the MGU variable condition was made explicit during this author
read-through. Exact proof/status declarations were inspected, the unrelated
Huet citation is absent, and no ordinary proof environment remains in the
new editorial body. The worked reductions, critical-pair enumeration and
natural-number inequalities were checked as mathematical calculations.
No new software tests, independent reviews, manuscript builds or renders
were run.

All seven proofs in this bounded host correction are supplied. The chapter
still has separately mapped work: complete source-specific LPO/KBO
definitions and metatheory, the full original Newman/Knuth-Bendix/Huet/
Dershowitz/Baader-Nipkow presentations, and the full scheduling analysis of
completion. In particular, the existing sheet's additional Collapse
eligibility language is not proved to be a complete scheduling strategy by
this batch. The invariant proof covers every eligible retained-rule step
without depending on that extra restriction. No change to the shared sheet
was made, and this note does not mark N-c-037 as wholly complete.

The research and PDF skills guided primary-source reading and this evidence
record. The acquired PDF was only a historical/technical source; it was not
the manuscript output.
