# Safra, *On the Complexity of omega-Automata*: source and version note

**Disposition:** THE REGISTERED NINE-PAGE FOCS 1988 BODY REMAINS
UNACQUIRED. A COMPLETE TWENTY-PAGE AUTHOR-HOSTED EXPANDED MANUSCRIPT WAS
ACQUIRED AND READ FROM ITS ACTUAL POSTSCRIPT FILE. ITS TECHNICAL CONTENT MAY
BE USED ONLY AT EXPLICIT EXPANDED-MANUSCRIPT STRENGTH.

This note controls Part IX presentation `N-c-013.d`. It keeps the 1988
proceedings paper and Safra's later expanded manuscript separate. The expanded
body is not called the proceedings paper, a proceedings facsimile, or a
published journal article.

## Registered work and DOI identity

The registered work is Shmuel Safra, “On the Complexity of omega-Automata,” in
the *29th Annual Symposium on Foundations of Computer Science*, White Plains,
New York, 24--26 October 1988, pp. 319--327, IEEE, print ISBN
`0-8186-0877-3`, DOI
[10.1109/SFCS.1988.21948](https://doi.org/10.1109/SFCS.1988.21948).
The [Tel Aviv University record](https://cris.tau.ac.il/en/publications/on-the-complexity-of-%CF%89-automata/)
reports nine pages and identifies Safra's then-affiliation as the Weizmann
Institute of Science.

IEEE/Crossref, TAU, and the raw DBLP record agree on DOI suffix `21948`.
Crossref assigns the next suffix, `21949`, to E. Allen Emerson and Charanjit
S. Jutla, “The Complexity of Tree Automata and Logics of Programs,” pp.
328--337. An earlier web-renderer click appeared to associate Safra's DBLP row
with `21949`; the raw XML resolves that event as a link-selection artifact, not
conflicting bibliographic evidence.

## Newly acquired author-hosted expansion

Safra's Tel Aviv University directory exposes the actual file
[DBA.ps](https://www.cs.tau.ac.il/~safra/PapersAndTalks/DBA.ps). The directory
lists it as 242 KiB and last modified 12 April 1999. The acquired bytes have the
following PostScript header:

```text
%!PS-Adobe-2.0
%%Creator: dvips 5.512 Copyright 1986, 1993 Radical Eye Software
%%Title: jcss.dvi
%%CreationDate: Tue Mar 21 15:47:45 1995
%%Pages: 20
%%PageOrder: Ascend
%DVIPSCommandLine: dvips jcss
%DVIPSSource: TeX output 1995.03.21:1547
```

The title page is “On the Complexity of omega-Automata,” by Shmuel Safra,
Department of Applied Mathematics, Weizmann Institute of Science. Its footnote
says that a preliminary version appeared as `[Saf88]`. The manuscript's own
reference `[Saf88]` identifies the FOCS paper, pp. 319--327, and adds that an
extended version was to appear in the *Journal of Computer and System Science*.
The acquired source is therefore author-authenticated as an expansion of the
1988 paper. Its header and length establish that it is not the nine-page
proceedings object.

No publisher record for a later journal publication under this title was
established. “To appear” is retained as the manuscript's historical statement,
not upgraded to a publication claim. The handbook cites the source separately
as an author-hosted expanded manuscript whose PostScript was generated on
21 March 1995.

The actual `.ps` file was read page by page. The title page, Sections 1--5,
Theorem 1, Lemmas 2, 3, and 5, Corollaries 4, 6, and 7, Appendix A's sketch,
and the references were read from that source object. No manuscript TeX build, handbook
PDF, PNG page set, or derivative source PDF was used as evidence. The source's
drawn automata motivate the construction, but no edge-by-edge transcription of
those drawings is claimed in the reader text.

## Access boundary for the registered proceedings version

The nine-page FOCS body was still not lawfully retrievable in this environment
on 24 August 2026 (America/Los_Angeles).

| Route | Exact result |
|---|---|
| IEEE Xplore record | The live [document page](https://ieeexplore.ieee.org/document/21948) exposed title, author, abstract, proceedings metadata, DOI, and a PDF control. The PDF control required institutional or member sign-in. No access control was bypassed. |
| IEEE first-page preview | The advertised first-page image did not load through the ordinary asset route. No proceedings page image was obtained. |
| Crossref version-of-record link | Crossref identifies the correct article number and publisher PDF path. The unauthenticated request returned an IEEE challenge response, not a PDF. |
| TAU CRIS | The institutional record supplies the abstract and bibliographic metadata but attaches no proceedings file. |
| OpenAlex | Work `W2031592188` reports the DOI landing page only, closed access, no repository full text, and no PDF location. |
| Semantic Scholar | Paper `961c7f4b10a535825a5d786c5896bf4a657623f1` reports closed status and no open PDF URL. |
| DBLP and Unpaywall route | The raw DBLP record identifies the correct DOI; its unpaywalled-version route supplied no independent body. |

This is an access failure, not evidence that the IEEE body does not exist. A
lawful library copy, author copy of the proceedings version, or user-supplied
scan could close the literal proceedings-body gap.

## Expanded-manuscript mathematical extraction

### Automata and acceptance conventions

The expanded manuscript defines an omega-automaton as
`A = <Sigma,Q,q0,delta,C>`, with finite `Q`, initial state `q0`, transition
relation written as the set-valued map
`delta: Q x Sigma -> P(Q)`, and an acceptance condition `C`. A run on an
infinite word starts at `q0` and follows `delta`. Its infinity set contains the
states occurring infinitely often. The manuscript separately tabulates Büchi,
Muller, Rabin, and Streett syntax and semantics.

Safra calls an automaton deterministic exactly when `|delta(q,a)|=1` for every
state `q` and letter `a`, a total as well as single-valued condition. The input
Büchi automaton may nevertheless have an empty successor set; the total
condition governs the constructed target. A Muller condition is a family
`M` of subsets of `Q`, and a run is accepted exactly when its infinity set
belongs to `M`.

For Rabin acceptance, the source writes pairs `(L_i,U_i)` and accepts when some
`L_i` state recurs infinitely often while every `U_i` state occurs only
finitely often. Thus `L_i` is the good/recurring component and `U_i` the
bad/eventually absent component. Streett acceptance uses the universal dual.
In the manuscript's compact class notation, `NB(n)` denotes `n`-state
nondeterministic Büchi automata, while `DR(m,h)` denotes deterministic Rabin
automata with `m` states and `h` Rabin pairs.

### Ordered vocabulary trees and exact state standing

For an input Büchi automaton with `n = |Q|`, the source fixes a vocabulary `V`
of size `n`. An ordered `V`-tree is the structure `T = <N,r,p,S>`:

- `N` is a subset of `V` and supplies the node identities;
- `r` is its distinguished root;
- `p` maps every non-root node to its parent; and
- `S` linearly orders siblings. The source first defines ancestor strictly and
  then defines left-to-right through ancestors which are siblings; read
  literally, that relation fails to compare siblings themselves. The handbook
  owns the correction: for two non-ancestral nodes, follow their root-to-node
  paths through their last common node and compare the first distinct children
  by their sibling order. For the handbook-owned name allocation, this
  corrected relation is extended to a total traversal which puts an ancestor
  before every proper descendant and otherwise uses that left-to-right order.

A determinization state is `(T,l,c)`, where `l:N -> P(Q)` labels nodes by
original-state subsets and `c:V -> {white,green,red}` colors every vocabulary
name. It satisfies two invariants:

1. the union of a node's children labels is a proper subset of the node's
   label; and
2. labels of non-ancestral nodes are disjoint.

The same strict-ancestor convention makes the printed specificity clause
require, read literally, membership and nonmembership at the node itself.
Its following parenthetical supplies the intended inclusive-path reading. The
handbook owns the correction: the inclusive root-to-`d` path is `d` together
with all its strict ancestors, and an original state `q` is specific to `d`
exactly when `q` belongs to `d` and belongs to no label off that path. Label
containment puts it in every ancestor label, and branch disjointness makes `d`
unique. Specificity is an eliminable description of label membership, not a
fourth component. It is later used to bound the number of live nodes by `n`.

The initial state is a one-node tree labelled `{q0}`, with every element of `V`
white. The source does not designate which vocabulary element names that root.
The handbook fixes one root name once and for all; this is a representative
choice, not a new source object.

### Six-stage letter update

Write `delta_hat(R,a) = union_{q in R} delta(q,a)`. For a letter `a`, the
source performs these operations in order, temporarily using a disjoint
`n`-element vocabulary `V'` for new nodes:

1. replace every label `R` by `delta_hat(R,a)`;
2. for every node whose resulting label meets the Büchi set `F`, add a youngest
   child from `V'` labelled `R intersect F`;
3. if a state occurs on more than one non-ancestral path, delete it from every
   path except the leftmost one;
4. delete all empty-labelled nodes;
5. whenever an old node's label equals the union of its children labels,
   delete its descendants and color it green; color other surviving old nodes
   white and absent old names red; and
6. rename every surviving temporary node by an unused element of `V`.

The source says to choose “some” unused names. Because the target is asserted
to be deterministic, the handbook fixes one ordering of `V`, enumerates the
surviving temporary nodes in the total traversal just defined, and assigns the
least available names. This is an eliminable choice of representative. It adds
no acceptance data.

After the pruning and collapse stages, every surviving node has at least one
specific original state. Hence at most `n` nodes survive, and the `n` names in
`V` suffice. A new name is red in the state in which it is allocated; a
surviving name persists through later states, is white on ordinary updates,
and is green on a collapse update.

### Printed empty-successor omission and bounded repair

The source permits `delta(q,a)` to be empty. If the root's advanced label is
empty, stage 4 deletes the root although the printed target states are rooted
trees. No empty-tree or absorbing case is stated. The handbook supplies one
handbook-owned rejecting sink for exactly this case. It is an automaton state,
not a tree node; it loops on every input, is in every red/bad component, and in
no green/good component. This makes the target transition total without
changing the recognized language or the asymptotic bound.

### Rabin pairs and proof

For every `v in V`, the green component contains states in which `c(v)` is
green and the red component contains states in which `c(v)` is red. The sink
is included in every red component. A run is accepted when one name is red
only finitely often and green infinitely often. The source therefore obtains
exactly `n` Rabin pairs.

The soundness proof chooses a name which is eventually never red and becomes
green at positions `i_1 < i_2 < ...`. If `S_j` is its label at `i_j`, the
creation and collapse rules ensure that every state in `S_{j+1}` has a
predecessor in `S_j` joined by a finite input-compatible run segment which
visits `F`. A finitely branching predecessor tree and König's lemma give one
infinite branch; concatenating its segments yields one Büchi-accepting input
run.

For completeness, an accepting original run is always represented in the
root. If the root is green infinitely often, it witnesses the Rabin condition.
Otherwise, after its last green event the accepting run enters a child on its
next visit to `F`. Horizontal deletion can move responsibility only finitely
often to older siblings, so the run eventually remains under one child. If
that child is not green infinitely often, the argument descends. Proper label
containment bounds tree depth, so some persistent node must be green infinitely
often.

### Bounds, lower-bound qualifier, and applications

The source bounds ordered tree shapes over `V` by
`2^(n log n + O(n))`. It prints an `n^n` label count by assigning every
original state to its specific node, but this silently omits an original state
which is absent from all live labels. The handbook makes the encoding total by
fixing one symbol `star` outside `V` and using a function from `Q` to
`N union {star}`: a present state maps to its unique specific node and an
absent state maps to `star`. The symbol is only an encoding value, not a node or
automaton component. This gives at most
`(n+1)^n = 2^(O(n log n))` assignments; colors contribute `3^n`. The repair is
handbook-owned and preserves Theorem 1's asymptotic statement: every `n`-state
nondeterministic Büchi automaton has an equivalent deterministic Rabin
automaton with `2^(O(n log n))` states and exactly `n` Rabin pairs.

**Direct manuscript update, 2026-09-06.** The live N13 counting paragraph now
states the total encoding count directly; the deficient historical `n^n`
reading is retained here only. The held PostScript's printed page 12,
Complexity paragraph (file lines 2816–2841), was read back for this edit.
The manuscript proves that the occurrences of each present original state
form one inclusive root-to-node path, so its specific node determines all
its label memberships. Adding the absent value gives an injective encoding
into the `(n+1)^n` functions. It also supplies the elementary ordered-tree
bound `8^n n!`: choose a node subset, a depth-first balanced-parenthesis
shape, and a bijective naming. Colors and the rejecting sink give the
explicit total `1 + 8^n n! (n+1)^n 3^n`. The asymptotic bound and exactly
`n` Rabin pairs are unchanged. The tree-count derivation and total encoding
are supplied mathematical details, not a claim that the source prints
this exact formula.

The following paragraph invokes a modification of Michel's argument for an
`n!` lower bound. The precise source qualification is optimal up to a constant
in the exponent; the abstract's unqualified word “optimal” must be read through
that theorem-level statement. Lemma 2 separately says that determinization to
Muller acceptance can require a doubly exponential acceptance-family size. Its
proof is explicitly only a sketch in Appendix A.

The principal printed applications are:

- Lemma 3 converts a deterministic Streett automaton with `n` states and `h`
  pairs into an equivalent deterministic Rabin automaton with
  `n * 2^(h log h)` states and `h+1` pairs;
- Corollary 4 gives a complementary deterministic Rabin automaton with
  `2^(O(n log n))` states and `n+1` pairs;
- Corollary 6 gives a complementary nondeterministic Büchi automaton with
  `2^(O(n log n))` states;
- immediately before Corollary 7, the source calls a Büchi automaton
  deterministic in the limit exactly when every accepting run makes only
  finitely many nondeterministic choices, meaning positions with more than one
  available successor. This accepting-run property is weaker than full
  determinism because rejecting runs need not eventually stop making such
  choices. Corollary 7 gives an equivalent Büchi automaton with that property
  and `O(3^n)` states; and
- the modal-logic discussion records the resulting deterministic exponential
  upper bounds for Delta-PDL and the mu-calculus and a deterministic doubly
  exponential upper bound for CTL-star.

These application statements belong to the expanded manuscript. They are not
retroactively assigned to the unread FOCS pages.

## Material difference from Thomas's later presentation

The expanded manuscript uses node identities drawn from an `n`-element
vocabulary and prints exactly `n` Rabin pairs. Thomas's May 1996 report
presentation uses an injective live-node name map into `{1,...,2n}` and prints
`2n` pairs. Their update descriptions and event encodings also differ. The
handbook preserves both under their own sources. It does not splice Safra's
smaller pair count into Thomas's later tree tuple or claim that one literal
presentation is the other.

## Acquired evidence objects and integrity

All retained objects are under `tmp/pdfs/p09-safra-1988/`.

| Object | Bytes | SHA-256 | Standing |
|---|---:|---|---|
| `DBA-author-hosted.ps` | 247,788 | `2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8` | Complete author-hosted expanded manuscript; actual source body used for the detailed reconstruction. |
| `crossref-work-2026-08-23.json` | 4,116 | `D635796C74804B3972970AA6D634EF4E8DEF2752BAF6AF279BD57E9F66B96602` | Registered-work metadata. |
| `crossref-neighbor-21949-2026-08-23.json` | 5,110 | `76E3682AE38B32A22FD4A8CD7800EE43349B6657EAED88B8F31487C06339F402` | Neighbor-DOI disambiguation. |
| `dblp-record-2026-08-23.xml` | 561 | `4E7ED9BE4E80EEA260D8F415826A503E574D055CD987FB2BBAA5D67D0721F28F` | Registered-work metadata. |
| `openalex-work-2026-08-23.json` | 13,786 | `93797AE265D630AE56A1EBD04A7A1AA8064FB253BD7C09AD8585FB3D6DC6FA8F` | Access-state metadata. |
| `semantic-scholar-work-2026-08-23.json` | 997 | `B2407554EECCC88D1F8F0FCA7DA81563793CC1CB2301E2B27C921B641432245A` | Access-state metadata. |
| `tau-cris-record-2026-08-23.html` | 41,954 | `BB0979E4C464A425E0B32C0C935565FB27BC01FE485C835931E45EA594EA0099` | Institutional metadata and abstract. |

No challenge page or sign-in response is treated as a source PDF. No derived
page image is an independent evidence object.

## Rights and reader-facing disposition

The university directory makes the PostScript lawfully readable for research,
but no open-content or republication licence was found. The handbook therefore
uses independently written exposition, mathematical notation, bounded source
locators, and attribution; it does not reproduce the article's prose or drawn
automata.

The reader-facing manuscript may now give the full expanded-manuscript state,
update, acceptance invariant, correctness proof, complexity count, and named
applications, provided that every detailed claim cites the expanded manuscript
entry. The proceedings entry supports only its registered identity and
abstract-level claims. The exact nine-page wording, theorem numbering,
compression choices, drawings, qualifications, and proof detail remain open
until the proceedings body itself is acquired and compared.

This acquisition and reconstruction do not by themselves admit
`N-c-013.d`. A frozen actual-LaTeX snapshot must receive independent
source-fidelity, mathematical, and adversarial scholarly review. Reviewers read
that `.tex` file directly and consult this actual PostScript source; no
manuscript render or PNG page set substitutes for either file. The one final
publication build remains deferred until the complete book text is frozen.

Three fresh blind Round 3 seats accepted one unchanged five-object snapshot
with no finding after reading the actual `.tex` and actual PostScript directly.
The [independent review record](p09-safra-expanded-1995-independent-review-record.md)
preserves the exact hashes and two rejected predecessor rounds. This admits the
reader content only at author-hosted expanded-manuscript strength. The exact
nine-page proceedings body and every broader topic, part, build, book, human-
review, and publication claim remain open.
