# map

**Cost**: B + D×L = 2 + 1×0.000 = 2.000

---

## Structure

```
structure map

B empty_check: empty | non_empty

L apply_f: element -> result (deps=0)

D xs: N [parallel, contiguous]
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| empty_check | empty \| non_empty | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| apply_f | element | result | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| xs | N | parallel, contiguous |
