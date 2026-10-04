# w02-p02-002: P2 chapter 9 (9.5, 9.6, 9.7), the fourteen syllogism rules under the empty-term policy

Packet: `work/waves/w02/packets/w02-p02-002.json`, unit ED26-P02-syllogistic-0001,
label tag `p02-w02-p02-002`.

## Scope of this session

The listed gaps for 9.5, 9.6, 9.7 and the unit were LR001-C4 (link ED26-SRC-063-0102
and ED26-SRC-063-0103 and identify the differing assumptions). LR001-C1, C2 and C3 were
assessed covered by `handbook/parts/p02/syllogistic-inference.tex`, its annex and the two
calculus sheets; those files were not edited.

The off-route draft of packet w02-p02-001
(`handbook/parts/p02/categorical-syllogistic-and-existential-import-w02-p02-001.tex`,
sec:p02-w02-p02-001-historical-contrast) already gives the assumption-by-assumption
comparison with both reconstructions. To avoid a second treatment, this packet's chapter
builds on its definitions (def:p02-w02-p02-001-patterns: sigma and the
existence-committing evaluation) and links its sections, and adds only material that
nothing in the handbook contains: the reading of Boger's fourteen two-premise syllogism
rules in S, their classification by existence dependence, minimal existence premises and
countermodels for Darapti and Felapton, validity of all fourteen under the
existence-committing evaluation, and the location of the a-conversion step in Boger's
table 19 completions.

Dependency: the chapter references labels of the w02-p02-001 chapter
(def:p02-w02-p02-001-patterns, def:p02-w02-p02-001-limits, thm:p02-w02-p02-001-reduction,
sec:p02-w02-p02-001-historical-contrast, sec:p02-w02-p02-001-woods-irvine). It must be
input after that chapter.

## Sources opened in this session

- Held scan `source/references/p13-arabic-originals/hhl1-dli-public-scan.pdf`
  (SHA-256 bfd90a829d98c6913eeda27f58b524dc7d47b4243abbd4a6d7eb49525f64c766, recomputed this
  session). Pages rendered with pdftoppm into the session scratchpad and read as images.
  - Woods and Irvine, "Aristotle's early logic" (ED26-SRC-063-0102): physical 32 (chapter
    title page, printed 27 by the offset below), physical 59 (running head 54: Min and
    Non-Circ), physical 68 (running head 63: Table 2, Prem+ said to be expressly proclaimed
    in the Prior Analytics), physical 104 (running head 99: end of the chapter's
    references). Printed = physical - 5.
  - Boger, "Aristotle's underlying logic" (ED26-SRC-063-0103): physical 184-192 viewed as a
    grid; physical 188 (p. 184: fourteen panvalid patterns in three figures; note 75,
    twenty-four in four figures for traditional logic), 191 (p. 187, table 19: completions;
    a-conversion only at line 4 of Darapti and Felapton; Baroco and Bocardo by reductio),
    192 (p. 188, table 20: the fourteen rules) at readable resolution; physical 187 (p. 183,
    table 16, the three conversions) read in the grid. Printed = physical - 4.
- Held derivative `source/references/p13-greek-originals/boger-semantics.txt`: physical 163
  (p. 159: no empty classes with existence; no affirmation true and every privative true
  for non-existence), physical 164 (p. 160: two-premise patterns as building blocks),
  physical 170 (p. 166, table 10: the deduction system ingredients).
- `source/references/pratt-hartmann-moss-2008-v1/0808.0521v1.pdf` hash recomputed
  (fbd2ccc0...b0e); no new locator to it is written in this chapter.

## Existing treatment found

Listed: `handbook/parts/p02/syllogistic-inference.tex` and the labels in the packet.
Not listed and linked: `handbook/parts/p13/presentations/src063-0103.tex`
(sec:p13-src063-0103, def:p13-boger-guarded-bridge),
`handbook/parts/p13/presentations/src063-0103-deduction.tex`
(sec:p13-boger-deduction, sec:p13-boger-deduction-rules, def:p13-boger-deduction-domain,
thm:p13-boger-conversions, thm:p13-boger-ten-completions with
`handbook/annex/p13/src063-0103-deduction.tex`), and the w02-p02-001 chapter above.
None of them reads the fourteen rules in S or gives countermodels with an empty middle term.

## What was written

- Body `handbook/parts/p02/categorical-syllogistic-and-existential-import-w02-p02-002.tex`.
- Annex `handbook/annex/p02/categorical-syllogistic-and-existential-import-w02-p02-002.tex`.
- Bib intake: WoodsIrvine2004EarlyLogic, the same entry as the w02-p02-001 intake
  (duplicate key with identical content; merge once).
- Symbol intake: chapter-local atoms, Boger's sentence notation, Gamma/theta sets, proof-local Z*, X*.
- Patch request `work/waves/w02/patches/w02-p02-002.json`: insert_after the lookup
  convention in the host; independent of the w02-p02-001 patch for host lines 14-17.

## Open items

- No handbook presentation of ED26-SRC-063-0102 exists; it is cited directly
  (WoodsIrvine2004EarlyLogic, pp. 27-99, p. 54, p. 63).
- Lead actions: input body and annex after the w02-p02-001 inputs in handbook/parts/p02.tex
  and handbook/annex/p02.tex; merge intakes; apply both patch requests.

## Continuation

State at return: body, annex, intakes and patch request written; unit-compile ok with
0 overfull; check.py shows only the bib-key finding for WoodsIrvine2004EarlyLogic (intake
key); find_fused_spaces clean on body and annex. Nothing in progress. If resumed: after a
presentation of ED26-SRC-063-0102 exists in Part 13, add its \ref next to the Woods and
Irvine citation in sec:p02-w02-p02-002-historical.
