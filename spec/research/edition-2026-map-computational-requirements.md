# Computational-logic requirement mapping: N-c-001 through N-c-040

Date: 9 September 2026. This is the finite scope allocation for the forty
original computational-logic requirements. It follows the governing edition
contract, the map-shard contract and the user's clarified CRC-style handbook
of logic and reasoning scope. It adds no general thinking curriculum.

The completed proposal has **40 requirement rows, 136 separate original
source-unit patches and 174 named subcomponents**. Every original requirement
wording, register row, inventory assessment, source ordinal, unit identity and
parent component identity is preserved. Original source-native presentations
remain distinct. Exact but missing bodies are acquisition tasks; unfinished
proofs and manuscript sections are writing tasks. Neither is falsely recorded
as completed by this map.

The handoff is
`spec/coverage/edition-2026/computational-requirements/proposals.jsonl`, SHA-256
`81DD9F79693E920CFA7EE36A75ABD7343DC8B19EDFFC685CAFBB4F7F766D08FA`.
`receipt.json` records the complete-set checks. `goal-profiles.tsv` contains
the forty explicit allocation decisions. `source-allocations.jsonl` exposes
each source ordinal, its exact identity/version, allocated subgoals and source
locator independently of the canonical integration. `identity-additions.json`
contains three previously unbound bibliographic identities. The compiler only
creates this owned proposal set; the requirement integrator owns the canonical
crosswalk and unit JSONLs.

## Evidence read and its limits

The mapper read the edition/map contracts and all forty original goal/source
rows and their preserved current assessments. The original source-candidate
file and actual canonical bibliography supplied the source allocations;
multi-line BibTeX fields were parsed from their literal braced values rather
than trusting null titles in the older extracted candidate cache. No staged
N-c proposal was available in the previous mapper's block3 directory.

Existing source evidence was consulted at the exact requirement and source
subsections of `p09-source-presentations-lot1.md`,
`p09-source-presentations-lot2-3.md`, `p09-source-presentations-lot4.md`, and
the P12 source-accounting/construction packages. The proposals retain those
locators and their distinct source/proof standings. These are existing
acquisition records and source readings, not a claim that this mapper reread
every paper or the entirety of those large notes.

Actual LaTeX supplied the current destination checks and the correction
decisions below. Selected substantive reading included the EL++ opening,
CR6-CR11 and query criterion, marked-run complexity and task reductions;
the TATA version/finite-tree opening; P12 extraction and hammer entries;
Martelli-Montanari and superposition entries; the complete short rewriting
chapter; System F/MLTT statements and boundaries; and the SMT combination
definition and theorem. Current label declarations and source-note headers
were also extracted where needed. `current-destination-receipts.json` pins
the actual files and records this limited reading standing. A byte hash or
label check is not a full mathematical review.

## Source identities resolved in this pass

