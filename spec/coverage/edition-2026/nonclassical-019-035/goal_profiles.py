"""Manual finite goal/source allocations; no manuscript acceptance."""
PROFILES = []
def goal(n, anchors, setup, related, failure, components):
    PROFILES.append(dict(id=f'N-b-{n:03}', part='p11' if n <= 24 or n >= 34 else 'p08',
        anchors=anchors.split(';'), setup=setup.split(';'), related=related.split(';') if related else [],
        failure=failure, components=[dict(sources=s, text=t) for s,t in components]))

goal(19,'def:p11-tarski-truth','Typed expressions/names and metalanguage translation;Satisfaction recursion with assignments;The exact arithmetic diagonal/undefinability theorem','',
 'Convention T becomes a truth definition or unrestricted object-language schema; stronger-metalanguage truth is ruled out by same-language undefinability.',[
 ([1,2],'State Convention T with sentence names and translated right-hand sides; distinguish material adequacy, recursive satisfaction and object-language disquotation.'),
 ([1],'Reconstruct the selected1935 formal truth/satisfaction and semantic closure/undefinability arguments with exact language/metatheory resources and separate original/translation roles.'),
 ([1,2],'Construct L0,L1,... with each successor naming and evaluating the preceding language; type every truth predicate and show how the hierarchy excludes the displayed same-level liar.'),
 ([2],'Present the1944 semantic conception argument, adequacy demands, objections, replies and applications separately from the1935 technical theorem.'),
 ([1,2],'Work a correct truth instance, an ill-typed self-application and a restricted arithmetic truth predicate; distinguish restriction from general same-language truth.')])

goal(20,'def:p11-kripke-truth','Interpreted truth-free base and syntax coding;Consistent partial truth/falsity extensions and information order;Strong Kleene operations/quantifiers;Ordinal recursion, chain unions and explicit maximality/choice assumptions','N-b-019;N-b-021;N-b-022;N-b-025',
 'Base facts are undefined; successor/limit clauses vanish; maximal means greatest; distinct jumps merge; a least-fixed-point sketch supplies all presentations.',[
 ([1,2,3],'Fix truth-free base values, code domain, positive/negative extensions and information order; give every Strong Kleene jump clause including quantifiers and non-sentence codes.'),
 ([1,2,3],'Prove monotonicity; define empty-truth-extension start, successors and union limits; prove stabilization at the stated set-size bound and least-fixed-point minimality.'),
 ([1,2,3],'Give consistent maximal-fixed-point existence/extension under its actual metatheoretic assumptions; distinguish maximal, greatest, intrinsic and least fixed points.'),
 ([1,2,3],'Define groundedness at the least fixed point and paradoxicality across fixed points; calculate grounded assertions, liar and ungrounded truth-teller without equating ungrounded with paradoxical.'),
 ([1,2],'Retain alternative evaluation/supervaluation comparisons and ghost-of-hierarchy limits; identify metalinguistic classifications unavailable in the object truth language.'),
 ([2],'Separate Martin–Woodruff1984pp47–51, Kripke1984pp53–81 and relevant editor introduction; compare original/reprint bodies before proof reuse.'),
 ([3],'Relate Halbach2011 semantic fixed points and KF without identifying an axiom theory with its least model; preserve applicable first-edition corrections.')])

goal(21,'def:p11-kripke-truth','Classical base satisfaction under a truth hypothesis;Ordinal revision sequences;Source-specific admissible limit assignments','N-b-020;N-b-022',
 'One oscillation replaces either construction; revision is information-monotone without proof; limit policy and stable/nearly-stable sequence quantifiers vanish.',[
 ([1],'Reconstruct Herzberger1982 Notes61–102: initial hypotheses, classical successor revision, limit policy, grounding/stability and eventual behavior; acquire the exact erratum at371.'),
 ([2],'Present Gupta–Belnap circular definitions and truth specialization, admissible sequences, successor rule, limit constraints and separate revision-system policies.'),
 ([1,2],'Define stable, nearly stable, categorical and recurrent/periodic behavior with exact eventual-stage and sequence quantifiers, preserving source differences.'),
 ([1,2],'Calculate a grounded assertion, liar oscillation and a limit-sensitive example with initial hypothesis and every required limit choice.'),
 ([1,2],'Compare revision with static partial fixed points and give the philosophical argument for circular truth; preserve source proof/sketch boundaries and separately owed proofs.')])

