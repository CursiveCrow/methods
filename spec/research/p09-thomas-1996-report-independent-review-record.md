# Thomas 1996 report-precursor independent manuscript review record

## Admission scope

This record admits exactly the manuscript content proposed for `N-c-013.e` and
`N-c-014.e` at the strength of Wolfgang Thomas's complete May 1996 Kiel report
precursor, *Languages, Automata, and Logic*, Bericht 9607.

It does not admit the registered 1997 chapter, Büchi 1962, McNaughton 1966,
Safra 1988, either presentation file overall, `N-c-013` or `N-c-014` overall,
Part IX, another part, a build, rendered-handbook inspection, human or user
review, the final book, or publication.

## Exact accepted snapshot

All three Round 3 reviewers accepted this unchanged seven-object pre-admission
snapshot:

| Artifact | SHA-256 |
|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` |
| `handbook/parts/p09/presentations/n-c-013.tex` | `23E73DA416CE583ADF084E1D16E4A5846AC9659E4ED0E937A1CB00FA0738AFED` |
| `handbook/parts/p09/presentations/n-c-014.tex` | `F9576BB10063037CDFD9018E6DC7DFB553651590FB74FC77D2D33EEBBF4D5915` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` |
| `spec/research/p09-thomas-1996-report-source-note.md` | `F169CB0936EAA8CB650102A974FEE01F05C3E9D58774F7A198E2CEE35E2A7150` |
| `spec/research/p09-source-presentations-lot2-3.md` | `C45908A389BB22FBB584672F9F78F1C0E45E7DDF274BC37039AEA9BC81ED281F` |

Each reviewer independently recomputed all seven identities before judgment.
After admission, the detailed and compact records received administrative
status sentences only; no mathematical or source claim changed:

| Post-admission artifact | SHA-256 |
|---|---|
| `spec/research/p09-thomas-1996-report-source-note.md` | `2BEE86E034AB4FACCA38D37E1873AC5890E730E8FC3ED3C3A63AD7AC9DCD42F6` |
| `spec/research/p09-source-presentations-lot2-3.md` | `A96CD73A2AF2BA741E41B016CABEE52D3AA7D91F600C63EEBB999CE9312BC33F` |

The closed decision ledger has SHA-256
`595CDC75837E56972A99F63F43B43DE7965B87DA43FCE5EFDEAFD8E039F9CA9C`;
the reconciled chair transcript has SHA-256
`D0327B64D1B3DFD9D42373E755A3C82C42B199C5DE2DD410A80AA024972F3606`.

## Final independent reports

The chair kept every report sealed until all three were filed, then read each
report completely and computed these identities:

| Seat | Report | SHA-256 | Verdict |
|---|---|---|---|
| Source fidelity | `boards/p09-thomas-1996-report/transcript/r3-source-fidelity.md` | `5F028511108664941B33E4BDBB1FB5A6CCA1B43FFC33616F7B976A1B7034A53A` | **ACCEPT** |
| Mathematical and proof correctness | `boards/p09-thomas-1996-report/transcript/r3-mathematical-proof.md` | `789E9DF877545B81D1D8FB0D0480E622EBF005C0C45EF8814C84F7D59EC96EE9` | **ACCEPT** |
| Adversarial publication and terminology | `boards/p09-thomas-1996-report/transcript/r3-adversarial-publication.md` | `3B253D567F9A64B98136B2C936050BEF1B18FA1CFDFFAA451D4D9547804B21F6` | **ACCEPT** |

The three seats were fresh agents with no inherited conversation history. They
read the actual frozen LaTeX and records and consulted the controlling PDF
itself at the source pages required for their judgments. They did not inspect
or rely on PNG or other derived page renders. No test, harness, checker,
repository script, TeX command, interim build, manuscript-PDF inspection, or
rendered-handbook inspection was used.

## Three-round history

1. **Round 1 rejected.** The reconstruction omitted the finite-union
   `U V^omega` characterization, left the empty Safra successor and mark
   lifetime underspecified, used a partial tree transition relation in a game
   requiring live positions, and introduced one technical name prematurely.
2. **Round 2 rejected.** Source fidelity accepted. Mathematical review found
   that deterministic Muller complementation omitted Thomas's total transition
   function; adversarial review found that persistent node names and Rabin
   pairs were used before injective live-node naming was made part of the
   determinization state.
3. **Round 3 accepted.** The reader supplied the total function and unique-run
   equation, defined a Safra state as the typed tuple `(T,ell,nu,M)`, required
   injective names and pairwise-distinct same-update allocation outside the
   predecessor name set, and reconciled ownership and status across both
   records. Three fresh seats found no remaining defect.

No finding was outvoted, and no acceptance was carried from one hash to a
changed snapshot.

## Bounded determinations

The final reviews independently established that:

- the 1996 report and registered 1997 chapter remain distinct authorities;
- the finite-word tuple and both MSO translations retain the report's exact
  effective strength and empty-word guard;
- all four infinite-word acceptance modes, Thomas's Streett ordering, and the
  finite-union characterization are correctly typed and attributed;
- deterministic Muller complementation now rests on the source's total
  transition function and unique run;
- the Safra determinization state, update order, current-event marks, empty
  absorbing successor, injective naming, `E_k,F_k` pairs, proof directions,
  and state/pair bounds are defined and mathematically coherent;
- the corrected `S1S` cycle criterion is visible and handbook-owned;
- the partial infinite-tree automaton is completed by one rejecting state
  before the game, with language preservation proved and propagated through
  complementation, the regular-tree basis route, and `S2S`;
- Thomas's later game-theoretic route remains separate from Rabin's 1969
  historical proof; and
- source content, handbook-owned repairs, access, licence, acquisition,
  admission, build status, and publication status remain distinct.

## Disposition

The exact Round 3 snapshot is admitted for source acquisition,
reader-facing reconstruction, and topic-level independent manuscript review of
`N-c-013.e` and `N-c-014.e` at May 1996 report-precursor strength only.

The registered 1997 chapter reconciliation, remaining original-source bodies,
the rest of Part IX, the other thirteen parts, the single final publication
build reserved until all fourteen parts are text-frozen, final visual review,
human review, book completion, and user acceptance remain open.
