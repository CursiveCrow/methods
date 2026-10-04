# P17-D5: single-peaked majority and median peaks

Date: 8 September 2026. Author block began at 06:53 UTC, with a
07:38 UTC deadline. The bounded author draft is complete in the two files
below. Independent review, root integration, production and admission
remain required; this note does not close P17-D5.

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p17/single-peaked-majority.tex` | 309 | 15554 | `BA7EF43E3E28026890EE178439A32CF13614D6E430CF916350FEFC479D423063` |
| `handbook/annex/p17/single-peaked-majority.tex` | 404 | 21295 | `1AA78E18617B8DE56578E7DA915F5A02F276FEA09737A21811EB21705E3AC3E0` |

Only those two new LaTeX files and this note were edited in this block.
The complete saved body and annex were read, and final changed definitions
were reread after their corrections. No manuscript rendering or build was
run, and no tests or shared-file edits were made.

## Exact source and reading

Ariel Rubinstein, *Lecture Notes in Microeconomic Theory: The Economic
Agent*, second edition, author revision last updated 11 January 2015.
Held file:
`source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf`.
Its SHA-256 was reverified as
`F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8`;
it has 172 physical pages and 1,431,428 bytes. The title, edition and
revision-date pages, physical pages 1--3, were personally read as text.
Use the existing `Rubinstein2015LectureNotes` bibliography key.

The source target was frozen before writing as Lecture 9 Problem 2,
printed page 128, physical page 142, with the full Lecture 9 context on
printed pages 122--128, physical pages 136--142. All seven complete pages
were personally read as extracted text and source page images. The source
reading images remain in the task workspace under
`tmp/pdfs/p17-single-peaked-source/page-136.png` through `page-142.png`.
These are source-reading evidence, not manuscript production evidence.

The exact problem uses X=[0,1] and the condition that if
`a_i^* >= b > c` or `c > b >= a_i^*`, then b is strictly preferred to c.
Lecture 9's basic domain on printed page 123 supplies strict individual
orderings and permits weak social output. The adjacent Problem 1
explicitly changes to weak individual inputs for its separate binary
result; that convention is not imported into Problem 2 here.
The new body retains the interval regime and explicitly identifies
`p_i` with the source's peak `a_i^*`.

The source states the odd-electorate conclusion as an exercise and does
not print its proof. The supplied proofs, ordered-set generalization,
median refinements, finite procedure and counterexamples are independently
written handbook deductions, with that attribution boundary stated in
the body. No continuity, utility representation or cross-side distance
assumption is added to the source theorem.

## Actual prerequisite interface

The complete current `social-choice.tex` body and annex were read, with
particular attention to strict orderings, weak social output, pair counts,
IIA, Pareto, dictatorship and the unrestricted-domain premise in Arrow's
proof. The finite-preference weak/strict/indifference definitions were
also read directly. Frozen prerequisite identities:

| File | SHA-256 |
| --- | --- |
| `handbook/parts/p17/social-choice.tex` | `224340F36A0774478ED6CFD8713601190B23F97BE7950106DD4CD8F8B71E64FA` |
| `handbook/annex/p17/social-choice.tex` | `C76738A8942F81BD5BF37E3701A30820AD24992E5B3805EC448CD9D883D69E6F` |
| `handbook/parts/p17/finite-preferences.tex` | `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C` |
| `handbook/annex/p17/finite-preferences.tex` | `B141A371731E7A0A3BEFF1C88C839F98720BE4F894A2D475CAF098A61159202C` |

The contract and conventions remain at hashes
`C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3`
and `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242`.
The conventions were reread in this block. The relevant P17-D5 assignment
uses the approved plan's bounded authorship and later independent-review
sequence.

## Seven complete statement/proof pairs

Each suffix has body label `thm:p17-<suffix>` and reciprocal proof
label `annex:p17.<suffix>`.

| Suffix | Supplied argument |
| --- | --- |
| `single-peaked-structure` | Unique greatest peak, four allowable restrictions to any axis-ordered triple, converse with an explicitly existing greatest alternative, and the finite greatest-element argument. |
| `single-peaked-majority` | Odd counts give exactly one direction per distinct pair. The two voter-set inclusions exclude both possible directed three-cycle orientations. Failure of full transitivity would create one of those cycles. Reflexive closure is checked separately. Works on the whole source interval and on the stated ordered-set extension. |
| `median-peak-winner` | Two coalitions of at least k+1 voters show that the median peak defeats every rival; unique strict and weak winner, greatest social alternative, and single-peakedness of the whole already-proved social ordering. Repeated peaks, endpoints, one voter and singleton sets are included. |
| `even-median-interval` | Exact weak-winner set between the two central peaks; alternatives outside lose strictly to a central peak. A strict winner exists exactly when those peaks coincide. No even-electorate transitivity assertion is made. |
| `single-peaked-algorithm` | Validates finite strict-ranking encodings; adjacent rank inequalities are necessary and sufficient on a supplied axis; failure witnesses, median histogram and full ranking are proved correct. Explicit random-access model, O(nq) validation, O(n+q) central-peak extraction and exactly nq(q-1)/2 individual comparisons for the full matrix. |
| `single-peaked-boundaries` | All ten pair counts in the five-voter profile, majority ranking differing from the median-peak voter's full ranking, the three-voter cycle outside the restricted domain, and the four-voter social-tie counterexample. An explicit strict distance ordering with a numerical tie-break realizes the parity failure on the full interval. |
| `single-peaked-arrow` | Pareto, anonymity, restricted-domain IIA, an admissible refuting profile for each proposed dictator, a concrete strict interval ordering excluded from the domain, and the precise unrestricted-domain premise absent from Arrow's theorem. |

The finite example's majority order is c>b>d>a>e, while voter 3's
ordering is c>b>d>e>a. Its median peak is c. The four-voter parity example
has x tied with y and z, while y defeats z by 3--1, giving
z weakly above x weakly above y but not z weakly above y. On the full
interval the same failure occurs at x=0, y=1/2, z=1, using peaks
0,0,1/2,1 and the explicitly proved strict tie-break convention.

## Root routes and notation

The current P17 driver has five chapters ending in `social-choice.tex`.
Append `parts/p17/single-peaked-majority` after that predecessor and append
the matching annex after its predecessor in `handbook/annex/p17.tex`.
This is candidate chapter scope P17.6 at the observed driver. The root
owns these shared route changes and any final scope reconciliation.

The predecessor's `def:p17-social-choice-next` still lists restricted
domains/median voters and Problems 2--5 as remaining work. After this unit's
relevant acceptance, replace the completed Problem 2 portion with an actual
forward reference to this chapter while retaining the other owed regimes
and Problems 3--5. No author update to that shared predecessor was made.

Reconcile these notation contributions into the root's canonical registry;
extend compatible existing social-choice rows where appropriate:

| Glyphs | Type and scope in the new chapter |
| --- | --- |
| `X,\leq,<` | Nonempty alternative set and fixed common linear axis, with source instance [0,1]. Axis comparison is distinct from voter preference. |
| `p_i,a_i^*` | Individual peak and the explicitly identified source alias. |
| `\mathcal L_{\mathrm{SP}}(X,\leq),\mathcal D_{\mathrm{SP}}` | Admissible strict-order set and restricted profile domain. |
| `N,n,k` | Finite electorate, its positive size and the parity parameter. |
| `V_P(x,y),\succ^M_P,\succeq^M_P,\sim^M_P` | Existing pair counts and majority comparisons, retaining the source predecessor's strict-input tie convention. |
| `F_{\mathrm{SP}}` | Social welfare function whose domain is the declared restricted set. |
| `p_{(j)},m,l,u,[l,u]_X` | Sorted peak occurrences, odd median, even central peaks and their interval within X. Sorted positions are not voter identities. |
| `q,a_j,r_i(j),h_i` | Finite axis size, indexed alternatives, rank arrays and top-alternative indices in the supplied-axis procedure. |
| `w` | Candidate strict or weak Condorcet winner in the median arguments. |
| `|t-p|` | Real absolute distance, used only to construct the strict interval parity example; it is not an assumption of the main theorem or cardinality notation. |

## Bounded verification and remaining work

The existing `tools/check.py` scanner reports no scoped findings on the
new pair: seven statuses, seven reciprocal annex items, no duplicate new
labels, and the existing bibliography key resolves. At the check, the
shared bibliography had 640 entries and zero intake stubs. New references
were checked against the two new files plus the actual social-choice and
finite-preference pairs: none is missing and none of the new labels is
duplicated there. These checks are not whole-book or formal-admission claims.

The assigned source result and stated deductions are supplied. Remaining
separate treatments include finding a common axis, weak individual ties,
other preference restrictions, multidimensional domains and strategic
misreporting. A median-winner theorem is not used to assert strategy-proofness.
Root integration, canonical notation and the three independent text roles
are the next actions for this frozen candidate.

## Root notation correction and predecessor connection

The publication reader identified real absolute-distance bars in the handbook's
own interval counterexample, conflicting with the cardinality-only house rule.
Root replaced them by the explicitly defined function d_p(t)=max(t-p,p-t),
with both same-side formulas proved before invoking strict movement toward p.
The original strict tie-break and the entire interval counterexample remain.
The body is unchanged at BA7EF43E3E28026890EE178439A32CF13614D6E430CF916350FEFC479D423063.
The revised annex is 408 lines at
5DDA4E25ADEF9987B45CE7050836D5BB2BEC11D9A55959FBDE460B8CEDE25E89.
The exact original annex is preserved in
tmp/edition-2026-bounded-kamp4-probability-decision/kamp8-median/before/median-annex.tex.
The notation intake's old absolute-distance row is superseded by d_p(t).

The predecessor social-choice body has only its last scope paragraph changed:
it now points to the completed Problem 2 chapter and retains Problems 3-5 as
separate work. Its current 323-line hash is
83E82EB6AF1353725E3D48799390AD9F4F3CAFCF566E694514C0D1AC2E5CCDCB.
The original 224340F3 snapshot is in the same before folder as social-body.tex.
These exact deltas are included in the affected independent review addenda;
this root note is not itself their acceptance.
