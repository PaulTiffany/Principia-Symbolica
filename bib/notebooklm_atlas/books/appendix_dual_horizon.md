# Principia Symbolica NotebookLM Atlas - appendix_dual_horizon

Nodes in this source group: 123

Each card preserves label, role, source location, proof status, complete supports, complete uses, macros, and full cleaned body text.
When enabled, verbatim LaTeX appears after the readable body for exact-source recovery.

### Dual Horizon – A Formal Proof by Elimination (`sec:appC_dual_horizon`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:3`

- Proof status: `not_applicable`
- Depends on: `definition:bk4_bounded_observer` (Bounded Observer); `definition:bk6_drift_operator_complete` (Drift Operator); `definition:bk6_reflection_operator_complete` (Reflection Operator); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `definition:bk4_bounded_observer` (Bounded Observer); `definition:bk6_drift_operator_complete` (Drift Operator); `definition:bk6_reflection_operator_complete` (Reflection Operator); `scholium:appC_two_modalities_one_root` (Two Modalities, One Root); `sec:appC_proof_by_elimination` (Proof II --- Effective-Signature (Geometric)); `sec:appC_proof_observational` (Proof I --- Observational Elimination); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: `remark:bk9_grace_flow_geometric_witness` (Geometric witness: grace as curvature flow); `sec:bk1_prefatio` (Prefatio)
- Macros used: none

**Statement / Body**

(no body text extracted)

### C.0.1 Method: two eliminations, one root (`subsec:appC_methodological_logical_framework`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:7`

- Proof status: `not_applicable`
- Depends on: none
- Cites: `assumption:appC_emergence_coupling` (Emergence Coupling lower bound); `assumption:appC_emergence_domination` (Emergence Domination); `remark:appC_domination_open_route` (Open derivation route for Emergence Domination); `sec:appC_born_rule` (Born Rule – A Formal Derivation); `sec:appC_proof_by_elimination` (Proof II --- Effective-Signature (Geometric)); `sec:appC_proof_observational` (Proof I --- Observational Elimination)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Formal Statement: Dual Horizon as Effective Signature (`sec:appC_formal_statement_dual_horizon_thesis`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:10`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Observer-visible symbolic system (`definition:appC_observer_visible_system`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:12`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk4_bounded_observer` (Bounded Observer); `definition:bk4_observer_kernel_convolution_map` (Observer-Kernel Convolution); `definition:bk6_drift_operator_complete` (Drift Operator); `definition:bk6_reflection_operator_complete` (Reflection Operator)
- Cites: `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk4_bounded_observer` (Bounded Observer); `definition:bk4_observer_kernel_convolution_map` (Observer-Kernel Convolution); `definition:bk6_drift_operator_complete` (Drift Operator); `definition:bk6_reflection_operator_complete` (Reflection Operator)
- Cited by: none
- Macros used: `\Obs`, `\drift`, `\manifold`

**Statement / Body**

A bounded symbolic dynamical system is a tuple
\((manifold, g, drift, R_{stab}, Obs)\), where \(manifold\) is a
symbolic manifold (cf. definition:bk1_symbolic_manifold) with metric \(g\),
\(drift\) is the drift field (cf. definition:bk6_drift_operator_complete),
\(R_{stab}\) is the stabilizing reflection field
(cf. definition:bk6_reflection_operator_complete), and \(Obs\) is a Bounded
Observer (cf. definition:bk4_bounded_observer) with resolution threshold
\(epsilon_{Obs}\). The observer-visible domain \(Omegasubseteqmanifold\)
is the region resolved by \(Obs\) above \(epsilon_{Obs}\), carrying the
resolution-weighted observer measure \(mu_{Obs}\) induced by the observer kernel
(cf. definition:bk4_observer_kernel_convolution_map).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Observer-visible symbolic system]
\label{definition:appC_observer_visible_system}
A \emph{bounded symbolic dynamical system} is a tuple
\((\manifold, g, \drift, R_{\mathrm{stab}}, \Obs)\), where \(\manifold\) is a
symbolic manifold (cf.~\ref{definition:bk1_symbolic_manifold}) with metric \(g\),
\(\drift\) is the drift field (cf.~\ref{definition:bk6_drift_operator_complete}),
\(R_{\mathrm{stab}}\) is the stabilizing reflection field
(cf.~\ref{definition:bk6_reflection_operator_complete}), and \(\Obs\) is a Bounded
Observer (cf.~\ref{definition:bk4_bounded_observer}) with resolution threshold
\(\epsilon_{\Obs}\). The \emph{observer-visible domain} \(\Omega\subseteq\manifold\)
is the region resolved by \(\Obs\) above \(\epsilon_{\Obs}\), carrying the
resolution-weighted observer measure \(\mu_{\Obs}\) induced by the observer kernel
(cf.~\ref{definition:bk4_observer_kernel_convolution_map}).
\end{definition}
```

### Generative and stabilizing horizon fluxes (`definition:appC_horizon_fluxes`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:27`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `remark:appC_horizon_realizations` (Invariance under horizon realization)
- Macros used: `\Obs`, `\drift`

**Statement / Body**

On the observer-visible domain \(Omega\) define the generative flux
\[
G_{Obs}(Omega) := int_Omega big(nabla\!cdotdriftbig)_+ dmu_{Obs},
 (x)_+ := max{x,0},
\]
and the stabilizing flux
\[
C_{Obs}(Omega) := int_Omega big(-nabla\!cdot R_{stab}big)_+ dmu_{Obs}.
\]
Thus \(G_{Obs}\) accumulates the observer-visible rate at which Drift sources
novelty (positive divergence) and \(C_{Obs}\) the rate at which stabilizing
Reflection sinks it (negative divergence). Up to the divergence theorem,
\(int_Omega nabla\!cdotdrift dmu_{Obs}\) is the net Drift flux across the
resolution boundary \(partialOmega\) - the observer's horizon - and
\(G_{Obs}\) retains only its sourcing part; symmetrically for \(C_{Obs}\). This is
the precise sense in which the two are horizon-effects, defined independently of how
many geometric horizons realize them.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Generative and stabilizing horizon fluxes]
\label{definition:appC_horizon_fluxes}
On the observer-visible domain \(\Omega\) define the \emph{generative flux}
\[
G_{\Obs}(\Omega) := \int_\Omega \big(\nabla\!\cdot\drift\big)_+ \, d\mu_{\Obs},
\qquad (x)_+ := \max\{x,0\},
\]
and the \emph{stabilizing flux}
\[
C_{\Obs}(\Omega) := \int_\Omega \big(-\nabla\!\cdot R_{\mathrm{stab}}\big)_+ \, d\mu_{\Obs}.
\]
Thus \(G_{\Obs}\) accumulates the observer-visible rate at which Drift \emph{sources}
novelty (positive divergence) and \(C_{\Obs}\) the rate at which stabilizing
Reflection \emph{sinks} it (negative divergence). Up to the divergence theorem,
\(\int_\Omega \nabla\!\cdot\drift \, d\mu_{\Obs}\) is the net Drift flux across the
resolution boundary \(\partial\Omega\) --- the observer's \emph{horizon} --- and
\(G_{\Obs}\) retains only its sourcing part; symmetrically for \(C_{\Obs}\). This is
the precise sense in which the two are horizon-effects, defined independently of how
many geometric horizons realize them.
\end{definition}
```

### Bounded reflexive emergence (`definition:appC_bounded_reflexive_emergence`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:48`

- Proof status: `definitional`
- Depends on: `definition:bk1_stage_composite_operator` (Stage–Composite Operator); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cites: `definition:bk1_stage_composite_operator` (Stage–Composite Operator); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cited by: `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Macros used: `\Obs`, `\drift`, `\freeenergy`

**Statement / Body**

The system exhibits bounded reflexive emergence on \(Omega\) over a
symbolic-time interval \(I\) if the observer-visible emergence functional
\(DeltaPhi_{Obs}\) - the net gain over \(I\) of retained, resolved coherent
structure produced by the coupled action of \(drift\) and \(R_{stab}\) (the
stage-composite emergence of Def. definition:bk1_stage_composite_operator,
measured as stabilized reduction of symbolic free energy \(freeenergy\),
cf. definition:bk2_symbolic_free_energy) - satisfies
\[
DeltaPhi_{Obs}(drift, R_{stab}) ge tau_E > 0
\]
for an observer-fixed emergence threshold \(tau_E\).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Bounded reflexive emergence]
\label{definition:appC_bounded_reflexive_emergence}
The system exhibits \emph{bounded reflexive emergence} on \(\Omega\) over a
symbolic-time interval \(I\) if the observer-visible emergence functional
\(\Delta\Phi_{\Obs}\) --- the net gain over \(I\) of retained, resolved coherent
structure produced by the coupled action of \(\drift\) and \(R_{\mathrm{stab}}\) (the
stage-composite emergence of Def.~\ref{definition:bk1_stage_composite_operator},
measured as stabilized reduction of symbolic free energy \(\freeenergy\),
cf.~\ref{definition:bk2_symbolic_free_energy}) --- satisfies
\[
\Delta\Phi_{\Obs}(\drift, R_{\mathrm{stab}}) \;\ge\; \tau_E \;>\; 0
\]
for an observer-fixed emergence threshold \(\tau_E\).
\end{definition}
```

### Emergence Domination (`assumption:appC_emergence_domination`)

Role: `assumption` | Type: `assumption` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:63`

- Proof status: `definitional`
- Depends on: none
- Cites: `definition:appC_observer_coherence_budget` (Observer coherence budget)
- Cited by: `proof:appC_dual_horizon_biconditional`; `proof:appC_dual_horizon_signature_geometric` (Proof of Theorem~\ref{theorem:appC_dual_horizon_signature} (geometric modality)); `remark:appC_domination_open_route` (Open derivation route for Emergence Domination); `subsec:appC_methodological_logical_framework` (C.0.1 Method: two eliminations, one root); `theorem:appC_dual_horizon_biconditional` (Emergence is sandwiched by the dual signature); `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Macros used: `\Obs`, `\drift`

**Statement / Body**

Observer-visible emergence cannot exceed the budget of the binding flux:
there is a finite gain constant \(Lambda=Lambda(epsilon_{Obs})\) with
\[
DeltaPhi_{Obs}(drift, R_{stab})
 le Lambda cdot minbig{ G_{Obs}(Omega), C_{Obs}(Omega) big}.
\]
This is symbolic-budget bookkeeping, not a dynamical postulate (cf. the token-budget
bound of Def. definition:appC_observer_coherence_budget): retained novelty
visible to \(Obs\) can be neither more than was generated nor more than was
stabilized, so it is bounded by the smaller of the two. Where one flux vanishes, no
emergence above the floor is available.

**Verbatim LaTeX Body**

```latex
\begin{assumption}[Emergence Domination]
\label{assumption:appC_emergence_domination}
Observer-visible emergence cannot exceed the budget of the \emph{binding} flux:
there is a finite gain constant \(\Lambda=\Lambda(\epsilon_{\Obs})\) with
\[
\Delta\Phi_{\Obs}(\drift, R_{\mathrm{stab}})
\;\le\; \Lambda \cdot \min\big\{\,G_{\Obs}(\Omega),\, C_{\Obs}(\Omega)\,\big\}.
\]
This is symbolic-budget bookkeeping, not a dynamical postulate (cf. the token-budget
bound of Def.~\ref{definition:appC_observer_coherence_budget}): retained novelty
visible to \(\Obs\) can be neither more than was generated nor more than was
stabilized, so it is bounded by the smaller of the two. Where one flux vanishes, no
emergence above the floor is available.
\end{assumption}
```

### Dual Horizon Necessity (Effective Signature) (`theorem:appC_dual_horizon_signature`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:78`

- Proof status: `proven`
- Depends on: `assumption:appC_emergence_domination` (Emergence Domination); `definition:appC_bounded_reflexive_emergence` (Bounded reflexive emergence); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cites: `assumption:appC_emergence_domination` (Emergence Domination); `definition:appC_bounded_reflexive_emergence` (Bounded reflexive emergence); `sec:appC_proof_by_elimination` (Proof II --- Effective-Signature (Geometric)); `sec:appC_proof_observational` (Proof I --- Observational Elimination); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Cited by: `proof:appC_dual_horizon_biconditional`; `proof:bk1_proof_of_dual_horizon_necessity_theorem` (Proof of Dual Horizon Necessity Theorem); `remark:appC_horizon_realizations` (Invariance under horizon realization); `sec:appC_proof_by_elimination` (Proof II --- Effective-Signature (Geometric)); `sec:appC_proof_observational` (Proof I --- Observational Elimination); `theorem:bk1_dual_horizon_necessity_theorem` (Dual Horizon Necessity Theorem)
- Macros used: `\Obs`, `\drift`, `\manifold`

**Statement / Body**

This is the expanded, realization-invariant form of the canonical Book I theorem
(Thm. theorem:bk1_dual_horizon_necessity_theorem); Book I carries the
statement of record, and what follows is its full derivation and defense.
Let \((manifold, g, drift, R_{stab}, Obs)\) be a bounded symbolic
dynamical system that exhibits bounded reflexive emergence on \(Omega\)
(Def. definition:appC_bounded_reflexive_emergence). Then
\[
G_{Obs}(Omega) > 0 text{and} C_{Obs}(Omega) > 0 .
\]
That is, the observer-visible flux carries a dual effective horizon signature
on the shared domain \(Omega\): one positive/generative and one
negative/stabilizing component, invariant under the geometric realization of those
components. The conclusion is established twice below: observationally, from Bounded
Observability alone (Proof I, Ssec:appC_proof_observational), and
geometrically, from Emergence Domination
(Assumption assumption:appC_emergence_domination; Proof II,
Ssec:appC_proof_by_elimination).

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Dual Horizon Necessity (Effective Signature)]
\label{theorem:appC_dual_horizon_signature}
This is the expanded, realization-invariant form of the canonical Book~I theorem
(Thm.~\ref{theorem:bk1_dual_horizon_necessity_theorem}); Book~I carries the
statement of record, and what follows is its full derivation and defense.
Let \((\manifold, g, \drift, R_{\mathrm{stab}}, \Obs)\) be a bounded symbolic
dynamical system that exhibits bounded reflexive emergence on \(\Omega\)
(Def.~\ref{definition:appC_bounded_reflexive_emergence}). Then
\[
G_{\Obs}(\Omega) > 0 \qquad\text{and}\qquad C_{\Obs}(\Omega) > 0 .
\]
That is, the observer-visible flux carries a \emph{dual effective horizon signature}
on the shared domain \(\Omega\): one positive/generative and one
negative/stabilizing component, invariant under the geometric realization of those
components. The conclusion is established twice below: observationally, from Bounded
Observability alone (Proof~I, \S\ref{sec:appC_proof_observational}), and
geometrically, from Emergence Domination
(Assumption~\ref{assumption:appC_emergence_domination}; Proof~II,
\S\ref{sec:appC_proof_by_elimination}).
\end{theorem}
```

### Proof I --- Observational Elimination (`sec:appC_proof_observational`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:99`

- Proof status: `not_applicable`
- Depends on: `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Cites: `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Cited by: `scholium:appC_two_modalities_one_root` (Two Modalities, One Root); `sec:appC_dual_horizon` (Dual Horizon – A Formal Proof by Elimination); `subsec:appC_methodological_logical_framework` (C.0.1 Method: two eliminations, one root); `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Macros used: none

**Statement / Body**

(no body text extracted)

### Proof of Theorem~\ref{theorem:appC_dual_horizon_signature} (observational modality) (`proof:appC_dual_horizon_signature_observational`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:105`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: `\Obs`, `\identity`, `\manifold`

**Statement / Body**

Assume bounded reflexive emergence, \(DeltaPhi_{Obs}getau_E>0\): over \(I\) the
observer registers and retains new coherent structure on \(Omega\). We
eliminate, in turn, the three ways the dual signature can fail - novelty that never
crosses the horizon, novelty that crosses but is never stabilized, and the two alive
yet never meeting on a single observer's domain.

textbf{Case A (no observer-visible generation): \(G_{Obs}(Omega)=0\).} No novelty
is sourced across the horizon into \(Omega\) that the observer can resolve above
\(epsilon_{Obs}\). Over \(I\) it therefore registers no new differentiated
content - only rearrangement below resolution, bare repetition, or decay. Retained
new structure presupposes registered new content; with none, \(DeltaPhi_{Obs}\)
cannot rise to \(tau_E\). One cannot retain what was never observed to enter.
Contradiction.

textbf{Case B (no observer-visible stabilization): \(C_{Obs}(Omega)=0\).} Novelty
is sourced but nothing contracts or integrates it on \(Omega\). Relative to finite
resolution \(epsilon_{Obs}\), unintegrated novelty disperses or saturates the
observer's channel: it may be registered transiently but is not retained as
stable identity \(identity\) across \(I\). Since \(DeltaPhi_{Obs}\) counts
retained structure, it stays below \(tau_E\). Novelty seen but not kept is not
emergence. Contradiction.

Case C (generation and stabilization in different observer patches). Suppose
both occur in \(manifold\) but not within one resolved domain \(Omega\). The
observer integrates emergence over a single \(Omega\); on it, the absent
contribution lies outside the patch or below \(epsilon_{Obs}\), so that \(Omega\)
reduces to Case A or Case B. No single bounded observer registers coupled becoming.
Contradiction.

In each case the observer fails to register retained emergence, contradicting
\(DeltaPhi_{Obs}getau_E\). Hence both an observer-visible generative contribution
and an observer-visible stabilizing contribution must be present on the shared
\(Omega\); that is, \(G_{Obs}(Omega)>0\) and \(C_{Obs}(Omega)>0\).

**Verbatim LaTeX Body**

```latex
\begin{proof}[Proof of Theorem~\ref{theorem:appC_dual_horizon_signature} (observational modality)]
\label{proof:appC_dual_horizon_signature_observational}
\leavevmode

Assume bounded reflexive emergence, \(\Delta\Phi_{\Obs}\ge\tau_E>0\): over \(I\) the
observer registers and \emph{retains} new coherent structure on \(\Omega\). We
eliminate, in turn, the three ways the dual signature can fail --- novelty that never
crosses the horizon, novelty that crosses but is never stabilized, and the two alive
yet never meeting on a single observer's domain.

\textbf{Case A (no observer-visible generation): \(G_{\Obs}(\Omega)=0\).} No novelty
is sourced across the horizon into \(\Omega\) that the observer can resolve above
\(\epsilon_{\Obs}\). Over \(I\) it therefore registers no \emph{new} differentiated
content --- only rearrangement below resolution, bare repetition, or decay. Retained
new structure presupposes registered new content; with none, \(\Delta\Phi_{\Obs}\)
cannot rise to \(\tau_E\). One cannot retain what was never observed to enter.
Contradiction.

\textbf{Case B (no observer-visible stabilization): \(C_{\Obs}(\Omega)=0\).} Novelty
is sourced but nothing contracts or integrates it on \(\Omega\). Relative to finite
resolution \(\epsilon_{\Obs}\), unintegrated novelty disperses or saturates the
observer's channel: it may be registered transiently but is not \emph{retained} as
stable identity \(\identity\) across \(I\). Since \(\Delta\Phi_{\Obs}\) counts
retained structure, it stays below \(\tau_E\). Novelty seen but not kept is not
emergence. Contradiction.

\textbf{Case C (generation and stabilization in different observer patches).} Suppose
both occur in \(\manifold\) but not within one resolved domain \(\Omega\). The
observer integrates emergence over a single \(\Omega\); on it, the absent
contribution lies outside the patch or below \(\epsilon_{\Obs}\), so that \(\Omega\)
reduces to Case~A or Case~B. No single bounded observer registers coupled becoming.
Contradiction.

In each case the observer fails to register retained emergence, contradicting
\(\Delta\Phi_{\Obs}\ge\tau_E\). Hence both an observer-visible generative contribution
and an observer-visible stabilizing contribution must be present on the shared
\(\Omega\); that is, \(G_{\Obs}(\Omega)>0\) and \(C_{\Obs}(\Omega)>0\).
\end{proof}
```

### Proof II --- Effective-Signature (Geometric) (`sec:appC_proof_by_elimination`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:144`

- Proof status: `not_applicable`
- Depends on: `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Cites: `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Cited by: `scholium:appC_two_modalities_one_root` (Two Modalities, One Root); `sec:appC_dual_horizon` (Dual Horizon – A Formal Proof by Elimination); `subsec:appC_methodological_logical_framework` (C.0.1 Method: two eliminations, one root); `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Macros used: none

**Statement / Body**

(no body text extracted)

### Proof of Theorem~\ref{theorem:appC_dual_horizon_signature} (geometric modality) (`proof:appC_dual_horizon_signature_geometric`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:148`

- Proof status: `not_applicable`
- Depends on: `assumption:appC_emergence_domination` (Emergence Domination)
- Cites: `assumption:appC_emergence_domination` (Emergence Domination)
- Cited by: none
- Macros used: `\Obs`, `\drift`, `\freeenergy`, `\identity`, `\manifold`

**Statement / Body**

Assume bounded reflexive emergence, \(DeltaPhi_{Obs}getau_E>0\). The dual
signature ``\(G_{Obs}(Omega)>0\) and \(C_{Obs}(Omega)>0\)'' can fail in exactly
three ways; we eliminate each.

textbf{Case A (no generative flux on \(Omega\)): \(G_{Obs}(Omega)=0\).} Then
\(min{G_{Obs},C_{Obs}}=0\), and Emergence Domination
(Assumption assumption:appC_emergence_domination) gives
\(DeltaPhi_{Obs}le Lambdacdot 0 = 0 < tau_E\), contradicting emergence.
Symbolically: Drift may be formally nonzero, yet it sources no observer-visible
novelty across the horizon - transport below \(epsilon_{Obs}\), bare repetition,
or collapse - so no new structure arises to be retained.

textbf{Case B (no stabilizing flux on \(Omega\)): \(C_{Obs}(Omega)=0\).} Again
\(min=0\) and \(DeltaPhi_{Obs}le 0<tau_E\), a contradiction. Symbolically:
novelty is generated but never contracted or integrated; symbolic free energy
\(freeenergy\) is not stably reduced, and the differentiated content disperses below
resolution before it can register as retained identity (\(identity\)). Generation
without a sink is flux, not emergence.

Case C (no shared domain). Suppose instead that both signs occur somewhere
in \(manifold\) - \((nabla\!cdotdrift)_+>0\) on some region and
\((-nabla\!cdot R_{stab})_+>0\) on another - but their observer-visible
supports do not both meet a common \(Omega\). Then on the domain over which \(Obs\)
actually integrates emergence, at least one integrand vanishes
\(mu_{Obs}\)-almost everywhere, so \(G_{Obs}(Omega)=0\) or
\(C_{Obs}(Omega)=0\), returning us to Case A or B. Uncoupled generation and
stabilization, however vigorous in separate observer patches, produce no reflexive
emergence for \(Obs\).

In every case \(DeltaPhi_{Obs}<tau_E\), contradicting the hypothesis. Hence both
fluxes are strictly positive on a shared \(Omega\): the dual effective signature is
necessary.

**Verbatim LaTeX Body**

