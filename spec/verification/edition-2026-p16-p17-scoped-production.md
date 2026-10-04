# P16/P17: scoped production record

Recorded 7 September 2026 Pacific time, 8 September UTC. Scope: the accepted finite-abduction and finite-preference bodies and proof annexes, with two actual P2 prerequisite fragments. This internal PDF is not a final publication or a whole-book build.

## Inputs and current standing

Content hashes and every local production repair are recorded in `spec/research/edition-2026-p16-p17-production-repairs.md`. The shared reference-kind correction and independent PASS are recorded in `spec/research/edition-2026-editorial-reference-types.md` and its cited review. The current LaTeX source is the source for all content judgments; the pages below were inspected for presentation after the earlier three-role text acceptances.

The internal driver is `tmp/pdfs/edition-2026-abduction-preferences/abduction-preferences-review.tex`, SHA-256 `D7967E49C17B8D26500FDAC91908C42903B99E6AED6954C80E068D870E5F2D27`. It includes the actual P2 scope wrappers for SRC-01661-01816 and SRC-01817-01898, followed by P16 and P17 in their edition positions, then both annexes and the bibliography. Its neutral prerequisite chapter and partial-book pagination are QA context.

Shared style: `2411A09B48D5C0A4ADBF583B350D5606CBD1A60C504681F67D52EEC444406C44`.
Current canonical bibliography: `716394DAA6C90F1DD84DF53902A8E5A200E8D48870E45CE0382119E0AB32BD8B`.

The nine-file scoped scanner covered the current P16/P17, PA numeral-builder, P19 and Kamp Lemma 3 body/annex files. It returned no findings; all twenty harvested result/proof pairs are reciprocal. The existing symbol checker accepts 1,042 rows and the bibliography checker accepts 638 entries with no intake stubs. These counts are mechanical scope evidence, not complete-book coverage.

Scanner SHA-256: `05F22DEE54E3F177EAD79DFAE16D88787E513A58441F443278679F8BC7443914`.
Notation generator SHA-256: `1107FA18828213D26FC7221B3D51A384F27A8CF8C1B136FF6DD15A2076A614D5`.
No new prose-mirroring tests were written.

## Actual final build

The build ran from `C:/Dev/the-methods-of-reason/handbook` with MiKTeX pdfTeX 1.40.29 (MiKTeX 26.5) and Biber 2.21. The final bibliography refresh and both subsequent LaTeX passes exited zero. The command uses `-disable-installer -interaction=batchmode -halt-on-error` and the isolated output directory. Biber found the two actual cited keys and rebuilt the bibliography from the current canonical file. Its Perl locale warning fell back to C; no bibliography failure occurred.

The final PDF, `tmp/pdfs/edition-2026-abduction-preferences/abduction-preferences-review.pdf`, has 45 letter pages, 494,494 bytes, SHA-256 `6FF063AACAC98D1C229555769071B5A5FC294D98813FA641CB7C077847825F04`.

| Final output evidence | SHA-256 |
| --- | --- |
| LOG | `6A87895FE16E73852C67096F66D56F80400093FDD4D45A572E033172293DDBAD` |
| BBL | `D17C35DC60C09BD1F401435B82C253A3BD502A15BEDE26D4815BD0F2F5C76FD4` |
| AUX | `8E7485A58207965541E124EBCCAC135FCE297E9E06FF7A5999F52F42B726D287` |

The final LaTeX log has zero overfull boxes, no undefined references/citations/reference formats, missing-character diagnostics, fatal errors or rerun requests. Its sole spacing diagnostic is an underfull hbox (badness 1028) in the unchanged P2 proof paragraph at lines 90–106. The paragraph was inspected on page 4 and remains readable; this nonfatal spacing observation is retained explicitly.

## Complete visual inspection

Root inspected all 45 complete page images at 1,600-pixel scale. All text, equations, tables, headings, folios and bibliography entries are legible, with no clipping, overlap, missing glyph or orphaned heading found. The final bibliography refresh was followed by a complete rerender using `pdftoppm -png -scale-to 1600`. All 45 final PNG hashes match the previously inspected page images exactly, so the inspection carries to the final build without repeating unchanged page reading.

