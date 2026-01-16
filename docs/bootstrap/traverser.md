# Traverser

**Cost**: B + D×L = 11 + 1×0.863 = 11.863

---

## Structure

```
structure Traverser

B visit_type: boundary | link | dimension | semantic
  boundary -> evaluate_partitions
  link -> follow_connection
  dimension -> iterate_elements
  semantic -> interpret_annotation
B order: parallel | sequential
  parallel -> deps_zero, can_parallelize
  sequential -> deps_nonzero, must_sequence
B semantic_type: pattern_match | text_match | action | template | compose
  pattern_match -> char_classification
  text_match -> keyword_detection
  action -> state_mutation
  template -> string_format
  compose -> call_substructure

L visit_boundary: structure -> current_boundary (deps=0)
L evaluate_partition: current_boundary -> state (deps=1)
L visit_link: structure -> current_link (deps=1)
L execute_link: current_link -> result (deps=1)
L visit_dimension: structure -> current_dim_index (deps=0)
L iterate: current_dim_index -> result (deps=1)
L parse_semantic: semantic_type -> instruction (deps=0)
L apply_semantic: instruction -> state (deps=1)
L traverse: structure -> result (deps=1)

D structure: 1 [input, type=ParsedStructure]
D current_boundary: 1 [sequential]
D current_link: 1 [sequential]
D current_dim_index: 1 [sequential]
D state: N [sequential]
D result: N [output]

returns: result
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| visit_type | boundary \| link \| dimension \| semantic | topological |
| order | parallel \| sequential | topological |
| semantic_type | pattern_match \| text_match \| action \| template \| compose | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| visit_boundary | structure | current_boundary | 0 |  |
| evaluate_partition | current_boundary | state | 1 |  |
| visit_link | structure | current_link | 1 |  |
| execute_link | current_link | result | 1 |  |
| visit_dimension | structure | current_dim_index | 0 |  |
| iterate | current_dim_index | result | 1 |  |
| parse_semantic | semantic_type | instruction | 0 |  |
| apply_semantic | instruction | state | 1 |  |
| traverse | structure | result | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| structure | 1 | input, type=ParsedStructure |
| current_boundary | 1 | sequential |
| current_link | 1 | sequential |
| current_dim_index | 1 | sequential |
| state | N | sequential |
| result | N | output |

## Returns

`result`
