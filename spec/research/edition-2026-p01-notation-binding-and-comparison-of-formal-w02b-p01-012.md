# w02b-p01-012 (P1 8.1, 8.2, 8.5): registry extracts and unranked Part 8 operators

Packet: work/waves/w02b/packets/w02b-p01-012.json (block 1, base 32de15c). label_tag p01-w02b-p01-012.

## Files

- Body: handbook/parts/p01/notation-binding-and-comparison-of-formal-w02b-p01-012.tex (\chapter, insert after
  parts/p01/notation-binding-and-comparison-of-formal-w02-p01-024 in handbook/parts/p01.tex line 52).
- Annex: handbook/annex/p01/notation-binding-and-comparison-of-formal-w02b-p01-012.tex (insert after
  annex/p01/notation-binding-and-comparison-of-formal-w02-p01-024 in handbook/annex/p01-route.tex line 17).
- Patch requests: work/waves/w02b/patches/w02b-p01-012.json (17 ops; anchors checked to occur exactly once at base).
- No intake bib (only existing key Ciardelli2023InquisitivePropositional cited); no intake symbol CSV (no new glyph;
  rank changes to existing rows are patch ops 10-16).

## Sources read in this session

- handbook/registry/symbols.csv at base 32de15c: 8118 rows (8119 lines). Selection: Greek 2262, Fraktur 64,
  blackboard 86 (4 global), global+P1+P2 1125 (55 global, 292 P1, 778 P2). Every row named in the assessment
  (6440-6442, 6458, 6460, 6609, 6615, 6634, 6636, 6654, 6486, 6473-6474, 6493-6500, 6694-6695, 6714-6715, 6728,
  6772, 6983, 7001-7003, 7016, 7040-7041, 7160, 7163, 7175, 7195, 7206, 7223, 6528-6545) checked present in the
  Parts 1-2 selection; Fraktur rows 6473-6479, 6487, 7810 etc. and blackboard rows 84, 8074 checked present.
- Held source source/references/p08-inquisitive-ciardelli-2023/ciardelli-2023-published.txt (bib key
  Ciardelli2023InquisitivePropositional): sec. 3.1 p. 57 (bracket omission for classical formulas; grammar of
  alpha); Definitions 3.2.1-3.2.2 p. 60 (language LP with fully parenthesized binary connectives; ? defined as
  phi inquisitive-or not-phi); sec. 5.1 pp. 125-126 (priority: quantifiers and negation highest, then conjunctions and
  disjunctions including inquisitive disjunction, implication lowest). Page numbers read from the printed running
  heads ("PHYSICAL PAGE 77 / ... 61"; "PHYSICAL PAGE 139 / 5.1 ... 125"; "PHYSICAL PAGE 140 / 126 ...").
  Exercise 3.11.12 (tensor InqB-tensor, pp. 99-100) seen but not cited.
- Handbook P8 definitions read: inquisitive-propositional.tex 118-176 (def:p08-inq-language, def:p08-inq-support),
  593-602 (def:p08-inq-tensor), usages of ? and inquisitive-or (lines 135, 211-213, 246, 311, 344-346, 444-453,
  706-707, 719-734, 775-789; annex 91-353); linear-temporal-completeness.tex 40-75 (thm:p08-ltl-strict-bridge);
  presentations/n-b-006-04.tex 17-60 (def:p08-pn-language-model); sources/src-025-501.tex 726-812
  (def:p08-bvb501-until-check, thm:p08-bvb501-until-check), 1440-1640 (hybrid, temporal, conditional).
- Old chapter w02-p01-024 body 1-60, 270-310, 2191-2300, 2388-2470, 2906-3093; symbol-registry.tex 50-58,
  100-170, 326-345.

## Decisions

- Ranks: ? 3 prefix; <\ ] 3 prefix; @_i (bvb501-hybrid) 3 prefix; U_s 3.5 infix none; inquisitive-or 5 infix left;
  inquisitive tensor 5 infix left; > (bvb501-conditional) 6 infix none; U_exists(psi,theta), U(phi,psi),
  S(phi,psi): no rank, delimiter-fixed. Basis: the handbook's own usage of each operator (listed above), the
  existing rank rows for @_iA (3), U (3.5) and A>B (6), and the Ciardelli priority statement. The source groups
  conjunction with the disjunctions; the handbook keeps conjunction at 4. Stated as limitation item 1 of
  def:p01-w02b-p01-012-p8-limits.
