REJECT

# N-c-013 integrated publication and terminology review — Round 1

## Scope and evidence

I read the actual manuscript source
`handbook/parts/p09/presentations/n-c-013.tex` from line 1 through line 1,222
and the actual host source
`handbook/parts/p09/logic-in-computer-science.tex` from line 723 through line
915.  The verdict is based on those LaTeX files.  I also consulted the current
N-c-013 source records where a provenance or terminology boundary required it,
especially the McNaughton, Vardi--Wolper, Büchi, Safra, and Thomas records.  I
did not read another integrated N-c-013 review or an earlier Safra/Thomas review
report.

No manuscript PDF, PNG, page image, rendered page, or other manuscript
rendering was opened.  No build, test, checker, repository script, or hash was
run.  Original-source renderings were not needed to decide these findings.

## Findings

### P1 — Blocking — Appendix B's displayed automaton uses two undefined state-set symbols

**Location:** `handbook/parts/p09/presentations/n-c-013.tex:74-124`, especially
lines 78-100 and 101-117; integrated claim at
`handbook/parts/p09/logic-in-computer-science.tex:748-756`.

The prose defines what a local state is and says which local states may start,
but it never introduces $N_L$ or $N_\varphi$.  The product display then
uses both symbols in

\[
N_M=N_L\times2^{e(\varphi)},\qquad
N_{M0}=N_\varphi\times\{\varnothing\},\qquad
F_M=N_L\times\{\varnothing\}.
\]

The reader can guess that $N_L$ is the set of locally consistent closure
types and that $N_\varphi$ is the subset containing $\varphi$, but the
manuscript does not say so.  This violates definition-before-use and leaves the
standing of two components of the construction implicit.  It is especially
material because the host theorem calls this the complete source presentation
and quotes its $2^{3|A|}$ product bound.

**Required correction:** before the product display, define $N_L$ exactly as
the set of local states satisfying the printed closure conditions and define
$N_\varphi=\{u\in N_L:\varphi\in u\}$, or use the source's exact alternative
if those inferred meanings are not correct.  State that the former is the
local-state set and the latter its initial-state subset.

### P2 — Blocking — The restricted temporal-language names are used without exact local definitions

**Location:** `handbook/parts/p09/presentations/n-c-013.tex:273-345`, especially
lines 273-292, 311-336, and 336-345.

The text defines $F\varphi$ and gives exact definitions of limit equivalence
and $k$-limit equivalence, but it never defines the formula classes
$TL(F)$, $TL(X,F)$, or $TL(Y,S)$.  Calling the last one the ``pure-past
fragment'' does not supply its grammar.  The text gives one scope restriction
for $past\text{-}TL(X,F)$, but its base grammar still depends on the
undefined $TL(X,F)$.  These names are then used to delimit Lemmas 4.1, 4.4,
and 4.6 and Theorems 4.3, 4.5, and 4.7, so their exact extension matters.

Under the governing terminology rule, each name needs at its point of entry an
exact eliminable definition, its standing as a formula fragment, its
nonredundancy from the other fragments, and its use.  The last two are already
substantially present; the definitions and standing are not.

**Required correction:** state the exact source grammar for each fragment
before its first theorem use (for example, the Boolean fragment whose temporal
constructors are precisely $F$, $X,F$, or $Y,S$, if that is the source's
convention), and give the complete formation restriction for
$past\text{-}TL(X,F)$.  Do not leave the reader to infer a grammar from the
subscript notation.

### P3 — Blocking — Büchi's regular-formula class is described but not exactly defined

**Location:** `handbook/parts/p09/presentations/n-c-013.tex:500-573`; later uses
at lines 575-603 and 689-695.

The manuscript introduces $\Sigma^0$ as a class of ``regular formulas whose
auxiliary recurrence is constrained on a finite interval,'' but does not give
the promised recurrence schema: the auxiliary-state quantifier, the initial
condition at $x$, the transition condition on $x\le t<y$, and the endpoint
condition at $y$ remain implicit.  Merely stating that truth depends on the
finite factor is not an eliminable definition of the formula class.  The class
is then essential to Lemmas 2--6, the multiperiodic bridge, Lemmas 9--10, and
the proposed axiom schema.  Its formula/denotation overload and its later use
are well explained, but its defining syntax is not.

