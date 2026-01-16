# dgemv_

**Cost**: B + D×L = 6 + 1×0.144 = 6.144

---

## Structure

```
structure dgemv_

B trans_mode: notrans | trans
B empty: m_zero_or_n_zero | valid
B skip: alpha_zero_beta_one | compute

L scale_y: y -> y (deps=0)
L dot_row: x -> temp (deps=1)
L accumulate: temp -> y (deps=0)

D A: m_times_n [input, column_major]
D x: var [input]
D y: var [input, output]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| trans_mode | notrans \| trans | topological |
| empty | m_zero_or_n_zero \| valid | topological |
| skip | alpha_zero_beta_one \| compute | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| scale_y | y | y | 0 |  |
| dot_row | x | temp | 1 |  |
| accumulate | temp | y | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| A | m_times_n | input, column_major |
| x | var | input |
| y | var | input, output |

## Returns

`void`
