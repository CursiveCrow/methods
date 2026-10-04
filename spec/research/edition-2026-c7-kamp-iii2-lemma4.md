# Edition 2026 C7: Kamp III.2, Lemma 4

Date: 7 September 2026 Pacific time; 8 September UTC.
Author: /root/kamp_lemma4_author.
Repository: C:\Dev\the-methods-of-reason.
Standing: complete author construction for integration and fresh review.

## Written extent

The full selected conjunction lemma is written, including its elementary
interval prerequisites, the finite fusion construction, every point/gap
case in both directions, and the final use of the defining Com premises.

| Owned manuscript | Extent | SHA256 |
| --- | --- | --- |
| handbook/parts/p09/presentations/kamp-iii2-lemma4.tex | 318 lines; definitions, three proved results, finite method, examples | 1821FB12C4E77B1D531A3BB154581451A972745BAFFAE1FF0611E34152CF13EB |
| handbook/annex/p09/kamp-iii2-lemma4.tex | 585 lines; three complete reciprocal proofs | 2C1DA5AE40BC16DD4533C64714DEF9868F93D2202202D30E6FFE10AA6DEB451E |

The body and annex files and this source note are the only repository
files owned or edited by this author. Root owns the host inputs,
bibliography, symbols and admission. No subagent, manuscript PDF build,
manuscript render, software test, generator, commit or admission action
was performed. The complete authored LaTeX was read back;
transcription and notation issues found there were corrected and reread.
The three result/proof pairs were inspected directly. A scoped text
search found no added macro definitions or source-only command aliases.
These author checks are not independent acceptance.

## Primary source and actual reading

Johan Anthony Willem Kamp, Tense Logic and the Theory of Linear Order,
UCLA dissertation, 1968. Existing bibliography key: Kamp1968.
Held source: tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf.
Institutional locator:
[University of Stuttgart held thesis](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).
The 128-page PDF's SHA256 was verified before and after source reading:
C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA.
Printed page n is physical PDF page n + 9, counting from one.

| Printed pages | Physical pages | Direct scan reading |
| --- | --- | --- |
| 63–66 | 72–75 | Complete basic grammars, occurrence sequence S, point subsequence Se, realization definition and four remarks. |
| 67–68 | 76–77 | Complete E and Ep/Ef definitions, R5–R6, definition I with Com in (13), R7–R8. |
| 73–78 | 82–87 | Complete Lemma 4 statement and proof, including the immediately preceding Com convention, distribution, purification, quasi-ordering/pure-pair/fusion vocabulary, endpoint conditions (19), all f_i clauses, both semantic directions and explicit end of proof. |
| 78–79 | 87–88 | Lemma 5 statement and complete proof read to establish the exact continuation boundary; opening of Lemma 6 is context only. |

The pages above were read as 180-dpi images. Physical 82, 85 and 86 were
also read at original 300-dpi resolution to resolve the Com/Lin displays
and the slot/point/positive-requirement passage. The source images remain
at the root's request under:

C:\Users\Crow\Documents\Codex\2026-08-10\phase-4-handover-migration-campaign-written\tmp\pdfs\kamp-lemma4-source\

The names page-NNN.png identify physical pages at 180 dpi; detail-NNN.png
identify the 300-dpi pages. The generated physical pages 78–81 and the
300-dpi pages 83–84 were not inspected and are not evidence for a claim.
The held source PDF was preserved byte for byte.

The PDF skill guided scan inspection. The research skill guided primary
source tracing and this single-note handoff. Both complete skills were
read by the author; this task's explicit prohibition on subagents
controlled the research workflow. No PDF was authored, so its PDF
authoring marker did not apply.

## Source and reconstruction distinctions

The target statement is unchanged: if phi and psi have I(x,y), their
conjunction has I(x,y). The source's property has no additional free
variables, permits fewer than both endpoints to occur freely, and promises
equivalence only under x < y on Com. That is the statement proved.

