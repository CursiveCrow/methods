REVISE

# Round-two blind review — mathematical and proof correctness

**Seat:** `/root/p09_math_proof_review`  
**Final verdict:** **REVISE**

I read `spec/research/boards/p09-n-c-012b/charter.md`, including the appended
round-two replacement snapshot, before substantive review. Every round-two
SHA-256 matched before review and again immediately before this filing. I then
visually reread all twelve printed authority pages 46--57 from the scholarly
render, reread `n-c-012.tex` lines 370--902 and 1307--1314, the complete Pnueli
source note, ledger lines 151--164, the complete `Pnueli1977` bibliography
entry, and the relevant shared Part IX temporal-logic surface in
`logic-in-computer-science.tex` lines 599--823.

## Remaining findings

### R2-MP-F1 — must-fix — the attachment displays still contain undefined and mismatched indices

- **Locations:**
  `handbook/parts/p09/presentations/n-c-012.tex:607-644`, especially
  `:608-623` and `:631-643`; related source-note discussion at
  `spec/research/p09-pnueli-1977-source-note.md:208-230`.
- **Claim:** The repaired text correctly reverses the Floyd premise direction,
  but its formulas are not yet fully typed. It introduces assertions
  `q_i(u)` indexed by the integer names in
  `ell_0,...,ell_m`, then writes
  `q_{N(ell_i,u)}(T(ell_i,u))`, although the already typed map
  `N:L x D -> L` returns a location, not an integer index. It also uses
  `u_0` without first declaring the initial state to be
  `<ell_0,u_0>`. In the partial-attachment display, the families
  `p_i(pi_2,u)` and `q_j(pi_1,u)` are used without declaring their domains or
  the two location enumerations.
- **Printed-source evidence:** Printed p. 50 treats `u_0` as the data part of
  the initial state and indexes the local assertion at the successor location
  returned by the next-location function. Printed p. 51's partial attachment
  has one family taking the second process's location and data and another
  taking the first process's location and data.
- **Mathematical harm:** As written, the verification condition applies an
  integer-indexed assertion family to an element of `L`; `u_0` has no local
  definition; and the partial-attachment functions have no declared types.
  Thus the displayed obligations are not literally well-typed even though the
  intended proof direction is now correct. This fails charter I4 and C4's
  exact-typing requirement.
- **Exact correction:** Write
  `L={ell_0,...,ell_m}` and
  `s_0=<ell_0,u_0>`. Define a location-indexed family
  `q_ell:D -> Prop` for every `ell in L` (with
  `q_i` explicitly declared as an abbreviation for `q_{ell_i}`), and state the
  preservation obligation as
  
  `forall ell in L forall u in D,
   q_ell(u) => q_{N(ell,u)}(T(ell,u))`.
  
  For partial attachment, declare
  `L_1={ell_i:i in I}`, `L_2={m_j:j in J}`,
  `p_i:L_2 x D -> Prop`, and
  `q_j:L_1 x D -> Prop` before the displayed conjunction. These declarations
  make the notation eliminable without changing the source argument.

### R2-MP-F2 — must-fix — the producer–consumer result reuses `N` at the wrong type and omits the positive-capacity premise used by the proof

- **Locations:**
  `handbook/parts/p09/presentations/n-c-012.tex:654-658`; corresponding source
  note `spec/research/p09-pnueli-1977-source-note.md:231-233`; the delivery
  summary at `spec/research/p09-source-presentations-lot2-3.md:157` and its
  repair-status assertion at `:163` depend on the same claim.
- **Claim:** At manuscript line 655 the inequality `0 <= n <= N` uses `N` as
  the buffer capacity, but the only live definition of `N` in this
  subsubsection is the next-location function
  `N:L x D -> L` at lines 402 and 406--410. The producer–consumer paragraph
  never resets `N` to a numeric capacity. It also states absence of deadlock
  without the positive-capacity hypothesis used in the source proof.
- **Printed-source evidence:** Printed p. 51 uses lower-case `n` for the
  current buffer load and upper-case `N` for the buffer capacity. At the top of
  printed p. 52, the deadlock argument reaches `N=0` and closes the contradiction
  expressly because the buffer has **positive capacity**.
- **Mathematical harm:** Under the manuscript's live types, `n <= N` compares a
  number with a function and is ill-formed. Even after silently guessing the
  intended scalar meaning, the no-deadlock derivation does not close unless
  capacity positivity is supplied: its final step is precisely the
  contradiction between capacity zero and positive capacity. This is a
  load-bearing omitted hypothesis, not merely an example-label preference.
- **Exact correction:** At this paragraph introduce a noncolliding scalar name,
  for example
  `C in N_{>0}` as the buffer capacity and `n in N` as the current load, explain
  that `C` is used locally to avoid collision with the already typed
  next-location map `N`, and state the conclusions as
  `0 <= n <= C` and absence of deadlock for `C>0`. Mirror that hypothesis and
  notation in the source note and qualify the ledger's exact-example/repair
  claim until the corrected snapshot is freshly reviewed.

## Exhaustive criterion and invariant coverage

- **C1 — checked clean.** The work identity, FOCS pagination, DOI,
  author-hosted route, compressed/decompressed/render hashes, physical-to-
  printed page map, 1981-wrapper status, rights language, bibliography entry,
  and author-copy/IEEE-direct distinction are exact. Manuscript lines
  1307--1314 correctly keep topic review and publisher-file comparison open.