**Required correction:** print an exact schematic $\Sigma^0$ formula with
all typed variables and interval bounds, or explicitly mark the exact syntax as
an owed source artifact and refrain from using the class as though already
defined.  The current source record contains enough structural information to
state the initial, transition, and endpoint parts; the manuscript should not
compress those out at the definition point.

### P4 — Blocking — The host citation cluster retrojects later automaton names into sources that do not support them

**Location:** `handbook/parts/p09/logic-in-computer-science.tex:723-745` and
759-762; controlling boundaries at
`handbook/parts/p09/presentations/n-c-013.tex:469-498`, 622-632, 757-781,
783-798, and 1036-1094.

The host defines deterministic parity and Rabin word automata, says that
determinization and translations connect their language classes, and attaches
the undifferentiated citation
`\cite{Buchi1962,McNaughton1966,Thomas1996Report}`.  That citation cannot carry
the paragraph as written:

- the Büchi presentation expressly says that the modern automaton tuple and
  terminology are handbook-owned rather than printed by Büchi;
- the McNaughton article body is unavailable, and its presentation expressly
  withholds every tuple, acceptance clause, construction, and later
  Muller/Rabin name;
- the Thomas report presentation supports the stated Rabin convention, but the
  N-c-013 source presentation supplies no parity-automaton translation or
  parity determinization result;
- the detailed Safra construction belongs to the 1995 expanded manuscript, not
  the unread 1988 proceedings body.  The 1988 abstract supports only its narrow
  announcement-level claims.

The second cluster, `\cite{Safra1988,Thomas1996Report}` after ``deterministic
parity or Rabin automata provide convenient complemented forms,'' repeats the
parity-support problem and does not tell the reader which version supports
which part.  Most seriously, the first cluster visually attributes later
parity/Rabin terminology to the unread McNaughton paper despite the explicit
open-cell rule in the presentation.

**Required correction:** partition citations claim by claim.  Remove
`McNaughton1966` from any definitional or acceptance-condition support unless
the article body is acquired; if historical attribution is retained, state
that Thomas's report supplies the later proof/attribution and that the 1966
body remains unread.  Cite `Thomas1996Report` and, for expansion-level Safra
details, `Safra1995Extended` at their actual strength.  Either supply a
source-backed parity presentation and translation claim or delete parity from
this N-c-013 claim.  Do not let a terminal citation cluster imply that every
listed source supports every preceding definition.

### P5 — Blocking — The host silently crosses Vardi--Wolper's start-set convention into the handbook's single-start convention

**Location:** source convention at
`handbook/parts/p09/presentations/n-c-013.tex:42-60`; the handbook's
single-start comparison is acknowledged at lines 469-498; host reuse and
theorem at `handbook/parts/p09/logic-in-computer-science.tex:723-725` and
748-756.

Vardi--Wolper's literal tuple has a start set $S_0\subseteq S$.  The host
definition says that the handbook reuses Definition
`def:p08-buchi-automaton`, and the N-c-013 presentation itself records that
the reused definition has one initial state.  The host theorem nevertheless
calls the resulting object a handbook Büchi automaton while calling the bound
Vardi--Wolper's literal Theorem 2.1 result, without supplying or owning the
normalization between the conventions.

The asymptotic $2^{O(|A|)}$ statement can survive a one-state normalization,
but the exact $2^{3|A|}$ product count is the source construction before that
normalization.  The two claims should not be made to share an unstated tuple
convention.

**Required correction:** either state the theorem using the source's permitted
initial-state set, or give the explicit handbook-owned conversion to the
single-start tuple and keep the source's pre-normalization $2^{3|A|}$ count
labelled as such.  Record any added state rather than silently treating the two
tuples as identical.

