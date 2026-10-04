# Round 6 adversarial publication and terminology review: Rabin 1969

## Disposition

I independently reviewed the entire Frozen Round 6 snapshot under the
adversarial-publication-and-terminology mandate.  The reconstruction is
mathematically and historically strong, and the reader itself passes the
load-bearing ordinary/dual, finite/infinite, source/later-source, and
decidability/complexity distinctions.  The snapshot nevertheless has one
unresolved **must-fix** first-use defect: the detailed source note and compact
record use Rabin's technical notion of a well-founded obligation mapping
without giving the exact source definition required by R12 and R26.  The
correct definition later present in the reader does not make those separate
first uses compliant.

Accordingly, this report rejects the unchanged Round 6 snapshot on finding
`AP6-01` alone.

## Independence, evidence boundary, and authorized scope

I used only:

1. `spec/research/boards/p09-rabin-1969/charter.md` in full;
2. the six objects in the charter's Frozen Round 6 table, each read in full;
3. `tmp/pdfs/p09-rabin-1969/rendered/page-01.jpg` through `page-36.jpg`; and
4. `tmp/pdfs/p09-rabin-1969/meyer1975-rendered/page-485.png` through
   `page-490.png`.

The hash-pinned Rabin and Meyer PDFs controlled identity, pagination, formulae,
symbols, and source wording.  The renders were used only as original-detail
reading aids.  I did not consult any Round 1--5 report or partial Round 4 work,
another Round 6 report, `ledger.md`, `transcript/chair.md`, another board, a
staging draft, the layout extraction as evidence, conversation history, memory,
or an external web source.  I did not contact another reviewer.

This was a manuscript-content review, not software work.  I ran no test,
automated checker, repository script, TeX command, interim build, handbook-PDF
inspection, or build.  The only computation was the charter-required native
SHA-256 identity check.  I edited no frozen object and wrote only this assigned
report.

## Native SHA-256 identity check

Before substantive review I ran the native PowerShell command
`Get-FileHash -Algorithm SHA256` independently on all six frozen objects.

| Frozen object | Charter SHA-256 | Recomputed SHA-256 | Result |
|---|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | MATCH |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | MATCH |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | MATCH |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | MATCH |
| `spec/research/p09-rabin-1969-source-note.md` | `29DAF36E123A2900620D49F018BD5F76BC4EE2FE0AAA7E3F85AAB50B23F37D7B` | `29DAF36E123A2900620D49F018BD5F76BC4EE2FE0AAA7E3F85AAB50B23F37D7B` | MATCH |
| `spec/research/p09-source-presentations-lot2-3.md` | `BB5D7220F75298C6DF3A1934D0DE36F25B9BD64AC5B2B71A141C2A41D3536236` | `BB5D7220F75298C6DF3A1934D0DE36F25B9BD64AC5B2B71A141C2A41D3536236` | MATCH |

There was no identity mismatch and therefore no freeze-integrity blocker.

## Printed pages visually inspected

- **Rabin:** all 36 physical render pages at original detail.  Physical p. 1
  is the custody-and-use cover.  Physical pp. 2--36 are every printed article
  page, pp. 1--35.  Thus I inspected the complete article, including all
  definitions, theorem statements, constructions, applications, qualifications,
  and references.
- **Meyer:** all six mandated article renders at original detail.  Physical PDF
  pp. 485--490 are printed article pp. 477--482.  In particular, I inspected
  the lower-bound theorem beginning on printed p. 478 and its enumerated
  two-successors-and-prefix item and attribution on printed p. 479.

No mandated source page was omitted or illegible at the detail used.

## Independent reconstruction and falsification checks

### Ordinary and dual semantics

From Rabin's printed pp. 5--7, ordinary acceptance is one global run followed
by all paths, with the infinitely recurring state set required to belong to
`F`: `exists r, for every path`.  The datum is
`F \subseteq \mathcal P(S)`, not a pair sequence.  From printed pp. 24--26,
Definition 3.6 reverses the prefix: every rooted run must have some path of one
of the types in `Omega`.  Because this is a universal implication over runs,
the dual condition is true when there is no rooted run.  The reader preserves
all three facts at `n-c-014.tex:974--1013` and `1143--1188`.

I separately checked the zero-pair case.  Lemma 3.6 enumerates
`P(S) - (F union {empty})`, so the list can be empty.  No path can have a type
from an empty list, hence the empty-list dual condition holds exactly when no
rooted run exists.  For `Omega^dagger=((S,S))`, every infinite path map into
the finite nonempty named state set has a nonempty recurrent-state set, which
cannot both meet and avoid `S`.  Thus its path-type language is empty and its
dual semantics is exactly the same.  The normalization at
`n-c-014.tex:1190--1213` is valid and does not invent a new acceptance
condition.

