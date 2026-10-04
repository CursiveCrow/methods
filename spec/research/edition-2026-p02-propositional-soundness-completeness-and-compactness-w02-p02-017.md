# w02-p02-017 research note (P2 ch. 14: sections 14.5, 14.6, 14.8)

Packet: work/waves/w02/packets/w02-p02-017.json (label_tag p02-w02-p02-017).
Gap closed in this block: D-P2-011-GOAL-03 (and with it the composite D-P2-011-C01):
distinguish the effective finite-input decision procedures (thm:p02-decidability,
supplement lines 201-206) from the arbitrary-language BPI-relative
compactness/completeness scope.

## What was written

- Body: handbook/parts/p02/propositional-soundness-completeness-and-compactness-w02-p02-017.tex
  (sec:p02-w02-p02-017-finite-input-scope, `\section` level per packet).
  - def:p02-w02-p02-017-coded-input (atom codings, finite encoded inputs, code numbers,
    decidable premise sets, computable valuations)
  - thm:p02-w02-p02-017-finite-reduction (finite inputs over an arbitrary set of atoms; local
    coding; coding-independence; ZF, no choice)
  - thm:p02-w02-p02-017-no-coding (codable atom sets are countable and well-orderable;
    P(N) example via thm:p01-cantor)
  - thm:p02-w02-p02-017-infinite-undecidable (uniformly decidable family Gamma_x with
    Gamma_x satisfiable iff x not in K)
  - thm:p02-w02-p02-017-no-computable-valuation (decidable satisfiable Delta with no
    computable valuation; satisfying valuation defined in ZF)
  - thm:p02-w02-p02-017-bpi-boundary (finite checks = hypothesis of compactness; coded case
    choice-free; scheme over all P equivalent to BPI; v_U comes from BPI)
  - thm:p02-w02-p02-017-pairs + def:p02-w02-p02-017-pairs-example (worked example:
    disjoint pairs; satisfying valuations = choice functions)
  - def:p02-w02-p02-017-limits (failure cases / what is not claimed)
  - Relationships and Sources paragraphs.
- Annex: handbook/annex/p02/propositional-soundness-completeness-and-compactness-w02-p02-017.tex,
  full proofs annex:p02-w02-p02-017-{finite-reduction,no-coding,infinite-undecidable,
  no-computable-valuation,bpi-boundary,pairs}.
- Editable-host pointers (one sentence each, no second treatment):
  - handbook/parts/p02/free-boolean-algebra-and-completeness.tex, end of
    def:p02-fbc-source-boundary (lines 285-290).
  - handbook/annex/p02/free-boolean-algebra-and-completeness.tex lines 474-476.
  - handbook/parts/p01/boolean-prime-ideal-and-ultrafilters.tex lines 199-203.
- Patch requests: work/waves/w02/patches/w02-p02-017.json (driver inputs for body and annex;
  pointer sentence after thm:p02-decidability in the supplement, which is not editable here).
- Symbol intake: handbook/registry/symbols-intake-p02-propositional-soundness-completeness-and-compactness-w02-p02-017.csv.
- No intake bib: the only citation key, Kleene1952, is already in handbook.bib.

## Provenance and sources

- All results are editorial proofs from handbook statements, each used at its own
  standing: thm:p04-kleene-normal-form and thm:p04-tm-partial-recursive (cited Kleene1952,
  on-route P04 supplement); thm:universal-computation and the primitive-recursive
  computability theorem of sec:turing-machines-02 (source proof sketches);
  thm:enumeration, thm:halting-undecidable and the K-complement corollary of
  sec:universal-reductions-03 (source complete proofs); thm:prop-compactness;
  thm:p01-bpi-propositional-compactness; thm:p02-fbc-completeness;
  thm:p02-fbc-separation; thm:p01-cantor.
- Locator verified in this session: Kleene 1952 (held file
  source/references/acq-r1-ACQ-2026-10-0230/kleene-1952-introduction-to-metamathematics-1974-reprint.pdf,
  PDF page 340) section 63, Theorem XIX(a), equation (60), printed page 330. Cited as
  `\cite[\S\,63, p.~330]{Kleene1952}`.
- The P04 labels in parts/p04/universal-reductions.tex and machines-effective-procedures.tex
  (thm:p04-enumeration etc.) are off the active route; the text uses the active labels
  (thm:enumeration, thm:universal-computation, thm:halting-undecidable,
  def:partial-computable, sec:turing-machines-0{1,2,3}, sec:universal-reductions-0{1,3}).

## Open items (not claimed in reader text)

- No held source in this session states Con(ZF) -> Con(ZF + not BPI) or the failure of
  choice for pairs in ZF. The reader text explicitly does not assert either
  (def:p02-w02-p02-017-limits item 1). Acquisition would allow a stronger statement:
  e.g. Jech, The Axiom of Choice (1973), or Howard-Rubin (1998), with exact model/form
  numbers. Not required by the duty text.
- Incident: a scratchpad helper named fix.py was shared with another session; running it
  once executed that session's script, which rewrote
  spec/research/edition-2026-p02-propositional-languages-valuations-and-truth-functions-w02-p02-004-return.json
  (replacing a vertical-tab+"arphi" corruption by "\varphi" in proposed_decisions and
  re-dumping with indent=1). This file belongs to packet w02-p02-004; reported in the
  return for the lead.

## Continuation

- State after this block: all six results written with annex proofs; unit-compile ok;
  find_fused_spaces clean; check.py shows no finding in the owned files or edited hosts.
- Remaining for the lead: apply the three patch requests (driver inputs and the supplement
  pointer). Until the driver inputs are applied, the host pointers to
  sec:p02-w02-p02-017-finite-input-scope resolve only in the unit build.
- D-P1-005 components and D-P2-011-GOAL-01/02 were not re-written; they are covered by the
  pre-existing treatments listed in the return.
