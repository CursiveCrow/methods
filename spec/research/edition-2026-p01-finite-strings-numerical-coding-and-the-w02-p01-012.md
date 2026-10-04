# w02-p01-012: chapter 4 (sections 4.1-4.4), finite strings and numerical coding

Provenance note for packet `work/waves/w02/packets/w02-p01-012.json`, label tag
`p01-w02-p01-012`. Session date 2026-10-04.

## Gap addressed

Assessment gap (ED26-FLRV1-U00090-01 / FLRV1-U00091): the source proof of the
lemma "Countability of finite strings" (frozen lines 1151-1162, on route
verbatim at `handbook/restoration/inherited-01148-01163.tex` lines 4-15)
asserts "Induction on n proves that every e_n is injective" with no base case
or inductive step, and does not show why w -> pair_N(n, e_n(w)) is injective
on A^*. The restoration host is read-only and byte-exact and was not edited.
The steps are written as an identified editorial expansion in the owned files:

- body `handbook/parts/p01/finite-strings-numerical-coding-and-the-w02-p01-012.tex`
  (sec:p01-w02-p01-012-string-coding);
- annex `handbook/annex/p01/finite-strings-numerical-coding-and-the-w02-p01-012.tex`
  (annex:p01-w02-p01-012-stage-injective: Step 0 pair injectivity, base case,
  inductive step exactly as the assessment specifies;
  annex:p01-w02-p01-012-tagged-injective: disjointness of the A^n, so the
  tagged map is well defined, then n=n' and w=w';
  annex:p01-w02-p01-012-countable; annex:p01-w02-p01-012-decoding-correct).

## Inputs opened this session (held source FLRV1, Version 1.0)

`source/formal-logic-reference.tex` read at lines 173-193 (title page: title,
Version 1.0, 9 August 2026), 365 (chapter "Sets, Relations, Functions, and
Cardinality"), 530-580 (section "Finite, countable, and uncountable sets",
`sec:set-prerequisites-05`, definition "Countable set", CSB theorem), and
1100-1225 (chapter "Finite Strings, Induction, and Recursion", section
"Finite sequences and strings": definitions, pairing paragraph, lemma and
proof, corollary, concatenation lemma). Restoration captures
`inherited-01101-01147.tex`, `inherited-01148-01163.tex`,
`inherited-01164-01223.tex` read in full. Cross-references checked:
`sec:turing-machines-01` (inherited-07506-07677.tex line 84ff uses
pair_N for tuples), `sec:arithmetic-coding-04` (inherited-09328-09438.tex
line 27, C(a,b)=1+pair_N(a,b)).

## Existing treatment search (A9)

- Listed: the three restoration captures and `sec:strings-01`. Extended by a
  new section that links back; nothing duplicated (the pairing bijectivity
  argument is cited; only its injectivity half is written out as Step 0
  because the induction uses it).
- Not listed but found: `handbook/annex/p01.tex` annex:p1.5
  (thm:p01-countable-strings) and `handbook/parts/p01/mathematical-preliminaries.tex`
  line 210. Both are off the active route (not input by parts/p01.tex or
  annex/p01-route.tex). annex:p1.5 also compresses the induction into one
  sentence. Not cited because off route.

## Decisions

- Notation follows the source: e, e_n, pair_N, t_s, w restricted to n, A^n,
  A^*, epsilon. The source commands `\length` and `\restr` raise errors outside
  inherited scopes, so the editorial file spells them `\operatorname{len}`
  and `\mathbin{\upharpoonright}` (their in-scope expansions).
- New local names: unpair, d_k, <x> (one-letter string), example letters.
- Heading level \section inside chapter ch:strings; insertion after
  `restoration/scope-SRC-01164-01223` (end of the source section), annex after
  `annex/p01/boolean-prime-ideal-and-ultrafilters` per the packet proposal.
- Open item for the lead (not a component blocker): the verbatim source proof
  has no forward pointer to the expansion; adding one would change a
  byte-exact restoration capture, so none was requested.

## Checks

- unit-compile: ok, 0 errors; 3 overfull boxes, all in annex item headings
  generated from long labels and in the bibliography rendering of the intake
  title.
- find_fused_spaces: no hits.
- check.py --tree handbook filtered: only bib-key for
  FrozenFormalLogicStringCoding (own intake key).

## Continuation

Component FLRV1-U00091 gap: written (body + annex, see above). Components
FLRV1-U00087/88/89/90/92/93/94/95: pre-existing verbatim on-route captures,
no gap reported by the assessment, not edited. Nothing further pending in this
session.
