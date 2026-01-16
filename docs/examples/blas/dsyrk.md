# dsyrk_

**Cost**: B + D×L = 4 + 1×0.144 = 4.144

---

## Structure

```
structure dsyrk_

B triangle: upper | lower
B transpose: normal | transposed

L syrk: A -> C (deps=1)

D A: n_times_k [input]
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
| syrk | A | C | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| A | n_times_k | input |
| C | n_times_n | input, output |

## Returns

`void`
