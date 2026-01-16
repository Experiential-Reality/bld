# attention

**Cost**: B + D×L = 6 + 1×0.144 = 6.144

---

## Structure

```
structure attention

B masking: causal | full | custom
  causal -> lower_triangular(scores)
  full -> no_mask
  custom -> apply_mask(mask)
B normalize: pre_norm | post_norm | none

L project_q: queries -> Q (deps=0, rho=learnable)
L project_k: keys -> K (deps=0, rho=learnable)
L project_v: values -> V (deps=0, rho=learnable)
L compute_scores: Q -> scores (deps=0)
L apply_mask: scores -> masked_scores (deps=0)
L softmax: masked_scores -> attention_weights (deps=1)
L aggregate: attention_weights -> attended (deps=0)
L project_out: attended -> output (deps=0, rho=learnable)

D queries: seq_len_times_embed [parallel, input]
D keys: seq_len_times_embed [parallel, input]
D values: seq_len_times_embed [parallel, input]
D output: seq_len_times_embed [parallel, output]
D W_q: embed_times_head_dim [parallel]
D W_k: embed_times_head_dim [parallel]
D W_v: embed_times_head_dim [parallel]
D W_o: head_dim_times_embed [parallel]

returns: output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| masking | causal \| full \| custom | topological |
| normalize | pre_norm \| post_norm \| none | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| project_q | queries | Q | 0 | rho=learnable |
| project_k | keys | K | 0 | rho=learnable |
| project_v | values | V | 0 | rho=learnable |
| compute_scores | Q | scores | 0 |  |
| apply_mask | scores | masked_scores | 0 |  |
| softmax | masked_scores | attention_weights | 1 |  |
| aggregate | attention_weights | attended | 0 |  |
| project_out | attended | output | 0 | rho=learnable |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| queries | seq_len_times_embed | parallel, input |
| keys | seq_len_times_embed | parallel, input |
| values | seq_len_times_embed | parallel, input |
| output | seq_len_times_embed | parallel, output |
| W_q | embed_times_head_dim | parallel |
| W_k | embed_times_head_dim | parallel |
| W_v | embed_times_head_dim | parallel |
| W_o | head_dim_times_embed | parallel |

## Returns

`output`