```latex
\begin{proof}[Proof of Theorem~\ref{theorem:appC_dual_horizon_signature} (geometric modality)]
\label{proof:appC_dual_horizon_signature_geometric}
\leavevmode

Assume bounded reflexive emergence, \(\Delta\Phi_{\Obs}\ge\tau_E>0\). The dual
signature ``\(G_{\Obs}(\Omega)>0\) and \(C_{\Obs}(\Omega)>0\)'' can fail in exactly
three ways; we eliminate each.

\textbf{Case A (no generative flux on \(\Omega\)): \(G_{\Obs}(\Omega)=0\).} Then
\(\min\{G_{\Obs},C_{\Obs}\}=0\), and Emergence Domination
(Assumption~\ref{assumption:appC_emergence_domination}) gives
\(\Delta\Phi_{\Obs}\le \Lambda\cdot 0 = 0 < \tau_E\), contradicting emergence.
Symbolically: Drift may be formally nonzero, yet it sources no observer-visible
novelty across the horizon --- transport below \(\epsilon_{\Obs}\), bare repetition,
or collapse --- so no new structure arises to be retained.

\textbf{Case B (no stabilizing flux on \(\Omega\)): \(C_{\Obs}(\Omega)=0\).} Again
\(\min=0\) and \(\Delta\Phi_{\Obs}\le 0<\tau_E\), a contradiction. Symbolically:
novelty is generated but never contracted or integrated; symbolic free energy
\(\freeenergy\) is not stably reduced, and the differentiated content disperses below
resolution before it can register as retained identity (\(\identity\)). Generation
without a sink is flux, not emergence.

\textbf{Case C (no shared domain).} Suppose instead that both signs occur somewhere
in \(\manifold\) --- \((\nabla\!\cdot\drift)_+>0\) on some region and
\((-\nabla\!\cdot R_{\mathrm{stab}})_+>0\) on another --- but their observer-visible
supports do not both meet a common \(\Omega\). Then on the domain over which \(\Obs\)
actually integrates emergence, at least one integrand vanishes
\(\mu_{\Obs}\)-almost everywhere, so \(G_{\Obs}(\Omega)=0\) or
\(C_{\Obs}(\Omega)=0\), returning us to Case A or B. Uncoupled generation and
stabilization, however vigorous in separate observer patches, produce no reflexive
emergence for \(\Obs\).

In every case \(\Delta\Phi_{\Obs}<\tau_E\), contradicting the hypothesis. Hence both
fluxes are strictly positive on a shared \(\Omega\): the dual effective signature is
necessary.
\end{proof}
```

### Sufficiency and the Conditional Biconditional (`subsec:appC_conclusion_of_proof_by_elimination`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:190`

- Proof status: `not_applicable`
- Depends on: none
- Cites: `axiom:appC_psc3prime` (PS--C3$'$ (Non-contextual token budget))
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Emergence Coupling lower bound (`assumption:appC_emergence_coupling`)

Role: `assumption` | Type: `assumption` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:197`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `proof:appC_dual_horizon_biconditional`; `subsec:appC_methodological_logical_framework` (C.0.1 Method: two eliminations, one root); `theorem:appC_dual_horizon_biconditional` (Emergence is sandwiched by the dual signature)
- Macros used: `\Obs`, `\drift`

**Statement / Body**

There is a coupling gain \(kappa=kappa(epsilon_{Obs})>0\) such that, when both
fluxes are present and interact on the shared domain \(Omega\),
\[
DeltaPhi_{Obs}(drift, R_{stab})
 ge kappacdotminbig{ G_{Obs}(Omega), C_{Obs}(Omega) big}.
\]
Necessarily \(kappaleLambda\), since both bounds hold simultaneously.

**Verbatim LaTeX Body**

```latex
\begin{assumption}[Emergence Coupling lower bound]
\label{assumption:appC_emergence_coupling}
There is a coupling gain \(\kappa=\kappa(\epsilon_{\Obs})>0\) such that, when both
fluxes are present and interact on the shared domain \(\Omega\),
\[
\Delta\Phi_{\Obs}(\drift, R_{\mathrm{stab}})
\;\ge\; \kappa\cdot\min\big\{\,G_{\Obs}(\Omega),\, C_{\Obs}(\Omega)\,\big\}.
\]
Necessarily \(\kappa\le\Lambda\), since both bounds hold simultaneously.
\end{assumption}
```

### Emergence is sandwiched by the dual signature (`theorem:appC_dual_horizon_biconditional`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:208`

- Proof status: `proven`
- Depends on: `assumption:appC_emergence_coupling` (Emergence Coupling lower bound); `assumption:appC_emergence_domination` (Emergence Domination); `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Cites: `assumption:appC_emergence_coupling` (Emergence Coupling lower bound); `assumption:appC_emergence_domination` (Emergence Domination)
- Cited by: `scholium:appC_two_horizons_co_constitutive` (The Two Horizons as Co-Constitutive)
- Macros used: `\Obs`, `\drift`

**Statement / Body**

Under Emergence Domination and Emergence Coupling
(Assumptions assumption:appC_emergence_domination, assumption:appC_emergence_coupling),
write \(m:=min{G_{Obs}(Omega),C_{Obs}(Omega)}\). Then
\[
kappa m le DeltaPhi_{Obs}(drift,R_{stab}) le Lambda m .
\]
Consequently:

- (Sufficiency) \(m ge tau_E/kappa Rightarrow DeltaPhi_{Obs}getau_E\);

- (Necessity) \(DeltaPhi_{Obs}getau_E Rightarrow m ge tau_E/Lambda > 0\).

In the tight-bookkeeping case \(kappa=Lambda=:Gamma\) the two collapse to an exact
biconditional, \( DeltaPhi_{Obs}getau_E iff mgetau_E/Gamma\).

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Emergence is sandwiched by the dual signature]
\label{theorem:appC_dual_horizon_biconditional}
Under Emergence Domination and Emergence Coupling
(Assumptions~\ref{assumption:appC_emergence_domination},~\ref{assumption:appC_emergence_coupling}),
write \(m:=\min\{G_{\Obs}(\Omega),C_{\Obs}(\Omega)\}\). Then
\[
\kappa\, m \;\le\; \Delta\Phi_{\Obs}(\drift,R_{\mathrm{stab}}) \;\le\; \Lambda\, m .
\]
Consequently:
\begin{enumerate}[label=(\roman*)]
\item \emph{(Sufficiency)} \(m \ge \tau_E/\kappa \;\Rightarrow\; \Delta\Phi_{\Obs}\ge\tau_E\);
\item \emph{(Necessity)} \(\Delta\Phi_{\Obs}\ge\tau_E \;\Rightarrow\; m \ge \tau_E/\Lambda > 0\).
\end{enumerate}
In the tight-bookkeeping case \(\kappa=\Lambda=:\Gamma\) the two collapse to an exact
biconditional, \(\;\Delta\Phi_{\Obs}\ge\tau_E \iff m\ge\tau_E/\Gamma\).
\end{theorem}
```

### proof:appC_dual_horizon_biconditional (`proof:appC_dual_horizon_biconditional`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:224`

- Proof status: `not_applicable`
- Depends on: `assumption:appC_emergence_coupling` (Emergence Coupling lower bound); `assumption:appC_emergence_domination` (Emergence Domination); `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Cites: `assumption:appC_emergence_coupling` (Emergence Coupling lower bound); `assumption:appC_emergence_domination` (Emergence Domination); `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

The sandwich is the conjunction of
Assumptions assumption:appC_emergence_domination
and assumption:appC_emergence_coupling. For (i),
\(DeltaPhi_{Obs}gekappa mgekappacdot(tau_E/kappa)=tau_E\). For (ii),
\(tau_EleDeltaPhi_{Obs}leLambda m\) gives \(mgetau_E/Lambda>0\); positivity
of \(m\) recovers Theorem theorem:appC_dual_horizon_signature. When
\(kappa=Lambda=Gamma\) the lower and upper thresholds coincide at
\(tau_E/Gamma\), yielding the biconditional.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_dual_horizon_biconditional}
The sandwich is the conjunction of
Assumptions~\ref{assumption:appC_emergence_domination}
and~\ref{assumption:appC_emergence_coupling}. For (i),
\(\Delta\Phi_{\Obs}\ge\kappa m\ge\kappa\cdot(\tau_E/\kappa)=\tau_E\). For (ii),
\(\tau_E\le\Delta\Phi_{\Obs}\le\Lambda m\) gives \(m\ge\tau_E/\Lambda>0\); positivity
of \(m\) recovers Theorem~\ref{theorem:appC_dual_horizon_signature}. When
\(\kappa=\Lambda=\Gamma\) the lower and upper thresholds coincide at
\(\tau_E/\Gamma\), yielding the biconditional.
\end{proof}
```

### Invariance under horizon realization (`remark:appC_horizon_realizations`)

Role: `remark` | Type: `remark` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:236`

- Proof status: `not_applicable`
- Depends on: `definition:appC_horizon_fluxes` (Generative and stabilizing horizon fluxes); `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Cites: `definition:appC_horizon_fluxes` (Generative and stabilizing horizon fluxes); `theorem:appC_dual_horizon_signature` (Dual Horizon Necessity (Effective Signature))
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

Both fluxes are integrals of positive parts of divergences against \(mu_{Obs}\);
nothing in Definition definition:appC_horizon_fluxes or
Theorem theorem:appC_dual_horizon_signature counts horizons. The same
signature \((G_{Obs}>0, C_{Obs}>0)\) is produced by (i) a single
generative/dissipative horizon pair; (ii) several same-sign horizons, whose positive
parts simply add; (iii) one sign-changing curvature field, whose positive and
negative divergence parts feed \(G_{Obs}\) and \(C_{Obs}\) respectively; (iv) a
smooth, delocalized source-sink field with no isolated horizon at all. The theorem
therefore does not fail on multi-horizon or sign-changing configurations - the
liability of the literal reading - because ``dual'' is a property of the
observer-visible flux signature, not of the geometry that realizes it.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Invariance under horizon realization]
\label{remark:appC_horizon_realizations}
Both fluxes are integrals of positive parts of divergences against \(\mu_{\Obs}\);
nothing in Definition~\ref{definition:appC_horizon_fluxes} or
Theorem~\ref{theorem:appC_dual_horizon_signature} counts horizons. The same
signature \((G_{\Obs}>0,\,C_{\Obs}>0)\) is produced by (i) a single
generative/dissipative horizon pair; (ii) several same-sign horizons, whose positive
parts simply add; (iii) one sign-changing curvature field, whose positive and
negative divergence parts feed \(G_{\Obs}\) and \(C_{\Obs}\) respectively; (iv) a
smooth, delocalized source--sink field with no isolated horizon at all. The theorem
therefore does not fail on multi-horizon or sign-changing configurations --- the
liability of the literal reading --- because ``dual'' is a property of the
observer-visible flux signature, not of the geometry that realizes it.
\end{remark}
```

### Open derivation route for Emergence Domination (`remark:appC_domination_open_route`)

Role: `remark` | Type: `remark` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:251`

- Proof status: `not_applicable`
- Depends on: `assumption:appC_emergence_domination` (Emergence Domination); `definition:bk4_observer_kernel_convolution_map` (Observer-Kernel Convolution)
- Cites: `assumption:appC_emergence_domination` (Emergence Domination); `axiom:appC_psc3prime` (PS--C3$'$ (Non-contextual token budget)); `definition:bk4_observer_kernel_convolution_map` (Observer-Kernel Convolution)
- Cited by: `scholium:appC_two_modalities_one_root` (Two Modalities, One Root); `subsec:appC_methodological_logical_framework` (C.0.1 Method: two eliminations, one root)
- Macros used: `\Obs`

**Statement / Body**

Emergence Domination (Assumption assumption:appC_emergence_domination) is the
single posited plank of Proof II, and it is where any residual circularity would
hide: were \(DeltaPhi_{Obs}\), \(G_{Obs}\), \(C_{Obs}\) not independently
measured, the bound would be analytic and the theorem would prove only what it
assumed. The route that would make it synthetic runs through finite observer
bandwidth: the bounded-observer kernel
(cf. definition:bk4_observer_kernel_convolution_map) has finite throughput
across the resolution boundary \(partialOmega\), so it cannot retain coherent
novelty faster than the binding flux carries it across the horizon - which is exactly
\(DeltaPhi_{Obs}leLambdamin{G_{Obs},C_{Obs}}\). We record this as open.
Until it is discharged, Domination stands as a labelled premise grounded in the
finitude of the observer, not in the definition of emergence - the same status, and
the same debt, as PS-C3\(^prime\) (Ax. axiom:appC_psc3prime). Proof I incurs no
such debt: it reaches the same conclusion from finite resolution \(epsilon_{Obs}\)
directly, which is why the two proofs are worth keeping side by side.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Open derivation route for Emergence Domination]
\label{remark:appC_domination_open_route}
Emergence Domination (Assumption~\ref{assumption:appC_emergence_domination}) is the
single posited plank of Proof~II, and it is where any residual circularity would
hide: were \(\Delta\Phi_{\Obs}\), \(G_{\Obs}\), \(C_{\Obs}\) not independently
measured, the bound would be analytic and the theorem would prove only what it
assumed. The route that would make it synthetic runs through \emph{finite observer
bandwidth}: the bounded-observer kernel
(cf.~\ref{definition:bk4_observer_kernel_convolution_map}) has finite throughput
across the resolution boundary \(\partial\Omega\), so it cannot retain coherent
novelty faster than the binding flux carries it across the horizon --- which is exactly
\(\Delta\Phi_{\Obs}\le\Lambda\min\{G_{\Obs},C_{\Obs}\}\). We record this as open.
Until it is discharged, Domination stands as a labelled premise grounded in the
finitude of the observer, not in the definition of emergence --- the same status, and
the same debt, as PS--C3\(^\prime\) (Ax.~\ref{axiom:appC_psc3prime}). Proof~I incurs no
such debt: it reaches the same conclusion from finite resolution \(\epsilon_{\Obs}\)
directly, which is why the two proofs are worth keeping side by side.
\end{remark}
```

### Two Modalities, One Root (`scholium:appC_two_modalities_one_root`)

Role: `scholium` | Type: `scholium` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:270`

- Proof status: `not_applicable`
- Depends on: `remark:appC_domination_open_route` (Open derivation route for Emergence Domination)
- Cites: `remark:appC_domination_open_route` (Open derivation route for Emergence Domination); `sec:appC_proof_by_elimination` (Proof II --- Effective-Signature (Geometric)); `sec:appC_proof_observational` (Proof I --- Observational Elimination); `theorem:appC_modal_transference` (Modal Transference)
- Cited by: `sec:appC_dual_horizon` (Dual Horizon – A Formal Proof by Elimination)
- Macros used: `\Obs`

**Statement / Body**

The necessity has now been proved twice: observationally
(Ssec:appC_proof_observational, by what a bounded observer can register and
retain) and geometrically (Ssec:appC_proof_by_elimination, by the flux
signature on the manifold). These are not independent confirmations. Both proofs
finally rest on the same fact - the finitude of the observer: Proof I on finite
resolution \(epsilon_{Obs}\), Proof II on finite bandwidth across \(partialOmega\)
(Remark remark:appC_domination_open_route). They are therefore two
presentations of one invariant in two carriers, the observational and the
geometric, and their agreement is precisely a transference test
(Thm. theorem:appC_modal_transference) of the Dual Horizon necessity against its
own mode of presentation. That the invariant survives the carrier swap is the
appendix's strongest internal evidence that the dual signature belongs to the symbolic
structure and not to either proof's framing. The earlier metaphysical trilemma -
``solely generative / solely dissipative / neither'' - is the degenerate, prose-bound
ancestor of Proof I, recovered as the corners \(C_{Obs}=0\), \(G_{Obs}=0\),
\(G_{Obs}=C_{Obs}=0\); its rehabilitation as Proof I now carries Case C, which the
metaphysical reading missed.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Two Modalities, One Root]
\label{scholium:appC_two_modalities_one_root}
The necessity has now been proved twice: observationally
(\S\ref{sec:appC_proof_observational}, by what a bounded observer can register and
retain) and geometrically (\S\ref{sec:appC_proof_by_elimination}, by the flux
signature on the manifold). These are not independent confirmations. Both proofs
finally rest on the same fact --- the finitude of the observer: Proof~I on finite
resolution \(\epsilon_{\Obs}\), Proof~II on finite bandwidth across \(\partial\Omega\)
(Remark~\ref{remark:appC_domination_open_route}). They are therefore two
\emph{presentations} of one invariant in two carriers, the observational and the
geometric, and their agreement is precisely a \emph{transference test}
(Thm.~\ref{theorem:appC_modal_transference}) of the Dual Horizon necessity against its
own mode of presentation. That the invariant survives the carrier swap is the
appendix's strongest internal evidence that the dual signature belongs to the symbolic
structure and not to either proof's framing. The earlier metaphysical trilemma ---
``solely generative / solely dissipative / neither'' --- is the degenerate, prose-bound
ancestor of Proof~I, recovered as the corners \(C_{\Obs}=0\), \(G_{\Obs}=0\),
\(G_{\Obs}=C_{\Obs}=0\); its rehabilitation as Proof~I now carries Case~C, which the
metaphysical reading missed.
\end{scholium}
```

### The Two Horizons as Co-Constitutive (`scholium:appC_two_horizons_co_constitutive`)

Role: `scholium` | Type: `scholium` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:291`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_drift_field` (Drift Field); `definition:bk7_symbolic_reflexive_validation_srv` (Symbolic Reflexive Validation (SRV)); `theorem:appC_dual_horizon_biconditional` (Emergence is sandwiched by the dual signature)
- Cites: `definition:bk1_drift_field` (Drift Field); `definition:bk7_symbolic_reflexive_validation_srv` (Symbolic Reflexive Validation (SRV)); `theorem:appC_dual_horizon_biconditional` (Emergence is sandwiched by the dual signature)
- Cited by: `scholium:appC_symbolic_geometric_equivalence` (Symbolic–Geometric Equivalence of $\varphi$)
- Macros used: `\Obs`

**Statement / Body**

Co-constitution is now a theorem about a bound, not a metaphor. Because the emergence
functional is sandwiched between \(kappa\) and \(Lambda\) times
\(min{G_{Obs},C_{Obs}}\) (Theorem theorem:appC_dual_horizon_biconditional),
the binding term is the smaller of the two fluxes: neither generation nor
stabilization can carry observer-visible becoming alone, and they constrain emergence
symmetrically and inseparably. Drift (cf. definition:bk1_drift_field) supplies
the novelty that Reflection retains; Reflection supplies the contraction that turns
novelty into structure. Their coupling on a shared bounded-observer domain - formally
enacted as Symbolic Reflexive Validation
(cf. definition:bk7_symbolic_reflexive_validation_srv) - is the crucible of
symbolic existence and becoming. The dual horizon is not two objects in the world but the two-signed
signature any world must present to a Bounded Observer in order to be seen to emerge at
all.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[The Two Horizons as Co-Constitutive]
\label{scholium:appC_two_horizons_co_constitutive}
Co-constitution is now a theorem about a bound, not a metaphor. Because the emergence
functional is sandwiched between \(\kappa\) and \(\Lambda\) times
\(\min\{G_{\Obs},C_{\Obs}\}\) (Theorem~\ref{theorem:appC_dual_horizon_biconditional}),
the binding term is the \emph{smaller} of the two fluxes: neither generation nor
stabilization can carry observer-visible becoming alone, and they constrain emergence
symmetrically and inseparably. Drift (cf.~\ref{definition:bk1_drift_field}) supplies
the novelty that Reflection retains; Reflection supplies the contraction that turns
novelty into structure. Their coupling on a shared bounded-observer domain --- formally
enacted as Symbolic Reflexive Validation
(cf.~\ref{definition:bk7_symbolic_reflexive_validation_srv}) --- is the crucible of
symbolic existence and becoming. The dual horizon is not two objects in the world but the two-signed
signature any world must present to a Bounded Observer in order to be seen to emerge at
all.
\end{scholium}
```

### Born Rule – A Formal Derivation (`sec:appC_born_rule`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:308`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer)
- Cited by: `subsec:appC_methodological_logical_framework` (C.0.1 Method: two eliminations, one root)
- Macros used: none

**Statement / Body**

(no body text extracted)

### Derivation Structure (`remark:appC_born_rule_dependency`)

Role: `remark` | Type: `remark` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:312`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `axiom:appC_psc3prime` (PS--C3$'$ (Non-contextual token budget)); `definition:bk1_bounded_observer` (Bounded Observer); `subsec:appC_born_additivity_derivation` (Interpretive-Budget Additivity from Bounded Discernibility); `subsec:appC_born_axioms` (Coherence Axioms (PS–C)); `theorem:appC_orthogonal_additivity` (Orthogonal additivity from bounded discernibility)
- Cited by: none
- Macros used: none

**Statement / Body**

This derivation proceeds from the coherence constraints PS-C1-C5
(Ssubsec:appC_born_axioms) to Gleason's hypotheses, and thence to
the Born Rule. The structural constraints PS-C1, PS-C2, PS-C4, PS-C5 are
consequences of bounded observation (Def. definition:bk1_bounded_observer),
not ad hoc quantum postulates: each encodes a constraint that any
finite-resolution observer necessarily satisfies. The additivity once carried as
PS-C3 splits in two: its within-frame content is proved in
Ssubsec:appC_born_additivity_derivation
(Thm. theorem:appC_orthogonal_additivity) from observer-token disjointness,
while its cross-frame content-non-contextuality-is isolated and posited as
PS-C3$'$ (Ax. axiom:appC_psc3prime). The derivation thus reduces Gleason's
additivity hypothesis to finite-budget bookkeeping plus a single, explicitly
labelled non-contextuality axiom, and is grounded in the PS foundational framework
rather than in the Hilbert space structure it explains; the Born conclusion is
conditional on PS-C3$'$.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Derivation Structure]
\label{remark:appC_born_rule_dependency}
This derivation proceeds from the coherence constraints PS-C1--C5
(\S\ref{subsec:appC_born_axioms}) to Gleason's hypotheses, and thence to
the Born Rule. The structural constraints PS-C1, PS-C2, PS-C4, PS-C5 are
consequences of bounded observation (Def.~\ref{definition:bk1_bounded_observer}),
not ad hoc quantum postulates: each encodes a constraint that any
finite-resolution observer necessarily satisfies. The additivity once carried as
PS-C3 splits in two: its \emph{within-frame} content is \emph{proved} in
\S\ref{subsec:appC_born_additivity_derivation}
(Thm.~\ref{theorem:appC_orthogonal_additivity}) from observer-token disjointness,
while its cross-frame content---non-contextuality---is isolated and posited as
PS-C3$'$ (Ax.~\ref{axiom:appC_psc3prime}). The derivation thus reduces Gleason's
additivity hypothesis to finite-budget bookkeeping plus a single, explicitly
labelled non-contextuality axiom, and is grounded in the PS foundational framework
rather than in the Hilbert space structure it explains; the Born conclusion is
conditional on PS-C3$'$.
\end{remark}
```

