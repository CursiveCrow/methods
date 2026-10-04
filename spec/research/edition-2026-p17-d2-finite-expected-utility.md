# P17-D2: expected utility and monetary risk

Author block: root, 8 September 2026 UTC / 7 September Pacific time. These are new independently written manuscript treatments, returned for fresh source, topic and publication-text reviews. No independent acceptance or admission is supplied by this note.

## Written scope

The new body/annex pairs are `handbook/parts/p17/finite-expected-utility.tex` and `handbook/annex/p17/finite-expected-utility.tex`, followed by `handbook/parts/p17/risk-aversion.tex` and `handbook/annex/p17/risk-aversion.tex`. Both follow the existing finite-preferences chapter on the active P17 routes. All four complete authored files were read back; subsequent strict-increase and quantifier wording clarifications were reread. The two chapters supply thirteen reciprocal result/proof items.

| Frozen author file | Lines | SHA-256 |
| --- | --- | --- |
| Expected-utility body | 390 | `6F83B6CB0300B241C8751E48747B577FB5869A02418C1C8C621E808515DD6EB5` |
| Expected-utility annex | 340 | `C04B72A6DDC4B34147359A776597B99A16E4DE6D61A7C4789F5C413CF2FF11D3` |
| Risk-aversion body | 355 | `F2B0A4CF575723E4CB6F8212077A59E64E276DAA43A5B25B57374D8E6657CD4A` |
| Risk-aversion annex | 417 | `1FAEAA08391C801C52CC0814189AE4B7FB4FB26DE788C0F7789D62D46917DC7A` |

| Treatment | Complete supplied content |
| --- | --- |
| Finite expected utility | Finite prize/simplex and compound reduction; weak preference, mixture independence and relative-neighborhood continuity; component replacement including zero and unit weights; strict binary-mixture order; full supremum-based calibration; both directions of finite vNM representation and all-indifferent case; positive affine uniqueness including constant utilities; finite-menu method, calibrated choice and common-consequence examples; full independence and continuity counterpreferences. |
| Monetary risk | Finite-support domain on an interval; first-order dominance with both endpoint conventions and explicit increasing witness; finite and strict Jensen, secants and derivative criterion; risk-aversion/concavity and risk-neutral/affine equivalences; certainty-equivalent existence and risk premium; all three comparative-risk equivalences; positive-derivative Arrow–Pratt criterion and local indifference-curve derivatives; full continuous wealth-invariance characterization on the real line, retaining the source's grid and differential routes; exact worked certainty equivalents and exponential premiums. |

## Exact primary source and reading

The held source is Ariel Rubinstein, *Lecture Notes in Microeconomic Theory: The Economic Agent*, second edition (2012), author revision dated 11 January 2015. Local file: `source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf`, SHA-256 `F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8`. The existing canonical key `Rubinstein2015LectureNotes` preserves that exact manifestation; no new entry or acquisition is needed.

Root read complete text from physical pages 1–14 for the version/title/contents context, physical 108–119 (printed 94–105), and physical 122–133 (printed 108–119). All eleven complete source pages 94–104 and all twelve pages 108–119 were also visually inspected at 1,500-pixel scale, including displayed formulas, the figures, marginal definitions, assumptions and source proof endings. The first page of Problem Set 7 was read as context; the problem set is not claimed covered.

The source images are retained in the current task workspace under `tmp/p17-expected-utility-source/`, named `source-108.png` through `source-118.png` and `risk-122.png` through `risk-133.png`. These are primary-source reading images, not manuscript renders. The PDF skill controlled accurate source reading. No PDF was authored in this block, so no PDF authoring marker applied. The research skill supported primary-source tracing; the three parallel authors also performed their assigned independent source work.

