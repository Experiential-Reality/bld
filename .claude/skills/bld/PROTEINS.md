# BLD for Protein Folding

> **Status**: Exploratory

## Core Mappings

| BLD | Sequence Structure | Physics (Traverser) |
|-----|-------------------|---------------------|
| **B** | Disorder regions, conformational switches | Hydrophobic interface, Ramachandran, steric |
| **L** | Backbone, H-bond potential, hydrophobic contacts | Collapse pathways, H-bond formation |
| **D** | Residue count, repeats | 3D space, phi/psi angles, thermal |

## The Prion Problem

**Question**: Why does the same sequence fold two different ways?

### PrPᶜ (Native State)
```
Structure: α-helix dominated
Alignment: Optimized for aqueous physics
Stability: Kinetically trapped
```

### PrPˢᶜ (Pathogenic State)
```
Structure: β-sheet dominated
Alignment: Alternative minimum
Stability: Thermodynamically lower (aggregation-prone)
```

## BLD Explanation

### Two Traversers
1. **Water physics**: Favors helix (PrPᶜ)
2. **Template (PrPˢᶜ)**: Provides different alignment landscape

### Template Conversion
```
PrPˢᶜ acts as second traverser:
- Lowers barrier between minima
- Provides alignment for β-sheet conformation
- This is why prions are "infectious"
```

## Levinthal Paradox Resolution

**Paradox**: Proteins fold in milliseconds despite astronomical conformational space.

**BLD Resolution**: Speed comes from locality of alignment.
```
Folding = gradient descent on alignment landscape
NOT exhaustive search through conformations
```

Each step follows local alignment gradient:
- Hydrophobic collapse (L: hydrophobic contacts)
- Secondary structure formation (L: H-bonds)
- Tertiary packing (B: steric boundaries)

## Key Predictions

1. **Mutations changing alignment**: Break folding
2. **Chaperones**: Additional traverser (flatten landscape)
3. **Intrinsically disordered proteins**: Equal alignment for folded/unfolded
4. **Temperature increase**: Thermal D dominates → unfolding
5. **Prion infectivity**: Template provides better alignment than water

## Practical Applications

### Stability Prediction
```
B: Count conformational switches
L: Sum contact energies (H-bonds, hydrophobic)
D: Chain length, repeat domains

Stability ∝ L_contacts - D × entropy_cost
```

### Misfolding Risk
```
High risk when:
- Multiple B minima (alternative conformations)
- Strong L between residues (aggregation-prone)
- High D (longer chains harder to fold)
```

### Drug Design
```
Target: Alter alignment landscape
Methods:
- Stabilize native B (prevent transition)
- Disrupt pathogenic L (break aggregation contacts)
- Reduce effective D (target specific domains)
```

## Quick Analysis Template

For any protein:
1. **B**: Where are conformational switches? (disorder regions, hinges)
2. **L**: What contacts exist? (H-bonds, hydrophobic, disulfide)
3. **D**: How many residues? What repeats?
4. **Predict**: Folding pathway follows alignment gradient

---

## See Also

- [ALIGNMENT.md](ALIGNMENT.md) — Understanding as alignment
- [SKILL.md](SKILL.md) — Main BLD reference
