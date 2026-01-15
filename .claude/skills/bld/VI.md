# BLD for Variational Inference

> **Status**: VALIDATED

Variational inference IS structural alignment: approximating a target distribution with a tractable family.

---

## Core Mappings

| BLD | VI Domain | Meaning |
|-----|-----------|---------|
| **B** | Multimodality | Mode separation in target distribution |
| **L** | Correlations | Dependencies between variables |
| **D** | Variable count | Embedding space dimensionality |

## The L Formula (PROVEN)

```
L = -½ ln(1 - ρ²)

where ρ is the correlation coefficient.
```

**Derivation**: From KL divergence between correlated Gaussians.

**Implications**:
- ρ = 0 → L = 0 (independent variables)
- ρ → 1 → L → ∞ (perfect correlation)
- L is always ≥ 0

## Key Findings (VALIDATED)

### B Scales with Structure, Not Parameters
```
B_cost depends on mode count (topology)
B_cost independent of dimension d
```

### L Scales Geometrically
```
L_cost ∝ d² (pairwise correlations)
Total L = Σᵢⱼ -½ ln(1 - ρᵢⱼ²)
```

### B×L Synergy
When both B and L are mismatched:
```
Total cost = B_cost + L_cost + synergy
Synergy = 2.0-2.5× amplification
```

## Validation Results

| Relationship | R² |
|--------------|-----|
| L vs correlation | 0.99 |
| B vs modes | 0.95 |
| D×L scaling | 0.99 |

## Practical Applications

### Mean-Field Approximation
```
Assumes: L = 0 (all correlations ignored)
Fails when: True posterior has strong correlations
Cost: Underestimates uncertainty
```

### Full Covariance
```
Captures: All pairwise L
Cost: O(d²) parameters
Use when: Correlations matter
```

### Mixture Models
```
Captures: B (multiple modes)
Cost: K × base_cost (K modes)
Use when: Target is multimodal
```

## Quick Analysis Template

For any VI problem:
1. **B**: How many modes in the target? (multimodal?)
2. **L**: How correlated are the variables? (use formula)
3. **D**: How many variables? (affects L cost)
4. **Predict**: Approximation error from B + D×L mismatch

---

## See Also

- [ALIGNMENT.md](ALIGNMENT.md) — Understanding as alignment
- [SKILL.md](SKILL.md) — Main BLD reference