goal(22,'def:p11-axiomatic-truth','PA syntax/coding of terms, sentences, substitution and evaluation;Classical versus partial consequence;Arithmetic versus expanded-language induction;Conservation, model expansion, interpretation, reflection and consistency','N-b-019;N-b-020;N-b-021',
 'Acronyms replace theories; CT-minus gains truth induction; theorem rules apply under open assumptions; invalid first-edition proofs survive; strength measures merge.',[
 ([3,4],'Specify TB sentence disquotation over PA, sentence class and arithmetic induction; uniform disquotation and expanded-language induction are separate variants.'),
 ([3,4],'Display typed CT-minus guards and every compositional clause over PA; distinguish CT with expanded truth-language induction and give exact induction schemas.'),
 ([2,3,4],'Specify KF base/outer logic, positive-negative Strong Kleene clauses, truth iteration, coding and induction; distinguish consistency/completeness/minimality extensions and PKF.'),
 ([1,3,4],'Specify FS compositional axioms and theorem-level truth introduction/elimination; reconstruct the original Friedman–Sheard complete axiom/rule-subset classification with native labels.'),
 ([1,2,3,4],'Supply precisely scoped arithmetical conservation, model expansion, consistency, interpretation and strength claims for each displayed variant, with individual source/proof bindings.'),
 ([2],'Retain Feferman1991 reflective closure for schematic theories and PA examples, identifying its relation to KF without reducing the article to that acronym.'),
 ([3],'Carry Halbach2011 Theorem7.8 repair and removal of incorrect Theorem8.5 proof into correction work; do not silently substitute2014 pagination or validate the removed proof.'),
 ([4],'Present Horsten2011 inferential deflationism and the role of each formal theory; distinguish philosophical conclusions from conservation/strength theorems.')])

goal(23,'sec:p11-paradoxes','Declared truth language and diagonalization;Exact truth/conditional/contraction rules;Expression naming, effective syntax and length','N-b-019;N-b-020;N-b-021;N-b-022;N-b-026',
 'Paradoxes get names only; Curry proves only bottom; infinite dependence vanishes; semantic definability becomes computability; response omits its changed premise/rule.',[
 ([3,4],'Formalize strengthened-liar revenge in an exact truth/status language, derive it and identify extra metalinguistic predicates and rejected closure/rules.'),
 ([1,3,4],'For arbitrary target A form C equivalent to(T(code(C)) implies A); derive A with truth, conditional and contraction steps explicit; retain Curry1942 native formalism and show the blocking restriction.'),
 ([2,4],'Give Yn equivalent to every later Ym being false and prove no classical assignment in the stated arithmetic/infinitary setup; distinguish no direct self-reference from stronger noncircularity.'),
 ([3],'Type Grelling names, predicates and heterological application; reconstruct Priest2006 section1.2 satisfaction-diagonal proof at11 with its naming,substitution and closure assumptions, then work a type-restricted diagnosis.'),
 ([3],'Fix Berry alphabet, descriptions, definability/denotation and length; reconstruct Priest2006 section1.8 at25–27, including possibly nondenoting terms,restricted instantiation,finite-length counting and the derivation without excluded middle; compare the separately identified Kolmogorov-complexity variant without assuming effective definability.'),
 ([3,4],'Compare all five paradoxes under hierarchical, partial, revisionary, axiomatic and paraconsistent responses; each comparison names changed principles and worked success/failure.')])

goal(24,'def:p11-sorites;def:p08-supervaluation;thm:p08-supervaluation-classical','Tolerance-chain consequence;Admissible precisifications of a base;Truth degrees and exact consequence','D-P10-026;N-b-028;N-b-029',
 'Global supertruth equals pointwise consequence; admissibility/completeability vanish; degree means probability; epistemicism becomes modal epistemic logic; contextualism has no identified account.',[
 ([1,2,3,4],'Display sorites endpoints and tolerance steps, separate borderline cases from inconsistent premises, and name each selected theory changed premise/inference.'),
 ([1,3],'Define Fine specification order, admissibility, completeability and supertruth/superfalsity/indeterminacy; give tautology preservation and exact converse restrictions.'),
 ([1,3],'Define local consequence within precisifications and global supertruth preservation across spaces; compare quantifier scope, deduction behavior and separating examples.'),
 ([4],'Present Smith2008 fuzzy plurivaluationism and degree argument with conditional, admissibility and higher-order commitments, distinct from a bare t-norm table.'),
 ([2],'Present Williamson1994 sharp-boundary epistemicism, inexact knowledge and margin-for-error argument with sorites/higher-order replies.'),
 ([3],'Present Keefe2000 comparison method, positive supervaluationism and criticisms; chapter6 pragmatic account supplies the contextualist pointer.'),
 ([1,2,3,4],'Compare one fixed sorites case across all four treatments, recording language, truth, consequence and costs with separate attribution.')])

