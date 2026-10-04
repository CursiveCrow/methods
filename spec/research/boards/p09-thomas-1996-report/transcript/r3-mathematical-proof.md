# Round 3 mathematical and proof-correctness review

## Independence, objects, and source pages

I performed this review independently on the frozen Round 3 snapshot. I read
the actual frozen LaTeX passages in full: `n-c-013.tex` lines 800--986 and
`n-c-014.tex` lines 888--927 and 1451--1596. I also read the charter, the
seat-relevant passages of the shared Part IX file and bibliography, the complete
Thomas source note, and the Thomas entries and consolidated status entry in the
compact record. I did not read the ledger, chair transcript, any earlier-round
report, another Round 3 report, another board or transcript, memory, staging
material, or web results, and I did not contact another reviewer.

I consulted the controlling hash-pinned PDF itself at its unnumbered title and
abstract pages, contents page `i`, and printed pp. 1, 8--12, 28--42, 43--61, and
72. Thus the mandatory Round 3 pages 28, 31, and 33--35, as well as the pages
needed to recheck every earlier repair, were read from the controlling PDF. No
PNG or other derived page render was opened or used. No test, test harness,
automated checker, repository script, TeX command, build, manuscript-PDF
inspection, or rendered-handbook inspection was run or used as evidence.

## Independently recomputed identities

