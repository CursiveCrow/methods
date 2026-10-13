# P15 164.11 supplement: Hempel-Oppenheim model-language examples (packet w02ca-p15-028)

## Duty

ED26-P15-CH-systematic-power-C007 / MP-0: the source examples of
Hempel-Oppenheim 1948 pp. 164-173 absent from
thm:p15-power-source-examples: (1) the L1 normal forms (p. 168) with
m=4, m_U=2,1,0,4, l_U=m-m_U (p. 169); (2) the L2 example (p. 166):
8 atoms, 256 minimal sentences, sample minimal sentence, 128-conjunct
minimal normal forms of P(a), Q(a); (3) the non-singular consequence
(Ex)(P(x)vQ(x)) of P(a)vQ(a) (p. 166) against the singular-consequence
clause of thm:p15-power-normal-forms.

## Source read this session

source/references/hempel-oppenheim-explanation-1948/hempel-oppenheim-1948.pdf
(42 physical pages, page 1 a JSTOR cover; printed page = physical + 133;
checked: physical 25 = printed 158, physical 33 = printed 166,
physical 35 = printed 168, physical 36 = printed 169).
Pages 164-169 read as text; printed pp. 166, 167, 168, 169 also read as
page images to recover the negation signs lost in text extraction.
Printed pp. 157-158 read for (7.1a) formal truth/equivalence, (7.1b)
singular, (7.1c) essentially generalized, (7.2b) universe of discourse.

Verified locators used: p. 158 (7.1a), (7.1b), (7.1c), (7.2b);
p. 166 (L1, four minimal sentences in order, L2 eight atoms, 256 minimal
sentences, sample minimal sentence, non-singular consequence, minimal
normal forms of P(a), Q(a) in L1 and 128 conjuncts in L2, vacuous
conjunction); p. 168 (four maximal sentences in order, the four pairs of
normal forms, vacuous disjunction); p. 169 (m=2^n, m_U, l_U=m-m_U,
"m=4, m_U=2,1,0,4", formula (9.1)).

Sample minimal sentence as printed (image of p. 166):
P(a) v P(b) v ~Q(a) v Q(b) v R(a,a) v R(a,b) v ~R(b,a) v ~R(b,b).
It is M_v for v=00100011 in the atom order
P(a),P(b),Q(a),Q(b),R(a,a),R(a,b),R(b,a),R(b,b).

## Files

- handbook/parts/p15/inductive-logic-and-confirmation-w02c-p15-028.tex
  (chapter sec:p15-w02c-p15-028-model-languages)
- handbook/annex/p15/inductive-logic-and-confirmation-w02c-p15-028.tex
  (sec:annex-p15-w02c-p15-028-model-languages)
- handbook/registry/symbols-intake-p15-inductive-logic-and-confirmation-w02c-p15-028.csv

No new bibliography key (HempelOppenheim1948Explanation exists).

## Editorial decisions

- Source connectives ~, v, ., the horseshoe, (x), (Ex) are transcribed as
  in the host chapter; the correspondence is stated in
  def:p15-w02c-p15-028-transcription. L1, L2, m, m_U, l_U are source
  notation.
- Row for Q(a)'s maximal normal form and the row for P(a) and Q(a) are
  computed, not source-stated; the body says so.
- The non-singular boundary is strengthened beyond the source's claim
  ("not of singular form") to "not equivalent to any singular sentence"
  using the source's own semantics (7.1a with soundness; 7.2b
  unrestricted universe). The dual boundary for state descriptions and the
  general atom-extension invariance of g_1 are editorial additions with
  annex proofs.

## Existing treatment found

thm:p15-power-source-examples (1/3 and K1-K3), thm:p15-power-normal-forms
(general normal forms), thm:p15-power-language-choice (score 1/2 with
names a,b). Linked, not duplicated. No other existing treatment of
items (1)-(3) found.

## Continuation

All three items written. Run 2 (this session): removed the arraystretch
redefinition from the L1 table and replaced a workflow word in
thm:p15-w02c-p15-028-nonsingular; re-verified the offset (physical 25,
33, 35, 36 = printed 158, 166, 168, 169) and the p. 158, 166, 168, 169
statements against the held PDF text. Patch request
work/waves/w02ca/patches/w02ca-p15-028.json asks for printed_offset 133 on
the held-sources entry. The G1 hit on the p02-002 research note is not this
packet's edit. Remaining: none known for C007. Insertion into the drivers
is for the lead.