### Preamble (`sec:appC_born_preamble`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:331`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk6_symbolic_curvature_tensor` (Symbolic Curvature Tensor)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk6_symbolic_curvature_tensor` (Symbolic Curvature Tensor)
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Observer Data Structures in the Quantum Regime (`subsec:appC_born_observer_structures`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:340`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer)
- Cited by: `scholium:bk4_emergence_of_classical_calculus` (Emergence of Classical Calculus)
- Macros used: none

**Statement / Body**

(no body text extracted)

### Frame space of $\Obs$ (`definition:appC_frame_space`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:350`

- Proof status: `definitional`
- Depends on: `definition:bk4_bounded_observer` (Bounded Observer)
- Cites: `definition:bk4_bounded_observer` (Bounded Observer)
- Cited by: `definition:appC_observer_token_space` (Observer token space for a projective frame)
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

For a bounded observer $Obs$ (cf. definition:bk4_bounded_observer), define
\[
F_{Obs} subseteq Proj(Horizon)
\]
as the frame space: the maximal set of mutually orthogonal projections
whose outcomes are classically discernible given the observer’s resolution threshold
$epsilon_{Obs}$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Frame space of $\Obs$]
\label{definition:appC_frame_space}
For a bounded observer $\Obs$ (cf.~\ref{definition:bk4_bounded_observer}), define
\[
F_{Obs} \subseteq Proj(\Horizon)
\]
as the \emph{frame space}: the maximal set of mutually orthogonal projections
whose outcomes are classically discernible given the observer’s resolution threshold
$\epsilon_{\Obs}$.
\end{definition}
```

### Coherence functional (`definition:appC_coherence_functional`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:361`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer)
- Cited by: `axiom:appC_psc1` (PS--C1 (Boundedness)); `axiom:appC_psc2` (PS--C2 (Unitary covariance)); `axiom:appC_psc3` (PS--C3 (Conservation of interpretive budget)); `axiom:appC_psc4` (PS--C4 (Ray invariance)); `axiom:appC_psc5` (PS--C5 (Resolution-limited distinguishability)); `definition:appC_observer_coherence_budget` (Observer coherence budget); `subsec:appC_born_axioms` (Coherence Axioms (PS–C))
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

For a Bounded Observer $Obs$ (cf. definition:bk1_bounded_observer), the coherence assignment functional is
\[
C_{Obs}: Proj(Horizon) times Horizon to [0,1],
(Pi, psi) mapsto C_{Obs}(tildepsi_{Obs}, Pi),
\]
where $tildepsi_{Obs}$ is the observer’s internal (fuzzy) representation
of the external state $psi in Horizon$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Coherence functional]
\label{definition:appC_coherence_functional}
For a Bounded Observer $\Obs$ (cf.~\ref{definition:bk1_bounded_observer}), the \emph{coherence assignment functional} is
\[
\mathcal{C}_{Obs}: Proj(\Horizon) \times \Horizon \to [0,1], \quad
(\Pi, \psi) \mapsto \mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \Pi),
\]
where $\tilde\psi_{\Obs}$ is the observer’s internal (fuzzy) representation
of the external state $\psi \in \Horizon$.
\end{definition}
```

### Formal correspondence at the observer boundary (`remark:appC_observer_lowering_boundary`)

Role: `remark` | Type: `remark` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:372`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The machine-checked companion supplies two complementary Gleason-facing
half-bridges, separated by an observer boundary. In the source-to-readout direction,
a normalized pure-state vector determines its Hermitian rank-one density and lowers
through a fixed observer kernel to a Born-compatible resolved readout. In the
readout-to-representation direction, explicitly certified conjugate-linear, linear,
and Hermitian cross laws construct a sesquilinear representation of the available
values. The second construction represents the readout; it is not an inverse that
recovers the originating vector or process state.

The seam is genuinely lossy. Global phase is forgotten, so distinct normalized
vectors can yield the same density and the same fixed-kernel observer record.
Explicit counterexamples further show that arbitrary coherent frame readouts and
arbitrary normalized resolution records need not determine an upstream Hermitian
state. Finite partial trace provides another exact lowering: it preserves trace and
all represented local-observer expectations while discarding access to the full joint
operator.

Temporal direction is already present in the companion's Cost of Cacophony backbone.
Simultaneous finite-support compression obeys the certified norm-fracture bounds, and
the diagonal witness has a strictly positive representability gap. A staged path is
instead accounted for as an ordered sum of per-step displacements; its transport cost
is paid by free-energy decrease in the certified JKO step. Under the stated
summability, completeness, or Lyapunov-descent premises, those directed stages
converge. Thus time is not merely a metaphor here: it is the parameter by which one
simultaneous obstruction is re-expressed as sequential transport with an explicit cost
and convergence contract.

What remains functionally interpretive is the physical specialization: mapping quantum decoherence
and noise as the continued unfolding of this general directed cost-and-loss geometry.
The exact temporal transport results, exact partial-trace reduction, and exact
phase-collision boundary ground that operational, testable reading without collapsing the mapped domains into one another.
This status distinction neither rejects the human mathematical argument under
PS-C1-PS-C6 nor reduces its observer interpretation to the finite Lean model.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Formal correspondence at the observer boundary]
\label{remark:appC_observer_lowering_boundary}
The machine-checked companion supplies two complementary Gleason-facing
half-bridges, separated by an observer boundary.  In the source-to-readout direction,
a normalized pure-state vector determines its Hermitian rank-one density and lowers
through a fixed observer kernel to a Born-compatible resolved readout.  In the
readout-to-representation direction, explicitly certified conjugate-linear, linear,
and Hermitian cross laws construct a sesquilinear representation of the available
values.  The second construction represents the readout; it is not an inverse that
recovers the originating vector or process state.

The seam is genuinely lossy.  Global phase is forgotten, so distinct normalized
vectors can yield the same density and the same fixed-kernel observer record.
Explicit counterexamples further show that arbitrary coherent frame readouts and
arbitrary normalized resolution records need not determine an upstream Hermitian
state.  Finite partial trace provides another exact lowering: it preserves trace and
all represented local-observer expectations while discarding access to the full joint
operator.

Temporal direction is already present in the companion's Cost of Cacophony backbone.
Simultaneous finite-support compression obeys the certified norm-fracture bounds, and
the diagonal witness has a strictly positive representability gap.  A staged path is
instead accounted for as an ordered sum of per-step displacements; its transport cost
is paid by free-energy decrease in the certified JKO step.  Under the stated
summability, completeness, or Lyapunov-descent premises, those directed stages
converge.  Thus time is not merely a metaphor here: it is the parameter by which one
simultaneous obstruction is re-expressed as sequential transport with an explicit cost
and convergence contract.

What remains functionally interpretive is the physical specialization: mapping quantum decoherence
and noise as the continued unfolding of this general directed cost-and-loss geometry.
The exact temporal transport results, exact partial-trace reduction, and exact
phase-collision boundary ground that operational, testable reading without collapsing the mapped domains into one another.
This status distinction neither rejects the human mathematical argument under
PS--C1--PS--C6 nor reduces its observer interpretation to the finite Lean model.
\end{remark}
```

### Interpretive-Budget Additivity from Bounded Discernibility (`subsec:appC_born_additivity_derivation`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:409`

- Proof status: `not_applicable`
- Depends on: none
- Cites: `axiom:appC_psc3prime` (PS--C3$'$ (Non-contextual token budget))
- Cited by: `remark:appC_born_rule_dependency` (Derivation Structure); `subsec:appC_born_axioms` (Coherence Axioms (PS–C))
- Macros used: none

**Statement / Body**

(no body text extracted)

### Bounded discernibility (`assumption:appC_bounded_discernibility`)

Role: `assumption` | Type: `assumption` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:424`

- Proof status: `definitional`
- Depends on: none
- Cites: `axiom:appC_psc5` (PS--C5 (Resolution-limited distinguishability))
- Cited by: `proof:appC_orthogonal_token_separation`
- Macros used: none

**Statement / Body**

A single resolved observer token is assigned to at most one of any two mutually
orthogonal (hence mutually exclusive) outcome subspaces: orthogonal resolved outcomes
receive distinct tokens. This is the content later codified, at the resolution scale,
as PS-C5 (Ax. axiom:appC_psc5).

**Verbatim LaTeX Body**

```latex
\begin{assumption}[Bounded discernibility]
\label{assumption:appC_bounded_discernibility}
A single resolved observer token is assigned to at most one of any two mutually
orthogonal (hence mutually exclusive) outcome subspaces: orthogonal resolved outcomes
receive distinct tokens. This is the content later codified, at the resolution scale,
as PS--C5 (Ax.~\ref{axiom:appC_psc5}).
\end{assumption}
```

### Observer token space for a projective frame (`definition:appC_observer_token_space`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:432`

- Proof status: `definitional`
- Depends on: `definition:appC_frame_space` (Frame space of $\Obs$)
- Cites: `definition:appC_frame_space` (Frame space of $\Obs$); `subsec:appC_born_interpretation_ps` (Interpretation Within Principia Symbolica)
- Cited by: none
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

Let $dimHorizon < infty$ and let
\[
mathfrak{F} = {Pi_i}_{i=1}^{n} subseteq Proj(Horizon),
 Pi_i Pi_j = 0\ (i neq j), sum_i Pi_i = mathbbm{1},
\]
be a complete orthogonal frame discernible to the Bounded Observer $Obs$
(cf. definition:appC_frame_space). Let $T_Obs(mathfrak{F})$ denote
the finite set of observer-resolvable outcome tokens produced when $Obs$
applies its collapse/refinement map (the observer-context realization of $R_lambda$,
cf. subsec:appC_born_interpretation_ps) to $mathfrak{F}$. For any projector
$Pi$ obtained by coarse-graining elements of $mathfrak{F}$, set
\[
T_Obs(Pi) := { t in T_Obs(mathfrak{F}) :
text{the outcome resolved by } t text{ lies in } im(Pi) }.
\]

**Verbatim LaTeX Body**

```latex
\begin{definition}[Observer token space for a projective frame]
\label{definition:appC_observer_token_space}
Let $\dim\Horizon < \infty$ and let
\[
\mathfrak{F} = \{\Pi_i\}_{i=1}^{n} \subseteq Proj(\Horizon),
\qquad \Pi_i \Pi_j = 0\ (i \neq j),\qquad \sum_i \Pi_i = \mathbbm{1},
\]
be a complete orthogonal frame discernible to the Bounded Observer $\Obs$
(cf.~\ref{definition:appC_frame_space}). Let $\mathcal{T}_\Obs(\mathfrak{F})$ denote
the finite set of \emph{observer-resolvable outcome tokens} produced when $\Obs$
applies its collapse/refinement map (the observer-context realization of $R_\lambda$,
cf.~\ref{subsec:appC_born_interpretation_ps}) to $\mathfrak{F}$. For any projector
$\Pi$ obtained by coarse-graining elements of $\mathfrak{F}$, set
\[
T_\Obs(\Pi) := \{\, t \in \mathcal{T}_\Obs(\mathfrak{F}) :
\text{the outcome resolved by } t \text{ lies in } \operatorname{im}(\Pi) \,\}.
\]
\end{definition}
```

### Observer coherence budget (`definition:appC_observer_coherence_budget`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:451`

- Proof status: `definitional`
- Depends on: `definition:appC_coherence_functional` (Coherence functional)
- Cites: `definition:appC_coherence_functional` (Coherence functional)
- Cited by: `assumption:appC_emergence_domination` (Emergence Domination); `proof:appC_orthogonal_additivity`; `proof:appC_psc3`; `remark:appC_born_honest_reduction` (What is proved, and what is posited)
- Macros used: `\Obs`

**Statement / Body**

A Bounded Observer $Obs$ in state $tildepsi_{Obs}$ carries a finite
coherence budget
\[
mu_{Obs,tildepsi} : Pbig(T_Obs(mathfrak{F})big) to [0,1],

mu_{Obs,tildepsi}(varnothing) = 0,
mu_{Obs,tildepsi}big(T_Obs(mathfrak{F})big) = 1,
\]
which is finitely additive on disjoint token sets:
$A cap B = varnothing Rightarrow
mu_{Obs,tildepsi}(A sqcup B) = mu_{Obs,tildepsi}(A) + mu_{Obs,tildepsi}(B)$.
This is not a quantum-probability axiom but finite symbolic-budget conservation:
disjoint resolved tokens cannot consume the same bounded interpretive resource twice.
The coherence functional (cf. definition:appC_coherence_functional) admits the
token-budget representation
\[
C_{Obs}(tildepsi_{Obs}, Pi) = mu_{Obs,tildepsi}big(T_Obs(Pi)big).
\]

**Verbatim LaTeX Body**

```latex
\begin{definition}[Observer coherence budget]
\label{definition:appC_observer_coherence_budget}
A Bounded Observer $\Obs$ in state $\tilde\psi_{\Obs}$ carries a finite
\emph{coherence budget}
\[
\mu_{\Obs,\tilde\psi} : \mathcal{P}\big(\mathcal{T}_\Obs(\mathfrak{F})\big) \to [0,1],
\qquad
\mu_{\Obs,\tilde\psi}(\varnothing) = 0,\quad
\mu_{\Obs,\tilde\psi}\big(\mathcal{T}_\Obs(\mathfrak{F})\big) = 1,
\]
which is finitely additive on disjoint token sets:
$A \cap B = \varnothing \Rightarrow
\mu_{\Obs,\tilde\psi}(A \sqcup B) = \mu_{\Obs,\tilde\psi}(A) + \mu_{\Obs,\tilde\psi}(B)$.
This is not a quantum-probability axiom but finite symbolic-budget conservation:
disjoint resolved tokens cannot consume the same bounded interpretive resource twice.
The coherence functional (cf.~\ref{definition:appC_coherence_functional}) admits the
token-budget representation
\[
\mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \Pi) = \mu_{\Obs,\tilde\psi}\big(T_\Obs(\Pi)\big).
\]
\end{definition}
```

### Orthogonal token separation (`lemma:appC_orthogonal_token_separation`)

Role: `lemma` | Type: `lemma` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:473`

- Proof status: `proven`
- Depends on: `assumption:appC_bounded_discernibility` (Bounded discernibility)
- Cites: none
- Cited by: `proof:appC_coarse_graining_tokens`; `remark:appC_born_honest_reduction` (What is proved, and what is posited)
- Macros used: `\Obs`

**Statement / Body**

If $Pi Xi = 0$ then $T_Obs(Pi) cap T_Obs(Xi) = varnothing$.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Orthogonal token separation]
\label{lemma:appC_orthogonal_token_separation}
If $\Pi\,\Xi = 0$ then $T_\Obs(\Pi) \cap T_\Obs(\Xi) = \varnothing$.
\end{lemma}
```

### proof:appC_orthogonal_token_separation (`proof:appC_orthogonal_token_separation`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:478`

- Proof status: `not_applicable`
- Depends on: `assumption:appC_bounded_discernibility` (Bounded discernibility)
- Cites: `assumption:appC_bounded_discernibility` (Bounded discernibility)
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

Orthogonality gives $im(Pi) cap im(Xi) = {0}$.
Were a token $t$ to lie in both $T_Obs(Pi)$ and $T_Obs(Xi)$, the single outcome
resolved by $t$ would simultaneously be a $Pi$-outcome and an $Xi$-outcome,
i.e.\ the observer would assign one resolved token to two mutually orthogonal
(hence mutually exclusive) subspaces. This violates bounded discernibility
(Assumption assumption:appC_bounded_discernibility). Hence the token sets are disjoint.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_orthogonal_token_separation}
Orthogonality gives $\operatorname{im}(\Pi) \cap \operatorname{im}(\Xi) = \{0\}$.
Were a token $t$ to lie in both $T_\Obs(\Pi)$ and $T_\Obs(\Xi)$, the single outcome
resolved by $t$ would simultaneously be a $\Pi$-outcome and an $\Xi$-outcome,
i.e.\ the observer would assign one resolved token to two mutually orthogonal
(hence mutually exclusive) subspaces. This violates bounded discernibility
(Assumption~\ref{assumption:appC_bounded_discernibility}). Hence the token sets are disjoint.
\end{proof}
```

### Coarse-graining of orthogonal tokens (`lemma:appC_coarse_graining_tokens`)

Role: `lemma` | Type: `lemma` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:488`

- Proof status: `proven`
- Depends on: `lemma:appC_orthogonal_token_separation` (Orthogonal token separation)
- Cites: none
- Cited by: `proof:appC_orthogonal_additivity`; `remark:appC_born_honest_reduction` (What is proved, and what is posited)
- Macros used: `\Obs`

**Statement / Body**

If $Pi_i Pi_j = 0$ for $i neq j$, then
$T_Obs\!big(sum_i Pi_ibig) = bigsqcup_i T_Obs(Pi_i)$.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Coarse-graining of orthogonal tokens]
\label{lemma:appC_coarse_graining_tokens}
If $\Pi_i \Pi_j = 0$ for $i \neq j$, then
$T_\Obs\!\big(\sum_i \Pi_i\big) = \bigsqcup_i T_\Obs(\Pi_i)$.
\end{lemma}
```

### proof:appC_coarse_graining_tokens (`proof:appC_coarse_graining_tokens`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:494`

- Proof status: `not_applicable`
- Depends on: `lemma:appC_orthogonal_token_separation` (Orthogonal token separation)
- Cites: `lemma:appC_orthogonal_token_separation` (Orthogonal token separation)
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

The projector $sum_i Pi_i$ encodes the coarse-grained question
``did the resolved outcome fall in $bigcup_i im(Pi_i)$?'' A token
answers affirmatively exactly when it lies in some $T_Obs(Pi_i)$, so
$T_Obs(sum_i Pi_i) = bigcup_i T_Obs(Pi_i)$. By
Lemma lemma:appC_orthogonal_token_separation the $T_Obs(Pi_i)$ are pairwise
disjoint, so the union is disjoint.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_coarse_graining_tokens}
The projector $\sum_i \Pi_i$ encodes the coarse-grained question
``did the resolved outcome fall in $\bigcup_i \operatorname{im}(\Pi_i)$?'' A token
answers affirmatively exactly when it lies in some $T_\Obs(\Pi_i)$, so
$T_\Obs(\sum_i \Pi_i) = \bigcup_i T_\Obs(\Pi_i)$. By
Lemma~\ref{lemma:appC_orthogonal_token_separation} the $T_\Obs(\Pi_i)$ are pairwise
disjoint, so the union is disjoint.
\end{proof}
```

### Orthogonal additivity from bounded discernibility (`theorem:appC_orthogonal_additivity`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:504`

- Proof status: `proven`
- Depends on: `definition:appC_observer_coherence_budget` (Observer coherence budget); `lemma:appC_coarse_graining_tokens` (Coarse-graining of orthogonal tokens)
- Cites: none
- Cited by: `lemma:appC_sigma_additivity` (Finite orthogonal additivity gives a Gleason frame function); `proof:appC_psc3`; `proof:appC_sigma_additivity`; `remark:appC_born_honest_reduction` (What is proved, and what is posited); `remark:appC_born_rule_dependency` (Derivation Structure)
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

Let $Obs$ be a Bounded Observer with finite coherence budget
$mu_{Obs,tildepsi}$. For any finite mutually orthogonal family
${Pi_i}_{i=1}^n subseteq Proj(Horizon)$,
\[
C_{Obs}\!Big(tildepsi_{Obs}, sum_i Pi_iBig)
= sum_i C_{Obs}(tildepsi_{Obs}, Pi_i).
\]

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Orthogonal additivity from bounded discernibility]
\label{theorem:appC_orthogonal_additivity}
Let $\Obs$ be a Bounded Observer with finite coherence budget
$\mu_{\Obs,\tilde\psi}$. For any finite mutually orthogonal family
$\{\Pi_i\}_{i=1}^n \subseteq Proj(\Horizon)$,
\[
\mathcal{C}_{\Obs}\!\Big(\tilde\psi_{\Obs}, \sum_i \Pi_i\Big)
= \sum_i \mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \Pi_i).
\]
\end{theorem}
```

### proof:appC_orthogonal_additivity (`proof:appC_orthogonal_additivity`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:515`

- Proof status: `not_applicable`
- Depends on: `definition:appC_observer_coherence_budget` (Observer coherence budget); `lemma:appC_coarse_graining_tokens` (Coarse-graining of orthogonal tokens)
- Cites: `definition:appC_observer_coherence_budget` (Observer coherence budget); `lemma:appC_coarse_graining_tokens` (Coarse-graining of orthogonal tokens)
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

By the token-budget representation (Def. definition:appC_observer_coherence_budget),
$C_{Obs}(tildepsi_{Obs}, sum_i Pi_i)
= mu_{Obs,tildepsi}big(T_Obs(sum_i Pi_i)big)$. By
Lemma lemma:appC_coarse_graining_tokens,
$T_Obs(sum_i Pi_i) = bigsqcup_i T_Obs(Pi_i)$. Finite additivity of the budget
over disjoint token sets gives
$mu_{Obs,tildepsi}(bigsqcup_i T_Obs(Pi_i))
= sum_i mu_{Obs,tildepsi}(T_Obs(Pi_i))$, and applying the representation once
more yields $sum_i C_{Obs}(tildepsi_{Obs}, Pi_i)$.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_orthogonal_additivity}
By the token-budget representation (Def.~\ref{definition:appC_observer_coherence_budget}),
$\mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \sum_i \Pi_i)
= \mu_{\Obs,\tilde\psi}\big(T_\Obs(\sum_i \Pi_i)\big)$. By
Lemma~\ref{lemma:appC_coarse_graining_tokens},
$T_\Obs(\sum_i \Pi_i) = \bigsqcup_i T_\Obs(\Pi_i)$. Finite additivity of the budget
over disjoint token sets gives
$\mu_{\Obs,\tilde\psi}(\bigsqcup_i T_\Obs(\Pi_i))
= \sum_i \mu_{\Obs,\tilde\psi}(T_\Obs(\Pi_i))$, and applying the representation once
more yields $\sum_i \mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \Pi_i)$.
\end{proof}
```

### PS--C3$'$ (Non-contextual token budget) (`axiom:appC_psc3prime`)

Role: `axiom` | Type: `axiom` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:528`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `definition:bk7_contextuality_defect` (Contextuality defect); `remark:appC_born_rule_dependency` (Derivation Structure); `remark:appC_domination_open_route` (Open derivation route for Emergence Domination); `remark:bk7_pisu_status` (Status of the trade-off and its corollaries); `subsec:appC_born_additivity_derivation` (Interpretive-Budget Additivity from Bounded Discernibility); `subsec:appC_born_axioms` (Coherence Axioms (PS–C)); `subsec:appC_conclusion_of_proof_by_elimination` (Sufficiency and the Conditional Biconditional); `subsec:bk7_pisu_implications` (Implications)
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

