# w02-p01-002: section 1.2 (calculi, semantics, components of a logical system)

Provenance note for packet `work/waves/w02/packets/w02-p01-002.json`, label tag
`p01-w02-p01-002`. Session date 2026-10-04.

## Inputs opened this session

- `work/waves/w02/packets/w02-p01-002.json` (whole packet).
- `tmp/acquisition/src026/dandelon.pdf`, SHA-256 digest
  `ab8f84067338238168d49ebb9477e39d0130ac4082af98cd8d631cebc4e96d70`, 7 physical
  pages, text extracted with `pdftotext -layout`. Content: title page of
  *Handbook of Logic in Computer Science*, Vol. 1, *Background: Mathematical
  Structures* (eds. Abramsky, Gabbay, Maibaum; Clarendon Press Oxford, 1992)
  and printed contents pages (vii onward). For the Ryan-Sadler chapter it gives
  only section titles and start pages (chapter p. 1; 1 Introduction p. 2; 2
  Valuation systems p. 9; 2.2 p. 13; 2.3 p. 21; 2.4 p. 25; 3 p. 30; 3.1 p. 31;
  3.2 p. 34; 3.3 p. 35; 3.4 p. 38; 3.5 p. 39; 4 p. 40; 4.1 p. 41; 4.2 p. 45;
  4.3 p. 51; 4.4 p. 56; 4.5 p. 57; 4.6 p. 62; 4.7 p. 64; 5 p. 66; 5.1 p. 67;
  5.2 p. 69; 5.3 p. 71; 5.4 p. 74; next chapter "Recursion theory" p. 79).
  No chapter body text.
- `tmp/acquisition/src026/ch1-minimal.html`, `ch1-crossref.json`: Oxford
  Academic landing page and Crossref record (DOI
  10.1093/oso/9780198537359.003.0001, pages 1-78, authors Mark Ryan and Martin
  Sadler). Abstract only; page states no access to the chapter.
- `tmp/acquisition/src026/ch1-pdf.response`: a "Just a moment..." JavaScript
  challenge page, not the chapter.
- `source/references/acq-r1-ACQ-2026-10-0316/manifest.json`: manifest only, no
  file for SRC-026. No `source/references/acq-r1-ACQ-2026-10-0452/` directory
  exists (that request, category C, key SRC-026, is the one naming the whole
  chapter pp. 1-78).
- Prior first-pass assessments under
  `spec/coverage/edition-2026/assessments/w02/CA-w02-w02-p01-002-b0-*.json`.

## Existing treatment search

- `handbook/restoration/inherited-00798-00852.tex` lines 4-54 (listed in the
  packet): the general language/calculus/semantics/logical-system definitions
  and the example; it carries FLRV1-U00054 to U00059 and is read-only here.
- `grep -i "valuation system|Ryan|Sadler"` over `handbook/**/*.tex`: no
  treatment of the Ryan-Sadler chapter. The only hits are unrelated names in
  `handbook/parts/p08/sources/src-025-501.tex` (Ryan--Schobbens, Huth--Ryan).
- General consequence-relation material exists elsewhere (for example
  `handbook/parts/p03/preservation-abstract-logic.tex`,
  `handbook/parts/p07/monotonicity-inference.tex`); none of it presents the
  Ryan-Sadler valuation-system framework and none was listed in the packet.

## Decision

The held file for SRC-026 is a contents listing, not the chapter. Under the
packet rule that a source-specific presentation is written only from a held
file containing the required pages, no Ryan-Sadler definitions, results,
proofs, examples or notation can be written. Writing general material on
valuation semantics or consequence relations from other authorities would not
present this source and would duplicate existing general material, so it was
not written as a substitute. No reader body, annex, bibliography intake or
symbol intake file was created, because any reader file would be either an
empty heading or a placeholder.

## Second session (2026-10-04): compile guard

