ACCEPT

# Integrated N-c-014 source-fidelity review — Round 3

## Verdict and bounded strength

The actual integrated presentation in `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1770, is source-faithful, mathematically coherent at the strength claimed, explicit about every source-version boundary, and correctly integrated into the actual host passage in `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--946. I found no concrete must-fix.

This acceptance is deliberately bounded. It accepts:

- the Büchi material only at complete September 1959 UMR1083 report-precursor strength, with the report's printed defects and the handbook's repairs distinguished;
- Elgot at complete 1961 journal-article strength as controlled by the published 1962 errata, with the 1959 UMR1342 report kept as a distinct precursor;
- Trakhtenbrot at the separately stated strengths of the complete 1961 announcement and complete 1962 expansion;
- Rabin at complete 1969 article strength, with Meyer's later complexity correction assigned only its corrective role; and
- Thomas only at complete May 1996 Kiel report-precursor strength.

It does not close the open reconciliation of Büchi's 1959 report against the registered 1960 journal article, and it does not close the open reconciliation of Thomas's 1996 report against the registered 1997 chapter. Those two open obligations are stated in the manuscript and the permitted acquisition ledger and are reasons for the final open register status, not reasons to reject the bounded presentation.

## Review protocol and evidence boundary

I read the replacement snapshot of `n-c-014.tex` directly and completely from line 1 through its actual EOF at line 1770. I then read the host file directly from line 836 through line 946, including the actual `\input{parts/p09/presentations/n-c-014}` at host line 937.

I also read every line of each of the five permitted source notes:

- `spec/research/p09-buchi-1960-source-note.md`, lines 1--367;
- `spec/research/p09-elgot-1961-source-note.md`, lines 1--423;
- `spec/research/p09-trakhtenbrot-1961-source-note.md`, lines 1--583;
- `spec/research/p09-rabin-1969-source-note.md`, lines 1--665; and
- `spec/research/p09-thomas-1996-report-source-note.md`, lines 1--353.

Within `spec/research/p09-source-presentations-lot2-3.md`, I used only the permitted integrated N-c-014 section, lines 681--745, and the consolidated acquisition-status ledger, lines 965--982. I inspected the relevant entries in `handbook/bib/handbook.bib`, including `McNaughton1966`, `Thomas1996Report`, `Thomas1997`, `ComonEtAl2007`, `Elgot1961`, `Elgot1959Report`, `Elgot1962Errata`, `Meyer1975Complexity`, `Rabin1969`, `ThatcherWright1968`, `Trakhtenbrot1961`, `Trakhtenbrot1962Expanded`, `Buchi1959WeakReport`, `Buchi1960`, and `BruyereEtAl1994`.

I did not inspect any manuscript PDF, page image, render, crop, PNG, or other derivative. I did not run TeX, a build, a test, a checker, a repository script, a hash operation, or any automated validation. I did not open any prior N-c-014 review, board, admission, chair, or reconciliation record. No original historical-source page was needed: no concrete ambiguity remained after comparison of the actual LaTeX with the five permitted full source notes, the permitted compact record portions, and the bibliography identities. Accordingly, there is no historical-page consultation to document.

## Source identity, hierarchy, and locators

### Büchi

The manuscript gets the controlling limitation right at first use. Lines 8--16 identify the registered object as the 1960 journal article, identify the complete reconstruction body as the September 1959 UMR1083 precursor, cite both identities, and expressly decline to claim identical wording, numbering, examples, or proof detail. All substantive page and theorem locators in the Büchi presentation point to `Buchi1959WeakReport`, not to unread journal pages. The bibliography keeps `Buchi1959WeakReport` and `Buchi1960` as separate entries with the correct report identifier, date, journal volume, issue range, pages, and DOI.

This matches the source note's authority rule: the 1959 report supplies the complete precursor development, while `Buchi1960` controls only the registered journal identity until the body is reconciled. Manuscript lines 971--973 repeat the precursor-strength boundary before moving to the later Thomas construction. No journal-version claim is inferred from the report.

### Elgot

Lines 232--237 place the complete 1961 journal article first in the authority order, retain UMR1342 as a primary precursor, and give the published 1962 errata control over corrected formulae. The substantive article locators use the journal's actual pp. 21--51, while lines 559--569 use report pp. 4, 6, and 41 only for the explicitly described version comparison and use errata pp. 558--559 for correction ownership. The bibliography separately and correctly records the 1961 article, the 1959 report, and the 1962 errata; in particular, the article page range is the corrected 21--51 rather than 21--52.

