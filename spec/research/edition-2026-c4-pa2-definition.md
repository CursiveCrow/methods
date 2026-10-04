# Edition 2026, C4: the active definition of PA2

Date: 7 September 2026. Requirement: R-032, within C4. This is an authored
definitional completion, not independent acceptance or completion of all C4.

## Scope and evidence

The original requirement calls for the language, axioms and semantics of PA2
before its first use. The active source at
`handbook/restoration/inherited-12356-12414.tex:4-21` supplies the successor
axioms and full second-order induction. Lines 55-58 refer to addition and
multiplication recursion axioms without displaying them. The next fragment,
`inherited-12415-12536.tex:35-51`, uses PA2 as the antecedent of a single
second-order sentence in the expanded signature.

The frozen source at `source/formal-logic-reference.tex:9103-9107` explicitly
supplies the four arithmetic recursion laws, also active in
`handbook/restoration/inherited-09099-09111.tex:4-10`. Its full Peano axioms
are at frozen lines 12359-12376. The active full-assignment definition and
quantifier clauses are in `inherited-12290-12355.tex:4-29`.

The inactive `handbook/parts/p02/second-and-higher-order-logic.tex:92-118`
was inspected as a previous implementation lead. It is not credited as current
reader content or as an independently verified external-source presentation.
The added definition reconstructs the already specified intended arithmetic
object from the displayed source axioms; it does not assert consultation of
an inaccessible external book or identify a new logical system.

## Added manuscript content

`handbook/parts/p02/pa2-definition.tex` defines the stable label `def:p02-pa2`.
It gives the signature and arities, lists all seven closed conjuncts, and states
full semantics over all subsets with total functions on a nonempty domain. It
explicitly distinguishes the single second-order induction sentence from a
first-order scheme and the expanded-signature antecedent from the successor-only
axiom set. All variables are bound; the displayed list contains two successor
sentences, one induction sentence and four recursion sentences.

The integration agent inserted the new file after `scope-SRC-12356-12414` and
before `scope-SRC-12415-12536` in `parts/p02.tex`. The lead read the actual
driver at lines 48-54 after insertion and verified that the definition precedes
the active full-validity use and the later comparison table. No frozen source
fragment is rewritten for this addition.

## Baseline identities and review boundary

Added definition file SHA256:
`6a5467b748c91f6cb9c8484e6c7e7b122a0268ecc80fc3a8c7213b92251d4a63`.

- `inherited-12356-12414.tex`: SHA256
  `3b850ff37842e3e024ac32b23712aa199db010ad2249e764bb590afc2ed89a04`.
- `inherited-12415-12536.tex`: SHA256
  `d4ff50a3145acac19b3e7a6054bcf0aef4aac1eb2e774f825ade02af2693f667`.
- Inactive `second-and-higher-order-logic.tex`: SHA256
  `72551e0b9ef0b8051f15a5efbde7107b147607f314a1f411641157134cc60ca0`.

The definition supplies the missing object for R-032. It does not finish the
subsequent proof sketch of noneffective full validity, the independent equality
translation, S-013, or D-P2-010. Those remain separate obligations. Independent
source/content review and production checks have not yet been performed.
