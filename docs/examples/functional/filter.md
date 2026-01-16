# filter

**Cost**: B + D×L = 4 + 1×0.144 = 4.144

---

## Structure

```
structure filter

B empty_check: empty | non_empty
B predicate: passes | fails

L test: element -> bool (deps=0)
L keep: element -> result (deps=1)

D xs: N [contiguous]
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| empty_check | empty \| non_empty | topological |
| predicate | passes \| fails | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| test | element | bool | 0 |  |
| keep | element | result | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| xs | N | contiguous |
