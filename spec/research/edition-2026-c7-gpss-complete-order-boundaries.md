# C7 author handoff: GPSS complete-order boundary constructions

## Governing integration correction

The ten local results below are connected to the manuscript. The earlier
description of an arbitrary-complete-order U-only future theorem as merely
unfinished was an incorrect inference from GPSS. Its p. 171 announcement
concerns adapting the argument for Kamp's S/U theorem. The body introduction
and concluding boundary now state the actual local scope and remove that
promise. The active author's next primary-source assignment supplies the
separate nonexpressibility result and the correct future-logic basis.
The original author-return description below records how the mistaken
continuation target arose; it no longer governs the work.

The integrated body after this correction has SHA-256
331EB9A122F8CB16219ED0A7754009E6651546BDF755978E8B365A6BAC61AA09.
The ten statement/proof pairs themselves retain the reported mathematical
content; the changed introduction and concluding boundary remove the
unsupported continuation promise.

8 September 2026. Author /root/kamp_lemma7_author, dispatched 13:54 UTC.
Ten results and their full proofs are written. The arbitrary complete-order
future-completeness theorem remains unfinished at the final-gap/upper-boundary
step below. Consolidated reviews remain deferred under the current contract.

## Owned files and exact reading

- handbook/parts/p09/presentations/gpss-complete-order-boundaries.tex
- handbook/annex/p09/gpss-complete-order-boundaries.tex
- This note.

All three paths were absent before authoring. Exact-path write permission was
granted. Only these files were written with apply_patch; root owns shared
integration. The full saved body and annex were read as one authoring batch,
including the later positive-chain addition and worked cases.

