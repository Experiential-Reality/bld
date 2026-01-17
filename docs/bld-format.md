# BLD Format Rules

Canonical reference for `.bld` file formatting.

## The Three Primitives

| Primitive | Meaning | Operator |
|-----------|---------|----------|
| **B** (Boundary) | Partition, distinction | newline (listing) |
| **L** (Link) | Connection, composition | `/` (path) |
| **D** (Dimension) | Repetition, scaling | `*` (multiplication) |

## The Three Questions

Before creating or modifying any BLD file, ask:

1. **Where does it partition?** (B) - What distinct parts exist?
2. **What connects?** (L) - What links to what?
3. **What repeats?** (D) - What pattern scales?

If you can't decompose further with these questions, you've reached the Planck level.

## Syntax Elements

| Element | Syntax | Example |
|---------|--------|---------|
| Partition | newline | each line is a partition |
| Link/Path | `/` | `arch/x86/mov` |
| Dimension | `*` | `8*b` |
| Range | `..` | `0..1` |
| Field | `:` | `W: b` |
| Alternative | `\|` | `a \| b \| c` |
| Constant | value | `0x05`, `60` |

## File Structure

- One structure per file
- File name = structure name
- Empty file = leaf (path IS value)
- Relative paths preferred (traverser resolves)

## Sequential vs Sparse

**Sequential (position = value):** Just list partitions
```
# jcc.bld - conditions 0-15, all defined
o
no
b
ae
...
```

**Sparse (gaps in values):** Use constants
```
# syscall.bld - not all numbers defined
read: 0
write: 1
exit: 60
```

## Constants

Constants that can't decompose further ARE structure:
- `0..1` - bit (indivisible Planck)
- `0x05` - Intel's syscall opcode
- `60` - Linux's exit syscall number

Ask: Can the 3 questions break this down further? If no, it's a valid constant.

## What IS Structure

- Partitions (B) - what distinct things exist
- Dimensions (D) - how things scale/repeat
- Composition (L) - how things connect

## What is NOT Structure

- **Traversal concepts** - input, output, immediate, direction
- **Computed values** - traverser calculates these
- **Semantic names** - arg0, number, fd (use position instead)
- **IO** - doesn't exist, only structure exists

## Key Principles

1. **Structure only** - no traversal in .bld files
2. **Position = value** for sequential data
3. **Constants** for sparse/Planck data
4. **Empty files** are valid leaves
5. **Relative paths** - traverser resolves
6. **Traverser IS compose** - it has no other structure
7. **IO doesn't exist** - there is only structure

## Formatting

- No trailing whitespace
- Single newline at end of file
- No blank lines between partitions
- No indentation (flat structure)
- Lowercase names
- Decompose multi-word into paths (`mod/rm` not `mod_rm`)

## Examples

```
# b.bld - the Planck
0..1
```

```
# byte.bld - dimension
8*b
```

```
# rex.bld - partitions with fields
W: b
R: b
X: b
B: b
```

```
# syscall.bld - ABI register sequence (position = arg number)
rax
rdi
rsi
rdx
r10
r8
r9
```

```
# mov.bld - sparse opcode constants
ri: 0xB8
rm: 0x8B
mr: 0x89
```

```
# exit.bld - instruction sequence
mov
xor
syscall
```

## The Cost Formula

```
Cost = B + D × L
```

- B = partitions (boundaries)
- D = dimension (scaling)
- L = links (composition)

Structure IS this formula. The traverser computes through it.
