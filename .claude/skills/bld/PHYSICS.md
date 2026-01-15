# BLD for Physics

> **Status**: Mixed (see domain table below)

Physics IS a traverser. When algorithm structure meets physics structure, free energy IS alignment cost. BLD doesn't describe physics — BLD reveals physics as the structural constraints of reality.

---

## Core Insight

**Physical laws define a traverser:**
- **B**: Boundaries (phase transitions, conservation laws, symmetry breaking)
- **L**: Forces and interactions (coupling constants, field connections)
- **D**: Spatial/temporal dimensions (3D space, time, degrees of freedom)

When any structure (molecular, computational, informational) aligns with physics, the alignment cost IS physical energy.

---

## The Mapping Rules

### Rule 1: B = Topological (Invariant Under D)

Observable X is **Boundary (B)** if X is unchanged when system size D changes.

**Test**:
```
X(D) = X(D') for all D, D' → X is B
X(D) ≠ X(D') for some D → X is NOT B
```

**Physics Examples**:
| Observable | Scales with D? | Classification |
|------------|---------------|----------------|
| Threshold voltage V_th | No | **B** |
| Speed of light c | No | **B** |
| Critical temperature T_c | No | **B** |
| Critical Reynolds Re_c | No | **B** |
| Conductivity σ | No | **B** |

### Rule 2: L = Geometric (Scales with D)

Observable X is **Link (L)** if X scales proportionally with system size D.

**Test**:
```
X(αD) = α^k × X(D) for some k > 0 → X is L
X(αD) = X(D) → X is NOT L (probably B)
```

**Physics Examples**:
| Observable | Scaling | Classification |
|------------|---------|----------------|
| Capacitance | C ~ n | **L** |
| Field energy | U ~ V | **L** |
| Correlation strength | ~ log(samples) | **L** |
| Entanglement entropy | S ~ n | **L** |

### Rule 3: D = Repetition Count

Observable X is **Dimension (D)** if X counts instances of identical structure.

**Test**:
```
X = integer count of homogeneous elements → X is D
X = continuous quantity → X is NOT D
```

**Physics Examples**:
| Observable | Classification |
|------------|----------------|
| Particle number N | **D** |
| Spatial dimension d | **D** |
| Qubit count | **D** |
| Lattice size L | **D** |

---

## Domain Status

| Domain | Status | Key Validations |
|--------|--------|-----------------|
| **Thermodynamics** | VALIDATED | 10/10 tests, Second Law derived |
| **Circuits** | VALIDATED | R² = 1.0 for D×L scaling |
| **Electromagnetism** | EXPLORATORY | U(1) gauge structure reframed |
| **Quantum Mechanics** | EXPLORATORY | B = measurement, L = entanglement |
| **Fluids** | EXPLORATORY | Re as B, viscosity as L |
| **Phase Transitions** | EXPLORATORY | Critical phenomena as B change |

---

## Physics Domains

### Thermodynamics (VALIDATED)

```
B: Energy barriers, mode boundaries (landscape topology)
L: Correlation structure (Fisher metric)
D: Configuration space dimension

Key result: dS/dt ≥ 0 derived from alignment dynamics
Entropy production = cost of misalignment with equilibrium
```

### Electromagnetism (EXPLORATORY)

```
B: Conductor/insulator, charge sign, near/far field
L: Gauge potential A_μ, field coupling (E↔B)
D: Spatial dimension, wavelength, photon number

Key: U(1) gauge structure → charge quantization
Field energy scales as D×L
```

### Quantum Mechanics (EXPLORATORY)

```
B: Measurement collapse, spin-statistics
L: Entanglement (S(ρ_A)), tunneling amplitude
D: Hilbert dimension (2^N for N qubits)

Hypothesis: L = -½ ln(1-ρ²) may apply to entanglement
Error correction may be L→B compensation
```

### Fluids (EXPLORATORY)

