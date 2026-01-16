# Aligner

**Cost**: B + D×L = 17 + 1×0.144 = 17.144

---

## Structure

```
structure Aligner

B transformation: parallelize | fuse | coalesce | vectorize | cascade | reorder
  parallelize -> set(link.deps, 0), add_prop(dim, parallel)
  fuse -> merge_links_with_same_extent
  coalesce -> set(link.pattern, coalesced)
  vectorize -> add_prop(dim, simd)
  cascade -> add_cascade_stage
  reorder -> topological_sort_by_deps
B pattern_strategy: parallel_opt | sequential_opt | tree_opt | scan_opt
  parallel_opt -> suggest(vectorize)
  sequential_opt -> suggest(parallelize), suggest(reorder)
  tree_opt -> suggest(reorder), suggest(fuse)
  scan_opt -> suggest(coalesce), suggest(cascade)
B suggestion_quality: high | medium | low | invalid
  high -> cost_reduction > 0.5
  medium -> cost_reduction > 0.1
  low -> cost_reduction > 0.0
  invalid -> cost_reduction <(0.0)
B convergence: improving | converged | diverging
  improving -> cost_decreased
  converged -> cost_change < threshold
  diverging -> cost_increased

L align: input -> output (deps=1)
L generate_suggestions: structure -> suggestions (deps=0)
L calculate_cost: structure -> cost (deps=0)
L try_parallelize: link ->  (new_link) (deps=0)
L try_fuse:  ->  (fused_link) (deps=0)
L try_coalesce: link ->  (new_link) (deps=0)
L try_vectorize: dimension ->  (new_dimension) (deps=0)
L try_cascade: boundary ->  (cascaded) (deps=0)
L apply_suggestion:  ->  (suggestion) -> new_structure (deps=1)
L verify_dxl: structure ->  (l_scales) (deps=0)
L check_convergence:  ->  (new_cost) -> convergence_status (deps=0)

D input: 1 [input, type=Structure]
D output: 1 [output, type=Structure]
D iterations: N [sequential, until_cost_converged]
D suggestions: M [parallel, ranked_by_cost_reduction]
D boundaries: K [from_input]
D links: J [from_input]
D dimensions: P [from_input]

returns: output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| transformation | parallelize \| fuse \| coalesce \| vectorize \| cascade \| reorder | topological |
| pattern_strategy | parallel_opt \| sequential_opt \| tree_opt \| scan_opt | topological |
| suggestion_quality | high \| medium \| low \| invalid | topological |
| convergence | improving \| converged \| diverging | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| align | input | output | 1 |  |
| generate_suggestions | structure | suggestions | 0 |  |
| calculate_cost | structure | cost | 0 |  |
| try_parallelize | link |  | 0 | new_link) (deps=0 |
| try_fuse |  |  | 0 | fused_link) (deps=0 |
| try_coalesce | link |  | 0 | new_link) (deps=0 |
| try_vectorize | dimension |  | 0 | new_dimension) (deps=0 |
| try_cascade | boundary |  | 0 | cascaded) (deps=0 |
| apply_suggestion |  |  | 0 | suggestion) -> new_structure (deps=1 |
| verify_dxl | structure |  | 0 | l_scales) (deps=0 |
| check_convergence |  |  | 0 | new_cost) -> convergence_status (deps=0 |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| input | 1 | input, type=Structure |
| output | 1 | output, type=Structure |
| iterations | N | sequential, until_cost_converged |
| suggestions | M | parallel, ranked_by_cost_reduction |
| boundaries | K | from_input |
| links | J | from_input |
| dimensions | P | from_input |

## Returns

`output`
