# Exact Hilbert-FOL adequacy: source and dependency record

Date: 1 October 2026 (local). New disjoint body and annex:
`handbook/parts/p02/hilbert-fol-adequacy.tex` and
`handbook/annex/p02/hilbert-fol-adequacy.tex`.

## Allocation and exact source extent

Read the actual `ED26-REQ-D-P3-001-01` record in
`spec/coverage/edition-2026/requirements-units.jsonl` before authoring. It
preserves original identity `D-P3-001`, is `identified_held`, and identifies
`handbook-mathematical-presentation:D-P3-001`, not an invented whole-book
Mendelson/Kleene/Enderton reconstruction. Its exact original goals are the
selected language/schemas/rules/equality convention, deduction with
generalization/free-variable restrictions, and the distinction from CPL's
assumptions/derived rules. Its remaining-work statement preserves
unverified source-calculus coverage beyond this selected fragment.
The dependency allocation `D-P2-001` supplies the separate propositional
Hilbert basis and comparison; its cited completeness is not silently
promoted to a locally reproduced proof here.

Read the literal `hilbert-fol.tex`, active
`first-order-calculi-supplement.tex` and its active annex, the current
Chapter 282 file `classical-and-constructive-calculi.tex`, the active
propositional Hilbert consumer/annex, the actual capture-avoiding syntax
in `inherited-03240-03428.tex`, and the current P7 canonical-LK/ND bridge
and completeness proofs. Chapter 282's filename was located rather than
assumed from its display title. Historical inactive combined calculus
files were not used as controlling consumer definitions.

The literal selected fragment is equality-free, primitive negation and
implication, primitive universal/existential quantification, A1–A3, MP,
universal instantiation/distribution, existential introduction,
premise-sensitive Gen and existential elimination. Every quantified rule
condition is matched. No existing rule, driver, canonical record, Chapter
282 paragraph, or prior minimal/intermediate file was edited.

## Seven reciprocal proof components

1. `thm:p02-hfa-propositional-kernels` ↔ `annex:p2.hfa.kernels`: exact
   finite-sequence substitution from A1–A3/MP CPL to FOL, with premise and
   union supports. Its tautology-existence input is explicitly the current
   cited CPL basis theorem, not Hilbert-FOL adequacy.
2. `thm:p02-hfa-soundness` ↔ `annex:p2.hfa.soundness`: direct semantic
   induction through every literal row, with both dependency-sensitive
   quantified rules checked against assignments and formula coincidence.
3. `thm:p02-hfa-discharge-interface` ↔ `annex:p2.hfa.discharge`: support
   refinement D-minus-discharged-premise, including traced subderivations
   when that premise was unused, Gen distribution and existential
   permutation. It does not license unrestricted Gen.
4. `thm:p02-hfa-alpha-encoding` ↔ `annex:p2.hfa.alpha`: alpha-equivalence
   derived by formula-complexity induction and literal quantifier schemas;
   closed falsum construction; exact FV preservation and substitution
   covariance up to alpha. The proof explicitly treats the syntax
   algorithm's unnecessary bound renamings and is independent of FOL
   completeness.
5. `thm:p02-hfa-existential-duality` ↔ `annex:p2.hfa.exists-duality`:
   empty-support derivations of both primitive ∃ / neg∀neg directions from
   the literal rules, checking ∃E consequent freshness and Gen/distribution
   conditions. This supplies the previously asserted composition bridge.
6. `thm:p02-hfa-proof-bridges` ↔ `annex:p2.hfa.bridges`: H→ND translates
   every literal row and satisfies ND's stricter witness absence and
   nonvacuous discharge; ND→H translates every propositional, quantifier and
   alpha row of the entire equality-free ND tree, using the closed falsum
   encoding and verified support interface. Equality-bearing proof trees are
   not accepted merely because their endpoints are equality-free.
7. `thm:p02-hfa-adequacy` ↔ `annex:p2.hfa.adequacy`: strong adequacy for
   the literal fragment; finite-input ZF and arbitrary-signature/arbitrary-
   premise ZFC scopes; full-language encoding with explicit expansion in the
   atomless-signature case. All proofs have actual reciprocal status labels.

## Noncircular imported dependencies and scopes

- `thm:p02-calculi-derivability-equivalence`, `cited=Kleene1952`, only for
  the exact CPL A1–A3/MP negation/implication tautology basis. A fragment
  tautology is unchanged by the existing CPL translation. A uniform formula
  substitution lifts its finite proof; no FOL theorem is used to certify a
  kernel. This remains an external cited propositional dependency.
