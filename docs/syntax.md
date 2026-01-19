# BLD Syntax

BLD expresses structure. The traverser computes.

## The Three Primitives

| Character | Primitive | Question |
|-----------|-----------|----------|
| `\|` | B (Boundary) | Where does behavior partition? |
| `/` | L (Link) | What connects to what? |
| `\n` | D (Dimension) | What repeats? |

```
Cost = B + D × L
```

## The 5 Structural Rules

1. **Links Cannot Cross Top-Level Trees** - Links only go DOWN within one tree. Collision during composition connects trees.
2. **Top-Level Concepts Require Composition** - Trees are incomplete alone. Compose them together.
3. **Empty Structures Are Meaningless** - The link implies existence. No empty files or directories.
4. **Position IS Value** - Line number in D structure = value.
5. **We Write Structure, Not Computation** - Don't think about bytes. Make structures match the rules. Math, not thinking.

## Dimension: `N/concept`

Count first, then unit. The traverser recognizes numeric first segment as dimension expression.

```
8/b         # 8 bits (byte)
64/b        # 64 bits
4/pad       # 4 padding bytes
1024/byte   # 1024 bytes
4/kilobyte  # 4 kilobytes
```

Proof: `6/pad` works, `pad/6` doesn't.
- `6/pad`: First segment `6` is numeric → dimension → 6 of pad
- `pad/6`: First segment `pad` is not numeric → path → tries to resolve pad/6

## Link: `concept/subconcept`

Path within a tree. Links only go DOWN.

```
const/type/exec     # within format/elf
syscall/exit        # within os/linux
hello/message       # decomposed structure for hello.bld
```

## Boundary: `left|right`

Partition behavior into two or more regions.

```
upper|lower         # case partition
0|1                 # bit partition
success|failure     # result partition
```

## Raw Concepts

A link to a missing file = raw concept. Value comes from position in parent D structure.

```
pad     # position 0 in parent D = value 0
exit    # position 60 in os/linux/syscall.bld = value 60
```

The link implies existence. Never create empty files.

## D Structures (Position IS Value)

Each line is a position. Line number = value.

```
os/linux/syscall.bld:
read        # position 0 = syscall 0
write       # position 1 = syscall 1
open        # position 2 = syscall 2
...
exit        # position 60 = syscall 60
```

## Cost-Driven Decisions

Use `Cost = B + D × L` to choose between structures.

```
# HIGH COST - duplication (D=26)
lower.bld:
a
b
c
...
z

# LOW COST - link (L=1)
lower.bld:
alphabet
```

Always minimize cost.

## Escaping

Concept characters must be escaped to express as content:

| Escape | Concept |
|--------|---------|
| `\|` | B (boundary) |
| `\/` | L (link) |
| `\\` | escape itself |

## Structure

Programs are top-level .bld files. Concept libraries decompose beneath them:

```
src/
  simple.bld      # Program - entry point
  hello.bld       # Program - entry point
  bld.bld         # Program describing BLD conceptual space
  hello/          # Decomposed structure for hello.bld
  os/             # Operating system (syscalls, fds)
  arch/           # Architecture (instructions, registers)
  format/         # Binary format (elf headers)
  encoding/       # Character encoding (ascii)
  lang/           # Language (english)
```

Concept libraries require composition. Only BLD primitives (`b.bld`, `d.bld`, `l.bld`, `bld.bld`) stand alone.

## Refactoring Methodology

For ANY structure, ask:

1. **B**: Where does behavior partition?
2. **L**: What connects to what?
3. **D**: What repeats?

Verify with `Cost = B + D × L`. If misaligned, restructure.

## Self-Reference

```
bld.bld:
b
l
d
```

BLD IS b, l, d. Boundary → Link → Dimension.
