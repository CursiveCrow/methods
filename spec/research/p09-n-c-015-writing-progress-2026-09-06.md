# Finite-tree automata and WSkS: completed constructive writing

The modern finite-tree presentation now supplies the constructions that
the earlier N15 text described only in outline. The separate
Thatcher--Wright source body remains an acquisition gap.

## Finite automata

The actual N15 LaTeX proves the subset-state invariant, including
nullary symbols, the empty subset, and alphabets without ground terms.
It supplies disjoint-union and intersection-product proofs and the
complete deterministic complementation argument.

The membership and emptiness section proves the productive-state
invariant and gives the linear occurrence-counter implementation.
Repeated occurrences of a child state contribute separate decrements.
First-marking rules give an acyclic witness graph, and the text
distinguishes its compact representation from an expanded tree.
The inclusion, equivalence and universality reductions are explicit.

## Finite-tree MSO equivalence

The public theorem thm:p09-finite-tree-automata now has a complete proof
at annex:p9.trees.1, in handbook/annex/p09/finite-trees.tex.
The active Part IX annex driver includes this file.

The proof marks individual and set assignments on a fixed finite ranked
tree. Individual tracks are singleton-guarded and may overlap. Atomic
equality, labels, membership and child relations have explicit finite
state tests. Rank-preserving bit erasure implements quantification;
relative complement handles negation; extra-track lifting aligns free
variables. The inverse translation existentially quantifies a state
partition and imposes root and local transition constraints.
Empty states/finals, nullary symbols, vacuous binders and absent ground
trees are included.

## WSkS canonical coding

The presentation retains TATA's actual ternary tracks and singleton
reading of X = Yi. It now defines the complete prefix/padding domain,
supplies the full eleven-node worked code, and constructs the regular
language W_n of exactly canonical assignment codes.

All four restricted atomic recognizers are given for general k.
The formula invariant restricts every recognized language to W_n.
Negation is complement relative to W_n.

Track deletion is the specified pruning homomorphism: a projected
all-bottom label becomes a nullary leaf and erases its child family.
The image automaton computes states realizable by deleted-track-only
subtrees and uses them as the targets of the new nullary rules.
Both run translations are proved.

Variable alignment uses an explicit inverse-pruning lift after
determinization and completion. A collapsed node receives the fixed
nullary-transition state irrespective of its children. The zero-track
alphabet is the singleton nullary alphabet {top}; deleting the last
track uses all productive states and retains arbitrarily deep finite
witnesses.

## Sources and current remaining work

The primary encoding derivation is documented in
p09-tata-wsks-encoding-proof-note.md, from the locally held official
TATA 2008 release. Its older admission records describe earlier
snapshots, not this expanded text.

The bounded renewed Thatcher--Wright search is recorded in
p09-thatcher-wright-acquisition-source-note.md. Neither the 1968
article nor RC-1713 was obtained. The locally held Thatcher
dissertation is a distinct work and is not used as a substitute.
The source-dependent N15 obligation remains open.

## Direct mathematical readings

An independent reader checked the actual generic automaton
constructions and their representation bounds. Another checked the
actual complete finite-domain MSO proof and its host statement.
Both found no concrete mathematical defect in their assigned scopes.
The canonical WSkS incorporation received its own bounded
source/mathematical reading. The reader confirmed the checker, atomic
automata, pruning image and inverse-image constructions, and requested
two explicit instructions: align the free variables before conjunction,
and determinize/complete the zero-track automaton before lifting it.
Both instructions are now incorporated into the actual LaTeX.

The named-theorem index and Part IX lookup now point to the supplied
finite-tree proof. This is authoring progress, not a claim that the
entire manuscript is ready for publication.
