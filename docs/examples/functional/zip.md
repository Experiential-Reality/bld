# zip

**Cost**: B + D×L = 3 + 1×0.000 = 3.000

---

## Structure

```
structure zip

B either_empty: both_non_empty | xs_empty | ys_empty

L pair: elements -> tuple (deps=0)

D xs: N [parallel, contiguous]
D ys: M [parallel, contiguous]
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| either_empty | both_non_empty \| xs_empty \| ys_empty | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| pair | elements | tuple | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| xs | N | parallel, contiguous |
| ys | M | parallel, contiguous |
