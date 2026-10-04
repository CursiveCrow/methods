# Edition 2026 C7: Kamp III.2, Lemma 6

Date: 7 September 2026 Pacific time / 8 September UTC.
Author: /root/kamp_lemma4_author.
Repository: C:\Dev\the-methods-of-reason.
Standing: complete author construction for integration and fresh review.

## Written extent

| Owned artifact | Extent | SHA256 |
| --- | --- | --- |
| handbook/parts/p09/presentations/kamp-iii2-lemma6.tex | 171 lines; complete statement, finite splice method and two examples | EBB6DEAE8B3C2538DDB8CF5AB9CF24C7C52AA0EB6202585A7E7B33B188AE99DB |
| handbook/annex/p09/kamp-iii2-lemma6.tex | 271 lines; one complete reciprocal proof | 9EA42EBBDFFE6A6A9071C581E2F10721CF2D2504B96EC1CE51FE15658469D171 |

The selected Lemma 6 is fully supplied. For a fixed Bp_n pattern and four
points a < b < c < d, its two premises are phi(a,b) and phi(a,d).
The conclusion is phi(a,c) iff its guarded past closure holds at c.
The past closure permits any initial point before c. Both source
branches, their exact switch inequalities and their full index range
are proved. The number of intervals remains exactly n.

Only these two new manuscript files and this note were edited. All
accepted Lemma 1-5 files and shared routes, bibliography and registry
were preserved. No subagent, manuscript PDF/build/render, software test,
generator, commit or admission action occurred. The full authored body
and annex were read back; subsequent small wording clarifications were
reread. The reciprocal result/proof pair and source-only command standing
were inspected directly. These author checks do not grant independent
acceptance.

## Primary source and actual complete reading

J. A. W. Kamp, Tense Logic and the Theory of Linear Order, UCLA dissertation,
1968. Existing bibliography key: Kamp1968.
Held 128-page source: tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf.
[Institutional locator](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).
Its SHA256 was verified before and after source reading:
C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA.
Printed page n is physical PDF page n + 9, counted from one.

| Printed / physical page | Complete page inspection this block |
| --- | --- |
| 79 / 88 | End of Lemma 5; complete Lemma 6 statement, explicit linear-structure premise, fixed Bp_n pattern, four points, both fixed-start realizations, guarded past conclusion, forward proof and opening reverse proof. |
| 80 / 89 | Entire remaining Lemma 6 proof: past realization, both possible initial-point comparisons, different bracketing realization in each branch, both switch inequalities, both outputs, final conclusion and exact start of Lemma 7. |
| 81 / 90 | Complete continuation of the two-part Lemma 7 statement and its proof opening, used only to identify the next source boundary and its length restrictions. No Lemma 7 construction is claimed. |

These three pages were read as full 180-dpi images. Physical 89 was also
freshly rendered and reread at original 300-dpi resolution to settle the
weak/strict comparisons and the switch bound. Images remain under:
C:\Users\Crow\Documents\Codex\2026-08-10\phase-4-handover-migration-campaign-written\tmp\pdfs\kamp-lemma6-source\
The source proof is page-088.png and page-089.png; the detailed second
page is detail-089.png. Pages 91-93 were generated while locating the
boundary but not inspected and are not evidence for any claim.

The preceding blocks' actual complete source readings of pp. 63-66
(basic grammar, occurrence word and realization remarks) and p. 73
(Com convention) were reused against the unchanged held-source hash.
The complete PDF and research skills were reread. PDF guided the scan
inspection; research guided primary-source tracing and this single note.
The assignment's no-subagent instruction controlled the research workflow.
No PDF was authored, so the PDF-authoring marker did not apply.

## Exact source construction and supplied details

The source's statement explicitly fixes a linear structure. Consequently
Lemma 6 has Lin scope despite the earlier default Com convention. No
complete-order equivalence is promoted to Lin. The proof uses finite
realizations and finite integer comparisons, with no order-theoretic
supremum or infimum.

