ACCEPT

# Round-four blind source-fidelity review: N-c-012.b

## Seat, scope, and verdict standard

- Seat: source fidelity, stable agent `/root/schmidt_smolka_1991_research`.
- Verdict: **ACCEPT**. I found no blocker, must-fix, should-fix, consider,
  discard, or unresolved-user source-fidelity item in the exact round-four
  snapshot.
- Review object: the complete round-four scope fixed by
  `spec/research/boards/p09-n-c-012b/charter.md:158-230`: reader presentation
  `handbook/parts/p09/presentations/n-c-012.tex:370-1114,1519-1526`; shared
  integration `handbook/parts/p09/logic-in-computer-science.tex:599-823`; the
  complete source note; source-presentation ledger lines 151-167; the complete
  `Pnueli1977`, `McNaughton1966`, and `Landweber1969` bibliography entries; and
  enough adjacent presentation text to test source and version separation.
- Acceptance standard applied: every authority page and every scoped claim had
  to be read and checked; a hash mismatch, unread page, unsupported assertion,
  incomplete coverage, mathematical uncertainty, or remaining substantive
  defect would have required **REVISE**.

## Identity verification

I verified all eight round-four identities before substantive review and
verified the same identities again after completing the source and artifact
read, immediately before filing this transcript:

| Frozen object | Expected and observed SHA-256 before and after review |
|---|---|
| `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` | `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB` |
| `tmp/pdfs/p09-pnueli-1977/focs77.ps` | `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F` |
| `tmp/pdfs/p09-pnueli-1977/focs77.pdf` | `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `B015988618D84AA836D35D3AA0A1D484438C65910B78BB94CB74577A9FB02C9E` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394` |
| `handbook/bib/handbook.bib` | `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9` |
| `spec/research/p09-pnueli-1977-source-note.md` | `C3EE541610841D57A6FB6729C482919431660CFF896276FDABB330D9D21ADE54` |
| `spec/research/p09-source-presentations-lot2-3.md` | `32F11A80F21E9C33AF3E664EBDEEB778E36B4B81E7A772C5BD91589090962AA0` |

No identity changed during the review.

## Authority reading and visual page control

I visually read the wrapper and every printed source page from the original
page images at `tmp/pdfs/p09-pnueli-1977/page-01.png` through
`page-13.png`, using the images rather than OCR or memory to settle notation.
The wrapper was used only for provenance. The complete substantive body read
was printed pp. 46-57:

| Physical/image page | Printed page | Freshly checked source content |
|---|---:|---|
| 1 / `page-01.png` | wrapper | title, Amir Pnueli, and May 1981 archival-wrapper date |
| 2 / `page-02.png` | 46 | summary, specification hierarchy, invariance and eventuality motivation |
| 3 / `page-03.png` | 47 | dynamic system, infinite execution, exact sequential and concurrent transition equations, deterministic-notation qualification, atomic interleaving, enabled-processor prose |
| 4 / `page-04.png` | 48 | reachability, partial correctness, clean execution, invariants, strict temporal implication |
| 5 / `page-05.png` | 49 | P1, literal P2, natural-number rank, ER opening |
| 6 / `page-06.png` | 50 | ER A1-A2/R1-R4, metarule I, Theorem 1 and proof sketch, sequential and finite-path attachments |
| 7 / `page-07.png` | 51 | full and partial concurrent attachment, source size prose, producer-consumer invariants and proof obligations |
| 8 / `page-08.png` | 52 | producer-consumer conclusion, H, inclusive F/G, absolute present, G1-G3, F2-F3, RT/RG/MP and RG warning |
| 9 / `page-09.png` | 53 | Theorem 2/referrals, Q1-Q4, finite action partition, literal tail condition, I1/I2/E/N and proof phases |
| 10 / `page-10.png` | 54 | DI/DN, Example 2, Theorem 3 and relative-completeness corollary |
| 11 / `page-11.png` | 55 | finite serial graph, proper executions, Theorem 4/SCC route, P/MRG, both Theorem 5 clauses |
| 12 / `page-12.png` | 56 | discussion, qualifications, and references 1-20 |
| 13 / `page-13.png` | 57 | references 21-33, Appendix A external/local proof ownership, Appendix B's two decision routes and exact language recursion |

