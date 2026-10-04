# N-c-010 independent manuscript review record

## Admission scope

This record closes the reader-facing source reconstructions for exactly:

- `N-c-010.a`, Baader--Brandt--Lutz (2005), including the separately acquired
  technical report and the later 2008 lineage check;
- `N-c-010.b`, Calvanese et al. (2007); and
- the W3C OWL 2 Profiles controlling presentation, together with the inherited
  Structural Specification and Direct Semantics conditions needed to state it.

It does not close `N-c-010.c`: the assigned 2017 Baader--Horrocks--Lutz--Sattler
chapter bodies remain unacquired, and their owed reconstruction remains
explicitly `OPEN`.  It also does not admit Part IX, any build or rendered page,
or the final handbook.

All three final reviewers accepted the following exact snapshot:

| Artifact | SHA-256 |
|---|---|
| `handbook/parts/p09/presentations/n-c-010.tex` | `2ECA1D578B5734E8BAC039BDBFA7A2F7BEF5364E7268A11A25B02E1B09A18C68` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `EAAA272F42596E72F7455C68555819A129215AE56A22DA87824B693DA9D9E056` |
| `handbook/bib/handbook.bib` | `AC811C3E21F76830822D4A78B3786AC2D36660BB919F6C5FEC16217BD663D8E2` |
| `spec/research/p09-source-presentations-lot2-3.md` | `1BD4B39F38ED3A5A014B037987BEF6D2DE141C7D2B85B6FC45878E6A1A831FEF` |
| `spec/research/p09-baader-brandt-lutz-2005-source-note.md` | `DBE576590ABB792315B6317D0F9A4F7C0CAA616C30A4959257C6045A8EB509ED` |
| `spec/research/p09-calvanese-et-al-2007-source-note.md` | `B0D4F0C2E5BD3BB795F313D08572939CC85CC08EFECB580A87ABEE94163270C4` |
| `spec/research/p09-w3c-owl2-profiles-2012-source-note.md` | `5B76CF7FD39CA288C1E754099219C576AC122E9334ADFF326F619D488BC0455C` |

The ledger hash is the pre-admission snapshot read by all three reviewers.  Its
subsequent status-only change records the unanimous verdict and links this
record; it does not change reader-facing content or a source claim.

## Primary authority surface

| Authority | Scope used | SHA-256 |
|---|---|---|
| Baader--Brandt--Lutz, IJCAI 2005 | complete six-page conference paper | `4C9CAA8C224506123B7EE06CFCC8F5759D3537F4C241BB7E6BDDCB89E0727A5A` |
| Baader--Brandt--Lutz, LTCS-05-01 | cover and all thirty-two printed report pages | `374D73EB848E556DA759D89231385353996F44E6A6131F53D2794BB68D5AA3BA` |
| Calvanese et al., JAR 2007 | complete forty-five-page article | `3ADF046934B01EAEDB9783F406B129C414515E6A187F2EC7E52008F072AA8164` |
| W3C OWL 2 Profiles, 11 December 2012 | complete dated Recommendation | `1599D792A39FE30000913822DEFFD78CB0905542C3EE3D956EFC9E51A7273C05` |
| W3C OWL 2 Structural Specification, 11 December 2012 | complete dated Recommendation | `2849F489758F82DF474536D66DDD86BCA8CF96F67500CE063FAA172DC29EBF7A` |
| W3C OWL 2 Direct Semantics, 11 December 2012 | complete dated Recommendation | `282DB71227A69895C6113E4141AC32AA8DFD5DD1E87420FA57245898F7B89022` |
| W3C OWL 2 errata capture | complete captured errata page | `FF1CC1B56B2A3A956D54E7D99FD97DA2389A3B3829D010750473238483253EE1` |
| Baader--Brandt--Lutz, OWLED 2008 | complete ten-page lineage paper | `D68DE99A3E6D613B116D405B562EC7F8030CDFA75B2449820D10240EB1868C99` |
| Horrocks--Kutz--Sattler, KR 2006 | complete eleven-page SROIQ lineage paper | `21235D525BD45B8DE924EE6700BD974E6AF1B8BE89C10F7B0A4E7C6EBC28ED0A` |

The inaccessible 2017 chapter bodies and the unacquired Kazakov body were not
treated as inspected authorities.  The manuscript withholds their exact
presentation-specific claims rather than inferring them from later metadata or
other papers.

## Reviewer runtime and independence

The runtime exposed each canonical reviewer identity and role but not an exact
deployment/build identifier.  All three were Codex subagents inheriting the
root's GPT-5-family model; an unavailable exact build is recorded as unavailable
rather than guessed.

Each reviewer was instructed to read the complete current scope and relevant
primary authorities, not to inspect or contact another reviewer, and not to
edit any file.  Source-PDF and captured-HTML reading was allowed only for
scholarship.  Tests, checkers, repository scripts, TeX, handbook-PDF inspection,
and builds were prohibited and were not used as review evidence.

## Source-fidelity review