Let $mathfrak{F}, mathfrak{F}'$ be complete orthogonal frames discernible to $Obs$,
and let $Pi in Proj(Horizon)$ be obtained by coarse-graining elements of
$mathfrak{F}$ and also of $mathfrak{F}'$, with token realizations
$T^{mathfrak{F}}_Obs(Pi)$ and $T^{mathfrak{F}'}_Obs(Pi)$. Then the budget
assigns them equal measure,
\[
mu_{Obs,tildepsi}big(T^{mathfrak{F}}_Obs(Pi)big)
= mu_{Obs,tildepsi}big(T^{mathfrak{F}'}_Obs(Pi)big);
\]
equivalently, $C_{Obs}(tildepsi_Obs,Pi)$ is well defined independently of
the complete frame within which $Obs$ poses the question $Pi$.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[PS--C3$'$ (Non-contextual token budget)]
\label{axiom:appC_psc3prime}
Let $\mathfrak{F}, \mathfrak{F}'$ be complete orthogonal frames discernible to $\Obs$,
and let $\Pi \in Proj(\Horizon)$ be obtained by coarse-graining elements of
$\mathfrak{F}$ and also of $\mathfrak{F}'$, with token realizations
$T^{\mathfrak{F}}_\Obs(\Pi)$ and $T^{\mathfrak{F}'}_\Obs(\Pi)$. Then the budget
assigns them equal measure,
\[
\mu_{\Obs,\tilde\psi}\big(T^{\mathfrak{F}}_\Obs(\Pi)\big)
= \mu_{\Obs,\tilde\psi}\big(T^{\mathfrak{F}'}_\Obs(\Pi)\big);
\]
equivalently, $\mathcal{C}_{\Obs}(\tilde\psi_\Obs,\Pi)$ is well defined independently of
the complete frame within which $\Obs$ poses the question $\Pi$.
\end{axiom}
```

### What is proved, and what is posited (`remark:appC_born_honest_reduction`)

Role: `remark` | Type: `remark` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:543`

- Proof status: `not_applicable`
- Depends on: `definition:appC_observer_coherence_budget` (Observer coherence budget); `lemma:appC_coarse_graining_tokens` (Coarse-graining of orthogonal tokens); `lemma:appC_orthogonal_token_separation` (Orthogonal token separation); `theorem:appC_orthogonal_additivity` (Orthogonal additivity from bounded discernibility)
- Cites: `definition:appC_observer_coherence_budget` (Observer coherence budget); `lemma:appC_coarse_graining_tokens` (Coarse-graining of orthogonal tokens); `lemma:appC_orthogonal_token_separation` (Orthogonal token separation); `theorem:appC_orthogonal_additivity` (Orthogonal additivity from bounded discernibility)
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

Lemma lemma:appC_orthogonal_token_separation,
Lemma lemma:appC_coarse_graining_tokens, and
Theorem theorem:appC_orthogonal_additivity establish additivity of the budget
within any single frame; this is bookkeeping, derived from token disjointness.
The frame-independence of the representation
$C_{Obs}(tildepsi_Obs,Pi) = mu_{Obs,tildepsi}(T_Obs(Pi))$ across
frames - PS-C3$'$ - is the PS form of non-contextuality and is posited, not derived.
The Born derivation therefore reduces Gleason's additivity hypothesis to two
ingredients: finite-budget conservation on disjoint tokens
(Def. definition:appC_observer_coherence_budget, a bookkeeping principle) and
non-contextuality of the budget (PS-C3$'$, the physical content).

**Verbatim LaTeX Body**

```latex
\begin{remark}[What is proved, and what is posited]
\label{remark:appC_born_honest_reduction}
Lemma~\ref{lemma:appC_orthogonal_token_separation},
Lemma~\ref{lemma:appC_coarse_graining_tokens}, and
Theorem~\ref{theorem:appC_orthogonal_additivity} establish additivity of the budget
\emph{within any single frame}; this is bookkeeping, derived from token disjointness.
The frame-independence of the representation
$\mathcal{C}_{\Obs}(\tilde\psi_\Obs,\Pi) = \mu_{\Obs,\tilde\psi}(T_\Obs(\Pi))$ across
frames -- PS--C3$'$ -- is the PS form of non-contextuality and is posited, not derived.
The Born derivation therefore reduces Gleason's additivity hypothesis to two
ingredients: finite-budget conservation on disjoint tokens
(Def.~\ref{definition:appC_observer_coherence_budget}, a bookkeeping principle) and
non-contextuality of the budget (PS--C3$'$, the physical content).
\end{remark}
```

### Open derivation route for PS--C3$'$ (`remark:appC_psc3prime_open_route`)

Role: `remark` | Type: `remark` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:558`

- Proof status: `not_applicable`
- Depends on: none
- Cites: `axiom:appC_psc5` (PS--C5 (Resolution-limited distinguishability)); `theorem:appC_born_rule` (Observer-relative Born Rule)
- Cited by: none
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

A future derivation could proceed through resolution-limited frame distinguishability
(PS-C5, Ax. axiom:appC_psc5): if two discernible frames agree on $Pi$ up to the
observer threshold $epsilon_Obs$, the budgets they assign $Pi$ must agree up to a
modulus controlled by $epsilon_Obs$, and a continuity-plus-density argument over the
frame manifold - connected for $dimHorizon ge 3$ - might then force exact equality
in the $epsilon_Obs to 0$ refinement limit. We record this as open. That
$dimHorizon ge 3$ enters in the same place it enters Gleason's theorem
(Thm. theorem:appC_born_rule) is structural evidence the route is the right one;
until it is completed, PS-C3$'$ stands as an axiom and the Born conclusion is
conditional on it.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Open derivation route for PS--C3$'$]
\label{remark:appC_psc3prime_open_route}
A future derivation could proceed through resolution-limited frame distinguishability
(PS--C5, Ax.~\ref{axiom:appC_psc5}): if two discernible frames agree on $\Pi$ up to the
observer threshold $\epsilon_\Obs$, the budgets they assign $\Pi$ must agree up to a
modulus controlled by $\epsilon_\Obs$, and a continuity-plus-density argument over the
frame manifold -- connected for $\dim\Horizon \ge 3$ -- might then force exact equality
in the $\epsilon_\Obs \to 0$ refinement limit. We record this as open. That
$\dim\Horizon \ge 3$ enters in the same place it enters Gleason's theorem
(Thm.~\ref{theorem:appC_born_rule}) is structural evidence the route is the right one;
until it is completed, PS--C3$'$ stands as an axiom and the Born conclusion is
conditional on it.
\end{remark}
```

### Coherence Axioms (PS–C) (`subsec:appC_born_axioms`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:572`

- Proof status: `not_applicable`
- Depends on: `axiom:appC_psc3prime` (PS--C3$'$ (Non-contextual token budget)); `definition:appC_coherence_functional` (Coherence functional)
- Cites: `axiom:appC_psc3prime` (PS--C3$'$ (Non-contextual token budget)); `definition:appC_coherence_functional` (Coherence functional); `subsec:appC_born_additivity_derivation` (Interpretive-Budget Additivity from Bounded Discernibility)
- Cited by: `remark:appC_born_rule_dependency` (Derivation Structure)
- Macros used: none

**Statement / Body**

(no body text extracted)

### PS--C1 (Boundedness) (`axiom:appC_psc1`)

Role: `axiom` | Type: `axiom` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:580`

- Proof status: `definitional`
- Depends on: `definition:appC_coherence_functional` (Coherence functional)
- Cites: `definition:appC_coherence_functional` (Coherence functional)
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

$0 leq C_{Obs}(tildepsi_{Obs}, Pi) leq 1$ (cf. definition:appC_coherence_functional)

**Verbatim LaTeX Body**

```latex
\begin{axiom}[PS--C1 (Boundedness)]
\label{axiom:appC_psc1}
$0 \leq \mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \Pi) \leq 1$ \quad (cf.~\ref{definition:appC_coherence_functional})
\end{axiom}
```

### PS--C2 (Unitary covariance) (`axiom:appC_psc2`)

Role: `axiom` | Type: `axiom` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:585`

- Proof status: `definitional`
- Depends on: `definition:appC_coherence_functional` (Coherence functional)
- Cites: `definition:appC_coherence_functional` (Coherence functional)
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

$C_{Obs}(U tildepsi_{Obs}, U Pi U^dagger)
= C_{Obs}(tildepsi_{Obs}, Pi)$ (cf. definition:appC_coherence_functional)

**Verbatim LaTeX Body**

```latex
\begin{axiom}[PS--C2 (Unitary covariance)]
\label{axiom:appC_psc2}
$\mathcal{C}_{\Obs}(U \tilde\psi_{\Obs}, U \Pi U^\dagger)
= \mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \Pi)$ \quad (cf.~\ref{definition:appC_coherence_functional})
\end{axiom}
```

### PS--C3 (Conservation of interpretive budget) (`axiom:appC_psc3`)

Role: `corollary` | Type: `corollary` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:591`

- Proof status: `proven`
- Depends on: `definition:appC_coherence_functional` (Coherence functional); `definition:appC_observer_coherence_budget` (Observer coherence budget); `theorem:appC_orthogonal_additivity` (Orthogonal additivity from bounded discernibility)
- Cites: `definition:appC_coherence_functional` (Coherence functional)
- Cited by: `lemma:appC_sigma_additivity` (Finite orthogonal additivity gives a Gleason frame function); `proof:appC_sigma_additivity`
- Macros used: `\Obs`

**Statement / Body**

For any complete orthogonal decomposition ${Pi_i}$ of $mathbbm{1}$ (cf. definition:appC_coherence_functional):
\[
sum_i C_{Obs}(tildepsi_{Obs}, Pi_i) = 1.
\]

**Verbatim LaTeX Body**

```latex
\begin{corollary}[PS--C3 (Conservation of interpretive budget)]
\label{axiom:appC_psc3}
For any complete orthogonal decomposition $\{\Pi_i\}$ of $\mathbbm{1}$ (cf.~\ref{definition:appC_coherence_functional}):
\[
\sum_i \mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \Pi_i) = 1.
\]
\end{corollary}
```

### proof:appC_psc3 (`proof:appC_psc3`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:599`

- Proof status: `not_applicable`
- Depends on: `definition:appC_observer_coherence_budget` (Observer coherence budget); `theorem:appC_orthogonal_additivity` (Orthogonal additivity from bounded discernibility)
- Cites: `definition:appC_observer_coherence_budget` (Observer coherence budget); `theorem:appC_orthogonal_additivity` (Orthogonal additivity from bounded discernibility)
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

Apply Theorem theorem:appC_orthogonal_additivity to the complete frame
$sum_i Pi_i = mathbbm{1}$:
$sum_i C_{Obs}(tildepsi_{Obs}, Pi_i)
= C_{Obs}(tildepsi_{Obs}, mathbbm{1})
= mu_{Obs,tildepsi}big(T_Obs(mathbbm{1})big)
= mu_{Obs,tildepsi}big(T_Obs(mathfrak{F})big) = 1$,
using the token-budget representation
(Def. definition:appC_observer_coherence_budget) and the normalization
$mu_{Obs,tildepsi}(T_Obs(mathfrak{F})) = 1$.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_psc3}
Apply Theorem~\ref{theorem:appC_orthogonal_additivity} to the complete frame
$\sum_i \Pi_i = \mathbbm{1}$:
$\sum_i \mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \Pi_i)
= \mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \mathbbm{1})
= \mu_{\Obs,\tilde\psi}\big(T_\Obs(\mathbbm{1})\big)
= \mu_{\Obs,\tilde\psi}\big(\mathcal{T}_\Obs(\mathfrak{F})\big) = 1$,
using the token-budget representation
(Def.~\ref{definition:appC_observer_coherence_budget}) and the normalization
$\mu_{\Obs,\tilde\psi}(\mathcal{T}_\Obs(\mathfrak{F})) = 1$.
\end{proof}
```

### PS--C4 (Ray invariance) (`axiom:appC_psc4`)

Role: `axiom` | Type: `axiom` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:612`

- Proof status: `definitional`
- Depends on: `definition:appC_coherence_functional` (Coherence functional)
- Cites: `definition:appC_coherence_functional` (Coherence functional)
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

$C_{Obs}(e^{itheta} tildepsi_{Obs}, Pi)
= C_{Obs}(tildepsi_{Obs}, Pi)$ (cf. definition:appC_coherence_functional).
The corresponding complex homogeneity is phase-faithful: amplitudes scale through
$overline a a=|a|^2$, not through the real shadow $a^2$.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[PS--C4 (Ray invariance)]
\label{axiom:appC_psc4}
$\mathcal{C}_{\Obs}(e^{i\theta} \tilde\psi_{\Obs}, \Pi)
= \mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \Pi)$ \quad (cf.~\ref{definition:appC_coherence_functional}).
The corresponding complex homogeneity is phase-faithful: amplitudes scale through
$\overline a a=|a|^2$, not through the real shadow $a^2$.
\end{axiom}
```

### PS--C5 (Resolution-limited distinguishability) (`axiom:appC_psc5`)

Role: `axiom` | Type: `axiom` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:620`

- Proof status: `definitional`
- Depends on: `definition:appC_coherence_functional` (Coherence functional)
- Cites: `definition:appC_coherence_functional` (Coherence functional)
- Cited by: `assumption:appC_bounded_discernibility` (Bounded discernibility); `remark:appC_psc3prime_open_route` (Open derivation route for PS--C3$'$)
- Macros used: `\Obs`

**Statement / Body**

If $Pi_1 perp Pi_2$ and $\| Pi_1 - Pi_2 \| > epsilon_{Obs}$,
then both coherence values cannot equal 1 for the same pure state (cf. definition:appC_coherence_functional).

**Verbatim LaTeX Body**

```latex
\begin{axiom}[PS--C5 (Resolution-limited distinguishability)]
\label{axiom:appC_psc5}
If $\Pi_1 \perp \Pi_2$ and $\| \Pi_1 - \Pi_2 \| > \epsilon_{\Obs}$,
then both coherence values cannot equal 1 for the same pure state (cf.~\ref{definition:appC_coherence_functional}).
\end{axiom}
```

### PS--C6 (Pure-state calibration) (`axiom:appC_psc6`)

Role: `axiom` | Type: `axiom` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:626`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

If the observer representation $tildepsi_{Obs}$ represents the normalized pure
state $psiinHorizon$ at the working resolution and
$P_psi:=|psiranglelanglepsi|$, then
\[
C_{Obs}(tildepsi_{Obs},P_psi)=1.
\]
Equivalently, the question whose range is precisely the represented ray is
answered with full coherence by that represented pure state.

**Verbatim LaTeX Body**

```latex
\begin{axiom}[PS--C6 (Pure-state calibration)]
\label{axiom:appC_psc6}
If the observer representation $\tilde\psi_{\Obs}$ represents the normalized pure
state $\psi\in\Horizon$ at the working resolution and
$P_\psi:=|\psi\rangle\langle\psi|$, then
\[
\mathcal{C}_{\Obs}(\tilde\psi_{\Obs},P_\psi)=1.
\]
Equivalently, the question whose range is precisely the represented ray is
answered with full coherence by that represented pure state.
\end{axiom}
```

### Preparatory Lemmas (`subsec:appC_born_lemmas`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:638`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Finite orthogonal additivity gives a Gleason frame function (`lemma:appC_sigma_additivity`)

Role: `lemma` | Type: `lemma` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:641`

- Proof status: `proven`
- Depends on: `axiom:appC_psc3` (PS--C3 (Conservation of interpretive budget)); `theorem:appC_orthogonal_additivity` (Orthogonal additivity from bounded discernibility)
- Cites: `axiom:appC_psc3` (PS--C3 (Conservation of interpretive budget)); `theorem:appC_orthogonal_additivity` (Orthogonal additivity from bounded discernibility)
- Cited by: `proof:appC_born_rule`
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

Let $dimHorizon=d<infty$ and fix an observer-state representation
$tildepsi_{Obs}$. Define
$mu_psi(Pi):=C_{Obs}(tildepsi_{Obs},Pi)$.
Boundedness (PS-C1) and within-frame additivity (PS-C3, now
Cor. axiom:appC_psc3, established as
Thm. theorem:appC_orthogonal_additivity) imply that $mu_psi$ is a
normalized nonnegative finitely additive measure on $Proj(Horizon)$; equivalently, its restriction to
rank-one projectors is a normalized frame function. Since $Horizon$ is finite
dimensional, every orthogonal family of nonzero projectors is finite, so finite
orthogonal additivity is also countable additivity in the only sense required by
finite-dimensional Gleason theory.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Finite orthogonal additivity gives a Gleason frame function]
\label{lemma:appC_sigma_additivity}
Let $\dim\Horizon=d<\infty$ and fix an observer-state representation
$\tilde\psi_{\Obs}$. Define
$\mu_\psi(\Pi):=\mathcal{C}_{\Obs}(\tilde\psi_{\Obs},\Pi)$.
Boundedness (PS--C1) and within-frame additivity (PS--C3, now
Cor.~\ref{axiom:appC_psc3}, established as
Thm.~\ref{theorem:appC_orthogonal_additivity}) imply that $\mu_\psi$ is a
normalized nonnegative finitely additive measure on $Proj(\Horizon)$; equivalently, its restriction to
rank-one projectors is a normalized frame function. Since $\Horizon$ is finite
dimensional, every orthogonal family of nonzero projectors is finite, so finite
orthogonal additivity is also countable additivity in the only sense required by
finite-dimensional Gleason theory.
\end{lemma}
```

### proof:appC_sigma_additivity (`proof:appC_sigma_additivity`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:656`

- Proof status: `not_applicable`
- Depends on: `axiom:appC_psc3` (PS--C3 (Conservation of interpretive budget)); `theorem:appC_orthogonal_additivity` (Orthogonal additivity from bounded discernibility)
- Cites: `axiom:appC_psc3` (PS--C3 (Conservation of interpretive budget)); `theorem:appC_orthogonal_additivity` (Orthogonal additivity from bounded discernibility)
- Cited by: none
- Macros used: none

**Statement / Body**

By PS-C1, $0le mu_psi(Pi)le 1$ for all projectors $Pi$. By
Corollary axiom:appC_psc3, applied to the one-element decomposition
${mathbbm{1}}$, $mu_psi(mathbbm{1})=1$; applying
Theorem theorem:appC_orthogonal_additivity to the empty sum gives
$mu_psi(0)=0$. For any mutually orthogonal finite family
${Pi_i}_{i=1}^n$, Theorem theorem:appC_orthogonal_additivity gives
\[
mu_psi\!left(sum_{i=1}^n Pi_iright)=sum_{i=1}^n mu_psi(Pi_i).
\]
If ${P_i}_{i=1}^d$ is an orthonormal rank-one resolution of the identity, then
$sum_imu_psi(P_i)=mu_psi(mathbbm{1})=1$, which is exactly the normalized
frame-function condition. Finally, an orthogonal family of nonzero subspaces in a
$d$-dimensional Hilbert space has cardinality at most $d$; hence no additional
countable-additivity condition remains to be checked.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_sigma_additivity}
By PS--C1, $0\le \mu_\psi(\Pi)\le 1$ for all projectors $\Pi$. By
Corollary~\ref{axiom:appC_psc3}, applied to the one-element decomposition
$\{\mathbbm{1}\}$, $\mu_\psi(\mathbbm{1})=1$; applying
Theorem~\ref{theorem:appC_orthogonal_additivity} to the empty sum gives
$\mu_\psi(0)=0$. For any mutually orthogonal finite family
$\{\Pi_i\}_{i=1}^n$, Theorem~\ref{theorem:appC_orthogonal_additivity} gives
\[
\mu_\psi\!\left(\sum_{i=1}^n \Pi_i\right)=\sum_{i=1}^n \mu_\psi(\Pi_i).
\]
If $\{P_i\}_{i=1}^d$ is an orthonormal rank-one resolution of the identity, then
$\sum_i\mu_\psi(P_i)=\mu_\psi(\mathbbm{1})=1$, which is exactly the normalized
frame-function condition. Finally, an orthogonal family of nonzero subspaces in a
$d$-dimensional Hilbert space has cardinality at most $d$; hence no additional
countable-additivity condition remains to be checked.
\end{proof}
```

### Unitary covariance of the measure family (`lemma:appC_unitary_invariance`)

Role: `lemma` | Type: `lemma` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:674`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

For every unitary $U$ and projector $Pi$,
\[
mu_{Upsi}(UPi U^dagger)=mu_psi(Pi),
\]
where $mu_psi(Pi):=C_{Obs}(tildepsi_{Obs},Pi)$ and
$mu_{Upsi}$ denotes the assignment associated with the transformed observer
representation $Utildepsi_{Obs}$.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Unitary covariance of the measure family]
\label{lemma:appC_unitary_invariance}
For every unitary $U$ and projector $\Pi$,
\[
\mu_{U\psi}(U\Pi U^\dagger)=\mu_\psi(\Pi),
\]
where $\mu_\psi(\Pi):=\mathcal{C}_{\Obs}(\tilde\psi_{\Obs},\Pi)$ and
$\mu_{U\psi}$ denotes the assignment associated with the transformed observer
representation $U\tilde\psi_{\Obs}$.
\end{lemma}
```

### proof:appC_unitary_invariance (`proof:appC_unitary_invariance`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:685`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

This is precisely PS-C2 written in measure notation:
\[
mu_{Upsi}(UPi U^dagger)
=C_{Obs}(Utildepsi_{Obs},UPi U^dagger)
=C_{Obs}(tildepsi_{Obs},Pi)
=mu_psi(Pi).
\]
Ray invariance PS-C4 ensures that this statement depends only on the ray of the
state representation and not on its arbitrary global phase.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_unitary_invariance}
This is precisely PS--C2 written in measure notation:
\[
\mu_{U\psi}(U\Pi U^\dagger)
=\mathcal{C}_{\Obs}(U\tilde\psi_{\Obs},U\Pi U^\dagger)
=\mathcal{C}_{\Obs}(\tilde\psi_{\Obs},\Pi)
=\mu_\psi(\Pi).
\]
Ray invariance PS--C4 ensures that this statement depends only on the ray of the
state representation and not on its arbitrary global phase.
\end{proof}
```

### Main Theorem (`subsec:appC_born_theorem`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:698`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Observer-relative Born Rule (`theorem:appC_born_rule`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:701`

- Proof status: `proven`
- Depends on: `lemma:appC_sigma_additivity` (Finite orthogonal additivity gives a Gleason frame function)
- Cites: none
- Cited by: `proof:appC_mixed_states`; `proof:appC_qubit_case`; `remark:appC_psc3prime_open_route` (Open derivation route for PS--C3$'$); `remark:bk7_pisu_status` (Status of the trade-off and its corollaries); `scholium:bk7_born_as_hilbert_cross_section` (Born as the Hilbert cross-section); `subsec:bk7_pisu_implications` (Implications)
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

Let $dim Horizon = d geq 3$, let $psiinHorizon$ be normalized, and suppose
PS-C1-PS-C6 hold for the observer representation $tildepsi_{Obs}$. Then for
any rank-one projector $Pi_a = |arangle langle a|$,
\[
C_{Obs}(tildepsi_{Obs}, Pi_a)
= |langle a | psi rangle|^2 .
\]
More generally, for every projector $Piin Proj(Horizon)$,
\[
C_{Obs}(tildepsi_{Obs},Pi)=tr(P_psiPi),
 P_psi:=|psiranglelanglepsi|.
\]

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Observer-relative Born Rule]
\label{theorem:appC_born_rule}
Let $\dim \Horizon = d \geq 3$, let $\psi\in\Horizon$ be normalized, and suppose
PS--C1--PS--C6 hold for the observer representation $\tilde\psi_{\Obs}$. Then for
any rank-one projector $\Pi_a = |a\rangle \langle a|$,
\[
\mathcal{C}_{\Obs}(\tilde\psi_{\Obs}, \Pi_a)
= |\langle a | \psi \rangle|^2 .
\]
More generally, for every projector $\Pi\in Proj(\Horizon)$,
\[
\mathcal{C}_{\Obs}(\tilde\psi_{\Obs},\Pi)=\operatorname{tr}(P_\psi\Pi),
\qquad P_\psi:=|\psi\rangle\langle\psi|.
\]
\end{theorem}
```

### proof:appC_born_rule (`proof:appC_born_rule`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:717`

- Proof status: `not_applicable`
- Depends on: `lemma:appC_sigma_additivity` (Finite orthogonal additivity gives a Gleason frame function)
- Cites: `lemma:appC_sigma_additivity` (Finite orthogonal additivity gives a Gleason frame function)
- Cited by: none
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

Set $mu_psi(Pi)=C_{Obs}(tildepsi_{Obs},Pi)$. By
Lemma lemma:appC_sigma_additivity, $mu_psi$ is a normalized nonnegative
frame function on the projectors of a Hilbert space of dimension at least three.
Finite-dimensional Gleason's theorem therefore gives a unique positive trace-one
operator $W_psi$ such that
\[
mu_psi(Pi)=tr(W_psiPi)
 text{for every }Piin Proj(Horizon).
\]
By PS-C6, $1=mu_psi(P_psi)=tr(W_psi P_psi)
=langlepsi,W_psipsirangle$. Write the spectral decomposition
$W_psi=sum_j p_j |u_jranglelangle u_j|$, with $p_jge0$ and
$sum_j p_j=1$. Then
\[
1=sum_j p_j |langle u_j,psirangle|^2 le sum_j p_j=1.
\]
Equality is possible only when every eigenvector with $p_j>0$ is colinear with
$psi$. Hence $W_psi=P_psi$. Consequently
\[
C_{Obs}(tildepsi_{Obs},Pi)
=tr(P_psiPi)
\]
for all projectors $Pi$. Taking $Pi=Pi_a=|aranglelangle a|$ gives
\[
tr(P_psiPi_a)=langle a,P_psi arangle
=|langle a|psirangle|^2,
\]
which is the Born rule.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_born_rule}
Set $\mu_\psi(\Pi)=\mathcal{C}_{\Obs}(\tilde\psi_{\Obs},\Pi)$. By
Lemma~\ref{lemma:appC_sigma_additivity}, $\mu_\psi$ is a normalized nonnegative
frame function on the projectors of a Hilbert space of dimension at least three.
Finite-dimensional Gleason's theorem therefore gives a unique positive trace-one
operator $W_\psi$ such that
\[
\mu_\psi(\Pi)=\operatorname{tr}(W_\psi\Pi)
\quad\text{for every }\Pi\in Proj(\Horizon).
\]
By PS--C6, $1=\mu_\psi(P_\psi)=\operatorname{tr}(W_\psi P_\psi)
=\langle\psi,W_\psi\psi\rangle$. Write the spectral decomposition
$W_\psi=\sum_j p_j |u_j\rangle\langle u_j|$, with $p_j\ge0$ and
$\sum_j p_j=1$. Then
\[
1=\sum_j p_j |\langle u_j,\psi\rangle|^2 \le \sum_j p_j=1.
\]
Equality is possible only when every eigenvector with $p_j>0$ is colinear with
$\psi$. Hence $W_\psi=P_\psi$. Consequently
\[
\mathcal{C}_{\Obs}(\tilde\psi_{\Obs},\Pi)
=\operatorname{tr}(P_\psi\Pi)
\]
for all projectors $\Pi$. Taking $\Pi=\Pi_a=|a\rangle\langle a|$ gives
\[
\operatorname{tr}(P_\psi\Pi_a)=\langle a,P_\psi a\rangle
=|\langle a|\psi\rangle|^2,
\]
which is the Born rule.
\end{proof}
```

### Qubit case \texorpdfstring{$d = 2$}{d = 2} (`corollary:appC_qubit_case`)

Role: `corollary` | Type: `corollary` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:749`

- Proof status: `proven`
- Depends on: `theorem:appC_born_rule` (Observer-relative Born Rule)
- Cites: none
- Cited by: none
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

Let $Vcongmathbb{C}^2$ be a qubit subspace. If the qubit coherence assignment is
the restriction of a PS-C1-PS-C6 assignment on an embedding
$widehatHorizon=Voplusmathbb{C}$ with represented state
$widehatpsi=psioplus0$, then for every qubit rank-one projector
$Pi_ain Proj(V)$,
\[
C_{Obs}(tildepsi_{Obs},Pi_a)=|langle a|psirangle|^2.
\]

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Qubit case \texorpdfstring{$d = 2$}{d = 2}]
\label{corollary:appC_qubit_case}
Let $V\cong\mathbb{C}^2$ be a qubit subspace. If the qubit coherence assignment is
the restriction of a PS--C1--PS--C6 assignment on an embedding
$\widehat\Horizon=V\oplus\mathbb{C}$ with represented state
$\widehat\psi=\psi\oplus0$, then for every qubit rank-one projector
$\Pi_a\in Proj(V)$,
\[
\mathcal{C}_{\Obs}(\tilde\psi_{\Obs},\Pi_a)=|\langle a|\psi\rangle|^2.
\]
\end{corollary}
```

### proof:appC_qubit_case (`proof:appC_qubit_case`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:761`

- Proof status: `not_applicable`
- Depends on: `theorem:appC_born_rule` (Observer-relative Born Rule)
- Cites: `theorem:appC_born_rule` (Observer-relative Born Rule)
- Cited by: none
- Macros used: `\Horizon`, `\Obs`

**Statement / Body**

Extend the qubit projector to $widehatPi_a=Pi_aoplus0$ on
$widehatHorizon$. The hypotheses place the extended assignment in dimension
$3$, so Theorem theorem:appC_born_rule gives
$widehat{mathcal C}_{Obs}(widehat{tildepsi}_{Obs},widehatPi_a)
=tr(|widehatpsiranglelanglewidehatpsi|widehatPi_a)
=|langle a|psirangle|^2$. Restricting back to $V$ gives the claimed qubit
formula. The extension hypothesis is essential: without it, two-dimensional
Hilbert space admits contextual dispersion-free frame assignments not excluded by
Gleason's theorem alone.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_qubit_case}
Extend the qubit projector to $\widehat\Pi_a=\Pi_a\oplus0$ on
$\widehat\Horizon$. The hypotheses place the extended assignment in dimension
$3$, so Theorem~\ref{theorem:appC_born_rule} gives
$\widehat{\mathcal C}_{\Obs}(\widehat{\tilde\psi}_{\Obs},\widehat\Pi_a)
=\operatorname{tr}(|\widehat\psi\rangle\langle\widehat\psi|\widehat\Pi_a)
=|\langle a|\psi\rangle|^2$. Restricting back to $V$ gives the claimed qubit
formula. The extension hypothesis is essential: without it, two-dimensional
Hilbert space admits contextual dispersion-free frame assignments not excluded by
Gleason's theorem alone.
\end{proof}
```

### Mixed states (`corollary:appC_mixed_states`)

Role: `corollary` | Type: `corollary` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:774`

- Proof status: `proven`
- Depends on: `theorem:appC_born_rule` (Observer-relative Born Rule)
- Cites: none
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

Assume, in addition, that the observer coherence budget is affine under classical
mixtures of preparations. If
$rho = sum_i p_i |psi_iranglelanglepsi_i|$ with $p_ige0$ and
$sum_i p_i=1$, then for every projector $Pi_a$,
\[
C_{Obs}(tilderho_{Obs}, Pi_a) = tr(rho Pi_a).
\]

**Verbatim LaTeX Body**

```latex
\begin{corollary}[Mixed states]
\label{corollary:appC_mixed_states}
Assume, in addition, that the observer coherence budget is affine under classical
mixtures of preparations. If
$\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$ with $p_i\ge0$ and
$\sum_i p_i=1$, then for every projector $\Pi_a$,
\[
\mathcal{C}_{\Obs}(\tilde\rho_{\Obs}, \Pi_a) = \operatorname{tr}(\rho \Pi_a).
\]
\end{corollary}
```

### proof:appC_mixed_states (`proof:appC_mixed_states`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:785`

- Proof status: `not_applicable`
- Depends on: `theorem:appC_born_rule` (Observer-relative Born Rule)
- Cites: `theorem:appC_born_rule` (Observer-relative Born Rule)
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

Affineness of the observer budget gives
\[
C_{Obs}(tilderho_{Obs},Pi_a)
=sum_i p_iC_{Obs}(widetilde{psi_i}_{Obs},Pi_a).
\]
By Theorem theorem:appC_born_rule, each pure component contributes
$C_{Obs}(widetilde{psi_i}_{Obs},Pi_a)
=tr(|psi_iranglelanglepsi_i|Pi_a)$. Therefore
\[
C_{Obs}(tilderho_{Obs},Pi_a)
=sum_i p_itr(|psi_iranglelanglepsi_i|Pi_a)
=tr\!left(sum_i p_i|psi_iranglelanglepsi_i|Pi_aright)
=tr(rhoPi_a).
\]

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_mixed_states}
Affineness of the observer budget gives
\[
\mathcal{C}_{\Obs}(\tilde\rho_{\Obs},\Pi_a)
=\sum_i p_i\mathcal{C}_{\Obs}(\widetilde{\psi_i}_{\Obs},\Pi_a).
\]
By Theorem~\ref{theorem:appC_born_rule}, each pure component contributes
$\mathcal{C}_{\Obs}(\widetilde{\psi_i}_{\Obs},\Pi_a)
=\operatorname{tr}(|\psi_i\rangle\langle\psi_i|\Pi_a)$. Therefore
\[
\mathcal{C}_{\Obs}(\tilde\rho_{\Obs},\Pi_a)
=\sum_i p_i\operatorname{tr}(|\psi_i\rangle\langle\psi_i|\Pi_a)
=\operatorname{tr}\!\left(\sum_i p_i|\psi_i\rangle\langle\psi_i|\Pi_a\right)
=\operatorname{tr}(\rho\Pi_a).
\]
\end{proof}
```

### Interpretation Within Principia Symbolica (`subsec:appC_born_interpretation_ps`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:803`

