# P18 / A4: original dynamic-game completeness and a full-domain correction

Authoring result: the original finite single-response completeness claim is
refuted by a complete rule-generated countermodel. The corrected sequential
licensing game is proved sound and complete for the original set-sized dynamic
theory domain, with well-founded winning strategies; finitary theories have
finite winning proof trees. The original support-compression obligation is
closed by counterexample, not left as an unproved lemma.

Seven reciprocal statement/proof pairs are supplied. No independent review,
scanner, test, build, or manuscript PDF render was performed. Root owns shared
integration and the preceding chapters.

## Exact primary versions and read extent

The same held primary versions are used:

- source/references/lis-burdens-a4-primary/prakken-sartor-dialectical-1996.pdf:
  Henry Prakken and Giovanni Sartor, A Dialectical Model of Assessing
  Conflicting Arguments in Legal Reasoning. Title-page date July 19, 1996;
  separate footer pratorkl.tex; 26/09/1996; 13:52. 43 author pages,
  314925 bytes. SHA256
  34743F348C3630867F8BB302AA01A5323EBEEBDA98BBEE454E8F1CE24C6ED5E5.
  Author source:
  https://webspace.science.uu.nl/~prakk101/pubs/DefArgAILaw96.pdf.
  Existing key: PrakkenSartor1996Dialectical.
- source/references/lis-burdens-a4-primary/prakken-sartor-priorities-1997.pdf:
  Henry Prakken and Giovanni Sartor, Argument-based extended logic programming
  with defeasible priorities. 52 author pages, 386869 bytes; published
  presentation JANCL 7, 25–75 (1997). SHA256
  EC4F092B180E47463595750A71B431BE57B8A92EFDB1844B5F030B76551AE472.
  Author source:
  https://webspace.science.uu.nl/~prakk101/pubs/DefArgJANCL97.pdf.
  Existing key: PrakkenSartor1997Priorities.

All 43 main-source and 52 companion pages were read in the preceding blocks.
This block reread the complete companion pp. 30–31 and 46–47, including
Definitions 6.1–6.2, Propositions 6.3–6.5, the full Lemma 10.3 and
Proposition 6.4 proof continuation. It also reread main-source pp. 25–27,
including its full dynamic dialogue and tree definitions. The prerequisite
dynamic formulas and proved interfaces were read directly from the actual
LaTeX. Source page images were used to preserve the mathematical symbols;
no manuscript pages were rendered.

The 1996 main source's forthcoming-companion citation and the companion's
own cross-reference suffix do not identify the same title by suffix alone.
The titles, held files and hashes above are the source identifiers.
No additional primary capture or source key beyond the four combined-intake
entries is required.

## Frozen target and disposition

| Exact target | Disposition |
|---|---|
| Original one-argument, self-priority defeat/neutralization response | Fully retained for the counterexample calculation |
| Companion Proposition 6.3 soundness | Prior proved source-game soundness remains valid; the new counterexample does not challenge it |
| Companion Proposition 6.4 finite completeness | Refuted even without global minimality and even if proponent repeats are allowed |
| Lemma 10.3 finite priority support | Its finite-information component is retained; it does not prove rank-preserving argument amalgamation |
| Proposition 6.4 pp. 46–47 earlier-stage merger | Exact inference refuted: the selected legal merger is incoherent and never justified |
| Main-source finitary carryover wording | No unrestricted finitary extension of the refuted original finite claim is valid |
| Corrected single-argument-per-move dialogue | Full state, transition, return, support and outcome definitions supplied |
| Corrected full-domain correspondence | General soundness, general well-founded completeness and determinacy proved |
| Finitary and finite proof regimes | Finitary finite winning trees; finite-ground decision construction proved separately |
| Source subargument consequence | Corrected proof closure follows explicitly from semantic subargument closure and the new correspondence |
| Dynamic reversed-role status construction | New fully specified attack-witness protocol, with exact source overruling/defensibility correspondence |

The newly supplied game is not attributed to Prakken and Sartor. It retains
their arguments and semantic G operator and explicitly changes the dialogue
protocol. The previously written support-explicit certificate procedure is
neither its definition nor a surrogate presented as the original theorem.

## Countermodel and exact failed inference

Use eight defeasible rules:

u: => a; v: => b; t: => c; z: => d;
m: => not c; n: => not d;
p: a => m < t; q: b => n < z.

The ordinary strict rules are a,b -> not a; c,a -> not c;
d,b -> not d. Include all ground instances of the exact four
priority schemata over the finite name vocabulary. No ordinary
contraposition closure is imposed, in accordance with the source domain.
There are no weak premises or strict facts.

Let P=[u,p], Q=[v,q], Z=[z], A=[t,z], B=[m,n].
The complete producer analysis proves:

- [], [v], Q enter J1; [u], P, Z enter J2; [t], A enter J3.
- P and Q are compatible as separate arguments, but any argument containing
  both positive priorities includes a,b and is incoherent.
- B is coherent and defeats A under empty priority support.
- Neutralizing B requires both priorities in the response, hence incoherence.
- Strictly self-defeating B requires c or d. The reverse conflict then
  forces the corresponding priority into that response, which also
  introduces a or b and yields an ordinary strict contradiction.
- Thus every legal response is incoherent; the opponent plays [] and wins,
  because the designated incoherence defeat is not neutralizable and
  nothing defeats [] in this strictly consistent base.

