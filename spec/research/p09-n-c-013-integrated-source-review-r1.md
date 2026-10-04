REJECT

# N-c-013 integrated source-fidelity review, Round 1

## Review object and method

This seat read the actual manuscript source
`handbook/parts/p09/presentations/n-c-013.tex` from line 1 through line 1222,
then read the actual host source
`handbook/parts/p09/logic-in-computer-science.tex` lines 723--915.  The review
compared those passages directly with:

- `spec/research/p09-vardi-wolper-1986-source-note.md`;
- `spec/research/p09-buchi-1962-source-acquisition.md`;
- `spec/research/p09-mcnaughton-1966-source-note.md`;
- `spec/research/p09-safra-1988-source-note.md`;
- `spec/research/p09-thomas-1996-report-source-note.md`; and
- the N-c-013 entries in
  `spec/research/p09-source-presentations-lot2-3.md` lines 613--675.

The manuscript was judged from the LaTeX text itself.  No manuscript PDF,
PNG, rendered page, or other manuscript rendering was opened or inspected.
No build, test, checker, repository script, hash, or automated validation was
run.  No prior integrated N-c-013 review report or prior Safra/Thomas review
report was read.

## Blocking findings

### 1. The host definition cites the unread McNaughton body as support for modern acceptance data

`handbook/parts/p09/logic-in-computer-science.tex:723-744` defines a modern
deterministic parity tuple and a modern deterministic Rabin tuple, gives their
acceptance clauses, and then collectively cites
`Buchi1962,McNaughton1966,Thomas1996Report` at line 744.  In that position the
McNaughton key appears to support the displayed modern tuple/acceptance
presentation.

That exceeds the manuscript's own correct evidence boundary.  The dedicated
presentation says that the 1966 article body was not acquired and that its
alphabet, automaton tuple, acceptance clause, theorem wording, constructions,
examples, and proof remain unavailable
(`handbook/parts/p09/presentations/n-c-013.tex:757-773`).  It then expressly
forbids attributing a modern deterministic Muller/Rabin tuple or acceptance
family to the article before that body is read
(`handbook/parts/p09/presentations/n-c-013.tex:775-781`).  The controlling
source record reaches the same conclusion: only the Project MAC summary's
omega-event vocabulary and equivalence effect are source-verified
(`spec/research/p09-mcnaughton-1966-source-note.md:121-144`), while every
automaton datum and acceptance clause remains open
(`spec/research/p09-mcnaughton-1966-source-note.md:184-197`), and no later
acceptance name may be retrojected
(`spec/research/p09-mcnaughton-1966-source-note.md:205-217`).

The repair is narrow: remove `McNaughton1966` from the supporting citation at
host line 744, or move it to a separate sentence whose only claim is the
registered historical identity and whose unread-body limitation is explicit.
`Thomas1996Report` can support the modern Rabin clause and Thomas's later
attribution of the determinization result; it cannot turn the unacquired 1966
body into evidence for the displayed definition.

### 2. The concurrent Vardi--Wolper locator stops one page too early

`handbook/parts/p09/presentations/n-c-013.tex:351-366` states the full
concurrent Markov-chain tuple and then gives the two distinct transition
conditions for probabilistic and nondeterministic states, including the role
of the fair-scheduling set.  The sole locator at line 367 is
`preprint p. 10`.

The controlling page map says that the concurrent model begins on internal
preprint p. 10 and is completed on internal p. 11
(`spec/research/p09-vardi-wolper-1986-source-note.md:50-51`).  Its controlling
reconstruction likewise presents the tuple, the two transition cases, and the
fair-scheduler meaning as one source unit
(`spec/research/p09-vardi-wolper-1986-source-note.md:458-479`).  Because the
manuscript states the completed unit, its locator must be `preprint pp. 10--11`
or be split so that each page supports only the material actually located
there.  The present single-page locator is incomplete.

