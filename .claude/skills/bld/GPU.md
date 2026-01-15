# BLD for GPU Performance

> **Status**: VALIDATED

GPU performance is alignment between algorithm structure and hardware traverser structure.

---

## Core Mappings

| BLD | GPU Domain | Examples |
|-----|------------|----------|
| **B** | Cache/dispatch boundaries | L2 cache (4MB), cold vs warm dispatch |
| **L** | Memory access patterns | Coalesced, strided, scattered |
| **D** | Parallelism dimensions | Threads, blocks, warps |

## Memory Pattern Costs (VALIDATED)

| Pattern | ns/access | Description |
|---------|-----------|-------------|
| Coalesced | 0.028 | Sequential, aligned |
| Strided | 0.034 | Regular stride |
| Scattered | 0.112 | Random access |

## Boundary Costs

### Dispatch Overhead
```
Cold dispatch: ~2.1 ms (first kernel)
Warm dispatch: ~1.2 ms (subsequent)
```

### Cache Boundaries
```
Working set < L2: Low cost
Working set > L2: Cache pressure multiplier 1.0-3.3×
```

## Engine Overlap Model

When hardware engines run in parallel:
```
Cost = max(engine_costs), not sum()
```

**Overlap efficiency on Intel Xe**:
```
("memory", "compute"): 22% efficiency
Compute slowed 4.5× when competing with memory
```

## D×L Scaling in GEMM

```
Compute = M × N × K × 2 FLOPs
Memory = M×K + K×N + M×N elements

Both scale with D (matrix dimensions)
```

### Cache Efficiency Model
```
Efficiency = sqrt(tile_size / working_set)
Not linear! Tiled patterns follow sqrt model.
```

## Validation Results

| Size | Predicted | Actual | Error |
|------|-----------|--------|-------|
| 256² | 1.51ms | 1.33ms | -13.6% |
| 1024² | 22.85ms | 20.33ms | -12.4% |
| 4096² | 2030ms | 1759ms | -15.4% |

## Practical Applications

### Kernel Optimization
```
1. Identify B: Cache boundaries, dispatch state
2. Identify L: Memory patterns (coalesced?)
3. Identify D: Parallelism (threads × blocks)
4. Optimize: Coalesce memory (reduce L cost)
5. Optimize: Tile for cache (respect B boundaries)
```

### Performance Prediction
```
Time = dispatch_overhead + memory_time + compute_time

where:
  memory_time = D × L_access × access_count
  compute_time = D × ops / throughput

If engines overlap: Time = max(memory, compute) × overlap_factor
```

## Quick Analysis Template

For any GPU kernel:
1. **B**: What cache/dispatch boundaries exist?
2. **L**: What memory patterns? (coalesced/strided/scattered)
3. **D**: What parallelism? (threads × blocks × elements)
4. **Predict**: Time = dispatch + max(memory, compute)

---

## See Also

- [ALIGNMENT.md](ALIGNMENT.md) — Understanding as alignment
- [SKILL.md](SKILL.md) — Main BLD reference