| Frozen object | Recomputed SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | matches; 478,293 bytes |
| `handbook/parts/p09/presentations/n-c-013.tex` | `23E73DA416CE583ADF084E1D16E4A5846AC9659E4ED0E937A1CB00FA0738AFED` | matches |
| `handbook/parts/p09/presentations/n-c-014.tex` | `F9576BB10063037CDFD9018E6DC7DFB553651590FB74FC77D2D33EEBBF4D5915` | matches |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` | matches |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | matches |
| `spec/research/p09-thomas-1996-report-source-note.md` | `F169CB0936EAA8CB650102A974FEE01F05C3E9D58774F7A198E2CEE35E2A7150` | matches |
| `spec/research/p09-source-presentations-lot2-3.md` | `C45908A389BB22FBB584672F9F78F1C0E45E7DDF274BC37039AEA9BC81ED281F` | matches |

## Mathematical reconstruction and adversarial checks

### Finite words

The tuple, transition relation, length-`n+1` run, initial condition, last-state
condition, and effective two-way theorem at `n-c-014.tex` lines 888--901 agree
with printed p. 8. The automaton-to-formula construction at lines 903--907
correctly tracks the states before each input letter, treats the final letter by
an outgoing transition to `F`, and adds the nonempty-domain guard exactly when
the automaton rejects the empty word. Thus both cases `q_0 in F` and `q_0 notin
F` at input length zero are correct. The singleton-set atomic cases, complement,
union, and projection at lines 908--913 agree with printed pp. 8--9. The finite
set range for `WS1S`, input-free successful-run test, reversed binary coding,
and finite carry set at lines 914--918 do not exceed printed pp. 10--12.

### Infinite words and determinization

The nondeterministic tuple, typed run, and `In(r)` at `n-c-013.tex` lines
800--821 agree with printed p. 28. Lines 822--832 restore the source's total
function `delta:Q x Sigma -> Q` and unique-run equation. Consequently every
word has exactly one deterministic run, including words for which a merely
functional partial relation would have no run. Complementing a deterministic
Muller family at lines 874--878 therefore complements the language, rather
than leaving missing-run words rejected on both sides.

The four conditions at lines 833--853 have the correct types and quantifiers.
In particular, Thomas's Streett ordering says that recurring `F_i` implies
recurring `E_i`. Empty Büchi or Rabin recurring components reject as they
should. The nondeterministic comparison retains only Proposition 5.3's
recognized-language equivalence. Lines 860--872 give a finite union of regular
`U_j V_j^omega` factors and require unbounded total factor length; infinitely
many empty factors therefore cannot denote a finite word.

For the determinization state, lines 883--896 supply the necessity, exact tuple,
standing, nonredundancy, and later use of the source term. In particular,
`nu:N(T) -> {1,...,2n}` is typed and injective and is distinct from both the
state-subset label map and the current mark set. The root begins as `{q_0}` with
name `1` and no mark. The text correctly identifies that choice of initial name
as a handbook normalization.

The update at lines 897--933 has the required lifetime and order: predecessor
marks are cleared while names remain; youngest accepting children are created;
every label, including each new one, advances; horizontal duplicates and empty
nodes are removed; and current collapses alone mark their parents. Generated
ordinary states therefore have nonempty node labels. If the advanced root is
empty, lines 915--925 instead enter the no-node, no-name, unmarked absorbing
state. No original run extends that prefix, so no continuation can recover an
accepting run. The special state is consequently language-correct and totalizes
the deterministic successor without pretending that an empty root is an
ordinary rooted tree.

Surviving nodes keep their predecessor names. At most one child is created for
each of at most `n` predecessor nodes, and all newly created nodes receive
pairwise distinct names outside the entire predecessor name set. Hence at most
`n` old names are withheld while at most `n` fresh names are simultaneously
needed; `1,...,2n` is sufficient even before cleanup. After empty-node removal,
sibling disjointness and proper child-union containment let each live node be
charged to a distinct original state, so at most `n` nodes remain. This also
handles deletion and later reuse without identifying a deleted lineage with a
same-update new lineage.

The sets at lines 936--943 are defined on every ordinary determinization state:
`E_k` means that `k` is outside `im(nu)`, and `F_k` means that the currently
marked live node has name `k`. The absorbing empty state is expressly in every
`E_k` and no `F_k`. Thus the Rabin condition is exactly eventual name presence
plus infinitely many distinct current collapse events, and the empty state
rejects. The `a b^omega` example at lines 948--952 correctly has one collapse
only; clearing the old mark prevents false acceptance. The construction has
exactly `2n` displayed pairs and `2^{O(n log n)}` states, while the lower-bound
claim at lines 953--958 retains the `2^{O(n)}`-state, `O(n)`-pair qualifier from
printed pp. 35--37.

The effective Büchi/MSO directions at lines 960--964 are sound. The corrected
input-free criterion at lines 965--969 requires a reachable nonempty cycle that
meets `F`; a reachable nonaccepting cycle is not enough. The text labels this as
a handbook repair of the defect on printed p. 38. The eventual-absence and
recurring-presence clauses at lines 969--979 have the source quantifier order,
and all quantifiers internal to their finite-prefix tests are bounded below the
current endpoint. Weak monadic quantification is explicitly finite-set-valued.

### Infinite trees, games, and `S2S`

The tree tuple, global run, root/child equations, and `exists run, for every
path` Muller condition at `n-c-014.tex` lines 1451--1475 agree with printed pp.
43--45. The two examples support exactly the stated Büchi/Muller separation.
The strict chain and pair condition at lines 1478--1489 are correct. A state
outside every displayed chain set contributes to no pair; in particular, a path
eventually constant outside all `F_i` rejects. The order-vector with hit at lines
1490--1498 is a permutation plus the previous position of the currently visited
state, is finite automaton-state memory rather than an input or run, and is used
by Remark 6.6 to recover the recurrent-state set.

The completion at lines 1500--1529 handles every absent state-letter transition
by two fresh rejecting children and loops the fresh state on all letters. It
preserves strict inclusions because the chain sets are unchanged as subsets of
the enlarged state set. If an added transition occurs at any node, either child
extends to a path permanently labelled by the fresh state, which lies in no
`F_i`; that run is unsuccessful. Conversely every original successful run
remains. Thus the language is unchanged while every Automaton position has a
move and every Pathfinder position has its two branch moves. This covers an
original automaton with no available transition and an empty recognized tree
language: completion creates plays but creates no accepting path or successful
run.

Lines 1531--1555 propagate that completion into the game and complement proof.
Automaton chooses a transition before Pathfinder chooses a branch. A memoryless
strategy depends on the current game position. Pathfinder's local instruction
has finite type `Sigma x Delta -> {0,1}`; an instruction-labelled tree records
the node-dependent strategy. Universal checking of all consistent transition
sequences is obtained through word-automaton closure, the resulting sequential
Muller automaton is deterministic, all paths are then checked by a deterministic
Muller tree automaton, and only the local instruction labels are guessed
nondeterministically. The construction depends on the original automaton, not
the particular input tree.

The completion gives the nonempty finite outdegree required by Theorem 6.13.
Lines 1555--1562 correctly retain its forced-finite-visit/attractor and
complementary-subgame induction, including the zero-nonempty-entry base case,
and separate finite-game effectivity in Theorem 6.16. Lines 1564--1574 give the
typed finite generator with output, input guessing, completed finite game,
memoryless winning strategy, effective emptiness test, and regular-member
conclusion. If the language is empty there is no winning initial position and no
regular-member claim; if it is nonempty the selected transition at each finite
Automaton position yields the generator.

Finally, lines 1576--1589 correctly separate the atomic, disjunction,
existential-projection, and completed-complement steps in the forward MSO
translation. The converse uses existential state tracks for one global run and
a universal path set for its acceptance. An input-free sentence is decided by
the same completed emptiness route. Lines 1591--1596 preserve the later Thomas
route and do not project it onto Rabin's historical proof.

## Mandatory invariant dispositions

| Invariant | Disposition |
|---|---|
| **H01** | Pass. The title/identity, May 1996 date, Bericht 9607, institution, 478,293-byte length, 75-page extent, and controlling hash agree among the PDF, `handbook.bib` lines 2346--2356, source note lines 13--41, and compact record line 608. It is described only as a report precursor. |
| **H02** | Pass. The report abstract's prospective *Handbook of Formal Language Theory* and the final bibliography entry's *Handbook of Formal Languages* remain distinct (`p09-thomas-1996-report-source-note.md` lines 73--82; `handbook.bib` lines 2358--2366). |
| **H03** | Pass. The title/abstract/contents/body/end page map and the Section 3.1, 5.1--5.3, and 6.1--6.3 printed ranges agree with the PDF (`p09-thomas-1996-report-source-note.md` lines 36--61). No final-chapter locator is inferred. |
| **H04** | Pass. Public course access is not promoted to a licence; the PDF and inert image boundary are exact (`p09-thomas-1996-report-source-note.md` lines 63--71 and 316--322). |
| **H05** | Pass. `n-c-014.tex` lines 888--901; printed p. 8. |
| **H06** | Pass. `n-c-014.tex` lines 903--913; printed pp. 8--9, including the empty-word guard. |
| **H07** | Pass. `n-c-014.tex` lines 914--918; printed pp. 10--12. |
| **H08** | Pass. `n-c-013.tex` lines 800--832; printed p. 28, with the deterministic total-function clause also controlling printed p. 31. |
| **H09** | Pass. `n-c-013.tex` lines 833--858; printed pp. 28--29. The Streett implication has the source direction. |
| **H10** | Pass. `n-c-013.tex` lines 853--881; printed pp. 29--31. The finite union, deterministic-Büchi failure, and total deterministic-Muller complement boundary retain their exact strengths. |
| **H11** | Pass. `n-c-013.tex` lines 883--905; printed pp. 31 and 33--34. The first occurrence supplies the five required terminology components and distinguishes the determinization state from input trees and runs. |
| **H12** | Pass. `n-c-013.tex` lines 897--933; printed pp. 33--34. Update order, current-event marks, empty successor, persistent names, same-update distinctness, fresh-name rule, live-node bound, and reservoir are coherent. |
| **H13** | Pass. `n-c-013.tex` lines 934--958; printed pp. 34--37. Persistent-name/current-mark acceptance, both proof directions, `E_k,F_k`, exact displayed pair count, asymptotic state bound, and lower-bound qualifier are correct. |
| **H14** | Pass. `n-c-013.tex` lines 960--969; printed p. 38. The two-way theorem remains effective and the accepting-cycle repair is visible and handbook-owned. |
| **H15** | Pass. `n-c-013.tex` lines 969--980; printed pp. 38--39. The outer quantifier order, bounded inner tests, and finite weak-set range are correct. |
| **H16** | Pass. `n-c-014.tex` lines 1451--1476; printed pp. 43--45. |
| **H17** | Pass. `n-c-014.tex` lines 1478--1498; printed pp. 45--47. Chain acceptance and the order-vector-with-hit standing and use are exact. |
| **H18** | Pass. `n-c-014.tex` lines 1534--1542; printed pp. 47--49. Move order, acceptance equivalence, and current-position-only strategy definition precede use. |
| **H19** | Pass. `n-c-014.tex` lines 1542--1555; printed pp. 49--50. The local-instruction, universal transition/path checks, nondeterministic guess, and input-tree independence are all preserved. |
| **H20** | Pass. `n-c-014.tex` lines 1555--1574; printed pp. 50--57. Determinacy, finite effectivity, regular generation, emptiness, and basis claims retain separate types and roles. |
| **H21** | Pass. `n-c-014.tex` lines 1576--1596; printed pp. 57--59. The translations and input-free decision route are correct, while `logic-in-computer-science.tex` lines 843--846 and the closing boundary preserve Rabin's historical standing. |
| **H22** | Pass. `logic-in-computer-science.tex` lines 25--42, 723--762, 814--828, 843--846, and 2348--2356; `handbook.bib` lines 2346--2367; source note lines 324--352; compact record lines 606--616, 674--682, and 902--911. Terminology, ownership, locators, history, and narrow open status agree. |

## Repair-invariant dispositions

| Invariant | Disposition |
|---|---|
| **R2-01** | Pass. `n-c-013.tex` lines 860--872 gives regular finite-word factors and unbounded-length infinite concatenation at report-precursor standing; printed p. 30. |
| **R2-02** | Pass. `n-c-013.tex` lines 915--925 and 942--947 supplies the no-node absorbing successor, rejection proof, `E_k/F_k` treatment, and unchanged bounds; source gap checked at printed pp. 28 and 34. |
| **R2-03** | Pass. `n-c-013.tex` lines 897--905 and 944--953 makes marks current-update events and uses infinitely many distinct collapses; `a b^omega` rejects; source gap checked at printed pp. 34--35. |
| **R2-04** | Pass. `n-c-014.tex` lines 1500--1533, 1553--1569, and 1580--1585 gives and propagates the exact rejecting completion; source gap checked at printed pp. 44, 47--51, 55--58. |
| **R3-01** | Pass. `n-c-013.tex` lines 809--832 and 874--878 states the total transition function and unique run before deterministic Muller complementation; printed pp. 28 and 31. |
| **R3-02** | Pass. `n-c-013.tex` lines 883--947 types the injective map, initial/fresh/persistent naming, same-update distinctness, empty name set, reservoir proof, and total `E_k,F_k` interpretation, while distinguishing source content from handbook normalization and definedness; printed pp. 33--35. |
| **R3-03** | Pass. Source note lines 331--349 and compact record lines 606--616, 674--682, and 902--911 agree that Rounds 1 and 2 rejected, Round 3 is open, the final chapter remains unreconciled, and no broader unit is admitted. Source note lines 63--71 correctly makes derived images evidentially inert. |

## Findings and seat rationale

No blocker, must-fix, should-fix, consider, discard, or unresolved-user finding
survived reconstruction. The repaired snapshot is typed on all acceptance and
transition boundaries, closes both kinds of missing-run case without changing
the recognized languages, makes named-node lineage and Rabin-pair definedness
literal, preserves every earlier repair, and states only report-precursor and
narrow presentation strength.

VERDICT: ACCEPT
