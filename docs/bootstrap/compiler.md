# BLDCompiler

**Cost**: B + D×L = 19 + 1×0.863 = 19.863

---

## Structure

```
structure BLDCompiler

B phase: parse | analyze | optimize | lower | emit | done
  parse -> parse_bld($source, structure)
  analyze -> uses(Analyzer)
  optimize -> uses(Optimizer)
  lower -> uses(Lowering)
  emit -> uses(ELF64)
  done -> emit($binary)
B target: x86_64 | aarch64 | wasm
  x86_64 -> uses(X86)
  aarch64 -> uses(ARM64)
  wasm -> uses(WASM)
B format: elf | macho | pe | raw
  elf -> uses(ELF)
  macho -> uses(MachO)
  pe -> uses(PE)
  raw -> emit_raw_bytes
B error: none | parse_error | analyze_error | optimize_error | lower_error | emit_error
  none -> continue
  parse_error -> report_parse_error
  analyze_error -> report_analyze_error
  optimize_error -> report_optimize_error
  lower_error -> report_lower_error
  emit_error -> report_emit_error

L compile: source -> binary (deps=1)
L parse: source -> structure (deps=0)
L analyze: structure -> analyzed (deps=1)
L optimize: analyzed -> optimized (deps=1)
L lower: optimized -> instructions (deps=1)
L emit: instructions -> binary (deps=1)
L main: source -> binary (deps=1)

D source: N [input, contiguous]
D binary: M [output, sequential]
D tokens: K [type=Token]
D structure: 1 [type=Structure]
D optimized: 1 [type=Structure]
D instructions: J [type=Instruction]
D opt_iterations: P [sequential, until_converged]

returns: binary
```

## Boundaries (B)

| Boundary | Partitions | Properties |
|----------|------------|------------|
| phase | parse \| analyze \| optimize \| lower \| emit \| done | topological |
| target | x86_64 \| aarch64 \| wasm | topological |
| format | elf \| macho \| pe \| raw | topological |
| error | none \| parse_error \| analyze_error \| optimize_error \| lower_error \| emit_error | topological |

## Links (L)

| Link | Source | Target | deps | Attributes |
|------|--------|--------|------|------------|
| compile | source | binary | 1 |  |
| parse | source | structure | 0 |  |
| analyze | structure | analyzed | 1 |  |
| optimize | analyzed | optimized | 1 |  |
| lower | optimized | instructions | 1 |  |
| emit | instructions | binary | 1 |  |
| main | source | binary | 1 |  |

## Dimensions (D)

| Dimension | Extent | Properties |
|-----------|--------|------------|
| source | N | input, contiguous |
| binary | M | output, sequential |
| tokens | K | type=Token |
| structure | 1 | type=Structure |
| optimized | 1 | type=Structure |
| instructions | J | type=Instruction |
| opt_iterations | P | sequential, until_converged |

## Returns

`binary`
