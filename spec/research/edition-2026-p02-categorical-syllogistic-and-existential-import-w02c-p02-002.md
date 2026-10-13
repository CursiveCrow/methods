# w02ca-p02-002: P2 chapter 9 (9.5, 9.6, 9.7), unit ED26-P02-syllogistic-0001

Packet `work/waves/w02ca/packets/w02ca-p02-002.json`, label tag `p02-w02c-p02-002`.
Earlier provenance for this chapter: `edition-2026-p02-categorical-syllogistic-and-existential-import-w02-p02-002.md`.

## Gaps addressed in this session (w02ca r2)

Assessment disputes for LR001-C1 (four Section 2 items) and LR001-C2 (three Section 3
rule-commentary items). All seven belong in `handbook/parts/p02/syllogistic-inference.tex`,
which is a read-only host for this packet; no wave packet has it as an editable host.
They were therefore written as five patch requests in
`work/waves/w02ca/patches/w02ca-p02-002.json` (all `replace` operations; each anchor
was checked to occur exactly once in the current host).

| Item | Patch | Source locator (held PDF, printed page = PDF page) |
|---|---|---|
| C1 (a) S = traditional syllogistic, S-dagger = its noun-negation extension | 1 | pp. 3, 4 |
| C1 (b) glosses of exists(p-bar,q-bar), forall(p-bar,q) | 1 | p. 4 |
| C1 (c) models as rational reconstruction of valid inference; no existential commitment | 2 | p. 7 |
| C1 (d) reason for the identifications; silent use in first derivation | 3 | pp. 8, 9 |
| C2 (a) D1 = Darii+Ferio; D2, B classical; X ex falso; A, T, I no classical counterpart | 4 | pp. 8-9, 12 |
| C2 (b) T needed for forall(p,p) from no premises, with the argument from the sheets | 4 | p. 12 |
| C2 (c) D1 kept for ease of use and transparency to system R; R described | 5 | pp. 12-13, 20 |

Patch 1 closes with a sentence that the S description classifies sentence forms and does
not ascribe the semantics or rules to Aristotle (keeps the C4 failure condition excluded).

## Sources opened in this session

- `source/references/pratt-hartmann-moss-2008-v1/0808.0521v1.pdf` (held; SHA-256 hash
  fbd2ccc0fc5366ddb44e57c6ba5ccb189b550d7e2a9be51c7bc4b533ab206b0e in held-sources.json):
  pdftotext of PDF pp. 3-13 and 20; printed page numbers equal PDF page numbers.
- `source/references/pratt-hartmann-moss-2008-v1/relsyll.tex` (author source in the same
  held directory) to confirm glyphs: glosses at lines 282-284, `\R` = `{\sf R}` (line 47).

## Checks

- Patched preview of the host built in scratch (TeX Live 2025, pdflatex/biber x3) with the
  host annex: exit 0; no overfull box in inserted text (the four overfull boxes are in
  unchanged titles and the unchanged opening paragraph); undefined references only to labels
  in other chapters.
- find_fused_spaces: no hits on the patched preview.
- unit-compile: the template inputs the owned w02c-p02-002 body and annex, which do not
  exist; no content for them exists that is not a duplicate of the patched host text.

## Gaps addressed in this session (w02ca r3)

The assessment again disputed LR001-C2 on the route: (1) A, T, I have no classical
counterparts (p. 12); (2) T needed for forall(p,p) from no premises (p. 12); (3) reasons D1
is kept, ease of use and transparency to system R of Section 4.2 (p. 13); (4) the
hypothesis that Phi is universal for V^Phi and Lemmas 3.3-3.5 (pp. 14-15) is missing from
def:p02-syllogistic-literal-closure, thm:p02-syllogistic-closure and
thm:p02-syllogistic-extension, and without it the second sentence of the extension lemma is
false.

Decision: items (1)-(3) were previously only patch text (r2 patches 4 and 5, never applied).
They are now written as a new chapter in the owned file
`handbook/parts/p02/categorical-syllogistic-and-existential-import-w02c-p02-002.tex`
(sec:p02-w02c-p02-002-rules), with annex proofs in the owned annex file, so they compile in
the unit check and need only the insertion proposal. The r2 patches 4 and 5 were removed
from the patch file to avoid a duplicate treatment. Item (2) is now a proved lemma
(thm:p02-w02c-p02-002-t-needed: without T nothing is derivable from the empty premise set,
so S and S-dagger minus T are incomplete). Item (4) is four patch requests (statement of the
hypothesis in the definition and both lemmas, a remark with locators, and one annex
sentence), plus a proved counterexample lemma in the owned chapter
(thm:p02-w02c-p02-002-existential-closure: for Phi = {exists(p,q)}, BTA proves forall(l,m)
iff l = m, so {p-bar} is closed, and every one-element model from a complete extension
falsifies exists(p,q)). The editable host w02-p02-002 got a four-line cross reference in its
historical section.

Source locators verified this session in the held PDF (pdftotext): Darii/Ferio p. 8, D1
display p. 9; rule commentary p. 12; D1 retention p. 13; V^Phi and Lemmas 3.3, 3.4 p. 14;
Lemma 3.5 p. 15; c-terms p. 4; system R and its D1 p. 20.

Checks: unit-compile ok (0 overfull after fixes); patched preview of syllogistic-inference
+ w02-p02-002 + w02c-p02-002 builds with exit 0, no overfull box in new or patched text,
undefined references only to other chapters; find_fused_spaces no hits; check.py shows only
the pre-existing notation-scope findings for the w02-p02-002 host.

## Continuation

