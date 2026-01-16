# Optimizer

**Cost**: B + D×L = 22 + 1×0.863 = 22.863

---

## Structure

```
structure Optimizer

B phase: discover | analyze | suggest | apply | verify | done
  discover -> uses(Analyzer)
  analyze -> uses(CostCalculator)
  suggest -> uses(Suggester)
  apply -> uses(Transformer)
  verify -> uses(Verifier)
  done -> emit_result
B cost_component: b_cost | l_cost | d_extent
  b_cost -> count_partitions($boundaries)
  l_cost -> sum_l_costs($links)
  d_extent -> product_extents($dimensions)
B transformation: parallelize | fuse | coalesce | vectorize | none
  parallelize -> set(link.deps, 0), add_prop(dim, parallel)
  fuse -> merge_links_same_extent
  coalesce -> set(link.pattern, coalesced)
  vectorize -> add_prop(dim, simd)
  none -> nop
B pattern: parallel | sequential | tree | scan
  parallel -> all_deps_zero($links)
  sequential -> any_deps_nonzero($links)
  tree -> any_hierarchy_depth($links)
  scan -> any_communication($links)
B verify_result: dxl_valid | dxl_invalid | improved | not_improved
  dxl_valid -> b_invariant_under_d, l_scales_with_d
  dxl_invalid -> warn(dxl_violation)
  improved -> cost_decreased
  not_improved -> revert

L optimize: input -> output (deps=1)
L discover_to_analyze: structure -> analysis (deps=1)
L analyze_to_suggest: analysis -> suggestions (deps=1)
L suggest_to_apply: suggestions -> transformed (deps=1)
L apply_to_verify: transformed -> verified (deps=1)
L verify_to_iterate: verified -> next_iteration (deps=1)
L calculate_l_cost: link -> l_cost (deps=0)
L calculate_total_cost: structure -> cost (deps=0)
L verify_dxl: structure -> scaling_result (deps=0)
L suggest_parallelize: link -> suggestion (deps=0)
L suggest_fuse: links -> suggestion (deps=0)
L suggest_coalesce: link -> suggestion (deps=0)
L suggest_vectorize: dimension -> suggestion (deps=0)
L apply_transformation:  ->  (suggestion) -> structure (deps=1)

D input: 1 [input, type=Structure]
D output: 1 [output, type=Structure]
D iterations: N [sequential, until_converged]
D suggestions: M [parallel, ranked_by_cost_reduction]
D boundaries: K [from_structure]
D links: J [from_structure]
D dimensions: P [from_structure]

returns: output
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| phase | discover \| analyze \| suggest \| apply \| verify \| done | topological |
| cost_component | b_cost \| l_cost \| d_extent | topological |
| transformation | parallelize \| fuse \| coalesce \| vectorize \| none | topological |
| pattern | parallel \| sequential \| tree \| scan | topological |
| verify_result | dxl_valid \| dxl_invalid \| improved \| not_improved | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| optimize | input | output | 1 |  |
| discover_to_analyze | structure | analysis | 1 |  |
| analyze_to_suggest | analysis | suggestions | 1 |  |
| suggest_to_apply | suggestions | transformed | 1 |  |
| apply_to_verify | transformed | verified | 1 |  |
| verify_to_iterate | verified | next_iteration | 1 |  |
| calculate_l_cost | link | l_cost | 0 |  |
| calculate_total_cost | structure | cost | 0 |  |
| verify_dxl | structure | scaling_result | 0 |  |
| suggest_parallelize | link | suggestion | 0 |  |
| suggest_fuse | links | suggestion | 0 |  |
| suggest_coalesce | link | suggestion | 0 |  |
| suggest_vectorize | dimension | suggestion | 0 |  |
| apply_transformation |  |  | 0 | suggestion) -> structure (deps=1 |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| input | 1 | input, type=Structure |
| output | 1 | output, type=Structure |
| iterations | N | sequential, until_converged |
| suggestions | M | parallel, ranked_by_cost_reduction |
| boundaries | K | from_structure |
| links | J | from_structure |
| dimensions | P | from_structure |

## Returns

`output`
