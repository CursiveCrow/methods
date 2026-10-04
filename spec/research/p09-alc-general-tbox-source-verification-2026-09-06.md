# ALC general-TBox integration: primary-source verification

Date: 2026-09-06, local time. Verification began at 01:14:50 UTC on
2026-09-07. This is a bounded, read-only manuscript check. Other agents'
review conclusions were not read.

## Outcome

The three cited source locators are correct. The new body and annex use
the correct ALC concept/TBox/finite-KB scope, with no unique-name
assumption. One precise source-normalization clarification is needed:
invoke **CKS Theorem 2.6(b)** explicitly when choosing a machine whose
space bound holds on all reachable configurations. The theorem can be
used with a sufficiently large space-constructible polynomial bound.

The detailed source checks and a proposed attribution paragraph follow.
No manuscript file was changed.

## 1. Baader-Horrocks-Sattler: exact draft theorem and semantics

Read directly from the existing local
`tmp/sources/p09-alc-general-tbox/baader-horrocks-sattler-2008-chapter.pdf`:

- **Definitions 1-3, draft pp. 5-6:** Boolean ALC, concept complements,
  existential/universal restrictions over arbitrary binary roles,
  nonempty interpretation domains, and finite general TBoxes. The
  separate definition of an acyclic/definitorial TBox is a restriction,
  not a hypothesis of Theorem 6.
- **Definitions 4-6, draft p. 7:** finite ABoxes with `x:C` and
  `(x,y):r`, finite KB pairs `(T,A)`, consistency, concept nonemptiness
  in a model, subsumption, and concept-instance checking. The definitions
  impose **no injectivity condition** on the interpretation of individual
  names. There is no UNA side condition to import into the manuscript.
- **Theorem 6, draft p. 26:** ALC concept satisfiability relative to
  general TBoxes is ExpTime-complete. Context and Proposition 5 make
  the input pair `(C,T)` explicit. This numbered theorem is not itself
  a theorem whose input is an ABox/TBox pair; the manuscript proves that
  extension and its further reductions locally.

