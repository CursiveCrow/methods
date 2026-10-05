# w02b-p01-014: symbol-registry apparatus units (Part 1)

Packet `work/waves/w02b/packets/w02b-p01-014.json`, mode `unit_accounting`,
label tag `p01-w02b-p01-014`. The packet owns no files and lists no editable
hosts; every host it names is read-only. Reader-text changes are therefore
submitted as patch requests in `work/waves/w02b/patches/w02b-p01-014.json`.

## Block 1: A-178-C02 (quantifier-scope promotion)

Gap from the r2 assessments (CA-w02b-w02b-p01-014-r2-b0-ED26-REQ-A-178-01-confirm):
the quantifier-scope reading rule, the worked case
`forall x P(x) -> Q(x)` = `(forall x P(x)) -> Q(x)` and the instruction to
write `forall x (P(x) -> Q(x))` were in table row 3 and running prose of
`handbook/parts/p01/symbol-registry.tex` (sec:p01-binding-precedence), outside
any hbconvention; the base precedence statement was prose too.

Existing treatments searched (A9):
- `def:p01-w02-p01-024-fixity` (notation-binding-...-w02-p01-024.tex, Part 1
  route): rank, association, equal-rank, unary fixity, dotted binders. It names
  quantifiers only in dotted forms. The new convention links it (clauses 1, 4,
  6) instead of restating it.
- `def:p01-w02-p01-024-free-bound`: occurrence-level scope and binding. Linked
  from clause 3 and the example.
