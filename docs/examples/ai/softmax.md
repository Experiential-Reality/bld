# softmax

**Cost**: B + D×L = 2 + 1×0.288 = 2.288

---

## Structure

```
structure softmax

B stability: stable | overflow_risk
  stable -> direct_computation
  overflow_risk -> subtract_max_first

L find_max: logits -> max_val (deps=1, hierarchy_depth=log2_N)
L subtract_max: logits -> shifted (deps=0)
L exp: shifted -> exp_vals (deps=0)
L sum: exp_vals -> sum_val (deps=1, hierarchy_depth=log2_N)
L normalize: exp_vals -> probs (deps=0)

D logits: N [parallel, input]
D probs: N [parallel, output]

returns: probs
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| stability | stable \| overflow_risk | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| find_max | logits | max_val | 1 | hierarchy_depth=log2_N |
| subtract_max | logits | shifted | 0 |  |
| exp | shifted | exp_vals | 0 |  |
| sum | exp_vals | sum_val | 1 | hierarchy_depth=log2_N |
| normalize | exp_vals | probs | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| logits | N | parallel, input |
| probs | N | parallel, output |

## Returns

`probs`
