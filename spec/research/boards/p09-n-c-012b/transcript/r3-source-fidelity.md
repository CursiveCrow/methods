ACCEPT

# Round-three blind opening position — source fidelity

## Verdict and findings

**ACCEPT.** I found no blocker, must-fix, should-fix, unresolved source question,
or other substantive source-fidelity defect in the round-three frozen scope. No
`SF-F*` finding is opened.

The verdict is limited to the hash-pinned N-c-012.b topic-review snapshot in the
round-three charter. It does not close the IEEE-file comparison, any other
N-c-012 presentation, Part IX admission, a build or rendered-handbook review,
human review, final-book completion, or user acceptance.

## Authority and exact material read

I read `spec/research/boards/p09-n-c-012b/charter.md` first, including the
round-three repaired snapshot and its mandatory fresh checks. I then visually
read the source wrapper and every body image at original available resolution:

- `page-01.png`: archival wrapper, used only for the title/author/May 1981
  provenance evidence;
- `page-02.png`: printed p. 46;
- `page-03.png`: printed p. 47;
- `page-04.png`: printed p. 48;
- `page-05.png`: printed p. 49;
- `page-06.png`: printed p. 50;
- `page-07.png`: printed p. 51;
- `page-08.png`: printed p. 52;
- `page-09.png`: printed p. 53;
- `page-10.png`: printed p. 54;
- `page-11.png`: printed p. 55;
- `page-12.png`: printed p. 56;
- `page-13.png`: printed p. 57.

The images, rather than OCR or recollection, controlled every substantive
reading. I also read the complete frozen manuscript scope
`handbook/parts/p09/presentations/n-c-012.tex:370-1048` and
`:1453-1460`, adjacent text at `:1049-1085` and `:1435-1475`, the complete
shared scope `handbook/parts/p09/logic-in-computer-science.tex:599-823`, all
570 lines of `spec/research/p09-pnueli-1977-source-note.md`, the scoped ledger
record `spec/research/p09-source-presentations-lot2-3.md:151-167` with
adjacency, and the complete `Pnueli1977`, `McNaughton1966`, and
`Landweber1969` bibliography entries at
`handbook/bib/handbook.bib:2226-2237`, `:2262-2271`, and `:2273-2281`.

## Checked-clean source correspondence

### C1 — identity, provenance, page map, rights, and version

Checked clean. The title, author, venue, year, printed pp. 46--57, DOI,
first-party NYU memorial route, retrieval date, and source/render identities in
`p09-pnueli-1977-source-note.md:7-40`, the reader disclosure at
`n-c-012.tex:372-382`, the ledger at `p09-source-presentations-lot2-3.md:151-153`,
and `Pnueli1977` at `handbook.bib:2226-2237` agree. The physical-to-printed map
is exactly wrapper page 1 followed by printed pp. 46--57 on physical pages
2--13. The May 1981 wrapper is not presented as a second mathematical edition.
The no-observed-licence and no-inferred-republication-right language is
appropriately narrow. The absent IEEE-direct comparison remains open at
`n-c-012.tex:1453-1460`, `p09-pnueli-1977-source-note.md:565-570`, and the
ledger's line 167.

### C2 — program model, executions, atomicity, fairness, and specification hierarchy

Checked clean against printed pp. 46--49. The dynamic system
`<S,R,s_0>`, possibly infinite carrier, infinite executions, and
nondeterministic transition relation are exact at `n-c-012.tex:384-396`. The
typed sequential maps and transition equation at `:397-413`, and the typed
concurrent maps and one-processor atomic interleaving equation at `:415-439`,
match printed p. 47; the source's deterministic notation is correctly qualified
as nonessential. The source's permitted refinement of an atomic statement is
retained. The early enabled-processor scheduling prose at `:440-443` is kept
distinct from the later formal action-occurrence restriction at `:820-828`.

