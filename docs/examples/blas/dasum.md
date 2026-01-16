# dasum_

**Cost**: B + D×L = 2 + 1×0.000 = 2.000

---

## Structure

```
structure dasum_

B empty: n_zero | n_positive

L abs: x -> ax (deps=0)
L sum: ax -> acc (hierarchy_depth=16)

D x: n [input]

returns: double
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| empty | n_zero \| n_positive | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| abs | x | ax | 0 |  |
| sum | ax | acc | 0 | hierarchy_depth=16 |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| x | n | input |

## Returns

`double`