| Source passage | Warranted construction in this manuscript |
| --- | --- |
| p. 67 finite substitution lists P0,...,Pn | Finite histories are followed at each original occurrence. Fresh placeholders above every label's predicate index, with intervening identity substitutions, prove the source-list presentation. Sequential effects, shared letters and replacements containing their own target are retained. |
| pp. 64, 74–75 S, Se, pure pair and fusion length | Distinct tags name occurrences, not distinct final formulas. The point tags correspond to Se of purified basic skeletons. Total preorder is the modern name for this source's total quasi-ordering. One first-sequence representative or one independent second-sequence representative per class proves that r_F is the source fusion length. |
| p. 75 (19) | First endpoints and last endpoints must coincide across the two chains. Same-chain positions remain strictly ordered. |
| p. 76 f_i clauses | h_F records point position; 2h_F − 1 is the odd slot. Interval labels occupy every slot strictly between their endpoint slots, including intervening odd point slots. Both source interval clauses are supplied explicitly. |
| pp. 76–78 semantic proof | The source sketches the extraction and converse checks. The annex proves both input extractions, the exhaustive point/gap split inside an original interval, the induced fusion, every odd-slot tag type, and every even-slot tag type. |

### The literal Lin representation premises

The source's definition (13) on p. 68 uses Com, and the immediately
preceding convention on p. 73 makes unqualified equivalence mean
Com-equivalence. The opening Lemma 4 proof nevertheless prints literal
Lin on the two representation premises. The later elementary fusion
identity (18) is in fact valid on Lin: the complete source proof uses
arbitrary linear structures and finite witness arrangements.

The author therefore uses the given representations on Com, proves
the elementary fusion identity on Lin, and restricts the latter to Com
when distributing and composing the given representations. No blanket
replacement of every Lin occurrence by Com, or transfer in the reverse
direction, is made.

There is a concrete reason the two scopes cannot simply be identified.
For a unary predicate P define the following equality-free abbreviations,
renaming bound variables separately at each insertion:

    U_P(v) := forall u (P(u) -> not(v < u)).
    C_P := ((exists u P(u)) and exists v U_P(v))
           -> exists s (U_P(s) and
                        forall v (U_P(v) -> not(v < s))).

C_P says that if the interpreted P is nonempty and upper-bounded,
it has a least upper bound. It is a sentence and so is permitted by the
"no other free variables" clause of I. On Com it is true for every P.
Thus the one-interval all-tautology Ep formula represents it under x < y.
On the rational order, interpret P as the rationals below sqrt(2).
It is nonempty and upper-bounded. Every rational upper bound r exceeds
sqrt(2), and a rational strictly between sqrt(2) and r is a smaller
upper bound. Hence there is no rational least upper bound. C_P is false
while that same tautology representation is true at
x = 0, y = 2. This disproves promotion of the given Com representation
to Lin. It does not assert that C_P lacks every possible Lin representation.

### Positive requirements, indices and the disjunction

At p. 77 the scan prints "iff" between a predicate's truth at a fused
point/gap and membership of that slot in f_i(Q). The construction on
p. 76 places only positive predicate conjunctions at slots. In a
two-point order with all input predicates true everywhere, the fused
one-interval formula is true but its interval predicate is true at
both endpoints although only the even gap slot belongs to its f_i set.
Thus truth does not imply required-slot membership. The proof needs
and uses membership implying truth. This concrete example is also
proved in the annex, with no restriction on arbitrary interpretations.

The source's following extraction paragraph uses k(j) both where an
odd-slot singleton has just been specified and as a point index.
The manuscript's h_F and 2h_F − 1 keep those roles explicit. Its
endpoint argument uses (19); the printed reference "(23)" is not used.
These are explicit reconstruction choices, not claims that our new
index names occur in the source.

The isolated claim on p. 76 displays an individual chi_i on the
right, while (18) and the actual converse paragraph on p. 77 use the
disjunction over all fusions. The manuscript consistently proves that
disjunction. Its three-point example shows why a specified strict-order
fusion need not follow from the input conjunction: only the coincident
fusion is realizable there. No individual-fusion equivalence is asserted.

