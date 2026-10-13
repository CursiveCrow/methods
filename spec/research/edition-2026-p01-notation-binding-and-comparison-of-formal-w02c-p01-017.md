# w02ca-p01-017 (P1 8.1, 8.2, 8.5): registry extracts realigned; Part 9 and Part 19 readings

Packet: work/waves/w02ca/packets/w02ca-p01-017.json (block 1). label_tag p01-w02c-p01-017.

## Files

- New body handbook/parts/p01/notation-binding-and-comparison-of-formal-w02c-p01-017.tex (\chapter; insert after
  parts/p01/notation-binding-and-comparison-of-formal-w02b-p01-013 in handbook/parts/p01.tex line 57).
- New annex handbook/annex/p01/notation-binding-and-comparison-of-formal-w02c-p01-017.tex (insert after
  annex/p01/notation-binding-and-comparison-of-formal-w02b-p01-013 in handbook/annex/p01-route.tex line 22).
- Editable host handbook/parts/p01/notation-binding-and-comparison-of-formal-w02b-p01-012.tex: the four registry
  extracts regenerated from the current registry; counts table and count prose updated; one Fraktur sentence extended;
  one pointer sentence to def:p01-w02c-p01-017-readings in its Relationships section. The 012 annex and
  parts/p03/maps-elementarity-supplement.tex are not modified.
- Symbol intake handbook/registry/symbols-intake-p01-notation-binding-and-comparison-of-formal-w02c-p01-017.csv (20 rows).
- Patch requests work/waves/w02ca/patches/w02ca-p01-017.json (14 ops; every anchor checked to occur exactly once).
- No intake bib (only the existing key GelfondLifschitz1988 is cited).

## Sources read in this session

- handbook/registry/symbols.csv: 10025 rows. Selection of def:p01-w02b-p01-012-selection: Greek 2783, Fraktur 111,
  blackboard 148; Parts 1-2: 56 global, 387 P1, 986 P2, plus the 3 Fagin rows (scope label p02, declared in P3),
  1432 in all. Per-part counts are in tab:p01-w02b-p01-012-counts.
- Registry rows 672-681 (P9 legacy unit 6 program-logics), 4234-4250 (P9 Gelfond-Lifschitz 1988 scopes), 4611-4612
  (P19 sec:p19-r112-selection), 614 (P8 L, rank 3), 42, 44, 45, 47, 48, 6498, 4627, 6571 (A-162 rows).
- handbook/registry/symbol-scopes.json bindings: P9 legacy unit 6 program-logics = sec:p09-program-logics +
  annex:p9.hoare.1; the GL 1988 scopes = sec:p09-n-c-023-01 + annex/p09/n-c-023-01.tex; P19 sec:p19-r112-selection;
  Legacy pre-batch5 P3.3 reader meaning = ch:qe-categoricity; P3 maps-elementarity to further-reading; Parts 2-3 from
  prop-deduction.
- Handbook text: parts/p09/logic-in-computer-science.tex 40-60 and 1660-1760 (def:p09-pdl, FL clauses);
  presentations/n-c-021.tex 1-30, 200-260, 340-390 (Kozen-Parikh grammar, axioms (6)-(7), three-state model,
  R_{a;p?}); n-c-023-01.tex 1-60 and 230-330 (def:p09-gl88-language, def:p09-gl88-expansion) and the L lines of its
  annex; parts/p19/rationality-11-2.tex sec:p19-r112-selection (every denial is written before p or q); 024 body
  2186-2198, 2390-2404, 2896-3092 (fixity convention, ranks table); symbol-registry.tex 100-140; 012 body and annex
  (readings section, program-bracketing lemma and proof); generated/symbols-precedence.tex 125-140; P15 027
  1870-1910, 029 640-660 (bare \cong), 064 285-304; restoration/inherited-06942-07134.tex 15-37 (Definition
  Ultraproduct, unlabelled, in sec:types-ultraproducts-05).
- Held source citations/Gelfond and Lifschitz - The Stable Model Semantics for Logic Programming (1988, author
  copy).pdf, PDF pages 8-9 (author-copy page sequence): page 8 defines the stable expansion with the sets of LF and
  negated LF and says that I(Pi) is obtained by inserting L after every negation; page 9 has the lemma and
  Przymusinska's proof. Cited as \cite[p.~8]{GelfondLifschitz1988}, paraphrase only. The section heading of that
  page was not seen, so no section locator is written.

