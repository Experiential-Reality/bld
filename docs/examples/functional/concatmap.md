# concatMap

**Cost**: B + D×L = 2 + 1×0.000 = 2.000

---

## Structure

```
structure concatMap

B empty_check: empty | non_empty

L apply_f: element -> list (deps=0)
L flatten: nested -> flat (pattern=reduce)

D xs: N [contiguous]
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| empty_check | empty \| non_empty | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| apply_f | element | list | 0 |  |
| flatten | nested | flat | 0 | pattern=reduce |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| xs | N | contiguous |