The earlier withdrawn p. 41 and p. 66/p. 70 glyph suspicions play no role
and have not been revived.

## Proof pairs and notation intake

| Body result | Reciprocal annex | Extent |
| --- | --- | --- |
| thm:p09-kamp-elementary-intervals | annex:p9.kamp.elementary.intervals | Parameter renaming through all five E seeds and constructors; finite-history labels; source initial-segment presentation; realization bridge; R5 and R6 in both orientations. |
| thm:p09-kamp-interval-substitution | annex:p9.kamp.interval.substitution | R7 via unchanged complete order and modified unary interpretation; R8 at both possible endpoint positions. |
| thm:p09-kamp-iii2-lemma4 | annex:p9.kamp.iii2.lemma4 | Finite fusions and their lengths; nonempty slot labels; full two-way fusion proof; source purification bridge; every pair of Com disjuncts; all boundary cases and examples. |

Suggested new notation intake uses the local Kamp P9.4 scope:

| Notation | Type and first declaration |
| --- | --- |
| Ep(x,y), Ef(x,y) | Binary elementary formula classes from finite proper substitutions; body 13. |
| W,V; theta(v); B_p(W;x,y), B_f(W;x,y) | Finite E-labelled words, capture-avoiding free-parameter instance, and the two explicit binary formula recursions; body 44. |
| I(x,y) | Property of formulas, witnessed by a guarded finite Ep disjunction on Com; body 117. |
| e_i,f_j,b_i,d_j; T in calligraphic type | Distinct occurrence tags and their finite set; body 151 and 195. |
| F, sim_F, F_(m,n) in calligraphic type | Finite total preorder, its coincidence equivalence, and the finite family satisfying restrictions and endpoint identifications; body 151. |
| C_k,r_F,h_F | Ordered equivalence class, class count/source fusion length, and tag-to-point-position map; body 151. |
| f_F | Map from point/interval tags to subsets of alternating slot indices; body 195. |
| rho_(F,s), chi_F | Unary E conjunction at one slot and the resulting binary Ep formula presentation; body 195. |
| A_i,B_i,C_i,D_i | E(w) formula labels in the three-case worked example, not newly primitive predicates; body 270. |

Root should input the body immediately after the Lemma 3 input in
handbook/parts/p09/presentations/n-c-012.tex, and the annex immediately
after the Lemma 3 input in handbook/annex/p09.tex. The existing Kamp1968
key suffices. No source-only macro aliases or new style commands were
introduced.

## Dependencies and exact next boundary

The actual complete body/annex pairs for Lemmas 1–3 were read. Their
current hashes agree with the prior Lemma 3 handoff's dependency list,
with Lemma 3's accepted annex using
91E5182F2545CDA968E8B13FAB320988CEA3B24FC1E6572271A4EC4B66E53C0E.
Its body is
811AAA41E515F647CB6BC252A4AFEF59279B8338A0FBB43BE72DA3E572A29BA3.
The full prior author note and the bounded
spec/verification/edition-2026-p19-kamp3-text-acceptance.md were read.
The III.1 prefix/components/normal-form interfaces at body 1–200 and
the n-c-012 order/language/S/U/D context through the Lemma 3 route were
read directly. The current edition contract and conventions were read
in full. Historical memory was used only for the distinction between
bounded text acceptance and admission; mathematical claims come from
the live manuscript and held source.

The exact next source result is Lemma 5, printed pp. 78–79:
for distinct x,y,z, finitely many E(z) formulas, I(x,z) formulas
and I(z,y) formulas, their conjunction under exists z (x < z < y)
has I(x,y). Its proof and source-specific endpoint-label concatenation
remain unauthored here. Lemma 6 begins on printed p. 79.

Fresh source-fidelity, topic-validity and publication-text reviews,
root integration, relevant static/build/visual evidence and the separate
admission mechanism remain open. This author result completes the
selected Lemma 4 treatment; it does not complete Theorem III.2 or N-c-012.
