# BLD

**Structural metaprogramming.** Describe structure. The traverser computes.

## How It Works

```
Input D  →  Traverser  →  Output D
(source)                  (bytes)
```

BLD files describe structure using three primitives. The traverser walks this structure, accumulates position, and produces bytes.

## The Three Primitives

| Character | Primitive | Forward | Reverse |
|-----------|-----------|---------|---------|
| `\|` | B (Boundary) | Sum | Difference |
| `/` | L (Link) | Product | Quotient |
| `\n` | D (Dimension) | Position | Position |

```
Cost = B + D × L
```

Traversal is bidirectional. Cost is conserved—refactoring makes hidden cost explicit.

## The Process

**Accumulation**: The traverser accumulates position as it walks:
- Each line (D) increments position
- Each link (L) multiplies through depth
- Boundaries (B) sum or select

**Link Resolution**: Links are relative to connected structures and resolve going UP the tree. At `/foo/bar`, a reference to `baz` tries `/foo/bar/baz`, then `/foo/baz`, then `/baz`. This is multidimensional accumulation—position is accumulated across all connected structures.

**Collision**: Links only go down within a tree. Separate trees connect through collision during composition. Raw concepts (e.g., `exit` at position 60) receive values from their position.

**Output**: The accumulated position becomes bytes.

## Quick Start

```bash
# Compose a .bld file to bytes
bld-py src/simple.bld output.bin
chmod +x output.bin
./output.bin

# View output as hex
bld-py src/simple.bld | xxd

# Compose an expression directly
bld-py -x "4/pad" | xxd
```

## Syntax

```
8/b             # Dimension: 8 bits
const/type      # Link: path within tree
left|right      # Boundary: partition
pad             # Raw concept: value from position
```

## Self-Reference

```
bld.bld:
b
l
d
```

BLD IS b, l, d.

## Learn More

- [bld-py](https://github.com/experiential-reality-org/bld-py) - The traverser
- [theory](https://github.com/experiential-reality-org/theory) - Mathematical foundations

## License

MIT
