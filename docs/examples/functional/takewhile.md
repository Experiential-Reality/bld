# takeWhile

**Cost**: B + D×L = 4 + 1×0.144 = 4.144

---

## Structure

```
structure takeWhile

B empty_check: empty | non_empty
B predicate: passes | fails

L test_and_take: element -> maybe_result (deps=1)

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
| test_and_take | element | maybe_result | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| xs | N | contiguous |