- Proof status: `not_applicable`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cited by: `definition:appC_observer_token_space` (Observer token space for a projective frame)
- Macros used: none

**Statement / Body**

(no body text extracted)

### Implications and Outlook (`subsec:appC_born_outlook`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:814`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Preamble (`subsec:appC_time_preamble_rigorous`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:829`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Critique of the Entropic Arrow (`subsec:appC_time_critique_rigorous`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:833`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### The Geometric Engine of Irreversibility (`subsec:appC_time_geometric_engine_final`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:837`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Reflective State Space \(\mathcal{S}_O\) (`definition:appC_reflective_state_space`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:841`

- Proof status: `definitional`
- Depends on: `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk4_bounded_observer` (Bounded Observer)
- Cites: `definition:bk1_symbolic_manifold` (Symbolic Manifold); `definition:bk4_bounded_observer` (Bounded Observer)
- Cited by: none
- Macros used: `\Obs`, `\manifold`

**Statement / Body**

A Bounded Observer \(Obs\) (cf. definition:bk4_bounded_observer) does not simply perceive a state \(x in manifold\) (cf. definition:bk1_symbolic_manifold). It perceives a state within the context of its own history, \(H_t\). The true state space is not \(manifold\), but the Reflective State Space \(S_O = manifold times H\), where \(H\) is the space of possible observer histories. A state is a tuple \((x, H_t)\).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Reflective State Space \(\mathcal{S}_O\)]
\label{definition:appC_reflective_state_space}
A Bounded Observer \(\Obs\) (cf.~\ref{definition:bk4_bounded_observer}) does not simply perceive a state \(x \in \manifold\) (cf.~\ref{definition:bk1_symbolic_manifold}). It perceives a state within the context of its own history, \(H_t\). The true state space is not \(\manifold\), but the \textbf{Reflective State Space} \(\mathcal{S}_O = \manifold \times \mathcal{H}\), where \(\mathcal{H}\) is the space of possible observer histories. A state is a tuple \((x, H_t)\).
\end{definition}
```

### The Axiom of Memory (`axiom:appC_axiom_of_memory`)

Role: `axiom` | Type: `axiom` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:846`

- Proof status: `definitional`
- Depends on: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy)
- Cited by: `proof:appC_fundamental_irreversibility`; `proof:appD_titans_as_arrow_of_time`; `proposition:appC_conditional_minimality_2x2` (Conditional Minimality of 2×2 Form); `scholium:appC_time_as_memory` (Time as the Accumulation of Memory); `scholium:appD_axiom_of_memory_titans` (The Axiom of Memory and the "Titans" Architecture)
- Macros used: `\Obs`, `\freeenergy`

**Statement / Body**

Every act of differentiation, \(delta^O\), by a Bounded Observer \(Obs\) necessarily alters its history. If \(delta^O\) maps a state \((x_0, H_{t_0})\) to \((x_1, H_{t_1})\), then \(H_{t_1} neq H_{t_0}\). Specifically, \(H_{t_1}\) contains the trace of the operation that led from \(x_0\) to \(x_1\). This act of recording is metabolically non-zero, incurring a minimal cost in Symbolic Free Energy \(Delta{freeenergy}_{text{mem}} > 0\) (cf. definition:bk2_symbolic_free_energy).

**Verbatim LaTeX Body**

```latex
\begin{axiom}[The Axiom of Memory]
\label{axiom:appC_axiom_of_memory}
Every act of differentiation, \(\delta^O\), by a Bounded Observer \(\Obs\) necessarily alters its history. If \(\delta^O\) maps a state \((x_0, H_{t_0})\) to \((x_1, H_{t_1})\), then \(H_{t_1} \neq H_{t_0}\). Specifically, \(H_{t_1}\) contains the trace of the operation that led from \(x_0\) to \(x_1\). This act of recording is metabolically non-zero, incurring a minimal cost in Symbolic Free Energy \(\Delta{\freeenergy}_{\text{mem}} > 0\) (cf.~\ref{definition:bk2_symbolic_free_energy}).
\end{axiom}
```

### Fundamental Irreversibility of Reflective Observation (`theorem:appC_fundamental_irreversibility_final`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:851`

- Proof status: `proven`
- Depends on: `axiom:appC_axiom_of_memory` (The Axiom of Memory); `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk4_bounded_observer` (Bounded Observer)
- Cites: `definition:bk2_symbolic_free_energy` (Symbolic Free Energy); `definition:bk4_bounded_observer` (Bounded Observer)
- Cited by: `corollary:appC_emergence_of_time_arrow_final` (The Emergence of the Arrow of Time); `proof:appD_titans_as_arrow_of_time`; `scholium:bk4_irreversibility_as_trace` (Irreversibility as Symbolic Trace)
- Macros used: none

**Statement / Body**

Any symbolic process involving a state change perceived by a Bounded Observer (cf. definition:bk4_bounded_observer) is fundamentally irreversible: each observation incurs a non-recoverable cost in Symbolic Free Energy (cf. definition:bk2_symbolic_free_energy).

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Fundamental Irreversibility of Reflective Observation]
\label{theorem:appC_fundamental_irreversibility_final}
Any symbolic process involving a state change perceived by a Bounded Observer (cf.~\ref{definition:bk4_bounded_observer}) is fundamentally irreversible: each observation incurs a non-recoverable cost in Symbolic Free Energy (cf.~\ref{definition:bk2_symbolic_free_energy}).
\end{theorem}
```

### proof:appC_fundamental_irreversibility (`proof:appC_fundamental_irreversibility`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:856`

- Proof status: `not_applicable`
- Depends on: `axiom:appC_axiom_of_memory` (The Axiom of Memory)
- Cites: `axiom:appC_axiom_of_memory` (The Axiom of Memory)
- Cited by: none
- Macros used: `\manifold`

**Statement / Body**

- Consider a process that takes the system from state \(A\) to state \(B\). In the Reflective State Space, this is a transition from \((x_A, H_A)\) to \((x_B, H_B)\). By the Axiom of Memory (Axiom axiom:appC_axiom_of_memory), the history is updated, so \(H_B\) contains the record of the A\(to\)B transformation.


- Now, consider a "reverse" process that takes the system from state \(B\) back to a state geometrically indistinguishable from \(A\). Let this new state be \(A'\). In the base manifold \(manifold\), we have \(x_{A'} = x_A\).


