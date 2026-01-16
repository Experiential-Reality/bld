# dtrmm_

**Cost**: B + D×L = 8 + 1×0.144 = 8.144

---

## Structure

```
structure dtrmm_

B position: left | right
  left -> k_dim(M), outer_var(k), inner_var(i)
  right -> k_dim(N), outer_var(j), inner_var(k)
B triangle: upper | lower
  upper -> k_start(0), k_end(K), k_direction(forward), inner_bound(< k), diag_after_inner
  lower -> k_start(K-1), k_end(0), k_direction(backward), inner_bound(> k), diag_before_inner
B transpose: normal | transposed
  normal -> A_access(A[i + k * lda])
  transposed -> A_access(A[k + i * lda])
B diagonal: unit | non_unit
  unit -> skip_diagonal, diag_value(1.0)
  non_unit -> include_diagonal, diag_value(A[k + k * lda])

L trmm: A -> B (deps=1)

D A: k_times_k [input]
D B: m_times_n [input, output]

returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| position | left \| right | topological |
| triangle | upper \| lower | topological |
| transpose | normal \| transposed | topological |
| diagonal | unit \| non_unit | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| trmm | A | B | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| A | k_times_k | input |
| B | m_times_n | input, output |

## Returns

`void`
