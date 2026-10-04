# Edition 2026 C7: Kamp III.2, Lemma 5

Date: 7 September 2026 Pacific time / 8 September UTC.
Author: /root/kamp_lemma4_author.
Repository: C:\Dev\the-methods-of-reason.
Standing: complete author construction for integration and fresh review.

## Written result

| Owned artifact | Extent | SHA256 |
| --- | --- | --- |
| handbook/parts/p09/presentations/kamp-iii2-lemma5.tex | 250 lines; two proved results, explicit word operation, finite-family convention, construction and example | 3FF96929A113AE7273508A7278D42A8DC883D014A592B98E780208BD243480EF |
| handbook/annex/p09/kamp-iii2-lemma5.tex | 464 lines; two complete reciprocal proofs | 26381378ADECC27A479724DBFAEA4650ACAF4DF29D62B4DF999FD42F758C8963 |

The selected Lemma 5 is fully supplied: finite E(z) midpoint conditions,
finite I(x,z) and I(z,y) side conditions, all their elementary disjunct
combinations, and the source's shared-midpoint concatenation. The original
conclusion retains Com scope. The elementary realization identity is
separately proved on Lin, explicitly identified as an additional conclusion,
and used only by restriction to Com for the arbitrary I premises.

Only these two new manuscript files and this note were edited. Accepted
Lemma 4 and all shared drivers, bibliography, registry and other files were
preserved. No subagent, manuscript PDF build/render, software test,
generator, commit or admission action occurred. The full new body and
annex were read back; subsequent wording and variable-scope clarifications
were reread. The two exact result/proof pairs were inspected directly.
A scoped search found no added macro definitions or source-only aliases.
These author checks are not independent acceptance.

## Held source and complete reading map

J. A. W. Kamp, Tense Logic and the Theory of Linear Order, UCLA dissertation,
1968. Existing key: Kamp1968. Held 128-page source:
tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf.
[Institutional source locator](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).
SHA256, verified before and after this block's source reading:
C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA.
Printed page n corresponds to physical PDF page n + 9, counted from one.

| Printed / physical page | Actual complete reading this block |
| --- | --- |
| 78 / 87 | End of Lemma 4; full Lemma 5 statement and (20); reduction of the midpoint conjunction; fresh Q0 reduction; Lemma 4 applied to both side conjunctions; literal Com representation premises; distribution over every pair. |
| 79 / 88 | Completion of the distributed formula; (21); reduction to pure basic skeletons; Q' and Q'' endpoint letters; deletion of the first right word position; concatenation; the complete proper substitution defining pi'; final equivalence; Lemma 6's statement and opening proof as continuation context only. |

Both complete pages were freshly rendered at 300 dpi and inspected at
original resolution. Images remain in the task workspace:
C:\Users\Crow\Documents\Codex\2026-08-10\phase-4-handover-migration-campaign-written\tmp\pdfs\kamp-lemma5-source\
as page-087.png and page-088.png. No manuscript page was rendered.

The preceding block's actual complete source readings of pp. 63-68 and
73-78 were reused against the unchanged held-source hash. They supply the
basic occurrence/realization conventions, E/Ep/Ef, property I and R5-R8,
and the fusion construction. This block freshly read the full accepted
Lemma 4 body, its annex 1-242 and 476-522 interfaces, and the active
Lemma 3 E definition and empty Boolean convention. The complete Lemma 1-3
body/annex readings and source substitution semantics from the preceding
block remain applicable; the Lemma 3 hashes were revalidated unchanged.

The complete PDF and research skills were reread. PDF guided scan
inspection; research guided primary-source tracing and this single note.
The assignment's explicit no-subagent instruction controlled the research
workflow. No PDF was authored, so its authoring marker did not apply.

## Source construction and explicit additions

The proof first conjoins the midpoint family inside E(z). Each side's
list of given I representations is folded through every disjunct pairing and
every Lemma 4 fusion. The final step takes the full pairwise product of
the resulting left/right lists. At a selected strict midpoint, both side
guards hold, so their defining Com equivalences apply at that same
assignment. Both directions of distribution under the existential are
proved without using separate midpoint witnesses.

