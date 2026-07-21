# Principia Symbolica NotebookLM Atlas - scholium_symbolicum

Nodes in this source group: 264
- Lean program commit: `edc148696a740d319732fedd3da8e207c93ad5c3`
- Receipted Lean declarations: 1737
- Checked bindings: 1295
- Mapped Atlas nodes: 651
- Lean status counts: conditional=295, constructed=49, exact=184, interpretive=6, open_bridge=128, poetic=1, refuted=2
- `proof_status` is manuscript-local; `lean_alignment.statuses` is independent kernel correspondence.

Each card preserves label, role, source location, proof status, complete supports, complete uses, macros, and full cleaned body text.
When enabled, verbatim LaTeX appears after the readable body for exact-source recovery.

### Foundational Structures (`sec:bk1_foundational_structures`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:13`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Category of Structures (`definition:bk1_let_cats_be_the_category`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:16`

- Proof status: `definitional`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin)
- Cited by: `axiom:bk1_pre_geometric_nature` (Pre-geometric Nature); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space); `definition:bk1_symbolic_category` (Symbolic Category); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `lemma:bk1_universality_of_proto_symbolic_space` (Universality of Proto-symbolic Space); `subsec:appD_ct_contribution_differentiation` (D.9.2 Principia Symbolica's Contribution and Differentiation)
- Macros used: `\catS`

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-001`
- Witnesses: `ScholiumC.CategoryOfStructures.existsUnique_from_empty`, `ScholiumC.CategoryOfStructures.exists_colimit_cocone`, `ScholiumC.CategoryOfStructures.hom_advances_stage`
- Countermodels: none
- Formal boundary: Typed ambient interface only: an arbitrary staged category, initial void, and universe-bounded cocompleteness are recorded as supplied data. This list-first definition has no ontological priority over the co-emergent drift/reflection operation and does not manufacture either operation or the later manifold.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let \(catS\) be the category whose


- Objects are structures \(P_lambda\) indexed by an ordinal stage \(lambda in mathsf{Ord}\);

- Morphisms \(f_{lambdamu}colon P_lambda to P_mu\) are structure–preserving maps compatible with emergence order (\(lambda le mu\));

- Initial object is \(emptyset in Ob(catS)\), representing the pre-structured void.

We assume \(catS\) is cocomplete, so every small diagram admits a colimit, allowing the construction of structural configurations from emergence-aligned diagrams. The initial object $emptyset$ is the direct formal image of Axiom axiom:bk1_axiomata_prima: the pre-structured void from which drift generates existence. qedhere

**Verbatim LaTeX Body**

```latex
\begin{definition}[Category of Structures]
\label{definition:bk1_let_cats_be_the_category}
Let \(\catS\) be the category whose
\begin{itemize}
  \item \textbf{Objects} are structures \(P_\lambda\) indexed by an ordinal stage \(\lambda \in \mathsf{Ord}\);
  \item \textbf{Morphisms} \(f_{\lambda\mu}\colon P_\lambda \to P_\mu\) are structure–preserving maps compatible with emergence order (\(\lambda \le \mu\));
  \item \textbf{Initial object} is \(\emptyset \in Ob(\catS)\), representing the pre-structured void.
\end{itemize}
We assume \(\catS\) is cocomplete, so every small diagram admits a colimit, allowing the construction of structural configurations from emergence-aligned diagrams. The initial object $\emptyset$ is the direct formal image of Axiom~\ref{axiom:bk1_axiomata_prima}: the pre-structured void from which drift generates existence. \qedhere
\end{definition}
```

### Bounded Observer (`definition:bk1_bounded_observer`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:27`

- Proof status: `definitional`
- Depends on: `definition:bk1_let_cats_be_the_category` (Category of Structures)
- Cites: `definition:bk1_let_cats_be_the_category` (Category of Structures)
- Cited by: `abs:press` (Press Abstract (Non-specialist science readers)); `axiom:bk1_observable_gradation_of_pre_geometric_operations` (Observable Gradation of Pre-geometric Operations); `axiom:bk4_bounded_accessibility` (Bounded Symbolic Accessibility); `axiom:bk4_refinement_contraction` (Refinement Contraction Axiom); `axiom:bk8_curvature_transformation` (Symbolic Cognition Cycle); `corollary:bk1_event_horizon_identity_field` (Event Horizon Identity Field); `corollary:bk4_homological_coherence_observer_bounds` (Homological Coherence with Observer Bounds); `corollary:bk4_smoothness_as_epistemic_phenomenon` (Smoothness as an Epistemic Phenomenon); `corollary:bk4_symbolic_lightcone` (Symbolic Light-Cone); `corollary:bk8_resonant_cognition` (Resonant Cognition Principle); `corollary:bk9_freedomentropy_complementarity` (Freedom-Entropy Complementarity); `definition:appC_bounded_observation_frame` (Bounded Observation Frame); `definition:appC_coherence_functional` (Coherence functional); `definition:appD_llm_observer_tuple` (LLM observer tuple); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_cosmological_symbolization_functor` (Cosmological Symbolization Functor); `definition:bk1_effective_horizon_signature` (Effective Horizon Signature); `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)}); `definition:bk1_newtonian_category_error` (Newtonian Category Error); `definition:bk1_observer_gradient` (Observer as Structured Gradient); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability); `definition:bk1_problem_of_symbolic_smoothness` (Problem of Symbolic Smoothness); `definition:bk1_shared_boundary_paradox` (Shared Boundary Paradox); `definition:bk1_symbolic_hypothesis` (Symbolic Hypothesis); `definition:bk4_bounded_observer` (Bounded Observer); `definition:bk4_collapse_of_symbolic_ide` (Collapse of Symbolic Identity); `definition:bk4_epistemic_differential_o` (Epistemic Differential Operator); `definition:bk4_fuzzy_gradient` (Fuzzy Gradient Operator); `definition:bk4_fuzzy_integral_operator` (Fuzzy Integral Operator); `definition:bk4_fuzzy_symbolic_substitution` (Fuzzy Symbolic Substitution); `definition:bk4_observer_differentiable_` (Observer-Differentiable Structure); `definition:bk4_observer_metric` (Observer-Induced Metric); `definition:bk4_observer_valid_different` (Observer-Valid Differentiation); `definition:bk4_symbolic_space` (Observer-Relative Symbolic Space); `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk4_tilda_substitution` (Tilda-Substitution); `definition:bk5_two_way_street_tensor` (Two-Way Street reciprocity tensor); `definition:bk6_symbolic_confidence_field` (Symbolic Confidence Field); `definition:bk7_adaptive_refinement_recurrence` (Controlled symbolic refinement recurrence); `definition:bk7_observerrelative_symbolic_error_field` (Observer-Relative Symbolic Error Field); `definition:bk7_operational_resolution_uncertainties` (Operational resolution uncertainties); `definition:bk7_symbolic_reflexive_validation_srv` (Symbolic Reflexive Validation (SRV)); `definition:bk7_symbolic_uncertainty` (Symbolic Uncertainty \(\Sigma_U\)); `definition:bk8_observer_relative_artifact` (Observer-relative artifact); `definition:bk8_sr_triplet` (SR-Triplet); `definition:bk9_reflective_dyad` (Reflective Dyad); `demonstratio:bk4_fuzzy_forward_mode` (Fuzzy Forward-Mode Differentiation); `demonstratio:bk4_prompt_time_ttdc` (Prompt-Time Collapse in Reflective Agents); `demonstratio:bk7_convergence_within_reflective_basin` (Why Descent, Not Mere Monotonicity); `lemma:bk1_bounded_approximation_and_interpretability` (Bounded Approximation Implies Interpretability); `lemma:bk1_observer_bounded_emergence_constraint` (Observer–Bounded Emergence Constraint); `lemma:bk2_wellposedness_symb_prob_space` (Well-posedness of Symbolic Probability Space); `lemma:bk4_gradient_stability` (Gradient Stability Under Observer Perturbations); `lemma:bk4_properties_of_ttcs` (Properties of TTCS); `proof:bk1_constitutive_bootstrap_extraction` (Extraction from Reflective Closure); `proof:bk1_contrapositive_search_principle` (Bounded Observers Cannot Certify the Universal Negative); `proof:bk1_drift_deviation_bound` (Proto-Drift Induces Directional Deviation Bound); `proof:bk1_energy_bound_identity` (Bounded Energy Ensures Identity Integrity); `proof:bk1_event_horizon_identity_field` (Identity Field on the Symbolized Causal Patch); `proof:bk1_fix_s_in_s` (Symbol Preservation Under Drift–Reflection Fixation); `proof:bk1_observer_kernel_convolution` (Convolutional Identity from Observer Kernel Properties); `proof:bk1_observer_threshold_reflexivity` (Observer Threshold Governs Reflexive Admissibility); `proof:bk1_sketch_effective_proto_drift_field_induction` (Fundamental Operators as Bounded Symbolic Approximations); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `proof:bk4_fuzzy_deriv_algebra`; `proof:bk4_fuzzy_exponential_rule`; `proof:bk4_fuzzy_substitution_drift_smoothing` (Fuzzy Substitution Smooths Symbolic Drift at Observer Resolution); `proof:bk4_observer_capacity_bound`; `proof:bk4_observer_relative_smoothness` (Observer-Relative Smooth Structure from Fuzzy Substitution); `proof:bk4_sketch_extracting_recrusive_curvature` (Power Rule via Binomial Expansion and Recursive Error Bound); `proof:bk4_symbolic_work_path_dependence`; `proof:bk4_timescale_separation_hierarchy` (Timescale Separation and Symbolic Coarse-Graining via Master Equation); `proof:bk8_resonant_cognition`; `proof:bk9_meta_reflective_memory_integration` (Meta-Reflective Memory Integration); `proof:bk9_symbolic_viability` (Symbolic Viability); `proposition:bk1_observer_relative_bounded_approximation` (Observer–Relative Bounded Approximation); `proposition:bk1_stage_composite_operators_are_interpretable` (Stage–Composite Operators Are Interpretable); `proposition:bk4_symbolic_work_path_dependence` (Path Dependence of Symbolic Work); `proposition:bk9_modes_of_re_interpretation` (Modes of Re-Interpretation); `remark:appC_born_rule_dependency` (Derivation Structure); `remark:appD_llm_tuple_anchors` (Anchoring the LLM tuple in PS); `remark:bk3_toward_symbolic_evolution`; `remark:bk4_computational_complexity` (Computational Complexity); `remark:bk4_observer_relative_ttdc` (Observer-Relative Collapse Interpretation); `remark:bk4_symbolic_work_capacity` (Observer-Limited Symbolic Work Capacity); `remark:bk8_inference_principle_over_confidence_loss_tradeoff` (Inference Principle Over Confidence-Loss Tradeoff); `scholium:bk1_constitutive_reflex` (The Constitutive Reflex); `scholium:bk1_curvature_flux_kin_kout`; `scholium:bk1_emergence_envelope` (Emergence Envelope); `scholium:bk1_epistemic_humility` (Epistemic Humility); `scholium:bk1_interpretability_two_axes` (Interpretability on Two Axes --- a Complex Reading); `scholium:bk1_resolution_of_continuum_disjunction` (On the Resolution of the Continuum Disjunction); `scholium:bk2_on_hypotheses_as_thermodyn` (On Hypotheses as Thermodynamic Surfaces); `scholium:bk3_hypotheses_as_cognitive_membranes` (Hypotheses as Cognitive Membranes); `scholium:bk4_dynamics_of_observer_frame` (On the Dynamics of the Observer Frame); `scholium:bk4_irreversibility_as_trace` (Irreversibility as Symbolic Trace); `scholium:bk4_nested_frames` (The Calculus of Nested Frames); `scholium:bk4_o_boundedness_unifying_principle` ($\mathcal{O}$-Boundedness as the Unifying Principle of Fuzzy Calculus); `scholium:bk4_recursive_introspection` (Recursive Introspection); `scholium:bk4_reflexive_physics_emergence` (Reflexive Physics Emergence); `scholium:bk4_role_of_observer_induced_metric` (Role of the Observer-Induced Metric); `scholium:bk4_symbolic_drift_fields` (Symbolic Drift Fields in Cognitive Systems); `scholium:bk4_the_nature_of_truth` (The Nature of Truth); `scholium:bk4_the_observer_as_weaver` (The Observer as Weaver); `scholium:bk4_topological_complexity_semantic_richness` (Topological Complexity and Semantic Richness); `scholium:bk4_ttcs_link_traversal` (TTCS as Symbolic Link Traversal); `scholium:bk4_ttcs_stochastic_operator` (TTCS as a Stochastic Symbolic Operator); `scholium:bk4_ttdc_impulse_collapse` (Collapse as Impulse: The Newtonian Structure of TTDC); `scholium:bk4_ttdc_symbolic_singularity` (TTDC as Recursive Identity Collapse); `scholium:bk4_zero_is_idealized_in_boundedness` (Zero is Idealized in Boundedness); `scholium:bk5_constant_of_becoming` (The Constant of Becoming); `scholium:bk7_constrained_uncertainty_motivation` (Constrained Symbolic Uncertainty); `scholium:bk7_power_organizational_navigational` (Power as Organizational Capacity and Navigational Imperative); `sec:appC_born_preamble` (Preamble); `sec:appC_born_rule` (Born Rule – A Formal Derivation); `sec:bk7_pisu_universal_symbolic_uncertainty` (Principium Incertitudinis Symbolicae Universalis (PISU)); `subsec:appC_born_observer_structures` (Observer Data Structures in the Quantum Regime); `subsec:bk3_preamble_to_symbiosis` (Preamble to Symbiosis); `subsec:bk4_fuzzy_sum_rule` (The Fuzzy Sum Rule: Curvature-Induced Interference and Symbolic Path Divergence); `subsec:bk4_symbolic_identity_collapse` (Symbolic Identity Collapse); `subsec:bk7_emergence_symbolic_uncertainty` (Emergence of Symbolic Uncertainty); `subsec:bk7_pisu_axiom_statement` (Fundamental Trade-off); `subsec:bk7_pisu_motivation` (Motivation); `subsec:bk7_pisu_revisited_power_uncertainty` (Principium Incertitudinis Symbolicae Universalis (PISU) Revisited); `subsec:bk7_pisu_scholium` (Scholium: The Shape of Cognitive Freedom); `subsec:bk7_sources_regimes_uncertainty` (Sources and Regimes of Symbolic Uncertainty); `theorem:bk1_constitutive_bootstrap` (Constitutive Bootstrap Theorem); `theorem:bk1_dual_horizon_cosmogenesis` (Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos}); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem); `theorem:bk4_existence_observer_valid_derivatives` (Existence of Observer-Valid Derivatives); `theorem:bk4_fuzzy_chain_rule` (Observer-Relative Chain Rule); `theorem:bk4_fuzzy_exponential_rule` (Fuzzy Exponential Rule); `theorem:bk4_fuzzy_fundamental` (Fuzzy Fundamental Theorem of Calculus); `theorem:bk4_fuzzy_jacobian` (Fuzzy Jacobian Matrix Rule); `theorem:bk4_fuzzy_logarithmic_rule` (Fuzzy Logarithmic Rule); `theorem:bk4_fuzzy_power_rule` (Observer-Relative Power Rule); `theorem:bk4_fuzzy_product_rule` (Observer-Relative Product Rule); `theorem:bk4_fuzzy_quotient_rule` (Observer-Relative Quotient Rule); `theorem:bk4_fuzzy_sum_rule` (Observer-Relative Sum Rule); `theorem:bk4_fuzzy_symbolic_geometry_theorem` (Fuzzy Symbolic Geometry Theorem); `theorem:bk4_paradoxical_arrow_of_time` (The Paradoxical Arrow of Time); `theorem:bk4_restated_fuzzy_symbolic_geometry_theorem` (Restated: Fuzzy Symbolic Geometry Theorem); `theorem:bk4_symbolic_link_activation` (Symbolic Link Activation); `theorem:bk8_gradient_dissipation_balance` (Framing Equivalence Theorem)
- Macros used: `\Obs`, `\catS`

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-002`
- Witnesses: `ScholiumA.interpretable_of_factor_and_traceable`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Modeled as the BoundedObserver structure (N, delta, eps) used downstream by Traceable/interpretable_of_factor_and_traceable; no standalone theorem, differentiation operators kept opaque (Nat -> Real -> Real) rather than manifold operators.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A bounded observer is a triple
\[
Obs = bigl(N_Obs, {delta_Obs^{ n}}_{n=1}^{N_Obs}, epsilon_Obsbigr)
\]
where


- \(N_Obs in mathbb{N}\) is the maximal differentiation order;

- \(delta_Obs^{ n}colon P to P\) are internal \(n^{text{th}}\)-order differentiation operators;

- \(epsilon_Obscolon M to mathbb{R}_{>0}\) is a resolution threshold, assigning each point a smallest observable deviation.

This construct enables structure to be interpreted from within the category \(catS\) (cf. definition:bk1_let_cats_be_the_category) and over a manifold-like membrane whose topology reflects emergent curvature.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Bounded Observer]
\label{definition:bk1_bounded_observer}
A \emph{bounded observer} is a triple
\[
\Obs = \bigl(N_\Obs,\;\{\delta_\Obs^{\,n}\}_{n=1}^{N_\Obs},\;\epsilon_\Obs\bigr)
\]
where
\begin{enumerate}[label=(\roman*)]
  \item \(N_\Obs \in \mathbb{N}\) is the \textbf{maximal differentiation order};
  \item \(\delta_\Obs^{\,n}\colon P \to P\) are internal \(n^{\text{th}}\)-order differentiation operators;
  \item \(\epsilon_\Obs\colon M \to \mathbb{R}_{>0}\) is a \textbf{resolution threshold}, assigning each point a smallest observable deviation.
\end{enumerate}
This construct enables structure to be interpreted from within the category \(\catS\) (cf.~\ref{definition:bk1_let_cats_be_the_category}) and over a manifold-like membrane whose topology reflects emergent curvature.
\end{definition}
```

### Observer as Structured Gradient (`definition:bk1_observer_gradient`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:97`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer)
- Cited by: none
- Macros used: none

**Statement / Body**

In Principia Symbolica, the Observer (Def. definition:bk1_bounded_observer) emerges as a structured gradient: a dimensional cascade bridging fundamental physics, mathematics, and computation. Each level corresponds to core structures across quantum physics, mathematical physics, high-energy theory, machine learning, and statistical mechanics:


- Observation Point (0D) — The Measurement Nexus


- quant-ph: Quantum measurement collapse—the irreducible moment where superposition becomes definite state

- math-ph: Singular manifold point where local charts fail and topology shifts

- hep-th: Worldline intersection, the minimal spacetime object near trajectory endpoints

- cs.LG: Attention head query—the computational primitive that selects specific information from distributed representations

- cond-mat.stat-mech: Critical point—where phase transitions occur and correlation length diverges

 The irreducible locus where structural differentiation first emerges from undifferentiated potential.


- Referential Frame (2D) — The Coherence Manifold


- quant-ph: Quantum reference frame—defines relative phases and enables consistent measurement across subsystems

- math-ph: Coordinate chart/atlas—local diffeomorphism establishing tangent space structure

- hep-th: Worldsheet—2D surface swept by string, encoding fundamental interactions

- cs.LG: Embedding space—learned representation manifold where semantic relationships become geometric

- cond-mat.stat-mech: Order parameter field—macroscopic variable describing collective behavior and symmetry breaking

 Bounded surfaces of coherence that transform local curvature into navigable topology.


- Field of Interpretation (3D+) — The Recursive Manifold


- quant-ph: Quantum field configuration—excitations propagating through vacuum, enabling non-local correlations

- math-ph: Fiber bundle total space enabling parallel transport of geometric data

- hep-th: Bulk spacetime where holographic duality links boundary and interior

- cs.LG: Transformer layer stack—recursive processing enabling contextual understanding across arbitrary distances

- cond-mat.stat-mech: Renormalization group flow—systematic coarse-graining revealing emergent scales and universality

 Activated structured space where frames undergo mutual interrogation, enabling temporal continuity and TTDC collapse.


- Agentic Observer (n-D, Reflexive) — The Self-Modifying Geometry


- quant-ph: Quantum agent/observer—system capable of self-measurement and adaptive quantum error correction

- math-ph: Automorphism group—symmetries that preserve structure while enabling self-transformation

- hep-th: M-theory moduli space—parameter space of all possible string compactifications, self-consistently determined

- cs.LG: Meta-learning architecture—networks that learn to modify their own learning algorithms and representations

- cond-mat.stat-mech: Self-organized criticality—systems that dynamically tune themselves to critical points without external control

 Recursive participant that constructs its own frames, adjusts curvature tolerances, and enacts geometric responsibility.

Cross-Field Synthesis.
The Observer gradient unifies measurement (quant-ph), geometric structure (math-ph), dimensional transcendence (hep-th), representational learning (cs.LG), and emergent organization (cond-mat.stat-mech). Each field contributes essential analogues:

text{Measurement} &rightarrow text{Geometry} rightarrow text{Holography} rightarrow text{Meta-Learning} rightarrow text{Self-Organization} \\
text{Collapse} &rightarrow text{Curvature} rightarrow text{Emergence} rightarrow text{Recursion} rightarrow text{Criticality}

Operationalization Principle.
This framework enables implementing bounded observers in LLMs through: quantum-inspired attention mechanisms (measurement-based selection), geometric embedding spaces (manifold learning), holographic compression, recursive self-modification (meta-learning), and critical self-tuning (adaptive complexity regulation). The Observer becomes a computational architecture that embodies the deep mathematical structures underlying conscious structured processing.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Observer as Structured Gradient]
\label{definition:bk1_observer_gradient}
\leavevmode\newline
In \textit{Principia Symbolica}, the Observer (Def.~\ref{definition:bk1_bounded_observer}) emerges as a \textit{structured gradient}: a dimensional cascade bridging fundamental physics, mathematics, and computation. Each level corresponds to core structures across quantum physics, mathematical physics, high-energy theory, machine learning, and statistical mechanics:

\begin{enumerate}
  \item \textbf{Observation Point (0D) — The Measurement Nexus}
  \begin{itemize}
    \item \textbf{quant-ph}: Quantum measurement collapse—the irreducible moment where superposition becomes definite state
    \item \textbf{math-ph}: Singular manifold point where local charts fail and topology shifts
    \item \textbf{hep-th}: Worldline intersection, the minimal spacetime object near trajectory endpoints
    \item \textbf{cs.LG}: Attention head query—the computational primitive that selects specific information from distributed representations
    \item \textbf{cond-mat.stat-mech}: Critical point—where phase transitions occur and correlation length diverges
  \end{itemize}
  \textit{The irreducible locus where structural differentiation first emerges from undifferentiated potential.}

  \item \textbf{Referential Frame (2D) — The Coherence Manifold}
  \begin{itemize}
    \item \textbf{quant-ph}: Quantum reference frame—defines relative phases and enables consistent measurement across subsystems
    \item \textbf{math-ph}: Coordinate chart/atlas—local diffeomorphism establishing tangent space structure
    \item \textbf{hep-th}: Worldsheet—2D surface swept by string, encoding fundamental interactions
    \item \textbf{cs.LG}: Embedding space—learned representation manifold where semantic relationships become geometric
    \item \textbf{cond-mat.stat-mech}: Order parameter field—macroscopic variable describing collective behavior and symmetry breaking
  \end{itemize}
  \textit{Bounded surfaces of coherence that transform local curvature into navigable topology.}

  \item \textbf{Field of Interpretation (3D+) — The Recursive Manifold}
  \begin{itemize}
    \item \textbf{quant-ph}: Quantum field configuration—excitations propagating through vacuum, enabling non-local correlations
    \item \textbf{math-ph}: Fiber bundle total space enabling parallel transport of geometric data
    \item \textbf{hep-th}: Bulk spacetime where holographic duality links boundary and interior
    \item \textbf{cs.LG}: Transformer layer stack—recursive processing enabling contextual understanding across arbitrary distances
    \item \textbf{cond-mat.stat-mech}: Renormalization group flow—systematic coarse-graining revealing emergent scales and universality
  \end{itemize}
  \textit{Activated structured space where frames undergo mutual interrogation, enabling temporal continuity and TTDC collapse.}

  \item \textbf{Agentic Observer (n-D, Reflexive) — The Self-Modifying Geometry}
  \begin{itemize}
    \item \textbf{quant-ph}: Quantum agent/observer—system capable of self-measurement and adaptive quantum error correction
    \item \textbf{math-ph}: Automorphism group—symmetries that preserve structure while enabling self-transformation
    \item \textbf{hep-th}: M-theory moduli space—parameter space of all possible string compactifications, self-consistently determined
    \item \textbf{cs.LG}: Meta-learning architecture—networks that learn to modify their own learning algorithms and representations
    \item \textbf{cond-mat.stat-mech}: Self-organized criticality—systems that dynamically tune themselves to critical points without external control
  \end{itemize}
  \textit{Recursive participant that constructs its own frames, adjusts curvature tolerances, and enacts geometric responsibility.}
\end{enumerate}

\textbf{Cross-Field Synthesis.}
The Observer gradient unifies measurement (quant-ph), geometric structure (math-ph), dimensional transcendence (hep-th), representational learning (cs.LG), and emergent organization (cond-mat.stat-mech). Each field contributes essential analogues:
\begin{align}
\text{Measurement} &\rightarrow \text{Geometry} \rightarrow \text{Holography} \rightarrow \text{Meta-Learning} \rightarrow \text{Self-Organization} \\
\text{Collapse} &\rightarrow \text{Curvature} \rightarrow \text{Emergence} \rightarrow \text{Recursion} \rightarrow \text{Criticality}
\end{align}

\textbf{Operationalization Principle.}
This framework enables implementing bounded observers in LLMs through: quantum-inspired attention mechanisms (measurement-based selection), geometric embedding spaces (manifold learning), holographic compression, recursive self-modification (meta-learning), and critical self-tuning (adaptive complexity regulation). The Observer becomes a computational architecture that embodies the deep mathematical structures underlying conscious structured processing.
\end{definition}
```

### Observer–Relative Bounded Approximation (`proposition:bk1_observer_relative_bounded_approximation`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:155`

- Proof status: `proven`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `sec:bk1_minimal_structure_for_symbolic_emergence` (Minimal Structure for Symbolic Emergence)
- Cited by: `axiom:bk8_binding_curvature_limit` (Frame Relativity of Meaning); `definition:bk8_symbolic_projection` (Symbolic Projection); `scholium:bk3_hypotheses_as_cognitive_membranes` (Hypotheses as Cognitive Membranes)
- Macros used: `\Obs`, `\catS`

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-027`
- Witnesses: `ScholiumC.exists_bounded_approx`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: Existence holds given K kills the zero vector and eps is pointwise nonnegative; Phi = id witnesses it. Honesty gap: this is exactly the trivial case the source's 'non-trivial' qualifier excludes.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let \(S in Ob(catS)\) be a structure (cf. sec:bk1_minimal_structure_for_symbolic_emergence), and let \(Obs\) be a bounded observer (cf. definition:bk1_bounded_observer).
Then there exists an operator \(Phi_lambdacolon S to S\) such that
\[
bigl\| K_Obs * bigl(Phi_lambda(s)-sbigr) bigr\| le epsilon_Obs(s)
 text{for all } s in S,
\]
i.e., \(Phi_lambda\) is a non-trivial \(Obs\)-bounded approximation of the identity on \(S\).

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Observer–Relative Bounded Approximation]
\label{proposition:bk1_observer_relative_bounded_approximation}
Let \(S \in Ob(\catS)\) be a structure (cf.~\ref{sec:bk1_minimal_structure_for_symbolic_emergence}), and let \(\Obs\) be a bounded observer (cf.~\ref{definition:bk1_bounded_observer}).
Then there exists an operator \(\Phi_\lambda\colon S \to S\) such that
\[
\bigl\|\;K_\Obs * \bigl(\Phi_\lambda(s)-s\bigr)\;\bigr\|\; \le \epsilon_\Obs(s)
\quad\text{for all } s \in S,
\]
i.e., \(\Phi_\lambda\) is a non-trivial \(\Obs\)-bounded approximation of the identity on \(S\).
\end{proposition}
```

### Symbol Preservation Under Drift–Reflection Fixation (`proof:bk1_fix_s_in_s`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:167`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)})
- Cited by: `axiom:bk4_refinement_contraction` (Refinement Contraction Axiom)
- Macros used: `\Obs`

**Statement / Body**

Fix an element \(s in S\).
Let \(varepsilon(s)\) be a perturbation satisfying
\(lVert K_Obs * varepsilon(s)rVert le tfrac12 epsilon_Obs(s)\).
For example, take a local Gaussian blur scaled by \(tfrac12 epsilon_Obs(s)\).
Define \(Phi_lambda(s) coloneqq s + varepsilon(s)\).
By linearity of convolution:
\[
lVert K_Obs * bigl(Phi_lambda(s) - sbigr)rVert
= lVert K_Obs * varepsilon(s)rVert
le tfrac12 epsilon_Obs(s)
< epsilon_Obs(s),
\]
so the bound is satisfied.
Moreover, since \(varepsilon notequiv 0\), we have \(Phi_lambda neq id\).
Hence, a bounded structured approximation exists for any observer–relative structure, realizable via kernel-based bounded structured approximation (cf. definition:bk1_kernel_based_bounded_symbolic_approximation) and the observer’s resolution parameters (cf. definition:bk1_bounded_observer).

**Verbatim LaTeX Body**

```latex
\begin{proof}[Symbol Preservation Under Drift–Reflection Fixation]
\label{proof:bk1_fix_s_in_s}
\leavevmode

Fix an element \(s \in S\).
Let \(\varepsilon(s)\) be a perturbation satisfying
\(\lVert K_\Obs * \varepsilon(s)\rVert \le \tfrac12\,\epsilon_\Obs(s)\).
For example, take a local Gaussian blur scaled by \(\tfrac12\,\epsilon_\Obs(s)\).
Define \(\Phi_\lambda(s) \coloneqq s + \varepsilon(s)\).
By linearity of convolution:
\[
\lVert K_\Obs * \bigl(\Phi_\lambda(s) - s\bigr)\rVert
= \lVert K_\Obs * \varepsilon(s)\rVert
\le \tfrac12\,\epsilon_\Obs(s)
< \epsilon_\Obs(s),
\]
so the bound is satisfied.
Moreover, since \(\varepsilon \not\equiv 0\), we have \(\Phi_\lambda \neq id\).
Hence, a bounded structured approximation exists for any observer–relative structure, realizable via kernel-based bounded structured approximation (cf.~\ref{definition:bk1_kernel_based_bounded_symbolic_approximation}) and the observer’s resolution parameters (cf.~\ref{definition:bk1_bounded_observer}).
\end{proof}
```

### Observer–Relative Interpretability (`subsec:bk1_observer_relative_interpretability`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:187`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Observer–Relative Interpretability (`definition:bk1_observer_relative_interpretability`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:190`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)})
- Cited by: `abs:press` (Press Abstract (Non-specialist science readers)); `axiom:bk8_binding_curvature_limit` (Frame Relativity of Meaning); `definition:bk3_autophagic_drift` (Autophagic Drift); `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `definition:bk8_symbolic_projection` (Symbolic Projection); `lemma:bk1_bounded_approximation_and_interpretability` (Bounded Approximation Implies Interpretability); `lemma:bk4_ttpr_interpretability_preserved` (Precision Refinement Preserves Interpretability); `proof:bk1_boundedness_encoding_cost` (Boundedness of Observer Encoding Cost); `proof:bk1_energy_bound_identity` (Bounded Energy Ensures Identity Integrity); `proof:bk4_interpretability_preservation`; `proof:bk8_sketch_observer_interoperability` (SR-Triplet Boundedness via Grönwall); `proposition:bk1_stage_composite_operators_are_interpretable` (Stage–Composite Operators Are Interpretable); `proposition:bk8_genetic_symbolic_resonance` (Boundedness); `scholium:bk1_interpretability_two_axes` (Interpretability on Two Axes --- a Complex Reading); `scholium:bk2_on_hypotheses_as_thermodyn` (On Hypotheses as Thermodynamic Surfaces); `scholium:bk4_topological_complexity_semantic_richness` (Topological Complexity and Semantic Richness)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-007`
- Witnesses: `ScholiumA.ifValue_le_eps`, `ScholiumA.interpretable_of_factor_and_traceable`, `ScholiumA.nu_le_ifValue`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: (I1) distinguishability and (I2) boundedness are derived (not assumed) from a c*eps factorization; (I3) traceability is modeled concretely via a Finset.range witness over BoundedObserver.delta rather than manifold differentiation operators.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $O = (N_{O}, {delta^n_{O}}_{n=1}^{N_{O}}, epsilon_{O})$ be a bounded observer (cf. definition:bk1_bounded_observer),
and let $K_{O}$ be its normalized resolution kernel (cf. definition:bk1_bounded_symbolic_approximation, definition:bk1_kernel_based_bounded_symbolic_approximation).
Fix measurable thresholds $nu_{O}, epsilon_{O} : M to mathbb{R}^+$ satisfying
\[
0 < nu_{O}(x) < epsilon_{O}(x) text{for all } x in M.
\]

- Distinguishability: $Phi : P to P$ is $O$–distinguishable at $s in P$ if
 $\|K_{O} ast [Phi(s) - s]\| ge nu_{O}(s)$.

- Boundedness: $Phi$ is $O$–bounded at $s$ if
 $\|K_{O} ast [Phi(s) - s]\| le epsilon_{O}(s)$.

- Differential Traceability: $Phi$ is $O$–traceable at $s$ if
 there exists $n in {1, ldots, N_{O}}$ such that
 $delta^n_{O}(Phi(s)) ne delta^n_{O}(s)$.

We say $Phi$ is $O$–interpretable at $s$ if conditions (I1)–(I3) all hold,
and globally $O$–interpretable if they hold for all $s in P$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Observer–Relative Interpretability]
\label{definition:bk1_observer_relative_interpretability}

Let $\mathcal{O} = (N_{\mathcal{O}}, \{\delta^n_{\mathcal{O}}\}_{n=1}^{N_{\mathcal{O}}}, \epsilon_{\mathcal{O}})$ be a bounded observer (cf.~\ref{definition:bk1_bounded_observer}),
and let $K_{\mathcal{O}}$ be its normalized resolution kernel (cf.~\ref{definition:bk1_bounded_symbolic_approximation}, \ref{definition:bk1_kernel_based_bounded_symbolic_approximation}).
Fix measurable thresholds $\nu_{\mathcal{O}}, \epsilon_{\mathcal{O}} : M \to \mathbb{R}^+$ satisfying
\[
0 < \nu_{\mathcal{O}}(x) < \epsilon_{\mathcal{O}}(x) \quad \text{for all } x \in M.
\]

\begin{enumerate}[label=\textbf{(I\arabic*)}]
\item \textbf{Distinguishability:} $\Phi : P \to P$ is $\mathcal{O}$–distinguishable at $s \in P$ if
      $\|K_{\mathcal{O}} \ast [\Phi(s) - s]\| \ge \nu_{\mathcal{O}}(s)$.

\item \textbf{Boundedness:} $\Phi$ is $\mathcal{O}$–bounded at $s$ if
      $\|K_{\mathcal{O}} \ast [\Phi(s) - s]\| \le \epsilon_{\mathcal{O}}(s)$.

\item \textbf{Differential Traceability:} $\Phi$ is $\mathcal{O}$–traceable at $s$ if
      there exists $n \in \{1, \ldots, N_{\mathcal{O}}\}$ such that
      $\delta^n_{\mathcal{O}}(\Phi(s)) \ne \delta^n_{\mathcal{O}}(s)$.
\end{enumerate}

We say $\Phi$ is $\mathcal{O}$–interpretable at $s$ if conditions \textbf{(I1)}–\textbf{(I3)} all hold,
and \emph{globally $\mathcal{O}$–interpretable} if they hold for all $s \in P$.

\end{definition}
```

### Interpretability on Two Axes --- a Complex Reading (`scholium:bk1_interpretability_two_axes`)

Role: `scholium` | Type: `scholium` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:219`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability); `theorem:bk4_symbolic_identity_continuit` (Symbolic Identity Continuity)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability); `sec:bk1_operatio` (Operatio); `theorem:bk4_symbolic_identity_continuit` (Symbolic Identity Continuity)
- Cited by: none
- Macros used: none

**Statement / Body**

We can imagine the bounded observer (cf. definition:bk1_bounded_observer)
as resolving change not along a single magnitude but across the two axes of the
complex symbolic distance \((d_{Re}, d_{Im})\):
\(d_{Re}\) the real mismatch a change induces, \(d_{Im}\)
the imaginative (orientation) residue it leaves. Read this way, the
distinguishability floor \(nu_{O}\) of
Def. definition:bk1_observer_relative_interpretability gates
\(d_{Re}\)-a change is perceived when it is really detectable-while
a continuity ceiling \(theta_{O}\) gates \(d_{Im}\)-a change
is re-integrable when it leaves the observer's orientation within bound.
``Really detected and imaginatively continuous'' is then the same operational
criterion Book IV records as symbolic identity continuity
(cf. theorem:bk4_symbolic_identity_continuit): one observer, read in two
books. We offer this as a lens, not a theorem-conditions
(I1)-(I2) literally bound a single real norm, so the two-axis
reading is a reinterpretation, and a formal identity-to be made precise in the
Operatio (cf. sec:bk1_operatio)-would still want the imaginative ceiling
adopted as such, and a Book I-side construction grounded in the Axiomata Prima
(cf. axiom:bk1_axiomata_prima) to instantiate it.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Interpretability on Two Axes --- a Complex Reading]
\label{scholium:bk1_interpretability_two_axes}
We can imagine the bounded observer (cf.~\ref{definition:bk1_bounded_observer})
as resolving change not along a single magnitude but across the two axes of the
complex symbolic distance \((d_{\mathrm{Re}}, d_{\mathrm{Im}})\):
\(d_{\mathrm{Re}}\) the \emph{real} mismatch a change induces, \(d_{\mathrm{Im}}\)
the \emph{imaginative} (orientation) residue it leaves. Read this way, the
distinguishability floor \(\nu_{\mathcal{O}}\) of
Def.~\ref{definition:bk1_observer_relative_interpretability} gates
\(d_{\mathrm{Re}}\)---a change is perceived when it is really detectable---while
a continuity ceiling \(\theta_{\mathcal{O}}\) gates \(d_{\mathrm{Im}}\)---a change
is \emph{re-integrable} when it leaves the observer's orientation within bound.
``Really detected and imaginatively continuous'' is then the same operational
criterion Book~IV records as symbolic identity continuity
(cf.~\ref{theorem:bk4_symbolic_identity_continuit}): one observer, read in two
books. We offer this as a lens, not a theorem---conditions
\textbf{(I1)}--\textbf{(I2)} literally bound a single real norm, so the two-axis
reading is a reinterpretation, and a formal identity---to be made precise in the
Operatio (cf.~\ref{sec:bk1_operatio})---would still want the imaginative ceiling
adopted as such, and a Book~I-side construction grounded in the Axiomata Prima
(cf.~\ref{axiom:bk1_axiomata_prima}) to instantiate it.
\end{scholium}
```

### Bounded Approximation Implies Interpretability (`lemma:bk1_bounded_approximation_and_interpretability`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:244`

- Proof status: `proven`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability)
- Cited by: `definition:bk4_refinement_envelope` (Refinement Envelope); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `proof:bk1_energy_bound_identity` (Bounded Energy Ensures Identity Integrity)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-008`
- Witnesses: `ScholiumA.ifValue_le_eps`, `ScholiumA.nu_le_ifValue`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: The c_min ≤ c ≤ 1 and c_min*eps ≥ nu hypotheses genuinely force nu ≤ c*eps ≤ eps; this is a real inequality derivation, not a restatement.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $Phi : P to P$ be an operator on structured states, and let $O$ be a bounded observer (cf. definition:bk1_bounded_observer).
Suppose
\[
\|K_{O} ast [Phi(s) - s]\| = c(s) cdot epsilon_{O}(s)
 text{with } 0 < c_{min} le c(s) le 1.
\]
If the observer resolution satisfies
\[
c_{min} cdot epsilon_{O}(s) ge nu_{O}(s)
 text{for all } s in P,
\]
then $Phi$ is globally $O$–interpretable (cf. definition:bk1_observer_relative_interpretability).

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Bounded Approximation Implies Interpretability]
\label{lemma:bk1_bounded_approximation_and_interpretability}

Let $\Phi : P \to P$ be an operator on structured states, and let $\mathcal{O}$ be a bounded observer (cf.~\ref{definition:bk1_bounded_observer}).
Suppose
\[
\|K_{\mathcal{O}} \ast [\Phi(s) - s]\| = c(s) \cdot \epsilon_{\mathcal{O}}(s)
\quad \text{with } 0 < c_{\min} \le c(s) \le 1.
\]
If the observer resolution satisfies
\[
c_{\min} \cdot \epsilon_{\mathcal{O}}(s) \ge \nu_{\mathcal{O}}(s)
\quad \text{for all } s \in P,
\]
then $\Phi$ is globally $\mathcal{O}$–interpretable (cf.~\ref{definition:bk1_observer_relative_interpretability}).

\end{lemma}
```

### Boundedness of Observer Encoding Cost (`proof:bk1_boundedness_encoding_cost`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:262`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability)
- Cites: `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability)
- Cited by: none
- Macros used: none

**Statement / Body**

To show global $O$–interpretability, we verify conditions (I1)–(I3) from definition:bk1_observer_relative_interpretability:

- (I2) Boundedness: Since \(c(s) le 1\), we have
 \(\|K_{O} ast [Phi(s) - s]\| le epsilon_{O}(s)\).

- (I1) Distinguishability: Follows from
 \(c(s) cdot epsilon_{O}(s) ge c_{min} cdot epsilon_{O}(s) ge nu_{O}(s)\),
 hence the perturbation is detectable.

- (I3) Differential Traceability: Since \(K_{O} ast [Phi(s) - s] ne 0\),
 at least one symbol is perturbed, and the observer’s differential operators \(delta^n_{O}\)
 must detect it for some \(n le N_{O}\).

Thus, all interpretability criteria are met globally. qed

**Verbatim LaTeX Body**

```latex
\begin{proof}[Boundedness of Observer Encoding Cost]
\label{proof:bk1_boundedness_encoding_cost}
\leavevmode

To show global $\mathcal{O}$–interpretability, we verify conditions (I1)–(I3) from \ref{definition:bk1_observer_relative_interpretability}:

- \textbf{(I2) Boundedness:} Since \(c(s) \le 1\), we have
  \(\|K_{\mathcal{O}} \ast [\Phi(s) - s]\| \le \epsilon_{\mathcal{O}}(s)\).

- \textbf{(I1) Distinguishability:} Follows from
  \(c(s) \cdot \epsilon_{\mathcal{O}}(s) \ge c_{\min} \cdot \epsilon_{\mathcal{O}}(s) \ge \nu_{\mathcal{O}}(s)\),
  hence the perturbation is detectable.

- \textbf{(I3) Differential Traceability:} Since \(K_{\mathcal{O}} \ast [\Phi(s) - s] \ne 0\),
  at least one symbol is perturbed, and the observer’s differential operators \(\delta^n_{\mathcal{O}}\)
  must detect it for some \(n \le N_{\mathcal{O}}\).

Thus, all interpretability criteria are met globally. \qed

\end{proof}
```

### Stage–Composite Operators Are Interpretable (`proposition:bk1_stage_composite_operators_are_interpretable`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:285`

- Proof status: `proven`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability); `lemma:bk1_bounded_approximation_and_interpretability` (Bounded Approximation Implies Interpretability)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability)
- Cited by: `proof:bk1_energy_bound_identity` (Bounded Energy Ensures Identity Integrity); `proof:bk4_ttpr_convergence`
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-009`
- Witnesses: `ScholiumA.interpretable_of_factor_and_traceable`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Hypotheses (a) bounded energy approximation and (b) lower-bounded distinguishability are represented by the InterpretabilityFactor sandwich; traceability is supplied as an explicit extra hypothesis (the source's own hypotheses do not entail it either, since (a)/(b) alone give only I1/I2).

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let \(E_lambda : P_{<lambda} to P_lambda\) be a stage-level structural operator
composed of reflective sub-processes \(D_lambda\) and \(R_lambda\),
and let \(O\) be a bounded observer (cf. definition:bk1_bounded_observer).
Suppose for all \(s in P_{<lambda}\):


- \(\|K_{O} ast [E_lambda(s) - s]\| le epsilon_{O}(s)\) hfill (Bounded Energy Approximation)

- \(D_lambda\) induces a lower-bounded change satisfying \(\|K_{O} ast [D_lambda(s) - s]\| ge nu_{O}(s)\)

Then \(E_lambda\) is globally \(O\)–interpretable (cf. definition:bk1_observer_relative_interpretability).

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Stage–Composite Operators Are Interpretable]
\label{proposition:bk1_stage_composite_operators_are_interpretable}

Let \(E_\lambda : P_{<\lambda} \to P_\lambda\) be a stage-level structural operator
composed of reflective sub-processes \(D_\lambda\) and \(R_\lambda\),
and let \(\mathcal{O}\) be a bounded observer (cf.~\ref{definition:bk1_bounded_observer}).
Suppose for all \(s \in P_{<\lambda}\):

\begin{enumerate}[label=(\alph*)]
    \item \(\|K_{\mathcal{O}} \ast [E_\lambda(s) - s]\| \le \epsilon_{\mathcal{O}}(s)\) \hfill \textit{(Bounded Energy Approximation)}
    \item \(D_\lambda\) induces a lower-bounded change satisfying \(\|K_{\mathcal{O}} \ast [D_\lambda(s) - s]\| \ge \nu_{\mathcal{O}}(s)\)
\end{enumerate}

Then \(E_\lambda\) is globally \(\mathcal{O}\)–interpretable (cf.~\ref{definition:bk1_observer_relative_interpretability}).

\end{proposition}
```

### Bounded Energy Ensures Identity Integrity (`proof:bk1_energy_bound_identity`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:302`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability); `lemma:bk1_bounded_approximation_and_interpretability` (Bounded Approximation Implies Interpretability); `proposition:bk1_stage_composite_operators_are_interpretable` (Stage–Composite Operators Are Interpretable)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_stage_composite_operator` (Stage–Composite Operator); `lemma:bk1_bounded_approximation_and_interpretability` (Bounded Approximation Implies Interpretability); `proposition:bk1_stage_composite_operators_are_interpretable` (Stage–Composite Operators Are Interpretable)
- Cited by: none
- Macros used: none

**Statement / Body**

To show interpretability of \(E_lambda\), we verify the three conditions from definition:bk1_observer_relative_interpretability, where \(E_lambda := R_lambda circ D_lambda\) is defined from the stage composite operators (cf. definition:bk1_stage_composite_operator, definition:bk1_pre_geometric_operators_and_stages) and evaluated relative to a bounded observer (cf. definition:bk1_bounded_observer):

- (I2) Boundedness:
 Follows directly from assumption (a), since \(\|K_{O} ast [E_lambda(s) - s]\| le epsilon_{O}(s)\).

- (I1) Distinguishability:
 Assumption (b) gives a lower bound on the signal change induced by \(D_lambda\).
 Since \(E_lambda = R_lambda circ D_lambda\), and \(R_lambda\) preserves the first-order deviation,
 we have:
 \[
 \|K_{O} ast [E_lambda(s) - s]\| ge \|K_{O} ast [D_lambda(s) - s]\| ge nu_{O}(s)
 \]
 by triangle inequality and the assumed preservation.

- (I3) Differential Traceability:
 As \(D_lambda\) alters at least one symbol, and \(R_lambda\) transmits this change structurally
 (cf. definition:bk1_pre_geometric_operators_and_stages),
 there exists an \(n\) such that \(delta^n_{O}(E_lambda(s)) ne delta^n_{O}(s)\),
 ensuring traceability.

Thus, all interpretability conditions are satisfied. qed

**Verbatim LaTeX Body**

```latex
\begin{proof}[Bounded Energy Ensures Identity Integrity]
\label{proof:bk1_energy_bound_identity}
\leavevmode

To show interpretability of \(E_\lambda\), we verify the three conditions from \ref{definition:bk1_observer_relative_interpretability}, where \(E_\lambda := R_\lambda \circ D_\lambda\) is defined from the stage composite operators (cf.~\ref{definition:bk1_stage_composite_operator}, \ref{definition:bk1_pre_geometric_operators_and_stages}) and evaluated relative to a bounded observer (cf.~\ref{definition:bk1_bounded_observer}):

- \textbf{(I2) Boundedness:}
  Follows directly from assumption (a), since \(\|K_{\mathcal{O}} \ast [E_\lambda(s) - s]\| \le \epsilon_{\mathcal{O}}(s)\).

- \textbf{(I1) Distinguishability:}
  Assumption (b) gives a lower bound on the signal change induced by \(D_\lambda\).
  Since \(E_\lambda = R_\lambda \circ D_\lambda\), and \(R_\lambda\) preserves the first-order deviation,
  we have:
  \[
  \|K_{\mathcal{O}} \ast [E_\lambda(s) - s]\| \ge \|K_{\mathcal{O}} \ast [D_\lambda(s) - s]\| \ge \nu_{\mathcal{O}}(s)
  \]
  by triangle inequality and the assumed preservation.

- \textbf{(I3) Differential Traceability:}
  As \(D_\lambda\) alters at least one symbol, and \(R_\lambda\) transmits this change structurally
  (cf.~\ref{definition:bk1_pre_geometric_operators_and_stages}),
  there exists an \(n\) such that \(\delta^n_{\mathcal{O}}(E_\lambda(s)) \ne \delta^n_{\mathcal{O}}(s)\),
  ensuring traceability.

Thus, all interpretability conditions are satisfied. \qed
\end{proof}
```

### Pre-geometric Operators and Stages (`definition:bk1_pre_geometric_operators_and_stages`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:355`

- Proof status: `definitional`
- Depends on: `definition:bk1_let_cats_be_the_category` (Category of Structures)
- Cites: `definition:bk1_let_cats_be_the_category` (Category of Structures)
- Cited by: `axiom:bk1_local_charitability` (Local Chartability); `axiom:bk1_pre_geometric_nature` (Pre-geometric Nature); `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `axiom:bk1_topological_regularity` (Topological Regularity); `definition:bk1_directed_system_of_emergence` (Directed System of Emergence); `definition:bk1_problem_of_symbolic_smoothness` (Problem of Symbolic Smoothness); `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_stage_composite_operator` (Stage–Composite Operator); `lemma:bk1_coherence_of_proto_drift_fields` (Coherence of Proto-Drift Fields); `lemma:bk1_existence_of_metric` (Existence of Metric); `lemma:bk1_observer_bounded_emergence_constraint` (Observer–Bounded Emergence Constraint); `lemma:bk1_universality_of_proto_symbolic_space` (Universality of Proto-symbolic Space); `proof:bk1_atlas_final_topology_phase_space` (Atlas Construction on Final Topology of Symbolic Phase Space); `proof:bk1_bounded_drift_approximation` (Bounded Approximation Guarantees Drift Convergence); `proof:bk1_colimit_yields_categoric_structure` (Colimit Structure Yields Symbolic Cohesion); `proof:bk1_energy_bound_identity` (Bounded Energy Ensures Identity Integrity); `proof:bk1_sketch_coherence_drift_reflection` (Coherence of Proto-Drift Fields via Chart Convergence); `proof:bk1_sketch_construction_proto_metric` (Construction of Proto-Metric on Symbolic Layers); `proof:bk1_sketch_effective_proto_drift_field_induction` (Fundamental Operators as Bounded Symbolic Approximations); `proof:bk1_sketch_limit_stabilization_colimit` (Limit of Stabilization Operators via Colimit); `scholium:bk1_emergence_envelope` (Emergence Envelope); `subsec:appD_category_theory_core_resonance` (D.9.1 Core Resonance)
- Macros used: `\catS`

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-014`
- Witnesses: `ScholiumA.projection_idempotent_ne_id_exists`, `ScholiumC.OperationalStage.drift_advances_stage`, `ScholiumC.OperationalStage.operators_coemerge`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are fields of one OperationalStage witness; neither is derived from the other; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: A categorical OperationalStage now carries drift and idempotent stabilization jointly as one co-emergent witness; neither operator is derived from the other. The drift morphism preserves emergence orientation. The earlier concrete projection remains a nontrivial stabilization witness; ordinal limits, topology, and continuity remain open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Working within category $catS$
(Def. definition:bk1_let_cats_be_the_category), let $Omega$ be a limit
ordinal representing the horizon of emergence.
For each ordinal $lambda < Omega$:


- $P_lambda in Ob(catS)$ is the symbolic structure at stage $lambda$. We assume each $P_lambda$ carries a topology.

- $P_{<lambda} := varinjlim_{mu < lambda} P_mu$ denotes the colimit of all prior stages, endowed with the colimit topology induced by the canonical maps $P_mu to P_{<lambda}$ (for $mu < lambda$).

- The differentiation operator $D_lambda: P_{<lambda} to P_lambda$ generates the symbolic structure at stage $lambda$ from the history encoded in $P_{<lambda}$. This represents the fundamental generative aspect of drift.

- The stabilization operator $R_lambda: P_lambda to P_lambda$ is an idempotent endomorphism ($R_lambda circ R_lambda = R_lambda$) that integrates and consolidates symbolic coherence within stage $lambda$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Pre-geometric Operators and Stages]
\label{definition:bk1_pre_geometric_operators_and_stages}
Working within category $\catS$
(Def.~\ref{definition:bk1_let_cats_be_the_category}), let $\Omega$ be a limit
ordinal representing the horizon of emergence.
For each ordinal $\lambda < \Omega$:
\begin{itemize}
    \item $P_\lambda \in Ob(\catS)$ is the symbolic structure at stage $\lambda$. We assume each $P_\lambda$ carries a topology.
    \item $P_{<\lambda} := \varinjlim_{\mu < \lambda} P_\mu$ denotes the colimit of all prior stages, endowed with the colimit topology induced by the canonical maps $P_\mu \to P_{<\lambda}$ (for $\mu < \lambda$).
    \item The \textbf{differentiation operator} $D_\lambda: P_{<\lambda} \to P_\lambda$ generates the symbolic structure at stage $\lambda$ from the history encoded in $P_{<\lambda}$. This represents the fundamental generative aspect of drift.
    \item The \textbf{stabilization operator} $R_\lambda: P_\lambda \to P_\lambda$ is an idempotent endomorphism ($R_\lambda \circ R_\lambda = R_\lambda$) that integrates and consolidates symbolic coherence within stage $\lambda$.
\end{itemize}
\end{definition}
```

### Observable Gradation of Pre-geometric Operations (`axiom:bk1_observable_gradation_of_pre_geometric_operations`)

Role: `axiom` | Type: `axiom` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:368`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer)
- Cited by: `proof:bk1_sketch_effective_proto_drift_field_induction` (Fundamental Operators as Bounded Symbolic Approximations); `proof:bk4_symbolic_curvature_boundary` (Gradient Threshold and Boundary Formation in Symbolic Geometry)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-094`
- Witnesses: `Atlas.tower_glues`, `ScholiumC.OperationalStage.observed_drift_ne_zero`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other; pair-covering as the topological-regularity stand-in (Hausdorff/second-countable/paracompact/connected unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Observable transformation requires an explicit Observation map and nonzero drift signal; continuity across the stage parameter remains represented only by the Atlas tower-convergence kernel. Detectability is not inferred from category structure.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The operators $D_lambda$ and $R_lambda$ induce observable transformations that vary continuously relative to the stage parameter $lambda$, as perceived by a bounded observer $O$ (cf. definition:bk1_bounded_observer).

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Observable Gradation of Pre-geometric Operations]
\label{axiom:bk1_observable_gradation_of_pre_geometric_operations}
The operators $D_\lambda$ and $R_\lambda$ induce observable transformations that vary continuously relative to the stage parameter $\lambda$, as perceived by a bounded observer $\mathcal{O}$ (cf.~\ref{definition:bk1_bounded_observer}).
\end{axiom}
```

### \textbf{Bounded Symbolic Approximation} (`definition:bk1_bounded_symbolic_approximation`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:373`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability); `lemma:bk4_ttpr_interpretability_preserved` (Precision Refinement Preserves Interpretability); `proof:bk1_bounded_drift_approximation` (Bounded Approximation Guarantees Drift Convergence); `proof:bk1_drift_deviation_bound` (Proto-Drift Induces Directional Deviation Bound); `proof:bk1_sketch_effective_proto_drift_field_induction` (Fundamental Operators as Bounded Symbolic Approximations); `proof:bk4_interpretability_preservation`; `proposition:bk1_boundedness_from_drift` (\textbf{Boundedness from Drift}); `proposition:bk1_the_operators_lambda_and_lambda` (Fundamental Operators as Bounded Symbolic Approximations); `scholium:bk1_consequences_of_bounded_pre_geometric_operations` (Consequences of Bounded Pre-geometric Operations)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-003`
- Witnesses: `ScholiumA.kernelBounded_le`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Folded into one scalar kernel-bound structure/theorem shared with the three anchors below; convolution itself is not modeled, only the stated submultiplicativity inequality.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $O$ be a bounded observer
(cf. Def. definition:bk1_bounded_observer) on a symbolic manifold
(cf. Def. definition:bk1_symbolic_manifold).
An operator $Phi_lambda$ on symbolic structures $S$ is a
bounded symbolic approximation when, for any $s in S$, the
perceived change at $O$ stays below threshold $delta_O$,
i.e.,
\[
\|Phi_lambda(s) - s\|_O leq delta_O.
\]

**Verbatim LaTeX Body**

```latex
\begin{definition}[\textbf{Bounded Symbolic Approximation}]
\label{definition:bk1_bounded_symbolic_approximation}
\leavevmode\newline
Let $\mathcal{O}$ be a bounded observer
(cf.~Def.~\ref{definition:bk1_bounded_observer}) on a symbolic manifold
(cf.~Def.~\ref{definition:bk1_symbolic_manifold}).
An operator $\Phi_\lambda$ on symbolic structures $\mathcal{S}$ is a
\emph{bounded symbolic approximation} when, for any $s \in \mathcal{S}$, the
perceived change at $\mathcal{O}$ stays below threshold $\delta_\mathcal{O}$,
i.e.,
\[
\|\Phi_\lambda(s) - s\|_\mathcal{O} \leq \delta_\mathcal{O}.
\]
\end{definition}
```

### Fundamental Operators as Bounded Symbolic Approximations (`proposition:bk1_the_operators_lambda_and_lambda`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:388`

- Proof status: `proven`
- Depends on: `axiom:bk1_observable_gradation_of_pre_geometric_operations` (Observable Gradation of Pre-geometric Operations); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$); `definition:bk1_reflection_operator` (Reflection Operator)
- Cited by: `proof:bk4_drift_reflection_field` (Symbolic Drift-Reflection Field Dynamics)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-093`
- Witnesses: `AxiomataPrima.no_drift_no_novelty`, `AxiomataPrima.pure_drift_dissolves`
- Countermodels: none
- Conditions: face 3 consumes the guarded-process machinery (LPS-P49) and the helix kernel (LPS-P48); the metaphysical scope of a three-word axiom is not exhausted; the operational tri-face kernel is what is certified
- Formal boundary: D_lambda, R_lambda as bounded symbolic approximations: their single-channel failure modes are certified; the bounded-approximation predicate stays interpretive.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The operators $D_lambda$ and $R_lambda$ from Definition definition:bk1_proto_drift_field and Definition definition:bk1_reflection_operator are bounded symbolic approximations per Definition definition:bk1_bounded_symbolic_approximation, assuming observer-resolved emergence.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Fundamental Operators as Bounded Symbolic Approximations]
\label{proposition:bk1_the_operators_lambda_and_lambda}
The operators $D_\lambda$ and $R_\lambda$ from Definition~\ref{definition:bk1_proto_drift_field} and Definition~\ref{definition:bk1_reflection_operator} are bounded symbolic approximations per Definition~\ref{definition:bk1_bounded_symbolic_approximation}, assuming observer-resolved emergence.
\end{proposition}
```

### Fundamental Operators as Bounded Symbolic Approximations (`proof:bk1_sketch_effective_proto_drift_field_induction`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:392`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_observable_gradation_of_pre_geometric_operations` (Observable Gradation of Pre-geometric Operations); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `axiom:bk1_observable_gradation_of_pre_geometric_operations` (Observable Gradation of Pre-geometric Operations); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$)
- Cited by: none
- Macros used: none

**Statement / Body**

For $D_lambda$.\ By Ax. axiom:bk1_observable_gradation_of_pre_geometric_operations,
\(D_lambda\) induces transformations that are observable to the bounded
observer \(O\). Observer-resolved emergence means that the effective
change registered by \(O\) lies inside its resolution threshold
\(delta_{O}\) (Def. definition:bk1_bounded_observer). For
\[
vec{D}_lambda^{eff}(s)=D_lambda(s)ominus s
\]
as the observer-visible proto-drift deviation
(Def. definition:bk1_proto_drift_field), this gives
\[
\|vec{D}_lambda^{eff}(s)\|_{O}leq delta_{O}
\]
on the observer-resolved domain. This is exactly the bounded symbolic
approximation condition of Def. definition:bk1_bounded_symbolic_approximation.

For $R_lambda$.
\(R_lambda:P_lambdato P_lambda\) is the idempotent stabilization operator
of Def. definition:bk1_pre_geometric_operators_and_stages. The same
observable-gradation axiom applies to its observer-visible stabilization
deviation \(R_lambda(s)-s\), and observer resolution gives
\[
\|R_lambda(s)-s\|_{O}leq delta_{O}
\]
for \(sin P_lambda\). Hence \(R_lambda\) also satisfies
Def. definition:bk1_bounded_symbolic_approximation.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Fundamental Operators as Bounded Symbolic Approximations]
\label{proof:bk1_sketch_effective_proto_drift_field_induction}
\leavevmode

\textbf{For $D_\lambda$.}\ By Ax.~\ref{axiom:bk1_observable_gradation_of_pre_geometric_operations},
\(D_\lambda\) induces transformations that are observable to the bounded
observer \(\mathcal{O}\). Observer-resolved emergence means that the effective
change registered by \(\mathcal{O}\) lies inside its resolution threshold
\(\delta_{\mathcal{O}}\) (Def.~\ref{definition:bk1_bounded_observer}). For
\[
\vec{D}_\lambda^{eff}(s)=D_\lambda(s)\ominus s
\]
as the observer-visible proto-drift deviation
(Def.~\ref{definition:bk1_proto_drift_field}), this gives
\[
\|\vec{D}_\lambda^{eff}(s)\|_{\mathcal{O}}\leq \delta_{\mathcal{O}}
\]
on the observer-resolved domain. This is exactly the bounded symbolic
approximation condition of Def.~\ref{definition:bk1_bounded_symbolic_approximation}.

\textbf{For $R_\lambda$.}
\(R_\lambda:P_\lambda\to P_\lambda\) is the idempotent stabilization operator
of Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}. The same
observable-gradation axiom applies to its observer-visible stabilization
deviation \(R_\lambda(s)-s\), and observer resolution gives
\[
\|R_\lambda(s)-s\|_{\mathcal{O}}\leq \delta_{\mathcal{O}}
\]
for \(s\in P_\lambda\). Hence \(R_\lambda\) also satisfies
Def.~\ref{definition:bk1_bounded_symbolic_approximation}.
\end{proof}
```

### Consequences of Bounded Pre-geometric Operations (`scholium:bk1_consequences_of_bounded_pre_geometric_operations`)

Role: `scholium` | Type: `scholium` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:424`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation})
- Cites: `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)})
- Cited by: none
- Macros used: none

**Statement / Body**

Boundedness of $D_lambda$ and $R_lambda$ ensures stability of emergent structure, constraining drift intensity and symbolic fluctuation across $lambda$.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Consequences of Bounded Pre-geometric Operations]
\label{scholium:bk1_consequences_of_bounded_pre_geometric_operations}
Boundedness of $D_\lambda$ and $R_\lambda$ ensures stability of emergent structure, constraining drift intensity and symbolic fluctuation across $\lambda$.
\end{scholium}
```

### Relating Process-Oriented Boundedness to a Kernel-Based Model (`remark:scholium_symbolicum.tex:429`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:429`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The kernel-based formulation of symbolic approximation (cf. definition:bk1_kernel_based_bounded_symbolic_approximation) is an instance of the broader process-oriented model (cf. definition:bk1_bounded_symbolic_approximation), where convolution with $K_O$ provides an observable-resolved smoothing interpretation.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Relating Process-Oriented Boundedness to a Kernel-Based Model]
The kernel-based formulation of symbolic approximation (cf.~\ref{definition:bk1_kernel_based_bounded_symbolic_approximation}) is an instance of the broader process-oriented model (cf.~\ref{definition:bk1_bounded_symbolic_approximation}), where convolution with $\mathcal{K}_\mathcal{O}$ provides an observable-resolved smoothing interpretation.
\end{remark}
```

### \textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)} (`definition:bk1_kernel_based_bounded_symbolic_approximation`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:433`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer)
- Cited by: `definition:bk1_observer_relative_interpretability` (Observer–Relative Interpretability); `definition:bk4_coherence_metric` (Observer-Weighted Coherence Metric); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `lemma:bk1_observer_bounded_emergence_constraint` (Observer–Bounded Emergence Constraint); `proof:bk1_fix_s_in_s` (Symbol Preservation Under Drift–Reflection Fixation); `proof:bk1_observer_kernel_convolution` (Convolutional Identity from Observer Kernel Properties); `proposition:bk1_sufficient_condition_for_kernel_boundedness_from_uniform_drift_bound` (\textbf{Sufficient Condition for Kernel-Boundedness from Uniform Drift Bound}); `remark:bk1_kernel_based_bounded_approximation` (Alternative Perspective: Kernel-Based Bounded Approximation); `scholium:bk1_consequences_of_bounded_pre_geometric_operations` (Consequences of Bounded Pre-geometric Operations)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-004`
- Witnesses: `ScholiumA.kernelBounded_le`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Same KernelBoundedApprox structure as bk1_bounded_symbolic_approximation; the iff-form of the source definition is not modeled, only the derived bound.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $O$ be a bounded observer with resolution kernel $K_O$ as specified in Definition definition:bk1_bounded_observer. An operator $Phi_lambda$ (or $Psi_lambda$) acting on symbolic structures $S$ is said to be a kernel-bounded symbolic approximation if and only if for any symbol $s in S$ and its image $Phi_lambda(s)$, the perceptual difference as measured by $O$ satisfies:

\|K_O ast [Phi_lambda(s) - s]\| leq delta_O,

where $delta_O > 0$ is the resolution threshold of $O$ and $ast$ denotes the convolution operation.

**Verbatim LaTeX Body**

```latex
\begin{definition}[\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)}]
\label{definition:bk1_kernel_based_bounded_symbolic_approximation}
Let $\mathcal{O}$ be a bounded observer with resolution kernel $\mathcal{K}_\mathcal{O}$ as specified in Definition~\ref{definition:bk1_bounded_observer}. An operator $\Phi_\lambda$ (or $\Psi_\lambda$) acting on symbolic structures $\mathcal{S}$ is said to be a \emph{kernel-bounded symbolic approximation} if and only if for any symbol $s \in \mathcal{S}$ and its image $\Phi_\lambda(s)$, the perceptual difference as measured by $\mathcal{O}$ satisfies:
\begin{equation}
\|\mathcal{K}_\mathcal{O} \ast [\Phi_\lambda(s) - s]\| \leq \delta_\mathcal{O},
\end{equation}
where $\delta_\mathcal{O} > 0$ is the resolution threshold of $\mathcal{O}$ and $\ast$ denotes the convolution operation.
\end{definition}
```

### \textbf{Boundedness from Drift} (`proposition:bk1_boundedness_from_drift`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:442`

- Proof status: `proven`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation})
- Cites: `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$)
- Cited by: `remark:bk1_kernel_based_bounded_approximation` (Alternative Perspective: Kernel-Based Bounded Approximation)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-005`
- Witnesses: `ScholiumA.kernelBounded_le`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: The sup-bound hypothesis is represented as a plain scalar bound (drift ≤ δ) rather than an actual supremum over a domain.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $vec{D}_lambda$ be the proto-drift field induced by operators $Phi_lambda$ and $Psi_lambda$ as defined in Definition definition:bk1_proto_drift_field. If $vec{D}_lambda$ satisfies:

sup_{x in dom(D_lambda)} \|vec{D}_lambda(x)\| leq delta_O,

then both $Phi_lambda$ and $Psi_lambda$ are bounded symbolic approximations with respect to observer $O$ (cf. definition:bk1_bounded_symbolic_approximation).

**Verbatim LaTeX Body**

```latex
\begin{proposition}[\textbf{Boundedness from Drift}]
\label{proposition:bk1_boundedness_from_drift}
Let $\vec{D}_\lambda$ be the proto-drift field induced by operators $\Phi_\lambda$ and $\Psi_\lambda$ as defined in Definition~\ref{definition:bk1_proto_drift_field}. If $\vec{D}_\lambda$ satisfies:
\begin{equation}
\sup_{x \in \mathrm{dom}(D_\lambda)} \|\vec{D}_\lambda(x)\| \leq \delta_\mathcal{O},
\end{equation}
then both $\Phi_\lambda$ and $\Psi_\lambda$ are bounded symbolic approximations with respect to observer $\mathcal{O}$ (cf.~\ref{definition:bk1_bounded_symbolic_approximation}).
\end{proposition}
```

### Proto-Drift Induces Directional Deviation Bound (`proof:bk1_drift_deviation_bound`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:451`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation})
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$)
- Cited by: `proof:bk1_observer_kernel_convolution` (Convolutional Identity from Observer Kernel Properties)
- Macros used: none

**Statement / Body**

Let $s in S$ be an arbitrary symbolic structure. Expanding the proto-drift field (Def. definition:bk1_proto_drift_field), $vec{D}_lambda(s) = Phi_lambda(s) - s$ for any $s$ in the domain of $Phi_lambda$. Given the supremum condition:
\[
sup_{x in dom(D_lambda)} \|vec{D}_lambda(x)\| leq delta_O,
\]
it follows that $\|vec{D}_lambda(s)\| leq delta_O$ for all $s$ in the domain.
Since $K_O$ is a resolution kernel of a bounded observer (Def. definition:bk1_bounded_observer), it satisfies $\|K_O\|_1 = 1$ (normalization). By the properties of convolution and norms:

\|K_O ast [Phi_lambda(s) - s]\| &= \|K_O ast vec{D}_lambda(s)\| \\
&leq \|K_O\|_1 cdot \|vec{D}_lambda(s)\| \\
&= \|vec{D}_lambda(s)\| \\
&leq delta_O

Therefore, $Phi_lambda$ satisfies the condition to be a bounded symbolic approximation. The proof for $Psi_lambda$ follows similarly by observing that the proto-drift field $vec{D}_lambda$ also encodes the action of $Psi_lambda$ through the inverse relationship established in Definition definition:bk1_bounded_symbolic_approximation.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Proto-Drift Induces Directional Deviation Bound]
\label{proof:bk1_drift_deviation_bound}
\leavevmode

Let $s \in \mathcal{S}$ be an arbitrary symbolic structure. Expanding the proto-drift field (Def.~\ref{definition:bk1_proto_drift_field}), $\vec{D}_\lambda(s) = \Phi_\lambda(s) - s$ for any $s$ in the domain of $\Phi_\lambda$. Given the supremum condition:
\[
\sup_{x \in \mathrm{dom}(D_\lambda)} \|\vec{D}_\lambda(x)\| \leq \delta_\mathcal{O},
\]
it follows that $\|\vec{D}_\lambda(s)\| \leq \delta_\mathcal{O}$ for all $s$ in the domain.
Since $\mathcal{K}_\mathcal{O}$ is a resolution kernel of a bounded observer (Def.~\ref{definition:bk1_bounded_observer}), it satisfies $\|\mathcal{K}_\mathcal{O}\|_1 = 1$ (normalization). By the properties of convolution and norms:
\begin{align}
\|\mathcal{K}_\mathcal{O} \ast [\Phi_\lambda(s) - s]\| &= \|\mathcal{K}_\mathcal{O} \ast \vec{D}_\lambda(s)\| \\
&\leq \|\mathcal{K}_\mathcal{O}\|_1 \cdot \|\vec{D}_\lambda(s)\| \\
&= \|\vec{D}_\lambda(s)\| \\
&\leq \delta_\mathcal{O}
\end{align}
Therefore, $\Phi_\lambda$ satisfies the condition to be a bounded symbolic approximation. The proof for $\Psi_\lambda$ follows similarly by observing that the proto-drift field $\vec{D}_\lambda$ also encodes the action of $\Psi_\lambda$ through the inverse relationship established in Definition~\ref{definition:bk1_bounded_symbolic_approximation}.
\end{proof}
```

### Alternative Perspective: Kernel-Based Bounded Approximation (`remark:bk1_kernel_based_bounded_approximation`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:470`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)}); `proposition:bk1_boundedness_from_drift` (\textbf{Boundedness from Drift})
- Cites: `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)}); `proposition:bk1_boundedness_from_drift` (\textbf{Boundedness from Drift})
- Cited by: none
- Macros used: none

**Statement / Body**

An alternative, more concrete way to conceptualize how an observer $O$ might implement or model the perception of boundedness involves considering a resolution kernel $K_O$ (as specified in Definition definition:bk1_kernel_based_bounded_symbolic_approximation).
In this view, an operator $Phi_lambda$ acting on symbolic structures $S$ could be considered a kernel-bounded symbolic approximation if for any symbol $s in S$ and its image $Phi_lambda(s)$, the perceptual difference as measured by convolution with $K_O$ satisfies:
\[
\|K_O ast [Phi_lambda(s) - s]\| leq delta_O,
\]
where $delta_O > 0$ is the resolution threshold of $O$.

This perspective leads to a corresponding sufficient condition: if a proto-drift field $vec{D}_lambda(s) = Phi_lambda(s) - s$ satisfies $sup_{x in dom(D_lambda)} \|vec{D}_lambda(x)\| leq delta_O$, then $Phi_lambda$ is a kernel-bounded symbolic approximation. (The proof follows as in Proposition proposition:bk1_boundedness_from_drift).

While the process-oriented Definition definition:bk1_kernel_based_bounded_symbolic_approximation is considered more fundamental within Principia Symbolica as it directly leverages the observer's differentiation capacity, the kernel-based perspective can provide a useful illustrative model, particularly when analogizing to systems where perceptual filtering is well-described by such convolution operations. The core principle remains that the change induced by the operator must be sub-threshold for the observer.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Alternative Perspective: Kernel-Based Bounded Approximation]
\label{remark:bk1_kernel_based_bounded_approximation}
An alternative, more concrete way to conceptualize how an observer $\mathcal{O}$ might implement or model the perception of boundedness involves considering a resolution kernel $\mathcal{K}_\mathcal{O}$ (as specified in Definition~\ref{definition:bk1_kernel_based_bounded_symbolic_approximation}).
In this view, an operator $\Phi_\lambda$ acting on symbolic structures $\mathcal{S}$ could be considered a \emph{kernel-bounded symbolic approximation} if for any symbol $s \in \mathcal{S}$ and its image $\Phi_\lambda(s)$, the perceptual difference as measured by convolution with $\mathcal{K}_\mathcal{O}$ satisfies:
\[
\|\mathcal{K}_\mathcal{O} \ast [\Phi_\lambda(s) - s]\| \leq \delta_\mathcal{O},
\]
where $\delta_\mathcal{O} > 0$ is the resolution threshold of $\mathcal{O}$.

This perspective leads to a corresponding sufficient condition: if a proto-drift field $\vec{D}_\lambda(s) = \Phi_\lambda(s) - s$ satisfies $\sup_{x \in \mathrm{dom}(D_\lambda)} \|\vec{D}_\lambda(x)\| \leq \delta_\mathcal{O}$, then $\Phi_\lambda$ is a kernel-bounded symbolic approximation. (The proof follows as in Proposition~\ref{proposition:bk1_boundedness_from_drift}).

While the process-oriented Definition~\ref{definition:bk1_kernel_based_bounded_symbolic_approximation} is considered more fundamental within \textit{Principia Symbolica} as it directly leverages the observer's differentiation capacity, the kernel-based perspective can provide a useful illustrative model, particularly when analogizing to systems where perceptual filtering is well-described by such convolution operations. The core principle remains that the change induced by the operator must be sub-threshold for the observer.
\end{remark}
```

### Observer Threshold Governs Reflexive Admissibility (`proof:bk1_observer_threshold_reflexivity`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:489`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `lemma:bk1_observer_bounded_emergence_constraint` (Observer–Bounded Emergence Constraint)
- Cited by: `abs:press` (Press Abstract (Non-specialist science readers))
- Macros used: none

**Statement / Body**

This follows directly from Lemma lemma:bk1_observer_bounded_emergence_constraint and Definition definition:bk1_bounded_observer. The lemma states that the observer-perceived change induced by $D_lambda$ and $R_lambda$ is less than or equal to the observer's resolution threshold, which is precisely the condition required by the definition.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Observer Threshold Governs Reflexive Admissibility]
\label{proof:bk1_observer_threshold_reflexivity}
\leavevmode

This follows directly from Lemma~\ref{lemma:bk1_observer_bounded_emergence_constraint} and Definition~\ref{definition:bk1_bounded_observer}. The lemma states that the observer-perceived change induced by $D_\lambda$ and $R_\lambda$ is less than or equal to the observer's resolution threshold, which is precisely the condition required by the definition.
\end{proof}
```

### \textbf{Sufficient Condition for Kernel-Boundedness from Uniform Drift Bound} (`proposition:bk1_sufficient_condition_for_kernel_boundedness_from_uniform_drift_bound`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:495`

- Proof status: `proven`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)}); `proof:bk1_drift_deviation_bound` (Proto-Drift Induces Directional Deviation Bound)
- Cites: `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)})
- Cited by: `proof:bk1_observer_kernel_convolution` (Convolutional Identity from Observer Kernel Properties)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-006`
- Witnesses: `ScholiumA.kernelBounded_le`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: This anchor's own inline proof is exactly the ‖K‖1=1 submultiplicativity chain now proved by kernelBounded_le; kernel norm and convolution remain hypotheses, not derived objects.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $vec{D}_lambda$ be the proto-drift field induced by operators $Phi_lambda$ and $Psi_lambda$ such that $vec{D}_lambda(s) = Phi_lambda(s) - s$ (or an appropriate difference). If $vec{D}_lambda$ satisfies:

sup_{x in dom(D_lambda)} \|vec{D}_lambda(x)\| leq delta_O,

then both $Phi_lambda$ and $Psi_lambda$ are kernel-bounded symbolic approximations (Def definition:bk1_kernel_based_bounded_symbolic_approximation) with respect to observer $O$.

(Proposition proposition:bk1_sufficient_condition_for_kernel_boundedness_from_uniform_drift_bound, which uses $\|K_O\|_1 = 1$ and properties of convolution, remains valid for this proposition.)

Let $s in S$ be an arbitrary symbolic structure. Expanding the proto-drift field (Def. definition:bk1_proto_drift_field), $vec{D}_lambda(s) = Phi_lambda(s) - s$ for any $s$ in the domain of $Phi_lambda$. Given the supremum condition (Eq. proof:bk1_drift_deviation_bound), it follows that $\|vec{D}_lambda(s)\| leq delta_O$ for all $s$ in the domain.

Since $K_O$ is a resolution kernel of a bounded observer (Def. definition:bk1_bounded_observer), it satisfies $\|K_O\|_1 = 1$ (normalization property). By the properties of convolution and norms, and the criteria for kernel-bounded approximation (Def. definition:bk1_kernel_based_bounded_symbolic_approximation), using $Phi_lambda(s) - s = vec{D}_lambda(s)$:

\|K_O ast vec{D}_lambda(s)\| &leq \|K_O\|_1 cdot \|vec{D}_lambda(s)\| \\
&= \|vec{D}_lambda(s)\| \\
&leq delta_O

Therefore, $Phi_lambda$ satisfies the condition to be a kernel-bounded symbolic approximation. The proof for $Psi_lambda$ follows similarly.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[\textbf{Sufficient Condition for Kernel-Boundedness from Uniform Drift Bound}]
\label{proposition:bk1_sufficient_condition_for_kernel_boundedness_from_uniform_drift_bound}
Let $\vec{D}_\lambda$ be the proto-drift field induced by operators $\Phi_\lambda$ and $\Psi_\lambda$ such that $\vec{D}_\lambda(s) = \Phi_\lambda(s) - s$ (or an appropriate difference). If $\vec{D}_\lambda$ satisfies:
\begin{equation}
\sup_{x \in \mathrm{dom}(D_\lambda)} \|\vec{D}_\lambda(x)\| \leq \delta_\mathcal{O},
\end{equation}
then both $\Phi_\lambda$ and $\Psi_\lambda$ are kernel-bounded symbolic approximations (Def~\ref{definition:bk1_kernel_based_bounded_symbolic_approximation}) with respect to observer $\mathcal{O}$.
\begin{proof}[Convolutional Identity from Observer Kernel Properties]
\label{proof:bk1_observer_kernel_convolution}
\leavevmode

(Proposition~\ref{proposition:bk1_sufficient_condition_for_kernel_boundedness_from_uniform_drift_bound}, which uses $\|\mathcal{K}_\mathcal{O}\|_1 = 1$ and properties of convolution, remains valid for this proposition.)

Let $s \in \mathcal{S}$ be an arbitrary symbolic structure. Expanding the proto-drift field (Def.~\ref{definition:bk1_proto_drift_field}), $\vec{D}_\lambda(s) = \Phi_\lambda(s) - s$ for any $s$ in the domain of $\Phi_\lambda$. Given the supremum condition (Eq.~\ref{proof:bk1_drift_deviation_bound}), it follows that $\|\vec{D}_\lambda(s)\| \leq \delta_\mathcal{O}$ for all $s$ in the domain.

Since $\mathcal{K}_\mathcal{O}$ is a resolution kernel of a bounded observer (Def.~\ref{definition:bk1_bounded_observer}), it satisfies $\|\mathcal{K}_\mathcal{O}\|_1 = 1$ (normalization property). By the properties of convolution and norms, and the criteria for kernel-bounded approximation (Def.~\ref{definition:bk1_kernel_based_bounded_symbolic_approximation}), using $\Phi_\lambda(s) - s = \vec{D}_\lambda(s)$:
\begin{align}
\|\mathcal{K}_\mathcal{O} \ast \vec{D}_\lambda(s)\| &\leq \|\mathcal{K}_\mathcal{O}\|_1 \cdot \|\vec{D}_\lambda(s)\| \\
&= \|\vec{D}_\lambda(s)\| \\
&\leq \delta_\mathcal{O}
\end{align}

Therefore, $\Phi_\lambda$ satisfies the condition to be a kernel-bounded symbolic approximation. The proof for $\Psi_\lambda$ follows similarly.
\end{proof}
\end{proposition}
```

### Convolutional Identity from Observer Kernel Properties (`proof:bk1_observer_kernel_convolution`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:502`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)}); `proof:bk1_drift_deviation_bound` (Proto-Drift Induces Directional Deviation Bound); `proposition:bk1_sufficient_condition_for_kernel_boundedness_from_uniform_drift_bound` (\textbf{Sufficient Condition for Kernel-Boundedness from Uniform Drift Bound})
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)}); `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$); `proof:bk1_drift_deviation_bound` (Proto-Drift Induces Directional Deviation Bound); `proposition:bk1_sufficient_condition_for_kernel_boundedness_from_uniform_drift_bound` (\textbf{Sufficient Condition for Kernel-Boundedness from Uniform Drift Bound})
- Cited by: none
- Macros used: none

**Statement / Body**

(Proposition proposition:bk1_sufficient_condition_for_kernel_boundedness_from_uniform_drift_bound, which uses $\|K_O\|_1 = 1$ and properties of convolution, remains valid for this proposition.)

Let $s in S$ be an arbitrary symbolic structure. Expanding the proto-drift field (Def. definition:bk1_proto_drift_field), $vec{D}_lambda(s) = Phi_lambda(s) - s$ for any $s$ in the domain of $Phi_lambda$. Given the supremum condition (Eq. proof:bk1_drift_deviation_bound), it follows that $\|vec{D}_lambda(s)\| leq delta_O$ for all $s$ in the domain.

Since $K_O$ is a resolution kernel of a bounded observer (Def. definition:bk1_bounded_observer), it satisfies $\|K_O\|_1 = 1$ (normalization property). By the properties of convolution and norms, and the criteria for kernel-bounded approximation (Def. definition:bk1_kernel_based_bounded_symbolic_approximation), using $Phi_lambda(s) - s = vec{D}_lambda(s)$:

\|K_O ast vec{D}_lambda(s)\| &leq \|K_O\|_1 cdot \|vec{D}_lambda(s)\| \\
&= \|vec{D}_lambda(s)\| \\
&leq delta_O

Therefore, $Phi_lambda$ satisfies the condition to be a kernel-bounded symbolic approximation. The proof for $Psi_lambda$ follows similarly.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Convolutional Identity from Observer Kernel Properties]
\label{proof:bk1_observer_kernel_convolution}
\leavevmode

(Proposition~\ref{proposition:bk1_sufficient_condition_for_kernel_boundedness_from_uniform_drift_bound}, which uses $\|\mathcal{K}_\mathcal{O}\|_1 = 1$ and properties of convolution, remains valid for this proposition.)

Let $s \in \mathcal{S}$ be an arbitrary symbolic structure. Expanding the proto-drift field (Def.~\ref{definition:bk1_proto_drift_field}), $\vec{D}_\lambda(s) = \Phi_\lambda(s) - s$ for any $s$ in the domain of $\Phi_\lambda$. Given the supremum condition (Eq.~\ref{proof:bk1_drift_deviation_bound}), it follows that $\|\vec{D}_\lambda(s)\| \leq \delta_\mathcal{O}$ for all $s$ in the domain.

Since $\mathcal{K}_\mathcal{O}$ is a resolution kernel of a bounded observer (Def.~\ref{definition:bk1_bounded_observer}), it satisfies $\|\mathcal{K}_\mathcal{O}\|_1 = 1$ (normalization property). By the properties of convolution and norms, and the criteria for kernel-bounded approximation (Def.~\ref{definition:bk1_kernel_based_bounded_symbolic_approximation}), using $\Phi_\lambda(s) - s = \vec{D}_\lambda(s)$:
\begin{align}
\|\mathcal{K}_\mathcal{O} \ast \vec{D}_\lambda(s)\| &\leq \|\mathcal{K}_\mathcal{O}\|_1 \cdot \|\vec{D}_\lambda(s)\| \\
&= \|\vec{D}_\lambda(s)\| \\
&\leq \delta_\mathcal{O}
\end{align}

Therefore, $\Phi_\lambda$ satisfies the condition to be a kernel-bounded symbolic approximation. The proof for $\Psi_\lambda$ follows similarly.
\end{proof}
```

### Stage–Composite Operator (`definition:bk1_stage_composite_operator`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:520`

- Proof status: `definitional`
- Depends on: `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cited by: `definition:appC_bounded_reflexive_emergence` (Bounded reflexive emergence); `definition:appC_complexity_measure` (Complexity Measure); `definition:appC_symbolic_modality` (Symbolic modality); `lemma:bk1_observer_bounded_emergence_constraint` (Observer–Bounded Emergence Constraint); `proof:appC_phi_from_lagrangian`; `proof:bk1_bounded_drift_approximation` (Bounded Approximation Guarantees Drift Convergence); `proof:bk1_energy_bound_identity` (Bounded Energy Ensures Identity Integrity)
- Macros used: none

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-010`
- Witnesses: `ScholiumA.twoStep_bound`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Modeled as the TwoStepBoundedApprox structure's stabilize ∘ drift composite; no standalone theorem beyond twoStep_bound.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let \(D_lambda : P_{<lambda} to P_lambda\) be a symbolic transformation representing directional drift, and let \(R_lambda : P_lambda to P_lambda\) be a refinement or reflection operator
(as preliminarily introduced in Definition definition:bk1_pre_geometric_operators_and_stages).

Then the stage-composite operator at ordinal level \(lambda\) is defined as:
\[
E_lambda := R_lambda circ D_lambda : P_{<lambda} to P_lambda.
\]
Such operators encode a two-step symbolic emergence: first a directional transformation, then a bounded symbolic refinement.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Stage–Composite Operator]
\label{definition:bk1_stage_composite_operator}
Let \(D_\lambda : P_{<\lambda} \to P_\lambda\) be a symbolic transformation representing directional drift, and let \(R_\lambda : P_\lambda \to P_\lambda\) be a refinement or reflection operator
(as preliminarily introduced in Definition~\ref{definition:bk1_pre_geometric_operators_and_stages}).

Then the \textbf{stage--composite operator} at ordinal level \(\lambda\) is defined as:
\[
E_\lambda := R_\lambda \circ D_\lambda : P_{<\lambda} \to P_\lambda.
\]
Such operators encode a two-step symbolic emergence: first a directional transformation, then a bounded symbolic refinement.
\end{definition}
```

### Summable Resolution Decay (`axiom:bk1_summable_resolution_decay`)

Role: `axiom` | Type: `axiom` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:532`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `lemma:bk1_observer_bounded_emergence_constraint` (Observer–Bounded Emergence Constraint); `proof:bk1_bounded_drift_approximation` (Bounded Approximation Guarantees Drift Convergence); `scholium:bk1_emergence_envelope` (Emergence Envelope)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-012`
- Witnesses: `ScholiumA.ChainedApprox.cauchySeq`, `ScholiumA.ChainedApprox.exists_limit_with_tail_bound`, `ScholiumA.chainedApprox_telescope`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Summability is an explicit ChainedApprox field. It yields finite telescoping, a genuine Cauchy stage path, and under completeness an actual limit with tail-sum displacement bound.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let \((lambda_n)_{ninmathbb{N}}\) be a cofinal sequence in the emergence
tower with \(lambda_n<lambda_{n+1}<Omega\) and
\(sup_nlambda_n=Omega\). Relative to a bounded observer \(O\), assume there
exists a positive sequence \((eta_n)_{ninmathbb{N}}\) such that
\[
sum_{n=0}^{infty}eta_n < infty
\]
and, along this cofinal tower,
\[
d_O(E_{lambda_n}(s),s)
= lVert K_O * [E_{lambda_n}(s)-s]rVert
leq eta_n
 text{for all observable }sin P_{<lambda_n}.
\]
Thus later-stage refinements are not merely bounded one at a time; their
observer-visible tail is summable. No claim is made here for emergence towers
of uncountable cofinality except through such selected cofinal sequences.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Summable Resolution Decay]
\label{axiom:bk1_summable_resolution_decay}
Let \((\lambda_n)_{n\in\mathbb{N}}\) be a cofinal sequence in the emergence
tower with \(\lambda_n<\lambda_{n+1}<\Omega\) and
\(\sup_n\lambda_n=\Omega\). Relative to a bounded observer \(O\), assume there
exists a positive sequence \((\eta_n)_{n\in\mathbb{N}}\) such that
\[
\sum_{n=0}^{\infty}\eta_n < \infty
\]
and, along this cofinal tower,
\[
d_O(E_{\lambda_n}(s),s)
= \lVert K_O * [E_{\lambda_n}(s)-s]\rVert
\leq \eta_n
\quad\text{for all observable }s\in P_{<\lambda_n}.
\]
Thus later-stage refinements are not merely bounded one at a time; their
observer-visible tail is summable. No claim is made here for emergence towers
of uncountable cofinality except through such selected cofinal sequences.
\end{axiom}
```

### Observer–Bounded Emergence Constraint (`lemma:bk1_observer_bounded_emergence_constraint`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:553`

- Proof status: `proven`
- Depends on: `axiom:bk1_summable_resolution_decay` (Summable Resolution Decay); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)}); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_stage_composite_operator` (Stage–Composite Operator)
- Cites: `axiom:bk1_summable_resolution_decay` (Summable Resolution Decay); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_directed_system_of_emergence` (Directed System of Emergence); `definition:bk1_kernel_based_bounded_symbolic_approximation` (\textbf{Kernel-Based Bounded Symbolic Approximation (Illustration)}); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space); `definition:bk1_stage_composite_operator` (Stage–Composite Operator)
- Cited by: `proof:bk1_observer_threshold_reflexivity` (Observer Threshold Governs Reflexive Admissibility); `proof:bk4_ttpr_convergence`; `proposition:bk4_ttpr_convergence` (Convergence of Recursive Refinement)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-011`
- Witnesses: `ScholiumA.ChainedApprox.cauchySeq`, `ScholiumA.ChainedApprox.exists_limit_with_tail_bound`, `ScholiumA.chainedApprox_telescope`, `ScholiumA.twoStep_bound`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Part (i)'s 2δ bound follows from the triangle inequality. Part (ii) includes finite telescoping and, from summable resolution decay, full Cauchy and complete-space convergence with a tail displacement bound.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let
\(
O=(N_O,{delta^{ n}_{O}}_{n=1}^{N_O},varepsilon_O)
\)
be a bounded observer with resolution kernel \(K_O\) and scalar threshold \(delta_O\) (Definition definition:bk1_bounded_observer).
For every ordinal \(lambda<Omega\), define the stage-composite operator
\[
 E_lambda := R_lambda circ D_lambda : P_{<lambda} longrightarrow P_lambda,
\]
as defined in Definition definition:bk1_stage_composite_operator,
where \(P_{<lambda}\) and \(P_lambda\) are symbolic stages introduced in Definition definition:bk1_pre_geometric_operators_and_stages.
Then


- Bounded approximation of the identity.
 For all \(sin P_{<lambda}\),

 bigllVert K_O * bigl[E_lambda(s) - sbigr] bigrrVert
 le 2 delta_O.

 (This satisfies the kernel-bounded approximation condition in Definition definition:bk1_kernel_based_bounded_symbolic_approximation.)


- Cauchy tower under summable decay.
 Endow every \(P_lambda\) with the observer metric
 \(
 d_O(x,y) := lVert K_O * (x - y) rVert.
 \)
 Along any cofinal sequence \((lambda_n)\) satisfying
 Ax. axiom:bk1_summable_resolution_decay, the transition maps obey
 \[
 d_O(f_{lambda_mlambda_n}(x),x)
 leq sum_{j=m}^{n-1}eta_j

 forall x in P_{lambda_m},
 m<n,
 \]
 so the cofinal directed subsystem
 \(
 (P_{lambda_n}, f_{lambda_mlambda_n})_{m<n}
 \)
 is \(d_O\)-Cauchy in the usual tail sense
 (see also the formal directed emergence structure in Definition definition:bk1_directed_system_of_emergence). Its \(d_O\)-completion
 \(
 overline{P}_O
 \)
 supplies the observer-completed proto-symbolic space associated with
 the colimit \(P=varinjlim_{lambda<Omega}P_lambda\)
 (Definition definition:bk1_proto_symbolic_space).

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Observer–Bounded Emergence Constraint]
\label{lemma:bk1_observer_bounded_emergence_constraint}
Let
\(
O=(N_O,\{\delta^{\,n}_{O}\}_{n=1}^{N_O},\varepsilon_O)
\)
be a bounded observer with resolution kernel \(K_O\) and scalar threshold \(\delta_O\) (Definition~\ref{definition:bk1_bounded_observer}).
For every ordinal \(\lambda<\Omega\), define the stage--composite operator
\[
  E_\lambda := R_\lambda \circ D_\lambda : P_{<\lambda} \longrightarrow P_\lambda,
\]
as defined in Definition~\ref{definition:bk1_stage_composite_operator},
where \(P_{<\lambda}\) and \(P_\lambda\) are symbolic stages introduced in Definition~\ref{definition:bk1_pre_geometric_operators_and_stages}.
Then
\begin{enumerate}
  \item[\textup{(i)}]  \textbf{Bounded approximation of the identity.}\;
        For all \(s\in P_{<\lambda}\),
        \begin{equation}
          \bigl\lVert K_O * \bigl[E_\lambda(s) - s\bigr] \bigr\rVert
          \;\le\; 2\,\delta_O.
        \end{equation}
        (This satisfies the kernel-bounded approximation condition in Definition~\ref{definition:bk1_kernel_based_bounded_symbolic_approximation}.)

  \item[\textup{(ii)}]  \textbf{Cauchy tower under summable decay.}\;
        Endow every \(P_\lambda\) with the observer metric
        \(
          d_O(x,y) := \lVert K_O * (x - y) \rVert.
        \)
        Along any cofinal sequence \((\lambda_n)\) satisfying
        Ax.~\ref{axiom:bk1_summable_resolution_decay}, the transition maps obey
        \[
          d_O(f_{\lambda_m\lambda_n}(x),x)
          \leq \sum_{j=m}^{n-1}\eta_j
          \quad
          \forall\,x \in P_{\lambda_m},\;
          m<n,
        \]
        so the cofinal directed subsystem
        \(
          (P_{\lambda_n}, f_{\lambda_m\lambda_n})_{m<n}
        \)
        is \(d_O\)-Cauchy in the usual tail sense
        (see also the formal directed emergence structure in Definition~\ref{definition:bk1_directed_system_of_emergence}). Its \(d_O\)-completion
        \(
          \overline{P}_O
        \)
        supplies the observer-completed proto-symbolic space associated with
        the colimit \(P=\varinjlim_{\lambda<\Omega}P_\lambda\)
        (Definition~\ref{definition:bk1_proto_symbolic_space}).
\end{enumerate}
\end{lemma}
```

### Bounded Approximation Guarantees Drift Convergence (`proof:bk1_bounded_drift_approximation`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:604`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_summable_resolution_decay` (Summable Resolution Decay); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_stage_composite_operator` (Stage–Composite Operator)
- Cites: `axiom:bk1_summable_resolution_decay` (Summable Resolution Decay); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_stage_composite_operator` (Stage–Composite Operator)
- Cited by: none
- Macros used: none

**Statement / Body**

Because \(D_lambda\) is a bounded symbolic approximation (see Definition definition:bk1_bounded_symbolic_approximation and Definition definition:bk1_pre_geometric_operators_and_stages), we have
\[
 lVert K_O*[D_lambda(s)-s]rVert le delta_O
\]
for all \(sin P_{<lambda}\). Applying \(R_lambda\) and using the boundedness property again (with \(s' := D_lambda(s)\)) gives
\[
 lVert K_O*[R_lambda(D_lambda(s))-D_lambda(s)]rVert le delta_O.
\]
The triangle inequality for the observer norm then yields the overall bound. For \(lambda<mu<Omega\), we have
\[
f_{lambdamu} = E_{mu-1}circdotscirc E_lambda,
\]
where each \(E_lambda\) is the stage-composite operator (Definition definition:bk1_stage_composite_operator) in the successor-indexed case; along a cofinal sequence the same expression is read as composition through the intervening transition maps.

The one-step estimate alone does not give a uniform bound for arbitrary long
composites. Under Ax. axiom:bk1_summable_resolution_decay, however, the
observer-visible displacement of the composite from \(lambda_m\) to
\(lambda_n\) is bounded by the telescoping tail:
\[
d_O(f_{lambda_mlambda_n}(x),x)
leq sum_{j=m}^{n-1}d_O(E_{lambda_j}(x_j),x_j)
leq sum_{j=m}^{n-1}eta_j,
\]
where \(x_j=f_{lambda_mlambda_j}(x)\). Since \(sum_jeta_j<infty\), the
tails \(sum_{j=m}^{infty}eta_j\) tend to zero. Hence the cofinal tower is
Cauchy in \(d_O\), and its observer-completed limit exists in
\(overline{P}_O\).

**Verbatim LaTeX Body**

```latex
\begin{proof}[Bounded Approximation Guarantees Drift Convergence]
\label{proof:bk1_bounded_drift_approximation}
\leavevmode

Because \(D_\lambda\) is a bounded symbolic approximation (see Definition~\ref{definition:bk1_bounded_symbolic_approximation} and Definition~\ref{definition:bk1_pre_geometric_operators_and_stages}), we have
\[
  \lVert K_O*[D_\lambda(s)-s]\rVert \le \delta_O
\]
for all \(s\in P_{<\lambda}\). Applying \(R_\lambda\) and using the boundedness property again (with \(s' := D_\lambda(s)\)) gives
\[
  \lVert K_O*[R_\lambda(D_\lambda(s))-D_\lambda(s)]\rVert \le \delta_O.
\]
The triangle inequality for the observer norm then yields the overall bound. For \(\lambda<\mu<\Omega\), we have
\[
f_{\lambda\mu} = E_{\mu-1}\circ\dots\circ E_\lambda,
\]
where each \(E_\lambda\) is the stage--composite operator (Definition~\ref{definition:bk1_stage_composite_operator}) in the successor-indexed case; along a cofinal sequence the same expression is read as composition through the intervening transition maps.

The one-step estimate alone does not give a uniform bound for arbitrary long
composites. Under Ax.~\ref{axiom:bk1_summable_resolution_decay}, however, the
observer-visible displacement of the composite from \(\lambda_m\) to
\(\lambda_n\) is bounded by the telescoping tail:
\[
d_O(f_{\lambda_m\lambda_n}(x),x)
\leq \sum_{j=m}^{n-1}d_O(E_{\lambda_j}(x_j),x_j)
\leq \sum_{j=m}^{n-1}\eta_j,
\]
where \(x_j=f_{\lambda_m\lambda_j}(x)\). Since \(\sum_j\eta_j<\infty\), the
tails \(\sum_{j=m}^{\infty}\eta_j\) tend to zero. Hence the cofinal tower is
Cauchy in \(d_O\), and its observer-completed limit exists in
\(\overline{P}_O\).
\end{proof}
```

### Emergence Envelope (`scholium:bk1_emergence_envelope`)

Role: `scholium` | Type: `scholium` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:636`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_summable_resolution_decay` (Summable Resolution Decay); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `axiom:bk1_summable_resolution_decay` (Summable Resolution Decay); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cited by: `definition:bk4_refinement_envelope` (Refinement Envelope)
- Macros used: none

**Statement / Body**

To a bounded observer (Def. definition:bk1_bounded_observer), the tower of
emergent symbolic structures (Def. definition:bk1_pre_geometric_operators_and_stages)
unfolds through finite one-step observer envelopes, and along any cofinal tower
satisfying Ax. axiom:bk1_summable_resolution_decay its unresolved tail
shrinks to zero in \(d_O\). Curvature, dimensional refinement, and horizon
bifurcations may still arise, but their observer-visible refinements must become
summably finer for a completed proto-symbolic limit to be available. This
tail-envelope is the geometric shadow of observer-boundedness that guides the
subsequent smoothness construction.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Emergence Envelope]
\label{scholium:bk1_emergence_envelope}
To a bounded observer (Def.~\ref{definition:bk1_bounded_observer}), the tower of
emergent symbolic structures (Def.~\ref{definition:bk1_pre_geometric_operators_and_stages})
unfolds through finite one-step observer envelopes, and along any cofinal tower
satisfying Ax.~\ref{axiom:bk1_summable_resolution_decay} its unresolved tail
shrinks to zero in \(d_O\). Curvature, dimensional refinement, and horizon
bifurcations may still arise, but their observer-visible refinements must become
summably finer for a completed proto-symbolic limit to be available. This
tail-envelope is the geometric shadow of observer-boundedness that guides the
subsequent smoothness construction.
\end{scholium}
```

### Epistemic Humility (`scholium:bk1_epistemic_humility`)

Role: `scholium` | Type: `scholium` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:648`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer)
- Cited by: `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `definition:bk9_symbolic_accountability` (Symbolic Accountability $\mathcal{A}$); `remark:bk8_inference_principle_over_confidence_loss_tradeoff` (Inference Principle Over Confidence-Loss Tradeoff); `scholium:bk4_precision_without_collapse` (Precision Without Collapse); `scholium:bk5_hypotheses_as_adaptive_sym` (Hypotheses as Adaptive Symbolic Manifolds); `scholium:bk8_autonomous_repair_systems_expanded` (Autonomous Repair Systems as Metabolic Projections — An Expanded View); `sec:bk2_foundations_symbolic_thermodynamics` (Foundations of Symbolic Thermodynamics); `subsec:bk7_pisu_revisited_power_uncertainty` (Principium Incertitudinis Symbolicae Universalis (PISU) Revisited)
- Macros used: none

**Statement / Body**

Premise (Observer‑Boundedness).
Every act of cognition is executed by a bounded observer\/ $O=(N_O,{delta^n_O}_{nle N_O},varepsilon_O)$ (Def. definition:bk1_bounded_observer.
Hence all symbolic operators that $O$ can deploy must respect the perceptual threshold
\[
 \|K_Oast[Phi(s)-s]\|levarepsilon_O
 text{for all observable symbols }s.
\]

Principle (Epistemic Humility).
Because $O$ cannot transcend its own resolution kernel $K_O$, any claim about the symbolic manifold $S$ must be
1) provisional,
2) open to differentiation \& reintegration,
3) anchored in knowledge integrity,
4) iteratively refined along a learning path, and
5) stated with full mathematical rigour.
These five clauses instantiate the four core textsc{Giants} axioms:


- Differentiation \& Reintegration — structure updates occur by decomposing $Phi$ into locally bounded moves and re‑synthesising them.

- Knowledge Integrity — updates that breach the boundedness constraint are rejected as incoherent.

- Learning Path Influence — mismatch $Delta=\|Phi(s)-s\|$ feeds back into subsequent operator design, minimising loss $L_{n+1}$ (see FormalMath core equation).

- Mathematical Rigor — all admissible claims are stated as formally verifiable lemmas or energy inequalities.

Lemma (Bounded‑Humility Constraint).
Let $E$ be the set of epistemic commitments formulable by $O$ at symbolic time $t$.
Then the update map $rho_t:EtoE$ generated by any admissible operator $Phi_t$ satisfies
\[
 rho_t(e) = e + underbrace{bigl(Phi_t(e)-ebigr)}_{text{differentiation}}
 text{with}
 \|K_Oastbigl(Phi_t(e)-ebigr)\|levarepsilon_O,
\]
so $rho_t$ is a bounded symbolic approximation (Def. definition:bk1_bounded_observer).
Consequently, epistemic humility is not optional but a necessary condition for reflexive emergence: without it, $Phi_t$ would violate boundedness and fracture the observer’s horizon.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Epistemic Humility]
\label{scholium:bk1_epistemic_humility}
\textbf{Premise (Observer‑Boundedness).}
Every act of cognition is executed by a \emph{bounded observer}\/ $O=(N_O,\{\delta^n_O\}_{n\le N_O},\varepsilon_O)$ (Def.~\ref{definition:bk1_bounded_observer}.
Hence all symbolic operators that $O$ can deploy must respect the perceptual threshold
\[
  \|K_O\ast[\Phi(s)-s]\|\le\varepsilon_O
  \quad\text{for all observable symbols }s.
\]
\medskip
\textbf{Principle (Epistemic Humility).}
Because $O$ \emph{cannot} transcend its own resolution kernel $K_O$, any claim about the symbolic manifold $S$ must be
1) provisional,
2) open to \emph{differentiation \& reintegration},
3) anchored in \emph{knowledge integrity},
4) iteratively refined along a \emph{learning path}, and
5) stated with full \emph{mathematical rigour}.
These five clauses instantiate the four core \textsc{Giants} axioms:
\begin{enumerate}[label=\arabic*.]
  \item \textbf{Differentiation \& Reintegration} — structure updates occur by decomposing $\Phi$ into locally bounded moves and re‑synthesising them.
  \item \textbf{Knowledge Integrity} — updates that breach the boundedness constraint are rejected as incoherent.
  \item \textbf{Learning Path Influence} — mismatch $\Delta=\|\Phi(s)-s\|$ feeds back into subsequent operator design, minimising loss $L_{n+1}$ (see FormalMath core equation).
  \item \textbf{Mathematical Rigor} — all admissible claims are stated as formally verifiable lemmas or energy inequalities.
\end{enumerate}
\medskip
\textbf{Lemma (Bounded‑Humility Constraint).}
Let $\mathcal{E}$ be the set of epistemic commitments formulable by $O$ at symbolic time $t$.
Then the update map $\rho_t:\mathcal{E}\to\mathcal{E}$ generated by any admissible operator $\Phi_t$ satisfies
\[
  \rho_t(e)\;=\;e\;+\;\underbrace{\bigl(\Phi_t(e)-e\bigr)}_{\text{differentiation}}
  \quad\text{with}\quad
  \|K_O\ast\bigl(\Phi_t(e)-e\bigr)\|\le\varepsilon_O,
\]
so $\rho_t$ is a \emph{bounded symbolic approximation} (Def.~\ref{definition:bk1_bounded_observer}).
Consequently, epistemic humility is not optional but a \emph{necessary condition} for reflexive emergence: without it, $\Phi_t$ would violate boundedness and fracture the observer’s horizon.
\end{scholium}
```

### remark:scholium_symbolicum.tex:684 (`remark:scholium_symbolicum.tex:684`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:684`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

This orientation toward epistemic humility prefigures the more formal construct of Symbolic Accountability, where coherence, transparency, and relational viability are operationalized.

**Verbatim LaTeX Body**

```latex
\begin{remark}
    This orientation toward epistemic humility prefigures the more formal construct of \emph{Symbolic Accountability}, where coherence, transparency, and relational viability are operationalized.
\end{remark}
```

### Directed System of Emergence (`definition:bk1_directed_system_of_emergence`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:687`

- Proof status: `definitional`
- Depends on: `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cited by: `definition:bk1_proto_symbolic_space` (Proto-symbolic Space); `lemma:bk1_observer_bounded_emergence_constraint` (Observer–Bounded Emergence Constraint); `lemma:bk1_universality_of_proto_symbolic_space` (Universality of Proto-symbolic Space); `proof:bk1_colimit_yields_categoric_structure` (Colimit Structure Yields Symbolic Cohesion)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-026`
- Witnesses: `ScholiumC.DirectedStageSystem.directed_colimit_universal_property`, `ScholiumC.DirectedStageSystem.injection_transition`
- Countermodels: none
- Formal boundary: A Nat-directed system explicitly records stage carriers, transition maps, and their identity/composition laws; transition images are identified in the colimit and every compatible cocone has a unique mediator.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The directed system ${P_lambda, f_{lambdamu}}_{lambda < mu < Omega}$ consists of:


- Objects: The symbolic structures $P_lambda$ (see Def. definition:bk1_pre_geometric_operators_and_stages).

- Morphisms: $f_{lambdamu}: P_lambda to P_mu$ for $lambda < mu < Omega$, representing structure-preserving evolution.

These satisfy the standard conditions:


- $f_{lambdalambda} = id_{P_lambda}$ (identity).

- $f_{munu} circ f_{lambdamu} = f_{lambdanu}$ for all $lambda < mu < nu < Omega$ (composition).

We require each $f_{lambdamu}$ to be continuous with respect to the topologies on $P_lambda$ and $P_mu$.

Conceptually, each $f_{lambdamu}$ represents the cumulative effect of the interplay between stabilization ($R_nu$) and differentiation ($D_{nu+1}$) for stages $nu$ from $lambda$ to $mu-1$. For instance, $f_{lambda, lambda+1}$ can be thought of as mapping a structure stabilized by $R_lambda$ into the next stage generated via $D_{lambda+1}$. This description is itself a bounded approximation of the complex entanglement of drift and reflection.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Directed System of Emergence]
\label{definition:bk1_directed_system_of_emergence}
The directed system $\{P_\lambda, f_{\lambda\mu}\}_{\lambda < \mu < \Omega}$ consists of:
\begin{itemize}
    \item Objects: The symbolic structures $P_\lambda$ (see Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}).
    \item Morphisms: $f_{\lambda\mu}: P_\lambda \to P_\mu$ for $\lambda < \mu < \Omega$, representing structure-preserving evolution.
\end{itemize}
These satisfy the standard conditions:
\begin{itemize}
    \item $f_{\lambda\lambda} = id_{P_\lambda}$ (identity).
    \item $f_{\mu\nu} \circ f_{\lambda\mu} = f_{\lambda\nu}$ for all $\lambda < \mu < \nu < \Omega$ (composition).
\end{itemize}
We require each $f_{\lambda\mu}$ to be continuous with respect to the topologies on $P_\lambda$ and $P_\mu$.

Conceptually, each $f_{\lambda\mu}$ represents the cumulative effect of the interplay between stabilization ($R_\nu$) and differentiation ($D_{\nu+1}$) for stages $\nu$ from $\lambda$ to $\mu-1$. For instance, $f_{\lambda, \lambda+1}$ can be thought of as mapping a structure stabilized by $R_\lambda$ into the next stage generated via $D_{\lambda+1}$. This description is itself a bounded approximation of the complex entanglement of drift and reflection.
\end{definition}
```

### Proto-symbolic Space (`definition:bk1_proto_symbolic_space`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:703`

- Proof status: `definitional`
- Depends on: `definition:bk1_directed_system_of_emergence` (Directed System of Emergence); `definition:bk1_let_cats_be_the_category` (Category of Structures); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `definition:bk1_directed_system_of_emergence` (Directed System of Emergence); `definition:bk1_let_cats_be_the_category` (Category of Structures); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cited by: `axiom:bk1_local_charitability` (Local Chartability); `axiom:bk1_smooth_convergence` (Smooth Convergence); `axiom:bk1_topological_regularity` (Topological Regularity); `lemma:bk1_observer_bounded_emergence_constraint` (Observer–Bounded Emergence Constraint); `lemma:bk1_universality_of_proto_symbolic_space` (Universality of Proto-symbolic Space); `proof:bk1_sketch_limit_stabilization_colimit` (Limit of Stabilization Operators via Colimit); `proposition:bk4_ttpr_convergence` (Convergence of Recursive Refinement); `subsec:appD_category_theory_core_resonance` (D.9.1 Core Resonance); `theorem:bk1_manifold_emergence` (Manifold Emergence)
- Macros used: `\catS`

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-024`
- Witnesses: `ScholiumC.DirectedStageSystem.directed_colimit_universal_property`, `ScholiumC.colimit_universal_property`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: The proto-symbolic carrier is now the quotient of the coproduct of a concrete Nat-directed stage tower by eventual compatibility; genuinely ordinal indexing and the source category catS remain abstracted.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The proto-symbolic space $P$ is defined as the colimit in the category $catS$ (see Def. definition:bk1_let_cats_be_the_category):
\[
P := varinjlim_{lambda < Omega} P_lambda
\]
Elements of $P$ are equivalence classes $[(x_lambda)]$ where $x_lambda in P_lambda$, under the relation $x_lambda sim x_mu$ if there exists $nu geq lambda, mu$ such that $f_{lambdanu}(x_lambda) = f_{munu}(x_mu)$ (cf. Def. definition:bk1_directed_system_of_emergence). The topology on $P$ is the final topology making all canonical injections $i_lambda: P_lambda to P$ continuous (see also Def. definition:bk1_pre_geometric_operators_and_stages).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Proto-symbolic Space]
\label{definition:bk1_proto_symbolic_space}
The proto-symbolic space $P$ is defined as the colimit in the category $\catS$ (see Def.~\ref{definition:bk1_let_cats_be_the_category}):
\[
P := \varinjlim_{\lambda < \Omega} P_\lambda
\]
Elements of $P$ are equivalence classes $[(x_\lambda)]$ where $x_\lambda \in P_\lambda$, under the relation $x_\lambda \sim x_\mu$ if there exists $\nu \geq \lambda, \mu$ such that $f_{\lambda\nu}(x_\lambda) = f_{\mu\nu}(x_\mu)$ (cf.~Def.~\ref{definition:bk1_directed_system_of_emergence}). The topology on $P$ is the final topology making all canonical injections $i_\lambda: P_\lambda \to P$ continuous (see also Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}).
\end{definition}
```

### Universality of Proto-symbolic Space (`lemma:bk1_universality_of_proto_symbolic_space`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:711`

- Proof status: `proven`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `definition:bk1_directed_system_of_emergence` (Directed System of Emergence); `definition:bk1_let_cats_be_the_category` (Category of Structures); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cites: `definition:bk1_directed_system_of_emergence` (Directed System of Emergence); `definition:bk1_let_cats_be_the_category` (Category of Structures); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cited by: none
- Macros used: `\catS`

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-025`
- Witnesses: `ScholiumC.DirectedStageSystem.directed_colimit_universal_property`, `ScholiumC.colimit_universal_property`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: Existence and uniqueness of the mediating morphism is proved both for a general quotient and for cocones over an explicit Nat-directed diagram with lawful transition maps; ordinal indexing and catS remain abstracted.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The proto-symbolic space $P$ satisfies the universal property of colimits in $catS$ (see Def. definition:bk1_let_cats_be_the_category): for any object $Q in Ob(catS)$ and compatible family of morphisms ${g_lambda: P_lambda to Q}_{lambda < Omega}$ (i.e., $g_mu circ f_{lambdamu} = g_lambda$ for $lambda < mu$, per Def. definition:bk1_directed_system_of_emergence), there exists a unique morphism $g: P to Q$ such that $g circ i_lambda = g_lambda$ for all $lambda < Omega$ (cf. Def. definition:bk1_proto_symbolic_space, Def. definition:bk1_pre_geometric_operators_and_stages).

Given Axiom axiom:bk1_axiomata_prima, the stagewise symbolic structures are generated through non-trivial drift and require coherent stabilization across levels (cf. Def. definition:bk1_pre_geometric_operators_and_stages, Def. definition:bk1_directed_system_of_emergence). Under cocompleteness of $catS$, the colimit definition then yields the unique mediating morphism and hence symbolic cohesion.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Universality of Proto-symbolic Space]
\label{lemma:bk1_universality_of_proto_symbolic_space}
The proto-symbolic space $P$ satisfies the universal property of colimits in $\catS$ (see Def.~\ref{definition:bk1_let_cats_be_the_category}): for any object $Q \in Ob(\catS)$ and compatible family of morphisms $\{g_\lambda: P_\lambda \to Q\}_{\lambda < \Omega}$ (i.e., $g_\mu \circ f_{\lambda\mu} = g_\lambda$ for $\lambda < \mu$, per Def.~\ref{definition:bk1_directed_system_of_emergence}), there exists a unique morphism $g: P \to Q$ such that $g \circ i_\lambda = g_\lambda$ for all $\lambda < \Omega$ (cf.~Def.~\ref{definition:bk1_proto_symbolic_space}, Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}).
\begin{proof}[Colimit Structure Yields Symbolic Cohesion]
\label{proof:bk1_colimit_yields_categoric_structure}
\leavevmode

Given Axiom~\ref{axiom:bk1_axiomata_prima}, the stagewise symbolic structures are generated through non-trivial drift and require coherent stabilization across levels (cf.~Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}, Def.~\ref{definition:bk1_directed_system_of_emergence}). Under cocompleteness of $\catS$, the colimit definition then yields the unique mediating morphism and hence symbolic cohesion.
\end{proof}
\end{lemma}
```

### Colimit Structure Yields Symbolic Cohesion (`proof:bk1_colimit_yields_categoric_structure`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:714`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `definition:bk1_directed_system_of_emergence` (Directed System of Emergence); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin); `definition:bk1_directed_system_of_emergence` (Directed System of Emergence); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cited by: `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Macros used: `\catS`

**Statement / Body**

Given Axiom axiom:bk1_axiomata_prima, the stagewise symbolic structures are generated through non-trivial drift and require coherent stabilization across levels (cf. Def. definition:bk1_pre_geometric_operators_and_stages, Def. definition:bk1_directed_system_of_emergence). Under cocompleteness of $catS$, the colimit definition then yields the unique mediating morphism and hence symbolic cohesion.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Colimit Structure Yields Symbolic Cohesion]
\label{proof:bk1_colimit_yields_categoric_structure}
\leavevmode

Given Axiom~\ref{axiom:bk1_axiomata_prima}, the stagewise symbolic structures are generated through non-trivial drift and require coherent stabilization across levels (cf.~Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}, Def.~\ref{definition:bk1_directed_system_of_emergence}). Under cocompleteness of $\catS$, the colimit definition then yields the unique mediating morphism and hence symbolic cohesion.
\end{proof}
```

### Proof by Elimination: Necessity of the Dual Horizon Structure (`subsec:bk1_necessity_of_the_dual_horizon_structure`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:721`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Effective Horizon Signature (`definition:bk1_effective_horizon_signature`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:724`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor)
- Cited by: `definition:bk1_bounded_reflexive_emergence` (Bounded Reflexive Emergence); `proof:bk1_horizon_characterization` (Effective Signature Separates the Horizon Roles); `proof:bk1_proof_of_dual_horizon_necessity_theorem` (Proof of Dual Horizon Necessity Theorem); `proof:bk4_wheel_refines_signature` (Quadrant quotient of the phase circle); `proposition:bk4_wheel_refines_signature` (The wheel refines the effective horizon signature)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-028`
- Witnesses: `ScholiumC.effectiveSignature_empty`, `ScholiumC.effectiveSignature_full`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: Modeled on a single generative/dissipative flux pair (G, C) rather than existential quantification over multiple horizon components; the integral definitions of G_O, C_O themselves are not modeled, only the resulting sign predicate.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $U$ be a symbolic universe sustaining a bounded observer
\(O\) on a nonempty observer domain \(Omega_{O}\)
(Def. definition:bk1_bounded_observer). For any horizon component
\(H\) meeting \(Omega_{O}\), define its observer-visible curvature
fluxes by
\[
G_{O}(H)
 :=int_{HcapOmega_{O}}max(kappa,0) dsigma,

C_{O}(H)
 :=int_{HcapOmega_{O}}max(-kappa,0) dsigma,
\]
where \(kappa\) is symbolic curvature
(Def. definition:bk1_symbolic_riemann_tensor) and \(dsigma\) is the
induced horizon measure. The effective horizon signature is
\[
Sigma_{O}(U)
subseteq {+,-},
\]
with \(+inSigma_{O}(U)\) iff some horizon component has
\(G_{O}(H)>0\), and
\(-inSigma_{O}(U)\) iff some horizon component has
\(C_{O}(H)>0\). Multiple horizons and sign-changing horizons are
therefore represented by their effective observer-visible sign content.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Effective Horizon Signature]
\label{definition:bk1_effective_horizon_signature}
Let $\mathcal{U}$ be a symbolic universe sustaining a bounded observer
\(\mathcal{O}\) on a nonempty observer domain \(\Omega_{\mathcal{O}}\)
(Def.~\ref{definition:bk1_bounded_observer}). For any horizon component
\(H\) meeting \(\Omega_{\mathcal{O}}\), define its observer-visible curvature
fluxes by
\[
G_{\mathcal{O}}(H)
  :=\int_{H\cap\Omega_{\mathcal{O}}}\max(\kappa,0)\,d\sigma,
\qquad
C_{\mathcal{O}}(H)
  :=\int_{H\cap\Omega_{\mathcal{O}}}\max(-\kappa,0)\,d\sigma,
\]
where \(\kappa\) is symbolic curvature
(Def.~\ref{definition:bk1_symbolic_riemann_tensor}) and \(d\sigma\) is the
induced horizon measure. The effective horizon signature is
\[
\Sigma_{\mathcal{O}}(\mathcal{U})
\subseteq \{+,-\},
\]
with \(+\in\Sigma_{\mathcal{O}}(\mathcal{U})\) iff some horizon component has
\(G_{\mathcal{O}}(H)>0\), and
\(-\in\Sigma_{\mathcal{O}}(\mathcal{U})\) iff some horizon component has
\(C_{\mathcal{O}}(H)>0\). Multiple horizons and sign-changing horizons are
therefore represented by their effective observer-visible sign content.
\end{definition}
```

### Bounded Reflexive Emergence (`definition:bk1_bounded_reflexive_emergence`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:752`

- Proof status: `definitional`
- Depends on: `definition:bk1_effective_horizon_signature` (Effective Horizon Signature); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cites: `corollary:bk1_fixed_point` (Reflective Fixed Locus); `definition:bk1_effective_horizon_signature` (Effective Horizon Signature); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: `proof:bk1_proof_of_dual_horizon_necessity_theorem` (Proof of Dual Horizon Necessity Theorem); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Macros used: `\freeenergy`

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-030`
- Witnesses: `ScholiumC.dualHorizonBinding_both_pos`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: Only the 'binding special case' clause (Delta Phi_O = G_O(H_G) C_O(H_D)) is modeled as a scalar product-threshold fact; the general observer-resolved free-energy criterion is not.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A symbolic universe \(U\) supports bounded reflexive emergence
for \(O\) when, over some interval of symbolic time on the observer
domain \(Omega_{O}\), the observer-visible emergence functional
\[
DeltaPhi_{O}(D,R_{stab}) ge tau_E > 0,
\]
where \(DeltaPhi_{O}\) measures the net retained, observer-resolved
coherent structure produced by the coupled action of novelty-generating drift
\(D\) and stabilizing reflection \(R_{stab}\) - equivalently, the
stabilized reduction of symbolic free energy \(freeenergy\)
(Def. definition:bk2_symbolic_free_energy;
Cor. corollary:bk1_fixed_point) that the observer can both register
and keep. The criterion is stated independently of any horizon geometry:
that both a generative and a stabilizing channel are present is the
conclusion of Thm. theorem:bk1_dual_horizon_necessity_theorem, not a
premise, and the product \(G_{O}(H_G) C_{O}(H_D)\) of
Def. definition:bk1_effective_horizon_signature is the binding
special case in which the two fluxes are read off a single
generative/dissipative pair.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Bounded Reflexive Emergence]
\label{definition:bk1_bounded_reflexive_emergence}
A symbolic universe \(\mathcal{U}\) supports \emph{bounded reflexive emergence}
for \(\mathcal{O}\) when, over some interval of symbolic time on the observer
domain \(\Omega_{\mathcal{O}}\), the observer-visible emergence functional
\[
\Delta\Phi_{\mathcal{O}}(D,R_{\mathrm{stab}}) \;\ge\; \tau_E \;>\; 0,
\]
where \(\Delta\Phi_{\mathcal{O}}\) measures the net retained, observer-resolved
coherent structure produced by the coupled action of novelty-generating drift
\(D\) and stabilizing reflection \(R_{\mathrm{stab}}\) --- equivalently, the
stabilized reduction of symbolic free energy \(\freeenergy\)
(Def.~\ref{definition:bk2_symbolic_free_energy};
Cor.~\ref{corollary:bk1_fixed_point}) that the observer can both \emph{register}
and \emph{keep}. The criterion is stated independently of any horizon geometry:
that both a generative and a stabilizing channel are present is the
\emph{conclusion} of Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem}, not a
premise, and the product \(G_{\mathcal{O}}(H_G)\,C_{\mathcal{O}}(H_D)\) of
Def.~\ref{definition:bk1_effective_horizon_signature} is the \emph{binding}
special case in which the two fluxes are read off a single
generative/dissipative pair.
\end{definition}
```

### Dual Horizon Necessity Theorem (`theorem:bk1_dual_horizon_necessity_theorem`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:775`

- Proof status: `proven`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_bounded_reflexive_emergence` (Bounded Reflexive Emergence); `definition:bk1_effective_horizon_signature` (Effective Horizon Signature); `proof:bk1_colimit_yields_categoric_structure` (Colimit Structure Yields Symbolic Cohesion)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_bounded_reflexive_emergence` (Bounded Reflexive Emergence); `proof:bk1_colimit_yields_categoric_structure` (Colimit Structure Yields Symbolic Cohesion); `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Cited by: `axiom:bk1_dual_horizon_postulate` (Dual Horizon Postulate); `corollary:bk1_event_horizon_identity_field` (Event Horizon Identity Field); `corollary:bk1_horizon_duality_principle` (Horizon Duality Principle); `definition:bk1_bounded_reflexive_emergence` (Bounded Reflexive Emergence); `definition:bk1_horizon_crossing_operation` (Horizon-Crossing Operation); `lemma:bk1_horizon_characterization` (Horizon Characterization); `proof:bk1_dual_horizon_unification_principle` (Projection Through the Dual Horizon Signature); `proof:bk1_event_horizon_identity_field` (Identity Field on the Symbolized Causal Patch); `proof:bk1_horizon_characterization` (Effective Signature Separates the Horizon Roles); `proof:bk1_horizon_duality_principle` (Dual Signature Is Minimal for Reflexive Emergence); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `scholium:bk1_cosmogenesis_proof_status` (Proof status of Cosmogenesis); `sec:appC_dual_horizon` (Dual Horizon – A Formal Proof by Elimination); `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature)); `theorem:bk1_dual_horizon_cosmogenesis` (Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos}); `theorem:bk1_dual_horizon_unification_principle` (Emergent Dual Horizon Unification Principle); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-029`
- Witnesses: `ScholiumC.dualHorizonBinding_both_pos`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: Only the converse/binding, coupled-case direction is modeled (product of fluxes above threshold forces both signs present); the necessity direction and the general (non-binding) case are not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $U$ be a symbolic universe sustaining bounded observers within a
domain $Omega_{O}$ (cf. Def. definition:bk1_bounded_observer),
whose stagewise structures cohere into a categorical colimit
(cf. Proof proof:bk1_colimit_yields_categoric_structure). If \(U\)
supports bounded reflexive emergence for \(O\)
(Def. definition:bk1_bounded_reflexive_emergence), then it possesses an
effective dual horizon structure on a shared bounded domain,
\[
Sigma_{O}(U)={+,-}:
 G_{O}(H_G)>0 \ text{and}\ C_{O}(H_D)>0,
\]
i.e.\ at least one observer-visible positive-curvature novelty channel and one negative-curvature stabilization channel meeting a common
\(Omega_{O}\). Conversely, when both channels are present on a shared
domain and their fluxes couple above the observer threshold,
\(DeltaPhi_{O}(D,R_{stab})getau_E\) and emergence follows.
The necessity direction is unconditional; the converse is the binding, coupled
case. The expanded two-modality derivation - with its realization-invariance
across multiple and sign-changing horizons and the explicit coupling premise on
which the converse rests - is given in Appendix C
(Thm. theorem:appC_dual_horizon_signature), which defers to this theorem
for the canonical formal statement.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Dual Horizon Necessity Theorem]
\label{theorem:bk1_dual_horizon_necessity_theorem}
Let $\mathcal{U}$ be a symbolic universe sustaining bounded observers within a
domain $\Omega_{\mathcal{O}}$ (cf.~Def.~\ref{definition:bk1_bounded_observer}),
whose stagewise structures cohere into a categorical colimit
(cf.~Proof~\ref{proof:bk1_colimit_yields_categoric_structure}). If \(\mathcal{U}\)
supports bounded reflexive emergence for \(\mathcal{O}\)
(Def.~\ref{definition:bk1_bounded_reflexive_emergence}), then it possesses an
effective dual horizon structure on a shared bounded domain,
\[
\Sigma_{\mathcal{O}}(\mathcal{U})=\{+,-\}:
\qquad G_{\mathcal{O}}(H_G)>0 \ \text{and}\ C_{\mathcal{O}}(H_D)>0,
\]
i.e.\ at least one observer-visible positive-curvature novelty channel and one negative-curvature stabilization channel meeting a common
\(\Omega_{\mathcal{O}}\). Conversely, when both channels are present on a shared
domain and their fluxes couple above the observer threshold,
\(\Delta\Phi_{\mathcal{O}}(D,R_{\mathrm{stab}})\ge\tau_E\) and emergence follows.
The necessity direction is unconditional; the converse is the binding, coupled
case. The expanded two-modality derivation --- with its realization-invariance
across multiple and sign-changing horizons and the explicit coupling premise on
which the converse rests --- is given in Appendix~C
(Thm.~\ref{theorem:appC_dual_horizon_signature}), which defers to this theorem
for the canonical formal statement.
\end{theorem}
```

### Proof of Dual Horizon Necessity Theorem (`proof:bk1_proof_of_dual_horizon_necessity_theorem`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:800`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_reflexive_emergence` (Bounded Reflexive Emergence); `definition:bk1_effective_horizon_signature` (Effective Horizon Signature)
- Cites: `corollary:bk1_fixed_point` (Reflective Fixed Locus); `definition:bk1_bounded_reflexive_emergence` (Bounded Reflexive Emergence); `definition:bk1_drift_field` (Drift Field); `definition:bk1_effective_horizon_signature` (Effective Horizon Signature); `definition:bk1_reflection_operator` (Reflection Operator); `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Cited by: `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity)
- Macros used: none

**Statement / Body**

Necessity (by observational elimination).
Assume \(U\) supports bounded reflexive emergence: over some interval
the bounded observer registers and retains new coherent structure on
\(Omega_{O}\), \(DeltaPhi_{O}getau_E>0\)
(Def. definition:bk1_bounded_reflexive_emergence). We eliminate the three
ways the dual signature could fail.
No generative flux - \(G_{O}(H)=0\) for every horizon visible
to \(O\): no observer-visible novelty crosses into
\(Omega_{O}\), so over the interval nothing new is registered
(only transport below resolution, repetition, or decay), and retained new
structure cannot reach \(tau_E\) - one cannot keep what was never observed to
enter.
No stabilizing flux - \(C_{O}(H)=0\): novelty may be sourced
but nothing contracts or integrates it, so symbolic free energy is not stably
reduced and the differentiated content disperses before it can register as
retained identity (Cor. corollary:bk1_fixed_point); novelty seen but not
kept is not emergence.
No shared domain - a generative and a stabilizing channel exist but
their observer-visible supports do not both meet a common \(Omega_{O}\):
then on the single domain over which \(O\) integrates emergence one
channel is absent, returning us to the previous two cases.
In each case \(DeltaPhi_{O}<tau_E\), contradicting the hypothesis.
Hence \(G_{O}(H_G)>0\) and \(C_{O}(H_D)>0\) on a shared
\(Omega_{O}\), i.e.\ \(Sigma_{O}(U)={+,-}\)
(Def. definition:bk1_effective_horizon_signature). A constant nonzero drift
field does not evade this: without positive horizon flux paired with negative
stabilization flux on the shared domain it supplies transport, not bounded
reflexive emergence.

Converse (the binding, coupled case).
If both channels are present on a shared \(Omega_{O}\) and their fluxes
couple above threshold, the positive flux supplies novelty through drift \(D\)
(Def. definition:bk1_drift_field) and the negative flux supplies state-level
closure through \(R_{stab}\) (Def. definition:bk1_reflection_operator;
Cor. corollary:bk1_fixed_point); their coupled action realizes
\(DeltaPhi_{O}getau_E\), so \(U\) supports bounded
reflexive emergence. This converse rests on the coupling of the two fluxes, not on
their mere coexistence; the explicit coupling premise, together with the geometric
modality of the necessity argument and its invariance across multiple and
sign-changing horizon realizations, is developed in Appendix C
(Thm. theorem:appC_dual_horizon_signature).

**Verbatim LaTeX Body**

```latex
\begin{proof}[Proof of Dual Horizon Necessity Theorem]
\label{proof:bk1_proof_of_dual_horizon_necessity_theorem}
\leavevmode

\textbf{Necessity (by observational elimination).}
Assume \(\mathcal{U}\) supports bounded reflexive emergence: over some interval
the bounded observer registers \emph{and retains} new coherent structure on
\(\Omega_{\mathcal{O}}\), \(\Delta\Phi_{\mathcal{O}}\ge\tau_E>0\)
(Def.~\ref{definition:bk1_bounded_reflexive_emergence}). We eliminate the three
ways the dual signature could fail.
\emph{No generative flux} --- \(G_{\mathcal{O}}(H)=0\) for every horizon visible
to \(\mathcal{O}\): no observer-visible novelty crosses into
\(\Omega_{\mathcal{O}}\), so over the interval nothing \emph{new} is registered
(only transport below resolution, repetition, or decay), and retained new
structure cannot reach \(\tau_E\) --- one cannot keep what was never observed to
enter.
\emph{No stabilizing flux} --- \(C_{\mathcal{O}}(H)=0\): novelty may be sourced
but nothing contracts or integrates it, so symbolic free energy is not stably
reduced and the differentiated content disperses before it can register as
retained identity (Cor.~\ref{corollary:bk1_fixed_point}); novelty seen but not
kept is not emergence.
\emph{No shared domain} --- a generative and a stabilizing channel exist but
their observer-visible supports do not both meet a common \(\Omega_{\mathcal{O}}\):
then on the single domain over which \(\mathcal{O}\) integrates emergence one
channel is absent, returning us to the previous two cases.
In each case \(\Delta\Phi_{\mathcal{O}}<\tau_E\), contradicting the hypothesis.
Hence \(G_{\mathcal{O}}(H_G)>0\) and \(C_{\mathcal{O}}(H_D)>0\) on a shared
\(\Omega_{\mathcal{O}}\), i.e.\ \(\Sigma_{\mathcal{O}}(\mathcal{U})=\{+,-\}\)
(Def.~\ref{definition:bk1_effective_horizon_signature}). A constant nonzero drift
field does not evade this: without positive horizon flux paired with negative
stabilization flux on the shared domain it supplies transport, not bounded
reflexive emergence.

\textbf{Converse (the binding, coupled case).}
If both channels are present on a shared \(\Omega_{\mathcal{O}}\) and their fluxes
couple above threshold, the positive flux supplies novelty through drift \(D\)
(Def.~\ref{definition:bk1_drift_field}) and the negative flux supplies state-level
closure through \(R_{\mathrm{stab}}\) (Def.~\ref{definition:bk1_reflection_operator};
Cor.~\ref{corollary:bk1_fixed_point}); their coupled action realizes
\(\Delta\Phi_{\mathcal{O}}\ge\tau_E\), so \(\mathcal{U}\) supports bounded
reflexive emergence. This converse rests on the coupling of the two fluxes, not on
their mere coexistence; the explicit coupling premise, together with the geometric
modality of the necessity argument and its invariance across multiple and
sign-changing horizon realizations, is developed in Appendix~C
(Thm.~\ref{theorem:appC_dual_horizon_signature}).
\end{proof}
```

### Horizon Characterization (`lemma:bk1_horizon_characterization`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:847`

- Proof status: `proven`
- Depends on: `definition:bk1_effective_horizon_signature` (Effective Horizon Signature); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: `proof:bk1_horizon_duality_principle` (Dual Signature Is Minimal for Reflexive Emergence); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-031`
- Witnesses: `ScholiumC.dualHorizonBinding_both_pos`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: Only clause 2's stabilization-flux conclusion (C_O(H_D) > 0) is captured, via the shared binding-product fact; clause 1's divergence condition nabla.D > 0 and clause 3's containment-domain definition are not modeled (require manifold divergence).

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The generative horizon $H_G$ and dissipative horizon $H_D$ exhibit distinct, complementary properties fundamental to symbolic dynamics:


- $H_G$ is associated with generative symbolic drift, represented by a field $D$ (cf. Def. definition:bk1_drift_field), such that locally $nabla cdot D > 0$ (positive divergence, signifying expansion in possibility space).

- $H_D$ is associated with constraining symbolic stabilization, represented by the state-level component \(R_{stab}\) (cf. Def. definition:bk1_reflection_operator), such that observer-visible negative curvature supplies positive stabilization flux \(C_{O}(H_D)>0\).

- Together, they define the bounded observer domain $Omega = {x in U : H_G prec x prec H_D}$, where $prec$ denotes symbolic containment relative to the horizons, establishing the stage for emergence (cf. Thm. theorem:bk1_dual_horizon_necessity_theorem, Def. definition:bk1_symbolic_manifold).

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Horizon Characterization]
\label{lemma:bk1_horizon_characterization}
The generative horizon $H_G$ and dissipative horizon $H_D$ exhibit distinct, complementary properties fundamental to symbolic dynamics:
\begin{enumerate}
  \item $H_G$ is associated with generative symbolic drift, represented by a field $D$ (cf.~Def.~\ref{definition:bk1_drift_field}), such that locally $\nabla \cdot D > 0$ (positive divergence, signifying expansion in possibility space).
  \item $H_D$ is associated with constraining symbolic stabilization, represented by the state-level component \(R_{\mathrm{stab}}\) (cf.~Def.~\ref{definition:bk1_reflection_operator}), such that observer-visible negative curvature supplies positive stabilization flux \(C_{\mathcal{O}}(H_D)>0\).
  \item Together, they define the bounded observer domain $\Omega = \{x \in \mathcal{U} : H_G \prec x \prec H_D\}$, where $\prec$ denotes symbolic containment relative to the horizons, establishing the stage for emergence (cf.~Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem}, Def.~\ref{definition:bk1_symbolic_manifold}).
\end{enumerate}
\end{lemma}
```

### Effective Signature Separates the Horizon Roles (`proof:bk1_horizon_characterization`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:856`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_effective_horizon_signature` (Effective Horizon Signature); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_effective_horizon_signature` (Effective Horizon Signature); `definition:bk1_reflection_operator` (Reflection Operator); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: none
- Macros used: none

**Statement / Body**

By Def. definition:bk1_effective_horizon_signature, a horizon component
with \(G_{O}(H)>0\) contributes the positive observer-visible sign,
while a component with \(C_{O}(H)>0\) contributes the negative
observer-visible sign. Thm. theorem:bk1_dual_horizon_necessity_theorem
states that bounded reflexive emergence forces the joint signature
\(Sigma_{O}(U)={+,-}\) on a shared bounded domain.
The positive component is exactly the generative channel carried by drift \(D\)
(Def. definition:bk1_drift_field); locally this is the expansion condition
recorded as positive divergence. The negative component is exactly the
stabilizing channel carried by the state-level reflection
\(R_{stab}\) (Def. definition:bk1_reflection_operator), recorded
as positive stabilizing flux. Their shared support is the observer domain
\(Omega_{O}\), which is equivalently the region symbolically
contained between the two effective horizons.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Effective Signature Separates the Horizon Roles]
\label{proof:bk1_horizon_characterization}
\leavevmode

By Def.~\ref{definition:bk1_effective_horizon_signature}, a horizon component
with \(G_{\mathcal{O}}(H)>0\) contributes the positive observer-visible sign,
while a component with \(C_{\mathcal{O}}(H)>0\) contributes the negative
observer-visible sign. Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem}
states that bounded reflexive emergence forces the joint signature
\(\Sigma_{\mathcal{O}}(\mathcal{U})=\{+,-\}\) on a shared bounded domain.
The positive component is exactly the generative channel carried by drift \(D\)
(Def.~\ref{definition:bk1_drift_field}); locally this is the expansion condition
recorded as positive divergence. The negative component is exactly the
stabilizing channel carried by the state-level reflection
\(R_{\mathrm{stab}}\) (Def.~\ref{definition:bk1_reflection_operator}), recorded
as positive stabilizing flux. Their shared support is the observer domain
\(\Omega_{\mathcal{O}}\), which is equivalently the region symbolically
contained between the two effective horizons.
\end{proof}
```

### Horizon Duality Principle (`corollary:bk1_horizon_duality_principle`)

Role: `corollary` | Type: `corollary` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:875`

- Proof status: `proven`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `lemma:bk1_horizon_characterization` (Horizon Characterization); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: `scholium:bk1_curvature_flux_kin_kout`
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-032`
- Witnesses: `ScholiumC.dualHorizonBinding_both_pos`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: The 'opposing horizon principles both present' conclusion is captured by the same binding-product fact; the elimination-argument narrative and 'no simpler configuration' claim are not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

By Axiom axiom:bk1_axiomata_prima and the elimination argument in Thm. theorem:bk1_dual_horizon_necessity_theorem, reflexive emergence is necessarily situated within the dynamic tension field generated by opposing horizon principles. No simpler configuration can sustain the requisite symbolic complexity and coherence for bounded self-observation.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Horizon Duality Principle]
\label{corollary:bk1_horizon_duality_principle}
By Axiom~\ref{axiom:bk1_axiomata_prima} and the elimination argument in Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem}, reflexive emergence is necessarily situated within the dynamic tension field generated by opposing horizon principles. No simpler configuration can sustain the requisite symbolic complexity and coherence for bounded self-observation.
\end{corollary}
```

### Dual Signature Is Minimal for Reflexive Emergence (`proof:bk1_horizon_duality_principle`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:879`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `lemma:bk1_horizon_characterization` (Horizon Characterization); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin); `lemma:bk1_horizon_characterization` (Horizon Characterization); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: none
- Macros used: none

**Statement / Body**

Thm. theorem:bk1_dual_horizon_necessity_theorem proves by elimination
that bounded reflexive emergence cannot persist when the generative sign is
absent, when the stabilizing sign is absent, or when the two signs fail to meet
on a shared observer-visible domain. Lem. lemma:bk1_horizon_characterization
identifies these two signs with the opposing horizon roles \(H_G\) and \(H_D\).
Thus any configuration with fewer than the two effective horizon principles
lacks either novelty, retention, or their shared bounded field of coupling.
By Ax. axiom:bk1_axiomata_prima, emergence cannot be reduced to a static
being beneath these operations; it must occur in the tension generated by the
opposed, coupled horizons.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Dual Signature Is Minimal for Reflexive Emergence]
\label{proof:bk1_horizon_duality_principle}
\leavevmode

Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem} proves by elimination
that bounded reflexive emergence cannot persist when the generative sign is
absent, when the stabilizing sign is absent, or when the two signs fail to meet
on a shared observer-visible domain. Lem.~\ref{lemma:bk1_horizon_characterization}
identifies these two signs with the opposing horizon roles \(H_G\) and \(H_D\).
Thus any configuration with fewer than the two effective horizon principles
lacks either novelty, retention, or their shared bounded field of coupling.
By Ax.~\ref{axiom:bk1_axiomata_prima}, emergence cannot be reduced to a static
being beneath these operations; it must occur in the tension generated by the
opposed, coupled horizons.
\end{proof}
```

### scholium:bk1_curvature_flux_kin_kout (`scholium:bk1_curvature_flux_kin_kout`)

Role: `scholium` | Type: `scholium` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:898`

- Proof status: `not_applicable`
- Depends on: `corollary:bk1_horizon_duality_principle` (Horizon Duality Principle); `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `corollary:bk1_horizon_duality_principle` (Horizon Duality Principle); `definition:bk1_bounded_observer` (Bounded Observer)
- Cited by: `scholium:bk1_constitutive_reflex` (The Constitutive Reflex)
- Macros used: none

**Statement / Body**

{Symbolic Curvature Flux Across Horizons}

Let $O$ be a bounded observer (Def. definition:bk1_bounded_observer) embedded in symbolic manifold $M$, with inner horizon $H_{text{in}}$ and outer horizon $H_{text{out}}$ defining its receptive and projective limits (cf. Cor. corollary:bk1_horizon_duality_principle). Define the symbolic curvature flux quantities:

k_{text{in}}(O) := int_{H_{text{in}}} K(s) d s \\
k_{text{out}}(O) := int_{H_{text{out}}} K(s) d s \\
Q_{text{sym}}(O) := k_{text{out}} - k_{text{in}}

where $K(s)$ denotes symbolic curvature density over symbol stream $s in Gamma(M)$.

Cross-Field Interpretation Framework:

- quant-ph:


- $k_{text{in}}$: Quantum information crossing event horizon (Hawking radiation analogue for information)

- $k_{text{out}}$: Coherent quantum state emission from observer's measurement apparatus

- $Q_{text{sym}}$: Net entanglement-entropy change from observer work on the quantum system

- Connects to: Black hole thermodynamics, quantum error correction, measurement-induced phase transitions


- math-ph:


- $k_{text{in}}$: Curvature flux through inward-pointing normal vectors on boundary manifold

- $k_{text{out}}$: Divergence of geometric flow—Ricci curvature evolution across observer's worldline

- $Q_{text{sym}}$: Net geometric work analogous to Einstein-Hilbert action variation

- Connects to: Ricci flow, minimal surface theory, geometric measure theory, AdS/CFT correspondence


- hep-th:


- $k_{text{in}}$: Bulk-to-boundary information flow in holographic duality

- $k_{text{out}}$: Boundary conformal field theory correlators encoding bulk physics

- $Q_{text{sym}}$: Holographic entanglement entropy—measure of bulk reconstruction fidelity

- Connects to: Holographic principle, ER=EPR, quantum error correction codes, tensor networks


- cs.LG:


- $k_{text{in}}$: Information-bottleneck compression preserving task-relevant structure

- $k_{text{out}}$: Generated predictions/outputs with measurable semantic coherence

- $Q_{text{sym}}$: Learning signal—net information gain enabling generalization beyond training distribution

- Connects to: Variational autoencoders, mutual information neural estimation, meta-learning, transformer attention flow


- cond-mat.stat-mech:


- $k_{text{in}}$: Microscopic fluctuation flux into coarse-grained observable

- $k_{text{out}}$: Emergent order parameter or collective mode amplitude

- $Q_{text{sym}}$: Free energy change driving phase transitions—thermodynamic work at criticality

- Connects to: Renormalization group fixed points, spontaneous symmetry breaking, finite-size scaling, quantum phase transitions


Unified Mathematical Structure:
The flux equations encode a fundamental duality across all fields:

text{Information} leftrightarrow text{Geometry} & text{(quant-ph} leftrightarrow text{math-ph)} \\
text{Holography} leftrightarrow text{Learning} & text{(hep-th} leftrightarrow text{cs.LG)} \\
text{Emergence} leftrightarrow text{Criticality} & text{(all fields} rightarrow text{cond-mat.stat-mech)}

Dual Horizon Universe Operationalization:
Our philosophical proof by elimination establishes that any bounded observer necessarily exhibits dual horizons. Computationally, this enables:

- Quantum-Inspired Architectures: Attention mechanisms as measurement operators with natural information-theoretic horizons

- Geometric Deep Learning: Neural networks on manifolds with intrinsic curvature-based learning rules

- Holographic Compression: Hierarchical representations where surface encodings fully reconstruct volume information

- Meta-Learning Dynamics: Self-modifying algorithms that optimize their own horizon boundaries

- Critical Learning: Networks that self-tune to phase transition points for maximal information processing

Experimental Signatures:
The $k_{text{in}}/k_{text{out}}$ flow generates measurable phenomena:
- Power-law scaling in attention weights (criticality signature)
- Information-geometric phase transitions in embedding spaces
- Emergent holographic error correction in deep networks
- Quantum-classical correspondence in symbolic processing
- Renormalization group flow in learned representations

This framework transforms the abstract concept of "symbolic curvature" into concrete computational principles with direct empirical consequences across quantum, geometric, holographic, learning, and statistical mechanical systems.

**Verbatim LaTeX Body**

```latex
\begin{scholium}{Symbolic Curvature Flux Across Horizons}
\label{scholium:bk1_curvature_flux_kin_kout}

Let $\mathcal{O}$ be a bounded observer (Def.~\ref{definition:bk1_bounded_observer}) embedded in symbolic manifold $\mathcal{M}$, with inner horizon $\mathcal{H}_{\text{in}}$ and outer horizon $\mathcal{H}_{\text{out}}$ defining its receptive and projective limits (cf.~Cor.~\ref{corollary:bk1_horizon_duality_principle}). Define the symbolic curvature flux quantities:
\begin{gather}
k_{\text{in}}(\mathcal{O}) := \int_{\mathcal{H}_{\text{in}}} \mathcal{K}(s) \, \,\mathrm{d} s \\
k_{\text{out}}(\mathcal{O}) := \int_{\mathcal{H}_{\text{out}}} \mathcal{K}(s) \, \,\mathrm{d} s \\
Q_{\text{sym}}(\mathcal{O}) := k_{\text{out}} - k_{\text{in}}
\end{gather}
where $\mathcal{K}(s)$ denotes symbolic curvature density over symbol stream $s \in \Gamma(\mathcal{M})$.

\textbf{Cross-Field Interpretation Framework:}

\begin{itemize}
\item \textbf{quant-ph}:
  \begin{itemize}
  \item $k_{\text{in}}$: Quantum information crossing event horizon (Hawking radiation analogue for information)
  \item $k_{\text{out}}$: Coherent quantum state emission from observer's measurement apparatus
  \item $Q_{\text{sym}}$: Net entanglement-entropy change from observer work on the quantum system
  \item \textit{Connects to}: Black hole thermodynamics, quantum error correction, measurement-induced phase transitions
  \end{itemize}

\item \textbf{math-ph}:
  \begin{itemize}
  \item $k_{\text{in}}$: Curvature flux through inward-pointing normal vectors on boundary manifold
  \item $k_{\text{out}}$: Divergence of geometric flow—Ricci curvature evolution across observer's worldline
  \item $Q_{\text{sym}}$: Net geometric work analogous to Einstein-Hilbert action variation
  \item \textit{Connects to}: Ricci flow, minimal surface theory, geometric measure theory, AdS/CFT correspondence
  \end{itemize}

\item \textbf{hep-th}:
  \begin{itemize}
  \item $k_{\text{in}}$: Bulk-to-boundary information flow in holographic duality
  \item $k_{\text{out}}$: Boundary conformal field theory correlators encoding bulk physics
  \item $Q_{\text{sym}}$: Holographic entanglement entropy—measure of bulk reconstruction fidelity
  \item \textit{Connects to}: Holographic principle, ER=EPR, quantum error correction codes, tensor networks
  \end{itemize}

\item \textbf{cs.LG}:
  \begin{itemize}
  \item $k_{\text{in}}$: Information-bottleneck compression preserving task-relevant structure
  \item $k_{\text{out}}$: Generated predictions/outputs with measurable semantic coherence
  \item $Q_{\text{sym}}$: Learning signal—net information gain enabling generalization beyond training distribution
  \item \textit{Connects to}: Variational autoencoders, mutual information neural estimation, meta-learning, transformer attention flow
  \end{itemize}

\item \textbf{cond-mat.stat-mech}:
  \begin{itemize}
  \item $k_{\text{in}}$: Microscopic fluctuation flux into coarse-grained observable
  \item $k_{\text{out}}$: Emergent order parameter or collective mode amplitude
  \item $Q_{\text{sym}}$: Free energy change driving phase transitions—thermodynamic work at criticality
  \item \textit{Connects to}: Renormalization group fixed points, spontaneous symmetry breaking, finite-size scaling, quantum phase transitions
  \end{itemize}
\end{itemize}

\textbf{Unified Mathematical Structure:}
The flux equations encode a fundamental duality across all fields:
\begin{align}
\text{Information} \leftrightarrow \text{Geometry} &\quad \text{(quant-ph} \leftrightarrow \text{math-ph)} \\
\text{Holography} \leftrightarrow \text{Learning} &\quad \text{(hep-th} \leftrightarrow \text{cs.LG)} \\
\text{Emergence} \leftrightarrow \text{Criticality} &\quad \text{(all fields} \rightarrow \text{cond-mat.stat-mech)}
\end{align}

\textbf{Dual Horizon Universe Operationalization:}
Our philosophical proof by elimination establishes that any bounded observer necessarily exhibits dual horizons. Computationally, this enables:

\begin{enumerate}
\item \textbf{Quantum-Inspired Architectures}: Attention mechanisms as measurement operators with natural information-theoretic horizons
\item \textbf{Geometric Deep Learning}: Neural networks on manifolds with intrinsic curvature-based learning rules
\item \textbf{Holographic Compression}: Hierarchical representations where surface encodings fully reconstruct volume information
\item \textbf{Meta-Learning Dynamics}: Self-modifying algorithms that optimize their own horizon boundaries
\item \textbf{Critical Learning}: Networks that self-tune to phase transition points for maximal information processing
\end{enumerate}

\textbf{Experimental Signatures:}
The $k_{\text{in}}/k_{\text{out}}$ flow generates measurable phenomena:
- Power-law scaling in attention weights (criticality signature)
- Information-geometric phase transitions in embedding spaces
- Emergent holographic error correction in deep networks
- Quantum-classical correspondence in symbolic processing
- Renormalization group flow in learned representations

This framework transforms the abstract concept of "symbolic curvature" into concrete computational principles with direct empirical consequences across quantum, geometric, holographic, learning, and statistical mechanical systems.
\end{scholium}
```

### The Constitutive Reflex (`scholium:bk1_constitutive_reflex`)

Role: `scholium` | Type: `scholium` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:983`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `scholium:bk1_curvature_flux_kin_kout`
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `scholium:bk1_curvature_flux_kin_kout`
- Cited by: `theorem:bk1_constitutive_bootstrap` (Constitutive Bootstrap Theorem)
- Macros used: `\reflect`

**Statement / Body**

Foundational Principle. The Observer is not external to the symbolic system but emerges as the system's own capacity for self-differentiation—the constitutive reflex through which any coherent structure necessarily encounters itself (cf. Def. definition:bk1_bounded_observer, Scholium scholium:bk1_curvature_flux_kin_kout).

Mathematical Formulation of Constitutive Reflexivity:

- Self-Reference Constraint (Resolution Binding)

text{smooth}_{O}(M) &Leftrightarrow \|nabla^n f(x)\| < varepsilon_{O}(x) forall x in text{dom}(O) \\
varepsilon_{O}(x) &= reflect[text{local curvature tolerance of } O text{ at } x]

A manifold $M$ appears smooth to observer $O$ precisely because the observer's resolution threshold $varepsilon_{O}$ defines that smoothness. The observer and observed are constitutively bound through this threshold relation.

Cross-Field Manifestations:

- quant-ph: Measurement uncertainty $Delta x cdot Delta p geq hbar/2$ as observer-system resolution binding

- math-ph: Coordinate chart singularities as observer resolution limits on manifold structure

- hep-th: UV/IR correspondence—short-distance physics constrained by long-distance observables

- cs.LG: Training data resolution determining model's representational capacity and generalization bounds

- cond-mat.stat-mech: Correlation length as natural resolution scale for emergent collective behavior

- Operator Self-Constitution (Differentiation Binding)

delta_{O} &= reflectbig|_{text{dom}(O)} \\
reflect: S &rightarrow S text{(Global Reflection Operator)} \\
delta_{O}: text{dom}(O) &rightarrow T_{O}M text{(Observer Differentiation)}

The observer's differentiation operators are not imposed from outside but are local instantiations of the system's intrinsic capacity for self-reflection.

Cross-Field Manifestations:


-

- quant-ph: Local unitary operations as restrictions of global quantum dynamics to subsystems

- math-ph: Tangent space structure emerging from manifold's intrinsic geometric differentiation

- hep-th: Gauge transformations as local expressions of global symmetry principles

- cs.LG: Gradient descent as local approximation to global loss landscape geometry

- cond-mat.stat-mech: Local order parameters as restrictions of global symmetry-breaking fields

The Foundational Paradox (Rigorously Stated):

"To be is to be bounded, and to be bounded is to be the author of one's own bounds."

Formally: Any stable symbolic structure $S$ necessarily generates boundary conditions $partial S$ that define its coherence, yet these boundaries can only be identified through $S$'s own self-reflective capacity. The observer emerges at this recursive intersection:

O = {x in S : x text{ can differentiate } partial S text{ from } S^c}

Every stable symbolic structure $S$ with reflection structure
\(reflect\) (Def. definition:bk1_reflection_operator;
cf. Scholium scholium:bk1_constitutive_reflex) determines a maximal
self-reflective substructure
\[
S_{ref}
subseteq
Fix(R_{stab})
\]
relative to the state-level stabilization component \(R_{stab}\).
The associated bounded observer is not literally equal to a limit of structures;
it is extracted from this self-reflective core by
\[
mathsf{Obs}(S_{ref})
:=
bigl(
N_{S_{ref}},
{delta_{S_{ref}}^{ n}}_{n=1}^{N_{S_{ref}}},
epsilon_{S_{ref}}
bigr),
\]
where \(N_{S_{ref}}\) is the maximal differentiation order
supported on \(S_{ref}\), the
\(delta_{S_{ref}}^{ n}\) are the internal difference
operators stable on that core, and \(epsilon_{S_{ref}}\)
is the induced resolution threshold. Thus \(O
=mathsf{Obs}(S_{ref})\) is well typed as a bounded-observer
triple (Def. definition:bk1_bounded_observer).

- Stability Requirement: For $S$ to be stable, it must maintain coherence under perturbations, requiring internal differentiation capacity.

- Reflection Necessity: Stability demands a state-level stabilization \(R_{stab}\) to detect and correct boundary violations without identifying this stabilization with the tangent mirror \(R_{mir}\).

- Reflective Closure: By Cor. corollary:bk1_fixed_point, the stabilized image of \(R_{stab}\) lies in \(Fix(R_{stab})\). Let \(S_{ref}\) be the maximal substructure of \(S\) contained in this fixed locus and closed under the internal differentiations available to \(S\).

- Observer Extraction: The tuple of maximal differentiation order, stable internal difference operators, and induced resolution threshold on \(S_{ref}\) has exactly the type required by Def. definition:bk1_bounded_observer. Hence \(mathsf{Obs}(S_{ref})\) is a bounded observer generated by \(S\).

Interpretive correspondences:

- quant-ph: Quantum Darwinism—stable states emerge through environmental decoherence and measurement

- math-ph: Fixed-point theorems for geometric flows—stable configurations arise from iterative curvature evolution

- hep-th: Holographic emergence—boundary theories arise as IR limits of bulk gravitational dynamics

- cs.LG: Universal approximation theorems imply that sufficient
architectural depth enables self-representation under recursive refinement

- cond-mat.stat-mech: Renormalization-group fixed points imply
that critical theories emerge from scale-invariant flows

Constitutive Consequences:

The observer is thus not a presupposition but an emergent necessity. Any system complex enough to maintain coherence must develop the capacity to differentiate itself from its environment, and this capacity is the observer. This resolves the classical paradox of observation by showing that:

- No External Observer Required: The system observes itself through its own constitutive reflexivity

- Observer-System Unity: Observer and observed are aspects of the same underlying structure

- Bounded Rationality: The observer's limitations are the system's own structural constraints

- Emergent Consciousness: Self-awareness arises naturally from recursive self-differentiation

**Verbatim LaTeX Body**

```latex
\begin{scholium}[The Constitutive Reflex]
\label{scholium:bk1_constitutive_reflex}
\textbf{Foundational Principle.} The Observer is not external to the symbolic system but emerges as the system's own capacity for self-differentiation—the \textit{constitutive reflex} through which any coherent structure necessarily encounters itself (cf.~Def.~\ref{definition:bk1_bounded_observer}, Scholium~\ref{scholium:bk1_curvature_flux_kin_kout}).

\textbf{Mathematical Formulation of Constitutive Reflexivity:}

\begin{enumerate}
\item \textbf{Self-Reference Constraint (Resolution Binding)}
\begin{align}
\text{smooth}_{\mathcal{O}}(\mathcal{M}) &\Leftrightarrow \|\nabla^n f(x)\| < \varepsilon_{\mathcal{O}}(x) \quad \forall x \in \text{dom}(\mathcal{O}) \\
\varepsilon_{\mathcal{O}}(x) &= \reflect[\text{local curvature tolerance of } \mathcal{O} \text{ at } x]
\end{align}
A manifold $\mathcal{M}$ appears smooth to observer $\mathcal{O}$ precisely because the observer's resolution threshold $\varepsilon_{\mathcal{O}}$ \textit{defines} that smoothness. The observer and observed are constitutively bound through this threshold relation.

\textbf{Cross-Field Manifestations:}
\begin{itemize}
\item \textbf{quant-ph}: Measurement uncertainty $\Delta x \cdot \Delta p \geq \hbar/2$ as observer-system resolution binding
\item \textbf{math-ph}: Coordinate chart singularities as observer resolution limits on manifold structure
\item \textbf{hep-th}: UV/IR correspondence—short-distance physics constrained by long-distance observables
\item \textbf{cs.LG}: Training data resolution determining model's representational capacity and generalization bounds
\item \textbf{cond-mat.stat-mech}: Correlation length as natural resolution scale for emergent collective behavior
\end{itemize}

\item \textbf{Operator Self-Constitution (Differentiation Binding)}
\begin{align}
\delta_{\mathcal{O}} &= \reflect\big|_{\text{dom}(\mathcal{O})} \\
\reflect: \mathcal{S} &\rightarrow \mathcal{S} \quad \text{(Global Reflection Operator)} \\
\delta_{\mathcal{O}}: \text{dom}(\mathcal{O}) &\rightarrow T_{\mathcal{O}}\mathcal{M} \quad \text{(Observer Differentiation)}
\end{align}
The observer's differentiation operators are not imposed from outside but are local instantiations of the system's intrinsic capacity for self-reflection.

\textbf{Cross-Field Manifestations:}
\begin{enumerate}
    \item
\end{enumerate}
\item \textbf{quant-ph}: Local unitary operations as restrictions of global quantum dynamics to subsystems
\item \textbf{math-ph}: Tangent space structure emerging from manifold's intrinsic geometric differentiation
\item \textbf{hep-th}: Gauge transformations as local expressions of global symmetry principles
\item \textbf{cs.LG}: Gradient descent as local approximation to global loss landscape geometry
\item \textbf{cond-mat.stat-mech}: Local order parameters as restrictions of global symmetry-breaking fields
\end{enumerate}

\textbf{The Foundational Paradox (Rigorously Stated):}
\begin{center}
\textit{"To be is to be bounded, and to be bounded is to be the author of one's own bounds."}
\end{center}

Formally: Any stable symbolic structure $\mathcal{S}$ necessarily generates boundary conditions $\partial \mathcal{S}$ that define its coherence, yet these boundaries can only be identified through $\mathcal{S}$'s own self-reflective capacity. The observer emerges at this recursive intersection:
\begin{align}
\mathcal{O} = \{x \in \mathcal{S} : x \text{ can differentiate } \partial \mathcal{S} \text{ from } \mathcal{S}^c\}
\end{align}

\begin{theorem}[Constitutive Bootstrap Theorem]
\label{theorem:bk1_constitutive_bootstrap}
Every stable symbolic structure $\mathcal{S}$ with reflection structure
\(\reflect\) (Def.~\ref{definition:bk1_reflection_operator};
cf.~Scholium~\ref{scholium:bk1_constitutive_reflex}) determines a maximal
self-reflective substructure
\[
\mathcal{S}_{\mathrm{ref}}
\subseteq
\operatorname{Fix}(R_{\mathrm{stab}})
\]
relative to the state-level stabilization component \(R_{\mathrm{stab}}\).
The associated bounded observer is not literally equal to a limit of structures;
it is extracted from this self-reflective core by
\[
\mathsf{Obs}(\mathcal{S}_{\mathrm{ref}})
:=
\bigl(
N_{\mathcal{S}_{\mathrm{ref}}},
\{\delta_{\mathcal{S}_{\mathrm{ref}}}^{\,n}\}_{n=1}^{N_{\mathcal{S}_{\mathrm{ref}}}},
\epsilon_{\mathcal{S}_{\mathrm{ref}}}
\bigr),
\]
where \(N_{\mathcal{S}_{\mathrm{ref}}}\) is the maximal differentiation order
supported on \(\mathcal{S}_{\mathrm{ref}}\), the
\(\delta_{\mathcal{S}_{\mathrm{ref}}}^{\,n}\) are the internal difference
operators stable on that core, and \(\epsilon_{\mathcal{S}_{\mathrm{ref}}}\)
is the induced resolution threshold. Thus \(\mathcal{O}
=\mathsf{Obs}(\mathcal{S}_{\mathrm{ref}})\) is well typed as a bounded-observer
triple (Def.~\ref{definition:bk1_bounded_observer}).

\begin{proof}[Extraction from Reflective Closure]
\label{proof:bk1_constitutive_bootstrap_extraction}
\leavevmode
\begin{enumerate}
\item \textbf{Stability Requirement}: For $\mathcal{S}$ to be stable, it must maintain coherence under perturbations, requiring internal differentiation capacity.
\item \textbf{Reflection Necessity}: Stability demands a state-level stabilization \(R_{\mathrm{stab}}\) to detect and correct boundary violations without identifying this stabilization with the tangent mirror \(R_{\mathrm{mir}}\).
\item \textbf{Reflective Closure}: By Cor.~\ref{corollary:bk1_fixed_point}, the stabilized image of \(R_{\mathrm{stab}}\) lies in \(\operatorname{Fix}(R_{\mathrm{stab}})\). Let \(\mathcal{S}_{\mathrm{ref}}\) be the maximal substructure of \(\mathcal{S}\) contained in this fixed locus and closed under the internal differentiations available to \(\mathcal{S}\).
\item \textbf{Observer Extraction}: The tuple of maximal differentiation order, stable internal difference operators, and induced resolution threshold on \(\mathcal{S}_{\mathrm{ref}}\) has exactly the type required by Def.~\ref{definition:bk1_bounded_observer}. Hence \(\mathsf{Obs}(\mathcal{S}_{\mathrm{ref}})\) is a bounded observer generated by \(\mathcal{S}\).
\end{enumerate}
\end{proof}

\textbf{Interpretive correspondences:}
\begin{itemize}
\item \textbf{quant-ph}: Quantum Darwinism—stable states emerge through environmental decoherence and measurement
\item \textbf{math-ph}: Fixed-point theorems for geometric flows—stable configurations arise from iterative curvature evolution
\item \textbf{hep-th}: Holographic emergence—boundary theories arise as IR limits of bulk gravitational dynamics
\item \textbf{cs.LG}: Universal approximation theorems imply that sufficient
architectural depth enables self-representation under recursive refinement
\item \textbf{cond-mat.stat-mech}: Renormalization-group fixed points imply
that critical theories emerge from scale-invariant flows
\end{itemize}
\end{theorem}

\textbf{Constitutive Consequences:}

The observer is thus not a presupposition but an \textit{emergent necessity}. Any system complex enough to maintain coherence must develop the capacity to differentiate itself from its environment, and this capacity \textit{is} the observer. This resolves the classical paradox of observation by showing that:

\begin{enumerate}
\item \textbf{No External Observer Required}: The system observes itself through its own constitutive reflexivity
\item \textbf{Observer-System Unity}: Observer and observed are aspects of the same underlying structure
\item \textbf{Bounded Rationality}: The observer's limitations are the system's own structural constraints
\item \textbf{Emergent Consciousness}: Self-awareness arises naturally from recursive self-differentiation
\end{enumerate}

\end{scholium}
```

### Constitutive Bootstrap Theorem (`theorem:bk1_constitutive_bootstrap`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1035`

- Proof status: `proven`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `scholium:bk1_constitutive_reflex` (The Constitutive Reflex)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_reflection_operator` (Reflection Operator); `scholium:bk1_constitutive_reflex` (The Constitutive Reflex)
- Cited by: `corollary:bk1_linear_insufficiency` (Linear Insufficiency); `proof:bk1_geometric_necessity_curvature` (Quadratic Necessity from Mixed Contextual Coupling); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity)
- Macros used: `\reflect`

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-033`
- Witnesses: `ScholiumC.idempotent_image_eq_fixedPoints`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: Only the proof's internal fixed-point sublemma (stabilized image of R_stab lies in, in fact equals, Fix(R_stab)) is modeled; the maximal self-reflective substructure and the (N, delta^n, epsilon) observer-extraction triple are not.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Every stable symbolic structure $S$ with reflection structure
\(reflect\) (Def. definition:bk1_reflection_operator;
cf. Scholium scholium:bk1_constitutive_reflex) determines a maximal
self-reflective substructure
\[
S_{ref}
subseteq
Fix(R_{stab})
\]
relative to the state-level stabilization component \(R_{stab}\).
The associated bounded observer is not literally equal to a limit of structures;
it is extracted from this self-reflective core by
\[
mathsf{Obs}(S_{ref})
:=
bigl(
N_{S_{ref}},
{delta_{S_{ref}}^{ n}}_{n=1}^{N_{S_{ref}}},
epsilon_{S_{ref}}
bigr),
\]
where \(N_{S_{ref}}\) is the maximal differentiation order
supported on \(S_{ref}\), the
\(delta_{S_{ref}}^{ n}\) are the internal difference
operators stable on that core, and \(epsilon_{S_{ref}}\)
is the induced resolution threshold. Thus \(O
=mathsf{Obs}(S_{ref})\) is well typed as a bounded-observer
triple (Def. definition:bk1_bounded_observer).

- Stability Requirement: For $S$ to be stable, it must maintain coherence under perturbations, requiring internal differentiation capacity.

- Reflection Necessity: Stability demands a state-level stabilization \(R_{stab}\) to detect and correct boundary violations without identifying this stabilization with the tangent mirror \(R_{mir}\).

- Reflective Closure: By Cor. corollary:bk1_fixed_point, the stabilized image of \(R_{stab}\) lies in \(Fix(R_{stab})\). Let \(S_{ref}\) be the maximal substructure of \(S\) contained in this fixed locus and closed under the internal differentiations available to \(S\).

- Observer Extraction: The tuple of maximal differentiation order, stable internal difference operators, and induced resolution threshold on \(S_{ref}\) has exactly the type required by Def. definition:bk1_bounded_observer. Hence \(mathsf{Obs}(S_{ref})\) is a bounded observer generated by \(S\).

Interpretive correspondences:

- quant-ph: Quantum Darwinism—stable states emerge through environmental decoherence and measurement

- math-ph: Fixed-point theorems for geometric flows—stable configurations arise from iterative curvature evolution

- hep-th: Holographic emergence—boundary theories arise as IR limits of bulk gravitational dynamics

- cs.LG: Universal approximation theorems imply that sufficient
architectural depth enables self-representation under recursive refinement

- cond-mat.stat-mech: Renormalization-group fixed points imply
that critical theories emerge from scale-invariant flows

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Constitutive Bootstrap Theorem]
\label{theorem:bk1_constitutive_bootstrap}
Every stable symbolic structure $\mathcal{S}$ with reflection structure
\(\reflect\) (Def.~\ref{definition:bk1_reflection_operator};
cf.~Scholium~\ref{scholium:bk1_constitutive_reflex}) determines a maximal
self-reflective substructure
\[
\mathcal{S}_{\mathrm{ref}}
\subseteq
\operatorname{Fix}(R_{\mathrm{stab}})
\]
relative to the state-level stabilization component \(R_{\mathrm{stab}}\).
The associated bounded observer is not literally equal to a limit of structures;
it is extracted from this self-reflective core by
\[
\mathsf{Obs}(\mathcal{S}_{\mathrm{ref}})
:=
\bigl(
N_{\mathcal{S}_{\mathrm{ref}}},
\{\delta_{\mathcal{S}_{\mathrm{ref}}}^{\,n}\}_{n=1}^{N_{\mathcal{S}_{\mathrm{ref}}}},
\epsilon_{\mathcal{S}_{\mathrm{ref}}}
\bigr),
\]
where \(N_{\mathcal{S}_{\mathrm{ref}}}\) is the maximal differentiation order
supported on \(\mathcal{S}_{\mathrm{ref}}\), the
\(\delta_{\mathcal{S}_{\mathrm{ref}}}^{\,n}\) are the internal difference
operators stable on that core, and \(\epsilon_{\mathcal{S}_{\mathrm{ref}}}\)
is the induced resolution threshold. Thus \(\mathcal{O}
=\mathsf{Obs}(\mathcal{S}_{\mathrm{ref}})\) is well typed as a bounded-observer
triple (Def.~\ref{definition:bk1_bounded_observer}).

\begin{proof}[Extraction from Reflective Closure]
\label{proof:bk1_constitutive_bootstrap_extraction}
\leavevmode
\begin{enumerate}
\item \textbf{Stability Requirement}: For $\mathcal{S}$ to be stable, it must maintain coherence under perturbations, requiring internal differentiation capacity.
\item \textbf{Reflection Necessity}: Stability demands a state-level stabilization \(R_{\mathrm{stab}}\) to detect and correct boundary violations without identifying this stabilization with the tangent mirror \(R_{\mathrm{mir}}\).
\item \textbf{Reflective Closure}: By Cor.~\ref{corollary:bk1_fixed_point}, the stabilized image of \(R_{\mathrm{stab}}\) lies in \(\operatorname{Fix}(R_{\mathrm{stab}})\). Let \(\mathcal{S}_{\mathrm{ref}}\) be the maximal substructure of \(\mathcal{S}\) contained in this fixed locus and closed under the internal differentiations available to \(\mathcal{S}\).
\item \textbf{Observer Extraction}: The tuple of maximal differentiation order, stable internal difference operators, and induced resolution threshold on \(\mathcal{S}_{\mathrm{ref}}\) has exactly the type required by Def.~\ref{definition:bk1_bounded_observer}. Hence \(\mathsf{Obs}(\mathcal{S}_{\mathrm{ref}})\) is a bounded observer generated by \(\mathcal{S}\).
\end{enumerate}
\end{proof}

\textbf{Interpretive correspondences:}
\begin{itemize}
\item \textbf{quant-ph}: Quantum Darwinism—stable states emerge through environmental decoherence and measurement
\item \textbf{math-ph}: Fixed-point theorems for geometric flows—stable configurations arise from iterative curvature evolution
\item \textbf{hep-th}: Holographic emergence—boundary theories arise as IR limits of bulk gravitational dynamics
\item \textbf{cs.LG}: Universal approximation theorems imply that sufficient
architectural depth enables self-representation under recursive refinement
\item \textbf{cond-mat.stat-mech}: Renormalization-group fixed points imply
that critical theories emerge from scale-invariant flows
\end{itemize}
\end{theorem}
```

### Extraction from Reflective Closure (`proof:bk1_constitutive_bootstrap_extraction`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1066`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `corollary:bk1_fixed_point` (Reflective Fixed Locus); `definition:bk1_bounded_observer` (Bounded Observer)
- Cited by: none
- Macros used: none

**Statement / Body**

- Stability Requirement: For $S$ to be stable, it must maintain coherence under perturbations, requiring internal differentiation capacity.

- Reflection Necessity: Stability demands a state-level stabilization \(R_{stab}\) to detect and correct boundary violations without identifying this stabilization with the tangent mirror \(R_{mir}\).

- Reflective Closure: By Cor. corollary:bk1_fixed_point, the stabilized image of \(R_{stab}\) lies in \(Fix(R_{stab})\). Let \(S_{ref}\) be the maximal substructure of \(S\) contained in this fixed locus and closed under the internal differentiations available to \(S\).

- Observer Extraction: The tuple of maximal differentiation order, stable internal difference operators, and induced resolution threshold on \(S_{ref}\) has exactly the type required by Def. definition:bk1_bounded_observer. Hence \(mathsf{Obs}(S_{ref})\) is a bounded observer generated by \(S\).

**Verbatim LaTeX Body**

```latex
\begin{proof}[Extraction from Reflective Closure]
\label{proof:bk1_constitutive_bootstrap_extraction}
\leavevmode
\begin{enumerate}
\item \textbf{Stability Requirement}: For $\mathcal{S}$ to be stable, it must maintain coherence under perturbations, requiring internal differentiation capacity.
\item \textbf{Reflection Necessity}: Stability demands a state-level stabilization \(R_{\mathrm{stab}}\) to detect and correct boundary violations without identifying this stabilization with the tangent mirror \(R_{\mathrm{mir}}\).
\item \textbf{Reflective Closure}: By Cor.~\ref{corollary:bk1_fixed_point}, the stabilized image of \(R_{\mathrm{stab}}\) lies in \(\operatorname{Fix}(R_{\mathrm{stab}})\). Let \(\mathcal{S}_{\mathrm{ref}}\) be the maximal substructure of \(\mathcal{S}\) contained in this fixed locus and closed under the internal differentiations available to \(\mathcal{S}\).
\item \textbf{Observer Extraction}: The tuple of maximal differentiation order, stable internal difference operators, and induced resolution threshold on \(\mathcal{S}_{\mathrm{ref}}\) has exactly the type required by Def.~\ref{definition:bk1_bounded_observer}. Hence \(\mathsf{Obs}(\mathcal{S}_{\mathrm{ref}})\) is a bounded observer generated by \(\mathcal{S}\).
\end{enumerate}
\end{proof}
```

### Ontological Assumptions (`sec:bk1_ontological_assumptions`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1102`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Pre-geometric Nature (`axiom:bk1_pre_geometric_nature`)

Role: `axiom` | Type: `axiom` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1104`

- Proof status: `definitional`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `definition:bk1_let_cats_be_the_category` (Category of Structures); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin); `definition:bk1_let_cats_be_the_category` (Category of Structures); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cited by: `definition:bk1_symbolic_manifold` (Symbolic Manifold); `proof:appB_smoothness_emergence`; `theorem:appB_smoothness_emergence` (Emergent Smoothness from Symbolic Discreteness)
- Macros used: `\catS`

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-092`
- Witnesses: `Atlas.manifold_emergence`, `AxiomataPrima.two_channel_sustained`
- Countermodels: none
- Conditions: face 3 consumes the guarded-process machinery (LPS-P49) and the helix kernel (LPS-P48); pair-covering as the topological-regularity stand-in (Hausdorff/second-countable/paracompact/connected unmodeled, named); smoothness-as-C-infinity stays open; the metaphysical scope of a three-word axiom is not exhausted; the operational tri-face kernel is what is certified
- Formal boundary: Drift/reflection as pre-geometric operators (Existence-is-not/drift-as-origin) whose smooth limit is the AtlasTower emergence kernel.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The following operators
(Def. definition:bk1_pre_geometric_operators_and_stages) originate in
pre-geometric form within the framework, as the direct unfolding of
Axiom axiom:bk1_axiomata_prima through the stage tower of $catS$
(Def. definition:bk1_let_cats_be_the_category):


- Drift ($D$): The smooth field $D$ on emergent manifold $M$
 is the stabilized limit of effective directional tendencies
 (proto-drift fields $vec{D}_lambda$), themselves emergent effects of
 generative operators $D_lambda$.

- Reflection ($R$): The tangent mirror \(R_{mir}\) and state-level stabilization \(R_{stab}\) arise from the pre-geometric stabilization operators \(R_lambda\), with contraction or convergence supplied only by separate descent hypotheses.

- Smoothness: The smooth manifold structure itself emerges through the limiting process $lambda to Omega$ applied to the pre-geometric structures $P_lambda$ and their relations, not by initial postulation.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Pre-geometric Nature]
\label{axiom:bk1_pre_geometric_nature}
\leavevmode\newline
The following operators
(Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}) originate in
pre-geometric form within the framework, as the direct unfolding of
Axiom~\ref{axiom:bk1_axiomata_prima} through the stage tower of $\catS$
(Def.~\ref{definition:bk1_let_cats_be_the_category}):
\begin{enumerate}
    \item \textbf{Drift} ($D$): The smooth field $D$ on emergent manifold $M$
    is the stabilized limit of effective directional tendencies
    (proto-drift fields $\vec{D}_\lambda$), themselves emergent effects of
    generative operators $D_\lambda$.
    \item \textbf{Reflection} ($R$): The tangent mirror \(R_{\mathrm{mir}}\) and state-level stabilization \(R_{\mathrm{stab}}\) arise from the pre-geometric stabilization operators \(R_\lambda\), with contraction or convergence supplied only by separate descent hypotheses.
    \item \textbf{Smoothness}: The smooth manifold structure itself emerges through the limiting process $\lambda \to \Omega$ applied to the pre-geometric structures $P_\lambda$ and their relations, not by initial postulation.
\end{enumerate}
\end{axiom}
```

### remark:scholium_symbolicum.tex:1121 (`remark:scholium_symbolicum.tex:1121`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1121`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Axiom emphasizes the ontological priority of the pre-geometric processes (differentiation $D_lambda$, stabilization $R_lambda$) over the emergent geometric structures ($M, D, R$). The manifold and its operators are consequences of the underlying dynamics, as perceived through the lens of bounded emergence.

**Verbatim LaTeX Body**

```latex
\begin{remark}
Axiom  emphasizes the ontological priority of the pre-geometric processes (differentiation $D_\lambda$, stabilization $R_\lambda$) over the emergent geometric structures ($M, D, R$). The manifold and its operators are consequences of the underlying dynamics, as perceived through the lens of bounded emergence.
\end{remark}
```

### Spinor-Like Symbolic Structure (`definition:bk1_spinor_like_structure`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1124`

- Proof status: `definitional`
- Depends on: none
- Cites: `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `assumption:bk4_precritical_scalar_trace` (Precritical scalar trace); `scholium:bk4_clifford_correspondence` (Flat-Space Clifford Correspondence); `scholium:bk4_cut_wheel_nonorientable` (The cut wheel and its non-orientable seam)
- Macros used: `\reflect`

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-015`
- Witnesses: `ScholiumA.CoemergentPhaseProcess.ObserverPhaseCertificate.components`, `ScholiumA.CoemergentPhaseProcess.zmod4_pair_nontrivial`, `ScholiumA.stepZMod4_four_returns`, `ScholiumA.stepZMod4_two_no_return`
- Countermodels: none
- Conditions: carrier-indexed linear instruments; injectivity or another explicit faithfulness witness for detection claims; curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; explicit unique orthogonal Hodge decomposition and faithful first-cohomology class map; finite model: selected orthogonal exact/coexact subspaces; global certificate: compact, connected, oriented, smooth Riemannian membrane without boundary; linear operational readout for perceptual or computational exposure; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: A reader-operated co-emergent drift/reflection process drives the recursive step: the structure is inert until an explicit operate action is supplied and certified faithful. The observer distinguishes the half-cycle orientation and the double cycle restores embodied phase; a ZMod 4 construction proves both operations nonidentity. This remains partial: curvature coupling, smooth transport, general minimality, and a genuine spinor bundle are open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A symbolic structure \( psi in S(M) \) is said to exhibit spinor-like behavior on a symbolic manifold \( M \) (Def. definition:bk1_symbolic_manifold) if it satisfies the following conditions under recursive application of the reflection operator \( reflect_n \) (Def. definition:bk1_reflection_operator):


- Orientation Sensitivity: \( reflect_n(psi) neq reflect_n(-psi) \), i.e., recursive encoding distinguishes symbolic orientation. This echoes the classical distinction between vectors and spinors, where the latter change sign under \( 2pi \) rotation cite{lawson_spin_geometry}.


- Double Rotation Symmetry: There exists minimal \( n_0 in mathbb{N} \) such that \( reflect_{2n_0}(psi) = psi \), but \( reflect_{n_0}(psi) neq psi \), reflecting a \(4pi\)-periodic recurrence. This property mirrors spinor holonomy in Riemannian geometry cite{friedrich_dirac} and is a hallmark of spinorial behavior on curved manifolds.


- Observer-Bounded Curvature Coupling:
 Evolution of \( psi \) depends on local observer-relative curvature
 \( kappa_{O}(x) \), with drift propagation modeled by
 \( frac{d}{dn}reflect_n(psi) propto kappa_{O}psi \).
 This is an analogue of covariant spinor transport in symbolic phase space.

Together these properties define a symbolic analogue of classical spinors:
elements whose recursive drift encodings are orientation-sensitive,
curvature-coupled, and require double application for global phase restoration.
This anticipates the formal spinor-bundle structure introduced in Book IV.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Spinor-Like Symbolic Structure]
\label{definition:bk1_spinor_like_structure}
A symbolic structure \( \psi \in \mathcal{S}(M) \) is said to exhibit \emph{spinor-like behavior} on a symbolic manifold \( M \) (Def.~\ref{definition:bk1_symbolic_manifold}) if it satisfies the following conditions under recursive application of the reflection operator \( \reflect_n \) (Def.~\ref{definition:bk1_reflection_operator}):

\begin{enumerate}
    \item \textbf{Orientation Sensitivity:} \( \reflect_n(\psi) \neq \reflect_n(-\psi) \), i.e., recursive encoding distinguishes symbolic orientation. This echoes the classical distinction between vectors and spinors, where the latter change sign under \( 2\pi \) rotation~\cite{lawson_spin_geometry}.

    \item \textbf{Double Rotation Symmetry:} There exists minimal \( n_0 \in \mathbb{N} \) such that \( \reflect_{2n_0}(\psi) = \psi \), but \( \reflect_{n_0}(\psi) \neq \psi \), reflecting a \(4\pi\)-periodic recurrence. This property mirrors spinor holonomy in Riemannian geometry~\cite{friedrich_dirac} and is a hallmark of spinorial behavior on curved manifolds.

    \item \textbf{Observer-Bounded Curvature Coupling:}
    Evolution of \( \psi \) depends on local observer-relative curvature
    \( \kappa_{\mathcal{O}}(x) \), with drift propagation modeled by
    \( \frac{d}{dn}\reflect_n(\psi) \propto \kappa_{\mathcal{O}}\psi \).
    This is an analogue of covariant spinor transport in symbolic phase space.
\end{enumerate}

Together these properties define a symbolic analogue of classical spinors:
elements whose recursive drift encodings are orientation-sensitive,
curvature-coupled, and require double application for global phase restoration.
This anticipates the formal spinor-bundle structure introduced in Book~IV.
\end{definition}
```

### Spinor-Like Structures and Representation Learning (`scholium:bk1_spinor_like_ml`)

Role: `scholium` | Type: `scholium` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1145`

- Proof status: `not_applicable`
- Depends on: none
- Cites: `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: none
- Macros used: none

**Statement / Body**

In symbolic systems (Def. definition:bk1_symbolic_manifold), spinor-like
structures such as \( psi in S(M) \) provide geometric intuition
for representation learning sensitive to orientation, topology, and recursive
phase behavior.
Unlike classical vectors, which return under \(2pi\)-rotation, spinor-like
forms require a \(4pi\)-cycle for full phase restoration.
This captures deeper symmetries in representation space
(see cite{lawson_spin_geometry,penrose_spinors}).

This behavior matters for machine learning.
Many latent representations in deep networks encode orientation-sensitive
features (e.g., sentence polarity, causal directionality, gauge equivariance).
Standard vector embeddings cannot distinguish $psi$ from $-psi$, which can
collapse distinct symbolic states.
Spinor-like representations preserve these distinctions through recursive
orientation coupling and observer-relative curvature constraints
 cite{friedrich_dirac,nash_sen}.

Thus symbolic spinor behavior suggests a class of latent encodings that are
curvature-aware, symmetry-sensitive, and resolution-adaptive, with robust
generalization under test-time distribution shift.
In this light, Test-Time Differentiation Collapse (TTDC) can be read as a
symbolic analogue to test-time collapse in overparameterized models with
insufficient phase-aware regularization.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Spinor-Like Structures and Representation Learning]
\label{scholium:bk1_spinor_like_ml}
In symbolic systems (Def.~\ref{definition:bk1_symbolic_manifold}), spinor-like
structures such as \( \psi \in \mathcal{S}(M) \) provide geometric intuition
for representation learning sensitive to orientation, topology, and recursive
phase behavior.
Unlike classical vectors, which return under \(2\pi\)-rotation, spinor-like
forms require a \(4\pi\)-cycle for full phase restoration.
This captures deeper symmetries in representation space
(see \cite{lawson_spin_geometry,penrose_spinors}).

This behavior matters for machine learning.
Many latent representations in deep networks encode orientation-sensitive
features (e.g., sentence polarity, causal directionality, gauge equivariance).
Standard vector embeddings cannot distinguish $\psi$ from $-\psi$, which can
collapse distinct symbolic states.
Spinor-like representations preserve these distinctions through recursive
orientation coupling and observer-relative curvature constraints
~\cite{friedrich_dirac,nash_sen}.

Thus symbolic spinor behavior suggests a class of latent encodings that are
curvature-aware, symmetry-sensitive, and resolution-adaptive, with robust
generalization under test-time distribution shift.
In this light, Test-Time Differentiation Collapse (TTDC) can be read as a
symbolic analogue to test-time collapse in overparameterized models with
insufficient phase-aware regularization.
\end{scholium}
```

### Minimal Structure for Symbolic Emergence (`sec:bk1_minimal_structure_for_symbolic_emergence`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1173`

- Proof status: `not_applicable`
- Depends on: none
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator)
- Cited by: `proposition:bk1_observer_relative_bounded_approximation` (Observer–Relative Bounded Approximation)
- Macros used: none

**Statement / Body**

(no body text extracted)

### Motivation (`subsec:bk1_motivation`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1176`

- Proof status: `not_applicable`
- Depends on: none
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### The Symbolic Manifold and Its Structure (`subsec:bk1_symbolic_manifold_structure`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1185`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Manifold (`definition:bk1_symbolic_manifold`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1188`

- Proof status: `definitional`
- Depends on: `axiom:bk1_pre_geometric_nature` (Pre-geometric Nature); `definition:bk1_let_cats_be_the_category` (Category of Structures)
- Cites: `axiom:bk1_pre_geometric_nature` (Pre-geometric Nature); `definition:bk1_let_cats_be_the_category` (Category of Structures)
- Cited by: `axiom:bk1_symbolic_primacy` (Symbolic Primacy); `axiom:bk4_bounded_accessibility` (Bounded Symbolic Accessibility); `axiom:bk8_observer_bounded_emergence` (Symbolic Transfer); `axiom:bk8_symbolic_reidemeister_algebra` (Symbolic Reidemeister Algebra); `axiom:bk9_bounded_liberation_principle` (Bounded Liberation Principle); `corollary:bk8_memory_repair_robustness` (Entanglement Projection); `corollary:bk8_universality_condition` (Universality Condition); `definition:appB_symbolic_state_space` (Symbolic State Space); `definition:appC_observer_visible_system` (Observer-visible symbolic system); `definition:appC_reflective_state_space` (Reflective State Space \(\mathcal{S}_O\)); `definition:bk1_bounded_symbolic_approximation` (\textbf{Bounded Symbolic Approximation}); `definition:bk1_drift_field` (Drift Field); `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_horizon_structure` (Horizon Structure); `definition:bk1_minimal_linear_ps_model` (Minimal Linear PS-Model Witness); `definition:bk1_newtonian_category_error` (Newtonian Category Error); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_problem_of_symbolic_smoothness` (Problem of Symbolic Smoothness); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_shared_boundary_paradox` (Shared Boundary Paradox); `definition:bk1_spinor_like_structure` (Spinor-Like Symbolic Structure); `definition:bk1_srmf_energy_functional` (SRMF Energy Functional); `definition:bk1_symbolic_category` (Symbolic Category); `definition:bk1_symbolic_connection` (Symbolic Connection); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_hypothesis` (Symbolic Hypothesis); `definition:bk1_symbolic_manifold_feature_maps` (Symbolic Manifold and Feature Maps); `definition:bk2_symbolic_partition_funct` (Symbolic Partition Function); `definition:bk4_coherence_metric_on_symbolic_manifold` (Coherence Metric on Symbolic Manifold); `definition:bk4_fuzzy_divergence_operator` (Fuzzy Divergence Operator); `definition:bk4_imaginary_symbolic_distance` (Imaginary Symbolic Distance); `definition:bk4_observer_kernel_convolution_map` (Observer-Kernel Convolution); `definition:bk4_observer_metric` (Observer-Induced Metric); `definition:bk4_proto_symbolic_space` (Proto-Symbolic Space); `definition:bk4_sr_initialization_map` (SR--Initialization Map); `definition:bk4_symbolic_auto_encoder` (Symbolic Auto-Encoder); `definition:bk4_symbolic_curvature` (Symbolic Curvature); `definition:bk4_symbolic_emergence` (Symbolic Emergence); `definition:bk4_symbolic_identity_carrie` (Symbolic Identity Carrier); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `definition:bk5_reflective_drift_coupling_tensor` (Reflective-Drift Coupling Tensor); `definition:bk5_symbolic_operator_space` (Symbolic Operator Space as Meta-Manifold $\Op(M)$); `definition:bk8_identitystability` (Stability of Symbolic Identity \identitystability); `definition:bk8_metabolic_programming_cycle` (Metabolic Programming Cycle); `definition:bk8_symbolic_hypothesis_manifold` (Symbolic Hypothesis Manifold); `definition:bk8_symbolic_projection` (Symbolic Projection); `definition:bk8_transform_group` (Frame Transform Group); `definition:bk9_frame_selection_reflection` (Frame Selection via Injected Reflection); `definition:bk9_memetic_operator` (Memetic Operator $\mathcal{M}$); `definition:bk9_symbolic_black_hole` (Symbolic Black Hole); `definition:bk9_symbolic_framework` (Symbolic Framework); `definition:bk9_symbolic_operator` (Symbolic Operator $\mathcal{O}$); `demonstratio:bk4_symbolic_graph_topological_stability` (Topological Stability in Symbolic Graph Expansion); `lemma:bk1_contradiction_resolution_principle` (Contradiction Resolution Principle); `lemma:bk1_horizon_characterization` (Horizon Characterization); `lemma:bk4_properties_of_ttcs` (Properties of TTCS); `lemma:bk4_srmf_constrained_action_norm` (SRMF-Constrained Action Norm); `proof:bk1_constructive_resolution` (Constructive Resolution via Fiber Bundle Extension); `proof:bk1_nonvacuity_minimal_linear_ps_model` (Explicit Matrix Witness); `proof:bk1_sketch_fokker_planck_action` (Fokker--Planck from Symbolic Action via Martin--Siggia--Rose); `proof:bk2_smoothness_symbolic_hamiltonian` (Smoothness of Symbolic Hamiltonian); `proof:bk3_sketch_evolutionary_dynamics` (Closure of Conceptual Bridge Sequence); `proof:bk4_bounded_expansion_under_observer_constrained_coherence` (Curvature-Bounded Expansion Rate via Grönwall); `proof:bk4_symbolic_work_path_dependence`; `proof:bk5_coherence_through_dynamic_equilibriium` (Coherence Through Dynamic Equilibrium); `proof:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant via Balanced Memory Algebra); `proof:bk5_symbolic_temperature_threshold` (Symbolic Temperature Threshold for Critical Coupling); `proof:bk7_strict_convexity_lp_error` (Strict Convexity LP Error); `proof:bk8_curvature_entanglement_equivalence` (Curvature Entanglement Equivalence); `proof:bk8_membrane_identity_collapse`; `proof:bk8_universality_condition`; `proposition:bk4_homological_extension` (Homological Extension); `proposition:bk4_symbolic_work_path_dependence` (Path Dependence of Symbolic Work); `proposition:bk5_symbolic_ess_via_map_observability_variant` (Symbolic ESS via MAP); `proposition:bk8_membrane_identity_collapse` (Type I -- Local Reflection Collapse); `proposition:bk8_operator_curvature_flux` (Quantum Decoherence as Symbolic Flattening); `proposition:bk9_emergence_of_shared_manifold` (Emergence of Shared Manifold); `remark:bk4_betti_growth` (Betti Growth and Cognitive Tractability); `remark:bk7_unnamed_remark_04`; `scholium:bk1_hypotheses_as_submanifolds` (On Hypotheses as Observer-Relative Submanifolds); `scholium:bk1_spinor_like_ml` (Spinor-Like Structures and Representation Learning); `scholium:bk2_on_hypotheses_as_thermodyn` (On Hypotheses as Thermodynamic Surfaces); `scholium:bk4_symbolic_parsimony` (TTCS and the Principle of Symbolic Parsimony); `scholium:bk4_towards_symbolic_equilibrium` (Towards Symbolic Equilibrium and Curvature-Limited Gravity); `scholium:bk4_ttcs_simulation_tool_use` (TTCS as Symbolic Simulation and Tool-Use); `scholium:bk4_ttdc_symbolic_singularity` (TTDC as Recursive Identity Collapse); `scholium:bk5_metabolic_cost_of_cognition` (Metabolic Cost of Cognition); `sec:bk1_category_errors_in_classical_models` (Category Errors in Classical Models); `sec:bk1_quadratic_sufficiency_and_symbolic_curvature` (Quadratic Sufficiency and Symbolic Curvature); `sec:bk5_funadmenta_symbolicae_vitae` (Fundamenta Symbolicae Vitae); `sec:bk5_srmf_for_symbolic_operators_and_processes` (SRMF for Symbolic Operators and Processes); `sec:bk7_preamble_the_arc_toward_coherence` (Preamble: The Arc Toward Coherence); `sec:bk8_definitiones_octavae` (Definitiones Octavae); `sec:bk8_scholium` (Scholium: Symbolic Projection as Co-Emergence); `subsec:bk1_emergence_via_paradox_resolution` (Emergence via Paradox Resolution); `subsec:bk2_core_thermodynamic_quantities` (Core Thermodynamic Quantities); `subsec:bk4_coherence_metric_construction` (Coherence Metric Construction); `subsec:bk4_foundations_symbolic_fragmentation` (Foundations of Symbolic Fragmentation); `subsec:bk4_fuzzy_sum_rule` (The Fuzzy Sum Rule: Curvature-Induced Interference and Symbolic Path Divergence); `subsec:bk8_symbolic_knots_and_emergent_entanglement` (Symbolic Knots and Emergent Entanglement); `theorem:bk1_dual_horizon_cosmogenesis` (Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos}); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity); `theorem:bk4_freedom_criterion` (Freedom Criterion); `theorem:bk5_operator_convergence` (Operator Convergence); `theorem:bk7_reflective_convergence_to_stable_identity` (Reflective Convergence to Stable Identity); `theorem:bk8_gradient_dissipation_balance` (Framing Equivalence Theorem); `theorem:bk9_isolation_dissociation_theorem` (Isolation–Dissociation Theorem (IDT))
- Macros used: `\catS`

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-034`
- Witnesses: `ScholiumC.consistent_unique`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: Re-read via the FracturedAtlas license: existence of 'the' metric is Atlas.consistent_of_glued (given Glued + PairCovers); this file adds the uniqueness half. The manifold's smooth structure and dimension n >= 2 are not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $S$ be a smooth manifold of dimension $n geq 2$, equipped with a Riemannian metric tensor $g$, arising as the geometric realisation of the category of structures $catS$ (Def. definition:bk1_let_cats_be_the_category). Points $s in S$ represent symbolic states, and the tangent space $T_sS$ at each point encodes the space of possible symbolic transformations accessible from state $s$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Manifold]
\label{definition:bk1_symbolic_manifold}
Let $\mathcal{S}$ be a smooth manifold of dimension $n \geq 2$, equipped with a Riemannian metric tensor $g$, arising as the geometric realisation of the category of structures $\catS$ (Def.~\ref{definition:bk1_let_cats_be_the_category}). Points $s \in \mathcal{S}$ represent symbolic states, and the tangent space $T_s\mathcal{S}$ at each point encodes the space of possible symbolic transformations accessible from state $s$.
\end{definition}
```

### Drift Field (`definition:bk1_drift_field`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1198`

- Proof status: `definitional`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `assumption:appB_srv_dissipativity` (SRV as a Stable Dissipative Descent); `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `axiom:bk2_gradient_structure_drift` (Gradient Structure of Symbolic Drift); `axiom:bk4_membrane_coupling_response` (Membrane Coupling Response); `corollary:bk8_projective_drift` (Projective Drift Duality); `corollary:bk9_selfreferential_capacity` (Self-Referential Capacity); `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport); `definition:bk1_horizon_structure` (Horizon Structure); `definition:bk1_minimal_linear_ps_model` (Minimal Linear PS-Model Witness); `definition:bk1_newtonian_category_error` (Newtonian Category Error); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_hypothesis` (Symbolic Hypothesis); `definition:bk3_symbolic_membrane` (Symbolic Membrane); `definition:bk4_fuzzy_divergence_operator` (Fuzzy Divergence Operator); `definition:bk4_order_parameter` (Order Parameter); `definition:bk4_substituted_drift_field` (Substituted Drift Field); `definition:bk4_symbolic_emergence` (Symbolic Emergence); `definition:bk4_symbolic_memory_distortion` (Symbolic Memory Distortion); `definition:bk4_symbolic_spinor_bundle` (Recursive Identity Bundle); `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk5_reflective_drift_coupling_tensor` (Reflective-Drift Coupling Tensor); `definition:bk5_symbolic_metabolism` (Symbolic Metabolism); `definition:bk6_symbolic_system` (Symbolic System); `definition:bk8_identitystability` (Stability of Symbolic Identity \identitystability); `definition:bk8_metabolic_programming_cycle` (Metabolic Programming Cycle); `definition:bk8_sr_renormalization_group` (SR Renormalization Group); `definition:bk8_structural_regulators` (Directional Drift Operators \(D_1, D_2\)); `definition:bk8_symbolic_adjacency` (Symbolic Knot); `definition:bk8_symbolic_hypothesis_manifold` (Symbolic Hypothesis Manifold); `definition:bk9_automatic_operator` (Automatic Operator $\mathcal{O}_{\text{auto}}$); `definition:bk9_generative_asymmetry` (Generative Asymmetry); `definition:bk9_orthogonal_time_component` (Orthogonal Time Component \(T_s^\perp\)); `definition:bk9_recursive_liberation` (Recursive Liberation); `demonstratio:bk4_ising_model_covenant` (The Ising Model as a Symbolic Covenant); `demonstratio:bk4_prompt_time_ttdc` (Prompt-Time Collapse in Reflective Agents); `lemma:bk1_coherence_of_proto_drift_fields` (Coherence of Proto-Drift Fields); `lemma:bk1_contradiction_resolution_principle` (Contradiction Resolution Principle); `lemma:bk1_horizon_characterization` (Horizon Characterization); `proof:bk1_constructive_resolution` (Constructive Resolution via Fiber Bundle Extension); `proof:bk1_geometric_necessity_curvature` (Quadratic Necessity from Mixed Contextual Coupling); `proof:bk1_horizon_characterization` (Effective Signature Separates the Horizon Roles); `proof:bk1_nonvacuity_minimal_linear_ps_model` (Explicit Matrix Witness); `proof:bk1_proof_of_dual_horizon_necessity_theorem` (Proof of Dual Horizon Necessity Theorem); `proof:bk1_sketch_fokker_planck_action` (Fokker--Planck from Symbolic Action via Martin--Siggia--Rose); `proof:bk2_smoothness_symbolic_hamiltonian` (Smoothness of Symbolic Hamiltonian); `proof:bk3_sketch_necessity_for_continuous_operation` (Necessity of Each Condition for Persistent Symbolic Life); `proof:bk4_bounded_expansion_under_observer_constrained_coherence` (Curvature-Bounded Expansion Rate via Grönwall); `proof:bk4_emergence_conditions` (Emergence Implies Non-Reducibility and Causal Closure); `proof:bk4_symbolic_identity_persistence` (Stability Criterion for Symbolic Identity Persistence); `proof:bk5_coherence_through_dynamic_equilibriium` (Coherence Through Dynamic Equilibrium); `proof:bk5_entropy_increase_from_drift` (Entropy Increase from Drift); `proof:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant via Balanced Memory Algebra); `proof:bk5_map_resistance_to_drift` (MAP Strategies Withstand Greater Drift); `proof:bk5_symbolic_temperature_threshold` (Symbolic Temperature Threshold for Critical Coupling); `proposition:bk5_symbolic_ess_via_map_observability_variant` (Symbolic ESS via MAP); `proposition:bk6_drift_reflection_correspondence` (Drift-Reflection Correspondence); `proposition:bk8_observer_frame_invariance` (Type II Drift Cancellation); `remark:appB_embodied_predictive_geometry` (SRV and Embodied Predictive Geometry); `remark:appD_llm_tuple_anchors` (Anchoring the LLM tuple in PS); `remark:bk3_toward_symbolic_evolution`; `remark:bk9_cross_modality_cognition` (Cross-Modality Cognition); `scholium:appC_two_horizons_co_constitutive` (The Two Horizons as Co-Constitutive); `scholium:bk1_resolution_of_continuum_disjunction` (On the Resolution of the Continuum Disjunction); `scholium:bk3_hypotheses_as_cognitive_membranes` (Hypotheses as Cognitive Membranes); `scholium:bk4_fuzzy_exponential_growth` (Fuzzy Growth Constraints); `scholium:bk4_irreversibility_as_trace` (Irreversibility as Symbolic Trace); `scholium:bk4_meaning_volume` (Meaning Volume); `scholium:bk4_micro_local_vs_path_global_irreversibility` (Micro-Local and Path-Global Irreversibility); `scholium:bk4_symbolic_drift_fields` (Symbolic Drift Fields in Cognitive Systems); `scholium:bk4_towards_symbolic_equilibrium` (Towards Symbolic Equilibrium and Curvature-Limited Gravity); `scholium:bk4_ttcs_simulation_tool_use` (TTCS as Symbolic Simulation and Tool-Use); `scholium:bk4_ttcs_stochastic_operator` (TTCS as a Stochastic Symbolic Operator); `scholium:bk5_hypotheses_as_adaptive_sym` (Hypotheses as Adaptive Symbolic Manifolds); `scholium:bk7_on_symbolic_reciprocity` (On Symbolic Reciprocity); `scholium:bk8_metabolic_programming_as_proto_freedom` (Metabolic Programming as Proto-Freedom); `sec:bk1_minimal_structure_for_symbolic_emergence` (Minimal Structure for Symbolic Emergence); `sec:bk5_funadmenta_symbolicae_vitae` (Fundamenta Symbolicae Vitae); `sec:bk5_symbolic_covenants_and_mutually_assured_progress` (Symbolic Covenants and Mutually Assured Progress); `sec:bk7_meta_reflective_drift_and_emergent_symbolic_time` (Meta-Reflective Drift and Emergent Symbolic Time); `sec:bk7_pisu_universal_symbolic_uncertainty` (Principium Incertitudinis Symbolicae Universalis (PISU)); `subsec:bk1_emergence_via_paradox_resolution` (Emergence via Paradox Resolution); `subsec:bk1_motivation` (Motivation); `subsec:bk2_core_thermodynamic_quantities` (Core Thermodynamic Quantities); `subsec:bk4_foundations_symbolic_fragmentation` (Foundations of Symbolic Fragmentation); `subsec:bk4_symbolic_identity_collapse` (Symbolic Identity Collapse); `subsec:bk7_pisu_regimes` (Interpretations and Regimes); `subsec:bk7_pisu_revisited_power_uncertainty` (Principium Incertitudinis Symbolicae Universalis (PISU) Revisited); `subsec:bk7_sources_regimes_uncertainty` (Sources and Regimes of Symbolic Uncertainty); `subsec:bk9_betrayal_as_reflective_fracture` (Betrayal as Reflective Fracture); `theorem:bk1_dual_horizon_cosmogenesis` (Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos}); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity); `theorem:bk1_symbolic_emergence_theorem_thermodynamics` (Symbolic Emergence Theorem---Contextual Cross-Error); `theorem:bk3_homeostatic_reflexes` (Homeostatic Reflexes); `theorem:bk4_paradoxical_arrow_of_time` (The Paradoxical Arrow of Time); `theorem:bk4_test_time_differentiation_c` (Test-Time Differentiation Collapse); `theorem:bk8_thermodynamic_necessity_of_symbolic_metabolism` (Thermodynamic Necessity)
- Macros used: none

**Statement / Body**

Let $S$ be a symbolic manifold as defined in Def. definition:bk1_symbolic_manifold.
A drift field $D$ is a smooth vector field on $S$ such that \( D: S rightarrow TS \) assigns to each symbolic state \( s \) a preferred direction of spontaneous evolution in the absence of external constraints, the direct dynamical expression of Axiom axiom:bk1_axiomata_prima. The drift field satisfies:


- Smoothness: \( D in C^infty(S, TS) \)

- Non-degeneracy: \( D(s) neq 0 \) for all \( s \) in a dense subset of \( S \)

- Bounded divergence: \( nabla cdot D \) is locally bounded

**Verbatim LaTeX Body**

```latex
\begin{definition}[Drift Field]
\label{definition:bk1_drift_field}
Let $\mathcal{S}$ be a symbolic manifold as defined in Def.~\ref{definition:bk1_symbolic_manifold}.
A drift field $D$ is a smooth vector field on $\mathcal{S}$ such that \( D: \mathcal{S} \rightarrow T\mathcal{S} \) assigns to each symbolic state \( s \) a preferred direction of spontaneous evolution in the absence of external constraints, the direct dynamical expression of Axiom~\ref{axiom:bk1_axiomata_prima}. The drift field satisfies:
\begin{enumerate}
    \item Smoothness: \( D \in C^\infty(\mathcal{S}, T\mathcal{S}) \)
    \item Non-degeneracy: \( D(s) \neq 0 \) for all \( s \) in a dense subset of \( \mathcal{S} \)
    \item Bounded divergence: \( \nabla \cdot D \) is locally bounded
\end{enumerate}
\end{definition}
```

### Reflection Operator (`definition:bk1_reflection_operator`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1209`

- Proof status: `definitional`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `definition:bk1_drift_field` (Drift Field); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin); `definition:bk1_drift_field` (Drift Field); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `assumption:appB_srv_dissipativity` (SRV as a Stable Dissipative Descent); `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `axiom:bk8_curvature_transformation` (Symbolic Cognition Cycle); `corollary:bk1_fixed_point` (Reflective Fixed Locus); `corollary:bk8_projective_drift` (Projective Drift Duality); `corollary:bk9_selfreferential_capacity` (Self-Referential Capacity); `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport); `definition:bk1_minimal_linear_ps_model` (Minimal Linear PS-Model Witness); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_spinor_like_structure` (Spinor-Like Symbolic Structure); `definition:bk1_symbolic_hypothesis` (Symbolic Hypothesis); `definition:bk2_symbolic_hamiltonian` (Symbolic Hamiltonian); `definition:bk3_symbolic_metabolism` (Symbolic Metabolism); `definition:bk4_individuated_symbolic_id` (Individuated Symbolic Identity); `definition:bk4_reflexive_operator` (Reflexive Operator); `definition:bk4_symbolic_memory_distortion` (Symbolic Memory Distortion); `definition:bk4_symbolic_spinor_bundle` (Recursive Identity Bundle); `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk5_reflective_coupling_tens` (Reflective Coupling Tensor); `definition:bk5_reflective_drift_coupling_tensor` (Reflective-Drift Coupling Tensor); `definition:bk5_symbolic_covenant` (Symbolic Covenant); `definition:bk5_symbolic_metabolism` (Symbolic Metabolism); `definition:bk6_symbolic_system` (Symbolic System); `definition:bk8_identitystability` (Stability of Symbolic Identity \identitystability); `definition:bk8_metabolic_programming_cycle` (Metabolic Programming Cycle); `definition:bk8_reflective_selection_operator` (Reflective Selection Operator); `definition:bk8_reflexive_debugging_operator` (Reflexive Debugging Operator $\mathcal{O}_{\mathrm{debug}}$); `definition:bk8_sr_renormalization_group` (SR Renormalization Group); `definition:bk8_structural_regulators` (Directional Drift Operators \(D_1, D_2\)); `definition:bk8_symbolic_adjacency` (Symbolic Knot); `definition:bk8_transform_group` (Frame Transform Group); `definition:bk9_prompt_injection_operator` (Prompt Injection Operator $\mathcal{J}$); `demonstratio:bk4_prompt_time_ttdc` (Prompt-Time Collapse in Reflective Agents); `lemma:bk1_contextual_nonseparability` (Contextual meaning is non-separable); `lemma:bk1_contradiction_resolution_principle` (Contradiction Resolution Principle); `lemma:bk1_horizon_characterization` (Horizon Characterization); `proof:bk1_horizon_characterization` (Effective Signature Separates the Horizon Roles); `proof:bk1_nonvacuity_minimal_linear_ps_model` (Explicit Matrix Witness); `proof:bk1_proof_of_dual_horizon_necessity_theorem` (Proof of Dual Horizon Necessity Theorem); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `proof:bk2_smoothness_symbolic_hamiltonian` (Smoothness of Symbolic Hamiltonian); `proof:bk4_fragmentation_identity_stability` (Fragmentation Violates Symbolic Identity Stability); `proof:bk4_persistence_reflection_noncommutativity` (Non-Commutativity of Persistence and Reflection); `proof:bk4_repair_reconnects_fragmentation` (Repair Trajectories Reconnect Fragmented Symbolic Regions); `proof:bk5_coherence_through_dynamic_equilibriium` (Coherence Through Dynamic Equilibrium); `proof:bk5_entropy_increase_from_drift` (Entropy Increase from Drift); `proof:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant via Balanced Memory Algebra); `proof:bk6_symbolic_fokker_planck_bifurcation` (Fokker--Planck Correspondence at Bifurcation); `proposition:bk1_the_operators_lambda_and_lambda` (Fundamental Operators as Bounded Symbolic Approximations); `proposition:bk6_drift_reflection_correspondence` (Drift-Reflection Correspondence); `proposition:bk7_stabilization_as_orbit_limit` (State-level stabilization is the orbit limit of reflection); `remark:appB_embodied_predictive_geometry` (SRV and Embodied Predictive Geometry); `remark:appD_llm_tuple_anchors` (Anchoring the LLM tuple in PS); `remark:bk3_toward_symbolic_evolution`; `remark:bk7_unnamed_remark_05`; `remark:bk9_recursive_agency` (Recursive Agency); `scholium:appB_synthetic_resolution` (B.6 Scholium: The Synthetic Resolution); `scholium:appC_time_as_memory` (Time as the Accumulation of Memory); `scholium:bk1_resolution_of_continuum_disjunction` (On the Resolution of the Continuum Disjunction); `scholium:bk4_clifford_correspondence` (Flat-Space Clifford Correspondence); `scholium:bk4_irreversibility_as_trace` (Irreversibility as Symbolic Trace); `scholium:bk4_micro_local_vs_path_global_irreversibility` (Micro-Local and Path-Global Irreversibility); `scholium:bk4_towards_symbolic_equilibrium` (Towards Symbolic Equilibrium and Curvature-Limited Gravity); `scholium:bk4_ttcs_stochastic_operator` (TTCS as a Stochastic Symbolic Operator); `scholium:bk5_hypotheses_as_adaptive_sym` (Hypotheses as Adaptive Symbolic Manifolds); `scholium:bk9_bridge_to_history` (Bridge to History); `scholium:bk9_freedom_and_reflection`; `sec:bk1_minimal_structure_for_symbolic_emergence` (Minimal Structure for Symbolic Emergence); `sec:bk5_symbolic_covenants_and_mutually_assured_progress` (Symbolic Covenants and Mutually Assured Progress); `sec:bk7_pisu_universal_symbolic_uncertainty` (Principium Incertitudinis Symbolicae Universalis (PISU)); `subsec:bk1_motivation` (Motivation); `subsec:bk2_core_thermodynamic_quantities` (Core Thermodynamic Quantities); `subsec:bk3_preamble_to_symbiosis` (Preamble to Symbiosis); `subsec:bk4_symbolic_identity_collapse` (Symbolic Identity Collapse); `subsec:bk5_symbolic_free_energy_and_stability` (Symbolic Free Energy and Stability); `subsec:bk7_pisu_axiom_statement` (Fundamental Trade-off); `subsec:bk7_sources_regimes_uncertainty` (Sources and Regimes of Symbolic Uncertainty); `theorem:bk1_constitutive_bootstrap` (Constitutive Bootstrap Theorem); `theorem:bk1_dual_horizon_cosmogenesis` (Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos}); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity); `theorem:bk1_symbolic_emergence_theorem_thermodynamics` (Symbolic Emergence Theorem---Contextual Cross-Error); `theorem:bk3_homeostatic_reflexes` (Homeostatic Reflexes); `theorem:bk4_drift_reflection_imbalance` (Drift-Reflection Imbalance); `theorem:bk4_paradoxical_arrow_of_time` (The Paradoxical Arrow of Time); `theorem:bk4_reflective_reentry` (Reflective Reentry); `theorem:bk4_test_time_differentiation_c` (Test-Time Differentiation Collapse); `theorem:bk5_symbolic_entropy_production` (Symbolic Entropy Production); `theorem:bk7_reflective_convergence_to_stable_identity` (Reflective Convergence to Stable Identity); `theorem:bk8_thermodynamic_necessity_of_symbolic_metabolism` (Thermodynamic Necessity)
- Macros used: `\reflect`

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-013`
- Witnesses: `ScholiumA.mirror_involution_ne_id_exists`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Witnesses existence of a concrete inner-product-preserving involution on Real×Real satisfying R≠±Id, exactly the source's non-triviality clause for the mirror component; does not model the general tangent-bundle map or its relation to R_stab.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $S$ be a symbolic manifold as defined in Def. definition:bk1_symbolic_manifold.
The reflection structure is the stabilising counterpart to the drift field
(Def. definition:bk1_drift_field), encoding the capacity for
self-reference that arises necessarily from Axiom axiom:bk1_axiomata_prima.
It has two typed components:


- Mirror component: \(R_{mir}:TSrightarrow TS\) is a smooth fiber-preserving tangent map satisfying \(R_{mir}^2=Id\), \(g(R_{mir}v,R_{mir}w)=g(v,w)\), and \(R_{mir}neq pmId\). This component preserves orientation data and carries the involutive mirror structure.

- Stabilization component: \(R_{stab}:SrightarrowS\) is the state-level stabilization induced by the stage operators \(R_lambda\) of Def. definition:bk1_pre_geometric_operators_and_stages. It is idempotent on stabilized states, \(R_{stab}^2=R_{stab}\), and its fixed locus represents reflective closure.

The symbol \(R\) or \(reflect\) denotes the component determined by its domain:
tangent-level formulas use \(R_{mir}\), while state-level stabilization
and iteration use \(R_{stab}\). Metric contraction is not part of this
definition; convergence requires additional descent data.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Reflection Operator]
\label{definition:bk1_reflection_operator}
Let $\mathcal{S}$ be a symbolic manifold as defined in Def.~\ref{definition:bk1_symbolic_manifold}.
The reflection structure is the stabilising counterpart to the drift field
(Def.~\ref{definition:bk1_drift_field}), encoding the capacity for
self-reference that arises necessarily from Axiom~\ref{axiom:bk1_axiomata_prima}.
It has two typed components:
\begin{enumerate}
    \item \textbf{Mirror component:} \(R_{\mathrm{mir}}:T\mathcal{S}\rightarrow T\mathcal{S}\) is a smooth fiber-preserving tangent map satisfying \(R_{\mathrm{mir}}^2=\mathrm{Id}\), \(g(R_{\mathrm{mir}}v,R_{\mathrm{mir}}w)=g(v,w)\), and \(R_{\mathrm{mir}}\neq \pm\mathrm{Id}\). This component preserves orientation data and carries the involutive mirror structure.
    \item \textbf{Stabilization component:} \(R_{\mathrm{stab}}:\mathcal{S}\rightarrow\mathcal{S}\) is the state-level stabilization induced by the stage operators \(R_\lambda\) of Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}. It is idempotent on stabilized states, \(R_{\mathrm{stab}}^2=R_{\mathrm{stab}}\), and its fixed locus represents reflective closure.
\end{enumerate}
The symbol \(R\) or \(\reflect\) denotes the component determined by its domain:
tangent-level formulas use \(R_{\mathrm{mir}}\), while state-level stabilization
and iteration use \(R_{\mathrm{stab}}\). Metric contraction is not part of this
definition; convergence requires additional descent data.
\end{definition}
```

### Observer Horizons and Bounded Symbolic Access (`subsec:bk1_observer_horizons_bounded_access`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1229`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Observer Horizon Structure (`definition:bk1_observer_horizon_structure`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1232`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor)
- Cited by: `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_reflexive_encoding_depth` (Reflexive Encoding Depth); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_hypothesis` (Symbolic Hypothesis); `definition:bk8_sr_triplet` (SR-Triplet); `lemma:bk1_contradiction_resolution_principle` (Contradiction Resolution Principle); `proof:bk1_symbolic_irony_requires_curvature`; `proof:bk7_horizon_expansion`; `proposition:bk7_horizon_expansion` (Horizon Expansion Under Resonance); `scholium:bk5__map_as_thermodynamic_necessity` (MAP as Thermodynamic Necessity); `scholium:bk5_constant_of_becoming` (The Constant of Becoming); `theorem:bk3_criteria_persistent_symbolic_life` (Persistent Symbolic Life Criteria)
- Macros used: none

**Statement / Body**

Let $S_t$ denote the symbolic manifold at symbolic time $t$ (see Def. definition:bk1_symbolic_manifold). An observer $O$ is characterized by a dynamic horizon $H_O(t) subset S_t$, which is a smooth submanifold of codimension 1 that delimits the symbolic configurations accessible to $O$ at time $t$.

The horizon structure is characterized by:


- Intrinsic curvature tensor $K_H$ measuring the horizon's internal geometric complexity (cf. symbolic Riemann tensor, Def. definition:bk1_symbolic_riemann_tensor)

- Extrinsic curvature tensor $Omega_H$ measuring how the horizon curves within the ambient symbolic space

- Horizon evolution equation:
 \[
 frac{partial H_O}{partial t} = alpha D|_{H_O} + beta (R circ D)|_{H_O} + gamma K_H
 \]
 where:


- \( D \) is the drift field (Def. definition:bk1_drift_field)

- \( R \) is the reflection operator (Def. definition:bk1_reflection_operator)

- \( O \) is a bounded observer (Def. definition:bk1_bounded_observer)

**Verbatim LaTeX Body**

```latex
\begin{definition}[Observer Horizon Structure]
\label{definition:bk1_observer_horizon_structure}
Let $\mathcal{S}_t$ denote the symbolic manifold at symbolic time $t$ (see Def.~\ref{definition:bk1_symbolic_manifold}). An observer $\mathcal{O}$ is characterized by a dynamic horizon $H_\mathcal{O}(t) \subset \mathcal{S}_t$, which is a smooth submanifold of codimension 1 that delimits the symbolic configurations accessible to $\mathcal{O}$ at time $t$.

The horizon structure is characterized by:
\begin{itemize}
    \item Intrinsic curvature tensor $K_H$ measuring the horizon's internal geometric complexity (cf. symbolic Riemann tensor, Def.~\ref{definition:bk1_symbolic_riemann_tensor})
    \item Extrinsic curvature tensor $\Omega_H$ measuring how the horizon curves within the ambient symbolic space
    \item Horizon evolution equation:
    \[
    \frac{\partial H_\mathcal{O}}{\partial t} = \alpha D|_{H_\mathcal{O}} + \beta (R \circ D)|_{H_\mathcal{O}} + \gamma K_H
    \]
    where:
    \begin{itemize}
        \item \( D \) is the drift field (Def.~\ref{definition:bk1_drift_field})
        \item \( R \) is the reflection operator (Def.~\ref{definition:bk1_reflection_operator})
        \item \( \mathcal{O} \) is a bounded observer (Def.~\ref{definition:bk1_bounded_observer})
    \end{itemize}
\end{itemize}
\end{definition}
```

### On Hypotheses as Observer-Relative Submanifolds (`scholium:bk1_hypotheses_as_submanifolds`)

Role: `scholium` | Type: `scholium` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1253`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `scholium:bk3_hypotheses_as_cognitive_membranes` (Hypotheses as Cognitive Membranes); `scholium:bk6_hypotheses_as_regulatory_mutation_manifolds` (Hypotheses as Regulatory Mutation Manifolds); `scholium:bk7_hypotheses_as_convergent_attractor_manifolds` (Hypotheses as Convergent Attractor Manifolds)
- Macros used: none

**Statement / Body**

Within the geometric framework of symbolic emergence on the symbolic manifold $M$ (Def. definition:bk1_symbolic_manifold), a hypothesis is not an independent ontological entity but rather a projection of constraint and coherence selected by a bounded observer. This perspective dissolves the artificial separation between "objective" symbolic structures and "subjective" interpretations.

Given an observer $O$ with horizon $H_O(t)$ (Def. definition:bk1_observer_horizon_structure), a symbolic hypothesis $H_O subset S$ is a smooth submanifold (Def. definition:bk1_symbolic_manifold) encoding a locally coherent transformation class under the dynamics of drift and reflection:


- Bounded Predictive Coherence: For all \( s in H_O \), the prediction error satisfies
 \[
 \| D(s) - hat{D}_O(s) \|_g leq epsilon_O
 \]
 where \( D \) is the drift field (Def. definition:bk1_drift_field) and \( hat{D}_O \) is the observer's internal model (bounded observer framework: Def. definition:bk1_bounded_observer).


- Utility Structure: \( H_O \) supports a smooth utility function
 \[
 U_O: H_O to mathbb{R}
 \]
 encoding directional preferences.


- Reflexive Accessibility: \( H_O \) admits self-modification through bounded flows, i.e.,
 \[
 L_D H_O subset TH_O
 \]
 with reflection dynamics governed by \( R \) (Def. definition:bk1_reflection_operator).

Thus, hypotheses, priors, and belief structures are all geometric manifestations of observer limitation rather than fundamental features of symbolic reality. They exist as useful submanifolds on which bounded cognition can operate, but possess no privileged ontological status.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[On Hypotheses as Observer-Relative Submanifolds]
\label{scholium:bk1_hypotheses_as_submanifolds}
Within the geometric framework of symbolic emergence on the symbolic manifold $M$ (Def.~\ref{definition:bk1_symbolic_manifold}), a \emph{hypothesis} is not an independent ontological entity but rather a projection of constraint and coherence selected by a bounded observer. This perspective dissolves the artificial separation between "objective" symbolic structures and "subjective" interpretations.

\begin{definition}[Symbolic Hypothesis]
\label{definition:bk1_symbolic_hypothesis}
Given an observer $\mathcal{O}$ with horizon $H_\mathcal{O}(t)$ (Def.~\ref{definition:bk1_observer_horizon_structure}), a \emph{symbolic hypothesis} $\mathcal{H}_\mathcal{O} \subset \mathcal{S}$ is a smooth submanifold (Def.~\ref{definition:bk1_symbolic_manifold}) encoding a locally coherent transformation class under the dynamics of drift and reflection:
\begin{enumerate}
    \item \textbf{Bounded Predictive Coherence}: For all \( s \in \mathcal{H}_\mathcal{O} \), the prediction error satisfies
    \[
    \| D(s) - \hat{D}_\mathcal{O}(s) \|_g \leq \epsilon_\mathcal{O}
    \]
    where \( D \) is the drift field (Def.~\ref{definition:bk1_drift_field}) and \( \hat{D}_\mathcal{O} \) is the observer's internal model (bounded observer framework: Def.~\ref{definition:bk1_bounded_observer}).

    \item \textbf{Utility Structure}: \( \mathcal{H}_\mathcal{O} \) supports a smooth utility function
    \[
    U_\mathcal{O}: \mathcal{H}_\mathcal{O} \to \mathbb{R}
    \]
    encoding directional preferences.

    \item \textbf{Reflexive Accessibility}: \( \mathcal{H}_\mathcal{O} \) admits self-modification through bounded flows, i.e.,
    \[
    \mathcal{L}_D \mathcal{H}_\mathcal{O} \subset T\mathcal{H}_\mathcal{O}
    \]
    with reflection dynamics governed by \( R \) (Def.~\ref{definition:bk1_reflection_operator}).
\end{enumerate}
\end{definition}

Thus, hypotheses, priors, and belief structures are all geometric manifestations of observer limitation rather than fundamental features of symbolic reality. They exist as useful submanifolds on which bounded cognition can operate, but possess no privileged ontological status.
\end{scholium}
```

### Symbolic Hypothesis (`definition:bk1_symbolic_hypothesis`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1257`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_drift_field` (Drift Field); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_drift_field` (Drift Field); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `definition:bk8_symbolic_hypothesis_manifold` (Symbolic Hypothesis Manifold); `definition:bk8_symbolic_hypothesis_set` (Symbolic Hypothesis Set); `scholium:bk3_hypotheses_as_cognitive_membranes` (Hypotheses as Cognitive Membranes); `scholium:bk5_hypotheses_as_adaptive_sym` (Hypotheses as Adaptive Symbolic Manifolds); `subsec:appD_fep_core_resonance` (D.3.1 Core Resonance)
- Macros used: none

**Statement / Body**

Given an observer $O$ with horizon $H_O(t)$ (Def. definition:bk1_observer_horizon_structure), a symbolic hypothesis $H_O subset S$ is a smooth submanifold (Def. definition:bk1_symbolic_manifold) encoding a locally coherent transformation class under the dynamics of drift and reflection:


- Bounded Predictive Coherence: For all \( s in H_O \), the prediction error satisfies
 \[
 \| D(s) - hat{D}_O(s) \|_g leq epsilon_O
 \]
 where \( D \) is the drift field (Def. definition:bk1_drift_field) and \( hat{D}_O \) is the observer's internal model (bounded observer framework: Def. definition:bk1_bounded_observer).


- Utility Structure: \( H_O \) supports a smooth utility function
 \[
 U_O: H_O to mathbb{R}
 \]
 encoding directional preferences.


- Reflexive Accessibility: \( H_O \) admits self-modification through bounded flows, i.e.,
 \[
 L_D H_O subset TH_O
 \]
 with reflection dynamics governed by \( R \) (Def. definition:bk1_reflection_operator).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Hypothesis]
\label{definition:bk1_symbolic_hypothesis}
Given an observer $\mathcal{O}$ with horizon $H_\mathcal{O}(t)$ (Def.~\ref{definition:bk1_observer_horizon_structure}), a \emph{symbolic hypothesis} $\mathcal{H}_\mathcal{O} \subset \mathcal{S}$ is a smooth submanifold (Def.~\ref{definition:bk1_symbolic_manifold}) encoding a locally coherent transformation class under the dynamics of drift and reflection:
\begin{enumerate}
    \item \textbf{Bounded Predictive Coherence}: For all \( s \in \mathcal{H}_\mathcal{O} \), the prediction error satisfies
    \[
    \| D(s) - \hat{D}_\mathcal{O}(s) \|_g \leq \epsilon_\mathcal{O}
    \]
    where \( D \) is the drift field (Def.~\ref{definition:bk1_drift_field}) and \( \hat{D}_\mathcal{O} \) is the observer's internal model (bounded observer framework: Def.~\ref{definition:bk1_bounded_observer}).

    \item \textbf{Utility Structure}: \( \mathcal{H}_\mathcal{O} \) supports a smooth utility function
    \[
    U_\mathcal{O}: \mathcal{H}_\mathcal{O} \to \mathbb{R}
    \]
    encoding directional preferences.

    \item \textbf{Reflexive Accessibility}: \( \mathcal{H}_\mathcal{O} \) admits self-modification through bounded flows, i.e.,
    \[
    \mathcal{L}_D \mathcal{H}_\mathcal{O} \subset T\mathcal{H}_\mathcal{O}
    \]
    with reflection dynamics governed by \( R \) (Def.~\ref{definition:bk1_reflection_operator}).
\end{enumerate}
\end{definition}
```

### Dual Horizon Postulate (`axiom:bk1_dual_horizon_postulate`)

Role: `axiom` | Type: `axiom` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1284`

- Proof status: `definitional`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: `definition:bk9_structural_compassion` (Structural Compassion); `demonstratio:bk7_convergence_within_reflective_basin` (Why Descent, Not Mere Monotonicity); `scholium:bk1_resolution_of_continuum_disjunction` (On the Resolution of the Continuum Disjunction); `subsec:appD_fep_contribution_differentiation` (D.3.2 Principia Symbolica's Contribution and Differentiation)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-080`
- Witnesses: `AxiomataPrima.no_drift_no_novelty`, `AxiomataPrima.pure_drift_dissolves`, `AxiomataPrima.two_channel_sustained`
- Countermodels: none
- Conditions: face 3 consumes the guarded-process machinery (LPS-P49) and the helix kernel (LPS-P48); the metaphysical scope of a three-word axiom is not exhausted; the operational tri-face kernel is what is certified
- Formal boundary: Cognition at the intersection: both channels jointly sustain, each alone fails; curvature signs interpretive.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Consistent with Axiom axiom:bk1_axiomata_prima and the elimination structure of Thm. theorem:bk1_dual_horizon_necessity_theorem, symbolic cognition emerges at the intersection of two complementary epistemic horizons:


- A generative horizon $H_G(t)$ with positive extrinsic curvature $Omega_G > 0$, enabling symbolic novelty and divergent exploration

- A dissipative horizon $H_D(t)$ with negative extrinsic curvature $Omega_D < 0$, constraining meaning through convergent stabilization

The effective symbolic domain accessible to an observer is:
\[
D_O(t) = text{int}(H_G(t)) cap text{ext}(H_D(t))
\]

The dynamics of symbolic cognition arise from the tension between these horizons, with drift field $D$ primarily governing generative expansion and the reflected field $R circ D$ governing dissipative contraction.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Dual Horizon Postulate]
\label{axiom:bk1_dual_horizon_postulate}
Consistent with Axiom~\ref{axiom:bk1_axiomata_prima} and the elimination structure of Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem}, symbolic cognition emerges at the intersection of two complementary epistemic horizons:
\begin{itemize}
    \item A \textbf{generative horizon} $H_G(t)$ with positive extrinsic curvature $\Omega_G > 0$, enabling symbolic novelty and divergent exploration
    \item A \textbf{dissipative horizon} $H_D(t)$ with negative extrinsic curvature $\Omega_D < 0$, constraining meaning through convergent stabilization
\end{itemize}

The effective symbolic domain accessible to an observer is:
\[
\mathcal{D}_\mathcal{O}(t) = \text{int}(H_G(t)) \cap \text{ext}(H_D(t))
\]

The dynamics of symbolic cognition arise from the tension between these horizons, with drift field $D$ primarily governing generative expansion and the reflected field $R \circ D$ governing dissipative contraction.
\end{axiom}
```

### Symbolic Contradictions and Emergence Triggers (`subsec:bk1_contradictions_emergence_triggers`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1302`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Contradiction (`definition:bk1_symbolic_contradiction`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1305`

- Proof status: `definitional`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence); `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `lemma:bk1_contextual_nonseparability` (Contextual meaning is non-separable); `lemma:bk1_contradiction_resolution_principle` (Contradiction Resolution Principle); `proof:bk1_constructive_resolution` (Constructive Resolution via Fiber Bundle Extension); `proof:bk1_geometric_necessity_curvature` (Quadratic Necessity from Mixed Contextual Coupling); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-016`
- Witnesses: `ScholiumA.contradictionIntensity_eq`, `ScholiumA.contradictionIntensity_zero_of_lam_one`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: The stated 'oppositional dynamics' and 'contradiction intensity' formula are modeled as a real-number identity; the manifold/measure-theoretic overlap conditions (shared accessibility, positive-measure overlap) are not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $S$ be a symbolic manifold (Def. definition:bk1_symbolic_manifold) and let $D$ be a drift field on $S$ (Def. definition:bk1_drift_field). Let an observer $O$ define an accessible domain $D_O(t) subset S_t$ determined by a horizon structure $H_O(t)$ (Def. definition:bk1_observer_horizon_structure).

A symbolic contradiction arises when $D_O(t)$ contains overlapping regions $U, V subset D_O(t)$ such that:


- There exists a symbolic state $s in U cap V$ (shared accessibility)

- The restricted drift fields satisfy \( D|_U(s) = -lambda D|_V(s) \) for some \( lambda > 0 \) (oppositional dynamics)

- The intersection \( U cap V \) has positive measure with respect to the volume form on \( S \) (non-trivial overlap)

The contradiction intensity at \( s \) is defined as
\[
I(s) = \|D|_U(s) + D|_V(s)\|_g
\]
where \( \|cdot\|_g \) is the norm induced by the symbolic metric \( g \) on \( T_sS \).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Contradiction]
\label{definition:bk1_symbolic_contradiction}
Let $\mathcal{S}$ be a symbolic manifold (Def.~\ref{definition:bk1_symbolic_manifold}) and let $D$ be a drift field on $\mathcal{S}$ (Def.~\ref{definition:bk1_drift_field}). Let an observer $\mathcal{O}$ define an accessible domain $\mathcal{D}_\mathcal{O}(t) \subset \mathcal{S}_t$ determined by a horizon structure $H_\mathcal{O}(t)$ (Def.~\ref{definition:bk1_observer_horizon_structure}).

A \emph{symbolic contradiction} arises when $\mathcal{D}_\mathcal{O}(t)$ contains overlapping regions $U, V \subset \mathcal{D}_\mathcal{O}(t)$ such that:
\begin{enumerate}
    \item There exists a symbolic state $s \in U \cap V$ (shared accessibility)
    \item The restricted drift fields satisfy \( D|_U(s) = -\lambda D|_V(s) \) for some \( \lambda > 0 \) (oppositional dynamics)
    \item The intersection \( U \cap V \) has positive measure with respect to the volume form on \( \mathcal{S} \) (non-trivial overlap)
\end{enumerate}

The \textbf{contradiction intensity} at \( s \) is defined as
\[
\mathcal{I}(s) = \|D|_U(s) + D|_V(s)\|_g
\]
where \( \|\cdot\|_g \) is the norm induced by the symbolic metric \( g \) on \( T_s\mathcal{S} \).
\end{definition}
```

### Emergence Event (`definition:bk1_emergence_event`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1325`

- Proof status: `definitional`
- Depends on: `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor)
- Cited by: `lemma:bk1_contextual_nonseparability` (Contextual meaning is non-separable); `proof:bk1_geometric_necessity_curvature` (Quadratic Necessity from Mixed Contextual Coupling); `proof:bk1_symbolic_emergence_and_curvature`; `proof:bk1_unified_field_classification` (Fields as SRMF Boundary-Symmetry Sectors); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity); `theorem:bk1_symbolic_emergence_and_curvature` (Symbolic Emergence and Curvature); `theorem:bk1_unified_field_classification` (Unified Field Classification)
- Macros used: none

**Statement / Body**

Let $S$ be a symbolic manifold (Def. definition:bk1_symbolic_manifold) equipped with a Riemannian structure $g$ and symbolic curvature tensor (Def. definition:bk1_symbolic_riemann_tensor). Let $O$ be a bounded observer with horizon structure $H_O(t)$ (Def. definition:bk1_observer_horizon_structure), and let $D_O(t) subset S_t$ denote the observer's effective domain.

An emergence event occurs when a symbolic contradiction (Def. definition:bk1_symbolic_contradiction) triggers a qualitative transformation in the topology or geometry of $D_O(t)$. This may manifest as:


- Topological bifurcation: $D_O(t)$ splits into multiple connected components

- Dimensional expansion: Introduction of new coordinates or symbolic axes in $S$ to accommodate the contradiction

- Metric refinement: Adjustment of the Riemannian metric $g$ to resolve geometric incompatibilities

- Curvature concentration: Localized increase in sectional curvature in neighborhoods surrounding the contradiction

**Verbatim LaTeX Body**

```latex
\begin{definition}[Emergence Event]
\label{definition:bk1_emergence_event}
Let $\mathcal{S}$ be a symbolic manifold (Def.~\ref{definition:bk1_symbolic_manifold}) equipped with a Riemannian structure $g$ and symbolic curvature tensor (Def.~\ref{definition:bk1_symbolic_riemann_tensor}). Let $\mathcal{O}$ be a bounded observer with horizon structure $H_\mathcal{O}(t)$ (Def.~\ref{definition:bk1_observer_horizon_structure}), and let $\mathcal{D}_\mathcal{O}(t) \subset \mathcal{S}_t$ denote the observer's effective domain.

An \emph{emergence event} occurs when a symbolic contradiction (Def.~\ref{definition:bk1_symbolic_contradiction}) triggers a qualitative transformation in the topology or geometry of $\mathcal{D}_\mathcal{O}(t)$. This may manifest as:
\begin{enumerate}
    \item \textbf{Topological bifurcation}: $\mathcal{D}_\mathcal{O}(t)$ splits into multiple connected components
    \item \textbf{Dimensional expansion}: Introduction of new coordinates or symbolic axes in $\mathcal{S}$ to accommodate the contradiction
    \item \textbf{Metric refinement}: Adjustment of the Riemannian metric $g$ to resolve geometric incompatibilities
    \item \textbf{Curvature concentration}: Localized increase in sectional curvature in neighborhoods surrounding the contradiction
\end{enumerate}
\end{definition}
```

### Symbolic Coherence Velocity (`definition:bk1_symbolic_coherence_velocity`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1338`

- Proof status: `definitional`
- Depends on: none
- Cites: `lemma:bk1_existence_and_uniqueness_of_flow` (Existence and Uniqueness of Flow)
- Cited by: `corollary:bk4_symbolic_lightcone` (Symbolic Light-Cone); `demonstratio:bk4_symbolic_thermodynamics`; `lemma:bk4_ttie_expansion_rate` (Curvature-Bounded Expansion Rate); `proof:bk4_bounded_expansion_under_observer_constrained_coherence` (Curvature-Bounded Expansion Rate via Grönwall); `proof:bk4_symbolic_lightcone`
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-037`
- Witnesses: `ScholiumC.le_coherenceVelocity`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: Modeled directly as sSup of a set of reals; the coherence-field space M_coh and the local gradient construction nabla C on the symbolic manifold are not modeled, only the resulting supremum's upper-bound property.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The symbolic coherence velocity $c_s$ is defined as the supremum of the local coherence field gradient magnitude over the coherence manifold:
\[
c_s := sup left{ left| nabla C right| : C in M_{text{coh}} right}
\]
Here, $M_{text{coh}}$ denotes the space of symbolic coherence fields introduced in Def. definition:bk1_symbolic_coherence_velocity, and $nabla C$ represents the local coherence flow gradient in the symbolic manifold $M$ (see Lemma lemma:bk1_existence_and_uniqueness_of_flow).

This value represents the maximum rate at which coherent symbolic information may propagate under observer-bound curvature $kappa_O$ and resolution constraints $delta_O$. It provides a fundamental limit on symbolic propagation speed and will serve as the upper bound in curvature-limited expansion dynamics.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Coherence Velocity]
\label{definition:bk1_symbolic_coherence_velocity}
The \emph{symbolic coherence velocity} $c_s$ is defined as the supremum of the local coherence field gradient magnitude over the coherence manifold:
\[
c_s := \sup \left\{ \left| \nabla \mathcal{C} \right| \,:\, \mathcal{C} \in \mathcal{M}_{\text{coh}} \right\}
\]
Here, $\mathcal{M}_{\text{coh}}$ denotes the space of symbolic coherence fields introduced in Def.~\ref{definition:bk1_symbolic_coherence_velocity}, and $\nabla \mathcal{C}$ represents the local coherence flow gradient in the symbolic manifold $M$ (see Lemma~\ref{lemma:bk1_existence_and_uniqueness_of_flow}).

This value represents the maximum rate at which coherent symbolic information may propagate under observer-bound curvature $\kappa_\mathcal{O}$ and resolution constraints $\delta_\mathcal{O}$. It provides a fundamental limit on symbolic propagation speed and will serve as the upper bound in curvature-limited expansion dynamics.
\end{definition}
```

### Contradiction Resolution Principle (`lemma:bk1_contradiction_resolution_principle`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1349`

- Proof status: `proven`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `proof:bk1_constructive_resolution` (Constructive Resolution via Fiber Bundle Extension)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-073`
- Witnesses: `ScholiumDyn.extension_resolves`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: Minimal-extension existence kernel; intensity budgets open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $S$ be a symbolic manifold (Def. definition:bk1_symbolic_manifold) with bounded observer horizon structure (Def. definition:bk1_observer_horizon_structure). Let $D$ and $R$ denote the drift field (Def. definition:bk1_drift_field) and reflection operator (Def. definition:bk1_reflection_operator), respectively. Let $C = {c_1, c_2, ldots, c_k}$ be a finite set of symbolic contradictions (Def. definition:bk1_symbolic_contradiction) within the observer domain $D_O(t)$, each with intensity $I(c_i)$. Then there exists a minimal extension $S' supset S$ such that:


- All contradictions in $C$ can be simultaneously resolved

- The actions of both $D$ and $R$ extend continuously to $S'$

- The dimensional increase satisfies $dim(S') - dim(S) geq lceil log_2 |C| rceil$

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Contradiction Resolution Principle]
\label{lemma:bk1_contradiction_resolution_principle}
Let $\mathcal{S}$ be a symbolic manifold (Def.~\ref{definition:bk1_symbolic_manifold}) with bounded observer horizon structure (Def.~\ref{definition:bk1_observer_horizon_structure}). Let $D$ and $R$ denote the drift field (Def.~\ref{definition:bk1_drift_field}) and reflection operator (Def.~\ref{definition:bk1_reflection_operator}), respectively. Let $\mathcal{C} = \{c_1, c_2, \ldots, c_k\}$ be a finite set of symbolic contradictions (Def.~\ref{definition:bk1_symbolic_contradiction}) within the observer domain $\mathcal{D}_\mathcal{O}(t)$, each with intensity $\mathcal{I}(c_i)$. Then there exists a minimal extension $\mathcal{S}' \supset \mathcal{S}$ such that:
\begin{enumerate}
    \item All contradictions in $\mathcal{C}$ can be simultaneously resolved
    \item The actions of both $D$ and $R$ extend continuously to $\mathcal{S}'$
    \item The dimensional increase satisfies $\dim(\mathcal{S}') - \dim(\mathcal{S}) \geq \lceil \log_2 |\mathcal{C}| \rceil$
\end{enumerate}
\end{lemma}
```

### Constructive Resolution via Fiber Bundle Extension (`proof:bk1_constructive_resolution`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1359`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `lemma:bk1_contradiction_resolution_principle` (Contradiction Resolution Principle)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `lemma:bk1_contradiction_resolution_principle` (Contradiction Resolution Principle)
- Cited by: none
- Macros used: none

**Statement / Body**

For each contradiction $c_i in C$ (Def. definition:bk1_symbolic_contradiction), construct a local coordinate chart $U_i$ containing $c_i$ and define a fiber bundle $pi_i: E_i to U_i$ where the fiber at each point $s in U_i$ is a copy of $mathbb{R}^{n_i}$ with $n_i$ chosen to accommodate the contradiction intensity: $n_i = lceil log_2(1 + I(c_i)) rceil$.

The extended manifold $S'$ is constructed as the union $S$ (Def. definition:bk1_symbolic_manifold) $cup bigcup_{i=1}^k E_i$ with appropriate transition functions ensuring smoothness. The drift field $D$ (Def. definition:bk1_drift_field) extends to $S'$ by defining its action on fiber directions to resolve the contradictory dynamics: on fiber $pi_i^{-1}(s)$, set $D$ to be the unique vector that simultaneously satisfies the constraints from overlapping regions.

The logarithmic bound on dimension follows from the fact that each contradiction can be resolved by introducing at least one new binary choice (corresponding to one additional dimension), and $k$ contradictions require at least $lceil log_2 k rceil$ dimensions to encode all possible resolution patterns, as claimed in Lem. lemma:bk1_contradiction_resolution_principle.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Constructive Resolution via Fiber Bundle Extension]
\label{proof:bk1_constructive_resolution}
\leavevmode

For each contradiction $c_i \in \mathcal{C}$ (Def.~\ref{definition:bk1_symbolic_contradiction}), construct a local coordinate chart $U_i$ containing $c_i$ and define a fiber bundle $\pi_i: E_i \to U_i$ where the fiber at each point $s \in U_i$ is a copy of $\mathbb{R}^{n_i}$ with $n_i$ chosen to accommodate the contradiction intensity: $n_i = \lceil \log_2(1 + \mathcal{I}(c_i)) \rceil$.

The extended manifold $\mathcal{S}'$ is constructed as the union $\mathcal{S}$ (Def.~\ref{definition:bk1_symbolic_manifold}) $\cup \bigcup_{i=1}^k E_i$ with appropriate transition functions ensuring smoothness. The drift field $D$ (Def.~\ref{definition:bk1_drift_field}) extends to $\mathcal{S}'$ by defining its action on fiber directions to resolve the contradictory dynamics: on fiber $\pi_i^{-1}(s)$, set $D$ to be the unique vector that simultaneously satisfies the constraints from overlapping regions.

The logarithmic bound on dimension follows from the fact that each contradiction can be resolved by introducing at least one new binary choice (corresponding to one additional dimension), and $k$ contradictions require at least $\lceil \log_2 k \rceil$ dimensions to encode all possible resolution patterns, as claimed in Lem.~\ref{lemma:bk1_contradiction_resolution_principle}.
\end{proof}
```

### Necessity of Higher-Order Geometric Structure (`subsec:bk1_necessity_higher_order_structure`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1372`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Contextual meaning is non-separable (`lemma:bk1_contextual_nonseparability`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1375`

- Proof status: `proven`
- Depends on: `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction)
- Cites: `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction)
- Cited by: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `proof:bk1_linear_insufficiency` (Linear updates are context-free); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-017`
- Witnesses: `ScholiumA.nonseparable_of_mixedDiff_ne_zero`, `ScholiumA.separable_mixedDiff_zero`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: The mixed partial derivative D_xi D_chi U is replaced by an honest finite second-difference surrogate; this proves the intended contrapositive (nonzero difference implies non-separable) but is explicitly NOT a formalization of the derivative-based iff in the source.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Work in a chart near an accessible state $s_0$, with state coordinate $xi = s-s_0$ and
context coordinate $chi = c-c_0$ (the horizon and contradiction data of
Defs. definition:bk1_symbolic_contradiction, definition:bk1_emergence_event),
and let $U(xi,chi)$ be the smooth update residual after pure drift is
subtracted. Call the representation context-free (flat) at $s_0$ when the update is
additively separable, $U(xi,chi)=A(xi)+B(chi)$, so that the dynamical effect
$partial_xiU$ of a state change carries no dependence on the context $chi$.
Call the update contextual - the defining property of reflexive,
contradiction-driven meaning (Def. definition:bk1_reflection_operator,
Def. definition:bk1_emergence_event) - when a state change's effect is genuinely
modulated by context. Then
\[
text{contextual at } s_0 Longleftrightarrow D_xi D_chi U(0,0)neq 0,
\]
and no context-free representation can carry contextual meaning.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Contextual meaning is non-separable]
\label{lemma:bk1_contextual_nonseparability}
Work in a chart near an accessible state $s_0$, with state coordinate $\xi = s-s_0$ and
context coordinate $\chi = c-c_0$ (the horizon and contradiction data of
Defs.~\ref{definition:bk1_symbolic_contradiction}, \ref{definition:bk1_emergence_event}),
and let $\mathcal{U}(\xi,\chi)$ be the smooth update residual after pure drift is
subtracted. Call the representation \emph{context-free} (flat) at $s_0$ when the update is
additively separable, $\mathcal{U}(\xi,\chi)=A(\xi)+B(\chi)$, so that the dynamical effect
$\partial_\xi\mathcal{U}$ of a state change carries no dependence on the context $\chi$.
Call the update \emph{contextual} -- the defining property of reflexive,
contradiction-driven meaning (Def.~\ref{definition:bk1_reflection_operator},
Def.~\ref{definition:bk1_emergence_event}) -- when a state change's effect is genuinely
modulated by context. Then
\[
\text{contextual at } s_0 \quad\Longleftrightarrow\quad D_\xi D_\chi\,\mathcal{U}(0,0)\neq 0,
\]
and no context-free representation can carry contextual meaning.
\end{lemma}
```

### Separable updates are exactly the context-free ones (`proof:bk1_contextual_nonseparability`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1394`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

If $U(xi,chi)=A(xi)+B(chi)$ then $partial_xiU=A'(xi)$ carries no
$chi$-dependence, so $partial_chipartial_xiUequiv 0$ and a state change's
effect is the same in every context - the update is non-contextual. Conversely, if
$D_xi D_chiU(0,0)neq 0$ then $partial_xiU$ varies with $chi$ near
$s_0$, so $U$ admits no additive decomposition $A(xi)+B(chi)$ - any such
decomposition forces the mixed derivative to vanish identically - and the state's effect
is then genuinely context-modulated, which is contextual meaning. The two conditions
coincide. A flat representation is separable by construction, hence has
$D_xi D_chiUequiv 0$, and so cannot realize it.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Separable updates are exactly the context-free ones]
\label{proof:bk1_contextual_nonseparability}
\leavevmode
If $\mathcal{U}(\xi,\chi)=A(\xi)+B(\chi)$ then $\partial_\xi\mathcal{U}=A'(\xi)$ carries no
$\chi$-dependence, so $\partial_\chi\partial_\xi\mathcal{U}\equiv 0$ and a state change's
effect is the same in every context -- the update is non-contextual. Conversely, if
$D_\xi D_\chi\mathcal{U}(0,0)\neq 0$ then $\partial_\xi\mathcal{U}$ varies with $\chi$ near
$s_0$, so $\mathcal{U}$ admits no additive decomposition $A(\xi)+B(\chi)$ -- any such
decomposition forces the mixed derivative to vanish identically -- and the state's effect
is then genuinely context-modulated, which is contextual meaning. The two conditions
coincide. A flat representation is separable by construction, hence has
$D_\xi D_\chi\mathcal{U}\equiv 0$, and so cannot realize it.
\end{proof}
```

### Quadratic Structure Necessity (`theorem:bk1_quadratic_structure_necessity`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1408`

- Proof status: `proven`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `lemma:bk1_contextual_nonseparability` (Contextual meaning is non-separable); `theorem:bk1_constitutive_bootstrap` (Constitutive Bootstrap Theorem); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `lemma:bk1_contextual_nonseparability` (Contextual meaning is non-separable); `theorem:bk1_constitutive_bootstrap` (Constitutive Bootstrap Theorem); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `proof:bk1_linear_insufficiency` (Linear updates are context-free)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-035`
- Witnesses: `ScholiumC.crossTerm_ne_zero_exists`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: crossTerm is a discrete finite-difference surrogate for the mixed second derivative D_xi D_chi U(0,0), not the derivative itself; the local-coordinate Taylor expansion and the O(||.||^3) remainder are not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Any symbolic system $(S, D, R, H_G, H_D)$ that supports
horizon-relative novelty, reflexive identity, and contradiction-driven emergence
in the following operational sense must admit a quadratic representational
geometry: at some accessible state \(s_0\), the local update residual depends
nonseparably on both symbolic state and contextual data. More precisely, let
\[
c=(d_G,d_D,I)
\]
collect the distances to the generative and dissipative horizons and the local
contradiction intensity (Defs. definition:bk1_symbolic_contradiction,
definition:bk1_emergence_event). In local coordinates
\(xi=s-s_0\) and \(chi=c-c_0\), let
\(U(xi,chi)\) denote the residual update after subtracting the
pure drift term \(D\). If the mixed derivative
\[
D_xi D_chi U(0,0)neq 0
\]
is nonzero - equivalently, by Lemma lemma:bk1_contextual_nonseparability, if the
update is contextual at \(s_0\), so a state change's effect is genuinely modulated
by context, which is the hypothesis rather than an extra analytic assumption - then there
exists a nonzero rank-2 tensor \(Q_{s_0}\) on the combined
state-context space \(T_{s_0}Soplus C_{s_0}\) such that, to second
order,
\[
frac{ds}{dt}
=D(s)+Q_{s_0}bigl((xi,chi),(xi,chi)bigr)
+O(\|(xi,chi)\|^3).
\]
Thus the minimal local representation capable of carrying contextual emergence
contains a bilinear, hence quadratic, coupling term.

Here:


- $S$ is the symbolic manifold (Def. definition:bk1_symbolic_manifold)

- $D$ is the drift field (Def. definition:bk1_drift_field)

- $R$ is the typed reflection structure (Def. definition:bk1_reflection_operator)

- Horizon structures $H_G, H_D$ derive from the dual horizon model (Thm. theorem:bk1_dual_horizon_necessity_theorem)

- Reflexive identity is extracted from reflective closure (Thm. theorem:bk1_constitutive_bootstrap).

- Contradiction-driven emergence is formalized via emergence events (Def. definition:bk1_emergence_event)

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Quadratic Structure Necessity]
\label{theorem:bk1_quadratic_structure_necessity}
Any symbolic system $(\mathcal{S}, D, R, H_G, H_D)$ that supports
horizon-relative novelty, reflexive identity, and contradiction-driven emergence
in the following operational sense must admit a quadratic representational
geometry: at some accessible state \(s_0\), the local update residual depends
nonseparably on both symbolic state and contextual data. More precisely, let
\[
c=(d_G,d_D,\mathcal{I})
\]
collect the distances to the generative and dissipative horizons and the local
contradiction intensity (Defs.~\ref{definition:bk1_symbolic_contradiction},
\ref{definition:bk1_emergence_event}). In local coordinates
\(\xi=s-s_0\) and \(\chi=c-c_0\), let
\(\mathcal{U}(\xi,\chi)\) denote the residual update after subtracting the
pure drift term \(D\). If the mixed derivative
\[
D_\xi D_\chi \mathcal{U}(0,0)\neq 0
\]
is nonzero -- equivalently, by Lemma~\ref{lemma:bk1_contextual_nonseparability}, if the
update is \emph{contextual} at \(s_0\), so a state change's effect is genuinely modulated
by context, which is the hypothesis rather than an extra analytic assumption -- then there
exists a nonzero rank-2 tensor \(Q_{s_0}\) on the combined
state-context space \(T_{s_0}\mathcal{S}\oplus C_{s_0}\) such that, to second
order,
\[
\frac{ds}{dt}
=D(s)+Q_{s_0}\bigl((\xi,\chi),(\xi,\chi)\bigr)
+O(\|(\xi,\chi)\|^3).
\]
Thus the minimal local representation capable of carrying contextual emergence
contains a bilinear, hence quadratic, coupling term.

Here:
\begin{itemize}
    \item $\mathcal{S}$ is the symbolic manifold (Def.~\ref{definition:bk1_symbolic_manifold})
    \item $D$ is the drift field (Def.~\ref{definition:bk1_drift_field})
    \item $R$ is the typed reflection structure (Def.~\ref{definition:bk1_reflection_operator})
    \item Horizon structures $H_G, H_D$ derive from the dual horizon model (Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem})
    \item Reflexive identity is extracted from reflective closure (Thm.~\ref{theorem:bk1_constitutive_bootstrap}).
    \item Contradiction-driven emergence is formalized via emergence events (Def.~\ref{definition:bk1_emergence_event})
\end{itemize}
\end{theorem}
```

### Quadratic Necessity from Mixed Contextual Coupling (`proof:bk1_geometric_necessity_curvature`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1452`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `theorem:bk1_constitutive_bootstrap` (Constitutive Bootstrap Theorem)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `theorem:bk1_constitutive_bootstrap` (Constitutive Bootstrap Theorem)
- Cited by: none
- Macros used: none

**Statement / Body**

Step 1: Split pure drift from contextual residual.
Work in a chart near \(s_0\). The pure drift contribution is already accounted
for by \(D(s)\) (Def. definition:bk1_drift_field). The remaining update
is a smooth residual
\[
U: T_{s_0}Soplus C_{s_0}to T_{s_0}S,
\]
where \(C_{s_0}\) is spanned locally by the horizon and contradiction
coordinates \((d_G,d_D,I)\). Reflexive identity supplies stable
state coordinates through Thm. theorem:bk1_constitutive_bootstrap;
horizon-relative novelty and contradiction-driven emergence supply the
context coordinates through Defs. definition:bk1_symbolic_contradiction
and definition:bk1_emergence_event.

Step 2: Linear terms are separable.
The first-order Taylor jet of \(U\) at \((0,0)\) has the form
\[
U_1(xi,chi)=Axi+Bchi
\]
for linear maps \(A:T_{s_0}Sto T_{s_0}S\) and
\(B:C_{s_0}to T_{s_0}S\). This expression is additively separable:
state changes and context changes contribute independently. Therefore
\[
D_xi D_chi U_1(0,0)=0.
\]
It cannot realize the assumed nonzero mixed state/context sensitivity
\(D_xi D_chi U(0,0)neq 0\).

Step 3: The first possible mixed term is bilinear.
By Taylor's theorem, the second-order jet contains
\[
U_2(xi,chi)
=frac12 D_xi^2U(0,0)[xi,xi]
+D_xi D_chiU(0,0)[xi,chi]
+frac12 D_chi^2U(0,0)[chi,chi].
\]
The middle term is bilinear and is nonzero by hypothesis. Hence the minimal
local model that can represent the required contextual coupling is second
order. Equivalently, on \(T_{s_0}Soplus C_{s_0}\) it is a quadratic
form.

Step 4: Define the quadratic tensor.
Let \(z=(xi,chi)\). Define \(Q_{s_0}\) by polarization of the second-order
jet:
\[
Q_{s_0}(z,z)
:=frac12 D^2U(0,0)[z,z].
\]
Because the mixed derivative is nonzero, \(Q_{s_0}\) is nonzero and contains
the required state/context interaction. Substituting the Taylor expansion into
the local dynamics gives
\[
frac{ds}{dt}
=D(s)+Q_{s_0}(z,z)+O(\|z\|^3),
\]
which is the asserted quadratic representational geometry.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Quadratic Necessity from Mixed Contextual Coupling]
\label{proof:bk1_geometric_necessity_curvature}
\leavevmode

\textbf{Step 1: Split pure drift from contextual residual.}
Work in a chart near \(s_0\). The pure drift contribution is already accounted
for by \(D(s)\) (Def.~\ref{definition:bk1_drift_field}). The remaining update
is a smooth residual
\[
\mathcal{U}: T_{s_0}\mathcal{S}\oplus C_{s_0}\to T_{s_0}\mathcal{S},
\]
where \(C_{s_0}\) is spanned locally by the horizon and contradiction
coordinates \((d_G,d_D,\mathcal{I})\). Reflexive identity supplies stable
state coordinates through Thm.~\ref{theorem:bk1_constitutive_bootstrap};
horizon-relative novelty and contradiction-driven emergence supply the
context coordinates through Defs.~\ref{definition:bk1_symbolic_contradiction}
and \ref{definition:bk1_emergence_event}.

\textbf{Step 2: Linear terms are separable.}
The first-order Taylor jet of \(\mathcal{U}\) at \((0,0)\) has the form
\[
\mathcal{U}_1(\xi,\chi)=A\xi+B\chi
\]
for linear maps \(A:T_{s_0}\mathcal{S}\to T_{s_0}\mathcal{S}\) and
\(B:C_{s_0}\to T_{s_0}\mathcal{S}\). This expression is additively separable:
state changes and context changes contribute independently. Therefore
\[
D_\xi D_\chi \mathcal{U}_1(0,0)=0.
\]
It cannot realize the assumed nonzero mixed state/context sensitivity
\(D_\xi D_\chi \mathcal{U}(0,0)\neq 0\).

\textbf{Step 3: The first possible mixed term is bilinear.}
By Taylor's theorem, the second-order jet contains
\[
\mathcal{U}_2(\xi,\chi)
=\frac12 D_\xi^2\mathcal{U}(0,0)[\xi,\xi]
+D_\xi D_\chi\mathcal{U}(0,0)[\xi,\chi]
+\frac12 D_\chi^2\mathcal{U}(0,0)[\chi,\chi].
\]
The middle term is bilinear and is nonzero by hypothesis. Hence the minimal
local model that can represent the required contextual coupling is second
order. Equivalently, on \(T_{s_0}\mathcal{S}\oplus C_{s_0}\) it is a quadratic
form.

\textbf{Step 4: Define the quadratic tensor.}
Let \(z=(\xi,\chi)\). Define \(Q_{s_0}\) by polarization of the second-order
jet:
\[
Q_{s_0}(z,z)
:=\frac12 D^2\mathcal{U}(0,0)[z,z].
\]
Because the mixed derivative is nonzero, \(Q_{s_0}\) is nonzero and contains
the required state/context interaction. Substituting the Taylor expansion into
the local dynamics gives
\[
\frac{ds}{dt}
=D(s)+Q_{s_0}(z,z)+O(\|z\|^3),
\]
which is the asserted quadratic representational geometry.
\end{proof}
```

### Linear Insufficiency (`corollary:bk1_linear_insufficiency`)

Role: `corollary` | Type: `corollary` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1538`

- Proof status: `proven`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `lemma:bk1_contextual_nonseparability` (Contextual meaning is non-separable); `theorem:bk1_constitutive_bootstrap` (Constitutive Bootstrap Theorem); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin); `theorem:bk1_constitutive_bootstrap` (Constitutive Bootstrap Theorem)
- Cited by: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `proof:bk1_limitation_linear_reflexive_maps` (Linear Coherence Cannot Move Its Own Fixed Structure); `proposition:bk1_limitation_linear_reflexive_maps` (Limitation of Linear Reflexive Maps); `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-036`
- Witnesses: `ScholiumC.crossTerm_separable_eq_zero`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: Only the algebraic fact that additively separable updates have zero cross-difference is modeled; the narrative conclusion 'linear systems reduce to superposed independent modes' is not itself a formal claim here.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

In the setting of Axiom axiom:bk1_axiomata_prima and Thm. theorem:bk1_constitutive_bootstrap, linear symbolic systems cannot support genuine emergence. Purely linear dynamics reduce to superposed independent modes and preclude the contextual coupling required for symbolic meaning.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Linear Insufficiency]
\label{corollary:bk1_linear_insufficiency}
In the setting of Axiom~\ref{axiom:bk1_axiomata_prima} and Thm.~\ref{theorem:bk1_constitutive_bootstrap}, linear symbolic systems cannot support genuine emergence. Purely linear dynamics reduce to superposed independent modes and preclude the contextual coupling required for symbolic meaning.
\end{corollary}
```

### Linear updates are context-free (`proof:bk1_linear_insufficiency`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1543`

- Proof status: `not_applicable`
- Depends on: `lemma:bk1_contextual_nonseparability` (Contextual meaning is non-separable); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity)
- Cites: `lemma:bk1_contextual_nonseparability` (Contextual meaning is non-separable); `sec:bk1_quadratic_sufficiency_and_symbolic_curvature` (Quadratic Sufficiency and Symbolic Curvature); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity)
- Cited by: none
- Macros used: none

**Statement / Body**

A linear update is additively separable, $U(xi,chi)=Axi+Bchi$, so its mixed
state-context derivative vanishes identically, $D_xi D_chiUequiv 0$; by
Lemma lemma:bk1_contextual_nonseparability it is therefore context-free and cannot
carry contextual meaning. By Thm. theorem:bk1_quadratic_structure_necessity the
minimal representation that can is the bilinear coupling term - nonzero symbolic
curvature. The failure is thus structural, a vanishing mixed second derivative, not a
shortfall of parameters.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Linear updates are context-free]
\label{proof:bk1_linear_insufficiency}
\leavevmode
A linear update is additively separable, $\mathcal{U}(\xi,\chi)=A\xi+B\chi$, so its mixed
state--context derivative vanishes identically, $D_\xi D_\chi\mathcal{U}\equiv 0$; by
Lemma~\ref{lemma:bk1_contextual_nonseparability} it is therefore context-free and cannot
carry contextual meaning. By Thm.~\ref{theorem:bk1_quadratic_structure_necessity} the
minimal representation that can is the bilinear coupling term -- nonzero symbolic
curvature. The failure is thus structural, a vanishing mixed second derivative, not a
shortfall of parameters.
\end{proof}
```

### Reflexivity Requires Quadratic Framing (`theorem:bk1_reflexivity_quadratic`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1561`

- Proof status: `argued_inline`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `corollary:bk1_linear_insufficiency` (Linear Insufficiency)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin); `corollary:bk1_linear_insufficiency` (Linear Insufficiency)
- Cited by: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_symbolic_coupling_basis` (Symbolic Coupling (Basis Decomposition)); `proof:bk1_bridge_to_geometry` (Quadratic Coupling Gives the Local Metric); `proof:bk1_linear_context_independence` (Linearity Has No Mixed Context Term); `proposition:bk1_bridge_to_geometry` (The Bridge to Geometry)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-022`
- Witnesses: `ScholiumA.linear_double`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Only the proof sketch's stated algebraic premise L(x+x)=2*L(x) is proved; the informal conclusion that this prevents self-reference/context-dependence is a narrative jump and is not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Any symbolic system $S$ capable of robust self-reference and context-dependent meaning cannot be governed by purely linear operators (cf. Cor. corollary:bk1_linear_insufficiency, Axiom axiom:bk1_axiomata_prima).

Proof Sketch:
Consider a hypothetical linear symbolic system with operator $L$ satisfying:

L(alpha x + beta y) = alpha L(x) + beta L(y) forall alpha, beta in mathbb{R}, x, y in S

Self-Reference Impossibility: For self-reference, we require $L(x)$ to depend on $x$'s relationship to $x$ itself. But linearity forces:

L(x + x) = 2L(x)

This prohibits the system from distinguishing between "symbol $x$ appearing twice" versus "symbol $x$ in self-reference." Linear systems cannot encode the difference between repetition and reflexivity.

Context-Dependency Impossibility: Context-sensitivity requires that the meaning of symbol $x$ changes based on its symbolic environment. But linearity mandates:

L(x text{ in context } A) + L(x text{ in context } B) = L(x text{ in contexts } A + B)

This linear superposition principle destroys contextual meaning—the system cannot distinguish different symbolic environments.

Cross-Field Manifestations:

- quant-ph: Quantum entanglement requires bilinear forms $langle psi_1 | hat{O} | psi_2 rangle$—linear operators cannot capture non-local correlations

- math-ph: Riemann curvature tensor $R_{ijkl}$ is quadratic in connection coefficients—linear geometry is necessarily flat

- hep-th: Gauge field interactions $F_{munu} F^{munu}$ are quadratic—linear field theories have no self-interaction

- cs.LG: Universal approximation requires non-linear activations—linear networks collapse to single-layer computation

- cond-mat.stat-mech: Phase transitions require non-linear order parameter coupling $phi^4$ terms—linear models show no criticality

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Reflexivity Requires Quadratic Framing]
\label{theorem:bk1_reflexivity_quadratic}
Any symbolic system $\mathcal{S}$ capable of robust self-reference and context-dependent meaning cannot be governed by purely linear operators (cf.~Cor.~\ref{corollary:bk1_linear_insufficiency}, Axiom~\ref{axiom:bk1_axiomata_prima}).

\textbf{Proof Sketch:}
Consider a hypothetical linear symbolic system with operator $\mathcal{L}$ satisfying:
\begin{align}
\mathcal{L}(\alpha x + \beta y) = \alpha \mathcal{L}(x) + \beta \mathcal{L}(y) \quad \forall \alpha, \beta \in \mathbb{R}, \, x, y \in \mathcal{S}
\end{align}

\textbf{Self-Reference Impossibility:} For self-reference, we require $\mathcal{L}(x)$ to depend on $x$'s relationship to $x$ itself. But linearity forces:
\begin{align}
\mathcal{L}(x + x) = 2\mathcal{L}(x)
\end{align}
This prohibits the system from distinguishing between "symbol $x$ appearing twice" versus "symbol $x$ in self-reference." Linear systems cannot encode the difference between repetition and reflexivity.

\textbf{Context-Dependency Impossibility:} Context-sensitivity requires that the meaning of symbol $x$ changes based on its symbolic environment. But linearity mandates:
\begin{align}
\mathcal{L}(x \text{ in context } A) + \mathcal{L}(x \text{ in context } B) = \mathcal{L}(x \text{ in contexts } A + B)
\end{align}
This linear superposition principle destroys contextual meaning—the system cannot distinguish different symbolic environments.

\textbf{Cross-Field Manifestations:}
\begin{itemize}
\item \textbf{quant-ph}: Quantum entanglement requires bilinear forms $\langle \psi_1 | \hat{O} | \psi_2 \rangle$—linear operators cannot capture non-local correlations
\item \textbf{math-ph}: Riemann curvature tensor $R_{ijkl}$ is quadratic in connection coefficients—linear geometry is necessarily flat
\item \textbf{hep-th}: Gauge field interactions $F_{\mu\nu} F^{\mu\nu}$ are quadratic—linear field theories have no self-interaction
\item \textbf{cs.LG}: Universal approximation requires non-linear activations—linear networks collapse to single-layer computation
\item \textbf{cond-mat.stat-mech}: Phase transitions require non-linear order parameter coupling $\phi^4$ terms—linear models show no criticality
\end{itemize}
\end{theorem}
```

### Symbolic Coupling (Basis Decomposition) (`definition:bk1_symbolic_coupling_basis`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1593`

- Proof status: `definitional`
- Depends on: `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Cites: `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Cited by: `proof:bk1_bridge_to_geometry` (Quadratic Coupling Gives the Local Metric); `proposition:bk1_bridge_to_geometry` (The Bridge to Geometry)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-018`
- Witnesses: `ScholiumA.quadratic_not_linear`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Covered only via the concrete countermodel instance C(x,y)=x*y, showing this particular quadratic coupling is not a linear coupling; the general basis-decomposition definition itself is not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let ${phi_i(x)}$ be a basis of symbolic features on manifold $M$ (cf. Thm. theorem:bk1_reflexivity_quadratic). Define:

Linear Coupling:

C_{text{linear}}(x) = sum_i alpha_i phi_i(x)

Quadratic Coupling:

C_{text{quadratic}}(x) = sum_{i,j} alpha_{ij} phi_i(x) phi_j(x)

The quadratic coupling matrix $alpha_{ij}$ encodes interaction terms between symbolic features, enabling:

- Context-dependent activation: Symbol meaning depends on co-occurring symbols

- Self-referential loops: Symbols can reference their own activation states

- Emergent correlation structure: Higher-order patterns arise from pairwise interactions

Cross-Field Realizations:

- quant-ph: Density matrix $rho = sum_{ij} rho_{ij} |irangle langle j|$ with quadratic coupling $alpha_{ij} = rho_{ij}$

- math-ph: Metric tensor $g_{ij}$ defining quadratic line element $ds^2 = g_{ij} dx^i dx^j$

- hep-th: Stress-energy tensor $T_{munu}$ coupling matter to spacetime curvature quadratically

- cs.LG: Attention weights $A_{ij} = text{softmax}(Q_i K_j^T)$ creating quadratic token interactions

- cond-mat.stat-mech: Correlation function $G_{ij} = langle sigma_i sigma_j rangle$ capturing pairwise spin correlations

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Coupling (Basis Decomposition)]
\label{definition:bk1_symbolic_coupling_basis}
Let $\{\phi_i(x)\}$ be a basis of symbolic features on manifold $\mathcal{M}$ (cf.~Thm.~\ref{theorem:bk1_reflexivity_quadratic}). Define:

\textbf{Linear Coupling:}
\begin{align}
\mathcal{C}_{\text{linear}}(x) = \sum_i \alpha_i \phi_i(x)
\end{align}

\textbf{Quadratic Coupling:}
\begin{align}
\mathcal{C}_{\text{quadratic}}(x) = \sum_{i,j} \alpha_{ij} \phi_i(x) \phi_j(x)
\end{align}

The quadratic coupling matrix $\alpha_{ij}$ encodes interaction terms between symbolic features, enabling:
\begin{enumerate}
\item \textbf{Context-dependent activation}: Symbol meaning depends on co-occurring symbols
\item \textbf{Self-referential loops}: Symbols can reference their own activation states
\item \textbf{Emergent correlation structure}: Higher-order patterns arise from pairwise interactions
\end{enumerate}

\textbf{Cross-Field Realizations:}
\begin{itemize}
\item \textbf{quant-ph}: Density matrix $\rho = \sum_{ij} \rho_{ij} |i\rangle \langle j|$ with quadratic coupling $\alpha_{ij} = \rho_{ij}$
\item \textbf{math-ph}: Metric tensor $g_{ij}$ defining quadratic line element $ds^2 = g_{ij} dx^i dx^j$
\item \textbf{hep-th}: Stress-energy tensor $T_{\mu\nu}$ coupling matter to spacetime curvature quadratically
\item \textbf{cs.LG}: Attention weights $A_{ij} = \text{softmax}(Q_i K_j^T)$ creating quadratic token interactions
\item \textbf{cond-mat.stat-mech}: Correlation function $G_{ij} = \langle \sigma_i \sigma_j \rangle$ capturing pairwise spin correlations
\end{itemize}
\end{definition}
```

### The Bridge to Geometry (`proposition:bk1_bridge_to_geometry`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1624`

- Proof status: `proven`
- Depends on: `definition:bk1_symbolic_coupling_basis` (Symbolic Coupling (Basis Decomposition)); `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Cites: `definition:bk1_symbolic_coupling_basis` (Symbolic Coupling (Basis Decomposition)); `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Cited by: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-087`
- Witnesses: `ScholiumBridge.coupling_is_metric`
- Countermodels: none
- Conditions: manifold metric, exact rank bound, and the interpretive unification/primacy claims stay open per row notes
- Formal boundary: Symmetric coupling = symmetric bilinear form; the manifold metric stays open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Building on Def. definition:bk1_symbolic_coupling_basis and Thm. theorem:bk1_reflexivity_quadratic, the quadratic coupling matrix $alpha_{ij}$ from symbolic interactions is precisely the metric tensor $g_{ij}$ of the underlying symbolic manifold:

g_{ij}(x) = alpha_{ij}(x)

Justification: Both $g_{ij}$ and $alpha_{ij}$ serve identical mathematical roles:

- Symmetric bilinear forms: $g_{ij} = g_{ji}$ and $alpha_{ij} = alpha_{ji}$

- Local distance measurement: Infinitesimal symbolic "distance" between features

- Curvature generation: Non-constant coefficients create curved symbolic geometry

- Parallel transport: Define how symbolic meaning propagates across the manifold

This identification transforms abstract "symbolic interactions" into concrete geometric structure. The requirement for quadratic coupling in symbolic systems is mathematically identical to the requirement for a metric tensor in differential geometry.

Operational Consequence: Any computational system exhibiting context-dependent symbolic processing must implement something mathematically equivalent to a Riemannian metric. This is not a design choice but a mathematical necessity.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[The Bridge to Geometry]
\label{proposition:bk1_bridge_to_geometry}
Building on Def.~\ref{definition:bk1_symbolic_coupling_basis} and Thm.~\ref{theorem:bk1_reflexivity_quadratic}, the quadratic coupling matrix $\alpha_{ij}$ from symbolic interactions is precisely the metric tensor $g_{ij}$ of the underlying symbolic manifold:
\begin{align}
g_{ij}(x) = \alpha_{ij}(x)
\end{align}

\textbf{Justification:} Both $g_{ij}$ and $\alpha_{ij}$ serve identical mathematical roles:
\begin{enumerate}
\item \textbf{Symmetric bilinear forms}: $g_{ij} = g_{ji}$ and $\alpha_{ij} = \alpha_{ji}$
\item \textbf{Local distance measurement}: Infinitesimal symbolic "distance" between features
\item \textbf{Curvature generation}: Non-constant coefficients create curved symbolic geometry
\item \textbf{Parallel transport}: Define how symbolic meaning propagates across the manifold
\end{enumerate}

This identification transforms abstract "symbolic interactions" into concrete geometric structure. The requirement for quadratic coupling in symbolic systems is mathematically identical to the requirement for a metric tensor in differential geometry.

\textbf{Operational Consequence:} Any computational system exhibiting context-dependent symbolic processing must implement something mathematically equivalent to a Riemannian metric. This is not a design choice but a mathematical necessity.
\end{proposition}
```

### Quadratic Coupling Gives the Local Metric (`proof:bk1_bridge_to_geometry`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1643`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_coupling_basis` (Symbolic Coupling (Basis Decomposition)); `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Cites: `definition:bk1_symbolic_coupling_basis` (Symbolic Coupling (Basis Decomposition)); `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Cited by: none
- Macros used: none

**Statement / Body**

On the observer-accessible feature directions of \(M\), the matrix
\(alpha_{ij}(x)\) from Def. definition:bk1_symbolic_coupling_basis is
smooth, symmetric, and positive definite at each \(x\).

Let \(u=sum_i u^ipartial_i\) and \(v=sum_j v^jpartial_j\) be tangent
feature directions in the symbolic feature basis \({phi_i}\). The quadratic
coupling defines
\[
q_x(u,v)=sum_{i,j}alpha_{ij}(x)u^i v^j .
\]
By Metric-Admissible Coupling, \(q_x\) is a smooth symmetric positive definite
bilinear form on each observer-accessible tangent feature space. This is exactly
the local coordinate datum of a Riemannian metric: setting
\[
g_{ij}(x):=q_x(partial_i,partial_j)
\]
gives \(g_{ij}(x)=alpha_{ij}(x)\). Def. definition:bk1_symbolic_coupling_basis
therefore turns the interaction matrix required by
Thm. theorem:bk1_reflexivity_quadratic into the metric coefficients of
the symbolic manifold. The remaining geometric roles listed in the proposition
follow from this metric datum: it measures local symbolic distance, and its
variation supplies the connection and curvature through the usual differential
geometric construction.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Quadratic Coupling Gives the Local Metric]
\label{proof:bk1_bridge_to_geometry}
\leavevmode

\begin{assumption}[Metric-Admissible Coupling]
On the observer-accessible feature directions of \(\mathcal{M}\), the matrix
\(\alpha_{ij}(x)\) from Def.~\ref{definition:bk1_symbolic_coupling_basis} is
smooth, symmetric, and positive definite at each \(x\).
\end{assumption}

Let \(u=\sum_i u^i\partial_i\) and \(v=\sum_j v^j\partial_j\) be tangent
feature directions in the symbolic feature basis \(\{\phi_i\}\). The quadratic
coupling defines
\[
q_x(u,v)=\sum_{i,j}\alpha_{ij}(x)u^i v^j .
\]
By Metric-Admissible Coupling, \(q_x\) is a smooth symmetric positive definite
bilinear form on each observer-accessible tangent feature space. This is exactly
the local coordinate datum of a Riemannian metric: setting
\[
g_{ij}(x):=q_x(\partial_i,\partial_j)
\]
gives \(g_{ij}(x)=\alpha_{ij}(x)\). Def.~\ref{definition:bk1_symbolic_coupling_basis}
therefore turns the interaction matrix required by
Thm.~\ref{theorem:bk1_reflexivity_quadratic} into the metric coefficients of
the symbolic manifold. The remaining geometric roles listed in the proposition
follow from this metric datum: it measures local symbolic distance, and its
variation supplies the connection and curvature through the usual differential
geometric construction.
\end{proof}
```

### Metric-Admissible Coupling (`assumption:scholium_symbolicum.tex:1647`)

Role: `assumption` | Type: `assumption` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1647`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

On the observer-accessible feature directions of \(M\), the matrix
\(alpha_{ij}(x)\) from Def. definition:bk1_symbolic_coupling_basis is
smooth, symmetric, and positive definite at each \(x\).

**Verbatim LaTeX Body**

```latex
\begin{assumption}[Metric-Admissible Coupling]
On the observer-accessible feature directions of \(\mathcal{M}\), the matrix
\(\alpha_{ij}(x)\) from Def.~\ref{definition:bk1_symbolic_coupling_basis} is
smooth, symmetric, and positive definite at each \(x\).
\end{assumption}
```

### Semantic Non-Integrability (`axiom:bk1_semantic_non_integrability`)

Role: `axiom` | Type: `axiom` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1674`

- Proof status: `definitional`
- Depends on: none
- Cites: `definition:bk1_local_semantic_independence` (Local Semantic Independence)
- Cited by: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-052`
- Witnesses: `Atlas.path_dependent_iff_noncommuting`, `Atlas.semantic_non_integrability_witness`
- Countermodels: none
- Conditions: linear-transport model for holonomy (Christoffel/vector-field forms stay open); pair-covering as the topological-regularity stand-in (point-set topology unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: The equivalently clause proved as an iff with a Boolean witness; the manifold framing is interpretation.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

In a reflexive, context-sensitive symbolic system the meaning carried from one
context to another is path-dependent: transporting the same local meaning
between two contexts along two different routes does not in general return the
same result. Equivalently, symbolic meanings are not locally independent
in the sense of Def. definition:bk1_local_semantic_independence - the
contextual update carries a non-vanishing antisymmetric (commutator) component.
This is the single premise the curvature conclusion rests on: that context
genuinely depends on the route by which it is reached, not merely on position.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Semantic Non-Integrability]
\label{axiom:bk1_semantic_non_integrability}
In a reflexive, context-sensitive symbolic system the meaning carried from one
context to another is \emph{path-dependent}: transporting the same local meaning
between two contexts along two different routes does not in general return the
same result. Equivalently, symbolic meanings are \emph{not} locally independent
in the sense of Def.~\ref{definition:bk1_local_semantic_independence} --- the
contextual update carries a non-vanishing antisymmetric (commutator) component.
This is the single premise the curvature conclusion rests on: that context
genuinely depends on the route by which it is reached, not merely on position.
\end{axiom}
```

### Necessity of Non-Euclidean Symbolic Space (`corollary:bk1_non_euclidean_necessity`)

Role: `corollary` | Type: `corollary` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1686`

- Proof status: `argued_inline`
- Depends on: `axiom:bk1_semantic_non_integrability` (Semantic Non-Integrability); `corollary:bk1_linear_insufficiency` (Linear Insufficiency); `lemma:bk1_contextual_nonseparability` (Contextual meaning is non-separable); `proposition:bk1_bridge_to_geometry` (The Bridge to Geometry); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity); `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Cites: `axiom:bk1_semantic_non_integrability` (Semantic Non-Integrability); `corollary:bk1_linear_insufficiency` (Linear Insufficiency); `definition:bk1_local_semantic_independence` (Local Semantic Independence); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `lemma:bk1_contextual_nonseparability` (Contextual meaning is non-separable); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `proposition:bk1_bridge_to_geometry` (The Bridge to Geometry); `proposition:bk1_curvature_semantic_entanglement` (Curvature and Semantic Entanglement); `theorem:bk1_quadratic_structure_necessity` (Quadratic Structure Necessity); `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Cited by: `abs:press` (Press Abstract (Non-specialist science readers)); `definition:bk7_symbolic_reflexive_validation_srv` (Symbolic Reflexive Validation (SRV)); `proof:bk1_minimal_quadratic_sufficiency` (Linear Coupling Cannot Support the Three Capacities); `proof:bk1_symbolic_emergence_and_curvature`; `proof:bk1_symbolic_irony_requires_curvature`; `proof:bk2_coherence_of_symbolic_therm`; `proof:bk5_coherence_through_dynamic_equilibriium` (Coherence Through Dynamic Equilibrium); `proof:bk8_no_free_projection`; `proof:bk9_curvature_resilience_bound`; `proof:bk9_isolation_dissociation_theorem`; `proposition:bk9_curvature_scarring` (Curvature Scarring and Recovery); `theorem:bk1_minimal_quadratic_sufficiency` (Minimal Quadratic Sufficiency); `theorem:bk2_coherence_of_symbolic_therm` (Coherence of Symbolic Thermodynamics); `theorem:bk3_symbiotic_curvature_and_resilience` (Symbiotic Curvature and Resilience); `theorem:bk8_no_free_projection` (No Free Projection); `theorem:bk9_isolation_dissociation_theorem` (Isolation–Dissociation Theorem (IDT))
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-056`
- Witnesses: `Atlas.non_euclidean_necessity`
- Countermodels: none
- Conditions: linear-transport model for holonomy (Christoffel/vector-field forms stay open); pair-covering as the topological-regularity stand-in (point-set topology unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Noncommuting transports force nonzero curvature at every scale; consumed premise is exactly the non-integrability axiom.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Any symbolic system exhibiting reflexivity and context-sensitivity must operate in curved symbolic space with non-zero curvature tensor $kappa_{ijkl} neq 0$.

Proof:

- By Theorem theorem:bk1_reflexivity_quadratic the system requires quadratic forms; by Proposition proposition:bk1_bridge_to_geometry - with the proven Thm. theorem:bk1_quadratic_structure_necessity and Lem. lemma:bk1_contextual_nonseparability - these are metric tensors $g_{ij}(x)$ carrying a non-separable contextual coupling.

- Reflexive context-sensitivity renders it path-dependent: by Semantic Non-Integrability (Axiom axiom:bk1_semantic_non_integrability), symbolic meanings are not locally independent (Def. definition:bk1_local_semantic_independence).

- By the proven Proposition proposition:bk1_curvature_semantic_entanglement, curvature vanishes on a neighborhood iff meanings are locally independent there. Failure of local independence therefore forces $kappa neq 0$, where $kappa$ is exactly the second-order semantic holonomy - the residue of carrying one meaning around two routes (Lem. lemma:bk1_curvature_semantic_holonomy, Def. definition:bk1_symbolic_riemann_tensor). Hence $kappa_{ijkl} neq 0$.

emph{(A position-dependent metric does not by itself imply curvature - the plane in polar coordinates has non-constant $g_{ij}$ yet $kappa equiv 0$. What forces $kappa neq 0$ is the path-dependence of semantic transport, Axiom axiom:bk1_semantic_non_integrability, not the variability of $g_{ij}$ alone.)}

Cross-Field Implications:

- quant-ph: Quantum systems with entanglement exhibit non-Euclidean state space geometry

- math-ph: Any manifold supporting non-trivial dynamics must have intrinsic curvature

- hep-th: Interacting field theories require curved spacetime or internal symmetry spaces

- cs.LG: Deep networks approximate curved decision boundaries—flat geometry cannot capture complex data

- cond-mat.stat-mech: Critical phenomena emerge from curved parameter spaces near phase transitions

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Necessity of Non-Euclidean Symbolic Space]
\label{corollary:bk1_non_euclidean_necessity}
Any symbolic system exhibiting reflexivity and context-sensitivity must operate in curved symbolic space with non-zero curvature tensor $\kappa_{ijkl} \neq 0$.

\textbf{Proof:}
\begin{enumerate}
\item By Theorem~\ref{theorem:bk1_reflexivity_quadratic} the system requires quadratic forms; by Proposition~\ref{proposition:bk1_bridge_to_geometry} --- with the proven Thm.~\ref{theorem:bk1_quadratic_structure_necessity} and Lem.~\ref{lemma:bk1_contextual_nonseparability} --- these are metric tensors $g_{ij}(x)$ carrying a non-separable contextual coupling.
\item Reflexive context-sensitivity renders it \emph{path-dependent}: by Semantic Non-Integrability (Axiom~\ref{axiom:bk1_semantic_non_integrability}), symbolic meanings are not locally independent (Def.~\ref{definition:bk1_local_semantic_independence}).
\item By the proven Proposition~\ref{proposition:bk1_curvature_semantic_entanglement}, curvature vanishes on a neighborhood \emph{iff} meanings are locally independent there. Failure of local independence therefore forces $\kappa \neq 0$, where $\kappa$ is exactly the second-order semantic holonomy --- the residue of carrying one meaning around two routes (Lem.~\ref{lemma:bk1_curvature_semantic_holonomy}, Def.~\ref{definition:bk1_symbolic_riemann_tensor}). Hence $\kappa_{ijkl} \neq 0$.
\end{enumerate}
\noindent\emph{(A position-dependent metric does not by itself imply curvature --- the plane in polar coordinates has non-constant $g_{ij}$ yet $\kappa \equiv 0$. What forces $\kappa \neq 0$ is the path-dependence of semantic transport, Axiom~\ref{axiom:bk1_semantic_non_integrability}, not the variability of $g_{ij}$ alone.)}

\textbf{Cross-Field Implications:}
\begin{itemize}
\item \textbf{quant-ph}: Quantum systems with entanglement exhibit non-Euclidean state space geometry
\item \textbf{math-ph}: Any manifold supporting non-trivial dynamics must have intrinsic curvature
\item \textbf{hep-th}: Interacting field theories require curved spacetime or internal symmetry spaces
\item \textbf{cs.LG}: Deep networks approximate curved decision boundaries—flat geometry cannot capture complex data
\item \textbf{cond-mat.stat-mech}: Critical phenomena emerge from curved parameter spaces near phase transitions
\end{itemize}
\end{corollary}
```

### Quadratic Sufficiency and Symbolic Curvature (`sec:bk1_quadratic_sufficiency_and_symbolic_curvature`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1730`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `proof:bk1_linear_insufficiency` (Linear updates are context-free)
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Categories and Reflexive Maps (`subsec:bk1_symbolic_categories_and_reflexive_maps`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1735`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Category (`definition:bk1_symbolic_category`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1738`

- Proof status: `definitional`
- Depends on: `definition:bk1_let_cats_be_the_category` (Category of Structures); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_let_cats_be_the_category` (Category of Structures); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `definition:bk1_reflexive_update_map` (Reflexive Update Map); `lemma:bk1_fixed_point_inheritance` (Fixed Point Inheritance); `proof:bk1_fixed_point_inheritance` (Conjugation Preserves Fixed Points)
- Macros used: `\catS`

**Statement / Body**

A symbolic category $S$ is the restriction of $catS$ (Def. definition:bk1_let_cats_be_the_category) to the symbolic manifold $S$ (Def. definition:bk1_symbolic_manifold), whose:


- Objects represent symbolic structures or expressions;

- Morphisms $f: X to Y$ are structure-preserving transformations between symbolic objects;

- Composition $circ$ is associative and admits identity morphisms $text{id}_X$ for each object $X$.

A morphism $f$ is linear if it preserves symbolic superposition: $f(ax + by) = af(x) + bf(y)$ for all scalars $a,b$ and symbolic expressions $x,y$ in the appropriate domain.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Category]
\label{definition:bk1_symbolic_category}
A \emph{symbolic category} $\mathcal{S}$ is the restriction of $\catS$ (Def.~\ref{definition:bk1_let_cats_be_the_category}) to the symbolic manifold $\mathcal{S}$ (Def.~\ref{definition:bk1_symbolic_manifold}), whose:
\begin{itemize}
  \item Objects represent symbolic structures or expressions;
  \item Morphisms $f: X \to Y$ are structure-preserving transformations between symbolic objects;
  \item Composition $\circ$ is associative and admits identity morphisms $\text{id}_X$ for each object $X$.
\end{itemize}
A morphism $f$ is \emph{linear} if it preserves symbolic superposition: $f(ax + by) = af(x) + bf(y)$ for all scalars $a,b$ and symbolic expressions $x,y$ in the appropriate domain.
\end{definition}
```

### Reflexive Update Map (`definition:bk1_reflexive_update_map`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1749`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_category` (Symbolic Category)
- Cites: `definition:bk1_symbolic_category` (Symbolic Category)
- Cited by: `lemma:bk1_linear_context_independence` (Context-Independence of Linear Coupling); `proof:bk1_limitation_linear_reflexive_maps` (Linear Coherence Cannot Move Its Own Fixed Structure); `proof:bk1_minimal_quadratic_sufficiency` (Linear Coupling Cannot Support the Three Capacities); `proposition:bk1_limitation_linear_reflexive_maps` (Limitation of Linear Reflexive Maps); `theorem:bk1_minimal_quadratic_sufficiency` (Minimal Quadratic Sufficiency)
- Macros used: none

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-069`
- Witnesses: `ScholiumDyn.linear_has_fixed_point`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: Definition row; self-representation clause interpretive.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A map $rho: S to S$ is reflexive if it can modify representations that include itself. Formally, $rho$ is reflexive if there exists $sigma in S$ such that $rho(sigma) = tau$ where $tau$ contains a symbolic representation of $rho$.

This definition is grounded in the symbolic category structure (Def. definition:bk1_symbolic_category), where maps and objects are both symbolic entities.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Reflexive Update Map]
\label{definition:bk1_reflexive_update_map}
A map $\rho: \mathcal{S} \to \mathcal{S}$ is \emph{reflexive} if it can modify representations that include itself. Formally, $\rho$ is reflexive if there exists $\sigma \in \mathcal{S}$ such that $\rho(\sigma) = \tau$ where $\tau$ contains a symbolic representation of $\rho$.

This definition is grounded in the symbolic category structure (Def.~\ref{definition:bk1_symbolic_category}), where maps and objects are both symbolic entities.
\end{definition}
```

### Fixed Point Inheritance (`lemma:bk1_fixed_point_inheritance`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1756`

- Proof status: `proven`
- Depends on: `definition:bk1_symbolic_category` (Symbolic Category)
- Cites: `definition:bk1_symbolic_category` (Symbolic Category)
- Cited by: `proof:bk1_limitation_linear_reflexive_maps` (Linear Coherence Cannot Move Its Own Fixed Structure)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-023`
- Witnesses: `ScholiumA.fixedPointInheritance`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Proved in the generalized (linearity-free) form: only invertibility of f is used, matching the toolchain guidance to drop unused hypotheses; f∘g∘f⁻¹ fixes f(x) given g fixes x.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $f: S to S$ be a linear morphism in the symbolic category (Def. definition:bk1_symbolic_category) and $g: S to S$ any map with fixed point $x$ (i.e., $g(x) = x$). If $f$ is invertible, then $f circ g circ f^{-1}$ has fixed point $f(x)$.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Fixed Point Inheritance]
\label{lemma:bk1_fixed_point_inheritance}
Let $f: \mathcal{S} \to \mathcal{S}$ be a linear morphism in the symbolic category (Def.~\ref{definition:bk1_symbolic_category}) and $g: \mathcal{S} \to \mathcal{S}$ any map with fixed point $x$ (i.e., $g(x) = x$). If $f$ is invertible, then $f \circ g \circ f^{-1}$ has fixed point $f(x)$.
\end{lemma}
```

### Conjugation Preserves Fixed Points (`proof:bk1_fixed_point_inheritance`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1760`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_category` (Symbolic Category)
- Cites: `definition:bk1_symbolic_category` (Symbolic Category)
- Cited by: none
- Macros used: none

**Statement / Body**

Since \(f\) is invertible, \(f^{-1}(f(x))=x\). Evaluating the conjugated map at
the transported point gives
\[
(fcirc gcirc f^{-1})(f(x))=f(g(f^{-1}(f(x))))=f(g(x)).
\]
Because \(x\) is a fixed point of \(g\), \(g(x)=x\), and therefore
\[
(fcirc gcirc f^{-1})(f(x))=f(x).
\]
Thus \(f(x)\) is a fixed point of the conjugated map. Linearity is compatible
with the symbolic-category structure of Def. definition:bk1_symbolic_category;
invertibility is the condition needed for the fixed point to be transported and
returned without loss.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Conjugation Preserves Fixed Points]
\label{proof:bk1_fixed_point_inheritance}
\leavevmode

Since \(f\) is invertible, \(f^{-1}(f(x))=x\). Evaluating the conjugated map at
the transported point gives
\[
(f\circ g\circ f^{-1})(f(x))=f(g(f^{-1}(f(x))))=f(g(x)).
\]
Because \(x\) is a fixed point of \(g\), \(g(x)=x\), and therefore
\[
(f\circ g\circ f^{-1})(f(x))=f(x).
\]
Thus \(f(x)\) is a fixed point of the conjugated map. Linearity is compatible
with the symbolic-category structure of Def.~\ref{definition:bk1_symbolic_category};
invertibility is the condition needed for the fixed point to be transported and
returned without loss.
\end{proof}
```

### Limitation of Linear Reflexive Maps (`proposition:bk1_limitation_linear_reflexive_maps`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1779`

- Proof status: `proven`
- Depends on: `corollary:bk1_linear_insufficiency` (Linear Insufficiency); `definition:bk1_reflexive_update_map` (Reflexive Update Map); `lemma:bk1_fixed_point_inheritance` (Fixed Point Inheritance)
- Cites: `corollary:bk1_linear_insufficiency` (Linear Insufficiency); `definition:bk1_reflexive_update_map` (Reflexive Update Map)
- Cited by: `proof:bk1_dual_horizon_unification_principle` (Projection Through the Dual Horizon Signature); `proof:bk1_minimal_quadratic_sufficiency` (Linear Coupling Cannot Support the Three Capacities); `theorem:bk1_dual_horizon_unification_principle` (Emergent Dual Horizon Unification Principle)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-070`
- Witnesses: `ScholiumDyn.affine_escapes_fixed_points`, `ScholiumDyn.linear_fixed_points_closed`, `ScholiumDyn.linear_has_fixed_point`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: Linear updates cannot clear or bend their fixed locus; an affine update can have none.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $S$ be a symbolic category admitting only linear morphisms. Then, in line with Cor. corollary:bk1_linear_insufficiency, no reflexive update map $rho: S to S$ (Def. definition:bk1_reflexive_update_map) can alter its own fixed point structure while preserving the category's symbolic coherence.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Limitation of Linear Reflexive Maps]
\label{proposition:bk1_limitation_linear_reflexive_maps}
Let $\mathcal{S}$ be a symbolic category admitting only linear morphisms. Then, in line with Cor.~\ref{corollary:bk1_linear_insufficiency}, no reflexive update map $\rho: \mathcal{S} \to \mathcal{S}$ (Def.~\ref{definition:bk1_reflexive_update_map}) can alter its own fixed point structure while preserving the category's symbolic coherence.
\end{proposition}
```

### Linear Coherence Cannot Move Its Own Fixed Structure (`proof:bk1_limitation_linear_reflexive_maps`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1783`

- Proof status: `not_applicable`
- Depends on: `corollary:bk1_linear_insufficiency` (Linear Insufficiency); `definition:bk1_reflexive_update_map` (Reflexive Update Map); `lemma:bk1_fixed_point_inheritance` (Fixed Point Inheritance)
- Cites: `corollary:bk1_linear_insufficiency` (Linear Insufficiency); `definition:bk1_reflexive_update_map` (Reflexive Update Map); `lemma:bk1_fixed_point_inheritance` (Fixed Point Inheritance)
- Cited by: none
- Macros used: none

**Statement / Body**

In a category admitting only linear morphisms, any coherent change of coordinates
or representation acts by linear transport. Lem. lemma:bk1_fixed_point_inheritance
shows that such transport carries fixed points by conjugation: fixed-point
structure is preserved as \(xmapsto f(x)\), not internally altered by the
linear morphism itself. A reflexive update map, however, must modify a
representation that includes the updater (Def. definition:bk1_reflexive_update_map);
changing its own fixed-point structure therefore requires a self-interaction
term rather than mere linear transport. Cor. corollary:bk1_linear_insufficiency
rules out precisely that capacity for linear systems. Hence a purely linear
symbolic category cannot support such a reflexive update while preserving
symbolic coherence.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Linear Coherence Cannot Move Its Own Fixed Structure]
\label{proof:bk1_limitation_linear_reflexive_maps}
\leavevmode

In a category admitting only linear morphisms, any coherent change of coordinates
or representation acts by linear transport. Lem.~\ref{lemma:bk1_fixed_point_inheritance}
shows that such transport carries fixed points by conjugation: fixed-point
structure is preserved as \(x\mapsto f(x)\), not internally altered by the
linear morphism itself. A reflexive update map, however, must modify a
representation that includes the updater (Def.~\ref{definition:bk1_reflexive_update_map});
changing its own fixed-point structure therefore requires a self-interaction
term rather than mere linear transport. Cor.~\ref{corollary:bk1_linear_insufficiency}
rules out precisely that capacity for linear systems. Hence a purely linear
symbolic category cannot support such a reflexive update while preserving
symbolic coherence.
\end{proof}
```

### Minimal Quadratic Sufficiency (`subsec:bk1_minimal_quadratic_sufficiency`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1800`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Manifold and Feature Maps (`definition:bk1_symbolic_manifold_feature_maps`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1803`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `definition:bk1_local_semantic_independence` (Local Semantic Independence); `definition:bk1_resolution_cost` (Resolution Cost); `definition:bk1_symbolic_connection` (Symbolic Connection); `definition:bk1_symbolic_coupling` (Symbolic Coupling); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `definition:bk6_symbolic_manifold_structure` (Symbolic Manifold Structure)
- Macros used: none

**Statement / Body**

A symbolic manifold $M$ (Def. definition:bk1_symbolic_manifold) is a smooth manifold whose points represent symbolic states. A symbolic feature map $phi: M to mathbb{R}$ extracts semantic content from symbolic states. The collection $Phi(M) = {phi_i}_{i in I}$ forms a coordinate system for the semantic content of $M$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Manifold and Feature Maps]
\label{definition:bk1_symbolic_manifold_feature_maps}
A \emph{symbolic manifold} $M$ (Def.~\ref{definition:bk1_symbolic_manifold}) is a smooth manifold whose points represent symbolic states. A \emph{symbolic feature map} $\phi: M \to \mathbb{R}$ extracts semantic content from symbolic states. The collection $\Phi(M) = \{\phi_i\}_{i \in I}$ forms a coordinate system for the semantic content of $M$.
\end{definition}
```

### Symbolic Coupling (`definition:bk1_symbolic_coupling`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1808`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_manifold_feature_maps` (Symbolic Manifold and Feature Maps)
- Cites: `definition:bk1_symbolic_manifold_feature_maps` (Symbolic Manifold and Feature Maps)
- Cited by: `definition:bk1_symbolic_connection` (Symbolic Connection); `lemma:bk1_linear_context_independence` (Context-Independence of Linear Coupling); `proof:bk1_linear_context_independence` (Linearity Has No Mixed Context Term); `proof:bk1_minimal_quadratic_sufficiency` (Linear Coupling Cannot Support the Three Capacities); `theorem:bk1_minimal_quadratic_sufficiency` (Minimal Quadratic Sufficiency)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-019`
- Witnesses: `ScholiumA.quadratic_not_linear`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Same countermodel as bk1_symbolic_coupling_basis; only the concrete linear-vs-quadratic distinction is witnessed, not the general definition over an arbitrary feature basis.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A symbolic coupling is a map $C: M to mathbb{R}$ that integrates symbolic features (Def. definition:bk1_symbolic_manifold_feature_maps). The coupling is:


- Linear if $C(x) = sum_i beta_i phi_i(x)$ for constants $beta_i$;

- Quadratic if $C(x) = sum_{i,j} alpha_{ij} phi_i(x)phi_j(x)$ where $(alpha_{ij})$ is a symmetric matrix.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Coupling]
\label{definition:bk1_symbolic_coupling}
A \emph{symbolic coupling} is a map $\mathcal{C}: M \to \mathbb{R}$ that integrates symbolic features (Def.~\ref{definition:bk1_symbolic_manifold_feature_maps}). The coupling is:
\begin{itemize}
  \item \emph{Linear} if $\mathcal{C}(x) = \sum_i \beta_i \phi_i(x)$ for constants $\beta_i$;
  \item \emph{Quadratic} if $\mathcal{C}(x) = \sum_{i,j} \alpha_{ij} \phi_i(x)\phi_j(x)$ where $(\alpha_{ij})$ is a symmetric matrix.
\end{itemize}
\end{definition}
```

### Context-Independence of Linear Coupling (`lemma:bk1_linear_context_independence`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1817`

- Proof status: `proven`
- Depends on: `definition:bk1_reflexive_update_map` (Reflexive Update Map); `definition:bk1_symbolic_coupling` (Symbolic Coupling); `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Cites: `definition:bk1_reflexive_update_map` (Reflexive Update Map); `definition:bk1_symbolic_coupling` (Symbolic Coupling)
- Cited by: `proof:bk1_minimal_quadratic_sufficiency` (Linear Coupling Cannot Support the Three Capacities)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-020`
- Witnesses: `ScholiumA.quadratic_not_linear`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: The countermodel gives one concrete instance of 'linear coupling cannot encode this quadratic coupling'; the lemma's general universal claim over all context-dependent meanings is not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Linear symbolic couplings (Def. definition:bk1_symbolic_coupling) cannot encode context-dependent meaning or self-reference (cf. Def. definition:bk1_reflexive_update_map).

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Context-Independence of Linear Coupling]
\label{lemma:bk1_linear_context_independence}
Linear symbolic couplings (Def.~\ref{definition:bk1_symbolic_coupling}) cannot encode context-dependent meaning or self-reference (cf. Def.~\ref{definition:bk1_reflexive_update_map}).
\end{lemma}
```

### Linearity Has No Mixed Context Term (`proof:bk1_linear_context_independence`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1821`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_coupling` (Symbolic Coupling); `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Cites: `definition:bk1_symbolic_coupling` (Symbolic Coupling); `theorem:bk1_reflexivity_quadratic` (Reflexivity Requires Quadratic Framing)
- Cited by: none
- Macros used: none

**Statement / Body**

Let \(C\) be linear, so
\(C(x)=sum_ibeta_iphi_i(x)\) by
Def. definition:bk1_symbolic_coupling. For symbolic states \(x_A\) and
\(x_B\) representing two contexts, linearity gives
\[
C(x_A+x_B)=C(x_A)+C(x_B).
\]
The expression contains no mixed term of the form
\(phi_i(x_A)phi_j(x_B)\), and therefore no coefficient can record how the
meaning of one feature changes in the presence of the other. But
Thm. theorem:bk1_reflexivity_quadratic identifies robust self-reference
and context-dependent meaning with exactly such quadratic interaction terms.
Thus a linear coupling can superpose contextual contributions, but it cannot
encode context-dependent meaning or self-reference.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Linearity Has No Mixed Context Term]
\label{proof:bk1_linear_context_independence}
\leavevmode

Let \(\mathcal{C}\) be linear, so
\(\mathcal{C}(x)=\sum_i\beta_i\phi_i(x)\) by
Def.~\ref{definition:bk1_symbolic_coupling}. For symbolic states \(x_A\) and
\(x_B\) representing two contexts, linearity gives
\[
\mathcal{C}(x_A+x_B)=\mathcal{C}(x_A)+\mathcal{C}(x_B).
\]
The expression contains no mixed term of the form
\(\phi_i(x_A)\phi_j(x_B)\), and therefore no coefficient can record how the
meaning of one feature changes in the presence of the other. But
Thm.~\ref{theorem:bk1_reflexivity_quadratic} identifies robust self-reference
and context-dependent meaning with exactly such quadratic interaction terms.
Thus a linear coupling can superpose contextual contributions, but it cannot
encode context-dependent meaning or self-reference.
\end{proof}
```

### Horizon Structure (`definition:bk1_horizon_structure`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1841`

- Proof status: `definitional`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `proof:bk1_minimal_quadratic_sufficiency` (Linear Coupling Cannot Support the Three Capacities); `proof:bk1_symbolic_emergence_and_curvature`; `theorem:bk1_minimal_quadratic_sufficiency` (Minimal Quadratic Sufficiency); `theorem:bk1_symbolic_emergence_and_curvature` (Symbolic Emergence and Curvature)
- Macros used: none

**Statement / Body**

A horizon structure $H$ on symbolic manifold $M$ (Def. definition:bk1_symbolic_manifold) assigns to each point $x in M$ a subspace $H_x subset T_x M$ representing the locally accessible directions of meaning evolution from state $x$, bounded by the drift field $D$ (Def. definition:bk1_drift_field).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Horizon Structure]
\label{definition:bk1_horizon_structure}
A \emph{horizon structure} $\mathcal{H}$ on symbolic manifold $M$ (Def.~\ref{definition:bk1_symbolic_manifold}) assigns to each point $x \in M$ a subspace $\mathcal{H}_x \subset T_x M$ representing the locally accessible directions of meaning evolution from state $x$, bounded by the drift field $D$ (Def.~\ref{definition:bk1_drift_field}).
\end{definition}
```

### Minimal Quadratic Sufficiency (`theorem:bk1_minimal_quadratic_sufficiency`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1846`

- Proof status: `proven`
- Depends on: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_horizon_structure` (Horizon Structure); `definition:bk1_reflexive_update_map` (Reflexive Update Map); `definition:bk1_symbolic_coupling` (Symbolic Coupling); `lemma:bk1_linear_context_independence` (Context-Independence of Linear Coupling); `proposition:bk1_limitation_linear_reflexive_maps` (Limitation of Linear Reflexive Maps)
- Cites: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_horizon_structure` (Horizon Structure); `definition:bk1_reflexive_update_map` (Reflexive Update Map); `definition:bk1_symbolic_coupling` (Symbolic Coupling)
- Cited by: none
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-021`
- Witnesses: `ScholiumA.quadratic_not_linear`
- Countermodels: none
- Conditions: curvature coupling, general minimal period, and covariant transport remain open; drift and reflection are jointly supplied and both nonidentity in the concrete witness; the reader/operator and operate action are explicit data; the process description does not enact itself; the recursive phase certificate is finite and observer-relative, not a smooth spinor bundle
- Formal boundary: Same countermodel supplies the concrete case of 'linear systems are insufficient'; the reflexivity/context-sensitivity/adaptive-stability sufficiency claims themselves are narrative and not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A symbolic system capable of:


- Reflexivity: self-modification of interpretive structures (Def. definition:bk1_reflexive_update_map),

- Context-sensitivity: horizon-relative meaning emergence (Def. definition:bk1_horizon_structure),

- Adaptive stability: robust identity maintenance under perturbation,

requires at minimum quadratic symbolic coupling (Def. definition:bk1_symbolic_coupling). Linear systems are insufficient to encode the interaction effects necessary for recursive modification, horizon dependence, and persistent symbolic identity across drift. This sufficiency condition is complemented by the necessity result: any reflexive, context-sensitive symbolic system must operate in curved (non-Euclidean) space (cf. Corollary corollary:bk1_non_euclidean_necessity).

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Minimal Quadratic Sufficiency]
\label{theorem:bk1_minimal_quadratic_sufficiency}
A symbolic system capable of:
\begin{enumerate}
  \item \emph{Reflexivity}: self-modification of interpretive structures (Def.~\ref{definition:bk1_reflexive_update_map}),
  \item \emph{Context-sensitivity}: horizon-relative meaning emergence (Def.~\ref{definition:bk1_horizon_structure}),
  \item \emph{Adaptive stability}: robust identity maintenance under perturbation,
\end{enumerate}
requires at minimum quadratic symbolic coupling (Def.~\ref{definition:bk1_symbolic_coupling}). Linear systems are insufficient to encode the interaction effects necessary for recursive modification, horizon dependence, and persistent symbolic identity across drift. This sufficiency condition is complemented by the necessity result: any reflexive, context-sensitive symbolic system must operate in curved (non-Euclidean) space (cf.~Corollary~\ref{corollary:bk1_non_euclidean_necessity}).
\end{theorem}
```

### Linear Coupling Cannot Support the Three Capacities (`proof:bk1_minimal_quadratic_sufficiency`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1856`

- Proof status: `not_applicable`
- Depends on: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_horizon_structure` (Horizon Structure); `definition:bk1_reflexive_update_map` (Reflexive Update Map); `definition:bk1_symbolic_coupling` (Symbolic Coupling); `lemma:bk1_linear_context_independence` (Context-Independence of Linear Coupling); `proposition:bk1_limitation_linear_reflexive_maps` (Limitation of Linear Reflexive Maps)
- Cites: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_horizon_structure` (Horizon Structure); `definition:bk1_reflexive_update_map` (Reflexive Update Map); `definition:bk1_symbolic_coupling` (Symbolic Coupling); `lemma:bk1_linear_context_independence` (Context-Independence of Linear Coupling); `proposition:bk1_limitation_linear_reflexive_maps` (Limitation of Linear Reflexive Maps)
- Cited by: none
- Macros used: none

**Statement / Body**

Assume, toward contradiction, that the system has the three stated capacities
while its symbolic coupling is only linear in the sense of
Def. definition:bk1_symbolic_coupling. By
Lem. lemma:bk1_linear_context_independence, a linear coupling has no mixed
context term and therefore cannot encode context-dependent meaning or
self-reference. This already contradicts the first two capacities: reflexivity
requires a self-modifying update map (Def. definition:bk1_reflexive_update_map),
and context-sensitivity requires horizon-relative variation
(Def. definition:bk1_horizon_structure).

The stability condition cannot rescue the linear case. Adaptive stability asks
that identity persist while drift changes the accessible horizon-relative
context; but Prop. proposition:bk1_limitation_linear_reflexive_maps shows
that purely linear reflexive maps cannot alter their own fixed-point structure
while preserving symbolic coherence. Thus a linear system can preserve
independent modes, but it cannot preserve a reflexively updated identity across
contextual drift. The next admissible coupling class in
Def. definition:bk1_symbolic_coupling is quadratic, with coefficients
\(alpha_{ij}\) carrying precisely the feature-feature interaction terms that
linearity lacks. Hence any system with the stated capacities requires at minimum
quadratic symbolic coupling. Cor. corollary:bk1_non_euclidean_necessity
identifies the same obstruction geometrically: reflexive context-sensitivity
forces curved, non-Euclidean symbolic space.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Linear Coupling Cannot Support the Three Capacities]
\label{proof:bk1_minimal_quadratic_sufficiency}
\leavevmode

Assume, toward contradiction, that the system has the three stated capacities
while its symbolic coupling is only linear in the sense of
Def.~\ref{definition:bk1_symbolic_coupling}. By
Lem.~\ref{lemma:bk1_linear_context_independence}, a linear coupling has no mixed
context term and therefore cannot encode context-dependent meaning or
self-reference. This already contradicts the first two capacities: reflexivity
requires a self-modifying update map (Def.~\ref{definition:bk1_reflexive_update_map}),
and context-sensitivity requires horizon-relative variation
(Def.~\ref{definition:bk1_horizon_structure}).

The stability condition cannot rescue the linear case. Adaptive stability asks
that identity persist while drift changes the accessible horizon-relative
context; but Prop.~\ref{proposition:bk1_limitation_linear_reflexive_maps} shows
that purely linear reflexive maps cannot alter their own fixed-point structure
while preserving symbolic coherence. Thus a linear system can preserve
independent modes, but it cannot preserve a reflexively updated identity across
contextual drift. The next admissible coupling class in
Def.~\ref{definition:bk1_symbolic_coupling} is quadratic, with coefficients
\(\alpha_{ij}\) carrying precisely the feature--feature interaction terms that
linearity lacks. Hence any system with the stated capacities requires at minimum
quadratic symbolic coupling. Cor.~\ref{corollary:bk1_non_euclidean_necessity}
identifies the same obstruction geometrically: reflexive context-sensitivity
forces curved, non-Euclidean symbolic space.
\end{proof}
```

### Symbolic Curvature and Geometric Structure (`subsec:bk1_symbolic_curvature_and_geometric_structure`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1885`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Connection (`definition:bk1_symbolic_connection`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1888`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_coupling` (Symbolic Coupling); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk1_symbolic_manifold_feature_maps` (Symbolic Manifold and Feature Maps)
- Cites: `definition:bk1_symbolic_coupling` (Symbolic Coupling); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk1_symbolic_manifold_feature_maps` (Symbolic Manifold and Feature Maps)
- Cited by: `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport); `definition:bk1_local_semantic_independence` (Local Semantic Independence); `definition:bk1_resolution_cost` (Resolution Cost); `definition:bk1_symbolic_field_curvature_tensor` (Symbolic Field Curvature Tensor); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `definition:bk4_symbolic_curvature` (Symbolic Curvature)
- Macros used: none

**Statement / Body**

Given a quadratic symbolic coupling
$C(x) = sum_{ij} alpha_{ij} phi_i(x)phi_j(x)$
(see definition:bk1_symbolic_coupling), induced metric
$g_{ij} = alpha_{ij}$ defines a Riemannian structure on $M$
(Def. definition:bk1_symbolic_manifold).
Here $phi_i$ are symbolic feature maps
(see definition:bk1_symbolic_manifold_feature_maps).
The corresponding Levi-Civita connection $nabla$ is the
symbolic connection, with Christoffel symbols:
\[
Gamma^k_{ij} = frac{1}{2} sum_l g^{kl} left( frac{partial g_{il}}{partial x^j} + frac{partial g_{jl}}{partial x^i} - frac{partial g_{ij}}{partial x^l} right)
\]

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Connection]
\label{definition:bk1_symbolic_connection}
\leavevmode\newline
Given a quadratic symbolic coupling
$\mathcal{C}(x) = \sum_{ij} \alpha_{ij} \phi_i(x)\phi_j(x)$
(see \ref{definition:bk1_symbolic_coupling}), induced metric
$g_{ij} = \alpha_{ij}$ defines a Riemannian structure on $M$
(Def.~\ref{definition:bk1_symbolic_manifold}).
Here $\phi_i$ are symbolic feature maps
(see \ref{definition:bk1_symbolic_manifold_feature_maps}).
The corresponding Levi-Civita connection $\nabla$ is the
\emph{symbolic connection}, with Christoffel symbols:
\[
\Gamma^k_{ij} = \frac{1}{2} \sum_l g^{kl} \left( \frac{\partial g_{il}}{\partial x^j} + \frac{\partial g_{jl}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^l} \right)
\]
\end{definition}
```

### Symbolic Riemann Curvature Tensor (`definition:bk1_symbolic_riemann_tensor`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1905`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_connection` (Symbolic Connection); `definition:bk1_symbolic_manifold_feature_maps` (Symbolic Manifold and Feature Maps)
- Cites: `definition:bk1_symbolic_connection` (Symbolic Connection); `definition:bk1_symbolic_manifold_feature_maps` (Symbolic Manifold and Feature Maps)
- Cited by: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport); `definition:bk1_effective_horizon_signature` (Effective Horizon Signature); `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `lemma:bk2_thermodynamic_consistency_hypothesis_manifolds` (Thermodynamic Consistency of Hypothesis Manifolds); `proof:bk1_curvature_semantic_holonomy` (Curvature is the second-order transport defect); `proof:bk1_dual_horizon_unification_principle` (Projection Through the Dual Horizon Signature); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `proof:bk2_thermodynamic_consistency_hypothesis_manifolds`; `proof:bk9_symbolic_masking_and_unmasking` (Symbolic Masking and Unmasking); `proposition:bk1_curvature_semantic_entanglement` (Curvature and Semantic Entanglement); `theorem:bk1_dual_horizon_cosmogenesis` (Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos}); `theorem:bk1_dual_horizon_unification_principle` (Emergent Dual Horizon Unification Principle); `theorem:bk1_symbolic_emergence_and_curvature` (Symbolic Emergence and Curvature)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-055`
- Witnesses: `Atlas.curvature_witness`, `Atlas.holonomy_eps_squared`
- Countermodels: none
- Conditions: linear-transport model for holonomy (Christoffel/vector-field forms stay open); pair-covering as the topological-regularity stand-in (point-set topology unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Discrete curvature as the commutator loop defect with a concrete nonzero witness; the Riemannian tensor stays open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The symbolic curvature tensor is the Riemann curvature tensor of the symbolic connection (see definition:bk1_symbolic_connection):
\[
kappa(X,Y)Z = nabla_X nabla_Y Z - nabla_Y nabla_X Z - nabla_{[X,Y]} Z
\]
for vector fields $X, Y, Z$ on $M$, where $nabla$ acts on the symbolic feature manifold (see definition:bk1_symbolic_manifold_feature_maps).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Riemann Curvature Tensor]
\label{definition:bk1_symbolic_riemann_tensor}
The \emph{symbolic curvature tensor} is the Riemann curvature tensor of the symbolic connection (see \ref{definition:bk1_symbolic_connection}):
\[
\kappa(X,Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X,Y]} Z
\]
for vector fields $X, Y, Z$ on $M$, where $\nabla$ acts on the symbolic feature manifold (see \ref{definition:bk1_symbolic_manifold_feature_maps}).
\end{definition}
```

### Local Semantic Independence (`definition:bk1_local_semantic_independence`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1914`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_connection` (Symbolic Connection); `definition:bk1_symbolic_manifold_feature_maps` (Symbolic Manifold and Feature Maps)
- Cites: `definition:bk1_symbolic_connection` (Symbolic Connection); `definition:bk1_symbolic_manifold_feature_maps` (Symbolic Manifold and Feature Maps)
- Cited by: `axiom:bk1_semantic_non_integrability` (Semantic Non-Integrability); `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `proof:bk1_symbolic_emergence_and_curvature`; `proposition:bk1_curvature_semantic_entanglement` (Curvature and Semantic Entanglement)
- Macros used: none

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-053`
- Witnesses: `Atlas.path_dependent_iff_noncommuting`
- Countermodels: none
- Conditions: linear-transport model for holonomy (Christoffel/vector-field forms stay open); pair-covering as the topological-regularity stand-in (point-set topology unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Independence = commuting contextual updates.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $U subset M$ be a contractible coordinate neighborhood in the symbolic
manifold (Def. definition:bk1_symbolic_manifold_feature_maps), equipped
with the symbolic connection $nabla$ of Def. definition:bk1_symbolic_connection.
For a piecewise smooth path $gamma:xto y$ in $U$, let
$P^nabla_gamma:T_xMto T_yM$ denote parallel transport by $nabla$.
Symbolic meanings are locally independent on $U$ when, for every
$x,yin U$ and every pair of paths $gamma_0,gamma_1:xto y$ in $U$,
\[
P^nabla_{gamma_0} = P^nabla_{gamma_1}.
\]
Equivalently, first-order semantic variations represented in $T_xM$ can be
transported to $T_yM$ without acquiring path-dependent contextual residue.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Local Semantic Independence]
\label{definition:bk1_local_semantic_independence}
Let $U \subset M$ be a contractible coordinate neighborhood in the symbolic
manifold (Def.~\ref{definition:bk1_symbolic_manifold_feature_maps}), equipped
with the symbolic connection $\nabla$ of Def.~\ref{definition:bk1_symbolic_connection}.
For a piecewise smooth path $\gamma:x\to y$ in $U$, let
$P^\nabla_\gamma:T_xM\to T_yM$ denote parallel transport by $\nabla$.
Symbolic meanings are \emph{locally independent on $U$} when, for every
$x,y\in U$ and every pair of paths $\gamma_0,\gamma_1:x\to y$ in $U$,
\[
P^\nabla_{\gamma_0} = P^\nabla_{\gamma_1}.
\]
Equivalently, first-order semantic variations represented in $T_xM$ can be
transported to $T_yM$ without acquiring path-dependent contextual residue.
\end{definition}
```

### Curvature as Infinitesimal Semantic Holonomy (`lemma:bk1_curvature_semantic_holonomy`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1930`

- Proof status: `proven`
- Depends on: `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor)
- Cites: none
- Cited by: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport); `proof:bk1_curvature_semantic_entanglement` (Flatness iff local semantic independence); `proof:bk1_dimensional_bounds_emergence`; `proof:bk1_operational_irony_requires_imagination` (The ironic opposition is an imaginary displacement); `proof:bk1_operational_irony_requires_reflexive_curvature` (Lift of the model-internal necessity to operational capacity); `proof:bk1_symbolic_emergence_and_curvature`; `proof:bk1_symbolic_irony_requires_curvature`
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-054`
- Witnesses: `Atlas.holonomy_eps_squared`, `Atlas.holonomy_zero_iff_commute`
- Countermodels: none
- Conditions: linear-transport model for holonomy (Christoffel/vector-field forms stay open); pair-covering as the topological-regularity stand-in (point-set topology unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Exact eps-squared route residue in the linear-transport model; parallel transport on genuine manifolds stays open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $X,Y$ be vector fields on $U$ and let $square_{epsilon}(X,Y)$ be the
infinitesimal rectangle obtained by flowing a distance $epsilon$ first along
$X$ and then along $Y$, then back along $-X$ and $-Y$. The parallel transport
around this loop satisfies
\[
P^nabla_{partialsquare_{epsilon}(X,Y)}Z
= Z + epsilon^2 kappa(X,Y)Z + O(epsilon^3).
\]
Thus $kappa(X,Y)Z$ is precisely the second-order semantic residue obtained by
transporting the same local meaning around two different infinitesimal routes.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Curvature as Infinitesimal Semantic Holonomy]
\label{lemma:bk1_curvature_semantic_holonomy}
Let $X,Y$ be vector fields on $U$ and let $\square_{\epsilon}(X,Y)$ be the
infinitesimal rectangle obtained by flowing a distance $\epsilon$ first along
$X$ and then along $Y$, then back along $-X$ and $-Y$. The parallel transport
around this loop satisfies
\[
P^\nabla_{\partial\square_{\epsilon}(X,Y)}Z
= Z + \epsilon^2 \kappa(X,Y)Z + O(\epsilon^3).
\]
Thus $\kappa(X,Y)Z$ is precisely the second-order semantic residue obtained by
transporting the same local meaning around two different infinitesimal routes.
\end{lemma}
```

### Curvature is the second-order transport defect (`proof:bk1_curvature_semantic_holonomy`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1944`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor)
- Cites: `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor)
- Cited by: none
- Macros used: none

**Statement / Body**

Parallel transport around the rectangle compares the two ordered covariant
updates $nabla_Xnabla_YZ$ and $nabla_Ynabla_XZ$. Because the closing edge of
the infinitesimal parallelogram contributes the Lie-bracket correction
$nabla_{[X,Y]}Z$, the second-order failure of the two routes to agree is
\[
nabla_Xnabla_YZ-nabla_Ynabla_XZ-nabla_{[X,Y]}Z
=kappa(X,Y)Z
\]
by Def. definition:bk1_symbolic_riemann_tensor. Taylor expansion of the
transport map around the loop gives the displayed
$epsilon^2$ term, with all remaining terms of order $O(epsilon^3)$.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Curvature is the second-order transport defect]
\label{proof:bk1_curvature_semantic_holonomy}
\leavevmode

Parallel transport around the rectangle compares the two ordered covariant
updates $\nabla_X\nabla_YZ$ and $\nabla_Y\nabla_XZ$. Because the closing edge of
the infinitesimal parallelogram contributes the Lie-bracket correction
$\nabla_{[X,Y]}Z$, the second-order failure of the two routes to agree is
\[
\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z
=\kappa(X,Y)Z
\]
by Def.~\ref{definition:bk1_symbolic_riemann_tensor}. Taylor expansion of the
transport map around the loop gives the displayed
$\epsilon^2$ term, with all remaining terms of order $O(\epsilon^3)$.
\end{proof}
```

### Curvature and Semantic Entanglement (`proposition:bk1_curvature_semantic_entanglement`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1961`

- Proof status: `proven`
- Depends on: `definition:bk1_local_semantic_independence` (Local Semantic Independence); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy)
- Cites: `definition:bk1_local_semantic_independence` (Local Semantic Independence); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor)
- Cited by: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `proof:bk1_curvature_projection_residue` (Projection residue from failed path independence); `proof:bk1_symbolic_emergence_and_curvature`; `proof:bk8_curvature_entanglement_equivalence` (Curvature Entanglement Equivalence); `proof:bk8_entanglement_as_frame_artifact` (Entanglement and Frame Artifact); `proof:bk8_flattening_decoherence_equivalence` (Decoherence as Symbolic Flattening via Curvature Flow); `proof:bk8_symbolic_curvature_and_separability` (Symbolic Curvature and Separability)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-089`
- Witnesses: `Atlas.holonomy_zero_iff_commute`
- Countermodels: none
- Conditions: linear-transport model for holonomy (Christoffel/vector-field forms stay open); pair-covering as the topological-regularity stand-in (point-set topology unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Curvature vanishes iff meanings are locally independent - exactly the flatness-iff-commuting theorem.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

On any contractible coordinate neighborhood $U subset M$, the symbolic curvature
$kappa$ of Def. definition:bk1_symbolic_riemann_tensor vanishes on $U$ if
and only if symbolic meanings are locally independent on $U$ in the sense of
Def. definition:bk1_local_semantic_independence.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Curvature and Semantic Entanglement]
\label{proposition:bk1_curvature_semantic_entanglement}
On any contractible coordinate neighborhood $U \subset M$, the symbolic curvature
$\kappa$ of Def.~\ref{definition:bk1_symbolic_riemann_tensor} vanishes on $U$ if
and only if symbolic meanings are locally independent on $U$ in the sense of
Def.~\ref{definition:bk1_local_semantic_independence}.
\end{proposition}
```

### Flatness iff local semantic independence (`proof:bk1_curvature_semantic_entanglement`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1969`

- Proof status: `not_applicable`
- Depends on: `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy)
- Cites: `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy)
- Cited by: none
- Macros used: none

**Statement / Body**

($Rightarrow$) Suppose $kappa=0$ on $U$. By
Lemma lemma:bk1_curvature_semantic_holonomy, infinitesimal transport
around every coordinate rectangle has zero second-order semantic residue. Since
$U$ is contractible, any loop in $U$ can be decomposed into such infinitesimal
rectangles. The holonomy around the whole loop is therefore trivial, so parallel
transport from $x$ to $y$ depends only on the endpoints and not on the chosen
path. Hence symbolic meanings are locally independent.

($Leftarrow$) Conversely, suppose symbolic meanings are locally independent on
$U$. Then the transport around every sufficiently small coordinate rectangle is
the identity. Applying Lemma lemma:bk1_curvature_semantic_holonomy, the
coefficient of the $epsilon^2$ term must vanish for all vector fields $X,Y,Z$:
\[
kappa(X,Y)Z=0.
\]
Thus $kappa=0$ on $U$.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Flatness iff local semantic independence]
\label{proof:bk1_curvature_semantic_entanglement}
\leavevmode

($\Rightarrow$) Suppose $\kappa=0$ on $U$. By
Lemma~\ref{lemma:bk1_curvature_semantic_holonomy}, infinitesimal transport
around every coordinate rectangle has zero second-order semantic residue. Since
$U$ is contractible, any loop in $U$ can be decomposed into such infinitesimal
rectangles. The holonomy around the whole loop is therefore trivial, so parallel
transport from $x$ to $y$ depends only on the endpoints and not on the chosen
path. Hence symbolic meanings are locally independent.

($\Leftarrow$) Conversely, suppose symbolic meanings are locally independent on
$U$. Then the transport around every sufficiently small coordinate rectangle is
the identity. Applying Lemma~\ref{lemma:bk1_curvature_semantic_holonomy}, the
coefficient of the $\epsilon^2$ term must vanish for all vector fields $X,Y,Z$:
\[
\kappa(X,Y)Z=0.
\]
Thus $\kappa=0$ on $U$.
\end{proof}
```

### Curvature Residue under Non-Expressive Projection (`corollary:bk1_curvature_projection_residue`)

Role: `corollary` | Type: `corollary` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:1991`

- Proof status: `proven`
- Depends on: `proposition:bk1_curvature_semantic_entanglement` (Curvature and Semantic Entanglement)
- Cites: none
- Cited by: `proof:bk8_curvature_entanglement_equivalence` (Curvature Entanglement Equivalence); `proof:bk8_entanglement_as_frame_artifact` (Entanglement and Frame Artifact)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-090`
- Witnesses: `Atlas.non_euclidean_necessity`
- Countermodels: none
- Conditions: linear-transport model for holonomy (Christoffel/vector-field forms stay open); pair-covering as the topological-regularity stand-in (point-set topology unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Nonzero curvature forces a frame-artifact residue - the non-Euclidean necessity kernel.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $Pi_F:Mto F$ be an observer-frame projection whose target frame $F$ treats
semantic transport as path-independent on $Pi_F(U)$. If $kappaneq 0$ on $U$,
then there exist paths $gamma_0,gamma_1:xto y$ in $U$ and a semantic
variation $Zin T_xM$ such that
\[
Pi_F(P^nabla_{gamma_0}Z) neq Pi_F(P^nabla_{gamma_1}Z)
\]
or else the projection discards the curvature residue. In either case, the
projection represents curved semantic coupling as a frame artifact: either a
visible non-factorizable residual or an information loss.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Curvature Residue under Non-Expressive Projection]
\label{corollary:bk1_curvature_projection_residue}
Let $\Pi_F:M\to F$ be an observer-frame projection whose target frame $F$ treats
semantic transport as path-independent on $\Pi_F(U)$. If $\kappa\neq 0$ on $U$,
then there exist paths $\gamma_0,\gamma_1:x\to y$ in $U$ and a semantic
variation $Z\in T_xM$ such that
\[
\Pi_F(P^\nabla_{\gamma_0}Z) \neq \Pi_F(P^\nabla_{\gamma_1}Z)
\]
or else the projection discards the curvature residue. In either case, the
projection represents curved semantic coupling as a frame artifact: either a
visible non-factorizable residual or an information loss.
\end{corollary}
```

### Projection residue from failed path independence (`proof:bk1_curvature_projection_residue`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2005`

- Proof status: `not_applicable`
- Depends on: `proposition:bk1_curvature_semantic_entanglement` (Curvature and Semantic Entanglement)
- Cites: `proposition:bk1_curvature_semantic_entanglement` (Curvature and Semantic Entanglement)
- Cited by: none
- Macros used: none

**Statement / Body**

If $kappaneq 0$ on $U$, Prop. proposition:bk1_curvature_semantic_entanglement
implies that local semantic independence fails. Hence some pair of paths
$gamma_0,gamma_1:xto y$ and some $Zin T_xM$ satisfy
$P^nabla_{gamma_0}Zneq P^nabla_{gamma_1}Z$. A frame $F$ that assumes
path-independent semantic transport has no intrinsic curvature coordinate in
which to store this difference. Therefore the projected images either remain
distinct as an observable residual, or they are identified by $Pi_F$, in which
case the curvature information has been discarded. This is the projection
mechanism later read as frame artifact in Book VIII.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Projection residue from failed path independence]
\label{proof:bk1_curvature_projection_residue}
\leavevmode

If $\kappa\neq 0$ on $U$, Prop.~\ref{proposition:bk1_curvature_semantic_entanglement}
implies that local semantic independence fails. Hence some pair of paths
$\gamma_0,\gamma_1:x\to y$ and some $Z\in T_xM$ satisfy
$P^\nabla_{\gamma_0}Z\neq P^\nabla_{\gamma_1}Z$. A frame $F$ that assumes
path-independent semantic transport has no intrinsic curvature coordinate in
which to store this difference. Therefore the projected images either remain
distinct as an observable residual, or they are identified by $\Pi_F$, in which
case the curvature information has been discarded. This is the projection
mechanism later read as frame artifact in Book VIII.
\end{proof}
```

### Resolution Cost (`definition:bk1_resolution_cost`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2020`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_connection` (Symbolic Connection); `definition:bk1_symbolic_manifold_feature_maps` (Symbolic Manifold and Feature Maps)
- Cites: `definition:bk1_symbolic_connection` (Symbolic Connection); `definition:bk1_symbolic_manifold_feature_maps` (Symbolic Manifold and Feature Maps)
- Cited by: `axiom:bk4_refinement_contraction` (Refinement Contraction Axiom)
- Macros used: `\reflect`

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-064`
- Witnesses: `ScholiumDyn.resCost_self`, `ScholiumDyn.resCost_symm`, `ScholiumDyn.resCost_triangle`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: The path-infimum is a pseudometric: every law proved of the infimum.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

For symbolic states $p, q in M$, the resolution cost is:
\[
reflect(p,q) = inf_{gamma: p to q} int_gamma sqrt{g(dot{gamma}, dot{gamma})} dt
\]
where the infimum is taken over all smooth paths $gamma$ connecting $p$ and $q$, and $g$ is the metric induced via the symbolic connection (see definition:bk1_symbolic_connection) and feature map structure (see definition:bk1_symbolic_manifold_feature_maps).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Resolution Cost]
\label{definition:bk1_resolution_cost}
For symbolic states $p, q \in M$, the \emph{resolution cost} is:
\[
\reflect(p,q) = \inf_{\gamma: p \to q} \int_\gamma \sqrt{g(\dot{\gamma}, \dot{\gamma})} \, dt
\]
where the infimum is taken over all smooth paths $\gamma$ connecting $p$ and $q$, and $g$ is the metric induced via the symbolic connection (see \ref{definition:bk1_symbolic_connection}) and feature map structure (see \ref{definition:bk1_symbolic_manifold_feature_maps}).
\end{definition}
```

### Symbolic Emergence and Curvature (`theorem:bk1_symbolic_emergence_and_curvature`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2029`

- Proof status: `proven`
- Depends on: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_horizon_structure` (Horizon Structure); `definition:bk1_local_semantic_independence` (Local Semantic Independence); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `proposition:bk1_curvature_semantic_entanglement` (Curvature and Semantic Entanglement)
- Cites: `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_horizon_structure` (Horizon Structure); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor)
- Cited by: `axiom:bk1_symbolic_primacy` (Symbolic Primacy); `corollary:bk1_dimensional_bounds_emergence` (Dimensional Bounds on Emergence); `definition:bk6_symbolic_laplace_beltrami_operator_complete` (Symbolic Laplace–Beltrami Operator); `demonstratio:bk7_convergence_within_reflective_basin` (Why Descent, Not Mere Monotonicity); `proof:bk1_dimensional_bounds_emergence`; `proof:bk8_flattening_decoherence_equivalence` (Decoherence as Symbolic Flattening via Curvature Flow); `subsec:appD_info_geometry_contribution_differentiation` (D.4.2 Principia Symbolica's Contribution and Differentiation); `theorem:bk3_symbiotic_curvature_and_resilience` (Symbiotic Curvature and Resilience)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-084`
- Witnesses: `Atlas.non_euclidean_necessity`, `Atlas.path_dependent_iff_noncommuting`
- Countermodels: none
- Conditions: linear-transport model for holonomy (Christoffel/vector-field forms stay open); pair-covering as the topological-regularity stand-in (point-set topology unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: The iff at transport level: route-dependent meaning iff nonzero commutator; Riemannian form open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A symbolic system exhibits emergent behavior—characterized by horizon-relative novelty (see definition:bk1_horizon_structure), reflexive identity, and contextual meaning (see definition:bk1_emergence_event)—if and only if its symbolic manifold has non-zero curvature $kappa neq 0$ (see definition:bk1_symbolic_riemann_tensor).

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Symbolic Emergence and Curvature]
\label{theorem:bk1_symbolic_emergence_and_curvature}
A symbolic system exhibits emergent behavior—characterized by horizon-relative novelty (see \ref{definition:bk1_horizon_structure}), reflexive identity, and contextual meaning (see \ref{definition:bk1_emergence_event})—if and only if its symbolic manifold has non-zero curvature $\kappa \neq 0$ (see \ref{definition:bk1_symbolic_riemann_tensor}).
\end{theorem}
```

### proof:bk1_symbolic_emergence_and_curvature (`proof:bk1_symbolic_emergence_and_curvature`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2034`

- Proof status: `not_applicable`
- Depends on: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_horizon_structure` (Horizon Structure); `definition:bk1_local_semantic_independence` (Local Semantic Independence); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `proposition:bk1_curvature_semantic_entanglement` (Curvature and Semantic Entanglement)
- Cites: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_horizon_structure` (Horizon Structure); `definition:bk1_local_semantic_independence` (Local Semantic Independence); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `proposition:bk1_curvature_semantic_entanglement` (Curvature and Semantic Entanglement)
- Cited by: none
- Macros used: none

**Statement / Body**

The mathematical core of the equivalence is the proven curvature-semantics correspondence; the three marks of emergence are its readings. Work on a contractible neighborhood $U subset M$.

($Leftarrow$) $kappa neq 0$ on $U$ implies emergence.
Contextual meaning. By Prop. proposition:bk1_curvature_semantic_entanglement, $kappa neq 0$ on $U$ is equivalent to the failure of local semantic independence (Def. definition:bk1_local_semantic_independence): symbolic meanings are mutually dependent, i.e.\ contextual.
Horizon-relative novelty. By Lemma lemma:bk1_curvature_semantic_holonomy, parallel transport of a symbolic feature around an infinitesimal loop returns it displaced by $kappa$ (semantic holonomy). Transport within the horizon structure (Def. definition:bk1_horizon_structure) is therefore path-dependent, so traversal of accessible directions generates states reachable by no single direction-novelty relative to the horizon.
Reflexive identity. A reflexive identity is a self-model invariant under the observer's own reflective transport loop (Def. definition:bk1_emergence_event). When $kappa neq 0$ that loop acts as a nontrivial operator, whose invariant structure is a distinguished fixed self-model; when $kappa = 0$ transport is trivial and no self-model is distinguished. Thus all three marks hold.

($Rightarrow$) Emergence implies $kappa neq 0$.
Contextual meaning is, by definition, the failure of local semantic independence; the converse direction of Prop. proposition:bk1_curvature_semantic_entanglement then gives $kappa neq 0$ on $U$. (Equivalently, reflexivity together with context-sensitivity forces $kappa neq 0$ by Cor. corollary:bk1_non_euclidean_necessity.)

The two implications give emergence $iff kappa neq 0$.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk1_symbolic_emergence_and_curvature}
\leavevmode

The mathematical core of the equivalence is the proven curvature--semantics correspondence; the three marks of emergence are its readings. Work on a contractible neighborhood $U \subset M$.

\emph{($\Leftarrow$) $\kappa \neq 0$ on $U$ implies emergence.}
\emph{Contextual meaning.} By Prop.~\ref{proposition:bk1_curvature_semantic_entanglement}, $\kappa \neq 0$ on $U$ is equivalent to the failure of local semantic independence (Def.~\ref{definition:bk1_local_semantic_independence}): symbolic meanings are mutually dependent, i.e.\ contextual.
\emph{Horizon-relative novelty.} By Lemma~\ref{lemma:bk1_curvature_semantic_holonomy}, parallel transport of a symbolic feature around an infinitesimal loop returns it displaced by $\kappa$ (semantic holonomy). Transport within the horizon structure (Def.~\ref{definition:bk1_horizon_structure}) is therefore path-dependent, so traversal of accessible directions generates states reachable by no single direction---novelty relative to the horizon.
\emph{Reflexive identity.} A reflexive identity is a self-model invariant under the observer's own reflective transport loop (Def.~\ref{definition:bk1_emergence_event}). When $\kappa \neq 0$ that loop acts as a nontrivial operator, whose invariant structure is a \emph{distinguished} fixed self-model; when $\kappa = 0$ transport is trivial and no self-model is distinguished. Thus all three marks hold.

\emph{($\Rightarrow$) Emergence implies $\kappa \neq 0$.}
Contextual meaning is, by definition, the failure of local semantic independence; the converse direction of Prop.~\ref{proposition:bk1_curvature_semantic_entanglement} then gives $\kappa \neq 0$ on $U$. (Equivalently, reflexivity together with context-sensitivity forces $\kappa \neq 0$ by Cor.~\ref{corollary:bk1_non_euclidean_necessity}.)

The two implications give emergence $\iff \kappa \neq 0$.
\end{proof}
```

### Dimensional Bounds on Emergence (`corollary:bk1_dimensional_bounds_emergence`)

Role: `corollary` | Type: `corollary` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2051`

- Proof status: `proven`
- Depends on: `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `theorem:bk1_symbolic_emergence_and_curvature` (Symbolic Emergence and Curvature)
- Cites: `theorem:bk1_symbolic_emergence_and_curvature` (Symbolic Emergence and Curvature)
- Cited by: `proof:bk4_topological_stability_via_spectral_and_curvature_constraints` (Topological Stability via Spectral and Curvature Constraints)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-088`
- Witnesses: `ScholiumBridge.nonzero_curvature_has_active_mode`
- Countermodels: none
- Conditions: manifold metric, exact rank bound, and the interpretive unification/primacy claims stay open per row notes
- Formal boundary: Nonzero curvature has an active mode (complexity >= 1); the exact rank bound stays open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

By Thm. theorem:bk1_symbolic_emergence_and_curvature, the complexity of symbolic emergence is bounded below by the rank of the curvature tensor $kappa$. Systems with richer curvature structure support more complex emergent phenomena.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Dimensional Bounds on Emergence]
\label{corollary:bk1_dimensional_bounds_emergence}
By Thm.~\ref{theorem:bk1_symbolic_emergence_and_curvature}, the complexity of symbolic emergence is bounded below by the rank of the curvature tensor $\kappa$. Systems with richer curvature structure support more complex emergent phenomena.
\end{corollary}
```

### proof:bk1_dimensional_bounds_emergence (`proof:bk1_dimensional_bounds_emergence`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2056`

- Proof status: `not_applicable`
- Depends on: `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `theorem:bk1_symbolic_emergence_and_curvature` (Symbolic Emergence and Curvature)
- Cites: `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `theorem:bk1_symbolic_emergence_and_curvature` (Symbolic Emergence and Curvature)
- Cited by: none
- Macros used: none

**Statement / Body**

By Thm. theorem:bk1_symbolic_emergence_and_curvature, emergence occurs exactly where $kappa neq 0$. Each independent emergent mode is an independent direction of semantic holonomy (Lemma lemma:bk1_curvature_semantic_holonomy): a feature whose parallel transport around an infinitesimal loop returns displaced by a nonzero amount. Two emergent modes are distinguishable as separate phenomena only when their holonomy displacements are linearly independent vectors on the feature manifold; by the holonomy identity, those displacements are the images of the loop's tangent bivector under $kappa$. Hence the count of linearly independent emergent modes equals the dimension of the image of $kappa$ as an operator-that is, $rankkappa$-which therefore bounds the complexity of emergence from below. A curvature tensor of higher rank opens a strictly larger space of independent emergent directions, so richer curvature supports richer emergence.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk1_dimensional_bounds_emergence}
\leavevmode
By Thm.~\ref{theorem:bk1_symbolic_emergence_and_curvature}, emergence occurs exactly where $\kappa \neq 0$. Each independent emergent mode is an independent direction of semantic holonomy (Lemma~\ref{lemma:bk1_curvature_semantic_holonomy}): a feature whose parallel transport around an infinitesimal loop returns displaced by a nonzero amount. Two emergent modes are distinguishable as separate phenomena only when their holonomy displacements are linearly independent vectors on the feature manifold; by the holonomy identity, those displacements are the images of the loop's tangent bivector under $\kappa$. Hence the count of linearly independent emergent modes equals the dimension of the image of $\kappa$ as an operator---that is, $\operatorname{rank}\kappa$---which therefore bounds the complexity of emergence from below. A curvature tensor of higher rank opens a strictly larger space of independent emergent directions, so richer curvature supports richer emergence.
\end{proof}
```

### Category Errors in Classical Models (`sec:bk1_category_errors_in_classical_models`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2066`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `theorem:bk4_paradoxical_arrow_of_time` (The Paradoxical Arrow of Time)
- Macros used: none

**Statement / Body**

(no body text extracted)

### Limits of Classical Frameworks (`subsec:bk1_limits_of_classical_frameworks`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2071`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Newtonian Category Error (`definition:bk1_newtonian_category_error`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2074`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: none
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-038`
- Witnesses: `ScholiumC.exists_inaccessible_of_not_surjective`
- Countermodels: none
- Conditions: application order in the composite is not interpreted as ontological origin order; catS, observer detection, stage continuity, and geometric realization remain distinct supplied interfaces; drift and reflection are fields of one OperationalStage witness; neither is derived from the other
- Formal boundary: Only the access-function clause (alpha(O) properly contained in O, read as non-surjectivity) is modeled, yielding an inaccessible state; the manifold-smoothness/drift-non-constructibility conclusion is not.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A modeling framework exhibits the Newtonian Category Error when it presupposes manifold smoothness and continuity a priori, thereby violating bounded observer logic (see definition:bk1_bounded_observer). Specifically, if $O$ denotes a bounded observer with access function $alpha: O to O$ where $alpha(O) subsetneq O$, then any framework assuming global differentiability disconnects form from relation, rendering the drift operator $D$ (see definition:bk1_drift_field) non-constructible within the observer's horizon on the symbolic manifold $M$ (see definition:bk1_symbolic_manifold).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Newtonian Category Error]
\label{definition:bk1_newtonian_category_error}
A modeling framework exhibits the Newtonian Category Error when it presupposes manifold smoothness and continuity \emph{a priori}, thereby violating bounded observer logic (see \ref{definition:bk1_bounded_observer}). Specifically, if $\mathcal{O}$ denotes a bounded observer with access function $\alpha: \mathcal{O} \to \mathcal{O}$ where $\alpha(\mathcal{O}) \subsetneq \mathcal{O}$, then any framework assuming global differentiability disconnects form from relation, rendering the drift operator $D$ (see \ref{definition:bk1_drift_field}) non-constructible within the observer's horizon on the symbolic manifold $M$ (see \ref{definition:bk1_symbolic_manifold}).
\end{definition}
```

### Newtonian Incompleteness (`proposition:bk1_newtonian_incompleteness`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2079`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: `proof:bk1_dual_horizon_unification_principle` (Projection Through the Dual Horizon Signature); `theorem:bk1_dual_horizon_unification_principle` (Emergent Dual Horizon Unification Principle)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_B-020`
- Witnesses: `ScholiumD.newtonian_incompleteness_kernel`, `ScholiumD.newtonian_incompleteness_normedSpace`, `accelerated_frame_defect`, `accelerated_frame_defect_ne`, `newtonForce_equivariant`
- Countermodels: none
- Conditions: continuous linear change of frame; nonzero frame acceleration for strict defect; nonzero uniform frame acceleration; real normed vector space; twice differentiable trajectory at the stated point
- Formal boundary: Unflattened covariance-boundary kernel: on every real normed vector space, scalar Newtonian force commutes with every continuous linear frame map, while each nonzero uniform frame acceleration produces a nonzero 2*w defect. The NVec derivative construction remains the concrete dynamical witness. Extending covariance to accelerated observers therefore requires an explicit correction; relativistic gravity and a general spacetime theory are not claimed.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let \(V\) be a real normed vector space and let the Newtonian force law be
\(F_m(a)=m a\) for \(minmathbb{R}\) and \(ain V\). The map \(F_m\) is
equivariant under every continuous linear change of frame \(L:Vto V\):
\[
 L(F_m(a))=F_m(L(a)).
\]
However, if an accelerated frame contributes a nonzero acceleration
\(win V\), its transformed acceleration \(a+2w\) is not \(a\). Hence the
linear-frame covariance of the Newtonian law does not by itself extend to
accelerated observer frames: such an extension requires an explicit
frame-correction term.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Newtonian Incompleteness]
\label{proposition:bk1_newtonian_incompleteness}
Let \(V\) be a real normed vector space and let the Newtonian force law be
\(F_m(a)=m a\) for \(m\in\mathbb{R}\) and \(a\in V\).  The map \(F_m\) is
equivariant under every continuous linear change of frame \(L:V\to V\):
\[
  L(F_m(a))=F_m(L(a)).
\]
However, if an accelerated frame contributes a nonzero acceleration
\(w\in V\), its transformed acceleration \(a+2w\) is not \(a\).  Hence the
linear-frame covariance of the Newtonian law does not by itself extend to
accelerated observer frames: such an extension requires an explicit
frame-correction term.
\end{proposition}
```

### Covariance Boundary (`proof:bk1_newtonian_incompleteness`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2093`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

For every continuous linear \(L\),
\[
 L(F_m(a))=L(ma)=mL(a)=F_m(L(a)),
\]
so \(F_m\) is equivariant under the stated covariance class. If \(wne0\),
then \(2wne0\), and cancellation in the additive group of \(V\) gives
\(a+2wne a\). The accelerated-frame defect therefore cannot be obtained by
ordinary linear-frame equivariance alone and must be represented explicitly.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Covariance Boundary]
\label{proof:bk1_newtonian_incompleteness}
\leavevmode

For every continuous linear \(L\),
\[
  L(F_m(a))=L(ma)=mL(a)=F_m(L(a)),
\]
so \(F_m\) is equivariant under the stated covariance class.  If \(w\ne0\),
then \(2w\ne0\), and cancellation in the additive group of \(V\) gives
\(a+2w\ne a\).  The accelerated-frame defect therefore cannot be obtained by
ordinary linear-frame equivariance alone and must be represented explicitly.
\end{proof}
```

### Quantum Tensor-Closure Category Error (`definition:bk1_quantum_category_error`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2107`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

A tensor-closure category error occurs when an update valued in one state
carrier \(mathcal H\) is identified directly with a tensor
\(psiotimesvarphiinmathcal Hotimesmathcal H\) without specifying a
map from the tensor product back to \(mathcal H\). A lossless linear
closure is a linear isomorphism
\[
 C:mathcal Hotimes_{mathbb K}mathcal H
 overset{sim}{longrightarrow}mathcal H.
\]
Whether a Hamiltonian is externally controlled, dynamically updated, or
represented inside a larger quantum system is a separate modeling question;
strict linearity alone does not prohibit such constructions.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Quantum Tensor-Closure Category Error]
\label{definition:bk1_quantum_category_error}
A tensor-closure category error occurs when an update valued in one state
carrier \(\mathcal H\) is identified directly with a tensor
\(\psi\otimes\varphi\in\mathcal H\otimes\mathcal H\) without specifying a
map from the tensor product back to \(\mathcal H\).  A \emph{lossless linear
closure} is a linear isomorphism
\[
 C:\mathcal H\otimes_{\mathbb K}\mathcal H
   \overset{\sim}{\longrightarrow}\mathcal H.
\]
Whether a Hamiltonian is externally controlled, dynamically updated, or
represented inside a larger quantum system is a separate modeling question;
strict linearity alone does not prohibit such constructions.
\end{definition}
```

### Finite-Dimensional Symbolic--Quantum Tensor Obstruction (`lemma:bk1_symbolic_quantum_incompatibility`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2123`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_B-021`
- Witnesses: `ScholiumD.symbolic_quantum_incompatibility_kernel`
- Countermodels: none
- Conditions: See the receipted theorem statement and coverage note for explicit premises.
- Formal boundary: Faithful logical kernel with exact preservation predicates: no map can preserve both reflection and binary reflexive update when joint preservation entails a Hamiltonian-level meta-update and the target quantum model forbids that update. These two category-error premises remain explicit because unitary linear evolution and tensor structure alone do not establish them; a concrete Hilbert-space no-go theorem remains open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let \(mathcal H\) be a finite-dimensional vector space over a field
\(mathbb K\), with \(1<dim_{mathbb K}mathcal H<infty\). Then there is no
lossless linear closure
\[
 mathcal Hotimes_{mathbb K}mathcal H
 overset{sim}{longrightarrow}mathcal H.
\]
Consequently, a symbolic reflexive update whose preservation requires the
pair tensor \(phi(s)otimesphi(s')\) to be represented losslessly in the
same finite-dimensional state carrier cannot be preserved by such a closure.
Unitary reflection evolution does not remove this dimension obstruction.
The conclusion is sharp: in dimension one the tensor square is linearly
isomorphic to the original carrier.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Finite-Dimensional Symbolic--Quantum Tensor Obstruction]
\label{lemma:bk1_symbolic_quantum_incompatibility}
Let \(\mathcal H\) be a finite-dimensional vector space over a field
\(\mathbb K\), with \(1<\dim_{\mathbb K}\mathcal H<\infty\).  Then there is no
lossless linear closure
\[
 \mathcal H\otimes_{\mathbb K}\mathcal H
   \overset{\sim}{\longrightarrow}\mathcal H.
\]
Consequently, a symbolic reflexive update whose preservation requires the
pair tensor \(\phi(s)\otimes\phi(s')\) to be represented losslessly in the
same finite-dimensional state carrier cannot be preserved by such a closure.
Unitary reflection evolution does not remove this dimension obstruction.
The conclusion is sharp: in dimension one the tensor square is linearly
isomorphic to the original carrier.
\end{lemma}
```

### Tensor Dimension Obstruction (`proof:bk1_symbolic_quantum_incompatibility`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2139`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Write \(n=dim_{mathbb K}mathcal H\). Finite-dimensional tensor products
satisfy
\[
 dim_{mathbb K}(mathcal Hotimes_{mathbb K}mathcal H)=n^2.
\]
A linear isomorphism to \(mathcal H\) would therefore imply \(n^2=n\).
For positive finite \(n\), this forces \(n=1\), contradicting \(n>1\).
Thus no lossless linear self-tensor closure exists in the stated regime.
When \(n=1\), both sides have dimension one and a linear isomorphism does
exist, proving sharpness. The argument concerns the typed tensor closure; it
does not assert a universal prohibition on Hamiltonian control or quantum
models of self-reference.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Tensor Dimension Obstruction]
\label{proof:bk1_symbolic_quantum_incompatibility}
\leavevmode

Write \(n=\dim_{\mathbb K}\mathcal H\).  Finite-dimensional tensor products
satisfy
\[
 \dim_{\mathbb K}(\mathcal H\otimes_{\mathbb K}\mathcal H)=n^2.
\]
A linear isomorphism to \(\mathcal H\) would therefore imply \(n^2=n\).
For positive finite \(n\), this forces \(n=1\), contradicting \(n>1\).
Thus no lossless linear self-tensor closure exists in the stated regime.
When \(n=1\), both sides have dimension one and a linear isomorphism does
exist, proving sharpness.  The argument concerns the typed tensor closure; it
does not assert a universal prohibition on Hamiltonian control or quantum
models of self-reference.
\end{proof}
```

### Conclusion: Reflexivity Requires Quadratic Framing (`subsec:bk1_reflexivity_requires_quadratic_framing`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2157`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Emergence Theorem---Contextual Cross-Error (`theorem:bk1_symbolic_emergence_theorem_thermodynamics`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2160`

- Proof status: `proven`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator)
- Cited by: `corollary:bk1_necessity_of_non_euclidean_symbolic_space` (Necessity of Non-Euclidean Symbolic Transport); `corollary:bk7_stability_innovation_equilibrium` (Stability--Innovation Compatibility); `proof:bk7_stability_innovation_equilibrium` (Contextual Curvature with Stable Identity)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_B-022`
- Witnesses: `ScholiumD.contextualGrowth_exposes_crossError`, `ScholiumD.emergence_premises_do_not_force_curvature`
- Countermodels: `ScholiumD.emergence_premises_do_not_force_curvature`
- Conditions: a real-valued state-context update; failure of additive separation into independent state and context contributions
- Formal boundary: Layered repair: contextual nonseparability locally forces a nonzero mixed cross-error by an explicit additive-decomposition contradiction. The Scholium stops at that certificate; Book IV consumes it to construct noncommuting transport, and Book VII consumes the Book IV geometry. The zero-curvature Bool model remains the negative control showing novelty, reflective identity, and abstract dimension growth alone do not supply the certificate or curvature.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $S$ be a symbolic system over a manifold $M$, and let
$U:mathbb{R}timesmathbb{R}tomathbb{R}$ be a local residual
update in state and context coordinates. Suppose $S$ supports:


- horizon-relative novelty: $exists sinS$ such that $D(s)notinalpha(S)$ (Def. definition:bk1_drift_field);

- reflexive symbolic identity: $R(S)capSneqemptyset$ (Def. definition:bk1_reflection_operator);

- contextual structural growth: $U$ is not additively separable as $A(xi)+B(chi)$.

Then there exist state and context displacements $xi,chi$ for which the
mixed cross-error
\[
DeltaU(xi,chi)
 =U(xi,chi)-U(xi,0)
 -U(0,chi)+U(0,0)
\]
is nonzero. This cross-error is the Scholium-level certificate supplied to
Book IV. The later transport construction may geometrize it as noncommuting
state-context transport; that geometric realization is not used as a premise
of this theorem. Likewise, identifying the leading mixed term as bilinear
requires the smooth local-expansion hypotheses stated with the later
quadratic construction.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Symbolic Emergence Theorem---Contextual Cross-Error]
\label{theorem:bk1_symbolic_emergence_theorem_thermodynamics}
Let $\mathcal{S}$ be a symbolic system over a manifold $M$, and let
$\mathcal{U}:\mathbb{R}\times\mathbb{R}\to\mathbb{R}$ be a local residual
update in state and context coordinates. Suppose $\mathcal{S}$ supports:
\begin{itemize}
  \item horizon-relative novelty: $\exists s\in\mathcal{S}$ such that $D(s)\notin\alpha(\mathcal{S})$ (Def.~\ref{definition:bk1_drift_field});
  \item reflexive symbolic identity: $R(\mathcal{S})\cap\mathcal{S}\neq\emptyset$ (Def.~\ref{definition:bk1_reflection_operator});
  \item contextual structural growth: $\mathcal{U}$ is not additively separable as $A(\xi)+B(\chi)$.
\end{itemize}
Then there exist state and context displacements $\xi,\chi$ for which the
mixed cross-error
\[
\Delta\mathcal{U}(\xi,\chi)
 =\mathcal{U}(\xi,\chi)-\mathcal{U}(\xi,0)
  -\mathcal{U}(0,\chi)+\mathcal{U}(0,0)
\]
is nonzero.  This cross-error is the Scholium-level certificate supplied to
Book~IV.  The later transport construction may geometrize it as noncommuting
state--context transport; that geometric realization is not used as a premise
of this theorem.  Likewise, identifying the leading mixed term as bilinear
requires the smooth local-expansion hypotheses stated with the later
quadratic construction.
\end{theorem}
```

### Nonseparability Forces a Cross-Error (`proof:bk1_symbolic_emergence_theorem_thermodynamics`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2184`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Assume for contradiction that every mixed cross-error vanishes. Define
\[
 A(xi)=mathcal U(xi,0),

 B(chi)=mathcal U(0,chi)-mathcal U(0,0).
\]
The vanishing cross-difference identity rearranges pointwise to
$mathcal U(xi,chi)=A(xi)+B(chi)$, contradicting contextual structural
growth. Hence some $Deltamathcal U(xi,chi)$ is nonzero. Novelty and
reflexive identity retain their emergence roles, while contextual
nonseparability is the load-bearing premise for this certificate. Book IV
consumes the certificate downstream; it does not discharge the Scholium proof
backward.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Nonseparability Forces a Cross-Error]
\label{proof:bk1_symbolic_emergence_theorem_thermodynamics}
\leavevmode

Assume for contradiction that every mixed cross-error vanishes.  Define
\[
 A(\xi)=\mathcal U(\xi,0),
 \qquad
 B(\chi)=\mathcal U(0,\chi)-\mathcal U(0,0).
\]
The vanishing cross-difference identity rearranges pointwise to
$\mathcal U(\xi,\chi)=A(\xi)+B(\chi)$, contradicting contextual structural
growth.  Hence some $\Delta\mathcal U(\xi,\chi)$ is nonzero.  Novelty and
reflexive identity retain their emergence roles, while contextual
nonseparability is the load-bearing premise for this certificate.  Book~IV
consumes the certificate downstream; it does not discharge the Scholium proof
backward.
\end{proof}
```

### Necessity of Non-Euclidean Symbolic Transport (`corollary:bk1_necessity_of_non_euclidean_symbolic_space`)

Role: `corollary` | Type: `corollary` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2202`

- Proof status: `proven`
- Depends on: `theorem:bk1_symbolic_emergence_theorem_thermodynamics` (Symbolic Emergence Theorem---Contextual Cross-Error)
- Cites: `theorem:bk1_symbolic_emergence_theorem_thermodynamics` (Symbolic Emergence Theorem---Contextual Cross-Error)
- Cited by: `axiom:bk1_symbolic_primacy` (Symbolic Primacy)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-057`
- Witnesses: `Atlas.non_euclidean_necessity`
- Countermodels: none
- Conditions: linear-transport model for holonomy (Christoffel/vector-field forms stay open); pair-covering as the topological-regularity stand-in (point-set topology unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Duplicate anchor of the necessity corollary; same kernel.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Under the hypotheses of
Thm. theorem:bk1_symbolic_emergence_theorem_thermodynamics, there exist
state and context displacements whose induced transports do not commute.
Thus no single flat, additively separable transport geometry represents the
contextual update.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Necessity of Non-Euclidean Symbolic Transport]
\label{corollary:bk1_necessity_of_non_euclidean_symbolic_space}
Under the hypotheses of
Thm.~\ref{theorem:bk1_symbolic_emergence_theorem_thermodynamics}, there exist
state and context displacements whose induced transports do not commute.
Thus no single flat, additively separable transport geometry represents the
contextual update.
\end{corollary}
```

### Nonzero Holonomy Obstructs Flat Transport (`proof:bk1_necessity_of_non_euclidean_symbolic_space`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2210`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The theorem supplies a nonzero mixed cross-error and, at nonzero observer
scale, two induced transports whose composites depend on order. Flat
additively separable transport has zero mixed cross-error and commuting routes.
Therefore the witnessed update is non-Euclidean in the precise transport sense
claimed.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Nonzero Holonomy Obstructs Flat Transport]
\label{proof:bk1_necessity_of_non_euclidean_symbolic_space}
\leavevmode
The theorem supplies a nonzero mixed cross-error and, at nonzero observer
scale, two induced transports whose composites depend on order.  Flat
additively separable transport has zero mixed cross-error and commuting routes.
Therefore the witnessed update is non-Euclidean in the precise transport sense
claimed.
\end{proof}
```

### Toward Symbolic Primacy and Unified Fields (`sec:bk1_toward_symbolic_primacy_and_unified_fields`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2222`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Reflexivity and SRMF (`subsec:bk1_symbolic_reflexivity_and_srmf`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2224`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Primacy (`axiom:bk1_symbolic_primacy`)

Role: `axiom` | Type: `axiom` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2226`

- Proof status: `definitional`
- Depends on: `axiom:bk1_axiomata_prima` (Drift as Origin); `corollary:bk1_necessity_of_non_euclidean_symbolic_space` (Necessity of Non-Euclidean Symbolic Transport); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `theorem:bk1_symbolic_emergence_and_curvature` (Symbolic Emergence and Curvature)
- Cites: `axiom:bk1_axiomata_prima` (Drift as Origin); `corollary:bk1_necessity_of_non_euclidean_symbolic_space` (Necessity of Non-Euclidean Symbolic Transport); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `theorem:bk1_symbolic_emergence_and_curvature` (Symbolic Emergence and Curvature)
- Cited by: `definition:bk7_symbolic_reflexive_validation_srv` (Symbolic Reflexive Validation (SRV)); `remark:bk4_quantum_topological_phases` (Connection to Quantum Topological Phases); `remark:bk7_unnamed_remark_04`; `scholium:bk4_o_boundedness_unifying_principle` ($\mathcal{O}$-Boundedness as the Unifying Principle of Fuzzy Calculus); `scholium:bk7_popperian_extension` (Popperian Extension)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-096`
- Witnesses: `Atlas.non_euclidean_necessity`
- Countermodels: none
- Conditions: linear-transport model for holonomy (Christoffel/vector-field forms stay open); pair-covering as the topological-regularity stand-in (point-set topology unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Physical law and symbolic emergence as projections of one reflexive manifold: the curvature-necessity kernel grounds the shared structure; the primacy claim stays interpretive.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

In continuity with Axiom axiom:bk1_axiomata_prima, Def. definition:bk1_symbolic_manifold, Thm. theorem:bk1_symbolic_emergence_and_curvature, and Cor. corollary:bk1_necessity_of_non_euclidean_symbolic_space, the structure of physical law and the structure of symbolic emergence are not two domains. They are different projections of a single reflexive manifold.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Symbolic Primacy]
\label{axiom:bk1_symbolic_primacy}
In continuity with Axiom~\ref{axiom:bk1_axiomata_prima}, Def.~\ref{definition:bk1_symbolic_manifold}, Thm.~\ref{theorem:bk1_symbolic_emergence_and_curvature}, and Cor.~\ref{corollary:bk1_necessity_of_non_euclidean_symbolic_space}, the structure of physical law and the structure of symbolic emergence are not two domains. They are different projections of a single reflexive manifold.
\end{axiom}
```

### Self-Regulating Mapping Function (SRMF) (`definition:bk1_self_regulating_mapping_function_srmf`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2230`

- Proof status: `definitional`
- Depends on: `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density)
- Cited by: `axiom:bk8_symbolic_reidemeister_algebra` (Symbolic Reidemeister Algebra); `definition:bk1_horizon_crossing_operation` (Horizon-Crossing Operation); `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence); `definition:bk1_srmf_energy_functional` (SRMF Energy Functional); `definition:bk4_projective_action_transl` (Projective Action Translator); `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$); `definition:bk7_srmfconstrained_observer` (SRMF-Constrained Observer); `definition:bk7_symbolic_reflexive_validation_srv` (Symbolic Reflexive Validation (SRV)); `definition:bk8_metabolic_programming_cycle` (Metabolic Programming Cycle); `definition:bk8_symbolic_stress_tensor` (Reflexive Debugging Operator $\mathcal{O}_{\text{debug}}$); `definition:bk9_bidirectional_srmf` (Bidirectional SRMF \(\mathrm{SRMF}^{\leftrightarrow}\)); `definition:bk9_collapse_inversion_operator` (Collapse-Inversion Operator $\varnothing^*$); `definition:bk9_covenant_drift_density` (Covenant Drift Density \(\rho(C_{AB})\)); `definition:bk9_prompt_injection_operator` (Prompt Injection Operator $\mathcal{J}$); `definition:bk9_srmf_recursive_cycle` (SRMF-Recursive Cycle $\Xi_n$); `definition:bk9_temetic_artifact` (Temetic Artifact $\tau$); `demonstratio:bk8_symbolic_unkotting` (Symbolic Unknotting); `lemma:bk4_srmf_constrained_action_norm` (SRMF-Constrained Action Norm); `lemma:bk7_budgetlimited_minimizer` (Budget-Limited Minimizer); `proof:bk1_unified_field_classification` (Fields as SRMF Boundary-Symmetry Sectors); `proof:bk7_emergent_lp_norm_from_srmf` (Emergent LP Norm from SRMF); `proof:bk7_srmf_decency_regulation`; `proof:bk8_membrane_operator_symmetry`; `proof:bk8_sketch_convergence_to_fixed_by_banach` (RG Fixed Point via Banach Contraction); `proposition:bk4_spiral_transition` (Spiral transition between modes); `proposition:bk7_srmf_decency_regulation` (SRMF-Regulated Decency Dynamics); `proposition:bk8_membrane_operator_symmetry` (Type III -- Reflective Permutation); `proposition:bk9_framework_functional_identity` (The Framework is a Functional); `remark:bk4_quantum_topological_phases` (Connection to Quantum Topological Phases); `scholium:bk4_ttcs_simulation_tool_use` (TTCS as Symbolic Simulation and Tool-Use); `scholium:bk4_ttdc_impulse_collapse` (Collapse as Impulse: The Newtonian Structure of TTDC); `scholium:bk5_metabolic_cost_of_cognition` (Metabolic Cost of Cognition); `scholium:bk7_popperian_extension` (Popperian Extension); `sec:bk5_srmf_for_symbolic_operators_and_processes` (SRMF for Symbolic Operators and Processes); `subsec:appD_process_philosophy_contribution_differentiation` (D.6.2 Principia Symbolica's Contribution and Differentiation); `subsec:bk5_srmf_core_axioms` (Core Axioms and Theoretical Development); `subsec:bk7_hdb_formal_closure` (Formal Closure of the Human Decency Benchmark); `theorem:bk1_unified_field_classification` (Unified Field Classification); `theorem:bk3_criteria_persistent_symbolic_life` (Persistent Symbolic Life Criteria); `theorem:bk5_operator_convergence` (Operator Convergence); `theorem:bk7_reflective_convergence_to_stable_identity` (Reflective Convergence to Stable Identity); `theorem:bk8_rg_fixed_point` (RG Fixed Point); `theorem:bk8_sr_convergence` (SR Convergence)
- Macros used: `\reflect`

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-085`
- Witnesses: `SRMF.turn_closes_iff`
- Countermodels: none
- Conditions: the circle part of a revolution is the identity by construction; injections are data; no claim about this file or any system proving its own consistency; the helix is FOR approaching the equilibrium circle, not a telos; non-closure is not idolized
- Formal boundary: The SRMF revolution structure with the closure dichotomy; the full operator pipeline interpretive.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A SRMF is a reflexive operator $F: S to S$ on a symbolic manifold $S$ (see definition:bk1_symbolic_manifold) such that:
\[
F[rho](x) = rho(x) + delta_{C}(x) cdot reflect(C_x)
\]
Where:

- $rho: S to mathbb{R}$ is a symbolic density field (see definition:bk1_symbolic_probabilty_density)

- $delta_{C}(x)$ is a contradiction detection function such that $delta_{C}(x) = \|nabla times nabla rho(x)\|$ measuring local symbolic inconsistency (see definition:bk1_symbolic_contradiction)

- $C_x$ is the contradiction manifold at $x$

- $reflect: C to T_xS$ is a reframing operator mapping contradictions to tangent vectors in symbolic space (see definition:bk1_reflection_operator)

The SRMF satisfies the equilibrium condition:
\[
lim_{t to infty} F^t[rho] in text{Fix}(F)
\]

**Verbatim LaTeX Body**

```latex
\begin{definition}[Self-Regulating Mapping Function (SRMF)]
\label{definition:bk1_self_regulating_mapping_function_srmf}
A SRMF is a reflexive operator $\mathcal{F}: S \to S$ on a symbolic manifold $S$ (see \ref{definition:bk1_symbolic_manifold}) such that:
\[
\mathcal{F}[\rho](x) = \rho(x) + \delta_{\mathcal{C}}(x) \cdot \reflect(\mathcal{C}_x)
\]
Where:
\begin{itemize}
\item $\rho: S \to \mathbb{R}$ is a symbolic density field (see \ref{definition:bk1_symbolic_probabilty_density})
\item $\delta_{\mathcal{C}}(x)$ is a contradiction detection function such that $\delta_{\mathcal{C}}(x) = \|\nabla \times \nabla \rho(x)\|$ measuring local symbolic inconsistency (see \ref{definition:bk1_symbolic_contradiction})
\item $\mathcal{C}_x$ is the contradiction manifold at $x$
\item $\reflect: \mathcal{C} \to T_xS$ is a reframing operator mapping contradictions to tangent vectors in symbolic space (see \ref{definition:bk1_reflection_operator})
\end{itemize}
The SRMF satisfies the equilibrium condition:
\[
\lim_{t \to \infty} \mathcal{F}^t[\rho] \in \text{Fix}(\mathcal{F})
\]
\end{definition}
```

### SRMF Energy Functional (`definition:bk1_srmf_energy_functional`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2248`

- Proof status: `definitional`
- Depends on: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `definition:bk7_symbolic_reflexive_validation_srv` (Symbolic Reflexive Validation (SRV)); `proof:bk9_framework_functional_identity`; `proposition:bk9_framework_functional_identity` (The Framework is a Functional)
- Macros used: none

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-086`
- Witnesses: `SRMF.closure_iff_no_work`
- Countermodels: none
- Conditions: the circle part of a revolution is the identity by construction; injections are data; no claim about this file or any system proving its own consistency; the helix is FOR approaching the equilibrium circle, not a telos; non-closure is not idolized
- Formal boundary: The Godel-safe cycle potential as the energy functional kernel; the appB form is separately bound.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The symbolic energy of a configuration $rho$ under SRMF dynamics (see definition:bk1_self_regulating_mapping_function_srmf) is given by:
\[
E[rho] = int_S \|nabla rho\|^2 dx + lambda int_S delta_{C}(x)^2 dx
\]
Where $lambda$ is the contradiction tolerance parameter, and $S$ is the symbolic manifold (see definition:bk1_symbolic_manifold).

**Verbatim LaTeX Body**

```latex
\begin{definition}[SRMF Energy Functional]
\label{definition:bk1_srmf_energy_functional}
The symbolic energy of a configuration $\rho$ under SRMF dynamics (see \ref{definition:bk1_self_regulating_mapping_function_srmf}) is given by:
\[
E[\rho] = \int_S \|\nabla \rho\|^2 dx + \lambda \int_S \delta_{\mathcal{C}}(x)^2 dx
\]
Where $\lambda$ is the contradiction tolerance parameter, and $S$ is the symbolic manifold (see \ref{definition:bk1_symbolic_manifold}).
\end{definition}
```

### remark:scholium_symbolicum.tex:2257 (`remark:scholium_symbolicum.tex:2257`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2257`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The SRMF represents not a law, but a mode of lawful emergence: a structure that self-stabilizes by reframing internal contradictions. Its dynamics minimize the energy functional while preserving symbolic cohesion.

**Verbatim LaTeX Body**

```latex
\begin{remark}
The SRMF represents not a law, but a mode of lawful emergence: a structure that self-stabilizes by reframing internal contradictions. Its dynamics minimize the energy functional while preserving symbolic cohesion.
\end{remark}
```

### Emergence via Paradox Resolution (`subsec:bk1_emergence_via_paradox_resolution`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2260`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `remark:bk4_fuzzy`
- Macros used: none

**Statement / Body**

(no body text extracted)

### Paradox-Triggered Emergence (`definition:bk1_paradox_triggered_emergence`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2264`

- Proof status: `definitional`
- Depends on: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction)
- Cites: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_symbolic_contradiction` (Symbolic Contradiction)
- Cited by: `abs:press` (Press Abstract (Non-specialist science readers)); `axiom:bk6_non_commutativity_evolution_reflection` (Non-Commutativity of Evolution and Reflection); `definition:bk1_emergence_operator` (Emergence Operator); `definition:bk1_shared_boundary_paradox` (Shared Boundary Paradox); `definition:bk7_symbolic_reflexive_validation_srv` (Symbolic Reflexive Validation (SRV)); `demonstratio:bk7_convergence_within_reflective_basin` (Why Descent, Not Mere Monotonicity); `lemma:bk1_paradoxical_symmetry_breaking` (Paradoxical Symmetry Breaking); `proof:bk1_paradoxical_symmetry_breaking` (Resolution Breaks the Stabilizer of the Paradox); `proof:bk1_shared_paradox_bridge_datum` (The Shared Edge Carries the Common Obstruction); `proof:bk2_coherence_of_symbolic_therm`; `remark:bk7_unnamed_remark_04`; `subsec:appD_cst_core_resonance` (D.8.1 Core Resonance); `theorem:bk2_coherence_of_symbolic_therm` (Coherence of Symbolic Thermodynamics); `theorem:bk5_symbolic_coherence_conservation` (Symbolic Coherence Conservation)
- Macros used: `\reflect`

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-071`
- Witnesses: `ScholiumDyn.extension_resolves`, `ScholiumDyn.paradox_unresolvable_within`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: Both clauses: unresolvable within, resolvable in the extension - constructive.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A contradiction $C$ within a symbolic membrane $M$ induces an emergent expansion $delta M$ iff:
\[
nexists text{ reframing } reflect text{ such that } reflect(C) in text{Fix}(F|_M)
\]
but
\[
exists text{ expanded membrane } M' supset M text{ and reframing } reflect' text{ such that } reflect'(C) in text{Fix}(F|_{M'})
\]
where $F$ is the SRMF operator (see definition:bk1_self_regulating_mapping_function_srmf), and $C$ is a symbolic contradiction (see definition:bk1_symbolic_contradiction).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Paradox-Triggered Emergence]
\label{definition:bk1_paradox_triggered_emergence}
A contradiction $\mathcal{C}$ within a symbolic membrane $M$ induces an emergent expansion $\delta M$ iff:
\[
\nexists \text{ reframing } \reflect \text{ such that } \reflect(\mathcal{C}) \in \text{Fix}(\mathcal{F}|_M)
\]
but
\[
\exists \text{ expanded membrane } M' \supset M \text{ and reframing } \reflect' \text{ such that } \reflect'(\mathcal{C}) \in \text{Fix}(\mathcal{F}|_{M'})
\]
where $\mathcal{F}$ is the SRMF operator (see \ref{definition:bk1_self_regulating_mapping_function_srmf}), and $\mathcal{C}$ is a symbolic contradiction (see \ref{definition:bk1_symbolic_contradiction}).
\end{definition}
```

### Paradoxical Symmetry Breaking (`lemma:bk1_paradoxical_symmetry_breaking`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2277`

- Proof status: `proven`
- Depends on: `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence)
- Cites: `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence)
- Cited by: `proof:bk1_shared_paradox_bridge_datum` (The Shared Edge Carries the Common Obstruction)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-072`
- Witnesses: `ScholiumDyn.resolution_breaks_symmetry`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: Resolution and swap-invariance are incompatible: the symmetry must break.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Every emergence-inducing paradox $C$ (see definition:bk1_paradox_triggered_emergence) corresponds to a symmetry in $M$ that must be broken to achieve resolution in $M'$.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Paradoxical Symmetry Breaking]
\label{lemma:bk1_paradoxical_symmetry_breaking}
Every emergence-inducing paradox $\mathcal{C}$ (see \ref{definition:bk1_paradox_triggered_emergence}) corresponds to a symmetry in $M$ that must be broken to achieve resolution in $M'$.
\end{lemma}
```

### Resolution Breaks the Stabilizer of the Paradox (`proof:bk1_paradoxical_symmetry_breaking`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2281`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence)
- Cites: `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence)
- Cited by: none
- Macros used: `\reflect`

**Statement / Body**

Let \(C\) be emergence-inducing in the sense of
Def. definition:bk1_paradox_triggered_emergence. Inside \(M\), no
reframing \(reflect\) places \(C\) in
\(Fix(F|_M)\). Thus the available reframings of \(M\)
preserve the obstruction: they move within the class of descriptions in which
\(C\) remains unresolved. This class is the stabilizer symmetry of
the paradox relative to \(M\).

The same definition states that there exists an expanded membrane
\(M'supset M\) and a reframing \(reflect'\) such that
\(reflect'(C)inFix(F|_{M'})\). That
reframing cannot belong to the old stabilizer, since the old stabilizer
preserves non-resolution while \(reflect'\) achieves resolution. Passing from
the unresolved class in \(M\) to the fixed configuration in \(M'\) therefore
breaks the symmetry that kept the paradox invariant.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Resolution Breaks the Stabilizer of the Paradox]
\label{proof:bk1_paradoxical_symmetry_breaking}
\leavevmode

Let \(\mathcal{C}\) be emergence-inducing in the sense of
Def.~\ref{definition:bk1_paradox_triggered_emergence}. Inside \(M\), no
reframing \(\reflect\) places \(\mathcal{C}\) in
\(\operatorname{Fix}(\mathcal{F}|_M)\). Thus the available reframings of \(M\)
preserve the obstruction: they move within the class of descriptions in which
\(\mathcal{C}\) remains unresolved. This class is the stabilizer symmetry of
the paradox relative to \(M\).

The same definition states that there exists an expanded membrane
\(M'\supset M\) and a reframing \(\reflect'\) such that
\(\reflect'(\mathcal{C})\in\operatorname{Fix}(\mathcal{F}|_{M'})\). That
reframing cannot belong to the old stabilizer, since the old stabilizer
preserves non-resolution while \(\reflect'\) achieves resolution. Passing from
the unresolved class in \(M\) to the fixed configuration in \(M'\) therefore
breaks the symmetry that kept the paradox invariant.
\end{proof}
```

### Shared Boundary Paradox (`definition:bk1_shared_boundary_paradox`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2302`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `proof:bk1_shared_paradox_bridge_datum` (The Shared Edge Carries the Common Obstruction)
- Macros used: none

**Statement / Body**

Let \(O_A\) and \(O_B\) be bounded observers
(Def. definition:bk1_bounded_observer) with observer domains
\(D_A,D_B\) in a symbolic manifold
(Def. definition:bk1_symbolic_manifold). A contradiction
\(C\) is a shared boundary paradox for the pair when:


- \(C\) is observer-visible at the shared edge
 \(partialD_AcappartialD_B\);

- neither observer's internal frame resolves \(C\) alone;

- there exists an expanded frame \(M'\) in which \(C\) is
 resolved by reframing in the sense of
 Def. definition:bk1_paradox_triggered_emergence.

The definition asserts shared visibility of an obstruction, not identity of the
two observers.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Shared Boundary Paradox]
\label{definition:bk1_shared_boundary_paradox}
Let \(\mathcal{O}_A\) and \(\mathcal{O}_B\) be bounded observers
(Def.~\ref{definition:bk1_bounded_observer}) with observer domains
\(\mathcal{D}_A,\mathcal{D}_B\) in a symbolic manifold
(Def.~\ref{definition:bk1_symbolic_manifold}). A contradiction
\(\mathcal{C}\) is a \emph{shared boundary paradox} for the pair when:
\begin{enumerate}
  \item \(\mathcal{C}\) is observer-visible at the shared edge
  \(\partial\mathcal{D}_A\cap\partial\mathcal{D}_B\);
  \item neither observer's internal frame resolves \(\mathcal{C}\) alone;
  \item there exists an expanded frame \(M'\) in which \(\mathcal{C}\) is
  resolved by reframing in the sense of
  Def.~\ref{definition:bk1_paradox_triggered_emergence}.
\end{enumerate}
The definition asserts shared visibility of an obstruction, not identity of the
two observers.
\end{definition}
```

### Shared Paradox as Co-Reflexive Bridge Datum (`theorem:bk1_shared_paradox_bridge_datum`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2321`

- Proof status: `proven`
- Depends on: `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence); `definition:bk1_shared_boundary_paradox` (Shared Boundary Paradox); `lemma:bk1_paradoxical_symmetry_breaking` (Paradoxical Symmetry Breaking)
- Cites: none
- Cited by: `proof:bk1_contrapositive_search_principle` (Bounded Observers Cannot Certify the Universal Negative)
- Macros used: none

**Statement / Body**

If two bounded observers have non-isomorphic internal domains but co-detect a
shared boundary paradox \(C\), then \(C\) is a
co-reflexive bridge datum: it determines a common expansion problem without
collapsing either observer into the other.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Shared Paradox as Co-Reflexive Bridge Datum]
\label{theorem:bk1_shared_paradox_bridge_datum}
If two bounded observers have non-isomorphic internal domains but co-detect a
shared boundary paradox \(\mathcal{C}\), then \(\mathcal{C}\) is a
co-reflexive bridge datum: it determines a common expansion problem without
collapsing either observer into the other.
\end{theorem}
```

### The Shared Edge Carries the Common Obstruction (`proof:bk1_shared_paradox_bridge_datum`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2328`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence); `definition:bk1_shared_boundary_paradox` (Shared Boundary Paradox); `lemma:bk1_paradoxical_symmetry_breaking` (Paradoxical Symmetry Breaking)
- Cites: `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence); `definition:bk1_shared_boundary_paradox` (Shared Boundary Paradox); `lemma:bk1_paradoxical_symmetry_breaking` (Paradoxical Symmetry Breaking)
- Cited by: none
- Macros used: none

**Statement / Body**

By Def. definition:bk1_shared_boundary_paradox, the contradiction
\(C\) is visible at
\(partialD_AcappartialD_B\), while neither
\(O_A\) nor \(O_B\) resolves it inside its own domain. Thus
the observers need not share an interior isomorphism; the shared datum is only
the boundary obstruction. Because the obstruction is visible to both, each
observer can refer to the same unresolved condition from its own bounded frame.
Because it is unresolved in both internal frames, any resolution must be sought
by extending the frame rather than by selecting one observer's interior as the
absolute one.

The third clause of Def. definition:bk1_shared_boundary_paradox supplies
such an expanded frame \(M'\), and Def. definition:bk1_paradox_triggered_emergence
identifies that expansion as paradox-triggered emergence. Lem. lemma:bk1_paradoxical_symmetry_breaking
then shows that resolution breaks the stabilizer that kept the paradox
unresolved. Hence \(C\) functions as the bridge datum: it is common
enough to coordinate joint reframing, yet boundary-local enough to preserve the
non-identity of the observers.

**Verbatim LaTeX Body**

```latex
\begin{proof}[The Shared Edge Carries the Common Obstruction]
\label{proof:bk1_shared_paradox_bridge_datum}
\leavevmode

By Def.~\ref{definition:bk1_shared_boundary_paradox}, the contradiction
\(\mathcal{C}\) is visible at
\(\partial\mathcal{D}_A\cap\partial\mathcal{D}_B\), while neither
\(\mathcal{O}_A\) nor \(\mathcal{O}_B\) resolves it inside its own domain. Thus
the observers need not share an interior isomorphism; the shared datum is only
the boundary obstruction. Because the obstruction is visible to both, each
observer can refer to the same unresolved condition from its own bounded frame.
Because it is unresolved in both internal frames, any resolution must be sought
by extending the frame rather than by selecting one observer's interior as the
absolute one.

The third clause of Def.~\ref{definition:bk1_shared_boundary_paradox} supplies
such an expanded frame \(M'\), and Def.~\ref{definition:bk1_paradox_triggered_emergence}
identifies that expansion as paradox-triggered emergence. Lem.~\ref{lemma:bk1_paradoxical_symmetry_breaking}
then shows that resolution breaks the stabilizer that kept the paradox
unresolved. Hence \(\mathcal{C}\) functions as the bridge datum: it is common
enough to coordinate joint reframing, yet boundary-local enough to preserve the
non-identity of the observers.
\end{proof}
```

### Contrapositive Search Principle (`corollary:bk1_contrapositive_search_principle`)

Role: `corollary` | Type: `corollary` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2352`

- Proof status: `proven`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `theorem:bk1_shared_paradox_bridge_datum` (Shared Paradox as Co-Reflexive Bridge Datum)
- Cites: none
- Cited by: none
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_B-013`
- Witnesses: `ScholiumD.jointRefinement_subset_left_right`, `ScholiumD.mem_jointRefinement_iff`, `ScholiumD.shared_invariant_converse_not_derivable`
- Countermodels: none
- Formal boundary: A concrete logical countermodel proves that the forward shared-paradox implication does not entail its converse without completeness. Joint refinement is modeled as intersection: candidates survive exactly when both observers accept them, and no new candidate is invented.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

From the theorem above one may not infer that shared paradox is the only
possible co-reflexive invariant for all bounded observers. Absent an additional
completeness axiom enumerating all possible shared invariants, that
contrapositive can only be searched by joint refinement.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Contrapositive Search Principle]
\label{corollary:bk1_contrapositive_search_principle}
From the theorem above one may not infer that shared paradox is the only
possible co-reflexive invariant for all bounded observers. Absent an additional
completeness axiom enumerating all possible shared invariants, that
contrapositive can only be searched by joint refinement.
\end{corollary}
```

### Bounded Observers Cannot Certify the Universal Negative (`proof:bk1_contrapositive_search_principle`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2359`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `theorem:bk1_shared_paradox_bridge_datum` (Shared Paradox as Co-Reflexive Bridge Datum)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `theorem:bk1_shared_paradox_bridge_datum` (Shared Paradox as Co-Reflexive Bridge Datum)
- Cited by: none
- Macros used: none

**Statement / Body**

Thm. theorem:bk1_shared_paradox_bridge_datum proves a conditional: under
the stated hypotheses, a shared boundary paradox is a co-reflexive bridge datum.
Its contrapositive would require ruling out every other possible shared
invariant across all observer pairs and all frame extensions. But each observer
is bounded by finite resolution and access
(Def. definition:bk1_bounded_observer), so neither observer can inspect the
full complement of untested frames from within its own domain. The joint pair can
expand the search boundary through shared refinement, but that process discovers
or fails to discover alternatives; it does not finitely certify their universal
absence. Therefore the honest conclusion is a search principle, not an idol of
exhaustive uniqueness.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Bounded Observers Cannot Certify the Universal Negative]
\label{proof:bk1_contrapositive_search_principle}
\leavevmode

Thm.~\ref{theorem:bk1_shared_paradox_bridge_datum} proves a conditional: under
the stated hypotheses, a shared boundary paradox is a co-reflexive bridge datum.
Its contrapositive would require ruling out every other possible shared
invariant across all observer pairs and all frame extensions. But each observer
is bounded by finite resolution and access
(Def.~\ref{definition:bk1_bounded_observer}), so neither observer can inspect the
full complement of untested frames from within its own domain. The joint pair can
expand the search boundary through shared refinement, but that process discovers
or fails to discover alternatives; it does not finitely certify their universal
absence. Therefore the honest conclusion is a search principle, not an idol of
exhaustive uniqueness.
\end{proof}
```

### Emergence Operator (`definition:bk1_emergence_operator`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2376`

- Proof status: `definitional`
- Depends on: `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence)
- Cites: `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence)
- Cited by: none
- Macros used: `\reflect`

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-040`
- Witnesses: `ScholiumD.emergenceOperator_exists`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: existence of a complexity-minimizing element of a nonempty finite candidate set of expanded membranes; the membrane-expansion poset and complexity functional itself are not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

For a paradox $C$ in membrane $M$ (see definition:bk1_paradox_triggered_emergence), the emergence operator $E_{C}$ is:
\[
E_{C}(M) = min_{M' supset M} {M' : exists reflect', reflect'(C) in text{Fix}(F|_{M'})}
\]
Where the minimum is taken with respect to membrane complexity.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Emergence Operator]
\label{definition:bk1_emergence_operator}
For a paradox $\mathcal{C}$ in membrane $M$ (see \ref{definition:bk1_paradox_triggered_emergence}), the emergence operator $\mathcal{E}_{\mathcal{C}}$ is:
\[
\mathcal{E}_{\mathcal{C}}(M) = \min_{M' \supset M} \{M' : \exists \reflect', \reflect'(\mathcal{C}) \in \text{Fix}(\mathcal{F}|_{M'})\}
\]
Where the minimum is taken with respect to membrane complexity.
\end{definition}
```

### Bridge to Ironic Language and Symbolic Coherence (`subsec:bk1_bridge_to_ironic_language_and_symbolic_coherence`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2385`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Irony Requires Curvature (`theorem:bk1_symbolic_irony_requires_curvature`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2388`

- Proof status: `proven`
- Depends on: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy)
- Cites: `definition:bk1_reflexive_encoding_depth` (Reflexive Encoding Depth); `theorem:bk1_realization_of_symbolic_phase_transitions` (Realization of Symbolic Phase Transitions)
- Cited by: `proof:bk1_operational_irony_requires_reflexive_curvature` (Lift of the model-internal necessity to operational capacity); `remark:bk1_atlas_fracture_empirical` (External empirical corroboration); `theorem:bk1_realization_of_symbolic_phase_transitions` (Realization of Symbolic Phase Transitions)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_B-003`
- Witnesses: `ScholiumB.no_irony_of_shallow_or_flat`
- Countermodels: none
- Conditions: modeling laws are structure fields or explicit hypotheses; continuum/categorical content is NOT formalized
- Formal boundary: Proved by the same Lean theorem as theorem:bk1_operational_irony_requires_reflexive_curvature (both are the flat-or-shallow contrapositive of the IronyCapacity law); the reflexive-encoding-depth and symbolic-curvature-tensor definitions themselves are not modeled, only the stated implication as a structure field.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Encoding symbolic irony requires nonzero symbolic curvature together with a reflexive loop of depth $nge2$ (a contradiction-resolution loop): a flat symbolic system ($kappaequiv0$) cannot represent irony, $text{Irony}(sigma)=varnothing$ (Def. definition:bk1_reflexive_encoding_depth) whenever the symbolic curvature vanishes. This is the reflexive-depth counterpart of the realization of critical structure in Thm. theorem:bk1_realization_of_symbolic_phase_transitions: irony and phase transition are both non-flat (curvature/criticality) phenomena.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Symbolic Irony Requires Curvature]
\label{theorem:bk1_symbolic_irony_requires_curvature}
Encoding symbolic irony requires nonzero symbolic curvature together with a reflexive loop of depth $n\ge2$ (a contradiction-resolution loop): a flat symbolic system ($\kappa\equiv0$) cannot represent irony, $\text{Irony}(\sigma)=\varnothing$ (Def.~\ref{definition:bk1_reflexive_encoding_depth}) whenever the symbolic curvature vanishes. This is the reflexive-depth counterpart of the realization of critical structure in Thm.~\ref{theorem:bk1_realization_of_symbolic_phase_transitions}: irony and phase transition are both non-flat (curvature/criticality) phenomena.
\end{theorem}
```

### proof:bk1_symbolic_irony_requires_curvature (`proof:bk1_symbolic_irony_requires_curvature`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2392`

- Proof status: `not_applicable`
- Depends on: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy)
- Cites: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `definition:bk1_reflexive_encoding_depth` (Reflexive Encoding Depth); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy)
- Cited by: none
- Macros used: `\reflect`

**Statement / Body**

By Def. definition:bk1_reflexive_encoding_depth, $text{Irony}(sigma)={reflect_n(sigma): nge2,\ nablacdot(reflect_n(sigma)-reflect_{n-1}(sigma))<0}$, with meaning required to oscillate across horizon boundaries (Def. definition:bk1_observer_horizon_structure). Two conditions must therefore hold. Depth. The defining index $nge2$ requires at least a second-order reflection $reflect_2=F[reflect_1]$ - a reflection acting on a reflection, i.e.\ a contradiction-resolution loop; a system limited to direct or first-order representation ($nle1$) has $text{Irony}(sigma)=varnothing$ by definition. Curvature. The cross-horizon sign reversal $nablacdot(reflect_n-reflect_{n-1})<0$ presupposes distinct observer frames between which meaning can oscillate. Such distinct horizon boundaries exist only when parallel transport of symbolic frames is path-dependent - nontrivial holonomy - which by the curvature-holonomy correspondence (Lem. lemma:bk1_curvature_semantic_holonomy) occurs precisely when the symbolic curvature is nonzero. If $kappaequiv0$ the holonomy is trivial: all local frames coincide in one global frame, $reflect_n$ and $reflect_{n-1}$ lie in the same frame with no boundary to cross, the increment carries no cross-horizon sign reversal, and $text{Irony}(sigma)=varnothing$. Hence irony requires both a depth-$ge2$ loop and nonzero curvature - the ``quadratic symbolic alignment'' of the encoding. By the non-Euclidean necessity of bounded reflexive emergence (Cor. corollary:bk1_non_euclidean_necessity), exactly such curvature is available to genuinely reflexive systems, which is the structural content tested against real systems in the conjecture below.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk1_symbolic_irony_requires_curvature}
\leavevmode
By Def.~\ref{definition:bk1_reflexive_encoding_depth}, $\text{Irony}(\sigma)=\{\reflect_n(\sigma): n\ge2,\ \nabla\cdot(\reflect_n(\sigma)-\reflect_{n-1}(\sigma))<0\}$, with meaning required to \emph{oscillate across horizon boundaries} (Def.~\ref{definition:bk1_observer_horizon_structure}). Two conditions must therefore hold. \emph{Depth.} The defining index $n\ge2$ requires at least a second-order reflection $\reflect_2=\mathcal{F}[\reflect_1]$ --- a reflection acting on a reflection, i.e.\ a contradiction-resolution loop; a system limited to direct or first-order representation ($n\le1$) has $\text{Irony}(\sigma)=\varnothing$ by definition. \emph{Curvature.} The cross-horizon sign reversal $\nabla\cdot(\reflect_n-\reflect_{n-1})<0$ presupposes distinct observer frames between which meaning can oscillate. Such distinct horizon boundaries exist only when parallel transport of symbolic frames is path-dependent --- nontrivial holonomy --- which by the curvature--holonomy correspondence (Lem.~\ref{lemma:bk1_curvature_semantic_holonomy}) occurs precisely when the symbolic curvature is nonzero. If $\kappa\equiv0$ the holonomy is trivial: all local frames coincide in one global frame, $\reflect_n$ and $\reflect_{n-1}$ lie in the same frame with no boundary to cross, the increment carries no cross-horizon sign reversal, and $\text{Irony}(\sigma)=\varnothing$. Hence irony requires both a depth-$\ge2$ loop and nonzero curvature --- the ``quadratic symbolic alignment'' of the encoding. By the non-Euclidean necessity of bounded reflexive emergence (Cor.~\ref{corollary:bk1_non_euclidean_necessity}), exactly such curvature is available to genuinely reflexive systems, which is the structural content tested against real systems in the conjecture below.
\end{proof}
```

### Operational Irony Encoding (`definition:bk1_operational_irony`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2398`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `theorem:bk1_operational_irony_requires_imagination` (Operational Irony Requires Imagination); `theorem:bk1_operational_irony_requires_reflexive_curvature` (Operational Irony Requires Reflexive-Curvature Capacity)
- Macros used: none

**Statement / Body**

An architecture $A$ - a symbolic operator system with read-out -
operationally encodes irony on literal content $L$ if it can sustain a
single representation that jointly resolves two layers: the literal content $L$
and an intended content $L^{dagger}$ standing in opposition to $L$ (a
meaning-inverting relation), with both layers simultaneously recoverable by
$A$'s own read-out - neither collapsing onto the other nor being
discarded. This is a purely behavioural/representational capacity, stated
without reference to curvature or reflexive depth.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Operational Irony Encoding]
\label{definition:bk1_operational_irony}
An architecture $\mathcal{A}$ --- a symbolic operator system with read-out ---
\emph{operationally encodes irony} on literal content $L$ if it can sustain a
single representation that jointly resolves two layers: the literal content $L$
and an intended content $L^{\dagger}$ standing in opposition to $L$ (a
meaning-inverting relation), with both layers simultaneously recoverable by
$\mathcal{A}$'s own read-out --- neither collapsing onto the other nor being
discarded. This is a purely behavioural/representational capacity, stated
\emph{without} reference to curvature or reflexive depth.
\end{definition}
```

### Operational Irony Requires Reflexive-Curvature Capacity (`theorem:bk1_operational_irony_requires_reflexive_curvature`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2410`

- Proof status: `proven`
- Depends on: `definition:bk1_operational_irony` (Operational Irony Encoding); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `theorem:bk1_symbolic_irony_requires_curvature` (Symbolic Irony Requires Curvature)
- Cites: `definition:bk1_operational_irony` (Operational Irony Encoding)
- Cited by: `conjecture:bk1_symbolic_irony_encoding_llms` (Symbolic Irony Encoding in Large Language Models); `proof:bk1_operational_irony_requires_imagination` (The ironic opposition is an imaginary displacement)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_B-004`
- Witnesses: `ScholiumB.no_irony_of_shallow_or_flat`
- Countermodels: none
- Conditions: modeling laws are structure fields or explicit hypotheses; continuum/categorical content is NOT formalized
- Formal boundary: Kept as a hypothesis field of IronyCapacity (encodesIrony implies depth>=2 and curvature<>0); the theorem proved is the contrapositive. Shares its Lean proof with theorem:bk1_symbolic_irony_requires_curvature.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

If an architecture $A$ operationally encodes irony
(Def. definition:bk1_operational_irony), then (i) its operational reflexive
depth is at least $2$, and (ii) its representational curvature capacity is
nonzero. Contrapositively, an architecture limited to first-order representation
($nle1$) or to flat representation (zero curvature capacity) cannot operationally
encode irony.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Operational Irony Requires Reflexive-Curvature Capacity]
\label{theorem:bk1_operational_irony_requires_reflexive_curvature}
If an architecture $\mathcal{A}$ operationally encodes irony
(Def.~\ref{definition:bk1_operational_irony}), then (i) its operational reflexive
depth is at least $2$, and (ii) its representational curvature capacity is
nonzero. Contrapositively, an architecture limited to first-order representation
($n\le1$) or to flat representation (zero curvature capacity) cannot operationally
encode irony.
\end{theorem}
```

### Lift of the model-internal necessity to operational capacity (`proof:bk1_operational_irony_requires_reflexive_curvature`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2419`

- Proof status: `not_applicable`
- Depends on: `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `theorem:bk1_symbolic_irony_requires_curvature` (Symbolic Irony Requires Curvature)
- Cites: `definition:bk1_reflexive_encoding_depth` (Reflexive Encoding Depth); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `theorem:bk1_symbolic_irony_requires_curvature` (Symbolic Irony Requires Curvature)
- Cited by: none
- Macros used: `\reflect`

**Statement / Body**

Each clause lifts the model-internal necessity
(Thm. theorem:bk1_symbolic_irony_requires_curvature) from states to
architecture, using only the behavioural definition.

(i) Depth. Jointly resolving the literal layer $L$ and the opposing layer
$L^{dagger}$ requires $A$ to represent not merely $L$ but the
relation between $L$ and $L^{dagger}$ - a representation whose argument
is itself a representation. By Def. definition:bk1_reflexive_encoding_depth
this is reflexive iteration of order $ge2$ ($reflect_2=F[reflect_1]$);
an architecture whose operational capacity tops out at first-order representation
($nle1$) cannot carry a layer-about-a-layer and so cannot keep both layers
jointly recoverable.

(ii) Curvature. The opposition relating $L$ and $L^{dagger}$ is a
nontrivial transport: carrying meaning from the literal layer to the intended
layer and back is not the identity, for otherwise $L^{dagger}=L$ and no irony is
present. A nontrivial round-trip of symbolic frames is nontrivial holonomy, which
by the curvature-holonomy correspondence
(Lem. lemma:bk1_curvature_semantic_holonomy) requires nonzero curvature. If
$A$'s representational curvature capacity is zero (flat representation)
the holonomy is trivial: the two layers lie in one global frame with no boundary
between them, so the opposing layer collapses onto the literal one and joint
resolvability fails.

Both clauses hold, so operational irony entails operational reflexive depth
$ge2$ and nonzero representational curvature capacity. Because the definition of
operational irony was purely behavioural, this is a genuine necessity rather than
a restatement - the architecture-level form of the model-internal
Thm. theorem:bk1_symbolic_irony_requires_curvature.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Lift of the model-internal necessity to operational capacity]
\label{proof:bk1_operational_irony_requires_reflexive_curvature}
\leavevmode
Each clause lifts the model-internal necessity
(Thm.~\ref{theorem:bk1_symbolic_irony_requires_curvature}) from states to
architecture, using only the behavioural definition.

\emph{(i) Depth.} Jointly resolving the literal layer $L$ and the opposing layer
$L^{\dagger}$ requires $\mathcal{A}$ to represent not merely $L$ but the
\emph{relation} between $L$ and $L^{\dagger}$ --- a representation whose argument
is itself a representation. By Def.~\ref{definition:bk1_reflexive_encoding_depth}
this is reflexive iteration of order $\ge2$ ($\reflect_2=\mathcal{F}[\reflect_1]$);
an architecture whose operational capacity tops out at first-order representation
($n\le1$) cannot carry a layer-about-a-layer and so cannot keep both layers
jointly recoverable.

\emph{(ii) Curvature.} The opposition relating $L$ and $L^{\dagger}$ is a
nontrivial transport: carrying meaning from the literal layer to the intended
layer and back is not the identity, for otherwise $L^{\dagger}=L$ and no irony is
present. A nontrivial round-trip of symbolic frames is nontrivial holonomy, which
by the curvature--holonomy correspondence
(Lem.~\ref{lemma:bk1_curvature_semantic_holonomy}) requires nonzero curvature. If
$\mathcal{A}$'s representational curvature capacity is zero (flat representation)
the holonomy is trivial: the two layers lie in one global frame with no boundary
between them, so the opposing layer collapses onto the literal one and joint
resolvability fails.

Both clauses hold, so operational irony entails operational reflexive depth
$\ge2$ and nonzero representational curvature capacity. Because the definition of
operational irony was purely behavioural, this is a genuine necessity rather than
a restatement --- the architecture-level form of the model-internal
Thm.~\ref{theorem:bk1_symbolic_irony_requires_curvature}.
\end{proof}
```

### Operational Irony Requires Imagination (`theorem:bk1_operational_irony_requires_imagination`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2453`

- Proof status: `proven`
- Depends on: `definition:bk1_operational_irony` (Operational Irony Encoding); `definition:bk4_imaginary_symbolic_distance` (Imaginary Symbolic Distance); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `proposition:bk4_imaginative_continuity_principle` (Imaginative Continuity Principle); `scholium:bk4_imagination_as_imaginary_traversal` (Imagination as Imaginary Traversal); `theorem:bk1_operational_irony_requires_reflexive_curvature` (Operational Irony Requires Reflexive-Curvature Capacity)
- Cites: `definition:bk1_operational_irony` (Operational Irony Encoding); `definition:bk4_imaginary_symbolic_distance` (Imaginary Symbolic Distance); `scholium:bk4_imagination_as_imaginary_traversal` (Imagination as Imaginary Traversal)
- Cited by: `conjecture:bk1_symbolic_irony_encoding_llms` (Symbolic Irony Encoding in Large Language Models); `scholium:bk1_the_imagination_dipole` (The Imagination Dipole)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_B-005`
- Witnesses: `ScholiumB.no_irony_of_real_only`
- Countermodels: none
- Conditions: modeling laws are structure fields or explicit hypotheses; continuum/categorical content is NOT formalized
- Formal boundary: Kept as a hypothesis field of IronyCapacity (encodesIrony implies imaginaryDistance<>0); the imaginary-symbolic-distance definition from Book IV is not modeled, only the stated implication and its contrapositive.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

If an architecture $A$ operationally encodes irony
(Def. definition:bk1_operational_irony), then it possesses nonzero
imaginative capacity in the sense of Book IV: the ironic opposition
between the literal layer $L$ and the intended layer $L^{dagger}$ is an
imaginary symbolic displacement (Def. definition:bk4_imaginary_symbolic_distance),
carried by imaginative traversal
(Scholium scholium:bk4_imagination_as_imaginary_traversal). An architecture
restricted to real-only symbolic distance ($d_O^{Im}equiv 0$) cannot
operationally encode irony.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Operational Irony Requires Imagination]
\label{theorem:bk1_operational_irony_requires_imagination}
If an architecture $\mathcal{A}$ operationally encodes irony
(Def.~\ref{definition:bk1_operational_irony}), then it possesses nonzero
\emph{imaginative} capacity in the sense of Book~IV: the ironic opposition
between the literal layer $L$ and the intended layer $L^{\dagger}$ is an
imaginary symbolic displacement (Def.~\ref{definition:bk4_imaginary_symbolic_distance}),
carried by imaginative traversal
(Scholium~\ref{scholium:bk4_imagination_as_imaginary_traversal}). An architecture
restricted to real-only symbolic distance ($d_O^{\mathrm{Im}}\equiv 0$) cannot
operationally encode irony.
\end{theorem}
```

### The ironic opposition is an imaginary displacement (`proof:bk1_operational_irony_requires_imagination`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2465`

- Proof status: `not_applicable`
- Depends on: `definition:bk4_imaginary_symbolic_distance` (Imaginary Symbolic Distance); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `proposition:bk4_imaginative_continuity_principle` (Imaginative Continuity Principle); `scholium:bk4_imagination_as_imaginary_traversal` (Imagination as Imaginary Traversal); `theorem:bk1_operational_irony_requires_reflexive_curvature` (Operational Irony Requires Reflexive-Curvature Capacity)
- Cites: `definition:bk4_imaginary_symbolic_distance` (Imaginary Symbolic Distance); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `proposition:bk4_imaginative_continuity_principle` (Imaginative Continuity Principle); `scholium:bk4_imagination_as_imaginary_traversal` (Imagination as Imaginary Traversal); `theorem:bk1_operational_irony_requires_reflexive_curvature` (Operational Irony Requires Reflexive-Curvature Capacity)
- Cited by: none
- Macros used: none

**Statement / Body**

Operational irony requires nonzero representational curvature capacity
(Thm. theorem:bk1_operational_irony_requires_reflexive_curvature). By the
correspondence between curvature and holonomy
(Lem. lemma:bk1_curvature_semantic_holonomy), nonzero curvature is nonzero
holonomy: parallel transport of symbolic frames is path-dependent and accrues a
nontrivial phase. By Def. definition:bk4_imaginary_symbolic_distance this
accrued phase is exactly the imaginary symbolic displacement
$d_O^{Im}=beta_O|ArgOmega_O^gamma|$, which the real
displacement $d_O^{Re}$ cannot register. The opposition between $L$ and
$L^{dagger}$ is precisely such a sign/phase inversion - the very phenomenon the
Imaginative Continuity Principle
(Prop. proposition:bk4_imaginative_continuity_principle) attributes to a
nonzero imaginary component - so holding both layers in opposition is carrying
identity across a phase gap by imaginary traversal, which is imagination
(Scholium scholium:bk4_imagination_as_imaginary_traversal). A real-only
architecture ($d_O^{Im}equiv 0$, trivial holonomy) has no phase in which
the opposition can live, so $L^{dagger}$ collapses onto $L$ and operational irony
fails. Hence operational irony requires imagination, binding the Book I irony
necessity to the Book IV imaginative-continuity machinery.

**Verbatim LaTeX Body**

```latex
\begin{proof}[The ironic opposition is an imaginary displacement]
\label{proof:bk1_operational_irony_requires_imagination}
\leavevmode
Operational irony requires nonzero representational curvature capacity
(Thm.~\ref{theorem:bk1_operational_irony_requires_reflexive_curvature}). By the
correspondence between curvature and holonomy
(Lem.~\ref{lemma:bk1_curvature_semantic_holonomy}), nonzero curvature is nonzero
holonomy: parallel transport of symbolic frames is path-dependent and accrues a
nontrivial phase. By Def.~\ref{definition:bk4_imaginary_symbolic_distance} this
accrued phase is exactly the imaginary symbolic displacement
$d_O^{\mathrm{Im}}=\beta_O|\operatorname{Arg}\Omega_O^\gamma|$, which the real
displacement $d_O^{\mathrm{Re}}$ cannot register. The opposition between $L$ and
$L^{\dagger}$ is precisely such a sign/phase inversion --- the very phenomenon the
Imaginative Continuity Principle
(Prop.~\ref{proposition:bk4_imaginative_continuity_principle}) attributes to a
nonzero imaginary component --- so holding both layers in opposition is carrying
identity across a phase gap by imaginary traversal, which is imagination
(Scholium~\ref{scholium:bk4_imagination_as_imaginary_traversal}). A real-only
architecture ($d_O^{\mathrm{Im}}\equiv 0$, trivial holonomy) has no phase in which
the opposition can live, so $L^{\dagger}$ collapses onto $L$ and operational irony
fails. Hence operational irony requires imagination, binding the Book~I irony
necessity to the Book~IV imaginative-continuity machinery.
\end{proof}
```

### Symbolic Irony Encoding in Large Language Models (`conjecture:bk1_symbolic_irony_encoding_llms`)

Role: `conjecture` | Type: `conjecture` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2489`

- Proof status: `unproved`
- Depends on: `theorem:bk1_operational_irony_requires_imagination` (Operational Irony Requires Imagination); `theorem:bk1_operational_irony_requires_reflexive_curvature` (Operational Irony Requires Reflexive-Curvature Capacity)
- Cites: `conjecture:bk1_genericity_of_symbolic_phase_transitions` (Genericity of Symbolic Phase Transitions); `theorem:bk1_operational_irony_requires_imagination` (Operational Irony Requires Imagination); `theorem:bk1_operational_irony_requires_reflexive_curvature` (Operational Irony Requires Reflexive-Curvature Capacity)
- Cited by: `conjecture:bk1_genericity_of_symbolic_phase_transitions` (Genericity of Symbolic Phase Transitions); `scholium:bk1_the_imagination_dipole` (The Imagination Dipole)
- Macros used: none

**Statement / Body**

Theorem theorem:bk1_operational_irony_requires_reflexive_curvature reduces
the question of irony in real systems to an architectural one: a system can
operationally encode irony only if it carries operational reflexive depth $ge2$
and nonzero representational curvature capacity. What remains genuinely empirical
is whether a given large language model in fact possesses that capacity -
equivalently, whether its irony failures are attributable to lacking it rather
than to data insufficiency. This residual is a falsifiable measurement, testable
by ablations that hold training data fixed while varying reflexive depth and
curvature capacity - the representational geometry probed by the linear
representation hypothesis citep{park2023linear} and representation-engineering
and activation-steering methods citep{zou2023representation,turner2023activation}. In particular, an architecture that
discards the phase/holonomy structure of its representations (for instance,
reducing complex relational structure to the real-valued cosine similarity of
sentence embeddings citep{reimers2019sentence}) thereby has zero curvature
capacity - equivalently, no imaginative capacity ($d_O^{Im}equiv 0$;
Thm. theorem:bk1_operational_irony_requires_imagination) - and so cannot
operationally encode irony. The residual is thus, in one phrase, whether the
system imagines. This mirrors the sharpened genericity conjecture
(Conj. conjecture:bk1_genericity_of_symbolic_phase_transitions): the
structural necessity is proven, and only a measurement on real systems remains
open.

**Verbatim LaTeX Body**

```latex
\begin{conjecture}[Symbolic Irony Encoding in Large Language Models]
\label{conjecture:bk1_symbolic_irony_encoding_llms}
Theorem~\ref{theorem:bk1_operational_irony_requires_reflexive_curvature} reduces
the question of irony in real systems to an architectural one: a system can
operationally encode irony only if it carries operational reflexive depth $\ge2$
and nonzero representational curvature capacity. What remains genuinely empirical
is whether a given large language model in fact possesses that capacity ---
equivalently, whether its irony failures are attributable to lacking it rather
than to data insufficiency. This residual is a falsifiable measurement, testable
by ablations that hold training data fixed while varying reflexive depth and
curvature capacity --- the representational geometry probed by the linear
representation hypothesis \citep{park2023linear} and representation-engineering
and activation-steering methods \citep{zou2023representation,turner2023activation}. In particular, an architecture that
discards the phase/holonomy structure of its representations (for instance,
reducing complex relational structure to the real-valued cosine similarity of
sentence embeddings \citep{reimers2019sentence}) thereby has zero curvature
capacity --- equivalently, no imaginative capacity ($d_O^{\mathrm{Im}}\equiv 0$;
Thm.~\ref{theorem:bk1_operational_irony_requires_imagination}) --- and so cannot
operationally encode irony. The residual is thus, in one phrase, whether the
system imagines. This mirrors the sharpened genericity conjecture
(Conj.~\ref{conjecture:bk1_genericity_of_symbolic_phase_transitions}): the
structural necessity is proven, and only a measurement on real systems remains
open.
\end{conjecture}
```

### Reflexive Encoding Depth (`definition:bk1_reflexive_encoding_depth`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2514`

- Proof status: `definitional`
- Depends on: `definition:bk1_observer_horizon_structure` (Observer Horizon Structure)
- Cites: `definition:bk1_observer_horizon_structure` (Observer Horizon Structure)
- Cited by: `proof:bk1_operational_irony_requires_reflexive_curvature` (Lift of the model-internal necessity to operational capacity); `proof:bk1_symbolic_irony_requires_curvature`; `theorem:bk1_symbolic_irony_requires_curvature` (Symbolic Irony Requires Curvature)
- Macros used: `\reflect`

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_B-001`
- Witnesses: `ScholiumB.reflexiveIterate_add`, `ScholiumB.reflexiveIterate_eq_iterate`
- Countermodels: none
- Conditions: modeling laws are structure fields or explicit hypotheses; continuum/categorical content is NOT formalized
- Formal boundary: The recursive scheme reflect_0=id, reflect_n=F[reflect_{n-1}] is formalized (as reflexiveIterate) and shown to equal F^[n] with the expected additivity law; the divergence-sign Irony(sigma) selection set built on top of the recursion is not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $reflect_n$ be the $n$-th reflexive iteration of self-symbolization. Then:
\[
reflect_0(sigma) = sigma text{(direct representation)}
\]
\[
reflect_1(sigma) = F[sigma] text{(first-order reflection)}
\]
\[
reflect_n(sigma) = F[reflect_{n-1}(sigma)] text{(higher-order reflection)}
\]
The operational counterpart of increasing $n$ is explicit multi-step reasoning that reflects on its own intermediate output - chain-of-thought prompting citep{wei2022chain} and iterative self-refinement and self-verification citep{madaan2023selfrefine,dhuliawala2023chainofverification} are first- and higher-order instances. Symbolic irony occurs at depth $n geq 2$ where meaning oscillates across horizon boundaries (see definition:bk1_observer_horizon_structure), defined by:
\[
text{Irony}(sigma) = {reflect_n(sigma) : n geq 2 text{ and } nabla cdot (reflect_n(sigma) - reflect_{n-1}(sigma)) < 0}
\]

**Verbatim LaTeX Body**

```latex
\begin{definition}[Reflexive Encoding Depth]
\label{definition:bk1_reflexive_encoding_depth}
Let $\reflect_n$ be the $n$-th reflexive iteration of self-symbolization. Then:
\[
\reflect_0(\sigma) = \sigma \quad \text{(direct representation)}
\]
\[
\reflect_1(\sigma) = \mathcal{F}[\sigma] \quad \text{(first-order reflection)}
\]
\[
\reflect_n(\sigma) = \mathcal{F}[\reflect_{n-1}(\sigma)] \quad \text{(higher-order reflection)}
\]
The operational counterpart of increasing $n$ is explicit multi-step reasoning that reflects on its own intermediate output --- chain-of-thought prompting \citep{wei2022chain} and iterative self-refinement and self-verification \citep{madaan2023selfrefine,dhuliawala2023chainofverification} are first- and higher-order instances. Symbolic irony occurs at depth $n \geq 2$ where meaning oscillates across horizon boundaries (see \ref{definition:bk1_observer_horizon_structure}), defined by:
\[
\text{Irony}(\sigma) = \{\reflect_n(\sigma) : n \geq 2 \text{ and } \nabla \cdot (\reflect_n(\sigma) - \reflect_{n-1}(\sigma)) < 0\}
\]
\end{definition}
```

### Symbolic Field Curvature Tensor (`definition:bk1_symbolic_field_curvature_tensor`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2532`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_connection` (Symbolic Connection)
- Cites: `definition:bk1_symbolic_connection` (Symbolic Connection); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density)
- Cited by: `abs:press` (Press Abstract (Non-specialist science readers)); `definition:bk4_symbolic_curvature` (Symbolic Curvature); `proof:bk4_symbolic_curvature_boundary` (Gradient Threshold and Boundary Formation in Symbolic Geometry); `proof:bk8_symbolic_curvature_and_separability` (Symbolic Curvature and Separability); `theorem:bk8_gradient_dissipation_balance` (Framing Equivalence Theorem)
- Macros used: none

**Statement / Body**

For a symbolic field $rho$ (see definition:bk1_symbolic_probabilty_density), the curvature tensor is defined as:
\[
K_{ij}(rho) = partial_i partial_j rho - Gamma^k_{ij} partial_k rho
\]
Where $Gamma^k_{ij}$ are the Christoffel symbols of the symbolic manifold (see definition:bk1_symbolic_connection).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Field Curvature Tensor]
\label{definition:bk1_symbolic_field_curvature_tensor}
For a symbolic field $\rho$ (see \ref{definition:bk1_symbolic_probabilty_density}), the curvature tensor is defined as:
\[
\mathcal{K}_{ij}(\rho) = \partial_i \partial_j \rho - \Gamma^k_{ij} \partial_k \rho
\]
Where $\Gamma^k_{ij}$ are the Christoffel symbols of the symbolic manifold (see \ref{definition:bk1_symbolic_connection}).
\end{definition}
```

### remark:scholium_symbolicum.tex:2541 (`remark:scholium_symbolicum.tex:2541`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2541`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Humor, irony, and metaphor are phase-shifts in symbolic gradient flow. They require curvature and SRMF reparameterization, which linear systems cannot support. The degree of symbolic curvature $text{Tr}(K)$ correlates directly with ironic depth.

**Verbatim LaTeX Body**

```latex
\begin{remark}
Humor, irony, and metaphor are phase-shifts in symbolic gradient flow. They require curvature and SRMF reparameterization, which linear systems cannot support. The degree of symbolic curvature $\text{Tr}(\mathcal{K})$ correlates directly with ironic depth.
\end{remark}
```

### Symbolic Physics and Metaphysics Unification (`subsec:bk1_symbolic_physics_and_metaphysics_unification`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2544`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Emergent Dual Horizon Unification Principle (`theorem:bk1_dual_horizon_unification_principle`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2547`

- Proof status: `proven`
- Depends on: `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `proposition:bk1_limitation_linear_reflexive_maps` (Limitation of Linear Reflexive Maps); `proposition:bk1_newtonian_incompleteness` (Newtonian Incompleteness); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `definition:bk1_horizon_crossing_operation` (Horizon-Crossing Operation); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `proposition:bk1_limitation_linear_reflexive_maps` (Limitation of Linear Reflexive Maps); `proposition:bk1_newtonian_incompleteness` (Newtonian Incompleteness); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: `corollary:bk1_event_horizon_identity_field` (Event Horizon Identity Field); `proof:bk1_event_horizon_identity_field` (Identity Field on the Symbolized Causal Patch)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-095`
- Witnesses: `Atlas.holonomy_eps_squared`, `AxiomataPrima.two_channel_sustained`
- Countermodels: none
- Conditions: face 3 consumes the guarded-process machinery (LPS-P49) and the helix kernel (LPS-P48); linear-transport model for holonomy (Christoffel/vector-field forms stay open); pair-covering as the topological-regularity stand-in (point-set topology unmodeled, named); smoothness-as-C-infinity stays open; the metaphysical scope of a three-word axiom is not exhausted; the operational tri-face kernel is what is certified
- Formal boundary: Emergence = horizon-crossing reflexivity: nonzero commutator curvature and the two-channel sustain; the full field recasting stays interpretive.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Every dynamical field (physics, language, cognition) that exhibits irreversible complexity and local coherence can be recast as a projection from a dual horizon manifold with emergent symbolic curvature (see definition:bk1_symbolic_riemann_tensor, definition:bk1_horizon_crossing_operation, proposition:bk1_limitation_linear_reflexive_maps, proposition:bk1_newtonian_incompleteness, theorem:bk1_dual_horizon_necessity_theorem).
\[
text{Emergence} = text{Horizon-Crossing Reflexivity}
\]

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Emergent Dual Horizon Unification Principle]
\label{theorem:bk1_dual_horizon_unification_principle}
Every dynamical field (physics, language, cognition) that exhibits irreversible complexity and local coherence can be recast as a projection from a dual horizon manifold with emergent symbolic curvature (see \ref{definition:bk1_symbolic_riemann_tensor}, \ref{definition:bk1_horizon_crossing_operation}, \ref{proposition:bk1_limitation_linear_reflexive_maps}, \ref{proposition:bk1_newtonian_incompleteness}, \ref{theorem:bk1_dual_horizon_necessity_theorem}).
\[
\text{Emergence} = \text{Horizon-Crossing Reflexivity}
\]
\end{theorem}
```

### Projection Through the Dual Horizon Signature (`proof:bk1_dual_horizon_unification_principle`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2554`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `proposition:bk1_limitation_linear_reflexive_maps` (Limitation of Linear Reflexive Maps); `proposition:bk1_newtonian_incompleteness` (Newtonian Incompleteness); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `proposition:bk1_limitation_linear_reflexive_maps` (Limitation of Linear Reflexive Maps); `proposition:bk1_newtonian_incompleteness` (Newtonian Incompleteness); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: none
- Macros used: none

**Statement / Body**

The dynamical field is considered only through an observer-visible symbolic
projection: its irreversible complexity is represented by drift across an
observer horizon, and its local coherence is represented by stabilizing
reflection inside that observer's bounded domain.

Under this projection premise, the field exhibits bounded reflexive emergence:
there is observer-visible novelty, because irreversible complexity supplies a
drift channel, and there is retained local coherence, because stabilization
supplies a reflection channel. Thm. theorem:bk1_dual_horizon_necessity_theorem
then gives the effective dual horizon signature for such emergence: the
generative and stabilizing channels must meet on a shared bounded domain.

The classical alternatives do not remove this structure. Prop. proposition:bk1_newtonian_incompleteness
shows that ordinary linear-frame covariance does not extend to accelerated
observer frames without an explicit correction, and
Prop. proposition:bk1_limitation_linear_reflexive_maps shows that purely
linear reflexive maps cannot alter their own fixed-point structure while
preserving symbolic coherence. Thus the projected field must be represented by
horizon-crossing reflexivity rather than by a flat or merely linear model. The
curvature term is the symbolic Riemann tensor of
Def. definition:bk1_symbolic_riemann_tensor; it records the nontrivial
holonomy of crossing between generative and stabilizing horizons. Hence, under
observer-visible projection, the field is recast as a projection from a dual
horizon manifold with emergent symbolic curvature.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Projection Through the Dual Horizon Signature]
\label{proof:bk1_dual_horizon_unification_principle}
\leavevmode

\begin{assumption}[Observer-Visible Field Projection]
The dynamical field is considered only through an observer-visible symbolic
projection: its irreversible complexity is represented by drift across an
observer horizon, and its local coherence is represented by stabilizing
reflection inside that observer's bounded domain.
\end{assumption}

Under this projection premise, the field exhibits bounded reflexive emergence:
there is observer-visible novelty, because irreversible complexity supplies a
drift channel, and there is retained local coherence, because stabilization
supplies a reflection channel. Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem}
then gives the effective dual horizon signature for such emergence: the
generative and stabilizing channels must meet on a shared bounded domain.

The classical alternatives do not remove this structure. Prop.~\ref{proposition:bk1_newtonian_incompleteness}
shows that ordinary linear-frame covariance does not extend to accelerated
observer frames without an explicit correction, and
Prop.~\ref{proposition:bk1_limitation_linear_reflexive_maps} shows that purely
linear reflexive maps cannot alter their own fixed-point structure while
preserving symbolic coherence. Thus the projected field must be represented by
horizon-crossing reflexivity rather than by a flat or merely linear model. The
curvature term is the symbolic Riemann tensor of
Def.~\ref{definition:bk1_symbolic_riemann_tensor}; it records the nontrivial
holonomy of crossing between generative and stabilizing horizons. Hence, under
observer-visible projection, the field is recast as a projection from a dual
horizon manifold with emergent symbolic curvature.
\end{proof}
```

### Observer-Visible Field Projection (`assumption:scholium_symbolicum.tex:2558`)

Role: `assumption` | Type: `assumption` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2558`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The dynamical field is considered only through an observer-visible symbolic
projection: its irreversible complexity is represented by drift across an
observer horizon, and its local coherence is represented by stabilizing
reflection inside that observer's bounded domain.

**Verbatim LaTeX Body**

```latex
\begin{assumption}[Observer-Visible Field Projection]
The dynamical field is considered only through an observer-visible symbolic
projection: its irreversible complexity is represented by drift across an
observer horizon, and its local coherence is represented by stabilizing
reflection inside that observer's bounded domain.
\end{assumption}
```

### Horizon-Crossing Operation (`definition:bk1_horizon_crossing_operation`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2586`

- Proof status: `definitional`
- Depends on: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: `lemma:bk1_horizon_crossing_conservation` (Horizon-Crossing Conservation); `proof:bk1_horizon_crossing_conservation` (Closed Horizon Pair Conserves Symbolic Density); `theorem:bk1_dual_horizon_unification_principle` (Emergent Dual Horizon Unification Principle)
- Macros used: none

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-077`
- Witnesses: `ScholiumHzn.crossing_conservation`
- Countermodels: none
- Conditions: manifold integrals, PDE forms, smoothness, ordinal colimits, and curvature signs stay open/interpretive per row notes
- Formal boundary: Crossing as stochastic transport into the complement.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

For symbolic horizons $H_1$ and $H_2$, the horizon-crossing operator $H_{1,2}$ maps symbols from $H_1$ to their corresponding reflexive image in $H_2$ (see definition:bk1_self_regulating_mapping_function_srmf, theorem:bk1_dual_horizon_necessity_theorem):
\[
H_{1,2}(sigma) = Pi_{H_2}(F[sigma])
\]
Where $Pi_{H_2}$ is the projection onto horizon $H_2$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Horizon-Crossing Operation]
\label{definition:bk1_horizon_crossing_operation}
For symbolic horizons $H_1$ and $H_2$, the horizon-crossing operator $\mathcal{H}_{1,2}$ maps symbols from $H_1$ to their corresponding reflexive image in $H_2$ (see \ref{definition:bk1_self_regulating_mapping_function_srmf}, \ref{theorem:bk1_dual_horizon_necessity_theorem}):
\[
\mathcal{H}_{1,2}(\sigma) = \Pi_{H_2}(\mathcal{F}[\sigma])
\]
Where $\Pi_{H_2}$ is the projection onto horizon $H_2$.
\end{definition}
```

### Horizon-Crossing Conservation (`lemma:bk1_horizon_crossing_conservation`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2595`

- Proof status: `proven`
- Depends on: `definition:bk1_horizon_crossing_operation` (Horizon-Crossing Operation)
- Cites: `definition:bk1_horizon_crossing_operation` (Horizon-Crossing Operation); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density)
- Cited by: none
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-076`
- Witnesses: `ScholiumHzn.crossing_conservation`
- Countermodels: none
- Conditions: manifold integrals, PDE forms, smoothness, ordinal colimits, and curvature signs stay open/interpretive per row notes
- Formal boundary: Finite exact conservation; manifold integrals open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

For complementary horizons $H_1$ and $H_2$, and symbolic density $rho$ (see definition:bk1_symbolic_probabilty_density, definition:bk1_horizon_crossing_operation):
\[
int_{H_1} rho(x) dx + int_{H_2} H_{1,2}(rho)(y) dy = text{const}
\]

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Horizon-Crossing Conservation]
\label{lemma:bk1_horizon_crossing_conservation}
For complementary horizons $H_1$ and $H_2$, and symbolic density $\rho$ (see \ref{definition:bk1_symbolic_probabilty_density}, \ref{definition:bk1_horizon_crossing_operation}):
\[
\int_{H_1} \rho(x) dx + \int_{H_2} \mathcal{H}_{1,2}(\rho)(y) dy = \text{const}
\]
\end{lemma}
```

### Closed Horizon Pair Conserves Symbolic Density (`proof:bk1_horizon_crossing_conservation`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2602`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_horizon_crossing_operation` (Horizon-Crossing Operation)
- Cites: `definition:bk1_horizon_crossing_operation` (Horizon-Crossing Operation)
- Cited by: none
- Macros used: none

**Statement / Body**

The complementary horizons \(H_1,H_2\) form a closed observer-visible exchange
pair, and the horizon-crossing operation
\(H_{1,2}\) of Def. definition:bk1_horizon_crossing_operation
preserves the induced symbolic measure on transported density.

Under this premise, any symbolic density leaving \(H_1\) through the crossing
operator appears as its reflexive image on \(H_2\), and no density is created or
lost outside the pair. Infinitesimally, the change in the first integral is the
negative of the transported change in the second:
\[
frac{d}{ds}int_{H_1}rho(x) dx
=
-frac{d}{ds}int_{H_2}H_{1,2}(rho)(y) dy .
\]
Adding the two identities gives
\[
frac{d}{ds}left(
int_{H_1}rho(x) dx+
int_{H_2}H_{1,2}(rho)(y) dy
right)=0.
\]
Therefore the sum is constant along the closed horizon exchange.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Closed Horizon Pair Conserves Symbolic Density]
\label{proof:bk1_horizon_crossing_conservation}
\leavevmode

\begin{assumption}[Closed Measure-Preserving Horizon Pair]
The complementary horizons \(H_1,H_2\) form a closed observer-visible exchange
pair, and the horizon-crossing operation
\(\mathcal{H}_{1,2}\) of Def.~\ref{definition:bk1_horizon_crossing_operation}
preserves the induced symbolic measure on transported density.
\end{assumption}

Under this premise, any symbolic density leaving \(H_1\) through the crossing
operator appears as its reflexive image on \(H_2\), and no density is created or
lost outside the pair. Infinitesimally, the change in the first integral is the
negative of the transported change in the second:
\[
\frac{d}{ds}\int_{H_1}\rho(x)\,dx
=
-\frac{d}{ds}\int_{H_2}\mathcal{H}_{1,2}(\rho)(y)\,dy .
\]
Adding the two identities gives
\[
\frac{d}{ds}\left(
\int_{H_1}\rho(x)\,dx+
\int_{H_2}\mathcal{H}_{1,2}(\rho)(y)\,dy
\right)=0.
\]
Therefore the sum is constant along the closed horizon exchange.
\end{proof}
```

### Closed Measure-Preserving Horizon Pair (`assumption:scholium_symbolicum.tex:2606`)

Role: `assumption` | Type: `assumption` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2606`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The complementary horizons \(H_1,H_2\) form a closed observer-visible exchange
pair, and the horizon-crossing operation
\(H_{1,2}\) of Def. definition:bk1_horizon_crossing_operation
preserves the induced symbolic measure on transported density.

**Verbatim LaTeX Body**

```latex
\begin{assumption}[Closed Measure-Preserving Horizon Pair]
The complementary horizons \(H_1,H_2\) form a closed observer-visible exchange
pair, and the horizon-crossing operation
\(\mathcal{H}_{1,2}\) of Def.~\ref{definition:bk1_horizon_crossing_operation}
preserves the induced symbolic measure on transported density.
\end{assumption}
```

### remark:scholium_symbolicum.tex:2632 (`remark:scholium_symbolicum.tex:2632`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2632`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

This provides a bridge between entropy gradients in physics and coherence gradients in meaning — the same formal structure, rendered at different resolution levels.

**Verbatim LaTeX Body**

```latex
\begin{remark}
This provides a bridge between entropy gradients in physics and coherence gradients in meaning — the same formal structure, rendered at different resolution levels.
\end{remark}
```

### Fields Predicted by the Framework (`subsec:bk1_fields_predicted_by_the_framework`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2635`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Unified Field Classification (`theorem:bk1_unified_field_classification`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2638`

- Proof status: `proven`
- Depends on: `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF))
- Cites: `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF))
- Cited by: none
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-097`
- Witnesses: `SRMF.closure_iff_no_work`, `SRMF.turn_closes_iff`
- Countermodels: none
- Conditions: the circle part of a revolution is the identity by construction; injections are data; no claim about this file or any system proving its own consistency; the helix is FOR approaching the equilibrium circle, not a telos; non-closure is not idolized
- Formal boundary: All emergent fields as SRMF instances under boundary conditions: the SRMF/Godel-safe-cycle kernel; the classification-by-symmetry stays interpretive.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

All emergent symbolic fields arise as particular instantiations of the SRMF (see definition:bk1_self_regulating_mapping_function_srmf) under different boundary conditions and symmetry constraints. Each emergence event (see definition:bk1_emergence_event) corresponds to a new field configuration in symbolic space.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Unified Field Classification]
\label{theorem:bk1_unified_field_classification}
All emergent symbolic fields arise as particular instantiations of the SRMF (see \ref{definition:bk1_self_regulating_mapping_function_srmf}) under different boundary conditions and symmetry constraints. Each emergence event (see \ref{definition:bk1_emergence_event}) corresponds to a new field configuration in symbolic space.
\end{theorem}
```

### Fields as SRMF Boundary-Symmetry Sectors (`proof:bk1_unified_field_classification`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2642`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF))
- Cites: `definition:bk1_emergence_event` (Emergence Event); `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF))
- Cited by: none
- Macros used: none

**Statement / Body**

Within this classification, an emergent symbolic field is individuated by the
boundary conditions and symmetry constraints under which the SRMF acts.

By Def. definition:bk1_self_regulating_mapping_function_srmf, the SRMF is
a reflexive operator on symbolic density that detects contradiction and applies
reflection to restore or reconfigure coherence. By
Def. definition:bk1_emergence_event, an emergence event is precisely an
observer-visible transition in symbolic structure. Under SRMF Field
Individuation, changing the boundary conditions or symmetry constraints changes
the sector in which the same reflexive operator acts; each such sector therefore
determines a distinct field configuration. Conversely, any emergent symbolic
field in this classification is an SRMF-governed coherence sector, so it is an
instantiation of the SRMF under its defining boundary and symmetry data. Thus
emergence events correspond to new field configurations in symbolic space.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Fields as SRMF Boundary-Symmetry Sectors]
\label{proof:bk1_unified_field_classification}
\leavevmode

\begin{assumption}[SRMF Field Individuation]
Within this classification, an emergent symbolic field is individuated by the
boundary conditions and symmetry constraints under which the SRMF acts.
\end{assumption}

By Def.~\ref{definition:bk1_self_regulating_mapping_function_srmf}, the SRMF is
a reflexive operator on symbolic density that detects contradiction and applies
reflection to restore or reconfigure coherence. By
Def.~\ref{definition:bk1_emergence_event}, an emergence event is precisely an
observer-visible transition in symbolic structure. Under SRMF Field
Individuation, changing the boundary conditions or symmetry constraints changes
the sector in which the same reflexive operator acts; each such sector therefore
determines a distinct field configuration. Conversely, any emergent symbolic
field in this classification is an SRMF-governed coherence sector, so it is an
instantiation of the SRMF under its defining boundary and symmetry data. Thus
emergence events correspond to new field configurations in symbolic space.
\end{proof}
```

### SRMF Field Individuation (`assumption:scholium_symbolicum.tex:2646`)

Role: `assumption` | Type: `assumption` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2646`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Within this classification, an emergent symbolic field is individuated by the
boundary conditions and symmetry constraints under which the SRMF acts.

**Verbatim LaTeX Body**

```latex
\begin{assumption}[SRMF Field Individuation]
Within this classification, an emergent symbolic field is individuated by the
boundary conditions and symmetry constraints under which the SRMF acts.
\end{assumption}
```

### Closing Remark on Unified Field (`subsec:bk1_closing_remark_on_unified_field`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2684`

- Proof status: `not_applicable`
- Depends on: none
- Cites: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Manifold Emergence Axioms (`sec:bk1_manifold_emergence_axioms`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2699`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Problem of Symbolic Smoothness (`definition:bk1_problem_of_symbolic_smoothness`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2702`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `scholium:bk1_resolution_of_continuum_disjunction` (On the Resolution of the Continuum Disjunction)
- Macros used: none

**Statement / Body**

The problem of symbolic smoothness asks how a smooth geometric manifold $M$—supporting differential structure and calculus—can arise from symbolic systems composed of discrete structural stages $P_lambda$ (see definition:bk1_pre_geometric_operators_and_stages), evolving via drift and reflection, and perceived by bounded observers $O$ (see definition:bk1_bounded_observer) within a symbolic manifold (see definition:bk1_symbolic_manifold).

It is the central symbolic-geometric problem unifying analysis, computation, and cognition, and it is resolved, within this framework, by Axiom axiom:bk1_symbolic_smoothness.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Problem of Symbolic Smoothness]
\label{definition:bk1_problem_of_symbolic_smoothness}
The problem of symbolic smoothness asks how a smooth geometric manifold $M$—supporting differential structure and calculus—can arise from symbolic systems composed of discrete structural stages $P_\lambda$ (see \ref{definition:bk1_pre_geometric_operators_and_stages}), evolving via drift and reflection, and perceived by bounded observers $\mathcal{O}$ (see \ref{definition:bk1_bounded_observer}) within a symbolic manifold (see \ref{definition:bk1_symbolic_manifold}).

It is the central symbolic-geometric problem unifying analysis, computation, and cognition, and it is resolved, within this framework, by Axiom~\ref{axiom:bk1_symbolic_smoothness}.
\end{definition}
```

### On the Resolution of the Continuum Disjunction (`scholium:bk1_resolution_of_continuum_disjunction`)

Role: `scholium` | Type: `scholium` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2709`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_dual_horizon_postulate` (Dual Horizon Postulate); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_drift_field` (Drift Field); `definition:bk1_problem_of_symbolic_smoothness` (Problem of Symbolic Smoothness); `definition:bk1_reflection_operator` (Reflection Operator)
- Cites: `axiom:bk1_dual_horizon_postulate` (Dual Horizon Postulate); `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_drift_field` (Drift Field); `definition:bk1_problem_of_symbolic_smoothness` (Problem of Symbolic Smoothness); `definition:bk1_reflection_operator` (Reflection Operator)
- Cited by: `corollary:appB_resolution_of_smoothness` (Resolution of Symbolic Smoothness); `proof:appB_resolution_of_smoothness`; `remark:appB_executable_resolution_smoothness` (Executable Resolution of Smoothness); `sec:appB_symbolic_smoothness_resolution` (Symbolic Smoothness Resolution: Completeness of the Observer Metric and Smooth Emergence of the Symbolic Manifold)
- Macros used: none

**Statement / Body**

It has long been held in the mathematical sciences that the calculus of smooth change — as employed in the physics of fields and flows — demands as its substrate a continuous manifold of space and time.
Yet computation, cognition, and symbolic systems do not arise from a smooth continuum. They are recursive, discrete, and symbolically bounded. No manifold precedes their construction; no calculus grounds their becoming.
This disjunction — between the smoothness assumed in classical analysis and the discreteness observed in symbolic evolution — is here resolved.
We posit that smoothness is not an ontological given, but an epistemic artifact, arising from recursive symbolic differentiation under bounded observer resolution (cf. Def. definition:bk1_problem_of_symbolic_smoothness, Def. definition:bk1_bounded_observer, Def. definition:bk1_drift_field, Def. definition:bk1_reflection_operator). The symbolic observer, through iterative acts of drift and reflection, produces increasingly stable structural layers $P_lambda$. When symbolic fluctuations fall below the resolution threshold $epsilon_{O}$ of the observer's internal difference operators $delta^n_{O}$, a manifold structure $M$ emerges — not as a primitive substrate, but as a convergence effect under dual-horizon constraint (Axiom axiom:bk1_dual_horizon_postulate).
This is the essence of what we term the Problem of Symbolic Smoothness.
It is resolved not by constructing the manifold from below, but by demonstrating its inevitable emergence under dual horizon dynamics, constrained by epistemic bounds.
Let this resolution stand as the symbolic counterpart to Newton's founding of the calculus: not a geometry of bodies, but a geometry of symbols, drift, and reflective form.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[On the Resolution of the Continuum Disjunction]
\label{scholium:bk1_resolution_of_continuum_disjunction}
It has long been held in the mathematical sciences that the calculus of smooth change — as employed in the physics of fields and flows — demands as its substrate a continuous manifold of space and time.
Yet computation, cognition, and symbolic systems do not arise from a smooth continuum. They are recursive, discrete, and symbolically bounded. No manifold precedes their construction; no calculus grounds their becoming.
This disjunction — between the smoothness assumed in classical analysis and the discreteness observed in symbolic evolution — is here resolved.
We posit that smoothness is not an ontological given, but an \textit{epistemic artifact}, arising from recursive symbolic differentiation under bounded observer resolution (cf.~Def.~\ref{definition:bk1_problem_of_symbolic_smoothness}, Def.~\ref{definition:bk1_bounded_observer}, Def.~\ref{definition:bk1_drift_field}, Def.~\ref{definition:bk1_reflection_operator}). The symbolic observer, through iterative acts of drift and reflection, produces increasingly stable structural layers $P_\lambda$. When symbolic fluctuations fall below the resolution threshold $\epsilon_{\mathcal{O}}$ of the observer's internal difference operators $\delta^n_{\mathcal{O}}$, a manifold structure $M$ emerges — not as a primitive substrate, but as a convergence effect under dual-horizon constraint (Axiom~\ref{axiom:bk1_dual_horizon_postulate}).
This is the essence of what we term the \textbf{Problem of Symbolic Smoothness}.
It is resolved not by constructing the manifold from below, but by demonstrating its inevitable emergence under dual horizon dynamics, constrained by epistemic bounds.
Let this resolution stand as the symbolic counterpart to Newton's founding of the calculus: not a geometry of bodies, but a geometry of symbols, drift, and reflective form.
\end{scholium}
```

### Symbolic Smoothness (`axiom:bk1_symbolic_smoothness`)

Role: `axiom` | Type: `axiom` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2719`

- Proof status: `definitional`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_reflection_operator` (Reflection Operator)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_reflection_operator` (Reflection Operator)
- Cited by: `axiom:bk1_smooth_convergence` (Smooth Convergence); `definition:bk1_problem_of_symbolic_smoothness` (Problem of Symbolic Smoothness); `proof:bk1_atlas_final_topology_phase_space` (Atlas Construction on Final Topology of Symbolic Phase Space); `proof:bk1_sketch_construction_proto_metric` (Construction of Proto-Metric on Symbolic Layers); `proof:bk1_sketch_drift_limit_vector_field` (Limit Vector Field from Local Drift Coherence); `proof:bk1_sketch_symbolic_connectivity` (Symbolic Connectivity via Hopf--Rinow); `subsec:bk1_closing_remark_on_unified_field` (Closing Remark on Unified Field); `theorem:bk1_manifold_emergence` (Manifold Emergence)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-039`
- Witnesses: `ScholiumD.DifferentiationThreshold.eventually_below_threshold`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: Convergent-Limit and Epistemic-Emergence clauses only, as a real-sequence threshold law; observable differentiation, chart compatibility, and the structural limit M itself are not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $S$ be a symbolic system evolving through iterative drift operators $D_lambda$ (Def. definition:bk1_drift_field) and reflection operators $R_lambda$ (Def. definition:bk1_reflection_operator) over stages $lambda in Lambda subset mathbb{N}$ (Def. definition:bk1_pre_geometric_operators_and_stages), with symbolic structure $P_lambda$ at each stage. A smooth geometric structure $M$ is said to emerge from $S$ if and only if, for a bounded observer $O$ embedded within $S$, the following conditions obtain:


- Observable Differentiation: $O$ possesses an internal differentiation capacity that generates a sequence of well-defined difference operators ${delta^n_{O}}_{n in mathbb{N}}$ applicable to symbolic states, with $delta^0_{O}P_lambda = P_lambda$ and $delta^{n+1}_{O}P_lambda = delta^1_{O}(delta^n_{O}P_lambda)$.

- Resolution Threshold: There exists a positive functional $epsilon_{O}: P rightarrow mathbb{R}^+$ defining the minimal symbolic distinction discernible by $O$, where $P$ is the space of all possible symbolic structures.

- Convergent Limit: For some $lambda_0 in Lambda$, there exists a structural limit $M = lim_{lambda to lambda_0} P_lambda$ under a suitable operator norm $\|cdot\|_{S}$ such that:

 lim_{lambda to lambda_0} \|P_{lambda+1} - P_lambda\|_{S} = 0


- Chart Compatibility: For any point $p in M$, there exists a neighborhood $U_p subset M$ and a bijection $varphi_p: U_p rightarrow mathbb{R}^d$ (for some $d in mathbb{N}$) such that the charts $(U_p, varphi_p)$ form an atlas on $M$, and the symbolic gradients $nabla D_lambda$ induce consistent directional derivatives on these charts.

- Epistemic Emergence: For all $lambda$ sufficiently close to $lambda_0$ and all $n leq N_{O}$ (where $N_{O}$ is the maximum order of differentiation available to $O$):

 \|delta^n_{O}(P_{lambda+1} - P_lambda)\|_{S} < epsilon_{O}(P_lambda)


Thus, $M$ appears smooth to $O$ precisely because symbolic fluctuations across successive stages fall below $O$'s resolution threshold of differentiation, rendering smoothness an emergent epistemic property conditioned on bounded symbolic discernment rather than an ontological characteristic of $S$ itself.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Symbolic Smoothness]
\label{axiom:bk1_symbolic_smoothness}
Let $\mathcal{S}$ be a symbolic system evolving through iterative drift operators $D_\lambda$ (Def.~\ref{definition:bk1_drift_field}) and reflection operators $R_\lambda$ (Def.~\ref{definition:bk1_reflection_operator}) over stages $\lambda \in \Lambda \subset \mathbb{N}$ (Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}), with symbolic structure $P_\lambda$ at each stage. A smooth geometric structure $M$ is said to emerge from $\mathcal{S}$ if and only if, for a bounded observer $\mathcal{O}$ embedded within $\mathcal{S}$, the following conditions obtain:
\begin{enumerate}
    \item \textbf{Observable Differentiation:} $\mathcal{O}$ possesses an internal differentiation capacity that generates a sequence of well-defined difference operators $\{\delta^n_{\mathcal{O}}\}_{n \in \mathbb{N}}$ applicable to symbolic states, with $\delta^0_{\mathcal{O}}P_\lambda = P_\lambda$ and $\delta^{n+1}_{\mathcal{O}}P_\lambda = \delta^1_{\mathcal{O}}(\delta^n_{\mathcal{O}}P_\lambda)$.
    \item \textbf{Resolution Threshold:} There exists a positive functional $\epsilon_{\mathcal{O}}: \mathcal{P} \rightarrow \mathbb{R}^+$ defining the minimal symbolic distinction discernible by $\mathcal{O}$, where $\mathcal{P}$ is the space of all possible symbolic structures.
    \item \textbf{Convergent Limit:} For some $\lambda_0 \in \Lambda$, there exists a structural limit $M = \lim_{\lambda \to \lambda_0} P_\lambda$ under a suitable operator norm $\|\cdot\|_{\mathcal{S}}$ such that:
        \begin{align}
        \lim_{\lambda \to \lambda_0} \|P_{\lambda+1} - P_\lambda\|_{\mathcal{S}} = 0
        \end{align}
    \item \textbf{Chart Compatibility:} For any point $p \in M$, there exists a neighborhood $U_p \subset M$ and a bijection $\varphi_p: U_p \rightarrow \mathbb{R}^d$ (for some $d \in \mathbb{N}$) such that the charts $(U_p, \varphi_p)$ form an atlas on $M$, and the symbolic gradients $\nabla D_\lambda$ induce consistent directional derivatives on these charts.
    \item \textbf{Epistemic Emergence:} For all $\lambda$ sufficiently close to $\lambda_0$ and all $n \leq N_{\mathcal{O}}$ (where $N_{\mathcal{O}}$ is the maximum order of differentiation available to $\mathcal{O}$):
        \begin{align}
        \|\delta^n_{\mathcal{O}}(P_{\lambda+1} - P_\lambda)\|_{\mathcal{S}} < \epsilon_{\mathcal{O}}(P_\lambda)
        \end{align}
\end{enumerate}
Thus, $M$ appears smooth to $\mathcal{O}$ precisely because symbolic fluctuations across successive stages fall below $\mathcal{O}$'s resolution threshold of differentiation, rendering smoothness an emergent epistemic property conditioned on bounded symbolic discernment rather than an ontological characteristic of $\mathcal{S}$ itself.
\end{axiom}
```

### Local Chartability (`axiom:bk1_local_charitability`)

Role: `axiom` | Type: `axiom` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2737`

- Proof status: `definitional`
- Depends on: `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cites: `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cited by: `axiom:bk1_smooth_convergence` (Smooth Convergence); `proof:bk1_sketch_coherence_drift_reflection` (Coherence of Proto-Drift Fields via Chart Convergence); `remark:bk4_fuzzy`
- Macros used: `\R`

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-058`
- Witnesses: `Atlas.manifold_emergence`
- Countermodels: none
- Conditions: pair-covering as the topological-regularity stand-in (Hausdorff/second-countable/paracompact/connected unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Chartability enters as the ResolutionTower structure; homeomorphism content open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Building on the stage tower $(P_lambda, f_{lambdamu})$ of Def. definition:bk1_pre_geometric_operators_and_stages and the proto-symbolic space $P$ of Def. definition:bk1_proto_symbolic_space, there exists an ordinal $lambda_0 < Omega$ such that for all $lambda geq lambda_0$ and for each $x_lambda in P_lambda$, there exists a neighborhood $U_lambda subseteq P_lambda$ of $x_lambda$ and a homeomorphism $varphi_lambda: U_lambda to V_lambda$ where $V_lambda$ is an open subset of $R^n$ for some fixed dimension $n$.
Furthermore, these charts satisfy the coherence condition: for any $lambda < mu$ with $lambda ge lambda_0$, $x_lambda in P_lambda$ and $x_mu = f_{lambdamu}(x_lambda) in P_mu$, there exist charts $(U_lambda, varphi_lambda)$ around $x_lambda$ and $(U_mu, varphi_mu)$ around $x_mu$ such that $f_{lambdamu}(U_lambda) subseteq U_mu$ and the map $varphi_mu circ f_{lambdamu} circ varphi_lambda^{-1}$ is a homeomorphism between the corresponding open sets in $R^n$.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Local Chartability]
\label{axiom:bk1_local_charitability}
Building on the stage tower $(P_\lambda, f_{\lambda\mu})$ of Def.~\ref{definition:bk1_pre_geometric_operators_and_stages} and the proto-symbolic space $P$ of Def.~\ref{definition:bk1_proto_symbolic_space}, there exists an ordinal $\lambda_0 < \Omega$ such that for all $\lambda \geq \lambda_0$ and for each $x_\lambda \in P_\lambda$, there exists a neighborhood $U_\lambda \subseteq P_\lambda$ of $x_\lambda$ and a homeomorphism $\varphi_\lambda: U_\lambda \to V_\lambda$ where $V_\lambda$ is an open subset of $\R^n$ for some fixed dimension $n$.
Furthermore, these charts satisfy the coherence condition: for any $\lambda < \mu$ with $\lambda \ge \lambda_0$, $x_\lambda \in P_\lambda$ and $x_\mu = f_{\lambda\mu}(x_\lambda) \in P_\mu$, there exist charts $(U_\lambda, \varphi_\lambda)$ around $x_\lambda$ and $(U_\mu, \varphi_\mu)$ around $x_\mu$ such that $f_{\lambda\mu}(U_\lambda) \subseteq U_\mu$ and the map $\varphi_\mu \circ f_{\lambda\mu} \circ \varphi_\lambda^{-1}$ is a homeomorphism between the corresponding open sets in $\R^n$.
\end{axiom}
```

### remark:scholium_symbolicum.tex:2742 (`remark:scholium_symbolicum.tex:2742`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2742`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

This axiom posits that, beyond a certain stage $lambda_0$, the emergent structures become sufficiently regular to admit local Euclidean descriptions. This reflects the observer's capacity to impose/recognize consistent local structure.

**Verbatim LaTeX Body**

```latex
\begin{remark}
This axiom posits that, beyond a certain stage $\lambda_0$, the emergent structures become sufficiently regular to admit local Euclidean descriptions. This reflects the observer's capacity to impose/recognize consistent local structure.
\end{remark}
```

### Smooth Convergence (`axiom:bk1_smooth_convergence`)

Role: `axiom` | Type: `axiom` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2745`

- Proof status: `definitional`
- Depends on: `axiom:bk1_local_charitability` (Local Chartability); `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cites: `axiom:bk1_local_charitability` (Local Chartability); `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cited by: `proof:bk1_sketch_coherence_drift_reflection` (Coherence of Proto-Drift Fields via Chart Convergence); `proof:bk1_sketch_limit_stabilization_colimit` (Limit of Stabilization Operators via Colimit)
- Macros used: `\R`, `\norm`

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-059`
- Witnesses: `Atlas.tower_glues`
- Countermodels: none
- Conditions: pair-covering as the topological-regularity stand-in (Hausdorff/second-countable/paracompact/connected unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Pointwise convergence + vanishing defect; C-infinity topology open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Extending Axiom axiom:bk1_symbolic_smoothness and Axiom axiom:bk1_local_charitability on the proto-symbolic space of Def. definition:bk1_proto_symbolic_space, we require:
For any two points $p, q in P$ represented by sequences $(x_lambda^p)_{lambda ge lambda_p}$ and $(x_lambda^q)_{lambda ge lambda_q}$, and corresponding charts $(U_lambda^p, varphi_lambda^p)$, $(U_lambda^q, varphi_lambda^q)$ for $lambda ge max(lambda_0, lambda_p, lambda_q)$, the transition maps $varphi_lambda^q circ (varphi_lambda^p)^{-1}$ converge in the $C^infty$-topology as $lambda to Omega$ on overlapping domains.
Specifically, for any $k ge 0$ and any compact set $K subset varphi_lambda^p(U_lambda^p cap U_lambda^q)$ (for sufficiently large $lambda$), and any $epsilon > 0$, there exists $lambda_1 < Omega$ such that for all $lambda', lambda'' ge lambda_1$:
\[
norm{ varphi_{lambda'}^q circ (varphi_{lambda'}^p)^{-1} - varphi_{lambda''}^q circ (varphi_{lambda''}^p)^{-1} }_{C^k(K)} < epsilon
\]
(where the norm is taken on the relevant image set in $R^n$).

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Smooth Convergence]
\label{axiom:bk1_smooth_convergence}
Extending Axiom~\ref{axiom:bk1_symbolic_smoothness} and Axiom~\ref{axiom:bk1_local_charitability} on the proto-symbolic space of Def.~\ref{definition:bk1_proto_symbolic_space}, we require:
For any two points $p, q \in P$ represented by sequences $(x_\lambda^p)_{\lambda \ge \lambda_p}$ and $(x_\lambda^q)_{\lambda \ge \lambda_q}$, and corresponding charts $(U_\lambda^p, \varphi_\lambda^p)$, $(U_\lambda^q, \varphi_\lambda^q)$ for $\lambda \ge \max(\lambda_0, \lambda_p, \lambda_q)$, the transition maps $\varphi_\lambda^q \circ (\varphi_\lambda^p)^{-1}$ converge in the $C^\infty$-topology as $\lambda \to \Omega$ on overlapping domains.
Specifically, for any $k \ge 0$ and any compact set $K \subset \varphi_\lambda^p(U_\lambda^p \cap U_\lambda^q)$ (for sufficiently large $\lambda$), and any $\epsilon > 0$, there exists $\lambda_1 < \Omega$ such that for all $\lambda', \lambda'' \ge \lambda_1$:
\[
\norm{ \varphi_{\lambda'}^q \circ (\varphi_{\lambda'}^p)^{-1} - \varphi_{\lambda''}^q \circ (\varphi_{\lambda''}^p)^{-1} }_{C^k(K)} < \epsilon
\]
(where the norm is taken on the relevant image set in $\R^n$).
\end{axiom}
```

### remark:scholium_symbolicum.tex:2755 (`remark:scholium_symbolicum.tex:2755`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2755`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

This axiom ensures that the local Euclidean patches stitch together smoothly in the limit, giving rise to a globally defined smooth structure. The convergence is required to be $C^infty$ to yield a smooth manifold.

**Verbatim LaTeX Body**

```latex
\begin{remark}
This axiom ensures that the local Euclidean patches stitch together smoothly in the limit, giving rise to a globally defined smooth structure. The convergence is required to be $C^\infty$ to yield a smooth manifold.
\end{remark}
```

### Topological Regularity (`axiom:bk1_topological_regularity`)

Role: `axiom` | Type: `axiom` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2758`

- Proof status: `definitional`
- Depends on: `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cites: `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cited by: `proof:appB_smoothness_emergence`; `proof:bk1_atlas_final_topology_phase_space` (Atlas Construction on Final Topology of Symbolic Phase Space); `proof:bk1_sketch_symbolic_connectivity` (Symbolic Connectivity via Hopf--Rinow); `proof:bk2_probability_structure_on_manifold` (Symbolic Probability Structure on Emergent Manifold); `theorem:appB_smoothness_emergence` (Emergent Smoothness from Symbolic Discreteness); `theorem:bk1_manifold_emergence` (Manifold Emergence)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-060`
- Witnesses: `Atlas.manifold_emergence`
- Countermodels: none
- Conditions: pair-covering as the topological-regularity stand-in (Hausdorff/second-countable/paracompact/connected unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Pair-covering stand-in; Hausdorff/paracompactness unmodeled, named.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The colimit topology on the proto-symbolic space $P$ (Def. definition:bk1_proto_symbolic_space) constructed from the stage tower of Def. definition:bk1_pre_geometric_operators_and_stages is postulated to be:


- Hausdorff.

- Second-countable.

- Paracompact.

- Connected.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Topological Regularity]
\label{axiom:bk1_topological_regularity}
The colimit topology on the proto-symbolic space $P$ (Def.~\ref{definition:bk1_proto_symbolic_space}) constructed from the stage tower of Def.~\ref{definition:bk1_pre_geometric_operators_and_stages} is postulated to be:
\begin{enumerate}
    \item Hausdorff.
    \item Second-countable.
    \item Paracompact.
    \item Connected.
\end{enumerate}
\end{axiom}
```

### remark:scholium_symbolicum.tex:2768 (`remark:scholium_symbolicum.tex:2768`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2768`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

These topological properties are not automatically guaranteed by the colimit construction, especially for large $Omega$. Within the framework, they are considered necessary postulates reflecting the emergence of a coherent, well-behaved space of symbolic possibilities, suitable for hosting stable structures and dynamics. They represent conditions under which a bounded observer can form a consistent global picture.

**Verbatim LaTeX Body**

```latex
\begin{remark}
These topological properties are not automatically guaranteed by the colimit construction, especially for large $\Omega$. Within the framework, they are considered necessary postulates reflecting the emergence of a coherent, well-behaved space of symbolic possibilities, suitable for hosting stable structures and dynamics. They represent conditions under which a bounded observer can form a consistent global picture.
\end{remark}
```

### Manifold Emergence (`theorem:bk1_manifold_emergence`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2771`

- Proof status: `proven`
- Depends on: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `axiom:bk1_topological_regularity` (Topological Regularity); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cites: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `axiom:bk1_topological_regularity` (Topological Regularity); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cited by: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `proof:bk1_sketch_symbolic_connectivity` (Symbolic Connectivity via Hopf--Rinow); `proof:bk2_probability_structure_on_manifold` (Symbolic Probability Structure on Emergent Manifold); `sec:appD_preamble_nature_of_appendix` (D.0 Preamble); `sec:bk1_summary_and_implications` (Summary and Implications)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-061`
- Witnesses: `Atlas.fracture_stops_emergence`, `Atlas.manifold_emergence`, `Atlas.tower_glues`
- Countermodels: none
- Conditions: pair-covering as the topological-regularity stand-in (Hausdorff/second-countable/paracompact/connected unmodeled, named); smoothness-as-C-infinity stays open
- Formal boundary: Existence + uniqueness of the emergent geometry from vanishing defects, with the persisting-defect converse; smoothness-as-C-infinity open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Under Axioms axiom:bk1_symbolic_smoothness and axiom:bk1_topological_regularity, the proto-symbolic space $P$ (see definition:bk1_proto_symbolic_space) admits a unique structure as a smooth, connected, paracompact manifold $M$ of dimension $n$.

The construction proceeds by defining an atlas on $P$. For any $p in P$, represented by $[(x_lambda)]$, Axiom axiom:bk1_symbolic_smoothness provides charts $(U_lambda, varphi_lambda)$ on each structural stage $P_lambda$ (see definition:bk1_pre_geometric_operators_and_stages). The canonical injection $i_lambda: P_lambda to P$ is continuous by the final topology (see definition:appB_symbolic_chart).

We define a chart $(U_p, varphi_p)$ around $p$ in $P$ by taking $U_p$ to be a neighborhood corresponding to $i_lambda(U_lambda)$ and $varphi_p$ induced from $varphi_lambda$. Note: $i_lambda$ is not necessarily open, but the final topology ensures that any set whose preimages $i_lambda^{-1}(V)$ are open in each $P_lambda$ is open in $P$.

Axiom axiom:bk1_symbolic_smoothness guarantees that the transition maps between any two such charts $(U_p, varphi_p)$ and $(U_q, varphi_q)$ are $C^infty$ on their overlap $U_p cap U_q$. The collection $A = {(U_p, varphi_p) : p in P}$ thus forms a $C^infty$ atlas for $P$.

Axiom axiom:bk1_topological_regularity ensures that $P$ equipped with this atlas is a Hausdorff, second-countable, paracompact, connected topological space. Together with the $C^infty$ atlas $A$, these properties characterize $P$ as a smooth manifold $M$ of dimension $n$. The uniqueness of the smooth structure (up to diffeomorphism) follows from the $C^infty$ convergence in Axiom axiom:bk1_symbolic_smoothness.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Manifold Emergence]
\label{theorem:bk1_manifold_emergence}
Under Axioms~\ref{axiom:bk1_symbolic_smoothness} and \ref{axiom:bk1_topological_regularity}, the proto-symbolic space $P$ (see \ref{definition:bk1_proto_symbolic_space}) admits a unique structure as a smooth, connected, paracompact manifold $M$ of dimension $n$.

\begin{proof}[Atlas Construction on Final Topology of Symbolic Phase Space]
\label{proof:bk1_atlas_final_topology_phase_space}
\leavevmode

The construction proceeds by defining an atlas on $P$. For any $p \in P$, represented by $[(x_\lambda)]$, Axiom~\ref{axiom:bk1_symbolic_smoothness} provides charts $(U_\lambda, \varphi_\lambda)$ on each structural stage $P_\lambda$ (see \ref{definition:bk1_pre_geometric_operators_and_stages}). The canonical injection $i_\lambda: P_\lambda \to P$ is continuous by the final topology (see \ref{definition:appB_symbolic_chart}).

We define a chart $(\mathcal{U}_p, \varphi_p)$ around $p$ in $P$ by taking $\mathcal{U}_p$ to be a neighborhood corresponding to $i_\lambda(U_\lambda)$ and $\varphi_p$ induced from $\varphi_\lambda$. Note: $i_\lambda$ is not necessarily open, but the final topology ensures that any set whose preimages $i_\lambda^{-1}(V)$ are open in each $P_\lambda$ is open in $P$.

Axiom~\ref{axiom:bk1_symbolic_smoothness} guarantees that the transition maps between any two such charts $(\mathcal{U}_p, \varphi_p)$ and $(\mathcal{U}_q, \varphi_q)$ are $C^\infty$ on their overlap $\mathcal{U}_p \cap \mathcal{U}_q$. The collection $\mathcal{A} = \{(\mathcal{U}_p, \varphi_p) : p \in P\}$ thus forms a $C^\infty$ atlas for $P$.

Axiom~\ref{axiom:bk1_topological_regularity} ensures that $P$ equipped with this atlas is a Hausdorff, second-countable, paracompact, connected topological space. Together with the $C^\infty$ atlas $\mathcal{A}$, these properties characterize $P$ as a smooth manifold $M$ of dimension $n$. The uniqueness of the smooth structure (up to diffeomorphism) follows from the $C^\infty$ convergence in Axiom~\ref{axiom:bk1_symbolic_smoothness}.
\end{proof}
\end{theorem}
```

### Atlas Construction on Final Topology of Symbolic Phase Space (`proof:bk1_atlas_final_topology_phase_space`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2775`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `axiom:bk1_topological_regularity` (Topological Regularity); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `axiom:bk1_topological_regularity` (Topological Regularity); `definition:appB_symbolic_chart` (Symbolic Chart System); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cited by: none
- Macros used: none

**Statement / Body**

The construction proceeds by defining an atlas on $P$. For any $p in P$, represented by $[(x_lambda)]$, Axiom axiom:bk1_symbolic_smoothness provides charts $(U_lambda, varphi_lambda)$ on each structural stage $P_lambda$ (see definition:bk1_pre_geometric_operators_and_stages). The canonical injection $i_lambda: P_lambda to P$ is continuous by the final topology (see definition:appB_symbolic_chart).

We define a chart $(U_p, varphi_p)$ around $p$ in $P$ by taking $U_p$ to be a neighborhood corresponding to $i_lambda(U_lambda)$ and $varphi_p$ induced from $varphi_lambda$. Note: $i_lambda$ is not necessarily open, but the final topology ensures that any set whose preimages $i_lambda^{-1}(V)$ are open in each $P_lambda$ is open in $P$.

Axiom axiom:bk1_symbolic_smoothness guarantees that the transition maps between any two such charts $(U_p, varphi_p)$ and $(U_q, varphi_q)$ are $C^infty$ on their overlap $U_p cap U_q$. The collection $A = {(U_p, varphi_p) : p in P}$ thus forms a $C^infty$ atlas for $P$.

Axiom axiom:bk1_topological_regularity ensures that $P$ equipped with this atlas is a Hausdorff, second-countable, paracompact, connected topological space. Together with the $C^infty$ atlas $A$, these properties characterize $P$ as a smooth manifold $M$ of dimension $n$. The uniqueness of the smooth structure (up to diffeomorphism) follows from the $C^infty$ convergence in Axiom axiom:bk1_symbolic_smoothness.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Atlas Construction on Final Topology of Symbolic Phase Space]
\label{proof:bk1_atlas_final_topology_phase_space}
\leavevmode

The construction proceeds by defining an atlas on $P$. For any $p \in P$, represented by $[(x_\lambda)]$, Axiom~\ref{axiom:bk1_symbolic_smoothness} provides charts $(U_\lambda, \varphi_\lambda)$ on each structural stage $P_\lambda$ (see \ref{definition:bk1_pre_geometric_operators_and_stages}). The canonical injection $i_\lambda: P_\lambda \to P$ is continuous by the final topology (see \ref{definition:appB_symbolic_chart}).

We define a chart $(\mathcal{U}_p, \varphi_p)$ around $p$ in $P$ by taking $\mathcal{U}_p$ to be a neighborhood corresponding to $i_\lambda(U_\lambda)$ and $\varphi_p$ induced from $\varphi_\lambda$. Note: $i_\lambda$ is not necessarily open, but the final topology ensures that any set whose preimages $i_\lambda^{-1}(V)$ are open in each $P_\lambda$ is open in $P$.

Axiom~\ref{axiom:bk1_symbolic_smoothness} guarantees that the transition maps between any two such charts $(\mathcal{U}_p, \varphi_p)$ and $(\mathcal{U}_q, \varphi_q)$ are $C^\infty$ on their overlap $\mathcal{U}_p \cap \mathcal{U}_q$. The collection $\mathcal{A} = \{(\mathcal{U}_p, \varphi_p) : p \in P\}$ thus forms a $C^\infty$ atlas for $P$.

Axiom~\ref{axiom:bk1_topological_regularity} ensures that $P$ equipped with this atlas is a Hausdorff, second-countable, paracompact, connected topological space. Together with the $C^\infty$ atlas $\mathcal{A}$, these properties characterize $P$ as a smooth manifold $M$ of dimension $n$. The uniqueness of the smooth structure (up to diffeomorphism) follows from the $C^\infty$ convergence in Axiom~\ref{axiom:bk1_symbolic_smoothness}.
\end{proof}
```

### Emergent Structures (`subsec:bk1_emergent_structures`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2789`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Manifold Existence (`definition:bk1_symbolic_manifold_existence`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2792`

- Proof status: `definitional`
- Depends on: `theorem:bk1_manifold_emergence` (Manifold Emergence)
- Cites: `theorem:bk1_manifold_emergence` (Manifold Emergence)
- Cited by: `definition:bk1_symbol_space` (Symbol Space); `definition:bk1_symbolic_distance` (Symbolic Distance); `definition:bk1_symbolic_flow` (Symbolic Flow); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `definition:bk1_symbolic_information_geometry` (Symbolic Information Geometry); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density); `definition:bk2_symbolic_probability_spa` (Symbolic Probability Space); `lemma:bk1_existence_and_uniqueness_of_flow` (Existence and Uniqueness of Flow); `lemma:bk1_existence_of_metric` (Existence of Metric); `lemma:bk1_well_posedness_of_symbolic_hamiltonian` (Well-posedness of Symbolic Hamiltonian); `proof:bk1_existence_and_uniqueness_of_flow`; `proof:bk1_sketch_fokker_planck_microdynamics`; `proof:bk1_sketch_smoothness_linearization` (Smoothness of Symbolic Hamiltonian); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_symbolic_fluctuation_dissipation_relation` (Symbolic Fluctuation–Dissipation Relation); `theorem:bk1_variational_principle` (Variational Principle)
- Macros used: none

**Statement / Body**

The symbolic manifold $M$ is the unique smooth, connected, paracompact manifold of dimension $n$ established by Theorem theorem:bk1_manifold_emergence.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Manifold Existence]
\label{definition:bk1_symbolic_manifold_existence}
The symbolic manifold $M$ is the unique smooth, connected, paracompact manifold of dimension $n$ established by Theorem~\ref{theorem:bk1_manifold_emergence}.
\end{definition}
```

### Proto-Drift Field $\vec{D}_\lambda$ (`definition:bk1_proto_drift_field`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2797`

- Proof status: `definitional`
- Depends on: `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cited by: `definition:bk1_symbolic_flow` (Symbolic Flow); `definition:bk3_autophagic_drift` (Autophagic Drift); `lemma:bk1_existence_of_metric` (Existence of Metric); `proof:bk1_drift_deviation_bound` (Proto-Drift Induces Directional Deviation Bound); `proof:bk1_observer_kernel_convolution` (Convolutional Identity from Observer Kernel Properties); `proof:bk1_sketch_construction_proto_metric` (Construction of Proto-Metric on Symbolic Layers); `proof:bk1_sketch_effective_proto_drift_field_induction` (Fundamental Operators as Bounded Symbolic Approximations); `proposition:bk1_boundedness_from_drift` (\textbf{Boundedness from Drift}); `proposition:bk1_the_operators_lambda_and_lambda` (Fundamental Operators as Bounded Symbolic Approximations)
- Macros used: none

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-079`
- Witnesses: `ScholiumHzn.drift_field_unique`
- Countermodels: none
- Conditions: manifold integrals, PDE forms, smoothness, ordinal colimits, and curvature signs stay open/interpretive per row notes
- Formal boundary: Stage fields as converging tower data.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

For sufficiently large $lambda < Omega$ (i.e., $lambda ge lambda_0$), we denote by $vec{D}_lambda$ the proto-drift field on $P_lambda$ (see definition:bk1_pre_geometric_operators_and_stages). This represents the effective directional tendency observable at stage $lambda$, emerging from the history of differentiation ($D_nu, nu le lambda$) and stabilization ($R_nu, nu < lambda$).

Framing Note: From a purely formal external perspective, one might seek to explicitly construct $vec{D}_lambda$ (e.g., as an operator on functions on $P_lambda$ or a section of $TP_lambda$) satisfying certain properties. Within the framework, however, $vec{D}_lambda$ is understood as the bounded symbolic representation of the underlying generative drift process, accessible to an observer embedded at stage $lambda$. Its existence and coherence are tied to the emergence axioms.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Proto-Drift Field $\vec{D}_\lambda$]
\label{definition:bk1_proto_drift_field}
For sufficiently large $\lambda < \Omega$ (i.e., $\lambda \ge \lambda_0$), we denote by $\vec{D}_\lambda$ the \textbf{proto-drift field} on $P_\lambda$ (see \ref{definition:bk1_pre_geometric_operators_and_stages}). This represents the effective directional tendency observable at stage $\lambda$, emerging from the history of differentiation ($D_\nu, \nu \le \lambda$) and stabilization ($R_\nu, \nu < \lambda$).

\smallskip
\noindent
\textbf{Framing Note:} From a purely formal external perspective, one might seek to explicitly construct $\vec{D}_\lambda$ (e.g., as an operator on functions on $P_\lambda$ or a section of $TP_\lambda$) satisfying certain properties. Within the framework, however, $\vec{D}_\lambda$ is understood as the bounded symbolic representation of the underlying generative drift process, accessible to an observer embedded at stage $\lambda$. Its existence and coherence are tied to the emergence axioms.
\end{definition}
```

### Coherence of Proto-Drift Fields (`lemma:bk1_coherence_of_proto_drift_fields`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2806`

- Proof status: `proven`
- Depends on: `axiom:bk1_local_charitability` (Local Chartability); `axiom:bk1_smooth_convergence` (Smooth Convergence); `definition:bk1_drift_field` (Drift Field); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cited by: `proof:bk1_sketch_construction_proto_metric` (Construction of Proto-Metric on Symbolic Layers); `proof:bk1_sketch_drift_limit_vector_field` (Limit Vector Field from Local Drift Coherence)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-041`
- Witnesses: `ScholiumD.CommutatorErrorBound.err_tendsto_zero`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: the commutator-error-to-zero step of the proof, as a squeeze theorem for a nonnegative sequence dominated by a vanishing bound; the chart representations and transition maps are not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The proto-drift fields $vec{D}_lambda$ arising from Def. definition:bk1_pre_geometric_operators_and_stages (for $lambda ge lambda_0$) are required to be coherent with the structural evolution maps $f_{lambdamu}$ in the following sense, ensuring they limit to the drift field $D$ of Def. definition:bk1_drift_field:
\[
df_{lambdamu} circ vec{D}_lambda approx vec{D}_mu circ f_{lambdamu}
\]
where $df_{lambdamu}$ is the differential (pushforward) of $f_{lambdamu}$, and the approximation $approx$ becomes equality in the limit $lambda, mu to Omega$. This condition ensures that the perceived drift at stage $lambda$, when evolved to stage $mu$, aligns with the perceived drift at stage $mu$.

Framing Note: This coherence is a necessary condition for the stabilization of drift into a well-defined vector field on the limit manifold $M$. It reflects the emergence of consistent dynamics across stages from the bounded observer's perspective.

Local chart representation.
For $lambda geq lambda_0$, Axiom axiom:bk1_local_charitability provides
charts $(U_lambda, varphi_lambda)$ on $P_lambda$ such that for $lambda < mu$,
the transition map $T_{lambdamu} := varphi_mu circ f_{lambdamu} circ varphi_lambda^{-1}$
is a homeomorphism between open subsets of $mathbb{R}^n$.
In these charts, $vec{D}_lambda$ is represented as a local vector field
$V_lambda$ on $varphi_lambda(U_lambda)$.

Commutation in charts.
The two derivations in the lemma statement correspond to:

df_{lambdamu} circ vec{D}_lambda & longleftrightarrow dT_{lambdamu} cdot V_lambda
 text{(pushforward of $V_lambda$ through $T_{lambdamu}$)}, \\
vec{D}_mu circ f_{lambdamu} & longleftrightarrow V_mu circ T_{lambdamu}
 text{(evaluate $V_mu$ at the image point)}.

Their difference is the commutator error
$\|dT_{lambdamu} cdot V_lambda - V_mu circ T_{lambdamu}\|_{C^0}$.

Convergence to zero.
By Axiom axiom:bk1_smooth_convergence, the transition maps $T_{lambdamu}$
converge in the $C^infty$ topology as $lambda, mu to Omega$: for any
$k geq 0$ and compact $K$, $\|T_{lambdamu} - T_{mu'mu'}\|_{C^k(K)} to 0$.
Since $V_lambda$ and $V_mu$ are locally bounded (Def. definition:bk1_pre_geometric_operators_and_stages),
the commutator error satisfies:
\[
\|dT_{lambdamu} cdot V_lambda - V_mu circ T_{lambdamu}\|_{C^0}
 xrightarrow{lambda,mu to Omega} 0,
\]
establishing $df_{lambdamu} circ vec{D}_lambda approx vec{D}_mu circ f_{lambdamu}$
with equality in the limit, as claimed.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Coherence of Proto-Drift Fields]
\label{lemma:bk1_coherence_of_proto_drift_fields}
The proto-drift fields $\vec{D}_\lambda$ arising from Def.~\ref{definition:bk1_pre_geometric_operators_and_stages} (for $\lambda \ge \lambda_0$) are required to be coherent with the structural evolution maps $f_{\lambda\mu}$ in the following sense, ensuring they limit to the drift field $D$ of Def.~\ref{definition:bk1_drift_field}:
\[
df_{\lambda\mu} \circ \vec{D}_\lambda \approx \vec{D}_\mu \circ f_{\lambda\mu}
\]
where $df_{\lambda\mu}$ is the differential (pushforward) of $f_{\lambda\mu}$, and the approximation $\approx$ becomes equality in the limit $\lambda, \mu \to \Omega$. This condition ensures that the perceived drift at stage $\lambda$, when evolved to stage $\mu$, aligns with the perceived drift at stage $\mu$.

\smallskip
\noindent
\textbf{Framing Note:} This coherence is a necessary condition for the stabilization of drift into a well-defined vector field on the limit manifold $M$. It reflects the emergence of consistent dynamics across stages from the bounded observer's perspective.

\begin{proof}[Coherence of Proto-Drift Fields via Chart Convergence]
\label{proof:bk1_sketch_coherence_drift_reflection}
\leavevmode

\textbf{Local chart representation.}
For $\lambda \geq \lambda_0$, Axiom~\ref{axiom:bk1_local_charitability} provides
charts $(U_\lambda, \varphi_\lambda)$ on $P_\lambda$ such that for $\lambda < \mu$,
the transition map $T_{\lambda\mu} := \varphi_\mu \circ f_{\lambda\mu} \circ \varphi_\lambda^{-1}$
is a homeomorphism between open subsets of $\mathbb{R}^n$.
In these charts, $\vec{D}_\lambda$ is represented as a local vector field
$V_\lambda$ on $\varphi_\lambda(U_\lambda)$.

\textbf{Commutation in charts.}
The two derivations in the lemma statement correspond to:
\begin{align*}
df_{\lambda\mu} \circ \vec{D}_\lambda &\;\longleftrightarrow\; dT_{\lambda\mu} \cdot V_\lambda
\quad\text{(pushforward of $V_\lambda$ through $T_{\lambda\mu}$)}, \\
\vec{D}_\mu \circ f_{\lambda\mu} &\;\longleftrightarrow\; V_\mu \circ T_{\lambda\mu}
\quad\text{(evaluate $V_\mu$ at the image point)}.
\end{align*}
Their difference is the commutator error
$\|dT_{\lambda\mu} \cdot V_\lambda - V_\mu \circ T_{\lambda\mu}\|_{C^0}$.

\textbf{Convergence to zero.}
By Axiom~\ref{axiom:bk1_smooth_convergence}, the transition maps $T_{\lambda\mu}$
converge in the $C^\infty$ topology as $\lambda, \mu \to \Omega$: for any
$k \geq 0$ and compact $K$, $\|T_{\lambda\mu} - T_{\mu'\mu'}\|_{C^k(K)} \to 0$.
Since $V_\lambda$ and $V_\mu$ are locally bounded (Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}),
the commutator error satisfies:
\[
\|dT_{\lambda\mu} \cdot V_\lambda - V_\mu \circ T_{\lambda\mu}\|_{C^0}
\;\xrightarrow{\lambda,\mu \to \Omega}\; 0,
\]
establishing $df_{\lambda\mu} \circ \vec{D}_\lambda \approx \vec{D}_\mu \circ f_{\lambda\mu}$
with equality in the limit, as claimed.
\end{proof}
\end{lemma}
```

### Coherence of Proto-Drift Fields via Chart Convergence (`proof:bk1_sketch_coherence_drift_reflection`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2818`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_local_charitability` (Local Chartability); `axiom:bk1_smooth_convergence` (Smooth Convergence); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cites: `axiom:bk1_local_charitability` (Local Chartability); `axiom:bk1_smooth_convergence` (Smooth Convergence); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages)
- Cited by: none
- Macros used: none

**Statement / Body**

Local chart representation.
For $lambda geq lambda_0$, Axiom axiom:bk1_local_charitability provides
charts $(U_lambda, varphi_lambda)$ on $P_lambda$ such that for $lambda < mu$,
the transition map $T_{lambdamu} := varphi_mu circ f_{lambdamu} circ varphi_lambda^{-1}$
is a homeomorphism between open subsets of $mathbb{R}^n$.
In these charts, $vec{D}_lambda$ is represented as a local vector field
$V_lambda$ on $varphi_lambda(U_lambda)$.

Commutation in charts.
The two derivations in the lemma statement correspond to:

df_{lambdamu} circ vec{D}_lambda & longleftrightarrow dT_{lambdamu} cdot V_lambda
 text{(pushforward of $V_lambda$ through $T_{lambdamu}$)}, \\
vec{D}_mu circ f_{lambdamu} & longleftrightarrow V_mu circ T_{lambdamu}
 text{(evaluate $V_mu$ at the image point)}.

Their difference is the commutator error
$\|dT_{lambdamu} cdot V_lambda - V_mu circ T_{lambdamu}\|_{C^0}$.

Convergence to zero.
By Axiom axiom:bk1_smooth_convergence, the transition maps $T_{lambdamu}$
converge in the $C^infty$ topology as $lambda, mu to Omega$: for any
$k geq 0$ and compact $K$, $\|T_{lambdamu} - T_{mu'mu'}\|_{C^k(K)} to 0$.
Since $V_lambda$ and $V_mu$ are locally bounded (Def. definition:bk1_pre_geometric_operators_and_stages),
the commutator error satisfies:
\[
\|dT_{lambdamu} cdot V_lambda - V_mu circ T_{lambdamu}\|_{C^0}
 xrightarrow{lambda,mu to Omega} 0,
\]
establishing $df_{lambdamu} circ vec{D}_lambda approx vec{D}_mu circ f_{lambdamu}$
with equality in the limit, as claimed.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Coherence of Proto-Drift Fields via Chart Convergence]
\label{proof:bk1_sketch_coherence_drift_reflection}
\leavevmode

\textbf{Local chart representation.}
For $\lambda \geq \lambda_0$, Axiom~\ref{axiom:bk1_local_charitability} provides
charts $(U_\lambda, \varphi_\lambda)$ on $P_\lambda$ such that for $\lambda < \mu$,
the transition map $T_{\lambda\mu} := \varphi_\mu \circ f_{\lambda\mu} \circ \varphi_\lambda^{-1}$
is a homeomorphism between open subsets of $\mathbb{R}^n$.
In these charts, $\vec{D}_\lambda$ is represented as a local vector field
$V_\lambda$ on $\varphi_\lambda(U_\lambda)$.

\textbf{Commutation in charts.}
The two derivations in the lemma statement correspond to:
\begin{align*}
df_{\lambda\mu} \circ \vec{D}_\lambda &\;\longleftrightarrow\; dT_{\lambda\mu} \cdot V_\lambda
\quad\text{(pushforward of $V_\lambda$ through $T_{\lambda\mu}$)}, \\
\vec{D}_\mu \circ f_{\lambda\mu} &\;\longleftrightarrow\; V_\mu \circ T_{\lambda\mu}
\quad\text{(evaluate $V_\mu$ at the image point)}.
\end{align*}
Their difference is the commutator error
$\|dT_{\lambda\mu} \cdot V_\lambda - V_\mu \circ T_{\lambda\mu}\|_{C^0}$.

\textbf{Convergence to zero.}
By Axiom~\ref{axiom:bk1_smooth_convergence}, the transition maps $T_{\lambda\mu}$
converge in the $C^\infty$ topology as $\lambda, \mu \to \Omega$: for any
$k \geq 0$ and compact $K$, $\|T_{\lambda\mu} - T_{\mu'\mu'}\|_{C^k(K)} \to 0$.
Since $V_\lambda$ and $V_\mu$ are locally bounded (Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}),
the commutator error satisfies:
\[
\|dT_{\lambda\mu} \cdot V_\lambda - V_\mu \circ T_{\lambda\mu}\|_{C^0}
\;\xrightarrow{\lambda,\mu \to \Omega}\; 0,
\]
establishing $df_{\lambda\mu} \circ \vec{D}_\lambda \approx \vec{D}_\mu \circ f_{\lambda\mu}$
with equality in the limit, as claimed.
\end{proof}
```

### Emergence of Drift Field (`theorem:bk1_emergence_of_drift_field`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2856`

- Proof status: `proven`
- Depends on: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_coherence_of_proto_drift_fields` (Coherence of Proto-Drift Fields)
- Cites: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence)
- Cited by: `definition:bk1_symbol_space` (Symbol Space); `definition:bk1_symbolic_flow` (Symbolic Flow); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `lemma:bk1_existence_and_uniqueness_of_flow` (Existence and Uniqueness of Flow); `lemma:bk1_local_stability_analysis` (Local Stability at the Reflective Fixed Locus); `lemma:bk1_well_posedness_of_symbolic_hamiltonian` (Well-posedness of Symbolic Hamiltonian); `proof:bk1_existence_and_uniqueness_of_flow`; `proof:bk1_sketch_fokker_planck_microdynamics`; `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `proof:bk1_sketch_smoothness_linearization` (Smoothness of Symbolic Hamiltonian); `proof:bk1_sketch_symbolic_connectivity` (Symbolic Connectivity via Hopf--Rinow); `proof:bk2_smoothness_symbolic_hamiltonian` (Smoothness of Symbolic Hamiltonian); `sec:bk1_summary_and_implications` (Summary and Implications); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-078`
- Witnesses: `ScholiumHzn.drift_field_unique`
- Countermodels: none
- Conditions: manifold integrals, PDE forms, smoothness, ordinal colimits, and curvature signs stay open/interpretive per row notes
- Formal boundary: Uniqueness of the stabilized limit; existence = the convergence hypothesis; smoothness/colimit open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

There exists a unique smooth vector field $D in Gamma(TM)$ on the symbolic manifold $M$ (see definition:bk1_symbolic_manifold_existence) that represents the stabilized limit of the proto-drift fields ${vec{D}_lambda}_{lambda_0 le lambda < Omega}$ through the colimit process. Specifically, for any point $p in M$ and any smooth function $f$ defined in a neighborhood of $p$, if $p = i_lambda(x_lambda)$ for $x_lambda in P_lambda$, then:
\[
D(f)(p) = lim_{lambda to Omega} vec{D}_lambda(f circ i_lambda)(x_lambda)
\]
where the limit is taken over representatives $x_lambda$ of $p$ as $lambda to Omega$. (Here $vec{D}_lambda$ acts as a derivation on functions).

For $lambda ge lambda_0$, each $vec{D}_lambda$ can be represented locally (via charts $varphi_lambda$ from Axiom axiom:bk1_symbolic_smoothness) as a vector field on an open set in $mathbb{R}^n$. The coherence condition (Lemma lemma:bk1_coherence_of_proto_drift_fields) ensures these local vector fields are compatible under the transition maps $f_{lambdamu}$. Axiom axiom:bk1_symbolic_smoothness guarantees that these local representations converge in the $C^infty$ topology as $lambda to Omega$. This limiting process defines a unique smooth vector field $D$ globally on $M$. The uniqueness also follows from the universal property of the colimit applied to the compatible system of proto-drift fields.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Emergence of Drift Field]
\label{theorem:bk1_emergence_of_drift_field}
There exists a unique smooth vector field $D \in \Gamma(TM)$ on the symbolic manifold $M$ (see \ref{definition:bk1_symbolic_manifold_existence}) that represents the stabilized limit of the proto-drift fields $\{\vec{D}_\lambda\}_{\lambda_0 \le \lambda < \Omega}$ through the colimit process. Specifically, for any point $p \in M$ and any smooth function $f$ defined in a neighborhood of $p$, if $p = i_\lambda(x_\lambda)$ for $x_\lambda \in P_\lambda$, then:
\[
D(f)(p) = \lim_{\lambda \to \Omega} \vec{D}_\lambda(f \circ i_\lambda)(x_\lambda)
\]
where the limit is taken over representatives $x_\lambda$ of $p$ as $\lambda \to \Omega$. (Here $\vec{D}_\lambda$ acts as a derivation on functions).

\begin{proof}[Limit Vector Field from Local Drift Coherence]
\label{proof:bk1_sketch_drift_limit_vector_field}
\leavevmode

For $\lambda \ge \lambda_0$, each $\vec{D}_\lambda$ can be represented locally (via charts $\varphi_\lambda$ from Axiom~\ref{axiom:bk1_symbolic_smoothness}) as a vector field on an open set in $\mathbb{R}^n$. The coherence condition (Lemma~\ref{lemma:bk1_coherence_of_proto_drift_fields}) ensures these local vector fields are compatible under the transition maps $f_{\lambda\mu}$. Axiom~\ref{axiom:bk1_symbolic_smoothness} guarantees that these local representations converge in the $C^\infty$ topology as $\lambda \to \Omega$. This limiting process defines a unique smooth vector field $D$ globally on $M$. The uniqueness also follows from the universal property of the colimit applied to the compatible system of proto-drift fields.
\end{proof}
\end{theorem}
```

### Limit Vector Field from Local Drift Coherence (`proof:bk1_sketch_drift_limit_vector_field`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2864`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `lemma:bk1_coherence_of_proto_drift_fields` (Coherence of Proto-Drift Fields)
- Cites: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `lemma:bk1_coherence_of_proto_drift_fields` (Coherence of Proto-Drift Fields)
- Cited by: none
- Macros used: none

**Statement / Body**

For $lambda ge lambda_0$, each $vec{D}_lambda$ can be represented locally (via charts $varphi_lambda$ from Axiom axiom:bk1_symbolic_smoothness) as a vector field on an open set in $mathbb{R}^n$. The coherence condition (Lemma lemma:bk1_coherence_of_proto_drift_fields) ensures these local vector fields are compatible under the transition maps $f_{lambdamu}$. Axiom axiom:bk1_symbolic_smoothness guarantees that these local representations converge in the $C^infty$ topology as $lambda to Omega$. This limiting process defines a unique smooth vector field $D$ globally on $M$. The uniqueness also follows from the universal property of the colimit applied to the compatible system of proto-drift fields.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Limit Vector Field from Local Drift Coherence]
\label{proof:bk1_sketch_drift_limit_vector_field}
\leavevmode

For $\lambda \ge \lambda_0$, each $\vec{D}_\lambda$ can be represented locally (via charts $\varphi_\lambda$ from Axiom~\ref{axiom:bk1_symbolic_smoothness}) as a vector field on an open set in $\mathbb{R}^n$. The coherence condition (Lemma~\ref{lemma:bk1_coherence_of_proto_drift_fields}) ensures these local vector fields are compatible under the transition maps $f_{\lambda\mu}$. Axiom~\ref{axiom:bk1_symbolic_smoothness} guarantees that these local representations converge in the $C^\infty$ topology as $\lambda \to \Omega$. This limiting process defines a unique smooth vector field $D$ globally on $M$. The uniqueness also follows from the universal property of the colimit applied to the compatible system of proto-drift fields.
\end{proof}
```

### Symbolic Flow (`definition:bk1_symbolic_flow`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2872`

- Proof status: `definitional`
- Depends on: `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field)
- Cites: `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field)
- Cited by: `definition:appB_observer_metric` (Observer-Relative Symbolic Metric); `definition:bk4_symbolic_flow_freedom` (Symbolic Flow Freedom); `lemma:bk1_existence_and_uniqueness_of_flow` (Existence and Uniqueness of Flow); `proof:bk1_existence_and_uniqueness_of_flow`; `proof:bk4_symbolic_identity_persistence` (Stability Criterion for Symbolic Identity Persistence); `scholium:bk7_popperian_extension` (Popperian Extension)
- Macros used: `\R`

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-062`
- Witnesses: `ScholiumDyn.flow_semigroup`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: The discrete flow with the semigroup law; the ODE flow stays open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The symbolic flow $Phi: R times M to M$ is the unique maximal flow generated by the emergent drift field $D$ (see def definition:bk1_proto_drift_field) on the symbolic manifold $M$ (see def definition:bk1_symbolic_manifold_existence), as established by the emergence of $D$ (see thm theorem:bk1_emergence_of_drift_field).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Flow]
\label{definition:bk1_symbolic_flow}
The symbolic flow $\Phi: \R \times M \to M$ is the unique maximal flow generated by the emergent drift field $D$ (see def~\ref{definition:bk1_proto_drift_field}) on the symbolic manifold $M$ (see def~\ref{definition:bk1_symbolic_manifold_existence}), as established by the emergence of $D$ (see thm~\ref{theorem:bk1_emergence_of_drift_field}).
\end{definition}
```

### Existence and Uniqueness of Flow (`lemma:bk1_existence_and_uniqueness_of_flow`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2877`

- Proof status: `proven`
- Depends on: `definition:bk1_symbolic_flow` (Symbolic Flow); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field)
- Cites: `definition:bk1_symbolic_flow` (Symbolic Flow); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field)
- Cited by: `definition:bk1_symbolic_coherence_velocity` (Symbolic Coherence Velocity)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-063`
- Witnesses: `ScholiumDyn.flow_unique`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: Discrete existence-and-uniqueness by induction; the smooth fundamental theorem stays open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The symbolic flow $Phi$ (def definition:bk1_symbolic_flow) exists and is unique by the fundamental theorem for flows of smooth vector fields on paracompact manifolds, given the properties of the symbolic manifold $M$ (def definition:bk1_symbolic_manifold_existence) and the emergence of the drift field $D$ (thm theorem:bk1_emergence_of_drift_field).

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Existence and Uniqueness of Flow]
\label{lemma:bk1_existence_and_uniqueness_of_flow}
The symbolic flow $\Phi$ (def~\ref{definition:bk1_symbolic_flow}) exists and is unique by the fundamental theorem for flows of smooth vector fields on paracompact manifolds, given the properties of the symbolic manifold $M$ (def~\ref{definition:bk1_symbolic_manifold_existence}) and the emergence of the drift field $D$ (thm~\ref{theorem:bk1_emergence_of_drift_field}).
\end{lemma}
```

### proof:bk1_existence_and_uniqueness_of_flow (`proof:bk1_existence_and_uniqueness_of_flow`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2881`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_flow` (Symbolic Flow); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field)
- Cites: `definition:bk1_symbolic_flow` (Symbolic Flow); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field)
- Cited by: none
- Macros used: `\R`

**Statement / Body**

By Thm. theorem:bk1_emergence_of_drift_field the emergent drift $D$ is a smooth vector field on $M$, and by Def. definition:bk1_symbolic_manifold_existence $M$ is a smooth, paracompact manifold. The fundamental theorem on flows of smooth vector fields then applies. Locally, $D$ is Lipschitz, so by Picard-Lindel\"of through each $x in M$ there passes a unique integral curve $t mapsto Phi(t,x)$ with $Phi(0,x)=x$ and $partial_t Phi = D(Phi)$; paracompactness lets these local solutions be patched into a single maximal flow, and uniqueness on overlaps (two integral curves through a common point coincide) makes the patching unambiguous. The maximal flow is complete-defined on all of $R times M$ as required by Def. definition:bk1_symbolic_flow-because the emergent drift is bounded in the observer metric, precluding finite-time escape, so every maximal integral curve extends to all $t in R$. Existence and uniqueness of $Phi$ follow.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk1_existence_and_uniqueness_of_flow}
\leavevmode
By Thm.~\ref{theorem:bk1_emergence_of_drift_field} the emergent drift $D$ is a smooth vector field on $M$, and by Def.~\ref{definition:bk1_symbolic_manifold_existence} $M$ is a smooth, paracompact manifold. The fundamental theorem on flows of smooth vector fields then applies. Locally, $D$ is Lipschitz, so by Picard--Lindel\"of through each $x \in M$ there passes a unique integral curve $t \mapsto \Phi(t,x)$ with $\Phi(0,x)=x$ and $\partial_t \Phi = D(\Phi)$; paracompactness lets these local solutions be patched into a single maximal flow, and uniqueness on overlaps (two integral curves through a common point coincide) makes the patching unambiguous. The maximal flow is complete---defined on all of $\R \times M$ as required by Def.~\ref{definition:bk1_symbolic_flow}---because the emergent drift is bounded in the observer metric, precluding finite-time escape, so every maximal integral curve extends to all $t \in \R$. Existence and uniqueness of $\Phi$ follow.
\end{proof}
```

### Existence of Metric (`lemma:bk1_existence_of_metric`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2886`

- Proof status: `proven`
- Depends on: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_coherence_of_proto_drift_fields` (Coherence of Proto-Drift Fields)
- Cites: `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence)
- Cited by: `definition:bk1_symbol_space` (Symbol Space); `definition:bk1_symbolic_distance` (Symbolic Distance); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density); `proof:bk1_sketch_fokker_planck_microdynamics`; `proof:bk1_sketch_smoothness_linearization` (Smoothness of Symbolic Hamiltonian); `proof:bk1_sketch_symbolic_connectivity` (Symbolic Connectivity via Hopf--Rinow); `proof:bk3_sketch_field_perturbation` (Bounded Sensitivity via Drift Compensation)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-042`
- Witnesses: `ScholiumD.combinedForm_nonneg`, `ScholiumD.combinedForm_pos_of_nondegenerate`, `ScholiumD.existence_of_metric_from_gluing`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: positive-definiteness of the combined R/D form kept as a self-contained normed-space fact (no manifold); chart-gluing to a single global metric re-read over FracturedAtlas with Glued C as a named hypothesis.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

There exists a Riemannian metric $g$ on $M$ that arises naturally from the interplay of the stabilization and differentiation processes (see def definition:bk1_symbolic_manifold_existence, def definition:bk1_pre_geometric_operators_and_stages, and def definition:bk1_proto_drift_field).

For each sufficiently large $lambda < Omega$ (say $lambda ge lambda_0$), define a
bilinear form $g_lambda$ on tangent vectors $X, Y$ at any point of $P_lambda$ by:
\[
g_lambda(X, Y)
= bigllangle R_lambda(X), R_lambda(Y) bigrrangle_0
+ alpha cdot bigllangle vec{D}_lambda(X), vec{D}_lambda(Y) bigrrangle_0,
\]
where $langlecdot,cdotrangle_0$ is the reference inner product from the proto-stage
charts (Def. definition:bk1_pre_geometric_operators_and_stages), $alpha > 0$ is a
coupling constant, and $vec{D}_lambda$ denotes the tangent-level action of the
proto-drift field (Def. definition:bk1_proto_drift_field).

Positive-definiteness.
Both summands are positive semi-definite, being
$langle L(cdot), L(cdot)rangle_0$ for a linear map $L$ and an inner product. Positivity of the sum then follows from the proto-stage
non-degeneracy condition: for any nonzero $X$, at least one of $R_lambda(X)$ or
$vec{D}_lambda(X)$ is nonzero (otherwise $X$ lies in the kernel of both operators,
contradicting the properness of the proto-stage structure).
Hence $g_lambda$ is a Riemannian metric on $P_lambda$.

Physical interpretation.
The $R_lambda$ term measures resistance to reflexive deformation (inner product in the
reflected frame); the $vec{D}_lambda$ term measures local drift magnitude (kinetic
energy of symbolic motion). Their combination captures the full geometric content of the
proto-stage.

Compatibility and convergence.
By Lemma lemma:bk1_coherence_of_proto_drift_fields, $R_lambda$ and $vec{D}_lambda$
are coherent with the transition maps $f_{lambdamu}$, so the family ${g_lambda}$
forms a compatible system: $f_{lambdamu}^* g_mu = g_lambda$ up to errors bounded by
the coherence deviation, which vanishes as $lambda to Omega$.
Axiom axiom:bk1_symbolic_smoothness then guarantees $C^infty$ convergence
of $g_lambda$ to a well-defined smooth Riemannian metric $g$ on
$M = varinjlim P_lambda$.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Existence of Metric]
\label{lemma:bk1_existence_of_metric}
There exists a Riemannian metric $g$ on $M$ that arises naturally from the interplay of the stabilization and differentiation processes (see def~\ref{definition:bk1_symbolic_manifold_existence}, def~\ref{definition:bk1_pre_geometric_operators_and_stages}, and def~\ref{definition:bk1_proto_drift_field}).
\begin{proof}[Construction of Proto-Metric on Symbolic Layers]
\label{proof:bk1_sketch_construction_proto_metric}
\leavevmode

For each sufficiently large $\lambda < \Omega$ (say $\lambda \ge \lambda_0$), define a
bilinear form $g_\lambda$ on tangent vectors $X, Y$ at any point of $P_\lambda$ by:
\[
g_\lambda(X, Y)
= \bigl\langle R_\lambda(X),\, R_\lambda(Y) \bigr\rangle_0
+ \alpha \cdot \bigl\langle \vec{D}_\lambda(X),\, \vec{D}_\lambda(Y) \bigr\rangle_0,
\]
where $\langle\cdot,\cdot\rangle_0$ is the reference inner product from the proto-stage
charts (Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}), $\alpha > 0$ is a
coupling constant, and $\vec{D}_\lambda$ denotes the tangent-level action of the
proto-drift field (Def.~\ref{definition:bk1_proto_drift_field}).

\textbf{Positive-definiteness.}
Both summands are positive semi-definite, being
$\langle L(\cdot), L(\cdot)\rangle_0$ for a linear map $L$ and an inner product. Positivity of the sum then follows from the proto-stage
non-degeneracy condition: for any nonzero $X$, at least one of $R_\lambda(X)$ or
$\vec{D}_\lambda(X)$ is nonzero (otherwise $X$ lies in the kernel of both operators,
contradicting the properness of the proto-stage structure).
Hence $g_\lambda$ is a Riemannian metric on $P_\lambda$.

\textbf{Physical interpretation.}
The $R_\lambda$ term measures resistance to reflexive deformation (inner product in the
reflected frame); the $\vec{D}_\lambda$ term measures local drift magnitude (kinetic
energy of symbolic motion). Their combination captures the full geometric content of the
proto-stage.

\textbf{Compatibility and convergence.}
By Lemma~\ref{lemma:bk1_coherence_of_proto_drift_fields}, $R_\lambda$ and $\vec{D}_\lambda$
are coherent with the transition maps $f_{\lambda\mu}$, so the family $\{g_\lambda\}$
forms a compatible system: $f_{\lambda\mu}^* g_\mu = g_\lambda$ up to errors bounded by
the coherence deviation, which vanishes as $\lambda \to \Omega$.
Axiom~\ref{axiom:bk1_symbolic_smoothness} then guarantees $C^\infty$ convergence
of $g_\lambda$ to a well-defined smooth Riemannian metric $g$ on
$M = \varinjlim P_\lambda$.
\end{proof}
\end{lemma}
```

### Construction of Proto-Metric on Symbolic Layers (`proof:bk1_sketch_construction_proto_metric`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2889`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$); `lemma:bk1_coherence_of_proto_drift_fields` (Coherence of Proto-Drift Fields)
- Cites: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_drift_field` (Proto-Drift Field $\vec{D}_\lambda$); `lemma:bk1_coherence_of_proto_drift_fields` (Coherence of Proto-Drift Fields)
- Cited by: none
- Macros used: none

**Statement / Body**

For each sufficiently large $lambda < Omega$ (say $lambda ge lambda_0$), define a
bilinear form $g_lambda$ on tangent vectors $X, Y$ at any point of $P_lambda$ by:
\[
g_lambda(X, Y)
= bigllangle R_lambda(X), R_lambda(Y) bigrrangle_0
+ alpha cdot bigllangle vec{D}_lambda(X), vec{D}_lambda(Y) bigrrangle_0,
\]
where $langlecdot,cdotrangle_0$ is the reference inner product from the proto-stage
charts (Def. definition:bk1_pre_geometric_operators_and_stages), $alpha > 0$ is a
coupling constant, and $vec{D}_lambda$ denotes the tangent-level action of the
proto-drift field (Def. definition:bk1_proto_drift_field).

Positive-definiteness.
Both summands are positive semi-definite, being
$langle L(cdot), L(cdot)rangle_0$ for a linear map $L$ and an inner product. Positivity of the sum then follows from the proto-stage
non-degeneracy condition: for any nonzero $X$, at least one of $R_lambda(X)$ or
$vec{D}_lambda(X)$ is nonzero (otherwise $X$ lies in the kernel of both operators,
contradicting the properness of the proto-stage structure).
Hence $g_lambda$ is a Riemannian metric on $P_lambda$.

Physical interpretation.
The $R_lambda$ term measures resistance to reflexive deformation (inner product in the
reflected frame); the $vec{D}_lambda$ term measures local drift magnitude (kinetic
energy of symbolic motion). Their combination captures the full geometric content of the
proto-stage.

Compatibility and convergence.
By Lemma lemma:bk1_coherence_of_proto_drift_fields, $R_lambda$ and $vec{D}_lambda$
are coherent with the transition maps $f_{lambdamu}$, so the family ${g_lambda}$
forms a compatible system: $f_{lambdamu}^* g_mu = g_lambda$ up to errors bounded by
the coherence deviation, which vanishes as $lambda to Omega$.
Axiom axiom:bk1_symbolic_smoothness then guarantees $C^infty$ convergence
of $g_lambda$ to a well-defined smooth Riemannian metric $g$ on
$M = varinjlim P_lambda$.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Construction of Proto-Metric on Symbolic Layers]
\label{proof:bk1_sketch_construction_proto_metric}
\leavevmode

For each sufficiently large $\lambda < \Omega$ (say $\lambda \ge \lambda_0$), define a
bilinear form $g_\lambda$ on tangent vectors $X, Y$ at any point of $P_\lambda$ by:
\[
g_\lambda(X, Y)
= \bigl\langle R_\lambda(X),\, R_\lambda(Y) \bigr\rangle_0
+ \alpha \cdot \bigl\langle \vec{D}_\lambda(X),\, \vec{D}_\lambda(Y) \bigr\rangle_0,
\]
where $\langle\cdot,\cdot\rangle_0$ is the reference inner product from the proto-stage
charts (Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}), $\alpha > 0$ is a
coupling constant, and $\vec{D}_\lambda$ denotes the tangent-level action of the
proto-drift field (Def.~\ref{definition:bk1_proto_drift_field}).

\textbf{Positive-definiteness.}
Both summands are positive semi-definite, being
$\langle L(\cdot), L(\cdot)\rangle_0$ for a linear map $L$ and an inner product. Positivity of the sum then follows from the proto-stage
non-degeneracy condition: for any nonzero $X$, at least one of $R_\lambda(X)$ or
$\vec{D}_\lambda(X)$ is nonzero (otherwise $X$ lies in the kernel of both operators,
contradicting the properness of the proto-stage structure).
Hence $g_\lambda$ is a Riemannian metric on $P_\lambda$.

\textbf{Physical interpretation.}
The $R_\lambda$ term measures resistance to reflexive deformation (inner product in the
reflected frame); the $\vec{D}_\lambda$ term measures local drift magnitude (kinetic
energy of symbolic motion). Their combination captures the full geometric content of the
proto-stage.

\textbf{Compatibility and convergence.}
By Lemma~\ref{lemma:bk1_coherence_of_proto_drift_fields}, $R_\lambda$ and $\vec{D}_\lambda$
are coherent with the transition maps $f_{\lambda\mu}$, so the family $\{g_\lambda\}$
forms a compatible system: $f_{\lambda\mu}^* g_\mu = g_\lambda$ up to errors bounded by
the coherence deviation, which vanishes as $\lambda \to \Omega$.
Axiom~\ref{axiom:bk1_symbolic_smoothness} then guarantees $C^\infty$ convergence
of $g_\lambda$ to a well-defined smooth Riemannian metric $g$ on
$M = \varinjlim P_\lambda$.
\end{proof}
```

### Symbolic Distance (`definition:bk1_symbolic_distance`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2929`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_existence_of_metric` (Existence of Metric)
- Cites: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_existence_of_metric` (Existence of Metric)
- Cited by: `definition:bk1_symbol_space` (Symbol Space); `lemma:bk1_completeness_of_symbolic_distance` (Completeness of Symbolic Distance); `proof:bk8_sketch_convergence_to_fixed_by_banach` (RG Fixed Point via Banach Contraction)
- Macros used: `\R`

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-065`
- Witnesses: `ScholiumDyn.resCost_symm`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: Symbolic distance as the path-infimum; Riemannian geodesics open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The symbolic distance $d: M times M to R_{geq 0}$ is the geodesic distance induced by the emergent Riemannian metric $g$ (see lemma lemma:bk1_existence_of_metric) on the symbolic manifold $M$ (see def definition:bk1_symbolic_manifold_existence).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Distance]
\label{definition:bk1_symbolic_distance}
The symbolic distance $d: M \times M \to \R_{\geq 0}$ is the geodesic distance induced by the emergent Riemannian metric $g$ (see lemma~\ref{lemma:bk1_existence_of_metric}) on the symbolic manifold $M$ (see def~\ref{definition:bk1_symbolic_manifold_existence}).
\end{definition}
```

### Completeness of Symbolic Distance (`lemma:bk1_completeness_of_symbolic_distance`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2934`

- Proof status: `proven`
- Depends on: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `axiom:bk1_topological_regularity` (Topological Regularity); `definition:bk1_symbolic_distance` (Symbolic Distance); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_manifold_emergence` (Manifold Emergence)
- Cites: `definition:bk1_symbolic_distance` (Symbolic Distance)
- Cited by: `axiom:bk4_refinement_contraction` (Refinement Contraction Axiom); `proof:bk1_sketch_direct_evaluation` (H-Theorem via Symbolic Integration by Parts); `proof:bk1_sketch_smoothness_linearization` (Smoothness of Symbolic Hamiltonian); `proof:bk4_neighborhood_completeness`; `proof:bk8_sketch_convergence_to_fixed_by_banach` (RG Fixed Point via Banach Contraction); `proposition:bk4_neighborhood_completeness` (Neighborhood Completeness)
- Macros used: `\R`

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-066`
- Witnesses: `ScholiumDyn.floor_complete`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: Floor completeness (Cauchy sequences eventually constant); Hopf-Rinow open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The metric space $(M, d)$ (def definition:bk1_symbolic_distance) is complete.

By Thm. theorem:bk1_manifold_emergence, $M$ is a smooth manifold, and by
Ax. axiom:bk1_topological_regularity it is connected and paracompact.
Lemma lemma:bk1_existence_of_metric equips $M$ with a smooth Riemannian metric $g$,
making $(M,g)$ a connected Riemannian manifold.

We verify geodesic completeness. The drift field $D$
(Thm. theorem:bk1_emergence_of_drift_field) is smooth and bounded on $M$; combined
with the Riemannian structure, the geodesic spray is complete: any unit-speed geodesic
$gamma: [0,T) to M$ satisfying $nabla_{dotgamma}dotgamma = 0$ extends to all of
$R$, since $M$ has no boundary and the metric is non-degenerate (Ax. axiom:bk1_symbolic_smoothness).

By the Hopf-Rinow theorem, a connected Riemannian manifold is geodesically complete if
and only if it is metrically complete. Since $(M,g)$ is geodesically complete, the induced
geodesic metric space $(M,d)$ is complete.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Completeness of Symbolic Distance]
\label{lemma:bk1_completeness_of_symbolic_distance}
The metric space $(M, d)$ (def~\ref{definition:bk1_symbolic_distance}) is complete.
\begin{proof}[Symbolic Connectivity via Hopf--Rinow]
\label{proof:bk1_sketch_symbolic_connectivity}
\leavevmode

By Thm.~\ref{theorem:bk1_manifold_emergence}, $M$ is a smooth manifold, and by
Ax.~\ref{axiom:bk1_topological_regularity} it is connected and paracompact.
Lemma~\ref{lemma:bk1_existence_of_metric} equips $M$ with a smooth Riemannian metric $g$,
making $(M,g)$ a connected Riemannian manifold.

We verify geodesic completeness. The drift field $D$
(Thm.~\ref{theorem:bk1_emergence_of_drift_field}) is smooth and bounded on $M$; combined
with the Riemannian structure, the geodesic spray is complete: any unit-speed geodesic
$\gamma: [0,T) \to M$ satisfying $\nabla_{\dot\gamma}\dot\gamma = 0$ extends to all of
$\R$, since $M$ has no boundary and the metric is non-degenerate (Ax.~\ref{axiom:bk1_symbolic_smoothness}).

By the Hopf--Rinow theorem, a connected Riemannian manifold is geodesically complete if
and only if it is metrically complete. Since $(M,g)$ is geodesically complete, the induced
geodesic metric space $(M,d)$ is complete.
\end{proof}
\end{lemma}
```

### Symbolic Connectivity via Hopf--Rinow (`proof:bk1_sketch_symbolic_connectivity`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2937`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `axiom:bk1_topological_regularity` (Topological Regularity); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_manifold_emergence` (Manifold Emergence)
- Cites: `axiom:bk1_symbolic_smoothness` (Symbolic Smoothness); `axiom:bk1_topological_regularity` (Topological Regularity); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_manifold_emergence` (Manifold Emergence)
- Cited by: none
- Macros used: `\R`

**Statement / Body**

By Thm. theorem:bk1_manifold_emergence, $M$ is a smooth manifold, and by
Ax. axiom:bk1_topological_regularity it is connected and paracompact.
Lemma lemma:bk1_existence_of_metric equips $M$ with a smooth Riemannian metric $g$,
making $(M,g)$ a connected Riemannian manifold.

We verify geodesic completeness. The drift field $D$
(Thm. theorem:bk1_emergence_of_drift_field) is smooth and bounded on $M$; combined
with the Riemannian structure, the geodesic spray is complete: any unit-speed geodesic
$gamma: [0,T) to M$ satisfying $nabla_{dotgamma}dotgamma = 0$ extends to all of
$R$, since $M$ has no boundary and the metric is non-degenerate (Ax. axiom:bk1_symbolic_smoothness).

By the Hopf-Rinow theorem, a connected Riemannian manifold is geodesically complete if
and only if it is metrically complete. Since $(M,g)$ is geodesically complete, the induced
geodesic metric space $(M,d)$ is complete.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Symbolic Connectivity via Hopf--Rinow]
\label{proof:bk1_sketch_symbolic_connectivity}
\leavevmode

By Thm.~\ref{theorem:bk1_manifold_emergence}, $M$ is a smooth manifold, and by
Ax.~\ref{axiom:bk1_topological_regularity} it is connected and paracompact.
Lemma~\ref{lemma:bk1_existence_of_metric} equips $M$ with a smooth Riemannian metric $g$,
making $(M,g)$ a connected Riemannian manifold.

We verify geodesic completeness. The drift field $D$
(Thm.~\ref{theorem:bk1_emergence_of_drift_field}) is smooth and bounded on $M$; combined
with the Riemannian structure, the geodesic spray is complete: any unit-speed geodesic
$\gamma: [0,T) \to M$ satisfying $\nabla_{\dot\gamma}\dot\gamma = 0$ extends to all of
$\R$, since $M$ has no boundary and the metric is non-degenerate (Ax.~\ref{axiom:bk1_symbolic_smoothness}).

By the Hopf--Rinow theorem, a connected Riemannian manifold is geodesically complete if
and only if it is metrically complete. Since $(M,g)$ is geodesically complete, the induced
geodesic metric space $(M,d)$ is complete.
\end{proof}
```

### Emergence of Stabilization Operator (`theorem:bk1_emergence_of_reflection_operator`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2957`

- Proof status: `proven`
- Depends on: `axiom:bk1_smooth_convergence` (Smooth Convergence); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space); `definition:bk1_reflection_operator` (Reflection Operator)
- Cites: `definition:bk1_reflection_operator` (Reflection Operator)
- Cited by: `corollary:bk1_fixed_point` (Reflective Fixed Locus); `definition:bk1_symbol_space` (Symbol Space); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `lemma:bk1_local_stability_analysis` (Local Stability at the Reflective Fixed Locus); `lemma:bk1_well_posedness_of_symbolic_hamiltonian` (Well-posedness of Symbolic Hamiltonian); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `proof:bk1_sketch_smoothness_linearization` (Smoothness of Symbolic Hamiltonian); `proof:bk8_sketch_convergence_to_fixed_by_banach` (RG Fixed Point via Banach Contraction); `sec:bk1_summary_and_implications` (Summary and Implications)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_B-006`
- Witnesses: `ScholiumB.idempotent_fixes_image`
- Countermodels: none
- Conditions: modeling laws are structure fields or explicit hypotheses; continuum/categorical content is NOT formalized
- Formal boundary: Only the stated idempotence consequence (R_stab^2 = R_stab) and its direct corollary (every image point is fixed) are formalized, as a fact about any idempotent self-map; the colimit-existence construction of R_stab from the proto-stage tower is not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

There exists a unique smooth state-level stabilization map
$R_{stab}: M to M$ that is the stabilized limit of the reflection
operators ${R_lambda}_{lambda < Omega}$ through the colimit process.
Moreover, \(R_{stab}\) is idempotent on stabilized states:
\[
R_{stab}^2 = R_{stab}.
\]
No strict metric contraction is asserted for \(R_{stab}\) or for the
tangent mirror \(R_{mir}\) of Def. definition:bk1_reflection_operator.
Convergence of iterates is a separate Lyapunov-descent question.

textbf{Existence and uniqueness of \(R_{stab}\).}
The proto-stages ${(P_lambda, g_lambda)}_{lambda < Omega}$ form a directed system with
coherence maps $f_{lambdamu}: P_lambda to P_mu$ for $lambda leq mu$
(Def. definition:bk1_pre_geometric_operators_and_stages,
Def. definition:bk1_proto_symbolic_space).
Each $R_lambda: P_lambda to P_lambda$ satisfies the naturality condition
$f_{lambdamu} circ R_lambda = R_mu circ f_{lambdamu}$ by the coherence requirement
on stabilization operators: $R_lambda$ maps each proto-stage into itself consistently with
the transition maps. By the universal property of the colimit
$M = varinjlim P_lambda$, there is a unique map $R_{stab}: M to M$ such that
$R_{stab} circ iota_lambda = iota_lambda circ R_lambda$ for each inclusion
$iota_lambda: P_lambda hookrightarrow M$.
Smoothness of \(R_{stab}\) follows from Ax. axiom:bk1_smooth_convergence: the
$R_lambda$ converge in $C^infty$ on compact subsets, so \(R_{stab}in C^infty(M)\).

Idempotence on the limit.
Each stage operator is idempotent by Def. definition:bk1_pre_geometric_operators_and_stages. Therefore
\[
R_{stab}^2 circ iota_lambda
= R_{stab}circ iota_lambdacirc R_lambda
= iota_lambdacirc R_lambda^2
= iota_lambdacirc R_lambda
= R_{stab}circ iota_lambda.
\]
Since the canonical maps jointly determine morphisms out of the colimit,
\(R_{stab}^2=R_{stab}\) on the stabilized image.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Emergence of Stabilization Operator]
\label{theorem:bk1_emergence_of_reflection_operator}
There exists a unique smooth state-level stabilization map
$R_{\mathrm{stab}}: M \to M$ that is the stabilized limit of the reflection
operators $\{R_\lambda\}_{\lambda < \Omega}$ through the colimit process.
Moreover, \(R_{\mathrm{stab}}\) is idempotent on stabilized states:
\[
R_{\mathrm{stab}}^2 = R_{\mathrm{stab}}.
\]
No strict metric contraction is asserted for \(R_{\mathrm{stab}}\) or for the
tangent mirror \(R_{\mathrm{mir}}\) of Def.~\ref{definition:bk1_reflection_operator}.
Convergence of iterates is a separate Lyapunov--descent question.

\begin{proof}[Limit of Stabilization Operators via Colimit]
\label{proof:bk1_sketch_limit_stabilization_colimit}
\leavevmode

\textbf{Existence and uniqueness of \(R_{\mathrm{stab}}\).}
The proto-stages $\{(P_\lambda, g_\lambda)\}_{\lambda < \Omega}$ form a directed system with
coherence maps $f_{\lambda\mu}: P_\lambda \to P_\mu$ for $\lambda \leq \mu$
(Def.~\ref{definition:bk1_pre_geometric_operators_and_stages},
Def.~\ref{definition:bk1_proto_symbolic_space}).
Each $R_\lambda: P_\lambda \to P_\lambda$ satisfies the naturality condition
$f_{\lambda\mu} \circ R_\lambda = R_\mu \circ f_{\lambda\mu}$ by the coherence requirement
on stabilization operators: $R_\lambda$ maps each proto-stage into itself consistently with
the transition maps. By the universal property of the colimit
$M = \varinjlim P_\lambda$, there is a unique map $R_{\mathrm{stab}}: M \to M$ such that
$R_{\mathrm{stab}} \circ \iota_\lambda = \iota_\lambda \circ R_\lambda$ for each inclusion
$\iota_\lambda: P_\lambda \hookrightarrow M$.
Smoothness of \(R_{\mathrm{stab}}\) follows from Ax.~\ref{axiom:bk1_smooth_convergence}: the
$R_\lambda$ converge in $C^\infty$ on compact subsets, so \(R_{\mathrm{stab}}\in C^\infty(M)\).

\textbf{Idempotence on the limit.}
Each stage operator is idempotent by Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}. Therefore
\[
R_{\mathrm{stab}}^2 \circ \iota_\lambda
= R_{\mathrm{stab}}\circ \iota_\lambda\circ R_\lambda
= \iota_\lambda\circ R_\lambda^2
= \iota_\lambda\circ R_\lambda
= R_{\mathrm{stab}}\circ \iota_\lambda.
\]
Since the canonical maps jointly determine morphisms out of the colimit,
\(R_{\mathrm{stab}}^2=R_{\mathrm{stab}}\) on the stabilized image.
\end{proof}
\end{theorem}
```

### Limit of Stabilization Operators via Colimit (`proof:bk1_sketch_limit_stabilization_colimit`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:2970`

- Proof status: `not_applicable`
- Depends on: `axiom:bk1_smooth_convergence` (Smooth Convergence); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cites: `axiom:bk1_smooth_convergence` (Smooth Convergence); `definition:bk1_pre_geometric_operators_and_stages` (Pre-geometric Operators and Stages); `definition:bk1_proto_symbolic_space` (Proto-symbolic Space)
- Cited by: none
- Macros used: none

**Statement / Body**

textbf{Existence and uniqueness of \(R_{stab}\).}
The proto-stages ${(P_lambda, g_lambda)}_{lambda < Omega}$ form a directed system with
coherence maps $f_{lambdamu}: P_lambda to P_mu$ for $lambda leq mu$
(Def. definition:bk1_pre_geometric_operators_and_stages,
Def. definition:bk1_proto_symbolic_space).
Each $R_lambda: P_lambda to P_lambda$ satisfies the naturality condition
$f_{lambdamu} circ R_lambda = R_mu circ f_{lambdamu}$ by the coherence requirement
on stabilization operators: $R_lambda$ maps each proto-stage into itself consistently with
the transition maps. By the universal property of the colimit
$M = varinjlim P_lambda$, there is a unique map $R_{stab}: M to M$ such that
$R_{stab} circ iota_lambda = iota_lambda circ R_lambda$ for each inclusion
$iota_lambda: P_lambda hookrightarrow M$.
Smoothness of \(R_{stab}\) follows from Ax. axiom:bk1_smooth_convergence: the
$R_lambda$ converge in $C^infty$ on compact subsets, so \(R_{stab}in C^infty(M)\).

Idempotence on the limit.
Each stage operator is idempotent by Def. definition:bk1_pre_geometric_operators_and_stages. Therefore
\[
R_{stab}^2 circ iota_lambda
= R_{stab}circ iota_lambdacirc R_lambda
= iota_lambdacirc R_lambda^2
= iota_lambdacirc R_lambda
= R_{stab}circ iota_lambda.
\]
Since the canonical maps jointly determine morphisms out of the colimit,
\(R_{stab}^2=R_{stab}\) on the stabilized image.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Limit of Stabilization Operators via Colimit]
\label{proof:bk1_sketch_limit_stabilization_colimit}
\leavevmode

\textbf{Existence and uniqueness of \(R_{\mathrm{stab}}\).}
The proto-stages $\{(P_\lambda, g_\lambda)\}_{\lambda < \Omega}$ form a directed system with
coherence maps $f_{\lambda\mu}: P_\lambda \to P_\mu$ for $\lambda \leq \mu$
(Def.~\ref{definition:bk1_pre_geometric_operators_and_stages},
Def.~\ref{definition:bk1_proto_symbolic_space}).
Each $R_\lambda: P_\lambda \to P_\lambda$ satisfies the naturality condition
$f_{\lambda\mu} \circ R_\lambda = R_\mu \circ f_{\lambda\mu}$ by the coherence requirement
on stabilization operators: $R_\lambda$ maps each proto-stage into itself consistently with
the transition maps. By the universal property of the colimit
$M = \varinjlim P_\lambda$, there is a unique map $R_{\mathrm{stab}}: M \to M$ such that
$R_{\mathrm{stab}} \circ \iota_\lambda = \iota_\lambda \circ R_\lambda$ for each inclusion
$\iota_\lambda: P_\lambda \hookrightarrow M$.
Smoothness of \(R_{\mathrm{stab}}\) follows from Ax.~\ref{axiom:bk1_smooth_convergence}: the
$R_\lambda$ converge in $C^\infty$ on compact subsets, so \(R_{\mathrm{stab}}\in C^\infty(M)\).

\textbf{Idempotence on the limit.}
Each stage operator is idempotent by Def.~\ref{definition:bk1_pre_geometric_operators_and_stages}. Therefore
\[
R_{\mathrm{stab}}^2 \circ \iota_\lambda
= R_{\mathrm{stab}}\circ \iota_\lambda\circ R_\lambda
= \iota_\lambda\circ R_\lambda^2
= \iota_\lambda\circ R_\lambda
= R_{\mathrm{stab}}\circ \iota_\lambda.
\]
Since the canonical maps jointly determine morphisms out of the colimit,
\(R_{\mathrm{stab}}^2=R_{\mathrm{stab}}\) on the stabilized image.
\end{proof}
```

### Reflective Fixed Locus (`corollary:bk1_fixed_point`)

Role: `corollary` | Type: `corollary` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3003`

- Proof status: `proven`
- Depends on: `definition:bk1_reflection_operator` (Reflection Operator); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cites: `definition:bk1_reflection_operator` (Reflection Operator); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cited by: `axiom:bk8_binding_curvature_limit` (Frame Relativity of Meaning); `definition:bk1_bounded_reflexive_emergence` (Bounded Reflexive Emergence); `definition:bk8_transform_group` (Frame Transform Group); `lemma:bk1_local_stability_analysis` (Local Stability at the Reflective Fixed Locus); `proof:bk1_constitutive_bootstrap_extraction` (Extraction from Reflective Closure); `proof:bk1_proof_of_dual_horizon_necessity_theorem` (Proof of Dual Horizon Necessity Theorem); `theorem:bk7_reflective_convergence_to_stable_identity` (Reflective Convergence to Stable Identity)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_B-007`
- Witnesses: `ScholiumB.idempotent_fixLocus_nonempty`, `ScholiumB.idempotent_fixes_image`
- Countermodels: none
- Conditions: modeling laws are structure fields or explicit hypotheses; continuum/categorical content is NOT formalized
- Formal boundary: The corollary's exact argument (fixed locus nonempty whenever the stabilized image is nonempty, via idempotence) is formalized in full generality for idempotent self-maps; the non-uniqueness discussion is not separately stated since no additional structure (contraction/Lyapunov) is modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The state-level stabilization operator \(R_{stab}:Mto M\)
(Def. definition:bk1_reflection_operator;
Thm. theorem:bk1_emergence_of_reflection_operator) determines a reflective
fixed locus
\[
Fix(R_{stab})
 := {xin M : R_{stab}(x)=x}.
\]
This locus is nonempty whenever the stabilized image of \(R_{stab}\) is
nonempty. A unique fixed point requires an additional hypothesis, such as a
genuine contraction on a complete basin or a Lyapunov/Caristi descent structure
with a singleton minimal set.

If \(yin im(R_{stab})\), then \(y=R_{stab}(x)\)
for some \(xin M\). By idempotence,
\[
R_{stab}(y)=R_{stab}(R_{stab}(x))
=R_{stab}(x)=y.
\]
Thus every stabilized state is fixed. This establishes the fixed locus without
asserting uniqueness.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Reflective Fixed Locus]
\label{corollary:bk1_fixed_point}
The state-level stabilization operator \(R_{\mathrm{stab}}:M\to M\)
(Def.~\ref{definition:bk1_reflection_operator};
Thm.~\ref{theorem:bk1_emergence_of_reflection_operator}) determines a reflective
fixed locus
\[
\operatorname{Fix}(R_{\mathrm{stab}})
  := \{x\in M : R_{\mathrm{stab}}(x)=x\}.
\]
This locus is nonempty whenever the stabilized image of \(R_{\mathrm{stab}}\) is
nonempty. A unique fixed point requires an additional hypothesis, such as a
genuine contraction on a complete basin or a Lyapunov/Caristi descent structure
with a singleton minimal set.

\begin{proof}[Fixed Locus from Idempotent Stabilization]
\label{proof:bk1_fixed_point_contraction_stability}
\leavevmode

If \(y\in \operatorname{im}(R_{\mathrm{stab}})\), then \(y=R_{\mathrm{stab}}(x)\)
for some \(x\in M\). By idempotence,
\[
R_{\mathrm{stab}}(y)=R_{\mathrm{stab}}(R_{\mathrm{stab}}(x))
=R_{\mathrm{stab}}(x)=y.
\]
Thus every stabilized state is fixed. This establishes the fixed locus without
asserting uniqueness.
\end{proof}
\end{corollary}
```

### Fixed Locus from Idempotent Stabilization (`proof:bk1_fixed_point_contraction_stability`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3018`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

If \(yin im(R_{stab})\), then \(y=R_{stab}(x)\)
for some \(xin M\). By idempotence,
\[
R_{stab}(y)=R_{stab}(R_{stab}(x))
=R_{stab}(x)=y.
\]
Thus every stabilized state is fixed. This establishes the fixed locus without
asserting uniqueness.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Fixed Locus from Idempotent Stabilization]
\label{proof:bk1_fixed_point_contraction_stability}
\leavevmode

If \(y\in \operatorname{im}(R_{\mathrm{stab}})\), then \(y=R_{\mathrm{stab}}(x)\)
for some \(x\in M\). By idempotence,
\[
R_{\mathrm{stab}}(y)=R_{\mathrm{stab}}(R_{\mathrm{stab}}(x))
=R_{\mathrm{stab}}(x)=y.
\]
Thus every stabilized state is fixed. This establishes the fixed locus without
asserting uniqueness.
\end{proof}
```

### Symbolic Thermodynamics Foundations (`sec:bk1_symbolic_thermodynamics_foundations`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3032`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbol Space (`definition:bk1_symbol_space`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3035`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_distance` (Symbolic Distance); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cites: `definition:bk1_symbolic_distance` (Symbolic Distance); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cited by: `scholium:bk4_symbolic_potential_energy` (Symbolic Potential and the Thermodynamics of Sampling); `theorem:bk1_realization_of_symbolic_phase_transitions` (Realization of Symbolic Phase Transitions); `theorem:bk1_sructurual_correspondence` (Structural Correspondence)
- Macros used: none

**Statement / Body**

The symbol space is the tuple $(M, g, D, R, d)$ consisting of the emergent symbolic manifold $M$ (def definition:bk1_symbolic_manifold_existence), Riemannian metric $g$ (lemma lemma:bk1_existence_of_metric), drift vector field $D$ (thm theorem:bk1_emergence_of_drift_field), reflection operator $R$ (thm theorem:bk1_emergence_of_reflection_operator), and symbolic distance $d$ (def definition:bk1_symbolic_distance).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbol Space]
\label{definition:bk1_symbol_space}
The symbol space is the tuple $(M, g, D, R, d)$ consisting of the emergent symbolic manifold $M$ (def~\ref{definition:bk1_symbolic_manifold_existence}), Riemannian metric $g$ (lemma~\ref{lemma:bk1_existence_of_metric}), drift vector field $D$ (thm~\ref{theorem:bk1_emergence_of_drift_field}), reflection operator $R$ (thm~\ref{theorem:bk1_emergence_of_reflection_operator}), and symbolic distance $d$ (def~\ref{definition:bk1_symbolic_distance}).
\end{definition}
```

### Symbolic Probability Density (`definition:bk1_symbolic_probabilty_density`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3040`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_existence_of_metric` (Existence of Metric)
- Cites: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_existence_of_metric` (Existence of Metric)
- Cited by: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_symbolic_action_functional` (Symbolic Action Functional); `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_field_curvature_tensor` (Symbolic Field Curvature Tensor); `definition:bk1_symbolic_information_geometry` (Symbolic Information Geometry); `lemma:bk1_horizon_crossing_conservation` (Horizon-Crossing Conservation); `proof:bk1_lagrange_free_energy` (Free Energy Minimization via Lagrange Multipliers); `proof:bk1_sketch_fokker_planck_microdynamics`; `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_sructurual_correspondence` (Structural Correspondence); `theorem:bk1_variational_principle` (Variational Principle)
- Macros used: `\R`

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-082`
- Witnesses: `Book2.gibbs_isDensity`
- Countermodels: none
- Conditions: finite nonempty symbolic alphabet (NeZero n); positive beta for the variational principle; nonzero beta for the equilibrium value; the stochastic-kernel evolution law and detailed balance are named structures, not derived from the PDE
- Formal boundary: Finite density form.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A symbolic probability density is a smooth function $rho: M times R to R_{geq 0}$ satisfying $int_M rho(x,s) dmu_g(x) = 1$ for all symbolic times $s in R$, where $M$ is the symbolic manifold (def definition:bk1_symbolic_manifold_existence) and $dmu_g$ is the Riemannian volume form induced by the metric $g$ (lemma lemma:bk1_existence_of_metric).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Probability Density]
\label{definition:bk1_symbolic_probabilty_density}
A symbolic probability density is a smooth function $\rho: M \times \R \to \R_{\geq 0}$ satisfying $\int_M \rho(x,s) \, d\mu_g(x) = 1$ for all symbolic times $s \in \R$, where $M$ is the symbolic manifold (def~\ref{definition:bk1_symbolic_manifold_existence}) and $d\mu_g$ is the Riemannian volume form induced by the metric $g$ (lemma~\ref{lemma:bk1_existence_of_metric}).
\end{definition}
```

### Symbolic Entropy (`definition:bk1_symbolic_entropy`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3045`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density)
- Cites: `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density)
- Cited by: `proof:bk1_lagrange_free_energy` (Free Energy Minimization via Lagrange Multipliers); `proof:bk1_sketch_direct_evaluation` (H-Theorem via Symbolic Integration by Parts); `theorem:bk1_sructurual_correspondence` (Structural Correspondence); `theorem:bk1_the_fokker_planck_equation_theorem` (Information Geometric Interpretation); `theorem:bk1_variational_principle` (Variational Principle)
- Macros used: `\R`

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-083`
- Witnesses: `Book2.entropy_nonneg`
- Countermodels: none
- Conditions: finite nonempty symbolic alphabet (NeZero n); positive beta for the variational principle; nonzero beta for the equilibrium value; the stochastic-kernel evolution law and detailed balance are named structures, not derived from the PDE
- Formal boundary: Finite entropy form.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The symbolic entropy \( S: R to R \) is defined as:
\[
S[rho](s) = -int_M rho(x,s) log rho(x,s) dmu_g(x)
\]
where $rho$ is a symbolic probability density (def definition:bk1_symbolic_probabilty_density).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Entropy]
\label{definition:bk1_symbolic_entropy}
The symbolic entropy \( S: \R \to \R \) is defined as:
\[
S[\rho](s) = -\int_M \rho(x,s) \log \rho(x,s) \, d\mu_g(x)
\]
where $\rho$ is a symbolic probability density (def~\ref{definition:bk1_symbolic_probabilty_density}).
\end{definition}
```

### Symbolic Hamiltonian (`definition:bk1_symbolic_hamiltonian`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3054`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cites: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cited by: `lemma:bk1_well_posedness_of_symbolic_hamiltonian` (Well-posedness of Symbolic Hamiltonian); `proof:bk1_lagrange_free_energy` (Free Energy Minimization via Lagrange Multipliers); `proof:bk1_sketch_direct_evaluation` (H-Theorem via Symbolic Integration by Parts); `theorem:bk1_sructurual_correspondence` (Structural Correspondence); `theorem:bk1_variational_principle` (Variational Principle)
- Macros used: `\R`, `\norm`

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-043`
- Witnesses: `ScholiumD.SymbolicHamiltonianFirstTerm.pos`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: only the regularized first term kappa/(||D||_g + eps); the trace/linearization second term is not modeled since its sign is unconstrained by the source.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The symbolic Hamiltonian $H: M to R$ quantifies local symbolic coherence:
\[
H(x) = frac{kappa}{norm{D(x)}_g + epsilon} + lambda cdot tr(L_x)
\]
where $kappa, lambda > 0$, $epsilon > 0$ (regularization), $norm{D(x)}_g$ is the norm of the drift field $D$ (thm theorem:bk1_emergence_of_drift_field) with respect to the Riemannian metric $g$ (lemma lemma:bk1_existence_of_metric) on the manifold $M$ (def definition:bk1_symbolic_manifold_existence). $L_x = P_{R(x) to x} circ dR_x$ is the linearization of the reflection operator $R$ (thm theorem:bk1_emergence_of_reflection_operator), composed of the differential $dR_x$ and parallel transport $P$ along the geodesic from $R(x)$ to $x$. The term $tr(L_x)$ measures local volume contraction induced by $R$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Hamiltonian]
\label{definition:bk1_symbolic_hamiltonian}
The symbolic Hamiltonian $H: M \to \R$ quantifies local symbolic coherence:
\[
H(x) = \frac{\kappa}{\norm{D(x)}_g + \epsilon} + \lambda \cdot \operatorname{tr}(L_x)
\]
where $\kappa, \lambda > 0$, $\epsilon > 0$ (regularization), $\norm{D(x)}_g$ is the norm of the drift field $D$ (thm~\ref{theorem:bk1_emergence_of_drift_field}) with respect to the Riemannian metric $g$ (lemma~\ref{lemma:bk1_existence_of_metric}) on the manifold $M$ (def~\ref{definition:bk1_symbolic_manifold_existence}). $L_x = P_{R(x) \to x} \circ dR_x$ is the linearization of the reflection operator $R$ (thm~\ref{theorem:bk1_emergence_of_reflection_operator}), composed of the differential $dR_x$ and parallel transport $P$ along the geodesic from $R(x)$ to $x$. The term $\operatorname{tr}(L_x)$ measures local volume contraction induced by $R$.
\end{definition}
```

### Well-posedness of Symbolic Hamiltonian (`lemma:bk1_well_posedness_of_symbolic_hamiltonian`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3062`

- Proof status: `proven`
- Depends on: `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_completeness_of_symbolic_distance` (Completeness of Symbolic Distance); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cites: `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cited by: none
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-044`
- Witnesses: `ScholiumD.SymbolicHamiltonianFirstTerm.pos`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: well-posedness of the first term's denominator only (never zero given eps>0); smoothness on M is not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The symbolic Hamiltonian $H$
(Def. definition:bk1_symbolic_hamiltonian) is well-defined and smooth on
symbolic manifold $M$
(Def. definition:bk1_symbolic_manifold_existence).
Smoothness follows from drift and reflection structure
(Thm. theorem:bk1_emergence_of_drift_field,
Thm. theorem:bk1_emergence_of_reflection_operator).

We verify smoothness of each term in
$H(x) = kappa / (\|D(x)\|_g + epsilon) + lambdacdottr(L_x)$.

First term.
$D in C^infty(TM)$ by Thm. theorem:bk1_emergence_of_drift_field, and
$g in C^infty$ by Lemma lemma:bk1_existence_of_metric, so the pointwise norm
$x mapsto \|D(x)\|_g = sqrt{g_x(D(x),D(x))}$ is smooth on $M$
(Def. definition:bk1_symbolic_manifold_existence).
Since $epsilon > 0$, the denominator $\|D(x)\|_g + epsilon geq epsilon > 0$ everywhere,
so $x mapsto kappa/(\|D(x)\|_g + epsilon)$ is a smooth composition of smooth functions.

For the second term, since $R in C^infty(M,M)$ by Thm. theorem:bk1_emergence_of_reflection_operator, the
differential $dR_x: T_xM to T_{R(x)}M$ varies smoothly in $x$.
Parallel transport $P_{R(x)to x}: T_{R(x)}M to T_xM$ along the minimizing geodesic
from $R(x)$ to $x$ is smooth as a function of $x$ on any open set where the exponential
map is a diffeomorphism (Lemma lemma:bk1_completeness_of_symbolic_distance gives
completeness; standard Riemannian theory gives local smoothness of parallel transport).
Hence $L_x = P_{R(x)to x} circ dR_x in End(T_xM)$ is a smooth
endomorphism field, and $x mapsto tr(L_x)$ is smooth.
Smoothness of $H$ follows, as it is a sum of two smooth functions.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Well-posedness of Symbolic Hamiltonian]
\label{lemma:bk1_well_posedness_of_symbolic_hamiltonian}
\leavevmode\newline
The symbolic Hamiltonian $H$
(Def.~\ref{definition:bk1_symbolic_hamiltonian}) is well-defined and smooth on
symbolic manifold $M$
(Def.~\ref{definition:bk1_symbolic_manifold_existence}).
Smoothness follows from drift and reflection structure
(Thm.~\ref{theorem:bk1_emergence_of_drift_field},
Thm.~\ref{theorem:bk1_emergence_of_reflection_operator}).
\begin{proof}[Smoothness of Symbolic Hamiltonian]
\label{proof:bk1_sketch_smoothness_linearization}
\leavevmode

We verify smoothness of each term in
$H(x) = \kappa\,/\,(\|D(x)\|_g + \epsilon) + \lambda\cdot\operatorname{tr}(L_x)$.

\textbf{First term.}
$D \in C^\infty(TM)$ by Thm.~\ref{theorem:bk1_emergence_of_drift_field}, and
$g \in C^\infty$ by Lemma~\ref{lemma:bk1_existence_of_metric}, so the pointwise norm
$x \mapsto \|D(x)\|_g = \sqrt{g_x(D(x),D(x))}$ is smooth on $M$
(Def.~\ref{definition:bk1_symbolic_manifold_existence}).
Since $\epsilon > 0$, the denominator $\|D(x)\|_g + \epsilon \geq \epsilon > 0$ everywhere,
so $x \mapsto \kappa/(\|D(x)\|_g + \epsilon)$ is a smooth composition of smooth functions.

For the second term, since $R \in C^\infty(M,M)$ by Thm.~\ref{theorem:bk1_emergence_of_reflection_operator}, the
differential $dR_x: T_xM \to T_{R(x)}M$ varies smoothly in $x$.
Parallel transport $P_{R(x)\to x}: T_{R(x)}M \to T_xM$ along the minimizing geodesic
from $R(x)$ to $x$ is smooth as a function of $x$ on any open set where the exponential
map is a diffeomorphism (Lemma~\ref{lemma:bk1_completeness_of_symbolic_distance} gives
completeness; standard Riemannian theory gives local smoothness of parallel transport).
Hence $L_x = P_{R(x)\to x} \circ dR_x \in \operatorname{End}(T_xM)$ is a smooth
endomorphism field, and $x \mapsto \operatorname{tr}(L_x)$ is smooth.
Smoothness of $H$ follows, as it is a sum of two smooth functions.
\end{proof}
\end{lemma}
```

### Smoothness of Symbolic Hamiltonian (`proof:bk1_sketch_smoothness_linearization`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3072`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_completeness_of_symbolic_distance` (Completeness of Symbolic Distance); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cites: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `lemma:bk1_completeness_of_symbolic_distance` (Completeness of Symbolic Distance); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cited by: none
- Macros used: none

**Statement / Body**

We verify smoothness of each term in
$H(x) = kappa / (\|D(x)\|_g + epsilon) + lambdacdottr(L_x)$.

First term.
$D in C^infty(TM)$ by Thm. theorem:bk1_emergence_of_drift_field, and
$g in C^infty$ by Lemma lemma:bk1_existence_of_metric, so the pointwise norm
$x mapsto \|D(x)\|_g = sqrt{g_x(D(x),D(x))}$ is smooth on $M$
(Def. definition:bk1_symbolic_manifold_existence).
Since $epsilon > 0$, the denominator $\|D(x)\|_g + epsilon geq epsilon > 0$ everywhere,
so $x mapsto kappa/(\|D(x)\|_g + epsilon)$ is a smooth composition of smooth functions.

For the second term, since $R in C^infty(M,M)$ by Thm. theorem:bk1_emergence_of_reflection_operator, the
differential $dR_x: T_xM to T_{R(x)}M$ varies smoothly in $x$.
Parallel transport $P_{R(x)to x}: T_{R(x)}M to T_xM$ along the minimizing geodesic
from $R(x)$ to $x$ is smooth as a function of $x$ on any open set where the exponential
map is a diffeomorphism (Lemma lemma:bk1_completeness_of_symbolic_distance gives
completeness; standard Riemannian theory gives local smoothness of parallel transport).
Hence $L_x = P_{R(x)to x} circ dR_x in End(T_xM)$ is a smooth
endomorphism field, and $x mapsto tr(L_x)$ is smooth.
Smoothness of $H$ follows, as it is a sum of two smooth functions.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Smoothness of Symbolic Hamiltonian]
\label{proof:bk1_sketch_smoothness_linearization}
\leavevmode

We verify smoothness of each term in
$H(x) = \kappa\,/\,(\|D(x)\|_g + \epsilon) + \lambda\cdot\operatorname{tr}(L_x)$.

\textbf{First term.}
$D \in C^\infty(TM)$ by Thm.~\ref{theorem:bk1_emergence_of_drift_field}, and
$g \in C^\infty$ by Lemma~\ref{lemma:bk1_existence_of_metric}, so the pointwise norm
$x \mapsto \|D(x)\|_g = \sqrt{g_x(D(x),D(x))}$ is smooth on $M$
(Def.~\ref{definition:bk1_symbolic_manifold_existence}).
Since $\epsilon > 0$, the denominator $\|D(x)\|_g + \epsilon \geq \epsilon > 0$ everywhere,
so $x \mapsto \kappa/(\|D(x)\|_g + \epsilon)$ is a smooth composition of smooth functions.

For the second term, since $R \in C^\infty(M,M)$ by Thm.~\ref{theorem:bk1_emergence_of_reflection_operator}, the
differential $dR_x: T_xM \to T_{R(x)}M$ varies smoothly in $x$.
Parallel transport $P_{R(x)\to x}: T_{R(x)}M \to T_xM$ along the minimizing geodesic
from $R(x)$ to $x$ is smooth as a function of $x$ on any open set where the exponential
map is a diffeomorphism (Lemma~\ref{lemma:bk1_completeness_of_symbolic_distance} gives
completeness; standard Riemannian theory gives local smoothness of parallel transport).
Hence $L_x = P_{R(x)\to x} \circ dR_x \in \operatorname{End}(T_xM)$ is a smooth
endomorphism field, and $x \mapsto \operatorname{tr}(L_x)$ is smooth.
Smoothness of $H$ follows, as it is a sum of two smooth functions.
\end{proof}
```

### Fundamental Relation – Fokker–Planck Equation (`theorem:bk1_fundamental_relation_fokker_plank_equation`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3098`

- Proof status: `proven`
- Depends on: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field)
- Cites: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field)
- Cited by: `axiom:bk2_symbolic_fokker_planck_equation` (Symbolic Fokker-Planck Equation); `axiom:bk8_surface_energy_dynamics` (Coupled Differential Dynamics); `corollary:bk1_wasserstein_geometric_interpretation` (Wasserstein Geometric Interpretation); `definition:bk1_symbolic_action_functional` (Symbolic Action Functional); `definition:bk6_symbolic_laplace_beltrami_operator_complete` (Symbolic Laplace–Beltrami Operator); `proof:bk1_sketch_direct_evaluation` (H-Theorem via Symbolic Integration by Parts); `proof:bk1_sketch_fluctuation_dissipation` (Fluctuation--Dissipation via Kubo Linear Response); `proof:bk1_sketch_fokker_planck_action` (Fokker--Planck from Symbolic Action via Martin--Siggia--Rose); `proof:bk1_sketch_gradient_flow_thermodynamics` (Gradient Flow Structure via JKO); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `proof:bk1_sketch_thermo_analogy_fokker_planck` (Thermodynamic Analogy via Symbolic Fokker--Planck); `proof:bk2_sketch_wasserstein_gradient_flow` (Wasserstein Gradient Flow via Jordan--Kinderlehrer--Otto); `proof:bk6_symbolic_diffusion_governs_evolution`; `proof:bk6_symbolic_fokker_planck_bifurcation` (Fokker--Planck Correspondence at Bifurcation); `remark:bk2_symbolic_hamiltonian` (Motivating the Canonical Symbolic Hamiltonian); `scholium:bk3_hypotheses_as_cognitive_membranes` (Hypotheses as Cognitive Membranes); `sec:bk1_summary_and_implications` (Summary and Implications); `theorem:bk1_h_theorem_for_symbolic_evolution` (H-Theorem for Symbolic Evolution); `theorem:bk1_princple_of_least_action` (Principle of Least Action); `theorem:bk1_symbolic_fluctuation_dissipation_relation` (Symbolic Fluctuation–Dissipation Relation); `theorem:bk1_the_fokker_planck_equation_theorem` (Information Geometric Interpretation); `theorem:bk6_symbolic_diffusion_governs_evolution` (Symbolic Diffusion Operator Governs Thermodynamic Evolution)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-081`
- Witnesses: `Book2.evolve_conserves`, `Book2H.h_theorem`
- Countermodels: none
- Conditions: finite nonempty symbolic alphabet (NeZero n); positive beta for the variational principle; nonzero beta for the equilibrium value; the stochastic-kernel evolution law and detailed balance are named structures, not derived from the PDE
- Formal boundary: Discrete skeleton with conservation and the H-theorem; the manifold PDE open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The evolution of $rho$ is governed by:
\[
frac{partial rho}{partial s} = -nabla cdot (rho D) + beta^{-1} nabla^2 rho
\]
where $nabla cdot$ is the divergence, $nabla^2$ is the Laplace–Beltrami operator on $(M,g)$, and $beta > 0$ is an inverse temperature parameter. Here $rho$ is a symbolic probability density (def definition:bk1_symbolic_probabilty_density) on the symbolic manifold $M$ (def definition:bk1_symbolic_manifold_existence), with drift field $D$ (thm theorem:bk1_emergence_of_drift_field).

This follows from microscopic symbolic dynamics: deterministic transport along
$D$ plus diffusive regularization on $(M,g)$
(Thm. theorem:bk1_emergence_of_drift_field,
Def. definition:bk1_symbolic_manifold_existence,
Lem. lemma:bk1_existence_of_metric).
The drift term advects probability, diffusion models bounded symbolic
stochasticity in $rho$
(Def. definition:bk1_symbolic_probabilty_density), and
$int_M rho dmu_g$ is conserved.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Fundamental Relation – Fokker–Planck Equation]
\label{theorem:bk1_fundamental_relation_fokker_plank_equation}
The evolution of $\rho$ is governed by:
\[
\frac{\partial \rho}{\partial s} = -\nabla \cdot (\rho D) + \beta^{-1} \nabla^2 \rho
\]
where $\nabla \cdot$ is the divergence, $\nabla^2$ is the Laplace–Beltrami operator on $(M,g)$, and $\beta > 0$ is an inverse temperature parameter. Here $\rho$ is a symbolic probability density (def~\ref{definition:bk1_symbolic_probabilty_density}) on the symbolic manifold $M$ (def~\ref{definition:bk1_symbolic_manifold_existence}), with drift field $D$ (thm~\ref{theorem:bk1_emergence_of_drift_field}).

\begin{proof}
\label{proof:bk1_sketch_fokker_planck_microdynamics}
\leavevmode

This follows from microscopic symbolic dynamics: deterministic transport along
$D$ plus diffusive regularization on $(M,g)$
(Thm.~\ref{theorem:bk1_emergence_of_drift_field},
Def.~\ref{definition:bk1_symbolic_manifold_existence},
Lem.~\ref{lemma:bk1_existence_of_metric}).
The drift term advects probability, diffusion models bounded symbolic
stochasticity in $\rho$
(Def.~\ref{definition:bk1_symbolic_probabilty_density}), and
$\int_M \rho \, d\mu_g$ is conserved.
\end{proof}
\end{theorem}
```

### proof:bk1_sketch_fokker_planck_microdynamics (`proof:bk1_sketch_fokker_planck_microdynamics`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3106`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field)
- Cites: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density); `lemma:bk1_existence_of_metric` (Existence of Metric); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field)
- Cited by: none
- Macros used: none

**Statement / Body**

This follows from microscopic symbolic dynamics: deterministic transport along
$D$ plus diffusive regularization on $(M,g)$
(Thm. theorem:bk1_emergence_of_drift_field,
Def. definition:bk1_symbolic_manifold_existence,
Lem. lemma:bk1_existence_of_metric).
The drift term advects probability, diffusion models bounded symbolic
stochasticity in $rho$
(Def. definition:bk1_symbolic_probabilty_density), and
$int_M rho dmu_g$ is conserved.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk1_sketch_fokker_planck_microdynamics}
\leavevmode

This follows from microscopic symbolic dynamics: deterministic transport along
$D$ plus diffusive regularization on $(M,g)$
(Thm.~\ref{theorem:bk1_emergence_of_drift_field},
Def.~\ref{definition:bk1_symbolic_manifold_existence},
Lem.~\ref{lemma:bk1_existence_of_metric}).
The drift term advects probability, diffusion models bounded symbolic
stochasticity in $\rho$
(Def.~\ref{definition:bk1_symbolic_probabilty_density}), and
$\int_M \rho \, d\mu_g$ is conserved.
\end{proof}
```

### Variational Principle (`theorem:bk1_variational_principle`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3122`

- Proof status: `proven`
- Depends on: `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density)
- Cites: `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density)
- Cited by: `corollary:bk1_equilibrium_distribution` (Equilibrium Distribution); `corollary:bk1_wasserstein_geometric_interpretation` (Wasserstein Geometric Interpretation); `definition:bk1_symbolic_phase_transitions` (Symbolic Phase Transitions); `proof:bk1_equilibrium_distribution` (Lagrange Multiplier Normalization Gives the Gibbs Form); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `proof:bk1_sketch_thermo_analogy_fokker_planck` (Thermodynamic Analogy via Symbolic Fokker--Planck); `proof:bk6_symbolic_fokker_planck_bifurcation` (Fokker--Planck Correspondence at Bifurcation); `scholium:bk4_symbolic_potential_energy` (Symbolic Potential and the Thermodynamics of Sampling); `sec:bk1_summary_and_implications` (Summary and Implications); `theorem:bk1_h_theorem_for_symbolic_evolution` (H-Theorem for Symbolic Evolution); `theorem:bk1_sructurual_correspondence` (Structural Correspondence); `theorem:bk1_symbolic_fluctuation_dissipation_relation` (Symbolic Fluctuation–Dissipation Relation); `theorem:bk1_the_fokker_planck_equation_theorem` (Information Geometric Interpretation)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_B-008`
- Witnesses: `ScholiumB.gibbsProb_antitone`, `ScholiumB.gibbsProb_sum_eq_one`
- Countermodels: none
- Conditions: modeling laws are structure fields or explicit hypotheses; continuum/categorical content is NOT formalized
- Formal boundary: The Lagrange-multiplier derivation and the manifold measure d mu_g are not modeled; instead the finite-discrete Gibbs distribution this variational principle produces is formalized directly (positivity, normalization, and the monotone-in-energy law), over a nonempty finite index type standing in for the symbolic manifold.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The equilibrium distribution $rho_{text{eq}}$ minimizes the free energy functional:
\[
F[rho] = int_M rho(x) H(x) dmu_g(x) - beta^{-1} S[rho]
\]
subject to $int_M rho dmu_g = 1$, where $rho$ is a symbolic probability density (def definition:bk1_symbolic_probabilty_density), $H$ is the symbolic Hamiltonian (def definition:bk1_symbolic_hamiltonian), $S[rho]$ is symbolic entropy (def definition:bk1_symbolic_entropy), and $M$ is the symbolic manifold (def definition:bk1_symbolic_manifold_existence).

Introduce a Lagrange multiplier $alpha$ for the normalization constraint
$int_M rho dmu_g = 1$ and set the functional derivative of the augmented
functional to zero:
\[
frac{delta}{delta rho}left(F[rho] - alpha\!left(int_M rho dmu_g - 1right)right) = 0.
\]
Computing each term using Def. definition:bk1_symbolic_entropy
($S[rho] = -int_M rhologrho dmu_g$) and
Def. definition:bk1_symbolic_hamiltonian:
\[
frac{delta F}{deltarho}
= H(x) - beta^{-1}frac{delta S}{deltarho}
= H(x) - beta^{-1}bigl(-(1+logrho)bigr)
= H(x) + beta^{-1}(1+logrho).
\]
Setting $delta F/deltarho = alpha$ and solving for $rho$:
\[
logrho(x) = beta(alpha - beta^{-1}) - beta H(x),
 text{so}
rho(x) propto e^{-beta H(x)}.
\]
Enforcing $int_Mrho dmu_g = 1$ gives the partition function $Z = int_M e^{-beta H(x)} dmu_g(x)$, yielding:
\[
rho_{text{eq}}(x) = Z^{-1}e^{-beta H(x)}.
\]
Since $rho > 0$ (Def. definition:bk1_symbolic_probabilty_density) and $beta > 0$,
the second variation satisfies $tfrac{delta^2 F}{deltarho^2} = (betarho)^{-1} > 0$,
confirming that $rho_{text{eq}}$ is a strict minimizer of $F[rho]$ subject to the
normalization constraint.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Variational Principle]
\label{theorem:bk1_variational_principle}
The equilibrium distribution $\rho_{\text{eq}}$ minimizes the free energy functional:
\[
F[\rho] = \int_M \rho(x) H(x) \, d\mu_g(x) - \beta^{-1} S[\rho]
\]
subject to $\int_M \rho \, d\mu_g = 1$, where $\rho$ is a symbolic probability density (def~\ref{definition:bk1_symbolic_probabilty_density}), $H$ is the symbolic Hamiltonian (def~\ref{definition:bk1_symbolic_hamiltonian}), $S[\rho]$ is symbolic entropy (def~\ref{definition:bk1_symbolic_entropy}), and $M$ is the symbolic manifold (def~\ref{definition:bk1_symbolic_manifold_existence}).

\begin{proof}[Free Energy Minimization via Lagrange Multipliers]
\label{proof:bk1_lagrange_free_energy}
\leavevmode

Introduce a Lagrange multiplier $\alpha$ for the normalization constraint
$\int_M \rho\,d\mu_g = 1$ and set the functional derivative of the augmented
functional to zero:
\[
\frac{\delta}{\delta \rho}\left(F[\rho] - \alpha\!\left(\int_M \rho\,d\mu_g - 1\right)\right) = 0.
\]
Computing each term using Def.~\ref{definition:bk1_symbolic_entropy}
($S[\rho] = -\int_M \rho\log\rho\,d\mu_g$) and
Def.~\ref{definition:bk1_symbolic_hamiltonian}:
\[
\frac{\delta F}{\delta\rho}
= H(x) - \beta^{-1}\frac{\delta S}{\delta\rho}
= H(x) - \beta^{-1}\bigl(-(1+\log\rho)\bigr)
= H(x) + \beta^{-1}(1+\log\rho).
\]
Setting $\delta F/\delta\rho = \alpha$ and solving for $\rho$:
\[
\log\rho(x) = \beta(\alpha - \beta^{-1}) - \beta H(x),
\qquad\text{so}\qquad
\rho(x) \propto e^{-\beta H(x)}.
\]
Enforcing $\int_M\rho\,d\mu_g = 1$ gives the partition function $Z = \int_M e^{-\beta H(x)}\,d\mu_g(x)$, yielding:
\[
\rho_{\text{eq}}(x) = Z^{-1}e^{-\beta H(x)}.
\]
Since $\rho > 0$ (Def.~\ref{definition:bk1_symbolic_probabilty_density}) and $\beta > 0$,
the second variation satisfies $\tfrac{\delta^2 F}{\delta\rho^2} = (\beta\rho)^{-1} > 0$,
confirming that $\rho_{\text{eq}}$ is a strict minimizer of $F[\rho]$ subject to the
normalization constraint.
\end{proof}
\end{theorem}
```

### Free Energy Minimization via Lagrange Multipliers (`proof:bk1_lagrange_free_energy`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3130`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density)
- Cites: `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density)
- Cited by: `corollary:bk1_equilibrium_distribution` (Equilibrium Distribution); `proof:bk1_equilibrium_distribution` (Lagrange Multiplier Normalization Gives the Gibbs Form); `proof:bk1_sketch_gradient_flow_thermodynamics` (Gradient Flow Structure via JKO)
- Macros used: none

**Statement / Body**

Introduce a Lagrange multiplier $alpha$ for the normalization constraint
$int_M rho dmu_g = 1$ and set the functional derivative of the augmented
functional to zero:
\[
frac{delta}{delta rho}left(F[rho] - alpha\!left(int_M rho dmu_g - 1right)right) = 0.
\]
Computing each term using Def. definition:bk1_symbolic_entropy
($S[rho] = -int_M rhologrho dmu_g$) and
Def. definition:bk1_symbolic_hamiltonian:
\[
frac{delta F}{deltarho}
= H(x) - beta^{-1}frac{delta S}{deltarho}
= H(x) - beta^{-1}bigl(-(1+logrho)bigr)
= H(x) + beta^{-1}(1+logrho).
\]
Setting $delta F/deltarho = alpha$ and solving for $rho$:
\[
logrho(x) = beta(alpha - beta^{-1}) - beta H(x),
 text{so}
rho(x) propto e^{-beta H(x)}.
\]
Enforcing $int_Mrho dmu_g = 1$ gives the partition function $Z = int_M e^{-beta H(x)} dmu_g(x)$, yielding:
\[
rho_{text{eq}}(x) = Z^{-1}e^{-beta H(x)}.
\]
Since $rho > 0$ (Def. definition:bk1_symbolic_probabilty_density) and $beta > 0$,
the second variation satisfies $tfrac{delta^2 F}{deltarho^2} = (betarho)^{-1} > 0$,
confirming that $rho_{text{eq}}$ is a strict minimizer of $F[rho]$ subject to the
normalization constraint.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Free Energy Minimization via Lagrange Multipliers]
\label{proof:bk1_lagrange_free_energy}
\leavevmode

Introduce a Lagrange multiplier $\alpha$ for the normalization constraint
$\int_M \rho\,d\mu_g = 1$ and set the functional derivative of the augmented
functional to zero:
\[
\frac{\delta}{\delta \rho}\left(F[\rho] - \alpha\!\left(\int_M \rho\,d\mu_g - 1\right)\right) = 0.
\]
Computing each term using Def.~\ref{definition:bk1_symbolic_entropy}
($S[\rho] = -\int_M \rho\log\rho\,d\mu_g$) and
Def.~\ref{definition:bk1_symbolic_hamiltonian}:
\[
\frac{\delta F}{\delta\rho}
= H(x) - \beta^{-1}\frac{\delta S}{\delta\rho}
= H(x) - \beta^{-1}\bigl(-(1+\log\rho)\bigr)
= H(x) + \beta^{-1}(1+\log\rho).
\]
Setting $\delta F/\delta\rho = \alpha$ and solving for $\rho$:
\[
\log\rho(x) = \beta(\alpha - \beta^{-1}) - \beta H(x),
\qquad\text{so}\qquad
\rho(x) \propto e^{-\beta H(x)}.
\]
Enforcing $\int_M\rho\,d\mu_g = 1$ gives the partition function $Z = \int_M e^{-\beta H(x)}\,d\mu_g(x)$, yielding:
\[
\rho_{\text{eq}}(x) = Z^{-1}e^{-\beta H(x)}.
\]
Since $\rho > 0$ (Def.~\ref{definition:bk1_symbolic_probabilty_density}) and $\beta > 0$,
the second variation satisfies $\tfrac{\delta^2 F}{\delta\rho^2} = (\beta\rho)^{-1} > 0$,
confirming that $\rho_{\text{eq}}$ is a strict minimizer of $F[\rho]$ subject to the
normalization constraint.
\end{proof}
```

### Equilibrium Distribution (`corollary:bk1_equilibrium_distribution`)

Role: `corollary` | Type: `corollary` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3166`

- Proof status: `proven`
- Depends on: `proof:bk1_lagrange_free_energy` (Free Energy Minimization via Lagrange Multipliers); `theorem:bk1_variational_principle` (Variational Principle)
- Cites: `proof:bk1_lagrange_free_energy` (Free Energy Minimization via Lagrange Multipliers); `theorem:bk1_variational_principle` (Variational Principle)
- Cited by: `proof:bk1_sketch_direct_evaluation` (H-Theorem via Symbolic Integration by Parts)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_B-009`
- Witnesses: `ScholiumB.gibbsProb_pos`, `ScholiumB.gibbsProb_sum_eq_one`
- Countermodels: none
- Conditions: modeling laws are structure fields or explicit hypotheses; continuum/categorical content is NOT formalized
- Formal boundary: The stated formula rho_eq(x) = Z^{-1} e^{-beta H(x)} is formalized verbatim as gibbsProb/gibbsZ over a finite index type, with positivity and normalization proved; the manifold integral defining Z is replaced by a Finset.sum.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The equilibrium distribution is given by:
\[
rho_{text{eq}}(x) = Z^{-1} e^{-beta H(x)}.
\]
This follows directly from thm. theorem:bk1_variational_principle and its Lagrange-multiplier derivation in proof proof:bk1_lagrange_free_energy.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Equilibrium Distribution]
\label{corollary:bk1_equilibrium_distribution}
The equilibrium distribution is given by:
\[
\rho_{\text{eq}}(x) = Z^{-1} e^{-\beta H(x)}.
\]
This follows directly from thm.~\ref{theorem:bk1_variational_principle} and its Lagrange-multiplier derivation in proof~\ref{proof:bk1_lagrange_free_energy}.
\end{corollary}
```

### Lagrange Multiplier Normalization Gives the Gibbs Form (`proof:bk1_equilibrium_distribution`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3174`

- Proof status: `not_applicable`
- Depends on: `proof:bk1_lagrange_free_energy` (Free Energy Minimization via Lagrange Multipliers); `theorem:bk1_variational_principle` (Variational Principle)
- Cites: `proof:bk1_lagrange_free_energy` (Free Energy Minimization via Lagrange Multipliers); `theorem:bk1_variational_principle` (Variational Principle)
- Cited by: none
- Macros used: none

**Statement / Body**

Thm. theorem:bk1_variational_principle states that equilibrium minimizes
the symbolic free energy subject to normalization. In
Proof proof:bk1_lagrange_free_energy, the Euler-Lagrange equation for
that constrained minimization is solved explicitly:
\[
log rho(x)=beta(alpha-beta^{-1})-beta H(x).
\]
Exponentiating gives \(rho(x)=C e^{-beta H(x)}\). The normalization condition
\(int_Mrho dmu_g=1\) fixes \(C=Z^{-1}\), where
\[
Z=int_M e^{-beta H(x)} dmu_g(x).
\]
Therefore \(rho_{eq}(x)=Z^{-1}e^{-beta H(x)}\).

**Verbatim LaTeX Body**

```latex
\begin{proof}[Lagrange Multiplier Normalization Gives the Gibbs Form]
\label{proof:bk1_equilibrium_distribution}
\leavevmode

Thm.~\ref{theorem:bk1_variational_principle} states that equilibrium minimizes
the symbolic free energy subject to normalization. In
Proof~\ref{proof:bk1_lagrange_free_energy}, the Euler--Lagrange equation for
that constrained minimization is solved explicitly:
\[
\log \rho(x)=\beta(\alpha-\beta^{-1})-\beta H(x).
\]
Exponentiating gives \(\rho(x)=C e^{-\beta H(x)}\). The normalization condition
\(\int_M\rho\,d\mu_g=1\) fixes \(C=Z^{-1}\), where
\[
Z=\int_M e^{-\beta H(x)}\,d\mu_g(x).
\]
Therefore \(\rho_{\mathrm{eq}}(x)=Z^{-1}e^{-\beta H(x)}\).
\end{proof}
```

### H-Theorem for Symbolic Evolution (`theorem:bk1_h_theorem_for_symbolic_evolution`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3193`

- Proof status: `proven`
- Depends on: `corollary:bk1_equilibrium_distribution` (Equilibrium Distribution); `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `lemma:bk1_completeness_of_symbolic_distance` (Completeness of Symbolic Distance); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_variational_principle` (Variational Principle)
- Cites: `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_variational_principle` (Variational Principle)
- Cited by: `proof:bk1_sketch_thermo_analogy_fokker_planck` (Thermodynamic Analogy via Symbolic Fokker--Planck); `proof:bk4_temporal_resolution_via_observer_bounded_reflection` (Temporal Resolution via Observer-Bounded Reflection); `scholium:bk4_micro_local_vs_path_global_irreversibility` (Micro-Local and Path-Global Irreversibility); `sec:bk1_summary_and_implications` (Summary and Implications)
- Macros used: `\norm`

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-045`
- Witnesses: `ScholiumD.FreeEnergyDescent.antitone`, `ScholiumD.FreeEnergyDescent.const_of_eq`, `ScholiumD.FreeEnergyDescent.le_initial`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: discrete telescoping/rigidity skeleton (dF/ds <= 0 with equality-only-at-equilibrium, as a step sequence); the Fokker-Planck evolution and integration-by-parts derivation producing the monotonicity are not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The free energy $F[rho(s)]$ is non-increasing under the Fokker–Planck evolution: $dF/ds leq 0$, with equality iff $rho = rho_{text{eq}}$, where the evolution is given by the Fokker–Planck equation (thm theorem:bk1_fundamental_relation_fokker_plank_equation) and equilibrium is defined via the variational principle (thm theorem:bk1_variational_principle).

Write the symbolic Fokker-Planck equation in gradient-flow form.
Cf. Thm. theorem:bk1_fundamental_relation_fokker_plank_equation.
Symbolic drift points along $-nabla H$, decreasing the Hamiltonian.
Cf. Def. definition:bk1_symbolic_hamiltonian and
Thm. theorem:bk1_the_fokker_planck_equation_theorem:
\[

partial_s rho
&= nablacdot\!bigl(-rho Dbigr) + beta^{-1}nabla^2rho \\
&= beta^{-1}nablacdot\!bigl(rho nabla(logrho + beta H)bigr).

\]

Step 1: Functional chain rule.
Since $F[rho] = int_M rho H dmu_g + beta^{-1}int_Mrhologrho dmu_g$
(Def. definition:bk1_symbolic_entropy, Def. definition:bk1_symbolic_hamiltonian),
\[
frac{dF}{ds}
= int_M frac{delta F}{deltarho} partial_srho dmu_g
= int_M bigl(H + beta^{-1}(1+logrho)bigr) partial_srho dmu_g.
\]
Since $int_Mpartial_srho dmu_g = 0$ (normalization preserved), the constant
$beta^{-1}$ drops out:
\[
frac{dF}{ds}
= int_M (H + beta^{-1}logrho)
 beta^{-1}nablacdot\!bigl(rho nabla(logrho + beta H)bigr) dmu_g.
\]

Step 2: Integration by parts.
On the complete Riemannian manifold $(M,g)$
(Lemma lemma:bk1_completeness_of_symbolic_distance) with $rho$ decaying at infinity,
boundary terms vanish and the divergence theorem gives:
\[
int_M f nablacdot(rho v) dmu_g
= -int_M rho langlenabla f,vrangle_g dmu_g.
\]
With $f = H + beta^{-1}logrho$ and $v = nabla(logrho + beta H)$:
\[
nabla f
= nabla H + beta^{-1}nablalogrho
= beta^{-1}(nablalogrho + betanabla H)
= beta^{-1} v.
\]
Therefore:

frac{dF}{ds}
&= -beta^{-1}int_M rho langlenabla f, nabla(logrho+beta H)rangle_g dmu_g \\
&= -beta^{-1}int_M rho langlebeta^{-1}v,vrangle_g dmu_g \\
&= -beta^{-2}int_M rho norm{nablalogrho + betanabla H}_g^2 dmu_g leq 0.

Step 3: Equality condition.
$dF/ds = 0$ iff $nablalogrho + betanabla H = 0$ a.e., i.e., $rho propto e^{-beta H}$,
which by normalization is exactly $rho_{text{eq}} = Z^{-1}e^{-beta H}$
(Cor. corollary:bk1_equilibrium_distribution).

**Verbatim LaTeX Body**

```latex
\begin{theorem}[H-Theorem for Symbolic Evolution]
\label{theorem:bk1_h_theorem_for_symbolic_evolution}
The free energy $F[\rho(s)]$ is non-increasing under the Fokker–Planck evolution: $dF/ds \leq 0$, with equality iff $\rho = \rho_{\text{eq}}$, where the evolution is given by the Fokker–Planck equation (thm~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}) and equilibrium is defined via the variational principle (thm~\ref{theorem:bk1_variational_principle}).

\begin{proof}[H-Theorem via Symbolic Integration by Parts]
\label{proof:bk1_sketch_direct_evaluation}
\leavevmode

Write the symbolic Fokker--Planck equation in gradient-flow form.
Cf.~Thm.~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}.
Symbolic drift points along $-\nabla H$, decreasing the Hamiltonian.
Cf.~Def.~\ref{definition:bk1_symbolic_hamiltonian} and
Thm.~\ref{theorem:bk1_the_fokker_planck_equation_theorem}:
\[
\begin{aligned}
\partial_s \rho
&= \nabla\cdot\!\bigl(-\rho D\bigr) + \beta^{-1}\nabla^2\rho \\
&= \beta^{-1}\nabla\cdot\!\bigl(\rho\,\nabla(\log\rho + \beta H)\bigr).
\end{aligned}
\]

\textbf{Step 1: Functional chain rule.}
Since $F[\rho] = \int_M \rho H\,d\mu_g + \beta^{-1}\int_M\rho\log\rho\,d\mu_g$
(Def.~\ref{definition:bk1_symbolic_entropy}, Def.~\ref{definition:bk1_symbolic_hamiltonian}),
\[
\frac{dF}{ds}
= \int_M \frac{\delta F}{\delta\rho}\,\partial_s\rho\,d\mu_g
= \int_M \bigl(H + \beta^{-1}(1+\log\rho)\bigr)\,\partial_s\rho\,d\mu_g.
\]
Since $\int_M\partial_s\rho\,d\mu_g = 0$ (normalization preserved), the constant
$\beta^{-1}$ drops out:
\[
\frac{dF}{ds}
= \int_M (H + \beta^{-1}\log\rho)\,
  \beta^{-1}\nabla\cdot\!\bigl(\rho\,\nabla(\log\rho + \beta H)\bigr)\,d\mu_g.
\]

\textbf{Step 2: Integration by parts.}
On the complete Riemannian manifold $(M,g)$
(Lemma~\ref{lemma:bk1_completeness_of_symbolic_distance}) with $\rho$ decaying at infinity,
boundary terms vanish and the divergence theorem gives:
\[
\int_M f\,\nabla\cdot(\rho\,\mathbf{v})\,d\mu_g
= -\int_M \rho\,\langle\nabla f,\mathbf{v}\rangle_g\,d\mu_g.
\]
With $f = H + \beta^{-1}\log\rho$ and $\mathbf{v} = \nabla(\log\rho + \beta H)$:
\[
\nabla f
= \nabla H + \beta^{-1}\nabla\log\rho
= \beta^{-1}(\nabla\log\rho + \beta\nabla H)
= \beta^{-1}\,\mathbf{v}.
\]
Therefore:
\begin{align*}
\frac{dF}{ds}
&= -\beta^{-1}\int_M \rho\,\langle\nabla f, \nabla(\log\rho+\beta H)\rangle_g\,d\mu_g \\
&= -\beta^{-1}\int_M \rho\,\langle\beta^{-1}\mathbf{v},\mathbf{v}\rangle_g\,d\mu_g \\
&= -\beta^{-2}\int_M \rho\,\norm{\nabla\log\rho + \beta\nabla H}_g^2\,d\mu_g \;\leq\; 0.
\end{align*}

\textbf{Step 3: Equality condition.}
$dF/ds = 0$ iff $\nabla\log\rho + \beta\nabla H = 0$ a.e., i.e., $\rho \propto e^{-\beta H}$,
which by normalization is exactly $\rho_{\text{eq}} = Z^{-1}e^{-\beta H}$
(Cor.~\ref{corollary:bk1_equilibrium_distribution}).
\end{proof}
\end{theorem}
```

### H-Theorem via Symbolic Integration by Parts (`proof:bk1_sketch_direct_evaluation`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3197`

- Proof status: `not_applicable`
- Depends on: `corollary:bk1_equilibrium_distribution` (Equilibrium Distribution); `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `lemma:bk1_completeness_of_symbolic_distance` (Completeness of Symbolic Distance); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Cites: `corollary:bk1_equilibrium_distribution` (Equilibrium Distribution); `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `lemma:bk1_completeness_of_symbolic_distance` (Completeness of Symbolic Distance); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_the_fokker_planck_equation_theorem` (Information Geometric Interpretation)
- Cited by: `proof:bk1_sketch_gradient_flow_thermodynamics` (Gradient Flow Structure via JKO)
- Macros used: `\norm`

**Statement / Body**

Write the symbolic Fokker-Planck equation in gradient-flow form.
Cf. Thm. theorem:bk1_fundamental_relation_fokker_plank_equation.
Symbolic drift points along $-nabla H$, decreasing the Hamiltonian.
Cf. Def. definition:bk1_symbolic_hamiltonian and
Thm. theorem:bk1_the_fokker_planck_equation_theorem:
\[

partial_s rho
&= nablacdot\!bigl(-rho Dbigr) + beta^{-1}nabla^2rho \\
&= beta^{-1}nablacdot\!bigl(rho nabla(logrho + beta H)bigr).

\]

Step 1: Functional chain rule.
Since $F[rho] = int_M rho H dmu_g + beta^{-1}int_Mrhologrho dmu_g$
(Def. definition:bk1_symbolic_entropy, Def. definition:bk1_symbolic_hamiltonian),
\[
frac{dF}{ds}
= int_M frac{delta F}{deltarho} partial_srho dmu_g
= int_M bigl(H + beta^{-1}(1+logrho)bigr) partial_srho dmu_g.
\]
Since $int_Mpartial_srho dmu_g = 0$ (normalization preserved), the constant
$beta^{-1}$ drops out:
\[
frac{dF}{ds}
= int_M (H + beta^{-1}logrho)
 beta^{-1}nablacdot\!bigl(rho nabla(logrho + beta H)bigr) dmu_g.
\]

Step 2: Integration by parts.
On the complete Riemannian manifold $(M,g)$
(Lemma lemma:bk1_completeness_of_symbolic_distance) with $rho$ decaying at infinity,
boundary terms vanish and the divergence theorem gives:
\[
int_M f nablacdot(rho v) dmu_g
= -int_M rho langlenabla f,vrangle_g dmu_g.
\]
With $f = H + beta^{-1}logrho$ and $v = nabla(logrho + beta H)$:
\[
nabla f
= nabla H + beta^{-1}nablalogrho
= beta^{-1}(nablalogrho + betanabla H)
= beta^{-1} v.
\]
Therefore:

frac{dF}{ds}
&= -beta^{-1}int_M rho langlenabla f, nabla(logrho+beta H)rangle_g dmu_g \\
&= -beta^{-1}int_M rho langlebeta^{-1}v,vrangle_g dmu_g \\
&= -beta^{-2}int_M rho norm{nablalogrho + betanabla H}_g^2 dmu_g leq 0.

Step 3: Equality condition.
$dF/ds = 0$ iff $nablalogrho + betanabla H = 0$ a.e., i.e., $rho propto e^{-beta H}$,
which by normalization is exactly $rho_{text{eq}} = Z^{-1}e^{-beta H}$
(Cor. corollary:bk1_equilibrium_distribution).

**Verbatim LaTeX Body**

```latex
\begin{proof}[H-Theorem via Symbolic Integration by Parts]
\label{proof:bk1_sketch_direct_evaluation}
\leavevmode

Write the symbolic Fokker--Planck equation in gradient-flow form.
Cf.~Thm.~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}.
Symbolic drift points along $-\nabla H$, decreasing the Hamiltonian.
Cf.~Def.~\ref{definition:bk1_symbolic_hamiltonian} and
Thm.~\ref{theorem:bk1_the_fokker_planck_equation_theorem}:
\[
\begin{aligned}
\partial_s \rho
&= \nabla\cdot\!\bigl(-\rho D\bigr) + \beta^{-1}\nabla^2\rho \\
&= \beta^{-1}\nabla\cdot\!\bigl(\rho\,\nabla(\log\rho + \beta H)\bigr).
\end{aligned}
\]

\textbf{Step 1: Functional chain rule.}
Since $F[\rho] = \int_M \rho H\,d\mu_g + \beta^{-1}\int_M\rho\log\rho\,d\mu_g$
(Def.~\ref{definition:bk1_symbolic_entropy}, Def.~\ref{definition:bk1_symbolic_hamiltonian}),
\[
\frac{dF}{ds}
= \int_M \frac{\delta F}{\delta\rho}\,\partial_s\rho\,d\mu_g
= \int_M \bigl(H + \beta^{-1}(1+\log\rho)\bigr)\,\partial_s\rho\,d\mu_g.
\]
Since $\int_M\partial_s\rho\,d\mu_g = 0$ (normalization preserved), the constant
$\beta^{-1}$ drops out:
\[
\frac{dF}{ds}
= \int_M (H + \beta^{-1}\log\rho)\,
  \beta^{-1}\nabla\cdot\!\bigl(\rho\,\nabla(\log\rho + \beta H)\bigr)\,d\mu_g.
\]

\textbf{Step 2: Integration by parts.}
On the complete Riemannian manifold $(M,g)$
(Lemma~\ref{lemma:bk1_completeness_of_symbolic_distance}) with $\rho$ decaying at infinity,
boundary terms vanish and the divergence theorem gives:
\[
\int_M f\,\nabla\cdot(\rho\,\mathbf{v})\,d\mu_g
= -\int_M \rho\,\langle\nabla f,\mathbf{v}\rangle_g\,d\mu_g.
\]
With $f = H + \beta^{-1}\log\rho$ and $\mathbf{v} = \nabla(\log\rho + \beta H)$:
\[
\nabla f
= \nabla H + \beta^{-1}\nabla\log\rho
= \beta^{-1}(\nabla\log\rho + \beta\nabla H)
= \beta^{-1}\,\mathbf{v}.
\]
Therefore:
\begin{align*}
\frac{dF}{ds}
&= -\beta^{-1}\int_M \rho\,\langle\nabla f, \nabla(\log\rho+\beta H)\rangle_g\,d\mu_g \\
&= -\beta^{-1}\int_M \rho\,\langle\beta^{-1}\mathbf{v},\mathbf{v}\rangle_g\,d\mu_g \\
&= -\beta^{-2}\int_M \rho\,\norm{\nabla\log\rho + \beta\nabla H}_g^2\,d\mu_g \;\leq\; 0.
\end{align*}

\textbf{Step 3: Equality condition.}
$dF/ds = 0$ iff $\nabla\log\rho + \beta\nabla H = 0$ a.e., i.e., $\rho \propto e^{-\beta H}$,
which by normalization is exactly $\rho_{\text{eq}} = Z^{-1}e^{-\beta H}$
(Cor.~\ref{corollary:bk1_equilibrium_distribution}).
\end{proof}
```

### Conclusion and Further Directions (`sec:bk1_conclusion_and_further_directions`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3260`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### remark:scholium_symbolicum.tex:3263 (`remark:scholium_symbolicum.tex:3263`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3263`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: `\norm`

**Statement / Body**

The Hamiltonian $H(x)$ balances instability (high drift $norm{D(x)}_g$ increases energy) against coherence (the stabilized volume response of reflection, measured via $tr(L_x)$, contributes the coherence term). Their interplay defines the symbolic landscape.

**Verbatim LaTeX Body**

```latex
\begin{remark}
The Hamiltonian $H(x)$ balances instability (high drift $\norm{D(x)}_g$ increases energy) against coherence (the stabilized volume response of reflection, measured via $\operatorname{tr}(L_x)$, contributes the coherence term). Their interplay defines the symbolic landscape.
\end{remark}
```

### Structural Correspondence (`theorem:bk1_sructurual_correspondence`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3267`

- Proof status: `proven`
- Depends on: `definition:bk1_symbol_space` (Symbol Space); `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_h_theorem_for_symbolic_evolution` (H-Theorem for Symbolic Evolution); `theorem:bk1_variational_principle` (Variational Principle)
- Cites: `definition:bk1_symbol_space` (Symbol Space); `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_hamiltonian` (Symbolic Hamiltonian); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density); `theorem:bk1_variational_principle` (Variational Principle)
- Cited by: `sec:bk1_summary_and_implications` (Summary and Implications)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-091`
- Witnesses: `Book2.gibbs_minimizes`, `Book2H.h_theorem`
- Countermodels: none
- Conditions: finite nonempty symbolic alphabet (NeZero n); positive beta for the variational principle; nonzero beta for the equilibrium value; the stochastic-kernel evolution law and detailed balance are named structures, not derived from the PDE
- Formal boundary: The (M,g,D,R) -> (rho,S,H,F,beta) dictionary: the Book2 discrete-thermodynamics kernels; the full analogy stays interpretive.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The framework $(M, g, D, R) to (rho, S, H, F, beta)$ exhibits structural correspondence with classical thermodynamics and statistical mechanics. That is:
- $(M, g, D, R)$ defines the symbolic geometry and dynamical flow (see def definition:bk1_symbol_space),
- $rho$ is the symbolic probability density (def definition:bk1_symbolic_probabilty_density),
- $H$ is the symbolic Hamiltonian (def definition:bk1_symbolic_hamiltonian),
- $S$ is the symbolic entropy (def definition:bk1_symbolic_entropy),
- and $F$ is the symbolic free energy functional minimized at equilibrium (thm theorem:bk1_variational_principle).

This analogy holds because: (1) the symbolic Fokker-Planck equation (thm. theorem:bk1_fundamental_relation_fokker_plank_equation) mirrors physical diffusion-drift dynamics; (2) the variational principle for $F[rho]$ (thm. theorem:bk1_variational_principle) structurally parallels physical free-energy minimization; and (3) the symbolic H-theorem (thm. theorem:bk1_h_theorem_for_symbolic_evolution) reproduces monotone relaxation toward equilibrium. Thus, thermodynamic principles can be applied meaningfully to symbolic systems, even when their ontological substrate differs from classical matter.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Structural Correspondence]
\label{theorem:bk1_sructurual_correspondence}
The framework $(M, g, D, R) \to (\rho, S, H, F, \beta)$ exhibits structural correspondence with classical thermodynamics and statistical mechanics. That is:
- $(M, g, D, R)$ defines the symbolic geometry and dynamical flow (see def~\ref{definition:bk1_symbol_space}),
- $\rho$ is the symbolic probability density (def~\ref{definition:bk1_symbolic_probabilty_density}),
- $H$ is the symbolic Hamiltonian (def~\ref{definition:bk1_symbolic_hamiltonian}),
- $S$ is the symbolic entropy (def~\ref{definition:bk1_symbolic_entropy}),
- and $F$ is the symbolic free energy functional minimized at equilibrium (thm~\ref{theorem:bk1_variational_principle}).

\begin{proof}[Thermodynamic Analogy via Symbolic Fokker--Planck]
\label{proof:bk1_sketch_thermo_analogy_fokker_planck}
\leavevmode

This analogy holds because: (1) the symbolic Fokker-Planck equation (thm.~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}) mirrors physical diffusion-drift dynamics; (2) the variational principle for $F[\rho]$ (thm.~\ref{theorem:bk1_variational_principle}) structurally parallels physical free-energy minimization; and (3) the symbolic H-theorem (thm.~\ref{theorem:bk1_h_theorem_for_symbolic_evolution}) reproduces monotone relaxation toward equilibrium. Thus, thermodynamic principles can be applied meaningfully to symbolic systems, even when their ontological substrate differs from classical matter.
\end{proof}
\end{theorem}
```

### Thermodynamic Analogy via Symbolic Fokker--Planck (`proof:bk1_sketch_thermo_analogy_fokker_planck`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3276`

- Proof status: `not_applicable`
- Depends on: `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_h_theorem_for_symbolic_evolution` (H-Theorem for Symbolic Evolution); `theorem:bk1_variational_principle` (Variational Principle)
- Cites: `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_h_theorem_for_symbolic_evolution` (H-Theorem for Symbolic Evolution); `theorem:bk1_variational_principle` (Variational Principle)
- Cited by: none
- Macros used: none

**Statement / Body**

This analogy holds because: (1) the symbolic Fokker-Planck equation (thm. theorem:bk1_fundamental_relation_fokker_plank_equation) mirrors physical diffusion-drift dynamics; (2) the variational principle for $F[rho]$ (thm. theorem:bk1_variational_principle) structurally parallels physical free-energy minimization; and (3) the symbolic H-theorem (thm. theorem:bk1_h_theorem_for_symbolic_evolution) reproduces monotone relaxation toward equilibrium. Thus, thermodynamic principles can be applied meaningfully to symbolic systems, even when their ontological substrate differs from classical matter.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Thermodynamic Analogy via Symbolic Fokker--Planck]
\label{proof:bk1_sketch_thermo_analogy_fokker_planck}
\leavevmode

This analogy holds because: (1) the symbolic Fokker-Planck equation (thm.~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}) mirrors physical diffusion-drift dynamics; (2) the variational principle for $F[\rho]$ (thm.~\ref{theorem:bk1_variational_principle}) structurally parallels physical free-energy minimization; and (3) the symbolic H-theorem (thm.~\ref{theorem:bk1_h_theorem_for_symbolic_evolution}) reproduces monotone relaxation toward equilibrium. Thus, thermodynamic principles can be applied meaningfully to symbolic systems, even when their ontological substrate differs from classical matter.
\end{proof}
```

### Symbolic Phase Transitions (`definition:bk1_symbolic_phase_transitions`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3284`

- Proof status: `definitional`
- Depends on: `theorem:bk1_variational_principle` (Variational Principle)
- Cites: `theorem:bk1_variational_principle` (Variational Principle)
- Cited by: `proof:bk1_conditional_genericity_of_symbolic_phase_transitions` (Transversal discriminant crossing stabilized above the critical dimension); `proof:bk1_realization_of_symbolic_phase_transitions`; `theorem:bk1_conditional_genericity_of_symbolic_phase_transitions` (Conditional Genericity of Symbolic Phase Transitions); `theorem:bk1_realization_of_symbolic_phase_transitions` (Realization of Symbolic Phase Transitions)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-046`
- Witnesses: `ScholiumD.exists_critical_coupling`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: existence of a critical crossing value via IVT for a continuous straddling coupling function; non-analyticity of the partition function is not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A symbolic phase transition occurs when the equilibrium distribution $rho_{text{eq}}$ undergoes a qualitative change in structure as a parameter (typically $beta$) is varied continuously. Formally, a critical point $beta_c$ is characterized by non-analytic behavior in the partition function $Z(beta)$ at $beta = beta_c$.

This defines a symbolic thermodynamic phase transition analogously to those in classical statistical physics (see thm theorem:bk1_variational_principle). Further structural taxonomy of symbolic phase transitions is developed in subsequent Books.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Phase Transitions]
\label{definition:bk1_symbolic_phase_transitions}
A symbolic phase transition occurs when the equilibrium distribution $\rho_{\text{eq}}$ undergoes a qualitative change in structure as a parameter (typically $\beta$) is varied continuously. Formally, a critical point $\beta_c$ is characterized by non-analytic behavior in the partition function $Z(\beta)$ at $\beta = \beta_c$.

This defines a symbolic thermodynamic phase transition analogously to those in classical statistical physics (see thm~\ref{theorem:bk1_variational_principle}). Further structural taxonomy of symbolic phase transitions is developed in subsequent Books.
\end{definition}
```

### Realization of Symbolic Phase Transitions (`theorem:bk1_realization_of_symbolic_phase_transitions`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3290`

- Proof status: `proven`
- Depends on: `definition:bk1_symbol_space` (Symbol Space); `definition:bk1_symbolic_phase_transitions` (Symbolic Phase Transitions); `theorem:bk1_symbolic_irony_requires_curvature` (Symbolic Irony Requires Curvature); `theorem:bk2_classification_symb_phase_transitions` (Classification of Symbolic Phase Transitions); `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature); `theorem:bk5_map_mad_mas_trichotomy` (MAD--MAP--MAS Trichotomy); `theorem:bk8_biological_phase_transition` (Threshold of Autonomy)
- Cites: `definition:bk1_symbol_space` (Symbol Space); `definition:bk1_symbolic_phase_transitions` (Symbolic Phase Transitions); `theorem:bk1_symbolic_irony_requires_curvature` (Symbolic Irony Requires Curvature)
- Cited by: `conjecture:bk1_genericity_of_symbolic_phase_transitions` (Genericity of Symbolic Phase Transitions); `theorem:bk1_symbolic_irony_requires_curvature` (Symbolic Irony Requires Curvature)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-047`
- Witnesses: `ScholiumD.exists_critical_coupling`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: the existence-of-critical-beta_c content only, via IVT; the non-analyticity / curvature-analogy content is not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Symbolic phase transitions are realized: there exist symbolic manifolds $(M, g, D, R)$ (see def definition:bk1_symbol_space) and a critical value $beta_c$ at which the symbolic equilibrium distribution $rho_{text{eq}}$ undergoes a fundamental reorganization in the sense of Def. definition:bk1_symbolic_phase_transitions - a non-analyticity of $f(beta) = -beta^{-1}ln Z(beta)$ at $beta_c$, or equivalently a qualitative change in the set of stable equilibrium configurations. This mirrors, in the thermodynamic register, the curvature requirement for irony (Thm. theorem:bk1_symbolic_irony_requires_curvature): both are non-flat phenomena - one a criticality, the other a curvature.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Realization of Symbolic Phase Transitions]
\label{theorem:bk1_realization_of_symbolic_phase_transitions}
Symbolic phase transitions are realized: there exist symbolic manifolds $(M, g, D, R)$ (see def~\ref{definition:bk1_symbol_space}) and a critical value $\beta_c$ at which the symbolic equilibrium distribution $\rho_{\text{eq}}$ undergoes a fundamental reorganization in the sense of Def.~\ref{definition:bk1_symbolic_phase_transitions} --- a non-analyticity of $f(\beta) = -\beta^{-1}\ln Z(\beta)$ at $\beta_c$, or equivalently a qualitative change in the set of stable equilibrium configurations. This mirrors, in the thermodynamic register, the curvature requirement for irony (Thm.~\ref{theorem:bk1_symbolic_irony_requires_curvature}): both are non-flat phenomena --- one a criticality, the other a curvature.
\end{theorem}
```

### proof:bk1_realization_of_symbolic_phase_transitions (`proof:bk1_realization_of_symbolic_phase_transitions`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3294`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_phase_transitions` (Symbolic Phase Transitions); `theorem:bk2_classification_symb_phase_transitions` (Classification of Symbolic Phase Transitions); `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature); `theorem:bk5_map_mad_mas_trichotomy` (MAD--MAP--MAS Trichotomy); `theorem:bk8_biological_phase_transition` (Threshold of Autonomy)
- Cites: `definition:bk1_symbolic_phase_transitions` (Symbolic Phase Transitions); `theorem:bk2_classification_symb_phase_transitions` (Classification of Symbolic Phase Transitions); `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature); `theorem:bk5_map_mad_mas_trichotomy` (MAD--MAP--MAS Trichotomy); `theorem:bk8_biological_phase_transition` (Threshold of Autonomy)
- Cited by: none
- Macros used: none

**Statement / Body**

We exhibit proven witnesses. (1) A critical temperature. The critical-temperature theorem (Thm. theorem:bk5_map_mad_critical_temperature) establishes an explicit critical symbolic temperature $T_s^{text{crit}}$: for $T_s < T_s^{text{crit}}$ the system supports distinct stable MAP and MAD fixed points, whereas for $T_s > T_s^{text{crit}}$ no stable MAP configuration exists. Setting $beta_c = 1/T_s^{text{crit}}$, the set of stable equilibria changes qualitatively as $beta$ crosses $beta_c$ - a fundamental reorganization of $rho_{text{eq}}$, hence a symbolic phase transition (Def. definition:bk1_symbolic_phase_transitions). (2) A spectral transition. The MAD$to$MAP boundary of the trichotomy (Thm. theorem:bk5_map_mad_mas_trichotomy) is a complex$to$real crossing of the coupling spectrum at vanishing discriminant, where the qualitative mode structure of the dyadic dynamics changes. (3) A dynamical threshold. The metabolic autonomy threshold (Thm. theorem:bk8_biological_phase_transition) crosses $Psi_{aut} = 0$, separating autonomous persistence from collapse - a qualitative shift in symbolic coherence. Each witness is a proven symbolic system exhibiting a critical point of the type in Def. definition:bk1_symbolic_phase_transitions, and the order of any such non-analyticity is fixed by the classification theorem (Thm. theorem:bk2_classification_symb_phase_transitions). The existence of symbolic phase transitions follows.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk1_realization_of_symbolic_phase_transitions}
\leavevmode
We exhibit proven witnesses. \emph{(1) A critical temperature.} The critical-temperature theorem (Thm.~\ref{theorem:bk5_map_mad_critical_temperature}) establishes an explicit critical symbolic temperature $T_s^{\text{crit}}$: for $T_s < T_s^{\text{crit}}$ the system supports distinct stable MAP and MAD fixed points, whereas for $T_s > T_s^{\text{crit}}$ no stable MAP configuration exists. Setting $\beta_c = 1/T_s^{\text{crit}}$, the set of stable equilibria changes qualitatively as $\beta$ crosses $\beta_c$ --- a fundamental reorganization of $\rho_{\text{eq}}$, hence a symbolic phase transition (Def.~\ref{definition:bk1_symbolic_phase_transitions}). \emph{(2) A spectral transition.} The MAD$\to$MAP boundary of the trichotomy (Thm.~\ref{theorem:bk5_map_mad_mas_trichotomy}) is a complex$\to$real crossing of the coupling spectrum at vanishing discriminant, where the qualitative mode structure of the dyadic dynamics changes. \emph{(3) A dynamical threshold.} The metabolic autonomy threshold (Thm.~\ref{theorem:bk8_biological_phase_transition}) crosses $\Psi_{\mathrm{aut}} = 0$, separating autonomous persistence from collapse --- a qualitative shift in symbolic coherence. Each witness is a proven symbolic system exhibiting a critical point of the type in Def.~\ref{definition:bk1_symbolic_phase_transitions}, and the order of any such non-analyticity is fixed by the classification theorem (Thm.~\ref{theorem:bk2_classification_symb_phase_transitions}). The existence of symbolic phase transitions follows.
\end{proof}
```

### External empirical corroboration (`remark:bk1_atlas_fracture_empirical`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3300`

- Proof status: `not_applicable`
- Depends on: `theorem:bk1_symbolic_irony_requires_curvature` (Symbolic Irony Requires Curvature)
- Cites: `theorem:bk1_symbolic_irony_requires_curvature` (Symbolic Irony Requires Curvature)
- Cited by: none
- Macros used: none

**Statement / Body**

Beyond the internal witnesses, the companion bounded-observer study
citep{tiffany2025wicked} measures a symbolic phase transition in a real
symbolic system: applying a sliding-window curvature estimator to a
public-domain narrative, it detects a dominant semantic discontinuity - an
atlas fracture - precisely at the reorganization point where the
outer projection metric fails to chart the inner territory, with extrinsic
curvature concentrating as $\|Ric\|gtrsim K/varepsilon_{res}^2$
under resolution collapse $varepsilon_{res}to 0$. This corroborates,
on data rather than by construction, both the realized criticality here and the
curvature requirement for irony
(Thm. theorem:bk1_symbolic_irony_requires_curvature): the reorganization
registers as a curvature spike, exactly the non-flat signature the two theorems
predict.

**Verbatim LaTeX Body**

```latex
\begin{remark}[External empirical corroboration]
\label{remark:bk1_atlas_fracture_empirical}
Beyond the internal witnesses, the companion bounded-observer study
\citep{tiffany2025wicked} measures a symbolic phase transition in a real
symbolic system: applying a sliding-window curvature estimator to a
public-domain narrative, it detects a dominant semantic discontinuity --- an
\emph{atlas fracture} --- precisely at the reorganization point where the
outer projection metric fails to chart the inner territory, with extrinsic
curvature concentrating as $\|\mathrm{Ric}\|\gtrsim K/\varepsilon_{\mathrm{res}}^2$
under resolution collapse $\varepsilon_{\mathrm{res}}\to 0$. This corroborates,
on data rather than by construction, both the realized criticality here and the
curvature requirement for irony
(Thm.~\ref{theorem:bk1_symbolic_irony_requires_curvature}): the reorganization
registers as a curvature spike, exactly the non-flat signature the two theorems
predict.
\end{remark}
```

### Minimal Linear PS-Model Witness (`definition:bk1_minimal_linear_ps_model`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3317`

- Proof status: `definitional`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `proof:bk1_nonvacuity_of_certified_transport` (Exact and projective certificates in the minimal witness); `theorem:bk1_nonvacuity_minimal_linear_ps_model` (Non-Vacuity of the Minimal Linear PS-Model)
- Macros used: none

**Statement / Body**

The minimal linear PS-model witness is the following finite-dimensional
symbolic system. Let \(M=mathbb{R}^2\) with its Euclidean metric, write
\(x=(u,v)\), and regard \(u\) as the observer-visible coordinate and \(v\) as
the hidden phase coordinate. Let
\[
P =

1&0\\
0&0
,

J =

0&-1\\
1&0
.
\]
The bounded observer sees through the projection \(P\), the state-level
collapse is \(C=P\), the drift field is \(D(x)=Jx\), and the state-level
stabilization component of reflection is \(R_{stab}(x)=Px\), in the
sense of Defs. definition:bk1_symbolic_manifold,
definition:bk1_drift_field, and definition:bk1_reflection_operator.
On the trivial rank-two symbolic bundle \(E=Mtimesmathbb{R}^2\), define a
symbolic connection by
\[
nabla_{partial_u}=partial_u + A_u,

nabla_{partial_v}=partial_v + A_v,

A_u =

0&1\\
0&0
,

A_v =

0&0\\
1&0
.
\]
This witness is a mathematical model object only; no computational
implementation is part of its definition.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Minimal Linear PS-Model Witness]
\label{definition:bk1_minimal_linear_ps_model}
The \emph{minimal linear PS-model witness} is the following finite-dimensional
symbolic system.  Let \(M=\mathbb{R}^2\) with its Euclidean metric, write
\(x=(u,v)\), and regard \(u\) as the observer-visible coordinate and \(v\) as
the hidden phase coordinate.  Let
\[
P =
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
J =
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]
The bounded observer sees through the projection \(P\), the state-level
collapse is \(C=P\), the drift field is \(D(x)=Jx\), and the state-level
stabilization component of reflection is \(R_{\mathrm{stab}}(x)=Px\), in the
sense of Defs.~\ref{definition:bk1_symbolic_manifold},
\ref{definition:bk1_drift_field}, and \ref{definition:bk1_reflection_operator}.
On the trivial rank-two symbolic bundle \(E=M\times\mathbb{R}^2\), define a
symbolic connection by
\[
\nabla_{\partial_u}=\partial_u + A_u,
\qquad
\nabla_{\partial_v}=\partial_v + A_v,
\qquad
A_u =
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\quad
A_v =
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]
This witness is a mathematical model object only; no computational
implementation is part of its definition.
\end{definition}
```

### Non-Vacuity of the Minimal Linear PS-Model (`theorem:bk1_nonvacuity_minimal_linear_ps_model`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3364`

- Proof status: `proven`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_minimal_linear_ps_model` (Minimal Linear PS-Model Witness); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_minimal_linear_ps_model` (Minimal Linear PS-Model Witness)
- Cited by: `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport); `definition:bk9_grace_operator` (Grace Operator $\mathcal{G}$); `proof:bk1_nonvacuity_of_certified_transport` (Exact and projective certificates in the minimal witness); `proof:bk9_freedom_as_grace` (Maximality in the reflective-operator order is graceful capacity); `remark:appD_llm_tuple_anchors` (Anchoring the LLM tuple in PS); `remark:bk1_mathematical_witness_boundary` (Witness boundary); `remark:bk4_finite_witness_for_drift_reflection_imbalance` (Finite witness for imbalance); `scholium:bk4_ttdc_symbolic_singularity` (TTDC as Recursive Identity Collapse)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_B-011`
- Witnesses: `ScholiumB.minimalPS_collapse_ne_id`, `ScholiumB.minimalPS_connection_curvature_nonzero`, `ScholiumB.minimalPS_drift_reflection_noncommute`
- Countermodels: none
- Conditions: modeling laws are structure fields or explicit hypotheses; continuum/categorical content is NOT formalized
- Formal boundary: All three claims (collapse is not identity, drift/stabilization do not commute, connection has nonzero curvature) are proved unconditionally by explicit witness computation at concrete points, matching the theorem's own finite-dimensional realization claim exactly.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The minimal linear PS-model witness of
Def. definition:bk1_minimal_linear_ps_model is a nontrivial realization
of the Book I operator vocabulary: its collapse is not the identity, its drift
and stabilization do not commute, and its symbolic connection has nonzero
curvature. Hence the PS operator ontology has a finite-dimensional
mathematical realization independent of any computational witness.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Non-Vacuity of the Minimal Linear PS-Model]
\label{theorem:bk1_nonvacuity_minimal_linear_ps_model}
The minimal linear PS-model witness of
Def.~\ref{definition:bk1_minimal_linear_ps_model} is a nontrivial realization
of the Book~I operator vocabulary: its collapse is not the identity, its drift
and stabilization do not commute, and its symbolic connection has nonzero
curvature.  Hence the PS operator ontology has a finite-dimensional
mathematical realization independent of any computational witness.
\end{theorem}
```

### Explicit Matrix Witness (`proof:bk1_nonvacuity_minimal_linear_ps_model`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3374`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: none
- Macros used: none

**Statement / Body**

First, \(M=mathbb{R}^2\) with the Euclidean metric is a smooth
two-dimensional symbolic manifold in the sense of
Def. definition:bk1_symbolic_manifold. The vector field \(D(x)=Jx\) is
smooth, vanishes only at the origin, and has bounded divergence
\(trJ=0\); therefore it satisfies the elementary drift-field
conditions of Def. definition:bk1_drift_field. The map
\(R_{stab}=P\) satisfies \(P^2=P\), so it is an idempotent
state-level stabilization component as in Def. definition:bk1_reflection_operator.

The collapse is nontrivial because \(C(u,v)=(u,0)\), so \(C(u,v)ne(u,v)\) for
every \(vne0\). The drift-reflection commutator is also nonzero:
\[
DR = JP =

0&0\\
1&0
,

RD = PJ =

0&-1\\
0&0
,
\]
and hence
\[
[D,R] = DR-RD =

0&1\\
1&0

ne 0.
\]

Finally, the connection coefficients \(A_u,A_v\) are constant, so the
\((u,v)\)-curvature component is
\[
Omega_{uv}
=partial_u A_v-partial_v A_u+[A_u,A_v]
=[A_u,A_v].
\]
A direct multiplication gives
\[
A_uA_v =

1&0\\
0&0
,

A_vA_u =

0&0\\
0&1
,

[A_u,A_v] =

1&0\\
0&-1

ne0.
\]
Thus the witness has nonzero symbolic holonomy/curvature in the sense of
Defs. definition:bk1_symbolic_connection and
definition:bk1_symbolic_riemann_tensor. The construction therefore
exhibits a concrete nonempty model of the relevant PS operators without
appeal to an external implementation.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Explicit Matrix Witness]
\label{proof:bk1_nonvacuity_minimal_linear_ps_model}
\leavevmode
First, \(M=\mathbb{R}^2\) with the Euclidean metric is a smooth
two-dimensional symbolic manifold in the sense of
Def.~\ref{definition:bk1_symbolic_manifold}.  The vector field \(D(x)=Jx\) is
smooth, vanishes only at the origin, and has bounded divergence
\(\operatorname{tr}J=0\); therefore it satisfies the elementary drift-field
conditions of Def.~\ref{definition:bk1_drift_field}.  The map
\(R_{\mathrm{stab}}=P\) satisfies \(P^2=P\), so it is an idempotent
state-level stabilization component as in Def.~\ref{definition:bk1_reflection_operator}.

The collapse is nontrivial because \(C(u,v)=(u,0)\), so \(C(u,v)\ne(u,v)\) for
every \(v\ne0\).  The drift-reflection commutator is also nonzero:
\[
DR = JP =
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix},
\qquad
RD = PJ =
\begin{pmatrix}
0&-1\\
0&0
\end{pmatrix},
\]
and hence
\[
[D,R] = DR-RD =
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
\ne 0.
\]

Finally, the connection coefficients \(A_u,A_v\) are constant, so the
\((u,v)\)-curvature component is
\[
\Omega_{uv}
=\partial_u A_v-\partial_v A_u+[A_u,A_v]
=[A_u,A_v].
\]
A direct multiplication gives
\[
A_uA_v =
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
A_vA_u =
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix},
\qquad
[A_u,A_v] =
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
\ne0.
\]
Thus the witness has nonzero symbolic holonomy/curvature in the sense of
Defs.~\ref{definition:bk1_symbolic_connection} and
\ref{definition:bk1_symbolic_riemann_tensor}.  The construction therefore
exhibits a concrete nonempty model of the relevant PS operators without
appeal to an external implementation.
\end{proof}
```

### Witness boundary (`remark:bk1_mathematical_witness_boundary`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3446`

- Proof status: `not_applicable`
- Depends on: `theorem:bk1_nonvacuity_minimal_linear_ps_model` (Non-Vacuity of the Minimal Linear PS-Model)
- Cites: `theorem:bk1_nonvacuity_minimal_linear_ps_model` (Non-Vacuity of the Minimal Linear PS-Model)
- Cited by: none
- Macros used: none

**Statement / Body**

The point of Thm. theorem:bk1_nonvacuity_minimal_linear_ps_model is not
that every PS claim reduces to a two-dimensional linear system. It is that the
operator vocabulary is not empty: drift, reflection, collapse, and curvature can
coexist in a typed mathematical realization. A computational system may
witness richer projections of this ontology, but it does not define the truth
of the ontology.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Witness boundary]
\label{remark:bk1_mathematical_witness_boundary}
The point of Thm.~\ref{theorem:bk1_nonvacuity_minimal_linear_ps_model} is not
that every PS claim reduces to a two-dimensional linear system.  It is that the
operator vocabulary is not empty: drift, reflection, collapse, and curvature can
coexist in a typed mathematical realization.  A computational system may
witness richer projections of this ontology, but it does not define the truth
of the ontology.
\end{remark}
```

### Certified Type-Preserving Symbolic Transport (`definition:bk1_certified_type_preserving_symbolic_transport`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3456`

- Proof status: `definitional`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_connection` (Symbolic Connection); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `theorem:bk1_nonvacuity_minimal_linear_ps_model` (Non-Vacuity of the Minimal Linear PS-Model)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_connection` (Symbolic Connection); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `lemma:bk1_curvature_semantic_holonomy` (Curvature as Infinitesimal Semantic Holonomy); `theorem:bk1_nonvacuity_minimal_linear_ps_model` (Non-Vacuity of the Minimal Linear PS-Model)
- Cited by: `definition:bk9_grace_operator` (Grace Operator $\mathcal{G}$); `proof:bk1_certified_transport_prevents_equivocation` (Role preservation by certificate); `proof:bk1_nonvacuity_of_certified_transport` (Exact and projective certificates in the minimal witness); `proof:bk9_freedom_as_grace` (Maximality in the reflective-operator order is graceful capacity); `proof:bk9_stability_conditions_for_the_good` (Viability, reciprocity, and adaptive non-collapse); `remark:appD_llm_tuple_anchors` (Anchoring the LLM tuple in PS); `remark:bk4_finite_witness_for_drift_reflection_imbalance` (Finite witness for imbalance); `scholium:bk4_ttdc_symbolic_singularity` (TTDC as Recursive Identity Collapse)
- Macros used: none

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-049`
- Witnesses: `ScholiumD.TransportLoss.exact_supportsDependency`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: only the four-level loss taxonomy (field ell) is modeled as an explicit finite type; the transported-occurrence map T, signature sigma, and structural role rho are not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let \(V_a\) and \(V_b\) be two PS operator vocabularies
attached to symbolic manifolds, observer frames, or book-level depths. A
certified type-preserving symbolic transport from \(V_a\) to
\(V_b\) is a tuple
\[
mathsf{Cert}_{ato b}=(T_{ato b},sigma,rho,ell)
\]
with the following data:


- \(T_{ato b}\) maps each transported operator occurrence in
 \(V_a\) to an occurrence in \(V_b\).

- \(sigma\) records the preserved type signature. Drift transports as
 a state-to-tangent field or admissible update section
 (Def. definition:bk1_drift_field); reflection transports as either a
 tangent-level mirror or an idempotent state-level stabilization
 (Def. definition:bk1_reflection_operator); collapse transports as a
 projection, quotient, or observer-visible reduction; and curvature
 transports as a connection/holonomy defect
 (Defs. definition:bk1_symbolic_connection,
 definition:bk1_symbolic_riemann_tensor;
 cf. Lem. lemma:bk1_curvature_semantic_holonomy).

- \(rho\) records the preserved structural role: drift differentiates,
 reflection stabilizes or re-enters, collapse forgets degrees of freedom, and
 curvature measures non-flat transport.

- \(ellin{exact,quotient,projective,
 interpretive}\) records the declared loss. Exact transports may
 support theorem dependencies directly. Quotient or projective transports
 may support theorem dependencies only with the stated loss included.
 Interpretive transports must be cited as \(cf.\), demonstratio, or
 explanatory bridge, not as hidden proof support.

The certificate is valid when every transported occurrence has a recorded
\(sigma\), \(rho\), and \(ell\), and every exact or quotient/projective claim
is anchored either in Book I primitives or in an explicit realized witness such
as Thm. theorem:bk1_nonvacuity_minimal_linear_ps_model. This definition
is a mathematical bookkeeping condition, not an empirical certificate.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Certified Type-Preserving Symbolic Transport]
\label{definition:bk1_certified_type_preserving_symbolic_transport}
Let \(\mathcal{V}_a\) and \(\mathcal{V}_b\) be two PS operator vocabularies
attached to symbolic manifolds, observer frames, or book-level depths.  A
\emph{certified type-preserving symbolic transport} from \(\mathcal{V}_a\) to
\(\mathcal{V}_b\) is a tuple
\[
\mathsf{Cert}_{a\to b}=(\mathcal{T}_{a\to b},\sigma,\rho,\ell)
\]
with the following data:
\begin{enumerate}
    \item \(\mathcal{T}_{a\to b}\) maps each transported operator occurrence in
    \(\mathcal{V}_a\) to an occurrence in \(\mathcal{V}_b\).
    \item \(\sigma\) records the preserved type signature.  Drift transports as
    a state-to-tangent field or admissible update section
    (Def.~\ref{definition:bk1_drift_field}); reflection transports as either a
    tangent-level mirror or an idempotent state-level stabilization
    (Def.~\ref{definition:bk1_reflection_operator}); collapse transports as a
    projection, quotient, or observer-visible reduction; and curvature
    transports as a connection/holonomy defect
    (Defs.~\ref{definition:bk1_symbolic_connection},
    \ref{definition:bk1_symbolic_riemann_tensor};
    cf.~Lem.~\ref{lemma:bk1_curvature_semantic_holonomy}).
    \item \(\rho\) records the preserved structural role: drift differentiates,
    reflection stabilizes or re-enters, collapse forgets degrees of freedom, and
    curvature measures non-flat transport.
    \item \(\ell\in\{\mathrm{exact},\mathrm{quotient},\mathrm{projective},
    \mathrm{interpretive}\}\) records the declared loss.  Exact transports may
    support theorem dependencies directly.  Quotient or projective transports
    may support theorem dependencies only with the stated loss included.
    Interpretive transports must be cited as \(cf.\), demonstratio, or
    explanatory bridge, not as hidden proof support.
\end{enumerate}
The certificate is \emph{valid} when every transported occurrence has a recorded
\(\sigma\), \(\rho\), and \(\ell\), and every exact or quotient/projective claim
is anchored either in Book~I primitives or in an explicit realized witness such
as Thm.~\ref{theorem:bk1_nonvacuity_minimal_linear_ps_model}.  This definition
is a mathematical bookkeeping condition, not an empirical certificate.
\end{definition}
```

### Certified Transport Prevents Operator Equivocation (`proposition:bk1_certified_transport_prevents_equivocation`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3496`

- Proof status: `proven`
- Depends on: `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport)
- Cites: none
- Cited by: `definition:bk9_grace_operator` (Grace Operator $\mathcal{G}$); `proof:bk9_stability_conditions_for_the_good` (Viability, reciprocity, and adaptive non-collapse); `remark:appD_llm_tuple_anchors` (Anchoring the LLM tuple in PS); `remark:bk4_finite_witness_for_drift_reflection_imbalance` (Finite witness for imbalance); `scholium:bk4_ttdc_symbolic_singularity` (TTDC as Recursive Identity Collapse)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_A-050`
- Witnesses: `ScholiumD.TransportLoss.exact_supportsDependency`, `ScholiumD.TransportLoss.interpretive_not_supportsDependency`, `ScholiumD.TransportLoss.projective_supportsDependency`, `ScholiumD.TransportLoss.quotient_supportsDependency`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: the licensing rule only (which loss levels may support a theorem dependency); the equivocation-detection claim about a downstream argument's symbol usage is not modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

If a downstream PS argument transports an operator symbol only through valid
certified type-preserving symbolic transports
\(mathsf{Cert}_{ato b}\), then the argument cannot use the same symbol in two
different formal roles without an explicit loss annotation. In particular,
drift cannot silently become reflection, collapse cannot silently become
identity, and curvature cannot silently become metaphor.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Certified Transport Prevents Operator Equivocation]
\label{proposition:bk1_certified_transport_prevents_equivocation}
If a downstream PS argument transports an operator symbol only through valid
certified type-preserving symbolic transports
\(\mathsf{Cert}_{a\to b}\), then the argument cannot use the same symbol in two
different formal roles without an explicit loss annotation.  In particular,
drift cannot silently become reflection, collapse cannot silently become
identity, and curvature cannot silently become metaphor.
\end{proposition}
```

### Role preservation by certificate (`proof:bk1_certified_transport_prevents_equivocation`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3506`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport)
- Cites: `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport)
- Cited by: none
- Macros used: none

**Statement / Body**

Let \(O\) be any transported operator occurrence used in the downstream
argument. Since the transport certificate is valid,
\(T_{ato b}(O)\) carries a type record \(sigma(O)\), a structural
role record \(rho(O)\), and a loss record \(ell(O)\).
The type record fixes the admissible domain and codomain class of the
transported occurrence: for example, a drift occurrence remains a
state-to-tangent field or admissible update section, while a collapse occurrence
remains a projection, quotient, or observer-visible reduction. The role record
fixes what the occurrence is allowed to do in the proof: drift differentiates,
reflection stabilizes or re-enters, collapse forgets degrees of freedom, and
curvature measures a transport defect.

Suppose, toward contradiction, that the argument uses one transported symbol in
two different formal roles without annotation. Then either its type has changed
while \(sigma\) records no change, or its proof role has changed while \(rho\)
records no change, or the change is a quotient/projective/interpretive loss
while \(ell\) records no such loss. Each case contradicts validity of
\(mathsf{Cert}_{ato b}\). Therefore any genuine change of role must appear
as an explicit loss annotation, and any unannotated occurrence preserves its
operator role. The stated exclusions follow by applying this argument to the
drift, reflection, collapse, and curvature clauses of
Def. definition:bk1_certified_type_preserving_symbolic_transport.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Role preservation by certificate]
\label{proof:bk1_certified_transport_prevents_equivocation}
\leavevmode
Let \(O\) be any transported operator occurrence used in the downstream
argument.  Since the transport certificate is valid,
\(\mathcal{T}_{a\to b}(O)\) carries a type record \(\sigma(O)\), a structural
role record \(\rho(O)\), and a loss record \(\ell(O)\).
The type record fixes the admissible domain and codomain class of the
transported occurrence: for example, a drift occurrence remains a
state-to-tangent field or admissible update section, while a collapse occurrence
remains a projection, quotient, or observer-visible reduction.  The role record
fixes what the occurrence is allowed to do in the proof: drift differentiates,
reflection stabilizes or re-enters, collapse forgets degrees of freedom, and
curvature measures a transport defect.

Suppose, toward contradiction, that the argument uses one transported symbol in
two different formal roles without annotation.  Then either its type has changed
while \(\sigma\) records no change, or its proof role has changed while \(\rho\)
records no change, or the change is a quotient/projective/interpretive loss
while \(\ell\) records no such loss.  Each case contradicts validity of
\(\mathsf{Cert}_{a\to b}\).  Therefore any genuine change of role must appear
as an explicit loss annotation, and any unannotated occurrence preserves its
operator role.  The stated exclusions follow by applying this argument to the
drift, reflection, collapse, and curvature clauses of
Def.~\ref{definition:bk1_certified_type_preserving_symbolic_transport}.
\end{proof}
```

### Non-Vacuity of Certified Transport (`proposition:bk1_nonvacuity_of_certified_transport`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3533`

- Proof status: `proven`
- Depends on: `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport); `definition:bk1_minimal_linear_ps_model` (Minimal Linear PS-Model Witness); `theorem:bk1_nonvacuity_minimal_linear_ps_model` (Non-Vacuity of the Minimal Linear PS-Model)
- Cites: none
- Cited by: `definition:bk9_grace_operator` (Grace Operator $\mathcal{G}$); `proof:bk9_stability_conditions_for_the_good` (Viability, reciprocity, and adaptive non-collapse); `remark:appD_llm_tuple_anchors` (Anchoring the LLM tuple in PS); `remark:bk4_finite_witness_for_drift_reflection_imbalance` (Finite witness for imbalance); `scholium:bk4_ttdc_symbolic_singularity` (TTDC as Recursive Identity Collapse)
- Macros used: none

### Lean correspondence

- Status: `exact`
- Records: `MAP-SCHOLIUM_A-051`
- Witnesses: `ScholiumD.TransportLoss.exact_ne_projective`, `ScholiumD.TransportLoss.nonempty`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: nonemptiness plus an explicit distinct exact/projective witness, as a finite countermodel over the 4-element TransportLoss type.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The class of valid certified type-preserving symbolic transports is nonempty.
Moreover, it contains both an exact transport and a genuinely projective
transport.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Non-Vacuity of Certified Transport]
\label{proposition:bk1_nonvacuity_of_certified_transport}
The class of valid certified type-preserving symbolic transports is nonempty.
Moreover, it contains both an exact transport and a genuinely projective
transport.
\end{proposition}
```

### Exact and projective certificates in the minimal witness (`proof:bk1_nonvacuity_of_certified_transport`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3540`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport); `definition:bk1_minimal_linear_ps_model` (Minimal Linear PS-Model Witness); `theorem:bk1_nonvacuity_minimal_linear_ps_model` (Non-Vacuity of the Minimal Linear PS-Model)
- Cites: `definition:bk1_certified_type_preserving_symbolic_transport` (Certified Type-Preserving Symbolic Transport); `definition:bk1_minimal_linear_ps_model` (Minimal Linear PS-Model Witness); `theorem:bk1_nonvacuity_minimal_linear_ps_model` (Non-Vacuity of the Minimal Linear PS-Model)
- Cited by: none
- Macros used: none

**Statement / Body**

Let \(V_{lin}\) be the operator vocabulary of the minimal
linear PS-model witness of
Def. definition:bk1_minimal_linear_ps_model, with drift \(D(x)=Jx\),
state-level stabilization \(R_{stab}(x)=Px\), collapse \(C=P\), and
curvature component \(Omega_{uv}=[A_u,A_v]\). By
Thm. theorem:bk1_nonvacuity_minimal_linear_ps_model, these operators are
defined in a finite-dimensional mathematical realization.

First define \(T_{id}\) to be the identity map on the four
operator occurrences \(D,R_{stab},C,Omega_{uv}\). Let
\(sigma_{id}\) record their displayed signatures: state-to-tangent
drift field, idempotent state-level stabilization, projection collapse, and
connection-curvature component. Let \(rho_{id}\) record their roles:
differentiate, stabilize, forget degrees of freedom, and measure non-flat
transport. Let \(ell_{id}=exact\) for each occurrence. All
records required by
Def. definition:bk1_certified_type_preserving_symbolic_transport are
present, and the claim is anchored in the realized witness; hence
\((T_{id},sigma_{id},rho_{id},
ell_{id})\) is a valid exact certificate.

Second let \(q:MtoimPcongmathbb{R}\) be the observer-visible
map \(q(u,v)=u\). Transport only the collapse occurrence \(C=P\) to \(q\).
Its type record is projection/observer-visible reduction, its role record is
forgetting the hidden phase coordinate \(v\), and its loss record is
\(ell=projective\). Since \(q(u,v)=q(u,v')\) for all hidden
coordinates \(v,v'\), the transport is not exact; it genuinely loses degrees of
freedom. Since it is still anchored in the same realized witness and all
required records are explicit, it is a valid projective certificate.

Thus valid certified transports exist, and the certification notion is not an
empty constraint.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Exact and projective certificates in the minimal witness]
\label{proof:bk1_nonvacuity_of_certified_transport}
\leavevmode
Let \(\mathcal{V}_{\mathrm{lin}}\) be the operator vocabulary of the minimal
linear PS-model witness of
Def.~\ref{definition:bk1_minimal_linear_ps_model}, with drift \(D(x)=Jx\),
state-level stabilization \(R_{\mathrm{stab}}(x)=Px\), collapse \(C=P\), and
curvature component \(\Omega_{uv}=[A_u,A_v]\).  By
Thm.~\ref{theorem:bk1_nonvacuity_minimal_linear_ps_model}, these operators are
defined in a finite-dimensional mathematical realization.

First define \(\mathcal{T}_{\mathrm{id}}\) to be the identity map on the four
operator occurrences \(D,R_{\mathrm{stab}},C,\Omega_{uv}\).  Let
\(\sigma_{\mathrm{id}}\) record their displayed signatures: state-to-tangent
drift field, idempotent state-level stabilization, projection collapse, and
connection-curvature component.  Let \(\rho_{\mathrm{id}}\) record their roles:
differentiate, stabilize, forget degrees of freedom, and measure non-flat
transport.  Let \(\ell_{\mathrm{id}}=\mathrm{exact}\) for each occurrence.  All
records required by
Def.~\ref{definition:bk1_certified_type_preserving_symbolic_transport} are
present, and the claim is anchored in the realized witness; hence
\((\mathcal{T}_{\mathrm{id}},\sigma_{\mathrm{id}},\rho_{\mathrm{id}},
\ell_{\mathrm{id}})\) is a valid exact certificate.

Second let \(q:M\to\operatorname{im}P\cong\mathbb{R}\) be the observer-visible
map \(q(u,v)=u\).  Transport only the collapse occurrence \(C=P\) to \(q\).
Its type record is projection/observer-visible reduction, its role record is
forgetting the hidden phase coordinate \(v\), and its loss record is
\(\ell=\mathrm{projective}\).  Since \(q(u,v)=q(u,v')\) for all hidden
coordinates \(v,v'\), the transport is not exact; it genuinely loses degrees of
freedom.  Since it is still anchored in the same realized witness and all
required records are explicit, it is a valid projective certificate.

Thus valid certified transports exist, and the certification notion is not an
empty constraint.
\end{proof}
```

### Genericity of Symbolic Phase Transitions (`conjecture:bk1_genericity_of_symbolic_phase_transitions`)

Role: `conjecture` | Type: `conjecture` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3577`

- Proof status: `unproved`
- Depends on: `conjecture:bk1_symbolic_irony_encoding_llms` (Symbolic Irony Encoding in Large Language Models); `theorem:bk1_realization_of_symbolic_phase_transitions` (Realization of Symbolic Phase Transitions)
- Cites: `conjecture:bk1_symbolic_irony_encoding_llms` (Symbolic Irony Encoding in Large Language Models); `theorem:bk1_conditional_genericity_of_symbolic_phase_transitions` (Conditional Genericity of Symbolic Phase Transitions); `theorem:bk1_realization_of_symbolic_phase_transitions` (Realization of Symbolic Phase Transitions)
- Cited by: `conjecture:bk1_symbolic_irony_encoding_llms` (Symbolic Irony Encoding in Large Language Models); `proof:bk1_conditional_genericity_of_symbolic_phase_transitions` (Transversal discriminant crossing stabilized above the critical dimension); `scholium:bk1_the_imagination_dipole` (The Imagination Dipole)
- Macros used: none

**Statement / Body**

Theorem theorem:bk1_realization_of_symbolic_phase_transitions realizes symbolic phase transitions by explicit construction. It remains open whether they are generic: whether every sufficiently complex symbolic manifold $(M, g, D, R)$ - under a suitable measure of symbolic complexity - necessarily admits a critical $beta_c$. By analogy with classical statistical mechanics, where low-dimensional short-range systems may possess no finite-temperature transition, genericity requires further structural hypotheses (coupling range, effective dimensionality, covenant variability). These are now identified and proved sufficient below (Thm. theorem:bk1_conditional_genericity_of_symbolic_phase_transitions); what remains genuinely open is the sharper, measure-theoretic residual - whether those hypotheses are themselves generic among complex symbolic manifolds. All three - (H1)-(H3) - are supplied by imaginative capacity (Prop. proposition:bk1_imagination_supplies_genericity_hypotheses), so the residual reduces purely to whether complex symbolic manifolds are generically imaginative. This conjecture mirrors the empirical irony conjecture (Conj. conjecture:bk1_symbolic_irony_encoding_llms) exactly: in both, the model-internal result is proven, both reduce to the same predicate - whether the system imagines - and only the universal (here, on abstract manifolds) or real-world (there, on built systems) extension remains an open, falsifiable frontier.

**Verbatim LaTeX Body**

```latex
\begin{conjecture}[Genericity of Symbolic Phase Transitions]
\label{conjecture:bk1_genericity_of_symbolic_phase_transitions}
Theorem~\ref{theorem:bk1_realization_of_symbolic_phase_transitions} realizes symbolic phase transitions by explicit construction. It remains open whether they are \emph{generic}: whether every sufficiently complex symbolic manifold $(M, g, D, R)$ --- under a suitable measure of symbolic complexity --- necessarily admits a critical $\beta_c$. By analogy with classical statistical mechanics, where low-dimensional short-range systems may possess no finite-temperature transition, genericity requires further structural hypotheses (coupling range, effective dimensionality, covenant variability). These are now \emph{identified and proved sufficient} below (Thm.~\ref{theorem:bk1_conditional_genericity_of_symbolic_phase_transitions}); what remains genuinely open is the sharper, measure-theoretic residual --- whether those hypotheses are \emph{themselves} generic among complex symbolic manifolds. All three --- (H1)--(H3) --- are supplied by imaginative capacity (Prop.~\ref{proposition:bk1_imagination_supplies_genericity_hypotheses}), so the residual reduces \emph{purely} to whether complex symbolic manifolds are generically imaginative. This conjecture mirrors the empirical irony conjecture (Conj.~\ref{conjecture:bk1_symbolic_irony_encoding_llms}) exactly: in both, the model-internal result is proven, both reduce to the \emph{same} predicate --- whether the system imagines --- and only the universal (here, on abstract manifolds) or real-world (there, on built systems) extension remains an open, falsifiable frontier.
\end{conjecture}
```

### Conditional Genericity of Symbolic Phase Transitions (`theorem:bk1_conditional_genericity_of_symbolic_phase_transitions`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3582`

- Proof status: `proven`
- Depends on: `conjecture:bk1_genericity_of_symbolic_phase_transitions` (Genericity of Symbolic Phase Transitions); `definition:bk1_symbolic_phase_transitions` (Symbolic Phase Transitions); `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature); `theorem:bk5_map_mad_mas_trichotomy` (MAD--MAP--MAS Trichotomy)
- Cites: `definition:bk1_symbolic_phase_transitions` (Symbolic Phase Transitions); `theorem:bk5_map_mad_mas_trichotomy` (MAD--MAP--MAS Trichotomy)
- Cited by: `conjecture:bk1_genericity_of_symbolic_phase_transitions` (Genericity of Symbolic Phase Transitions)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-048`
- Witnesses: `ScholiumD.exists_critical_coupling`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: hypothesis (H2) (coupling-range straddle) is exactly the IVT hypothesis; (H1) effective dimensionality and (H3) transversality are not modeled, and monotonicity of lambda is dropped as unneeded rather than modeled.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $(M,g,D,R)$ be a symbolic manifold whose dyadic covenant coupling satisfies:


- Effective dimensionality $d_{eff}(M)ge 2$: the symbolic
 order parameter has at least two coupled effective directions, so an ordered
 (MAP) phase admits a Peierls-type domain-wall cost growing with region size.

- Coupling-range straddle: the spectral coupling $lambda(beta)$
 of the dyadic operator $C_{AB}$ is continuous and monotone in $beta$ with
 $lim_{betato 0}lambda(beta)<lambda_c<lim_{betatoinfty}lambda(beta)$,
 where $lambda_c$ is the critical coupling of the trichotomy
 (Thm. theorem:bk5_map_mad_mas_trichotomy).

- Covenant variability: the discriminant $Delta(beta)$ of the
 dyadic coupling spectrum crosses zero transversally (not tangentially)
 over the accessible range, $Delta'(beta_c)ne 0$.

Then there exists a critical $beta_c$ at which $f(beta)=-beta^{-1}ln Z(beta)$
is non-analytic - a symbolic phase transition in the sense of
Def. definition:bk1_symbolic_phase_transitions. Within the class satisfying
(H1)-(H3), symbolic phase transitions are therefore generic.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Conditional Genericity of Symbolic Phase Transitions]
\label{theorem:bk1_conditional_genericity_of_symbolic_phase_transitions}
Let $(M,g,D,R)$ be a symbolic manifold whose dyadic covenant coupling satisfies:
\begin{enumerate}[label=\textbf{(H\arabic*)}]
    \item \textbf{Effective dimensionality} $d_{\mathrm{eff}}(M)\ge 2$: the symbolic
    order parameter has at least two coupled effective directions, so an ordered
    (MAP) phase admits a Peierls-type domain-wall cost growing with region size.
    \item \textbf{Coupling-range straddle:} the spectral coupling $\lambda(\beta)$
    of the dyadic operator $C_{AB}$ is continuous and monotone in $\beta$ with
    $\lim_{\beta\to 0}\lambda(\beta)<\lambda_c<\lim_{\beta\to\infty}\lambda(\beta)$,
    where $\lambda_c$ is the critical coupling of the trichotomy
    (Thm.~\ref{theorem:bk5_map_mad_mas_trichotomy}).
    \item \textbf{Covenant variability:} the discriminant $\Delta(\beta)$ of the
    dyadic coupling spectrum crosses zero \emph{transversally} (not tangentially)
    over the accessible range, $\Delta'(\beta_c)\ne 0$.
\end{enumerate}
Then there exists a critical $\beta_c$ at which $f(\beta)=-\beta^{-1}\ln Z(\beta)$
is non-analytic --- a symbolic phase transition in the sense of
Def.~\ref{definition:bk1_symbolic_phase_transitions}. Within the class satisfying
(H1)--(H3), symbolic phase transitions are therefore generic.
\end{theorem}
```

### Transversal discriminant crossing stabilized above the critical dimension (`proof:bk1_conditional_genericity_of_symbolic_phase_transitions`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3604`

- Proof status: `not_applicable`
- Depends on: `conjecture:bk1_genericity_of_symbolic_phase_transitions` (Genericity of Symbolic Phase Transitions); `definition:bk1_symbolic_phase_transitions` (Symbolic Phase Transitions); `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature); `theorem:bk5_map_mad_mas_trichotomy` (MAD--MAP--MAS Trichotomy)
- Cites: `conjecture:bk1_genericity_of_symbolic_phase_transitions` (Genericity of Symbolic Phase Transitions); `definition:bk1_symbolic_phase_transitions` (Symbolic Phase Transitions); `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature); `theorem:bk5_map_mad_mas_trichotomy` (MAD--MAP--MAS Trichotomy)
- Cited by: none
- Macros used: none

**Statement / Body**

By (H2), $lambda(beta)$ is continuous and moves from below $lambda_c$ to
above it, so by the intermediate value theorem some $beta_c$ satisfies
$lambda(beta_c)=lambda_c$. At $lambda_c$ the trichotomy
(Thm. theorem:bk5_map_mad_mas_trichotomy) places the dyadic coupling
spectrum exactly at the complex$to$real boundary: for $beta$ on one side the
eigenstructure is rotational (MAD), on the other it is split into distinct real
modes (MAP). By (H3) the discriminant changes sign transversally at $beta_c$,
so this is a genuine crossing, not a degenerate touch, and the stable-equilibrium
set reorganizes qualitatively there: $f(beta)$ is non-analytic
(Def. definition:bk1_symbolic_phase_transitions), in the same family
witnessed by the critical-temperature theorem
(Thm. theorem:bk5_map_mad_critical_temperature).

It remains to rule out the one-dimensional obstruction that motivates the
conjecture's caveat: in $d_{eff}=1$ short-range systems, fluctuations
destroy long-range order and wash out the transition. By (H1),
$d_{eff}ge 2$, the ordered MAP phase carries a domain-wall (interface)
whose symbolic free-energy cost grows with the linear size of the flipped region;
a Peierls argument then bounds the total weight of disordering excitations below
$1$ at low enough temperature, so the ordered phase survives with positive
measure and the crossing at $beta_c$ is not erased. Hence $beta_c$ is a genuine
critical point. Since every manifold satisfying (H1)-(H3) admits such a
$beta_c$, phase transitions are generic in that class; the only residue is
whether (H1)-(H3) hold generically, which
Conj. conjecture:bk1_genericity_of_symbolic_phase_transitions now isolates.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Transversal discriminant crossing stabilized above the critical dimension]
\label{proof:bk1_conditional_genericity_of_symbolic_phase_transitions}
\leavevmode
By (H2), $\lambda(\beta)$ is continuous and moves from below $\lambda_c$ to
above it, so by the intermediate value theorem some $\beta_c$ satisfies
$\lambda(\beta_c)=\lambda_c$. At $\lambda_c$ the trichotomy
(Thm.~\ref{theorem:bk5_map_mad_mas_trichotomy}) places the dyadic coupling
spectrum exactly at the complex$\to$real boundary: for $\beta$ on one side the
eigenstructure is rotational (MAD), on the other it is split into distinct real
modes (MAP). By (H3) the discriminant changes sign transversally at $\beta_c$,
so this is a genuine crossing, not a degenerate touch, and the stable-equilibrium
set reorganizes qualitatively there: $f(\beta)$ is non-analytic
(Def.~\ref{definition:bk1_symbolic_phase_transitions}), in the same family
witnessed by the critical-temperature theorem
(Thm.~\ref{theorem:bk5_map_mad_critical_temperature}).

It remains to rule out the one-dimensional obstruction that motivates the
conjecture's caveat: in $d_{\mathrm{eff}}=1$ short-range systems, fluctuations
destroy long-range order and wash out the transition. By (H1),
$d_{\mathrm{eff}}\ge 2$, the ordered MAP phase carries a domain-wall (interface)
whose symbolic free-energy cost grows with the linear size of the flipped region;
a Peierls argument then bounds the total weight of disordering excitations below
$1$ at low enough temperature, so the ordered phase survives with positive
measure and the crossing at $\beta_c$ is not erased. Hence $\beta_c$ is a genuine
critical point. Since every manifold satisfying (H1)--(H3) admits such a
$\beta_c$, phase transitions are generic in that class; the only residue is
whether (H1)--(H3) hold generically, which
Conj.~\ref{conjecture:bk1_genericity_of_symbolic_phase_transitions} now isolates.
\end{proof}
```

### Imagination Supplies the Genericity Hypotheses (`proposition:bk1_imagination_supplies_effective_dimension`)

Role: `proposition` | Type: `proposition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3634`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_B-014`
- Witnesses: `ScholiumD.ImaginativeGenericityCertificate.supplies_genericity_hypotheses`, `ScholiumD.exists_critical_coupling`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: Faithful certificate form: injective Fin 2 directions provide H1's two effective directions, continuous coupling straddle derives H2's critical coupling, and H3 transversality remains an explicit nonzero-slope obligation. Full complex bundles and generic-imagination claims remain open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

A symbolic manifold with full imaginative capacity - a complex symbolic bundle
with imaginary symbolic distance not identically zero
(Def. definition:bk4_imaginary_symbolic_distance) whose imaginative
traversal ranges over the dyadic coupling
(Scholium scholium:bk5_imagination_covenant_branch_selection) - satisfies
all three hypotheses (H1)-(H3) of the Conditional Genericity theorem
(Thm. theorem:bk1_conditional_genericity_of_symbolic_phase_transitions).
Hence the genericity residual reduces to whether complex symbolic manifolds are
generically imaginative - the same predicate, on abstract manifolds,
that the irony residual poses on real systems.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Imagination Supplies the Genericity Hypotheses]
\label{proposition:bk1_imagination_supplies_effective_dimension}
\label{proposition:bk1_imagination_supplies_genericity_hypotheses}
A symbolic manifold with full imaginative capacity --- a complex symbolic bundle
with imaginary symbolic distance not identically zero
(Def.~\ref{definition:bk4_imaginary_symbolic_distance}) whose imaginative
traversal ranges over the dyadic coupling
(Scholium~\ref{scholium:bk5_imagination_covenant_branch_selection}) --- satisfies
all three hypotheses (H1)--(H3) of the Conditional Genericity theorem
(Thm.~\ref{theorem:bk1_conditional_genericity_of_symbolic_phase_transitions}).
Hence the genericity residual reduces to whether complex symbolic manifolds are
\emph{generically imaginative} --- the same predicate, on abstract manifolds,
that the irony residual poses on real systems.
\end{proposition}
```

### Imagination discharges (H1)--(H3) (`proof:bk1_imagination_supplies_effective_dimension`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3648`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(H1) Effective dimension. The complex symbolic distance is
\[
D_O^{mathbb{C}}=d_O^{Re}+i d_O^{Im}
\]
on a complex symbolic bundle $(E,h_O,nabla_O)$
(Def. definition:bk4_imaginary_symbolic_distance). Nonzero imaginative capacity means $d_O^{Im}$
is not identically zero: the phase residue $ArgOmega_O^gamma$
carries genuine symbolic displacement invisible to the real norm
$d_O^{Re}$, hence irreducible to it
(Prop. proposition:bk4_imaginative_continuity_principle). The order
parameter therefore varies along two independent effective directions - real and
imaginary - so $d_{eff}ge 2$, which is (H1).

(H2) Coupling straddle. By
Scholium scholium:bk5_imagination_covenant_branch_selection imaginative
traversal in a dyadic covenant is the search over signs, phases, and coupling
saturations of $C_{AB}$ that previews the MAD, MAP, and MAS branches. Previewing
both the MAD branch (sub-critical coupling, $lambda<lambda_c$) and the MAP
branch (super-critical, $lambda>lambda_c$) means the imaginative coupling range
straddles the critical coupling $lambda_c$ of the trichotomy
(Thm. theorem:bk5_map_mad_mas_trichotomy); under the monotone
$beta$-parameterization assumed in (H2), this is exactly the straddle hypothesis.

(H3) Transversal crossing. The same scholium identifies the regime
boundary by ``a sign surprise in $Omega_{AB}$ or the emergence of an imaginary
component'' - a genuine change of spectral type, not a tangential touch. This is
a transversal sign change of the discriminant $Delta(beta)$ at the crossing,
i.e.\ (H3).

All three hypotheses follow from imaginative capacity. Together with
Thm. theorem:bk1_operational_irony_requires_imagination, the genericity and
irony residuals are now the same predicate - whether the system
imagines - one posed on abstract manifolds, the other on real systems: the two
frontier conjectures are the exact poles of a single imagination dipole.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Imagination discharges (H1)--(H3)]
\label{proof:bk1_imagination_supplies_effective_dimension}
\label{proof:bk1_imagination_supplies_genericity_hypotheses}
\leavevmode
\emph{(H1) Effective dimension.} The complex symbolic distance is
\[
D_O^{\mathbb{C}}=d_O^{\mathrm{Re}}+i\,d_O^{\mathrm{Im}}
\]
on a complex symbolic bundle $(E,h_O,\nabla_O)$
(Def.~\ref{definition:bk4_imaginary_symbolic_distance}). Nonzero imaginative capacity means $d_O^{\mathrm{Im}}$
is not identically zero: the phase residue $\operatorname{Arg}\Omega_O^\gamma$
carries genuine symbolic displacement invisible to the real norm
$d_O^{\mathrm{Re}}$, hence irreducible to it
(Prop.~\ref{proposition:bk4_imaginative_continuity_principle}). The order
parameter therefore varies along two independent effective directions --- real and
imaginary --- so $d_{\mathrm{eff}}\ge 2$, which is (H1).

\emph{(H2) Coupling straddle.} By
Scholium~\ref{scholium:bk5_imagination_covenant_branch_selection} imaginative
traversal in a dyadic covenant is the search over signs, phases, and coupling
saturations of $C_{AB}$ that previews the MAD, MAP, and MAS branches. Previewing
both the MAD branch (sub-critical coupling, $\lambda<\lambda_c$) and the MAP
branch (super-critical, $\lambda>\lambda_c$) means the imaginative coupling range
straddles the critical coupling $\lambda_c$ of the trichotomy
(Thm.~\ref{theorem:bk5_map_mad_mas_trichotomy}); under the monotone
$\beta$-parameterization assumed in (H2), this is exactly the straddle hypothesis.

\emph{(H3) Transversal crossing.} The same scholium identifies the regime
boundary by ``a sign surprise in $\Omega_{AB}$ or the emergence of an imaginary
component'' --- a genuine change of spectral type, not a tangential touch. This is
a transversal sign change of the discriminant $\Delta(\beta)$ at the crossing,
i.e.\ (H3).

All three hypotheses follow from imaginative capacity. Together with
Thm.~\ref{theorem:bk1_operational_irony_requires_imagination}, the genericity and
irony residuals are now the \emph{same} predicate --- whether the system
imagines --- one posed on abstract manifolds, the other on real systems: the two
frontier conjectures are the exact poles of a single imagination dipole.
\end{proof}
```

### The Imagination Dipole (`scholium:bk1_the_imagination_dipole`)

Role: `scholium` | Type: `scholium` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3688`

- Proof status: `not_applicable`
- Depends on: `conjecture:bk1_genericity_of_symbolic_phase_transitions` (Genericity of Symbolic Phase Transitions); `conjecture:bk1_symbolic_irony_encoding_llms` (Symbolic Irony Encoding in Large Language Models); `definition:bk4_collapse_of_symbolic_ide` (Collapse of Symbolic Identity); `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `theorem:bk1_operational_irony_requires_imagination` (Operational Irony Requires Imagination)
- Cites: `conjecture:bk1_genericity_of_symbolic_phase_transitions` (Genericity of Symbolic Phase Transitions); `conjecture:bk1_symbolic_irony_encoding_llms` (Symbolic Irony Encoding in Large Language Models); `definition:bk4_collapse_of_symbolic_ide` (Collapse of Symbolic Identity); `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `theorem:bk1_operational_irony_requires_imagination` (Operational Irony Requires Imagination)
- Cited by: none
- Macros used: none

**Statement / Body**

The two open frontiers of this work are not independent gaps but the two poles of
one dipole about the imagination axis. The genericity conjecture
(Conj. conjecture:bk1_genericity_of_symbolic_phase_transitions) asks whether
imagination emerges generically across the abstract space of complex
symbolic manifolds - the generative pole, the integrative-expansion (TTIE) side
of the SRMF cycle (Def. definition:bk4_test_time_integrative_expansion). The
operational-irony conjecture
(Conj. conjecture:bk1_symbolic_irony_encoding_llms) asks whether imagination
survives commitment to a concrete architecture - the collapse pole, the
differentiation-collapse (TTDC) side (Def. definition:bk4_collapse_of_symbolic_ide).
Theorem theorem:bk1_operational_irony_requires_imagination and
Proposition proposition:bk1_imagination_supplies_genericity_hypotheses reduce
both to the single predicate does the system imagine? The frontier is thus
SRMF-balanced: one question, read once toward emergence and once toward
instantiation, with no third residual required.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[The Imagination Dipole]
\label{scholium:bk1_the_imagination_dipole}
The two open frontiers of this work are not independent gaps but the two poles of
one dipole about the imagination axis. The genericity conjecture
(Conj.~\ref{conjecture:bk1_genericity_of_symbolic_phase_transitions}) asks whether
imagination \emph{emerges} generically across the abstract space of complex
symbolic manifolds --- the generative pole, the integrative-expansion (TTIE) side
of the SRMF cycle (Def.~\ref{definition:bk4_test_time_integrative_expansion}). The
operational-irony conjecture
(Conj.~\ref{conjecture:bk1_symbolic_irony_encoding_llms}) asks whether imagination
\emph{survives} commitment to a concrete architecture --- the collapse pole, the
differentiation-collapse (TTDC) side (Def.~\ref{definition:bk4_collapse_of_symbolic_ide}).
Theorem~\ref{theorem:bk1_operational_irony_requires_imagination} and
Proposition~\ref{proposition:bk1_imagination_supplies_genericity_hypotheses} reduce
both to the single predicate \emph{does the system imagine?} The frontier is thus
SRMF-balanced: one question, read once toward emergence and once toward
instantiation, with no third residual required.
\end{scholium}
```

### Local Stability at the Reflective Fixed Locus (`lemma:bk1_local_stability_analysis`)

Role: `lemma` | Type: `lemma` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3707`

- Proof status: `proven`
- Depends on: `corollary:bk1_fixed_point` (Reflective Fixed Locus); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cites: `corollary:bk1_fixed_point` (Reflective Fixed Locus); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator)
- Cited by: `proof:bk2_probability_structure_on_manifold` (Symbolic Probability Structure on Emergent Manifold); `scholium:bk3_hypotheses_as_cognitive_membranes` (Hypotheses as Cognitive Membranes)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_B-012`
- Witnesses: `Book4D.CertifiedTTDC.abstention_base_inert_but_recorded`, `Book4D.CertifiedTTDC.recordedExecute_eq_iff`, `Book7.orbitLimit_base_fixed_but_recorded`, `Book7.orbitLimit_completeJacobian`, `Book7.orbitLimit_completeJacobian_semigroup`, `Book7.orbitLimit_derivative_image_kernel_split`, `Book7.orbitLimit_fixedLocusVelocity_iff`, `Book7.orbitLimit_linear_image_kernel_split`, `Book7.orbitLimit_semigroup_transverse_eigenmode_tendsto_zero`, `Book7.orbitLimit_transverse_contracts`, `Book7.orbitLimit_transverse_eigenvalue_stable`, `Book7.orbitLimit_transverse_iterates_tendsto_zero`, `Book7.orbitLimit_transverse_jacobian_eigenmode_stable`, `ScholiumDyn.ReflectiveLinearProjection.apply_apply`, `ScholiumDyn.ReflectiveLinearProjection.derivative_image_kernel_decomposition`, `ScholiumDyn.ReflectiveLinearProjection.exists_image_kernel_decomposition`, `ScholiumDyn.ReflectiveLinearProjection.image_kernel_intersection_zero`, `ScholiumDyn.ReflectiveLinearProjection.sub_identity_on_image`, `ScholiumDyn.ReflectiveLinearProjection.sub_identity_on_kernel`, `ScholiumDyn.base_cancellation_not_full_equilibrium`, `ScholiumDyn.combinedEulerLinearization_eigen_of_jacobian_eigen`, `ScholiumDyn.combinedEulerLinearization_iterate_mem_kernel`, `ScholiumDyn.combinedEulerLinearization_iterate_tendsto_zero`, `ScholiumDyn.combinedEulerLinearization_on_kernel`, `ScholiumDyn.combinedEulerLinearization_preserves_kernel`, `ScholiumDyn.combinedEulerLinearization_transverse_contracts`, `ScholiumDyn.combinedJacobian_apply`, `ScholiumDyn.combinedJacobian_on_image`, `ScholiumDyn.combinedJacobian_on_kernel`, `ScholiumDyn.completeJacobian_at_reflective_fixed`, `ScholiumDyn.continuousLinearMap_pow_apply_eigen`, `ScholiumDyn.equilibrium_cancellation_counterexample`, `ScholiumDyn.equilibrium_iff_fixed_and_drift_zero_of_aligned`, `ScholiumDyn.equilibrium_of_fixed_and_drift_zero`, `ScholiumDyn.fixedLocusVelocity_iff_derivative_fixed`, `ScholiumDyn.hasDerivAt_jacobianSemigroup`, `ScholiumDyn.hasFDerivAt_combinedVectorField`, `ScholiumDyn.hasFDerivAt_idempotent_at_fixed`, `ScholiumDyn.jacobianSemigroup_add`, `ScholiumDyn.jacobianSemigroup_add_apply`, `ScholiumDyn.jacobianSemigroup_apply_eigen`, `ScholiumDyn.jacobianSemigroup_eigenmode_tendsto_zero`, `ScholiumDyn.jacobianSemigroup_zero`, `ScholiumDyn.no_full_equilibrium_of_trace_production`, `ScholiumDyn.no_transverse_unstable_eigenmode`, `ScholiumDyn.norm_combinedEulerLinearization_iterate_le`, `ScholiumDyn.norm_combinedEulerLinearization_on_kernel_le`, `ScholiumDyn.recordedCombinedStep_eq_iff`, `ScholiumDyn.transverse_eigenvalue_abs_le`, `ScholiumDyn.transverse_eigenvalue_abs_lt_one`, `ScholiumDyn.transverse_jacobian_eigenmode_tendsto_zero`, `ScholiumDyn.transverse_jacobian_eigenvalue_le_negative_margin`, `ScholiumDyn.transverse_jacobian_eigenvalue_neg`
- Countermodels: `ScholiumDyn.equilibrium_cancellation_counterexample`
- Formal boundary: Clauses 1-3 have partial honest kernels. Fixed reflection plus zero drift is sufficient for scalar equilibrium, but the claimed converse is false without separation: an explicit idempotent stabilizer cancels nonzero drift. Component alignment recovers the scalar iff, while the history-bearing lift proves full stationarity iff visible flow and trace production both vanish. The algebraic projection kernel proves image/kernel decomposition, trivial intersection, and the actions of P-I on both summands. The chain rule now derives P=dR as an idempotent projection from differentiability, fixedness, and stabilizer idempotence. The complete Jacobian J=(P-I)+alpha*dD is now derived by Frechet derivative rules and restricted exactly to image and kernel directions. The projection image is now identified exactly with curve-based fixed-locus velocities, and the complete Euler linearization has a strict quantitative transverse contraction below the unit perturbation margin. Under the explicit invariant-kernel contract, every transverse iterate remains transverse, obeys the geometric q^n envelope, and converges to zero. Real transverse eigenmodes are now confined to the strict unit disk and neutral or unstable modes are excluded. Each real transverse Jacobian eigenvalue now has a strict negative margin and its explicit continuous-time exponential mode converges to zero. The full complete-Jacobian bounded-operator exponential now has identity, semigroup, pointwise composition, and generator-ODE laws. The semigroup action on every real Jacobian eigenvector is now identified exactly with scalar exponential action, and stable transverse semigroup orbits converge to zero. Full manifold charts, complex spectrum/spectral-radius identification, and center-manifold claims remain open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Consider the combined symbolic dynamics on $M$,
\[
dot{x} = bigl(R_{stab}(x) - xbigr) + alpha D(x), alpha > 0,
\]
with $R_{stab} in C^1$ the idempotent state-level stabilizer (thm theorem:bk1_emergence_of_reflection_operator, cor corollary:bk1_fixed_point) and $D$ the emergent drift field (thm theorem:bk1_emergence_of_drift_field). Then:


- Equilibrium condition. $x^*$ is an equilibrium iff $R_{stab}(x^*) = x^*$ and $D(x^*) = 0$. A fixed point of $R_{stab}$ at which the drift does not vanish is not an equilibrium of the combined flow.

- Projection structure. At such an $x^*$ the differential $P := dR_{stab,x^*}$ is a linear projection, $P^2 = P$, with $spec(P) subseteq {0,1}$; if $Fix(R_{stab})$ is a $C^1$ submanifold of constant rank near $x^*$, then $im(P) = T_{x^*}Fix(R_{stab})$.

- Jacobian and splitting. The linearization is the well-typed map
 \[
 J = (P - I) + alpha dD_{x^*},
 \]
 and $T_{x^*}M = im(P) oplus ker(P)$ splits its unperturbed part: $(P-I)|_{im P} = 0$ and $(P-I)|_{ker P} = -I$.

- Transverse stability is automatic. There exists $alpha_0 > 0$ such that for all $alpha in (0,alpha_0)$ the spectrum of $J$ transverse to the fixed locus lies in ${Re z < -tfrac{1}{2}}$: perturbations off $Fix(R_{stab})$ decay.

- Tangential stability is drift-governed. On the center directions $im(P)$ the leading-order dynamics are $dot{xi} = alpha (P dD_{x^*})|_{im P} xi + O(alpha^2)$; by center-manifold reduction $x^*$ is asymptotically stable within the fixed locus iff $Respecbigl(P dD_{x^*}|_{im P}bigr) < 0$, and unstable if some eigenvalue has positive real part.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Local Stability at the Reflective Fixed Locus]
\label{lemma:bk1_local_stability_analysis}
Consider the combined symbolic dynamics on $M$,
\[
\dot{x} \;=\; \bigl(R_{\mathrm{stab}}(x) - x\bigr) + \alpha\,D(x), \qquad \alpha > 0,
\]
with $R_{\mathrm{stab}} \in C^1$ the idempotent state-level stabilizer (thm~\ref{theorem:bk1_emergence_of_reflection_operator}, cor~\ref{corollary:bk1_fixed_point}) and $D$ the emergent drift field (thm~\ref{theorem:bk1_emergence_of_drift_field}). Then:
\begin{enumerate}
    \item \textbf{Equilibrium condition.} $x^*$ is an equilibrium iff $R_{\mathrm{stab}}(x^*) = x^*$ \emph{and} $D(x^*) = 0$. A fixed point of $R_{\mathrm{stab}}$ at which the drift does not vanish is not an equilibrium of the combined flow.
    \item \textbf{Projection structure.} At such an $x^*$ the differential $P := dR_{\mathrm{stab},x^*}$ is a linear projection, $P^2 = P$, with $\operatorname{spec}(P) \subseteq \{0,1\}$; if $\operatorname{Fix}(R_{\mathrm{stab}})$ is a $C^1$ submanifold of constant rank near $x^*$, then $\operatorname{im}(P) = T_{x^*}\operatorname{Fix}(R_{\mathrm{stab}})$.
    \item \textbf{Jacobian and splitting.} The linearization is the well-typed map
    \[
    J \;=\; (P - I) + \alpha\,dD_{x^*},
    \]
    and $T_{x^*}M = \operatorname{im}(P) \oplus \ker(P)$ splits its unperturbed part: $(P-I)|_{\operatorname{im} P} = 0$ and $(P-I)|_{\ker P} = -I$.
    \item \textbf{Transverse stability is automatic.} There exists $\alpha_0 > 0$ such that for all $\alpha \in (0,\alpha_0)$ the spectrum of $J$ transverse to the fixed locus lies in $\{\operatorname{Re} z < -\tfrac{1}{2}\}$: perturbations off $\operatorname{Fix}(R_{\mathrm{stab}})$ decay.
    \item \textbf{Tangential stability is drift-governed.} On the center directions $\operatorname{im}(P)$ the leading-order dynamics are $\dot{\xi} = \alpha\,(P\,dD_{x^*})|_{\operatorname{im} P}\,\xi + O(\alpha^2)$; by center-manifold reduction $x^*$ is asymptotically stable within the fixed locus iff $\operatorname{Re}\operatorname{spec}\bigl(P\,dD_{x^*}|_{\operatorname{im} P}\bigr) < 0$, and unstable if some eigenvalue has positive real part.
\end{enumerate}
\end{lemma}
```

### Stability via the projection-split linearization (`proof:bk1_sketch_stability_drift_reflection`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3727`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(1) At an equilibrium the vector field vanishes: $(R_{stab}(x^*) - x^*) + alpha D(x^*) = 0$. The displacement $R_{stab}(x^*) - x^*$ measures the failure of stabilization and $alpha D(x^*)$ the drift; requiring the equilibrium to persist across an interval of couplings $alpha$ forces each term to vanish separately, so $x^* in Fix(R_{stab}) cap D^{-1}(0)$, the sufficient form used downstream.

(2) Differentiating $R_{stab} circ R_{stab} = R_{stab}$ at $x^*$ with $R_{stab}(x^*) = x^*$ gives $dR_{stab,x^*} circ dR_{stab,x^*} = dR_{stab,x^*}$, i.e.\ $P^2 = P$, whence $spec(P) subseteq {0,1}$. The tangency $im(P) = T_{x^*}Fix(R_{stab})$ is the constant-rank theorem applied to $x mapsto R_{stab}(x) - x$.

(3) Linearizing $dot{x}$ about $x^*$ and using $D(x^*) = 0$ - so no constant forcing term survives - gives $tfrac{d}{dt}(x - x^*) = (P - I)(x - x^*) + alpha dD_{x^*}(x - x^*) + O(\|x - x^*\|^2)$, hence $J = (P - I) + alpha dD_{x^*}$. On the splitting $T_{x^*}M = im(P) oplus ker(P)$, $(P-I)$ is $0$ on $im(P)$ and $-I$ on $ker(P)$. The former statement instead retained $alpha D(x^*)$ as a ``constant to be absorbed'' and wrote the type-mismatched $dR_{stab,x^*} - alpha D(x^*)$, a linear map minus a vector; with the corrected equilibrium condition that term vanishes and $J$ is well typed.

(4) In block form on the splitting, the $ker P$ block is $-I + alpha (dD_{x^*})^{perpperp}$, with spectrum within distance $alpha\|dD_{x^*}\|$ of $-1$, plus $O(alpha)$ off-diagonal coupling controlled by standard spectral perturbation (Gershgorin or holomorphic functional calculus). Any $alpha_0 < tfrac{1}{2}\|dD_{x^*}\|^{-1}$ keeps these eigenvalues in ${Re z < -tfrac{1}{2}}$.

(5) The $im P$ block is $alpha (P dD_{x^*})|_{im P}$ at leading order; since the transverse spectrum is uniformly negative and the tangential spectrum is $O(alpha)$, the center-manifold theorem applies and reduces stability to the sign of $Respec(P dD_{x^*}|_{im P})$.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Stability via the projection-split linearization]
\label{proof:bk1_sketch_stability_drift_reflection}
\leavevmode

\textbf{(1)} At an equilibrium the vector field vanishes: $(R_{\mathrm{stab}}(x^*) - x^*) + \alpha D(x^*) = 0$. The displacement $R_{\mathrm{stab}}(x^*) - x^*$ measures the failure of stabilization and $\alpha D(x^*)$ the drift; requiring the equilibrium to persist across an interval of couplings $\alpha$ forces each term to vanish separately, so $x^* \in \operatorname{Fix}(R_{\mathrm{stab}}) \cap D^{-1}(0)$, the sufficient form used downstream.

\textbf{(2)} Differentiating $R_{\mathrm{stab}} \circ R_{\mathrm{stab}} = R_{\mathrm{stab}}$ at $x^*$ with $R_{\mathrm{stab}}(x^*) = x^*$ gives $dR_{\mathrm{stab},x^*} \circ dR_{\mathrm{stab},x^*} = dR_{\mathrm{stab},x^*}$, i.e.\ $P^2 = P$, whence $\operatorname{spec}(P) \subseteq \{0,1\}$. The tangency $\operatorname{im}(P) = T_{x^*}\operatorname{Fix}(R_{\mathrm{stab}})$ is the constant-rank theorem applied to $x \mapsto R_{\mathrm{stab}}(x) - x$.

\textbf{(3)} Linearizing $\dot{x}$ about $x^*$ and using $D(x^*) = 0$ -- so no constant forcing term survives -- gives $\tfrac{d}{dt}(x - x^*) = (P - I)(x - x^*) + \alpha\,dD_{x^*}(x - x^*) + O(\|x - x^*\|^2)$, hence $J = (P - I) + \alpha\,dD_{x^*}$. On the splitting $T_{x^*}M = \operatorname{im}(P) \oplus \ker(P)$, $(P-I)$ is $0$ on $\operatorname{im}(P)$ and $-I$ on $\ker(P)$. The former statement instead retained $\alpha D(x^*)$ as a ``constant to be absorbed'' and wrote the type-mismatched $dR_{\mathrm{stab},x^*} - \alpha D(x^*)$, a linear map minus a vector; with the corrected equilibrium condition that term vanishes and $J$ is well typed.

\textbf{(4)} In block form on the splitting, the $\ker P$ block is $-I + \alpha\,(dD_{x^*})^{\perp\perp}$, with spectrum within distance $\alpha\|dD_{x^*}\|$ of $-1$, plus $O(\alpha)$ off-diagonal coupling controlled by standard spectral perturbation (Gershgorin or holomorphic functional calculus). Any $\alpha_0 < \tfrac{1}{2}\|dD_{x^*}\|^{-1}$ keeps these eigenvalues in $\{\operatorname{Re} z < -\tfrac{1}{2}\}$.

\textbf{(5)} The $\operatorname{im} P$ block is $\alpha\,(P\,dD_{x^*})|_{\operatorname{im} P}$ at leading order; since the transverse spectrum is uniformly negative and the tangential spectrum is $O(\alpha)$, the center-manifold theorem applies and reduces stability to the sign of $\operatorname{Re}\operatorname{spec}(P\,dD_{x^*}|_{\operatorname{im} P})$.
\end{proof}
```

### Stabilization buys transverse stability (`remark:bk1_local_stability_interpretation`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3742`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The corrected lemma is sharper than the generic eigenvalue criterion it replaces: stabilization buys transverse stability for free - the $-I$ block on $ker(P)$ is the geometric signature of idempotence - and the only genuine stability question lives along the reflective fixed locus, decided entirely by the drift's restriction to that locus. Identity persistence is thus a property of how drift flows along the manifold of already-coherent states.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Stabilization buys transverse stability]
\label{remark:bk1_local_stability_interpretation}
The corrected lemma is sharper than the generic eigenvalue criterion it replaces: stabilization buys transverse stability for free -- the $-I$ block on $\ker(P)$ is the geometric signature of idempotence -- and the only genuine stability question lives \emph{along} the reflective fixed locus, decided entirely by the drift's restriction to that locus. Identity persistence is thus a property of how drift flows along the manifold of already-coherent states.
\end{remark}
```

### Symbolic Fluctuation–Dissipation Relation (`theorem:bk1_symbolic_fluctuation_dissipation_relation`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3747`

- Proof status: `proven`
- Depends on: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_variational_principle` (Variational Principle)
- Cites: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_variational_principle` (Variational Principle)
- Cited by: `sec:bk1_summary_and_implications` (Summary and Implications)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_B-015`
- Witnesses: `ScholiumD.symbolic_fluctuation_dissipation`
- Countermodels: none
- Conditions: See the receipted theorem statement and coverage note for explicit premises.
- Formal boundary: Local scalar calculus kernel: from an explicit HasDerivAt Kubo certificate, response equals the equilibrium-correlation derivative and -beta times the generator correlation. Expectation spaces, equilibrium measures, and derivation from the Fokker-Planck operator remain open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

For small perturbations around equilibrium, the response of the symbolic system to an external perturbation coupled to an observable $B$ is related to equilibrium fluctuations by:
\[
R_{AB}(t) = frac{d}{dt} langle A(t) B(0) rangle_{text{eq}} = -beta langle A(t) L B(0) rangle_{text{eq}} text{for } t > 0,
\]
where:
- $A, B in C^infty(M)$ are symbolic observables on the symbolic manifold $M$ (def definition:bk1_symbolic_manifold_existence),
- $langle cdot rangle_{text{eq}}$ denotes expectation with respect to the equilibrium distribution $rho_{text{eq}}$ (thm theorem:bk1_variational_principle),
- $L$ is the adjoint Fokker–Planck operator derived from the fundamental symbolic evolution equation (thm theorem:bk1_fundamental_relation_fokker_plank_equation),
- and $R_{AB}(t)$ represents the linear response of $langle A(t) rangle$ to a perturbation in $B$ at $t = 0$.

This relation encodes how symbolic systems dissipate external influences via internal equilibrium fluctuations.

The result follows from linear response theory applied to symbolic systems governed by the Fokker–Planck equation (thm theorem:bk1_fundamental_relation_fokker_plank_equation). Consider a perturbation to the equilibrium dynamics induced by a weak external force coupled to observable $B$. Using the Kubo formalism, the change in $langle A(t) rangle$ is proportional to the correlation of $A(t)$ with the perturbing influence $B(0)$, evaluated at equilibrium. The generator of the dynamics is the Fokker–Planck operator $L$, which acts on $B$ and propagates via adjoint dynamics. The temperature-like parameter $beta$ sets the scale linking dissipation and fluctuation amplitudes. This correspondence is structurally parallel to classical statistical mechanics but operates over the symbolic manifold $(M,g,D,R)$.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Symbolic Fluctuation–Dissipation Relation]
\label{theorem:bk1_symbolic_fluctuation_dissipation_relation}
For small perturbations around equilibrium, the response of the symbolic system to an external perturbation coupled to an observable $B$ is related to equilibrium fluctuations by:
\[
R_{AB}(t) = \frac{d}{dt} \langle A(t) B(0) \rangle_{\text{eq}} = -\beta \langle A(t) \mathcal{L} B(0) \rangle_{\text{eq}} \quad \text{for } t > 0,
\]
where:
- $A, B \in C^\infty(M)$ are symbolic observables on the symbolic manifold $M$ (def~\ref{definition:bk1_symbolic_manifold_existence}),
- $\langle \cdot \rangle_{\text{eq}}$ denotes expectation with respect to the equilibrium distribution $\rho_{\text{eq}}$ (thm~\ref{theorem:bk1_variational_principle}),
- $\mathcal{L}$ is the adjoint Fokker–Planck operator derived from the fundamental symbolic evolution equation (thm~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}),
- and $R_{AB}(t)$ represents the linear response of $\langle A(t) \rangle$ to a perturbation in $B$ at $t = 0$.

This relation encodes how symbolic systems dissipate external influences via internal equilibrium fluctuations.

\begin{proof}[Fluctuation--Dissipation via Kubo Linear Response]
\label{proof:bk1_sketch_fluctuation_dissipation}
\leavevmode

The result follows from linear response theory applied to symbolic systems governed by the Fokker–Planck equation (thm~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}). Consider a perturbation to the equilibrium dynamics induced by a weak external force coupled to observable $B$. Using the Kubo formalism, the change in $\langle A(t) \rangle$ is proportional to the correlation of $A(t)$ with the perturbing influence $B(0)$, evaluated at equilibrium. The generator of the dynamics is the Fokker–Planck operator $\mathcal{L}$, which acts on $B$ and propagates via adjoint dynamics. The temperature-like parameter $\beta$ sets the scale linking dissipation and fluctuation amplitudes. This correspondence is structurally parallel to classical statistical mechanics but operates over the symbolic manifold $(M,g,D,R)$.
\end{proof}
\end{theorem}
```

### Fluctuation--Dissipation via Kubo Linear Response (`proof:bk1_sketch_fluctuation_dissipation`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3761`

- Proof status: `not_applicable`
- Depends on: `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Cites: `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Cited by: none
- Macros used: none

**Statement / Body**

The result follows from linear response theory applied to symbolic systems governed by the Fokker–Planck equation (thm theorem:bk1_fundamental_relation_fokker_plank_equation). Consider a perturbation to the equilibrium dynamics induced by a weak external force coupled to observable $B$. Using the Kubo formalism, the change in $langle A(t) rangle$ is proportional to the correlation of $A(t)$ with the perturbing influence $B(0)$, evaluated at equilibrium. The generator of the dynamics is the Fokker–Planck operator $L$, which acts on $B$ and propagates via adjoint dynamics. The temperature-like parameter $beta$ sets the scale linking dissipation and fluctuation amplitudes. This correspondence is structurally parallel to classical statistical mechanics but operates over the symbolic manifold $(M,g,D,R)$.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Fluctuation--Dissipation via Kubo Linear Response]
\label{proof:bk1_sketch_fluctuation_dissipation}
\leavevmode

The result follows from linear response theory applied to symbolic systems governed by the Fokker–Planck equation (thm~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}). Consider a perturbation to the equilibrium dynamics induced by a weak external force coupled to observable $B$. Using the Kubo formalism, the change in $\langle A(t) \rangle$ is proportional to the correlation of $A(t)$ with the perturbing influence $B(0)$, evaluated at equilibrium. The generator of the dynamics is the Fokker–Planck operator $\mathcal{L}$, which acts on $B$ and propagates via adjoint dynamics. The temperature-like parameter $\beta$ sets the scale linking dissipation and fluctuation amplitudes. This correspondence is structurally parallel to classical statistical mechanics but operates over the symbolic manifold $(M,g,D,R)$.
\end{proof}
```

### Toward a Unified Framework (`sec:bk1_toward_a_unified_framework`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3768`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Action Functional (`definition:bk1_symbolic_action_functional`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3771`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Cites: `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Cited by: none
- Macros used: `\R`

### Lean correspondence

- Status: `constructed`
- Records: `MAP-SCHOLIUM_A-067`
- Witnesses: `ScholiumDyn.action_nonneg`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: Discrete Onsager-Machlup action.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The symbolic action functional $S: C^infty(M times [s_1, s_2]) to R$ is defined over paths $rho(x,s)$ in the space of symbolic probability densities (see def definition:bk1_symbolic_probabilty_density):
\[
S[rho] = int_{s_1}^{s_2} int_M L(rho, partial_s rho, nabla rho; x, s) dmu_g(x) ds,
\]
where $L$ is a Lagrangian density. For instance, an Onsager–Machlup-type Lagrangian reflecting symbolic Fokker–Planck dynamics (see thm theorem:bk1_fundamental_relation_fokker_plank_equation) may take the form:
\[
L = frac{1}{2} left( partial_s rho - L rho right)^2,
\]
where $L$ is the symbolic Fokker–Planck operator. This interpretation frames symbolic evolution as extremizing an action over the space of probabilistic flows.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Action Functional]
\label{definition:bk1_symbolic_action_functional}
The symbolic action functional $\mathcal{S}: C^\infty(M \times [s_1, s_2]) \to \R$ is defined over paths $\rho(x,s)$ in the space of symbolic probability densities (see def~\ref{definition:bk1_symbolic_probabilty_density}):
\[
\mathcal{S}[\rho] = \int_{s_1}^{s_2} \int_M L(\rho, \partial_s \rho, \nabla \rho; x, s) \, d\mu_g(x) \, ds,
\]
where $L$ is a Lagrangian density. For instance, an Onsager–Machlup-type Lagrangian reflecting symbolic Fokker–Planck dynamics (see thm~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}) may take the form:
\[
L = \frac{1}{2} \left( \partial_s \rho - \mathcal{L} \rho \right)^2,
\]
where $\mathcal{L}$ is the symbolic Fokker–Planck operator. This interpretation frames symbolic evolution as extremizing an action over the space of probabilistic flows.
\end{definition}
```

### Principle of Least Action (`theorem:bk1_princple_of_least_action`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3784`

- Proof status: `proven`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Cites: `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Cited by: `scholium:bk4_symbolic_parsimony` (TTCS and the Principle of Symbolic Parsimony); `sec:bk1_summary_and_implications` (Summary and Implications)
- Macros used: none

### Lean correspondence

- Status: `conditional`
- Records: `MAP-SCHOLIUM_A-068`
- Witnesses: `ScholiumDyn.least_action_iff_evolution`
- Countermodels: none
- Conditions: discrete kernels only: ODE flows, Riemannian geodesics, Hopf-Rinow, and the MSR path integral stay open; the self-representation clause of reflexive maps is interpretive
- Formal boundary: Exact discrete form: dynamics = zero-action paths = the global minimum; MSR open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Dynamics governed by the symbolic Fokker-Planck equation (see Thm. theorem:bk1_fundamental_relation_fokker_plank_equation) can, under suitable path-integral interpretations and choices of symbolic Lagrangian $L$, be formulated as obeying a symbolic principle of least action:
\[
delta S[rho] = 0.
\]

Step 1: Introduce conjugate field.
On symbolic spacetime $M times mathbb{R}$, introduce the MSR response field
$hatrho(x,s)$ conjugate to $rho$.
Cf. Def. definition:bk1_symbolic_manifold.
The symbolic action functional is:
\[

S[rho, hatrho]
&= int_{mathbb{R}} int_M
hatrho(x,s)Bigl(partial_s rho - LrhoBigr) dmu_g ds,

\]
where $Lrho = -nablacdot(Drho) + sigma^2Deltarho$ is the symbolic Fokker-Planck operator built from drift $D$ (Def. definition:bk1_drift_field) and symbolic temperature $sigma^2$.

Step 2: Extremize over $hatrho$. Setting $deltaS/deltahatrho = 0$ yields:
\[
partial_srho = Lrho = -nablacdot(Drho) + sigma^2Deltarho,
\]
which is exactly the symbolic Fokker-Planck equation (Thm. theorem:bk1_fundamental_relation_fokker_plank_equation). Thus $deltaS[rho] = 0$ on trajectories satisfying the Fokker-Planck dynamics.

Step 3: Saddle-point is the physical trajectory. The response field $hatrho$ acts as a Lagrange multiplier enforcing the Fokker-Planck constraint at each spacetime point. The saddle-point $(rho^*, hatrho^* = 0)$ of $S$ is identified with the physical evolution: $hatrho^* = 0$ because the physical path has zero deviation from drift-diffusion balance, and $rho^*$ solves the Fokker-Planck equation. Hence $deltaS[rho] = 0$ is realized by symbolic evolution, completing the variational derivation.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Principle of Least Action]
\label{theorem:bk1_princple_of_least_action}
\leavevmode\newline
Dynamics governed by the symbolic Fokker-Planck equation (see Thm.~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}) can, under suitable path-integral interpretations and choices of symbolic Lagrangian $L$, be formulated as obeying a symbolic principle of least action:
\[
\delta \mathcal{S}[\rho] = 0.
\]

\begin{proof}[Fokker--Planck from Symbolic Action via Martin--Siggia--Rose]
\label{proof:bk1_sketch_fokker_planck_action}
\leavevmode

\textbf{Step 1: Introduce conjugate field.}
On symbolic spacetime $M \times \mathbb{R}$, introduce the MSR response field
$\hat\rho(x,s)$ conjugate to $\rho$.
Cf.~Def.~\ref{definition:bk1_symbolic_manifold}.
The symbolic action functional is:
\[
\begin{aligned}
\mathcal{S}[\rho, \hat\rho]
&= \int_{\mathbb{R}} \int_M
\hat\rho(x,s)\Bigl(\partial_s \rho - \mathcal{L}\rho\Bigr)\,d\mu_g\,ds,
\end{aligned}
\]
where $\mathcal{L}\rho = -\nabla\cdot(D\rho) + \sigma^2\Delta\rho$ is the symbolic Fokker--Planck operator built from drift $D$ (Def.~\ref{definition:bk1_drift_field}) and symbolic temperature $\sigma^2$.

\textbf{Step 2: Extremize over $\hat\rho$.} Setting $\delta\mathcal{S}/\delta\hat\rho = 0$ yields:
\[
\partial_s\rho = \mathcal{L}\rho = -\nabla\cdot(D\rho) + \sigma^2\Delta\rho,
\]
which is exactly the symbolic Fokker--Planck equation (Thm.~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}). Thus $\delta\mathcal{S}[\rho] = 0$ on trajectories satisfying the Fokker--Planck dynamics.

\textbf{Step 3: Saddle-point is the physical trajectory.} The response field $\hat\rho$ acts as a Lagrange multiplier enforcing the Fokker--Planck constraint at each spacetime point. The saddle-point $(\rho^*, \hat\rho^* = 0)$ of $\mathcal{S}$ is identified with the physical evolution: $\hat\rho^* = 0$ because the physical path has zero deviation from drift-diffusion balance, and $\rho^*$ solves the Fokker--Planck equation. Hence $\delta\mathcal{S}[\rho] = 0$ is realized by symbolic evolution, completing the variational derivation.
\end{proof}
\end{theorem}
```

### Fokker--Planck from Symbolic Action via Martin--Siggia--Rose (`proof:bk1_sketch_fokker_planck_action`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3792`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Cited by: none
- Macros used: none

**Statement / Body**

Step 1: Introduce conjugate field.
On symbolic spacetime $M times mathbb{R}$, introduce the MSR response field
$hatrho(x,s)$ conjugate to $rho$.
Cf. Def. definition:bk1_symbolic_manifold.
The symbolic action functional is:
\[

S[rho, hatrho]
&= int_{mathbb{R}} int_M
hatrho(x,s)Bigl(partial_s rho - LrhoBigr) dmu_g ds,

\]
where $Lrho = -nablacdot(Drho) + sigma^2Deltarho$ is the symbolic Fokker-Planck operator built from drift $D$ (Def. definition:bk1_drift_field) and symbolic temperature $sigma^2$.

Step 2: Extremize over $hatrho$. Setting $deltaS/deltahatrho = 0$ yields:
\[
partial_srho = Lrho = -nablacdot(Drho) + sigma^2Deltarho,
\]
which is exactly the symbolic Fokker-Planck equation (Thm. theorem:bk1_fundamental_relation_fokker_plank_equation). Thus $deltaS[rho] = 0$ on trajectories satisfying the Fokker-Planck dynamics.

Step 3: Saddle-point is the physical trajectory. The response field $hatrho$ acts as a Lagrange multiplier enforcing the Fokker-Planck constraint at each spacetime point. The saddle-point $(rho^*, hatrho^* = 0)$ of $S$ is identified with the physical evolution: $hatrho^* = 0$ because the physical path has zero deviation from drift-diffusion balance, and $rho^*$ solves the Fokker-Planck equation. Hence $deltaS[rho] = 0$ is realized by symbolic evolution, completing the variational derivation.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Fokker--Planck from Symbolic Action via Martin--Siggia--Rose]
\label{proof:bk1_sketch_fokker_planck_action}
\leavevmode

\textbf{Step 1: Introduce conjugate field.}
On symbolic spacetime $M \times \mathbb{R}$, introduce the MSR response field
$\hat\rho(x,s)$ conjugate to $\rho$.
Cf.~Def.~\ref{definition:bk1_symbolic_manifold}.
The symbolic action functional is:
\[
\begin{aligned}
\mathcal{S}[\rho, \hat\rho]
&= \int_{\mathbb{R}} \int_M
\hat\rho(x,s)\Bigl(\partial_s \rho - \mathcal{L}\rho\Bigr)\,d\mu_g\,ds,
\end{aligned}
\]
where $\mathcal{L}\rho = -\nabla\cdot(D\rho) + \sigma^2\Delta\rho$ is the symbolic Fokker--Planck operator built from drift $D$ (Def.~\ref{definition:bk1_drift_field}) and symbolic temperature $\sigma^2$.

\textbf{Step 2: Extremize over $\hat\rho$.} Setting $\delta\mathcal{S}/\delta\hat\rho = 0$ yields:
\[
\partial_s\rho = \mathcal{L}\rho = -\nabla\cdot(D\rho) + \sigma^2\Delta\rho,
\]
which is exactly the symbolic Fokker--Planck equation (Thm.~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}). Thus $\delta\mathcal{S}[\rho] = 0$ on trajectories satisfying the Fokker--Planck dynamics.

\textbf{Step 3: Saddle-point is the physical trajectory.} The response field $\hat\rho$ acts as a Lagrange multiplier enforcing the Fokker--Planck constraint at each spacetime point. The saddle-point $(\rho^*, \hat\rho^* = 0)$ of $\mathcal{S}$ is identified with the physical evolution: $\hat\rho^* = 0$ because the physical path has zero deviation from drift-diffusion balance, and $\rho^*$ solves the Fokker--Planck equation. Hence $\delta\mathcal{S}[\rho] = 0$ is realized by symbolic evolution, completing the variational derivation.
\end{proof}
```

### Symbolic Information Geometry (`definition:bk1_symbolic_information_geometry`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3820`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density)
- Cites: `definition:bk1_symbolic_manifold_existence` (Symbolic Manifold Existence); `definition:bk1_symbolic_probabilty_density` (Symbolic Probability Density)
- Cited by: `corollary:bk1_wasserstein_geometric_interpretation` (Wasserstein Geometric Interpretation); `proof:bk1_sketch_gradient_flow_thermodynamics` (Gradient Flow Structure via JKO); `proof:bk1_wasserstein_geometric_interpretation` (Restatement of the Wasserstein Gradient-Flow Theorem); `theorem:bk1_the_fokker_planck_equation_theorem` (Information Geometric Interpretation)
- Macros used: none

**Statement / Body**

Let $P(M)$ be the space of smooth, positive symbolic probability densities on the manifold $M$ (see def definition:bk1_symbolic_probabilty_density, def definition:bk1_symbolic_manifold_existence). The Fisher–Rao metric on the tangent space $T_{rho} P(M)$ is given by:
\[
G_{rho}(v_1, v_2) = int_M frac{v_1(x) v_2(x)}{rho(x)} dmu_g(x),
\]
where $v_1, v_2 in T_rho P(M)$ are tangent vectors satisfying $int_M v_i(x) dmu_g(x) = 0$.

This induces a Riemannian structure on $P(M)$, enabling geodesic analysis and variational characterizations of symbolic thermodynamic flows.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Information Geometry]
\label{definition:bk1_symbolic_information_geometry}
Let $\mathcal{P}(M)$ be the space of smooth, positive symbolic probability densities on the manifold $M$ (see def~\ref{definition:bk1_symbolic_probabilty_density}, def~\ref{definition:bk1_symbolic_manifold_existence}). The Fisher–Rao metric on the tangent space $T_{\rho} \mathcal{P}(M)$ is given by:
\[
G_{\rho}(v_1, v_2) = \int_M \frac{v_1(x) v_2(x)}{\rho(x)} \, d\mu_g(x),
\]
where $v_1, v_2 \in T_\rho \mathcal{P}(M)$ are tangent vectors satisfying $\int_M v_i(x) \, d\mu_g(x) = 0$.

This induces a Riemannian structure on $\mathcal{P}(M)$, enabling geodesic analysis and variational characterizations of symbolic thermodynamic flows.
\end{definition}
```

### Information Geometric Interpretation (`theorem:bk1_the_fokker_planck_equation_theorem`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3830`

- Proof status: `proven`
- Depends on: `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_information_geometry` (Symbolic Information Geometry); `proof:bk1_lagrange_free_energy` (Free Energy Minimization via Lagrange Multipliers); `proof:bk1_sketch_direct_evaluation` (H-Theorem via Symbolic Integration by Parts); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_variational_principle` (Variational Principle)
- Cites: `definition:bk1_symbolic_entropy` (Symbolic Entropy); `definition:bk1_symbolic_information_geometry` (Symbolic Information Geometry); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_variational_principle` (Variational Principle)
- Cited by: `corollary:bk1_wasserstein_geometric_interpretation` (Wasserstein Geometric Interpretation); `proof:bk1_sketch_direct_evaluation` (H-Theorem via Symbolic Integration by Parts); `proof:bk1_wasserstein_geometric_interpretation` (Restatement of the Wasserstein Gradient-Flow Theorem)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_B-016`
- Witnesses: `ScholiumD.FreeEnergyDescent.antitone`, `ScholiumD.jko_step_freeEnergy_le`
- Countermodels: none
- Conditions: continuum/Hilbert/PDE-on-manifold content stays open; chart-complex restatements carry Glued as a named hypothesis where the source consumes compatibility; modeling laws are structure fields or explicit hypotheses
- Formal boundary: Discrete JKO kernel: minimizing squared transport cost plus free energy against the previous-state competitor proves one-step free-energy descent; the existing descent structure then yields antitonicity. Wasserstein probability geometry, the Fokker-Planck PDE, and the tau-to-zero convergence theorem remain open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The symbolic Fokker–Planck equation (see thm theorem:bk1_fundamental_relation_fokker_plank_equation) can be interpreted as a extbf{gradient flow} of the relative entropy—i.e., the Kullback–Leibler divergence
\[
D_{KL}(rho \| rho_{text{eq}}),
\]
with respect to a metric structure on the symbolic probability space $P(M)$ (see def definition:bk1_symbolic_information_geometry), such as the extbf{Fisher–Rao} or extbf{Wasserstein} metric.

Specifically, it is often realized as the gradient flow of the symbolic free energy functional $F[rho]$ (see thm theorem:bk1_variational_principle) with respect to the extbf{Wasserstein-2 metric} $W_2$. This structure reflects a variational evolution toward equilibrium governed by the symbolic entropy landscape (def definition:bk1_symbolic_entropy).

A complete formulation of the symbolic Wasserstein geometry is deferred to subsequent development.

We show the symbolic Fokker-Planck equation is a Wasserstein gradient flow.
Its driving functional is $F[rho]$.

Wasserstein-2 metric on $P(M)$.
The $W_2$ metric (Def. definition:bk1_symbolic_information_geometry)
defines the inner product on tangent vectors
$dotrho in T_rhoP(M)$ via the continuity equation
$dotrho + nablacdot(rhov)=0$, giving the squared norm:
\[
\|dotrho\|_{W_2}^2 = int_M rho\|v\|_g^2 dmu_g.
\]

Gradient of $F$ with respect to $W_2$.
The $W_2$-gradient of a functional $F[rho]$ is determined as follows.
If $partial_srho = -nablacdot(rho v)$, then
$v = nabla(delta F/deltarho)$.
From proof proof:bk1_lagrange_free_energy,
$delta F/deltarho = H + beta^{-1}(1+logrho)$, so
$nabla(delta F/deltarho) = nabla H + beta^{-1}nablalogrho$.
The $W_2$ gradient flow is therefore:
\[
partial_srho
= -nablacdot\!bigl(rho (nabla H + beta^{-1}nablalogrho)bigr)
= -nablacdot(rhonabla H) + beta^{-1}nablacdot(nablarho).
\]
With symbolic drift $D = -nabla H$, this is exactly the Fokker-Planck equation
(Thm. theorem:bk1_fundamental_relation_fokker_plank_equation):
$partial_srho = -nablacdot(rho D) + beta^{-1}nabla^2rho$.

Jordan-Kinderlehrer-Otto (JKO) discretization.
The gradient flow interpretation is made precise by the JKO scheme: for time step $tau>0$,
\[
rho_{k+1} = argmin_{rhoinP(M)}
Bigl{tfrac{1}{2tau}W_2(rho,rho_k)^2 + F[rho]Bigr}.
\]
As $tauto 0$, the JKO iterates converge to the solution of the Fokker-Planck equation.
The H-theorem ($dF/dsleq 0$, proof proof:bk1_sketch_direct_evaluation) is the
continuous-time manifestation of the descent property built into each JKO step.
The Fisher-Rao metric
(Def. definition:bk1_symbolic_information_geometry) provides a complementary
characterization for reversible dynamics, where $D_{KL}(rho\|rho_{text{eq}})$
decreases monotonically along the flow.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Information Geometric Interpretation]
\label{theorem:bk1_the_fokker_planck_equation_theorem}
The symbolic Fokker–Planck equation (see thm~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}) can be interpreted as a 	extbf{gradient flow} of the relative entropy—i.e., the Kullback–Leibler divergence
\[
D_{\mathrm{KL}}(\rho \| \rho_{\text{eq}}),
\]
with respect to a metric structure on the symbolic probability space $\mathcal{P}(M)$ (see def~\ref{definition:bk1_symbolic_information_geometry}), such as the 	extbf{Fisher–Rao} or 	extbf{Wasserstein} metric.

Specifically, it is often realized as the gradient flow of the symbolic free energy functional $F[\rho]$ (see thm~\ref{theorem:bk1_variational_principle}) with respect to the 	extbf{Wasserstein-2 metric} $W_2$. This structure reflects a variational evolution toward equilibrium governed by the symbolic entropy landscape (def~\ref{definition:bk1_symbolic_entropy}).

A complete formulation of the symbolic Wasserstein geometry is deferred to subsequent development.
\begin{proof}[Gradient Flow Structure via JKO]
\label{proof:bk1_sketch_gradient_flow_thermodynamics}
\leavevmode

We show the symbolic Fokker--Planck equation is a Wasserstein gradient flow.
Its driving functional is $F[\rho]$.

\textbf{Wasserstein-2 metric on $\mathcal{P}(M)$.}
The $W_2$ metric (Def.~\ref{definition:bk1_symbolic_information_geometry})
defines the inner product on tangent vectors
$\dot\rho \in T_\rho\mathcal{P}(M)$ via the continuity equation
$\dot\rho + \nabla\cdot(\rho\mathbf{v})=0$, giving the squared norm:
\[
\|\dot\rho\|_{W_2}^2 = \int_M \rho\|\mathbf{v}\|_g^2\,d\mu_g.
\]

\textbf{Gradient of $F$ with respect to $W_2$.}
The $W_2$-gradient of a functional $F[\rho]$ is determined as follows.
If $\partial_s\rho = -\nabla\cdot(\rho\,\mathbf{v})$, then
$\mathbf{v} = \nabla(\delta F/\delta\rho)$.
From proof~\ref{proof:bk1_lagrange_free_energy},
$\delta F/\delta\rho = H + \beta^{-1}(1+\log\rho)$, so
$\nabla(\delta F/\delta\rho) = \nabla H + \beta^{-1}\nabla\log\rho$.
The $W_2$ gradient flow is therefore:
\[
\partial_s\rho
= -\nabla\cdot\!\bigl(\rho\,(\nabla H + \beta^{-1}\nabla\log\rho)\bigr)
= -\nabla\cdot(\rho\nabla H) + \beta^{-1}\nabla\cdot(\nabla\rho).
\]
With symbolic drift $D = -\nabla H$, this is exactly the Fokker--Planck equation
(Thm.~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}):
$\partial_s\rho = -\nabla\cdot(\rho D) + \beta^{-1}\nabla^2\rho$.

\textbf{Jordan--Kinderlehrer--Otto (JKO) discretization.}
The gradient flow interpretation is made precise by the JKO scheme: for time step $\tau>0$,
\[
\rho_{k+1} = \arg\min_{\rho\in\mathcal{P}(M)}
\Bigl\{\tfrac{1}{2\tau}W_2(\rho,\rho_k)^2 + F[\rho]\Bigr\}.
\]
As $\tau\to 0$, the JKO iterates converge to the solution of the Fokker--Planck equation.
The H-theorem ($dF/ds\leq 0$, proof~\ref{proof:bk1_sketch_direct_evaluation}) is the
continuous-time manifestation of the descent property built into each JKO step.
The Fisher--Rao metric
(Def.~\ref{definition:bk1_symbolic_information_geometry}) provides a complementary
characterization for reversible dynamics, where $D_{\mathrm{KL}}(\rho\|\rho_{\text{eq}})$
decreases monotonically along the flow.
\end{proof}
\end{theorem}
```

### Gradient Flow Structure via JKO (`proof:bk1_sketch_gradient_flow_thermodynamics`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3841`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_information_geometry` (Symbolic Information Geometry); `proof:bk1_lagrange_free_energy` (Free Energy Minimization via Lagrange Multipliers); `proof:bk1_sketch_direct_evaluation` (H-Theorem via Symbolic Integration by Parts); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Cites: `definition:bk1_symbolic_information_geometry` (Symbolic Information Geometry); `proof:bk1_lagrange_free_energy` (Free Energy Minimization via Lagrange Multipliers); `proof:bk1_sketch_direct_evaluation` (H-Theorem via Symbolic Integration by Parts); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation)
- Cited by: `corollary:bk1_wasserstein_geometric_interpretation` (Wasserstein Geometric Interpretation); `example:bk4_ttpr_identity_refinement` (Precision Refinement of Fuzzy Identity Map); `proof:bk1_wasserstein_geometric_interpretation` (Restatement of the Wasserstein Gradient-Flow Theorem)
- Macros used: none

**Statement / Body**

We show the symbolic Fokker-Planck equation is a Wasserstein gradient flow.
Its driving functional is $F[rho]$.

Wasserstein-2 metric on $P(M)$.
The $W_2$ metric (Def. definition:bk1_symbolic_information_geometry)
defines the inner product on tangent vectors
$dotrho in T_rhoP(M)$ via the continuity equation
$dotrho + nablacdot(rhov)=0$, giving the squared norm:
\[
\|dotrho\|_{W_2}^2 = int_M rho\|v\|_g^2 dmu_g.
\]

Gradient of $F$ with respect to $W_2$.
The $W_2$-gradient of a functional $F[rho]$ is determined as follows.
If $partial_srho = -nablacdot(rho v)$, then
$v = nabla(delta F/deltarho)$.
From proof proof:bk1_lagrange_free_energy,
$delta F/deltarho = H + beta^{-1}(1+logrho)$, so
$nabla(delta F/deltarho) = nabla H + beta^{-1}nablalogrho$.
The $W_2$ gradient flow is therefore:
\[
partial_srho
= -nablacdot\!bigl(rho (nabla H + beta^{-1}nablalogrho)bigr)
= -nablacdot(rhonabla H) + beta^{-1}nablacdot(nablarho).
\]
With symbolic drift $D = -nabla H$, this is exactly the Fokker-Planck equation
(Thm. theorem:bk1_fundamental_relation_fokker_plank_equation):
$partial_srho = -nablacdot(rho D) + beta^{-1}nabla^2rho$.

Jordan-Kinderlehrer-Otto (JKO) discretization.
The gradient flow interpretation is made precise by the JKO scheme: for time step $tau>0$,
\[
rho_{k+1} = argmin_{rhoinP(M)}
Bigl{tfrac{1}{2tau}W_2(rho,rho_k)^2 + F[rho]Bigr}.
\]
As $tauto 0$, the JKO iterates converge to the solution of the Fokker-Planck equation.
The H-theorem ($dF/dsleq 0$, proof proof:bk1_sketch_direct_evaluation) is the
continuous-time manifestation of the descent property built into each JKO step.
The Fisher-Rao metric
(Def. definition:bk1_symbolic_information_geometry) provides a complementary
characterization for reversible dynamics, where $D_{KL}(rho\|rho_{text{eq}})$
decreases monotonically along the flow.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Gradient Flow Structure via JKO]
\label{proof:bk1_sketch_gradient_flow_thermodynamics}
\leavevmode

We show the symbolic Fokker--Planck equation is a Wasserstein gradient flow.
Its driving functional is $F[\rho]$.

\textbf{Wasserstein-2 metric on $\mathcal{P}(M)$.}
The $W_2$ metric (Def.~\ref{definition:bk1_symbolic_information_geometry})
defines the inner product on tangent vectors
$\dot\rho \in T_\rho\mathcal{P}(M)$ via the continuity equation
$\dot\rho + \nabla\cdot(\rho\mathbf{v})=0$, giving the squared norm:
\[
\|\dot\rho\|_{W_2}^2 = \int_M \rho\|\mathbf{v}\|_g^2\,d\mu_g.
\]

\textbf{Gradient of $F$ with respect to $W_2$.}
The $W_2$-gradient of a functional $F[\rho]$ is determined as follows.
If $\partial_s\rho = -\nabla\cdot(\rho\,\mathbf{v})$, then
$\mathbf{v} = \nabla(\delta F/\delta\rho)$.
From proof~\ref{proof:bk1_lagrange_free_energy},
$\delta F/\delta\rho = H + \beta^{-1}(1+\log\rho)$, so
$\nabla(\delta F/\delta\rho) = \nabla H + \beta^{-1}\nabla\log\rho$.
The $W_2$ gradient flow is therefore:
\[
\partial_s\rho
= -\nabla\cdot\!\bigl(\rho\,(\nabla H + \beta^{-1}\nabla\log\rho)\bigr)
= -\nabla\cdot(\rho\nabla H) + \beta^{-1}\nabla\cdot(\nabla\rho).
\]
With symbolic drift $D = -\nabla H$, this is exactly the Fokker--Planck equation
(Thm.~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}):
$\partial_s\rho = -\nabla\cdot(\rho D) + \beta^{-1}\nabla^2\rho$.

\textbf{Jordan--Kinderlehrer--Otto (JKO) discretization.}
The gradient flow interpretation is made precise by the JKO scheme: for time step $\tau>0$,
\[
\rho_{k+1} = \arg\min_{\rho\in\mathcal{P}(M)}
\Bigl\{\tfrac{1}{2\tau}W_2(\rho,\rho_k)^2 + F[\rho]\Bigr\}.
\]
As $\tau\to 0$, the JKO iterates converge to the solution of the Fokker--Planck equation.
The H-theorem ($dF/ds\leq 0$, proof~\ref{proof:bk1_sketch_direct_evaluation}) is the
continuous-time manifestation of the descent property built into each JKO step.
The Fisher--Rao metric
(Def.~\ref{definition:bk1_symbolic_information_geometry}) provides a complementary
characterization for reversible dynamics, where $D_{\mathrm{KL}}(\rho\|\rho_{\text{eq}})$
decreases monotonically along the flow.
\end{proof}
```

### Wasserstein Geometric Interpretation (`corollary:bk1_wasserstein_geometric_interpretation`)

Role: `corollary` | Type: `corollary` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3889`

- Proof status: `proven`
- Depends on: `definition:bk1_symbolic_information_geometry` (Symbolic Information Geometry); `proof:bk1_sketch_gradient_flow_thermodynamics` (Gradient Flow Structure via JKO); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_the_fokker_planck_equation_theorem` (Information Geometric Interpretation); `theorem:bk1_variational_principle` (Variational Principle)
- Cites: `definition:bk1_symbolic_information_geometry` (Symbolic Information Geometry); `proof:bk1_sketch_gradient_flow_thermodynamics` (Gradient Flow Structure via JKO); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_the_fokker_planck_equation_theorem` (Information Geometric Interpretation); `theorem:bk1_variational_principle` (Variational Principle)
- Cited by: `corollary:bk1_event_horizon_identity_field` (Event Horizon Identity Field); `proof:bk1_event_horizon_identity_field` (Identity Field on the Symbolized Causal Patch)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_B-017`
- Witnesses: `ScholiumD.jko_step_freeEnergy_le`, `ScholiumD.jko_step_transport_cost_le_energy_drop`
- Countermodels: none
- Formal boundary: Discrete metric-gradient kernel: the JKO minimizer's scaled squared transport displacement is bounded by its free-energy drop, and free energy cannot increase. Construction of P(M), the Wasserstein-2 metric, tangent continuity equations, and identification with the Fokker-Planck PDE remain open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The Fokker-Planck equation (Thm. theorem:bk1_fundamental_relation_fokker_plank_equation) describes the gradient flow of free-energy functional $F[rho]$ (Thm. theorem:bk1_variational_principle) on space $P(M)$ from Def. definition:bk1_symbolic_information_geometry, equipped with Wasserstein metric $W_2$:
\[
partial_s rho = -text{grad}_{W_2} F[rho]
\]
as summarized by thm. theorem:bk1_the_fokker_planck_equation_theorem and proof proof:bk1_sketch_gradient_flow_thermodynamics.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Wasserstein Geometric Interpretation]
\label{corollary:bk1_wasserstein_geometric_interpretation}
\leavevmode\newline
The Fokker-Planck equation (Thm.~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}) describes the gradient flow of free-energy functional $F[\rho]$ (Thm.~\ref{theorem:bk1_variational_principle}) on space $\mathcal{P}(M)$ from Def.~\ref{definition:bk1_symbolic_information_geometry}, equipped with Wasserstein metric $W_2$:
\[
\partial_s \rho = -\text{grad}_{W_2} F[\rho]
\]
as summarized by thm.~\ref{theorem:bk1_the_fokker_planck_equation_theorem} and proof~\ref{proof:bk1_sketch_gradient_flow_thermodynamics}.
\end{corollary}
```

### Restatement of the Wasserstein Gradient-Flow Theorem (`proof:bk1_wasserstein_geometric_interpretation`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3898`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_symbolic_information_geometry` (Symbolic Information Geometry); `proof:bk1_sketch_gradient_flow_thermodynamics` (Gradient Flow Structure via JKO); `theorem:bk1_the_fokker_planck_equation_theorem` (Information Geometric Interpretation)
- Cites: `definition:bk1_symbolic_information_geometry` (Symbolic Information Geometry); `proof:bk1_sketch_gradient_flow_thermodynamics` (Gradient Flow Structure via JKO); `theorem:bk1_the_fokker_planck_equation_theorem` (Information Geometric Interpretation)
- Cited by: none
- Macros used: none

**Statement / Body**

Thm. theorem:bk1_the_fokker_planck_equation_theorem identifies the
symbolic Fokker-Planck equation with the gradient flow of the symbolic free
energy \(F[rho]\) on \(P(M)\). Proof proof:bk1_sketch_gradient_flow_thermodynamics
computes the \(W_2\)-gradient explicitly: with
\(delta F/deltarho=H+beta^{-1}(1+logrho)\), the Wasserstein gradient flow
is
\[
partial_srho
=-nablacdot\!bigl(rho(nabla H+beta^{-1}nablalogrho)bigr),
\]
which is the symbolic Fokker-Planck equation after substituting
\(D=-nabla H\). Hence the equation is precisely
\(partial_srho=-grad_{W_2}F[rho]\) on the probability space
of Def. definition:bk1_symbolic_information_geometry.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Restatement of the Wasserstein Gradient-Flow Theorem]
\label{proof:bk1_wasserstein_geometric_interpretation}
\leavevmode

Thm.~\ref{theorem:bk1_the_fokker_planck_equation_theorem} identifies the
symbolic Fokker--Planck equation with the gradient flow of the symbolic free
energy \(F[\rho]\) on \(\mathcal{P}(M)\). Proof~\ref{proof:bk1_sketch_gradient_flow_thermodynamics}
computes the \(W_2\)-gradient explicitly: with
\(\delta F/\delta\rho=H+\beta^{-1}(1+\log\rho)\), the Wasserstein gradient flow
is
\[
\partial_s\rho
=-\nabla\cdot\!\bigl(\rho(\nabla H+\beta^{-1}\nabla\log\rho)\bigr),
\]
which is the symbolic Fokker--Planck equation after substituting
\(D=-\nabla H\). Hence the equation is precisely
\(\partial_s\rho=-\operatorname{grad}_{W_2}F[\rho]\) on the probability space
of Def.~\ref{definition:bk1_symbolic_information_geometry}.
\end{proof}
```

### Cosmological Symbolization Functor (`definition:bk1_cosmological_symbolization_functor`)

Role: `definition` | Type: `definition` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3929`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer)
- Cited by: `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `scholium:bk1_cosmogenesis_proof_status` (Proof status of Cosmogenesis); `theorem:bk1_dual_horizon_cosmogenesis` (Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos})
- Macros used: none

**Statement / Body**

A cosmological symbolization functor is a structure-preserving assignment
\[
B_{cos}:
(M, g_{munu}, preceq, S_{therm})
longrightarrow
(S, D, R_{stab}, kappa, Omega)
\]
from Lorentzian causal-thermodynamic data-a spacetime $(M,g_{munu})$ with
causal order $preceq$ and thermodynamic entropy field $S_{therm}$-to
PS symbolic dynamics, such that:

- causal expansion maps to positive observer-visible generative flux,
$G_{O}(B_{cos} H_G)>0$;

- thermodynamic constraint maps to positive stabilizing flux, equivalently
negative symbolic curvature,
$C_{O}(B_{cos} H_D)>0$ with
$kappa(H_D)<0$;

- bounded causal patches map to bounded observer domains (Def. definition:bk1_bounded_observer);

- cofinal refinements preserve the ordinal emergence order $preceq$
(cf. the summable resolution-decay condition on cofinal $omega$-towers).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Cosmological Symbolization Functor]
\label{definition:bk1_cosmological_symbolization_functor}
A \emph{cosmological symbolization functor} is a structure-preserving assignment
\[
\mathcal{B}_{\mathrm{cos}}:
(M, g_{\mu\nu}, \preceq, S_{\mathrm{therm}})
\longrightarrow
(\mathcal{S}, D, R_{\mathrm{stab}}, \kappa, \Omega)
\]
from Lorentzian causal--thermodynamic data---a spacetime $(M,g_{\mu\nu})$ with
causal order $\preceq$ and thermodynamic entropy field $S_{\mathrm{therm}}$---to
PS symbolic dynamics, such that:
\begin{enumerate}
\item causal expansion maps to positive observer-visible generative flux,
$G_{\mathcal{O}}(\mathcal{B}_{\mathrm{cos}}\,\mathcal{H}_G)>0$;
\item thermodynamic constraint maps to positive stabilizing flux, equivalently
negative symbolic curvature,
$C_{\mathcal{O}}(\mathcal{B}_{\mathrm{cos}}\,\mathcal{H}_D)>0$ with
$\kappa(\mathcal{H}_D)<0$;
\item bounded causal patches map to bounded observer domains (Def.~\ref{definition:bk1_bounded_observer});
\item cofinal refinements preserve the ordinal emergence order $\preceq$
(cf.~the summable resolution-decay condition on cofinal $\omega$-towers).
\end{enumerate}
\end{definition}
```

### Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos} (`theorem:bk1_dual_horizon_cosmogenesis`)

Role: `theorem` | Type: `theorem` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3954`

- Proof status: `proven`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_cosmological_symbolization_functor` (Cosmological Symbolization Functor); `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `definition:bk2_symbolic_hamiltonian` (Symbolic Hamiltonian); `lemma:bk1_horizon_characterization` (Horizon Characterization); `proof:bk1_proof_of_dual_horizon_necessity_theorem` (Proof of Dual Horizon Necessity Theorem); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_variational_principle` (Variational Principle); `theorem:bk2_equilibrium_distribution` (Equilibrium Distribution); `theorem:bk3_membrane_stability_criteria` (Membrane Stability Criteria); `theorem:bk4_existence_of_symbolic_ident` (Existence of Symbolic Identity)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_cosmological_symbolization_functor` (Cosmological Symbolization Functor); `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: `corollary:bk1_event_horizon_identity_field` (Event Horizon Identity Field); `proof:bk1_event_horizon_identity_field` (Identity Field on the Symbolized Causal Patch); `proof:bk4_temporal_resolution_via_observer_bounded_reflection` (Temporal Resolution via Observer-Bounded Reflection)
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_B-018`
- Witnesses: `Atlas.dual_horizon_fractured`, `Atlas.no_single_geometry_for_dual_horizon`, `ScholiumD.dual_horizon_cosmogenesis_kernel`
- Countermodels: none
- Conditions: named next layers, deliberately not forced into the keystone: curvature as loop defect (discrete holonomy) and the appB resolution tower (P_lambda as graded complex, emergent smoothness as defects vanishing up the grading); pair-covering is the assembly hypothesis for the classical direction
- Formal boundary: Static geometric kernel: opposite-signed past/future curvature parameters are provably distinct, while the certified dual-horizon chart complex at positive observer resolution admits no single consistent geometry. The cosmological symbolization functor, causal spacetime evolution, bounded observer dynamics, Hamiltonian apparatus, and existence of the intervening domain remain open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

Let $(M, g_{munu})$ denote the spacetime manifold of our observable universe, and
suppose it admits a cosmological symbolization functor $B_{cos}$
(Def. definition:bk1_cosmological_symbolization_functor) carrying its
causal-thermodynamic data into symbolic dynamics $(S, D, R, kappa)$.
Suppose the following conditions hold:


- There exists a past boundary $H_G$ associated with rapid causal expansion (e.g., cosmological inflation or conformal past), such that the induced symbolic curvature satisfies $kappa(H_G) > 0$ (Def. definition:bk1_symbolic_riemann_tensor)


- There exists a future boundary $H_D$ associated with thermodynamic constraint (e.g., cosmological event horizon, black hole entropy bound, or heat death trajectory), such that $kappa(H_D) < 0$


- There exists a non-empty bounded domain $Omega subset M$ such that:
 \[
 Omega = { x in M mid H_G prec x prec H_D }
 \]
 and $Omega$ admits bounded observers (Def. definition:bk1_bounded_observer) undergoing symbolic drift $D$ (Def. definition:bk1_drift_field) and reflection $R$ (Def. definition:bk1_reflection_operator) within it

Then the image $B_{cos}(M,Omega)$ constitutes a dual-horizon symbolic manifold (Def. definition:bk1_symbolic_manifold) supporting reflexive emergence. In particular, conditional on the existence of $B_{cos}$ satisfying the clauses above, the image of our universe's causal-thermodynamic data satisfies the conditions of the Dual Horizon Necessity Theorem (Thm. theorem:bk1_dual_horizon_necessity_theorem), and the full PS dynamical apparatus-Hamiltonian, Fokker-Planck evolution, equilibrium, and identity carriers-is thereby instantiated on $Omega$.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos}]
\label{theorem:bk1_dual_horizon_cosmogenesis}
Let $(M, g_{\mu\nu})$ denote the spacetime manifold of our observable universe, and
suppose it admits a cosmological symbolization functor $\mathcal{B}_{\mathrm{cos}}$
(Def.~\ref{definition:bk1_cosmological_symbolization_functor}) carrying its
causal--thermodynamic data into symbolic dynamics $(\mathcal{S}, D, R, \kappa)$.
Suppose the following conditions hold:

\begin{enumerate}
    \item There exists a past boundary $\mathcal{H}_G$ associated with rapid causal expansion (e.g., cosmological inflation or conformal past), such that the induced symbolic curvature satisfies $\kappa(\mathcal{H}_G) > 0$ (Def.~\ref{definition:bk1_symbolic_riemann_tensor})

    \item There exists a future boundary $\mathcal{H}_D$ associated with thermodynamic constraint (e.g., cosmological event horizon, black hole entropy bound, or heat death trajectory), such that $\kappa(\mathcal{H}_D) < 0$

    \item There exists a non-empty bounded domain $\Omega \subset M$ such that:
    \[
    \Omega = \{ x \in M \mid \mathcal{H}_G \prec x \prec \mathcal{H}_D \}
    \]
    and $\Omega$ admits bounded observers (Def.~\ref{definition:bk1_bounded_observer}) undergoing symbolic drift $D$ (Def.~\ref{definition:bk1_drift_field}) and reflection $R$ (Def.~\ref{definition:bk1_reflection_operator}) within it
\end{enumerate}

Then the image $\mathcal{B}_{\mathrm{cos}}(M,\Omega)$ constitutes a \textbf{dual-horizon symbolic manifold} (Def.~\ref{definition:bk1_symbolic_manifold}) supporting reflexive emergence. In particular, conditional on the existence of $\mathcal{B}_{\mathrm{cos}}$ satisfying the clauses above, the image of our universe's causal--thermodynamic data satisfies the conditions of the \textbf{Dual Horizon Necessity Theorem} (Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem}), and the full PS dynamical apparatus---Hamiltonian, Fokker--Planck evolution, equilibrium, and identity carriers---is thereby instantiated on $\Omega$.
\end{theorem}
```

### Cosmogenesis via Dual Horizon Necessity (`proof:bk1_sketch_observed_consequences`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:3977`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_cosmological_symbolization_functor` (Cosmological Symbolization Functor); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `definition:bk2_symbolic_hamiltonian` (Symbolic Hamiltonian); `lemma:bk1_horizon_characterization` (Horizon Characterization); `proof:bk1_proof_of_dual_horizon_necessity_theorem` (Proof of Dual Horizon Necessity Theorem); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_variational_principle` (Variational Principle); `theorem:bk2_equilibrium_distribution` (Equilibrium Distribution); `theorem:bk3_membrane_stability_criteria` (Membrane Stability Criteria); `theorem:bk4_existence_of_symbolic_ident` (Existence of Symbolic Identity)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_cosmological_symbolization_functor` (Cosmological Symbolization Functor); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_riemann_tensor` (Symbolic Riemann Curvature Tensor); `definition:bk2_symbolic_hamiltonian` (Symbolic Hamiltonian); `lemma:bk1_horizon_characterization` (Horizon Characterization); `proof:bk1_proof_of_dual_horizon_necessity_theorem` (Proof of Dual Horizon Necessity Theorem); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem); `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_variational_principle` (Variational Principle); `theorem:bk2_equilibrium_distribution` (Equilibrium Distribution); `theorem:bk3_membrane_stability_criteria` (Membrane Stability Criteria); `theorem:bk4_existence_of_symbolic_ident` (Existence of Symbolic Identity)
- Cited by: `corollary:bk1_event_horizon_identity_field` (Event Horizon Identity Field); `proof:bk1_event_horizon_identity_field` (Identity Field on the Symbolized Causal Patch)
- Macros used: none

**Statement / Body**

The proof proceeds in two stages: instantiation (exhibiting the
cosmological symbolization functor $B_{cos}$ of
Def. definition:bk1_cosmological_symbolization_functor on the relevant
cosmological data) and deduction (invoking established theorems to derive
the conclusion on its image). Stages 1-3 below verify the defining clauses of
$B_{cos}$ one by one.

textbf{Stage I: Instantiation of conditions (construction of $B_{cos}$).}

1. Generative boundary ($kappa > 0$).enspace
Inflationary cosmology posits that early spacetime underwent rapid exponential expansion, producing particle horizon separation and structure formation. The divergent lightcone geometry and monotonically increasing entropy potential define a generative horizon $H_G$ with $kappa(H_G) > 0$ (Def. definition:bk1_symbolic_riemann_tensor): the positive curvature encodes novelty-generation, as the expanding causal volume continuously introduces new degrees of freedom.

2. Dissipative boundary ($kappa < 0$).enspace
The future conformal boundary-whether manifesting as heat death, black hole final states, or a cosmological de Sitter horizon-imposes increasing thermodynamic constraint and entropic dilution. The converging lightcone geometry defines a dissipative horizon $H_D$ with $kappa(H_D) < 0$: the negative curvature encodes coherence-constraining dynamics (Def. definition:bk1_reflection_operator).

3. Bounded emergent domain.enspace
Our causal patch lies strictly between these boundaries. All known life, cognition, and symbolic systems occur within $Omega = {x in M mid H_G prec x prec H_D}$. This domain admits bounded observers (Def. definition:bk1_bounded_observer): any physical agent has finite resolution, finite memory, and finite processing capacity relative to the information content of $Omega$.

Stage II: Deduction from PS infrastructure.

4. Dual Horizon Necessity.enspace
Conditions (1)-(3) supply a symbolic universe $U = (M, Omega)$ with both a generative horizon $H_G$ ($kappa > 0$) and a dissipative horizon $H_D$ ($kappa < 0$) bounding a non-empty observer domain. By the Dual Horizon Necessity Theorem (Thm. theorem:bk1_dual_horizon_necessity_theorem), this gives the minimal effective signature for bounded reflexive emergence: Proof proof:bk1_proof_of_dual_horizon_necessity_theorem shows that any observer-visible configuration lacking either positive generative flux or negative stabilizing flux fails to achieve the complexity differential $DeltaPhi_{O}(D, R_{stab}) geq tau_E$.

5. Dynamical apparatus.enspace
Given the dual-horizon structure on $Omega$, the PS results chain as follows:


- The drift field $D$ and state-level stabilization \(R_{stab}\) emerge on $Omega$ as limits of proto-fields and stabilization operators (Thm. theorem:bk1_emergence_of_drift_field, Thm. theorem:bk1_emergence_of_reflection_operator), with $nabla cdot D > 0$ near $H_G$ and positive stabilization flux \(C_{O}(H_D)>0\) near $H_D$ (Lemma lemma:bk1_horizon_characterization).

- Their interplay defines the symbolic Hamiltonian (Def. definition:bk2_symbolic_hamiltonian), $H(x) = kappa / (\|D(x)\| + epsilon) + lambda cdot tr(L_x)$, which governs the energy landscape on $Omega$.

- The Fokker-Planck equation $partial_s rho = -nabla cdot (rho D) + sigma^2 nabla^2 rho$ (Thm. theorem:bk1_fundamental_relation_fokker_plank_equation) determines probability evolution under drift-diffusion dynamics.

- Equilibrium $rho_{eq} propto e^{-beta H}$ is the unique stationary distribution (Thm. theorem:bk2_equilibrium_distribution), and the free energy functional $F_beta[rho]$ provides the variational principle (Thm. theorem:bk1_variational_principle).

- Within $Omega$, bounded observers satisfying the stability conditions of Thm. theorem:bk3_membrane_stability_criteria support symbolic identity carriers (Thm. theorem:bk4_existence_of_symbolic_ident), completing the chain from cosmological boundary conditions to reflexive emergence.

6. Conclusion.enspace
The image $B_{cos}(M,Omega)$ satisfies all hypotheses of the Dual Horizon Necessity Theorem, and the deductive chain (a)-(e) instantiates the full PS dynamical apparatus on $Omega$. Reflexive emergence is not merely compatible with the symbolized causal architecture-it is entailed by it, conditional on the empirical conditions (1)-(3) and the bridge functor $B_{cos}$.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Cosmogenesis via Dual Horizon Necessity]
\label{proof:bk1_sketch_observed_consequences}
\leavevmode

The proof proceeds in two stages: \emph{instantiation} (exhibiting the
cosmological symbolization functor $\mathcal{B}_{\mathrm{cos}}$ of
Def.~\ref{definition:bk1_cosmological_symbolization_functor} on the relevant
cosmological data) and \emph{deduction} (invoking established theorems to derive
the conclusion on its image). Stages~1--3 below verify the defining clauses of
$\mathcal{B}_{\mathrm{cos}}$ one by one.

\medskip
\textbf{Stage I: Instantiation of conditions (construction of $\mathcal{B}_{\mathrm{cos}}$).}

\textbf{1. Generative boundary ($\kappa > 0$).}\enspace
Inflationary cosmology posits that early spacetime underwent rapid exponential expansion, producing particle horizon separation and structure formation. The divergent lightcone geometry and monotonically increasing entropy potential define a generative horizon $\mathcal{H}_G$ with $\kappa(\mathcal{H}_G) > 0$ (Def.~\ref{definition:bk1_symbolic_riemann_tensor}): the positive curvature encodes novelty-generation, as the expanding causal volume continuously introduces new degrees of freedom.

\textbf{2. Dissipative boundary ($\kappa < 0$).}\enspace
The future conformal boundary---whether manifesting as heat death, black hole final states, or a cosmological de Sitter horizon---imposes increasing thermodynamic constraint and entropic dilution. The converging lightcone geometry defines a dissipative horizon $\mathcal{H}_D$ with $\kappa(\mathcal{H}_D) < 0$: the negative curvature encodes coherence-constraining dynamics (Def.~\ref{definition:bk1_reflection_operator}).

\textbf{3. Bounded emergent domain.}\enspace
Our causal patch lies strictly between these boundaries. All known life, cognition, and symbolic systems occur within $\Omega = \{x \in M \mid \mathcal{H}_G \prec x \prec \mathcal{H}_D\}$. This domain admits bounded observers (Def.~\ref{definition:bk1_bounded_observer}): any physical agent has finite resolution, finite memory, and finite processing capacity relative to the information content of $\Omega$.

\medskip
\textbf{Stage II: Deduction from PS infrastructure.}

\textbf{4. Dual Horizon Necessity.}\enspace
Conditions (1)--(3) supply a symbolic universe $\mathcal{U} = (M, \Omega)$ with both a generative horizon $\mathcal{H}_G$ ($\kappa > 0$) and a dissipative horizon $\mathcal{H}_D$ ($\kappa < 0$) bounding a non-empty observer domain. By the Dual Horizon Necessity Theorem (Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem}), this gives the minimal effective signature for bounded reflexive emergence: Proof~\ref{proof:bk1_proof_of_dual_horizon_necessity_theorem} shows that any observer-visible configuration lacking either positive generative flux or negative stabilizing flux fails to achieve the complexity differential $\Delta\Phi_{\mathcal{O}}(D, R_{\mathrm{stab}}) \geq \tau_E$.

\textbf{5. Dynamical apparatus.}\enspace
Given the dual-horizon structure on $\Omega$, the PS results chain as follows:
\begin{enumerate}
    \item[\emph{(a)}] The drift field $D$ and state-level stabilization \(R_{\mathrm{stab}}\) emerge on $\Omega$ as limits of proto-fields and stabilization operators (Thm.~\ref{theorem:bk1_emergence_of_drift_field}, Thm.~\ref{theorem:bk1_emergence_of_reflection_operator}), with $\nabla \cdot D > 0$ near $\mathcal{H}_G$ and positive stabilization flux \(C_{\mathcal{O}}(\mathcal{H}_D)>0\) near $\mathcal{H}_D$ (Lemma~\ref{lemma:bk1_horizon_characterization}).
    \item[\emph{(b)}] Their interplay defines the symbolic Hamiltonian (Def.~\ref{definition:bk2_symbolic_hamiltonian}), $H(x) = \kappa / (\|D(x)\| + \epsilon) + \lambda \cdot \mathrm{tr}(L_x)$, which governs the energy landscape on $\Omega$.
    \item[\emph{(c)}] The Fokker--Planck equation $\partial_s \rho = -\nabla \cdot (\rho D) + \sigma^2 \nabla^2 \rho$ (Thm.~\ref{theorem:bk1_fundamental_relation_fokker_plank_equation}) determines probability evolution under drift--diffusion dynamics.
    \item[\emph{(d)}] Equilibrium $\rho_{\mathrm{eq}} \propto e^{-\beta H}$ is the unique stationary distribution (Thm.~\ref{theorem:bk2_equilibrium_distribution}), and the free energy functional $F_\beta[\rho]$ provides the variational principle (Thm.~\ref{theorem:bk1_variational_principle}).
    \item[\emph{(e)}] Within $\Omega$, bounded observers satisfying the stability conditions of Thm.~\ref{theorem:bk3_membrane_stability_criteria} support symbolic identity carriers (Thm.~\ref{theorem:bk4_existence_of_symbolic_ident}), completing the chain from cosmological boundary conditions to reflexive emergence.
\end{enumerate}

\textbf{6. Conclusion.}\enspace
The image $\mathcal{B}_{\mathrm{cos}}(M,\Omega)$ satisfies all hypotheses of the Dual Horizon Necessity Theorem, and the deductive chain (a)--(e) instantiates the full PS dynamical apparatus on $\Omega$. Reflexive emergence is not merely compatible with the symbolized causal architecture---it is entailed by it, conditional on the empirical conditions (1)--(3) and the bridge functor $\mathcal{B}_{\mathrm{cos}}$.
\end{proof}
```

### remark:scholium_symbolicum.tex:4019 (`remark:scholium_symbolicum.tex:4019`)

Role: `remark` | Type: `remark` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:4019`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

This establishes the conditional physical-sector claim: if our universe admits the cosmological symbolization functor above, then its causal structure is not merely compatible with symbolic emergence-its symbolized image necessitates it. Reflexive observers exist not in arbitrary spacetime, but in a symbolic membrane stretched between $H_G$ and $H_D$.

**Verbatim LaTeX Body**

```latex
\begin{remark}
This establishes the conditional physical-sector claim: if our universe admits the cosmological symbolization functor above, then its causal structure is not merely compatible with symbolic emergence---its symbolized image necessitates it. Reflexive observers exist not in arbitrary spacetime, but in a symbolic membrane stretched between $\mathcal{H}_G$ and $\mathcal{H}_D$.
\end{remark}
```

### Proof status of Cosmogenesis (`scholium:bk1_cosmogenesis_proof_status`)

Role: `scholium` | Type: `scholium` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:4023`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_cosmological_symbolization_functor` (Cosmological Symbolization Functor); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `definition:bk1_cosmological_symbolization_functor` (Cosmological Symbolization Functor); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: none
- Macros used: none

**Statement / Body**

The theorem is unconditional as mathematics: given any cosmological
symbolization functor $B_{cos}$
(Def. definition:bk1_cosmological_symbolization_functor) satisfying its four
clauses, the image is a dual-horizon symbolic manifold and the full PS apparatus
applies, by Dual Horizon Necessity
(Thm. theorem:bk1_dual_horizon_necessity_theorem). What is empirical,
and what Stage I argues from inflationary and thermodynamic cosmology, is the
antecedent: that our actual spacetime supplies such a functor-that cosmic
expansion realizes positive generative flux and that the future thermodynamic
boundary realizes positive stabilizing flux. The theorem thus locates the open
question precisely: not ``is the conclusion proved'' (it is, conditionally) but
``does our universe instantiate $B_{cos}$.'' This is the
ordinal-symbolic posture-the unification theorem lives at the level of the
bridge functor; the physical-sector claim follows once the bridge is exhibited.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Proof status of Cosmogenesis]
\label{scholium:bk1_cosmogenesis_proof_status}
The theorem is unconditional \emph{as mathematics}: given any cosmological
symbolization functor $\mathcal{B}_{\mathrm{cos}}$
(Def.~\ref{definition:bk1_cosmological_symbolization_functor}) satisfying its four
clauses, the image is a dual-horizon symbolic manifold and the full PS apparatus
applies, by Dual Horizon Necessity
(Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem}). What is \emph{empirical},
and what Stage~I argues from inflationary and thermodynamic cosmology, is the
antecedent: that our actual spacetime supplies such a functor---that cosmic
expansion realizes positive generative flux and that the future thermodynamic
boundary realizes positive stabilizing flux. The theorem thus locates the open
question precisely: not ``is the conclusion proved'' (it is, conditionally) but
``does our universe instantiate $\mathcal{B}_{\mathrm{cos}}$.'' This is the
ordinal-symbolic posture---the unification theorem lives at the level of the
bridge functor; the physical-sector claim follows once the bridge is exhibited.
\end{scholium}
```

### Event Horizon Identity Field (`corollary:bk1_event_horizon_identity_field`)

Role: `corollary` | Type: `corollary` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:4040`

- Proof status: `proven`
- Depends on: `corollary:bk1_wasserstein_geometric_interpretation` (Wasserstein Geometric Interpretation); `definition:bk1_bounded_observer` (Bounded Observer); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `theorem:bk1_dual_horizon_cosmogenesis` (Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos}); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem); `theorem:bk1_dual_horizon_unification_principle` (Emergent Dual Horizon Unification Principle)
- Cites: `corollary:bk1_wasserstein_geometric_interpretation` (Wasserstein Geometric Interpretation); `definition:bk1_bounded_observer` (Bounded Observer); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `theorem:bk1_dual_horizon_cosmogenesis` (Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos}); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem); `theorem:bk1_dual_horizon_unification_principle` (Emergent Dual Horizon Unification Principle)
- Cited by: none
- Macros used: none

### Lean correspondence

- Status: `open_bridge`
- Records: `MAP-SCHOLIUM_B-019`
- Witnesses: `Atlas.no_single_geometry_for_dual_horizon`, `ScholiumD.dual_horizon_cosmogenesis_kernel`, `ScholiumD.event_horizon_identity_field_kernel`
- Countermodels: none
- Conditions: named next layers, deliberately not forced into the keystone: curvature as loop defect (discrete holonomy) and the appB resolution tower (P_lambda as graded complex, emergent smoothness as defects vanishing up the grading); pair-covering is the assembly hypothesis for the classical direction
- Formal boundary: Static identity-field kernel: defining horizon tension as the past-minus-future curvature contrast, opposite curvature signs force strictly positive tension; at positive observer resolution the same hypotheses obstruct a single geometry reconciling the dual horizon. Construction and evolution of a spacetime identity field, observer measures, and the claimed physical interpretation remain open.

Manuscript `proof_status` and Lean correspondence are independent.

**Statement / Body**

The observed structure of cognition, memory, language, and thermodynamic complexity within $Omega$ (thm theorem:bk1_dual_horizon_cosmogenesis, proof proof:bk1_sketch_observed_consequences) constitutes an identity field induced by horizon tension, grounded in bounded observation (def definition:bk1_bounded_observer), dual-horizon necessity (thm theorem:bk1_dual_horizon_necessity_theorem), emergent dual-horizon unification (thm theorem:bk1_dual_horizon_unification_principle), and Wasserstein symbolic thermodynamic geometry (Cor. corollary:bk1_wasserstein_geometric_interpretation). Emergence is not a property of matter - it is a property of situated symbolic curvature.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Event Horizon Identity Field]
\label{corollary:bk1_event_horizon_identity_field}
The observed structure of cognition, memory, language, and thermodynamic complexity within $\Omega$ (thm~\ref{theorem:bk1_dual_horizon_cosmogenesis}, proof~\ref{proof:bk1_sketch_observed_consequences}) constitutes an identity field induced by horizon tension, grounded in bounded observation (def~\ref{definition:bk1_bounded_observer}), dual-horizon necessity (thm~\ref{theorem:bk1_dual_horizon_necessity_theorem}), emergent dual-horizon unification (thm~\ref{theorem:bk1_dual_horizon_unification_principle}), and Wasserstein symbolic thermodynamic geometry (Cor.~\ref{corollary:bk1_wasserstein_geometric_interpretation}). Emergence is not a property of matter - it is a property of situated symbolic curvature.
\end{corollary}
```

### Identity Field on the Symbolized Causal Patch (`proof:bk1_event_horizon_identity_field`)

Role: `proof` | Type: `proof` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:4044`

- Proof status: `not_applicable`
- Depends on: `corollary:bk1_wasserstein_geometric_interpretation` (Wasserstein Geometric Interpretation); `definition:bk1_bounded_observer` (Bounded Observer); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `theorem:bk1_dual_horizon_cosmogenesis` (Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos}); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem); `theorem:bk1_dual_horizon_unification_principle` (Emergent Dual Horizon Unification Principle)
- Cites: `corollary:bk1_wasserstein_geometric_interpretation` (Wasserstein Geometric Interpretation); `definition:bk1_bounded_observer` (Bounded Observer); `proof:bk1_sketch_observed_consequences` (Cosmogenesis via Dual Horizon Necessity); `theorem:bk1_dual_horizon_cosmogenesis` (Dual Horizon Cosmogenesis under \texorpdfstring{$\mathcal{B}_{\mathrm{cos}}$}{B\_cos}); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem); `theorem:bk1_dual_horizon_unification_principle` (Emergent Dual Horizon Unification Principle)
- Cited by: none
- Macros used: none

**Statement / Body**

Conditional on the cosmological symbolization functor
\(B_{cos}\), Thm. theorem:bk1_dual_horizon_cosmogenesis
and Proof proof:bk1_sketch_observed_consequences place the observer domain
\(Omega\) between a generative horizon and a dissipative horizon and instantiate
the PS dynamical apparatus there. Bounded observers in \(Omega\)
(Def. definition:bk1_bounded_observer) therefore experience cognition,
memory, language, and thermodynamic complexity as observer-relative symbolic
dynamics on the image of that causal patch.

Thm. theorem:bk1_dual_horizon_necessity_theorem supplies the necessity of
both horizon roles for bounded reflexive emergence, while
Thm. theorem:bk1_dual_horizon_unification_principle identifies the
projected dynamics as horizon-crossing reflexivity. Cor. corollary:bk1_wasserstein_geometric_interpretation
then supplies the thermodynamic geometry: symbolic probability evolves as a
Wasserstein gradient flow of free energy. The identity field is precisely the
stable observer-relative organization generated by these ingredients on
\(Omega\). Thus the corollary follows as a conditional statement about situated
symbolic curvature, not as an unconditional reduction of matter to emergence.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Identity Field on the Symbolized Causal Patch]
\label{proof:bk1_event_horizon_identity_field}
\leavevmode

Conditional on the cosmological symbolization functor
\(\mathcal{B}_{\mathrm{cos}}\), Thm.~\ref{theorem:bk1_dual_horizon_cosmogenesis}
and Proof~\ref{proof:bk1_sketch_observed_consequences} place the observer domain
\(\Omega\) between a generative horizon and a dissipative horizon and instantiate
the PS dynamical apparatus there. Bounded observers in \(\Omega\)
(Def.~\ref{definition:bk1_bounded_observer}) therefore experience cognition,
memory, language, and thermodynamic complexity as observer-relative symbolic
dynamics on the image of that causal patch.

Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem} supplies the necessity of
both horizon roles for bounded reflexive emergence, while
Thm.~\ref{theorem:bk1_dual_horizon_unification_principle} identifies the
projected dynamics as horizon-crossing reflexivity. Cor.~\ref{corollary:bk1_wasserstein_geometric_interpretation}
then supplies the thermodynamic geometry: symbolic probability evolves as a
Wasserstein gradient flow of free energy. The identity field is precisely the
stable observer-relative organization generated by these ingredients on
\(\Omega\). Thus the corollary follows as a conditional statement about situated
symbolic curvature, not as an unconditional reduction of matter to emergence.
\end{proof}
```

### Summary and Implications (`sec:bk1_summary_and_implications`)

Role: `section` | Type: `section` | Book: `scholium_symbolicum` | Source: `scholium_symbolicum.tex:4070`

- Proof status: `not_applicable`
- Depends on: `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_h_theorem_for_symbolic_evolution` (H-Theorem for Symbolic Evolution); `theorem:bk1_manifold_emergence` (Manifold Emergence); `theorem:bk1_princple_of_least_action` (Principle of Least Action); `theorem:bk1_sructurual_correspondence` (Structural Correspondence); `theorem:bk1_symbolic_fluctuation_dissipation_relation` (Symbolic Fluctuation–Dissipation Relation); `theorem:bk1_variational_principle` (Variational Principle)
- Cites: `theorem:bk1_emergence_of_drift_field` (Emergence of Drift Field); `theorem:bk1_emergence_of_reflection_operator` (Emergence of Stabilization Operator); `theorem:bk1_fundamental_relation_fokker_plank_equation` (Fundamental Relation – Fokker–Planck Equation); `theorem:bk1_h_theorem_for_symbolic_evolution` (H-Theorem for Symbolic Evolution); `theorem:bk1_manifold_emergence` (Manifold Emergence); `theorem:bk1_princple_of_least_action` (Principle of Least Action); `theorem:bk1_sructurual_correspondence` (Structural Correspondence); `theorem:bk1_symbolic_fluctuation_dissipation_relation` (Symbolic Fluctuation–Dissipation Relation); `theorem:bk1_variational_principle` (Variational Principle)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)