- `thm:prop-completeness`, current inherited complete ND proof, supplies
  closed propositional trees for A1–A3 in the reverse H→ND translation.
- `thm:fol-substitution`, formula coincidence and alpha invariance, for
  exact total-substitution soundness; these are syntax/semantics results,
  not FOL calculus adequacy.
- `thm:fol-completeness` and `cor:fol-completeness-countable`, through the
  equality-free specialization explicitly developed in
  `annex:p7.calculi.4`: no identity rules, no congruence quotient. This is
  the existing independent complete calculus used for the forward proof
  bridge. Its arbitrary-signature strong form assumes Choice; supplied
  countable-language form does not. No completeness of the new Hilbert
  composite is a premise of any bridge lemma.

Finite inputs reduce to a finite occurring signature. Every reduct model can
be uniformly expanded by one chosen domain element for all unused functions
and empty unused relations, so this step requires no infinite choice.
For arbitrary premises in arbitrary signatures the inherited ZFC boundary
remains. No computability/decidability claim for unrestricted FOL is made.

## Exact boundary cases and root-owned updates

No inconsistent literal rule was found. Two genuine scope hazards were
handled rather than ignored:

1. The sheet has no alpha rule although total substitution can alter bound
   strings. The new alpha derivation is needed both for direct ND alpha steps
   and to match quantifier instances after the grammar translation.
2. With no equality-free relation atom, a bottom-free fragment contains no
   formula. The literal adequacy statement is then vacuous, not false. A
   full-language falsum encoding requires an explicitly named fresh nullary
   predicate extension; a function-only signature by itself does not supply
   an anchor atom. For a nonempty fragment the encoding's anchor is closed
   before it is used, so no free eigenvariable is smuggled into a context.

Adding equality atoms with identity semantics but no identity schemas is a
different language and would not be complete: an empty interpretation of
that binary relation witnesses the unchanged rules' failure to derive
reflexivity. On the literal sheet the reflexivity formula is outside the
grammar; the note does not call that an inconsistency of the actual sheet.

Root can now link the new result from the Hilbert row of the active
`first-order-calculi-supplement.tex` and Chapter 282's formerly cited
adequacy boundary. The active comparison row already describes primitive
existential elimination correctly but asserts the neg∀neg composition;
the new direct lemma provides its actual local derivations. Route the body
and annex, then merge the unique symbol intake. No bibliography intake is
needed because all controlling keys already exist. Separate original-source
version/whole-extent obligations and the cited CPL dependency remain at
their honest standing; the new proof is editorial, not source transcription.

## Frozen output hashes and verification boundary

SHA-256 after the final substantive edits:

- Body: `159080A064A994426219595B71F2CED174BE3432600CB910C619AE3B8C96305A`
- Annex: `A8A3BC5B7970BF75F0A3FFAF0FD631F7DC7D7067D6BFFD0794FB22321039D621`
- `symbols-intake-p02-hilbert-fol-adequacy.csv`:
  `010B341B6D41600A0F105233CDF99F5CB8641DD3533CE7DCF8BE5F983A49F90D`

Observed controlling-file hashes at source inspection:

- `registry/calculi/hilbert-fol.tex`:
  `FE7AB4AFCBCDCFEF825F940148043A122E9ED71A25DA9708B9DC1C10FCD45AE7`
- `parts/p02/first-order-calculi-supplement.tex`:
  `20A957BAFD06B88AE9413F778B96618989E1F922EC76834DF1B9E9419E6703BB`
- `annex/p02/first-order-calculi-supplement.tex`:
  `8C420A879023118AEF2521B3DAF61FF3933948F770005E6F3833DCF5D834BB03`
- `parts/p14/classical-and-constructive-calculi.tex`:
  `309703C807DCA7C2C1E6EC37C15E90EED4B9B2552E029298DD842FA091940429`
- `parts/p07/calculi-and-derivability-supplement.tex`:
  `D34E8E71075E2B0943AEDFB163C74D11A0B103465550FB89F8E115BF0DC2FC65`
- `annex/p07/calculi-and-cut-elimination-supplement.tex`:
  `CEA69B38858A7FF046E86D0CC3C053CEC821AB5BDA715F8B266B46765D2094E1`
- `restoration/inherited-03240-03428.tex`:
  `36D7779D6B9BB3CAF0C4EF514A79A1C7D8AA10BD4A72290256EA1D09D5DB58CC`

Authoring, exact-file inspection and mathematical dependency checks only.
No children, independent review, build, render or prose test was run. Root
owns integration and consolidated verification. The note does not grant
source admission, independent acceptance or publication completion.
