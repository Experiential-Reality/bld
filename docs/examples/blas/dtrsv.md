# dtrsv_

**Cost**: B + D×L = 6 + 1×0.144 = 6.144

---

## Structure

```
structure dtrsv_

B triangle: upper | lower
B transpose: normal | transposed
B diagonal: unit | non_unit

L trsv: A -> x (deps=1)

D A: n_times_n [input]
D x: n [input, output]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| triangle | upper \| lower | topological |
| transpose | normal \| transposed | topological |
| diagonal | unit \| non_unit | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| trsv | A | x | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| A | n_times_n | input |
| x | n | input, output |

## Returns

`void`
