ACCEPT

# Round-five blind source-fidelity review: N-c-012.b

## Opening position

**Verdict: ACCEPT.** I found no blocker, must-fix, should-fix, or unresolved
source-fidelity defect in the exact round-five snapshot. I independently
checked the complete authority and frozen artifact scope; the result is not an
inference from an earlier review or from another seat.

- Seat: source fidelity.
- Stable agent identifier: `/root/schmidt_smolka_1991_research`.
- Frozen reader scope: `handbook/parts/p09/presentations/n-c-012.tex:370-1178`
  and `:1583-1590`.
- Frozen shared scope:
  `handbook/parts/p09/logic-in-computer-science.tex:599-823`.
- Frozen evidence scope: the complete
  `spec/research/p09-pnueli-1977-source-note.md`,
  `spec/research/p09-source-presentations-lot2-3.md:151-167`, and the complete
  `Pnueli1977`, `McNaughton1966`, and `Landweber1969` bibliography entries.
- Boundary context read: `n-c-012.tex:350-369,1179-1225,1560-1590` and ledger
  lines 145-172, enough to test adjacent Kamp, GPSS, Sistla--Clarke, and
  Alpern--Schneider separation.
- Authority scope: provenance wrapper plus every printed body page 46-57.

## Frozen identities

I computed all eight SHA-256 values before substantive reading. I recomputed
them after the complete authority/artifact review and immediately before filing
this transcript. Every value matched the charter both times:

| Object | Expected and observed SHA-256 |
|---|---|
| `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` | `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB` |
| `tmp/pdfs/p09-pnueli-1977/focs77.ps` | `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F` |
| `tmp/pdfs/p09-pnueli-1977/focs77.pdf` | `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `1FABE2120A026468AE21DD2BC116A92DE9AAE048D84655032DA4F7048B82620E` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394` |
| `handbook/bib/handbook.bib` | `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9` |
| `spec/research/p09-pnueli-1977-source-note.md` | `B27AAA9E6C69403998671A924B7F1883DBC2122048D7CF47124464CA63B65803` |
| `spec/research/p09-source-presentations-lot2-3.md` | `3065E52284FF29AAD53121398C3307D691955C13358AE9E314819285A3534203` |

No frozen identity changed during review.

## Complete visual authority read

I visually reread `page-01.png` through `page-13.png` at original detail. I did
not use OCR as authority. `page-01.png` visibly bears the title, Amir Pnueli's
name, and the May 1981 wrapper date. The substantive pages were:

| Image | Printed page | Source matter checked |
|---|---:|---|
| `page-02.png` | 46 | title and affiliations; summary; invariance/eventuality hierarchy; scope and motivation |
| `page-03.png` | 47 | dynamic system; infinite execution; exact sequential and concurrent transition equations; nondeterminism; atomicity; enabled-processor prose |
| `page-04.png` | 48 | explicit-time hierarchy; accessible states; invariance, partial correctness, clean execution, mutual exclusion and deadlock; strict temporal implication |
| `page-05.png` | 49 | accessibility/responsiveness; scope exclusions; P1; literal P2; A1-A2 and R1-R4 |
| `page-06.png` | 50 | first-order axioms; metarule I; Theorem 1 and its proof sketch; sequential attachment; Floyd conditions; finite-path attachment |
| `page-07.png` | 51 | full/partial concurrent attachment; source size prose; producer-consumer invariants and initial/preservation obligations |
| `page-08.png` | 52 | producer-consumer proof conclusion; H; inclusive F/G; absolute present; G1-G3, F2-F3, RT/RG/MP; RG warning |
| `page-09.png` | 53 | S4 and Theorem 2 wording; complexity referral; Q1-Q4; finite action partition; literal `j>=i` tail; I1/I2/E/N |
| `page-10.png` | 54 | derived DI/DN; Theorem 3 and corollary; Example 2 proof structure |
| `page-11.png` | 55 | finite serial systems; proper executions; Theorem 4 and SCC route; P/MRG; both Theorem 5 clauses |
| `page-12.png` | 56 | discussion, limitations, and references 1-20 |
| `page-13.png` | 57 | references 21-33; Appendix A's referred and local proofs; Appendix B's two routes, atomic-language display, recursion, closure and inclusion referrals |

This confirms the physical/printed map stated at source-note lines 25-32 and
reader lines 372-382: physical pages 2-13 map to printed pages 46-57 by
`printed = physical + 44`. The wrapper is provenance packaging, not a second
mathematical edition.

## F27-F35 reconsidered from the round-five text

### F27 - raw-path counterexample