### Trakhtenbrot

Lines 571--581 distinguish the four-page registered 1961 announcement from the twenty-nine-page 1962 expansion, preserve the different official Math-Net English title renderings, and assign announcement theorem/page claims to pp. 326--329 and expanded-development claims to pp. 103--131. Lines 971--977 later summarize the two bodies at their distinct strengths and disclaim a complete line-by-line translation. The bibliography likewise preserves “Single-Place” for 1961 and “One-Place” for 1962 rather than silently normalizing the official records.

### Rabin and the later complexity correction

Lines 1038--1040 make Rabin's 1969 article control the historical definitions, numbered results, and original proof architecture. Lines 1069--1091 identify Definition 1.1, Theorem 1.1, and Theorem 1.12 at the correct source locations. The manuscript accurately reports Rabin's elementary-recursive claim as a historical claim and then refuses to retain it in light of Meyer's later lower bound, with the correction confined to complexity and not allowed to displace Rabin's decidability or proof architecture. `Rabin1969` and `Meyer1975Complexity` have distinct, accurate bibliography entries.

### Thomas

The finite-word Thomas passage begins at lines 979--993 by calling the acquired body a 1996 report precursor and citing `Thomas1996Report`. Lines 1029--1034 prevent that modern construction from replacing Büchi, Elgot, or Trakhtenbrot. The infinite-tree Thomas passage begins at lines 1616--1618 by identifying Sections 6.1--6.2 as a later game-theoretic construction assembled from post-1969 work, and lines 1765--1770 expressly state that all Thomas locators belong to the May 1996 report rather than the registered 1997 chapter. The bibliography contains separate `Thomas1996Report` and `Thomas1997` entries with correct report and final-chapter standings.

## Claim/source correspondence and proof ownership

### Büchi's weak language, automaton, and finite-word result

Lines 18--29 correctly define weak second-order arithmetic as an interpreted monadic language over natural numbers with finite-set predicate quantification. Lines 31--71 give the source's actual propositional-formula automaton data `E,H`, its typed transit recursion, the exact pointwise special-output identity, and eventual-truth behavior. The manuscript does not replace this object with a modern nondeterministic finite automaton and keeps formula data, input predicate, transit predicate, output predicate, and behavior set at distinct standings.

Lines 73--142 correctly separate synthesis from analysis. They report Theorem 1's sound formula-to-automaton construction, expose why printed formula (2) cannot establish Theorem 2 under printed Definition 2, give the decisive one-bit counterexample, and then state a finite-witness correction. The correction is mathematically adequate: the downward-closed finite cutoff has a last true point; the run is constrained through that point; the input is forced false from the boundary onward; and the special-output identity propagates the boundary truth along the omitted tail. Lines 140--142 expressly call this a handbook-owned emendation rather than Büchi's printed formula.

Lines 144--169 reproduce the terminal-marker encoding with the empty-word case, distinguish arbitrary-output string behavior from eventual behavior, and give the source's Theorems 6--8 at their actual four-way strength. Lines 171--230 preserve the displayed last-true-point convention against the report's conflicting length prose, include the necessary false-tail guard and inclusive finite search bound in the decision proof, preserve ultimate periodicity, and distinguish the false unary-power-predicate equivalence from the later correct `\in_2`/`V_2` signature. The manuscript does not silently repair Büchi's Theorems 4 and 9 or overclaim what Corollary 5 needs.

### Elgot's finite-set correspondence and design construction

Lines 239--257 give the correctly typed source acceptor `(S,f,d,D)`, with `I` as input alphabet and `S` as the finite internal-state set, including the exact empty-word convention. Lines 259--330 define `L_1^1`, the canonical admissible characteristic-column encoding, and both effective directions of Theorem 5.3. Coordinate deletion is correctly followed by right truncation, and the reverse construction gives start, terminal, and adjacency constraints before existentially projecting the state coordinates.

Lines 346--373 separately define the `A/B` transducer and state all four conditions of Theorem 7.1. The replacement fixed-point passage at lines 375--420 now closes the earlier initial-prefix gap and is correct:

