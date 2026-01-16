# idamax_

**Cost**: B + D×L = 3 + 1×0.144 = 3.144

---

## Structure

```
structure idamax_

B empty: n_zero | n_single | n_many

L find_max: x -> idx (deps=1)

D x: n [input]

returns: int
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| empty | n_zero \| n_single \| n_many | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| find_max | x | idx | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| x | n | input |

## Returns

`int`