goal(25,'def:p08-fde-matrix;def:p08-fde-orders;thm:p08-k3-lp-facts','Boolean support pairs;Finite matrix designation and finite-premise tableaux','D-P10-024',
 'Neither/both merge; two orders become one; shared K3/LP operations imply same consequence; multiple-conclusion duality becomes unqualified single-conclusion equivalence.',[
 ([1,2,3],'Give constant-free FDE negation/conjunction/disjunction, values, operations and designation; work nonexplosion and excluded-middle countervaluations.'),
 ([1],'Reconstruct Dunn1976 coupled-trees semantics and adequacy in its native structures/consequence, with explicit support-pair bridge.'),
 ([2],'Present Belnap1977 information-processing rationale and two lattice orders with exact operations and inference policy.'),
 ([3],'Retain Omori–Wansing2017 historical/formal comparison and the actual fragments/extensions/consequence conventions.'),
 ([1,2,3],'Supply finite tableau adequacy/decision, K3/LP submatrices and correctly scoped theorem-set/multiple-conclusion duality proofs, distinguishing editorial specialization from source attribution.')])

goal(26,'def:p08-paraconsistency;def:p08-inclosure-schema','Matrix consequence and explosion;Truth/designation/denial/acceptance;Typed collections and closure/transcendence','N-b-023;N-b-025',
 'Paraconsistency equals true contradictions; LP alone resolves Curry; inclosure assumes its own unrestricted premises; later schema is attributed to1979.',[
 ([1],'Reconstruct Priest1979 LP valuation/designation, nonexplosion, paradox motivation and source validity claims.'),
 ([2],'Present Priest2006 second-edition dialetheism/semantic-closure argument, entailment/disjunctive-syllogism replies and relevant later autocommentary.'),
 ([2],'Give Omega,delta,psi and all inclosure assumptions; derive contradiction at X=Omega and work an instance; use separately identified Priest2002 chapter9 for the native schema.'),
 ([1,2],'Compare true contradiction, nonexplosion, triviality, denial and rational acceptance; give arguments showing paraconsistency need not entail dialetheism.'),
 ([2],'Identify the precise inclosure premise/rule changed by hierarchical, typed and semantic replies; schema resemblance does not establish uniform solution.')])

goal(27,'def:p08-pointed-rm-frame;thm:p08-relevance-variable-sharing;thm:p08-gamma-admissibility','Constant-free relevant theoremhood;Pointed ternary/star frames and hereditary valuations;Theorem-rule versus open-assumption scope','D-P10-032',
 'Variable sharing defines relevance or holds for arbitrary premises/full RM; gamma is an axiom or unrestricted syllogism; unmatched source frame packages merge.',[
 ([1,4],'Give exact E/R systems and complete constant-free theorem-implication variable-sharing proof with its invariant.'),
 ([2],'Reconstruct Meyer–Dunn1969 E,R,gamma proof with gamma precisely a theoremhood metarule.'),
 ([3,4],'Give each source pointed frame/star/ternary/valuation clauses, match axioms to conditions and supply selected soundness/completeness proofs.'),
 ([4],'Distinguish E,R,RM and implicational/full-language profiles, with counterexample to unqualified RM variable sharing.'),
 ([5],'Present Mares2004 relevant-implication interpretation and informational/situational semantics, including formal R appendices and limits.'),
 ([1,2,3,4,5],'Compare matched derivations/countermodels through explicit translations; theoremhood adequacy does not become arbitrary-premise completeness.')])

goal(28,'def:p08-lukasiewicz-matrices;thm:p08-lukasiewicz-completeness;thm:p08-mcnaughton','Finite matrix/tableau consequence;Real arithmetic and continuous piecewise-linear functions;MV algebras, filters and Lindenbaum quotients','D-P10-020;N-d-013',
 'Finite/infinite logics merge; n convention changes; finite tableau decides continuum; finite standard completeness becomes arbitrary strong standard completeness.',[
 ([1],'Retain the entire1920 L3 source presentation, original motivation/notation and designation; it is not every later Ln proof.'),
 ([2],'Reconstruct selected finite/infinite many-valued results of Lukasiewicz–Tarski1930 with stated/proved/problem and translation distinctions.'),
 ([4],'Define each fixed n-value chain with exact n convention, designation and operations; give finite adequacy/decision and separating valuations.'),
 ([4],'Give infinite L calculus/real semantics and separate theoremhood, finite-standard and arbitrary-MV consequence; complete promised P10 treatment.'),
 ([3],'Reconstruct McNaughton1951 finite-variable continuous piecewise-linear integer-coefficient characterization and proof, distinct from approximation/strong completeness.'),
 ([3,4],'Work representable and nonrepresentable functions and bind the functional/MV bridge with its hypotheses.')])