- However, in the full Reflective State Space, the new state is \((x_{A'}, H_{A'})\). The reverse process is also an act of differentiation that must be recorded. Therefore, the new history \(H_{A'}\) contains the record of the B\(to\)A' transformation. It is necessarily different from the original history, \(H_{A'} neq H_A\).


- The full initial and final states are \((x_A, H_A)\) and \((x_{A'}, H_{A'})\). Since \(x_{A'} = x_A\) but \(H_{A'} neq H_A\), the full system state is not restored.
 \[
 (x_A, H_A) neq (x_{A'}, H_{A'})
 \]

- The process is irreversible. The difference between the initial and final states lies not in the geometric position on the base manifold, but in the accumulated history within the observer. This is a fundamental asymmetry.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_fundamental_irreversibility}
\leavevmode

\begin{enumerate}
    \item Consider a process that takes the system from state \(A\) to state \(B\). In the Reflective State Space, this is a transition from \((x_A, H_A)\) to \((x_B, H_B)\). By the Axiom of Memory (Axiom~\ref{axiom:appC_axiom_of_memory}), the history is updated, so \(H_B\) contains the record of the A\(\to\)B transformation.

    \item Now, consider a "reverse" process that takes the system from state \(B\) back to a state geometrically indistinguishable from \(A\). Let this new state be \(A'\). In the base manifold \(\manifold\), we have \(x_{A'} = x_A\).

    \item However, in the full Reflective State Space, the new state is \((x_{A'}, H_{A'})\). The reverse process is also an act of differentiation that must be recorded. Therefore, the new history \(H_{A'}\) contains the record of the B\(\to\)A' transformation. It is necessarily different from the original history, \(H_{A'} \neq H_A\).

    \item The full initial and final states are \((x_A, H_A)\) and \((x_{A'}, H_{A'})\). Since \(x_{A'} = x_A\) but \(H_{A'} \neq H_A\), the full system state is not restored.
    \[
    (x_A, H_A) \neq (x_{A'}, H_{A'})
    \]
    \item The process is irreversible. The difference between the initial and final states lies not in the geometric position on the base manifold, but in the accumulated history within the observer. This is a fundamental asymmetry.
\end{enumerate}
\end{proof}
```

### The Emergence of the Arrow of Time (`corollary:appC_emergence_of_time_arrow_final`)

Role: `corollary` | Type: `corollary` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:875`

- Proof status: `proven`
- Depends on: `theorem:appC_fundamental_irreversibility_final` (Fundamental Irreversibility of Reflective Observation)
- Cites: `theorem:appC_fundamental_irreversibility_final` (Fundamental Irreversibility of Reflective Observation)
- Cited by: none
- Macros used: none

**Statement / Body**

The fundamental irreversibility established in
Theorem theorem:appC_fundamental_irreversibility_final induces a directed
partial order on observer-accessible reflective states. Along any nontrivial
observed path, the order parameter
\[
N(H):=text{the number of recorded differentiation traces in }H
\]
is strictly increasing; if symbolic free-energy minimization selects admissible
successor states, the selected direction is the direction in which records are
accumulated and unrecoverable memory cost has already been paid.

**Verbatim LaTeX Body**

```latex
\begin{corollary}[The Emergence of the Arrow of Time]
\label{corollary:appC_emergence_of_time_arrow_final}
The fundamental irreversibility established in
Theorem~\ref{theorem:appC_fundamental_irreversibility_final} induces a directed
partial order on observer-accessible reflective states. Along any nontrivial
observed path, the order parameter
\[
N(H):=\text{the number of recorded differentiation traces in }H
\]
is strictly increasing; if symbolic free-energy minimization selects admissible
successor states, the selected direction is the direction in which records are
accumulated and unrecoverable memory cost has already been paid.
\end{corollary}
```

### proof:appC_emergence_of_time_arrow_final (`proof:appC_emergence_of_time_arrow_final`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:889`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: `\freeenergy`

**Statement / Body**

Let $(x_n,H_n)$ be a path generated by nontrivial acts of observer
differentiation. By the Axiom of Memory, each step appends a new trace to the
history and incurs positive cost $Delta{freeenergy}_{text{mem}}>0$. Hence
$N(H_{n+1})=N(H_n)+1$ for every observed step, so $N$ is strictly increasing along
the path. A reverse path that restored the base point $x_n$ would still have a
history containing the additional forward and reverse records, and therefore
would have larger $N$ than the original state. Thus the relation
$(x,H)prec(x',H')$ iff $H'$ contains the records of $H$ plus at least one new
record is transitive, antisymmetric up to equality of histories, and nontrivial;
it defines an observer-relative temporal orientation. When the dynamics also
minimize symbolic free energy among admissible successors, this orientation is
the direction along which the system pays and accumulates the non-recoverable
memory costs. That oriented accumulation is the arrow of time.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_emergence_of_time_arrow_final}
Let $(x_n,H_n)$ be a path generated by nontrivial acts of observer
differentiation. By the Axiom of Memory, each step appends a new trace to the
history and incurs positive cost $\Delta{\freeenergy}_{\text{mem}}>0$. Hence
$N(H_{n+1})=N(H_n)+1$ for every observed step, so $N$ is strictly increasing along
the path. A reverse path that restored the base point $x_n$ would still have a
history containing the additional forward and reverse records, and therefore
would have larger $N$ than the original state. Thus the relation
$(x,H)\prec(x',H')$ iff $H'$ contains the records of $H$ plus at least one new
record is transitive, antisymmetric up to equality of histories, and nontrivial;
it defines an observer-relative temporal orientation. When the dynamics also
minimize symbolic free energy among admissible successors, this orientation is
the direction along which the system pays and accumulates the non-recoverable
memory costs. That oriented accumulation is the arrow of time.
\end{proof}
```

### Time as the Accumulation of Memory (`scholium:appC_time_as_memory`)

Role: `scholium` | Type: `scholium` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:906`

- Proof status: `not_applicable`
- Depends on: `axiom:appC_axiom_of_memory` (The Axiom of Memory); `definition:bk1_reflection_operator` (Reflection Operator)
- Cites: `axiom:appC_axiom_of_memory` (The Axiom of Memory); `definition:bk1_reflection_operator` (Reflection Operator)
- Cited by: `scholium:appC_symbolic_geometric_equivalence` (Symbolic–Geometric Equivalence of $\varphi$)
- Macros used: none

**Statement / Body**

This derivation reframes the Arrow of Time. It is not about the universe expanding or entropy increasing. It is about the simple, profound fact that a system capable of knowing cannot "un-know." Every observation, every reflection (cf. definition:bk1_reflection_operator), every act of differentiation leaves a trace, as required by the Axiom of Memory (cf. axiom:appC_axiom_of_memory). Time is the continuous accumulation of these traces. It is the ever-growing distinction between "what was" and "what is," a distinction that exists only for a system that remembers. The irreversibility is not in the world, but in the memory of it.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Time as the Accumulation of Memory]
\label{scholium:appC_time_as_memory}
This derivation reframes the Arrow of Time. It is not about the universe expanding or entropy increasing. It is about the simple, profound fact that a system capable of knowing cannot "un-know." Every observation, every reflection (cf.~\ref{definition:bk1_reflection_operator}), every act of differentiation leaves a trace, as required by the Axiom of Memory (cf.~\ref{axiom:appC_axiom_of_memory}). Time is the continuous accumulation of these traces. It is the ever-growing distinction between "what was" and "what is," a distinction that exists only for a system that remembers. The irreversibility is not in the world, but in the memory of it.
\end{scholium}
```

### \texorpdfstring{Structural Derivations of $\varphi$ Across Symbolic Modalities (`section:appendix_dual_horizon.tex:911`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:911`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic Potential Function (`definition:appC_lagrangian_potential`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:921`

- Proof status: `definitional`
- Depends on: `definition:bk6_drift_operator_complete` (Drift Operator); `definition:bk6_reflection_operator_complete` (Reflection Operator)
- Cites: `definition:bk6_drift_operator_complete` (Drift Operator); `definition:bk6_reflection_operator_complete` (Reflection Operator)
- Cited by: `theorem:appC_phi_from_lagrangian` (Emergence of $\varphi$ from Lagrangian Equilibrium)
- Macros used: none

**Statement / Body**

Define the symbolic potential governing recursive learning as:
\[
V(C) = frac{1}{2} left(C - frac{1}{C} right)^2
\]
This encodes the symbolic tension between drift (cf. Def. definition:bk6_drift_operator_complete) and reflection (Def. definition:bk6_reflection_operator_complete), as defined in Book VI.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Potential Function]
\label{definition:appC_lagrangian_potential}
Define the symbolic potential governing recursive learning as:
\[
V(C) = \frac{1}{2} \left(C - \frac{1}{C} \right)^2
\]
This encodes the symbolic tension between drift (\textit{cf.} Def.~\ref{definition:bk6_drift_operator_complete}) and reflection (Def.~\ref{definition:bk6_reflection_operator_complete}), as defined in Book VI.
\end{definition}
```

### Emergence of $\varphi$ from Lagrangian Equilibrium (`theorem:appC_phi_from_lagrangian`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:930`

- Proof status: `proven`
- Depends on: `definition:appC_lagrangian_potential` (Symbolic Potential Function); `definition:bk1_stage_composite_operator` (Stage–Composite Operator); `definition:bk6_drift_operator_complete` (Drift Operator); `definition:bk6_reflection_operator_complete` (Reflection Operator)
- Cites: `definition:appC_lagrangian_potential` (Symbolic Potential Function)
- Cited by: `proof:appC_phi_min_growth`; `remark:bk5_curvature_vs_chaos` (Scale-Resonant Curvature vs Symbolic Chaos)
- Macros used: none

**Statement / Body**

Let $(C_n)_{nge0}$ be the positive stroboscopic complexity sequence selected by
the drift-reflection balance associated with
Def. definition:appC_lagrangian_potential. Assume the balanced two-step
closure
\[
C_{n+1}=C_n+C_{n-1}, C_0>0, C_1>0,
\]
which says that each new symbolic state preserves the current differentiated
content while reintegrating the immediately preceding memory trace. Then the
successive growth ratios
\[
lambda_n:=frac{C_{n+1}}{C_n}
\]
converge to the golden ratio
$varphi=(1+sqrt5)/2$.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Emergence of $\varphi$ from Lagrangian Equilibrium]
\label{theorem:appC_phi_from_lagrangian}
Let $(C_n)_{n\ge0}$ be the positive stroboscopic complexity sequence selected by
the drift--reflection balance associated with
Def.~\ref{definition:appC_lagrangian_potential}. Assume the balanced two-step
closure
\[
C_{n+1}=C_n+C_{n-1},\qquad C_0>0,\quad C_1>0,
\]
which says that each new symbolic state preserves the current differentiated
content while reintegrating the immediately preceding memory trace. Then the
successive growth ratios
\[
\lambda_n:=\frac{C_{n+1}}{C_n}
\]
converge to the golden ratio
$\varphi=(1+\sqrt5)/2$.
\end{theorem}
```

### proof:appC_phi_from_lagrangian (`proof:appC_phi_from_lagrangian`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:949`

- Proof status: `not_applicable`
- Depends on: `definition:bk1_stage_composite_operator` (Stage–Composite Operator); `definition:bk6_drift_operator_complete` (Drift Operator); `definition:bk6_reflection_operator_complete` (Reflection Operator)
- Cites: `definition:bk1_stage_composite_operator` (Stage–Composite Operator); `definition:bk6_drift_operator_complete` (Drift Operator); `definition:bk6_reflection_operator_complete` (Reflection Operator)
- Cited by: none
- Macros used: none

**Statement / Body**

The recurrence has characteristic polynomial $r^2-r-1=0$, with roots
$varphi=(1+sqrt5)/2$ and $widehatvarphi=(1-sqrt5)/2=-varphi^{-1}$. Hence
\[
C_n=Avarphi^n+Bwidehatvarphi^{ n}
\]
for constants $A,B$ determined by $C_0,C_1$. Since
$A=(C_1-widehatvarphi C_0)/(varphi-widehatvarphi)$ and
$C_0,C_1>0$ while $widehatvarphi<0$, we have $A>0$. Therefore
\[
lambda_n=frac{C_{n+1}}{C_n}
=frac{Avarphi^{n+1}+Bwidehatvarphi^{ n+1}}
 {Avarphi^n+Bwidehatvarphi^{ n}}
longrightarrow varphi,
\]
because $|widehatvarphi|<varphi$. Equivalently, any positive fixed ratio
$lambda$ for the two-step closure must satisfy
$lambda=1+1/lambda$, and the unique positive solution is $varphi$.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_phi_from_lagrangian}
The recurrence has characteristic polynomial $r^2-r-1=0$, with roots
$\varphi=(1+\sqrt5)/2$ and $\widehat\varphi=(1-\sqrt5)/2=-\varphi^{-1}$. Hence
\[
C_n=A\varphi^n+B\widehat\varphi^{\,n}
\]
for constants $A,B$ determined by $C_0,C_1$. Since
$A=(C_1-\widehat\varphi C_0)/(\varphi-\widehat\varphi)$ and
$C_0,C_1>0$ while $\widehat\varphi<0$, we have $A>0$. Therefore
\[
\lambda_n=\frac{C_{n+1}}{C_n}
=\frac{A\varphi^{n+1}+B\widehat\varphi^{\,n+1}}
       {A\varphi^n+B\widehat\varphi^{\,n}}
\longrightarrow \varphi,
\]
because $|\widehat\varphi|<\varphi$. Equivalently, any positive fixed ratio
$\lambda$ for the two-step closure must satisfy
$\lambda=1+1/\lambda$, and the unique positive solution is $\varphi$.
\end{proof}
```

### scholium:appendix_dual_horizon.tex:970 (`scholium:appendix_dual_horizon.tex:970`)

Role: `scholium` | Type: `scholium` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:970`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

This derivation reveals $varphi$ as a symbolic equilibrium point: the unique attractor balancing forward momentum (drift, Def. definition:bk6_drift_operator_complete) and reflective curvature (Def. definition:bk6_reflection_operator_complete). It constitutes a primitive emergence structure (cf. Emergence Operator, Def. definition:bk1_stage_composite_operator).

**Verbatim LaTeX Body**

```latex
\begin{scholium}
This derivation reveals $\varphi$ as a symbolic equilibrium point: the unique attractor balancing forward momentum (drift, Def.~\ref{definition:bk6_drift_operator_complete}) and reflective curvature (Def.~\ref{definition:bk6_reflection_operator_complete}). It constitutes a primitive emergence structure \textit{(cf.} Emergence Operator, Def.~\ref{definition:bk1_stage_composite_operator}).
\end{scholium}
```

### Bounded Observation Frame (`definition:appC_bounded_observation_frame`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:977`

- Proof status: `definitional`
- Depends on: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk4_observer_kernel_convolution_map` (Observer-Kernel Convolution)
- Cites: `definition:bk1_bounded_observer` (Bounded Observer); `definition:bk4_observer_kernel_convolution_map` (Observer-Kernel Convolution)
- Cited by: none
- Macros used: none

**Statement / Body**

Let $H$ be a separable Hilbert space. Define the observer-relative frame (Def. definition:bk4_observer_kernel_convolution_map):
\[
F_delta(t) = {x in H : \|x - x_0(t)\| leq delta}
\]
with $x_0(t)$ the current observer state and $delta$ their perceptual radius (see also bounded observer kernel in Def. definition:bk1_bounded_observer).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Bounded Observation Frame]
\label{definition:appC_bounded_observation_frame}
Let $\mathcal{H}$ be a separable Hilbert space. Define the observer-relative frame (Def.~\ref{definition:bk4_observer_kernel_convolution_map}):
\[
F_\delta(t) = \{x \in \mathcal{H} : \|x - x_0(t)\| \leq \delta\}
\]
with $x_0(t)$ the current observer state and $\delta$ their perceptual radius (see also bounded observer kernel in Def.~\ref{definition:bk1_bounded_observer}).
\end{definition}
```

### Complexity Measure (`definition:appC_complexity_measure`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:986`

- Proof status: `definitional`
- Depends on: `definition:bk1_stage_composite_operator` (Stage–Composite Operator)
- Cites: `definition:bk1_stage_composite_operator` (Stage–Composite Operator)
- Cited by: none
- Macros used: none

**Statement / Body**

The complexity $C(t)$ of the agent’s symbolic representation is:
\[
C(t) = dimleft(text{span}(F_delta(t) cap text{learned_basis}(t))right)
\]
cf. recursive emergence in Def. definition:bk1_stage_composite_operator.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Complexity Measure]
\label{definition:appC_complexity_measure}
The complexity $C(t)$ of the agent’s symbolic representation is:
\[
C(t) = \dim\left(\text{span}(F_\delta(t) \cap \text{learned\_basis}(t))\right)
\]
cf. recursive emergence in Def.~\ref{definition:bk1_stage_composite_operator}.
\end{definition}
```

### Frame Curvature Operator $K_t$ (`definition:appC_frame_curvature_operator`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:998`

- Proof status: `definitional`
- Depends on: `definition:bk6_symbolic_curvature_tensor` (Symbolic Curvature Tensor)
- Cites: `definition:bk6_symbolic_curvature_tensor` (Symbolic Curvature Tensor)
- Cited by: none
- Macros used: none

**Statement / Body**

The curvature of evolving frames is defined symbolically as:
\[
K_t(v) = lim_{h to 0} frac{P_{F_delta(t+h)}(v) - P_{F_delta(t)}(v)}{h}
\]
This parallels the symbolic curvature tensor in Def. definition:bk6_symbolic_curvature_tensor.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Frame Curvature Operator $K_t$]
\label{definition:appC_frame_curvature_operator}
The curvature of evolving frames is defined symbolically as:
\[
K_t(v) = \lim_{h \to 0} \frac{P_{F_\delta(t+h)}(v) - P_{F_\delta(t)}(v)}{h}
\]
This parallels the symbolic curvature tensor in Def.~\ref{definition:bk6_symbolic_curvature_tensor}.
\end{definition}
```

### Banach Space of Curvature Flows (`lemma:appC_banach_space_of_curvature_flows`)

Role: `lemma` | Type: `lemma` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1007`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Fix a finite observation interval $[0,T]$. Let
$L(H)$ denote the bounded operators on the Hilbert space and
let
\[
Lip([0,T],L(H))
:={K:[0,T]toL(H) : Ktext{ is Lipschitz}}
\]
with norm
\[
\|K\|_{Lip}
:=sup_{tin[0,T]}\|K_t\|_{op}
+sup_{sne t}frac{\|K_t-K_s\|_{op}}{|t-s|}.
\]
Then $Lip([0,T],L(H))$ is a Banach space. The
admissible bounded-observer curvature flows satisfying
\[
\|K_t-K_s\|_{op}le C_1delta |t-s| (s,tin[0,T])
\]
form a closed complete subset of this Banach space.

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Banach Space of Curvature Flows]
\label{lemma:appC_banach_space_of_curvature_flows}
Fix a finite observation interval $[0,T]$. Let
$\mathcal{L}(\mathcal{H})$ denote the bounded operators on the Hilbert space and
let
\[
\operatorname{Lip}([0,T],\mathcal{L}(\mathcal{H}))
:=\{K:[0,T]\to\mathcal{L}(\mathcal{H}) : K\text{ is Lipschitz}\}
\]
with norm
\[
\|K\|_{\operatorname{Lip}}
:=\sup_{t\in[0,T]}\|K_t\|_{\mathrm{op}}
+\sup_{s\ne t}\frac{\|K_t-K_s\|_{\mathrm{op}}}{|t-s|}.
\]
Then $\operatorname{Lip}([0,T],\mathcal{L}(\mathcal{H}))$ is a Banach space. The
admissible bounded-observer curvature flows satisfying
\[
\|K_t-K_s\|_{\mathrm{op}}\le C_1\delta |t-s|\qquad(s,t\in[0,T])
\]
form a closed complete subset of this Banach space.
\end{lemma}
```

### proof:appC_banach_space_of_curvature_flows (`proof:appC_banach_space_of_curvature_flows`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1030`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Let $(K^{(m)})$ be a Cauchy sequence in the Lipschitz norm. Then it is Cauchy in
the uniform operator norm, and since $L(H)$ is Banach, there
exists a uniform limit $K:[0,T]toL(H)$. The Lipschitz
seminorms of $K^{(m)}-K^{(ell)}$ also converge to zero, so for every $sne t$
the quotients
\[
frac{(K^{(m)}_t-K^{(m)}_s)-(K^{(ell)}_t-K^{(ell)}_s)}{|t-s|}
\]
are Cauchy in operator norm uniformly over $s,t$. Passing to the uniform limit
shows that $K$ has finite Lipschitz seminorm and that
$\|K^{(m)}-K\|_{Lip}to0$. Thus the space is complete.
If each $K^{(m)}$ satisfies
$\|K^{(m)}_t-K^{(m)}_s\|_{op}le C_1delta |t-s|$, uniform convergence
permits passage to the limit, giving the same inequality for $K$. Hence the
admissible class is closed and therefore complete.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_banach_space_of_curvature_flows}
Let $(K^{(m)})$ be a Cauchy sequence in the Lipschitz norm. Then it is Cauchy in
the uniform operator norm, and since $\mathcal{L}(\mathcal{H})$ is Banach, there
exists a uniform limit $K:[0,T]\to\mathcal{L}(\mathcal{H})$. The Lipschitz
seminorms of $K^{(m)}-K^{(\ell)}$ also converge to zero, so for every $s\ne t$
the quotients
\[
\frac{(K^{(m)}_t-K^{(m)}_s)-(K^{(\ell)}_t-K^{(\ell)}_s)}{|t-s|}
\]
are Cauchy in operator norm uniformly over $s,t$. Passing to the uniform limit
shows that $K$ has finite Lipschitz seminorm and that
$\|K^{(m)}-K\|_{\operatorname{Lip}}\to0$. Thus the space is complete.
If each $K^{(m)}$ satisfies
$\|K^{(m)}_t-K^{(m)}_s\|_{\mathrm{op}}\le C_1\delta |t-s|$, uniform convergence
permits passage to the limit, giving the same inequality for $K$. Hence the
admissible class is closed and therefore complete.
\end{proof}
```

### Sustainable Growth Rate (`definition:appC_sustainable_growth_rate`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1052`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `theorem:appC_phi_min_growth` (Golden Ratio as Minimal Sustainable Growth Rate); `theorem:appC_phi_minimized_entropy_per_complexity` ($\varphi$ Minimizes Entropy-per-Complexity)
- Macros used: none

**Statement / Body**

A growth rate $lambda>1$ is sustainable for a bounded recursive observer if
there exists a positive complexity sequence $(C_n)$ with finite asymptotic ratio
\[
lambda=lim_{ntoinfty}frac{C_{n+1}}{C_n}
\]
and satisfying the drift-reflection retention constraint
\[
C_{n+1}ge C_n+C_{n-1} (nge1).
\]
Equality is the minimal balanced closure: the next state preserves current
symbolic content and exactly one previous memory trace, with no superfluous
expansion.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Sustainable Growth Rate]
\label{definition:appC_sustainable_growth_rate}
A growth rate $\lambda>1$ is \emph{sustainable} for a bounded recursive observer if
there exists a positive complexity sequence $(C_n)$ with finite asymptotic ratio
\[
\lambda=\lim_{n\to\infty}\frac{C_{n+1}}{C_n}
\]
and satisfying the drift--reflection retention constraint
\[
C_{n+1}\ge C_n+C_{n-1}\qquad(n\ge1).
\]
Equality is the minimal balanced closure: the next state preserves current
symbolic content and exactly one previous memory trace, with no superfluous
expansion.
\end{definition}
```

### Golden Ratio as Minimal Sustainable Growth Rate (`theorem:appC_phi_min_growth`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1068`

- Proof status: `proven`
- Depends on: `definition:appC_sustainable_growth_rate` (Sustainable Growth Rate); `theorem:appC_phi_from_lagrangian` (Emergence of $\varphi$ from Lagrangian Equilibrium)
- Cites: `definition:appC_sustainable_growth_rate` (Sustainable Growth Rate)
- Cited by: `proof:appC_phi_minimized_entropy_per_complexity`
- Macros used: none

**Statement / Body**

Among all sustainable growth rates in the sense of
Def. definition:appC_sustainable_growth_rate, the least possible value is
$varphi$.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Golden Ratio as Minimal Sustainable Growth Rate]
\label{theorem:appC_phi_min_growth}
Among all sustainable growth rates in the sense of
Def.~\ref{definition:appC_sustainable_growth_rate}, the least possible value is
$\varphi$.
\end{theorem}
```

### proof:appC_phi_min_growth (`proof:appC_phi_min_growth`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1075`

- Proof status: `not_applicable`
- Depends on: `theorem:appC_phi_from_lagrangian` (Emergence of $\varphi$ from Lagrangian Equilibrium)
- Cites: `theorem:appC_phi_from_lagrangian` (Emergence of $\varphi$ from Lagrangian Equilibrium)
- Cited by: none
- Macros used: none

**Statement / Body**

Let $lambda$ be sustainable and let $(C_n)$ witness sustainability. Divide
$C_{n+1}ge C_n+C_{n-1}$ by $C_n>0$ and pass to the limit:
\[
lambda=lim_{ntoinfty}frac{C_{n+1}}{C_n}
ge 1+lim_{ntoinfty}frac{C_{n-1}}{C_n}
=1+frac{1}{lambda}.
\]
Thus $lambda^2-lambda-1ge0$. Since $lambda>0$, this implies
$lambdage(1+sqrt5)/2=varphi$. The equality recurrence
$C_{n+1}=C_n+C_{n-1}$ with $C_0,C_1>0$ has asymptotic ratio $varphi$ by
Theorem theorem:appC_phi_from_lagrangian; hence the lower bound is sharp.
Therefore the minimal sustainable growth rate is $varphi$.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_phi_min_growth}
Let $\lambda$ be sustainable and let $(C_n)$ witness sustainability. Divide
$C_{n+1}\ge C_n+C_{n-1}$ by $C_n>0$ and pass to the limit:
\[
\lambda=\lim_{n\to\infty}\frac{C_{n+1}}{C_n}
\ge 1+\lim_{n\to\infty}\frac{C_{n-1}}{C_n}
=1+\frac{1}{\lambda}.
\]
Thus $\lambda^2-\lambda-1\ge0$. Since $\lambda>0$, this implies
$\lambda\ge(1+\sqrt5)/2=\varphi$. The equality recurrence
$C_{n+1}=C_n+C_{n-1}$ with $C_0,C_1>0$ has asymptotic ratio $\varphi$ by
Theorem~\ref{theorem:appC_phi_from_lagrangian}; hence the lower bound is sharp.
Therefore the minimal sustainable growth rate is $\varphi$.
\end{proof}
```

### Complexity Growth Operator $G$ (`definition:appC_complexity_growth_operator`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1094`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `theorem:appC_phi_as_spectral_radius` (Spectral Radius of $G$ Equals $\varphi$)
- Macros used: none

**Statement / Body**

Work in $mathbb{R}^2$ with any norm, encoding a two-step symbolic state
as $(C_n,C_{n-1})^T$. Define the balanced complexity growth operator
\[
Gx\y
=x+y\x,

G=1&1\\1&0.
\]
This is the linear operator form of the minimal drift-reflection closure
$C_{n+1}=C_n+C_{n-1}$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Complexity Growth Operator $G$]
\label{definition:appC_complexity_growth_operator}
Work in $\mathbb{R}^2$ with any norm, encoding a two-step symbolic state
as $(C_n,C_{n-1})^T$. Define the balanced complexity growth operator
\[
G\begin{pmatrix}x\\y\end{pmatrix}
=\begin{pmatrix}x+y\\x\end{pmatrix},
\qquad
G=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
This is the linear operator form of the minimal drift--reflection closure
$C_{n+1}=C_n+C_{n-1}$.
\end{definition}
```

### Spectral Radius of $G$ Equals $\varphi$ (`theorem:appC_phi_as_spectral_radius`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1108`

- Proof status: `proven`
- Depends on: `definition:appC_complexity_growth_operator` (Complexity Growth Operator $G$)
- Cites: `definition:appC_complexity_growth_operator` (Complexity Growth Operator $G$)
- Cited by: `remark:bk5_curvature_vs_chaos` (Scale-Resonant Curvature vs Symbolic Chaos)
- Macros used: none

**Statement / Body**

For $G$ defined in Def. definition:appC_complexity_growth_operator,
\[
rho(G)=lim_{n to infty} \|G^n\|^{1/n} = varphi .
\]

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Spectral Radius of $G$ Equals $\varphi$]
\label{theorem:appC_phi_as_spectral_radius}
For $G$ defined in Def.~\ref{definition:appC_complexity_growth_operator},
\[
\rho(G)=\lim_{n \to \infty} \|G^n\|^{1/n} = \varphi .
\]
\end{theorem}
```

### proof:appC_phi_as_spectral_radius (`proof:appC_phi_as_spectral_radius`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1116`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The characteristic polynomial of $G$ is
\[
det\!1-mu&1\\1&-mu
=mu^2-mu-1.
\]
Its eigenvalues are $varphi=(1+sqrt5)/2$ and
$widehatvarphi=(1-sqrt5)/2=-varphi^{-1}$. Hence the spectral radius is
$rho(G)=max{|varphi|,|widehatvarphi|}=varphi$. Since $G$ is a finite
matrix, Gelfand's formula gives $rho(G)=lim_{ntoinfty}\|G^n\|^{1/n}$ for any
matrix norm.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_phi_as_spectral_radius}
The characteristic polynomial of $G$ is
\[
\det\!\begin{pmatrix}1-\mu&1\\1&-\mu\end{pmatrix}
=\mu^2-\mu-1.
\]
Its eigenvalues are $\varphi=(1+\sqrt5)/2$ and
$\widehat\varphi=(1-\sqrt5)/2=-\varphi^{-1}$. Hence the spectral radius is
$\rho(G)=\max\{|\varphi|,|\widehat\varphi|\}=\varphi$. Since $G$ is a finite
matrix, Gelfand's formula gives $\rho(G)=\lim_{n\to\infty}\|G^n\|^{1/n}$ for any
matrix norm.
\end{proof}
```

### Complexity--Entropy Tradeoff (`definition:appC_complexity_entropy_tradeof`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1133`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `theorem:appC_phi_minimized_entropy_per_complexity` ($\varphi$ Minimizes Entropy-per-Complexity)
- Macros used: none

**Statement / Body**

For a sustainable asymptotic growth factor $lambda$, define the normalized
one-step symbolic inefficiency
\[
I(lambda):=lambda+frac{1}{lambda}.
\]
The first term records forward expansion cost; the second records the reflective
memory load required by bounded retention. This is the dimensionless
entropy-per-complexity overhead associated with one asymptotic drift-reflection
step.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Complexity--Entropy Tradeoff]
\label{definition:appC_complexity_entropy_tradeof}
For a sustainable asymptotic growth factor $\lambda$, define the normalized
one-step symbolic inefficiency
\[
\mathcal{I}(\lambda):=\lambda+\frac{1}{\lambda}.
\]
The first term records forward expansion cost; the second records the reflective
memory load required by bounded retention. This is the dimensionless
entropy-per-complexity overhead associated with one asymptotic drift--reflection
step.
\end{definition}
```

### $\varphi$ Minimizes Entropy-per-Complexity (`theorem:appC_phi_minimized_entropy_per_complexity`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1146`

- Proof status: `proven`
- Depends on: `definition:appC_complexity_entropy_tradeof` (Complexity--Entropy Tradeoff); `definition:appC_sustainable_growth_rate` (Sustainable Growth Rate); `theorem:appC_phi_min_growth` (Golden Ratio as Minimal Sustainable Growth Rate)
- Cites: `definition:appC_complexity_entropy_tradeof` (Complexity--Entropy Tradeoff); `definition:appC_sustainable_growth_rate` (Sustainable Growth Rate)
- Cited by: none
- Macros used: none

**Statement / Body**

Among all sustainable growth rates $lambda$ in the sense of
Def. definition:appC_sustainable_growth_rate, the inefficiency
$I(lambda)$ of Def. definition:appC_complexity_entropy_tradeof is
minimized at $lambda=varphi$.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[$\varphi$ Minimizes Entropy-per-Complexity]
\label{theorem:appC_phi_minimized_entropy_per_complexity}
Among all sustainable growth rates $\lambda$ in the sense of
Def.~\ref{definition:appC_sustainable_growth_rate}, the inefficiency
$\mathcal{I}(\lambda)$ of Def.~\ref{definition:appC_complexity_entropy_tradeof} is
minimized at $\lambda=\varphi$.
\end{theorem}
```

### proof:appC_phi_minimized_entropy_per_complexity (`proof:appC_phi_minimized_entropy_per_complexity`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1154`

