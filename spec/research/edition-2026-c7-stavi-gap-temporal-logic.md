# C7 author handoff: Stavi operators and positive partition constructions

8 September 2026. Author /root/kamp_lemma7_author; block began 15:38 UTC.
Nine closed results are written. The full arbitrary-order completeness
target remains open at canonical partition negation; no outline is counted
as completing that target.

## Owned files and acquired primary

- handbook/parts/p09/presentations/stavi-gap-temporal-logic.tex
- handbook/annex/p09/stavi-gap-temporal-logic.tex
- This note.

All three paths were unused before authoring. Only these and the authorized
new primary capture/reading derivatives were written. Shared files and
previous authors' work were preserved.

Primary: Alexander Rabinovich, A Proof of Stavi's Theorem, Logical Methods
in Computer Science 14(1:20), 2018, pp. 1–18, published 6 March 2018.
DOI: 10.23638/LMCS-14(1:20)2018.
Exact version: arXiv 1711.03876v2, revised 5 March 2018.
Direct download: https://arxiv.org/pdf/1711.03876v2.
The author publication list also identifies the paper:
https://www.cs.tau.ac.il/~rabinoa/journal1.html.

Unchanged primary:
source/references/rabinovich-stavi-2018/1711.03876v2.pdf.
SHA256: A8A1D4A6D0F8D76E3F358C87CFE7336A7B9F3DC19900BDBCD708114F4B9F8AC6.
Reading text and source-page images are under
tmp/pdfs/p09-rabinovich-stavi-2018.

Personally read the entire eighteen-page paper: cuts and operator definitions,
all partition constructions, the bounded sampling/plain-chain proof, the
complete negation cases, and the closing comparisons and references.
Definition/recurrence pages 4, 5 and 7 were also inspected as source images.
The research/PDF skills supplied acquisition and reading. The whole saved
body and annex received the author mathematical read-back. There were no
reviews, scanners, tests, manuscript builds or manuscript renders.

## Nine complete proof pairs

| Result | Annex |
| --- | --- |
| thm:p09-stavi-gap-cuts | annex:p9.stavi.gap.cuts |
| thm:p09-stavi-definable-gap | annex:p9.stavi.definable.gap |
| thm:p09-stavi-first-order-clauses | annex:p9.stavi.first.order.clauses |
| thm:p09-stavi-two-block | annex:p9.stavi.two.block |
| thm:p09-stavi-partition-prefix-rays | annex:p9.stavi.partition.prefix.rays |
| thm:p09-stavi-positive-partitions | annex:p9.stavi.positive.partitions |
| thm:p09-stavi-basic-partition-translations | annex:p9.stavi.basic.partition.translations |
| thm:p09-stavi-common-gap | annex:p9.stavi.common.gap |
| thm:p09-stavi-gap-partition | annex:p9.stavi.gap.partition |

The cut theorem proves both definitions of proper gap and equivalence
between absence of gaps and Dedekind completeness. Gamma-plus constructs
the unique initial-run gap, with all four first-order conjuncts, the
missing-extremum arguments, coinitial failures and its full past dual.

The binary Stavi clauses are U_gap/S_gap. U_s/S_s remain ordinary strict
operators. Both first-order truth tables are displayed and proved, including
the open stretch beyond the gap and its untested endpoint. No operand is
evaluated at a gap. The temporal-language-to-first-order direction is complete.
The dense rational example and discrete incomplete Z+Z example distinguish
proper gaps from local neighbor properties.

The two-cell U_* formula includes every attained boundary ownership and
proper-gap case. The finite-prefix recurrence proves all four adjacent
singleton-flag cases in both directions, including truth throughout
realizing cells. Its ray seeds handle both an unrestricted final cell and
a forced singleton final point; the past versions reverse labels and flags.

Positive closure is fully constructive: nonempty intersections form monotone
paths; flagged rows/columns occur only once and their intersections are
singletons. Named points are anchored with all optional side pieces.
Weak order types retain equality cases. Quantifier elimination glues
endpoint singletons at the same quantified point and preserves distinct
forced cells for surviving endpoints, retaining their strict inequalities.

