# dsyr2_

**Cost**: B + D×L = 2 + 1×0.000 = 2.000

---

## Structure

```
structure dsyr2_

B triangle: upper | lower

L rank2: x -> A (deps=0)

D x: n [input]
D y: n [input]
D A: n_times_n [input, output]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| triangle | upper \| lower | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| rank2 | x | A | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| x | n | input |
| y | n | input |
| A | n_times_n | input, output |

## Returns

`void`
