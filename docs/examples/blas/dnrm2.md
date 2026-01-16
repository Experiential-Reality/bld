# dnrm2_

**Cost**: B + D×L = 2 + 1×0.000 = 2.000

---

## Structure

```
structure dnrm2_

B empty: n_zero | n_positive

L square: x -> x2 (deps=0)
L sum: x2 -> acc (hierarchy_depth=16)
L sqrt: acc -> result (deps=0)

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
| square | x | x2 | 0 |  |
| sum | x2 | acc | 0 | hierarchy_depth=16 |
| sqrt | acc | result | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| x | n | input |

## Returns

`double`
