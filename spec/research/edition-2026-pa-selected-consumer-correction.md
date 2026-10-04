# PA selected-predicate consumer correction

NOW-03d implementation, 8 September 2026 UTC / 7 September Pacific. Root owns this integration; the Sigma-one consumer specialist owns only the two assigned completeness files and its separate note. All eleven files were copied byte for byte before editing to `tmp/edition-2026-bounded-kamp4-probability-decision/consumer-before/`, with each relative path's slashes replaced by `--`. The eleventh change corrects the stale final forward reference identified during publication review. The original `source/formal-logic-reference.tex` remains unchanged at `0509750C13B88A4E18914BD52BDE171C725CBA14221CBFC2227D7693A2B421CC`.

## Mathematical correction

The earlier certified numerical proof relation and an arbitrarily chosen numeralwise representative remain a separately identified presentation. They supply the earlier external proof-meaning and numeralwise D1 statements. They are not internally identified with the selected direct PA graph.

The standard PA application now explicitly uses `Prv^19_PA(x) = exists p Gamma_d19(p,x,1)`. D1 and D2 are the actual internal-modus-ponens theorem, and D3 is the original-sentence evidence construction. The new D3 pair is frozen at body `7310A4F7967AD376E54F799324ADDC214535520ACA5AD8174F2D73AA8F9B821B` and annex `46CCC2144A1599DD6C5118EFCC8CA3BFB7899B8234CEF37E28547D7F47DEB9D0`.

All three independent new-unit reviews pass: `edition-2026-evidence-extension-source-review.md` (`AD962D84D995C26D33B8D3F5271D23EF98C23D75F659FE409C5FC61F6B292448`), topic report (`C0FFCADF57F1BF5A84A1272038302221FE6AC19AA745BAB0D409CCAEE9CAF8D0`), and publication report (`BF3A3B540BECEC4E886B33024B9AF344FA6130543B89EF542B7596E4A02868B4`). Those reviews establish the new construction; the present consumer edits require their own affected reviews.

The correction changes the active statements and definitions:

- The certified presentation is named explicitly at `def:fixed-proof-predicate`; its actual numerical construction and D1 proof remain intact.
- The derivability/consistency chapter declares a formula parameter with its proof-existence meaning, preserves the generic D1–D3 hypotheses, and selects the literal direct formula explicitly for standard PA uses. Its consistency sentence then uses that same selection.
- The second-incompleteness theorem and presentation-dependence explanation point to this precise choice, including the conditional relation between a subscripted proof-formula consistency statement and the selected `Con(T)`.
- GL's realization and every PA dictionary entry use `Prv^19_PA` explicitly and reference the proved D1/D2/D3 results. Its modal, fixed-point and Solovay statements retain their promised scope and existing proof statuses.
- The numerical/checker/library continuation paragraphs now identify the supplied original-Sigma-one and D3 constructions. The direct `mp_19` is distinguished from the certified numerical `mp`.
- The formalized Sigma-one theorem and its annex use the actual selected proof descriptions, Gamma output graphs and original-root invariants. The full external Q clause remains. The specialist note `edition-2026-pa-sigma-consumer-correction.md` records its exact evidence alias, weak guards, signed original-syntax return and added strict-range enumeration.

No arbitrary-representative equivalence, generic-theory D3, completed Solovay proof or formal unit admission is inferred. The proved original closed-Sigma-one promise is preserved.

## Exact before and after files

| File | Before SHA-256 | After SHA-256 | Current lines |
| --- | --- | --- | --- |
| `handbook/restoration/inherited-09328-09438.tex` | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` | `3C8947571A8DB7953ACCA52551EA4B5A303B6AF6D2FF3B4F3F1ECC8CADC023B4` | 552 |
| `handbook/restoration/inherited-09750-09816.tex` | `EFA16565DC4206D722BA62585AA452A86394B5827C84B6201C6340815062D2DE` | `C349CB272C3771C144798A25029E404EB11B6EC9DBBCA9E252B3A4ECD0EFEF7A` | 94 |
| `handbook/restoration/inherited-09877-09924.tex` | `2AA31395C09B01D9D0058A7AEDAE38FCB148A03C9DBAFD2EE52DC70125B74AA0` | `BE42EE8E10B64F754DE176B3F6D716F256CEF8CCFB423F45A27F90370ED5ABA4` | 47 |
| `handbook/parts/p05/provability-logic-gl.tex` | `9AD6D30124B666C8845B421FA40BED296CC59621D0F733C7053581C870EF183E` | `3A9C9FB7A4A1DB02E4380645BDC2DACA78E5E05F7A0465B27EBBF790EE3C5525` | 209 |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` | `CEAF88551ADCB5D9DAE1318CF13B3B7FDA150024FE14B317875CEE2D681A4D2C` | 254 |
| `handbook/parts/p05/pa-checker-arithmetization.tex` | `993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA` | `BFB54076530ADAB0DCAA1ED95E183EBB22341403EAE08187CFDD66F1DC766441` | 526 |
| `handbook/annex/p05/internal-proof-predicate.tex` | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` | `0BA00EA54615857EC2EBF334D9C947CBFEF8D67239BE0F78ED2A84126B7AEB28` | 534 |
| `handbook/parts/p05/models-and-interpretability-supplement.tex` | `6FF8A78906F572422862078DD5E75E07F6924BAAA16E73E37ADCD8F21D20E6C1` | `49F73D85C2ECF81812D194B9A079955AD8AE186934302581E21EA240BE415A41` | 266 |
| `handbook/annex/p05/depth-completion-supplement.tex` | `C04CCF07077B183DC4BC8AB622CC49653CA6B927C40A81AE074D57A407808FF0` | `7BEA46720C677FF6384C3D512D064CD195FEA9B9646B24BF7F200FFC61A3B55A` | 357 |
| `handbook/parts/p05/independence-catalog.tex` | `5C0F15A7244728C5DC703F625BEB03D039E504284BE1A8B2D51D75CA5F75F599` | `24716C807E6D5F1C8B795225B8E0F0ADAE6209FAEFD2F3B110A8DA01DAAA3BE2` | 342 |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` | `9EAFE46E69EE0F91D472B205D2F60E9C8D6053D1775E9BD888DC0625F5C3E4C6` | 539 |

The root changes to the old selected-checker and arithmetic-library dependency files are explanatory selection/continuation passages; their actual numerical definitions, Gamma formation, rule tests and previous proofs are preserved. The independent reviewers must verify this against the exact backups, not treat a changed whole-file hash as evidence of unchanged content.

## Review and remaining production work

The affected source, mathematical and publication-text reviews must read the actual changed content, the before snapshots and the exact selected-construction dependencies. In particular they must check the local formula choice in the generic consistency chapter, the preserved external Q argument, the original evidence identity and both internal witness-elimination steps.

The three edited restoration fragments need their existing correction/provenance records refreshed after the text is frozen. This note supplies change provenance and recoverable predecessor bytes; it does not falsely report those formal records validated. Relevant static/build/visual and separate admission gates remain open. No software test, manuscript build or page inspection was used to substitute for these corrections.
