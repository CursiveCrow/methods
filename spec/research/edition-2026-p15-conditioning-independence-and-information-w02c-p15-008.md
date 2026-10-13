# P15 159.7 / 159.10 — a space without a regular conditional probability (w02ca-p15-008)

## Provenance

- Packet: work/waves/w02ca/packets/w02ca-p15-008.json; label_tag p15-w02c-p15-008.
- Open duty: ED26-P15-CH-regular-conditional-laws-C002 (worked boundary for the claim in
  def:p15-regular-conditional-law, handbook/parts/p15/regular-conditional-laws.tex lines 49-51,
  that a regular conditional probability on (Omega,F_0) needs an existence hypothesis).
- Held source opened this session: source/references/durrett-probability-2019-01-11/PTE5_011119.pdf
  (bib key DurrettPTEAuthor2019). Printed p. 214 = PDF p. 222: definition of r.c.d. and r.c.p.,
  Theorem 4.1.16, the sentence that r.c.d.'s do not always exist, credit to Dieudonne (1948),
  pointers to Doob (1953) p. 624 and Faden (1985), and the accumulation heuristic.
  Printed p. 215 = PDF p. 223: Theorem 4.1.17 (r.c.d.'s exist if (S,S) is nice).
- Dieudonne 1948, Doob 1953 and Faden 1985 are not held (held-sources.json lists only Durrett among
  these). No example is attributed to them. The model written here is a self-contained construction
  (Vitali-type selector for the cosets of Z + sqrt2 Z, the even/odd split of the integer part,
  a Steinhaus-type difference lemma proved from the cover construction of Lebesgue measure,
  and the adjunction of the resulting set to the Borel sets of (0,1) with conditional mass 1/2).
  It carries no source attribution in the reader text.

## Existing treatments found

- Listed in the packet: regular-conditional-laws.tex (body/annex), w02b-p15-008 body/annex
  (def:p15-w02b-p15-008-rcd, thm:p15-w02b-p15-008-ae-counterexample, def:p15-w02b-p15-008-limits
  item 3), conditional-expectation.tex.
- Not listed in the packet: handbook/parts/p15/probability-spaces-and-random-variables-w02c-p15-002.tex
  def:p15-w02c-p15-002-rcd-nonexistence (lines 580-600) and thm:p15-w02c-p15-002-ae-additivity
  (another w02c packet). It states Durrett's non-existence remark and says the example "is not
  reproduced here". The new chapter links to both labels in its Relationships section rather than
  duplicating them.
- thm:p15-w02b-p15-022-presentable item 4 (exchangeability chapter) assumes a non-presentable
  exchangeable law. The new model is not exchangeable and does not supply one; the reader text says so
  (def:p15-w02c-p15-008-limits item 4). That law belongs to the exchangeability unit, not this packet.

## What was written

- Body: handbook/parts/p15/conditioning-independence-and-information-w02c-p15-008.tex
  (chapter sec:p15-w02c-p15-008-no-rcp).
- Annex: handbook/annex/p15/conditioning-independence-and-information-w02c-p15-008.tex
  (five annexitems, all proofs written in full).
- Symbol intake: handbook/registry/symbols-intake-p15-conditioning-independence-and-information-w02c-p15-008.csv.
- No new bibliography keys (only DurrettPTEAuthor2019), so no bib intake file.
- Patch requests: work/waves/w02ca/patches/w02ca-p15-008.json (two insert_after pointers: one in
  def:p15-regular-conditional-law, one in item (iii) of def:p15-w02b-p15-008-limits).
- Driver insertion (lead action): body after parts/p15/conditioning-independence-and-information-w02b-p15-008
  in handbook/parts/p15.tex; annex after annex/p15/conditioning-independence-and-information-w02b-p15-008
  in handbook/annex/p15.tex. w02ca-p15-007 requests the same anchor; either order compiles.

## Continuation

- State: C002 model, nonexistence proof (both Durrett's a.e. sense and the kernel sense), worked
  example, limits and relationships are written. unit-compile ok with 0 overfull; find_fused_spaces
  clean; check.py --tree handbook shows no findings in these files.
- Remaining outside owned files: lead applies the two patch entries and the two driver inputs.
- Not supplied here: an exchangeable non-presentable law for item 4 of
  thm:p15-w02b-p15-022-presentable. The 159.7 gap text notes that item 4 depends on such a law;
  its stated "Owed" item is the non-existence model, which is written. The non-presentable law
  (Dubins-Freedman 1979, Freedman 1980, not held) is left open and flagged to the lead.

### Continuation, block 2 (assessment disputes C002 and C021 of the conditional-expectation unit)

- Both disputes are classified lead_owned, route pending. The conditional-expectation unit is a
  readonly unit of packet w02c-p15-007; its C002 text (P|G versus P integrals, measure and
  absolute-continuity steps) is in the w02c-p15-007 body/annex and in w02ca-p15-007 patch entries on
  handbook/annex/p15/conditional-expectation.tex. Nothing written here for C002.
- C021 items on the route: patch file work/waves/w02ca/patches/w02ca-p15-008.json now carries
  (a) an extended insert after the existence-hypothesis sentence of def:p15-regular-conditional-law
  stating Durrett's p. 214 history (Dieudonne 1948; Doob 1953 p. 624; Faden 1985) and the
  exceptional-set explanation, with the pointer to thm:p15-w02c-p15-008-no-rcp (item 3);
  (b) an insert after the nonuniform-density sentence of thm:p15-conditioning-coordinate-examples
  naming Example 4.1.8 Borel's paradox and stating the apparent paradox (p. 210);
  (c) the two driver \input lines for this packet's body and annex.
- Locators re-seen this session in the held PDF: printed p. 210 = file page 218 (Example 4.1.8,
  Borel's paradox); printed p. 214 = file page 222 (r.c.d. definition, Theorem 4.1.16,
  Dieudonne/Doob/Faden, piling-up remark).
- Lead actions still needed: apply the patch entries; input the w02c-p15-007, w02c-p15-002 and
  w02c-p15-008 files in the drivers.

### Continuation, r4 block 1 (assessment disputes C001, C003, C008, C010, C012, C016, C018 of the conditional-expectation unit)

- The unit is a readonly unit of packet w02c-p15-007 (packet readonly_units); its host
  handbook/parts/p15/conditional-expectation.tex and annex are read-only for this packet. Following the
  block 2 handling of C021, the missing source claims are written as patch entries 6-14 of
  work/waves/w02ca/patches/w02ca-p15-008.json (insert_after, anchors each verified unique):
  6 C001 (best-guess reading, p. 207; conditions (i), (ii) pp. 205-206; Theorem 4.1.15 p. 213 as the
  L^2 form of the reading); 7 C003 (Examples 4.1.3-4.1.4 glosses pp. 207-208, guess and verify p. 208,
  Section 4.1.2 opening p. 210); 8 C008 (smaller sigma-algebra wins, powerful tool with Theorem 4.1.14,
  caution about false results, no analogue for ordinary expectation, all p. 212); 9 C010 (Example 4.1.5
  reading p. 208); 10 and 12 C012(b) (Remark after Example 4.1.6, p. 209: any Borel k with
  k(y)m(y) = int g f dx on D_0 = {m<inf, a<inf}; arbitrary on {m=0}; full annex proof); 11 C012(a)
  (Example 4.1.6 heuristic p. 209; Example 4.1.7 pp. 209-210); 13 C016 (Exercise 4.1.7 as special case
  of Exercise 4.1.6, p. 216, with the reduction written out); 14 C018 (Exercise 4.1.8 hint p. 216, both
  constant cases worked).
- Held source opened this session: source/references/durrett-probability-2019-01-11/PTE5_011119.pdf,
  file pages 213-224 (printed pp. 205-216) extracted with pdftotext into this block's scratch folder.
  Every locator above was seen there.
- Checks: patched copies of both hosts compiled in the scratch folder (pdflatex + biber, exit 0, no
  undefined citations, no overfull box beyond the unpatched host's own); 7-word overlap scan against
  the extracted pages shows no run longer than 8 words; find_fused_spaces clean on patched copies;
  unit-compile ok; check.py --tree handbook shows no finding in owned files.
- New symbols D_0 and k (scope thm:p15-conditional-density-formulas) added to the symbol intake. The
  host annex already uses k as a second representing function inside
  annex:p15.conditional-factorization; the scopes do not overlap.
- Lead actions: apply patch entries 6-14 (and 1-5 from earlier blocks).
