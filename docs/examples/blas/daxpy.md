# daxpy_

**Cost**: B + D×L = 2 + 1×0.000 = 2.000

---

## Structure

```
structure daxpy_

B skip: alpha_zero | alpha_nonzero

L fma: x -> y (deps=0)

D x: n [input]
D y: n [input, output]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| skip | alpha_zero \| alpha_nonzero | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| fma | x | y | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| x | n | input |
| y | n | input, output |

## Returns

`void`
