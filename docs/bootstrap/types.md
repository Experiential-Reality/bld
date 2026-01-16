# ParsedStructure

**Cost**: B + D×L = 0 + 1×0.000 = 0.000

---

## Structure

```
structure ParsedStructure



D name: identifier
D boundaries: M [parallel, type=ParsedBoundary]
D links: N [parallel, type=ParsedLink]
D dimensions: K [parallel, type=ParsedDimension]
D parameters: P [parallel, type=ParsedParameter]
D return_type: identifier [optional]

returns: ParsedStructure
```

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| name | identifier |  |
| boundaries | M | parallel, type=ParsedBoundary |
| links | N | parallel, type=ParsedLink |
| dimensions | K | parallel, type=ParsedDimension |
| parameters | P | parallel, type=ParsedParameter |
| return_type | identifier | optional |

## Returns

`ParsedStructure`
