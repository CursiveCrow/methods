# Requested manuscript review PDF

The user requested a PDF of the current manuscript while authoring continued.
This authorizes this review snapshot during the otherwise deferred build and
review phase. It does not resume independent content reviews or constitute
publication acceptance.

## Artifact

- Output: output/pdf/the-methods-of-reason-review-2026-09-08-2129.pdf.
- Captured connected manuscript: September 8, 2026, 21:29 PDT.
- Final PDF creation: September 8, 2026, 22:50:38 PDT.
- Pages: 4615; bytes: 14276387.
- SHA-256: 5E75454AA510B60DAEA7A136B397A3E885D698011738FED5CDB1DB3F7F11F2B9.
- Title metadata: The Methods of Reason.
- Subject metadata: Review manuscript captured September 8, 2026 at 21:29 PDT.
- Unencrypted PDF 1.7, letter-size base pages, 1405 outline destinations.
- Final output copy was hashed and matches the completed build exactly.

Snapshot and build files are under build/review-2026-09-08-2130/handbook.
The original source-manifest.csv records the copied inputs before the review
title overlay and necessary typesetting corrections. Later author returns
remain in the main manuscript folder and are outside this fixed snapshot.
The old handbook/main.pdf was not used as the review artifact.

## Build and necessary corrections

The build uses TeX Live 2025, with exact pdflatex, biber and makeindex paths
in the snapshot's .latexmkrc. Shell escape is disabled. The completed command
was latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error
-recorder main.tex. It returned exit code 0 and reported all targets current.
The final log is review-final-build.log; main.log, main.blg and main.ilg
retain the actual diagnostics. Biber processed all 682 requested citation
keys. MakeIndex accepted 3985 entries, rejected zero and reported zero
warnings. Index-entry count alone is not a reference-usability verdict.

Necessary fixes were made both in the active manuscript and the snapshot:

- Loaded mathtools, mathrsfs, csquotes and the required Cyrillic encoding
  fallback, preserving the intended arrows, script letters and source glyphs.
- Replaced source-only notation calls in the affected editorial Tseitin,
  preservation and PA proof-predicate files by their identical printed
  mathematical spellings.
- Corrected the malformed closing set delimiters in the independence and
  reverse-mathematics chapters.
- Protected literal at-signs in hybrid-logic titles from the title/index
  sort-key separator.
- Corrected the description-logic table's extra alignment tab and the
  deep-inference rule's mathematical side-condition delimiter.
- Added direct row-fragment input for the two generated apparatus tables.
  Their generated content was not hand-edited.
- Initialized the amsthm proof label before a leading paragraph heading;
  this removes the repeated list/prevdepth errors without changing proofs.
- Supplied a guarded annexlemma environment for the existing auxiliary
  lemmas within the internal PA proof, preserving their labels and proofs.
- Closed the missing displays in the Kamp normal-form and sequential
  intervention annexes, and the malformed lambda-development inline math.
- Added a neutral entry reference format for legacy hbitem labels.

Interrupted diagnostic passes left incomplete auxiliary files and an old
index. The final bibliography and index were regenerated/settled from the
captured inputs. A bounded trace showed the paragraph routine itself
completed normally; malformed mathematical delimiters and buffered output
had obscured the stopping location. Temporary tracing was removed from the
snapshot source. The isolated diagnostic driver is a build aid, not a
manuscript test suite or an independent content review.

## Limited checks and remaining draft conditions

The PDF skill's creation marker ran once before the snapshot/build work.
The PDF was reopened and its metadata, page count and outline destinations
were read. Root inspected actual page images for PDF pages 1, 11, 2327,
2465, 2593, 2594 and 4312: cover, contents, decision methods, argumentation,
empirical text/table and proof annex. These samples were legible and did
not show clipping or missing mathematical content.

This is not an every-page inspection. The final build still reports 35
unresolved reference occurrences, along with overfull/underfull layout
warnings. Most unresolved occurrences involve leading whitespace in a
reference list; other retained namespace/target issues also remain. Those
are still manuscript work. There are no unresolved citation warnings in
the completed build. No independent mathematical, empirical, source or
publication acceptance is asserted by this review PDF.

## Useful PDF page destinations

These are one-based physical PDF pages, not the printed folio numbers.

| Treatment | PDF page |
| --- | ---: |
| Uncertainty and statistical inference | 1689 |
| Robust hypothesis testing | 2089 |
| Robust sequential endpoints | 2099 |
| Sequential decisions | 2321 |
| Ambiguity and robust choice | 2331 |
| Bellman original resource and search constructions | 2343 |
| Schemes and critical questions | 2431 |
| Dialogue and burdens | 2449 |
| Scheme classification and diagnosis | 2465 |
| Empirical science of reasoning | 2491 |
| Original conjunction judgments | 2575 |
| Language and response-format experiments | 2589 |
| Complete proof annex begins | 2999 |

Authoring continued in three disjoint assignments during the build. The
full manuscript-completion goal and the instruction to perform consolidated
reviews after the remaining changes are still active.