1. `d\in D` at line 401 is exactly the condition that the empty paired word belongs to `\gamma`.
2. `I_\infty(a)` is exactly defined at lines 396--400 as the set of first output letters whose first transition enters a stable retained triple.
3. Requiring `I_\infty(a)\ne\varnothing` for every first input letter at lines 401--402 is exactly empty-prefix input-totality.
4. The stable recurrence at lines 386--395 ensures that every nonempty retained prefix lies in `\gamma` and can be extended for every next input letter.
5. The compatible initial and successor equations at lines 403--413 admit exactly the reachable stable triple sequences, not arbitrary surviving triples.
6. Lines 414--420 prove both strong extendability and maximality: every constructed prefix passes the membership and extension conditions, while the run triples of any strongly extendable sublanguage survive every deletion stage.

Thus `\gamma_A` is empty exactly when the empty-prefix membership or totality condition fails, and otherwise is the largest strongly `A`-extendable regular sublanguage. Theorem 8.1, lexicographic synthesis, the vacuous empty case of Corollary 8.2, the nonempty comparison case, and the formula encoding in lines 421--433 now rest on a complete construction.

Lines 435--441 correctly keep Theorem 7.3 in the causal-transducer setting rather than conflating it with Büchi acceptance. Lines 443--542 state the exact restricted syntax needed in §8.6, give the erratum's finite-union correction and general-arity tagging construction, and explicitly supply the `n=1` binary promotion as a handbook completion rather than attributing it to the erratum. The unary promotion is extensionally correct: `R_j\times R_j` enforces the same all-position unary constraint, while `(E_j\cap R_j)\times R_j` preserves the original first-letter condition. Lines 544--557 then state the Post-system undecidability boundary without broadening Elgot's positive design algorithms.

### Trakhtenbrot's logic, operators, topology, and synthesis boundary

Lines 583--632 define the source's interpreted system before use, state that `\mathcal I` is the handbook's typographic rendering of the Cyrillic source name, distinguish primitive grammar from eliminable conveniences, and give the controlled/lower/upper syntactic classes separately from their semantic dependence consequences. This prevents both conflation with Büchi's weak finite-set system and the use of undefined “local” terminology.

Lines 634--687 distinguish anticipation, finite memory with whole-future suffix access, finite operators, the zero-anticipation automaton-realizable class, source weight, and the 1961/1962 letter-name boundary. Lines 689--741 define one- and many-coordinate portions, homogeneity, graph portions, output prefixes, tails, and residual operators with complete types. Lines 738--741 identify the residual maps as handbook exactifications and explain why they are not broad memory states.

Lines 743--779 correctly reject the source's printed weight-to-homogeneity-degree bound. The two-state presentation computes the displayed operator, the one-state contradiction is valid, and the three nonempty/four all-prefix graph portions refute both the printed `k` bound and the inadequate `k+1` repair. The counterexample and qualification are expressly handbook-owned, while source closedness is retained.

Lines 784--827 state both definability directions and correctly restrict the covering construction to nonempty homogeneous sets before handling the empty set by a contradictory initial condition in the same recurrent syntactic shape. Lines 829--836 define the conditional-algorithm boundary rather than silently erasing it. Lines 838--896 keep continuity, finite memory, bounded anticipation, solution containment, general-solution parametrization, and fixed-lookahead synthesis at their unequal source strengths.

Lines 898--960 give the explicit-definition synthesis and the literal finite-word bridge with typed finite-word maps. The empty-language counterexample to the printed enumeration converse is valid; nonemptiness supplies exactly the missing lengthwise seed and is labelled a handbook-owned correction. The special-beginning condition is defined as an eventually-zero tail property, not an arbitrary prefix. Lines 962--969 correctly decline to attribute the modern one-sentence finite-word theorem verbatim to the announcement or to adjudicate the source's priority remarks independently.

### Rabin's structures, two translations, complementation, and emptiness proof

Lines 1042--1091 define the source root symbol, both order relations, successors, predecessor, all `T_n`, and the structures `\mathfrak N_n` before their use. The editorial order subscripts are explicitly identified as typographic disambiguations, not new relations. Lines 1093--1151 give arbitrary-root valued trees, paths, transition tables, ordinary automata, runs, and the designated Muller family with the essential `\exists r\,\forall\pi` order. The later pair sequence is expressly excluded from ordinary acceptance.

Lines 1153--1242 give the exact track encoding, both logical directions, the concrete principal-formula instance, the finite witness type needed for it, and the exact sentence-to-nonemptiness reduction. The manuscript does not insert Thomas's later regular-tree basis theorem into Rabin's sentence proof.