Checked clean at `n-c-012.tex:960-967` against printed p. 53. The action symbols
`a={(t,t)}` and `c={(s,s)}` are both binary relations on `S`; they form the
stated two-member partition and have no type change. The producer-consumer load
is `b:S->Z` at lines 764-773, so no action/load collision remains. With `p`
only at `s` and `q` nowhere, both local N premises hold, while the raw
`s,s,...` path never takes `a` and refutes the conclusion without the formal
action-occurrence restriction.

### F28 - exact full attachment

Checked clean at `n-c-012.tex:707-729` against printed p. 51. The finite index
sets and both location enumerations precede the typed family
`h_ij:D->{false,true}`. The displayed conjunction has both control equalities
and the correct pair-indexed assertion. Lines 717-729 state that it is a
metalinguistic representation of one global state assertion, explain why the
full-attachment name is needed to distinguish pair indexing from the partial
families, and use that distinction immediately in the size comparison.

### F29 - source-supplied indicator facts only

Checked clean at `n-c-012.tex:764-811` against printed pp. 51-52. Capacity,
load, semaphores, and all indicator families are typed. Lines 773-784 accurately
say the source does not enumerate complete indicator support sets and list only
the consequences actually used. No unprinted location set is manufactured.
The invariant equations and all arithmetic steps at lines 785-808 are exact.

### F30 - state assertions before use and technical-name discipline

Checked clean. `n-c-012.tex:458-462` types a state assertion as
`S->{false,true}` and distinguishes it from a tense formula before P1, P2, ER,
or the tense language uses it. `H(t,p)` is explicitly only the source's
metalinguistic evaluation abbreviation at lines 813-817. I found no redundant
one-off invented name in the frozen subsection.

### F31 - arbitrary paths, proper executions, and restricted validity

Checked clean at `n-c-012.tex:1010-1042` against printed p. 55. The text
separates an arbitrary-start infinite action-condition path from a proper
execution beginning at `s_0`, then defines `Sigma |=_prop A` over the latter.
The relation's type, metalinguistic standing, necessity, and use in Theorems 4
and 5 are explicit. The arbitrary-start property is used only for the
continuation test; the theorem statements use initial-state validity.

### F32 - attachment size and retained proof obligations

Checked clean at `n-c-012.tex:748-762`. The partial top level has
`|I|+|J|` written families, the fully unfolded two-process case has product
`|I||J|` size (at most quadratic in those two set sizes), and exponential
growth is reserved for varying process count through `prod_h |L_h|`. Lines
759-761 retain initial-truth and per-transition preservation obligations for
global invariants. This is a disclosed mathematical parameterization of p. 51's
informal complexity prose, not an unprinted source theorem.

### F33 - SCC criterion and handbook proof ownership

Checked clean at `n-c-012.tex:1055-1074` against printed p. 55. The reader first
states the source's component-label sentence and explicitly says that the paper
prints no set formula or two-direction proof. It then labels as
handbook-supplied the exact internal-edge condition
`a intersect (C x C) != empty` for every action. Both directions are present:
chosen internal action edges plus strong-connectivity paths yield a repeatable
fair closed walk; a fair infinite path in the finite condensation DAG
eventually remains in one component and supplies every internal action edge.
Reachability, cyclicity, and target-state deletion are not omitted.

### F34 - Theorem 5 adequacy boundary

Checked clean at `n-c-012.tex:1092-1097` against printed p. 55 and Appendix B
on p. 57. Both Theorem 5 clauses are stated: restricted semantic validity is
decidable, and valid propositional tense formulas are derivable in the extended
calculus. The text expressly records that no general derivation construction
is printed for adequacy and that Appendix B addresses only decidability.

### F35 - Appendix B's three ownership levels

Checked clean at `n-c-012.tex:1130-1177` against printed p. 57. Pnueli's local
assertion that a finite-state acceptor for the proper-execution language can be
constructed is kept local and unproved, with no invented tuple or acceptance
condition and no assignment to reference 32. Reference 32 is attached only to
the imported omega-regular/effective-closure machinery. Reference 33 is
attached separately to the inclusion decision. The complete recursion and the
absence of a later LTL-to-Buchi translation or complexity classification are
also explicit.

## F36-F40 mandatory round-five checks

### F36 - P2 typing, two independent counterexamples, and repair standing

Checked clean at `n-c-012.tex:501-552` and source-note lines 139-196 against
printed p. 49.

1. The source says `n>0` but prints `A(s',n-1)`. The reader extends the
   predicate's domain to `N_0` only to type the `n=1` instance, retains `n>0`
   in both rule premises, retains the literal current-state disjunct `psi(s)`,
   and labels the totalization and universal closures as handbook repairs.
