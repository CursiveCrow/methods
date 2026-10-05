# w02b-p15-073 — P15 chapter 173 (sections 173.5–173.8): range estimate and omitted variable

Packet: work/waves/w02b/packets/w02b-p15-073.json. Label tag: p15-w02b-p15-073.

## Provenance

- Held source opened in this session: source/references/mahajan-2014-insight/mahajan-2014-art-of-insight-ocw.pdf
  (SHA-256 digest b4deb8e4…42a6, 410 pages; held-sources.json entry). Printed pp. 6–7 read via pdftotext
  (PDF pages 25–26), plus the held extract dimensional-reading/sections-1-3-to-1-5.txt (printed pp. 7–16).
- Locators used and seen: p. 6, eq. (1.3) (two-second following rule, one person per car, 1800 people/hour);
  p. 7 (gap qualification: about 4 s late at night, 1 s in the day; compromise value; train line
  150 × 20 × 6 = 18 000 people/hour, eq. (1.4)). Section 1.2 "Rails versus roads" (contents p. 6).
- Handbook derivations (not attributed to the source): steady single-lane traffic model, time-gap model,
  non-overlap bound q ≤ nv/L, Φ(z) = 1/(1+z), monotone-box lemma, outward-rounding reporting convention,
  all numerical input ranges (n ∈ [1, 1.5], τ ∈ [1, 2] s, L ∈ [4, 6] m, v ∈ [25, 35] or [0.5, 2] m/s).
- No new bibliography keys (Mahajan2014Insight is in handbook.bib).

## Gap addressed by the new text (unassessed)

ED26-GAP-SCI-002-C04 (sections 173.5, 173.6, 173.7; unit ED26-SCI-Mahajan2014-001): one order-of-magnitude
estimate with explicit input ranges (def:p15-w02b-p15-073-lane-estimate), the same estimate with its omitted
variable L/v at highway speed (def:p15-w02b-p15-073-highway) and its failure in slow traffic
(def:p15-w02b-p15-073-congested: range excluded, factor up to 13, threshold verdict changes to abstain; a
gap-rule-free version below 4/3 m/s from thm part (4)). Digits: outward one-significant-figure report;
geometric midpoint 3118 shown as the unearned-digit failure. Not a confidence interval:
def:p15-w02b-p15-073-not-interval.

Existing treatment found and linked (not rewritten): host dimensional-and-scaling-inference.tex covers
C01 (thm:p15-dimensional-rank-nullity, def:p15-dimensional-elimination, W/(mg) rank example), C02
(sec:p15-dimensional-pi, scaling laws, pendulum constant), C03 (units, curved track conversions, drag regime,
sphere plot); range bounds thm:p15-dimensional-product-bounds. SCI-003 (unit ED26-SCI-Mahajan2014-002) is
readonly, owned by w02b-p15-070; only \cref'd.

Patch request: work/waves/w02b/patches/w02b-p15-073.json (one sentence after the train-line range paragraph
in the host, pointing to the new chapter).

## Continuation

- Run r2 (continuation): closed the C03 gap named by the assessment. New section
  sec:p15-w02b-p15-073-invalid (body lines 139-221): lemma thm:p15-w02b-p15-073-invalid-candidate
  (monomial test, sum test, unit dependence of n/(tau+L); annex proof lines 91-137) and example
  def:p15-w02b-p15-073-invalid-check (three candidates checked against dimension vectors; two shown
  invalid with numbers in m, km, mm; the valid one shown not established by the check). Procedure step 1
  now includes the dimensional check and unit conversion. All of this is a handbook derivation; no source
  locator is attached to it.
