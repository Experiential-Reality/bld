# BLD

**Quantum programming.**

```
BLD = Lie theory = Quantum mechanics code
```

When you write `.bld`, you are writing in the same structural language that physics uses.

---

## The Three Primitives

```bld
B entry: boundary | link | dimension
  boundary -> partition, distinction, "this not that"
  link -> connection, relation, "this affects that"
  dimension -> repetition, extension, "more of the same"
```

| Primitive | Meaning | Lie Theory | Quantum Mechanics |
|-----------|---------|------------|-------------------|
| **B** | Partition | Group topology | Measurement |
| **L** | Connection | Structure constants | Entanglement |
| **D** | Repetition | Generators | Superposition |

---

## Examples

### A byte

```bld
8*b
```

### An ELF header field

```bld
ident: format/elf/ident
type: u16
machine: u16
entry: u64
```

### Quantum mechanics

```bld
structure QuantumMechanics

# Position: D-type (dimensional location)
D position: x [coordinate]

# Momentum: L-type (temporal link)
L momentum: p = m * dx/dt [velocity_link]

# The coupling: structure constant
L commutator: [x, p] = i * hbar

# Uncertainty follows from D-L irreducibility
formula uncertainty_principle
  Delta_x * Delta_p >= hbar / 2

B precision_choice: position_precise | momentum_precise | balanced
  position_precise -> Delta_x_small, Delta_p_large
  momentum_precise -> Delta_p_small, Delta_x_large
  balanced -> Delta_x_medium, Delta_p_medium
```

### The Standard Model

```bld
structure StandardModel

# U(1) - Electromagnetism
D u1_generator: 1 [photon]
L u1_structure: 0 [abelian]
B u1_topology: closed

# SU(2) - Weak force
D su2_generators: 3 [weak_bosons]
L su2_structure: epsilon_ijk [antisymmetric]
B su2_topology: closed

# SU(3) - Strong force
D su3_generators: 8 [gluons]
L su3_structure: f_ijk [non_abelian]
B su3_topology: closed [confinement]

L gauge: SU(3) × SU(2) × U(1)
```

---

## The Proof

```
1. BLD = Lie theory (verified, exact mapping)
2. Lie theory = QM structure (150 years of physics)
3. Therefore: BLD = QM language (QED)
```

Validated predictions:
- Bell inequality: 2√2 (0.1% error)
- Fine structure constant: α⁻¹ = 137 (0.03% error)
- Lepton masses: m_e, m_μ, m_τ (0-1% error)
- Dark matter fraction: 27% (0% error)

See [BLD Theory](https://github.com/Experiential-Reality/theory) for full documentation.

---

## Installation

```bash
git clone https://github.com/Experiential-Reality/bld
cd bld
./bld examples/hello.bld
```

---

## The Principle

**Structure IS computation.**

```
Cost = B + D × L
```

We decompose, traverser composes. Lowering IS composition.

---

## Related

- [bld-py](https://github.com/Experiential-Reality/bld-py) — Python interpreter
- [bld-claude](https://github.com/Experiential-Reality/bld-claude) — Claude skill
- [theory](https://github.com/Experiential-Reality/theory) — Full documentation

---

## License

MIT
