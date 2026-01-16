# drotmg_

**Cost**: B + D×L = 3 + 1×0.144 = 3.144

---

## Structure

```
structure drotmg_

B rescale: underflow | overflow | normal

L generate_modified: d1 -> param (deps=1)

D param: five [output]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| rescale | underflow \| overflow \| normal | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| generate_modified | d1 | param | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| param | five | output |

## Returns

`void`
