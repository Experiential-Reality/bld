# take

**Cost**: B + D×L = 4 + 1×0.000 = 4.000

---

## Structure

```
structure take

B count_check: zero_or_negative | positive
B empty_check: empty | non_empty

L slice: elements -> prefix (deps=0)

D xs: N [contiguous]
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| count_check | zero_or_negative \| positive | topological |
| empty_check | empty \| non_empty | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| slice | elements | prefix | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| xs | N | contiguous |
