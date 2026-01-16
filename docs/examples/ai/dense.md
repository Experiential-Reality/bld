# dense

**Cost**: B + D×L = 5 + 1×0.000 = 5.000

---

## Structure

```
structure dense

B activation: linear | relu | sigmoid | tanh | softmax
  linear -> passthrough
  relu -> max(0, x)
  tanh -> tanh(x)
  softmax -> exp(x)

L matmul: input -> pre_activation (deps=0, rho=learnable)
L add_bias: pre_activation -> pre_activation (deps=0, rho=learnable)
L activate: pre_activation -> output (deps=0)

D input: in_dim [parallel, input]
D output: out_dim [parallel, output]
D weights: in_dim_times_out_dim [parallel]
D bias: out_dim [parallel]

returns: output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| activation | linear \| relu \| sigmoid \| tanh \| softmax | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| matmul | input | pre_activation | 0 | rho=learnable |
| add_bias | pre_activation | pre_activation | 0 | rho=learnable |
| activate | pre_activation | output | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| input | in_dim | parallel, input |
| output | out_dim | parallel, output |
| weights | in_dim_times_out_dim | parallel |
| bias | out_dim | parallel |

## Returns

`output`
