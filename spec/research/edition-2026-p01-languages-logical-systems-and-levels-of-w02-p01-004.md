# w02-p01-004: sections 1.3 and 1.4 (object language and metalanguage; formula schemas, metavariables, quotation and codes)

Provenance note for packet `work/waves/w02/packets/w02-p01-004.json`, label tag
`p01-w02-p01-004`. Session date 2026-10-04.

## Gap addressed

Assessment gap for 1.4: no formula-schema notion, no numerical-code
construction and no schema/code distinction on the active P1 route; the only
coding construction on route is P5 `sec:arithmetic-coding-04`
(`handbook/restoration/inherited-09328-09438.tex`). Partial P1 credit existed at
`handbook/restoration/inherited-00853-00906.tex` lines 16-22 (metavariables,
quotation) and 24-28 (forward mention of self-encoding). That host is read-only
and was not edited. The new P1 section `sec:p01-w02-p01-004-schemas-codes`
develops: schematic letters and schemas, unique readability for schemas,
instantiation and instance sets, uniqueness of matching, a matching procedure
with correctness, size of instance sets, the link to uniform substitution, the
bound/schematic readings of displays, quotation names, a numerical code for
propositional formulas (injective, decreasing on immediate subformulas), a
decoding/recognition procedure with correctness, the schema/quotation/code/
numeral distinction as a definition plus theorem, the decidable code set of an
instance family, the corner-quote warning, and the limitation that a schema is
not one sentence (Tarski undefinability via the T-schema display).

## Components (section 1.3 source blocks)

The packet's five components are the source blocks of section 1.3. The
restoration file `handbook/restoration/inherited-00853-00906.tex` lines 1-53 is
byte-identical to source lines 853-905 (checked this session with `diff`), on
the P1 route via `restoration/scope-SRC-00853-00906`. Line mapping: restoration
line = source line - 852. No correction was applied; none was needed.

## Inputs opened this session (held source FLRV1, Version 1.0)

`source/formal-logic-reference.tex` (packet held path), read at lines:
- 173-193 title page (title, Version 1.0, 9 August 2026);
- 840-915 chapter "Levels, Objects, and Consequence", section "Object
  language and metalanguage" (all five component blocks);
- 1101-1200 chapter "Finite Strings, Induction, and Recursion", section "Finite
  sequences and strings": pairing `pair_N`, bijectivity argument with t_s,
  lemma "Countability of finite strings" and its corollary;
- 1590-1610 chapter "Writing Formal Definitions and Proofs", section "Error
  taxonomy" (level error row);
- 1658-1830 chapter "Propositional Syntax and Semantics": "Propositional
  alphabet", "Propositional formula", defined connectives, lemma "Parenthesis
  counting", theorem "Unique readability", "Complexity and subformula";
- 3910-3926 chapter "Theories and Axiomatization", warning checklist item 6
  (schema as a set of sentences);
- 9328-9335 chapter "Arithmetic, Representation, and Coding", section "Gödel
  coding" (source version of the definition; the handbook restoration carries a
  corrected version, which the new text references by label only);
- 9925-9992 chapter "Provability, the Second Incompleteness Theorem, and
  Truth": "Arithmetical truth definition", theorem "Tarski undefinability",
  remark "Partial truth definitions";
- 10175-10190 replacement schema ("not one first-order sentence");
- 15235-15260 chapter "Rule Sheets", section "Classical natural deduction"
  (rule schema reading by uniform substitution).
Handbook files read: `handbook/restoration/inherited-00853-00906.tex`,
`inherited-09328-09438.tex` (coding table, primitive-recursive implementation,
numeral code nu), `inherited-09925-09992.tex` lines 1-40,
`handbook/parts/p02/propositional-substitution.tex` lines 1-80
(`def:p02-uniform-substitution`, `thm:p02-uniform-substitution`),
`handbook/parts/p14/symbols-terminology-and-glossary.tex` lines 60-75, 490-505,
`handbook/registry/symbols.csv` (rows for phi/psi/chi, sigma/tau, upsilon,
corner quotes, numeral bar, iota, lambda, pi).

