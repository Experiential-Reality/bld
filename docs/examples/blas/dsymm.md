# dsymm_

**Cost**: B + D×L = 4 + 1×0.144 = 4.144

---

## Structure

```
structure dsymm_

B position: left | right
B triangle: upper | lower

L symm: A -> C (deps=1)

D A: k_times_k [input]
D B: m_times_n [input]
D C: m_times_n [input, output]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| position | left \| right | topological |
| triangle | upper \| lower | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| symm | A | C | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| A | k_times_k | input |
| B | m_times_n | input |
| C | m_times_n | input, output |

## Returns

`void`