- Canonical reviewer: `/root/schmidt_smolka_1991_research`.
- Role: complete primary-source fidelity.
- Authority scope: every authority in the table above, all three source notes,
  the integrated presentation, overview, bibliography, and ledger.
- Final verdict on the accepted snapshot: **ACCEPT**.

The final-round instruction required a complete rereview and explicitly asked
the reviewer to verify the positive-length transitive-role constructor and all
Structural Specification conditions on a datatype introduced by
`DatatypeDefinition`, then to reconfirm every prior source-fidelity dimension.

Evidence digest: the reviewer checked the EL++ grammar, semantics, CBoxes,
arbitrary input role chains and unary/binary normalization, NF1--NF7,
CR1--CR11, finite saturation range, concrete-domain hypotheses, proof
dependencies, countermodel, extension bounds, source defects, and OWL
nonidentity.  For DL-Lite it checked all three grammars, UNA, equality
preprocessing, ABox boundaries, canonical interpretation, NI closure, chase,
homomorphism, constant-restricted certain answers, PerfectRef, examples, and
the exact theorem parameters.  For OWL it checked the ontology header,
datatype inventories and restrictions, all EL/QL/RL expression and axiom
positions, property hierarchy, simplicity, regularity, anonymous individuals,
EL range imposition, Direct-Semantics checked expressions, PR1, noninclusions,
and every Table 10 qualification.

## Subject-matter review

- Canonical reviewer: `/root/p09_math_proof_review`.
- Role: mathematical and proof correctness.
- Authority scope: the complete accepted snapshot and every acquired primary
  authority required by a theorem, rule, semantic clause, or complexity claim.
- Final verdict on the accepted snapshot: **ACCEPT**.

The final-round instruction required the reviewer to recalculate all hashes,
re-read the complete unit, verify the two last source corrections in
mathematical context, and reconfirm every type, quantifier, hypothesis, proof
step, reconstruction, example, and fixed/varying complexity parameter.

Evidence digest: the reviewer verified finite CR8 carriage and termination,
nominal reachability, the EL++ soundness and countermodel directions, and every
constructor-sensitive complexity boundary.  It verified the DL-Lite empty-ABox
case, canonical carrier, total homomorphism repair, constant-restricted
Theorem 29 and Lemma 39 equation, every PerfectRef rewrite/reduction case,
finite-state termination repair, inconsistent-KB FO completion, and Theorems
41, 43, 44, 46, 47, and 48 at their stated strengths.  It also verified every
OWL grammar arity and position, the inherited datatype/property restrictions,
the six noninclusion witnesses, the task definitions, checked-expression
simplicity, input axes, and Table 10 force markers.

## Adversarial publication and AGENTS review

- Canonical reviewer: `/root/mcnaughton_1966_research`.
- Role: omissions, unsupported additions, terminology, source standing,
  cross-presentation integration, and the supplied five-part technical-name
  rule.
- Authority scope: the complete accepted snapshot, all source notes and
  authorities, bibliography identities, and the open 2017 boundary.
- Final verdict on the accepted snapshot: **ACCEPT**.

The final-round instruction required the reviewer to recheck its two previous
blocking findings, apply the technical-name rule to every introduced term, and
repeat the complete adversarial publication review without another reviewer's
output.

Evidence digest: the review confirmed that transitive closure was no longer
strengthened to reflexive-transitive closure; that the defined-datatype
declaration, empty lexical space, literal prohibition, facet prohibition, and
`DatatypeRestriction` boundary were all present; and that the separate W3C
hierarchy closure remained correctly reflexive-transitive.  It also confirmed
definition before use, exact metalinguistic standing and downstream necessity
for `q_unsat` and `Consistent`, disclosure of handbook reconstructions,
noncollapsed source variants, exact profile and complexity boundaries,
bibliographic identity, and the continued `OPEN` status of `N-c-010.c`.

## Revision history and final boundary

Four independent rounds were needed; no majority vote was used.

1. The first round found defects in CR8's finite range, DL-Lite equality and
   active-domain handling, canonical typing, OWL inherited definitions, task
   parameters, Table 10 attribution, and unsupported expressive-DL claims.
2. The second round found the remaining checked-expression simplicity
   condition, undefined DL-Lite abbreviations, equality-reconstruction
   disclosure, OWL grammar arities and axiom positions, the EL role-chain
   normalization wording, the IJCAI imprint, a canonical-answer type error in
   the source note, and underfixed TBox-size parameters.
3. After those repairs, source fidelity and mathematics accepted, while the
   adversarial review found two residual source defects: transitive closure had
   been strengthened to reflexive-transitive closure, and the inherited
   defined-datatype lexical/facet restrictions were missing.
4. After the two final corrections, all three reviewers independently returned
   **ACCEPT** on the exact snapshot recorded above.

This establishes the three manuscript-content review gates only for
`N-c-010.a`, `N-c-010.b`, and the controlling W3C presentation.  It establishes
the accuracy of the explicit open boundary for `N-c-010.c` but does not fulfill
that presentation.  Part IX admission, the final one-book publication build,
rendered-page inspection, and the user's final acceptance remain open.
