# Edition 2026: independent source fidelity review of C3, C4 and C5

Date: 7 September 2026. Reviewer role: independent source fidelity reviewer.
Reviewer context: `/root/edition_small_source_review`. Actual model identifier
and reasoning configuration were not exposed to this reviewer and are recorded
as unavailable.

## Verdict and authority

| Bounded correction | Verdict | Basis |
| --- | --- | --- |
| C3 / INV-CTL-001 / A-146 root valuation | PASS | The explicit negative root valuation makes all four displayed truth values follow from the current CTL semantics. The single changed label is identifiable. |
| C4 / R-032 expanded-signature PA2 definition | PASS | The seven conjuncts assemble the source's successor, induction and arithmetic recursion axioms in the signature required by the active reduction, with full semantics stated before use. |
| C5 / R-030 DLO extension cases | PASS | The theorem's active proof now gives all four cases, freshness and order preservation, the inverse extension, and the union argument while retaining the surrounding source content. |
| C4 / S-013 analytic derivation | PASS | The definition immediately follows the chapter title, states the source's propositional and first-order distinction, and preserves the surrounding source and proof boundaries. |

These are source fidelity verdicts for the four assigned corrections. They are
not admission of whole requirements, the surrounding chapters, an external
source presentation, or the edition. No FAIL or UNRESOLVED finding was found
within these four bounded source fidelity scopes.

The governing authority is `spec/EDITION-2026-CONTRACT.md`, read in full.
Its lines 53-60 authorize direct correction in active restoration files while
preserving the frozen source archive and keeping correction provenance outside
the reader's derivation. Lines 67-70 preserve separate full-proof obligations.
The relevant execution-plan rows are
`spec/EDITION-2026-EXECUTION-PLAN.md:163-165`. A justified correction is therefore
assessed for preservation of the required mathematical content and faithful
identification of the change; identity with an incomplete historical passage
is not the acceptance condition.

I did not read other reviewers' reports or author verification/verdict
sections. After comparing the manuscript with its sources, I inspected only
the identified source, attribution and change-description portions of the
correction notes listed below. Their assessments were not used as verdict
evidence.

## Reviewed snapshot

All five assigned SHA256 values matched the actual files at the beginning of
the review and were checked again at its end. Paths below are relative to
`C:/Dev/the-methods-of-reason`.

| Artifact | SHA256 |
| --- | --- |
| `source/formal-logic-reference.tex` | `0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc` |
| `handbook/parts/p08/temporal-epistemic-supplement.tex` | `3028f3196a8f8fc064a06e5e7aec3366fad90aa042fceaf0645825aa70eddb56` |
| `handbook/parts/p02/pa2-definition.tex` | `6a5467b748c91f6cb9c8484e6c7e7b122a0268ecc80fc3a8c7213b92251d4a63` |
| `handbook/restoration/inherited-07295-07468.tex` | `1958b3363dcac80b5c7af56f446e74591b4249d23c1c8543cc9ec7de7bb93a89` |
| `handbook/restoration/inherited-11711-11740.tex` | `35225299698968b229674bdf96987d1fbde59dcecb15659c4615f18b27679c08` |
| `spec/EDITION-2026-CONTRACT.md` | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |
| `spec/EDITION-2026-EXECUTION-PLAN.md` | `aa39a98636ad6844c142be99d328a0bd0c9fc8919debbffcb1987b73154553ec` |

## C3: CTL root valuation — PASS

The actual semantic clauses were read in
`handbook/parts/p08/temporal-epistemic-supplement.tex:46-104`, and the complete
figure was read at lines 329-353. The structure has nonempty state set, a total
successor relation and infinite paths. The until clauses at lines 80-99 permit
the witness position to be zero. The EF/AF expansions are explicitly present
in `handbook/registry/calculi/hilbert-ctl.tex:5-6`.

The figure now labels the root `w:¬p` at line 332. Its positive left branch
starts at `u`, and its right branch consists entirely of negative states,
including the root. Lines 349-351 explicitly identify both continuations as
infinite branches. Thus EFp is true, with the left path and witness position
1; AFp is false because the right path has no position satisfying p. EXp is
true because u is a positive successor, and AXp is false because v is a
negative successor. These are exactly the annotations at lines 346-347. No
unlabelled value at position zero is needed.