2. The zero-boundary counterexample at lines 528-535 works independently of
   strict futurity: on `a,b,b,...`, `psi` is false everywhere and `A` holds at
   `(a,1)` and `(b,0)`. The first P2 premise holds, the only true positive-rank
   transition premise uses `A(b,0)`, and even inclusive eventuality fails.
3. The strict-future counterexample at lines 544-552 is different: `psi` holds
   at the current `a` state and discharges the literal `psi(s)` premise, while
   no later state satisfies `psi`; hence the printed `j>i` conclusion fails.
4. The proposed `forall s, not A(s,0)` boundary at lines 536-542 is correctly
   identified as an unprinted sufficient repair only for inclusive eventuality.
   If no target holds, a chosen positive witness rank must decrease on each
   step of the infinite execution until forbidden rank zero is required. It
   does not repair the separate strict-current-target problem and is not added
   to literal P2.

The manuscript therefore separates well-typedness, soundness, strictness, and
source/reconstruction ownership exactly as required.

### F37 - R4's parameterized state-assertion family

Checked clean at `n-c-012.tex:554-606` and source-note lines 198-226 against
the p. 49 R4 display. One nonempty parameter domain `U` and one exact family
`p-hat:S x U->{false,true}` are used throughout. Every specialization
`p-hat_u` and the pointwise existential
`(exists_U p-hat)(s) iff exists u in U, p-hat(s,u)` is an ordinary state
assertion, not a tense formula. The rule premise means one derivation uniform
in arbitrary `u`; the consequent and every open assumption must be independent
of `u`. These eigenparameter/hygiene conditions are sufficient for the typed
first-order reading, are distinguished from the source's untyped display, and
are not presented as printed side conditions.

### F38 - metarule I and Theorem 1 use the same family

Checked clean at `n-c-012.tex:608-660` and source-note lines 228-275 against
printed p. 50. I specializes the already defined family to
`N_0={0,1,2,...}`. Its base case is `|- p-hat_0 leadsto q`; its step is a
derivation of the successor instance under the displayed temporary hypothesis
for arbitrary `n`; and its conclusion yields each indexed instance. `q` is
independent of `n`. R4 then forms the already typed pointwise existential state
assertion. Theorem 1 uses the same form `P:S x N_0->{false,true}`, its
specializations `P_n`, and the pointwise assertion `s |-> exists n P(s,n)`.
The reader also accurately retains expressive assertion language, pointwise
finite branching rather than a uniform bound, Koenig's-lemma dependence,
proof-sketch status, and the independently disclosed deadlock-vacuity gap.

### F39 - printed `m_i=1` implication

Checked clean at `n-c-012.tex:773-808`, source-note lines 330-365, and printed
pp. 51-52. The reconstruction states both directions that the actual proof
uses: simultaneous critical-region membership gives `m_1=m_2=1`, and the
source's p. 52 sentence says `m_i=1` places process `i` in its critical section
and therefore excludes waiting on a semaphore. Consequently, from a blocked
process's `m_i=0` and `mu=0`, the first invariant yields `m_{3-i}=1`, and the
other process is not blocked. This supplies the exact missing inference without
asserting a complete unprinted support set.

### F40 - Theorem 2 model class and Appendix B atomic-language typing

Both remaining round-five technical corrections checked clean.

**Theorem 2.** `n-c-012.tex:881-908` precisely preserves printed pp. 52-53:
Pnueli calls the pure propositional future-restricted calculus complete in the
absolute sense and decidable, refers outward for the full proof, invokes S4 for
decidability, and states no complexity bound or class. The reader then marks
the model-class qualification as handbook analysis. Its displayed formula

`(Fp and Fq) -> (F(p and Fq) or F(q and Fp))`

is valid under the reader's inclusive linear-execution semantics. Given future
witness positions for `p` and `q`, their linear order makes the earlier witness
satisfy its letter together with eventual occurrence of the other; the outer F
then holds. It fails on the stated reflexive-transitive S4 frame: at the root,
one incomparable reflexive terminal successor satisfies only `p` and another
only `q`. The root satisfies `Fp and Fq`, but no accessible state satisfies
either `p and Fq` or `q and Fp`. Thus the S4 referral does not establish
completeness for the displayed linear semantics. The text warrants only an
unresolved source model class and does not falsely reject Pnueli's printed
claim under every possible interpretation.