For the exact pp. 46–47 step, Z strictly defeats B relative to Q, B does not
attack Q, and Z+Q=[z,v,q] is legal and strictly self-defeats B. Nevertheless
Z+Q is incoherent and outside every justification stage. Q is in J1 and Z
is in J2; no J1 argument conflicts with B. Thus the proof's earliest-conflict
selection does not restore the claimed earlier-rank conclusion.

An optional additional default u': => a proves that allowing alternative
head producers does not repair the example. Each legal argument still
chooses one producer; all contradiction arguments remain valid.

## Corrected protocol: every changed rule

The state has a branch-local licensed list and a stack of suspended claim
hearings. Each opponent challenge remains an actual D_empty defeater.
Each proponent move names exactly one legal source argument.

1. A fresh hearing suspends the current challenge and asks the opponent
   to challenge the auxiliary argument.
2. A closed hearing licenses its claim and returns to the same suspended
   challenge; it does not automatically close the parent.
3. A resolution cites one licensed argument and uses the priorities of the
   entire licensed list for strict defense or neutralization.
4. Global minimality is removed.
5. A fresh hearing cannot repeat a pending or licensed claim. Licensed
   arguments may be cited repeatedly; shared subarguments and repeated heads
   across different entries do not merge their contents.
6. An infinite proving play is a proponent loss.

Raw comparison formulas are defined for arbitrary recorded lists. Soundness
does not assume that an arbitrary cooperative play licenses only J members.
Instead an explicit opponent strategy maintains that invariant and prevents
every non-J claim from closing. The separate cooperative-play example shows
why one finished transcript must not be mistaken for a winning strategy.

Completeness uses the semantic entry ordinal of the active claim. For the
opponent's single chosen challenge, finite priority dependence supplies
finitely many earlier justified witnesses. They are heard sequentially;
strict stability and defeat antitonicity justify the final response after
return. Every nested hearing has smaller entry rank. This handles repeated
heads, shared trees and arbitrary strict consequences without any merger.
The finite-tree conclusion is proved by finite branching plus the complete
elementary no-infinite-branch argument.

## Reciprocal proof map

Chapter label: sec:p18-is-dynamic-completeness.

| Body theorem | Annex item | Result |
|---|---|---|
| thm:p18-is-compression-countermodel | annex:p18.is-compression-countermodel | Complete original-game countermodel, all response forms, alternative producer |
| thm:p18-is-compression-rank | annex:p18.is-compression-rank | Exact earlier-rank amalgamation failure |
| thm:p18-is-licensing-sound | annex:p18.is-licensing-sound | General soundness and opponent strategy |
| thm:p18-is-licensing-complete | annex:p18.is-licensing-complete | Full transfinite-rank completeness, determinacy and subargument closure |
| thm:p18-is-licensing-finite | annex:p18.is-licensing-finite | Finitary finite proofs and finite-ground decision procedure |
| thm:p18-is-licensing-worked | annex:p18.is-licensing-worked | Full repaired exchange, shared support and cooperative-play boundary |
| thm:p18-is-licensing-reversed | annex:p18.is-licensing-reversed | Dynamic attack-based overruling and residual defensibility |

## Integration intake and remaining separate obligations

The original author block owned the new body, matching annex and this note.
This chapter is now routed as P18.17 after sec:p18-is-dynamic.
The preceding LIS/IS reader pointers and source notes now link the
conclusive countermodel and corrected correspondence instead of
calling the compression and finite/finitary questions open.
The previous source game's soundness proof and finite-information lemma
remain unchanged prerequisites. Integration updates their reader pointers
and source records rather than altering those proofs.

Local notation intake: player labels P_pl/O_pl; licensed ordered list L;
its entry set |L| and explicit E_L/D_L abbreviations; active and suspended
frames (C,B); Hear, Defend,
Neutralize move tags; source semantic entry ordinal rho(C).
All source D_X/E_X/G/J notation is retained. Countermodel capital P/Q
are arguments and are explicitly distinguished from the players.
No citation beyond the four requested LIS/IS keys is needed.
The combined symbol intake is handbook/registry/symbols-intake-p18-lis-is.csv
with P18.14–P18.17 scopes, meta precedence and exact first-use labels.
The combined bibliography intake is handbook/bib/intake-p18-lis-is.bib.
Canonical symbol/bibliography merging and progress are root-owned.
The E_L abbreviation already used in the worked game is now explicitly
defined beside D_L at def:p18-is-licensing-state.

The exact support-compression obligation is closed. The corrected dynamic
attack-status protocol is also supplied, with general strategy and finite
decision scopes distinguished. A bare player swap in the old self-context
game is not silently claimed complete.

The separate sensitive direct-exclusion semantics remains refuted in its
old form and needs an explicit semantic redesign if retained. The historical
non-semidecidability coding and separate stable-semantics comparison chain
remain as previously recorded; this assignment does not count them completed.
No theorem here claims a finite negative certificate for every infinite-domain
defender win, or derives effective enumeration merely from finitariness.

The research and PDF skills guided exact source/version reading. One whole
author read-through of the completed body and annex was completed. Direct
corrections make the soundness statement explicitly quantify over winning
strategies and distinguish the licensed list from its entry set. This was
the authoring check for this return. No acceptance review is claimed.