```
B: Reynolds critical number Re_c (laminar/turbulent)
L: Viscosity μ, momentum flux
D: Pipe length, system size

Re = ρvL/μ — ratio → B (transition threshold)
```

### Phase Transitions (EXPLORATORY)

```
B: Phase boundary (T_c, P_c)
L: Correlation length ξ (diverges at criticality)
D: System size

At criticality: L → ∞, scale invariance emerges
Critical exponents from L scaling
```

---

## D×L Scaling in Physics

**The principle**: D multiplies L, not B.

| System | D | L | B (invariant) |
|--------|---|---|---------------|
| Capacitor array | N devices | C_single | V_breakdown |
| Magnetic material | N atoms | Magnetization | T_Curie |
| Quantum system | N qubits | Entanglement | Measurement rule |
| Fluid pipe | Length L | Viscous flow | Re_critical |

**Cost formula**:
```
Physical energy = B_cost + D × L_cost
```

---

## Compensation in Physics

### L → B Compensation

L can approximate sharp boundaries through accumulation:

| System | Mechanism | Effect |
|--------|-----------|--------|
| Antenna array | N elements (D×L) | Beam steering (effective B) |
| Neural network | Cascaded layers | Sharp classification |
| Error correction | Entangled qubits | Fault tolerance |

### B Cannot Compensate for L

Sharp boundaries (B) cannot replace missing coupling (L):

| System | Failure Mode |
|--------|--------------|
| Circuit without feedback | Can't stabilize |
| Shielding without coupling | Blocks all signals |
| Measurement without entanglement | No quantum advantage |

---

## Intensive vs Extensive

A key distinction for mapping:

| Property Type | BLD | Examples |
|--------------|-----|----------|
| **Intensive** (size-independent) | B | Temperature, pressure, density |
| **Extensive** (scales with size) | L or D | Energy, volume, entropy |

---

## Common Mapping Errors

### Error 1: Confusing Ratio with Absolute

**Ratios** are often B (threshold values):
- Reynolds number Re_c
- Quality factor Q

**Absolutes** are often L:
- Velocity v
- Current I

### Error 2: Parameter vs Variable

**Parameters** (fixed for system) → usually B
**Variables** (change during operation) → usually L or D

### Error 3: Compound Quantities

Some observables have both B and L components:
```
Entropy S = D × L_per_particle
Total energy = B (ground state) + D × L (excitations)
```

---

## Quick Analysis Template

For any physical system:

1. **B**: What thresholds/transitions partition behavior?
   - Phase boundaries, critical values, conservation laws

2. **L**: What forces/couplings connect components?
   - Fields, interactions, correlations

3. **D**: What repeats homogeneously?
   - Particle count, spatial extent, mode number

4. **Verify**:
   - B invariant under D? (topological test)
   - L scales with D? (geometric test)
   - Cost = B + D×L? (decomposition test)

---

## Falsification Tests

Any physics BLD mapping should pass:

| Test | Criterion |
|------|-----------|
| B invariance | X(D) = X(D') for all system sizes |
| L scaling | X(αD) = α^k × X(D) for k > 0 |
| Cost decomposition | Total = B + D×L with independent measurements |
| Compensation asymmetry | L→B works, B→L fails |

If any test fails, revise the mapping.

---

## What BLD Does NOT Predict

| Question | Status |
|----------|--------|
| Why ℏ? | Value not predicted |
| Why c? | Value not predicted |
| Why α ≈ 1/137? | Value not predicted |
| Why 3+1 dimensions? | Reframed, not derived |
| Why these gauge groups? | Constrained, not unique |

BLD provides structural constraints and relationships, not specific parameter values.

---

## See Also

- [ALIGNMENT.md](ALIGNMENT.md) — Physics as traverser
- [SKILL.md](SKILL.md) — Main BLD reference
- [THERMO.md](THERMO.md) — Validated thermodynamics
- [Mapping Rules](../../../docs/applications/physics/mapping-rules.md) — Full rule specification