**Appendix B.** `n-c-012.tex:1147-1160` and source-note lines 638-652 faithfully
type p. 57's display. Each state is explicitly embedded as a one-letter word in
`S^1 subseteq S*`, so `[[p]]` is a finite-word language and can be the left
operand of the declared prefix-concatenation operation
`U subseteq S*`, `V subseteq S^omega`. Therefore
`L(p)=[[p]]S^omega` is a well-typed language of infinite words whose first
letter satisfies `p`, exactly matching the printed
`(s_1+...+s_m)S^omega` construction. No state is confused with a set of
infinite words, and the source recursion is unchanged.

## Criterion-by-criterion review

### C1 - source identity, provenance, rights, page map, and version

Checked clean. Reader lines 372-382, source-note lines 7-40, ledger line 153,
and `handbook.bib:2226-2237` consistently identify Amir Pnueli, the FOCS 1977
paper, printed pp. 46-57, DOI `10.1109/SFCS.1977.32`, and the NYU
author-hosted PostScript. They distinguish the May 1981 wrapper from the body,
describe PDF/PNG files only as scholarly renders, and infer no republication
right from public hosting. Reader lines 1583-1590 and the evidence surfaces
leave IEEE-direct comparison open.

### C2 - program model, executions, atomicity, fairness, hierarchy

Checked clean against printed pp. 46-49. Reader lines 384-443 give
`Sigma=<S,R,s_0>`, infinite initial-state executions, possible infinite state
space and nondeterminism, exact sequential `N/T` types and transition equation,
exact concurrent interleaving and unchanged control coordinates, nonessential
determinism, atomic-statement granularity, and the permitted refinement into
smaller steps. Lines 445-490 give reflexive-transitive reachability, state
assertions, invariance, partial correctness, clean execution, mutual exclusion,
deadlock, strict temporal implication, total correctness, accessibility,
responsiveness, and the printed three-event/quantitative exclusions. Early
enabled-processor prose remains distinct from p. 53's action-occurrence rule.

### C3 - P1/P2, ER, Theorem 1, and proof assumptions

Checked clean against printed pp. 49-50. Reader lines 492-552 reproduce P1 and
literal P2 with all disclosed typing and soundness boundaries. Lines 554-606
give A1-A2 and R1-R4 at exact strengths, include first-order theorems, and
clearly own the R4 typing/hygiene reconstruction. Lines 608-648 type I and the
Theorem 1 family. Lines 629-660 preserve the theorem's source strength,
expressiveness and pointwise finite-branching assumptions, Koenig proof
dependency, proof-sketch status, and deadlock-vacuity gap. Lines 662-670 keep
the zero-rank issue separate from the strict/inclusive tensions involving P2,
A2, F, and Theorem 3.

### C4 - sequential and concurrent applications

Checked clean against printed pp. 50-52. Reader lines 672-705 type
location-indexed sequential assertions and correctly make the Floyd conditions
premises whose proof enables P1, while finite-path reasoning is decomposed into
A1/R2 steps. Lines 707-762 give exact full and partial two-process formulas,
their metalinguistic standing, and the warranted size/proof-obligation
qualification. Lines 764-811 give all producer-consumer types, source-used
indicator implications, three invariant equations, and every deduction for
mutual exclusion, `0<=b<=C`, and deadlock exclusion under `C>0`.

### C5 - future calculus, quantifiers, system rules, Theorems 2-3

Checked clean against printed pp. 52-54. Reader lines 813-879 distinguish H
from the object language, define inclusive recursive F/G semantics and absolute
present `s_0`, reproduce G1-G3, RT/RG/MP, F2-F3, and Q1-Q4 at their exact
equivalence/implication strengths, and leave the source's quantifier-schema
range unresolved. Lines 881-908 give Theorem 2's literal assertion and referral
boundaries plus the warranted model-class counterexample. Lines 910-970 give
the finite disjoint action partition, literal `j>=i` tail condition,
I1/I2/E/N with premises, N's restricted execution class, and a correct raw-path
counterexample. Lines 972-1008 type derived DI/DN and preserve Example 2 and
Theorem 3 at their printed proof/referral granularity.

### C6 - finite systems, Theorems 4-5, and appendices

Checked clean against printed pp. 55-57. Reader lines 1010-1042 give finite
seriality and exact arbitrary-start/proper/validity standings. Lines 1044-1074
state Theorem 4 and distinguish source wording from handbook reachability and
SCC reconstruction. Lines 1076-1090 give P, MRG's exact no-P-in-the-derivation
condition, and its necessity. Lines 1092-1097 state both Theorem 5 clauses and
the adequacy gap. Lines 1099-1128 keep externally owned T2/T3 and corollaries
separate from Pnueli's local six-step lemma proof. Lines 1130-1177 type both
Appendix B decision routes, the proper-execution language, atomic and composite
language recursion, and all local/external ownership boundaries.

