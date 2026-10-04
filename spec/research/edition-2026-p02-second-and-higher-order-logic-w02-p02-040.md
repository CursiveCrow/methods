# Packet w02-p02-040 (P2 chapter 23, sections 23.1-23.4): research and provenance note

## Sources opened in this session

- Church1940: `source/references/acq-r1-ACQ-2026-10-0080/church-1940-simple-theory-of-types.pdf`
  (JSTOR scan, J. Symbolic Logic 5(2), printed pp. 56-68; listed in
  spec/coverage/edition-2026/held-sources.json). Every page was read from page
  images, because the OCR text layer garbles formulas: p. 56 (types),
  p. 57 (primitive symbols, wff rules), p. 58 (abbreviation list, read at 220 dpi),
  p. 59 (bracket precedence, intended interpretation), p. 60 (rules I-VI, IV', VI',
  axioms 1-2), p. 61 (axioms 3-11 read at 260 dpi; roles of the axioms), p. 62
  (iota definitional schema read at 260 dpi; proofs on assumptions; VII),
  p. 63 (proof of VII; 12-21; footnote 10), p. 64 (22-26, VIII, start of the 27^o proof),
  p. 65 (27^o, 27^alpha-beta, 28, 29), p. 66 (30, footnote 12), p. 67 (31-34),
  p. 68 (35-43, footnote 13).
- Every Church locator written in the body/annex was seen on these pages.
- Not held (checked against held-sources.json): Henkin1950, Andrews2002,
  Shapiro1991, Jech2003. No source-specific presentation of them was written.

## Route files read

inherited-12262-12289, 12290-12355, 12356-12414, 12415-12536, 12537-12673,
12721-12783, 12784-12923; parts/p02/simple-type-logical-constants.tex,
pa2-definition.tex, second-and-higher-order-logic-supplement.tex;
annex/p02/higher-order-supplement.tex; registry/calculi/sol.tex;
inherited-09925-09992 (Tarski undefinability and corollary), inherited-08710-08876
lines 950-1045 (thm:p04-ce-sigma-one), inherited-07753-07843 (c.e. definitions),
inherited-09328-09438 (Goedel coding).

## Decisions

