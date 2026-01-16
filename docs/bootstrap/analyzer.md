# Analyzer

**Cost**: B + D×L = 24 + 3×0.144 = 24.432

---

## Structure

```
structure Analyzer

B question: q1_boundaries | q2_links | q3_dimensions
  q1_boundaries -> extract_boundaries($source)
  q2_links -> extract_links($source)
  q3_dimensions -> extract_dimensions($source)
B boundary_indicator: conditional | type_tag | threshold | mode | switch | enum
  conditional -> if_else_chain
  type_tag -> isinstance_check
  threshold -> comparison_operator
  mode -> state_variable
  switch -> match_statement
  enum -> enumeration_type
B link_indicator: pointer | dependency | correlation | call | reference | import
  pointer -> address_of
  dependency -> depends_on
  correlation -> correlated_with
  call -> function_call
  reference -> variable_reference
  import -> module_import
B dimension_indicator: array | loop | parallel | layer | batch | sequence
  array -> array_type
  loop -> for_while_statement
  parallel -> parallel_annotation
  layer -> neural_layer
  batch -> batch_dimension
  sequence -> sequence_type
B result_status: complete | partial | failed
  complete -> all_three_extracted
  partial -> some_extracted
  failed -> extraction_error

L analyze: source -> structure (deps=1)
L q1: source -> boundaries (deps=0)
L q2: source -> links (deps=0)
L q3: source -> dimensions (deps=0)
L combine:  ->  (dimensions) -> structure (deps=1)
L validate_structure: structure -> validated (deps=0)

D source: 1 [input]
D structure: 1 [output, type=Structure]
D boundaries: N [output, parallel]
D links: M [output, parallel]
D dimensions: K [output, parallel]
D questions: 3 [parallel]

returns: structure
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| question | q1_boundaries \| q2_links \| q3_dimensions | topological |
| boundary_indicator | conditional \| type_tag \| threshold \| mode \| switch \| enum | topological |
| link_indicator | pointer \| dependency \| correlation \| call \| reference \| import | topological |
| dimension_indicator | array \| loop \| parallel \| layer \| batch \| sequence | topological |
| result_status | complete \| partial \| failed | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| analyze | source | structure | 1 |  |
| q1 | source | boundaries | 0 |  |
| q2 | source | links | 0 |  |
| q3 | source | dimensions | 0 |  |
| combine |  |  | 0 | dimensions) -> structure (deps=1 |
| validate_structure | structure | validated | 0 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| source | 1 | input |
| structure | 1 | output, type=Structure |
| boundaries | N | output, parallel |
| links | M | output, parallel |
| dimensions | K | output, parallel |
| questions | 3 | parallel |

## Returns

`structure`