### Formula/run encodings and the path product

Definition 1.7's full-root bit-track map is a bijection, and the reader keeps
principal-formula recognition, Boolean closure, coordinate removal/addition,
and complement as distinct steps (`n-c-014.tex:1027--1065`; Rabin printed
pp. 7--9 and 30--31).  The worked formula at lines 1067--1077 is visibly
handbook-owned and has the asserted two-track witness.  The converse at lines
1079--1098 has the correct one-initial-state normalization and
`exists state tracks, for every path track` prefix.  The closed-sentence step
is nonemptiness, with no silently inserted basis theorem.

For Theorem 3.1, I recomputed the product from Rabin printed pp. 17--19.  The
state set `U x S`, initial set `{u0} x S`, transition
`((K(u,s),s1),(K(u,s),s2))`, and projected Muller family are well typed.  The
first coordinate is shared before a branch splits because the word automaton
is deterministic.  Its root/input indexing changes at most a finite initial
position and therefore cannot change an infinitely-often acceptance family;
the displayed reader construction at lines 1102--1139 is faithful.

### Complementation, finite trees, and emptiness

Rabin printed p. 19 defines the dependency mapping used below and makes
well-foundedness absence of an infinite descending dependency sequence.  Lemma
3.3 then characterizes it by disjoint ordinal strata with every successor
obligation in a strictly lower stratum.  The reader states this correctly at
`n-c-014.tex:1227--1233` and keeps the marked-tree, simultaneous-run, merging,
two-half-step, and positive-length induction architecture.  The cross-record
first-use defect concerning that same notion is finding `AP6-01` below.

Rabin printed p. 30 first distinguishes predecessor closure from the full-child
condition, then stipulates that subsequent "finite tree" means a frontiered
finite binary tree.  The reader's lines 1259--1283 correctly define the
terminal-node frontier, identify `frontiered` as a property of `E`, explain its
nonredundancy and later use, exclude the frontier from the valuation, type
`M:S x Sigma -> P((S x S) union {(f,f)})`, and keep `f` external to `S`.
Lines 1284--1294 also restore the distinct roles of Lemma 3.12, Corollary 3.13,
Lemma 3.14, and Corollary 3.15.

I recomputed Section 3.12's reduction: erase the alphabet to one letter;
complement the one-tree language; turn that complement back into a dual
membership question; and repeat the finite half-steps.  Definition 3.7's root
exception is necessary because only states strictly below the root are forced
into the restriction set.  On Rabin printed p. 34, the displayed nonempty
`H` branch omits the already-shorter case `H=empty`, and the printed nonempty
`U0` branch omits the no-run base.  Allowing every `H subseteq U_k` gives the
direct shorter question for `H=empty`; allowing `m=0`, `U0=empty` makes the
sole finite tree admit no run from `s0`.  Finite branching plus Koenig's
Infinity Lemma makes that finite obstruction equivalent to absence of an
infinite run.  The two repairs at `n-c-014.tex:1335--1400` are therefore
necessary, sufficient, and properly handbook-owned.  The weak monadic result
remains an external Doner/Thatcher--Wright base theorem and does not weaken the
full infinite-tree input problem.

### Complexity, source roles, rights, and completion scope

Rabin printed pp. 1 and 4 make the elementary-recursive claim.  Meyer printed
p. 478 states the growing-tower lower-bound theorem, and p. 479 lists "the
theory of two successors and prefix" with credit to Meyer and Stockmeyer.
That language is a sublanguage of Rabin's displayed binary theory.  The
snapshot therefore correctly withdraws only the elementary-recursive
worst-case claim while preserving decidability and effectiveness.  It does not
launder Meyer into Rabin's proof, McNaughton into a locally proved theorem,
Thomas's later basis route into Section 3.12, or Doner/Thatcher--Wright into
Rabin's own finite-tree proof.

The Rabin cover supports personal noncommercial research use, not an
open-content or republication license.  Public access to the Meyer volume
likewise is not described as a license.  The local PDFs and renders remain
research objects.  Finally, the source note expressly withholds terminal
admission, the compact record says Round 6 remains required, and the reader
limits its proof-reconstruction claim.  No text purports to complete all of
`N-c-014`, Part IX, a build, rendered-handbook review, human review, user
acceptance, another part, or the book.

## Finding

### AP6-01 — must-fix — well-founded obligation mapping is undefined at first use in two frozen records

**Exact frozen manuscript locations.**

1. `spec/research/p09-rabin-1969-source-note.md:122--124` first introduces
   "well-founded mappings" in the page map.  Its later substantive summary at
   `:417--425` repeatedly invokes a "well-foundedness requirement" and a
   "well-founded family" but still never gives the defining no-infinite-descent
   clause.
