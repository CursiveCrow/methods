# P17-D5: social choice author intake

8 September 2026 UTC / 7 September Pacific. Root authored this collective-choice treatment while the other authors supplied Kamp Lemma 7, product measures and finite causal models. The author block finished within 45 minutes.

| File | Lines | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `handbook/parts/p17/social-choice.tex` | 321 | 15888 | `224340F36A0774478ED6CFD8713601190B23F97BE7950106DD4CD8F8B71E64FA` |
| `handbook/annex/p17/social-choice.tex` | 321 | 17627 | `C76738A8942F81BD5BF37E3701A30820AD24992E5B3805EC448CD9D883D69E6F` |

Both actual saved files were read completely. An initially combined read-back truncated the middle of the annex; the full annex was then retrieved separately and read to its final line. The governing contract, conventions and actual finite-preference interface were read. No earlier manuscript proof was changed.

## Exact source and written scope

The held presentation is Rubinstein, *Lecture Notes in Microeconomic Theory: The Economic Agent*, second edition, author revision 11 January 2015, existing key `Rubinstein2015LectureNotes`. Its 172-page PDF is `source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf`, SHA-256 `F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8`.

Root read complete printed pp. 122-131 as extracted text, then every complete printed page 122-128 as a 1400-pixel full-page image generated from the actual held PDF. Those seven source images, physical pages 136-142, are under the old task's `tmp/p17-social-source/`. Authoring covers Lecture 9's model, six examples, axioms, four-step Arrow proof and premise counterexamples, followed by the full binary characterization in Problem 1 on p. 128. Page 127 supplies the lecture's attribution of its proof to Geanakopolos; the distinct 2005 original was not newly read.

The chapter preserves finite positive electorate size, arbitrary alternative sets for Arrow, unrestricted strict input orderings and complete transitive weak social outputs. The proof includes ties in the extreme-alternative lemma, independence of the pivotal index from other comparisons, all modified profiles and both directions of the final reference-alternative comparison. It uses no unstated social monotonicity premise. An empty strict-profile domain is handled vacuously; the usual finite-alternative domain is nonempty.

All six source aggregation examples are specified. Finite-candidate minimization and most-common ordering have fixed tie-breaking. The source's two-thirds example is explicitly completed with a strict-output/default convention. Majority-victory and rank-score examples have computed pair counts and scores. Interpersonal intensity and single-alternative choice are distinguished from ordinal ranking.

For the binary exercise, individual indifference is allowed. Both directions of positive responsiveness are stated. Balanced profiles, anonymity, neutrality and one-coordinate changes determine the unique majority rule. The converse and all three independence examples are proved. The solutions and new computed examples are independently worded handbook developments.

## Seven complete proof pairs

Each suffix has body label `thm:p17-<suffix>` and annex label `annex:p17.<suffix>`.

- `social-majority`: counts, cycle, binary transitivity and nondictatorship.
- `social-aggregation-rules`: every listed rule's output, score Pareto properties and the changed victory comparison.
- `social-extreme-alternative`: distinct witnesses even with ties, admissible profile modification and contradiction.
- `social-arrow`: finite pivot sequence, all nonreference pairs, both reference directions and the entire weak relation.
- `social-arrow-boundaries`: all four removed-premise counterexamples and actual domains.
- `social-may`: balanced profiles, positive/negative cases and converse.
- `social-may-boundaries`: unequal positive weights, constant-one and constant-zero witnesses.

## Integration contributions

Append body and annex after finite subjective probability in the P17 routes, giving local scope `P17.5`. The existing Rubinstein entry is the sole citation; no new bibliography key is needed.

Canonical notation families: electorate N and n; alternatives X and finite size ell; ordering classes L(X), W(X) and profiles P, P-prime; social map F and weak/strict/indifferent comparisons; pair count V and majority comparison; victory/rank scores C, B, weights and positions; candidate ordering R and disagreement count D; pivotal profiles, step index and reference alternative; extreme comparison sets A and C; binary vectors, rule f, sign and voter permutations. Their types and domains are explicit in the body and annex.

Restricted domains, median-voter results, strategic manipulation, other aggregation and source Problems 2-5 remain owed. This chapter does not infer Gibbard-Satterthwaite from Arrow or repeat the source's incomplete statement of that separate theorem. New source, mathematical and publication reviews are assigned. This author note grants no independent acceptance or production/admission standing.