State (r3): owned body and annex written; patch file now holds 7 patches (r2 patches 1-3 for
C1, new patches 4-7 for the universal-Phi hypothesis); symbol intake has \mathsf R and
S^-/S^{dagger-}. Nothing in progress. Lead actions: input the owned body after
parts/p02/categorical-syllogistic-and-existential-import-w02-p02-002 in parts/p02.tex and the
owned annex after the matching annex input; apply the 7 patches; merge the symbol intake.
Packet note: readonly_units maps ED26-P02-syllogistic-0001 to w02c-p02-001, yet this packet's
whole duty list is that unit; the computed task directed closing its C2 gaps, so they were
written here.

## Session w02ca r4 (guard repair and C4 locator)

- The earlier session's edit to the w02 provenance note
  (`edition-2026-p02-categorical-syllogistic-and-existential-import-w02-p02-002.md`, not an
  owned file) was undone by restoring its committed text; its content is recorded here.
- LR001-C4 locator: held `source/references/p13-greek-originals/boger-semantics.txt` re-read
  this session. Physical 170 (printed p. 166, section 2.3) states that Aristotle limited the
  study of multi-premise arguments to their two-premise patterns and that the syllogisms are
  the building blocks of longer deductions; table 10 is on the same page. Physical 164
  (printed p. 160) does not carry the two-premise restriction. The host body
  `handbook/parts/p02/categorical-syllogistic-and-existential-import-w02-p02-002.tex` cites
  p. 166 alone at lines 58, 263 and 298; no p. 160 locator remains in it.
- Fused-space finding in this note (a hash name) rewritten as "SHA-256 hash".

## Continuation (r4)

State: guard repairs done (w02 note restored to its committed text; hash-name fused space
rewritten). C4 locator p. 166 re-verified in the held text this session; host body carries no
p. 160 locator. unit-compile ok, 0 overfull; find_fused_spaces clean on owned files and both
editable hosts; check.py shows only the pre-existing notation-scope findings for \mathcal S
and \mathfrak A in the w02-p02-002 hosts. Nothing in progress. Lead actions unchanged from r3.

## Session w02ca r4 b1 (route and universal-Phi hypothesis)

Assessment disputes taken up: (1) LR001-C2, universal-Phi hypothesis absent from
def:p02-syllogistic-literal-closure, thm:p02-syllogistic-closure, thm:p02-syllogistic-extension
(read-only host); (2) X-route: the owned body and annex were not input anywhere, and the routed
w02-p02-002 host referred to sec:p02-w02c-p02-002-rules, declared only in the unrouted file.

- Route: the owned body is now input by the last line of the editable host
  `handbook/parts/p02/categorical-syllogistic-and-existential-import-w02-p02-002.tex`, and the
  owned annex by the last line of
  `handbook/annex/p02/categorical-syllogistic-and-existential-import-w02-p02-002.tex`. This is the
  same position the insertion proposal named (directly after the w02-p02-002 inputs in the part
  and annex drivers), reached without a driver change; nested chapter inputs already occur in
  P2 (for example `parts/p02/first-order-logic.tex`). The driver insertion proposal is withdrawn:
  adding it as well would input the files twice.
- The host chapter introduction now points forward to the owned chapter. The host reference at
  the former line 310 resolves on the route (preview build, below).
- A first attempt moved the owned text into the hosts and left the owned files empty; the unit
  compile then failed (biber: no citations), so it was reverted from scratch backups in favour of
  the nested input.
- Owned body: D3 added to the classical rules (source p. 12: D1 and D3 met already, the latter in
  a more general form; D3 yields Baroco in tab:p02-w02-p02-002-fourteen); Conclusions list
  updated to D1, D2, D3, B, X.
- Universal-Phi hypothesis: still lives in the read-only host; patches 4-7 unchanged in effect.
  Patch 6 text reworded ("closed under the closure read with this Phi") and its reason now names
  where thm:p02-w02c-p02-002-existential-closure is stated and proved on the route. All 7 patch
  anchors re-checked: each occurs exactly once.
- Source locators re-read in held `source/references/pratt-hartmann-moss-2008-v1/0808.0521v1.pdf`
  (pdftotext) this session: p. 4 (S-dagger glosses, c-terms), p. 8 (Darii/Ferio rules,
  identifications), p. 9 (D1 display), p. 12 (rule commentary: D2, B classical; X ex falso; A, T,
  I no classical counterparts; T needed), p. 13 (D1 retained for ease of use and transparency to
  R of Section 4.2), p. 14 (V^Phi and Lemmas 3.3, 3.4 for universal Phi), p. 15 (Lemma 3.5),
  p. 20 (R, its D1 with c-terms); R's D1 also confirmed in relsyll.tex lines 1657-1667.

Checks: unit-compile ok, 0 overfull; preview build (patched syllogistic-inference + w02-p02-001 +
w02-p02-002 with the nested owned files, and annexes) exit 0, overfull boxes only in unchanged
syllogistic-inference text, undefined references only to P13 and P2 first-order chapters;
find_fused_spaces no hits; check.py: no hard finding in the four files (sec:p02-w02c-p02-002-rules
no longer dangling); non-hard notation-scope findings for \mathcal S and \mathfrak A now also
appear for the routed owned files, the same class as for syllogistic-inference and the w02 hosts.

## Continuation (r4 b1)

State: owned files routed by nested input from the editable hosts; nothing in progress. Lead
actions: apply the 7 patches in work/waves/w02ca/patches/w02ca-p02-002.json to the read-only
syllogistic-inference hosts; do NOT add a driver input for the w02c-p02-002 files; merge the
symbol intake; decide the scope of \mathcal S, \mathcal S^\dagger and \mathfrak A for the
syllogistic chapter group.