- Proof status: `not_applicable`
- Depends on: `theorem:appC_phi_min_growth` (Golden Ratio as Minimal Sustainable Growth Rate)
- Cites: `theorem:appC_phi_min_growth` (Golden Ratio as Minimal Sustainable Growth Rate)
- Cited by: none
- Macros used: none

**Statement / Body**

By Theorem theorem:appC_phi_min_growth, every sustainable $lambda$ satisfies
$lambdagevarphi>1$. On $(1,infty)$,
\[
I'(lambda)=1-frac{1}{lambda^2}>0,
\]
so $I$ is strictly increasing throughout the feasible interval
$[varphi,infty)$. Therefore the minimum over sustainable rates occurs at the
left endpoint $lambda=varphi$.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_phi_minimized_entropy_per_complexity}
By Theorem~\ref{theorem:appC_phi_min_growth}, every sustainable $\lambda$ satisfies
$\lambda\ge\varphi>1$. On $(1,\infty)$,
\[
\mathcal{I}'(\lambda)=1-\frac{1}{\lambda^2}>0,
\]
so $\mathcal{I}$ is strictly increasing throughout the feasible interval
$[\varphi,\infty)$. Therefore the minimum over sustainable rates occurs at the
left endpoint $\lambda=\varphi$.
\end{proof}
```

### $\varphi$-Stable Region (`definition:appC_phi_stable_region`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1169`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `proof:appC_geodesic_convergence`
- Macros used: none

**Statement / Body**

Let $Phi$ be the entropy-minimizing reflective update map on the observer's
symbolic manifold. A region $M_varphi$ is $varphi$-stable if:


- it is invariant under the update, $Phi(M_varphi)subseteq M_varphi$;

- along $M_varphi$ the curvature operator satisfies
 \[
 langle K_t(v), v rangle = varphi^{-1} \|v\|^2;
 \]

- there is a neighborhood $U$ of $M_varphi$ and a constant $q<1$ such that
 \[
 d(Phi(x),M_varphi)le q d(x,M_varphi) (xin U).
 \]

**Verbatim LaTeX Body**

```latex
\begin{definition}[$\varphi$-Stable Region]
\label{definition:appC_phi_stable_region}
Let $\Phi$ be the entropy-minimizing reflective update map on the observer's
symbolic manifold. A region $M_\varphi$ is \emph{$\varphi$-stable} if:
\begin{enumerate}
    \item it is invariant under the update, $\Phi(M_\varphi)\subseteq M_\varphi$;
    \item along $M_\varphi$ the curvature operator satisfies
    \[
    \langle K_t(v), v \rangle = \varphi^{-1} \|v\|^2;
    \]
    \item there is a neighborhood $U$ of $M_\varphi$ and a constant $q<1$ such that
    \[
    d(\Phi(x),M_\varphi)\le q\,d(x,M_\varphi)\qquad(x\in U).
    \]
\end{enumerate}
\end{definition}
```

### Geodesic Convergence to $M_\varphi$ (`lemma:appC_geodesic_convergence`)

Role: `lemma` | Type: `lemma` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1186`

- Proof status: `proven`
- Depends on: `definition:appC_phi_stable_region` ($\varphi$-Stable Region)
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

If an observer trajectory $x_{n+1}=Phi(x_n)$ remains in the neighborhood $U$ of a
$varphi$-stable region $M_varphi$, then $x_n$ converges to $M_varphi$ in
observer-relative distance:
\[
 d(x_n,M_varphi)le q^n d(x_0,M_varphi)longrightarrow0 .
\]

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Geodesic Convergence to $M_\varphi$]
\label{lemma:appC_geodesic_convergence}
If an observer trajectory $x_{n+1}=\Phi(x_n)$ remains in the neighborhood $U$ of a
$\varphi$-stable region $M_\varphi$, then $x_n$ converges to $M_\varphi$ in
observer-relative distance:
\[
 d(x_n,M_\varphi)\le q^n d(x_0,M_\varphi)\longrightarrow0 .
\]
\end{lemma}
```

### proof:appC_geodesic_convergence (`proof:appC_geodesic_convergence`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1196`

- Proof status: `not_applicable`
- Depends on: `definition:appC_phi_stable_region` ($\varphi$-Stable Region)
- Cites: `definition:appC_phi_stable_region` ($\varphi$-Stable Region)
- Cited by: none
- Macros used: none

**Statement / Body**

The contraction clause in Def. definition:appC_phi_stable_region gives
$d(x_{n+1},M_varphi)=d(Phi(x_n),M_varphi)le qd(x_n,M_varphi)$ whenever
$x_nin U$. Iterating yields
$d(x_n,M_varphi)le q^n d(x_0,M_varphi)$. Since $0le q<1$, $q^nto0$, so the
distance from the trajectory to $M_varphi$ tends to zero. Invariance of
$M_varphi$ ensures that once the trajectory reaches the stable region it remains
there.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_geodesic_convergence}
The contraction clause in Def.~\ref{definition:appC_phi_stable_region} gives
$d(x_{n+1},M_\varphi)=d(\Phi(x_n),M_\varphi)\le qd(x_n,M_\varphi)$ whenever
$x_n\in U$. Iterating yields
$d(x_n,M_\varphi)\le q^n d(x_0,M_\varphi)$. Since $0\le q<1$, $q^n\to0$, so the
distance from the trajectory to $M_\varphi$ tends to zero. Invariance of
$M_\varphi$ ensures that once the trajectory reaches the stable region it remains
there.
\end{proof}
```

### Symbolic–Geometric Equivalence of $\varphi$ (`scholium:appC_symbolic_geometric_equivalence`)

Role: `scholium` | Type: `scholium` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1207`

- Proof status: `not_applicable`
- Depends on: `scholium:appC_time_as_memory` (Time as the Accumulation of Memory); `scholium:appC_two_horizons_co_constitutive` (The Two Horizons as Co-Constitutive)
- Cites: `scholium:appC_time_as_memory` (Time as the Accumulation of Memory); `scholium:appC_two_horizons_co_constitutive` (The Two Horizons as Co-Constitutive)
- Cited by: none
- Macros used: none

**Statement / Body**

The golden ratio appears in symbolic thermodynamics, curvature operators, and recursive observer models. It is a structural attractor unifying symbolic emergence (cf. Scholium scholium:appC_two_horizons_co_constitutive) and the memory-based geometry of time (Scholium scholium:appC_time_as_memory).

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Symbolic–Geometric Equivalence of $\varphi$]
\label{scholium:appC_symbolic_geometric_equivalence}
The golden ratio appears in symbolic thermodynamics, curvature operators, and recursive observer models. It is a structural attractor unifying symbolic emergence (cf. Scholium~\ref{scholium:appC_two_horizons_co_constitutive}) and the memory-based geometry of time (Scholium~\ref{scholium:appC_time_as_memory}).
\end{scholium}
```

### Symbolic Operator Assumptions (`definition:appC_symbolic_operator_assumptions`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1215`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `lemma:appC_matrix_representation_symbolic_operators` (Matrix Representation of Symbolic Operators)
- Macros used: none

**Statement / Body**

Assume symbolic emergence is represented by a positive two-step complexity
sequence $(s_n)$ whose state vector is
\[
s_n=(s_n,s_{n-1})^T.
\]
The minimal drift-reflection closure preserves current symbolic content and one
memory trace:
\[
s_{n+1}=s_n+s_{n-1}.
\]
Thus Drift contributes the current term $s_n$, Reflection contributes the retained
memory term $s_{n-1}$, and recursive emergence is their balanced composition.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Operator Assumptions]
\label{definition:appC_symbolic_operator_assumptions}
Assume symbolic emergence is represented by a positive two-step complexity
sequence $(s_n)$ whose state vector is
\[
\mathbf{s}_n=(s_n,s_{n-1})^T.
\]
The minimal drift--reflection closure preserves current symbolic content and one
memory trace:
\[
s_{n+1}=s_n+s_{n-1}.
\]
Thus Drift contributes the current term $s_n$, Reflection contributes the retained
memory term $s_{n-1}$, and recursive emergence is their balanced composition.
\end{definition}
```

### Matrix Representation of Symbolic Operators (`lemma:appC_matrix_representation_symbolic_operators`)

Role: `lemma` | Type: `lemma` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1231`

- Proof status: `proven`
- Depends on: `definition:appC_symbolic_operator_assumptions` (Symbolic Operator Assumptions)
- Cites: `definition:appC_symbolic_operator_assumptions` (Symbolic Operator Assumptions)
- Cited by: `proof:appC_conditional_minimality_2x2`; `theorem:appC_unified_recursive_fixed_point` (Unified Recursive Fixed Point)
- Macros used: none

**Statement / Body**

Under the two-step closure of
Def. definition:appC_symbolic_operator_assumptions, symbolic evolution is
represented by
\[
M=1&1\\1&0,

s_{n+1}=Ms_n.
\]

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Matrix Representation of Symbolic Operators]
\label{lemma:appC_matrix_representation_symbolic_operators}
Under the two-step closure of
Def.~\ref{definition:appC_symbolic_operator_assumptions}, symbolic evolution is
represented by
\[
M=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\qquad
\mathbf{s}_{n+1}=M\mathbf{s}_n.
\]
\end{lemma}
```

### proof:appC_matrix_rep_symbolic_operators (`proof:appC_matrix_rep_symbolic_operators`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1243`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

By definition,
$s_{n+1}=s_n+s_{n-1}$ and the memory coordinate updates by
$s_nmapsto s_n$. Therefore
\[
s_{n+1}\s_n
=s_n+s_{n-1}\s_n
=1&1\\1&0
s_n\s_{n-1}.
\]
This proves the claimed matrix representation.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_matrix_rep_symbolic_operators}
By definition,
$s_{n+1}=s_n+s_{n-1}$ and the memory coordinate updates by
$s_n\mapsto s_n$. Therefore
\[
\begin{pmatrix}s_{n+1}\\s_n\end{pmatrix}
=\begin{pmatrix}s_n+s_{n-1}\\s_n\end{pmatrix}
=\begin{pmatrix}1&1\\1&0\end{pmatrix}
\begin{pmatrix}s_n\\s_{n-1}\end{pmatrix}.
\]
This proves the claimed matrix representation.
\end{proof}
```

### Golden Ratio as Eigenvalue of Recursive Emergence (`theorem:appC_phi_eigenvalue_recursive_emergence`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1257`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The golden ratio $varphi$ is the Perron-Frobenius eigenvalue, hence the dominant
asymptotic growth factor, of the minimal recursive-emergence matrix
$M=bigl(1&1\\1&0bigr)$.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Golden Ratio as Eigenvalue of Recursive Emergence]
\label{theorem:appC_phi_eigenvalue_recursive_emergence}
The golden ratio $\varphi$ is the Perron--Frobenius eigenvalue, hence the dominant
asymptotic growth factor, of the minimal recursive-emergence matrix
$M=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)$.
\end{theorem}
```

### proof:appC_phi_eigenvalue_recursive_emergence (`proof:appC_phi_eigenvalue_recursive_emergence`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1264`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The characteristic polynomial is
\[
det(M-mu I)=det1-mu&1\\1&-mu
=mu^2-mu-1.
\]
Its roots are
\[
mu_+=frac{1+sqrt5}{2}=varphi,

mu_- =frac{1-sqrt5}{2}=-varphi^{-1}.
\]
Since $|mu_-|<mu_+$, the spectral radius is $varphi$. The matrix has strictly
positive powers after finitely many steps, so the Perron-Frobenius eigenvalue is
real, positive, simple, and equal to this spectral radius. Hence generic positive
state vectors grow asymptotically at rate $varphi$.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_phi_eigenvalue_recursive_emergence}
The characteristic polynomial is
\[
\det(M-\mu I)=\det\begin{pmatrix}1-\mu&1\\1&-\mu\end{pmatrix}
=\mu^2-\mu-1.
\]
Its roots are
\[
\mu_+=\frac{1+\sqrt5}{2}=\varphi,
\qquad
\mu_- =\frac{1-\sqrt5}{2}=-\varphi^{-1}.
\]
Since $|\mu_-|<\mu_+$, the spectral radius is $\varphi$. The matrix has strictly
positive powers after finitely many steps, so the Perron--Frobenius eigenvalue is
real, positive, simple, and equal to this spectral radius. Hence generic positive
state vectors grow asymptotically at rate $\varphi$.
\end{proof}
```

### Fibonacci Structure via Matrix Powers (`lemma:appC_fibonacci_structure_matrix_powers`)

Role: `lemma` | Type: `lemma` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1283`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Let $F_0=0$, $F_1=1$, and $F_{n+1}=F_n+F_{n-1}$. For
$M=bigl(1&1\\1&0bigr)$,
\[
M^n=F_{n+1}&F_n\F_n&F_{n-1} (nge1).
\]

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Fibonacci Structure via Matrix Powers]
\label{lemma:appC_fibonacci_structure_matrix_powers}
Let $F_0=0$, $F_1=1$, and $F_{n+1}=F_n+F_{n-1}$. For
$M=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)$,
\[
M^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}\qquad(n\ge1).
\]
\end{lemma}
```

### proof:appC_fibonacci_matrix_powers (`proof:appC_fibonacci_matrix_powers`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1292`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

For $n=1$ the formula gives
$bigl(F_2&F_1\F_1&F_0bigr)
=bigl(1&1\\1&0bigr)=M$. Assume the formula
holds for $n$. Then
\[
M^{n+1}=M^nM
=F_{n+1}&F_n\F_n&F_{n-1}
 1&1\\1&0
=F_{n+1}+F_n&F_{n+1}\F_n+F_{n-1}&F_n
=F_{n+2}&F_{n+1}\F_{n+1}&F_n.
\]
This is the formula with $n$ replaced by $n+1$.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_fibonacci_matrix_powers}
For $n=1$ the formula gives
$\bigl(\begin{smallmatrix}F_2&F_1\\F_1&F_0\end{smallmatrix}\bigr)
=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)=M$. Assume the formula
holds for $n$. Then
\[
M^{n+1}=M^nM
=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}
 \begin{pmatrix}1&1\\1&0\end{pmatrix}
=\begin{pmatrix}F_{n+1}+F_n&F_{n+1}\\F_n+F_{n-1}&F_n\end{pmatrix}
=\begin{pmatrix}F_{n+2}&F_{n+1}\\F_{n+1}&F_n\end{pmatrix}.
\]
This is the formula with $n$ replaced by $n+1$.
\end{proof}
```

### Conditional Minimality of 2×2 Form (`proposition:appC_conditional_minimality_2x2`)

Role: `proposition` | Type: `proposition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1308`

- Proof status: `proven`
- Depends on: `axiom:appC_axiom_of_memory` (The Axiom of Memory); `lemma:appC_matrix_representation_symbolic_operators` (Matrix Representation of Symbolic Operators)
- Cites: `axiom:appC_axiom_of_memory` (The Axiom of Memory)
- Cited by: none
- Macros used: none

**Statement / Body**

Under the assumption that symbolic emergence requires encoding both current state
and one memory state, the 2×2 matrix form is minimal for representing the
drift-reflection composition (see Axiom axiom:appC_axiom_of_memory).

**Verbatim LaTeX Body**

```latex
\begin{proposition}[Conditional Minimality of 2×2 Form]
\label{proposition:appC_conditional_minimality_2x2}
Under the assumption that symbolic emergence requires encoding both current state
and one memory state, the 2×2 matrix form is minimal for representing the
drift-reflection composition (see Axiom~\ref{axiom:appC_axiom_of_memory}).
\end{proposition}
```

### proof:appC_conditional_minimality_2x2 (`proof:appC_conditional_minimality_2x2`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1315`

- Proof status: `not_applicable`
- Depends on: `lemma:appC_matrix_representation_symbolic_operators` (Matrix Representation of Symbolic Operators)
- Cites: `lemma:appC_matrix_representation_symbolic_operators` (Matrix Representation of Symbolic Operators)
- Cited by: none
- Macros used: none

**Statement / Body**

A one-dimensional linear state stores only one scalar degree of freedom at step
$n$. It can represent a Markov update $s_{n+1}=a s_n$, but it cannot distinguish
two histories with the same current value $s_n$ and different previous values
$s_{n-1}$, even though the required recursion
$s_{n+1}=f(s_n,s_{n-1})$ depends on both. Therefore dimension one is insufficient
for memory-dependent emergence. Dimension two is sufficient, because the state
vector $(s_n,s_{n-1})^T$ and the matrix in
Lemma lemma:appC_matrix_representation_symbolic_operators exactly encode the
current value and one retained memory trace. Hence $2times2$ is minimal under the
stated one-step-memory assumption.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_conditional_minimality_2x2}
A one-dimensional linear state stores only one scalar degree of freedom at step
$n$. It can represent a Markov update $s_{n+1}=a s_n$, but it cannot distinguish
two histories with the same current value $s_n$ and different previous values
$s_{n-1}$, even though the required recursion
$s_{n+1}=f(s_n,s_{n-1})$ depends on both. Therefore dimension one is insufficient
for memory-dependent emergence. Dimension two is sufficient, because the state
vector $(s_n,s_{n-1})^T$ and the matrix in
Lemma~\ref{lemma:appC_matrix_representation_symbolic_operators} exactly encode the
current value and one retained memory trace. Hence $2\times2$ is minimal under the
stated one-step-memory assumption.
\end{proof}
```

### Bounded Symbolic Observer Dynamics (`definition:appC_bounded_symbolic_observer_dynamics`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1332`

- Proof status: `definitional`
- Depends on: `definition:bk4_bounded_observer` (Bounded Observer)
- Cites: `definition:bk4_bounded_observer` (Bounded Observer)
- Cited by: `definition:appC_symbolic_curvature_function` (Symbolic Curvature Function); `proof:appC_geometric_interpretation_curvature`
- Macros used: none

**Statement / Body**

Consider a symbolic observer with bounded attention radius $delta$ (cf. definition:bk4_bounded_observer) navigating meaning space. The observer experiences:

- Forward drift: tendency to explore new symbolic territory at rate $theta$

- Reflective curvature: memory-based constraint pulling back with strength $1/theta$

- Bounded exploration: total symbolic displacement must remain finite

**Verbatim LaTeX Body**

```latex
\begin{definition}[Bounded Symbolic Observer Dynamics]
\label{definition:appC_bounded_symbolic_observer_dynamics}
Consider a symbolic observer with bounded attention radius $\delta$ (cf.~\ref{definition:bk4_bounded_observer}) navigating meaning space. The observer experiences:
\begin{itemize}
\item Forward drift: tendency to explore new symbolic territory at rate $\theta$
\item Reflective curvature: memory-based constraint pulling back with strength $1/\theta$
\item Bounded exploration: total symbolic displacement must remain finite
\end{itemize}
\end{definition}
```

### Symbolic Curvature Function (`definition:appC_symbolic_curvature_function`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1342`

- Proof status: `definitional`
- Depends on: `definition:appC_bounded_symbolic_observer_dynamics` (Bounded Symbolic Observer Dynamics)
- Cites: `definition:appC_bounded_symbolic_observer_dynamics` (Bounded Symbolic Observer Dynamics)
- Cited by: none
- Macros used: none

**Statement / Body**

The total symbolic curvature experienced by the observer (Def. definition:appC_bounded_symbolic_observer_dynamics) is:
\[
kappa(theta) = theta + frac{1}{theta}
\]
where $theta > 0$ represents the ratio of forward drift to reflective strength.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Curvature Function]
\label{definition:appC_symbolic_curvature_function}
The total symbolic curvature experienced by the observer (Def.~\ref{definition:appC_bounded_symbolic_observer_dynamics}) is:
\[
\kappa(\theta) = \theta + \frac{1}{\theta}
\]
where $\theta > 0$ represents the ratio of forward drift to reflective strength.
\end{definition}
```

### Geometric Interpretation of Curvature Terms (`lemma:appC_geometric_interpretation_curvature`)

Role: `lemma` | Type: `lemma` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1351`

- Proof status: `proven`
- Depends on: `definition:appC_bounded_symbolic_observer_dynamics` (Bounded Symbolic Observer Dynamics); `definition:bk6_symbolic_curvature_tensor` (Symbolic Curvature Tensor)
- Cites: `definition:bk6_symbolic_curvature_tensor` (Symbolic Curvature Tensor)
- Cited by: none
- Macros used: none

**Statement / Body**

The term $theta$ represents symbolic drift velocity, while $1/theta$ represents
the curvature penalty imposed by bounded memory. The sum $kappa(theta)$ measures
total symbolic effort required to maintain coherent exploration (cf.
Def. definition:bk6_symbolic_curvature_tensor).

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Geometric Interpretation of Curvature Terms]
\label{lemma:appC_geometric_interpretation_curvature}
The term $\theta$ represents symbolic drift velocity, while $1/\theta$ represents
the curvature penalty imposed by bounded memory. The sum $\kappa(\theta)$ measures
total symbolic effort required to maintain coherent exploration (cf.
Def.~\ref{definition:bk6_symbolic_curvature_tensor}).
\end{lemma}
```

### proof:appC_geometric_interpretation_curvature (`proof:appC_geometric_interpretation_curvature`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1359`

- Proof status: `not_applicable`
- Depends on: `definition:appC_bounded_symbolic_observer_dynamics` (Bounded Symbolic Observer Dynamics)
- Cites: `definition:appC_bounded_symbolic_observer_dynamics` (Bounded Symbolic Observer Dynamics)
- Cited by: none
- Macros used: none

**Statement / Body**

By Def. definition:appC_bounded_symbolic_observer_dynamics, $theta$ is the
forward exploration rate, so its contribution to one-step effort is linear in
$theta$ after normalization of units. The reflective term must decrease as drift
increases and increase as drift slows, because slower forward motion forces a
larger fraction of the step to be spent maintaining memory coherence. The
scale-free reciprocal $1/theta$ is the unique reciprocal penalty normalized to
be $1$ at the balanced point $theta=1$. Since the two costs are paid in the same
step and in the same normalized units, finite symbolic effort is their additive
sum $kappa(theta)=theta+1/theta$.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_geometric_interpretation_curvature}
By Def.~\ref{definition:appC_bounded_symbolic_observer_dynamics}, $\theta$ is the
forward exploration rate, so its contribution to one-step effort is linear in
$\theta$ after normalization of units. The reflective term must decrease as drift
increases and increase as drift slows, because slower forward motion forces a
larger fraction of the step to be spent maintaining memory coherence. The
scale-free reciprocal $1/\theta$ is the unique reciprocal penalty normalized to
be $1$ at the balanced point $\theta=1$. Since the two costs are paid in the same
step and in the same normalized units, finite symbolic effort is their additive
sum $\kappa(\theta)=\theta+1/\theta$.
\end{proof}
```

### Golden Ratio as Minimal Curvature Parameter (`theorem:appC_phi_minimal_curvature_parameter`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1372`

- Proof status: `proven`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The parameter $theta = varphi$ minimizes the symbolic curvature function
$kappa(theta)$ among nondegenerate recursively sustainable exploration
parameters, i.e. among $theta$ satisfying $thetage 1+1/theta$.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Golden Ratio as Minimal Curvature Parameter]
\label{theorem:appC_phi_minimal_curvature_parameter}
The parameter $\theta = \varphi$ minimizes the symbolic curvature function
$\kappa(\theta)$ among nondegenerate recursively sustainable exploration
parameters, i.e. among $\theta$ satisfying $\theta\ge 1+1/\theta$.
\end{theorem}
```

### proof:appC_phi_minimal_curvature (`proof:appC_phi_minimal_curvature`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1379`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