2. `spec/research/p09-source-presentations-lot2-3.md:668` first and only
   introduces "well-founded obligation mappings" in the compact Rabin record.
   It says that members lie in lower ordinal strata, but it does not define the
   underlying mapping or state the source's absence-of-infinite-descent
   condition.

The reader's correct definition at
`handbook/parts/p09/presentations/n-c-014.tex:1227--1233` does not cure these
separate frozen first uses.  The five-part rule is local: a later definition in
another object is not a definition at the first-use location.

**Controlling printed source.** Rabin printed p. 19, Definition 3.2 and Lemma
3.3 (physical render `page-20.jpg`).  The source fixes a nonempty set `H` and a
mapping `h |-> H_h subseteq H`; it calls the mapping well founded exactly when
there is no infinite sequence `h_1,h_2,...` satisfying
`h_{m+1} in H_{h_m}` for every `m`.  Lemma 3.3 then gives the equivalent
ordinal decomposition in which every member of `H_h` lies in a lower stratum.

**Defect.** R12 expressly requires definition by absence of infinite descent,
followed by the lower-stratum fact.  The detailed note supplies neither at its
first use and never supplies the definition later.  The compact record supplies
only an abbreviated lower-stratum consequence.  Neither location gives the
complete standing of the object as a dependency mapping on the marked
obligations, explains that the notion is needed to exclude endless deferral
chains rather than to rename the simultaneous finite-state run condition, or
ties the exact definition locally to its use in Lemmas 3.3--3.4 and 3.11.
Consequently the name fails R12 and R26's necessity, exact definition,
standing, nonredundancy, and use-at-first-location rule.  This is not a merely
stylistic preference: without the defining chain quantifier, "lower ordinal
strata" can be read as an unexplained proof device rather than the equivalent
certificate for the precise relation Rabin defined.

**Minimum sufficient repair.** In the detailed note, either remove the
technical name from the early page map and make its first substantive
occurrence an exact definition, or put the exact definition at that early
location.  At that first defining location state:

- the necessity: endless deferral chains among activated obligations must be
  excluded;
- the definition and standing: for nonempty `H`, this is a mapping
  `h |-> H_h subseteq H`, well founded iff no infinite
  `h_{m+1} in H_{h_m}` chain exists;
- the nonredundancy: it constrains the obligation-dependency relation and is
  not the ordinary path acceptance condition or the simultaneous-run merge;
  and
- the use: Lemma 3.3 supplies the lower-stratum characterization, Lemma 3.4
  makes the marked family automaton definable, and Lemma 3.11 uses it in the
  arbitrary-sequence half-step.

Make the same exact local addition, or avoid the technical name entirely, at
the compact record's line 668.  Preserve the correct statement that every
member of `H_h` belongs to a strictly lower ordinal stratum and the present
separation between transfinite reasoning and the finite constructions.  No
mathematical change to the reader is required for this finding.

## R01--R29 audit ledger

