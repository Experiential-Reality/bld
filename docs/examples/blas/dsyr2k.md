# dsyr2k_

**Cost**: B + D×L = 4 + 1×0.144 = 4.144

---

## Structure

```
structure dsyr2k_

B triangle: upper | lower
B transpose: normal | transposed

L syr2k: A -> C (deps=1)

D A: n_times_k [input]
D B: n_times_k [input]
D C: n_times_n [input, output]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| triangle | upper \| lower | topological |
| transpose | normal \| transposed | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| syr2k | A | C | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| A | n_times_k | input |
| B | n_times_k | input |
| C | n_times_n | input, output |

## Returns

`void`
