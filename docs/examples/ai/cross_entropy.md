# cross_entropy

**Cost**: B + D×L = 3 + 1×0.288 = 3.288

---

## Structure

```
structure cross_entropy

B edge_case: normal | zero_pred | perfect_pred
  normal -> standard_computation
  zero_pred -> clip_to_epsilon
  perfect_pred -> zero_loss

L log_pred: predictions -> log_preds (deps=0)
L multiply: log_preds -> weighted (deps=0)
L sum_classes: weighted -> sample_losses (deps=1)
L mean_batch: sample_losses -> loss (deps=1, hierarchy_depth=log2_batch)

D predictions: batch_times_classes [parallel, input]
D targets: batch_times_classes [parallel, input]
D loss: 1 [scalar, output]

returns: loss
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| edge_case | normal \| zero_pred \| perfect_pred | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| log_pred | predictions | log_preds | 0 |  |
| multiply | log_preds | weighted | 0 |  |
| sum_classes | weighted | sample_losses | 1 |  |
| mean_batch | sample_losses | loss | 1 | hierarchy_depth=log2_batch |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| predictions | batch_times_classes | parallel, input |
| targets | batch_times_classes | parallel, input |
| loss | 1 | scalar, output |

## Returns

`loss`