| Invariant | Result | Adversarial check |
|---|---|---|
| R01 | PASS | Reader lines 914--917 retain Rabin's `Lambda`; printed pp. 3--5 show that symbol. |
| R02 | PASS | Reader lines 941--963 give every `0<n<=omega`, `T_n=n*`, successors, both orders, finite-`n` definability, and the `T_omega` exception; printed pp. 4--5 and 10--11 agree. |
| R03 | PASS | Reader lines 965--1014 preserve arbitrary roots, distinct table/automaton tuples, `F subseteq P(S)`, and `exists run / every path`; printed pp. 5--7 agree. |
| R04 | PASS | Reader lines 1143--1188 assign `Omega` only to dual `every run / some path` semantics and make no-run vacuity explicit; printed pp. 24--26 agree. |
| R05 | PASS | Reader lines 1016--1023 state Theorems 1.3--1.6 and describe coordinate removal and unconstrained addition directly, with no undefined operation name; printed pp. 6--7 agree. |
| R06 | PASS | Reader lines 1027--1065 type the full-root bijection and separate principal formulae, finite lift, Boolean closure, projection, and complement; printed pp. 7--9 and 30--31 agree. |
| R07 | PASS | Reader lines 1067--1077 label the two-track formula as handbook-owned and do not attribute a transition table to Rabin. |
| R08 | PASS | Reader lines 1079--1098 preserve one-start normalization, `exists B-bar / every C`, and direct sentence nonemptiness; printed pp. 9--10 agree. |
| R09 | PASS | Reader lines 1102--1139 have the exact deterministic word tuple, product, update, initial set, and projected Muller family; the recurrence indexing is harmless only because acceptance is infinitely-often, as checked above; printed pp. 17--19 agree. |
| R10 | PASS | Reader lines 1143--1188 preserve Definition 3.5's two type conditions, Definition 3.6's reversal, and the complement role; printed pp. 24--26 agree. |
| R11 | PASS | Reader lines 1218--1225 retain marking, simultaneous activated runs, same-state merging, and the Theorem 3.1 path check; printed pp. 19--24 agree. |
| R12 | **FAIL: AP6-01** | Reader lines 1227--1233 and 1296--1303 are correct, but the detailed note and compact record use the technical name without the exact printed-p. 19 no-infinite-descent definition. |
| R13 | PASS | Reader lines 1235--1256 preserve same-length Lemmas 3.7--3.8, shorter `Omega_{k-1}`, the arbitrary and last-lower-empty cases, and induction only after the zero-length normalization; printed pp. 26--32 agree. |
| R14 | PASS | Reader lines 1259--1283 and compact line 670 give the exact frontier/full-child distinction, standing, nonredundancy, later use, valuation domain, transition codomain, and external `f`; printed p. 30 agrees. |
| R15 | PASS | Reader lines 1284--1294 and compact line 670 assign the lift, principal-formula application, compactness, and return to frontiered machinery to the correct four numbered results; printed pp. 30--32 agree. |
| R16 | PASS | Reader lines 1307--1333 give alphabet erasure, complement, dual conversion, and membership, not a basis theorem; printed pp. 32--34 agree. |
| R17 | PASS | Reader lines 1335--1351 state each current table and pair sequence and preserve Definition 3.7's formal-state/root boundary; printed pp. 32--34 agree. |
| R18 | PASS | Reader lines 1353--1371 include every `H subseteq U_k`, distinguish empty/direct-shorter from nonempty/restricted branches, and justify finite-stratum termination; printed pp. 33--34 plus the explicit handbook repair support it. |
| R19 | PASS | Reader lines 1373--1400 allow `m=0`, `U0=empty`, and `E0` with no run, invoke Koenig compactness, preserve the printed nonempty branch, and keep the weak-theory theorem external; printed p. 34 supports the diagnosed omission. |
| R20 | PASS | Reader lines 952--960 and all records distinguish Rabin's printed pp. 1/4 historical claim from Meyer's printed pp. 478--479 lower bound and exact Meyer--Stockmeyer attribution. |
| R21 | PASS | Reader lines 1404--1421 represent the linear-order, unary-function, Cantor-space, Boolean-algebra, and game applications at the printed pp. 10--17 class strength. |
| R22 | PASS | Reader lines 1423--1437 state reconstruction limits and keep Thomas's basis route and McNaughton's word result externally attributed. |
| R23 | PASS | Numbering, notation, locators, strength, and attributions checked against all printed pages; no separate defect found. |
| R24 | PASS, subject to AP6-01's terminology completeness | Reader, note, compact record, and bibliography are factually consistent on identities, Meyer, scan URL, Thatcher--Wright, and pending status.  AP6-01 is an omitted local definition, not a contradictory source/result assignment. |
| R25 | PASS | Detailed note lines 83--94 accurately limit both access routes; the cover and Meyer pages support no license inflation. |
| R26 | **FAIL: AP6-01** | The well-founded-mapping name is not five-part compliant at its first uses in the detailed note and compact record.  Other load-bearing new names, especially `Omega^dagger` and `frontiered`, are locally defined and used. |
| R27 | PASS | No finite/infinite, weak/full, ordinary/dual, existence/effectivity, source/later-route, or decidability/complexity conflation survived the independent checks. |
| R28 | PASS | Detailed note lines 37--38, reader lines 1423--1437, and compact line 672 withhold admission and all wider publication claims. |
| R29 | PASS | Reader lines 1190--1213 explicitly allow length zero and prove exact equivalence with `((S,S))`; printed Lemma 3.6 on pp. 25--26 supplies the possibly empty enumeration. |

## Limitations and exact effect of the verdict

- This verdict concerns only the frozen `N-c-014.d` manuscript-content
  snapshot.  It is not a verdict on all `N-c-014`, Part IX, another part, the
  handbook as a whole, typesetting, a generated page, a build, human review, or
  user acceptance.
- The native hashes establish identity, not scholarly correctness; correctness
  was checked separately against the printed pages.
- I inspected the complete six-page Meyer article mandated by the charter, not
  every other article in the complete ICM volume.
- I made no live access, licensing, or bibliographic investigation beyond the
  frozen records and the printed custody/rights language.  The rights conclusion
  is therefore the appropriately narrow negative one: no open-content or
  republication license is established by this evidence.
- The rejection is driven by one local terminology/completeness defect.  I
  found no blocker and no second must-fix after testing the mathematics,
  indexing, quantifiers, vacuity, frontier type, base cases, source roles,
  complexity correction, rights language, and completion scope.

VERDICT: REJECT — AP6-01
