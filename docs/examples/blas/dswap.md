# dswap_

**Cost**: B + D×L = 0 + 1×0.000 = 0.000

---

## Structure

```
structure dswap_


L swap: x -> y (deps=0)

D x: n [input, output]
D y: n [input, output]

returns: void
```

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| swap | x | y | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| x | n | input, output |
| y | n | input, output |

## Returns

`void`