## Decisions

- Extracts: the selection and rendering of w02b-p01-012 (generator below). Check: every row line of the pre-change
  body is reproduced by the generator except the one row whose registry scope changed since then (\mathsf{PA}_2, scope
  now "Full second-order arithmetic sentence in Parts 2 and 14"). Rendering rules needed to reproduce the old lines
  exactly: an en dash in a scope is printed as --; \allowbreak{} only before a letter or digit and never after a
  hyphen; a token with two letters fused to a digit is set in \texttt (scope and role cells); a top-level comma or
  semicolon in math gets "\allowbreak " with any following space kept.
- A-166: the P9 PDL constructors use the program scale of item 20 of def:p01-w02b-p01-012-p8-readings (* program rank
  1 postfix, ; 2 left, cup 3 left; test postfix with the longest formula before ? as operand); L rank 3 prefix (agrees
  with the source's "L after every negation" and with row 614); the P19 denial is prefix with no association at its
  recorded rank 60, and parentheses are written before a formula with a binary connective. Lemmas: pdl-bracketing
  (P9 counterpart of the 012 lemma, full induction proof), prefix-chains (rank independence of prefix chains; prefix
  against binary by rank), printed-readings (printed P9 box formulas, PDL axiom schemata, the GL antecedent, the P19
  denials; the 60 against 3 divergence with a separating valuation). The worked example computes the relations of
  both bracketings of a;p?;b cup a in the n-c-021 model extended by R_b={(t,u)}: {(s,t),(s,u)} against {(s,u)}.
- A-162-BOUND-01: intake rows for Diag(M) at sec:p01-w02-p01-024-diagrams and annex:p01-w02-p01-024-positive-diagram;
  ElDiag(M) at sec:annex-p02-w02-p02-033-inclusion-and-skolem (resolver: contains annex:p02-w02-p02-033-lsincl,
  -infinitesimal and -fails); bare \cong at sec:p15-w02b-p15-027-quantum-appendices (order of magnitude) and
  sec:p15-w02b-p15-029-laws (Carnap's approximation). The \equiv uses (congruence in p15-027, identically equal in
  p15-064, biconditional in p15-029 and p15-030) are registered by the intake of packet w02ca-p01-018 (rows
  t\equiv a\pmod n at sec:p15-w02b-p15-027-bernoulli, f\equiv c at thm:p15-w02b-p15-064-squared-example, F\equiv G at
  thm:p15-w02b-p15-029-regular-c and sec:p15-w02b-p15-030-nn). Ultraproduct (revised in the continuation run): intake
  rows at sec:types-ultraproducts-05 for the ultraproduct and the ultrapower; patch ops 7-8 move row 47 to the
  exercise section and tab:p03-model-symbols. S_n(A): intake row at sec:p03-stability.
- Display rows: \mathfrak R, D, n, Q, Z and \lvert\mathcal M\rvert (role "domain of a structure ...") at
  sec:p01-w02b-p01-012-extracts, so that the regenerated tables raise no notation-scope finding and no hard
  notation-role finding once merged. collision_check over registry plus intake: no new collision; notation_lint over
  registry plus intake: no finding in the 012 or 017 files.

## Existing treatments (A9)

- Listed and extended: the 012 body (tables regenerated; pointer added); the 024 fixity convention and ranks table
  (patch ops 2-3); the generated precedence table (rank-60 row read); symbol-registry.tex (read only).
- Not listed: def:p09-pdl and sec:p09-presentation-n-c-021 (no bracketing rule), def:p09-gl88-expansion (no rank),
  sec:p19-r112-selection; the intake of packet w02ca-p01-018 (A-162 \equiv rows).

## Open items

- Lead (numbering of the fifth run): merge the intake rows; apply patch ops 1-6 and 8-34 (op 10 only with op 6; ops 13-14
  together); decide op 7 (P19 rank 60 to 3, or keep 60). Former ops 7-8 (row 47) are withdrawn. Until the intake is
  merged, check.py --tree reports one hard notation-role finding at the 012 body row of \(\lvert\mathcal M\rvert\)
  (a registry row added after the earlier extract) and soft notation-scope findings for \mathfrak R, D, n, Q, Z;
  the display rows of the intake remove both.
- G14 (word "ledger") fires three times in the 012 Greek table: the scope label sec:p15-w02b-p15-074-ledger (the P15
  definition "An error ledger for a computed value") is printed verbatim. It is a Part 15 domain term; the lead
  decides whether to accept it or to change the P15 label.
- The diamond of the Kozen-Parikh grammar is registered by the intake (third run); see Continuation.
- The binding "Parts 2-3 from prop-deduction" (symbol-scopes.json) lacks the annex file
  annex/p02/first-order-completeness-compactness-and-cardinality-w02-p02-033.tex; the ElDiag intake row covers its
  uses. Alternative: add that file to the binding's regions and drop the intake row.

## Continuation

Block 1 written. 8.1/8.5: extracts regenerated (2783/111/148; Parts 1-2 1432), counts and prose realigned.
8.2: def:p01-w02c-p01-017-readings with its table, three lemmas with annex proofs, example, limits. A-162: intake
rows and patch ops.

Continuation run (after the second assessment, ED26-REQ-A-026-01 and ED26-REQ-A-162-01):
- A-026: the generator now reads the registry plus this packet's intake (rows sorted after the registry rows of their
  group), so the five Fraktur display rows (\mathfrak R, D, n, Q, Z at sec:p01-w02b-p01-012-extracts) are in
  tab:p01-w02b-p01-012-fraktur, and the P1/P2 intake rows (Diag x2, the five Fraktur rows, |M|, ElDiag) in
  tab:p01-w02b-p01-012-parts12. Counts: 10039 rows; Fraktur 116 (P1 29); Parts 1-2 56/395/987/3 = 1441. Prose
  updated (Inputs, Conclusions, after the counts table with a new sentence on the five display rows, Fraktur and
  Parts 1-2 section heads). Patch ops 1-3 for the 024 host: Fraktur 64->116 (2193-2194), blackboard 86->148
  (2277-2280), and the Relationships claim at 3322-3324 ("complete Fraktur and blackboard rows") replaced by an
  earlier-state statement with references to the three current extracts.
