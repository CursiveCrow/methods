# w02-p01-009: sections 3.7, 3.8 (Ultrafilter Lemma as a statused theorem)

Provenance note for packet `work/waves/w02/packets/w02-p01-009.json`, label tag
`p01-w02-p01-009`. Session date 2026-10-04.

## Gaps addressed

S-005 (C01-C04): the read-only capture `handbook/restoration/inherited-00745-00772.tex`
lines 1-22 holds the Ultrafilter Lemma in a definition environment with an
uncited strict-weakness claim (line 18-19). New section
`sec:p01-w02-p01-009-ultrafilter-lemma` supplies
`thm:p01-w02-p01-009-ultrafilter-lemma` (proved=annex) carrying the exact
principle of `def:ultrafilter-lemma` (part 1, displayed conditions verbatim in
content and notation), its scope sentence (metatheoretic choice principle, not
an object-theory formula), the ZF-provable implication AC -> lemma (part 2),
ZF-equivalents (part 3) and the relative non-implication (part 4) cited to
`HalpernLevy1971` and derived from `thm:p01-bpi-choice-separation`.

## Authorized corrections identified (FLRV1-U00048, source lines 745-766)

1. Standing: an existence principle housed in a definition is rehoused as a
   labeled statused theorem (S-005 required fix).
2. The source asserts "strictly weaker over ZF than AC" absolutely and without a
   reference. Corrected form: relative to Con(ZF), cited to Halpern-Levy 1971.
3. The capture itself is unchanged (read-only, lead-owned). Annotating or
   converting the capture, and removing/annotating its uncited sentence at
   lines 18-19, is lead-owned and requested as blocked_policy in the return.

## Inputs opened this session

- `source/formal-logic-reference.tex` lines 365-380, 648-700, 740-775 (held, FLRV1 v1.0).
- `source/references/p01-bpi-ultrafilters/repicky2015-bpi.pdf` (held): p. 543
  Theorem 1 (Halpern and Levy, transitive model of ZF with BPI and not AC);
  p. 543 "we assume V |= ZFC"; proof runs pp. 543-546; reference [2] is
  Halpern-Levy, PSPM XIII Part I, pp. 83-134.
- HalpernLevy1971 is NOT held (not in held-sources.json); cited without a
  locator. Acquisition need recorded in the return.
- Handbook: parts/p01/boolean-prime-ideal-and-ultrafilters.tex and its annex;
  parts/p01/mathematical-preliminaries.tex 118-135 (inactive
  thm:p01-ultrafilter-lemma, not on route; not reused, label not duplicated);
  parts/p03/ultrafilter-choice-and-source-boundary.tex;
  parts/p06/cardinals-choice-supplement.tex 170-300.

## Existing treatment found

- D-P1-005 (BPI <-> arbitrary-set propositional compactness, both directions,
  countable choice-free route distinguished) is already on route in
  `handbook/parts/p01/boolean-prime-ideal-and-ultrafilters.tex` lines 162-201
  (def:p01-bpi-propositional-compactness, thm:p01-bpi-propositional-compactness)
  with annex proofs; the new theorem part 3 and warning item 6 link it.
- Not listed in packet: `handbook/parts/p01/mathematical-preliminaries.tex`
  thm:p01-ultrafilter-lemma (lines 123-135) is off route (inactive).

## Continuation

- Written: body file (all subsections), annex (3 annexitems), bib intake, symbol intake.
- Pass 2 (2026-10-04): guard G1 listed six files under spec/research for
  packets w02-p02-054, w02-p02-044 and w02-p02-045. This packet did not write
  them (their mtimes are 04:01-04:08, after this packet's last write at 03:37;
  their names carry the other packets' ids) and did not modify them: they are
  other agents' owned files and are outside this packet's owned set. Lead to
  reattribute the guard finding.
- Pass 2: re-opened source/formal-logic-reference.tex 740-772 and
  repicky2015-bpi.pdf (p. 543 Theorem 1, "we assume V |= ZFC", model
  M = HOD^{V[G]}(A) with ZF and failure of AC taken from Jech 1978 pp. 184-187 /
  Jech 2003 pp. 221-223, elementary Halpern-Lauchli case taken from [2]).
  Locators in the body re-verified. Added symbol-intake row for \mathcal P(I)
  (source \Pow, which handbook.sty restricts to restoration captures and which
  typesets as \mathcal P).
- Open, blocked_source: the relative non-implication construction (the model of
  ZF + BPI + not AC) named in the section-level missing piece. HalpernLevy1971
  (PSPM XIII Part I, pp. 83-134) is not held; Repicky's held proof is not
  self-contained (imports the model's ZF properties and the failure of AC from
  Jech's Set Theory, 1978 pp. 184-187 or 2003 pp. 221-223, neither held, and the
  elementary partition case from Halpern-Levy). Needs those works before an
  annex construction can be written.
- Lead actions: insert driver lines; capture handling (S-005-C03/C04
  capture-side items, patch work/waves/w02/patches/w02-p01-009.json);
  HalpernLevy1971 locator after acquisition. unit-compile overfull box (1.24pt)
  is in the bibliography entry Repicky2015BPI of handbook.bib, not in owned files.
