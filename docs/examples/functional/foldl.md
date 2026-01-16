# foldl

**Cost**: B + D×L = 2 + 1×0.144 = 2.144

---

## Structure

```
structure foldl

B empty_check: empty | non_empty

L combine: acc -> acc (deps=1)

D xs: N [contiguous]
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| empty_check | empty \| non_empty | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| combine | acc | acc | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| xs | N | contiguous |
