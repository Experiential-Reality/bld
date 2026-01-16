# dgemm_

**Cost**: B + D×L = 6 + 1×0.144 = 6.144

---

## Structure

```
structure dgemm_

B trans_mode: notrans | trans
B empty: dims_zero | valid
B skip: alpha_zero_beta_one | compute

L scale_C: C -> C (deps=0)
L matmul: A -> C (deps=1)

D A: m_times_k [input]
D B: k_times_n [input]
D C: m_times_n [input, output]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| trans_mode | notrans \| trans | topological |
| empty | dims_zero \| valid | topological |
| skip | alpha_zero_beta_one \| compute | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| scale_C | C | C | 0 |  |
| matmul | A | C | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| A | m_times_k | input |
| B | k_times_n | input |
| C | m_times_n | input, output |

## Returns

`void`
