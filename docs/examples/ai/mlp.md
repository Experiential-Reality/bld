# mlp

**Cost**: B + D×L = 2 + 1×0.432 = 2.432

---

## Structure

```
structure mlp

B training_mode: train | inference
  train -> apply_dropout
  inference -> no_dropout

L layer_1: input -> hidden (uses=dense, deps=1)
L layer_hidden: hidden -> hidden (uses=dense, deps=1)
L layer_out: hidden -> output (uses=dense, deps=1)
L dropout: hidden -> hidden (deps=0)

D input: in_dim [parallel, input]
D hidden: hidden_dim [parallel]
D output: out_dim [parallel, output]

returns: output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| training_mode | train \| inference | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| layer_1 | input | hidden | 1 | uses=dense |
| layer_hidden | hidden | hidden | 1 | uses=dense |
| layer_out | hidden | output | 1 | uses=dense |
| dropout | hidden | hidden | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| input | in_dim | parallel, input |
| hidden | hidden_dim | parallel |
| output | out_dim | parallel, output |

## Returns

`output`
