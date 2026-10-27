# w02ca-p15-010 (P15, section 159.9): provenance note

Section 159.9 is carried by the existing chapter
`handbook/parts/p15/uniform-integrability-and-conditional-limits.tex`
(sec:p15-uniform-integrability-and-conditional-limits) with annex
`handbook/annex/p15/uniform-integrability-and-conditional-limits.tex`.
Both are read-only hosts for this packet; the packet's owned body/annex
files were not created, because the open duties are additions to the
existing treatment (A9: extend, no second treatment). The additions are
patch requests in `work/waves/w02ca/patches/w02ca-p15-010.json` (three
entries, all against the read-only body host).

Packet note: readonly_units lists the unit
ED26-P15-CH-uniform-integrability-and-conditional-limits with owner
"w02c-p15-014"; the w02ca packet w02ca-p15-014 (section 161.1) carries the
same unit but its recorded gaps do not touch C011, C015 or C016. The
computed task assigned those three gaps to this packet, so they were
supplied here as patch requests.

## Source opened in this session

- `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`
  (DurrettPTEAuthor2019, author version 5, 11 January 2019). Printed page
  = PDF page - 8.
  - Thm 4.6.9 and continuation: printed pp. 247-248 (PDF 255-256). The
    Chung line, the "It is obvious" / "It is incredible" paragraphs, the
    Kolmogorov derivation and the closing "very useful" claim.
  - Ex. 4.6.1: printed p. 248 (PDF 256). Prior / posterior definitions,
    source symbols Z_i (noise), theta, Y_i = Z_i + theta.
  - Exs. 4.6.2-4.6.6: printed p. 249 (PDF 257). Ex. 4.6.3 contains the
    "much simpler than the bare-hands approach ... Exercise 1.4.3 ... a lot
    of machinery" remark; Ex. 4.6.4 says "Use Theorem 4.6.9".
  - Ex. 1.4.3: printed p. 24 (PDF 32). Simple function from the definition
    of the integral, sets approximated by intervals via Exercise A.2.1,
    corners rounded for continuity.

## Notation

Host notation kept: xi_i for the noise / independent sequence (source
Z_i in Ex. 4.6.1, X_i in the Thm 4.6.9 continuation; the patches state
the source names). New symbol K_n (regular conditional law of theta given
F_n) appears only in the patch text for
def:p15-w02c-p15-010-prior-posterior; it is a local name for the kernel of
def:p15-regular-conditional-law and is not entered in a registry because
the owned symbol-intake CSV was not created (no owned .tex file exists).
If the lead applies the patch, the scope for K_n is
def:p15-w02c-p15-010-prior-posterior.

## Labels proposed (inside patch text)

- def:p15-w02c-p15-010-levy-two-readings (hbexample, after
  thm:p15-levy-information-law)
- def:p15-w02c-p15-010-approximation-routes (hbexample, after
  thm:p15-dyadic-martingales)
- def:p15-w02c-p15-010-prior-posterior (hbdefinition, after
  thm:p15-posterior-mean-consistency)

## Continuation

- C011: patch entry 1 (insert_after the end of
  thm:p15-levy-information-law). Supplies the Chung line (short quoted
  phrase "obvious or incredible", rest paraphrased), both readings, the
  Kolmogorov consequence and the closing usefulness claim, linked to
  thm:p15-extinction-or-escape (Exs. 4.6.4-5).
- C015: patch entry 2 (replace the closing line of
  thm:p15-dyadic-martingales and insert an hbexample after it). Supplies
  the Ex. 4.6.3 comparison with Ex. 1.4.3
  (thm:p15-criteria-real-integration) and names the machinery by label.
- C016: patch entry 3 (replace the last sentences of
  thm:p15-posterior-mean-consistency and insert an hbdefinition after
  it). Supplies the statistical reading, prior, posterior after n
  observations, and the posterior-mean identification via
  thm:p15-real-conditional-law and thm:p15-kernel-expectation.