The unit compile failed because no owned body file existed. Re-checked: the
only SRC-026 files are still the contents facsimile, the Oxford landing and
Crossref records and a challenge page (`ch1-pdf.response`, HTTP 403). The
dandelon rendering `dandelon-render/page-2.png` was viewed this session and
confirms the chapter's printed contents on p. vii (OCR reads "54" for "S4",
"/" for "I", "l" for "1"; the image shows S4, I and 1). Chapter span pp. 1-78
confirmed by `ch1-crossref.json` (`page: 1-78`) and the next chapter starting
at p. 79 in the contents.

Files created, all owned by the packet:

- `handbook/parts/p01/languages-logical-systems-and-levels-of-w02-p01-002.tex`
  (35 lines): toc line, `\section{Valuation systems and consequence
  relations}` with label `sec:p01-w02-p01-002-valuation-systems`, a pointer to
  `sec:levels-01`, the chapter's printed section structure with starting pages
  (only locators seen on p. vii), and a visible `\hbstub` stating that the
  chapter's definitions, results, proofs and examples are pending. No formal
  claim about the chapter's content is made; logic names I, C, S4 appear only
  as printed in section titles, in text italics, so no symbol intake rows.
- `handbook/annex/p01/languages-logical-systems-and-levels-of-w02-p01-002.tex`:
  comment only (no body result to back).
- `handbook/bib/intake-p01-languages-logical-systems-and-levels-of-w02-p01-002.bib`:
  `RyanSadler1992` (@incollection), data from the title page and Crossref.

Checks: `tools/waves.py unit-compile` ok; `tools/find_fused_spaces.py` no
hits; `tools/check.py --tree handbook` hard findings on these files: only the
intake key `RyanSadler1992` (bib-key); non-hard metric `stub-marker` for the
`\hbstub`.

## Third session (2026-10-04): hard guards G9 and G1

- G9: the `\hbstub` in the body file was replaced by a plain reader sentence
  saying the section gives the chapter's structure only and pointing to the
  chapter (pp. 1-78). The words "(p. vii)" were removed from the body: the
  rendered contents page (`dandelon-render/page-2.png`, viewed again this
  session) shows no printed page number, so that locator was not verified.
  All section start pages in the body list were re-checked against that image.
- G1: `spec/research/edition-2026-p01-w02-p01-026-note.md` and
  `spec/research/edition-2026-p01-w02-p01-026-return.json` were not written by
  this packet. Their content is the provenance note and return of packet
  w02-p01-026 (symbol-registry patches, SRC-043). They are another agent's
  files, so they were neither edited nor deleted here; the G1 attribution
  needs resolving by whoever owns packet w02-p01-026.
- Re-searched for the chapter body: `tmp/acquisition/src026/` still holds only
  the contents facsimile, Oxford landing/Crossref records and a challenge
  page; no `source/references/*/manifest.json` mentions Sadler or ISBN
  9780198537359; request ACQ-2026-10-0452 (`work/waves/w01/ACQUISITION-LIST.csv`
  line 453) is in state held_preview.
- Checks: unit-compile ok; find_fused_spaces no hits; check.py --tree handbook
  on owned files: only bib-key RyanSadler1992 (own intake).

## Fourth session (2026-10-04): redirect on the missing chapter body

The redirect asked for the missing dependency to be attacked first. Work done:

- Local tree: no file of the chapter body exists. `find` over the worktree
  for sadler, ryan, valuation, src026, src-026 and logic-in-computer finds
  only the SRC-026 metadata scratch in `tmp/acquisition/src026/`, unrelated
  files, and this packet's own files. `held-sources.json` lists only
  `tmp/acquisition/src026/dandelon.pdf` for this source.