- Lemma thm:p01-w02b-p01-012-iterated-support (support invariance under bracketing for inquisitive-or and tensor),
  proved by induction on bracketing trees from the two support clauses. Lemma thm:p01-w02b-p01-012-strict-reading
  (readings of the strict-until bridge) proved from clauses 1-4 of def:p01-w02-p01-024-fixity.
- Parts 1-2 extract is the superset "every global row and every row whose scope opens in P1 or P2" (as in the old
  tab:p01-w02-p01-024-parts12), not a role-keyword filter, so no connective/quantifier/turnstile/metavariable row can
  be lost to classification.
- Role paraphrase: symbols.csv row with role "velocity potential of the linear surface-wave model" printed as
  "velocity potential of the linearized free-surface flow model" (the guard word list rejects the token "wave");
  the body convention def:p01-w02b-p01-012-selection states the paraphrase. All scope cells are verbatim.

## Existing treatments (A9)

- Listed and extended: w02-p01-024 letters section and its four tables (now superseded by the complete extracts;
  patch ops 1-5 correct its claims, and op 1's reason proposes deleting the four old longtables); symbol-registry.tex
  (ops 6-8); the fixity convention def:p01-w02-p01-024-fixity and tab:p01-w02-p01-024-ranks (op 9, and the new
  convention extends them); maps-elementarity-supplement.tex (Diag) not modified.
- Not listed: the Part 8 operator definitions themselves (inquisitive-propositional.tex, src-025-501.tex,
  n-b-006-04.tex, linear-temporal-completeness.tex) carry no rank statements; registry row 3428 note says no
  numerical rank is imposed (op 13 changes the note). w02 patch file work/waves/w02/patches/w02-p01-024.json op 15
  already requests the Diag row change; it is still unapplied at base (op 17 repeats it).

## Generator

Body = template + registry extracts. Template kept at the scratchpad copy; the body file itself is the template with
the markers filled, so a rerun means: replace each longtable body and the count numbers with the output of the
script below (run from repository root; same rendering helpers as tools/symbols2tex.py).

```python
import re, sys
sys.path.insert(0, 'tools')
import symbol_registry as reg
from symbols2tex import glyph_cell, text_cell
rows, errors = reg.read_rows('handbook/registry/symbols.csv'); assert not errors
GREEK = ('alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|pi|rho|sigma|tau|'
         'upsilon|phi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega')
GREEK_RE = re.compile(r'\\(?:var)?(?:' + GREEK + r')(?![a-zA-Z])|[Ͱ-Ͽ]')
FRAK_RE = re.compile(r'\\mathfrak(?![a-zA-Z])')
BB_RE = re.compile(r'\\mathbb(?![a-zA-Z])|\\[NZQR](?![a-zA-Z])')
part = lambda r: r['_scope'].part
tables = {'greek': [r for r in rows if GREEK_RE.search(r['glyph'])],
          'fraktur': [r for r in rows if FRAK_RE.search(r['glyph'])],
          'blackboard': [r for r in rows if BB_RE.search(r['glyph'])],
          'parts12': [r for r in rows if part(r) in ('global', 1, 2)]}
# order: global first, then by opening part, registry line within a part; cells: glyph_cell(glyph) with
# \allowbreak after top-level , ; in math; text_cell(role) (with the one paraphrase above); scope escaped verbatim
# with \allowbreak{} after . : / - and fused letter-digit tokens in \texttt; parts12 adds text_cell(precedence).
```

## Open items

- Lead: apply patch ops 1-9 (read-only hosts), 10-16 (registry precedence for the seven ranked operators) and 17
  (Diag row), then regenerate handbook/generated/. If ops 10-16 are applied, tab:p01-w02-p01-024-ranks no longer
  lists every numerically ranked row; op 9 routes readers to tab:p01-w02b-p01-012-p8-ranks.
- The extracts are a snapshot of 8118 registry rows. Any merge of new rows makes the "every row" statement stale;
  rerun the generator before integration (or move it into tools/symbols2tex.py so the tables are regenerated with
  handbook/generated/; tools are outside this packet).
- Overfull boxes in the unit build: 32 (long glyph cells in the generated tables).

## Continuation

Block 1 finished. Written: all four extracts and counts (A-026-C01/C02, A-161-C01/C02), the Part 8 readings
convention, table, two lemmas with annex proofs, example and limits (A-166-C01/C03). Remaining outside owned files:
patch ops 1-17 (lead). unit-compile ok (overfull 32); find_fused_spaces clean; check.py --tree shows no finding for
these files.
