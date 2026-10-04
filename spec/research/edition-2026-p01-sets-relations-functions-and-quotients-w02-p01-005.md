# w02-p01-005 research note: P1 section 2.1 set operations

Packet: `work/waves/w02/packets/w02-p01-005.json` (P1, chapter 2, section 2.1,
label_tag `p01-w02-p01-005`, heading level `\section`).

## Sources opened in this session

- `source/formal-logic-reference.tex` (Version 1.0, held; packet held path).
  Lines read and used as locators:
  - 363--371: Part ``Foundations of Formal Work'', chapter ``Sets, Relations,
    Functions, and Cardinality'' opening (ambient classical set theory in the
    metalanguage; no informal collection is a set without licence).
  - 373--404: section ``Sets and classes'' (Subset 376--382, Power set
    384--389, Class 391--394, paragraph 396--398, warning 400--404).
  - 10060--10064: Part ``Axiomatic Set Theory'', chapter ``The Axioms of ZF
    and ZFC''.
  - 10076--10082: `\Lang_{\in}=\set{\in}`, equality logical identity, `\in`
    binary relation symbol.
  - 10089--10165: section ``The language and the axiom schemas'': convention
    Classes 10092--10101, Extensionality 10103--10110, Empty set
    10112--10118, Pairing, union, and power set 10120--10141, Infinity
    10143--10153 (uses `x\cup\set{x}` undefined at 10144), Separation schema
    10155--10165.
  - 10188--10201: definition of omega by separation from an inductive set.
  - 10335--10339: warning ``Unrestricted comprehension''.
  - 16306--16317: chapter ``Exercise Feedback'', section ``Set theory and
    forcing'', solution sketch to ex:zf-zfc-01 (product bounded inside the
    double power set of `a\cup b`).
- No external set-theory textbook is held (searched
  `spec/coverage/edition-2026/held-sources.json` for Jech, Kunen, Enderton,
  Halmos, Zermelo, Levy, Suppes and similar; only Fraenkel 1922 and Cantor 1897
  appear, neither used). The new text therefore cites only the frozen
  manuscript, and the bib note states that definitions of binary union,
  intersection, difference and intersection of a nonempty set, the lemmas,
  laws and proofs are editorial completions from the manuscript's axioms.

## Existing treatment search (A9)

- Listed: `handbook/restoration/inherited-00373-00405.tex` (sec:set-prerequisites-01):
  subset, power set, class, warning. Kept as is; new section cites it.
- Found, not listed:
  - `handbook/restoration/inherited-10089-10271.tex` (sec:zf-zfc-01, on the
    P6 route via scope-SRC-10089-10271): axioms only; new section cites it for
    the axioms and supplies the derived operations.
  - `handbook/parts/p01/boolean-prime-ideal-and-ultrafilters.tex`
    def:p01-bpi-boolean-algebra and def:p01-bpi-filter-ideal use
    `\mathcal P(S)` with `\cap,\cup,S\setminus A` as a Boolean algebra without
    proof; the new corollary proves those laws and links there.
  - `handbook/parts/p01/equivalence-closure-and-quotients.tex` line 52 uses
    separation from `X\times X` and `\bigcap\mathcal F`; same roles.
  - `handbook/parts/p01/mathematical-preliminaries.tex` (not on the p01 driver
    route): register table with subset/power set/class rows; no union,
    intersection or difference rows. Not cited (off route).
- No P1 treatment of binary union, intersection, difference, separation
  notation `\{x\in A:P(x)\}`, or the no-universal-set results was found.

## Decisions

- Source macros `\set`, `\Pow`, `\tuple` are guarded outside restoration;
  the new files use `\{\}`, `\mathcal P` and `\langle\rangle`.
- Membership is stated as the one primitive nonlogical relation of
  `\Lang_{\in}` (source 10076--10082) and the chapter's ambient theory is the
  manuscript's ZF axiom block taken in the metalanguage (source 363--371 says
  only ``ordinary classical set theory''; the identification of the axioms
  used is stated explicitly in the reader text as the axioms invoked, each
  named where used).
- Product existence is proved as a lemma (bounding set
  `\mathcal P(\mathcal P(A\cup B))`) following the manuscript's exercise
  solution architecture, written as a full proof; needed for the Boolean
  algebra corollary's operation graphs.
- Placement: packet proposal is after `restoration/scope-SRC-00507-00532`.
  The return also records the alternative of placing the section directly
  after `restoration/scope-SRC-00373-00405` (adjacent to the subset/power set
  section it extends); the lead decides.

## Continuation

Block 2 (4 October 2026). Assessment disputes for 2.1: the owned body and annex
files are not input by any driver, so their content (membership as primitive,
set operations, bounded formation with existence and uniqueness) is inactive.
Actions this block:
- Added def:p01-w02-p01-005-existence-principles (body lines 67-98): the six
  principles displayed in the source's own notation from source lines
  10103-10165 (definitions Extensionality, Empty set, Pairing/union/power set,
  Separation schema), so extensionality and separation are stated as
  principles, not only cited.
- Filed patch requests `work/waves/w02/patches/w02-p01-005.json`: insert the
  body input after `\input{restoration/scope-SRC-00507-00532}` in
  handbook/parts/p01.tex (packet proposal; alternative after
  scope-SRC-00373-00405 noted) and the annex input after the
  `\hbannexchapter{1}...\label{annex:p01}` line of handbook/annex/p01-route.tex.
  Section-level credit is blocked_policy until the lead applies both.
- Hard-guard G1 items (spec/research/...-w02-p02-044*, -045*, -054*) are not
  files of this packet: the 044/045 notes are headed by their own packets and
  the 054 paths do not exist in the tree; nothing was changed there.
Checks: unit-compile ok (3 overfull); fused-space no hits; check.py filtered:
only bib-key for the own intake key.