The recursive sustainability constraint is
\[
thetage 1+frac{1}{theta},
\]
which is equivalent, for $theta>0$, to
$theta^2-theta-1ge0$. Hence the feasible set is
$[varphi,infty)$, where $varphi=(1+sqrt5)/2$. On this interval,
\[
kappa'(theta)=1-frac{1}{theta^2}>0,
\]
because $thetagevarphi>1$. Thus $kappa$ is strictly increasing on the feasible
set and its minimum occurs at the left endpoint $theta=varphi$. The minimized
curvature is
\[
kappa(varphi)=varphi+frac1varphi=varphi+(varphi-1)=2varphi-1=sqrt5.
\]
The unconstrained point $theta=1$ is lower for $kappa$ alone, but it violates
the nondegenerate recursive sustainability constraint $thetage1+1/theta$ and
therefore represents stagnation rather than sustained symbolic exploration.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_phi_minimal_curvature}
The recursive sustainability constraint is
\[
\theta\ge 1+\frac{1}{\theta},
\]
which is equivalent, for $\theta>0$, to
$\theta^2-\theta-1\ge0$. Hence the feasible set is
$[\varphi,\infty)$, where $\varphi=(1+\sqrt5)/2$. On this interval,
\[
\kappa'(\theta)=1-\frac{1}{\theta^2}>0,
\]
because $\theta\ge\varphi>1$. Thus $\kappa$ is strictly increasing on the feasible
set and its minimum occurs at the left endpoint $\theta=\varphi$. The minimized
curvature is
\[
\kappa(\varphi)=\varphi+\frac1\varphi=\varphi+(\varphi-1)=2\varphi-1=\sqrt5.
\]
The unconstrained point $\theta=1$ is lower for $\kappa$ alone, but it violates
the nondegenerate recursive sustainability constraint $\theta\ge1+1/\theta$ and
therefore represents stagnation rather than sustained symbolic exploration.
\end{proof}
```

### Symbolic Flow Stability (`definition:appC_symbolic_flow_stability`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1402`

- Proof status: `definitional`
- Depends on: `definition:bk6_reflection_operator_complete` (Reflection Operator)
- Cites: `definition:bk6_reflection_operator_complete` (Reflection Operator)
- Cited by: `lemma:appC_stability_phi_flow` (Stability of $\varphi$-Flow)
- Macros used: none

**Statement / Body**

A symbolic flow is stable if small perturbations in the exploration parameter $theta$ decay exponentially. The stability condition requires:
\[
left| frac{d}{dtheta} left( 1 + frac{1}{theta} right) right|_{theta=varphi} < 1
\]
(cf. Def. definition:bk6_reflection_operator_complete)

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic Flow Stability]
\label{definition:appC_symbolic_flow_stability}
A symbolic flow is stable if small perturbations in the exploration parameter $\theta$ decay exponentially. The stability condition requires:
\[
\left| \frac{d}{d\theta} \left( 1 + \frac{1}{\theta} \right) \right|_{\theta=\varphi} < 1
\]
(cf. Def.~\ref{definition:bk6_reflection_operator_complete})
\end{definition}
```

### Stability of $\varphi$-Flow (`lemma:appC_stability_phi_flow`)

Role: `lemma` | Type: `lemma` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1411`

- Proof status: `proven`
- Depends on: `definition:appC_symbolic_flow_stability` (Symbolic Flow Stability)
- Cites: `definition:appC_symbolic_flow_stability` (Symbolic Flow Stability)
- Cited by: none
- Macros used: none

**Statement / Body**

The $varphi$-flow satisfies the stability condition (cf. definition:appC_symbolic_flow_stability).

**Verbatim LaTeX Body**

```latex
\begin{lemma}[Stability of $\varphi$-Flow]
\label{lemma:appC_stability_phi_flow}
The $\varphi$-flow satisfies the stability condition (cf.~\ref{definition:appC_symbolic_flow_stability}).
\end{lemma}
```

### proof:appC_stability_phi_flow (`proof:appC_stability_phi_flow`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1416`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

Let $f(theta)=1+1/theta$. Then $f'(theta)=-1/theta^2$, so
\[
|f'(varphi)|=frac{1}{varphi^2}=2-varphi<1.
\]
By the one-dimensional fixed-point stability criterion, sufficiently small
perturbations of the iteration $theta_{n+1}=f(theta_n)$ contract in a
neighborhood of $varphi$. Hence the $varphi$-flow satisfies the stated stability
condition.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_stability_phi_flow}
Let $f(\theta)=1+1/\theta$. Then $f'(\theta)=-1/\theta^2$, so
\[
|f'(\varphi)|=\frac{1}{\varphi^2}=2-\varphi<1.
\]
By the one-dimensional fixed-point stability criterion, sufficiently small
perturbations of the iteration $\theta_{n+1}=f(\theta_n)$ contract in a
neighborhood of $\varphi$. Hence the $\varphi$-flow satisfies the stated stability
condition.
\end{proof}
```

### Unified Recursive Fixed Point (`theorem:appC_unified_recursive_fixed_point`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1431`

- Proof status: `proven`
- Depends on: `lemma:appC_matrix_representation_symbolic_operators` (Matrix Representation of Symbolic Operators)
- Cites: `lemma:appC_matrix_representation_symbolic_operators` (Matrix Representation of Symbolic Operators)
- Cited by: `remark:appC_connection_other_modalities` (Connection to Other Symbolic Modalities)
- Macros used: none

**Statement / Body**

Both the matrix eigenvalue approach (cf. lemma:appC_matrix_representation_symbolic_operators) and the topological curvature approach converge to the same fixed-point equation:
\[
lambda = 1 + frac{1}{lambda} Rightarrow lambda^2 - lambda - 1 = 0 Rightarrow lambda = varphi
\]
for the unique positive nondegenerate fixed point.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Unified Recursive Fixed Point]
\label{theorem:appC_unified_recursive_fixed_point}
Both the matrix eigenvalue approach (cf.~\ref{lemma:appC_matrix_representation_symbolic_operators}) and the topological curvature approach converge to the same fixed-point equation:
\[
\lambda = 1 + \frac{1}{\lambda} \Rightarrow \lambda^2 - \lambda - 1 = 0 \Rightarrow \lambda = \varphi
\]
for the unique positive nondegenerate fixed point.
\end{theorem}
```

### proof:appC_unified_recursive_fixed_point (`proof:appC_unified_recursive_fixed_point`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1440`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

In the matrix approach, the minimal memory-preserving recurrence is
$C_{n+1}=C_n+C_{n-1}$. If the positive asymptotic ratio
$lambda=lim C_{n+1}/C_n$ exists, division by $C_n$ and passage to the limit give
\[
lambda=1+frac{1}{lambda}.
\]
In the topological approach, recursive sustainable exploration requires that the
forward parameter equal one unit of new exploration plus the reciprocal
reflective correction, so its fixed point satisfies the same equation
$theta=1+1/theta$. In both cases the positive solution of
$x^2-x-1=0$ is $x=varphi$, while the other solution is negative and therefore
inadmissible as a growth or curvature parameter.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_unified_recursive_fixed_point}
In the matrix approach, the minimal memory-preserving recurrence is
$C_{n+1}=C_n+C_{n-1}$. If the positive asymptotic ratio
$\lambda=\lim C_{n+1}/C_n$ exists, division by $C_n$ and passage to the limit give
\[
\lambda=1+\frac{1}{\lambda}.
\]
In the topological approach, recursive sustainable exploration requires that the
forward parameter equal one unit of new exploration plus the reciprocal
reflective correction, so its fixed point satisfies the same equation
$\theta=1+1/\theta$. In both cases the positive solution of
$x^2-x-1=0$ is $x=\varphi$, while the other solution is negative and therefore
inadmissible as a growth or curvature parameter.
\end{proof}
```

### Structural Universality of $\varphi$ (`scholium:appC_structural_universality_phi`)

Role: `scholium` | Type: `scholium` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1456`

- Proof status: `not_applicable`
- Depends on: `definition:bk6_symbolic_curvature_tensor` (Symbolic Curvature Tensor); `theorem:bk6_symbolic_diffusion_governs_evolution` (Symbolic Diffusion Operator Governs Thermodynamic Evolution)
- Cites: `definition:bk6_symbolic_curvature_tensor` (Symbolic Curvature Tensor); `theorem:bk6_symbolic_diffusion_governs_evolution` (Symbolic Diffusion Operator Governs Thermodynamic Evolution)
- Cited by: none
- Macros used: none

**Statement / Body**

The independent emergence of $varphi$ from matrix spectral theory and topological curvature analysis suggests that $varphi$ represents a fundamental structural constant of bounded recursive systems. This convergence transcends particular mathematical representations, indicating an intrinsic property of symbolic emergence under resource constraints (see Def. definition:bk6_symbolic_curvature_tensor, Thm. theorem:bk6_symbolic_diffusion_governs_evolution).

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Structural Universality of $\varphi$]
\label{scholium:appC_structural_universality_phi}
The independent emergence of $\varphi$ from matrix spectral theory and topological curvature analysis suggests that $\varphi$ represents a fundamental structural constant of bounded recursive systems. This convergence transcends particular mathematical representations, indicating an intrinsic property of symbolic emergence under resource constraints (see Def.~\ref{definition:bk6_symbolic_curvature_tensor}, Thm.~\ref{theorem:bk6_symbolic_diffusion_governs_evolution}).
\end{scholium}
```

### Connection to Other Symbolic Modalities (`remark:appC_connection_other_modalities`)

Role: `remark` | Type: `remark` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1461`

- Proof status: `not_applicable`
- Depends on: `theorem:appC_unified_recursive_fixed_point` (Unified Recursive Fixed Point)
- Cites: `theorem:appC_unified_recursive_fixed_point` (Unified Recursive Fixed Point)
- Cited by: none
- Macros used: none

**Statement / Body**

The fixed-point equation $lambda = 1 + 1/lambda$ (cf. theorem:appC_unified_recursive_fixed_point) appears in multiple contexts within symbolic dynamics. The consistent emergence of $varphi$ across matrix, topological, and (potentially) thermodynamic or spectral approaches is not a coincidence to be noted but a transfer to be proved: the Modal Transference Theorem below states the conditions under which an ordinal-recursive invariant such as $varphi$ is carried, intact, from one observer-accessible carrier to another.

**Verbatim LaTeX Body**

```latex
\begin{remark}[Connection to Other Symbolic Modalities]
\label{remark:appC_connection_other_modalities}
The fixed-point equation $\lambda = 1 + 1/\lambda$ (cf.~\ref{theorem:appC_unified_recursive_fixed_point}) appears in multiple contexts within symbolic dynamics. The consistent emergence of $\varphi$ across matrix, topological, and (potentially) thermodynamic or spectral approaches is not a coincidence to be noted but a transfer to be proved: the Modal Transference Theorem below states the conditions under which an ordinal-recursive invariant such as $\varphi$ is carried, intact, from one observer-accessible carrier to another.
\end{remark}
```

### Modal Transference of Symbolic Invariants (`sec:appC_modal_transference`)

Role: `section` | Type: `section` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1466`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: none

**Statement / Body**

(no body text extracted)

### Symbolic modality (`definition:appC_symbolic_modality`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1483`

- Proof status: `definitional`
- Depends on: `definition:bk1_stage_composite_operator` (Stage–Composite Operator)
- Cites: `definition:bk1_stage_composite_operator` (Stage–Composite Operator)
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

A symbolic modality is a tuple
\[
mathfrak{M} = (X_mathfrak{M},\ preceq_mathfrak{M},\ d_{Obs,mathfrak{M}},\
E_mathfrak{M},\ I_mathfrak{M}),
\]
where $X_mathfrak{M}$ is a space of modal presentations, $preceq_mathfrak{M}$
is an observer-resolved emergence order, $d_{Obs,mathfrak{M}}$ is the
observer-relative modal distance, $E_mathfrak{M}$ is the stage-composite
emergence operator (cf. Def. definition:bk1_stage_composite_operator) in
the modality, and $I_mathfrak{M}$ is a family of structural invariants
(cyclic order, adjacency, recurrence spectrum, proportion, curvature signature).

**Verbatim LaTeX Body**

```latex
\begin{definition}[Symbolic modality]
\label{definition:appC_symbolic_modality}
A \emph{symbolic modality} is a tuple
\[
\mathfrak{M} = (X_\mathfrak{M},\ \preceq_\mathfrak{M},\ d_{\Obs,\mathfrak{M}},\
E_\mathfrak{M},\ \mathcal{I}_\mathfrak{M}),
\]
where $X_\mathfrak{M}$ is a space of modal presentations, $\preceq_\mathfrak{M}$
is an observer-resolved emergence order, $d_{\Obs,\mathfrak{M}}$ is the
observer-relative modal distance, $E_\mathfrak{M}$ is the stage-composite
emergence operator (cf.~Def.~\ref{definition:bk1_stage_composite_operator}) in
the modality, and $\mathcal{I}_\mathfrak{M}$ is a family of structural invariants
(cyclic order, adjacency, recurrence spectrum, proportion, curvature signature).
\end{definition}
```

### Modal transference map (`definition:appC_modal_transference_map`)

Role: `definition` | Type: `definition` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1498`

- Proof status: `definitional`
- Depends on: none
- Cites: none
- Cited by: `corollary:bk4_chromatic_transference_of_wheel` (Chromatic transference of the wheel); `proof:bk4_chromatic_transference_of_wheel`; `scholium:appC_transference_tests` (Sonification and the Chromatic Wheel as Transference Tests)
- Macros used: `\Obs`

**Statement / Body**

Let $mathfrak{M}_A,mathfrak{M}_B$ be symbolic modalities. A modal
transference map is an observer-bounded map
$T_{Ato B}:X_{mathfrak{M}_A}to X_{mathfrak{M}_B}$ satisfying:

- Ordinal preservation:
$xpreceq_{mathfrak{M}_A}y Rightarrow T_{Ato B}(x)preceq_{mathfrak{M}_B}T_{Ato B}(y)$.

- Observer-bounded distortion: there exist $L<infty$ and
$varepsilon_Obsge 0$ with
\[
d_{Obs,mathfrak{M}_B}\!big(T_{Ato B}x, T_{Ato B}ybig)
le L d_{Obs,mathfrak{M}_A}(x,y) + varepsilon_Obs.
\]

- Operator semi-conjugacy:
$T_{Ato B}circ E_{mathfrak{M}_A} sim_Obs E_{mathfrak{M}_B}circ T_{Ato B}$,
equality holding up to observer resolution $varepsilon_Obs$.

- Invariant preservation: for each $IinI_{mathfrak{M}_A}$
transferred by $T_{Ato B}$ there is $T_*IinI_{mathfrak{M}_B}$ with
$I(x)=T_*I(T_{Ato B}x)$ up to $varepsilon_Obs$.

**Verbatim LaTeX Body**

```latex
\begin{definition}[Modal transference map]
\label{definition:appC_modal_transference_map}
Let $\mathfrak{M}_A,\mathfrak{M}_B$ be symbolic modalities. A \emph{modal
transference map} is an observer-bounded map
$T_{A\to B}:X_{\mathfrak{M}_A}\to X_{\mathfrak{M}_B}$ satisfying:
\begin{enumerate}
\item \emph{Ordinal preservation:}
$x\preceq_{\mathfrak{M}_A}y \Rightarrow T_{A\to B}(x)\preceq_{\mathfrak{M}_B}T_{A\to B}(y)$.
\item \emph{Observer-bounded distortion:} there exist $L<\infty$ and
$\varepsilon_\Obs\ge 0$ with
\[
d_{\Obs,\mathfrak{M}_B}\!\big(T_{A\to B}x,\,T_{A\to B}y\big)
\le L\, d_{\Obs,\mathfrak{M}_A}(x,y) + \varepsilon_\Obs.
\]
\item \emph{Operator semi-conjugacy:}
$T_{A\to B}\circ E_{\mathfrak{M}_A} \sim_\Obs E_{\mathfrak{M}_B}\circ T_{A\to B}$,
equality holding up to observer resolution $\varepsilon_\Obs$.
\item \emph{Invariant preservation:} for each $I\in\mathcal{I}_{\mathfrak{M}_A}$
transferred by $T_{A\to B}$ there is $T_*I\in\mathcal{I}_{\mathfrak{M}_B}$ with
$I(x)=T_*I(T_{A\to B}x)$ up to $\varepsilon_\Obs$.
\end{enumerate}
\end{definition}
```

### Modal Transference (`theorem:appC_modal_transference`)

Role: `theorem` | Type: `theorem` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1521`

- Proof status: `proven`
- Depends on: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure)
- Cites: `definition:bk5_balanced_two_step_memory_closure` (Balanced Two-Step Symbolic Memory Closure)
- Cited by: `corollary:bk4_chromatic_transference_of_wheel` (Chromatic transference of the wheel); `proof:bk4_chromatic_transference_of_wheel`; `scholium:appC_two_modalities_one_root` (Two Modalities, One Root)
- Macros used: none

**Statement / Body**

Let $T_{Ato B}$ be a modal transference map between symbolic modalities
$mathfrak{M}_A$ and $mathfrak{M}_B$. Then any invariant determined only by
ordinal order, operator recurrence, cyclic adjacency, or spectral proportion is
preserved across the transfer up to observer resolution. In particular, if a
recurrence invariant $lambda$ is fixed in $mathfrak{M}_A$ by the balanced
two-step closure $a_{n+1}=a_n+a_{n-1}$
(cf. book V, Def. definition:bk5_balanced_two_step_memory_closure), then its
transferred presentation in $mathfrak{M}_B$ carries the same positive spectral
invariant $lambda=varphi$.

**Verbatim LaTeX Body**

```latex
\begin{theorem}[Modal Transference]
\label{theorem:appC_modal_transference}
Let $T_{A\to B}$ be a modal transference map between symbolic modalities
$\mathfrak{M}_A$ and $\mathfrak{M}_B$. Then any invariant determined only by
ordinal order, operator recurrence, cyclic adjacency, or spectral proportion is
preserved across the transfer up to observer resolution. In particular, if a
recurrence invariant $\lambda$ is fixed in $\mathfrak{M}_A$ by the balanced
two-step closure $a_{n+1}=a_n+a_{n-1}$
(cf.~book V, Def.~\ref{definition:bk5_balanced_two_step_memory_closure}), then its
transferred presentation in $\mathfrak{M}_B$ carries the same positive spectral
invariant $\lambda=\varphi$.
\end{theorem}
```

### proof:appC_modal_transference (`proof:appC_modal_transference`)

Role: `proof` | Type: `proof` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1534`

- Proof status: `not_applicable`
- Depends on: none
- Cites: none
- Cited by: none
- Macros used: `\Obs`

**Statement / Body**

By ordinal preservation, $T_{Ato B}$ preserves the emergence order of the source
modality; by observer-bounded distortion, differences below the observer
threshold in $mathfrak{M}_A$ remain below threshold in $mathfrak{M}_B$. By
operator semi-conjugacy the transferred system follows the same emergence
dynamics up to resolution: $T_{Ato B}circ E_{mathfrak{M}_A} sim_Obs
E_{mathfrak{M}_B}circ T_{Ato B}$. An invariant fixed solely by the recurrence
or adjacency structure of $E_{mathfrak{M}_A}$ cannot change when $E_{mathfrak{M}_A}$
is replaced by its semi-conjugate presentation $E_{mathfrak{M}_B}$ except below
threshold. For the balanced two-step closure the companion matrix is
$A=big(1&1\\1&0big)$, with characteristic
equation $lambda^2-lambda-1=0$ and positive root $varphi$. Since transference
preserves the recurrence structure, the same spectral invariant appears in the
target modality. Hence $varphi$ is not tied to a sensory carrier; it is an
ordinal-recursive invariant transferred through modal presentation.

**Verbatim LaTeX Body**

```latex
\begin{proof}
\label{proof:appC_modal_transference}
By ordinal preservation, $T_{A\to B}$ preserves the emergence order of the source
modality; by observer-bounded distortion, differences below the observer
threshold in $\mathfrak{M}_A$ remain below threshold in $\mathfrak{M}_B$. By
operator semi-conjugacy the transferred system follows the same emergence
dynamics up to resolution: $T_{A\to B}\circ E_{\mathfrak{M}_A} \sim_\Obs
E_{\mathfrak{M}_B}\circ T_{A\to B}$. An invariant fixed solely by the recurrence
or adjacency structure of $E_{\mathfrak{M}_A}$ cannot change when $E_{\mathfrak{M}_A}$
is replaced by its semi-conjugate presentation $E_{\mathfrak{M}_B}$ except below
threshold. For the balanced two-step closure the companion matrix is
$A=\big(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\big)$, with characteristic
equation $\lambda^2-\lambda-1=0$ and positive root $\varphi$. Since transference
preserves the recurrence structure, the same spectral invariant appears in the
target modality. Hence $\varphi$ is not tied to a sensory carrier; it is an
ordinal-recursive invariant transferred through modal presentation.
\end{proof}
```

### Sonification and the Chromatic Wheel as Transference Tests (`scholium:appC_transference_tests`)

Role: `scholium` | Type: `scholium` | Book: `appendix_dual_horizon` | Source: `appendix_dual_horizon.tex:1552`

- Proof status: `not_applicable`
- Depends on: `definition:appC_modal_transference_map` (Modal transference map)
- Cites: `definition:appC_modal_transference_map` (Modal transference map)
- Cited by: none
- Macros used: none

**Statement / Body**

The sonification and chromatic-wheel constructions are not offered as analogies.
They are modal transference tests. Each asks whether an invariant first defined
in ordinal-symbolic form survives transfer into a distinct observer-accessible
carrier. Sonification is the transference map
$T_{symbolictoaudio}$ carrying symbolic order into pitch,
interval, rhythm, and phase; the Newtonian color wheel is the map
$T_{symbolictochromatic}$ carrying cyclic adjacency,
opposition, and return into visual structure. When cyclic order, recurrence
spectrum, and bounded adjacency are preserved under
Def. definition:appC_modal_transference_map, the invariant belongs to the
symbolic structure rather than to the particular sensory modality. This is the
precise sense in which domains are modal presentations of shared ordinal-symbolic
invariants-not the claim that everything is the same substance, but the claim
that distinct modalities preserve the same emergence grammar when the
transference map respects ordinal order, observer bounds, and operator recurrence.

**Verbatim LaTeX Body**

```latex
\begin{scholium}[Sonification and the Chromatic Wheel as Transference Tests]
\label{scholium:appC_transference_tests}
The sonification and chromatic-wheel constructions are not offered as analogies.
They are modal transference tests. Each asks whether an invariant first defined
in ordinal-symbolic form survives transfer into a distinct observer-accessible
carrier. Sonification is the transference map
$T_{\mathrm{symbolic}\to\mathrm{audio}}$ carrying symbolic order into pitch,
interval, rhythm, and phase; the Newtonian color wheel is the map
$T_{\mathrm{symbolic}\to\mathrm{chromatic}}$ carrying cyclic adjacency,
opposition, and return into visual structure. When cyclic order, recurrence
spectrum, and bounded adjacency are preserved under
Def.~\ref{definition:appC_modal_transference_map}, the invariant belongs to the
symbolic structure rather than to the particular sensory modality. This is the
precise sense in which domains are modal presentations of shared ordinal-symbolic
invariants---not the claim that everything is the same substance, but the claim
that distinct modalities preserve the same emergence grammar when the
transference map respects ordinal order, observer bounds, and operator recurrence.
\end{scholium}
```