The physical/printed map is therefore exactly physical page `n` to printed
page `n+44` for `2 <= n <= 13`, as recorded in the source note at lines 25-32
and the reader presentation at lines 372-382.

## Mandatory F27-F35 fresh checks

### F27 — raw-path counterexample action typing and collision

Checked clean. `n-c-012.tex:897-904` uses
`a={(t,t)}` and `c={(s,s)}` as two binary relations in the action partition
`{a,c}`. Both action symbols therefore have the single required type
`S x S`; the infinite raw path repeatedly takes `c`, never `a`, and witnesses
the unsoundness of N without the p. 53 action-occurrence restriction. The
producer-consumer load has already been renamed `b:S->Z` at lines 721-730, so
the counterexample does not reuse that load symbol. Its two N premises and its
failed conclusion are all as claimed.

### F28 — full attachment

Checked clean. `n-c-012.tex:664-686` defines finite index sets and location
enumerations, types every `h_ij:D->{false,true}`, and gives the exact global
formula
`q_full(pi_1,pi_2;u)` with both control equalities and the pair-indexed data
assertion. Lines 674-686 state its metalinguistic standing, distinguish its
`|I||J|` components from the one-indexed partial families, and use that
distinction immediately in the size comparison. The source display is printed
on p. 51. The full-attachment name is not left as an undefined program-semantic
constructor.

### F29 — producer-consumer indicator premises

Checked clean. `n-c-012.tex:721-765` types capacity, load, semaphores, and all
three indicator families. Lines 731-739 accurately say that p. 51 only calls
the indicators one on some locations and zero elsewhere, without listing
support sets. The reconstruction states exactly the source implications it
uses: simultaneous critical sections give `m_1=m_2=1`; mutex blocking gives
`m_i=0` and `mu=0`; simultaneous producer/consumer waits give
`r_1=r_2=e=f=0`; and `0<=s_i<=r_i<=1`. No unprinted support set is inferred.
Lines 740-763 reproduce the three invariant equations and every arithmetic
step for mutual exclusion, `0<=b<=C`, and positive-capacity deadlock exclusion.
This matches printed pp. 51-52 and source-note lines 283-315.

### F30 — state-assertion typing and redundant names

Checked clean. The general state-assertion type
`p:S->{false,true}` is introduced at `n-c-012.tex:458-462`, before P1, P2, ER,
the attachment discussion, or the tense-language construction uses such an
assertion. Its standing as a one-state assertion rather than a tense formula is
explicit. The later `H(t,p)` is correctly identified at lines 767-771 as the
source's metalinguistic evaluation abbreviation, not promoted to a new
object-language operator. I found no redundant one-off invented technical name
in the frozen scope.

### F31 — three path and validity standings

Checked clean. `n-c-012.tex:947-979` separately defines (1) an arbitrary-start
infinite `R`-path from any `s` satisfying the p. 53 action condition, (2) the
source's initial-state proper execution with `t_0=s_0`, and (3) the restricted
system/formula semantic relation `Sigma |=_prop A` quantified over those proper
executions. Lines 977-979 give the relation's metalinguistic standing,
necessity, nonredundancy, and later theorem use. Theorem 4 uses arbitrary-start
continuations in its statewise semantic route at lines 981-1011, while
Theorems 4-5 use the initial-state validity relation at lines 985 and 1029-1034.
This is faithful to printed p. 55 and source-note lines 445-477.

### F32 — attachment-size parameters and proof obligations

Checked clean. `n-c-012.tex:705-719` distinguishes `|I|+|J|` top-level partial
families from `|I||J|` two-process expansion. It correctly calls the latter a
product (at most quadratic in the two displayed location-set sizes), and
reserves exponential cross-product growth for a varying process count through
`prod_h |L_h|`. It also retains the requirement to prove initial truth and
preservation under every relevant processor transition. This is an explicit,
mathematically sound parameterization of p. 51's informal size prose, not an
attribution of a modern complexity theorem to Pnueli; source-note lines 249-281
record the same boundary.