| Source extent | Manuscript use |
| --- | --- |
| 94–97 | Lottery domain, consequential description, compound mixtures and independence; the new joint-law proof distinguishes conditional branch laws from independence of branch and prize. |
| 97–100 | Replacement property, strict mixture lemma, neighborhood continuity, vNM construction and affine uniqueness. The handbook supplies complete interval-calibration and endpoint proofs; no general Debreu theorem is used as a missing premise. |
| 101–102 | Exact four common-consequence lotteries and procedural/consequence qualifications. No source empirical response percentage is turned into a new population claim. |
| 108–110 | Finite-support monetary domain, tail/cumulative first-order dominance and telescoping identity, with a fully specified converse utility witness. |
| 110–113 | Concavity, Jensen, secants, risk aversion, certainty equivalents and three comparative definitions. Included endpoints retain an explicit continuity hypothesis where required. |
| 114–115 | Arrow–Pratt comparison and binary indifference curvature, with explicit C2 and positive-derivative conditions. |
| 115–118 | Final-wealth interpretation, wealth translations, grid increments and continuous/differential constant-risk-aversion characterization. The full continuous functional-equation proof supplies compatibility across grids. |
| 118–119 | Read for source boundaries; Rabin calibration and empirical extrapolation are separate remaining treatments, not proved or claimed by the finite-risk results. |

## Dependencies and checks

The actual finite P15 expectation definition/theorem and finite P17 preference, ordinal-representation and maximal-choice interfaces were read. Their current maintained hashes remain: P15 body `934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1`, P15 annex `7CE651CE52FE8BFA66E5BEC221BDF48EE6318538E6A99B8E987E18C90D6B67F3`, P17 finite body `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C`, P17 finite annex `B141A371731E7A0A3BEFF1C88C839F98720BE4F894A2D475CAF098A61159202C`. Their existing text and production records remain separate evidence.

The expected-utility proof assumes real order completeness; the risk proof additionally uses the stated elementary one-variable calculus in its differential results. The global expected-utility function on an infinite monetary interval is explicitly assumed, not inferred merely from the finite-prize representation. The no-derivative wealth-invariance proof retains its original continuity/strict-monotonicity scope. Its differential route states its additional regularity separately.

Direct author checks covered zero mixture weights, singleton prizes, all-indifferent utility, strict versus nondecreasing transformations, atom endpoints, the strict-Jensen minimum-prize argument, certainty-equivalent range, derivative positivity, and the additive/multiplicative functional equations on negative as well as positive wealth. Worked values are checked by the actual displayed sums and transformations. The existing scoped scanner reports no findings and all thirteen proof pairs are reciprocal. The larger ten-file wave scan has thirty-one reciprocal pairs and no findings; bibliography has 639 entries with no intake stubs. No tests, manuscript build or manuscript page inspection were performed.

## Notation intake and continuation

P17.2 roles: `Z`, `Delta(Z)`, `delta_z`, `p,q,r`, mixture weights and reduction; `succeq/succ/sim` on lotteries; Euclidean `d`; binary segment `B_t`; best/worst `M,m,z^+,z^-`; consequence `u` versus lottery `U_u`; affine constants; finite menu `mathcal B`; common-consequence lotteries and the counterpreference `V`.

P17.3 roles: interval `I`, `Delta_f(I)`, support, mean `mu`, monetary `U_u`, dominance `succeq_FSD`, cumulative `F_p` versus upper tail `G_p`; certainty equivalent and premium `CE_u,pi_u`; relative transformation `phi`; absolute coefficient `r_u`; local curve `psi_t` and fixed probability `theta`; translated lottery `T_w`; continuous translation factors `A(w)` and their logarithm; grid spacing/increments/ratio; exponential parameter `rho` and `cosh`. Each is declared locally before use. Root owns canonical notation and candidate projections.

The review emphasis is exact utility-scale meaning, the global-domain distinction, all endpoint cases, strict versus weak claims, and preservation of the source's continuous wealth-invariance scope. General subjective expected utility, ambiguity, higher-order dominance, infinite-support/stopping issues, the complete Rabin calibration argument, sequential information and strategic/collective reasoning remain required later work. This two-chapter authoring block does not close the entire P17-D2 parent or P17.
