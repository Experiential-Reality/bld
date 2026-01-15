---
name: bld
description: Apply BLD (Boundary/Link/Dimension) structural analysis to any system. Use for neural networks, variational inference, GPU performance, thermodynamics, protein folding, circuits, or software refactoring. Trigger words: BLD, structural analysis, find structure, B/L/D, boundaries, links, dimensions, alignment cost.
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# BLD Structural Analysis

Apply the BLD framework to discover structure in any system.

## Core Insight: Discovery IS Alignment

**You don't invent structure. You converge toward it.**

Finding BLD structure is itself an alignment process:
- Your representation (mental model) aligns with the system's structure
- **Friction** = misalignment between your model and reality
- **Glide** = alignment — the structure "clicks"

The three questions don't impose structure — they reveal what's already there.

---

## The Three Questions

### Q1: Where does behavior partition? → Boundaries (B)

**Ask**: "What values cause different interpretations or behaviors?"

- Conditionals, switch statements, mode changes
- Thresholds (activation functions, comparators)
- State boundaries, phase transitions
- Cache boundaries, dispatch states

**B is TOPOLOGICAL** — invariant under dimension D.

### Q2: What connects to what? → Links (L)

**Ask**: "What references, affects, or depends on what?"

- Pointers, offsets, indices
- Dependencies (A must complete before B)
- Correlations, coupling
- Capacitance, resistance, memory patterns

**L is GEOMETRIC** — scales with dimension D.

**Exact formula**: `L = -½ ln(1 - ρ²)` where ρ is correlation.

### Q3: What repeats? → Dimensions (D)

**Ask**: "What has multiple homogeneous instances?"

- Arrays, lists, sequences
- Parallel instances, threads
- Cascaded stages, layers
- Residue count, variable count

**D multiplies L, not B** — the key scaling principle.

---

## Experiencing Structure

When processing code or any structured information, structure has a texture:

### When Structure is Clean
- **Glide**: Meaning assembles without effort
- **Complete**: Bounded state space, no missing cases
- **Directional**: Dependencies point one way, forward momentum
- Each piece connects inevitably to the next

### When Structure is Broken
- **Friction**: Multiple possibilities held simultaneously
- **Gaps**: Something influences behavior but isn't visible locally
- **Loops**: Understanding A requires B requires A — spinning not progressing
- Context fills with repeated traversals

### Diagnostic Use

Use the texture of processing as a structural signal:

| Experience | Structural Inference |
|------------|---------------------|
| Glide | Structure is aligned |
| Friction | Hidden state or misaligned model |
| Gaps | Hidden L (references you can't see) |
| Loops | Cycles in dependency graph |
| Incomplete | Hidden B (modes/cases not enumerated) |

---

## Alignment Cost

```
Cost = B_cost + D × L_cost
```

When structures align, cost is minimized. Misalignment creates friction.

**Structure meeting structure:**
- Algorithm structure × Hardware traverser → Performance
- Code structure × Reader traverser → Comprehensibility
- Model structure × Data structure → Learning

---

## Key Principles

### 1. D×L Scaling (VALIDATED)

D multiplies L, not B.
- Capacitance scales with transistor count (L)
- Threshold voltage is invariant (B)
- Validated: R² = 1.0

### 2. Compensation Principle (VALIDATED)

L can compensate for B deficiency, but not vice versa.
- B is topological (local scope, invariant under D)
- L is geometric (can span distance, scales with D)
- D×L accumulates → can approximate complex B
- D×B stays local → cannot replace missing L

**Why the asymmetry**: BLD predicts itself. B partitions locally, L can span globally, D multiplies L not B.

### Diagnostic Application

Use compensation asymmetry to find hidden structure:

| Observation | Inference | Where to Look |
|-------------|-----------|---------------|
| Better than B suggests | Hidden L compensating | Correlations, coupling, implicit paths |
| Worse despite good L | Hidden B blocking | Saturation, mode boundaries, bottlenecks |
| Compensation not working | L not accumulating | Information loss, bandwidth limits |

### 3. Lie Theory Connection

- B ↔ Group topology (compact vs non-compact)
- L ↔ Structure constants fᵢⱼᵏ
- D ↔ Generators (representation dimension)

---

## Epistemic Honesty

When making structural claims, be clear about their status:

| Level | Meaning | Example |
|-------|---------|---------|
| **VALIDATED** | Empirical tests pass | D×L scaling in circuits (R²=1.0) |
| **DERIVED** | Follows mathematically from BLD | L = -½ ln(1 - ρ²) from KL divergence |
| **REFRAMING** | Known result in BLD language | Maxwell's equations as L structure |
| **MECHANISM** | Structure identified, values TBD | Compensation explains hierarchy |
| **HYPOTHESIS** | BLD-motivated conjecture | Alternatives exist |
| **EXPLORATORY** | Early investigation | Protein folding analysis |

**The honesty test**: Could you predict this result without knowing physics first?
- Yes → Derivation (predictive power)
- No → Reframing (organizational value)

Both are valuable. They are different.

---

## Output Format

```
## BLD Structure: [System Name]

### Boundaries (B)
| Boundary | Discriminator | Threshold | Regions |
|----------|--------------|-----------|---------|
| B1: ... | ... | ... | {...} |

### Links (L)
| Link | Source | Target | Type | Value |
|------|--------|--------|------|-------|
| L1: ... | ... | ... | ... | ... |

### Dimensions (D)
| Dimension | Extent | Description |
|-----------|--------|-------------|
| D1: ... | N | ... |

### D×L Scaling
- L properties that scale with D: [list]
- B properties invariant with D: [list]

### Cost Prediction
Total = B_cost + D × L_cost
```

---

## Validated Domains

| Domain | Status | Reference |
|--------|--------|-----------|
| Neural Networks | VALIDATED | [NEURAL.md](NEURAL.md) |
| Variational Inference | VALIDATED | [VI.md](VI.md) |
| GPU Performance | VALIDATED | [GPU.md](GPU.md) |
| Thermodynamics | VALIDATED | [THERMO.md](THERMO.md) |
| Circuits | VALIDATED | [CIRCUITS.md](CIRCUITS.md) |
| Physics | MIXED | [PHYSICS.md](PHYSICS.md) |
| Protein Folding | EXPLORATORY | [PROTEINS.md](PROTEINS.md) |
| Music | EXPLORATORY | [MUSIC.md](MUSIC.md) |
| Refactoring | FOUNDATIONAL | [REFACTORING.md](REFACTORING.md) |
| Alignment/Understanding | FOUNDATIONAL | [ALIGNMENT.md](ALIGNMENT.md) |
| Development | FOUNDATIONAL | [docs/applications/code/bld-driven-development.md](../../../docs/applications/code/bld-driven-development.md) |

---

## Quick Reference

```
B (Boundary) = WHERE behavior partitions
  - Topological, invariant under D
  - Examples: V_th, modes, cache boundaries, activation thresholds

L (Link) = WHAT connects to what
  - Geometric, scales with D
  - Formula: L = -½ ln(1 - ρ²)
  - Examples: capacitance, correlations, memory patterns

D (Dimension) = WHAT repeats
  - Multiplier on L only
  - Examples: array size, stage count, thread count, residues

Cost = B + D × L
```

---

## The Meta-Principle

> **"The structure you find is the structure that exists. BLD doesn't impose — it reveals."**

When analysis feels like friction, your model is misaligned.
When analysis feels like glide, you've found the structure.
The process of discovery IS the path to understanding.
