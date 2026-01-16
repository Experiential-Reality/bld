# BLD Structure Documentation

This documentation is automatically generated from BLD structure files using `bld-py markdown`.

## Source Structures

Core structures that make BLD self-hosting:

| Structure | Description | Cost |
|-----------|-------------|------|
| [bld](src/bld.md) | BLD language specification (self-referential) | - |
| [cli](src/cli.md) | CLI commands (build/analyze/optimize) | - |
| [parser](src/parser.md) | BLD parser structure | - |
| [tokenizer](src/tokenizer.md) | Lexical tokenizer | - |
| [grammar](src/grammar.md) | BLD grammar rules | - |
| [traverser](src/traverser.md) | Structure traversal | - |
| [compiler](src/compiler.md) | Compilation pipeline | - |
| [analyzer](src/analyzer.md) | Static analysis | - |
| [optimizer](src/optimizer.md) | Optimization passes | - |
| [aligner](src/aligner.md) | Structure alignment | - |
| [calibrate](src/calibrate.md) | Calibration | - |

### Code Generation

| Structure | Description |
|-----------|-------------|
| [elf](src/elf.md) | ELF64 binary format |
| [lowering](src/lowering.md) | Abstract lowering |
| [lowering_x86](src/lowering_x86.md) | x86-64 lowering |
| [lowering_riscv](src/lowering_riscv.md) | RISC-V lowering |
| [lowering_aarch64](src/lowering_aarch64.md) | AArch64 lowering |

### Architecture Structures (Bidirectional)

| Structure | Description |
|-----------|-------------|
| [x86](src/x86.md) | x86-64 instruction encoding/decoding |
| [riscv](src/riscv.md) | RISC-V instruction encoding/decoding |
| [aarch64](src/aarch64.md) | AArch64 instruction encoding/decoding |
| [translate_x86_riscv](src/translate_x86_riscv.md) | Binary translation |

### Language Structures (Bidirectional)

| Structure | Description |
|-----------|-------------|
| [python](src/python.md) | Python language (emit/parse) |
| [github_markdown](src/github_markdown.md) | GitHub-flavored markdown |

### Other

| Structure | Description |
|-----------|-------------|
| [pattern](src/pattern.md) | Pattern matching |
| [types](src/types.md) | Type system |

---

## Examples

### Functional Programming

Higher-order functions as BLD structures:

| Structure | Description |
|-----------|-------------|
| [map](examples/functional/map.md) | Transform each element |
| [filter](examples/functional/filter.md) | Select elements by predicate |
| [foldl](examples/functional/foldl.md) | Left fold (reduce) |
| [foldr](examples/functional/foldr.md) | Right fold |
| [scanl](examples/functional/scanl.md) | Running fold |
| [concat](examples/functional/concat.md) | Concatenate lists |
| [concatmap](examples/functional/concatmap.md) | Map then concatenate |
| [zip](examples/functional/zip.md) | Pair elements |
| [zipwith](examples/functional/zipwith.md) | Combine with function |
| [take](examples/functional/take.md) | First n elements |
| [takewhile](examples/functional/takewhile.md) | Take while predicate |

### BLAS (Linear Algebra)

Double-precision BLAS operations as BLD structures:

#### Level 1 (Vector)

| Structure | Description |
|-----------|-------------|
| [daxpy](examples/blas/daxpy.md) | y = αx + y |
| [dcopy](examples/blas/dcopy.md) | Copy vector |
| [ddot](examples/blas/ddot.md) | Dot product |
| [dnrm2](examples/blas/dnrm2.md) | Euclidean norm |
| [dasum](examples/blas/dasum.md) | Sum of absolute values |
| [dscal](examples/blas/dscal.md) | Scale vector |
| [dswap](examples/blas/dswap.md) | Swap vectors |
| [idamax](examples/blas/idamax.md) | Index of max absolute value |
| [drot](examples/blas/drot.md) | Apply rotation |
| [drotg](examples/blas/drotg.md) | Generate rotation |
| [drotm](examples/blas/drotm.md) | Modified rotation |
| [drotmg](examples/blas/drotmg.md) | Generate modified rotation |

#### Level 2 (Matrix-Vector)

| Structure | Description |
|-----------|-------------|
| [dgemv](examples/blas/dgemv.md) | y = αAx + βy |
| [dsymv](examples/blas/dsymv.md) | Symmetric matrix-vector |
| [dtrmv](examples/blas/dtrmv.md) | Triangular matrix-vector |
| [dtrsv](examples/blas/dtrsv.md) | Triangular solve |
| [dger](examples/blas/dger.md) | Rank-1 update |
| [dsyr](examples/blas/dsyr.md) | Symmetric rank-1 |
| [dsyr2](examples/blas/dsyr2.md) | Symmetric rank-2 |

#### Level 3 (Matrix-Matrix)

| Structure | Description |
|-----------|-------------|
| [dgemm](examples/blas/dgemm.md) | C = αAB + βC |
| [dsymm](examples/blas/dsymm.md) | Symmetric matrix multiply |
| [dsyrk](examples/blas/dsyrk.md) | Symmetric rank-k |
| [dsyr2k](examples/blas/dsyr2k.md) | Symmetric rank-2k |
| [dtrmm](examples/blas/dtrmm.md) | Triangular matrix multiply |
| [dtrsm](examples/blas/dtrsm.md) | Triangular solve |

### AI/ML Operations

Neural network primitives as BLD structures:

| Structure | Description |
|-----------|-------------|
| [attention](examples/ai/attention.md) | Attention mechanism |
| [transformer](examples/ai/transformer.md) | Transformer block |
| [softmax](examples/ai/softmax.md) | Softmax activation |
| [cross_entropy](examples/ai/cross_entropy.md) | Cross-entropy loss |
| [dense](examples/ai/dense.md) | Dense (fully connected) layer |
| [mlp](examples/ai/mlp.md) | Multi-layer perceptron |
| [forward](examples/ai/forward.md) | Forward pass |

### Other

| Structure | Description |
|-----------|-------------|
| [hello](examples/hello.md) | Hello world example |

---

## Regenerating Documentation

To regenerate this documentation:

```bash
# Single file
bld doc file.bld -o docs/file.md

# All files
for f in src/*.bld; do
  bld doc "$f" -o "docs/src/$(basename "$f" .bld).md"
done
```

---

*Generated by traversing BLD structures. Structure IS computation.*
