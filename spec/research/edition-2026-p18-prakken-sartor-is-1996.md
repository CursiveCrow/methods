# P18: original Prakken–Sartor IS construction

## Author block and actual return

Block began 2026-09-09 at 05:01 UTC.
Owned body and annex: handbook/parts/p18/prakken-sartor-is-1996.tex
and handbook/annex/p18/prakken-sartor-is-1996.tex.
Root owns shared files and all earlier returns.
The build/review-2026-09-08-2130 tree was not edited or used in this block.

This is a bounded FIXED-PRIORITY return, not completion of the full
1996 source assignment. It supplies ground rules, arguments, strict
extensions, relevant frontiers, the source set lift, generated defeat,
fixed-point semantics, full structural proofs, a corrected finite proof
game, its soundness/finitary completeness proof, a finite-ground decision
method, and the exact fixed-role LIS justification bridge.
Nine reciprocal theorem/annex pairs are provided.

The original global-minimality game is not falsely called complete.
A full finite, rule-generated countermodel is supplied. The corrected
reader game retains the actual source defeat construction while removing
that invalid global reply restriction.

Integration status: routed as P18.15 with its nine-pair annex.
P18.16 now supplies the reversed-role fixed-comparison game, dynamic
operator, priority examples and applicability alternatives with their
proved limits. P18.17 resolves the original dynamic completeness claim
by counterexample and a corrected sequential protocol.
The exact unrestricted implementation coding, sensitive-exclusion
redesign and broader stable-semantics comparisons remain separate.

## Exact primary source and complete read

File:
C:/Dev/the-methods-of-reason/source/references/lis-burdens-a4-primary/prakken-sartor-dialectical-1996.pdf

- Title: A Dialectical Model of Assessing Conflicting Arguments in Legal
  Reasoning, H. Prakken and G. Sartor.
- Title-page date: July 19, 1996.
- Page footers separately show pratorkl.tex; 26/09/1996; 13:52.
  Both are recorded; neither is silently substituted for the other.
- Held author layout: 43 pages, 314925 bytes.
- SHA256: 34743F348C3630867F8BB302AA01A5323EBEEBDA98BBEE454E8F1CE24C6ED5E5.
- Original URL: https://webspace.science.uu.nl/~prakk101/pubs/DefArgAILaw96.pdf
- Proposed key: PrakkenSartor1996Dialectical.
- Read ALL pages 1–43, including all examples, notes and references,
  directly from source-page images because the text encoding is damaged.
  These images are reading aids in the thread scratch folder.

Complete source map:

- pp. 1–5: scope, five framework components, logical/procedural distinction.
- pp. 6–8: head conflicts, priorities, weak assumptions, applicability.
- pp. 8–10: Definitions 4.1–4.3, ground-instance language and rule sequences.
- pp. 11–14: Examples 4.4–4.10, strict extensions, coherence, conflict freedom.
- pp. 14–17: Definitions 4.14–4.17, relevant rules, strict set lift,
  rebuttal, undercutting and empty incoherence defeat; Example 4.18.
- pp. 17–25: fixed-priority status and finite proof trees; Definitions
  5.3–5.6, source examples, reversed-role discussion and exact proof referral.
- pp. 25–31: dynamic-priority language, four strict priority axioms,
  Definitions 6.1–6.3, neutralizing moves, examples 6.4–6.5.
- pp. 31–33: applicability representations, Definition 7.1, implementation.
- pp. 34–40: related approaches, qualification of comparisons, conclusion.
- pp. 41–43: notes and references; note 4 makes order irrelevant except
  for premise-before-conclusion, and reference p. 42 identifies the
  technical companion.

## Actual companion proof dependency

File:
C:/Dev/the-methods-of-reason/source/references/lis-burdens-a4-primary/prakken-sartor-priorities-1997.pdf

- Title: Argument-based extended logic programming with defeasible priorities.
- Authors: Henry Prakken and Giovanni Sartor.
- 52 author pages; 386869 bytes.
- SHA256: EC4F092B180E47463595750A71B431BE57B8A92EFDB1844B5F030B76551AE472.
- URL: https://webspace.science.uu.nl/~prakk101/pubs/DefArgJANCL97.pdf
- Proposed key: PrakkenSartor1997Priorities.
- The 1996 main source calls this Prakken–Sartor 1996b, forthcoming in
  Journal of Applied Non-Classical Logics. The later bibliographic record
  in Prakken 2001 gives volume 7, pp. 25–75 (1997).
- The initial block read pages 1–32 and 39–52. P18.16 subsequently read
  pp. 33–38, completing all 52 pages; P18.17 reread the complete
  dynamic-game definitions and pp. 46–47 proof continuation.
- Necessary source passages read completely: fixed semantics §§3–4,
  dynamic definitions §§5–6.1, Appendix pp. 43–49, and references.
- Fixed semantic statements: pp. 15–17, Propositions 3.3, 3.6–3.8.
- Fixed game: p. 24, Definitions 4.5–4.8 and Propositions 4.9–4.10.
- Dynamic game: pp. 30–31. Its Proposition 6.4 says FINITE theories,
  while the 1996 paper suggests that the preceding finitary scope carries
  over. P18.17 resolves the distinction: the original finite claim is
  refuted, while the corrected game is complete generally with
  well-founded strategies and has finite proofs for finitary theories.
