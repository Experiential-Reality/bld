# dger_

**Cost**: B + D×L = 0 + 1×0.000 = 0.000

---

## Structure

```
structure dger_


L outer_product: x -> A (deps=0)

D x: m [input]
D y: n [input]
D A: m_times_n [input, output]

returns: void
```

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| outer_product | x | A | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| x | m | input |
| y | n | input |
| A | m_times_n | input, output |

## Returns

`void`
