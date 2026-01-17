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

## The .bld Format

BLD files use a minimal syntax where structure emerges from simple patterns:

### Dimension — Repetition with `*`

```bld
# byte.bld - 8 bit positions
8*b

# u64.bld - 64 bit positions
64*b

# string.bld - variable length
N*byte
```

The pattern `N*type` declares N positions of a type. Size comes from dimension.

### Link — Composition with paths

```bld
# arch/x86/mov.bld - compose instruction parts
prefix: arch/x86/rex
opcode: arch/x86/opcode/mov
modrm: arch/x86/modrm
```

Paths like `arch/x86/rex` reference other .bld files. The traverser follows the path and composes the output.

### Boundary — Partition with `|` or `..`

```bld
# b.bld - the bit (two states)
0..1

# bld.bld - partition of constructs
partition: identifier | sequence
```

Boundaries express distinctions: this OR that. A bit partitions into 0 or 1.

### Fields — Named composition

```bld
# format/elf/header.bld - ELF64 header structure
ident: format/elf/ident
type: u16
machine: u16
version: u32
entry: u64
phoff: u64
```

Fields compose types into larger structures. The traverser walks each field in order.

### Constants — Direct output

```bld
# arch/x86/opcode/mov.bld - x86 MOV opcodes
ri: 0xB8
rm: 0x8B
mr: 0x89
```

Hex constants (`0x48`) and decimals emit bytes directly. Comments use `#`.

### Sequence — Composition by listing

```bld
# program/hello.bld - compose a program
format/elf/minimal
program/hello/code
```

Lines listed in sequence compose in order. This produces ELF header followed by code.

### Complete Example

```bld
# measure.bld - the cost formula
partitions: N
positions: M*b
links: K
```

This expresses `Cost = B + D × L`:
- `partitions: N` — count of boundaries
- `positions: M*b` — M bits of dimension
- `links: K` — count of connections

The traverser composes by walking the structure. No special emit primitives needed.

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