## Source-by-source audit of the remaining text

### Vardi and Wolper

Apart from finding 2, the presentation preserves the source and version
boundary.  It identifies the accessible eighteen-page file as an author
preprint dated in 1985, keeps the 1986 proceedings identity and pp. 322--331,
and does not call the preprint a proceedings facsimile
(`n-c-013.tex:8-15`; source record `p09-vardi-wolper-1986-source-note.md:7-33`).
The PTL semantics, source tuple, several-start convention, semi-deterministic
restriction, Theorem 2.1 bound, and cited emptiness status agree with the
record (`n-c-013.tex:17-72`; source record `:56-128`).  Appendix B's local and
eventuality components, pre-projection `2^{3|phi|}` bound, projection, and
unexpanded proof boundary are kept distinct (`n-c-013.tex:74-124`; source
record `:130-200`).

The finite-program product is correctly presented as universal-path
satisfaction reduced to emptiness against the automaton for the negated
formula, and the source's tuple-order inconsistency is disclosed rather than
normalized invisibly (`n-c-013.tex:126-181`; source record
`p09-vardi-wolper-1986-source-note.md:219-296`).  The three-state calculation
is explicitly labelled handbook-owned (`n-c-013.tex:183-203`).  Vardi--Wolper
is credited only with its upper bounds; the combined-input PSPACE lower bound
is assigned separately to Sistla--Clarke (`n-c-013.tex:163-181`; host
`logic-in-computer-science.tex:799-812`).

The ETL variants retain their three different acceptance standings and their
cited-proof boundary (`n-c-013.tex:205-230`; source record
`p09-vardi-wolper-1986-source-note.md:298-319`).  The probabilistic section
uses measure-one satisfaction, explicitly allows a nonempty measure-zero
counterexample set, and never substitutes universal-path language emptiness
(`n-c-013.tex:232-260`; source record `:321-358`).  The Streett pair convention
is correct, and the internally inconsistent printed "opposite" conversion is
reported as a defect with the intended expensive direction identified as a
handbook correction, not quoted as a clean source theorem
(`n-c-013.tex:262-271`; source record `:360-376`).  Limit equivalence,
probabilistic fairness, the restricted-fragment results, and every sketched,
cited, or deferred proof boundary remain source-bounded
(`n-c-013.tex:273-373`; source record `:378-499`).

### Buechi 1962

The complete article is identified as printed pp. 1--11 inside a later
Stanford printing, with the original 1962 proceedings identity separated from
the 1966 and 1990 reprint DOIs (`n-c-013.tex:377-389`; source record
`p09-buchi-1962-source-acquisition.md:1-37`).  `SC` is kept as Buechi's
interpreted formalism, not silently renamed into an automaton or word
language, while the modern S1S/Buechi comparison is explicitly handbook-owned
(`n-c-013.tex:391-419,469-498`; source record `:78-111,158-189`).

The formula-class standings, infinitely-often clause, source-declared
formula/denotation overload, finite-word congruence, and multiperiodic-language
standing are exact (`n-c-013.tex:421-523`; source record
`p09-buchi-1962-source-acquisition.md:113-156,191-224`).  The Sequential Lemma
retains the material quantifier `p<q`; the finite-word bridge keeps the Myhill,
Buechi 1960, and Rabin--Scott proof referrals visible
(`n-c-013.tex:525-573`; source record `:226-288`).  The complement argument
uses the source's finite congruence and the bound `2^{2m^2}`, not later
determinization, and the repeated blocks are stated as nonempty
(`n-c-013.tex:575-603`; source record `:290-336`).

