# Calibrate

**Cost**: B + D×L = 19 + 1×0.144 = 19.144

---

## Structure

```
structure Calibrate

B platform: cpu | gpu_intel | gpu_nvidia | gpu_amd | fpga | asic
  cpu -> uses(CPUCalibration)
  gpu_intel -> uses(IntelXeCalibration)
  gpu_nvidia -> uses(NvidiaCalibration)
  gpu_amd -> uses(AMDCalibration)
  fpga -> uses(FPGACalibration)
  asic -> uses(ASICCalibration)
B boundary_type: dispatch | workgroup | subgroup | memory_bank | cache_line
  dispatch -> crossing_cost_ns(50000), conflict_factor(1.0)
  workgroup -> crossing_cost_ns(200), conflict_factor(1.0)
  subgroup -> crossing_cost_ns(1), conflict_factor(1.0)
  memory_bank -> crossing_cost_ns(0), conflict_factor(4.0)
  cache_line -> crossing_cost_ns(0), conflict_factor(2.0)
B link_type: memory_coalesced | memory_scattered | compute_serial | compute_independent
  memory_coalesced -> ns_per_access(0.148), startup_ns(6400000)
  memory_scattered -> ns_per_access(0.59), startup_ns(6400000)
  compute_serial -> ns_per_access(0.0077), startup_ns(0)
  compute_independent -> ns_per_access(0.0018), startup_ns(0)
B dimension_type: compute_units | subgroup_lanes | threads_per_eu | array_elements
  compute_units -> extent(96), properties([parallel])
  subgroup_lanes -> extent(32), properties([lockstep), simd]
  threads_per_eu -> extent(7), properties([time_sliced])
  array_elements -> extent(N), properties([from_input])

L calibrate: platform -> calibration_data (deps=1)
L measure_dispatch: platform -> dispatch_cost (deps=0)
L measure_barrier: platform -> barrier_cost (deps=0)
L measure_cache_miss: platform -> cache_penalty (deps=0)
L measure_memory_bandwidth: platform -> memory_ns (deps=0)
L measure_compute_throughput: platform -> compute_ns (deps=0)
L measure_startup_latency: platform -> startup_ns (deps=0)
L count_compute_units: platform -> cu_count (deps=0)
L count_subgroup_size: platform -> subgroup_size (deps=0)
L validate_dxl: measurements ->  (l_r2) (deps=0)

D platforms: N [parallel]
D measurements: M [per_platform]
D benchmarks: K [parallel]

returns: calibration_data
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| platform | cpu \| gpu_intel \| gpu_nvidia \| gpu_amd \| fpga \| asic | topological |
| boundary_type | dispatch \| workgroup \| subgroup \| memory_bank \| cache_line | topological |
| link_type | memory_coalesced \| memory_scattered \| compute_serial \| compute_independent | topological |
| dimension_type | compute_units \| subgroup_lanes \| threads_per_eu \| array_elements | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| calibrate | platform | calibration_data | 1 |  |
| measure_dispatch | platform | dispatch_cost | 0 |  |
| measure_barrier | platform | barrier_cost | 0 |  |
| measure_cache_miss | platform | cache_penalty | 0 |  |
| measure_memory_bandwidth | platform | memory_ns | 0 |  |
| measure_compute_throughput | platform | compute_ns | 0 |  |
| measure_startup_latency | platform | startup_ns | 0 |  |
| count_compute_units | platform | cu_count | 0 |  |
| count_subgroup_size | platform | subgroup_size | 0 |  |
| validate_dxl | measurements |  | 0 | l_r2) (deps=0 |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| platforms | N | parallel |
| measurements | M | per_platform |
| benchmarks | K | parallel |

## Returns

`calibration_data`