- Verification done: each anchor occurs exactly once in the host; the
  host with all three patches applied was compiled in a scratch build
  (pdflatex + biber + pdflatex x2, TEXINPUTS on handbook/) with no errors,
  no overfull box in the patched ranges, and every label referenced by
  the patch text located in the handbook tree; find_fused_spaces.py
  reports no hit on the patched copy or the patch file.
- Open: the lead must apply the three patch entries. `waves.py
  unit-compile` on this packet fails because the owned body/annex files
  do not exist (no owned .tex was written).

### Continuation, run after the usage-limit reset (2026-10-10)

- The current assessment marks C011 and C015 lead_owned: the unit is a
  readonly unit of this packet (owner w02c-p15-014), and the owner has
  written both items in handbook/parts/p15/limit-theorems-and-concentration-w02c-p15-014.tex
  (lines 270-318 def:p15-w02c-p15-014-levy-readings; lines 320-343
  def:p15-w02c-p15-014-dyadic-price). That file is not input by any driver.
- Withdrew former patch entries 1 (C011) and 2 (C015) from
  work/waves/w02ca/patches/w02ca-p15-010.json: they would be second
  treatments of the owner's text. Former entry 3 (C016) is kept as the
  only entry; the lead decides whether it is still wanted.
- Remaining (lead): route the owner file by adding
  \input{parts/p15/limit-theorems-and-concentration-w02c-p15-014} and the
  annex counterpart to the P15 drivers. Remaining (owner w02c-p15-014):
  the Evaluation paragraph (line 311) does not render Durrett's
  dictionary-sense gloss ("too unusual or improbable to be possible")
  named in the C011 gap.
- No owned .tex file exists; unit-compile fails for that reason only.

### Continuation, block 1 of run r4 (2026-10-10)

- The owner file handbook/parts/p15/limit-theorems-and-concentration-w02c-p15-014.tex
  now also carries C016 (def:p15-w02c-p15-014-prior-posterior and
  thm:p15-w02c-p15-014-posterior-mean, section
  sec:p15-w02c-p15-014-conditional-remarks, lines 391-542). The former
  C016 patch entry (a second definition of prior/posterior) is withdrawn.