- Fixed the fused-space hit on the provenance line (now "SHA-256 digest").
- G1 hits on spec/research/edition-2026-p01-symbol-registry-w02b-p01-014{.md,-return.json}: those files
  belong to packet w02b-p01-014 (written 18:15-18:16, after this packet's last write at 17:23); not
  created or edited by this packet and left untouched.
- State: unit-compile ok (3 overfull boxes, all in the Mahajan2014Insight bibliography entry);
  find_fused_spaces no hits; check.py shows no findings for these files.
- Open items: C04 route pending: driver inputs (handbook/parts/p15.tex after
  parts/p15/approximate-quantitative-inference; handbook/annex/p15.tex after
  annex/p15/approximate-quantitative-inference) and the host patch are lead actions.
- Symbol overlap to decide: n (here occupancy; host row 2316 uses n for number of quantities), D (same role
  as def:p15-dimensional-matrix), Phi (normal CDF elsewhere in P15), sigma (here the unit-change vector,
  the host's s), L, v, q, tau local to sec:p15-w02b-p15-073.
- Run r3 (continuation, section 173.8 relation signs). Held PDF reopened this session (SHA-256 digest
  b4deb8e4...42a6). Pages viewed as images: physical 24 (book p. 5, Sec. 1.1, table of the five signs
  equality by definition, =, approx, sim, propto; circle and cylinder examples), physical 230 (book p. 211,
  Sec. 6.3.5, eq. (6.23) E sim rho R^5/t^2), 232 (book p. 213, Sec. 6.4, a sim 3 angstroms, eqs. (6.28) approx,
  (6.29)-(6.32) sim), 237 (book p. 218, Sec. 6.4.3, v_term approx 1 m/s), 240 (book p. 221, eq. (6.38)
  n sigma lambda sim 1), 245-247 (book pp. 226-228, eqs. (6.48)-(6.53) sim; p. 227 says the function is a cube
  root times a dimensionless constant), 316 (book p. 297, Sec. 8.3, eq. (8.33) F_d sim rho v^2 A_cs, c_d table
  car 0.4, sphere 0.5, cylinder 1.0, flat plate 2.0), 326 (book p. 307, Sec. 8.3, k_B T sim G M m_p / R, eq. (8.47)).
  Result: every approx_est in approximate-quantitative-inference.tex (lines 228, 236, 255, 292, 430) restates a
  source sim; line 226 'a approx 3 angstroms' restates a source sim. The host's claim of a single sign is wrong.
  The sign counts quoted in the assessment (sim 83, propto 18, approx 5) were not recounted (pdftotext loses the
  glyphs); no count is written in reader text.
- Fix: two replace entries appended to work/waves/w02b/patches/w02b-p15-073.json for the read-only host
  (def:p15-approximation-relations lines 29-31; line 226). Test-compiled in scratch with the patches applied:
  no LaTeX error from the new text. Own chapter: lines 278-282 contrast the source's sim with the ratio-limit
  sim of thm part (5); sources paragraph line 448-449 cites Sec. 1.1, p. 5.
- Symbol intake: six rows for the source's graded signs and drag quantities, scope def:p15-approximation-relations.
- Still open (lead actions): driver inputs for this chapter and its annex; the three patch entries.
- Run r4 (continuation). The only gaps named were G1 hard guards on
  spec/research/edition-2026-p01-symbol-registry-w02b-p01-014{.md,-return.json} (owner packet w02b-p01-014,
  last written 22:34 by that packet's agent) and
  spec/research/edition-2026-p02-fol-metatheorem-table-and-nd-cpl-sheet-w02b-p02-036{.md,-return.json}
  (owner packet w02b-p02-036, written 18:23). Neither was created or edited by this packet; A8 forbids
  modifying other agents' files, so they were left untouched. The guard attributes untracked files of
  concurrent packets to this packet; the lead resolves it by scoping G1 per packet.
- r3 assessments (all eight components covered; C03/C04 route pending) reread; no text change needed.
  Re-ran unit-compile (ok, 3 overfull boxes in the Mahajan2014Insight bib entry), find_fused_spaces (no hits),
  check.py (no findings in owned files).
- Open lead items unchanged: driver inputs (parts/p15.tex, annex/p15.tex after
  approximate-quantitative-inference) and work/waves/w02b/patches/w02b-p15-073.json. Assessor observation:
  chapter heading differs from the toc-tagged section titles 173.5-173.8; numbering/routing is a lead decision.