Theorem 1, the handbook-owned modern automata equivalence, Lemma 12's finite
stem--nonempty-cycle argument, and Theorem 2's decidability conclusion retain
their ownership and do not acquire a modern complexity bound
(`n-c-013.tex:605-663`; source record `:338-399`).  The later consequences,
`SC_fin` and `SC_per` distinctions, source discrepancy over `Nn`, Theorems
3--4, proposed but unproved axiom system, and three open problems are all
reported at their actual strength (`n-c-013.tex:665-755`; source record
`:401-508`).  The host theorem at
`logic-in-computer-science.tex:830-841` accurately marks `SC` as the source
formalism and the automata packaging as modern, and states decidability
without a modern complexity claim.

### McNaughton 1966

The dedicated presentation itself is source-faithful.  It reports the
publisher's open-archive identification while distinguishing access failure
from nonexistence (`n-c-013.tex:757-763`; source record
`p09-mcnaughton-1966-source-note.md:12-69,96-116`).  It uses only the Project
MAC report's first-person vocabulary and equivalence effect, separates the
fallacious game memo, and withholds every article-body definition,
construction, acceptance clause, proof, example, and modern tuple
(`n-c-013.tex:765-781`; source record `:118-217`).  Finding 1 concerns only the
contradictory host citation.

### Safra 1988 and the 1995 expanded manuscript

The text keeps the unread nine-page 1988 proceedings body separate from the
complete twenty-page author-hosted expansion and attributes detailed material
only to the latter (`n-c-013.tex:783-798`; source record
`p09-safra-1988-source-note.md:1-88`).  It preserves Safra's total target
determinism convention, `(L_i,U_i)` pair order, `n`-name vocabulary, and `n`
Rabin pairs (`n-c-013.tex:800-830,927-942`; source record
`:90-115,196-202`).

The corrected sibling order, inclusive specificity relation, deterministic
name allocation, empty-root sink, total label encoding, and all other repairs
are explicitly identified as handbook-owned and have eliminable standing
(`n-c-013.tex:832-925,991-1002`; source record
`p09-safra-1988-source-note.md:117-194,221-234`).  The correctness argument,
asymptotic result, lower-bound qualification, deterministic-in-the-limit
definition, and applications remain at expanded-manuscript strength
(`n-c-013.tex:944-1025`; source record `:196-264`).  No detail from the
expanded manuscript is retrojected into the unread FOCS body.

### Thomas 1996 report precursor

The presentation consistently cites `Thomas1996Report`, identifies it as the
May 1996 Kiel report precursor, and explicitly withholds claims about the
registered 1997 chapter (`n-c-013.tex:1036-1039,1218-1222`; source record
`p09-thomas-1996-report-source-note.md:3-88,320-350`).  The four acceptance
modes, total deterministic transition premise, Streett pair order, finite-union
characterization, and deterministic-Buechi complement boundary agree with the
report record (`n-c-013.tex:1040-1117`; source record `:114-149`).

Thomas's `2n`-name Safra-tree presentation is not fused with Safra's separate
`n`-name expanded-manuscript construction.  The mark lifetime, empty-root
state, injective name discipline, same-update allocation, Rabin pairs, bounds,
and counterexample are all labelled with the correct source or handbook
ownership (`n-c-013.tex:1119-1194`; source record
`p09-thomas-1996-report-source-note.md:150-196,280-304`).  The Buechi/MSO
correspondence and weak-MSO consequence retain report-precursor strength, and
the accepting-cycle correction is disclosed as handbook-owned
(`n-c-013.tex:1196-1216`; source record `:198-204,280-289`).

## Cross-source and terminology conclusion

The presentation file itself does not splice Vardi--Wolper's product with
Safra/Thomas determinization, does not assign Sistla--Clarke's hardness to
Vardi--Wolper, does not replace Buechi's `SC` by a purported source automaton
tuple, and does not merge Safra's `n` pairs with Thomas's `2n` pairs.  Its new
or adapted names are locally defined, assigned a standing, distinguished from
nearby source terms, and used; no additional AGENTS.md terminology violation
was found.

Admission requires the two narrow source-text repairs above.  No other
source-fidelity finding was identified on the reviewed actual-LaTeX snapshot.