- Not listed in the packet: `def:p02-fol-quantifier-scope` in
  `handbook/parts/p02/first-order-syntax-semantics.tex` line 76. It states the
  same reading rule but the file is not input by any driver (grep of
  handbook/main.tex and handbook/parts/*.tex finds no `\input` of it), so it is
  not on the Part 1 route and is not linked from the new text.

Patch requests (host `handbook/parts/p01/symbol-registry.tex`):
1. replace the opening paragraph of sec:p01-binding-precedence with a pointer
   paragraph and the numbered Convention
   `def:p01-w02b-p01-014-quantifier-scope` (Precedence and quantifier scope in
   abbreviated formulas): grammar-primacy preamble; clause 1 ranks (smaller
   ranks bind more tightly, association, equal rank via fixity clauses 1--3);
   clause 2 the operand of `forall x` / `exists x` defined by the first binary
   connective of rank > 3 outside parentheses opened after the prefix, or the
   closing parenthesis matching one opened before it; clause 3 binding;
   clause 4 stacked prefixes; clause 5 parentheses extend the scope (the
   `forall x (P(x) -> Q(x))` instruction and the parentheses-restoration rule);
   clause 6 dotted binders deferred to fixity clause 5; closing line with the
   `forall x P(x) -> Q(x)` and `exists x P(x) & Q(x)` cases.
2. table row 3 reading rule points to the convention.
3. worked-disambiguation lead-in cites the two conventions.
4. the prose "Write ... / Restore parentheses ..." sentences replaced by a
   pointer to clauses 2 and 5 and to the example.
5. insert after the FV paragraph the Example
   `def:p01-w02b-p01-014-two-readings`: operand determination for
   `forall x P(x) -> Q(x)`, FV of both readings, and a two-element structure
   (dom {0,1}, P = {0}, Q = empty) in which the abbreviated reading is
   satisfied under every assignment and the other reading under none.

No new symbols (all glyphs are registered: forall, exists, to, land, neg,
FV, dom, entails, mathcal M). No citations: the convention is the handbook's
own normative notation rule, not a source presentation. No result is
asserted, so no annex item is needed.

Verification done in a scratch copy (not in the tree): the five patches were
applied to a copy of symbol-registry.tex, which compiled twice with pdflatex
(TeX Live 2025) inside a book/handbook.sty wrapper with no errors and with
both new labels resolved (the remaining undefined references are labels in
other route files absent from the wrapper); `tools/find_fused_spaces.py` on
the patched copy reports nothing; `tools/check.py --tree handbook --root
<copy>` gives the same finding list as the unpatched tree.
`tools/waves.py unit-compile` refuses this packet ("packet lacks owned body
and annex .tex files to compile").

## Other components (not addressed in this block)

Per the r2 assessments, the remaining open items need changes outside any
file this packet may edit (tools, generated files, canonical registry,
restoration captures, other packets' files) or need an unheld source:
- A-160-C02, A-160-C03, A-167-C01, L-018-C02, L-018-C03, L-018-C04, L-018-C05,
  S-002-C02, S-002-C03, S-002-C04: lead-owned changes (see return file).
- ED26-SRC-043-0902-C001: Jech, Set Theory, Academic Press 1978, printed
  pp. 289--291 is not in held-sources.json (no "Jech" entry).

## Block 2: G1 guard, L-018-C03 (Part 1 host longtables), S-002-C02 bridge

G1 guard failures reported at the start of this block:
- `spec/research/edition-2026-p01-symbol-registry-w02b-p01-014.md` and
  `-return.json` are this packet's mandated note and return; they are flagged
  because the packet's `owned_files` is empty and the snapshot
  (`work/waves/w02b/snapshots/w02b-p01-014.json`, created 2026-10-04T18:31:18Z)
  predates them. Not removable without losing the mandated record; the fix is
  lead-side: add both paths to the packet's owned_files (as `_owned_files` in
  tools/waves.py does for section packets) and re-take the snapshot.
- `spec/research/edition-2026-p02-fol-metatheorem-table-and-nd-cpl-sheet-w02b-p02-036{.md,-return.json}`
  were not written by this packet; they are packet w02b-p02-036's note and
  return (that packet also owns no files, so they are absent from
  wave_packet_paths and land on this packet's G1 scan). Not touched.

Patch requests added (entries 6-9 of `work/waves/w02b/patches/w02b-p01-014.json`,
host `handbook/parts/p01/symbol-registry.tex`):
6-8. tab:p01-classical-symbols, tab:p01-precedence, tab:p01-letter-families:
   continued caption after `\endfirsthead`, a `continued` foot and an empty
   last foot, matching tab:p01-sixteen.
9. after the editorial-defaults paragraph: typed distinction and bridge for the
   inherited structure-domain bars (sec:fol-semantics-01, thm:downward-ls):
   bars on a structure = domain, `|M| = dom M`; in `||N||` inner = domain,
   outer = cardinality; editorial form `|dom N|`.

Verification (scratch copies only): all nine patches applied to a copy of the
host; pdflatex (TeX Live 2025) in a book + handbook.sty wrapper, twice, no
errors; with each table body repeated twelve times the rendered PDF shows 9, 11
and 23 continuation captions and 43 `continued` feet; find_fused_spaces: no
hits; check.py --tree handbook --root <copy>: identical finding list with and
without the patches. unit-compile refuses (no owned .tex).

Longtable scan (scratchpad lt.py, all handbook .tex): 116 longtables lack a
continued caption and/or a continued foot; outside this host they are in
generated/ (audit-pNN, symbols-tables: generator change), restoration/ (6),
and other packets' or unassigned part files (listed in the return).

## Block 3: A-178-C02 re-raised (r3 assessment)

The r3 assessment repeats the A-178-C02 gap: the quantifier-scope reading is
still prose/table text at symbol-registry.tex 137-139 and 160-182 and no
route hbconvention states it. Cause: patch entries 1-5 (block 1) are not yet
applied to the host; the host text is unchanged (git log shows no edit since
the recovery commit). The packet owns no files, so the convention cannot be
placed on the route by this packet; it needs the lead to apply entries 1-5.

Re-verification this block (scratch copies only):
- all nine anchor quotes occur exactly once in the current host, so the
  entries still apply as written;
- patched copy compiled twice with pdflatex (TeX Live 2025) in a book +
  handbook.sty wrapper: no errors; def:p01-w02b-p01-014-quantifier-scope and
  def:p01-w02b-p01-014-two-readings resolve; every target the patch text
  cites exists on the route (def:p01-w02-p01-024-fixity clauses 1-5 as
  numbered there, def:p01-w02-p01-024-free-bound,
  thm:p01-w02-p01-024-fv-occurrence, tab:p01-w02-p01-024-ranks,
  sec:fol-semantics-02 via parts/p02.tex -> restoration/scope-SRC-03519-03680,
  macros \dom, \FV, \entails in handbook.sty);
- find_fused_spaces on the patched copy: no hits;
- check.py --tree handbook --root <copy>: 3283 lines before and after
  patching, no difference, no finding naming symbol-registry.tex;
- unit-compile: refused ("packet lacks owned body and annex .tex files").

## Block 4: G1 re-raised; policy-text patches

G1 (r3-b1 verify): the same four paths as block 2. Not fixable inside this
packet: the packet's owned_files and editable_hosts are empty, so its mandated
note and return (spec/research/edition-2026-p01-symbol-registry-w02b-p01-014.md,
-return.json) are outside the allowed set by construction, and the w02b-p02-036
note and return belong to that packet (not written or touched here). Removing
this packet's two files would not clear G1 (the p02-036 hits remain) and would
lose the record the task requires. Lead fix: give unit_accounting packets
their note and return as owned files (tools/waves.py `_owned_files` pattern),
or exempt spec/research/edition-2026-*-<packet id>{.md,-return.json} from the
G1 scan for the matching packet, and re-take the snapshot.

r3 assessments: every open gap is recorded as lead_owned; no gap is
addressable in a file this packet may edit. Added patch entries 10-11 for the
defect observations of the r3 A-167/S-002 assessments:
10. handbook/CONVENTIONS.md symbol-registry seed sentence: the bar,
    equivalence and forcing rulings restated as house defaults for editorial
    notation, with the section 7 obligation for declared source-local roles.
11. handbook/handbook.sty `bs` comment: "cardinality only" replaced by
    "cardinality (house default); source-local roles ... registered".
All eleven anchors occur exactly once in the current hosts.
unit-compile: refused ("packet lacks owned body and annex .tex files").

## Continuation

- A-178-C02: patch requests 1-5 (block 1), re-verified in block 3 against
  the current host; they close the r3 gap only once the lead applies them. L-018-C03 (this host): patch
  requests 6-8. S-002-C02: Part 1 bridge, patch request 9. Route text is
  unchanged until the lead applies them.
- Lead-owned remainder, exact changes in the return file: packet ownership of
  the note/return (G1); generator for the Part 1 tables (A-160-C02); registry
  notation lint (A-160-C03); symbols.csv row for the inherited domain bars
  (S-002-C03/C04, A-167-C01); captions in tools/symbols2tex.py and the
  audit-table emitter (L-018-C02/C03); longtables in other files (L-018-C03);
  a main.tex build for rendered multi-page evidence (L-018-C04).
- Policy-text corrections for A-167-C01/S-002: patch entries 10-11 (block 4).
- ED26-SRC-043-0902-C001 remains blocked_source (Jech 1978 pp. 289-291).
