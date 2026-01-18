# BLD Language Syntax

BLD (Boundary/Link/Dimension) is a structural language where the filesystem IS the syntax.

## Separators

Two separators with distinct meanings:

| Symbol | Meaning | Usage |
|--------|---------|-------|
| `|` | Boundary | Partitions options: `0|1`, `b|l` |
| `/` | Path | Separates path segments: `core/math/add` |

## Primitives

Three irreducible primitives:

| Primitive | Meaning | File |
|-----------|---------|------|
| **B** | Boundary (partition) | `b.bld` |
| **L** | Link (connection) | `l.bld` |
| **D** | Dimension (repetition) | `d.bld` |

## Core Definitions

### b.bld - The Bit
```
0|1
```
The fundamental unit. A boundary between 0 and 1.

### d.bld - Dimension
```
n*b
```
Repetition. `n` positions of `b`.

### l.bld - Link
```
path
```
A reference to another concept via path.

### string.bld - String
```
n*b
```
A sequence of bytes. Alias for dimension of bits.

### path.bld - Path
```
n*string
```
A sequence of strings. Separator `/` matched at traversal time.

### line.bld - Line
```
b|l
```
A line is either bytes (b) or a link (l). Boundary between literal and reference.

### file.bld - File
```
string
n*line
```
A file is a name (string) followed by contents (n lines).

### bld.bld - The Language
```
b
d
l
```
BLD itself: three links to the three primitives.

## File Format

Every `.bld` file follows this structure:

```
filename.bld     <- concept name (string)
─────────────
line 1           <- D position 1 (b|l)
line 2           <- D position 2 (b|l)
line 3           <- D position 3 (b|l)
...
```

- **Filename** = concept name
- **Lines** = dimension (D) positions
- **Line content** = bytes (b) OR link (l)
- **Directory** `/` = path separator

## Constants

A **const** is any file with:
- No links (only b, no l)
- Single dimension (just n*b)
- No boundary (no `|` in content)

Examples of consts:
```
ascii/H.bld:
0x48

ascii/newline.bld:
0x0A

os/linux/syscall/exit.bld:
60
```

Constants are leaf nodes - they produce bytes directly without composition.

## Links

A **link** is a path to another `.bld` file:
```
core/mathematics/add
```

This references `core/mathematics/add.bld`. The traverser:
1. Follows the path
2. Composes the target file
3. Returns the result

## Boundaries

The pipe `|` separates partitions:
```
0|1       <- bit: zero or one
b|l       <- line: bytes or link
yes|no    <- boolean
```

A boundary partitions a space into options.

## Dispatch Tables

A dispatch table maps conditions to actions:
```
n*(b|l)
```

Each line is `condition|action`:
```
classify.bld:
ascii/space|skip
ascii/tab|skip
ascii/newline|next
ascii/hash|comment
ascii/0|hex
digit|decimal
alpha|path
```

Order matters - first match wins. The traverser:
1. Reads input
2. Matches condition (left of `|`)
3. Follows action link (right of `|`)

## Dimensions

Dimension is repetition:
```
n*unit
```

Where `n` is the count and `unit` is what repeats.

Examples:
- `8*b` = byte (8 bits)
- `n*line` = file contents (n lines)
- `n*string` = path (n segments)
- `n*(b|l)` = dispatch table (n entries)

## Real Examples

### BLD defining itself

```
bld/
├── b.bld           # 0|1
├── d.bld           # n*b
├── l.bld           # path
├── string.bld      # n*b
├── path.bld        # n*string
├── line.bld        # b|l
├── file.bld        # string n*line
├── dispatch.bld    # n*(b|l)
└── bld.bld         # b d l
```

### Mathematics

```
core/mathematics/add.bld:
b
b
```

Two bit operands. Forward traversal = add, reverse = subtract.

```
core/mathematics/mult.bld:
b
b
```

Two bit operands. Forward traversal = multiply, reverse = divide.

### ASCII Character (const)

```
ascii/H.bld:
0x48
```

No links, single dimension, no boundary = const. Produces byte 0x48.

### String using links

```
program/cli/data/hello.bld:
ascii/H
ascii/e
ascii/l
ascii/l
ascii/o
```

Five links to ASCII concepts. Composes to "Hello".

### x86 Instruction (const)

```
arch/x86/syscall.bld:
0x0F
0x05
```

Two const bytes. Produces the syscall instruction.

### Parser Dispatch

```
program/cli/parse/classify.bld:
ascii/space|skip
ascii/tab|skip
ascii/newline|next
ascii/hash|comment
ascii/0|hex
digit|decimal
alpha|path
```

Input classification. Matches byte, follows handler.

### Composed Program

```
program/cli/x86/exit.bld:
arch/x86/rex/w
arch/x86/opcode/mov/ri32
arch/x86/modrm/ri/rax
os/linux/syscall/exit
arch/x86/imm32/pad
arch/x86/syscall
```

Links compose to x86 code that calls exit syscall.

## Traversal

The traverser walks the structure:

1. **Read file** - get lines
2. **For each line**:
   - If `|` present: dispatch (match left, follow right)
   - If `/` present: link (follow path)
   - Otherwise: const (emit bytes)
3. **Return** composed bytes

Traversal direction matters:
- Forward through `add.bld` = addition
- Reverse through `add.bld` = subtraction

## Composition

Composition is concatenation with structure:

```
A.bld:        B.bld:        A composed with B:
0x01          0x03          0x01
0x02                        0x02
                            0x03
```

When A links to B, B's bytes follow A's bytes.

## Summary

| Concept | Structure | Example |
|---------|-----------|---------|
| Bit | `0|1` | fundamental unit |
| Dimension | `n*b` | repetition |
| Link | `path` | reference |
| String | `n*b` | byte sequence |
| Path | `n*string` | segment sequence |
| Line | `b|l` | literal or reference |
| Dispatch | `n*(b|l)` | condition→action table |
| File | `string n*line` | name + contents |
| Const | file with only b | `0x48` |
| BLD | `b d l` | the language |

The filesystem IS the language:
- Files are concepts
- Paths (`/`) are links
- Pipes (`|`) are boundaries
- Lines are dimensions
