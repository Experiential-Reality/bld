# Claude Instructions for BLD

This repository contains the BLD (Boundary/Link/Dimension) language and interpreter.

## Core Principle

**Structure IS computation.** The traverser composes BLD structures to produce output.

## The Three Primitives

| Primitive | Meaning | Question |
|-----------|---------|----------|
| **B** (Boundary) | Partition, distinction | Where does behavior partition? |
| **L** (Link) | Connection, composition | What connects to what? |
| **D** (Dimension) | Repetition, positions | What repeats? |

## Key Insights

**Bit IS Planck length.** Size = 1 by definition. Indivisible.
```
bit:      B = 0 | 1           (size = 1)
byte:     D positions: 8      (8 bit positions)
u64:      D positions: 64     (64 bit positions = 8 bytes)
kilobyte: D positions: 1024   (1024 byte positions)
```

**D multiplies L, not B.** Cost = B + D × L
- Topological properties (B) are invariant
- Geometric properties (L) scale with dimension

**We decompose, traverser composes.**
- Express structures as decomposed parts
- Traverser follows paths and composes output

**Lowering IS composition.**
- No separate transformation pass
- Compose with arch-specific structure directly

## Repository Structure

```
bld/
├── src/                    # BLD structures
│   ├── bit.bld             # Fundamental unit (Planck length)
│   ├── byte.bld            # 8 bit positions
│   ├── u16.bld, u32.bld, u64.bld
│   ├── kilobyte.bld        # 1024 byte positions
│   ├── string.bld          # Variable length bytes (UTF-8)
│   ├── bld.bld             # BLD defining itself
│   ├── measure.bld         # Cost = B + D × L
│   ├── traverser.bld       # The one operation: compose
│   ├── arch/x86/           # x86 instruction encoding
│   │   ├── opcodes.bld     # Decomposed by bit structure
│   │   ├── modrm.bld, rex.bld, sib.bld
│   │   ├── arithmetic/     # test, cmp, add, inc
│   │   ├── jumps/          # je, jne, jmp
│   │   └── mov/            # rr, ri, rm, movzx
│   ├── format/elf/         # ELF64 format
│   │   ├── header.bld, ident.bld, phdr.bld
│   └── os/linux/x86/       # Linux x86-64
│       ├── syscall/        # exit, read, write, open, close
│       └── strings/        # strcmp
├── examples/               # Example structures
└── .claude/skills/bld/     # Claude skill files
```

## The Interpreter

The Python interpreter (`bld-py/`) is bootstrap. It implements:

1. **Parse** - .bld text → structure
2. **Traverse** - Visit B/L/D, compose output

Size comes from D positions. No variables, no emit primitives.

## Remember

> "The structure you find is the structure that exists. BLD doesn't impose—it reveals."
