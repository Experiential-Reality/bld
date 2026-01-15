# BLD for Circuits

> **Status**: VALIDATED (6/6 tests passing)

Quick reference for applying BLD to electrical circuits.

**Repository**: [github.com/rax-V/bld-circuits](https://github.com/rax-V/bld-circuits) (6/6 validations passing)

## Circuit-Specific Mappings

| BLD | Circuit Manifestation | Examples |
|-----|----------------------|----------|
| **B** | Mode transitions | V_th (cutoff/conducting), V_dsat (linear/saturation) |
| **L** | Electrical coupling | C_gs, C_gd, R_on, signal paths |
| **D** | Repetition | Parallel transistors, cascaded stages |

## Common Circuits

### CMOS Inverter

```
B: V_th_inv ≈ VDD/2 (switching threshold)
L: C_in = C_gs + C_gd (input capacitance)
D: N parallel inverters or N-stage buffer

D×L: C_total = N × C_single
B invariant: V_th unchanged with N
```

### Current Mirror

```
B: Saturation boundary (V_ds > V_dsat)
L: Gate coupling (shared V_gs)
D: Multiple outputs

D×L: I_out_total = N × I_ref
B invariant: V_th unchanged
```

### Ring Oscillator

```
B: Switching threshold per stage
L: t_pd per stage (propagation delay)
D: N stages

D×L: Period = 2 × N × t_pd  ← THE D×L FORMULA
B invariant: Same threshold regardless of N
```

### Op-Amp (Compensation Principle)

```
B: Per-stage gain limit (~100)
L: Inter-stage coupling, Miller capacitor
D: N stages

Compensation: Total gain = A^N
  - Single stage: A = 100
  - Two stages: A² = 10,000
  - Three stages: A³ = 1,000,000

L (cascading) compensates for B (limited per-stage gain)
```

**Why the asymmetry exists (BLD predicts itself)**:
- B (V_th) is topological: partitions locally, invariant under D
- L (stages, capacitance) is geometric: connects across stages, scales with D
- D×L accumulates: cascade integrates → effective sharp boundary
- D×B stays local: each stage still makes its own local decision

**Diagnostic use**: When a circuit doesn't behave as expected:
- Better than expected → hidden L (parasitic coupling)
- Worse despite good L → hidden B (saturation, thermal)
- Cascade not improving → information loss between stages

### Flash ADC

```
B: Comparator thresholds (2^N - 1 boundaries)
L: Power per comparator, input capacitance
D: Number of comparators = 2^N - 1

D×L: Power_total = D × P_comparator
B invariant: Each threshold structure identical
```

| Bits | D | Power (µW) | Ratio |
|------|---|------------|-------|
| 2 | 3 | 270.57 | 1.00× |
| 3 | 7 | 631.35 | 2.33× |
| 4 | 15 | 1352.91 | 5.00× |

R² = 1.0 — explains why flash ADCs don't scale beyond ~6 bits.

## Validation Results (6/6 Passing)

| Test | Result | Metric |
|------|--------|--------|
| Ring Oscillator Timing | PASS | T = 2×N×t_pd |
| Current Mirror D×L | PASS | R² = 1.0 |
| Power Scaling D×L | PASS | R² = 1.0 |
| Flash ADC D×L | PASS | R² = 1.0 |
| Compensation (L→B) | PASS | 87.8% improvement |
| Boundary Invariance | PASS | CV < 1% |

Run validation:
```bash
git clone https://github.com/rax-V/bld-circuits.git
cd bld-circuits && pip install -e .
PYTHONPATH=src python experiments/run_all_validations.py
```

---

## See Also

- [ALIGNMENT.md](ALIGNMENT.md) — Understanding as alignment
- [SKILL.md](SKILL.md) — Main BLD reference
