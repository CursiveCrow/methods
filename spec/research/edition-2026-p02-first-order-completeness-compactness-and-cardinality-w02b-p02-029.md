# w02b-p02-029 research note (P2, sections 20.5, 20.6)

## Duty addressed in this pass

20.6 US-0(b): complete proofs of the set-theoretic prerequisites that
`thm:downward-ls` and `thm:upward-ls` (handbook/restoration/inherited-05043-05131.tex)
use and that the route cites to Jech2003 (handbook/restoration/inherited-00648-00744.tex
lines 10-47 and 87-96): finite-coding clauses 1, 2, 4; the well-ordering
theorem from AC; `cor:cardinal-assignment`.

## Existing treatment found (A9)

- `thm:p01-w02-p01-008-well-ordering` with annex proof
  `annex:p01-w02-p01-008-well-ordering` (handbook/annex/p01/orders-ordinals-cardinality-and-choice-w02-p01-008.tex
  lines 279-378): tower proof from a choice function on P(A)\{empty}. Read in full; complete.
- `thm:p01-w02-p01-008-cardinal-assignment` with annex proof (same file lines 380-469):
  existence, uniqueness, agreement, totality and max, finite cardinals, converse. Read in full; complete.
- `thm:p01-w02-p01-011-finite-coding` with annex proof
  (handbook/annex/p01/finite-strings-numerical-coding-and-the-w02-p01-011.tex lines 417-496),
  resting on `thm:p01-w02-p01-011-square` (lines 361-415, choice-free canonical-order proof).
  Clauses 1, 2, 3, 4 all proved. Read in full; complete.
- `thm:p01-w02-p01-011-syntax-counting` (lines 528-579).
- All four are on the P1 driver route (handbook/parts/p01.tex lines 15, 34; annex/p01-route.tex lines 7, 10).

Decision: no second proof of these results is written (A9). The new section
(owned body/annex files) links them and proves, in full, every remaining
set-theoretic step of the two Loewenheim--Skolem proofs that no existing
result covers: closure of the bound |X| <= mu (subsets, finite and countable
sets, binary unions and products, images, finite sequences); existence and
infinitude of mu = max(|A|, |L|, aleph_0); finite injections into infinite
sets; Skolem functions from one well-order (single use of AC); the stage
bound and closure properties of the A_n; fresh constants; the cardinal
steps of the upward proof; and the necessity of each term of the max.

The LS treatment itself (restoration 05043-05131) and the cited status lines
in restoration 00648-00744 are read-only; cross-references from them need a
patch (work/waves/w02b/patches/w02b-p02-029.json) executed by the lead.

## Sources and locators used (all seen in this session)

- source/formal-logic-reference.tex (FLRV1, Version 1.0): lines 657-660
  (well-ordering theorem), 662-667 (cardinal assignment), 679-694 (finite
  coding), 696 ff. (syntax counting), 734 (Jech pointer), 3071 (|L| := |F u R|),
  5043-5131 (Loewenheim--Skolem section; downward 5046-5095, upward 5097-5125).
- Bib keys reused (already merged in handbook/bib/handbook.bib):
  FrozenFormalLogicCompactnessApplications (note covers lines 5043--5131),
  FrozenFormalLogicFiniteCoding (note covers lines 648--744). No new key.

## Continuation

- Body (408 lines) and annex (337 lines) written; unit-compile ok; no fused
  spaces; check.py --tree shows no finding in the owned files.
- Patch requests written: work/waves/w02b/patches/w02b-p02-029.json
  (4 entries; anchors verified unique).
- Open for the lead (blocked_policy): driver input lines in handbook/parts/p02.tex
  after line 86 and handbook/annex/p02.tex after line 37; the four patch
  requests; the earlier w02-p01-011 patches on restoration 00648-00744 (status
  line 46, lines 87-96) remain unapplied.
- Not touched: FLRV1 units U00346-U00352 (20.5, existing restoration text);
  ED26-SRC-001-001 / ED26-SRC-007-001 (owned by w02b-p02-001).
- Next pass, if any: re-check after patches land that the route no longer
  carries "Status: cited theorem" for the well-ordering theorem,
  cor:cardinal-assignment and thm:infinite-cardinal-finite-coding.
