# transformer

**Cost**: B + D×L = 0 + 1×0.144 = 0.144

---

## Structure

```
structure transformer


L embed: token_ids -> hidden (deps=0, rho=from_gguf)
L blocks: hidden -> final_hidden (uses=transformer_block, deps=1)
L final_norm: final_hidden -> normed (deps=0)
L lm_head: normed -> logits (deps=0, rho=from_gguf)

D layers: n_layers [sequential]
D tokens: seq_len [parallel]

returns: logits
```

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| embed | token_ids | hidden | 0 | rho=from_gguf |
| blocks | hidden | final_hidden | 1 | uses=transformer_block |
| final_norm | final_hidden | normed | 0 |  |
| lm_head | normed | logits | 0 | rho=from_gguf |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| layers | n_layers | sequential |
| tokens | seq_len | parallel |

## Returns

`logits`
