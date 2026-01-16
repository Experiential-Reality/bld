# dsymv_

**Cost**: B + D×L = 2 + 1×0.144 = 2.144

---

## Structure

```
structure dsymv_

B triangle: upper | lower

L symv: A -> y (deps=1)

D A: n_times_n [input]
D x: n [input]
D y: n [input, output]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| triangle | upper \| lower | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| symv | A | y | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| A | n_times_n | input |
| x | n | input |
| y | n | input, output |

## Returns

`void`
