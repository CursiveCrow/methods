# Vardi 1982: completed reductions and domain correction, 26 October 2026

The held primary is source/references/p09-vardi1982/stoc82-author.pdf.
The scanned original pages 2--7 and 9 were read directly; the layout text
file contains only page breaks. Printed pp. 141--142 give Theorem 5 and
its brief machine-tableau sketch; pp. 142--143 give Remark 2; p. 145 reports
the fixed-point normal-form claim and attributes it to Immerman's paper.
No new source or invented citation is introduced.

Theorem 5 now has complete lower-bound arguments on both axes. The data
proof includes the missing PTIME-to-path-system reduction using complete
cell tokens and binary-premise intermediate points, with a logspace output
enumerator. The expression proof supplies Boolean successor formulas,
initialization from the input word, finite deterministic local updates,
boundary and halting conditions, the designated target tuple, and an
explicit logspace expression generator on the fixed Boolean database.
The existing monotonicity and iteration proof supplies both upper bounds.

The previous Remark 2 annex incorrectly applied the externally cited
C(Y)=C(YF+) normal form to empty-universe Boolean queries. Under the
literal source grammar adopted in the manuscript, any existentially
projected individual variable makes a Boolean expression false on empty
input. A true-on-empty expression therefore has only nullary fixed-point
components, each equivalent to its first-order first iterate. A new proved
lemma establishes this boundary and supplies a finite order-game proof
that even cardinality, with zero even, is a counterexample to all-domain
capture in that literal grammar.

The corrected capture theorem retains the full mathematical scope:
YF+ captures PTIME on nonempty ordered universes, also covers all-domain
positive-rank queries and empty-false Boolean queries, and the explicitly
closed Y handles every all-domain ordered PTIME query. SF captures all
total consistent NPTIME queries, with tuple markers, the already proved
Fagin theorem, a one-relation coding, and singleton/empty exceptions made
explicit. The historical source claims and grammar qualifications remain
visible. The proofs are author reconstructions, not claims about what the
extended abstract printed or about independent source admission.

Verification is recorded in the task's p03-games/vardi-stage directory.
No previously unproved external normal-form step is presented as proved.
The separate full-source requirements and independent consolidated review
remain outside this author correction.