- Appendix proof chain read: Lemmas 10.1–10.3 and the source
  soundness/completeness/subargument proofs, pp. 43–47.

## Corrections and mathematical evidence

1. Relevant frontiers are defined recursively on the whole argument.
   This supplies the strict-fact empty case and strict producers already
   in the original prefix, which the printed suffix-based clauses do not
   explicitly cover despite the source's own examples.
2. Rule contents use unique producing heads and no redundant repeated
   occurrence. Duplicate identical rules can be deleted without changing
   conclusions or assumptions; valid reorderings are identified for
   content-based repetition/minimality, following note 4.
3. Defeat need not imply attack in the designated empty/incoherent case.
   With S empty and rules ⇒a, ⇒not-a, the empty argument defeats their
   incoherent combination without attacking it. The reader states the
   qualified implication, not the companion's unqualified Corollary 2.17.
4. The main game's global minimality requirement fails even for a finite
   ground theory. The complete countermodel uses S and priorities empty:
   r1:⇒a; r2:⇒b; r3:~b⇒not-a; r4:~a⇒not-b.
   Every subset is a valid argument content. C={r1,r2} is undefeated
   because it undercuts every contrary attacker. Thus C and its singleton
   subarguments are semantically justified. Starting with r1, an opponent
   forces r3, r2, r4, after which the only globally minimal strict
   defender repeats r1. C would protect it but is not globally minimal.
5. This matches a specific proof gap: the companion's pp. 46–47
   construction selects a minimal defender WITHIN an earlier justified
   stage. That does not establish the displayed GLOBAL minimality in
   Definition 4.5. The proof-theoretic subargument construction on
   pp. 45–46 likewise can introduce a reply that is not globally minimal.
6. The reader directly removes global reply minimality, retains
   proponent nonrepetition, and proves soundness generally and finite
   proof completeness under the source's finitary hypothesis.
   This corrected theorem is not attributed as a valid theorem of the
   unrepaired game.
7. The original attack-based overruled label is distinguished from later
   defeat-based labels. The empty-incoherence clause means its residual
   defensible class can contain incoherent arguments. No epistemic
   endorsement or classical truth claim is inferred from that label.
8. Finite GROUND rule data, rather than finitely many written schemata,
   is the input to the proved decision method. Function-bearing schemata
   can generate infinitely many argument contents.

## Nine reciprocal proof pairs and source map

Body thm:p18-is1996-SUFFIX; annex annex:p18.is1996-SUFFIX:

- closure: finite strict derivations versus strict extensions; hereditary
  conclusions/assumptions; deletion of repeated identical producers.
- frontier: unique finite relevant-rule recursion, including empty cases.
- set-priority: exact existential/universal strict lift, transitivity,
  irreflexivity, asymmetry, and empty-frontier comparisons.
- orientation: every attack yields some defeat direction; exceptional
  empty defeats; inherited attacks; strict-base inconsistency.
- semantics: full least-fixed-point construction, finite approximation
  and finitary equality, attack conflict freedom, subargument closure,
  strict-base inconsistency. Includes a proved ordinary/strict-defense
  fixed-point equality rather than an assumed Dung substitution.
- proof-correctness: full upward soundness and descending finite-rank
  completeness for the corrected game, with all opponent branches.
- minimality: complete four-rule source-system countermodel.
- finite: finite-ground enumeration and decision method with proof.
- lis-bridge: justification correspondence for the actual generated
  defeat relation; no automatic single-target changing-role conversion.

The proofs are independent complete derivations informed by the read
source proof routes. No unproved original claim is assigned a proof label.
The general set-sized constructions use classical set theory with choice.

## Integration and continuation

Main label: sec:p18-is1996.
Cross-reference: sec:p18-lis-burdens and thm:p18-lis-grounded-game.
Local notation: S, D, prec for the theory; Con/Ass; C_S; R_L;
prec_*; U/R/D_Gamma; J_Gamma/F_Gamma; finite proof tree and finitary.
Root handles canonical bibliography and symbols. The original author
block edited no shared file; this integration block routes P18.14–P18.17
and supplies separate combined symbol and bibliography intakes.

P18.16 supplies the conflict-free domain of the evolving-order operator,
its complete semantic proofs, both applicability approaches and the
priority examples. P18.17 supplies the conclusive source-game
countermodel and corrected sequential dialogue, including the exact
general/finitary distinction and a dynamic attack-status protocol.
The Dung report version dispute and the independently broader 1997
stable/model-theoretic comparisons remain separate.
The sensitive direct-exclusion semantics and exact historical
non-semidecidability coding also retain their explicit obligations.
Combined intake paths are handbook/registry/symbols-intake-p18-lis-is.csv
and handbook/bib/intake-p18-lis-is.bib. Reader pointers now identify the
completed continuation instead of calling it pending.

## Authoring record

Research and PDF skills guided exact source reading and this durable note.
One complete author read-through of body, annex and note was completed
after the saved batch. It clarified the set-theoretic setting, the
source-specific undercut terminology and the actual contrary conclusions
in the earlier-support example. The initial proponent move is distinguished
from replies, following the companion's explicit i > 1 qualification.
No independent review, scanner, tests, compiler, manuscript PDF generation
or manuscript PDF inspection was performed.
