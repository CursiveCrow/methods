REVISE

# Round-three blind adversarial publication/AGENTS review: N-c-012.c

## Reviewer identity, runtime, and independence

- Stable agent identifier: `/root/mcnaughton_1966_research`.
- Seat: adversarial publication and AGENTS compliance.
- Runtime exposure: the instruction surface identifies this runtime as Codex based
  on GPT-5; no more specific model build or version identifier was exposed.
- I read the complete updated charter before substantive review and used only its
  frozen round-three snapshot as the controlling unit.
- I did not inspect `ledger.md`, `transcript/chair.md`, an r1 or r2 transcript
  (including my own), another r3 transcript, or another reviewer's verdict. I did
  not contact another reviewer.
- I made no manuscript, source-note, source-presentation-ledger, bibliography, or
  shared-integration edit. This transcript is the only file I created or edited.
- I ran no test, test harness, automated checker, repository script, TeX command,
  handbook-PDF inspection, or build. The only mechanical operation on the frozen
  unit was SHA-256 identity hashing. Source-image reading was visual scholarship.

## Frozen identity verification before review

Every round-three identity matched before substantive reading:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf` | `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2` |
| `tmp/pdfs/p09-gpss-1980/page-08-quantifier-symbols.png` | `D74FF885AC1010EA703749F215D1E47DFB3649595F3F8C0A282E073DB714C0F9` |
| `tmp/pdfs/p09-gpss-1980/page-10-closure-crop.png` | `F49C546E4F07A005BA548AB594C6F63B01B37FC62FE3D8DD89A3FAE44EAEA434` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `3C62CB8706389EFA4572A45EE4321A5A985F2CEDC027C263F4E1B9D2F074F3E5` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `DAE8982D6CAA548BEBCB916B197399B6499A7C6DB966E6972CC4E2C50AC163BA` |
| `handbook/bib/handbook.bib` | `BB4096F50E3359E2F07187E1B898F8A8E65CF4A3AC3C288E3FA58099A2A53380` |
| `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` | `D7DF8D78587EDFBB0E5EFBE90A92EC39ED154214A9D2CE47DF1E0D8D23F3C49A` |
| `spec/research/p09-source-presentations-lot2-3.md` | `44538248682AA9229F049D27A32086FA8E65973B39DFA8FCDAB41ACD918008E0` |

No identity mismatch invalidated the substantive review.

## Authority pages visually read

I visually read the source-image render of every physical page; physical pages
1--11 are printed pages 163--173 with no wrapper. I used the images rather than
OCR or memory as authority:

- printed p. 163: title, all four authors, affiliations, abstract, ACM notices,
  introduction, and the informal strict clauses for `F`, `G`, `X`, and `U`;
- printed p. 164: initial grammar, model, clauses (1)--(5), the reversed `F`
  inequality, omega-validity, `L(U)`, eliminations, execution model, and partial
  correctness;
- printed p. 165: total correctness, invariance/eventuality inventories, and the
  expressiveness motivation;
- printed p. 166: insistence, its equivalent form, busy waiting, minimal fairness,
  infinite overtaking, and the start of persistence;
- printed p. 167: semaphore and guarded-region persistence examples, impulse, and
  the start of unsolicited response;
- printed p. 168: unsolicited response, `Pr`, FIFO, the proposed semaphore axiom,
  repeated-response refinement, and the four questions;
- printed p. 169: Kamp attribution, prior-system claims, first-order language, and
  complete/discrete/omega order classes;
- printed p. 170: inclusive `>= x` future-formula restriction, Theorems 2.1--2.3,
  `[SS]`, `At`, `Bet`, special formulas, Lemma 1, and decomposition formulas;
- printed p. 171: Main Lemma, Proposition 2.4, event-expression architecture,
  Theorem 2.5, A1--A5, U1--U2, R1--R3, and Theorems 3.1--3.2;
- printed p. 172: maximal theories, `Gamma`, the quotient relations, transitive-
  closure lemma, path/sequence conditions, truth lemma, and decidability; and
- printed p. 173: `F^0`, `G^0`, the two conflicting `U^0` surfaces, transformed
  systems, and the complete source bibliography.

I also visually read both controlling high-resolution crops. The p. 170 crop
unambiguously prints `(forall y >= x)` and `(exists y >= x)`. The p. 172 crop
unambiguously prints the literal closure premise `Xw in Gamma` leading to
`X not-w in Gamma`, together with the other displayed closure obligations.

## Strongest publication case for the frozen snapshot

The snapshot is substantially source-critical and mathematically disciplined.
It preserves the p. 164 `F` direction defect, makes the coherent future reading
and no-successor completion handbook-owned, separates GPSS strict infix `U` from
Kamp prefix `U` and modern inclusive `U`, gives correct two-way discrete-word
translations, preserves all four unequal theorem domains, keeps the normal-form
and canonical-model arguments at outline strength, and exposes rather than
repairs the p. 173 `U^0` conflict. The round-three F11--F13 repairs are present:
system-relative maximality and `Delta_0` selection are explicit, the restricted
domain and `s_0` are typed without an undefined descendant term, `Gamma` is not
called literally finite, and `[SS]` is identified and kept externally owned.

That strong case does not cure the findings below. They are reader-verifiability,
source-ownership, and technical-name-use defects in the frozen integrated unit.

## Findings

### AP-R3-F1 — Must fix: load-bearing source-local references remain opaque and incompletely mapped

- Severity: major publication/source-ownership defect.
- Artifact locations:
  - `handbook/parts/p09/presentations/n-c-012.tex:1652-1661` uses `[G2]`, `[P2]`,
    and `[MY]` without identifying the works; it also loses the printed
    `respectively` mapping of the two prior systems.
  - `handbook/parts/p09/presentations/n-c-012.tex:1824-1828` again assigns an
    equivalent transformed system to opaque `[MY]`.
  - `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:515-519`,
    `598-600`, `638`, `940-942`, `1004-1011`, `1098`, `1116`, and `1122-1131`
    likewise leave the proof/proposal referrals as source-local tags; the note
    additionally invokes `[G1]` and `[FL]` for the canonical-model analogy
    without expanding them.
  - `spec/research/p09-source-presentations-lot2-3.md:177-181` repeats `[G2]`,
    `[P2]`, and `[MY]` in the registered source account without a local mapping.
- Printed authority evidence:
  - p. 169 says the systems for `L(X,F)` and `L(X,F,U)` were suggested in
    `[P2]` and `[MY]`, **respectively**, and claimed complete there.
  - p. 170 sends the direct syntactic proof of Theorem 2.3 to `[G2]`.
  - p. 172 compares the quotient construction with `[G1]` and `[FL]`.
  - p. 173 identifies the relevant records as D. Gabbay, “The Separation
    Property of tense Logics,” manuscript, September 1979 (`[G2]`); A. Pnueli,
    “The Temporal Semantics of Concurrent Programs,” International Symposium
    on Semantics of Concurrent Computation, Evian, July 1979 (`[P2]`); T. J.
    Myers and A. Pnueli, “The Temporal Situation Until Now,” University of
    Pennsylvania technical note, 1979 (`[MY]`); D. Gabbay, “Axiomatization of
    Logic of Programs,” manuscript, November 1977 (`[G1]`); and M. J. Fischer
    and R. L. Ladner, “Propositional Modal Logic of Programs,” Ninth ACM
    Symposium on Theory of Computing, Boulder, May 1977 (`[FL]`).
- Claim: identifying `[SS]` while leaving the equally load-bearing Theorem 2.3
  referral `[G2]` opaque is inconsistent source treatment. The prior-system
  sentence also fails to state the exact source mapping: `[P2]` is attached to
  `DX/L(X,F)` and `[MY]` to `DUX/L(X,F,U)`, respectively.
- Reader/publication harm: a handbook reader cannot identify the delegated
  proof or the claimed prior systems from the handbook bibliography, and tags
  such as `[G2]` and `[MY]` look like unresolved citations. More importantly,
  the reader cannot tell whether those external bodies were acquired and
  verified or are merely bibliography entries reported by GPSS. This weakens
  the otherwise careful proof-ownership boundary required by C5--C7 and I7.
- Exact correction: at the first reader-facing occurrence, expand `[G2]`,
  `[P2]`, and `[MY]` to the printed p. 173 identities; restore `respectively`
  for the `DX`/`DUX` mapping; and state that GPSS reports these referrals but the
  handbook does not import or independently verify the manuscript/technical-
  note bodies unless a separate acquisition record establishes that fact.
  Add a compact source-local reference-key table to the source note covering at
  least `[G2]`, `[P2]`, `[MY]`, `[G1]`, `[FL]`, and the already identified
  `[SS]`. Replace opaque tags in the ledger with the identities or a precise
  pointer to that mapping. Bibliography records may be added if the handbook
  chooses to cite the external works directly, but must not imply body access.

### AP-R3-F2 — Must fix: the ledger calls a printed source refinement a “repair”

- Severity: moderate source/handbook-ownership defect.
- Artifact location: `spec/research/p09-source-presentations-lot2-3.md:175`.
- Printed authority evidence: p. 168 itself prints
  `Pr(p,q) and G(q implies Pr(p,q))` after explaining that the preceding
  first-occurrence condition permits one `p` to precede many `q` occurrences.
  The reader correctly calls it “the stronger source formula” at
  `handbook/parts/p09/presentations/n-c-012.tex:1459-1465`; the source note calls
  it the “printed refinement” at
  `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md:472-482`.
- Claim: the ledger instead calls the same formula “the interleaving repair.”
  In this integrated unit, “repair” is already used for genuinely handbook-
  owned interventions: reversing the p. 164 `F` inequality and discussing the
  possible unprinted `GA`-to-`G^0A` replacement. Calling a verbatim source
  refinement a repair collapses that ownership boundary.
- Reader/publication harm: the ledger can be read as claiming that the handbook
  supplied or corrected the repeated-response formula, contradicting the reader
  and note and blurring I4/I5's required source-versus-handbook separation.
- Exact correction: replace “the interleaving repair” with “the source's printed
  repeated-response refinement” (or equally explicit wording) and retain the
  printed p. 168 locator.

### AP-R3-F3 — Must fix: `Pr`'s local use account says two displays, but the abbreviation is used in three

- Severity: minor but definite publication/AGENTS-use defect.
- Artifact location: `handbook/parts/p09/presentations/n-c-012.tex:1433-1465`.
- Printed authority evidence: p. 168 defines `Pr` and then uses it in (1) the
  general FIFO request/response condition, (2) the proposed FIFO semaphore
  implementation axiom, and (3) the repeated-response refinement.
- Claim: lines 1441--1442 say the abbreviation is needed “only ... in the next
  two displays,” but lines 1463--1464 use it in a third display.
- Reader/publication harm: the sentence intended to discharge the user's
  necessity/nonredundancy/use rule is factually false about actual downstream
  use. The third use is important because it is precisely where `Pr` is iterated
  to exclude one request licensing arbitrarily many responses.
- Exact correction: remove “only,” or replace “the next two displays” with “the
  three following displays: the general FIFO condition, its implementation-
  specific semaphore instance, and the repeated-response refinement.”

## Criterion-by-criterion disposition

- **C1 — checked clean.** The four-author printed identity, eleven-page map,
  archive provenance, incomplete embedded `Author` field, DOI, POPL venue,
  pp. 163--173, ISBN/publisher record, archive-versus-ACM byte-identity limit,
  and conditional-copying/not-open-content boundary are consistent across the
  reader, source note, bibliography record, ledger, and inspected p. 163.
- **C2 — checked clean.** The initial grammar contains `q_i`, all four printed
  Boolean connectives, primitive `F/X/U`, and derived `G`; `q_i/Q_i` are kept
  distinct. Strict `F/G/U`, the one-sided `X` clause, the p. 164 `F` conflict,
  `L(U)` overload, local `U_s/S_s` standing, Kamp operand reversal, and both
  strict/inclusive bridge directions are exact and convention-separated.
- **C3 — substantively clean apart from AP-R3-F2/F3's ownership/use wording.**
  Partial/total correctness, both source lists, insistence/persistence/impulse,
  busy wait, minimal scheduler fairness, infinite overtaking, semaphore and
  guarded-region conditions, unsolicited response, `Pr`, FIFO, the proposed
  implementation axiom, and repeated-response formula match pp. 164--168.
- **C4 — checked clean.** All four questions, the literal Kamp IV.3 boundary,
  `L_1`, order classes, inclusive `>= x` future restriction, and handbook-owned
  temporal-to-first-order recursion are explicit. No complexity question is
  retrojected.
- **C5 — blocked by AP-R3-F1; otherwise checked clean.** Theorem 2.1, 2.2, 2.3,
  Proposition 2.4, and Theorem 2.5 retain their unequal formula, model, and point
  domains. `At/Bet`, special/decomposition forms, Main Lemma, event-expression
  omissions, numbering tension, and `[SS]` boundary are accurate. The opaque
  `[G2]` direct-proof referral is not publication-ready.
- **C6 — blocked by AP-R3-F1; otherwise checked clean.** `DX/DUX`, A1--A5,
  U1--U2, R1--R3, soundness/completeness strength, system-relative maximality,
  `Delta_0`, the exact restricted domain, literal `Gamma` closure, finite-up-to-
  equivalence qualification, quotient relations, transitive-closure lemma,
  intended adjacency, recurrence condition, truth lemma, and bound-free
  decidability are correctly separated. The prior `[P2]/[MY]` mapping and
  identities remain incomplete.
- **C7 — blocked narrowly by AP-R3-F1; otherwise checked clean.** The literal
  `F^0/G^0/U^0` equations, transformed schemes, explicit omega-countermodel,
  possible-but-unprinted repair, exact `D^0X/D^0UX` languages, conflict-qualified
  completeness, and separation from modern strong until/LTL/automata/PSPACE are
  correct. The repeated opaque `[MY]` ownership tag remains unresolved.
- **C8 — checked clean.** `tau` and `sigma` are typed eliminable translations,
  have the correct Kamp-prefix operand order, preserve next/previous through
  bottom on open intervals, and state their exact infinite-word domain. The
  public first-order theorem includes `X/Y` on the inclusive side and does not
  credit inclusive `U/S` alone with next-time expressiveness.
- **C9 — blocked by AP-R3-F1--F3.** The prose is otherwise independently worded,
  definitions precede substantive uses, new local notation has standing and
  nonredundancy, source omissions remain omissions, and the GPSS/Sistla--Clarke
  boundary explicitly changes from strict to inclusive clauses. Opaque external
  tags, the ledger's ownership word, and the false `Pr` use count prevent a clean
  publication/AGENTS verdict.

## Invariant-by-invariant disposition

- **I1:** honored in this review; no mechanical publication gate was substituted
  for scholarship.
- **I2:** honored; all eight hashes matched before and after substantive review.
- **I3:** honored; every printed page 163--173 and both controlling crops were
  visually read, with images controlling over OCR.
- **I4:** checked clean; the p. 164 inequality remains visible, the future reading
  and endpoint totalization are explicitly handbook-owned, and supplied
  translations retain ownership.
- **I5:** checked clean; GPSS strict infix `U`, Kamp strict prefix `U/S`, inclusive
  strong `U/S`, and the two inconsistent `U^0` surfaces remain distinct.
- **I6:** checked clean; grammar, expressive equivalence, theorem hypotheses,
  proof status, and deductive completeness are not collapsed; source-undefined
  `S`, `S'`, and `U'` remain source-reported or handbook-supplied as stated.
- **I7:** blocked only by AP-R3-F1's referral identifiability. The local proof
  statuses themselves are correct: 2.2 and 3.2 are outlines, 2.3 is external,
  event expressions and gap semantics are absent, 3.1 has no proof, and the
  canonical omissions are enumerated.
- **I8:** checked clean; no later LTL label, automata construction, small-model
  bound, PSPACE result, or model-checking theorem is attributed to GPSS.
- **I9:** blocked by AP-R3-F3 and affected by AP-R3-F2. All mathematically
  load-bearing local symbols are otherwise defined with standing,
  nonredundancy, and use, while undefined source labels are treated as missing
  artifacts rather than silently formalized.
- **I10:** honored; blind independence was maintained.
- **I11:** applied; these defects require `REVISE` regardless of another seat.
- **I12:** honored; no topic, part, book, build, rendered-page, human-review, or
  user-acceptance closure is claimed.

## Mandatory F01--F13 recheck

- **F01 checked clean:** metadata names Pnueli, Shelah, and Stavi and omits only
  Gabbay; the archive hash is not claimed ACM-byte-identical.
- **F02 checked clean:** initial atoms/connectives/primitive operators and the
  `q_i/Q_i` distinction are exact; Section 3's basis change is separate.
- **F03 checked clean:** local strict `Gp` and the globally prefixed form are
  distinguished from eventual permanence.
- **F04 checked clean:** weakest acceptable busy-wait behaviour, minimal fairness,
  and infinite overtaking all survive.
- **F05 checked clean:** `at_l`, current values, remembered inputs, precondition,
  and postcondition are typed before their displays.
- **F06 checked clean:** the FIFO semaphore formula is explicitly a proposed
  implementation-specific axiom.
- **F07 checked clean:** Lemma 1 is an unprinted induction essentially following
  Kamp Chapter II Theorem 1.
- **F08 checked clean:** all three canonical facts are typed, linearity is
  restricted to the exact `Delta_0`-rooted domain, and missing derivations remain
  missing.
- **F09 checked clean:** `D^0X/D^0UX` have the exact languages and claimed
  strength, with no invented p. 173 proof.
- **F10 checked clean:** both literal `U^0` surfaces, the separating model,
  possible repair boundary, and conflict-qualified `D^0UX` claim are present.
- **F11 checked clean:** maximality is system-relative; the unprinted standard
  selection of `Delta_0` is explicit; the restricted domain is displayed; and
  `s_0=Delta_0 intersection Gamma` contains `A_0`.
- **F12 checked clean:** `Gamma` is described only as finite up to logical
  equivalence, every literal closure obligation is retained, and the finite
  quotient remains a source assertion without invented representatives.
- **F13 checked clean in its stated `[SS]` scope:** `[SS]` is identified as the
  forthcoming Shelah--Stavi manuscript, and no imported verification is claimed.
  AP-R3-F1 is the distinct, analogous unresolved `[G2]/[P2]/[MY]` problem.

## Premortem

Assume this topic shipped unchanged and failed scholarly review. The most likely
failure is not a semantic equation: those are unusually well controlled. It is
that a source-critical reader follows the delegated proof and prior-calculus
claims, finds literal `[G2]`, `[P2]`, and `[MY]` with no handbook identity, and
cannot determine either which work is meant or whether the handbook inspected
it. The same reader then encounters “repair” for a formula that is visibly
printed on p. 168, weakening confidence in the carefully advertised
source/handbook boundary. A terminology audit would separately catch the false
two-display account of `Pr`. An ordinary copyedit might catch only that last
count; it would miss the load-bearing proof-referral provenance defect. That is
why AP-R3-F1 controls the verdict.

## Frozen identity verification after review and before filing

Immediately before filing, all eight frozen objects again matched the exact
round-three SHA-256 values listed in the pre-review table. No frozen artifact
drifted during this review.

## Narrow closure boundary

This verdict keeps N-c-012.c open pending repair and a fresh common frozen
snapshot. Even a later acceptance can close only N-c-012.c topic-level AI
review. It cannot close N-c-012.d, N-c-012 as a whole, Part IX admission, any
source-wide ledger, the final publication build, rendered-page inspection,
human review, final-book completion, or user acceptance.

REVISE