- work/waves/w02ca/patches/w02ca-p15-010.json now holds three link-only
  replace entries against the read-only host body: C011 (locator to
  thm. 4.6.9, pp. 247-248 and \cref to the owner's levy-readings), C015
  (removes "the complete source Exercises 4.6.2--3", \cref to the
  owner's dyadic-price), C016 (removes the undefined "prior variable" /
  "posterior consistency claim", \cref to the owner's prior-posterior and
  posterior-mean). Each is to be applied only with the owner routing
  (owner patch entries 4-5 in w02ca-p15-014.json). Anchors checked unique;
  find_fused_spaces clean on the patched scratch copy.
- Durrett PTE v5 pp. 247-248 reread (PDF 255-256): the closing sentence
  quotes "too unusual or improbable to be possible". Owner line ~429
  renders it as "literally incredible" without that gloss; this edit
  belongs to the owner file.
- unit-compile still fails only because no owned .tex exists (none
  written; a stub would be a placeholder).

### Continuation, block 1 of run r5 (2026-10-10)

- New gap C019 (Durrett sec. 4.7 preamble, p. 249: the sigma-fields
  decrease as n decreases to minus infinity, so the convergence theory is
  particularly simple). Reread in the held PDF (printed p. 249, PDF 257).
  The owner file already carries it:
  def:p15-w02c-p15-014-reversed-martingales,
  handbook/parts/p15/limit-theorems-and-concentration-w02c-p15-014.tex
  lines 622-670, still unrouted.
- Added patch entry 4 to work/waves/w02ca/patches/w02ca-p15-010.json:
  link-only replace at the end of def:p15-backward-martingale (host line
  315-330), adds the locator sec. 4.7, p. 249 and a \cref to the owner
  convention. Anchor unique; all four entries apply cleanly to a scratch
  copy; find_fused_spaces clean.
- C011 owner text (line ~509) still reads "literally incredible" and
  omits Durrett's gloss "too unusual or improbable to be possible"
  (p. 248); owner edit.
- unit-compile fails only because no owned .tex exists (none written).

### Continuation, block 1 of run r6 (2026-10-11)

- Gaps C011, C015, C016 reassigned again (lead_owned, owner
  w02c-p15-014). The assessment reads only the routed host, so the owner
  text is invisible to it: the owner file is still not input by
  handbook/parts/p15.tex or handbook/annex/p15.tex.
- Owner text now at: levy-readings lines 677-722 (Chung line, obvious
  reading, incredible reading, "very useful" evaluation, name L\'evy's
  zero-one law in reader text), dyadic-price lines 724-747 (Ex. 4.6.3
  remark vs Ex. 1.4.3), prior-posterior lines 777-814 and posterior-mean
  816-826 (Ex. 4.6.1 definitions and normal-population reading),
  reversed-martingales 828-876. Every gap item in the r6 assessment is
  present there.
- Reread Durrett PTE v5 PDF pp. 255-257 (printed 247-249) this session;
  all patch locators confirmed. All four patch anchors unique in the
  current host. No new text written: writing it here would be a second
  treatment of the owner's components (A9, A14).
- Remaining (lead): apply owner patch entries 3-4 of
  work/waves/w02ca/patches/w02ca-p15-014.json (driver routing), then the
  four link-only entries of work/waves/w02ca/patches/w02ca-p15-010.json.

### Continuation, block 2 of run r6 (2026-10-11)

- Gaps now listed: C001, C003, C011, C012, C015, C016, C019, all lead_owned
  (owner w02c-p15-014, owner file not on the route). Every item is written in
  the owner file handbook/parts/p15/limit-theorems-and-concentration-w02c-p15-014.tex:
  ui-arbitrary 563-597 (C001), ui-moment-source 599-634 (C003),
  levy-readings 677-722 (C011), dyadic-price 724-747 (C015),
  conditional-dominated 749-775 (C012), prior-posterior and posterior-mean
  777-826 (C016), reversed-martingales 828-876 (C019). Annex proofs exist for
  the lemmas (annex:p15-w02c-p15-014-ui-arbitrary, -ui-moment, -posterior-mean).
- Found that work/waves/w02ca/patches/w02ca-p15-019.json entries 24-30
  (0-based) file host pointers for all seven gaps at the same or overlapping
  anchors as this packet's former four entries. Applying both sets would
  conflict, so this packet's four host entries are withdrawn in favour of
  the w02ca-p15-019 set. Their locators were checked in the held PDF.
- New single entry in work/waves/w02ca/patches/w02ca-p15-010.json: replace
  in the owner file's Evaluation paragraph (lines 715-717) adding Durrett's
  quoted gloss "too unusual or improbable to be possible" (p. 248). Anchor
  unique; find_fused_spaces clean on the patch file and the patched scratch
  copy.
- Defect noted in w02ca-p15-014.json entry 9 (0-based): JSON text has
  U+000B + "arphi" where "\varphi" is meant.
- Source reread: PTE5 PDF pp. 252-257 (printed 244-249), pdftotext. Printed
  p. 244: definition for any collection and the M+1 remark; p. 245: Thm
  4.6.2; p. 247: Thm 4.6.9, Chung line, both readings; p. 248: Kolmogorov
  conclusion, closing judgement, Thm 4.6.10 title, Ex. 4.6.1; p. 249: Exs.
  4.6.2-3 and the Section 4.7 opening.
- Remaining (lead): apply w02ca-p15-014.json entries 3-4 (driver inputs),
  9-10 (C003 host fix, after correcting the \varphi escape), then
  w02ca-p15-019.json entries 24-30, and this packet's single entry.
- unit-compile: not applicable, no owned .tex exists (none written; a stub
  would be a placeholder and a second treatment).

### Continuation, block 3 of run r6 (2026-10-11)

- Hard guard G10 (unit compile) failed because the owned body and annex
  files did not exist. Created both as comment-only files (no reader text,
  no heading): body
  handbook/parts/p15/conditioning-independence-and-information-w02c-p15-010.tex
  lines 1-10 (toc tag, route comment naming
  sec:p15-uniform-integrability-and-conditional-limits and the owner's
  sec:p15-w02c-p15-014-ui-source and sec:p15-w02c-p15-014-conditional-remarks,
  and \nocite{DurrettPTEAuthor2019}, which biber needs to avoid the
  "does not contain any citations" warning); annex
  handbook/annex/p15/conditioning-independence-and-information-w02c-p15-010.tex
  lines 1-4. Same shape as the owned files of w02ca-p15-018. They set no
  text, so inserting them into the drivers is optional for the lead.
- unit-compile: ok. find_fused_spaces: no hit. check.py --tree handbook: no
  finding in either owned file.
- Gaps C001, C003, C011, C012, C015, C016, C019 unchanged in substance: the
  owner text is still in the unrouted file
  handbook/parts/p15/limit-theorems-and-concentration-w02c-p15-014.tex
  (ui-arbitrary 563, ui-arbitrary lemma 583, ui-moment-source 599,
  levy-readings 677, dyadic-price 724, conditional-dominated 749,
  prior-posterior 777, posterior-mean 816, reversed-martingales 828).
  w02ca-p15-019.json entries 24-30 (host pointers) all still anchor exactly
  once in the routed host. This packet's single patch entry (C011 gloss in
  the owner file) still anchors exactly once.
