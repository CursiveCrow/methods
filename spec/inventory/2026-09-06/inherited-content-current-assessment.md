# Current inherited content: physical presence and changed passages

This continuation inventories actual source correspondence. It does not alter the book, reset historical provenance, or rerun publication checks.

## Whole inherited corpus

The frozen 17,206-line authority remains byte-identical to its manifest. A fresh comparison found 282 physical `inherited-*.tex` artifacts: 263 are on the active route and equal their complete source intervals after line-ending normalization, six are active with changed reader text, and thirteen are inactive source artifacts. The complete line comparisons are saved in [inherited-current-fragments.json](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/inherited-current-fragments.json).

All 1,055 entries in the old structural source-unit inventory have active fragment destinations. Of those structural units, 1,049 have unchanged source text and six intersect changed text. This is stronger evidence of present content than the old `open/missing` destination strings. It does not establish mathematical correctness or full publication acceptance. The structural-unit list does not individually enumerate every paragraph-level feedback item or bibliography record, so those surfaces require their own accounting.

Six original provenance records bind old artifact hashes. Their stale hashes correspond exactly to the six changed active fragments below. They must not be used to restore an earlier mathematical error over the current corrections.

## All six changed active fragments: actual text read

The complete current contents of every file in this table were read, together with the full corresponding source difference and the cited current writing/correction notes. Full paths, line counts and SHA-256 values are in the fragment inventory; the [difference report](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/inherited-current-differences.md) preserves the exact changes.

| Current reader file | Actual current change | Inventory disposition and remaining book evidence |
| --- | --- | --- |
| `handbook/restoration/inherited-10675-10769.tex` | Defines `Def(empty) = {empty}` separately before applying satisfaction to nonempty sets, and explicitly gives `L_1 = {empty}`. | Direct correction present. The text still explicitly calls its later constructibility argument a sketch and its relativization scheme cited. The old exact-copy hash is stale. |
| `handbook/restoration/inherited-11104-11126.tex` | Makes both finite conjunction index ranges start at 1; defines empty conjunctions as true and the zero-variable quantifier block as empty. | Direct correction present in the lemma, with the retained public alias. The proof is the active next fragment; no appended reader repair is needed for these clauses. |
| `handbook/restoration/inherited-11127-11199.tex` | Uses the corrected empty-base definition to obtain `empty in L_1 subset L`, then carries out the displayed derivation induction. | Corrected proof body present. The full current proof was read for its content and dependency standing; this inventory does not manufacture a new independent acceptance record. |
| `handbook/restoration/inherited-11914-11960.tex` | Replaces the old cited-only Craig/Beth paragraph with expanded formula/free-variable and arbitrary-theory statements linked to four supplied P7 proof items. | Actual proof expansion and strengthened precision are present. This is not an unchanged transcription. Existing scoped writing/review notes identify the expansion; full distinct-source/fidelity and publication admission remain separate. |
| `handbook/restoration/inherited-13519-13551.tex` | Restricts group operators to nonempty finite groups. The preceding multi-agent S5 argument remains explicitly a source sketch. | The convention correction is present and matches the correction note. It does not turn the adjacent source sketch into a complete proof. |
| `handbook/restoration/inherited-13972-14000.tex` | Defines the empty tensor as the monoidal unit and spells out validity of empty-antecedent sequents and the unit instance. | Direct correction present in the actual semantic clause. The older exact-copy provenance hash is stale. |

Controlling current evidence: [direct-corrections note](C:/Dev/the-methods-of-reason/spec/research/manuscript-direct-corrections-2026-09-06.md), [Craig/Beth proof-writing note](C:/Dev/the-methods-of-reason/spec/research/p07-interpolation-writing-progress-2026-09-06.md), and [current correction policy](C:/Dev/the-methods-of-reason/handbook/CONVENTIONS.md:3). The notes record earlier bounded independent readings. This report records its own narrower content inspection rather than reissuing those reviewers' verdicts.

## The thirteen inactive artifacts

The inactive set contains eight preamble/document-opening artifacts, three blank/end-of-document controls, the manual bibliography, and the old index-production controls. They are not thirteen missing technical chapters.

The current driver has its own document boundaries and invokes one bibliography and one index. The shared style supplies the inherited environment and notation compatibility. Actual style passages at lines 450–680 and 1439–1490 were read: they include source proof-plan/solution/theorem environments and the local restoration of `defeq`, `Rule`, `side`, and the inherited symbols. The source's `defeq` meaning is explicitly restored inside the inherited scope, independently of the outer editorial meaning. The legacy preamble's layout-only controls remain archival; a current layout pass is still separate evidence.

The 394-line manual bibliography is represented by the 64-key inherited category in the active BibLaTeX database rather than by a second manual bibliography. All 64 keys still exist. A fresh field comparison found **62 entries identical to the old field ledger, with two extended entries**:

- `GabbayPnueliShelahStavi1980` retains every old field and adds series, publisher, ISBN, author-archive URL, access date and hosting note.
- `TroelstraVanDalen1988` retains every old field and adds series, volume 121, location and ISBN. The added volume specificity needs its own exact-source evidence; it is not covered merely by the old broader title/year review.

The historical semantic-review file still matches its recorded hash for all 64 decisions. Its old verdict binds the old field sets; the two added field sets are additional current verification work. See [inherited bibliography comparison](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/inherited-bibliography-current-comparison.json).

The current `main.tex` invokes `printindex` at line 63. The old seven-line index control artifact is therefore not an absent index. Whether all current entries, sorting and rendered navigation are complete remains an apparatus/publication question documented by the separate inventory.

## Exercise feedback: complete source-surface accounting

The active feedback chapter contains **111 paragraph-level feedback headings**, with **89 declared solutions and 22 declared solution sketches**. Some headings serve multiple exercises: together they reference **117 distinct targets (112 exercise targets and five problem targets)**. Every target resolves to an actual label on the active reader route. The full feedback file matches the frozen source interval exactly after line-ending normalization. The earlier count of five `solution` environments referred to a different source surface and must not be read as only five answers in the book. The initial first-target-only heading parser was corrected to account for every target in shared headings.

The [feedback inventory](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/exercise-feedback-current-inventory.json) records all 111 headings, their current line ranges, declared status and actual target locations. This is complete presence/status/routing accounting; it does not independently prove that every declared solution is mathematically correct.

## Remaining inventory work

The current physical inherited-content mapping, all six changed-fragment descriptions, and all 111 feedback surfaces are established. Remaining related inventory work includes the exact whole-interval interpretation of every preamble/layout record and the complete current bibliography/source identification. Current review or publication evidence must be recorded as present, stale, or absent at its actual scope, without converting old `open/missing` strings into a false claim that existing content is unwritten.
