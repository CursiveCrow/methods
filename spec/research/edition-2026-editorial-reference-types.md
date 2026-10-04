# Editorial reference kinds: shared-style correction

Recorded 7 September 2026 Pacific time, 8 September UTC. During the actual scoped P16/P17 build, editorial references lacked a registered reference kind and emitted undefined-format warnings. The public environments share the `hbitem` number counter, but their labels need their own semantic kind.

The correction in `handbook/handbook.sty` adds a local `\crefalias{hbitem}{kind}` before the shared begin helper in each of nine editorial environments. It adds the lower- and upper-case reference names for theorem, lemma, corollary, convention, method, example, warning, proof boundary and annex proof item. The definition names already existed. No counter, label identifier, proof-status record, source guard or stable part identity changed.

| Identity | SHA-256 |
| --- | --- |
| Style before this correction | `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288` |
| Corrected style | `2411A09B48D5C0A4ADBF583B350D5606CBD1A60C504681F67D52EEC444406C44` |
| Independent review | `D54BE0952FEB0173CD9955E1C000C0A61906B44766C2C02145466D63331D59A8` |

The independent review is `spec/verification/edition-2026-editorial-reference-types-review.md`. It retrieved fourteen exact primary-code/output passages, verified the installed cleveref and LaTeX first-aid behavior, and independently reversed the changed bytes in memory to recover the exact preceding style hash. The alias uses a local definition and remains active through the label write inside the environment group. The shared number and anchor sequence is preserved. Its verdict is PASS for this specific style correction.

A focused fixture was justified by this actual shared-style bug. `tmp/pdfs/edition-2026-abduction-preferences/reference-types-check.tex` exercises all nine editorial kinds, a repeated theorem, annex references, an actual inherited source wrapper and an editorial definition following that wrapper. Before correction, root observed eleven editorial label records of kind `hbitem` and undefined-kind diagnostics. Those old AUX/log files were not retained separately, and the independent reviewer explicitly did not count the old output as independently observed evidence. After correction, actual AUX records carry the correct semantic kinds while preserving the common numbering, inherited lemma/theorem kinds and stable owner/status fields. The final fixture log has no warnings or undefined-reference-format diagnostics.

| Current fixture artifact | SHA-256 |
| --- | --- |
| TEX | `F56A3750B81D91DF6EC88B5D38A926B59919007C772C2DEF4F6FF1E4223D902E` |
| AUX | `E45CF52651A33561EA1733E5F9730546C90D47266B1240F59EA06ED76B84E8AE` |
| LOG | `988D079E2258DAD5A522B28E9F76796F45447087582F1F5D76EA470777B94743` |

This fixture is internal metadata verification and supplies no book proof or admission. It does not exercise every capitalization/plural combination; remaining registrations were inspected directly. The corrected style also builds successfully in the separate 45-page P16/P17 production scope. Full-book validation and final rendering remain open.