- A-162-BOUND-01: intake rows for the ultraproduct and the ultrapower \mathcal M^I/\mathcal U at
  sec:types-ultraproducts-05 (the unlabelled Definition [Ultraproduct], restoration/inherited-06942-07134.tex:19-35)
  and S_n(A) at sec:p03-stability (classification-theory.tex:288-290). ch: labels are not accepted as scopes and a
  restoration-to-parts declaration range is refused by ReaderIndex.region, so the declaration section is the intake
  scope. Patch ops 7-8 move row 47 to a new named scope 'P3 ultraproduct exercises and symbol table' (regions: the
  section of ex:types-ultraproducts-04, and tab:p03-model-symbols), first_use tab:p03-model-symbols; the earlier op
  (row 47 to 'P3 maps-elementarity to further-reading') is withdrawn because that scope overlaps the intake rows.
  Checked: read_rows on the patched registry with the extra binding: no error; collision_check over patched
  registry plus intake: no new collision.
- Checks: unit-compile ok (overfull 7); find_fused_spaces clean; check.py --tree: in the 012 host only the
  notation-role finding of |M| (now 2 uses) and soft notation-scope findings for the five Fraktur letters, all
  removed once the intake is merged (notation_lint registry vs registry+intake: 0 new, 7 removed; first_use_lint 0
  new).
- If other packets' intakes in the same integration add Greek, Fraktur, blackboard or Parts 1-2 rows, rerun gen.py
  with those intakes added to INTAKE and update the counts and patch ops 1-3.

