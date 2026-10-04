# Scoped static checks for four integrated units

Date: 7 September 2026 local time. This scope is the eight maintained LaTeX
files for the selected PA checker, finite abduction, finite preferences and
Kamp III.2 Lemma 2. The final identities are recorded in their integration,
source-repair and editorial-alias-expansion notes.

The lead invoked the existing check._hb_scan_file on each of those eight
actual files, followed by check._hb_check_symbols and check._hb_check_bib
against the canonical registry and bibliography. The first scan identified
35 calls to source-only Prop, True, False and R aliases in new editorial
files. Their exact printed expansions were substituted directly; the shared
style and checker were unchanged.

The repeated affected check returned exit code zero and findings {}.
It recorded 1,002 symbol rows, 961 distinct full glyph entries, 635
bibliography keys and zero intake stubs. A direct equality comparison of
declared (theorem owner, proved target) pairs with (annex backreference,
annex label) pairs found exactly fifteen reciprocal pairs and no difference.
The independent text reviewers also inspected their actual prerequisites
and body/annex routing at the recorded scopes.

The normal symbols2tex entry point then generated only isolated views under
tmp/edition-2026-kamp-l2-p17/, passing its field grammar, scope and collision
validation. Its current identities are in
spec/research/edition-2026-editorial-alias-expansion.md.

These are narrowly scoped file, symbol, citation-key and reciprocal-status
checks. They are not the full handbook check: no whole-book cross-reference
closure, semantic validation, layout, build, PDF inspection or admission is
established. The separate full source-unit join still fails at source unit
740, SRC-10675-10769, after passing the refreshed P5 records. P19 is still
absent from the active main route. The final handbook PDF remains an older
publication artifact.