- **C2 — checked clean.** The sequential and concurrent state spaces, typed
  `N/T` and `N_i/T_i` maps, literal transition equations, one-processor atomic
  update, nonessential-determinism qualification, early enabled-processor
  motivation, later action fairness, specification hierarchy, clean-execution
  distinction, and reflexive-transitive `R^*` construction are correct.
- **C3 — checked clean.** P1 is correctly quantified. Literal P2 is typed at
  `n=0`, retains the printed current-state `psi(s)` disjunct, and the displayed
  two-state counterexample genuinely satisfies both premises while refuting
  strict `j>i`. ER A1--A2/R1--R4 are exact; R4's handbook-supplied
  no-free-variable-in-the-consequent condition is the needed hygiene rule.
  Metarule `(I)` has the correct proof-theoretic standing. Pointwise finite
  branching, rather than a uniform numerical bound, is stated before the
  Koenig argument, and the expressiveness/sketch boundary of Theorem 1 is
  preserved. The source's P2/A2/inclusive-`F`/Theorem-3 strictness conflicts are
  all disclosed rather than repaired.
- **C4 — not clean because of R2-MP-F1 and R2-MP-F2.** The Floyd base and step
  formulas now have the correct premise-to-invariant direction, the finite-path
  ER reduction correctly uses A1 plus R2, and the full-versus-partial-versus-
  global attachment distinctions and high-interaction caveat are source-exact.
  The remaining displayed types and the positive producer–consumer capacity
  premise must be repaired.
- **C5 — checked clean.** `H(t,p)` is restricted to atemporal assertions;
  nested `F/G` formulas have recursive inclusive semantics; G1--G3, RT/RG/MP,
  F2--F3, and Q1--Q4 have the exact strengths. RG is confined to the pure
  homogeneous system pending MRG. Theorem 2's propositional scope and external
  proof/decidability referrals are exact. The finite disjoint action partition
  is typed; direct visual reading of printed p. 53 shows the literal tail
  comparison is `j >= i`, and the manuscript's
  `forall i exists j>=i` positive form is the correct negation of the printed
  indefinite-delay condition. I1, I2, E, and N are exact. The nonempty-action
  two-state counterexample satisfies both local N premises and correctly shows
  why action fairness is indispensable. Theorem 3 and its relative-
  completeness corollary remain at source strength.
- **C6 — checked clean.** Finiteness, seriality, proper action-fair execution,
  and the distinction between arbitrary graph paths and proper paths are exact.
  Theorem 4's all-`p`-state source route is reported as the source's sufficient
  route, while restriction to `X` is explicitly disclosed as a handbook
  refinement for initial-state validity. The internal-edge SCC equivalence is
  valid in both directions: strong connectivity constructs a fair repeated
  tour through one internal edge of every action, and any infinite path in the
  finite condensation DAG eventually remains in one SCC. P and MRG are exact;
  the two-state P/RG counterexample proves MRG's side condition necessary.
  Both clauses of Theorem 5 are stated. Appendix A reproduces T2, T3, their
  corollaries, and the six-step local lemma at their correct external/local
  proof ownership. Appendix B is correctly limited to the MSO-successor and
  omega-regular inclusion routes/construction outline.
- **C7 — not clean only as a consequence of the two findings.** The source
  note, ledger, bibliography, and shared Part IX surface otherwise agree. The
  shared surface keeps Pnueli's future-only inclusive calculus separate from
  GPSS `X/U`, modern Buchi translation, safety/liveness classification, and
  PSPACE results. The note and ledger must not claim an exact completed example
  and universally repaired snapshot while the attachment display and capacity
  hypothesis remain defective.
- **C8 — not clean because I4 and I7 fail at the two cited locations.** Every
  other new technical name has a local necessity, exact definition or axiom,
  standing, nonredundancy, and later use. The presentation is independently
  worded; I5's source tension, I6's anti-retrojection boundary, I8's open IEEE
  comparison, I9's unanimity gate, and I10's narrow topic-only scope are all
  preserved.

## Verified round-two hashes

Each matched both before substantive review and immediately before filing:

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` — `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps` — `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf` — `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex` — `83C56ED3E9A17246150C727DCBCA4418F185FB166AA7AF6201D353CDF4467C07`
- `handbook/parts/p09/logic-in-computer-science.tex` — `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib` — `757EBA2102F6D2A1A31299FB990C6D30718BBAE2EA213114AD75C4038463BF60`
- `spec/research/p09-pnueli-1977-source-note.md` — `9BE7FC420BF1987191517960D4209A435B812F828C9A28476E94EBCA96904518`
- `spec/research/p09-source-presentations-lot2-3.md` — `D920A431C50518FD6F976AAC5A98C4826270ED3BA8898D7CC73A60231FE92F5B`

The harness did not expose a runtime model/version. I did not inspect
`ledger.md`, `transcript/chair.md`, any round-one transcript (including my own),
or either other round-two transcript; I did not contact another reviewer. I
made no edit outside this assigned transcript and ran no tests, automated
checkers, repository scripts, TeX, handbook-PDF inspection, or builds.

**Final verdict: REVISE.**
