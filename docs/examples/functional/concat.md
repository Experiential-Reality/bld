# concat

**Cost**: B + D×L = 2 + 1×0.000 = 2.000

---

## Structure

```
structure concat

B empty_check: empty | non_empty

L flatten: nested -> flat (pattern=reduce)

D xss: N [contiguous]
D inner: M [contiguous]
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| empty_check | empty \| non_empty | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| flatten | nested | flat | 0 | pattern=reduce |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| xss | N | contiguous |
| inner | M | contiguous |
