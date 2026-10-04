# w02-p01-008: sections 3.1, 3.2, 3.6 (orders, natural numbers, choice and cardinal assignment)

Provenance note for packet `work/waves/w02/packets/w02-p01-008.json`, label tag
`p01-w02-p01-008`. Session date 2026-10-04.

## Gaps addressed

- 3.1: partial order (with antisymmetry), strict partial order, non-strict linear
  order, non-strict well-order, minimal vs least member
  (`def:p01-w02-p01-008-order-kinds`); stated and proved correspondence
  strict <-> non-strict by removing/adding `id_A`
  (`thm:p01-w02-p01-008-strict-nonstrict`, annex proof).
- 3.2: metatheoretic `omega` as least inductive set (`thm:p01-w02-p01-008-omega`),
  `N := omega`, `0 = empty`, `n+1 = S(n)` (`def:p01-w02-p01-008-naturals`),
  induction (`thm:p01-w02-p01-008-induction`), `n = {k in N : k < n}` and
  `n+1 = {k : k <= n}` as theorems, N an ordinal, predecessor, omega limit
  (`thm:p01-w02-p01-008-naturals`), pigeonhole, uniqueness of finite size,
  N infinite cardinal, countable = finite or countably infinite, natural numbers
  = finite ordinals (`thm:p01-w02-p01-008-pigeonhole`).
- 3.6: representation of every well-order by a unique ordinal and order type of a
  subset of an ordinal (`thm:p01-w02-p01-008-representation`); Well-ordering
  theorem by a tower (chain) argument with no ordinals and no recursion
  (`thm:p01-w02-p01-008-well-ordering`); cardinal assignment with existence,
  uniqueness, agreement with injection comparison, totality and finite max,
  |n| = n and |N| = omega = aleph_0, and the converse (assignment for all sets
  implies AC) (`thm:p01-w02-p01-008-cardinal-assignment`). All proofs in
  `handbook/annex/p01/orders-ordinals-cardinality-and-choice-w02-p01-008.tex`.
  No use of transfinite recursion; ordinal comparability is taken from
  `thm:p01-w02-p01-011-ordinals` (annex-proved there from the ordinal
  definition alone). The agreement proof avoids CSB (whose capture proof uses
  recursion on N) by the order-type lemma, representation item 2.

## Authorized corrections identified

1. Source lines 536-539 write `n = {0,...,n-1}` as notation over an undefined
   N. Now a theorem (`thm:p01-w02-p01-008-naturals` item 3) over the constructed
   N; the capture text itself is unchanged (read-only).
2. Source lines 657-667 give the Well-ordering theorem and Cardinal assignment
   with "Status: cited theorem" and a pointer to Jech2003 (not held). The
   capture remains read-only; the statused, proved forms are
   `thm:p01-w02-p01-008-well-ordering` and
   `thm:p01-w02-p01-008-cardinal-assignment`. Updating the capture's status
   lines and its "See Jech2003 for complete proofs" sentence to point to these
   is a lead-owned change (crosslink request in the return).
3. Source line 456-462 calls an `R`-minimal element "R-least" for strict
   orders; kept, and disambiguated by item 4 of the definition plus item 4 of
   the correspondence theorem.

## Inputs opened this session

- `source/formal-logic-reference.tex` lines 440-680 and 10085-10205 (FLRV1
  v1.0, held): units 21, 22, 30-33, 41-44; definitions "Infinity", "Separation
  schema", "Replacement schema", "The set omega".
- Captures: `handbook/restoration/inherited-00363-00372.tex`,
  `-00373-00405`, `-00406-00443`, `-00444-00506`, `-00533-00602`,
  `-00603-00647`, `-00648-00744`, `-10559-10674` lines 25-70.