Lines 1244--1283 correctly state Theorem 3.1 and its deterministic Muller word-automaton product. The transition update, projected infinitely-recurring family, and reason determinism is required are all explicit; McNaughton's result is named as an external dependency rather than silently treated as a proof supplied by Rabin.

Lines 1285--1357 define the finite pair sequence, both path types, dual acceptance, vacuous no-run case, and the zero-length defect. `\Omega^\dagger=((S,S))` is an exact one-pair representation of the impossible path type: an infinite path over finite nonempty `S` cannot have its infinitely recurring set both meet and avoid `S`. The notation has an exact standing and is used only to feed the source's positive-length induction.

Lines 1359--1465 reconstruct the marked-tree, simultaneous-run, well-founded-obligation, two-half-step, and positive-length induction architecture. “Well founded” receives the source's exact no-infinite-dependency-chain definition at lines 1371--1377, its standing is a property of the obligation mapping, it is distinguished from ordinary path acceptance and run merging by its stated role, and it is used in the exact later lemmas. The manuscript locates transfinite induction in Lemmas 3.3 and 3.11 rather than substituting the vague phrase “transfinite proof” for the finite-state construction.

Lines 1195--1209 and 1403--1456 define the source finite-tree property, terminal-node frontier, valuation domain, external frontier value, automaton, and run. “Frontiered” is defined as a property of `E`, distinguished from predecessor closure, and used by the lift, principal-formula application, complementation base, and emptiness base. The manuscript correctly says `f\notin S` is an external frontier value rather than an ordinary state and does not silently add mixed frontier/state transitions.

Lines 1467--1584 reconstruct Rabin's actual one-letter, complement, dual-language, finite-reduction, and weak-finite-tree-theory emptiness proof. The restricted table and the finite table-run are separately and exactly typed. The two printed nonempty-witness gaps are exposed and repaired: `H=\varnothing` gives the direct shorter question, and `m=0`, `U_0=\varnothing` gives the finite no-run obstruction. Both repairs are labelled handbook-owned. The finite-tree decision theorem remains an external base dependency and is not used to identify full `S2S` with weak logic.

Lines 1586--1614 account for the actual Chapter II applications and state an honest proof boundary: the handbook reconstructs the operative architecture but leaves the article's full transition tables and internal inductions in the cited complete source.

### Thomas's later route

Lines 979--1027 give the finite-word automaton, `n+1`-state run, both directions of Theorem 3.1, the empty-word guard, singleton-set atomic forms, weak-sentence decision, and Presburger route at the exact 1996 report locator. The source alphabet/letter predicate is renamed only to avoid collision and is given an exact eliminable definition.

Lines 1618--1643 define the full-tree Muller automaton and preserve the `\exists r\,\forall\pi` acceptance order. Lines 1645--1670 define the strict chain, its path condition, the empty-chain endpoint, and the order-vector-with-hit memory before use. The empty-chain endpoint is clearly owned by the handbook as the completion required when deletion of equal adjacent pairs removes the whole list.

Lines 1672--1701 repair the report's missing game premise with a fully typed rejecting-state completion. The fresh state is outside every accepting `F_i`, missing transitions go to two fresh-state children, and the fresh state loops. Any run using an added transition therefore has a constantly fresh-state path satisfying no chain pair, so the completion preserves the language while making every game position live. `\mathcal A^\bot` is defined as a chain tree automaton, distinguished from a run or game, proved nonredundant by the partial-transition/game-totality mismatch, and then actually used.

Lines 1703--1735 reconstruct the Automaton/Pathfinder game, memoryless strategies, local instruction labels, complement automaton, determinacy induction, and finite-game effectiveness. Lines 1737--1763 define regular generated trees as a property of input trees, derive effective emptiness and a regular member, and complete both directions of the MSO/tree-automaton route. Lines 1765--1770 keep this later route separate from Rabin's original Section 3.12 proof and from the unread final Thomas chapter.

## Technical-name rule

The presentation satisfies the supplied naming rule. Source terminology is defined where first used and assigned a standing before it carries proof weight: examples include special predicate and string behavior; admissibility and strong `A`-extendability; `\mathcal I`, upper/lower formula, finite operator, portion, homogeneity, solution, general solution, automaton-enumerability, and special beginning; and Rabin's ordinary/dual types, frontiered finite trees, and well-founded obligation mappings.