| Physical pages | Inspected content and outcome |
| --- | --- |
| 1–8 | P2 prerequisite part/chapter and actual fragments. Page 4's mild underfull spacing is readable. Page 7 is a short legitimate excerpt ending. Pages 2 and 8 are expected blank versos. |
| 9–18 | P16 part title and complete finite-abduction chapter, pages 11–17. The repaired long headings remain attached to their text. Pages 10 and 18 are expected blank versos. |
| 19–28 | P17 part title and complete finite-preference chapter, pages 21–27. Relation examples, order assumptions and representation statements are legible. Pages 20 and 28 are expected blank versos. |
| 29–36 | Complete P16 proof annex. The four candidate sets on page 34 fit as a display. Page 35 is a legitimate short proof ending; page 36 is the expected blank verso. |
| 37–44 | Complete P17 proof annex. The three-piece interpolation formula on page 40 and all conditions/indices are visible. Page 44 is the expected blank verso. |
| 45 | Bibliography: both actual cited source manifestations and their locators are readable. |

The following table pins every inspected final image under `tmp/pdfs/edition-2026-abduction-preferences/`.

| Image | SHA-256 |
| --- | --- |
| `page-01.png` | `B291CB0C8C5ADE9A089245676D757ADCA1190A9A6AAA11DC6CECE239672979B0` |
| `page-02.png` | `6F926107030E7B8DBA4FDE4129F12C132FB1C29E4F71831818390B5074A8FD88` |
| `page-03.png` | `AA92F70FD98B364539BC3F6DADFDE20C293B994FCAF381B7C9F1D8693C219F42` |
| `page-04.png` | `5B6390679592820192274666976F9D06177210FB39177E6192565DB9916535C8` |
| `page-05.png` | `6C6B358BFDC3D24CDFF6B64E21D18B4B6D54497135EEF531A0F94CD71D023497` |
| `page-06.png` | `9D855E970E1676BFD6875A71AE7BCAF929CDB8926A3756398F3C53CA6409664D` |
| `page-07.png` | `ABAF427428833928F80D09A07DB7001B6E85A77E0041D3CA7E418A9089350125` |
| `page-08.png` | `6F926107030E7B8DBA4FDE4129F12C132FB1C29E4F71831818390B5074A8FD88` |
| `page-09.png` | `5CF0EC79FC532CF666F06849F266C7DF1F9F405FDCDF032883452CB9823E6F8C` |
| `page-10.png` | `6F926107030E7B8DBA4FDE4129F12C132FB1C29E4F71831818390B5074A8FD88` |
| `page-11.png` | `891D7B303FD6DF0D903DA72E604A6B125AD847D95E3271B415AF3F41C62600E9` |
| `page-12.png` | `CD8923EEA6B50FF5BCABB89060289B6C21F7EE2CA23CEA04B785A42AB13D2C07` |
| `page-13.png` | `2F4896ECC38C677129138CF3BFDB507233C355F9A1131E3A905499C47768D0E3` |
| `page-14.png` | `E45BC775D98F2E5B63F4D8AD2588E0ABEEEA7A7B9A44A62DAD2897FAE1191741` |
| `page-15.png` | `FBDC4731A1619E7EF1F0A615B892BFD45C246B949657CC4C17B8E058D7A8950D` |
| `page-16.png` | `900E8C3DBA696EE5672D79BBD2FA27692577CD8CC36F33CA2F3FDC1C77BAEB5B` |
| `page-17.png` | `72D2D0CDE466C522468645AE0A64E23D87D4C7DA7872092053E6FBFA188696BB` |
| `page-18.png` | `6F926107030E7B8DBA4FDE4129F12C132FB1C29E4F71831818390B5074A8FD88` |
| `page-19.png` | `3290B3A27A04B36EF0100986D0E2F5450136A009E007C00CFA2624A67B4EBCDB` |
| `page-20.png` | `6F926107030E7B8DBA4FDE4129F12C132FB1C29E4F71831818390B5074A8FD88` |
| `page-21.png` | `025E6FF9A3247A1C49372518DB7A1661B734212A119D2DA1981523CA9F0D78CD` |
| `page-22.png` | `310185F971FD8DEB118683311201690F142408896DFDD0F9407676CF49121862` |
| `page-23.png` | `CEA0C01B1066C029F5F5C7C1865E85436623461439E86823F684814938ADB4D5` |
| `page-24.png` | `08C4F62237147A7CC49DF86A8A27478B69FBADA22DDB96ED7BAD4FC9B1C7BBB3` |
| `page-25.png` | `AE85FD6FAD16E7C9A717F4C9040B214B5979C41F2348FC1E59EFD36D2F40C09F` |
| `page-26.png` | `1EFF039A72242494F00213F823AA5024B0890C6A137A66F9E851B0EBE2A5DC27` |
| `page-27.png` | `E3A070D64099BF7F3AF0CF3B9F6387CDD8816F42E616C1EA0DF80F7C553D0C9F` |
| `page-28.png` | `6F926107030E7B8DBA4FDE4129F12C132FB1C29E4F71831818390B5074A8FD88` |
| `page-29.png` | `163A79C77E6C4F9A657BB94B8C29D8E9B591E5A8B87DFB728CA796B61186FDB4` |
| `page-30.png` | `4A530EBD7F4DA0D65F0430EEF7BADF7985AA84A6FA9F6B50C53A5B6722D61CC4` |
| `page-31.png` | `713398A426C9B38FC23B5F105029DB6E3CC0BFC1DC35212B091448AB564DDCD8` |
| `page-32.png` | `F7944EE6FE40FEB44893E81AA1913656A2EFD51ED43C310E26A13B719F440493` |
| `page-33.png` | `51152224149A967987E57B08A8AA329ECC41440AF762CF66E00917DC24D2278A` |
| `page-34.png` | `B63F88E3D8B4993CECDBA4406255F758DB663D2B13C7213101479C49A14FA56E` |
| `page-35.png` | `D62C8BFEA80935DF1EEC6DE21B649C156380689FAD13E57CDDC90D51EE9A9301` |
| `page-36.png` | `6F926107030E7B8DBA4FDE4129F12C132FB1C29E4F71831818390B5074A8FD88` |
| `page-37.png` | `FC2772066DCB2656DEF3A2EEBCC30BD342DEF63D1C3FAAEFDFDA0EEF5D690670` |
| `page-38.png` | `EE6C2731121FA4F5A4A773127EC3CD162B7912A9971BDC3F7146AEE9C5A62377` |
| `page-39.png` | `DBA675A95DD756F9AEF225C7D69B663FC88215568C6D88F6B58AF48828463132` |
| `page-40.png` | `323F50A1683F3953E5D88367E6C017151DE2B63E6A449493FCCD22F06F6A8A20` |
| `page-41.png` | `68C5BA49C3BEA21E8954497FEFF00A705A7DAC82ECDD8B11A203B0A5A10B5539` |
| `page-42.png` | `6F6CAB3D5ED4893E5B34755D6267217D9578E17EE58191D0547CD4B7452DBE39` |
| `page-43.png` | `F7401DB434F7343A9D5D09C4DFBB4D2E9F235E59CEDEA2F05CB71E8F28601346` |
| `page-44.png` | `6F926107030E7B8DBA4FDE4129F12C132FB1C29E4F71831818390B5074A8FD88` |
| `page-45.png` | `5555CE412D4FF59CC08F657C0D909DD090947B19F87249F2C845F5B27EE02A8B` |

## Remaining gates

Scoped static/build/visual checks above pass with the disclosed nonfatal spacing observation. The independent preservation review has returned PASS: `spec/verification/edition-2026-p16-p17-production-preservation.md`, 189 lines, SHA-256 `AA0DF60E43A44775609BEE19E0EF0992D9BFA4DB1DD63F844D8E3B39A6F56872`. It read all four current bodies/annexes and all four drivers, independently recovered all three changed content files' accepted hashes and both P16 drivers' prior hashes, verified unchanged P17 body/drivers, and preserved both exact source artifacts and citation entries. Thus the earlier bounded source/text judgments carry through the verified local production changes. It did not repeat or independently claim root's visual inspection.

Formal unit admission, admitted-content navigation, complete part coverage, final integrated-book build and inspection, and final user editorial acceptance remain open. The public `handbook/main.pdf` was not replaced by this QA output.
