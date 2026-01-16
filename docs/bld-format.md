# BLD File Format

Canonical reference for `.bld` file formatting.

## File Extension

`.bld`

## Structure

- One structure per file
- File name = structure name
- Empty file = leaf (path IS value)

## Syntax Elements

| Element | Syntax | Example |
|---------|--------|---------|
| Path/Link | `/` | `arch/x86/mov` |
| Dimension | `*` | `8*b` |
| Range | `..` | `char/a..z` |
| Field | `:` | `opcode: arch/x86/opcode/mov` |
| Alternative | `\|` | `0 \| 1` |
| Partition | newline | each line is a partition |

## Formatting Rules

- No trailing whitespace
- Single newline at end of file
- No blank lines between partitions
- Indentation: none (flat structure)

## Naming

- Lowercase
- Underscores for multi-word (`mod_rm.bld`)
- Or decompose into path (`mod/rm.bld`)

## What NOT to Include

- Traversal concepts (immediate, input, output)
- Computed values (traverser calculates these)
- Comments explaining traversal flow
- Boilerplate or declarations

## Constants Are OK

Constants that can't decompose further ARE structure:
- `0..1` - bit (indivisible)
- `0x05` - Intel's syscall opcode (Intel's definition)
- `60` - Linux's exit syscall (Linux's definition)

These are the Planck level of their domain. If you can't apply the 3 questions to break it down further, it's a valid constant.

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
# jcc.bld - partitions (position = value)
o
no
b
ae
e
ne
be
a
s
ns
p
np
l
ge
le
g
```

```
# mov.bld - composition
prefix: arch/x86/rex
opcode: arch/x86/opcode/mov
modrm: arch/x86/modrm
```

## The Principle

**Structure = B + D**
- B: What partitions exist (listing)
- D: What math applies (N*type)

**Traversal = L + flow**
- L: Path through structure
- Flow: Input/output during traversal

If a file describes WHERE values come from or WHAT bytes to emit, that's traversal.
If a file describes WHAT exists and HOW MUCH, that's structure.