## Existing treatment search (A9)

- Listed: `inherited-00853-00906.tex` and the P14 glossary pointers to
  `sec:levels-02`. Extended by linking (`\cref{sec:levels-02}`), not duplicated.
- Not listed but found and linked: `def:p02-uniform-substitution` /
  `thm:p02-uniform-substitution` (P2, on route via `parts/p02.tex` line 7) --
  schema instances are proved to be uniform-substitution instances of a
  translated formula, and validity transfer uses the P2 theorem;
  `sec:arithmetic-coding-04` (P5 coding of L_A, corner quotes, numerals) --
  referenced as the arithmetic counterpart, not reproduced;
  `thm:tarski-undefinability` (P5) -- cited in the limitation warning;
  `sec:strings-01` (pairing and the injection of A* into N) -- reused, not
  reproved; `sec:turing-machines-02` referenced for primitive recursion.
- No handbook file defines formula schemas with instance sets, matching, or a
  propositional formula code (grep for schema/substitution instance/quasi-quot/
  corner quot across handbook/*.tex).

## Decisions

- Schematic letters are a separate metalinguistic set Xi = {xi_k}; displays
  keep writing phi, psi, chi (registered formula metavariables) for xi_0, xi_1,
  xi_2. The bound/schematic reading convention makes the two uses exact.
- Schemas use fraktur s, t to avoid the registered global sentence
  metavariables sigma, tau. The annex token map is `tk`, not tau, for the same
  reason.
- The P1 code is written `#phi`, not corner quotes, because corner quotes are
  registered for the P5 code (scope P5 arithmetic-coding onward) and the P1
  code is a different function (tags 0-5, propositional sort only).
- Codes: #p_n = 1+pi(0,n), #bot = 1+pi(1,0), #neg phi = 1+pi(2,#phi),
  #(phi o psi) = 1+pi(k, pi(#phi,#psi)) with k = 3,4,5 for and, or, implies.
  Worked example values checked by hand: #p_0 = 1, #neg p_0 = 8,
  pi(1,8) = 53, #(p_0 -> neg p_0) = 1765; pi^{-1}(4) = (1,1) so 5 is no code.
- No primitive-recursiveness claim for `dec` is made; the text states the
  limitation and points to the P5 implementation for the arithmetic code.
- All proofs are editorial completions; no external presentation is
  attributed. No source other than FLRV1 was used; no Quine/Tarski primary was
  opened, so quasi-quotation is not attributed and `Tarski1983` is not cited by
  the new text.

## Checks

- `python -B tools/waves.py unit-compile work/waves/w02/packets/w02-p01-004.json`:
  ok, 0 errors, no undefined citations or refs; remaining overfull boxes are
  the section heading in the unit wrapper, three auto-generated annex item
  headings, and the intake bibliography note.
- `python -B tools/find_fused_spaces.py` on body and annex: no hits.
- `python -B tools/check.py --tree handbook` filtered to these files: only
  bib-key for `FrozenFormalLogicSchemasCodes` (own intake key).

## Continuation

Latest pass (2026-10-04): wrote out the binary case of substitution-link clause 1 and the case-by-case induction for instance-count clause 1; replaced 'admitted' in body line 131. G1 hits for w02-p02-044/045/054 research files are other packets' files, not touched here.

All packet components and the 1.4 assessment gap are written. Open items for
the lead: insert the body input after `restoration/scope-SRC-00853-00906` and
before the 1.5 section input `parts/p01/languages-logical-systems-and-levels-of-w02-p01-003`
in `handbook/parts/p01.tex`; insert the annex input in
`handbook/annex/p01-route.tex` (packet proposal: after
`annex/p01/boolean-prime-ideal-and-ultrafilters`, before the 003 annex if that
is inserted at the same anchor); merge the bib and symbol intakes.