### C7 - cross-file consistency and anti-conflation

Checked clean. The complete source note at lines 1-696 agrees with the reader
on identities, source defects, formal reconstructions, theorem strengths,
proof ownership, and open status. Ledger lines 151-167 accurately summarize the
same record and say the new repairs await fresh unanimous review. The three
bibliography entries at lines 2226-2237 and 2262-2281 correctly identify the
paper and Pnueli's references 32 and 33. Shared Part IX lines 599-823 keep later
X/U LTL, GPSS expressiveness, Sistla--Clarke PSPACE results,
Alpern--Schneider safety/liveness, and Vardi--Wolper LTL-to-Buchi work under
their own sources. Adjacent `n-c-012.tex:1179-1225` explicitly marks GPSS's
strict operators as source-specific. No later grammar, translation, semantic
class, or complexity theorem is retrojected into Pnueli 1977.

### C8 - independent exposition, definitions, and technical names

Checked clean. The exposition is independently worded and citations are
located at the claims they support. Definitions and types precede use. Each
handbook-introduced technical name or abbreviation that does work locally
supplies necessity, exact definition, standing, nonredundancy, and subsequent
use: temporal implication (`473-490`), state assertion (`458-462`), the R4
parameter family and pointwise existential (`554-606`), full and partial
attachments (`707-762`), restricted system validity (`1031-1042`), the proper
execution language (`1136-1145`), the one-letter atomic language (`1147-1154`),
and the eliminable omega-regular abbreviation (`1162-1169`). Collision-avoiding
renamings are typed and justified. I found no unsupported hypothetical name.

## Invariant-by-invariant review

- **I1:** satisfied. The review used source-image reading, direct text reading,
  scholarly reasoning, and SHA-256 identity checks only. I ran no tests, test
  harnesses, automated checkers, repository scripts, TeX, handbook-PDF
  inspection, or builds.
- **I2:** satisfied. All eight hashes matched before substantive work and again
  immediately before filing.
- **I3:** satisfied. I visually reread every printed page 46-57 and the wrapper;
  images controlled over OCR and memory.
- **I4:** satisfied. Types, quantifiers, premises, side conditions, theorem
  strength, proof status, and external-result boundaries were checked
  individually as recorded above.
- **I5:** satisfied. Strict `j>i`, literal P2/current target, A2, inclusive F,
  and Theorem 3's representation remain visibly distinct at reader lines
  473-552 and 662-670. The new zero-boundary defect is not conflated with that
  strictness tension.
- **I6:** satisfied. Reader lines 833-836 and 1173-1177 exclude X/U,
  later LTL-to-Buchi translation, safety/liveness syntax, and PSPACE from the
  Pnueli presentation; shared later results remain separately sourced.
- **I7:** satisfied. The five-part technical-name requirements are met at the
  local definitions identified under C8, including the newly typed R4 family
  and one-letter language.
- **I8:** satisfied. Body-level reconstruction uses the author-hosted source,
  while IEEE-direct comparison remains explicitly open in reader lines
  1583-1590, source-note lines 689-696, and ledger lines 153 and 167.
- **I9:** satisfied. The evidence surfaces report the previous split verdict
  and state that incorporation is not acceptance; this transcript is only one
  independent round-five seat verdict.
- **I10:** satisfied. Acceptance is limited to N-c-012.b source fidelity on the
  exact round-five hashes. It does not admit N-c-012 as a whole, Part IX, any
  ledger-wide gate, a build, handbook visual review, human review, final-book
  completion, or user acceptance.

## Independence, method, runtime, and closure boundary

I read the charter before substantive work, including the complete round-five
snapshot and all mandatory obligations. I did not inspect `ledger.md`,
`transcript/chair.md`, any r1-r4 transcript (including my own), or either other
r5 transcript. I did not contact another reviewer or request, infer, or discuss
another seat's result. I edited no reader, shared source, note, ledger,
bibliography, authority, render, or other review record. This transcript is the
only file created.

The harness did not expose an exact runtime model/version.

The closure boundary is narrow: this verdict accepts only the source fidelity
of N-c-012.b on the eight round-five identities above. It leaves the
IEEE-direct comparison, the rest of N-c-012, Part IX admission, all build and
visual gates, human review, final publication, and user acceptance open. It has
topic-review effect only if the other blind seats independently accept the same
snapshot under the charter's unanimity rule.

ACCEPT
