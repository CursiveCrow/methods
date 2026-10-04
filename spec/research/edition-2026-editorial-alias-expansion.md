# Editorial alias expansion preserving the printed mathematics

Date: 7 September 2026 local time. The existing scoped manuscript scanner
found source-only command tokens in the new P16 and P17 editorial files.
The same commands raise actual package errors outside inherited restoration
wrappers in handbook.sty. No style rule or validator was relaxed.

## Exact replacement rule

The source guards at handbook.sty lines 824–852 and 1067–1072 give these
printed forms: Prop is mathsf{Prop}; True is mathbf{T}; False is mathbf{F};
R is mathbb{R}. The new editorial text now writes those exact expressions
literally. The inherited source, wrappers and source macro definitions are
unchanged. The intended symbols, types, definitions, formulas and proofs
therefore remain the same, while the source-only command calls are removed.

| File | Replacements | Previous SHA256 | Current SHA256 |
| --- | --- | --- | --- |
| handbook/parts/p16/finite-abduction.tex | 5 Prop, 2 False, 4 True | `ab9195ba7c823075cafbf3ead98efcc5cb754696f0c42d27ef108a5b9303a5ff` | `19e88af8c80b63a7125fe61b3fe9ce192564ca02456a61020570ad4c6b7b9bc9` |
| handbook/annex/p16/finite-abduction.tex | 4 Prop, 2 False, 2 True | `35b9c51f77801cbffc7b372b7dd9bb67fafc2033e29be5f29453db756c8ea2b9` | `9965ee04ce9f0d7f9a6cc786cee9355bc0e7b1403803a61af745087c1c06d893` |
| handbook/parts/p17/finite-preferences.tex | 11 R | `7c70f6c3428efd358bdfdd99ba03911699dd7a4a16179033b408b9f9be2ad988` | `58cfd946f16a9d068d0d81af3262e26bbe926f87ffef45c01cadd72e0dd0927c` |
| handbook/annex/p17/finite-preferences.tex | 5 R | `30faeddd5023d3f64a565fa669c47980de325a2bfecb6f96acaed9398e204fe1` | `dfa00cc716098da6bf6076fef0258a4180dd868358561ac56e12cf96b925d9df` |
| handbook/registry/symbols.csv | 1 R in the newly added P17 glyph | `0f2efca2f92e7b967f3be3efa137c9dc36f9ad64ba314e987a48ad4817c4a14b` | `0f404db829e704a9166a4b219498003ab1217a72eb5b7f579e65b5c402774c47` |

Token-boundary matching avoids changing longer command names. The operation
prepared exact patches and applied each through the file-editing tool.
Line counts, labels, statements, examples and source citations are unchanged.
The four author/intake snapshots remain evidence for the earlier text and
must be read with this explicit current-version mapping.

## Actual affected checks

The first scoped file scan reported 35 source-command occurrences, nineteen
in P16 and sixteen in P17. After the replacements, the same eight-file
scan returned an empty findings object. Symbol checks report 1,002 data rows
and 961 distinct full glyph entries; bibliography checking sees 635 keys and
zero intake stubs. All fifteen declared proved-status pairs exactly match
the fifteen annex label/backreference pairs.

The existing symbols2tex generator passed with explicit isolated output
under tmp/edition-2026-kamp-l2-p17/. The current table hash is
`addda71cdcbffed7af0f4b25ad44acdc4ce7d3b1936ff6edadb3bf0123a68d91`;
the symbol-index hash is
`5a672feb30559f607fe5876bf73a71c1b4e5aa2a746619795ca065077866aa4a`.
No active generated view was promoted. No new checker, mirrored prose test,
manuscript build or PDF render was used to make this repair.

The independent publication reviewer is checking complete inverse preservation
and the exact source macro expansions. This note records the mechanical edit
and actual affected checks; the independent report supplies acceptance of
the preservation claim. Full production and formal admission remain separate.