The explicit reflexive closure reconstruction at `:445-459` supplies the
zero-step case needed for `s_0` to be accessible while disclosing that the
paper calls `R*` a transitive closure. Partial correctness, clean execution,
illegal-intermediate-state examples, mutual exclusion, and deadlock freedom
are separated at `:461-468`. The single-time/invariance and two-time/eventuality
levels, total correctness, accessibility, responsiveness, three-or-more-event
boundary, and quantitative-time boundary are accurately represented at
`:470-487`, without importing a later safety/liveness syntax.

### C3 — P1, P2, ER, metarule I, and Theorem 1

Checked clean against printed pp. 49--50. P1 at `n-c-012.tex:489-497` has the
literal initial and transition-preservation premises. P2 at `:498-523` retains
the source's positive rule instances, decrement to `n-1`, and current-state
target `psi(s)`. Extending the rank predicate's domain to include zero is
explicitly identified as a handbook typing repair. The two-state construction
at `:525-533` is a valid counterexample to combining literal P2 with the
printed strict `j>i` temporal implication.

All of A1--A2 and R1--R4 appear at `:535-564`; the unprinted but required R4
variable-hygiene condition is disclosed at `:566-568`, and first-order
predicate-calculus theorems are retained as axioms at `:569`. Metarule I and
its temporary-hypothesis standing are exact at `:573-585`. Theorem 1 is called
sound and complete only for temporal implications; its argument is labelled a
proof sketch and retains the expressive-assertion-language and pointwise
finite-branching hypotheses at `:587-603`. The source's use of Koenig's lemma,
induction, existential hiding, composition, and pointwise implication is
represented at the printed level of granularity. The deadlock-vacuity problem
created by infinite-only executions before any seriality assumption is
correctly isolated as a source-proof gap at `:605-615`, not silently repaired.
The strict definition, A2, current-state P2 target, inclusive F, and Theorem 3
encoding remain visibly unreconciled at `:617-624`.

### C4 — sequential and concurrent applications

Checked clean against printed pp. 50--52. The source's location-indexed
sequential assertion family, attachment, initial obligation, and typed
per-location transition obligation are exact at `n-c-012.tex:626-655`; the
text correctly says that substitution into P1 reduces the proof to those
obligations rather than deriving the obligations. The finite-path use of A1
and R2 and its Floyd/intermittent-assertion standing are accurately bounded at
`:656-659`.

The full-attachment product-size observation and typed two-family partial
attachment at `:661-688` match printed p. 51. Its sum-size benefit under loose
interaction, recovered exponential work under strong interaction, and the
distinct global-invariant route are not overstated at `:689-693`. The
producer--consumer reconstruction at `:695-730` discloses every renaming and
type, prints all three invariants, and preserves every calculation step:
mutual-exclusion contradiction from invariant (1), nonnegativity and the full
`b <= C-f <= C` upper-bound chain, the mutex-wait case, the remaining
`IS_EMPTY`/`IS_FULL` simultaneous-wait case, and the final contradiction with
strictly positive capacity. The conclusions are exactly mutual exclusion,
`0 <= b <= C`, and absence of deadlock for positive capacity.

### C5 — future-only calculus, quantified schemata, system rules, and Theorems 2--3

Checked clean against printed pp. 52--54. `H(t,p)` is treated as a
metalinguistic evaluation abbreviation for an atemporal state assertion, while
the recursive handbook semantics at `n-c-012.tex:732-758` supplies typed nested
Boolean/F/G evaluation. F and G are inclusive. The source's additional detail
that the absolute present of a system is `s_0` is now stated exactly at
`:756-758`. No X or U constructor is attributed to the paper.

G1--G3, RT, unrestricted pure RG, MP, and derived F2--F3 are exact at
`:760-781`. Q1--Q4 at `:782-798` preserve the two equivalences and two
one-direction implications; the source's failure to delimit the metavariable's
tense-formula range or provide separate domain semantics remains unresolved,
while the handbook's conservative atemporal-use policy is labelled as such.
Theorem 2 at `:800-810` has exactly the pure propositional future-restricted
scope, absolute completeness and decidability claims, and outward proof/S4
referrals. Printed p. 53 states only that complexity results exist elsewhere;
the manuscript correctly supplies no numerical bound or complexity class.

