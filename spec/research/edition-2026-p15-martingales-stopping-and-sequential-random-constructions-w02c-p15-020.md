# P15 packet w02ca-p15-020: provenance and continuation

Packet: `work/waves/w02ca/packets/w02ca-p15-020.json` (sections 162.2, 162.6, 162.10; label tag `p15-w02c-p15-020`).

## Sources opened in this session

- Durrett, *Probability: Theory and Examples*, version 5 (`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`, key `DurrettPTEAuthor2019`, printed page = PDF page - 8). Read: Exercise 4.8.4 (printed p. 261); Section 4.9 pp. 263-265 (equation (4.9.2), the Theorem 3.8.8 and Example 8.1.12 references); Theorem 3.8.8 (printed p. 191); display (7.4.6) (printed p. 374, hitting-time density); Example 8.1.12 (printed p. 395).
- Wald 1945, *Sequential Tests of Statistical Hypotheses* (`source/references/wald-1945-sequential/pages/page-NN.png`, printed page = NN + 116, key `Wald1945SequentialTests`). Read pages 119, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 146.
- Session 2 (continuation after usage reset): Wald 1945 pages 118, 122, 125, 133, 135, 136, 143, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157 opened. Durrett PTE5 pp. 186, 189 (Theorem 3.8.2, display (3.8.11), (3.8.12), kappa = 2 theta - 1), p. 191 (stable-law definition, Theorem 3.8.8), pp. 263-266 opened.

## Work in this session

1. C009 and C020 (optional-stopping host, read-only): patch requests in `work/waves/w02ca/patches/w02ca-p15-020.json` (entries 1-6). Entry 1 restores "T is a stopping time" in thm:p15-os-wald-second (Durrett Ex. 4.8.4, p. 261); entries 2-5 make the stopping-time use explicit in the annex, check that the exit time is a stopping time, and add the counterexample (E S_T^2 = 1/2 versus sigma^2 E T = 3/2) with a proof that the time is not a stopping time; entry 6 replaces "the nonpositive case is analogous" by a written exclusion of xi_1 <= 0 a.s. and writes out the block bound and the sum giving E_x tau <= k p_delta^{-k}.
2. C014 (reflection host, editable): def:p15-rb-next-boundary rewritten (body lines 321-356). It now says the limit is proved by the direct transform route, that the handbook treats neither the stable domain-of-attraction route (Durrett p. 264, Theorem 3.8.8 at p. 191) nor the Brownian identification (pp. 264-265, Example 8.1.12 at p. 395), names the normal-only domain-of-attraction chapter, and records that g is the a = 1 case of (7.4.6) (p. 374) as a formula comparison only.
3. Sequential-evidence assessment disputes: new chapter `handbook/parts/p15/martingales-stopping-and-sequential-random-constructions-w02c-p15-020.tex` with annex. C02 items (1)-(6), C03 items (1)-(2) and C04 item (7) are written. Patch entry 7 links def:p15-se-exponential-root to the new root results.
4. Scratchpad incident: the session scratchpad root is shared with another agent. A script I wrote there was overwritten by that agent's script, and running it wrote `work/waves/w02ca/patches/w02ca-p15-017.json`, the file that agent's script was meant to produce. I did not edit it otherwise. The lead should confirm that file with the p15-017 owner.
5. Session 2: owned chapter gains sections sec:p15-w02c-p15-020-regimes, -moments, -current, -truncation (C04 items a-i, C05 items a-c) and the p. 133 secondary-importance remark (C02). Tables 1-3 recomputed with scratchpad script p020/tables.py (Python statistics.NormalDist); eleven one-unit differences from the printed Tables 2-3 and one from Table 1 are listed in the text. Durrett display (3.8.11) read literally gives kappa = -1 for the positive half-stable law; the text records kappa = 1 as the source's tail value 2 theta - 1 with its density (3.8.12).
6. Session 2, reflection host (editable): 1878 attribution (C003), betting reading with proof (C009), density remark and pi_2n reading (C010), new thm:p15-w02c-p15-020-return-domain with annex proof and updated def:p15-rb-next-boundary (C014 a).

## Continuation

- C04 remainder: (b) EZ_n convergence under lattice approximation for unbounded non-lattice scores, and gamma when boundary hits have positive probability (bracket only); (f) normal-for-non-normal approximation of the law of n (invariance principle, not on route); (g) magnitude of the truncation-bound slack (identified exactly, not computed).
- C05 remainder: 47 per cent bound proved only on tabulated pairs (plus numerical .001 grid); Section 2.3 efficiency proved only as the normal small-shift limit.
- C014 (b) Brownian identification: needs Brownian first-passage content or a user decision.
- X-extent-scope (Part II Sections 5-6, pp. 158-186; Historical Note B, pp. 119-122): needs a scope decision; none read or written.
- Optional-stopping C009, C020: patch requests 1-6 in work/waves/w02ca/patches/w02ca-p15-020.json await the lead.
- Placement of the owned chapter on the route (after sequential-evidence in both drivers) awaits the lead.
