# Edition 2026 C6.3–C6.5: computation verification, P4 portion

Date: 7 September 2026. Author report for the actual bounded H3/H4 formulas, full computation-verification proof and P4 c.e./Delta-1 proof. “Complete proof” below describes a supplied manuscript argument after author read-back. Independent acceptance remains for the review round.

## Saved artifacts and frozen identity

The manuscript edit is confined to [inherited-08710-08876.tex](../../handbook/restoration/inherited-08710-08876.tex), after the H1/H2 packing lemma. This note is the only other file written. No source acquisition, bibliography change, P5 edit, shared driver/style/symbol/provenance edit, software test, manuscript build/render or delegation was performed.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor history file, complete C6.2 version | 076FFD24CBF5824234818704CABCEFF918D607EF61C36DC34314C3F47D3CABF5 |
| Frozen history file after this block | E391CAA3351C3DC768D2FAC6E00636EA57C7BB189161A6941C25229C0D922D30 |
| Protected prefix through original/current line 529 | EF4DC92D08B421705E102AE42104F331458AB5D0D53536E1A50B266907BA45DC |
| Unchanged serialization file | DE01687B7F524F49D6B3E90C9ACD038550F7BE1551A1AABC771B8BBB3B4B0177 |

The protected-prefix digest hashes the exact UTF-8 text before the old Comp theorem, and afterward before the new configuration/transition/output definition. The hashes agree. All root E/E2 and history material, H1/H2 definitions, their correctness proofs and their packing lemma remain unchanged. No correction to that protected material was needed.

The earlier complete saved candidate had hash 8700B8163D63CE22E0C42A34CC9A3A6C113F5DFBC03109DAB75F236B9EE3BB6E. Final clarification edits described R5 accurately as an abbreviation, linked enumeration and prefix normal form by their labels, stated the bounded evaluator's canonical one-digit output operation, and explicitly returned false for the bottom formula. The intermediate hash before that last same-line clarification was FA87FBD3DF2184F1535AACB7E39179076C6627BC2A6B46D5ABD8DD6459AD9CD5.

## Current manuscript locations

| Label or component | Lines | Supplied content |
| --- | --- | --- |
| def:p04-computation-formula | 530–673 | Literal Cfg, Init, Step, H3, OutCells, OutNext, H4 and Comp formulas |
| lem:p04-configuration-output-formulas | 675–800 | Boundedness and both conditional correctness directions, relative to certified H1/H2 input/table |
| thm:bounded-verification | 802–904 | Existing theorem with complete supplied proof replacing the former proof plan |
| Source/P5 boundary paragraph | 906–912 | Bespoke-code attribution and separation from Q-representation/internal provability |
| One-step identity example | 914–953 | Exact program, header, input, bitmap, tape, state/head and output; leading-zero and blank-bitmap failures |
| thm:p04-ce-sigma-one | 955–1042 | Existing c.e./Sigma-1 and decidable/Delta-1 statement with stable label and complete supplied proof |

No ordinary theorem was added. The four openings remain in order at lines 802, 955, 1056 and 1077. The P4 driver's third/fourth theorem hooks retain their hierarchy targets. Those latter two results remain cited theorems and were not reconstructed.

## Actual local reading and dependencies

The precise owner of this serialization is the active handbook itself. No external normal-form coding or T-predicate was substituted. No external paper or book body was newly read or attributed as the source of these literal formulas.

| Actual source | Read scope and use |
| --- | --- |
| [inherited-08710-08876.tex](../../handbook/restoration/inherited-08710-08876.tex) | Complete C6.2 reading reused at identical predecessor hash. This block read the live boundary and old proofs at 497–605 before writing; new definitions/lemma read back at 530–825, then Comp/example/c.e./retained suffix at 802–1098. Final changed lines and labels were read at the frozen hash. |
| [inherited-07851-08048.tex](../../handbook/restoration/inherited-07851-08048.tex) | Serialization at 22–80; raw numerical-output definition at 82–109; complete enumeration theorem at 147–210. Full file read in C6.2; unchanged hash reverified here. |
| [inherited-07506-07677.tex](../../handbook/restoration/inherited-07506-07677.tex) | Exact transition, initial tape, canonical binary and first-blank output at 1–145 were read in C6.2 and used through the preserved interface. |
| [inherited-07753-07843.tex](../../handbook/restoration/inherited-07753-07843.tex) | Full 1–91 read. C.e. is defined as a partial-computable domain at 9–12. Four-way equivalence at 56–76 remains a sketch and is not used for the forward implication. Decidability/complement has a supplied proof at 78–90. Hash: E2B7284BEABCA82F440BB921D779243F1615F8D7077ABA73DFF6CBDE28458B00. |
| [inherited-08306-08438.tex](../../handbook/restoration/inherited-08306-08438.tex) | Current 61–133 reread for the closure-based hierarchy and definability classes; language and marked bounds reused from C6.2. |
| [inherited-08439-08709.tex](../../handbook/restoration/inherited-08439-08709.tex) | Current 153–271 read for thm:prefix-normal-form and its full supplied proof. P/B/packing dependencies reused from C6.2. Unchanged hash: 95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A. |
| [parts/p04.tex](../../handbook/parts/p04.tex) | 1–75 read for active routing and theorem-hook ordinals. |

The primitive-recursion fragment and machines/effective-procedures supplement were also read while locating the finite-procedure interface. The new Comp proof does not use a generic T-predicate, the cited Kleene normal-form theorem, a representability theorem, or the c.e.-is-Sigma-1 conclusion. Beta packing retains its explicit Chinese remainder theorem dependency. The research skill's primary-source/note practice is continued within the assignment's no-delegation instruction.