goal(29,'def:p08-tnorm-residuum;thm:p08-tnorm-completeness','T-norm residuation/continuity;Propositional language and premise-cardinality regimes;Integral commutative residuated lattices, prelinearity/divisibility','D-P10-021;N-d-015;N-b-024;N-b-028',
 'BL/MTL share continuity class; Product becomes Godel; omitted proofs count as supplied; cardinality restrictions or corrections vanish.',[
 ([1,2,3],'Define t-norm/left-continuity/continuity, residuum and weak/strong conjunction; calculate three standard operations and differences.'),
 ([1,2,3],'Give exact BL,MTL,Godel/Product sheets, algebra signatures and prelinearity/divisibility/variant equations.'),
 ([1],'Retain Hajek1998 original metamathematics and then-open standard-BL status; subsequent completeness proofs have separate sources.'),
 ([2],'Reconstruct Esteva–Godo2001 MTL271–288 and separate its results from Jenei–Montagna later standard completeness.'),
 ([3],'Supply separately authored2011 selected extents in I,II,IV,V,VI,VII; chapterI omissions do not discharge independently required proof sources.'),
 ([1,2,3],'Give exact theorem/finite/arbitrary-premise standard-versus-algebra completeness with language-cardinality bounds and failure cases; complete P10 definitions/proofs.'),
 ([3],'Apply chapterI25October2022 corrections: continuity for Theorem1.1.5(3), Sn at52 and conjectural IMTL comprehension at92; date later status claims.')])

goal(30,'def:p08-bhk-reading;def:p08-choice-sequence-principles','Constructions versus derivations;Arithmetic and two-sorted sequence languages;Decidable bars, admissible predicates and total functionals','D-P10-015;D-P10-019',
 'Brouwer1908 has later BHK clauses; IPL proves analysis; all choice sequences are recursive; realizability validity becomes HA derivability.',[
 ([1],'Present Brouwer1908 critique and historically faithful weak counterexample, distinct from later Kripke models.'),
 ([2,3,4],'Give all six BHK clauses and source-specific comparison with forcing and number realizability.'),
 ([2,3,4],'Define lawlike/lawless/choice-sequence notions in each source theory/language with admitted construction principles.'),
 ([3,4],'Fix analysis base, decidable bar, bar condition, inductive predicate and complete bar-induction schema, distinguishing stronger bar/fan variants.'),
 ([3,4],'Fix continuity quantification/totality/modulus and theory-specific status and relation to the selected bar principle.'),
 ([3,4],'State Markov schema/predicate class/base, realizability evidence and derivability bounds, routing the actual P7 proof.')])

goal(31,'def:p08-intermediate-logic;def:p08-intermediate-lattice;thm:p08-kc-profile;thm:p08-lc-profile','IPC/CPC theoremhood, substitution and MP;Kripke/Heyting semantics','D-P10-018;N-d-009;A-081;A-144',
 'Local chain is full lattice; Godel1932 proves later LC result; maximal=greatest outside finite/rooted bounds; theoremhood becomes strong consequence.',[
 ([1],'Retain Godel1932 original finite-valued sequence/intuitionistic result separately from Dummett completeness.'),
 ([2],'Reconstruct Dummett1959 denumerable matrix/calculus completeness, LC prelinearity and exact linear-frame/FMP/decision consequences.'),
 ([3],'Reconstruct Jankov1968 weak excluded middle and semantic proof with finite rooted greatest-world bounds and Russian/English versions.'),
 ([4],'Define the full intermediate lattice, intersection meets, closure joins and empty-family bounds, with wider landscape and Heyting-variety relation.'),
 ([2,3,4],'Give IPC<KC<LC<CPC via derivations/counterframes and KC/LC disjunction-property failure, respecting IPC property.'),
 ([4],'Bind numerical Godel-chain/intermediate presentations via explicit translations and actual strong-consequence restrictions.')])

