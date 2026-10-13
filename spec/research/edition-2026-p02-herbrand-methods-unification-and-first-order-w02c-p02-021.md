# w02ca-p02-021 (P2, section 19.8) research note

Label tag: p02-w02c-p02-021.  Toc tag: `%% toc: P2 19 19.8`.

## Provenance

- Duty MP-0 (a): converse Factoring case of Lemma thm:p02-w02b-p02-026-translation(3)
  (host annex/p02/herbrand-methods-unification-and-first-order-w02b-p02-026.tex lines 90-91,
  "Factoring is reversed in the same way").  Written as Lemma thm:p02-w02c-p02-021-factoring
  (both directions) with annex proof annex:p02-w02c-p02-021-factoring, which also assembles
  item (3) in both directions (members of T, Resolution via the w02b converse argument,
  Factoring via item (2)).
- Duty MP-0 (b): right-hand-side Superposition case of Lemma
  thm:p02-w02b-p02-026-superposition-sound (host annex lines 353-355).  Written as Lemma
  thm:p02-w02c-p02-021-superposition-rhs with annex proof annex:p02-w02c-p02-021-superposition-rhs,
  explicit (P1) and (P2) steps; also covers the source equation written r=l and restates the
  first-argument case for completeness.
- Source opened this session: source/references/acq-r1-ACQ-2026-10-0379/
  nieuwenhuis-rubio-2001-paramodulation-based-theorem-proving.pdf (held; bib key
  NieuwenhuisRubio2001Typescript, typescript pagination).  Locators verified: sec. 1.1 p. 3
  (factoring rule display, rendered page image checked: (C v A)sigma, sigma = mgu(A,B));
  sec. 1.2 p. 5 (equation l~r "or, equivalently, r~l" in rewriting); sec. 2.1 p. 12
  (equation is the multiset {s,t}, written s~t or t~s).
- Rule sheet read: handbook/registry/calculi/ordered-superposition.tex (Superposition displays
  s[l'] diamond t only).
- Existing treatment found and extended (not listed in packet "existing"):
  handbook/parts/p02/herbrand-methods-unification-and-first-order-w02b-p02-026.tex and its annex.
- Patch requests: work/waves/w02ca/patches/w02ca-p02-021.json (two replacements in the
  w02b-p02-026 annex pointing the two short sentences to the new lemmas).
- Units in this packet are all readonly (owned by w02c-p02-020 and w02c-p02-003); not written.

## Continuation

- MP-0 (a) and (b) written; unit-compile ok; fused-space check clean.
- Open: lead to apply patch requests and insert the body/annex inputs after the
  w02b-p02-026 inputs (body: parts/p02/first-order-logic.tex after line 9; annex:
  annex/p02.tex after line 46).
