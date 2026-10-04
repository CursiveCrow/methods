# Internal cartesian language: independent mathematical review

Reviewed on 2026-09-06 (local date), against the actual saved manuscript.

## Scope and outcome

**Scoped mathematical pass. No necessary mathematical repair found.**

Read both complete files:

- handbook/parts/p10/internal-cartesian-language.tex, lines 1–189.
- handbook/annex/p10/internal-cartesian-language.tex, lines 1–283.

Also read the complete body and annex of cartesian-lambda.tex for the syntax, typed equational substitution, context products and exponentials, and categorical interpretation interface. Checked the live def:p10-ccc definition. No other review conclusions were read.

This review covers the stated small-category construction with chosen terminal object, products, and exponentials, and with the **full true equations-in-context diagram**. It does not replace source attribution review or establish a smaller finite axiom basis, a free-category universal property, host/driver integration, or typeset quality. No tests, builds, or renders were run. No manuscript file was edited.

## 1. Language, interpretation, and diagram

Body lines 6–10 specify smallness and chosen categorical structure. Lines 14–37 give a set of named base types and correctly typed closed constants. In particular:

- The named base type for the object \(B^A\) is distinguished syntactically from the arrow type formed from the named \(A,B\) types.
- Both types interpret as the same chosen object \(B^A\). Consequently \(e_{A,B}\) and \(l_{A,B}\) can denote the identity unary arrow on that object.
- Body lines 49–60 correctly convert a unary arrow into a closed constant by currying its composite with \(1\times A\to A\); the pairing constant is doubly curried from \((1\times A)\times B\to A\times B\).
- The all-context interpretation of a closed constant is its closed denotation composed with the unique map to the terminal object, as explicitly supplied in annex lines 8–16.

The leading terminal factor is retained in body lines 39–45. No later proof needs a literal equality \(1\times A=A\).

Body lines 67–80 define the theory by **all** semantically true typed equations, with the specified closure operations. Lines 82–110 explicitly say that the displayed structural equations are only a subfamily. The faithfulness proof invokes arbitrary semantic equations and is authorized to do so. No claim of effective enumeration or finite axiomatization is made.

Annex lines 18–30 establish
\[
M=_{\mathcal C}N \quad\Longleftrightarrow\quad
\llbracket M\rrbracket=\llbracket N\rrbracket.
\]
The forward direction uses soundness of every closure operation; the reverse direction uses membership in the defined full diagram. This is not circular with the later categorical equivalence: the interpretation is defined first in the already given category, and the semantic substitution proof extends the earlier pure-language induction by the constant case.

All displayed structural equations in body lines 88–105 are well typed and true with these interpretations. The transposition equation uses \(d:\underline D\) and \(a:\underline A\), and follows from the evaluation equation for \(\Lambda f\).

## 2. Recursive type comparisons and packing

Annex lines 33–65 define the two comparisons by structural recursion on types. In the arrow step:

- \(\iota_S a\) has type \(S\); \(h(\iota_S a)\) has type \(T\); applying \(\kappa_T\) produces the named \(B\) type. Its abstraction therefore has the input type required by \(l_{A,B}\).
- Conversely, \(\kappa_S s\) has named \(A\) type, \(e_{A,B}z\) has named \(A\)-to-\(B\) arrow type, and \(\iota_T\) returns a term of type \(T\).

The parameterized evaluation/currying calculation in lines 49–61 proves that these are identity unary maps on the interpreted objects, not merely equations tested on closed elements. Hence their composites belong to the full diagram in arbitrary contexts. The argument does not assume that the category is well pointed.

Packing at annex lines 68–80 starts with \(u:\underline1\), whose term denotation is \(1_1\), and adds one factor by categorical pairing. Induction therefore gives a packing **term** with denotation \(1_{P_\Gamma}\).

The distinction in lines 82–97 is exact:
\[
E(\operatorname{pack}_\Gamma)=s_{P_\Gamma}
=\langle!,1_{P_\Gamma}\rangle:
P_\Gamma\longrightarrow1\times P_\Gamma,
\]
whereas
\[
E(\operatorname{unpack}_\Gamma)=\varepsilon_{P_\Gamma}
=\pi_2:1\times P_\Gamma\longrightarrow P_\Gamma.
\]
Each unpacking component uses the correctly typed constant for
\(\rho_i:P_\Gamma\to A_{T_i}\), followed by \(\iota_{T_i}\).
The tuple's terminal component is unique, so the stated components determine its entire arrow.

Lines 99–112 prove both inverse equations, including the empty context: its unpacking tuple is empty, and the other composite is the diagram equation \(z=u\) at the named terminal type.