For basic words with a and b intervals, the joined word has a+b intervals.
Its point at index a carries (eta AND alpha_a) AND gamma_0; every original
interval label remains on its original gap. The forward proof joins the
two realizing chains. The reverse proof extracts the one point at index a,
then recovers the complete left prefix and right suffix. Both endpoint
labels and the midpoint label are checked separately.

The source-specific substitution is written out in the first annex:
Q' is the last left occurrence, Q'' the first right occurrence, and pi
is the basic word obtained by removing Q'' from the right word before
concatenation. Proper substitution for Q' inserts
(Q0(z) AND Q'(z)) AND Q''(z). The newly inserted Q' is retained once,
as required by single-pass substitution. Restoring all fresh skeleton
labels and finally the midpoint condition yields exactly the labelled
join. The argument identifies the actual bound midpoint argument of pi;
it does not replace a bound variable declaration or leave z free.

The scan twice cites R8 in its compressed replacement reductions. The
expanded proof uses the actual proved substitution preservation R7 and
elementary closure R6, with their declared hypotheses. It does not
relabel the separate one-point remark R8 as a substitution theorem.
No new source-error assertion or withdrawn glyph finding is introduced.

The source prints indexed families and no separate zero-family analysis
in this lemma. The manuscript states the positive indexed formula and
then proves its explicit empty-family convention; it does not claim that
the source explicitly excludes zero. Empty midpoint, left and right
families use T^K_z, T^K_x and T^K_y respectively. Neutral interval
representations use one-interval tautological words, without adding Bp_0.
All three empty families still give exactly exists z (x < z < y).

The proofs include singleton families, repeated disjuncts, false midpoint
conditions, false side formulas, empty disjunctions, contradictory shared
point labels, false labels on empty open gaps, adjacent outer endpoints,
singleton orders, and global endpoints. A three-point example verifies
the midpoint argument and the all-empty strict-witness condition.
The extra fixed predicate P0 introduced by the declared empty conventions
is disclosed; temporary fresh skeleton letters disappear.

## Root integration and notation intake

Input the new body after Lemma 4 in
handbook/parts/p09/presentations/n-c-012.tex, and the matching annex after
Lemma 4 in handbook/annex/p09.tex. Existing Kamp1968 suffices.

| Body result | Reciprocal annex |
| --- | --- |
| thm:p09-kamp-elementary-midpoint | annex:p9.kamp.elementary.midpoint |
| thm:p09-kamp-iii2-lemma5 | annex:p9.kamp.iii2.lemma5 |

Suggested notation uses the local Kamp P9.4 scope:

| Notation | Declared role |
| --- | --- |
| W star_eta V | Finite word operation joining two positive-interval words and conjoining three labels at their common point; body 13. |
| a,b; eta | Input interval counts and the unary E(w) midpoint label; body 13 and 51. |
| theta(z), Phi(x,z), Psi(z,y), Gamma(x,y) | Three finite aggregate formulas and their strict-midpoint existential; body 85. |
| calligraphic L,R; W_rho,V_sigma | Finite elementary representation lists and their labelled words; body 135. |
| Q0,Q',Q''; pi,pi' | Fresh unary midpoint letter, two endpoint placeholder letters, basic concatenation and its proper-substitution result; first annex item, source-construction paragraph. Q0 is distinct in role from fixed P0. |

Lemma 4's current body hash remains
1821FB12C4E77B1D531A3BB154581451A972745BAFFAE1FF0611E34152CF13EB;
its annex remains
2C1DA5AE40BC16DD4533C64714DEF9868F93D2202202D30E6FFE10AA6DEB451E.
The complete current integration record
spec/research/edition-2026-bounded-kamp4-probability-decision-integration.md
was read; it records three independent text PASS reviews for that pair.
That acceptance is a prerequisite here, not acceptance of this new unit.

The exact next boundary is Lemma 6, beginning at printed p. 79 / physical
88. It concerns a fixed Bp_n pattern, four strictly increasing points,
two realizations from the first point and a guarded past-closure test at
the third. Its full proof continuation remains owed. This block does not
extend into Lemma 6. Fresh source, topic and publication-text reviews,
root integration, relevant static/build/visual evidence and separate
admission remain open for Lemma 5.