The [author-hosted PDF](https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2007/BaHS07a.pdf)
is a 47-page draft, with its own page numbers and bare theorem numbers.
Its first-page placeholder front matter says 2007. The publication is
Franz Baader, Ian Horrocks, and Ulrike Sattler, *Description Logics*,
Chapter 3 in *Handbook of Knowledge Representation*, Elsevier, 2008,
pp. 135-179, DOI
[10.1016/S1574-6526(07)03003-9](https://doi.org/10.1016/S1574-6526(07)03003-9).
The live bibliography correctly identifies the draft's distinct locators.

The primary theorem confirms the concept/general-TBox classification.
It does not turn the local type elimination, countdown encoding, or
finite-ABox extension into reproductions of that chapter's proofs.

## 2. Donini-Massacci: exact bound and its hypotheses

Read directly from the existing local
`tmp/sources/p09-alc-general-tbox/donini-massacci-2000.pdf`:

- **Section 2, printed pp. 90-92:** plain ALC grammar, nonempty domain,
  finite unrestricted inclusions, and concept satisfiability relative
  to all inclusions. In this paper `KB` denotes the TBox; it does not
  denote an ABox/TBox pair.
- **Theorem 3.13, printed p. 98** (PDF p. 12): search strategies
  satisfying **Techniques 1-7** terminate in single deterministic
  exponential time in the combined size of `C` and the TBox `KB`.
- **Theorem 6.17, printed p. 123** (PDF p. 37): the number of DFS calls
  is `O(2^(c n))` for a suitable constant `c>1`. The preceding argument
  bounds key branching points and recursion depth. Theorem 3.13 is
  explicitly restated and concluded on the same page.

Thus the locators are exact. The source bound requires its stated
search strategy and reuse of inconsistent sets. It is not a bound on
every sound terminating blocking tableau. The new body and annex
correctly prove their own type-enumeration bound instead.

Publication: Francesco M. Donini and Fabio Massacci, *EXPTIME tableaux
for ALC*, *Artificial Intelligence* 124(1) (2000), 87-138, DOI
[10.1016/S0004-3702(00)00070-9](https://doi.org/10.1016/S0004-3702(00)00070-9).
The [author PDF](https://disi.unitn.it/~massacci/Publications/doni-mass-00-AIJ.pdf)
has 52 pages and retains the publication pagination.

## 3. CKS: class equality and bounded-machine normalization

The exact [primary scan](https://people.cs.umass.edu/~immerman/cs601/alternation.pdf)
was fetched and read in memory. It is Ashok K. Chandra, Dexter C. Kozen,
and Larry J. Stockmeyer, **Alternation**, *Journal of the ACM* 28(1)
(January 1981), 114-133, DOI
[10.1145/322234.322243](https://doi.org/10.1145/322234.322243), 20 PDF pages.

Verified locators:

- **Corollary 3.6, p. 122**, explicitly includes
  `EXPTIME = APSPACE`.
- **Theorem 2.5, pp. 120-121**, removes negating states while preserving
  the language and the time/space acceptance bounds.
- **Theorem 2.6(b), p. 121; proof p. 122**, applies when `S(n) >= log n`
  is space-constructible. It produces an equivalent machine with every
  path terminating in exponentially bounded length and every reachable
  configuration satisfying the space bound.
- **Definition 2.5, p. 120**, initially bounds accepting computations;
  it does not by itself bound every reachable configuration. This is
  why Theorem 2.6(b) should be named for the stronger machine convention.
- **Definition 2.3, p. 117**, requires at least one successor for every
  nonhalting existential or universal configuration. The annex's
  empty-choice discussion is an elementary conversion from other
  possible conventions, not the convention used in CKS.

The original machine has a separate read-only input tape and finitely
many work tapes. The annex's finite-track, marked-head one-tape
simulation and binary branching conversion are locally explained
elementary normalizations; they need not be attributed to a specific
CKS theorem. Increase the polynomial bound after these simulations.

## 4. Actual insertion read and the exact repair

Both files were read in full:

- `handbook/parts/p09/alc-general-tboxes.tex`;
- `handbook/annex/p09/alc-general-tboxes.tex`.

The body theorem `thm:p09-alc-general-exptime`, beginning at line 149
when inspected, states combined complexity for concepts under general
finite TBoxes, finite KBs, subsumption, instance checking, and optional
tested concepts. Its task scope agrees with the sources and with the
explicit local reductions. The local (2^{O(N^2)}) ABox-assignment bound
is not attributed to Donini-Massacci's narrower input. The canonical
interpretation expressly permits distinct names to denote one type,
matching the adopted semantics.

In the annex, lines 148-153 use Corollary 3.6 to choose a polynomial-space
ATM and immediately pass to the one-tape form. Lines 178-180 cite
Section 2 generally; lines 189-190 assert that the chosen bound agrees
with the machine on its actual computations. Make the stronger source
normalization explicit by inserting this after the machine is chosen
and before the one-tape simulation:

```latex
Choose a space-constructible polynomial bound large enough for the
machine and at least the input length.  By
\cite[Theorems~2.5 and~2.6(b), pp.~120--122]{ChandraKozenStockmeyer1981},
we may choose an equivalent machine with no negating states whose
reachable configurations all obey that bound and whose computation
paths all terminate.  Increase the polynomial bound as needed for
the following tape and branching simulations.
```

With this sentence, the subsequent tape-boundary convention is fully
aligned with the stronger chosen machine model. Alternatively, one
could work only with accepting trees inside a space bound and prove
that rejecting excursions preserves acceptance, but the cited
Theorem 2.6(b) already supplies the cleaner route.

No other source-scope defect was found in the read body/annex. This
does not claim a second full independent audit of every transition
GCI or complexity-counting lemma; this task checks source statements,
normalization assumptions, and their use in the actual insertion.

## 5. Suggested reader-facing attribution paragraph

After the combined-complexity theorem or after its explanatory paragraph
at the end of the new body file, the following is source-accurate:

```latex
The concept/general-TBox classification is stated in
\cite[Theorem~6, p.~26 of the author draft]{BaaderHorrocksSattler2008}.
Donini and Massacci give a tableau procedure whose prescribed search
strategy runs in single deterministic exponential time in the combined
size of the concept and TBox
\cite[Theorem~3.13, p.~98; Theorem~6.17, p.~123]{DoniniMassacci2000}.
Here the finite-type construction proves the upper bound for the full
input convention, and Annex~\ref{annex:p9.alc.3} proves the lower bound
from the alternating-space characterization
\cite[Corollary~3.6, p.~122]{ChandraKozenStockmeyer1981}.
```

The language does not claim that either acquired DL source contains
the exact local type construction or binary countdown reduction.
There is no need to put a history of missing-source access in the
reader-facing paragraph.

## Limits and file changes

The exact 2017 textbook chapters remain unacquired; no acquisition
search for them was repeated. Existing lecture slides are a distinct
source. No other agent's review result was consulted. Only this note
was authored; no manuscript files, tests, builds, or renders were
changed or run.