goal(32,'def:p08-preferential-model;thm:p08-klm-representation;thm:p08-rational-representation;def:p08-agm','Classical propositional closure;Preference, valuation copies and definable sets;Belief remainders/selection','D-P10-036;A-093',
 'Rational Monotony is in System P; ranking substitutes for smoothness; finite preorder replaces original AGM; Inclusion is conditional; one-step revision covers update/iteration.',[
 ([2],'Give original KLM cumulative/preferential states/copies, smoothness, all System-P principles and complete representation in both directions.'),
 ([3],'Give Lehmann–Magidor rational consequence/ranked representation/rational closure at exact knowledge-base scope, with proof and preference-without-RM example.'),
 ([1],'State all contraction/revision postulates and exact hypotheses; give original expansion, remainder selection and partial-meet operations.'),
 ([1],'Reconstruct original partial-meet representation and Levi/Harper proofs with basic/supplementary postulates distinguished.'),
 ([4],'Present Makinson2005 selected classical-to-nonmonotonic bridge constructions and hypotheses, preserving preferential/belief-change differences.'),
 ([1,2,3,4],'Work exception, nonmonotony and revision/contraction examples; compare finite faithful-preorder with original AGM through restricted explicit translation.')])

goal(33,'def:p08-default-theory;def:p08-circumscription','Classical closure/least fixed points;Predicate signatures and second-order arities;Minimization and credulous/skeptical consequence','D-P10-035;N-x-009',
 'Prerequisites self-support in candidate; fixed/varying swap; empty extension families vanish; later circumscription is attributed to1980.',[
 ([1],'Give Reiter1980 fact/default language and grounded extension operator, separating candidate justifications from prerequisite construction and preserving variable conventions.'),
 ([1],'Compute no/multiple/normal extensions and credulous/skeptical consequences including empty-family convention; bind source proofs.'),
 ([2],'Reconstruct McCarthy1980 original schema/signature/variation and minimal-model argument with abnormality examples.'),
 ([2],'Give current minimized/fixed/varying and parallel/prioritized interface with separate provenance for later generalizations.'),
 ([1,2],'Give source entries with inputs, output, assumptions, examples, limits and P9/P18 links; every translation has stated/proved restrictions.')])

goal(34,'def:p11-model-consequence;sec:p11-consequence','Signature interpretation/domain policy;Introduction/elimination rules and reductions;Semantic types, permutations/bijections','',
 'Definition settles adequacy; domain policy transfers between authors; invariance lacks types; harmony means merely having rules.',[
 ([1],'Reconstruct Tarski1936 consequence argument and constant distinction in original/translation with competing domain-policy readings explicit.'),
 ([2],'Present Prawitz1974 general proof theory, canonical validity and normalization role; do not substitute1965.'),
 ([3],'Present Etchemendy1990 interpretation/representation and under/overgeneration arguments with exact target/examples and attributed replies.'),
 ([4],'Give Sher1991 logicality, typed isomorphism/permutation invariance and quantifier cases with formal/philosophical limits.'),
 ([5],'Present Dummett1991 justification/harmony with reduction, expansion, stability/separability in actual roles and good/bad rule packages.'),
 ([1,2,3,4,5],'Compare semantic/proof accounts on one fixed language/example without making soundness/completeness settle normative/conceptual adequacy.')])

goal(35,'def:p11-plural-quantification;sec:p11-ontology','First-order binding/identity/regimentation;Monadic second-order full/Henkin semantics;Plural membership/comprehension and ontology','',
 'Plural variables are singular sets; monadic translation covers polyadic SOL without coding; empty/comprehension policies vanish; innocence is a formal theorem.',[
 ([2,3],'Specify singular/plural sorts, one-of, equality/extensionality, binding/substitution, empty/nonempty convention, quantifier rules and comprehension per Boolos source.'),
 ([2,3],'Give monadic second-order/plural translation with a non-first-order example and preservation proof; handle empty extensions or restrict domain explicitly.'),
 ([2,3,4],'Separate monadic plurality from polyadic relations/higher plurality; extensions need explicit tuple coding/extra sorts and hypotheses.'),
 ([1],'Reconstruct Quine1970 first-edition second-order and commitment arguments; the1948 criterion cannot substitute.'),
 ([2,3],'Present Boolos1984 and Nominalist Platonism1985 separately; philosophical innocence/commitment is distinct from translation.'),
 ([4],'Present Shapiro1991 defense with full/Henkin distinction and semantic/proof-limitation/mathematical-practice arguments.'),
 ([1,2,3,4],'Compare ranges, metatheory and commitment criteria on one example without deriving ontology from notation/completeness.')])