The correction is part of a separately identified editorial derivative
(`temporal-epistemic-supplement.tex:1-18`), not a claim to reproduce a CTL
figure from the frozen archive. A search of that archive found no `CTL`,
`computation tree` or `fig:p08-ctl-tree` text. The change-description record is
`spec/research/edition-2026-c3-ctl-correction.md:5-16`.

For retention evidence, I replaced the one occurrence of the corrected root
label with the old bare `w` label in memory only. The resulting complete-file
SHA256 was
`637fa1588d8e7ef2412142562847733a2ca0c271bd294576bbf0879217c30b70`, exactly the
predecessor digest recorded at that note's line 13. This checks the claimed
single-label change against the recorded digest. A separately saved predecessor
body was not opened, so the historical digest's provenance is not independently
certified by this review.

The active route is `handbook/main.tex:32` to `handbook/parts/p08.tex:32`.
The correction introduces no external consultation or theorem-proof claim.
This verdict covers the textual model and its four truth values; rendered
legibility and the full A-146 apparatus obligation remain outside it.

## C4 / R-032: the PA2 definition — PASS

The whole new file `handbook/parts/p02/pa2-definition.tex:1-42` was read.
Lines 4-8 specify the signature `{0,S,+,×}`, its arities, logical equality,
and PA2 as one conjunction of seven closed sentences. Lines 11-16 are the
same successor nonzero, successor injectivity and unary second-order induction
axioms as frozen source lines 12359-12376. Lines 17-23 give the four arithmetic
recursion equations displayed at frozen lines 9105-9107, preserving the
source's recursion on the second argument and the multiplication clause
`x × S(y) = (x × y) + x`.

The definition does not silently import all of Robinson arithmetic: its four
recursion equations have been selected for the expanded full second-order
object, and its induction conjunct is the source's second-order sentence.
Lines 26-31 state unary X's full powerset range, a nonempty object domain,
and total functions. This matches the full-assignment and quantifier clauses
at frozen lines 12293-12329 and the active matching fragment at
`inherited-12290-12355.tex:4-40`. Lines 33-39 explicitly distinguish the
seven-conjunct expanded sentence from the successor-only axiom set.

The seam is active and ordered correctly:
`handbook/main.tex:25` reaches `handbook/parts/p02.tex`; its lines 50-53 input
the full-semantics fragment, the successor-categoricity fragment, the new
definition, and then the fragment containing the first substantive PA2 use.
The wrappers at `scope-SRC-12290-12355.tex:1-3`,
`scope-SRC-12356-12414.tex:1-3`, and `scope-SRC-12415-12536.tex:1-3` input those
actual files. The reduction's uses are at
`inherited-12415-12536.tex:39-43`. The inactive alternative
`parts/p02/second-and-higher-order-logic.tex` was not treated as active evidence.

Read-only line comparisons show that the complete active full-semantics,
successor-categoricity and failure-of-compactness/effective-completeness
fragments retain their corresponding frozen source lines. The new definition
therefore supplies the missing antecedent without replacing the source's
categoricity argument or its qualifications.

In particular, `inherited-12415-12536.tex:35-51` still says “Proof sketch” and
still identifies the reduction, effectiveness and computability proof as
omitted. The source's expanded-signature observation at
`inherited-12356-12414.tex:55-58` is also retained. Defining PA2 does not fill
or close those separate proof obligations.

The addition is identifiable by the file's opening provenance comments and
`spec/research/edition-2026-c4-pa2-definition.md:6-28`. No new external-source
consultation is asserted. The existing Barwise–Feferman and Shapiro references
remain source citations for the inherited sketch; this review does not certify
their external bodies.

## C5 / R-030: DLO four-case completion — PASS