Basic partitions have first-order definitions. For a bounded interval,
relativize the ray formula while input labels are still unary names, then
inline their whole-model definitions. The order avoids restricting hidden
label quantifiers. Open/half-open forms use forced singleton padding.
One-variable simple formulas return to temporal logic; whole-order
partitions choose an actual point of the first cell and use A OR F A OR P A.

UG(D,E) identifies equality of the D-gap and the D-and-E-gap, proving
the condition E throughout (t,g), with no E(t) test.
OG and CG give complete partitions on (t,g) and [t,g), respectively.
They include the actual last-cell label, forbid a singleton last cell
at a proper gap, and use a separate initial true singleton so D(t)
is not imposed. CG explicitly tests its own E_1(t) and handles both
a singleton and a non-singleton first cell. Both order-dual versions
and every flag transformation are proved.

## Corrections and exact next construction

The positive formulas directly correct the source's compact Lemma 5.5
recipe: a last flagged cell cannot reach a proper gap; UG(D,E_k) alone
does not assert E_k at its current point; and a succeeding D-gap does
not require D(t). The whole-order return also restricts its one-cell
past flag set to O intersect {1}.

Still required: Proposition 5.4 (plain labelled-point-chain complement),
Lemma 5.6 and Corollary 5.7 (bounded sampling and prefix-complement
interfaces), Proposition 5.3 (open partition complement), Lemma 5.2
and the final first-order induction. These are not claimed proved.

The next author block must retain these concrete repairs:

1. Process forced first/last singleton cells before a uniform endpoint-cell
   extension. On R, Part(true,true; first cell singleton) on (0,1) is
   false, whereas the corresponding partition on [z,1) exists for
   every 0<z<1. Source Case 1 therefore cannot be applied unchanged
   when 1 is flagged. A first forced cell requires the immediate
   successor s of a inside (a,b), its label at s, and the shorter
   partition on (s,b). Include missing-successor/adjacency and the dual.

2. The p. 17 equal-gap detector must use the final boundary label delta_N,
   not an unrelated delta_2 when N>=3. With delta_2=true, the printed
   detector can hold even when the two boundary gaps coincide.
   The corrected candidate is delta_1 U_s
   (delta_1 AND UG(delta_1,delta_N)); its full proof remains in that block.

3. At a common proper gap enumerate between-cell splits and within-cell
   splits. A crossing cell in the latter must be unflagged. The proved
   OG/CG formulas now supply the actual endpoint conditions for the
   pieces. Do not insert a domain point at the missing cut.

The plain-chain recursion must retain the complete remaining label list
when deleting its first or last member. The bounded sampling lemma needs
the full four-case proof, including the labels on truncated cells.

## Integration and source identity

New bibliography key: Rabinovich2018Stavi, using the metadata above.
Route this pair as a distinct later Stavi presentation near GPSS Theorem 2.5.
The 1980 U'/S' symbols remain historically undeclared; this is an explicit
later realization of the full gap basis, not a literal decoding of the
missing 1980 definitions. Keep the reverse-completeness boundary in
def:p09-stavi-completeness-continuation until the negation proof is written.

The new primary identifies Gabbay–Hodkinson–Reynolds, Temporal expressive
completeness in the presence of gaps, Logic Colloquium '90, LNL 2, 1993,
pp. 89–121, and the 1994 book's Chapters 11–12 as other published proofs.
Their bodies are not claimed acquired by this distinct 2018 capture.

Local notation: proper-gap L/R and point-gap intervals, gamma-plus/minus,
Gamma_P and Run_P, U_gap/S_gap versus strict U_s/S_s, the full four-operator
language, Part and O, U_*, F_i, UG, OG_D and CG_D. No shared macro or
notation file was changed. These nine authored proof pairs await the
deferred consolidated independent reviews.