- Church's notation is kept verbatim (value type first, subscripted constants,
  bold syntactic variables, dots and the turned iota). The letter iota has two
  roles in the source (type symbol, selection constant); both are recorded in
  the symbol intake. N is both N_oo (negation) and N_{o alpha'} (number predicate)
  in the source; also recorded.
- The source gives no model theory. The standard model S(D,c) is the handbook's
  formalization of the source's words on p. 59; this standing is stated in the
  body. Independence of 7 and 8 and non-theoremhood of 26^alpha for iota-free alpha
  are the source's claims (pp. 61, 64); the proofs by standard models are the
  handbook's.
- Propositional calculus from Axioms 1-4: the source itself cites Hilbert-Ackermann
  and Bernays (p. 62, n. 9). This cited boundary is preserved in
  def:p02-w02-p02-040-church-prop and is the only cited step in the derivations.
- The source leaves 12-20 and 22-24 to the reader; the annex supplies them.
- PA2 + and x preservation, reals categoricity and the nonaxiomatizability proof
  are new handbook proofs; the restoration hosts are read-only, so pointer edits
  are patch requests in work/waves/w02/patches/w02-p02-040.json.
- Second-order code tags 15-18 extend the constructor table of
  sec:arithmetic-coding-04 (tags 0-14 used there); first-order codes unchanged.

## Block 2 sources and decisions

- Church1940 pages re-read from page images in block 2: p. 61 (axioms 3-11, roles,
  n. 8, class-representation formula, "9 obviously not independent of 1-4 and 11"),
  p. 62 (independence of each 9^alpha with 1-9 only; iota_{alpha beta(o(alpha beta))}
  schema and the claim that 9^alpha become theorems of 1-8, 9^o, 9^iota, 10;
  start of section 5 and n. 9), p. 64 (22-26, VIII, announcement that 26^iota',
  26^iota'', ... are consequences of 1-6 and 8), p. 65 (28, 25, 29), p. 66
  (30^alpha, (1), (2), proof of (2), start of (1), n. 12), p. 67 (end of (1);
  section 7: 31, 32, 33 with proof, 34), p. 68 (proof hint of 34, 35, section 8
  schema, F formula, 36-43 with hints, n. 13 Rosser definitions, read at 300 dpi).
- Rosser's symbols on p. 68 n. 13 are rendered \mathfrak s and \mathfrak B
  (fraktur in the scan).
- (P) is now proved (annex:p02-w02-p02-040-church-prop-complete) by a clause
  reduction from (a1)-(a4) with MP; the source's citation of Hilbert-Ackermann
  and Bernays (n. 9) is kept as a record only.
- Finding: Church's derivation of (1) uses 28^alpha, which for iota-types rests
  on Axiom 7; the p. 64 announcement "consequences of 1-6 and 8" is not
  established by the written derivation (warning def:...-church-26-axiom-7).
- Finding: the section 8 recursion schema fails for Church's F without a
  hypothesis on A and B; proved under (H) (A and values of B are numbers), with a
  standard-model counterexample (A constant functional, B = K) in the annex.
- Independence of each 9^alpha: proved by a standard model whose selection
  function at alpha is constant (handbook proof; the source gives none).
- n. 12 claims (Church's and Turing's replacement results; openness of the
  independence of 8 from 1-7 and 30^iota) are stated as reported, not proved.
- Tags 15-18 for second-order codes coincide with outer tags of derivation
  records, proof codes and alpha records in sec:arithmetic-coding-04; the
  annex shows the sorts are disjoint by arity.

## Block 3 sources and decisions

- No new source was opened; Church1940 locators added in block 3 (p. 61, the
  p = q remark) were read in blocks 1-2. Henkin1950, Andrews2002, Shapiro1991
  remain unheld; the general-model definitions and proofs are the handbook's.
- General models allow D_o with more than two members and a truth set T,
  because Church's axioms do not include propositional extensionality
  (p. 61). Separation (G5) makes Leibniz equality identity; Axiom 10 is then
  valid, and in the decoding E_ext makes the quotient extensional.
- Encoding: one function symbol per abstract with first-order equality beta
  axioms (strict many-sorted logic of def:p02-many-sorted-signature has
  same-sort equality). Canonical model: wffs modulo conversion; witnesses
  F y -> Pi F with Rule VI; arbitrary Gamma handled by renaming to even
  variables and back through decoding/encoding (no AC in 3 => 1).
- Native sheet:sol completeness: Henkin pair saturation with Cut; equality
  replacement both ways derived from =L, neg L/R and Cut; corollary gives
  native = translation-defined = H_CC consequence (AC only via
  thm:p02-sol-derived-adequacy).
- Guard: the w02-p02-042 unit-accounting files flagged in G1 do not exist in
  this worktree and were never touched by this packet.

## Continuation

Written through block 3 (body handbook/parts/p02/second-and-higher-order-logic-w02-p02-040.tex,
annex handbook/annex/p02/second-and-higher-order-logic-w02-p02-040.tex):
- Blocks 1-2 items (see return JSON).
- Block 3: subsection sec:p02-w02-p02-040-church-general (general models,
  first-order encoding Enc, soundness, encoding/decoding/exactness, strong
  completeness with compactness, example, limits) and section
  sec:p02-w02-p02-040-sol-native (native derivability, soundness and
  completeness of the sheet:sol rule list, correspondence corollary, example,
  limits), with annex proofs.

Remaining, in priority order:
1. D-P9-001-GOAL-03: thm:p04-ce-sigma-one proof is a sketch in
   handbook/annex/p04/decision-problems-and-arithmetical-hierarchy.tex
   (annex:p04-hierarchy.8); clause 3 of the nonaxiomatizability proof depends
   on it. Not editable here (policy).
2. N-a-071-S01-PROOF items (i)-(iii) as in the return JSON (Axiom 7 in the
   derivation of 26 at iota-types; n. 12 claims; section 8 schema).
3. Existence of a complete ordered field (Dedekind cuts); Jech2003 not held.
4. N-a-071-S02/S03/S04: blocked_source (Henkin1950, Andrews2002, Shapiro1991).
