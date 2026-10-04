# P5 selected checker and P16 finite-abduction integration

Date: 7 September 2026 local time. Integration and readback by the lead.
This note records active routing and notation intake; independent text
reviews, production and formal admission remain separate requirements.

## Integrated source and exact snapshot

The lead read both complete body/annex pairs before completing this intake.
Their authored mathematical text is unchanged:

| File | Lines | SHA256 |
| --- | --- | --- |
| handbook/parts/p05/pa-checker-arithmetization.tex | 516 | `33195dff4bb6d2d7bd898e0af9d8ec1980a1272593139624aa17577e132c15f5` |
| handbook/annex/p05/pa-checker-arithmetization.tex | 537 | `03baf39d646901dc307812b0d22fe8823cfec53b3d7b85a3ff0adf754aaf71e5` |
| handbook/parts/p16/finite-abduction.tex | 340 | `ab9195ba7c823075cafbf3ead98efcc5cb754696f0c42d27ef108a5b9303a5ff` |
| handbook/annex/p16/finite-abduction.tex | 283 | `35b9c51f77801cbffc7b372b7dd9bb67fafc2033e29be5f29453db756c8ea2b9` |

The P5 body follows the direct numerical checker after the inherited theorem
hook is removed. The new P5 annex follows the direct numerical proof annex,
which itself follows the internal graph prerequisites. P16 now has a
substantive part driver and corresponding proof-annex chapter after P15 and
before P18. Stable identities are p16 in both routes. The main driver at this
snapshot has seventeen active parts: P1–P10, P15, P16, P18, P11–P14.

| Shared file at this integration snapshot | SHA256 |
| --- | --- |
| handbook/main.tex | `c4a8f12bf84c6360da6da39cf38e42a526e62adbbf65949c1ca0fccc77806a74` |
| handbook/parts/p05.tex | `6017629c3a54e1e063306659eec261f5b7831183662f83dc5ffb67b518e5c54e` |
| handbook/annex/p05-route.tex | `7ca80013363ca96f4bcc926c4ff33faeba47a9b6e3dd1839ccf467e30b813eee` |
| handbook/parts/p16.tex | `b8462255c289fbca14a9296ee8f7567c524a7abfac44fc5bb5f681aa3997c64e` |
| handbook/annex/p16.tex | `f60e8a47b426a42c69dfc8d903f308fa7654269a7e8cefd95ff03b9b85d0883d` |
| handbook/bib/handbook.bib | `d0aa1c02842e4ff29dd425a8c3fe95f9f12877a06a5ddd841c30c38a3cdda0f6` |
| handbook/registry/symbols.csv | `7b813370086d8b0009b4fa43243b69098d19cea57f3eef0a81dfc1b599de1766` |

These shared-file hashes describe this snapshot. Later unrelated part intake
must preserve the actual reviewed dependency scope instead of silently
presenting an earlier shared-file hash as the current file.

## Source and notation intake

The only new bibliography key is EiterGottlobAbductionManuscript. It identifies
the undated TU Wien copy with title page and printed pages 1–45. No journal
pagination, journal DOI or fabricated manuscript year is assigned. The author
source note records the actual read extent and PDF hash; the fresh source
review independently compares the actual required passages. P5 adds no new
external citation key and must be reviewed against its exact internal
description, syntax and natural-deduction dependencies.

Twenty-six typed notation rows were appended: sixteen for the selected PA
graph/library/machine/row constructions, and ten for finite abduction. Their
scopes are P5.1 and P16.1. Existing rows and anchor order were retained.
The registry now has 980 rows and 939 distinct full glyph entries. The actual
`check._hb_check_symbols` returned an empty findings object. The initial direct
call to the generator's collision helper passed its tuple return incorrectly;
the normal generator entry point was then used successfully, with no checker
change or new test suite.

```text
C:\Python314\python.exe -B tools\symbols2tex.py handbook\registry\symbols.csv tmp\edition-2026-p5-p16-integration\symbols-tables.tex
```

The isolated table hash is
`e1e0f82047dcf248e725118bbc9e6ca61566247ae45a55e86f2da5bdbbfc96af`;
the isolated symbol-index hash is
`140e06597f30fa0e2e7400f879c12c141417e84e0fd7b8c4830768c2df23ea83`.
The generator validates field grammar, scopes and collisions. These are
candidate review views; no active generated view or admitted projection was
promoted. No manuscript PDF was built or rendered during this intake.

## Review and remaining content

The independent source reviewer received the four unchanged content hashes
and these integration identities. It reviews both full LaTeX pairs and their
actual governing sources, blind to other current reviewer findings. The
fresh topic and publication reviews remain required before text acceptance.

P5's newly authored D1/D2 and exact-description claims await those reviews.
D3, proof builders and replacement of the earlier arbitrary-predicate
consumers remain open, as do the separately owed GL results. P16 supplies
only its finite atomic-hypothesis foundation and examples; other abduction,
diagnosis and causal treatments remain separate obligations. The source-unit
provenance refresh for the earlier P5 prerequisites is documented in
`spec/verification/edition-2026-p5-prerequisites-provenance-migration.md`.
