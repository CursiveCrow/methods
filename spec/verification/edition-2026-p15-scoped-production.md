# P15 finite probability: scoped build and page inspection

Date: 7 September 2026. This is an internal production check of the finite
probability chapter and its seven proof items. It is not the final integrated
book, an independent content review or formal admission.

## Maintained inputs

| Input | SHA256 |
| --- | --- |
| handbook/parts/p15/finite-probability.tex | 934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1 |
| handbook/annex/p15/finite-probability.tex | 7CE651CE52FE8BFA66E5BEC221BDF48EE6318538E6A99B8E987E18C90D6B67F3 |
| handbook/parts/p15.tex | 234902D78F435603CC88523F5D7B19C21CA7E444730A92BAC91B8871C4AB0781 |
| handbook/annex/p15.tex | E8EC3BEEAEDAEFAA4E17F4C69EC6E3F48D44E3EC37046EFD2455DF408107D5AA |
| handbook/handbook.sty | 1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288 |
| handbook/bib/handbook.bib | 417399F8D66B5D7285B6B98DA4C2C6AF38EE1D1510E3C56273226FC936F708B7 |

The internal driver is
`tmp/pdfs/edition-2026-finite-probability/finite-probability-review.tex`.
It uses the actual book class, shared style, canonical bibliography and both
P15 wrappers. Setting the preceding part counter to ten gives P15 its actual
current printed position XI. The standalone chapter starts at chapter one;
this does not claim final whole-book chapter numbers or pagination.

## Build

The PDF skill's supplied operation marker succeeded once before creating the
internal driver. Production used the existing LaTeX source, as required by the
manuscript plan. The installed MiKTeX pdfTeX was run with automatic package
installation disabled. The first sandboxed invocation could not access its
existing local cache; the scoped invocation with cache access succeeded.

Working directory: `C:/Dev/the-methods-of-reason/handbook`.
Commands, with the displayed absolute paths:

    pdflatex.exe -disable-installer -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=C:/Dev/the-methods-of-reason/tmp/pdfs/edition-2026-finite-probability C:/Dev/the-methods-of-reason/tmp/pdfs/edition-2026-finite-probability/finite-probability-review.tex
    biber.exe --input-directory C:/Dev/the-methods-of-reason/tmp/pdfs/edition-2026-finite-probability --output-directory C:/Dev/the-methods-of-reason/tmp/pdfs/edition-2026-finite-probability finite-probability-review

Two LaTeX passes followed Biber, and two passes followed each subsequent
layout change to settle page references. The final log has no overfull box,
undefined citation, undefined reference, missing glyph or rerun warning.
One underfull-box diagnostic, badness 1484 at the first annex heading, remains
as an inspected spacing choice: that two-line heading is legible and entirely
within the text block. Biber emitted a system locale fallback message but
found the actual bibliography and wrote the cited entry successfully.

All seven emitted status rows retain stable owner `p15`, each with its exact
corresponding proof-annex target. The internal output has 19 letter-size pages
and 349,781 bytes. Its final SHA256 is
`0ED3BA5BC4832B24B5E0604E0E5CEF7455C523D3A88B2C8F56545DF442A7438B`.

## Actual layout repairs

The first build exposed an overwide law-projection display and inline example,
plus small heading/paragraph overflows. The maintained body now puts the
projection formulas on two aligned rows and separates four long theorem/example
headings from their following text. Both P15 wrappers apply a local 1.5em
emergency stretch within groups. The final annex heading has an explicit
line break. No shared style was changed.

The first separated-heading output left two headings alone at page bottoms.
Adding a no-break immediately after each of the four new paragraph breaks
keeps the heading with its first text. The final file remains 467 source lines.
These changes preserve every mathematical statement, proof, example, number,
label and source citation. The independent publication R2 report verifies
exact recovery of the original reviewed inputs by reversing just these
layout changes and the wrapper controls.

## Complete page inspection

Rendered all nineteen pages with bundled Poppler at a maximum dimension of
1600 pixels. Root inspected every complete page of the first zero-overfull
output: part title, blank versos, chapter text, displays, worked table,
proofs, headers/folios, and bibliography.

After the keep-with-text repair, all nineteen pages were rendered again.
Complete PNG byte comparison found changes only on pages 7–10. Root inspected
all four new pages completely. The other fifteen page images are byte-identical
to the already inspected images. Consequently every final page has inspection
evidence, with the two orphaned headings corrected.

No lost or clipped content, overlapping text, missing glyph, unresolved printed
reference or orphaned heading was observed in the final output. Formula and
table elements are readable. The intended blank versos are pages 2 and 12;
the bibliography is page 19. The shared style's technical proof identifiers
are retained, with valid links. Broader reference-apparatus and whole-book
publication requirements remain their own tasks.

The PDF and page images stay organized under the isolated `tmp/pdfs/` folder
as working evidence. No `handbook/main.pdf` build, canonical notation-view
promotion, packet/requirement closure or final publication acceptance occurred.

## Final editorial-notation refresh

A subsequent publication review identified the house-style requirements
also applicable to P15. The new chapter label and its annex reference now
use `sec:p15-finite-probability`. All 21 literal definition signs use the
registered `defeq` macro. Its one letter-adjacent use has an explicit command
delimiter. The independent standard-PA/argumentation publication R2 report
checks those tokens and recovers the earlier accepted body/annex hashes
exactly by reversing only these editorial changes.

Biber and two LaTeX passes were rerun against the current inputs in the table
above. The final log again has zero overfull boxes and no undefined reference,
undefined citation, missing glyph or rerun warning. The previously inspected
underfull heading remains unchanged. All nineteen pages were rendered anew.
Only pages 3–7, 9 and 10 differ from the prior complete page inspection; root
visually inspected every one of these seven final pages. The other twelve
PNG files are byte-identical to the previously inspected output. All final
pages therefore retain complete inspection evidence, including the corrected
definition glyphs and kept-with-text headings.