| Source point or construction | Manuscript rendition |
| --- | --- |
| Four underlined point symbols t1,t2,t3,t4 | a,b,c,d respectively, with a < b < c < d. These are domain points, not object-language variables. |
| Sequences v1,...,v_(n+1) and w1,...,w_(n+1) | v0,...,v_n and w0,...,w_n. The point count remains n+1. |
| Past closure at t3 | phi^(exists<)(y) = exists v (v < y AND phi[v/x]), with v fresh and only free x occurrences replaced. No comparison with a is added. |
| t1 <= v1 | Choose w from a to d; retain exactly w_k <= v_k < w_(k+1). |
| v1 <= t1 | Choose w from a to b; retain exactly v_k <= w_k < v_(k+1). The operational split uses strict v0 < a after the first branch, and the proof separately includes equality. |
| Source switch range 1,...,n | Manuscript range 0,...,n-1, under the shift k_source = k + 1. Both extreme switches and n = 1 are included. |
| Source output prefix of w followed by suffix of v | Exactly (w0,...,w_k,v_(k+1),...,v_n), retaining n intervals and endpoints a,c. |

For existence of a first-case switch, the proof takes the greatest index
with w_i <= v_i; the endpoint inequalities ensure that this index is
less than n and eligible. The second case uses the greatest index with
v_i <= w_i. The implemented method chooses the least eligible switch,
but the proof verifies every index satisfying the printed conditions.
It does not rely on the additional right-endpoint inequality enjoyed
by the particular index used in the existence argument.

The first joining gap is covered by the union of the old gaps
(w_k,w_(k+1)) and (v_k,v_(k+1)). Every point below w_(k+1) is
covered by the former, and every point at or above w_(k+1) by the
latter. This includes the old endpoint that can become an interior
point of the new gap. The second joining gap is contained in the
old v gap. All other intervals and every point label are checked
at their exact original positions. The final label A_n(c) is retained.

The body supplies a finite two-interval example where the first new
gap needs both old gaps, and a one-interval example where both given
premises hold but the final label at c fails. Both are verified in
the annex. Equality of starting points, first/last switches, adjacency,
empty gaps, false gap predicates, repeated letters and insufficient
points are all addressed.

No mathematical correction to the source statement or its two splice
conditions was needed. The consistent point names, shifted indices,
definite least-index choice and expanded interval proofs are explicit
handbook details. No new source-error diagnosis or withdrawn glyph
finding is introduced.

## Dependencies, integration and notation intake

The full current Lemma 5 body was reread and both accepted target hashes
were revalidated unchanged:
body 3FF96929A113AE7273508A7278D42A8DC883D014A592B98E780208BD243480EF;
annex 26381378ADECC27A479724DBFAEA4650ACAF4DF29D62B4DF999FD42F758C8963.
The three independent evidence-extension reports were hashed and their
Kamp PASS entries inspected: source AD962D84D995C26D33B8D3F5271D23EF98C23D75F659FE409C5FC61F6B292448;
topic C0FFCADF57F1BF5A84A1272038302221FE6AC19AA745BAB0D409CCAEE9CAF8D0;
publication BF3A3B540BECEC4E886B33024B9AF344FA6130543B89EF542B7596E4A02868B4.
These records concern Lemma 5, not this new unit.

The actual mathematical dependency is the fixed-word realization and
guarded-closure equivalence from Lemma 1. Its full body and annex 1-133
were reread in this block; the remaining prior complete annex reading
was reused. Its unchanged body/annex hashes are
3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6 and
631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1.
No mathematical assertion of Lemmas 2-5 or 7 is used to prove Lemma 6.

Root should input the body after Lemma 5 in
handbook/parts/p09/presentations/n-c-012.tex, and the matching annex
after Lemma 5 in handbook/annex/p09.tex. Existing Kamp1968 suffices.
The exact reciprocal pair is thm:p09-kamp-iii2-lemma6 and
annex:p9.kamp.iii2.lemma6.

Suggested local P9.4 notation intake:

| Notation | Type / declaration |
| --- | --- |
| phi(r,s), phi^(exists<)(y) | Semantic endpoint assignment and the one-variable guarded past formula; body 12. |
| a,b,c,d | The four domain points corresponding to the source's underlined t1,...,t4; body 50. |
| bold v, w-minus, w-plus, w, r | Finite realizing sequences of the same fixed word, each with n+1 points; body 80 and annex splice. |
| k; J,K and j | Switch index in 0,...,n-1; finite comparison-index sets and their maximum used to prove existence; body 80 and the two annex switch-index paragraphs. |

The next source result is Lemma 7, beginning printed p. 80 / physical 89.
Its two-part statement continues on printed p. 81, where its proof begins.
That complete proof continuation, its two constructions and exact
length restrictions remain owed. This block stops at Lemma 6.
Fresh source, topic and publication-text review, root integration,
relevant static/build/visual evidence and separate admission remain open.
