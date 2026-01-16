# ddot_

**Cost**: B + D×L = 0 + 1×0.144 = 0.144

---

## Structure

```
structure ddot_


L product: element -> temp (deps=0)
L accumulate: temp -> acc (deps=1)

D x: n [input]
D y: n [input]

returns: double
```

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| product | element | temp | 0 |  |
| accumulate | temp | acc | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| x | n | input |
| y | n | input |

## Returns

`double`
