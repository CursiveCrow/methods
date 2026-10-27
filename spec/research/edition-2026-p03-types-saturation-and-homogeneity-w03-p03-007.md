# w03a-p03-007 (P3, section 25.1): Vaught 1961, section 5

## Sources read in this session

- `source/references/p03-vaught1961-original/vaught-1961-extracted.txt`
  (text of `vaught-1961-denumerable-models.pdf`, acquired from J. Baldwin's
  institutional page, SHA-256 digest beginning 5b834ccf; printed pagination 303-321).
  Read: printed pp. 315-318 (section 5 in full, notes 16-22) and p. 321
  (reference list). No online copy was used.

## Locators used (all seen in the held file)

- p. 315 (block 2, checked against the page image of the PDF, physical page 13):
  the illustrations before section 5: "condition of 3.5 or 4.7"; sections 3
  and 4 give no new information; T_1 = infinite discretely ordered systems
  with "say" a first but no last element; each script-P_n(T_1) countable via
  the known decision procedure; n. 16 (cf. [18] pp. 90-91); the
  aleph_0-universal homogeneous model omega+(omega^*+omega).eta; T_1 has
  2^aleph_0 non-isomorphic denumerable models; T_2 = real closed fields,
  script-P_1(T_2) "obviously" has 2^aleph_0 members; "as is known (cf. [16],
  [12])" the real algebraic numbers are prime and each F_n(T_2) is
  atomistic. p. 321 refs [12] Robinson 1956, [16] Tarski 1951 2nd ed., [18]
  Tarski-Vaught 1957.
- p. 315: Ehrenfeucht's 5.1; "the results of 3 and 4 may be applied"; 5.2 as
  an immediate consequence of 3.5, 4.8, 5.1; n. 17 (examples in [9] Los 1955
  and [19] Vaught 1954; categorical theories without finite models are
  complete); n. 18 (attribution of 5.1 to [2] Ehrenfeucht 1958 Notices, only
  n = 1 stated; [1] earlier result; case alpha = 0 easier, Mostowski [10];
  countable Boolean algebras have countably many or 2^aleph_0 prime ideals).
- p. 316: Theorem 5.2; aleph_alpha-categorical theories satisfy 5.1's
  hypothesis; no interest when aleph_0-categorical; ACF illustration (refs
  [12] and [18] p. 101); Theorem 5.3 with proof (uses 3.4, 1.1.1, 1.1, 3.6,
  1.3, generalized LS n. 19); Los's conjecture and the "5.2"/"5.3" wording.
- p. 317: Theorem 5.4; proof with T', displays (1), (2), relativization n. 21
  ([17] pp. 24-25), interpretations, 4.2 with 5.1, display (3), 4.4.
- p. 318: union of saturated chain (1.1.1); conclusion; n. 22.

## Mapping of the source to the reader text

- 5.1: `thm:p03-w03-p03-007-ehrenfeucht` (cited=Ehrenfeucht1958Notices),
  attribution paragraph after it; categorical case proved independently in
  `thm:p03-w03-p03-007-categorical-small`.
- n. 17: `thm:p03-w03-p03-007-categorical-complete` (proved in annex).
- 5.2: `thm:p03-w03-p03-007-five-two` with the 3.5/4.8/5.1 derivation remark.
- 5.3: `thm:p03-w03-p03-007-minimal-prime`, chain lemmas
  `thm:p03-w03-p03-007-chains`, `thm:p03-w03-p03-007-copy`.
- Los remark and n. 22: `def:p03-w03-p03-007-los-remark`; n. 22's claim is
  covered via `thm:p03-w03-p03-007-morley-transfer` (Morley), Vaught's own
  argument for it is not printed in the source.
- 5.4: `def:p03-w03-p03-007-auxiliary-theory`,
  `thm:p03-w03-p03-007-auxiliary`, `thm:p03-w03-p03-007-definable-sets`.
- ACF illustration: `thm:p03-w03-p03-007-acf` (stated for ACF_0, since a
  complete theory must fix the characteristic).
- p. 315 illustrations (T_1, T_2): `def:p03-w03-p03-007-illustrations`
  (proofboundary recording all six claims with attributed standing),
  `thm:p03-w03-p03-007-real-types` (the "obvious" one-type count, proved for
  Th of the real field), relationship paragraph to 3.5/4.7/never-two and to
  `thm:p03-vaught-discrete-example`.
- Boundaries: `thm:p03-w03-p03-007-pure-sets`,
  `thm:p03-w03-p03-007-two-cardinal-boundary`.

## Decisions

- Vaught's "in 5.2" at p. 316 in the Los remark is read as 5.3 (5.2 has no
  aleph_1; the next sentence names 5.3). Stated in the reader warning.
- No new bib keys for Vaught's refs [16] (Tarski 1951) and [18] (Tarski-Vaught
  1957): they were not read; they are named in prose and located through
  Vaught's p. 321 reference list.
- Footnote marker attached to the statement of 5.2 on p. 316 is illegible in
  the extraction; no locator is attributed to it.

## Route

The body and annex files are not input by any host. Patch request:
`work/waves/w03a/patches/w03a-p03-007.json` (body after
`parts/p03/presentations/n-a-003-01` in `parts/p03/classification-theory.tex`;
annex after `annex/p03/n-a-003-01` in `annex/p03.tex`).

## Continuation

- Block 1 (2026-10-12): fixed the undefined reference to the section 6
  presentation (now `sec:p03-vaught-never-two-presentation`); added n. 17
  lemma with annex proof; added the 3.5/4.8/5.1 derivation remark for 5.2;
  replaced the "not reconstructed" sentence on n. 22 by the Morley-based
  coverage; shortened titles causing overfull boxes; wrote patch request and
  return file. unit-compile reports ok (3 overfull boxes remain, none
  fatal); check.py shows only bib-key for the intake key
  Ehrenfeucht1958Notices.
- Open: Chang-Keisler 1990 and Marker 2002 parts of N-a-003-C01, and Hodges
  1993 chapters 7 and 10 (ED26-SRC-048-0007-C001..C004,
  ED26-SRC-048-0010-C001..C007): sources not held, no free copy of any
  version.
- Open: the route insertion needs the lead to apply the patch request.
- Block 2 (2026-10-13): closed the assessed N-a-003-C01 gap on the p. 315
  illustrations: new subsection `sec:p03-w03-p03-007-illustrations` (body
  lines 375-466), proofboundary with T_1 hypothesis, the 2^aleph_0
  denumerable-models remark, the atomisticity of F_n(T_2), and all other p. 315
  claims with attributed, unproved standing; lemma on 2^aleph_0 one-types of
  Th(R) with annex proof (annex lines 607-653). Patch request extended with
  a cross-link sentence for n-a-003-01.tex. unit-compile ok (3 overfull);
  check.py: only bib-key for Ehrenfeucht1958Notices.
- Still open: T_1 completeness, its countable type sets, the order type of
  its universal homogeneous model, its 2^aleph_0 denumerable models, and the
  T_2 prime-model/atomisticity claims are recorded as attributed (Vaught
  proves none of them); Chang-Keisler, Marker and Hodges parts as before.
