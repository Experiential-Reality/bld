# dtrsm_

**Cost**: B + D×L = 8 + 1×0.144 = 8.144

---

## Structure

```
structure dtrsm_

B position: left | right
B triangle: upper | lower
B transpose: normal | transposed
B diagonal: unit | non_unit

L trsm: A -> B (deps=1)

D A: k_times_k [input]
D B: m_times_n [input, output]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| position | left \| right | topological |
| triangle | upper \| lower | topological |
| transpose | normal \| transposed | topological |
| diagonal | unit \| non_unit | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| trsm | A | B | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| A | k_times_k | input |
| B | m_times_n | input, output |

## Returns

`void`