The finite action partition and the literal tail condition are exact at
`:812-828`. Visual inspection of printed p. 53 confirms `j >= i`, not `j > i`;
the displayed equivalent statement therefore correctly requires every action
after every tail point. I1, I2, E, and N, including all state positions and the
designated-action premises, are exact at `:830-858`. N is restricted to the
action-occurrence execution class, and the handbook counterexample at
`:862-869` correctly shows why that restriction is necessary. DI and DN at
`:874-897` match printed p. 54 and are correctly classified as derived
strengthenings of I2 and N. The Example 2 use and accessibility target are
faithfully bounded at `:898-910`. Theorem 3 is stated only as “at least as
strong as ER”; its entire printed proof is accurately described as the skeletal
instruction to encode `p leadsto q` by `p => Fq` and show the ER axioms, with
no invented individual derivations.

### C6 — finite-state package and appendices

Checked clean against printed pp. 55 and 57. Finiteness and the source's
no-halting/no-deadlock seriality assumption occur before proper execution at
`n-c-012.tex:912-924`. Proper executions are exactly initial paths on which
every action labels infinitely many traversed edges. Theorem 4's
`G(p => Fq)` scope and source-sufficient all-state procedure are kept separate
from the disclosed handbook reachable-state pruning at `:926-936`. After
removing q-states, the cyclic strongly connected component criterion at
`:938-951` correctly requires an internal edge for every action; both
directions of the finite-graph argument are sound and do not weaken the source
to outgoing labels.

P and restricted MRG, including the “no P in the derivation” side condition,
are exact at `:953-968`. Theorem 5 retains both printed clauses—decidability of
arbitrary propositional tense-formula validity on a finite system and adequacy
of extended Kb—at `:969-971`; no stronger complexity result is supplied.

Appendix A's externally referred T2/T3 formulas and their corollaries are
separated from Pnueli's local six-step lemma proof at `:973-1002`, with every
formula and proof step matching printed p. 57. Appendix B's monadic
second-order-successor route and infinite-word-language route are both present
at `:1004-1007`. `L_prop(Sigma)`, the atemporal truth set, prefix
concatenation, and all six source recursion clauses are correctly typed and
used at `:1008-1031`. The source's omega-regular terminology is given an
explicit eliminable language-class standing, not retrojected as a Pnueli
LTL-to-Buchi translation. The unprinted acceptor tuple/acceptance condition,
external effective closure/acceptor facts, and externally owned inclusion
decision are kept distinct at `:1033-1046`. The bibliography records for
McNaughton and Landweber agree with Pnueli's printed references 32 and 33.

### C7 — cross-file consistency

Checked clean. The 570-line source note agrees with the reader presentation on
every authority identity, page locator, definition, formula, repair, source
defect, theorem qualification, and external-proof boundary. Its disposition at
`p09-pnueli-1977-source-note.md:552-570` remains pre-admission. The ledger
record at `p09-source-presentations-lot2-3.md:151-167` accurately mirrors the
same source, repairs, qualifications, and pending-round-three status. The three
bibliography entries are consistent with the article and printed references.

The shared temporal section at
`logic-in-computer-science.tex:599-823` defines modern inclusive LTL,
first-order expressiveness, later PSPACE results, safety/liveness, and word
automata under their own sources. The input boundary at line 820 and the
explicit qualifications in `n-c-012.tex:470-487`, `:617-624`, `:732-758`, and
`:1033-1046` prevent those later definitions and results from being attributed
to Pnueli 1977. Adjacent GPSS text at `n-c-012.tex:1049-1085` independently
introduces its strict F/G/X/U presentation, so there is no direct source or
notation collision.

