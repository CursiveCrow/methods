# Evidence extension: independent source-fidelity review

Reviewer: `/root/evidence_extension_source_review`, a fresh nonauthor.
Date: 8 September 2026 UTC / 7 September Pacific.
Repository: `C:\Dev\the-methods-of-reason`, branch `phase4-codex`.
Standing: source-fidelity review of four frozen body/annex pairs. No current
reviewer conclusions were consulted. This file is the reviewer's sole write.

## Verdicts and complete target reading

| Unit | Source-fidelity verdict | Target reading |
| --- | --- | --- |
| Kamp III.2, Lemma 5 | **PASS** | Entire body, lines 1-250, and entire annex, lines 1-464, including both proofs and all examples. |
| Measure extension and distribution existence | **PASS** | Entire body, lines 1-368, and entire annex, lines 1-551, including all six proofs. |
| Finite bets and subjective probability | **PASS** | Entire body, lines 1-288, and entire annex, lines 1-266, including all six proofs. |
| PA evidence construction and positive introspection | **PASS** | Entire frozen body, lines 1-562, and entire frozen annex, lines 1-984, including all five proofs and the general original-Sigma-one assertion. Reading began only after root supplied this pair's final hashes. |

No unread remainder in the eight targets or their four intake notes. No
actionable source mismatch, omitted source hypothesis, unsupported attribution,
or unprovided original-presentation conversion was found in these targets.
The verdicts concern the frozen text and its stated dependencies.

### Exact reviewed target hashes

Paths in this table are relative to `handbook/`.

| File | SHA-256 |
| --- | --- |
| `parts/p09/presentations/kamp-iii2-lemma5.tex` | `3FF96929A113AE7273508A7278D42A8DC883D014A592B98E780208BD243480EF` |
| `annex/p09/kamp-iii2-lemma5.tex` | `26381378ADECC27A479724DBFAEA4650ACAF4DF29D62B4DF999FD42F758C8963` |
| `parts/p15/measure-extension.tex` | `E1333244607DB51AE1EE5EC8FBF6AECA9AE8A2D85989677ED29ED9866119558E` |
| `annex/p15/measure-extension.tex` | `D5179047198A9EDDE628274345D19DE75E30FC33CE065DAEC9F23F02DE83838F` |
| `parts/p17/finite-subjective-probability.tex` | `A599CD4F95B5876E0E6904CB144F83979154958DE6D56E3CBFDE17AC98401243` |
| `annex/p17/finite-subjective-probability.tex` | `655A21E509312E709AAEBD5080DF265DB5D7D1BDC5BC2A5407C292BA25B80A48` |
| `parts/p05/pa-positive-introspection.tex` | `7310A4F7967AD376E54F799324ADDC214535520ACA5AD8174F2D73AA8F9B821B` |
| `annex/p05/pa-positive-introspection.tex` | `46CCC2144A1599DD6C5118EFCC8CA3BFB7899B8234CEF37E28547D7F47DEB9D0` |

The complete intakes were `spec/research/edition-2026-c7-kamp-iii2-lemma5.md`,
`edition-2026-p15-u1-measure-extension.md`,
`edition-2026-p17-finite-subjective-probability.md`, and
`edition-2026-p5-positive-introspection.md`. The last intake's supplied hash,
`249CE2FC092F7A34D0ABBA4DB3C34C6770567DEDCDBE9423EDBF2CF561B65252`, matched.
Intake claims were checked against the actual text and sources below.

## Held primary sources and actual reading

All three PDF hashes were independently computed in this review.

| Held source | SHA-256 | Fresh reading in this review |
| --- | --- | --- |
| Kamp, *Tense Logic and the Theory of Linear Order*, UCLA dissertation, 1968; `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf` | `C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA` | Title and approval pages (physical 1-2), plus full printed pp. 12-14, 40, 63-68, 73, and 78-79 as complete page images. Printed n is physical n+9. Pages 78-79 were the retained full source images, physical 87-88. The scan's extracted text was unusable for reliable reading, so the page images supplied the evidence. |
| Durrett, *Probability: Theory and Examples*, author Version 5, 11 January 2019; `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf` | `AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886` | Title/version page and full printed pp. 1-6, 11, 455-460 from the actual PDF; full pp. 5, 6, 11 and 459 also inspected as page images. Printed n is physical n+8. The complete Appendix A.1 was read, including all of Lemma A.1.6. |
| Rubinstein, *Lecture Notes in Microeconomic Theory: The Economic Agent*, second edition, author revision 11 January 2015; `source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf` | `F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8` | Physical pp. 1-3 for title/revision; full printed pp. 100-103 from the PDF and full pp. 102-103 as images. Full printed pp. 16-17 were read for the source's precise continuity definitions. Printed n is physical n+14. |