The handbook's own notations also meet the rule:

- `M_h`, `M_\infty`, and `I_\infty(a)` at lines 383--413 are exact finite-set abbreviations required to distinguish stable continuation from the initial state's empty-prefix and first-input obligations; all are used immediately in the maximality proof.
- `T_u` at lines 720--741 is an exactly typed residual stream operator, distinguished from a broad future-dependent memory state and used to formulate the correction to the printed graph-degree claim.
- `\preccurlyeq_{\mathrm{is}}` and `\preccurlyeq_{\mathrm{lex}}` at lines 1046--1055 are declared typographic disambiguations of two source relations, not additional primitives.
- `\Omega^\dagger` at lines 1334--1357 is exactly defined, proved equivalent to the zero-length case, distinguished from a new acceptance semantics, and used in the induction and emptiness recursion.
- “finite table-run” at lines 1515--1530 is required to separate an ordinary-state finite restriction from both the infinite run and the external-frontier-value finite-tree run; it is defined exactly and used in the base decision clause.
- `\mathcal A^\bot` at lines 1672--1705 is exactly defined, assigned the standing of a completed chain tree automaton, distinguished from the source automaton only at missing transitions, and used throughout the game argument.

No passage names a hypothetical primitive or construction before the theory has supplied its exact role. Where a named distinction is not needed, the manuscript uses direct description.

## Cross-source nonconflation

The presentation maintains the important separations throughout:

- Büchi's formula-defined deterministic bit-state recursion is not Elgot's source tuple or Thomas's modern nondeterministic tuple.
- Büchi's finite-set interpretation is not Trakhtenbrot's arbitrary-predicate system.
- Elgot's finite-word acceptor is not his later synchronous transducer, and his infinite causal behavior is not Büchi acceptance.
- Trakhtenbrot's broad finite-memory equations are not prefix-determined automaton states; residual operators are not identified with those states.
- Rabin's ordinary acceptance family is not his dual pair sequence.
- Rabin's infinite-tree runs, his source finite-tree automata, the finite table-runs used in his emptiness base, and the host's bottom-up ranked-tree automata remain different objects.
- Rabin's original complementation and Section 3.12 emptiness argument are not Thomas's post-1969 game/complement/basis route.
- Thomas's report locators are not projected onto the unreconciled 1997 chapter.

These are not merely summary disclaimers: each distinction is enforced at the defining and proof-use locations.

## Host integration

The host integration is correct.

- Host lines 836--850 state the finite-word equivalence as a modern formulation, cite the relevant source package, describe the original encodings separately, and expressly say that the named theorem is not claimed to occur verbatim in each source.
- Host lines 874--877 state only Rabin's decidability conclusion at the public theorem level.
- Host lines 879--929 define finite ranked trees and bottom-up finite-tree automata before the integrated presentation is input, and expressly distinguish them from Rabin's infinite-tree construction.
- Host line 937 inputs the actual N-c-014 presentation between N-c-013 and N-c-015, before the next section starts at host line 940.
- Within the input presentation, lines 1440--1442 explicitly distinguish Rabin's finite source run from the host's bottom-up ranked-tree run, so the placement does not invite an unmarked identification.

No forward reference, authority substitution, or source-boundary contradiction is introduced by the host passage.

## Rights and reproduction boundary

The source notes consistently state that public or institutional readability is not an open-content or republication licence. The actual manuscript does not claim such a licence, does not incorporate source page images, and does not treat research PDFs or derived renders as handbook assets. It uses ordinary mathematical reconstruction, short source terminology, bibliographic attribution, and exact locators. The integrated LaTeX therefore introduces no rights or reproduction overclaim within the reviewed scope.

## Open obligations and limits of this verdict

The consolidated ledger correctly leaves Büchi 1960 and Thomas 1997 open at lines 974--975. The manuscript independently preserves the same two boundaries at lines 8--16 and 1765--1770. This review therefore does not infer final-version wording, numbering, examples, proof detail, or pagination from either precursor.

This is a source-fidelity and mathematical-coherence verdict on the actual LaTeX source at the stated bounded strengths. It is not a TeX-build verdict, a rendered-layout verdict, a manuscript-PDF inspection, a Russian-language-specialist certification, a human or user acceptance, a Part IX completion claim, or a publication gate.

REGISTER STATUS: OPEN