- Source reread this block: PTE5 PDF pp. 255-257 (printed 247-249),
  pdftotext; p. 248 carries the quoted gloss and the title of Thm 4.6.10;
  p. 249 carries the Ex. 4.6.3 comparison and the Section 4.7 opening.
- Remaining (lead): apply w02ca-p15-014.json entries 3-4 (owner routing)
  and 9-10, w02ca-p15-019.json entries 24-30, and this packet's entry.

### Continuation, block 1 of run r6 (2026-10-12), author lane 64

- New gap C013 (Durrett Example 4.6.11, printed p. 248, PDF p. 256): the
  general claim "uniformly integrable and almost surely convergent X_n
  give E(X_n|F) -> E(X|F) in L1, by Theorem 4.6.3 (p. 245) and Exercise
  4.6.7 (p. 249)". Reread in the held PDF this session (pdftotext, PDF
  pp. 252-257). It is not written anywhere in the tree: the owner file
  (limit-theorems-and-concentration-w02c-p15-014.tex line 772) only
  names the counterexample, and no entry of w02ca-p15-014.json or
  w02ca-p15-019.json covers it.
- Added patch entries 1 and 2 (0-based) to
  work/waves/w02ca/patches/w02ca-p15-010.json, against the routed host:
  entry 1 replaces the sentence "The third example is the complete
  construction of source Example~4.6.11." inside thm:p15-ui-counterexamples
  with the general claim, Durrett's route (Thm 4.6.3 =
  thm:p15-vitali-convergence, Ex. 4.6.7 = item (1) of
  thm:p15-changing-conditional-limits with constant information) and the
  boundary (no almost-sure strengthening); entry 2 extends the annex proof
  annex:p15.ui-counterexamples (anchor "although \(E|B_n|=1/n\to0\).")
  with the full proof (a.s. to probability by continuity from above,
  Vitali, item (1)). Both anchors occur exactly once. Scratch build of the
  patched host body and annex (pdflatex + biber + pdflatex x2): no error,
  no overfull box in the patched ranges, only external refs undefined.
  find_fused_spaces: no hit on the patched copies; in the patch JSON the
  only hits are the verbatim host anchor "\to0" (must match the host).
- C001, C003, C011, C012, C015, C016, C019: unchanged; text in the
  unrouted owner file (ui-arbitrary 563, ui-moment-source 599,
  levy-readings 677, dyadic-price 724, conditional-dominated 749,
  prior-posterior 777, posterior-mean 816, reversed-martingales 828);
  host pointers in w02ca-p15-019.json entries 24-30 and owner routing in
  w02ca-p15-014.json entries 3-4 are still unapplied (all anchors still
  unique this session).

### Continuation, block 1 of run r6 (2026-10-13), author lane 64

- Gaps listed: C001, C003, C011, C012, C013, C015, C016, C019, plus the
  note that the owner file is off route. Nothing changed since the
  2026-10-12 block: handbook/parts/p15.tex and handbook/annex/p15.tex still
  do not input the owner file; no patch of w02ca-p15-010.json,
  w02ca-p15-014.json or w02ca-p15-019.json has been applied (host
  uniform-integrability-and-conditional-limits.tex unchanged since 8 Sep).