- Acquisition round r1 (commits aa2547e, 75e9076): ACQ-2026-10-0452, the
  request naming the whole chapter pp. 1-78, is category C in
  `work/waves/w01/ACQUISITION-LIST.md` ("no free copy found: needs a file
  you supply in source/references/") and was not in the r1 download set.
  ACQ-2026-10-0316 (category B, also listing ED26-SRC-026-001) failed:
  `work/waves/w01/downloads/out-014.jsonl` line 10 records HTTP 403
  bot-check from onlinelibrary.wiley.com, no file; its directory
  `source/references/acq-r1-ACQ-2026-10-0316/` holds only `manifest.json`.
- Two web searches (chapter title with authors; Mark Ryan Birmingham with
  chapter title) returned only bibliographic records (for example a
  PhilArchive record, RYAVSA) and no lawful full-text copy. Nothing was
  downloaded: downloads need the user's explicit approval, and the publisher
  route is a bot-check page that was not bypassed.
- Held file re-opened this session: `dandelon.pdf` (SHA-256 verified
  `ab8f8406...6d70`), text via `pdftotext -layout`, and
  `dandelon-render/page-2.png` viewed. All section start pages in the body
  list re-checked against the image (1 Introduction 2; 1.1 2; 1.2 8;
  2 9; 2.1 9; 2.2 13; 2.3 21; 2.4 25; 2.5 30; 3 30; 3.1 31; 3.2 34; 3.3 35;
  3.4 38; 3.5 39; 3.6 40; 4 40; 4.1 41; 4.2 45; 4.3 51; 4.4 56; 4.5 57;
  4.6 62; 4.7 64; 5 66; 5.1 67; 5.2 69; 5.3 71; 5.4 74; Recursion theory 79).
  The page carries no printed folio; physical page 3 is headed "viii
  Contents". `ch1-crossref.json` gives `page: 1-78`.
- Fix: the intake bib comment no longer cites "contents p. vii" (folio not
  visible on the held page).
- FLRV1 mapping re-verified: `source/formal-logic-reference.tex` lines
  798-852 and `handbook/restoration/inherited-00798-00852.tex` lines 1-54
  are identical row for row (source line n is restoration line n-797):
  U00054 source 801 = lines 4-5; U00055 804-809 = 7-12; U00056 811-816 =
  14-19; U00057 818-825 = 21-28; U00058 827-835 = 30-38; U00059 843-851 =
  46-54.
- No other handbook treatment of the chapter found (grep for valuation
  system, RyanSadler, Sadler, entailment relation, consequence operator over
  `handbook/`; hits are this packet's files and unrelated logic-programming
  consequence operators in P9 and P18).
- Checks: unit-compile ok; find_fused_spaces no hits; check.py --tree
  handbook on owned files: only bib-key RyanSadler1992 (own intake).

## Continuation

State at return (2026-10-04, fourth session):

- FLRV1-U00054 to FLRV1-U00059: carried verbatim by the read-only text
  `handbook/restoration/inherited-00798-00852.tex` (lines 4-5, 7-12, 14-19,
  21-28, 30-38, 46-54); not edited.
- ED26-SRC-026-001-DOMAIN, -CHAIN, -CASES, -ATTRIBUTION, -SECTION-1 to
  -SECTION-5: blocked_source. Required: Mark Ryan and Martin Sadler,
  "Valuation Systems and Consequence Relations", in S. Abramsky, D. M. Gabbay
  and T. S. E. Maibaum (eds.), *Handbook of Logic in Computer Science*, Vol. 1,
  *Background: Mathematical Structures*, Clarendon Press Oxford, 1992,
  pp. 1-78 (DOI 10.1093/oso/9780198537359.003.0001), whole chapter body,
  page-faithful. Acquisition request ACQ-2026-10-0452 (category C): the file
  must be supplied by the user (suggested folder
  `source/references/acq-r1-ACQ-2026-10-0452/`) and then indexed in
  `spec/coverage/edition-2026/held-sources.json`.
- Body file 34 lines (contents of the chapter with start pages and a pointer);
  annex holds no item; no symbol intake (no notation of the chapter is used).
- Next step once the chapter body is held: replace the closing paragraph of
  the body file with the presentation of sections 1 to 5.4 in source order,
  add annex items with full proofs, symbol intake rows for the chapter's
  notation, and rerun unit-compile.
