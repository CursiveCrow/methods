# w02-p02-025 research note: P2 chapter 17, sections 17.4, 17.5, 17.6

Packet: work/waves/w02/packets/w02-p02-025.json. Label tag p02-w02-p02-025.

## Files

- Body: handbook/parts/p02/first-order-calculi-and-equality-w02-p02-025.tex
  (section sec:p02-w02-p02-025-fol-calculi; insertion proposal: after
  `\input{parts/p02/first-order-depth}` in handbook/parts/p02/first-order-logic.tex).
- Annex: handbook/annex/p02/first-order-calculi-and-equality-w02-p02-025.tex
  (insertion: after `\input{annex/p02/first-order-completeness-remainder}` in
  handbook/annex/p02.tex).
- Editable hosts changed: handbook/registry/calculi/tableaux-fol.tex (equality
  rules =refl, =repl; identity text: freshness, fairness, T versus T^=,
  adequacy and non-termination links), handbook/parts/p02/hilbert-fol-adequacy.tex
  (pointer to the Kleene presentation; pointer to explicit identity/permutation).
- Patch requests: work/waves/w02/patches/w02-p02-025.json (5 entries: annex
  p2.fol.calc.5 proof text; two in annex p2.hfa.discharge; hilbert-fol sheet
  statement of the deduction theorem; supplement sentence correcting the
  attribution of the premise condition to Kleene's rule 12).
- Intake bib: no new keys. Symbol intake: 7 rows.

## Sources opened in this session

- Kleene1952, held file
  source/references/acq-r1-ACQ-2026-10-0230/kleene-1952-introduction-to-metamathematics-1974-reprint.pdf
  (1974 seventh reprint; manifest states pagination x+550 matching 1952; PDF
  page = printed page + 9). Locators read and used:
  - Section 19, p. 81: stipulations for postulates 1-8 and 9-13 (C not
    containing x free; t free for x in A(x)).
  - Section 19, p. 82: full postulate list Group A1 (1a, 1b, 2, 3, 4a, 4b, 5a,
    5b, 6, 7, 8 with degree mark), Group A2 (9, 10, 11, 12), Group B (13-21);
    definition of axiom (1a, 1b, 3-8, 10, 11, 13, 14-21) and immediate
    consequence (2, 9, 12); note deferring the degree mark to Section 23.
    Verified against a rendered page image, not only OCR.
  - Section 20, p. 87: deduction from assumption formulas, the turnstile.
  - Section 21, p. 90: Theorem 1 (propositional deduction theorem) and its
    course-of-values induction, cases (a)-(d).
  - Section 21, p. 93: (8') permutation by two applications of Theorem 1.
  - Section 22, p. 95: 'depends' definition; p. 95-96: 'varied' / 'held
    constant'; p. 96: Example 3 and the restriction statement; p. 97:
    Theorem 1 (concluded) and subcases (e1), (e2) using (6'), (7'); p. 98:
    case (f) using (8') twice; attribution to Herbrand 1930.
- Not opened: Mendelson1997, Smullyan1968, Enderton2001 (cited only without
  locators, as attributions already on the route).

## Existing treatments found (A9)

- Listed: first-order-calculi-supplement.tex (body and annex), hilbert-fol-adequacy.tex
  (body and annex), propositional-hilbert-tableaux.tex, registry sheets.
- NOT listed in the packet: handbook/parts/p02/axiomatic-calculi-analytic-tableaux-and-refutation-w02-p02-014.tex
  and its annex (packet w02-p02-014, same wave, untracked). It already writes
  D-P3-002 GOAL-02/03/04 in full: equality tableau rules
  (def:p02-w02-p02-014-fol-equality), task bookkeeping with freshness,
  instantiation and fairness (def:p02-w02-p02-014-fol-branch), soundness,
  Hintikka sets, congruence, Herbrand truth lemma, extraction, fair systematic
  procedure with infinite branch construction and semidecision, propositional
  termination and decision, decision-versus-semidecision boundary; patch file
  work/waves/w02/patches/w02-p02-014.json moves both adequacy theorems from
  cited=Smullyan1968 to proved=. Per A9 this packet links that treatment and
  does not write a second one. Its one recorded remainder (no registry sheet
  for the equality rules) is closed here by the tableaux-fol.tex sheet edit.
  I spot-read the 014 semidecision proof (annex lines 630-700) and the
  definitions; I did not re-verify every 014 annex proof.
- annex:p2.calc.2 already contains an explicit identity derivation (propositional
  sheet); annex:p2.hfa.discharge already references it.

## Decisions

- The permutation is written as an explicit 19-line A1/A2/MP derivation
  (5 A1, 5 A2, 9 MP), not via the kernel lemma, so the first-order deduction
  theorem no longer depends on cited propositional completeness.
- A full support-tracking proof of the deduction theorem is given as
  thm:p02-w02-p02-025-discharge. It has the same content as
  thm:p02-hfa-discharge-interface; the patch to annex p2.fol.calc.5 points
  the existing proof at the new lemmas instead of creating a further body
  theorem. The lead may decide whether thm:p02-w02-p02-025-discharge should
  stay as a separate result or be merged with the discharge interface.
- Kleene presentation keeps Kleene's notation (supset, &, A(x)/A(t), plain
  turnstile); rules are written as "from ... infer ..." text to avoid
  rule displays outside the registry. A Kleene calculus sheet under
  registry/calculi/ was not created (not an owned file).
- Kleene's deduction theorem is proved in the annex (Steps 0-3), following
  Kleene's case structure, rather than cited.

## Open items

- Version: Kleene1952 held file is the 1974 reprint; page locators are from
  it. The bib entry says 1952. Lead decision whether to add a version note to
  the bib entry.
- Driver insertions (body and annex) and the 5 patch requests are for the
  lead. The patches reference labels defined in this packet's files and in
  w02-p02-014's files; apply after both packets' inputs exist.

## Continuation

Status at return: all files written; unit-compile ok (overfull 0); check.py
shows no finding in this packet's files; fused-space check clean.
Remaining for a later block, if wanted: a registry sheet for Kleene's
predicate calculus (needs a new file under registry/calculi/ and a
\showcalculus line in parts/p14/rule-sheets.tex, both outside owned files).
