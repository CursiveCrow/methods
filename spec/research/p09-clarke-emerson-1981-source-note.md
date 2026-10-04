# Clarke--Emerson 1981 workshop / 1982 LNCS chapter: source note

**Registered presentation:** N-c-016.a, Edmund M. Clarke and E. Allen
Emerson, “Design and Synthesis of Synchronization Skeletons Using Branching
Time Temporal Logic.”

**Disposition:** PUBLISHED TWENTY-PAGE BODY, FORMULA PRESENTATION, RESULTS,
FIGURES, AND SOURCE-VERSION BOUNDARIES CLOSED FROM AN AUTHORIZED REPRINT;
SPRINGER-DIRECT DOWNLOAD REMAINS SUBSCRIPTION-RESTRICTED.

## Bibliographic identity and controlling object

The event and publication years must be kept distinct.

- Clarke's [older CMU bibliography](https://www.cs.cmu.edu/~emc/publications.html)
  describes the paper as presented at the
  Workshop on Logic of Programs, Yorktown Heights, New York, May 1981. That
  is the basis for the registered presentation year.
- Springer's official chapter record cites the work as a 1982 conference
  paper in Dexter Kozen, ed., *Logics of Programs*, *Lecture Notes in Computer
  Science* 131, pp. 52--71, DOI
  [10.1007/BFb0025774](https://doi.org/10.1007/BFb0025774). The
  [official book record](https://link.springer.com/book/10.1007/BFb0025769)
  gives Springer-Verlag Berlin Heidelberg, copyright 1982, VIII + 429 pages,
  and softcover publication on 1 March 1982.
- The chapter page's later “First Online” and “Published” dates concern the
  digitized Springer record; they do not change the original volume year.

The formal bibliography for the printed chapter is therefore:

> Clarke, Edmund M., and E. Allen Emerson. “Design and Synthesis of
> Synchronization Skeletons Using Branching Time Temporal Logic.” In
> *Logics of Programs*, edited by Dexter Kozen, Lecture Notes in Computer
> Science 131, 52--71. Berlin and Heidelberg: Springer, 1982.
> https://doi.org/10.1007/BFb0025774.

The controlling body used for this note is the complete twenty-page
[CMU-author-hosted Springer reprint](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Design%20and%20synthesis%20of%20synchronization%20skeletons%20using%20branching%20time%20temporal%20logic.pdf),
linked from Clarke's [CMU publications index](https://www.cs.cmu.edu/~emc/papers.htm).
Its first page says that the chapter was originally published in Kozen's
LNCS 131, pp. 52--71 (1982). The reprint appears in the 2008 Springer volume
*25 Years of Model Checking* at pp. 196--215. It preserves the complete
twenty-page original body and adds only the reprint footer and original-
publication notice on its first page.

Throughout this note, “original p. 52” means the chapter's original LNCS
pagination, “reprint p. 196” means the pagination printed by the 2008 volume,
and “PDF p. 1” means the physical PDF page. The mapping is exact:

\[
  \text{original page}=51+\text{PDF page},\qquad
  \text{reprint page}=195+\text{PDF page}.
\]

## Access, file identity, scan state, and rights

Both retrieved PDF objects are first-party author-hosted files, but they are
different source objects.

| Source object | Stable access route | Bytes | Pages | SHA-256 | Body status |
|---|---|---:|---:|---|---|
| Authorized 2008 Springer reprint of the original LNCS chapter | [CMU PDF](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Design%20and%20synthesis%20of%20synchronization%20skeletons%20using%20branching%20time%20temporal%20logic.pdf) | 18,066,035 | 20 | `EC3B3C64045CD7B5ADAD09C9C442AAAC9B8933508FD4EB64DE0D2FCBEE2B7F75` | Controlling complete published body |
| Fuller author manuscript | [CMU PDF](https://www.cs.cmu.edu/~emc/papers/Invited%20Conference%20Articles/Design%20and%20Synthesis%20of%20Synchronization%20Skeletons%20Using%20Branching%20Time%20Temporal%20Logic.pdf) | 1,421,920 | 66 | `A9757ADAF5CF8C797607D57E754CDEAFFD96D9FED20A993B532DF59553F48154` | Separate 37-numbered-page manuscript plus 29 figure sheets; not the controlling chapter |

Retrieval and inspection date: 22 August 2026.

The controlling file is PDF 1.6, 430 by 660 points, with twenty pages. Its
metadata gives creation 12 May 2008 and modification 2 July 2008. The
chapter body is a page image; the sparse reprint overlay does not supply a
reliable body text layer. The CMU server allowed anonymous HTTP retrieval and
returned `application/pdf`; the observed file had `Last-Modified: Thu, 06 Feb
2014 20:58:00 GMT` and ETag `"113aa73-4f1c320ea8600"`.

The fuller manuscript is PDF 1.2, US letter size, with sixty-six physical
pages. Its metadata identifies an HP 9100C Digital Sender scan made on
26 February 2004; it has no usable text layer. The CMU server likewise allowed
anonymous retrieval; the observed response had `Last-Modified: Tue, 06 Jul
2004 19:44:02 GMT` and ETag `"15b260-3de91e020c480"`.

All twenty controlling pages were rendered at 200 dpi and inspected visually.
All sixty-six manuscript pages were rendered at 150 dpi and inspected
visually for version comparison. Formulae and page locators below were checked
against the page images, not accepted from OCR.

The reprint's first page states copyright © Springer-Verlag Berlin Heidelberg
2008 and identifies the original Springer publication. The
[official Springer chapter page](https://link.springer.com/chapter/10.1007/BFb0025774)
states © 1982 Springer-Verlag Berlin Heidelberg, exposes only subscription
access to the publisher PDF, and links to reprints and permissions. No open
license or Creative Commons grant was found. Public author-hosted access
permits inspection; it is not evidence of permission to republish the scan.
The fuller manuscript displays no affirmative republication license either.

## Published-body visual page audit

| Original / reprint / PDF page | Visually inspected content |
|---|---|
| 52 / 196 / 1 | Title, authors and Harvard affiliation; §1 introduction; definition and motivation of a synchronization skeleton; finite-model synthesis claim; original-publication and reprint notices |
| 53 / 197 / 2 | Prior synthesis work; model checking as mechanical finite-state verification; paper outline; beginning of §2 computation-tree model |
| 54 / 198 / 3 | Process flowgraphs and code regions; §3 CTL historical relation to EC80 and UB; complete primitive grammar |
| 55 / 199 / 4 | Structure and path definitions; inductive satisfaction clauses; validity and satisfiability; Boolean, release, eventuality, invariance, and next abbreviations |
| 56 / 200 / 5 | Remaining next abbreviations; §4 labelling model checker; until fixed-point identity; defective displayed approximation |
| 57 / 201 / 6 | Model-checker pseudocode; infinitely-often extension; Proposition 4.1 and first part of proof |
| 58 / 202 / 7 | End of Proposition 4.1 proof; Figures 4.1--4.4 |
| 59 / 203 / 8 | Model-checking time bound; arbitrary linear-time path-prefix extension; Proposition 4.2 and first part of proof |
| 60 / 204 / 9 | End of Proposition 4.2 reduction; experimental C/DEC 11/70 implementation; §5 tableau input/output and three stages; correction footnote concerning BM81 |
| 61 / 205 / 10 | AND/OR labels; `Blocks` and `Tiles`; alpha/beta expansion; elementary/nonelementary formulae; termination count; `EFp ∧ EF~p` example begins |
| 62 / 206 / 11 | Figure 5.1, the complete tableau for `EFp ∧ EF~p` |
| 63 / 207 / 12 | Consistency/eventuality checks and finite-model choice; §6 three-step synthesis procedure; mutual-exclusion code regions and Figure 6.1 |
| 64 / 208 / 13 | The nine numbered mutual-exclusion requirement groups; beginning of tableau-recording conventions |
| 65 / 209 / 14 | Remaining conventions; representative OR-node labels; pruning an inconsistent mutual-exclusion branch; model-fragment construction begins |
| 66 / 210 / 15 | Figure 6.2, the reduced tableau/model-fragment scaffold |
| 67 / 211 / 16 | Figures 6.3--6.5, selected local fragments; Figure 6.6, completed global system flowgraph |
| 68 / 212 / 17 | Why the model satisfies mutual exclusion; insertion of assignments to `TURN`; beginning of per-process factorization |
| 69 / 213 / 18 | Figure 6.7(a),(b), the factored skeletons for `P_1` and `P_2`; beginning of the general factoring rule |
| 70 / 214 / 19 | General factoring rule and auxiliary-label treatment; §7 conclusion; implementation acknowledgement |
| 71 / 215 / 20 | §8 bibliography, eighteen entries |

## Program model and the source term “synchronization skeleton”

The paper defines a **synchronization skeleton** at original p. 52 as an
abstraction of an actual program in which detail irrelevant to
synchronization is suppressed. Its standing in the paper is therefore a
finite-state program abstraction, not a temporal formula, semantic structure,
or proof object. It is needed because code regions such as a process's entire
critical section can be represented by one node while only transitions among
regions and their enabling conditions matter for synchronization. The term is
used again for the per-process flowgraphs factored from the constructed global
model in §6.

The computation model, original pp. 53--54, has finitely many fixed processes
running in parallel. Parallelism is nondeterministic interleaving of the
processes' sequential atomic actions. An execution state contains the
processes' location counters and data values. From a chosen start state, all
nondeterministic executions form a computation tree: nodes carry execution
states, and an outgoing arc carries the index of the process whose atomic
action produces that successor.

Each process `P_i` is also represented as a flowgraph. A node is a uniquely
labelled code region, and an arc represents a possible transition between
regions. The internal computation within a region is left uninterpreted
because it is irrelevant to the synchronization abstraction. The synthesis
problem is to supply enabling conditions on the arcs so that the global
system satisfies a temporal specification.

This must not be strengthened silently. The chapter addresses the control
structure relevant to synchronization; it does not synthesize the suppressed
functional code, prove that an arbitrary low-level implementation realizes
each atomic region, or supply a refinement theorem from machine instructions
to the skeleton.

## Literal CTL grammar, structures, and satisfaction

### Source grammar

Section 3 calls the language a propositional branching-time Temporal Logic
named **Computation Tree Logic (CTL)**. It says the language is based on EC80
and uses notation inspired by Unified Branching Time (UB). Its primitive
formation rules, original p. 54, are:

1. an atomic proposition `p`, `f_1 ∧ f_2`, and `~f_1` are formulae;
2. `EX_j f_1` is a formula, intuitively true when one atomic step of process
   `P_j` can reach an immediate state satisfying `f_1`;
3. `A[f_1 U f_2]` is a formula, requiring the stated strong-until condition
   on every computation path;
4. `E[f_1 U f_2]` is a formula, requiring that condition on some computation
   path.

Thus branching quantification is built into the `A[U]` and `E[U]`
constructors. `EX_j` additionally records which process makes the next move.
There is no separate syntactic category of arbitrary path formulae in the
base language.

### Structures and paths

At original p. 55 a structure is

\[
M=(S,A_1,\ldots,A_k,L),
\]

where `S` is a countable set of states, `A_i ⊆ S × S` gives the possible
transitions by process `i`, and `L` assigns the atomic propositions true at
each state. Let `A=A_1 ∪ ... ∪ A_k`. The source requires `A` to be total:
for every `x∈S` there is a `y` with `(x,y)∈A`. A path is an infinite sequence
`(s_0,s_1,s_2,...)∈S^ω` with `(s_i,s_{i+1})∈A` for every `i`. In the associated
computation tree, an arc from a node labelled `s` to a node labelled `t`
carries process index `i` exactly when `(s,t)∈A_i`.

The semantic state space is therefore countable, not definitionally finite.
Finiteness is imposed by the model-checking input and by the finite-model
synthesis procedure. The paper calls `M` a “structure”; it does not use the
later handbook term “Kripke structure.”

### Satisfaction clauses

For a state `s_0`, the printed clauses are equivalent to:

\[
\begin{aligned}
s_0\models p
  &\iff p\in L(s_0),\\
s_0\models \mathord{\sim}f
  &\iff \text{not }(s_0\models f),\\
s_0\models f_1\land f_2
  &\iff s_0\models f_1\text{ and }s_0\models f_2,\\
s_0\models EX_j f
  &\iff \exists t\,((s_0,t)\in A_j\land t\models f),\\
s_0\models A[f_1 U f_2]
  &\iff \text{for every path }(s_0,s_1,\ldots),\ 
     \exists i\ge 0\,[s_i\models f_2\land
     \forall j(0\le j<i\Rightarrow s_j\models f_1)],\\
s_0\models E[f_1 U f_2]
  &\iff \text{for some path }(s_0,s_1,\ldots),\ 
     \exists i\ge 0\,[s_i\models f_2\land
     \forall j(0\le j<i\Rightarrow s_j\models f_1)].
\end{aligned}
\]

Both until operators are strong: the witness state satisfying `f_2` must
exist. The witness may be the current state (`i=0`), in which case the
`f_1` prefix condition is vacuous.

The paper writes `⊨f` for truth at every state in every structure and `⊭f`
for satisfiability, meaning truth at some state in some structure. The second
glyph is the paper's printed satisfiability notation; modern presentations
should not mistake it for a claim of non-validity.

### Printed abbreviations

Original pp. 55--56 define Boolean disjunction, implication, and equivalence
in the usual way and then give:

\[
\begin{aligned}
A[f_1 V f_2] &\equiv \mathord{\sim}E[\mathord{\sim}f_1 U
  \mathord{\sim}f_2],\\
E[f_1 V f_2] &\equiv \mathord{\sim}A[\mathord{\sim}f_1 U
  \mathord{\sim}f_2],\\
AFf &\equiv A[\mathrm{true}\ U f],\\
EFf &\equiv E[\mathrm{true}\ U f],\\
AGf &\equiv \mathord{\sim}EF\mathord{\sim}f,\\
EGf &\equiv \mathord{\sim}AF\mathord{\sim}f,\\
AX_i f &\equiv \mathord{\sim}EX_i\mathord{\sim}f,\\
EXf &\equiv EX_1f\lor\cdots\lor EX_kf,\\
AXf &\equiv \mathord{\sim}EX\mathord{\sim}f.
\end{aligned}
\]

The paper describes `A[V]` and `E[V]` directly by a release-style condition:
at each state on the relevant path(s), if `f_1` has been false at every prior
state, then `f_2` holds at the current state. The `V` notation is source
notation; it should not be replaced silently by a differently scoped later
operator without showing the equivalence.

## Model checking and verification

### Input, output, and labelling procedure

Section 4 takes a formula `f_0` and a **finite** structure
`M=(S,A_1,...,A_k,L)`. Let `sub^+(f_0)` be the set of subformulae whose main
connective is not negation. The procedure labels every state with `f` or
`~f` for each `f∈sub^+(f_0)` so that the label records whether `M,s⊨f`.
It makes `n+1` passes for `n=length(f_0)`, treating subformulae in increasing
length. Atomic, conjunction, and `EX_j` cases use already available labels.
Until formulae are propagated outward from states where their right operand
already holds; after the positive cases are exhausted, the complementary
negative labels are added. The output is therefore truth information for the
formula at each state, and in particular the answer to whether a designated
state satisfies it.

The printed algorithm is a model checker for an already supplied finite
structure. It is distinct from §5's satisfiability procedure, whose input is
only a formula and whose successful output includes a finite model.

### Until recurrence and a printed display defect

Immediately before the displayed approximants, original p. 56 prints the
correct identity

\[
A[f_1 U f_2]=f_2\lor(f_1\land AXA[f_1 U f_2]).
\]

Its prose says to add the until formula at `s` either when `f_2` already holds
there or when `f_1` holds there and the until formula holds at every immediate
successor. The next-page pseudocode likewise tests `f_1∈set(s)` before either
the universal or existential propagation step.

The displayed universal approximants on original p. 56 nevertheless read:

\[
\begin{aligned}
(A[f_1 U f_2])^0 &= f_2,\\
(A[f_1 U f_2])^{k+1} &= f_2\lor AX((A[f_1 U f_2])^k).
\end{aligned}
\]

The second line has lost the required `f_1∧` guard. Taken literally, it is
not an approximation of the stated strong-until semantics. This is a printed
display defect, not a different semantics: the preceding identity, the
explanatory prose, and the algorithm on original p. 57 all retain the guard.
The same omission occurs in the corresponding display on printed p. 11 of
the fuller manuscript.

The published chapter does not separately display an `E`-until recurrence.
Its immediate-base case and guarded pseudocode propagation jointly support
the following reconstruction:

\[
\begin{aligned}
(E[f_1 U f_2])^0 &= f_2,\\
(E[f_1 U f_2])^{k+1}
  &=f_2\lor(f_1\land EX((E[f_1 U f_2])^k)).
\end{aligned}
\]

That formula is an evidentiary reconstruction from the two printed algorithm
clauses, not a quotation of a separate display in the chapter. The fuller
manuscript's fixed-point table, printed p. 9, independently prints
`E[f U g] = lfp Z [g ∨ (f ∧ EXZ)]`.

### Infinitely-often extension and Proposition 4.1

Original p. 57 next says that the logic may be extended to permit

\[
\forall\text{ path }\forall^\infty\text{ node }p
\]

or its dual

\[
\exists\text{ path }\exists^\infty\text{ node }p,
\]

which the paper writes `E^∞Fp`, with the infinity mark printed over `E`.
This is an explicit extension, not a constructor in the grammar of §3.

**Proposition 4.1** (original pp. 57--58; reprint pp. 201--202; PDF
pp. 6--7) states that `M,s⊨E^∞Fp` exactly when a path from `s` reaches a state
`s'` satisfying `p` and either `s'` is its own successor or the strongly
connected component containing `s'` has cardinality greater than one. The
proof supplies both directions. Its forward direction writes an infinite
path `(s_0,s_1,s_2,...)`, with `s_0=s`, and a state `s'` such that `s'=s_i`
for infinitely many distinct indices `i`; the reverse direction constructs
an infinite path through the self-loop or nontrivial strongly connected
component.

The finite-structure context matters. The proposition's displayed statement
says merely “a structure,” but §4 began by assuming a finite structure, and
the inference from infinitely many `p` positions to one repeated `p` state
uses that context. The handbook should state the finite hypothesis explicitly
rather than generalize the proposition to arbitrary countable structures.

### Time bound and the arbitrary-path extension

Original p. 59 states that basic CTL model checking runs in

\[
length(f)\cdot(card(S))^2
\]

time. Because strongly connected components can be found in linear time, the
same displayed bound is said to hold after adding the infinitely-often
quantifiers. These are the chapter's stated bounds; it neither claims the
later linear-in-structure CTL bound nor proves a matching lower bound.

The paper then considers a different extension: prefix an arbitrary assertion
of linear-time logic by an existential or universal path quantifier. Its
example allows formulae such as

\[
E[Fg_1\land\cdots\land Fg_n\land Gh_1\land\cdots\land Gh_n].
\]

**Proposition 4.2** (original pp. 59--60; reprint pp. 203--204; PDF
pp. 8--9) reduces Directed Hamiltonian Path to model checking this extension.
For graph vertices `v_1,...,v_n`, it labels `v_i` only with `p_i`, adds a new
source `u_1` reaching all vertices and a sink `u_2` reached from every vertex,
and gives `u_2` a self-loop. The formula is

\[
E[,Fp_1\land\cdots\land Fp_n
\land G(p_1\to XG\mathord{\sim}p_1)\land\cdots\land
G(p_n\to XG\mathord{\sim}p_n),].
\]

The complete printed proof shows that it holds at `u_1` exactly when there is
an infinite path that visits every graph vertex exactly once before remaining
at the sink, hence exactly when the original graph has a directed Hamiltonian
path. The conclusion supported is NP-hardness for model checking the extended
language. It is not an NP-hardness result for the base CTL grammar.

The chapter reports an experimental implementation of the model checker in C
on a DEC 11/70 at Harvard; its concluding footnote credits Marshall Brinn with
the programming. No source code, benchmark table, or machine-checked
correctness artifact is part of the chapter.

## Tableau decision procedure

### Published input, output, and proof boundary

Section 5 explicitly says it is an **outline** and “briefly” describes the
procedure; detail is in “the full paper.” The input is a CTL formula `f_0`.
The output is either “YES, `f_0` is satisfiable” or “NO, `f_0` is
unsatisfiable”; in the yes case a finite model is constructed. The three
published stages, original p. 60, are:

1. build a finite directed AND/OR tableau `T` encoding candidate models;
2. delete inconsistent portions and decide by whether the root is deleted;
3. unravel the remaining tableau into a model of `f_0`.

OR-node labels are written `G_i`, AND-node labels `H_i`, and arbitrary labels
`F_i`; the root is `G_0={f_0}`. Same-type nodes with identical labels are
identified, so no two AND nodes share a label and no two OR nodes share a
label.

### Literal `Blocks` and `Tiles` content in the chapter

At original p. 61 the paper defines `Blocks(G)={H_1,...,H_k}` to be the set of
successors of an OR node `G`, with the intended satisfiability relation

\[
\text{`G` is satisfiable iff `H_1` or ... or `H_k` is satisfiable}.
\]

It classifies a conjunctive formula as `α≡α_1∧α_2` and a disjunctive formula
as `β≡β_1∨β_2`. The printed examples are:

- `f∧g` is alpha and `f∨g` is beta;
- `EFp=p∨EXEFp` is beta;
- `AGp=p∧AXAGp` is alpha.

A formula with no modalities or with main connective `EX` or `AX` is called
**elementary**; every other formula is **nonelementary**. A set `F` is called
**downward closed** when (i) `α∈F` implies `α_1,α_2∈F`, and (ii) `β∈F`
implies `β_1∈F` or `β_2∈F`. `Blocks(G)` is constructed by repeatedly
expanding nonelementary formulae; an alpha expansion keeps both components,
whereas each beta expansion produces two alternatives. Expansion stops when
all resulting `H_i` are downward closed.

The paper defines `Tiles(H)={G_1,...,G_k}` as the set of successors of an AND
node `H`. If `H` contains no propositional inconsistency, its intended relation
is

\[
\text{`H` is satisfiable iff every one of `G_1`,...,`G_k` is satisfiable}.
\]

The chapter says `Tiles(H)` uses the elementary formulae in `H` and gives the
single concrete construction:

\[
\{AXh_1,AXh_2,EXg_1,EXg_2,EXg_3\}
\quad\mapsto\quad
\{\{h_1,h_2,g_1\},\{h_1,h_2,g_2\},\{h_1,h_2,g_3\}\}.
\]

That is the complete published `Tiles` detail. Process-indexed formal clauses
and exceptional cases occur only in the fuller manuscript and must not be
presented as though printed on original p. 61.

The chapter bounds the number of possible labels by
`2^{length(f_0)}` and says each can occur at most twice, once for each node
type. This is its termination argument for tableau construction and its
explicit exponential-size warning. It does not state a named complexity
class for satisfiability.

### Consistency, eventualities, and the worked formula

Figure 5.1 (original p. 62) is the complete AND/OR tableau for
`EFp∧EF~p`. Original p. 63 marks a label inconsistent if it contains both
`p` and `~p`; it also requires eventualities such as `AFh` or `EFh` to be
fulfilled. In particular, if `EFh∈F`, some reachable node `F'` must contain
`h`. The example's root survives. A finite model is made from copies of
consistent AND nodes, choosing successors so that the two eventualities are
actually fulfilled; the text chooses `H_0` as root and `H_5` as its successor
to fulfill `EF~p`, after which `H_5` loops to itself.

The published text illustrates these operations but does not print a general
correctness proof or quantitative finite-model theorem. Those boundaries are
material because the longer manuscript does.

### BM81 correction footnote

The footnote on original p. 60 expressly says the BM81 algorithm is incorrect
and can claim that certain satisfiable formulae are unsatisfiable. It directs
the reader to EH81 for corrected tableau- and filtration-based UB decision
procedures and says Ben-Ari reported a forthcoming correction using different
techniques. The chapter does not silently adopt the faulty result.

### What the fuller manuscript adds, and only there

The sixty-six-page CMU object is a distinct fuller author manuscript: a title
sheet, abstract, thirty-seven numbered text pages, and twenty-nine interleaved
figure sheets. Its Appendix §10 supplies detail omitted from the chapter.
These additions are useful for understanding the authors' intended full
procedure, but they are not evidence that the twenty-page publication printed
the appendix.

The appendix's exact alpha/beta component table on manuscript printed p. 31
is:

| Kind | Formula | First component | Second component |
|---|---|---|---|
| alpha | `f∧g` | `f` | `g` |
| alpha | `A[f V g]` | `g` | `f∨AX A[f V g]` |
| alpha | `E[f V g]` | `g` | `f∨EX E[f V g]` |
| beta | `f∨g` | `f` | `g` |
| beta | `A[f U g]` | `g` | `f∧AX A[f U g]` |
| beta | `E[f U g]` | `g` | `f∧EX E[f U g]` |

It constructs a finite propositional expansion tree rooted at `G`; if its
elementary leaves are `F_1,...,F_m`, then
`Blocks(G)={H_1,...,H_m}`, where `H_i` is the union of all formulae on the
path from `F_i` back to the root.

For each process `j∈[1:k]`, manuscript printed p. 32 defines

\[
HA_j=\{f:AX_jf\in H\},\qquad HE_j=\{g:EX_jg\in H\}.
\]

If `HE_j={g_1,...,g_n}`, it defines

\[
Tiles_j(H)=\{G_j^1,\ldots,G_j^n\},\qquad
G_j^i=HA_j\cup\{g_i\},
\]

and then `Tiles(H)=⋃{Tiles_j(H):j∈[1:k]}`. An arc from `H` to a tile is
labelled with every process index whose `Tiles_j(H)` contains that tile. The
appendix also gives two special cases: if the union `HA` is nonempty but the
union `HE` is empty, split `H` into `H_j=H∪{EX_j True}`; if both are empty,
take `Tiles(H)={G}` with `G={f:f∈H}` and `Blocks(G)={H}`.

On manuscript printed p. 37 an unnumbered theorem says the root of the fully
marked tableau `T*` is unmarked iff `f_0` is satisfiable and, if satisfiable,
`f_0` has a finite model of size

\[
O(c^{length(f_0)})\quad\text{for some }c>1.
\]

The next sentence says the proof will not be given and instead cites the
corresponding UB theorem in EH81. Accordingly, even in the fuller manuscript
this is a cited/sketched boundary, not a proved theorem in the scanned body.
The published chapter neither prints this theorem nor supplies the omitted
proof.

## Synthesis procedure and mutual-exclusion example

### The three published stages

At original p. 63, §6 identifies exactly three steps:

1. specify the desired concurrent-system behavior in CTL;
2. apply the satisfiability procedure to obtain a finite model;
3. factor the individual processes' synchronization skeletons from the global
   system flowgraph defined by that model.

The worked system has two processes. For process `P_i`, `NCS_i`, `TRY_i`, and
`CS_i` stand for the noncritical, trying, and critical code regions. Figure
6.1 records the region cycle `NCS_i → TRY_i → CS_i → NCS_i`; moves wholly
inside one region are not part of the synchronization skeleton.

### The nine printed requirement groups

Original p. 64 says the conjunction of the following groups specifies the
mutual-exclusion system. In groups containing `i`, the formula is required
for each process; in group 8, `j` is the other process.

1. **Start state:**
   \[
   NCS_1\land NCS_2.
   \]
2. **Mutual exclusion:**
   \[
   AG(\mathord{\sim}(CS_1\land CS_2)).
   \]
3. **Absence of starvation for `P_i`:**
   \[
   AG(TRY_i\to AFCS_i).
   \]
4. **Each process is always in exactly one of the three regions:**
   \[
   \begin{aligned}
   AG(NCS_i\lor TRY_i\lor CS_i),\\
   AG(NCS_i\to\mathord{\sim}(TRY_i\lor CS_i)),\\
   AG(TRY_i\to\mathord{\sim}(NCS_i\lor CS_i)),\\
   AG(CS_i\to\mathord{\sim}(NCS_i\lor TRY_i)).
   \end{aligned}
   \]
5. **It is always possible to enter the trying region from the noncritical
   region:**
   \[
   AG(NCS_i\to EX_iTRY_i).
   \]
6. **Any move by `P_i` from its trying region enters its critical region:**
   \[
   AG(TRY_i\land EX_i\mathrm{true}\to AX_iCS_i).
   \]
7. **It is always possible to re-enter the noncritical region from the
   critical region:**
   \[
   AG(CS_i\to EX_iNCS_i).
   \]
8. **One process's transition cannot move the other process:**
   \[
   \begin{aligned}
   AG(NCS_i\to AX_jNCS_i),\\
   AG(TRY_i\to AX_jTRY_i),\\
   AG(CS_i\to AX_jCS_i).
   \end{aligned}
   \]
9. **Some process can always move:**
   \[
   AG(EX\mathrm{true}).
   \]

Group 3 is the liveness/starvation requirement; group 2 is the safety
requirement; groups 4--9 also constrain region exclusivity and process-
labelled transitions. The source does not assume a separate fairness
condition in the model definition. The liveness obligation is written into
the branching-time specification itself.

### Tableau pruning, finite global model, and factoring

The chapter suppresses redundant formulae while drawing the large example.
It automatically expands a conjunction into a set, propagates an `AGf`
invariant without repeatedly writing it, omits `f∨g` when `f` is already
present, and uses region membership to omit redundant negative region atoms.
It records only representative OR-node labels, obtains the rest by symmetry,
and deletes a branch containing `CS_1,CS_2` because it contradicts the mutual-
exclusion invariant.

Figures 6.2--6.5 show the remaining tableau and chosen model fragments.
Original pp. 65--68 paste fragments for AND nodes together while ensuring that
eventualities at each fragment root are fulfilled. Cycles are accepted only
after checking that they do not strand an eventuality. Figure 6.6 is the
resulting global system flowgraph. The text then assigns the auxiliary
variable `TURN` on transitions to distinguish otherwise identical source and
target labels and says inspection shows that every infinite path from a
`TRY_i` state reaches `CS_i`.

Figures 6.7(a) and 6.7(b) factor this graph into one skeleton for each process.
The general description at original p. 70 starts process `P_i` with its `m`
code-region nodes and no arcs. It draws `R_j→R_k` when the global flowgraph
contains an `i`-labelled arc whose `P_i` components change from `R_j` to
`R_k`. The enabling condition on that local arc is the disjunction of the
other processes' component labels for all such global arcs. When equal global
labels occur at distinct nodes, auxiliary values are introduced so every
global node has a distinct label, and those assignments are carried onto the
appropriate local transition.

This is a detailed worked construction, not a separately numbered general
synthesis theorem. The conclusion says automatic synthesis is possible and
warns that the algorithm may be exponential; it expresses hope that small
synchronization skeletons make the method practical and says substantial
additional research is needed. The chapter gives neither a polynomial
complexity claim for synthesis nor an implementation of the synthesis stage.

## Numbered results, definitions, and proof status

The controlling twenty-page chapter has no numbered “Definition,” “Lemma,” or
“Theorem” environments. Its only numbered mathematical results are the two
propositions in §4.

| Item | Original-page locator | Exact mathematical role | Evidentiary status in controlling body |
|---|---|---|---|
| Proposition 4.1 | 57--58 | SCC/self-loop characterization of `E^∞Fp` in the finite-model-checking context | Full two-direction proof printed |
| Proposition 4.2 | 59--60 | Directed Hamiltonian Path reduction proving NP-hardness for the arbitrary-linear-path-prefix extension | Full construction and equivalence proof printed |
| Basic CTL model-checker bound | 59 | `length(f)·(card(S))^2`; same displayed bound claimed with infinitely-often quantifiers | Stated with algorithmic explanation and Tarjan SCC citation; not a numbered theorem |
| Tableau termination | 61 | At most `2^{length(f_0)}` labels, each occurring at most once per node type | Direct finite-count argument; not a numbered theorem |
| CTL satisfiability correctness / finite-model property | 52, 60--63 | Decision procedure returns satisfiable/unsatisfiable and constructs a finite model | Claimed and illustrated; published presentation is explicitly a brief outline and refers detail elsewhere |
| Mutual-exclusion synthesis | 63--70 | CTL specification to pruned tableau to finite global graph to two process skeletons | Detailed example; no separately numbered proof of a general synthesis theorem |

The fuller manuscript has differently numbered results and must be cited as a
different version:

- Proposition 4.1, manuscript printed p. 10: `EFh` is the least fixed point of
  `τ[Z]=h∨EXZ`; a proof is printed.
- Proposition 5.1, manuscript printed pp. 13--14: the infinitely-often SCC
  result that became published Proposition 4.1; a proof is printed.
- Theorem 5.2, manuscript printed pp. 14--15: the Hamiltonian reduction that
  became published Proposition 4.2; a proof is printed.
- the unnumbered theorem on manuscript printed p. 37: fully marked tableau
  correctness and exponential finite-model size; the proof is expressly not
  given.

No result should be cited under the manuscript number when the intended
authority is the published chapter.

## Complete worked examples and figure inventory

The controlling body contains the following figures and examples, and no
others:

| Figure(s) | Original page(s) | Function in the paper |
|---|---:|---|
| 4.1--4.4 | 58 | Four snapshots of the labelling algorithm for `AFb∧EGa` (also written `AFb∧~AF~a`) on one finite structure |
| 5.1 | 62 | Complete AND/OR tableau for satisfiability of `EFp∧EF~p` |
| 6.1 | 63 | One process's `NCS_i→TRY_i→CS_i→NCS_i` region cycle |
| 6.2 | 66 | Reduced mutual-exclusion tableau/model-fragment scaffold after inconsistency deletion |
| 6.3--6.5 | 67 | Selected local model fragments used to fulfill eventualities |
| 6.6 | 67 | Constructed global two-process system flowgraph, including `TURN` distinctions |
| 6.7(a),(b) | 69 | Factored synchronization skeletons for `P_1` and `P_2` |

The four §4 snapshots illustrate formula labelling; they are not a proof of
the complexity bound. The `EFp∧EF~p` tableau illustrates satisfiability and
finite-model extraction; it is not the omitted general correctness proof.
The mutual-exclusion sequence is the sole synthesis case study and is the
source of all published skeleton figures.

## Controlling chapter versus fuller manuscript

| Feature | Published LNCS chapter, original pp. 52--71 | Fuller CMU author manuscript |
|---|---|---|
| Physical extent | 20 pages, continuously typeset; controlling object | 66 scan pages: title, abstract, 37 numbered text pages, and 29 separate figure sheets |
| Section structure | §§1--8: introduction, model, language, model checker, decision procedure, synthesis, conclusion, bibliography | §§1--10, including a separate fixed-point section and a detailed decision-procedure appendix |
| Abstract | No abstract heading in the twenty-page body | Separate full abstract page |
| Decision-detail cross-reference | Says the decision procedure is described in detail “in the full paper” | Says the detail is “in the appendix,” and the same scan contains Appendix §10 |
| Fixed-point result | Uses fixed-point identities inside model checking but has no separate numbered fixed-point proposition | Separate fixed-point section and Proposition 4.1 on `EFh` |
| Infinitely-often result | Proposition 4.1 | Proposition 5.1 |
| Hamiltonian result | Proposition 4.2 | Theorem 5.2 |
| Decision-procedure detail | Explicit “brief” outline; says detail is in the full paper | Appendix defines complete alpha/beta table, process-indexed `Tiles`, marking, fragments, and construction |
| Finite-model theorem | General finite-model claim and termination count, but no numbered theorem or quantitative model-size theorem | Unnumbered p. 37 theorem states `O(c^{length(f_0)})`, then explicitly withholds proof and cites EH81 |
| Figures | 4.1--4.4, 5.1, 6.1--6.7 | Additional Figures 3.1--3.2, 5.1--5.6, 6.1--6.3, 7.1--7.15, and 10.1--10.2; figures are renumbered and heavily condensed in publication |
| `A[U]` approximation defect | Present, original p. 56 | Present, manuscript printed p. 11 |
| Bibliography | Eighteen entries; adds `[BA81]` and uses the internally matching key `[SM68]` | Seventeen entries; footnote cites absent `[BA81]`, and text cites `[SM68]` while bibliography prints `[SM63]` for the 1968 Smullyan book |

The manuscript's physical-page map is: PDF p. 1 title; p. 2 abstract;
pp. 3--5 printed pp. 1--3; pp. 6--7 printed pp. 4--5; p. 8 printed p. 6;
p. 9 Figure 3.1; p. 10 printed p. 7; p. 11 printed p. 8; p. 12 Figure 3.2;
pp. 13--14 printed pp. 9--10; pp. 15--17 printed pp. 11--13; pp. 18--23
Figures 5.1--5.6; pp. 24--25 printed pp. 14--15; pp. 26--27 printed
pp. 16--17; p. 28 Figure 6.1; p. 29 printed p. 18; p. 30 Figure 6.2;
p. 31 printed p. 19; p. 32 Figure 6.3; p. 33 printed p. 20; pp. 34--36
Figure 7.1 and printed pp. 21--22; pp. 37--41 Figures 7.2--7.6; p. 42
printed p. 23; pp. 43--44 Figures 7.7--7.9; p. 45 printed p. 24;
pp. 46--48 Figures 7.10--7.12; p. 49 printed p. 25; pp. 50--52 Figures
7.13--7.15; pp. 53--56 printed pp. 26--29; pp. 57--66 Appendix §10,
printed pp. 30--37 with Figures 10.1--10.2 interleaved.

This version separation is controlling: an appendix proof, definition, bound,
or figure may be cited as fuller-manuscript evidence only after being labelled
as such. It cannot close a claim about what the published chapter itself
proves.

## Relation to later CTL, CTL*, and Queille--Sifakis

### Later CTL and CTL*

The paper itself supplies the historically safe description: its language is
CTL, based on EC80 and using UB-like notation. Its exact grammar includes
process-indexed `EX_j` and path-quantified strong until. A handbook may compare
that grammar with later presentations, but must preserve these differences:

- the paper has no separate state-formula/path-formula grammar;
- its base language does not allow an arbitrary linear-time assertion under
  `A` or `E`;
- `E^∞Fp` is introduced as an additional infinitary construction;
- arbitrary path-prefixing of linear-time assertions is introduced as another
  extension and shown NP-hard to model check;
- the paper neither uses the name `CTL*` nor claims that the extension studied
  in Proposition 4.2 is the entirety of the later language CTL*.

It would therefore be anachronistic to cite Proposition 4.2 simply as “CTL*
model checking is NP-hard” or to import later CTL/CTL* syntax, expressiveness,
or complexity classifications into this source.

### Independent Queille--Sifakis line

The chapter's eighteen-entry bibliography contains no Queille--Sifakis or
CESAR entry, and the body does not mention them. No wording, construction, or
result from their independent work should be attributed to this paper.

For historical orientation only, Clarke's later author-hosted paper
[“Model Checking: Back and Forth between Hardware and Software”](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Model%20Checking%20Back%20and%20Forth%20between%20Hardware%20and%20Software.pdf)
states that Clarke--Emerson and, independently, Queille--Sifakis introduced
algorithmic model checking. Springer's official
[*25 Years of Model Checking* record](https://link.springer.com/book/10.1007/978-3-540-69850-0)
places this Clarke--Emerson reprint at pp. 196--215 and the Queille--Sifakis
CESAR reprint at pp. 216--230. Those later first-party editorial facts support
independence and juxtaposition, not identity of the two algorithms or
formalisms.

## Bibliography audit

Original p. 71 contains exactly eighteen keyed entries:

1. `[BA81]` M. Ben-Ari, personal communication, 1981.
2. `[BH81]` M. Ben-Ari, J. Halpern, and A. Pnueli, “Finite Models for
   Deterministic Propositional Logic,” *Proceedings 8th International
   Colloquium on Automata, Languages, and Programming*, to appear, 1981.
3. `[BM81]` M. Ben-Ari, Z. Manna, and A. Pnueli, “The Temporal Logic of
   Branching Time,” 8th Annual ACM Symposium on Principles of Programming
   Languages, 1981.
4. `[CL77]` E. M. Clarke, “Program Invariants as Fixpoints,” 18th Annual
   Symposium on Foundations of Computer Science, 1977.
5. `[EC80]` E. A. Emerson and E. M. Clarke, “Characterizing Correctness
   Properties of Parallel Programs as Fixpoints,” Proceedings 7th
   International Colloquium on Automata, Languages, and Programming,
   LNCS 85, Springer-Verlag, 1981.
6. `[EH81]` E. A. Emerson and J. Halpern, “A New Decision Procedure for the
   Temporal Logic of Branching Time,” unpublished manuscript, Harvard
   University, 1981.
7. `[FS81]` L. Flon and N. Suzuki, “The Total Correctness of Parallel
   Programs,” *SIAM Journal on Computing*, to appear, 1981.
8. `[GP80]` D. Gabbay, A. Pnueli, et al., “The Temporal Analysis of Fairness,”
   7th Annual ACM Symposium on Principles of Programming Languages, 1980.
9. `[HC68]` G. Hughes and M. Cresswell, *An Introduction to Modal Logic*,
   Methuen, London, 1968.
10. `[LA80]` L. Lamport, “Sometime” is Sometimes “Not Never.” 7th Annual ACM
    Symposium on Principles of `Prgramming` Languages, 1980. (`Prgramming` is
    the printed spelling.)
11. `[LA78]` M. Laventhal, *Synthesis of Synchronization Code for Data
    Abstractions*, Ph.D. thesis, MIT, June 1978.
12. `[PA69]` D. Park, “Fixpoint Induction and Proofs of Program Properties,”
    in *Machine Intelligence 5*, D. `Mitchie`, ed., Edinburgh University Press,
    1970.
13. `[PR77]` V. Pratt, “A Practical Decision Method for Propositional Dynamic
    Logic,” 10th ACM Symposium on Theory of Computing, 1977.
14. `[RK80]` K. Ramamritham and R. Keller, “Specification and Synthesis of
    Synchronizers,” 9th International Conference on Parallel Processing,
    1980.
15. `[SM68]` R. M. Smullyan, *First Order Logic*, Springer-Verlag, Berlin,
    1968.
16. `[TA55]` A. Tarski, “A Lattice-Theoretical Fixpoint Theorem and Its
    Applications,” *Pacific Journal of Mathematics* 5, 285--309 (1955).
17. `[TA72]` R. Tarjan, “Depth First Search and Linear Graph Algorithms,”
    *SIAM Journal on Computing* 1:2, 146--160, 1972.
18. `[WO81]` P. Wolper, “Synthesis of Communicating Processes From Temporal
    Logic Specifications,” unpublished manuscript, Stanford University, 1981.

The printed bibliography itself contains historical “to appear” and
“unpublished manuscript” descriptions. They are evidence of the chapter's
1981--82 source context, not current access or final-publication metadata for
those works.

## Source defects and unresolved ambiguities

| Location | Printed issue | Evidentiary treatment |
|---|---|---|
| Original p. 56 | `(A[f_1 U f_2])^{k+1}` display omits `f_1∧` | Record literal display and the proof-supported correction separately; identity, prose, and algorithm all include the guard |
| Original p. 57 | Proposition 4.1 says “a structure” without restating finiteness | Retain §4's finite-input context; do not assert the SCC characterization for arbitrary countable structures |
| Original p. 60 | BM81 algorithm reported incorrect | Preserve the footnote's correction and EH81 referral; do not cite BM81 as the correctness basis |
| Original pp. 60--63 | Published procedure says detail is in “the full paper,” but the chapter does not identify a publication object there | Treat the acquired 66-page scan as a separate fuller manuscript on file identity and matching content; do not call its appendix part of the LNCS chapter |
| Original p. 61 | `Tiles` receives only one unindexed concrete example although the semantic language has process-indexed next modalities | Report only the published outline; process-indexed formal clauses belong to manuscript pp. 31--32 |
| Original p. 52 versus manuscript p. 37 | Published text invokes a bounded finite-model property but omits a quantitative bound; fuller manuscript gives an exponential bound without proof | Keep the published claim, manuscript theorem, and cited-proof boundary distinct |
| Manuscript pp. 16, 28 versus published pp. 60, 71 | Manuscript footnote cites `[BA81]` although its bibliography omits that entry; manuscript text cites `[SM68]` although its bibliography labels the 1968 Smullyan book `[SM63]` | Published chapter adds `[BA81]` and uses `[SM68]`, repairing both cross-reference failures |
| Published p. 71 | `[LA80]` prints `Prgramming`, and `[PA69]` prints editor surname `Mitchie` | Preserve these as printed bibliographic spellings when transcribing the source; do not mistake silent normalization for the chapter's literal text |
| Reprint notice versus official book title | Reprint p. 196 says “Logic of Programs”; Springer calls the book *Logics of Programs* and the event series “Logic of Programs 1981” | Formal publication citation follows the official book title; the singular wording remains part of the reprint notice |
| Springer HTML abstract versus printed body | The official chapter page labels the two conclusion paragraphs as its abstract, but the twenty-page body has no abstract heading and the fuller manuscript has a different, genuine abstract page | Do not attribute the Springer HTML extract to a printed chapter abstract |
| Year surfaces | Workshop/event is 1981; official chapter and LNCS volume are 1982; online metadata is later | Use 1981 for the presentation registration and 1982 for the formal publication citation |

## Evidentiary closure for handbook use

| Needed artifact or claim | Closed? | Controlling evidence and permitted formulation |
|---|---|---|
| Registered identity, venue, DOI, pages, and year distinction | Yes | Official Springer chapter/book records plus the authorized reprint's original-publication notice; presentation 1981, publication 1982 |
| Complete published chapter body | Yes | All twenty pages of the CMU-author-hosted Springer reprint inspected; original pp. 52--71 map exactly to reprint pp. 196--215 |
| File identity and preservation record | Yes | Exact byte counts, page counts, SHA-256 hashes, PDF metadata, scan/text-layer state, and access date recorded above |
| Rights to inspect and quote briefly | Yes, with ordinary source limits | Public author-hosted access and publisher metadata support inspection; no open republication license was found |
| Rights to republish page images or the complete text | No | Springer copyright and permissions surface; author-hosted availability is not a republication grant |
| Source definition and standing of “synchronization skeleton” | Yes | Original pp. 52, 54, 63--70: finite-state abstraction suppressing irrelevant internal code and later factored into per-process flowgraphs |
| Literal CTL grammar, structures, paths, and satisfaction | Yes | Original pp. 54--56; all primitive and derived operators and the total-transition condition recorded above |
| Base CTL model-checker input/output and stated complexity | Yes | Original pp. 56--59; finite structure plus formula, per-state truth labels, stated `length(f)·card(S)^2` bound |
| Exact universal- and existential-until recurrence status | Yes | Literal defective universal display distinguished from the correct identity/loop; existential recurrence labelled as reconstruction, not a separate printed display |
| Infinitely-often extension and Proposition 4.1 | Yes | Original pp. 57--58; exact notation, finite-context SCC condition, and full proof boundary recorded |
| Arbitrary-linear-path extension and Proposition 4.2 | Yes | Original pp. 59--60; exact reduction formula and NP-hardness scope recorded |
| Published tableau input/output, `Blocks`, `Tiles`, termination, and worked model | Yes | Original pp. 60--63; outline status and omitted formal detail explicit |
| Complete published alpha/beta and process-indexed `Tiles` definitions | No, because the chapter does not print them | Fuller manuscript pp. 31--32 supplies them only as version-separated evidence |
| Published general tableau correctness proof and quantitative small-model theorem | No | Chapter gives an outline; fuller manuscript p. 37 states an exponential theorem but explicitly withholds proof and cites EH81 |
| Nine mutual-exclusion requirement groups | Yes | Original p. 64; every formula and prose role recorded above |
| Worked synthesis construction and every published figure | Yes | Original pp. 63--70 and Figures 4.1--4.4, 5.1, 6.1--6.7 visually inspected and inventoried |
| General synthesis complexity or implementation | No | Chapter warns of potential exponential behavior and reports only a model-checker implementation, not a synthesis implementation |
| Distinction from later CTL/CTL* | Yes | Based on the chapter's literal grammar and explicitly marked extensions; no later language name or theorem retrojected |
| Distinction from Queille--Sifakis | Yes | No mention in the chapter; later first-party Clarke and Springer historical surfaces support independent attribution only |
| Independent byte comparison with a Springer-direct subscriber download | No | Official body is subscription-restricted; the controlling authorized reprint is complete but was not byte-compared with a subscriber file |

No tests, checkers, TeX builds, or PDF builds were run. Source PDFs were used
only for read-only metadata inspection, rendering, and visual scholarship.