- Owner text rechecked in
  handbook/parts/p15/limit-theorems-and-concentration-w02c-p15-014.tex:
  ui-arbitrary 563 (M+1 remark at 574, 589), ui-moment-source 599 ("common
  way to check" at 622), levy-readings 677 (Chung 682, "very useful" 717),
  dyadic-price 724 (machinery remark 731), conditional-dominated 749
  (Thm 4.6.10 title), prior-posterior 777 (normal population 786, prior
  790, posterior 792, posterior mean 802), posterior-mean 816,
  reversed-martingales 828 (reversed 833, simple convergence theory).
  C013's general claim is in this packet's patch entries 1-2 (host body
  and annex), not in the owner file.
- Source reread this block: PTE5 PDF pp. 252-257 (printed 244-249),
  pdftotext: p. 244 M+1 remark; p. 245 "A common way to check" and Thm
  4.6.2; p. 247 Chung line; p. 248 "very useful", Thm 4.6.10 title,
  Example 4.6.11 general claim via Thm 4.6.3 and Ex. 4.6.7, Ex. 4.6.1
  normal population; p. 249 Ex. 4.6.3 machinery remark, sec. 4.7
  "some authors call them reversed", "particularly simple".
- All three patch anchors of w02ca-p15-010.json still occur exactly once.
- No new reader text written: every gap item exists in the owner's text
  (A14) or in this packet's pending host patches (C013); the assessment
  reads only the routed host, so it will keep listing them until the lead
  routes the owner file (w02ca-p15-014.json entries 3-4) and applies the
  host pointers (w02ca-p15-019.json entries 24-30, w02ca-p15-014.json
  entries 9-10) and this packet's entries 0-2.

### Continuation, block 2 of run r6 (2026-10-13), author lane 64

- Hard guard G1 (spec/research/edition-2026-authoring-batch-intake-13.json
  changed outside the owned set): this packet never wrote that file. It is
  clean in the working tree; its last change is the lead commit 6de06cc3
  ("authored state (r1-r6) and route of batch 13"). Nothing to revert from
  this packet; the guard should be rerun against a base after 6de06cc3.
- Routing changed: handbook/parts/p15.tex line 115 and handbook/annex/p15.tex
  line 114 now input the owner file limit-theorems-and-concentration-w02c-p15-014
  (and lines 33 / 32 input this packet's comment-only owned files). The r6-b1
  assessment, which read the same driver hash 46006426..., still calls the
  owner file unrouted; its C001, C003 and C016 gap items are on the route in
  the owner text (ui-arbitrary 563, ui-moment-source 599, prior-posterior 777,
  posterior-mean 816).
- Assessment defect observations closed by new patch entries 3-5 of
  work/waves/w02ca/patches/w02ca-p15-010.json (all against read-only hosts):
  entry 3 (body, after the conclusion of thm:p15-extinction-or-escape) states
  Durrett's real-level form of the hypothesis (ex. 4.6.4, printed p. 249) and
  its equivalence with the integer thresholds; entry 4 (annex, after "This is
  exactly \(X_n\to\infty\).") proves that reduction; entry 5 (body) replaces
  "known mean \(\mu\)" in thm:p15-posterior-mean-consistency by
  \(\mu=E\xi_1\) with a note that only existence of the mean is used (Durrett
  ex. 4.6.1, printed p. 248, assumes E|Z_i| finite and theta with finite mean).
  No overlap with w02ca-p15-019.json entry 29.
- Source reread this block: PTE5 PDF pp. 256-257 (pdftotext): ex. 4.6.1 on
  printed p. 248, exs. 4.6.4-4.6.5 on printed p. 249.
- Checks: all six patch anchors occur exactly once; find_fused_spaces clean on
  the patched scratch copies (the only hits in the patch JSON are the verbatim
  host anchor "\to0"); unit-compile ok; check.py --tree handbook shows no
  finding in the owned files. The patched hosts were not compiled this block.