- Handbook siblings: `parts/p01/orders-ordinals-cardinality-and-choice-w02-p01-009.tex`
  (+annex, return), `parts/p01/sets-relations-functions-and-quotients-w02-p01-005.tex`,
  `parts/p01/finite-strings-numerical-coding-and-the-w02-p01-011.tex` lines
  1-200 and its annex items `ordinals` and `representation`,
  `parts/p01/inductive-definitions-closure-and-recursion-w02-p01-013.tex`
  (headings), `parts/p06/axioms-hierarchy.tex` 158-200,
  `parts/p06/cardinals-choice*.tex` (headings), `parts/p06.tex`, `parts/p01.tex`.
- No external held authority on set theory was found in
  `spec/coverage/edition-2026/held-sources.json` (no Jech, Kunen, Enderton,
  Halmos, Zermelo). All proofs are editorial; no external locator is written.
  The bib key `Zermelo1908` in handbook.bib is the axiomatization paper
  (Math. Ann. 65, 261-281), not the 1908 "Neuer Beweis" well-ordering paper, so
  no attribution of the tower method is made in reader text.

## Existing treatment found

- Listed and extended: captures 00444-00506, 00533-00602, 00648-00744
  (cor:cardinal-assignment, sec:set-prerequisites-03/05/06).
- Not listed in packet:
  - `handbook/parts/p01/finite-strings-numerical-coding-and-the-w02-p01-011.tex`
    (wave sibling): `thm:p01-w02-p01-011-ordinals` (ordinal items 1-6),
    `thm:p01-w02-p01-011-representation` (initial segments represented by
    ordinals), `thm:p01-w02-p01-011-infinite-ordinals` item 4 (least ordinal
    bijective with an ordinal). Reused by reference, not duplicated. Its inputs
    paragraph asserts N as the least inductive set without construction; this
    packet's section 3.2 supplies it.
  - `handbook/parts/p01/inductive-definitions-closure-and-recursion-w02-p01-013.tex`
    (wave sibling): `thm:p01-w02-p01-013-recursion` (transfinite recursion,
    proved); referenced for recursion on N, not used in any proof here.
  - `handbook/parts/p01/mathematical-preliminaries.tex` (off route):
    `def:p01-natural-numbers`, `thm:p01-well-ordering` (cited=Jech2003). Not
    reused.
  - `handbook/parts/p06/axioms-hierarchy.tex` (off route): `def:p06-omega`,
    `thm:p06-omega-least` (object-language omega). Not reused.

## Dependencies for placement

The proofs rely on labels of wave siblings 011 (ordinals, representation) and
013 (recursion, referenced only in a limitation). If 011 is not placed on the
route, `thm:p01-w02-p01-011-ordinals` items 1-5 and
`thm:p01-w02-p01-011-representation` items 1-2 must be on route for these
proofs to be complete on the reader route.

## Continuation

- Written: body file (3 sections), annex (8 annexitems), bib intake, symbol
  intake. unit-compile ok; check.py shows only the intake bib-key finding.
- Block 2 (2026-10-04): the four G1 guard hits
  (`spec/research/edition-2026-p02-unit-accounting-w02-p02-042{.md,-return.json}`,
  `...-w02-p02-044{.md,-return.json}`) are untracked files written by the
  agents of packets w02-p02-042 and w02-p02-044 (each note is headed with its
  own packet id; mtimes 04:10-05:01, after this packet's last write at 04:43).
  This packet did not create or change them and does not modify or delete
  them (A8: other agents' files). Re-checked every source locator against
  `source/formal-logic-reference.tex` (lines 365, 444, 452, 533-550, 648-667,
  10063, 10143, 10188) and the sibling statements used
  (`thm:p01-w02-p01-011-ordinals` items 1-5, `-representation` items 1-2 and
  its annex proof: no use of this packet's results, so no circularity).
  unit-compile ok; find_fused_spaces clean; check.py only the intake
  bib-key finding.
- Remaining for the lead: insert driver lines (body after
  `restoration/scope-SRC-00745-00772` in `handbook/parts/p01.tex`; annex before
  `annex/p01/boolean-prime-ideal-and-ultrafilters` in
  `handbook/annex/p01-route.tex`); optional capture status update (correction 2).