Personally read the complete GPSS primary passage on printed pp. 169–171:
complete/discrete models, future quantifier scope, Theorems 2.1–2.3, special
and decomposition definitions, the entire Proposition 2.4 outline, and the
complete-order/gap announcements. Held primary:
tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf.
SHA256: 2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2.
The 11-page object is the author-archive
[Sh:134 paper](https://shelah.logic.at/files/95957/134.pdf);
PDF page equals printed page minus 162.

The research and PDF skills supplied primary reading and this note. All four
agent slots were occupied, so the needed reading and authoring were done
locally. There were no reviews, review waits, scanners, tests, builds or
manuscript renders. Hashes identify artifacts and do not establish acceptance.
No external SS/G2 manuscript was acquired or claimed as acquired.

## Ten completed proof pairs

| Body label | Reciprocal annex |
| --- | --- |
| thm:p09-gpss-complete-order-bridge | annex:p9.gpss.complete.order.bridge |
| thm:p09-gpss-right-limit | annex:p9.gpss.right.limit |
| thm:p09-gpss-future-word-limit | annex:p9.gpss.future.word.limit |
| thm:p09-gpss-fixed-start-limit | annex:p9.gpss.fixed.start.limit |
| thm:p09-gpss-left-labelled-closure | annex:p9.gpss.left.labelled.closure |
| thm:p09-gpss-infimum-descriptors | annex:p9.gpss.infimum.descriptors |
| thm:p09-gpss-infimum-case-compiler | annex:p9.gpss.infimum.case.compiler |
| thm:p09-gpss-complete-positive-chain | annex:p9.gpss.complete.positive.chain |
| thm:p09-gpss-complete-bounded-obstruction | annex:p9.gpss.complete.bounded.obstruction |
| thm:p09-gpss-initial-gap-complement | annex:p9.gpss.initial.gap.complement |

The Com bridge derives the one-sided clauses from two-sided bounded-set
completeness by cutting a set at one member. The temporal bridge explicitly
maps Kamp U(witness, interval) to GPSS interval U_s witness; it does not
convert arbitrary Kamp elementary labels into future labels.

The nonvacuous right limit is K+ A = F true AND NOT ((NOT A) U_s true).
All last-point, immediate-successor and current-atom distinctions are proved.
For a word W, E+_W is its nested future formula starting at the current point.
The future-only word-limit recursion is Gamma_(A) = K+ A and
Gamma_W = K+(E+_W) AND Gamma_(suffix W).
A bounded suffix and an earlier globally viable start are spliced at the
first crossing index, including equality and both extreme indices.
The exact vacuous Kamp Lf condition is NOT F true OR Gamma_W.
Fixed-start accumulation additionally retains A0 and a real B1 neighborhood.
This new splice avoids the S occurring inside Kamp's displayed future-limit
recurrence; that mixed recurrence is not imported as though it were L(U).

The intermediate grammar is explicitly enlarged to alpha(x) AND D(x,y),
where x is actual and alpha remains future-only. Positive conjunction,
concatenation and complete future-ray complements are proved. At a midpoint
z, the right operand's left label joins its point label. Cofinal clauses
retain F psi AND GF psi, including last-point behavior.

Infimum events have empty, initial, attained-interior and unattained-interior
statuses. The initial infimum is the excluded lower endpoint and has no
occurrence-membership test there. An unattained interior infimum uses
NOT A AND K+ A at the boundary and absence before it. All four unbounded
future statuses also have explicit L(U) formulas. The finite event compiler
handles undefined bounds, every weak order and equality, fuses equal points,
transfers universal labels onto every covered gap and inserted point, and
gathers lower-endpoint labels into alpha. No event or extra parameter remains.

For a positive chain with m points and no final gap, the new determining
recursion selects the infimum c of its globally future-viable first-point
label, checks its initial gap before c, and recurses on m-1 points with a
true initial gap. Nonattained c requires a real right neighborhood; only an
interior c additionally requires the gap label at c. The bounded suffix and
provisional global chain are joined by a complete splice. At most 4m nonroot
event nodes are needed. Point-list length decreases even when c returns the
same lower endpoint. Its relative complement follows from the event compiler.

## The necessary grammar change and direct correction

The original endpoint-free bounded class fails complement closure on the
complete order {0,2} union {1/n:n>=1}, with actual endpoints 0 and 2.
Every interior point has a finite future. Vary q0(1/n) independently and fix
the other interpretation. Every fixed decomposition witness tuple gives a
closed set of binary interpretations; countably many tuples and finitely
many disjuncts give a countable union of closed sets.

The legal initial-gap word exists z in (0,2) forall u in (0,z) q0(u)
holds exactly when the bit sequence has finitely many zeros. Its complement
has infinitely many zeros and is proved not to be a countable union of closed
sets by an explicit nested-cylinder diagonal argument. This is an actual
bounded-endpoint obstruction, distinct from the earlier formal-left-endpoint
result. It does not refute future expressibility at the initial point.

The corrected initial-gap complement is fully written:
Adj(x,y) OR K+(NOT A)(x), under x<y.
Its two explicit left-labelled decompositions supply the needed endpoint
condition directly. GPSS p. 171 announces a modification for complete orders;
it does not state that its intermediate grammar is unchanged. The new
grammar and formulas are independently derived components of that task,
not the literal text of an acquired SS/G2 proof.

## Exact continuation boundary

The next input is a general bounded word with final gap Phi_m. The completed
event recursion treats all points and preceding gaps, but not Phi_m after the
last point. With no final-gap failures the positive-chain test suffices.
Otherwise the relevant upper boundary is the supremum of the failures.

Construct the full finite future-only treatment of this final gap: an
unattained supremum at y, an attained interior supremum, and an unattained
interior supremum. Preserve cut point labels and shorter-prefix obligations.
Return the actual construction to the declared enlarged class, or prove
another explicit bounded complement construction. Status enumeration alone
does not close this step. Then complete regional negation and the full
complete-order future translation.

An unattained upper boundary requires actual occurrences arbitrarily close
below it, including a nonempty witness. This cannot simply become a
future-only unary label at that boundary: the real-order interpretations
A=(-1,0) and A=empty agree at and after zero and disagree on left accumulation.
Kamp's remote-boundary construction uses past-limit labels, so its Com result
requires another proved transformation before it can discharge this task.
The source's separate 2.3 and general-gap 2.5 obligations retain their status.

## Root integration, actual host reading and notation

Add this body/annex pair after gpss-decomposition-complement. No bibliography
entry or macro is needed. Keep the discrete theorems unchanged; link this
unit at the final boundary of thm:p09-gpss-discrete-future-completeness.
In n-c-012.tex, the paragraph near “the promised modifications for arbitrary
complete orders” can now link these completed components while retaining
the final-gap boundary. Do not describe the original bounded complement
as Com-wide.

Personally read the needed actual model/operator clauses in n-c-012.tex,
the full basic-word body, the full limiting-word body and annex, and the
boundary/completion bodies. Key host snapshots:

- kamp-iii2-lemma1.tex body:
  3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6.
- kamp-iii2-lemma2.tex body:
  49C59D4BDF9169590457F73F3841B35E9620F6C4A54083044DAD625598823677.
- kamp-iii2-lemma2.tex annex:
  75BAE1D38B195849018E8F573741A7F04B8F0984C6804FECFF770D00602FA4F2.
- kamp-iii2-lemma8-completion.tex body:
  22D58367E4A6C31471D59825476ECA6BB18EACDC1D5DAA8210E1619565D1C9DD.

Local notation: N+, partial+, K+, E+_W, Gamma_W, suffix W-, left label alpha,
Inf_A(s,t), its three defined statuses, Test_A(s), V_(Theta;Phi), c/h/j/k
and R in its length recursion, D_A and Adj, and FIN/INF with cylinders.
Current points, endpoint values and event statuses are explicitly typed.
These ten authored proof pairs do not grant independent acceptance.
