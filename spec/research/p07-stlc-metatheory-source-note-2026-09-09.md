# Completing the arrow-only simple-type normalization dependency

This block completes the previously sketched substitution/subject-reduction
and strong beta-normalization arguments required by the handbook's exact
registered arrow-only STLC. It supplies actual body statements and four
reciprocal annex proofs in `handbook/parts/p07/stlc-metatheory.tex` and
`handbook/annex/p07/stlc-metatheory.tex`.

The author read the actual sheet, active inherited STLC passage, inactive
normalization chapter and its sketch annex before writing. The new statements
reuse the existing public subject-reduction and strong-normalization identities
from the inactive chapter. That chapter remains unrouted. The active inherited
presentation and its own hook identities remain intact, with a separate full
derivation now available. This does not complete natural-deduction normalization
for all connectives, polymorphic normalization, or an entire source book.

## Controlling source and exact extent

- Girard, *Proofs and Types*, translated and with appendices by Paul Taylor and
  Yves Lafont. Author/translator-hosted [distribution page](https://www.paultaylor.eu/stable/Proofs%2BTypes.html)
  and [actual PDF](https://www.paultaylor.eu/stable/prot.pdf).
- Local file: `source/references/p07-stlc-normalization/girard-lafont-taylor-prot-online.pdf`.
- 947,152 bytes; 183 physical pages; SHA-256
  `909424159082d3f31d190c20b1a9b4dd39355b527bc1c680fb0aa763913f56dc`.
- Actual copyright page: first published 1989; reprinted with minor corrections
  1990; reprinted for the Web 2003. This manifestation has its own bibliography
  identity and does not stand for an unverified original printing.
- Complete Chapter 6, printed pages 41--45 (physical 49--53), was read. The
  present proof uses Sections 6.1, 6.2.1, 6.2.3, 6.3.2 and 6.3.3 for the exact
  arrow-only target. The product cases read in 6.2.2 and 6.3.1 remain outside
  this host calculus, which has no product constructor.
- Selinger arXiv:0804.3434v2, printed pages 71--72, was read only as a comparison:
  those pages state normalization but do not supply its proof. The new full
  derivation does not attribute its missing closure steps to that statement.

## What is supplied

1. Context extension, exchange, bound-variable renaming and every variable,
   application and abstraction case of simultaneous typing substitution.
2. Subject reduction at the root, under an abstraction and in both application
   positions, followed by the finite-reduction consequence.
3. A complete reducibility proof: existence of finite reduction heights;
   substitution/reduction interaction, including repeated and erased copies;
   all three closure properties at base and arrow types; controlled beta
   expansion; the abstraction argument with its strong-normalization premise;
   every fundamental-lemma case and the identity-substitution conclusion.
4. Typed inert constants, including an arbitrary constant signature, by a
   finite fresh-variable replacement argument.

The auxiliary predicates here range over raw annotated terms. Typability is
used in the fundamental lemma. This explicit convention avoids an unstated
compatibility requirement between arbitrary open typing contexts. The proof
still reaches the full original open-term arrow-only target. Neutral means
non-abstraction and includes a beta-redex application; it does not mean normal.

The source's abstraction argument uses the body's reduction height. The new
derivation explicitly establishes that premise by substituting a fresh variable
and lifting reduction, before invoking height induction. Arbitrary beta
expansion is not claimed to preserve strong normalization.

## Authoring standing

Root integration now routes both files and merges the five symbol records and
the distinct web-reprint bibliography entry. The original active STLC passage
in `handbook/restoration/inherited-12030-12100.tex` explicitly fixes compatible
beta reduction and links its subject-reduction and normalization statements
directly to these complete proofs. Its old sketch/omission paragraphs are
replaced by those exact applications. The frozen source is unchanged.

Source reading and proof construction are authoring work. Bibliography/symbol
intakes preserve the new version and notation; root owns their integration.
The new normalization result provides the exact public label already used by
the monotonicity chapter. Its inert-constant corollary supplies that chapter's
constant-symbol case explicitly. Independent acceptance and the final
manuscript build/output checks remain for the consolidated batch.
