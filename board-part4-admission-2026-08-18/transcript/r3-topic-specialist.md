# Round 3 final focused verification — computability/complexity topic specialist

## Verdict

**F13 accept-fixed.  F14 accept-fixed.  No residual correctness defect in the
focused frozen scope.**

I re-read my R2 transcript and the current live versions of the complexity,
frontiers, and degree/priority body and annex files.  I did not read another
seat's transcript, edit manuscript/control/test/generated files, run a build,
or run tests.

## F13 — accept-fixed

The definition order is now correct:

- `handbook/parts/p04/complexity.tex:171-186` first defines QBF formation,
  Boolean quantifier range, closedness, truth, TQBF, and the fixed-alternation
  Sigma/Pi languages.
- Only afterward, at lines 188-218, does the succinct entry fix CVP, the padded
  gate-list/QBF encoding, fixed-width addresses, SCVP, and STQBF.

Thus the phrase “valid encoded true closed quantified Boolean formula” at
lines 208-210 is eliminable through a preceding reader-visible owner.  No
second QBF definition was introduced.

The padded encoding is also sufficient for the cited classifications.  Its
self-delimiting decoder ignores trailing zeroes after the end marker, is
logspace computable, and is logspace intertranslatable with the ordinary
encodings; consequently every ordinary instance has a valid encoding of a
large enough power-of-two length (`complexity.tex:195-199`).  The bit circuit
then denotes exactly the \(2^m\)-bit expansion indexed by fixed-width binary
addresses (`:201-210`).  Under this convention, the statements at `:220-224`
have the right strengths and reductions:

- CVP is \(\mathsf P\)-complete under logspace many-one reductions;
- SCVP is \(\mathsf{EXPTIME}\)-complete under polynomial-time many-one
  reductions; and
- STQBF is \(\mathsf{EXPSPACE}\)-complete under polynomial-time many-one
  reductions.

The power-of-two restriction no longer removes hardness instances, invalid
decoded strings remain no-instances, and exponential decompression gives the
stated deterministic time/space membership bounds.

## F14 — accept-fixed

The complete Omega annex now supplies the formerly missing contradiction
target at `handbook/annex/p04/frontiers.tex:32-37`.  If
\(\operatorname{dom}(U_K)\) were decidable, the displayed procedure searches
programs by increasing length, discards nonhalters using that decider, runs the
remaining finite set, and stops at the first length producing \(x\).
Universality ensures that some description of every finite string exists, so
this procedure computes \(K_{U_K}(x)\), contradicting the preceding cited
noncomputability theorem.  It therefore proves, rather than assumes, the
domain undecidability used at lines 39-47.

The rest of the annex proof is exact:

- dovetailed halting weights form a computable nondecreasing rational
  approximation with supremum \(\Omega_{U_K}\) (`:27-30`);
- a computable Omega would provide a strict lower rational approximation with
  residual below \(2^{-(n+1)}\), after which any unseen program of length at
  most \(n\) would contribute too much mass (`:39-47`); and
- for the first \(n\) bits, non-dyadicness makes the lower truncation strict,
  and once the partial sum exceeds it, an unseen length-at-most-\(n\) halt
  would cross the interval's upper endpoint (`:49-56`).

This proves exactly the body theorem at
`handbook/parts/p04/frontiers-of-computability.tex:357-365`: left-c.e.-ness,
noncomputability, and finite-bit determination of halting through length
\(n\).  The `proved=annex:p4.frontiers.2` status is now justified.

## Kleene--Post — checked clean

The body requirements are typed as function comparisons
\(\chi_A\not\simeq\varphi_e^B\) and
\(\chi_B\not\simeq\varphi_e^A\) at
`handbook/parts/p04/degrees-and-priority-continuation.tex:84-90`; the annex
uses the same schemas at
`handbook/annex/p04/degrees-and-priority-continuation.tex:39-47`.

The annex covers the manuscript's decider-based definition of Turing
reducibility: every oracle decider is wrapped so that simulated acceptance
writes \(1\) and accepts, while simulated rejection writes \(0\) and accepts;
normal finite-table serialization gives a valid numerical-program code
(`:48-53`).  Hence one of the enumerated numerical functions really is the
target characteristic function whenever a Turing reduction exists.

Finite-string convergence is explicitly defined at `:54-57`, including the
requirement that every queried oracle position lie below the finite string's
length and receive that string's answer.  The extension question at `:59-74`
is an existential finite-computation question; cited completeness of \(K\)
handles it, and the following direct primitive-recursive query-free compiler
reduces \(K\) to the present definedness jump.  The proof therefore does not
use the sketched jump-convention bridge or relativized parameter theorem.

The yes/no permanence argument, totality by padding, computation in
\(\varnothing'\), and strict-below-\(\mathbf0'\) conclusions at `:75-95` all
follow.  I found no remaining type, output-convention, or dependency gap.

## Friedberg--Muchnik — checked clean

The body and annex requirements compare the oracle numerical functions with
the total characteristic functions, not with sets as if they were functions:
`handbook/parts/p04/degrees-and-priority-continuation.tex:124-140` and
`handbook/annex/p04/degrees-and-priority-continuation.tex:99-105`.

The annex now supplies every focused proof obligation:

- stage convergence and use are defined at lines 107-116; stability below the
  finite use preserves a seen computation, and every final halting computation
  appears after its finite oracle segment stabilizes;
- every Turing reduction is covered syntactically by the accept/reject-to-1/0
  wrapper followed by primitive-recursive normalization and serialization,
  without invoking relativized adequacy (`:118-123`);
- the finite state, fair scheduler, witness policy, action, restraint,
  initialization, and symmetric strategy are effective (`:125-145`);
- the finite-injury induction treats both action and no-action cases, including
  why only finitely many lower-priority enumerations can occur below the final
  finite use (`:147-158`); and
- the final reduction of any c.e. enumeration to \(\varnothing'\) explicitly
  compiles a query-free program that writes \(0\) and accepts exactly when the
  enumerator lists the queried number (`:160-169`).

Accordingly the complete annex establishes incomparable c.e. sets and the
strict intermediate-degree consequence without resting on the inherited
proof-sketch clauses.

## Key theorem-statement recheck

The focused surrounding statements remain coherent with these proofs and
definitions:

- jump extensivity is confined to the completely proved
  \(A\leq_mA'\) lemma, while strictness uses separately cited diagonal
  nonreducibility;
- Kleene--Post asserts an unrestricted incomparable pair below
  \(\mathbf0'\) and expressly makes no c.e. claim;
- Friedberg--Muchnik asserts incomparable c.e. sets and correctly derives
  nonzero degrees below \(\mathbf0'\);
- TQBF and fixed-alternation QBF retain PSPACE and polynomial-hierarchy
  completeness with polynomial-time many-one reductions;
- the deterministic time/space hierarchy and Savitch statements retain their
  constructibility and lower-bound hypotheses; and
- Fagin remains a single Part III identity with no built-in order, while the
  ordered FO(LFP) capture theorem retains positivity and its built-in-order
  hypothesis.

## Conclusion

R2 **F13 and F14 are closed**.  The revised Kleene--Post and
Friedberg--Muchnik complete proofs meet the requested typing, wrapper,
stage-convergence, syntactic-coverage, and dependency conditions.  The
succinct padded encoding and the checked key theorem statements have no
remaining correctness defect in this frozen focused scope.  At the
source/content level, I have no blocking topic-specialist objection.  Build,
visual, human, administrative, and user-acceptance gates remain external and
were not inferred.