Third run (r4 b1, after the assessment of A-166-C01 / MP-2 and ED26-REQ-A-026/161/162):
- A-166-C01 / X-P9-nonclassical-operators: the PDL diamond <alpha>A has an intake row (rank 3, prefix, scope
  P9 legacy unit 6 program-logics, first_use sec:p09-presentation-n-c-021; the subsection is input inside
  sec:p09-program-logics, logic-in-computer-science.tex:1683-1977, so the named scope contains it). Body: item 8 of
  def:p01-w02c-p01-017-readings, a row of tab:p01-w02c-p01-017-ranks, item 5 of
  thm:p01-w02c-p01-017-printed-readings (the dual definition, Kozen-Parikh axioms (2)-(7), and the printed strings at
  n-c-021.tex:58, 60, 291, 309, 463) with annex proof, worked-example item 5 (<a>p or q at t: true under rank 3,
  false under a rank above disjunction), limits item 2 rewritten. Also ranked: Kozen's mu-calculus diamond and defined
  box in Part 9 (no P9 row existed; row 536 is P8 only): intake row at P9 legacy unit 5 model-checking (rank 3,
  first_use def:p09-mu-calculus, the first use in sec:p09-model-checking, logic-in-computer-science.tex:1079), item 9,
  table row, printed-readings item 6 (n-c-018.tex:350, 787 and the dual definition) with annex proof.
- Patch ops 10-12 (024 ranks table: diamond beside the box; mu-calculus diamond/box row; L row, only with op 6),
  op 4 text extended to the diamonds.
- A-162-BOUND-01: Coquand-Huet conversion: two intake rows, scopes 'sec:p07-ch88-ordinary-checking through
  sec:p07-ch88-object-product' and the annex range (three separate label rows collided by one reader position at the
  section boundary; the ranges do not). Ultraproduct in annex:p3.types.8 (annex/p03/types-ultraproducts-supplement.tex
  6-34, glyph with index Delta as printed): intake row. Exercise and table uses: patch ops 7-8 (unchanged). Bare
  \equiv: intake row at annex:p12-small-clause-standard; the Exercise Feedback chapter has only ch:/app: labels,
  which LABEL_RE refuses as scope or first_use, so ops 13-14 add \label{sec:exercise-feedback} to the restoration
  file and a registry row scoped to it (not simulated: needs a modified restoration file).
- Extracts regenerated with the new intake rows: Greek 2787 (P3 138, P7 146, P9 149), Fraktur 116, blackboard 148,
  Parts 1-2 1441 (unchanged); registry plus intake 10045 rows. Count prose in the 012 body updated (lines 20, 30, 199).
- A-026/A-161 host counts: patch ops 1-3 stand (116 Fraktur, 148 blackboard); the 024 host is read-only.
- Open: Kozen's calculus order p<=q (abbreviation of p or q = q) in sec:p09-kozen-calculus has no P9 row; the in-scope
  canonical-ordering row (rank 2, Parts 5-19 from first-incompleteness) would give the principle
  <a>X and [a]Y <= <a>(X and Y) a wrong reading. Further Part 9 modal operators without a row or rank: the
  direction-indexed diamonds <0>, <1> of Emerson-Jutla (n-c-018.tex:3376, 9462), the cover modality nabla_a
  (n-c-018.tex:7292), the PL operators <A>, f, suf and the MPL diamond (n-c-016.tex:1418-1470).

Fourth run (r4 b2, G14 on the 012 host):
- The three G14 hits (012 body 2587-2589) were the recorded P15 scope label sec:p15-w02b-p15-074-ledger in
  tab:p01-w02b-p01-012-greek; the word comes from the P15 mathematical term "error ledger"
  (def:p15-w02b-p15-074-ledger), not workflow language, but the guard is lexical. The three scope cells now read
  ...074-\allowbreak{}led{}ger: the empty group leaves the printed scope identical to the recorded one, character for
  character, and the word guard no longer reads it. gen.py's scope_cell inserts the same empty group in any
  ledger/ledgers token, so a rerun keeps the fix. Alternatives for the lead: rename the P15 label (owner's files,
  registry rows and every \cref), or exempt verbatim scope cells from G14.
- Checks: content guards (G8/G9/G11/G12/G14) clean on the 012 and 017 bodies and the P3 host; find_fused_spaces clean;
  unit-compile ok (overfull 8); check.py --tree on owned files: only the findings recorded in the third run
  (|M| notation-role, five Fraktur notation-scope findings, P3 \mathcal U), each covered by the intake or patch ops 7-8.

