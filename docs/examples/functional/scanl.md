# scanl

**Cost**: B + D×L = 2 + 1×0.000 = 2.000

---

## Structure

```
structure scanl

B empty_check: empty | non_empty

L accumulate: element -> running (communication_distances=[1])

D xs: N [contiguous]
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| empty_check | empty \| non_empty | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| accumulate | element | running | 0 | communication_distances=[1] |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| xs | N | contiguous |