The complete current `handbook/restoration/inherited-07295-07468.tex:1-217`
was read against frozen source lines 7295-7468. The source theorem and its
“complete proof” status at frozen lines 7402-7407 are unchanged at current
lines 108-113. Its former proof at frozen lines 7409-7425 suppresses the
interval cases. The frozen exercise feedback at lines 16102-16110, still
present as a “Solution sketch” in
`inherited-15638-16742.tex:465-473`, names those cases and asks the reader to
check them. It is a source lead, not a complete case proof.

The active proof now defines the finite lower and upper image sets L and U
at lines 123-133, and states that they partition the old range. Lines 135-146
give the four required cases: both bounds using density, only a lower bound
using no greatest element, only an upper bound using no least element, and
no bounds using the nonempty domain. Lines 148-154 establish that the chosen
point is outside the old range and that the extended finite bijection
preserves and reflects order. This supplies the source's compressed “unused
point in the corresponding interval” step with its exact hypotheses.

Lines 156-161 apply the same construction to the inverse map for a back stage,
retaining every old pair. Lines 163-169 explain why the increasing union is
a function, injective, total, surjective and order preserving and reflecting.
Lines 169-174 supply the existence of a countably infinite DLO model using
the rationals, as required by the retained categoricity definition at lines
4-9. These additions elaborate the original argument and do not substitute
a theorem about a different class of orders.

Retention was checked directly and by case-sensitive comparisons of logical
lines: frozen lines 7295-7408 equal current lines 1-114, and frozen lines
7427-7467 equal current lines 177-217. The final blank source line is not
substantive content. Thus the finite partial isomorphism definition,
back-and-forth method and theorem, saturated-structure corollary, ACF example,
Ryll–Nardzewski and Morley statements, citations and final warning are retained.
The latter two theorems remain “cited theorem” at current lines 198 and 207.
Their complete proofs have not been supplied or relabelled by this correction.

The active route is `handbook/main.tex:26` to `handbook/parts/p03.tex:58` to
`scope-SRC-07295-07468.tex:2`. The correction is externally identified in
`spec/research/edition-2026-c5-dlo-four-cases.md:1-12,28-33`. Its new proof
paragraphs claim no consultation of Hodges or Marker; the original citations
and their roles remain intact.

## C4 / S-013: analytic derivation — PASS

The complete current `handbook/restoration/inherited-11711-11740.tex:1-57`
was read. The original chapter title and label occupy lines 1-2; the new
definition occupies lines 4-30 before the original first section at line 32.
This meets the assigned location requirement at the titled concept's first
appearance.

The propositional clause at lines 5-9 combines cut-freeness with the literal
subformula condition displayed in frozen lines 11824-11833. Its primitive
syntax and abbreviation convention makes the selected syntax explicit. The
first-order clause at lines 11-18 states instances under capture-avoiding term
substitution and bound-variable renaming, explains what happens when an outer
quantifier is removed, and retains the selected rules' language and freshness
conditions. This spells out the qualification in frozen lines 11858-11864
and 15614-15617 rather than asserting the false literal first-order property.
The example at lines 20-23 illustrates exactly that distinction.

Lines 23-27 preserve the limitations: infinitely many term instances may
remain, the subsequent existence claims retain their stated proof status,
and extensions need their own results. The source consequence and calculus
dependence passages at frozen lines 11882-11913 are retained in the matching
active fragment. The active cut-elimination theorem and reduction at
`inherited-11768-11823.tex:11-55` still carry “proof sketch”; the propositional
subformula and empty-sequent corollaries remain sketches in
`inherited-11824-11881.tex:20-33,43-57`. No source sketch is upgraded by the
new definition.

Case-sensitive line comparisons verify that frozen lines 11711-11713 equal
current lines 1-3 and frozen lines 11714-11739 equal current lines 32-57.
The chapter title, label, rank/height definition and complete displayed mix
rule text are retained. The inserted definition is therefore identifiable
without losing any original substantive content. Its provenance note's source
discussion is `spec/research/edition-2026-c4-analytic-definition.md:22-38`.
The addition attributes no new external theorem or consulted source.

The active route is `handbook/main.tex:30` to `handbook/parts/p07.tex:99`,
then `scope-SRC-11711-11740.tex:2`; the supporting subformula and consequence
fragments follow at driver lines 102-103.