### C8 — exposition, definition order, terminology, and status

Checked clean. The exposition is independently worded and does not reproduce
the scanned pages. Definitions and types precede their uses. Source notation
renamings (`C`, `b`, `mu/e/f`, and the action family) state the collision they
avoid and are used. The local `leadsto` standing is explicitly a statement
family rather than a new handbook LTL constructor. The sole added language
name `L_prop(Sigma)` supplies, at one location, its necessity, exact eliminable
definition, standing as a subset of `S^omega`, distinction from the unprinted
automaton `A_Sigma`, and actual use in the inclusion question
(`n-c-012.tex:1008-1042`). The omega-regular label likewise has an eliminable
standing and a demonstrated use. These satisfy the five-part technical-name
rule. The reader/source-note/ledger language preserves the narrow open status
required by the charter.

## Invariant-by-invariant audit

- **I1:** Satisfied. I used only visual source reading, direct text reading, and
  SHA-256 identity hashing. I ran no tests, test harnesses, automated checkers,
  repository scripts, TeX, handbook-PDF inspection, or builds.
- **I2:** Satisfied. All eight identities matched before substantive review and
  again immediately before this transcript was filed; the exact values are
  recorded below.
- **I3:** Satisfied. The wrapper and all twelve printed pages 46--57 were read
  visually; no substantive conclusion rests on OCR.
- **I4:** Satisfied. Types, quantifiers, all displayed premises and side
  conditions, theorem strengths, proof-sketch/referral statuses, source defects,
  and external-proof boundaries were checked against the controlling images.
- **I5:** Satisfied. Strict `j>i`, P2's current-state target, A2, inclusive F,
  and Theorem 3's `p => Fq` representation are separately printed and the
  unreconciled source tension is explicit.
- **I6:** Satisfied. No X/U grammar, later LTL-to-Buchi translation,
  safety/liveness syntax, or PSPACE classification is attributed to Pnueli
  1977.
- **I7:** Satisfied. Every added technical name in this scope supplies the five
  required local elements; source names and mere notation renamings are not
  inflated into hypothetical theoretical objects.
- **I8:** Satisfied. The body-level reconstruction is complete on the
  author-hosted source, while IEEE-direct comparison remains explicitly open.
- **I9:** Satisfied. This is one independent seat's verdict only; it asserts no
  majority rule or board-level closure.
- **I10:** Satisfied. The acceptance is expressly limited to N-c-012.b topic
  review and does not claim any broader admission, build, visual, human, final,
  or user gate.

## Pre-review and post-review SHA-256 verification

All values matched both before substantive reading and again immediately before
filing:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` | `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB` |
| `tmp/pdfs/p09-pnueli-1977/focs77.ps` | `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F` |
| `tmp/pdfs/p09-pnueli-1977/focs77.pdf` | `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `80F9D4B96FEEBD329F683D5048E31544EDD4A97B3922752AC3D17DAB851D9219` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394` |
| `handbook/bib/handbook.bib` | `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9` |
| `spec/research/p09-pnueli-1977-source-note.md` | `BC88DE02A62B27112B723548D1483D2E8525CFB0EF175273DE4D15A3EAAB5BBF` |
| `spec/research/p09-source-presentations-lot2-3.md` | `5FF3CCC5C8B88882D9218BB4221AEFAEB313EFF15657BCDB427C25F9F6852714` |

## Independence, runtime, and final verdict

I acted only as the source-fidelity seat
`/root/schmidt_smolka_1991_research`. I did not inspect `ledger.md`,
`transcript/chair.md`, any round-one or round-two transcript (including my own),
or either other round-three transcript. I did not request, infer from, discuss,
or contact another reviewer's output. I edited no manuscript, source note,
ledger, bibliography, shared surface, or other agent-owned file; this transcript
is the only file I created.

The harness did not expose a runtime model/version identifier.

**Final verdict: ACCEPT.**
