# w02-p02-018 — propositional resolution and satisfiability procedures (P2 15.1, 15.2, 15.3, 15.8)

Packet: work/waves/w02/packets/w02-p02-018.json; label_tag p02-w02-p02-018.

## Files

- handbook/parts/p02/propositional-resolution-and-satisfiability-procedures-w02-p02-018.tex (body)
- handbook/annex/p02/propositional-resolution-and-satisfiability-procedures-w02-p02-018.tex (annex)
- handbook/bib/intake-p02-propositional-resolution-and-satisfiability-procedures-w02-p02-018.bib (comment only; no new keys)
- handbook/registry/symbols-intake-p02-propositional-resolution-and-satisfiability-procedures-w02-p02-018.csv
- work/waves/w02/patches/w02-p02-018.json (4 patch requests: thm:p02-decidability statement and status,
  thm:p02-sat-np-complete status, thm:p02-taut-conp-complete status, assembling annex items)

## 15.1 / 15.2 (FLRV1-U00200 to U00206)

Source lines 2810-2914 of source/formal-logic-reference.tex are byte-identical (diff run this session) to
handbook/restoration/inherited-02810-02914.tex lines 1-105, input on route by
restoration/scope-SRC-02810-02914 in handbook/parts/p02.tex. Unit map: U00200 2810 -> line 1 (section,
sec:prop-metatheory-04); U00201 2821-2830 -> 12-21 (Resolvent); U00202 2832-2836 -> 23-27; U00203 2837-2846
-> 28-37; U00204 2848-2852 -> 39-43 (thm:prop-resolution-complete); U00205 2853-2881 -> 44-72; U00206
2883-2906 -> 74-97 (rem:resolution-finiteness). No correction was needed or made; nothing new written.

## 15.3 provenance

- Truth-table procedure, evaluator, bounds, limits, membership, negation reduction: editorial proofs from the
  inherited semantics (sec:prop-syntax-semantics-01/02/04: grammar, valuation, lem:prop-coincidence,
  lem:prop-clause-satisfaction) and the complexity conventions def:p02-complexity-standing, def:p02-sat-taut.
  No external source presentation is reproduced.
- Cook-Levin hardness: own proof encoding a deterministic multitape verifier directly (no one-tape
  simulation). Historical attribution cites Cook1971 at p. 152, Theorem 1, read this session in
  source/references/acq-r1-ACQ-2026-10-0089/cook-1971-complexity-theorem-proving.pdf (printed page 152
  carries "Theorem 1" and the start of its proof; one-tape NTM, P-reducibility, DNF tautologies).
- AroraBarak2009: the held file source/references/acq-r1-ACQ-2026-10-0012/... is the January 2007 internet
  draft (manifest result "version_differs"; chapter organisation differs from the 2009 CUP text). No
  presentation was written from it and no AroraBarak2009 locator was written. A presentation of the
  Cook-Levin reduction specific to Arora-Barak 2009 remains an acquisition need.
- Undecidable infinite theories: cardinality argument (thm:p01-cantor; countably many machines); no appeal to
  thm:halting-undecidable, to avoid an unproved bridge between the Part-4 machine model and the
  computability chapter's index model.

## 15.8 provenance

- Formats: SAT certificate aligned with def:p12-sat-certificate-boundary; resolution log format declared
  here (parents j,k < i, pivot L, resolvent equality); countervaluation certificate.
- Worked instances use the clause set of fig:p02-resolution-dag and def:p12-dpll-trace; the DPLL extraction
  uses Method def:p12-dpll and thm:p12-dpll-correctness. p,q,r = p_0,p_1,p_2 so form_CPL gives exactly the
  displayed disjunctions (code order).
- A-121: new figure fig:p02-w02-p02-018-fol-dag (C1={P(x),Q(x)}, C2={~Q(y),R(y)}, C3={~P(a)}, C4={~R(a)}),
  three resolution steps with MGUs {x->y}, {y->a}, id; each MGU checked against the inherited unification
  procedure (equation orientation r from A, t from B) and directly; lemma thm:p02-w02-p02-018-fol-dag.

## Overlaps found (for the lead)

- Packet w02-p02-019 (15.5-15.7) is writing, in parallel, handbook/parts/p02/propositional-resolution-and-
  satisfiability-procedures-w02-p02-019.tex with its own truth-table method/theorem (O(2^k l) claim),
  SAT-in-NP, negation maps, TAUT coNP and a sentence saying its truth-table theorem proves
  thm:p02-decidability. Its annex did not exist when checked. Duplicate treatments of 15.3 content; the lead
  should keep one set and cross-link, and apply only one packet's status patches for thm:p02-decidability,
  thm:p02-sat-np-complete, thm:p02-taut-conp-complete.
- sec:p09-presentation-n-c-026 (handbook/parts/p09/presentations/n-c-026.tex) has a prose Cook-Levin
  reconstruction (one-tape verifier, 3-cell windows, one-tape simulation assumed). Not listed in the packet.
  Linked from the body; the proof here differs by encoding the multitape verifier directly.
- thm:p02-w02-p02-014-decision / -consequence (tableau decision and countermodel read-off) linked as the
  third extraction route.

## Symbol decisions

- Language complement written L^{\mathsf c} (not overline) because \overline L is the registered literal
  complement used in the same section.
- \operatorname{len} used for string length; |.| only for cardinality (|Q|, |Sigma_M|).
- Opposite truth value written b' in the evaluator proof.

## Continuation

State at return: body and annex written; unit-compile ok; find_fused_spaces no hits; check.py --tree
handbook shows no finding in this packet's files. Open items: Arora-Barak 2009 published text not held
(acquisition need); lead to apply patch file after inserting the driver inputs, and reconcile with
w02-p02-019.

Block 2 (2026-10-04): the guard reported eight changed files outside this packet's owned set
(spec/research/edition-2026-p02-completeness-choice-scope-w02-p02-054{.md,-return.json},
edition-2026-p02-unit-accounting-w02-p02-042/044/045{.md,-return.json}). None was written by this packet:
they carry other packets' ids, their timestamps (04:02 to 05:01) postdate this packet's last write (04:00),
and the 054 and 045 pair are absent from the tree now. They belong to the concurrent sessions for
w02-p02-042/044/045/054 and were left untouched (modifying or deleting them would edit another agent's
files). The guard should attribute them to those packets. No owned file changed in block 2 apart from this
note and the return file. Re-ran: unit-compile ok (0 errors, 0 unknown refs, 0 undefined citations, 2
overfull annex headings); find_fused_spaces no hits; check.py --tree handbook no finding in this packet's
files. Open items unchanged: Arora-Barak 2009 published text not held; lead applies the patch file after
inserting the driver inputs and reconciles with w02-p02-019.
