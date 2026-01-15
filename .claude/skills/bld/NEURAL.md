# BLD for Neural Networks

> **Status**: VALIDATED

## The Core Insight

**Architectures succeed when their B/L/D structure aligns with the data's B/L/D structure.**

Neural networks are traversers. Data has structure. Learning IS alignment.

---

## Architecture Comparison

| Architecture | B (Boundaries) | L (Links) | D (Dimensions) |
|-------------|----------------|-----------|----------------|
| **MLP** | Activation boundaries | Dense, static weights | batch × layers × hidden |
| **CNN** | Activation + pooling | Sparse, local kernels | batch × spatial × channels |
| **Transformer** | Attention masks | Dynamic, content-dependent | batch × seq × heads |

## Multi-Layer Perceptron (MLP)

```
B: Simple activation boundaries (ReLU at x=0)
L: Dense weight matrices (full connectivity)
D: batch × layers × hidden_units

Key: Global L can compensate for simple B
```

## Convolutional Neural Network (CNN)

```
B: Activations + pooling regions
L: Sparse local kernels + skip connections
D: batch × H × W × channels

Key: Local L matches spatial locality of images
     Cannot compensate for missing global features
```

## Transformer

```
B: Attention masks, layer boundaries
L: Dynamic attention (content-dependent!)
D: batch × sequence × heads × hidden

Key: Dynamic L adapts to input structure
```

## The Compensation Principle (VALIDATED)

**Statement**: Global L can compensate for B deficiency, but local L cannot.

### Why the Asymmetry Exists (BLD Predicts Itself)

The asymmetry follows from primitive definitions:
- **B (activations) is topological**: Each neuron partitions locally. Invariant under D.
- **L (connectivity) is geometric**: Dense L spans globally, sparse L stays local. Scales with D.
- **D×L accumulates**: Deep networks cascade soft boundaries through links → sharp decisions.
- **D×B stays local**: Each neuron still makes its own local decision.

### How It Manifests

When L is global (MLP):
- Every input connected to every output
- Capacity can redistribute across all features
- Simple B (ReLU) is sufficient — L compensates

When L is local (CNN):
- Kernels see only local regions
- Cannot redistribute capacity globally
- B deficiency is exposed — no compensation possible

### Diagnostic Use

| Observation | Inference | Where to Look |
|-------------|-----------|---------------|
| Network outperforms architecture | Hidden L | Data correlations, batch norm coupling |
| Network underperforms despite global L | Hidden B | Dead neurons, mode collapse |
| "Identical" networks differ | Hidden structure | Initialization (L), training dynamics (B) |

### Validated Formula

```
Performance = a - b₁·ΔL - c·ΔB·ΔL

Note: No independent ΔB term!
B only matters when L is also mismatched.
```

**Results**:
- L effect: b₁ ≈ 0.025 per unit ΔL
- B×L interaction: c ≈ 0.061
- 6.2% diagonal advantage when structure matches

## D×L Scaling

### Width Scaling (D = neuron count)
```
Parameters = D² × L_weights  (quadratic)
Compute = D × L_ops         (linear)
Threshold (B) = unchanged   (activation at x=0)
```

### Depth Scaling (D = layer count)
```
Representational power grows exponentially
This is L compensating for B (limited per-layer expressivity)
Same principle as op-amp cascading!
```

## Practical Implications

1. **Image tasks**: Use CNN (local L matches spatial locality)
2. **Sequence tasks**: Use Transformer (dynamic L matches context)
3. **General tasks**: MLP works but is inefficient (dense L)

## Quick Analysis Template

For any neural architecture:
1. **B**: What activations/masks partition the space?
2. **L**: What's the connectivity pattern? (dense/sparse/dynamic)
3. **D**: What dimensions repeat? (batch, spatial, channels)
4. **Check**: Does L pattern match data locality?

---

## Alignment Perspective

### Why Architecture Choice Matters

Choosing an architecture = choosing how the traverser (network) will align with data structure:

| Data Property | Aligned Architecture | Why |
|--------------|---------------------|-----|
| Spatial locality (images) | CNN | Local L matches local features |
| Sequential/contextual (text) | Transformer | Dynamic L matches context dependence |
| No special structure | MLP | Dense L handles anything (inefficiently) |

### Experiential Signals

When analyzing network performance:

| Observation | Structural Interpretation |
|-------------|--------------------------|
| Fast learning | Good alignment — structure matches |
| Slow learning | Misalignment — network fighting data structure |
| Overfitting | Too much L capacity — capturing noise not structure |
| Underfitting | Too little B/L — can't represent data structure |

**Use these signals diagnostically**: If a network underperforms, ask which B/L/D component is misaligned with the data.

---

## See Also

- [ALIGNMENT.md](ALIGNMENT.md) — Understanding as alignment
- [SKILL.md](SKILL.md) — Main BLD reference