The existing bibliography records `Kamp1968`, `DurrettPTEAuthor2019`, and
`Rubinstein2015LectureNotes` were inspected at `handbook/bib/handbook.bib`.
They identify the held manifestations correctly. Primary locators are the
[Stuttgart thesis](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf),
[Duke author version](https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf), and
[Rubinstein author revision](https://arielrubinstein.tau.ac.il/Rubinstein2007.pdf).
The held documents, not a newly retrieved alternative edition, support this review.

## Kamp III.2, Lemma 5: PASS

The exact displayed source hypothesis and conclusion on pp. 78-79 are retained:
distinct x,y,z; E(z) midpoint conditions; I(x,z) and I(z,y) side conditions;
one strictly intermediate witness; and I(x,y) as the conclusion. Source p. 68
defines I with Com, and p. 73 changes the default equivalence convention to
Com. The new body at 175-211 preserves this scope. Its separately labelled
Lin identity at 51-83 is an additional consequence of the finite realization
proof, rather than a change to the arbitrary I-representation premises.

The source's actual construction was checked in full. It conjoins midpoint
conditions, introduces fresh Q0, uses Lemma 4 on each side, distributes every
pair, deletes the first right-word occurrence Q'', concatenates, and substitutes
(Q0(z) and Q'(z)) and Q''(z) at Q'. The body word at 13-49 and annex 113-196
retain that complete construction. In particular Q'' is restored at the shared
point, the newly inserted Q' survives the single substitution step, later
restoration removes the fresh skeleton letters, and the replacement argument
is bound at the actual midpoint. The source's compressed R8 references do not
become invented closure rules: the annex uses the actual R6 and R7 statements.

The complete two realization directions and finite-family proof were read.
The lists enumerate every fusion and every left/right choice. The two sides
use the same witness; all interval labels and three midpoint labels survive.
The empty-family extension is explicitly separated from the indexed source
statement and proved at annex 403-436. Its all-empty case remains the strict
midpoint existential. False gap labels on empty gaps and contradictory point
labels are treated differently, as their semantics require.

Dependency reading was selective and explicit: the live n-c-012 order/language
interface, Lemma 1 body 1-190, Lemma 2 body 1-120, all of Lemmas 3 and 4 bodies,
and Lemma 4 annex 1-242 and 476-522. These contain the required basic classes,
word realization, E/Ep, proper substitution, R5-R8 and accepted conjunction
interface. This review does not claim a new full review of all older Lemma 1-4
proofs. Lemma 6 beyond the page-79 continuation context remains outside scope.

## Measure extension and distribution existence: PASS

The source's exact semialgebra definition, partition hypotheses and two-stage
extension are present at body 25-91 and annex 12-87. The explicit empty-set
clause and the term premeasure clarify the source's measure-on-an-algebra
convention without enlarging the theorem. The cover construction at body
127-165 and annex 164-272 agrees with the source's full existence proof on
pp. 458-460, which expressly does not require sigma-finiteness. Uniqueness
retains the sigma-finite hypothesis and uses restrictions to finite-measure
sets before subtraction, matching Theorem A.1.5. The arbitrary-outer-measure
claim is supported by the source's remark after Lemma A.1.7 and by the supplied
proof. Completeness of the larger splitting domain is proved separately;
the Borel restriction is not declared complete.

The complement-placement correction was independently checked against the
whole source p. 459 and its preceding definition on p. 458. The last display
of Lemma A.1.6 prints mu*(F^c intersect A), after splitting each covering Bi
into Bi intersect A and Bi intersect A^c. The required second covered set is
F intersect A^c. The new annex's T setminus A at 214-235 is that correct set.
This conclusion comes from the actual source display and covering argument,
not merely the author intake's assertion.

The full Stieltjes proof at annex 274-413 retains finite real values at finite
arguments, monotonicity, right continuity, allowed infinite interval endpoints,
finite refinements and the countable cover inequality. Its clipping step
justifies the source's bounded-cover reduction; compactness is proved from
real completeness. Unbounded target increments are obtained from endpoint
limits before a measure exists. Thus no circular use of measure continuity
enters the extension. The Lebesgue specialization, trace probability space,
translation invariance and endpoint null sets have complete supplied proofs.

The quantile in body 269-319 is precisely the source's supremum of the strict
sublevel set. Annex 470-551 proves finiteness, both ray-equivalence directions,
measurability and the law on the constructed (0,1) space. Right continuity and
both tails remain explicit; neither ordinary invertibility nor positive mass
at every value is imposed. The jump-fiber and flat-portion refinements and the
non-sigma-finite nonuniqueness example are proved handbook deductions.

The actual accepted measurable-probability definitions of measures/sums,
continuity, Borel generators, measurable maps, pi/lambda systems, the pi-lambda
theorem and CDF uniqueness were read at their live body locations. These are
used within their declared domains. Full rereview of their earlier annex is
not claimed. Integration and product-measure results beyond this unit remain
outside this verdict.

## Finite bets and subjective probability: PASS

Body 23-64 retains the source's complete finite real payoff space and all three
conditions. The continuity definition matches source C1 on printed p. 16;
the source's weak monotonicity means strict improvement in every state, and
additivity permits an arbitrary common vector. The text does not replace these
by one-state strict monotonicity or sure-cash translation alone.

The source p. 103 separates U={x:x weakly preferred to 0} and D={x:0 strictly
preferred to x}. Body 123-130 explicitly identifies the annex's alternative
cash-equivalent construction. The full annex 4-158 constructs that functional,
including existence, uniqueness, additivity, the Lipschitz bound, rational-to-real
homogeneity and normalization, then verifies precisely those two separating
halfspaces. Thus the source theorem is retained while the proof method is
identified accurately. The unique probability weights, zero-weight states and
one-state case follow from the supplied proof; the finite P15 expectation
definition was checked at its actual location.

Body 209-253 and annex 187-240 explicitly specify the all-event, signed,
finite-portfolio contract model. The equivalence between its strict sure-loss
criterion and probability quotes is proved as a handbook consequence. It is
not attributed to the exact source claim. The distinction from the source's
dynamic exchange cycle on pp. 100-101 is accurate. The stronger nonpositive
portfolio exclusion retains its strictly positive atomic-weight hypothesis.
The nonlinear example's premise failure and numeric comparison were read and
checked; it does not claim that nonlinear expected utility precludes beliefs.

## PA original evidence construction and selected D3: PASS

This is an internal construction from the actual accepted arithmetic definitions,
not a newly quoted external theorem. The selected predicate is exactly the
one in `parts/p05/pa-checker-arithmetization.tex:396`: Prf19(p,x) is
Gamma_d19(p,x,1), and Prv19(x) is its proof existential. The new body 465-507
fixes the original P19/g19 codes before substitution, and the final proof at
annex 908-984 returns D3 for that same predicate and numeral convention.

The full five result/proof pairs were checked against the governing definitions:

- Body 92-137 / annex 4-141: h(Sz),t(Sz) invert the original zero-based pairing;
  the beta least-search fold uses bound Sz and a success flag distinct from
  saved value zero. All positive evidence clauses match the existing evidence
  construction, including its bounded-leaf priority, finite collection and
  dependent witnesses.
- Body 139-260 / annex 143-394: the positive raw builders consume the actual
  pair/tag/beta evidence. The marked-universal list has a proved entry invariant
  and is fed to the accepted arbitrary-matrix U constructor. The output contains
  range exhaustion, equality transport, original-guard discharge and universal
  introduction. The original code, Safe invariant, sentence bit and all actual
  tag-19 factors are addressed.
- Body 262-463 / annex 396-706: the general original closed-Sigma-one promise
  is supplied. The signed normal forms match the governing hierarchy conversion.
  Signed children are qualified by that syntax; the two excluded unbounded signs
  would leave an unbounded universal in a Sigma-one formation. Both signs of
  every Boolean connective, positive unbounded existential, negative unbounded
  universal and all four marked cases have specified raw constructors. The
  bounded priority case uses the explicit internal Boolean identities S1-S3 to
  return to the original bounded formula. The negative marked existential uses
  two copies of its minor, removes both marker-2 leaves, and selects its fresh
  y above every original existential index and above the nine allowed axiom
  indices. These conditions match the actual all-variable rule. Each original
  root is supplied directly; no unspecified normal-form bridge proof is assumed.
- Body 465-526 / annex 708-906: the actual original Gamma construction has
  exactly the positive marked formation asserted. Initial equalities,
  composition, nullary composition, recursion's initial entry, bounded step
  with two entry witnesses, final beta entry and outer trace existential are
  covered. The original computation trace and collected evidence sequence stay
  distinct. The original second beta term S(k) and all fixed graph binders are
  retained. The fully expanded numerical checker descriptions add no new
  formula-level negation to those graph clauses.
- Body 528-546 / annex 908-984: internal evidence existence and the proved
  builder invariant yield the exact original provability sentence code c_phi;
  the final existential introductions and eliminations meet the stated
  nonvacuity and freshness conditions. D1/D2 are those of the same selected
  graph. No D3 premise, consistency premise, varying-description evaluator or
  transfer from an arbitrary numeralwise representative enters this proof.

The actual dependency text read included all of `inherited-08306-08438.tex`
(hierarchy), all of `inherited-09262-09327.tex` (Gamma and evidence statement),
`inherited-08439-08709.tex:1-130` (original P/B and coding interface),
`annex/p05/internal-proof-predicate.tex:51-233,310-415` (internal pair/beta,
extension, collection and every Ev clause), the full standard-PA body,
checker body 1-122 and 281-523, numeral body 1-220 and annex 206-322, and bounded
body 1-107 and 259-486 with annex 271-423. Older proofs outside these extents
were treated as accepted prerequisites, not newly rereviewed conclusions.

The bounded, numeral and checker body/annex hashes and the governing hierarchy,
P/B, Gamma and internal-evidence hashes all match the dependency hashes in the
new intake. In particular bounded body/annex remain
`8345A3C2C7702A5DD039BA6068CEBD7C0B69D2ABE387FB6FDFB29A5E46AFE480` /
`0C3D2614397C7CF68D4B32E0179E4A023EB460A8815EAE67E58836326DFA260A`,
and Gamma/evidence-definition file remains
`B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB`.

## Integration checkpoint and review limits

Final shared-file snapshot: **PASS for source meaning and input placement**.
The root supplied its final hashes, and all matched the live files. The P5
body/annex inputs follow the accepted bounded builders; Kamp Lemma 5 follows
Lemma 4 in both routes; P15 follows measurable probability; P17 follows risk
aversion. The new inputs were inspected in those eight route files.

The registry parses as 1,122 records. Every new record at physical lines
1096-1123 was read, together with the changed older records at physical 939
and 942. Their scopes and descriptions preserve the actual source domains,
the original Sigma-one evidence construction, literal graph selection and
D1-D3 scheme. Neither revised older record asserts an internal transfer to
an arbitrary numeralwise or certified-proof representative. All 30 relevant
candidate-table entries and their candidate-index mappings were read; their
meanings agree with the registry. The remaining unrelated apparatus entries
were not reviewed again. This is a text check of the candidates, not their
typeset or admitted state.

| Shared file | Final SHA-256 |
| --- | --- |
| `handbook/registry/symbols.csv` | `D0F3B085CC5AD9CA62419DEEC804C820CD4A0B92A9BDD7558742F4AABC96D755` |
| `handbook/bib/handbook.bib` | `BD462E1E3BC9B6E6C1AA40B30E4E7C23A6B4533FA196EDD43B881F8C7757FA59` |
| `handbook/parts/p05.tex` | `6EA790CF41F1671DD5F999403C3D7FC8350329B36A1AF2D8A6B491513C21362C` |
| `handbook/annex/p05-route.tex` | `5FE64A4257974D3DAD547CF2F07B2F018FB803626DF1655836DA2D34E59E363B` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `68AC755FF0A84BF23AC1C0BE4CCB2BA6F0888B5EF3E72892AE684E7AB792F6CA` |
| `handbook/annex/p09.tex` | `DE1903830EC8C5EE6E002A1A796D537A72D85B6FBE1127333798775CE6D4F906` |
| `handbook/parts/p15.tex` | `78D9FEF22C2EA0B43782BA52128CF993153F790108149684D860F94214681ACF` |
| `handbook/annex/p15.tex` | `9505B528969CA51B2BD40175B16FDB8BFA6B9AD64F36B92927D820BC49B81DB2` |
| `handbook/parts/p17.tex` | `C43B6F3D62FD1C7A29E31B1FE6721D5C2AF9444BCC23B7FBD59D471831D9C764` |
| `handbook/annex/p17.tex` | `5C3048BCCDBA8D79C22700705B9480D79E5BB1D6C7CBA29F1D9C80D04D51FE5B` |
| `tmp/edition-2026-bounded-kamp4-probability-decision/evidence-extension/symbols-tables.tex` | `ED71907AB47A0572E19945B2B8F36062C2799584BD4279661B1471F9B82D4F6B` |
| `tmp/edition-2026-bounded-kamp4-probability-decision/evidence-extension/symbol-index.tex` | `9792C9416BB9B7BD275D6349C5AFE003A41E5C551E3014EFD000D9F7DBA9721B` |

All eight target hashes were checked again after their complete reading and
remained equal to the frozen values above. No source-fidelity item remains
unresolved in the assigned scope. The approximately 15-minute checkpoint
reported the completed target reading and the then-pending shared snapshot;
that final snapshot has now been checked within the assigned 45-minute bound.

The PDF skill guided direct source-page inspection; the research skill guided
primary-source tracing and this single report. The assignment's no-subagent
scope controlled research delegation. No source or manuscript was edited;
no source was downloaded. No manuscript test, build, render, generator,
provenance admission or acceptance-record mutation was performed. This report
does not supply those separate production or admission gates.