### F33 — SCC formula and proof ownership

Checked clean. `n-c-012.tex:992-1011` first reports only what p. 55 prints: a
component is labelled by actions occurring on edges among its states, without
a set formula or proof. It then visibly marks as handbook-supplied the exact
criterion `a intersect (C x C) != empty` for every action and gives both
directions: an internal edge per action plus strong-connectivity paths yields a
repeated fair closed walk; a fair infinite path in the finite condensation DAG
eventually remains in one component and supplies an internal edge of every
action. Reachability, cyclicity, and deletion of target states are all present.
Source-note lines 485-504 preserve the same source/reconstruction boundary.

### F34 — Theorem 5 adequacy and Appendix B

Checked clean. `n-c-012.tex:1029-1034` states both literal p. 55 clauses:
decidability of restricted finite-system validity for arbitrary propositional
tense formulas, and adequacy of the extended calculus. It then explicitly says
that Pnueli prints no general semantic-validity-to-derivation construction and
that Appendix B treats only decidability. `n-c-012.tex:1067-1113` accordingly
contains only the two semantic decision routes. This matches the source heading
and text on p. 57 and source-note lines 522-527 and 556-602.

### F35 — three Appendix B ownership standings

Checked clean. `n-c-012.tex:1073-1082` separately records Pnueli's own local,
unproved assertion that a finite-state infinite-word acceptor for the proper
execution language can be constructed; it does not assign that assertion to
reference 32 and does not invent an automaton tuple or acceptance condition.
Lines 1084-1105 type the state language and prefix concatenation, reproduce the
complete Boolean/F/G recursion, give the eliminable Buchi-recognizability
standing of “omega-regular,” and assign the imported language and effective
closure machinery to reference 32. Lines 1105-1110 separately assign the
inclusion decision to reference 33 and state that none of those imported facts
is proved locally. Printed p. 57 visibly supports those three distinct
ownership levels; the `McNaughton1966` and `Landweber1969` entries accurately
identify references 32 and 33.

## Criterion-by-criterion source-fidelity coverage

### C1 — identity, provenance, page map, rights, and version

Checked clean. `n-c-012.tex:372-382`, source-note lines 7-40, ledger lines
151-153, and `handbook.bib:2226-2237` consistently identify Amir Pnueli,
“The Temporal Logic of Programs,” FOCS 1977, pp. 46-57, DOI
`10.1109/SFCS.1977.32`, and the NYU author-hosted PostScript route. They
distinguish the May 1981 wrapper from the printed 1977 body, record the exact
physical/printed page map and render status, avoid inferring republication
rights from public access, and state that no IEEE-supplied comparison has been
performed. `n-c-012.tex:1519-1526` keeps that publisher-file comparison open.

### C2 — program model, executions, atomicity, fairness, hierarchy

Checked clean against printed pp. 46-49. `n-c-012.tex:384-443` types
`Sigma=<S,R,s_0>`, infinite initial-state executions, the exact sequential
`N/T` equation, the exact `n`-processor interleaving equation, the
nondeterministic processor selection, fixed other control coordinates,
atomic-statement modelling qualification, and the source's nonessential
determinism qualification. Lines 440-443 keep early enabled-processor fairness
prose distinct from the later formal action condition. Lines 445-490 define
reflexive-transitive `R*`, accessible states, invariant and clean execution,
partial and total correctness, accessibility and responsiveness, strict
temporal implication with `j>i`, and the source's stated omissions concerning
three-event order and quantitative response time.

### C3 — invariance, ranking, ER, and Theorem 1

