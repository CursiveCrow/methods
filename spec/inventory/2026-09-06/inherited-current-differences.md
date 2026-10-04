# Current inherited-source differences

This report records actual text differences, without altering or condemning them. Current correction policy must be applied by reading the changed passages and provenance.

## handbook/restoration/inherited-10675-10769.tex

Active: True. Source lines 10675–10769. Current file SHA-256: `b745b19a1b07592a4cd59fec1791b3102e88b3c53e30f276c06ca168ebc1d57a`.

```diff
--- source/formal-logic-reference.tex:10675-10769
+++ handbook/restoration/inherited-10675-10769.tex
@@ -5,7 +5,12 @@
 \label{sec:constructibility-forcing-01}
 
 \begin{definition}[Definable subsets]
-For a set \(A\), let \(\operatorname{Def}(A)\) be the collection of subsets of
+\label{def:p06-def-empty-base}
+Set
+\[
+  \operatorname{Def}(\varnothing)\defeq\{\varnothing\}.
+\]
+For a nonempty set \(A\), let \(\operatorname{Def}(A)\) be the collection of subsets of
 \(A\) definable over the structure \((A,\in)\) by a first-order formula with
 parameters from \(A\):
 \[
@@ -24,6 +29,10 @@
 \(s_{x,\bar a}\) maps \(y\) to \(x\) and each displayed variable in
 \(\bar z\) to the corresponding entry of \(\bar a\); its values on other
 variables are irrelevant.
+The satisfaction clause applies to nonempty \(A\).  The separate empty-base
+clause makes the unique subset of \(\varnothing\) the sole member of
+\(\operatorname{Def}(\varnothing)\), without evaluating a formula in an
+empty structure.
 The satisfaction relation in this definition is the set-sized satisfaction
 relation constructed in the metatheory.  It is not a truth predicate internal
 to \(\ZF\) for the entire universe.
@@ -41,6 +50,7 @@
   L=\bigcup_{\alpha\in\operatorname{Ord}}L_\alpha.
 \]
 A set is constructible iff it belongs to \(L\).
+In particular, \(L_1=\operatorname{Def}(\varnothing)=\{\varnothing\}\).
 \end{definition}
 
 The ordinary Tarskian satisfaction relation fixed earlier takes a set-sized
@@ -92,4 +102,3 @@
 consistency implication is asserted here; the exact relative-consistency
 statements are derived from this scheme in the final section of this
 chapter.
-
```

## handbook/restoration/inherited-11104-11126.tex

Active: True. Source lines 11104–11126. Current file SHA-256: `fc5c0dfca658ca116d180db210ea02ad12445a628b6f1e805386e2c461464956`.

```diff
--- source/formal-logic-reference.tex:11104-11126
+++ handbook/restoration/inherited-11104-11126.tex
@@ -3,6 +3,7 @@
 
 \begin{lemma}[Relativization of derivations]
 \label{lem:relativization-derivations}
+\label{def:p06-relativization-index-erratum}
 Let \(\varphi_1,\ldots,\varphi_k,\psi\) be formulas of \(\Lang_{\in}\) whose
 free variables are among the pairwise distinct variables
 \(v_1,\ldots,v_m\).  If \(\set{\varphi_1,\ldots,\varphi_k}\derives\psi\) in
@@ -11,13 +12,12 @@
   \ZF\derives
   \forall v_1\cdots\forall v_m\,
   \Bigl(
-    \bigwedge_{j\leq m}v_j\in L
+    \bigwedge_{1\leq j\leq m}v_j\in L
     \land
-    \bigwedge_{i\leq k}\varphi_i^{L}
+    \bigwedge_{1\leq i\leq k}\varphi_i^{L}
     \to\psi^{L}
   \Bigr).
 \]
-For \(m=0\) or \(k=0\) the corresponding conjunction is absent from the
-displayed conclusion.
+An empty conjunction denotes \(\top\).  When \(m=0\), the universal
+quantifier block is also empty.
 \end{lemma}
-
```

## handbook/restoration/inherited-11127-11199.tex

Active: True. Source lines 11127–11199. Current file SHA-256: `410062ce1d18f96ff5a58e317052fbbbf64fba1d7a145a44159a4d1a0df60052`.

