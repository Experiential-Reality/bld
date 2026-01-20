# BLD

**Structural metaprogramming.** Describe structure. The traverser computes.

## The Insight

Line numbers ARE values. Structure IS computation.

```
syscall.bld:
read     # line 0 = value 0
write    # line 1 = value 1
open     # line 2 = value 2
...
exit     # line 60 = value 60
```

No parsing. No interpretation. Position IS meaning.

## Three Primitives

| Char | Name | Math | Type |
|------|------|------|------|
| `\|` | B (Boundary) | Sum | Choice between alternatives |
| `/` | L (Link) | Product | Connection to other structure |
| `\n` | D (Dimension) | Position | Constants to operate on |

**These three are mathematically proven irreducible.** No primitive can be expressed using the other two.

```
Cost = B + D × L
```

## How It Works

```
Input D  →  Traverser  →  Output D
(source)                  (bytes)
```

1. Write structure in `.bld` files
2. Traverser walks structure
3. Position accumulates (lines count, links multiply, boundaries sum)
4. Bytes emerge from accumulated position

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
8/b             # Dimension: 8 bits (count first, then unit)
const/type      # Link: path within tree
left|right      # Boundary: partition
pad             # Raw concept: value from position in parent D
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

- [Syntax Reference](docs/syntax.md) - Complete syntax documentation
- [bld-py](https://github.com/experiential-reality-org/bld-py) - The traverser
- [theory](https://github.com/experiential-reality-org/theory) - Mathematical foundations

## License

MIT