The original **Paulin-Mohring 1989** extraction attribution is allocated to
the POPL article *Extracting F-omega's Programs from Proofs in the Calculus of
Constructions*, pp. 89-104, DOI 10.1145/75277.75285. The official project
record identifies a realizability interpretation, the informative/logical
distinction and an appendix program. The separate January 1989 thesis remains
a different work; no whole-thesis obligation is inferred from the original
author/year alone. The exact article body still needs qualification before
its source-specific treatment is accepted. [Official Rocq paper record](https://rocq-prover.org/papers/extracting-fs-programs-from-proofs-in-the-calculus-of-constructions),
[ACM article identity](https://doi.org/10.1145/75277.75285).

**Letouzey 2003** is *A New Extraction for Coq*, the TYPES 2002 contribution
published in LNCS 2646 in 2003, pp. 200-219, DOI
10.1007/3-540-39185-1_12. The publisher gives the exact source and publication
date. The author-hosted twenty-page PDF supplies a body lead; its opening and
the distinction between restricted strong reduction and unrestricted weak
evaluation were inspected. This is separate from the 2004 thesis and the
2008 overview already cited by the active manuscript. No source-body equality
with the publisher version or complete new acquisition is claimed.
[Publisher record](https://link.springer.com/chapter/10.1007/3-540-39185-1_12),
[author-hosted paper](https://www.irif.fr/~letouzey/download/extraction2002.pdf).

**Paulson-Blanchette 2010** is the two-author IWIL 2010 Sledgehammer report,
published in EPiC Series in Computing 2 on 15 May 2012, pp. 1-11, DOI
10.29007/36dt. The meeting year accounts for the original 2010 attribution.
The same-title PAAR 2010 contribution is by Paulson alone and was published
as EPiC 9, pp. 1-10, DOI 10.29007/tnfd; it is not silently substituted. The
required pointer explains premise selection, translation, external search
and checked reconstruction rather than attributing kernel truth to a solver's
success token. [Two-author IWIL record](https://easychair.org/publications/paper/wV),
[separate PAAR record](https://easychair.org/publications/paper/Mzp).

## Preserved version and proof distinctions

The source-allocation records retain, among others, the 1995 first edition of
Ebbinghaus-Flum; the 1998 guarded-fragment journal article versus its 1996
preprint; the 2003 Description Logic Handbook first edition; the separate
2005 EL++ conference and report extents; the corrected 1985 Sistla-Clarke
journal versus its 1982 predecessor; the 1988 and 1995 Safra bodies; Büchi's
1959 report versus 1960 journal; Trakhtenbrot's 1961 announcement versus 1962
expansion; the 1981 meeting versus 1982 Clarke-Emerson publication and 2008
authorized reprint; and the 2005 Bradfield-Stirling preprint versus the 2007
published chapter.

Thomas's held **May 1996 Kiel report** cannot establish the separately
registered **1997 chapter, pp. 389-455**. McMillan's held **May 1992 CMU
thesis** cannot establish the revised **1993 Kluwer book, xvii+194 pages**.
The exact source boundaries are explicit acquisition and writing obligations.
The latter distinction is documented in
`spec/research/p09-mcmillan-1993-acquisition-note.md`; Thomas is recorded in
`spec/research/p09-thomas-1996-report-source-note.md`.

The latest existing Thatcher-Wright acquisition note was read. It reports no
acquired exact 1968 article, *Mathematical Systems Theory* 2(1), pp. 57-81,
DOI 10.1007/BF01691346. Its abstract, DOI landing page, 1966 RC1713 lead and
Thatcher dissertation remain different evidence. This mapper made no new
claim of acquisition or of nonexistence of a public copy. See
`spec/research/p09-thatcher-wright-1968-new-leads-2026-09-08.md`.

The active TATA text selects the **18 November 2008 release** against the
register's evolving 2007 attribution. Finite ranked-tree and weak-set
translations remain distinct from Rabin's full infinite-tree setting.

Every source's actual sketch or external referral retains its attributed
standing. That standing cannot remove an independently promised full proof,
an inherited substantive construction or another exact-source obligation.
The finite subcomponents specify the required cases without inventing an
obligation to reconstruct every unrelated chapter of every cited book.

## Actual current deltas and destination corrections

**N-c-010:** The original assessment says the nominal repair is still only
proposed. The actual current `n-c-010.tex` explicitly supplies three
corrections, CR8 feature support, a fresh query nominal, the marked criterion
including inconsistency at disconnected nominals, soundness/countermodel
arguments, and classification by polynomially many marked runs. The proposal
preserves the old assessment verbatim and adds this later delta. It does not
renew independent proof acceptance. The missing expressive-family/2017 book
work remains owed. Source/handbook correction attribution remains explicit.

**N-c-009:** The inventory's `annex:p9.alc.1–.3` is a shorthand, not a
literal label. The mapper bound the three actual declarations: `.1` is in
`handbook/annex/p09/proofs.tex`; `.2` and `.3` are in
`handbook/annex/p09/alc-general-tboxes.tex`. Each actual label was unique.
The original shorthand and original inventory destinations remain preserved.

**N-c-036:** The live superposition completeness entry cites
`BachmairGanzinger2001`; the original row separately requires the 1994
article. The map binds the 2001 treatment as an additional proof dependency
and leaves the original 1994 presentation intact.

**N-c-037:** The live critical-pair definition cites `Huet1973`, whose exact
canonical identity is *The Undecidability of Unification in Third Order
Logic*. That citation requires direct correction in the later writing batch.
The map retains the correct separate Huet 1980 rewriting presentation and the
1973 unification obligation under N-c-035. No manuscript text was edited here.

**N-c-029/030:** System F Church-style and Curry-style checking remain
distinct. The actual MLTT entry explicitly limits its cited
Abel-Coquand-Dybjer result to dependent functions and one Russell universe.
The map preserves that dependency and separately owes the constructor-level
metatheory for the larger selected Pi/Sigma/identity/cumulative-universe
sheet. The narrow result is not credited as proof of the whole calculus.

**N-c-031/038:** The active assistant table names Lean 4.32.1, Rocq 9.1.1
and Isabelle2025-2; other entries have their own product/retrieval boundaries.
The proposals bind versioned documentation as a separate premise role and
require the exact matching official sources before implementation claims are
accepted. The historical architecture sources do not establish these current
version claims, and this map does not infer that their kernels are identical.

## Construction accounting and remaining work

The compiler checked all forty IDs, every original source ordinal and every
parent component mapping, parsed every selected canonical title, verified all
selected actual destination labels, and refused to overwrite a published
proposal. Its only initial failure exposed the ALC shorthand above; it was
resolved against actual files before publication. These are complete-set
mapping checks, not new manuscript tests or independent reviews.

Each patched source unit contains named components with positive/failure
conditions, internal setup and explicit additional dependency roles, existing
destinations and disjoint proposed body/annex/lookup destinations. Proposed
paths identify missing work; they do not create empty manuscript chapters or
require duplicate writing where an exact treatment is already present.

Remaining work is explicit: qualify missing exact-source bodies, finish each
mapped source-specific component and promised proof, repair direct source and
mathematical errors in the authorized writing batch, integrate precise
body/annex/lookup links, and then perform the consolidated independent checks.
The root still owns global source-overlap and prerequisite reconciliation.
This completed forty-row proposal does not establish that the whole coverage
map, manuscript or publication is complete.

No manuscript writing, build, render, test suite, new review wave, commit or
publication occurred. The research skill guided the primary-source identity
checks and this single durable evidence note.
