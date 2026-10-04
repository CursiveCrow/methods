# w02-p02-001: P2 chapter 9 (9.1--9.4), categorical syllogistic and existential import

Packet: `work/waves/w02/packets/w02-p02-001.json`, unit ED26-P02-syllogistic-0001,
label tag `p02-w02-p02-001`.

## Scope of this session

The assessed gaps for 9.1--9.4 and the unit were all LR001-C4 (link ED26-SRC-063-0102
and ED26-SRC-063-0103 from the modern S/S-dagger reconstruction and identify the
differing assumptions). LR001-C1, C2 and C3 were assessed covered by the existing
treatment in `handbook/parts/p02/syllogistic-inference.tex`,
`handbook/annex/p02/syllogistic-inference.tex` and the two calculus sheets; those
files were not edited.

## Sources opened in this session

- ED26-SRC-063-0103, Boger, "Aristotle's underlying logic", HHL vol. 1 (2004),
  pp. 101--246. Held derivatives `source/references/p13-greek-originals/boger-grammar.txt`
  (physical 131--150), `boger-continuation.txt` (physical 115--130) and
  `boger-semantics.txt` (physical 151--170) of the held scan
  `source/references/p13-arabic-originals/hhl1-dli-public-scan.pdf`
  (SHA-256 digest `bfd90a829d98c6913eeda27f58b524dc7d47b4243abbd4a6d7eb49525f64c766`).
  Printed = physical - 4 in this region (running heads checked: physical 134 = 130,
  135 = 131, 136 = 132, 128 = 124, 129 = 125, 151 = 147, 152 = 148, 163 = 159,
  165 = 161, 167 = 163, 168 = 164, 169 = 165, 170 = 166).
  Locators used: pp. 124--125 (indefinite nouns, note 24, table 1), 130--131 (CSFR1--4,
  predicate-first order, note 29), 132 (Pr. An. A46, "is not-good" an affirmation),
  147--148 (determinate vs indeterminate some), 159--163 (existential import; "no empty
  classes" with existent subjects; tables 7--9), 164--165 (extensional vs intensional),
  166 (table 10, deduction system ingredients).
- ED26-SRC-063-0102, Woods and Irvine, "Aristotle's early logic", same held scan.
  Chapter located at physical 32--104 = printed 27--99 (printed = physical - 5;
  running heads checked: physical 33 = 28, 34 = 29, 55 = 50, 59 = 54, 60 = 55,
  68 = 63, 69 = 64, 70 = 65, 104 = 99; physical 32 is the title page, printed 27).
  The scan's own text layer is unusable (Devanagari OCR), so I rendered physical
  pages 28--104 with pdftoppm (200 dpi, gray) and OCRed them with tesseract.js (eng)
  into the session scratchpad only (not saved under source/). Every claim below was
  read in that OCR text.
  Locators used: 38 (broad-sense theory presupposed by Pr. An., found in Topics and
  SE), 39--40 (one-one rule; connective-free except negation; example (delta) "No men
  are non-animals" is a proposition; protaseic arguments), 49--51 (Gentzen structural
  properties; syllogisms irreflexive and nonmonotonic; validity as core Gentzen
  validity), 52 (direct vs hypothetical / per impossibile syllogisms), 54 (Min,
  Non-Circ), 55--56 (Prem+, admitted on sufferance), 59 (Meth: classical validity),
  60--62 (All A are A; logical truths from the empty set), 63 (Table 2 row 2:
  "All men are mortal; All ducks are quackers; therefore some men are mortal" listed
  as valid), 64--65 (Bolzano; no syllogism from inconsistent premises via Non-Circ
  and argumental conversion; paraconsistent), 65 (connective-free except negation).
  held-sources.json lists the scan (entry with path hhl1-dli-public-scan.pdf,
  source_ids empty). The earlier assessment's statement that 0102 is "not held" is
  therefore about the absence of a registered source id, not about the file.

## What was written

- Body `handbook/parts/p02/categorical-syllogistic-and-existential-import-w02-p02-001.tex`
  (chapter sec:p02-w02-p02-001-historical-contrast): comparison table with Boger
  (tab:p02-w02-p02-001-boger), patterns and existence-committing evaluation
  (def:p02-w02-p02-001-patterns, via def:p13-boger-guarded-bridge), five theorems,
  selection translation, method, two worked examples, a limitation warning, and the
  Woods--Irvine assumption list with a structural-properties theorem.
- Annex `handbook/annex/p02/categorical-syllogistic-and-existential-import-w02-p02-001.tex`:
  full proofs of all five theorems.
- Patch request `work/waves/w02/patches/w02-p02-001.json`: replaces the generic
  Part 13 pointer at `handbook/parts/p02/syllogistic-inference.tex` lines 14--17.

Existing treatments found and linked, not listed in the packet's "existing":
`handbook/parts/p13/presentations/src063-0103.tex` (sec:p13-src063-0103,
def:p13-boger-guarded-bridge, thm:p13-boger-existence-bridge with
annex:p13.boger.existence) and `handbook/parts/p13/presentations/src063-0103-deduction.tex`
(sec:p13-boger-deduction, thm:p13-boger-conversions, def:p13-boger-deduction-bookkeeping).
The conversion results are linked, not re-proved.

## Open items

- No handbook presentation of ED26-SRC-063-0102 exists (proposed destination
  handbook/parts/p13/presentations/src063-0102.tex belongs to another packet); the
  chapter is therefore cited directly. When that presentation exists, a \ref to it
  should be added next to the citations in sec:p02-w02-p02-001-woods-irvine.
- Lead actions: input the body after parts/p02/syllogistic-inference in
  handbook/parts/p02.tex and the annex after annex/p02/syllogistic-inference in
  handbook/annex/p02.tex; merge WoodsIrvine2004EarlyLogic and the symbol intake; apply
  the patch request.

## Continuation

State at return: LR001-C4 body, annex, bib, symbol intake and patch request written;
unit-compile ok (0 overfull); check.py shows only the bib-key finding for the intake
key WoodsIrvine2004EarlyLogic; find_fused_spaces clean. Nothing further is in
progress. If resumed: (1) after `handbook/parts/p13/presentations/src063-0102.tex` exists, add its \ref in
sec:p02-w02-p02-001-woods-irvine and in the patched host paragraph; (2) the OCR of
Woods--Irvine lives only in a session scratchpad and must be regenerated (pdftoppm +
tesseract.js, physical 32--104) to re-verify locators.

Second pass (2026-10-04): guard fixes only. Reader text reworded to remove "admit"
forms (body lines 85, 202, 365, 376, 378; meaning unchanged: Prem+ is the provisional
condition of printed pp. 55--56). Note lines 22 and 89 reworded to clear fused-space
hits. The G1 hits on spec/research files for packets w02-p02-042, -044, -045 and -054
are files written by other packets' sessions; this session did not create or modify
them and left them untouched. The ED26-SRC-063-0102 link remains open: a search of
handbook/ again finds no presentation of that unit (canonical destination
`handbook/parts/p13/presentations/src063-0102.tex`, a Part 13 file outside this
packet's owned set). unit-compile ok; check.py shows only the intake bib-key finding;
find_fused_spaces clean.

Third pass (2026-10-04): the only listed gaps were G1 hits on
spec/research/edition-2026-p02-unit-accounting-w02-p02-042.md / -return.json and
-044.md / -return.json. Those are the notes of the accounting packets w02-p02-042 and
w02-p02-044, whose packet JSONs list no owned files, so the guard's wave_packet_paths map
cannot attribute them to their owners and reports them as hard hits against every packet.
This session did not create, modify or remove them (the -044 pair is absent from the tree
at this pass; the -042 pair was written 04:10-04:11 by that packet's session). Fixing the
hit needs a lead change: register each accounting packet's spec/research note and return
file in its packet owned_files (or in the snapshot's wave_packet_paths). No reader file
changed in this pass. Re-checked: no handbook presentation of ED26-SRC-063-0102 exists yet;
unit-compile ok (0 overfull); check.py shows only the intake bib-key finding;
find_fused_spaces clean.