### P6 — Blocking — Theorem 4 uses undefined arithmetic terminology and defines source abbreviations only after first use

**Location:** `handbook/parts/p09/presentations/n-c-013.tex:717-728`.

The structures containing $\mathrm{Re}$ and $\mathrm{Ra}$ are displayed
before either abbreviation is glossed.  More importantly, the assertion that
their first-order theories are ``arithmetically equivalent'' has no exact
meaning in the manuscript: it is unclear whether the claim is mutual
interpretability, effective many-one reducibility of truth sets, definitional
equivalence, or another source-specific relation.  The following paragraph
carefully preserves the source's $\mathrm{Nn}$ discrepancy, but it does not
close this prior definition gap.  Presenting the phrase as a clean theorem
polishes past what the reader-facing reconstruction has defined.

**Required correction:** introduce $\mathrm{Re}$ and $\mathrm{Ra}$ before
the display and give an exact eliminable meaning for ``arithmetically
equivalent.''  If the complete source does not determine that meaning, label it
as an unresolved source phrase and state only the independently exact
decidability consequence.  Preserve the existing $\mathrm{Nn}$ discrepancy
rather than choosing one reading.

### P7 — Blocking — The host S1S theorem has an ambiguous free-variable scope and suppresses handbook ownership of the modern converse

**Location:** `handbook/parts/p09/logic-in-computer-science.tex:830-840`;
controlling account at
`handbook/parts/p09/presentations/n-c-013.tex:605-632`.

``Every formula with $k$ free monadic variables'' does not say whether free
individual variables are excluded.  The displayed alphabet
$\{0,1\}^k$ encodes only the $k$ monadic assignments.  If free individual
variables are permitted, their values require an additional stated encoding;
if they are not, the hypothesis must say so.  The presentation itself notes
that the source separately extends the normal form to free individual
variables.

The same host theorem presents the two-way modern Büchi-language
correspondence under the title ``Büchi's decision theorem'' and the sole source
field `Buchi1962`, while the detailed presentation correctly identifies the
modern tuple and converse coding as a handbook-owned corollary rather than a
literal theorem in the article.  A distant source presentation does not cure
the local attribution ambiguity in the public theorem box.

**Required correction:** say that the only free variables are the named $k$
monadic variables, or supply the singleton-track encoding for free individuals.
Within the theorem box, distinguish Büchi's recurrent normal form and decision
theorem from the handbook-owned modern automaton packaging and converse coding.

## Coverage with no further finding

- `n-c-013.tex:8-15` correctly identifies the Vardi--Wolper file as an author
  preprint rather than a proceedings facsimile, and the later theorem/proof
  boundaries remain reader-visible.
- `n-c-013.tex:757-781` correctly keeps every body-dependent McNaughton datum
  open and does not import the adjacent fallacious game-memo claim.  Finding P4
  concerns the host citation, not this bounded presentation.
- `n-c-013.tex:783-1034` correctly separates the unread nine-page Safra 1988
  paper from the author-hosted 1995 expanded manuscript.  All detailed
  locators use `Safra1995Extended`, handbook-owned repairs are labelled, and
  the $n$-name/$n$-pair construction is not fused with Thomas's version.
- `n-c-013.tex:1036-1222` correctly labels the acquired Thomas body as the May
  1996 report precursor rather than the unread 1997 chapter.  The
  $2n$-name/$2n$-pair convention, empty-state completion, current-mark
  clarification, and repaired accepting-cycle criterion all retain their
  stated ownership and source boundary.
- The locally introduced terms `semi-deterministic`, `multiperiodic`,
  $SC_{\mathrm{per}}$, Safra's `specific`, the rejecting sink, the absence
  symbol, `deterministic in the limit`, and Thomas's `Safra tree` otherwise
  supply the needed definition, standing, distinction, and subsequent use.

Because P1--P7 affect definition-before-use, theorem scope, or source
attribution in the actual LaTeX, this snapshot is not publication-admissible.
