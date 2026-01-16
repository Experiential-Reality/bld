# drotm_

**Cost**: B + D×L = 4 + 1×0.000 = 4.000

---

## Structure

```
structure drotm_

B flag: rescale | neg_one | zero | one

L modified_rotate: x -> y (deps=0)

D x: n [input, output]
D y: n [input, output]
D param: five [input]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| flag | rescale \| neg_one \| zero \| one | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| modified_rotate | x | y | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| x | n | input, output |
| y | n | input, output |
| param | five | input |

## Returns

`void`
