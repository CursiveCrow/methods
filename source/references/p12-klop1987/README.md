# Held-source reading aids: Klop 1987

This directory contains only new reading aids for the distinct CWI Note
CS-N8701. The authoritative report remains
`tmp/acquisition/src027/cwi-klop.pdf`; its SHA-256 is
`F0103746292B130E47C2D02FE1192ABED2E33967AE0F952B87ED369C7E341543`.

`render-source-pages.py` renders selected ambiguous primary-source pages
with the bundled `pypdfium2` package. `source-pages/printed-NN.png` uses
the report's printed numbering; physical page = printed page +4.
These are source inspection images, not final handbook figures, and
they do not establish reproduction rights or publisher-version equivalence.

The source reading and exact partial authoring/component qualification
are recorded in `spec/research/p12-klop1987-source-note.md`.

`bergstra-klop1986.pdf` is the ordinary-strategy proof dependency explicitly
cited by the 1987 tutorial: JCSS 32 (1986), pp.323-362, freely served by
[CWI](https://ir.cwi.nl/pub/1781/1781D.pdf). SHA-256:
`B866DEB58156BB961EF3BA184F3C2C1119BBF03767C4B73E2057007723D366EF`.
Only residual preliminaries pp.330-332 and the ordinary-TRS specialization
of appendix pp.352-360 inform the new proofs. The paper's conditional,
bound-variable and weakly regular extensions are not imported.
`render-strategy-supplement.py` and `strategy-source-pages/` are source-only
reading aids, not manuscript renders or final figure assets.

`ars-ex5-7-source-detail.png` and `ars-ex8-source-detail.png` retain
high-resolution readings of the source's finite-arrow distinctions.

`group-completion-evidence.py`, `group-critical-pairs.json`, and
`group-overlap-locations.json` are direct finite-term mathematical
recomputation aids for the source's Table12 ten-rule group system.
They enumerate220 candidates,65 unifiable locations,15 literal trivial
pairs and50 nontrivial pairs, retaining each concrete joining trace.
The active annex prints the full overlap list and all50 joining proofs;
these files are not a substitute for its reader-facing argument and
are not a prose-test suite or an admission record.

`star-games-hydras-2021.pdf` is an explicitly separate primary acyclicity
proof dependency, publisher PDF https://lmcs.episciences.org/7518/pdf .
SHA256 `A653EBC3A3F33F8C19ABBC5E11E14C49F247E428A57554AB73C4A97DFCCC9883`.
Selected reading extent is20:9 and20:12--20:18, not the whole32-page
paper. `read-star-game-proof.py` and `marked-tree-source-pages/` contain
source-only reading aids. Its stronger meet-preserving embedding is
kept distinct from the1987report's ancestry-order convention.
