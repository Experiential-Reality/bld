# foldr

**Cost**: B + D×L = 2 + 1×0.000 = 2.000

---

## Structure

```
structure foldr

B empty_check: empty | non_empty

L combine: element -> acc (hierarchy_depth=8)

D xs: N [contiguous]
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| empty_check | empty \| non_empty | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| combine | element | acc | 0 | hierarchy_depth=8 |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| xs | N | contiguous |
