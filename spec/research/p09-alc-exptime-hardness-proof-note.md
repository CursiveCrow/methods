# EXPTIME-hardness of ALC concept satisfiability with general GCIs

Date: 2026-09-06.

This note gives a polynomial reduction to plain \(\mathcal{ALC}\)
concept satisfiability relative to a finite general TBox. The output
uses two ordinary roles. It uses no inverse roles, role functionality,
nominals, number restrictions, or ABox.

## 1. Exact external complexity dependency

The independent source dependency is
\[
 \mathsf{APSPACE}=\mathsf{EXPTIME}.
 \tag{CKS}
\]
It is Corollary 3.6 on printed p. 122 of Ashok K. Chandra, Dexter C.
Kozen, and Larry J. Stockmeyer, “Alternation,” Journal of the ACM
28(1) (1981), pp. 114–133,
[DOI 10.1145/322234.322243](https://doi.org/10.1145/322234.322243).
The actual twenty-page
[institutional source PDF](https://people.cs.umass.edu/~immerman/cs601/alternation.pdf)
was opened as text. Theorems 3.3–3.4 immediately precede the corollary;
Section 2 defines the machine semantics. Theorem 2.5 removes negating
states, and Theorem 2.6(b) supplies a globally space-bounded form for
constructible bounds. Its proof of Theorem 5.4, printed p. 131, also
uses a one-tape form with two transitions per nonfinal situation.
The [author's bibliography](https://www.cs.cornell.edu/~kozen/Papers/papers_by_year.htm)
independently fixes the article identity.

No existing Part IV theorem label or bibliography key for (CKS) was
found in the live search, so none is invented here. A suitable new
bibliography key would be ChandraKozenStockmeyer1981. The lower bound
below cites (CKS) directly; it does not derive ALC hardness from a
later result whose own proof assumes that hardness.

Here \(\mathsf{EXPTIME}\) means the union of deterministic time
\(2^{n^{O(1)}}\) classes, and \(\mathsf{APSPACE}\) means alternating
polynomial space. In particular, every language \(K\in\mathsf{EXPTIME}\)
has a fixed polynomial-space alternating machine to which the
construction below applies.

## 2. A precise bounded machine and its acceptance semantics

Fix a machine \(M\) with finite tape alphabet \(\Gamma\), including
blank, and finite disjoint control classes
\[
 Q=Q_\exists\mathbin{\dot\cup}Q_\forall
                  \mathbin{\dot\cup}\{q_{\rm acc},q_{\rm rej}\}.
\]
On input \(w\), a polynomial bound \(s=s(|w|)\geq\max\{1,|w|\}\)
limits the tape to cells \(1,\ldots,s\). The initial tape contains
\(w\), followed by blanks, and the initial head is at cell 1.

For each \(q\in Q_\exists\cup Q_\forall\) and \(\gamma\in\Gamma\),
there are two instructions, indexed by \(j=0,1\):
\[
 \delta_j(q,\gamma)=(q',\gamma',d),
 \qquad d\in\{-1,0,1\}.
\]
They write \(\gamma'\), change control to \(q'\), and move the head
by \(d\). The two instructions may be identical. Accepting and
rejecting controls halt.

A configuration within the bound is a triple
\[
 c=(q,i,u),\qquad q\in Q,\quad 1\leq i\leq s,\quad u\in\Gamma^s.
\]
If an instruction would move outside \(1,\ldots,s\), define its
successor instead to have control \(q_{\rm rej}\), retain the
current valid head position, and perform the specified tape write.
This convention makes both successors \(\tau_0(c),\tau_1(c)\)
well-defined bounded configurations. All such boundary successors
are rejecting, so their otherwise immaterial tape data cannot
create acceptance.

These normalizations preserve the required hardness. A fixed
polynomial-space machine can be simulated on one polynomially
bounded tape by finitely many tracks and head-marker tracks.
Scanning those tracks is deterministic; an existential or universal
branch is made only after the scanned symbols determining the
original move have been collected. Updating the chosen move uses
another finite scan. Arbitrary finite branching is replaced by
binary choice trees of the same existential or universal kind,
with deterministic or single-choice steps duplicated as needed.
If the starting convention permits a nonfinal case with no moves,
replace it by its prescribed halting answer: an empty existential
choice rejects, and an empty universal choice accepts under the
usual empty-conjunction convention. Two identical moves to that
answer remove the empty choice. The normalized machine used here
has exactly two moves in every nonhalting situation.
Halting answers are given their designated controls. A polynomial
space limit can be enforced explicitly. No claim that an arbitrary
unbounded machine already has these properties is made.

### Finite accepting trees

An accepting tree rooted at a configuration \(c\) is a finite rooted
tree labelled by bounded configurations with these conditions:

- Every leaf has control \(q_{\rm acc}\).
- At an existential configuration, exactly one instruction index
  \(j\in\{0,1\}\) is selected and the node has one child labelled
  \(\tau_j(c)\).
- At a universal configuration, the node has two children, one for
  each index \(j\), labelled \(\tau_j(c)\).
- Rejecting configurations do not occur.

Duplicated successor configurations are allowed as distinct tree
occurrences. The machine accepts precisely when its initial
configuration has such a finite tree. A loop alone is not acceptance.

The finite-tree semantics can also be calculated on the finite set
\(\mathcal C_s=Q\times\{1,\ldots,s\}\times\Gamma^s\). Put
\[
 W_0=\varnothing,
\]
\[
 W_{t+1}=
 \mathcal C_{\rm acc}
 \cup\{c\in\mathcal C_\exists:
                  \tau_0(c)\in W_t\text{ or }\tau_1(c)\in W_t\}
 \cup\{c\in\mathcal C_\forall:
                  \tau_0(c),\tau_1(c)\in W_t\}.
 \tag{1}
\]
Induction on \(t\) proves that \(W_t\) contains exactly the
configurations having an accepting tree of height at most \(t-1\),
where height counts edges and the case \(t=0\) contains none.
This proves equivalence of the operational tree definition and
the least-fixed-point calculation.

Write
\[
 q=|Q|,\qquad g=|\Gamma|,\qquad N=q\,s\,g^s.
\]
There are \(N\) bounded configurations. The increasing sequence
(1) stabilizes by stage \(N\), since each strict stage adds a
configuration. Consequently, if any accepting tree exists, there
is one of height at most \(N-1\).

More explicitly, give each accepted configuration its first
entry stage in (1). At an existential node select an instruction
with smaller entry stage; at a universal node both successors
have smaller stages. These choices give a positional accepting
strategy and the asserted height bound.

The bound is existential: not every accepting history-dependent
strategy must have height at most \(N-1\). Such a strategy might
deliberately traverse a loop finitely many times before accepting.
The reduction needs only the existence of the bounded strategy
just constructed.

## 3. Target problem and names

An instance of the target problem is an ALC concept \(C\) and a
finite set \(\mathcal T\) of GCIs \(E\sqsubseteq F\). It is
satisfiable when an interpretation with nonempty domain satisfies
every GCI at every domain element and has some element in \(C\).

Use two role names \(r_0,r_1\), and these concept names:
\[
 \mathsf Q_q\quad(q\in Q),\qquad
 \mathsf H_i\quad(1\leq i\leq s),\qquad
 \mathsf A_{i,\gamma}\quad(1\leq i\leq s,\ \gamma\in\Gamma).
\]
They record control, head position, and tape symbols. Add rank-bit
concept names
\[
 \mathsf B_0,\ldots,\mathsf B_{b-1},
\]
with bit 0 least significant. Choose
\[
 b=1+\lceil\log_2 q\rceil+\lceil\log_2 s\rceil
                              +s\lceil\log_2 g\rceil.
 \tag{2}
\]
This is positive, also when \(s=1\) or \(g=1\), and
\[
 2^{b-1}\geq N,\qquad R:=2^b-1\geq N.
 \tag{3}
\]
Only \(b\) concept names and an all-ones initial bit string are
written; no unary representation of \(R\) is produced.

The following displayed families define \(\mathcal T_{M,s}\)
completely. Indexed symbols and semantic arithmetic in the
explanation are metanotation, not extra ALC constructors.

## 4. Global configuration GCIs

Exactly one control holds at each element:
\[
 \top\sqsubseteq\bigsqcup_{q\in Q}\mathsf Q_q,
 \qquad
 \mathsf Q_q\sqcap\mathsf Q_{q'}\sqsubseteq\bot
                   \quad(q\ne q').
 \tag{4}
\]
Exactly one head position holds:
\[
 \top\sqsubseteq\bigsqcup_{i=1}^s\mathsf H_i,
 \qquad
 \mathsf H_i\sqcap\mathsf H_{i'}\sqsubseteq\bot
                   \quad(i\ne i').
 \tag{5}
\]
For each cell, exactly one tape symbol holds:
\[
 \top\sqsubseteq\bigsqcup_{\gamma\in\Gamma}\mathsf A_{i,\gamma},
 \qquad
 \mathsf A_{i,\gamma}\sqcap\mathsf A_{i,\eta}\sqsubseteq\bot
                   \quad(\gamma\ne\eta).
 \tag{6}
\]
Thus each model element describes one bounded configuration.
Different elements may describe the same configuration.

Rejecting halt is forbidden, and accepting halt needs no further
computation:
\[
 \mathsf Q_{q_{\rm rej}}\sqsubseteq\bot,
 \qquad
 \mathsf Q_{q_{\rm acc}}\sqsubseteq
                     \forall r_0.\bot\sqcap\forall r_1.\bot.
 \tag{7}
\]
The second GCI permits accepting leaves and fixes their halt
behavior; it does not require an accepting element to exist.

The branching requirements are
\[
 \mathsf Q_q\sqsubseteq
       (\exists r_0.\top\sqcup\exists r_1.\top)
                   \quad(q\in Q_\exists),
 \tag{8}
\]
\[
 \mathsf Q_q\sqsubseteq
       (\exists r_0.\top\sqcap\exists r_1.\top)
                   \quad(q\in Q_\forall).
 \tag{9}
\]
These GCIs impose existence, not uniqueness, of successors.

## 5. Updates and unchanged tape cells

For each nonhalting \(q\), cell \(i\), symbol \(\gamma\), and
instruction index \(j\), use the guard
\[
 G_{q,i,\gamma}=
           \mathsf Q_q\sqcap\mathsf H_i\sqcap\mathsf A_{i,\gamma}.
\]
Compute the bounded instruction data
\((q',i',\gamma')\) as in Section 2, including its rejecting
boundary convention. Include
\[
 G_{q,i,\gamma}\sqsubseteq
       \forall r_j.
       (\mathsf Q_{q'}\sqcap\mathsf H_{i'}\sqcap
                                      \mathsf A_{i,\gamma'}).
 \tag{10}
\]
This updates the control, the head, and the scanned cell.
For every \(i,\gamma,j\), also include the frame GCI
\[
 \neg\mathsf H_i\sqcap\mathsf A_{i,\gamma}
                \sqsubseteq\forall r_j.\mathsf A_{i,\gamma}.
 \tag{11}
\]
Every unscanned tape cell is therefore unchanged along either role.
The scanned cell is governed by (10), not by (11).

By (4)–(6), exactly one update guard is active at a nonhalting
element. It follows that every \(r_j\)-successor, if present,
describes exactly the machine successor \(\tau_j(c)\). Multiple
successor elements are harmless: they must have the same required
configuration data, although they need not be the same element.
If an instruction crosses the tape boundary, its target control
is rejecting, and (7) consequently makes that role impossible
at the guarded element.

## 6. Exact decrement using polynomially many rank-bit clauses

Use the abbreviations
\[
 Z=\bigsqcap_{\ell<b}\neg\mathsf B_\ell,\qquad
 L_j=\bigsqcap_{\ell<j}\neg\mathsf B_\ell.
 \tag{12}
\]
In particular \(L_0=\top\). These are concept expressions,
not new primitive predicates. Expand them when counting size.

For every bit \(j<b\) and role \(r\in\{r_0,r_1\}\), include all
four GCIs
\[
 \begin{aligned}
 L_j\sqcap\mathsf B_j
      &\sqsubseteq\forall r.\neg\mathsf B_j,\\
 L_j\sqcap\neg\mathsf B_j
      &\sqsubseteq\forall r.\mathsf B_j,\\
 \neg L_j\sqcap\mathsf B_j
      &\sqsubseteq\forall r.\mathsf B_j,\\
 \neg L_j\sqcap\neg\mathsf B_j
      &\sqsubseteq\forall r.\neg\mathsf B_j.
 \end{aligned}
 \tag{13}
\]
Finally include
\[
 Z\sqsubseteq\forall r_0.\bot\sqcap\forall r_1.\bot.
 \tag{14}
\]
For \(j=0\), the two clauses guarded by \(\neg L_0=\bot\) are
vacuous; leaving them in the finite list is harmless.
All negations can be pushed to concept names by the ordinary
ALC Boolean laws.

For a model element \(d\), define its semantic rank
\[
 v(d)=\sum_{j<b}2^j\,\mathbf 1_{d\in\mathsf B_j}.
\]
If \(v(d)=0\), (14) forbids any successor of either role.
If \(v(d)>0\), let \(\ell\) be its least set bit. Along every
role edge, (13) changes each lower bit from 0 to 1, changes
bit \(\ell\) from 1 to 0, and leaves every higher bit unchanged.
Therefore
\[
 (d,e)\in r_j^{\mathcal I}
        \quad\Longrightarrow\quad v(e)=v(d)-1.
 \tag{15}
\]
There is no underflow because (14) forbids the only case in
which binary subtraction could wrap from 0 to all ones.

This rank is essential for machines that may loop. Without it,
an existential self-loop configuration with no accepting
continuation could be represented by a self-looping ALC model.
Equations (13)–(14) exclude that spurious infinite witness.

## 7. The initial concept

Let \(u^0_i\) be the initial symbol of cell \(i\): the corresponding
input symbol when \(i\leq|w|\), and blank otherwise. Define
\[
 C_w=
   \mathsf Q_{q_{\rm init}}\sqcap\mathsf H_1
   \sqcap\bigsqcap_{i=1}^s\mathsf A_{i,u^0_i}
   \sqcap\bigsqcap_{j<b}\mathsf B_j.
 \tag{16}
\]
Its rank is \(R=2^b-1\), and its configuration is exactly the
bounded initial configuration. Empty input is covered by
\(s\geq1\) and the all-blank tape.

The reduction outputs
\[
 w\longmapsto (C_w,\mathcal T_{M,s(|w|)}).
\]

## 8. Acceptance gives an ALC model

Suppose \(M\) accepts \(w\). Section 2 supplies an accepting
tree of height at most \(N-1\). Use its finitely many node
occurrences as the interpretation domain. Interpret the
configuration concepts according to each node's labelled
configuration.

At an existential node, put its selected child in the role
corresponding to the chosen instruction. At a universal node,
put its two indexed children in \(r_0,r_1\), respectively.
There are no other role edges, and accepting leaves have none.
At depth \(d\), interpret the rank bits as the binary expansion
of \(R-d\). This is nonnegative by (3) and the tree-height bound.

The one-hot GCIs (4)–(6) hold because every label is a
configuration. Reject does not occur and accepting nodes are
leaves, so (7) holds. The shape of the accepting tree gives
(8)–(9). Actual machine transitions give (10)–(11), and the
depth assignment gives (13)–(14). The root satisfies (16).
Thus \(C_w\) is satisfiable relative to \(\mathcal T_{M,s}\).

## 9. An arbitrary ALC model gives a finite accepting tree

Conversely, let \(\mathcal I\models\mathcal T_{M,s}\) and take
\(d_0\in C_w^{\mathcal I}\). No finiteness or tree shape of
\(\mathcal I\) is assumed.

We prove by induction on \(v(d)\) that the configuration
described by every element \(d\) has a finite accepting tree.
If its control is accepting, the one-node tree suffices.
Its control cannot be rejecting by (7).

If the control is nonhalting, (8) or (9) requires an outgoing
role edge. Thus its rank cannot be zero, by (14).
At an existential control, choose an index \(j\) for which
an \(r_j\)-successor exists and choose one such successor \(e\).
At a universal control, choose one witness for each of the
two roles. By (10)–(11), these witnesses describe precisely
the required machine successors. By (15), their ranks are
one smaller, so the induction hypothesis supplies finite
accepting trees for them. Attach one tree at an existential
node and both at a universal node.

The result is finite at each induction step. The role
witnesses may coincide as model elements or may describe
the same configuration; duplicating their occurrences in
the accepting tree is permitted. Extra successors do not
invalidate the argument because all satisfy the same
transition and rank constraints.

At rank zero the preceding argument forces accepting control,
so the induction has a valid base. At \(d_0\), (16) identifies
the initial machine configuration. Therefore \(M\) accepts
\(w\). Together with Section 8,
\[
 w\in L(M)
 \quad\Longleftrightarrow\quad
 C_w\text{ is satisfiable with respect to }\mathcal T_{M,s}.
 \tag{17}
\]

## 10. Polynomial size and exact complexity scope

There are
\[
 q+s+sg+b
\]
concept names and two roles. Expanding the abbreviations,
the total number of concept-symbol occurrences in the GCI
families is
\[
 O(q^2+s^2+sg^2+qsg+b^2).
 \tag{18}
\]
The terms come respectively from the one-hot restrictions,
the transition guards, and the expanded lower-zero bit
tests. The frame clauses contribute only \(O(sg)\).
The initial concept has \(O(s+b)\) occurrences.
Encoding the indexed names introduces only a logarithmic
factor. All lists can be generated directly in time polynomial
in these parameters.

For hardness, fix any \(K\in\mathsf{EXPTIME}\). By (CKS), choose
one fixed normalized alternating machine \(M\) for \(K\) and
a fixed polynomial bound \(s(|w|)\). Then \(q,g\) are constants,
\(s\) and \(b\) are polynomial in \(|w|\), and (18) is polynomial.
Equation (17) is a polynomial many-one reduction from \(K\).
Therefore plain ALC concept satisfiability with finite general
GCIs is EXPTIME-hard in combined complexity.

Equivalently, one may use a uniform bounded-machine input
\((M,w,1^s)\), with \(M\) already in the stated binary form.
The same output is polynomial in that encoding, and the
configuration graph has at most \(qsg^s\) vertices, exponential
in a polynomial of the input length. Its least-fixed-point
acceptance calculation gives the corresponding EXPTIME upper
bound for that bounded-machine source problem. The unary
space bound matters: this construction is not claimed
polynomial when an arbitrary \(s\) is supplied in binary.

The reduction does not establish hardness for a fixed TBox
or data complexity. The TBox and its vocabulary grow with
the tape and counter lengths. Input content is encoded by
the queried concept; the role vocabulary remains fixed.
It also does not establish the lower bound for TBox
consistency without a queried concept, since an unrelated
accepting configuration could otherwise supply a model.

## Outcome and incorporation boundaries

The full construction establishes the requested lower bound
without adding any non-ALC constructor. Its external
complexity dependency is the explicitly cited CKS
characterization; the accepting-tree semantics, finite
configuration rank, bit-counter GCIs, both model directions,
and polynomial count are proved here.

The only necessary qualification to the proposed plan is
the rank-height wording: acceptance guarantees the
existence of a bounded-height accepting strategy, not
the bound for every history-dependent accepting strategy.
No other flaw was found in this reduction approach.

The research and PDF skills were used for the primary
CKS locator. The explicit no-new-agents instruction
overrode the research skill's usual delegation step.
No handbook edits, software tests, builds, or renders
were performed.
