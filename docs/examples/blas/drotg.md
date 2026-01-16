# drotg_

**Cost**: B + D×L = 3 + 1×0.144 = 3.144

---

## Structure

```
structure drotg_

B cases: b_zero | a_zero | general

L generate: a -> c (deps=1)


returns: void
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| cases | b_zero \| a_zero \| general | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| generate | a | c | 1 |  |

## Returns

`void`