## H3 and H4 obligations supplied

H3 extracts k,n,b,L,T,H,W and bounded auxiliaries m,mu. It checks L>=1, H=T, W=L+2T+1, k=3+m, W=Smu; all state/head/symbol ranges; every tape prefix recurrence and complete tag-11 code; initial state 0 and head H; input symbols S d_i at H+i and blanks elsewhere; and every transition t<T.

Each transition explicitly selects i<m through R5, matches the current state and scanned symbol, forbids halting source states, applies the exact left/right head equation, writes the selected symbol at the scanned cell and preserves every other window cell. H2 and k=3+m give m=(n-2)b. Thus padding cannot supply a fictitious transition. H3 alone is not claimed to validate the program; its correctness lemma assumes H1 and H2.

H4 requires accepting state 1, positive output length, H+ell<W, a blank at H+ell and normalized binary symbols S o_i at all preceding output columns. Thus the chosen blank is the first nonnegative blank. It checks every binary prefix, first and last values, recurrence and bound by y. Zero output is exactly one zero bit; a positive output starts with one. Final head, negative cells and cells beyond that first blank impose no additional output condition.

Every matrix lookup is E/E2 or bounded R5; every matrix comparison is Lt/Le or an equality and Boolean connectives. Fresh renaming applies before every abbreviation expansion. No schematic array term, exponentiation, subtraction, division or added arithmetic-language function remains in a formula matrix.

## Full computation proof and all witness bounds

The definition is exactly

\[
\mathsf{Comp}(e,x,s)=
\mathsf H_1(x,s)\land\mathsf H_2(e,s)\land\mathsf H_3(s)\land\mathsf H_4(s).
\]

For a satisfying s, unique extraction makes repeated header values agree. H1/H2 recover the input and valid exact table. The new lemma extends each stored window tape with blanks outside the physical interval [-H,W-H), makes its physical head h_t-H, and proves that its initial tape and every full one-step transition are those of the raw decoded machine. H4 supplies acceptance with canonical numerical output.

Conversely, an actual T-step accepting numerical run has -t<=p_t<=t by induction. Its nonblank support through time T is contained in [-T,max(T,L-1)]. Choosing H=T, W=L+2T+1 gives the physical window [-T,L+T], containing every scanned cell and a blank at the rightmost cell L+T. The first nonnegative blank ell therefore satisfies ell<=L+T, hence H+ell<W. Actual states, shifted heads, tape symbols and their base-b prefixes, and output data are a finite compatible extension of the input/table assignment. Beta packing supplies one s.

All stored values are then at most s. The remaining witnesses obey m=k-3<=k<=s, mu=W-1<W<=s and lambda=ell-1<ell<=s. Row fields/pairing tails are bounded by their stored row codes. Tag/position indices use E/E2's own bounds and are not assumed <=s. No polynomial bound on s is claimed. Tape leading zeros are permitted because width is explicit.

For T=0 the transition range is empty and H3 describes the initial configuration. H4 cannot accept it because normalized start 0 and accepting state 1 are distinct. Rejecting halts and accepting halts with invalid numerical output fail the final checks.

## Worked data and failures

The example uses n=b=3, A=6 and delta(0,a)=(1,a,R) for a=0,1,2, with the exact five-field row codes and six-entry description. For x=2:

| Component | Exact value |
| --- | --- |
| Input bits/prefixes | (1,0) / (1,2) |
| T,H,W | 1,1,5 |
| Header | (6,c0,3,3,6,2,1,1,5,2,2) |
| Bitmap bits/tails | (0,1,1) / (6,3,1,0) |
| Both tape rows | (0,2,1,0,0) |
| Both tape-prefix rows | (0,2,7,21,63) |
| Complete tape codes | 63,63 |
| States / shifted heads | (0,1) / (1,2) |
| Selected transition row | i=2<m=3 |
| Output bits/prefixes | (1,0) / (1,2) |
| Output length/value/first-blank column | ell=2, y=2, H+ell=3 |

Every recurrence and location was checked against the actual formula. The exact pairing expression and beta-packing lemma supply the coding claim without printing enormous decimal integers. The failure word (0,1), with prefixes (0,1), satisfies the recurrence and prefix bounds for value 1 but fails H1's first-bit condition. Bitmap (1,1,1), value 7, fails H2's blank-symbol exclusion.

## P4 c.e./Delta-1 proof and remaining standing

The forward Sigma-1 direction uses the definition of c.e. as a domain, then complete thm:enumeration for this numbering, then the newly supplied bounded Comp proof. It does not rely on the separate four-way equivalence sketch.

The reverse direction supplies a bounded-formula evaluator by induction on syntax: finite arithmetic and Boolean evaluation and bounded-quantifier loops with fixed finite ranges. Empty existential/universal ranges are included. The proof explains finite tape-block implementation and explicitly places the returned truth digit at physical cell 0 followed by a blank at cell 1. Prefix normal form gives existential witness tuples over a bounded matrix; finite tuple-box enumeration reaches every witness. Returning 0 on discovery and continuing forever otherwise has exactly the required partial-computable domain, including the empty set.

Negation exchanges Sigma-1 and Pi-1 definability. The earlier supplied decidability/complement characterization yields decidable iff Delta-1.

The assigned P4 portion now has complete supplied arguments and a worked example. Independent review and any resulting repairs remain. P5 numeralwise representability in Q, internal syntax/proof coding and D1–D3 proof transformations are separate obligations; this standard-model truth theorem does not prove them. The separate universal-machine/compiler and hierarchy-completeness proof boundaries outside the assigned portion were not changed.
