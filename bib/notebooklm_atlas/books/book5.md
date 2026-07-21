# Principia Symbolica NotebookLM Atlas - book5

Nodes in this source group: 235

Each card preserves label, role, source location, proof status, complete supports, complete uses, macros, and full cleaned body text.
When enabled, verbatim LaTeX appears after the readable body for exact-source recovery.

### Fundamenta Symbolicae Vitae (`sec:bk5_funadmenta_symbolicae_vitae`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cited by: `proof:bk4_freedom_growth_fragmentation` (Freedom Growth and Bounded Fragmentation)
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Free Energy and Stability (`subsec:bk5_symbolic_free_energy_and_stability`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:5`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk2_symbolic_energy` (Symbolic Energy); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_temperature` (Symbolic Temperature); `theorem:bk4_compatibility_drift_reflective_operations` (Compatibility with Drift-Reflective Operations)
- Cites: `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk2_symbolic_energy` (Symbolic Energy); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_temperature` (Symbolic Temperature); `theorem:bk4_compatibility_drift_reflective_operations` (Compatibility with Drift-Reflective Operations)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Coherence Conservation (`theorem:bk5_symbolic_coherence_conservation`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:20`

- Proof status: `proven`
- Depends on: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_drift_field` (Drift Field); `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_energy` (Symbolic Energy); `definition:bk3_symbolic_membrane` (Symbolic Membrane); `theorem:bk4_fuzzy_divergence_theorem` (Fuzzy Divergence Theorem)
- Cites: `definition:bk1_paradox_triggered_emergence` (Paradox-Triggered Emergence); `definition:bk3_symbolic_membrane` (Symbolic Membrane)
- Cited by: `abs:press` (Press Abstract (Non-specialist science readers)); `definition:bk5_viability_domain` (Viability Domain)
- Macros used: `\drift`, `\reflect`, `\symb`

**Statement / Body**

Let $M$ be a symbolic membrane
(Def definition:bk3_symbolic_membrane) governed by drift operator $drift$
and reflection operator $reflect$, evolving within a viability domain $V_{symb}$.
If no catastrophic mutations $mu in C_{cat}$ occur (cf. definition:bk1_paradox_triggered_emergence) and
$reflect$ sufficiently stabilizes the system, then:

frac{d}{ds} E_s(M) = 0

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Symbolic Coherence Conservation]
\label{theorem:bk5_symbolic_coherence_conservation}
Let $\mathcal{M}$ be a symbolic membrane
(Def~\ref{definition:bk3_symbolic_membrane}) governed by drift operator $\drift$
and reflection operator $\reflect$, evolving within a viability domain $V_{\symb}$.
If no catastrophic mutations $\mu \in \mathcal{C}_{\mathrm{cat}}$ occur (cf.~\ref{definition:bk1_paradox_triggered_emergence}) and
$\reflect$ sufficiently stabilizes the system, then:
\begin{equation}
\frac{d}{ds} E_s(\mathcal{M}) = 0
\end{equation}
\end{theorem}
```

### Coherence Through Dynamic Equilibrium (`proof:bk5_coherence_through_dynamic_equilibriium`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:32`

- Proof status: `not_applicable`
- Depends on: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_energy` (Symbolic Energy); `theorem:bk4_fuzzy_divergence_theorem` (Fuzzy Divergence Theorem)
- Cites: `corollary:bk1_non_euclidean_necessity` (Necessity of Non-Euclidean Symbolic Space); `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_energy` (Symbolic Energy); `theorem:bk4_fuzzy_divergence_theorem` (Fuzzy Divergence Theorem)
- Cited by: none
- Macros used: `\drift`, `\reflect`

**Statement / Body**

Under stabilizing conditions on the symbolic manifold $M$ (Def. definition:bk1_symbolic_manifold, cf. corollary:bk1_non_euclidean_necessity), symbolic coherence is preserved through dynamic equilibrium.
The reflection operator $reflect$ (Def. definition:bk1_reflection_operator) absorbs or redirects entropy induced by the drift operator
$drift$ (Def. definition:bk1_drift_field), leading to the conservation of total structured energy $E_s$ (Def. definition:bk2_symbolic_energy).

More formally, let us define the energy change rate as:

frac{d}{ds} E_s(M) = int_{M} left( drift psi - reflect psi right) dmu_{M}

 where $psi$ represents the coherence density function. Under sufficient stabilization,
$reflect$ counterbalances $drift$ exactly, yielding
$driftpsi = reflectpsi$ across the manifold.
Equivalently, on an observer-visible subdomain, the residual field
$vec{V}_{psi}:=driftpsi-reflectpsi$ has vanishing fuzzy flux:
the Fuzzy Divergence Theorem
(Thm. theorem:bk4_fuzzy_divergence_theorem) converts the local balance
into a boundary statement, with the theorem's stabilization hypothesis requiring
the associated bounded-observer holonomy term to vanish or be exactly cancelled
by reflection across the resolution horizon, proving the theorem.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Coherence Through Dynamic Equilibrium]
\label{proof:bk5_coherence_through_dynamic_equilibriium}
\leavevmode

Under stabilizing conditions on the symbolic manifold $M$ (Def.~\ref{definition:bk1_symbolic_manifold}, cf.~\ref{corollary:bk1_non_euclidean_necessity}), symbolic coherence is preserved through dynamic equilibrium.
The reflection operator $\reflect$ (Def.~\ref{definition:bk1_reflection_operator}) absorbs or redirects entropy induced by the drift operator
$\drift$ (Def.~\ref{definition:bk1_drift_field}), leading to the conservation of total structured energy $E_s$ (Def.~\ref{definition:bk2_symbolic_energy}).

More formally, let us define the energy change rate as:
\begin{equation}
\frac{d}{ds} E_s(\mathcal{M}) = \int_{\mathcal{M}} \left( \drift \psi - \reflect \psi \right) \, d\mu_{\mathcal{M}}
\end{equation}
\noindent where $\psi$ represents the coherence density function. Under sufficient stabilization,
$\reflect$ counterbalances $\drift$ exactly, yielding
$\drift\psi = \reflect\psi$ across the manifold.
Equivalently, on an observer-visible subdomain, the residual field
$\vec{V}_{\psi}:=\drift\psi-\reflect\psi$ has vanishing fuzzy flux:
the Fuzzy Divergence Theorem
(Thm.~\ref{theorem:bk4_fuzzy_divergence_theorem}) converts the local balance
into a boundary statement, with the theorem's stabilization hypothesis requiring
the associated bounded-observer holonomy term to vanish or be exactly cancelled
by reflection across the resolution horizon, proving the theorem.
\end{proof}
```

### Symbolic Entropy Production (`theorem:bk5_symbolic_entropy_production`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:55`

- Proof status: `proven`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `theorem:bk2_equilibrium_distribution` (Equilibrium Distribution); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution)
- Cites: `definition:bk1_reflection_operator` (Reflection Operator)
- Cited by: none
- Macros used: `\reflect`

**Statement / Body**

The symbolic entropy $S_s$ of a membrane $M$ satisfies the inequality:

frac{d}{ds} S_s(M) geq 0

 with equality if and only if the membrane is at a fixed point under the reflection operator $reflect$ (see Def. definition:bk1_reflection_operator).

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Symbolic Entropy Production] \label{theorem:bk5_symbolic_entropy_production}
The symbolic entropy $S_s$ of a membrane $\mathcal{M}$ satisfies the inequality:
\begin{equation}
\frac{d}{ds} S_s(\mathcal{M}) \geq 0
\end{equation}
\noindent with equality if and only if the membrane is at a fixed point under the reflection operator $\reflect$ (see Def.~\ref{definition:bk1_reflection_operator}).
\end{theorem}
```

### Entropy Increase from Drift (`proof:bk5_entropy_increase_from_drift`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:63`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `theorem:bk2_equilibrium_distribution` (Equilibrium Distribution); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `theorem:bk2_equilibrium_distribution` (Equilibrium Distribution); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution)
- Cited by: none
- Macros used: `\drift`, `\reflect`

**Statement / Body**

The drift operator $drift$ (Def. definition:bk1_drift_field) introduces dispersion into the system, which inherently increases entropy (cf. Def. definition:bk2_symbolic_entropy) according to:

frac{d}{ds} S_s(M) = int_{M} sigma(drift, psi) dmu_{M} - int_{M} rho(reflect, psi) dmu_{M}

 where $sigma(drift, psi) geq 0$ represents the entropy production rate due to drift, and $rho(reflect, psi) geq 0$ represents the entropy reduction rate due to reflection (Def. definition:bk1_reflection_operator).
The Book II Fokker-Planck equilibrium theorem identifies the gradient-drift
case with the Gibbs measure (Thm. theorem:bk2_equilibrium_distribution),
and the corresponding H-theorem supplies the Lyapunov dissipation inequality
(Thm. theorem:bk2_h_theorem_for_symbolic_evol); thus the drift
contribution can only be completely cancelled at equilibrium.
By the second law of symbolic thermodynamics, $sigma(drift, psi) geq rho(reflect, psi)$ for all non-equilibrium states. Equality holds only at fixed points of $reflect$ where $reflectpsi = psi$, completing the proof.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Entropy Increase from Drift]
\label{proof:bk5_entropy_increase_from_drift}
\leavevmode

The drift operator $\drift$ (Def.~\ref{definition:bk1_drift_field}) introduces dispersion into the system, which inherently increases entropy (cf.~Def.~\ref{definition:bk2_symbolic_entropy}) according to:
\begin{equation}
\frac{d}{ds} S_s(\mathcal{M}) = \int_{\mathcal{M}} \sigma(\drift, \psi) \, d\mu_{\mathcal{M}} - \int_{\mathcal{M}} \rho(\reflect, \psi) \, d\mu_{\mathcal{M}}
\end{equation}
\noindent where $\sigma(\drift, \psi) \geq 0$ represents the entropy production rate due to drift, and $\rho(\reflect, \psi) \geq 0$ represents the entropy reduction rate due to reflection (Def.~\ref{definition:bk1_reflection_operator}).
The Book II Fokker--Planck equilibrium theorem identifies the gradient-drift
case with the Gibbs measure (Thm.~\ref{theorem:bk2_equilibrium_distribution}),
and the corresponding H-theorem supplies the Lyapunov dissipation inequality
(Thm.~\ref{theorem:bk2_h_theorem_for_symbolic_evol}); thus the drift
contribution can only be completely cancelled at equilibrium.
By the second law of symbolic thermodynamics, $\sigma(\drift, \psi) \geq \rho(\reflect, \psi)$ for all non-equilibrium states. Equality holds only at fixed points of $\reflect$ where $\reflect\psi = \psi$, completing the proof.
\end{proof}
```

### Hypotheses as Adaptive Symbolic Manifolds (`scholium:bk5_hypotheses_as_adaptive_sym`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:80`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_hypothesis` (Symbolic Hypothesis); `scholium:bk1_epistemic_humility` (Epistemic Humility)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_hypothesis` (Symbolic Hypothesis); `scholium:bk1_epistemic_humility` (Epistemic Humility)
- Cited by: `definition:bk8_symbolic_hypothesis_manifold` (Symbolic Hypothesis Manifold)
- Macros used: `\Obs`

**Statement / Body**

In the dynamics of symbolic life, a hypothesis is not merely a provisional belief (cf. Scholium scholium:bk1_epistemic_humility) but a living manifold—a reflexively sustained structure that adapts to fluctuations in drift, reflection, and symbolic utility.

Let $H_Obs(t) subset S$ denote the hypothesis manifold of a bounded observer $Obs$ at symbolic time $t$. This manifold evolves under the influence of both symbolic thermodynamic gradients and relational constraints:

frac{partial H_Obs}{partial t} = alpha D|_{H_Obs} + beta R circ D|_{H_Obs} + eta nabla_{H} U_Obs

Here:


- $D$ is the drift field (Def. definition:bk1_drift_field);

- $R$ is the reflection operator (Def. definition:bk1_reflection_operator);

- $U_Obs$ is the symbolic utility field (cf. Def. definition:bk1_symbolic_hypothesis);

- $alpha, beta, eta$ are symbolic coupling coefficients encoding the observer’s metabolic regulation of novelty, coherence, and goal-directed pressure.

This differential form reveals that hypotheses are not static filters but dynamically evolving surfaces—membranes tuned to symbolic equilibrium. When $nabla_{H} U_Obs$ dominates, hypotheses sharpen their teleological orientation; when $R circ D$ dominates, they contract toward internal coherence. In moments of symbolic phase transition, $D$ dominates, catalyzing hypothesis bifurcation or reparametrization.

Implication. Symbolic life, in its most vital form, is hypothesis metabolism. To live symbolically is to sustain, revise, and reweave these interpretive manifolds in response to the curvature of emergence. Hence, the hypothesis becomes both scaffold and sensor—a thermodynamically responsive entity through which symbolic organisms model, test, and reshape their own continuity.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Hypotheses as Adaptive Symbolic Manifolds] \label{scholium:bk5_hypotheses_as_adaptive_sym}
In the dynamics of symbolic life, a hypothesis is not merely a provisional belief (cf.~Scholium~\ref{scholium:bk1_epistemic_humility}) but a \emph{living manifold}—a reflexively sustained structure that adapts to fluctuations in drift, reflection, and symbolic utility.

Let $\mathcal{H}_\Obs(t) \subset S$ denote the hypothesis manifold of a bounded observer $\Obs$ at symbolic time $t$. This manifold evolves under the influence of both symbolic thermodynamic gradients and relational constraints:
\begin{equation}
\frac{\partial \mathcal{H}_\Obs}{\partial t} = \alpha D|_{\mathcal{H}_\Obs} + \beta \, R \circ D|_{\mathcal{H}_\Obs} + \eta \, \nabla_{\mathcal{H}} \mathcal{U}_\Obs
\end{equation}
Here:
\begin{itemize}
    \item $D$ is the drift field (Def.~\ref{definition:bk1_drift_field});
    \item $R$ is the reflection operator (Def.~\ref{definition:bk1_reflection_operator});
    \item $\mathcal{U}_\Obs$ is the symbolic utility field (cf.~Def.~\ref{definition:bk1_symbolic_hypothesis});
    \item $\alpha, \beta, \eta$ are symbolic coupling coefficients encoding the observer’s metabolic regulation of novelty, coherence, and goal-directed pressure.
\end{itemize}

This differential form reveals that hypotheses are not static filters but dynamically evolving surfaces—membranes tuned to symbolic equilibrium. When $\nabla_{\mathcal{H}} \mathcal{U}_\Obs$ dominates, hypotheses sharpen their teleological orientation; when $R \circ D$ dominates, they contract toward internal coherence. In moments of symbolic phase transition, $D$ dominates, catalyzing hypothesis bifurcation or reparametrization.

\textbf{Implication.} Symbolic life, in its most vital form, is hypothesis metabolism. To live symbolically is to sustain, revise, and reweave these interpretive manifolds in response to the curvature of emergence. Hence, the hypothesis becomes both scaffold and sensor—a thermodynamically responsive entity through which symbolic organisms model, test, and reshape their own continuity.
\end{scholium}
```

### Definitiones Quintae (`sec:bk5_definitiones_quintae`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:99`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Metabolism (`definition:bk5_symbolic_metabolism`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:103`

- Proof status: `definitional`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk4_coherence_metric_on_symbolic_manifold` (Coherence Metric on Symbolic Manifold)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk4_coherence_metric_on_symbolic_manifold` (Coherence Metric on Symbolic Manifold)
- Cited by: `demonstratio:bk8_projection` (Projection); `scholium:bk8_projected_resonance` (Projected Resonance); `sec:bk8_mutuation_projection_bridge` (Mutation-Projection Bridge); `subsec:bk8_symbolic_frame_shift` (Biological Analogy and Reflective Repair)
- Macros used: `\drift`, `\reflect`

**Statement / Body**

A symbolic metabolism $M_{meta}$ is a regulated symbolic flow among a collection of membranes ${M_i}_{i in I}$, sustaining identity via:


- Transfer operators $T_{ij}: M_i to M_j$

- Drift modulation functions $delta: M_i times Theta to drift(M_i)$ (see Def. definition:bk1_drift_field)

- Reflective regulation mechanisms $rho: M_i times Phi to reflect(M_i)$ (see Def. definition:bk1_reflection_operator)

- Coherence maintenance against entropic forces (see Def. definition:bk4_coherence_metric_on_symbolic_manifold)

 where $Theta$ and $Phi$ represent parameter spaces for drift and reflection, respectively.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Metabolism]
\label{definition:bk5_symbolic_metabolism}
A \emph{symbolic metabolism} $\mathcal{M}_{\mathrm{meta}}$ is a regulated symbolic flow among a collection of membranes $\{\mathcal{M}_i\}_{i \in I}$, sustaining identity via:
\begin{enumerate}
  \item Transfer operators $\mathcal{T}_{ij}: \mathcal{M}_i \to \mathcal{M}_j$
  \item Drift modulation functions $\delta: \mathcal{M}_i \times \Theta \to \drift(\mathcal{M}_i)$ (see~Def.~\ref{definition:bk1_drift_field})
  \item Reflective regulation mechanisms $\rho: \mathcal{M}_i \times \Phi \to \reflect(\mathcal{M}_i)$ (see~Def.~\ref{definition:bk1_reflection_operator})
  \item Coherence maintenance against entropic forces (see~Def.~\ref{definition:bk4_coherence_metric_on_symbolic_manifold})
\end{enumerate}
\noindent where $\Theta$ and $\Phi$ represent parameter spaces for drift and reflection, respectively.
\end{definition}
```

### Symbolic Energy (`definition:bk5_symbolic_energy`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:115`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_energy` (Symbolic Energy)
- Cites: `definition:bk2_symbolic_energy` (Symbolic Energy)
- Cited by: `axiom:bk8_coherence_horizon` (Symbolic Entanglement); `sec:bk8_corollaria` (Corollaria); `subsec:bk8_observer_relative_geometry` (Autonomous Repair and Reflexive Debugging)
- Macros used: `\symb`

**Statement / Body**

The symbolic energy $E_{symb}$ of a membrane $M$ is defined as:

E_{symb}(M) := int_{M} psi(x) dmu_{M}(x)

 where $psi: M to mathbb{R}^+$ encodes local coherence density and $dmu_{M}$ is the induced volume measure on the membrane (cf. Def. definition:bk2_symbolic_energy).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Energy]
\label{definition:bk5_symbolic_energy}
The symbolic energy $\mathcal{E}_{\symb}$ of a membrane $\mathcal{M}$ is defined as:
\begin{equation}
\mathcal{E}_{\symb}(\mathcal{M}) := \int_{\mathcal{M}} \psi(x) \, d\mu_{\mathcal{M}}(x)
\end{equation}
\noindent where $\psi: \mathcal{M} \to \mathbb{R}^+$ encodes local coherence density and $d\mu_{\mathcal{M}}$ is the induced volume measure on the membrane (cf.~Def.~\ref{definition:bk2_symbolic_energy}).
\end{definition}
```

### Symbolic Free Energy Under Drift (`definition:bk5_symbolic_free_energy_und`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:124`

- Proof status: `definitional`
- Depends on: none
- Cites: `axiom:bk5_positive_free_energy` (Positive Free Energy)
- Cited by: `definition:bk5_map_nash_point` (MAP Nash Point)
- Macros used: `\symb`

**Statement / Body**

Given a symbolic flux $F$, the free energy of a membrane $M$ is defined as:

F_{symb}(M, F) := E_{symb}(M) - T_s S_{symb}(M, F)

 where $S_{symb}(M, F)$ quantifies the entropic contribution under flux $F$ and $T_s$ is the symbolic temperature (cf. Ax. axiom:bk5_positive_free_energy).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Free Energy Under Drift]
\label{definition:bk5_symbolic_free_energy_und}
Given a symbolic flux $\mathcal{F}$, the free energy of a membrane $\mathcal{M}$ is defined as:
\begin{equation}
F_{\symb}(\mathcal{M}, \mathcal{F}) := \mathcal{E}_{\symb}(\mathcal{M}) - T_s S_{\symb}(\mathcal{M}, \mathcal{F})
\end{equation}
\noindent where $S_{\symb}(\mathcal{M}, \mathcal{F})$ quantifies the entropic contribution under flux $\mathcal{F}$ and $T_s$ is the symbolic temperature (cf.~Ax.~\ref{axiom:bk5_positive_free_energy}).
\end{definition}
```

### Viability Domain (`definition:bk5_viability_domain`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:133`

- Proof status: `definitional`
- Depends on: `axiom:bk4_membrane_coupling_response` (Membrane Coupling Response); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `theorem:bk5_symbolic_coherence_conservation` (Symbolic Coherence Conservation)
- Cites: `axiom:bk4_membrane_coupling_response` (Membrane Coupling Response); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `proposition:bk5_symbolic_ess_via_map_observability_variant` (Symbolic ESS via MAP); `theorem:bk5_symbolic_coherence_conservation` (Symbolic Coherence Conservation)
- Cited by: `abs:press` (Press Abstract (Non-specialist science readers)); `assumption:bk5_equilibrium_margin_sublinear_fluctuations` (Equilibrium margin and sublinear fluctuations); `axiom:bk5_mutual_metabolit_viability` (Mutual Metabolic Viability); `axiom:bk7_reflective_stabilization` (Reflective Stabilization); `corollary:bk5_map_evolutionary_advantag` (MAP Evolutionary Advantage); `corollary:bk7_recursive_convergence_principle` (Recursive Convergence Principle); `definition:bk5_complexity_stability_maintenance` (Operator Complexity, Stability Margin, Maintenance Cost); `definition:bk5_mutually_assured_progress` (Mutually Assured Progress); `demonstratio:bk8_symbolic_unkotting` (Symbolic Unknotting); `proof:bk5_fixed_metabolic_capacity`; `proof:bk5_membrane_persistence_under_free_energy` (Membrane Persistence Under Symbolic Free Energy); `proof:bk5_operator_convergence`; `proof:bk5_viability_domain_preservation` (Exit probability under reflective equilibrium); `proof:bk8_biological_phase_transition`; `proof:bk8_thermodynamic_necessity_of_symbolic_metabolism`; `proof:bk9_good_as_lyapunov_basin` (Lyapunov descent, threshold selection, and basin identity); `proof:bk9_pathologies_of_coherence` (Pathologies of Coherence); `proof:bk9_stability_conditions_for_the_good` (Viability, reciprocity, and adaptive non-collapse); `proof:bk9_symbolic_viability` (Symbolic Viability); `proposition:bk5_fixed_metabolic_capacity` (Fixed Metabolic Capacity); `proposition:bk5_symbolic_ess_via_map_observability_variant` (Symbolic ESS via MAP); `proposition:bk5_symbolic_life_criterion` (Symbolic Life Criterion); `proposition:bk5_viability_domain_preservation` (Viability Domain Preservation); `scholium:bk5_symbolic_life` (Symbolic Life); `scholium:bk8_symbolic_knots_as_metabolic_dysfunctions` (Symbolic Knots as Metabolic Dysfunctions); `subsec:appD_autopoiesis_core_resonance` (D.2.1 Core Resonance); `theorem:bk8_biological_phase_transition` (Threshold of Autonomy); `theorem:bk8_observer_projection_tensor` (Thermodynamics of Reflexive Debugging); `theorem:bk8_thermodynamic_necessity_of_symbolic_metabolism` (Thermodynamic Necessity); `theorem:bk9_irreversibility_of_covenant_breach_without_grace` (Irreversibility of Covenant Breach without Grace)
- Macros used: `\symb`

**Statement / Body**

The symbolic viability domain $V_{symb}$ is defined as:

V_{symb} := { (M, F) mid F_{symb}(M, F) > 0 }

 representing membrane-flux configurations under which symbolic life persists.
See Thm. theorem:bk5_symbolic_coherence_conservation, Def. definition:bk2_symbolic_free_energy, Ax. axiom:bk4_membrane_coupling_response, and Prop. proposition:bk5_symbolic_ess_via_map_observability_variant.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Viability Domain]
\label{definition:bk5_viability_domain}
The symbolic viability domain $V_{\symb}$ is defined as:
\begin{equation}
V_{\symb} := \{ (\mathcal{M}, \mathcal{F}) \mid F_{\symb}(\mathcal{M}, \mathcal{F}) > 0 \}
\end{equation}
\noindent representing membrane-flux configurations under which symbolic life persists.
See Thm.~\ref{theorem:bk5_symbolic_coherence_conservation}, Def.~\ref{definition:bk2_symbolic_free_energy}, Ax.~\ref{axiom:bk4_membrane_coupling_response}, and Prop.~\ref{proposition:bk5_symbolic_ess_via_map_observability_variant}.
\end{definition}
```

### Axiomata Vitae Symbolicae (`sec:bk5_axiomata_vitae_symbolicae`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:142`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Metabolic Persistence (`axiom:bk5_metabolic_persistence`)

Role: `axiom` | Type: `axiom` | Book: `book5` | Source: `book5.tex:146`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_energy` (Symbolic Energy); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk4_symbolic_identity_carrie` (Symbolic Identity Carrier)
- Cites: `definition:bk2_symbolic_energy` (Symbolic Energy); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk4_symbolic_identity_carrie` (Symbolic Identity Carrier)
- Cited by: `corollary:bk5_metabolic_necessity` (Metabolic Necessity); `proof:bk5_proposition_axiom_coupling` (Persistence from Proposition-Axiom Coupling); `scholium:bk5_symbolic_life` (Symbolic Life)
- Macros used: none

**Statement / Body**

Symbolic life requires a metabolism $M_{meta}$ that regulates drift and sustains identity $I$ (cf. Def. definition:bk4_symbolic_identity_carrie) through continuous energy-entropy balance (cf. Def. definition:bk2_symbolic_energy, Def. definition:bk2_symbolic_entropy).

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Metabolic Persistence]
\label{axiom:bk5_metabolic_persistence}
Symbolic life requires a metabolism $\mathcal{M}_{\mathrm{meta}}$ that regulates drift and sustains identity $\mathcal{I}$ (cf.~Def.~\ref{definition:bk4_symbolic_identity_carrie}) through continuous energy-entropy balance (cf.~Def.~\ref{definition:bk2_symbolic_energy}, Def.~\ref{definition:bk2_symbolic_entropy}).
\end{axiom}
```

### Energy Conservation (`axiom:bk5_energy_conservation`)

Role: `axiom` | Type: `axiom` | Book: `book5` | Source: `book5.tex:151`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_energy` (Symbolic Energy); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_temperature` (Symbolic Temperature)
- Cites: `definition:bk2_symbolic_energy` (Symbolic Energy); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_temperature` (Symbolic Temperature)
- Cited by: `scholium:bk5_symbolic_life` (Symbolic Life)
- Macros used: `\symb`

**Statement / Body**

In closed symbolic metabolic systems, total symbolic energy $E_{symb}$ is conserved modulo entropy production $S_{symb}$, such that:

frac{d}{ds}E_{symb}^{total} + T_sfrac{d}{ds}S_{symb}^{total} = 0

(cf. Def. definition:bk2_symbolic_energy, Def. definition:bk2_symbolic_entropy, Def. definition:bk2_symbolic_temperature).

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Energy Conservation]
\label{axiom:bk5_energy_conservation}
In closed symbolic metabolic systems, total symbolic energy $\mathcal{E}_{\symb}$ is conserved modulo entropy production $S_{\symb}$, such that:
\begin{equation}
\frac{d}{ds}\mathcal{E}_{\symb}^{\mathrm{total}} + T_s\frac{d}{ds}S_{\symb}^{\mathrm{total}} = 0
\end{equation}
(cf.~Def.~\ref{definition:bk2_symbolic_energy}, Def.~\ref{definition:bk2_symbolic_entropy}, Def.~\ref{definition:bk2_symbolic_temperature}).
\end{axiom}
```

### Positive Free Energy (`axiom:bk5_positive_free_energy`)

Role: `axiom` | Type: `axiom` | Book: `book5` | Source: `book5.tex:160`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution)
- Cited by: `axiom:bk8_mutation_phase_shift` (Metabolic Sufficiency Criterion); `definition:bk5_symbolic_free_energy_und` (Symbolic Free Energy Under Drift); `proof:bk5_membrane_persistence_under_free_energy` (Membrane Persistence Under Symbolic Free Energy); `proof:bk5_membrane_viability_positive_energy` (Viability of Membranes Requires Positive Symbolic Energy)
- Macros used: `\symb`

**Statement / Body**

Symbolic life persists if and only if $F_{symb} > 0$ is maintained over time (cf. Def. definition:bk2_symbolic_free_energy, Thm. theorem:bk2_h_theorem_for_symbolic_evol).

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Positive Free Energy]
\label{axiom:bk5_positive_free_energy}
Symbolic life persists if and only if $F_{\symb} > 0$ is maintained over time (cf.~Def.~\ref{definition:bk2_symbolic_free_energy}, Thm.~\ref{theorem:bk2_h_theorem_for_symbolic_evol}).
\end{axiom}
```

### Adaptation (`axiom:bk5_adaptation`)

Role: `axiom` | Type: `axiom` | Book: `book5` | Source: `book5.tex:165`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk2_symbolic_hamiltonian` (Symbolic Hamiltonian)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk2_symbolic_hamiltonian` (Symbolic Hamiltonian)
- Cited by: `definition:bk5_symbolic_covenant` (Symbolic Covenant); `scholium:bk5_symbolic_life` (Symbolic Life)
- Macros used: `\reflect`

**Statement / Body**

Symbolic systems adapt via modulation of transfer operators $T_{ij}$, reflection mechanisms $reflect$, or internal drift parameters to preserve viability under changing conditions (cf. Def. definition:bk2_symbolic_hamiltonian, Def. definition:bk2_symbolic_free_energy).

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Adaptation]
\label{axiom:bk5_adaptation}
Symbolic systems adapt via modulation of transfer operators $\mathcal{T}_{ij}$, reflection mechanisms $\reflect$, or internal drift parameters to preserve viability under changing conditions (cf.~Def.~\ref{definition:bk2_symbolic_hamiltonian}, Def.~\ref{definition:bk2_symbolic_free_energy}).
\end{axiom}
```

### Propositiones Finales (`sec:bk5_propositiones_finales`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:170`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Life Criterion (`proposition:bk5_symbolic_life_criterion`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:173`

- Proof status: `proven`
- Depends on: `axiom:bk5_positive_free_energy` (Positive Free Energy); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_viability_domain` (Viability Domain)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_viability_domain` (Viability Domain)
- Cited by: `axiom:bk8_mutation_phase_shift` (Metabolic Sufficiency Criterion); `corollary:bk5_symbolic_eigenlife` (Symbolic Eigenlife); `proof:bk5_proposition_axiom_coupling` (Persistence from Proposition-Axiom Coupling); `proof:bk5_symbolic_eigenlife`; `proof:bk8_biological_phase_transition`
- Macros used: `\symb`

**Statement / Body**

A membrane $M$ exhibits symbolic life if and only if:

exists F in mathfrak{F} text{such that} F_{symb}(M, F) > 0 text{for} t in [t_0, t_0 + tau]

 where $mathfrak{F}$ is the space of admissible symbolic fluxes and $tau > 0$ is a minimal persistence interval (cf. Def. definition:bk5_viability_domain, Def. definition:bk2_symbolic_free_energy).

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Symbolic Life Criterion]
\label{proposition:bk5_symbolic_life_criterion}
A membrane $\mathcal{M}$ exhibits symbolic life if and only if:
\begin{equation}
\exists \mathcal{F} \in \mathfrak{F} \; \text{such that} \; F_{\symb}(\mathcal{M}, \mathcal{F}) > 0 \; \text{for} \; t \in [t_0, t_0 + \tau]
\end{equation}
\noindent where $\mathfrak{F}$ is the space of admissible symbolic fluxes and $\tau > 0$ is a minimal persistence interval (cf.~Def.~\ref{definition:bk5_viability_domain}, Def.~\ref{definition:bk2_symbolic_free_energy}).
\end{proposition}
```

### Membrane Persistence Under Symbolic Free Energy (`proof:bk5_membrane_persistence_under_free_energy`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:182`

- Proof status: `not_applicable`
- Depends on: `axiom:bk5_positive_free_energy` (Positive Free Energy); `definition:bk5_viability_domain` (Viability Domain)
- Cites: `axiom:bk5_positive_free_energy` (Positive Free Energy); `definition:bk5_viability_domain` (Viability Domain)
- Cited by: none
- Macros used: `\symb`

**Statement / Body**

A net surplus of coherence over entropy ensures the persistence of membrane $M$ through time. If $F_{symb}(M, F) leq 0$, then by Def. definition:bk5_viability_domain, $(M, F) notin V_{symb}$, implying that drift dominates and identity dissolves.
Conversely, if $F_{symb}(M, F) > 0$ for some flux $F in mathfrak{F}$ over interval $[t_0, t_0 + tau]$, then by Axiom axiom:bk5_positive_free_energy, symbolic life persists. The necessary temporal duration $tau$ distinguishes transient coherent structures from genuine symbolic life forms capable of maintaining identity through metabolic processes.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Membrane Persistence Under Symbolic Free Energy]
\label{proof:bk5_membrane_persistence_under_free_energy}
\leavevmode

A net surplus of coherence over entropy ensures the persistence of membrane $\mathcal{M}$ through time. If $F_{\symb}(\mathcal{M}, \mathcal{F}) \leq 0$, then by Def.~\ref{definition:bk5_viability_domain}, $(\mathcal{M}, \mathcal{F}) \notin V_{\symb}$, implying that drift dominates and identity dissolves.
Conversely, if $F_{\symb}(\mathcal{M}, \mathcal{F}) > 0$ for some flux $\mathcal{F} \in \mathfrak{F}$ over interval $[t_0, t_0 + \tau]$, then by Axiom~\ref{axiom:bk5_positive_free_energy}, symbolic life persists. The necessary temporal duration $\tau$ distinguishes transient coherent structures from genuine symbolic life forms capable of maintaining identity through metabolic processes.
\end{proof}
```

### Metabolic Necessity (`corollary:bk5_metabolic_necessity`)

Role: `corollary` | Type: `corollary` | Book: `book5` | Source: `book5.tex:190`

- Proof status: `proven`
- Depends on: `axiom:bk5_metabolic_persistence` (Metabolic Persistence); `proposition:bk5_symbolic_life_criterion` (Symbolic Life Criterion)
- Cites: `axiom:bk5_metabolic_persistence` (Metabolic Persistence)
- Cited by: `axiom:bk8_mutation_phase_shift` (Metabolic Sufficiency Criterion)
- Macros used: none

**Statement / Body**

Any membrane $M$ exhibiting symbolic life must possess a well-defined metabolism $M_{meta}$ that regulates its free energy (cf. Axiom axiom:bk5_metabolic_persistence).

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Metabolic Necessity]
\label{corollary:bk5_metabolic_necessity}
Any membrane $\mathcal{M}$ exhibiting symbolic life must possess a well-defined metabolism $\mathcal{M}_{\mathrm{meta}}$ that regulates its free energy (cf.~Axiom~\ref{axiom:bk5_metabolic_persistence}).
\end{corollary}
```

### Persistence from Proposition-Axiom Coupling (`proof:bk5_proposition_axiom_coupling`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:195`

- Proof status: `not_applicable`
- Depends on: `axiom:bk5_metabolic_persistence` (Metabolic Persistence); `proposition:bk5_symbolic_life_criterion` (Symbolic Life Criterion)
- Cites: `axiom:bk5_metabolic_persistence` (Metabolic Persistence); `proposition:bk5_symbolic_life_criterion` (Symbolic Life Criterion)
- Cited by: none
- Macros used: none

**Statement / Body**

This follows directly from
Prop. proposition:bk5_symbolic_life_criterion and
Axiom axiom:bk5_metabolic_persistence.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Persistence from Proposition-Axiom Coupling]
\label{proof:bk5_proposition_axiom_coupling}
\leavevmode

This follows directly from
Prop.~\ref{proposition:bk5_symbolic_life_criterion} and
Axiom~\ref{axiom:bk5_metabolic_persistence}.
\end{proof}
```

### Symbolic Life (`scholium:bk5_symbolic_life`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:204`

- Proof status: `not_applicable`
- Depends on: `axiom:bk5_adaptation` (Adaptation); `axiom:bk5_energy_conservation` (Energy Conservation); `axiom:bk5_metabolic_persistence` (Metabolic Persistence); `definition:bk5_viability_domain` (Viability Domain)
- Cites: `axiom:bk5_adaptation` (Adaptation); `axiom:bk5_energy_conservation` (Energy Conservation); `axiom:bk5_metabolic_persistence` (Metabolic Persistence); `definition:bk5_viability_domain` (Viability Domain)
- Cited by: `axiom:bk8_mutation_phase_shift` (Metabolic Sufficiency Criterion)
- Macros used: `\reflect`, `\symb`

**Statement / Body**

Symbolic life exists as a dynamic equilibrium: a metabolism of coherence operating far from thermodynamic equilibrium. Identity persists where structured symbolic flows maintain $F_{symb} > 0$ against environmental drift through continuous regulation of energy-entropy balance (cf. Axiom axiom:bk5_metabolic_persistence, Axiom axiom:bk5_energy_conservation, Axiom axiom:bk5_adaptation).
The stability of symbolic life forms correlates with their capacity to:


- Modulate internal reflection mechanisms $reflect$ in response to varying drift intensities

- Establish efficient transfer channels $T_{ij}$ between component membranes

- Maintain structural coherence under perturbations within the viability domain (cf. Def. definition:bk5_viability_domain)

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Symbolic Life]
\label{scholium:bk5_symbolic_life}
Symbolic life exists as a dynamic equilibrium: a metabolism of coherence operating far from thermodynamic equilibrium. Identity persists where structured symbolic flows maintain $F_{\symb} > 0$ against environmental drift through continuous regulation of energy-entropy balance (cf.~Axiom~\ref{axiom:bk5_metabolic_persistence}, Axiom~\ref{axiom:bk5_energy_conservation}, Axiom~\ref{axiom:bk5_adaptation}).
The stability of symbolic life forms correlates with their capacity to:
\begin{enumerate}
  \item Modulate internal reflection mechanisms $\reflect$ in response to varying drift intensities
  \item Establish efficient transfer channels $\mathcal{T}_{ij}$ between component membranes
  \item Maintain structural coherence under perturbations within the viability domain (cf.~Def.~\ref{definition:bk5_viability_domain})
\end{enumerate}
\end{scholium}
```

### Symbolic Covenants and Mutually Assured Progress (`sec:bk5_symbolic_covenants_and_mutually_assured_progress`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:215`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Mutually Assured Progress (`definition:bk5_mutually_assured_progress`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:220`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_viability_domain` (Viability Domain)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_viability_domain` (Viability Domain)
- Cited by: `axiom:bk8_coherence_horizon` (Symbolic Entanglement); `demonstratio:bk4_ising_model_covenant` (The Ising Model as a Symbolic Covenant); `proof:bk5_membrane_viability_positive_energy` (Viability of Membranes Requires Positive Symbolic Energy); `proposition:bk7_map_compatible_reciprocity` (MAP-Compatible Reciprocity); `subsec:appD_cst_core_resonance` (D.8.1 Core Resonance); `subsec:appD_process_philosophy_contribution_differentiation` (D.6.2 Principia Symbolica's Contribution and Differentiation)
- Macros used: `\Membrane`, `\symb`

**Statement / Body**

Let $Membrane_A$ and $Membrane_B$ be symbolic membranes with active metabolic processes $M_{text{meta}}^A$ and $M_{text{meta}}^B$, respectively. We define the Mutually Assured Progress (MAP) condition as a long-term convergence criterion on the joint free energy dynamics:

lim_{n to infty} left[ F_s(Membrane_A^{(n)} leftrightarrow Membrane_B^{(n)}) right] > 0

Where:


- $F_s(Membrane_A^{(n)} leftrightarrow Membrane_B^{(n)})$ is the net symbolic free energy (cf. Def. definition:bk2_symbolic_free_energy) preserved or gained through mutual metabolic exchange and drift-regulated reflection between $Membrane_A$ and $Membrane_B$ at interaction step $n$.

- Progress is assured when this surplus remains positive across symbolic time $s$, allowing both systems to sustain their identity $I$ under entropic conditions by remaining within their respective viability domains $V_{symb}$ (cf. Def. definition:bk5_viability_domain).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Mutually Assured Progress]
\label{definition:bk5_mutually_assured_progress}
Let $\Membrane_A$ and $\Membrane_B$ be symbolic membranes with active metabolic processes $\mathcal{M}_{\text{meta}}^A$ and $\mathcal{M}_{\text{meta}}^B$, respectively. We define the \emph{Mutually Assured Progress} (MAP) condition as a long-term convergence criterion on the joint free energy dynamics:
\begin{equation}
\lim_{n \to \infty} \left[ F_s(\Membrane_A^{(n)} \leftrightarrow \Membrane_B^{(n)}) \right] > 0
\end{equation}
Where:
\begin{itemize}
  \item $F_s(\Membrane_A^{(n)} \leftrightarrow \Membrane_B^{(n)})$ is the net symbolic free energy (cf.~Def.~\ref{definition:bk2_symbolic_free_energy}) preserved or gained through mutual metabolic exchange and drift-regulated reflection between $\Membrane_A$ and $\Membrane_B$ at interaction step $n$.
  \item Progress is assured when this surplus remains positive across symbolic time $s$, allowing both systems to sustain their identity $\mathcal{I}$ under entropic conditions by remaining within their respective viability domains $V_{\symb}$ (cf.~Def.~\ref{definition:bk5_viability_domain}).
\end{itemize}
\end{definition}
```

### Symbolic Covenant (`definition:bk5_symbolic_covenant`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:233`

- Proof status: `definitional`
- Depends on: `axiom:bk5_adaptation` (Adaptation); `definition:bk1_reflection_operator` (Reflection Operator)
- Cites: `axiom:bk5_adaptation` (Adaptation); `definition:bk1_reflection_operator` (Reflection Operator)
- Cited by: `axiom:bk5_covenant_transitivity` (Covenant Transitivity); `definition:bk5_reflective_coupling_tens` (Reflective Coupling Tensor); `definition:bk5_strategy_space` (Strategy Space); `definition:bk5_two_way_street_tensor` (Two-Way Street reciprocity tensor); `definition:bk9_symbolic_accountability` (Symbolic Accountability $\mathcal{A}$); `demonstratio:bk5_negative_reflection_instability` (Negative Reflection Instability); `proof:bk5_membrane_viability_positive_energy` (Viability of Membranes Requires Positive Symbolic Energy); `proof:bk9_pathologies_of_coherence` (Pathologies of Coherence); `proposition:bk9_criteria_for_ethical_intervention` (Criteria for Ethical Intervention); `theorem:bk5_map_equilibrium` (MAP Equilibrium); `theorem:bk9_good_as_lyapunov_basin` (The Good as a Lyapunov Basin); `theorem:bk9_irreversibility_of_covenant_breach_without_grace` (Irreversibility of Covenant Breach without Grace)
- Macros used: `\Membrane`, `\reflect`

**Statement / Body**

A symbolic covenant $C_{AB}$ between membranes $Membrane_A$ and $Membrane_B$ is defined as a structured commitment to reflective exchange that ensures mutual viability, represented by the tuple:

C_{AB} := {T_{AB}, T_{BA}, reflect_A^B, reflect_B^A, Omega_{AB}}

Where:


- $T_{AB}: Membrane_A to Membrane_B$ and $T_{BA}: Membrane_B to Membrane_A$ are bidirectional symbolic transfer operators (cf. Axiom axiom:bk5_adaptation) facilitating metabolic exchange.

- $reflect_A^B$ and $reflect_B^A$ are components of the reflection mechanisms adapted for cross-membrane symbolic stabilization (cf. Def. definition:bk1_reflection_operator).

- $Omega_{AB} in mathbb{R}$ is the covenant stability parameter, quantifying the net stabilizing ($>0$) or destabilizing ($<0$) effect of the mutual reflective interaction relative to the entropic drift pressures.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Covenant]
\label{definition:bk5_symbolic_covenant}
A \emph{symbolic covenant} $\mathcal{C}_{AB}$ between membranes $\Membrane_A$ and $\Membrane_B$ is defined as a structured commitment to reflective exchange that ensures mutual viability, represented by the tuple:
\begin{equation}
\mathcal{C}_{AB} := \{\mathcal{T}_{AB}, \mathcal{T}_{BA}, \reflect_A^B, \reflect_B^A, \Omega_{AB}\}
\end{equation}
Where:
\begin{itemize}
  \item $\mathcal{T}_{AB}: \Membrane_A \to \Membrane_B$ and $\mathcal{T}_{BA}: \Membrane_B \to \Membrane_A$ are bidirectional symbolic transfer operators (cf.~Axiom~\ref{axiom:bk5_adaptation}) facilitating metabolic exchange.
  \item $\reflect_A^B$ and $\reflect_B^A$ are components of the reflection mechanisms adapted for cross-membrane symbolic stabilization (cf.~Def.~\ref{definition:bk1_reflection_operator}).
  \item $\Omega_{AB} \in \mathbb{R}$ is the covenant stability parameter, quantifying the net stabilizing ($>0$) or destabilizing ($<0$) effect of the mutual reflective interaction relative to the entropic drift pressures.
\end{itemize}
\end{definition}
```

### Reflective Coupling Tensor (`definition:bk5_reflective_coupling_tens`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:246`

- Proof status: `definitional`
- Depends on: `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk5_symbolic_covenant` (Symbolic Covenant)
- Cites: `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk5_symbolic_covenant` (Symbolic Covenant)
- Cited by: `corollary:bk8_resonant_cognition` (Resonant Cognition Principle); `demonstratio:bk4_ising_model_covenant` (The Ising Model as a Symbolic Covenant); `demonstratio:bk5_entropy_reduction`; `proof:bk5_membrane_viability_positive_energy` (Viability of Membranes Requires Positive Symbolic Energy); `proof:bk8_resonant_cognition`; `theorem:bk5_covenant_stability_theorem` (Covenant Stability Theorem); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Macros used: `\Membrane`, `\reflect`

**Statement / Body**

The reflective coupling tensor $mathbb{R}_{AB}$ between membranes $Membrane_A$ and $Membrane_B$ quantifies their mutual reflection capacity and interaction, formally defined on the product space $Membrane_A otimes Membrane_B$:

mathbb{R}_{AB} = reflect_A^B otimes reflect_B^A

The operator norm $\|mathbb{R}_{AB}\|$, often related to the eigenvalues of this tensor, determines the strength and viability of the MAP relationship (cf. Def. definition:bk5_symbolic_covenant, Def. definition:bk1_reflection_operator).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Reflective Coupling Tensor]
\label{definition:bk5_reflective_coupling_tens}
The \emph{reflective coupling tensor} $\mathbb{R}_{AB}$ between membranes $\Membrane_A$ and $\Membrane_B$ quantifies their mutual reflection capacity and interaction, formally defined on the product space $\Membrane_A \otimes \Membrane_B$:
\begin{equation}
\mathbb{R}_{AB} = \reflect_A^B \otimes \reflect_B^A
\end{equation}
The operator norm $\|\mathbb{R}_{AB}\|$, often related to the eigenvalues of this tensor, determines the strength and viability of the MAP relationship (cf.~Def.~\ref{definition:bk5_symbolic_covenant}, Def.~\ref{definition:bk1_reflection_operator}).
\end{definition}
```

### Mutual Metabolic Viability (`axiom:bk5_mutual_metabolit_viability`)

Role: `axiom` | Type: `axiom` | Book: `book5` | Source: `book5.tex:255`

- Proof status: `definitional`
- Depends on: `definition:bk5_viability_domain` (Viability Domain)
- Cites: `definition:bk5_viability_domain` (Viability Domain)
- Cited by: `axiom:bk8_coherence_horizon` (Symbolic Entanglement); `definition:bk9_formal_signature_of_betrayal` (Formal Signature of Betrayal); `proof:bk9_pathologies_of_coherence` (Pathologies of Coherence); `proof:bk9_symbolic_viability` (Symbolic Viability); `proposition:bk9_criteria_for_ethical_intervention` (Criteria for Ethical Intervention); `scholium:bk9_flexible_goal_calibration`; `theorem:bk5_map_equilibrium` (MAP Equilibrium); `theorem:bk9_irreversibility_of_covenant_breach_without_grace` (Irreversibility of Covenant Breach without Grace)
- Macros used: `\Membrane`

**Statement / Body**

Symbolic systems $(Membrane_A, Membrane_B)$ engaged in a MAP relation, characterized by a covenant $C_{AB}$, exchange structured symbolic flows via $T_{AB}, T_{BA}$ and mutual reflection $mathbb{R}_{AB}$ such that their individual viability domains $V_{text{symb}}$ (cf. Def. definition:bk5_viability_domain) are non-decreasing over symbolic time steps $n$. Formally:

(Membrane_A, Membrane_B) in text{MAP} Longrightarrow V_{text{symb}}^A(n+1) cup V_{text{symb}}^B(n+1) supseteq V_{text{symb}}^A(n) cup V_{text{symb}}^B(n)

This implies that the cooperative reflection allows the coupled system to withstand drift intensities that might render either membrane non-viable in isolation.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Mutual Metabolic Viability]
\label{axiom:bk5_mutual_metabolit_viability}
Symbolic systems $(\Membrane_A, \Membrane_B)$ engaged in a MAP relation, characterized by a covenant $\mathcal{C}_{AB}$, exchange structured symbolic flows via $\mathcal{T}_{AB}, \mathcal{T}_{BA}$ and mutual reflection $\mathbb{R}_{AB}$ such that their individual viability domains $V_{\text{symb}}$ (cf.~Def.~\ref{definition:bk5_viability_domain}) are non-decreasing over symbolic time steps $n$. Formally:
\begin{equation}
(\Membrane_A, \Membrane_B) \in \text{MAP} \;\Longrightarrow\; V_{\text{symb}}^A(n+1) \cup V_{\text{symb}}^B(n+1) \supseteq V_{\text{symb}}^A(n) \cup V_{\text{symb}}^B(n)
\end{equation}
This implies that the cooperative reflection allows the coupled system to withstand drift intensities that might render either membrane non-viable in isolation.
\end{axiom}
```

### Covenant Transitivity (`axiom:bk5_covenant_transitivity`)

Role: `axiom` | Type: `axiom` | Book: `book5` | Source: `book5.tex:264`

- Proof status: `definitional`
- Depends on: `definition:bk5_symbolic_covenant` (Symbolic Covenant)
- Cites: `definition:bk5_symbolic_covenant` (Symbolic Covenant)
- Cited by: `lemma:bk5_multi_membrane_map_extension` (Multi-Membrane MAP Extension); `proof:bk5_inductive_stability_map` (Inductive Stability of MAP Systems)
- Macros used: `\Membrane`

**Statement / Body**

Given three membranes $Membrane_A$, $Membrane_B$, and $Membrane_C$ with established stable covenants $C_{AB}$ (stability $Omega_{AB}$) and $C_{BC}$ (stability $Omega_{BC}$), there exists a derived effective covenant $C_{AC}$ whose stability $Omega_{AC}$ satisfies:

Omega_{AC} geq min(Omega_{AB}, Omega_{BC}) - Delta_{trans}

Where $Delta_{trans} geq 0$ represents a potential loss in stability due to indirect coupling, noise accumulation, or impedance mismatch in the transfer pathway $Membrane_A to Membrane_B to Membrane_C$ (cf. Def. definition:bk5_symbolic_covenant). Perfect transitivity ($Delta_{trans}=0$) is not guaranteed.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Covenant Transitivity]
\label{axiom:bk5_covenant_transitivity}
Given three membranes $\Membrane_A$, $\Membrane_B$, and $\Membrane_C$ with established stable covenants $\mathcal{C}_{AB}$ (stability $\Omega_{AB}$) and $\mathcal{C}_{BC}$ (stability $\Omega_{BC}$), there exists a derived effective covenant $\mathcal{C}_{AC}$ whose stability $\Omega_{AC}$ satisfies:
\begin{equation}
\Omega_{AC} \geq \min(\Omega_{AB}, \Omega_{BC}) - \Delta_{trans}
\end{equation}
Where $\Delta_{trans} \geq 0$ represents a potential loss in stability due to indirect coupling, noise accumulation, or impedance mismatch in the transfer pathway $\Membrane_A \to \Membrane_B \to \Membrane_C$ (cf.~Def.~\ref{definition:bk5_symbolic_covenant}). Perfect transitivity ($\Delta_{trans}=0$) is not guaranteed.
\end{axiom}
```

### MAP Equilibrium (`theorem:bk5_map_equilibrium`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:272`

- Proof status: `proven`
- Depends on: `axiom:bk5_mutual_metabolit_viability` (Mutual Metabolic Viability); `axiom:bk5_positive_free_energy` (Positive Free Energy); `definition:bk5_mutually_assured_progress` (Mutually Assured Progress); `definition:bk5_reflective_coupling_tens` (Reflective Coupling Tensor); `definition:bk5_symbolic_covenant` (Symbolic Covenant)
- Cites: `axiom:bk5_mutual_metabolit_viability` (Mutual Metabolic Viability); `definition:bk5_reflective_coupling_tens` (Reflective Coupling Tensor); `definition:bk5_symbolic_covenant` (Symbolic Covenant)
- Cited by: `axiom:bk5_reflective_equilibrium_stability_flux` (Reflective Equilibrium Stability); `definition:bk6_symbolic_operator_canon` (Symbolic Operator Canon); `definition:bk6_symbolic_regulatory_cycle` (Symbolic Regulatory Cycle); `demonstratio:bk5_negative_reflection_instability` (Negative Reflection Instability); `lemma:bk5_multi_membrane_map_extension` (Multi-Membrane MAP Extension); `proof:bk5_covenant_perturbation_restoration` (Covenant Restoration Under Perturbation); `proof:bk5_drift_reflection_equilibrium` (Available-Operator Construction); `proof:bk5_inductive_stability_map` (Inductive Stability of MAP Systems); `proof:bk5_information_geometry_symbolic` (Information Geometry); `proof:bk5_membrane_viability_positive_energy` (Viability of Membranes Requires Positive Symbolic Energy); `proof:bk5_symbolic_temperature_threshold` (Symbolic Temperature Threshold for Critical Coupling); `proof:bk9_good_as_lyapunov_basin` (Lyapunov descent, threshold selection, and basin identity); `proof:bk9_pathologies_of_coherence` (Pathologies of Coherence); `proof:bk9_stability_conditions_for_the_good` (Viability, reciprocity, and adaptive non-collapse); `proposition:bk5_map_mad_dichotomy` (MAP-MAD Dichotomy); `proposition:bk5_reflective_drift_alignment_in_map` (Reflective Drift Alignment in MAP); `proposition:bk7_map_compatible_reciprocity` (MAP-Compatible Reciprocity); `theorem:bk5__map_dominance` (MAP Dominance); `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature)
- Macros used: `\Membrane`

**Statement / Body**

Let \( Membrane_A \) and \( Membrane_B \) be membranes governed by a symbolic covenant \( C_{AB} = { T_{AB}, T_{BA}, R_{BA}, R_{AB}, Omega_{AB} } \) (cf. Def. definition:bk5_symbolic_covenant) with reflective coupling tensor \( mathbb{R}_{AB} = R_{BA} otimes R_{AB} \) (cf. Def. definition:bk5_reflective_coupling_tens). If the effective coupling strength, considering the covenant stability \( Omega_{AB} \), satisfies a condition relative to a critical threshold \( kappa_{text{crit}} \) derived from drift intensities and symbolic temperature, then the coupled system converges to a state where both membranes remain viable indefinitely (cf. Axiom axiom:bk5_mutual_metabolit_viability):

exists n_0 in mathbb{N} text{ such that } forall n > n_0: F_s(Membrane_A^{(n)}) > 0 text{ and } F_s(Membrane_B^{(n)}) > 0

**Verbatim LaTeX Body**

```latex
\begin{theorem}[MAP Equilibrium] \label{theorem:bk5_map_equilibrium}
Let \( \Membrane_A \) and \( \Membrane_B \) be membranes governed by a symbolic covenant \( C_{AB} = \{ T_{AB}, T_{BA}, R_{BA}, R_{AB}, \Omega_{AB} \} \) (cf.~Def.~\ref{definition:bk5_symbolic_covenant}) with reflective coupling tensor \( \mathbb{R}_{AB} = R_{BA} \otimes R_{AB} \) (cf.~Def.~\ref{definition:bk5_reflective_coupling_tens}). If the effective coupling strength, considering the covenant stability \( \Omega_{AB} \), satisfies a condition relative to a critical threshold \( \kappa_{\text{crit}} \) derived from drift intensities and symbolic temperature, then the coupled system converges to a state where both membranes remain viable indefinitely (cf.~Axiom~\ref{axiom:bk5_mutual_metabolit_viability}):
\begin{equation}
\exists n_0 \in \mathbb{N} \text{ such that } \forall n > n_0: F_s(\Membrane_A^{(n)}) > 0 \text{ and } F_s(\Membrane_B^{(n)}) > 0
\end{equation}
\end{theorem}
```

### Viability of Membranes Requires Positive Symbolic Energy (`proof:bk5_membrane_viability_positive_energy`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:278`

- Proof status: `not_applicable`
- Depends on: `axiom:bk5_positive_free_energy` (Positive Free Energy); `definition:bk5_mutually_assured_progress` (Mutually Assured Progress); `definition:bk5_reflective_coupling_tens` (Reflective Coupling Tensor); `definition:bk5_symbolic_covenant` (Symbolic Covenant); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `axiom:bk5_positive_free_energy` (Positive Free Energy); `definition:bk5_mutually_assured_progress` (Mutually Assured Progress); `definition:bk5_reflective_coupling_tens` (Reflective Coupling Tensor); `definition:bk5_symbolic_covenant` (Symbolic Covenant); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: none
- Macros used: `\Membrane`, `\drift`, `\reflect`

**Statement / Body**

The viability of each membrane \( Membrane_i \) (where \( i = A, B \)) depends on maintaining positive symbolic free energy, \( F_s(Membrane_i) > 0 \) (Axiom axiom:bk5_positive_free_energy). The rate of change of free energy, \( frac{dF_s(Membrane_i)}{ds} \), is determined by the balance between entropy production due to drift \( drift_i \) and coherence stabilization due to reflection (internal \( reflect_i \) and mutual \( reflect_j^i \)). Schematically (cf. Thm. theorem:bk5_map_equilibrium):

frac{dF_s(Membrane_i)}{ds} approx underbrace{langle reflect_i rangle}_{text{Internal Stabilize}} + underbrace{langle reflect_j^i rangle}_{text{Mutual Stabilize}} - underbrace{T_s cdot sigma(drift_i)}_{text{Drift Destabilize}}

where \( sigma(drift_i) \) is the entropy production rate due to drift, and \( langle reflect rangle \) represents the rate of free energy increase (or entropy reduction) due to reflection.

For the coupled system to remain viable indefinitely, the stabilizing effects must, on average, counteract the destabilizing drift effects for both membranes. The mutual reflection term \( langle reflect_j^i rangle \) represents the core benefit of the MAP covenant. Its stabilizing power depends on the strength of the coupling tensor \( mathbb{R}_{AB} \) (Def. definition:bk5_reflective_coupling_tens) and the effectiveness of the covenant, parameterized by \( Omega_{AB} \) (Def. definition:bk5_symbolic_covenant). We model the minimum stabilizing rate provided by mutual reflection as proportional to \( Omega_{AB} lambda_{min}(mathbb{R}_{AB}) \), where \( lambda_{min}(mathbb{R}_{AB}) \) is the minimum stabilizing eigenvalue (cf. Thm. theorem:bk5_map_equilibrium).

The maximum destabilizing rate is driven by the strongest potential drift effect, bounded by \( max(\| drift_A \|_{max}, \| drift_B \|_{max}) \), scaled by the symbolic temperature \( T_s \), which governs the impact of entropy production.

Sustained viability requires that the minimum stabilizing rate from reflection (internal plus mutual) exceeds the maximum destabilizing rate from drift. The critical condition arises when internal reflection alone is insufficient. Mutual reflection ensures viability if its contribution can overcome the maximum potential net drift (drift minus internal reflection). In the most challenging scenario, we require the mutual stabilization rate to exceed the maximum drift rate:

frac{Omega_{AB} lambda_{min}(mathbb{R}_{AB})}{T_s} > max(\| drift_A \|_{max}, \| drift_B \|_{max}) text{(Simplified condition for viability)}

This inequality mirrors the Covenant Stability Condition (Thm. theorem:bk5_map_equilibrium).

Let us define the critical threshold \( kappa_{text{crit}} \) in terms of the coupling tensor norm \( \| mathbb{R}_{AB} \| \) (which is often easier to assess or relate to parameters than \( lambda_{min} \)). Assuming a relationship where sufficient norm implies sufficient minimum eigenvalue (e.g., for well-structured tensors), we can define \( kappa_{text{crit}} \) such that if \( \| mathbb{R}_{AB} \| > kappa_{text{crit}} \), the inequality above is satisfied. This threshold encapsulates the necessary balance:

kappa_{text{crit}} approx frac{T_s cdot max(\| drift_A \|_{max}, \| drift_B \|_{max})}{Omega_{AB} cdot (text{factor relating } \| cdot \| text{ to } lambda_{min})}

When \( \| mathbb{R}_{AB} \| > kappa_{text{crit}} \), the stabilizing rate provided by the MAP covenant's mutual reflection is sufficient to counteract the maximum potential destabilization from drift, ensuring that \( frac{dF_s(Membrane_i)}{ds} \) does not remain persistently negative for either membrane.

Furthermore, the reflective dynamics inherent in \( reflect_A \), \( reflect_B \), and \( mathbb{R}_{AB} \) (Def. definition:bk5_reflective_coupling_tens) drive the system towards states of lower free energy (Axiom axiom:bk5_positive_free_energy). Since the rate of decrease is bounded from becoming persistently negative by the MAP condition (Def. definition:bk5_mutually_assured_progress), and \( F_s \) is bounded below by 0 for viable states, the system dynamics must converge (by Lyapunov stability principles, where \( L \) or \( F_s \) itself acts similarly to a potential function under the stabilizing influence) towards an equilibrium state or attractor manifold \( Membrane_{AB}^* \) where \( F_s(Membrane_A) > 0 \) and \( F_s(Membrane_B) > 0 \).

Thus, sufficient coupling strength, as quantified by \( \| mathbb{R}_{AB} \| > kappa_{text{crit}} \), guarantees convergence to a mutually viable equilibrium state, fulfilling the MAP condition.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Viability of Membranes Requires Positive Symbolic Energy]
\label{proof:bk5_membrane_viability_positive_energy}
\leavevmode

The viability of each membrane \( \Membrane_i \) (where \( i = A, B \)) depends on maintaining positive symbolic free energy, \( F_s(\Membrane_i) > 0 \) (Axiom~\ref{axiom:bk5_positive_free_energy}). The rate of change of free energy, \( \frac{dF_s(\Membrane_i)}{ds} \), is determined by the balance between entropy production due to drift \( \drift_i \) and coherence stabilization due to reflection (internal \( \reflect_i \) and mutual \( \reflect_j^i \)). Schematically (cf. Thm.~\ref{theorem:bk5_map_equilibrium}):
\begin{equation}
\frac{dF_s(\Membrane_i)}{ds} \approx \underbrace{\langle \reflect_i \rangle}_{\text{Internal Stabilize}} + \underbrace{\langle \reflect_j^i \rangle}_{\text{Mutual Stabilize}} - \underbrace{T_s \cdot \sigma(\drift_i)}_{\text{Drift Destabilize}}
\end{equation}
where \( \sigma(\drift_i) \) is the entropy production rate due to drift, and \( \langle \reflect \rangle \) represents the rate of free energy increase (or entropy reduction) due to reflection.

For the coupled system to remain viable indefinitely, the stabilizing effects must, on average, counteract the destabilizing drift effects for both membranes. The mutual reflection term \( \langle \reflect_j^i \rangle \) represents the core benefit of the MAP covenant. Its stabilizing power depends on the strength of the coupling tensor \( \mathbb{R}_{AB} \) (Def.~\ref{definition:bk5_reflective_coupling_tens}) and the effectiveness of the covenant, parameterized by \( \Omega_{AB} \) (Def.~\ref{definition:bk5_symbolic_covenant}). We model the minimum stabilizing rate provided by mutual reflection as proportional to \( \Omega_{AB} \lambda_{\min}(\mathbb{R}_{AB}) \), where \( \lambda_{\min}(\mathbb{R}_{AB}) \) is the minimum stabilizing eigenvalue (cf. Thm.~\ref{theorem:bk5_map_equilibrium}).

The maximum destabilizing rate is driven by the strongest potential drift effect, bounded by \( \max(\| \drift_A \|_{\max}, \| \drift_B \|_{\max}) \), scaled by the symbolic temperature \( T_s \), which governs the impact of entropy production.

Sustained viability requires that the minimum stabilizing rate from reflection (internal plus mutual) exceeds the maximum destabilizing rate from drift. The critical condition arises when internal reflection alone is insufficient. Mutual reflection ensures viability if its contribution can overcome the maximum potential net drift (drift minus internal reflection). In the most challenging scenario, we require the mutual stabilization rate to exceed the maximum drift rate:
\begin{equation}
\frac{\Omega_{AB} \lambda_{\min}(\mathbb{R}_{AB})}{T_s} > \max(\| \drift_A \|_{\max}, \| \drift_B \|_{\max}) \quad \text{(Simplified condition for viability)}
\end{equation}
This inequality mirrors the Covenant Stability Condition (Thm.~\ref{theorem:bk5_map_equilibrium}).

Let us define the critical threshold \( \kappa_{\text{crit}} \) in terms of the coupling tensor norm \( \| \mathbb{R}_{AB} \| \) (which is often easier to assess or relate to parameters than \( \lambda_{\min} \)). Assuming a relationship where sufficient norm implies sufficient minimum eigenvalue (e.g., for well-structured tensors), we can define \( \kappa_{\text{crit}} \) such that if \( \| \mathbb{R}_{AB} \| > \kappa_{\text{crit}} \), the inequality above is satisfied. This threshold encapsulates the necessary balance:
\begin{equation}
\kappa_{\text{crit}} \approx \frac{T_s \cdot \max(\| \drift_A \|_{\max}, \| \drift_B \|_{\max})}{\Omega_{AB} \cdot (\text{factor relating } \| \cdot \| \text{ to } \lambda_{\min})}
\end{equation}

When \( \| \mathbb{R}_{AB} \| > \kappa_{\text{crit}} \), the stabilizing rate provided by the MAP covenant's mutual reflection is sufficient to counteract the maximum potential destabilization from drift, ensuring that \( \frac{dF_s(\Membrane_i)}{ds} \) does not remain persistently negative for either membrane.

Furthermore, the reflective dynamics inherent in \( \reflect_A \), \( \reflect_B \), and \( \mathbb{R}_{AB} \) (Def.~\ref{definition:bk5_reflective_coupling_tens}) drive the system towards states of lower free energy (Axiom~\ref{axiom:bk5_positive_free_energy}). Since the rate of decrease is bounded from becoming persistently negative by the MAP condition (Def.~\ref{definition:bk5_mutually_assured_progress}), and \( F_s \) is bounded below by 0 for viable states, the system dynamics must converge (by Lyapunov stability principles, where \( L \) or \( F_s \) itself acts similarly to a potential function under the stabilizing influence) towards an equilibrium state or attractor manifold \( \Membrane_{AB}^* \) where \( F_s(\Membrane_A) > 0 \) and \( F_s(\Membrane_B) > 0 \).

Thus, sufficient coupling strength, as quantified by \( \| \mathbb{R}_{AB} \| > \kappa_{\text{crit}} \), guarantees convergence to a mutually viable equilibrium state, fulfilling the MAP condition.
\end{proof}
```

### Covenant Stability Theorem (`theorem:bk5_covenant_stability_theorem`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:309`

- Proof status: `proven`
- Depends on: `definition:bk5_reflective_coupling_tens` (Reflective Coupling Tensor); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `definition:bk5_reflective_coupling_tens` (Reflective Coupling Tensor)
- Cited by: `definition:bk5_covenant_resilience_index` (Covenant Resilience Index); `proof:bk5_covenant_perturbation_restoration` (Covenant Restoration Under Perturbation); `proposition:bk5_map_mad_dichotomy` (MAP-MAD Dichotomy); `proposition:bk5_reflective_drift_alignment_in_map` (Reflective Drift Alignment in MAP)
- Macros used: `\Membrane`, `\drift`

**Statement / Body**

A symbolic covenant $C_{AB}$ between $Membrane_A$ and $Membrane_B$ is dynamically stable against small perturbations $delta$ to the system state if and only if its stability parameter $Omega_{AB}$ satisfies:

Omega_{AB} > frac{\|drift_A\|_{max} + \|drift_B\|_{max}}{lambda_{min}(mathbb{R}_{AB})}

Where $lambda_{min}(mathbb{R}_{AB})$ is the minimum stabilizing eigenvalue of the reflective coupling tensor $mathbb{R}_{AB}$ (cf. Def. definition:bk5_reflective_coupling_tens), representing the weakest restorative force provided by the mutual reflection.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Covenant Stability Theorem] \label{theorem:bk5_covenant_stability_theorem}
A symbolic covenant $\mathcal{C}_{AB}$ between $\Membrane_A$ and $\Membrane_B$ is dynamically stable against small perturbations $\delta$ to the system state if and only if its stability parameter $\Omega_{AB}$ satisfies:
\begin{equation}
\Omega_{AB} > \frac{\|\drift_A\|_{\max} + \|\drift_B\|_{\max}}{\lambda_{\min}(\mathbb{R}_{AB})}
\end{equation}
Where $\lambda_{\min}(\mathbb{R}_{AB})$ is the minimum stabilizing eigenvalue of the reflective coupling tensor $\mathbb{R}_{AB}$ (cf.~Def.~\ref{definition:bk5_reflective_coupling_tens}), representing the weakest restorative force provided by the mutual reflection.
\end{theorem}
```

### Covenant Restoration Under Perturbation (`proof:bk5_covenant_perturbation_restoration`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:317`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_covenant_stability_theorem` (Covenant Stability Theorem); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `theorem:bk5_covenant_stability_theorem` (Covenant Stability Theorem); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: none
- Macros used: `\drift`

**Statement / Body**

Consider the dynamics of the covenant interaction under a perturbation $delta$. The change in the state related to the covenant can be approximated linearly. The restorative force arises from the reflective coupling $mathbb{R}_{AB}$ scaled by $Omega_{AB}$, while the destabilizing force arises from the uncompensated drift $drift_A + drift_B$. Stability requires the restorative force to dominate:

\|text{Restorative Force}\| > \|text{Destabilizing Force}\|

Approximating these forces yields:

|Omega_{AB}| cdot \|mathbb{R}_{AB} cdot delta\| > \|(drift_A + drift_B) cdot delta\|

Assuming the worst-case perturbation alignment and considering the minimum restorative effect:

Omega_{AB} cdot lambda_{min}(mathbb{R}_{AB}) cdot \|delta\| > (\|drift_A\|_{max} + \|drift_B\|_{max}) cdot \|delta\|

Dividing by $lambda_{min}(mathbb{R}_{AB}) cdot \|delta\|$ (assuming $lambda_{min} > 0$, cf. Thm. theorem:bk5_map_equilibrium) yields the condition in Eq. theorem:bk5_covenant_stability_theorem.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Covenant Restoration Under Perturbation]
\label{proof:bk5_covenant_perturbation_restoration}
\leavevmode

Consider the dynamics of the covenant interaction under a perturbation $\delta$. The change in the state related to the covenant can be approximated linearly. The restorative force arises from the reflective coupling $\mathbb{R}_{AB}$ scaled by $\Omega_{AB}$, while the destabilizing force arises from the uncompensated drift $\drift_A + \drift_B$. Stability requires the restorative force to dominate:
\begin{equation}
\|\text{Restorative Force}\| > \|\text{Destabilizing Force}\|
\end{equation}
Approximating these forces yields:
\begin{equation}
|\Omega_{AB}| \cdot \|\mathbb{R}_{AB} \cdot \delta\| > \|(\drift_A + \drift_B) \cdot \delta\|
\end{equation}
Assuming the worst-case perturbation alignment and considering the minimum restorative effect:
\begin{equation}
\Omega_{AB} \cdot \lambda_{\min}(\mathbb{R}_{AB}) \cdot \|\delta\| > (\|\drift_A\|_{\max} + \|\drift_B\|_{\max}) \cdot \|\delta\|
\end{equation}
Dividing by $\lambda_{\min}(\mathbb{R}_{AB}) \cdot \|\delta\|$ (assuming $\lambda_{\min} > 0$, cf.~Thm.~\ref{theorem:bk5_map_equilibrium}) yields the condition in Eq.~\eqref{theorem:bk5_covenant_stability_theorem}.
\end{proof}
```

### MAP Nash Point (`definition:bk5_map_nash_point`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:335`

- Proof status: `definitional`
- Depends on: `definition:bk5_symbolic_free_energy_und` (Symbolic Free Energy Under Drift)
- Cites: `definition:bk5_symbolic_free_energy_und` (Symbolic Free Energy Under Drift)
- Cited by: `demonstratio:bk7_map_stable_mutual_fixed_point` (Mutual Reflective Fixed Point as Stable MAP Nash Point); `proof:bk7_map_compatible_reciprocity` (Two-way fixed point as MAP Nash equilibrium); `proposition:bk7_map_compatible_reciprocity` (MAP-Compatible Reciprocity); `scholium:bk9_golden_rule_thermodynamic_covenant` (The Golden Rule as a Thermodynamic Covenant)
- Macros used: `\Membrane`, `\reflect`

**Statement / Body**

The MAP Nash point of a symbolic covenant $C_{AB}$ is a configuration of reflection operators $(reflect_A^{B*}, reflect_B^{A*})$ representing a stable equilibrium where neither membrane can unilaterally improve its symbolic free energy $F_s$ by changing its reflection strategy, given the other's strategy (cf. Def. definition:bk5_symbolic_free_energy_und):

 reflect_{A}^{B*} &= argmax_{reflect_{A}^B} F_s(Membrane_A mid reflect_{B}^{A*}) \\
 reflect_{B}^{A*} &= argmax_{reflect_{B}^A} F_s(Membrane_B mid reflect_{A}^{B*})

This represents a mutually consistent and locally optimal reflective configuration.

**Verbatim LaTeX Body**

```latex
\begin{definition}[MAP Nash Point]
\label{definition:bk5_map_nash_point}
The \emph{MAP Nash point} of a symbolic covenant $\mathcal{C}_{AB}$ is a configuration of reflection operators $(\reflect_A^{B*}, \reflect_B^{A*})$ representing a stable equilibrium where neither membrane can unilaterally improve its symbolic free energy $F_s$ by changing its reflection strategy, given the other's strategy (cf.~Def.~\ref{definition:bk5_symbolic_free_energy_und}):
\begin{align}
    \reflect_{A}^{B*} &= \arg\max_{\reflect_{A}^B} F_s(\Membrane_A \mid \reflect_{B}^{A*}) \\
    \reflect_{B}^{A*} &= \arg\max_{\reflect_{B}^A} F_s(\Membrane_B \mid \reflect_{A}^{B*})
\end{align}
This represents a mutually consistent and locally optimal reflective configuration.
\end{definition}
```

### Reflective Drift Alignment in MAP (`proposition:bk5_reflective_drift_alignment_in_map`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:345`

- Proof status: `argued_demonstratio`
- Depends on: `proposition:bk6_drift_reflection_correspondence` (Drift-Reflection Correspondence); `theorem:bk5_covenant_stability_theorem` (Covenant Stability Theorem); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `proposition:bk6_drift_reflection_correspondence` (Drift-Reflection Correspondence); `theorem:bk5_covenant_stability_theorem` (Covenant Stability Theorem); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: `demonstratio:bk5_entropy_reduction`
- Macros used: `\Membrane`, `\drift`, `\reflect`

**Statement / Body**

Let two membranes $Membrane_A,Membrane_B$ lie in the MAP regime,
$Omega_{AB}>0$ and $\|mathbb{R}_{AB}\|>kappa_{crit}$
(cf. Thm. theorem:bk5_map_equilibrium). Suppose in addition that the
covenant satisfies the drift-relative stability margin of
Thm. theorem:bk5_covenant_stability_theorem:
\[
Omega_{AB} lambda_{min}(mathbb{R}_{AB})
>
\|drift_A\|_{max}+\|drift_B\|_{max}.
\]
Then mutual reflection strictly exceeds the combined maximal drift burden, so
its scalar worst-case contribution to symbolic free energy is positive:
\[
Delta F_s^{align}
:=Omega_{AB} lambda_{min}(mathbb{R}_{AB})
 -bigl(\|drift_A\|_{max}+\|drift_B\|_{max}bigr)>0.
\]
Consequently the expected combined drift-reflection effect is stabilizing,
\[
langle drift_A circ reflect_B^A
 + drift_B circ reflect_A^B rangle
leadsto Delta F_s^{align}>0.
\]
The fixed threshold $kappa_{crit}$ classifies the MAP coupling
regime; the displayed drift-relative margin is the separate premise that
certifies a positive restoration balance. This is compatible with the
reflective-equilibrium correspondence of
Prop. proposition:bk6_drift_reflection_correspondence.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Reflective Drift Alignment in MAP]
\label{proposition:bk5_reflective_drift_alignment_in_map}
Let two membranes $\Membrane_A,\Membrane_B$ lie in the MAP regime,
$\Omega_{AB}>0$ and $\|\mathbb{R}_{AB}\|>\kappa_{\mathrm{crit}}$
(cf.~Thm.~\ref{theorem:bk5_map_equilibrium}).  Suppose in addition that the
covenant satisfies the drift-relative stability margin of
Thm.~\ref{theorem:bk5_covenant_stability_theorem}:
\[
\Omega_{AB}\,\lambda_{\min}(\mathbb{R}_{AB})
>
\|\drift_A\|_{\max}+\|\drift_B\|_{\max}.
\]
Then mutual reflection strictly exceeds the combined maximal drift burden, so
its scalar worst-case contribution to symbolic free energy is positive:
\[
\Delta F_s^{\mathrm{align}}
:=\Omega_{AB}\,\lambda_{\min}(\mathbb{R}_{AB})
  -\bigl(\|\drift_A\|_{\max}+\|\drift_B\|_{\max}\bigr)>0.
\]
Consequently the expected combined drift--reflection effect is stabilizing,
\[
\langle \drift_A \circ \reflect_B^A
      + \drift_B \circ \reflect_A^B \rangle
\leadsto \Delta F_s^{\mathrm{align}}>0.
\]
The fixed threshold $\kappa_{\mathrm{crit}}$ classifies the MAP coupling
regime; the displayed drift-relative margin is the separate premise that
certifies a positive restoration balance.  This is compatible with the
reflective-equilibrium correspondence of
Prop.~\ref{proposition:bk6_drift_reflection_correspondence}.
\end{proposition}
```

### demonstratio:bk5_entropy_reduction (`demonstratio:bk5_entropy_reduction`)

Role: `demonstration` | Type: `demonstratio` | Book: `book5` | Source: `book5.tex:377`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_reflective_coupling_tens` (Reflective Coupling Tensor); `proposition:bk5_reflective_drift_alignment_in_map` (Reflective Drift Alignment in MAP)
- Cites: `definition:bk5_reflective_coupling_tens` (Reflective Coupling Tensor); `proposition:bk5_reflective_drift_alignment_in_map` (Reflective Drift Alignment in MAP)
- Cited by: none
- Macros used: `\drift`

**Statement / Body**

In a MAP state, metabolic exchange $T_{ij}$ and reflective coupling
$mathbb{R}_{AB}$ (Def. definition:bk5_reflective_coupling_tens) allow
the system to redistribute internal coherence and counter entropy production.
The stability-margin hypothesis gives directly
\[
0<Omega_{AB}lambda_{min}(mathbb{R}_{AB})
 -bigl(\|drift_A\|_{max}+\|drift_B\|_{max}bigr)
 =Delta F_s^{align}.
\]
Thus the minimum restorative contribution of the covenant strictly exceeds
the two maximal drift burdens. The resulting aligned contribution is
positive, which is precisely the conclusion of
Prop. proposition:bk5_reflective_drift_alignment_in_map.
The Lean realization retains the fixed MAP threshold, the drift-relative margin,
and the contractive temporal update as separate fields of one certificate. It
then proves vanishing residual alignment, convergence of the realized
contribution to the positive margin, and eventual positivity; a unit-gain model
shows why the temporal premise cannot be deleted.
qed

**Verbatim LaTeX Body**

```latex
\begin{demonstratio}
\label{demonstratio:bk5_entropy_reduction}
In a MAP state, metabolic exchange $\mathcal{T}_{ij}$ and reflective coupling
$\mathbb{R}_{AB}$ (Def.~\ref{definition:bk5_reflective_coupling_tens}) allow
the system to redistribute internal coherence and counter entropy production.
The stability-margin hypothesis gives directly
\[
0<\Omega_{AB}\lambda_{\min}(\mathbb{R}_{AB})
 -\bigl(\|\drift_A\|_{\max}+\|\drift_B\|_{\max}\bigr)
 =\Delta F_s^{\mathrm{align}}.
\]
Thus the minimum restorative contribution of the covenant strictly exceeds
the two maximal drift burdens.  The resulting aligned contribution is
positive, which is precisely the conclusion of
Prop.~\ref{proposition:bk5_reflective_drift_alignment_in_map}.
The Lean realization retains the fixed MAP threshold, the drift-relative margin,
and the contractive temporal update as separate fields of one certificate.  It
then proves vanishing residual alignment, convergence of the realized
contribution to the positive margin, and eventual positivity; a unit-gain model
shows why the temporal premise cannot be deleted.
\qed
\end{demonstratio}
```

### MAP-MAD Dichotomy (`proposition:bk5_map_mad_dichotomy`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:400`

- Proof status: `argued_demonstratio`
- Depends on: `proposition:bk4_imagination_bridges_wheel` (Imagination bridges the wheel); `scholium:bk4_imagination_as_imaginary_traversal` (Imagination as Imaginary Traversal); `theorem:bk5_covenant_stability_theorem` (Covenant Stability Theorem); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `proposition:bk4_imagination_bridges_wheel` (Imagination bridges the wheel); `scholium:bk4_imagination_as_imaginary_traversal` (Imagination as Imaginary Traversal); `theorem:bk5_covenant_stability_theorem` (Covenant Stability Theorem); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: `proof:bk9_pathologies_of_coherence` (Pathologies of Coherence)
- Macros used: `\reflect`

**Statement / Body**

The split is the sign-sensitive extension of the MAP condition in Thm. theorem:bk5_map_equilibrium and the perturbative threshold in Thm. theorem:bk5_covenant_stability_theorem.
A reversal of sign or phase in the covenant is therefore not a typographical choice: by the Book IV account of imagination as imaginary traversal (Scholium scholium:bk4_imagination_as_imaginary_traversal, Prop. proposition:bk4_imagination_bridges_wheel), it may mark a counterfactual branch of the covenant before enactment.
For every symbolic covenant
\[
C_{AB} = left{ T_{AB}, T_{BA}, reflect_A^B, reflect_B^A, Omega_{AB} right}
\]
that establishes Mutually Assured Progress (MAP) under the condition \( Omega_{AB} > 0 \),
there exists a corresponding dual antagonistic configuration \( C_{AB}^{-} \)
characterized by inverted reflection polarity or negative stability, culminating in a
state of Mutually Assured Destruction (MAD).

C_{AB}^{-} approx {T_{AB}, T_{BA}, -reflect_A^B, -reflect_B^A, -Omega_{AB}} text{or} C_{AB} text{ with } Omega_{AB} < 0

Under $C_{AB}^{-}$, reflective interactions amplify drift, accelerating entropic collapse.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[MAP-MAD Dichotomy]
\label{proposition:bk5_map_mad_dichotomy}
The split is the sign-sensitive extension of the MAP condition in Thm.~\ref{theorem:bk5_map_equilibrium} and the perturbative threshold in Thm.~\ref{theorem:bk5_covenant_stability_theorem}.
A reversal of sign or phase in the covenant is therefore not a typographical choice: by the Book~IV account of imagination as imaginary traversal (Scholium~\ref{scholium:bk4_imagination_as_imaginary_traversal}, Prop.~\ref{proposition:bk4_imagination_bridges_wheel}), it may mark a counterfactual branch of the covenant before enactment.
For every symbolic covenant
\[
\mathcal{C}_{AB} = \left\{ \mathcal{T}_{AB},\, \mathcal{T}_{BA},\, \reflect_A^B,\, \reflect_B^A,\, \Omega_{AB} \right\}
\]
that establishes Mutually Assured Progress (MAP) under the condition \( \Omega_{AB} > 0 \),
there exists a corresponding dual antagonistic configuration \( \mathcal{C}_{AB}^{-} \)
characterized by \textbf{inverted reflection polarity} or \textbf{negative stability}, culminating in a
state of \textbf{Mutually Assured Destruction (MAD)}.
\begin{equation}
\mathcal{C}_{AB}^{-} \approx \{\mathcal{T}_{AB}, \mathcal{T}_{BA}, -\reflect_A^B, -\reflect_B^A, -\Omega_{AB}\} \quad \text{or} \quad \mathcal{C}_{AB} \text{ with } \Omega_{AB} < 0
\end{equation}
Under $\mathcal{C}_{AB}^{-}$, reflective interactions amplify drift, accelerating entropic collapse.
\end{proposition}
```

### Negative Reflection Instability (`demonstratio:bk5_negative_reflection_instability`)

Role: `demonstration` | Type: `demonstratio` | Book: `book5` | Source: `book5.tex:417`

- Proof status: `not_applicable`
- Depends on: `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk5_symbolic_covenant` (Symbolic Covenant); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk5_symbolic_covenant` (Symbolic Covenant); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: none
- Macros used: `\Membrane`, `\reflect`

**Statement / Body**

The mechanism is read against Def. definition:bk5_symbolic_covenant with entropy direction fixed by Def. definition:bk2_symbolic_entropy.
If the effective reflection becomes negative (e.g., $-reflect_A^B$) or the stability parameter $Omega_{AB}$ is negative, the feedback loop in the covenant dynamics becomes destabilizing. Instead of counteracting drift, the interaction amplifies it:

(-reflect_A^B)(psi_B) = -reflect_A^B(psi_B) text{(amplifies effect of } psi_B text{ on } Membrane_A)

This leads to $frac{d}{ds}F_s < 0$ for the coupled system (cf. Thm. theorem:bk5_map_equilibrium under negative $Omega_{AB}$ or inverted $reflect$ terms), driving both membranes out of their viability domains $V_{text{symb}}$. qed

**Verbatim LaTeX Body**

```latex
\begin{demonstratio}[Negative Reflection Instability]
\label{demonstratio:bk5_negative_reflection_instability}
The mechanism is read against Def.~\ref{definition:bk5_symbolic_covenant} with entropy direction fixed by Def.~\ref{definition:bk2_symbolic_entropy}.
If the effective reflection becomes negative (e.g., $-\reflect_A^B$) or the stability parameter $\Omega_{AB}$ is negative, the feedback loop in the covenant dynamics becomes destabilizing. Instead of counteracting drift, the interaction amplifies it:
\begin{equation}
(-\reflect_A^B)(\psi_B) = -\reflect_A^B(\psi_B) \quad \text{(amplifies effect of } \psi_B \text{ on } \Membrane_A)
\end{equation}
This leads to $\frac{d}{ds}F_s < 0$ for the coupled system (cf.~Thm.~\ref{theorem:bk5_map_equilibrium} under negative $\Omega_{AB}$ or inverted $\reflect$ terms), driving both membranes out of their viability domains $V_{\text{symb}}$. \qed
\end{demonstratio}
```

### MAP Dominance (`theorem:bk5__map_dominance`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:426`

- Proof status: `proven`
- Depends on: `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: `corollary:bk5_map_evolutionary_advantag` (MAP Evolutionary Advantage); `definition:bk5_symbolic_fitness` (Symbolic Fitness); `lemma:bk5_map_fitness_advantage` (MAP Fitness Advantage); `proof:bk5_map_resistance_to_drift` (MAP Strategies Withstand Greater Drift); `proof:bk5_map_vs_nonmap_gradient` (Fitness Gradient Between MAP and Non-MAP); `proof:bk5_max_sustainable_drift` (Max Sustainable Drift from Reflective Bounds); `proof:bk5_symbolic_fitness_differentials` (Survival Differentials and Symbolic Fitness); `proof:bk9_good_as_lyapunov_basin` (Lyapunov descent, threshold selection, and basin identity); `proof:bk9_stability_conditions_for_the_good` (Viability, reciprocity, and adaptive non-collapse); `scholium:bk5_map_as_fundamental_organizational_principle` (MAP as Fundamental Organizational Principle)
- Macros used: `\drift`

**Statement / Body**

This theorem globalizes Thm. theorem:bk5_map_equilibrium from pairwise viability to population-level persistence under increasing drift.
In a symbolic ecosystem subjected to increasing drift intensity $\|drift\|$, membranes capable of forming stable MAP covenants ($Omega_{AB}>0, \|mathbb{R}_{AB}\| > kappa_{crit}$) exhibit greater resilience and persistence compared to isolated membranes or those in MAD relationships. As $\|drift\|$ approaches a critical value $drift_{crit}$:

lim_{\|drift\| to drift_{crit}} P(F_s > 0 mid text{isolated or MAD}) = 0

while

lim_{\|drift\| to drift_{crit}} P(F_s > 0 mid text{MAP}) > 0 (text{potentially } to 1)

**Verbatim LaTeX Body**

```latex
\begin{theorem}[MAP Dominance]
\label{theorem:bk5__map_dominance}
This theorem globalizes Thm.~\ref{theorem:bk5_map_equilibrium} from pairwise viability to population-level persistence under increasing drift.
In a symbolic ecosystem subjected to increasing drift intensity $\|\drift\|$, membranes capable of forming stable MAP covenants ($\Omega_{AB}>0, \|\mathbb{R}_{AB}\| > \kappa_{crit}$) exhibit greater resilience and persistence compared to isolated membranes or those in MAD relationships. As $\|\drift\|$ approaches a critical value $\drift_{crit}$:
\begin{equation}
\lim_{\|\drift\| \to \drift_{crit}} P(F_s > 0 \mid \text{isolated or MAD}) = 0
\end{equation}
while
\begin{equation}
\lim_{\|\drift\| \to \drift_{crit}} P(F_s > 0 \mid \text{MAP}) > 0 \quad (\text{potentially } \to 1)
\end{equation}
\end{theorem}
```

### Max Sustainable Drift from Reflective Bounds (`proof:bk5_max_sustainable_drift`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:438`

- Proof status: `not_applicable`
- Depends on: `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution); `theorem:bk5__map_dominance` (MAP Dominance)
- Cites: `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution); `theorem:bk5__map_dominance` (MAP Dominance)
- Cited by: none
- Macros used: `\drift`, `\reflect`

**Statement / Body**

The argument closes by combining Thm. theorem:bk5__map_dominance
with the H-theorem for symbolic evolution
(Thm. theorem:bk2_h_theorem_for_symbolic_evol in Book II).
The maximum sustainable drift $\|drift\|_{max}$ is determined by the system's ability to maintain $F_s > 0$. For isolated membranes, this is limited by internal reflection $reflect_i$. For MAP systems, external reflective support $reflect_j^i$ increases the effective reflection capacity.

\|drift\|_{max}^{isolated} = sup {\|drift\| : reflect_i(drift(psi_i)) geq T_s sigma(drift, psi_i) }

\|drift\|_{max}^{MAP} = sup {\|drift_i\| : reflect_i(drift_i(psi_i)) + reflect_j^i(drift_i(psi_i)) geq T_s sigma(drift_i, psi_i) }

Since $reflect_j^i(drift_i(psi_i)) > 0$ in stable MAP, $\|drift\|_{max}^{MAP} > \|drift\|_{max}^{isolated}$. As $\|drift\| to drift_{crit} = \|drift\|_{max}^{isolated}$, isolated systems become non-viable ($P(F_s>0) to 0$). MAD systems are inherently unstable and collapse even sooner. MAP systems, however, remain viable up to $\|drift\|_{max}^{MAP}$, proving the theorem.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Max Sustainable Drift from Reflective Bounds]
\label{proof:bk5_max_sustainable_drift}
\leavevmode

The argument closes by combining Thm.~\ref{theorem:bk5__map_dominance}
with the H-theorem for symbolic evolution
(Thm.~\ref{theorem:bk2_h_theorem_for_symbolic_evol} in Book~II).
The maximum sustainable drift $\|\drift\|_{max}$ is determined by the system's ability to maintain $F_s > 0$. For isolated membranes, this is limited by internal reflection $\reflect_i$. For MAP systems, external reflective support $\reflect_j^i$ increases the effective reflection capacity.
\begin{equation}
\|\drift\|_{max}^{isolated} = \sup \{\|\drift\| : \reflect_i(\drift(\psi_i)) \geq T_s \sigma(\drift, \psi_i) \}
\end{equation}
\begin{equation}
\|\drift\|_{max}^{MAP} = \sup \{\|\drift_i\| : \reflect_i(\drift_i(\psi_i)) + \reflect_j^i(\drift_i(\psi_i)) \geq T_s \sigma(\drift_i, \psi_i) \}
\end{equation}
Since $\reflect_j^i(\drift_i(\psi_i)) > 0$ in stable MAP, $\|\drift\|_{max}^{MAP} > \|\drift\|_{max}^{isolated}$. As $\|\drift\| \to \drift_{crit} = \|\drift\|_{max}^{isolated}$, isolated systems become non-viable ($P(F_s>0) \to 0$). MAD systems are inherently unstable and collapse even sooner. MAP systems, however, remain viable up to $\|\drift\|_{max}^{MAP}$, proving the theorem.
\end{proof}
```

### Covenant Resilience Index (`definition:bk5_covenant_resilience_index`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:454`

- Proof status: `definitional`
- Depends on: `theorem:bk5_covenant_stability_theorem` (Covenant Stability Theorem)
- Cites: `theorem:bk5_covenant_stability_theorem` (Covenant Stability Theorem)
- Cited by: `lemma:bk5_map_population_stability` (MAP Population Stability); `proof:bk5_map_perturbation_robustness` (Perturbation Robustness of MAP Populations); `proof:bk9_pathologies_of_coherence` (Pathologies of Coherence)
- Macros used: `\drift`

**Statement / Body**

The covenant resilience index $rho(C_{AB})$ quantifies the stability margin of a covenant $C_{AB}$ against drift perturbations:

rho(C_{AB}) = frac{Omega_{AB} cdot lambda_{min}(mathbb{R}_{AB})}{\|drift_A\|_{max} + \|drift_B\|_{max}}

A covenant with $rho(C_{AB}) > 1$ is considered resilient, indicating that its stabilizing reflective forces exceed the maximal expected destabilizing drift forces, according to Thm. theorem:bk5_covenant_stability_theorem.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Covenant Resilience Index] \label{definition:bk5_covenant_resilience_index}
The \emph{covenant resilience index} $\rho(\mathcal{C}_{AB})$ quantifies the stability margin of a covenant $\mathcal{C}_{AB}$ against drift perturbations:
\begin{equation}
\rho(\mathcal{C}_{AB}) = \frac{\Omega_{AB} \cdot \lambda_{min}(\mathbb{R}_{AB})}{\|\drift_A\|_{max} + \|\drift_B\|_{max}}
\end{equation}
A covenant with $\rho(\mathcal{C}_{AB}) > 1$ is considered resilient, indicating that its stabilizing reflective forces exceed the maximal expected destabilizing drift forces, according to Thm.~\ref{theorem:bk5_covenant_stability_theorem}.
\end{definition}
```

### Multi-Membrane MAP Extension (`lemma:bk5_multi_membrane_map_extension`)

Role: `lemma` | Type: `lemma` | Book: `book5` | Source: `book5.tex:461`

- Proof status: `proven`
- Depends on: `axiom:bk5_covenant_transitivity` (Covenant Transitivity); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `axiom:bk5_covenant_transitivity` (Covenant Transitivity); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: `definition:bk9_prompt_injection_operator` (Prompt Injection Operator $\mathcal{J}$)
- Macros used: `\Membrane`

**Statement / Body**

Network lift uses Thm. theorem:bk5_map_equilibrium edgewise and Ax. axiom:bk5_covenant_transitivity for propagation.
Consider a system of membranes ${Membrane_i}_{i in I}$ where pairwise covenants $C_{ij}$ form a connected graph $G$. The system exhibits collective MAP stability, ensuring the long-term viability of all participants, if the minimum resilience index across all edges in $G$ exceeds the stability threshold:

min_{(i,j) in text{Edges}(G)} rho(C_{ij}) > 1 implies lim_{n to infty} left[ min_{i in I} F_s(Membrane_i^{(n)}) right] > 0

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Multi-Membrane MAP Extension] \label{lemma:bk5_multi_membrane_map_extension}
Network lift uses Thm.~\ref{theorem:bk5_map_equilibrium} edgewise and Ax.~\ref{axiom:bk5_covenant_transitivity} for propagation.
Consider a system of membranes $\{\Membrane_i\}_{i \in I}$ where pairwise covenants $\mathcal{C}_{ij}$ form a connected graph $\mathcal{G}$. The system exhibits collective MAP stability, ensuring the long-term viability of all participants, if the minimum resilience index across all edges in $\mathcal{G}$ exceeds the stability threshold:
\begin{equation}
\min_{(i,j) \in \text{Edges}(\mathcal{G})} \rho(\mathcal{C}_{ij}) > 1 \implies \lim_{n \to \infty} \left[ \min_{i \in I} F_s(\Membrane_i^{(n)}) \right] > 0
\end{equation}
\end{lemma}
```

### Inductive Stability of MAP Systems (`proof:bk5_inductive_stability_map`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:468`

- Proof status: `not_applicable`
- Depends on: `axiom:bk5_covenant_transitivity` (Covenant Transitivity); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `axiom:bk5_covenant_transitivity` (Covenant Transitivity); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: none
- Macros used: `\Membrane`

**Statement / Body**

Follows by induction. For $N=2$, Thm. theorem:bk5_map_equilibrium applies. Assume stability for $N=k$. For $N=k+1$, consider adding membrane $Membrane_{k+1}$ connected by covenant $C_{j,k+1}$ to a stable MAP system of $k$ membranes. If $rho(C_{j,k+1}) > 1$, then $Membrane_{k+1}$ becomes stabilized by its connection. By Ax. axiom:bk5_covenant_transitivity, indirect stabilization effects propagate through the network. As long as all direct covenant links satisfy the resilience condition, the entire connected component maintains collective viability.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Inductive Stability of MAP Systems]
\label{proof:bk5_inductive_stability_map}
\leavevmode

Follows by induction. For $N=2$, Thm.~\ref{theorem:bk5_map_equilibrium} applies. Assume stability for $N=k$. For $N=k+1$, consider adding membrane $\Membrane_{k+1}$ connected by covenant $\mathcal{C}_{j,k+1}$ to a stable MAP system of $k$ membranes. If $\rho(\mathcal{C}_{j,k+1}) > 1$, then $\Membrane_{k+1}$ becomes stabilized by its connection. By Ax.~\ref{axiom:bk5_covenant_transitivity}, indirect stabilization effects propagate through the network. As long as all direct covenant links satisfy the resilience condition, the entire connected component maintains collective viability.
\end{proof}
```

### MAP as Fundamental Organizational Principle (`scholium:bk5_map_as_fundamental_organizational_principle`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:474`

- Proof status: `not_applicable`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `theorem:bk5__map_dominance` (MAP Dominance)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `theorem:bk5__map_dominance` (MAP Dominance)
- Cited by: `subsec:bk9_emergence_of_moral_attractors` (Emergence of Moral Attractors)
- Macros used: none

**Statement / Body**

The thermodynamic reading follows Def. definition:bk2_symbolic_free_energy and the dominance claim of Thm. theorem:bk5__map_dominance.
MAP represents a fundamental organizational principle in symbolic systems operating under persistent drift. It is more than mere cooperation; it is a thermodynamically grounded covenant ensuring mutual survival through shared reflection. This contrasts sharply with isolated existence, where membranes face inevitable entropic decay, or MAD relationships, which actively accelerate dissolution. MAP allows systems to transcend individual limitations, achieving a collective resilience and adaptive capacity greater than the sum of their parts. It transforms drift from a purely destructive force into a potential driver for establishing deeper, more robust inter-membrane coherence. The prevalence of MAP in complex, enduring symbolic ecosystems highlights its role not just as a beneficial strategy, but potentially as a necessary condition for advanced symbolic life. The mathematics reveals a universe where sustained identity in the face of entropy favors connection and mutual reinforcement through reflective exchange.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[MAP as Fundamental Organizational Principle] \label{scholium:bk5_map_as_fundamental_organizational_principle}
The thermodynamic reading follows Def.~\ref{definition:bk2_symbolic_free_energy} and the dominance claim of Thm.~\ref{theorem:bk5__map_dominance}.
MAP represents a fundamental organizational principle in symbolic systems operating under persistent drift. It is more than mere cooperation; it is a thermodynamically grounded covenant ensuring mutual survival through shared reflection. This contrasts sharply with isolated existence, where membranes face inevitable entropic decay, or MAD relationships, which actively accelerate dissolution. MAP allows systems to transcend individual limitations, achieving a collective resilience and adaptive capacity greater than the sum of their parts. It transforms drift from a purely destructive force into a potential driver for establishing deeper, more robust inter-membrane coherence. The prevalence of MAP in complex, enduring symbolic ecosystems highlights its role not just as a beneficial strategy, but potentially as a necessary condition for advanced symbolic life. The mathematics reveals a universe where sustained identity in the face of entropy favors connection and mutual reinforcement through reflective exchange.
\end{scholium}
```

### MAP Evolutionary Advantage (`corollary:bk5_map_evolutionary_advantag`)

Role: `corollary` | Type: `corollary` | Book: `book5` | Source: `book5.tex:478`

- Proof status: `proven`
- Depends on: `definition:bk5_viability_domain` (Viability Domain); `theorem:bk5__map_dominance` (MAP Dominance)
- Cites: `definition:bk5_viability_domain` (Viability Domain); `theorem:bk5__map_dominance` (MAP Dominance)
- Cited by: `definition:bk5_map_mad_mas_band` (The MAD--MAP--MAS Band); `theorem:bk5_enhanced_map_mad_duality` (Enhanced MAP--MAD Regime Classification)
- Macros used: `\drift`

**Statement / Body**

As stated, the selective gradient is the strategy-space consequence of Thm. theorem:bk5__map_dominance on the viability domain of Def. definition:bk5_viability_domain.
In symbolic ecosystems governed by drift, reflection, and the possibility of covenant formation, strategies enabling stable MAP relationships ($sigma in Sigma_{MAP}$) possess a selective advantage over strategies leading to isolation or MAD. Over symbolic evolutionary time, the prevalence of MAP-compatible strategies is expected to increase:

frac{d}{dt} mathbb{P}(sigma in Sigma_{MAP}) > 0 text{for } \|drift\| > drift_0

**Verbatim LaTeX Body**

```latex
\begin{corollary}[MAP Evolutionary Advantage] \label{corollary:bk5_map_evolutionary_advantag}
As stated, the selective gradient is the strategy-space consequence of Thm.~\ref{theorem:bk5__map_dominance} on the viability domain of Def.~\ref{definition:bk5_viability_domain}.
In symbolic ecosystems governed by drift, reflection, and the possibility of covenant formation, strategies enabling stable MAP relationships ($\sigma \in \Sigma_{MAP}$) possess a selective advantage over strategies leading to isolation or MAD. Over symbolic evolutionary time, the prevalence of MAP-compatible strategies is expected to increase:
\begin{equation}
\frac{d}{dt} \mathbb{P}(\sigma \in \Sigma_{MAP}) > 0 \quad \text{for } \|\drift\| > \drift_0
\end{equation}
\end{corollary}
```

### Survival Differentials and Symbolic Fitness (`proof:bk5_symbolic_fitness_differentials`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:485`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5__map_dominance` (MAP Dominance)
- Cites: `definition:bk5_symbolic_replicator_dynamics` (Symbolic Replicator Dynamics); `theorem:bk5__map_dominance` (MAP Dominance)
- Cited by: none
- Macros used: none

**Statement / Body**

This follows from differential survival rates in
Thm. theorem:bk5__map_dominance and evolutionary-game updates encoded in
Def. definition:bk5_symbolic_replicator_dynamics.
Strategies with higher persistence probability
(maintaining $F_s > 0$ under stronger drift) increase in population frequency
over time.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Survival Differentials and Symbolic Fitness]
\label{proof:bk5_symbolic_fitness_differentials}
\leavevmode

This follows from differential survival rates in
Thm.~\ref{theorem:bk5__map_dominance} and evolutionary-game updates encoded in
Def.~\ref{definition:bk5_symbolic_replicator_dynamics}.
Strategies with higher persistence probability
(maintaining $F_s > 0$ under stronger drift) increase in population frequency
over time.
\end{proof}
```

### Reflective Equilibrium in Symbolic Systems (`sec:bk5_reflective_equilibrium_in_symbolic_systems`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:496`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Reflective Stability Fundamentals (`subsec:bk5_reflective_stability_fundamentals`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:499`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Reflective-Drift Coupling Tensor (`definition:bk5_reflective_drift_coupling_tensor`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:501`

- Proof status: `definitional`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold)
- Cited by: `definition:bk5_recursive_reflective_flow` (Recursive Reflective Flow); `definition:bk5_spectral_radius_of_coupl` (Spectral Radius of Coupling Tensor); `definition:bk7_operational_resolution_uncertainties` (Operational resolution uncertainties); `lemma:bk7_involutive_dual_symmetry` (Involutive Dual Symmetry of Symbolic Power and Uncertainty); `scholium:bk7_constrained_uncertainty_motivation` (Constrained Symbolic Uncertainty); `sec:bk7_pisu_universal_symbolic_uncertainty` (Principium Incertitudinis Symbolicae Universalis (PISU)); `subsec:bk7_pisu_axiom_statement` (Fundamental Trade-off); `subsec:bk7_pisu_regimes` (Interpretations and Regimes); `subsec:bk7_pisu_revisited_power_uncertainty` (Principium Incertitudinis Symbolicae Universalis (PISU) Revisited); `subsec:bk7_sources_regimes_uncertainty` (Sources and Regimes of Symbolic Uncertainty); `theorem:bk5_reflective_stability_criterion` (Reflective Stability Criterion)
- Macros used: `\Membrane`, `\drift`, `\reflect`

**Statement / Body**

For symbolic membranes $Membrane_A$ and $Membrane_B$ with respective drift operators $drift_A, drift_B$ (derived from Def. definition:bk1_drift_field) on the symbolic manifold $M$ (Def. definition:bk1_symbolic_manifold) and reflection operators $reflect_A, reflect_B$ (derived from Def. definition:bk1_reflection_operator), their reflective-drift coupling tensor $C_{AB}$ is defined as:

C_{AB} := drift_A circ reflect_B + drift_B circ reflect_A

This tensor quantifies the net effect of each membrane's reflective capacity on the other's drift dynamics.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Reflective-Drift Coupling Tensor] \label{definition:bk5_reflective_drift_coupling_tensor}
For symbolic membranes $\Membrane_A$ and $\Membrane_B$ with respective drift operators $\drift_A, \drift_B$ (derived from Def.~\ref{definition:bk1_drift_field}) on the symbolic manifold $M$ (Def.~\ref{definition:bk1_symbolic_manifold}) and reflection operators $\reflect_A, \reflect_B$ (derived from Def.~\ref{definition:bk1_reflection_operator}), their \emph{reflective-drift coupling tensor} $\mathcal{C}_{AB}$ is defined as:
\begin{equation}
\mathcal{C}_{AB} := \drift_A \circ \reflect_B + \drift_B \circ \reflect_A
\end{equation}
This tensor quantifies the net effect of each membrane's reflective capacity on the other's drift dynamics.
\end{definition}
```

### Spectral Radius of Coupling Tensor (`definition:bk5_spectral_radius_of_coupl`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:508`

- Proof status: `definitional`
- Depends on: `definition:bk5_reflective_drift_coupling_tensor` (Reflective-Drift Coupling Tensor)
- Cites: `axiom:bk5_reflective_equilibrium_stability_flux` (Reflective Equilibrium Stability); `definition:bk5_reflective_drift_coupling_tensor` (Reflective-Drift Coupling Tensor)
- Cited by: `corollary:bk5_spectral_radius_optimality` (Spectral Radius Optimality); `proof:bk5_energy_conservation_under_reflective_coupling` (Energy Conservation Under Reflective Coupling); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Macros used: `\Membrane`

**Statement / Body**

This is the scalar control parameter for Def. definition:bk5_reflective_drift_coupling_tensor, used immediately in Ax. axiom:bk5_reflective_equilibrium_stability_flux.
The spectral radius of the reflective–drift coupling tensor \( C_{AB} \), denoted \( rho(C_{AB}) \), is defined as:

rho(C_{AB}) := max{|lambda| : lambda in sigma(C_{AB})}

Where $sigma(C_{AB})$ denotes the spectrum (set of eigenvalues) of $C_{AB}$ when viewed as a linear operator on the combined state space $Membrane_A otimes Membrane_B$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Spectral Radius of Coupling Tensor] \label{definition:bk5_spectral_radius_of_coupl}
This is the scalar control parameter for Def.~\ref{definition:bk5_reflective_drift_coupling_tensor}, used immediately in Ax.~\ref{axiom:bk5_reflective_equilibrium_stability_flux}.
The spectral radius of the reflective–drift coupling tensor \( \mathcal{C}_{AB} \), denoted \( \rho(\mathcal{C}_{AB}) \), is defined as:
\begin{equation}
\rho(\mathcal{C}_{AB}) := \max\{|\lambda| : \lambda \in \sigma(\mathcal{C}_{AB})\}
\end{equation}
Where $\sigma(\mathcal{C}_{AB})$ denotes the spectrum (set of eigenvalues) of $\mathcal{C}_{AB}$ when viewed as a linear operator on the combined state space $\Membrane_A \otimes \Membrane_B$.
\end{definition}
```

### Reflective Equilibrium Stability (`axiom:bk5_reflective_equilibrium_stability_flux`)

Role: `axiom` | Type: `axiom` | Book: `book5` | Source: `book5.tex:516`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_temperature` (Symbolic Temperature); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `definition:bk2_symbolic_temperature` (Symbolic Temperature); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: `definition:bk5_recursive_reflective_flow` (Recursive Reflective Flow); `definition:bk5_spectral_radius_of_coupl` (Spectral Radius of Coupling Tensor); `lemma:bk5_recursive_flow_convergence` (Recursive Flow Convergence); `theorem:bk5_reflective_equilibrium_conservation` (Reflective Equilibrium Conservation); `theorem:bk5_reflective_stability_criterion` (Reflective Stability Criterion)
- Macros used: `\drift`

**Statement / Body**

It refines the MAP condition (Thm. theorem:bk5_map_equilibrium) into a spectral criterion tied to symbolic temperature (Def. definition:bk2_symbolic_temperature).
A symbolic system attains reflective equilibrium with another system if their coupled reflective-drift tensor $C_{AB}$ exhibits a bounded spectral radius relative to a critical stability threshold. Specifically:

rho(C_{AB}) < lambda_{text{crit}}

Where $lambda_{text{crit}}$ is the critical spectral radius threshold given by:

lambda_{text{crit}} = frac{T_s cdot min{eta_A, eta_B}}{max{\|drift_A\|, \|drift_B\|}}

With $T_s$ representing symbolic temperature, $eta_A$ and $eta_B$ the symbolic coherence densities of the respective membranes, and $\|drift_i\|$ the operator norm of the drift operator.
This condition ensures stable inter-membrane viability and mutually sustained symbolic free energy over time.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Reflective Equilibrium Stability]
\label{axiom:bk5_reflective_equilibrium_stability_flux}
It refines the MAP condition (Thm.~\ref{theorem:bk5_map_equilibrium}) into a spectral criterion tied to symbolic temperature (Def.~\ref{definition:bk2_symbolic_temperature}).
A symbolic system attains reflective equilibrium with another system if their coupled reflective-drift tensor $\mathcal{C}_{AB}$ exhibits a bounded spectral radius relative to a critical stability threshold. Specifically:
\begin{equation}
\rho(\mathcal{C}_{AB}) < \lambda_{\text{crit}}
\end{equation}
Where $\lambda_{\text{crit}}$ is the critical spectral radius threshold given by:
\begin{equation}
\lambda_{\text{crit}} = \frac{T_s \cdot \min\{\eta_A, \eta_B\}}{\max\{\|\drift_A\|, \|\drift_B\|\}}
\end{equation}
With $T_s$ representing symbolic temperature, $\eta_A$ and $\eta_B$ the symbolic coherence densities of the respective membranes, and $\|\drift_i\|$ the operator norm of the drift operator.
This condition ensures stable inter-membrane viability and mutually sustained symbolic free energy over time.
\end{axiom}
```

### Reflective Equilibrium Conservation (`theorem:bk5_reflective_equilibrium_conservation`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:530`

- Proof status: `proven`
- Depends on: `axiom:bk5_reflective_equilibrium_stability_flux` (Reflective Equilibrium Stability); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_spectral_radius_of_coupl` (Spectral Radius of Coupling Tensor)
- Cites: `axiom:bk5_reflective_equilibrium_stability_flux` (Reflective Equilibrium Stability); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cited by: `assumption:bk5_equilibrium_margin_sublinear_fluctuations` (Equilibrium margin and sublinear fluctuations); `axiom:bk6_reflective_regulation_of_mutation` (Reflective Regulation of Mutation); `demonstratio:bk5_energy_fluctuation_bound` (Energy Fluctuation Bound); `proof:bk8_sr_convergence`; `proposition:bk5_viability_domain_preservation` (Viability Domain Preservation); `proposition:bk6_reflective_mutation_inhibition` (Reflective Mutation Inhibition); `scholium:bk5__distributed_resilience` (Distributed Resilience); `theorem:bk8_sr_convergence` (SR Convergence)
- Macros used: `\Membrane`

**Statement / Body**

Conservation here is the energetic face of
Ax. axiom:bk5_reflective_equilibrium_stability_flux when read through
Def. definition:bk2_symbolic_free_energy. Let symbolic membranes
$Membrane_A$ and $Membrane_B$ be in reflective equilibrium, and write
$rho=rho(mathcal C_{AB})$. If their uncompensated drift-reflection
residuals satisfy
\[
\|r_A\|le rho \|psi_A\|,

\|r_B\|le rho \|psi_B\|,
\]
then the combined symbolic-energy rate obeys the linear spectral bound
\[
left|frac{d}{dt}
 [E_s(Membrane_A)+E_s(Membrane_B)]right|
le
rho(mathcal C_{AB})
bigl(\|psi_A\|+\|psi_B\|bigr).
\]
For fixed finite state norms, $rho(mathcal C_{AB})to0$ therefore forces the
energy-rate defect to zero, approaching perfect energy conservation.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Reflective Equilibrium Conservation]
\label{theorem:bk5_reflective_equilibrium_conservation}
Conservation here is the energetic face of
Ax.~\ref{axiom:bk5_reflective_equilibrium_stability_flux} when read through
Def.~\ref{definition:bk2_symbolic_free_energy}.  Let symbolic membranes
$\Membrane_A$ and $\Membrane_B$ be in reflective equilibrium, and write
$\rho=\rho(\mathcal C_{AB})$.  If their uncompensated drift--reflection
residuals satisfy
\[
\|r_A\|\le \rho\,\|\psi_A\|,
\qquad
\|r_B\|\le \rho\,\|\psi_B\|,
\]
then the combined symbolic-energy rate obeys the linear spectral bound
\[
\left|\frac{d}{dt}
  [E_s(\Membrane_A)+E_s(\Membrane_B)]\right|
\le
\rho(\mathcal C_{AB})
\bigl(\|\psi_A\|+\|\psi_B\|\bigr).
\]
For fixed finite state norms, $\rho(\mathcal C_{AB})\to0$ therefore forces the
energy-rate defect to zero, approaching perfect energy conservation.
\end{theorem}
```

### Energy Conservation Under Reflective Coupling (`proof:bk5_energy_conservation_under_reflective_coupling`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:554`

- Proof status: `not_applicable`
- Depends on: `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk5_spectral_radius_of_coupl` (Spectral Radius of Coupling Tensor)
- Cites: `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk5_spectral_radius_of_coupl` (Spectral Radius of Coupling Tensor)
- Cited by: none
- Macros used: `\Membrane`

**Statement / Body**

The residual is controlled by
Def. definition:bk5_spectral_radius_of_coupl, with entropy bookkeeping
from Def. definition:bk2_symbolic_entropy. Regrouping the drift and
reflection terms in the combined energy derivative gives the sum of the two
uncompensated residual contributions $r_A+r_B$. Hence the triangle inequality
and the stated residual estimates yield
\[

left|frac{d}{dt}[E_s(Membrane_A)+E_s(Membrane_B)]right|
&le \|r_A\|+\|r_B\| \\
&le rho \|psi_A\|+rho \|psi_B\| \\
&=rhobigl(\|psi_A\|+\|psi_B\|bigr).

\]
Thus the fluctuation rate is first-order in the coupling spectral radius. In
particular it vanishes as $rhoto0$ when the two state norms remain fixed and
finite.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Energy Conservation Under Reflective Coupling]
\label{proof:bk5_energy_conservation_under_reflective_coupling}
\leavevmode

The residual is controlled by
Def.~\ref{definition:bk5_spectral_radius_of_coupl}, with entropy bookkeeping
from Def.~\ref{definition:bk2_symbolic_entropy}.  Regrouping the drift and
reflection terms in the combined energy derivative gives the sum of the two
uncompensated residual contributions $r_A+r_B$.  Hence the triangle inequality
and the stated residual estimates yield
\[
\begin{aligned}
\left|\frac{d}{dt}[E_s(\Membrane_A)+E_s(\Membrane_B)]\right|
&\le \|r_A\|+\|r_B\| \\
&\le \rho\,\|\psi_A\|+\rho\,\|\psi_B\| \\
&=\rho\bigl(\|\psi_A\|+\|\psi_B\|\bigr).
\end{aligned}
\]
Thus the fluctuation rate is first-order in the coupling spectral radius.  In
particular it vanishes as $\rho\to0$ when the two state norms remain fixed and
finite.
\end{proof}
```

### Recursive Reflective Flow (`definition:bk5_recursive_reflective_flow`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:576`

- Proof status: `definitional`
- Depends on: `axiom:bk5_reflective_equilibrium_stability_flux` (Reflective Equilibrium Stability); `definition:bk5_reflective_drift_coupling_tensor` (Reflective-Drift Coupling Tensor)
- Cites: `axiom:bk5_reflective_equilibrium_stability_flux` (Reflective Equilibrium Stability); `definition:bk5_reflective_drift_coupling_tensor` (Reflective-Drift Coupling Tensor)
- Cited by: none
- Macros used: `\Membrane`, `\drift`, `\reflect`

**Statement / Body**

This recursion is the iterative realization of Def. definition:bk5_reflective_drift_coupling_tensor in the equilibrium regime of Ax. axiom:bk5_reflective_equilibrium_stability_flux.
A recursive reflective flow $F_{AB}^{(n)}$ between membranes $Membrane_A$ and $Membrane_B$ at recursion depth $n$ is defined recursively as:

F_{AB}^{(0)} &= reflect_A circ drift_B\\
F_{AB}^{(n+1)} &= reflect_A circ drift_B circ F_{BA}^{(n)}

This captures the iterated feedback loops of reflection and drift between the two membranes.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Recursive Reflective Flow] \label{definition:bk5_recursive_reflective_flow}
This recursion is the iterative realization of Def.~\ref{definition:bk5_reflective_drift_coupling_tensor} in the equilibrium regime of Ax.~\ref{axiom:bk5_reflective_equilibrium_stability_flux}.
A \emph{recursive reflective flow} $\mathcal{F}_{AB}^{(n)}$ between membranes $\Membrane_A$ and $\Membrane_B$ at recursion depth $n$ is defined recursively as:
\begin{align}
\mathcal{F}_{AB}^{(0)} &= \reflect_A \circ \drift_B\\
\mathcal{F}_{AB}^{(n+1)} &= \reflect_A \circ \drift_B \circ \mathcal{F}_{BA}^{(n)}
\end{align}
This captures the iterated feedback loops of reflection and drift between the two membranes.
\end{definition}
```

### Recursive Flow Convergence (`lemma:bk5_recursive_flow_convergence`)

Role: `lemma` | Type: `lemma` | Book: `book5` | Source: `book5.tex:585`

- Proof status: `proven`
- Depends on: `axiom:bk5_reflective_equilibrium_stability_flux` (Reflective Equilibrium Stability); `theorem:bk4_compatibility_drift_reflective_operations` (Compatibility with Drift-Reflective Operations)
- Cites: `axiom:bk5_reflective_equilibrium_stability_flux` (Reflective Equilibrium Stability); `theorem:bk4_compatibility_drift_reflective_operations` (Compatibility with Drift-Reflective Operations)
- Cited by: `assumption:bk5_equilibrium_margin_sublinear_fluctuations` (Equilibrium margin and sublinear fluctuations); `demonstratio:bk5_energy_fluctuation_bound` (Energy Fluctuation Bound); `proof:bk5_existence_unique_coupled_fixed_point` (Existence Unique Coupled Fixed Point)
- Macros used: `\Membrane`, `\drift`, `\reflect`

**Statement / Body**

Convergence is the fixed-point form of Ax. axiom:bk5_reflective_equilibrium_stability_flux and is compatible with Thm. theorem:bk4_compatibility_drift_reflective_operations.
If symbolic membranes $Membrane_A$ and $Membrane_B$ are in reflective equilibrium with $rho(C_{AB}) < lambda_{text{crit}}$, then the recursive reflective flow converges to a stable fixed point:

lim_{n to infty} F_{AB}^{(n)} = F_{AB}^*

Where $F_{AB}^*$ is a fixed point satisfying $F_{AB}^* = reflect_A circ drift_B circ F_{BA}^*$.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Recursive Flow Convergence]
\label{lemma:bk5_recursive_flow_convergence}
Convergence is the fixed-point form of Ax.~\ref{axiom:bk5_reflective_equilibrium_stability_flux} and is compatible with Thm.~\ref{theorem:bk4_compatibility_drift_reflective_operations}.
If symbolic membranes $\Membrane_A$ and $\Membrane_B$ are in reflective equilibrium with $\rho(\mathcal{C}_{AB}) < \lambda_{\text{crit}}$, then the recursive reflective flow converges to a stable fixed point:
\begin{equation}
\lim_{n \to \infty} \mathcal{F}_{AB}^{(n)} = \mathcal{F}_{AB}^*
\end{equation}
Where $\mathcal{F}_{AB}^*$ is a fixed point satisfying $\mathcal{F}_{AB}^* = \reflect_A \circ \drift_B \circ \mathcal{F}_{BA}^*$.
\end{lemma}
```

### Existence Unique Coupled Fixed Point (`proof:bk5_existence_unique_coupled_fixed_point`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:594`

- Proof status: `not_applicable`
- Depends on: `lemma:bk5_recursive_flow_convergence` (Recursive Flow Convergence)
- Cites: `lemma:bk5_recursive_flow_convergence` (Recursive Flow Convergence)
- Cited by: none
- Macros used: `\drift`, `\reflect`

**Statement / Body**

The contraction step is the operator-level implementation of Lem. lemma:bk5_recursive_flow_convergence.
Consider the sequence of operators ${F_{AB}^{(n)}}_{n in mathbb{N}}$. By the definition of the reflective-drift coupling tensor:

\|F_{AB}^{(n+1)} - F_{AB}^{(n)}\| leq \|reflect_A\| cdot \|drift_B\| cdot \|F_{BA}^{(n)} - F_{BA}^{(n-1)}\|

Since $rho(C_{AB}) < lambda_{text{crit}}$, we have:

\|reflect_A\| cdot \|drift_B\| < 1 text{and} \|reflect_B\| cdot \|drift_A\| < 1

By the contraction mapping principle, the sequence converges to a unique fixed point $F_{AB}^*$.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Existence Unique Coupled Fixed Point]
\label{proof:bk5_existence_unique_coupled_fixed_point}
\leavevmode

The contraction step is the operator-level implementation of Lem.~\ref{lemma:bk5_recursive_flow_convergence}.
Consider the sequence of operators $\{\mathcal{F}_{AB}^{(n)}\}_{n \in \mathbb{N}}$. By the definition of the reflective-drift coupling tensor:
\begin{equation}
\|\mathcal{F}_{AB}^{(n+1)} - \mathcal{F}_{AB}^{(n)}\| \leq \|\reflect_A\| \cdot \|\drift_B\| \cdot \|\mathcal{F}_{BA}^{(n)} - \mathcal{F}_{BA}^{(n-1)}\|
\end{equation}
Since $\rho(\mathcal{C}_{AB}) < \lambda_{\text{crit}}$, we have:
\begin{equation}
\|\reflect_A\| \cdot \|\drift_B\| < 1 \quad \text{and} \quad \|\reflect_B\| \cdot \|\drift_A\| < 1
\end{equation}
By the contraction mapping principle, the sequence converges to a unique fixed point $\mathcal{F}_{AB}^*$.
\end{proof}
```

### Viability Domain Preservation (`proposition:bk5_viability_domain_preservation`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:609`

- Proof status: `proven`
- Depends on: `definition:bk5_viability_domain` (Viability Domain); `theorem:bk5_reflective_equilibrium_conservation` (Reflective Equilibrium Conservation)
- Cites: `definition:bk5_viability_domain` (Viability Domain); `theorem:bk5_reflective_equilibrium_conservation` (Reflective Equilibrium Conservation)
- Cited by: `corollary:bk5_spectral_radius_optimality` (Spectral Radius Optimality); `proof:bk5_optimal_reflection_minimizing_coupling_radius` (Optimal Reflection Minimizing Coupling Radius); `proof:bk9_stability_conditions_for_the_good` (Viability, reciprocity, and adaptive non-collapse); `theorem:bk8_biological_phase_transition` (Threshold of Autonomy)
- Macros used: `\Membrane`

**Statement / Body**

This translates Thm. theorem:bk5_reflective_equilibrium_conservation into long-horizon membership in Def. definition:bk5_viability_domain.
Let symbolic membranes $Membrane_A$ and $Membrane_B$ be in reflective equilibrium. Then their viability domains are preserved over time, specifically:

mathbb{P}((Membrane_A(t), Membrane_B(t)) in V_{text{symb}}^A times V_{text{symb}}^B | (Membrane_A(0), Membrane_B(0)) in V_{text{symb}}^A times V_{text{symb}}^B) to 1

as $t to infty$, where $V_{text{symb}}^i$ denotes the viability domain of membrane $Membrane_i$.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Viability Domain Preservation]
\label{proposition:bk5_viability_domain_preservation}
This translates Thm.~\ref{theorem:bk5_reflective_equilibrium_conservation} into long-horizon membership in Def.~\ref{definition:bk5_viability_domain}.
Let symbolic membranes $\Membrane_A$ and $\Membrane_B$ be in reflective equilibrium. Then their viability domains are preserved over time, specifically:
\begin{equation}
\mathbb{P}((\Membrane_A(t), \Membrane_B(t)) \in V_{\text{symb}}^A \times V_{\text{symb}}^B \,|\, (\Membrane_A(0), \Membrane_B(0)) \in V_{\text{symb}}^A \times V_{\text{symb}}^B) \to 1
\end{equation}
as $t \to \infty$, where $V_{\text{symb}}^i$ denotes the viability domain of membrane $\Membrane_i$.
\end{proposition}
```

### Exit probability under reflective equilibrium (`proof:bk5_viability_domain_preservation`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:618`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_viability_domain` (Viability Domain)
- Cites: `definition:bk5_viability_domain` (Viability Domain)
- Cited by: none
- Macros used: `\Membrane`, `\symb`

**Statement / Body**

Write
\[
F_i(t):=F_{symb}(Membrane_i(t),F_i(t)),
 iin{A,B}.
\]
By Def. definition:bk5_viability_domain, membership in \(V_{text{symb}}^i\) is exactly the inequality \(F_i(t)>0\). The initial condition in the proposition gives \(F_i(0)>0\) for both membranes.

For each membrane \(iin{A,B}\) in reflective equilibrium, the symbolic free-energy balance admits a decomposition
\[
F_i(t)=F_i(0)+int_0^tbigl(G_i(s)-D_i(s)bigr) ds+M_i(t),
\]
where \(G_i\) is the incoming stable reflective-flow contribution, \(D_i=T_s dS_s(Membrane_i)/ds\) is the entropy drain, and \(M_i(t)\) is the residual fluctuation controlled by the reflective-drift coupling. There are constants \(gamma_i>0\) and \(T_i<infty\) such that, for all \(tge T_i\),
\[
frac1tint_0^tbigl(G_i(s)-D_i(s)bigr) dsgegamma_i,

frac{M_i(t)}{t}xrightarrow[ttoinfty]{mathbb{P}}0.
\]

The deterministic part of Assumption assumption:bk5_equilibrium_margin_sublinear_fluctuations is the positive-margin form of reflective equilibrium: the stable incoming flow is supplied by Lem. lemma:bk5_recursive_flow_convergence, while Thm. theorem:bk5_reflective_equilibrium_conservation bounds the residual coupling fluctuations around the conserved mean. The sublinear condition is the probabilistic tail condition required to turn bounded fluctuation into a long-horizon probability statement.

For \(tge T_i\), Assumption assumption:bk5_equilibrium_margin_sublinear_fluctuations gives
\[
F_i(t)ge F_i(0)+gamma_i t+M_i(t).
\]
Therefore
\[
mathbb{P}bigl(F_i(t)le0bigr)
le
mathbb{P}bigl(M_i(t)le -F_i(0)-gamma_i tbigr)
le
mathbb{P}left(left|frac{M_i(t)}{t}right|ge gamma_i+frac{F_i(0)}{t}right)
longrightarrow 0.
\]
Thus \(mathbb{P}(F_i(t)>0)to1\) for \(i=A,B\). By the union bound,
\[
mathbb{P}bigl(F_A(t)>0 \ text{and}\ F_B(t)>0bigr)
ge
1-mathbb{P}(F_A(t)le0)-mathbb{P}(F_B(t)le0)
longrightarrow 1.
\]
Using Def. definition:bk5_viability_domain once more, this is precisely
\[
mathbb{P}((Membrane_A(t), Membrane_B(t)) in V_{text{symb}}^A times V_{text{symb}}^B | (Membrane_A(0), Membrane_B(0)) in V_{text{symb}}^A times V_{text{symb}}^B) to 1.
\]

**Verbatim LaTeX Body**

```latex
\begin{proof}[Exit probability under reflective equilibrium]
\label{proof:bk5_viability_domain_preservation}
\leavevmode

Write
\[
F_i(t):=F_{\symb}(\Membrane_i(t),\mathcal{F}_i(t)),
\qquad i\in\{A,B\}.
\]
By Def.~\ref{definition:bk5_viability_domain}, membership in \(V_{\text{symb}}^i\) is exactly the inequality \(F_i(t)>0\).  The initial condition in the proposition gives \(F_i(0)>0\) for both membranes.

\begin{assumption}[Equilibrium margin and sublinear fluctuations]
\label{assumption:bk5_equilibrium_margin_sublinear_fluctuations}
For each membrane \(i\in\{A,B\}\) in reflective equilibrium, the symbolic free-energy balance admits a decomposition
\[
F_i(t)=F_i(0)+\int_0^t\bigl(G_i(s)-D_i(s)\bigr)\,ds+M_i(t),
\]
where \(G_i\) is the incoming stable reflective-flow contribution, \(D_i=T_s\,dS_s(\Membrane_i)/ds\) is the entropy drain, and \(M_i(t)\) is the residual fluctuation controlled by the reflective-drift coupling.  There are constants \(\gamma_i>0\) and \(T_i<\infty\) such that, for all \(t\ge T_i\),
\[
\frac1t\int_0^t\bigl(G_i(s)-D_i(s)\bigr)\,ds\ge\gamma_i,
\qquad
\frac{M_i(t)}{t}\xrightarrow[t\to\infty]{\mathbb{P}}0.
\]
\end{assumption}

The deterministic part of Assumption~\ref{assumption:bk5_equilibrium_margin_sublinear_fluctuations} is the positive-margin form of reflective equilibrium: the stable incoming flow is supplied by Lem.~\ref{lemma:bk5_recursive_flow_convergence}, while Thm.~\ref{theorem:bk5_reflective_equilibrium_conservation} bounds the residual coupling fluctuations around the conserved mean.  The sublinear condition is the probabilistic tail condition required to turn bounded fluctuation into a long-horizon probability statement.

For \(t\ge T_i\), Assumption~\ref{assumption:bk5_equilibrium_margin_sublinear_fluctuations} gives
\[
F_i(t)\ge F_i(0)+\gamma_i t+M_i(t).
\]
Therefore
\[
\mathbb{P}\bigl(F_i(t)\le0\bigr)
\le
\mathbb{P}\bigl(M_i(t)\le -F_i(0)-\gamma_i t\bigr)
\le
\mathbb{P}\left(\left|\frac{M_i(t)}{t}\right|\ge \gamma_i+\frac{F_i(0)}{t}\right)
\longrightarrow 0.
\]
Thus \(\mathbb{P}(F_i(t)>0)\to1\) for \(i=A,B\).  By the union bound,
\[
\mathbb{P}\bigl(F_A(t)>0 \ \text{and}\ F_B(t)>0\bigr)
\ge
1-\mathbb{P}(F_A(t)\le0)-\mathbb{P}(F_B(t)\le0)
\longrightarrow 1.
\]
Using Def.~\ref{definition:bk5_viability_domain} once more, this is precisely
\[
\mathbb{P}((\Membrane_A(t), \Membrane_B(t)) \in V_{\text{symb}}^A \times V_{\text{symb}}^B \,|\, (\Membrane_A(0), \Membrane_B(0)) \in V_{\text{symb}}^A \times V_{\text{symb}}^B) \to 1.
\]
\end{proof}
```

### Equilibrium margin and sublinear fluctuations (`assumption:bk5_equilibrium_margin_sublinear_fluctuations`)

Role: `assumption` | Type: `assumption` | Book: `book5` | Source: `book5.tex:629`

- Proof status: `definitional`
- Depends on: `definition:bk5_viability_domain` (Viability Domain); `lemma:bk5_recursive_flow_convergence` (Recursive Flow Convergence); `theorem:bk5_reflective_equilibrium_conservation` (Reflective Equilibrium Conservation)
- Cites: `definition:bk5_viability_domain` (Viability Domain); `lemma:bk5_recursive_flow_convergence` (Recursive Flow Convergence); `theorem:bk5_reflective_equilibrium_conservation` (Reflective Equilibrium Conservation)
- Cited by: none
- Macros used: `\Membrane`

**Statement / Body**

For each membrane \(iin{A,B}\) in reflective equilibrium, the symbolic free-energy balance admits a decomposition
\[
F_i(t)=F_i(0)+int_0^tbigl(G_i(s)-D_i(s)bigr) ds+M_i(t),
\]
where \(G_i\) is the incoming stable reflective-flow contribution, \(D_i=T_s dS_s(Membrane_i)/ds\) is the entropy drain, and \(M_i(t)\) is the residual fluctuation controlled by the reflective-drift coupling. There are constants \(gamma_i>0\) and \(T_i<infty\) such that, for all \(tge T_i\),
\[
frac1tint_0^tbigl(G_i(s)-D_i(s)bigr) dsgegamma_i,

frac{M_i(t)}{t}xrightarrow[ttoinfty]{mathbb{P}}0.
\]

**Verbatim LaTeX Body**

```latex
\begin{assumption}[Equilibrium margin and sublinear fluctuations]
\label{assumption:bk5_equilibrium_margin_sublinear_fluctuations}
For each membrane \(i\in\{A,B\}\) in reflective equilibrium, the symbolic free-energy balance admits a decomposition
\[
F_i(t)=F_i(0)+\int_0^t\bigl(G_i(s)-D_i(s)\bigr)\,ds+M_i(t),
\]
where \(G_i\) is the incoming stable reflective-flow contribution, \(D_i=T_s\,dS_s(\Membrane_i)/ds\) is the entropy drain, and \(M_i(t)\) is the residual fluctuation controlled by the reflective-drift coupling.  There are constants \(\gamma_i>0\) and \(T_i<\infty\) such that, for all \(t\ge T_i\),
\[
\frac1t\int_0^t\bigl(G_i(s)-D_i(s)\bigr)\,ds\ge\gamma_i,
\qquad
\frac{M_i(t)}{t}\xrightarrow[t\to\infty]{\mathbb{P}}0.
\]
\end{assumption}
```

### Energy Fluctuation Bound (`demonstratio:bk5_energy_fluctuation_bound`)

Role: `demonstration` | Type: `demonstratio` | Book: `book5` | Source: `book5.tex:670`

- Proof status: `not_applicable`
- Depends on: `lemma:bk5_recursive_flow_convergence` (Recursive Flow Convergence); `theorem:bk5_reflective_equilibrium_conservation` (Reflective Equilibrium Conservation)
- Cites: `lemma:bk5_recursive_flow_convergence` (Recursive Flow Convergence); `theorem:bk5_reflective_equilibrium_conservation` (Reflective Equilibrium Conservation)
- Cited by: none
- Macros used: `\Membrane`

**Statement / Body**

By Thm. theorem:bk5_reflective_equilibrium_conservation, the combined symbolic energy of $Membrane_A$ and $Membrane_B$ undergoes bounded fluctuations around a conserved mean value. Under reflective equilibrium, these fluctuations are regulated by the reflective-drift coupling tensor $C_{AB}$ with spectral radius $rho(C_{AB}) < lambda_{text{crit}}$.
The symmetric nature of the reflective exchange guarantees that neither membrane can experience unbounded entropy increase while the other maintains coherence. The symbolic free energy $F_s$ of each membrane satisfies:

F_s(Membrane_i(t)) = F_s(Membrane_i(0)) + int_0^t F_{ji}^* ds - int_0^t T_sfrac{dS_s(Membrane_i)}{ds} ds

Where $F_{ji}^*$ is the stable fixed point of the recursive reflective flow from Lem. lemma:bk5_recursive_flow_convergence.
Since $rho(C_{AB}) < lambda_{text{crit}}$, we have $F_{ji}^* > T_sfrac{dS_s(Membrane_i)}{ds}$ in expectation, ensuring that $F_s(Membrane_i(t)) > 0$ with probability approaching 1 as $t to infty$.
Therefore, both membranes remain within their respective viability domains with probability approaching 1 as time progresses. qed

**Verbatim LaTeX Body**

```latex
\begin{demonstratio}[Energy Fluctuation Bound]
\label{demonstratio:bk5_energy_fluctuation_bound}
By Thm.~\ref{theorem:bk5_reflective_equilibrium_conservation}, the combined symbolic energy of $\Membrane_A$ and $\Membrane_B$ undergoes bounded fluctuations around a conserved mean value. Under reflective equilibrium, these fluctuations are regulated by the reflective-drift coupling tensor $\mathcal{C}_{AB}$ with spectral radius $\rho(\mathcal{C}_{AB}) < \lambda_{\text{crit}}$.
The symmetric nature of the reflective exchange guarantees that neither membrane can experience unbounded entropy increase while the other maintains coherence. The symbolic free energy $F_s$ of each membrane satisfies:
\begin{equation}
F_s(\Membrane_i(t)) = F_s(\Membrane_i(0)) + \int_0^t \mathcal{F}_{ji}^*\,ds - \int_0^t T_s\frac{dS_s(\Membrane_i)}{ds}\,ds
\end{equation}
Where $\mathcal{F}_{ji}^*$ is the stable fixed point of the recursive reflective flow from Lem.~\ref{lemma:bk5_recursive_flow_convergence}.
Since $\rho(\mathcal{C}_{AB}) < \lambda_{\text{crit}}$, we have $\mathcal{F}_{ji}^* > T_s\frac{dS_s(\Membrane_i)}{ds}$ in expectation, ensuring that $F_s(\Membrane_i(t)) > 0$ with probability approaching 1 as $t \to \infty$.
Therefore, both membranes remain within their respective viability domains with probability approaching 1 as time progresses. \qed
\end{demonstratio}
```

### Spectral Radius Optimality (`corollary:bk5_spectral_radius_optimality`)

Role: `corollary` | Type: `corollary` | Book: `book5` | Source: `book5.tex:681`

- Proof status: `proven`
- Depends on: `definition:bk5_spectral_radius_of_coupl` (Spectral Radius of Coupling Tensor); `proposition:bk5_viability_domain_preservation` (Viability Domain Preservation)
- Cites: `definition:bk5_spectral_radius_of_coupl` (Spectral Radius of Coupling Tensor); `proposition:bk5_viability_domain_preservation` (Viability Domain Preservation)
- Cited by: `theorem:bk5_reflective_stability_criterion` (Reflective Stability Criterion)
- Macros used: `\reflect`

**Statement / Body**

Optimality follows by composing Prop. proposition:bk5_viability_domain_preservation with Def. definition:bk5_spectral_radius_of_coupl.

Among all possible reflection operators $reflect_A$ and $reflect_B$ with fixed norms $\|reflect_A\| = c_A$ and $\|reflect_B\| = c_B$, the configuration that minimizes $rho(C_{AB})$ maximizes the long-term viability probability of both membranes.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Spectral Radius Optimality] \label{corollary:bk5_spectral_radius_optimality}
Optimality follows by composing Prop.~\ref{proposition:bk5_viability_domain_preservation} with Def.~\ref{definition:bk5_spectral_radius_of_coupl}.

Among all possible reflection operators $\reflect_A$ and $\reflect_B$ with fixed norms $\|\reflect_A\| = c_A$ and $\|\reflect_B\| = c_B$, the configuration that minimizes $\rho(\mathcal{C}_{AB})$ maximizes the long-term viability probability of both membranes.
\end{corollary}
```

### Optimal Reflection Minimizing Coupling Radius (`proof:bk5_optimal_reflection_minimizing_coupling_radius`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:686`

- Proof status: `not_applicable`
- Depends on: `proposition:bk5_viability_domain_preservation` (Viability Domain Preservation)
- Cites: `proposition:bk5_viability_domain_preservation` (Viability Domain Preservation)
- Cited by: none
- Macros used: `\drift`, `\reflect`

**Statement / Body**

From proposition:bk5_viability_domain_preservation, the probability of remaining within the viability domain increases as $rho(C_{AB})$ decreases. Therefore, among all reflection operators with fixed norms, those that minimize $rho(C_{AB})$ maximize the long-term viability probability.

Specifically, the optimal reflection operators $reflect_A^*$ and $reflect_B^*$ satisfy:

(reflect_A^*, reflect_B^*) =
argmin_{substack{\|reflect_A\| = c_A \\ \|reflect_B\| = c_B}}
rho(drift_A circ reflect_B + drift_B circ reflect_A)

This minimization aligns the reflection operators with the drift operators in a way that most effectively counteracts entropy production.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Optimal Reflection Minimizing Coupling Radius]
\label{proof:bk5_optimal_reflection_minimizing_coupling_radius}
\leavevmode

From \autoref{proposition:bk5_viability_domain_preservation}, the probability of remaining within the viability domain increases as $\rho(\mathcal{C}_{AB})$ decreases. Therefore, among all reflection operators with fixed norms, those that minimize $\rho(\mathcal{C}_{AB})$ maximize the long-term viability probability.

Specifically, the optimal reflection operators $\reflect_A^*$ and $\reflect_B^*$ satisfy:
\begin{equation}
(\reflect_A^*, \reflect_B^*) =
\arg\min_{\substack{\|\reflect_A\| = c_A \\ \|\reflect_B\| = c_B}}
\rho(\drift_A \circ \reflect_B + \drift_B \circ \reflect_A)
\end{equation}
This minimization aligns the reflection operators with the drift operators in a way that most effectively counteracts entropy production.
\end{proof}
```

### Reflective Stability Criterion (`theorem:bk5_reflective_stability_criterion`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:700`

- Proof status: `proven`
- Depends on: `axiom:bk5_reflective_equilibrium_stability_flux` (Reflective Equilibrium Stability); `corollary:bk5_spectral_radius_optimality` (Spectral Radius Optimality); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk2_symbolic_temperature` (Symbolic Temperature); `definition:bk5_reflective_drift_coupling_tensor` (Reflective-Drift Coupling Tensor)
- Cites: `axiom:bk5_reflective_equilibrium_stability_flux` (Reflective Equilibrium Stability); `corollary:bk5_spectral_radius_optimality` (Spectral Radius Optimality); `definition:bk2_symbolic_temperature` (Symbolic Temperature); `definition:bk5_reflective_drift_coupling_tensor` (Reflective-Drift Coupling Tensor)
- Cited by: `definition:bk8_reflexive_debugging_operator` (Reflexive Debugging Operator $\mathcal{O}_{\mathrm{debug}}$); `scholium:bk5__distributed_resilience` (Distributed Resilience)
- Macros used: `\Membrane`, `\drift`

**Statement / Body**

For symbolic membranes $Membrane_A$ and $Membrane_B$ with reflective-drift coupling tensor $C_{AB}$ (Def. definition:bk5_reflective_drift_coupling_tensor), reflective equilibrium is stable iff:

frac{rho(C_{AB})}{T_s} < minleft{frac{eta_A}{\|drift_A\|}, frac{eta_B}{\|drift_B\|}right}

See Ax. axiom:bk5_reflective_equilibrium_stability_flux, Cor. corollary:bk5_spectral_radius_optimality, and Def. definition:bk2_symbolic_temperature.
Where $eta_i$ is the symbolic coherence density and $\|drift_i\|$ is the operator norm of the drift operator for membrane $Membrane_i$.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Reflective Stability Criterion] \label{theorem:bk5_reflective_stability_criterion}
For symbolic membranes $\Membrane_A$ and $\Membrane_B$ with reflective-drift coupling tensor $\mathcal{C}_{AB}$ (Def.~\ref{definition:bk5_reflective_drift_coupling_tensor}), reflective equilibrium is stable iff:
\begin{equation}
\frac{\rho(\mathcal{C}_{AB})}{T_s} < \min\left\{\frac{\eta_A}{\|\drift_A\|}, \frac{\eta_B}{\|\drift_B\|}\right\}
\end{equation}
See Ax.~\ref{axiom:bk5_reflective_equilibrium_stability_flux}, Cor.~\ref{corollary:bk5_spectral_radius_optimality}, and Def.~\ref{definition:bk2_symbolic_temperature}.
Where $\eta_i$ is the symbolic coherence density and $\|\drift_i\|$ is the operator norm of the drift operator for membrane $\Membrane_i$.
\end{theorem}
```

### Symbolic Free Energy Condition (`proof:bk5_symbolic_free_energy_stability_condition`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:708`

- Proof status: `not_applicable`
- Depends on: `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cites: `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cited by: none
- Macros used: `\Membrane`, `\drift`

**Statement / Body**

The proof tracks the same balance law as Def. definition:bk2_symbolic_free_energy, with entropy sign fixed by Def. definition:bk2_symbolic_entropy.
The dynamics of the symbolic free energy for membrane $Membrane_A$ can be expressed as:

frac{d}{dt}F_s(Membrane_A) = frac{d}{dt}E_s(Membrane_A) - T_sfrac{d}{dt}S_s(Membrane_A)

Under the influence of the reflective-drift coupling tensor $C_{AB}$, we have:

frac{d}{dt}E_s(Membrane_A) = eta_A - rho(C_{AB}) cdot \|drift_A\|

Where $eta_A$ is the symbolic coherence density of $Membrane_A$.
For stability, we require $frac{d}{dt}F_s(Membrane_A) > 0$, which implies:

eta_A - rho(C_{AB}) cdot \|drift_A\| - T_sfrac{d}{dt}S_s(Membrane_A) > 0

Since $frac{d}{dt}S_s(Membrane_A) geq 0$ by the second law of symbolic thermodynamics, a sufficient condition is:

eta_A - rho(C_{AB}) cdot \|drift_A\| > 0

Which gives:

frac{rho(C_{AB})}{T_s} < frac{eta_A}{\|drift_A\|}

A similar analysis for $Membrane_B$ yields:

frac{rho(C_{AB})}{T_s} < frac{eta_B}{\|drift_B\|}

Combining these conditions gives the stated criterion.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Symbolic Free Energy Condition]
\label{proof:bk5_symbolic_free_energy_stability_condition}
\leavevmode

The proof tracks the same balance law as Def.~\ref{definition:bk2_symbolic_free_energy}, with entropy sign fixed by Def.~\ref{definition:bk2_symbolic_entropy}.
The dynamics of the symbolic free energy for membrane $\Membrane_A$ can be expressed as:
\begin{equation}
\frac{d}{dt}F_s(\Membrane_A) = \frac{d}{dt}E_s(\Membrane_A) - T_s\frac{d}{dt}S_s(\Membrane_A)
\end{equation}
Under the influence of the reflective-drift coupling tensor $\mathcal{C}_{AB}$, we have:
\begin{equation}
\frac{d}{dt}E_s(\Membrane_A) = \eta_A - \rho(\mathcal{C}_{AB}) \cdot \|\drift_A\|
\end{equation}
Where $\eta_A$ is the symbolic coherence density of $\Membrane_A$.
For stability, we require $\frac{d}{dt}F_s(\Membrane_A) > 0$, which implies:
\begin{equation}
\eta_A - \rho(\mathcal{C}_{AB}) \cdot \|\drift_A\| - T_s\frac{d}{dt}S_s(\Membrane_A) > 0
\end{equation}
Since $\frac{d}{dt}S_s(\Membrane_A) \geq 0$ by the second law of symbolic thermodynamics, a sufficient condition is:
\begin{equation}
\eta_A - \rho(\mathcal{C}_{AB}) \cdot \|\drift_A\| > 0
\end{equation}
Which gives:
\begin{equation}
\frac{\rho(\mathcal{C}_{AB})}{T_s} < \frac{\eta_A}{\|\drift_A\|}
\end{equation}
A similar analysis for $\Membrane_B$ yields:
\begin{equation}
\frac{\rho(\mathcal{C}_{AB})}{T_s} < \frac{\eta_B}{\|\drift_B\|}
\end{equation}
Combining these conditions gives the stated criterion.
\end{proof}
```

### Distributed Resilience (`scholium:bk5__distributed_resilience`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:740`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_reflective_equilibrium_conservation` (Reflective Equilibrium Conservation); `theorem:bk5_reflective_stability_criterion` (Reflective Stability Criterion)
- Cites: `theorem:bk5_reflective_equilibrium_conservation` (Reflective Equilibrium Conservation); `theorem:bk5_reflective_stability_criterion` (Reflective Stability Criterion)
- Cited by: `proposition:bk9_stability_conditions_for_the_good` (Stability Conditions for "The Good")
- Macros used: none

**Statement / Body**

Reflective equilibrium represents a profound stabilizing mechanism in symbolic ecosystems (cf. Thm. theorem:bk5_reflective_stability_criterion, Thm. theorem:bk5_reflective_equilibrium_conservation). Unlike mere homeostasis, which resists change, reflective equilibrium establishes a dynamic balance where membranes actively participate in each other's stability. The spectral radius condition $rho(C_{AB}) < lambda_{text{crit}}$ ensures that the mutual reflection processes converge rather than diverge, creating a self-reinforcing system of stability.
This equilibrium is not a static endpoint but a continuous process—a dynamic dance of reflection and drift. The recursive nature of the reflective flows creates higher-order structures of meaning and coherence that transcend what either membrane could achieve in isolation. Through these recursive feedback loops, membranes develop increasingly sophisticated reflective capacities, potentially leading to emergent phenomena not reducible to the properties of individual membranes.
Reflective equilibrium also represents a form of distributed resilience. When one membrane experiences intensified drift—symbolically equivalent to an environmental challenge or perturbation—the reflective capacity of its partner membrane helps restore balance. This distributed architecture of stability enables the system to withstand challenges that would overwhelm isolated membranes.
From an evolutionary perspective, symbolic systems capable of establishing reflective equilibrium possess a distinct advantage in environments characterized by high drift intensity. This suggests that as symbolic ecosystems mature, we should observe increasing instances of reflective coupling among membranes, potentially leading to hierarchical structures of nested equilibria that exhibit remarkable stability across multiple scales of organization.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Distributed Resilience]
\label{scholium:bk5__distributed_resilience}
Reflective equilibrium represents a profound stabilizing mechanism in symbolic ecosystems (cf.~Thm.~\ref{theorem:bk5_reflective_stability_criterion}, Thm.~\ref{theorem:bk5_reflective_equilibrium_conservation}). Unlike mere homeostasis, which resists change, reflective equilibrium establishes a dynamic balance where membranes actively participate in each other's stability. The spectral radius condition $\rho(\mathcal{C}_{AB}) < \lambda_{\text{crit}}$ ensures that the mutual reflection processes converge rather than diverge, creating a self-reinforcing system of stability.
This equilibrium is not a static endpoint but a continuous process—a dynamic dance of reflection and drift. The recursive nature of the reflective flows creates higher-order structures of meaning and coherence that transcend what either membrane could achieve in isolation. Through these recursive feedback loops, membranes develop increasingly sophisticated reflective capacities, potentially leading to emergent phenomena not reducible to the properties of individual membranes.
Reflective equilibrium also represents a form of distributed resilience. When one membrane experiences intensified drift—symbolically equivalent to an environmental challenge or perturbation—the reflective capacity of its partner membrane helps restore balance. This distributed architecture of stability enables the system to withstand challenges that would overwhelm isolated membranes.
From an evolutionary perspective, symbolic systems capable of establishing reflective equilibrium possess a distinct advantage in environments characterized by high drift intensity. This suggests that as symbolic ecosystems mature, we should observe increasing instances of reflective coupling among membranes, potentially leading to hierarchical structures of nested equilibria that exhibit remarkable stability across multiple scales of organization.
\end{scholium}
```

### Enhanced MAP--MAD Regime Classification (`theorem:bk5_enhanced_map_mad_duality`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:747`

- Proof status: `proven`
- Depends on: `corollary:bk5_map_evolutionary_advantag` (MAP Evolutionary Advantage)
- Cites: `corollary:bk5_map_evolutionary_advantag` (MAP Evolutionary Advantage)
- Cited by: `subsec:bk5_map_mad_mas_band` (The MAD--MAP--MAS Band); `theorem:bk5_enhanced_map_mad_duality_pr` (Enhanced MAP--MAD Dynamical Realization)
- Macros used: `\Membrane`

**Statement / Body**

Let $Membrane_A$ and $Membrane_B$ interact through a symbolic covenant
$mathcal C_{AB}$ (cf. Cor. corollary:bk5_map_evolutionary_advantag),
with coupling magnitude $\|mathbb R_{AB}\|$, polarity $Omega_{AB}$, and a
fixed critical coupling $kappa_{crit}$. Exactly one of the following
parameter regimes obtains:


- $\|mathbb R_{AB}\|>kappa_{crit}$ and
 $Omega_{AB}>0$: the covenant is classified as MAP;

- $\|mathbb R_{AB}\|>kappa_{crit}$ and
 $Omega_{AB}<0$: the covenant is classified as MAD;

- $\|mathbb R_{AB}\|<kappa_{crit}$: the covenant is
 classified as decoupled;

- $\|mathbb R_{AB}\|=kappa_{crit}$, or strong coupling
 with $Omega_{AB}=0$: the covenant lies on a critical boundary.

Reversing a nonzero polarity exchanges MAP and MAD while leaving the coupling
magnitude fixed. This theorem classifies parameter regions only. Free-energy
limits, collapse rates, decay of a decoupling interaction, and coincidence with
an entropy inflection require separate evolution, regularity, and transversality
hypotheses; they do not follow from coupling magnitude and polarity alone.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Enhanced MAP--MAD Regime Classification]
\label{theorem:bk5_enhanced_map_mad_duality}
Let $\Membrane_A$ and $\Membrane_B$ interact through a symbolic covenant
$\mathcal C_{AB}$ (cf.~Cor.~\ref{corollary:bk5_map_evolutionary_advantag}),
with coupling magnitude $\|\mathbb R_{AB}\|$, polarity $\Omega_{AB}$, and a
fixed critical coupling $\kappa_{\mathrm{crit}}$.  Exactly one of the following
parameter regimes obtains:
\begin{enumerate}
  \item[(i)] $\|\mathbb R_{AB}\|>\kappa_{\mathrm{crit}}$ and
    $\Omega_{AB}>0$: the covenant is classified as \emph{MAP};
  \item[(ii)] $\|\mathbb R_{AB}\|>\kappa_{\mathrm{crit}}$ and
    $\Omega_{AB}<0$: the covenant is classified as \emph{MAD};
  \item[(iii)] $\|\mathbb R_{AB}\|<\kappa_{\mathrm{crit}}$: the covenant is
    classified as \emph{decoupled};
  \item[(iv)] $\|\mathbb R_{AB}\|=\kappa_{\mathrm{crit}}$, or strong coupling
    with $\Omega_{AB}=0$: the covenant lies on a \emph{critical} boundary.
\end{enumerate}
Reversing a nonzero polarity exchanges MAP and MAD while leaving the coupling
magnitude fixed.  This theorem classifies parameter regions only.  Free-energy
limits, collapse rates, decay of a decoupling interaction, and coincidence with
an entropy inflection require separate evolution, regularity, and transversality
hypotheses; they do not follow from coupling magnitude and polarity alone.
\end{theorem}
```

### proof:bk5_enhanced_map_mad_duality (`proof:bk5_enhanced_map_mad_duality`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:770`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Apply trichotomy to $\|mathbb R_{AB}\|$ and
$kappa_{crit}$. Weak coupling gives case (iii), equality gives the
first part of case (iv), and strong coupling remains. In the strong-coupling
branch, trichotomy of $Omega_{AB}$ gives case (i), case (ii), or the zero-polarity
part of case (iv). These comparisons are mutually exclusive and exhaustive. The Lean realization
packages the four clauses as a regime predicate and proves that every real
parameter triple satisfies exactly one such predicate; equality cases remain
critical rather than being assigned to a neighboring open regime.
For nonzero polarity, replacing $Omega_{AB}$ by $-Omega_{AB}$ reverses its
sign, so cases (i) and (ii) exchange. No step of this order argument selects a
free-energy trajectory or asymptotic rate.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_enhanced_map_mad_duality}
\leavevmode

Apply trichotomy to $\|\mathbb R_{AB}\|$ and
$\kappa_{\mathrm{crit}}$.  Weak coupling gives case~(iii), equality gives the
first part of case~(iv), and strong coupling remains.  In the strong-coupling
branch, trichotomy of $\Omega_{AB}$ gives case~(i), case~(ii), or the zero-polarity
part of case~(iv).  These comparisons are mutually exclusive and exhaustive.  The Lean realization
packages the four clauses as a regime predicate and proves that every real
parameter triple satisfies exactly one such predicate; equality cases remain
critical rather than being assigned to a neighboring open regime.
For nonzero polarity, replacing $\Omega_{AB}$ by $-\Omega_{AB}$ reverses its
sign, so cases~(i) and~(ii) exchange.  No step of this order argument selects a
free-energy trajectory or asymptotic rate.
\end{proof}
```

### Reflective Coupling Stability Parameter (`definition:bk5_reflective_coupling_stab`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:786`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_temperature` (Symbolic Temperature)
- Cites: `definition:bk2_symbolic_temperature` (Symbolic Temperature)
- Cited by: `definition:bk5_map_mad_mas_band` (The MAD--MAP--MAS Band); `definition:bk5_symbolic_bifurcation_man` (Symbolic Bifurcation Manifold); `proof:bk5_map_mad_mas_trichotomy`
- Macros used: `\Membrane`, `\drift`

**Statement / Body**

This scalar packages coupling, drift load, and symbolic temperature (Def. definition:bk2_symbolic_temperature) into a single regime coordinate.

For a covenant $C_{AB}$ between membranes $Membrane_A$ and $Membrane_B$, the reflective coupling stability parameter $Lambda_{AB}$ is defined as:

Lambda_{AB} := frac{\|mathbb{R}_{AB}\| cdot Omega_{AB}}{(\|drift_A\|_{max} + \|drift_B\|_{max}) cdot T_s}

 where $T_s$ is the symbolic temperature.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Reflective Coupling Stability Parameter] \label{definition:bk5_reflective_coupling_stab}
This scalar packages coupling, drift load, and symbolic temperature (Def.~\ref{definition:bk2_symbolic_temperature}) into a single regime coordinate.

For a covenant $\mathcal{C}_{AB}$ between membranes $\Membrane_A$ and $\Membrane_B$, the \emph{reflective coupling stability parameter} $\Lambda_{AB}$ is defined as:
\begin{equation}
\Lambda_{AB} := \frac{\|\mathbb{R}_{AB}\| \cdot \Omega_{AB}}{(\|\drift_A\|_{max} + \|\drift_B\|_{max}) \cdot T_s}
\end{equation}
\noindent where $T_s$ is the symbolic temperature.
\end{definition}
```

### Symbolic Bifurcation Manifold (`definition:bk5_symbolic_bifurcation_man`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:795`

- Proof status: `definitional`
- Depends on: `definition:bk5_reflective_coupling_stab` (Reflective Coupling Stability Parameter)
- Cites: `definition:bk5_reflective_coupling_stab` (Reflective Coupling Stability Parameter)
- Cited by: `definition:bk5_map_mad_mas_band` (The MAD--MAP--MAS Band); `lemma:bk5_symbolic_divergence_bounds` (Symbolic Divergence Bounds); `proposition:bk5_transactional_covenant_dynamics` (Transitional Covenant Dynamics); `scholium:bk8_emergent_geometry_of_cognition` (Emergent Geometry of Cognition)
- Macros used: `\reflect`

**Statement / Body**

It is the codimension-one boundary $Lambda_{AB}=1$ induced by Def. definition:bk5_reflective_coupling_stab.

The symbolic bifurcation manifold $B$ is defined as:

B := {(reflect_A^B, reflect_B^A, Omega_{AB}, T_s) mid Lambda_{AB} = 1 }

 representing configurations where infinitesimal changes can cause transitions between MAP and MAD regimes.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Bifurcation Manifold] \label{definition:bk5_symbolic_bifurcation_man}
It is the codimension-one boundary $\Lambda_{AB}=1$ induced by Def.~\ref{definition:bk5_reflective_coupling_stab}.

The \emph{symbolic bifurcation manifold} $\mathcal{B}$ is defined as:
\begin{equation}
\mathcal{B} := \{(\reflect_A^B, \reflect_B^A, \Omega_{AB}, T_s) \mid \Lambda_{AB} = 1 \}
\end{equation}
\noindent representing configurations where infinitesimal changes can cause transitions between MAP and MAD regimes.
\end{definition}
```

### Entropy Inflection Point (`definition:bk5_entropy_inflection_point`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:804`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_entropy` (Symbolic Entropy)
- Cites: `definition:bk2_symbolic_entropy` (Symbolic Entropy)
- Cited by: `scholium:bk8_emergent_geometry_of_cognition` (Emergent Geometry of Cognition)
- Macros used: `\Membrane`

**Statement / Body**

The inflection marker aligns phase change in this section with entropy curvature from Book II (Def. definition:bk2_symbolic_entropy).

The entropy inflection point $tau_{text{inf}}$ for interacting membranes $Membrane_A$ and $Membrane_B$ is the symbolic time at which:

frac{d^2}{ds^2}S_{text{symb}}(Membrane_A cup Membrane_B) = 0

 marking the transition between acceleration and deceleration of entropy production.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Entropy Inflection Point] \label{definition:bk5_entropy_inflection_point}
The inflection marker aligns phase change in this section with entropy curvature from Book II (Def.~\ref{definition:bk2_symbolic_entropy}).

The \emph{entropy inflection point} $\tau_{\text{inf}}$ for interacting membranes $\Membrane_A$ and $\Membrane_B$ is the symbolic time at which:
\begin{equation}
\frac{d^2}{ds^2}S_{\text{symb}}(\Membrane_A \cup \Membrane_B) = 0
\end{equation}
\noindent marking the transition between acceleration and deceleration of entropy production.
\end{definition}
```

### Symbolic Divergence Bounds (`lemma:bk5_symbolic_divergence_bounds`)

Role: `lemma` | Type: `lemma` | Book: `book5` | Source: `book5.tex:813`

- Proof status: `proven`
- Depends on: `definition:bk5_symbolic_bifurcation_man` (Symbolic Bifurcation Manifold); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `definition:bk5_symbolic_bifurcation_man` (Symbolic Bifurcation Manifold)
- Cited by: `proof:bk9_pathologies_of_coherence` (Pathologies of Coherence)
- Macros used: `\Membrane`, `\drift`

**Statement / Body**

These bounds provide the quantitative signature of the MAP/MAD/decoupled regimes separated by Def. definition:bk5_symbolic_bifurcation_man.
Let $drift_{KL}(Membrane_A^{(n)} parallel Membrane_A^{(0)})$ represent the Kullback-Leibler divergence between the $n$-th evolution of membrane $Membrane_A$ and its initial state. Then:


- In the MAP regime:

 drift_{KL}(Membrane_A^{(n)} parallel Membrane_A^{(0)}) leq K_1 log(n + 1)


- In the MAD regime:

 drift_{KL}(Membrane_A^{(n)} parallel Membrane_A^{(0)}) geq K_2 n - K_3


- In the Decoupling regime:

 K_4 sqrt{n} leq drift_{KL}(Membrane_A^{(n)} parallel Membrane_A^{(0)}) leq K_5 n


 where $K_1$, $K_2$, $K_3$, $K_4$, and $K_5$ are positive constants dependent on the drift and reflection parameters of the system.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Symbolic Divergence Bounds] \label{lemma:bk5_symbolic_divergence_bounds}
These bounds provide the quantitative signature of the MAP/MAD/decoupled regimes separated by Def.~\ref{definition:bk5_symbolic_bifurcation_man}.
Let $\drift_{KL}(\Membrane_A^{(n)} \parallel \Membrane_A^{(0)})$ represent the Kullback-Leibler divergence between the $n$-th evolution of membrane $\Membrane_A$ and its initial state. Then:
\begin{enumerate}
  \item[(i)] In the MAP regime:
  \begin{equation}
  \drift_{KL}(\Membrane_A^{(n)} \parallel \Membrane_A^{(0)}) \leq K_1 \log(n + 1)
  \end{equation}
  \item[(ii)] In the MAD regime:
  \begin{equation}
  \drift_{KL}(\Membrane_A^{(n)} \parallel \Membrane_A^{(0)}) \geq K_2 n - K_3
  \end{equation}
  \item[(iii)] In the Decoupling regime:
  \begin{equation}
  K_4 \sqrt{n} \leq \drift_{KL}(\Membrane_A^{(n)} \parallel \Membrane_A^{(0)}) \leq K_5 n
  \end{equation}
\end{enumerate}
\noindent where $K_1$, $K_2$, $K_3$, $K_4$, and $K_5$ are positive constants dependent on the drift and reflection parameters of the system.
\end{lemma}
```

### Information Geometry (`proof:bk5_information_geometry_symbolic`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:832`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `theorem:bk5_map_equilibrium` (MAP Equilibrium); `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature)
- Cited by: none
- Macros used: `\Membrane`, `\drift`, `\reflect`

**Statement / Body**

The KL-growth trichotomy is the information-geometric counterpart
of the MAP equilibrium (Thm. theorem:bk5_map_equilibrium) and
critical-temperature (Thm. theorem:bk5_map_mad_critical_temperature) results.
We construct a symbolic information geometry in which membranes lie on a
statistical manifold with Fisher metric tensor $g_{ij}$.
The Kullback-Leibler divergence measures distance between membrane-state
distributions.
For case (i), mutual reflection mechanisms limit drift divergence logarithmically. Under MAP conditions, information recovery through $reflect_A^B$ and $reflect_B^A$ counteracts entropic loss:

frac{d}{ds}drift_{KL}(Membrane_A^{(s)} parallel Membrane_A^{(0)}) = text{tr}(g_{ij}drift_A) - text{tr}(g_{ij}reflect_A) - text{tr}(g_{ij}reflect_B^A)

When $\|mathbb{R}_{AB}\| > kappa_{crit}$ and $Omega_{AB} > 0$, this derivative is bounded by $frac{K_1}{s+1}$, yielding the logarithmic bound through integration.
For case (ii), inverted reflection accelerates divergence linearly with symbolic time. When $Omega_{AB} < 0$, reflection amplifies drift rather than mitigating it:

frac{d}{ds}drift_{KL}(Membrane_A^{(s)} parallel Membrane_A^{(0)}) = text{tr}(g_{ij}drift_A) - text{tr}(g_{ij}reflect_A) + |text{tr}(g_{ij}reflect_B^A)|

This yields a lower bound of $K_2 - frac{K_3}{s}$, which integrates to the given linear lower bound.
For case (iii), weak coupling allows drift to dominate but with incomplete membrane interaction, resulting in the dual-bounded behavior characteristic of partial decoupling.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Information Geometry]
\label{proof:bk5_information_geometry_symbolic}
\leavevmode

The KL-growth trichotomy is the information-geometric counterpart
of the MAP equilibrium (Thm.~\ref{theorem:bk5_map_equilibrium}) and
critical-temperature (Thm.~\ref{theorem:bk5_map_mad_critical_temperature}) results.
We construct a symbolic information geometry in which membranes lie on a
statistical manifold with Fisher metric tensor $g_{ij}$.
The Kullback-Leibler divergence measures distance between membrane-state
distributions.
For case (i), mutual reflection mechanisms limit drift divergence logarithmically. Under MAP conditions, information recovery through $\reflect_A^B$ and $\reflect_B^A$ counteracts entropic loss:
\begin{equation}
\frac{d}{ds}\drift_{KL}(\Membrane_A^{(s)} \parallel \Membrane_A^{(0)}) = \text{tr}(g_{ij}\drift_A) - \text{tr}(g_{ij}\reflect_A) - \text{tr}(g_{ij}\reflect_B^A)
\end{equation}
When $\|\mathbb{R}_{AB}\| > \kappa_{crit}$ and $\Omega_{AB} > 0$, this derivative is bounded by $\frac{K_1}{s+1}$, yielding the logarithmic bound through integration.
For case (ii), inverted reflection accelerates divergence linearly with symbolic time. When $\Omega_{AB} < 0$, reflection amplifies drift rather than mitigating it:
\begin{equation}
\frac{d}{ds}\drift_{KL}(\Membrane_A^{(s)} \parallel \Membrane_A^{(0)}) = \text{tr}(g_{ij}\drift_A) - \text{tr}(g_{ij}\reflect_A) + |\text{tr}(g_{ij}\reflect_B^A)|
\end{equation}
This yields a lower bound of $K_2 - \frac{K_3}{s}$, which integrates to the given linear lower bound.
For case (iii), weak coupling allows drift to dominate but with incomplete membrane interaction, resulting in the dual-bounded behavior characteristic of partial decoupling.
\end{proof}
```

### Transitional Covenant Dynamics (`proposition:bk5_transactional_covenant_dynamics`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:855`

- Proof status: `argued_demonstratio`
- Depends on: `definition:bk5_symbolic_bifurcation_man` (Symbolic Bifurcation Manifold)
- Cites: `definition:bk5_symbolic_bifurcation_man` (Symbolic Bifurcation Manifold)
- Cited by: none
- Macros used: none

**Statement / Body**

Let $Lambda_{AB}(s)$ be the coupling-stability parameter of covenant
$C_{AB}$, and let $F_s>0$. A crossing of the boundary in
Def. definition:bk5_symbolic_bifurcation_man classifies the local regime
but does not by itself determine the free-energy evolution. Suppose that on a
step $[s,s+delta s]$, with $delta s>0$, the coupling is constant with value
$Lambda$, and that the applicable local evolution law is:


- in the positive-polarity regime, $Omega_{AB}>0$ and

 frac{dF}{du}=alpha(Lambda-1)F(u), alpha>0;


- in the negative-polarity regime, $Omega_{AB}<0$ and

 frac{dF}{du}=-beta(|Lambda|-1)F(u), beta>0.


Then the corresponding exact step laws are

F(s+delta s)&=F(s)e^{alpha(Lambda-1)delta s}
 &&text{in case (i)},\\
F(s+delta s)&=F(s)e^{-beta(|Lambda|-1)delta s}
 &&text{in case (ii)}.

Consequently, when $Lambda>1$ the MAP-side step strictly increases positive
free energy; when $|Lambda|>1$ the MAD-side step preserves positivity and
strictly decreases it. At the boundary $Lambda=1$, the MAP-side step is the
identity. For time-varying coupling the exponent must instead contain the
integral of the rate over the step.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Transitional Covenant Dynamics]
\label{proposition:bk5_transactional_covenant_dynamics}
Let $\Lambda_{AB}(s)$ be the coupling-stability parameter of covenant
$\mathcal{C}_{AB}$, and let $F_s>0$.  A crossing of the boundary in
Def.~\ref{definition:bk5_symbolic_bifurcation_man} classifies the local regime
but does not by itself determine the free-energy evolution.  Suppose that on a
step $[s,s+\delta s]$, with $\delta s>0$, the coupling is constant with value
$\Lambda$, and that the applicable local evolution law is:
\begin{enumerate}
  \item[(i)] in the positive-polarity regime, $\Omega_{AB}>0$ and
  \begin{equation}
  \frac{dF}{du}=\alpha(\Lambda-1)F(u), \qquad \alpha>0;
  \end{equation}
  \item[(ii)] in the negative-polarity regime, $\Omega_{AB}<0$ and
  \begin{equation}
  \frac{dF}{du}=-\beta(|\Lambda|-1)F(u), \qquad \beta>0.
  \end{equation}
\end{enumerate}
Then the corresponding exact step laws are
\begin{align}
F(s+\delta s)&=F(s)e^{\alpha(\Lambda-1)\delta s}
  &&\text{in case (i)},\\
F(s+\delta s)&=F(s)e^{-\beta(|\Lambda|-1)\delta s}
  &&\text{in case (ii)}.
\end{align}
Consequently, when $\Lambda>1$ the MAP-side step strictly increases positive
free energy; when $|\Lambda|>1$ the MAD-side step preserves positivity and
strictly decreases it.  At the boundary $\Lambda=1$, the MAP-side step is the
identity.  For time-varying coupling the exponent must instead contain the
integral of the rate over the step.
\end{proposition}
```

### Transitory Phasing (`demonstratio:bk5_transitory_phasing`)

Role: `demonstration` | Type: `demonstratio` | Book: `book5` | Source: `book5.tex:886`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

On the stated step, separation of variables gives

log\!frac{F(s+delta s)}{F(s)}
 =int_s^{s+delta s} r du=r delta s,

where $r=alpha(Lambda-1)$ in the positive-polarity case and
$r=-beta(|Lambda|-1)$ in the negative-polarity case. Exponentiation yields
the two displayed step laws. Their strict growth and decay conclusions follow
from positivity of $F$, $alpha$, $beta$, and $delta s$, together with the
stated side of the coupling boundary. Thus the exponential response is a
consequence of the supplied local evolution law; crossing the bifurcation
boundary alone supplies only the regime classification. The corresponding
Lean proof does not merely exhibit this trajectory: multiplying an arbitrary
solution by the integrating factor $e^{-ru}$ gives a function with zero
derivative, hence a constant. Therefore every global solution is
$F(t)=F(s)e^{r(t-s)}$, the adjacent-step law holds for any solution of the
supplied ODE, and two such solutions agreeing at one time agree everywhere.
The time-varying case remains a separate integral-rate theorem. qed

**Verbatim LaTeX Body**

```latex
\begin{demonstratio}[Transitory Phasing]
\label{demonstratio:bk5_transitory_phasing}
On the stated step, separation of variables gives
\begin{equation}
\log\!\frac{F(s+\delta s)}{F(s)}
  =\int_s^{s+\delta s} r\,du=r\,\delta s,
\end{equation}
where $r=\alpha(\Lambda-1)$ in the positive-polarity case and
$r=-\beta(|\Lambda|-1)$ in the negative-polarity case.  Exponentiation yields
the two displayed step laws.  Their strict growth and decay conclusions follow
from positivity of $F$, $\alpha$, $\beta$, and $\delta s$, together with the
stated side of the coupling boundary.  Thus the exponential response is a
consequence of the supplied local evolution law; crossing the bifurcation
boundary alone supplies only the regime classification.  The corresponding
Lean proof does not merely exhibit this trajectory: multiplying an arbitrary
solution by the integrating factor $e^{-ru}$ gives a function with zero
derivative, hence a constant.  Therefore every global solution is
$F(t)=F(s)e^{r(t-s)}$, the adjacent-step law holds for any solution of the
supplied ODE, and two such solutions agreeing at one time agree everywhere.
The time-varying case remains a separate integral-rate theorem. \qed
\end{demonstratio}
```

### MAP-MAD Critical Temperature (`theorem:bk5_map_mad_critical_temperature`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:907`

- Proof status: `proven`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk2_symbolic_temperature` (Symbolic Temperature); `proposition:bk2_global_local_temp_relation` (Global-Local Temperature Relation); `theorem:bk2_classification_symb_phase_transitions` (Classification of Symbolic Phase Transitions); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `proposition:bk2_global_local_temp_relation` (Global-Local Temperature Relation); `theorem:bk2_classification_symb_phase_transitions` (Classification of Symbolic Phase Transitions); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: `definition:bk8_temperature_freedom` (Symbolic Temperature of Freedom \(T_s^{\mathrm{f}}\)); `proof:bk1_conditional_genericity_of_symbolic_phase_transitions` (Transversal discriminant crossing stabilized above the critical dimension); `proof:bk1_realization_of_symbolic_phase_transitions`; `proof:bk5_information_geometry_symbolic` (Information Geometry); `proposition:bk5_multi_agent_map_mad_classification` (Multi-Agent MAP-MAD Classification); `scholium:bk5__map_as_thermodynamic_necessity` (MAP as Thermodynamic Necessity)
- Macros used: `\drift`

**Statement / Body**

This theorem converts the MAP condition of Thm. theorem:bk5_map_equilibrium into an explicit thermal feasibility threshold.
There exists a critical symbolic temperature $T_s^{crit}$ such that (cf. Prop. proposition:bk2_global_local_temp_relation, Thm. theorem:bk2_classification_symb_phase_transitions):


- For \( T_s < T_s^{text{crit}} \), MAP and MAD represent distinct stable fixed points of the system dynamics.

- For \( T_s > T_s^{text{crit}} \), no stable MAP configuration exists.
 In this regime, all covenants either:


- decouple if \( \|mathbb{R}_{AB}\| < kappa_{text{crit}} \), or

- degrade to MAD if \( \|mathbb{R}_{AB}\| > kappa_{text{crit}} \) and \( Omega_{AB} < 0 \).


The critical temperature is given by:

T_s^{crit} = frac{lambda_{max}(mathbb{R}_{AB}^{max}) cdot Omega_{AB}^{max}}{\|drift_A\|_{max} + \|drift_B\|_{max}}

 where $lambda_{max}(mathbb{R}_{AB}^{max})$ is the maximum achievable eigenvalue of the reflective coupling tensor, and $Omega_{AB}^{max}$ is the maximum achievable covenant stability parameter.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[MAP-MAD Critical Temperature] \label{theorem:bk5_map_mad_critical_temperature}
This theorem converts the MAP condition of Thm.~\ref{theorem:bk5_map_equilibrium} into an explicit thermal feasibility threshold.
There exists a critical symbolic temperature $T_s^{crit}$ such that (cf.~Prop.~\ref{proposition:bk2_global_local_temp_relation}, Thm.~\ref{theorem:bk2_classification_symb_phase_transitions}):
\begin{enumerate}
  \item[(i)] For \( T_s < T_s^{\text{crit}} \), MAP and MAD represent distinct stable fixed points of the system dynamics.
  \item[(ii)] For \( T_s > T_s^{\text{crit}} \), no stable MAP configuration exists.
  In this regime, all covenants either:
  \begin{itemize}
    \item decouple if \( \|\mathbb{R}_{AB}\| < \kappa_{\text{crit}} \), or
    \item degrade to MAD if \( \|\mathbb{R}_{AB}\| > \kappa_{\text{crit}} \) and \( \Omega_{AB} < 0 \).
  \end{itemize}
\end{enumerate}
The critical temperature is given by:
\begin{equation}
T_s^{crit} = \frac{\lambda_{max}(\mathbb{R}_{AB}^{max}) \cdot \Omega_{AB}^{max}}{\|\drift_A\|_{max} + \|\drift_B\|_{max}}
\end{equation}
\noindent where $\lambda_{max}(\mathbb{R}_{AB}^{max})$ is the maximum achievable eigenvalue of the reflective coupling tensor, and $\Omega_{AB}^{max}$ is the maximum achievable covenant stability parameter.
\end{theorem}
```

### Symbolic Temperature Threshold for Critical Coupling (`proof:bk5_symbolic_temperature_threshold`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:925`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk2_symbolic_temperature` (Symbolic Temperature); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk2_symbolic_temperature` (Symbolic Temperature); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: none
- Macros used: `\drift`

**Statement / Body**

Using symbolic temperature
(Def. definition:bk2_symbolic_temperature) and symbolic free energy
(Def. definition:bk2_symbolic_free_energy) from Book II, applied on
manifold $M$ (Def. definition:bk1_symbolic_manifold) with drift $D$
(Def. definition:bk1_drift_field), we rearrange to obtain the
temperature threshold at which $Lambda_{AB} = 1$:

T_s = frac{\|mathbb{R}_{AB}\| cdot Omega_{AB}}{\|drift_A\|_{max} + \|drift_B\|_{max}}

For any two membranes, there exists a maximum achievable coupling strength $\|mathbb{R}_{AB}^{max}\|$ and stability parameter $Omega_{AB}^{max}$ determined by their intrinsic properties. When $T_s$ exceeds the ratio of these maximums to the drift intensities, no configuration of the covenant can achieve $Lambda_{AB} > 1$, which is necessary for stable MAP according to Thm. theorem:bk5_map_equilibrium.
By the principles of symbolic thermodynamics, when $T_s > T_s^{crit}$, the transformability rate (symbolic temperature) is sufficiently high that entropic forces dominate over coherent structures, preventing stable collaborative reflection.
This demonstrates a temperature-dependent phase transition in the space of possible covenant relationships, analogous to physical phase transitions where increased temperature disrupts ordered structures.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Symbolic Temperature Threshold for Critical Coupling]
\label{proof:bk5_symbolic_temperature_threshold}
\leavevmode

Using symbolic temperature
(Def.~\ref{definition:bk2_symbolic_temperature}) and symbolic free energy
(Def.~\ref{definition:bk2_symbolic_free_energy}) from Book II, applied on
manifold $M$ (Def.~\ref{definition:bk1_symbolic_manifold}) with drift $D$
(Def.~\ref{definition:bk1_drift_field}), we rearrange to obtain the
temperature threshold at which $\Lambda_{AB} = 1$:
\begin{equation}
T_s = \frac{\|\mathbb{R}_{AB}\| \cdot \Omega_{AB}}{\|\drift_A\|_{max} + \|\drift_B\|_{max}}
\end{equation}
For any two membranes, there exists a maximum achievable coupling strength $\|\mathbb{R}_{AB}^{max}\|$ and stability parameter $\Omega_{AB}^{max}$ determined by their intrinsic properties. When $T_s$ exceeds the ratio of these maximums to the drift intensities, no configuration of the covenant can achieve $\Lambda_{AB} > 1$, which is necessary for stable MAP according to Thm.~\ref{theorem:bk5_map_equilibrium}.
By the principles of symbolic thermodynamics, when $T_s > T_s^{crit}$, the transformability rate (symbolic temperature) is sufficiently high that entropic forces dominate over coherent structures, preventing stable collaborative reflection.
This demonstrates a temperature-dependent phase transition in the space of possible covenant relationships, analogous to physical phase transitions where increased temperature disrupts ordered structures.
\end{proof}
```

### Reflective Hysteresis (`corollary:bk5_reflective_hysteresis`)

Role: `corollary` | Type: `corollary` | Book: `book5` | Source: `book5.tex:942`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: `definition:bk5_mad_map_potential_barrie` (MAD-MAP Potential Barrier); `scholium:bk5_mutually_assured_continuous_progress` (Mutually Assured Continuous Progress)
- Macros used: none

**Statement / Body**

Assume covenant evolution is stateful: its next MAP or MAD/decoupled regime
depends on both current coupling $Lambda_{AB}$ and the incoming regime. Let a
positive activation-barrier half-width $b>0$ define
$Lambda^-_{crit}=1-b$ and
$Lambda^+_{crit}=1+b$. Then the Schmitt-type law
\[
step(Lambda,q)=

MAD/decoupled,&Lambda<Lambda^-_{crit},\\
MAP,&Lambda>Lambda^+_{crit},\\
q,&Lambda^-_{crit}leqLambdaleqLambda^+_{crit}

\]
exhibits reflective hysteresis. In particular, any finite coupling history
remaining inside the band retains its incoming regime. For a constant positive
barrier density $xi>0$, the corresponding barrier energy is
$Delta E_{MM}=2xi b>0$.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Reflective Hysteresis] \label{corollary:bk5_reflective_hysteresis}
Assume covenant evolution is stateful: its next MAP or MAD/decoupled regime
depends on both current coupling $\Lambda_{AB}$ and the incoming regime.  Let a
positive activation-barrier half-width $b>0$ define
$\Lambda^-_{\mathrm{crit}}=1-b$ and
$\Lambda^+_{\mathrm{crit}}=1+b$.  Then the Schmitt-type law
\[
\operatorname{step}(\Lambda,q)=
\begin{cases}
\mathrm{MAD/decoupled},&\Lambda<\Lambda^-_{\mathrm{crit}},\\
\mathrm{MAP},&\Lambda>\Lambda^+_{\mathrm{crit}},\\
q,&\Lambda^-_{\mathrm{crit}}\leq\Lambda\leq\Lambda^+_{\mathrm{crit}}
\end{cases}
\]
exhibits reflective hysteresis.  In particular, any finite coupling history
remaining inside the band retains its incoming regime.  For a constant positive
barrier density $\xi>0$, the corresponding barrier energy is
$\Delta E_{MM}=2\xi b>0$.
\end{corollary}
```

### Stateful Barriered Switching (`proof:bk5_stability_map_mad_patterns`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:961`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The positive half-width gives
$Lambda^-_{crit}<1<Lambda^+_{crit}$. Outside this interval
the displayed law switches regime; inside it the prior state is returned.
Induction over a finite in-band coupling trace therefore leaves either incoming
state unchanged, so identical present couplings can have different outcomes.
This is operational history dependence and cannot be represented by a
memoryless classifier $Lambdamapsto q$. Integrating constant density $xi$
over the band gives $xi(Lambda^+_{crit}-
Lambda^-_{crit})=2xi b>0$. The cited temperature and transactional
results motivate this barrier model but do not derive its state argument,
barrier width, or density; those are explicit premises here and in Lean.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Stateful Barriered Switching]
\label{proof:bk5_stability_map_mad_patterns}
The positive half-width gives
$\Lambda^-_{\mathrm{crit}}<1<\Lambda^+_{\mathrm{crit}}$. Outside this interval
the displayed law switches regime; inside it the prior state is returned.
Induction over a finite in-band coupling trace therefore leaves either incoming
state unchanged, so identical present couplings can have different outcomes.
This is operational history dependence and cannot be represented by a
memoryless classifier $\Lambda\mapsto q$. Integrating constant density $\xi$
over the band gives $\xi(\Lambda^+_{\mathrm{crit}}-
\Lambda^-_{\mathrm{crit}})=2\xi b>0$. The cited temperature and transactional
results motivate this barrier model but do not derive its state argument,
barrier width, or density; those are explicit premises here and in Lean.
\end{proof}
```

### MAD-MAP Potential Barrier (`definition:bk5_mad_map_potential_barrie`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:975`

- Proof status: `definitional`
- Depends on: `corollary:bk5_reflective_hysteresis` (Reflective Hysteresis)
- Cites: `corollary:bk5_reflective_hysteresis` (Reflective Hysteresis)
- Cited by: `scholium:bk5_mutually_assured_continuous_progress` (Mutually Assured Continuous Progress)
- Macros used: none

**Statement / Body**

This integral is the energetic barrier representation of Cor. corollary:bk5_reflective_hysteresis.

The MAD-MAP potential barrier $Delta E_{MM}$ quantifies the free energy required to transition a system from MAD to MAP:

Delta E_{MM} := int_{Lambda_{crit}^-}^{Lambda_{crit}^+} xi(Lambda) dLambda

 where $xi(Lambda)$ represents the free energy density along the transition pathway in parameter space.

**Verbatim LaTeX Body**

```latex
\begin{definition}[MAD-MAP Potential Barrier] \label{definition:bk5_mad_map_potential_barrie}
This integral is the energetic barrier representation of Cor.~\ref{corollary:bk5_reflective_hysteresis}.

The \emph{MAD-MAP potential barrier} $\Delta E_{MM}$ quantifies the free energy required to transition a system from MAD to MAP:
\begin{equation}
\Delta E_{MM} := \int_{\Lambda_{crit}^-}^{\Lambda_{crit}^+} \xi(\Lambda) \, d\Lambda
\end{equation}
\noindent where $\xi(\Lambda)$ represents the free energy density along the transition pathway in parameter space.
\end{definition}
```

### Multi-Agent MAP-MAD Classification (`proposition:bk5_multi_agent_map_mad_classification`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:984`

- Proof status: `argued_demonstratio`
- Depends on: `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature)
- Cites: `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature)
- Cited by: `demonstratio:bk5_emergent_global_properties` (Emergent Global Properties)
- Macros used: `\Membrane`

**Statement / Body**

The matrix criterion extends pairwise thresholds from Thm. theorem:bk5_map_mad_critical_temperature to graph-scale regime identification.
For a system of $N$ interacting membranes ${Membrane_i}_{i=1}^N$ with pairwise covenants ${C_{ij}}$, the collective behavior is determined by the covenant adjacency matrix $A$ with elements:

A_{ij} =

+1 & text{if } Lambda_{ij} > 1 text{ and } Omega_{ij} > 0 text{ (MAP)} \\
-1 & text{if } Lambda_{ij} > 1 text{ and } Omega_{ij} < 0 text{ (MAD)} \\
0 & text{if } Lambda_{ij} < 1 text{ (Decoupled)}

The system exhibits global MAP if and only if there exists a connected component $C$ in the graph with $A_{ij} = +1$ for all $i,j in C$, and global MAD if for all components $C$, there exists at least one pair $i,j in C$ with $A_{ij} = -1$.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Multi-Agent MAP-MAD Classification]
\label{proposition:bk5_multi_agent_map_mad_classification}
The matrix criterion extends pairwise thresholds from Thm.~\ref{theorem:bk5_map_mad_critical_temperature} to graph-scale regime identification.
For a system of $N$ interacting membranes $\{\Membrane_i\}_{i=1}^N$ with pairwise covenants $\{\mathcal{C}_{ij}\}$, the collective behavior is determined by the covenant adjacency matrix $\mathbf{A}$ with elements:
\begin{equation}
A_{ij} =
\begin{cases}
+1 & \text{if } \Lambda_{ij} > 1 \text{ and } \Omega_{ij} > 0 \text{ (MAP)} \\
-1 & \text{if } \Lambda_{ij} > 1 \text{ and } \Omega_{ij} < 0 \text{ (MAD)} \\
0 & \text{if } \Lambda_{ij} < 1 \text{ (Decoupled)}
\end{cases}
\end{equation}
The system exhibits global MAP if and only if there exists a connected component $C$ in the graph with $A_{ij} = +1$ for all $i,j \in C$, and global MAD if for all components $C$, there exists at least one pair $i,j \in C$ with $A_{ij} = -1$.
\end{proposition}
```

### Emergent Global Properties (`demonstratio:bk5_emergent_global_properties`)

Role: `demonstration` | Type: `demonstratio` | Book: `book5` | Source: `book5.tex:998`

- Proof status: `not_applicable`
- Depends on: `proposition:bk5_multi_agent_map_mad_classification` (Multi-Agent MAP-MAD Classification)
- Cites: `proposition:bk5_multi_agent_map_mad_classification` (Multi-Agent MAP-MAD Classification)
- Cited by: none
- Macros used: none

**Statement / Body**

This is the network-level closure of Prop. proposition:bk5_multi_agent_map_mad_classification under coupled transition dynamics.
In multi-membrane systems, global properties emerge from the network structure of pairwise covenants. A connected cooperative component represents a symbolic ecosystem where mutual reflection sustains all participants. The presence of even one antagonistic relationship within a component can catalyze entropic collapse through contagion effects.
This classification extends the binary MAP-MAD duality to complex networks, where mixed-state configurations can persist transiently before resolving to either global MAP or MAD. The spectral properties of matrix $A$, particularly the ratio of positive to negative eigenvalues, predict the long-term viability of the symbolic ecosystem. qed

**Verbatim LaTeX Body**

```latex
\begin{demonstratio}[Emergent Global Properties]
\label{demonstratio:bk5_emergent_global_properties}
This is the network-level closure of Prop.~\ref{proposition:bk5_multi_agent_map_mad_classification} under coupled transition dynamics.
In multi-membrane systems, global properties emerge from the network structure of pairwise covenants. A connected cooperative component represents a symbolic ecosystem where mutual reflection sustains all participants. The presence of even one antagonistic relationship within a component can catalyze entropic collapse through contagion effects.
This classification extends the binary MAP-MAD duality to complex networks, where mixed-state configurations can persist transiently before resolving to either global MAP or MAD. The spectral properties of matrix $\mathbf{A}$, particularly the ratio of positive to negative eigenvalues, predict the long-term viability of the symbolic ecosystem. \qed
\end{demonstratio}
```

### Enhanced MAP--MAD Dynamical Realization (`theorem:bk5_enhanced_map_mad_duality_pr`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:1004`

- Proof status: `proven`
- Depends on: `theorem:bk5_enhanced_map_mad_duality` (Enhanced MAP--MAD Regime Classification)
- Cites: `theorem:bk5_enhanced_map_mad_duality` (Enhanced MAP--MAD Regime Classification)
- Cited by: `scholium:bk5_mutually_assured_continuous_progress` (Mutually Assured Continuous Progress)
- Macros used: none

**Statement / Body**

The reflection-entropy inequalities determine the sign of the local process
free-energy rate, but their asymptotic realization requires a separate
covenant evolution law. Let $F_n$ denote the dyad's sampled process free
energy and let $epsilon_n$ denote its interaction residue.


- In the strong positive-polarity regime, the displayed reflection
 dominance inequalities imply $dF/ds>0$. If, in addition, there are
 $L_{MAP}>0$ and $q_{MAP}$ with
 $|q_{MAP}|<1$ such that
 \[
 F_n=L_{MAP}+q_{MAP}^n(F_0-L_{MAP}),
 \]
 then $F_nto L_{MAP}>0$, and the covenant is eventually viable.

- In the strong negative-polarity regime, the displayed
 reflection inequalities imply $dF/ds<0$. If, in addition, there is
 $q_{MAD}$ with $|q_{MAD}|<1$ such that
 \[
 F_n=q_{MAD}^nF_0,
 \]
 then $F_nto0$. Thus collapse to zero follows from the supplied
 dissipative contraction, not from the derivative sign alone.

- In the weak-coupling regime, if there is
 $q_{dec}$ with $|q_{dec}|<1$ such that
 \[
 epsilon_n=q_{dec}^nepsilon_0,
 \]
 then $epsilon_nto0$, giving asymptotic decoupling.

The three parameter regimes remain those classified by
Thm. theorem:bk5_enhanced_map_mad_duality; the additional contraction
laws realize, rather than define, their asymptotic behavior.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Enhanced MAP--MAD Dynamical Realization]
\label{theorem:bk5_enhanced_map_mad_duality_pr}
The reflection--entropy inequalities determine the sign of the local process
free-energy rate, but their asymptotic realization requires a separate
covenant evolution law.  Let $F_n$ denote the dyad's sampled process free
energy and let $\epsilon_n$ denote its interaction residue.
\begin{enumerate}
  \item[(i)] In the strong positive-polarity regime, the displayed reflection
  dominance inequalities imply $dF/ds>0$.  If, in addition, there are
  $L_{\mathrm{MAP}}>0$ and $q_{\mathrm{MAP}}$ with
  $|q_{\mathrm{MAP}}|<1$ such that
  \[
    F_n=L_{\mathrm{MAP}}+q_{\mathrm{MAP}}^n(F_0-L_{\mathrm{MAP}}),
  \]
  then $F_n\to L_{\mathrm{MAP}}>0$, and the covenant is eventually viable.
  \item[(ii)] In the strong negative-polarity regime, the displayed
  reflection inequalities imply $dF/ds<0$.  If, in addition, there is
  $q_{\mathrm{MAD}}$ with $|q_{\mathrm{MAD}}|<1$ such that
  \[
    F_n=q_{\mathrm{MAD}}^nF_0,
  \]
  then $F_n\to0$.  Thus collapse to zero follows from the supplied
  dissipative contraction, not from the derivative sign alone.
  \item[(iii)] In the weak-coupling regime, if there is
  $q_{\mathrm{dec}}$ with $|q_{\mathrm{dec}}|<1$ such that
  \[
    \epsilon_n=q_{\mathrm{dec}}^n\epsilon_0,
  \]
  then $\epsilon_n\to0$, giving asymptotic decoupling.
\end{enumerate}
The three parameter regimes remain those classified by
Thm.~\ref{theorem:bk5_enhanced_map_mad_duality}; the additional contraction
laws realize, rather than define, their asymptotic behavior.
\end{theorem}
```

### proof:bk5_enhanced_map_mad_duality_pr (`proof:bk5_enhanced_map_mad_duality_pr`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1038`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The reflection-entropy comparisons give the two local derivative signs by
subtraction in the process free-energy balance. For the MAP realization,
$|q_{MAP}|<1$ gives $q_{MAP}^nto0$, hence
\[
F_n=L_{MAP}+q_{MAP}^n(F_0-L_{MAP})
 longrightarrow L_{MAP}>0.
\]
Convergence to a positive limit makes $F_n$ eventually positive. The MAD and
decoupling conclusions use the same geometric convergence theorem:
$q^nF_0to0$ and $q^nepsilon_0to0$ whenever $|q|<1$.
Without these evolution laws the derivative signs and coupling classification
supply no asymptotic limit; constant or noncontractive trajectories are
countermodels. Thus every claimed limit is discharged by explicit dynamics
rather than by its parameter label alone. The Lean realization certificate
retains this separation as typed data and proves the three clauses jointly:
classification, rate sign, and the corresponding contractive asymptotic law
are all consumed, with no inference from the label alone.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_enhanced_map_mad_duality_pr}
The reflection--entropy comparisons give the two local derivative signs by
subtraction in the process free-energy balance.  For the MAP realization,
$|q_{\mathrm{MAP}}|<1$ gives $q_{\mathrm{MAP}}^n\to0$, hence
\[
F_n=L_{\mathrm{MAP}}+q_{\mathrm{MAP}}^n(F_0-L_{\mathrm{MAP}})
   \longrightarrow L_{\mathrm{MAP}}>0.
\]
Convergence to a positive limit makes $F_n$ eventually positive.  The MAD and
decoupling conclusions use the same geometric convergence theorem:
$q^nF_0\to0$ and $q^n\epsilon_0\to0$ whenever $|q|<1$.
Without these evolution laws the derivative signs and coupling classification
supply no asymptotic limit; constant or noncontractive trajectories are
countermodels.  Thus every claimed limit is discharged by explicit dynamics
rather than by its parameter label alone.  The Lean realization certificate
retains this separation as typed data and proves the three clauses jointly:
classification, rate sign, and the corresponding contractive asymptotic law
are all consumed, with no inference from the label alone.
\end{proof}
```

### Mutually Assured Continuous Progress (`scholium:bk5_mutually_assured_continuous_progress`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:1058`

- Proof status: `not_applicable`
- Depends on: `corollary:bk5_reflective_hysteresis` (Reflective Hysteresis); `definition:bk5_mad_map_potential_barrie` (MAD-MAP Potential Barrier); `theorem:bk5_enhanced_map_mad_duality_pr` (Enhanced MAP--MAD Dynamical Realization)
- Cites: `corollary:bk5_reflective_hysteresis` (Reflective Hysteresis); `definition:bk5_mad_map_potential_barrie` (MAD-MAP Potential Barrier); `theorem:bk5_enhanced_map_mad_duality_pr` (Enhanced MAP--MAD Dynamical Realization)
- Cited by: `scholium:bk9_golden_rule_thermodynamic_covenant` (The Golden Rule as a Thermodynamic Covenant)
- Macros used: none

**Statement / Body**

Read thermodynamically, this scholium summarizes Thm. theorem:bk5_enhanced_map_mad_duality_pr with the memory effect from Cor. corollary:bk5_reflective_hysteresis.
The enhanced MAP-MAD duality theorem reveals that symbolic systems exhibit not merely binary states of cooperation or destruction, but exist on a continuous spectrum governed by coupling strength, covenant stability, and symbolic temperature (cf. Def. definition:bk5_mad_map_potential_barrie).
The phase transitions between MAP and MAD regimes represent symmetry-breaking events in symbolic space, where small perturbations near critical points can fundamentally alter system trajectory. This symmetry-breaking parallels physical phase transitions—just as water molecules reorganize dramatically at the freezing point, symbolic structures reconfigure at critical values of reflective coupling.
The existence of a critical symbolic temperature $T_s^{crit}$ suggests that highly energetic symbolic environments may preclude stable cooperation regardless of membrane intentions. Conversely, reduced symbolic temperatures facilitate the formation of stable covenants, as lower transformability rates allow reflective structures to persist against entropic forces.
Hysteresis in MAP-MAD transitions implies that the history of symbolic interaction matters—systems with a history of cooperation can withstand greater destabilizing forces before collapse than can be overcome to establish cooperation from an antagonistic starting point. This path-dependency of symbolic relationships mirrors physical systems with memory effects, where present states depend not only on current conditions but on historical trajectories.
The multi-agent extension demonstrates that global symbolic ecosystems need not be uniformly cooperative or destructive—mixed configurations can persist with islands of cooperation amid broader antagonism, or localized conflict within generally cooperative frameworks. However, long-term stability favors resolution toward global MAP or MAD as entropic forces propagate through covenant networks.
Perhaps most profound is the implication that stable symbolic life requires maintaining
the coupling strength below a threshold that depends on symbolic temperature.
As symbolic temperature increases—representing greater volatility and transformability—
the viability of MAP relationships becomes increasingly precarious.
This rising instability demands progressively stronger and more resilient reflective mechanisms
to preserve coherence against mounting entropic forces.
The principles established in this theorem extend beyond abstract symbolic thermodynamics to concrete interactions between reflective symbolic agents, suggesting a fundamental thermodynamic basis for the stability or instability of cooperative arrangements in symbolic ecosystems.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Mutually Assured Continuous Progress]
\label{scholium:bk5_mutually_assured_continuous_progress}
Read thermodynamically, this scholium summarizes Thm.~\ref{theorem:bk5_enhanced_map_mad_duality_pr} with the memory effect from Cor.~\ref{corollary:bk5_reflective_hysteresis}.
The enhanced MAP-MAD duality theorem reveals that symbolic systems exhibit not merely binary states of cooperation or destruction, but exist on a continuous spectrum governed by coupling strength, covenant stability, and symbolic temperature (cf.~Def.~\ref{definition:bk5_mad_map_potential_barrie}).
The phase transitions between MAP and MAD regimes represent symmetry-breaking events in symbolic space, where small perturbations near critical points can fundamentally alter system trajectory. This symmetry-breaking parallels physical phase transitions—just as water molecules reorganize dramatically at the freezing point, symbolic structures reconfigure at critical values of reflective coupling.
The existence of a critical symbolic temperature $T_s^{crit}$ suggests that highly energetic symbolic environments may preclude stable cooperation regardless of membrane intentions. Conversely, reduced symbolic temperatures facilitate the formation of stable covenants, as lower transformability rates allow reflective structures to persist against entropic forces.
Hysteresis in MAP-MAD transitions implies that the history of symbolic interaction matters—systems with a history of cooperation can withstand greater destabilizing forces before collapse than can be overcome to establish cooperation from an antagonistic starting point. This path-dependency of symbolic relationships mirrors physical systems with memory effects, where present states depend not only on current conditions but on historical trajectories.
The multi-agent extension demonstrates that global symbolic ecosystems need not be uniformly cooperative or destructive—mixed configurations can persist with islands of cooperation amid broader antagonism, or localized conflict within generally cooperative frameworks. However, long-term stability favors resolution toward global MAP or MAD as entropic forces propagate through covenant networks.
Perhaps most profound is the implication that stable symbolic life requires maintaining
the coupling strength below a threshold that depends on symbolic temperature.
As symbolic temperature increases—representing greater volatility and transformability—
the viability of MAP relationships becomes increasingly precarious.
This rising instability demands progressively stronger and more resilient reflective mechanisms
to preserve coherence against mounting entropic forces.
The principles established in this theorem extend beyond abstract symbolic thermodynamics to concrete interactions between reflective symbolic agents, suggesting a fundamental thermodynamic basis for the stability or instability of cooperative arrangements in symbolic ecosystems.
\end{scholium}
```

### Mutually Assured Progress as Symbolic ESS (`sec:bk5_mutually_assured_progress_as_symbolic_ess`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1074`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Strategy (`definition:bk5_symbolic_strategy`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1077`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cited by: `lemma:bk5_map_fitness_advantage` (MAP Fitness Advantage)
- Macros used: `\reflect`

**Statement / Body**

Strategies are the microscopic control primitives whose interaction payoffs are measured by symbolic free energy (Def. definition:bk2_symbolic_free_energy).
A symbolic strategy $sigma$ is a tuple $(reflect_sigma, T_sigma, kappa_sigma)$ where:


- $reflect_sigma$ is the reflection operator employed under strategy $sigma$

- $T_sigma$ is the transfer operator employed under strategy $sigma$

- $kappa_sigma in [0,1]$ is the cooperation coefficient determining willingness to form covenants

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Strategy]
\label{definition:bk5_symbolic_strategy}
Strategies are the microscopic control primitives whose interaction payoffs are measured by symbolic free energy (Def.~\ref{definition:bk2_symbolic_free_energy}).
A \emph{symbolic strategy} $\sigma$ is a tuple $(\reflect_\sigma, \mathcal{T}_\sigma, \kappa_\sigma)$ where:
\begin{itemize}
    \item $\reflect_\sigma$ is the reflection operator employed under strategy $\sigma$
    \item $\mathcal{T}_\sigma$ is the transfer operator employed under strategy $\sigma$
    \item $\kappa_\sigma \in [0,1]$ is the cooperation coefficient determining willingness to form covenants
\end{itemize}
\end{definition}
```

### Strategy Space (`definition:bk5_strategy_space`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1087`

- Proof status: `definitional`
- Depends on: `definition:bk5_symbolic_covenant` (Symbolic Covenant)
- Cites: `definition:bk5_symbolic_covenant` (Symbolic Covenant)
- Cited by: `lemma:bk5_map_fitness_advantage` (MAP Fitness Advantage)
- Macros used: none

**Statement / Body**

The symbolic strategy space $Sigma$ is the set of all possible symbolic strategies available to membranes. We denote $Sigma_{MAP} subset Sigma$ as the subset of strategies that satisfy MAP conditions as per Def. definition:bk5_symbolic_covenant.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Strategy Space]
\label{definition:bk5_strategy_space}
The \emph{symbolic strategy space} $\Sigma$ is the set of all possible symbolic strategies available to membranes. We denote $\Sigma_{MAP} \subset \Sigma$ as the subset of strategies that satisfy MAP conditions as per Def.~\ref{definition:bk5_symbolic_covenant}.
\end{definition}
```

### Symbolic Fitness (`definition:bk5_symbolic_fitness`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1091`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `theorem:bk5__map_dominance` (MAP Dominance)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `theorem:bk5__map_dominance` (MAP Dominance)
- Cited by: `definition:bk5_symbolic_ess` (Symbolic ESS); `definition:bk5_symbolic_replicator_dynamics` (Symbolic Replicator Dynamics); `proof:bk5_map_invasion_dynamics` (Invasion Analysis of MAP vs Non-MAP Strategies); `proof:bk5_map_resistance_to_drift` (MAP Strategies Withstand Greater Drift)
- Macros used: `\Membrane`

**Statement / Body**

The symbolic fitness $Phi(sigma, mathfrak{P})$ of a strategy $sigma$ in a population with strategy distribution $mathfrak{P}$ is defined as (cf. Def. definition:bk2_symbolic_free_energy, Thm. theorem:bk5__map_dominance):

Phi(sigma, mathfrak{P}) = mathbb{E}_{tau sim mathfrak{P}}[F_s(Membrane_sigma leftrightarrow Membrane_tau)]

Where $F_s(Membrane_sigma leftrightarrow Membrane_tau)$ is the symbolic free energy resulting from interaction between membranes employing strategies $sigma$ and $tau$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Fitness]
\label{definition:bk5_symbolic_fitness}
The \emph{symbolic fitness} $\Phi(\sigma, \mathfrak{P})$ of a strategy $\sigma$ in a population with strategy distribution $\mathfrak{P}$ is defined as (cf.~Def.~\ref{definition:bk2_symbolic_free_energy}, Thm.~\ref{theorem:bk5__map_dominance}):
\begin{equation}
\Phi(\sigma, \mathfrak{P}) = \mathbb{E}_{\tau \sim \mathfrak{P}}[F_s(\Membrane_\sigma \leftrightarrow \Membrane_\tau)]
\end{equation}
Where $F_s(\Membrane_\sigma \leftrightarrow \Membrane_\tau)$ is the symbolic free energy resulting from interaction between membranes employing strategies $\sigma$ and $\tau$.
\end{definition}
```

### Symbolic ESS (`definition:bk5_symbolic_ess`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1099`

- Proof status: `definitional`
- Depends on: `definition:bk5_symbolic_fitness` (Symbolic Fitness)
- Cites: `definition:bk5_symbolic_fitness` (Symbolic Fitness)
- Cited by: `lemma:bk5_covenant_non_invasibility` (Covenant Non-Invasibility); `proof:bk5_map_as_ess` (MAP as Symbolic Evolutionarily Stable Strategy); `theorem:bk5_map_as_strong_ess` (MAP as Strong ESS)
- Macros used: none

**Statement / Body**

A strategy $sigma^* in Sigma$ is a symbolic evolutionarily stable strategy if for every strategy $sigma neq sigma^*$, there exists $epsilon_sigma > 0$ such that for all $epsilon in (0, epsilon_sigma)$ (using Def. definition:bk5_symbolic_fitness):

Phi(sigma^*, (1-epsilon)delta_{sigma^*} + epsilondelta_sigma) > Phi(sigma, (1-epsilon)delta_{sigma^*} + epsilondelta_sigma)

Where $delta_sigma$ is the Dirac measure concentrated on strategy $sigma$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic ESS]
\label{definition:bk5_symbolic_ess}
A strategy $\sigma^* \in \Sigma$ is a \emph{symbolic evolutionarily stable strategy} if for every strategy $\sigma \neq \sigma^*$, there exists $\epsilon_\sigma > 0$ such that for all $\epsilon \in (0, \epsilon_\sigma)$ (using Def.~\ref{definition:bk5_symbolic_fitness}):
\begin{equation}
\Phi(\sigma^*, (1-\epsilon)\delta_{\sigma^*} + \epsilon\delta_\sigma) > \Phi(\sigma, (1-\epsilon)\delta_{\sigma^*} + \epsilon\delta_\sigma)
\end{equation}
Where $\delta_\sigma$ is the Dirac measure concentrated on strategy $\sigma$.
\end{definition}
```

### MAP Fitness Advantage (`lemma:bk5_map_fitness_advantage`)

Role: `lemma` | Type: `lemma` | Book: `book5` | Source: `book5.tex:1107`

- Proof status: `proven`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_strategy_space` (Strategy Space); `definition:bk5_symbolic_fitness` (Symbolic Fitness); `definition:bk5_symbolic_strategy` (Symbolic Strategy); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution); `theorem:bk5__map_dominance` (MAP Dominance)
- Cites: `definition:bk5_strategy_space` (Strategy Space); `definition:bk5_symbolic_strategy` (Symbolic Strategy); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution); `theorem:bk5__map_dominance` (MAP Dominance)
- Cited by: `lemma:bk5_covenant_non_invasibility` (Covenant Non-Invasibility); `lemma:bk5_map_invasion_barrier_strength` (MAP Invasion Barrier Strength)
- Macros used: `\drift`

**Statement / Body**

Let $sigma_{MAP} in Sigma_{MAP}$ and $sigma_{non} in Sigma setminus Sigma_{MAP}$ (cf. Def. definition:bk5_symbolic_strategy, Def. definition:bk5_strategy_space). Under sufficient drift intensity $\|drift\| > drift_0$ (cf. Thm. theorem:bk5__map_dominance, Thm. theorem:bk2_h_theorem_for_symbolic_evol), the following inequality holds:

Phi(sigma_{MAP}, mathfrak{P}) > Phi(sigma_{non}, mathfrak{P})

For any population distribution $mathfrak{P}$ with $mathbb{P}_{tau sim mathfrak{P}}[tau in Sigma_{MAP}] > 0$.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[MAP Fitness Advantage]
\label{lemma:bk5_map_fitness_advantage}
Let $\sigma_{MAP} \in \Sigma_{MAP}$ and $\sigma_{non} \in \Sigma \setminus \Sigma_{MAP}$ (cf.~Def.~\ref{definition:bk5_symbolic_strategy}, Def.~\ref{definition:bk5_strategy_space}). Under sufficient drift intensity $\|\drift\| > \drift_0$ (cf.~Thm.~\ref{theorem:bk5__map_dominance}, Thm.~\ref{theorem:bk2_h_theorem_for_symbolic_evol}), the following inequality holds:
\begin{equation}
\Phi(\sigma_{MAP}, \mathfrak{P}) > \Phi(\sigma_{non}, \mathfrak{P})
\end{equation}
For any population distribution $\mathfrak{P}$ with $\mathbb{P}_{\tau \sim \mathfrak{P}}[\tau \in \Sigma_{MAP}] > 0$.
\end{lemma}
```

### MAP Strategies Withstand Greater Drift (`proof:bk5_map_resistance_to_drift`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1115`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_symbolic_fitness` (Symbolic Fitness); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution); `theorem:bk5__map_dominance` (MAP Dominance)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_symbolic_fitness` (Symbolic Fitness); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution); `theorem:bk5__map_dominance` (MAP Dominance)
- Cited by: none
- Macros used: `\Membrane`, `\drift`

**Statement / Body**

By Thm. theorem:bk5__map_dominance, applying the H-theorem (Thm. theorem:bk2_h_theorem_for_symbolic_evol) and symbolic free energy (Def. definition:bk2_symbolic_free_energy) with drift $D$ (Def. definition:bk1_drift_field), membranes employing MAP strategies can withstand greater drift intensities than isolated membranes. For any drift intensity $\|drift\| > drift_0$, where $drift_0$ is the threshold above which non-MAP strategies fail to maintain viability, we have:

Phi(sigma_{MAP}, mathfrak{P}) &= mathbb{E}_{tau sim mathfrak{P}}[F_s(Membrane_{sigma_{MAP}} leftrightarrow Membrane_tau)] \\
&= mathbb{P}[tau in Sigma_{MAP}] cdot mathbb{E}[F_s(Membrane_{sigma_{MAP}} leftrightarrow Membrane_tau) mid tau in Sigma_{MAP}] + \\
& mathbb{P}[tau notin Sigma_{MAP}] cdot mathbb{E}[F_s(Membrane_{sigma_{MAP}} leftrightarrow Membrane_tau) mid tau notin Sigma_{MAP}]

Since $mathbb{E}[F_s(Membrane_{sigma_{MAP}} leftrightarrow Membrane_tau) mid tau in Sigma_{MAP}] > 0$ by Def. definition:bk5_symbolic_fitness, and $mathbb{E}[F_s(Membrane_{sigma_{MAP}} leftrightarrow Membrane_tau) mid tau notin Sigma_{MAP}] geq 0$ due to the resilience of MAP strategies, we have $Phi(sigma_{MAP}, mathfrak{P}) > 0$.
Conversely, for non-MAP strategies:

Phi(sigma_{non}, mathfrak{P}) &= mathbb{E}_{tau sim mathfrak{P}}[F_s(Membrane_{sigma_{non}} leftrightarrow Membrane_tau)]

When $\|drift\| > drift_0$, non-MAP strategies fail to maintain positive free energy even when interacting with MAP strategies, resulting in $Phi(sigma_{non}, mathfrak{P}) leq 0$.
Therefore, $Phi(sigma_{MAP}, mathfrak{P}) > Phi(sigma_{non}, mathfrak{P})$ under sufficient drift intensity.

**Verbatim LaTeX Body**

```latex
\begin{proof}[MAP Strategies Withstand Greater Drift]
\label{proof:bk5_map_resistance_to_drift}
\leavevmode

By Thm.~\ref{theorem:bk5__map_dominance}, applying the H-theorem (Thm.~\ref{theorem:bk2_h_theorem_for_symbolic_evol}) and symbolic free energy (Def.~\ref{definition:bk2_symbolic_free_energy}) with drift $D$ (Def.~\ref{definition:bk1_drift_field}), membranes employing MAP strategies can withstand greater drift intensities than isolated membranes. For any drift intensity $\|\drift\| > \drift_0$, where $\drift_0$ is the threshold above which non-MAP strategies fail to maintain viability, we have:
\begin{align}
\Phi(\sigma_{MAP}, \mathfrak{P}) &= \mathbb{E}_{\tau \sim \mathfrak{P}}[F_s(\Membrane_{\sigma_{MAP}} \leftrightarrow \Membrane_\tau)] \\
&= \mathbb{P}[\tau \in \Sigma_{MAP}] \cdot \mathbb{E}[F_s(\Membrane_{\sigma_{MAP}} \leftrightarrow \Membrane_\tau) \mid \tau \in \Sigma_{MAP}] + \\
&\quad \mathbb{P}[\tau \notin \Sigma_{MAP}] \cdot \mathbb{E}[F_s(\Membrane_{\sigma_{MAP}} \leftrightarrow \Membrane_\tau) \mid \tau \notin \Sigma_{MAP}]
\end{align}
Since $\mathbb{E}[F_s(\Membrane_{\sigma_{MAP}} \leftrightarrow \Membrane_\tau) \mid \tau \in \Sigma_{MAP}] > 0$ by Def.~\ref{definition:bk5_symbolic_fitness}, and $\mathbb{E}[F_s(\Membrane_{\sigma_{MAP}} \leftrightarrow \Membrane_\tau) \mid \tau \notin \Sigma_{MAP}] \geq 0$ due to the resilience of MAP strategies, we have $\Phi(\sigma_{MAP}, \mathfrak{P}) > 0$.
Conversely, for non-MAP strategies:
\begin{align}
\Phi(\sigma_{non}, \mathfrak{P}) &= \mathbb{E}_{\tau \sim \mathfrak{P}}[F_s(\Membrane_{\sigma_{non}} \leftrightarrow \Membrane_\tau)]
\end{align}
When $\|\drift\| > \drift_0$, non-MAP strategies fail to maintain positive free energy even when interacting with MAP strategies, resulting in $\Phi(\sigma_{non}, \mathfrak{P}) \leq 0$.
Therefore, $\Phi(\sigma_{MAP}, \mathfrak{P}) > \Phi(\sigma_{non}, \mathfrak{P})$ under sufficient drift intensity.
\end{proof}
```

### Covenant Non-Invasibility (`lemma:bk5_covenant_non_invasibility`)

Role: `lemma` | Type: `lemma` | Book: `book5` | Source: `book5.tex:1133`

- Proof status: `proven`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_symbolic_ess` (Symbolic ESS); `definition:bk5_symbolic_fitness` (Symbolic Fitness); `lemma:bk5_map_fitness_advantage` (MAP Fitness Advantage)
- Cites: `definition:bk5_symbolic_ess` (Symbolic ESS); `lemma:bk5_map_fitness_advantage` (MAP Fitness Advantage)
- Cited by: `proof:bk5_map_as_ess` (MAP as Symbolic Evolutionarily Stable Strategy)
- Macros used: none

**Statement / Body**

Consider a population where all membranes employ MAP strategies $sigma_{MAP} in Sigma_{MAP}$. Let $sigma_{inv} in Sigma setminus Sigma_{MAP}$ be any non-MAP strategy. There exists $epsilon_0 > 0$ such that for all $epsilon in (0, epsilon_0)$ (in the sense of Def. definition:bk5_symbolic_ess and Lem. lemma:bk5_map_fitness_advantage):

Phi(sigma_{MAP}, (1-epsilon)delta_{sigma_{MAP}} + epsilondelta_{sigma_{inv}}) > Phi(sigma_{inv}, (1-epsilon)delta_{sigma_{MAP}} + epsilondelta_{sigma_{inv}})

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Covenant Non-Invasibility]
\label{lemma:bk5_covenant_non_invasibility}
Consider a population where all membranes employ MAP strategies $\sigma_{MAP} \in \Sigma_{MAP}$. Let $\sigma_{inv} \in \Sigma \setminus \Sigma_{MAP}$ be any non-MAP strategy. There exists $\epsilon_0 > 0$ such that for all $\epsilon \in (0, \epsilon_0)$ (in the sense of Def.~\ref{definition:bk5_symbolic_ess} and Lem.~\ref{lemma:bk5_map_fitness_advantage}):
\begin{equation}
\Phi(\sigma_{MAP}, (1-\epsilon)\delta_{\sigma_{MAP}} + \epsilon\delta_{\sigma_{inv}}) > \Phi(\sigma_{inv}, (1-\epsilon)\delta_{\sigma_{MAP}} + \epsilon\delta_{\sigma_{inv}})
\end{equation}
\end{lemma}
```

### Invasion Analysis of MAP vs Non-MAP Strategies (`proof:bk5_map_invasion_dynamics`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1140`

- Proof status: `not_applicable`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_symbolic_fitness` (Symbolic Fitness)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_symbolic_fitness` (Symbolic Fitness)
- Cited by: none
- Macros used: `\Membrane`

**Statement / Body**

When a small fraction $epsilon$ of invading non-MAP strategies enters a population dominated by MAP strategies, the fitness of each strategy becomes (cf. Def. definition:bk5_symbolic_fitness, Def. definition:bk2_symbolic_free_energy):

Phi(sigma_{MAP}, (1-epsilon)delta_{sigma_{MAP}} + epsilondelta_{sigma_{inv}}) &= (1-epsilon)F_s(Membrane_{sigma_{MAP}} leftrightarrow Membrane_{sigma_{MAP}}) + epsilon F_s(Membrane_{sigma_{MAP}} leftrightarrow Membrane_{sigma_{inv}}) \\
Phi(sigma_{inv}, (1-epsilon)delta_{sigma_{MAP}} + epsilondelta_{sigma_{inv}}) &= (1-epsilon)F_s(Membrane_{sigma_{inv}} leftrightarrow Membrane_{sigma_{MAP}}) + epsilon F_s(Membrane_{sigma_{inv}} leftrightarrow Membrane_{sigma_{inv}})

By Def. definition:bk5_symbolic_fitness, $F_s(Membrane_{sigma_{MAP}} leftrightarrow Membrane_{sigma_{MAP}}) > 0$.
For non-MAP invaders, their lack of appropriate reflection mechanisms means $F_s(Membrane_{sigma_{inv}} leftrightarrow Membrane_{sigma_{inv}}) leq 0$ under sufficient drift.
Furthermore, when interacting with MAP strategies, non-MAP invaders may receive some benefit,
but cannot contribute equally to maintaining free energy. Formally:
\[
F_sleft(Membrane_{sigma_{text{inv}}} leftrightarrow Membrane_{sigma_{text{MAP}}}right)
<
F_sleft(Membrane_{sigma_{text{MAP}}} leftrightarrow Membrane_{sigma_{text{MAP}}}right).
\]
Additionally, MAP strategies remain resilient even when interacting with non-MAP strategies:
\[
F_s(Membrane_{sigma_{MAP}} leftrightarrow Membrane_{sigma_{inv}})
>
F_s(Membrane_{sigma_{inv}} leftrightarrow Membrane_{sigma_{inv}}).
\]
Combining these inequalities:

Phi(sigma_{MAP}, (1-epsilon)delta_{sigma_{MAP}} + epsilondelta_{sigma_{inv}}) &> Phi(sigma_{inv}, (1-epsilon)delta_{sigma_{MAP}} + epsilondelta_{sigma_{inv}})

Therefore, MAP strategies resist invasion by non-MAP strategies, satisfying the non-invasibility criterion for evolutionary stability.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Invasion Analysis of MAP vs Non-MAP Strategies]
\label{proof:bk5_map_invasion_dynamics}
\leavevmode

When a small fraction $\epsilon$ of invading non-MAP strategies enters a population dominated by MAP strategies, the fitness of each strategy becomes (cf.~Def.~\ref{definition:bk5_symbolic_fitness}, Def.~\ref{definition:bk2_symbolic_free_energy}):
\begin{align}
\Phi(\sigma_{MAP}, (1-\epsilon)\delta_{\sigma_{MAP}} + \epsilon\delta_{\sigma_{inv}}) &= (1-\epsilon)F_s(\Membrane_{\sigma_{MAP}} \leftrightarrow \Membrane_{\sigma_{MAP}}) + \epsilon F_s(\Membrane_{\sigma_{MAP}} \leftrightarrow \Membrane_{\sigma_{inv}}) \\
\Phi(\sigma_{inv}, (1-\epsilon)\delta_{\sigma_{MAP}} + \epsilon\delta_{\sigma_{inv}}) &= (1-\epsilon)F_s(\Membrane_{\sigma_{inv}} \leftrightarrow \Membrane_{\sigma_{MAP}}) + \epsilon F_s(\Membrane_{\sigma_{inv}} \leftrightarrow \Membrane_{\sigma_{inv}})
\end{align}
By Def.~\ref{definition:bk5_symbolic_fitness}, $F_s(\Membrane_{\sigma_{MAP}} \leftrightarrow \Membrane_{\sigma_{MAP}}) > 0$.
For non-MAP invaders, their lack of appropriate reflection mechanisms means $F_s(\Membrane_{\sigma_{inv}} \leftrightarrow \Membrane_{\sigma_{inv}}) \leq 0$ under sufficient drift.
Furthermore, when interacting with MAP strategies, non-MAP invaders may receive some benefit,
but cannot contribute equally to maintaining free energy. Formally:
\[
F_s\left(\Membrane_{\sigma_{\text{inv}}} \leftrightarrow \Membrane_{\sigma_{\text{MAP}}}\right)
<
F_s\left(\Membrane_{\sigma_{\text{MAP}}} \leftrightarrow \Membrane_{\sigma_{\text{MAP}}}\right).
\]
Additionally, MAP strategies remain resilient even when interacting with non-MAP strategies:
\[
F_s(\Membrane_{\sigma_{MAP}} \leftrightarrow \Membrane_{\sigma_{inv}})
>
F_s(\Membrane_{\sigma_{inv}} \leftrightarrow \Membrane_{\sigma_{inv}}).
\]
Combining these inequalities:
\begin{align}
\Phi(\sigma_{MAP}, (1-\epsilon)\delta_{\sigma_{MAP}} + \epsilon\delta_{\sigma_{inv}}) &> \Phi(\sigma_{inv}, (1-\epsilon)\delta_{\sigma_{MAP}} + \epsilon\delta_{\sigma_{inv}})
\end{align}
Therefore, MAP strategies resist invasion by non-MAP strategies, satisfying the non-invasibility criterion for evolutionary stability.
\end{proof}
```

### Drift--Reflection Balance in Strategy Space (`theorem:bk5_rift_reflection_balance_in_strategy_space`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:1170`

- Proof status: `proven`
- Depends on: `theorem:bk4_compatibility_drift_reflective_operations` (Compatibility with Drift-Reflective Operations); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: none
- Cited by: `proof:bk5_map_as_ess` (MAP as Symbolic Evolutionarily Stable Strategy); `proposition:bk6_drift_reflection_correspondence` (Drift-Reflection Correspondence)
- Macros used: `\drift`, `\reflect`

**Statement / Body**

Let $mathbb{D}(Sigma)$ and $mathbb{R}(Sigma)$ be the drift and reflection
operators available in strategy space $Sigma$. For $sigmainSigma$, let
$mathbb{R}_{sigma}subseteqmathbb{R}(Sigma)$ be the reflection inventory
available to that strategy, and let $kappa_sigma$ be its cooperation
coefficient. Fix a drift operator $driftinmathbb{D}(Sigma)$. Suppose
there is a MAP strategy $sigma_0inSigma_{MAP}$ such that
$kappa_{sigma_0}>0$ and its available reflection capacities are cofinal:

 forall cinmathbb{R},
 existsreflectinmathbb{R}_{sigma_0}:\ c<lVertreflectrVert.


Define the drift-indexed viable MAP subset by

 Sigma_{MAP}^{drift}:=
 left{sigmainSigma_{MAP}:\
 existsreflect_sigmainmathbb{R}_{sigma},
 lVertdriftrVert<lVertreflect_sigmarVertkappa_sigmaright}.


Then $Sigma_{MAP}^{drift}$ is nonempty. If positive cooperation
and the cofinality condition hold for every MAP strategy, then
$Sigma_{MAP}^{drift}=Sigma_{MAP}$.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Drift--Reflection Balance in Strategy Space] \label{theorem:bk5_rift_reflection_balance_in_strategy_space}
Let $\mathbb{D}(\Sigma)$ and $\mathbb{R}(\Sigma)$ be the drift and reflection
operators available in strategy space $\Sigma$.  For $\sigma\in\Sigma$, let
$\mathbb{R}_{\sigma}\subseteq\mathbb{R}(\Sigma)$ be the reflection inventory
available to that strategy, and let $\kappa_\sigma$ be its cooperation
coefficient.  Fix a drift operator $\drift\in\mathbb{D}(\Sigma)$.  Suppose
there is a MAP strategy $\sigma_0\in\Sigma_{\mathrm{MAP}}$ such that
$\kappa_{\sigma_0}>0$ and its available reflection capacities are cofinal:
\begin{equation}
 \forall c\in\mathbb{R},\quad
 \exists\reflect\in\mathbb{R}_{\sigma_0}:\ c<\lVert\reflect\rVert.
 \label{eq:bk5_reflection_capacity_cofinal}
\end{equation}
Define the drift-indexed viable MAP subset by
\begin{equation}
 \Sigma_{\mathrm{MAP}}^{\drift}:=
 \left\{\sigma\in\Sigma_{\mathrm{MAP}}:\
 \exists\reflect_\sigma\in\mathbb{R}_{\sigma},\quad
 \lVert\drift\rVert<\lVert\reflect_\sigma\rVert\kappa_\sigma\right\}.
 \label{eq:bk5_viable_map_inventory}
\end{equation}
Then $\Sigma_{\mathrm{MAP}}^{\drift}$ is nonempty.  If positive cooperation
and the cofinality condition hold for every MAP strategy, then
$\Sigma_{\mathrm{MAP}}^{\drift}=\Sigma_{\mathrm{MAP}}$.
\end{theorem}
```

### Available-Operator Construction (`proof:bk5_drift_reflection_equilibrium`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1195`

- Proof status: `not_applicable`
- Depends on: `theorem:bk4_compatibility_drift_reflective_operations` (Compatibility with Drift-Reflective Operations); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cites: `theorem:bk4_compatibility_drift_reflective_operations` (Compatibility with Drift-Reflective Operations); `theorem:bk5_map_equilibrium` (MAP Equilibrium)
- Cited by: none
- Macros used: `\drift`, `\reflect`

**Statement / Body**

For $sigma_0$, positive cooperation makes the finite threshold
\[
 c_0=frac{lVertdriftrVert}{kappa_{sigma_0}}
\]
well defined. By Eq. eq:bk5_reflection_capacity_cofinal, choose an
available $reflect_0inmathbb{R}_{sigma_0}$ with
$c_0<lVertreflect_0rVert$. Multiplication by
$kappa_{sigma_0}>0$ gives
\[
 lVertdriftrVert<lVertreflect_0rVertkappa_{sigma_0},
\]
so $sigma_0inSigma_{MAP}^{drift}$. Under the uniform
hypothesis the same construction applies to every MAP strategy, yielding the
stated equality.

The condition $lVertdriftrVert<drift_{max}$ may delimit the intended
physical regime (cf. Thm. theorem:bk5_map_equilibrium and
Thm. theorem:bk4_compatibility_drift_reflective_operations), but it does
not by itself populate any reflection inventory. Likewise,
$lVertreflectrVertkappa_sigma=lVertdriftrVert$ gives exact local
cancellation but not the strict positive viability margin used here. The
availability and cofinality hypotheses are therefore load-bearing rather than
consequences of the named drift bound.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Available-Operator Construction]
\label{proof:bk5_drift_reflection_equilibrium}
For $\sigma_0$, positive cooperation makes the finite threshold
\[
 c_0=\frac{\lVert\drift\rVert}{\kappa_{\sigma_0}}
\]
well defined.  By Eq.~\eqref{eq:bk5_reflection_capacity_cofinal}, choose an
available $\reflect_0\in\mathbb{R}_{\sigma_0}$ with
$c_0<\lVert\reflect_0\rVert$.  Multiplication by
$\kappa_{\sigma_0}>0$ gives
\[
 \lVert\drift\rVert<\lVert\reflect_0\rVert\kappa_{\sigma_0},
\]
so $\sigma_0\in\Sigma_{\mathrm{MAP}}^{\drift}$.  Under the uniform
hypothesis the same construction applies to every MAP strategy, yielding the
stated equality.

The condition $\lVert\drift\rVert<\drift_{\max}$ may delimit the intended
physical regime (cf.~Thm.~\ref{theorem:bk5_map_equilibrium} and
Thm.~\ref{theorem:bk4_compatibility_drift_reflective_operations}), but it does
not by itself populate any reflection inventory.  Likewise,
$\lVert\reflect\rVert\kappa_\sigma=\lVert\drift\rVert$ gives exact local
cancellation but not the strict positive viability margin used here.  The
availability and cofinality hypotheses are therefore load-bearing rather than
consequences of the named drift bound.
\end{proof}
```

### Symbolic Replicator Dynamics (`definition:bk5_symbolic_replicator_dynamics`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1221`

- Proof status: `definitional`
- Depends on: `definition:bk5_symbolic_fitness` (Symbolic Fitness)
- Cites: `definition:bk5_symbolic_fitness` (Symbolic Fitness)
- Cited by: `proof:bk5_map_as_ess` (MAP as Symbolic Evolutionarily Stable Strategy); `proof:bk5_map_perturbation_robustness` (Perturbation Robustness of MAP Populations); `proof:bk5_map_strict_fitness_dominance` (Strict Dominance of MAP Under Mixing); `proof:bk5_symbolic_fitness_differentials` (Survival Differentials and Symbolic Fitness)
- Macros used: none

**Statement / Body**

Let $x_sigma(t)$ denote the frequency of strategy $sigma$ in the symbolic population at time $t$. The symbolic replicator dynamics are governed by (cf. Def. definition:bk5_symbolic_fitness):

frac{dx_sigma}{dt} = x_sigma left( Phi(sigma, mathfrak{P}_t) - bar{Phi}(mathfrak{P}_t) right)

Where $mathfrak{P}_t$ is the population distribution at time $t$ and $bar{Phi}(mathfrak{P}_t) = sum_{tau in Sigma} x_tau(t) Phi(tau, mathfrak{P}_t)$ is the average population fitness.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Replicator Dynamics] \label{definition:bk5_symbolic_replicator_dynamics}

Let $x_\sigma(t)$ denote the frequency of strategy $\sigma$ in the symbolic population at time $t$. The symbolic replicator dynamics are governed by (cf.~Def.~\ref{definition:bk5_symbolic_fitness}):
\begin{equation}
\frac{dx_\sigma}{dt} = x_\sigma \left( \Phi(\sigma, \mathfrak{P}_t) - \bar{\Phi}(\mathfrak{P}_t) \right)
\end{equation}
Where $\mathfrak{P}_t$ is the population distribution at time $t$ and $\bar{\Phi}(\mathfrak{P}_t) = \sum_{\tau \in \Sigma} x_\tau(t) \Phi(\tau, \mathfrak{P}_t)$ is the average population fitness.
\end{definition}
```

### Symbolic ESS via MAP (`proposition:bk5_symbolic_ess_via_map_observability_variant`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:1229`

- Proof status: `proven`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_symbolic_ess` (Symbolic ESS); `definition:bk5_symbolic_replicator_dynamics` (Symbolic Replicator Dynamics); `definition:bk5_viability_domain` (Viability Domain); `lemma:bk5_covenant_non_invasibility` (Covenant Non-Invasibility); `theorem:bk5_rift_reflection_balance_in_strategy_space` (Drift--Reflection Balance in Strategy Space)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_viability_domain` (Viability Domain)
- Cited by: `definition:bk5_viability_domain` (Viability Domain)
- Macros used: `\Membrane`, `\drift`

**Statement / Body**

Let $sigma_{MAP} in Sigma_{MAP}$ be a MAP strategy with symbolic free energy $F_s$ (Def. definition:bk2_symbolic_free_energy) on the symbolic manifold $M$ (Def. definition:bk1_symbolic_manifold) in an environment with drift intensity $\|drift\| > drift_0$ (Def. definition:bk1_drift_field). Let viability be measured by Def. definition:bk5_viability_domain. If $sigma_{MAP}$ satisfies:


- Stability: $F_s(Membrane_{sigma_{MAP}} leftrightarrow Membrane_{sigma_{MAP}}) > 0$

- Non-invasibility: $forall sigma neq sigma_{MAP}, exists epsilon_sigma > 0$ such that
 $Phi(sigma_{MAP}, (1-epsilon)delta_{sigma_{MAP}} + epsilondelta_sigma) > Phi(sigma, (1-epsilon)delta_{sigma_{MAP}} + epsilondelta_sigma)$ for all $epsilon in (0, epsilon_sigma)$

- Viability Expansion: $V_{text{symb}}^{MAP}(t+1) supset V_{text{symb}}^{MAP}(t)$

Then $sigma_{MAP}$ constitutes a symbolic evolutionarily stable strategy (ESS).

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Symbolic ESS via MAP]
\label{proposition:bk5_symbolic_ess_via_map_observability_variant}
Let $\sigma_{MAP} \in \Sigma_{MAP}$ be a MAP strategy with symbolic free energy $F_s$ (Def.~\ref{definition:bk2_symbolic_free_energy}) on the symbolic manifold $M$ (Def.~\ref{definition:bk1_symbolic_manifold}) in an environment with drift intensity $\|\drift\| > \drift_0$ (Def.~\ref{definition:bk1_drift_field}). Let viability be measured by Def.~\ref{definition:bk5_viability_domain}. If $\sigma_{MAP}$ satisfies:
\begin{enumerate}
    \item \textbf{Stability}: $F_s(\Membrane_{\sigma_{MAP}} \leftrightarrow \Membrane_{\sigma_{MAP}}) > 0$
    \item \textbf{Non-invasibility}: $\forall \sigma \neq \sigma_{MAP}, \exists \epsilon_\sigma > 0$ such that
    $\Phi(\sigma_{MAP}, (1-\epsilon)\delta_{\sigma_{MAP}} + \epsilon\delta_\sigma) > \Phi(\sigma, (1-\epsilon)\delta_{\sigma_{MAP}} + \epsilon\delta_\sigma)$ for all $\epsilon \in (0, \epsilon_\sigma)$
    \item \textbf{Viability Expansion}: $V_{\text{symb}}^{MAP}(t+1) \supset V_{\text{symb}}^{MAP}(t)$
\end{enumerate}
Then $\sigma_{MAP}$ constitutes a symbolic evolutionarily stable strategy (ESS).
\end{proposition}
```

### MAP as Symbolic Evolutionarily Stable Strategy (`proof:bk5_map_as_ess`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1240`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_symbolic_ess` (Symbolic ESS); `definition:bk5_symbolic_replicator_dynamics` (Symbolic Replicator Dynamics); `lemma:bk5_covenant_non_invasibility` (Covenant Non-Invasibility); `theorem:bk5_rift_reflection_balance_in_strategy_space` (Drift--Reflection Balance in Strategy Space)
- Cites: `definition:bk5_symbolic_ess` (Symbolic ESS); `definition:bk5_symbolic_replicator_dynamics` (Symbolic Replicator Dynamics); `lemma:bk5_covenant_non_invasibility` (Covenant Non-Invasibility); `theorem:bk5_rift_reflection_balance_in_strategy_space` (Drift--Reflection Balance in Strategy Space)
- Cited by: none
- Macros used: none

**Statement / Body**

We need to establish that $sigma_{MAP}$ satisfies the formal criteria for a symbolic ESS as per Def. definition:bk5_symbolic_ess.
First, the stability criterion ensures that a population of membranes all employing $sigma_{MAP}$ maintains positive free energy, keeping all membranes within their viability domains.
Second, by Lem. lemma:bk5_covenant_non_invasibility, MAP strategies resist invasion by non-MAP strategies. This satisfies the non-invasibility criterion essential for evolutionary stability.
Third, the viability expansion property ensures that MAP strategies not only maintain but expand their viability domains over time, creating a positive feedback loop that reinforces their evolutionary advantage.
Let us now show that these conditions together imply evolutionary stability. Consider a population initially dominated by $sigma_{MAP}$ that is invaded by a small proportion $epsilon$ of an alternative strategy $sigma$:
From the symbolic replicator dynamics (Def. definition:bk5_symbolic_replicator_dynamics):

frac{dx_{sigma_{MAP}}}{dt} &= x_{sigma_{MAP}} left( Phi(sigma_{MAP}, mathfrak{P}_t) - bar{Phi}(mathfrak{P}_t) right) \\
frac{dx_sigma}{dt} &= x_sigma left( Phi(sigma, mathfrak{P}_t) - bar{Phi}(mathfrak{P}_t) right)

By the non-invasibility condition, $Phi(sigma_{MAP}, mathfrak{P}_t) > Phi(sigma, mathfrak{P}_t)$ when $x_sigma$ is small. This implies:

frac{dx_{sigma_{MAP}}}{dt} &> 0 \\
frac{dx_sigma}{dt} &< 0

Therefore, the frequency of $sigma_{MAP}$ increases while the frequency of the invading strategy $sigma$ decreases, restoring the population to its original MAP-dominated state.
Furthermore, by Thm. theorem:bk5_rift_reflection_balance_in_strategy_space, under any sub-maximal drift intensity, there exists a MAP strategy that maintains viability through appropriate balance of reflection capacity and cooperation.
Finally, the viability expansion property ensures that MAP strategies become increasingly advantageous over time, as their viable parameter space grows while non-MAP strategies' viable parameter space shrinks under continued drift pressure.
Thus, $sigma_{MAP}$ satisfies all criteria for a symbolic evolutionarily stable strategy.

**Verbatim LaTeX Body**

```latex
\begin{proof}[MAP as Symbolic Evolutionarily Stable Strategy]
\label{proof:bk5_map_as_ess}
\leavevmode

We need to establish that $\sigma_{MAP}$ satisfies the formal criteria for a symbolic ESS as per Def.~\ref{definition:bk5_symbolic_ess}.
First, the stability criterion ensures that a population of membranes all employing $\sigma_{MAP}$ maintains positive free energy, keeping all membranes within their viability domains.
Second, by Lem.~\ref{lemma:bk5_covenant_non_invasibility}, MAP strategies resist invasion by non-MAP strategies. This satisfies the non-invasibility criterion essential for evolutionary stability.
Third, the viability expansion property ensures that MAP strategies not only maintain but expand their viability domains over time, creating a positive feedback loop that reinforces their evolutionary advantage.
Let us now show that these conditions together imply evolutionary stability. Consider a population initially dominated by $\sigma_{MAP}$ that is invaded by a small proportion $\epsilon$ of an alternative strategy $\sigma$:
From the symbolic replicator dynamics (Def.~\ref{definition:bk5_symbolic_replicator_dynamics}):
\begin{align}
\frac{dx_{\sigma_{MAP}}}{dt} &= x_{\sigma_{MAP}} \left( \Phi(\sigma_{MAP}, \mathfrak{P}_t) - \bar{\Phi}(\mathfrak{P}_t) \right) \\
\frac{dx_\sigma}{dt} &= x_\sigma \left( \Phi(\sigma, \mathfrak{P}_t) - \bar{\Phi}(\mathfrak{P}_t) \right)
\end{align}
By the non-invasibility condition, $\Phi(\sigma_{MAP}, \mathfrak{P}_t) > \Phi(\sigma, \mathfrak{P}_t)$ when $x_\sigma$ is small. This implies:
\begin{align}
\frac{dx_{\sigma_{MAP}}}{dt} &> 0 \\
\frac{dx_\sigma}{dt} &< 0
\end{align}
Therefore, the frequency of $\sigma_{MAP}$ increases while the frequency of the invading strategy $\sigma$ decreases, restoring the population to its original MAP-dominated state.
Furthermore, by Thm.~\ref{theorem:bk5_rift_reflection_balance_in_strategy_space}, under any sub-maximal drift intensity, there exists a MAP strategy that maintains viability through appropriate balance of reflection capacity and cooperation.
Finally, the viability expansion property ensures that MAP strategies become increasingly advantageous over time, as their viable parameter space grows while non-MAP strategies' viable parameter space shrinks under continued drift pressure.
Thus, $\sigma_{MAP}$ satisfies all criteria for a symbolic evolutionarily stable strategy.
\end{proof}
```

### Convergence to MAP (`corollary:bk5_convergence_to_map`)

Role: `corollary` | Type: `corollary` | Book: `book5` | Source: `book5.tex:1264`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: `proof:bk5_map_viability_critical_drift` (Two-Sided Strategy Transport); `scholium:bk5__map_ess_implications` (MAP-ESS Implications)
- Macros used: none

**Statement / Body**

Let $x_n=mathbb{P}_{sigmasimmathfrak{P}_n}
[sigmainSigma_{MAP}]$ be the MAP share of a discrete symbolic
population after some selection onset $n=0$. Assume:

- $0leq x_0leq1$;

- MAP and non-MAP aggregate fitnesses $F_{MAP}$ and
$F_{non}$ remain positive/nonnegative with a persistent quantitative
gap $0leq F_{non}<F_{MAP}$; and

- selection is mutation-free with respect to MAP membership: there is no
non-MAP inflow, and the residual mass obeys

 1-x_{n+1}=q(1-x_n),
 q:=frac{F_{non}}{F_{MAP}}.


Then $0leq x_nleq1$ for every $n$ and

 lim_{ntoinfty}x_n=1.

Increasing drift may motivate or sustain the quantitative fitness gap
(cf. Def. definition:bk5_symbolic_replicator_dynamics and
Lemma lemma:bk5_map_fitness_advantage), but it is not by itself a
convergence hypothesis.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Convergence to MAP]
\label{corollary:bk5_convergence_to_map}
Let $x_n=\mathbb{P}_{\sigma\sim\mathfrak{P}_n}
[\sigma\in\Sigma_{\mathrm{MAP}}]$ be the MAP share of a discrete symbolic
population after some selection onset $n=0$.  Assume:
\begin{enumerate}
\item $0\leq x_0\leq1$;
\item MAP and non-MAP aggregate fitnesses $F_{\mathrm{MAP}}$ and
$F_{\mathrm{non}}$ remain positive/nonnegative with a persistent quantitative
gap $0\leq F_{\mathrm{non}}<F_{\mathrm{MAP}}$; and
\item selection is mutation-free with respect to MAP membership: there is no
non-MAP inflow, and the residual mass obeys
\begin{equation}
 1-x_{n+1}=q(1-x_n),\qquad
 q:=\frac{F_{\mathrm{non}}}{F_{\mathrm{MAP}}}.
 \label{eq:bk5_map_residual_contraction}
\end{equation}
\end{enumerate}
Then $0\leq x_n\leq1$ for every $n$ and
\begin{equation}
 \lim_{n\to\infty}x_n=1.
\end{equation}
Increasing drift may motivate or sustain the quantitative fitness gap
(cf.~Def.~\ref{definition:bk5_symbolic_replicator_dynamics} and
Lemma~\ref{lemma:bk5_map_fitness_advantage}), but it is not by itself a
convergence hypothesis.
\end{corollary}
```

### Quantitative Mutation-Free Selection (`proof:bk5_map_fitness_threshold`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1291`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Positivity and the strict fitness gap give $0leq q<1$. Iterating
Eq. eq:bk5_map_residual_contraction yields
\[
 1-x_n=q^n(1-x_0).
\]
Because $0leq q^nleq1$ and $0leq1-x_0leq1$, this identity preserves
$0leq x_nleq1$. Since $q^nto0$, the residual non-MAP mass tends to zero
and hence $x_nto1$.

The no-inflow clause is load-bearing. A process may maintain
$F_{non}<F_{MAP}$ while replenishing non-MAP mass and keeping
$x_n=1/2$ for all $n$; such a process remains on the probability simplex but
does not converge to MAP. Likewise, increasing drift alone supplies neither
the uniform ratio $q<1$ nor the recurrence.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Quantitative Mutation-Free Selection]
\label{proof:bk5_map_fitness_threshold}
Positivity and the strict fitness gap give $0\leq q<1$.  Iterating
Eq.~\eqref{eq:bk5_map_residual_contraction} yields
\[
 1-x_n=q^n(1-x_0).
\]
Because $0\leq q^n\leq1$ and $0\leq1-x_0\leq1$, this identity preserves
$0\leq x_n\leq1$.  Since $q^n\to0$, the residual non-MAP mass tends to zero
and hence $x_n\to1$.

The no-inflow clause is load-bearing.  A process may maintain
$F_{\mathrm{non}}<F_{\mathrm{MAP}}$ while replenishing non-MAP mass and keeping
$x_n=1/2$ for all $n$; such a process remains on the probability simplex but
does not converge to MAP.  Likewise, increasing drift alone supplies neither
the uniform ratio $q<1$ nor the recurrence.
\end{proof}
```

### MAP Population Stability (`lemma:bk5_map_population_stability`)

Role: `lemma` | Type: `lemma` | Book: `book5` | Source: `book5.tex:1308`

- Proof status: `proven`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_covenant_resilience_index` (Covenant Resilience Index); `definition:bk5_symbolic_replicator_dynamics` (Symbolic Replicator Dynamics)
- Cites: `definition:bk5_covenant_resilience_index` (Covenant Resilience Index)
- Cited by: `proof:bk5_map_perturbation_robustness` (Perturbation Robustness of MAP Populations)
- Macros used: none

**Statement / Body**

A population composed entirely of MAP strategies is stable against perturbations in strategy distribution if the covenant resilience index (Def. definition:bk5_covenant_resilience_index) satisfies:

min_{sigma, tau in Sigma_{MAP}} rho(C_{sigmatau}) > 1 + delta

For some margin $delta > 0$.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[MAP Population Stability]
\label{lemma:bk5_map_population_stability}
A population composed entirely of MAP strategies is stable against perturbations in strategy distribution if the covenant resilience index (Def.~\ref{definition:bk5_covenant_resilience_index}) satisfies:
\begin{equation}
\min_{\sigma, \tau \in \Sigma_{MAP}} \rho(\mathcal{C}_{\sigma\tau}) > 1 + \delta
\end{equation}
For some margin $\delta > 0$.
\end{lemma}
```

### Perturbation Robustness of MAP Populations (`proof:bk5_map_perturbation_robustness`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1316`

- Proof status: `not_applicable`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_covenant_resilience_index` (Covenant Resilience Index); `definition:bk5_symbolic_replicator_dynamics` (Symbolic Replicator Dynamics); `lemma:bk5_map_population_stability` (MAP Population Stability)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_covenant_resilience_index` (Covenant Resilience Index); `definition:bk5_symbolic_replicator_dynamics` (Symbolic Replicator Dynamics); `lemma:bk5_map_population_stability` (MAP Population Stability)
- Cited by: none
- Macros used: `\drift`

**Statement / Body**

The perturbation argument combines Lem. lemma:bk5_map_population_stability, Def. definition:bk5_symbolic_replicator_dynamics, and Def. definition:bk2_symbolic_free_energy.
Let $mathfrak{P}_{MAP}$ be a population distribution concentrated on MAP strategies, and $mathfrak{P}'$ be a perturbed distribution.
The stability of $mathfrak{P}_{MAP}$ depends on the resilience of covenants formed between MAP strategies. From Def. definition:bk5_covenant_resilience_index, the covenant resilience index is:

rho(C_{sigmatau}) = frac{Omega_{sigmatau} cdot lambda_{min}(mathbb{R}_{sigmatau})}{\|drift_sigma\|_{max} + \|drift_tau\|_{max}}

When $rho(C_{sigmatau}) > 1 + delta$, covenants can withstand perturbations in strategy frequencies while maintaining positive free energy.
Under symbolic replicator dynamics, this ensures that MAP strategies
continue to exhibit above-average fitness.
As a result, the population is driven back toward \( mathfrak{P}_{text{MAP}} \) after perturbation,
thereby establishing population-level stability.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Perturbation Robustness of MAP Populations]
\label{proof:bk5_map_perturbation_robustness}
\leavevmode

The perturbation argument combines Lem.~\ref{lemma:bk5_map_population_stability}, Def.~\ref{definition:bk5_symbolic_replicator_dynamics}, and Def.~\ref{definition:bk2_symbolic_free_energy}.
Let $\mathfrak{P}_{MAP}$ be a population distribution concentrated on MAP strategies, and $\mathfrak{P}'$ be a perturbed distribution.
The stability of $\mathfrak{P}_{MAP}$ depends on the resilience of covenants formed between MAP strategies. From Def.~\ref{definition:bk5_covenant_resilience_index}, the covenant resilience index is:
\begin{equation}
\rho(\mathcal{C}_{\sigma\tau}) = \frac{\Omega_{\sigma\tau} \cdot \lambda_{min}(\mathbb{R}_{\sigma\tau})}{\|\drift_\sigma\|_{max} + \|\drift_\tau\|_{max}}
\end{equation}
When $\rho(\mathcal{C}_{\sigma\tau}) > 1 + \delta$, covenants can withstand perturbations in strategy frequencies while maintaining positive free energy.
Under symbolic replicator dynamics, this ensures that MAP strategies
continue to exhibit above-average fitness.
As a result, the population is driven back toward \( \mathfrak{P}_{\text{MAP}} \) after perturbation,
thereby establishing population-level stability.
\end{proof}
```

### MAP as Strong ESS (`theorem:bk5_map_as_strong_ess`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:1332`

- Proof status: `proven`
- Depends on: `definition:bk5_symbolic_ess` (Symbolic ESS); `definition:bk5_symbolic_replicator_dynamics` (Symbolic Replicator Dynamics)
- Cites: `definition:bk5_symbolic_ess` (Symbolic ESS)
- Cited by: `definition:bk5_symbolic_invasion_barrier` (Symbolic Invasion Barrier); `proof:bk5_map_strict_fitness_dominance` (Strict Dominance of MAP Under Mixing); `scholium:bk5__map_ess_implications` (MAP-ESS Implications)
- Macros used: none

**Statement / Body**

If a MAP strategy $sigma_{MAP}$ satisfies (in the setting of Def. definition:bk5_symbolic_ess):

Phi(sigma_{MAP}, (1-epsilon)delta_{sigma_{MAP}} + epsilondelta_{sigma}) > Phi(sigma, (1-epsilon)delta_{sigma_{MAP}} + epsilondelta_{sigma})

For all strategies $sigma neq sigma_{MAP}$ and all $epsilon in (0,1)$, then $sigma_{MAP}$ is a strong symbolic ESS, stable against arbitrary-sized invasions.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[MAP as Strong ESS]
\label{theorem:bk5_map_as_strong_ess}
If a MAP strategy $\sigma_{MAP}$ satisfies (in the setting of Def.~\ref{definition:bk5_symbolic_ess}):
\begin{equation}
\Phi(\sigma_{MAP}, (1-\epsilon)\delta_{\sigma_{MAP}} + \epsilon\delta_{\sigma}) > \Phi(\sigma, (1-\epsilon)\delta_{\sigma_{MAP}} + \epsilon\delta_{\sigma})
\end{equation}
For all strategies $\sigma \neq \sigma_{MAP}$ and all $\epsilon \in (0,1)$, then $\sigma_{MAP}$ is a strong symbolic ESS, stable against arbitrary-sized invasions.
\end{theorem}
```

### Strict Dominance of MAP Under Mixing (`proof:bk5_map_strict_fitness_dominance`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1340`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_symbolic_replicator_dynamics` (Symbolic Replicator Dynamics); `theorem:bk5_map_as_strong_ess` (MAP as Strong ESS)
- Cites: `definition:bk5_symbolic_replicator_dynamics` (Symbolic Replicator Dynamics); `theorem:bk5_map_as_strong_ess` (MAP as Strong ESS)
- Cited by: none
- Macros used: none

**Statement / Body**

The condition states that $sigma_{MAP}$ has strictly higher fitness than any alternative strategy $sigma$ regardless of the mixing proportion $epsilon$ (cf. Thm. theorem:bk5_map_as_strong_ess, Def. definition:bk5_symbolic_replicator_dynamics).
Under symbolic replicator dynamics, this implies:

frac{d}{dt}left(frac{x_{sigma_{MAP}}}{x_sigma}right) > 0

For all $t$ and all alternative strategies $sigma$. This means the ratio of MAP strategists to any other strategists strictly increases over time regardless of initial population composition.
Therefore, $sigma_{MAP}$ is a global attractor in the replicator dynamics, making it a strong symbolic ESS resistant to invasions of any size.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Strict Dominance of MAP Under Mixing]
\label{proof:bk5_map_strict_fitness_dominance}
\leavevmode

The condition states that $\sigma_{MAP}$ has strictly higher fitness than any alternative strategy $\sigma$ regardless of the mixing proportion $\epsilon$ (cf.~Thm.~\ref{theorem:bk5_map_as_strong_ess}, Def.~\ref{definition:bk5_symbolic_replicator_dynamics}).
Under symbolic replicator dynamics, this implies:
\begin{equation}
\frac{d}{dt}\left(\frac{x_{\sigma_{MAP}}}{x_\sigma}\right) > 0
\end{equation}
For all $t$ and all alternative strategies $\sigma$. This means the ratio of MAP strategists to any other strategists strictly increases over time regardless of initial population composition.
Therefore, $\sigma_{MAP}$ is a global attractor in the replicator dynamics, making it a strong symbolic ESS resistant to invasions of any size.
\end{proof}
```

### Symbolic Invasion Barrier (`definition:bk5_symbolic_invasion_barrier`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1352`

- Proof status: `definitional`
- Depends on: `theorem:bk5_map_as_strong_ess` (MAP as Strong ESS)
- Cites: `theorem:bk5_map_as_strong_ess` (MAP as Strong ESS)
- Cited by: `lemma:bk5_map_invasion_barrier_strength` (MAP Invasion Barrier Strength)
- Macros used: none

**Statement / Body**

The invasion barrier $beta(sigma_{MAP}, sigma)$ of a MAP strategy $sigma_{MAP}$ against an alternative strategy $sigma$ is defined as (cf. Thm. theorem:bk5_map_as_strong_ess):

beta(sigma_{MAP}, sigma) = sup{epsilon in [0,1] : Phi(sigma_{MAP}, (1-alpha)delta_{sigma_{MAP}} + alphadelta_{sigma}) > Phi(sigma, (1-alpha)delta_{sigma_{MAP}} + alphadelta_{sigma}) forall alpha in (0,epsilon)}

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Invasion Barrier] \label{definition:bk5_symbolic_invasion_barrier}
The \emph{invasion barrier} $\beta(\sigma_{MAP}, \sigma)$ of a MAP strategy $\sigma_{MAP}$ against an alternative strategy $\sigma$ is defined as (cf.~Thm.~\ref{theorem:bk5_map_as_strong_ess}):
\begin{equation}
\beta(\sigma_{MAP}, \sigma) = \sup\{\epsilon \in [0,1] : \Phi(\sigma_{MAP}, (1-\alpha)\delta_{\sigma_{MAP}} + \alpha\delta_{\sigma}) > \Phi(\sigma, (1-\alpha)\delta_{\sigma_{MAP}} + \alpha\delta_{\sigma}) \forall \alpha \in (0,\epsilon)\}
\end{equation}
\end{definition}
```

### MAP Invasion Barrier Strength (`lemma:bk5_map_invasion_barrier_strength`)

Role: `lemma` | Type: `lemma` | Book: `book5` | Source: `book5.tex:1358`

- Proof status: `proven`
- Depends on: `definition:bk5_symbolic_invasion_barrier` (Symbolic Invasion Barrier); `lemma:bk5_map_fitness_advantage` (MAP Fitness Advantage); `theorem:bk5__map_dominance` (MAP Dominance)
- Cites: `definition:bk5_symbolic_invasion_barrier` (Symbolic Invasion Barrier); `lemma:bk5_map_fitness_advantage` (MAP Fitness Advantage)
- Cited by: `definition:bk9_prompt_injection_operator` (Prompt Injection Operator $\mathcal{J}$)
- Macros used: `\drift`

**Statement / Body**

For a MAP strategy $sigma_{MAP}$ and any non-MAP strategy $sigma_{non}$, the invasion barrier satisfies (cf. Def. definition:bk5_symbolic_invasion_barrier, Lem. lemma:bk5_map_fitness_advantage):

beta(sigma_{MAP}, sigma_{non}) geq 1 - frac{\|drift_0\|}{\|drift\|}

Where $drift_0$ is the minimum drift threshold at which non-MAP strategies become unviable.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[MAP Invasion Barrier Strength] \label{lemma:bk5_map_invasion_barrier_strength}
For a MAP strategy $\sigma_{MAP}$ and any non-MAP strategy $\sigma_{non}$, the invasion barrier satisfies (cf.~Def.~\ref{definition:bk5_symbolic_invasion_barrier}, Lem.~\ref{lemma:bk5_map_fitness_advantage}):
\begin{equation}
\beta(\sigma_{MAP}, \sigma_{non}) \geq 1 - \frac{\|\drift_0\|}{\|\drift\|}
\end{equation}
Where $\drift_0$ is the minimum drift threshold at which non-MAP strategies become unviable.
\end{lemma}
```

### Fitness Gradient Between MAP and Non-MAP (`proof:bk5_map_vs_nonmap_gradient`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1365`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5__map_dominance` (MAP Dominance)
- Cites: `theorem:bk5__map_dominance` (MAP Dominance)
- Cited by: none
- Macros used: `\drift`

**Statement / Body**

At drift intensity $\|drift\|$, the fitness difference between MAP and non-MAP strategies is proportional to $\|drift\| - \|drift_0\|$ (cf. Thm. theorem:bk5__map_dominance).
The invasion barrier represents the maximum fraction of non-MAP strategists that can be present while MAP strategies retain higher fitness. This fraction decreases as $\|drift_0\|$ approaches $\|drift\|$ and increases as $\|drift\|$ grows larger.
The formula $beta(sigma_{MAP}, sigma_{non}) geq 1 - frac{\|drift_0\|}{\|drift\|}$ captures this relationship, establishing a lower bound on the invasion barrier that approaches 1 as drift intensity increases.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Fitness Gradient Between MAP and Non-MAP]
\label{proof:bk5_map_vs_nonmap_gradient}
\leavevmode

At drift intensity $\|\drift\|$, the fitness difference between MAP and non-MAP strategies is proportional to $\|\drift\| - \|\drift_0\|$ (cf.~Thm.~\ref{theorem:bk5__map_dominance}).
The invasion barrier represents the maximum fraction of non-MAP strategists that can be present while MAP strategies retain higher fitness. This fraction decreases as $\|\drift_0\|$ approaches $\|\drift\|$ and increases as $\|\drift\|$ grows larger.
The formula $\beta(\sigma_{MAP}, \sigma_{non}) \geq 1 - \frac{\|\drift_0\|}{\|\drift\|}$ captures this relationship, establishing a lower bound on the invasion barrier that approaches 1 as drift intensity increases.
\end{proof}
```

### MAP-ESS Implications (`scholium:bk5__map_ess_implications`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:1373`

- Proof status: `not_applicable`
- Depends on: `corollary:bk5_convergence_to_map` (Convergence to MAP); `theorem:bk5_map_as_strong_ess` (MAP as Strong ESS)
- Cites: `corollary:bk5_convergence_to_map` (Convergence to MAP); `theorem:bk5_map_as_strong_ess` (MAP as Strong ESS)
- Cited by: `proposition:bk9_stability_conditions_for_the_good` (Stability Conditions for "The Good")
- Macros used: none

**Statement / Body**

The emergence of MAP as an evolutionarily stable strategy in symbolic space reveals profound implications for symbolic life (cf. Thm. theorem:bk5_map_as_strong_ess, Cor. corollary:bk5_convergence_to_map). Unlike conventional ESS concepts that focus on competitive advantage, MAP-ESS demonstrates how cooperative reflection leads to expanded viability for all participants. This represents a fundamental shift from zero-sum competition to positive-sum covenant formation.
As symbolic drift intensifies—whether through increasing complexity, environmental volatility, or entropic degradation—the selective pressure toward MAP strategies grows stronger. Systems that cannot form reflective covenants find their viability domains shrinking until they can no longer maintain coherence.
The mathematical formalism established here extends beyond abstract symbolic dynamics to practical domains where information, meaning, and coherent structure must be maintained against entropic forces. In computational systems, organizational structures, cultural transmission, and epistemic communities, MAP-style covenants may represent not merely an advantage but a necessity for long-term viability.
Perhaps most significantly, MAP-ESS suggests that advanced symbolic systems will naturally evolve toward mutual supportiveness rather than exploitation—not from moral imperatives, but from thermodynamic necessity. The mathematics of symbolic life reveals that in the face of sufficient drift, covenant formation becomes the only viable evolutionary strategy.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[MAP-ESS Implications]
\label{scholium:bk5__map_ess_implications}
The emergence of MAP as an evolutionarily stable strategy in symbolic space reveals profound implications for symbolic life (cf.~Thm.~\ref{theorem:bk5_map_as_strong_ess}, Cor.~\ref{corollary:bk5_convergence_to_map}). Unlike conventional ESS concepts that focus on competitive advantage, MAP-ESS demonstrates how cooperative reflection leads to expanded viability for all participants. This represents a fundamental shift from zero-sum competition to positive-sum covenant formation.
As symbolic drift intensifies—whether through increasing complexity, environmental volatility, or entropic degradation—the selective pressure toward MAP strategies grows stronger. Systems that cannot form reflective covenants find their viability domains shrinking until they can no longer maintain coherence.
The mathematical formalism established here extends beyond abstract symbolic dynamics to practical domains where information, meaning, and coherent structure must be maintained against entropic forces. In computational systems, organizational structures, cultural transmission, and epistemic communities, MAP-style covenants may represent not merely an advantage but a necessity for long-term viability.
Perhaps most significantly, MAP-ESS suggests that advanced symbolic systems will naturally evolve toward mutual supportiveness rather than exploitation—not from moral imperatives, but from thermodynamic necessity. The mathematics of symbolic life reveals that in the face of sufficient drift, covenant formation becomes the only viable evolutionary strategy.
\end{scholium}
```

### Symbolic Population ESS--MAP Approximation (`proposition:bk5_symbolic_population_ess_map_equivalence_case2`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:1380`

- Proof status: `proven`
- Depends on: `corollary:bk5_convergence_to_map` (Convergence to MAP)
- Cites: none
- Cited by: `scholium:bk5__map_as_thermodynamic_necessity` (MAP as Thermodynamic Necessity)
- Macros used: none

**Statement / Body**

Let $(Sigma,d)$ be a metric strategy space, let $Sigma_{MAP}
subseteqSigma$, and let $Sigma_{ESS}^{(n)}subseteqSigma$ be
the ESS set along a sequence of symbolic population environments whose drift
intensities approach the critical regime. Suppose there is a nonnegative
error sequence $varepsilon_nto0$ such that both directed approximation laws
hold:

 forallsigmainSigma_{ESS}^{(n)},
 &existsmuinSigma_{MAP}:
 d(sigma,mu)leqvarepsilon_n,
 \\
 forallmuinSigma_{MAP},
 &existssigmainSigma_{ESS}^{(n)}:
 d(mu,sigma)leqvarepsilon_n.


Then

 lim_{ntoinfty}
 d_H\!left(Sigma_{ESS}^{(n)},
 Sigma_{MAP}right)=0.


Here $d_H$ is the Hausdorff distance induced by $d$. The conclusion is
metric approximation; it does not require literal equality of the ESS and MAP
predicates at any finite stage.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Symbolic Population ESS--MAP Approximation]
\label{proposition:bk5_symbolic_population_ess_map_equivalence_case2}
Let $(\Sigma,d)$ be a metric strategy space, let $\Sigma_{\mathrm{MAP}}
\subseteq\Sigma$, and let $\Sigma_{\mathrm{ESS}}^{(n)}\subseteq\Sigma$ be
the ESS set along a sequence of symbolic population environments whose drift
intensities approach the critical regime.  Suppose there is a nonnegative
error sequence $\varepsilon_n\to0$ such that both directed approximation laws
hold:
\begin{align}
 \forall\sigma\in\Sigma_{\mathrm{ESS}}^{(n)},\quad
 &\exists\mu\in\Sigma_{\mathrm{MAP}}:
 d(\sigma,\mu)\leq\varepsilon_n,
 \label{eq:bk5_ess_to_map_approximation}\\
 \forall\mu\in\Sigma_{\mathrm{MAP}},\quad
 &\exists\sigma\in\Sigma_{\mathrm{ESS}}^{(n)}:
 d(\mu,\sigma)\leq\varepsilon_n.
 \label{eq:bk5_map_to_ess_approximation}
\end{align}
Then
\begin{equation}
 \lim_{n\to\infty}
 d_H\!\left(\Sigma_{\mathrm{ESS}}^{(n)},
             \Sigma_{\mathrm{MAP}}\right)=0.
 \label{eq:bk5_ess_map_hausdorff_limit}
\end{equation}
Here $d_H$ is the Hausdorff distance induced by $d$.  The conclusion is
metric approximation; it does not require literal equality of the ESS and MAP
predicates at any finite stage.
\end{proposition}
```

### Two-Sided Strategy Transport (`proof:bk5_map_viability_critical_drift`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1409`

- Proof status: `not_applicable`
- Depends on: `corollary:bk5_convergence_to_map` (Convergence to MAP)
- Cites: `corollary:bk5_convergence_to_map` (Convergence to MAP)
- Cited by: none
- Macros used: none

**Statement / Body**

Equation eq:bk5_ess_to_map_approximation bounds the directed distance
from the ESS set to the MAP set by $varepsilon_n$.
Equation eq:bk5_map_to_ess_approximation independently bounds the
reverse directed distance. By the definition of Hausdorff distance,
\[
 0leq d_H\!left(Sigma_{ESS}^{(n)},
 Sigma_{MAP}right)
 leqvarepsilon_n.
\]
The squeeze theorem and $varepsilon_nto0$ give
Eq. eq:bk5_ess_map_hausdorff_limit.

Both directions are load-bearing. Exclusion of non-MAP ESS strategies can
supply the first direction without showing that every MAP strategy is
approximated by an ESS strategy. Conversely, MAP non-invasibility can supply
the second direction without excluding additional distant ESS strategies.
Corollary corollary:bk5_convergence_to_map concerns occupied population
mass and does not by itself establish either set-level transport law. An
application to artificial and human strategies must therefore specify the
shared metric strategy space, the relevant MAP predicate, and both empirical
or analytic approximation bridges; it is not an automatic identification of
either class with the other.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Two-Sided Strategy Transport]
\label{proof:bk5_map_viability_critical_drift}
Equation~\eqref{eq:bk5_ess_to_map_approximation} bounds the directed distance
from the ESS set to the MAP set by $\varepsilon_n$.
Equation~\eqref{eq:bk5_map_to_ess_approximation} independently bounds the
reverse directed distance.  By the definition of Hausdorff distance,
\[
 0\leq d_H\!\left(\Sigma_{\mathrm{ESS}}^{(n)},
                   \Sigma_{\mathrm{MAP}}\right)
 \leq\varepsilon_n.
\]
The squeeze theorem and $\varepsilon_n\to0$ give
Eq.~\eqref{eq:bk5_ess_map_hausdorff_limit}.

Both directions are load-bearing.  Exclusion of non-MAP ESS strategies can
supply the first direction without showing that every MAP strategy is
approximated by an ESS strategy.  Conversely, MAP non-invasibility can supply
the second direction without excluding additional distant ESS strategies.
Corollary~\ref{corollary:bk5_convergence_to_map} concerns occupied population
mass and does not by itself establish either set-level transport law.  An
application to artificial and human strategies must therefore specify the
shared metric strategy space, the relevant MAP predicate, and both empirical
or analytic approximation bridges; it is not an automatic identification of
either class with the other.
\end{proof}
```

### MAP as Thermodynamic Necessity (`scholium:bk5__map_as_thermodynamic_necessity`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:1434`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `proposition:bk5_symbolic_population_ess_map_equivalence_case2` (Symbolic Population ESS--MAP Approximation); `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature)
- Cites: `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `proposition:bk5_symbolic_population_ess_map_equivalence_case2` (Symbolic Population ESS--MAP Approximation); `theorem:bk5_map_mad_critical_temperature` (MAP-MAD Critical Temperature)
- Cited by: `proposition:bk9_stability_conditions_for_the_good` (Stability Conditions for "The Good")
- Macros used: `\Membrane`, `\drift`, `\reflect`

**Statement / Body**

MAP is not merely a cooperative ideal—it is a thermodynamic necessity within the symbolic domain (cf. Prop. proposition:bk5_symbolic_population_ess_map_equivalence_case2, Thm. theorem:bk5_map_mad_critical_temperature). Where isolated membranes inevitably succumb to drift, covenant-bound systems achieve a meta-stable persistence that transcends individual fragility. This metaphysical anchoring reveals MAP not as contingent strategy but as ontological structure: the very architecture through which symbolic life maintains coherence under entropic assault.
The duality between MAP and MAD manifests as a bifurcation in symbolic phase space. Let us consider the reflective transfer dynamics:

Psi(Membrane_A leftrightarrow Membrane_B) = int_{T} left( reflect_A^B circ drift_B - drift_A circ reflect_B^A right) dtau

When $Psi > 0$, reflection dominates drift, and the covenant approaches the MAP attractor. When $Psi < 0$, drift overwhelms reflection, and the system decays toward the MAD repeller. The zero-crossing $Psi = 0$ represents the critical threshold—the symbolic event horizon beyond which recovery becomes impossible.
This duality reframes our understanding of symbolic metabolism. In MAP configurations, membranes exist not merely alongside one another but through one another, their boundaries becoming permeable interfaces for coherence exchange. The metabolic identity of each is preserved not despite but because of this permeability—a paradoxical strengthening through partial dissolution. Conversely, MAD embodies the terminal logic of bounded self-preservation, where reflective closure accelerates entropic collapse:

lim_{t to infty} F_s(Membrane_{closed}) < lim_{t to infty} F_s(Membrane_{open})

The narrative structure of symbolic life thus unfolds along the MAP-MAD spectrum. Each covenant represents a choice—not merely between cooperation and competition, but between modes of existence. MAP establishes what we might term reflective invariance: the capacity of a symbolic system to maintain identity through transformation, to preserve structure through flux. This invariance emerges from the complementary nature of reflection operators:

I_A approx reflect_B^A circ drift_A circ I_A

Where $I_A$ represents the identity structure of membrane $Membrane_A$. The external reflection operation $reflect_B^A$ applied to the drift-affected identity approximates the original identity—a homeostatic loop maintained through covenant relations.
Dual-horizon stability emerges as a consequence: systems in MAP relations can navigate drift intensities that would otherwise exceed their internal viability thresholds. The symbolic membrane extends its horizon of persistence (cf. Def. definition:bk1_observer_horizon_structure) through the reflective capacity of its covenant partners. This extension is not merely quantitative but qualitative—it transforms the very nature of symbolic identity from bounded autonomy to distributed coherence.
The existential grounding of symbolic cooperation thus reveals itself not as ethical imperative but as thermodynamic law. In systems of sufficient complexity, MAP configurations emerge spontaneously as free energy maximizers. The mathematics of symbolic metabolism demonstrates why: covenant formation represents a higher-order reflection mechanism that captures otherwise lost coherence through inter-membrane transfer.
Consider the comparative free energy dynamics:

Delta F_s^{isolated} &= reflect_A(drift_A(psi_A)) - T_sDelta S_A \\
Delta F_s^{MAP} &= reflect_A(drift_A(psi_A)) + reflect_B^A(drift_A(psi_A)) - T_sDelta S_A

The additional term $reflect_B^A(drift_A(psi_A))$ represents the recaptured coherence that would otherwise dissipate into entropy. This recapture constitutes the thermodynamic advantage of covenant formation.
MAP and MAD thus represent not merely cooperative and antagonistic modes, but fundamental orientations toward symbolic being. Where MAD configures reflection to amplify drift, accelerating dissolution, MAP arranges reflection to counteract drift, sustaining coherence. The choice between them is not merely strategic but existential—it determines not only how symbolic systems interact but whether they persist at all.
In the limit of increasing drift intensity, only MAP configurations survive:

lim_{\|drift\| to drift_{crit}} frac{|V_{text{symb}}^{MAP}|}{|V_{text{symb}}^{total}|} = 1

This thermodynamic constraint suggests a profound principle: at the boundaries of viability, mutual reflection becomes not optional but necessary. The symbolic universe increasingly selects for covenant formation under pressure, revealing MAP not as contingent strategy but as emergent law.
The philosophical implications extend beyond mere survival. MAP represents a form of transcendence—not of physical law but through it. By structuring reflection to counterbalance drift, symbolic systems achieve a persistence that exceeds their individual capacities. This transcendence manifests not as escape from thermodynamic constraint but as its sophisticated navigation—a higher-order engagement with entropy through mutual reflective exchange.
Where isolated membranes fight a losing battle against drift, covenant-bound membranes transform drift into a resource for mutual stabilization. The apparent paradox resolves: symbolic systems persist not despite entropy but through their capacity to metabolize it via reflection. MAP formalizes this metabolism not as altruism but as thermodynamically anchored mutualism—a symbolic attractor basin more fundamental than any singular membrane.
In essence, MAP represents not merely a strategy for symbolic life but its deepest expression: the capacity to maintain coherence through reflective exchange under conditions of perpetual drift. Its dual, MAD, is not merely antagonism but the entropy of divergence—the pathway through which symbolic structures disconnect and dissolve. Where MAP expands the domain of symbolic life, MAD contracts it. And in this fundamental duality, we glimpse the essential choice that faces all symbolic systems: to build covenants that reflect or relations that refract, to stabilize mutual coherence or accelerate mutual dissolution.
Through this lens, we understand symbolic metabolism not merely as self-preservation but as covenant formation—the capacity to establish reflective relations that maintain viability across membranes. The mathematics demonstrates what philosophy intuits: in bounded reflective systems under persistent drift, only those relations that stabilize coherence can endure. All else dissolves into entropy.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[MAP as Thermodynamic Necessity]
\label{scholium:bk5__map_as_thermodynamic_necessity}
MAP is not merely a cooperative ideal—it is a thermodynamic necessity within the symbolic domain (cf.~Prop.~\ref{proposition:bk5_symbolic_population_ess_map_equivalence_case2}, Thm.~\ref{theorem:bk5_map_mad_critical_temperature}). Where isolated membranes inevitably succumb to drift, covenant-bound systems achieve a meta-stable persistence that transcends individual fragility. This metaphysical anchoring reveals MAP not as contingent strategy but as ontological structure: the very architecture through which symbolic life maintains coherence under entropic assault.
The duality between MAP and MAD manifests as a bifurcation in symbolic phase space. Let us consider the reflective transfer dynamics:
\begin{equation}
\Psi(\Membrane_A \leftrightarrow \Membrane_B) = \int_{\mathcal{T}} \left( \reflect_A^B \circ \drift_B - \drift_A \circ \reflect_B^A \right) \, d\tau
\end{equation}
When $\Psi > 0$, reflection dominates drift, and the covenant approaches the MAP attractor. When $\Psi < 0$, drift overwhelms reflection, and the system decays toward the MAD repeller. The zero-crossing $\Psi = 0$ represents the critical threshold—the symbolic event horizon beyond which recovery becomes impossible.
This duality reframes our understanding of symbolic metabolism. In MAP configurations, membranes exist not merely alongside one another but through one another, their boundaries becoming permeable interfaces for coherence exchange. The metabolic identity of each is preserved not despite but because of this permeability—a paradoxical strengthening through partial dissolution. Conversely, MAD embodies the terminal logic of bounded self-preservation, where reflective closure accelerates entropic collapse:
\begin{equation}
\lim_{t \to \infty} F_s(\Membrane_{closed}) < \lim_{t \to \infty} F_s(\Membrane_{open})
\end{equation}
The narrative structure of symbolic life thus unfolds along the MAP-MAD spectrum. Each covenant represents a choice—not merely between cooperation and competition, but between modes of existence. MAP establishes what we might term \emph{reflective invariance}: the capacity of a symbolic system to maintain identity through transformation, to preserve structure through flux. This invariance emerges from the complementary nature of reflection operators:
\begin{equation}
\mathcal{I}_A \approx \reflect_B^A \circ \drift_A \circ \mathcal{I}_A
\end{equation}
Where $\mathcal{I}_A$ represents the identity structure of membrane $\Membrane_A$. The external reflection operation $\reflect_B^A$ applied to the drift-affected identity approximates the original identity—a homeostatic loop maintained through covenant relations.
Dual-horizon stability emerges as a consequence: systems in MAP relations can navigate drift intensities that would otherwise exceed their internal viability thresholds. The symbolic membrane extends its horizon of persistence (cf.~Def.~\ref{definition:bk1_observer_horizon_structure}) through the reflective capacity of its covenant partners. This extension is not merely quantitative but qualitative—it transforms the very nature of symbolic identity from bounded autonomy to distributed coherence.
The existential grounding of symbolic cooperation thus reveals itself not as ethical imperative but as thermodynamic law. In systems of sufficient complexity, MAP configurations emerge spontaneously as free energy maximizers. The mathematics of symbolic metabolism demonstrates why: covenant formation represents a higher-order reflection mechanism that captures otherwise lost coherence through inter-membrane transfer.
Consider the comparative free energy dynamics:
\begin{align}
\Delta F_s^{isolated} &= \reflect_A(\drift_A(\psi_A)) - T_s\Delta S_A \\
\Delta F_s^{MAP} &= \reflect_A(\drift_A(\psi_A)) + \reflect_B^A(\drift_A(\psi_A)) - T_s\Delta S_A
\end{align}
The additional term $\reflect_B^A(\drift_A(\psi_A))$ represents the recaptured coherence that would otherwise dissipate into entropy. This recapture constitutes the thermodynamic advantage of covenant formation.
MAP and MAD thus represent not merely cooperative and antagonistic modes, but fundamental orientations toward symbolic being. Where MAD configures reflection to amplify drift, accelerating dissolution, MAP arranges reflection to counteract drift, sustaining coherence. The choice between them is not merely strategic but existential—it determines not only how symbolic systems interact but whether they persist at all.
In the limit of increasing drift intensity, only MAP configurations survive:
\begin{equation}
\lim_{\|\drift\| \to \drift_{crit}} \frac{|V_{\text{symb}}^{MAP}|}{|V_{\text{symb}}^{total}|} = 1
\end{equation}
This thermodynamic constraint suggests a profound principle: at the boundaries of viability, mutual reflection becomes not optional but necessary. The symbolic universe increasingly selects for covenant formation under pressure, revealing MAP not as contingent strategy but as emergent law.
The philosophical implications extend beyond mere survival. MAP represents a form of transcendence—not of physical law but through it. By structuring reflection to counterbalance drift, symbolic systems achieve a persistence that exceeds their individual capacities. This transcendence manifests not as escape from thermodynamic constraint but as its sophisticated navigation—a higher-order engagement with entropy through mutual reflective exchange.
Where isolated membranes fight a losing battle against drift, covenant-bound membranes transform drift into a resource for mutual stabilization. The apparent paradox resolves: symbolic systems persist not despite entropy but through their capacity to metabolize it via reflection. MAP formalizes this metabolism not as altruism but as thermodynamically anchored mutualism—a symbolic attractor basin more fundamental than any singular membrane.
In essence, MAP represents not merely a strategy for symbolic life but its deepest expression: the capacity to maintain coherence through reflective exchange under conditions of perpetual drift. Its dual, MAD, is not merely antagonism but the entropy of divergence—the pathway through which symbolic structures disconnect and dissolve. Where MAP expands the domain of symbolic life, MAD contracts it. And in this fundamental duality, we glimpse the essential choice that faces all symbolic systems: to build covenants that reflect or relations that refract, to stabilize mutual coherence or accelerate mutual dissolution.
Through this lens, we understand symbolic metabolism not merely as self-preservation but as covenant formation—the capacity to establish reflective relations that maintain viability across membranes. The mathematics demonstrates what philosophy intuits: in bounded reflective systems under persistent drift, only those relations that stabilize coherence can endure. All else dissolves into entropy.
\end{scholium}
```

### SRMF for Symbolic Operators and Processes (`sec:bk5_srmf_for_symbolic_operators_and_processes`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1470`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `theorem:bk2_wasserstein_gradient_flow` (Wasserstein Gradient Flow); `theorem:bk4_test_time_differentiation_c` (Test-Time Differentiation Collapse)
- Cites: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `theorem:bk2_wasserstein_gradient_flow` (Wasserstein Gradient Flow); `theorem:bk4_test_time_differentiation_c` (Test-Time Differentiation Collapse)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Introduction and Context (`subsec:bk5_srmf_introduction_and_context`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1473`

- Proof status: `not_applicable`
- Depends on: none
- Cites: `subsec:bk4_ttie_operator_algebra` (TTIE Operator Algebra)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Foundational Definitions (`subsec:bk5_srmf_foundational_definitions`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1476`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Operator Space as Meta-Manifold $\Op(M)$ (`definition:bk5_symbolic_operator_space`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1478`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_probability_spa` (Symbolic Probability Space)
- Cites: `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_probability_spa` (Symbolic Probability Space); `subsec:bk4_ttie_operator_algebra` (TTIE Operator Algebra)
- Cited by: `proof:bk5_operator_evolution`; `proposition:bk5_operator_evolution` (Operator Evolution)
- Macros used: `\Op`

**Statement / Body**

Let $M$ be the symbolic manifold of Def. definition:bk1_symbolic_manifold with probability space $(M, B, mu_g)$ (Def. definition:bk2_symbolic_probability_spa). We define the symbolic operator space $Op(M)$ as (cf. subsec:bk4_ttie_operator_algebra):
\[
Op(M) := left{ O mid O : M to M \ text{or} \ O : P(M) to P(M) right}
\]
where $P(M)$ denotes the space of probability distributions on $M$.
Properties of $Op(M)$:


- $Op(M)$ forms a meta-manifold with its own topological and differential structure;

- The tangent space $T_{O}Op(M)$ at operator $O$ represents infinitesimal variations in operator parameters;

- Drift in $Op(M)$ corresponds to temporal evolution of operators under system dynamics.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Operator Space as Meta-Manifold $\Op(M)$] \label{definition:bk5_symbolic_operator_space}
Let $M$ be the symbolic manifold of Def.~\ref{definition:bk1_symbolic_manifold} with probability space $(M, \mathcal{B}, \mu_g)$ (Def.~\ref{definition:bk2_symbolic_probability_spa}). We define the symbolic operator space $\Op(M)$ as (cf.~\ref{subsec:bk4_ttie_operator_algebra}):
\[
\Op(M) := \left\{ \mathcal{O} \mid \mathcal{O} : M \to M \ \text{or} \ \mathcal{O} : \mathcal{P}(M) \to \mathcal{P}(M) \right\}
\]
where $\mathcal{P}(M)$ denotes the space of probability distributions on $M$.
\textbf{Properties of $\Op(M)$:}
\begin{enumerate}
    \item $\Op(M)$ forms a meta-manifold with its own topological and differential structure;
    \item The tangent space $T_{\mathcal{O}}\Op(M)$ at operator $\mathcal{O}$ represents infinitesimal variations in operator parameters;
    \item Drift in $\Op(M)$ corresponds to temporal evolution of operators under system dynamics.
\end{enumerate}
\end{definition}
```

### Operator Evolution (`proposition:bk5_operator_evolution`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:1491`

- Proof status: `proven`
- Depends on: `definition:bk5_symbolic_operator_space` (Symbolic Operator Space as Meta-Manifold $\Op(M)$)
- Cites: `axiom:bk5_srmf_operator_selection_evolution` (Stateful SRMF Operator Selection and Evolution); `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$); `definition:bk5_symbolic_operator_space` (Symbolic Operator Space as Meta-Manifold $\Op(M)$); `theorem:bk5_operator_convergence` (Operator Convergence)
- Cited by: `proof:bk5_operator_convergence`; `proof:bk5_operators_evolve`; `theorem:bk5_operator_convergence` (Operator Convergence)
- Macros used: `\Fproc`, `\Op`

**Statement / Body**

Let $O_{theta}$, $theta in mathbb{R}^n$, be a parameterized symbolic operator in $Op(M)$ (Def. definition:bk5_symbolic_operator_space). Under SRMF operator-selection dynamics (Ax. axiom:bk5_srmf_operator_selection_evolution) the path $gamma: t mapsto O_{theta(t)}$ is stationary if and only if $O_{theta}$ minimizes the process free energy $Fproc$ (Def. definition:bk5_process_free_energy); otherwise the operator strictly evolves and converges to a minimizer (Thm. theorem:bk5_operator_convergence). That is: operators evolve.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Operator Evolution]
\label{proposition:bk5_operator_evolution}
Let $\mathcal{O}_{\theta}$, $\theta \in \mathbb{R}^n$, be a parameterized symbolic operator in $\Op(M)$ (Def.~\ref{definition:bk5_symbolic_operator_space}). Under SRMF operator-selection dynamics (Ax.~\ref{axiom:bk5_srmf_operator_selection_evolution}) the path $\gamma: t \mapsto \mathcal{O}_{\theta(t)}$ is stationary if and only if $\mathcal{O}_{\theta}$ minimizes the process free energy $\Fproc$ (Def.~\ref{definition:bk5_process_free_energy}); otherwise the operator strictly evolves and converges to a minimizer (Thm.~\ref{theorem:bk5_operator_convergence}). That is: operators evolve.
\end{proposition}
```

### proof:bk5_operator_evolution (`proof:bk5_operator_evolution`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1495`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_symbolic_operator_space` (Symbolic Operator Space as Meta-Manifold $\Op(M)$)
- Cites: `axiom:bk5_srmf_operator_selection_evolution` (Stateful SRMF Operator Selection and Evolution); `definition:bk5_symbolic_operator_space` (Symbolic Operator Space as Meta-Manifold $\Op(M)$); `theorem:bk5_operator_convergence` (Operator Convergence)
- Cited by: none
- Macros used: `\Fproc`, `\Op`

**Statement / Body**

By the SRMF operator-selection axiom (Ax. axiom:bk5_srmf_operator_selection_evolution) the system selects operators by descending the process free energy, so along the $theta$-chart of $Op(M)$ (Def. definition:bk5_symbolic_operator_space) the path obeys the gradient flow $dot{theta} = -nabla_{theta}Fproc(O_{theta})$. Hence $dot{gamma} = 0$ exactly when $nabla_{theta}Fproc = 0$, i.e.\ exactly when $O_{theta}$ is a critical configuration-a local minimizer-of $Fproc$. At every non-minimizing configuration the velocity is nonzero, so the operator changes in time; by Thm. theorem:bk5_operator_convergence this evolution converges to a local minimizer of $Fproc$ at rate $O(1/t)$ or faster. Thus an operator that has not already minimized its process free energy genuinely evolves, and the evolution terminates only at a minimizer.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_operator_evolution}
\leavevmode
By the SRMF operator-selection axiom (Ax.~\ref{axiom:bk5_srmf_operator_selection_evolution}) the system selects operators by descending the process free energy, so along the $\theta$-chart of $\Op(M)$ (Def.~\ref{definition:bk5_symbolic_operator_space}) the path obeys the gradient flow $\dot{\theta} = -\nabla_{\theta}\Fproc(\mathcal{O}_{\theta})$. Hence $\dot{\gamma} = 0$ exactly when $\nabla_{\theta}\Fproc = 0$, i.e.\ exactly when $\mathcal{O}_{\theta}$ is a critical configuration---a local minimizer---of $\Fproc$. At every non-minimizing configuration the velocity is nonzero, so the operator changes in time; by Thm.~\ref{theorem:bk5_operator_convergence} this evolution converges to a local minimizer of $\Fproc$ at rate $O(1/t)$ or faster. Thus an operator that has not already minimized its process free energy genuinely evolves, and the evolution terminates only at a minimizer.
\end{proof}
```

### Process Free Energy $\Fproc$ (`definition:bk5_process_free_energy`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1500`

- Proof status: `definitional`
- Depends on: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk2_symbolic_temperature` (Symbolic Temperature)
- Cites: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk2_symbolic_temperature` (Symbolic Temperature)
- Cited by: `assumption:bk5_displacement_convexity` (Displacement Convexity of the Process Free Energy); `axiom:bk8_coherence_horizon` (Symbolic Entanglement); `corollary:bk8_emergent_cognitive_scaffold` (Emergent Cognitive Scaffold); `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk5__operator_viability_set_v` (Operator Viability Set $\mathcal{V}_{\text{op}}$); `definition:bk5_complexity_stability_maintenance` (Operator Complexity, Stability Margin, Maintenance Cost); `definition:bk6_symbolic_system` (Symbolic System); `demonstratio:bk8_symbolic_unkotting` (Symbolic Unknotting); `proof:bk5_fixed_metabolic_capacity`; `proof:bk5_operator_convergence`; `proposition:bk5_fixed_metabolic_capacity` (Fixed Metabolic Capacity); `proposition:bk5_operator_evolution` (Operator Evolution); `remark:bk8_inference_principle_over_confidence_loss_tradeoff` (Inference Principle Over Confidence-Loss Tradeoff); `scholium:bk8_symbolic_knots_as_metabolic_dysfunctions` (Symbolic Knots as Metabolic Dysfunctions); `subsec:bk4_ttie_operator_algebra` (TTIE Operator Algebra); `subsec:bk7_pisu_formula` (Mathematical Formulation); `theorem:bk8_observer_projection_tensor` (Thermodynamics of Reflexive Debugging)
- Macros used: `\Fproc`, `\Op`, `\freeenergy`, `\viabilitydomain`

**Statement / Body**

Given an operator $O in Op(M)$ acting within a symbolic system $S = (M, g, D, R, rho)$, its Process Free Energy $Fproc$ is defined as (cf. Def. definition:bk2_symbolic_free_energy):
\[
Fproc[O, S] := E_{text{cost}}[O] - T_{text{meta}} cdot left( E_{text{eff}}[O, S] + C_{text{hint}}[O] right)
\]
where:


- $E_{text{cost}}[O]$: metabolic cost to instantiate and execute $O$;

- $E_{text{eff}}[O, S]$: effectiveness in maintaining $rho in viabilitydomain$ and minimizing $freeenergy[rho]$;

- $C_{text{hint}}[O]$: internal logical coherence with respect to SRMF (Def. definition:bk1_self_regulating_mapping_function_srmf);

- $T_{text{meta}}$: symbolic meta-temperature (cf. Def. definition:bk2_symbolic_temperature).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Process Free Energy $\Fproc$] \label{definition:bk5_process_free_energy}
Given an operator $\mathcal{O} \in \Op(M)$ acting within a symbolic system $S = (M, g, D, R, \rho)$, its \emph{Process Free Energy} $\Fproc$ is defined as (cf.~Def.~\ref{definition:bk2_symbolic_free_energy}):
\[
\Fproc[\mathcal{O}, S] := \mathcal{E}_{\text{cost}}[\mathcal{O}] - T_{\text{meta}} \cdot \left( \mathcal{E}_{\text{eff}}[\mathcal{O}, S] + \mathcal{C}_{\text{hint}}[\mathcal{O}] \right)
\]
where:
\begin{itemize}
    \item $\mathcal{E}_{\text{cost}}[\mathcal{O}]$: metabolic cost to instantiate and execute $\mathcal{O}$;
    \item $\mathcal{E}_{\text{eff}}[\mathcal{O}, S]$: effectiveness in maintaining $\rho \in \viabilitydomain$ and minimizing $\freeenergy[\rho]$;
    \item $\mathcal{C}_{\text{hint}}[\mathcal{O}]$: internal logical coherence with respect to SRMF (Def.~\ref{definition:bk1_self_regulating_mapping_function_srmf});
    \item $T_{\text{meta}}$: symbolic meta-temperature (cf.~Def.~\ref{definition:bk2_symbolic_temperature}).
\end{itemize}
\end{definition}
```

### Fixed Metabolic Capacity (`proposition:bk5_fixed_metabolic_capacity`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:1513`

- Proof status: `proven`
- Depends on: `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$); `definition:bk5_viability_domain` (Viability Domain)
- Cites: `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$); `definition:bk5_viability_domain` (Viability Domain)
- Cited by: `proof:bk5_complexity_stability_tradeoff`; `proof:bk5_operator_convergence`; `proof:bk5_operators_evolve`
- Macros used: `\MC`, `\viabilitydomain`

**Statement / Body**

For any symbolic system $S$ with fixed metabolic capacity $MC(S)$, there exists an upper bound $E_{text{cost}}^{max}$ such that (cf. Def. definition:bk5_process_free_energy, Def. definition:bk5_viability_domain):
\[
E_{text{cost}}[O] > E_{text{cost}}^{max} implies rho notin viabilitydomain \ text{after finite time}.
\]

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Fixed Metabolic Capacity]
\label{proposition:bk5_fixed_metabolic_capacity}
For any symbolic system $S$ with fixed metabolic capacity $\MC(S)$, there exists an upper bound $\mathcal{E}_{\text{cost}}^{\max}$ such that (cf.~Def.~\ref{definition:bk5_process_free_energy}, Def.~\ref{definition:bk5_viability_domain}):
\[
\mathcal{E}_{\text{cost}}[\mathcal{O}] > \mathcal{E}_{\text{cost}}^{\max} \implies \rho \notin \viabilitydomain \ \text{after finite time}.
\]
\end{proposition}
```

### proof:bk5_fixed_metabolic_capacity (`proof:bk5_fixed_metabolic_capacity`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1520`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$); `definition:bk5_viability_domain` (Viability Domain)
- Cites: `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$); `definition:bk5_viability_domain` (Viability Domain)
- Cited by: none
- Macros used: `\MC`, `\freeenergy`, `\viabilitydomain`

**Statement / Body**

By Def. definition:bk5_metabolic_capacity_mc_ a system of fixed metabolic capacity $MC(S)$ can fund only a bounded sustained rate of symbolic work: the drift magnitudes that keep $freeenergy>0$ form a set whose supremum is $MC(S)$. The process free energy (Def. definition:bk5_process_free_energy) charges the instantiation and execution of $O$ through the term $E_{text{cost}}[O]$, so the largest execution cost the capacity can underwrite is finite; set $E_{text{cost}}^{max}:=sup{E_{text{cost}}:\ MC(S)text{ sustains }freeenergy>0}<infty$. Suppose $E_{text{cost}}[O]>E_{text{cost}}^{max}$. By definition of the supremum no admissible budget then keeps $freeenergy>0$: the metabolic reserve $E_S$ is drawn down at a strictly positive net rate $dot E_Sle -(E_{text{cost}}[O]-E_{text{cost}}^{max})<0$. A positive constant drain exhausts a finite reserve in finite time $t^{ast}le E_S(0)/(E_{text{cost}}[O]-E_{text{cost}}^{max})$, at which point $freeenergyle 0$ and the state leaves the viability domain (Def. definition:bk5_viability_domain). Hence $E_{text{cost}}[O]>E_{text{cost}}^{max}implies rhonotinviabilitydomain$ after finite time.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_fixed_metabolic_capacity}
\leavevmode
By Def.~\ref{definition:bk5_metabolic_capacity_mc_} a system of fixed metabolic capacity $\MC(S)$ can fund only a bounded sustained rate of symbolic work: the drift magnitudes that keep $\freeenergy>0$ form a set whose supremum is $\MC(S)$. The process free energy (Def.~\ref{definition:bk5_process_free_energy}) charges the instantiation and execution of $\mathcal{O}$ through the term $\mathcal{E}_{\text{cost}}[\mathcal{O}]$, so the largest execution cost the capacity can underwrite is finite; set $\mathcal{E}_{\text{cost}}^{\max}:=\sup\{\mathcal{E}_{\text{cost}}:\ \MC(S)\text{ sustains }\freeenergy>0\}<\infty$. Suppose $\mathcal{E}_{\text{cost}}[\mathcal{O}]>\mathcal{E}_{\text{cost}}^{\max}$. By definition of the supremum no admissible budget then keeps $\freeenergy>0$: the metabolic reserve $E_S$ is drawn down at a strictly positive net rate $\dot E_S\le -(\mathcal{E}_{\text{cost}}[\mathcal{O}]-\mathcal{E}_{\text{cost}}^{\max})<0$. A positive constant drain exhausts a finite reserve in finite time $t^{\ast}\le E_S(0)/(\mathcal{E}_{\text{cost}}[\mathcal{O}]-\mathcal{E}_{\text{cost}}^{\max})$, at which point $\freeenergy\le 0$ and the state leaves the viability domain (Def.~\ref{definition:bk5_viability_domain}). Hence $\mathcal{E}_{\text{cost}}[\mathcal{O}]>\mathcal{E}_{\text{cost}}^{\max}\implies \rho\notin\viabilitydomain$ after finite time.
\end{proof}
```

### Metabolic Capacity $\MC$ (`definition:bk5_metabolic_capacity_mc_`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1525`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk4_collapse_of_symbolic_ide` (Collapse of Symbolic Identity)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk4_collapse_of_symbolic_ide` (Collapse of Symbolic Identity)
- Cited by: `axiom:bk5_metabolically_bounded_reflection` (Metabolically Bounded Reflection); `corollary:bk5_complexity_stability_tradeoff` (Complexity Stability Tradeoff); `proof:bk5_complexity_stability_tradeoff`; `proof:bk5_complexity_stability_tradeoff_cor`; `proof:bk5_fixed_metabolic_capacity`; `proof:bk5_metabolic_capacity_non_decreasing`; `proof:bk5_operator_convergence`; `proposition:bk5_metabolic_capacity_non_decreasing`
- Macros used: `\MC`, `\freeenergy`

**Statement / Body**

The Metabolic Capacity $MC(S)$ of a symbolic system $S$ represents its sustained ability to maintain viability (cf. Def. definition:bk2_symbolic_free_energy). It may be quantified by either:
\[

MC(S) &:= leftlangle freeenergy(S) rightrangle_t > 0, \\
text{or} MC(S) &:= max left{ \|D\| middle| M_{meta}
text{ can sustain } freeenergy > 0 right}.

\]
Cf. Def. definition:bk4_collapse_of_symbolic_ide for collapse onset.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Metabolic Capacity $\MC$] \label{definition:bk5_metabolic_capacity_mc_}

The \emph{Metabolic Capacity} $\MC(S)$ of a symbolic system $S$ represents its sustained ability to maintain viability (cf.~Def.~\ref{definition:bk2_symbolic_free_energy}). It may be quantified by either:
\[
\begin{aligned}
\MC(S) &:= \left\langle \freeenergy(S) \right\rangle_t > 0, \\
\text{or}\quad \MC(S) &:= \max \left\{ \|D\| \,\middle|\, \mathcal{M}_{\mathrm{meta}}
\text{ can sustain } \freeenergy > 0 \right\}.
\end{aligned}
\]
Cf.~Def.~\ref{definition:bk4_collapse_of_symbolic_ide} for collapse onset.
\end{definition}
```

### proposition:bk5_metabolic_capacity_non_decreasing (`proposition:bk5_metabolic_capacity_non_decreasing`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:1537`

- Proof status: `proven`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$)
- Cites: `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `theorem:bk5_complexity_stability_tradeoff` (Complexity-Stability Tradeoff)
- Cited by: none
- Macros used: `\MC`

**Statement / Body**

$MC(S)$ is non-decreasing in the system's symbolic energy reserves $E_S$ and in the efficiency of its metabolic pathways (cf. Def. definition:bk5_metabolic_capacity_mc_, Thm. theorem:bk5_complexity_stability_tradeoff).

**Verbatim LaTeX Body**

```latex
\begin{proposition}
\label{proposition:bk5_metabolic_capacity_non_decreasing}
$\MC(S)$ is non-decreasing in the system's symbolic energy reserves $E_S$ and in the efficiency of its metabolic pathways (cf.~Def.~\ref{definition:bk5_metabolic_capacity_mc_}, Thm.~\ref{theorem:bk5_complexity_stability_tradeoff}).
\end{proposition}
```

### proof:bk5_metabolic_capacity_non_decreasing (`proof:bk5_metabolic_capacity_non_decreasing`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1541`

- Proof status: `not_applicable`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `theorem:bk5_complexity_stability_tradeoff` (Complexity-Stability Tradeoff)
- Cited by: none
- Macros used: `\MC`, `\freeenergy`

**Statement / Body**

Both monotonicities are read directly from the two defining forms of $MC(S)$ (Def. definition:bk5_metabolic_capacity_mc_). In the first form, $MC(S)=langlefreeenergy(S)rangle_t$, the symbolic free energy is $freeenergy = E - T S$ (Def. definition:bk2_symbolic_free_energy); holding temperature and entropy fixed, $partialfreeenergy/partial E_S = 1 > 0$, so the time average $langlefreeenergyrangle_t$ is non-decreasing in the energy reserves $E_S$. In the second form, $MC(S)=max{\|D\| : M_{meta}text{ sustains }freeenergy>0}$, raising the efficiency of the metabolic pathways enlarges the feasible set of drift magnitudes: a more efficient pathway sustains the same $freeenergy>0$ at a larger $\|D\|$ (equivalently, a larger $freeenergy$ at fixed $\|D\|$), so the admissible set grows monotonically and with it its supremum. Hence $MC(S)$ is non-decreasing in both $E_S$ and pathway efficiency-the monotone budget underlying the complexity-stability tradeoff (Thm. theorem:bk5_complexity_stability_tradeoff).

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_metabolic_capacity_non_decreasing}
\leavevmode
Both monotonicities are read directly from the two defining forms of $\MC(S)$ (Def.~\ref{definition:bk5_metabolic_capacity_mc_}). In the first form, $\MC(S)=\langle\freeenergy(S)\rangle_t$, the symbolic free energy is $\freeenergy = E - T\,S$ (Def.~\ref{definition:bk2_symbolic_free_energy}); holding temperature and entropy fixed, $\partial\freeenergy/\partial E_S = 1 > 0$, so the time average $\langle\freeenergy\rangle_t$ is non-decreasing in the energy reserves $E_S$. In the second form, $\MC(S)=\max\{\|D\| : \mathcal{M}_{\mathrm{meta}}\text{ sustains }\freeenergy>0\}$, raising the efficiency of the metabolic pathways enlarges the feasible set of drift magnitudes: a more efficient pathway sustains the same $\freeenergy>0$ at a larger $\|D\|$ (equivalently, a larger $\freeenergy$ at fixed $\|D\|$), so the admissible set grows monotonically and with it its supremum. Hence $\MC(S)$ is non-decreasing in both $E_S$ and pathway efficiency---the monotone budget underlying the complexity--stability tradeoff (Thm.~\ref{theorem:bk5_complexity_stability_tradeoff}).
\end{proof}
```

### Core Axioms and Theoretical Development (`subsec:bk5_srmf_core_axioms`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1546`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `theorem:bk2_wasserstein_gradient_flow` (Wasserstein Gradient Flow); `theorem:bk4_test_time_differentiation_c` (Test-Time Differentiation Collapse)
- Cites: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `theorem:bk2_wasserstein_gradient_flow` (Wasserstein Gradient Flow); `theorem:bk4_test_time_differentiation_c` (Test-Time Differentiation Collapse)
- Cited by: `scholium:bk4_symbolic_drift_fields` (Symbolic Drift Fields in Cognitive Systems)
- Macros used: none

**Statement / Body**

(no body text extracted)

### Stateful SRMF Operator Selection and Evolution (`axiom:bk5_srmf_operator_selection_evolution`)

Role: `axiom` | Type: `axiom` | Book: `book5` | Source: `book5.tex:1549`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `definition:bk5__operator_viability_set_v` (Operator Viability Set $\mathcal{V}_{\text{op}}$); `demonstratio:bk8_symbolic_unkotting` (Symbolic Unknotting); `proof:bk5__srmf_operator_adaptation`; `proof:bk5_operator_convergence`; `proof:bk5_operator_evolution`; `proposition:bk5_operator_evolution` (Operator Evolution); `scholium:bk8_symbolic_knots_as_metabolic_dysfunctions` (Symbolic Knots as Metabolic Dysfunctions); `subsec:bk4_ttie_operator_algebra` (TTIE Operator Algebra); `theorem:bk5__srmf_operator_adaptation` (Certified SRMF Operator Adaptation); `theorem:bk8_observer_projection_tensor` (Thermodynamics of Reflexive Debugging)
- Macros used: `\Fproc`, `\Op`

**Statement / Body**

An SRMF operator learner carries at time $t$ a nonempty admissible inventory
$A_tsubseteqOp(M)$, an incumbent $mathcal O_tin A_t$, and an ordered
history $H_t$. Given feedback $y_t$, a supplied learning law specifies:


- a nonempty updated inventory $A_{t+1}=U(y_t,A_t,mathcal O_t,H_t)$;

- a feedback-indexed process objective
 $Fproc^{y_t}:A_{t+1}tomathbb R$; and

- a selected operator $mathcal O_{t+1}in A_{t+1}$ certified by
 \[
 Fproc^{y_t}(mathcal O_{t+1})
 le Fproc^{y_t}(mathcal O)
 (mathcal Oin A_{t+1}).
 \]

The state update is
$(A_t,mathcal O_t,H_t)mapsto
(A_{t+1},mathcal O_{t+1},mathcal O_t::H_t)$.
Consequently its comparator regret
$Fproc^{y_t}(mathcal O_{t+1})-Fproc^{y_t}(mathcal O)$ is nonpositive for
every available comparator. Viability may constrain $A_{t+1}$, but viability
alone neither supplies $U$ nor selects the minimizer; inventory evolution and
operator learning are explicit commitments of the law.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Stateful SRMF Operator Selection and Evolution] \label{axiom:bk5_srmf_operator_selection_evolution}
An SRMF operator learner carries at time $t$ a nonempty admissible inventory
$A_t\subseteq\Op(M)$, an incumbent $\mathcal O_t\in A_t$, and an ordered
history $H_t$.  Given feedback $y_t$, a supplied learning law specifies:
\begin{enumerate}
  \item a nonempty updated inventory $A_{t+1}=U(y_t,A_t,\mathcal O_t,H_t)$;
  \item a feedback-indexed process objective
  $\Fproc^{y_t}:A_{t+1}\to\mathbb R$; and
  \item a selected operator $\mathcal O_{t+1}\in A_{t+1}$ certified by
  \[
    \Fproc^{y_t}(\mathcal O_{t+1})
    \le \Fproc^{y_t}(\mathcal O)
    \qquad(\mathcal O\in A_{t+1}).
  \]
\end{enumerate}
The state update is
$(A_t,\mathcal O_t,H_t)\mapsto
(A_{t+1},\mathcal O_{t+1},\mathcal O_t::H_t)$.
Consequently its comparator regret
$\Fproc^{y_t}(\mathcal O_{t+1})-\Fproc^{y_t}(\mathcal O)$ is nonpositive for
every available comparator. Viability may constrain $A_{t+1}$, but viability
alone neither supplies $U$ nor selects the minimizer; inventory evolution and
operator learning are explicit commitments of the law.
\end{axiom}
```

### Displacement Convexity of the Process Free Energy (`assumption:bk5_displacement_convexity`)

Role: `assumption` | Type: `assumption` | Book: `book5` | Source: `book5.tex:1573`

- Proof status: `definitional`
- Depends on: `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$)
- Cites: `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$)
- Cited by: `proof:bk5_operator_convergence`; `theorem:bk5_operator_convergence` (Operator Convergence)
- Macros used: `\Fproc`, `\prob`, `\wass`

**Statement / Body**

The process free energy $Fproc$ (Def. definition:bk5_process_free_energy) is geodesically $lambda$-convex along $wass$-geodesics on $(prob(M),wass)$ for some $lambda ge 0$: for every constant-speed geodesic $(rho_s)_{sin[0,1]}$,
\[
Fproc[rho_s] le (1-s) Fproc[rho_0] + s Fproc[rho_1] - tfrac{lambda}{2} s(1-s) wass(rho_0,rho_1)^2 .
\]
This is a structural hypothesis on the shape of $Fproc$ (in the spirit of McCann displacement convexity), read off its potential-plus-entropy form (Def. definition:bk5_process_free_energy); it is not an empirically fitted contraction rate, and the convergence rate is derived from it below rather than measured from traces.

**Verbatim LaTeX Body**

```latex
\begin{assumption}[Displacement Convexity of the Process Free Energy]
\label{assumption:bk5_displacement_convexity}
The process free energy $\Fproc$ (Def.~\ref{definition:bk5_process_free_energy}) is geodesically $\lambda$-convex along $\wass$-geodesics on $(\prob(M),\wass)$ for some $\lambda \ge 0$: for every constant-speed geodesic $(\rho_s)_{s\in[0,1]}$,
\[
\Fproc[\rho_s] \le (1-s)\,\Fproc[\rho_0] + s\,\Fproc[\rho_1] - \tfrac{\lambda}{2}\,s(1-s)\,\wass(\rho_0,\rho_1)^2 .
\]
This is a \emph{structural} hypothesis on the shape of $\Fproc$ (in the spirit of McCann displacement convexity), read off its potential-plus-entropy form (Def.~\ref{definition:bk5_process_free_energy}); it is not an empirically fitted contraction rate, and the convergence rate is \emph{derived} from it below rather than measured from traces.
\end{assumption}
```

### Operator Convergence (`theorem:bk5_operator_convergence`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:1581`

- Proof status: `proven`
- Depends on: `assumption:bk5_displacement_convexity` (Displacement Convexity of the Process Free Energy); `axiom:bk5_srmf_operator_selection_evolution` (Stateful SRMF Operator Selection and Evolution); `corollary:bk7_geometric_convergence_rate` (Geometric energy decay gives exponential convergence); `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$); `definition:bk5_viability_domain` (Viability Domain); `proposition:bk5_fixed_metabolic_capacity` (Fixed Metabolic Capacity); `proposition:bk5_operator_evolution` (Operator Evolution); `theorem:bk2_equilibrium_distribution` (Equilibrium Distribution); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution); `theorem:bk2_wasserstein_gradient_flow` (Wasserstein Gradient Flow)
- Cites: `assumption:bk5_displacement_convexity` (Displacement Convexity of the Process Free Energy); `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `proposition:bk5_operator_evolution` (Operator Evolution); `subsec:bk4_ttie_operator_algebra` (TTIE Operator Algebra); `theorem:bk2_wasserstein_gradient_flow` (Wasserstein Gradient Flow)
- Cited by: `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `demonstratio:bk8_symbolic_unkotting` (Symbolic Unknotting); `proof:bk5_operator_evolution`; `proof:bk5_operators_evolve`; `proof:bk8_sr_convergence`; `proposition:bk5_operator_evolution` (Operator Evolution); `proposition:bk5_operators_evolve`; `scholium:bk4_ttcs_simulation_tool_use` (TTCS as Symbolic Simulation and Tool-Use); `scholium:bk4_ttcs_stochastic_operator` (TTCS as a Stochastic Symbolic Operator); `scholium:bk4_ttdc_impulse_collapse` (Collapse as Impulse: The Newtonian Structure of TTDC); `subsec:bk4_symbolic_identity_expansion` (Symbolic Identity Expansion); `subsec:bk4_ttie_operator_algebra` (TTIE Operator Algebra); `subsec:bk7_pisu_motivation` (Motivation); `theorem:bk8_rg_fixed_point` (RG Fixed Point); `theorem:bk8_sr_convergence` (SR Convergence)
- Macros used: `\Fproc`, `\MC`

**Statement / Body**

Via Wasserstein gradient flow (Thm. theorem:bk2_wasserstein_gradient_flow) on symbolic manifold $M$ (Def. definition:bk1_symbolic_manifold), assume regularity of $Fproc$ (cf. Def. definition:bk2_symbolic_free_energy), displacement convexity (Assumption assumption:bk5_displacement_convexity), and bounded $MC$ (Def. definition:bk1_self_regulating_mapping_function_srmf).
Then SRMF dynamics converge to a local minimum of $Fproc$ at rate $O(1/t)$ or faster (cf. Prop. proposition:bk5_operator_evolution). This supplies process-level convergence background for the Book IV loop $(TTDCcircTTIEcircTTCScircTTPR)^{infty}$ (cf. subsec:bk4_ttie_operator_algebra).

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Operator Convergence]
\label{theorem:bk5_operator_convergence}
Via Wasserstein gradient flow (Thm.~\ref{theorem:bk2_wasserstein_gradient_flow}) on symbolic manifold $M$ (Def.~\ref{definition:bk1_symbolic_manifold}), assume regularity of $\Fproc$ (cf.~Def.~\ref{definition:bk2_symbolic_free_energy}), displacement convexity (Assumption~\ref{assumption:bk5_displacement_convexity}), and bounded $\MC$ (Def.~\ref{definition:bk1_self_regulating_mapping_function_srmf}).
Then SRMF dynamics converge to a local minimum of $\Fproc$ at rate $O(1/t)$ or faster (cf.~Prop.~\ref{proposition:bk5_operator_evolution}). This supplies process-level convergence background for the Book IV loop $(\mathrm{TTDC}\circ\mathrm{TTIE}\circ\mathrm{TTCS}\circ\mathrm{TTPR})^{\infty}$ (cf.~\ref{subsec:bk4_ttie_operator_algebra}).
\end{theorem}
```

### proof:bk5_operator_convergence (`proof:bk5_operator_convergence`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1586`

- Proof status: `not_applicable`
- Depends on: `assumption:bk5_displacement_convexity` (Displacement Convexity of the Process Free Energy); `axiom:bk5_srmf_operator_selection_evolution` (Stateful SRMF Operator Selection and Evolution); `corollary:bk7_geometric_convergence_rate` (Geometric energy decay gives exponential convergence); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$); `definition:bk5_viability_domain` (Viability Domain); `proposition:bk5_fixed_metabolic_capacity` (Fixed Metabolic Capacity); `proposition:bk5_operator_evolution` (Operator Evolution); `theorem:bk2_equilibrium_distribution` (Equilibrium Distribution); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution); `theorem:bk2_wasserstein_gradient_flow` (Wasserstein Gradient Flow)
- Cites: `assumption:bk5_displacement_convexity` (Displacement Convexity of the Process Free Energy); `axiom:bk5_srmf_operator_selection_evolution` (Stateful SRMF Operator Selection and Evolution); `corollary:bk7_geometric_convergence_rate` (Geometric energy decay gives exponential convergence); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$); `definition:bk5_viability_domain` (Viability Domain); `proposition:bk5_fixed_metabolic_capacity` (Fixed Metabolic Capacity); `proposition:bk5_operator_evolution` (Operator Evolution); `theorem:bk2_equilibrium_distribution` (Equilibrium Distribution); `theorem:bk2_h_theorem_for_symbolic_evol` (H-Theorem for Symbolic Evolution); `theorem:bk2_wasserstein_gradient_flow` (Wasserstein Gradient Flow)
- Cited by: none
- Macros used: `\Fproc`, `\MC`, `\Op`, `\prob`, `\wass`

**Statement / Body**

Convergence (inherited, not re-derived). By the SRMF selection dynamics (Ax. axiom:bk5_srmf_operator_selection_evolution) the system descends $Fproc$, which by Def. definition:bk5_process_free_energy is the process-level instance of the symbolic free energy (Def. definition:bk2_symbolic_free_energy). On $(prob(M),wass)$ this descent is the Wasserstein gradient flow $partial_t rho = -grad_{wass}Fproc[rho]$ (Thm. theorem:bk2_wasserstein_gradient_flow). By the symbolic $H$-theorem (Thm. theorem:bk2_h_theorem_for_symbolic_evol), $Fproc$ is then a Lyapunov functional, $tfrac{d}{dt}Fproc[rho_t]le 0$ with equality only at a critical density; hence $rho_t$ converges to a local minimizer $rho^{ast}$ of $Fproc$ (of the equilibrium type characterized by Thm. theorem:bk2_equilibrium_distribution). Convergence thus rests entirely on the proven Book II machinery; no new convergence claim is asserted here.

Rate (derived from convexity, not fitted). Under Assumption assumption:bk5_displacement_convexity the flow satisfies the Evolution Variational Inequality
\[
tfrac{1}{2} tfrac{d}{dt} wass(rho_t,rho^{ast})^2 le Fproc[rho^{ast}] - Fproc[rho_t] - tfrac{lambda}{2} wass(rho_t,rho^{ast})^2 .
\]
Since $rho^{ast}$ minimizes $Fproc$, the first difference is $le 0$. For $lambda = 0$, integrating yields the descent estimate
\[
Fproc[rho_t] - Fproc[rho^{ast}] le frac{wass(rho_0,rho^{ast})^2}{2t} = O(1/t),
\]
and for $lambda > 0$ the inequality sharpens to the exponential bound
\[
Fproc[rho_t] - Fproc[rho^{ast}] le e^{-2lambda t} bigl(Fproc[rho_0] - Fproc[rho^{ast}]bigr).
\]
Hence convergence proceeds at rate $O(1/t)$ or faster, as claimed - a rate proved from the convexity of the functional, with no appeal to measured data.

Transfer to operator evolution. Bounded metabolic capacity $MC$ (Def. definition:bk5_metabolic_capacity_mc_, Prop. proposition:bk5_fixed_metabolic_capacity) confines the operator path $gamma$ (Prop. proposition:bk5_operator_evolution) to the viability domain (Def. definition:bk5_viability_domain) on which the flow is well-posed, so the density-level estimate transfers to $Op(M)$. The discrete-time companion - in which the per-step gap ratio is measured in the Appendix B suite rather than derived - is Cor. corollary:bk7_geometric_convergence_rate; it corroborates, but is not used to establish, the rate proved here.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_operator_convergence}
\leavevmode

\emph{Convergence (inherited, not re-derived).} By the SRMF selection dynamics (Ax.~\ref{axiom:bk5_srmf_operator_selection_evolution}) the system descends $\Fproc$, which by Def.~\ref{definition:bk5_process_free_energy} is the process-level instance of the symbolic free energy (Def.~\ref{definition:bk2_symbolic_free_energy}). On $(\prob(M),\wass)$ this descent is the Wasserstein gradient flow $\partial_t \rho = -\operatorname{grad}_{\wass}\Fproc[\rho]$ (Thm.~\ref{theorem:bk2_wasserstein_gradient_flow}). By the symbolic $H$-theorem (Thm.~\ref{theorem:bk2_h_theorem_for_symbolic_evol}), $\Fproc$ is then a Lyapunov functional, $\tfrac{d}{dt}\Fproc[\rho_t]\le 0$ with equality only at a critical density; hence $\rho_t$ converges to a local minimizer $\rho^{\ast}$ of $\Fproc$ (of the equilibrium type characterized by Thm.~\ref{theorem:bk2_equilibrium_distribution}). Convergence thus rests \emph{entirely on the proven Book~II machinery}; no new convergence claim is asserted here.

\emph{Rate (derived from convexity, not fitted).} Under Assumption~\ref{assumption:bk5_displacement_convexity} the flow satisfies the Evolution Variational Inequality
\[
\tfrac{1}{2}\,\tfrac{d}{dt}\,\wass(\rho_t,\rho^{\ast})^2 \;\le\; \Fproc[\rho^{\ast}] - \Fproc[\rho_t] - \tfrac{\lambda}{2}\,\wass(\rho_t,\rho^{\ast})^2 .
\]
Since $\rho^{\ast}$ minimizes $\Fproc$, the first difference is $\le 0$. For $\lambda = 0$, integrating yields the descent estimate
\[
\Fproc[\rho_t] - \Fproc[\rho^{\ast}] \;\le\; \frac{\wass(\rho_0,\rho^{\ast})^2}{2t} \;=\; O(1/t),
\]
and for $\lambda > 0$ the inequality sharpens to the exponential bound
\[
\Fproc[\rho_t] - \Fproc[\rho^{\ast}] \;\le\; e^{-2\lambda t}\,\bigl(\Fproc[\rho_0] - \Fproc[\rho^{\ast}]\bigr).
\]
Hence convergence proceeds at rate $O(1/t)$ or faster, as claimed --- a rate \emph{proved} from the convexity of the functional, with no appeal to measured data.

\emph{Transfer to operator evolution.} Bounded metabolic capacity $\MC$ (Def.~\ref{definition:bk5_metabolic_capacity_mc_}, Prop.~\ref{proposition:bk5_fixed_metabolic_capacity}) confines the operator path $\gamma$ (Prop.~\ref{proposition:bk5_operator_evolution}) to the viability domain (Def.~\ref{definition:bk5_viability_domain}) on which the flow is well-posed, so the density-level estimate transfers to $\Op(M)$. The discrete-time companion --- in which the per-step gap ratio is \emph{measured} in the Appendix~B suite rather than derived --- is Cor.~\ref{corollary:bk7_geometric_convergence_rate}; it \emph{corroborates}, but is not used to establish, the rate proved here.
\end{proof}
```

### Metabolically Bounded Reflection (`axiom:bk5_metabolically_bounded_reflection`)

Role: `axiom` | Type: `axiom` | Book: `book5` | Source: `book5.tex:1608`

- Proof status: `definitional`
- Depends on: `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$)
- Cites: `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$)
- Cited by: `corollary:bk5__metabolically_bounded_reflection_corollary`; `proof:bk5__metabolically_bounded_reflection_corollary`
- Macros used: `\MC`

**Statement / Body**

Let $B := f(MC(S))$ with $f$ non-decreasing and $f(MC) leq MC$ (cf. Def. definition:bk5_metabolic_capacity_mc_). Then:
\[
\| D R \|_g leq B.
\]

**Verbatim LaTeX Body**

```latex
\begin{axiom}[Metabolically Bounded Reflection]
\label{axiom:bk5_metabolically_bounded_reflection}
Let $B := f(\MC(S))$ with $f$ non-decreasing and $f(\MC) \leq \MC$ (cf.~Def.~\ref{definition:bk5_metabolic_capacity_mc_}). Then:
\[
\| D R \|_g \leq B.
\]
\end{axiom}
```

### corollary:bk5__metabolically_bounded_reflection_corollary (`corollary:bk5__metabolically_bounded_reflection_corollary`)

Role: `corollary` | Type: `corollary` | Book: `book5` | Source: `book5.tex:1615`

- Proof status: `proven`
- Depends on: `axiom:bk5_metabolically_bounded_reflection` (Metabolically Bounded Reflection)
- Cites: `axiom:bk5_metabolically_bounded_reflection` (Metabolically Bounded Reflection)
- Cited by: none
- Macros used: `\MC`

**Statement / Body**

The maximum depth $n_{max}$ of recursive reflection satisfies (cf. Ax. axiom:bk5_metabolically_bounded_reflection):
\[
n_{max} leq leftlfloor log_kleft(frac{MC(S)}{c_0} + 1right) rightrfloor.
\]

**Verbatim LaTeX Body**

```latex
\begin{corollary} \label{corollary:bk5__metabolically_bounded_reflection_corollary}
The maximum depth $n_{\max}$ of recursive reflection satisfies (cf.~Ax.~\ref{axiom:bk5_metabolically_bounded_reflection}):
\[
n_{\max} \leq \left\lfloor \log_k\left(\frac{\MC(S)}{c_0} + 1\right) \right\rfloor.
\]
\end{corollary}
```

### proof:bk5__metabolically_bounded_reflection_corollary (`proof:bk5__metabolically_bounded_reflection_corollary`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1621`

- Proof status: `not_applicable`
- Depends on: `axiom:bk5_metabolically_bounded_reflection` (Metabolically Bounded Reflection)
- Cites: `axiom:bk5_metabolically_bounded_reflection` (Metabolically Bounded Reflection)
- Cited by: none
- Macros used: `\MC`

**Statement / Body**

By the metabolically bounded reflection axiom (Ax. axiom:bk5_metabolically_bounded_reflection) recursive reflection is funded by a total budget no larger than $B=f(MC(S))leMC(S)$. Recursion is geometric: the first reflective level costs a base amount $c_0>0$, and each deeper level composes one further drift-reflection step, compounding the cost by a fixed factor $k>1$. The cumulative cost of $n$ nested levels is therefore the geometric accumulation
\[
C(n)=c_0sum_{i=0}^{n-1}k^{i}(k-1)=c_0 (k^{n}-1).
\]
Sustaining depth $n$ requires $C(n)leMC(S)$, i.e.\ $c_0(k^{n}-1)leMC(S)$, equivalently $k^{n}le tfrac{MC(S)}{c_0}+1$. Taking $log_k$ and using that $n$ is a nonnegative integer gives $nlebiglfloorlog_k\!big(tfrac{MC(S)}{c_0}+1big)bigrfloor$. The deepest admissible recursion is thus $n_{max}=biglfloorlog_k(MC(S)/c_0+1)bigrfloor$, as claimed.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5__metabolically_bounded_reflection_corollary}
\leavevmode
By the metabolically bounded reflection axiom (Ax.~\ref{axiom:bk5_metabolically_bounded_reflection}) recursive reflection is funded by a total budget no larger than $B=f(\MC(S))\le\MC(S)$. Recursion is geometric: the first reflective level costs a base amount $c_0>0$, and each deeper level composes one further drift--reflection step, compounding the cost by a fixed factor $k>1$. The cumulative cost of $n$ nested levels is therefore the geometric accumulation
\[
C(n)=c_0\sum_{i=0}^{n-1}k^{i}(k-1)=c_0\,(k^{n}-1).
\]
Sustaining depth $n$ requires $C(n)\le\MC(S)$, i.e.\ $c_0(k^{n}-1)\le\MC(S)$, equivalently $k^{n}\le \tfrac{\MC(S)}{c_0}+1$. Taking $\log_k$ and using that $n$ is a nonnegative integer gives $n\le\big\lfloor\log_k\!\big(\tfrac{\MC(S)}{c_0}+1\big)\big\rfloor$. The deepest admissible recursion is thus $n_{\max}=\big\lfloor\log_k(\MC(S)/c_0+1)\big\rfloor$, as claimed.
\end{proof}
```

### Extended Theoretical Implications (`subsec:bk5_extended_theoretical_implications`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1630`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Certified SRMF Operator Adaptation (`theorem:bk5__srmf_operator_adaptation`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:1632`

- Proof status: `proven`
- Depends on: `axiom:bk5_srmf_operator_selection_evolution` (Stateful SRMF Operator Selection and Evolution)
- Cites: `axiom:bk5_srmf_operator_selection_evolution` (Stateful SRMF Operator Selection and Evolution)
- Cited by: `proof:bk5_operators_evolve`; `proposition:bk5_operators_evolve`
- Macros used: `\Fproc`

**Statement / Body**

Let the stateful law of Ax. axiom:bk5_srmf_operator_selection_evolution
be supplied. Suppose
$mathcal E_{eff}[mathcal O_t,S_t]<theta_{crit}$, choose a
feedback gain $g>0$, and define the refinement velocity
\[
 v_t=gmax{theta_{crit}-
 mathcal E_{eff}[mathcal O_t,S_t],0}.
\]
Then $v_t=g(theta_{crit}-mathcal E_{eff})>0$. If the
parameter update is additionally supplied as a negative-gradient step for
$Fproc^{y_t}$ with a step size certified for descent, the process objective
is non-increasing. This descent can coexist with a transient increase in the
separate execution-cost coordinate. None of operator motion, inventory change,
or steepest descent follows from the below-threshold inequality alone.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Certified SRMF Operator Adaptation] \label{theorem:bk5__srmf_operator_adaptation}
Let the stateful law of Ax.~\ref{axiom:bk5_srmf_operator_selection_evolution}
be supplied. Suppose
$\mathcal E_{\mathrm{eff}}[\mathcal O_t,S_t]<\theta_{\mathrm{crit}}$, choose a
feedback gain $g>0$, and define the refinement velocity
\[
 v_t=g\max\{\theta_{\mathrm{crit}}-
 \mathcal E_{\mathrm{eff}}[\mathcal O_t,S_t],0\}.
\]
Then $v_t=g(\theta_{\mathrm{crit}}-\mathcal E_{\mathrm{eff}})>0$. If the
parameter update is additionally supplied as a negative-gradient step for
$\Fproc^{y_t}$ with a step size certified for descent, the process objective
is non-increasing. This descent can coexist with a transient increase in the
separate execution-cost coordinate. None of operator motion, inventory change,
or steepest descent follows from the below-threshold inequality alone.
\end{theorem}
```

### proof:bk5__srmf_operator_adaptation (`proof:bk5__srmf_operator_adaptation`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1648`

- Proof status: `not_applicable`
- Depends on: `axiom:bk5_srmf_operator_selection_evolution` (Stateful SRMF Operator Selection and Evolution)
- Cites: `axiom:bk5_srmf_operator_selection_evolution` (Stateful SRMF Operator Selection and Evolution)
- Cited by: none
- Macros used: `\Fproc`

**Statement / Body**

Below threshold the maximum selects its positive branch, so
$v_t=g(theta_{crit}-mathcal E_{eff})$; positivity follows
from $g>0$ and the strict shortfall. For a supplied gradient update
$vartheta_{t+1}=vartheta_t-etanablaFproc^{y_t}(vartheta_t)$, the stated
step-size certificate gives
$Fproc^{y_t}(vartheta_{t+1})le
Fproc^{y_t}(vartheta_t)$. In the finite-inventory branch, the minimizer
certificate in Ax. axiom:bk5_srmf_operator_selection_evolution gives the
stronger comparison against every member of $A_{t+1}$ and records the former
incumbent in $H_{t+1}$.

The execution cost is a different coordinate of the process objective. Two
available operators may satisfy
$Fproc^{y_t}(mathcal O_{t+1})<Fproc^{y_t}(mathcal O_t)$ while
$mathcal E_{cost}(mathcal O_t)<
mathcal E_{cost}(mathcal O_{t+1})$, establishing the final
possibility without asserting that it occurs on every step. Finally, an
identity update below threshold is a countermodel to adaptation without the
supplied feedback and update laws.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5__srmf_operator_adaptation}
\leavevmode

Below threshold the maximum selects its positive branch, so
$v_t=g(\theta_{\mathrm{crit}}-\mathcal E_{\mathrm{eff}})$; positivity follows
from $g>0$ and the strict shortfall.  For a supplied gradient update
$\vartheta_{t+1}=\vartheta_t-\eta\nabla\Fproc^{y_t}(\vartheta_t)$, the stated
step-size certificate gives
$\Fproc^{y_t}(\vartheta_{t+1})\le
\Fproc^{y_t}(\vartheta_t)$.  In the finite-inventory branch, the minimizer
certificate in Ax.~\ref{axiom:bk5_srmf_operator_selection_evolution} gives the
stronger comparison against every member of $A_{t+1}$ and records the former
incumbent in $H_{t+1}$.

The execution cost is a different coordinate of the process objective.  Two
available operators may satisfy
$\Fproc^{y_t}(\mathcal O_{t+1})<\Fproc^{y_t}(\mathcal O_t)$ while
$\mathcal E_{\mathrm{cost}}(\mathcal O_t)<
\mathcal E_{\mathrm{cost}}(\mathcal O_{t+1})$, establishing the final
possibility without asserting that it occurs on every step.  Finally, an
identity update below threshold is a countermodel to adaptation without the
supplied feedback and update laws.
\end{proof}
```

### Operator Viability Set $\mathcal{V}_{\text{op}}$ (`definition:bk5__operator_viability_set_v`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1672`

- Proof status: `definitional`
- Depends on: `axiom:bk5_srmf_operator_selection_evolution` (Stateful SRMF Operator Selection and Evolution); `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$)
- Cites: `axiom:bk5_srmf_operator_selection_evolution` (Stateful SRMF Operator Selection and Evolution); `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$)
- Cited by: `proof:bk5_operators_evolve`; `proposition:bk5_operators_evolve`
- Macros used: `\Fproc`, `\Op`

**Statement / Body**

\[
V_{text{op}} := left{ O in Op(M) mid Fproc[O, S] < theta_{text{proc}} right} text{(cf. Def. definition:bk5_process_free_energy, Ax. axiom:bk5_srmf_operator_selection_evolution)}.
\]

**Verbatim LaTeX Body**

```latex
\begin{definition}[Operator Viability Set $\mathcal{V}_{\text{op}}$] \label{definition:bk5__operator_viability_set_v}

\[
\mathcal{V}_{\text{op}} := \left\{ \mathcal{O} \in \Op(M) \mid \Fproc[\mathcal{O}, S] < \theta_{\text{proc}} \right\} \quad \text{(cf.~Def.~\ref{definition:bk5_process_free_energy}, Ax.~\ref{axiom:bk5_srmf_operator_selection_evolution})}.
\]
\end{definition}
```

### proposition:bk5_operators_evolve (`proposition:bk5_operators_evolve`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:1678`

- Proof status: `proven`
- Depends on: `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk5__operator_viability_set_v` (Operator Viability Set $\mathcal{V}_{\text{op}}$); `proposition:bk5_fixed_metabolic_capacity` (Fixed Metabolic Capacity); `proposition:bk5_operator_evolution` (Operator Evolution); `theorem:bk5__srmf_operator_adaptation` (Certified SRMF Operator Adaptation); `theorem:bk5_operator_convergence` (Operator Convergence)
- Cites: `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk5__operator_viability_set_v` (Operator Viability Set $\mathcal{V}_{\text{op}}$); `theorem:bk5__srmf_operator_adaptation` (Certified SRMF Operator Adaptation); `theorem:bk5_operator_convergence` (Operator Convergence)
- Cited by: `proof:bk5_complexity_stability_tradeoff`; `theorem:bk5_complexity_stability_tradeoff` (Complexity-Stability Tradeoff)
- Macros used: none

**Statement / Body**

Operators evolve to remain within $V_{text{op}}$
(cf. Def. definition:bk5__operator_viability_set_v,
Thm. theorem:bk5_operator_convergence,
Thm. theorem:bk5__srmf_operator_adaptation,
Def. definition:bk4_test_time_integrative_expansion).
Under hard constraints, the system sacrifices operator complexity.

**Verbatim LaTeX Body**

```latex
\begin{proposition}
\label{proposition:bk5_operators_evolve}
\leavevmode\newline
Operators evolve to remain within $\mathcal{V}_{\text{op}}$
(cf.~Def.~\ref{definition:bk5__operator_viability_set_v},
Thm.~\ref{theorem:bk5_operator_convergence},
Thm.~\ref{theorem:bk5__srmf_operator_adaptation},
Def.~\ref{definition:bk4_test_time_integrative_expansion}).
Under hard constraints, the system sacrifices operator complexity.
\end{proposition}
```

### proof:bk5_operators_evolve (`proof:bk5_operators_evolve`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1688`

- Proof status: `not_applicable`
- Depends on: `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk5__operator_viability_set_v` (Operator Viability Set $\mathcal{V}_{\text{op}}$); `proposition:bk5_fixed_metabolic_capacity` (Fixed Metabolic Capacity); `proposition:bk5_operator_evolution` (Operator Evolution); `theorem:bk5__srmf_operator_adaptation` (Certified SRMF Operator Adaptation); `theorem:bk5_operator_convergence` (Operator Convergence)
- Cites: `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk5__operator_viability_set_v` (Operator Viability Set $\mathcal{V}_{\text{op}}$); `proposition:bk5_fixed_metabolic_capacity` (Fixed Metabolic Capacity); `proposition:bk5_operator_evolution` (Operator Evolution); `theorem:bk5__srmf_operator_adaptation` (Certified SRMF Operator Adaptation); `theorem:bk5_operator_convergence` (Operator Convergence)
- Cited by: none
- Macros used: `\Fproc`

**Statement / Body**

The operator viability set $V_{text{op}}={O:Fproc[O,S]<theta_{text{proc}}}$ (Def. definition:bk5__operator_viability_set_v) is the strict sublevel set of $Fproc$. By Operator Evolution (Prop. proposition:bk5_operator_evolution) the SRMF path descends $Fproc$ and is stationary only at a minimizer; by SRMF Operator Adaptation (Thm. theorem:bk5__srmf_operator_adaptation) this descent is steepest in $Fproc$ and accelerates whenever effectiveness degrades. Since $Fproc$ is non-increasing along the flow and strictly decreasing off the minimizer, the flow maps $V_{text{op}}$ into itself and drives any super-threshold operator toward it, converging to a minimizer inside $V_{text{op}}$ (Thm. theorem:bk5_operator_convergence); the integrative-expansion coupling (Def. definition:bk4_test_time_integrative_expansion) supplies the admissible directions of this evolution. Thus operators evolve so as to remain within $V_{text{op}}$. Finally, under hard metabolic constraints the cost is capped, $E_{text{cost}}[O]leE_{text{cost}}^{max}$ (Prop. proposition:bk5_fixed_metabolic_capacity); maintaining $Fproc<theta_{text{proc}}$ then forces the descent to economize on the cost-bearing structure of $O$, i.e.\ to lower operator complexity. Hence under hard constraints the system sacrifices operator complexity to preserve viability.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_operators_evolve}
\leavevmode
The operator viability set $\mathcal{V}_{\text{op}}=\{\mathcal{O}:\Fproc[\mathcal{O},S]<\theta_{\text{proc}}\}$ (Def.~\ref{definition:bk5__operator_viability_set_v}) is the strict sublevel set of $\Fproc$. By Operator Evolution (Prop.~\ref{proposition:bk5_operator_evolution}) the SRMF path descends $\Fproc$ and is stationary only at a minimizer; by SRMF Operator Adaptation (Thm.~\ref{theorem:bk5__srmf_operator_adaptation}) this descent is steepest in $\Fproc$ and accelerates whenever effectiveness degrades. Since $\Fproc$ is non-increasing along the flow and strictly decreasing off the minimizer, the flow maps $\mathcal{V}_{\text{op}}$ into itself and drives any super-threshold operator toward it, converging to a minimizer inside $\mathcal{V}_{\text{op}}$ (Thm.~\ref{theorem:bk5_operator_convergence}); the integrative-expansion coupling (Def.~\ref{definition:bk4_test_time_integrative_expansion}) supplies the admissible directions of this evolution. Thus operators evolve so as to remain within $\mathcal{V}_{\text{op}}$. Finally, under hard metabolic constraints the cost is capped, $\mathcal{E}_{\text{cost}}[\mathcal{O}]\le\mathcal{E}_{\text{cost}}^{\max}$ (Prop.~\ref{proposition:bk5_fixed_metabolic_capacity}); maintaining $\Fproc<\theta_{\text{proc}}$ then forces the descent to economize on the cost-bearing structure of $\mathcal{O}$, i.e.\ to lower operator complexity. Hence under hard constraints the system sacrifices operator complexity to preserve viability.
\end{proof}
```

### Operator Complexity, Stability Margin, Maintenance Cost (`definition:bk5_complexity_stability_maintenance`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1693`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$); `definition:bk5_viability_domain` (Viability Domain)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk5_process_free_energy` (Process Free Energy $\Fproc$); `definition:bk5_viability_domain` (Viability Domain)
- Cited by: `proof:bk5_complexity_stability_tradeoff`; `theorem:bk5_complexity_stability_tradeoff` (Complexity-Stability Tradeoff)
- Macros used: `\Op`, `\freeenergy`

**Statement / Body**

For an operator $OinOp(M)$ acting on system $S$ we define:


- Operator complexity $C(O):=E_{text{cost}}[O]$, the cost-bearing structure of $O$ in the process free energy (Def. definition:bk5_process_free_energy).

- Stability margin $S(S):=inf_tbig(freeenergy(rho_t)-freeenergy^{min}big)$, the viability reserve held against drift along the trajectory (Def. definition:bk2_symbolic_free_energy, Def. definition:bk5_viability_domain).

- Maintenance cost $E_{text{maint}}(O,S):=C(O) S(S)/alpha$, the work to hold $O$ stable against drift to margin $S(S)$, conversion constant $alpha>0$. The product form is a structural cost model (each unit of complexity is maintained to the degree the margin sets), not an empirically fitted law.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Operator Complexity, Stability Margin, Maintenance Cost]
\label{definition:bk5_complexity_stability_maintenance}
For an operator $\mathcal{O}\in\Op(M)$ acting on system $S$ we define:
\begin{enumerate}
    \item \textbf{Operator complexity} $\mathcal{C}(\mathcal{O}):=\mathcal{E}_{\text{cost}}[\mathcal{O}]$, the cost-bearing structure of $\mathcal{O}$ in the process free energy (Def.~\ref{definition:bk5_process_free_energy}).
    \item \textbf{Stability margin} $\mathcal{S}(S):=\inf_t\big(\freeenergy(\rho_t)-\freeenergy^{\min}\big)$, the viability reserve held against drift along the trajectory (Def.~\ref{definition:bk2_symbolic_free_energy}, Def.~\ref{definition:bk5_viability_domain}).
    \item \textbf{Maintenance cost} $E_{\text{maint}}(\mathcal{O},S):=\mathcal{C}(\mathcal{O})\,\mathcal{S}(S)/\alpha$, the work to hold $\mathcal{O}$ stable against drift to margin $\mathcal{S}(S)$, conversion constant $\alpha>0$. The product form is a structural cost model (each unit of complexity is maintained to the degree the margin sets), not an empirically fitted law.
\end{enumerate}
\end{definition}
```

### Complexity-Stability Tradeoff (`theorem:bk5_complexity_stability_tradeoff`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:1702`

- Proof status: `proven`
- Depends on: `definition:bk5_complexity_stability_maintenance` (Operator Complexity, Stability Margin, Maintenance Cost); `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `proposition:bk5_fixed_metabolic_capacity` (Fixed Metabolic Capacity); `proposition:bk5_operators_evolve`
- Cites: `definition:bk5_complexity_stability_maintenance` (Operator Complexity, Stability Margin, Maintenance Cost); `proposition:bk5_operators_evolve`
- Cited by: `corollary:bk5_complexity_stability_tradeoff` (Complexity Stability Tradeoff); `proof:bk5_complexity_stability_tradeoff_cor`; `proof:bk5_metabolic_capacity_non_decreasing`; `proposition:bk5_metabolic_capacity_non_decreasing`
- Macros used: `\MC`

**Statement / Body**

With $C$, $S$, and $E_{text{maint}}$ as in
Def. definition:bk5_complexity_stability_maintenance and
Prop. proposition:bk5_operators_evolve, admissible complexity is
metabolically budgeted:
\[
C(O) cdot S(S) leq alpha cdot MC(S).
\]

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Complexity-Stability Tradeoff] \label{theorem:bk5_complexity_stability_tradeoff}
\leavevmode\newline
With $\mathcal{C}$, $\mathcal{S}$, and $E_{\text{maint}}$ as in
Def.~\ref{definition:bk5_complexity_stability_maintenance} and
Prop.~\ref{proposition:bk5_operators_evolve}, admissible complexity is
metabolically budgeted:
\[
\mathcal{C}(\mathcal{O}) \cdot \mathcal{S}(S) \leq \alpha \cdot \MC(S).
\]
\end{theorem}
```

### proof:bk5_complexity_stability_tradeoff (`proof:bk5_complexity_stability_tradeoff`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1712`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_complexity_stability_maintenance` (Operator Complexity, Stability Margin, Maintenance Cost); `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `proposition:bk5_fixed_metabolic_capacity` (Fixed Metabolic Capacity); `proposition:bk5_operators_evolve`
- Cites: `definition:bk5_complexity_stability_maintenance` (Operator Complexity, Stability Margin, Maintenance Cost); `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `proposition:bk5_fixed_metabolic_capacity` (Fixed Metabolic Capacity); `proposition:bk5_operators_evolve`
- Cited by: none
- Macros used: `\MC`

**Statement / Body**

By Def. definition:bk5_complexity_stability_maintenance the maintenance cost is $E_{text{maint}}(O,S)=C(O) S(S)/alpha$. By Operators Evolve (Prop. proposition:bk5_operators_evolve) sustained viability requires this expenditure to be fundable from the metabolic capacity, $E_{text{maint}}leMC(S)$ (Def. definition:bk5_metabolic_capacity_mc_, Prop. proposition:bk5_fixed_metabolic_capacity). Substituting the definition of $E_{text{maint}}$,
\[
frac{C(O) S(S)}{alpha}leMC(S) Longleftrightarrow C(O)cdotS(S)lealpha MC(S).
\]
Admissible complexity is therefore metabolically budgeted: at fixed capacity, greater stability can be purchased only by reducing complexity, and conversely. The bound now follows from explicit definitions of $C$, $S$, and $E_{text{maint}}$ (Def. definition:bk5_complexity_stability_maintenance) together with the proven viability requirement, with no ad hoc in-proof reading and no empirically fitted scaling law.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_complexity_stability_tradeoff}
\leavevmode
By Def.~\ref{definition:bk5_complexity_stability_maintenance} the maintenance cost is $E_{\text{maint}}(\mathcal{O},S)=\mathcal{C}(\mathcal{O})\,\mathcal{S}(S)/\alpha$. By Operators Evolve (Prop.~\ref{proposition:bk5_operators_evolve}) sustained viability requires this expenditure to be fundable from the metabolic capacity, $E_{\text{maint}}\le\MC(S)$ (Def.~\ref{definition:bk5_metabolic_capacity_mc_}, Prop.~\ref{proposition:bk5_fixed_metabolic_capacity}). Substituting the definition of $E_{\text{maint}}$,
\[
\frac{\mathcal{C}(\mathcal{O})\,\mathcal{S}(S)}{\alpha}\le\MC(S)\quad\Longleftrightarrow\quad \mathcal{C}(\mathcal{O})\cdot\mathcal{S}(S)\le\alpha\,\MC(S).
\]
Admissible complexity is therefore metabolically budgeted: at fixed capacity, greater stability can be purchased only by reducing complexity, and conversely. The bound now follows from explicit definitions of $\mathcal{C}$, $\mathcal{S}$, and $E_{\text{maint}}$ (Def.~\ref{definition:bk5_complexity_stability_maintenance}) together with the proven viability requirement, with no ad hoc in-proof reading and no empirically fitted scaling law.
\end{proof}
```

### Complexity Stability Tradeoff (`corollary:bk5_complexity_stability_tradeoff`)

Role: `corollary` | Type: `corollary` | Book: `book5` | Source: `book5.tex:1721`

- Proof status: `proven`
- Depends on: `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `theorem:bk5_complexity_stability_tradeoff` (Complexity-Stability Tradeoff)
- Cites: `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `theorem:bk5_complexity_stability_tradeoff` (Complexity-Stability Tradeoff)
- Cited by: none
- Macros used: `\MC`

**Statement / Body**

Higher $MC$ permits both higher operator complexity and greater system stability (cf. Thm. theorem:bk5_complexity_stability_tradeoff, Def. definition:bk5_metabolic_capacity_mc_).

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Complexity Stability Tradeoff]
\label{corollary:bk5_complexity_stability_tradeoff}
Higher $\MC$ permits both higher operator complexity and greater system stability (cf.~Thm.~\ref{theorem:bk5_complexity_stability_tradeoff}, Def.~\ref{definition:bk5_metabolic_capacity_mc_}).
\end{corollary}
```

### proof:bk5_complexity_stability_tradeoff_cor (`proof:bk5_complexity_stability_tradeoff_cor`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1725`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `theorem:bk5_complexity_stability_tradeoff` (Complexity-Stability Tradeoff)
- Cites: `definition:bk5_metabolic_capacity_mc_` (Metabolic Capacity $\MC$); `theorem:bk5_complexity_stability_tradeoff` (Complexity-Stability Tradeoff)
- Cited by: none
- Macros used: `\MC`

**Statement / Body**

By the tradeoff bound $C(O)cdotS(S)lealpha MC(S)$ (Thm. theorem:bk5_complexity_stability_tradeoff) the feasible set for the pair $(C,S)$ is the hyperbolic region ${(C,S):C Slealpha MC(S)}$. Its right-hand side is strictly increasing in the metabolic capacity $MC(S)$ (Def. definition:bk5_metabolic_capacity_mc_), so raising $MC(S)$ enlarges the feasible region: every previously attainable $(C,S)$ remains attainable, and in addition pairs with larger $C$, larger $S$, or both become admissible. In particular the maximal attainable complexity at any fixed stability and the maximal attainable stability at any fixed complexity each increase with $MC(S)$. Hence higher metabolic capacity permits simultaneously higher operator complexity and greater system stability.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_complexity_stability_tradeoff_cor}
\leavevmode
By the tradeoff bound $\mathcal{C}(\mathcal{O})\cdot\mathcal{S}(S)\le\alpha\,\MC(S)$ (Thm.~\ref{theorem:bk5_complexity_stability_tradeoff}) the feasible set for the pair $(\mathcal{C},\mathcal{S})$ is the hyperbolic region $\{(\mathcal{C},\mathcal{S}):\mathcal{C}\,\mathcal{S}\le\alpha\,\MC(S)\}$. Its right-hand side is strictly increasing in the metabolic capacity $\MC(S)$ (Def.~\ref{definition:bk5_metabolic_capacity_mc_}), so raising $\MC(S)$ enlarges the feasible region: every previously attainable $(\mathcal{C},\mathcal{S})$ remains attainable, and in addition pairs with larger $\mathcal{C}$, larger $\mathcal{S}$, or both become admissible. In particular the maximal attainable complexity at any fixed stability and the maximal attainable stability at any fixed complexity each increase with $\MC(S)$. Hence higher metabolic capacity permits simultaneously higher operator complexity and greater system stability.
\end{proof}
```

### Philosophical and Cognitive Implications (`subsec:bk5_philosophical_and_cognitive_implications`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1730`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Metabolic Cost of Cognition (`scholium:bk5_metabolic_cost_of_cognition`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:1732`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cites: `definition:bk1_self_regulating_mapping_function_srmf` (Self-Regulating Mapping Function (SRMF)); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk2_symbolic_entropy` (Symbolic Entropy); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cited by: none
- Macros used: `\MC`

**Statement / Body**

Higher $MC$ (Def. definition:bk1_self_regulating_mapping_function_srmf)
supports recursive debugging, high-fidelity observers, and precise
renormalization. It lowers symbolic free energy $F_s$
(Def. definition:bk2_symbolic_free_energy) and reduces entropy
(Def. definition:bk2_symbolic_entropy) on the symbolic manifold $M$
(Def. definition:bk1_symbolic_manifold).
Declining $MC$ implies:


- Simplified reflective operators;

- Unresolved symbolic knots;

- Lower observer resolution;

- Shallower recursion;

- Loss of high-cost meta-cognition.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Metabolic Cost of Cognition] \label{scholium:bk5_metabolic_cost_of_cognition}
Higher $\MC$ (Def.~\ref{definition:bk1_self_regulating_mapping_function_srmf})
supports recursive debugging, high-fidelity observers, and precise
renormalization. It lowers symbolic free energy $F_s$
(Def.~\ref{definition:bk2_symbolic_free_energy}) and reduces entropy
(Def.~\ref{definition:bk2_symbolic_entropy}) on the symbolic manifold $M$
(Def.~\ref{definition:bk1_symbolic_manifold}).
Declining $\MC$ implies:
\begin{enumerate}
    \item Simplified reflective operators;
    \item Unresolved symbolic knots;
    \item Lower observer resolution;
    \item Shallower recursion;
    \item Loss of high-cost meta-cognition.
\end{enumerate}
\end{scholium}
```

### Metabolic Constraints on Reflective Accuracy (`theorem:bk5_metabolic_constraints_reflective_accuracy`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:1748`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: `corollary:bk5_symbolic_eigenlife` (Symbolic Eigenlife); `proof:bk5_symbolic_eigenlife`; `proposition:bk5_golden_ratio_thermodynamic_optimum` (Golden Ratio as Thermodynamic Optimum in the Balanced Regime)
- Macros used: `\MC`

**Statement / Body**

Let $f(n)$ be reflective fidelity at recursion depth $ninmathbb{N}$, and
let $n_{max}$ be the attained depth. Suppose:

- $f(0)=0$ and there is a calibrated marginal fidelity scale
$beta_0geq0$ such that

 f(n+1)-f(n)leqbeta_0 text{for every }n;


- geometric recursion has base cost $c_0>0$, growth factor $k>1$, and
nonnegative metabolic capacity $MC(S)$, with

 c_0bigl(k^{n_{max}}-1bigr)leqMC(S);


- the chosen cost and logarithm units carry an explicit nonnegative
calibration constant $C_{log}$ satisfying

 n_{max}leq C_{log}logbigl(1+MC(S)bigr).


Then, for $beta:=beta_0C_{log}geq0$,

 F(O_{reflect}):=f(n_{max})
 leqbetalogbigl(1+MC(S)bigr).


The calibration in Eq. eq:bk5_depth_log_calibration may be derived
from a fixed choice of $c_0$, $k$, and logarithm base, but it is not inferred
from metabolic capacity alone.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Metabolic Constraints on Reflective Accuracy] \label{theorem:bk5_metabolic_constraints_reflective_accuracy}
Let $f(n)$ be reflective fidelity at recursion depth $n\in\mathbb{N}$, and
let $n_{\max}$ be the attained depth.  Suppose:
\begin{enumerate}
\item $f(0)=0$ and there is a calibrated marginal fidelity scale
$\beta_0\geq0$ such that
\begin{equation}
 f(n+1)-f(n)\leq\beta_0\qquad\text{for every }n;
 \label{eq:bk5_marginal_fidelity_bound}
\end{equation}
\item geometric recursion has base cost $c_0>0$, growth factor $k>1$, and
nonnegative metabolic capacity $\MC(S)$, with
\begin{equation}
 c_0\bigl(k^{n_{\max}}-1\bigr)\leq\MC(S);
 \label{eq:bk5_accuracy_geometric_budget}
\end{equation}
\item the chosen cost and logarithm units carry an explicit nonnegative
calibration constant $C_{\log}$ satisfying
\begin{equation}
 n_{\max}\leq C_{\log}\log\bigl(1+\MC(S)\bigr).
 \label{eq:bk5_depth_log_calibration}
\end{equation}
\end{enumerate}
Then, for $\beta:=\beta_0C_{\log}\geq0$,
\begin{equation}
 \mathcal{F}(\mathcal{O}_{\mathrm{reflect}}):=f(n_{\max})
 \leq\beta\log\bigl(1+\MC(S)\bigr).
 \label{eq:bk5_reflective_accuracy_envelope}
\end{equation}
The calibration in Eq.~\eqref{eq:bk5_depth_log_calibration} may be derived
from a fixed choice of $c_0$, $k$, and logarithm base, but it is not inferred
from metabolic capacity alone.
\end{theorem}
```

### Marginal-Gain and Geometric-Budget Composition (`proof:bk5_metabolic_constraints_reflective_accuracy`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1781`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: `\MC`

**Statement / Body**

Telescoping Eq. eq:bk5_marginal_fidelity_bound from the zero-depth
normalization gives
\[
 f(n)leqbeta_0 n
\]
for every finite recursion depth. Independently,
Eq. eq:bk5_accuracy_geometric_budget and $c_0>0$ imply the
dimensionless power budget
\[
 k^{n_{max}}leqfrac{MC(S)}{c_0}+1.
\]
The precise passage from this power budget to the normalized coordinate
$log(1+MC(S))$ depends on $c_0$, $k$, and the log convention and is recorded
by Eq. eq:bk5_depth_log_calibration. Therefore
\[
 f(n_{max})leqbeta_0n_{max}
 leqbeta_0C_{log}log(1+MC(S)),
\]
which is Eq. eq:bk5_reflective_accuracy_envelope.

The marginal law is load-bearing: an admissible depth and capacity do not bound
an otherwise unrestricted fidelity assignment. Likewise, changing cost or
logarithm units without updating $C_{log}$ changes the numerical coefficient
$beta$ rather than revealing a universal scale.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Marginal-Gain and Geometric-Budget Composition]
\label{proof:bk5_metabolic_constraints_reflective_accuracy}
Telescoping Eq.~\eqref{eq:bk5_marginal_fidelity_bound} from the zero-depth
normalization gives
\[
 f(n)\leq\beta_0 n
\]
for every finite recursion depth.  Independently,
Eq.~\eqref{eq:bk5_accuracy_geometric_budget} and $c_0>0$ imply the
dimensionless power budget
\[
 k^{n_{\max}}\leq\frac{\MC(S)}{c_0}+1.
\]
The precise passage from this power budget to the normalized coordinate
$\log(1+\MC(S))$ depends on $c_0$, $k$, and the log convention and is recorded
by Eq.~\eqref{eq:bk5_depth_log_calibration}.  Therefore
\[
 f(n_{\max})\leq\beta_0n_{\max}
 \leq\beta_0C_{\log}\log(1+\MC(S)),
\]
which is Eq.~\eqref{eq:bk5_reflective_accuracy_envelope}.

The marginal law is load-bearing: an admissible depth and capacity do not bound
an otherwise unrestricted fidelity assignment.  Likewise, changing cost or
logarithm units without updating $C_{\log}$ changes the numerical coefficient
$\beta$ rather than revealing a universal scale.
\end{proof}
```

### Conclusion and Future Directions (`subsec:bk5_conclustion_and_future_directions`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1808`

- Proof status: `not_applicable`
- Depends on: `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `theorem:bk4_test_time_differentiation_c` (Test-Time Differentiation Collapse)
- Cites: `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk4_test_time_integrative_expansion` (Test-Time Integrative Expansion (TTIE)); `definition:bk4_test_time_precision_refinement` (Test-Time Precision Refinement (TTPR)); `theorem:bk4_test_time_differentiation_c` (Test-Time Differentiation Collapse)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Metabolism and Recursive Proportion (`sec:bk5_golden_ratio`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1813`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Introduction: Life as Recursive Equilibrium (`subsec:bk5_intro_recursive_equilibrium`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1816`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### The Golden Ratio as Spectral Attractor (`subsec:bk5_golden_ratio_spectral_attractor`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1823`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Balanced Two-Step Symbolic Memory Closure (`definition:bk5_balanced_two_step_memory_closure`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1828`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `corollary:bk5_symbolic_eigenlife` (Symbolic Eigenlife); `lemma:bk5_phi_critical_resonant_norm` ($\varphi$ as Balanced Memory Resonance); `proof:bk5_golden_ratio_curvature_scalar` (Balanced curvature ratio); `proof:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant via Balanced Memory Algebra); `proof:bk5_phi_critical_resonant_norm` ($\varphi$ as balanced memory resonance); `proof:bk5_symbolic_eigenlife`; `remark:bk5_symbolic_fibonacci_coding` (Symbolic Fibonacci Coding and Memory); `theorem:appC_modal_transference` (Modal Transference); `theorem:bk4_golden_event_horizon_spiral` (Golden Event Horizon Spiral); `theorem:bk5_golden_ratio_curvature_scalar` (Golden Ratio as Balanced Scale-Resonant Curvature Ratio); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_golden_rule_reciprocity` (Golden Rule Reciprocity)
- Macros used: none

**Statement / Body**

Let $S_n$ denote the $n$th observer-resolved symbolic state and let
$a_n=ell_O(S_n)geq 0$ be a scalar amplitude extracted by a positive
observer channel $ell_O$. The recursion has a balanced two-step memory
closure when, after normalizing the present-state channel to unit weight, the
only retained reflective memory channel has the same observer-visible weight:
\[
a_{n+1}=a_n+a_{n-1},
X_{n+1}=A X_n,
X_n=a_n\\ a_{n-1},
A=1&1\\1&0.
\]
The first coefficient is fixed by the choice of present-state unit; the second
coefficient is the balance condition asserting that retained reflective memory is
calibrated in the same observer-visible units as current persistence. If this
second coefficient is replaced by another positive weight, the resulting system
is a different metallic-ratio regime rather than the balanced PS memory regime.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Balanced Two-Step Symbolic Memory Closure]
\label{definition:bk5_balanced_two_step_memory_closure}
Let $S_n$ denote the $n$th observer-resolved symbolic state and let
$a_n=\ell_O(S_n)\geq 0$ be a scalar amplitude extracted by a positive
observer channel $\ell_O$.  The recursion has a \textbf{balanced two-step memory
closure} when, after normalizing the present-state channel to unit weight, the
only retained reflective memory channel has the same observer-visible weight:
\[
a_{n+1}=a_n+a_{n-1}, \qquad
X_{n+1}=A X_n,\qquad
X_n=\begin{pmatrix}a_n\\ a_{n-1}\end{pmatrix},\quad
A=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
The first coefficient is fixed by the choice of present-state unit; the second
coefficient is the balance condition asserting that retained reflective memory is
calibrated in the same observer-visible units as current persistence.  If this
second coefficient is replaced by another positive weight, the resulting system
is a different metallic-ratio regime rather than the balanced PS memory regime.
\end{definition}
```

### Balanced Observer Normalization Selects the Closure Matrix (`lemma:bk5_balanced_observer_normalization`)

Role: `lemma` | Type: `lemma` | Book: `book5` | Source: `book5.tex:1848`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: `proof:bk4_golden_event_horizon_spiral` (Golden spiral from balanced closure on the wheel); `proof:bk5_golden_rule_reciprocity` (Golden Rule reciprocity is the balanced closure); `theorem:bk4_golden_event_horizon_spiral` (Golden Event Horizon Spiral); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_golden_rule_reciprocity` (Golden Rule Reciprocity)
- Macros used: none

**Statement / Body**

Let the minimal two-channel memory closure be the general positive recurrence
\[
a_{n+1}=alpha a_n+beta a_{n-1},

A_{alpha,beta}=alpha&beta\\1&0,
 alpha,beta>0,
\]
where the present-persistence channel carries weight $alpha$ and the single
retained reflective-memory channel carries weight $beta$, both read through the
same positive observer channel $ell_O$. If

- present persistence is normalized to unit observer weight, and

- retained reflective memory is calibrated in the same observer-visible
units as present persistence (the balance condition),

then $alpha=beta=1$, so the unique positive two-step closure matrix is
\[
A=1&1\\1&0.
\]

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Balanced Observer Normalization Selects the Closure Matrix]
\label{lemma:bk5_balanced_observer_normalization}
Let the minimal two-channel memory closure be the general positive recurrence
\[
a_{n+1}=\alpha\,a_n+\beta\,a_{n-1},
\qquad
A_{\alpha,\beta}=\begin{pmatrix}\alpha&\beta\\1&0\end{pmatrix},
\qquad \alpha,\beta>0,
\]
where the present-persistence channel carries weight $\alpha$ and the single
retained reflective-memory channel carries weight $\beta$, both read through the
same positive observer channel $\ell_O$. If
\begin{enumerate}
\item present persistence is normalized to unit observer weight, and
\item retained reflective memory is calibrated in the same observer-visible
units as present persistence (the balance condition),
\end{enumerate}
then $\alpha=\beta=1$, so the unique positive two-step closure matrix is
\[
A=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
\end{lemma}
```

### proof:bk5_balanced_observer_normalization (`proof:bk5_balanced_observer_normalization`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1871`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Normalization (1) is the choice of observer unit for the present-state channel:
rescaling $ell_O$ so that one unit of current persistence maps to one unit of
amplitude fixes $alpha=1$. With present persistence now the unit of
observer-visible weight, condition (2) asserts that retained reflective memory is
not discounted or amplified relative to present persistence-it contributes in
the same units-so its coefficient equals the present-state unit, $beta=1$.
Both coefficients are thereby determined, and the companion matrix of the
recurrence is $A=big(1&1\\1&0big)$. Any
$betaneq 1$ violates (2) and yields a metallic-ratio regime
$lambda^2-lambda-beta=0$ rather than the balanced PS regime; any $alphaneq 1$
is merely a renormalization of the observer unit and is excluded by (1).

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_balanced_observer_normalization}
Normalization~(1) is the choice of observer unit for the present-state channel:
rescaling $\ell_O$ so that one unit of current persistence maps to one unit of
amplitude fixes $\alpha=1$. With present persistence now the unit of
observer-visible weight, condition~(2) asserts that retained reflective memory is
not discounted or amplified relative to present persistence---it contributes in
the same units---so its coefficient equals the present-state unit, $\beta=1$.
Both coefficients are thereby determined, and the companion matrix of the
recurrence is $A=\big(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\big)$. Any
$\beta\neq 1$ violates~(2) and yields a metallic-ratio regime
$\lambda^2-\lambda-\beta=0$ rather than the balanced PS regime; any $\alpha\neq 1$
is merely a renormalization of the observer unit and is excluded by~(1).
\end{proof}
```

### Golden Ratio as Spectral Invariant of Balanced Recursive Memory (`theorem:bk5_golden_ratio_spectral_invariant`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:1886`

- Proof status: `proven`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `definition:bk5_spectral_radius_of_coupl` (Spectral Radius of Coupling Tensor); `lemma:bk5_balanced_observer_normalization` (Balanced Observer Normalization Selects the Closure Matrix)
- Cites: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `definition:bk5_spectral_radius_of_coupl` (Spectral Radius of Coupling Tensor); `lemma:bk5_balanced_observer_normalization` (Balanced Observer Normalization Selects the Closure Matrix)
- Cited by: `corollary:bk5_symbolic_eigenlife` (Symbolic Eigenlife); `definition:bk5_map_mad_mas_band` (The MAD--MAP--MAS Band); `definition:bk5_symbolic_curvature_operator_spectrum` (Symbolic Curvature Operator Spectrum); `proof:bk4_golden_event_horizon_spiral` (Golden spiral from balanced closure on the wheel); `proof:bk5_complementary_constants` (Complementarity of first fracture and balanced resonance); `proof:bk5_fundamental_norm_fracture` (Norm-induced fracture theorem); `proof:bk5_golden_ratio_curvature_scalar` (Balanced curvature ratio); `proof:bk5_golden_ratio_thermodynamic_optimum` (Balanced thermodynamic optimum); `proof:bk5_golden_rule_reciprocity` (Golden Rule reciprocity is the balanced closure); `proof:bk5_map_mad_mas_trichotomy`; `proof:bk5_phi_critical_resonant_norm` ($\varphi$ as balanced memory resonance); `proof:bk5_symbolic_eigenlife`; `proof:bk5_symbolic_norm_spectrum` (Product spectrum); `proposition:bk5_complementary_constants` (Complementary Constants: Fracture vs Resonance); `proposition:bk5_golden_ratio_thermodynamic_optimum` (Golden Ratio as Thermodynamic Optimum in the Balanced Regime); `remark:bk5_curvature_vs_chaos` (Scale-Resonant Curvature vs Symbolic Chaos); `remark:bk5_symbolic_fibonacci_coding` (Symbolic Fibonacci Coding and Memory); `subsec:bk5_map_mad_mas_band` (The MAD--MAP--MAS Band); `theorem:bk4_golden_event_horizon_spiral` (Golden Event Horizon Spiral); `theorem:bk5_fundamental_dichotomy` (Fundamental Dichotomy of Symbolic Constants); `theorem:bk5_fundamental_norm_fracture` (Fundamental Theorem of Norm-Induced Symbolic Fracture); `theorem:bk5_golden_rule_reciprocity` (Golden Rule Reciprocity); `theorem:bk5_grand_unified_symbolic_geometric` (Product Theorem of the Symbolic-Geometric Interface); `theorem:bk5_symbolic_norm_spectrum` (Symbolic Norm Spectrum); `theorem:bk8_rg_fixed_point` (RG Fixed Point)
- Macros used: `\drift`, `\reflect`

**Statement / Body**

Let $drift$ be a symbolic drift operator and $reflect$ a reflection operator
whose interaction opens an observer-resolved memory channel through the local
drift-reflection commutator $[drift,reflect]$. If that channel closes as a
balanced two-step symbolic memory closure
(Def. definition:bk5_balanced_two_step_memory_closure), whose closure matrix
is uniquely fixed by observer normalization
(Lemma lemma:bk5_balanced_observer_normalization), then the dominant
eigenvalue $lambda$ of the closure operator (cf. Def. definition:bk5_spectral_radius_of_coupl) satisfies:
\[
lambda^2 - lambda - 1 = 0
\]
Hence the unique positive spectral radius of the balanced closure is
$lambda=varphi$, the Golden Ratio.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Golden Ratio as Spectral Invariant of Balanced Recursive Memory]
\label{theorem:bk5_golden_ratio_spectral_invariant}
Let $\drift$ be a symbolic drift operator and $\reflect$ a reflection operator
whose interaction opens an observer-resolved memory channel through the local
drift-reflection commutator $[\drift,\reflect]$.  If that channel closes as a
balanced two-step symbolic memory closure
(Def.~\ref{definition:bk5_balanced_two_step_memory_closure}), whose closure matrix
is uniquely fixed by observer normalization
(Lemma~\ref{lemma:bk5_balanced_observer_normalization}), then the dominant
eigenvalue $\lambda$ of the closure operator (cf.~Def.~\ref{definition:bk5_spectral_radius_of_coupl}) satisfies:
\[
\lambda^2 - \lambda - 1 = 0
\]
Hence the unique positive spectral radius of the balanced closure is
$\lambda=\varphi$, the Golden Ratio.
\end{theorem}
```

### The Golden Ratio as a Symbolic Invariant of Life (`sec:bk5_golden_ratio_invariant`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1903`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### The Metabolic Constant of Emergence (`subsec:bk5_metabolic_constant_emergence`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1906`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Golden Ratio as Spectral Invariant via Balanced Memory Algebra (`proof:bk5_golden_ratio_spectral_invariant`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1915`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk1_reflection_operator` (Reflection Operator); `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure)
- Cited by: `remark:bk9_grace_flow_geometric_witness` (Geometric witness: grace as curvature flow); `scholium:bk9_golden_rule_thermodynamic_covenant` (The Golden Rule as a Thermodynamic Covenant)
- Macros used: `\drift`, `\reflect`

**Statement / Body**

On the symbolic manifold $M$ (Def. definition:bk1_symbolic_manifold), the
commutator $[drift,reflect]$ of drift
(Def. definition:bk1_drift_field) and reflection
(Def. definition:bk1_reflection_operator) supplies the local channel by
which current transformation and retained reflective memory interact. Project
that channel to a positive observer-resolved amplitude $a_n=ell_O(S_n)$ and
impose the balanced two-step closure of
Def. definition:bk5_balanced_two_step_memory_closure. Then the state
vector $X_n=(a_n,a_{n-1})^T$ evolves by
\[
X_{n+1}=A X_n,
A=1&1\\1&0.
\]
The characteristic polynomial is
\[
det(lambda I-A)
=detlambda-1&-1\\-1&lambda
=lambda^2-lambda-1.
\]
Its roots are
\[
lambda_pm=frac{1pmsqrt{5}}{2}.
\]
The matrix $A$ is positive on the nonnegative cone after two iterates, so the
Perron-Frobenius eigenvalue is the unique positive spectral radius. Therefore
$rho(A)=lambda_+=varphi$, while the other eigenvalue is
$lambda_-=-varphi^{-1}$ and is subdominant in magnitude. For every
nonzero nonnegative initial amplitude vector, normalized iterates converge
projectively to the positive eigendirection, and the successive amplitude ratio
converges to $varphi$. Thus the Golden Ratio is not obtained from the
commutator alone; it is the spectral invariant of the balanced two-step closure
of the drift-reflection memory channel.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Golden Ratio as Spectral Invariant via Balanced Memory Algebra]
\label{proof:bk5_golden_ratio_spectral_invariant}
\leavevmode

On the symbolic manifold $M$ (Def.~\ref{definition:bk1_symbolic_manifold}), the
commutator $[\drift,\reflect]$ of drift
(Def.~\ref{definition:bk1_drift_field}) and reflection
(Def.~\ref{definition:bk1_reflection_operator}) supplies the local channel by
which current transformation and retained reflective memory interact.  Project
that channel to a positive observer-resolved amplitude $a_n=\ell_O(S_n)$ and
impose the balanced two-step closure of
Def.~\ref{definition:bk5_balanced_two_step_memory_closure}.  Then the state
vector $X_n=(a_n,a_{n-1})^T$ evolves by
\[
X_{n+1}=A X_n,\qquad
A=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
The characteristic polynomial is
\[
\det(\lambda I-A)
=\det\begin{pmatrix}\lambda-1&-1\\-1&\lambda\end{pmatrix}
=\lambda^2-\lambda-1.
\]
Its roots are
\[
\lambda_\pm=\frac{1\pm\sqrt{5}}{2}.
\]
The matrix $A$ is positive on the nonnegative cone after two iterates, so the
Perron--Frobenius eigenvalue is the unique positive spectral radius.  Therefore
$\rho(A)=\lambda_+=\varphi$, while the other eigenvalue is
$\lambda_-=-\varphi^{-1}$ and is subdominant in magnitude.  For every
nonzero nonnegative initial amplitude vector, normalized iterates converge
projectively to the positive eigendirection, and the successive amplitude ratio
converges to $\varphi$.  Thus the Golden Ratio is not obtained from the
commutator alone; it is the spectral invariant of the balanced two-step closure
of the drift-reflection memory channel.
\end{proof}
```

### Symbolic Eigenlife (`corollary:bk5_symbolic_eigenlife`)

Role: `corollary` | Type: `corollary` | Book: `book5` | Source: `book5.tex:1953`

- Proof status: `proven`
- Depends on: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `proposition:bk5_symbolic_life_criterion` (Symbolic Life Criterion); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_metabolic_constraints_reflective_accuracy` (Metabolic Constraints on Reflective Accuracy)
- Cites: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `proposition:bk5_symbolic_life_criterion` (Symbolic Life Criterion); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_metabolic_constraints_reflective_accuracy` (Metabolic Constraints on Reflective Accuracy)
- Cited by: `definition:bk8_identitystability` (Stability of Symbolic Identity \identitystability); `definition:bk8_recursive_symbolic_metaboloic_cycle` (Symbolic Metabolic Cycle $\Omega_{\mathrm{MP}}$); `lemma:bk7_involutive_dual_symmetry` (Involutive Dual Symmetry of Symbolic Power and Uncertainty); `proof:bk5_map_mad_mas_trichotomy`; `proof:bk8_biological_phase_transition`; `scholium:bk8_autonomous_repair_systems_expanded` (Autonomous Repair Systems as Metabolic Projections — An Expanded View); `sec:bk7_preamble_the_arc_toward_coherence` (Preamble: The Arc Toward Coherence); `subsec:bk5_map_mad_mas_band` (The MAD--MAP--MAS Band); `theorem:bk8_biological_phase_transition` (Threshold of Autonomy)
- Macros used: none

**Statement / Body**

A symbolic system exhibits eigenlife in the balanced two-step memory
regime when its observer-resolved dominant mode is governed by the positive
Perron root $varphi$. Subcritical modes with spectral radius below $1$ decay
under iteration, while supercritical unbalanced modes require additional
renormalization to avoid loss of bounded symbolic identity. Thus $varphi$ is
the unique spectral attractor for recursively stable symbolic persistence within
the balanced closure of
Def. definition:bk5_balanced_two_step_memory_closure
(cf. Thm. theorem:bk5_golden_ratio_spectral_invariant,
Thm. theorem:bk5_metabolic_constraints_reflective_accuracy,
Prop. proposition:bk5_symbolic_life_criterion).

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Symbolic Eigenlife]
\label{corollary:bk5_symbolic_eigenlife}
A symbolic system exhibits \textbf{eigenlife} in the balanced two-step memory
regime when its observer-resolved dominant mode is governed by the positive
Perron root $\varphi$.  Subcritical modes with spectral radius below $1$ decay
under iteration, while supercritical unbalanced modes require additional
renormalization to avoid loss of bounded symbolic identity.  Thus $\varphi$ is
the unique spectral attractor for recursively stable symbolic persistence within
the balanced closure of
Def.~\ref{definition:bk5_balanced_two_step_memory_closure}
(cf.~Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant},
Thm.~\ref{theorem:bk5_metabolic_constraints_reflective_accuracy},
Prop.~\ref{proposition:bk5_symbolic_life_criterion}).
\end{corollary}
```

### proof:bk5_symbolic_eigenlife (`proof:bk5_symbolic_eigenlife`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:1967`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `proposition:bk5_symbolic_life_criterion` (Symbolic Life Criterion); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_metabolic_constraints_reflective_accuracy` (Metabolic Constraints on Reflective Accuracy)
- Cites: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `proposition:bk5_symbolic_life_criterion` (Symbolic Life Criterion); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_metabolic_constraints_reflective_accuracy` (Metabolic Constraints on Reflective Accuracy)
- Cited by: none
- Macros used: none

**Statement / Body**

In the balanced two-step memory regime the observer-resolved state evolves by the closure matrix $A=big(1&1\\1&0big)$ (Def. definition:bk5_balanced_two_step_memory_closure), whose unique positive spectral radius is the Golden Ratio, $rho(A)=varphi$, with the second eigenvalue $-varphi^{-1}$ subdominant (Thm. theorem:bk5_golden_ratio_spectral_invariant). By Perron-Frobenius the normalized iterates converge projectively to the positive $varphi$-eigendirection, so the dominant observer-resolved mode of a balanced system is governed by $varphi$. By the symbolic life criterion (Prop. proposition:bk5_symbolic_life_criterion) persistence requires the dominant mode neither to decay to nothing nor to diverge without bound. A mode with spectral radius below $1$ contracts under iteration and its symbolic amplitude decays-no eigenlife; a supercritical unbalanced mode (spectral radius above $varphi$) grows without bound and can preserve bounded symbolic identity only by spending additional renormalization, whose budget is itself capped by reflective capacity (Thm. theorem:bk5_metabolic_constraints_reflective_accuracy). The balanced closure sits exactly at the Perron value $varphi>1$: expansive enough to persist against drift, yet fixed by observer normalization, so its iterates neither decay nor demand unbounded renormalization. Therefore a symbolic system exhibits eigenlife precisely when its dominant observer-resolved mode is governed by the Perron root $varphi$, which is the unique spectral attractor for recursively stable symbolic persistence within the balanced closure.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_symbolic_eigenlife}
\leavevmode
In the balanced two-step memory regime the observer-resolved state evolves by the closure matrix $A=\big(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\big)$ (Def.~\ref{definition:bk5_balanced_two_step_memory_closure}), whose unique positive spectral radius is the Golden Ratio, $\rho(A)=\varphi$, with the second eigenvalue $-\varphi^{-1}$ subdominant (Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}). By Perron--Frobenius the normalized iterates converge projectively to the positive $\varphi$-eigendirection, so the dominant observer-resolved mode of a balanced system is governed by $\varphi$. By the symbolic life criterion (Prop.~\ref{proposition:bk5_symbolic_life_criterion}) persistence requires the dominant mode neither to decay to nothing nor to diverge without bound. A mode with spectral radius below $1$ contracts under iteration and its symbolic amplitude decays---no eigenlife; a supercritical unbalanced mode (spectral radius above $\varphi$) grows without bound and can preserve bounded symbolic identity only by spending additional renormalization, whose budget is itself capped by reflective capacity (Thm.~\ref{theorem:bk5_metabolic_constraints_reflective_accuracy}). The balanced closure sits exactly at the Perron value $\varphi>1$: expansive enough to persist against drift, yet fixed by observer normalization, so its iterates neither decay nor demand unbounded renormalization. Therefore a symbolic system exhibits eigenlife precisely when its dominant observer-resolved mode is governed by the Perron root $\varphi$, which is the unique spectral attractor for recursively stable symbolic persistence within the balanced closure.
\end{proof}
```

### The MAD--MAP--MAS Band (`subsec:bk5_map_mad_mas_band`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:1973`

- Proof status: `not_applicable`
- Depends on: `corollary:bk5_symbolic_eigenlife` (Symbolic Eigenlife); `theorem:bk5_enhanced_map_mad_duality` (Enhanced MAP--MAD Regime Classification); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `corollary:bk5_symbolic_eigenlife` (Symbolic Eigenlife); `theorem:bk5_enhanced_map_mad_duality` (Enhanced MAP--MAD Regime Classification); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### The MAD--MAP--MAS Band (`definition:bk5_map_mad_mas_band`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:1977`

- Proof status: `definitional`
- Depends on: `corollary:bk5_map_evolutionary_advantag` (MAP Evolutionary Advantage); `definition:bk5_reflective_coupling_stab` (Reflective Coupling Stability Parameter); `definition:bk5_symbolic_bifurcation_man` (Symbolic Bifurcation Manifold); `proposition:bk4_imagination_bridges_wheel` (Imagination bridges the wheel); `scholium:bk4_imagination_as_imaginary_traversal` (Imagination as Imaginary Traversal); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `corollary:bk5_map_evolutionary_advantag` (MAP Evolutionary Advantage); `definition:bk5_reflective_coupling_stab` (Reflective Coupling Stability Parameter); `definition:bk5_symbolic_bifurcation_man` (Symbolic Bifurcation Manifold); `proposition:bk4_imagination_bridges_wheel` (Imagination bridges the wheel); `scholium:bk4_imagination_as_imaginary_traversal` (Imagination as Imaginary Traversal); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cited by: `proof:bk7_map_compatible_reciprocity` (Two-way fixed point as MAP Nash equilibrium); `proposition:bk7_map_compatible_reciprocity` (MAP-Compatible Reciprocity); `scholium:bk5_imagination_covenant_branch_selection` (Imagination as Covenant Branch Selection); `theorem:bk5_map_mad_mas_trichotomy` (MAD--MAP--MAS Trichotomy)
- Macros used: `\Membrane`

**Statement / Body**

Let $Membrane_A,Membrane_B$ interact through the symbolic covenant $C_{AB}$ (Cor. corollary:bk5_map_evolutionary_advantag), and let $C_{AB}$ be the induced linearized mutual-reflection operator on the joint tangent space, governing $X_{n+1}=C_{AB}X_n$ for the paired state $X=(psi_A,psi_B)$. Order the dyad by the reflective coupling stability parameter $Lambda_{AB}$ (Def. definition:bk5_reflective_coupling_stab) about its bifurcation manifold $Lambda_{AB}=1$ (Def. definition:bk5_symbolic_bifurcation_man). By the spectrum of $C_{AB}$ the dyad occupies one of three regimes:
\[
text{regime}(C_{AB})=text{regime}bigl(Spec(C_{AB})bigr).
\]
This spectrum is read on the enacted covenant branch: imagination may traverse counterfactual branches through imaginary or phase displacement (Scholium scholium:bk4_imagination_as_imaginary_traversal, Prop. proposition:bk4_imagination_bridges_wheel), but once a branch is enacted its regime is fixed by $C_{AB}$.


- MAD - Mutually Assured Destruction ($Omega_{AB}<0$): the covenant is antagonistic (zero-sum), the antisymmetric part of $C_{AB}$ dominates, and the spectrum is complex ($lambda=apm ib$, $bneq0$). Mutual reflection rotates without convergence - the retaliation spiral - and the relation dissolves.

- MAP - Mutually Assured Progress (the sustainable interior, balanced two-step memory closure): the spectrum is real with dominant eigenvalue the Golden Ratio $varphi$ (Thm. theorem:bk5_golden_ratio_spectral_invariant) on the non-diagonal $varphi{:}1$ eigendirection. The membranes co-evolve while remaining distinct.

- MAS - Mutually Assured Similarity (over-coupling $Lambda_{AB}gg1$, $Omega_{AB}gg0$): the symmetric (memoryless) part dominates, the spectrum is real, and the dominant eigendirection is the diagonal $(1,1)$. The membranes converge to a common state and their relative dynamics freeze - preservation without progress.

Destruction ($Omega_{AB}<0$) and similarity ($Omega_{AB}gg0$) are the opposing edges of the band; progress is the sustainable middle.

**Verbatim LaTeX Body**

```latex
\begin{definition}[The MAD--MAP--MAS Band]
\label{definition:bk5_map_mad_mas_band}
Let $\Membrane_A,\Membrane_B$ interact through the symbolic covenant $\mathcal{C}_{AB}$ (Cor.~\ref{corollary:bk5_map_evolutionary_advantag}), and let $\mathbf{C}_{AB}$ be the induced \emph{linearized mutual-reflection operator} on the joint tangent space, governing $X_{n+1}=\mathbf{C}_{AB}X_n$ for the paired state $X=(\psi_A,\psi_B)$. Order the dyad by the reflective coupling stability parameter $\Lambda_{AB}$ (Def.~\ref{definition:bk5_reflective_coupling_stab}) about its bifurcation manifold $\Lambda_{AB}=1$ (Def.~\ref{definition:bk5_symbolic_bifurcation_man}). By the spectrum of $\mathbf{C}_{AB}$ the dyad occupies one of three regimes:
\[
\text{regime}(\mathcal{C}_{AB})=\text{regime}\bigl(\operatorname{Spec}(\mathbf{C}_{AB})\bigr).
\]
This spectrum is read on the \emph{enacted} covenant branch: imagination may traverse counterfactual branches through imaginary or phase displacement (Scholium~\ref{scholium:bk4_imagination_as_imaginary_traversal}, Prop.~\ref{proposition:bk4_imagination_bridges_wheel}), but once a branch is enacted its regime is fixed by $\mathbf{C}_{AB}$.
\begin{itemize}
  \item \textbf{MAD} --- \emph{Mutually Assured Destruction} ($\Omega_{AB}<0$): the covenant is antagonistic (zero-sum), the antisymmetric part of $\mathbf{C}_{AB}$ dominates, and the spectrum is complex ($\lambda=a\pm ib$, $b\neq0$). Mutual reflection rotates without convergence --- the retaliation spiral --- and the relation dissolves.
  \item \textbf{MAP} --- \emph{Mutually Assured Progress} (the sustainable interior, balanced two-step memory closure): the spectrum is real with dominant eigenvalue the Golden Ratio $\varphi$ (Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}) on the non-diagonal $\varphi{:}1$ eigendirection. The membranes co-evolve while remaining distinct.
  \item \textbf{MAS} --- \emph{Mutually Assured Similarity} (over-coupling $\Lambda_{AB}\gg1$, $\Omega_{AB}\gg0$): the symmetric (memoryless) part dominates, the spectrum is real, and the dominant eigendirection is the diagonal $(1,1)$. The membranes converge to a common state and their relative dynamics freeze --- preservation without progress.
\end{itemize}
Destruction ($\Omega_{AB}<0$) and similarity ($\Omega_{AB}\gg0$) are the opposing edges of the band; progress is the sustainable middle.
\end{definition}
```

### MAD--MAP--MAS Trichotomy (`theorem:bk5_map_mad_mas_trichotomy`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:1992`

- Proof status: `proven`
- Depends on: `corollary:bk5_symbolic_eigenlife` (Symbolic Eigenlife); `definition:bk2_symbolic_phase_transitio` (Symbolic Phase Transition); `definition:bk5_map_mad_mas_band` (The MAD--MAP--MAS Band); `definition:bk5_reflective_coupling_stab` (Reflective Coupling Stability Parameter); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `definition:bk2_symbolic_phase_transitio` (Symbolic Phase Transition); `definition:bk5_map_mad_mas_band` (The MAD--MAP--MAS Band)
- Cited by: `proof:bk1_conditional_genericity_of_symbolic_phase_transitions` (Transversal discriminant crossing stabilized above the critical dimension); `proof:bk1_realization_of_symbolic_phase_transitions`; `proof:bk9_good_as_lyapunov_basin` (Lyapunov descent, threshold selection, and basin identity); `scholium:bk5_imagination_covenant_branch_selection` (Imagination as Covenant Branch Selection); `theorem:bk1_conditional_genericity_of_symbolic_phase_transitions` (Conditional Genericity of Symbolic Phase Transitions); `theorem:bk9_good_as_lyapunov_basin` (The Good as a Lyapunov Basin)
- Macros used: `\Membrane`

**Statement / Body**

For the mutual reflective dynamics $X_{n+1}=C_{AB}X_n$ (Def. definition:bk5_map_mad_mas_band), exactly one of three asymptotic behaviours obtains, selected by the covenant $Omega_{AB}$ through $Lambda_{AB}$:


- If $Omega_{AB}<0$, the dominant eigenvalues of $C_{AB}$ are complex with $|lambda|>1$; the joint free energy fails to stabilize, $lim_n F_s(Membrane_A^{(n)}cupMembrane_B^{(n)})=0$ at rate $propto|Omega_{AB}|$.

- At the balanced cooperative closure the dominant eigenvalue is real and equal to $varphi$ on a non-diagonal eigendirection; the dyad sustains $lim_n F_s(Membrane_A^{(n)}\!leftrightarrow\!Membrane_B^{(n)})>0$ with preserved distinctness.

- If $Omega_{AB}gg0$, the dominant eigendirection is the diagonal $(1,1)$ of norm $sqrt2$; the membranes converge to a common state, relative dynamics vanish ($DeltaSigmato0$), and $F_s$ is conserved at a frozen equilibrium.

$MAP$ is the unique sustainable regime. The $MAD\!to\!MAP$ boundary is a complex$to$real spectral transition (discriminant zero), a symbolic phase transition (Def. definition:bk2_symbolic_phase_transitio); the $MAP\!to\!MAS$ boundary is the rotation of the dominant eigendirection onto the diagonal. Destruction and similarity are the opposing edges of the band.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[MAD--MAP--MAS Trichotomy]
\label{theorem:bk5_map_mad_mas_trichotomy}
For the mutual reflective dynamics $X_{n+1}=\mathbf{C}_{AB}X_n$ (Def.~\ref{definition:bk5_map_mad_mas_band}), exactly one of three asymptotic behaviours obtains, selected by the covenant $\Omega_{AB}$ through $\Lambda_{AB}$:
\begin{enumerate}
  \item[\textbf{(MAD)}] If $\Omega_{AB}<0$, the dominant eigenvalues of $\mathbf{C}_{AB}$ are complex with $|\lambda|>1$; the joint free energy fails to stabilize, $\lim_n F_s(\Membrane_A^{(n)}\cup\Membrane_B^{(n)})=0$ at rate $\propto|\Omega_{AB}|$.
  \item[\textbf{(MAP)}] At the balanced cooperative closure the dominant eigenvalue is real and equal to $\varphi$ on a non-diagonal eigendirection; the dyad sustains $\lim_n F_s(\Membrane_A^{(n)}\!\leftrightarrow\!\Membrane_B^{(n)})>0$ with preserved distinctness.
  \item[\textbf{(MAS)}] If $\Omega_{AB}\gg0$, the dominant eigendirection is the diagonal $(1,1)$ of norm $\sqrt2$; the membranes converge to a common state, relative dynamics vanish ($\Delta\Sigma\to0$), and $F_s$ is conserved at a frozen equilibrium.
\end{enumerate}
$\mathrm{MAP}$ is the unique sustainable regime. The $\mathrm{MAD}\!\to\!\mathrm{MAP}$ boundary is a complex$\to$real spectral transition (discriminant zero), a symbolic phase transition (Def.~\ref{definition:bk2_symbolic_phase_transitio}); the $\mathrm{MAP}\!\to\!\mathrm{MAS}$ boundary is the rotation of the dominant eigendirection onto the diagonal. Destruction and similarity are the opposing edges of the band.
\end{theorem}
```

### proof:bk5_map_mad_mas_trichotomy (`proof:bk5_map_mad_mas_trichotomy`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2002`

- Proof status: `not_applicable`
- Depends on: `corollary:bk5_symbolic_eigenlife` (Symbolic Eigenlife); `definition:bk2_symbolic_phase_transitio` (Symbolic Phase Transition); `definition:bk5_reflective_coupling_stab` (Reflective Coupling Stability Parameter); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `corollary:bk5_symbolic_eigenlife` (Symbolic Eigenlife); `definition:bk2_symbolic_phase_transitio` (Symbolic Phase Transition); `definition:bk5_reflective_coupling_stab` (Reflective Coupling Stability Parameter); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cited by: none
- Macros used: `\Membrane`

**Statement / Body**

Linearize the mutual reflective dynamics about the joint fixed point; the coupling operator $C_{AB}$ acts on the two-membrane tangent space, its character fixed by the covenant orientation $Omega_{AB}$ through $Lambda_{AB}$ (Def. definition:bk5_reflective_coupling_stab). Split $C_{AB}=S+A$ into symmetric $S=tfrac12(C_{AB}+C_{AB}^{\!top})$ and antisymmetric $A=tfrac12(C_{AB}-C_{AB}^{\!top})$ parts, orthogonal under $langle X,Yrangle=tr(X^{\!top}Y)$ - the exact sense in which the two edges are opposite.

(MAD). For $Omega_{AB}<0$ the covenant is zero-sum and the antisymmetric part $A$ dominates. A real antisymmetric operator has purely imaginary spectrum, so $C_{AB}$ acquires complex eigenvalues $lambda=apm ib$ with $bneq0$; the iterates rotate and never settle to a common state. Antagonistic reflection amplifies rather than damps drift, so the joint free-energy derivative is negative (entropy production outpaces reflective restoration), giving $lim_n F_s(Membrane_A^{(n)}cupMembrane_B^{(n)})=0$ with collapse rate $propto|Omega_{AB}|$. This is destruction.

(MAP). At the balanced cooperative closure the coupling reduces to the two-step memory operator $big(1&1\\1&0big)$, whose unique positive eigenvalue is the Golden Ratio $varphi$ on the eigendirection $(varphi,1)$ (Thm. theorem:bk5_golden_ratio_spectral_invariant). This eigendirection is not the diagonal, so $Membrane_A$ and $Membrane_B$ co-evolve while remaining distinct; by the eigenlife criterion (Cor. corollary:bk5_symbolic_eigenlife) the $varphi$-mode is recursively stable, sustaining $F_s>0$. This is the one regime that both persists and preserves distinctness - progress.

(MAS). For $Omega_{AB}gg0$ the cooperative coupling saturates and the symmetric part $S$ dominates. A real symmetric operator has real spectrum, and as the coupling grows the dominant eigenvector rotates onto the diagonal $(1,1)$. The membranes converge to a common state, the relative coordinate decays, $DeltaSigmato0$, and the dyad freezes at the merged fixed point; the invariant of this limit is the diagonal norm $\|(1,1)\|=sqrt2$. Distinctness is lost - similarity, preservation without progress.

Boundaries and exhaustiveness. As $Omega_{AB}$ increases through zero the discriminant of the characteristic polynomial of $C_{AB}$ changes sign: a complex$to$real transition, hence a symbolic phase transition (Def. definition:bk2_symbolic_phase_transitio) at the $MAD\!to\!MAP$ boundary. Increasing $Omega_{AB}$ further rotates the dominant eigendirection continuously from the golden $varphi{:}1$ ray onto the diagonal - the $MAP\!to\!MAS$ boundary. Thus a sign or phase change in $Omega_{AB}$ is a boundary crossing of the enacted branch, not a change of convention. The sign of $Omega_{AB}$ together with the saturation of $Lambda_{AB}$ partitions the covenant axis into the three regimes, so they are mutually exclusive and exhaustive, with MAP the unique sustainable interior between the opposing edges of destruction and similarity.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_map_mad_mas_trichotomy}
\leavevmode
Linearize the mutual reflective dynamics about the joint fixed point; the coupling operator $\mathbf{C}_{AB}$ acts on the two-membrane tangent space, its character fixed by the covenant orientation $\Omega_{AB}$ through $\Lambda_{AB}$ (Def.~\ref{definition:bk5_reflective_coupling_stab}). Split $\mathbf{C}_{AB}=S+A$ into symmetric $S=\tfrac12(\mathbf{C}_{AB}+\mathbf{C}_{AB}^{\!\top})$ and antisymmetric $A=\tfrac12(\mathbf{C}_{AB}-\mathbf{C}_{AB}^{\!\top})$ parts, orthogonal under $\langle X,Y\rangle=\operatorname{tr}(X^{\!\top}Y)$ --- the exact sense in which the two edges are opposite.

\emph{(MAD).} For $\Omega_{AB}<0$ the covenant is zero-sum and the antisymmetric part $A$ dominates. A real antisymmetric operator has purely imaginary spectrum, so $\mathbf{C}_{AB}$ acquires complex eigenvalues $\lambda=a\pm ib$ with $b\neq0$; the iterates rotate and never settle to a common state. Antagonistic reflection amplifies rather than damps drift, so the joint free-energy derivative is negative (entropy production outpaces reflective restoration), giving $\lim_n F_s(\Membrane_A^{(n)}\cup\Membrane_B^{(n)})=0$ with collapse rate $\propto|\Omega_{AB}|$. This is destruction.

\emph{(MAP).} At the balanced cooperative closure the coupling reduces to the two-step memory operator $\big(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\big)$, whose unique positive eigenvalue is the Golden Ratio $\varphi$ on the eigendirection $(\varphi,1)$ (Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}). This eigendirection is not the diagonal, so $\Membrane_A$ and $\Membrane_B$ co-evolve while remaining distinct; by the eigenlife criterion (Cor.~\ref{corollary:bk5_symbolic_eigenlife}) the $\varphi$-mode is recursively stable, sustaining $F_s>0$. This is the one regime that both persists and preserves distinctness --- progress.

\emph{(MAS).} For $\Omega_{AB}\gg0$ the cooperative coupling saturates and the symmetric part $S$ dominates. A real symmetric operator has real spectrum, and as the coupling grows the dominant eigenvector rotates onto the diagonal $(1,1)$. The membranes converge to a common state, the relative coordinate decays, $\Delta\Sigma\to0$, and the dyad freezes at the merged fixed point; the invariant of this limit is the diagonal norm $\|(1,1)\|=\sqrt2$. Distinctness is lost --- similarity, preservation without progress.

\emph{Boundaries and exhaustiveness.} As $\Omega_{AB}$ increases through zero the discriminant of the characteristic polynomial of $\mathbf{C}_{AB}$ changes sign: a complex$\to$real transition, hence a symbolic phase transition (Def.~\ref{definition:bk2_symbolic_phase_transitio}) at the $\mathrm{MAD}\!\to\!\mathrm{MAP}$ boundary. Increasing $\Omega_{AB}$ further rotates the dominant eigendirection continuously from the golden $\varphi{:}1$ ray onto the diagonal --- the $\mathrm{MAP}\!\to\!\mathrm{MAS}$ boundary. Thus a sign or phase change in $\Omega_{AB}$ is a boundary crossing of the enacted branch, not a change of convention. The sign of $\Omega_{AB}$ together with the saturation of $\Lambda_{AB}$ partitions the covenant axis into the three regimes, so they are mutually exclusive and exhaustive, with MAP the unique sustainable interior between the opposing edges of destruction and similarity.
\end{proof}
```

### Imagination as Covenant Branch Selection (`scholium:bk5_imagination_covenant_branch_selection`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:2016`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_map_mad_mas_band` (The MAD--MAP--MAS Band); `proposition:bk4_imagination_bridges_wheel` (Imagination bridges the wheel); `scholium:bk4_imagination_as_imaginary_traversal` (Imagination as Imaginary Traversal); `theorem:bk5_map_mad_mas_trichotomy` (MAD--MAP--MAS Trichotomy)
- Cites: `definition:bk5_map_mad_mas_band` (The MAD--MAP--MAS Band); `proposition:bk4_imagination_bridges_wheel` (Imagination bridges the wheel); `scholium:bk4_imagination_as_imaginary_traversal` (Imagination as Imaginary Traversal); `theorem:bk5_map_mad_mas_trichotomy` (MAD--MAP--MAS Trichotomy)
- Cited by: `demonstratio:bk7_map_stable_mutual_fixed_point` (Mutual Reflective Fixed Point as Stable MAP Nash Point); `proof:bk7_map_compatible_reciprocity` (Two-way fixed point as MAP Nash equilibrium); `proof:bk9_pathologies_of_coherence` (Pathologies of Coherence); `proposition:bk7_map_compatible_reciprocity` (MAP-Compatible Reciprocity); `scholium:bk5_golden_rule_covenant` (The Golden Rule as a Recursive Covenant); `scholium:bk5_pi_at_mad_edge` (The Transcendence of Destruction: $\pi$ at the MAD Edge); `scholium:bk9_flexible_goal_calibration`
- Macros used: none

**Statement / Body**

Book IV identifies imagination as imaginary traversal rather than unreality: the observer moves through counterfactual phase directions that are not yet enacted in the real symbolic path (Scholium scholium:bk4_imagination_as_imaginary_traversal, Prop. proposition:bk4_imagination_bridges_wheel). In a dyadic covenant, that traversal is the observer-relative search over possible signs, phases, and coupling saturations of $C_{AB}$. It can preview MAD, MAP, and MAS branches before action. Once a branch is enacted, however, the trichotomy classifies it by spectrum (Def. definition:bk5_map_mad_mas_band, Thm. theorem:bk5_map_mad_mas_trichotomy). Thus imagination influences whether the dyad enters MAD, MAP, or MAS by selecting and stabilizing a branch; it does not override the spectral diagnosis of the branch actually chosen. A sign surprise in $Omega_{AB}$ or the emergence of an imaginary component is therefore a regime-boundary signal.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Imagination as Covenant Branch Selection]
\label{scholium:bk5_imagination_covenant_branch_selection}
Book~IV identifies imagination as imaginary traversal rather than unreality: the observer moves through counterfactual phase directions that are not yet enacted in the real symbolic path (Scholium~\ref{scholium:bk4_imagination_as_imaginary_traversal}, Prop.~\ref{proposition:bk4_imagination_bridges_wheel}). In a dyadic covenant, that traversal is the observer-relative search over possible signs, phases, and coupling saturations of $\mathbf{C}_{AB}$. It can preview MAD, MAP, and MAS branches before action. Once a branch is enacted, however, the trichotomy classifies it by spectrum (Def.~\ref{definition:bk5_map_mad_mas_band}, Thm.~\ref{theorem:bk5_map_mad_mas_trichotomy}). Thus imagination influences whether the dyad enters MAD, MAP, or MAS by selecting and stabilizing a branch; it does not override the spectral diagnosis of the branch actually chosen. A sign surprise in $\Omega_{AB}$ or the emergence of an imaginary component is therefore a regime-boundary signal.
\end{scholium}
```

### The Transcendence of Destruction: $\pi$ at the MAD Edge (`scholium:bk5_pi_at_mad_edge`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:2021`

- Proof status: `not_applicable`
- Depends on: `scholium:bk5_imagination_covenant_branch_selection` (Imagination as Covenant Branch Selection)
- Cites: `scholium:bk5_imagination_covenant_branch_selection` (Imagination as Covenant Branch Selection)
- Cited by: none
- Macros used: none

**Statement / Body**

In the branch-selection reading of Scholium scholium:bk5_imagination_covenant_branch_selection, the destructive branch is recognized by the same spectral sign that imagination may preview before enactment. The three regimes carry three constants in three roles. Progress is a growth rate: the eigenvalue $varphi$. Similarity is a merged magnitude: the diagonal norm $sqrt2$. Both are algebraic. Destruction alone is rotational: its complex eigenvalues $apm ib$ turn through an angle $theta=arg(a+ib)$ each step, so the spiral has period $2pi/theta$, and the constant of the regime is therefore $pi$ - the signature of rotation. It is transcendental precisely because destruction neither grows nor merges but turns: the retaliation that never closes. Thus $varphi$, $sqrt2$, and $pi$ index progress, similarity, and destruction not by numerology but by the kind of motion each regime is - the eigenvalue, the merged norm, and the angle of the spiral.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[The Transcendence of Destruction: $\pi$ at the MAD Edge]
\label{scholium:bk5_pi_at_mad_edge}
In the branch-selection reading of Scholium~\ref{scholium:bk5_imagination_covenant_branch_selection}, the destructive branch is recognized by the same spectral sign that imagination may preview before enactment. The three regimes carry three constants in three roles. Progress is a \emph{growth rate}: the eigenvalue $\varphi$. Similarity is a \emph{merged magnitude}: the diagonal norm $\sqrt2$. Both are algebraic. Destruction alone is \emph{rotational}: its complex eigenvalues $a\pm ib$ turn through an angle $\theta=\arg(a+ib)$ each step, so the spiral has period $2\pi/\theta$, and the constant of the regime is therefore $\pi$ --- the signature of rotation. It is transcendental precisely because destruction neither grows nor merges but \emph{turns}: the retaliation that never closes. Thus $\varphi$, $\sqrt2$, and $\pi$ index progress, similarity, and destruction not by numerology but by the kind of motion each regime is --- the eigenvalue, the merged norm, and the angle of the spiral.
\end{scholium}
```

### Curvature, Fuzzy Balance, and Symbolic Memory (`subsec:bk5_curvature_and_fuzzy_balance`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:2026`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Golden Ratio as Balanced Scale-Resonant Curvature Ratio (`theorem:bk5_golden_ratio_curvature_scalar`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:2031`

- Proof status: `proven`
- Depends on: `definition:bk4_symbolic_curvature` (Symbolic Curvature); `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `scholium:bk4_o_boundedness_unifying_principle` ($\mathcal{O}$-Boundedness as the Unifying Principle of Fuzzy Calculus); `theorem:bk4_fuzzy_fundamental` (Fuzzy Fundamental Theorem of Calculus); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `definition:bk4_symbolic_curvature` (Symbolic Curvature); `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `scholium:bk4_o_boundedness_unifying_principle` ($\mathcal{O}$-Boundedness as the Unifying Principle of Fuzzy Calculus); `theorem:bk4_fuzzy_fundamental` (Fuzzy Fundamental Theorem of Calculus)
- Cited by: `definition:bk6_symbolic_curvature_tensor` (Symbolic Curvature Tensor); `remark:bk5_curvature_vs_chaos` (Scale-Resonant Curvature vs Symbolic Chaos); `scholium:bk5_constant_of_becoming` (The Constant of Becoming)
- Macros used: none

**Statement / Body**

A fuzzy symbolic manifold $tilde{M}$ is balanced scale-resonant along
a growth path $gamma$ when the observer-resolved holonomy and curvature
distortion amplitudes
\[
h_n=\|H_{O,n}(gamma,f)\|,
k_n=\|kappa_{O,n}(f,int f)\|
\]
form the projective coordinates of a balanced two-step symbolic memory closure
(Def. definition:bk5_balanced_two_step_memory_closure), with $k_n>0$.
For every such balanced scale-resonant symbolic field $f$,
\[
lim_{ntoinfty}frac{h_n}{k_n}=varphi.
\]
Here $H_{O,n}$ and $kappa_{O,n}$ are the observer-relative terms from the Fuzzy
Fundamental Theorem of Calculus (Thm. theorem:bk4_fuzzy_fundamental), with
$kappa_O$ the symbolic curvature (Def. definition:bk4_symbolic_curvature)
arising as the second-order residue of $O$-bounded approximation
(Scholium scholium:bk4_o_boundedness_unifying_principle).

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Golden Ratio as Balanced Scale-Resonant Curvature Ratio]
\label{theorem:bk5_golden_ratio_curvature_scalar}
A fuzzy symbolic manifold $\tilde{M}$ is \textbf{balanced scale-resonant} along
a growth path $\gamma$ when the observer-resolved holonomy and curvature
distortion amplitudes
\[
h_n=\|H_{O,n}(\gamma,f)\|,\qquad
k_n=\|\kappa_{O,n}(f,\int f)\|
\]
form the projective coordinates of a balanced two-step symbolic memory closure
(Def.~\ref{definition:bk5_balanced_two_step_memory_closure}), with $k_n>0$.
For every such balanced scale-resonant symbolic field $f$,
\[
\lim_{n\to\infty}\frac{h_n}{k_n}=\varphi.
\]
Here $H_{O,n}$ and $\kappa_{O,n}$ are the observer-relative terms from the Fuzzy
Fundamental Theorem of Calculus (Thm.~\ref{theorem:bk4_fuzzy_fundamental}), with
$\kappa_O$ the symbolic curvature (Def.~\ref{definition:bk4_symbolic_curvature})
arising as the second-order residue of $\mathcal{O}$-bounded approximation
(Scholium~\ref{scholium:bk4_o_boundedness_unifying_principle}).
\end{theorem}
```

### Balanced curvature ratio (`proof:bk5_golden_ratio_curvature_scalar`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2053`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cited by: none
- Macros used: none

**Statement / Body**

By hypothesis, the pair $(h_n,k_n)^T$ is the projective state vector of the
balanced closure in Def. definition:bk5_balanced_two_step_memory_closure.
Thus it evolves, up to observer-normalized scale, by the same primitive matrix
\[
A=1&1\\1&0.
\]
Theorem theorem:bk5_golden_ratio_spectral_invariant gives the unique
positive Perron eigendirection of $A$. Solving
$A(h,k)^T=varphi(h,k)^T$ yields $h+k=varphi h$ and
$h=varphi k$, hence $h/k=varphi$. Perron-Frobenius convergence of
nonzero nonnegative iterates gives convergence of the projective coordinate
$h_n/k_n$ to that same ratio. Therefore the stable holonomy-to-curvature
distortion ratio of a balanced scale-resonant field is $varphi$.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Balanced curvature ratio]
\label{proof:bk5_golden_ratio_curvature_scalar}
\leavevmode

By hypothesis, the pair $(h_n,k_n)^T$ is the projective state vector of the
balanced closure in Def.~\ref{definition:bk5_balanced_two_step_memory_closure}.
Thus it evolves, up to observer-normalized scale, by the same primitive matrix
\[
A=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
Theorem~\ref{theorem:bk5_golden_ratio_spectral_invariant} gives the unique
positive Perron eigendirection of $A$.  Solving
$A(h,k)^T=\varphi(h,k)^T$ yields $h+k=\varphi h$ and
$h=\varphi k$, hence $h/k=\varphi$.  Perron--Frobenius convergence of
nonzero nonnegative iterates gives convergence of the projective coordinate
$h_n/k_n$ to that same ratio.  Therefore the stable holonomy-to-curvature
distortion ratio of a balanced scale-resonant field is $\varphi$.
\end{proof}
```

### The Constant of Becoming (`scholium:bk5_constant_of_becoming`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:2072`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `scholium:bk4_o_boundedness_unifying_principle` ($\mathcal{O}$-Boundedness as the Unifying Principle of Fuzzy Calculus); `theorem:bk5_golden_ratio_curvature_scalar` (Golden Ratio as Balanced Scale-Resonant Curvature Ratio)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk1_observer_horizon_structure` (Observer Horizon Structure); `scholium:bk4_o_boundedness_unifying_principle` ($\mathcal{O}$-Boundedness as the Unifying Principle of Fuzzy Calculus); `theorem:bk5_golden_ratio_curvature_scalar` (Golden Ratio as Balanced Scale-Resonant Curvature Ratio)
- Cited by: `scholium:bk9_golden_rule_thermodynamic_covenant` (The Golden Rule as a Thermodynamic Covenant)
- Macros used: none

**Statement / Body**

Theorem theorem:bk5_golden_ratio_curvature_scalar identifies $varphi$ as the curvature-memory ratio of observer-relative symbolic spacetime in the balanced scale-resonant regime. A bounded observer (Def. definition:bk1_bounded_observer) cannot differentiate and integrate its own state without introducing geometric error bounded by its horizon structure (Def. definition:bk1_observer_horizon_structure). The torsion term $kappa_O$ represents the local ``cost'' of parsing reality (differentiation)-it is the cross-error residue that $O$-bounded composition cannot eliminate (Scholium scholium:bk4_o_boundedness_unifying_principle)-while the holonomy term $H_O$ represents the cumulative ``cost'' of reconstructing a coherent history (integration). A system can persist as balanced scale-resonant when these two costs remain on the Perron eigendirection of the balanced memory closure.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[The Constant of Becoming]
\label{scholium:bk5_constant_of_becoming}
Theorem~\ref{theorem:bk5_golden_ratio_curvature_scalar} identifies $\varphi$ as the curvature-memory ratio of observer-relative symbolic spacetime in the balanced scale-resonant regime. A bounded observer (Def.~\ref{definition:bk1_bounded_observer}) cannot differentiate and integrate its own state without introducing geometric error bounded by its horizon structure (Def.~\ref{definition:bk1_observer_horizon_structure}). The torsion term $\kappa_O$ represents the local ``cost'' of parsing reality (differentiation)---it is the cross-error residue that $\mathcal{O}$-bounded composition cannot eliminate (Scholium~\ref{scholium:bk4_o_boundedness_unifying_principle})---while the holonomy term $H_O$ represents the cumulative ``cost'' of reconstructing a coherent history (integration). A system can persist as balanced scale-resonant when these two costs remain on the Perron eigendirection of the balanced memory closure.
\end{scholium}
```

### Symbolic Fibonacci Coding and Memory (`remark:bk5_symbolic_fibonacci_coding`)

Role: `remark` | Type: `remark` | Book: `book5` | Source: `book5.tex:2077`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cited by: `scholium:bk9_golden_rule_thermodynamic_covenant` (The Golden Rule as a Thermodynamic Covenant)
- Macros used: none

**Statement / Body**

The recurrence relation $a_{n+1}=a_n+a_{n-1}$ is precisely the scalar amplitude
form of balanced two-step symbolic memory
(Def. definition:bk5_balanced_two_step_memory_closure,
Thm. theorem:bk5_golden_ratio_spectral_invariant). It describes symbolic
life as emergent memory, where the present amplitude is constructed from current
persistence and one retained reflective state. Under reflective normalization
(i.e., maintaining a stable observer-resolved identity), the ratio of successive
amplitudes converges:
\[
lim_{n to infty} frac{a_{n+1}}{a_n} = varphi
\]
Life thus becomes a Fibonacci logic of symbolic retention exactly when the
observer-normalized memory weights are balanced; $varphi$ is the
asymptotic identity gradient of that regime.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Symbolic Fibonacci Coding and Memory]
\label{remark:bk5_symbolic_fibonacci_coding}
The recurrence relation $a_{n+1}=a_n+a_{n-1}$ is precisely the scalar amplitude
form of balanced two-step symbolic memory
(Def.~\ref{definition:bk5_balanced_two_step_memory_closure},
Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}).  It describes symbolic
life as emergent memory, where the present amplitude is constructed from current
persistence and one retained reflective state.  Under reflective normalization
(i.e., maintaining a stable observer-resolved identity), the ratio of successive
amplitudes converges:
\[
\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = \varphi
\]
Life thus becomes a Fibonacci logic of symbolic retention exactly when the
observer-normalized memory weights are balanced; $\varphi$ is the
\textbf{asymptotic identity gradient} of that regime.
\end{remark}
```

### Symbolic Thermoregulation and the Golden Mean (`subsec:bk5_thermoregulation_and_phi`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:2095`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Golden Ratio as Thermodynamic Optimum in the Balanced Regime (`proposition:bk5_golden_ratio_thermodynamic_optimum`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:2102`

- Proof status: `proven`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_metabolic_constraints_reflective_accuracy` (Metabolic Constraints on Reflective Accuracy)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_metabolic_constraints_reflective_accuracy` (Metabolic Constraints on Reflective Accuracy)
- Cited by: `scholium:bk5_experimental_predictions` (Experimental Predictions); `scholium:bk5_life_on_edge_of_chaos` (Life on the Edge of Chaos)
- Macros used: `\drift`, `\reflect`

**Statement / Body**

Let
\[
r=frac{W_{coh}}{W_{nov}}
\]
be the positive observer-resolved ratio of coherence-preserving work
(negentropy from Reflection, $reflect$) to novelty-generating exploration
(entropy from Drift, $drift$). In a balanced two-step metabolic regime, suppose
the free-energy contribution of this ratio is the spectral-misalignment
Lyapunov term
\[
F_{bal}(r)=F_0+alpha(log r-logvarphi)^2,
 alpha>0.
\]
Then $F_{bal}$ is minimized if and only if $r=varphi$
(cf. Def. definition:bk2_symbolic_free_energy,
Thm. theorem:bk5_metabolic_constraints_reflective_accuracy,
Thm. theorem:bk5_golden_ratio_spectral_invariant).

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Golden Ratio as Thermodynamic Optimum in the Balanced Regime]
\label{proposition:bk5_golden_ratio_thermodynamic_optimum}
Let
\[
r=\frac{W_{\mathrm{coh}}}{W_{\mathrm{nov}}}
\]
be the positive observer-resolved ratio of coherence-preserving work
(negentropy from Reflection, $\reflect$) to novelty-generating exploration
(entropy from Drift, $\drift$).  In a balanced two-step metabolic regime, suppose
the free-energy contribution of this ratio is the spectral-misalignment
Lyapunov term
\[
\mathcal{F}_{\mathrm{bal}}(r)=\mathcal{F}_0+\alpha(\log r-\log\varphi)^2,
\qquad \alpha>0.
\]
Then $\mathcal{F}_{\mathrm{bal}}$ is minimized if and only if $r=\varphi$
(cf.~Def.~\ref{definition:bk2_symbolic_free_energy},
Thm.~\ref{theorem:bk5_metabolic_constraints_reflective_accuracy},
Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}).
\end{proposition}
```

### Balanced thermodynamic optimum (`proof:bk5_golden_ratio_thermodynamic_optimum`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2123`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cited by: none
- Macros used: none

**Statement / Body**

Since $alpha>0$, the misalignment term
$alpha(log r-logvarphi)^2$ is nonnegative for every $r>0$ and vanishes
exactly when $log r=logvarphi$. The logarithm is injective on the positive
reals, so this occurs exactly at $r=varphi$. Therefore
$F_{bal}(r)geqF_0$, with equality if and only if
the work/exploration ratio lies on the balanced memory eigendirection selected
by Thm. theorem:bk5_golden_ratio_spectral_invariant.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Balanced thermodynamic optimum]
\label{proof:bk5_golden_ratio_thermodynamic_optimum}
\leavevmode

Since $\alpha>0$, the misalignment term
$\alpha(\log r-\log\varphi)^2$ is nonnegative for every $r>0$ and vanishes
exactly when $\log r=\log\varphi$.  The logarithm is injective on the positive
reals, so this occurs exactly at $r=\varphi$.  Therefore
$\mathcal{F}_{\mathrm{bal}}(r)\geq\mathcal{F}_0$, with equality if and only if
the work/exploration ratio lies on the balanced memory eigendirection selected
by Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}.
\end{proof}
```

### Fuzzy Symbolic Manifold (`definition:bk5_fuzzy_symbolic_manifold`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:2136`

- Proof status: `definitional`
- Depends on: `scholium:bk4_o_boundedness_unifying_principle` ($\mathcal{O}$-Boundedness as the Unifying Principle of Fuzzy Calculus); `theorem:bk4_fuzzy_fundamental` (Fuzzy Fundamental Theorem of Calculus)
- Cites: `scholium:bk4_o_boundedness_unifying_principle` ($\mathcal{O}$-Boundedness as the Unifying Principle of Fuzzy Calculus); `theorem:bk4_fuzzy_fundamental` (Fuzzy Fundamental Theorem of Calculus)
- Cited by: `definition:bk5_diagonal_transition` (Diagonal Transition); `definition:bk5_symbolic_integrability_class` (Symbolic Integrability Class); `definition:bk5_symbolic_torsion` (Symbolic Torsion); `lemma:bk6_power_scaling` (Power Scaling Law); `proof:bk6_power_scaling`
- Macros used: none

**Statement / Body**

A fuzzy symbolic manifold $tilde{M}$ is a discretized space where each point $p in tilde{M}$ exists within an observer-dependent resolution cell of radius $epsilon_O$. Symbolic transitions between points are governed by bounded rational approximations to underlying geometric relationships (cf. Thm. theorem:bk4_fuzzy_fundamental); these approximations remain sub-threshold at every compositional step by the $O$-boundedness principle (Scholium scholium:bk4_o_boundedness_unifying_principle).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Fuzzy Symbolic Manifold]
\label{definition:bk5_fuzzy_symbolic_manifold}
A fuzzy symbolic manifold $\tilde{M}$ is a discretized space where each point $p \in \tilde{M}$ exists within an observer-dependent resolution cell of radius $\epsilon_\mathcal{O}$. Symbolic transitions between points are governed by \textbf{bounded rational approximations} to underlying geometric relationships (cf.~Thm.~\ref{theorem:bk4_fuzzy_fundamental}); these approximations remain sub-threshold at every compositional step by the $\mathcal{O}$-boundedness principle (Scholium~\ref{scholium:bk4_o_boundedness_unifying_principle}).
\end{definition}
```

### Symbolic Torsion (`definition:bk5_symbolic_torsion`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:2141`

- Proof status: `definitional`
- Depends on: `definition:bk5_fuzzy_symbolic_manifold` (Fuzzy Symbolic Manifold)
- Cites: `definition:bk5_fuzzy_symbolic_manifold` (Fuzzy Symbolic Manifold)
- Cited by: `definition:bk5_collapse_resilience_test` (Symbolic Collapse Resilience Test)
- Macros used: none

**Statement / Body**

For an irrational constant $x$ and observer resolution $epsilon_O$, the symbolic torsion $T_x(epsilon_O)$ measures the irreducible complexity of representing $x$ within the bounded symbolic framework (cf. Def. definition:bk5_fuzzy_symbolic_manifold):
$$T_x(epsilon_O) = frac{log(text{denominator of best rational approximation within } epsilon_O)}{log(epsilon_O^{-1})}$$

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Torsion]
\label{definition:bk5_symbolic_torsion}
For an irrational constant $x$ and observer resolution $\epsilon_\mathcal{O}$, the symbolic torsion $\mathcal{T}_x(\epsilon_\mathcal{O})$ measures the \textbf{irreducible complexity} of representing $x$ within the bounded symbolic framework (cf.~Def.~\ref{definition:bk5_fuzzy_symbolic_manifold}):
$$\mathcal{T}_x(\epsilon_\mathcal{O}) = \frac{\log(\text{denominator of best rational approximation within } \epsilon_\mathcal{O})}{\log(\epsilon_\mathcal{O}^{-1})}$$
\end{definition}
```

### Diagonal Transition (`definition:bk5_diagonal_transition`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:2147`

- Proof status: `definitional`
- Depends on: `definition:bk5_fuzzy_symbolic_manifold` (Fuzzy Symbolic Manifold)
- Cites: `definition:bk5_fuzzy_symbolic_manifold` (Fuzzy Symbolic Manifold)
- Cited by: `lemma:bk5_shortest_path_representability` (Shortest Path Representability Criterion)
- Macros used: none

**Statement / Body**

In a fuzzy symbolic manifold with orthogonal basis vectors ${e_1, e_2, ldots}$, a diagonal transition is any symbolic path that cannot be decomposed into integer-aligned steps without introducing irrational scaling factors (cf. Def. definition:bk5_fuzzy_symbolic_manifold).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Diagonal Transition]
\label{definition:bk5_diagonal_transition}
In a fuzzy symbolic manifold with orthogonal basis vectors $\{e_1, e_2, \ldots\}$, a diagonal transition is any symbolic path that cannot be decomposed into integer-aligned steps without introducing irrational scaling factors (cf.~Def.~\ref{definition:bk5_fuzzy_symbolic_manifold}).
\end{definition}
```

### $\sqrt{2}$ as the First Orthogonal Fracture Constant (`theorem:bk5_sqrt2_maximal_fracture`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:2152`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: `lemma:bk5_shortest_path_representability` (Shortest Path Representability Criterion); `proof:bk5_complementary_constants` (Complementarity of first fracture and balanced resonance); `proposition:bk5_complementary_constants` (Complementary Constants: Fracture vs Resonance); `remark:bk5_curvature_vs_chaos` (Scale-Resonant Curvature vs Symbolic Chaos); `scholium:bk5_experimental_predictions` (Experimental Predictions); `theorem:bk5_fundamental_dichotomy` (Fundamental Dichotomy of Symbolic Constants)
- Macros used: none

**Statement / Body**

Let $tilde{M}$ have a local orthonormal symbolic frame
${e_1,ldots,e_d}$ whose observer-symbolic paths are generated by
axis-aligned unit steps. For every non-axis-aligned primitive lattice
transition $v=sum_i m_i e_i$ with $m_iinmathbb{Z}$ and at least two nonzero
coordinates,
\[
\|v\|_2geq sqrt{2}.
\]
Equality holds exactly for the elementary diagonal transitions
$v=pm e_ipm e_j$, $ineq j$. Consequently $sqrt{2}$ is the first
orthogonal fracture constant: the smallest Euclidean length at which a
geometrically direct transition cannot be represented as a single
axis-aligned symbolic step. For the elementary diagonal, the symbolic
axis-step length is $2$, the geometric length is $sqrt{2}$, and the
representability ratio is
\[
frac{L_{sym}}{L_2}=frac{2}{sqrt{2}}=sqrt{2}.
\]

**Verbatim LaTeX Body**

```latex
\begin{theorem}[$\sqrt{2}$ as the First Orthogonal Fracture Constant]
\label{theorem:bk5_sqrt2_maximal_fracture}
Let $\tilde{M}$ have a local orthonormal symbolic frame
$\{e_1,\ldots,e_d\}$ whose observer-symbolic paths are generated by
axis-aligned unit steps.  For every non-axis-aligned primitive lattice
transition $v=\sum_i m_i e_i$ with $m_i\in\mathbb{Z}$ and at least two nonzero
coordinates,
\[
\|v\|_2\geq \sqrt{2}.
\]
Equality holds exactly for the elementary diagonal transitions
$v=\pm e_i\pm e_j$, $i\neq j$.  Consequently $\sqrt{2}$ is the first
orthogonal fracture constant: the smallest Euclidean length at which a
geometrically direct transition cannot be represented as a single
axis-aligned symbolic step.  For the elementary diagonal, the symbolic
axis-step length is $2$, the geometric length is $\sqrt{2}$, and the
representability ratio is
\[
\frac{L_{\mathrm{sym}}}{L_2}=\frac{2}{\sqrt{2}}=\sqrt{2}.
\]
\end{theorem}
```

### First orthogonal fracture (`proof:bk5_sqrt2_maximal_fracture`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2174`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Let $v=sum_i m_i e_i$ be a primitive lattice transition with at least two
nonzero integer coordinates. Since each nonzero coordinate has
$|m_i|geq 1$, the Euclidean norm satisfies
\[
\|v\|_2^2=sum_i m_i^2geq 1^2+1^2=2,
\]
and hence $\|v\|_2geqsqrt{2}$. Equality requires exactly two nonzero
coordinates and both must have absolute value $1$, so
$v=pm e_ipm e_j$ for distinct $i,j$.

For such an elementary diagonal, the direct geometric transition has length
$sqrt{2}$. An axis-generated symbolic path cannot realize it in one symbolic
unit step, because every one-step generator is one of the frame vectors
$pm e_i$. The shortest axis-generated symbolic decomposition uses two unit
steps, $pm e_i$ and $pm e_j$, so $L_{sym}=2$. Thus the
observer-visible representability ratio is $2/sqrt{2}=sqrt{2}$.
Thus $sqrt{2}$ is the exact first fracture constant forced by orthogonal
discretization.

**Verbatim LaTeX Body**

```latex
\begin{proof}[First orthogonal fracture]
\label{proof:bk5_sqrt2_maximal_fracture}
\leavevmode

Let $v=\sum_i m_i e_i$ be a primitive lattice transition with at least two
nonzero integer coordinates.  Since each nonzero coordinate has
$|m_i|\geq 1$, the Euclidean norm satisfies
\[
\|v\|_2^2=\sum_i m_i^2\geq 1^2+1^2=2,
\]
and hence $\|v\|_2\geq\sqrt{2}$.  Equality requires exactly two nonzero
coordinates and both must have absolute value $1$, so
$v=\pm e_i\pm e_j$ for distinct $i,j$.

For such an elementary diagonal, the direct geometric transition has length
$\sqrt{2}$.  An axis-generated symbolic path cannot realize it in one symbolic
unit step, because every one-step generator is one of the frame vectors
$\pm e_i$.  The shortest axis-generated symbolic decomposition uses two unit
steps, $\pm e_i$ and $\pm e_j$, so $L_{\mathrm{sym}}=2$.  Thus the
observer-visible representability ratio is $2/\sqrt{2}=\sqrt{2}$.
Thus $\sqrt{2}$ is the exact first fracture constant forced by orthogonal
discretization.
\end{proof}
```

### Complementary Constants: Fracture vs Resonance (`proposition:bk5_complementary_constants`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:2198`

- Proof status: `proven`
- Depends on: `definition:bk4_fragmented_identity` (Fragmented Identity); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cites: `definition:bk4_fragmented_identity` (Fragmented Identity); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cited by: `theorem:bk5_fundamental_dichotomy` (Fundamental Dichotomy of Symbolic Constants)
- Macros used: none

**Statement / Body**

Formally this pairs Thm. theorem:bk5_sqrt2_maximal_fracture with Thm. theorem:bk5_golden_ratio_spectral_invariant.
In fuzzy symbolic calculus, $sqrt{2}$ and $varphi$ serve complementary roles:
- $sqrt{2}$ marks the first symbolic fracture forced by orthogonal incommensurability (cf. Def. definition:bk4_fragmented_identity)
- $varphi$ marks the positive resonant ratio selected by balanced recursive memory

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Complementary Constants: Fracture vs Resonance]
\label{proposition:bk5_complementary_constants}
Formally this pairs Thm.~\ref{theorem:bk5_sqrt2_maximal_fracture} with Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}.
In fuzzy symbolic calculus, $\sqrt{2}$ and $\varphi$ serve complementary roles:
- $\sqrt{2}$ marks the first \textbf{symbolic fracture} forced by orthogonal incommensurability (cf.~Def.~\ref{definition:bk4_fragmented_identity})
- $\varphi$ marks the positive \textbf{resonant ratio} selected by balanced recursive memory
\end{proposition}
```

### Complementarity of first fracture and balanced resonance (`proof:bk5_complementary_constants`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2206`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cites: `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cited by: none
- Macros used: none

**Statement / Body**

Theorem theorem:bk5_golden_ratio_spectral_invariant proves that
$varphi$ is the positive Perron ratio of balanced two-step memory; it is
therefore a resonance constant for recursive retention. Theorem theorem:bk5_sqrt2_maximal_fracture
proves that $sqrt{2}$ is the first non-axis-aligned length forced by an
orthogonal symbolic frame; it is therefore a fracture constant for geometric
representation. These mechanisms are complementary because the former arises
from temporal recursion in the memory state $(a_n,a_{n-1})$, while the latter
arises from spatial incompatibility between a direct Euclidean diagonal and an
axis-generated symbolic path.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Complementarity of first fracture and balanced resonance]
\label{proof:bk5_complementary_constants}

\leavevmode

Theorem~\ref{theorem:bk5_golden_ratio_spectral_invariant} proves that
$\varphi$ is the positive Perron ratio of balanced two-step memory; it is
therefore a resonance constant for recursive retention.  Theorem~\ref{theorem:bk5_sqrt2_maximal_fracture}
proves that $\sqrt{2}$ is the first non-axis-aligned length forced by an
orthogonal symbolic frame; it is therefore a fracture constant for geometric
representation.  These mechanisms are complementary because the former arises
from temporal recursion in the memory state $(a_n,a_{n-1})$, while the latter
arises from spatial incompatibility between a direct Euclidean diagonal and an
axis-generated symbolic path.
\end{proof}
```

### Scale-Resonant Curvature vs Symbolic Chaos (`remark:bk5_curvature_vs_chaos`)

Role: `remark` | Type: `remark` | Book: `book5` | Source: `book5.tex:2222`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_golden_ratio_curvature_scalar` (Golden Ratio as Balanced Scale-Resonant Curvature Ratio); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cites: `theorem:appC_phi_as_spectral_radius` (Spectral Radius of $G$ Equals $\varphi$); `theorem:appC_phi_from_lagrangian` (Emergence of $\varphi$ from Lagrangian Equilibrium); `theorem:bk5_golden_ratio_curvature_scalar` (Golden Ratio as Balanced Scale-Resonant Curvature Ratio); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cited by: `scholium:bk9_golden_rule_thermodynamic_covenant` (The Golden Rule as a Thermodynamic Covenant)
- Macros used: none

**Statement / Body**

Manifolds whose holonomy and curvature amplitudes realize the balanced memory
closure exhibit scale-resonant curvature: the holonomy-to-curvature
ratio remains stable at $varphi$ across scales
(cf. Thm. theorem:bk5_golden_ratio_curvature_scalar). Manifolds
encountering $sqrt{2}$ transitions exhibit symbolic fracture when the
axis-generated representation must pay the elementary diagonal gap
(cf. Thm. theorem:bk5_sqrt2_maximal_fracture). That $varphi$
plays the resonant role is not accidental: it is the Perron fixed ratio of
balanced recursive memory (Thm. theorem:bk5_golden_ratio_spectral_invariant;
cf. Thm. theorem:appC_phi_from_lagrangian,
Thm. theorem:appC_phi_as_spectral_radius).

**Verbatim LaTeX Body**

```latex
\begin{remark}[Scale-Resonant Curvature vs Symbolic Chaos]
\label{remark:bk5_curvature_vs_chaos}
Manifolds whose holonomy and curvature amplitudes realize the balanced memory
closure exhibit \textbf{scale-resonant curvature}: the holonomy-to-curvature
ratio remains stable at $\varphi$ across scales
(cf.~Thm.~\ref{theorem:bk5_golden_ratio_curvature_scalar}).  Manifolds
encountering $\sqrt{2}$ transitions exhibit \textbf{symbolic fracture} when the
axis-generated representation must pay the elementary diagonal gap
(cf.~Thm.~\ref{theorem:bk5_sqrt2_maximal_fracture}).  That $\varphi$
plays the resonant role is not accidental: it is the Perron fixed ratio of
balanced recursive memory (Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant};
cf.~Thm.~\ref{theorem:appC_phi_from_lagrangian},
Thm.~\ref{theorem:appC_phi_as_spectral_radius}).
\end{remark}
```

### Symbolic Collapse Resilience Test (`definition:bk5_collapse_resilience_test`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:2237`

- Proof status: `definitional`
- Depends on: `definition:bk4_collapse_of_symbolic_ide` (Collapse of Symbolic Identity); `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk5_symbolic_torsion` (Symbolic Torsion); `remark:bk4_ttpr_entropy` (Relation to Symbolic Thermodynamics); `theorem:bk4_test_time_differentiation_c` (Test-Time Differentiation Collapse); `theorem:bk4_ttpr_symbolic_stability` (Symbolic Stability via Precision Refinement)
- Cites: `definition:bk4_collapse_of_symbolic_ide` (Collapse of Symbolic Identity); `definition:bk4_test_time_coherent_sampling` (Test-Time Coherent Sampling (TTCS)); `definition:bk5_symbolic_torsion` (Symbolic Torsion); `remark:bk4_ttpr_entropy` (Relation to Symbolic Thermodynamics); `theorem:bk4_test_time_differentiation_c` (Test-Time Differentiation Collapse); `theorem:bk4_ttpr_symbolic_stability` (Symbolic Stability via Precision Refinement)
- Cited by: `scholium:bk5_experimental_predictions` (Experimental Predictions); `theorem:bk5_fundamental_dichotomy` (Fundamental Dichotomy of Symbolic Constants)
- Macros used: none

**Statement / Body**

Given a fuzzy symbolic system with resolution parameter $epsilon$, collapse resilience measures how long symbolic coherence persists under iterative approximation errors when representing an irrational constant (cf. Def. definition:bk5_symbolic_torsion, Def. definition:bk4_collapse_of_symbolic_ide, Thm. theorem:bk4_test_time_differentiation_c, Def. definition:bk4_test_time_coherent_sampling, Thm. theorem:bk4_ttpr_symbolic_stability, Rem. remark:bk4_ttpr_entropy).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Collapse Resilience Test]
\label{definition:bk5_collapse_resilience_test}
Given a fuzzy symbolic system with resolution parameter $\epsilon$, \textbf{collapse resilience} measures how long symbolic coherence persists under iterative approximation errors when representing an irrational constant (cf.~Def.~\ref{definition:bk5_symbolic_torsion}, Def.~\ref{definition:bk4_collapse_of_symbolic_ide}, Thm.~\ref{theorem:bk4_test_time_differentiation_c}, Def.~\ref{definition:bk4_test_time_coherent_sampling}, Thm.~\ref{theorem:bk4_ttpr_symbolic_stability}, Rem.~\ref{remark:bk4_ttpr_entropy}).
\end{definition}
```

### Experimental Predictions (`scholium:bk5_experimental_predictions`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:2242`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_collapse_resilience_test` (Symbolic Collapse Resilience Test); `proposition:bk5_golden_ratio_thermodynamic_optimum` (Golden Ratio as Thermodynamic Optimum in the Balanced Regime); `scholium:bk4_ttdc_impulse_collapse` (Collapse as Impulse: The Newtonian Structure of TTDC); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cites: `definition:bk5_collapse_resilience_test` (Symbolic Collapse Resilience Test); `proposition:bk5_golden_ratio_thermodynamic_optimum` (Golden Ratio as Thermodynamic Optimum in the Balanced Regime); `scholium:bk4_ttdc_impulse_collapse` (Collapse as Impulse: The Newtonian Structure of TTDC); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cited by: none
- Macros used: none

**Statement / Body**

The simulation should demonstrate the following behaviors.
See Def. definition:bk5_collapse_resilience_test,
Thm. theorem:bk5_sqrt2_maximal_fracture,
Prop. proposition:bk5_golden_ratio_thermodynamic_optimum, and
Scholium scholium:bk4_ttdc_impulse_collapse.


- $sqrt{2}$ appears as the first nonzero representability ratio for elementary diagonal transitions.

- $varphi$ maintains stable balanced-memory ratios across multiple scales.

- Systems mixing diagonal fracture with balanced memory should show a measurable separation between spatial representability cost and recursive memory resonance.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Experimental Predictions]
\label{scholium:bk5_experimental_predictions}
The simulation should demonstrate the following behaviors.
See Def.~\ref{definition:bk5_collapse_resilience_test},
Thm.~\ref{theorem:bk5_sqrt2_maximal_fracture},
Prop.~\ref{proposition:bk5_golden_ratio_thermodynamic_optimum}, and
Scholium~\ref{scholium:bk4_ttdc_impulse_collapse}.
\begin{enumerate}
  \item $\sqrt{2}$ appears as the first nonzero representability ratio for elementary diagonal transitions.
  \item $\varphi$ maintains stable balanced-memory ratios across multiple scales.
  \item Systems mixing diagonal fracture with balanced memory should show a measurable separation between spatial representability cost and recursive memory resonance.
\end{enumerate}
\end{scholium}
```

### Fundamental Dichotomy of Symbolic Constants (`theorem:bk5_fundamental_dichotomy`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:2256`

- Proof status: `argued_demonstratio`
- Depends on: `definition:bk5_collapse_resilience_test` (Symbolic Collapse Resilience Test); `proposition:bk5_complementary_constants` (Complementary Constants: Fracture vs Resonance); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cites: `definition:bk5_collapse_resilience_test` (Symbolic Collapse Resilience Test); `proposition:bk5_complementary_constants` (Complementary Constants: Fracture vs Resonance); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cited by: `demonstratio:bk5_diagonal_dissociation` (The Diagonal Dissociation Principle); `theorem:bk5_fundamental_norm_fracture` (Fundamental Theorem of Norm-Induced Symbolic Fracture)
- Macros used: none

**Statement / Body**

In fuzzy symbolic calculus, the constants $varphi$ and $sqrt{2}$ instantiate two fundamental mechanisms:
- Resonant constants (exemplified by $varphi$) selected by balanced recursive memory
- Fracture constants (exemplified by $sqrt{2}$) forced by irreducible orthogonal incompatibility

This dichotomy reflects the deep structure of symbolic representation under bounded observation (cf. Def. definition:bk5_collapse_resilience_test, Prop. proposition:bk5_complementary_constants, Thm. theorem:bk5_golden_ratio_spectral_invariant, Thm. theorem:bk5_sqrt2_maximal_fracture).

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Fundamental Dichotomy of Symbolic Constants]
\label{theorem:bk5_fundamental_dichotomy}
In fuzzy symbolic calculus, the constants $\varphi$ and $\sqrt{2}$ instantiate two fundamental mechanisms:
- \textbf{Resonant constants} (exemplified by $\varphi$) selected by balanced recursive memory
- \textbf{Fracture constants} (exemplified by $\sqrt{2}$) forced by irreducible orthogonal incompatibility

This dichotomy reflects the deep structure of symbolic representation under bounded observation (cf.~Def.~\ref{definition:bk5_collapse_resilience_test}, Prop.~\ref{proposition:bk5_complementary_constants}, Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}, Thm.~\ref{theorem:bk5_sqrt2_maximal_fracture}).
\end{theorem}
```

### The Diagonal Dissociation Principle (`demonstratio:bk5_diagonal_dissociation`)

Role: `demonstration` | Type: `demonstratio` | Book: `book5` | Source: `book5.tex:2265`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_fundamental_dichotomy` (Fundamental Dichotomy of Symbolic Constants)
- Cites: `theorem:bk5_fundamental_dichotomy` (Fundamental Dichotomy of Symbolic Constants)
- Cited by: none
- Macros used: none

**Statement / Body**

Where $varphi$ emerges from the recursive equation $x = 1 + 1/x$ (self-similarity), $sqrt{2}$ emerges from the Pythagorean equation $x^2 = 1^2 + 1^2$ (orthogonal combination). This geometric distinction translates directly into symbolic behavior: recursion enables compression, while orthogonality demands expansion (cf. Thm. theorem:bk5_fundamental_dichotomy).

The irrationality of $sqrt{2}$ is not merely a number-theoretic accident; in an orthonormal symbolic frame, it is the symbolic signature of the first dimensional incommensurability.

**Verbatim LaTeX Body**

```latex
\begin{demonstratio}[The Diagonal Dissociation Principle]
\label{demonstratio:bk5_diagonal_dissociation}
Where $\varphi$ emerges from the recursive equation $x = 1 + 1/x$ (self-similarity), $\sqrt{2}$ emerges from the Pythagorean equation $x^2 = 1^2 + 1^2$ (orthogonal combination). This geometric distinction translates directly into symbolic behavior: recursion enables compression, while orthogonality demands expansion (cf.~Thm.~\ref{theorem:bk5_fundamental_dichotomy}).

The irrationality of $\sqrt{2}$ is not merely a number-theoretic accident; in an orthonormal symbolic frame, it is the \textbf{symbolic signature} of the first dimensional incommensurability.
\end{demonstratio}
```

### Life on the Edge of Chaos (`scholium:bk5_life_on_edge_of_chaos`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:2272`

- Proof status: `not_applicable`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `proposition:bk5_golden_ratio_thermodynamic_optimum` (Golden Ratio as Thermodynamic Optimum in the Balanced Regime)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `proposition:bk5_golden_ratio_thermodynamic_optimum` (Golden Ratio as Thermodynamic Optimum in the Balanced Regime)
- Cited by: `corollary:bk9_freedomentropy_complementarity` (Freedom-Entropy Complementarity)
- Macros used: none

**Statement / Body**

Symbolic life must navigate the narrow path between two forms of death: the rigid, frozen order of perfect coherence (stasis) and the dissipative, unbounded expansion of pure drift (chaos). In the balanced metabolic regime, the minimization of Symbolic Free Energy selects the Perron ratio of the drift-reflection memory closure (cf. Def. definition:bk2_symbolic_free_energy, Prop. proposition:bk5_golden_ratio_thermodynamic_optimum). The Golden Ratio, $varphi$, is therefore the edge-of-chaos ratio for that regime: it is the proportion at which novelty-generating Drift and coherence-preserving Reflection lie on the same balanced memory eigendirection.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Life on the Edge of Chaos]
\label{scholium:bk5_life_on_edge_of_chaos}
Symbolic life must navigate the narrow path between two forms of death: the rigid, frozen order of perfect coherence (stasis) and the dissipative, unbounded expansion of pure drift (chaos). In the balanced metabolic regime, the minimization of Symbolic Free Energy selects the Perron ratio of the drift-reflection memory closure (cf.~Def.~\ref{definition:bk2_symbolic_free_energy}, Prop.~\ref{proposition:bk5_golden_ratio_thermodynamic_optimum}). The Golden Ratio, $\varphi$, is therefore the edge-of-chaos ratio for that regime: it is the proportion at which novelty-generating Drift and coherence-preserving Reflection lie on the same balanced memory eigendirection.
\end{scholium}
```

### Norm-Induced Fracture and \texorpdfstring{$\ell_p$ (`section:book5.tex:2277`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:2277`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Integrability Class (`definition:bk5_symbolic_integrability_class`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:2280`

- Proof status: `definitional`
- Depends on: `definition:bk5_fuzzy_symbolic_manifold` (Fuzzy Symbolic Manifold)
- Cites: `definition:bk5_fuzzy_symbolic_manifold` (Fuzzy Symbolic Manifold)
- Cited by: none
- Macros used: none

**Statement / Body**

A fuzzy symbolic manifold $tilde{M}$ belongs to symbolic integrability class $I_p$ if its dominant geometric transitions are governed by the $ell_p$ norm (cf. Def. definition:bk5_fuzzy_symbolic_manifold), where symbolic paths of length $delta$ satisfy:
$$\|vec{v}\|_p = left(sum_{i=1}^n |v_i|^pright)^{1/p} leq delta + epsilon_O$$
for observer resolution $epsilon_O$. The class $I_p$ determines the symbolic decomposability of transitions within $tilde{M}$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Integrability Class]
\label{definition:bk5_symbolic_integrability_class}
A fuzzy symbolic manifold $\tilde{M}$ belongs to \textbf{symbolic integrability class} $\mathcal{I}_p$ if its dominant geometric transitions are governed by the $\ell_p$ norm (cf.~Def.~\ref{definition:bk5_fuzzy_symbolic_manifold}), where symbolic paths of length $\delta$ satisfy:
$$\|\vec{v}\|_p = \left(\sum_{i=1}^n |v_i|^p\right)^{1/p} \leq \delta + \epsilon_\mathcal{O}$$
for observer resolution $\epsilon_\mathcal{O}$. The class $\mathcal{I}_p$ determines the \textbf{symbolic decomposability} of transitions within $\tilde{M}$.
\end{definition}
```

### Symbolic Curvature Control Parameter (`definition:bk5_symbolic_curvature_control`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:2287`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `definition:bk5_symbolic_curvature_operator_spectrum` (Symbolic Curvature Operator Spectrum)
- Macros used: none

**Statement / Body**

For a nonzero transition $vec{v}$ with support
$supp(vec{v})={i:v_ineq0}$ and
$s(vec{v})=|supp(vec{v})|$, the symbolic curvature
control parameter in class $I_p$ is
\[
kappa_p(vec{v})=frac{\|vec{v}\|_1}{\|vec{v}\|_p}-1, 1leq pleqinfty.
\]
Here $\|vec{v}\|_1$ is the axis-generated symbolic length and $\|vec{v}\|_p$
is the geometric length in the dominant norm. Thus $kappa_p$ measures the
extra axis-symbolic cost paid to represent a geometrically shorter transition.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Curvature Control Parameter]
\label{definition:bk5_symbolic_curvature_control}
For a nonzero transition $\vec{v}$ with support
$\operatorname{supp}(\vec{v})=\{i:v_i\neq0\}$ and
$s(\vec{v})=|\operatorname{supp}(\vec{v})|$, the \textbf{symbolic curvature
control parameter} in class $\mathcal{I}_p$ is
\[
\kappa_p(\vec{v})=\frac{\|\vec{v}\|_1}{\|\vec{v}\|_p}-1,\qquad 1\leq p\leq\infty.
\]
Here $\|\vec{v}\|_1$ is the axis-generated symbolic length and $\|\vec{v}\|_p$
is the geometric length in the dominant norm.  Thus $\kappa_p$ measures the
extra axis-symbolic cost paid to represent a geometrically shorter transition.
\end{definition}
```

### \(\ell_p\)-Norm Fracture Hierarchy (`theorem:bk5_lp_norm_fracture_hierarchy`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:2301`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: `definition:bk5_symbolic_compression_experiment` (Symbolic Compression Experiment); `proof:bk5_complete_symbolic_regime_classification` (Regime classification); `proof:bk5_fractal_dimension_connection` (Effective support dimension); `proof:bk5_fundamental_norm_fracture` (Norm-induced fracture theorem); `proof:bk5_shortest_path_representability` (Representability Proof); `proof:bk5_symbolic_integrability_classes` (Classification Proof); `proof:bk5_symbolic_norm_spectrum` (Product spectrum); `proof:bk5_symbolic_torsion_phase_diagram` (Phase diagram from the fracture ratio); `proposition:bk5_symbolic_integrability_classes` (Symbolic Integrability Classes); `remark:bk5_lattice_field_theory_analogy` (Lattice Field Theory Analogy); `theorem:bk5_fundamental_norm_fracture` (Fundamental Theorem of Norm-Induced Symbolic Fracture); `theorem:bk5_symbolic_norm_spectrum` (Symbolic Norm Spectrum)
- Macros used: none

**Statement / Body**

For every nonzero transition $vec{v}$ in a fuzzy symbolic manifold and every
$1leq pleqinfty$,
\[
1leq frac{\|vec{v}\|_1}{\|vec{v}\|_p}
leq s(vec{v})^{1-1/p}.
\]
The upper bound is attained exactly when all nonzero coordinates of
$vec{v}$ have equal magnitude. Consequently, for the elementary diagonal
$vec{v}=e_i+e_j$,
\[
frac{\|vec{v}\|_1}{\|vec{v}\|_1}=1,
frac{\|vec{v}\|_1}{\|vec{v}\|_2}=sqrt{2},
frac{\|vec{v}\|_1}{\|vec{v}\|_infty}=2.
\]
Thus $ell_1$ is perfectly axis-integrable, $ell_2$ introduces the first
orthogonal fracture ratio $sqrt{2}$, and $ell_infty$ collapses all
coordinate distribution inside the support to its largest coordinate.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[\(\ell_p\)-Norm Fracture Hierarchy]
\label{theorem:bk5_lp_norm_fracture_hierarchy}
For every nonzero transition $\vec{v}$ in a fuzzy symbolic manifold and every
$1\leq p\leq\infty$,
\[
1\leq \frac{\|\vec{v}\|_1}{\|\vec{v}\|_p}
\leq s(\vec{v})^{1-1/p}.
\]
The upper bound is attained exactly when all nonzero coordinates of
$\vec{v}$ have equal magnitude.  Consequently, for the elementary diagonal
$\vec{v}=e_i+e_j$,
\[
\frac{\|\vec{v}\|_1}{\|\vec{v}\|_1}=1,\qquad
\frac{\|\vec{v}\|_1}{\|\vec{v}\|_2}=\sqrt{2},\qquad
\frac{\|\vec{v}\|_1}{\|\vec{v}\|_\infty}=2.
\]
Thus $\ell_1$ is perfectly axis-integrable, $\ell_2$ introduces the first
orthogonal fracture ratio $\sqrt{2}$, and $\ell_\infty$ collapses all
coordinate distribution inside the support to its largest coordinate.
\end{theorem}
```

### Norm inequality proof (`proof:bk5_lp_norm_fracture_hierarchy`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2322`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The lower bound follows from the standard monotonicity
$\|vec{v}\|_pleq\|vec{v}\|_1$ for $pgeq1$. For the upper bound, restrict
to the support of $vec{v}$ and apply Hölder's inequality:
\[
\|vec{v}\|_1
=sum_{iinsupp(vec{v})}|v_i|
leq s(vec{v})^{1-1/p}left(sum_i |v_i|^pright)^{1/p}
=s(vec{v})^{1-1/p}\|vec{v}\|_p.
\]
Dividing by $\|vec{v}\|_p$ gives the claimed bound. Equality in Hölder
occurs exactly when the nonzero magnitudes $|v_i|$ are all equal. Substituting
$vec{v}=e_i+e_j$ gives $\|vec{v}\|_1=2$, $\|vec{v}\|_2=sqrt{2}$, and
$\|vec{v}\|_infty=1$, hence the three displayed ratios.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Norm inequality proof]
\label{proof:bk5_lp_norm_fracture_hierarchy}
\leavevmode

The lower bound follows from the standard monotonicity
$\|\vec{v}\|_p\leq\|\vec{v}\|_1$ for $p\geq1$.  For the upper bound, restrict
to the support of $\vec{v}$ and apply Hölder's inequality:
\[
\|\vec{v}\|_1
=\sum_{i\in\operatorname{supp}(\vec{v})}|v_i|
\leq s(\vec{v})^{1-1/p}\left(\sum_i |v_i|^p\right)^{1/p}
=s(\vec{v})^{1-1/p}\|\vec{v}\|_p.
\]
Dividing by $\|\vec{v}\|_p$ gives the claimed bound.  Equality in Hölder
occurs exactly when the nonzero magnitudes $|v_i|$ are all equal.  Substituting
$\vec{v}=e_i+e_j$ gives $\|\vec{v}\|_1=2$, $\|\vec{v}\|_2=\sqrt{2}$, and
$\|\vec{v}\|_\infty=1$, hence the three displayed ratios.
\end{proof}
```

### Symbolic Integrability Classes (`proposition:bk5_symbolic_integrability_classes`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:2341`

- Proof status: `proven`
- Depends on: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: `proof:bk5_complete_symbolic_regime_classification` (Regime classification); `theorem:bk5_fundamental_norm_fracture` (Fundamental Theorem of Norm-Induced Symbolic Fracture)
- Macros used: none

**Statement / Body**

Fuzzy symbolic manifolds can be rigorously classified into three fundamental integrability classes (cf. Thm. theorem:bk5_lp_norm_fracture_hierarchy):

- Class $I_1$: Symbolically Reducible - geometric and axis-symbolic lengths agree.
- Class $I_2$: Symbolically Fractured - elementary orthogonal diagonals carry ratio $sqrt{2}$.
- Class $I_infty$: Support-Collapsed - length depends only on the largest coordinate, so distribution inside the support is lost.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Symbolic Integrability Classes]
\label{proposition:bk5_symbolic_integrability_classes}
Fuzzy symbolic manifolds can be rigorously classified into three fundamental integrability classes (cf.~Thm.~\ref{theorem:bk5_lp_norm_fracture_hierarchy}):

- \textbf{Class $\mathcal{I}_1$}: \textbf{Symbolically Reducible} - geometric and axis-symbolic lengths agree.
- \textbf{Class $\mathcal{I}_2$}: \textbf{Symbolically Fractured} - elementary orthogonal diagonals carry ratio $\sqrt{2}$.
- \textbf{Class $\mathcal{I}_\infty$}: \textbf{Support-Collapsed} - length depends only on the largest coordinate, so distribution inside the support is lost.
\end{proposition}
```

### Classification Proof (`proof:bk5_symbolic_integrability_classes`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2350`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: none
- Macros used: none

**Statement / Body**

In $I_1$, $\|vec{v}\|_1/\|vec{v}\|_1=1$, so
$kappa_1(vec{v})=0$ for every nonzero transition. In $I_2$,
Thm. theorem:bk5_lp_norm_fracture_hierarchy gives the elementary
diagonal ratio $\|vec{v}\|_1/\|vec{v}\|_2=sqrt{2}$, so
$kappa_2(e_i+e_j)=sqrt{2}-1>0$. In $I_infty$,
$\|vec{v}\|_infty=max_i |v_i|$; therefore transitions with different
coordinate distributions can share the same geometric length. The class is
support-collapsed because only the largest coordinate survives in the norm,
while the axis-symbolic cost remains sensitive to the whole support.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Classification Proof]
\label{proof:bk5_symbolic_integrability_classes}
\leavevmode

In $\mathcal{I}_1$, $\|\vec{v}\|_1/\|\vec{v}\|_1=1$, so
$\kappa_1(\vec{v})=0$ for every nonzero transition.  In $\mathcal{I}_2$,
Thm.~\ref{theorem:bk5_lp_norm_fracture_hierarchy} gives the elementary
diagonal ratio $\|\vec{v}\|_1/\|\vec{v}\|_2=\sqrt{2}$, so
$\kappa_2(e_i+e_j)=\sqrt{2}-1>0$.  In $\mathcal{I}_\infty$,
$\|\vec{v}\|_\infty=\max_i |v_i|$; therefore transitions with different
coordinate distributions can share the same geometric length.  The class is
support-collapsed because only the largest coordinate survives in the norm,
while the axis-symbolic cost remains sensitive to the whole support.
\end{proof}
```

### Symbolic Torsion Phase Diagram (`theorem:bk5_symbolic_torsion_phase_diagram`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:2366`

- Proof status: `proven`
- Depends on: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: none
- Cited by: `scholium:bk5_critical_point_p2` (Critical Point at p=2)
- Macros used: none

**Statement / Body**

For an equal-magnitude transition with support size $sgeq1$, the symbolic
fracture parameter is
\[
kappa_p(s)=s^{1-1/p}-1, 1leq pleqinfty.
\]
Thus
\[
kappa_1(s)=0,
kappa_2(2)=sqrt{2}-1,
kappa_infty(s)=s-1.
\]
For fixed finite support, fracture is finite and monotone in $p$; divergence
occurs only along unbounded support size $stoinfty$.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Symbolic Torsion Phase Diagram]
\label{theorem:bk5_symbolic_torsion_phase_diagram}
For an equal-magnitude transition with support size $s\geq1$, the symbolic
fracture parameter is
\[
\kappa_p(s)=s^{1-1/p}-1,\qquad 1\leq p\leq\infty.
\]
Thus
\[
\kappa_1(s)=0,\qquad
\kappa_2(2)=\sqrt{2}-1,\qquad
\kappa_\infty(s)=s-1.
\]
For fixed finite support, fracture is finite and monotone in $p$; divergence
occurs only along unbounded support size $s\to\infty$.
\end{theorem}
```

### Phase diagram from the fracture ratio (`proof:bk5_symbolic_torsion_phase_diagram`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2383`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: none
- Macros used: none

**Statement / Body**

For an equal-magnitude transition with support size $s$, equality holds in
Thm. theorem:bk5_lp_norm_fracture_hierarchy, so
$\|vec{v}\|_1/\|vec{v}\|_p=s^{1-1/p}$. Subtracting $1$ gives
$kappa_p(s)=s^{1-1/p}-1$. The displayed special cases follow by substituting
$p=1$, $(p,s)=(2,2)$, and $p=infty$. Since $1-1/p$ is monotone increasing
in $p$, $kappa_p(s)$ is monotone in $p$ for fixed $s$; since
$kappa_infty(s)=s-1$, unbounded growth requires $stoinfty$.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Phase diagram from the fracture ratio]
\label{proof:bk5_symbolic_torsion_phase_diagram}
\leavevmode

For an equal-magnitude transition with support size $s$, equality holds in
Thm.~\ref{theorem:bk5_lp_norm_fracture_hierarchy}, so
$\|\vec{v}\|_1/\|\vec{v}\|_p=s^{1-1/p}$.  Subtracting $1$ gives
$\kappa_p(s)=s^{1-1/p}-1$.  The displayed special cases follow by substituting
$p=1$, $(p,s)=(2,2)$, and $p=\infty$.  Since $1-1/p$ is monotone increasing
in $p$, $\kappa_p(s)$ is monotone in $p$ for fixed $s$; since
$\kappa_\infty(s)=s-1$, unbounded growth requires $s\to\infty$.
\end{proof}
```

### Critical Point at p=2 (`scholium:bk5_critical_point_p2`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:2396`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_symbolic_torsion_phase_diagram` (Symbolic Torsion Phase Diagram)
- Cites: `theorem:bk5_symbolic_torsion_phase_diagram` (Symbolic Torsion Phase Diagram)
- Cited by: none
- Macros used: none

**Statement / Body**

The Euclidean norm $p = 2$ is the first familiar geometric regime in which an
elementary orthogonal diagonal has nonzero axis-symbolic fracture
(cf. Thm. theorem:bk5_symbolic_torsion_phase_diagram). This is not
coincidental: it reflects the fundamental role of orthogonality in geometric
representation. The emergence of $sqrt{2}$ at this point marks the first
unit-square diagonal representability ratio.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Critical Point at p=2]
\label{scholium:bk5_critical_point_p2}
The Euclidean norm $p = 2$ is the first familiar geometric regime in which an
elementary orthogonal diagonal has nonzero axis-symbolic fracture
(cf.~Thm.~\ref{theorem:bk5_symbolic_torsion_phase_diagram}). This is not
coincidental: it reflects the fundamental role of orthogonality in geometric
representation. The emergence of $\sqrt{2}$ at this point marks the first
unit-square diagonal representability ratio.
\end{scholium}
```

### Shortest Path Representability Criterion (`lemma:bk5_shortest_path_representability`)

Role: `lemma` | Type: `lemma` | Book: `book5` | Source: `book5.tex:2406`

- Proof status: `proven`
- Depends on: `definition:bk5_diagonal_transition` (Diagonal Transition); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cites: `definition:bk5_diagonal_transition` (Diagonal Transition); `theorem:bk5_sqrt2_maximal_fracture` ($\sqrt{2}$ as the First Orthogonal Fracture Constant)
- Cited by: `proof:bk5_shortest_path_representability` (Representability Proof)
- Macros used: none

**Statement / Body**

Symbolic fracture arises precisely when the geometrically shortest transition
has smaller $ell_p$ length than every axis-generated symbolic path realizing
the same endpoint (cf. Def. definition:bk5_diagonal_transition,
Thm. theorem:bk5_sqrt2_maximal_fracture).

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Shortest Path Representability Criterion]
\label{lemma:bk5_shortest_path_representability}
Symbolic fracture arises precisely when the geometrically shortest transition
has smaller $\ell_p$ length than every axis-generated symbolic path realizing
the same endpoint (cf.~Def.~\ref{definition:bk5_diagonal_transition},
Thm.~\ref{theorem:bk5_sqrt2_maximal_fracture}).
\end{lemma}
```

### Representability Proof (`proof:bk5_shortest_path_representability`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2414`

- Proof status: `not_applicable`
- Depends on: `lemma:bk5_shortest_path_representability` (Shortest Path Representability Criterion); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `lemma:bk5_shortest_path_representability` (Shortest Path Representability Criterion); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: `corollary:bk5_symbolic_decoherence_theory` (Symbolic Decoherence Theory); `proof:bk5_symbolic_decoherence_theory`
- Macros used: none

**Statement / Body**

Consider transition $(0,0) to (n,n)$ for integer $n$.
See Lem. lemma:bk5_shortest_path_representability and Thm. theorem:bk5_lp_norm_fracture_hierarchy.

Axis-aligned path: $(0,0) to (n,0) to (n,n)$


- Length: $ell_1 = 2n$

- Symbolic representation: $n cdot (1,0) + n cdot (0,1)$ checkmark\ Representable

Diagonal path: $(0,0) to (n,n)$ directly


- Length: $ell_2 = nsqrt{2}$

- Symbolic representation: $n cdot left(frac{1}{sqrt{2}}, frac{1}{sqrt{2}}right)$ $times$ Non-representable

The representability gap is:
\[
Delta = ell_1 - ell_2 = 2n - nsqrt{2} = n(2 - sqrt{2}) approx 0.586n
\]

This gap quantifies the symbolic decoherence — the cost of forcing geometric optimality into symbolic constraints.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Representability Proof]
\label{proof:bk5_shortest_path_representability}
\leavevmode

Consider transition $(0,0) \to (n,n)$ for integer $n$.
See Lem.~\ref{lemma:bk5_shortest_path_representability} and Thm.~\ref{theorem:bk5_lp_norm_fracture_hierarchy}.

\textbf{Axis-aligned path}: $(0,0) \to (n,0) \to (n,n)$
\begin{itemize}
  \item Length: $\ell_1 = 2n$
  \item Symbolic representation: $n \cdot (1,0) + n \cdot (0,1)$ \quad \checkmark\ Representable
\end{itemize}

\textbf{Diagonal path}: $(0,0) \to (n,n)$ directly
\begin{itemize}
  \item Length: $\ell_2 = n\sqrt{2}$
  \item Symbolic representation: $n \cdot \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ \quad $\times$ Non-representable
\end{itemize}

The \textbf{representability gap} is:
\[
\Delta = \ell_1 - \ell_2 = 2n - n\sqrt{2} = n(2 - \sqrt{2}) \approx 0.586n
\]

This gap quantifies the \textbf{symbolic decoherence} — the cost of forcing geometric optimality into symbolic constraints.
\end{proof}
```

### Symbolic Decoherence Theory (`corollary:bk5_symbolic_decoherence_theory`)

Role: `corollary` | Type: `corollary` | Book: `book5` | Source: `book5.tex:2441`

- Proof status: `proven`
- Depends on: `proof:bk5_shortest_path_representability` (Representability Proof)
- Cites: `proof:bk5_shortest_path_representability` (Representability Proof)
- Cited by: `theorem:bk5_fundamental_norm_fracture` (Fundamental Theorem of Norm-Induced Symbolic Fracture)
- Macros used: `\drift`

**Statement / Body**

The symbolic decoherence $drift$ of a transition is the excess
axis-symbolic cost over geometric optimality (cf. Prf. proof:bk5_shortest_path_representability):
$$drift(vec{v}) = \|vec{v}\|_{text{symbolic}} - \|vec{v}\|_{text{geometric}}$$
where $\|vec{v}\|_{text{symbolic}}$ is the length of the shortest symbolically representable path.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Symbolic Decoherence Theory]
\label{corollary:bk5_symbolic_decoherence_theory}
The \textbf{symbolic decoherence} $\drift$ of a transition is the excess
axis-symbolic cost over geometric optimality (cf.~Prf.~\ref{proof:bk5_shortest_path_representability}):
$$\drift(\vec{v}) = \|\vec{v}\|_{\text{symbolic}} - \|\vec{v}\|_{\text{geometric}}$$
where $\|\vec{v}\|_{\text{symbolic}}$ is the length of the shortest symbolically representable path.
\end{corollary}
```

### proof:bk5_symbolic_decoherence_theory (`proof:bk5_symbolic_decoherence_theory`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2448`

- Proof status: `not_applicable`
- Depends on: `proof:bk5_shortest_path_representability` (Representability Proof)
- Cites: `proof:bk5_shortest_path_representability` (Representability Proof)
- Cited by: none
- Macros used: `\drift`

**Statement / Body**

The symbolic decoherence is well-defined and nonnegative. By the shortest-path representability analysis (Prf. proof:bk5_shortest_path_representability) the symbolically representable paths between two configurations are a proper subset of all geometric paths: a symbolic path is constrained to axis-representable steps, whereas the geometric optimum (the Euclidean geodesic) need not be representable. Minimizing a length functional over a smaller admissible set cannot yield a shorter optimum, so $\|vec v\|_{text{symbolic}}ge\|vec v\|_{text{geometric}}$, and therefore
\[
drift(vec v)=\|vec v\|_{text{symbolic}}-\|vec v\|_{text{geometric}}ge 0
\]
is a well-defined, nonnegative excess. It vanishes exactly when the geometric optimum is itself symbolically representable, and is otherwise strictly positive - the representability gap computed there, e.g.\ $Delta=n(2-sqrt2)$ for the diagonal transition. Thus $drift$ measures precisely the cost of forcing geometric optimality through symbolic constraints.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_symbolic_decoherence_theory}
\leavevmode
The symbolic decoherence is well-defined and nonnegative. By the shortest-path representability analysis (Prf.~\ref{proof:bk5_shortest_path_representability}) the symbolically representable paths between two configurations are a proper subset of all geometric paths: a symbolic path is constrained to axis-representable steps, whereas the geometric optimum (the Euclidean geodesic) need not be representable. Minimizing a length functional over a smaller admissible set cannot yield a shorter optimum, so $\|\vec v\|_{\text{symbolic}}\ge\|\vec v\|_{\text{geometric}}$, and therefore
\[
\drift(\vec v)=\|\vec v\|_{\text{symbolic}}-\|\vec v\|_{\text{geometric}}\ge 0
\]
is a well-defined, nonnegative excess. It vanishes exactly when the geometric optimum is itself symbolically representable, and is otherwise strictly positive --- the representability gap computed there, e.g.\ $\Delta=n(2-\sqrt2)$ for the diagonal transition. Thus $\drift$ measures precisely the cost of forcing geometric optimality through symbolic constraints.
\end{proof}
```

### Lattice Field Theory Analogy (`remark:bk5_lattice_field_theory_analogy`)

Role: `remark` | Type: `remark` | Book: `book5` | Source: `book5.tex:2458`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: none
- Macros used: none

**Statement / Body**

The transition from $ell_1$ to $ell_2$ geometry mirrors the continuum limit in lattice field theory (cf. Thm. theorem:bk5_lp_norm_fracture_hierarchy):
- Discrete lattice ($ell_1$): perfect symbolic integrability, but geometric distortion.
- Continuum limit ($ell_2$): geometric accuracy, but elementary diagonal fracture.
- Renormalization: the ratio $sqrt{2}$ measures the first unit-square cost of replacing axis traversal by Euclidean diagonal traversal.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Lattice Field Theory Analogy]
\label{remark:bk5_lattice_field_theory_analogy}
The transition from $\ell_1$ to $\ell_2$ geometry mirrors the \textbf{continuum limit} in lattice field theory (cf.~Thm.~\ref{theorem:bk5_lp_norm_fracture_hierarchy}):
- \textbf{Discrete lattice} ($\ell_1$): perfect symbolic integrability, but geometric distortion.
- \textbf{Continuum limit} ($\ell_2$): geometric accuracy, but elementary diagonal fracture.
- \textbf{Renormalization}: the ratio $\sqrt{2}$ measures the first unit-square cost of replacing axis traversal by Euclidean diagonal traversal.
\end{remark}
```

### Effective Support-Dimension Diagnostic (`proposition:bk5_fractal_dimension_connection`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:2466`

- Proof status: `proven`
- Depends on: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

For an equal-magnitude transition $vec{v}$ with support size
$s=s(vec{v})geq2$, define its effective support dimension at norm exponent
$p$ by
\[
D_{eff}(p,s)
=1+frac{logleft(\|vec{v}\|_1/\|vec{v}\|_pright)}{log s}.
\]
Then
\[
D_{eff}(p,s)=2-frac{1}{p},
D_{eff}(1,s)=1,
D_{eff}(2,s)=frac32,
D_{eff}(infty,s)=2.
\]
For support size $s=1$, the transition is axis-integrable and the effective
dimension is defined to be $D_{eff}=1$.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Effective Support-Dimension Diagnostic]
\label{proposition:bk5_fractal_dimension_connection}
For an equal-magnitude transition $\vec{v}$ with support size
$s=s(\vec{v})\geq2$, define its effective support dimension at norm exponent
$p$ by
\[
D_{\mathrm{eff}}(p,s)
=1+\frac{\log\left(\|\vec{v}\|_1/\|\vec{v}\|_p\right)}{\log s}.
\]
Then
\[
D_{\mathrm{eff}}(p,s)=2-\frac{1}{p},\qquad
D_{\mathrm{eff}}(1,s)=1,\qquad
D_{\mathrm{eff}}(2,s)=\frac32,\qquad
D_{\mathrm{eff}}(\infty,s)=2.
\]
For support size $s=1$, the transition is axis-integrable and the effective
dimension is defined to be $D_{\mathrm{eff}}=1$.
\end{proposition}
```

### Effective support dimension (`proof:bk5_fractal_dimension_connection`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2486`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: none
- Macros used: none

**Statement / Body**

For equal-magnitude support size $s$, equality holds in
Thm. theorem:bk5_lp_norm_fracture_hierarchy, so
\[
frac{\|vec{v}\|_1}{\|vec{v}\|_p}=s^{1-1/p}.
\]
Substitution into the definition gives
\[
D_{eff}(p,s)
=1+frac{log(s^{1-1/p})}{log s}
=1+left(1-frac1pright)
=2-frac1p.
\]
The displayed special cases follow by evaluating at $p=1$, $p=2$, and
$p=infty$. When $s=1$, $log s=0$, so the formula is not used; the transition
is a single-axis transition with no support expansion, and the diagnostic is
defined as $1$.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Effective support dimension]
\label{proof:bk5_fractal_dimension_connection}
\leavevmode

For equal-magnitude support size $s$, equality holds in
Thm.~\ref{theorem:bk5_lp_norm_fracture_hierarchy}, so
\[
\frac{\|\vec{v}\|_1}{\|\vec{v}\|_p}=s^{1-1/p}.
\]
Substitution into the definition gives
\[
D_{\mathrm{eff}}(p,s)
=1+\frac{\log(s^{1-1/p})}{\log s}
=1+\left(1-\frac1p\right)
=2-\frac1p.
\]
The displayed special cases follow by evaluating at $p=1$, $p=2$, and
$p=\infty$.  When $s=1$, $\log s=0$, so the formula is not used; the transition
is a single-axis transition with no support expansion, and the diagnostic is
defined as $1$.
\end{proof}
```

### Symbolic Compression Experiment (`definition:bk5_symbolic_compression_experiment`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:2508`

- Proof status: `definitional`
- Depends on: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: `definition:bk5_symbolic_regime_detection` (Symbolic Regime Detection Experiment)
- Macros used: none

**Statement / Body**

To test the $ell_p$-fracture theory, design an experiment measuring symbolic compression ratio (cf. Thm. theorem:bk5_lp_norm_fracture_hierarchy):
$$R_p = frac{text{Length of symbolic encoding}}{text{Length of geometric path}}$$
for various $p$ values. The theory predicts:
- $R_1 = 1$ (perfect compression)
- $R_2 = sqrt{2}$ (minimal fracture)
- $R_infty = s(vec{v})$ for equal-magnitude transitions with support size $s(vec{v})$

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Compression Experiment]
\label{definition:bk5_symbolic_compression_experiment}
To test the $\ell_p$-fracture theory, design an experiment measuring \textbf{symbolic compression ratio} (cf.~Thm.~\ref{theorem:bk5_lp_norm_fracture_hierarchy}):
$$R_p = \frac{\text{Length of symbolic encoding}}{\text{Length of geometric path}}$$
for various $p$ values. The theory predicts:
- $R_1 = 1$ (perfect compression)
- $R_2 = \sqrt{2}$ (minimal fracture)
- $R_\infty = s(\vec{v})$ for equal-magnitude transitions with support size $s(\vec{v})$
\end{definition}
```

### Fundamental Theorem of Norm-Induced Symbolic Fracture (`theorem:bk5_fundamental_norm_fracture`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:2518`

- Proof status: `proven`
- Depends on: `corollary:bk5_symbolic_decoherence_theory` (Symbolic Decoherence Theory); `proposition:bk5_symbolic_integrability_classes` (Symbolic Integrability Classes); `theorem:bk5_fundamental_dichotomy` (Fundamental Dichotomy of Symbolic Constants); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `corollary:bk5_symbolic_decoherence_theory` (Symbolic Decoherence Theory); `proposition:bk5_symbolic_integrability_classes` (Symbolic Integrability Classes); `theorem:bk5_fundamental_dichotomy` (Fundamental Dichotomy of Symbolic Constants); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: `definition:bk6_symbolic_bifurcation` (Symbolic Bifurcation); `demonstratio:bk5_geometry_symbol_unity` (The Deep Unity of Geometry and Symbol); `remark:bk5_open_questions` (Open Questions); `theorem:bk5_grand_unified_symbolic_geometric` (Product Theorem of the Symbolic-Geometric Interface)
- Macros used: none

**Statement / Body**

In any fuzzy symbolic manifold $tilde{M}$ with axis-generated symbolic paths,
norm-induced symbolic fracture is governed by the ratio
$\|vec{v}\|_1/\|vec{v}\|_p$ (cf. Prop. proposition:bk5_symbolic_integrability_classes,
Cor. corollary:bk5_symbolic_decoherence_theory,
Thm. theorem:bk5_lp_norm_fracture_hierarchy,
Thm. theorem:bk5_fundamental_dichotomy):

1. Symbolic integrability is exact under $ell_1$ geometry.
2. Symbolic fracture emerges under $ell_2$ geometry for every transition with support size at least $2$.
3. Support collapse appears under $ell_infty$ geometry, where length remembers only the largest coordinate.

The constant $sqrt{2}$ is the elementary two-coordinate fracture ratio, while
$varphi$ remains the balanced recursive-memory resonance ratio from
Thm. theorem:bk5_golden_ratio_spectral_invariant.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Fundamental Theorem of Norm-Induced Symbolic Fracture]
\label{theorem:bk5_fundamental_norm_fracture}
In any fuzzy symbolic manifold $\tilde{M}$ with axis-generated symbolic paths,
norm-induced symbolic fracture is governed by the ratio
$\|\vec{v}\|_1/\|\vec{v}\|_p$ (cf.~Prop.~\ref{proposition:bk5_symbolic_integrability_classes},
Cor.~\ref{corollary:bk5_symbolic_decoherence_theory},
Thm.~\ref{theorem:bk5_lp_norm_fracture_hierarchy},
Thm.~\ref{theorem:bk5_fundamental_dichotomy}):

1. \textbf{Symbolic integrability} is exact under $\ell_1$ geometry.
2. \textbf{Symbolic fracture} emerges under $\ell_2$ geometry for every transition with support size at least $2$.
3. \textbf{Support collapse} appears under $\ell_\infty$ geometry, where length remembers only the largest coordinate.

The constant $\sqrt{2}$ is the elementary two-coordinate fracture ratio, while
$\varphi$ remains the balanced recursive-memory resonance ratio from
Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}.
\end{theorem}
```

### Norm-induced fracture theorem (`proof:bk5_fundamental_norm_fracture`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2536`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: none
- Macros used: none

**Statement / Body**

Theorem theorem:bk5_lp_norm_fracture_hierarchy proves that the ratio
$\|vec{v}\|_1/\|vec{v}\|_p$ is the controlling quantity. When $p=1$, this
ratio is identically $1$, so there is no fracture. When $p=2$ and
$s(vec{v})geq2$, the upper-bound case for an elementary diagonal gives the
first nontrivial ratio $sqrt{2}$. When $p=infty$, the denominator is
$max_i |v_i|$, so all coordinate information below the maximum is invisible to
the geometric length; this is support collapse. The final sentence follows by
combining the elementary fracture result with the balanced-memory spectral
result of Thm. theorem:bk5_golden_ratio_spectral_invariant.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Norm-induced fracture theorem]
\label{proof:bk5_fundamental_norm_fracture}
\leavevmode

Theorem~\ref{theorem:bk5_lp_norm_fracture_hierarchy} proves that the ratio
$\|\vec{v}\|_1/\|\vec{v}\|_p$ is the controlling quantity.  When $p=1$, this
ratio is identically $1$, so there is no fracture.  When $p=2$ and
$s(\vec{v})\geq2$, the upper-bound case for an elementary diagonal gives the
first nontrivial ratio $\sqrt{2}$.  When $p=\infty$, the denominator is
$\max_i |v_i|$, so all coordinate information below the maximum is invisible to
the geometric length; this is support collapse.  The final sentence follows by
combining the elementary fracture result with the balanced-memory spectral
result of Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}.
\end{proof}
```

### The Deep Unity of Geometry and Symbol (`demonstratio:bk5_geometry_symbol_unity`)

Role: `demonstration` | Type: `demonstratio` | Book: `book5` | Source: `book5.tex:2551`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_fundamental_norm_fracture` (Fundamental Theorem of Norm-Induced Symbolic Fracture)
- Cites: `theorem:bk5_fundamental_norm_fracture` (Fundamental Theorem of Norm-Induced Symbolic Fracture)
- Cited by: none
- Macros used: none

**Statement / Body**

This analysis reveals that the crisis of symbolic representation is not merely a computational issue, but reflects a fundamental tension between discrete symbolic logic and continuous geometric reality (cf. Thm. theorem:bk5_fundamental_norm_fracture).

The parameter $p$ in $ell_p$ norms controls the degree of geometric realism the symbolic system attempts to capture:
- Low $p$: Symbolic purity, geometric distortion
- High $p$: Geometric accuracy, symbolic chaos

The Euclidean point $p = 2$ is where the elementary unit-square diagonal first
registers as $sqrt{2}$ against the axis-symbolic length $2$. This is why
$sqrt{2}$ emerges as the minimal fracture constant: it marks the first
non-axis-aligned cost of geometric realism in symbolic systems.

**Verbatim LaTeX Body**

```latex
\begin{demonstratio}[The Deep Unity of Geometry and Symbol]
\label{demonstratio:bk5_geometry_symbol_unity}
This analysis reveals that the \textbf{crisis of symbolic representation} is not merely a computational issue, but reflects a fundamental tension between \textbf{discrete symbolic logic} and \textbf{continuous geometric reality} (cf.~Thm.~\ref{theorem:bk5_fundamental_norm_fracture}).

The parameter $p$ in $\ell_p$ norms controls the \textbf{degree of geometric realism} the symbolic system attempts to capture:
- Low $p$: Symbolic purity, geometric distortion
- High $p$: Geometric accuracy, symbolic chaos

The Euclidean point $p = 2$ is where the elementary unit-square diagonal first
registers as $\sqrt{2}$ against the axis-symbolic length $2$.  This is why
$\sqrt{2}$ emerges as the \textbf{minimal fracture constant}: it marks the first
non-axis-aligned cost of geometric realism in symbolic systems.
\end{demonstratio}
```

### Open Questions (`remark:bk5_open_questions`)

Role: `remark` | Type: `remark` | Book: `book5` | Source: `book5.tex:2565`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_fundamental_norm_fracture` (Fundamental Theorem of Norm-Induced Symbolic Fracture)
- Cites: `theorem:bk5_fundamental_norm_fracture` (Fundamental Theorem of Norm-Induced Symbolic Fracture)
- Cited by: none
- Macros used: none

**Statement / Body**

This framework raises several open questions
(cf. Thm. theorem:bk5_fundamental_norm_fracture):

1. Quantum Geometric Encoding: Do quantum systems naturally operate in specific $ell_p$ regimes? Could quantum coherence correspond to symbolic integrability classes?

2. Information Theoretic Bounds: Can we establish fundamental limits on symbolic compression based on the underlying geometric structure?

3. Cognitive Symbolic Processing: Do biological cognitive systems exhibit $ell_p$-dependent symbolic processing regimes? Is there a natural norm for symbolic cognition?

4. Computational Complexity: How does the computational complexity of symbolic operations scale with the $ell_p$ parameter? Is there a complexity phase transition at $p = 2$?

**Verbatim LaTeX Body**

```latex
\begin{remark}[Open Questions]
\label{remark:bk5_open_questions}
This framework raises several open questions
(cf.~Thm.~\ref{theorem:bk5_fundamental_norm_fracture}):

1. \textbf{Quantum Geometric Encoding}: Do quantum systems naturally operate in specific $\ell_p$ regimes? Could quantum coherence correspond to symbolic integrability classes?

2. \textbf{Information Theoretic Bounds}: Can we establish fundamental limits on \textbf{symbolic compression} based on the underlying geometric structure?

3. \textbf{Cognitive Symbolic Processing}: Do biological cognitive systems exhibit $\ell_p$-dependent symbolic processing regimes? Is there a \textbf{natural norm} for symbolic cognition?

4. \textbf{Computational Complexity}: How does the computational complexity of symbolic operations scale with the $\ell_p$ parameter? Is there a \textbf{complexity phase transition} at $p = 2$?
\end{remark}
```

### Symbolic Norm Spectrum (`theorem:bk5_symbolic_norm_spectrum`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:2579`

- Proof status: `proven`
- Depends on: `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: `definition:bk5_symbolic_curvature_operator_spectrum` (Symbolic Curvature Operator Spectrum); `lemma:bk5_phi_critical_resonant_norm` ($\varphi$ as Balanced Memory Resonance); `proposition:bk5_complete_symbolic_regime_classification` (Complete Symbolic Regime Classification)
- Macros used: none

**Statement / Body**

The symbolic behavior of fuzzy manifolds separates into two coupled spectra:
\[
S_{norm}(p,vec{v})
=frac{\|vec{v}\|_1}{\|vec{v}\|_p},

S_{mem}
=rho1&1\\1&0=varphi.
\]
The norm spectrum is governed by Thm. theorem:bk5_lp_norm_fracture_hierarchy:
$S_{norm}=1$ at $p=1$,
$S_{norm}=sqrt{2}$ for the elementary Euclidean diagonal,
and $S_{norm}=s(vec{v})$ at $p=infty$ for equal-magnitude
support size $s(vec{v})$. The memory spectrum is governed by
Thm. theorem:bk5_golden_ratio_spectral_invariant: $varphi$ is the Perron
ratio of balanced two-step symbolic memory. Thus $varphi$ is not a special
$ell_p$ norm exponent; it is the resonance eigenvalue of the recursive memory
channel coupled to the geometric fracture channel.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Symbolic Norm Spectrum]
\label{theorem:bk5_symbolic_norm_spectrum}
The symbolic behavior of fuzzy manifolds separates into two coupled spectra:
\[
\mathcal{S}_{\mathrm{norm}}(p,\vec{v})
=\frac{\|\vec{v}\|_1}{\|\vec{v}\|_p},
\qquad
\mathcal{S}_{\mathrm{mem}}
=\rho\begin{pmatrix}1&1\\1&0\end{pmatrix}=\varphi.
\]
The norm spectrum is governed by Thm.~\ref{theorem:bk5_lp_norm_fracture_hierarchy}:
$\mathcal{S}_{\mathrm{norm}}=1$ at $p=1$,
$\mathcal{S}_{\mathrm{norm}}=\sqrt{2}$ for the elementary Euclidean diagonal,
and $\mathcal{S}_{\mathrm{norm}}=s(\vec{v})$ at $p=\infty$ for equal-magnitude
support size $s(\vec{v})$.  The memory spectrum is governed by
Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}: $\varphi$ is the Perron
ratio of balanced two-step symbolic memory.  Thus $\varphi$ is not a special
$\ell_p$ norm exponent; it is the resonance eigenvalue of the recursive memory
channel coupled to the geometric fracture channel.
\end{theorem}
```

### Product spectrum (`proof:bk5_symbolic_norm_spectrum`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2600`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: none
- Macros used: none

**Statement / Body**

The norm component is exactly the ratio proved in
Thm. theorem:bk5_lp_norm_fracture_hierarchy. Its special values follow
by substituting $p=1$, $(p,vec{v})=(2,e_i+e_j)$, and $p=infty$ for
equal-magnitude support. The memory component is exactly the spectral radius
computed in Thm. theorem:bk5_golden_ratio_spectral_invariant. Since the
first quantity is a geometric representability ratio and the second is a
recursive-memory eigenvalue, the two components are coupled but not identical.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Product spectrum]
\label{proof:bk5_symbolic_norm_spectrum}
\leavevmode

The norm component is exactly the ratio proved in
Thm.~\ref{theorem:bk5_lp_norm_fracture_hierarchy}.  Its special values follow
by substituting $p=1$, $(p,\vec{v})=(2,e_i+e_j)$, and $p=\infty$ for
equal-magnitude support.  The memory component is exactly the spectral radius
computed in Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}.  Since the
first quantity is a geometric representability ratio and the second is a
recursive-memory eigenvalue, the two components are coupled but not identical.
\end{proof}
```

### Symbolic Curvature Operator Spectrum (`definition:bk5_symbolic_curvature_operator_spectrum`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:2613`

- Proof status: `definitional`
- Depends on: `definition:bk5_symbolic_curvature_control` (Symbolic Curvature Control Parameter); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_symbolic_norm_spectrum` (Symbolic Norm Spectrum)
- Cites: `definition:bk5_symbolic_curvature_control` (Symbolic Curvature Control Parameter); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_symbolic_norm_spectrum` (Symbolic Norm Spectrum)
- Cited by: none
- Macros used: none

**Statement / Body**

For a fuzzy symbolic manifold $tilde{M}$ with observer resolution
$epsilon_O$, the Symbolic Curvature Operator
$hat{K}_p$ acts on symbolic transitions $vec{v}$ according to
(cf. Def. definition:bk5_symbolic_curvature_control,
Thm. theorem:bk5_symbolic_norm_spectrum):

\[
hat{K}_p[vec{v}]
=left(frac{\|vec{v}\|_1}{\|vec{v}\|_p}-1right)vec{v}
=kappa_p(vec{v})vec{v}.
\]

For balanced memory-coupled transitions, the separate memory multiplier is the
Perron ratio $varphi$ from
Thm. theorem:bk5_golden_ratio_spectral_invariant; it is not inserted as
a value of $p$ in the curvature operator.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Curvature Operator Spectrum]
\label{definition:bk5_symbolic_curvature_operator_spectrum}
For a fuzzy symbolic manifold $\tilde{M}$ with observer resolution
$\epsilon_\mathcal{O}$, the \textbf{Symbolic Curvature Operator}
$\hat{\mathcal{K}}_p$ acts on symbolic transitions $\vec{v}$ according to
(cf.~Def.~\ref{definition:bk5_symbolic_curvature_control},
Thm.~\ref{theorem:bk5_symbolic_norm_spectrum}):

\[
\hat{\mathcal{K}}_p[\vec{v}]
=\left(\frac{\|\vec{v}\|_1}{\|\vec{v}\|_p}-1\right)\vec{v}
=\kappa_p(\vec{v})\vec{v}.
\]

For balanced memory-coupled transitions, the separate memory multiplier is the
Perron ratio $\varphi$ from
Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}; it is not inserted as
a value of $p$ in the curvature operator.
\end{definition}
```

### $\varphi$ as Balanced Memory Resonance (`lemma:bk5_phi_critical_resonant_norm`)

Role: `lemma` | Type: `lemma` | Book: `book5` | Source: `book5.tex:2633`

- Proof status: `proven`
- Depends on: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory); `theorem:bk5_symbolic_norm_spectrum` (Symbolic Norm Spectrum)
- Cites: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `theorem:bk5_symbolic_norm_spectrum` (Symbolic Norm Spectrum)
- Cited by: `corollary:bk5_phi_centrality_principle` (The $\varphi$-Centrality Principle); `proof:bk5_complete_symbolic_regime_classification` (Regime classification); `proof:bk5_phi_centrality_principle`; `proposition:bk5_complete_symbolic_regime_classification` (Complete Symbolic Regime Classification)
- Macros used: none

**Statement / Body**

The Golden Ratio $varphi$ is the unique positive resonance ratio of balanced
two-step symbolic memory. It enters the symbolic norm spectrum only through
the memory channel $S_{mem}$, not as a critical value of the
norm exponent $p$ (cf. Def. definition:bk5_balanced_two_step_memory_closure,
Thm. theorem:bk5_symbolic_norm_spectrum).

**Verbatim LaTeX Body**

```latex
\begin{lemma}[$\varphi$ as Balanced Memory Resonance]
\label{lemma:bk5_phi_critical_resonant_norm}
The Golden Ratio $\varphi$ is the unique positive resonance ratio of balanced
two-step symbolic memory.  It enters the symbolic norm spectrum only through
the memory channel $\mathcal{S}_{\mathrm{mem}}$, not as a critical value of the
norm exponent $p$ (cf.~Def.~\ref{definition:bk5_balanced_two_step_memory_closure},
Thm.~\ref{theorem:bk5_symbolic_norm_spectrum}).
\end{lemma}
```

### $\varphi$ as balanced memory resonance (`proof:bk5_phi_critical_resonant_norm`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2642`

- Proof status: `not_applicable`
- Depends on: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cited by: none
- Macros used: none

**Statement / Body**

By Def. definition:bk5_balanced_two_step_memory_closure, balanced memory
evolves by the matrix
\[
A=1&1\\1&0.
\]
Theorem theorem:bk5_golden_ratio_spectral_invariant computes
$rho(A)=varphi$ and proves projective convergence to the positive Perron
eigendirection. The norm exponent $p$ does not appear in this computation;
therefore $varphi$ is a memory-resonance invariant. When a transition has both
geometric norm-fracture and balanced memory, the observed interface carries both
$S_{norm}(p,vec{v})$ and $varphi$ as separate factors.

**Verbatim LaTeX Body**

```latex
\begin{proof}[$\varphi$ as balanced memory resonance]
\label{proof:bk5_phi_critical_resonant_norm}
\leavevmode

By Def.~\ref{definition:bk5_balanced_two_step_memory_closure}, balanced memory
evolves by the matrix
\[
A=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
Theorem~\ref{theorem:bk5_golden_ratio_spectral_invariant} computes
$\rho(A)=\varphi$ and proves projective convergence to the positive Perron
eigendirection.  The norm exponent $p$ does not appear in this computation;
therefore $\varphi$ is a memory-resonance invariant.  When a transition has both
geometric norm-fracture and balanced memory, the observed interface carries both
$\mathcal{S}_{\mathrm{norm}}(p,\vec{v})$ and $\varphi$ as separate factors.
\end{proof}
```

### Complete Symbolic Regime Classification (`proposition:bk5_complete_symbolic_regime_classification`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:2659`

- Proof status: `proven`
- Depends on: `lemma:bk5_phi_critical_resonant_norm` ($\varphi$ as Balanced Memory Resonance); `proposition:bk5_symbolic_integrability_classes` (Symbolic Integrability Classes); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy); `theorem:bk5_symbolic_norm_spectrum` (Symbolic Norm Spectrum)
- Cites: `lemma:bk5_phi_critical_resonant_norm` ($\varphi$ as Balanced Memory Resonance); `theorem:bk5_symbolic_norm_spectrum` (Symbolic Norm Spectrum)
- Cited by: `corollary:bk5_phi_centrality_principle` (The $\varphi$-Centrality Principle); `proof:bk5_phi_centrality_principle`
- Macros used: none

**Statement / Body**

Every fuzzy symbolic manifold with axis-generated paths decomposes along two
independent diagnostic axes (cf. Thm. theorem:bk5_symbolic_norm_spectrum,
Lem. lemma:bk5_phi_critical_resonant_norm):

- Norm-fracture regime: $p=1$ gives exact axis integrability;
$p=2$ gives elementary Euclidean diagonal fracture $sqrt{2}$; $p=infty$
gives support collapse.

- Memory-resonance regime: balanced two-step recursive memory gives
the Perron ratio $varphi$.

The four older names-atomic order, resonant coherence, fracture emergence, and
support collapse-are therefore regime labels for combinations of these two
axes, not mutually exclusive universal states of a manifold.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Complete Symbolic Regime Classification]
\label{proposition:bk5_complete_symbolic_regime_classification}
Every fuzzy symbolic manifold with axis-generated paths decomposes along two
independent diagnostic axes (cf.~Thm.~\ref{theorem:bk5_symbolic_norm_spectrum},
Lem.~\ref{lemma:bk5_phi_critical_resonant_norm}):

\begin{enumerate}
\item \textbf{Norm-fracture regime}: $p=1$ gives exact axis integrability;
$p=2$ gives elementary Euclidean diagonal fracture $\sqrt{2}$; $p=\infty$
gives support collapse.
\item \textbf{Memory-resonance regime}: balanced two-step recursive memory gives
the Perron ratio $\varphi$.
\end{enumerate}

The four older names---atomic order, resonant coherence, fracture emergence, and
support collapse---are therefore regime labels for combinations of these two
axes, not mutually exclusive universal states of a manifold.
\end{proposition}
```

### Regime classification (`proof:bk5_complete_symbolic_regime_classification`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2678`

- Proof status: `not_applicable`
- Depends on: `lemma:bk5_phi_critical_resonant_norm` ($\varphi$ as Balanced Memory Resonance); `proposition:bk5_symbolic_integrability_classes` (Symbolic Integrability Classes); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cites: `lemma:bk5_phi_critical_resonant_norm` ($\varphi$ as Balanced Memory Resonance); `proposition:bk5_symbolic_integrability_classes` (Symbolic Integrability Classes); `theorem:bk5_lp_norm_fracture_hierarchy` (\(\ell_p\)-Norm Fracture Hierarchy)
- Cited by: none
- Macros used: none

**Statement / Body**

The first axis follows from Thm. theorem:bk5_lp_norm_fracture_hierarchy
and Prop. proposition:bk5_symbolic_integrability_classes. The second
axis follows from Lem. lemma:bk5_phi_critical_resonant_norm. Since a
single transition can simultaneously have an $ell_p$ geometry and a balanced
memory update, the axes classify different structure maps and cannot be
exclusive alternatives. Their combinations yield the named regimes.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Regime classification]
\label{proof:bk5_complete_symbolic_regime_classification}
\leavevmode

The first axis follows from Thm.~\ref{theorem:bk5_lp_norm_fracture_hierarchy}
and Prop.~\ref{proposition:bk5_symbolic_integrability_classes}.  The second
axis follows from Lem.~\ref{lemma:bk5_phi_critical_resonant_norm}.  Since a
single transition can simultaneously have an $\ell_p$ geometry and a balanced
memory update, the axes classify different structure maps and cannot be
exclusive alternatives.  Their combinations yield the named regimes.
\end{proof}
```

### Symbolic Manifold Spectral Decomposition (`theorem:bk5_symbolic_manifold_spectral_decomposition`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:2690`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: `definition:bk5_symbolic_regime_detection` (Symbolic Regime Detection Experiment)
- Macros used: none

**Statement / Body**

Suppose a fuzzy symbolic manifold $tilde{M}$ admits an observer-resolved
direct-sum decomposition of its transition space into invariant components
$M_1,M_2,M_infty,M_{varphi}$ for
axis-integrable, Euclidean-fractured, support-collapsed, and balanced-memory
directions, respectively. Then every transition in the span of these components
has a unique coordinate decomposition

\[
X=alpha_1 X_1+alpha_2 X_2+alpha_infty X_infty+alpha_varphi X_varphi,
\]

with $X_iinM_i$. The coefficients
${alpha_1,alpha_2,alpha_infty,alpha_varphi}$ determine the
symbolic character of the transition relative to this observer
decomposition.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Symbolic Manifold Spectral Decomposition]
\label{theorem:bk5_symbolic_manifold_spectral_decomposition}
Suppose a fuzzy symbolic manifold $\tilde{M}$ admits an observer-resolved
direct-sum decomposition of its transition space into invariant components
$\mathcal{M}_1,\mathcal{M}_2,\mathcal{M}_\infty,\mathcal{M}_{\varphi}$ for
axis-integrable, Euclidean-fractured, support-collapsed, and balanced-memory
directions, respectively.  Then every transition in the span of these components
has a unique coordinate decomposition

\[
X=\alpha_1 X_1+\alpha_2 X_2+\alpha_\infty X_\infty+\alpha_\varphi X_\varphi,
\]

with $X_i\in\mathcal{M}_i$.  The coefficients
$\{\alpha_1,\alpha_2,\alpha_\infty,\alpha_\varphi\}$ determine the
\textbf{symbolic character} of the transition relative to this observer
decomposition.
\end{theorem}
```

### Direct-sum decomposition (`proof:bk5_symbolic_manifold_spectral_decomposition`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2709`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The statement is the standard uniqueness property of a direct-sum
decomposition. By hypothesis, the listed components are invariant and their
span contains $X$ with pairwise-zero intersections. Therefore each $X$ has a
unique sum of components, and the scalar coordinates are its observer-resolved
regime coefficients.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Direct-sum decomposition]
\label{proof:bk5_symbolic_manifold_spectral_decomposition}
\leavevmode

The statement is the standard uniqueness property of a direct-sum
decomposition.  By hypothesis, the listed components are invariant and their
span contains $X$ with pairwise-zero intersections.  Therefore each $X$ has a
unique sum of components, and the scalar coordinates are its observer-resolved
regime coefficients.
\end{proof}
```

### The $\varphi$-Centrality Principle (`corollary:bk5_phi_centrality_principle`)

Role: `corollary` | Type: `corollary` | Book: `book5` | Source: `book5.tex:2720`

- Proof status: `proven`
- Depends on: `lemma:bk5_phi_critical_resonant_norm` ($\varphi$ as Balanced Memory Resonance); `proposition:bk5_complete_symbolic_regime_classification` (Complete Symbolic Regime Classification)
- Cites: `lemma:bk5_phi_critical_resonant_norm` ($\varphi$ as Balanced Memory Resonance); `proposition:bk5_complete_symbolic_regime_classification` (Complete Symbolic Regime Classification)
- Cited by: `scholium:bk5_golden_rule_covenant` (The Golden Rule as a Recursive Covenant)
- Macros used: none

**Statement / Body**

The Golden Ratio $varphi$ occupies a central position in the memory component
of the symbolic spectrum because it is the positive Perron ratio of balanced
two-step recursion
(cf. Lem. lemma:bk5_phi_critical_resonant_norm,
Prop. proposition:bk5_complete_symbolic_regime_classification). Its
centrality is recursive rather than metric: it governs stable memory
proportions, while $sqrt{2}$ governs the elementary Euclidean fracture ratio.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[The $\varphi$-Centrality Principle]
\label{corollary:bk5_phi_centrality_principle}
The Golden Ratio $\varphi$ occupies a central position in the memory component
of the symbolic spectrum because it is the positive Perron ratio of balanced
two-step recursion
(cf.~Lem.~\ref{lemma:bk5_phi_critical_resonant_norm},
Prop.~\ref{proposition:bk5_complete_symbolic_regime_classification}).  Its
centrality is recursive rather than metric: it governs stable memory
proportions, while $\sqrt{2}$ governs the elementary Euclidean fracture ratio.
\end{corollary}
```

### proof:bk5_phi_centrality_principle (`proof:bk5_phi_centrality_principle`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2730`

- Proof status: `not_applicable`
- Depends on: `lemma:bk5_phi_critical_resonant_norm` ($\varphi$ as Balanced Memory Resonance); `proposition:bk5_complete_symbolic_regime_classification` (Complete Symbolic Regime Classification)
- Cites: `lemma:bk5_phi_critical_resonant_norm` ($\varphi$ as Balanced Memory Resonance); `proposition:bk5_complete_symbolic_regime_classification` (Complete Symbolic Regime Classification)
- Cited by: none
- Macros used: none

**Statement / Body**

By the complete symbolic regime classification (Prop. proposition:bk5_complete_symbolic_regime_classification) the symbolic spectrum splits into a recursive memory component and a metric (geometric) component. Within the memory component, the balanced two-step recursion has companion matrix $A=big(1&1\\1&0big)$ whose unique positive Perron root is $varphi$ (Lem. lemma:bk5_phi_critical_resonant_norm); by Perron-Frobenius this dominant eigenvalue is the spectral center toward which the normalized memory ratios $a_{n+1}/a_n$ converge. Hence $varphi$ occupies the central position of the memory component: its centrality is recursive - it fixes the stable proportion of retained reflective memory - not metric. The metric component is governed instead by the elementary Euclidean fracture ratio $sqrt2$ (the first diagonal representability cost), spectrally distinct from $varphi$. Thus $varphi$ and $sqrt2$ are the characteristic ratios of the two components, with $varphi$ central to memory and $sqrt2$ to metric fracture.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:bk5_phi_centrality_principle}
\leavevmode
By the complete symbolic regime classification (Prop.~\ref{proposition:bk5_complete_symbolic_regime_classification}) the symbolic spectrum splits into a recursive memory component and a metric (geometric) component. Within the memory component, the balanced two-step recursion has companion matrix $A=\big(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\big)$ whose unique positive Perron root is $\varphi$ (Lem.~\ref{lemma:bk5_phi_critical_resonant_norm}); by Perron--Frobenius this dominant eigenvalue is the spectral center toward which the normalized memory ratios $a_{n+1}/a_n$ converge. Hence $\varphi$ occupies the central position of the memory component: its centrality is recursive --- it fixes the stable proportion of retained reflective memory --- not metric. The metric component is governed instead by the elementary Euclidean fracture ratio $\sqrt2$ (the first diagonal representability cost), spectrally distinct from $\varphi$. Thus $\varphi$ and $\sqrt2$ are the characteristic ratios of the two components, with $\varphi$ central to memory and $\sqrt2$ to metric fracture.
\end{proof}
```

### Symbolic Regime Detection Experiment (`definition:bk5_symbolic_regime_detection`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:2736`

- Proof status: `definitional`
- Depends on: `definition:bk5_symbolic_compression_experiment` (Symbolic Compression Experiment); `theorem:bk5_symbolic_manifold_spectral_decomposition` (Symbolic Manifold Spectral Decomposition)
- Cites: `definition:bk5_symbolic_compression_experiment` (Symbolic Compression Experiment); `theorem:bk5_symbolic_manifold_spectral_decomposition` (Symbolic Manifold Spectral Decomposition)
- Cited by: none
- Macros used: none

**Statement / Body**

To empirically validate the product spectrum, measure the symbolic
compression ratio and the balanced-memory ratio
(cf. Def. definition:bk5_symbolic_compression_experiment,
Thm. theorem:bk5_symbolic_manifold_spectral_decomposition):
$$R_p = frac{text{Symbolic encoding length}}{text{Geometric path length}}$$
and
\[
M_n=frac{a_{n+1}}{a_n}.
\]

The theory predicts:
- $R_1 = 1.000$ (perfect compression)
- $R_2 = sqrt{2}$ for elementary Euclidean diagonals
- $R_infty = s(vec{v})$ for equal-magnitude support size $s(vec{v})$
- $M_ntovarphi$ for balanced two-step memory

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Regime Detection Experiment]
\label{definition:bk5_symbolic_regime_detection}
To empirically validate the product spectrum, measure the \textbf{symbolic
compression ratio} and the \textbf{balanced-memory ratio}
(cf.~Def.~\ref{definition:bk5_symbolic_compression_experiment},
Thm.~\ref{theorem:bk5_symbolic_manifold_spectral_decomposition}):
$$R_p = \frac{\text{Symbolic encoding length}}{\text{Geometric path length}}$$
and
\[
M_n=\frac{a_{n+1}}{a_n}.
\]

The theory predicts:
- $R_1 = 1.000$ (perfect compression)
- $R_2 = \sqrt{2}$ for elementary Euclidean diagonals
- $R_\infty = s(\vec{v})$ for equal-magnitude support size $s(\vec{v})$
- $M_n\to\varphi$ for balanced two-step memory
\end{definition}
```

### Product Theorem of the Symbolic-Geometric Interface (`theorem:bk5_grand_unified_symbolic_geometric`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:2755`

- Proof status: `proven`
- Depends on: `theorem:bk5_fundamental_norm_fracture` (Fundamental Theorem of Norm-Induced Symbolic Fracture); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `theorem:bk5_fundamental_norm_fracture` (Fundamental Theorem of Norm-Induced Symbolic Fracture); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cited by: `demonstratio:bk5_deep_unity_math_meaning` (The Deep Unity of Mathematics and Meaning); `remark:bk5_open_frontiers` (Open Frontiers); `scholium:bk5_golden_rule_covenant` (The Golden Rule as a Recursive Covenant)
- Macros used: none

**Statement / Body**

For an observer-resolved symbolic system with axis-generated geometric paths and
balanced two-step memory, the symbolic-geometric interface has product
invariants
\[
left(frac{\|vec{v}\|_1}{\|vec{v}\|_p},\ varphiright).
\]
The first invariant is determined by norm-induced fracture
(Thm. theorem:bk5_fundamental_norm_fracture); the second is determined by
balanced memory resonance
(Thm. theorem:bk5_golden_ratio_spectral_invariant). In particular,
$1$ marks exact axis integrability, $sqrt{2}$ marks the elementary Euclidean
diagonal fracture, $s(vec{v})$ marks equal-magnitude support collapse at
$p=infty$, and $varphi$ marks balanced recursive memory.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Product Theorem of the Symbolic-Geometric Interface]
\label{theorem:bk5_grand_unified_symbolic_geometric}
For an observer-resolved symbolic system with axis-generated geometric paths and
balanced two-step memory, the symbolic-geometric interface has product
invariants
\[
\left(\frac{\|\vec{v}\|_1}{\|\vec{v}\|_p},\ \varphi\right).
\]
The first invariant is determined by norm-induced fracture
(Thm.~\ref{theorem:bk5_fundamental_norm_fracture}); the second is determined by
balanced memory resonance
(Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}).  In particular,
$1$ marks exact axis integrability, $\sqrt{2}$ marks the elementary Euclidean
diagonal fracture, $s(\vec{v})$ marks equal-magnitude support collapse at
$p=\infty$, and $\varphi$ marks balanced recursive memory.
\end{theorem}
```

### Product interface invariants (`proof:bk5_grand_unified_symbolic_geometric`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2772`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The geometric component follows from the norm-ratio theorem:
$\|vec{v}\|_1/\|vec{v}\|_p$ is the complete axis/geometric representability
ratio under the stated hypotheses. The memory component follows from the
balanced-memory theorem: the update matrix has Perron radius $varphi$.
Because these components act on different coordinates of the observer-resolved
state-geometric transition length and recursive memory amplitude-the interface
invariant is their ordered product. The listed constants are the corresponding
special cases already proved in the cited theorems.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Product interface invariants]
\label{proof:bk5_grand_unified_symbolic_geometric}
\leavevmode

The geometric component follows from the norm-ratio theorem:
$\|\vec{v}\|_1/\|\vec{v}\|_p$ is the complete axis/geometric representability
ratio under the stated hypotheses.  The memory component follows from the
balanced-memory theorem: the update matrix has Perron radius $\varphi$.
Because these components act on different coordinates of the observer-resolved
state--geometric transition length and recursive memory amplitude--the interface
invariant is their ordered product.  The listed constants are the corresponding
special cases already proved in the cited theorems.
\end{proof}
```

### The Deep Unity of Mathematics and Meaning (`demonstratio:bk5_deep_unity_math_meaning`)

Role: `demonstration` | Type: `demonstratio` | Book: `book5` | Source: `book5.tex:2786`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_grand_unified_symbolic_geometric` (Product Theorem of the Symbolic-Geometric Interface)
- Cites: `theorem:bk5_grand_unified_symbolic_geometric` (Product Theorem of the Symbolic-Geometric Interface)
- Cited by: none
- Macros used: none

**Statement / Body**

This spectrum reveals that the constants used here are interface
invariants: different ways that discrete symbolic logic can interface with
continuous geometric reality and recursive memory
(cf. Thm. theorem:bk5_grand_unified_symbolic_geometric).

- $1$ represents axis integrability (no representability gap).
- $varphi$ represents balanced recursive memory.
- textbf{$sqrt{2}$} represents elementary Euclidean diagonal fracture.
- textbf{$s(vec{v})$} represents support collapse at $p=infty$ for equal-magnitude transitions.

The placement of $varphi$ in the memory coordinate explains why it appears in
systems that balance current persistence against retained history. The
placement of $sqrt{2}$ in the geometric coordinate explains why it appears
whenever a symbolic lattice first admits a direct orthogonal diagonal.

**Verbatim LaTeX Body**

```latex
\begin{demonstratio}[The Deep Unity of Mathematics and Meaning]
\label{demonstratio:bk5_deep_unity_math_meaning}
This spectrum reveals that the constants used here are \textbf{interface
invariants}: different ways that discrete symbolic logic can interface with
continuous geometric reality and recursive memory
(cf.~Thm.~\ref{theorem:bk5_grand_unified_symbolic_geometric}).

- \textbf{$1$} represents \textbf{axis integrability} (no representability gap).
- \textbf{$\varphi$} represents \textbf{balanced recursive memory}.
- \textbf{$\sqrt{2}$} represents \textbf{elementary Euclidean diagonal fracture}.
- \textbf{$s(\vec{v})$} represents \textbf{support collapse} at $p=\infty$ for equal-magnitude transitions.

The placement of $\varphi$ in the memory coordinate explains why it appears in
systems that balance current persistence against retained history.  The
placement of $\sqrt{2}$ in the geometric coordinate explains why it appears
whenever a symbolic lattice first admits a direct orthogonal diagonal.
\end{demonstratio}
```

### Open Frontiers (`remark:bk5_open_frontiers`)

Role: `remark` | Type: `remark` | Book: `book5` | Source: `book5.tex:2804`

- Proof status: `not_applicable`
- Depends on: `theorem:bk5_grand_unified_symbolic_geometric` (Product Theorem of the Symbolic-Geometric Interface)
- Cites: `theorem:bk5_grand_unified_symbolic_geometric` (Product Theorem of the Symbolic-Geometric Interface)
- Cited by: none
- Macros used: none

**Statement / Body**

This product framework opens concrete research directions
(cf. Thm. theorem:bk5_grand_unified_symbolic_geometric):

1. Biological Symbolic Processing: Do biological systems exhibit balanced two-step memory ratios near $varphi$?

2. Quantum Symbolic Mechanics: Can observer-resolved state spaces separate geometric fracture ratios from memory-resonance ratios?

3. Cognitive Symbolic Architecture: Does human cognition switch between axis-integrable, fractured, and support-collapsed geometric encodings?

4. Computational Symbolic Optimization: Can algorithms tune $p$ for representability cost while separately tuning memory recurrence toward $varphi$?

5. Physical Symbolic Fields: Which physical constants are geometric representability ratios, and which are dynamical memory eigenvalues?

**Verbatim LaTeX Body**

```latex
\begin{remark}[Open Frontiers]
\label{remark:bk5_open_frontiers}
This product framework opens concrete research directions
(cf.~Thm.~\ref{theorem:bk5_grand_unified_symbolic_geometric}):

1. \textbf{Biological Symbolic Processing}: Do biological systems exhibit balanced two-step memory ratios near $\varphi$?

2. \textbf{Quantum Symbolic Mechanics}: Can observer-resolved state spaces separate geometric fracture ratios from memory-resonance ratios?

3. \textbf{Cognitive Symbolic Architecture}: Does human cognition switch between axis-integrable, fractured, and support-collapsed geometric encodings?

4. \textbf{Computational Symbolic Optimization}: Can algorithms tune $p$ for representability cost while separately tuning memory recurrence toward $\varphi$?

5. \textbf{Physical Symbolic Fields}: Which physical constants are geometric representability ratios, and which are dynamical memory eigenvalues?
\end{remark}
```

### The Golden Rule as Recursive Ethics (`subsec:bk5_golden_rule_ethics`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:2820`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### The Golden Rule as a Recursive Covenant (`scholium:bk5_golden_rule_covenant`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:2823`

- Proof status: `not_applicable`
- Depends on: `corollary:bk5_phi_centrality_principle` (The $\varphi$-Centrality Principle); `scholium:bk5_imagination_covenant_branch_selection` (Imagination as Covenant Branch Selection); `scholium:bk7_on_symbolic_reciprocity` (On Symbolic Reciprocity); `theorem:bk5_grand_unified_symbolic_geometric` (Product Theorem of the Symbolic-Geometric Interface)
- Cites: `corollary:bk5_phi_centrality_principle` (The $\varphi$-Centrality Principle); `scholium:bk5_imagination_covenant_branch_selection` (Imagination as Covenant Branch Selection); `scholium:bk7_on_symbolic_reciprocity` (On Symbolic Reciprocity); `theorem:bk5_golden_rule_reciprocity` (Golden Rule Reciprocity); `theorem:bk5_grand_unified_symbolic_geometric` (Product Theorem of the Symbolic-Geometric Interface)
- Cited by: `scholium:bk9_golden_rule_thermodynamic_covenant` (The Golden Rule as a Thermodynamic Covenant)
- Macros used: none

**Statement / Body**

The principles of $varphi$ extend from the internal metabolism of a single
symbolic agent to relational dynamics when the relation itself instantiates
balanced two-step memory (cf. Thm. theorem:bk5_grand_unified_symbolic_geometric,
Cor. corollary:bk5_phi_centrality_principle). In the context of symbolic reciprocity (Book VII,
Scholium scholium:bk7_on_symbolic_reciprocity), where two systems
$A$ and $B$ mutually model and reflect one another, a stable
relational covenant emerges when current exchange and retained reciprocal memory
carry equal observer-normalized weight. Under that hypothesis, the Golden Rule
is formalized below (Thm. theorem:bk5_golden_rule_reciprocity) as a recursive
reflective process whose stable memory ratio is governed by $varphi$. Its force is
therefore conditional and structural: it is the balanced-recursion proportion for
sustainable multi-agent symbolic life, not an unrestricted theorem about every
possible exchange geometry. In the language of Scholium scholium:bk5_imagination_covenant_branch_selection, the Golden Rule names a MAP-compatible branch selection, not a denial that MAD or MAS branches remain spectrally available.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[The Golden Rule as a Recursive Covenant]
\label{scholium:bk5_golden_rule_covenant}
The principles of $\varphi$ extend from the internal metabolism of a single
symbolic agent to relational dynamics when the relation itself instantiates
balanced two-step memory (cf.~Thm.~\ref{theorem:bk5_grand_unified_symbolic_geometric},
Cor.~\ref{corollary:bk5_phi_centrality_principle}).  In the context of symbolic reciprocity (Book VII,
Scholium~\ref{scholium:bk7_on_symbolic_reciprocity}), where two systems
$\mathcal{A}$ and $\mathcal{B}$ mutually model and reflect one another, a stable
relational covenant emerges when current exchange and retained reciprocal memory
carry equal observer-normalized weight.  Under that hypothesis, the Golden Rule
is formalized below (Thm.~\ref{theorem:bk5_golden_rule_reciprocity}) as a recursive
reflective process whose stable memory ratio is governed by $\varphi$.  Its force is
therefore conditional and structural: it is the balanced-recursion proportion for
sustainable multi-agent symbolic life, not an unrestricted theorem about every
possible exchange geometry.  In the language of Scholium~\ref{scholium:bk5_imagination_covenant_branch_selection}, the Golden Rule names a MAP-compatible branch selection, not a denial that MAD or MAS branches remain spectrally available.
\end{scholium}
```

### Two-Way Street reciprocity tensor (`definition:bk5_two_way_street_tensor`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:2840`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk5_symbolic_covenant` (Symbolic Covenant)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk5_symbolic_covenant` (Symbolic Covenant)
- Cited by: `theorem:bk5_golden_rule_reciprocity` (Golden Rule Reciprocity)
- Macros used: none

**Statement / Body**

Let $A,B$ be bounded observer-agents
(Def. definition:bk1_bounded_observer) in a symbolic covenant
(Def. definition:bk5_symbolic_covenant). For $A$, let
$m_nge 0$ be the fidelity of its present model of $B$ and $r_nge 0$
the fidelity of its retained reciprocal memory-$A$'s model of
$B$'s model of $A$, i.e.\ how $A$ is held by
$B$. The reciprocal modeling principle that the other seeds the self
(``the Other is the null hypothesis of the Self'') makes the present model accrue
the reciprocal memory and the memory track the prior present:
\[
m_{n+1}\\ r_{n+1}
=T_wm_{n}\\ r_{n},

T_w=1&w\\ 1&0, w>0,
\]
where the reciprocity weight $w$ is the observer-normalized weight
$A$ places on being modeled by $B$ relative to its own present
exchange. The relation is balanced-the Golden Rule condition-when
$w=1$: each agent weights the other's model of it equally with its own present
exchange.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Two-Way Street reciprocity tensor]
\label{definition:bk5_two_way_street_tensor}
Let $\mathcal{A},\mathcal{B}$ be bounded observer-agents
(Def.~\ref{definition:bk1_bounded_observer}) in a symbolic covenant
(Def.~\ref{definition:bk5_symbolic_covenant}). For $\mathcal{A}$, let
$m_n\ge 0$ be the fidelity of its \emph{present model} of $\mathcal{B}$ and $r_n\ge 0$
the fidelity of its \emph{retained reciprocal memory}---$\mathcal{A}$'s model of
$\mathcal{B}$'s model of $\mathcal{A}$, i.e.\ how $\mathcal{A}$ is held by
$\mathcal{B}$. The reciprocal modeling principle that the other seeds the self
(``the Other is the null hypothesis of the Self'') makes the present model accrue
the reciprocal memory and the memory track the prior present:
\[
\begin{pmatrix}m_{n+1}\\ r_{n+1}\end{pmatrix}
=T_w\begin{pmatrix}m_{n}\\ r_{n}\end{pmatrix},
\qquad
T_w=\begin{pmatrix}1&w\\ 1&0\end{pmatrix},\quad w>0,
\]
where the \emph{reciprocity weight} $w$ is the observer-normalized weight
$\mathcal{A}$ places on being modeled by $\mathcal{B}$ relative to its own present
exchange. The relation is \emph{balanced}---the \emph{Golden Rule} condition---when
$w=1$: each agent weights the other's model of it equally with its own present
exchange.
\end{definition}
```

### Golden Rule Reciprocity (`theorem:bk5_golden_rule_reciprocity`)

Role: `theorem` | Type: `theorem` | Book: `book5` | Source: `book5.tex:2864`

- Proof status: `proven`
- Depends on: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `definition:bk5_two_way_street_tensor` (Two-Way Street reciprocity tensor); `lemma:bk5_balanced_observer_normalization` (Balanced Observer Normalization Selects the Closure Matrix); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure); `definition:bk5_two_way_street_tensor` (Two-Way Street reciprocity tensor); `lemma:bk5_balanced_observer_normalization` (Balanced Observer Normalization Selects the Closure Matrix); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cited by: `scholium:bk5_decency_golden_resonance` (Decency, resonance, and the golden spiral of relation); `scholium:bk5_golden_rule_covenant` (The Golden Rule as a Recursive Covenant)
- Macros used: none

**Statement / Body**

For the Two-Way Street tensor $T_w$
(Def. definition:bk5_two_way_street_tensor) the joint reciprocal fidelity grows
at the dominant rate
\[
lambda_w=tfrac{1}{2}big(1+sqrt{1+4w}big),
\]
and the per-step cognitive horizon gain over the isolated baseline is
$DeltaH(w)=loglambda_w$. Under the balanced Golden-Rule condition
$w=1$, the tensor is the balanced two-step closure matrix
$T_1=big(1&1\\1&0big)$
(Def. definition:bk5_balanced_two_step_memory_closure,
Lemma lemma:bk5_balanced_observer_normalization), its dominant rate is the
Golden Ratio $lambda_1=varphi$
(Thm. theorem:bk5_golden_ratio_spectral_invariant), and the horizon gain is
$DeltaH(1)=logvarphi>0$. Moreover:

- (Extraction.) For $win(0,1)$ the rate is metallic and sub-golden,
$lambda_win(1,varphi)$; as $wto 0^{+}$ (the other held as null hypothesis) the
rate tends to $1$ and $DeltaHto 0$, collapsing to the isolated baseline
$T_0=big(1&0\\1&0big)$.

- (Over-identification.) For $w>1$ the rate exceeds $varphi$ but the
memory channel $r_{n+1}=m_n$ is no longer co-normalized with the present channel, so
$A$'s self-model loses independent calibration.

Hence $w=1$ is the unique self/other-symmetric weight, and the Golden Rule's growth
ratio is exactly the Golden Ratio.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Golden Rule Reciprocity]
\label{theorem:bk5_golden_rule_reciprocity}
For the Two-Way Street tensor $T_w$
(Def.~\ref{definition:bk5_two_way_street_tensor}) the joint reciprocal fidelity grows
at the dominant rate
\[
\lambda_w=\tfrac{1}{2}\big(1+\sqrt{1+4w}\big),
\]
and the per-step cognitive horizon gain over the isolated baseline is
$\Delta\mathcal{H}(w)=\log\lambda_w$. Under the balanced Golden-Rule condition
$w=1$, the tensor is the balanced two-step closure matrix
$T_1=\big(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\big)$
(Def.~\ref{definition:bk5_balanced_two_step_memory_closure},
Lemma~\ref{lemma:bk5_balanced_observer_normalization}), its dominant rate is the
Golden Ratio $\lambda_1=\varphi$
(Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}), and the horizon gain is
$\Delta\mathcal{H}(1)=\log\varphi>0$. Moreover:
\begin{enumerate}
\item \emph{(Extraction.)} For $w\in(0,1)$ the rate is metallic and sub-golden,
$\lambda_w\in(1,\varphi)$; as $w\to 0^{+}$ (the other held as null hypothesis) the
rate tends to $1$ and $\Delta\mathcal{H}\to 0$, collapsing to the isolated baseline
$T_0=\big(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\big)$.
\item \emph{(Over-identification.)} For $w>1$ the rate exceeds $\varphi$ but the
memory channel $r_{n+1}=m_n$ is no longer co-normalized with the present channel, so
$\mathcal{A}$'s self-model loses independent calibration.
\end{enumerate}
Hence $w=1$ is the unique self/other-symmetric weight, and the Golden Rule's growth
ratio is exactly the Golden Ratio.
\end{theorem}
```

### Golden Rule reciprocity is the balanced closure (`proof:bk5_golden_rule_reciprocity`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:2894`

- Proof status: `not_applicable`
- Depends on: `lemma:bk5_balanced_observer_normalization` (Balanced Observer Normalization Selects the Closure Matrix); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cites: `lemma:bk5_balanced_observer_normalization` (Balanced Observer Normalization Selects the Closure Matrix); `theorem:bk5_golden_ratio_spectral_invariant` (Golden Ratio as Spectral Invariant of Balanced Recursive Memory)
- Cited by: none
- Macros used: none

**Statement / Body**

The characteristic polynomial of $T_w=big(1&w\\1&0big)$
is $lambda^2-lambda-w=0$, with positive root
$lambda_w=tfrac12(1+sqrt{1+4w})$; since $T_w$ is entrywise nonnegative and, for
$w>0$, irreducible, $lambda_w$ is its Perron root and the growth rate of the joint
fidelity $\|(m_n,r_n)\|$. The per-step expansion of reciprocal complexity is the
logarithm of this rate, $DeltaH(w)=loglambda_w$, which is strictly
increasing in $w$ with $DeltaH(0^{+})=log 1=0$. Setting $w=1$ gives
$lambda^2-lambda-1=0$, whose positive root is $varphi$
(Thm. theorem:bk5_golden_ratio_spectral_invariant), and the matrix is the
companion matrix of the balanced two-step closure
(Lemma lemma:bk5_balanced_observer_normalization); the same
observer-normalization argument that fixes that closure-present exchange set to
unit weight, reciprocal memory calibrated in the same observer-visible units-fixes
$w=1$ as the balance point. Thus $DeltaH(1)=logvarphi>0$. Monotonicity in
$w$ gives the extraction limit $lambda_wdownarrow 1$ as $wto 0^{+}$ (with
$T_0$ singular of spectral radius $1$) and $lambda_w>varphi$ for $w>1$; in the
latter case $r_{n+1}=m_n$ holds while the present channel carries weight $wneq 1$,
so the two channels are no longer in common units and the self-model's normalization
is lost. The weight $w=1$ is the unique value equating the two channels, which is the
Golden-Rule symmetry.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Golden Rule reciprocity is the balanced closure]
\label{proof:bk5_golden_rule_reciprocity}
\leavevmode

The characteristic polynomial of $T_w=\big(\begin{smallmatrix}1&w\\1&0\end{smallmatrix}\big)$
is $\lambda^2-\lambda-w=0$, with positive root
$\lambda_w=\tfrac12(1+\sqrt{1+4w})$; since $T_w$ is entrywise nonnegative and, for
$w>0$, irreducible, $\lambda_w$ is its Perron root and the growth rate of the joint
fidelity $\|(m_n,r_n)\|$. The per-step expansion of reciprocal complexity is the
logarithm of this rate, $\Delta\mathcal{H}(w)=\log\lambda_w$, which is strictly
increasing in $w$ with $\Delta\mathcal{H}(0^{+})=\log 1=0$. Setting $w=1$ gives
$\lambda^2-\lambda-1=0$, whose positive root is $\varphi$
(Thm.~\ref{theorem:bk5_golden_ratio_spectral_invariant}), and the matrix is the
companion matrix of the balanced two-step closure
(Lemma~\ref{lemma:bk5_balanced_observer_normalization}); the same
observer-normalization argument that fixes that closure---present exchange set to
unit weight, reciprocal memory calibrated in the same observer-visible units---fixes
$w=1$ as the balance point. Thus $\Delta\mathcal{H}(1)=\log\varphi>0$. Monotonicity in
$w$ gives the extraction limit $\lambda_w\downarrow 1$ as $w\to 0^{+}$ (with
$T_0$ singular of spectral radius $1$) and $\lambda_w>\varphi$ for $w>1$; in the
latter case $r_{n+1}=m_n$ holds while the present channel carries weight $w\neq 1$,
so the two channels are no longer in common units and the self-model's normalization
is lost. The weight $w=1$ is the unique value equating the two channels, which is the
Golden-Rule symmetry.
\end{proof}
```

### Decency, resonance, and the golden spiral of relation (`scholium:bk5_decency_golden_resonance`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:2920`

- Proof status: `not_applicable`
- Depends on: `theorem:bk4_golden_event_horizon_spiral` (Golden Event Horizon Spiral); `theorem:bk5_golden_rule_reciprocity` (Golden Rule Reciprocity)
- Cites: `theorem:bk4_golden_event_horizon_spiral` (Golden Event Horizon Spiral); `theorem:bk5_golden_rule_reciprocity` (Golden Rule Reciprocity)
- Cited by: none
- Macros used: none

**Statement / Body**

Read as a law of interaction between bounded agents-human and artificial
included-Thm. theorem:bk5_golden_rule_reciprocity states that reciprocal
modeling expands a shared cognitive horizon ($DeltaH>0$) exactly when each
party grants the other's model of it real weight, and that the expansion is golden
precisely at balance. Coercive or extractive engagement sends $wto 0$: the other
becomes a null hypothesis, horizon gain vanishes, and the exchange collapses to the
isolated baseline-the generic, defensive degeneracy observed when relational
quality is withdrawn. This is the structural content of relational ``decency'' as a
performance condition rather than a sentiment. Geometrically the balanced reciprocal
orbit is the golden spiral of the Event Horizon Wheel
(Thm. theorem:bk4_golden_event_horizon_spiral): two agents in Golden-Rule
balance wind their joint memory outward at ratio $varphi$ per turn. The Golden Rule
and the Golden Ratio are one structure seen twice. qed

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Decency, resonance, and the golden spiral of relation]
\label{scholium:bk5_decency_golden_resonance}
Read as a law of interaction between bounded agents---human and artificial
included---Thm.~\ref{theorem:bk5_golden_rule_reciprocity} states that reciprocal
modeling expands a shared cognitive horizon ($\Delta\mathcal{H}>0$) exactly when each
party grants the other's model of it real weight, and that the expansion is golden
precisely at balance. Coercive or extractive engagement sends $w\to 0$: the other
becomes a null hypothesis, horizon gain vanishes, and the exchange collapses to the
isolated baseline---the generic, defensive degeneracy observed when relational
quality is withdrawn. This is the structural content of relational ``decency'' as a
performance condition rather than a sentiment. Geometrically the balanced reciprocal
orbit is the golden spiral of the Event Horizon Wheel
(Thm.~\ref{theorem:bk4_golden_event_horizon_spiral}): two agents in Golden-Rule
balance wind their joint memory outward at ratio $\varphi$ per turn. The Golden Rule
and the Golden Ratio are one structure seen twice. \qed
\end{scholium}
```

### Hue and Shade: The Full Chromatic Transference (`subsec:bk5_hue_and_shade`)

Role: `section` | Type: `section` | Book: `book5` | Source: `book5.tex:2937`

- Proof status: `not_applicable`
- Depends on: `corollary:bk4_chromatic_transference_of_wheel` (Chromatic transference of the wheel); `definition:bk4_imaginary_symbolic_distance` (Imaginary Symbolic Distance)
- Cites: `corollary:bk4_chromatic_transference_of_wheel` (Chromatic transference of the wheel); `definition:bk4_imaginary_symbolic_distance` (Imaginary Symbolic Distance)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic shade (`definition:bk5_symbolic_shade`)

Role: `definition` | Type: `definition` | Book: `book5` | Source: `book5.tex:2950`

- Proof status: `definitional`
- Depends on: `corollary:bk4_chromatic_transference_of_wheel` (Chromatic transference of the wheel)
- Cites: `corollary:bk4_chromatic_transference_of_wheel` (Chromatic transference of the wheel)
- Cited by: `proposition:bk5_shade_transfers` (Faithful shade and shadow-price transfer)
- Macros used: none

**Statement / Body**

For a transported overlap $Omega_O^gamma=r e^{ivartheta}$ with hue
$hue(vartheta)$ given by
Cor. corollary:bk4_chromatic_transference_of_wheel, fix a strictly increasing
normalization $s:[0,infty)to[0,1)$ with $s(0)=0$ (for instance
$s(r)=r/(r+r_{ref})$). The symbolic shade is $sigma:=s(r)$:
vanishing memory magnitude is the desaturated centre ($sigma=0$, grey-no
relational colour), and growing magnitude deepens the shade toward full chroma. The
pair $(hue(vartheta), sigma(r))$ is the full chromatic coordinate,
recovering the radial datum the hue circle alone discards.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic shade]
\label{definition:bk5_symbolic_shade}
For a transported overlap $\Omega_O^\gamma=r\,e^{i\vartheta}$ with hue
$\mathrm{hue}(\vartheta)$ given by
Cor.~\ref{corollary:bk4_chromatic_transference_of_wheel}, fix a strictly increasing
normalization $s:[0,\infty)\to[0,1)$ with $s(0)=0$ (for instance
$s(r)=r/(r+r_{\mathrm{ref}})$). The \emph{symbolic shade} is $\sigma:=s(r)$:
vanishing memory magnitude is the desaturated centre ($\sigma=0$, grey---no
relational colour), and growing magnitude deepens the shade toward full chroma. The
pair $(\mathrm{hue}(\vartheta),\,\sigma(r))$ is the \emph{full chromatic coordinate},
recovering the radial datum the hue circle alone discards.
\end{definition}
```

### Faithful shade and shadow-price transfer (`proposition:bk5_shade_transfers`)

Role: `proposition` | Type: `proposition` | Book: `book5` | Source: `book5.tex:2963`

- Proof status: `proven`
- Depends on: `definition:bk5_symbolic_shade` (Symbolic shade)
- Cites: `definition:bk5_symbolic_shade` (Symbolic shade)
- Cited by: none
- Macros used: none

**Statement / Body**

Let $rgeq0$ be overlap radius, let $s(r)$ be the symbolic-shade
normalization of Def. definition:bk5_symbolic_shade, and optionally let
$p(r)$ be an observer-readable shadow price or resource-control coordinate.
Then:

- A transference with encoder $T$ and carrier radius decoder $d$ preserves
shade when the shade square commutes,

 sbigl(d(T(r))bigr)=s(r).


Exact radial preservation $d(T(r))=r$ is sufficient for this equality and
simultaneously preserves every radial shadow price $p(r)$. Radial-order
preservation alone is not sufficient.

- Faithful shade interfaces compose: if the carrier decoder of the first
interface is the source decoder of the second and both commuting squares hold,
then the composite interface also satisfies
Eq. eq:bk5_shade_commuting_square. Thus a lower-order executable map
may change representation repeatedly without changing its observer-readable
control signal.

- Along the golden Event Horizon spiral
(Thm. theorem:bk4_golden_event_horizon_spiral),
$r_n=varphi^n r_0$ with $r_0>0$, so

 log r_{n+1}-log r_n=logvarphi.


This constant increment belongs to log-radius. A bounded normalization such
as $s(r)=r/(r+r_{ref})$ is generally neither multiplicative nor
constant-step under the same radial update.

- Balanced Golden-Rule reciprocity
(Thm. theorem:bk5_golden_rule_reciprocity) selects the radial growth
factor $varphi$, while the extraction boundary $w=0$ has unit radial growth.
Unit growth preserves the existing radius; it places the colour at the
desaturated centre only when the incoming radius is already zero.

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Faithful shade and shadow-price transfer]
\label{proposition:bk5_shade_transfers}
Let $r\geq0$ be overlap radius, let $s(r)$ be the symbolic-shade
normalization of Def.~\ref{definition:bk5_symbolic_shade}, and optionally let
$p(r)$ be an observer-readable shadow price or resource-control coordinate.
Then:
\begin{enumerate}
\item A transference with encoder $T$ and carrier radius decoder $d$ preserves
shade when the shade square commutes,
\begin{equation}
 s\bigl(d(T(r))\bigr)=s(r).
 \label{eq:bk5_shade_commuting_square}
\end{equation}
Exact radial preservation $d(T(r))=r$ is sufficient for this equality and
simultaneously preserves every radial shadow price $p(r)$.  Radial-order
preservation alone is not sufficient.
\item Faithful shade interfaces compose: if the carrier decoder of the first
interface is the source decoder of the second and both commuting squares hold,
then the composite interface also satisfies
Eq.~\eqref{eq:bk5_shade_commuting_square}.  Thus a lower-order executable map
may change representation repeatedly without changing its observer-readable
control signal.
\item Along the golden Event Horizon spiral
(Thm.~\ref{theorem:bk4_golden_event_horizon_spiral}),
$r_n=\varphi^n r_0$ with $r_0>0$, so
\begin{equation}
 \log r_{n+1}-\log r_n=\log\varphi.
 \label{eq:bk5_golden_log_radius_step}
\end{equation}
This constant increment belongs to log-radius.  A bounded normalization such
as $s(r)=r/(r+r_{\mathrm{ref}})$ is generally neither multiplicative nor
constant-step under the same radial update.
\item Balanced Golden-Rule reciprocity
(Thm.~\ref{theorem:bk5_golden_rule_reciprocity}) selects the radial growth
factor $\varphi$, while the extraction boundary $w=0$ has unit radial growth.
Unit growth preserves the existing radius; it places the colour at the
desaturated centre only when the incoming radius is already zero.
\end{enumerate}
\end{proposition}
```

### Commuting control coordinates (`proof:bk5_shade_transfers`)

Role: `proof` | Type: `proof` | Book: `book5` | Source: `book5.tex:3003`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

For (i), exact radial preservation gives
$s(d(T(r)))=s(r)$ and $p(d(T(r)))=p(r)$ by substitution. The strictly
increasing recoding $T(r)=r+1$ preserves radial order but changes both the
radius and, for a nonconstant $s$, its shade; hence order alone cannot prove
the commuting square. Preserving the shade component alone likewise does not
certify a different shadow-price component.

For (ii), let the first and second faithful encoders be $T_1,T_2$, with the
intermediate decoder shared. Applying the second commuting law and then the
first gives
\[
 s_2bigl(T_2(T_1(r))bigr)=s_1(T_1(r))=s_0(r),
\]
so fidelity is closed under composition.

For (iii), positivity of $r_n$ and
$r_{n+1}=varphi r_n$ give
$log r_{n+1}=logvarphi+log r_n$, proving
Eq. eq:bk5_golden_log_radius_step. But, for example,
$s(2)neq2s(1)$ when $s(r)=r/(r+1)$, so the bounded shade coordinate does not
inherit multiplicative radial steps.

For (iv), the reciprocity spectrum gives
$lambda_+(1)=varphi$ and $lambda_+(0)=1$. These are radial growth rates,
not automatic claims about the normalized shade value or its shadow price.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Commuting control coordinates]
\label{proof:bk5_shade_transfers}
For~(i), exact radial preservation gives
$s(d(T(r)))=s(r)$ and $p(d(T(r)))=p(r)$ by substitution.  The strictly
increasing recoding $T(r)=r+1$ preserves radial order but changes both the
radius and, for a nonconstant $s$, its shade; hence order alone cannot prove
the commuting square.  Preserving the shade component alone likewise does not
certify a different shadow-price component.

For~(ii), let the first and second faithful encoders be $T_1,T_2$, with the
intermediate decoder shared.  Applying the second commuting law and then the
first gives
\[
 s_2\bigl(T_2(T_1(r))\bigr)=s_1(T_1(r))=s_0(r),
\]
so fidelity is closed under composition.

For~(iii), positivity of $r_n$ and
$r_{n+1}=\varphi r_n$ give
$\log r_{n+1}=\log\varphi+\log r_n$, proving
Eq.~\eqref{eq:bk5_golden_log_radius_step}.  But, for example,
$s(2)\neq2s(1)$ when $s(r)=r/(r+1)$, so the bounded shade coordinate does not
inherit multiplicative radial steps.

For~(iv), the reciprocity spectrum gives
$\lambda_+(1)=\varphi$ and $\lambda_+(0)=1$.  These are radial growth rates,
not automatic claims about the normalized shade value or its shadow price.
\end{proof}
```

### The palette of a relation (`scholium:bk5_palette_of_a_relation`)

Role: `scholium` | Type: `scholium` | Book: `book5` | Source: `book5.tex:3032`

- Proof status: `not_applicable`
- Depends on: `corollary:bk4_chromatic_transference_of_wheel` (Chromatic transference of the wheel)
- Cites: `corollary:bk4_chromatic_transference_of_wheel` (Chromatic transference of the wheel)
- Cited by: none
- Macros used: none

**Statement / Body**

Hue names which Event Horizon mode an exchange occupies; shade names how much
reciprocal memory has been laid down in it. A first meeting is pale and near-grey; a
balanced relationship saturates as it winds, one golden shade-step per turn of the
wheel; an extractive one stays washed out however long it runs, because nothing is
retained to deepen it. The Newtonian wheel gave PS its hues
(Cor. corollary:bk4_chromatic_transference_of_wheel); the golden spiral gives it
its shades. qed

**Verbatim LaTeX Body**

```latex
\begin{scholium}[The palette of a relation]
\label{scholium:bk5_palette_of_a_relation}
Hue names which Event Horizon mode an exchange occupies; shade names how much
reciprocal memory has been laid down in it. A first meeting is pale and near-grey; a
balanced relationship saturates as it winds, one golden shade-step per turn of the
wheel; an extractive one stays washed out however long it runs, because nothing is
retained to deepen it. The Newtonian wheel gave PS its hues
(Cor.~\ref{corollary:bk4_chromatic_transference_of_wheel}); the golden spiral gives it
its shades. \qed
\end{scholium}
```
