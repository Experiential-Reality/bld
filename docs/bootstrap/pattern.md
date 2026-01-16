# PatternDetector

**Cost**: B + D×L = 9 + 1×0.144 = 9.144

---

## Structure

```
structure PatternDetector

B execution_pattern: parallel | sequential | tree | scan
B deps_class: zero | nonzero
B has_special: hierarchy | communication | neither

L extract_deps: links -> deps_values (deps=0)
L classify_deps: deps_values -> deps_class (deps=0)
L check_hierarchy: links -> has_hierarchy (deps=0)
L check_communication: links -> has_communication (deps=0)
L any_hierarchy: has_hierarchy -> result (deps=0)
L any_communication: has_communication -> result (deps=0)
L any_sequential: deps_class -> result (deps=0)
L select_pattern: results -> execution_pattern   # Depends on all reductions (deps=1)

D parsed: 1 [input, type=ParsedStructure]
D pattern: 1 [output]
D links: N [input]
D deps_values: N [parallel]
D has_hierarchy: N [parallel]
D has_communication: N [parallel]

returns: execution_pattern
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| execution_pattern | parallel \| sequential \| tree \| scan | topological |
| deps_class | zero \| nonzero | topological |
| has_special | hierarchy \| communication \| neither | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| extract_deps | links | deps_values | 0 |  |
| classify_deps | deps_values | deps_class | 0 |  |
| check_hierarchy | links | has_hierarchy | 0 |  |
| check_communication | links | has_communication | 0 |  |
| any_hierarchy | has_hierarchy | result | 0 |  |
| any_communication | has_communication | result | 0 |  |
| any_sequential | deps_class | result | 0 |  |
| select_pattern | results | execution_pattern   # Depends on all reductions | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| parsed | 1 | input, type=ParsedStructure |
| pattern | 1 | output |
| links | N | input |
| deps_values | N | parallel |
| has_hierarchy | N | parallel |
| has_communication | N | parallel |

## Returns

`execution_pattern`