```diff
--- source/formal-logic-reference.tex:11127-11199
+++ handbook/restoration/inherited-11127-11199.tex
@@ -10,13 +10,14 @@
 \(\forall u_1\cdots\forall u_r\) and the guard hypotheses \(u_j\in L\).
 
 Two bookkeeping devices recur.  First, \(\ZF\derives\exists u\,(u\in L)\):
-by the comprehension reading of \(\operatorname{Def}\), separation proves
-\(\set{x\in L_0:\ldots}=\varnothing\) whatever the satisfaction clause
-returns over the empty domain, which the fixed structure convention
-excludes from semantic evaluation; hence
-\(\varnothing\in\operatorname{Def}(L_0)=L_1\), so \(\varnothing\in L\).
-This derivation does not route through the proof-sketch theorem that \(L\)
-contains every ordinal.  Whenever the induction hypothesis supplies a claim
+Definition~\ref{def:p06-def-empty-base} gives
+\[
+  L_1=\operatorname{Def}(L_0)
+     =\operatorname{Def}(\varnothing)=\{\varnothing\},
+  \qquad \varnothing\in L_1\subseteq L.
+\]
+Thus \(\varnothing\) supplies the required witness directly.
+Whenever the induction hypothesis supplies a claim
 whose variable list contains a variable \(u\) absent from the target node,
 instantiate the universally quantified guarded implication at this witness;
 the vanished variable and its guard disappear.  Second, where the
@@ -70,4 +71,3 @@
 \(v_1,\ldots,v_m\); implication introduction and universal introduction in
 the ambient \(\ZF\) derivation yield the displayed conclusion.
 \end{proof}
-
```

## handbook/restoration/inherited-11914-11960.tex

Active: True. Source lines 11914–11960. Current file SHA-256: `2d8eb98f583c9deb327252df70b2dbbfd36f949d6237e1817873fdf9aeac4302`.

```diff
--- source/formal-logic-reference.tex:11914-11960
+++ handbook/restoration/inherited-11914-11960.tex
@@ -1,47 +1,65 @@
 \section{Interpolation and definability}
 \label{sec:cut-elimination-interpolation}
 
-Interpolation is one of the consequences of cut elimination named in the
-preceding section; its statement, and the definability theorem derived from
-it, are recorded here at cited-theorem level.
+Interpolation produces an intermediate formula in the vocabulary shared by
+an antecedent and its consequence.  Maehara's partition method and the
+relationalization argument below prove it for general first-order signatures.
+Beth definability follows by applying interpolation to two expansions of a
+common reduct.
 
 \begin{theorem}[Craig interpolation]
 \label{thm:craig-interpolation}
-Let \(\varphi\) and \(\psi\) be first-order sentences with
-\(\entails\varphi\to\psi\).  Then there is a sentence \(\theta\) such
+Let \(\varphi\) and \(\psi\) be first-order formulas with
+\(\entails\varphi\to\psi\).  Then there is a formula \(\theta\) such
 that \(\entails\varphi\to\theta\), \(\entails\theta\to\psi\), and
 every nonlogical symbol of \(\theta\) occurs in both \(\varphi\) and
 \(\psi\); equality and \(\bottom\) may occur in \(\theta\)
-regardless.  The degenerate cases are covered because \(\bottom\) and
+regardless.  Moreover,
+\[
+ \FV(\theta)\subseteq\FV(\varphi)\cap\FV(\psi).
+\]
+In particular, sentences have a sentence interpolant.
+The degenerate cases are covered because \(\bottom\) and
 \(\neg\bottom\) are available as interpolants when \(\varphi\) is
 unsatisfiable or \(\psi\) is valid.
-\textit{Status: cited theorem.}
+\textit{Status: proved (Annex~\ref{annex:p7.interp.3}).}
 \end{theorem}
 
-See \cite{TroelstraSchwichtenberg2000} for the proof-theoretic route
-through Maehara's lemma over a cut-free sequent calculus, and
-\cite{Hodges1993} for the model-theoretic route through compactness and
-elementary diagrams.
+The proof uses the partition lemma, direct cut-free completeness for the
+relational fragment, and an explicit graph translation for functions and
+equality.  Historical treatments are
+\cite{Craig1957,Maehara1960,TroelstraSchwichtenberg2000,Hodges1993}.
 
 \begin{theorem}[Beth definability]
 \label{thm:beth}
+Assume the Axiom of Choice in the ambient set theory, as in
+Theorem~\ref{thm:fol-compactness} for arbitrary signatures.
 Let \(T\) be a first-order theory in a signature containing a
-distinguished relation symbol \(R\), and suppose \(T\) defines \(R\)
+distinguished relation symbol \(R\) of finite arity \(n\geq0\), and suppose \(T\) defines \(R\)
 implicitly: any two models of \(T\) with the same reduct to the signature
 without \(R\) interpret \(R\) identically.  Then \(T\) defines \(R\)
 explicitly: some formula \(\theta(\bar x)\) not containing \(R\)
 satisfies
-\(T\derives\forall\bar x\,(R(\bar x)\leftrightarrow\theta(\bar x))\).
-\textit{Status: cited theorem.}
+\[
+ T\derives\forall\bar x\,
+       (R(\bar x)\leftrightarrow\theta(\bar x)),
+ \qquad \FV(\theta)\subseteq\{x_1,\ldots,x_n\}.
+\]
+The theory and its signature may be infinite, and the signature may contain
+functions and constants.  Some finite \(T_0\subseteq T\) already proves
+the displayed definition.  For \(n=0\), both the tuple and its quantifier
+block are empty.
+\textit{Status: proved (Annex~\ref{annex:p7.interp.4}).}
 \end{theorem}
 
-Beth definability follows from Craig interpolation; see \cite{Hodges1993}.
-The Robinson joint-consistency theorem is a further standard equivalent of
-interpolation and is stated and proved in the same source.  The theorem is
-converse to the conservativity of definitional extensions
+The proof is in Annex~\ref{annex:p7.interp.4}; see also
+\cite{Beth1953,Hodges1993}.
+The model-theoretic route through Robinson joint consistency is proved in
+Theorem~\ref{thm:p03-robinson-joint-consistency}, and its equivalence with
+Craig interpolation is Theorem~\ref{thm:p03-craig-robinson-beth}.
+Beth's theorem complements the conservativity of definitional extensions
 (\cref{thm:definitional-conservativity}): adding a defining axiom for
 \(R\) produces a theory that defines \(R\) explicitly, hence implicitly,
 while proving no new sentences of the smaller signature; Beth definability
 states that implicit definability already guarantees an explicit
 definition.
-
```

