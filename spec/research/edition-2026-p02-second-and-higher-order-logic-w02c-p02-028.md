# Research note: packet w02ca-p02-028 (P2, section 23.1), label tag p02-w02c-p02-028

## Provenance

- Source opened this session: `source/references/acq-r1-ACQ-2026-10-0080/church-1940-simple-theory-of-types.pdf`
  (JSTOR scan of Church, "A Formulation of the Simple Theory of Types", JSL 5(2), 1940, pp. 56-68; PDF page 2 = journal p. 56).
  Pages 56, 58, 59, 61, 62, 63, 64, 65, 66 were rendered and read as images (the text layer is unreliable).
- Locators used and seen: p. 56 (opening paragraphs; sec. 1 type-symbol examples `o iota`, `iota iota iota`, `iota iota(iota iota)`; nn. 1-5),
  p. 57 (sec. 1 interpretation-irrelevance remark, "formal consistency assumed"), p. 59 (sec. 2 predecessor remark),
  p. 60 (sec. 3 "rules I-III are called rules of lambda-conversion"), p. 61 (sec. 4 axioms 3-11; formal vs syntactical theorems; independence of 7 and 8; class representation; p = q axiom),
  p. 63 (sec. 5 remark on 21), p. 64 (sec. 6 announcement on 26), pp. 65-66 (27, 28, 30, n. 12).
- Not held (checked held-sources.json this session): Henkin 1950 (ACQ-2026-10-0187), Andrews 2002 (ACQ-2026-10-0008), Shapiro 1991 (ACQ-2026-10-0503).

## What was written

Body `handbook/parts/p02/second-and-higher-order-logic-w02c-p02-028.tex` (insert after `parts/p02/second-and-higher-order-logic-w02b-p02-034`, line 162 of `handbook/parts/p02.tex`);
annex `handbook/annex/p02/second-and-higher-order-logic-w02c-p02-028.tex` (insert after line 58 of `handbook/annex/p02.tex`).

- S01-PRESENTATION (1) p. 56 justification: `def:p02-w02c-p02-028-purpose`.
- S01-PRESENTATION (2) nn. 1-5 attributions and n. 2 pointer: `def:p02-w02c-p02-028-attributions`.
- S01-PRESENTATION (3) / S01-BRIDGE: source example reconstructed in `def:p02-w02c-p02-028-type-examples` with host form; the altered example at 040:43-45 needs patch 1 in `work/waves/w02ca/patches/w02ca-p02-028.json`.
- S01-PRESENTATION (4) p. 57, p. 61, p. 63 qualifications: `def:p02-w02c-p02-028-qualifications`.
- S01-PROOF (1) p. 59: `thm:p02-w02c-p02-028-predecessor`, proof `annex:p02-w02c-p02-028-predecessor`.
  Method: a relation between S(D,c) and the two-individual model S(E,c') with R_iota = graph of a surjection g: D -> E and R_o total.
  Every selection-free wff respects it (constants N, A, Pi have types ending in o). R_iota' is single-valued.
  In E, S 0 = S 2 while 0 /= 2, because h^3 = h for all h: E -> E.
  Precise form: no closed selection-free F_{iota' iota'} has F(S 0) = 0 and F(S 2) = 2 in any S(D,c) with |D| >= 2. Hence N x > F(S x) = x is not a theorem of Axioms 1-11.
  The handbook formulation is its own; the source gives only the one-line remark.
- S01-PROOF (2) p. 61 adequacy: `def:p02-w02c-p02-028-class`, `thm:p02-w02c-p02-028-classes`, proof `annex:p02-w02c-p02-028-classes`.
  Clause 1 uses 1-6, 9^iota', 10^iota'alpha. Clause 2 uses 1-7, 9^iota'.
- S01-PROOF (3) p. 64: `thm:p02-w02c-p02-028-no-ax7` derives 26^{alpha_k} (k >= 1) from 1-6, 8 and instances of 10, without 7, by cases on 27^iota.
  NOT established: derivability from 1-6^alpha and 8 alone (without 10), or a proof that it fails. Recorded in `def:p02-w02c-p02-028-open`.
  Obstacle: 28^iota (used by the source's route) is false in the one-individual standard model where Axiom 8 is valid, so 28^iota is not derivable from 1-6, 8.
  A non-derivability proof would need a non-extensional general model of 1-6 and 8 that refutes 26^iota'; none was constructed.
- Patch requests (read-only hosts): `work/waves/w02ca/patches/w02ca-p02-028.json`. There are six: the 040 example; the 040 Axiom 7 warning; the 040 annex cross-reference; two in the 041 predecessor warning; and the 034 open-claims warning. All anchors were verified unique.

## Continuation

- Remaining for S01-PROOF (3): derive 26^iota', 26^iota'', ... from Axioms 1-6^alpha and 8 alone, or show this fails (blocked_math here).
- Remaining for S01-PRESENTATION (3) / S01-BRIDGE: apply patch 1 (040:43-45 example), executed by the lead.
- Henkin/Andrews/Shapiro shares (S02-S04 and their share of C01): blocked_source until ACQ-2026-10-0187, -0008 and -0503 are held.
- Unit compile: ok, 0 overfull (session end).
