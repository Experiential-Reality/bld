# forward

**Cost**: B + D×L = 2 + 1×0.144 = 2.144

---

## Structure

```
structure forward

B valid_input: valid | invalid
  valid -> proceed
  invalid -> error

L transform: input -> output (uses=mlp, deps=1)

D input: batch_times_in_dim [parallel, input]
D output: batch_times_out_dim [parallel, output]
D batch: N [parallel]

returns: output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| valid_input | valid \| invalid | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| transform | input | output | 1 | uses=mlp |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| input | batch_times_in_dim | parallel, input |
| output | batch_times_out_dim | parallel, output |
| batch | N | parallel |

## Returns

`output`