Checked clean against printed pp. 49-50. `n-c-012.tex:492-521` gives P1 and
literal P2, discloses the zero-rank typing repair, retains `n>0` in rule
instances, and preserves the printed current-state target `psi(s)`. Lines
528-536 supply a valid, explicitly handbook-owned counterexample to combining
that rule with strict `j>i`. Lines 538-588 give every ER form A1-A2/R1-R4,
state the unprinted but necessary R4 variable-hygiene condition, include
first-order predicate-calculus theorems, and correctly type I as a metarule.
Lines 590-618 state Theorem 1 at its source strength: soundness/completeness for
temporal implications, an expressive assertion language, pointwise finite
branching rather than a uniform bound, Koenig's-lemma dependence, an explicit
proof-sketch boundary, and the handbook-discovered deadlock-vacuity gap. Lines
620-627 preserve rather than silently resolve the strict/inclusive source
tension among the definition, P2, A2, inclusive F, and Theorem 3.

### C4 — sequential and concurrent applications

Checked clean against printed pp. 50-52. `n-c-012.tex:629-662` correctly makes
the Floyd verification conditions premises that must be established before P1
yields invariance; it uses location-indexed assertion types and accurately
describes finite-path A1/R2 composition. Lines 664-719 give the exact typed
full and partial two-process attachment formulas and the repaired size
parameterization. Lines 721-765 give the complete producer-consumer example,
positive capacity, collision-free renamings, every source-used indicator fact,
all three invariants, and the full mutual-exclusion, bounded-load, and deadlock
calculation without presenting it as later model checking.

### C5 — future logic, proof systems, quantifiers, Theorems 2-3

Checked clean against printed pp. 52-54. `n-c-012.tex:767-845` keeps H
metalinguistic, defines nested formulas recursively, gives inclusive F/G and
absolute present `s_0`, states G1-G3, RT/RG/MP, F2-F3, and prints Q1-Q4 at
their exact equivalence/implication strengths. It explicitly leaves the
source's Q-schema range unresolved and does not invent domain semantics.
Theorem 2 remains only the pure propositional future-restricted `K_b` result;
the proof, S4 decision route, and complexity work are referred outward, and no
unprinted bound or class is supplied. Lines 847-907 reproduce the finite action
partition and the literal p. 53 tail quantifier `j>=i`, distinguish it from the
earlier enabled-processor prose, give I1/I2/E/N with all premises, and restrict
N to the action-occurrence execution class. Lines 909-945 correctly type
derived DI/DN, state their Example 2 use, and retain Theorem 3's skeletal local
proof and relative-completeness corollary without fabricating the omitted ER
derivations.

### C6 — finite-state package, Theorems 4-5, and appendices

Checked clean against printed pp. 55-57. `n-c-012.tex:947-979` gives finite
seriality, action-labelled paths, the arbitrary-start/proper/validity
distinctions, and exact action fairness. Lines 981-1011 state Theorem 4 and
carefully label reachable-state pruning and the exact SCC criterion/proof as
handbook observations. Lines 1013-1027 reproduce P and the exact MRG
no-P-in-derivation side condition and explain its necessity. Lines 1029-1034
give both Theorem 5 clauses and the missing adequacy proof boundary. Lines
1036-1065 preserve Appendix A's externally owned T2/T3 formulas and
corollaries separately from Pnueli's complete local six-step lemma proof.
Lines 1067-1113 preserve Appendix B's two routes, full language recursion,
types, and three external/local proof boundaries without adding a later
LTL-to-Buchi construction or complexity result.

### C7 — cross-file consistency

Checked clean. The complete source note gives the same identities, source
defects, formulas, result strengths, ownership boundaries, and open status at
lines 1-626. The ledger at lines 151-167 accurately summarizes the same source
record and says round-four fresh unanimous acceptance is still pending rather
than treating repairs or the prior source-fidelity acceptance as admission.
The Pnueli bibliography entry at lines 2226-2237 is accurate; the McNaughton
and Landweber entries at lines 2262-2281 match Pnueli's references 32 and 33.
The shared Part IX surface at
`logic-in-computer-science.tex:599-823` keeps later X/U LTL, GPSS
expressiveness, Sistla-Clarke PSPACE classifications, Alpern-Schneider
safety/liveness, and Vardi-Wolper LTL-to-Buchi work separately sourced and
does not attribute them to Pnueli 1977. The reused Buchi definition at lines
663-686 supports, but does not silently enlarge, the eliminable Appendix B
language-class abbreviation.