## 3. Fullness, faithfulness, and the equivalence

Annex lines 119–128 define evaluation on tuple classes and establish functoriality using semantic substitution. It does not require the equivalence theorem as an input.

For fullness, lines 131–146 correctly realize arbitrary
\(f:P_\Gamma\to P_\Delta\) by
\[
\operatorname{unpack}_\Delta\circ J(f)\circ
\operatorname{pack}_\Gamma.
\]
The middle tuple denotes \(1_1\times f\), giving
\[
\varepsilon_{P_\Delta}(1_1\times f)s_{P_\Gamma}=f.
\]
The source and target of every map match, including empty contexts.

Faithfulness at lines 149–154 follows by projecting equality of tuple arrows to the corresponding term arrows and invoking the full diagram. No missing surjectivity of closed terms, well-pointedness, or representative-selection principle is used. Essential surjectivity at lines 155–157 has the explicit representative \((\underline A)\) and isomorphism \(\varepsilon_A\).

The explicit \(J\) at lines 160–163 respects identities and composition by the displayed diagram equations. Its composite \(EJ\) acts as \(1\times(-)\) on both objects and arrows.

The counit naturality calculation at lines 164–169 has type \(1\times A\to B\). Unit naturality at lines 171–177 compares two arrows with common source \(\Gamma\) and target \(JE(\Delta)\); applying the already established faithful functor gives the same arrow \(s_{P_\Delta}E(M)\).

Both triangle identities at lines 178–190 are correct:

- \(\varepsilon_{E\Gamma}E(\eta_\Gamma)=\varepsilon_{P_\Gamma}s_{P_\Gamma}=1\).
- \(J(\varepsilon_A)\eta_{J(A)}\) is represented, after the identity comparison's beta step, by \(c_{\pi_2}(\mathsf{pair}_{1,A}\,u\,x)=x\).

The construction of \(J,\eta,\varepsilon\) is explicit and avoids arbitrary choices of representatives of isomorphism classes.

## 4. Products and exponentials

Annex lines 198–209 validly reuse the context-category CCC proof. Constants require only the additional constant substitution case; the equation theory already contains beta and eta and is a typed substitution congruence. Additional equations therefore preserve the evaluation/transposition inverse identities.

The canonical product comparison and its inverse in lines 212–227 use the recursive context product projections. They account for both leading terminal factors and all empty blocks. Projection uniqueness proves the stated naturality and coherence.

The exponential argument in lines 230–270 is independent of any prior assumption that \(E\) preserves exponentials. For arbitrary \(D\) and \(f:D\times P_\Gamma\to P_\Delta\), it first obtains the syntactic arrow with interpretation
\[
f\circ(\varepsilon_D\times1)\circ j_{J(D),\Gamma}.
\]
Transposition exists in the independently established syntactic CCC. Precomposing its interpretation with \(s_D\) gives the requested arrow out of \(D\). The product comparison's naturality proves its evaluation equation.

For uniqueness, fullness supplies a syntactic arrow representing \(q'\varepsilon_D\), faithfulness identifies its uncurrying with the original arrow, and syntactic transpose uniqueness identifies the transposes. Every dependency has already been proved, so there is no circular appeal to preservation of exponentials.

The resulting universal property proves that the specified
\[
\chi_{\Gamma,\Delta}=
\Lambda\!\left(E(\operatorname{ev}_{\rm syn})
                 j_{\Delta^\Gamma,\Gamma}^{-1}\right)
\]
is an isomorphism. The inverse and both inverse equations follow from the two exponential universal properties, as stated at lines 264–270.

The empty cases at lines 272–275 correctly compare \(P_\Delta\) with \(P_\Delta^1\), and \(1\) with \(1^{P_\Gamma}\), rather than silently treating those chosen objects as equal. The final statement about \(J\)'s named-object comparisons is supported by \(u\), pairing/projections, and the inverse \(e,l\) equations already listed in the diagram.

## Interface and proof limits

All invoked lambda interface labels exist in the actual saved body/annex: def:p10-stlc-beta-eta, thm:p10-stlc-equational-substitution, def:p10-stlc-context-category, thm:p10-stlc-context-ccc, def:p10-stlc-ccc-interpretation, and thm:p10-stlc-ccc-completeness. Their use here respects the arrow-only syntax and the distinction between a term's codomain object and a singleton context's product interpretation.

The reconstruction theorem is correctly scoped to the named language with the full true equational diagram. It does not follow for bare beta-eta syntax from mere interpretability in a CCC, and the body explicitly distinguishes those statements at lines 185–189.
