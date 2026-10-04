# Wave W0 report: backlog integration

Date: 2026-10-04. Base: tag `w02a`. Commit `ee6559b`, tag `w00`.
This report records ledger bookkeeping. It is not a review, admission or acceptance of any text.

## Ledger status

| status | at w02a | now | change |
|---|---:|---:|---:|
| authored_unreviewed | 760 | 759 | −1 |
| partial | 1,203 | 1,228 | +25 |
| missing | 195 | 171 | −24 |
| unassessed | 317 | 317 | 0 |

Duty conservation (I7): unaccounted components went from 20,810 to 20,434, across 3,325 units.

## What happened

1. **Readiness.** An Opus agent checked each of the 16 saved, off-route drafts. Checks covered backlinks, label uniqueness, citation keys, fused spaces, a unit compile and overlap with routed text. All 16 were routable. Fixes were mechanical only: display layout, heading level to match the host, and fused spaces in intake note fields.
2. **Routing.** 17 groups were routed (batch manifest 10). The 17th is the Part 9 short-grammar normalization pair from the off-route classification. Two ordering points:
   - The normalization depends on the routed recombination-computation chapter, so routing ran in two passes.
   - The Abelard chapter (267.2) was anchored after the early Latin chapter (267.1) to keep the planned order.
3. **Adoption.**
   - **The 12 groups routed earlier but not yet merged:** adopted using your six approved glyph-overlap defaults. The restored native symbol intake was added for p09-recombination-models. The production set P and the monolith μ got named scopes that also cover their annex proofs.
   - **The 17 new groups:** 614 symbol rows and 28 bibliography records. Thirteen typed overrides cover glyphs that carry two roles in the same region, such as p/q in Part 10 and H/K in Part 4. The two calculus sheets are owned by their groups.
4. **Build.** The full TeX Live build is green at 14,522 pages, up from 13,651. Compared with `w02a`:
   - undefined citations fell from 20 to 0;
   - the same 75 undefined references remain, none new;
   - check-delta shows 0 new findings and 41 fixed.
5. **Assessment.** After routing, every section the drafts serve was assessed with keyed first and confirm assessors: 31 sections in Parts 3, 4, 6, 8, 9, 10, 13, 15, 16, 18 and 19.
   - 24 moved from missing to partial.
   - None reached authored_unreviewed. Each draft covers part of its section's owed components.
   - The remaining duties are recorded: 111 writable gaps, 86 source blockers and 4 policy items.
   - §210.4 moved from authored_unreviewed to partial. Its Harrah 2002, Ginzburg 2011 and Hintikka–Halonen–Mutanen 2002 source presentations are owed and not held.

Assessment-only packets own no files, so assessors filed ordinary authoring gaps as "lead-owned". Those were recorded as writable gaps (41 section gaps, 100 unit components), so the authoring waves for those parts will pick them up. Three items that really are lead work stay lead-owned:
- the held-sources binding for Reiter 1980 and the KLM author copy (§117.2);
- destination naming for the Gabbay–Woods vol. 2 chapters (§267.1, §267.2).

## Questions for you

1. **POL-2026-10-0004, §222.9.** The held copy of Opfer & Siegler, *Development of quantitative thinking* (Oxford Handbook of Thinking and Reasoning 2012, ch. 30) is the 2011 author draft. May the draft serve as the source version, or must the published chapter (pp. 585–605) be acquired?
2. **POL-2026-10-0005, §226.1–226.3.** The same question for Gleitman & Papafragou, *New perspectives on language and thought* (same handbook, ch. 28).
3. **Retirement proposals (OI-14).** These seven off-route files are superseded. Nothing has been moved. Retire them?

| file | why |
|---|---|
| `parts/p06/constructibility-base-erratum.tex` | already built into live `restoration/inherited-10675-10769.tex` |
| `parts/p06/relativization-index-erratum.tex` | already in live `restoration/inherited-11104-11126.tex` |
| `parts/p08/imll-empty-context-erratum.tex` | already in live `restoration/inherited-13972-14000.tex`; routing would duplicate the label |
| `parts/p08/group-operator-convention.tex` | normative content is live in `restoration/inherited-13519-13551.tex`, but its side remark on empty-group identities is not; decide whether that remark must be kept |
| `annex/p06/descriptive-set-theory.tex` | comment-only placeholder |
| `annex/p06/large-cardinals-absoluteness.tex` | comment-only placeholder |
| `annex/p12/src-027-501.tex` | strict subset of live `annex/p12/sources/src-027-501.tex` |

Seven other off-route files stay where they are, because tools reference them or they are kept as evidence. One draft is unfinished: the Part 13 supposition theories chapter (§267.3) goes to the Part 13 authoring wave.

## New source requests (for acquisition list r3)

These are new records, not yet searched. Bibliographic details come from the assessors' duty text and will be verified during scouting.

| request | work | sections |
|---|---|---|
| ACQ-2026-10-0620 | McCarthy 1986, Applications of circumscription (Artificial Intelligence 28) | 117.2 |
| ACQ-2026-10-0621 | Mosses 1990, Denotational semantics (Handbook of TCS vol. B) | 151.3, 151.4 |
| ACQ-2026-10-0622 | Plotkin 1977, LCF considered as a programming language (TCS 5) | 151.3–151.6 |
| ACQ-2026-10-0623 | Stoughton 1991, Interdefinability of parallel operations in PCF | 151.3–151.6 |
| ACQ-2026-10-0624 | Jim & Meyer 1991, Full abstraction and the context lemma | 151.3–151.6 |

Many other W0 blockers point at existing records whose download is a different version from the one owed. Examples: Lehmann–Magidor 1992 (only the arXiv preprint is held), Burris–Sankappanavar 1981, and the Handbook of Set Theory chapters (only author drafts held). Those records stay open.

## Tooling changes

- `tools/integrate_wave.py`: `collect` carries a return's `rule_sheets` (OI-13, fixed).
- `tools/wave_proposals.py`: blocker resolution now behaves as follows.
  - It matches source-series ids such as SRC-059.
  - A named work (author and year) wins over a series id.
  - A downloaded file no longer hides a blocker, because it may be another version. Only a duty that marks a work "(held" does.
- `work/waves/tooling/accounting_packets.py`: builds assessment-only packets with per-section keys.
- `work/waves/tooling/reclassify_accounting.py`: applies the lead-owned → writable reclassification described above.

## Next

W2-b covers:
- the 13 remaining packets of the Part 2 chain;
- the Part 15 lanes;
- the W2-a carry-over;
- the sections of the 12 completed chain packets, assessed at block 0.

After that comes acquisition list r3, for your approval.
