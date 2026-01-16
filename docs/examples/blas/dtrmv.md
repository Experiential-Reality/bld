# dtrmv_

**Cost**: B + D×L = 6 + 1×0.144 = 6.144

---

## Structure

```
structure dtrmv_

B triangle: upper | lower
B transpose: normal | transposed
B diagonal: unit | non_unit

L trmv: A -> x (deps=1)

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
| trmv | A | x | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| A | n_times_n | input |
| x | n | input, output |

## Returns

`void`