### C8 — exposition, definitions before use, and terminology

Checked clean. The reader prose is independently worded and source citations
are located at the paragraphs they support. Definitions and types precede use.
For each handbook-introduced name that carries technical work, the local text
supplies the required exact definition, standing, distinction, necessity, and
use: temporal implication (`n-c-012.tex:473-490`), state assertion
(`458-462`), full attachment (`664-686`), partial attachment (`688-719`), the
restricted system-validity relation (`968-979`), the proper-execution language
(`1073-1082`), and the eliminable omega-regular abbreviation (`1098-1105`).
Collision-avoiding renamings are typed and explained where introduced. Source
notations such as H are described rather than promoted into unsupported new
constructors. I found no hypothetical technical name lacking the user's five
required elements.

## Invariant-by-invariant coverage

- **I1 — scholarly method:** satisfied. I used only direct file reading,
  visual source-image inspection, scholarly reasoning, and SHA-256 identity
  hashing. I ran no tests, test harnesses, automated checkers, repository
  scripts, TeX, handbook-PDF inspection, or builds.
- **I2 — frozen hashes:** satisfied. All eight identities matched both before
  substantive review and after the complete read.
- **I3 — all twelve pages:** satisfied. I visually read printed pp. 46-57 in
  full, plus the wrapper for provenance; images controlled over OCR and memory.
- **I4 — exact formal detail:** satisfied. Types, quantifiers, transition
  equations, rules, side conditions, theorem strengths, proof status, and
  external-proof ownership were checked individually as recorded above.
- **I5 — strict/inclusive tension:** satisfied at `n-c-012.tex:473-536` and
  `620-627`, with the strict `j>i` definition, literal current-state P2, ER A2,
  inclusive F, and Theorem 3 representation kept distinct.
- **I6 — anti-retrojection:** satisfied. The Pnueli subsection expressly
  excludes X/U at lines 787-790 and later Buchi/complexity claims at lines
  1098-1113; shared later results remain separately attributed.
- **I7 — technical names:** satisfied for every introduced name and
  abbreviation, as detailed under C8 and the F28/F30/F31/F35 checks.
- **I8 — publisher comparison:** satisfied. The body reconstruction is based
  on the author-hosted source, while `n-c-012.tex:1519-1526`, source-note lines
  619-626, and ledger lines 153 and 167 leave IEEE-direct comparison open.
- **I9 — unanimity/no majority:** satisfied. Neither the reader, source note,
  nor ledger treats the prior split verdict or the existence of repairs as
  acceptance. This transcript is an independent seat verdict only.
- **I10 — narrow closure:** satisfied. Even this **ACCEPT** can close only the
  N-c-012.b topic-review seat for the exact round-four snapshot and only if the
  charter's other independent seats accept those same identities. It does not
  admit N-c-012 as a whole, Part IX, any ledger-wide gate, a build, handbook
  visual review, human review, final-book completion, or user acceptance.

## Independence, method, runtime, and closure record

I read `charter.md` first and obeyed its blind-review boundary. I did not read
or inspect `ledger.md`, `transcript/chair.md`, any round-one, round-two, or
round-three transcript (including my own), or either other round-four
transcript. I did not request, infer, or discuss another reviewer's position,
and I did not contact another reviewer. I edited no manuscript, shared file,
source note, source-presentation ledger, bibliography, authority, or render;
this transcript is the only file I created.

The harness did not expose an exact runtime model/version. The stable seat
identifier was `/root/schmidt_smolka_1991_research`.

The closure boundary is deliberately narrow: this verdict accepts only the
source fidelity of N-c-012.b on the eight round-four identities recorded above.
It does not resolve the open IEEE-direct comparison and does not establish any
broader topic, part, build, visual, human, publication, or user-acceptance gate.

ACCEPT
