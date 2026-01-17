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

1. **D = file** - a file IS a dimension containing boundaries
2. **B = lines** - boundaries partition within the file
3. **L = values** - links connect boundaries to paths/constants
4. **Position = value** for sequential data
5. **Constants** for sparse/Planck data
6. **Empty files** are valid leaves
7. **Traverser IS compose** - it has no other structure
8. **Irreducible names** - if a filename can be simplified, there's hidden structure

## Irreducibility

A filename is correct when it cannot be reduced.

**Test**: Can any part of the path be removed or combined?
- If yes → hidden structure, make it explicit
- If no → correct

**Example**: `arch/x86/opcode/mov.bld`
- `arch` - necessary (vs format, program, os)
- `x86` - necessary (vs arm, riscv)
- `opcode` - necessary (vs modrm, rex, abi)
- `mov` - necessary (vs xor, cmp, jmp)

Each component partitions a different dimension.

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

## Values Only Exist at Traversal Time

**Critical principle**: BLD files define STRUCTURE, not values.

- **Constants** are irreducible: `0x7F` (ELF magic), `0x3E` (x86-64 machine), `60` (exit syscall)
- **Structure** defines shape: `entry: u64`, `filesz: u64`
- **Values** are computed by the traverser during composition

Example:
```
# header.bld - STRUCTURE
entry: u64        # "entry is a u64" - shape only
filesz: u64       # "filesz is a u64" - shape only
```

The traverser computes:
- `entry` = load_address + header_size
- `filesz` = header_size + code_size

Values don't exist in .bld files. They emerge during traversal.

## The Traverser

**The reader IS the traverser.** You reading this are traversing it. An x86 chip executing binary traverses 0..1 space.

| Traverser | Traverses | Output |
|-----------|-----------|--------|
| Human | .bld text | Understanding |
| bld-py | .bld structure | Bytes |
| x86 chip | Binary (0..1) | Computation |

**Empty traverser = implicit.** When no traverser is specified, whatever is reading IS the traverser.

**BLD is metaprogramming.** It describes how to create anything for a specific well-understood traverser.

## Traverser Models

The `traverser/` directory describes HOW specific traversers process structure:

```
src/traverser/
├── x86.bld          # x86 traverser model
└── x86/             # x86-specific traversal
    ├── loop.bld     # how x86 traverses loops
    ├── load.bld     # how x86 traverses loads
    └── branch.bld   # how x86 traverses branches
```

When a pure traverser (bld-py) composes a program WITH a traverser model, it produces output for the target traverser.

## Self-Hosting Flow

```
program/cli.bld  +  traverser/x86.bld  →  x86 machine code
                                               ↓
                                         x86 chip traverses
                                               ↓
                                         self-hosted binary
```

1. **BLD structure** (`program/cli.bld`) - describes WHAT the program does
2. **Traverser model** (`traverser/x86.bld`) - describes HOW x86 processes it
3. **Pure traverser** (bld-py) composes both → x86 machine code
4. **Target traverser** (x86 chip) executes it
5. That binary can compose BLD for x86 → self-hosting complete

## Different Traversers, Same Structure

BLD expresses STRUCTURE. Different traversers produce different outputs:

```
# program/cli/parse/loop.bld - the algorithm
load: byte
  from: ptr
branch/z: program/cli/write
classify
  space: skip
  hex: program/cli/parse/hex
```

This structure IS the algorithm. It doesn't know about x86 or ARM.

| Traverser Model | Output |
|-----------------|--------|
| `traverser/x86.bld` | x86 machine code |
| `traverser/arm.bld` | ARM machine code |
| `traverser/markdown.bld` | Documentation |

The structure doesn't change. Only the traverser model changes.