## Supporting file identities

These SHA256 values identify the principal dependencies actually inspected.
They do not imply that external works cited inside them were acquired or read.

| Artifact under `handbook/` | SHA256 |
| --- | --- |
| `parts/p02.tex` | `bf76eb346924365e7d06eb3596cf22b266d61ea6ff24096b6c527fd9f8151e0c` |
| `parts/p03.tex` | `3694a5cde0762b4cf489aa640aeca2f00b9216bf16fe4bfa2a43e0fd4583ba69` |
| `parts/p07.tex` | `c3cbd4afb174e51b042a9a6b5cbf374b33428a47e69a66440660159100eadd31` |
| `parts/p08.tex` | `18a9d459d89930dd02ec3e337acb806e4a1eb307938e4cc4e699d42428b0af27` |
| `registry/calculi/hilbert-ctl.tex` | `d8213c581d16700e21c5295f996501c14d0f25968382f394df3e93690e6a717c` |
| `restoration/inherited-09099-09111.tex` | `38534e090c35db78d99d045d19b3c7f34f1f1aaa8999cf118c7a416cd41d9d2b` |
| `restoration/inherited-12290-12355.tex` | `dd9a1564fa0d18d05d5a9ff0adc5f67b3accf6f9cf465a8efb1016a12d4da1b0` |
| `restoration/inherited-12356-12414.tex` | `3b850ff37842e3e024ac32b23712aa199db010ad2249e764bb590afc2ed89a04` |
| `restoration/inherited-12415-12536.tex` | `d4ff50a3145acac19b3e7a6054bcf0aef4aac1eb2e774f825ade02af2693f667` |
| `restoration/inherited-11768-11823.tex` | `a248a9312df24072b30435ab996e241415c725d40edadd15905fd317eb3392cf` |
| `restoration/inherited-11824-11881.tex` | `05cd142307a51b542a1a11f102fc76de4f1cf8e6843df2fe7c1afc42cb13e397` |
| `restoration/inherited-11882-11913.tex` | `8dadda42399ae66736facb728ff48faffaa77aa1a9e08d2fce8bf98564e4a0e5` |
| `restoration/inherited-15638-16742.tex` | `993a3153c9ca856f761b5650c312e85e2be78fa23b8afc8edcd4e87a7b2983bf` |
| `restoration/inherited-15489-15619.tex` | `175a9850e56757bcdd168d683f1e52a35b9207832204e3bb105f4a57405beb78` |

## Read extent and limits

Every assigned target range was read. Continuous primary-source ranges read
were 7175-7198, 7295-7468, 7469-7478, 9099-9111, 11711-11740,
11768-11823, 11824-11913, 12290-12465, 15601-15619 and 16098-16118.
The entire three short target files were read. In the temporal supplement,
continuous reading covered lines 1-115 and 318-353; lines 116-317 and 354-756
were not comprehensively read and receive no surrounding-chapter verdict.

The complete active supporting fragments 09099-09111, 12290-12355,
12356-12414, 12415-12536, 11768-11823, 11824-11881 and 11882-11913 were
read. The DLO feedback fragment was read only at its lines 465-477; the
qualifying-problem solution fragment only at lines 113-131. Other contents of
those two longer feedback files remain outside this review. All four relevant
part drivers and the CTL sheet were read; main.tex was inspected at its
relevant part input lines. The execution plan was consulted for the three
correction rows, not reviewed as a whole.

No external book or paper body was consulted. Existing external source
citations elsewhere in the inspected fragments retain their source's roles;
this review supplies no independent acquisition, rights or external textual
fidelity verdict for them. Historical review acceptances were not reused.
Only the general distinction between text review and admission was consulted
in the local memory guidance; all manuscript findings above came from the
current files.

Verification consisted of reading actual LaTeX, following the stated input
seams, comparing retained source lines, checking the four displayed CTL truth
values, and hashing files. No software tests, build, render, formal
mechanization, provenance admission, register closure or publication acceptance
was performed. The separate full-proof obligations identified above remain
open at their inherited status. The only file written by this reviewer is
this report.