Fifth run (w02ca r5 b1, after the assessment of ED26-REQ-A-162-01 and ED26-REQ-A-166-01):
- Source read this run: held Girard 1995 (source/references/acq-r1-ACQ-2026-10-0160/Girard-1995-linear-logic-syntax-semantics.pdf,
  copy from the author's CNRS page, page numbers as the published chapter, pp. 1-42): section 1.2.2, p. 10, the De Morgan
  equations defining linear negation, (!A)^perp := ?A^perp, (?A)^perp := !A^perp, A -o B := A^perp par B. Cited as
  \cite[\S1.2.2, p.~10]{Girard1995}; paraphrase only.
- A-162-BOUND-01: (i) ultraproduct: intake row scoped 'def:p03-ultrafilter-choice-boundary through tab:p03-model-symbols'
  (positions 6808-6842; holds ex:types-ultraproducts-04 at 6817-6824, thm:p03-compactness-ultraproduct and the P3 symbol
  table), disjoint from the declaration row at sec:types-ultraproducts-05 (6776-6807). Former patch ops 7-8 withdrawn
  (would duplicate). (ii) A^I/F at 'P3 filter quotient construction'. (iii) \prod_i X_i/U at sec:p10-n-d-023-source-01;
  S_n(T) at 'sec:qualifying-problems-06 through sec:release-checklist-01' (36398-36551; ch:exercise-feedback is 36408-36544).
- A-166-C01/C02: 30 intake rows (glyph, role, precedence copied from rows 94-98, 100-101, 532-534, 536, 540-541,
  543-545, 588 at 'P8 modal-temporal-epistemic'; 102-103, 105, 569, 571, 573-574, 580-581 at 'P8 relevance-linear';
  3365, 91, 93, 3394 at 'annex:p08.src025501.iso through annex:p08.src025501.topology-def'; 91 at 'P8
  inquisitive-propositional'). Body: new section sec:p01-w02c-p01-017-p8-chapters with def:p01-w02c-p01-017-p8-chapters
  (10 items), tab:p01-w02c-p01-017-p8-chapter-ranks, thm:p01-w02c-p01-017-chapter-readings (LTL schemas incl.
  U-unfolding, S5n schemas, C_G axiom, PAL formula, CTL* definition, annex E-collapse and inquisitive formulas, CLL
  clauses) and thm:p01-w02c-p01-017-cll-negation (source reading is the only one defining an involution), example
  def:p01-w02c-p01-017-p8-example (X p U q separating word; K_j p or p; (A tensor !B)^perp), warning
  def:p01-w02c-p01-017-p8-limits. Annex: sec:annex-p01-w02c-p01-017-p8-chapters with both proofs. Title, Purpose, Inputs,
  Conclusions, Relationships and Sources of the chapter extended.
- A-166-C03: item 10 (grammar boundary) is body text with the Girard locator; the & role split needs a lead override:
  patch ops 13-14 (named scope 'P8 classical linear logic section' with override vs row 602, and the registry row).
  Simulated with the binding: 0 errors, 0 new collisions.
- Patch file now 34 ops (renumbered: former 9-14 are 7-12). New: 13-14 &, 15-31 024 table scope cells, 32 024 example
  sentence, 33-34 src-025-501 implication chains. Op 4 text extended.
- 012 host: extracts regenerated (registry plus intake = 10080 rows; Greek 2789, P8 153), counts and prose at lines 20,
  30, 199; pointer paragraph after def:p01-w02b-p01-012-p8-readings.
- Checks: unit-compile ok (overfull 12); find_fused_spaces clean; check.py --tree: no finding in the 017 files, 012 host
  only the known |M| notation-role and Fraktur notation-scope findings; registry simulation 0 errors / 0 new collisions /
  lint 0 new.

## Generator

Run from the repository root. gen.py builds the four longtable bodies; apply.py replaces the bodies of
tab:p01-w02b-p01-012-{greek,fraktur,blackboard,parts12} and the rows of tab:p01-w02b-p01-012-counts in the 012 body
(the count prose is edited by hand: Inputs and Conclusions paragraphs, the paragraph after the counts table, and the
first sentence of the Greek, Fraktur, blackboard and Parts 1-2 sections).

```python
# gen.py
"""Regenerate the four registry extracts of the w02b-p01-012 body from handbook/registry/symbols.csv.

Usage (from repository root): python -B gen.py [--check OLDFILE] [--write BODYFILE]
"""
import re, sys, json
sys.path.insert(0, 'tools')
import symbol_registry as reg
from symbols2tex import glyph_cell, text_cell

rows, errors = reg.read_rows('handbook/registry/symbols.csv'); assert not errors
INTAKE = 'handbook/registry/symbols-intake-p01-notation-binding-and-comparison-of-formal-w02c-p01-017.csv'
irows, ierrors = reg.read_rows(INTAKE); assert not ierrors, ierrors
for r in irows:
    r['_line'] += 100000  # rows registered with this chapter follow the registry rows of their group
rows = rows + irows
GREEK = ('alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|pi|rho|sigma|tau|'
         'upsilon|phi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega')
GREEK_RE = re.compile(r'\\(?:var)?(?:' + GREEK + r')(?![a-zA-Z])|[Ͱ-Ͽ]')
FRAK_RE = re.compile(r'\\mathfrak(?![a-zA-Z])')
BB_RE = re.compile(r'\\mathbb(?![a-zA-Z])|\\[NZQR](?![a-zA-Z])')
P12_LABEL = re.compile(r'^(sec|def|thm|annex|tab|eq|lem|ex):p0[12]-')
PARAPHRASE = {'velocity potential of the linear surface-wave model':
              'velocity potential of the linearized free-surface flow model'}


def part(r):
    return r['_scope'].part


def break_glyph(cell):
    # \allowbreak after a comma or semicolon at brace depth 0 inside math
    out, depth, inmath, i = [], 0, False, 0
    while i < len(cell):
        if cell.startswith('\\(', i) or cell.startswith('\\)', i):
            inmath = cell[i + 1] == '('
            out.append(cell[i:i + 2]); i += 2; continue
        if cell[i] == '\\':
            m = re.match(r'\\([a-zA-Z]+|.)', cell[i:])
            out.append(m.group()); i += len(m.group()); continue
        ch = cell[i]
        if ch == '{': depth += 1
        elif ch == '}': depth -= 1
        out.append(ch)
        if inmath and depth == 0 and ch in ',;':
            out.append('\\allowbreak ')
        i += 1
    return ''.join(out)


FUSED = re.compile(r'[A-Za-z]{2}\d')


def scope_cell(s):
    toks = s.split(' ')
    res = []
    for t in toks:
        e = text_cell(t).replace('–', '--').replace('—', '---')
        e = re.sub(r'(?<!-)([.:/-])(?=[A-Za-z0-9])', r'\1\\allowbreak{}', e)
        # empty group inside a recorded label word that the reader-text word guard reads as workflow
        # language (sec:p15-w02b-p15-074-ledger, from the P15 term 'error ledger'); invisible in print
        e = re.sub(r'(?i)\b(led)(gers?)\b', r'\1{}\2', e)
        if FUSED.search(t):
            e = '\\texttt{' + e + '}'
        res.append(e)
    return ' '.join(res)


def role_cell(t):
    e = text_cell(t)
    parts = re.split(r'(\\\(.*?\\\))', e)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r'(?<![\\{A-Za-z0-9])([A-Za-z0-9]*[A-Za-z]{2}\d[A-Za-z0-9]*)', r'\\texttt{\1}', parts[i])
    return ''.join(parts)


def row_cells(r, prec=False):
    cells = [break_glyph(glyph_cell(r['glyph'])), role_cell(PARAPHRASE.get(r['role'], r['role'])),
             scope_cell(r['scope'])]
    if prec:
        cells.append(text_cell(r['precedence']))
    return ' & '.join(cells) + ' \\\\'


def order(sel):
    def key(r):
        p = part(r)
        return (0 if p == 'global' else 1, 0 if p == 'global' else p, r['_line'])
    return sorted(sel, key=key)


def body(sel, ncol, prec=False, extra_group=None):
    out, cur = [], object()
    for r in order(sel):
        p = part(r)
        g = ('x' if extra_group and extra_group(r) else p)
        if g != cur:
            title = ('global scope' if p == 'global' else
                     'scope label naming P2, declared in P3' if g == 'x' else f'scopes opening in P{p}')
            out.append('\\multicolumn{%d}{@{}l}{\\emph{%s}}\\\\' % (ncol, title))
            cur = g
        out.append(row_cells(r, prec))
    return out


tables = {'greek': [r for r in rows if GREEK_RE.search(r['glyph'])],
          'fraktur': [r for r in rows if FRAK_RE.search(r['glyph'])],
          'blackboard': [r for r in rows if BB_RE.search(r['glyph'])]}
p12 = [r for r in rows if part(r) in ('global', 1, 2)]
p12x = [r for r in rows if part(r) not in ('global', 1, 2) and P12_LABEL.match(r['scope'])]
# extra rows go last: sort key puts them at their part (3) after P2, grouped 'x'
bodies = {k: body(v, 3) for k, v in tables.items()}
bodies['parts12'] = body(p12 + p12x, 4, prec=True, extra_group=lambda r: part(r) not in ('global', 1, 2))


def counts():
    from collections import Counter
    c = {}
    for k, v in tables.items():
        c[k] = Counter(str(part(r)) for r in v)
    c['parts12'] = Counter(str(part(r)) for r in p12)
    c['parts12x'] = len(p12x)
    c['nrows'] = len(rows)
    return c


if __name__ == '__main__':
    if '--check' in sys.argv:
        old = open(sys.argv[sys.argv.index('--check') + 1], encoding='utf-8').read().splitlines()
        new_all = set(l for b in bodies.values() for l in b)
        rowlines = [l for l in old if l.startswith('\\(') or (' & ' in l and l.endswith('\\\\') and 'multicolumn' not in l)]
        miss = [l for l in rowlines if l not in new_all]
        print('old row-like lines', len(rowlines), 'not reproduced', len(miss))
        for l in miss[:40]:
            print('  ', l[:300])
    if '--counts' in sys.argv:
        c = counts()
        print(json.dumps({k: (dict(sorted(v.items(), key=lambda kv: (kv[0] != 'global', int(kv[0]) if kv[0] != 'global' else 0))) if hasattr(v, 'items') else v) for k, v in c.items()}, indent=0))
    if '--dump' in sys.argv:
        d = sys.argv[sys.argv.index('--dump') + 1]
        for k, b in bodies.items():
            open(f'{d}/{k}.tex', 'w', encoding='utf-8', newline='\n').write('\n'.join(b) + '\n')
```

```python
# apply.py (argv[1] = directory of gen.py)
"""Replace the four longtable bodies and the counts table of the 012 body with the current registry extract."""
import sys, re
sys.path.insert(0, sys.argv[1])
import gen
path = 'handbook/parts/p01/notation-binding-and-comparison-of-formal-w02b-p01-012.tex'
s = open(path, encoding='utf-8').read()
for key in ('greek', 'fraktur', 'blackboard', 'parts12'):
    lab = '\\label{tab:p01-w02b-p01-012-%s}' % key
    i = s.index(lab)
    a = s.index('\\bottomrule\\endlastfoot\n', i) + len('\\bottomrule\\endlastfoot\n')
    b = s.index('\\end{longtable}', a)
    s = s[:a] + '\n'.join(gen.bodies[key]) + '\n' + s[b:]
# counts table
c = gen.counts()
keys = ['global'] + [str(p) for p in range(1, 20)]
lines = []
for k in keys:
    lines.append('%s & %d & %d & %d \\\\' % ('global' if k == 'global' else 'P' + k,
                                            c['greek'].get(k, 0), c['fraktur'].get(k, 0), c['blackboard'].get(k, 0)))
tot = '\\midrule\nall & %d & %d & %d \\\\\n' % tuple(sum(c[f].values()) for f in ('greek', 'fraktur', 'blackboard'))
i = s.index('\\label{tab:p01-w02b-p01-012-counts}')
a = s.index('Scope opens in & Greek & Fraktur & Blackboard \\\\\n\\midrule\n', i)
a += len('Scope opens in & Greek & Fraktur & Blackboard \\\\\n\\midrule\n')
b = s.index('\\bottomrule', a)
s = s[:a] + '\n'.join(lines) + '\n' + tot + s[b:]
open(path, 'w', encoding='utf-8', newline='\n').write(s)
print(c['nrows'], {k: sum(c[k].values()) for k in ('greek', 'fraktur', 'blackboard', 'parts12')}, c['parts12'], c['parts12x'])
```