## handbook/restoration/inherited-13519-13551.tex

Active: True. Source lines 13519–13551. Current file SHA-256: `f2142f552bda2969628d21f60ad90baaf70163e8c478c31021e4d2f95d77e3c3`.

```diff
--- source/formal-logic-reference.tex:13519-13551
+++ handbook/restoration/inherited-13519-13551.tex
@@ -17,7 +17,7 @@
 truth-lemma calculation are omitted; the one-agent instances are controlled by
 \cite[Chapter 4]{BlackburnDeRijkeVenema2001}.
 
-For a finite group \(G\subseteq I\), the language further adds the
+For a nonempty finite group \(G\subseteq I\), the language further adds the
 operators \(E_G\) and \(C_G\), with \(E_GA\) and \(C_GA\) formulas
 whenever \(A\) is a formula.  Everyone-knows is definable by
 \[
@@ -30,4 +30,3 @@
 reachable, so the clause is reflexive.  Common knowledge is therefore a
 reflexive-transitive closure modality; it is not a finite iteration of
 \(E_G\) bounded in advance.
-
```

## handbook/restoration/inherited-13972-14000.tex

Active: True. Source lines 13972–14000. Current file SHA-256: `79ac085c09dd1f0ceda5a1e34a3d46eca61c5786fcab0926cffe5bf82ddecc88`.

```diff
--- source/formal-logic-reference.tex:13972-14000
+++ handbook/restoration/inherited-13972-14000.tex
@@ -21,9 +21,14 @@
   \qquad
   \sem{\mathbf1}=1.
 \]
-The sequent \(A_1,\ldots,A_n\Rightarrow B\) is valid when
+\phantomsection\label{def:p08-imll-empty-tensor}
+For \(n\geq0\), the sequent \(A_1,\ldots,A_n\Rightarrow B\) is valid when
 \[
-  \sem{A_1}\otimes\cdots\otimes\sem{A_n}\leq\sem B
+  \bigotimes_{i=1}^{n}\sem{A_i}\leq\sem B,
+  \qquad
+  \bigotimes_{i=1}^{0}\sem{A_i}\defeq1
 \]
 under every valuation in every such monoid.
-
+In particular, \(\Rightarrow B\) is valid exactly when
+\(1\leq\sem B\) under every valuation, and \(\Rightarrow\mathbf1\)
+is valid by reflexivity of \(\leq\).
```
