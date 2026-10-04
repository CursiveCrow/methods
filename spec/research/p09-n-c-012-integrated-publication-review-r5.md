# N-c-012 integrated publication and terminology review, Round 5

## Scope and conclusion

The presentation is publishable on terminology, exposition, source-boundary, and mathematical-coherence grounds. The five source presentations remain distinct, every handbook repair material to a stated result is identified as a repair rather than silently attributed, and no reader-facing workflow debris remains. The opening register-row remark is a non-rendered LaTeX comment only (`handbook/parts/p09/presentations/n-c-012.tex:1`). Layout and rendering are outside this round and supply no evidence here.

## Terminology and definition-before-use

- `K_b` is introduced only after its semantics and proof ingredients have been displayed. Its exact standing is a theorem system consisting of the pure propositional future calculus, derived inclusive `F`, G1--G3, and RT/RG/MP; it is expressly neither a formula class nor a model class and is distinguished from `DX` and `DUX` (`n-c-012.tex:819-898`). The later ER comparison does not erase that boundary: the manuscript observes that translated ER axiom A1 needs system-dependent rule E, which bare `K_b` does not contain, and therefore leaves Theorem 3 as an unresolved source assertion rather than claiming an embedding (`n-c-012.tex:1020-1029`). This satisfies necessity, definition, standing, nonredundancy, and later-use requirements.

- The occurrence summaries `\mathcal L_i` and `\mathcal L_C(x)` are defined before their rules are used: the first is indexed by a prefix occurrence and the second by a recurrent graph node (`n-c-012.tex:2163-2189`). Their standing as eliminable finite metalinguistic truth data is explicit, as is their nonredundancy: prefix occurrences and recurrent nodes have different future domains, and neither summary is the later semantic source truth set `[s_i]_{S,f}` (`n-c-012.tex:2203-2215`).

- Other potentially collision-prone names receive the same local treatment. Examples include the parameterized family needed only for ER rule R4 (`n-c-012.tex:543-616`), `L_{\rm prop}(\Sigma)` as an execution language rather than an automaton (`n-c-012.tex:1154-1201`), the strict GPSS warnings `\mathsf U_s,\mathsf S_s` (`n-c-012.tex:1253-1317`), ambient-subsequence measures (`n-c-012.tex:2020-2051`), and the ETL input-length parameter `\ell_{\mathrm{in}}` (`n-c-012.tex:2582-2595`). Each is eliminable or source-defined, typed, distinguished from nearby notation, and used by a subsequent result.

## Counterexamples, suffix, and certificate

- The repeated-node counterexample is correct. Along `x,u,x,c,c,\ldots`, `Fa` is true at the first occurrence of `x`, while `b\land\neg Fa` is true at the second; hence the whole word satisfies `Fa\land F(b\land\neg Fa)`, but one node-indexed label for `x` cannot record both occurrence truths (`n-c-012.tex:2145-2162`). The move to `\mathcal L_i` is therefore necessary rather than cosmetic.

- The directed-cycle counterexample is also correct. With edges `q_0\to c\to d` and `d\to d`, the singleton `C={c}` is strongly connected under reflexive reachability but has no infinite internal continuation. The literal checks can therefore accept `GP` although the only infinite path reaches `d` and falsifies it (`n-c-012.tex:2217-2229`). Requiring an internal directed cycle is exactly the missing condition: it forces a self-loop for a singleton and is automatic for a larger finite strongly connected component (`n-c-012.tex:2229-2234`).

- The repaired witness has a sufficient suffix and size argument. Strong connectivity plus the directed-cycle condition permits an infinite suffix visiting every node of `C` infinitely often, which validates the recurrent `F` rule; the prefix rule separately ranges over later prefix occurrences and recurrent nodes (`n-c-012.tex:2181-2210`). There are only `r+1+|C|` summaries, each a subset of `\operatorname{SF}(f)`, while the guessed prefix has length at most `\operatorname{length}(f)|N|`; thus occurrence sensitivity preserves a polynomial certificate (`n-c-012.tex:2132-2143`, `2203-2215`).

## ETL and theorem scope

- ETL formation is explicit and has the correct standing: it is the least formula class extending the inclusive temporal language by grammar-indexed constructors, not a grammar, automaton, or proof system (`n-c-012.tex:2468-2519`).

- The source permits a finite emitted word in a production, but its later consistency rule has no empty-emission case. The manuscript therefore restricts emitted words to nonempty terminal words and labels this as a handbook restriction, not a source claim (`n-c-012.tex:2468-2478`). Replacing an `r`-terminal production by a chain of `r` one-terminal productions preserves generated strings and incurs only linear encoded-size growth (`n-c-012.tex:2479-2483`); this justifies use of the one-terminal consistency rule (`n-c-012.tex:2596-2609`).

- The scope qualification reaches the results that depend on it. Theorem 5.4 is expressly reconstructed only for the nonempty-emission grammar domain (`n-c-012.tex:2582-2585`), and the final classification table repeats that convention instead of presenting unrestricted ETL (`n-c-012.tex:2639-2670`). The formula-and-grammar encoded-input size is kept distinct from constructor arity, so the closure bound used for PSPACE is not misstated (`n-c-012.tex:2586-2595`).

## Source labels, transitions, and publication coherence

- Repairs and unresolved source claims are consistently reader-facing and ownership-qualified. Representative load-bearing cases are Kamp's missing parity premise (`n-c-012.tex:272-341`), Pnueli's zero-rank and strict-future conflicts (`n-c-012.tex:517-541`, `668-676`), GPSS's conflicting future and weak-until clauses (`n-c-012.tex:1237-1251`, `1778-1805`), the Sistla--Clarke strict/non-strict size defect (`n-c-012.tex:2051-2106`), and Alpern--Schneider's Corollary 2.1 repair and counterexample (`n-c-012.tex:2978-3011`). None is promoted from source assertion or outline to handbook proof without the needed argument.

- The host section establishes the inclusive Part IX language and the exact strict/inclusive two-way bridge before the presentation is inserted (`handbook/parts/p09/logic-in-computer-science.tex:602-694`). It then places N-c-012 with the other temporal/automata presentations before the model-checking section (`logic-in-computer-science.tex:900-912`). Within N-c-012, the progression from expressiveness, to transition-system proof methods, to strict temporal systems, to operator-sensitive complexity, to semantic safety/liveness is closed by an accurate five-way boundary (`n-c-012.tex:3047-3060`). That boundary preserves strict versus inclusive semantics, theorem systems versus formula classes, existential path problems versus formula satisfiability/validity, and syntactic versus semantic classifications.

No publication or terminology blocker remains in the reviewed source.

VERDICT: ACCEPT
